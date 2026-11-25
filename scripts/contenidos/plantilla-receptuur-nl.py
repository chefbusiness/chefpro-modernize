#!/usr/bin/env python3
"""Receptuur (NL), sjabloon GRATIS — lead magnet de /nl/blog/receptuur.

Gemelo neerlandés de plantilla-ficha-tecnica-gratis.py (misma hoja única, mismo diseño, mismas fórmulas y mismo
ejemplo: zalm van de grillplaat met gesauteerde groenten), ADAPTADO:
  - btw de eten in de horeca 9 % (en vez del IVA del 10 %): verkoopprijs € 14,30 excl. / € 15,59 incl.; op de kaart
    € 15,90 → werkelijke food cost 29,4 %;
  - los 14 allergenen con su nombre oficial neerlandés y dos columnas para marcar con «X»: «Bevat» y «Kan bevatten
    (kruisbesmetting)», más «Welke soort / via welk ingrediënt» (granen y noten piden «noteer welke»). Nunca «sporen»;
  - kritische controlepunten y bewaring remiten al HACCP-plan of de Hygiënecode voor de Horeca (sin cifras de España);
  - fila «Gecontroleerd door»; uitval ≥ 100 % muestra aviso en la bruto hoeveelheid (como el gemelo FR);
  - pie con la guía NL y la food cost calculator NL (en vez de la plantilla de escandallo española).
LowFruits NL (nov-2026): «receptuur» 170/mes, «receptuur voorbeeld» 90.
Sale: astro-site/public/descargas/receptuur-sjabloon-gratis-aichef.xlsx
El xlsx pasa por inject_cache.py + caché «texto vacío» (como el DE), un gate data_only, un gate pycel sobre una COPIA
sin caché (los números del post salen de las fórmulas, no de lo inyectado), un gate de idioma (nada de español ni
«sporen») y parche_xml_xlsx.py --check. `/descargas/*` está en noindex (netlify.toml). Sesión Claude Code, 25-nov-2026.
"""
import contextlib
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import zipfile
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / 'astro-site/public/descargas/receptuur-sjabloon-gratis-aichef.xlsx'
INJECT = RAIZ / 'scripts/productos-digitales/inject_cache.py'
PARCHE = RAIZ / 'scripts/productos-digitales/parche_xml_xlsx.py'
GIDS = 'https://aichef.pro/nl/blog/receptuur'
CALCULATOR = 'https://aichef.pro/nl/food-cost-calculator-restaurant'
HOJA = 'Receptuur'

NEGRO, DORADO, GRIS = '111111', 'FFD700', 'F3F3F3'
fino = Side(style='thin', color='BBBBBB')
borde = Border(left=fino, right=fino, top=fino, bottom=fino)
entrada = PatternFill('solid', fgColor='FFF8D6')
EUR = '"€" #,##0.00'  # en un Excel en neerlandés: € 4,29
UITVAL_KO = 'uitval ≥ 100 %'

