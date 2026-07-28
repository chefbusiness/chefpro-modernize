#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditoría del mapa 301 de un subdominio WordPress migrado.

POR QUÉ EXISTE. El 2026-07-28, nueve días después del cutover del blog ES, se
descubrió que las 8 archives de categoría de `blog.aichef.pro` redirigían a un
404: sus URLs viven en la RAÍZ (ese WordPress tiene la base de categoría vacía)
y caían en la regla genérica `/:slug → /blog/:slug`, que las trataba como si
fueran posts. Auditando el resto aparecieron 16 casos más: las 7 páginas del WP,
los sitemaps hijos, robots.txt, favicon.ico y los archives de año.

El patrón es siempre el mismo y conviene tenerlo grabado:

    la genérica `/:slug` se traga TODO lo que llegue con un solo segmento,
    así que cada familia de un segmento que no sea un post necesita su
    propia regla ANTES — o se convierte en un 301 a un 404.

QUÉ HACE. Simula el motor de Netlify (primera coincidencia gana, `*` = prefijo,
`:slug` = un segmento) sobre el censo COMPLETO del export del WordPress, sigue
las cadenas de redirección como haría un navegador (Netlify no encadena por
dentro) y comprueba que el destino final exista en `astro-site/dist`. No toca la
red: es un gate offline que se puede correr antes de desplegar.

Uso:
    npm run build --prefix astro-site      # hace falta un dist reciente
    python3 scripts/astro-migration/fase8b-auditar-301.py            # blog ES
    python3 scripts/astro-migration/fase8b-auditar-301.py --sitio en # enblog
Sale con 1 si hay algún 301 que muere en un 404.
"""
import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DIST = REPO / 'astro-site' / 'dist'
REDIRECTS = REPO / 'astro-site' / 'public' / '_redirects'
DEST = 'https://aichef.pro'

SITIOS = {
    'es': {
        'host': 'https://blog.aichef.pro',
        'export': Path('/root/aichef-blog-media/blog-export-2026-07-19'),
    },
    'en': {
        'host': 'https://enblog.aichef.pro',
        'export': Path('/root/aichef-blog-media/enblog-export'),
    },
}

# Rutas que no salen de ningún export pero que Google (y los bots) piden igual.
INFRA = ('/robots.txt', '/favicon.ico', '/sitemap.xml', '/sitemap_index.xml',
         '/post-sitemap.xml', '/page-sitemap.xml', '/category-sitemap.xml',
         '/feed', '/comments/feed', '/page/2', '/amp', '/xmlrpc.php',
         '/wp-login.php', '/wp-admin', '/wp-json/wp/v2/posts',
         '/2024', '/2025', '/2026', '/2024/09', '/author/john', '/')


def reglas(prefijo):
    """[(patrón, destino)] en orden. prefijo=None → las reglas sin host."""
    out = []
    for linea in REDIRECTS.read_text(encoding='utf-8').split('\n'):
        linea = linea.strip()
        if not linea or linea.startswith('#'):
            continue
        p = linea.split()
        if len(p) < 2:
            continue
        if prefijo:
            if p[0].startswith(prefijo):
                out.append((p[0][len(prefijo):] or '/', p[1]))
        elif not p[0].startswith('http'):
            out.append((p[0], p[1]))
    return out


def resolver(path, rs):
    """Primera regla que casa, como Netlify."""
    p = '/' + path.strip('/') if path.strip('/') else '/'
    for pat, dest in rs:
        if pat == '/*':
            return dest, pat
        if pat.endswith('/*'):
            base = pat[:-2]
            if p == base or p.startswith(base + '/'):
                return dest.replace(':splat', p[len(base):].lstrip('/')), pat
        elif ':' in pat:
            segs = [s for s in p.strip('/').split('/') if s]
            if len(segs) == len([s for s in pat.strip('/').split('/') if s]) and segs:
                return dest.replace(':slug', segs[0]), pat
        elif pat.rstrip('/') == p.rstrip('/'):
            return dest, pat
    return None, None


def existe(url):
    """¿El destino está construido en el dist?"""
    if not url.startswith(DEST):
        return True                       # externo: no es cosa nuestra
    ruta = url[len(DEST):].split('?')[0].split('#')[0].strip('/')
    if not ruta:
        return (DIST / 'index.html').exists()
    return any((DIST / (ruta + '.html'), DIST / ruta / 'index.html', DIST / ruta)[i].exists()
               for i in range(3))


def censo(export):
    """[(familia, path)] con todo lo que el WordPress servía."""
    casos = []
    def jl(f):
        p = export / f
        return [json.loads(l) for l in p.open(encoding='utf-8') if l.strip()] if p.exists() else []

    for post in jl('posts-publish.jsonl'):
        casos.append(('post publicado', '/' + post['slug']))
    for pag in jl('pages-all.jsonl'):
        casos.append(('página WP', '/' + pag['slug']))
    cats = export / 'categories.json'
    if cats.exists():
        for c in json.loads(cats.read_text(encoding='utf-8')):
            casos.append(('categoría raíz', '/' + c['slug']))
            casos.append(('categoría /category/', '/category/%s/' % c['slug']))
            casos.append(('categoría paginada', '/%s/page/2' % c['slug']))
            casos.append(('feed de categoría', '/%s/feed' % c['slug']))
    tags = export / 'tags.json'
    if tags.exists():
        for t in json.loads(tags.read_text(encoding='utf-8'))[:40]:
            casos.append(('tag', '/tag/%s/' % t['slug']))
    for extra in INFRA:
        casos.append(('infraestructura', extra))
    return casos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sitio', choices=sorted(SITIOS), default='es')
    args = ap.parse_args()
    cfg = SITIOS[args.sitio]

    if not DIST.exists():
        sys.exit('No hay dist: construye antes (npm run build --prefix astro-site)')
    if not cfg['export'].exists():
        sys.exit('No encuentro el export en %s' % cfg['export'])

    rs, propias = reglas(cfg['host']), reglas(None)
    casos = censo(cfg['export'])
    print('%s — %d reglas, %d URLs del censo\n' % (cfg['host'], len(rs), len(casos)))

    rotos, sin_regla, cadenas, ok = [], [], [], 0
    for familia, path in casos:
        dest, pat = resolver(path, rs)
        if dest is None:
            sin_regla.append((familia, path))
            continue
        saltos = [dest]
        for _ in range(5):                      # el navegador vuelve a pedir el destino
            actual = saltos[-1]
            if not actual.startswith(DEST):
                break
            sig, _p = resolver(actual[len(DEST):] or '/', propias)
            if not sig or sig == actual:
                break
            saltos.append(sig if sig.startswith('http') else DEST + sig)
        if not existe(saltos[-1]):
            rotos.append((familia, path, saltos[-1], pat))
        else:
            ok += 1
            if len(saltos) > 1:
                cadenas.append((path, saltos))

    print('%d OK · %d rotos · %d sin regla · %d cadenas de 2+ saltos'
          % (ok, len(rotos), len(sin_regla), len(cadenas)))
    for path, saltos in cadenas:
        print('  ⚠️  cadena %s → %s' % (path, ' → '.join(s.replace(DEST, '') for s in saltos)))
    for familia, path in sin_regla:
        print('  ❌ SIN REGLA  [%s] %s' % (familia, path))
    for familia, path, dest, pat in rotos:
        print('  ❌ 301 A UN 404  [%-20s] %-45s → %s (regla %s)' % (familia, path, dest, pat))
    return 1 if (rotos or sin_regla) else 0


if __name__ == '__main__':
    sys.exit(main())
