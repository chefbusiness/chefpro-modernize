#!/usr/bin/env python3
"""Plantilla de ficha técnica de cocina GRATIS (lead magnet de /blog/ficha-tecnica-de-cocina).

Una hoja con el ejemplo del post (Salmón a la plancha con verduras salteadas, el mismo plato del
escandallo): datos generales, ingredientes con merma y cantidad bruta calculada (redondeada al gramo
hacia arriba), elaboración con tiempo y temperatura, los 14 alérgenos del Reglamento (UE) 1169/2011
con desplegable, conservación, emplatado y el bloque de coste → PVP.

Uso:  python3 scripts/contenidos/plantilla-ficha-tecnica-gratis.py
Sale: astro-site/public/descargas/plantilla-ficha-tecnica-cocina-gratis-aichef.xlsx
El script inyecta los valores calculados (inject_cache.py) y comprueba las celdas con data_only.
Después: python3 scripts/productos-digitales/parche_xml_xlsx.py --check <xlsx>
"""
import subprocess
import sys
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / 'astro-site/public/descargas/plantilla-ficha-tecnica-cocina-gratis-aichef.xlsx'
GUIA = 'https://aichef.pro/blog/ficha-tecnica-de-cocina'
ESCANDALLO = 'https://aichef.pro/descargas/plantilla-escandallo-gratis-aichef.xlsx'

NEGRO, DORADO, GRIS = '111111', 'FFD700', 'F3F3F3'
fino = Side(style='thin', color='BBBBBB')
borde = Border(left=fino, right=fino, top=fino, bottom=fino)
entrada = PatternFill('solid', fgColor='FFF8D6')
EUR = '#,##0.00 "€"'

# (ingrediente, neto, unidad, merma) — los del post y del escandallo.
INGREDIENTES = [
    ('Lomo de salmón fresco', 180, 'g', 0.18),
    ('Calabacín', 80, 'g', 0.10),
    ('Pimiento rojo', 60, 'g', 0.20),
    ('Cebolla morada', 40, 'g', 0.12),
    ('Ajo', 5, 'g', 0.10),
    ('AOVE', 15, 'ml', 0.0),
    ('Limón', 30, 'g', 0.0),
    ('Sal, pimienta y perejil', None, 'al gusto', None),
]
PASOS = [
    ('Cortar el calabacín y el pimiento en bastones regulares y la cebolla morada en juliana fina.', '5 min', ''),
    ('Saltear las verduras con el ajo laminado y parte del AOVE a fuego fuerte, sin que pierdan el color.', '4 min', 'fuego fuerte'),
    ('Marcar el salmón por el lado de la piel en la plancha bien caliente y terminar por el otro lado.', '6 min', 'plancha bien caliente'),
    ('Retirar y dejar reposar un minuto antes de emplatar.', '1 min', ''),
    ('Emplatar las verduras de base, el salmón encima con la piel hacia arriba, el limón y el perejil.', '2 min', ''),
]
ALERGENOS = ['Cereales con gluten', 'Crustáceos', 'Huevos', 'Pescado', 'Cacahuetes', 'Soja', 'Leche',
             'Frutos de cáscara', 'Apio', 'Mostaza', 'Granos de sésamo', 'Dióxido de azufre y sulfitos',
             'Altramuces', 'Moluscos']
assert len(ALERGENOS) == 14


def titulo(ws, fila, texto):
    c = ws.cell(row=fila, column=1, value=texto)
    c.font = Font(bold=True, color='FFFFFF')
    c.fill = PatternFill('solid', fgColor=NEGRO)
    ws.merge_cells(start_row=fila, start_column=1, end_row=fila, end_column=6)


def celda(ws, fila, col, valor=None, fmt=None, es_entrada=False, negrita=False):
    c = ws.cell(row=fila, column=col, value=valor)
    c.border = borde
    if fmt:
        c.number_format = fmt
    if es_entrada:
        c.fill = entrada
    if negrita:
        c.font = Font(bold=True)
    c.alignment = Alignment(wrap_text=True, vertical='top')
    return c