# (ingrediënt, netto, eenheid, uitval) — los del post (y del ejemplo ES).
INGREDIENTEN = [
    ('Verse zalmfilet', 180, 'g', 0.18),
    ('Courgette', 80, 'g', 0.10),
    ('Rode paprika', 60, 'g', 0.20),
    ('Rode ui', 40, 'g', 0.12),
    ('Knoflook', 5, 'g', 0.10),
    ('Extra vierge olijfolie', 15, 'ml', 0.0),
    ('Citroen', 30, 'g', 0.0),
    ('Zout, peper en peterselie (2 g · 0,5 g · 3 g)', None, 'g', 0.0),  # sin netto: la bruta queda vacía
]
BRUTO = [220, 89, 75, 46, 6, 15, 30]
STAPPEN = [
    ('Snijd de courgette en de paprika in gelijke reepjes, de rode ui in fijne julienne en de knoflook in plakjes.',
     '5 min', ''),
    ('Bak de groenten met de knoflook en 10 ml extra vierge olijfolie op hoog vuur, zonder dat ze hun kleur verliezen.',
     '4 min', 'hoog vuur'),
    ('Schroei de zalm met de resterende 5 ml extra vierge olijfolie aan op de huidzijde en maak hem aan de andere kant af.',
     '6 min', 'goed hete grillplaat'),
    ('Haal de zalm eraf en laat hem een minuut rusten voor het opmaken.', '1 min', ''),
    ('Maak de groenten als basis op, leg de zalm er met de huid naar boven op en werk af met het partje citroen en de '
     'peterselie.', '2 min', ''),
]
ALLERGENEN = [
    'Glutenbevattende granen (tarwe, rogge, gerst, haver, spelt, khorasantarwe of hybriden: noteer welke)',
    'Schaaldieren', 'Eieren', 'Vis', "Aardnoten (pinda's)", 'Soja', 'Melk (inclusief lactose)',
    'Noten (amandelen, hazelnoten, walnoten, cashewnoten, pecannoten, paranoten, pistachenoten, macadamianoten: '
    'noteer welke)',
    'Selderij', 'Mosterd', 'Sesamzaad', 'Zwaveldioxide en sulfieten (> 10 mg/kg of 10 mg/l als SO2)', 'Lupine',
    'Weekdieren',
]
assert len(ALLERGENEN) == 14
HACCP = 'volgens uw HACCP-plan of de Hygiënecode voor de Horeca'
FOOTER_GIDS = 'Gratis sjabloon van AI Chef Pro · Uitleg:'
FOOTER_CALC = 'Gratis food cost calculator (kostprijs per gerecht):'
NOTA_BTW = 'De food cost rekent u altijd over de verkoopprijs exclusief btw, nooit over de prijs inclusief btw.'

# Gate de idioma: palabras españolas (del generador ES) que no pueden quedar en el xlsx, más «sporen».
PROHIBIDAS = ['ración', 'raciones', 'merma', 'alérgeno', 'alérgenos', 'contiene', 'trazas', 'elaboración', 'paso',
              'conservación', 'emplatado', 'montaje', 'menaje', 'plato', 'coste', 'pvp', 'iva', 'appcc', 'sanidad',
              'escandallo', 'rellena', 'guía', 'plantilla', 'ficha', 'técnica', 'cocina', 'salmón', 'pescado', 'fuego',
              'plancha', 'aove', 'autor', 'fecha', 'versión', 'cantidad', 'bruta', 'neta', 'unidad', 'tiempo',
              'temperatura', 'categoría', 'peso', 'precio', 'carta', 'objetivo', 'real', 'restauración', 'españa',
              'reglamento', 'ue', 'limón', 'ajo', 'cebolla', 'pimiento', 'calabacín', 'sal', 'pimienta', 'perejil',
              'verduras', 'vida', 'útil', 'puntos', 'críticos', 'con', 'del', 'los', 'las', 'para', 'por', 'una',
              'que', 'sin', 'tu', 'y', 'aaaa', 'sporen']
TIPOGRAFIA_OK = set('·€≥–—’‘“”…°')


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


def alto(ws, fila, *textos_y_anchos):
    """Alto explícito (15 pt por línea estimada): Excel no ajusta solo las filas con celdas combinadas."""
    lineas = max(len(textwrap.wrap(t, w)) if t else 1 for t, w in textos_y_anchos)
    if lineas > 1:
        ws.row_dimensions[fila].height = 15 * lineas + 2


def formula_bruto(f):
    # bruto = netto / (1 − uitval), naar boven afgerond op de gram; uitval ≥ 100 % → aviso (como el gemelo FR)
    return f'=IF(OR(B{f}="",NOT(ISNUMBER(B{f}))),"",IF(N(D{f})>=1,"{UITVAL_KO}",ROUNDUP(B{f}/(1-N(D{f})),0)))'


