#!/usr/bin/env python3
"""Allergenliste (DE), Vorlage GRATIS — lead magnet de /de/blog/allergenkennzeichnung.

Gemelo alemán de plantilla-tableau-allergenes-fr.py (mismo diseño, colores, inject_cache y gates), ADAPTADO:
  - código de letras AUSTRIACO (A B C D E F G H L M N O P R), la única referencia documentada; en Alemania no hay
    código oficial y la hoja lo dice con la nota literal;
  - columnas A (Getreide) y H (Schalenfrüchte) = texto libre con validación de longitud (hay que nombrar la ART:
    Weizen, Haselnuss…); el resto, desplegable «X» (enthalten) / vacío; «Spuren (freiwillig)» y «Zusatzstoffe
    (§ 5 LMZDV)» de texto; «Anzahl Allergene» calculada (COUNTIF de las X + las dos celdas de texto no vacías y distintas de
    «nein/keine/kein», que además se marcan en naranja);
  - campos Betrieb / Stand (Datum der letzten Prüfung) / Geprüft von; notas literales de la LMIDV (§ 4 Abs. 4).
Keywords DE (nov-2026): «allergenliste vorlage» 170, «allergene liste vorlage» 90, «allergenkennzeichnung vorlage» 70,
«allergene tabelle vorlage» 70.
Sale: astro-site/public/descargas/allergenliste-vorlage-gastronomie-aichef.xlsx — 2 hojas: «Allergenliste» (activa,
      30 filas vacías) y «Beispiel» (5 platos alemanes, typische Rezeptur, ilustrativos).
      astro-site/public/descargas/allergenliste-vorlage-gastronomie-aichef.pdf — A4 apaisado, 1 página, a mano.
El xlsx pasa por inject_cache.py + caché «texto vacío» (como el HACCP FR), un gate data_only, un gate de lógica del
recuento en una COPIA temporal y, después:
  python3 scripts/productos-digitales/parche_xml_xlsx.py --check astro-site/public/descargas/allergenliste-vorlage-gastronomie-aichef.xlsx
`/descargas/*` está en noindex (netlify.toml). Sesión Claude Code, 25-nov-2026.
"""
import datetime
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
XLSX = RAIZ / 'astro-site/public/descargas/allergenliste-vorlage-gastronomie-aichef.xlsx'
PDF = RAIZ / 'astro-site/public/descargas/allergenliste-vorlage-gastronomie-aichef.pdf'
INJECT = RAIZ / 'scripts/productos-digitales/inject_cache.py'
ARTIKEL = 'https://aichef.pro/de/blog/allergenkennzeichnung'
TITEL = 'Allergenliste – Gastronomie'

SCHWARZ, GOLD, GRAU = '111111', 'FFD700', 'F3F3F3'
duenn = Side(style='thin', color='BBBBBB')
rahmen = Border(left=duenn, right=duenn, top=duenn, bottom=duenn)
eingabe = PatternFill('solid', fgColor='FFF8D6')
schwarz = PatternFill('solid', fgColor=SCHWARZ)
grau = PatternFill('solid', fgColor=GRAU)
NB = ' '

# (Buchstabe, Name, Art nennen?) — österreichische Empfehlung, Reihenfolge von Anhang II LMIV
ALLERGENE = [('A', 'Glutenhaltiges Getreide', True), ('B', 'Krebstiere', False), ('C', 'Ei', False),
             ('D', 'Fisch', False), ('E', 'Erdnuss', False), ('F', 'Soja', False), ('G', 'Milch oder Laktose', False),
             ('H', 'Schalenfrüchte', True), ('L', 'Sellerie', False), ('M', 'Senf', False), ('N', 'Sesam', False),
             ('O', 'Sulfite', False), ('P', 'Lupinen', False), ('R', 'Weichtiere', False)]
BUCHSTABEN = [b for b, _, _ in ALLERGENE]
assert BUCHSTABEN == list('ABCDEFGHLMNOPR') and len(ALLERGENE) == 14
# Kurzname unter dem Buchstaben im PDF («<br/>» = Zeilenumbruch)
KURZ = {'A': 'Getreide<br/>(Art)', 'B': 'Krebs-<br/>tiere', 'C': 'Ei', 'D': 'Fisch', 'E': 'Erd-<br/>nuss',
        'F': 'Soja', 'G': 'Milch,<br/>Laktose', 'H': 'Schalen-<br/>früchte (Art)', 'L': 'Sellerie', 'M': 'Senf',
        'N': 'Sesam', 'O': 'Sulfite', 'P': 'Lupinen', 'R': 'Weich-<br/>tiere'}

# Spalten (1-based): A Gericht · B–O die 14 Allergene · P Spuren · Q Zusatzstoffe · R Anzahl
S_GERICHT, S_ERSTES, S_LETZTES, S_SPUREN, S_ZUSATZ, S_ANZAHL = 1, 2, 15, 16, 17, 18
S_ART = [S_ERSTES + i for i, (_, _, art) in enumerate(ALLERGENE) if art]          # [2, 9] → B und I
S_KREUZ = [S_ERSTES + i for i, (_, _, art) in enumerate(ALLERGENE) if not art]    # C–H und J–O
assert S_ART == [2, 9]
Z_FELD1, Z_FELD2, Z_LEGENDE, Z_GRUPPE, Z_KOPF, ERSTE = 4, 5, 7, 8, 9, 10
ANZ_ZEILEN = 30

