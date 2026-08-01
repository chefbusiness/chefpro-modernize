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
from datetime import date
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


def bridge(prompt, etiqueta, slug, forzar=False, minimo=200):
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
    if len(txt) < minimo:
        sys.exit('respuesta demasiado corta en %s (%d caracteres, mínimo %d).\n'
                 'Antes de culpar a bridge: comprueba que el material que se le manda NO va '
                 'vacío — un prompt sin contenido devuelve una respuesta vacía.'
                 % (etiqueta, len(txt), minimo))
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


def limpia(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).strip()


# El inglés de cocina usa «sauté», «purée», «jalapeño»: los acentos NO delatan
# español. Lo que sí delata es la apertura de interrogación y una acumulación de
# palabras función. Con menos de tres se colarían falsos positivos («à la carte»).
FUNCION_ES = re.compile(r'\b(el|la|los|las|del|que|para|con|una|por|más|cómo|qué|tus?|'
                        r'este|esta|sus?|puede|cocina)\b', re.I)

# Cabecera de la tabla o eco del contexto: lo único que hay que descartar de la
# lista de prompts que devuelve el modelo.
CABECERA = re.compile(r'(prompt\s*/|===|agent\s*:|context\s*:)', re.I)


def sin_espanol(textos, etiqueta, slug):
    """El modelo trata como clave fija lo que se le pasa en español y lo devuelve
    sin traducir: en el piloto salieron las 10 preguntas de la FAQ en español con
    la respuesta en inglés, y eso alimenta además el FAQPage."""
    malos = [t for t in textos
             if re.search(r'[¿¡]', t) or len(set(m.group(0).lower()
                                                 for m in FUNCION_ES.finditer(t))) >= 3]
    if malos:
        sys.exit('%s: %d línea(s) siguen en español, p.ej. «%s».\n'
                 'Borra %s/%s-%s.txt y reintenta.'
                 % (etiqueta, len(malos), malos[0][:100], CACHE, slug, etiqueta))


# ─── Extracción del post ES ─────────────────────────────────────────────────
# El corpus tiene DOS moldes de HTML y hay que leer los dos. Asumir uno solo
# costó una sesión entera (piloto de id-alergenos, 2026-08-01):
#
#   · «nuevo» — lo emite fase8c-libreria-assemble.py. Etiquetas separadas por
#     "\n", tips como <h3>+<p>, FAQ en el frontmatter.
#   · «WordPress» — los 25 heredados del export. Etiquetas PEGADAS, párrafos con
#     class="wp-block-paragraph", tips como <h3>+<ul><li>, y la FAQ solo en el
#     cuerpo (<h2>Preguntas Frecuentes…</h2>), nunca en el frontmatter.
#
# Por eso NADA de aquí puede dar por hecho que dos etiquetas van pegadas, y todo
# se busca DENTRO de su sección: el regex viejo de tips, al no encontrar par en
# su zona, seguía con .*? hasta cazar uno en la FAQ 30 KB más abajo y devolvía
# la FAQ disfrazada de tips.

RELACIONADOS = re.compile(r'<h2[^>]*>\s*También te [Pp]uede [Ii]nteresar\s*</h2>')
SECCION_REAL = re.compile(r'<h2[^>]*>\s*(?:Prompts para |Tips y Consejos|Preguntas Frecuentes|'
                          r'Explora más)')


def _sin_relacionados(cuerpo):
    """Los 5 posts de molde WordPress antiguo llevan incrustado EN MITAD del
    artículo un «También te puede interesar» congelado del WordPress: el 20-25 %
    del HTML, 7-9 imágenes y SIETE <h2> falsos que son títulos de posts
    relacionados (uno repetido cinco veces, apuntando a páginas pSEO de ciudades).

    No es contenido del post —BlogPost.astro ya pinta sus propios relacionados de
    la misma categoría— y envenena cualquier censo: por su culpa estos posts
    parecían tener 12-16 imágenes cuando las suyas son 2-4."""
    m = RELACIONADOS.search(cuerpo)
    if not m:
        return cuerpo
    sig = SECCION_REAL.search(cuerpo, m.end())
    return cuerpo[:m.start()] + (cuerpo[sig.start():] if sig else '')


