#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CRO home (Keak, 20-sep-2026) — funde keak-copy.<lang>.json en src/i18n/locales/<lang>.json
y, con --check, hace de GATE de i18n.

Qué hace al fundir (idempotente):
  1. Deep-merge de las claves v2_* del copy traducido dentro del JSON del idioma.
  2. Para fr/de/it/pt/nl: «75+» → «50+» en las cadenas nuevas (esas plataformas sirven
     53-54 agentes y su hero ya anuncia 50+; ver Hero.astro / CATALOGO_ITALIANO_PENDIENTE.md).
  3. hero.v2_business_types = hero.business_types sin su primer elemento («Gestión»/
     «Management»: encajaba en «Transforma tu Gestión» pero no en «…en tu Gestión»).
     El primero que queda es «Restaurante»: es lo que Google lee en el H1 SSR.
     Y hero.v2_business_prefixes = el ARTÍCULO con género que va delante en de/it/pt
     («in Ihrer» / «nella tua» / «na sua»), lista PARALELA a la anterior y con el
     mismo número de elementos; en es/en/fr/nl son 11 cadenas vacías. El artículo
     va en su propia clave porque en el H1 se pinta FUERA del <span> dorado.
  4. pricing.plans.member.period = pricing.plans.premium_pro.period si falta (la tarjeta
     Member v2 muestra «/mes» como las demás).

Qué comprueba --check (falla con código 1):
  · toda clave v2 del inglés existe en los 7 idiomas y ninguna vale ""
  · los dígitos de cada cadena coinciden con el inglés (salvo el 75+→50+ documentado)
  · cero caracteres de otro alfabeto; «AI Chef Pro» intacto donde el inglés lo lleva
  · hero.v2_business_types y hero.v2_business_prefixes tienen 11 elementos en los 7
    idiomas (y por tanto rotan en sincronía: mismo índice = artículo + sustantivo)
Uso:
    python3 merge-keak-copy.py --lang en          # una
    python3 merge-keak-copy.py --todos            # las 7 que tengan keak-copy.<lang>.json
    python3 merge-keak-copy.py --check            # gate
