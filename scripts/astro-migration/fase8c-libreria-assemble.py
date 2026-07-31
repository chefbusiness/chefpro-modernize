#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8C — Generador de librerías de prompts por agente.

Reproduce el molde de la "generación A" (el bueno de los 25 existentes), medido
sobre `libreria-de-prompts-para-chef-privado-pro-ai`:

    H2  Importancia de los prompts en IA Generativa para {Agente}
    H2  Ejemplos de prompts en el contexto de {Agente}
    H2  Prompts para {FACETA} en {Agente}          ← ×7, cada uno con:
        H3  Cómo utilizar estos prompts            ← + ejemplo trabajado
        tabla de 15 prompts (3 columnas)
    H2  Tips y Consejos de Uso para {Agente}       ← 10 × H3
    H2  Explora más librerías de prompts           ← interlinking

UNA DIFERENCIA DELIBERADA CON LOS 25 EXISTENTES: la FAQ va al **frontmatter**,
no al cuerpo. Los 25 la tienen escrita como H2 y por eso **ninguno emite
FAQPage**: el layout saca el schema del campo `faq`. Aquí se hace bien desde el
principio (y el layout ya pinta el acordeón al final del artículo).

La prosa la escribe SIEMPRE bridge.py (DeepSeek v4) — REGLA CAPITAL del
proyecto. Este script orquesta, parsea y ensambla; no redacta.

Uso:
    python3 fase8c-libreria-assemble.py --config fase8c-agentes/id-alergenos.json
    python3 fase8c-libreria-assemble.py --config ... --solo-bloque 3   # regenera uno
    python3 fase8c-libreria-assemble.py --config ... --ensamblar       # sin llamar a la API
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'es'
CACHE = Path('/tmp/fase8c-libreria')
BRIDGE = Path('/root/chefbusiness-ai/bridge.py')
PYBRIDGE = '/root/chefbusiness-ai/.venv/bin/python'
# bridge.py con DeepSeek es modelo de RAZONAMIENTO: el trace de razonamiento consume
# del mismo presupuesto que la respuesta. Con 9000 un bloque de 15 prompts largos se
# truncó a mitad de frase (cazado el 2026-07-31 en el bloque 6 de ID Alérgenos), así
# que hay margen de sobra: lo que sobra no se paga, lo truncado sí se repite.
MAX_TOKENS = 16000

SYSTEM = (
    'Eres redactor senior de contenidos gastronómicos profesionales para AI Chef Pro. '
    'Escribes en español de España, con tono humano y directo, sin relleno corporativo ni '
    'frases hechas de marketing. Hablas a cocineros y gestores de hostelería que trabajan a '
    'diario. Nunca inventas datos, normativas ni funcionalidades: si no estás seguro de un '
    'dato, lo omites. Ortografía y acentuación impecables.'
)


def bridge(prompt, etiqueta, cfg, forzar=False):
    """Llama a bridge.py y cachea la salida en /tmp para poder reensamblar gratis."""
    CACHE.mkdir(exist_ok=True)
    destino = CACHE / ('%s-%s.txt' % (cfg['slug'], etiqueta))
    if destino.exists() and not forzar:
        return destino.read_text(encoding='utf-8')
    contexto = (
        'AGENTE: %s\nQUÉ HACE (resumen fiel de su configuración): %s\n'
        'PÚBLICO: %s\n\n' % (cfg['agente'], cfg['que_hace'], cfg['publico'])
    )
    cmd = [PYBRIDGE, str(BRIDGE), '--task', 'content', '--domain', 'aichef', '--lang', 'es',
           '--system', SYSTEM, '--max-tokens', str(MAX_TOKENS),
           '--prompt', contexto + prompt]
    print('  bridge → %s …' % etiqueta, flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    if r.returncode != 0:
        sys.exit('bridge falló en %s:\n%s' % (etiqueta, r.stderr[-800:]))
    txt = r.stdout.strip()
    if len(txt) < 200:
        sys.exit('bridge devolvió respuesta vacía o mínima en %s (¿max-tokens?)' % etiqueta)
    destino.write_text(txt, encoding='utf-8')
    return txt


# ── parseo de las respuestas ────────────────────────────────────────────────
def limpia(s):
    """Quita restos de markdown y comillas rectas de una línea de prosa."""
    s = re.sub(r'^\s*[-*]\s+', '', s.strip())
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    return s.strip()


def parsea_bloque(txt):
    """{intro, como_usar, filas[(prompt, area, categoria)]} del formato pactado."""
    def seccion(nombre):
        m = re.search(r'===%s===\s*(.*?)(?====|\Z)' % nombre, txt, re.S)
        return m.group(1).strip() if m else ''
    filas = []
    for linea in seccion('PROMPTS').splitlines():
        partes = [p.strip() for p in linea.split('|')]
        if len(partes) >= 3 and len(partes[0]) > 40:
            p = limpia(partes[0]).strip('«»"“” ')
            filas.append(('«%s»' % p, limpia(partes[1]), limpia(partes[2])))
    return {'intro': limpia(seccion('INTRO')), 'como': limpia(seccion('COMO_USAR')), 'filas': filas}


def parsea_pares(txt, nombre):
    """[(titulo, texto)] de un bloque con formato 'TÍTULO | TEXTO' por línea."""
    m = re.search(r'===%s===\s*(.*?)(?====|\Z)' % nombre, txt, re.S)
    out = []
    for linea in (m.group(1) if m else txt).splitlines():
        if '|' in linea:
            a, b = linea.split('|', 1)
            a, b = limpia(a), limpia(b)
            if len(a) > 3 and len(b) > 20:
                out.append((a, b))
    return out


# ── construcción del HTML ───────────────────────────────────────────────────
def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def tabla(filas):
    th = ('<thead><tr><th>Prompt / Solicitud</th><th>Área / Objetivo / Punto de dolor</th>'
          '<th>Categoría</th></tr></thead>')
    tds = ''.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (esc(a), esc(b), esc(c))
                  for a, b, c in filas)
    # `tabla-prompts` da a estas tablas su propio tratamiento responsive: la
    # primera celda es prosa larga y con el CSS genérico del catálogo la tabla
    # se iba a ~3.000 px de ancho con scroll horizontal (inusable).
    return ('<figure class="wp-block-table"><div class="table-scroll tabla-prompts"><table>%s'
            '<tbody>%s</tbody></table></div></figure>' % (th, tds))


