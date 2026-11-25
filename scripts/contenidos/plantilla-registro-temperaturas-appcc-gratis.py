#!/usr/bin/env python3
"""Plantilla GRATIS de registro de temperaturas APPCC (lead magnet de /blog/appcc-seguridad-alimentaria-ia-hosteleria).

Un mes de registro de cámaras: 31 días × 4 lecturas (cada 4 horas, como la tabla de PCC del post), dos cámaras
de refrigeración y un congelador. Los límites son los de la tabla del post (refrigeración de 0 °C a 4 °C,
congelación ≤ −18 °C) y van en celdas editables: cada local pone los de SU plan APPCC.
La columna «¿En rango?» y el color rojo salen solos; la medida correctora y la firma las rellena el equipo.

Uso:  python3 scripts/contenidos/plantilla-registro-temperaturas-appcc-gratis.py
Sale: astro-site/public/descargas/plantilla-registro-temperaturas-appcc-gratis-aichef.xlsx
Inyecta los valores calculados (inject_cache.py) y comprueba las celdas con data_only.
"""
import subprocess
import sys
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / 'astro-site/public/descargas/plantilla-registro-temperaturas-appcc-gratis-aichef.xlsx'
GUIA = 'https://aichef.pro/blog/appcc-seguridad-alimentaria-ia-hosteleria'
PACK = 'https://aichef.pro/pack-appcc?utm_source=plantilla-gratis&utm_medium=xlsx&utm_content=temperaturas'

NEGRO, DORADO, GRIS = '111111', 'FFD700', 'F3F3F3'
fino = Side(style='thin', color='BBBBBB')
borde = Border(left=fino, right=fino, top=fino, bottom=fino)
entrada = PatternFill('solid', fgColor='FFF8D6')
rojo = PatternFill('solid', fgColor='F8CBAD')
HORAS = ['08:00', '12:00', '16:00', '20:00']
# Ejemplo en los dos primeros días (una lectura fuera de rango con su medida correctora).
EJEMPLO = {
    (1, 0): (2.5, 3.0, -19.0, '', 'MG'), (1, 1): (3.0, 3.5, -18.5, '', 'MG'),
    (1, 2): (3.5, 4.0, -19.0, '', 'LP'), (1, 3): (3.0, 3.5, -18.5, '', 'LP'),
    (2, 0): (2.5, 6.5, -19.0, 'Cámara 2 a 6,5 °C: puerta mal cerrada. Cerrada y producto pasado a cámara 1; relectura a las 08:30: 3,5 °C.', 'MG'),
    (2, 1): (3.0, 3.5, -18.5, '', 'MG'),
}


