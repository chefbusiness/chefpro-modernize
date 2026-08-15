#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 11 (blog) — Quita del corpus del blog (es/en/it) la promesa del plan
gratis de AI Chef Pro y actualiza el leitmotiv 55+ → 75+ (es/en; el blog it no
lo usa). NO toca las ofertas de OTROS productos del grupo (Miselup «Plan gratis
para siempre», Timlup «Pruébalo gratis») — cada CTA se ancla a su href.

    python3 fase11-plan-miembro-blog.py            # dry-run + informe
    python3 fase11-plan-miembro-blog.py --aplicar

A cada post tocado se le sube modDate a la fecha del día (después: purgar
.astro, regen-lastmod y build — gotcha del caché de frontmatter).

El banner promo-aichefpro-3.jpeg (468 referencias) lleva «PRUEBA GRATIS» y
«55+» EN LOS PÍXELES: se regenera aparte con la skill de imágenes y se pisa en
la misma ruta; aquí solo se actualizan alt y UTM.
"""
import argparse, datetime, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BLOG = REPO / 'astro-site/src/content/blog'
HOY = datetime.date.today().isoformat()

# (regex_o_literal, reemplazo) por idioma. Orden: largos primero.
REEMPLAZOS = {
    'es': [
        # Tarjeta AI Chef Pro del bloque ecosistema (anclada por href app.aichef.pro)
        (re.compile(r'(<a href="https://app\.aichef\.pro/?[^"]*"[^>]*>)Empieza gratis →'), r'\1Empieza hoy →'),
        (re.compile(r'(<a href="https://(?:app\.)?aichef\.pro[^"]*"[^>]*>)Empezar Gratis(?: Ahora)?<'), r'\1Empezar Ahora<'),
        (re.compile(r'(<a href="https://(?:app\.)?aichef\.pro/?[^"]*"[^>]*>)Probar Gratis<'), r'\1Probar AI Chef Pro<'),
        ('Prueba gratis AI Chef Pro aquí en', 'Prueba AI Chef Pro aquí en'),
        ('Prueba Gratis <strong>AI Chef Pro</strong>', 'Prueba <strong>AI Chef Pro</strong>'),
        (re.compile(r'Prueba AI Chef Pro [Gg]ratis'), 'Prueba AI Chef Pro'),
        ('[probar AI Chef Pro gratis]', '[probar AI Chef Pro]'),
        ('[Empieza gratis en AI Chef Pro]', '[Empieza hoy en AI Chef Pro]'),
        ('- **Plan gratuito**: 3.000 créditos al mes, sin tarjeta.',
         '- **Plan Miembro**: 10 € al mes con 10.000 créditos.'),
        ('¿Cuánto cuesta AI Chef Pro y qué incluye el plan gratuito?',
         '¿Cuánto cuesta AI Chef Pro y qué incluye el plan Miembro?'),
        (re.compile(r'AI Chef Pro ofrece un plan gratuito con 3\.000 créditos al mes, sin (?:necesidad de )?tarjeta[.,]?'),
         'AI Chef Pro parte del plan Miembro: 10 € al mes con 10.000 créditos.'),
        ('reúne 55+ herramientas', 'reúne 75+ herramientas'),
        ('¿Es gratis empezar con AI Chef Pro?', '¿Cuánto cuesta empezar con AI Chef Pro?'),
        ('Comenzar Gratis Ahora', 'Comenzar Ahora'),
        ('Explorar AI Chef Pro Gratis', 'Explorar AI Chef Pro'),
        ('Crear Cuenta Gratis en AI Chef Pro', 'Crear Cuenta en AI Chef Pro'),
        # Lineup de precios FÓSIL (Pro 10€/Premium 15€ ya no existen): entero al actual
        ('Miembro Gratis • Pro 10€/mes • Premium 15€/mes • Premium Pro 25€/mes • Premium Plus 50€/mes',
         'Miembro 10€/mes • Premium Pro 25€/mes • Premium Plus 50€/mes • Premium Max 95€/mes'),
        ('| Gratuito | 0 € | 3.000 |', '| Miembro | 10 € | 10.000 |'),
        ('| Gratuito | 3.000 | 0 € (sin tarjeta) |', '| Miembro | 10.000 | 10 €/mes |'),
        # Banner congelado: alt y UTM (el jpeg se pisa aparte con la misma ruta)
        ('Promo Prueba Gratis AI Chef Pro', 'Promo AI Chef Pro'),
        ('utm_campaign=prueba-gratis', 'utm_campaign=empieza-hoy'),
        ('utm_content=bloque-prueba-gratis', 'utm_content=bloque-empieza-hoy'),
    ],
    'en': [
        (re.compile(r'(<a href="https://enapp\.aichef\.pro/?[^"]*"[^>]*>)\s*Start [Ff]ree(?: today)?(?: —[^<]*)?<'), r'\1Start today<'),
        (re.compile(r'Start free with 10 uses/month'), 'Start with the Member plan (€10/month)'),
        (re.compile(r'Start free — 10 uses/month'), 'Member plan — €10/month'),
        (re.compile(r'Start free today'), 'Start today'),
        (re.compile(r'\bStart free\b'), 'Start today'),
        (re.compile(r'5 free credits to start\s*•\s*'), ''),
        (re.compile(r'•\s*5 free credits to start'), ''),
        (re.compile(r'55\+ AI tools from €25/month'), '75+ AI tools from €10/month'),
        (re.compile(r'No credit card required\.?'), 'Cancel anytime.'),
        (re.compile(r'\s*•\s*No credit card\b'), ' • Cancel anytime'),
        ('free plan (AI Chef Member)', 'AI Chef Member plan (€10/month)'),
        (re.compile(r'AI Chef Pro has a free plan[^.]*\.'),
         'AI Chef Pro starts with the Member plan: €10/month with 10,000 credits.'),
        (re.compile(r'\bfree plan\b'), 'Member plan (€10/month)'),
        ('55+', '75+'),
    ],
    'it': [
        ('Puoi provarlo gratis su', 'Puoi provarlo su'),
    ],
}

# El verificador solo mira «gratis» CERCA de la marca o del plan — el blog habla
# legítimamente de postres gratis, herramientas web gratuitas ajenas, etc.
CERCA = 120
MARCA = re.compile(r'AI Chef|aichef\.pro|plan|crédit|credit', re.I)
PALABRA = {'es': re.compile(r'(?:\s|^|>|«|\[)(gratis|gratuit[oa]s?)\b', re.I),
           'en': re.compile(r'(?:\s|^|>|\[)(free)\b', re.I),
           'it': re.compile(r'(?:\s|^|>|«|\[)(gratis|gratuit[oaie])\b', re.I)}
# Dominios de productos hermanos cuya oferta gratis NO es asunto de este barrido.
HERMANOS = re.compile(r'miselup\.pro|timlup\.pro|gastroseo|gastrolocal|hosply|ingredientsindex|chefbusiness')
WHITELIST_EN = [r'gluten-free', r'dairy-free', r'sugar-free', r'alcohol-free', r'lactose-free',
                r'allergen-free', r'nut-free', r'free-range', r'risk-free', r'free up', r'frees up',
                r'free items', r'free dessert', r'free delivery', r'free shipping', r'hands-free',
                r'free-form', r'contact-free', r'error-free', r'stress-free', r'waste-free']


def procesa(f, lang, aplicar):
    t = f.read_text(encoding='utf-8')
    original = t
    for patron, nuevo in REEMPLAZOS[lang]:
        if isinstance(patron, str):
            t = t.replace(patron, nuevo)
        else:
            t = patron.sub(nuevo, t)
    restos = []
    for m in PALABRA[lang].finditer(t):
        ctx = t[max(0, m.start() - CERCA):m.end() + CERCA].replace('\n', ' ')
        if not MARCA.search(ctx):
            continue
        if HERMANOS.search(ctx):
            continue
        if lang == 'en' and any(re.search(w, ctx, re.I) for w in WHITELIST_EN):
            continue
        restos.append((f.name, ctx[max(0, len(ctx)//2 - 90):len(ctx)//2 + 90]))
    if t != original:
        t2 = re.sub(r'^modDate: \d{4}-\d{2}-\d{2}$', f'modDate: {HOY}', t, count=1, flags=re.M)
        if aplicar:
            f.write_text(t2, encoding='utf-8')
        return True, restos
    return False, restos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--aplicar', action='store_true')
    args = ap.parse_args()
    total_restos = []
    for lang in ['es', 'en', 'it']:
        tocados = 0
        for f in sorted((BLOG / lang).glob('*.md')):
            cambiado, restos = procesa(f, lang, args.aplicar)
            tocados += cambiado
            total_restos += [(lang,) + r for r in restos]
        print(f'—— {lang}: {tocados} posts modificados')
    if total_restos:
        vistos = set()
        print(f'\n⚠ {len(total_restos)} contextos con «gratis» cerca de la marca/plan — revisar:')
        for lang, fn, ctx in total_restos:
            clave = re.sub(r'\s+', ' ', ctx)[:80]
            if clave in vistos:
                continue
            vistos.add(clave)
            print(f'   [{lang}] {fn}: …{ctx}…')
            if len(vistos) >= 40:
                print('   …')
                break
        sys.exit(1)
    print('\n✅ limpio' + ('' if args.aplicar else ' (dry-run)'))


if __name__ == '__main__':
    main()