ART_HINWEIS = 'Bitte die Art nennen, z. B. Weizen / Haselnuss – „Gluten“ oder „Nüsse“ allein genügt nicht.'
CODE_HINWEIS = ('In Deutschland gibt es keinen amtlichen Buchstaben-Code. Diese Vorlage nutzt die österreichische '
                'Empfehlung (A–R); verwenden Sie den Code nur mit Legende.')
MUENDLICH = ('Mündliche Information ist erlaubt (§ 4 Abs. 4 LMIDV), wenn hinreichend unterrichtetes Personal sie auf '
             'Nachfrage unverzüglich vor der Bestellung gibt, eine schriftliche oder elektronische Dokumentation der '
             'allergenen Zutaten vorliegt, die der Behörde und auf Nachfrage dem Gast leicht zugänglich ist, und ein '
             'gut sichtbarer Hinweis auf beides aufmerksam macht. Beispiel für den Hinweis: „Informationen zu '
             'Allergenen erhalten Sie mündlich von unserem Personal; eine schriftliche Dokumentation liegt auf '
             'Nachfrage zur Einsicht bereit.“')
PRUEFEN = 'Prüfen Sie die Liste bei jeder Rezeptur- oder Lieferantenänderung.'
SPUREN_HINWEIS = ('„Spuren“ ist freiwillig: Tragen Sie dort nur ein echtes Risiko einer Kreuzkontamination ein. '
                  'Ein Spurenhinweis ersetzt nie die Angabe eines Allergens, das als Zutat enthalten ist.')
REZEPTUR_HINWEIS = ('Füllen Sie jede Zeile anhand der Rezeptur aus, nie aus dem Gedächtnis: Grundrezept, Soße, Beilage, '
                    'Dressing, zugekaufte Produkte (Zutatenliste bzw. Produktdatenblatt) und Frittierfett.')
NOTIZEN = [CODE_HINWEIS, ART_HINWEIS, SPUREN_HINWEIS, REZEPTUR_HINWEIS, MUENDLICH, PRUEFEN]
LEGENDE = ('X = enthalten · leer = nicht enthalten · in die Spalten „A · Glutenhaltiges Getreide“ und „H · '
           'Schalenfrüchte“ die Art eintragen (z. B. Weizen, Haselnuss) · „Anzahl Allergene“ berechnet sich automatisch')
ANLEITUNG = ('Füllen Sie die gelben Zellen aus: eine Zeile pro Gericht. In den Spalten „A · Glutenhaltiges Getreide“ '
             'und „H · Schalenfrüchte“ nennen Sie die Art, in den übrigen Allergen-Spalten wählen Sie „X“ aus der '
             'Liste.')
BEISPIEL_HINWEIS = ('Fiktives Beispiel zur Veranschaulichung – typische Rezeptur, an Ihre Rezeptur anpassen. Die Allergene '
                    'Ihrer Gerichte hängen von Ihren Rezepturen und Lieferanten ab. Spuren und Zusatzstoffe sind hier '
                    'nicht ausgefüllt; prüfen Sie zugekaufte Produkte, z. B. Speck (meist Nitritpökelsalz: „mit '
                    'Konservierungsstoff“).')

# (Gericht mit angenommener Rezeptur, {Buchstabe: Wert}) — «X» oder die Art (A, H); alles andere bleibt leer.
BEISPIEL = [
    ('Wiener Schnitzel (Kalb, Panade aus Weizenmehl, Ei und Semmelbröseln, in Butterschmalz ausgebacken) mit '
     'Kartoffelsalat (mit Gemüsebrühe mit Sellerie, Essig-Öl-Marinade mit Senf)',
     {'A': 'Weizen', 'C': 'X', 'G': 'X', 'L': 'X', 'M': 'X'}),
    ('Rinderroulade (Füllung mit Senf, Speck und Gewürzgurke) mit Rotweinsoße (Röstgemüse mit Sellerie, mit '
     'Weizenmehl gebunden)', {'A': 'Weizen', 'L': 'X', 'M': 'X', 'O': 'X'}),
    ('Forelle Müllerin (in Weizenmehl gewendet, in Butter gebraten) mit Petersilienkartoffeln',
     {'A': 'Weizen', 'D': 'X', 'G': 'X'}),
    ('Käsespätzle (Teig aus Weizenmehl und Eiern, Bergkäse) mit Röstzwiebeln (in Weizenmehl gewendet)',
     {'A': 'Weizen', 'C': 'X', 'G': 'X'}),
    ('Apfelstrudel (Strudelteig aus Weizenmehl, Butterbrösel, Füllung mit Mandeln) mit Vanillesoße (Milch, Eigelb)',
     {'A': 'Weizen', 'C': 'X', 'G': 'X', 'H': 'Mandel'}),
]
ANZAHLEN = [5, 4, 3, 3, 4]
assert [len(w) for _, w in BEISPIEL] == ANZAHLEN
assert all(set(w) <= set(BUCHSTABEN) for _, w in BEISPIEL)
assert all((v != 'X') == dict((b, a) for b, _, a in ALLERGENE)[b] for _, w in BEISPIEL for b, v in w.items())


