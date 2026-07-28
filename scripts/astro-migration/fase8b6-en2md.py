#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8B.6 — Conversor del blog EN (enblog.aichef.pro) → colección Astro.

Hermano de `fase8b-wp2md.py` (el del blog ES), pero el HTML de origen es más
limpio: sin clases wp-block, sin iframes y con TODAS las imágenes servidas por
el propio dominio (cero CDN de Jetpack).

CENSO Y CRITERIO (2026-07-28). El WordPress inglés tiene 89 posts publicados:
  · 39 de contenido real  → SE MIGRAN. 31 clics y 7.678 impresiones en 90 días,
    media de 3.645 palabras. 21 de ellos con CERO impresiones pese a ser guías
    de 3.000-5.000 palabras: no son malos, es que viven en un subdominio sin
    autoridad. Ese es justamente el problema que la migración resuelve.
  · 50 guías de ciudad (`local-ai-guides`) → NO se migran. 0 clics y ~180
    impresiones entre las 50, y son plantilla repetida por ciudad
    ("ai-recipe-costing-for-chefs-in-{london,toronto,sydney…}"): traerlas al
    dominio principal importaría un patrón de doorway pages. Mismo criterio
    Tier D que se aplicó a los 50 pSEO del blog ES. Van con 301 al hub.

QUÉ HACE POR POST:
  1. Frontmatter: title, description (del excerpt, ≤158), pubDate, modDate,
     category, image/imageAlt (featured_media del manifiesto), lang: en, wpId.
  2. Extrae el bloque "Frequently Asked Questions" (microdatos schema.org) al
     campo `faq` del frontmatter y LO ELIMINA del cuerpo — si no, la página
     acabaría con dos declaraciones FAQPage: la del microdato heredado y la
     JSON-LD que emite el layout.
  3. Imágenes: enblog.aichef.pro/wp-content/uploads/X → /blog-assets/en/X
     (subcarpeta propia: los nombres de fichero pueden chocar con los del ES).
  4. Enlaces: enblog.aichef.pro/{slug} → /en/blog/{slug} si el post migra;
     al hub /en/blog si es una guía de ciudad o no existe.
  5. Tablas envueltas en .table-scroll (misma convención que el blog ES).

Uso:
    python3 scripts/astro-migration/fase8b6-en2md.py [--apply] [--medios]
