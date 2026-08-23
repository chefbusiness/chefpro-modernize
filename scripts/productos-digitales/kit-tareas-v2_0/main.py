#!/usr/bin/env python3
"""
main.py — Orquestador del post-proceso v2.0 de la familia «Kit de Tareas».

    python3 main.py --producto <pid> [--dry-run] [--solo motor,contenido]
                    [--json informe.json]

`--producto` por defecto `kit-tareas` (el representante). El motor (§1 y §2 de
`kit-tareas-v2-SPEC.md`) es de FAMILIA: se puede pasar a cualquier hermano
(`kit-tareas-cafeteria`, `kit-tareas-hotel`…) y sólo tocará las hojas que
reconozca por CABECERA. El módulo de CONTENIDO es propio de cada producto y se
carga si existe `contenido_<pid con guiones bajos>.py`.

REGLA DURA: `astro-site/public/dl/<pid>/` NO se toca. `--dry-run` copia el
producto al scratchpad y trabaja allí. Sin `--dry-run` el script ABORTA salvo
que se le pase `KIT_TAREAS_APPLY=1`: la ejecución real la hace el orquestador
cuando la ronda 2 dé verde.

Orden de trabajo:
  1. Copia de trabajo (dry-run) o respaldo con marca de tiempo EN EL SCRATCHPAD
     (nunca una carpeta .bak dentro de public/dl/, que se publicaría).
  2. `motor.contexto()` lee el kit entero: nombre comercial, pie, sufijo de
     metadata, hora ancla de apertura y qué fichero hace de negocio / caja /
     áreas. De ahí sale el «Se conecta con» sin nombres a mano.
  3. Por fichero: motor.aplicar → contenido.post (si hay) → motor.cerrar.
  4. Idempotencia: se repite el pipeline sobre un clon y se compara celda a
     celda. 0 diferencias o falla.
  5. `inject_cache.py` SIEMPRE al final (cualquier guardado posterior de
     openpyxl borraría el cache).
  6. Verificación: data_only de cada fórmula nueva · pycel con los casos de §6
     (arqueo, contador honesto, denominador del 07) · DV «✓,—,N/A» en todas las
     hojas de checklist · bio en todas las Instrucciones · censo --fail.

Térmica: todo en SERIE, sin builds ni navegador.
"""
import argparse
import contextlib
import copy
import datetime
import importlib
import json
import logging
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import openpyxl                                            # noqa: E402

import motor                                               # noqa: E402

logging.disable(logging.CRITICAL)

AQUI = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(AQUI)
ROOT = os.path.dirname(os.path.dirname(SCRIPTS))
DL = os.path.join(ROOT, 'astro-site', 'public', 'dl')
SCRATCH = os.environ.get(
    'CLAUDE_SCRATCHPAD',
    '/private/tmp/claude-501/-Users-johnguerrero-chefpro-modernize/'
    'f83a04d3-d14f-49b3-aa79-c442fb4d7983/scratchpad')
INJECT = os.path.join(SCRIPTS, 'inject_cache.py')
CENSO = os.path.join(SCRIPTS, 'censo-entregables.py')
SPEC = 'scripts/productos-digitales/kit-tareas-v2-SPEC.md §1 y §2'


def log(msg):
    print(msg, flush=True)


# ==========================================================================
# Copias
# ==========================================================================
def preparar_copia(origen, destino):
    if not os.path.isdir(origen):
        raise SystemExit(f'No existe el origen: {origen}')
    if os.path.isdir(destino):
        shutil.rmtree(destino)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    shutil.copytree(origen, destino)
    log(f'  copia de trabajo regenerada: {destino}')


def digest(path):
    """Huella comparable (valores, formato, relleno, bloqueo, merges, DV, CF)."""
    wb = openpyxl.load_workbook(path)
    fuera = {}
    for ws in wb.worksheets:
        celdas = {}
        for row in ws.iter_rows():
            for c in row:
                if c.value is None:
                    continue
                relleno = None
                if c.fill is not None and c.fill.fill_type == 'solid':
                    relleno = str(c.fill.fgColor.rgb)
                celdas[c.coordinate] = (repr(c.value), c.number_format,
                                        relleno, bool(c.protection.locked))
        fuera[ws.title] = {
            'celdas': celdas,
            'merges': sorted(str(m) for m in ws.merged_cells.ranges),
            'dv': sorted(f'{dv.type}:{dv.formula1}:{dv.sqref}'
                         for dv in ws.data_validations.dataValidation),
            'cf': sorted(str(r.sqref) for r in ws.conditional_formatting),
            'area': str(ws.print_area),
            'prot': bool(ws.protection.sheet),
            'alturas': {k: v.height for k, v in ws.row_dimensions.items()
                        if v.height},
        }
    return fuera


