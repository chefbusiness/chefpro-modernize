#!/usr/bin/env python3
"""Calcolo food cost (scandaglio), plantilla Excel GRATIS (IT) — lead magnet de /it/blog/food-cost.

Keywords IT (nov-2026): «calcolo food cost» 260/mes, «calcolare food cost» 260, «calcolo food cost excel» 40,
«food cost tabella». Duplicado y adaptado del gemelo ES (plantilla-escandallo-gratis.py) con el estilo FR/DE
(plantilla-fiche-technique-fr.py, plantilla-wareneinsatz-rechner-de.py).
Sale: astro-site/public/descargas/calcolo-food-cost-excel-gratis-aichef.xlsx (sin PDF) — 3 hojas:
  «Esempio»          el ejemplo EXACTO del post: tagliatelle al ragù, una porción, 1,80 € · 12,00 € IVA inclusa
                     → 10,91 € IVA esclusa → food cost 16,5 % · margine 9,11 €.
  «Scandaglio vuoto» la misma estructura vacía (15 filas + forfait). Hoja activa.
  «Pasta fresca»     coste de la pasta fresca all'uovo hecha en casa con precios indicativos editables
                     (4,20 € · 2,63 €/kg · porción 0,32 € frente a 0,54 € comprada).
Las cantidades son NETAS (g) y la columna «Quantità lorda» = netta ÷ (1 − calo), redondeada al gramo por arriba;
el coste se calcula sobre la lorda. Un calo ≥ 100 % NO desaparece del total: la lorda enseña «calo ≥ 100 %», el
coste de la fila da error (aunque falte el precio) y el error llega al coste por porción, al food cost y al margen.
Sin datos del sector salvo los dos rangos orientativos del post (25-35 % / 20-25 %).
El xlsx pasa por inject_cache.py (valores calculados), un gate data_only, un gate de lógica con pycel (rellena la
hoja vacía en memoria) y parche_xml_xlsx.py --check. `/descargas/*` está en noindex (netlify.toml).
"""
import contextlib
import logging
import os
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

RAIZ = Path(__file__).resolve().parents[2]
XLSX = RAIZ / 'astro-site/public/descargas/calcolo-food-cost-excel-gratis-aichef.xlsx'
ARTICOLO = 'https://aichef.pro/it/blog/food-cost'

NERO, ORO, GRIGIO = '111111', 'FFD700', 'F3F3F3'
sottile = Side(style='thin', color='BBBBBB')
bordo = Border(left=sottile, right=sottile, top=sottile, bottom=sottile)
input_fill = PatternFill('solid', fgColor='FFF8D6')
grigio_fill = PatternFill('solid', fgColor=GRIGIO)
errore_fill = PatternFill('solid', fgColor='FBE3E3')
EUR = '#,##0.00 "€"'
GR = '#,##0'
NB = ' '  # spazio non separabile tra cifra e unità («25 %», «1,80 €»)
PCT0 = '0' + NB + '%'
PCT1 = '0.0' + NB + '%'
CALO_KO = 'calo ≥' + NB + '100' + NB + '%'

# Esempio del post: (ingrediente, quantità netta g, calo, prezzo d'acquisto IVA esclusa €/kg)
ESEMPIO = [
    ('Tagliatelle fresche', 120, 0, 4.50),
    ('Ragù di manzo', 150, 0, 6.00),
    ('Parmigiano Reggiano', 10, 0, 22.00),
    ('Burro', 10, 0, 9.00),
]
FORFAIT = ('Sale, pepe, varie', 0.05)
PREZZO_CARTA, IVA = 12.00, 0.10
IVA_NOTA = f'In Italia la somministrazione al tavolo sconta l\'IVA al 10{NB}%, vino compreso.'
FOOTER = [
    'Il food cost si calcola sul prezzo IVA esclusa, mai su quello in carta.',
    f'Riferimenti orientativi: ristorazione tradizionale tra il 25{NB}% e il 35{NB}%, pizza tra il 20{NB}% e il '
    f'25{NB}% (vedi l\'articolo).',
]
NOTA_MANODOPERA = ('Il costo della manodopera e il calo dell\'impasto non sono inclusi: il risparmio sulla materia '
                   'prima va confrontato con il tempo di lavoro.')
PCT_AMMESSE = {'10', '20', '25', '35', '100'}  # IVA, i due riferimenti del post e il messaggio di calo

