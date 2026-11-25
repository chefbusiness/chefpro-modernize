#!/usr/bin/env python3
"""Tabella allergeni (IT), plantilla GRATIS — lead magnet de /it/blog/lista-allergeni-alimentari.

Gemelo italiano de plantilla-allergenliste-de.py (mismo diseño, colores, inject_cache y gates), ADAPTADO:
  - los 14 alérgenos NUMERADOS del 1 al 14 en el orden del anexo II del Reg. (UE) 1169/2011 (la práctica que
    respaldan las ASL; ejemplo AUSL Bologna: «Pizza margherita (1, 7)»); cabecera girada con número y nombre;
  - columnas 1 (Cereali contenenti glutine) y 8 (Frutta a guscio) = texto libre con validación de longitud (hay que
    nombrar el TIPO: grano, orzo…; nocciole, mandorle…); el resto, desplegable «X» (presente) / vacío; «Può contenere
    tracce (facoltativo)» de texto; «Codici per il menù» calculada: la lista de números presentes separada por
    comas («1, 3, 7»), vacía sin piatto. Las celdas de tipo que dicen «no/nessuno/nessuna» no cuentan y se marcan en
    naranja (igual que «glutine», «frutta a guscio»… sin tipo, que sí cuentan);
  - campos Locale / Aggiornata il / Verificata da; notas del art. 19, comma 8, del D.Lgs. 231/2017 (texto literal
    del brief) y aviso de ejemplo que remite al personal.
  - sin columna de aditivos (la del gemelo alemán es del § 5 LMZDV, sin equivalente aquí).
Keywords IT (GSC, nov-2026): «tabella allergeni alimentari da esporre», «tabella allergeni da esporre», «scheda
allergeni da stampare» (pos. 1), «tabella allergeni da stampare gratis», «allergeni 1 3 7», «tabella allergeni con
numeri».
Sale: astro-site/public/descargas/tabella-allergeni-ristorante-aichef.xlsx — 2 hojas: «Tabella allergeni» (activa,
      30 filas vacías) y «Esempio» (5 platos italianos, ricetta tipica, ilustrativos; los dos de la AUSL Bologna).
      astro-site/public/descargas/tabella-allergeni-ristorante-aichef.pdf — A4 apaisado, 1 página, a mano.
El xlsx pasa por inject_cache.py + caché «texto vacío» (como el gemelo DE), un gate data_only, un gate de lógica de
los códigos en una COPIA temporal y, después:
  python3 scripts/productos-digitales/parche_xml_xlsx.py --check astro-site/public/descargas/tabella-allergeni-ristorante-aichef.xlsx
`/descargas/*` está en noindex (netlify.toml). Sesión Claude Code, 25-nov-2026.
"""
import datetime
import math
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import warnings
import zipfile
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

RAIZ = Path(__file__).resolve().parents[2]
XLSX = RAIZ / 'astro-site/public/descargas/tabella-allergeni-ristorante-aichef.xlsx'
PDF = RAIZ / 'astro-site/public/descargas/tabella-allergeni-ristorante-aichef.pdf'
INJECT = RAIZ / 'scripts/productos-digitales/inject_cache.py'
ARTICOLO = 'https://aichef.pro/it/blog/lista-allergeni-alimentari'
TITOLO = 'Tabella allergeni – Ristorante'
FOGLIO, FOGLIO_ES = 'Tabella allergeni', 'Esempio'

NERO, ORO, GRIGIO = '111111', 'FFD700', 'F3F3F3'
sottile = Side(style='thin', color='BBBBBB')
bordo = Border(left=sottile, right=sottile, top=sottile, bottom=sottile)
giallo = PatternFill('solid', fgColor='FFF8D6')
nero = PatternFill('solid', fgColor=NERO)
grigio = PatternFill('solid', fgColor=GRIGIO)
NB = ' '

# (numero, nome, indicare il tipo?) — ordine dell'allegato II del Reg. (UE) 1169/2011
ALLERGENI = [(1, 'Cereali contenenti glutine', True), (2, 'Crostacei', False), (3, 'Uova', False),
             (4, 'Pesce', False), (5, 'Arachidi', False), (6, 'Soia', False), (7, 'Latte', False),
             (8, 'Frutta a guscio', True), (9, 'Sedano', False), (10, 'Senape', False), (11, 'Semi di sesamo', False),
             (12, 'Anidride solforosa e solfiti', False), (13, 'Lupini', False), (14, 'Molluschi', False)]
NUMERI = [n for n, _, _ in ALLERGENI]
assert NUMERI == list(range(1, 15))
# Nome breve sotto il numero nel PDF («<br/>» = a capo)
BREVE = {1: 'Cereali con<br/>glutine (tipo)', 2: 'Crosta-<br/>cei', 3: 'Uova', 4: 'Pesce', 5: 'Arachidi', 6: 'Soia',
         7: 'Latte', 8: 'Frutta a<br/>guscio (tipo)', 9: 'Sedano', 10: 'Senape', 11: 'Sesamo', 12: 'Solfiti',
         13: 'Lupini', 14: 'Mollu-<br/>schi'}

