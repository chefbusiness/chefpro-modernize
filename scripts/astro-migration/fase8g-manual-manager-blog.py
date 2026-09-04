#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8G — Inserción QUIRÚRGICA del «Manual del Manager de Restaurante» en los
5 posts ES afines (SPEC §1 D16 y §10.3; refutación C3 del 2026-09-04).

POR QUÉ NO ES `fase8f` COPIADO SIN MÁS (refutación C3): los 5 posts objetivo
YA tienen sus 3 banners (política del 31-08-2026), y la `PRIORIDAD_SUSTITUIR`
de `fase8f` está escrita para un producto de food cost — protege
`kit-escandallos`/`kit-inventario` y sacrifica primero `kit-tareas-`,
`kit-gestion-personal` y `pack-appcc`. Para el Manual esos tres son
precisamente sus cross-sell más afines (§10.3 «Salientes»): ejecutar la lista
de `fase8f` tal cual borraría del blog justo los productos que la propia
landing recomienda. Este script trae su PROPIA `PRIORIDAD_SUSTITUIR` (con
`kit-escandallos` como primer sacrificio) y su propio `NUNCA`
(`kit-gestion-personal`, `kit-tareas*`, `pack-appcc`).

También difiere en el ANCLAJE del párrafo de enlace: `fase8f` ancla siempre
en el primer `^## ` markdown. Uno de los 5 posts
(`libreria-de-prompts-para-gerente-de-restaurante-pro-ai`) no tiene NINGÚN
`## ` — es molde WordPress con `<h2>` HTML pegado— y otro
(`gerente-de-restaurante-20-areas-clave...`) tiene su primer `## ` como
apertura literal del cuerpo, sin una sola frase de intro delante: anclar ahí
pondría el párrafo de venta como primera línea del artículo. `elegir_ancla()`
prueba primero `## ` markdown y si no hay ninguno cae a `<h2` HTML; en los
dos casos descarta el primer candidato si no hay texto de introducción antes
(usa el siguiente) y exige balance de `<div>` en cero en el punto de corte
(la guardia documentada en CLAUDE.md contra los bloques congelados de
WordPress: una inserción a medio `<div>` rompe el HTML del resto del post).

Por instrucción explícita: si algún post no tuviera NINGÚN banner sustituible
fuera de `NUNCA`, se deja SIN banner del manual y se anota — no se fuerza
nunca una sustitución sobre `NUNCA`.

Hace dos cosas y sólo dos, por post (igual que `fase8f`):
  1. sustituye UN banner existente (el menos afín, por lista de prioridad
     propia) por el del manual, con el MISMO `banner()` y UTM del ensamblador;
  2. añade un párrafo con enlace contextual (sin UTM en el texto) en el
     anclaje elegido.
Y lo demuestra: deshace las tres ediciones sobre el resultado (banner, párrafo
y modDate) y exige que el texto vuelva a ser IDÉNTICO al original, byte a
byte. También actualiza el `modDate`.

    python3 scripts/astro-migration/fase8g-manual-manager-blog.py            # dry-run
    python3 scripts/astro-migration/fase8g-manual-manager-blog.py --aplicar
