#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8C — Versión INGLESA de una librería de prompts publicada en español.

NO es una traducción. Es una adaptación al mercado profesional estadounidense,
que es donde vive el otro idioma dominante de la plataforma (enapp.aichef.pro).
Decisión de John (2026-07-31): EE. UU. como mercado principal.

QUÉ CAMBIA respecto al post español, y por qué importa:
  · **Normativa.** El ES cita Reglamento UE 1169/2011 y RD 126/2015. En EE. UU.
    eso no aplica: se habla de FDA Food Code, FALCPA y los 9 alérgenos mayores
    (el sésamo entró en 2023), y de HACCP en vez de APPCC. Traducir la norma
    europea sería publicar derecho que no rige para el lector.
  · **Unidades.** Imperiales por delante (oz, lb, °F, quarts) y métrico entre
    paréntesis solo cuando la precisión lo pide.
  · **Moneda y mercado.** Dólares y ciudades de EE. UU., no Valencia ni Cádiz.
  · **Oficio.** Vocabulario de cocina americana: walk-in, prep list, line cook,
    expo, back of house, 86'd… no calcos del español.

Las IMÁGENES se reutilizan del post español: son fotos sin texto ni caras, así
que valen igual. Lo que sí se adapta es el `alt`.

Los BANNERS de producto apuntan por ahora a la landing ES —no existen landings en
inglés— con el UTM del post inglés para poder medir esa fuga. Decisión consciente
de John, no un olvido.

Uso:
    python3 scripts/astro-migration/fase8c-libreria-en.py --slug id-alergenos
    python3 scripts/astro-migration/fase8c-libreria-en.py --slug ... --ensamblar
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ES = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'es'
EN = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'en'
CACHE = Path('/tmp/fase8c-libreria-en')
BRIDGE = Path('/root/chefbusiness-ai/bridge.py')
PYBRIDGE = '/root/chefbusiness-ai/.venv/bin/python'
MAX_TOKENS = 16000
MAPA = Path(__file__).parent / 'fase8c-agentes' / 'agentes-en.json'

SYSTEM = (
    'You are a senior food-service content writer for AI Chef Pro, writing for US '
    'professional kitchens: chefs, sous chefs, kitchen managers and restaurant owners. '
    'You write natural American English — the way someone who has actually worked a line '
    'writes, not translated Spanish. You NEVER invent regulations, data or product '
    'features. You never name real people or imply they endorse anything. '
    'US context by default: FDA Food Code, FALCPA and the 9 major allergens, HACCP (never '
    '"APPCC"), imperial units first with metric in parentheses only where precision matters, '
    'US dollars, US cities. '
    'BUT the audience is the whole English-speaking trade, so nod to the other markets where it '
    'actually changes the answer: name the UK (FSA, Natasha\'s Law), Australia and New Zealand '
    '(FSANZ) and India (FSSAI) as the equivalent authorities, and let some prompt examples be set '
    'in London, Manchester, Sydney, Auckland, Toronto or Mumbai instead of always a US city. '
    'Name the REGULATOR and the general obligation only — never invent article numbers, dates or '
    'thresholds for those markets. Spelling and grammar must be flawless.'
)


