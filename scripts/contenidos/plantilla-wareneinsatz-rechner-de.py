#!/usr/bin/env python3
"""Wareneinsatz-Rechner (DE), plantilla Excel GRATIS — lead magnet de /de/blog/wareneinsatz-berechnen.

Keywords DE (nov-2026): «wareneinsatz berechnen» 1.000/mes, «wareneinsatzquote» 210.
Sale: astro-site/public/descargas/wareneinsatz-rechner-vorlage-aichef.xlsx (sin PDF) — 3 hojas:
  «Beispiel»      el ejemplo del post: 8.400 + 12.600 − 7.800 = 13.200 € · 13.200 ÷ 44.000 = 30 %
                  (Speisen 32 %, Getränke 24 %). El reparto Speisen/Getränke de inventarios y compras
                  es ilustrativo y la hoja lo dice.
  «Monat (leer)»  la misma tabla vacía + ayuda Bruttoumsatz → Nettoumsatz (7 % / 19 %). Hoja activa.
  «12 Monate»     enero-diciembre, cuotas por categoría y total, fila del año y aviso suave cuando la
                  cuota sube más de 2 puntos frente al mes anterior.
Sin «Branchenwerte»: el post insiste en comparar la evolución propia, no un valor del sector.
El xlsx pasa por inject_cache.py (valores calculados), un gate data_only, un gate de lógica con pycel
(rellena las hojas vacías en memoria y comprueba los cálculos) y parche_xml_xlsx.py --check.
`/descargas/*` está en noindex (netlify.toml).
"""
import re
import subprocess
import sys
import zipfile
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

RAIZ = Path(__file__).resolve().parents[2]
XLSX = RAIZ / 'astro-site/public/descargas/wareneinsatz-rechner-vorlage-aichef.xlsx'
ARTIKEL = 'https://aichef.pro/de/blog/wareneinsatz-berechnen'

SCHWARZ, GOLD, GRAU = '111111', 'FFD700', 'F3F3F3'
duenn = Side(style='thin', color='BBBBBB')
rahmen = Border(left=duenn, right=duenn, top=duenn, bottom=duenn)
eingabe_fill = PatternFill('solid', fgColor='FFF8D6')
grau_fill = PatternFill('solid', fgColor=GRAU)
warn_fill = PatternFill('solid', fgColor='FBE3E3')
EUR = '#,##0.00 "€"'
PCT = '0.0 %'
NB = ' '  # espacio de no separación entre cifra y unidad («8.400 €», «30 %»)

# Ejemplo del post: (Kategorie, Anfangsbestand, Einkäufe, Endbestand, Nettoumsatz)
BEISPIEL = [('Speisen', 5900, 10080, 5420, 33000), ('Getränke', 2500, 2520, 2380, 11000)]
MONATE = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober',
          'November', 'Dezember']
UST_SPEISEN, UST_GETRAENKE = 0.07, 0.19
UST_HINWEIS = ('Seit dem 1. Januar 2026 gilt für Speisen in der Gastronomie dauerhaft der ermäßigte Steuersatz von '
               f'7{NB}% (auch außer Haus und bei Lieferung); Getränke bleiben bei 19{NB}%. Prüfen Sie Sonderfälle '
               '(z. B. Kombiangebote) mit Ihrer Steuerberatung.')
FUSS = ['Alle Werte netto, also ohne Mehrwertsteuer: Wareneinsatz und Umsatz.',
        'Ohne Inventur am Monatsanfang und am Monatsende keine echte Quote.']

# Filas fijas de las hojas mensuales
Z_KOPF, Z_SPEISEN, Z_GETRAENKE, Z_GESAMT = 8, 9, 10, 11
# Filas fijas de «12 Monate»
J_KOPF, J_ERSTER = 7, 8
J_LETZTER = J_ERSTER + 11
J_JAHR = J_LETZTER + 1


