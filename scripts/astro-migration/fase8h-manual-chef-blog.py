#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8H — Inserción QUIRÚRGICA del «Manual del Chef Ejecutivo» en el blog ES:
5 posts con banner FIJADO (research §13.2) + 8 posts con SÓLO enlace
contextual (research §13.1). Clonado de `fase8g-manual-manager-blog.py`, del
que hereda el gate de reversibilidad byte a byte.

QUÉ CAMBIA RESPECTO A `fase8g` (y por qué):

1. `NUNCA` y `PRIORIDAD_SUSTITUIR` son OTRAS. Los cross-sell de ESTE manual
   son `kit-tareas*`, `pack-appcc`, `kit-escandallos`, `guia-food-cost` y el
   `manual-manager`: sustituir cualquiera de esos banners sería quitarnos
   ventas propias, así que van a `NUNCA`. El primer sacrificio pasa a ser
   `kit-inventario` (la merma por PRODUCTO es suya; este manual mide la merma
   agregada por partida), después los planes de negocio y las guías de
   apertura, que son de abrir un local y no de dirigir una cocina.

2. La víctima se declara POR POST (`SUSTITUIR`), tomada de la tabla §13.2 del
   research, y `PRIORIDAD_SUSTITUIR` queda de RESPALDO. Hacía falta: con la
   lista genérica, `que-son-las-mermas-en-cocina` habría perdido el banner de
   `kit-inventario` (el más afín al tema del post) en lugar del de
   `plan-negocio-cocteleria-eventos`, que es el que la tabla marca. Si la
   víctima declarada no está en el post o cae en `NUNCA`, se recurre a la
   prioridad; si tampoco hay candidato, NO se fuerza nada.

3. `mise-en-place` es el caso previsto: sus tres banners (`kit-tareas`,
   `kit-escandallos`, `pack-appcc`) están los tres en `NUNCA`. La regla manda
   sobre la tabla, así que **se queda sin banner del manual** y se anota. Sí
   recibe su párrafo de enlace contextual: no cuesta un banner a nadie y es
   el entrante más valioso del post (regla capital: cero huérfanas). Ese es
   el modo LINK-ONLY del informe.

4. Modo `--solo-enlace`: procesa los 8 posts de §13.1, que reciben enlace
   contextual y NINGÚN banner (sus tres banners son de otros productos y
   están bien donde están). Mismo gate de reversibilidad.

Hace, por post, sólo lo que dice el informe:
  1. (modo banner) sustituye UN banner por el del manual, con el MISMO
     `banner()` y UTM del ensamblador `fase8c-libreria-assemble.py`;
  2. añade un párrafo con enlace contextual (sin UTM en el texto);
  3. actualiza el `modDate`.
Y lo demuestra: deshace las ediciones en orden inverso y exige que el texto
vuelva a ser IDÉNTICO al original, byte a byte.

    python3 scripts/astro-migration/fase8h-manual-chef-blog.py                  # dry-run (5 posts)
    python3 scripts/astro-migration/fase8h-manual-chef-blog.py --aplicar
    python3 scripts/astro-migration/fase8h-manual-chef-blog.py --solo-enlace    # dry-run (8 posts)
    python3 scripts/astro-migration/fase8h-manual-chef-blog.py --solo-enlace --aplicar
