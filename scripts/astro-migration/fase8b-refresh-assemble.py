#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8B — Ensamblador de refresh Tier A.

Combina el cuerpo NUEVO generado por bridge.py con el .md existente del post:
  - Conserva: pubDate, category, image/imageAlt (featured), lang, wpId, tier.
  - Actualiza: title, description (argumentos), modDate (hoy), faq (del bloque
    ===FAQ=== del fichero generado), cuerpo completo.
  - Sustituye <!--IMG1..N--> por <figure> con imágenes del post viejo
    (por orden de aparición, saltando la featured).
  - Envuelve tablas en .table-scroll (mismo tratamiento que el conversor).

Uso:
  python3 fase8b-refresh-assemble.py --slug chef-gpt-espanol \
      --html /ruta/out.html --title "..." --description "..." --date 2026-07-19
"""
import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'es'


def yaml_str(s):
    return '"%s"' % s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ').strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--slug', required=True)
    ap.add_argument('--html', required=True)
    ap.add_argument('--title', required=True)
    ap.add_argument('--description', required=True)
    ap.add_argument('--date', required=True, help='modDate YYYY-MM-DD')
    args = ap.parse_args()

    md_path = CONTENT / (args.slug + '.md')
    old = md_path.read_text(encoding='utf-8')
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', old, re.S)
    if not m:
        sys.exit('frontmatter no parseable en ' + str(md_path))
    fm_old, body_old = m.group(1), m.group(2)

    def fm_get(key):
        mm = re.search(r'^%s: (.*)$' % key, fm_old, re.M)
        return mm.group(1) if mm else None

    raw = Path(args.html).read_text(encoding='utf-8')
    if '===FAQ===' in raw:
        body_new, _, faq_raw = raw.partition('===FAQ===')
        faq_json = re.search(r'\[.*\]', faq_raw, re.S)
        faq = json.loads(faq_json.group(0)) if faq_json else []
    else:
        body_new, faq = raw, []
    body_new = body_new.strip()
    # Por si el modelo lo envolvió en fences
    body_new = re.sub(r'^```(?:html)?\s*|\s*```$', '', body_new)

    # Imágenes del cuerpo viejo (figure completo si existe; si no, el img)
    old_figs = re.findall(r'<figure[^>]*>.*?</figure>', body_old, re.S)
    old_figs = [f for f in old_figs if '<img' in f and 'audio' not in f]
    if not old_figs:
        old_figs = ['<figure>%s</figure>' % i
                    for i in re.findall(r'<img[^>]+>', body_old)]
    featured = fm_get('image')
    if featured:
        old_figs = [f for f in old_figs if featured not in f]

    used = 0
    def _img(mm):
        nonlocal used
        if used < len(old_figs):
            fig = old_figs[used]
            used += 1
            # Con cuerpo markdown, el HTML necesita líneas en blanco alrededor
            # para que remark lo trate como bloque.
            return '\n\n' + fig + '\n\n'
        return ''
    body_new = re.sub(r'<!--IMG\d+-->', _img, body_new)

    # Tablas responsive (idéntico al conversor; el HTML de bridge llega limpio)
    body_new = re.sub(r'<table\b', '<div class="table-scroll"><table', body_new)
    body_new = body_new.replace('</table>', '</table></div>')

    fm_lines = [
        'title: ' + yaml_str(args.title),
        'description: ' + yaml_str(args.description),
        'pubDate: ' + (fm_get('pubDate') or args.date),
        'modDate: ' + args.date,
        'category: ' + (fm_get('category') or 'ia-en-gastronomia'),
    ]
    for k in ('image', 'imageAlt', 'lang', 'wpId', 'tier'):
        v = fm_get(k)
        if v:
            fm_lines.append('%s: %s' % (k, v))
    if faq:
        fm_lines.append('faq:')
        for f in faq:
            fm_lines.append('  - q: ' + yaml_str(f['q']))
            fm_lines.append('    a: ' + yaml_str(f['a']))

    md_path.write_text('---\n' + '\n'.join(fm_lines) + '\n---\n\n' + body_new + '\n',
                       encoding='utf-8')
    words = len(re.sub(r'<[^>]+>', ' ', body_new).split())
    print('✅ %s ensamblado: %d palabras, %d imgs insertadas/%d disponibles, %d FAQ, %d tablas'
          % (args.slug, words, used, len(old_figs), len(faq), body_new.count('<table')))
    if not faq:
        print('  ⚠️  SIN FAQ — revisar salida de bridge')
        sys.exit(1)


if __name__ == '__main__':
    main()