# Righe fisse dei due fogli di scandaglio (stessa struttura → stesse celle)
R_PIATTO, R_PORZ = 4, 5
R_TIT_ING, R_INT = 7, 8
R_ING1 = 9
N_RIGHE = 15
R_INGN = R_ING1 + N_RIGHE - 1      # 23
R_FORF = R_INGN + 1                # 24 · sale, pepe, varie (forfait)
R_NOTA_CALO = R_FORF + 1           # 25
R_TIT_PREZZO = R_NOTA_CALO + 2     # 27
R_COSTO, R_CARTA, R_IVA, R_NETTO, R_FC, R_MARG = range(R_TIT_PREZZO + 1, R_TIT_PREZZO + 7)  # 28-33
R_FORMULA = R_MARG + 2             # 35
R_FOOTER = R_FORMULA + 3           # 38
COSTI = f'F{R_ING1}:F{R_FORF}'

# Righe fisse di «Pasta fresca»
P_FARINA, P_UOVA = 6, 7
P_PESO, P_COSTO, P_KG, P_PORZ, P_CASA = 11, 12, 13, 14, 15
P_ACQ_PREZZO, P_ACQ_PORZ, P_DIFF = 18, 19, 20


# ---------------------------------------------------------------- utilità di stile
def barra(ws, riga, testo, fino):
    c = ws.cell(row=riga, column=1, value=testo)
    c.font = Font(bold=True, color='FFFFFF')
    c.fill = PatternFill('solid', fgColor=NERO)
    ws.merge_cells(start_row=riga, start_column=1, end_row=riga, end_column=fino)


def testata(ws, titolo, istruzioni, fino):
    ws['A1'] = titolo
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws['A1'].fill = PatternFill('solid', fgColor=NERO)
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=fino)
    ws.row_dimensions[1].height = 26
    ws['A2'] = istruzioni
    ws['A2'].font = Font(italic=True, color='555555')
    ws['A2'].alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=fino)
    ws.row_dimensions[2].height = 30


def cella(ws, r, c, valore=None, fmt=None, inp=False, grassetto=False, grigio=False):
    z = ws.cell(row=r, column=c, value=valore)
    z.border = bordo
    if fmt:
        z.number_format = fmt
    if inp:
        z.fill = input_fill
    elif grigio:
        z.fill = grigio_fill
    if grassetto:
        z.font = Font(bold=True)
    z.alignment = Alignment(wrap_text=True, vertical='center')
    return z


def intestazioni(ws, riga, testi, altezza=48):
    for col, txt in enumerate(testi, start=1):
        z = cella(ws, riga, col, txt, grassetto=True, grigio=True)
        z.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
    ws.row_dimensions[riga].height = altezza


def nota(ws, riga, testo, fino, altezza=None, corsivo=True, fill=None, col=1):
    c = ws.cell(row=riga, column=col, value=testo)
    c.font = Font(italic=corsivo, color='555555')
    c.alignment = Alignment(wrap_text=True, vertical='top')
    if fill:
        c.fill = fill
    ws.merge_cells(start_row=riga, start_column=col, end_row=riga, end_column=fino)
    if altezza:
        ws.row_dimensions[riga].height = altezza


def dv_numero(ws, tipo='decimal', minimo='0', titolo='Valore non valido',
              msg='Scrivi solo il numero, uguale o maggiore di 0 (per esempio 4,50).'):
    dv = DataValidation(type=tipo, operator='greaterThanOrEqual', formula1=minimo, allow_blank=True,
                        showErrorMessage=True, errorTitle=titolo, error=msg)
    ws.add_data_validation(dv)
    return dv


def dv_percentuale(ws, titolo, msg):
    dv = DataValidation(type='decimal', operator='between', formula1='0', formula2='0.99', allow_blank=True,
                        showErrorMessage=True, errorTitle=titolo, error=msg)
    ws.add_data_validation(dv)
    return dv


def footer(ws, riga, fino):
    """Note generali + link all'articolo, in fondo a ogni foglio."""
    barra(ws, riga, 'Da ricordare', fino)
    for i, txt in enumerate(FOOTER):
        nota(ws, riga + 1 + i, txt, fino, altezza=30 if i else None, corsivo=False)
    r = riga + 1 + len(FOOTER)
    ws.cell(row=r, column=1, value='Guida completa con l\'esempio spiegato:').font = Font(bold=True)
    link = ws.cell(row=r, column=2, value=ARTICOLO)
    link.hyperlink = ARTICOLO
    link.font = Font(color='0563C1', underline='single')
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=fino)
    nota(ws, r + 1, 'Modello gratuito di AI Chef Pro (aichef.pro): puoi copiarlo e adattarlo ai tuoi piatti.', fino)


