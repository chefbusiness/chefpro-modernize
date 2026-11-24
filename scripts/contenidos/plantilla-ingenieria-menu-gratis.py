#!/usr/bin/env python3
"""Plantilla de ingeniería de menú GRATIS (lead magnet de /blog/carta-restaurante-rentable-ingenieria-menu-ia).

Matriz de rentabilidad y popularidad con el ejemplo de 8 platos del post, 22 filas libres y la
clasificación automática (Estrella, Caballo, Puzzle, Perro). Umbrales:
- Rentabilidad: margen de contribución medio PONDERADO por las ventas (total de margen ÷ total de unidades).
- Popularidad: a elegir en un desplegable, la media de unidades por plato o la regla del 70 % (0,7 × media).

Uso:  python3 scripts/contenidos/plantilla-ingenieria-menu-gratis.py
Sale: astro-site/public/descargas/plantilla-ingenieria-menu-gratis-aichef.xlsx
Inyecta los valores calculados (inject_cache.py) y comprueba las celdas con data_only.
Después: python3 scripts/productos-digitales/parche_xml_xlsx.py --check <xlsx>
"""
import subprocess
import sys
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / 'astro-site/public/descargas/plantilla-ingenieria-menu-gratis-aichef.xlsx'
GUIA = 'https://aichef.pro/blog/carta-restaurante-rentable-ingenieria-menu-ia'
ESCANDALLO = 'https://aichef.pro/descargas/plantilla-escandallo-gratis-aichef.xlsx'

# (plato, precio sin IVA, coste, unidades/mes, clasificación esperada) — los del post.
PLATOS = [
    ('Ensalada de burrata y tomate raff', 12.50, 3.10, 200, 'Estrella'),
    ('Tataki de atún rojo con sésamo', 18.00, 5.40, 180, 'Estrella'),
    ('Croquetas caseras de jamón', 9.50, 2.80, 320, 'Caballo'),
    ('Pasta boloñesa de la casa', 11.00, 4.40, 210, 'Caballo'),
    ('Carrillera al vino tinto con puré trufado', 17.00, 5.90, 85, 'Puzzle'),
    ('Bacalao confitado con pilpil suave', 19.50, 7.80, 90, 'Puzzle'),
    ('Nuggets de pollo con patatas (menú infantil)', 8.00, 3.20, 55, 'Perro'),
    ('Tarta de queso al horno', 7.50, 2.60, 60, 'Perro'),
]
LIBRES = 22
NEGRO, DORADO, GRIS = '111111', 'FFD700', 'F3F3F3'
EUR = '#,##0.00 "€"'
fino = Side(style='thin', color='BBBBBB')
borde = Border(left=fino, right=fino, top=fino, bottom=fino)
entrada = PatternFill('solid', fgColor='FFF8D6')