# Colonne (1-based): A Piatto · B–O i 14 allergeni · P Tracce · Q Codici per il menù
C_PIATTO, C_PRIMO, C_ULTIMO, C_TRACCE, C_CODICI = 1, 2, 15, 16, 17
C_TIPO = [C_PRIMO + i for i, (_, _, tipo) in enumerate(ALLERGENI) if tipo]        # [2, 9] → B e I
C_X = [C_PRIMO + i for i, (_, _, tipo) in enumerate(ALLERGENI) if not tipo]       # C–H e J–O
assert C_TIPO == [2, 9]
R_CAMPI1, R_CAMPI2, R_LEGENDA, R_GRUPPO, R_TESTATA, PRIMA = 4, 5, 7, 8, 9, 10
N_RIGHE = 30


def it(s):
    """Tipografia: spazio unificatore dopo «art.», «comma», «D.Lgs.», «Reg.», «(UE)», «allegato» davanti al numero."""
    if not isinstance(s, str) or s.startswith('='):
        return s
    return re.sub(r'(?<!\S)(art\.|comma|D\.Lgs\.|Reg\.|\(UE\)|allegato) (?=[\dIVX(])', r'\1' + NB, s)


# ---------------------------------------------------------------- Testi (note al piede: letterali del brief)
LEGGE = ('L’obbligo viene dal Reg. (UE) 1169/2011; le modalità le fissa l’art. 19, comma 8, del D.Lgs. 231/2017, in '
         'vigore dal 9 maggio 2018: l’informazione deve essere riconducibile a ciascun piatto e data prima che venga servito, su menù, registro, '
         'cartello o sistema equivalente, in italiano, visibile e leggibile.')
AVVISO_BASE = ('In alternativa puoi esporre un avviso che rimanda al personale, purché esista una documentazione scritta '
               'piatto per piatto, facilmente reperibile per il cliente e per l’autorità.')
CARTELLO = ('Per informazioni sugli allergeni presenti nei nostri piatti è possibile rivolgersi al personale di sala: la '
            'documentazione scritta è disponibile su richiesta.')
AVVISO = f'{AVVISO_BASE} Esempio di avviso: «{CARTELLO}»'
NUMERI_NOTA = ('I numeri da 1 a 14 seguono l’ordine dell’allegato II del Reg. (UE) 1169/2011: usali sul menù solo '
               'insieme a una legenda con il nome degli allergeni.')
TIPO_NOTA = 'Indica il cereale o il frutto a guscio: «glutine» o «frutta a guscio» da soli non bastano.'
TRACCE_NOTA = ('L’indicazione delle tracce («può contenere») è facoltativa: usala solo per un rischio reale di '
               'contaminazione crociata.')
AGGIORNA = 'Aggiorna la tabella a ogni cambio di ricetta, menù o fornitore.'
NOTE = [LEGGE, AVVISO, None, NUMERI_NOTA, TIPO_NOTA, TRACCE_NOTA, AGGIORNA]  # None = legenda (dopo ALLERGENI)
LEGENDA = ('X = presente · vuoto = assente · nelle colonne «1 · Cereali contenenti glutine» e «8 · Frutta a guscio» '
           'scrivi il tipo (per esempio grano, orzo, nocciole, mandorle) · la colonna «Codici per il menù» si compila '
           'da sola')
ISTRUZIONI = ('Compila le celle gialle, una riga per piatto, partendo dalla ricetta e non a memoria: impasto, salsa, '
              'contorno, condimento e prodotti acquistati (etichetta o scheda tecnica). Nelle colonne 1 e 8 scrivi il '
              'tipo, nelle altre scegli «X» dall’elenco: i codici per il menù si calcolano da soli.')
ESEMPIO_NOTA = ('Esempio fittizio a scopo illustrativo – ricetta tipica, adattala alla tua. Gli allergeni dei tuoi '
                'piatti dipendono dalle tue ricette e dai tuoi fornitori. Le tracce qui non sono compilate; controlla '
                'sempre l’etichetta o la scheda tecnica dei prodotti acquistati, per esempio salumi e dado da brodo.')
GRUPPO = 'I 14 allergeni dell’allegato II del Reg. (UE) 1169/2011, numerati da 1 a 14 nell’ordine dell’allegato'
TESTATE = {C_PIATTO: 'Piatto (con i componenti: salsa, contorno, condimento)',
           C_TRACCE: 'Può contenere tracce (facoltativo)', C_CODICI: 'Codici per il menù'}

# (piatto con la ricetta ipotizzata, {numero: valore}, codici attesi) — «X» o il tipo (1, 8); il resto resta vuoto.
ESEMPIO = [
    ('Pizza margherita (impasto con farina di grano, pomodoro, mozzarella fior di latte, basilico, olio '
     'extravergine d’oliva)', {1: 'grano', 7: 'X'}, '1, 7'),
    ('Tortellini al ragù (sfoglia all’uovo con farina di grano, ripieno di carne e Parmigiano Reggiano; ragù con '
     'soffritto di sedano, carota e cipolla, senza vino: se lo sfumi con il vino aggiungi il 12; se la mortadella del '
     'ripieno ha il pistacchio, aggiungi l’8)',
     {1: 'grano', 3: 'X', 7: 'X', 9: 'X'}, '1, 3, 7, 9'),
    ('Trofie al pesto alla genovese (trofie di farina di grano; pesto con basilico, pinoli, Parmigiano Reggiano, '
     'Pecorino, aglio e olio: i pinoli non rientrano nella frutta a guscio dell’allegato II, quindi l’8 non si '
     'segna)', {1: 'grano', 7: 'X'}, '1, 7'),
    ('Spaghetti alle vongole (spaghetti di grano duro, vongole, aglio, prezzemolo, olio; sfumati con vino bianco: il '
     'vino porta solfiti e la cottura non garantisce di scendere sotto i 10 mg/kg di SO2: nel dubbio si segna il 12)', {1: 'grano duro', 12: 'X', 14: 'X'},
     '1, 12, 14'),
    ('Tiramisù (savoiardi con farina di grano e uova, crema di mascarpone e uova, caffè, cacao; senza liquore)',
     {1: 'grano', 3: 'X', 7: 'X'}, '1, 3, 7'),
]
assert all(set(v) <= set(NUMERI) for _, v, _ in ESEMPIO)
assert all((x != 'X') == dict((n, t) for n, _, t in ALLERGENI)[n] for _, v, _ in ESEMPIO for n, x in v.items())
assert all(c == ', '.join(str(n) for n in sorted(v)) for _, v, c in ESEMPIO)
CODICI_ATTESI = [c for _, _, c in ESEMPIO]
assert CODICI_ATTESI[:2] == ['1, 7', '1, 3, 7, 9']  # i due esempi dell'AUSL Bologna