def stampa(ws, larghezze):
    for col, w in larghezze.items():
        ws.column_dimensions[col].width = w
    ws.sheet_view.showGridLines = False
    ws.page_setup.orientation = 'portrait'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True


# ---------------------------------------------------------------- fogli
def foglio_scandaglio(wb, nome, esempio):
    ws = wb.create_sheet(nome)
    if esempio:
        istr = ('Esempio dell\'articolo: lo scandaglio delle tagliatelle al ragù, una porzione. Per i tuoi piatti '
                'usa il foglio «Scandaglio vuoto».')
    else:
        istr = ('Compila solo le celle gialle: quantità lorda, costo, prezzo IVA esclusa, food cost e margine si '
                'calcolano da soli.')
    testata(ws, 'Calcolo food cost: lo scandaglio del piatto', istr, 6)

    cella(ws, R_PIATTO, 1, 'Piatto', grassetto=True)
    cella(ws, R_PIATTO, 2, 'Tagliatelle al ragù' if esempio else None, inp=True)
    for c in range(3, 7):
        ws.cell(row=R_PIATTO, column=c).border = bordo
    ws.merge_cells(start_row=R_PIATTO, start_column=2, end_row=R_PIATTO, end_column=6)
    cella(ws, R_PORZ, 1, 'Porzioni', grassetto=True)
    porz = cella(ws, R_PORZ, 2, 1 if esempio else None, '0', inp=True)
    dv_numero(ws, 'whole', '1', 'Porzioni', 'Scrivi un numero intero di porzioni, da 1 in su.').add(porz.coordinate)
    nota(ws, R_PORZ, 'Se lo scandaglio è per più porzioni, il costo per porzione è il totale diviso per le porzioni.',
         6, altezza=30, col=3)

    barra(ws, R_TIT_ING, 'Ingredienti (quantità per il numero di porzioni indicato)', 6)
    intestazioni(ws, R_INT, ['Ingrediente', 'Quantità netta (g)', 'Calo (%)', 'Quantità lorda (g)',
                             'Prezzo d\'acquisto IVA esclusa (€/kg)', 'Costo (€)'])
    dv_qta = dv_numero(ws, msg='Scrivi la quantità in grammi, solo il numero (per esempio 120).')
    dv_calo = dv_percentuale(ws, 'Calo', 'Il calo va da 0 % a 99 % (scrivi 20 % oppure 0,2).')
    dv_eur = dv_numero(ws)
    righe = (ESEMPIO if esempio else []) + [None] * (N_RIGHE - (len(ESEMPIO) if esempio else 0))
    for i, item in enumerate(righe):
        r = R_ING1 + i
        nome_i, netta, calo, prezzo = item if item else (None, None, None, None)
        cella(ws, r, 1, nome_i, inp=True)
        dv_qta.add(cella(ws, r, 2, netta, GR, inp=True).coordinate)
        dv_calo.add(cella(ws, r, 3, calo, PCT0, inp=True).coordinate)
        dv_eur.add(cella(ws, r, 5, prezzo, EUR, inp=True).coordinate)
        # lorda = netta ÷ (1 − calo), al grammo per eccesso; calo ≥ 100 % → messaggio (non sparisce dal totale)
        cella(ws, r, 4, f'=IF(B{r}="","",IF(N(C{r})>=1,"{CALO_KO}",ROUNDUP(B{r}/(1-N(C{r})),0)))', GR, grigio=True)
        # costo = lorda × prezzo, ai centesimi come la tabella del post. Se la lorda è il messaggio di calo,
        # il costo va in errore anche senza prezzo: l'errore arriva al totale invece di scomparire.
        cella(ws, r, 6, f'=IF(OR(D{r}="",AND(ISNUMBER(D{r}),E{r}="")),"",ROUND(D{r}/1000*E{r},2))', EUR, grigio=True)
    # Riga forfait (sale, pepe, varie): il costo si scrive a mano, come nel post.
    cella(ws, R_FORF, 1, FORFAIT[0], inp=True)
    for c in range(2, 6):
        cella(ws, R_FORF, c)
    ws.cell(row=R_FORF, column=2, value='Forfait: scrivi il costo direttamente nella colonna «Costo».').font = \
        Font(italic=True, color='555555')
    ws.merge_cells(start_row=R_FORF, start_column=2, end_row=R_FORF, end_column=5)
    dv_eur.add(cella(ws, R_FORF, 6, FORFAIT[1] if esempio else None, EUR, inp=True).coordinate)
    nota(ws, R_NOTA_CALO, f'Se nella colonna «Quantità lorda» compare «{CALO_KO}», correggi il calo: costo, food cost '
                          'e margine restano in errore finché non lo fai.', 6, altezza=30)
    ws.conditional_formatting.add(
        f'E{R_ING1}:E{R_INGN}',
        FormulaRule(formula=[f'AND($B{R_ING1}<>"",$E{R_ING1}="")'], fill=errore_fill))
    ws.conditional_formatting.add(
        f'D{R_ING1}:F{R_INGN}',
        FormulaRule(formula=[f'OR(ISERROR($F{R_ING1}),AND($D{R_ING1}<>"",NOT(ISNUMBER($D{R_ING1}))))'],
                    fill=errore_fill, font=Font(bold=True, color='9C1C1C')))

    barra(ws, R_TIT_PREZZO, 'Costo, prezzo e food cost', 6)
    c, carta, iva, netto = f'B{R_COSTO}', f'B{R_CARTA}', f'B{R_IVA}', f'B{R_NETTO}'
    blocco = [
        (R_COSTO, 'Costo materie prime per porzione',
         f'=IF(AND(COUNT({COSTI})=0,NOT(ISERROR(SUM({COSTI})))),"",'
         f'ROUND(SUM({COSTI})/IF(N(B{R_PORZ})>1,B{R_PORZ},1),2))', EUR, False),
        (R_CARTA, 'Prezzo in carta IVA inclusa', PREZZO_CARTA if esempio else None, EUR, True),
        (R_IVA, 'IVA', IVA, PCT0, True),
        (R_NETTO, 'Prezzo di vendita IVA esclusa',
         f'=IF(OR(N({carta})<=0,{iva}=""),"",ROUND({carta}/(1+N({iva})),2))', EUR, False),
        (R_FC, 'Food cost (costo ÷ prezzo IVA esclusa)', f'=IF(OR({c}="",{netto}=""),"",{c}/{netto})', PCT1, False),
        (R_MARG, 'Margine sulle materie prime per porzione', f'=IF(OR({c}="",{netto}=""),"",{netto}-{c})', EUR, False),
    ]
    for r, etichetta, valore, fmt, inp in blocco:
        cella(ws, r, 1, etichetta, grassetto=True)
        z = cella(ws, r, 2, valore, fmt, inp=inp, grassetto=True, grigio=not inp)
        ws.row_dimensions[r].height = 20
        if r == R_CARTA:
            dv_eur.add(z.coordinate)
        if r == R_IVA:
            dv_percentuale(ws, 'IVA', 'Scrivi l\'aliquota in percentuale, per esempio 10 % (oppure 0,1).').add(z.coordinate)
    nota(ws, R_IVA, IVA_NOTA, 6, col=3)
    ws.row_dimensions[R_IVA].height = 30
    ws.conditional_formatting.add(f'B{R_COSTO}:B{R_MARG}', FormulaRule(
        formula=[f'ISERROR(B{R_COSTO})'], fill=errore_fill, font=Font(bold=True, color='9C1C1C')))
    nota(ws, R_FORMULA, 'Food cost = costo materie prime per porzione ÷ prezzo di vendita IVA esclusa × 100. Il '
                        'margine copre tutto il resto: personale, affitto, energia, marketing, attrezzature e utile.',
         6, altezza=30, corsivo=False)
    footer(ws, R_FOOTER, 6)
    stampa(ws, {'A': 42, 'B': 13, 'C': 10, 'D': 13, 'E': 17, 'F': 12})
    return ws


