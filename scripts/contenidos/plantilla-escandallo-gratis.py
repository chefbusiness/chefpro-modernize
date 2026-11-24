#!/usr/bin/env python3
"""Plantilla de escandallo GRATIS (lead magnet del pilar /blog/escandallos-ia-cocina-profesional).

Una hoja de escandallo con el ejemplo del post (Salmón a la plancha con verduras salteadas,
4,29 € por ración) ya rellenado, 15 filas libres con las fórmulas puestas y el bloque
coste → PVP sin IVA → PVP con IVA → precio de carta → food cost real. Es el escalón
gratuito; el Kit de Escandallos Pro (de pago) es el completo.

Las cifras del ejemplo tienen que cuadrar con el post: el coste de cada línea se redondea a
céntimos (como en la tabla del artículo) y el total da 4,29 €. El script lo comprueba.

Uso:  python3 scripts/contenidos/plantilla-escandallo-gratis.py
Sale: astro-site/public/descargas/plantilla-escandallo-gratis-aichef.xlsx
El script inyecta él mismo los valores calculados (inject_cache.py, pycel) para que los visores
que no recalculan (Quick Look, WhatsApp, Gmail) no enseñen celdas en blanco, y comprueba las
celdas del libro con data_only. Después: python3 scripts/productos-digitales/parche_xml_xlsx.py --check <xlsx>
"""
import subprocess
import sys
from pathlib import Path

from openpyxl import load_workbook

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / 'astro-site/public/descargas/plantilla-escandallo-gratis-aichef.xlsx'
GUIA = 'https://aichef.pro/blog/escandallos-ia-cocina-profesional'
KIT = 'https://aichef.pro/kit-escandallos?utm_source=plantilla-gratis&utm_medium=xlsx&utm_content=escandallo'

# (ingrediente, bruto comprado en kg o L, merma, precio €/kg o €/L) — los del post.
EJEMPLO = [
    ('Lomo de salmón fresco', 0.220, 0.18, 16.00),
    ('Calabacín', 0.090, 0.10, 2.20),
    ('Pimiento rojo', 0.075, 0.20, 2.80),
    ('Cebolla morada', 0.046, 0.12, 1.50),
    ('Ajo', 0.006, 0.10, 6.00),
    ('AOVE', 0.015, 0.00, 9.00),
    ('Limón (emplatado)', 0.030, 0.00, 2.00),
]
FIJO = ('Sal, pimienta, perejil (coste fijo)', 0.05)
FILAS_LIBRES = 15

NEGRO, DORADO, GRIS = '111111', 'FFD700', 'F3F3F3'
EUR = '#,##0.00 "€"'
EUR_KG = '#,##0.00 "€/kg"'
KG = '0.000'
PCT = '0%'
PCT1 = '0.0%'
fino = Side(style='thin', color='BBBBBB')
borde = Border(left=fino, right=fino, top=fino, bottom=fino)
entrada = PatternFill('solid', fgColor='FFF8D6')  # celdas que rellena el cocinero


def cabecera(ws):
    ws['A1'] = 'Plantilla de escandallo de cocina'
    ws['A1'].font = Font(bold=True, size=16, color=DORADO)
    ws['A1'].fill = PatternFill('solid', fgColor=NEGRO)
    ws.merge_cells('A1:G1')
    ws['A2'] = 'Rellena solo las celdas amarillas. El resto se calcula solo.'
    ws['A2'].font = Font(italic=True, color='555555')
    ws.merge_cells('A2:G2')
    ws['A3'] = 'Plato:'
    ws['B3'] = 'Salmón a la plancha con verduras salteadas'
    ws['B3'].fill = entrada
    ws.merge_cells('B3:G3')
    ws['A3'].font = Font(bold=True)