# Nelle colonne del tipo (1, 8) queste voci vogliono dire «assente»: arancione e non contano nei codici.
PAROLE_NO = ('no', 'nessuno', 'nessuna', 'nessun', 'assente', 'non presente', 'senza', 'senza glutine', 'pinoli')
LEGENDA_NOTE = 'Legenda – ' + ' · '.join(f'{n} {nome}' for n, nome, _ in ALLERGENI)
NOTE[NOTE.index(None)] = LEGENDA_NOTE
# … e queste sono generiche (manca il tipo): arancione, ma contano (l'allergene c'è).
PAROLE_GENERICHE = ('glutine', 'cereali', 'cereale', 'frutta a guscio', 'frutto a guscio', 'frutta secca', 'x')


def tipo_conta(ref):
    """VERO se la cella del tipo è compilata e non dice «no», «nessuno» o «nessuna»."""
    return 'AND(' + ','.join([f'{ref}<>""'] + [f'LOWER(TRIM({ref}))<>"{w}"' for w in PAROLE_NO]) + ')'


def formula_codici(r):
    """Numeri presenti (X nelle colonne a croce, tipo compilato nelle colonne 1 e 8) separati da «, »; vuota senza
    piatto. Ogni allergene presente aggiunge «, n»; MID(…,3,100) toglie il primo «, ». Niente TEXTJOIN: funziona anche
    in Excel 2016, LibreOffice, Google Sheets e pycel."""
    pezzi = []
    for i, (n, _, tipo) in enumerate(ALLERGENI):
        ref = f'{get_column_letter(C_PRIMO + i)}{r}'
        cond = tipo_conta(ref) if tipo else f'{ref}="X"'
        pezzi.append(f'IF({cond},", {n}","")')
    return f'=IF(A{r}="","",MID({"&".join(pezzi)},3,100))'


def blocco(ws, riga, c1, c2, valore=None, input_=False, grassetto=False, fmt=None, allin=None):
    """Cella (unita da c1 a c2) con bordo; openpyxl riporta il bordo sul contorno quando unisce."""
    c = ws.cell(row=riga, column=c1, value=it(valore))
    c.border = bordo
    if input_:
        c.fill = giallo
    if grassetto:
        c.font = Font(bold=True, size=10)
    if fmt:
        c.number_format = fmt
    c.alignment = allin or Alignment(vertical='center', wrap_text=True)
    if c2 > c1:
        ws.merge_cells(start_row=riga, start_column=c1, end_row=riga, end_column=c2)
    return c