def _secciones(cuerpo):
    """[(título del h2, contenido hasta el siguiente h2)] en orden de aparición.

    «Cómo utilizar estos prompts» NO abre sección: en casi todo el corpus es un
    <h3> dentro del bloque, pero en recetario-cocina-creativa-ai es un <h2>, y
    trocear ahí partía el bloque en dos y dejaba su tabla de 15 prompts fuera."""
    limites = [m for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', cuerpo, re.S)
               if 'Cómo utilizar' not in m.group(1)]
    out = []
    for i, m in enumerate(limites):
        fin = limites[i + 1].start() if i + 1 < len(limites) else len(cuerpo)
        out.append((limpia(m.group(1)), cuerpo[m.end():fin]))
    return out


def _primer_parrafo(seccion):
    m = re.search(r'<p[^>]*>(.*?)</p>', seccion, re.S)
    return m.group(1) if m else ''


def _como_usar(seccion):
    # El encabezado va en h3 en casi todo el corpus y en h2 en recetario; en
    # catering-ai el texto además vive dentro de un <strong>. Se salta cualquier
    # cierre de etiqueta entre la frase y el párrafo siguiente.
    # …y en catering-ai el texto acaba en «&nbsp;». Se tolera cualquier mezcla de
    # espacios, entidades y cierres de etiqueta entre la frase y su párrafo.
    m = re.search(r'Cómo utilizar estos prompts(?:&nbsp;|\s|</?[a-z][^>]*>){0,8}?<p[^>]*>(.*?)</p>',
                  seccion, re.S)
    if m:
        return m.group(1)
    # Y en el último bloque de catering-ai ni siquiera es un encabezado: es una
    # entradilla en negrita DENTRO del párrafo, con el texto a continuación.
    m = re.search(r'<p[^>]*><strong>Cómo utilizar estos prompts:?</strong>(?:&nbsp;|\s)*(.*?)</p>',
                  seccion, re.S)
    return m.group(1) if m else ''


# Un tip se abre con un <h3> o, en el molde WordPress antiguo, con un párrafo en
# negrita que hace de encabezado sin serlo.
ABRE_TIP = re.compile(r'(?:<h3[^>]*>(.*?)</h3>|<p[^>]*><strong>(.*?)</strong></p>)'
                      r'\s*(.*?)(?=<h3|<p[^>]*><strong>|\Z)', re.S)


def _tips(zona):
    """Tres moldes de desarrollo: <p> (nuevo), <ul><li>consejo</li><li>ejemplo</li>
    (WordPress) y el mismo <ul> colgando de un <p><strong> (WordPress antiguo)."""
    tips = []
    for m in ABRE_TIP.finditer(zona):
        titulo, resto = limpia(m.group(1) or m.group(2) or ''), m.group(3)
        p = re.search(r'<p[^>]*>(.*?)</p>', resto, re.S)
        lis = re.findall(r'<li>(.*?)</li>', resto, re.S)
        texto = limpia(p.group(1)) if p else ' '.join(limpia(x) for x in lis)
        if titulo and len(texto) > 20:
            tips.append((titulo, texto))
    return tips


def _faq(fm, secciones):
    """Frontmatter en el molde nuevo; sección visible en el de WordPress. En
    catering-ai la FAQ es un bloque de Rank Math, que mete un <div> entre la
    pregunta y la respuesta: sin tolerarlo, la extracción daba cero."""
    faq = re.findall(r'^  - q: "(.*?)"\n    a: "(.*?)"$', fm, re.M | re.S)
    if faq:
        return faq
    for titulo, seccion in secciones:
        if titulo.startswith('Preguntas Frecuentes'):
            return [(limpia(q), limpia(a)) for q, a in re.findall(
                r'<h3[^>]*>(.*?)</h3>(?:\s|<div[^>]*>)*<p[^>]*>(.*?)</p>', seccion, re.S)]
    return []


