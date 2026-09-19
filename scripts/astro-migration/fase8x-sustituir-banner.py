#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8X — Inserción QUIRÚRGICA de UN producto digital en los posts del blog,
GENÉRICA: el producto y su tabla de posts viven en un JSON, no en el código.

    python3 scripts/astro-migration/fase8x-sustituir-banner.py --producto <pid>              # dry-run
    python3 scripts/astro-migration/fase8x-sustituir-banner.py --producto <pid> --aplicar
    python3 scripts/astro-migration/fase8x-sustituir-banner.py --producto <pid> --informe f.txt
Después, SIEMPRE: python3 scripts/astro-migration/fase8b-regen-lastmod.py

POR QUÉ ESTE SCRIPT EXISTE (D46 de la SPEC de Chocolatería)
-----------------------------------------------------------
`fase8f` (Food Cost), `fase8g` (Manager), `fase8h` (Chef) y `fase8i`
(Pastelería) son CUATRO COPIAS del mismo algoritmo con la tabla del research
clavada en el módulo. Éste es el mismo algoritmo —heredado literalmente de
`fase8i`, gate de reversibilidad byte a byte incluido— con la tabla movida a
`fase8x-config/<pid>.json`. `fase8j` queda sin usar a propósito: el quinto
producto ya no clona nada.

Hace, por post, sólo lo que dice su fila del JSON:
  1. (acción `SUSTITUIR`) cambia UN banner declarado por el del producto, con
     el MISMO `banner()` y el MISMO UTM del ensamblador
     `fase8c-libreria-assemble.py` — nunca una copia del HTML;
  1bis. (bloque `miswiring`, opcional e INDEPENDIENTE del producto) cambia un
     banner mal cableado por el que le corresponde, mismo mecanismo;
  2. inserta un párrafo con enlace contextual (sin UTM en el texto);
  3. actualiza el `modDate`.
Y lo demuestra: deshace las ediciones en orden inverso y exige que el texto
vuelva a ser IDÉNTICO al original, byte a byte. Dry-run por defecto.

POR QUÉ SUSTITUIR Y NO AÑADIR
-----------------------------
Los posts del corpus ES ya llevan exactamente 3 banners desde
`fase8e-banners-corpus.py` (política de John del 2026-07-31). `fase8e` SÓLO
INSERTA: correrlo para colocar un producto nuevo devuelve un informe vacío y
hace creer que la rotación está hecha. Y reejecutar
`fase8c-libreria-assemble.py` está PROHIBIDO: reconstruye el cuerpo desde el
`.txt` de bridge y pisa cualquier edición manual posterior. La única vía para
meter un producto nuevo en un post ya publicado es sustituir, y es lo que hace
este script.

EL CONTRATO DEL JSON (`fase8x-config/<pid>.json`)
-------------------------------------------------
{
  "producto": "<pid>",              # obligatorio; debe coincidir con --producto
  "fecha": "AAAA-MM-DD",            # el modDate que se escribe
  "lang": "es",                     # opcional (por defecto "es")
  "ancla": "…",                     # opcional: texto del <a>. Por defecto, el
                                    #   NOMBRE DEL CATÁLOGO en ese idioma, que
                                    #   es lo que garantiza un nombre único en
                                    #   todas las superficies. El escape HTML
                                    #   del "&" lo hace el script.
  "nunca": ["kit-…", "guia-…"],     # prefijos de producto que JAMÁS se
                                    #   sacrifican (el cross-sell del propio
                                    #   producto). El pid se añade solo.
  "prohibidos": ["slug-post", …],   # posts que NO se pueden tocar; el script
                                    #   aborta si alguien los mete en "posts"
  "esperado": {"sustituir": N, "solo_enlace": N, "miswiring": N},
  "posts": {
    "<slug-post>": {
      "accion": "SUSTITUIR" | "SOLO_ENLACE",
      "victima": "<pid-del-banner-que-se-va>",   # sólo si SUSTITUIR
      "miswiring": {"viejo": "<pid>", "nuevo": "<pid>"},   # opcional
      "ancla_n": 1,                 # opcional: cuál de los headings válidos
                                    #   recibe el párrafo (1 = el primero, que
                                    #   es el defecto). Sirve para apartarlo de
                                    #   otro párrafo de enlace ya presente.
      "parrafo": "…{ENLACE}…"       # exactamente UN {ENLACE}
    }, …
  }
}