def diff_digest(a, b, fichero):
    fuera = []
    for hoja in sorted(set(a) | set(b)):
        if hoja not in a or hoja not in b:
            fuera.append(f'{fichero}:{hoja}: hoja sólo en una pasada')
            continue
        ha, hb = a[hoja], b[hoja]
        for k in ('merges', 'dv', 'cf', 'area', 'prot', 'alturas'):
            if ha[k] != hb[k]:
                fuera.append(f'{fichero}:{hoja}: cambia {k} '
                             f'({ha[k]} → {hb[k]})'[:300])
        ca, cb = ha['celdas'], hb['celdas']
        for coord in sorted(set(ca) | set(cb)):
            if ca.get(coord) != cb.get(coord):
                fuera.append(f'{fichero}:{hoja}!{coord}: '
                             f'{ca.get(coord)} → {cb.get(coord)}')
    return fuera


# ==========================================================================
# Pipeline
# ==========================================================================
def ficheros_de(carpeta):
    return sorted(f for f in os.listdir(carpeta) if f.endswith('.xlsx'))


def procesar(carpeta, fname, etapas, contenido, informe):
    path = os.path.join(carpeta, fname)
    wb = openpyxl.load_workbook(path)
    cambios = []
    estado = None
    # El registro de fórmulas se vacía AQUÍ y no dentro de `motor.aplicar`:
    # aplicar() sale antes de tocarlo cuando el fichero está fuera de alcance
    # (los 01-17 del hotel), y entonces este fichero heredaba el registro del
    # anterior — 98 «fórmulas sin cache» que en realidad estaban en otro libro.
    motor.REGISTRO.clear()
    if 'motor' in etapas:
        estado = motor.aplicar(wb, fname, cambios)
    if 'contenido' in etapas and contenido is not None and \
            hasattr(contenido, 'post'):
        # El módulo de contenido devuelve True cuando ha cambiado la
        # ESTRUCTURA del libro (filas u hojas nuevas). En ese caso hay que
        # volver a pasar el motor ANTES de cerrar: `estado` se midió sobre la
        # geometría vieja y con ella (a) el cuerpo que `proteger` desbloquea se
        # quedaría corto —las últimas filas de la tabla saldrían bloqueadas—,
        # (b) el rango del CF no cubriría las filas nuevas y (c) una hoja
        # creada por el contenido no estaría en `recon`, así que se publicaría
        # sin DV, sin contador, sin A4 y sin protección. El motor es
        # idempotente, así que repasarlo no cuesta más que tiempo.
        if contenido.post(wb, fname, cambios) and 'motor' in etapas and estado:
            motor.REGISTRO.clear()
            extra = []
            estado = motor.aplicar(wb, fname, extra)
            cambios += [c for c in extra if c not in cambios]
    if 'motor' in etapas and estado:
        motor.cerrar(wb, fname, estado, cambios)
    registro = list(motor.REGISTRO)
    guardado = bool(estado or cambios)
    if guardado:
        # Guardar con openpyxl BORRA el valor cacheado de TODAS las fórmulas del
        # libro, también de las que el motor no ha tocado (y de las hojas fuera
        # de alcance, como los inventarios del 05 de cafetería). Por eso
        # `inject_cache` se corre sobre todo fichero GUARDADO, no sólo sobre los
        # que estrenan fórmula: si no, el censo saca `nocache_real` en ficheros
        # que el motor apenas rozó.
        wb.save(path)
    informe.append({'fichero': fname,
                    'guardado': guardado,
                    'en_alcance': bool(estado),
                    'hojas_tocadas': sorted((estado or {}).get('hojas', {})),
                    'cambios': cambios,
                    'formulas_nuevas': len(registro)})
    return registro


# ==========================================================================
# Gates
# ==========================================================================
def inject_cache(carpeta, nombres):
    fuera = []
    for n in nombres:
        r = subprocess.run([sys.executable, INJECT, os.path.join(carpeta, n)],
                           capture_output=True, text=True)
        fuera.append({'fichero': n, 'salida': r.stdout.strip(),
                      'exit': r.returncode})
        log('    ' + (r.stdout.strip() or r.stderr.strip()[-200:]))
    return fuera