def generar():
    wb = Workbook()
    ws = wb.active
    ws.title = HOJA
    ws['A1'] = 'Receptuur'
    ws['A1'].font = Font(bold=True, size=16, color=DORADO)
    ws['A1'].fill = PatternFill('solid', fgColor=NEGRO)
    ws.merge_cells('A1:F1')
    ws['A2'] = 'Vul de gele cellen in. De bruto hoeveelheid en de verkoopprijs worden automatisch berekend.'
    ws['A2'].font = Font(italic=True, color='555555')
    ws.merge_cells('A2:F2')

    # Algemene gegevens (filas 5-12)
    titulo(ws, 4, 'Algemene gegevens')
    gegevens = [('Gerecht', 'Zalm van de grillplaat met gesauteerde groenten'), ('Categorie', 'Vis'),
                ('Aantal porties', 1), ('Gewicht per portie', "Ongeveer 410 g rauw (som van de netto's)"),
                ('Bereidingstijd', '20 min'), ('Auteur', 'Chef-kok'), ('Gecontroleerd door', ''),
                ('Datum en versie', 'dd-mm-jjjj · v1.0')]
    for i, (k, v) in enumerate(gegevens):
        f = 5 + i
        celda(ws, f, 1, k, negrita=True)
        celda(ws, f, 2, v if v != '' else None, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=2, end_row=f, end_column=6)

    # Ingrediënten (título fila 14, cabecera 15, datos desde la 16)
    titulo(ws, 14, 'Ingrediënten (per portie)')
    kop = ['Ingrediënt', 'Netto hoeveelheid (op het bord)', 'Eenheid', 'Uitval (%)', 'Bruto hoeveelheid (in te kopen)',
           'Allergenen in dit ingrediënt']
    for col, txt in enumerate(kop, start=1):
        c = celda(ws, 15, col, txt, negrita=True)
        c.fill = PatternFill('solid', fgColor=GRIS)
    ws.row_dimensions[15].height = 47
    eerste = 16
    rijen = INGREDIENTEN + [None] * 4
    for i, item in enumerate(rijen):
        f = eerste + i
        if item:
            n, netto, eenheid, uitval = item
            celda(ws, f, 1, n, es_entrada=True)
            celda(ws, f, 2, netto, '0', es_entrada=True)
            celda(ws, f, 3, eenheid, es_entrada=True)
            celda(ws, f, 4, uitval, '0%', es_entrada=True)
            celda(ws, f, 6, 'Vis' if n == 'Verse zalmfilet' else None, es_entrada=True)
            alto(ws, f, (n, 33))
        else:
            for col in (1, 2, 3, 4, 6):
                celda(ws, f, col, None, '0%' if col == 4 else ('0' if col == 2 else None), es_entrada=True)
        celda(ws, f, 5, formula_bruto(f), '0')
    laatste_ing = eerste + len(rijen) - 1
    dvu = DataValidation(type='decimal', operator='between', formula1='0', formula2='0.99',
                         error='De uitval ligt tussen 0 % en 99 % (typ 20 % of 0,2).', errorTitle='Uitval',
                         showErrorMessage=True)
    ws.add_data_validation(dvu)
    dvu.add(f'D{eerste}:D{laatste_ing}')

    # Bereiding
    fb = laatste_ing + 2
    titulo(ws, fb, 'Bereiding stap voor stap')
    for col, txt in enumerate(['Stap', 'Handeling', '', '', 'Tijd', 'Temperatuur / gaarpunt'], start=1):
        if txt:
            c = celda(ws, fb + 1, col, txt, negrita=True)
            c.fill = PatternFill('solid', fgColor=GRIS)
    ws.merge_cells(start_row=fb + 1, start_column=2, end_row=fb + 1, end_column=4)
    stappen = STAPPEN + [('', '', '')] * 3
    for i, (txt, tijd, temp) in enumerate(stappen):
        f = fb + 2 + i
        celda(ws, f, 1, i + 1)
        celda(ws, f, 2, txt or None, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=2, end_row=f, end_column=4)
        celda(ws, f, 5, tijd or None, es_entrada=True)
        celda(ws, f, 6, temp or None, es_entrada=True)
        ws.row_dimensions[f].height = 48

    # Allergenen: dos columnas para marcar con X (Bevat / Kan bevatten) + soort
    fa = fb + 2 + len(stappen) + 1
    titulo(ws, fa, 'Allergenen (Verordening (EU) nr. 1169/2011): zet een X in de juiste kolom')
    for c0, c1, txt in ((1, 1, 'Allergeen'), (2, 2, 'Bevat'), (3, 4, 'Kan bevatten (kruisbesmetting)'),
                        (5, 6, 'Welke soort / via welk ingrediënt')):
        c = celda(ws, fa + 1, c0, txt, negrita=True)
        c.fill = PatternFill('solid', fgColor=GRIS)
        if c1 > c0:
            celda(ws, fa + 1, c1).fill = PatternFill('solid', fgColor=GRIS)
            ws.merge_cells(start_row=fa + 1, start_column=c0, end_row=fa + 1, end_column=c1)
    ws.row_dimensions[fa + 1].height = 32
    dvx = DataValidation(type='list', formula1='"X"', allow_blank=True, showErrorMessage=True,
                         errorTitle='Allergenen', error='Kies X of laat de cel leeg.')
    ws.add_data_validation(dvx)
    eerste_all = fa + 2
    for i, a in enumerate(ALLERGENEN):
        f = eerste_all + i
        celda(ws, f, 1, a)
        celda(ws, f, 2, 'X' if a == 'Vis' else None, es_entrada=True).alignment = Alignment(horizontal='center',
                                                                                          vertical='top')
        celda(ws, f, 3, None, es_entrada=True).alignment = Alignment(horizontal='center', vertical='top')
        celda(ws, f, 4, None, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=3, end_row=f, end_column=4)
        celda(ws, f, 5, 'Verse zalmfilet' if a == 'Vis' else None, es_entrada=True)
        celda(ws, f, 6, None, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=5, end_row=f, end_column=6)
        alto(ws, f, (a, 33))
    laatste_all = eerste_all + len(ALLERGENEN) - 1
    dvx.add(f'B{eerste_all}:C{laatste_all}')

    # Bewaring en kritische controlepunten
    fc = laatste_all + 2
    titulo(ws, fc, 'Bewaring en kritische beheerspunten (CCP)')
    for i, (k, v) in enumerate([
            ('Bewaring', 'Zalm gekoeld tot het aanschroeien; gesneden groenten afgedekt en gekoeld. Tijden en '
                         f'temperaturen {HACCP}.'),
            ('Kritische beheerspunten (CCP)', f'Koude keten van de vis; bereiding van de zalm. Grenzen en wie ze '
                                               f'controleert: {HACCP}.'),
            ('Houdbaarheid van voorbereidingen', f'{HACCP[0].upper()}{HACCP[1:]}.')]):
        f = fc + 1 + i
        celda(ws, f, 1, k, negrita=True)
        celda(ws, f, 2, v, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=2, end_row=f, end_column=6)
        alto(ws, f, (k, 33), (v, 72))
    fo = fc + 5
    titulo(ws, fo, 'Opmaak')
    for i, (k, v) in enumerate([
            ('Opbouw', 'Groenten in het midden als basis, zalm erop met de huid naar boven, een partje citroen en '
                       'gehakte peterselie.'),
            ('Servies', 'Plat bord.'), ('Referentiefoto', 'Plak hier de foto van het afgewerkte bord.')]):
        f = fo + 1 + i
        celda(ws, f, 1, k, negrita=True)
        celda(ws, f, 2, v, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=2, end_row=f, end_column=6)
        alto(ws, f, (k, 33), (v, 72))

    # Kostprijs → verkoopprijs
    fk = fo + 5
    titulo(ws, fk, 'Kostprijs en verkoopprijs')
    b = fk + 1
    blok = [
        ('Kostprijs per portie (uit uw kostprijsberekening)', 4.29, EUR, True),
        ('Beoogde food cost (%)', 0.30, '0%', True),
        ('Verkoopprijs excl. btw', f'=IF(OR(B{b}="",N(B{b + 1})=0),"",B{b}/B{b + 1})', EUR, False),
        ('Btw (eten in de horeca in Nederland: 9 %)', 0.09, '0%', True),
        ('Verkoopprijs incl. btw', f'=IF(B{b + 2}="","",B{b + 2}*(1+N(B{b + 3})))', EUR, False),
        ('Prijs op de kaart (incl. btw, zelf afgerond)', 15.90, EUR, True),
        ('Werkelijke food cost bij die prijs (%)', f'=IF(OR(B{b}="",N(B{b + 5})=0),"",B{b}/(B{b + 5}/(1+N(B{b + 3}))))', '0.0%', False),
    ]
    for i, (k, v, fmt, ent) in enumerate(blok):
        celda(ws, b + i, 1, k, negrita=True)
        c = celda(ws, b + i, 2, v, fmt, es_entrada=ent, negrita=True)
        if not ent:
            c.fill = PatternFill('solid', fgColor=GRIS)
        alto(ws, b + i, (k, 33))
    fn = b + len(blok) + 1
    ws.cell(row=fn, column=1, value=NOTA_BTW).font = Font(italic=True, color='555555')
    ws.merge_cells(start_row=fn, start_column=1, end_row=fn, end_column=6)
    ws.cell(row=fn + 1, column=1, value=FOOTER_GIDS)
    ws.cell(row=fn + 1, column=2, value=GIDS).hyperlink = GIDS
    ws.cell(row=fn + 2, column=1, value=FOOTER_CALC)
    ws.cell(row=fn + 2, column=2, value=CALCULATOR).hyperlink = CALCULATOR
    for f in (fn + 1, fn + 2):
        ws.cell(row=f, column=2).font = Font(color='0563C1', underline='single')

    for col, w in {'A': 34, 'B': 16, 'C': 10, 'D': 11, 'E': 16, 'F': 24}.items():
        ws.column_dimensions[col].width = w
    ws.page_setup.orientation = 'portrait'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    wb.save(SALIDA)
    return {'eerste': eerste, 'laatste_ing': laatste_ing, 'eerste_all': eerste_all, 'laatste_all': laatste_all,
            'b': b, 'fn': fn}