def de(s):
    """Deutsche Typografie: geschütztes Leerzeichen zwischen Zahl und Einheit und in «z. B.», «§ 5», «Abs. 4»."""
    if not isinstance(s, str) or s.startswith('='):
        return s
    s = s.replace('z. B.', f'z.{NB}B.')
    s = re.sub(r'(§|Abs\.|Nr\.) (\d)', r'\1' + NB + r'\2', s)
    return re.sub(r'(\d) (°C|%)(?!\w)', r'\1' + NB + r'\2', s)


# In den Art-Spalten (A, H) bedeuten diese Einträge «nicht enthalten»: orange markiert und nicht mitgezählt.
NEIN_WOERTER = ('nein', 'keine', 'kein')


def art_zaehlt(ref):
    """WAHR (= 1), wenn die Art-Zelle ausgefüllt ist und nicht «nein», «keine» oder «kein» sagt."""
    return 'AND(' + ','.join([f'{ref}<>""'] + [f'LOWER(TRIM({ref}))<>"{w}"' for w in NEIN_WOERTER]) + ')'


def formel_anzahl(z):
    """X in den Kreuz-Spalten + ausgefüllte Art-Zellen (A, H) ohne «nein/keine/kein»; leer ohne Gericht."""
    return (f'=IF(A{z}="","",COUNTIF(C{z}:H{z},"X")+COUNTIF(J{z}:O{z},"X")+{art_zaehlt(f"B{z}")}'
            f'+{art_zaehlt(f"I{z}")})')


def block(ws, zeile, s1, s2, wert=None, eingabe_zelle=False, fett=False, fmt=None, ausr=None):
    """Zelle (verbunden von s1 bis s2) mit Rahmen; openpyxl überträgt den Rahmen beim Verbinden auf den Umriss."""
    c = ws.cell(row=zeile, column=s1, value=de(wert))
    c.border = rahmen
    if eingabe_zelle:
        c.fill = eingabe
    if fett:
        c.font = Font(bold=True, size=10)
    if fmt:
        c.number_format = fmt
    c.alignment = ausr or Alignment(vertical='center', wrap_text=True)
    if s2 > s1:
        ws.merge_cells(start_row=zeile, start_column=s1, end_row=zeile, end_column=s2)
    return c