def verificar_cache(carpeta, registros):
    fallos, vacias, ok = [], 0, 0
    for fname, registro in registros.items():
        if not registro:
            continue
        wbv = openpyxl.load_workbook(os.path.join(carpeta, fname),
                                     data_only=True)
        for hoja, coord, formula in registro:
            if hoja not in wbv.sheetnames:
                fallos.append(f'{fname}:{hoja}!{coord}: hoja ausente')
                continue
            v = wbv[hoja][coord].value
            if v is None:
                if '""' in formula:
                    vacias += 1
                else:
                    fallos.append(f'{fname}:{hoja}!{coord}: sin cache '
                                  f'({formula[:70]})')
            else:
                ok += 1
    return {'con_valor': ok, 'vacias_por_diseno': vacias, 'fallos': fallos}


def _ev(xl, ref):
    with open(os.devnull, 'w') as dn, contextlib.redirect_stderr(dn):
        try:
            return xl.evaluate(ref)
        except Exception as e:                                   # noqa: BLE001
            return f'ERR:{type(e).__name__}: {e}'


def _copia(carpeta, fname, demos, etiqueta):
    os.makedirs(demos, exist_ok=True)
    dst = os.path.join(demos, f'{etiqueta}-{fname}')
    shutil.copy2(os.path.join(carpeta, fname), dst)
    return dst


def demo_arqueo(carpeta, demos):
    """§6 — fondo 150, efectivo contado 1.150, tarjetas 800, Z 1.800 → 0."""
    from pycel import ExcelCompiler
    fname = motor.CTX.get('f_caja')
    if not fname:
        return []
    casos = []
    for etiqueta, z, esperado in (('arqueo-cuadra', 1800, 0),
                                  ('arqueo-descuadra', 1790, 10)):
        dst = _copia(carpeta, fname, demos, etiqueta)
        wb = openpyxl.load_workbook(dst)
        ap, ci = wb['Apertura de Caja'], wb['Cierre de Caja']
        r_fondo = motor._buscar(ap, motor.ETIQ_FONDO, col=2)
        ap.cell(row=r_fondo, column=3).value = 150
        for etq, cant in (('500 €', 2), ('100 €', 1), ('50 €', 1)):
            r = motor._buscar(ci, etq, col=1)
            ci.cell(row=r, column=2).value = cant
        r_tar = motor._buscar(ci, 'Total Tarjetas (Visa/MC)', col=1)
        r_z = motor._buscar(ci, motor.ETIQ_Z, col=1)
        r_desc = motor._buscar(ci, 'DESCUADRE', col=1)
        r_tot = motor._buscar(ci, 'TOTAL FACTURADO', col=1)
        r_ef = motor._buscar(ci, motor.ETIQ_EFECTIVO, col=1)
        ci.cell(row=r_tar, column=3).value = 800
        ci.cell(row=r_z, column=3).value = z
        wb.save(dst)
        xl = ExcelCompiler(filename=dst)
        obtenido = _ev(xl, f"'Cierre de Caja'!C{r_desc}")
        casos.append({
            'caso': etiqueta,
            'ref': f"{fname}:Cierre de Caja:C{r_desc}",
            'entradas': {f'Apertura de Caja!C{r_fondo}': 150,
                         'Cierre de Caja!B(500/100/50 €)': '2/1/1 = 1.150 €',
                         f'Cierre de Caja!C{r_tar}': 800,
                         f'Cierre de Caja!C{r_z}': z},
            'efectivo_contado': _ev(xl, f"'Cierre de Caja'!C{r_ef}"),
            'total_facturado': _ev(xl, f"'Cierre de Caja'!C{r_tot}"),
            'esperado': esperado, 'obtenido': obtenido,
            'ok': obtenido == esperado, 'copia': dst})
    return casos