# ---------------------------------------------------------------- caché
def cache_texto_vacio(ruta):
    """inject_cache.py no inyecta el resultado «""»: la celda se queda con caché vacía (<v/>, que un visor sin
    recálculo enseña como 0 en la bruto hoeveelheid). Se escribe como Excel (t="str" + <v></v>), tocando solo el XML
    de las hojas (copiado del gemelo DE)."""
    patron = re.compile(r'<c r="([A-Z]+[0-9]+)"((?:(?!\st=)[^>])*)>(<f>[^<]*</f>)(?:<v>\s*</v>|<v\s*/>)?</c>')
    with zipfile.ZipFile(ruta) as z:
        partes = [(i, z.read(i.filename)) for i in z.infolist()]
    n = 0
    with zipfile.ZipFile(str(ruta) + '.tmp', 'w', zipfile.ZIP_DEFLATED) as zout:
        for info, datos in partes:
            if re.match(r'xl/worksheets/sheet[0-9]+\.xml$', info.filename):
                xml, k = patron.subn(r'<c r="\1"\2 t="str">\3<v></v></c>', datos.decode('utf-8'))
                datos, n = xml.encode('utf-8'), n + k
            zout.writestr(info, datos)
    shutil.move(str(ruta) + '.tmp', str(ruta))
    return n


