#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8E — Inserta banners de producto en los posts del corpus que no tienen ninguno.

POR QUÉ EXISTE ESTE SCRIPT Y NO SE REUTILIZA EL ENSAMBLADOR
-----------------------------------------------------------
La política de John (2026-07-31) es MÍNIMO 3 banners de producto digital por
post, a tres alturas. Medido el 2026-08-31 sobre el `dist`: sólo **39 de 325
posts ES** la cumplían; **286 no tenían un solo banner**. Y la rotación de
productos del 2026-08-30 vive en `fase8c-libreria-assemble.py`, que **no sirve
aquí**: ese script RECONSTRUYE el cuerpo entero desde el `.txt` de bridge, así
que pasarlo por encima de un post publicado lo pisa (ya se llevó por delante
dos enlaces internos de `cocina-molecular` el 2026-08-01).

Este script hace lo contrario: **no genera nada, sólo INSERTA**. El cuerpo
original se conserva byte a byte y hay un gate que lo demuestra — se quitan del
resultado exactamente las cadenas insertadas y se compara con el original.

DÓNDE INSERTA
-------------
En puntos al ~30 %, ~58 % y ~85 % del cuerpo, buscando el encabezado más
cercano (`<h2>`, `<h3>` o Markdown `##`). Dos guardas:

  · **Nada dentro de los bloques congelados de WordPress.** `wp-block-blocksy-query`
    («También te puede interesar»), `wp-block-jetpack-donations` y el grupo
    «CHEFBUSINESS GROUP» traen encabezados FALSOS —hasta 105 en el corpus—; un
    banner ahí caería en mitad de un widget muerto.
  · **Nada dentro de un contenedor abierto.** Se exige balance 0 de
    div/figure/table/ul/ol/blockquote/aside en el offset: en Markdown una línea
    en blanco DENTRO de un `<div>` corta el bloque HTML y el resto se escaparía
    como texto plano. Esta guarda cubre además cualquier bloque congelado que no
    conozcamos (asume que hay una quinta familia: CLAUDE.md).

QUÉ PRODUCTOS ELIGE
-------------------
`rotar_productos()` del ensamblador, importado, no copiado. Se FIJA uno por
relevancia temática cuando el slug/título lo canta (un post de pizzería vende el
kit de pizzería) y los otros dos salen de la rotación determinista sembrada con
el slug: reejecutar no ensucia el diff y el catálogo se cubre entero.

Uso:
    python3 scripts/astro-migration/fase8e-banners-corpus.py            # dry-run
    python3 scripts/astro-migration/fase8e-banners-corpus.py --informe  # + reparto
    python3 scripts/astro-migration/fase8e-banners-corpus.py --aplicar