def demo_contador(carpeta, demos):
    """§6 — 25 tareas, 3 N/A, 22 ✓ → «22 de 22»."""
    from pycel import ExcelCompiler
    mejor = None
    for fname in motor.CTX.get('con_checklist', ()):
        wb = openpyxl.load_workbook(os.path.join(carpeta, fname))
        for ws in wb.worksheets:
            g = motor.geometria(ws)
            if not g or not g['contador']:
                continue
            tareas = [r for r in range(g['hr'] + 1, g['contador'])
                      if isinstance(ws.cell(row=r, column=2).value, str)
                      and ws.cell(row=r, column=2).value.strip()
                      and not motor.es_fila_seccion(ws, r)]
            if len(tareas) == 25:
                mejor = (fname, ws.title, g, tareas)
                break
            if not mejor or len(tareas) > len(mejor[3]):
                mejor = (fname, ws.title, g, tareas)
        if mejor and len(mejor[3]) == 25:
            break
    if not mejor:
        return []
    fname, hoja, g, tareas = mejor
    dst = _copia(carpeta, fname, demos, 'contador')
    wb = openpyxl.load_workbook(dst)
    ws = wb[hoja]
    for i, r in enumerate(tareas):
        ws.cell(row=r, column=g['marca']).value = 'N/A' if i < 3 else '✓'
    wb.save(dst)
    xl = ExcelCompiler(filename=dst)
    col_num = motor.get_column_letter(g['marca'] - 2)
    col_den = motor.get_column_letter(g['marca'])
    num = _ev(xl, f"'{hoja}'!{col_num}{g['contador']}")
    den = _ev(xl, f"'{hoja}'!{col_den}{g['contador']}")
    esperado = (len(tareas) - 3, len(tareas) - 3)
    return [{'caso': 'contador-honesto',
             'ref': f'{fname}:{hoja}:{col_num}{g["contador"]}/'
                    f'{col_den}{g["contador"]}',
             'entradas': f'{len(tareas)} tareas · 3 N/A · {len(tareas) - 3} ✓',
             'esperado': f'{esperado[0]} de {esperado[1]}',
             'obtenido': f'{num} de {den}',
             'ok': (num, den) == esperado, 'copia': dst}]


def demo_07(carpeta, demos):
    """§6 — 8 tareas escritas en la plantilla en blanco → «de 8»."""
    from pycel import ExcelCompiler
    for fname in sorted(motor.CTX.get('con_checklist', ())):
        wb = openpyxl.load_workbook(os.path.join(carpeta, fname))
        hojas = [ws.title for ws in wb.worksheets
                 if ws.title in motor.PLANTILLA_07]
        if len(hojas) < 3:
            continue
        dst = _copia(carpeta, fname, demos, 'plantilla-8-tareas')
        wb = openpyxl.load_workbook(dst)
        ws = wb[hojas[0]]
        g = motor.geometria(ws)
        libres = [r for r in range(g['hr'] + 1, g['contador'])
                  if not motor.es_fila_seccion(ws, r)]
        for r in libres:
            ws.cell(row=r, column=2).value = None
        for i, r in enumerate(libres[:8]):
            ws.cell(row=r, column=2).value = f'Tarea propia {i + 1}'
        wb.save(dst)
        xl = ExcelCompiler(filename=dst)
        col_den = motor.get_column_letter(g['marca'])
        den = _ev(xl, f"'{hojas[0]}'!{col_den}{g['contador']}")
        return [{'caso': 'denominador-07',
                 'ref': f'{fname}:{hojas[0]}:{col_den}{g["contador"]}',
                 'entradas': '8 tareas escritas, ninguna marcada',
                 'esperado': 8, 'obtenido': den, 'ok': den == 8,
                 'copia': dst}]
    return []


def gate_recuento(carpeta, nombres):
    """TEC-R2-01/COM-R2-01 — cuántas tareas entrega el kit, DE VERDAD.

    La landing publicaba «121 tareas en el kit completo (recuento v2.0)» y el
    recuento no se había hecho: 121 era el fichero 01 de la v1.1. La cifra sale
    de los mismos denominadores que enseña el Excel, así que la página de venta
    y el producto no pueden volver a divergir sin que este gate lo cante.
    """
    por_fichero, total = {}, 0
    for n in nombres:
        wbv = openpyxl.load_workbook(os.path.join(carpeta, n), data_only=True)
        wb = openpyxl.load_workbook(os.path.join(carpeta, n))
        n_tareas = 0
        for ws in wb.worksheets:
            g = motor.geometria(ws)
            if not g or not g['contador']:
                continue
            v = wbv[ws.title].cell(row=g['contador'], column=g['marca']).value
            n_tareas += int(v or 0)
        por_fichero[n] = n_tareas
        total += n_tareas
    return {'total': total, 'por_fichero': por_fichero}