def inyectar(ruta):
    out = subprocess.run([sys.executable, str(INJECT), str(ruta)], check=True, capture_output=True, text=True).stdout
    m = re.search(r'formulas=(\d+) cache_inyectado=(\d+) fallos_pycel=(\d+)', out)
    assert m and m.group(3) == '0', out
    vacias = cache_texto_vacio(ruta)
    assert int(m.group(1)) == int(m.group(2)) + vacias, (out, vacias)  # toda fórmula lleva caché
    return f'formulas={m.group(1)} cache={m.group(2)} vacías={vacias}'


# ---------------------------------------------------------------- gates
def gate_fichero(p):
    wf = load_workbook(SALIDA)
    assert wf.sheetnames == [HOJA], wf.sheetnames
    ws = wf[HOJA]
    e, b = p['eerste'], p['b']
    # alérgenos: los 14 nombres oficiales, una única lista «X» sobre Bevat + Kan bevatten; ejemplo = solo vis
    assert [ws.cell(row=p['eerste_all'] + i, column=1).value for i in range(14)] == ALLERGENEN
    assert ws.cell(row=p['eerste_all'] - 1, column=2).value == 'Bevat'
    assert ws.cell(row=p['eerste_all'] - 1, column=3).value == 'Kan bevatten (kruisbesmetting)'
    lijst = [d for d in ws.data_validations.dataValidation if d.type == 'list']
    assert len(lijst) == 1 and lijst[0].formula1 == '"X"', lijst
    assert str(lijst[0].sqref) == f'B{p["eerste_all"]}:C{p["laatste_all"]}', lijst[0].sqref
    dec = [d for d in ws.data_validations.dataValidation if d.type == 'decimal']
    assert len(dec) == 1 and str(dec[0].sqref) == f'D{e}:D{p["laatste_ing"]}', dec
    assert all(d.showErrorMessage for d in ws.data_validations.dataValidation)
    marcas = {ws.cell(row=p['eerste_all'] + i, column=c).value for i in range(14) for c in (2, 3)} - {None}
    assert marcas == {'X'} and ws.cell(row=p['eerste_all'] + ALLERGENEN.index('Vis'), column=2).value == 'X'
    assert sum(ws.cell(row=p['eerste_all'] + i, column=c).value == 'X' for i in range(14) for c in (2, 3)) == 1
    # bloque de precio: 9 % btw, 4,29, 30 %, 15,90; formato euro
    assert (ws[f'B{b}'].value, ws[f'B{b + 1}'].value, ws[f'B{b + 3}'].value, ws[f'B{b + 5}'].value) == \
        (4.29, 0.30, 0.09, 15.90)
    assert all(ws[f'B{b + i}'].number_format == EUR for i in (0, 2, 4, 5))
    # pie: guía NL y calculadora NL, con hipervínculo
    destinos = {c.hyperlink.target for row in ws.iter_rows() for c in row if c.hyperlink}
    assert destinos == {GIDS, CALCULATOR}, destinos
    assert ws.cell(row=p['fn'] + 1, column=1).value == FOOTER_GIDS
    # data_only = lo que ve un visor que no recalcula
    wv = load_workbook(SALIDA, data_only=True)[HOJA]
    bruto = [wv.cell(row=e + i, column=5).value for i in range(7)]
    assert all(isinstance(x, (int, float)) for x in bruto), bruto
    assert [int(x) for x in bruto] == BRUTO, bruto
    assert all(wv.cell(row=e + i, column=5).value in (None, '') for i in range(7, 12))  # zout… y 4 filas vacías
    excl, incl, fc = (wv[f'B{b + 2}'].value, wv[f'B{b + 4}'].value, wv[f'B{b + 6}'].value)
    assert (round(excl, 2), round(incl, 2), round(fc * 100, 1)) == (14.30, 15.59, 29.4), (excl, incl, fc)
    return bruto


