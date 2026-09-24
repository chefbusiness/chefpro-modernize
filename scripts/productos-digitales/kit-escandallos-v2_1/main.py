#!/usr/bin/env python3
"""
main.py — Construcción del Kit de Escandallos Pro v2.1 (F2-ES).

    python3 main.py [--json informe.json]      # DRY-RUN (por defecto)
    KIT_ESCANDALLOS_APPLY=1 python3 main.py --real

Dry-run: copia los 12 xlsx publicados de `astro-site/public/dl/kit-escandallos/` a
`<scratchpad>/v2_1-dryrun/` y trabaja allí. `dl/` NO se toca.
`--real` escribe IN PLACE en `dl/kit-escandallos/` (respaldo previo en el scratchpad) y
exige además `KIT_ESCANDALLOS_APPLY=1`: lo lanza el orquestador tras la revisión.

Orden (SPEC §2.0):
  1. copia de trabajo (dry-run) o respaldo (real);
  2. `nuevas.py`: genera 12-test-de-rendimiento.xlsx y 13-lista-precios-ingredientes.xlsx;
  3. pycel evalúa la «MERMA % PARA TU ESCANDALLO» del 12 (no se escribe a mano) y se
     contrasta con la misma cuenta en Python;
  4. `parche_v2_1.py` sobre los 12 libros publicados, con esa merma para 01!H5;
  5. idempotencia: 2.ª pasada completa (2 + 4) sobre un clon → 0 diferencias;
  6. `inject_cache.py` AL FINAL sobre los 14 (cualquier save() posterior borraría la caché).

Térmica: todo en SERIE, sin builds ni navegador. La verificación va aparte
(`verificar.py`), también en serie.
"""
import argparse
import datetime
import json
import logging
import os
import shutil
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(SCRIPTS, 'kit-escandallos-v2_0'))
sys.path.insert(0, AQUI)

import openpyxl                                                # noqa: E402

import motor                                                   # noqa: E402
import nuevas                                                  # noqa: E402
import parche_v2_1                                             # noqa: E402

logging.disable(logging.CRITICAL)

ROOT = os.path.dirname(os.path.dirname(SCRIPTS))
ORIGEN = os.path.join(ROOT, 'astro-site', 'public', 'dl', 'kit-escandallos')
# R1 T8: nada de rutas de una sesión concreta en el código (repo PÚBLICO, y el
# `--real` puede lanzarse en el VPS). Carpeta de trabajo: `--scratch`, o la
# variable CLAUDE_SCRATCHPAD; si no hay ninguna, el dry-run va a `.work/` del repo
# (en .gitignore) y `--real` ABORTA (el respaldo previo tiene que ir a un sitio
# que el orquestador conozca).
SCRATCH_REPO = os.path.join(ROOT, '.work', 'kit-escandallos-v2_1')
INJECT = os.path.join(SCRIPTS, 'inject_cache.py')


def scratch_dir(arg=None, real=False):
    s = arg or os.environ.get('CLAUDE_SCRATCHPAD')
    if not s:
        if real:
            raise SystemExit('ABORTADO: --real necesita --scratch <carpeta> o la variable '
                             'CLAUDE_SCRATCHPAD para dejar el respaldo de dl/.')
        s = SCRATCH_REPO
    return os.path.abspath(s)


def dryrun_dir(arg=None):
    return os.path.join(scratch_dir(arg), 'v2_1-dryrun')


SCRATCH = scratch_dir()
DRYRUN = dryrun_dir()

PUBLICADOS = motor.FICHEROS + parche_v2_1.OTROS          # los 12 xlsx de v2.0
NUEVOS = [nuevas.F12, nuevas.F13]
LIBROS = PUBLICADOS + NUEVOS                             # los 14 de v2.1


def log(msg):
    print(msg, flush=True)