def gate_dv_y_bio(carpeta, nombres):
    """DV «✓,—,N/A» en TODA hoja de checklist y bio en TODA Instrucciones.

    TEC-R2-08: también se censan las hojas FUERA de alcance. Aplicar sólo el
    motor a los 08/09 de un hermano (el kit de hotel) deja el producto con dos
    listas de desplegable conviviendo —4 hojas con «✓,—,N/A» y 48 con «✓,✗,—»—
    y el gate lo daba por verde porque sólo miraba lo que había tocado.
    """
    dv_mal, sin_bio, hojas, con_bio = [], [], 0, 0
    listas_kit, hojas_p4 = {}, 0
    for n in nombres:
        wb = openpyxl.load_workbook(os.path.join(carpeta, n))
        for ws in wb.worksheets:
            for dv in ws.data_validations.dataValidation:
                if dv.type == 'list':
                    listas_kit.setdefault(dv.formula1, []).append(
                        f'{n}:{ws.title}')
        # R3-e — las hojas del molde P4 también se auditan: son las que dejaban
        # el producto con dos desplegables y dos semánticas de conteo.
        for ws in wb.worksheets:
            if not motor.geometria_p4(ws):
                continue
            hojas_p4 += 1
            listas = {dv.formula1 for dv in ws.data_validations.dataValidation
                      if dv.type == 'list'}
            if listas and listas != {motor.DV_LISTA}:
                dv_mal.append(f'{n}:{ws.title} (molde P4): DV = '
                              f'{sorted(listas)} (esperada {motor.DV_LISTA})')
        if not motor.en_alcance(wb):
            continue
        for ws in wb.worksheets:
            if not motor.geometria(ws):
                continue
            hojas += 1
            listas = {dv.formula1 for dv in ws.data_validations.dataValidation
                      if dv.type == 'list'}
            if listas != {motor.DV_LISTA}:
                dv_mal.append(f'{n}:{ws.title}: DV = {sorted(listas)} '
                              f'(esperada {motor.DV_LISTA})')
        ws = wb['Instrucciones'] if 'Instrucciones' in wb.sheetnames else None
        texto = ' '.join(str(c.value) for row in (ws.iter_rows() if ws else [])
                         for c in row if c.value)
        if ws is None or not motor.RX_BIO.search(texto):
            sin_bio.append(n)
        else:
            con_bio += 1
    mezcla = []
    if len(listas_kit) > 1:
        mezcla = [f'{f} en {len(h)} hojas (p.ej. {h[0]})'
                  for f, h in sorted(listas_kit.items())]
    return {'hojas_checklist': hojas, 'hojas_p4': hojas_p4,
            'dv_incorrectas': dv_mal,
            'instrucciones_con_bio': con_bio, 'sin_bio': sin_bio,
            'listas_dv_del_producto': sorted(listas_kit),
            'aviso_dv_mezcladas': mezcla}


def gate_precargado(carpeta):
    """§6 — «08: ninguna tarea sin Responsable/Hora» (DOM-06/TEC-06).

    R3-b — el gate AUDITA QUE ESTÁ AUDITANDO EL FICHERO CORRECTO. En bar y en
    dark-kitchen daba verde («48 tareas, 0 huecos») sobre 01-apertura-cierre,
    que ya venía con sus responsables puestos, mientras el 08 real salía con
    D5:E22 vacías en las 18 tareas. Un gate que no comprueba su propio sujeto
    no es un gate: por él pasó dark-kitchen con exit 0 estando roto.
    """
    fname = motor.CTX.get('f_negocio')
    if not fname:
        return {'fichero': None, 'tareas': 0, 'huecos': [],
                'firma_ok': False,
                'huecos_firma': ['no se ha identificado el fichero de NEGOCIO '
                                 'del kit: DOM-06 no se ha aplicado a nada']}
    wb = openpyxl.load_workbook(os.path.join(carpeta, fname))
    papel, detalle = motor.papel_del_fichero(wb)
    firma = []
    if papel != 'negocio':
        firma.append(f'{fname}: el gate está auditando un fichero que NO es el '
                     f'de negocio (papel detectado: {papel}; {detalle})')
    if len(detalle.get('con_notas', [])) != 2:
        firma.append(f'{fname}: se esperaban 2 checklists de apertura/cierre '
                     f'con columna «Notas» y hay '
                     f'{len(detalle.get("con_notas", []))} '
                     f'({detalle.get("con_notas")})')
    huecos, tareas = [], 0
    for ws in wb.worksheets:
        g = motor.geometria(ws)
        if not g:
            continue
        col_r = g['cols'].get('Responsable')
        col_h = motor._col_tiempo(g['cols'])
        for r in range(g['hr'] + 1, g['ultima'] + 1):
            if not isinstance(ws.cell(row=r, column=1).value, int):
                continue
            tareas += 1
            for nombre, c in (('Responsable', col_r), ('Hora', col_h)):
                if c and not ws.cell(row=r, column=c).value:
                    huecos.append(f'{fname}:{ws.title}!'
                                  f'{motor.get_column_letter(c)}{r}: '
                                  f'{nombre} vacío')
    return {'fichero': fname, 'tareas': tareas, 'huecos': huecos,
            'firma_ok': not firma, 'huecos_firma': firma,
            'checklists_con_notas': detalle.get('con_notas')}


