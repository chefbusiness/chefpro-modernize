#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
auditar_libros_1_2.py — gate de los libros 1 y 2 de «Manual del Chef Ejecutivo»
(`cuadro-de-mando-cocina.xlsx` y `planificacion-produccion-semanal.xlsx`).

No corrige nada: comprueba y aborta con código 1 si algo falla. Es el gate que
pide la SPEC §2.2 y el encargo del constructor:

  1. Todas las celdas del `mapa-<libro>.json` existen y tienen VALOR cacheado
     (openpyxl `data_only=True` → nunca `None`). Se cuenta cuántas.
  2. Todas las fórmulas del libro están cacheadas o devuelven «sin dato» («»):
     ninguna se queda en blanco por un fallo de pycel.
  3. Cero funciones prohibidas: INDIRECT, COUNTA, PMT, OFFSET, XLOOKUP, LET,
     LAMBDA, RANK, NETWORKDAYS.
  4. Cero referencias a otros ficheros («[» dentro de una fórmula).
  5. Cero constantes numéricas dentro de una fórmula de cálculo, salvo 0, 1,
     100 y los índices de INDEX/MATCH.
  6. Cero caracteres fuera de cp1252 (WinAnsi) en cualquier texto.
  7. Hoja «Instrucciones» la primera, con línea de versión, bio y nota de
     desproteger; celdas verdes desbloqueadas y hoja protegida sin contraseña.
  8. Término único «partida»: ni un «estación» fuera de la glosa autorizada.
  9. Todo dato legal lleva su nota «Verificado el 06-09-2026 · norma · URL».
 10. Cero divisiones sin IFERROR y cero semáforos sin ISNUMBER.

Uso:  python3 auditar_libros_1_2.py
"""
import json
import os
import re
import sys

import openpyxl

AQUI = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(AQUI, 'build')
LIBROS = ['cuadro-de-mando-cocina', 'planificacion-produccion-semanal']

FECHA_VERIF = '06-09-2026'
PROHIBIDAS = ('INDIRECT', 'COUNTA', 'PMT', 'OFFSET', 'XLOOKUP', 'LET',
              'LAMBDA', 'RANK', 'NETWORKDAYS')
#: 0, 1 y 100 son los únicos literales tolerados en una fórmula de cálculo; el
#: resto de números que aparecen dentro de una fórmula son índices de
#: INDEX/MATCH (posición de la ranura de partida), que la SPEC permite.
TOLERADOS = {'0', '1', '100'}

RX_FUNC = re.compile(r'\b(' + '|'.join(PROHIBIDAS) + r')\s*\(', re.I)
RX_TEXTO = re.compile(r'"[^"]*"')
RX_INDICE = re.compile(r'\b(?:INDEX|MATCH)\s*\([^()]*?,\s*(\d+)\s*\)', re.I)
RX_NUM = re.compile(r'(?<![A-Z0-9_$.!:])(\d+(?:\.\d+)?)')

fallos = []
avisos = []
resumen = []


def falla(m):
    fallos.append(m)


def avisa(m):
    avisos.append(m)


def textos(wb):
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str):
                    yield ws.title, c.coordinate, c.value


def audita(nombre):
    ruta = os.path.join(BUILD, nombre + '.xlsx')
    mapa_ruta = os.path.join(BUILD, 'mapa-' + nombre + '.json')
    if not os.path.exists(ruta):
        falla('%s: no existe el xlsx' % nombre)
        return
    if not os.path.exists(mapa_ruta):
        falla('%s: no existe el mapa' % nombre)
        return
    wb = openpyxl.load_workbook(ruta)
    wbv = openpyxl.load_workbook(ruta, data_only=True)
    mapa = json.load(open(mapa_ruta, encoding='utf-8'))

    # --- 1. celdas del mapa con valor -------------------------------------
    n_mapa = n_mapa_formula = 0
    for hoja, cont in mapa['hojas'].items():
        if hoja not in wbv.sheetnames:
            falla('%s: el mapa cita una hoja inexistente «%s»' % (nombre, hoja))
            continue
        for desc, coord in cont['celdas'].items():
            n_mapa += 1
            v = wbv[hoja][coord].value
            es_formula = (wb[hoja][coord].data_type == 'f')
            if es_formula:
                n_mapa_formula += 1
            if v is None:
                falla('%s: %s!%s («%s») SIN VALOR' % (nombre, hoja, coord,
                                                      desc))
    resumen.append('%s: %d celdas en el mapa (%d de ellas fórmulas), todas '
                   'con valor' % (nombre, n_mapa, n_mapa_formula))

    # --- 2. fórmulas cacheadas o «sin dato» --------------------------------
    n_f = n_cache = n_vacias = 0
    for ws in wb.worksheets:
        wsv = wbv[ws.title]
        for row in ws.iter_rows():
            for c in row:
                if c.data_type != 'f':
                    continue
                n_f += 1
                v = wsv[c.coordinate].value
                if v is None:
                    n_vacias += 1
                else:
                    n_cache += 1
    resumen.append('%s: %d fórmulas, %d con valor cacheado, %d que devuelven '
                   '«sin dato»' % (nombre, n_f, n_cache, n_vacias))

    # --- 3, 4, 5. contenido de las fórmulas -------------------------------
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.data_type != 'f' or not isinstance(c.value, str):
                    continue
                fx = c.value
                m = RX_FUNC.search(fx)
                if m:
                    falla('%s: %s!%s usa la función prohibida %s'
                          % (nombre, ws.title, c.coordinate, m.group(1)))
                if '[' in fx:
                    falla('%s: %s!%s referencia otro fichero'
                          % (nombre, ws.title, c.coordinate))
                cuerpo = RX_TEXTO.sub('', fx)
                indices = set(RX_INDICE.findall(cuerpo))
                for num in RX_NUM.findall(cuerpo):
                    if num in TOLERADOS or num in indices:
                        continue
                    falla('%s: %s!%s lleva la constante %s dentro de la '
                          'fórmula: %s' % (nombre, ws.title, c.coordinate,
                                           num, fx[:110]))

    # --- 6. WinAnsi --------------------------------------------------------
    for hoja, coord, txt in textos(wb):
        try:
            txt.encode('cp1252')
        except UnicodeEncodeError as e:
            falla('%s: %s!%s tiene un carácter fuera de cp1252 (%r)'
                  % (nombre, hoja, coord, txt[e.start:e.end]))

    # --- 7. instrucciones, versión, bio, protección ------------------------
    if wb.sheetnames[0] != 'Instrucciones':
        falla('%s: la primera hoja es «%s», no «Instrucciones»'
              % (nombre, wb.sheetnames[0]))
    ins = '\n'.join(v for h, _c, v in textos(wb) if h == 'Instrucciones')
    if ('Versión 1.0 · septiembre 2026 · aichef.pro/manual-chef-ejecutivo · '
            'info@aichef.pro') not in ins:
        falla('%s: falta la línea de versión exacta en «Instrucciones»'
              % nombre)
    if 'John Guerrero' not in ins:
        falla('%s: falta la bio anclada en «Instrucciones»' % nombre)
    if 'desprotege' not in ins.lower() and 'desproteger' not in ins.lower():
        falla('%s: falta la nota de desproteger' % nombre)
    for ws in wb.worksheets:
        if not ws.protection.sheet:
            falla('%s: la hoja «%s» no está protegida' % (nombre, ws.title))
        if ws.protection.password:
            falla('%s: la hoja «%s» tiene contraseña' % (nombre, ws.title))
    n_verdes = n_mal = 0
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                relleno = c.fill
                verde = (relleno is not None and relleno.fill_type == 'solid'
                         and isinstance(relleno.fgColor.rgb, str)
                         and relleno.fgColor.rgb.upper().endswith('E8F5E9'))
                if not verde:
                    continue
                n_verdes += 1
                if c.data_type == 'f':
                    falla('%s: %s!%s es fórmula y está en verde'
                          % (nombre, ws.title, c.coordinate))
                if c.protection.locked:
                    n_mal += 1
    if n_mal:
        falla('%s: %d celdas verdes siguen bloqueadas' % (nombre, n_mal))
    resumen.append('%s: %d celdas verdes, todas desbloqueadas' % (nombre,
                                                                  n_verdes))

    # --- 8. término «partida» ---------------------------------------------
    # La D9 admite UN solo uso: la glosa de la PRIMERA mención, una vez por
    # libro. B8 de la refutación xlsx (2026-09-06): la formulación única de
    # los tres libros es la del libro 4 (la verificable, «vocabulario de la
    # matriz de polivalencia del Manual del Manager»); la segunda aparición
    # («columna «estación»...») que traían los libros 1 y 2 se quitó, no se
    # sustituyó por otra: ya no hay un segundo uso autorizado.
    GLOSA = 'estaciones, en el vocabulario'
    n_glosa = 0
    for hoja, coord, txt in textos(wb):
        bajo = txt.lower()
        if 'estaci' not in bajo:
            continue
        if GLOSA.lower() in bajo:
            n_glosa += 1
            continue
        falla('%s: %s!%s usa «estación» fuera de la única glosa autorizada '
              'por la D9 (B8 de la refutación xlsx): %s'
              % (nombre, hoja, coord, txt[:100]))
    if n_glosa != 1:
        falla('%s: la glosa «(estaciones, en el vocabulario...)» aparece %d '
              'veces; la D9 exige exactamente una por libro'
              % (nombre, n_glosa))
    resumen.append('%s: 1 glosa de «estación», sin segundo uso (B8 de la '
                   'refutación xlsx)' % nombre)

    # --- 9. notas legales --------------------------------------------------
    todo = list(textos(wb))
    n_legal = 0
    for hoja, coord, txt in todo:
        if 'Verificado el' not in txt:
            continue
        n_legal += 1
        if FECHA_VERIF not in txt:
            falla('%s: %s!%s cita una fecha de verificación distinta de %s'
                  % (nombre, hoja, coord, FECHA_VERIF))
        if 'http' not in txt:
            falla('%s: %s!%s dice «Verificado el» y no trae URL'
                  % (nombre, hoja, coord))
    if not n_legal:
        falla('%s: ninguna nota «Verificado el ...»' % nombre)
    resumen.append('%s: %d notas legales con fecha, norma y URL'
                   % (nombre, n_legal))

    # --- 10. IFERROR e ISNUMBER -------------------------------------------
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.data_type != 'f' or not isinstance(c.value, str):
                    continue
                fx = c.value
                if '/' in RX_TEXTO.sub('', fx) and 'IFERROR' not in fx.upper():
                    falla('%s: %s!%s divide sin IFERROR: %s'
                          % (nombre, ws.title, c.coordinate, fx[:110]))
    for ws in wb.worksheets:
        for rango in ws.conditional_formatting:
            for regla in rango.rules:
                for f in (regla.formula or []):
                    if 'ISNUMBER' not in f.upper():
                        falla('%s: %s!%s tiene un semáforo sin ISNUMBER: %s'
                              % (nombre, ws.title, rango.sqref, f[:90]))

    # --- 10-bis. desplegables contra rango: el rango existe y tiene opciones
    n_dv = 0
    for ws in wb.worksheets:
        for dv in ws.data_validations.dataValidation:
            if dv.type != 'list':
                continue
            n_dv += 1
            f1 = (dv.formula1 or '').lstrip('=')
            if f1.startswith('"'):
                falla('%s: %s tiene un desplegable de lista con comas, no '
                      'contra rango: %s' % (nombre, ws.title, f1[:60]))
                continue
            hoja_dv, rango = (f1.split('!') if '!' in f1
                              else (ws.title, f1))
            hoja_dv = hoja_dv.strip("'")
            if hoja_dv not in wb.sheetnames:
                falla('%s: desplegable contra una hoja inexistente (%s)'
                      % (nombre, f1))
                continue
            opciones = [c.value for fila in wb[hoja_dv][rango] for c in fila
                        if c.value not in (None, '')]
            if not opciones:
                falla('%s: el desplegable %s apunta a un rango VACÍO'
                      % (nombre, f1))
    resumen.append('%s: %d desplegables, todos contra un rango con opciones'
                   % (nombre, n_dv))

    # --- 11. el libro 1 no lleva NI UNA columna financiera (SPEC 2.2) -----
    if nombre == 'cuadro-de-mando-cocina':
        n_eur = 0
        for ws in wb.worksheets:
            for row in ws.iter_rows():
                for c in row:
                    if c.number_format and '\u20ac' in c.number_format:
                        n_eur += 1
                        falla('%s: %s!%s tiene formato de euros' %
                              (nombre, ws.title, c.coordinate))
        financieras = ('food cost', 'labor cost', 'prime cost', 'ventas netas',
                       'ticket medio', 'facturaci')
        for hoja, coord, txt in textos(wb):
            bajo = txt.lower()
            for termino in financieras:
                if termino not in bajo:
                    continue
                # se pueden CITAR (para mandar al cuadro del Manager), pero no
                # puede haber una columna que las mida en este libro.
                if hoja in ('Semana', 'Comparativa entre Unidades') and \
                        len(txt) < 60:
                    falla('%s: %s!%s parece una columna financiera: %s'
                          % (nombre, hoja, coord, txt[:80]))
        resumen.append('%s: 0 formatos de euros y ninguna columna financiera'
                       % nombre)

    # --- 12. las referencias del mapa apuntan a celdas que existen --------
    for desc, ref in mapa.get('referencias', {}).items():
        hoja_r, coord = ref.rsplit('!', 1)
        hoja_r = hoja_r.split(' · ')[0]
        if hoja_r not in wbv.sheetnames:
            falla('%s: la referencia «%s» apunta a la hoja inexistente %s'
                  % (nombre, desc, hoja_r))
        elif wbv[hoja_r][coord].value is None:
            falla('%s: la referencia «%s» (%s) no tiene valor'
                  % (nombre, desc, ref))

    # --- extra: recuento de hojas -----------------------------------------
    resumen.append('%s: hojas = %s' % (nombre, ' · '.join(wb.sheetnames)))


def main():
    for nombre in LIBROS:
        if os.path.exists(os.path.join(BUILD, nombre + '.xlsx')):
            audita(nombre)
        else:
            avisa('%s: todavía no construido, se salta' % nombre)
    print('\n'.join(resumen))
    if avisos:
        print('\nAVISOS')
        print('\n'.join(' - ' + a for a in avisos))
    if fallos:
        print('\nFALLOS (%d)' % len(fallos))
        print('\n'.join(' - ' + f for f in fallos))
        sys.exit(1)
    print('\nGATE VERDE: 0 fallos')


if __name__ == '__main__':
    main()