"""
import argparse
import collections
import datetime
import importlib.util
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BLOG = REPO / 'astro-site' / 'src' / 'content' / 'blog'
ASSEMBLE = Path(__file__).resolve().parent / 'fase8c-libreria-assemble.py'

N_BANNERS = 3
ALTURAS = (0.30, 0.58, 0.85)     # a qué fracción del cuerpo va cada banner
SEPARACION_MIN = 0.10            # dos banners nunca a menos del 10 % del cuerpo
VENTANA_ENCABEZADO = 0.12        # radio para preferir un encabezado al párrafo

FRONTMATTER = re.compile(r'\A---\n(.*?)\n---\n', re.S)
ENCABEZADO = re.compile(r'<h[23][ >]|^#{2,3} ', re.M)
FIN_PARRAFO = re.compile(r'</p>')
CONTENEDORES = ('div', 'figure', 'table', 'ul', 'ol', 'blockquote', 'aside')

# Bloques congelados del export de WordPress (CLAUDE.md). Se delimitan por firma
# ESTRUCTURAL: el `data-id` ata apertura y cierre. Adivinar dónde acaban ya se
# comió una FAQ entera el 2026-08-01.
BLOCKSY_ABRE = re.compile(r'<div data-id="([^"]+)" class="wp-block-blocksy-query">')
DONACIONES = re.compile(r'<div class="wp-block-jetpack-donations">.*?</div>\s*', re.S)
GRUPO_CB = re.compile(r'<div class="wp-block-group[^"]*"[^>]*>.*?CHEFBUSINESS GROUP.*?</div>', re.S)

# Relevancia temática: el PRIMER patrón que case fija ese producto. El orden
# importa — lo específico antes que lo genérico (nikkei antes que japonés).
TEMATICO = [
    ('guia-restaurante-nikkei', {'nikkei'}),
    ('kit-tareas-sushi-bar', {'sushi', 'sashimi', 'nigiri', 'maki'}),
    ('guia-restaurante-japones', {'japones', 'japonesa', 'ramen', 'izakaya', 'wagyu', 'umami'}),
    ('guia-restaurante-peruano', {'peruano', 'peruana', 'peru', 'ceviche', 'cebiche', 'pisco'}),
    ('guia-restaurante-mexicano', {'mexicano', 'mexicana', 'mexico', 'taco', 'tacos', 'mole', 'guacamole'}),
    ('kit-tareas-pizzeria', {'pizza', 'pizzas', 'pizzeria', 'napoletana'}),
    ('kit-tareas-hamburgueseria', {'hamburguesa', 'hamburguesas', 'hamburgueseria', 'burger', 'smash'}),
    ('kit-tareas-heladeria', {'helado', 'helados', 'heladeria', 'gelato', 'sorbete', 'sorbetes'}),
    ('kit-tareas-chocolateria', {'chocolate', 'chocolateria', 'bombon', 'bombones', 'cacao', 'praline'}),
    ('kit-tareas-pasteleria', {'pasteleria', 'reposteria', 'postre', 'postres', 'tarta', 'tartas', 'bizcocho'}),
    ('kit-tareas-panaderia', {'panaderia', 'obrador', 'masa', 'fermentacion', 'brioche', 'focaccia'}),
    ('kit-tareas-asador', {'asador', 'parrilla', 'brasa', 'brasas', 'barbacoa', 'ahumado', 'ahumados'}),
    ('kit-tareas-marisqueria', {'marisco', 'mariscos', 'marisqueria', 'pescado', 'pescados', 'ostras'}),
    ('kit-tareas-tapas-bar', {'tapas', 'tapa', 'gastrobar', 'pintxos', 'pinchos'}),
    ('kit-tareas-cafeteria', {'cafeteria', 'cafe', 'barista', 'brunch', 'espresso'}),
    ('kit-tareas-bar', {'coctel', 'cocteles', 'cocteleria', 'cocktail', 'bartender', 'mixologia', 'bar'}),
    ('kit-tareas-catering', {'catering', 'banquete', 'banquetes', 'eventos'}),
    ('kit-tareas-food-truck', {'truck', 'trucks', 'foodtruck', 'ambulante'}),
    ('kit-tareas-dark-kitchen', {'dark', 'delivery', 'domicilio', 'fantasma', 'ghost'}),
    ('kit-tareas-hotel', {'hotel', 'hoteles', 'hoteleria', 'buffet', 'room'}),
    ('kit-tareas-chef-privado', {'privado', 'showcooking'}),
    ('pack-appcc', {'appcc', 'haccp', 'alergeno', 'alergenos', 'higiene', 'trazabilidad', 'sanitario'}),
    ('kit-inventario', {'inventario', 'stock', 'merma', 'mermas', 'almacen', 'desperdicio'}),
    ('kit-escandallos', {'escandallo', 'escandallos', 'coste', 'costes', 'rentabilidad', 'margen', 'foodcost'}),
    ('kit-gestion-personal', {'personal', 'turnos', 'equipo', 'brigada', 'plantilla', 'liderazgo'}),
    ('kit-plan-financiero', {'financiero', 'financiera', 'finanzas', 'presupuesto', 'viabilidad', 'tesoreria'}),
    ('kit-tareas-restaurante-creativo', {'creativa', 'creativo', 'vanguardia', 'esferificacion', 'molecular'}),
    ('pro-prompts-ebook', {'prompt', 'prompts', 'chatgpt'}),
]


def carga_ensamblador():
    """Importa el ensamblador para reutilizar catálogo, rotación y banner.

    Se importa en vez de copiarse: el parser del catálogo lleva dentro el gate de
    recuento que evita perder productos en silencio (CLAUDE.md), y duplicarlo
    sería duplicar también ese riesgo."""
    spec = importlib.util.spec_from_file_location('fase8c_assemble', ASSEMBLE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sin_acentos(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower())
                   if unicodedata.category(c) != 'Mn')


def tokens(slug, titulo):
    t = set(slug.split('-'))
    t |= set(re.findall(r'[a-z0-9]+', sin_acentos(titulo)))
    return t


def fijado_tematico(slug, titulo, prods):
    tk = tokens(slug, titulo)
    for pid, claves in TEMATICO:
        if pid in prods and (tk & claves):
            return pid
    return None


def regiones_congeladas(cuerpo):
    """Tramos [inicio, fin) de bloques muertos de WordPress. Sus encabezados son
    falsos: el widget de relacionados trae 7 y el de donaciones 105 en el corpus."""
    reg = []
    for m in BLOCKSY_ABRE.finditer(cuerpo):
        cierre = re.compile(r"<style>\[data-id='%s'\].*?</style></div>"
                            % re.escape(m.group(1)), re.S)
        mc = cierre.search(cuerpo, m.end())
        if mc:
            reg.append((m.start(), mc.end()))
    for patron in (DONACIONES, GRUPO_CB):
        for m in patron.finditer(cuerpo):
            reg.append((m.start(), m.end()))
    return reg


def nivel_contenedor(cuerpo, pos):
    """Cuántos contenedores quedan ABIERTOS en `pos`. Debe ser 0 para insertar:
    una línea en blanco dentro de un <div> rompe el bloque HTML de Markdown."""
    trozo = cuerpo[:pos]
    n = 0
    for tag in CONTENEDORES:
        n += len(re.findall(r'<%s[\s>]' % tag, trozo))
        n -= len(re.findall(r'</%s>' % tag, trozo))
    return n


def candidatos(cuerpo):
    """(offset, útil, es_encabezado) donde se puede insertar sin romper nada.

    `útil` es el offset descontando los bloques congelados que quedan por
    delante. Repartir sobre la longitud BRUTA colocaría mal los banners: esos
    bloques llegan al 21 % del HTML en los glosarios delgados (CLAUDE.md), así
    que el «85 %» bruto de un post puede caer detrás de todo el texto real."""
    reg = sorted(regiones_congeladas(cuerpo))
    fuera = lambda p: not any(a <= p < b for a, b in reg)

    def util(p):
        return p - sum(min(b, p) - a for a, b in reg if a < p)

    out = []
    for m in ENCABEZADO.finditer(cuerpo):
        p = m.start()
        if fuera(p) and nivel_contenedor(cuerpo, p) == 0:
            out.append((p, util(p), True))
    for m in FIN_PARRAFO.finditer(cuerpo):
        p = m.end()
        if fuera(p) and nivel_contenedor(cuerpo, p) == 0:
            out.append((p, util(p), False))
    largo = util(len(cuerpo))
    return sorted(set(out)), largo


def elige_puntos(cands, largo):
    """Tres offsets repartidos por el artículo, prefiriendo encabezados."""
    if not cands or largo <= 0:
        return []
    puntos, usados = [], []
    for frac in ALTURAS:
        objetivo = largo * frac
        libres = [c for c in cands
                  if all(abs(c[1] - u) >= SEPARACION_MIN * largo for u in usados)]
        if not libres:
            continue
        cerca = [c for c in libres
                 if c[2] and abs(c[1] - objetivo) <= VENTANA_ENCABEZADO * largo]
        elegido = min(cerca or libres, key=lambda c: abs(c[1] - objetivo))
        puntos.append(elegido[0])
        usados.append(elegido[1])
    return sorted(set(puntos))


def envuelve(cuerpo, pos, html):
    """Inserta dejando UNA línea en blanco a cada lado, sin añadir de más.

    Markdown necesita el bloque HTML aislado por líneas en blanco, pero el
    cuerpo del molde WordPress ya trae dos saltos entre etiquetas: meter otros
    dos deja cinco líneas vacías y ensucia el diff sin cambiar el render."""
    antes = '' if cuerpo[:pos].endswith('\n\n') else (
        '\n' if cuerpo[:pos].endswith('\n') else '\n\n')
    despues = '' if cuerpo[pos:].startswith('\n\n') else (
        '\n' if cuerpo[pos:].startswith('\n') else '\n\n')
    return antes + html + despues


def procesa(ruta, mod, prods, hoy, lang='es'):
    texto = ruta.read_text(encoding='utf-8')
    mfm = FRONTMATTER.match(texto)
    if not mfm:
        return None, 'sin frontmatter reconocible'
    fm, cuerpo = mfm.group(0), texto[mfm.end():]
    if 'utm_medium=banner' in cuerpo:
        return None, 'ya tiene banners'

    slug = ruta.stem
    mt = re.search(r'^title:\s*"(.*)"\s*$', fm, re.M)
    titulo = mt.group(1) if mt else slug

    cands, largo = candidatos(cuerpo)
    puntos = elige_puntos(cands, largo)
    if len(puntos) < N_BANNERS:
        return None, 'sólo %d punto(s) de inserción seguros' % len(puntos)

    fijado = fijado_tematico(slug, titulo, prods)
    elegidos = mod.rotar_productos(slug, prods, [fijado] if fijado else None,
                                   n=N_BANNERS)
    # El idioma NO es decorativo: banner() saca de él nombre, descripción y copy.
    # Sin pasarlo, --lang en habría metido banners EN ESPAÑOL en el blog inglés.
    trozos = [envuelve(cuerpo, pos, mod.banner(p, prods, slug, lang))
              for pos, p in zip(puntos, elegidos)]

    nuevo = cuerpo
    for pos, trozo in sorted(zip(puntos, trozos), reverse=True):
        nuevo = nuevo[:pos] + trozo + nuevo[pos:]

    # GATE: quitar exactamente lo insertado tiene que devolver el original.
    # Es la prueba de que este script no regenera ni reescribe nada.
    control = nuevo
    for trozo in trozos:
        if trozo not in control:
            return None, 'GATE: el banner insertado no se localiza'
        control = control.replace(trozo, '', 1)
    if control != cuerpo:
        return None, 'GATE: el cuerpo cambió más allá de las inserciones'

    fm_nuevo = re.sub(r'^modDate: .*$', 'modDate: %s' % hoy, fm, count=1, flags=re.M)
    return (fm_nuevo + nuevo, elegidos, fijado), None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', default='es', choices=['es', 'en'])
    ap.add_argument('--aplicar', action='store_true')
    ap.add_argument('--informe', action='store_true')
    ap.add_argument('--limite', type=int)
    args = ap.parse_args()

    mod = carga_ensamblador()
    prods = mod.catalogo_productos()
    hoy = datetime.date.today().isoformat()
    carpeta = BLOG / args.lang

    hechos, saltados, fallos = [], collections.Counter(), []
    reparto, tematicos = collections.Counter(), 0
    for ruta in sorted(carpeta.glob('*.md')):
        res, motivo = procesa(ruta, mod, prods, hoy, args.lang)
        if res is None:
            saltados[motivo] += 1
            if motivo.startswith('GATE') or motivo.startswith('sólo'):
                fallos.append((ruta.name, motivo))
            continue
        texto, elegidos, fijado = res
        if args.aplicar:
            ruta.write_text(texto, encoding='utf-8')
        hechos.append(ruta.name)
        reparto.update(elegidos)
        tematicos += bool(fijado)
        if args.limite and len(hechos) >= args.limite:
            break

    print('%s · %s' % ('APLICADO' if args.aplicar else 'DRY-RUN', carpeta.name))
    print('  posts con banners nuevos: %d  (%d banners)' % (len(hechos), len(hechos) * N_BANNERS))
    print('  con producto fijado por tema: %d' % tematicos)
    for motivo, n in saltados.most_common():
        print('  saltados — %s: %d' % (motivo, n))
    if fallos:
        print('\n  ⚠ revisar a mano:')
        for n, m in fallos[:20]:
            print('    · %-64s %s' % (n, m))
    if args.informe and reparto:
        tot = sum(reparto.values())
        print('\n  reparto: %d productos distintos de %d' % (len(reparto), len(prods)))
        print('  más usado: %s (%.1f %%) · menos usado: %s (%.1f %%)'
              % (reparto.most_common(1)[0][0], 100 * reparto.most_common(1)[0][1] / tot,
                 reparto.most_common()[-1][0], 100 * reparto.most_common()[-1][1] / tot))
        sin = sorted(set(prods) - set(reparto))
        print('  sin ningún banner: %s' % (', '.join(sin) if sin else 'ninguno'))
    if not args.aplicar:
        print('\n  (dry-run: no se ha escrito nada. Añade --aplicar)')


if __name__ == '__main__':
    main()