def foglio_pasta(wb):
    ws = wb.create_sheet('Pasta fresca')
    testata(ws, 'Pasta fresca all\'uovo: quanto costa farla in casa',
            'Prezzi indicativi: sostituiscili con quelli delle tue fatture (celle gialle). Il resto si calcola da solo.',
            5)
    barra(ws, 4, 'Ingredienti dell\'impasto', 5)
    intestazioni(ws, 5, ['Ingrediente', 'Quantità', 'Prezzo d\'acquisto IVA esclusa', 'Peso nell\'impasto (g)',
                         'Costo (€)'], altezza=32)
    dv = dv_numero(ws)
    f, u = P_FARINA, P_UOVA
    cella(ws, f, 1, 'Farina 00', grassetto=True)
    dv.add(cella(ws, f, 2, 1000, '#,##0 "g"', inp=True).coordinate)
    dv.add(cella(ws, f, 3, 1.20, '#,##0.00 "€/kg"', inp=True).coordinate)
    cella(ws, f, 4, f'=IF(B{f}="","",B{f})', GR, grigio=True)
    cella(ws, f, 5, f'=IF(OR(B{f}="",C{f}=""),"",ROUND(B{f}/1000*C{f},2))', EUR, grigio=True)
    cella(ws, u, 1, 'Uova (numero)', grassetto=True)
    dv.add(cella(ws, u, 2, 10, '0', inp=True).coordinate)
    dv.add(cella(ws, u, 3, 0.30, '#,##0.00 "€ l\'uno"', inp=True).coordinate)
    cella(ws, u, 4, f'=IF(OR(B{u}="",B8=""),"",B{u}*B8)', GR, grigio=True)
    cella(ws, u, 5, f'=IF(OR(B{u}="",C{u}=""),"",ROUND(B{u}*C{u},2))', EUR, grigio=True)
    for r in (f, u):
        ws.row_dimensions[r].height = 20
    cella(ws, 8, 1, 'Peso di un uovo senza guscio (g)', grassetto=True)
    dv.add(cella(ws, 8, 2, 60, GR, inp=True).coordinate)
    nota(ws, 8, f'Indicativo: circa 60{NB}g per un uovo grande senza guscio; con uova medie conta 50-55{NB}g. '
                'Pesale sgusciate e scrivi il peso reale.', 5, altezza=30, col=3)

    barra(ws, 10, 'Costo della pasta fresca fatta in casa', 5)
    acq = f'B{P_ACQ_PREZZO}'
    blocco = [
        (P_PESO, 'Peso dell\'impasto (circa)', f'=IF(COUNT(D{f}:D{u})=0,"",SUM(D{f}:D{u}))', '#,##0 "g"', False),
        (P_COSTO, 'Costo degli ingredienti', f'=IF(COUNT(E{f}:E{u})=0,"",SUM(E{f}:E{u}))', EUR, False),
        (P_KG, 'Costo al kg della pasta fresca',
         f'=IF(OR(B{P_COSTO}="",N(B{P_PESO})=0),"",ROUND(B{P_COSTO}/(B{P_PESO}/1000),2))', '#,##0.00 "€/kg"', False),
        (P_PORZ, 'Porzione di pasta', 120, '#,##0 "g"', True),
        (P_CASA, 'Costo della porzione fatta in casa',
         f'=IF(OR(B{P_KG}="",N(B{P_PORZ})=0),"",ROUND(B{P_KG}*B{P_PORZ}/1000,2))', EUR, False),
        (P_ACQ_PREZZO, 'Tagliatelle fresche acquistate (IVA esclusa)', 4.50, '#,##0.00 "€/kg"', True),
        (P_ACQ_PORZ, 'Costo della porzione acquistata',
         f'=IF(OR(N({acq})=0,N(B{P_PORZ})=0),"",ROUND({acq}*B{P_PORZ}/1000,2))', EUR, False),
        (P_DIFF, 'Differenza per porzione (acquistata − in casa)',
         f'=IF(OR(B{P_CASA}="",B{P_ACQ_PORZ}=""),"",ROUND(B{P_ACQ_PORZ}-B{P_CASA},2))', EUR, False),
    ]
    barra(ws, 17, 'Confronto con la pasta fresca acquistata', 5)
    for r, etichetta, valore, fmt, inp in blocco:
        cella(ws, r, 1, etichetta, grassetto=True)
        z = cella(ws, r, 2, valore, fmt, inp=inp, grassetto=True, grigio=not inp)
        ws.row_dimensions[r].height = 20
        if inp:
            dv.add(z.coordinate)
    nota(ws, 22, NOTA_MANODOPERA, 5, altezza=30, corsivo=False, fill=input_fill)
    ws.cell(row=22, column=1).font = Font(bold=True, color='111111')
    nota(ws, 23, 'Nel tuo scandaglio, usa il costo al kg della pasta fresca come prezzo d\'acquisto (€/kg) della pasta.', 5)
    footer(ws, 25, 5)
    stampa(ws, {'A': 50, 'B': 14, 'C': 20, 'D': 15, 'E': 12})
    return ws