def censo(carpeta):
    r = subprocess.run([sys.executable, CENSO, '--only', carpeta, '--fail',
                        '--quiet'], capture_output=True, text=True)
    log(r.stdout.strip())
    if r.returncode != 0:
        log(r.stderr.strip()[-1200:])
    salida = (r.stdout.strip() or r.stderr.strip()).splitlines()
    return {'exit': r.returncode, 'salida': salida[-8:]}


def inventario(carpeta, nombres):
    fuera = []
    for n in nombres:
        wb = openpyxl.load_workbook(os.path.join(carpeta, n))
        hojas = []
        for ws in wb.worksheets:
            hojas.append({
                'hoja': ws.title, 'dim': ws.dimensions,
                'dv': [f'{dv.type}:{dv.formula1}'
                       for dv in ws.data_validations.dataValidation],
                'cf': len(list(ws.conditional_formatting)),
                'print_area': ws.print_area,
                'orient': ws.page_setup.orientation,
                'a4': ws.page_setup.paperSize == 9,
                'protegida': bool(ws.protection.sheet),
                'formulas': sum(1 for row in ws.iter_rows() for c in row
                                if c.data_type == 'f'),
            })
        fuera.append({'fichero': n, 'title': wb.properties.title,
                      'subject': wb.properties.subject, 'hojas': hojas})
    return fuera


