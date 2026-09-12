#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gates de `documentos.es_fila_porcentual()` y del reformateo de filas (2026-09-10).

Contexto (hallazgo A1 de `auditorias/guia-pasteleria-docs-refutacion-2026-09-10.md`):
la guarda que se añadió el 2026-08-29 para que una fila etiquetada «(%)» no se
imprimiera con el formato de su columna miraba las DOS primeras celdas con el patrón
`%\\s*$`, que casa con cualquier texto acabado en «%». La referencia T1 de la carta de
la Guía de Pastelería se llama «Tarta de chocolate 70 %», así que las tres tablas que
la contienen se reformateaban ENTERAS como porcentajes: en el cap. 17 la temperatura
legal de conservación salía impresa «4,0 %» donde son 4 °C y el plazo del art. 9.3
salía «24,0 %» donde son 24 horas. Ni un aviso, el gate `coherencia_cifras` en verde y
el defecto vivo en la página 83 del PDF que se vende.

Regla que se fija aquí: una celda cuenta como porcentual si su ETIQUETA declara el
porcentaje («(%)», «en %», «(porcentaje)») o si la celda ENTERA es un número seguido
de «%». Una cadena con letras, nunca.

Uso: /usr/local/bin/python3 scripts/productos-digitales/tests/test_fila_porcentual.py
Sin pytest a propósito (el pipeline de productos no lo tiene): exit 0 = verde,
exit 1 = algún gate rojo. No escribe nada dentro del repo.
"""
import importlib.util
import os
import sys
import tempfile

REPO = '/Users/johnguerrero/chefpro-modernize'
PD = os.path.join(REPO, 'scripts', 'productos-digitales')

spec = importlib.util.spec_from_file_location(
    'd', os.path.join(PD, 'guias-v2_0', 'documentos.py'))
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)

FALLOS = []


def check(gate, cond, detalle=''):
    print(f'  [{"OK  " if cond else "FALLO"}] {gate}' +
          (f' — {detalle}' if detalle else ''))
    if not cond:
        FALLOS.append(gate)


# --------------------------------------------------------------------------
def gate_a():
    """es_fila_porcentual(): qué SÍ y qué NO declara una fila de porcentajes."""
    print('\ngate a · es_fila_porcentual, caso a caso')
    si = [
        (['Margen EBITDA (%)', 0.12], 'etiqueta con «(%)»'),
        (['Peso de cada canal en %', 0.78], 'etiqueta con «en %»'),
        (['Ocupación (porcentaje)', 0.5], 'etiqueta con «(porcentaje)»'),
        (['Cuota', '35,2 %'], 'la celda ES un porcentaje entero'),
        (['Cuota', '-4%'], 'porcentaje negativo y sin espacio'),
        (['Cuota', ' 12.5 % '], 'porcentaje con espacios y punto decimal'),
    ]
    for celdas, por_que in si:
        check(f'a: SÍ es porcentual ({por_que})', d.es_fila_porcentual(celdas),
              repr(celdas))
    no = [
        (['T1', 'Tarta de chocolate 70 %'], 'EL CASO A1: nombre de producto'),
        (['Cacao mínimo 70 %', 'No'], 'nombre en la primera celda'),
        (['Chocolate al 70 % de cacao', 4], 'porcentaje en mitad de la frase'),
        (['Referencia', 'Napolitana de crema'], 'texto normal'),
        (['Plazo legal en horas', 24], 'nada que declare porcentaje'),
    ]
    for celdas, por_que in no:
        check(f'a: NO es porcentual ({por_que})',
              not d.es_fila_porcentual(celdas), repr(celdas))


# --------------------------------------------------------------------------
def _libro_de_prueba(ruta):
    """Tres filas reales del cap. 17 de la Guía de Pastelería: la de la tarta
    (la que rompía), una fila hermana que siempre salió bien y una fila que SÍ
    es de porcentajes y tiene que seguir reformateándose."""
    import openpyxl
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Hoja'
    filas = [
        ['T1', 'Tarta de chocolate 70 %', 'No', 4, 24, 'Vitrina refrigerada'],
        ['PI2', 'Napolitana de crema', 'No', 4, 24, 'Vitrina refrigerada'],
        ['B1', 'Croissant de mantequilla', 'Sí', None, None, 'Ambiente'],
        ['R1', 'Peso de cada familia (%)', 0.352, 0.24, 0.12, 'calculado'],
    ]
    for i, f in enumerate(filas, start=6):
        for j, v in enumerate(f):
            ws.cell(row=i, column=j + 1, value=v)
    wb.save(ruta)


def gate_b():
    """construir_tabla(): la fila de la tarta se imprime con SUS unidades."""
    print('\ngate b · construir_tabla sobre las filas reales del cap. 17')
    tmp = tempfile.mkdtemp(prefix='test-fila-pct-')
    _libro_de_prueba(os.path.join(tmp, 'libro.xlsx'))
    t = {
        'src': ('libro.xlsx', 'Hoja'),
        'cols': [('Ref', 'A', 'txt'), ('Referencia', 'B', 'txt'),
                 ('¿Estable a temperatura ambiente?', 'C', 'txt'),
                 ('Temperatura de conservación (grados)', 'D', 'num'),
                 ('Plazo legal en horas', 'E', 'num'),
                 ('Dónde va en el mostrador', 'F', 'txt')],
        'filas': (6, 9),
    }
    md, n = d.construir_tabla(tmp, t)
    print(md)
    lineas = md.splitlines()
    tarta = [l for l in lineas if 'Tarta de chocolate' in l][0]
    napo = [l for l in lineas if 'Napolitana' in l][0]
    pesos = [l for l in lineas if 'Peso de cada familia' in l][0]

    check('b: la tarta imprime «4» de temperatura, no «4,0 %»',
          '| 4 |' in tarta and '%' not in tarta.split('|', 3)[3], tarta)
    check('b: la tarta imprime «24» de plazo, no «24,0 %»',
          '| 24 |' in tarta, tarta)
    check('b: la napolitana (fila hermana) no ha cambiado',
          '| 4 |' in napo and '| 24 |' in napo, napo)
    check('b: una fila que SÍ declara «(%)» se sigue reformateando',
          '35,2' in pesos and '%' in pesos, pesos)
    check('b: se construyen las cuatro filas', n == 4, f'n={n}')

    # omitir_filas (B12): la tabla del P&L saca de la resta las dos filas de
    # IVA soportado sin perder el resto del rango.
    t2 = dict(t, omitir_filas=(7,))
    md2, n2 = d.construir_tabla(tmp, t2)
    check('b: omitir_filas quita exactamente la fila pedida',
          n2 == 3 and 'Napolitana' not in md2 and 'Tarta de chocolate' in md2,
          f'n={n2}')


if __name__ == '__main__':
    for g in (gate_a, gate_b):
        g()
    print('\n' + '=' * 70)
    if FALLOS:
        print(f'ROJO — {len(FALLOS)} comprobaciones fallidas:')
        for f in FALLOS:
            print(' -', f)
        sys.exit(1)
    print('VERDE — es_fila_porcentual y construir_tabla pasan todos los gates.')
