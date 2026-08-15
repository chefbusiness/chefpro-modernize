#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 11 — El plan AI Chef Miembro deja de ser gratis: 10 €/mes con 10.000
créditos (decisión de John, 2026-08-15). Barrido de los 7 locales de i18n.

    python3 fase11-plan-miembro-locales.py             # dry-run: enseña el diff
    python3 fase11-plan-miembro-locales.py --aplicar

Qué hace, por capas:
  1. pricing.plans.member — precio/uses/features derivados del hermano
     premium_pro del MISMO fichero (25→10, 85.000→10.000): así el formato de
     número y de moneda de cada idioma se hereda solo y no se hardcodea.
  2. tool*.pricing.plans[0] (las tarjetas de las 8 free tools) — igual, derivado
     de la fila premium de al lado.
  3. «55+» → «75+» en es/en y «50+» en fr/de/it/pt/nl. La asimetría es a
     propósito: las plataformas it/fr/de/pt/nl sirven 53-54 agentes (medido
     2026-08-14); escribir 75+ ahí vendería agentes que no existen. Cuando John
     complete esos catálogos, subirlas.
  4. De-gratis de los CTAs que llevan a la APP (lista explícita de rutas):
     quita la palabra «gratis» local y limpia espacios. Si el resultado queda en
     una sola palabra, se le añade « AI Chef Pro».
  5. Prosa reescrita desde .work/fase11-copy-<lang>.limpio.json (faq.q3/a3,
     schema.offers.miembro, subtítulos de landings), con {N} → 75+/50+.
  6. VERIFICADOR fail-closed: cualquier valor que siga conteniendo la palabra
     «gratis» local y NO esté en la lista KEEP (cosas que siguen siendo gratis
     de verdad: las free tools de la web, la micro-sesión de mentoría, la FAQ
     de ChatGPT, los 2 meses gratis del plan anual) aborta con la lista.
