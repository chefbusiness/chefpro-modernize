#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8I — Inserción QUIRÚRGICA de «Cómo Montar una Pastelería»
(`guia-pasteleria-obrador`, producto 48) en los 8 posts de su universo
(research §13.2). Clonado de `fase8h-manual-chef-blog.py`, del que hereda el
gate de reversibilidad byte a byte.

QUÉ CAMBIA RESPECTO A `fase8h` (y por qué):

1. Aquí la tabla del research (§13.2) es TOTALMENTE explícita y sin huecos:
   dice, post a post, si hay sustitución de banner o sólo enlace, y cuál es
   la víctima. No hace falta una `PRIORIDAD_SUSTITUIR` de respaldo como en
   `fase8h` — con sólo 3 posts a sustituir y los 3 verificados contra el
   `.md` real, un candidato inesperado es un error del research o del script,
   no un hueco a rellenar: el script ABORTA en vez de improvisar.

2. Ganancia neta para el 48: **3 banners** (los 3 posts de pastelería). Los
   otros 5 del universo de 8 reciben SÓLO el párrafo de enlace contextual —
   sus banners no se tocan para hacerle sitio al 48.

3. Miswiring independiente, en la MISMA pasada: `libreria-de-prompts-para-
   panadero-consultor-pro-ai` y `libreria-de-prompts-para-panaderia-creativa-
   ai` llevan `kit-tareas-pasteleria` de primer banner —el kit de la OTRA
   línea— en vez de `kit-tareas-panaderia`. Se corrige aquí porque es la
   sesión que tiene el research delante, pero es un fix AJENO al producto 48:
   no cuenta como banner del 48 y no está sujeto a `NUNCA` (no es su banner).

4. `NUNCA` (research, última viñeta de §13.2): `kit-tareas-pasteleria`,
   `kit-escandallos`, `pack-appcc` y `guia-food-cost` (prefijo de
   `guia-food-cost-ingenieria-menu`) — cross-sell directo de la guía; jamás
   se sacrifican para hacerle hueco a ella misma. `PRODUCTO` también, por si
   algún día se reejecuta sobre un post que ya lo lleva de rebote.

5. Dos de los cinco posts «sólo enlace» (`chocolatería-creativa` y
   `chocolatero-consultor-pro`) reciben un enlace HONESTO: la guía es de
   pastelería, no de chocolatería —no dice temperar ni bombonería—, así que
   el párrafo enlaza por el esqueleto de decisión que comparte cualquier
   obrador dulce (licencias, coste de apertura, plan financiero), nunca por
   la técnica. Mismo cuidado en los dos posts de panadería.

Hace, por post, sólo lo que dice el informe:
  1. (3 posts) sustituye UN banner por el del 48, con el MISMO `banner()` y
     UTM del ensamblador `fase8c-libreria-assemble.py`;
  1bis. (2 posts) sustituye el banner mal cableado `kit-tareas-pasteleria`
     por `kit-tareas-panaderia` (mismo mecanismo, producto distinto);
  2. añade un párrafo con enlace contextual (sin UTM en el texto) en los 8;
  3. actualiza el `modDate`.
Y lo demuestra: deshace las ediciones en orden inverso y exige que el texto
vuelva a ser IDÉNTICO al original, byte a byte.

    python3 scripts/astro-migration/fase8i-guia-pasteleria-blog.py                # dry-run (8 posts)
    python3 scripts/astro-migration/fase8i-guia-pasteleria-blog.py --dry-run      # idéntico, explícito
    python3 scripts/astro-migration/fase8i-guia-pasteleria-blog.py --aplicar
    python3 scripts/astro-migration/fase8i-guia-pasteleria-blog.py --informe informe.txt