def main():
    wb = Workbook()
    ws = wb.active
    ws.title = 'Ingeniería de menú'
    ws['A1'] = 'Ingeniería de menú: matriz de rentabilidad y popularidad'
    ws['A1'].font = Font(bold=True, size=16, color=DORADO)
    ws['A1'].fill = PatternFill('solid', fgColor=NEGRO)
    ws.merge_cells('A1:I1')
    ws['A2'] = 'Rellena las celdas amarillas con los datos de un mes (precios sin IVA). La clasificación sale sola.'
    ws['A2'].font = Font(italic=True, color='555555')
    ws.merge_cells('A2:I2')

    cab = ['Plato', 'Precio sin IVA', 'Coste (escandallo)', 'Margen €', 'Margen %', 'Unidades/mes',
           'Margen total €', 'Peso en ventas %', 'Clasificación']
    ft = 4
    for col, txt in enumerate(cab, start=1):
        c = ws.cell(row=ft, column=col, value=txt)
        c.font = Font(bold=True, color='FFFFFF')
        c.fill = PatternFill('solid', fgColor=NEGRO)
        c.alignment = Alignment(wrap_text=True, horizontal='center', vertical='center')
        c.border = borde
    ws.row_dimensions[ft].height = 32
    p1 = ft + 1
    pn = p1 + len(PLATOS) + LIBRES - 1
    # Bloque de umbrales (columna K-L)
    U_MARGEN, U_POP, METODO, MEDIA_UDS = '$L$5', '$L$8', '$L$6', '$L$7'
    filas = PLATOS + [None] * LIBRES
    for i, item in enumerate(filas):
        r = p1 + i
        if item:
            n, pv, co, ud, _ = item
            vals = {1: n, 2: pv, 3: co, 6: ud}
        else:
            vals = {}
        for col in (1, 2, 3, 6):
            c = ws.cell(row=r, column=col, value=vals.get(col))
            c.fill = entrada
        ws.cell(row=r, column=4, value=f'=IF(OR(B{r}="",C{r}=""),"",B{r}-C{r})')
        ws.cell(row=r, column=5, value=f'=IF(OR(B{r}="",C{r}=""),"",(B{r}-C{r})/B{r})')
        ws.cell(row=r, column=7, value=f'=IF(OR(D{r}="",F{r}=""),"",D{r}*F{r})')
        ws.cell(row=r, column=8, value=f'=IF(F{r}="","",F{r}/SUM($F${p1}:$F${pn}))')
        ws.cell(row=r, column=9, value=(f'=IF(OR(D{r}="",F{r}=""),"",IF(AND(D{r}>={U_MARGEN},F{r}>={U_POP}),"Estrella",'
                                        f'IF(F{r}>={U_POP},"Caballo",IF(D{r}>={U_MARGEN},"Puzzle","Perro"))))'))
        for col, fmt in {2: EUR, 3: EUR, 4: EUR, 5: '0%', 6: '0', 7: EUR, 8: '0.0%'}.items():
            ws.cell(row=r, column=col).number_format = fmt
        for col in range(1, 10):
            ws.cell(row=r, column=col).border = borde

    rango = f'I{p1}:I{pn}'
    for txt, color in [('Estrella', 'C6EFCE'), ('Caballo', 'FFEB9C'), ('Puzzle', 'DDEBF7'), ('Perro', 'F8CBAD')]:
        ws.conditional_formatting.add(rango, CellIsRule(operator='equal', formula=[f'"{txt}"'], fill=PatternFill('solid', fgColor=color)))

    # Umbrales
    ws['K4'] = 'Umbrales de la matriz'
    ws['K4'].font = Font(bold=True, color='FFFFFF')
    ws['K4'].fill = PatternFill('solid', fgColor=NEGRO)
    ws.merge_cells('K4:L4')
    bloque = [
        ('Margen medio ponderado (umbral de rentabilidad)', f'=SUM(G{p1}:G{pn})/SUM(F{p1}:F{pn})', EUR, False),
        ('Método de popularidad', 'Media', None, True),
        ('Media de unidades por plato', f'=AVERAGE(F{p1}:F{pn})', '0', False),
        ('Umbral de popularidad (unidades)', f'=IF({METODO}="Regla del 70 %",0.7*{MEDIA_UDS},{MEDIA_UDS})', '0', False),
        ('Total de unidades vendidas', f'=SUM(F{p1}:F{pn})', '0', False),
        ('Margen total de la carta', f'=SUM(G{p1}:G{pn})', EUR, False),
    ]
    for i, (k, v, fmt, ent) in enumerate(bloque):
        r = 5 + i
        a = ws.cell(row=r, column=11, value=k)
        a.font = Font(bold=True)
        a.border = borde
        a.alignment = Alignment(wrap_text=True)
        c = ws.cell(row=r, column=12, value=v)
        c.border = borde
        c.font = Font(bold=True)
        if fmt:
            c.number_format = fmt
        c.fill = entrada if ent else PatternFill('solid', fgColor=GRIS)
    dv = DataValidation(type='list', formula1='"Media,Regla del 70 %"', allow_blank=False)
    ws.add_data_validation(dv)
    dv.add('L6')

    guia = [('Qué hacer con cada uno', ''), ('Estrella', 'Proteger y destacar: no tocar la receta.'),
            ('Caballo', 'Subir precio con cabeza o ajustar escandallo y ración.'),
            ('Puzzle', 'Reposicionar en carta, mejor nombre y descripción, empuje de sala.'),
            ('Perro', 'Eliminar o reinventar, salvo que sea estratégico.')]
    for i, (k, v) in enumerate(guia):
        r = 13 + i
        ws.cell(row=r, column=11, value=k).font = Font(bold=True)
        ws.cell(row=r, column=12, value=v).alignment = Alignment(wrap_text=True)
    ws.cell(row=19, column=11, value='Guía con el ejemplo explicado:')
    ws.cell(row=19, column=12, value=GUIA).hyperlink = GUIA
    ws.cell(row=20, column=11, value='Coste de cada plato (plantilla de escandallo gratis):')
    ws.cell(row=20, column=12, value=ESCANDALLO).hyperlink = ESCANDALLO
    for r in (19, 20):
        ws.cell(row=r, column=12).font = Font(color='0563C1', underline='single')

    for col, w in {'A': 40, 'B': 12, 'C': 12, 'D': 11, 'E': 10, 'F': 11, 'G': 13, 'H': 11, 'I': 13, 'J': 3, 'K': 34, 'L': 44}.items():
        ws.column_dimensions[col].width = w
    ws.freeze_panes = f'B{p1}'

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    wb.save(SALIDA)
    subprocess.run([sys.executable, str(RAIZ / 'scripts/productos-digitales/inject_cache.py'), str(SALIDA)],
                   check=True, stdout=subprocess.DEVNULL)
    wv = load_workbook(SALIDA, data_only=True)['Ingeniería de menú']
    clas = [wv.cell(row=p1 + i, column=9).value for i in range(len(PLATOS))]
    assert clas == [p[4] for p in PLATOS], clas
    assert round(float(wv['L5'].value), 2) == 8.53, wv['L5'].value
    assert round(float(wv['L7'].value)) == 150 and round(float(wv['L8'].value)) == 150
    assert int(wv['L9'].value) == 1200
    print(f'OK {SALIDA.relative_to(RAIZ)} · clasificación {clas} · margen medio ponderado {wv["L5"].value:.2f} € · umbral 150 uds')


if __name__ == '__main__':
    main()