def foglio(wb, nome, esempio):
    ws = wb.create_sheet(nome)
    righe = ESEMPIO if esempio else [None] * N_RIGHE
    ultima = PRIMA + len(righe) - 1

    ws['A1'] = TITOLO
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws['A1'].fill = nero
    ws['A1'].alignment = Alignment(vertical='center')
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=C_CODICI)
    ws.row_dimensions[1].height = 30
    ws['A2'] = it(ESEMPIO_NOTA if esempio else ISTRUZIONI)
    ws['A2'].font = Font(italic=True, bold=esempio, color='555555')
    ws['A2'].alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=C_CODICI)
    ws.row_dimensions[2].height = 30
    ws.row_dimensions[3].height = 6

    sinistra = Alignment(horizontal='left', vertical='center')
    blocco(ws, R_CAMPI1, 1, 1, 'Locale', grassetto=True)
    blocco(ws, R_CAMPI1, 2, 8, 'Trattoria (esempio fittizio)' if esempio else None, input_=True, allin=sinistra)
    blocco(ws, R_CAMPI1, 9, 13, 'Verificata da', grassetto=True)
    blocco(ws, R_CAMPI1, 14, C_CODICI, 'Chef di cucina' if esempio else None, input_=True, allin=sinistra)
    blocco(ws, R_CAMPI2, 1, 1, 'Aggiornata il', grassetto=True)
    blocco(ws, R_CAMPI2, 2, 8, datetime.date(2026, 11, 25) if esempio else None, input_=True, fmt='dd/mm/yyyy',
           allin=sinistra)
    nota = ws.cell(row=R_CAMPI2, column=9, value=it(AGGIORNA))
    nota.font = Font(italic=True, color='555555', size=9)
    nota.alignment = Alignment(vertical='center')
    ws.merge_cells(start_row=R_CAMPI2, start_column=9, end_row=R_CAMPI2, end_column=C_CODICI)
    for r in (R_CAMPI1, R_CAMPI2):
        ws.row_dimensions[r].height = 20
    ws.row_dimensions[6].height = 6
    dv_data = DataValidation(type='date', operator='greaterThanOrEqual', formula1='36526', allow_blank=True,
                             showErrorMessage=True, errorTitle='Data',
                             error='Inserisci una data, per esempio 25/11/2026.')
    ws.add_data_validation(dv_data)
    dv_data.add(f'B{R_CAMPI2}')

    leg = ws.cell(row=R_LEGENDA, column=1, value=it(LEGENDA))
    leg.font = Font(bold=True, size=10)
    leg.alignment = Alignment(wrap_text=True, vertical='center')
    ws.merge_cells(start_row=R_LEGENDA, start_column=1, end_row=R_LEGENDA, end_column=C_CODICI)
    ws.row_dimensions[R_LEGENDA].height = 27

    for c in range(1, C_CODICI + 1):
        ws.cell(row=R_GRUPPO, column=c).fill = nero
    g = ws.cell(row=R_GRUPPO, column=C_PRIMO, value=it(GRUPPO))
    g.font = Font(bold=True, size=9, color='FFFFFF')
    g.alignment = Alignment(horizontal='center', vertical='center')
    ws.merge_cells(start_row=R_GRUPPO, start_column=C_PRIMO, end_row=R_GRUPPO, end_column=C_ULTIMO)

    for c in range(1, C_CODICI + 1):
        cella = ws.cell(row=R_TESTATA, column=c)
        cella.border = bordo
        cella.fill = grigio
        if C_PRIMO <= c <= C_ULTIMO:
            n, nome_a, tipo = ALLERGENI[c - C_PRIMO]
            cella.value = f'{n} · {nome_a}' + ('\n(indica il tipo)' if tipo else '')
            cella.font = Font(bold=True, size=9)
            # 90° = dal basso verso l'alto; 150 pt di altezza: «12 · Anidride solforosa e solfiti» (~131 pt in
            # Helvetica grassetto 9, meno in Calibri) sta su una riga; «(indica il tipo)» va a capo nelle colonne larghe.
            cella.alignment = Alignment(text_rotation=90, horizontal='center', vertical='bottom', wrap_text=True)
        else:
            cella.value = it(TESTATE[c])
            cella.font = Font(bold=True, size=10)
            cella.alignment = Alignment(horizontal='center' if c == C_CODICI else 'left', vertical='bottom',
                                        wrap_text=True)
    ws.row_dimensions[R_TESTATA].height = 150

    centro = Alignment(horizontal='center', vertical='center', wrap_text=True)
    for i, voce in enumerate(righe):
        r = PRIMA + i
        piatto, valori, _ = voce if voce else (None, {}, None)
        blocco(ws, r, C_PIATTO, C_PIATTO, piatto, input_=True)
        for c in range(C_PRIMO, C_ULTIMO + 1):
            blocco(ws, r, c, c, valori.get(NUMERI[c - C_PRIMO]), input_=True, allin=centro)
        blocco(ws, r, C_TRACCE, C_TRACCE, None, input_=True)
        # «1, 2, …, 14» è lungo: si riduce per stare nella cella invece di andare a capo (riga da 22 pt)
        cod = blocco(ws, r, C_CODICI, C_CODICI, formula_codici(r),
                     allin=Alignment(horizontal='center', vertical='center', shrink_to_fit=True))
        cod.fill = grigio
        cod.font = Font(bold=True)
        # Esempio: 15 pt per riga stimata nella colonna A (larghezza 44, ~46 caratteri per riga), almeno 3 righe
        ws.row_dimensions[r].height = 15 * max(3, len(textwrap.wrap(piatto, 46))) if esempio else 22

    area_tipo = ' '.join(f'{get_column_letter(c)}{PRIMA}:{get_column_letter(c)}{ultima}' for c in C_TIPO)
    area_x = f'C{PRIMA}:H{ultima} J{PRIMA}:O{ultima}'
    dv_x = DataValidation(type='list', formula1='"X"', allow_blank=True, showErrorMessage=True,
                          errorTitle='Allergeni', error='Scegli «X» (presente) o lascia la cella vuota.')
    ws.add_data_validation(dv_x)
    for a in area_x.split():
        dv_x.add(a)
    dv_tipo = DataValidation(type='textLength', operator='between', formula1='3', formula2='60', allow_blank=True,
                             showErrorMessage=True, showInputMessage=True, errorTitle='Indica il tipo',
                             error='Indica il tipo in 3-60 caratteri, per esempio grano o nocciole: qui una «X» non '
                                   'basta.',
                             promptTitle='Indica il tipo',
                             prompt='Per esempio grano, orzo, avena; nocciole, mandorle, noci. ' + TIPO_NOTA)
    ws.add_data_validation(dv_tipo)
    for a in area_tipo.split():
        dv_tipo.add(a)
    dv_testo = DataValidation(type='textLength', operator='lessThanOrEqual', formula1='250', allow_blank=True,
                              showErrorMessage=True, errorTitle='Testo', error='Al massimo 250 caratteri.')
    ws.add_data_validation(dv_testo)
    dv_testo.add(f'P{PRIMA}:P{ultima}')

    # A colpo d'occhio: presente = rosso; «glutine», «frutta a guscio»… da soli nelle colonne 1/8 = arancione (manca il
    # tipo), come «no», «nessuno», «nessuna» (lì va lasciata vuota; la cella non conta nei codici).
    rosso = PatternFill('solid', fgColor='F8D7DA', bgColor='F8D7DA')
    arancio = PatternFill('solid', fgColor='FFE3B3', bgColor='FFE3B3')
    for a in area_tipo.split():
        prima_c = a.split(':')[0]
        verifica = ','.join(f'LOWER(TRIM({prima_c}))="{w}"' for w in PAROLE_GENERICHE + PAROLE_NO)
        ws.conditional_formatting.add(a, FormulaRule(formula=[f'OR({verifica})'], stopIfTrue=True,
                                                     font=Font(bold=True, color='8A5300'), fill=arancio))
        ws.conditional_formatting.add(a, FormulaRule(formula=[f'{prima_c}<>""'], font=Font(bold=True, color='9C1C1C'),
                                                     fill=rosso))
    for a in area_x.split():
        ws.conditional_formatting.add(a, CellIsRule(operator='equal', formula=['"X"'],
                                                    font=Font(bold=True, color='9C1C1C'), fill=rosso))

    rn = ultima + 2
    for i, testo in enumerate(NOTE):
        c = ws.cell(row=rn + i, column=1, value=it(testo))
        c.font = Font(italic=True, color='555555', size=10)
        c.alignment = Alignment(wrap_text=True, vertical='top')
        ws.merge_cells(start_row=rn + i, start_column=1, end_row=rn + i, end_column=C_CODICI)
        # ~150 caratteri per riga sull'area unita A–Q (larghezza ~164)
        ws.row_dimensions[rn + i].height = 14 * math.ceil(len(testo) / 150) + 2
    rl = rn + len(NOTE)
    ws.cell(row=rl, column=1, value='Guida completa ai 14 allergeni:').font = Font(size=10)
    link = ws.cell(row=rl, column=2, value=ARTICOLO)
    link.hyperlink = ARTICOLO
    link.font = Font(color='0563C1', underline='single', size=10)
    ws.merge_cells(start_row=rl, start_column=2, end_row=rl, end_column=C_CODICI)

    ws.column_dimensions['A'].width = 44
    for c in range(C_PRIMO, C_ULTIMO + 1):
        ws.column_dimensions[get_column_letter(c)].width = 11 if c in C_TIPO else 5
    ws.column_dimensions['P'].width = 20
    ws.column_dimensions['Q'].width = 18
    ws.freeze_panes = f'B{PRIMA}'
    ws.sheet_view.showGridLines = False
    ws.print_title_rows = f'{R_GRUPPO}:{R_TESTATA}'
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins.left = ws.page_margins.right = 0.4
    ws.page_margins.top = ws.page_margins.bottom = 0.5
    return ws