def gate_pycel(p):
    """Las cifras del post salen de las FÓRMULAS: copia sin caché (openpyxl no conserva los <v>) + pycel."""
    logging.disable(logging.CRITICAL)
    from pycel import ExcelCompiler
    wf = load_workbook(SALIDA)
    with tempfile.TemporaryDirectory() as tmp:
        copia = str(Path(tmp) / 'sin-cache.xlsx')
        wf.save(copia)
        with zipfile.ZipFile(copia) as z:
            hoja = z.read('xl/worksheets/sheet1.xml').decode('utf-8')
        assert not re.search(r'</f><v>[^<]+</v>', hoja), 'la copia conserva caché'
        xl = ExcelCompiler(filename=copia)

        def val(ref):
            with open(os.devnull, 'w') as dn, contextlib.redirect_stderr(dn):
                x = xl.evaluate(f"'{HOJA}'!{ref}")
            return x.item() if hasattr(x, 'item') else x

        e, b = p['eerste'], p['b']
        # Calentamiento: pycel solo recalcula tras set_value las fórmulas que ya evaluó.
        for row in wf[HOJA].iter_rows():
            for c in row:
                if c.data_type == 'f':
                    val(c.coordinate)
        bruto = [val(f'E{e + i}') for i in range(7)]
        assert [int(x) for x in bruto] == BRUTO, bruto
        assert all(val(f'E{e + i}') in (None, '') for i in range(7, 12))
        excl, incl, fc = val(f'B{b + 2}'), val(f'B{b + 4}'), val(f'B{b + 6}')
        assert (round(excl, 2), round(incl, 2), round(fc * 100, 1)) == (14.30, 15.59, 29.4), (excl, incl, fc)
        res = {'excl': excl, 'incl': incl, 'fc': fc}

        def poner(ref, x):
            val(ref)
            xl.set_value(f"'{HOJA}'!{ref}", x)

        # Lógica: fila vacía con 100 g y 25 % de uitval → 134 g (133,3 al gramo por exceso); uitval 100 % → aviso;
        # otro precio de carta → otra food cost; sin cambiar nada más.
        poner(f'B{e + 8}', 100)
        poner(f'D{e + 8}', 0.25)
        assert val(f'E{e + 8}') == 134, val(f'E{e + 8}')
        poner(f'D{e}', 1)
        assert val(f'E{e}') == UITVAL_KO, val(f'E{e}')
        poner(f'B{b + 5}', 16.50)
        assert round(val(f'B{b + 6}') * 100, 1) == 28.3, val(f'B{b + 6}')  # 4,29 / (16,50 / 1,09)
        poner(f'B{b + 3}', 0.21)
        assert round(val(f'B{b + 4}'), 2) == 17.30, val(f'B{b + 4}')  # 14,30 × 1,21
        # Casos con celdas vacías / texto: ni error ni 0 falso (patrón del gemelo FR)
        poner(f'B{e}', '180 g')  # netto como texto
        assert val(f'E{e}') in (None, ''), val(f'E{e}')
        poner(f'B{b + 5}', '')  # prijs op de kaart vacío
        assert val(f'B{b + 6}') in (None, ''), val(f'B{b + 6}')
        poner(f'B{b + 1}', '')  # food cost objetivo vacío
        assert val(f'B{b + 2}') in (None, '') and val(f'B{b + 4}') in (None, ''), (val(f'B{b + 2}'), val(f'B{b + 4}'))
        poner(f'B{b}', '')  # sin kostprijs
        assert val(f'B{b + 2}') in (None, '') and val(f'B{b + 6}') in (None, '')
        poner(f'B{b + 1}', 0.30)
        poner(f'B{b + 5}', 15.90)
        assert val(f'B{b + 2}') in (None, '') and val(f'B{b + 6}') in (None, '')
    return res