# ---------------------------------------------------------------- gate
def inietta():
    out = subprocess.run([sys.executable, str(RAIZ / 'scripts/productos-digitales/inject_cache.py'), str(XLSX)],
                         check=True, capture_output=True, text=True).stdout.strip()
    m = re.search(r'formulas=(\d+) cache_inyectado=(\d+) fallos_pycel=(\d+)', out)
    assert m and m.group(3) == '0', out
    return out


def gate_file():
    """Gate sul libro pubblicato (data_only = quello che vede un visore che non ricalcola)."""
    wf = load_workbook(XLSX)
    assert wf.sheetnames == ['Esempio', 'Scandaglio vuoto', 'Pasta fresca'], wf.sheetnames
    assert wf.active.title == 'Scandaglio vuoto', wf.active.title
    with zipfile.ZipFile(XLSX) as zf:
        sel = [n for n in sorted(zf.namelist()) if re.match(r'xl/worksheets/sheet\d+\.xml$', n)
               and 'tabSelected="1"' in zf.read(n).decode('utf-8')]
    assert sel == ['xl/worksheets/sheet2.xml'], sel
    for ws in wf.worksheets:
        assert any(c.hyperlink and c.hyperlink.target == ARTICOLO for row in ws.iter_rows() for c in row), ws.title
        testi = [c.value for row in ws.iter_rows() for c in row if isinstance(c.value, str)]
        for frase in FOOTER:
            assert frase in testi, (ws.title, frase)
        dvs = ws.data_validations.dataValidation
        assert dvs and all(d.showErrorMessage for d in dvs), ws.title
        ps = ws.page_setup
        assert str(ps.paperSize) == str(ws.PAPERSIZE_A4) and ps.fitToWidth == 1 and ps.fitToHeight == 0, ws.title
        assert ws.sheet_properties.pageSetUpPr.fitToPage, ws.title
        # nessun dato di settore inventato: solo le percentuali ammesse nei testi
        for t in testi:
            for pct in re.findall(r'(\d+(?:,\d+)?)\s?%', t):
                assert pct in PCT_AMMESSE, (ws.title, t)
    wv = load_workbook(XLSX, data_only=True)
    es = wv['Esempio']
    righe = list(range(R_ING1, R_ING1 + len(ESEMPIO))) + [R_FORF]
    costi = [es.cell(row=r, column=6).value for r in righe]
    assert all(isinstance(v, (int, float)) for v in costi), costi
    costi = [round(v, 2) for v in costi]
    assert costi == [0.54, 0.90, 0.22, 0.09, 0.05], costi
    lorde = [es.cell(row=r, column=4).value for r in righe[:-1]]
    assert lorde == [120, 150, 10, 10], lorde
    tot, netto = round(es[f'B{R_COSTO}'].value, 2), round(es[f'B{R_NETTO}'].value, 2)
    fc, marg = round(es[f'B{R_FC}'].value * 100, 1), round(es[f'B{R_MARG}'].value, 2)
    assert (tot, netto, fc, marg) == (1.80, 10.91, 16.5, 9.11), (tot, netto, fc, marg)
    assert es[f'B{R_CARTA}'].value == PREZZO_CARTA and es[f'B{R_IVA}'].value == IVA
    # foglio vuoto: nessuna formula mostra un errore o un numero
    vuoto = wv['Scandaglio vuoto']
    for row in wf['Scandaglio vuoto'].iter_rows():
        for c in row:
            if c.data_type == 'f':
                v = vuoto[c.coordinate].value
                assert v in (None, ''), ('Scandaglio vuoto', c.coordinate, v)
    assert vuoto[f'B{R_IVA}'].value == IVA
    assert any(c.value == IVA_NOTA for row in vuoto.iter_rows() for c in row)
    pa = wv['Pasta fresca']
    pasta = [round(pa[f'B{r}'].value, 2) for r in (P_COSTO, P_KG, P_CASA, P_ACQ_PORZ, P_DIFF)]
    assert pasta == [4.20, 2.63, 0.32, 0.54, 0.22], pasta
    assert round(pa[f'B{P_PESO}'].value) == 1600 and [pa[f'E{r}'].value for r in (P_FARINA, P_UOVA)] == [1.2, 3.0]
    assert any(c.value == NOTA_MANODOPERA for row in pa.iter_rows() for c in row)
    return tot, fc, pasta