# ---------------------------------------------------------------- PDF da stampare
def pdf_vuoto():
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase.pdfmetrics import stringWidth
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    def t(s):
        """Testo PDF: tipografia + WinAnsi del carattere standard (Helvetica: à è é ì ò ù « » ’ – ·)."""
        s = it(s)
        s.encode('cp1252')  # UnicodeEncodeError se un carattere non fosse rappresentabile
        return s

    pagina = landscape(A4)
    mx, my = 12 * mm, 9 * mm
    doc = SimpleDocTemplate(str(PDF), pagesize=pagina, leftMargin=mx, rightMargin=mx, topMargin=my, bottomMargin=my,
                            title=t(TITOLO), author='AI Chef Pro', subject=t('Modello da stampare e compilare a mano'))
    W = pagina[0] - 2 * mx
    linea = colors.HexColor('#999999')
    s_lab = ParagraphStyle('lab', fontName='Helvetica-Bold', fontSize=8.5, leading=10)
    s_num = ParagraphStyle('num', fontName='Helvetica-Bold', fontSize=11, leading=12, alignment=TA_CENTER)
    s_breve = ParagraphStyle('breve', fontName='Helvetica', fontSize=5.8, leading=6.6, alignment=TA_CENTER,
                             splitLongWords=0)
    s_testa = ParagraphStyle('testa', fontName='Helvetica-Bold', fontSize=8, leading=9.5)
    s_leg = ParagraphStyle('leg', fontName='Helvetica', fontSize=8.5, leading=10.5)
    s_nota = ParagraphStyle('nota', fontName='Helvetica', fontSize=7.3, leading=9)
    s_piede = ParagraphStyle('piede', fontName='Helvetica-Oblique', fontSize=7.5, leading=9.5,
                             textColor=colors.HexColor('#555555'))

    el = []
    fascia = Table([[t(TITOLO)]], colWidths=[W])
    fascia.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#' + NERO)),
                                ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#' + ORO)),
                                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                                ('FONTSIZE', (0, 0), (-1, -1), 16), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 10)]))
    el += [fascia, Spacer(1, 5)]

    campi = Table([[Paragraph('Locale', s_lab), '', Paragraph('Aggiornata il', s_lab), '',
                    Paragraph('Verificata da', s_lab), '']],
                  colWidths=[W * x for x in (0.07, 0.36, 0.10, 0.14, 0.10, 0.23)], rowHeights=20)
    campi.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, linea), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                               *[('BACKGROUND', (c, 0), (c, 0), colors.HexColor('#' + GRIGIO)) for c in (0, 2, 4)]]))
    el += [campi, Spacer(1, 5)]
    el += [Paragraph(t('<b>X</b> = presente · vuoto = assente · colonne <b>1</b> (cereali) e <b>8</b> (frutta a '
                       'guscio): scrivi il tipo (per esempio grano, orzo, nocciole, mandorle) – «glutine» o «frutta a '
                       'guscio» da soli non bastano · <b>Codici per il menù</b>: i numeri presenti separati da '
                       'virgole, per esempio 1, 3, 7.'), s_leg),
           Spacer(1, 3)]

    b_x, b_tipo, b_tracce, b_codici = 27, 46, 70, 74
    b_piatto = W - 12 * b_x - 2 * b_tipo - b_tracce - b_codici
    larghezze = [b_piatto] + [b_tipo if tipo else b_x for _, _, tipo in ALLERGENI] + [b_tracce, b_codici]
    for (n, _, _), larg in zip(ALLERGENI, larghezze[1:15]):
        for riga in BREVE[n].split('<br/>'):
            assert stringWidth(riga, 'Helvetica', 5.8) <= larg - 2, (n, riga)
    testata = ([Paragraph(t('Piatto <font name="Helvetica" size="6.5">(con i componenti: salsa, contorno, '
                            'condimento)</font>'), s_testa)]
               + [[Paragraph(str(n), s_num), Paragraph(t(BREVE[n]), s_breve)] for n in NUMERI]
               + [Paragraph(t('Può contenere tracce <font name="Helvetica" size="6.5">(facoltativo)</font>'), s_testa),
                  Paragraph(t('Codici per il menù'), s_testa)])
    n_righe, altezza = 15, 20.5  # 7,2 mm per riga: spazio sufficiente per scrivere a mano
    matrice = Table([testata] + [[''] * 17 for _ in range(n_righe)], colWidths=larghezze,
                    rowHeights=[32] + [altezza] * n_righe, repeatRows=1)
    matrice.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, linea),
                                 ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor('#' + NERO)),
                                 ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#' + GRIGIO)),
                                 ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#FAFAFA')]),
                                 ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
                                 ('LEFTPADDING', (1, 0), (14, 0), 1), ('RIGHTPADDING', (1, 0), (14, 0), 1),
                                 ('TOPPADDING', (1, 0), (14, 0), 1), ('BOTTOMPADDING', (1, 0), (14, 0), 1)]))
    el += [matrice, Spacer(1, 5)]
    # spazio unificatore: il numero non resta mai a fine riga senza il suo nome
    legenda = ' · '.join(f'<b>{n}</b>{NB}{nome_a}' + (' (indica il tipo)' if tipo else '')
                         for n, nome_a, tipo in ALLERGENI)
    el += [Paragraph(t(f'<b>Legenda</b> – i 14 allergeni dell’allegato II del Reg. (UE) 1169/2011: {legenda}.'),
                     s_nota), Spacer(1, 1.5),
           Paragraph(t(LEGGE), s_nota), Spacer(1, 1.5),
           Paragraph(t(f'{AVVISO_BASE} Esempio di avviso: <b>«{CARTELLO}»</b>'), s_nota), Spacer(1, 1.5),
           Paragraph(t(f'{NUMERI_NOTA} {TRACCE_NOTA} {AGGIORNA}'), s_nota), Spacer(1, 3),
           Paragraph(t('Modello gratuito di AI Chef Pro · Guida: <a href="https://aichef.pro/it/blog/lista-allergeni-alimentari" '
                       'color="#1a5fb4">aichef.pro/it/blog/lista-allergeni-alimentari</a>'),
                     s_piede)]
    doc.build(el)


