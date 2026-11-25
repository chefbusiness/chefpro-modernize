#!/usr/bin/env python3
"""Scheda tecnica ricetta (IT), modello GRATIS — lead magnet de /it/blog/scheda-tecnica-ricetta.

Gemelo italiano de plantilla-receptuur-nl.py (misma hoja única, mismo diseño, mismas fórmulas y mismo ejemplo del
post: salmone alla piastra con verdure saltate), ADAPTADO:
  - IVA de la somministrazione di alimenti e bevande 10 %: prezzo di vendita 14,30 € IVA esclusa / 15,73 € IVA
    inclusa; in carta 15,90 € → food cost reale 29,7 %. Formato «4,29 €» (como calcolo-food-cost-excel-gratis);
  - los 14 allergeni con el nombre del anexo II del Reg. (UE) n. 1169/2011 y dos columnas para marcar con «X»:
    «Contiene» y «Può contenere (contaminazione crociata)», más «Tipo / ingrediente da cui proviene» (cereali y
    frutta a guscio piden «indica quale»). Nunca «tracce» (misma decisión que «sporen» en NL);
  - punti critici y conservazione remiten a «secondo il tuo piano di autocontrollo (HACCP)», sin ninguna cifra;
  - pasos de la preparazione en infinitivo, como el post; el resto del texto, de tú (tuteo);
  - pie con la guía IT y el calcolatore di food cost IT.
LowFruits IT (nov-2026): «scheda tecnica ricetta», «scheda tecnica piatto», «scheda tecnica di cucina».
Sale: astro-site/public/descargas/scheda-tecnica-ricetta-excel-gratis-aichef.xlsx
El xlsx pasa por inject_cache.py + caché «texto vacío» (como el DE/NL), un gate data_only, un gate pycel sobre una
COPIA sin caché (los números del post salen de las fórmulas, no de lo inyectado), un gate de idioma (nada de
neerlandés, español ni inglés; nada de «tracce») y parche_xml_xlsx.py --check. `/descargas/*` está en noindex
(netlify.toml). Sesión Claude Code, 25-nov-2026.
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
SALIDA = RAIZ / 'astro-site/public/descargas/scheda-tecnica-ricetta-excel-gratis-aichef.xlsx'
INJECT = RAIZ / 'scripts/productos-digitales/inject_cache.py'
PARCHE = RAIZ / 'scripts/productos-digitales/parche_xml_xlsx.py'
GUIDA = 'https://aichef.pro/it/blog/scheda-tecnica-ricetta'
CALCOLATORE = 'https://aichef.pro/it/calcolatore-food-cost-ristorante'
HOJA = 'Scheda tecnica'

NEGRO, DORADO, GRIS = '111111', 'FFD700', 'F3F3F3'
fino = Side(style='thin', color='BBBBBB')
borde = Border(left=fino, right=fino, top=fino, bottom=fino)
entrada = PatternFill('solid', fgColor='FFF8D6')
EUR = '#,##0.00 "€"'  # in un Excel in italiano: 4,29 € (come il modello di food cost IT)
PCT0, PCT1 = '0 %', '0.0 %'
CALO_KO = 'calo ≥ 100 %'

# (ingrediente, netto, unità, calo) — quelli del post.
INGREDIENTI = [
    ('Filetto di salmone fresco', 180, 'g', 0.18),
    ('Zucchine', 80, 'g', 0.10),
    ('Peperone rosso', 60, 'g', 0.20),
    ('Cipolla rossa', 40, 'g', 0.12),
    ('Aglio', 5, 'g', 0.10),
    ('Olio extravergine di oliva (EVO)', 15, 'ml', 0.0),
    ('Limone', 30, 'g', 0.0),
    ('Sale, pepe e prezzemolo (2 g · 0,5 g · 3 g)', None, 'g', 0.0),  # senza netto: la lorda resta vuota
]
LORDO = [220, 89, 75, 46, 6, 15, 30]
PASSI = [
    ("Tagliare le zucchine e il peperone a bastoncini regolari, la cipolla rossa a julienne fine e affettare l'aglio.",
     '5 min', ''),
    ("Saltare le verdure con l'aglio e 10 ml di olio EVO a fuoco vivo, senza che perdano il colore: devono restare "
     'cotte e croccanti, non stufate.', '4 min', 'fuoco vivo'),
    ('Segnare il salmone con i 5 ml di olio EVO rimanenti dal lato della pelle e finire la cottura dall\'altro lato.',
     '6 min', 'piastra ben calda'),
    ('Ritirare il salmone e lasciarlo riposare prima di impiattare.', '1 min', ''),
    ("Impiattare le verdure alla base, appoggiare il salmone sopra con la pelle verso l'alto e finire con lo spicchio "
     'di limone e il prezzemolo.', '2 min', ''),
]
ALLERGENI = [
    'Cereali contenenti glutine (grano, segale, orzo, avena, farro, kamut o ceppi ibridati: indica quale)',
    'Crostacei', 'Uova', 'Pesce', 'Arachidi', 'Soia', 'Latte (compreso il lattosio)',
    'Frutta a guscio (mandorle, nocciole, noci, noci di acagiù, noci di pecan, noci del Brasile, pistacchi, noci '
    'macadamia o del Queensland: indica quale)',
    'Sedano', 'Senape', 'Semi di sesamo', 'Anidride solforosa e solfiti (> 10 mg/kg o 10 mg/l espressi come SO2)',
    'Lupini', 'Molluschi',
]
assert len(ALLERGENI) == 14
HACCP = 'secondo il tuo piano di autocontrollo (HACCP)'
FOOTER_GUIDA = 'Modello gratuito di AI Chef Pro · Guida:'
FOOTER_CALC = 'Calcolatore di food cost gratuito (costo di ogni piatto):'
NOTA_IVA = 'Il food cost si calcola sempre sul prezzo di vendita IVA esclusa, mai su quello IVA inclusa.'

# Gate di lingua: parole neerlandesi (del gemello NL), spagnole (del generatore ES) e inglesi che non possono restare
# nell'xlsx, più «tracce». Escluse quelle che sono anche italiane (con, del, una, peso, carta, temperatura, contiene,
# iva, netto, per, food, cost…).
PROHIBIDAS = [
    # neerlandese
    'receptuur', 'portie', 'porties', 'uitval', 'bevat', 'bevatten', 'kan', 'kruisbesmetting', 'allergenen',
    'allergeen', 'gerecht', 'bereiding', 'stap', 'handeling', 'tijd', 'gaarpunt', 'bewaring', 'opmaak', 'opbouw',
    'servies', 'kostprijs', 'verkoopprijs', 'btw', 'excl', 'incl', 'zalm', 'groenten', 'grillplaat', 'vis', 'eieren',
    'melk', 'noten', 'selderij', 'mosterd', 'sesamzaad', 'lupine', 'weekdieren', 'schaaldieren', 'uw', 'het', 'een',
    'van', 'de', 'en', 'op', 'met', 'voor', 'zelf', 'werkelijke', 'beoogde', 'hoeveelheid', 'eenheid', 'bruto', 'jjjj',
    'sporen', 'hygiënecode', 'horeca', 'sjabloon', 'uitleg', 'gids', 'soja', 'gecontroleerd', 'welke',
    # spagnolo
    'ración', 'raciones', 'merma', 'alérgeno', 'alérgenos', 'trazas', 'elaboración', 'paso', 'conservación',
    'emplatado', 'montaje', 'menaje', 'plato', 'pvp', 'appcc', 'sanidad', 'escandallo', 'rellena', 'guía', 'plantilla',
    'ficha', 'técnica', 'cocina', 'salmón', 'pescado', 'fuego', 'plancha', 'aove', 'autor', 'fecha', 'versión',
    'cantidad', 'bruta', 'neta', 'unidad', 'tiempo', 'categoría', 'precio', 'objetivo', 'real', 'restauración',
    'españa', 'reglamento', 'limón', 'ajo', 'cebolla', 'pimiento', 'calabacín', 'sal', 'pimienta', 'perejil', 'verduras',
    'vida', 'útil', 'puntos', 'críticos', 'los', 'las', 'para', 'por', 'que', 'sin', 'y', 'el', 'dd', 'unos', 'suma',
    'netos', 'ingredientes', 'ración',
    # inglese
    'recipe', 'sheet', 'template', 'free', 'portion', 'portions', 'serving', 'servings', 'yield', 'waste', 'net',
    'gross', 'weight', 'price', 'vat', 'allergen', 'allergens', 'contains', 'may', 'contain', 'cross', 'contamination',
    'step', 'time', 'storage', 'plating', 'critical', 'points', 'salmon', 'grilled', 'vegetables', 'the', 'and', 'of',
    'with', 'your', 'fill', 'cells', 'yellow', 'guide', 'calculator', 'cereals', 'containing', 'gluten', 'eggs', 'fish',
    'peanuts', 'milk', 'nuts', 'celery', 'mustard', 'sesame', 'seeds', 'sulphur', 'sulfites', 'lupin', 'molluscs',
    'crustaceans', 'dish', 'checked', 'by', 'date', 'version', 'author', 'category', 'traces', 'excluding', 'including',
    'actual', 'target', 'eu', 'shrink', 'trim',
    # italiano vietato
    'tracce',
]
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


def formula_lordo(f):
    # lordo = netto / (1 − calo), arrotondato al grammo per eccesso; calo ≥ 100 % → avviso (come il gemello FR)
    return f'=IF(OR(B{f}="",NOT(ISNUMBER(B{f}))),"",IF(N(D{f})>=1,"{CALO_KO}",ROUNDUP(B{f}/(1-N(D{f})),0)))'


def generar():
    wb = Workbook()
    ws = wb.active
    ws.title = HOJA
    ws['A1'] = 'Scheda tecnica ricetta'
    ws['A1'].font = Font(bold=True, size=16, color=DORADO)
    ws['A1'].fill = PatternFill('solid', fgColor=NEGRO)
    ws.merge_cells('A1:F1')
    ws['A2'] = 'Compila le celle gialle. La quantità lorda e il prezzo di vendita si calcolano da soli.'
    ws['A2'].font = Font(italic=True, color='555555')
    ws.merge_cells('A2:F2')

    # Dati generali (righe 5-12)
    titulo(ws, 4, 'Dati generali')
    dati = [('Piatto', 'Salmone alla piastra con verdure saltate'), ('Categoria', 'Pesci'),
            ('Numero di porzioni', 1), ('Peso per porzione', 'Circa 410 g a crudo (somma dei netti)'),
            ('Tempo di preparazione', '20 min'), ('Autore', 'Chef di cucina'), ('Verificata da', ''),
            ('Data e versione', 'gg-mm-aaaa · v1.0')]
    for i, (k, v) in enumerate(dati):
        f = 5 + i
        celda(ws, f, 1, k, negrita=True)
        celda(ws, f, 2, v if v != '' else None, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=2, end_row=f, end_column=6)

    # Ingredienti (titolo riga 14, intestazione 15, dati dalla 16)
    titulo(ws, 14, 'Ingredienti (per porzione)')
    intest = ['Ingrediente', 'Quantità netta (nel piatto)', 'Unità', 'Calo (%)', 'Quantità lorda (da acquistare)',
              'Allergeni di questo ingrediente']
    for col, txt in enumerate(intest, start=1):
        c = celda(ws, 15, col, txt, negrita=True)
        c.fill = PatternFill('solid', fgColor=GRIS)
    ws.row_dimensions[15].height = 47
    primo = 16
    righe = INGREDIENTI + [None] * 4
    for i, item in enumerate(righe):
        f = primo + i
        if item:
            n, netto, unita, calo = item
            celda(ws, f, 1, n, es_entrada=True)
            celda(ws, f, 2, netto, '0', es_entrada=True)
            celda(ws, f, 3, unita, es_entrada=True)
            celda(ws, f, 4, calo, PCT0, es_entrada=True)
            celda(ws, f, 6, 'Pesce' if n == 'Filetto di salmone fresco' else None, es_entrada=True)
            alto(ws, f, (n, 33))
        else:
            for col in (1, 2, 3, 4, 6):
                celda(ws, f, col, None, PCT0 if col == 4 else ('0' if col == 2 else None), es_entrada=True)
        celda(ws, f, 5, formula_lordo(f), '0')
    ultimo_ing = primo + len(righe) - 1
    dvc = DataValidation(type='decimal', operator='between', formula1='0', formula2='0.99',
                         error='Il calo va da 0 % a 99 % (scrivi 20 % oppure 0,2).', errorTitle='Calo',
                         showErrorMessage=True)
    ws.add_data_validation(dvc)
    dvc.add(f'D{primo}:D{ultimo_ing}')

    # Preparazione
    fp = ultimo_ing + 2
    titulo(ws, fp, 'Preparazione passo passo')
    for col, txt in enumerate(['Passo', 'Operazione', '', '', 'Tempo', 'Temperatura / punto di cottura'], start=1):
        if txt:
            c = celda(ws, fp + 1, col, txt, negrita=True)
            c.fill = PatternFill('solid', fgColor=GRIS)
    ws.merge_cells(start_row=fp + 1, start_column=2, end_row=fp + 1, end_column=4)
    passi = PASSI + [('', '', '')] * 3
    for i, (txt, tempo, temp) in enumerate(passi):
        f = fp + 2 + i
        celda(ws, f, 1, i + 1)
        celda(ws, f, 2, txt or None, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=2, end_row=f, end_column=4)
        celda(ws, f, 5, tempo or None, es_entrada=True)
        celda(ws, f, 6, temp or None, es_entrada=True)
        # 48 pt di base (spazio per scrivere); di più se il testo del passo supera 3 righe in B:D (~37 caratteri)
        ws.row_dimensions[f].height = max(48, 15 * len(textwrap.wrap(txt, 37)) + 2) if txt else 48

    # Allergeni: due colonne da segnare con X (Contiene / Può contenere) + tipo
    fa = fp + 2 + len(passi) + 1
    titulo(ws, fa, 'Allergeni (Reg. (UE) n. 1169/2011, allegato II): metti una X nella colonna giusta')
    for c0, c1, txt in ((1, 1, 'Allergene'), (2, 2, 'Contiene'), (3, 4, 'Può contenere (contaminazione crociata)'),
                        (5, 6, 'Tipo / ingrediente da cui proviene')):
        c = celda(ws, fa + 1, c0, txt, negrita=True)
        c.fill = PatternFill('solid', fgColor=GRIS)
        if c1 > c0:
            celda(ws, fa + 1, c1).fill = PatternFill('solid', fgColor=GRIS)
            ws.merge_cells(start_row=fa + 1, start_column=c0, end_row=fa + 1, end_column=c1)
    ws.row_dimensions[fa + 1].height = 32
    dvx = DataValidation(type='list', formula1='"X"', allow_blank=True, showErrorMessage=True,
                         errorTitle='Allergeni', error='Scegli X oppure lascia vuota la cella.')
    ws.add_data_validation(dvx)
    primo_all = fa + 2
    for i, a in enumerate(ALLERGENI):
        f = primo_all + i
        celda(ws, f, 1, a)
        celda(ws, f, 2, 'X' if a == 'Pesce' else None, es_entrada=True).alignment = Alignment(horizontal='center',
                                                                                            vertical='top')
        celda(ws, f, 3, None, es_entrada=True).alignment = Alignment(horizontal='center', vertical='top')
        celda(ws, f, 4, None, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=3, end_row=f, end_column=4)
        celda(ws, f, 5, 'Filetto di salmone fresco' if a == 'Pesce' else None, es_entrada=True)
        celda(ws, f, 6, None, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=5, end_row=f, end_column=6)
        alto(ws, f, (a, 33))
    ultimo_all = primo_all + len(ALLERGENI) - 1
    dvx.add(f'B{primo_all}:C{ultimo_all}')

    # Conservazione e punti critici
    fc = ultimo_all + 2
    titulo(ws, fc, 'Conservazione e punti critici di controllo (CCP)')
    for i, (k, v) in enumerate([
            ('Conservazione', 'Salmone in refrigerazione fino al momento di segnarlo; verdura tagliata coperta e in '
                              f'frigo. Tempi e temperature {HACCP}.'),
            ('Punti critici (CCP)', 'Catena del freddo del pesce fino al momento di segnarlo; cottura del salmone. '
                                    f'Limiti e chi li verifica: {HACCP}.'),
            ('Vita utile delle preparazioni precedenti', f'{HACCP[0].upper()}{HACCP[1:]}.')]):
        f = fc + 1 + i
        celda(ws, f, 1, k, negrita=True)
        celda(ws, f, 2, v, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=2, end_row=f, end_column=6)
        alto(ws, f, (k, 33), (v, 72))
    fi = fc + 5
    titulo(ws, fi, 'Impiattamento')
    for i, (k, v) in enumerate([
            ('Montaggio e guarnizione', "Verdure al centro come base, salmone sopra con la pelle verso l'alto, uno "
                                        'spicchio di limone e prezzemolo tritato.'),
            ('Stoviglie', 'Piatto piano.'), ('Foto di riferimento', 'Incolla qui la foto del piatto finito.')]):
        f = fi + 1 + i
        celda(ws, f, 1, k, negrita=True)
        celda(ws, f, 2, v, es_entrada=True)
        ws.merge_cells(start_row=f, start_column=2, end_row=f, end_column=6)
        alto(ws, f, (k, 33), (v, 72))

    # Costo → prezzo di vendita
    fk = fi + 5
    titulo(ws, fk, 'Costo e prezzo di vendita')
    b = fk + 1
    blocco = [
        ('Costo per porzione (dal tuo calcolo del food cost)', 4.29, EUR, True),
        ('Food cost obiettivo (%)', 0.30, PCT0, True),
        ('Prezzo di vendita IVA esclusa', f'=IF(OR(B{b}="",N(B{b + 1})=0),"",B{b}/B{b + 1})', EUR, False),
        ('IVA (somministrazione di alimenti e bevande in Italia: 10 %)', 0.10, PCT0, True),
        ('Prezzo di vendita IVA inclusa', f'=IF(B{b + 2}="","",B{b + 2}*(1+N(B{b + 3})))', EUR, False),
        ('Prezzo in carta (IVA inclusa, arrotondato a tua scelta)', 15.90, EUR, True),
        ('Food cost reale a quel prezzo (%)', f'=IF(OR(B{b}="",N(B{b + 5})=0),"",B{b}/(B{b + 5}/(1+N(B{b + 3}))))', PCT1, False),
    ]
    for i, (k, v, fmt, ent) in enumerate(blocco):
        celda(ws, b + i, 1, k, negrita=True)
        c = celda(ws, b + i, 2, v, fmt, es_entrada=ent, negrita=True)
        if not ent:
            c.fill = PatternFill('solid', fgColor=GRIS)
        alto(ws, b + i, (k, 33))
    fn = b + len(blocco) + 1
    ws.cell(row=fn, column=1, value=NOTA_IVA).font = Font(italic=True, color='555555')
    ws.merge_cells(start_row=fn, start_column=1, end_row=fn, end_column=6)
    ws.cell(row=fn + 1, column=1, value=FOOTER_GUIDA)
    ws.cell(row=fn + 1, column=2, value=GUIDA).hyperlink = GUIDA
    ws.cell(row=fn + 2, column=1, value=FOOTER_CALC)
    ws.cell(row=fn + 2, column=2, value=CALCOLATORE).hyperlink = CALCOLATORE
    for f in (fn + 1, fn + 2):
        ws.cell(row=f, column=2).font = Font(color='0563C1', underline='single')
        # la B è occupata dall'URL: il testo della A non può sconfinare, va a capo dentro la sua colonna
        ws.cell(row=f, column=1).alignment = Alignment(wrap_text=True, vertical='top')
        ws.cell(row=f, column=2).alignment = Alignment(vertical='top')
        alto(ws, f, (ws.cell(row=f, column=1).value, 33))

    for col, w in {'A': 34, 'B': 16, 'C': 10, 'D': 11, 'E': 16, 'F': 24}.items():
        ws.column_dimensions[col].width = w
    ws.page_setup.orientation = 'portrait'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    wb.save(SALIDA)
    return {'primo': primo, 'ultimo_ing': ultimo_ing, 'primo_all': primo_all, 'ultimo_all': ultimo_all,
            'b': b, 'fn': fn}


# ---------------------------------------------------------------- caché
def cache_texto_vacio(ruta):
    """inject_cache.py no inyecta el resultado «""»: la celda se queda con caché vacía (<v/>, que un visor sin
    recálculo enseña como 0 en la quantità lorda). Se escribe como Excel (t="str" + <v></v>), tocando solo el XML
    de las hojas (copiado del gemelo DE/NL)."""
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
    e, b = p['primo'], p['b']
    # allergeni: i 14 nomi ufficiali, una sola lista «X» su Contiene + Può contenere; esempio = solo pesce
    assert [ws.cell(row=p['primo_all'] + i, column=1).value for i in range(14)] == ALLERGENI
    assert ws.cell(row=p['primo_all'] - 1, column=2).value == 'Contiene'
    assert ws.cell(row=p['primo_all'] - 1, column=3).value == 'Può contenere (contaminazione crociata)'
    lista = [d for d in ws.data_validations.dataValidation if d.type == 'list']
    assert len(lista) == 1 and lista[0].formula1 == '"X"', lista
    assert str(lista[0].sqref) == f'B{p["primo_all"]}:C{p["ultimo_all"]}', lista[0].sqref
    dec = [d for d in ws.data_validations.dataValidation if d.type == 'decimal']
    assert len(dec) == 1 and str(dec[0].sqref) == f'D{e}:D{p["ultimo_ing"]}', dec
    assert all(d.showErrorMessage for d in ws.data_validations.dataValidation)
    segni = {ws.cell(row=p['primo_all'] + i, column=c).value for i in range(14) for c in (2, 3)} - {None}
    assert segni == {'X'} and ws.cell(row=p['primo_all'] + ALLERGENI.index('Pesce'), column=2).value == 'X'
    assert sum(ws.cell(row=p['primo_all'] + i, column=c).value == 'X' for i in range(14) for c in (2, 3)) == 1
    # blocco prezzo: IVA 10 %, 4,29, 30 %, 15,90; formato euro
    assert (ws[f'B{b}'].value, ws[f'B{b + 1}'].value, ws[f'B{b + 3}'].value, ws[f'B{b + 5}'].value) == \
        (4.29, 0.30, 0.10, 15.90)
    assert all(ws[f'B{b + i}'].number_format == EUR for i in (0, 2, 4, 5))
    # piè di pagina: guida IT e calcolatore IT, con collegamento
    destinos = {c.hyperlink.target for row in ws.iter_rows() for c in row if c.hyperlink}
    assert destinos == {GUIDA, CALCOLATORE}, destinos
    assert ws.cell(row=p['fn'] + 1, column=1).value == FOOTER_GUIDA
    # data_only = quello che vede un visualizzatore che non ricalcola
    wv = load_workbook(SALIDA, data_only=True)[HOJA]
    lordo = [wv.cell(row=e + i, column=5).value for i in range(7)]
    assert all(isinstance(x, (int, float)) for x in lordo), lordo
    assert [int(x) for x in lordo] == LORDO, lordo
    assert all(wv.cell(row=e + i, column=5).value in (None, '') for i in range(7, 12))  # sale… e 4 righe vuote
    escl, incl, fc = (wv[f'B{b + 2}'].value, wv[f'B{b + 4}'].value, wv[f'B{b + 6}'].value)
    assert (round(escl, 2), round(incl, 2), round(fc * 100, 1)) == (14.30, 15.73, 29.7), (escl, incl, fc)
    return lordo


def gate_pycel(p):
    """Le cifre del post escono dalle FORMULE: copia senza cache (openpyxl non conserva i <v>) + pycel."""
    logging.disable(logging.CRITICAL)
    from pycel import ExcelCompiler
    wf = load_workbook(SALIDA)
    with tempfile.TemporaryDirectory() as tmp:
        copia = str(Path(tmp) / 'senza-cache.xlsx')
        wf.save(copia)
        with zipfile.ZipFile(copia) as z:
            hoja = z.read('xl/worksheets/sheet1.xml').decode('utf-8')
        assert not re.search(r'</f><v>[^<]+</v>', hoja), 'la copia conserva la cache'
        xl = ExcelCompiler(filename=copia)

        def val(ref):
            with open(os.devnull, 'w') as dn, contextlib.redirect_stderr(dn):
                x = xl.evaluate(f"'{HOJA}'!{ref}")
            return x.item() if hasattr(x, 'item') else x

        e, b = p['primo'], p['b']
        # Riscaldamento: pycel ricalcola dopo set_value solo le formule che ha già valutato.
        for row in wf[HOJA].iter_rows():
            for c in row:
                if c.data_type == 'f':
                    val(c.coordinate)
        lordo = [val(f'E{e + i}') for i in range(7)]
        assert [int(x) for x in lordo] == LORDO, lordo
        assert all(val(f'E{e + i}') in (None, '') for i in range(7, 12))
        escl, incl, fc = val(f'B{b + 2}'), val(f'B{b + 4}'), val(f'B{b + 6}')
        assert (round(escl, 2), round(incl, 2), round(fc * 100, 1)) == (14.30, 15.73, 29.7), (escl, incl, fc)
        res = {'escl': escl, 'incl': incl, 'fc': fc}

        def poner(ref, x):
            val(ref)
            xl.set_value(f"'{HOJA}'!{ref}", x)

        # Logica: riga vuota con 100 g e 25 % di calo → 134 g (133,3 arrotondato per eccesso); calo 100 % → avviso;
        # altro prezzo in carta → altro food cost; altra IVA → altro prezzo IVA inclusa.
        poner(f'B{e + 8}', 100)
        poner(f'D{e + 8}', 0.25)
        assert val(f'E{e + 8}') == 134, val(f'E{e + 8}')
        poner(f'D{e}', 1)
        assert val(f'E{e}') == CALO_KO, val(f'E{e}')
        poner(f'B{b + 5}', 16.50)
        assert round(val(f'B{b + 6}') * 100, 1) == 28.6, val(f'B{b + 6}')  # 4,29 / (16,50 / 1,10)
        poner(f'B{b + 3}', 0.22)
        assert round(val(f'B{b + 4}'), 2) == 17.45, val(f'B{b + 4}')  # 14,30 × 1,22
        # Casi con celle vuote / testo: né errore né 0 falso (schema del gemello FR)
        poner(f'B{e}', '180 g')  # netto come testo
        assert val(f'E{e}') in (None, ''), val(f'E{e}')
        poner(f'B{b + 5}', '')  # prezzo in carta vuoto
        assert val(f'B{b + 6}') in (None, ''), val(f'B{b + 6}')
        poner(f'B{b + 1}', '')  # food cost obiettivo vuoto
        assert val(f'B{b + 2}') in (None, '') and val(f'B{b + 4}') in (None, ''), (val(f'B{b + 2}'), val(f'B{b + 4}'))
        poner(f'B{b}', '')  # senza costo per porzione
        assert val(f'B{b + 2}') in (None, '') and val(f'B{b + 6}') in (None, '')
        poner(f'B{b + 1}', 0.30)
        poner(f'B{b + 5}', 15.90)
        assert val(f'B{b + 2}') in (None, '') and val(f'B{b + 6}') in (None, '')
    return res


def textos_xlsx():
    """Tutto il testo che vede l'utente: celle, titoli dei fogli e testi delle convalide."""
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
        assert not m, f'parola straniera o vietata «{w}»: …{todo[max(0, m.start() - 40):m.end() + 40]}…'
    raros = {ch for ch in todo if ord(ch) > 0x24F and ch not in TIPOGRAFIA_OK}
    assert not raros, f'caratteri fuori dall\'alfabeto latino: {sorted(raros)}'
    return len(textos)


def gate_parche():
    r = subprocess.run([sys.executable, str(PARCHE), '--check', str(SALIDA)], capture_output=True, text=True, cwd=RAIZ)
    assert r.returncode == 0, r.stdout + r.stderr
    return r.stdout.strip().splitlines()[-1] if r.stdout.strip() else 'ok'


def main():
    p = generar()
    cache = inyectar(SALIDA)
    lordo = [int(x) for x in gate_fichero(p)]
    gate_pycel(p)
    n = gate_idioma()
    parche = gate_parche()
    print(f'OK {SALIDA.relative_to(RAIZ)} · {cache} · lordo {lordo} · '
          'Esempio salmone: costo per porzione € 4,29 · 14,30 / 15,73 / 15,90 · 29,7 %')
    print(f'   gates: data_only OK · pycel sin caché OK (+4 casos de lógica, +5 de celdas vacías/texto) · idioma OK '
          f'({n} textos, sin neerlandés, español, inglés ni «tracce») · parche --check: {parche}')


if __name__ == '__main__':
    main()