def textos_xlsx():
    """Todo el texto que ve el usuario: celdas, títulos de hoja y textos de las validaciones."""
    wf = load_workbook(SALIDA)
    out = list(wf.sheetnames)
    for ws in wf.worksheets:
        out += [c.value for row in ws.iter_rows() for c in row if isinstance(c.value, str)]
        for d in ws.data_validations.dataValidation:
            out += [x for x in (d.error, d.errorTitle, d.prompt, d.promptTitle, d.formula1) if x]
    return out


def gate_idioma():
    textos = textos_xlsx()
    todo = '\n'.join(textos)
    for w in PROHIBIDAS:
        m = re.search(rf'(?<![\w]){re.escape(w)}(?![\w])', todo, flags=re.IGNORECASE)
        assert not m, f'palabra española o prohibida «{w}»: …{todo[max(0, m.start() - 40):m.end() + 40]}…'
    raros = {ch for ch in todo if ord(ch) > 0x24F and ch not in TIPOGRAFIA_OK}
    assert not raros, f'caracteres fuera del alfabeto latino: {sorted(raros)}'
    return len(textos)


def gate_parche():
    r = subprocess.run([sys.executable, str(PARCHE), '--check', str(SALIDA)], capture_output=True, text=True, cwd=RAIZ)
    assert r.returncode == 0, r.stdout + r.stderr
    return r.stdout.strip().splitlines()[-1] if r.stdout.strip() else 'ok'


def main():
    p = generar()
    cache = inyectar(SALIDA)
    bruto = [int(x) for x in gate_fichero(p)]
    gate_pycel(p)
    n = gate_idioma()
    parche = gate_parche()
    print(f'OK {SALIDA.relative_to(RAIZ)} · {cache} · bruto {bruto} · '
          'Voorbeeld zalm: kostprijs per portie € 4,29 · verkoopprijs € 14,30 / € 15,59 / € 15,90 · 29,4 %')
    print(f'   gates: data_only OK · pycel sin caché OK (+4 casos de lógica, +5 de celdas vacías/texto) · idioma OK ({n} textos, sin español '
          f'ni «sporen») · parche --check: {parche}')


if __name__ == '__main__':
    main()