def blatt(wb, name, beispiel):
    ws = wb.create_sheet(name)
    zeilen = BEISPIEL if beispiel else [None] * ANZ_ZEILEN
    letzte = ERSTE + len(zeilen) - 1

    ws['A1'] = TITEL
    ws['A1'].font = Font(bold=True, size=16, color=GOLD)
    ws['A1'].fill = schwarz
    ws['A1'].alignment = Alignment(vertical='center')
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=S_ANZAHL)
    ws.row_dimensions[1].height = 30
    ws['A2'] = de(BEISPIEL_HINWEIS if beispiel else ANLEITUNG)
    ws['A2'].font = Font(italic=True, bold=beispiel, color='555555')
    ws['A2'].alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=S_ANZAHL)
    ws.row_dimensions[2].height = 30
    ws.row_dimensions[3].height = 6

    links = Alignment(horizontal='left', vertical='center')
    block(ws, Z_FELD1, 1, 1, 'Betrieb', fett=True)
    block(ws, Z_FELD1, 2, 8, 'Gasthaus (fiktives Beispiel)' if beispiel else None, eingabe_zelle=True, ausr=links)
    block(ws, Z_FELD1, 9, 13, 'Geprüft von', fett=True)
    block(ws, Z_FELD1, 14, S_ANZAHL, 'Küchenchef/in' if beispiel else None, eingabe_zelle=True, ausr=links)
    block(ws, Z_FELD2, 1, 1, 'Stand (Datum der letzten Prüfung)', fett=True)
    block(ws, Z_FELD2, 2, 8, datetime.date(2026, 11, 25) if beispiel else None, eingabe_zelle=True, fmt='dd.mm.yyyy',
          ausr=links)
    hinweis = ws.cell(row=Z_FELD2, column=9, value=de(PRUEFEN))
    hinweis.font = Font(italic=True, color='555555', size=9)
    hinweis.alignment = Alignment(vertical='center')
    ws.merge_cells(start_row=Z_FELD2, start_column=9, end_row=Z_FELD2, end_column=S_ANZAHL)
    for z in (Z_FELD1, Z_FELD2):
        ws.row_dimensions[z].height = 20
    ws.row_dimensions[6].height = 6
    dv_datum = DataValidation(type='date', operator='greaterThanOrEqual', formula1='36526', allow_blank=True,
                              showErrorMessage=True, errorTitle='Datum',
                              error=de('Geben Sie ein Datum ein, z. B. 25.11.2026.'))
    ws.add_data_validation(dv_datum)
    dv_datum.add(f'B{Z_FELD2}')

    leg = ws.cell(row=Z_LEGENDE, column=1, value=de(LEGENDE))
    leg.font = Font(bold=True, size=10)
    leg.alignment = Alignment(wrap_text=True, vertical='center')
    ws.merge_cells(start_row=Z_LEGENDE, start_column=1, end_row=Z_LEGENDE, end_column=S_ANZAHL)
    ws.row_dimensions[Z_LEGENDE].height = 27

    for s in range(1, S_ANZAHL + 1):
        ws.cell(row=Z_GRUPPE, column=s).fill = schwarz
    g = ws.cell(row=Z_GRUPPE, column=S_ERSTES,
                value='Die 14 Allergene (Anhang II LMIV) – Buchstaben nach österreichischer Empfehlung')
    g.font = Font(bold=True, size=9, color='FFFFFF')
    g.alignment = Alignment(horizontal='center', vertical='center')
    ws.merge_cells(start_row=Z_GRUPPE, start_column=S_ERSTES, end_row=Z_GRUPPE, end_column=S_LETZTES)

    koepfe = {S_GERICHT: 'Gericht (mit Komponenten: Soße, Beilage, Dressing)', S_SPUREN: 'Spuren (freiwillig)',
              S_ZUSATZ: 'Zusatzstoffe (§ 5 LMZDV, z. B. mit Farbstoff)', S_ANZAHL: 'Anzahl Allergene'}
    for s in range(1, S_ANZAHL + 1):
        c = ws.cell(row=Z_KOPF, column=s)
        c.border = rahmen
        c.fill = grau
        if S_ERSTES <= s <= S_LETZTES:
            b, n, art = ALLERGENE[s - S_ERSTES]
            c.value = f'{b} · {n}' + ('\n(Art nennen)' if art else '')
            c.font = Font(bold=True, size=9)
            # 90° = von unten nach oben; 130 pt Zeilenhöhe: «A · Glutenhaltiges Getreide» (~100 pt in Calibri fett 9)
            # passt in eine Zeile, «(Art nennen)» steht in den breiten Spalten A und H daneben.
            c.alignment = Alignment(text_rotation=90, horizontal='center', vertical='bottom', wrap_text=True)
        else:
            c.value = de(koepfe[s])
            c.font = Font(bold=True, size=10)
            c.alignment = Alignment(horizontal='center' if s == S_ANZAHL else 'left', vertical='bottom', wrap_text=True)
    ws.row_dimensions[Z_KOPF].height = 130

    mitte = Alignment(horizontal='center', vertical='center', wrap_text=True)
    for i, eintrag in enumerate(zeilen):
        z = ERSTE + i
        gericht, werte = eintrag if eintrag else (None, {})
        block(ws, z, S_GERICHT, S_GERICHT, gericht, eingabe_zelle=True)
        for s in range(S_ERSTES, S_LETZTES + 1):
            block(ws, z, s, s, werte.get(BUCHSTABEN[s - S_ERSTES]), eingabe_zelle=True, ausr=mitte)
        block(ws, z, S_SPUREN, S_SPUREN, None, eingabe_zelle=True)
        block(ws, z, S_ZUSATZ, S_ZUSATZ, None, eingabe_zelle=True)
        anz = block(ws, z, S_ANZAHL, S_ANZAHL, formel_anzahl(z), fmt='0', ausr=mitte)
        anz.fill = grau
        anz.font = Font(bold=True)
        # Beispiel: 15 pt je geschätzte Zeile in Spalte A (Breite 44, ~46 Zeichen je Zeile), mindestens 3 Zeilen
        ws.row_dimensions[z].height = 15 * max(3, len(textwrap.wrap(gericht, 46))) if beispiel else 22

    art_bereich = ' '.join(f'{get_column_letter(s)}{ERSTE}:{get_column_letter(s)}{letzte}' for s in S_ART)
    kreuz_bereich = f'C{ERSTE}:H{letzte} J{ERSTE}:O{letzte}'
    dv_kreuz = DataValidation(type='list', formula1='"X"', allow_blank=True, showErrorMessage=True,
                              errorTitle='Allergene', error='Wählen Sie „X“ (enthalten) oder lassen Sie die Zelle leer.')
    ws.add_data_validation(dv_kreuz)
    for b in kreuz_bereich.split():
        dv_kreuz.add(b)
    dv_art = DataValidation(type='textLength', operator='between', formula1='3', formula2='60', allow_blank=True,
                            showErrorMessage=True, showInputMessage=True, errorTitle='Art nennen',
                            error=de('Nennen Sie die Art in 3 bis 60 Zeichen, z. B. Weizen oder Haselnuss – ein „X“ '
                                     'genügt hier nicht.'),
                            promptTitle='Art nennen', prompt=de(ART_HINWEIS))
    ws.add_data_validation(dv_art)
    for b in art_bereich.split():
        dv_art.add(b)
    dv_text = DataValidation(type='textLength', operator='lessThanOrEqual', formula1='250', allow_blank=True,
                             showErrorMessage=True, errorTitle='Text', error='Höchstens 250 Zeichen.')
    ws.add_data_validation(dv_text)
    dv_text.add(f'P{ERSTE}:Q{letzte}')

    # Auf einen Blick: enthalten = rot; «Gluten», «Nüsse» … allein in A/H = orange Warnung (Art fehlt), ebenso
    # «nein», «keine», «kein» (dort leer lassen; die Zelle zählt nicht mit).
    rot = PatternFill('solid', fgColor='F8D7DA', bgColor='F8D7DA')
    orange = PatternFill('solid', fgColor='FFE3B3', bgColor='FFE3B3')
    for b in art_bereich.split():
        erste = b.split(':')[0]
        pruef = ','.join(f'LOWER(TRIM({erste}))="{w}"' for w in ('gluten', 'getreide', 'nüsse', 'nuss', 'schalenfrüchte')
                         + NEIN_WOERTER)
        ws.conditional_formatting.add(b, FormulaRule(formula=[f'OR({pruef})'], stopIfTrue=True,
                                                     font=Font(bold=True, color='8A5300'), fill=orange))
        ws.conditional_formatting.add(b, FormulaRule(formula=[f'{erste}<>""'], font=Font(bold=True, color='9C1C1C'),
                                                     fill=rot))
    for b in kreuz_bereich.split():
        ws.conditional_formatting.add(b, CellIsRule(operator='equal', formula=['"X"'],
                                                    font=Font(bold=True, color='9C1C1C'), fill=rot))

    fz = letzte + 2
    for i, notiz in enumerate(NOTIZEN):
        c = ws.cell(row=fz + i, column=1, value=de(notiz))
        c.font = Font(italic=True, color='555555', size=10)
        c.alignment = Alignment(wrap_text=True, vertical='top')
        ws.merge_cells(start_row=fz + i, start_column=1, end_row=fz + i, end_column=S_ANZAHL)
        ws.row_dimensions[fz + i].height = (54 if len(notiz) > 420 else 40 if len(notiz) > 280
                                            else 27 if len(notiz) > 140 else 15)
    zl = fz + len(NOTIZEN)
    ws.cell(row=zl, column=1, value='Ausführlicher Leitfaden zur Allergenkennzeichnung:').font = Font(size=10)
    link = ws.cell(row=zl, column=2, value=ARTIKEL)
    link.hyperlink = ARTIKEL
    link.font = Font(color='0563C1', underline='single', size=10)
    ws.merge_cells(start_row=zl, start_column=2, end_row=zl, end_column=S_ANZAHL)

    ws.column_dimensions['A'].width = 44
    for s in range(S_ERSTES, S_LETZTES + 1):
        ws.column_dimensions[get_column_letter(s)].width = 11 if s in S_ART else 5
    ws.column_dimensions['P'].width = 18
    ws.column_dimensions['Q'].width = 26
    ws.column_dimensions['R'].width = 10
    ws.freeze_panes = f'B{ERSTE}'
    ws.sheet_view.showGridLines = False
    ws.print_title_rows = f'{Z_GRUPPE}:{Z_KOPF}'
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins.left = ws.page_margins.right = 0.4
    return ws


