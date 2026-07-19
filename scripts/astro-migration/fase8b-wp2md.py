#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8B — Conversor WP → content collection de Astro (blog).

Lee el export-seguro de blog.aichef.pro (JSONL de la REST API) y genera:
  - astro-site/src/content/blog/es/{slug}.md   (frontmatter YAML + cuerpo HTML saneado)
  - astro-site/public/blog-assets/YYYY/MM/*    (medios referenciados, copiados del export)

Uso:
  python3 scripts/astro-migration/fase8b-wp2md.py --slugs slug1 slug2 ...
  python3 scripts/astro-migration/fase8b-wp2md.py --slugs-file lista.txt [--dry-run]

Notas:
  - Python 3.7 compatible (sin removesuffix/walrus). Solo stdlib.
  - El slug del fichero = slug del WP VERBATIM (mapa 301 1:1).
  - excerpt de WP = meta description (convención RankMath-por-excerpt del blog).
  - Enlaces internos blog.aichef.pro/{slug}/ → /blog/{slug}. Imágenes
    wp-content/uploads → /blog-assets (y se copian desde el export local).
  - srcset/sizes se eliminan (Astro sirve el original; optimización por tanda).
"""
import argparse
import html
import json
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
EXPORT = Path.home() / 'aichef-blog' / 'export-2026-07-19'
OUT_MD = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'es'
OUT_ASSETS = REPO / 'astro-site' / 'public' / 'blog-assets'
UPLOADS_RE = re.compile(
    r'https?://blog\.aichef\.pro/wp-content/uploads/([^"\'\s\)\?]+)(?:\?[^"\'\s\)]*)?')
# CDN de Jetpack (i0/i1/i2.wp.com) que proxyea los uploads del blog — moriría
# con WP igual que el origen: se reescribe a /blog-assets y se pierde la query.
JETPACK_RE = re.compile(
    r'https?://i\d+\.wp\.com/blog\.aichef\.pro/wp-content/uploads/([^"\'\s\)\?]+)(?:\?[^"\'\s\)]*)?')
INTERNAL_LINK_RE = re.compile(r'https?://blog\.aichef\.pro/([a-z0-9\-]+)/?(?=["\'])')
WP_COMMENT_RE = re.compile(r'<!--\s*/?wp:[^>]*-->\s*')
SRCSET_RE = re.compile(r'\s(?:srcset|sizes)="[^"]*"')

# WP category id → categoría destino (BLOG_CATEGORIES en src/lib/blog.ts).
# Prioridad: si un post tiene varias, gana la PRIMERA de esta lista.
# Ids del export categories.json (verificados 2026-07-19).
CAT_PRIORITY = [
    (264, None),                         # Guias IA Locales → Tier D: NO migrar
    (15, 'libreria-de-prompts'),         # Librería de Prompts (cat WP 15)
    (24, 'glosario'),                    # Glosario y Léxico Científico Culinario
    (21, 'glosario'),                    # Glosario y Léxico AI
    (13, 'ia-en-gastronomia'),           # IA en Gastronomía
    (9, 'ai-chef-pro'),                  # AI Chef Pro
    (44, 'recetas'),                     # Recetario Pro AI → Recetas (John 2026-07-19)
    (1, 'tutoriales'),                   # Tutoriales
]

# Overrides explícitos slug→categoría (ganan a todo lo demás). Generado por la
# recategorización con jueces del 2026-07-19: recetas de platos que WP tenía
# en "Tutoriales" (error arrastrado) + glosario perdido en tutoriales.
OVERRIDES_FILE = REPO / 'scripts' / 'astro-migration' / 'fase8b-cat-overrides.json'