Después: python3 scripts/astro-migration/fase8b-regen-lastmod.py
"""
import argparse
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BLOG = ROOT / 'astro-site/src/content/blog/es'
PRODUCTO = 'manual-chef-ejecutivo'
URL = 'https://aichef.pro/manual-chef-ejecutivo'
HOY = '2026-09-06'

# Respaldo cuando la víctima declarada no está o cae en NUNCA. `kit-inventario`
# es el primer sacrificio (mermas por producto y recepción, que este manual NO
# toca), después planes de negocio y guías de apertura —son de abrir un local,
# no de dirigir una cocina—, y por último los kits de gestión y financiero.
PRIORIDAD_SUSTITUIR = [
    'kit-inventario',
    'plan-negocio-',
    'guia-restaurante-', 'guia-dark-kitchen', 'guia-panaderia-obrador',
    'kit-gestion-personal',
    'kit-plan-financiero',
    'mega-pack',
]
# Cross-sell directo del manual (research §13.1 «Salientes»): jamás se retiran
# del blog para hacerle hueco. `kit-tareas` como prefijo cubre también todos
# los `kit-tareas-<concepto>`; `guia-food-cost` cubre el slug completo.
NUNCA = ('kit-tareas', 'pack-appcc', 'kit-escandallos', 'guia-food-cost',
         'manual-manager', PRODUCTO)

# Víctima declarada por post (research §13.2). `mise-en-place` la tiene en
# NUNCA a propósito: queda documentado que la tabla lo pedía y que la regla
# ganó.
SUSTITUIR = {
    'libreria-de-prompts-para-chef-ejecutivo-pro-ai': 'kit-inventario',
    'escandallos-ia-cocina-profesional': 'plan-negocio-bar-restaurante',
    'que-son-las-mermas-en-cocina': 'plan-negocio-cocteleria-eventos',
    'mise-en-place': 'kit-escandallos',
    'tipos-de-cortes-en-la-cocina-profesional': 'guia-restaurante-gastronomico',
}

A = '<a href="%s">Manual del Chef Ejecutivo</a>' % URL

# Los 5 posts con banner fijado (§13.2).
POSTS = {
    'libreria-de-prompts-para-chef-ejecutivo-pro-ai':
        'Los prompts de este agente resuelven preguntas sueltas; el criterio '
        'completo para dirigir la cocina —brigada y partidas, producción '
        'diaria, fichas técnicas, indicadores y seguridad alimentaria, con '
        'sus siete herramientas Excel— está desarrollado en el ' + A + '.',
    'escandallos-ia-cocina-profesional':
        'El escandallo dice cuánto cuesta un plato; la ficha técnica de '
        'proceso dice cómo se hace para que salga igual lo haga quien lo '
        'haga. Esa otra mitad —con su plantilla, sus alérgenos de proceso y '
        'su vida útil— es una de las siete herramientas del ' + A + '.',
    'que-son-las-mermas-en-cocina':
        'Medir la merma es el primer paso; saber de qué partida sale y qué '
        'conversación toca cuando se dispara tres semanas seguidas es el '
        'segundo, y tiene su cuadro de mando semanal en el ' + A + '.',
    'mise-en-place':
        'La mise en place se sostiene cuando hay detrás una planificación de '
        'producción: cuánto se produce hoy en cada partida a partir de los '
        'cubiertos previstos y del stock ya elaborado. Esa plantilla, con su '
        'lista de producción diaria imprimible, es una de las siete '
        'herramientas del ' + A + '.',
    'tipos-de-cortes-en-la-cocina-profesional':
        'Que el corte salga igual en todos los turnos no es cuestión de '
        'memoria, sino de ficha técnica de proceso y de una rúbrica que '
        'evalúe la competencia de cada cocinero. Las dos plantillas van en '
        'el ' + A + '.',
}

# Los 8 posts que reciben SÓLO enlace contextual (§13.1), sin tocar banners.
SOLO_ENLACE = {
    'alergenos':
        'La declaración de alérgenos de la carta es una cosa; gestionarlos '
        'dentro de la cocina —contacto y traza en cada elaboración, '
        'utensilios y superficies compartidos, sustituciones posibles y qué '
        'se canta en el pase— es otra, y tiene su capítulo y su ficha en el '
        + A + '.',
    'gestion-de-alergenos-con-ia-en-restaurantes':
        'Para llevar el alérgeno al proceso —no sólo a la carta— la ficha '
        'técnica de proceso registra contacto, traza, utensilio compartido y '
        'sustitución posible de cada elaboración. Es una de las siete '
        'herramientas del ' + A + '.',
    'ia-gestion-alergenos-hosteleria':
        'Quien dirige la cocina responde de que el protocolo se cumpla en el '
        'pase, no sólo de que la carta esté bien: ese criterio, con la norma '
        'citada y la ficha de proceso, está en el ' + A + '.',
    'appcc-seguridad-alimentaria-ia-hosteleria':
        'Los registros son la mitad del trabajo; la otra mitad es el '
        'criterio de quien dirige la cocina: qué temperaturas gobiernan cada '
        'proceso, de qué respondes tú y qué mira el inspector. Está '
        'desarrollado en el ' + A + '.',
    '12-innovaciones-ia-cocinas-profesionales':
        'La tecnología ordena lo que ya tiene sistema: si la producción, la '
        'ficha técnica y el pase no están escritos, no hay herramienta que '
        'los arregle. El ' + A + ' es ese sistema, con sus siete plantillas '
        'de cocina.',
    'como-la-ia-transformara-el-rol-de-los-chefs':
        'El chef que dirige dedica cada vez menos tiempo a cocinar y más a '
        'decidir: brigada, producción, estándares, costes y seguridad '
        'alimentaria. Ese oficio, el de dirigir la cocina, es justo el del '
        + A + '.',
    'de-chef-tradicional-a-chef-ia':
        'El salto no es sólo de herramientas: es pasar de ejecutar a dirigir '
        '—organigrama, fichas técnicas, indicadores de cocina y evaluación '
        'técnica de la brigada—. Ese camino está escrito en el ' + A + '.',
    'gestion-personal-hosteleria-ia-reducir-rotacion':
        'En cocina, retener pasa también por la evaluación técnica y el plan '
        'de desarrollo: qué competencias domina cada persona, cuál es su '
        'próxima partida a aprender y qué se le pide para ascender. Esa '
        'plantilla va en el ' + A + '.',
}

RX_ASIDE = re.compile(r'<aside class="not-prose[^"]*">.*?utm_medium=banner.*?</aside>', re.S)
RX_SLUG = re.compile(r'href="/([a-z0-9-]+)\?utm_source=blog')
RX_MD_H2 = re.compile(r'^## ', re.M)
RX_HTML_H2 = re.compile(r'<h2\b')
# `tipos-de-cortes-en-la-cocina-profesional` (molde WordPress) NO tiene ni un
# `## ` ni un `<h2`: su encabezado de mayor rango es `<h3 class="wp-block-heading">`.
# Sin este tercer intento el script abortaba con «sin ancla válida».
RX_HTML_H3 = re.compile(r'<h3\b')
RX_FRONTMATTER = re.compile(r'^---\n.*?\n---\n', re.S)


def cargar_ensamblador():
    ruta = ROOT / 'scripts/astro-migration/fase8c-libreria-assemble.py'
    spec = importlib.util.spec_from_file_location('asm', ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def elegir_victima(slug, slugs):
    """Víctima declarada en §13.2; si no vale, la lista de prioridad.

    Devuelve (slug_victima, motivo) o (None, motivo). NO aborta: un post sin
    candidato fuera de NUNCA se queda sin banner (instrucción explícita)."""
    declarada = SUSTITUIR.get(slug)
    if declarada:
        if declarada.startswith(NUNCA):
            motivo = 'la declarada (%s) está en NUNCA' % declarada
        elif declarada not in slugs:
            motivo = 'la declarada (%s) no está en el post' % declarada
        else:
            return declarada, 'declarada en §13.2'
    else:
        motivo = 'sin víctima declarada'
    for pref in PRIORIDAD_SUSTITUIR:
        for s in slugs:
            if s.startswith(pref) and not s.startswith(NUNCA):
                return s, motivo + ' → respaldo por prioridad'
    return None, motivo + ' → ningún candidato fuera de NUNCA'


def fin_frontmatter(texto):
    m = RX_FRONTMATTER.match(texto)
    return m.end() if m else 0


def elegir_ancla(texto):
    """Punto de inserción del párrafo: primer heading (md o, si no hay
    ninguno, HTML) que tenga texto de introducción delante y balance de
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