"""
import argparse, json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LOCALES = REPO / 'src/i18n/locales'
COPY = REPO / '.work'

LANGS = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl']
N_TOOLS = {'es': '75+', 'en': '75+', 'fr': '50+', 'de': '50+', 'it': '50+', 'pt': '50+', 'nl': '50+'}
PALABRAS_GRATIS = {
    # ⚠ «gratuito/gratuita» faltó en la primera versión y el verificador dejó
    # pasar el faq.a6 francés — mantener las declinaciones completas.
    'es': [r'gratis', r'gratuit[oa]s?'], 'en': [r'for free', r'free'],
    'fr': [r'gratuitement', r'gratuits?', r'gratuites?'],
    'de': [r'kostenlos(?:e[snr]?)?'], 'it': [r'gratuitamente', r'gratis', r'gratuit[oaie]'],
    'pt': [r'de graça', r'gratuitamente', r'grátis', r'gratuit[oa]s?'], 'nl': [r'gratis'],
}

# Rutas cuyo «gratis» se ELIMINA (CTAs que abren la app / hablan del plan).
STRIP = [
    r'^cta\.primary$', r'^footer\.try_free_button$', r'^pricing\.start_free$',
    r'^toolHub\.cta\.secondary$',
    r'^tool\w+\.cta_section\.primary$', r'^tool\w+\.tool\.try_free$',
    r'^landing\w+\.hero\.cta_primary$', r'^landing\w+\.cta_section\.(primary|secondary)$',
]
# Rutas que SIGUEN siendo gratis de verdad y no se tocan.
KEEP = [
    r'^tool\w+\.seo\.', r'^tool\w+\.hero\.badge$', r'^tool\w+\.pricing\.subtitle$',
    r'^tool\w+\.cta_section\.cta_primary$', r'^tool\w+\.hero\.', r'^tool\w+\.tool\.(?!try_free)',
    r'^tool\w+\.results?\.', r'^tool\w+\.form\.', r'^tool\w+\.other_tools',
    r'^toolHub\.(?!cta\.secondary)',
    r'^footer\.(nav_free_tools|free_tools_hub)$',
    r'^mentoriaOnline\.', r'^landingChatGPT\.faq\[1\]\.',
    r'^landingCostes\.pricing_section\.annual_note$',
    r'^pricing\.free_trial$',   # clave MUERTA (ningún componente la lee); se deja y se reporta
    r'^nav\.', r'^header\.',    # etiquetas «Herramientas Gratuitas» del menú (free tools)
    r'^announcement_bar\.',     # anuncia un post del blog («free and paid tools»), no el plan
    r'^tool\w+\.faq\[',         # «esta versión gratuita…» = la free tool de la web
    r'^tool\w+\.results\b',     # consejos del test («añade una carta QR gratuita»)
    r'^tool\w+\.breadcrumb_hub$',
    r'^tool\w+\.cta_section\.cta_secondary$',  # «ver todas las herramientas gratuitas»
]
# Claves de meta description cuya ÚLTIMA frase con «gratis» se sustituye por el
# sufijo local (copy.seo_sufijo): «…. Empieza gratis.» → «…. Empieza hoy.»
SEO_DESC = [r'^seo\.description$', r'^pages\.index\.seo_description$',
            r'^landing\w+\.seo\.description$', r'^landing\w+\.seo\.og_description$']
# Prosa reescrita entera: ruta → clave del fichero de copy.
PROSA = {
    'faq.q3': 'faq_q3',
    'faq.a3': 'faq_a3',
    'schema.offers.miembro': 'schema_miembro',
    'landingRestaurantes.faq[3].answer': 'landing_rest_faq',
    'landingChatGPT.pricing_section.subtitle': 'landing_chatgpt_sub',
    'landingCostes.pricing_section.subtitle': 'landing_costes_sub',
    'landingSoftwareGestion.pricing_section.subtitle': 'landing_escala_sub',
    'landingRecetas.pricing_section.subtitle': 'landing_escala_sub',
    'landingEscandallos.pricing_section.subtitle': 'landing_escandallos_sub',
}


def hojas(o, p=''):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from hojas(v, f'{p}.{k}' if p else k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from hojas(v, f'{p}[{i}]')
    else:
        yield p, o


def poner(d, ruta, val):
    segs = re.findall(r'([^.\[\]]+)|\[(\d+)\]', ruta)
    o = d
    for s in segs[:-1]:
        o = o[s[0] or int(s[1])]
    ult = segs[-1]
    o[ult[0] or int(ult[1])] = val


def swap_num(texto, de, a):
    """'85.000/mes' → '10.000/mes' respetando el separador local."""
    return re.sub(rf'\b{de}\b', a, texto, count=1)


def procesa(lang, aplicar):
    ruta_json = LOCALES / f'{lang}.json'
    d = json.loads(ruta_json.read_text(encoding='utf-8'))
    copy = json.loads((COPY / f'fase11-copy-{lang}.limpio.json').read_text()) if lang != 'es' \
        else {k: v for k, v in json.loads((COPY / 'fase11-copy-es.json').read_text()).items() if k != '_doc'}
    cambios, restos = [], []

    # 1. plan member derivado del premium_pro hermano
    pl = d['pricing']['plans']
    antes = (pl['member']['price'], pl['member']['uses'])
    pl['member']['price'] = swap_num(pl['premium_pro']['price'], '25', '10')
    pl['member']['uses'] = swap_num(pl['premium_pro']['uses'], '85', '10')
    feats = pl['member']['features']
    claves_f = list(feats) if isinstance(feats, dict) else range(len(feats))
    fp = pl['premium_pro']['features']
    fp1 = fp['1'] if isinstance(fp, dict) else fp[1]
    feats[claves_f[1]] = swap_num(fp1, '85', '10')
    cambios.append(f'member: {antes} → ({pl["member"]["price"]}, {pl["member"]["uses"]}) · feat1={feats[claves_f[1]]}')

    # 2. tarjetas de plan de las free tools
    nombre_corto = re.sub(r'^AI Chef ', '', pl['member']['name'])
    for tk, tv in d.items():
        if tk.startswith('tool') and isinstance(tv, dict) and 'pricing' in tv and 'plans' in tv.get('pricing', {}):
            planes = tv['pricing']['plans']
            if len(planes) >= 2:
                p0, p1 = planes[0], planes[1]
                p0['name'] = nombre_corto
                p0['price'] = swap_num(p1['price'], '25', '10')
                p0['uses'] = swap_num(p1['uses'], '85', '10')
                cambios.append(f'{tk}.pricing.plans[0] → {p0["name"]} · {p0["price"]} · {p0["uses"]}')

    # 3 + 4 + 5 sobre todas las hojas
    n = N_TOOLS[lang]
    strip_re = [re.compile(p) for p in STRIP]
    keep_re = [re.compile(p) for p in KEEP]
    seo_re = [re.compile(p) for p in SEO_DESC]
    palabras = re.compile(r'(?:\s|^)(' + '|'.join(PALABRAS_GRATIS[lang]) + r')(?=\s|[.,;:!]|$)', re.I)
    restos_manual = json.loads((COPY / f'fase11-restos-{lang}.json').read_text()) \
        if (COPY / f'fase11-restos-{lang}.json').exists() else {}
    for ruta, val in list(hojas(d)):
        if not isinstance(val, str):
            continue
        nuevo = val
        if '55+' in nuevo:
            nuevo = nuevo.replace('55+', n)
        if ruta in restos_manual:
            nuevo = restos_manual[ruta].replace('{N}', n)
        elif ruta in PROSA:
            nuevo = copy[PROSA[ruta]].replace('{N}', n)
        elif any(rx.search(ruta) for rx in seo_re) and palabras.search(nuevo):
            frases = re.split(r'(?<=[.!])\s+', nuevo)
            frases = [f for f in frases if not palabras.search(f' {f} ')]
            nuevo = ' '.join(frases).strip()
            suf = copy['seo_sufijo']
            if suf not in nuevo:
                nuevo = (nuevo + ' ' + suf).strip()
        elif any(rx.search(ruta) for rx in strip_re) and palabras.search(nuevo):
            nuevo = palabras.sub('', nuevo)
            nuevo = re.sub(r'\s{2,}', ' ', nuevo).strip()
            nuevo = re.sub(r'\s+([.,;:!])', r'\1', nuevo)
            if ' ' not in nuevo.strip():
                nuevo = nuevo.strip() + ' AI Chef Pro'
        if nuevo != val:
            cambios.append(f'{ruta}: {val[:60]!r} → {nuevo[:60]!r}')
            poner(d, ruta, nuevo)

    # 6. verificador fail-closed
    for ruta, val in hojas(d):
        if isinstance(val, str) and palabras.search(f' {val} '):
            if not any(rx.search(ruta) for rx in keep_re):
                restos.append(f'{lang}:{ruta} = {val}')

    if aplicar:
        ruta_json.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return cambios, restos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--aplicar', action='store_true')
    ap.add_argument('--exportar-restos', action='store_true',
                    help='vuelca los valores sin clasificar a .work/fase11-pendientes-<lang>.json '
                         'para reescribirlos con bridge y guardarlos como fase11-restos-<lang>.json')
    args = ap.parse_args()
    total_restos = []
    pendientes = {}
    for lang in LANGS:
        cambios, restos = procesa(lang, args.aplicar)
        if args.exportar_restos:
            pendientes[lang] = restos
        print(f'—— {lang}: {len(cambios)} cambios')
        for c in cambios[:12]:
            print(f'   {c}')
        if len(cambios) > 12:
            print(f'   … y {len(cambios) - 12} más')
        total_restos += restos
    if args.exportar_restos:
        for lang, rs in pendientes.items():
            if rs:
                out = {}
                for r in rs:
                    ruta, val = r.split(' = ', 1)
                    out[ruta.split(':', 1)[1]] = val
                (COPY / f'fase11-pendientes-{lang}.json').write_text(
                    json.dumps(out, ensure_ascii=False, indent=1))
                print(f'→ .work/fase11-pendientes-{lang}.json ({len(out)})')
        return
    if total_restos:
        print(f'\n⛔ {len(total_restos)} valores con «gratis» SIN clasificar (ni STRIP ni KEEP):')
        for r in total_restos[:25]:
            print(f'   · {r}')
        sys.exit(1)
    print('\n✅ sin restos fuera de la lista KEEP' + ('' if args.aplicar else ' (dry-run: nada escrito)'))


if __name__ == '__main__':
    main()