def gate_logica():
    """Riempie in memoria (pycel) il foglio vuoto e controlla i calcoli, compresi i casi incompleti o sbagliati."""
    logging.disable(logging.CRITICAL)
    from pycel import ExcelCompiler
    wf = load_workbook(XLSX)
    # Copia SENZA cache (openpyxl non conserva i valori delle formule): pycel deve calcolare tutto dalle formule,
    # non rileggere i valori iniettati da inject_cache.py.
    tmp = tempfile.TemporaryDirectory()
    copia = str(Path(tmp.name) / 'gate.xlsx')
    wf.save(copia)

    def nuovo(foglio='Scandaglio vuoto'):
        xl = ExcelCompiler(filename=copia)

        def val(ref):
            with open(os.devnull, 'w') as dn, contextlib.redirect_stderr(dn):
                x = xl.evaluate(f"'{foglio}'!{ref}")
            return x.item() if hasattr(x, 'item') else x

        # Riscaldamento: pycel ricalcola dopo set_value solo le formule che ha già valutato; quelle mai valutate
        # restituirebbero il valore in cache (iniettato) e il gate passerebbe senza aver ricalcolato niente.
        for row in wf[foglio].iter_rows():
            for c in row:
                if c.data_type == 'f':
                    val(c.coordinate)

        def imposta(valori):
            # «Cancellare» una cella = '' (pycel ignora set_value(None): non ricalcola i dipendenti). Per queste
            # formule '' e la cella vuota si comportano uguale: tutte controllano ="" o passano per N() prima di operare.
            for ref, x in valori.items():
                val(ref)  # pycel lascia cambiare solo le celle già nella sua mappa
                xl.set_value(f"'{foglio}'!{ref}", '' if x is None else x)
        return val, imposta

    def vuota(x):
        return x in (None, '')

    def errore(x):
        return isinstance(x, str) and x.startswith('#')

    a = R_ING1
    # 1) L'esempio del post copiato nel foglio vuoto dà gli stessi numeri.
    val, imposta = nuovo()
    dati = {f'F{R_FORF}': 0.05, f'B{R_CARTA}': 12}
    for i, (_, netta, calo, prezzo) in enumerate(ESEMPIO):
        dati.update({f'B{a + i}': netta, f'C{a + i}': calo, f'E{a + i}': prezzo})
    imposta(dati)
    assert [round(val(f'F{a + i}'), 2) for i in range(4)] == [0.54, 0.90, 0.22, 0.09]
    assert round(val(f'B{R_COSTO}'), 2) == 1.80 and round(val(f'B{R_NETTO}'), 2) == 10.91
    assert round(val(f'B{R_FC}') * 100, 1) == 16.5 and round(val(f'B{R_MARG}'), 2) == 9.11
    # 2) Quattro porzioni (quantità × 4): costo per porzione = totale ÷ 4.
    imposta({f'B{R_PORZ}': 4, f'F{R_FORF}': 0.20, f'B{a}': 480, f'B{a + 1}': 600, f'B{a + 2}': 40, f'B{a + 3}': 40})
    assert round(val(f'B{R_COSTO}'), 2) == 1.80 and round(val(f'B{R_FC}') * 100, 1) == 16.5
    # 3) Calo del 20 %: lorda = netta ÷ 0,8 al grammo per eccesso; costo sulla lorda.
    imposta({f'B{a + 4}': 100, f'C{a + 4}': 0.2, f'E{a + 4}': 10, f'B{a + 5}': 120, f'C{a + 5}': 0.1})
    assert val(f'D{a + 4}') == 125 and round(val(f'F{a + 4}'), 2) == 1.25
    assert val(f'D{a + 5}') == 134 and vuota(val(f'F{a + 5}'))  # senza prezzo: costo vuoto, non 0
    # 4) Calo ≥ 100 %: messaggio nella lorda e ERRORE fino al margine, anche senza prezzo (non sparisce dal totale).
    imposta({f'C{a + 5}': 1})
    assert val(f'D{a + 5}') == CALO_KO, val(f'D{a + 5}')
    assert errore(val(f'F{a + 5}')) and errore(val(f'B{R_COSTO}'))
    assert errore(val(f'B{R_FC}')) and errore(val(f'B{R_MARG}'))

    val, imposta = nuovo()
    # 5) Solo quantità, nessun prezzo: tutto vuoto (niente 0,00 € falsi).
    imposta({f'B{a}': 120})
    assert val(f'D{a}') == 120 and vuota(val(f'F{a}')) and vuota(val(f'B{R_COSTO}'))
    assert vuota(val(f'B{R_FC}')) and vuota(val(f'B{R_MARG}'))
    # 6) Costo senza prezzo in carta → food cost vuoto, senza #DIV/0!; IVA cancellata → prezzo IVA esclusa vuoto.
    imposta({f'E{a}': 4.5})
    assert round(val(f'B{R_COSTO}'), 2) == 0.54 and vuota(val(f'B{R_NETTO}')) and vuota(val(f'B{R_FC}'))
    imposta({f'B{R_CARTA}': 12, f'B{R_IVA}': None})
    assert vuota(val(f'B{R_NETTO}')) and vuota(val(f'B{R_FC}'))
    imposta({f'B{R_IVA}': 0.10})
    assert round(val(f'B{R_NETTO}'), 2) == 10.91
    # 7) Calo ≥ 100 % come UNICA riga (nessun altro costo): l'errore non deve diventare una cella vuota.
    val, imposta = nuovo()
    imposta({f'B{a}': 100, f'C{a}': 1.5})
    assert val(f'D{a}') == CALO_KO and errore(val(f'F{a}')) and errore(val(f'B{R_COSTO}'))
    # 8) Solo il forfait: il costo per porzione è il forfait.
    val, imposta = nuovo()
    imposta({f'F{R_FORF}': 0.05})
    assert round(val(f'B{R_COSTO}'), 2) == 0.05

    # Pasta fresca: cambiando i prezzi indicativi i calcoli seguono; svuotando, niente errori.
    pv, pimposta = nuovo('Pasta fresca')
    pimposta({f'C{P_FARINA}': 1.50, f'C{P_UOVA}': 0.25})
    assert round(pv(f'B{P_COSTO}'), 2) == 4.00 and round(pv(f'B{P_KG}'), 2) == 2.50
    assert round(pv(f'B{P_CASA}'), 2) == 0.30 and round(pv(f'B{P_DIFF}'), 2) == 0.24
    pimposta({ref: None for ref in (f'B{P_FARINA}', f'B{P_UOVA}', f'D{P_UOVA}', f'B{P_PORZ}', f'B{P_ACQ_PREZZO}')})
    for r in (P_PESO, P_COSTO, P_KG, P_CASA, P_ACQ_PORZ, P_DIFF):
        assert vuota(pv(f'B{r}')), (r, pv(f'B{r}'))
    tmp.cleanup()
    return 'OK'