# ---------------------------------------------------------------- PDF zum Ausdrucken
def pdf_leer():
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase.pdfmetrics import stringWidth
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    def t(s):
        """PDF-Text: deutsche Typografie + WinAnsi der Standardschrift (Helvetica: ä, ö, ü, ß, „ “, –, §, °)."""
        s = de(s).replace('−', '-')
        s.encode('cp1252')  # UnicodeEncodeError, falls ein Zeichen nicht darstellbar wäre (≤, ≥ …)
        return s

    seite = landscape(A4)
    mx, my = 12 * mm, 9 * mm
    doc = SimpleDocTemplate(str(PDF), pagesize=seite, leftMargin=mx, rightMargin=mx, topMargin=my, bottomMargin=my,
                            title=t(TITEL), author='AI Chef Pro',
                            subject=t('Vorlage zum Ausdrucken und Ausfüllen von Hand'))
    W = seite[0] - 2 * mx
    linie = colors.HexColor('#999999')
    s_lab = ParagraphStyle('lab', fontName='Helvetica-Bold', fontSize=8.5, leading=10)
    s_bst = ParagraphStyle('bst', fontName='Helvetica-Bold', fontSize=11, leading=12, alignment=TA_CENTER)
    s_kurz = ParagraphStyle('kurz', fontName='Helvetica', fontSize=5.8, leading=6.6, alignment=TA_CENTER,
                            splitLongWords=0)
    s_kopf = ParagraphStyle('kopf', fontName='Helvetica-Bold', fontSize=8, leading=9.5)
    s_leg = ParagraphStyle('leg', fontName='Helvetica', fontSize=8.5, leading=10.5)
    s_note = ParagraphStyle('note', fontName='Helvetica', fontSize=7.3, leading=9)
    s_fuss = ParagraphStyle('fuss', fontName='Helvetica-Oblique', fontSize=7.5, leading=9.5,
                            textColor=colors.HexColor('#555555'))

    el = []
    band = Table([[t(TITEL)]], colWidths=[W])
    band.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#' + SCHWARZ)),
                              ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#' + GOLD)),
                              ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                              ('FONTSIZE', (0, 0), (-1, -1), 16), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                              ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 10)]))
    el += [band, Spacer(1, 5)]

    felder = Table([[Paragraph('Betrieb', s_lab), '', Paragraph(t('Stand (Datum der letzten Prüfung)'), s_lab), '',
                     Paragraph(t('Geprüft von'), s_lab), '']],
                   colWidths=[W * x for x in (0.07, 0.30, 0.23, 0.12, 0.09, 0.19)], rowHeights=20)
    felder.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, linie), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                *[('BACKGROUND', (c, 0), (c, 0), colors.HexColor('#' + GRAU)) for c in (0, 2, 4)]]))
    el += [felder, Spacer(1, 5)]
    el += [Paragraph(t('<b>X</b> = enthalten · leer = nicht enthalten · Spalten <b>A</b> (Getreide) und <b>H</b> '
                       '(Schalenfrüchte): die Art eintragen (z. B. Weizen, Haselnuss) – „Gluten“ oder „Nüsse“ allein '
                       'genügt nicht.'), s_leg),
           Spacer(1, 3)]

    b_kreuz, b_art, b_spuren, b_zusatz = 27, 46, 66, 86
    b_gericht = W - 12 * b_kreuz - 2 * b_art - b_spuren - b_zusatz
    breiten = [b_gericht] + [b_art if art else b_kreuz for _, _, art in ALLERGENE] + [b_spuren, b_zusatz]
    for (b, _, art), breite in zip(ALLERGENE, breiten[1:15]):
        for zeile in KURZ[b].split('<br/>'):
            assert stringWidth(zeile, 'Helvetica', 5.8) <= breite - 2, (b, zeile)
    kopf = ([Paragraph(t('Gericht <font name="Helvetica" size="6.5">(mit Komponenten: Soße, Beilage, Dressing)</font>'),
                       s_kopf)]
            + [[Paragraph(b, s_bst), Paragraph(t(KURZ[b]), s_kurz)] for b in BUCHSTABEN]
            + [Paragraph(t('Spuren <font name="Helvetica" size="6.5">(freiwillig)</font>'), s_kopf),
               Paragraph(t('Zusatzstoffe<br/><font name="Helvetica" size="6.5">(§ 5 LMZDV)</font>'), s_kopf)])
    anz, hoehe = 16, 20.5  # 7,2 mm je Zeile: genug Platz zum Schreiben von Hand
    matrix = Table([kopf] + [[''] * 17 for _ in range(anz)], colWidths=breiten, rowHeights=[32] + [hoehe] * anz,
                   repeatRows=1)
    matrix.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, linie),
                                ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor('#' + SCHWARZ)),
                                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#' + GRAU)),
                                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#FAFAFA')]),
                                ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
                                ('LEFTPADDING', (1, 0), (14, 0), 1), ('RIGHTPADDING', (1, 0), (14, 0), 1),
                                ('TOPPADDING', (1, 0), (14, 0), 1), ('BOTTOMPADDING', (1, 0), (14, 0), 1)]))
    el += [matrix, Spacer(1, 5)]
    # geschütztes Leerzeichen: der Buchstabe bleibt am Zeilenende nie ohne seinen Namen stehen
    legende = ' · '.join(f'<b>{b}</b>{NB}{n}' + (' (Art nennen)' if art else '') for b, n, art in ALLERGENE)
    el += [Paragraph(t(f'<b>Legende</b> – die 14 Allergene nach Anhang II LMIV: {legende}.'), s_note), Spacer(1, 1.5),
           Paragraph(t(CODE_HINWEIS), s_note), Spacer(1, 1.5),
           Paragraph(t(MUENDLICH), s_note), Spacer(1, 1.5),
           Paragraph(t(PRUEFEN + ' ' + SPUREN_HINWEIS), s_note), Spacer(1, 3),
           Paragraph(t('Kostenlose Vorlage von AI Chef Pro · Leitfaden: aichef.pro/de/blog/allergenkennzeichnung'),
                     s_fuss)]
    doc.build(el)