def digest(path):
    """Huella comparable de un .xlsx (la de v2.0 main.py, sin fecha de guardado)."""
    wb = openpyxl.load_workbook(path)
    fuera = {'_props': (wb.properties.subject, wb.properties.title)}
    for ws in wb.worksheets:
        celdas = {}
        for row in ws.iter_rows():
            for c in row:
                if c.value is None:
                    continue
                relleno = None
                if c.fill is not None and c.fill.fill_type == 'solid':
                    relleno = str(c.fill.fgColor.rgb)
                celdas[c.coordinate] = (repr(c.value), c.number_format, relleno,
                                        bool(c.protection.locked))
        fuera[ws.title] = {
            'celdas': celdas,
            'merges': sorted(str(m) for m in ws.merged_cells.ranges),
            'dv': sorted(f'{dv.type}:{dv.formula1}:{dv.sqref}'
                         for dv in ws.data_validations.dataValidation),
            'cf': sorted(str(r.sqref) for r in ws.conditional_formatting),
            'prot': bool(ws.protection.sheet), 'area': str(ws.print_area),
        }
    return fuera


def diff_digest(a, b, fichero):
    fuera = []
    if a['_props'] != b['_props']:
        fuera.append(f'{fichero}: cambian las propiedades')
    for hoja in sorted(set(a) - {'_props'} | set(b) - {'_props'}):
        if hoja not in a or hoja not in b:
            fuera.append(f'{fichero}:{hoja}: hoja sólo en una pasada')
            continue
        ha, hb = a[hoja], b[hoja]
        for k in ('merges', 'dv', 'cf', 'prot', 'area'):
            if ha[k] != hb[k]:
                fuera.append(f'{fichero}:{hoja}: cambia {k}')
        for coord in sorted(set(ha['celdas']) | set(hb['celdas'])):
            if ha['celdas'].get(coord) != hb['celdas'].get(coord):
                fuera.append(f'{fichero}:{hoja}!{coord}: {ha["celdas"].get(coord)} → '
                             f'{hb["celdas"].get(coord)}')
    return fuera


def construir(carpeta, datos, informe, fichas):
    """Pasos 2-4 sobre `carpeta`. `fichas` = carpeta de la que se leen los ingredientes
    y precios de 01-08 para el 13: SIEMPRE una copia publicada con caché (en `--real`, el
    respaldo previo; si no, la 2.ª pasada leería fichas recién guardadas por openpyxl, sin
    caché, y los precios enlazados del 04 saldrían vacíos). Devuelve la merma usada."""
    p12 = nuevas.generar_12(carpeta, datos)
    _, info13 = nuevas.generar_13(carpeta, fichas, datos)
    merma, coste_porcion = nuevas.merma_calculada(p12)
    esperada = nuevas.merma_python(datos['despiece'])
    if abs(merma - esperada) > 1e-9:
        raise SystemExit(f'pycel da {merma} y Python {esperada}: el 12 no calcula '
                         'lo que dice la SPEC')
    parche = parche_v2_1.aplicar(carpeta, merma, datos=datos)
    informe.update({'merma_12': merma, 'coste_porcion_12': coste_porcion,
                    'lista_13': {k: v for k, v in info13.items()
                                 if k not in ('mapa', 'lista')},
                    'parche': parche})
    return merma, info13


def inject_cache(carpeta):
    fuera = []
    for n in LIBROS:
        r = subprocess.run([sys.executable, '-W', 'ignore', INJECT,
                            os.path.join(carpeta, n)], capture_output=True, text=True)
        linea = r.stdout.strip()
        log('    ' + linea)
        fuera.append({'fichero': n, 'salida': linea, 'exit': r.returncode})
        if r.returncode != 0:
            log('    ERROR inject_cache: ' + r.stderr[-400:])
    return fuera