def load_jsonl(path):
    items = []
    with open(str(path), encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items


def yaml_str(s):
    """Escapado YAML seguro: comillas dobles + escapes."""
    s = s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ').strip()
    return '"%s"' % s


def strip_tags(s):
    return re.sub(r'<[^>]+>', '', s or '').strip()


def map_category(cat_ids, cat_map):
    """Devuelve slug destino o None (Tier D / sin categoría migrable)."""
    for wp_id, dest in CAT_PRIORITY:
        if wp_id in cat_ids:
            return dest
    # Sin match conocido: aviso y fallback a ia-en-gastronomia
    names = [cat_map.get(c, str(c)) for c in cat_ids]
    print('  ⚠️  categorías no mapeadas %s → ia-en-gastronomia' % names)
    return 'ia-en-gastronomia'


def sanitize_body(html_body, migrated_slugs):
    """Limpia el HTML de WP y reescribe URLs internas."""
    body = WP_COMMENT_RE.sub('', html_body)
    body = SRCSET_RE.sub('', body)
    # Atributos internos de WP con permalinks del subdominio (galerías)
    body = re.sub(r'\sdata-permalink="[^"]*"', '', body)
    # Archives y raíz del blog → hub /blog
    body = re.sub(r'href="https?://blog\.aichef\.pro/(?:tag|category|author)/[^"]*"',
                  'href="https://aichef.pro/blog"', body)
    body = re.sub(r'href="https?://blog\.aichef\.pro/?"',
                  'href="https://aichef.pro/blog"', body)
    # Imágenes → /blog-assets (la copia física la hace collect_assets)
    body = JETPACK_RE.sub(lambda m: '/blog-assets/' + m.group(1), body)
    body = UPLOADS_RE.sub(lambda m: '/blog-assets/' + m.group(1), body)

    # Enlaces internos a posts → /blog/{slug} (si el destino no migra — Tier D —
    # se apunta al hub /blog para no dejar 404 internos)
    def _link(m):
        slug = m.group(1)
        if slug in ('wp-content', 'wp-json', 'category', 'tag', 'author', 'feed'):
            return m.group(0)
        if migrated_slugs and slug not in migrated_slugs:
            return 'https://aichef.pro/blog'
        return 'https://aichef.pro/blog/' + slug

    body = INTERNAL_LINK_RE.sub(_link, body)
    # Catch-all: cualquier href residual al subdominio (paths multi-segmento,
    # adjuntos, mayúsculas…) → hub /blog. Tras el cutover el subdominio muere.
    body = re.sub(r'href="https?://blog\.aichef\.pro/[^"]*"',
                  'href="https://aichef.pro/blog"', body, flags=re.I)
    # Variantes redimensionadas de WP (-WxH) → original (el export solo tiene
    # originales; sobran bytes servir la variante).
    body = re.sub(r'(/blog-assets/[^"\'\s\)]*?)-\d+x\d+\.(jpe?g|png|webp|gif)',
                  r'\1.\2', body)
    # Líneas con sangría inicial → colapsar (evita bloques de código markdown)
    body = '\n'.join(l.lstrip() if l[:4] == '    ' else l for l in body.split('\n'))
    return body.strip()


def collect_assets(body_and_featured, dry_run):
    """Copia del export local todos los /blog-assets/... referenciados."""
    copied, missing = 0, []
    for rel in sorted(set(re.findall(r'/blog-assets/([^"\'\s\)]+)', body_and_featured))):
        src = EXPORT / 'media' / rel
        dst = OUT_ASSETS / rel
        if not src.exists():
            # El export guarda nombres DECODIFICADOS (¿… en vez de %C2%BF…);
            # la URL servida percent-encoded resuelve al fichero decodificado.
            from urllib.parse import unquote
            rel_dec = unquote(rel)
            if (EXPORT / 'media' / rel_dec).exists():
                src = EXPORT / 'media' / rel_dec
                dst = OUT_ASSETS / rel_dec
        if dst.exists():
            continue
        if not src.exists():
            missing.append(rel)
            continue
        if not dry_run:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(src), str(dst))
        copied += 1
    return copied, missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--slugs', nargs='*', default=[])
    ap.add_argument('--slugs-file')
    ap.add_argument('--all-migrated-slugs-file',
                    help='censo completo de slugs que SÍ migrarán (para reescribir enlaces internos); si falta, los enlaces internos se reescriben todos a /blog/{slug}')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    wanted = list(args.slugs)
    if args.slugs_file:
        with open(args.slugs_file, encoding='utf-8') as f:
            wanted += [l.strip() for l in f if l.strip() and not l.startswith('#')]
    if not wanted:
        sys.exit('Nada que convertir: pasa --slugs o --slugs-file')

    migrated_slugs = None
    if args.all_migrated_slugs_file:
        with open(args.all_migrated_slugs_file, encoding='utf-8') as f:
            migrated_slugs = set(l.strip() for l in f if l.strip())

    posts = {p['slug']: p for p in load_jsonl(EXPORT / 'posts-publish.jsonl')}
    media = {m['id']: m for m in load_jsonl(EXPORT / 'media.jsonl')}
    cats = {c['id']: c['name'] for c in json.load(open(str(EXPORT / 'categories.json'), encoding='utf-8'))}
    # Cluster de la auditoría 2026-06-15: los posts money (C1..C5) archivados en
    # WP bajo "Tutoriales"/"Recetario" se recolocan en ia-en-gastronomia.
    catalogo_path = Path.home() / 'aichef-blog' / '.work' / 'audit-2026-06-15' / 'catalogo.json'
    clusters = {}
    if catalogo_path.exists():
        clusters = {c['slug']: c['cluster']
                    for c in json.load(open(str(catalogo_path), encoding='utf-8'))}
    overrides = {}
    if OVERRIDES_FILE.exists():
        overrides = json.load(open(str(OVERRIDES_FILE), encoding='utf-8'))

    ok, skipped, total_assets, all_missing = 0, [], 0, []
    for slug in wanted:
        p = posts.get(slug)
        if not p:
            skipped.append((slug, 'no está en posts-publish.jsonl'))
            continue
        dest_cat = map_category(p.get('categories', []), cats)
        if dest_cat is None:
            skipped.append((slug, 'Tier D (guias-ia-locales): NO se migra'))
            continue
        if (clusters.get(slug, '').startswith('C')
                and dest_cat in ('tutoriales', 'recetas', 'glosario')):
            dest_cat = 'ia-en-gastronomia'
        if slug in overrides:
            dest_cat = overrides[slug]

        title = html.unescape(strip_tags(p['title']['rendered']))
        desc = html.unescape(strip_tags(p.get('excerpt', {}).get('rendered', '')))
        desc = re.sub(r'\s+', ' ', desc).replace('[…]', '').replace('…', '').strip()
        if not desc:
            desc = title
        # Meta description: máx ~158 chars cortando en límite de palabra.
        if len(desc) > 158:
            desc = desc[:158].rsplit(' ', 1)[0].rstrip(' ,;:.') + '…'
        body = sanitize_body(p['content']['rendered'], migrated_slugs)

        image_line = ''
        feat = media.get(p.get('featured_media') or 0)
        featured_ref = ''
        if feat:
            m = UPLOADS_RE.search(feat['source_url'] or '')
            if m:
                featured_ref = '/blog-assets/' + m.group(1)
                alt = html.unescape(feat.get('alt_text') or '') or title
                image_line = 'image: %s\nimageAlt: %s\n' % (featured_ref, yaml_str(alt))

        n, missing = collect_assets(body + ' ' + featured_ref, args.dry_run)
        total_assets += n
        all_missing += missing

        fm = (
            '---\n'
            'title: %s\n'
            'description: %s\n'
            'pubDate: %s\n'
            'modDate: %s\n'
            'category: %s\n'
            '%s'
            'lang: es\n'
            'wpId: %d\n'
            '---\n\n' % (
                yaml_str(title), yaml_str(desc[:300]),
                p['date'][:10], p['modified'][:10],
                dest_cat, image_line, p['id'],
            )
        )
        if not args.dry_run:
            OUT_MD.mkdir(parents=True, exist_ok=True)
            out = OUT_MD / (slug + '.md')
            out.write_text(fm + body + '\n', encoding='utf-8')
        ok += 1
        print('  ✅ %s → %s (%d medios)' % (slug, dest_cat, n))

    # Lastmod real por post para el sitemap (astro.config.mjs → BLOG_LASTMOD).
    if not args.dry_run:
        lastmod = {}
        for md in sorted(OUT_MD.glob('*.md')):
            m = re.search(r'^modDate: (\d{4}-\d{2}-\d{2})', md.read_text(encoding='utf-8'), re.M)
            if m:
                lastmod['/blog/' + md.stem] = m.group(1)
        (REPO / 'astro-site' / 'src' / 'lib' / 'blog-lastmod.json').write_text(
            json.dumps(lastmod, ensure_ascii=False, indent=0, sort_keys=True),
            encoding='utf-8')

    print('\n== RESUMEN: %d convertidos, %d saltados, %d medios copiados%s' % (
        ok, len(skipped), total_assets, ' [DRY-RUN]' if args.dry_run else ''))
    for s, why in skipped:
        print('  ⏭️  %s — %s' % (s, why))
    if all_missing:
        print('  🚨 %d medios referenciados NO están en el export:' % len(all_missing))
        for rel in all_missing[:20]:
            print('     ' + rel)
        sys.exit(1)


if __name__ == '__main__':
    main()