def procesar(slug, texto, mod, prods, con_banner, parrafos):
    """(salida, victima, detalle) — salida None = no se toca el post."""
    if URL in texto:
        return None, None, 'YA enlaza al producto — no se toca (idempotente)'

    victima = None
    tras_banner, viejo, nuevo = texto, None, None
    nota = ''
    if con_banner:
        asides = RX_ASIDE.findall(texto)
        if len(asides) != 3:
            sys.exit('%s: esperaba 3 banners, hay %d' % (slug, len(asides)))
        slugs = [RX_SLUG.search(a).group(1) for a in asides]
        victima, motivo = elegir_victima(slug, slugs)
        if victima is None:
            nota = 'SIN BANNER (%s) → sólo enlace contextual; ' % motivo
        else:
            viejo = asides[slugs.index(victima)]
            nuevo = mod.banner(PRODUCTO, prods, slug, 'es')
            assert texto.count(viejo) == 1
            tras_banner = texto.replace(viejo, nuevo)
            nota = '%s; ' % motivo

    tras_parrafo, pos, insertado, titulo = insertar_parrafo(tras_banner, parrafos[slug])

    md_old = re.search(r'^modDate: (\d{4}-\d{2}-\d{2})$', tras_parrafo, re.M)
    assert md_old, '%s: sin modDate' % slug
    salida = tras_parrafo.replace(md_old.group(0), 'modDate: ' + HOY, 1)

    # Gate: deshacer las ediciones en orden inverso (modDate, párrafo, banner)
    # y exigir que el resultado sea el original byte a byte.
    d1 = salida.replace('modDate: ' + HOY, md_old.group(0), 1)
    assert d1 == tras_parrafo, '%s: no se pudo deshacer el modDate' % slug
    d2 = d1[:pos] + d1[pos + len(insertado):]
    assert d2 == tras_banner, '%s: no se pudo deshacer el párrafo' % slug
    if victima is not None:
        assert d2.count(nuevo) == 1
        d2 = d2.replace(nuevo, viejo, 1)
    if d2 != texto:
        sys.exit('%s: el gate de reversibilidad NO cuadra' % slug)
    if con_banner:
        assert len(RX_ASIDE.findall(salida)) == 3

    return salida, victima, nota + 'enlace antes de «%s»' % titulo


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--aplicar', action='store_true')
    ap.add_argument('--solo-enlace', action='store_true',
                    help='procesa los 8 posts de §13.1 (enlace contextual, sin tocar banners)')
    args = ap.parse_args()
    mod = cargar_ensamblador()
    prods = mod.catalogo_productos()
    if PRODUCTO not in prods:
        sys.exit('el producto no está en products-catalog.ts')

    parrafos = SOLO_ENLACE if args.solo_enlace else POSTS
    con_banner = not args.solo_enlace
    print('modo %s · %d posts · producto %s' % (
        'SÓLO ENLACE (§13.1)' if args.solo_enlace else 'BANNER + ENLACE (§13.2)',
        len(parrafos), PRODUCTO))

    saltados, sin_banner = [], []
    for slug in parrafos:
        ruta = BLOG / (slug + '.md')
        if not ruta.exists():
            sys.exit('%s: el .md no existe en %s' % (slug, BLOG))
        texto = ruta.read_text(encoding='utf-8')
        salida, victima, detalle = procesar(slug, texto, mod, prods, con_banner, parrafos)
        if salida is None:
            saltados.append((slug, detalle))
            print('%s %-48s %s' % ('SKIP  ', slug, detalle))
            continue
        if con_banner and victima is None:
            sin_banner.append((slug, detalle))
        print('%s %-48s sustituye %-30s +%d bytes  %s' % (
            'APPLY ' if args.aplicar else 'dry   ', slug, victima or '—',
            len(salida) - len(texto), detalle))
        if args.aplicar:
            ruta.write_text(salida, encoding='utf-8')

    if sin_banner:
        print('\n%d post(s) sin banner del manual (NUNCA manda sobre §13.2, no se fuerza):' % len(sin_banner))
        for slug, detalle in sin_banner:
            print('  - %s: %s' % (slug, detalle))
    if saltados:
        print('\n%d post(s) saltados:' % len(saltados))
        for slug, detalle in saltados:
            print('  - %s: %s' % (slug, detalle))
    if not args.aplicar:
        print('\n(dry-run: nada escrito; --aplicar para aplicar)')


if __name__ == '__main__':
    main()