def trocea_es(md):
    """Extrae del .md español lo que hay que adaptar."""
    txt = md.read_text(encoding='utf-8')
    fm, cuerpo = txt.split('---', 2)[1], _sin_relacionados(txt.split('---', 2)[2])
    def campo(k):
        m = re.search(r'^%s: "(.*?)"$' % k, fm, re.M | re.S)
        return m.group(1) if m else ''
    secciones = _secciones(cuerpo)
    bloques = []
    for titulo, seccion in secciones:
        if not titulo.startswith('Prompts para '):
            continue
        bloques.append({
            'titulo': titulo[len('Prompts para '):],
            'intro': _primer_parrafo(seccion),
            'como': _como_usar(seccion),
            'filas': re.findall(r'<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>',
                                seccion, re.S)})
    zona_tips = next((s for t, s in secciones if t.startswith('Tips y Consejos')), '')
    return {'title': campo('title'), 'description': campo('description'),
            'image': re.search(r'^image: (.*)$', fm, re.M).group(1).strip(),
            'imageAlt': campo('imageAlt'), 'faq': _faq(fm, secciones),
            'imgs': re.findall(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"', cuerpo),
            'bloques': bloques, 'tips': _tips(zona_tips),
            'fecha': re.search(r'^pubDate: (\S+)', fm, re.M).group(1)}


def verifica(d, slug):
    """Aborta ANTES de gastar un token si el post ES no encaja con el molde.
    El fallo real se veía como 'respuesta vacía en tips', que acusaba al modelo
    de un fallo del parser y mandaba a depurar al sitio equivocado."""
    faltas = []
    if not d['bloques']:
        faltas.append('ningún <h2>Prompts para …</h2>')
    for i, b in enumerate(d['bloques'], 1):
        if not b['filas']:
            faltas.append('bloque %d: tabla de prompts vacía' % i)
        if not limpia(b['intro']):
            faltas.append('bloque %d: sin párrafo de introducción' % i)
        if not limpia(b['como']):
            faltas.append('bloque %d: sin «Cómo utilizar estos prompts»' % i)
    if not d['faq']:
        faltas.append('sin FAQ ni en el frontmatter ni en la sección «Preguntas Frecuentes»')
    if not 1 <= len(d["imgs"]) <= 10:
        faltas.append('%d imágenes en el cuerpo: fuera del rango que el molde reparte (1-10). '
                      'Si son muchas, comprueba que _sin_relacionados() esté recortando el '
                      'bloque «También te puede interesar»' % len(d['imgs']))
    # Los tips SÍ pueden faltar: catering-ai no tiene esa sección en español y se
    # redactan desde cero en inglés. Se avisa, no se aborta.
    if not d['tips']:
        print('   ⚠ sin tips en el post ES: se redactarán desde cero en inglés', flush=True)
    if faltas:
        sys.exit('EXTRACCIÓN INCOMPLETA de %s — el post ES no encaja con el molde:\n  · %s'
                 % (slug, '\n  · '.join(faltas)))


MARCA_HERMANAS = '<h2 class="wp-block-heading">More prompt libraries for AI Chef Pro agents</h2>'


def bloque_enlaces(slug_en, mapa, extra=()):
    """El anchor sale del nombre REAL del agente en agentes-en.json. Derivarlo del
    slug daba «Allergen Id» y «Gencal Waste» en el enlace de cada post."""
    nombres = {v['slug_en']: v['agente'] for v in mapa.values()}
    enlaces = [(s, 'Prompts for %s' % nombres[s])
               for s in sorted(q.stem for q in EN.glob('prompt-library-*.md'))
               if s != slug_en and s in nombres]
    return enlaces + [(e['slug'], e['texto']) for e in extra]


def bloque_hermanas(enlaces):
    html = (MARCA_HERMANAS +
            '<p>Every agent in the suite has its own prompt library. Browse the rest and put '
            'the AI to work across your whole operation:</p>')
    if enlaces:      # el primero de la tanda nace sin hermanas: nada de <ul> vacío
        html += '<ul>%s</ul>' % ''.join(
            '<li><a href="https://aichef.pro/en/blog/%s">%s</a></li>' % (s, t) for s, t in enlaces)
    # Al hub curado, no a la archive cronológica: el hub agrupa las 26 con sus
    # nombres reales de agente. Ojo con el slug, en plural: el filtro del sitemap
    # excluye todo lo que acabe en `-library` (así se llaman los dashboards de pago).
    return html + ('<p><a href="https://aichef.pro/en/prompt-libraries">'
                   'See every prompt library →</a></p>')


def reenlazar(mapa):
    """El bloque de hermanas se escribe una vez, así que el orden de generación deja
    a los primeros con menos enlaces que los últimos. Esto lo rehace en todos."""
    libs = sorted(EN.glob('prompt-library-*.md'))
    tocados = 0
    for p in libs:
        txt = p.read_text(encoding='utf-8')
        i = txt.find(MARCA_HERMANAS)
        if i < 0:
            print('  ⚠ %s no tiene bloque de hermanas; lo dejo intacto' % p.name)
            continue
        extra = next((v.get('enlaces_extra', []) for v in mapa.values()
                      if v['slug_en'] == p.stem), [])
        nuevo = txt[:i] + bloque_hermanas(bloque_enlaces(p.stem, mapa, extra)) + '\n'
        if nuevo != txt:
            p.write_text(nuevo, encoding='utf-8')
            tocados += 1
    print('↔ bloque de hermanas rehecho en %d de %d librerías EN' % (tocados, len(libs)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--slug', help='slug del agente, p.ej. id-alergenos')
    ap.add_argument('--ensamblar', action='store_true')
    ap.add_argument('--reenlazar', action='store_true',
                    help='rehace el bloque de enlaces entre librerías EN y termina')
    args = ap.parse_args()

    mapa = json.loads(MAPA.read_text(encoding='utf-8')) if MAPA.exists() else {}
    if args.reenlazar:
        return reenlazar(mapa)
    if not args.slug:
        sys.exit('hace falta --slug (o --reenlazar)')
    if args.slug not in mapa:
        sys.exit('falta %s en %s (nombre del agente y slug EN)' % (args.slug, MAPA.name))
    info = mapa[args.slug]
    md_es = ES / ('libreria-de-prompts-para-%s.md' % args.slug)
    if not md_es.exists():
        sys.exit('no existe el post ES: %s' % md_es.name)
    d = trocea_es(md_es)
    verifica(d, args.slug)
    print('· %s → %d bloques / %d prompts / %d tips / %d FAQ / %d imágenes'
          % (args.slug, len(d['bloques']), sum(len(b['filas']) for b in d['bloques']),
             len(d['tips']), len(d['faq']), len(d['imgs'])), flush=True)
    A = info['agente']          # nombre del agente TAL CUAL está en la plataforma

    def pedir(et, prompt, forzar=False, minimo=200):
        if args.ensamblar:
            f = CACHE / ('%s-%s.txt' % (args.slug, et))
            if not f.exists():
                sys.exit('falta caché de %s' % et)
            return f.read_text(encoding='utf-8')
        return bridge(prompt, et, args.slug, forzar, minimo)

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

    # Reparto de imágenes. Estuvo fijo en 2 mientras todos los posts tenían 2; los
    # del molde WordPress antiguo traen hasta 6 propias y descartarlas rompería la
    # paridad con el español. La primera va tras el «por qué» y el resto se
    # espacian entre los bloques.
    def reparte(cuantos):
        """Marcadores espaciados entre los bloques. Si hay más marcadores que
        bloques caen varios tras el mismo, que es feo pero no pierde ninguno:
        empujarlos al siguiente hueco libre los amontonaba todos en el último."""
        sitios = {}
        for k in range(cuantos):
            idx = max(1, min(len(d['bloques']),
                             round((k + 1) * len(d['bloques']) / (cuantos + 1)) or 1))
            sitios.setdefault(idx, []).append(k)
        return sitios

    tras_bloque = reparte(len(d['imgs']) - 1)
    # Tres banners a tres alturas (política de John). Estaban clavados en los
    # bloques 2, 4 y 6: con 5 bloques el tercero no existía y el post salía con dos.
    # Imágenes y banners NO se excluyen: un bloque puede llevar de los dos.
    tras_bloque_banner = reparte(min(3, len(info.get('productos', []))))

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
            # Un umbral de longitud descarta prompts cortos LEGÍTIMOS: varios posts
            # abren con uno deliberadamente vago («Dame el escandallo de este plato»,
            # 34 caracteres) para contrastarlo con el específico. Lo que hay que
            # descartar es la cabecera de la tabla o el eco del contexto, no la brevedad.
            if len(p) >= 3 and all(p[:3]) and len(p[0]) > 12 and not CABECERA.match(p[0]):
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
        for n in tras_bloque.get(i, []):
            partes.append('<!--IMG%d-->' % (n + 2))
        for n in tras_bloque_banner.get(i, []):
            partes.append('<!--BANNER%d-->' % n)

    # 3) tips y FAQ
    if d['tips']:
        n_tips = len(d['tips'])
        pide_tips = ('Adapt these Spanish usage tips to US professional kitchens.\n%s\n\n'
                     'EXACT format: %d lines "SHORT TITLE | tip of 35-60 words". No markdown.'
                     % ('\n'.join('%s | %s' % (limpia(a), limpia(b)) for a, b in d['tips']),
                        n_tips))
    else:
        # catering-ai no tiene sección de tips en español. Se redactan desde cero,
        # pero anclados a lo que el agente hace de verdad —las áreas de sus propios
        # bloques—, no inventados en el aire.
        n_tips = 8
        pide_tips = ('Write practical usage tips for this agent, for US professional '
                     'kitchens. Base them ONLY on what the agent actually does, which these '
                     'prompt areas describe:\n%s\n\n'
                     'EXACT format: %d lines "SHORT TITLE | tip of 35-60 words". No markdown.'
                     % ('\n'.join('- ' + b['titulo'] for b in d['bloques']), n_tips))
    tips_txt = pedir('tips', CTX + pide_tips)
    tips_en = []
    for l in tips_txt.splitlines():
        if '|' in l:
            a, b = l.split('|', 1)
            if len(a.strip()) > 3 and len(b.strip()) > 20:
                tips_en.append((a.strip().lstrip('-* '), b.strip()))
    sin_espanol([t for t, _ in tips_en] + [x for _, x in tips_en], 'tips', args.slug)
    if len(tips_en) < n_tips:
        sys.exit('tips: %d de %d. Borra %s/%s-tips.txt y reintenta'
                 % (len(tips_en), n_tips, CACHE, args.slug))
    partes.append('<h2 class="wp-block-heading">Tips for getting more out of %s</h2>' % A)
    for titulo, texto in tips_en:
        partes += ['<h3 class="wp-block-heading">%s</h3>' % titulo, '<p>%s</p>' % texto]

    # Ojo con el enunciado: con un «QUESTION | ANSWER» a secas, el modelo trata la
    # pregunta como una clave fija y la devuelve EN ESPAÑOL, traduciendo solo la
    # respuesta. Pasó en el piloto y se publicaría una FAQ bilingüe absurda que
    # además alimenta el FAQPage.
    faq_txt = pedir('faq', CTX + (
        'Adapt this Spanish FAQ to US professional kitchens. BOTH the question and the '
        'answer must be WRITTEN IN ENGLISH: never echo the Spanish question back.\n%s\n\n'
        'EXACT format: %d lines "ENGLISH QUESTION | ENGLISH ANSWER of 40-70 words". Third '
        'person about the agent, never first person. No markdown.'
        % ('\n'.join('%s | %s' % (q, a) for q, a in d['faq']), len(d['faq']))))
    faq_en = []
    for l in faq_txt.splitlines():
        if '|' in l:
            q, a = l.split('|', 1)
            if len(q.strip()) > 5 and len(a.strip()) > 20:
                faq_en.append((q.strip().lstrip('-* '), a.strip()))
    sin_espanol([q for q, _ in faq_en] + [a for _, a in faq_en], 'faq', args.slug)
    if len(faq_en) < len(d['faq']):
        sys.exit('faq: %d de %d preguntas. Borra %s/%s-faq.txt y reintenta'
                 % (len(faq_en), len(d['faq']), CACHE, args.slug))

    # 4) alts de las imágenes: se reutilizan los ficheros del post ES (fotos sin
    #    texto ni caras), pero el texto alternativo hay que adaptarlo.
    # Los alts VACÍOS del español no se mandan a traducir. Descuadraban el recuento
    # —bridge devuelve una línea menos por cada uno— y, sobre todo, pedirle que
    # invente uno a partir del nombre del fichero puede meter el nombre de una
    # PERSONA REAL en el post: recetario-cocina-creativa-ai trae una foto cuyo
    # fichero es el nombre y apellido de un chef. Un alt vacío es HTML válido para
    # una imagen decorativa; inventarlo no lo es.
    todos = [(d['image'], d['imageAlt'])] + d['imgs']
    pide = [(i, a) for i, (_, a) in enumerate(todos) if a.strip()]
    alts_txt = pedir('alts', CTX + (
        'Adapt these Spanish image alt texts to English. One per line, same order, '
        'no numbering, no markdown, max 120 chars each:\n%s'
        % '\n'.join(a for _, a in pide)), minimo=60)
    # El modelo a veces devuelve como primera línea el encabezado del contexto
    # («AGENT: Gastro Lexicum»). Cuela por longitud y descuadra el recuento.
    # Umbral bajo a propósito: un alt legítimo puede ser «AI Chef Pro» (11
    # caracteres) y exigir más de 15 lo descartaba, descuadrando el recuento y
    # haciendo parecer que fallaba el modelo. Quien valida aquí es el RECUENTO
    # contra las imágenes del español, no la longitud de cada línea.
    lineas = [l.strip().lstrip('-* ') for l in alts_txt.splitlines()
              if len(l.strip()) > 3 and not re.match(r'(AGENT|CONTEXT)\s*:', l.strip(), re.I)]
    if len(lineas) != len(pide):
        sys.exit('alts: bridge devolvió %d líneas y hacen falta %d (%d imágenes, %d con alt '
                 'en el español).\nBorra %s/%s-alts.txt y reintenta. Sin esto se cuela un alt '
                 'EN ESPAÑOL dentro de un post inglés, y en silencio.'
                 % (len(lineas), len(pide), len(todos), len(pide), CACHE, args.slug))
    alts = [''] * len(todos)
    for (i, _), texto in zip(pide, lineas):
        alts[i] = texto

    # 5) sustituir marcadores por imágenes y banners
    gen = cargar_generador()
    prods = gen.catalogo_productos()

    # Pese a la orden de no traducir el nombre del agente, el modelo cuela el
    # español de vez en cuando (1 post de 21 en la primera tanda: «Barista
    # Consultor Pro» en vez de «Barista Consultant Pro»). Se normaliza aquí en vez
    # de fiarlo al prompt: un post inglés que nombra al agente en español describe
    # algo que el lector no encuentra en su interfaz. En los 12 de hotelería, que
    # se llaman igual en los dos idiomas, esto es un no-op.
    m_nombre_es = re.search(r'<h[123][^>]*>Tips y Consejos de Uso para (.*?)</h[123]>',
                            md_es.read_text(encoding='utf-8'), re.S)
    nombre_es = limpia(m_nombre_es.group(1)) if m_nombre_es else ''

    def en_ingles(s):
        return s.replace(nombre_es, A) if nombre_es and nombre_es != A else s

    cuerpo = en_ingles('\n'.join(partes))
    for n, (src, _alt) in enumerate(d['imgs'], 1):
        cuerpo = cuerpo.replace('<!--IMG%d-->' % n, gen.figura(src, alts[n]))
    for n, slug_prod in enumerate(info.get('productos', [])):
        cuerpo = cuerpo.replace('<!--BANNER%d-->' % n,
                                gen.banner(slug_prod, prods, info['slug_en'], 'en'))
    sobrantes = re.findall(r'<!--(IMG|BANNER)\d+-->', cuerpo)
    if sobrantes:
        sys.exit('quedan marcadores sin sustituir: %s' % sobrantes)

    # 6) interlinking EN: las librerías inglesas que ya existan + la archive de
    #    su categoría + los posts EN que la configuración marque como afines.
    enlaces = bloque_enlaces(info['slug_en'], mapa, info.get('enlaces_extra', []))
    cuerpo += bloque_hermanas(enlaces)

    # 7) frontmatter y escritura
    def y(s):
        return '"%s"' % s.replace('\\', '\\\\').replace('"', '\\"').strip()
    # La fecha NO se hereda del post español: este contenido no existía hasta que se
    # generó, y 21 URLs nuevas entrando al sitemap fechadas cinco semanas antes
    # regalan la señal de frescura del lanzamiento. Decisión de John, 2026-08-01.
    # pubDate se fija una sola vez: si el post inglés ya existe, se respeta el suyo y
    # solo se mueve modDate, para que un reensamblado no lo rejuvenezca.
    destino = EN / (info['slug_en'] + '.md')
    hoy = date.today().isoformat()
    pub = hoy
    if destino.exists():
        previo = re.search(r'^pubDate: (\S+)', destino.read_text(encoding='utf-8'), re.M)
        if previo:
            pub = previo.group(1)

    fm = ['---', 'title: %s' % y(en_ingles(sec('TITLE'))),
          'description: %s' % y(en_ingles(sec('DESCRIPTION'))),
          'pubDate: %s' % pub, 'modDate: %s' % hoy,
          'category: prompt-library', 'tags: []',
          'translations:', '  es: %s' % y('libreria-de-prompts-para-%s' % args.slug),
          'image: %s' % d['image'],
          'imageAlt: %s' % y(en_ingles(alts[0] if alts else d['imageAlt'])),
          'lang: en', 'faq:']
    for q, a in faq_en:
        fm += ['  - q: %s' % y(en_ingles(q)), '    a: %s' % y(en_ingles(a))]
    fm += ['draft: false', '---', '']

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