def balken(ws, zeile, text, bis):
    c = ws.cell(row=zeile, column=1, value=text)
    c.font = Font(bold=True, color='FFFFFF')
    c.fill = PatternFill('solid', fgColor=SCHWARZ)
    ws.merge_cells(start_row=zeile, start_column=1, end_row=zeile, end_column=bis)


def kopf(ws, titel, anleitung, bis):
    ws['A1'] = titel
    ws['A1'].font = Font(bold=True, size=16, color=GOLD)
    ws['A1'].fill = PatternFill('solid', fgColor=SCHWARZ)
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=bis)
    ws.row_dimensions[1].height = 26
    ws['A2'] = anleitung
    ws['A2'].font = Font(italic=True, color='555555')
    ws['A2'].alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=bis)
    ws.row_dimensions[2].height = 30


def zelle(ws, r, c, wert=None, fmt=None, eingabe=False, fett=False, grau=False):
    z = ws.cell(row=r, column=c, value=wert)
    z.border = rahmen
    if fmt:
        z.number_format = fmt
    if eingabe:
        z.fill = eingabe_fill
    elif grau:
        z.fill = grau_fill
    if fett:
        z.font = Font(bold=True)
    z.alignment = Alignment(wrap_text=True, vertical='center')
    return z


def ueberschriften(ws, zeile, texte):
    for col, txt in enumerate(texte, start=1):
        z = zelle(ws, zeile, col, txt, fett=True, grau=True)
        z.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
    ws.row_dimensions[zeile].height = 32


def stammdaten(ws, felder, bis):
    for i, (etikett, wert) in enumerate(felder):
        r = 4 + i
        zelle(ws, r, 1, etikett, fett=True)
        zelle(ws, r, 2, wert, eingabe=True)
        for c in range(3, bis + 1):
            ws.cell(row=r, column=c).border = rahmen
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=bis)


def dv_betrag(ws):
    dv = DataValidation(type='decimal', operator='greaterThanOrEqual', formula1='0', allow_blank=True,
                        showErrorMessage=True, errorTitle='Ungültiger Betrag',
                        error='Bitte geben Sie einen Betrag von 0 oder mehr ein (nur die Zahl, z. B. 8400).')
    ws.add_data_validation(dv)
    return dv


def notiz(ws, zeile, text, bis, hoehe=None, kursiv=True, fill=None):
    c = ws.cell(row=zeile, column=1, value=text)
    c.font = Font(italic=kursiv, color='555555')
    c.alignment = Alignment(wrap_text=True, vertical='top')
    if fill:
        c.fill = fill
    ws.merge_cells(start_row=zeile, start_column=1, end_row=zeile, end_column=bis)
    if hoehe:
        ws.row_dimensions[zeile].height = hoehe


def fuss(ws, zeile, bis):
    """Notas generales + enlace al artículo, al pie de cada hoja."""
    balken(ws, zeile, 'Wichtig', bis)
    for i, txt in enumerate(FUSS):
        notiz(ws, zeile + 1 + i, txt, bis, kursiv=False)
    r = zeile + 1 + len(FUSS)
    ws.cell(row=r, column=1, value='Anleitung mit durchgerechnetem Beispiel:').font = Font(bold=True)
    link = ws.cell(row=r, column=2, value=ARTIKEL)
    link.hyperlink = ARTIKEL
    link.font = Font(color='0563C1', underline='single')
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=bis)
    notiz(ws, r + 1, 'Kostenlose Vorlage von AI Chef Pro (aichef.pro). Sie dürfen sie kopieren und anpassen.', bis)


def druck(ws, breiten):
    for col, w in breiten.items():
        ws.column_dimensions[col].width = w
    ws.sheet_view.showGridLines = False
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True


