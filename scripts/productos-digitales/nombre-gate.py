#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""nombre-gate.py — un producto, UN nombre visible: el mismo en todas las superficies.

Por qué (D6 de scripts/productos-digitales/guia-pasteleria-SPEC.md, 2026-09-10): el repo
ya pagó este defecto una vez. El pie decía «Biblioteca de Prompts» y la página de destino
se titulaba «Librería de Prompts»; en inglés, «Prompt Library» apuntaba a «Prompt
Libraries» y el hub quedó huérfano. La regla que quedó escrita en CLAUDE.md es que **el
nombre del enlace debe coincidir con el de la página de destino**, y hasta hoy no la ataba
ningún gate: el `name.es` del catálogo, el H1 de la landing, el `productName` del JSON-LD,
el texto de los enlaces cruzados y el `<title>` del dashboard se escriben a mano en cinco
ficheros distintos, y nada compara los cinco.

Qué compara, para cada producto pedido:

  1. `name.es` de src/data/products-catalog.ts                      (banners de los 325 posts)
  2. H1 de la ficha .ts de astro-site/src/data/productos/**         (`hero.titlePre` + `hero.titleGold`)
  3. `schema.productName` de esa misma ficha                        (JSON-LD Product)
  4. `label` de TODOS los enlaces cruzados a /<slug> que haya en    (footerLinks de las
     las demás fichas de astro-site/src/data/productos/**            fichas hermanas)
  5. `<title>` del dashboard src/pages/<X>Dashboard.tsx, quitando   (zona app post-pago)
     los sufijos de la familia (« — Dashboard», « | AI Chef Pro»)

Cinco iguales → OK. Cualquier discrepancia → salida 1 con las cinco cadenas a la vista.

Uso:
    /usr/local/bin/python3 scripts/productos-digitales/nombre-gate.py
    /usr/local/bin/python3 scripts/productos-digitales/nombre-gate.py --only guia-pasteleria-obrador

EN (tienda inglesa, fichas en astro-site/src/data/productos-en/**): la regla es la misma pero
el "nombre" es `name.en` del catálogo (se llega a la ficha por `urlByLang.en` = /en/digital-products/<slug>)
y el H1 NO es igual al nombre —en EN el H1 es la forma corta: «Taco Shop Business Plan» frente a
«Taco Shop Business Plan Kit»—, así que se exige que el nombre EMPIECE por el H1. Se comparan: name.en,
`schema.productName`, label de los footerLinks hermanos a /en/digital-products/<slug> y `<title>` del
dashboard (zona-app.ts, sin sufijos). Se ejecuta tras el bucle ES; `--only` acepta también un slug EN.

Sin `--only` recorre todos los productos que tengan ficha .ts con `slug:` y entrada en el
catálogo. Los que no tengan alguna de las superficies (p. ej. una landing sin dashboard)
se saltan esa comprobación e informan de ello, pero no fallan por ausencia: este gate mide
COHERENCIA, no cobertura — de la cobertura ya se ocupa gate-flujo-postpago.py.

Nota de implementación: se parsean los .ts con expresiones regulares a propósito (no hay
runtime de TS aquí). Por eso el gate es estricto con el formato y prefiere ABORTAR con un
mensaje claro antes que devolver un verde silencioso: un parser hecho a mano sobre un
fichero que otros editan pierde datos sin avisar, y eso ya costó dinero en el catálogo de
productos (kit-inventario invisible e invendible, 2026-08-30).
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CATALOGO = ROOT / 'src' / 'data' / 'products-catalog.ts'
FICHAS_DIR = ROOT / 'astro-site' / 'src' / 'data' / 'productos'
FICHAS_EN_DIR = ROOT / 'astro-site' / 'src' / 'data' / 'productos-en'
ZONA_APP = ROOT / 'astro-site' / 'src' / 'lib' / 'zona-app.ts'
SPA_PAGES = ROOT / 'src' / 'pages'

# Sufijos de familia que el <title> del dashboard añade al nombre del producto.
SUFIJOS_TITLE = [' | AI Chef Pro', ' — Dashboard', ' - Dashboard']


def catalogo_nombres():
    """{slug: name.es} de products-catalog.ts, con gate de recuento contra lo declarado."""
    txt = CATALOGO.read_text(encoding='utf-8')
    out = {}
    for m in re.finditer(r"^  '([a-z0-9-]+)': \{", txt, re.M):
        pid = m.start()
        seg = txt[m.start():]
        sig = re.search(r"^  '[a-z0-9-]+': \{", seg[10:], re.M)
        seg = seg[:10 + sig.start()] if sig else seg
        n = re.search(r"name: \{ es: '([^']*)'", seg)
        if n:
            out[m.group(1)] = n.group(1)
    declaradas = set(re.findall(r"^  '([a-z0-9-]+)': \{", txt, re.M))
    perdidas = declaradas - set(out)
    if perdidas:
        sys.exit('❌ el parser del catálogo perdió %d entrada(s): %s'
                 % (len(perdidas), ', '.join(sorted(perdidas))))
    return out


def fichas(base=None):
    """{slug: (ruta, texto)} de todas las fichas .ts de producto."""
    out = {}
    for f in sorted((base or FICHAS_DIR).rglob('*.ts')):
        if f.name == 'types.ts':
            continue
        txt = f.read_text(encoding='utf-8')
        m = re.search(r"^  slug: '([a-z0-9-]+)',", txt, re.M)
        if m:
            out[m.group(1)] = (f, txt)
    return out


def h1_de(txt):
    pre = re.search(r"^    titlePre: '([^']*)',", txt, re.M)
    gold = re.search(r"^    titleGold: '([^']*)',", txt, re.M)
    if not pre or not gold:
        return None
    return (pre.group(1) + gold.group(1)).strip()


def product_name_de(txt):
    # `productName:` puede ir en la misma línea o en la siguiente (prettier lo parte
    # cuando es largo: así está en kit-tareas-pasteleria.ts).
    m = re.search(r"productName:\s*\n?\s*'((?:[^'\\]|\\.)*)'", txt)
    return m.group(1).replace("\\'", "'") if m else None


def labels_cruzados(slug, todas):
    """Textos de TODOS los enlaces a /<slug> en los footerLinks de las demás fichas."""
    out = []
    for otro, (ruta, txt) in sorted(todas.items()):
        if otro == slug:
            continue
        for m in re.finditer(
                r"\{ href: '/" + re.escape(slug) + r"', label: '([^']*)' \}"
                r"|\{ label: '([^']*)', href: '/" + re.escape(slug) + r"' \}", txt):
            out.append((ruta.name, m.group(1) or m.group(2)))
    return out


def catalogo_nombres_en():
    """{slug_en: name.en} de las entradas del catálogo con urlByLang.en = /en/digital-products/<slug>."""
    txt = CATALOGO.read_text(encoding='utf-8')
    out = {}
    starts = list(re.finditer(r"^  '[a-z0-9-]+': \{", txt, re.M))
    for i, m in enumerate(starts):
        seg = txt[m.start():starts[i + 1].start() if i + 1 < len(starts) else len(txt)]
        u = re.search(r"urlByLang: \{[^}]*en: '/en/digital-products/([a-z0-9-]+)'", seg)
        n = re.search(r"name: \{ es: '(?:[^'\\]|\\.)*', en: '((?:[^'\\]|\\.)*)'", seg)
        if u and n:
            out[u.group(1)] = n.group(1).replace("\\'", "'")
    return out


def labels_cruzados_en(slug, todas):
    out = []
    h = re.escape('/en/digital-products/' + slug)
    for otro, (ruta, txt) in sorted(todas.items()):
        if otro == slug:
            continue
        for m in re.finditer(r"\{ href: '" + h + r"', label: '([^']*)' \}"
                             r"|\{ label: '([^']*)', href: '" + h + r"' \}", txt):
            out.append((ruta.name, m.group(1) or m.group(2)))
    return out


def title_dashboard_en(slug):
    reg = ZONA_APP.read_text(encoding='utf-8')
    m = re.search(r"\{ productId: '" + re.escape(slug) + r"',[^\n]*?dashboardComponent: '([^']+)'", reg)
    if not m:
        return None, 'sin entrada en zona-app.ts'
    f = SPA_PAGES / (m.group(1) + '.tsx')
    if not f.exists():
        return None, 'no existe %s' % f.name
    titles = re.findall(r'<title>([^<]+)</title>', f.read_text(encoding='utf-8'))
    if len(titles) != 1:
        return None, '%s tiene %d <title> (esperado 1)' % (f.name, len(titles))
    t = titles[0]
    for s in SUFIJOS_TITLE:
        t = t.replace(s, '')
    return t.strip(), f.name


def comprobar_en(slugs_pedidos):
    """Misma regla para la tienda EN. Devuelve (comprobados, fallos)."""
    cat = catalogo_nombres_en()
    fis = fichas(FICHAS_EN_DIR)
    slugs = slugs_pedidos if slugs_pedidos else sorted(set(cat) & set(fis))
    fallos = 0
    print('--- EN')
    for slug in slugs:
        if slug not in fis:
            print('❌ %s: no hay ficha EN con ese slug' % slug)
            fallos += 1
            continue
        nombre = cat.get(slug)
        if nombre is None:
            print('❌ %s: sin name.en/urlByLang.en en products-catalog.ts' % slug)
            fallos += 1
            continue
        ruta, txt = fis[slug]
        h1 = h1_de(txt)
        pn = product_name_de(txt)
        cruz = labels_cruzados_en(slug, fis)
        tit, nota = title_dashboard_en(slug)
        malas = []
        if h1 is None or not nombre.startswith(h1):
            malas.append('H1 de %s: %r (el nombre debe empezar por el H1)' % (ruta.name, h1))
        if pn != nombre:
            malas.append('schema.productName de %s: %r' % (ruta.name, pn))
        for fichero, label in cruz:
            if label != nombre:
                malas.append('footerLink en %s: %r' % (fichero, label))
        if tit is not None and tit != nombre:
            malas.append('<title> de %s (sin sufijos): %r' % (nota, tit))
        if malas:
            fallos += 1
            print('❌ %s — name.en del catálogo es %r y NO coincide con:' % (slug, nombre))
            for m in malas:
                print('     · %s' % m)
        else:
            print('✅ %s — %r en catálogo, H1, JSON-LD, %d enlace(s) cruzado(s)%s'
                  % (slug, nombre, len(cruz),
                     ' y <title> del dashboard' if tit is not None else '  (⚠️ dashboard no comprobado: %s)' % nota))
    return len(slugs), fallos


def title_dashboard(slug):
    """<title> del dashboard de la zona app, sin los sufijos de familia."""
    reg = ZONA_APP.read_text(encoding='utf-8')
    m = re.search(r"\{ productId: '" + re.escape(slug) + r"',[^\n]*?dashboardComponent: '([^']+)'", reg)
    if not m:
        return None, 'sin entrada en zona-app.ts'
    f = SPA_PAGES / (m.group(1) + '.tsx')
    if not f.exists():
        return None, 'no existe %s' % f.name
    titles = re.findall(r'<title>([^<]+)</title>', f.read_text(encoding='utf-8'))
    if len(titles) != 1:
        return None, '%s tiene %d <title> (esperado 1)' % (f.name, len(titles))
    t = titles[0]
    for s in SUFIJOS_TITLE:
        t = t.replace(s, '')
    return t.strip(), f.name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', help='comprobar sólo este slug')
    args = ap.parse_args()

    cat = catalogo_nombres()
    fis = fichas()
    slugs = [args.only] if args.only else sorted(set(cat) & set(fis))
    if args.only and args.only not in fis:
        if args.only in fichas(FICHAS_EN_DIR):
            n, f = comprobar_en([args.only])
            print('---\n%d producto(s) EN comprobado(s) · %d con el nombre roto' % (n, f))
            sys.exit(1 if f else 0)
        sys.exit('❌ %s: no hay ficha .ts con ese slug en %s'
                 % (args.only, FICHAS_DIR.relative_to(ROOT)))

    fallos = 0
    for slug in slugs:
        nombre = cat.get(slug)
        if nombre is None:
            print('❌ %s: sin entrada en products-catalog.ts' % slug)
            fallos += 1
            continue
        ruta, txt = fis[slug]
        h1 = h1_de(txt)
        pn = product_name_de(txt)
        cruz = labels_cruzados(slug, fis)
        tit, nota = title_dashboard(slug)

        malas = []
        if h1 != nombre:
            malas.append('H1 de %s: %r' % (ruta.name, h1))
        if pn != nombre:
            malas.append('schema.productName de %s: %r' % (ruta.name, pn))
        for fichero, label in cruz:
            if label != nombre:
                malas.append('footerLink en %s: %r' % (fichero, label))
        if tit is not None and tit != nombre:
            malas.append('<title> de %s (sin sufijos): %r' % (nota, tit))

        if malas:
            fallos += 1
            print('❌ %s — el nombre del catálogo es %r y NO coincide con:' % (slug, nombre))
            for m in malas:
                print('     · %s' % m)
        else:
            aviso = '' if tit is not None else '  (⚠️ dashboard no comprobado: %s)' % nota
            print('✅ %s — %r en catálogo, H1, JSON-LD, %d enlace(s) cruzado(s)%s%s'
                  % (slug, nombre, len(cruz),
                     ' y <title> del dashboard' if tit is not None else '', aviso))

    print('---')
    print('%d producto(s) comprobado(s) · %d con el nombre roto' % (len(slugs), fallos))
    if not args.only:
        n_en, f_en = comprobar_en(None)
        print('---')
        print('%d producto(s) EN comprobado(s) · %d con el nombre roto' % (n_en, f_en))
        fallos += f_en
    sys.exit(1 if fallos else 0)


if __name__ == '__main__':
    main()
