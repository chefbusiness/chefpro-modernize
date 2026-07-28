#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8B — Gate de aceptación del port del blog.

LOCAL (siempre):
  1. 322 .md en content/blog/es con frontmatter completo (title/description/
     category/pubDate/wpId) y categoría válida.
  2. Cero referencias a wp-content / i0.wp.com / blog.aichef.pro en hrefs/srcs.
  3. Toda referencia /blog-assets/... existe en disco (imágenes Y audio).

REMOTO (--base URL, p.ej. el branch deploy):
  4. Hub /blog 200 con tarjetas + categorías + rel alternate RSS.
  5. Paginación completa 200 (páginas 2..N según EXPECTED_POSTS/24).
  6. Muestra de 20 posts: 200 + <title> coincide con frontmatter + canonical
     a aichef.pro/blog/{slug} + BlogPosting + hreflang es/x-default.
  7. Categorías (6) 200 · RSS 200 con items · muestra de 10 assets 200.
  8. Anti-regresión: /, /kit-tareas-asador, /usos/rol/sous-chef, /en → 200.

Uso:
  python3 scripts/astro-migration/fase8b-gate.py                # solo local
  python3 scripts/astro-migration/fase8b-gate.py --base https://fase8b-blog--aichef-astro-staging.netlify.app