def blatt_monat(wb, name, beispiel):
    ws = wb.create_sheet(name)
    if beispiel:
        anleitung = ('Beispiel aus dem Artikel: So sieht ein ausgefüllter Monat aus. Ihre eigenen Zahlen tragen Sie '
                     'im Blatt „Monat (leer)“ ein.')
    else:
        anleitung = ('Füllen Sie nur die gelben Zellen aus. Wareneinsatz und Wareneinsatzquote werden automatisch '
                     'berechnet.')
    kopf(ws, 'Wareneinsatz-Rechner', anleitung, 7)
    stammdaten(ws, [('Monat/Jahr', 'Beispielmonat' if beispiel else None),
                    ('Betrieb', 'Beispielrestaurant (fiktiv)' if beispiel else None)], 7)

    balken(ws, 7, 'Wareneinsatz und Wareneinsatzquote (netto)', 7)
    ueberschriften(ws, Z_KOPF, ['Kategorie', 'Anfangsbestand (€)', 'Einkäufe (€)', 'Endbestand (€)',
                                'Wareneinsatz (€)', 'Nettoumsatz (€)', 'Wareneinsatzquote'])
    dv = dv_betrag(ws)
    for i, r in enumerate((Z_SPEISEN, Z_GETRAENKE)):
        kat, anfang, einkauf, ende, umsatz = BEISPIEL[i]
        zelle(ws, r, 1, kat, fett=True)
        for col, wert in ((2, anfang), (3, einkauf), (4, ende), (6, umsatz)):
            z = zelle(ws, r, col, wert if beispiel else None, EUR, eingabe=True)
            dv.add(z.coordinate)
        # Wareneinsatz = Anfangsbestand + Einkäufe − Endbestand (vacío hasta tener los tres valores)
        zelle(ws, r, 5, f'=IF(OR(B{r}="",C{r}="",D{r}=""),"",B{r}+C{r}-D{r})', EUR, grau=True)
        # Quote = Wareneinsatz ÷ Nettoumsatz (vacía sin Umsatz)
        zelle(ws, r, 7, f'=IF(OR(E{r}="",N(F{r})=0),"",E{r}/F{r})', PCT, grau=True)
    g, s1, s2 = Z_GESAMT, Z_SPEISEN, Z_GETRAENKE
    zelle(ws, g, 1, 'Gesamt', fett=True, grau=True)
    for col in 'BCDF':
        zelle(ws, g, ' ABCDEFG'.index(col), f'=IF(AND({col}{s1}="",{col}{s2}=""),"",SUM({col}{s1}:{col}{s2}))',
              EUR, fett=True, grau=True)
    zelle(ws, g, 5, f'=IF(OR(B{g}="",C{g}="",D{g}=""),"",B{g}+C{g}-D{g})', EUR, fett=True, grau=True)
    zelle(ws, g, 7, f'=IF(OR(E{g}="",N(F{g})=0),"",E{g}/F{g})', PCT, fett=True, grau=True)
    for r in (s1, s2, g):
        ws.row_dimensions[r].height = 20
    # Wareneinsatz negativo = error de inventario o de compras
    ws.conditional_formatting.add(f'E{s1}:E{g}', CellIsRule(operator='lessThan', formula=['0'],
                                                             font=Font(bold=True, color='9C1C1C'), fill=warn_fill))

    notiz(ws, 13, 'Wareneinsatz = Anfangsbestand + Einkäufe − Endbestand · Wareneinsatzquote = Wareneinsatz ÷ '
                  'Nettoumsatz', 7, kursiv=False)
    notiz(ws, 14, 'Füllen Sie jede Zeile vollständig aus. Der Endbestand dieses Monats ist der Anfangsbestand des '
                  'nächsten. Ein negativer Wareneinsatz (rot markiert) deutet auf einen Fehler in der Inventur oder '
                  'bei den Einkäufen hin.', 7, hoehe=30)
    weiter = 16
    if beispiel:
        balken(ws, weiter, 'Hinweis zum Beispiel', 7)
        notiz(ws, weiter + 1,
              'Beispielzahlen aus dem Artikel. Die Aufteilung von Anfangsbestand, Einkäufen und Endbestand auf '
              'Speisen und Getränke ist zur Veranschaulichung angenommen. Die Gesamtwerte (8.400' + NB + '€ + '
              '12.600' + NB + '€ − 7.800' + NB + '€ = 13.200' + NB + '€; 13.200' + NB + '€ ÷ 44.000' + NB + '€ = '
              '30' + NB + '%) und die Quoten von 32' + NB + '% (Speisen) und 24' + NB + '% (Getränke) entsprechen '
              'dem Artikel.', 7, hoehe=46, kursiv=False)
        weiter += 3
    else:
        balken(ws, weiter, 'Hilfsrechnung: Bruttoumsatz → Nettoumsatz', 7)
        ueberschriften(ws, weiter + 1, ['Kategorie', 'Bruttoumsatz (€)', 'MwSt.-Satz', 'Nettoumsatz (€)'])
        dv_satz = DataValidation(type='decimal', operator='between', formula1='0', formula2='0.99', allow_blank=True,
                                 showErrorMessage=True, errorTitle='Steuersatz',
                                 error='Geben Sie den Steuersatz als Prozentwert ein, z. B. 7 % (oder 0,07).')
        ws.add_data_validation(dv_satz)
        for i, (kat, satz) in enumerate((('Speisen', UST_SPEISEN), ('Getränke', UST_GETRAENKE))):
            r = weiter + 2 + i
            zelle(ws, r, 1, kat, fett=True)
            dv.add(zelle(ws, r, 2, None, EUR, eingabe=True).coordinate)
            dv_satz.add(zelle(ws, r, 3, satz, '0 %', eingabe=True).coordinate)
            zelle(ws, r, 4, f'=IF(B{r}="","",ROUND(B{r}/(1+N(C{r})),2))', EUR, fett=True, grau=True)
            ws.row_dimensions[r].height = 20
        notiz(ws, weiter + 4, 'Übertragen Sie den Nettoumsatz in die Spalte „Nettoumsatz“ der Tabelle oben.', 7,
              kursiv=False)
        notiz(ws, weiter + 5, UST_HINWEIS, 7, hoehe=46)
        weiter += 7
    fuss(ws, weiter, 7)
    druck(ws, {'A': 24, 'B': 17, 'C': 15, 'D': 17, 'E': 17, 'F': 17, 'G': 17})
    return ws