def main():
    wb = Workbook()
    wb.remove(wb.active)
    foglio_scandaglio(wb, 'Esempio', True)
    foglio_scandaglio(wb, 'Scandaglio vuoto', False)
    foglio_pasta(wb)
    for i, ws in enumerate(wb.worksheets):
        ws.sheet_view.tabSelected = (i == 1)
    wb.active = 1
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.title = 'Calcolo food cost (scandaglio)'
    XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb.save(XLSX)
    print(inietta())
    tot, fc, pasta = gate_file()
    esito = gate_logica()
    chk = subprocess.run([sys.executable, str(RAIZ / 'scripts/productos-digitales/parche_xml_xlsx.py'), '--check',
                          str(XLSX)], cwd=RAIZ, capture_output=True, text=True)
    print(chk.stdout.strip())
    assert chk.returncode == 0, chk.stdout + chk.stderr
    it = lambda x: f'{x:.2f}'.replace('.', ',')  # noqa: E731
    print(f'OK {XLSX.name} · Esempio {it(tot)} € / {f"{fc:.1f}".replace(".", ",")} % · 3 fogli · '
          f'Pasta fresca {" / ".join(it(x) for x in pasta[:4])} · gate logico {esito} · attivo «Scandaglio vuoto»')


if __name__ == '__main__':
    main()
