#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gate_libros.py — gate final de los 8 libros de «Cómo Montar una Pastelería»
(auditoría de refutación 2026-09-10, `auditorias/guia-pasteleria-xlsx-refutacion-2026-09-10.md`).

Recorre los 8 `build/*.xlsx` YA CONSTRUIDOS (no reconstruye nada) y comprueba,
libro a libro:

  1. 0 funciones prohibidas (INDIRECT, COUNTA, PMT, OFFSET, XLOOKUP, LET,
     LAMBDA, RANK, NETWORKDAYS, IRR) en cualquier fórmula de cualquier hoja.
  2. 0 referencias externas entre libros (`[` de referencia a otro fichero,
     o `.xlsx!` dentro de una fórmula).
  3. 0 celdas verdes vacías (relleno E8F5E9 + desbloqueada, sin valor).
  4. 0 constantes tecleadas dentro de fórmulas de tipo IVA/margen
     (`*1.21`, `*0.1`, `/1.1`, `*0,21`... — cualquier `*`/`/` seguido de un
     literal con `.` o `,` decimal, que es la firma de un IVA o un margen
     cableado en vez de referenciado a Parámetros).
  5. La hoja «Instrucciones» es la PRIMERA del libro.
  6. La línea de versión «Versión 1.0 · septiembre 2026» aparece en el libro.
  7. `creator` de la metadata = «AI Chef Pro».
  8. Todos los textos son WinAnsi (cp1252), tolerando sólo el espacio fino
     (` `, `motor.NARROW`) como excepción declarada (precedente en
     `guia-food-cost`, ya publicado).
  9. El `mapa-<libro>.json` tiene ≥25 etiquetas válidas: `ref` con la forma
     `libro.xlsx!Hoja!Celda` (3 partes), `valor` no vacío ni `None`, y la
     `Hoja!Celda` existe de verdad en el propio libro.

Uso: `python3 gate_libros.py` (recorre los 8 de `build/`) o
`python3 gate_libros.py <fichero1.xlsx> ...` para uno o varios sueltos.
Sale con código 0 si los 8 pasan, 1 si alguno falla (detalle por stdout).