def blatt_jahr(wb):
    ws = wb.create_sheet('12 Monate')
    kopf(ws, 'Wareneinsatz-Rechner: 12 Monate im Vergleich',
         'Tragen Sie pro Monat Wareneinsatz und Nettoumsatz ein (gelbe Zellen). Die Quoten werden automatisch berechnet.',
         8)
    stammdaten(ws, [('Jahr', None), ('Betrieb', None)], 8)
    ueberschriften(ws, J_KOPF, ['Monat', 'Wareneinsatz Speisen (€)', 'Nettoumsatz Speisen (€)', 'Quote Speisen',
                                'Wareneinsatz Getränke (€)', 'Nettoumsatz Getränke (€)', 'Quote Getränke',
                                'Quote gesamt'])
    ws.row_dimensions[J_KOPF].height = 46
    dv = dv_betrag(ws)
    for i, monat in enumerate(MONATE):
        r = J_ERSTER + i
        zelle(ws, r, 1, monat, fett=True)
        for col in (2, 3, 5, 6):
            dv.add(zelle(ws, r, col, None, EUR, eingabe=True).coordinate)
        zelle(ws, r, 4, f'=IF(OR(B{r}="",N(C{r})=0),"",B{r}/C{r})', PCT, grau=True)
        zelle(ws, r, 7, f'=IF(OR(E{r}="",N(F{r})=0),"",E{r}/F{r})', PCT, grau=True)
        zelle(ws, r, 8, f'=IF(OR(D{r}="",G{r}=""),"",(B{r}+E{r})/(C{r}+F{r}))', PCT, grau=True)
        ws.row_dimensions[r].height = 18
    a, z, j = J_ERSTER, J_LETZTER, J_JAHR
    zelle(ws, j, 1, 'Jahr gesamt¹', fett=True, grau=True)
    # Año: solo los meses cuya cuota existe (Wareneinsatz y Umsatz de esa categoría), para que suma y cuota casen.
    for wcol, ucol, qcol in (('B', 'C', 'D'), ('E', 'F', 'G')):
        for col in (wcol, ucol):
            zelle(ws, j, ' ABCDEFGH'.index(col),
                  f'=IF(COUNT({qcol}{a}:{qcol}{z})=0,"",SUMIF({qcol}{a}:{qcol}{z},">=0",{col}{a}:{col}{z}))',
                  EUR, fett=True, grau=True)
        zelle(ws, j, ' ABCDEFGH'.index(qcol), f'=IF(OR({wcol}{j}="",N({ucol}{j})=0),"",{wcol}{j}/{ucol}{j})', PCT,
              fett=True, grau=True)
    # Cuota global del año: solo los meses con cuota global (Speisen y Getränke completos), sin mezclar meses.
    zelle(ws, j, 8, f'=IF(COUNT(H{a}:H{z})=0,"",SUMPRODUCT(--ISNUMBER(H{a}:H{z}),B{a}:B{z}+E{a}:E{z})'
                    f'/SUMPRODUCT(--ISNUMBER(H{a}:H{z}),C{a}:C{z}+F{a}:F{z}))', PCT, fett=True, grau=True)
    ws.row_dimensions[j].height = 20
    # Aviso suave: la cuota sube más de 2 puntos frente al mes anterior (desde febrero; ROUND evita 0,32−0,30 > 0,02)
    for col in 'DGH':
        ws.conditional_formatting.add(
            f'{col}{a + 1}:{col}{z}',
            FormulaRule(formula=[f'AND(ISNUMBER({col}{a + 1}),ISNUMBER({col}{a}),ROUND({col}{a + 1}-{col}{a},4)>0.02)'],
                        fill=warn_fill, font=Font(bold=True, color='9C1C1C')))

    r = j + 2
    notiz(ws, r, 'Hellrot markiert: Die Quote liegt mehr als 2 Prozentpunkte über der des Vormonats.', 8,
          kursiv=False, fill=warn_fill)
    notiz(ws, r + 1, 'Vergleichen Sie Ihre Quote Monat für Monat: Entscheidend ist die Entwicklung, nicht ein '
                     'Branchenwert.', 8, kursiv=False)
    notiz(ws, r + 2, '¹ Jahressummen und Jahresquoten berücksichtigen nur die Monate, in denen Wareneinsatz und Nettoumsatz '
                     'der jeweiligen Kategorie eingetragen sind. „Quote gesamt“ erscheint, sobald Speisen und Getränke '
                     'vollständig eingetragen sind.', 8, hoehe=30)
    notiz(ws, r + 3, 'Tipp: Legen Sie für jeden Monat eine Kopie des Blatts „Monat (leer)“ an (Rechtsklick auf den '
                     'Blattreiter → Verschieben oder kopieren) und übertragen Sie die Ergebnisse in diese Tabelle.', 8, hoehe=30)
    fuss(ws, r + 5, 8)
    druck(ws, {'A': 16, 'B': 15, 'C': 15, 'D': 12, 'E': 15, 'F': 15, 'G': 12, 'H': 12})
    return ws


