#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gate_libros.py — gate final de los 8 libros de «Cómo Montar una Churrería-Chocolatería»
(producto 51, `guia-churreria-chocolateria`). Calcado de `guia-chocolateria/gate_libros.py`
(que a su vez viene del de la pastelería), MÁS el gate nuevo de la SPEC §2.4 (D16):
`auditar_ciclos(D)` y las comprobaciones de cruces que pidió la refutación de los 8 xlsx
(`auditorias/guia-churreria-xlsx-refutacion-2026-10-03.md`).

Recorre los 8 `build/*.xlsx` YA CONSTRUIDOS (no reconstruye nada) y comprueba, libro a libro:

  1. 0 funciones prohibidas (INDIRECT, COUNTA, PMT, OFFSET, XLOOKUP, LET, LAMBDA, RANK,
     NETWORKDAYS, IRR) en cualquier fórmula de cualquier hoja.
  2. 0 referencias externas entre libros (`[`, o `.xlsx!` dentro de una fórmula).
  3. 0 celdas verdes vacías (relleno E8F5E9 + desbloqueada, sin valor).
  4. 0 constantes tecleadas dentro de fórmulas de tipo IVA/margen/umbral (`*1.21`, `/1,1`...).
  5. La hoja «Instrucciones» es la PRIMERA del libro.
  6. La línea «Versión 1.0 · octubre 2026» aparece en Instrucciones.
  7. `creator` de la metadata = «AI Chef Pro».
  8. Todos los textos son WinAnsi (cp1252), salvo el espacio fino (U+202F) declarado.
  9. El `mapa-<libro>.json` tiene >= 25 etiquetas válidas (ref de tres partes, hoja y celda
     que existen, valor igual al `data_only`), y cita TODAS las celdas de origen de `CRUCES`.
 10. A4 y hojas protegidas; ningún texto interno de la fábrica (R-09 de la refutación); ningún
     literal de texto de más de 255 caracteres dentro de una fórmula (límite de Excel).

Y, sobre los ocho a la vez (SPEC §2.4):

 11. `auditar_ciclos(D)`: Kahn sobre `D.CRUCES`; ABORTA si queda un nodo en ciclo, si
     `D.ORDEN_RELLENO` no es un orden topológico del grafo, si el libro 7 aparece en alguna
     arista, o si alguna hoja tiene un rótulo «cópialo del libro N» / «trae aquí la cifra de»
     que no está en `CRUCES`. Se prueba antes de usarlo con DOS CANARIOS (un `CRUCES` con
     ciclo y otro con una arista hacia atrás), más uno de rótulo no declarado: los tres tienen
     que abortar, o el gate no sirve.
 12. `auditar_cruces(D)`: cada celda cruzada tiene su rótulo literal y su verde en la hoja
     receptora, con el `valor_defecto`; la celda de origen (K rótulo, L valor) publica ese
     valor; UNA fila de CUADRE por celda cruzada (contadas contra `CRUCES`).
 13. Ninguna fila ni bloque «fondo de maniobra» en el libro 2; ningún «gastos fijos» ni
     «renta» en el 5; ninguna hoja de escandallo referencia una celda cuya nota diga «CON IVA».
 14. Las notas legales de la refutación: ni «seis» ni «media» (cuota del 676) en ningún
     comentario del libro 7; ningún «art. 8» de la norma de aceites en un comentario.
 15. R-03: el libro 1 cita la celda del veredicto «¿Una churrera o dos?» del libro 5, y esa
     celda existe y contiene un veredicto.

Uso: `python3 gate_libros.py` (recorre los 8 de `build/`). Sale con código 0 si todo pasa, 1 si
algo falla (detalle por stdout). `GUIA_BUILD_DIR` cambia el directorio.