# ---------------------------------------------------------------- Gate
def cache_testo_vuoto(percorso):
    """inject_cache.py non inietta il risultato «""»: la cella resta con una cache vuota (<v></v>, letta come 0) e chi
    non ricalcola (Anteprima di macOS, telefono) mostrerebbe «0» in «Codici per il menù». Qui si scrive la cache
    «testo vuoto» come fa Excel (t="str" + <v></v>), senza toccare il resto dello zip (come nel gemello DE)."""
    schema = re.compile(r'<c r="([A-Z]+[0-9]+)"((?:(?!\st=)[^>])*)>(<f>[^<]*</f>)(?:<v>\s*</v>|<v\s*/>)?</c>')
    with zipfile.ZipFile(percorso) as z:
        parti = [(i, z.read(i.filename)) for i in z.infolist()]
    n = 0
    with zipfile.ZipFile(str(percorso) + '.tmp', 'w', zipfile.ZIP_DEFLATED) as zout:
        for info, dati in parti:
            if re.match(r'xl/worksheets/sheet[0-9]+\.xml$', info.filename):
                xml, k = schema.subn(r'<c r="\1"\2 t="str">\3<v></v></c>', dati.decode('utf-8'))
                dati, n = xml.encode('utf-8'), n + k
            zout.writestr(info, dati)
    shutil.move(str(percorso) + '.tmp', str(percorso))
    return n