def injizieren():
    out = subprocess.run([sys.executable, str(RAIZ / 'scripts/productos-digitales/inject_cache.py'), str(XLSX)],
                         check=True, capture_output=True, text=True).stdout.strip()
    m = re.search(r'formulas=(\d+) cache_inyectado=(\d+) fallos_pycel=(\d+)', out)
    assert m and m.group(3) == '0', out
    return out


def gate_datei():
    """Gate sobre el libro publicado (data_only = lo que ve un visor que no recalcula)."""
    wf = load_workbook(XLSX)
    assert wf.sheetnames == ['Beispiel', 'Monat (leer)', '12 Monate'], wf.sheetnames
    assert wf.active.title == 'Monat (leer)', wf.active.title
    with zipfile.ZipFile(XLSX) as zf:
        sel = [n for n in sorted(zf.namelist()) if re.match(r'xl/worksheets/sheet\d+\.xml$', n)
               and 'tabSelected="1"' in zf.read(n).decode('utf-8')]
    assert sel == ['xl/worksheets/sheet2.xml'], sel
    for ws in wf.worksheets:
        assert any(c.hyperlink and c.hyperlink.target == ARTIKEL for row in ws.iter_rows() for c in row), ws.title
        textos = [c.value for row in ws.iter_rows() for c in row if isinstance(c.value, str)]
        for frase in FUSS:
            assert frase in textos, (ws.title, frase)
        dvs = ws.data_validations.dataValidation
        assert dvs and all(d.showErrorMessage for d in dvs), ws.title
        assert ws.page_setup.orientation == 'landscape' and ws.page_setup.fitToWidth == 1, ws.title
        # nada de «Branchenwerte»: ningún texto con un porcentaje de referencia salvo los del ejemplo y el IVA
        for t in textos:
            for pct in re.findall(r'(\d+)\s?%', t):
                assert pct in ('7', '19', '30', '32', '24'), (ws.title, t)
    wv = load_workbook(XLSX, data_only=True)
    bsp = wv['Beispiel']
    we = [bsp.cell(row=r, column=5).value for r in (Z_SPEISEN, Z_GETRAENKE, Z_GESAMT)]
    assert all(isinstance(v, (int, float)) for v in we), we
    we = [round(v) for v in we]
    assert we == [10560, 2640, 13200], we
    assert we[2] == we[0] + we[1]
    summen = [round(bsp.cell(row=Z_GESAMT, column=c).value) for c in (2, 3, 4, 6)]
    assert summen == [8400, 12600, 7800, 44000], summen
    quoten = [round(bsp.cell(row=r, column=7).value, 2) for r in (Z_SPEISEN, Z_GETRAENKE, Z_GESAMT)]
    assert quoten == [0.32, 0.24, 0.30], quoten
    # hojas vacías: ninguna fórmula enseña error ni un número
    for nombre in ('Monat (leer)', '12 Monate'):
        for row in wf[nombre].iter_rows():
            for c in row:
                if c.data_type == 'f':
                    v = wv[nombre][c.coordinate].value
                    assert v in (None, ''), (nombre, c.coordinate, v)
    leer = wv['Monat (leer)']
    assert [leer.cell(row=r, column=3).value for r in (18, 19)] == [UST_SPEISEN, UST_GETRAENKE]
    assert any(c.value == UST_HINWEIS for row in leer.iter_rows() for c in row)
    return round(bsp.cell(row=Z_GESAMT, column=5).value), round(bsp.cell(row=Z_GESAMT, column=7).value * 100)