def main():
    wb = Workbook()
    ws = wb.active
    ws.title = 'Escandallo'
    cabecera(ws)

    titulos = ['Ingrediente', 'Cantidad bruta comprada (kg o L)', 'Merma (%)',
               'Cantidad neta (kg o L)', 'Precio de compra (€/kg o €/L)',
               'Precio real neto (€/kg o €/L)', 'Coste (€)']
    fila_t = 5
    for col, txt in enumerate(titulos, start=1):
        c = ws.cell(row=fila_t, column=col, value=txt)
        c.font = Font(bold=True, color='FFFFFF')
        c.fill = PatternFill('solid', fgColor=NEGRO)
        c.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
        c.border = borde
    ws.row_dimensions[fila_t].height = 42

    primera = fila_t + 1
    filas = [(n, b, m, p) for n, b, m, p in EJEMPLO] + [None] * FILAS_LIBRES
    r = primera
    for item in filas:
        if item:
            n, b, m, p = item
            ws.cell(row=r, column=1, value=n)
            ws.cell(row=r, column=2, value=b)
            ws.cell(row=r, column=3, value=m)
            ws.cell(row=r, column=5, value=p)
        # Fórmulas: neta = bruta × (1 − merma) · kilo neto = precio / (1 − merma)
        # coste = bruta × precio, redondeado a céntimos (como la tabla del post).
        ws.cell(row=r, column=4, value=f'=IF(B{r}="","",B{r}*(1-C{r}))')
        ws.cell(row=r, column=6, value=f'=IF(OR(E{r}="",C{r}>=1),"",E{r}/(1-C{r}))')
        ws.cell(row=r, column=7, value=f'=IF(OR(B{r}="",E{r}=""),"",ROUND(B{r}*E{r},2))')
        for col in range(1, 8):
            c = ws.cell(row=r, column=col)
            c.border = borde
            if col in (1, 2, 3, 5):
                c.fill = entrada
        ws.cell(row=r, column=2).number_format = KG
        ws.cell(row=r, column=3).number_format = PCT
        ws.cell(row=r, column=4).number_format = KG
        ws.cell(row=r, column=5).number_format = EUR_KG
        ws.cell(row=r, column=6).number_format = EUR
        ws.cell(row=r, column=7).number_format = EUR
        r += 1

    # Línea de coste fijo (sal, especias…): se escribe el coste directamente.
    fila_fijo = r
    ws.cell(row=fila_fijo, column=1, value=FIJO[0])
    ws.cell(row=fila_fijo, column=7, value=FIJO[1])
    for col in range(1, 8):
        ws.cell(row=fila_fijo, column=col).border = borde
    ws.cell(row=fila_fijo, column=1).fill = entrada
    ws.cell(row=fila_fijo, column=7).fill = entrada
    ws.cell(row=fila_fijo, column=7).number_format = EUR
    ultima = fila_fijo

    dv = DataValidation(type='decimal', operator='between', formula1='0', formula2='0.99',
                        error='La merma va de 0 % a 99 %.', errorTitle='Merma')
    ws.add_data_validation(dv)
    dv.add(f'C{primera}:C{ultima - 1}')

    # Bloque de precio.
    b = ultima + 2
    bloque = [
        ('Coste total de materia prima', f'=SUM(G{primera}:G{ultima})', EUR, False),
        ('Raciones que salen', 1, '0', True),
        ('Coste por ración', f'=B{b}/B{b + 1}', EUR, False),
        ('Food cost objetivo', 0.30, PCT, True),
        ('PVP sin IVA', f'=B{b + 2}/B{b + 3}', EUR, False),
        ('IVA (restauración en España: 10 %)', 0.10, PCT, True),
        ('PVP con IVA', f'=B{b + 4}*(1+B{b + 5})', EUR, False),
        ('Precio de carta (redondeado por ti)', 15.90, EUR, True),
        ('Food cost real con ese precio', f'=B{b + 2}/(B{b + 7}/(1+B{b + 5}))', PCT1, False),
        ('Margen bruto por ración', f'=B{b + 7}/(1+B{b + 5})-B{b + 2}', EUR, False),
    ]
    for i, (etq, val, fmt, es_entrada) in enumerate(bloque):
        fila = b + i
        a = ws.cell(row=fila, column=1, value=etq)
        a.font = Font(bold=True)
        a.border = borde
        v = ws.cell(row=fila, column=2, value=val)
        v.number_format = fmt
        v.border = borde
        v.font = Font(bold=True)
        if es_entrada:
            v.fill = entrada
        else:
            v.fill = PatternFill('solid', fgColor=GRIS)

    nota = b + len(bloque) + 1
    ws.cell(row=nota, column=1, value='Guía paso a paso con tres ejemplos resueltos:')
    ws.cell(row=nota, column=2, value=GUIA).hyperlink = GUIA
    ws.cell(row=nota + 1, column=1, value='¿Toda la carta, mermas y PVP? Kit de Escandallos Pro:')
    ws.cell(row=nota + 1, column=2, value=KIT).hyperlink = KIT
    for f in (nota, nota + 1):
        ws.cell(row=f, column=2).font = Font(color='0563C1', underline='single')

    anchos = {'A': 40, 'B': 18, 'C': 11, 'D': 15, 'E': 17, 'F': 17, 'G': 12}
    for col, w in anchos.items():
        ws.column_dimensions[col].width = w
    ws.freeze_panes = f'A{primera}'

    # Hoja de instrucciones.
    h = wb.create_sheet('Cómo se usa')
    pasos = [
        'Cómo usar esta plantilla',
        '1. Escribe cada ingrediente, también la sal, el aceite y la guarnición.',
        '2. Cantidad bruta = lo que compras y pagas (con piel, espinas o hueso), en kg o litros.',
        '3. Merma = lo que pierdes al limpiar o cocinar. Un 18 % se escribe 18 %.',
        '4. Precio de compra = el del último albarán, por kg o por litro.',
        '5. Lo pequeño (sal, especias, perejil) va en la última línea: escribe su coste directamente en la columna G.',
        '6. Indica cuántas raciones salen y tu food cost objetivo.',
        '7. Redondea el PVP con IVA a tu precio de carta y mira el food cost real.',
        '',
        'Las columnas D, F y G y el bloque de precio llevan fórmulas: no las borres.',
        'Revisa los precios cada vez que cambie una tarifa o la temporada.',
        '',
        'Plantilla gratuita de AI Chef Pro (aichef.pro). Puedes copiarla y adaptarla.',
    ]
    for i, txt in enumerate(pasos, start=1):
        c = h.cell(row=i, column=1, value=txt)
        if i == 1:
            c.font = Font(bold=True, size=14, color=DORADO)
            c.fill = PatternFill('solid', fgColor=NEGRO)
    h.column_dimensions['A'].width = 95

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    wb.save(SALIDA)

    # Gate: el ejemplo del post tiene que dar 4,29 €, 14,30 € y el resto de cifras citadas.
    coste = round(sum(round(bru * pre, 2) for _, bru, _, pre in EJEMPLO) + FIJO[1], 2)
    assert coste == 4.29, coste
    pvp = round(coste / 0.30, 2)
    assert pvp == 14.30, pvp
    assert round(pvp * 1.10, 2) == 15.73
    fc_real = coste / (15.90 / 1.10)
    assert round(fc_real * 100, 1) == 29.7, fc_real
    assert round(15.90 / 1.10 - coste, 2) == 10.16
    # Valores cacheados + comprobación sobre el LIBRO, no sobre la aritmética en Python.
    subprocess.run([sys.executable, str(RAIZ / 'scripts/productos-digitales/inject_cache.py'), str(SALIDA)],
                   check=True, stdout=subprocess.DEVNULL)
    wsv = load_workbook(SALIDA, data_only=True)['Escandallo']
    celdas = {'G6': 3.52, 'B30': 4.29, 'B32': 4.29, 'B34': 14.30, 'B36': 15.73, 'B39': 10.16}
    for ref, esperado in celdas.items():
        v = wsv[ref].value
        assert v is not None and round(float(v), 2) == esperado, (ref, v, esperado)
    assert round(float(wsv['B38'].value) * 100, 1) == 29.7, wsv['B38'].value
    print(f'OK {SALIDA.relative_to(RAIZ)} · coste {coste} · PVP {pvp} · con IVA 15,73 · '
          f'FC real {fc_real:.1%}')


if __name__ == '__main__':
    main()