def h2(t):
    return '<h2 class="wp-block-heading">%s</h2>' % esc(t)


def h3(t):
    return '<h3 class="wp-block-heading">%s</h3>' % esc(t)


def p(t):
    return '<p>%s</p>' % t


def figura(src, alt):
    return ('<figure class="wp-block-image size-large"><img decoding="async" src="%s" alt="%s" '
            'loading="lazy" /></figure>' % (src, esc(alt)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', required=True)
    ap.add_argument('--solo-bloque', type=int, default=0, help='regenera sólo ese bloque (1-7)')
    ap.add_argument('--ensamblar', action='store_true', help='no llama a la API, usa la caché')
    args = ap.parse_args()

    ruta = Path(args.config)
    if not ruta.is_absolute():
        ruta = Path(__file__).parent / args.config
    cfg = json.loads(ruta.read_text(encoding='utf-8'))
    A = cfg['agente']

    def pedir(etiqueta, prompt, forzar=False):
        if args.ensamblar:
            f = CACHE / ('%s-%s.txt' % (cfg['slug'], etiqueta))
            if not f.exists():
                sys.exit('falta la caché de %s; corre sin --ensamblar' % etiqueta)
            return f.read_text(encoding='utf-8')
        return bridge(prompt, etiqueta, cfg, forzar)

    # 1) Apertura: dos secciones de contexto
    apertura = pedir('apertura', (
        'Escribe la APERTURA de un artículo sobre la librería de prompts del agente.\n'
        'Formato EXACTO, sin markdown, sin títulos, sin listas:\n'
        '===ENTRADILLA===\n<un párrafo de 90-130 palabras presentando qué resuelve el agente '
        'y a quién sirve>\n'
        '===IMPORTANCIA===\n<dos párrafos, 150-200 palabras en total, sobre por qué un prompt '
        'bien formulado cambia el resultado EN ESTE dominio concreto; nada genérico sobre IA>\n'
        '===EJEMPLOS===\n<un párrafo de 90-130 palabras que explique que abajo hay %d prompts '
        'agrupados por área de trabajo>' % (len(cfg['bloques']) * 15)))
    ent = re.search(r'===ENTRADILLA===\s*(.*?)===', apertura, re.S)
    imp = re.search(r'===IMPORTANCIA===\s*(.*?)===', apertura, re.S)
    eje = re.search(r'===EJEMPLOS===\s*(.*)', apertura, re.S)

    partes = [p(limpia(ent.group(1)))] if ent else []
    partes += [h2('Importancia de los prompts en IA Generativa para %s' % A)]
    partes += [p(x) for x in limpia(imp.group(1)).split('\n') if x.strip()] if imp else []
    if cfg.get('img1'):
        partes.append(figura(cfg['img1']['src'], cfg['img1']['alt']))
    partes += [h2('Ejemplos de prompts en el contexto de %s' % A)]
    partes += [p(limpia(eje.group(1)))] if eje else []

    # 2) Los 7 bloques
    for i, b in enumerate(cfg['bloques'], 1):
        txt = pedir('bloque%d' % i, (
            'Genera el bloque de prompts «%s» para este agente.\n'
            'Enfoque del bloque: %s\n\n'
            'Formato EXACTO, sin markdown:\n'
            '===INTRO===\n<un párrafo de 70-110 palabras sobre qué resuelve el agente en esta área>\n'
            '===COMO_USAR===\n<un párrafo que tome un prompt corto de ejemplo y lo convierta en uno '
            'MUY concreto y realista de un negocio español, con cifras, ciudad, tipo de local y '
            'restricciones. Redáctalo dirigiéndote al lector de tú («si partes de…», «podrías '
            'personalizarlo así:»), sin usar «nosotros» ni hablar en primera persona del agente; '
            'termina con «Cuanto más concreto seas, mejor será el resultado.»>\n'
            '===PROMPTS===\n<EXACTAMENTE 15 líneas. Cada línea: PROMPT | ÁREA | CATEGORÍA. '
            'El PROMPT es una petición real de 25-60 palabras, en segunda persona del singular, '
            'con datos concretos (cantidades, tipo de establecimiento, normativa si aplica). '
            'ÁREA = el problema que resuelve, 3-8 palabras. CATEGORÍA = «%s». '
            'No numeres las líneas. No uses comillas al principio ni al final.>'
            % (b['titulo'], b['foco'], b['categoria'])),
            forzar=bool(args.solo_bloque and i == args.solo_bloque))
        d = parsea_bloque(txt)
        if len(d['filas']) < 15:
            sys.exit('bloque %d: %d prompts parseados de 15 — respuesta truncada o formato roto.\n'
                     '   Borra /tmp/fase8c-libreria/%s-bloque%d.txt y reejecuta.'
                     % (i, len(d['filas']), cfg['slug'], i))
        partes += [h2('Prompts para %s en %s' % (b['titulo'], A)), p(d['intro']),
                   h3('Cómo utilizar estos prompts'), p(d['como']), tabla(d['filas'][:15])]
        if i == 4 and cfg.get('img2'):
            partes.append(figura(cfg['img2']['src'], cfg['img2']['alt']))

    # 3) Tips
    tips_txt = pedir('tips', (
        'Escribe 10 consejos de uso para sacar partido a este agente.\n'
        'Formato EXACTO: 10 líneas «TÍTULO CORTO | consejo de 35-60 palabras». '
        'El título corto, 2-5 palabras, en imperativo. Nada genérico sobre IA: cada consejo '
        'debe ser específico del trabajo de este agente. Sin markdown ni numeración.'))
    partes += [h2('Tips y Consejos de Uso para %s' % A)]
    for t, texto in parsea_pares(tips_txt, 'TIPS')[:10]:
        partes += [h3(t), p(texto)]

    # 4) FAQ → al FRONTMATTER (aquí está la mejora sobre los 25 existentes)
    faq_txt = pedir('faq', (
        'Escribe 10 preguntas frecuentes con su respuesta sobre este agente.\n'
        'Formato EXACTO: 10 líneas «PREGUNTA | RESPUESTA de 40-70 palabras». '
        'Preguntas que haría de verdad un profesional de hostelería antes de usarlo. '
        'Responde en TERCERA persona hablando del agente («Es un agente que…», «Analiza…», '
        '«El agente aplica…»), NUNCA en primera persona: el artículo lo firma el blog, no el agente. '
        'Sin markdown ni numeración. No prometas funcionalidades que no se han descrito.'))
    faq = parsea_pares(faq_txt, 'FAQ')[:10]
    if len(faq) < 6:
        sys.exit('FAQ: sólo %d pares parseados' % len(faq))

    # 5) Interlinking
    partes += [h2('Explora más librerías de prompts para los agentes de AI Chef Pro'),
               p('Cada agente de la suite tiene su propia librería de prompts. No te quedes '
                 'solo con uno: explora el resto y mueve la IA por toda tu cocina:'),
               '<ul>%s</ul>' % ''.join(
                   '<li><a href="https://aichef.pro/blog/%s">%s</a></li>' % (s, esc(t))
                   for s, t in cfg['enlaces'])]

    # 6) Frontmatter + escritura
    def y(s):
        return '"%s"' % s.replace('\\', '\\\\').replace('"', '\\"').strip()
    fm = ['---', 'title: %s' % y(cfg['title']), 'description: %s' % y(cfg['description']),
          'pubDate: %s' % cfg['fecha'], 'modDate: %s' % cfg['fecha'],
          'category: libreria-de-prompts', 'tags: []',
          'image: %s' % cfg['featured']['src'], 'imageAlt: %s' % y(cfg['featured']['alt']),
          'lang: es', 'faq:']
    for q, a in faq:
        fm += ['  - q: %s' % y(q), '    a: %s' % y(a)]
    fm += ['draft: false', '---', '']

    destino = CONTENT / (cfg['slug'] + '.md')
    cuerpo = '\n'.join(partes)
    destino.write_text('\n'.join(fm) + cuerpo + '\n', encoding='utf-8')
    palabras = len(re.sub(r'<[^>]+>', ' ', cuerpo).split())
    print('\n✅ %s\n   %d palabras · %d tablas · %d prompts · %d FAQ · %d enlaces internos'
          % (destino.relative_to(REPO), palabras, len(cfg['bloques']),
             len(cfg['bloques']) * 15, len(faq), len(cfg['enlaces'])))


if __name__ == '__main__':
    main()