# ---------------------------------------------------------------- Gates
def cache_text_leer(pfad):
    """inject_cache.py injiziert das Ergebnis «""» nicht: die Zelle behält einen leeren Cache (<v></v>, als 0 gelesen),
    und Betrachter ohne Neuberechnung (macOS-Vorschau, Handy) zeigen «0» in «Anzahl Allergene». Hier wird der Cache
    «leerer Text» wie in Excel geschrieben (t="str" + <v></v>), ohne den Rest des Zip anzufassen (wie im HACCP FR)."""
    muster = re.compile(r'<c r="([A-Z]+[0-9]+)"((?:(?!\st=)[^>])*)>(<f>[^<]*</f>)(?:<v>\s*</v>|<v\s*/>)?</c>')
    with zipfile.ZipFile(pfad) as z:
        teile = [(i, z.read(i.filename)) for i in z.infolist()]
    n = 0
    with zipfile.ZipFile(str(pfad) + '.tmp', 'w', zipfile.ZIP_DEFLATED) as zout:
        for info, daten in teile:
            if re.match(r'xl/worksheets/sheet[0-9]+\.xml$', info.filename):
                xml, k = muster.subn(r'<c r="\1"\2 t="str">\3<v></v></c>', daten.decode('utf-8'))
                daten, n = xml.encode('utf-8'), n + k
            zout.writestr(info, daten)
    shutil.move(str(pfad) + '.tmp', str(pfad))
    return n