"""
import argparse, json, re, sys
from pathlib import Path

DIR = Path(__file__).parent
LOCALES = DIR.parent.parent / 'src' / 'i18n' / 'locales'
LANGS = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl']
SECUNDARIOS = {'fr', 'de', 'it', 'pt', 'nl'}
SOSPECHOSO = re.compile(
    r'[　-鿿Ѐ-ӿ가-힯؀-ۿ֐-׿฀-๿぀-ヿ]')

# ─── Correcciones HUMANAS sobre lo que devolvió el bridge (20-sep-2026) ───────────
# Pasaron todos los gates automáticos y aun así estaban mal; por eso viven aquí,
# documentadas, y no en un retoque a mano del JSON que nadie recordaría:
#  · «Member» sin localizar en chip y CTA (el plan se llama AI Chef Miembro/Membre/
#    Mitglied/Membro/Lid en cada idioma): se deriva de pricing.plans.member.name.
#  · «escandallos» es español: en FR/IT/PT no existe (fiche technique / calcoli di
#    food cost / ficha técnica).
#  · «el pase» de cocina: FR «le passe» y PT «o passe» son correctos; IT dice «il
#    pass», DE «der Pass» y NL «de pas».
#  · DE/IT/PT tienen artículo con GÉNERO delante del negocio («in Ihrer Pizzeria»
#    pero «in Ihrem Restaurant»): el prefijo del H1 se acorta y el artículo se
#    emite en hero.v2_business_prefixes, que el hero pinta FUERA del <span>
#    dorado (el color de marca y el subrayado son del NOMBRE del negocio, no de
#    la preposición). ES/EN/FR/NL no lo necesitan (tu/your/votre/uw).
OVERRIDES = {
    'es': {'pricing.plans.member.v2_cta': 'Empezar como Miembro'},
    'fr': {'pricing.plans.member.v2_cta': 'Commencer avec Membre',
           'pricing.plans.member.v2_hint': '≈ 200 recettes ou 100 fiches techniques'},
    'de': {'pricing.plans.member.v2_cta': 'Als Mitglied starten',
           'hero.v2_title_prefix': 'Senken Sie die Zutatenkosten',
           'showcase.v2_business_title_suffix': 'senken – mit Tools, die für den Pass gebaut wurden.'},
    'it': {'pricing.plans.member.v2_cta': 'Inizia con Membro',
           'pricing.plans.member.v2_hint': '≈ 200 ricette o 100 calcoli di food cost',
           'hero.v2_title_prefix': 'Abbatti i costi degli ingredienti',
           'showcase.v2_business_title_suffix': 'con strumenti costruiti per il pass.'},
    'pt': {'pricing.plans.member.v2_cta': 'Começar com Membro',
           'pricing.plans.member.v2_hint': '≈ 200 receitas ou 100 fichas técnicas',
           'hero.v2_title_prefix': 'Reduza os custos de ingredientes'},
    'nl': {'pricing.plans.member.v2_cta': 'Beginnen als Lid',
           'showcase.v2_business_title_suffix': 'met tools gebouwd voor de pas.'},
}
# Palabra rotatoria de los idiomas con género, como PARES (artículo, sustantivo):
# 11 elementos, mismo orden que hero.business_types sin «Gestión». El artículo sale
# a hero.v2_business_prefixes y el sustantivo a hero.v2_business_types, que es lo
# único que se pinta en dorado. Géneros comprobados a mano.
LISTAS_V2 = {
    'de': [('Ihr', 'Restaurant'), ('Ihr', 'Catering'), ('Ihre', 'Pizzeria'),
           ('Ihre', 'Burger-Bar'), ('Ihre', 'Bäckerei'), ('Ihre', 'Konditorei'),
           ('Ihre', 'Chocolaterie'), ('Ihre', 'Eisdiele'), ('Ihre', 'Dark Kitchen'),
           ('Ihr', 'Café'), ('Ihr', 'Brunch')],
    'it': [('il tuo', 'Ristorante'), ('il tuo', 'Catering'), ('la tua', 'Pizzeria'),
           ('la tua', 'Hamburgheria'), ('la tua', 'Panetteria'), ('la tua', 'Pasticceria'),
           ('la tua', 'Cioccolateria'), ('la tua', 'Gelateria'), ('la tua', 'Dark Kitchen'),
           ('la tua', 'Caffetteria'), ('il tuo', 'Brunch')],
    'pt': [('o seu', 'Restaurante'), ('o seu', 'Catering'), ('a sua', 'Pizzaria'),
           ('a sua', 'Hamburgueria'), ('a sua', 'Padaria'), ('a sua', 'Confeitaria'),
           ('a sua', 'Chocolataria'), ('a sua', 'Sorveteria'), ('a sua', 'Dark Kitchen'),
           ('a sua', 'Cafeteria'), ('o seu', 'Brunch')],
}

# ─── Decisiones de John sobre el preview (20-sep-2026, tarde) ─────────────────────
# H1 = opción A («Crea, gestiona y haz crecer tu {X} con AI Chef Pro»): tres verbos =
# tres familias de agentes (creatividad · gestión · marketing) y tres perfiles (chefs,
# pasteleros y panaderos · gerentes y dueños · emprendedores). Sustituye al «Cut
# ingredient costs…» de Keak, que reducía 75+ agentes a un solo beneficio. En DE/IT/PT el
# negocio pasa a objeto directo, así que el artículo (LISTAS_V2) es nominativo.
# El gancho del coste no se pierde: baja al subtítulo, que además se amplía a recetas y
# marketing (idea de John: que no todo suene a reducir costes). Y el subtítulo termina en
# «restaurantes y negocios de hostelería», no «cocinas profesionales»: John (20-sep, noche)
# quiere alejarse de «SaaS para cocinas» hacia el negocio de hostelería en general.
# Hint del plan Miembro: «≈ 200 recipes or 100 cost calcs» lo inventó Keak y no se
# puede verificar contra la plataforma → hint cualitativo con la misma escalera que
# los otros planes (una partida → carta completa → multisede). Decisión delegada.
# Prueba social (John, 20-sep noche): «recetas, procesos y soluciones generadas» y «de más de
# 90 países» — GSC 90 d: 145 países con clic, 92 con ≥5 clics; se pone 90+ (conservador).
# El 764+ de chefs pasa a ser dinámico (lib/social-counts.ts), como el contador de soluciones.
# Franja de cifras (SocialProofStrip): «1 nuevo agente cada semana» ya no es verdad → «15+
# herramientas para conectar (Gmail, Sheets, Outlook…)» vía Composio (16 plataformas reales).
DECISIONES_JOHN = {
    'en': {'stats.v2_integrations_label': 'Tools to Connect (Gmail, Sheets, Outlook…)',
           'hero.v2_social_count': 'recipes, processes & solutions generated',
           'hero.v2_social_countries': 'from 90+ countries',
           'hero.v2_title_prefix': 'Create, run and grow your', 'hero.v2_title_suffix': 'with',
           'hero.v2_subtitle': 'Automate recipes, food cost, waste, menus and marketing with 75+ AI agents built for restaurants and hospitality businesses.',
           'pricing.plans.member.v2_hint': '≈ a month of recipes, costings and menus for one station'},
    'es': {'stats.v2_integrations_label': 'Herramientas para Conectar (Gmail, Sheets, Outlook…)',
           'hero.v2_social_count': 'recetas, procesos y soluciones generadas',
           'hero.v2_social_countries': 'de más de 90 países',
           'hero.v2_title_prefix': 'Crea, gestiona y haz crecer tu', 'hero.v2_title_suffix': 'con',
           'hero.v2_subtitle': 'Automatiza recetas, food cost, mermas, cartas y marketing con más de 75 agentes de IA diseñados para restaurantes y negocios de hostelería.',
           'pricing.plans.member.v2_hint': '≈ un mes de recetas, escandallos y cartas para una partida'},
    'fr': {'stats.v2_integrations_label': 'Outils à Connecter (Gmail, Sheets, Outlook…)',
           'hero.v2_social_count': 'recettes, procédures et solutions générées',
           'hero.v2_social_countries': 'dans plus de 90 pays',
           'hero.v2_title_prefix': 'Créez, gérez et développez votre', 'hero.v2_title_suffix': 'avec',
           'hero.v2_subtitle': 'Automatisez recettes, food cost, pertes, cartes et marketing avec 50+ agents IA conçus pour les restaurants et les entreprises de l\'hôtellerie-restauration.',
           'pricing.plans.member.v2_hint': '≈ un mois de recettes, fiches techniques et cartes pour un poste'},
    'de': {'stats.v2_integrations_label': 'Tools zum Verbinden (Gmail, Sheets, Outlook…)',
           'hero.v2_social_count': 'generierte Rezepte, Prozesse & Lösungen',
           'hero.v2_social_countries': 'aus über 90 Ländern',
           'hero.v2_title_prefix': 'Kreieren, steuern und ausbauen:', 'hero.v2_title_suffix': 'mit',
           'hero.v2_subtitle': 'Automatisieren Sie Rezepte, Food Cost, Warenverluste, Speisekarten und Marketing mit 50+ KI-Agenten für Restaurants und Gastronomiebetriebe.',
           'pricing.plans.member.v2_hint': '≈ ein Monat Rezepte, Kalkulationen und Speisekarten für einen Posten'},
    'it': {'stats.v2_integrations_label': 'Strumenti da Collegare (Gmail, Sheets, Outlook…)',
           'hero.v2_social_count': 'ricette, processi e soluzioni generate',
           'hero.v2_social_countries': 'in oltre 90 paesi',
           'hero.v2_title_prefix': 'Crea, gestisci e fai crescere', 'hero.v2_title_suffix': 'con',
           'hero.v2_subtitle': 'Automatizza ricette, food cost, sprechi, menu e marketing con 50+ agenti AI pensati per ristoranti e aziende della ristorazione.',
           'pricing.plans.member.v2_hint': '≈ un mese di ricette, food cost e menu per una partita'},
    'pt': {'stats.v2_integrations_label': 'Ferramentas para Ligar (Gmail, Sheets, Outlook…)',
           'hero.v2_social_count': 'receitas, processos e soluções geradas',
           'hero.v2_social_countries': 'de mais de 90 países',
           'hero.v2_title_prefix': 'Crie, gira e faça crescer', 'hero.v2_title_suffix': 'com',
           'hero.v2_subtitle': 'Automatize receitas, food cost, desperdício, ementas e marketing com 50+ agentes de IA criados para restaurantes e negócios de hotelaria e restauração.',
           'pricing.plans.member.v2_hint': '≈ um mês de receitas, fichas técnicas e ementas para um cozinheiro'},
    'nl': {'stats.v2_integrations_label': 'Tools om te Koppelen (Gmail, Sheets, Outlook…)',
           'hero.v2_social_count': 'recepten, processen & oplossingen gegenereerd',
           'hero.v2_social_countries': 'uit meer dan 90 landen',
           'hero.v2_title_prefix': 'Creëer, beheer en laat uw', 'hero.v2_title_suffix': 'groeien met',
           'hero.v2_subtitle': "Automatiseer recepten, food cost, verspilling, menu's en marketing met 50+ AI-agents ontwikkeld voor restaurants en horecabedrijven.",
           'pricing.plans.member.v2_hint': "≈ een maand recepten, kostprijzen en menu's voor één kok"},
}


def poner(d, path, val):
    toks = path.split('.')
    cur = d
    for k in toks[:-1]:
        cur = cur.setdefault(k, {})
    cur[toks[-1]] = val


def pares(o, path='', acc=None):
    acc = [] if acc is None else acc
    if isinstance(o, dict):
        for k in sorted(o):
            pares(o[k], f'{path}.{k}' if path else k, acc)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            pares(v, f'{path}[{i}]', acc)
    elif isinstance(o, str):
        acc.append((path, o))
    return acc


def resolve(d, path):
    cur = d
    for tok in re.split(r'\.|\[(\d+)\]', path):
        if tok is None or tok == '':
            continue
        if isinstance(cur, list):
            cur = cur[int(tok)] if int(tok) < len(cur) else None
        elif isinstance(cur, dict):
            cur = cur.get(tok)
        else:
            return None
        if cur is None:
            return None
    return cur


def deep_merge(dst, src):
    for k, v in src.items():
        if isinstance(v, dict) and isinstance(dst.get(k), dict):
            deep_merge(dst[k], v)
        else:
            dst[k] = v


def rebaja_agentes(o):
    if isinstance(o, dict):
        return {k: rebaja_agentes(v) for k, v in o.items()}
    if isinstance(o, list):
        return [rebaja_agentes(v) for v in o]
    if isinstance(o, str):
        return o.replace('75+', '50+')
    return o


def cargar(lang):
    p = LOCALES / f'{lang}.json'
    return p, json.loads(p.read_text(encoding='utf-8'))


def guardar(p, d):
    # Mismo formato que el resto del fichero (2 espacios, sin escapar unicode).
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def fundir(lang):
    src = DIR / f'keak-copy.{lang}.json'
    if not src.exists():
        print(f'  – {lang}: no hay keak-copy.{lang}.json (pendiente de traducir)')
        return False
    copy = json.loads(src.read_text(encoding='utf-8'))
    if lang in SECUNDARIOS:
        copy = rebaja_agentes(copy)
    for ruta, val in OVERRIDES.get(lang, {}).items():
        poner(copy, ruta, val)
    for ruta, val in DECISIONES_JOHN.get(lang, {}).items():
        poner(copy, ruta, val)
    p, d = cargar(lang)
    deep_merge(d, copy)
    # Nombre corto del plan de entrada = su nombre localizado sin «AI Chef »
    short = d['pricing']['plans']['member']['name'].replace('AI Chef ', '').strip()
    d['pricing']['plans']['member']['v2_short'] = short
    bt = d['hero'].get('business_types') or []
    pares_v2 = LISTAS_V2.get(lang)
    if pares_v2:
        tipos = [sust for _, sust in pares_v2]
        prefijos = [art for art, _ in pares_v2]
    else:
        tipos = bt[1:] if len(bt) > 1 else list(bt)
        # es/en/fr/nl: «tu/your/votre/uw» ya va en v2_title_prefix, sin género.
        prefijos = [''] * len(tipos)
    d['hero']['v2_business_types'] = tipos
    d['hero']['v2_business_prefixes'] = prefijos
    member = d['pricing']['plans']['member']
    if not member.get('period'):
        member['period'] = d['pricing']['plans']['premium_pro'].get('period', '')
    guardar(p, d)
    print(f'  ✓ {lang}: {len(pares(copy))} cadenas fundidas · v2_business_types={len(tipos)}'
          f' · v2_business_prefixes={len(prefijos)}'
          f'{" (con artículo)" if pares_v2 else " (vacíos)"}')
    return True


def check():
    en_copy = json.loads((DIR / 'keak-copy.en.json').read_text(encoding='utf-8'))
    # El inglés de referencia es el de Keak MÁS las decisiones de John (H1, subtítulo, hint).
    for ruta, val in DECISIONES_JOHN.get('en', {}).items():
        poner(en_copy, ruta, val)
    claves = pares(en_copy)
    errores = []
    for lang in LANGS:
        _, d = cargar(lang)
        for ruta, en in claves:
            v = resolve(d, ruta)
            if not isinstance(v, str) or not v.strip():
                errores.append(f'{lang}: falta o vacía {ruta}')
                continue
            if SOSPECHOSO.search(v):
                errores.append(f'{lang}: alfabeto ajeno en {ruta}: {v[:50]!r}')
            en_dig = re.sub(r'\D', '', en)
            if lang in SECUNDARIOS:
                en_dig = re.sub(r'\D', '', en.replace('75+', '50+'))
            if en_dig != re.sub(r'\D', '', v):
                errores.append(f'{lang}: dígitos distintos en {ruta}: EN {en!r} → {v!r}')
            if 'AI Chef Pro' in en and 'AI Chef Pro' not in v:
                errores.append(f'{lang}: falta «AI Chef Pro» en {ruta}')
        bt = d['hero'].get('v2_business_types')
        if not isinstance(bt, list) or len(bt) != 11:
            errores.append(f'{lang}: hero.v2_business_types tiene {len(bt) if isinstance(bt, list) else "nada"} (esperado 11)')
        # Paralela a la anterior: el hero rota las dos con el MISMO índice, así que
        # una lista más corta dejaría «in Ihrer Restaurant» a partir de ese punto.
        bp = d['hero'].get('v2_business_prefixes')
        if not isinstance(bp, list) or len(bp) != 11:
            errores.append(f'{lang}: hero.v2_business_prefixes tiene {len(bp) if isinstance(bp, list) else "nada"} (esperado 11)')
        elif not all(isinstance(x, str) for x in bp):
            errores.append(f'{lang}: hero.v2_business_prefixes tiene elementos que no son cadenas')
        if not d['pricing']['plans']['member'].get('period'):
            errores.append(f'{lang}: pricing.plans.member.period vacío')
    if errores:
        print('\n'.join(errores))
        print(f'\n✗ GATE i18n: {len(errores)} errores')
        return 1
    print(f'✓ GATE i18n: {len(claves)} claves × {len(LANGS)} idiomas, todo presente y coherente')
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', choices=LANGS)
    ap.add_argument('--todos', action='store_true')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    if a.check:
        return check()
    langs = LANGS if a.todos else ([a.lang] if a.lang else [])
    if not langs:
        sys.exit('indica --lang, --todos o --check')
    for lang in langs:
        fundir(lang)
    return 0


if __name__ == '__main__':
    sys.exit(main())
