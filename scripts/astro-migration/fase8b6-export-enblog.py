#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8B.6 — Export seguro de enblog.aichef.pro (blog EN en WordPress).

Mismo criterio que el export ES de Fase 8B: se baja TODO antes de tocar nada
(posts publicados, borradores, programados, páginas, taxonomías y medios), para
que apagar el WordPress inglés no dependa de que la migración haya salido bien.

Salida en --dest (por defecto /root/aichef-blog-media/enblog-export/):
    posts-publish.jsonl · posts-draft.jsonl · posts-future.jsonl
    pages-all.jsonl · categories.json · tags.json
    media.jsonl  y (con --medios) media/YYYY/MM/...

Uso:
    python3 scripts/astro-migration/fase8b6-export-enblog.py [--medios]
"""
import argparse
import json
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = 'https://enblog.aichef.pro/wp-json/wp/v2'
UA = {'User-Agent': 'Mozilla/5.0 (export aichef.pro)'}


def get(url, intentos=3):
    for i in range(intentos):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read().decode('utf-8')), dict(r.headers)
        except Exception as e:
            if i == intentos - 1:
                raise
            time.sleep(2 * (i + 1))
    raise RuntimeError('inalcanzable: ' + url)


def paginar(endpoint, **params):
    """Recorre todas las páginas de un endpoint del REST API."""
    out = []
    page = 1
    qs = ''.join('&%s=%s' % kv for kv in params.items())
    while True:
        url = '%s/%s?per_page=100&page=%d%s' % (BASE, endpoint, page, qs)
        try:
            datos, _ = get(url)
        except urllib.error.HTTPError as e:
            if e.code == 400:   # página fuera de rango = fin
                break
            raise
        if not datos:
            break
        out.extend(datos)
        if len(datos) < 100:
            break
        page += 1
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dest', default='/root/aichef-blog-media/enblog-export')
    ap.add_argument('--medios', action='store_true',
                    help='descarga también los binarios (no solo el manifiesto)')
    args = ap.parse_args()
    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)

    resumen = {}
    for estado, fichero in (('publish', 'posts-publish.jsonl'),
                            ('draft', 'posts-draft.jsonl'),
                            ('future', 'posts-future.jsonl')):
        posts = paginar('posts', status=estado)
        (dest / fichero).write_text(
            '\n'.join(json.dumps(p, ensure_ascii=False) for p in posts) + '\n',
            encoding='utf-8')
        resumen[estado] = len(posts)
        print('  %-8s %4d posts → %s' % (estado, len(posts), fichero))

    pages = paginar('pages')
    (dest / 'pages-all.jsonl').write_text(
        '\n'.join(json.dumps(p, ensure_ascii=False) for p in pages) + '\n', encoding='utf-8')
    print('  pages    %4d' % len(pages))

    for ep, fich in (('categories', 'categories.json'), ('tags', 'tags.json')):
        datos = paginar(ep)
        (dest / fich).write_text(json.dumps(datos, ensure_ascii=False, indent=1),
                                 encoding='utf-8')
        print('  %-8s %4d' % (ep, len(datos)))

    medios = paginar('media')
    (dest / 'media.jsonl').write_text(
        '\n'.join(json.dumps(m, ensure_ascii=False) for m in medios) + '\n', encoding='utf-8')
    print('  media    %4d (manifiesto)' % len(medios))

    if args.medios:
        MD = dest / 'media'
        ok = fail = 0
        total = 0
        for i, m in enumerate(medios, 1):
            src = m.get('source_url')
            if not src or '/wp-content/uploads/' not in src:
                continue
            rel = src.split('/wp-content/uploads/')[-1]
            out = MD / rel
            if out.exists() and out.stat().st_size:
                total += out.stat().st_size
                continue
            out.parent.mkdir(parents=True, exist_ok=True)
            try:
                req = urllib.request.Request(src, headers=UA)
                with urllib.request.urlopen(req, timeout=90) as r:
                    data = r.read()
                out.write_bytes(data)
                ok += 1
                total += len(data)
            except Exception as e:
                fail += 1
                print('    ⚠️  %s: %s' % (rel, e))
            if i % 50 == 0:
                print('    %d/%d  %.0f MB' % (i, len(medios), total / 1048576), flush=True)
        print('  binarios: %d descargados, %d fallos, %.1f MB' % (ok, fail, total / 1048576))

    (dest / 'README.md').write_text(
        '# Export de enblog.aichef.pro (blog EN en WordPress)\n\n'
        'Tomado antes de la migración Fase 8B.6 a aichef.pro/en/blog.\n\n'
        '| Fichero | Items |\n|---|---:|\n'
        '| posts-publish.jsonl | %d |\n| posts-draft.jsonl | %d |\n'
        '| posts-future.jsonl | %d |\n| pages-all.jsonl | %d |\n| media.jsonl | %d |\n\n'
        '⚠️ El WordPress inglés debe seguir VIVO hasta que el mapa 301 de\n'
        '`enblog.aichef.pro` esté activo en producción.\n'
        % (resumen['publish'], resumen['draft'], resumen['future'], len(pages), len(medios)),
        encoding='utf-8')
    print('\n✅ export en %s' % dest)


if __name__ == '__main__':
    main()