def main():
    ap = argparse.ArgumentParser(description='Kit de Escandallos Pro v2.1')
    ap.add_argument('--real', action='store_true',
                    help='escribe en astro-site/public/dl/kit-escandallos/ (con '
                         'KIT_ESCANDALLOS_APPLY=1)')
    ap.add_argument('--json', default=None)
    ap.add_argument('--scratch', default=None,
                    help='carpeta de trabajo (por defecto CLAUDE_SCRATCHPAD; sin ella, '
                         '.work/ del repo en dry-run; obligatoria con --real)')
    ap.add_argument('--sin-idempotencia', action='store_true')
    args = ap.parse_args()

    if args.real and os.environ.get('KIT_ESCANDALLOS_APPLY') != '1':
        raise SystemExit('ABORTADO: --real escribe en dl/kit-escandallos/. Hace falta '
                         'también KIT_ESCANDALLOS_APPLY=1 (orquestador, tras la revisión).')
    scratch = scratch_dir(args.scratch, real=args.real)
    os.makedirs(scratch, exist_ok=True)
    dryrun = os.path.join(scratch, 'v2_1-dryrun')
    idem_dir = os.path.join(scratch, 'v2_1-idem')

    datos = nuevas.cargar_datos()
    informe = {'producto': 'kit-escandallos', 'version': '2.1',
               'fecha': datetime.datetime.now().isoformat(timespec='seconds'),
               'modo': 'real' if args.real else 'dry-run', 'origen': ORIGEN}
    respaldo = None
    if args.real:
        carpeta = ORIGEN
        respaldo = os.path.join(scratch, 'kit-escandallos.bak-'
                                + datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
        shutil.copytree(ORIGEN, respaldo)
        log(f'  respaldo de dl/kit-escandallos: {respaldo}')
    else:
        carpeta = dryrun
        if os.path.isdir(carpeta):
            shutil.rmtree(carpeta)
        os.makedirs(carpeta)
        for n in PUBLICADOS:
            shutil.copy2(os.path.join(ORIGEN, n), os.path.join(carpeta, n))
        log(f'  copia de los {len(PUBLICADOS)} publicados → {carpeta}')
    informe['carpeta'] = carpeta

    log('\n== 1/3 · nuevas (12, 13) + merma calculada + parche de los 12 ==')
    fichas = respaldo or ORIGEN
    informe['fichas_leidas_de'] = fichas
    merma, info13 = construir(carpeta, datos, informe, fichas)
    log(f"  merma del solomillo (pycel): {merma:.6f} · coste por porción 12: "
        f"{informe['coste_porcion_12']:.4f} €")
    log(f"  13: {info13['filas']} ingredientes + {info13['vacias']} filas vacías; "
        f"{len(info13['conflictos'])} ingredientes con dos precios en el kit")
    for r in informe['parche']:
        if 'formulas_reescritas' in r:
            log(f"  {r['fichero']}: {r['formulas_reescritas']}/{r['formulas_conversiones']}"
                f" fórmulas → {r['rango']} · 13: {r['linea_13']}"
                + (f" · 12: {r['linea_12']} · H5 {r['H5']}" if 'H5' in r else ''))
        else:
            log(f"  {r['fichero']}: ZIP ({r['partes']} partes), versión «{r['version_antes'][:14]}…» → 2.1")

    idem = {'ejecutada': False}
    if not args.sin_idempotencia:
        log('\n== 2/3 · idempotencia: 2.ª pasada sobre un clon ==')
        if os.path.isdir(idem_dir):
            shutil.rmtree(idem_dir)
        shutil.copytree(carpeta, idem_dir)
        antes = {n: digest(os.path.join(carpeta, n)) for n in LIBROS}
        construir(idem_dir, datos, {}, fichas)
        difs = []
        for n in LIBROS:
            difs += diff_digest(antes[n], digest(os.path.join(idem_dir, n)), n)
        idem = {'ejecutada': True, 'diferencias': len(difs), 'detalle': difs[:40]}
        log(f'  diferencias 1.ª vs 2.ª pasada: {len(difs)}')
        for d in difs[:10]:
            log('    ' + d)
        shutil.rmtree(idem_dir)

    log('\n== 3/3 · inject_cache (AL FINAL, sobre los 14) ==')
    cache = inject_cache(carpeta)

    fallos = []
    if idem.get('diferencias'):
        fallos.append(f"idempotencia: {idem['diferencias']} diferencias")
    fallos += [f"inject_cache {c['fichero']}: exit {c['exit']}" for c in cache if c['exit']]
    fallos += [f"inject_cache {c['fichero']}: {c['salida']}" for c in cache
               if 'fallos_pycel=0' not in c['salida']]
    informe.update({'idempotencia': idem, 'inject_cache': cache, 'fallos': fallos,
                    'respaldo': respaldo})
    if args.json:
        with open(args.json, 'w', encoding='utf-8') as fh:
            json.dump(informe, fh, ensure_ascii=False, indent=1, default=str)
        log(f'\ninforme → {args.json}')
    log('\n' + ('FALLOS:\n  ' + '\n  '.join(fallos) if fallos else
                'CONSTRUCCIÓN OK (siguiente: verificar.py)'))
    return 1 if fallos else 0


if __name__ == '__main__':
    sys.exit(main())