def main():
    wb = Workbook()
    ws = wb.active
    ws.title = 'Ficha técnica'
    ws['A1'] = 'Ficha técnica de cocina'
    ws['A1'].font = Font(bold=True, size=16, color=DORADO)
    ws['A1'].fill = PatternFill('solid', fgColor=NEGRO)
    ws.merge_cells('A1:F1')
    ws['A2'] = 'Rellena las celdas amarillas. La cantidad bruta y el precio se calculan solos.'
    ws['A2'].font = Font(italic=True, color='555555')
    ws.merge_cells('A2:F2')

    # Datos generales (filas 4-10)
    titulo(ws, 4, 'Datos generales')
    datos = [('Plato', 'Salmón a la plancha con verduras salteadas'), ('Categoría', 'Pescados'), ('Raciones', 1),
             ('Tiempo de preparación', '20 min'), ('Autor', ''), ('Fecha y versión', 'v1.0')]
    for i, (k, v) in enumerate(datos):
        f = 5 + i
        celda(ws, f, 1, k, negrita=True)
        celda(ws, f, 2, v, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=2, end_row=f, end_column=6)

    # Ingredientes (cabecera fila 12, datos 13-24)
    titulo(ws, 12, 'Ingredientes (por ración)')
    cab = ['Ingrediente', 'Cantidad neta (en plato)', 'Unidad', 'Merma (%)', 'Cantidad bruta (a comprar)', 'Alérgenos que aporta']
    for col, txt in enumerate(cab, start=1):
        c = celda(ws, 13, col, txt, negrita=True)
        c.fill = PatternFill('solid', fgColor=GRIS)
    primera = 14
    filas = INGREDIENTES + [None] * 4
    for i, item in enumerate(filas):
        f = primera + i
        if item:
            n, neto, ud, merma = item
            celda(ws, f, 1, n, es_entrada=True)
            celda(ws, f, 2, neto, '0', es_entrada=True)
            celda(ws, f, 3, ud, es_entrada=True)
            celda(ws, f, 4, merma, '0%', es_entrada=True)
            celda(ws, f, 6, 'Pescado' if n.startswith('Lomo de salmón') else '', es_entrada=True)
        else:
            for col in (1, 2, 3, 4, 6):
                celda(ws, f, col, None, '0%' if col == 4 else ('0' if col == 2 else None), es_entrada=True)
        # bruta = neta / (1 − merma), redondeada al gramo hacia arriba
        celda(ws, f, 5, f'=IF(OR(B{f}="",D{f}=""),"",ROUNDUP(B{f}/(1-D{f}),0))', '0')
    ultima_ing = primera + len(filas) - 1

    # Elaboración (cabecera, datos)
    fe = ultima_ing + 2
    titulo(ws, fe, 'Elaboración paso a paso')
    for col, txt in enumerate(['Paso', 'Qué se hace', '', '', 'Tiempo', 'Temperatura / punto'], start=1):
        if txt:
            c = celda(ws, fe + 1, col, txt, negrita=True)
            c.fill = PatternFill('solid', fgColor=GRIS)
    ws.merge_cells(start_row=fe + 1, start_column=2, end_row=fe + 1, end_column=4)
    pasos = PASOS + [('', '', '')] * 3
    for i, (txt, tiempo, temp) in enumerate(pasos):
        f = fe + 2 + i
        celda(ws, f, 1, i + 1)
        celda(ws, f, 2, txt or None, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=2, end_row=f, end_column=4)
        celda(ws, f, 5, tiempo or None, es_entrada=True)
        celda(ws, f, 6, temp or None, es_entrada=True)
        ws.row_dimensions[f].height = 32

    # Alérgenos (14, con desplegable)
    fa = fe + 2 + len(pasos) + 1
    titulo(ws, fa, 'Alérgenos (Reglamento UE 1169/2011)')
    dv = DataValidation(type='list', formula1='"Contiene,Puede contener trazas,No contiene"', allow_blank=True)
    ws.add_data_validation(dv)
    for i, a in enumerate(ALERGENOS):
        f = fa + 1 + i
        celda(ws, f, 1, a)
        c = celda(ws, f, 2, 'Contiene' if a == 'Pescado' else 'No contiene', es_entrada=True)
        dv.add(c.coordinate)

    # Conservación y emplatado
    fc = fa + 1 + len(ALERGENOS) + 1
    titulo(ws, fc, 'Conservación y puntos críticos')
    for i, (k, v) in enumerate([('Conservación', 'Salmón refrigerado hasta marcar; verdura cortada tapada y refrigerada.'),
                                ('Puntos críticos (según tu plan APPCC)', 'Cadena de frío del pescado; cocción del salmón.'),
                                ('Vida útil de elaboraciones previas', 'La que fije tu plan APPCC.')]):
        f = fc + 1 + i
        celda(ws, f, 1, k, negrita=True)
        celda(ws, f, 2, v, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=2, end_row=f, end_column=6)
    fm = fc + 5
    titulo(ws, fm, 'Emplatado')
    for i, (k, v) in enumerate([('Montaje', 'Verduras de base, salmón encima con la piel hacia arriba, limón y perejil.'),
                                ('Menaje', 'Plato llano.'), ('Foto de referencia', 'Pega aquí la foto del plato terminado.')]):
        f = fm + 1 + i
        celda(ws, f, 1, k, negrita=True)
        celda(ws, f, 2, v, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=2, end_row=f, end_column=6)

    # Coste → PVP
    fp = fm + 5
    titulo(ws, fp, 'Coste y precio (del escandallo)')
    b = fp + 1
    bloque = [
        ('Coste por ración (del escandallo)', 4.29, EUR, True),
        ('Food cost objetivo', 0.30, '0%', True),
        ('PVP sin IVA', f'=B{b}/B{b + 1}', EUR, False),
        ('IVA (restauración en España: 10 %)', 0.10, '0%', True),
        ('PVP con IVA', f'=B{b + 2}*(1+B{b + 3})', EUR, False),
        ('Precio de carta (redondeado por ti)', 15.90, EUR, True),
        ('Food cost real con ese precio', f'=B{b}/(B{b + 5}/(1+B{b + 3}))', '0.0%', False),
    ]
    for i, (k, v, fmt, ent) in enumerate(bloque):
        celda(ws, b + i, 1, k, negrita=True)
        c = celda(ws, b + i, 2, v, fmt, es_entrada=ent, negrita=True)
        if not ent:
            c.fill = PatternFill('solid', fgColor=GRIS)
    fn = b + len(bloque) + 1
    ws.cell(row=fn, column=1, value='Guía con el ejemplo explicado:')
    ws.cell(row=fn, column=2, value=GUIA).hyperlink = GUIA
    ws.cell(row=fn + 1, column=1, value='Plantilla de escandallo gratis (el coste):')
    ws.cell(row=fn + 1, column=2, value=ESCANDALLO).hyperlink = ESCANDALLO
    for f in (fn, fn + 1):
        ws.cell(row=f, column=2).font = Font(color='0563C1', underline='single')

    for col, w in {'A': 34, 'B': 16, 'C': 10, 'D': 11, 'E': 16, 'F': 24}.items():
        ws.column_dimensions[col].width = w

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    wb.save(SALIDA)
    subprocess.run([sys.executable, str(RAIZ / 'scripts/productos-digitales/inject_cache.py'), str(SALIDA)],
                   check=True, stdout=subprocess.DEVNULL)
    wv = load_workbook(SALIDA, data_only=True)['Ficha técnica']
    brutos = [wv.cell(row=primera + i, column=5).value for i in range(7)]
    assert [int(x) for x in brutos] == [220, 89, 75, 46, 6, 15, 30], brutos
    assert round(float(wv.cell(row=b + 2, column=2).value), 2) == 14.30
    assert round(float(wv.cell(row=b + 4, column=2).value), 2) == 15.73
    assert round(float(wv.cell(row=b + 6, column=2).value) * 100, 1) == 29.7
    print(f'OK {SALIDA.relative_to(RAIZ)} · brutos {brutos} · PVP 14,30 · con IVA 15,73 · FC real 29,7 %')


if __name__ == '__main__':
    main()