def injizieren(pfad):
    aus = subprocess.run([sys.executable, str(INJECT), str(pfad)], check=True, capture_output=True, text=True).stdout
    assert 'fallos_pycel=0' in aus, aus
    m = re.search(r'formulas=(\d+) cache_inyectado=(\d+)', aus)
    leer = cache_text_leer(pfad)
    assert int(m.group(1)) == int(m.group(2)) + leer, (aus, leer)  # jede Formel hat einen Cache
    return f'{aus.strip()} cache_texte_vide={leer}'


def gate_xlsx():
    with zipfile.ZipFile(XLSX) as z:
        ansichten = [z.read(f'xl/worksheets/sheet{i}.xml').decode('utf-8').count('tabSelected="1"') for i in (1, 2)]
        alles = ' '.join(z.read(n).decode('utf-8') for n in z.namelist() if n.endswith('.xml'))
    assert ansichten == [1, 0], f'tabSelected: {ansichten}'
    assert 'DIN 10508' not in alles and 'DEHOGA' not in alles
    wf = load_workbook(XLSX)
    assert wf.sheetnames == ['Allergenliste', 'Beispiel'] and wf.active.title == 'Allergenliste', wf.sheetnames
    for ws, n in ((wf['Allergenliste'], ANZ_ZEILEN), (wf['Beispiel'], len(BEISPIEL))):
        letzte = ERSTE + n - 1
        koepfe = [ws.cell(row=Z_KOPF, column=s).value for s in range(S_ERSTES, S_LETZTES + 1)]
        assert [k.split(' · ')[0] for k in koepfe] == BUCHSTABEN, koepfe
        assert [k.split(' · ')[1].split('\n')[0] for k in koepfe] == [n_ for _, n_, _ in ALLERGENE], koepfe
        assert all(ws.cell(row=Z_KOPF, column=s).alignment.text_rotation == 90 for s in range(S_ERSTES, S_LETZTES + 1))
        assert ws.freeze_panes == f'B{ERSTE}', ws.freeze_panes
        typen = sorted(d.type for d in ws.data_validations.dataValidation)
        assert typen == ['date', 'list', 'textLength', 'textLength'], typen
        assert all(d.showErrorMessage for d in ws.data_validations.dataValidation)
        liste = [d for d in ws.data_validations.dataValidation if d.type == 'list']
        assert len(liste) == 1 and liste[0].formula1 == '"X"', liste
        assert sorted(str(liste[0].sqref).split()) == sorted([f'C{ERSTE}:H{letzte}', f'J{ERSTE}:O{letzte}'])
        art = [d for d in ws.data_validations.dataValidation if d.type == 'textLength' and d.operator == 'between']
        assert len(art) == 1 and (art[0].formula1, art[0].formula2) == ('3', '60') and art[0].showInputMessage
        assert sorted(str(art[0].sqref).split()) == sorted([f'B{ERSTE}:B{letzte}', f'I{ERSTE}:I{letzte}'])
        assert 'Weizen / Haselnuss' in art[0].prompt and 'genügt nicht' in art[0].prompt.replace(NB, ' ')
        for z in range(ERSTE, letzte + 1):
            assert ws.cell(row=z, column=S_ANZAHL).value == formel_anzahl(z)
        assert ws.cell(row=letzte + 1, column=S_ANZAHL).value is None
        texte = ' '.join(str(c.value) for row in ws.iter_rows() for c in row if c.value).replace(NB, ' ')
        for pflicht in (CODE_HINWEIS, ART_HINWEIS, PRUEFEN, MUENDLICH, 'Zusatzstoffe (§ 5 LMZDV, z. B. mit Farbstoff)',
                        'Stand (Datum der letzten Prüfung)', 'Geprüft von', 'Betrieb'):
            assert pflicht in texte, pflicht
        assert any(c.hyperlink and c.hyperlink.target == ARTIKEL for row in ws.iter_rows() for c in row)
    wv = load_workbook(XLSX, data_only=True)
    bsp = wv['Beispiel']
    anzahlen = [bsp.cell(row=ERSTE + i, column=S_ANZAHL).value for i in range(len(BEISPIEL))]
    assert all(isinstance(v, (int, float)) for v in anzahlen), anzahlen
    anzahlen = [int(v) for v in anzahlen]
    assert anzahlen == ANZAHLEN, anzahlen
    for i, (_, werte) in enumerate(BEISPIEL):
        zelle = {b: bsp.cell(row=ERSTE + i, column=S_ERSTES + k).value for k, b in enumerate(BUCHSTABEN)}
        assert {b: v for b, v in zelle.items() if v is not None} == werte, (i, zelle)
        assert sum(v is not None for v in zelle.values()) == anzahlen[i]
        assert all(v in (None, 'X') for b, v in zelle.items() if b not in ('A', 'H'))
        assert bsp.cell(row=ERSTE + i, column=S_SPUREN).value is None
    leer = wv['Allergenliste']
    for z in range(ERSTE, ERSTE + ANZ_ZEILEN):
        assert all(leer.cell(row=z, column=s).value is None for s in range(1, S_ZUSATZ + 1)), z
        assert leer.cell(row=z, column=S_ANZAHL).value in (None, ''), z
    return anzahlen