Reglas que el script IMPONE, no supone:
  · la víctima declarada tiene que estar de verdad en el post (si no está, es
    un error del research o de una pasada anterior: ABORTA, no improvisa otra);
  · la víctima no puede empezar por ningún prefijo de `nunca`;
  · el post tiene que tener exactamente 3 banners antes Y después;
  · los `esperado` tienen que cuadrar con la tabla (un `esperado` que no cuadra
    es una fila que se cayó al editar el JSON);
  · si el post ya enlaza al producto, se SALTA (idempotente: reejecutar no
    duplica nada).
"""
import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BLOG = ROOT / 'astro-site/src/content/blog'
CONFIG_DIR = Path(__file__).resolve().parent / 'fase8x-config'
BASE_URL = 'https://aichef.pro'

RX_ASIDE = re.compile(r'<aside class="not-prose[^"]*">.*?utm_medium=banner.*?</aside>', re.S)
RX_SLUG = re.compile(r'href="/([a-z0-9-]+)\?utm_source=blog')
RX_MD_H2 = re.compile(r'^## ', re.M)
RX_HTML_H2 = re.compile(r'<h2\b')
RX_HTML_H3 = re.compile(r'<h3\b')
RX_FRONTMATTER = re.compile(r'^---\n.*?\n---\n', re.S)
RX_FECHA = re.compile(r'^\d{4}-\d{2}-\d{2}$')

# Contenedores de bloque cuyo balance tiene que estar en CERO en el punto de
# inserción. `div` cubre los bloques congelados del export de WordPress;
# `aside` cubre los PROPIOS BANNERS, y no es teórico: sin él, en un post sin
# `<h2>` (molde WordPress antiguo, headings sólo en `<h3>`) el primer candidato
# es el `<h3>` que el banner lleva DENTRO, y el párrafo se insertaría entre la
# antetítulo y el nombre del producto, partiendo el banner. Lo vio el dry-run
# de `coulant-de-guanaja-70-…`, que eligió el byte 2501 = dentro del primer
# `<aside>`. `fase8i` no lo caza porque sus 8 posts anclaban todos en un `h2`.
CONTENEDORES = ('div', 'aside', 'section')

ACCIONES = ('SUSTITUIR', 'SOLO_ENLACE')


def cargar_ensamblador():
    """Importa `fase8c-libreria-assemble.py` como módulo.

    No se copia su `banner()` ni su catálogo: el HTML del banner, el UTM y el
    parser del `.ts` (con su gate de recuento contra la fuente) tienen que ser
    los mismos que usa el ensamblador, o los banners insertados aquí
    divergirían en silencio de los 326 ya publicados."""
    ruta = ROOT / 'scripts/astro-migration/fase8c-libreria-assemble.py'
    spec = importlib.util.spec_from_file_location('asm', ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def cargar_config(pid, ruta_override=None):
    ruta = Path(ruta_override) if ruta_override else CONFIG_DIR / (pid + '.json')
    if not ruta.exists():
        sys.exit('no existe la config del producto: %s' % ruta)
    cfg = json.loads(ruta.read_text(encoding='utf-8'))
    if cfg.get('producto') != pid:
        sys.exit('la config declara el producto %r y se pidió %r'
                 % (cfg.get('producto'), pid))
    if not RX_FECHA.match(cfg.get('fecha', '')):
        sys.exit('la config necesita "fecha": "AAAA-MM-DD" (el modDate que se escribe)')
    posts = cfg.get('posts') or {}
    if not posts:
        sys.exit('la config no declara ningún post')
    prohibidos = set(cfg.get('prohibidos') or [])
    choque = prohibidos & set(posts)
    if choque:
        sys.exit('posts declarados PROHIBIDOS y a la vez en "posts": %s'
                 % ', '.join(sorted(choque)))
    for slug, fila in posts.items():
        accion = fila.get('accion')
        if accion not in ACCIONES:
            sys.exit('%s: "accion" debe ser %s, no %r'
                     % (slug, ' o '.join(ACCIONES), accion))
        if accion == 'SUSTITUIR' and not fila.get('victima'):
            sys.exit('%s: accion SUSTITUIR sin "victima"' % slug)
        if accion == 'SOLO_ENLACE' and fila.get('victima'):
            sys.exit('%s: accion SOLO_ENLACE no puede traer "victima"' % slug)
        mis = fila.get('miswiring')
        if mis is not None and not (mis.get('viejo') and mis.get('nuevo')):
            sys.exit('%s: "miswiring" necesita "viejo" y "nuevo"' % slug)
        n = fila.get('ancla_n', 1)
        if not isinstance(n, int) or isinstance(n, bool) or n < 1:
            sys.exit('%s: "ancla_n" debe ser un entero >= 1, no %r' % (slug, n))
        parrafo = fila.get('parrafo') or ''
        if parrafo.count('{ENLACE}') != 1:
            sys.exit('%s: el "parrafo" necesita exactamente un {ENLACE} (tiene %d)'
                     % (slug, parrafo.count('{ENLACE}')))
    esperado = cfg.get('esperado') or {}
    real = {
        'sustituir': sum(1 for f in posts.values() if f['accion'] == 'SUSTITUIR'),
        'solo_enlace': sum(1 for f in posts.values() if f['accion'] == 'SOLO_ENLACE'),
        'miswiring': sum(1 for f in posts.values() if f.get('miswiring')),
    }
    for k, v in esperado.items():
        if k not in real:
            sys.exit('"esperado" no conoce la clave %r' % k)
        if real[k] != v:
            sys.exit('"esperado.%s" dice %d y la tabla tiene %d: se cayó una fila '
                     'al editar el JSON' % (k, v, real[k]))
    cfg['_real'] = real
    return cfg, ruta


def fin_frontmatter(texto):
    m = RX_FRONTMATTER.match(texto)
    return m.end() if m else 0


def elegir_ancla(texto, slug, n=1):
    """Punto de inserción del párrafo: el n-ésimo heading (md o, si no hay
    ninguno, HTML h2/h3) que tenga texto de introducción delante y los
    contenedores de bloque balanceados.

    El balance en cero de `CONTENEDORES` es lo que mantiene el párrafo FUERA de
    dos sitios donde no puede caer: los bloques congelados que el export de
    WordPress dejó en el cuerpo («También te puede interesar», donaciones de
    Jetpack, «CHEFBUSINESS GROUP») —una línea en blanco dentro de uno de esos
    `<div>` corta el bloque HTML de Markdown y el resto del post se escaparía
    como texto plano— y el interior de un `<aside>` de banner, cuyo `<h3>` es
    un candidato perfectamente válido para el regex y catastrófico para el
    banner."""
    inicio = fin_frontmatter(texto)
    for rx, modo in ((RX_MD_H2, 'md'), (RX_HTML_H2, 'html'), (RX_HTML_H3, 'html')):
        if not rx.search(texto):
            continue
        validos = []
        for m in rx.finditer(texto):
            pos = m.start()
            if not texto[inicio:pos].strip():
                continue
            seg = texto[:pos]
            if any(seg.count('<' + c) != seg.count('</' + c + '>')
                   for c in CONTENEDORES):
                continue
            validos.append(pos)
        if not validos:
            continue
        # El tier que tiene candidatos es el que manda: si pide el 3.º y sólo
        # hay 2, ABORTA en vez de caer al tier siguiente, que colocaría el
        # párrafo en un sitio completamente distinto sin decirlo.
        if n > len(validos):
            sys.exit('%s: se pidió el ancla nº %d y sólo hay %d heading(s) '
                     'válido(s) de ese nivel' % (slug, n, len(validos)))
        pos = validos[n - 1]
        m2 = re.search(r'\n(#{1,6} .{0,80}|<h[1-6][^>]*>.{0,80})', texto[pos:pos + 200])
        titulo = m2.group(1) if m2 else texto[pos:pos + 60]
        return pos, modo, titulo.strip(), n, len(validos)
    sys.exit('%s: sin ancla válida para el párrafo de enlace' % slug)


def insertar_parrafo(texto, cuerpo, slug, n=1):
    """Devuelve (texto_nuevo, pos, insertado, nota_ancla)."""
    pos, modo, titulo, idx, total = elegir_ancla(texto, slug, n)
    titulo = '%s  [ancla %d de %d]' % (titulo, idx, total)
    parrafo = '<p>' + cuerpo + '</p>'
    if modo == 'md':
        antes = '' if texto[:pos].endswith('\n\n') else '\n'
        insertado = antes + parrafo + '\n\n'
    else:
        insertado = parrafo
    return texto[:pos] + insertado + texto[pos:], pos, insertado, titulo


def procesar(slug, fila, texto, mod, prods, cfg):
    """(salida, detalle_banner, (pos, titulo, parrafo), gate_ok).

    salida None = el post ya enlaza al producto y no se toca."""
    pid, url, lang = cfg['producto'], cfg['_url'], cfg['lang']
    if url in texto:
        return None, None, None, None

    asides = RX_ASIDE.findall(texto)
    if len(asides) != 3:
        sys.exit('%s: esperaba 3 banners, hay %d' % (slug, len(asides)))
    slugs_banner = [RX_SLUG.search(a).group(1) for a in asides]

    trabajo = texto
    viejo_prod = nuevo_prod = None
    viejo_mis = nuevo_mis = None
    detalle_banner = 'ninguno (sólo enlace)'

    if fila['accion'] == 'SUSTITUIR':
        victima = fila['victima']
        if victima not in slugs_banner:
            sys.exit('%s: la víctima declarada (%s) no está en el post (tiene %s)'
                     % (slug, victima, slugs_banner))
        if victima.startswith(cfg['_nunca']):
            sys.exit('%s: la víctima declarada (%s) está en NUNCA' % (slug, victima))
        viejo_prod = asides[slugs_banner.index(victima)]
        nuevo_prod = mod.banner(pid, prods, slug, lang)
        assert trabajo.count(viejo_prod) == 1
        trabajo = trabajo.replace(viejo_prod, nuevo_prod)
        detalle_banner = '%s → %s' % (victima, pid)

    mis = fila.get('miswiring')
    if mis:
        if mis['viejo'] not in slugs_banner:
            sys.exit('%s: el banner mal cableado (%s) no está' % (slug, mis['viejo']))
        viejo_mis = asides[slugs_banner.index(mis['viejo'])]
        nuevo_mis = mod.banner(mis['nuevo'], prods, slug, lang)
        assert trabajo.count(viejo_mis) == 1
        trabajo = trabajo.replace(viejo_mis, nuevo_mis)
        nota = '%s → %s (fix miswiring, ajeno a %s)' % (mis['viejo'], mis['nuevo'], pid)
        detalle_banner = nota if detalle_banner.startswith('ninguno') \
            else detalle_banner + '; ' + nota

    cuerpo = fila['parrafo'].replace('{ENLACE}', cfg['_a'])
    tras_banner = trabajo
    tras_parrafo, pos, insertado, titulo = insertar_parrafo(
        tras_banner, cuerpo, slug, fila.get('ancla_n', 1))

    md_old = re.search(r'^modDate: (\d{4}-\d{2}-\d{2})$', tras_parrafo, re.M)
    assert md_old, '%s: sin modDate' % slug
    salida = tras_parrafo.replace(md_old.group(0), 'modDate: ' + cfg['fecha'], 1)

    # Gate: deshacer las ediciones en orden inverso (modDate, párrafo, banner de
    # miswiring, banner del producto) y exigir que el resultado sea el original
    # byte a byte. Es lo único que demuestra que el script SÓLO ha hecho lo que
    # dice el informe.
    d1 = salida.replace('modDate: ' + cfg['fecha'], md_old.group(0), 1)
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
    if len(RX_ASIDE.findall(salida)) != 3:
        sys.exit('%s: tras aplicar no quedan 3 banners' % slug)

    return salida, detalle_banner, (pos, titulo, cuerpo), True


def main():
    ap = argparse.ArgumentParser(
        description='Sustituye un banner por el de un producto e inserta su '
                    'enlace contextual en los posts que declare su JSON.')
    ap.add_argument('--producto', required=True,
                    help='id del producto (= nombre del JSON en fase8x-config/)')
    ap.add_argument('--config', help='ruta alternativa al JSON de configuración')
    ap.add_argument('--aplicar', action='store_true', help='escribe los .md')
    ap.add_argument('--dry-run', action='store_true',
                    help='no hace nada distinto: dry-run ya es el comportamiento por defecto')
    ap.add_argument('--informe', help='ruta donde volcar el informe además de imprimirlo')
    args = ap.parse_args()

    cfg, ruta_cfg = cargar_config(args.producto, args.config)
    pid = cfg['producto']
    cfg['lang'] = cfg.get('lang', 'es')

    mod = cargar_ensamblador()
    prods = mod.catalogo_productos()
    if pid not in prods:
        sys.exit('%s no está en src/data/products-catalog.ts: sin entrada en el '
                 'catálogo no hay banner posible (lo añade la capa de producto)' % pid)

    # El nombre del enlace sale del CATÁLOGO, no de la config: es lo que
    # garantiza que el blog llame al producto igual que la landing, el hub y el
    # correo. `esc()` convierte el "&" literal del nombre en "&amp;".
    nombre_catalogo = prods[pid][cfg['lang']][0]
    ancla = cfg.get('ancla') or nombre_catalogo
    cfg['_url'] = BASE_URL + prods[pid]['url']
    cfg['_a'] = '<a href="%s">%s</a>' % (cfg['_url'], mod.esc(ancla))
    # Los prefijos que nunca se sacrifican. El propio producto entra siempre:
    # si una reejecución lo encontrase ya puesto, no se pisaría a sí mismo.
    cfg['_nunca'] = tuple(sorted(set(cfg.get('nunca') or []) | {pid}))

    blog_lang = BLOG / cfg['lang']
    if not blog_lang.is_dir():
        sys.exit('no existe el corpus del idioma %r en %s' % (cfg['lang'], BLOG))

    lineas = []

    def out(s=''):
        print(s)
        lineas.append(s)

    out('Fase 8X — producto %s · %d posts · %s'
        % (pid, len(cfg['posts']), 'APLICANDO' if args.aplicar else 'dry-run'))
    out('  config: %s' % ruta_cfg)
    out('  enlace: %s' % cfg['_a'])
    if ancla != nombre_catalogo:
        out('  ⚠️  el ancla del JSON NO es el nombre del catálogo (%r)' % nombre_catalogo)
    out('  NUNCA (prefijos): %s' % ', '.join(cfg['_nunca']))
    if cfg.get('prohibidos'):
        out('  PROHIBIDOS (no se tocan): %s' % ', '.join(cfg['prohibidos']))
    out('')

    saltados, tocados = [], []
    for slug, fila in cfg['posts'].items():
        ruta = blog_lang / (slug + '.md')
        if not ruta.exists():
            sys.exit('%s: el .md no existe en %s' % (slug, blog_lang))
        texto = ruta.read_text(encoding='utf-8')
        salida, detalle_banner, info_enlace, gate_ok = procesar(
            slug, fila, texto, mod, prods, cfg)

        out('=== %s ===' % slug)
        if salida is None:
            out('  SKIP — ya enlaza a %s (idempotente)' % cfg['_url'])
            saltados.append(slug)
            out('')
            continue

        pos, titulo, parrafo = info_enlace
        out('  Acción: %s' % fila['accion'])
        out('  Banner sustituido: %s' % detalle_banner)
        out('  Posición del enlace: byte %d, antes de: %s' % (pos, titulo))
        out('  Enlace contextual: "%s"' % parrafo)
        out('  Gate de reversibilidad: %s' % ('OK' if gate_ok else 'FALLO'))
        out('  Banners tras aplicar: 3')
        out('  Delta de tamaño: +%d bytes' % (len(salida) - len(texto)))
        if args.aplicar:
            ruta.write_text(salida, encoding='utf-8')
            out('  ESCRITO')
        tocados.append(slug)
        out('')

    r = cfg['_real']
    out('Resumen: %d/%d posts tocados (%d con banner de %s, %d sólo-enlace, '
        '%d con fix de miswiring), %d saltados por idempotencia.'
        % (len(tocados), len(cfg['posts']), r['sustituir'], pid,
           r['solo_enlace'], r['miswiring'], len(saltados)))
    if not args.aplicar:
        out('(dry-run: nada escrito; --aplicar para aplicar)')
    else:
        out('Siguiente paso OBLIGATORIO: '
            'python3 scripts/astro-migration/fase8b-regen-lastmod.py')

    if args.informe:
        Path(args.informe).write_text('\n'.join(lineas) + '\n', encoding='utf-8')
        print('\nInforme volcado en %s' % args.informe)


if __name__ == '__main__':
    main()