Después: python3 scripts/astro-migration/fase8b-regen-lastmod.py
"""
import argparse
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BLOG = ROOT / 'astro-site/src/content/blog/es'
PRODUCTO = 'guia-pasteleria-obrador'
URL = 'https://aichef.pro/guia-pasteleria-obrador'
HOY = '2026-09-10'

# Cross-sell directo de la guía (research §13.2, última viñeta): jamás se
# retiran del blog para hacerle hueco al 48. `guia-food-cost` cubre el slug
# completo `guia-food-cost-ingenieria-menu`. `PRODUCTO` por si se reejecuta
# sobre un post que ya lo lleva.
NUNCA = ('kit-tareas-pasteleria', 'kit-escandallos', 'pack-appcc',
         'guia-food-cost', PRODUCTO)

# Víctima declarada por post para el banner del 48 (research §13.2). Sólo 3
# posts —los de pastelería— sustituyen un banner por el suyo; los otros 5 del
# universo de 8 van en `SOLO_ENLACE` sin tocar ninguno de sus tres.
SUSTITUIR = {
    'libreria-de-prompts-para-pastelero-consultor-pro-ai': 'kit-plan-financiero',
    'libreria-de-prompts-para-pasteleria-creativa-ai': 'pro-prompts-ebook',
    'ai-chef-pro-un-chatgpt-para-la-pasteleria-profesional-usos-y-aplicaciones':
        'guia-restaurante-gastronomico',
}

# Miswiring AJENO al 48 (research §13.2, filas de panadería): estos dos posts
# llevan el kit de TAREAS DE PASTELERÍA en vez del de panadería. Se corrige en
# la misma pasada porque comparte gate y ventana de mantenimiento, no porque
# el 48 tenga nada que ver. (post -> (banner_viejo, banner_nuevo))
MISWIRING = {
    'libreria-de-prompts-para-panadero-consultor-pro-ai':
        ('kit-tareas-pasteleria', 'kit-tareas-panaderia'),
    'libreria-de-prompts-para-panaderia-creativa-ai':
        ('kit-tareas-pasteleria', 'kit-tareas-panaderia'),
}

A = '<a href="%s">Cómo Montar una Pastelería</a>' % URL

# Los 3 posts con banner FIJADO (§13.2): sustituyen un banner por el del 48 Y
# reciben además su propio párrafo de enlace contextual.
POSTS = {
    'libreria-de-prompts-para-pastelero-consultor-pro-ai':
        'Estos prompts resuelven la consultoría del obrador que ya existe; la '
        'secuencia completa de decisiones para que exista —qué local sirve, '
        'cuánto cuesta abrir de verdad y el plan financiero a tres años hasta '
        'el punto de equilibrio— está desarrollada en la guía ' + A + '.',
    'libreria-de-prompts-para-pasteleria-creativa-ai':
        'Una carta creativa se sostiene si detrás hay un obrador capaz de '
        'producirla cada día: los metros que exige, el frío del que depende '
        'cada elaboración y el margen real de cada familia. Esa carta de '
        'apertura de treinta referencias, con su criterio de margen, es uno '
        'de los veinte capítulos de la guía ' + A + '.',
    'ai-chef-pro-un-chatgpt-para-la-pasteleria-profesional-usos-y-aplicaciones':
        'La IA ayuda a decidir mejor en un obrador que ya funciona. Todo lo '
        'que hay que decidir ANTES de que exista —el local, las licencias, la '
        'maquinaria y el plan financiero hasta el punto de equilibrio— es el '
        'contenido de la guía ' + A + '.',
}

# Los 5 posts que reciben SÓLO enlace contextual (§13.2: «los otros 5 del
# universo de 8»), sin tocar ninguno de sus tres banners para el 48. Dos de
# ellos (panadero-consultor-pro, panaderia-creativa) sí llevan el fix aparte
# del miswiring, declarado en `MISWIRING`.
SOLO_ENLACE = {
    'libreria-de-prompts-para-panadero-consultor-pro-ai':
        'Montar un obrador de panadería y uno de pastelería comparten el '
        'mismo esqueleto de decisión —registro sanitario, coste de apertura '
        'partida a partida y plan financiero hasta el punto de equilibrio—; '
        'lo que cambia es la técnica, que no es lo que cubre este agente. Ese '
        'esqueleto, con sus ocho Excel, es el de la guía ' + A + '.',
    'libreria-de-prompts-para-panaderia-creativa-ai':
        'Diseñar una viennoiserie de autor no dice si el obrador que la '
        'produce es viable: depende del local, la maquinaria y el margen '
        'real de cada referencia. Ese criterio de apertura —pensado para '
        'pastelería, pero con el mismo esqueleto administrativo que un '
        'obrador de panadería— está en la guía ' + A + '.',
    'libreria-de-prompts-para-chocolateria-creativa-ai':
        'El temperado y el bombón no están en esta guía: es de pastelería, '
        'no de chocolatería. Lo que sí comparte cualquier obrador dulce es el '
        'camino de licencias, coste de apertura y plan financiero hasta el '
        'punto de equilibrio, que es el contenido de la guía ' + A + '.',
    'libreria-de-prompts-para-chocolatero-consultor-pro-ai':
        'La consultoría de chocolate resuelve el proceso; abrir el obrador '
        'que lo aloja es una decisión previa y distinta, con su local, su '
        'maquinaria y su registro sanitario. Esa hoja de ruta —pensada para '
        'pastelería, pero compartida por cualquier obrador dulce— está en la '
        'guía ' + A + '.',
    'ia-para-panaderias':
        'La IA ordena la producción y la fermentación de un obrador que ya '
        'existe; las decisiones de antes de que exista —cuánto cuesta abrir, '
        'qué licencia toca y si el local aguanta la carga del forjado— son '
        'las de la guía ' + A + ', pensada para pastelería pero con el mismo '
        'camino administrativo que una panadería.',
}

RX_ASIDE = re.compile(r'<aside class="not-prose[^"]*">.*?utm_medium=banner.*?</aside>', re.S)
RX_SLUG = re.compile(r'href="/([a-z0-9-]+)\?utm_source=blog')
RX_MD_H2 = re.compile(r'^## ', re.M)
RX_HTML_H2 = re.compile(r'<h2\b')
RX_HTML_H3 = re.compile(r'<h3\b')
RX_FRONTMATTER = re.compile(r'^---\n.*?\n---\n', re.S)


def cargar_ensamblador():
    ruta = ROOT / 'scripts/astro-migration/fase8c-libreria-assemble.py'
    spec = importlib.util.spec_from_file_location('asm', ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fin_frontmatter(texto):
    m = RX_FRONTMATTER.match(texto)
    return m.end() if m else 0


def elegir_ancla(texto):
    """Punto de inserción del párrafo: primer heading (md o, si no hay
    ninguno, HTML h2/h3) que tenga texto de introducción delante y balance de
    `<div>` en cero (fuera de cualquier bloque congelado de WordPress)."""
    inicio = fin_frontmatter(texto)
    for rx, modo in ((RX_MD_H2, 'md'), (RX_HTML_H2, 'html'), (RX_HTML_H3, 'html')):
        candidatos = [m.start() for m in rx.finditer(texto)]
        if not candidatos:
            continue
        for pos in candidatos:
            antes = texto[inicio:pos].strip()
            if not antes:
                continue
            seg = texto[:pos]
            if seg.count('<div') != seg.count('</div>'):
                continue
            m2 = re.search(r'\n(#{1,6} .{0,80}|<h[1-6][^>]*>.{0,80})', texto[pos:pos + 200])
            titulo = m2.group(1) if m2 else texto[pos:pos + 60]
            return pos, modo, titulo.strip()
    sys.exit('sin ancla válida para el párrafo de enlace')


def insertar_parrafo(texto, cuerpo):
    """Devuelve (texto_nuevo, pos, insertado, titulo_ancla)."""
    pos, modo, titulo = elegir_ancla(texto)
    parrafo = '<p>' + cuerpo + '</p>'
    if modo == 'md':
        antes = '' if texto[:pos].endswith('\n\n') else '\n'
        insertado = antes + parrafo + '\n\n'
    else:
        insertado = parrafo
    return texto[:pos] + insertado + texto[pos:], pos, insertado, titulo


def procesar(slug, texto, mod, prods, cuerpo_parrafo):
    """(salida, detalle_banner, detalle_enlace, gate_ok) — salida None = no
    se toca el post (ya enlaza al producto)."""
    if URL in texto:
        return None, None, None, None

    asides = RX_ASIDE.findall(texto)
    if len(asides) != 3:
        sys.exit('%s: esperaba 3 banners, hay %d' % (slug, len(asides)))
    slugs_banner = [RX_SLUG.search(a).group(1) for a in asides]

    trabajo = texto
    viejo_prod = nuevo_prod = None
    viejo_mis = nuevo_mis = None
    detalle_banner = 'ninguno (sólo enlace)'

    if slug in SUSTITUIR:
        victima = SUSTITUIR[slug]
        if victima not in slugs_banner:
            sys.exit('%s: la víctima declarada (%s) no está en el post (tiene %s)'
                      % (slug, victima, slugs_banner))
        if victima.startswith(NUNCA):
            sys.exit('%s: la víctima declarada (%s) está en NUNCA' % (slug, victima))
        viejo_prod = asides[slugs_banner.index(victima)]
        nuevo_prod = mod.banner(PRODUCTO, prods, slug, 'es')
        assert trabajo.count(viejo_prod) == 1
        trabajo = trabajo.replace(viejo_prod, nuevo_prod)
        detalle_banner = '%s → %s (banner del 48)' % (victima, PRODUCTO)

    if slug in MISWIRING:
        vieja_slug, nueva_slug = MISWIRING[slug]
        if vieja_slug not in slugs_banner:
            sys.exit('%s: el banner mal cableado (%s) no está' % (slug, vieja_slug))
        viejo_mis = asides[slugs_banner.index(vieja_slug)]
        nuevo_mis = mod.banner(nueva_slug, prods, slug, 'es')
        assert trabajo.count(viejo_mis) == 1
        trabajo = trabajo.replace(viejo_mis, nuevo_mis)
        nota_mis = '%s → %s (fix miswiring, ajeno al 48)' % (vieja_slug, nueva_slug)
        detalle_banner = nota_mis if detalle_banner.startswith('ninguno') \
            else detalle_banner + '; ' + nota_mis

    tras_banner = trabajo
    tras_parrafo, pos, insertado, titulo = insertar_parrafo(tras_banner, cuerpo_parrafo)

    md_old = re.search(r'^modDate: (\d{4}-\d{2}-\d{2})$', tras_parrafo, re.M)
    assert md_old, '%s: sin modDate' % slug
    salida = tras_parrafo.replace(md_old.group(0), 'modDate: ' + HOY, 1)

    # Gate: deshacer las ediciones en orden inverso (modDate, párrafo, banner
    # de miswiring, banner del 48) y exigir que el resultado sea el original
    # byte a byte.
    d1 = salida.replace('modDate: ' + HOY, md_old.group(0), 1)
    assert d1 == tras_parrafo, '%s: no se pudo deshacer el modDate' % slug
    d2 = d1[:pos] + d1[pos + len(insertado):]
    assert d2 == tras_banner, '%s: no se pudo deshacer el párrafo' % slug
    if nuevo_mis is not None:
        assert d2.count(nuevo_mis) == 1
        d2 = d2.replace(nuevo_mis, viejo_mis, 1)
    if nuevo_prod is not None:
        assert d2.count(nuevo_prod) == 1
        d2 = d2.replace(nuevo_prod, viejo_prod, 1)
    if d2 != texto:
        sys.exit('%s: el gate de reversibilidad NO cuadra' % slug)
    assert len(RX_ASIDE.findall(salida)) == 3

    return salida, detalle_banner, (pos, titulo, cuerpo_parrafo), True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--aplicar', action='store_true')
    ap.add_argument('--dry-run', action='store_true',
                     help='no hace nada distinto: dry-run ya es el comportamiento por defecto')
    ap.add_argument('--informe', help='ruta donde volcar el informe además de imprimirlo')
    args = ap.parse_args()
    mod = cargar_ensamblador()
    prods = mod.catalogo_productos()
    if PRODUCTO not in prods:
        sys.exit('el producto no está en products-catalog.ts')

    todos = {}
    todos.update(POSTS)
    todos.update(SOLO_ENLACE)
    assert len(todos) == 8, 'se esperaban 8 posts en el universo, hay %d' % len(todos)

    lineas = []

    def out(s=''):
        print(s)
        lineas.append(s)

    out('Fase 8I — %s posts · producto %s (%s)' % (
        len(todos), PRODUCTO, 'APLICANDO' if args.aplicar else 'dry-run'))
    out('')

    saltados = []
    for slug in todos:
        ruta = BLOG / (slug + '.md')
        if not ruta.exists():
            sys.exit('%s: el .md no existe en %s' % (slug, BLOG))
        texto = ruta.read_text(encoding='utf-8')
        salida, detalle_banner, info_enlace, gate_ok = procesar(
            slug, texto, mod, prods, todos[slug])

        out('=== %s ===' % slug)
        if salida is None:
            out('  SKIP — ya enlaza a %s (idempotente)' % URL)
            saltados.append(slug)
            out('')
            continue

        pos, titulo, parrafo = info_enlace
        out('  Banner sustituido: %s' % detalle_banner)
        out('  Posición del enlace: byte %d, antes de: %s' % (pos, titulo))
        out('  Enlace contextual: "%s"' % parrafo)
        out('  Gate de reversibilidad: %s' % ('OK' if gate_ok else 'FALLO'))
        out('  Delta de tamaño: +%d bytes' % (len(salida) - len(texto)))
        if args.aplicar:
            ruta.write_text(salida, encoding='utf-8')
            out('  ESCRITO')
        out('')

    out('Resumen: %d/%d posts con banner del 48 sustituido, %d/%d posts sólo-enlace, '
        '%d posts con fix de miswiring (ajeno al 48), %d saltados (idempotente).' % (
            len(SUSTITUIR), len(todos), len(SOLO_ENLACE), len(todos),
            len(MISWIRING), len(saltados)))
    if not args.aplicar:
        out('(dry-run: nada escrito; --aplicar para aplicar)')

    if args.informe:
        Path(args.informe).write_text('\n'.join(lineas) + '\n', encoding='utf-8')
        print('\nInforme volcado en %s' % args.informe)


if __name__ == '__main__':
    main()