def gate_logik():
    """Testwerte in einer TEMPORÄREN Kopie: die veröffentlichte Datei bleibt leer."""
    fall = [  # ({Spalte: Wert}, erwartet, Beschreibung)
        ({1: 'Nur Gericht'}, 0, 'Gericht ohne Allergene → 0'),
        ({1: 'Brot', 2: 'Weizen, Roggen'}, 1, 'nur A (Art als Text) → 1'),
        ({1: 'Nusskuchen', 2: 'Weizen', 4: 'X', 8: 'X', 9: 'Haselnuss'}, 4, 'A + C + G + H → 4'),
        ({1: 'Kleinbuchstabe', 3: 'x'}, 1, '„x“ klein geschrieben zählt wie „X“ → 1'),
        ({1: 'Spuren', 16: 'Sesam', 17: 'mit Farbstoff'}, 0, 'Spuren und Zusatzstoffe zählen nicht → 0'),
        ({3: 'X', 9: 'Walnuss'}, None, 'Allergene ohne Gericht → leer'),
        ({}, None, 'leere Zeile → leer'),
        ({1: 'Alle 14', **{s: ('Weizen' if s == 2 else 'Pistazie' if s == 9 else 'X') for s in range(2, 16)}}, 14,
         'alle 14 Allergene → 14'),
        ({1: 'Salat', 2: 'nein', 9: 'kein'}, 0, '„nein“ in A und „kein“ in H zählen nicht → 0'),
        # «Keine» groß geschrieben; Leerzeichen am Rand nicht testbar: TRIM von pycel 1.0b30 kürzt nur
        # Mehrfach-Leerzeichen, das von Excel/LibreOffice entfernt sie auch am Anfang und Ende.
        ({1: 'Omelett', 2: 'Keine', 4: 'X', 9: 'Haselnuss'}, 2, '„Keine“ in A zählt nicht, C + H zählen → 2'),
    ]
    with tempfile.TemporaryDirectory() as tmp:
        kopie = Path(tmp) / 'test.xlsx'
        shutil.copy(XLSX, kopie)
        wb = load_workbook(kopie)
        for i, (werte, _, _) in enumerate(fall):
            for s, v in werte.items():
                wb['Allergenliste'].cell(row=ERSTE + i, column=s, value=v)
        wb.save(kopie)
        injizieren(kopie)
        wv = load_workbook(kopie, data_only=True)
        erg = []
        for i, (_, erw, beschr) in enumerate(fall):
            v = wv['Allergenliste'].cell(row=ERSTE + i, column=S_ANZAHL).value
            erg.append((beschr, erw, None if v == '' else int(v) if isinstance(v, float) else v))
    for beschr, erw, v in erg:
        print(f'  {"OK " if erw == v else "KO "} {beschr} → {v!r} (erwartet {erw!r})')
    assert all(erw == v for _, erw, v in erg), 'Gate Logik KO'
    return len(erg)


def gate_pdf():
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        from pypdf import PdfReader
        leser = PdfReader(str(PDF))
        seiten = len(leser.pages)
        assert seiten == 1, f'{seiten} Seiten'
        p = leser.pages[0]
        assert float(p.mediabox.width) > float(p.mediabox.height), 'nicht quer'
        text = ' '.join(p.extract_text().replace(NB, ' ').split())
    fehlend = [m for m in ('Glutenhaltiges Getreide', 'Schalenfrüchte', 'Weichtiere', 'Milch oder Laktose', 'Sellerie',
                           'Stand (Datum der letzten Prüfung)', 'Geprüft von', '§ 4 Abs. 4 LMIDV', '§ 5 LMZDV',
                           'österreichische Empfehlung (A–R)', 'keinen amtlichen Buchstaben-Code',
                           '„Informationen zu Allergenen erhalten Sie mündlich von unserem Personal',
                           'Rezeptur- oder Lieferantenänderung', TITEL, 'aichef.pro/de/blog/allergenkennzeichnung')
                if m not in text]
    assert not fehlend, fehlend
    assert 'DIN' not in text and 'DEHOGA' not in text
    legende = text[text.index('Legende'):]
    for b, n, _ in ALLERGENE:
        assert f'{b} {n}' in legende, (b, n)
    return seiten


def main():
    wb = Workbook()
    wb.remove(wb.active)
    leer = blatt(wb, 'Allergenliste', False)
    bsp = blatt(wb, 'Beispiel', True)
    leer.sheet_view.tabSelected = True
    bsp.sheet_view.tabSelected = False
    wb.active = 0
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.title = TITEL
    XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb.save(XLSX)
    print(injizieren(XLSX))
    anzahlen = gate_xlsx()
    n_logik = gate_logik()
    pdf_leer()
    seiten = gate_pdf()
    print(f'OK {XLSX.name} · leer {ANZ_ZEILEN} Zeilen × 14 Allergene (Code A–R) · Beispiel Anzahlen {anzahlen} '
          f'· Gate Logik {n_logik}/{n_logik} · {PDF.name} {seiten} Seite')


if __name__ == '__main__':
    main()