def bridge(prompt, etiqueta, slug, forzar=False):
    CACHE.mkdir(exist_ok=True)
    destino = CACHE / ('%s-%s.txt' % (slug, etiqueta))
    if destino.exists() and not forzar:
        return destino.read_text(encoding='utf-8')
    cmd = [PYBRIDGE, str(BRIDGE), '--task', 'content', '--domain', 'aichef', '--lang', 'en',
           '--system', SYSTEM, '--max-tokens', str(MAX_TOKENS), '--prompt', prompt]
    print('  bridge → %s …' % etiqueta, flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    if r.returncode != 0:
        sys.exit('bridge falló en %s:\n%s' % (etiqueta, r.stderr[-600:]))
    txt = r.stdout.strip()
    if len(txt) < 200:
        sys.exit('respuesta vacía en %s' % etiqueta)
    destino.write_text(txt, encoding='utf-8')
    return txt


def cargar_generador():
    """El maquetado de banners e imágenes vive en el generador ES: se importa
    para no tener dos versiones del mismo HTML."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'gen', Path(__file__).parent / 'fase8c-libreria-assemble.py')
    mod = importlib.util.module_from_spec(spec)
    guardado, sys.argv = sys.argv, ['gen']
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.argv = guardado
    return mod


def trocea_es(md):
    """Extrae del .md español lo que hay que adaptar."""
    txt = md.read_text(encoding='utf-8')
    fm, cuerpo = txt.split('---', 2)[1], txt.split('---', 2)[2]
    def campo(k):
        m = re.search(r'^%s: "(.*?)"$' % k, fm, re.M | re.S)
        return m.group(1) if m else ''
    faq = re.findall(r'^  - q: "(.*?)"\n    a: "(.*?)"$', fm, re.M | re.S)
    imgs = re.findall(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"', cuerpo)
    bloques = []
    for m in re.finditer(
            r'<h2 class="wp-block-heading">Prompts para (.*?)</h2>(.*?)(?=<h2 class="wp-block-heading">|\Z)',
            cuerpo, re.S):
        seccion = m.group(2)
        filas = re.findall(r'<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>', seccion, re.S)
        intro = re.search(r'^<p>(.*?)</p>', seccion, re.S)
        como = re.search(r'Cómo utilizar estos prompts</h3><p>(.*?)</p>', seccion, re.S)
        bloques.append({'titulo': m.group(1), 'intro': intro.group(1) if intro else '',
                        'como': como.group(1) if como else '', 'filas': filas})
    tips = re.findall(r'<h3 class="wp-block-heading">(.*?)</h3><p>(.*?)</p>',
                      cuerpo[cuerpo.find('Tips y Consejos'):] if 'Tips y Consejos' in cuerpo else '', re.S)
    return {'title': campo('title'), 'description': campo('description'),
            'image': re.search(r'^image: (.*)$', fm, re.M).group(1).strip(),
            'imageAlt': campo('imageAlt'), 'faq': faq, 'imgs': imgs,
            'bloques': bloques, 'tips': tips,
            'fecha': re.search(r'^pubDate: (\S+)', fm, re.M).group(1)}


def limpia(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--slug', required=True, help='slug del agente, p.ej. id-alergenos')
    ap.add_argument('--ensamblar', action='store_true')
    args = ap.parse_args()

    mapa = json.loads(MAPA.read_text(encoding='utf-8')) if MAPA.exists() else {}
    if args.slug not in mapa:
        sys.exit('falta %s en %s (nombre del agente y slug EN)' % (args.slug, MAPA.name))
    info = mapa[args.slug]
    md_es = ES / ('libreria-de-prompts-para-%s.md' % args.slug)
    if not md_es.exists():
        sys.exit('no existe el post ES: %s' % md_es.name)
    d = trocea_es(md_es)
    A = info['agente']          # nombre del agente TAL CUAL está en la plataforma

    def pedir(et, prompt, forzar=False):
        if args.ensamblar:
            f = CACHE / ('%s-%s.txt' % (args.slug, et))
            if not f.exists():
                sys.exit('falta caché de %s' % et)
            return f.read_text(encoding='utf-8')
        return bridge(prompt, et, args.slug, forzar)

    CTX = ('AGENT: %s (an AI agent inside AI Chef Pro; keep the agent name EXACTLY as given, '
           'do not translate it).\n' % A)

    # 1) cabecera + apertura
    cab = pedir('cabecera', CTX + (
        'Below is the Spanish opening of a prompt-library article. Rewrite it for US '
        'professional kitchens. Do not translate literally: adapt examples, units, currency '
        'and any regulation to the US reality.\n\n'
        'SPANISH TITLE: %s\nSPANISH DESCRIPTION: %s\nSPANISH OPENING: %s\n\n'
        'EXACT format, no markdown:\n'
        '===TITLE===\n<English title, max 70 chars, keep the pattern '
        '"Prompt Library for {agent}: ..." >\n'
        '===DESCRIPTION===\n<meta description, max 155 chars>\n'
        '===LEDE===\n<one paragraph, 90-130 words, what the agent solves and for whom>\n'
        '===WHY===\n<two paragraphs, 150-200 words total, why a precise prompt changes the '
        'output IN THIS domain>\n'
        '===EXAMPLES===\n<one paragraph, 90-130 words, introducing the %d prompts grouped by '
        'area below>'
        % (d['title'], d['description'], limpia(d['bloques'][0]['intro'])[:400],
           sum(len(b['filas']) for b in d['bloques']))))

    partes = []
    def sec(n, t=cab):
        m = re.search(r'===%s===\s*(.*?)(?====|\Z)' % n, t, re.S)
        return m.group(1).strip() if m else ''

    partes.append('<p>%s</p>' % sec('LEDE'))
    partes.append('<h2 class="wp-block-heading">Why prompts matter with %s</h2>' % A)
    partes += ['<p>%s</p>' % p for p in sec('WHY').split('\n') if p.strip()]
    if len(d['imgs']) > 0:
        partes.append('<!--IMG1-->')
    partes.append('<h2 class="wp-block-heading">Prompt examples for %s</h2>' % A)
    partes.append('<p>%s</p>' % sec('EXAMPLES'))

    # 2) los bloques, uno por llamada
    for i, b in enumerate(d['bloques'], 1):
        filas_es = '\n'.join('%s | %s | %s' % (limpia(a), limpia(x), limpia(c)) for a, x, c in b['filas'])
        txt = pedir('bloque%d' % i, CTX + (
            'Adapt this Spanish block of a prompt library to US professional kitchens.\n'
            'SPANISH BLOCK TITLE: %s\nSPANISH INTRO: %s\nSPANISH WORKED EXAMPLE: %s\n'
            'SPANISH PROMPTS (one per line, "prompt | area | category"):\n%s\n\n'
            'Rules: rewrite, do not translate word for word. Swap Spanish cities for US ones, '
            'euros for dollars, metric for imperial, and any EU/Spanish regulation for its US '
            'equivalent (FDA Food Code, FALCPA, HACCP). Keep the SAME NUMBER of prompts and the '
            'same practical intent of each one.\n\n'
            'EXACT format, no markdown:\n'
            '===BLOCK_TITLE===\n<English block title, no agent name>\n'
            '===INTRO===\n<one paragraph, 70-110 words>\n'
            '===HOW===\n<one paragraph that turns a short prompt into a very specific one for a '
            'real US business, with numbers, city and constraints; end with "The more specific '
            'you are, the better the result.">\n'
            '===PROMPTS===\n<%d lines, each "PROMPT | AREA | CATEGORY">'
            % (b['titulo'], limpia(b['intro'])[:500], limpia(b['como'])[:600],
               filas_es, len(b['filas']))))
        bt = re.search(r'===BLOCK_TITLE===\s*(.*?)(?====)', txt, re.S)
        intro = re.search(r'===INTRO===\s*(.*?)(?====)', txt, re.S)
        como = re.search(r'===HOW===\s*(.*?)(?====)', txt, re.S)
        filas = []
        for l in (re.search(r'===PROMPTS===\s*(.*)', txt, re.S) or [None, ''])[1].splitlines():
            p = [x.strip() for x in l.split('|')]
            if len(p) >= 3 and len(p[0]) > 40:
                filas.append(('«%s»' % p[0].strip('«»"“” '), p[1], p[2]))
        if len(filas) < len(b['filas']):
            sys.exit('bloque %d: %d prompts de %d — respuesta truncada.\n   Borra %s/%s-bloque%d.txt'
                     % (i, len(filas), len(b['filas']), CACHE, args.slug, i))
        esc = lambda s: s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        partes += ['<h2 class="wp-block-heading">Prompts for %s in %s</h2>' % (esc(bt.group(1).strip()), A),
                   '<p>%s</p>' % intro.group(1).strip(),
                   '<h3 class="wp-block-heading">How to use these prompts</h3>',
                   '<p>%s</p>' % como.group(1).strip(),
                   '<figure class="wp-block-table"><div class="table-scroll tabla-prompts"><table>'
                   '<thead><tr><th>Prompt / Request</th><th>Area / Goal / Pain point</th>'
                   '<th>Category</th></tr></thead><tbody>%s</tbody></table></div></figure>'
                   % ''.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>'
                             % (esc(a), esc(x), esc(c)) for a, x, c in filas[:len(b['filas'])])]
        if i == 4 and len(d['imgs']) > 1:
            partes.append('<!--IMG2-->')
        if i in (2, 4, 6) and info.get('productos'):
            n = [2, 4, 6].index(i)
            if n < len(info['productos']):
                partes.append('<!--BANNER%d-->' % n)

    # 3) tips y FAQ
    tips_txt = pedir('tips', CTX + (
        'Adapt these Spanish usage tips to US professional kitchens.\n%s\n\n'
        'EXACT format: %d lines "SHORT TITLE | tip of 35-60 words". No markdown.'
        % ('\n'.join('%s | %s' % (limpia(a), limpia(b)) for a, b in d['tips']), len(d['tips']))))
    partes.append('<h2 class="wp-block-heading">Tips for getting more out of %s</h2>' % A)
    for l in tips_txt.splitlines():
        if '|' in l:
            a, b = l.split('|', 1)
            if len(a.strip()) > 3 and len(b.strip()) > 20:
                partes += ['<h3 class="wp-block-heading">%s</h3>' % a.strip().lstrip('-* '),
                           '<p>%s</p>' % b.strip()]

    faq_txt = pedir('faq', CTX + (
        'Adapt this Spanish FAQ to US professional kitchens.\n%s\n\n'
        'EXACT format: %d lines "QUESTION | ANSWER of 40-70 words". Third person about the '
        'agent, never first person. No markdown.'
        % ('\n'.join('%s | %s' % (q, a) for q, a in d['faq']), len(d['faq']))))
    faq_en = []
    for l in faq_txt.splitlines():
        if '|' in l:
            q, a = l.split('|', 1)
            if len(q.strip()) > 5 and len(a.strip()) > 20:
                faq_en.append((q.strip().lstrip('-* '), a.strip()))

    # 4) alts de las imágenes: se reutilizan los ficheros del post ES (fotos sin
    #    texto ni caras), pero el texto alternativo hay que adaptarlo.
    alts_txt = pedir('alts', CTX + (
        'Adapt these Spanish image alt texts to English. One per line, same order, '
        'no numbering, no markdown, max 120 chars each:\n%s'
        % '\n'.join(a for _, a in [(d['image'], d['imageAlt'])] + d['imgs'])))
    alts = [l.strip().lstrip('-* ') for l in alts_txt.splitlines() if len(l.strip()) > 15]

    # 5) sustituir marcadores por imágenes y banners
    gen = cargar_generador()
    prods = gen.catalogo_productos()
    cuerpo = '\n'.join(partes)
    for n, (src, _alt) in enumerate(d['imgs'], 1):
        alt = alts[n] if n < len(alts) else _alt
        cuerpo = cuerpo.replace('<!--IMG%d-->' % n, gen.figura(src, alt))
    for n, slug_prod in enumerate(info.get('productos', [])):
        cuerpo = cuerpo.replace('<!--BANNER%d-->' % n,
                                gen.banner(slug_prod, prods, info['slug_en'], 'en'))
    sobrantes = re.findall(r'<!--(IMG|BANNER)\d+-->', cuerpo)
    if sobrantes:
        sys.exit('quedan marcadores sin sustituir: %s' % sobrantes)

    # 6) interlinking EN: las librerías inglesas que ya existan + la archive de
    #    su categoría + los posts EN que la configuración marque como afines.
    hermanas = sorted(q.stem for q in EN.glob('prompt-library-*.md') if q.stem != info['slug_en'])
    enlaces = [(s, 'Prompts for ' + s.replace('prompt-library-', '').replace('-', ' ').title())
               for s in hermanas] + [(e['slug'], e['texto']) for e in info.get('enlaces_extra', [])]
    cuerpo += ('<h2 class="wp-block-heading">More prompt libraries for AI Chef Pro agents</h2>'
               '<p>Every agent in the suite has its own prompt library. Browse the rest and put '
               'the AI to work across your whole operation:</p><ul>%s</ul>'
               % ''.join('<li><a href="https://aichef.pro/en/blog/%s">%s</a></li>' % (s, txt)
                         for s, txt in enlaces)
               + '<p><a href="https://aichef.pro/en/blog/category/prompt-library">'
                 'See every prompt library →</a></p>')

    # 7) frontmatter y escritura
    def y(s):
        return '"%s"' % s.replace('\\', '\\\\').replace('"', '\\"').strip()
    fm = ['---', 'title: %s' % y(sec('TITLE')), 'description: %s' % y(sec('DESCRIPTION')),
          'pubDate: %s' % d['fecha'], 'modDate: %s' % d['fecha'],
          'category: prompt-library', 'tags: []',
          'translations:', '  es: %s' % y('libreria-de-prompts-para-%s' % args.slug),
          'image: %s' % d['image'], 'imageAlt: %s' % y(alts[0] if alts else d['imageAlt']),
          'lang: en', 'faq:']
    for q, a in faq_en:
        fm += ['  - q: %s' % y(q), '    a: %s' % y(a)]
    fm += ['draft: false', '---', '']

    destino = EN / (info['slug_en'] + '.md')
    destino.write_text('\n'.join(fm) + cuerpo + '\n', encoding='utf-8')

    # Recíproco en el post ES: si solo lo declara un lado, Google lo ignora.
    txt_es = md_es.read_text(encoding='utf-8')
    if 'translations:' not in txt_es.split('---')[1]:
        txt_es = txt_es.replace('\nlang: es\n',
                                '\nlang: es\ntranslations:\n  en: %s\n' % info['slug_en'], 1)
        md_es.write_text(txt_es, encoding='utf-8')
        print('   ↔ par declarado también en el post ES')
    palabras = len(re.sub(r'<[^>]+>', ' ', cuerpo).split())
    print('\n✅ %s\n   %d palabras · %d tablas · %d FAQ · %d banners · %d enlaces internos'
          % (destino.relative_to(REPO), palabras, cuerpo.count('<table>'), len(faq_en),
             cuerpo.count('Digital product ·'), len(enlaces) + 1))


if __name__ == '__main__':
    main()