Via: Claude Code
"""
import importlib.util
import json
import os
import re
import sys
import types

import openpyxl

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)
BUILD = os.environ.get('GUIA_BUILD_DIR') or os.path.join(AQUI, 'build')

PROHIBIDAS = ('INDIRECT(', 'COUNTA(', 'PMT(', 'OFFSET(', 'XLOOKUP(', 'LET(',
              'LAMBDA(', 'RANK(', 'NETWORKDAYS(', 'IRR(')

VERDE_FILL = 'E8F5E9'
#: `motor.NARROW`, U+202F: único carácter fuera de WinAnsi tolerado. Por escape SIEMPRE.
NARROW = ' '

RX_VERSION = re.compile(r'Versi[óo]n\s+1\.0\s+·\s+octubre\s+2026')
RX_CONST_PCT = re.compile(r'[*/]\s*\d{1,3}[.,]\d{1,4}(?!\d)')   # *1.21  /1,1  *0.21  etc.
RX_ROTULO = re.compile(r'c[óo]pialo del libro|trae aqu[íi] la cifra de', re.I)
RX_ART8 = re.compile(r'\barts?\.\s?8\b', re.I)


def _cargar_datos_ejemplo():
    spec = importlib.util.spec_from_file_location(
        'datos_ejemplo_churreria_gate', os.path.join(AQUI, 'datos_ejemplo.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    import enmiendas_churreria
    enmiendas_churreria.aplicar(mod)       # el contrato de cruces enmendado: el MISMO que usan los 8
    return mod


def _es_verde(cell):
    try:
        fg = cell.fill.fgColor
        rgb = (fg.rgb or '') if fg else ''
    except Exception:                                          # noqa: BLE001
        return False
    if not isinstance(rgb, str):
        return False
    return rgb.upper().endswith(VERDE_FILL) and not (cell.protection and cell.protection.locked)


def _refs_externas(formula):
    return '[' in formula or '.xlsx!' in formula or ".xlsx'!" in formula


def _constante_tecleada(formula):
    """Cero constantes de IVA/margen/umbral dentro de una fórmula. Se ignoran las conversiones
    de unidad aceptadas (60 min/h, 12 meses, 365/7 días, 1000 g/kg, 24 h, 52 semanas, 100)."""
    fallos = []
    for m in RX_CONST_PCT.finditer(formula):
        literal = m.group(0)[1:].strip()
        try:
            v = float(literal.replace(',', '.'))
        except ValueError:
            continue
        if v in (60.0, 12.0, 365.0, 7.0, 1000.0, 24.0, 52.0, 100.0):
            continue
        fallos.append(m.group(0))
    return fallos


def _barrido_cp1252(wb):
    fallos = []
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                textos = []
                if isinstance(c.value, str):
                    textos.append(c.value)
                if c.comment is not None:
                    textos.append(c.comment.text)
                for t in textos:
                    for ch in t:
                        if ch == NARROW:
                            continue
                        try:
                            ch.encode('cp1252')
                        except UnicodeEncodeError:
                            fallos.append('%s!%s: %r (U+%04X)' % (ws.title, c.coordinate, ch, ord(ch)))
    return fallos


# ==========================================================================
# 1. Un libro
# ==========================================================================
def auditar_libro(nombre, ruta, D):
    """Devuelve (ok, detalle, wbf, wbv)."""
    detalle = []
    if not os.path.exists(ruta):
        return False, ['no existe %s' % ruta], None, None
    import enmiendas_churreria as E
    wbf = openpyxl.load_workbook(ruta)
    wbv = openpyxl.load_workbook(ruta, data_only=True)

    usos, refs_ext, consts = [], [], []
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                v = c.value
                if not isinstance(v, str) or not v.startswith('='):
                    continue
                for p in PROHIBIDAS:
                    if p in v.upper():
                        usos.append('%s!%s usa %s' % (ws.title, c.coordinate, p[:-1]))
                if _refs_externas(v):
                    refs_ext.append('%s!%s -> %s' % (ws.title, c.coordinate, v[:70]))
                for lit in _constante_tecleada(v):
                    consts.append('%s!%s: %s en %s' % (ws.title, c.coordinate, lit, v[:70]))
    # Excel no admite un literal de texto de más de 255 caracteres dentro de una fórmula
    largos = []
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                v = c.value
                if isinstance(v, str) and v.startswith('='):
                    if len(v) > 8000:
                        largos.append('%s!%s: fórmula de %d caracteres' % (ws.title, c.coordinate, len(v)))
                    for lit in re.findall(r'"((?:[^"]|"")*)"', v):
                        if len(lit) > 255:
                            largos.append('%s!%s: literal de %d caracteres' % (ws.title, c.coordinate, len(lit)))
    if largos:
        detalle.append('límites de Excel (%d): %s' % (len(largos), '; '.join(largos[:6])))
    if usos:
        detalle.append('funciones prohibidas (%d): %s' % (len(usos), '; '.join(usos[:10])))
    if refs_ext:
        detalle.append('referencias externas (%d): %s' % (len(refs_ext), '; '.join(refs_ext[:10])))
    if consts:
        detalle.append('constantes tecleadas en fórmula (%d): %s' % (len(consts), '; '.join(consts[:10])))

    vacias = []
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                if _es_verde(c) and (c.value is None or (isinstance(c.value, str) and not c.value.strip())):
                    vacias.append('%s!%s' % (ws.title, c.coordinate))
    if vacias:
        detalle.append('verdes vacías (%d): %s' % (len(vacias), ', '.join(vacias[:10])))

    if wbf.sheetnames[0] != 'Instrucciones':
        detalle.append('la primera hoja es %r, no «Instrucciones»' % wbf.sheetnames[0])
    textos_ins = []
    if 'Instrucciones' in wbf.sheetnames:
        for row in wbf['Instrucciones'].iter_rows():
            for c in row:
                if isinstance(c.value, str):
                    textos_ins.append(c.value)
    if not any(RX_VERSION.search(t) for t in textos_ins):
        detalle.append('no aparece «Versión 1.0 · octubre 2026» en Instrucciones')

    if (wbf.properties.creator or '') != 'AI Chef Pro':
        detalle.append('creator = %r, no «AI Chef Pro»' % wbf.properties.creator)

    no_winansi = _barrido_cp1252(wbf)
    if no_winansi:
        detalle.append('caracteres fuera de WinAnsi (%d): %s' % (len(no_winansi), '; '.join(no_winansi[:10])))

    # A4 y protección
    for ws in wbf.worksheets:
        if ws.page_setup.paperSize != 9:
            detalle.append('«%s» no es A4 (paperSize=%r)' % (ws.title, ws.page_setup.paperSize))
        if not ws.protection.sheet:
            detalle.append('«%s» no está protegida' % ws.title)

    # R-09: ningún texto interno de la fábrica
    internos = []
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                textos = []
                if isinstance(c.value, str) and not c.value.startswith('='):
                    textos.append(c.value)
                if c.comment is not None:
                    textos.append(c.comment.text)
                for t in textos:
                    r = E.interno_en(t)
                    if r:
                        internos.append('%s!%s: %s' % (ws.title, c.coordinate, ', '.join(r)))
    if internos:
        detalle.append('texto interno de la fábrica (%d): %s' % (len(internos), '; '.join(internos[:8])))

    # mapa
    ruta_mapa = os.path.join(BUILD, 'mapa-' + nombre + '.json')
    if not os.path.exists(ruta_mapa):
        detalle.append('no existe %s' % ruta_mapa)
    else:
        with open(ruta_mapa, encoding='utf-8') as fh:
            mapa = json.load(fh)
        etiquetas = dict((k, v) for k, v in mapa.items() if not k.startswith('_'))
        if len(etiquetas) < 25:
            detalle.append('mapa con sólo %d etiquetas (mínimo 25)' % len(etiquetas))
        malas = []
        for etq, d in etiquetas.items():
            partes = d.get('ref', '').split('!')
            if len(partes) != 3:
                malas.append('%s: ref=%r sin forma libro!Hoja!Celda' % (etq, d.get('ref')))
                continue
            _l, hoja, celda = partes
            if hoja not in wbv.sheetnames:
                malas.append('%s: hoja %r no existe' % (etq, hoja))
                continue
            v = d.get('valor')
            if v is None:
                malas.append('%s: valor None en el mapa' % etq)
                continue
            real = wbv[hoja][celda].value
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                if not isinstance(real, (int, float)) or abs(real - v) > max(1e-9, abs(v) * 1e-9):
                    malas.append('%s: el mapa dice %r y la celda %r' % (etq, v, real))
            elif hasattr(real, 'isoformat'):
                # una fecha: el mapa la guarda como texto ISO (aaaa-mm-dd[ hh:mm:ss])
                if str(v)[:10] != real.isoformat()[:10]:
                    malas.append('%s: el mapa dice %r y la celda %r' % (etq, v, real))
            elif (real if real is not None else '') != v and str(real) != str(v):
                malas.append('%s: el mapa dice %r y la celda %r' % (etq, v, real))
            if d.get('tipo') not in ('entrada', 'salida', 'parametro'):
                malas.append('%s: tipo %r no válido' % (etq, d.get('tipo')))
        if malas:
            detalle.append('mapa con %d etiquetas inválidas: %s' % (len(malas), '; '.join(malas[:8])))
    return (len(detalle) == 0), detalle, wbf, wbv


# ==========================================================================
# 2. SPEC §2.4: el grafo de cruces
# ==========================================================================
def _problemas_grafo(cruces, orden_relleno, libros, hay_ciclo_fn=None):
    """Núcleo de `auditar_ciclos` (sin hojas): ciclo, orden no topológico y libro 7 en una arista.
    Se separa para poder probarlo con los canarios."""
    problemas = []
    arcos = set((c['origen'], c['receptor']) for c in cruces)
    nodos = set(libros)
    entrada = dict((n, 0) for n in nodos)
    for _a, b in arcos:
        entrada[b] += 1
    libres = sorted(n for n in nodos if entrada[n] == 0)
    orden = []
    while libres:                                              # Kahn
        n = libres.pop(0)
        orden.append(n)
        for a, b in sorted(arcos):
            if a == n:
                entrada[b] -= 1
                if entrada[b] == 0:
                    libres.append(b)
                    libres.sort()
    en_ciclo = sorted(n for n in nodos if n not in orden)
    if en_ciclo:
        problemas.append('CICLO entre libros: quedan sin ordenar %s' % en_ciclo)
    if sorted(orden_relleno) != sorted(nodos):
        problemas.append('ORDEN_RELLENO %s no contiene exactamente los libros %s'
                         % (list(orden_relleno), sorted(nodos)))
    else:
        pos = dict((n, i) for i, n in enumerate(orden_relleno))
        atras = sorted((a, b) for a, b in arcos if pos[a] >= pos[b])
        if atras:
            problemas.append('ORDEN_RELLENO no es un orden topológico: aristas hacia atrás %s' % atras)
    if any(7 in a for a in arcos):
        problemas.append('el libro 7 aparece en una arista: %s' % sorted(a for a in arcos if 7 in a))
    return problemas


def _rotulos_no_declarados(wbf_por_libro, D):
    """Cualquier celda de texto con «cópialo del libro N» / «trae aquí la cifra de» que no sea EXACTAMENTE
    el rótulo de una entrada de `D.CRUCES`."""
    declarados = set(D.rotulo_cruce(c) for c in D.CRUCES)
    fallos = []
    for nombre, wbf in wbf_por_libro.items():
        for ws in wbf.worksheets:
            for row in ws.iter_rows():
                for c in row:
                    if c.__class__.__name__ == 'MergedCell':
                        continue
                    vals = []
                    if isinstance(c.value, str) and not c.value.startswith('='):
                        vals.append(c.value)
                    if c.comment is not None:
                        vals.append(c.comment.text)
                    for v in vals:
                        if RX_ROTULO.search(v) and v.strip() not in declarados:
                            fallos.append('%s: %s!%s: %r' % (nombre, ws.title, c.coordinate, v[:80]))
    return fallos


def auditar_ciclos(D, wbf_por_libro=None):
    """SPEC §2.4: ciclo (Kahn), orden de relleno topológico, libro 7 aislado y ningún rótulo
    «cópialo del libro N» que no esté en `CRUCES`. Devuelve la lista de problemas (vacía = bien)."""
    problemas = _problemas_grafo(D.CRUCES, D.ORDEN_RELLENO, list(D.LIBROS))
    if wbf_por_libro:
        problemas += ['rótulo de cruce NO DECLARADO en CRUCES: ' + f
                      for f in _rotulos_no_declarados(wbf_por_libro, D)]
    return problemas


def probar_canarios(D):
    """Antes de fiarse de `auditar_ciclos`, hay que ver que ABORTA con lo que debe abortar.
    Devuelve (lista de líneas, ok)."""
    base = [dict(c) for c in D.CRUCES]
    lineas, ok = [], True

    # canario 1: un CRUCES con ciclo (6 -> 3 cierra 3 -> 6)
    ciclo = base + [{'origen': 6, 'receptor': 3}]
    p1 = _problemas_grafo(ciclo, D.ORDEN_RELLENO, list(D.LIBROS))
    bueno = any(x.startswith('CICLO') for x in p1)
    lineas.append('canario 1 (CRUCES con ciclo 6 -> 3): %s' % ('aborta, bien' if bueno else 'NO ABORTA'))
    ok = ok and bueno

    # canario 2: una arista hacia atrás contra el orden firmado (6 -> 2)
    atras = base + [{'origen': 6, 'receptor': 2}]
    p2 = _problemas_grafo(atras, D.ORDEN_RELLENO, list(D.LIBROS))
    bueno = any('hacia atrás' in x for x in p2)
    lineas.append('canario 2 (arista hacia atrás 6 -> 2): %s' % ('aborta, bien' if bueno else 'NO ABORTA'))
    ok = ok and bueno

    # canario 3: el libro 7 en una arista (7 -> 1)
    siete = base + [{'origen': 7, 'receptor': 1}]
    p3 = _problemas_grafo(siete, D.ORDEN_RELLENO, list(D.LIBROS))
    bueno = any('libro 7' in x for x in p3)
    lineas.append('canario 3 (libro 7 en una arista 7 -> 1): %s' % ('aborta, bien' if bueno else 'NO ABORTA'))
    ok = ok and bueno

    # canario 4: un rótulo «cópialo del libro N» que no está en CRUCES
    wb = openpyxl.Workbook()
    wb.active['A1'] = 'cópialo del libro 9: inventado.xlsx!Hoja!L5'
    p4 = _rotulos_no_declarados({'sintetico': wb}, D)
    bueno = len(p4) == 1
    lineas.append('canario 4 (rótulo no declarado): %s' % ('aborta, bien' if bueno else 'NO ABORTA'))
    ok = ok and bueno

    # y el contrato real tiene que estar limpio
    real = _problemas_grafo(D.CRUCES, D.ORDEN_RELLENO, list(D.LIBROS))
    lineas.append('CRUCES real: %s' % ('sin ciclos, orden de relleno topológico, libro 7 aislado'
                                         if not real else 'PROBLEMAS: %s' % real))
    ok = ok and not real
    return lineas, ok


# ==========================================================================
# 3. SPEC §2.4 y refutación: los cruces contra las hojas reales
# ==========================================================================
def _nombre_libro(D, n):
    return os.path.splitext(D.LIBROS[n])[0]


def auditar_cruces(D, abiertos):
    """`abiertos` = {nombre_libro: (wbf, wbv)}. Cada cruce de `CRUCES`: hoja y celda de origen y
    receptora que EXISTEN, rótulo literal y verde con el `valor_defecto` en el receptor, la celda de
    origen publicando ese valor, y UNA fila de CUADRE por celda cruzada."""
    problemas = []
    por_receptor = {}
    for c in D.CRUCES:
        por_receptor.setdefault(c['receptor'], []).append(c)
        n_o, n_r = _nombre_libro(D, c['origen']), _nombre_libro(D, c['receptor'])
        if n_o not in abiertos or n_r not in abiertos:
            problemas.append('cruce %d (%s): libro %s o %s no auditado' % (c['n'], c['x'], n_o, n_r))
            continue
        wbf_o, wbv_o = abiertos[n_o]
        wbf_r, wbv_r = abiertos[n_r]
        ho, co = c['hoja_origen'], c['celda_origen']
        hr = c['hoja_receptor']
        if ho not in wbv_o.sheetnames:
            problemas.append('cruce %d (%s): la hoja de origen %r NO existe en %s' % (c['n'], c['x'], ho, n_o))
            continue
        if hr not in wbv_r.sheetnames:
            problemas.append('cruce %d (%s): la hoja receptora %r NO existe en %s' % (c['n'], c['x'], hr, n_r))
            continue
        # origen: rótulo en K, valor en L desde la fila 5
        if not re.match(r'^L\d+$', co) or int(co[1:]) < 5:
            problemas.append('cruce %d (%s): la celda de origen %s no está en la L desde la fila 5'
                             % (c['n'], c['x'], co))
        else:
            rot = wbf_o[ho]['K' + co[1:]].value
            if not isinstance(rot, str) or not rot.strip():
                problemas.append('cruce %d (%s): %s!K%s sin rótulo' % (c['n'], c['x'], ho, co[1:]))
            v = wbv_o[ho][co].value
            e = c['valor_defecto']
            if not isinstance(v, (int, float)) or abs(v - e) > max(1e-9, abs(e) * 1e-9):
                problemas.append('cruce %d (%s): %s!%s = %r y el contrato dice %r'
                                 % (c['n'], c['x'], ho, co, v, e))
        # receptor: el rótulo literal, una sola vez, y su verde con el valor por defecto
        rot_lit = D.rotulo_cruce(c)
        sitios = []
        for row in wbf_r[hr].iter_rows():
            for cel in row:
                if cel.__class__.__name__ == 'MergedCell':
                    continue
                if isinstance(cel.value, str) and cel.value.strip() == rot_lit:
                    sitios.append(cel)
        if len(sitios) != 1:
            problemas.append('cruce %d (%s): el rótulo %r aparece %d veces en %s!%s (debe ser 1)'
                             % (c['n'], c['x'], rot_lit, len(sitios), n_r, hr))
            continue
        cel_rot = sitios[0]
        fila = cel_rot.row
        # el valor verde está en la misma fila, en la columna B
        cel_v = wbf_r[hr]['B%d' % fila]
        if not _es_verde(cel_v):
            problemas.append('cruce %d (%s): %s!B%d no es verde y editable' % (c['n'], c['x'], hr, fila))
        vv = wbv_r[hr]['B%d' % fila].value
        e = c['valor_defecto']
        if not isinstance(vv, (int, float)) or abs(vv - e) > max(1e-9, abs(e) * 1e-9):
            problemas.append('cruce %d (%s): %s!B%d = %r y el contrato dice %r' % (c['n'], c['x'], hr, fila, vv, e))
    # una fila de CUADRE por celda cruzada
    for r, cruces in sorted(por_receptor.items()):
        n_r = _nombre_libro(D, r)
        if n_r not in abiertos:
            continue
        wbf_r, _wbv_r = abiertos[n_r]
        hr = cruces[0]['hoja_receptor']
        cuadres = 0
        for row in wbf_r[hr].iter_rows():
            for cel in row:
                if cel.__class__.__name__ == 'MergedCell':
                    continue
                if (cel.column_letter == 'A' and isinstance(cel.value, str)
                        and cel.value.startswith('CUADRE')):
                    cuadres += 1
        if cuadres != len(cruces):
            problemas.append('libro %d (%s): %d filas de CUADRE y %d celdas cruzadas'
                             % (r, n_r, cuadres, len(cruces)))
    # el mapa de cada origen cita sus celdas de origen
    for c in D.CRUCES:
        n_o = _nombre_libro(D, c['origen'])
        ruta = os.path.join(BUILD, 'mapa-' + n_o + '.json')
        if not os.path.exists(ruta):
            continue
        with open(ruta, encoding='utf-8') as fh:
            mapa = json.load(fh)
        ref = '%s!%s!%s' % (c['fichero_origen'], c['hoja_origen'], c['celda_origen'])
        if not any(d.get('ref') == ref for k, d in mapa.items() if not k.startswith('_')):
            problemas.append('cruce %d (%s): el mapa de %s no cita la celda de origen %s'
                             % (c['n'], c['x'], n_o, ref))
    return problemas


def auditar_fronteras(D, abiertos):
    """§2.4: ningún «fondo de maniobra» (fila o bloque) en el 2; ningún «gastos fijos» ni «renta» en
    el 5; ninguna hoja de escandallo referencia una celda cuya nota diga «CON IVA». Más las
    notas legales (R-07, R-08) y el veredicto de «¿una churrera o dos?» (R-03)."""
    problemas = []
    # --- libro 2: ninguna fila ni bloque «fondo de maniobra» -----------------------
    n2 = _nombre_libro(D, 2)
    if n2 in abiertos:
        for ws in abiertos[n2][0].worksheets:
            for row in ws.iter_rows():
                for c in row:
                    if (isinstance(c.value, str) and not c.value.startswith('=')
                            and re.match(r'\s*fondo de maniobra', c.value, re.I)):
                        problemas.append('libro 2: %s!%s abre una fila o bloque «fondo de maniobra»: %r'
                                         % (ws.title, c.coordinate, c.value[:60]))
    # --- libro 5: ningún «gastos fijos» ni «renta» ----------------------------------
    n5 = _nombre_libro(D, 5)
    if n5 in abiertos:
        for ws in abiertos[n5][0].worksheets:
            for row in ws.iter_rows():
                for c in row:
                    if isinstance(c.value, str) and not c.value.startswith('='):
                        if re.search(r'gastos\s+fijos', c.value, re.I) or re.search(r'\brenta\b', c.value, re.I):
                            problemas.append('libro 5: %s!%s con «gastos fijos» o «renta»: %r'
                                             % (ws.title, c.coordinate, c.value[:60]))
    # --- libro 3: ninguna hoja de escandallo referencia una celda cuya nota diga «CON IVA» ----
    n3 = _nombre_libro(D, 3)
    if n3 in abiertos:
        wbf3 = abiertos[n3][0]
        con_iva = set()
        for ws in wbf3.worksheets:
            for row in ws.iter_rows():
                for c in row:
                    if c.comment is not None and 'CON IVA' in c.comment.text:
                        con_iva.add((ws.title, c.coordinate))
        if con_iva:
            for ws in wbf3.worksheets:
                if 'scandallo' not in ws.title:
                    continue
                for row in ws.iter_rows():
                    for c in row:
                        if isinstance(c.value, str) and c.value.startswith('='):
                            for (h, coord) in con_iva:
                                m = re.match(r'([A-Z]+)(\d+)', coord)
                                pat = r"'%s'!\$?%s\$?%s(?!\d)" % (re.escape(h), m.group(1), m.group(2))
                                if re.search(pat, c.value):
                                    problemas.append('libro 3: %s!%s referencia %s!%s, cuya nota dice «CON IVA»'
                                                     % (ws.title, c.coordinate, h, coord))
    # --- libro 7: R-07 (nada de la media cuota del 676) y R-08 (ni art. 8 de la norma de aceites) ----
    n7 = _nombre_libro(D, 7)
    if n7 in abiertos:
        for ws in abiertos[n7][0].worksheets:
            for row in ws.iter_rows():
                for c in row:
                    if c.comment is not None:
                        t = c.comment.text
                        if re.search(r'\bseis\b', t, re.I) or re.search(r'\bmedia\b', t, re.I):
                            problemas.append('libro 7: %s!%s: la nota habla de «seis» o «media» (cuota del 676, R-07)'
                                             % (ws.title, c.coordinate))
                        if RX_ART8.search(t):
                            problemas.append('libro 7: %s!%s: la nota cita el art. 8 de la norma de aceites (R-08)'
                                             % (ws.title, c.coordinate))
    n4 = _nombre_libro(D, 4)
    if n4 in abiertos:
        for ws in abiertos[n4][0].worksheets:
            for row in ws.iter_rows():
                for c in row:
                    if c.comment is not None and RX_ART8.search(c.comment.text):
                        problemas.append('libro 4: %s!%s: la nota cita el art. 8 de la norma de aceites (R-08)'
                                         % (ws.title, c.coordinate))
    # --- R-03: el libro 1 cita E23 del libro 5 y ahí hay un veredicto ----------------
    n1 = _nombre_libro(D, 1)
    if n1 in abiertos and n5 in abiertos:
        texto_b17 = None
        wbv1 = abiertos[n1][1]
        hoja_cuello = D.HOJAS[1][5]            # «Cuello de Botella»
        for row in wbv1[hoja_cuello].iter_rows():
            for c in row:
                if isinstance(c.value, str) and '¿Una churrera o dos?' == c.value.strip():
                    texto_b17 = wbv1[hoja_cuello]['B%d' % c.row].value
        hoja_cap = 'Capacidad contra el Pico'
        v5 = abiertos[n5][1][hoja_cap]['E23'].value if hoja_cap in abiertos[n5][1].sheetnames else None
        if not (isinstance(texto_b17, str) and hoja_cap in texto_b17 and 'E23' in texto_b17):
            problemas.append('R-03: el libro 1 no cita «%s», celda E23 del libro 5 (dice %r)'
                             % (hoja_cap, texto_b17))
        if not (isinstance(v5, str) and (v5.startswith('Una') or v5.startswith('Necesitas'))):
            problemas.append('R-03: %s!E23 del libro 5 no contiene el veredicto (dice %r)' % (hoja_cap, v5))
    return problemas


# ==========================================================================
def main(argv):
    D = _cargar_datos_ejemplo()
    nombres = [os.path.splitext(D.LIBROS[n])[0] for n in sorted(D.LIBROS)]
    todo_ok = True
    abiertos, abiertos_f = {}, {}
    lineas = []

    def out(txt=''):
        lineas.append(txt)
        print(txt)

    out('=' * 82)
    out('GATE FINAL — 8 libros «Cómo Montar una Churrería-Chocolatería» (2026-10-03)')
    out('contrato: %d celdas cruzadas · aristas %s' % (len(D.CRUCES), sorted(D.aristas())))
    out('=' * 82)
    for nombre in nombres:
        ok, detalle, wbf, wbv = auditar_libro(nombre, os.path.join(BUILD, nombre + '.xlsx'), D)
        if wbf is not None:
            abiertos[nombre] = (wbf, wbv)
            abiertos_f[nombre] = wbf
        out('\n[%s] %s' % ('VERDE' if ok else 'ROJO', nombre))
        if wbf is not None:
            n_f = sum(1 for ws in wbf.worksheets for row in ws.iter_rows() for c in row
                      if c.__class__.__name__ != 'MergedCell' and isinstance(c.value, str)
                      and c.value.startswith('='))
            n_v = sum(1 for ws in wbf.worksheets for row in ws.iter_rows() for c in row
                      if c.__class__.__name__ != 'MergedCell' and _es_verde(c))
            sin_cache = sum(1 for ws in wbf.worksheets for row in ws.iter_rows() for c in row
                            if c.__class__.__name__ != 'MergedCell' and isinstance(c.value, str)
                            and c.value.startswith('=') and wbv[ws.title][c.coordinate].value is None)
            out('   fórmulas %d (sin caché %d, «sin dato» a propósito) · verdes %d · hojas %d'
                % (n_f, sin_cache, n_v, len(wbf.worksheets)))
        for linea in detalle:
            out('   - ' + linea)
        todo_ok = todo_ok and ok

    out('\n--- SPEC §2.4: el grafo de cruces ---')
    lin_can, ok_can = probar_canarios(D)
    for l in lin_can:
        out('   ' + l)
    todo_ok = todo_ok and ok_can
    if len(abiertos) == len(nombres):
        pro = auditar_ciclos(D, abiertos_f)
        out('[%s] auditar_ciclos(D): ciclo, orden de relleno, libro 7 y rótulos no declarados'
            % ('VERDE' if not pro else 'ROJO'))
        for l in pro:
            out('   - ' + l)
        todo_ok = todo_ok and not pro
        pro = auditar_cruces(D, abiertos)
        out('[%s] LAS %d CELDAS CRUZADAS (rótulo literal, verde con valor por defecto, origen en K/L, '
            'una fila de CUADRE por celda)' % ('VERDE' if not pro else 'ROJO', len(D.CRUCES)))
        for l in pro[:40]:
            out('   - ' + l)
        todo_ok = todo_ok and not pro
        pro = auditar_fronteras(D, abiertos)
        out('[%s] FRONTERAS: sin fondo de maniobra en el 2, sin gastos fijos ni renta en el 5, escandallo sin '
            '«CON IVA», notas legales del 676 y de la norma de aceites, veredicto «¿una churrera o dos?»'
            % ('VERDE' if not pro else 'ROJO'))
        for l in pro[:40]:
            out('   - ' + l)
        todo_ok = todo_ok and not pro
    else:
        out('[SALTADO] cruces y fronteras: hace falta auditar los 8 libros juntos')
        todo_ok = False

    out('\n' + '=' * 82)
    out('RESULTADO GLOBAL: ' + ('VERDE — 8/8 libros en verde, contrato de %d celdas cruzadas sin ciclos'
                               % len(D.CRUCES) if todo_ok else 'ROJO — hay hallazgos sin corregir'))
    out('=' * 82)
    ruta = os.path.join(BUILD, 'gate-libros-ultima-salida.txt')
    try:
        with open(ruta, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(lineas) + '\n')
    except OSError:
        pass
    return 0 if todo_ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