def main():
    wb = Workbook()
    ws = wb.active
    ws.title = 'Registro de temperaturas'
    ws['A1'] = 'Registro de temperaturas de cámaras (APPCC)'
    ws['A1'].font = Font(bold=True, size=16, color=DORADO)
    ws['A1'].fill = PatternFill('solid', fgColor=NEGRO)
    ws.merge_cells('A1:I1')
    ws['A2'] = 'Valores de ejemplo: pon los límites, los equipos y la frecuencia que marque TU plan APPCC.'
    ws['A2'].font = Font(italic=True, color='555555')
    ws.merge_cells('A2:I2')

    datos = [('Establecimiento', ''), ('Mes y año', ''), ('Responsable', '')]
    for i, (k, v) in enumerate(datos):
        ws.cell(row=3 + i, column=1, value=k).font = Font(bold=True)
        ws.merge_cells(start_row=3 + i, start_column=1, end_row=3 + i, end_column=2)
        c = ws.cell(row=3 + i, column=3, value=v)
        c.fill = entrada
        ws.merge_cells(start_row=3 + i, start_column=3, end_row=3 + i, end_column=5)

    # Límites (F3:I5)
    ws['F3'] = 'Límites (edítalos)'
    ws['F3'].font = Font(bold=True)
    lim = [('Refrigeración: mínimo °C', 0), ('Refrigeración: máximo °C', 4), ('Congelación: máximo °C', -18)]
    for i, (k, v) in enumerate(lim):
        ws.cell(row=4 + i, column=6, value=k)
        c = ws.cell(row=4 + i, column=8, value=v)
        c.fill = entrada
        c.font = Font(bold=True)
        c.border = borde
    RMIN, RMAX, CMAX = '$H$4', '$H$5', '$H$6'

    cab = ['Día', 'Hora', 'Cámara 1 (refrigeración) °C', 'Cámara 2 (refrigeración) °C', 'Congelador 1 °C',
           '¿En rango?', 'Medida correctora (si no está en rango)', '', 'Firma']
    ft = 8
    for col, txt in enumerate(cab, start=1):
        c = ws.cell(row=ft, column=col, value=txt or None)
        c.font = Font(bold=True, color='FFFFFF')
        c.fill = PatternFill('solid', fgColor=NEGRO)
        c.alignment = Alignment(wrap_text=True, horizontal='center', vertical='center')
        c.border = borde
    ws.merge_cells(start_row=ft, start_column=7, end_row=ft, end_column=8)
    ws.row_dimensions[ft].height = 42

    p1 = ft + 1
    r = p1
    for dia in range(1, 32):
        for k, hora in enumerate(HORAS):
            ws.cell(row=r, column=1, value=dia)
            ws.cell(row=r, column=2, value=hora).fill = entrada
            ej = EJEMPLO.get((dia, k))
            for col in (3, 4, 5):
                c = ws.cell(row=r, column=col, value=(ej[col - 3] if ej else None))
                c.fill = entrada
                c.number_format = '0.0'
            cg = ws.cell(row=r, column=7, value=(ej[3] or None) if ej else None)
            cg.fill = entrada
            cg.alignment = Alignment(wrap_text=True, vertical='top')
            ws.merge_cells(start_row=r, start_column=7, end_row=r, end_column=8)
            if ej and ej[3]:
                ws.row_dimensions[r].height = 46
            ws.cell(row=r, column=9, value=ej[4] if ej else None).fill = entrada
            ws.cell(row=r, column=6, value=(
                f'=IF(COUNT(C{r}:E{r})=0,"",IF(AND(OR(C{r}="",AND(C{r}>={RMIN},C{r}<={RMAX})),'
                f'OR(D{r}="",AND(D{r}>={RMIN},D{r}<={RMAX})),OR(E{r}="",E{r}<={CMAX})),"Sí","NO"))'))
            for col in range(1, 10):
                ws.cell(row=r, column=col).border = borde
            r += 1
    pn = r - 1

    ws.conditional_formatting.add(f'F{p1}:F{pn}', CellIsRule(operator='equal', formula=['"NO"'], fill=rojo, font=Font(bold=True)))
    ws.conditional_formatting.add(f'C{p1}:D{pn}', FormulaRule(formula=[f'AND(C{p1}<>"",OR(C{p1}<{RMIN},C{p1}>{RMAX}))'], fill=rojo))
    ws.conditional_formatting.add(f'E{p1}:E{pn}', FormulaRule(formula=[f'AND(E{p1}<>"",E{p1}>{CMAX})'], fill=rojo))

    fn = pn + 2
    notas = [
        'Cada lectura en rojo necesita su medida correctora escrita y una nueva lectura.',
        'Revisa los termómetros con un termómetro patrón según tu plan, y guarda este registro el tiempo que te pida.',
    ]
    for i, n in enumerate(notas):
        ws.cell(row=fn + i, column=1, value=n).font = Font(italic=True, color='555555')
        ws.merge_cells(start_row=fn + i, start_column=1, end_row=fn + i, end_column=9)
    for k, (etq, url) in enumerate([('Guía del APPCC con el ejemplo de PCC:', GUIA),
                                     ('19 plantillas de APPCC (limpieza, trazabilidad, alérgenos, plagas…): Pack APPCC', PACK)]):
        rr = fn + 3 + k
        ws.cell(row=rr, column=1, value=etq).font = Font(bold=True)
        ws.merge_cells(start_row=rr, start_column=1, end_row=rr, end_column=5)
        c = ws.cell(row=rr, column=6, value=url)
        c.hyperlink = url
        c.font = Font(color='0563C1', underline='single')
        ws.merge_cells(start_row=rr, start_column=6, end_row=rr, end_column=9)

    for col, w in {'A': 6, 'B': 9, 'C': 15, 'D': 15, 'E': 14, 'F': 10, 'G': 40, 'H': 12, 'I': 10}.items():
        ws.column_dimensions[col].width = w
    ws.column_dimensions['F'].width = 12
    ws.freeze_panes = f'C{p1}'
    ws.print_title_rows = f'{ft}:{ft}'
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    wb.save(SALIDA)
    subprocess.run([sys.executable, str(RAIZ / 'scripts/productos-digitales/inject_cache.py'), str(SALIDA)],
                   check=True, stdout=subprocess.DEVNULL)
    wv = load_workbook(SALIDA, data_only=True)['Registro de temperaturas']
    en_rango = [wv.cell(row=p1 + i, column=6).value for i in range(6)]
    assert en_rango == ['Sí', 'Sí', 'Sí', 'Sí', 'NO', 'Sí'], en_rango
    assert wv.cell(row=p1 + 6, column=6).value in (None, ''), wv.cell(row=p1 + 6, column=6).value
    assert pn - p1 + 1 == 124
    print(f'OK {SALIDA.relative_to(RAIZ)} · 124 lecturas · ejemplo {en_rango}')


if __name__ == '__main__':
    main()