"""
import argparse
import html as htmllib
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
EXPORT = Path('/root/aichef-blog-media/enblog-export')
OUT_MD = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'en'
ASSETS = REPO / 'astro-site' / 'public' / 'blog-assets' / 'en'
ORIGEN = 'https://enblog.aichef.pro'


def limpiar(s):
    """Entidades HTML → texto plano, colapsando espacios."""
    return re.sub(r'\s+', ' ', htmllib.unescape(re.sub(r'<[^>]+>', '', s))).strip()


def yaml_str(s):
    return '"%s"' % s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ').strip()


def _contenido(html, pos):
    """Contenido del elemento cuya etiqueta de apertura empieza en `pos`.

    Cuenta anidamiento de esa misma etiqueta, así que soporta cualquier nivel.
    Devuelve (texto_interior, fin_del_elemento) o (None, None) si no cierra.
    """
    ap = re.match(r'<([a-zA-Z0-9]+)\b[^>]*>', html[pos:])
    if not ap:
        return None, None
    tag = ap.group(1)
    ini = pos + ap.end()
    prof = 1
    for t in re.finditer(r'<(/?)%s\b[^>]*>' % re.escape(tag), html[ini:], re.I):
        prof += 1 if not t.group(1) else -1
        if prof == 0:
            return html[ini:ini + t.start()], ini + t.end()
    return None, None


def extraer_faq(html):
    """Saca el bloque FAQPage de microdatos y devuelve (cuerpo_sin_faq, faq).

    Se ancla en el `<div ... schema.org/FAQPage ...>`, NO en el texto del <h2>:
    hay 13 variantes del encabezado en el corpus ("Frequently Asked Questions
    About Menu Engineering Software", "8. Frequently Asked Questions", "Part 2:
    …and FAQ"…) y buscar el literal sólo cazaba 3 de 22.

    Y es AGNÓSTICO DE LA ETIQUETA: en unos posts la pregunta va en
    `<h3 itemprop="name">` y en otros en `<p><strong><span itemprop="name">`.
    Exigir `</h3>` dejaba fuera 6 posts. Si el div del FAQPage no cierra bien
    (HTML roto en origen, 3 casos), se recorta hasta el siguiente <h2>.
    """
    # El contenedor es <div> en unos posts y <section> en otros → cualquier tag.
    m = re.search(r'<[a-zA-Z0-9]+[^>]*schema\.org/FAQPage[^>]*>', html, re.I)
    if not m:
        return html, []
    _, fin = _contenido(html, m.start())
    if fin is None:
        sig = re.search(r'<h2\b', html[m.end():])
        fin = m.end() + sig.start() if sig else len(html)
    bloque = html[m.start():fin]

    faq = []
    # Se ancla en itemtype=".../Question", que SIEMPRE está, y no en
    # itemprop="mainEntity", que falta en varios posts del corpus.
    for q in re.finditer(r'<[a-zA-Z0-9]+[^>]*schema\.org/Question[^>]*>', bloque, re.I):
        ini_q = q.start()
        cuerpo_q, _ = _contenido(bloque, ini_q)
        if cuerpo_q is None:
            cuerpo_q = bloque[q.end():q.end() + 4000]
        pregunta = respuesta = None
        for attr, destino in (('name', 'q'), ('text', 'a')):
            mm = re.search(r'itemprop="%s"' % attr, cuerpo_q)
            if not mm:
                continue
            val, _ = _contenido(cuerpo_q, cuerpo_q.rfind('<', 0, mm.start()))
            if val is None:
                continue
            if destino == 'q':
                # En algunos posts `itemprop="name"` cuelga del propio elemento
                # Question, no del <h3>: entonces `val` es la pregunta Y la
                # respuesta juntas. Si dentro hay un encabezado, ése manda.
                h = re.search(r'<h[1-6][^>]*>(.*?)</h[1-6]>', val, re.S)
                pregunta = limpiar(h.group(1)) if h else limpiar(val)
            else:
                respuesta = limpiar(val)
        if pregunta and respuesta:
            faq.append({'q': pregunta, 'a': respuesta})
    if not faq:
        return html, []          # no lo toco si no he sabido parsearlo

    # el <h2> que lo precede se va con el bloque (el layout ya pinta su propio
    # encabezado de FAQ); si no hay <h2> justo antes, sólo se quita el div.
    ini = m.start()
    prev = re.search(r'<h2[^>]*>(?:(?!</h2>).)*</h2>\s*$', html[:ini], re.S)
    if prev:
        ini = prev.start()
    return html[:ini] + html[fin:], faq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--medios', action='store_true', help='copia los binarios')
    args = ap.parse_args()

    posts = [json.loads(l) for l in
             (EXPORT / 'posts-publish.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
    cats = {c['id']: c['slug'] for c in
            json.loads((EXPORT / 'categories.json').read_text(encoding='utf-8'))}
    medios = {m['id']: m for m in
              (json.loads(l) for l in
               (EXPORT / 'media.jsonl').read_text(encoding='utf-8').splitlines() if l.strip())}

    def cats_de(p):
        return [cats.get(c, '?') for c in p.get('categories', [])]

    migran = [p for p in posts if 'local-ai-guides' not in cats_de(p)]
    excluidos = [p['slug'] for p in posts if 'local-ai-guides' in cats_de(p)]
    slugs_migran = {p['slug'] for p in migran}
    print('%d posts: %d migran, %d guías de ciudad excluidas'
          % (len(posts), len(migran), len(excluidos)))

    resumen = []
    assets_usados = set()
    rotas = set()
    for p in migran:
        slug = p['slug']
        cuerpo = p['content']['rendered']
        cuerpo, faq = extraer_faq(cuerpo)

        # imágenes del propio WordPress → carpeta EN de assets.
        # Se descarta la query (`?ver=2`): forma parte de la URL, no del fichero.
        def _img(m):
            rel = m.group(1).split('?')[0]
            assets_usados.add(rel)
            return '/blog-assets/en/' + rel
        cuerpo = re.sub(re.escape(ORIGEN) + r'/wp-content/uploads/([^"\'\s)]+)', _img, cuerpo)
        # variantes -WxH que WP genera y que no existen como fichero propio
        cuerpo = re.sub(r'(/blog-assets/en/[^"\'\s)]+?)-\d+x\d+(\.(?:jpg|jpeg|png|webp))',
                        r'\1\2', cuerpo)
        cuerpo = re.sub(r'\s(?:srcset|sizes)="[^"]*"', '', cuerpo)

        # enlaces internos del subdominio
        def _link(m):
            destino = m.group(1).strip('/')
            if destino in slugs_migran:
                return '"https://aichef.pro/en/blog/%s"' % destino
            return '"https://aichef.pro/en/blog"'
        cuerpo = re.sub(r'"' + re.escape(ORIGEN) + r'/([^"#?]*?)/?"', _link, cuerpo)

        # Imágenes ROTAS EN ORIGEN. 15 ficheros referenciados por los posts dan
        # 404 en el propio enblog.aichef.pro (bug heredado, ya visible en el
        # blog inglés vivo). Se elimina la <figure> entera: portarlas sería
        # publicar imágenes rotas en el dominio bueno.
        for rel in sorted(assets_usados):
            if (EXPORT / 'media' / rel).exists():
                continue
            ruta = '/blog-assets/en/' + rel
            antes = cuerpo
            cuerpo = re.sub(r'<figure\b(?:(?!</figure>).)*?' + re.escape(ruta)
                            + r'(?:(?!</figure>).)*?</figure>', '', cuerpo, flags=re.S)
            if cuerpo == antes:      # <img> suelto, sin <figure>
                cuerpo = re.sub(r'<img\b[^>]*?' + re.escape(ruta) + r'[^>]*?>', '', cuerpo)
            rotas.add(rel)

        cuerpo = re.sub(r'<table\b', '<div class="table-scroll"><table', cuerpo)
        cuerpo = cuerpo.replace('</table>', '</table></div>')

        cat = 'ai-in-gastronomy' if 'ai-in-gastronomy' in cats_de(p) else 'ai-chef-pro'

        img = alt = None
        fm = medios.get(p.get('featured_media'))
        if fm and fm.get('source_url', '').startswith(ORIGEN):
            rel = fm['source_url'].split('/wp-content/uploads/')[-1]
            assets_usados.add(rel)
            img = '/blog-assets/en/' + rel
            alt = limpiar(fm.get('alt_text') or fm.get('title', {}).get('rendered', '')) or None

        desc = limpiar(p['excerpt']['rendered'])
        desc = re.sub(r'\s*\[…\]$|\s*\[\.\.\.\]$', '', desc)
        if len(desc) > 158:
            corte = desc[:158].rsplit(' ', 1)[0]
            desc = corte.rstrip(' ,.;:') + '…'

        fm_lines = [
            'title: ' + yaml_str(limpiar(p['title']['rendered'])),
            'description: ' + yaml_str(desc),
            'pubDate: ' + p['date'][:10],
            'modDate: ' + (p.get('modified') or p['date'])[:10],
            'category: ' + cat,
            'lang: en',
            'wpId: %d' % p['id'],
        ]
        if img:
            fm_lines.append('image: ' + img)
            if alt:
                fm_lines.append('imageAlt: ' + yaml_str(alt))
        if faq:
            fm_lines.append('faq:')
            for f in faq:
                fm_lines.append('  - q: ' + yaml_str(f['q']))
                fm_lines.append('    a: ' + yaml_str(f['a']))

        md = '---\n' + '\n'.join(fm_lines) + '\n---\n\n' + cuerpo.strip() + '\n'
        palabras = len(re.sub(r'<[^>]+>', ' ', cuerpo).split())
        n_img = len(re.findall(r'<img\b', cuerpo))
        resumen.append((slug, palabras, len(faq), cuerpo.count('<table'), bool(img), n_img))
        if args.apply:
            OUT_MD.mkdir(parents=True, exist_ok=True)
            (OUT_MD / (slug + '.md')).write_text(md, encoding='utf-8')

    con_faq = sum(1 for r in resumen if r[2])
    print('  %d posts · %d con FAQ extraída · %d con destacada · %d assets referenciados'
          % (len(resumen), con_faq, sum(1 for r in resumen if r[4]), len(assets_usados)))
    if rotas:
        print('  %d imágenes ROTAS EN ORIGEN eliminadas del cuerpo (404 en enblog):' % len(rotas))
        for r in sorted(rotas):
            print('    · %s' % r)
    flojos = [r for r in resumen if r[5] < 2]
    if flojos:
        print('  ⚠️  %d posts quedan con <2 imágenes en el cuerpo (estándar del proyecto):'
              % len(flojos))
        for s, _, _, _, _, n in sorted(flojos, key=lambda x: x[5]):
            print('    · %-56s %d img' % (s[:56], n))

    if args.medios:
        src_media = EXPORT / 'media'
        faltan = []
        copiados = 0
        for rel in sorted(assets_usados):
            o, d = src_media / rel, ASSETS / rel
            if not o.exists():
                faltan.append(rel)
                continue
            if not d.exists():
                d.parent.mkdir(parents=True, exist_ok=True)
                if args.apply:
                    d.write_bytes(o.read_bytes())
                copiados += 1
        print('  medios: %d copiados, %d SIN ORIGEN' % (copiados, len(faltan)))
        for f in faltan[:10]:
            print('    ⚠️  %s' % f)

    if not args.apply:
        print('\n(dry-run: no se ha escrito nada; usa --apply [--medios])')
        return
    print('\n✅ %d .md en %s' % (len(resumen), OUT_MD))


if __name__ == '__main__':
    main()