# ==========================================================================
def main():
    ap = argparse.ArgumentParser(
        description='Post-proceso v2.0 de la familia Kit de Tareas')
    ap.add_argument('--producto', default='kit-tareas')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--solo', default='motor,contenido',
                    help='etapas: motor, contenido')
    ap.add_argument('--json', default=None)
    ap.add_argument('--sin-idempotencia', action='store_true')
    ap.add_argument('--sin-demos', action='store_true')
    args = ap.parse_args()

    pid = args.producto
    origen = os.path.join(DL, pid)
    destino = os.path.join(SCRATCH, 'dryrun-kt', pid)
    idem_dir = os.path.join(SCRATCH, 'dryrun-kt', pid + '-idem')
    demos_dir = os.path.join(SCRATCH, 'dryrun-kt', '_demos', pid)

    if not args.dry_run and os.environ.get('KIT_TAREAS_APPLY') != '1':
        raise SystemExit(
            f'ABORTADO: sin --dry-run este script escribiría en {origen}, que '
            'la SPEC declara intocable hasta que la ronda 2 dé verde. Usa '
            '--dry-run (o KIT_TAREAS_APPLY=1 si eres el orquestador y ya '
            'tienes el visto bueno).')

    respaldo = None
    if args.dry_run:
        preparar_copia(origen, destino)
        carpeta = destino
    else:
        carpeta = origen
        respaldo = os.path.join(
            SCRATCH, f'{pid}.bak-'
            + datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
        os.makedirs(os.path.dirname(respaldo), exist_ok=True)
        shutil.copytree(origen, respaldo)
        log(f'  respaldo previo de los entregables: {respaldo}')

    etapas = {e.strip() for e in args.solo.split(',') if e.strip()}
    contenido = None
    modulo = 'contenido_' + pid.replace('-', '_')
    if 'contenido' in etapas:
        try:
            contenido = importlib.import_module(modulo)
            log(f'  {modulo} cargado')
        except ImportError:
            log(f'  {modulo}.py no existe — sólo motor')

    nombres = ficheros_de(carpeta)
    log(f'\n== 1/7 · contexto del kit ({len(nombres)} xlsx) ==')
    try:
        ctx = motor.contexto(
            carpeta, nombres,
            lambda f: openpyxl.load_workbook(os.path.join(carpeta, f)))
    except motor.KitAmbiguo as e:
        # R3-a — el motor NO adivina el papel de un fichero. Se aborta con el
        # informe escrito, para que el orquestador vea por qué.
        log('\nABORTADO — ' + str(e))
        if args.json:
            os.makedirs(os.path.dirname(os.path.abspath(args.json)),
                        exist_ok=True)
            with open(args.json, 'w', encoding='utf-8') as fh:
                json.dump({'producto': pid, 'version': '2.0', 'spec': SPEC,
                           'modo': 'dry-run' if args.dry_run else 'produccion',
                           'abortado': str(e), 'fallos': [str(e)], 'exit': 2},
                          fh, ensure_ascii=False, indent=1)
        return 2
    ctx['producto'] = pid
    motor.CTX['producto'] = pid
    log(f"  kit «{ctx['kit']}» · en alcance {len(ctx['ficheros'])}/"
        f"{len(nombres)} · negocio={ctx['f_negocio']} caja={ctx['f_caja']} "
        f"areas={ctx['f_areas']} · hora ancla {ctx['hora_apertura']} · "
        f"cierre «{ctx['literal_cierre']}»")

    log(f'\n== 2/7 · post-proceso ==')
    motor.SOLAPES.clear()
    informe_ficheros, registros = [], {}
    for fname in nombres:
        registros[fname] = procesar(carpeta, fname, etapas, contenido,
                                    informe_ficheros)
        f = informe_ficheros[-1]
        if f['en_alcance']:
            estado_txt = (f"{len(f['cambios'])} cambios, "
                          f"{f['formulas_nuevas']} fórmulas")
        elif f['guardado']:
            # R3-e — «fuera de alcance» ya no significa «intacto»: el molde P4
            # recibe DV, contador, CF y bio sin entrar en el molde ▸.
            estado_txt = (f"fuera del molde ▸ · molde P4: "
                          f"{len(f['cambios'])} cambios, "
                          f"{f['formulas_nuevas']} fórmulas")
        else:
            estado_txt = 'FUERA DE ALCANCE (intacto)'
        log(f'  {fname}: {estado_txt}')

    # R3-f — se fotografía ANTES de la 2.ª pasada, que volvería a acumular.
    solapes = sorted(motor.SOLAPES, key=lambda d: -d['ratio'])
    if solapes:
        log('  solape medido banda↔marco (umbral de anotación '
            f'{motor.UMBRAL_BANDA:.0%}): '
            + ' · '.join(f"{d['hoja']} {d['ratio']:.0%}"
                         + ('' if d['anotada'] else ' (NO anotada)')
                         for d in solapes[:6]))

    idem = {'ejecutada': False}
    if not args.sin_idempotencia:
        log('\n== 3/7 · idempotencia (2.ª pasada sobre un clon) ==')
        if os.path.isdir(idem_dir):
            shutil.rmtree(idem_dir)
        shutil.copytree(carpeta, idem_dir)
        antes = {n: digest(os.path.join(carpeta, n)) for n in nombres}
        motor.contexto(
            idem_dir, nombres,
            lambda f: openpyxl.load_workbook(os.path.join(idem_dir, f)))
        motor.CTX['producto'] = pid
        for fname in nombres:
            procesar(idem_dir, fname, etapas, contenido, [])
        difs = []
        for n in nombres:
            difs += diff_digest(antes[n], digest(os.path.join(idem_dir, n)), n)
        idem = {'ejecutada': True, 'diferencias': len(difs),
                'detalle': difs[:30]}
        log(f'  diferencias 1.ª vs 2.ª pasada: {len(difs)}')
        for d in difs[:10]:
            log('    ' + d)
        motor.contexto(
            carpeta, nombres,
            lambda f: openpyxl.load_workbook(os.path.join(carpeta, f)))
        motor.CTX['producto'] = pid

    log('\n== 4/7 · inject_cache (al final del todo) ==')
    guardados = [f['fichero'] for f in informe_ficheros if f['guardado']]
    cache = inject_cache(carpeta, guardados)

    log('\n== 5/7 · data_only de las fórmulas nuevas ==')
    ver = verificar_cache(carpeta, registros)
    log(f"  con valor: {ver['con_valor']} · fallos: {len(ver['fallos'])}")
    for f in ver['fallos'][:8]:
        log('    ' + f)

    log('\n== 6/7 · pycel con los casos de §6 + DV y bio ==')
    demostraciones = []
    if not args.sin_demos:
        if os.path.isdir(demos_dir):
            shutil.rmtree(demos_dir)
        demostraciones = (demo_arqueo(carpeta, demos_dir)
                          + demo_contador(carpeta, demos_dir)
                          + demo_07(carpeta, demos_dir))
    for c in demostraciones:
        log(f"  {c['caso']} · {c['ref']}: {c['obtenido']!r} "
            f"{'OK' if c['ok'] else 'FALLA (esperaba ' + repr(c['esperado']) + ')'}")
    gates = gate_dv_y_bio(carpeta, nombres)
    log(f"  DV «✓,—,N/A»: {gates['hojas_checklist']} hojas de checklist, "
        f"{len(gates['dv_incorrectas'])} incorrectas · bio en "
        f"{gates['instrucciones_con_bio']}/{len(ctx['ficheros'])} "
        'Instrucciones en alcance')
    for d in gates['dv_incorrectas'][:8]:
        log('    ' + d)
    for m in gates['aviso_dv_mezcladas']:
        log('    AVISO TEC-R2-08 · el producto tiene MÁS de una lista de '
            'desplegable: ' + m)
    prec = gate_precargado(carpeta)
    log(f"  08 precargado: fichero {prec['fichero']} "
        f"(firma de negocio {'OK' if prec.get('firma_ok') else 'NO VÁLIDA'}) · "
        f"{prec['tareas']} tareas, {len(prec['huecos'])} sin "
        'Responsable u Hora')
    for h in prec.get('huecos_firma', []):
        log('    ' + h)
    for h in prec['huecos'][:6]:
        log('    ' + h)
    rec = gate_recuento(carpeta, nombres)
    log(f"  recuento de tareas entregadas: {rec['total']} en total · "
        + ' · '.join(f'{k.split("-")[0]}={v}'
                     for k, v in rec['por_fichero'].items() if v))

    log('\n== 7/7 · censo-entregables --fail ==')
    cen = censo(carpeta)

    fallos = []
    if idem.get('diferencias'):
        fallos.append(f"idempotencia: {idem['diferencias']} diferencias")
    if ver['fallos']:
        fallos.append(f"cache: {len(ver['fallos'])} fórmulas sin valor")
    fallos += [f"§6 {c['caso']}: esperaba {c['esperado']!r}, dio "
               f"{c['obtenido']!r}" for c in demostraciones if not c['ok']]
    fallos += gates['dv_incorrectas']
    fallos += prec.get('huecos_firma', [])
    fallos += prec['huecos'][:10]
    fallos += [f'sin bio en Instrucciones: {n}' for n in gates['sin_bio']
               if n in ctx['ficheros']]
    if cen['exit'] != 0:
        fallos.append('censo-entregables --fail devolvió ' + str(cen['exit']))
    if not args.sin_demos and not demostraciones:
        fallos.append('§6: no se pudo ejecutar ninguna demostración')

    informe = {
        'producto': pid, 'version': '2.0', 'spec': SPEC,
        'fecha': datetime.datetime.now().isoformat(timespec='seconds'),
        'modo': 'dry-run' if args.dry_run else 'produccion',
        'etapas': sorted(etapas),
        'carpeta_origen': origen, 'carpeta_trabajo': carpeta,
        'contexto': {k: (sorted(v) if isinstance(v, set) else v)
                     for k, v in ctx.items()},
        'ficheros': informe_ficheros,
        'fuera_de_alcance': [f['fichero'] for f in informe_ficheros
                             if not f['en_alcance']],
        'inventario': inventario(carpeta, nombres),
        'gates': {
            'idempotencia': idem,
            'inject_cache': cache,
            'data_only_formulas_nuevas': ver,
            'dv_y_bio': gates,
            'negocio_precargado': prec,
            'recuento_tareas': rec,
            'bandas_solapadas': solapes,
            'censo_entregables': cen,
        },
        'demostraciones_spec_6': demostraciones,
        'fallos': fallos,
        'exit': 1 if fallos else 0,
        'respaldo': respaldo,
    }
    if args.json:
        os.makedirs(os.path.dirname(os.path.abspath(args.json)), exist_ok=True)
        with open(args.json, 'w', encoding='utf-8') as fh:
            json.dump(informe, fh, ensure_ascii=False, indent=1)
        log(f'\ninforme → {args.json}')

    log('\n' + ('FALLOS:\n  ' + '\n  '.join(fallos) if fallos
                else 'TODO VERDE (idempotencia, cache, §6, DV, bio, censo)'))
    return 1 if fallos else 0


if __name__ == '__main__':
    sys.exit(main())