Después: python3 scripts/astro-migration/fase8b-regen-lastmod.py
"""
import argparse
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BLOG = ROOT / 'astro-site/src/content/blog/es'
PRODUCTO = 'manual-manager-restaurante'
HOY = '2026-09-04'

# El banner que se SUSTITUYE en cada post: el menos afín de los tres
# publicados, para ESTE producto. Al contrario que en `fase8f`, aquí
# `kit-escandallos` es el primer sacrificio (no tiene nada que ver con
# gestión de equipo/normativa/reseñas) y las guías de apertura y planes de
# negocio le siguen; `kit-inventario` y `kit-plan-financiero` son los últimos
# recursos porque comparten algo de terreno (control operativo, finanzas).
PRIORIDAD_SUSTITUIR = [
    'kit-escandallos',
    'guia-food-cost-ingenieria-menu',
    'guia-restaurante', 'guia-dark-kitchen', 'guia-panaderia-obrador',
    'plan-negocio-',
    'kit-inventario',
    'kit-plan-financiero',
]
# Cross-sell directo del manual (§10.3 «Salientes» del research): jamás se
# retiran del blog para hueco del propio manual. `kit-tareas` como prefijo
# cubre también todos los `kit-tareas-<concepto>`.
NUNCA = ('kit-gestion-personal', 'kit-tareas', 'pack-appcc', PRODUCTO)

POSTS = {
    'gerente-de-restaurante-20-areas-clave-donde-la-ia-te-puede-ayudar':
        'Estas 20 áreas son el mapa; convertirlas en rutina semanal, con la '
        'normativa laboral vigente y las plantillas de cuadro de mando, '
        'cuadrante y cumplimiento legal, es el trabajo del '
        '<a href="https://aichef.pro/manual-manager-restaurante">Manual del Manager de Restaurante</a>.',
    'libreria-de-prompts-para-gerente-de-restaurante-pro-ai':
        'Los prompts de este agente responden preguntas puntuales; el '
        'criterio completo para dirigir el restaurante día a día —con las '
        'plantillas de cuadro de mando, formación y cumplimiento legal— '
        'está desarrollado en el '
        '<a href="https://aichef.pro/manual-manager-restaurante">Manual del Manager de Restaurante</a>.',
    'gestion-personal-hosteleria-ia-reducir-rotacion':
        'Reducir la rotación también se juega en la matriz de formación y '
        'polivalencia del equipo: el '
        '<a href="https://aichef.pro/manual-manager-restaurante">Manual del Manager de Restaurante</a> '
        'trae la plantilla de cross-training y el cálculo del coste real de '
        'una baja.',
    'rentabilidad-restaurante-kpis-metricas-2026':
        'El cuadro de mando semanal —con estos mismos KPIs llevados a las '
        '52 semanas del año, no sólo al cierre de mes— es una de las siete '
        'herramientas Excel del '
        '<a href="https://aichef.pro/manual-manager-restaurante">Manual del Manager de Restaurante</a>.',
    'ia-en-la-gestion-de-criticas-y-reputacion-de-restaurantes':
        'Responder bien la reseña es el primer paso; registrar la queja, '
        'los plazos autonómicos de la hoja de reclamaciones y el '
        'seguimiento hasta el cierre es el segundo, y tiene su propia '
        'plantilla en el '
        '<a href="https://aichef.pro/manual-manager-restaurante">Manual del Manager de Restaurante</a>.',
}

RX_ASIDE = re.compile(r'<aside class="not-prose[^"]*">.*?utm_medium=banner.*?</aside>', re.S)
RX_SLUG = re.compile(r'href="/([a-z0-9-]+)\?utm_source=blog')
RX_MD_H2 = re.compile(r'^## ', re.M)
RX_HTML_H2 = re.compile(r'<h2\b')
RX_FRONTMATTER = re.compile(r'^---\n.*?\n---\n', re.S)


def cargar_ensamblador():
    ruta = ROOT / 'scripts/astro-migration/fase8c-libreria-assemble.py'
    spec = importlib.util.spec_from_file_location('asm', ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def elegir_victima(slugs):
    """Devuelve el slug a sustituir, o None si ninguno es sustituible.

    NO aborta el proceso: por instrucción, un post sin candidato fuera de
    NUNCA se deja sin banner del manual (no se fuerza)."""
    for pref in PRIORIDAD_SUSTITUIR:
        for s in slugs:
            if s.startswith(pref) and not s.startswith(NUNCA):
                return s
    return None


def fin_frontmatter(texto):
    m = RX_FRONTMATTER.match(texto)
    return m.end() if m else 0


def elegir_ancla(texto):
    """Punto de inserción del párrafo: primer heading (md o, si no hay
    ninguno, HTML) que tenga texto de introducción delante y balance de
    `<div>` en cero (fuera de cualquier bloque congelado de WordPress)."""
    inicio = fin_frontmatter(texto)
    for rx, modo in ((RX_MD_H2, 'md'), (RX_HTML_H2, 'html')):
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
        break
    sys.exit('sin ancla válida para el párrafo de enlace')


def procesar(slug, texto, mod, prods):
    asides = RX_ASIDE.findall(texto)
    if len(asides) != 3:
        sys.exit('%s: esperaba 3 banners, hay %d' % (slug, len(asides)))
    slugs = [RX_SLUG.search(a).group(1) for a in asides]
    if PRODUCTO in slugs:
        sys.exit('%s: ya lleva el banner del producto' % slug)

    victima = elegir_victima(slugs)
    if victima is None:
        return None, None, 'SIN BANNER SUSTITUIBLE (los 3 son NUNCA / ningún candidato en la prioridad) — no se toca'

    viejo = asides[slugs.index(victima)]
    nuevo = mod.banner(PRODUCTO, prods, slug, 'es')
    assert texto.count(viejo) == 1
    tras_banner = texto.replace(viejo, nuevo)

    pos, modo, titulo = elegir_ancla(tras_banner)
    parrafo = '<p>' + POSTS[slug] + '</p>'
    if modo == 'md':
        antes = '' if tras_banner[:pos].endswith('\n\n') else '\n'
        insertado = antes + parrafo + '\n\n'
    else:
        insertado = parrafo
    tras_parrafo = tras_banner[:pos] + insertado + tras_banner[pos:]

    md_old = re.search(r'^modDate: (\d{4}-\d{2}-\d{2})$', tras_parrafo, re.M)
    assert md_old, '%s: sin modDate' % slug
    salida = tras_parrafo.replace(md_old.group(0), 'modDate: ' + HOY, 1)

    # Gate: deshacer las TRES ediciones (modDate, párrafo, banner), en orden
    # inverso, y exigir que el resultado sea el original byte a byte.
    d1 = salida.replace('modDate: ' + HOY, md_old.group(0), 1)
    assert d1 == tras_parrafo, '%s: no se pudo deshacer el modDate' % slug
    d2 = d1[:pos] + d1[pos + len(insertado):]
    assert d2 == tras_banner, '%s: no se pudo deshacer el párrafo' % slug
    assert d2.count(nuevo) == 1
    d3 = d2.replace(nuevo, viejo, 1)
    if d3 != texto:
        sys.exit('%s: el gate de reversibilidad NO cuadra' % slug)
    assert len(RX_ASIDE.findall(salida)) == 3

    return salida, victima, 'antes de «%s»' % titulo


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--aplicar', action='store_true')
    args = ap.parse_args()
    mod = cargar_ensamblador()
    prods = mod.catalogo_productos()
    if PRODUCTO not in prods:
        sys.exit('el producto no está en products-catalog.ts')

    sin_banner = []
    for slug in POSTS:
        ruta = BLOG / (slug + '.md')
        if not ruta.exists():
            sys.exit('%s: el .md no existe en %s' % (slug, BLOG))
        texto = ruta.read_text(encoding='utf-8')
        salida, victima, detalle = procesar(slug, texto, mod, prods)
        if salida is None:
            sin_banner.append((slug, detalle))
            print('%s %-58s %s' % ('SKIP  ', slug, detalle))
            continue
        print('%s %-58s sustituye %-32s +%d bytes  enlace %s' % (
            'APPLY ' if args.aplicar else 'dry   ', slug, victima,
            len(salida) - len(texto), detalle))
        if args.aplicar:
            ruta.write_text(salida, encoding='utf-8')

    if sin_banner:
        print('\n%d post(s) sin banner del manual (no forzado):' % len(sin_banner))
        for slug, detalle in sin_banner:
            print('  - %s: %s' % (slug, detalle))
    if not args.aplicar:
        print('\n(dry-run: nada escrito; --aplicar para aplicar)')


if __name__ == '__main__':
    main()