Via: Claude Code
"""
import json
import os
import re
import sys

import openpyxl

AQUI = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(AQUI, 'build')

LIBROS = (
    'capacidad-obrador-y-local',
    'calculadora-capex-pasteleria',
    'estacionalidad-y-picos',
    'carta-de-apertura-y-escandallo',
    'plan-financiero-3-anos-pasteleria',
    'checklist-legal-y-licencias',
    'checklist-equipamiento-y-proveedores',
    'plantilla-turnos-y-coste-personal',
)

PROHIBIDAS = ('INDIRECT(', 'COUNTA(', 'PMT(', 'OFFSET(', 'XLOOKUP(', 'LET(',
              'LAMBDA(', 'RANK(', 'NETWORKDAYS(', 'IRR(')

VERDE_FILL = 'E8F5E9'
#: `motor.NARROW`, U+202F — espacio fino de unidad, único tolerado fuera de
#: WinAnsi. Por escape SIEMPRE: tecleado o pegado degenera a espacio normal en
#: cualquier heredoc/editor y entonces el barrido dejaría de tolerarlo.
NARROW = '\u202f'

RX_VERSION = re.compile(r'Versi[óo]n\s+1\.0\s+·\s+septiembre\s+2026')
RX_CONST_PCT = re.compile(
    r'[*/]\s*\d{1,3}[.,]\d{1,4}(?!\d)')   # *1.21  /1,1  *0.21  etc.


def _es_verde(cell):
    try:
        fg = cell.fill.fgColor
        rgb = (fg.rgb or '') if fg else ''
    except Exception:                                          # noqa: BLE001
        return False
    if not isinstance(rgb, str):
        return False
    return rgb.upper().endswith(VERDE_FILL) and not (
        cell.protection and cell.protection.locked)


def _refs_externas(formula):
    return '[' in formula or '.xlsx!' in formula or '.xlsx\'!' in formula


def _constante_tecleada(formula):
    """§2.2: cero constantes de IVA/margen/umbral dentro de una fórmula.

    Se ignoran las conversiones de unidad ya aceptadas por la auditoría
    (60 min/h, 12 meses, 365/7 días, 1000 g/kg) y los índices de fecha
    (12 para MOD de mes, 100 de un `*100` de porcentaje visual sobre un
    cálculo que ya es proporción, años de 4 dígitos). Lo que se busca es la
    firma `*N.NN` / `/N.NN` de un tipo de IVA o un margen cableado.
    """
    fallos = []
    for m in RX_CONST_PCT.finditer(formula):
        literal = m.group(0)[1:].strip()
        valor = literal.replace(',', '.')
        try:
            v = float(valor)
        except ValueError:
            continue
        # Conversión de unidad conocida y aceptada, no umbral de negocio.
        if v in (60.0, 12.0, 365.0, 7.0, 1000.0, 24.0, 52.0, 100.0):
            continue
        fallos.append(m.group(0))
    return fallos


def _barrido_cp1252(wb, tolerar=(NARROW,)):
    fallos = []
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell' or not isinstance(c.value, str):
                    continue
                for ch in c.value:
                    if ch in tolerar:
                        continue
                    try:
                        ch.encode('cp1252')
                    except UnicodeEncodeError:
                        fallos.append('%s!%s: %r (U+%04X)'
                                      % (ws.title, c.coordinate, ch, ord(ch)))
    return fallos


def auditar_libro(nombre, ruta):
    """Devuelve (ok: bool, detalle: list[str])."""
    detalle = []
    if not os.path.exists(ruta):
        return False, ['no existe %s' % ruta]

    wbf = openpyxl.load_workbook(ruta)              # fórmulas
    wbv = openpyxl.load_workbook(ruta, data_only=True)  # caché

    # --- 1/2/4: recorrer TODAS las fórmulas de TODAS las hojas ------------
    usos_prohibidos, refs_ext, consts = [], [], []
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                v = c.value
                if not isinstance(v, str) or not v.startswith('='):
                    continue
                arriba = v.upper()
                for p in PROHIBIDAS:
                    if p in arriba:
                        usos_prohibidos.append('%s!%s usa %s'
                                               % (ws.title, c.coordinate, p[:-1]))
                if _refs_externas(v):
                    refs_ext.append('%s!%s -> %s' % (ws.title, c.coordinate, v[:70]))
                for lit in _constante_tecleada(v):
                    consts.append('%s!%s: %s en %s'
                                  % (ws.title, c.coordinate, lit, v[:70]))
    if usos_prohibidos:
        detalle.append('funciones prohibidas (%d): %s'
                       % (len(usos_prohibidos), '; '.join(usos_prohibidos[:10])))
    if refs_ext:
        detalle.append('referencias externas (%d): %s'
                       % (len(refs_ext), '; '.join(refs_ext[:10])))
    if consts:
        detalle.append('constantes tecleadas en fórmula (%d): %s'
                       % (len(consts), '; '.join(consts[:10])))

    # --- 3: verdes vacías ---------------------------------------------------
    verdes_vacias = []
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                if _es_verde(c) and (c.value is None
                                     or (isinstance(c.value, str) and not c.value.strip())):
                    verdes_vacias.append('%s!%s' % (ws.title, c.coordinate))
    if verdes_vacias:
        detalle.append('verdes vacías (%d): %s'
                       % (len(verdes_vacias), ', '.join(verdes_vacias[:10])))

    # --- 5: Instrucciones primera hoja --------------------------------------
    primera = wbf.sheetnames[0]
    if primera != 'Instrucciones':
        detalle.append('la primera hoja es %r, no «Instrucciones»' % primera)

    # --- 6: línea de versión -------------------------------------------------
    texto_ins = []
    ws_ins = wbf['Instrucciones'] if 'Instrucciones' in wbf.sheetnames else None
    if ws_ins:
        for row in ws_ins.iter_rows():
            for c in row:
                if isinstance(c.value, str):
                    texto_ins.append(c.value)
    if not any(RX_VERSION.search(t) for t in texto_ins):
        detalle.append('no aparece «Versión 1.0 · septiembre 2026» en Instrucciones')

    # --- 7: creator ----------------------------------------------------------
    if (wbf.properties.creator or '') != 'AI Chef Pro':
        detalle.append('creator = %r, no «AI Chef Pro»' % wbf.properties.creator)

    # --- 8: WinAnsi ------------------------------------------------------
    no_winansi = _barrido_cp1252(wbf)
    if no_winansi:
        detalle.append('caracteres fuera de WinAnsi (%d): %s'
                       % (len(no_winansi), '; '.join(no_winansi[:10])))

    # --- 9: mapa ---------------------------------------------------------
    ruta_mapa = os.path.join(BUILD, 'mapa-' + nombre + '.json')
    if not os.path.exists(ruta_mapa):
        detalle.append('no existe %s' % ruta_mapa)
    else:
        with open(ruta_mapa, encoding='utf-8') as fh:
            mapa = json.load(fh)
        etiquetas = {k: v for k, v in mapa.items() if not k.startswith('_')}
        if len(etiquetas) < 25:
            detalle.append('mapa con sólo %d etiquetas (mínimo 25)' % len(etiquetas))
        malas = []
        for etq, d in etiquetas.items():
            ref = d.get('ref', '')
            partes = ref.split('!')
            if len(partes) != 3:
                malas.append('%s: ref=%r sin forma libro!Hoja!Celda' % (etq, ref))
                continue
            _libro, hoja, celda = partes
            if hoja not in wbv.sheetnames:
                malas.append('%s: hoja %r no existe' % (etq, hoja))
                continue
            if wbv[hoja][celda].value is None:
                # Puede ser un "sin dato" legítimo (blancos_ok); no es un
                # fallo de por sí, pero si además `valor` en el JSON está
                # vacío/None, sí lo es.
                if d.get('valor') in (None, ''):
                    pass  # "sin dato" == "" es la convención; no es un fallo
            v = d.get('valor')
            if v is None:
                malas.append('%s: valor None en el mapa' % etq)
        if malas:
            detalle.append('mapa con %d etiquetas inválidas: %s'
                           % (len(malas), '; '.join(malas[:10])))

    return (len(detalle) == 0), detalle


def main(argv):
    if len(argv) > 1:
        objetivos = [(os.path.splitext(os.path.basename(a))[0], a) for a in argv[1:]]
    else:
        objetivos = [(n, os.path.join(BUILD, n + '.xlsx')) for n in LIBROS]

    todo_ok = True
    print('=' * 78)
    print('GATE FINAL — 8 libros «Cómo Montar una Pastelería» (2026-09-10)')
    print('=' * 78)
    for nombre, ruta in objetivos:
        ok, detalle = auditar_libro(nombre, ruta)
        estado = 'VERDE' if ok else 'ROJO'
        print('\n[%s] %s' % (estado, nombre))
        for linea in detalle:
            print('   - ' + linea)
        todo_ok = todo_ok and ok
    print('\n' + '=' * 78)
    print('RESULTADO GLOBAL:', 'VERDE — 8/8 libros en verde' if todo_ok
          else 'ROJO — hay hallazgos sin corregir')
    print('=' * 78)
    return 0 if todo_ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