def inietta(percorso):
    out = subprocess.run([sys.executable, str(INJECT), str(percorso)], check=True, capture_output=True,
                         text=True).stdout
    assert 'fallos_pycel=0' in out, out
    m = re.search(r'formulas=(\d+) cache_inyectado=(\d+)', out)
    vuote = cache_testo_vuoto(percorso)
    assert int(m.group(1)) == int(m.group(2)) + vuote, (out, vuote)  # ogni formula ha la sua cache
    return f'{out.strip()} cache_testo_vuoto={vuote}'


def gate_xlsx():
    with zipfile.ZipFile(XLSX) as z:
        viste = [z.read(f'xl/worksheets/sheet{i}.xml').decode('utf-8').count('tabSelected="1"') for i in (1, 2)]
        tutto = ' '.join(z.read(n).decode('utf-8') for n in z.namelist() if n.endswith('.xml'))
    assert viste == [1, 0], f'tabSelected: {viste}'
    for residuo in ('LMIV', 'LMIDV', 'LMZDV', 'Gericht', 'Spuren', 'Weizen', 'Art nennen', 'Geprüft', 'österreich',
                    'Zusatzstoffe', 'TEXTJOIN'):
        assert residuo not in tutto, residuo
    wf = load_workbook(XLSX)
    assert wf.sheetnames == [FOGLIO, FOGLIO_ES] and wf.active.title == FOGLIO, wf.sheetnames
    for ws, n in ((wf[FOGLIO], N_RIGHE), (wf[FOGLIO_ES], len(ESEMPIO))):
        ultima = PRIMA + n - 1
        testate = [ws.cell(row=R_TESTATA, column=c).value for c in range(C_PRIMO, C_ULTIMO + 1)]
        assert [int(k.split(' · ')[0]) for k in testate] == NUMERI, testate
        assert [k.split(' · ')[1].split('\n')[0] for k in testate] == [x for _, x, _ in ALLERGENI], testate
        assert [k.endswith('\n(indica il tipo)') for k in testate] == [t for _, _, t in ALLERGENI], testate
        assert all(ws.cell(row=R_TESTATA, column=c).alignment.text_rotation == 90
                   for c in range(C_PRIMO, C_ULTIMO + 1))
        assert [ws.cell(row=R_TESTATA, column=c).value for c in (C_TRACCE, C_CODICI)] == [
            'Può contenere tracce (facoltativo)', 'Codici per il menù']
        assert ws.freeze_panes == f'B{PRIMA}', ws.freeze_panes
        tipi = sorted(d.type for d in ws.data_validations.dataValidation)
        assert tipi == ['date', 'list', 'textLength', 'textLength'], tipi
        assert all(d.showErrorMessage and d.error for d in ws.data_validations.dataValidation)
        lista = [d for d in ws.data_validations.dataValidation if d.type == 'list']
        assert len(lista) == 1 and lista[0].formula1 == '"X"', lista
        assert sorted(str(lista[0].sqref).split()) == sorted([f'C{PRIMA}:H{ultima}', f'J{PRIMA}:O{ultima}'])
        tipo = [d for d in ws.data_validations.dataValidation if d.type == 'textLength' and d.operator == 'between']
        assert len(tipo) == 1 and (tipo[0].formula1, tipo[0].formula2) == ('3', '60') and tipo[0].showInputMessage
        assert sorted(str(tipo[0].sqref).split()) == sorted([f'B{PRIMA}:B{ultima}', f'I{PRIMA}:I{ultima}'])
        assert 'grano' in tipo[0].prompt and 'nocciole' in tipo[0].prompt and TIPO_NOTA in tipo[0].prompt
        # limiti di Excel: titolo ≤ 32, messaggio ≤ 255 caratteri (altrimenti «riparazione» all'apertura)
        for d in ws.data_validations.dataValidation:
            assert all(len(x or '') <= 32 for x in (d.errorTitle, d.promptTitle)), d
            assert all(len(x or '') <= 255 for x in (d.error, d.prompt)), d
        for r in range(PRIMA, ultima + 1):
            assert ws.cell(row=r, column=C_CODICI).value == formula_codici(r)
        assert ws.cell(row=ultima + 1, column=C_CODICI).value is None
        testi = ' '.join(str(c.value) for row in ws.iter_rows() for c in row if c.value).replace(NB, ' ')
        for obbligo in NOTE + ['Locale', 'Aggiornata il', 'Verificata da', 'Piatto (con i componenti',
                               'art. 19, comma 8, del D.Lgs. 231/2017']:
            assert obbligo in testi, obbligo
        assert any(c.hyperlink and c.hyperlink.target == ARTICOLO for row in ws.iter_rows() for c in row)
    wv = load_workbook(XLSX, data_only=True)
    es = wv[FOGLIO_ES]
    codici = [es.cell(row=PRIMA + i, column=C_CODICI).value for i in range(len(ESEMPIO))]
    assert codici == CODICI_ATTESI, codici
    for i, (_, valori, _) in enumerate(ESEMPIO):
        cella = {n: es.cell(row=PRIMA + i, column=C_PRIMO + k).value for k, n in enumerate(NUMERI)}
        assert {n: v for n, v in cella.items() if v is not None} == valori, (i, cella)
        assert all(v in (None, 'X') for n, v in cella.items() if n not in (1, 8))
        assert es.cell(row=PRIMA + i, column=C_TRACCE).value is None
    vuoto = wv[FOGLIO]
    for r in range(PRIMA, PRIMA + N_RIGHE):
        assert all(vuoto.cell(row=r, column=c).value is None for c in range(1, C_TRACCE + 1)), r
        assert vuoto.cell(row=r, column=C_CODICI).value in (None, ''), r
    return codici