def gate_logik():
    """Rellena en memoria (pycel) las hojas vacías y comprueba los cálculos, incluidos los casos incompletos."""
    import contextlib
    import logging
    import os
    logging.disable(logging.CRITICAL)
    from pycel import ExcelCompiler
    xl = ExcelCompiler(filename=str(XLSX))

    def setze(blatt, werte):
        for ref, v in werte.items():
            wert(blatt, ref)  # pycel solo deja cambiar celdas que ya están en su mapa
            xl.set_value(f"'{blatt}'!{ref}", v)

    def wert(blatt, ref):
        with open(os.devnull, 'w') as dn, contextlib.redirect_stderr(dn):
            v = xl.evaluate(f"'{blatt}'!{ref}")
        return v.item() if hasattr(v, 'item') else v

    m = 'Monat (leer)'
    # Solo Speisen completo; Getränke vacío → Gesamt = Speisen. Bruto → neto reproduce el Umsatz del artículo.
    setze(m, {'B9': 5900, 'C9': 10080, 'D9': 5420, 'F9': 33000, 'B18': 35310, 'B19': 13090})
    assert round(wert(m, 'E9')) == 10560 and round(wert(m, 'G9'), 2) == 0.32
    assert wert(m, 'E10') in (None, '') and wert(m, 'G10') in (None, '')
    assert round(wert(m, 'E11')) == 10560 and round(wert(m, 'G11'), 2) == 0.32
    assert (wert(m, 'D18'), wert(m, 'D19')) == (33000, 11000), (wert(m, 'D18'), wert(m, 'D19'))
    # Fila a medias → Wareneinsatz y Quote vacíos; Umsatz 0 → Quote vacía, sin #DIV/0!
    setze(m, {'B10': 2500, 'F10': 0})
    assert wert(m, 'E10') in (None, '') and wert(m, 'G10') in (None, '')
    setze(m, {'C10': 2520, 'D10': 2380})
    assert round(wert(m, 'E10')) == 2640 and wert(m, 'G10') in (None, '')
    assert round(wert(m, 'E11')) == 13200

    j = '12 Monate'
    setze(j, {'B8': 9900, 'C8': 33000, 'E8': 2640, 'F8': 11000,      # enero 30 % / 24 % / 28,5 %
              'B9': 10560, 'C9': 33000, 'E9': 2860, 'F9': 11000,     # febrero 32 % / 26 %
              'B10': 11550, 'C10': 33000,                             # marzo 35 %, sin bebidas
              'B11': 10000})                                          # abril: sin Umsatz → fuera del año
    assert [round(wert(j, f'D{r}'), 3) for r in (8, 9, 10)] == [0.30, 0.32, 0.35]
    assert round(wert(j, 'H8'), 3) == 0.285 and wert(j, 'H10') in (None, '') and wert(j, 'D11') in (None, '')
    assert round(wert(j, 'B20')) == 32010 and round(wert(j, 'C20')) == 99000  # abril (sin Umsatz) no cuenta
    assert round(wert(j, 'D20'), 4) == round(32010 / 99000, 4)
    assert round(wert(j, 'E20')) == 5500 and round(wert(j, 'G20'), 2) == 0.25
    assert round(wert(j, 'H20'), 4) == round((9900 + 10560 + 2640 + 2860) / (33000 + 33000 + 11000 + 11000), 4)  # solo ene y feb
    # Regla del aviso: +2 puntos exactos no avisa, +3 sí (misma aritmética que la fórmula del formato condicional)
    assert not round(0.32 - 0.30, 4) > 0.02 and round(0.35 - 0.32, 4) > 0.02
    reglas = [r.formula[0] for rng in load_workbook(XLSX)[j].conditional_formatting for r in rng.rules]
    assert 'AND(ISNUMBER(D9),ISNUMBER(D8),ROUND(D9-D8,4)>0.02)' in reglas, reglas
    assert len(reglas) == 3, reglas
    return 'OK'


def main():
    wb = Workbook()
    wb.remove(wb.active)
    blatt_monat(wb, 'Beispiel', True)
    blatt_monat(wb, 'Monat (leer)', False)
    blatt_jahr(wb)
    for i, ws in enumerate(wb.worksheets):
        ws.sheet_view.tabSelected = (i == 1)
    wb.active = 1
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.title = 'Wareneinsatz-Rechner'
    XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb.save(XLSX)
    print(injizieren())
    we, quote = gate_datei()
    n = gate_logik()
    chk = subprocess.run([sys.executable, str(RAIZ / 'scripts/productos-digitales/parche_xml_xlsx.py'), '--check',
                          str(XLSX)], cwd=RAIZ, capture_output=True, text=True)
    print(chk.stdout.strip())
    assert chk.returncode == 0, chk.stdout + chk.stderr
    print(f'OK {XLSX.name} · Beispiel {we:,} € / {quote} %'.replace(',', '.') +
          f' · 3 Blätter · Logik-Gate {n} · aktiv „Monat (leer)“')


if __name__ == '__main__':
    main()