"""
import argparse
import html as htmllib
import json
import random
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'es'
ASSETS = REPO / 'astro-site' / 'public' / 'blog-assets'
VALID_CATS = {'ia-en-gastronomia', 'ai-chef-pro', 'libreria-de-prompts',
              'tutoriales', 'glosario', 'recetas'}
# 346 al portar desde WordPress (Fase 8B) − 24 consolidados con 301 hacia su
# pilar refrescado el 2026-07-28 (fase8c-consolidar-301.py) = 322.
EXPECTED_POSTS = 322
PER_PAGE = 24

checks = fails = 0


def check(cond, label):
    global checks, fails
    checks += 1
    if not cond:
        fails += 1
        print('  ❌ ' + label)


def curl(url):
    r = subprocess.run(['curl', '-s', '-A', 'Mozilla/5.0', '--max-time', '30',
                        '-w', '\n__HTTP__%{http_code}', url],
                       capture_output=True)
    out = r.stdout.decode('utf-8', errors='replace')
    body, _, code = out.rpartition('\n__HTTP__')
    return (int(code) if code.strip().isdigit() else 0), body


def curl_status(url):
    """Solo código HTTP (para binarios/paginación — no descarga el cuerpo entero)."""
    r = subprocess.run(['curl', '-s', '-o', '/dev/null', '-A', 'Mozilla/5.0',
                        '--max-time', '30', '-w', '%{http_code}', url],
                       capture_output=True, text=True)
    return int(r.stdout.strip()) if r.stdout.strip().isdigit() else 0


def parse_frontmatter(txt):
    m = re.match(r'^---\n(.*?)\n---\n', txt, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            k, _, v = line.partition(':')
            fm[k.strip()] = v.strip().strip('"')
    return fm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', help='URL base del deploy a verificar (opcional)')
    args = ap.parse_args()
    random.seed(8)  # muestra determinista

    print('— LOCAL —')
    mds = sorted(CONTENT.glob('*.md'))
    check(len(mds) == EXPECTED_POSTS, 'posts .md: %d != %d' % (len(mds), EXPECTED_POSTS))

    posts = {}
    for md in mds:
        txt = md.read_text(encoding='utf-8')
        fm = parse_frontmatter(txt)
        slug = md.stem
        check(fm is not None, '%s: sin frontmatter' % slug)
        if not fm:
            continue
        posts[slug] = fm
        for k in ('title', 'description', 'category', 'pubDate', 'wpId'):
            check(bool(fm.get(k)), '%s: falta %s' % (slug, k))
        check(fm.get('category') in VALID_CATS,
              '%s: categoría inválida %r' % (slug, fm.get('category')))
        body = txt.split('---\n', 2)[-1]
        check('blog.aichef.pro/wp-content' not in body,
              '%s: referencia residual a blog.aichef.pro/wp-content' % slug)
        # CDN de Jetpack: cualquier host iN.wp.com, apunte a donde apunte.
        # (El patrón viejo sólo miraba i0-2.wp.com/blog.aichef.pro y se le
        #  escaparon 2 imágenes servidas como i0.wp.com/www.aichef.pro —
        #  ese CDN muere al apagar WordPress. Cazado el 2026-07-28.)
        for m2 in re.finditer(r'i\d+\.wp\.com', body):
            check(False, '%s: imagen servida por el CDN de Jetpack (%s)'
                  % (slug, m2.group(0)))
            break
        for m2 in re.finditer(r'(?:href|src)="https?://blog\.aichef\.pro', body):
            check(False, '%s: enlace vivo a blog.aichef.pro' % slug)
            break
        # Hrefs malformados del conversor: href="https://\&quot;URL\&quot;".
        # No son URLs válidas → 404 en producción. El check anterior no los veía
        # porque el \&quot; se cuela entre href=" y el esquema. (2026-07-28)
        for m2 in re.finditer(r'(?:href|src)="[^"]*\\&quot;', body):
            check(False, '%s: href/src malformado (comillas sin desescapar)' % slug)
            break
        for rel in set(re.findall(r'/blog-assets/([^"\'\s\)]+)', txt)):
            from urllib.parse import unquote
            check((ASSETS / rel).exists() or (ASSETS / unquote(rel)).exists(),
                  '%s: asset inexistente %s' % (slug, rel))

    print('  local: %d checks' % checks)

    if args.base:
        B = args.base.rstrip('/')
        print('— REMOTO %s —' % B)
        st, hub = curl(B + '/blog')
        check(st == 200, '/blog: HTTP %d' % st)
        check(hub.count('<article') == PER_PAGE, '/blog: %d tarjetas != %d' % (hub.count('<article'), PER_PAGE))
        check('application/rss+xml' in hub, '/blog: sin rel alternate RSS')
        check('/blog/pagina/2' in hub, '/blog: sin enlace a página 2')

        total_pages = -(-EXPECTED_POSTS // PER_PAGE)
        for n in range(2, total_pages + 1):
            st, _ = curl('%s/blog/pagina/%d' % (B, n))
            check(st == 200, '/blog/pagina/%d: HTTP %d' % (n, st))
        st, _ = curl('%s/blog/pagina/%d' % (B, total_pages + 1))
        check(st == 404, '/blog/pagina/%d debía ser 404 (HTTP %d)' % (total_pages + 1, st))

        sample = random.sample(sorted(posts), 20)
        for slug in sample:
            st, page = curl('%s/blog/%s' % (B, slug))
            check(st == 200, '/blog/%s: HTTP %d' % (slug, st))
            if st != 200:
                continue
            t = re.search(r'<title>([^<]*)</title>', page)
            expected = posts[slug]['title']
            got = htmllib.unescape(t.group(1)) if t else ''
            check(expected in got, '/blog/%s: title %r no contiene %r' % (slug, got[:60], expected[:40]))
            check('href="https://aichef.pro/blog/%s"' % slug in page, '/blog/%s: canonical mal' % slug)
            check('BlogPosting' in page, '/blog/%s: sin BlogPosting' % slug)
            check('hreflang="x-default"' in page, '/blog/%s: sin x-default' % slug)

        for cat in sorted(VALID_CATS):
            st, _ = curl('%s/blog/categoria/%s' % (B, cat))
            check(st == 200, '/blog/categoria/%s: HTTP %d' % (cat, st))

        st, rss = curl(B + '/blog/rss.xml')
        check(st == 200 and rss.count('<item>') == 30, 'rss: HTTP %d, %d items' % (st, rss.count('<item>')))

        all_assets = [p for p in ASSETS.rglob('*') if p.is_file()]
        for p in random.sample(all_assets, 10):
            rel = str(p.relative_to(ASSETS))
            from urllib.parse import quote
            st = curl_status('%s/blog-assets/%s' % (B, quote(rel)))
            check(st == 200, '/blog-assets/%s: HTTP %d' % (rel, st))

        for path in ('/', '/kit-tareas-asador', '/usos/rol/sous-chef', '/en'):
            st, _ = curl(B + path)
            check(st == 200, 'anti-regresión %s: HTTP %d' % (path, st))

    print('\n%s GATE FASE 8B: %d checks, %d fallos' % ('✅' if not fails else '🚨', checks, fails))
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