def gate_logica():
    """Valori di prova in una copia TEMPORANEA: il file pubblicato resta vuoto."""
    tutti = {c: ('grano' if c == 2 else 'pistacchi' if c == 9 else 'X') for c in range(2, 16)}
    casi = [  # ({colonna: valore}, atteso, descrizione)
        ({1: 'Solo piatto'}, '', 'piatto senza allergeni → vuoto'),
        ({1: 'Pane', 2: 'grano, segale'}, '1', 'solo 1 (tipo come testo) → «1»'),
        ({1: 'Torta di nocciole', 2: 'grano', 4: 'X', 8: 'X', 9: 'nocciole'}, '1, 3, 7, 8', '1 + 3 + 7 + 8'),
        ({1: 'Minuscola', 3: 'x'}, '2', '«x» minuscola vale come «X» → «2»'),
        ({1: 'Tracce', 16: 'sesamo'}, '', 'le tracce non entrano nei codici → vuoto'),
        ({3: 'X', 9: 'noci'}, '', 'allergeni senza piatto → vuoto'),
        ({}, '', 'riga vuota → vuoto'),
        ({1: 'Tutti e 14', **tutti}, ', '.join(map(str, NUMERI)), 'tutti i 14 → «1, 2, …, 14»'),
        ({1: 'Insalata', 2: 'no', 9: 'nessuna'}, '', '«no» in 1 e «nessuna» in 8 non contano → vuoto'),
        # «Nessuno» con la maiuscola; spazi ai bordi non verificabili: TRIM di pycel 1.0b30 accorcia solo gli spazi
        # multipli, quello di Excel/LibreOffice li toglie anche all'inizio e alla fine.
        ({1: 'Frittata', 2: 'Nessuno', 4: 'X', 9: 'pistacchi'}, '3, 8', '«Nessuno» in 1 non conta, 3 + 8 → «3, 8»'),
        ({1: 'Due cifre', 11: 'X', 15: 'X'}, '10, 14', 'ordine numerico con due cifre → «10, 14»'),
        ({1: 'Generico', 2: 'glutine'}, '1', '«glutine» senza tipo conta (arancione) → «1»'),
    ]
    with tempfile.TemporaryDirectory() as tmp:
        copia = Path(tmp) / 'test.xlsx'
        shutil.copy(XLSX, copia)
        wb = load_workbook(copia)
        for i, (valori, _, _) in enumerate(casi):
            for c, v in valori.items():
                wb[FOGLIO].cell(row=PRIMA + i, column=c, value=v)
        wb.save(copia)
        inietta(copia)
        wv = load_workbook(copia, data_only=True)
        esiti = []
        for i, (_, atteso, descr) in enumerate(casi):
            v = wv[FOGLIO].cell(row=PRIMA + i, column=C_CODICI).value
            esiti.append((descr, atteso, '' if v is None else v))
    for descr, atteso, v in esiti:
        print(f'  {"OK " if atteso == v else "KO "} {descr} → {v!r} (atteso {atteso!r})')
    assert all(atteso == v for _, atteso, v in esiti), 'Gate logica KO'
    return len(esiti)


def gate_pdf():
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        from pypdf import PdfReader
        lettore = PdfReader(str(PDF))
        pagine = len(lettore.pages)
        assert pagine == 1, f'{pagine} pagine'
        p = lettore.pages[0]
        assert float(p.mediabox.width) > float(p.mediabox.height), 'non orizzontale'
        testo = ' '.join(p.extract_text().replace(NB, ' ').split())
    mancanti = [m for m in ('Cereali contenenti glutine', 'Frutta a guscio', 'Anidride solforosa e solfiti',
                            'Molluschi', 'Locale', 'Aggiornata il', 'Verificata da', 'Può contenere tracce',
                            'Codici per il menù', 'in vigore dal 9 maggio 2018', 'art. 19, comma 8, del D.Lgs. 231/2017',
                            '«' + CARTELLO + '»', 'allegato II del Reg. (UE) 1169/2011', 'da soli non bastano',
                            'contaminazione crociata', 'ricetta, menù o fornitore', TITOLO,
                            'aichef.pro/it/blog/lista-allergeni-alimentari')
                if m not in testo]
    assert not mancanti, mancanti
    legenda = testo[testo.index('Legenda'):]
    for n, nome_a, _ in ALLERGENI:
        assert f'{n} {nome_a}' in legenda, (n, nome_a)
    return pagine


def main():
    wb = Workbook()
    wb.remove(wb.active)
    vuoto = foglio(wb, FOGLIO, False)
    es = foglio(wb, FOGLIO_ES, True)
    vuoto.sheet_view.tabSelected = True
    es.sheet_view.tabSelected = False
    wb.active = 0
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.title = TITOLO
    XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb.save(XLSX)
    print(inietta(XLSX))
    codici = gate_xlsx()
    n_logica = gate_logica()
    pdf_vuoto()
    pagine = gate_pdf()
    print(f'OK {XLSX.name} · vuota {N_RIGHE} righe × 14 allergeni (numeri 1-14) · Esempio codici {codici} '
          f'· Gate logica {n_logica}/{n_logica} · {PDF.name} PDF {pagine} pagina')


if __name__ == '__main__':
    main()
