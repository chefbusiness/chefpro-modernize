#!/usr/bin/env python3
"""HACCP-lijsten horeca (NL), GRATIS — lead magnet de /nl/blog/hygienecode y /nl/blog/haccp-betekenis.

Gemelo neerlandés de plantilla-haccp-vorlagen-de.py (mismo diseño negro/oro, celdas amarillas, validaciones con
mensaje, formato condicional rojo, inject_cache + caché «texto vacío», gate de lógica sobre COPIAS con pycel, una sola
pestaña seleccionada, A4), ADAPTADO a la Hygiënecode voor de Horeca 2026 de KHN. Los formularios v2 de KHN se usaron
SOLO para saber qué se registra y con qué norma; ni su maquetación ni sus textos se copian. Solo valores dados:
  - «Koelingen en vriezers»: 6 apparaten editables (4 koelingen ≤ 7 °C, 2 vriezers ≤ −18 °C, ley) y 5 semanas: display
    Ma–Zo + meting semanal con thermometer gekalibreerd; «In orde?» = MAX de la fila ≤ norm de la fila.
  - «Kritische punten»: los CCP de la code 2026 son koken ≥ 75 °C, terugkoelen ≥ 75 → ≤ 7 °C en ≤ 5 uur con
    tijd/temp start (obligatoria), na 2 uur (richtwaarde ≤ 20 °C: si solo falla eso, «Let op» y no «NEE»; F en ámbar,
    rojo solo con «NEE») y eind, y regenereren ≥ 60 °C en ≤ 60 min; warmhouden ≥ 60 °C (ley) NO es CCP: se mide cada
    semana y se apunta (recomendado; obligatorio con afwijking). Normas en celdas amarillas; duración con MOD(…;1)
    (medianoche). Fuentes: 75 °C de inicio, 60 minuten y 75 °C para todo = solo la code 2026 (formularios KHN); la
    NVWA solo aconseja kip en gehakt ≥ 75 °C, afkoelen binnen 5 uur onder 7 °C y opwarmen ≥ 60 °C.
  - «In orde?» = "" si falta un dato necesario o si hay TEXTO en una celda numérica (dato o norma): «abc» >= 75 es
    VERDADERO en Excel y daba «Ja». Gate con texto en cada bloque, también en «Voorbeeld».
  - «Ontvangst»: solo desviaciones; gekoeld max. 7 °C, rauw gevogelte max. 4 °C, diepvries −15 °C of kouder.
  - «Thermometer»: control anual, afwijking max. ±1,0 °C (bijv. smeltend ijs 0 °C).
  - «Voorbeeld»: semana 48 (23–29 nov 2026) rellenada; UNA afwijking (koelwerkbank wo 9,0 °C) con su maatregel.
Formatos pensados para Quick Look (vista previa de macOS/iPhone, probado con qlmanage): la norma se muestra con una
fórmula de texto («max. 7 °C», «−18 °C of kouder») y no con un formato numérico de secciones; la duración de terugkoelen
va en [h]:mm y la de regenereren en minutos enteros ('[h]" u "mm"' y '[m]" min"' salen como «4 1899 30 12»).
Keywords NL (LowFruits, nov-2026): «hygiënecode horeca» 260, «haccp horeca lijsten» 110, «haccp horeca» 90.

Uso:  python3 scripts/contenidos/plantilla-haccp-lijsten-nl.py
Sale: astro-site/public/descargas/haccp-lijsten-horeca-aichef.xlsx  (5 hojas; las 4 plantillas sin valores de prueba)
      astro-site/public/descargas/haccp-lijsten-horeca-aichef.pdf   (A4, 4 páginas, a mano: koelingen, kritische punten,
      ontvangst, thermometer, como las 4 plantillas del Excel)
Después:
  python3 scripts/productos-digitales/parche_xml_xlsx.py --check astro-site/public/descargas/haccp-lijsten-horeca-aichef.xlsx
`/descargas/*` está en noindex (netlify.toml). Sesión Claude Code, 25-nov-2026.
"""
import datetime
import math
import re
import shutil
import subprocess
import sys
import tempfile
import warnings
import zipfile
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.pagebreak import Break

RAIZ = Path(__file__).resolve().parents[2]
XLSX = RAIZ / 'astro-site/public/descargas/haccp-lijsten-horeca-aichef.xlsx'
PDF = RAIZ / 'astro-site/public/descargas/haccp-lijsten-horeca-aichef.pdf'
INJECT = RAIZ / 'scripts/productos-digitales/inject_cache.py'
ARTIKEL = 'https://aichef.pro/nl/blog/hygienecode'
VOET = 'Gratis hulpmiddel van AI Chef Pro · Uitleg: aichef.pro/nl/blog/hygienecode'

ZWART, GOUD, GRIJS = '111111', 'FFD700', 'F3F3F3'
dun = Side(style='thin', color='BBBBBB')
rand = Border(left=dun, right=dun, top=dun, bottom=dun)
invoer = PatternFill('solid', fgColor='FFF8D6')
rood = PatternFill('solid', fgColor='F8CBAD')
oranje = PatternFill('solid', fgColor='FFE699')
grijs = PatternFill('solid', fgColor=GRIJS)
zwart = PatternFill('solid', fgColor=ZWART)
NB = ' '
F_TEMP = '0.0'
F_AFW = '+0.0;-0.0;0.0'
F_TIJD = 'hh:mm'
# Quick Look (macOS-voorvertoning, iPhone) toont '[h]" u "mm"', '[m]" min"' en getalformaten met tekstsecties fout
# (getest: «4 1899 30 12»): duur terugkoelen als [h]:mm, duur regenereren als hele minuten, normen als tekstformule.
F_DUUR_U = '[h]:mm'
F_DUUR_M = '0" min"'
F_DATUM = 'dd-mm-yyyy'

# ------------------------------------------------------------------ teksten (notas del brief, literales)
NOTA_WET = ('Wettelijke grenzen: gekoeld ten hoogste 7 °C (art. 15 Warenwetbesluit Bereiding en behandeling van '
            'levensmiddelen; voorverpakt: de temperatuur van de fabrikant), warmhouden ten minste 60 °C (art. 15 lid 2), '
            'diepgevroren ten hoogste −18 °C (Warenwetregeling Diepgevroren levensmiddelen).')
NOTA_CODE = ('Koken ≥ 75 °C, terugkoelen van ≥ 75 °C naar ≤ 7 °C binnen 5 uur en regenereren binnen 60 minuten tot '
             '≥ 60 °C zijn normen uit de nieuwe Hygiënecode Horeca (2026), zoals op de formulieren van KHN; geen '
             'wetsartikelen. De NVWA adviseert kip en gehakt tot ≥ 75 °C te verhitten, binnen 5 uur af te koelen tot '
             'onder 7 °C en op te warmen tot ≥ 60 °C.')
NOTA_WARM = 'Warmhouden: elke week meten; vastleggen wordt aanbevolen en is verplicht bij een afwijking.'
NOTA_REGISTRATIE = ('De wet schrijft geen dagelijkse lijst voor: registreer wat uw hygiënecode of HACCP-plan vraagt. In de '
                    'hygiënecode 2026 is meten van koelingen verplicht en registreren verplicht bij een afwijking; '
                    'kritische punten meet en registreert u wekelijks.')
NOTA_BEWAAR = 'Bewaar de lijsten minimaal zes maanden (advies KHN).'
NOTA_2016 = ('De Hygiënecode voor de Horeca 2016 mag u gebruiken tot en met 31 maart 2027; daarna controleert de NVWA '
             'met de nieuwe code.')
NOTA_HULP = 'Dit is een hulpmiddel, geen officieel formulier van de NVWA of KHN.'
NOTA_ONTVANGST = ('Meten bij ontvangst blijft verplicht; vastleggen hoeft alleen bij een afwijking, samen met de actie '
                  '(Hygiënecode voor de Horeca 2026).')
BRON_CODE = 'Hygiënecode voor de Horeca 2026 en advies van de NVWA'  # alleen 7 °C en 5 uur (NVWA: afkoelen)
BRON_CODE26 = 'Hygiënecode voor de Horeca 2026'
BRON_KOKEN = 'Hygiënecode 2026 (NVWA-advies: kip en gehakt ≥ 75 °C)'
BRON_REGEN = 'Hygiënecode 2026; NVWA: opwarmen tot ≥ 60 °C'
WET_KOEL = 'Gekoeld: ten hoogste 7 °C (art. 15 Warenwetbesluit Bereiding en behandeling van levensmiddelen)'
WET_VRIES = 'Diepgevroren: ten hoogste −18 °C (Warenwetregeling Diepgevroren levensmiddelen)'
VERBODEN = ('100 °C', '80 °C', '72 °C', '74 °C', '3 dagen', 'DIN', 'BfR', 'FAVV', 'Vlaanderen')

# (naam, norm °C) — 4 koelingen (wet: ≤ 7 °C) en 2 vriezers (wet: ≤ −18 °C); in gele cellen aan te passen
APPARATEN = [('Koelcel', 7), ('Koelkast keuken', 7), ('Koelwerkbank', 7), ('Barkoeling', 7), ('Vriezer', -18),
             ('Vriescel', -18)]
N_APP = len(APPARATEN)
T0 = 7                 # kopregel van de apparatentabel (rijen 8–13)
W0 = 16                # eerste weekblok
BLOK = N_APP + 3       # band + kop + 6 rijen + lege rij
N_WEKEN = 5
DAGEN = ['Ma', 'Di', 'Wo', 'Do', 'Vr', 'Za', 'Zo']
KOP_KOEL = ['Apparaat', 'Norm'] + DAGEN + ['Meting thermometer (°C)', 'In orde?', 'Afwijking? Correctieve maatregel',
                                           'Paraaf']
BREEDTE_GRID = {'A': 26, 'B': 16, 'C': 9, 'D': 9, 'E': 9, 'F': 9, 'G': 9, 'H': 9, 'I': 9, 'J': 12, 'K': 9, 'L': 38,
                'M': 8}

# Normen kritische punten (sleutel, omschrijving, waarde, eenheid, bron) — in gele cellen aan te passen
NORMEN = [
    ('koken_t', 'Koken – kerntemperatuur ten minste', 75, '°C', BRON_KOKEN),
    ('terug_start', 'Terugkoelen – kerntemperatuur bij de start ten minste', 75, '°C', BRON_CODE26),
    ('terug_2u', 'Terugkoelen – na 2 uur ten hoogste (richtwaarde)', 20, '°C', 'Hygiënecode voor de Horeca 2026 '
                                                                               '(richtwaarde)'),
    ('terug_eind', 'Terugkoelen – kerntemperatuur aan het eind ten hoogste', 7, '°C', BRON_CODE),
    ('terug_d', 'Terugkoelen – duur ten hoogste', 5, 'uur', BRON_CODE),
    ('regen_t', 'Regenereren – kerntemperatuur ten minste', 60, '°C', BRON_REGEN),
    ('regen_d', 'Regenereren – duur ten hoogste', 60, 'minuten', BRON_CODE26),
    ('warm_t', 'Warmhouden – temperatuur ten minste', 60, '°C',
     'Wet: art. 15 lid 2 Warenwetbesluit Bereiding en behandeling van levensmiddelen'),
]
N0 = 7                 # kopregel van de normentabel (rijen 8–15)
V = {k: f'$E${N0 + 1 + i}' for i, (k, _, _, _, _) in enumerate(NORMEN)}
V_LIT = {k: str(w) for k, _, w, _, _ in NORMEN}  # Voorbeeld: dezelfde normen als vaste getallen
N_RIJEN = 8            # rijen per kritisch punt
CCP_ORDE = ['koken', 'terug', 'regen', 'warm']
# (kop, eerste kolom, laatste kolom, soort) op het raster A–M van «Koelingen en vriezers»
CCP_KOL = {
    'koken': [('Product', 1, 1, 'tekst'), ('Datum', 2, 2, 'datum'), ('Tijd', 3, 3, 'tijd'),
              ('Kerntemp. (°C)', 4, 4, 'temp'), ('In orde?', 5, 5, 'ok'),
              ('Correctieve maatregel (bij afwijking)', 6, 12, 'tekst'), ('Paraaf', 13, 13, 'paraaf')],
    'terug': [('Product', 1, 1, 'tekst'), ('Datum', 2, 2, 'datum'), ('Tijd start', 3, 3, 'tijd'),
              ('Temp. start (°C)', 4, 4, 'temp'), ('Tijd na 2 uur', 5, 5, 'tijd'), ('Temp. na 2 uur (°C)', 6, 6, 'temp'),
              ('Tijd eind', 7, 7, 'tijd'), ('Temp. eind (°C)', 8, 8, 'temp'), ('Duur (u:mm)', 9, 10, 'duur_u'),
              ('In orde?', 11, 11, 'ok'), ('Correctieve maatregel', 12, 12, 'tekst'), ('Paraaf', 13, 13, 'paraaf')],
    'regen': [('Product', 1, 1, 'tekst'), ('Datum', 2, 2, 'datum'), ('Tijd start', 3, 3, 'tijd'),
              ('Tijd norm bereikt', 4, 4, 'tijd'), ('Kerntemp. (°C)', 5, 5, 'temp'), ('Duur', 6, 6, 'duur_m'),
              ('In orde?', 7, 7, 'ok'), ('Correctieve maatregel (bij afwijking)', 8, 12, 'tekst'),
              ('Paraaf', 13, 13, 'paraaf')],
    'warm': [('Product', 1, 1, 'tekst'), ('Datum', 2, 2, 'datum'), ('Tijd meting', 3, 3, 'tijd'),
             ('Laagste temp. (°C)', 4, 4, 'temp'), ('In orde?', 5, 5, 'ok'),
             ('Correctieve maatregel (bij afwijking)', 6, 12, 'tekst'), ('Paraaf', 13, 13, 'paraaf')],
}
OK_KOL = {art: next(k1 for _, k1, _, s in kol if s == 'ok') for art, kol in CCP_KOL.items()}

ONTVANGST = [('Gekoeld', 7), ('Rauw gevogelte', 4), ('Diepvries', -15)]
O0 = 7                 # kopregel normen ontvangst (rijen 8–10)
O_KOP, O_N = 13, 20    # kopregel en aantal rijen van de ontvangstlijst
TH_NORM = 7            # cel C7: afwijking ten hoogste
TH_KOP, TH_N = 9, 12

# Voorbeeld: week 48 (ma 23 t/m zo 29 november 2026), één afwijking
VB_VELDEN = ['Eetcafé Het Voorbeeld (fictief)', 'Week 48 (23 t/m 29 november 2026)', 'S. de Vries']
VB_WEEK = 48
VB_MAATREGEL = ('Wo 14:00: display 9,0 °C; de deur stond open na de levering. Deur gesloten en producten gemeten '
                '(kern 6,5 °C, in orde). Om 14:30 opnieuw gemeten: 5,0 °C.')
VB_KOEL = [  # (display ma–zo, wekelijkse meting, maatregel)
    ([3.0, 3.5, 3.0, 4.0, 3.5, 4.0, 3.5], 3.8, None),
    ([4.0, 4.5, 4.0, 4.0, 5.0, 4.5, 4.0], 4.3, None),
    ([5.0, 5.5, 9.0, 5.0, 5.5, 6.0, 5.0], 5.2, VB_MAATREGEL),
    ([5.0, 5.0, 5.5, 5.0, 6.0, 6.5, 5.5], 5.6, None),
    ([-20.0, -20.0, -19.0, -20.0, -21.0, -20.0, -20.0], -19.5, None),
    ([-22.0, -21.0, -22.0, -22.0, -21.0, -22.0, -22.0], -21.0, None),
]


def hm(h, m):
    return (h * 60 + m) / 1440


VB_CCP = {  # {kolom: waarde}
    'koken': {1: 'Kippendijen uit de combisteamer', 2: datetime.date(2026, 11, 24), 3: hm(12, 15), 4: 82.0, 13: 'MB'},
    'terug': {1: 'Runderbouillon in GN-bakken, ijswaterbad', 2: datetime.date(2026, 11, 25), 3: hm(14, 0), 4: 85.0,
              5: hm(16, 0), 6: 18.0, 7: hm(18, 30), 8: 6.0, 13: 'MB'},
    'regen': {1: 'Stoofvlees, per portie', 2: datetime.date(2026, 11, 26), 3: hm(17, 30), 4: hm(17, 55), 5: 72.0,
              13: 'JK'},
    'warm': {1: 'Soep van de dag, au bain-marie', 2: datetime.date(2026, 11, 27), 3: hm(19, 0), 4: 68.0, 13: 'JK'},
}


def norm_tekst(ref):
    """Formuledeel: 7 → «max. 7 °C», −18 → «−18 °C of kouder» (tekst, leesbaar in elke viewer)."""
    return f'IF({ref}<0,"−"&ABS({ref})&"{NB}°C of kouder","max. "&{ref}&"{NB}°C")'


def nl(s):
    """Nederlandse typografie: harde spatie tussen getal en eenheid, na ≤/≥ en in «art. 15», «lid 2»."""
    if not isinstance(s, str) or s.startswith('='):
        return s
    s = re.sub(r'\b(art\.|lid|nr\.) (\d)', r'\1' + NB + r'\2', s)
    s = re.sub(r'([≤≥±]) (?=[\d−])', r'\1' + NB, s)
    return re.sub(r'(\d) (°C|uur|u|min|minuten|%)(?![\wëéï])', r'\1' + NB + r'\2', s)


def cel(ws, r, k, waarde=None, fmt=None, inv=False, vet=False, fond=None, wrap=True, mid=False, grootte=None):
    c = ws.cell(row=r, column=k, value=nl(waarde))
    c.border = rand
    if fmt:
        c.number_format = fmt
    if inv:
        c.fill = invoer
    elif fond:
        c.fill = fond
    if vet or grootte:
        c.font = Font(bold=vet, size=grootte or 11)
    c.alignment = Alignment(wrap_text=wrap, vertical='center' if mid else 'top', horizontal='center' if mid else None)
    return c


def samen(ws, r, k1, k2, r2=None):
    if k2 > k1 or (r2 and r2 > r):
        ws.merge_cells(start_row=r, start_column=k1, end_row=r2 or r, end_column=k2)


def rand_bereik(ws, r, k1, k2, fond=None):
    for k in range(k1, k2 + 1):
        ws.cell(row=r, column=k).border = rand
        if fond:
            ws.cell(row=r, column=k).fill = fond


def bladkop(ws, titel, uitleg, laatste):
    ws['A1'] = nl(titel)
    ws['A1'].font = Font(bold=True, size=16, color=GOUD)
    ws['A1'].fill = zwart
    samen(ws, 1, 1, laatste)
    ws.row_dimensions[1].height = 24
    ws['A2'] = nl(uitleg)
    ws['A2'].font = Font(italic=True, color='555555')
    ws['A2'].alignment = Alignment(wrap_text=True, vertical='top')
    samen(ws, 2, 1, laatste)
    ws.row_dimensions[2].height = 30


def velden(ws, namen, label_tot, invoer_tot, waarden=None):
    for i, naam in enumerate(namen):
        r = 3 + i
        cel(ws, r, 1, naam, vet=True)
        rand_bereik(ws, r, 1, label_tot)
        samen(ws, r, 1, label_tot)
        cel(ws, r, label_tot + 1, waarden[i] if waarden else None, inv=True)
        rand_bereik(ws, r, label_tot + 1, invoer_tot)
        samen(ws, r, label_tot + 1, invoer_tot)


def kopregel(ws, r, koppen, hoogte=32):
    """koppen: lijst van (tekst, k1, k2)."""
    for tekst, k1, k2 in koppen:
        c = ws.cell(row=r, column=k1, value=nl(tekst))
        c.font = Font(bold=True, color='FFFFFF')
        c.alignment = Alignment(wrap_text=True, horizontal='center', vertical='center')
        rand_bereik(ws, r, k1, k2, zwart)
        samen(ws, r, k1, k2)
    ws.row_dimensions[r].height = hoogte


def notities(ws, r, teksten, laatste, hoogte=30):
    for i, n in enumerate(teksten):
        c = ws.cell(row=r + i, column=1, value=nl(n))
        c.font = Font(italic=True, color='555555')
        c.alignment = Alignment(wrap_text=True, vertical='top')
        samen(ws, r + i, 1, laatste)
        ws.row_dimensions[r + i].height = hoogte
    return r + len(teksten)


def artikel_link(ws, r, laatste, tot=2):
    ws.cell(row=r, column=1, value=nl('Uitleg over de hygiënecode voor de horeca:')).font = Font(bold=True)
    samen(ws, r, 1, tot)
    c = ws.cell(row=r, column=tot + 1, value=ARTIKEL)
    c.hyperlink = ARTIKEL
    c.font = Font(color='0563C1', underline='single')
    samen(ws, r, tot + 1, laatste)


def pagina(ws, fixeren, breedtes, breuken=()):
    for k, w in breedtes.items():
        ws.column_dimensions[k].width = w
    ws.sheet_view.showGridLines = False
    if fixeren:
        ws.freeze_panes = fixeren
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    for r in breuken:
        ws.row_breaks.append(Break(id=r))


def _dv(ws, bereik, **kw):
    dv = DataValidation(allow_blank=True, showErrorMessage=True, **kw)
    ws.add_data_validation(dv)
    for b in bereik.split():
        dv.add(b)


def toets_temp(ws, bereik, mini, maxi):
    _dv(ws, bereik, type='decimal', operator='between', formula1=str(mini), formula2=str(maxi), errorTitle='Temperatuur',
        error=f'Vul een temperatuur (°C) in tussen {mini} en {maxi}, bijv. 3,5 of -18.')


def toets_geheel(ws, bereik, mini, maxi, titel):
    _dv(ws, bereik, type='whole', operator='between', formula1=str(mini), formula2=str(maxi), errorTitle=titel,
        error=f'Vul een geheel getal in tussen {mini} en {maxi}.')


def toets_tijd(ws, bereik):
    _dv(ws, bereik, type='time', operator='between', formula1='0', formula2='0.999305556', errorTitle='Tijd',
        error='Vul een tijd in als uu:mm (bijv. 14:30).')


def toets_datum(ws, bereik):
    _dv(ws, bereik, type='date', operator='greaterThanOrEqual', formula1='36526', errorTitle='Datum',
        error='Vul een datum in, bijv. 25-11-2026.')


def cf_rood(ws, bereik, formule):
    ws.conditional_formatting.add(bereik, FormulaRule(formula=[formule], fill=rood))


def cf_nee(ws, bereik):
    ws.conditional_formatting.add(bereik, CellIsRule(operator='equal', formula=['"NEE"'], fill=rood,
                                                     font=Font(bold=True)))


# ------------------------------------------------------------------ apparatentabel + weekblok (ook in «Voorbeeld»)
def apparaten_tabel(ws):
    for (a, b), txt in (((1, 1), 'Apparaat'), ((2, 4), 'Naam (aan te passen)'), ((5, 5), 'Norm (°C)'),
                        ((6, 13), 'Wettelijke grens')):
        cel(ws, T0, a, txt, vet=True, fond=grijs)
        rand_bereik(ws, T0, a, b, grijs)
        samen(ws, T0, a, b)
    koel, vries = nl(WET_KOEL), nl(WET_VRIES)
    for i, (naam, norm) in enumerate(APPARATEN):
        r = T0 + 1 + i
        cel(ws, r, 1, f'Apparaat {i + 1}', vet=True)
        cel(ws, r, 2, naam, inv=True)
        rand_bereik(ws, r, 2, 4)
        samen(ws, r, 2, 4)
        cel(ws, r, 5, norm, '0', inv=True, vet=True, mid=True)
        c = cel(ws, r, 6, f'=IF(E{r}="","",IF(E{r}<0,"{vries}","{koel}"))', grootte=9)
        c.alignment = Alignment(vertical='center', wrap_text=True)
        rand_bereik(ws, r, 6, 13)
        samen(ws, r, 6, 13)
        ws.row_dimensions[r].height = 18
    toets_geheel(ws, f'E{T0 + 1}:E{T0 + N_APP}', -40, 30, 'Norm')


def geen_getal(*refs):
    """Formuledeel, WAAR als een van de cellen geen getal is (leeg of tekst). Nodig omdat Excel tekst groter vindt dan
    elk getal: «abc» >= 75 is WAAR en gaf «Ja»."""
    return 'OR(' + ','.join(f'NOT(ISNUMBER({r}))' for r in refs) + ')'


def formule_koel(z, t):
    # MAX en COUNT slaan tekst over: «9,0» als tekst in een dagcel gaf «Ja» → tekst in de rij geeft leeg
    return (f'=IF(OR({geen_getal(f"$E${t}")},COUNT(C{z}:J{z})=0,SUMPRODUCT(--ISTEXT(C{z}:J{z}))>0),"",'
            f'IF(MAX(C{z}:J{z})<=$E${t},"Ja","NEE"))')


def week_blok(ws, r, week=None, data=None):
    c = ws.cell(row=r, column=1, value='Week')
    c.font = Font(bold=True, color=GOUD)
    c.fill = zwart
    c.border = rand
    c.alignment = Alignment(horizontal='right', vertical='center')
    cel(ws, r, 2, week, '0', inv=True, vet=True, mid=True)
    b = ws.cell(row=r, column=3, value=nl('Display: elke dag aflezen (°C) · Meting: één keer per week met een '
                                          'gekalibreerde thermometer'))
    b.font = Font(italic=True, color='FFFFFF')
    b.alignment = Alignment(vertical='center')
    rand_bereik(ws, r, 3, 13, zwart)
    samen(ws, r, 3, 13)
    ws.row_dimensions[r].height = 20
    kopregel(ws, r + 1, [(t, k, k) for k, t in enumerate(KOP_KOEL, start=1)])
    e = r + 2
    for i in range(N_APP):
        z, t = e + i, T0 + 1 + i
        rij = data[i] if data else ([None] * 7, None, None)
        cel(ws, z, 1, f'=IF($B${t}="","",$B${t})', vet=True, mid=False)
        ws.cell(row=z, column=1).alignment = Alignment(vertical='center', wrap_text=True)
        cel(ws, z, 2, f'=IF($E${t}="","",{norm_tekst(f"$E${t}")})', mid=True)
        for k, w in enumerate(rij[0] + [rij[1]], start=3):
            cel(ws, z, k, w, F_TEMP, inv=True, mid=True)
        cel(ws, z, 11, formule_koel(z, t), mid=True)
        cel(ws, z, 12, rij[2], inv=True)
        cel(ws, z, 13, 'SdV' if data else None, inv=True, mid=True)
        ws.row_dimensions[z].height = 15 * math.ceil(len(rij[2]) / 40) + 4 if rij[2] else 20
    l = e + N_APP - 1
    toets_temp(ws, f'C{e}:J{l}', -40, 30)
    toets_geheel(ws, f'B{r}', 1, 53, 'Weeknummer')
    for i in range(N_APP):  # de norm staat per apparaat in de tabel bovenaan (kolom B is tekst)
        z, t = e + i, T0 + 1 + i
        cf_rood(ws, f'C{z}:J{z}', f'AND(ISNUMBER(C{z}),ISNUMBER($E${t}),C{z}>$E${t})')
    cf_nee(ws, f'K{e}:K{l}')
    return e


# ------------------------------------------------------------------ kritische punten (ook in «Voorbeeld»)
def band_ccp(art, v):
    if art == 'koken':
        return f'="Koken – kerntemperatuur ten minste "&{v["koken_t"]}&"{NB}°C"'
    if art == 'terug':
        return (f'="Terugkoelen – van ten minste "&{v["terug_start"]}&"{NB}°C naar ten hoogste "&{v["terug_eind"]}'
                f'&"{NB}°C binnen "&{v["terug_d"]}&"{NB}uur · richtwaarde na 2{NB}uur: ten hoogste "&{v["terug_2u"]}'
                f'&"{NB}°C"')
    if art == 'regen':
        return (f'="Regenereren – binnen "&{v["regen_d"]}&"{NB}minuten tot een kerntemperatuur van ten minste "'
                f'&{v["regen_t"]}&"{NB}°C"')
    return (f'="Warmhouden – ten minste "&{v["warm_t"]}&"{NB}°C, gemeten op de koudste plek · elke week meten; '
            f'vastleggen aanbevolen, verplicht bij een afwijking"')


def formule_ccp(art, soort, z, v):
    if art in ('koken', 'warm'):
        n = v['koken_t' if art == 'koken' else 'warm_t']
        return f'=IF({geen_getal(f"D{z}", n)},"",IF(D{z}>={n},"Ja","NEE"))'
    if art == 'terug':
        if soort == 'duur_u':
            return f'=IF({geen_getal(f"C{z}", f"G{z}")},"",MOD(G{z}-C{z},1))'
        # start, eind en duur zijn nodig (zonder starttemperatuur: leeg, geen «Ja»); de 2-uursmeting mag ontbreken,
        # maar tekst erin geeft leeg. Alleen de richtwaarde na 2 uur overschreden → «Let op», niet «NEE».
        nodig = geen_getal(f'I{z}', f'H{z}', f'D{z}', v['terug_d'], v['terug_eind'], v['terug_start'], v['terug_2u'])
        return (f'=IF(OR({nodig},AND(F{z}<>"",NOT(ISNUMBER(F{z})))),"",IF(AND(ROUND(I{z}*1440,0)<={v["terug_d"]}*60,'
                f'H{z}<={v["terug_eind"]},D{z}>={v["terug_start"]}),IF(OR(F{z}="",F{z}<={v["terug_2u"]}),"Ja",'
                f'"Let op"),"NEE"))')
    if soort == 'duur_m':
        return f'=IF({geen_getal(f"C{z}", f"D{z}")},"",ROUND(MOD(D{z}-C{z},1)*1440,0))'
    return (f'=IF({geen_getal(f"F{z}", f"E{z}", v["regen_d"], v["regen_t"])},"",'
            f'IF(AND(F{z}<={v["regen_d"]},E{z}>={v["regen_t"]}),"Ja","NEE"))')


def ccp_blok(ws, r, art, n, v, data=None):
    b = ws.cell(row=r, column=1, value=band_ccp(art, v))
    b.font = Font(bold=True, size=12, color=GOUD)
    b.alignment = Alignment(vertical='center')
    rand_bereik(ws, r, 1, 13, zwart)
    samen(ws, r, 1, 13)
    ws.row_dimensions[r].height = 22
    kol = CCP_KOL[art]
    kopregel(ws, r + 1, [(t, k1, k2) for t, k1, k2, _ in kol], hoogte=44)
    e = r + 2
    for z in range(e, e + n):
        for _, k1, k2, soort in kol:
            w = data.get(k1) if data else None
            if soort in ('ok', 'duur_u', 'duur_m'):
                fmt = {'ok': None, 'duur_u': F_DUUR_U, 'duur_m': F_DUUR_M}[soort]
                cel(ws, z, k1, formule_ccp(art, soort, z, v), fmt, mid=True)
                rand_bereik(ws, z, k1, k2)
            else:
                fmt = {'datum': F_DATUM, 'tijd': F_TIJD, 'temp': F_TEMP}.get(soort)
                cel(ws, z, k1, w, fmt, inv=True, mid=soort not in ('tekst',))
                if soort == 'tekst':
                    ws.cell(row=z, column=k1).alignment = Alignment(wrap_text=True, vertical='center')
                for k in range(k1 + 1, k2 + 1):
                    ws.cell(row=z, column=k).border = rand
                    ws.cell(row=z, column=k).fill = invoer
            samen(ws, z, k1, k2)
        ws.row_dimensions[z].height = 30 if data else 22
    l = e + n - 1
    kl = {s: [] for s in ('datum', 'tijd', 'temp')}
    for _, k1, _, soort in kol:
        if soort in kl:
            kl[soort].append(k1)
    letter = ' ABCDEFGHIJKLM'
    toets_datum(ws, ' '.join(f'{letter[k]}{e}:{letter[k]}{l}' for k in kl['datum']))
    toets_tijd(ws, ' '.join(f'{letter[k]}{e}:{letter[k]}{l}' for k in kl['tijd']))
    toets_temp(ws, ' '.join(f'{letter[k]}{e}:{letter[k]}{l}' for k in kl['temp']), -30, 110)
    ok = letter[OK_KOL[art]]
    cf_nee(ws, f'{ok}{e}:{ok}{l}')
    if art == 'koken':
        regels = [('D', f'AND(ISNUMBER(D{e}),D{e}<{v["koken_t"]})')]
    elif art == 'warm':
        regels = [('D', f'AND(ISNUMBER(D{e}),D{e}<{v["warm_t"]})')]
    elif art == 'terug':
        regels = [('D', f'AND(ISNUMBER(D{e}),D{e}<{v["terug_start"]})'),
                  ('F', f'AND(ISNUMBER(F{e}),F{e}>{v["terug_2u"]},K{e}="NEE")'),
                  ('H', f'AND(ISNUMBER(H{e}),H{e}>{v["terug_eind"]})'),
                  ('I', f'AND(ISNUMBER(I{e}),I{e}*1440>{v["terug_d"]}*60+0.5)')]
        # 2-uursmeting boven de richtwaarde: rood alleen als het resultaat «NEE» is, anders oranje (zoals «Let op»)
        ws.conditional_formatting.add(f'F{e}:F{l}', FormulaRule(
            formula=[f'AND(ISNUMBER(F{e}),F{e}>{v["terug_2u"]},K{e}<>"NEE")'], fill=oranje))
        ws.conditional_formatting.add(f'K{e}:K{l}', CellIsRule(operator='equal', formula=['"Let op"'], fill=oranje,
                                                               font=Font(bold=True)))
    else:
        regels = [('E', f'AND(ISNUMBER(E{e}),E{e}<{v["regen_t"]})'),
                  ('F', f'AND(ISNUMBER(F{e}),F{e}>{v["regen_d"]})')]
    for k, f in regels:
        cf_rood(ws, f'{k}{e}:{k}{l}', f)
    return e


# ------------------------------------------------------------------ Blad 1: Koelingen en vriezers
def blad_koelingen(wb):
    ws = wb.create_sheet('Koelingen en vriezers')
    bladkop(ws, 'HACCP-lijst koelingen en vriezers',
            'Vul de gele cellen in. Lees elke dag het display af en meet één keer per week met een gekalibreerde '
            'thermometer. “In orde?” wordt automatisch ingevuld; bij een afwijking noteert u de correctieve maatregel '
            'en uw paraaf.', 13)
    velden(ws, ['Bedrijf', 'Week/maand', 'Verantwoordelijke'], 1, 4)
    apparaten_tabel(ws)
    notities(ws, T0 + N_APP + 1, ['Vul hier uw eigen apparaten en normen in; ze verschijnen vanzelf in de weken '
                                  'hieronder. Een strengere norm uit uw HACCP-plan mag u hier invullen.'], 13, 18)
    starts = [week_blok(ws, W0 + j * BLOK) for j in range(N_WEKEN)]
    fz = notities(ws, W0 + N_WEKEN * BLOK, [
        NOTA_WET, NOTA_REGISTRATIE,
        'Elke rode waarde vraagt om een correctieve maatregel en een nieuwe meting die laat zien dat de norm weer '
        'wordt gehaald.',
        NOTA_BEWAAR, NOTA_2016, NOTA_HULP], 13)
    artikel_link(ws, fz + 1, 13)
    pagina(ws, 'C3', BREEDTE_GRID, breuken=(W0 + BLOK - 1, W0 + 3 * BLOK - 1))
    return starts


# ------------------------------------------------------------------ Blad 2: Kritische punten
def blad_kritisch(wb):
    ws = wb.create_sheet('Kritische punten')
    bladkop(ws, 'HACCP-lijst kritische punten (koken, terugkoelen, regenereren) en warmhouden',
            'Meet en registreer de kritische punten één keer per week. ' + NOTA_WARM + ' Vul de gele cellen in '
            '(tijden als uu:mm). Duur en “In orde?” worden automatisch berekend met de normen in de tabel hieronder.', 13)
    ws.row_dimensions[2].height = 44
    velden(ws, ['Bedrijf', 'Week/maand', 'Verantwoordelijke'], 1, 4)
    for (a, b), txt in (((1, 4), 'Norm (aan te passen)'), ((5, 5), 'Waarde'), ((6, 7), 'Eenheid'), ((8, 13), 'Bron')):
        cel(ws, N0, a, txt, vet=True, fond=grijs)
        rand_bereik(ws, N0, a, b, grijs)
        samen(ws, N0, a, b)
    for i, (_, tekst, waarde, eenheid, bron) in enumerate(NORMEN):
        r = N0 + 1 + i
        cel(ws, r, 1, tekst)
        rand_bereik(ws, r, 1, 4)
        samen(ws, r, 1, 4)
        cel(ws, r, 5, waarde, inv=True, vet=True, mid=True)
        cel(ws, r, 6, eenheid)
        rand_bereik(ws, r, 6, 7)
        samen(ws, r, 6, 7)
        cel(ws, r, 8, bron, grootte=9)
        rand_bereik(ws, r, 8, 13)
        samen(ws, r, 8, 13)
        ws.row_dimensions[r].height = 18
    temps = ' '.join(V[k].replace('$', '') for k in ('koken_t', 'terug_start', 'terug_2u', 'terug_eind', 'regen_t',
                                                     'warm_t'))
    toets_geheel(ws, temps, -30, 110, 'Norm')
    toets_geheel(ws, V['terug_d'].replace('$', ''), 1, 24, 'Uren')
    toets_geheel(ws, V['regen_d'].replace('$', ''), 1, 1440, 'Minuten')
    nl_rij = N0 + len(NORMEN) + 1
    c = ws.cell(row=nl_rij, column=1, value=nl(NOTA_CODE))
    c.font = Font(bold=True, italic=True, color='555555')
    c.alignment = Alignment(wrap_text=True, vertical='top')
    samen(ws, nl_rij, 1, 13)
    ws.row_dimensions[nl_rij].height = 44
    starts, r = {}, nl_rij + 2
    breuken = []
    for art in CCP_ORDE:
        starts[art] = ccp_blok(ws, r, art, N_RIJEN, V)
        r += N_RIJEN + 3
        if art in ('koken', 'regen'):
            breuken.append(r - 1)
    fz = notities(ws, r, [
        '“In orde?” vergelijkt met de normen bovenaan (gele cellen). De duur houdt rekening met middernacht.',
        'Terugkoelen: noteer de starttijd zodra u begint met terugkoelen; de kerntemperatuur is dan ten minste de '
        'starttemperatuur uit de normen. “Let op” betekent: de richtwaarde na 2 uur is overschreden, de eindnorm is wel '
        'gehaald.',
        'Regenereren: noteer de tijd waarop u begint met opwarmen en de tijd waarop de kern de norm haalt.',
        'Warmhouden: meet elke week op de koudste plek en noteer de laagste temperatuur; vastleggen wordt aanbevolen '
        'en is verplicht bij een afwijking.',
        '“In orde?” blijft leeg zolang een nodig gegeven ontbreekt of als er tekst staat waar een getal hoort.',
        NOTA_BEWAAR, NOTA_HULP], 13, 18)
    artikel_link(ws, fz + 1, 13)
    pagina(ws, 'C3', BREEDTE_GRID, breuken=breuken)
    return starts


# ------------------------------------------------------------------ Blad 3: Ontvangst
def norm_ontvangst(z, refs, vorm=lambda r: r):
    """Norm van de gekozen soort in kolom D (getal, of met vorm=norm_tekst de tekst); onbekende soort → ""."""
    f = '""'
    for (soort, _), ref in reversed(list(zip(ONTVANGST, refs))):
        f = f'IF(D{z}="{soort}",{vorm(ref)},{f})'
    return f


def blad_ontvangst(wb):
    ws = wb.create_sheet('Ontvangst')
    bladkop(ws, 'HACCP-lijst ontvangst – alleen afwijkingen',
            'Meet bij ontvangst de temperatuur. Noteer hier alleen een levering die afwijkt, en wat u ermee hebt gedaan. '
            'Kies de soort in de keuzelijst; de norm en “Binnen de norm?” worden automatisch ingevuld.', 9)
    velden(ws, ['Bedrijf', 'Week/maand', 'Verantwoordelijke'], 1, 3)
    for (a, b), txt in (((1, 2), 'Soort'), ((3, 3), 'Norm (°C)'), ((4, 9), 'Bron')):
        cel(ws, O0, a, txt, vet=True, fond=grijs)
        rand_bereik(ws, O0, a, b, grijs)
        samen(ws, O0, a, b)
    for i, (soort, norm) in enumerate(ONTVANGST):
        r = O0 + 1 + i
        cel(ws, r, 1, soort, vet=True)
        rand_bereik(ws, r, 1, 2)
        samen(ws, r, 1, 2)
        cel(ws, r, 3, norm, '0', inv=True, vet=True, mid=True)
        cel(ws, r, 4, 'Hygiënecode voor de Horeca 2026', grootte=9)
        rand_bereik(ws, r, 4, 9)
        samen(ws, r, 4, 9)
        ws.row_dimensions[r].height = 18
    toets_geheel(ws, f'C{O0 + 1}:C{O0 + len(ONTVANGST)}', -40, 30, 'Norm')
    notities(ws, O0 + len(ONTVANGST) + 1, [NOTA_ONTVANGST], 9, 18)
    kopregel(ws, O_KOP, [(t, k, k) for k, t in enumerate(
        ['Datum', 'Leverancier', 'Product', 'Soort', 'Norm', 'Gemeten temperatuur (°C)', 'Binnen de norm?',
         'Afwijking en actie (bijv. geweigerd, teruggestuurd)', 'Paraaf'], start=1)], hoogte=36)
    e, l = O_KOP + 1, O_KOP + O_N
    refs = [f'$C${O0 + 1 + i}' for i in range(len(ONTVANGST))]
    for z in range(e, l + 1):
        cel(ws, z, 1, None, F_DATUM, inv=True, mid=True)
        cel(ws, z, 2, None, inv=True)
        cel(ws, z, 3, None, inv=True)
        cel(ws, z, 4, None, inv=True, mid=True)
        cel(ws, z, 5, '=' + norm_ontvangst(z, refs, norm_tekst), mid=True)
        cel(ws, z, 6, None, F_TEMP, inv=True, mid=True)
        norm = norm_ontvangst(z, refs)
        cel(ws, z, 7, f'=IF(OR(E{z}="",{geen_getal(f"F{z}", norm)}),"",IF(F{z}<={norm},"Ja","NEE"))', mid=True)
        cel(ws, z, 8, None, inv=True)
        cel(ws, z, 9, None, inv=True, mid=True)
        ws.row_dimensions[z].height = 22
    toets_datum(ws, f'A{e}:A{l}')
    _dv(ws, f'D{e}:D{l}', type='list', formula1='"' + ','.join(s for s, _ in ONTVANGST) + '"', errorTitle='Soort',
        error='Kies ' + ', '.join(s for s, _ in ONTVANGST[:-1]) + f' of {ONTVANGST[-1][0]} uit de lijst.')
    toets_temp(ws, f'F{e}:F{l}', -40, 30)
    cf_rood(ws, f'F{e}:F{l}', f'AND(ISNUMBER(F{e}),E{e}<>"",F{e}>{norm_ontvangst(e, refs)})')
    cf_nee(ws, f'G{e}:G{l}')
    fz = notities(ws, l + 2, [NOTA_BEWAAR, NOTA_HULP], 9, 18)
    artikel_link(ws, fz + 1, 9)
    pagina(ws, f'A{e}', {'A': 18, 'B': 22, 'C': 24, 'D': 16, 'E': 16, 'F': 13, 'G': 11, 'H': 46, 'I': 9})
    return e


# ------------------------------------------------------------------ Blad 4: Thermometer
def blad_thermometer(wb):
    ws = wb.create_sheet('Thermometer')
    bladkop(ws, 'Controle van de thermometers',
            'Controleer elke thermometer minimaal één keer per jaar, bijvoorbeeld in smeltend ijs (0 °C). Vul de gele '
            'cellen in; de afwijking en “In orde?” worden automatisch berekend.', 8)
    velden(ws, ['Bedrijf', 'Jaar', 'Verantwoordelijke'], 1, 3)
    cel(ws, TH_NORM, 1, 'Afwijking ten hoogste (+ of −)', vet=True, fond=grijs)
    rand_bereik(ws, TH_NORM, 1, 2, grijs)
    samen(ws, TH_NORM, 1, 2)
    cel(ws, TH_NORM, 3, 1.0, f'"±{NB}"0.0"{NB}°C"', inv=True, vet=True, mid=True)
    cel(ws, TH_NORM, 4, 'Hygiënecode voor de Horeca 2026: minimaal één keer per jaar controleren', grootte=9)
    rand_bereik(ws, TH_NORM, 4, 8)
    samen(ws, TH_NORM, 4, 8)
    ws.row_dimensions[TH_NORM].height = 18
    _dv(ws, f'C{TH_NORM}', type='decimal', operator='between', formula1='0.1', formula2='5', errorTitle='Afwijking',
        error='Vul een afwijking (°C) in tussen 0,1 en 5.')
    kopregel(ws, TH_KOP, [(t, k, k) for k, t in enumerate(
        ['Datum', 'Thermometer (naam of nummer)', 'Referentie (°C)', 'Gemeten (°C)', 'Afwijking (°C)', 'In orde?',
         'Correctieve maatregel (bij afwijking)', 'Paraaf'], start=1)], hoogte=36)
    e, l = TH_KOP + 1, TH_KOP + TH_N
    n = f'$C${TH_NORM}'
    for z in range(e, l + 1):
        cel(ws, z, 1, None, F_DATUM, inv=True, mid=True)
        cel(ws, z, 2, None, inv=True)
        cel(ws, z, 3, 0, F_TEMP, inv=True, mid=True)  # smeltend ijs; andere referentie: overschrijven
        cel(ws, z, 4, None, F_TEMP, inv=True, mid=True)
        cel(ws, z, 5, f'=IF({geen_getal(f"C{z}", f"D{z}")},"",ROUND(D{z}-C{z},1))', F_AFW, mid=True)
        cel(ws, z, 6, f'=IF({geen_getal(f"E{z}", n)},"",IF(ABS(E{z})<={n},"Ja","NEE"))', mid=True)
        cel(ws, z, 7, None, inv=True)
        cel(ws, z, 8, None, inv=True, mid=True)
        ws.row_dimensions[z].height = 22
    toets_datum(ws, f'A{e}:A{l}')
    toets_temp(ws, f'C{e}:D{l}', -30, 110)
    cf_rood(ws, f'D{e}:E{l}', f'AND(ISNUMBER($C{e}),ISNUMBER($D{e}),ABS(ROUND($D{e}-$C{e},1))>{n})')
    cf_nee(ws, f'F{e}:F{l}')
    fz = notities(ws, l + 2, [
        'Smeltend ijs: een bak met ijsblokjes en een beetje koud water; de referentie is dan 0 °C. Gebruikt u een andere '
        'referentie, vul die dan in de kolom Referentie in.',
        'Is de afwijking groter dan de norm, laat de thermometer dan kalibreren of vervang hem, en noteer dat als '
        'correctieve maatregel.',
        NOTA_BEWAAR, NOTA_HULP], 8, 18)
    artikel_link(ws, fz + 1, 8)
    pagina(ws, f'A{e}', {'A': 18, 'B': 28, 'C': 14, 'D': 13, 'E': 13, 'F': 10, 'G': 46, 'H': 9})
    return e


# ------------------------------------------------------------------ Blad 5: Voorbeeld
def blad_voorbeeld(wb):
    ws = wb.create_sheet('Voorbeeld')
    bladkop(ws, 'Voorbeeld – één ingevulde week (fictief)',
            'Zo kan een ingevulde week eruitzien, met één afwijking en de correctieve maatregel (woensdag, '
            'koelwerkbank). Gebruik voor uw eigen registratie de andere tabbladen.', 13)
    velden(ws, ['Bedrijf', 'Week/maand', 'Verantwoordelijke'], 1, 4, VB_VELDEN)
    apparaten_tabel(ws)
    e = week_blok(ws, W0, VB_WEEK, VB_KOEL)
    r, starts = W0 + BLOK, {}
    for art in CCP_ORDE:
        starts[art] = ccp_blok(ws, r, art, 1, V_LIT, VB_CCP[art])
        r += 4
    fz = notities(ws, r, ['Fictief voorbeeld ter illustratie: bedrijf, namen en metingen zijn verzonnen.', NOTA_HULP],
                  13, 18)
    artikel_link(ws, fz + 1, 13)
    pagina(ws, None, BREEDTE_GRID, breuken=(W0 + BLOK - 1,))
    return e, starts


# ------------------------------------------------------------------ PDF om af te drukken
def pdf_druk():
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase.pdfmetrics import stringWidth
    from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    def t(s):
        """PDF-tekst: Nederlandse typografie + WinAnsi van Helvetica (ë, é, “ ”, –, °). Het minteken U+2212 ontbreekt
        in WinAnsi: het kastlijntje «–» (0x96) vervangt het. ≤ en ≥ ontbreken ook: in de PDF staan ze in woorden."""
        s = nl(s).replace('−', '–')
        s.encode('cp1252')  # UnicodeEncodeError als een teken niet afdrukbaar is (≤, ≥ …)
        return s

    lijn, zw, goud = colors.HexColor('#999999'), colors.HexColor('#111111'), colors.HexColor('#FFD700')
    s_h = ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=10.5, leading=12.5, spaceBefore=5, spaceAfter=1,
                         textColor=zw)
    s_txt = ParagraphStyle('t', fontName='Helvetica', fontSize=8, leading=10)
    s_note = ParagraphStyle('n', fontName='Helvetica-Oblique', fontSize=7.3, leading=9,
                            textColor=colors.HexColor('#333333'))
    s_th = ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=7, leading=8, alignment=1, textColor=colors.white)
    s_lab = ParagraphStyle('lab', fontName='Helvetica', fontSize=6.5, leading=7.5, textColor=colors.HexColor('#777777'))
    s_norm = ParagraphStyle('norm', fontName='Helvetica-Bold', fontSize=7, leading=8, alignment=1)
    W = A4[0] - 28 * mm

    def band(tekst, grootte=13):
        assert stringWidth(t(tekst), 'Helvetica-Bold', grootte) < W - 12, tekst  # één regel, binnen de balk
        b = Table([[t(tekst)]], colWidths=[W])
        b.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), zw), ('TEXTCOLOR', (0, 0), (-1, -1), goud),
                               ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), grootte),
                               ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 7)]))
        return b

    def voet(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica-Oblique', 7.5)
        canvas.setFillColor(colors.HexColor('#555555'))
        canvas.drawCentredString(A4[0] / 2, 7 * mm, t(VOET))
        canvas.restoreState()

    def info():
        tb = Table([['Bedrijf:', '', 'Verantwoordelijke:', '']], colWidths=[W * 0.1, W * 0.42, W * 0.18, W * 0.3],
                   rowHeights=17)
        tb.setStyle(TableStyle([('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 8.5),
                                ('LINEBELOW', (1, 0), (1, 0), 0.5, lijn), ('LINEBELOW', (3, 0), (3, 0), 0.5, lijn),
                                ('VALIGN', (0, 0), (-1, -1), 'BOTTOM')]))
        return tb

    def raster(koppen, anteile, n, hoogte=22, kop_h=26):
        assert abs(sum(anteile) - 1) < 1e-9, sum(anteile)
        tb = Table([[Paragraph(t(x), s_th) for x in koppen]] + [[''] * len(koppen) for _ in range(n)],
                   colWidths=[W * x for x in anteile], rowHeights=[kop_h] + [hoogte] * n)
        tb.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, lijn), ('BACKGROUND', (0, 0), (-1, 0), zw),
                                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, 0), 2),
                                ('RIGHTPADDING', (0, 0), (-1, 0), 2), ('TOPPADDING', (0, 0), (-1, 0), 2),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 2)]))
        return tb

    doc = SimpleDocTemplate(str(PDF), pagesize=A4, leftMargin=14 * mm, rightMargin=14 * mm, topMargin=11 * mm,
                            bottomMargin=14 * mm, title=t('HACCP-lijsten horeca: koelingen, kritische punten, ontvangst '
                                                          'en thermometer'),
                            author='AI Chef Pro',
                            subject=t('Koelingen, vriezers, koken, terugkoelen, regenereren, warmhouden, ontvangst en '
                                      'controle van de thermometers'))
    # Pagina 1 — koelingen en vriezers, twee weken
    el = [band('HACCP-lijst koelingen en vriezers'), Spacer(1, 4), info(), Spacer(1, 4),
          Paragraph(t('Lees elke dag het display af en noteer de temperatuur. Meet één keer per week met een '
                      'gekalibreerde thermometer. Bij een afwijking: correctieve maatregel en paraaf.'), s_txt)]
    koppen = ['Apparaat', 'Norm'] + DAGEN + ['Wekelijks meten (°C)', 'Afwijking? Correctieve maatregel', 'Paraaf']
    anteile = [0.15, 0.10] + [0.055] * 7 + [0.09, 0.215, 0.06]
    assert abs(sum(anteile) - 1) < 1e-9
    soorten = [('Koeling', 'max. 7 °C')] * 4 + [('Vriezer', '−18 °C of kouder')] * 2
    for _ in range(2):
        el += [Paragraph(t('Week: ……………    Van ……………… tot en met ………………'), s_h)]
        rijen = [[Paragraph(t(x), s_th) for x in koppen]]
        rijen += [[Paragraph(t(s + ':'), s_lab), Paragraph(t(n), s_norm)] + [''] * 10 for s, n in soorten]
        tb = Table(rijen, colWidths=[W * x for x in anteile], rowHeights=[26] + [34] * len(soorten))
        tb.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, lijn), ('BACKGROUND', (0, 0), (-1, 0), zw),
                                ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'), ('VALIGN', (0, 1), (0, -1), 'TOP'),
                                ('VALIGN', (1, 1), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, 0), 2),
                                ('RIGHTPADDING', (0, 0), (-1, 0), 2),
                                ('BACKGROUND', (1, 1), (1, -1), colors.HexColor('#F3F3F3')),
                                ('LINEAFTER', (1, 0), (1, -1), 1.2, zw), ('LINEAFTER', (8, 0), (8, -1), 1.2, zw),
                                ('LINEABOVE', (0, 5), (-1, 5), 1.2, zw)]))
        el += [tb]
    el += [Spacer(1, 6),
           Paragraph(t('Wettelijke grenzen: gekoeld ten hoogste 7 °C (art. 15 Warenwetbesluit Bereiding en behandeling '
                       'van levensmiddelen; voorverpakt: de temperatuur van de fabrikant), diepgevroren ten hoogste '
                       '−18 °C (Warenwetregeling Diepgevroren levensmiddelen).'), s_note), Spacer(1, 2),
           Paragraph(t('De wet schrijft geen dagelijkse lijst voor. In de Hygiënecode voor de Horeca 2026 is meten van '
                       'koelingen verplicht en registreren verplicht bij een afwijking.'), s_note), Spacer(1, 2),
           Paragraph(t(NOTA_BEWAAR + ' De Hygiënecode voor de Horeca 2016 mag u gebruiken tot en met 31 maart 2027. '
                       + NOTA_HULP), s_note), PageBreak()]

    # Pagina 2 — kritische punten
    el += [band('HACCP-lijst kritische punten (koken, terugkoelen, regenereren) en warmhouden', 12), Spacer(1, 4),
           info(), Spacer(1, 2),
           Paragraph(t('<b>Week: ……………</b>    Meet en registreer de kritische punten één keer per week. ' + NOTA_WARM),
                     s_txt)]
    a7 = [0.09, 0.25, 0.07, 0.10, 0.08, 0.34, 0.07]
    el += [Paragraph(t('Koken'), s_h), Paragraph(t('Kerntemperatuur ten minste 75 °C.'), s_txt), Spacer(1, 2),
           raster(['Datum', 'Product', 'Tijd', 'Kerntemp. (°C)', 'In orde? (ja/nee)', 'Correctieve maatregel',
                   'Paraaf'], a7, 4),
           Paragraph(t('Terugkoelen'), s_h),
           Paragraph(t('Van ten minste 75 °C naar ten hoogste 7 °C binnen 5 uur; richtwaarde na 2 uur: ten hoogste '
                       '20 °C.'), s_txt), Spacer(1, 2),
           raster(['Datum', 'Product', 'Tijd start', '°C start', 'Tijd na 2 uur', '°C na 2 uur', 'Tijd eind',
                   '°C eind', 'In orde? (ja/nee)', 'Correctieve maatregel', 'Paraaf'],
                  [0.08, 0.17, 0.065, 0.065, 0.065, 0.065, 0.065, 0.065, 0.07, 0.22, 0.07], 4),
           Paragraph(t('Regenereren'), s_h),
           Paragraph(t('Binnen 60 minuten tot een kerntemperatuur van ten minste 60 °C.'), s_txt), Spacer(1, 2),
           raster(['Datum', 'Product', 'Tijd start', 'Tijd norm bereikt', 'Minuten', 'Kerntemp. (°C)',
                   'In orde? (ja/nee)', 'Correctieve maatregel', 'Paraaf'],
                  [0.08, 0.20, 0.07, 0.08, 0.07, 0.08, 0.07, 0.28, 0.07], 4),
           Paragraph(t('Warmhouden'), s_h),
           Paragraph(t('Ten minste 60 °C. Meet elke week op de koudste plek en noteer de laagste temperatuur; '
                       'vastleggen wordt aanbevolen en is verplicht bij een afwijking.'), s_txt),
           Spacer(1, 2),
           raster(['Datum', 'Product', 'Tijd', 'Laagste temp. (°C)', 'In orde? (ja/nee)', 'Correctieve maatregel',
                   'Paraaf'], a7, 4),
           Spacer(1, 6),
           Paragraph(t('Koken ten minste 75 °C, terugkoelen van ten minste 75 °C naar ten hoogste 7 °C binnen 5 uur en '
                       'regenereren binnen 60 minuten tot ten minste 60 °C zijn normen uit de nieuwe Hygiënecode Horeca '
                       '(2026), zoals op de formulieren van KHN, geen wetsartikelen; 20 °C na 2 uur is een richtwaarde. '
                       'De NVWA adviseert kip en gehakt tot ten minste 75 °C te verhitten, binnen 5 uur af te koelen tot '
                       'onder 7 °C en op te warmen tot ten minste 60 °C. Warmhouden ten minste 60 °C staat in de wet '
                       '(art. 15 lid 2 Warenwetbesluit Bereiding en behandeling van levensmiddelen).'),
                     s_note), Spacer(1, 2),
           Paragraph(t(NOTA_BEWAAR + ' ' + NOTA_HULP), s_note), PageBreak()]

    def normtabel(rijen, anteile):
        tb = Table([[Paragraph(t(x), s_th) for x in ('Soort', 'Norm', 'Bron')]]
                   + [[Paragraph(t(a), s_txt), Paragraph(t(b), s_norm), Paragraph(t(c), s_lab)] for a, b, c in rijen],
                   colWidths=[W * x for x in anteile])
        tb.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, lijn), ('BACKGROUND', (0, 0), (-1, 0), zw),
                                ('BACKGROUND', (1, 1), (1, -1), colors.HexColor('#F3F3F3')),
                                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        return tb

    # Pagina 3 — ontvangst, alleen afwijkingen (zoals het tabblad «Ontvangst»)
    bron_o = 'Hygiënecode voor de Horeca 2026'
    el += [band('HACCP-lijst ontvangst – alleen afwijkingen'), Spacer(1, 4), info(), Spacer(1, 4),
           Paragraph(t('Meet bij ontvangst de temperatuur. Noteer hier alleen een levering die afwijkt, en wat u ermee '
                       'hebt gedaan.'), s_txt), Spacer(1, 4),
           normtabel([(soort, f'–{abs(n)} °C of kouder' if n < 0 else f'max. {n} °C', bron_o) for soort, n in ONTVANGST],
                     [0.3, 0.2, 0.5]), Spacer(1, 3),
           Paragraph(t(NOTA_ONTVANGST), s_note), Spacer(1, 4),
           raster(['Datum', 'Leverancier', 'Product', 'Soort', 'Norm', 'Gemeten (°C)', 'Binnen de norm? (ja/nee)',
                   'Afwijking en actie (bijv. geweigerd, teruggestuurd)', 'Paraaf'],
                  [0.08, 0.14, 0.15, 0.10, 0.08, 0.08, 0.08, 0.23, 0.06], 18, hoogte=25, kop_h=30),
           Spacer(1, 6), Paragraph(t(NOTA_BEWAAR + ' ' + NOTA_HULP), s_note), PageBreak()]

    # Pagina 4 — controle van de thermometers, jaarlijks (zoals het tabblad «Thermometer»)
    el += [band('Controle van de thermometers – jaarlijks'), Spacer(1, 4), info(), Spacer(1, 4),
           Paragraph(t('<b>Jaar: ……………</b>    Controleer elke thermometer minimaal één keer per jaar, bijvoorbeeld in '
                       'smeltend ijs (0 °C).'), s_txt), Spacer(1, 4),
           normtabel([('Afwijking ten hoogste (+ of –)', '± 1,0 °C', 'Hygiënecode voor de Horeca 2026: minimaal één '
                       'keer per jaar controleren')], [0.3, 0.2, 0.5]), Spacer(1, 6),
           raster(['Datum', 'Thermometer (naam of nummer)', 'Referentie (°C)', 'Gemeten (°C)', 'Afwijking (°C)',
                   'In orde? (ja/nee)', 'Correctieve maatregel (bij afwijking)', 'Paraaf'],
                  [0.09, 0.20, 0.09, 0.09, 0.09, 0.08, 0.30, 0.06], TH_N, hoogte=28, kop_h=30),
           Spacer(1, 6),
           Paragraph(t('Smeltend ijs: een bak met ijsblokjes en een beetje koud water; de referentie is dan 0 °C. Gebruikt '
                       'u een andere referentie, vul die dan in de kolom Referentie in.'), s_note), Spacer(1, 2),
           Paragraph(t('Is de afwijking groter dan de norm, laat de thermometer dan kalibreren of vervang hem, en noteer '
                       'dat als correctieve maatregel.'), s_note), Spacer(1, 2),
           Paragraph(t(NOTA_BEWAAR + ' ' + NOTA_HULP), s_note)]
    doc.build(el, onFirstPage=voet, onLaterPages=voet)


# ------------------------------------------------------------------ Gates
def cache_tekst_leeg(pad):
    """inject_cache.py injecteert het resultaat «""» niet: de cel houdt een lege cache (<v></v>, gelezen als 0) en
    viewers zonder herberekening (macOS-voorvertoning, telefoon) tonen «0». Hier wordt de cache «lege tekst» zoals in
    Excel geschreven (t="str" + <v></v>), zonder de rest van de zip aan te raken (zelfde als het Duitse gemelo)."""
    patroon = re.compile(r'<c r="([A-Z]+[0-9]+)"((?:(?!\st=)[^>])*)>(<f>[^<]*</f>)(?:<v>\s*</v>|<v\s*/>)?</c>')
    with zipfile.ZipFile(pad) as z:
        delen = [(i, z.read(i.filename)) for i in z.infolist()]
    n = 0
    with zipfile.ZipFile(str(pad) + '.tmp', 'w', zipfile.ZIP_DEFLATED) as zout:
        for info, data in delen:
            if re.match(r'xl/worksheets/sheet[0-9]+\.xml$', info.filename):
                xml, k = patroon.subn(r'<c r="\1"\2 t="str">\3<v></v></c>', data.decode('utf-8'))
                data, n = xml.encode('utf-8'), n + k
            zout.writestr(info, data)
    shutil.move(str(pad) + '.tmp', str(pad))
    return n


def injecteren(pad):
    uit = subprocess.run([sys.executable, str(INJECT), str(pad)], check=True, capture_output=True, text=True).stdout
    assert 'fallos_pycel=0' in uit, uit
    m = re.search(r'formulas=(\d+) cache_inyectado=(\d+)', uit)
    leeg = cache_tekst_leeg(pad)
    assert int(m.group(1)) == int(m.group(2)) + leeg, (uit, leeg)  # elke formule heeft een cache (waarde of lege tekst)
    return f'{uit.strip()} cache_tekst_leeg={leeg}'


K, KP, O, T, VB = 'Koelingen en vriezers', 'Kritische punten', 'Ontvangst', 'Thermometer', 'Voorbeeld'


def gevallen_toetsen(gevallen, normen=None, extra=()):
    """Testwaarden in een TIJDELIJKE kopie (het gepubliceerde bestand blijft leeg); normen = {(blad, cel): waarde}."""
    with tempfile.TemporaryDirectory() as tmp:
        kopie = Path(tmp) / 'test.xlsx'
        shutil.copy(XLSX, kopie)
        wb = load_workbook(kopie)
        for (blad, ref), w in (normen or {}).items():
            wb[blad][ref] = w
        for blad, z, waarden, _, _, _ in gevallen:
            for k, w in waarden.items():
                wb[blad].cell(row=z, column=k).value = w  # cell(..., value=None) zou de cel NIET leegmaken
        wb.save(kopie)
        injecteren(kopie)
        wv = load_workbook(kopie, data_only=True)
        res = []
        for blad, z, _, k_ok, verw, omschr in gevallen:
            w = wv[blad].cell(row=z, column=k_ok).value
            res.append((blad, omschr, verw, None if w == '' else w))
        ex = {(blad, z, k): wv[blad].cell(row=z, column=k).value for blad, z, k in extra}
    return res, ex


def minuten(d):
    return d.total_seconds() / 60 if hasattr(d, 'total_seconds') else d * 1440  # openpyxl leest [h]:mm als timedelta


def gate_logica(wk, st, o1, t1, vb):
    p = wk[0]
    kk, tk, rk, hk = st['koken'], st['terug'], st['regen'], st['warm']
    gevallen = [  # (blad, rij, {kolom: waarde}, kolom «In orde?», verwacht, omschrijving)
        (K, p + 0, {3: 3.5}, 11, 'Ja', 'Koelcel ma 3,5 °C (norm 7)'),
        (K, p + 1, {3: 4.0, 4: 7.0, 5: 5.0}, 11, 'Ja', 'Koelkast di 7,0 °C precies op de norm'),
        (K, p + 2, {3: 4.0, 5: 7.1}, 11, 'NEE', 'Koelwerkbank wo 7,1 °C'),
        (K, p + 3, {10: 7.5}, 11, 'NEE', 'alleen de wekelijkse meting 7,5 °C'),
        (K, p + 4, {3: -19.0, 4: -18.0}, 11, 'Ja', 'Vriezer −19 en −18 °C (norm −18)'),
        (K, p + 5, {3: -20.0, 9: -17.5}, 11, 'NEE', 'Vriescel zo −17,5 °C'),
        (K, wk[1], {3: 2.0}, 11, 'Ja', 'week 2 volgt apparaat 1'),
        (K, wk[1] + 4, {3: -16.0}, 11, 'NEE', 'week 2: vriezer −16 °C'),
        (K, wk[2], {12: 'alleen tekst', 13: 'SdV'}, 11, None, 'alleen maatregel en paraaf → leeg'),
        (K, wk[4] + 5, {}, 11, None, 'lege rij (week 5) → leeg'),
        (KP, kk + 0, {4: 75.0}, 5, 'Ja', 'koken precies 75 °C'),
        (KP, kk + 1, {4: 82.0}, 5, 'Ja', 'koken 82 °C'),
        (KP, kk + 2, {4: 74.9}, 5, 'NEE', 'koken 74,9 °C'),
        (KP, kk + 3, {1: 'Kip', 3: hm(12, 0)}, 5, None, 'koken zonder temperatuur → leeg'),
        (KP, kk + 4, {4: 'tachtig'}, 5, None, 'koken: tekst als kerntemperatuur → leeg (was «Ja»)'),
        (KP, tk + 0, {3: hm(14, 0), 4: 85.0, 5: hm(16, 0), 6: 18.0, 7: hm(18, 30), 8: 6.0}, 11, 'Ja',
         'terugkoelen 4 u 30, 18 °C na 2 uur, eind 6 °C'),
        (KP, tk + 1, {3: hm(14, 0), 4: 80.0, 7: hm(19, 0), 8: 7.0}, 11, 'Ja',
         'terugkoelen precies 5 uur en 7 °C, zonder 2-uursmeting'),
        (KP, tk + 2, {3: hm(14, 0), 4: 80.0, 7: hm(19, 5), 8: 6.0}, 11, 'NEE', 'terugkoelen 5 u 05'),
        (KP, tk + 3, {3: hm(14, 0), 4: 80.0, 7: hm(18, 0), 8: 8.0}, 11, 'NEE', 'terugkoelen eind 8 °C'),
        (KP, tk + 4, {3: hm(14, 0), 4: 70.0, 7: hm(18, 0), 8: 5.0}, 11, 'NEE', 'terugkoelen start 70 °C'),
        (KP, tk + 5, {3: hm(14, 0), 4: 85.0, 5: hm(16, 0), 6: 24.0, 7: hm(18, 45), 8: 6.0}, 11, 'Let op',
         'terugkoelen: na 2 uur 24 °C, eindnorm gehaald'),
        (KP, tk + 6, {3: hm(22, 0), 4: 80.0, 7: hm(2, 30), 8: 6.0}, 11, 'Ja', 'terugkoelen 22:00 → 02:30 (middernacht)'),
        (KP, tk + 7, {3: hm(14, 0), 4: 85.0, 5: hm(16, 0), 6: 18.0}, 11, None, 'terugkoelen nog zonder eind → leeg'),
        (KP, rk + 0, {3: hm(17, 30), 4: hm(17, 55), 5: 72.0}, 7, 'Ja', 'regenereren 25 min, 72 °C'),
        (KP, rk + 1, {3: hm(17, 30), 4: hm(18, 30), 5: 60.0}, 7, 'Ja', 'regenereren precies 60 min en 60 °C'),
        (KP, rk + 2, {3: hm(17, 30), 4: hm(18, 31), 5: 65.0}, 7, 'NEE', 'regenereren 61 min'),
        (KP, rk + 3, {3: hm(17, 30), 4: hm(17, 50), 5: 58.0}, 7, 'NEE', 'regenereren kern 58 °C'),
        (KP, rk + 4, {3: hm(23, 40), 4: hm(0, 20), 5: 70.0}, 7, 'Ja', 'regenereren 23:40 → 00:20 (middernacht)'),
        (KP, rk + 5, {3: hm(18, 0), 4: hm(17, 55), 5: 70.0}, 7, 'NEE', 'regenereren: tijden verwisseld (1435 min)'),
        (KP, rk + 6, {3: hm(17, 30), 5: 70.0}, 7, None, 'regenereren zonder eindtijd → leeg'),
        (KP, hk + 0, {4: 65.0}, 5, 'Ja', 'warmhouden 65 °C'),
        (KP, hk + 1, {4: 60.0}, 5, 'Ja', 'warmhouden precies 60 °C'),
        (KP, hk + 2, {4: 59.5}, 5, 'NEE', 'warmhouden 59,5 °C'),
        (KP, hk + 3, {}, 5, None, 'warmhouden lege rij → leeg'),
        (KP, hk + 4, {4: 'warm'}, 5, None, 'warmhouden: tekst als temperatuur → leeg (was «Ja»)'),
        (O, o1 + 0, {4: 'Gekoeld', 6: 7.0}, 7, 'Ja', 'ontvangst gekoeld 7,0 °C'),
        (O, o1 + 1, {4: 'Gekoeld', 6: 7.5}, 7, 'NEE', 'ontvangst gekoeld 7,5 °C'),
        (O, o1 + 2, {4: 'Rauw gevogelte', 6: 4.0}, 7, 'Ja', 'ontvangst rauw gevogelte 4,0 °C'),
        (O, o1 + 3, {4: 'Rauw gevogelte', 6: 4.5}, 7, 'NEE', 'ontvangst rauw gevogelte 4,5 °C'),
        (O, o1 + 4, {4: 'Diepvries', 6: -15.0}, 7, 'Ja', 'ontvangst diepvries −15 °C'),
        (O, o1 + 5, {4: 'Diepvries', 6: -14.0}, 7, 'NEE', 'ontvangst diepvries −14 °C'),
        (O, o1 + 6, {6: 5.0}, 7, None, 'ontvangst temperatuur zonder soort → leeg'),
        (O, o1 + 7, {4: 'Gekoeld'}, 7, None, 'ontvangst soort zonder temperatuur → leeg'),
        (T, t1 + 0, {4: 0.8}, 6, 'Ja', 'thermometer +0,8 °C'),
        (T, t1 + 1, {4: 1.0}, 6, 'Ja', 'thermometer +1,0 °C (grens inclusief)'),
        (T, t1 + 2, {4: -1.0}, 6, 'Ja', 'thermometer −1,0 °C (grens inclusief)'),
        (T, t1 + 3, {4: 1.1}, 6, 'NEE', 'thermometer +1,1 °C'),
        (T, t1 + 4, {4: -1.2}, 6, 'NEE', 'thermometer −1,2 °C'),
        (T, t1 + 5, {}, 6, None, 'thermometer lege rij → leeg'),
        (T, t1 + 6, {3: None, 4: 0.5}, 6, None, 'thermometer zonder referentie → leeg'),
    ]
    extra = [(KP, tk, 9), (KP, rk, 6), (KP, rk + 4, 6), (KP, rk + 5, 6), (KP, tk + 6, 9), (T, t1 + 3, 5),
             (O, o1 + 4, 5), (O, o1 + 2, 5), (K, wk[1], 1), (K, wk[1], 2)]
    res, ex = gevallen_toetsen(gevallen, extra=extra)
    assert abs(minuten(ex[(KP, tk, 9)]) - 270) < 1e-6, ex[(KP, tk, 9)]
    assert abs(minuten(ex[(KP, tk + 6, 9)]) - 270) < 1e-6, ex[(KP, tk + 6, 9)]
    assert [ex[(KP, rk, 6)], ex[(KP, rk + 4, 6)], ex[(KP, rk + 5, 6)]] == [25, 40, 1435], ex
    assert abs(ex[(T, t1 + 3, 5)] - 1.1) < 1e-9, ex[(T, t1 + 3, 5)]
    assert ex[(O, o1 + 4, 5)] == f'−15{NB}°C of kouder' and ex[(O, o1 + 2, 5)] == f'max. 4{NB}°C', ex
    assert ex[(K, wk[1], 1)] == 'Koelcel' and ex[(K, wk[1], 2)] == f'max. 7{NB}°C', ex
    # Normen zijn aan te passen: koelcel naar 5 °C, koken naar 80 °C, gevogelte naar 3 °C → dezelfde formules volgen.
    gevallen2 = [(K, p, {3: 6.0}, 11, 'NEE', 'norm koelcel 5 °C: 6,0 °C'),
                 (K, wk[3], {3: 5.0}, 11, 'Ja', 'norm koelcel 5 °C: week 4, 5,0 °C'),
                 (KP, kk, {4: 78.0}, 5, 'NEE', 'norm koken 80 °C: 78 °C'),
                 (KP, tk, {3: hm(14, 0), 4: 85.0, 5: hm(16, 0), 6: 25.0, 7: hm(20, 0), 8: 9.0}, 11, 'NEE',
                  'terugkoelen: 2 uur te warm én eind 9 °C → NEE, niet Let op'),
                 (O, o1, {4: 'Rauw gevogelte', 6: 3.5}, 7, 'NEE', 'norm gevogelte 3 °C: 3,5 °C')]
    res2, _ = gevallen_toetsen(gevallen2, {(K, f'E{T0 + 1}'): 5, (KP, V['koken_t'].replace('$', '')): 80,
                                           (O, f'C{O0 + 2}'): 3})
    # Tekst in getalcellen (gegevens én normen) en ontbrekende verplichte gegevens → leeg, nooit «Ja»; ook «Voorbeeld».
    e_vb, vst = vb
    gevallen3 = [
        (K, p, {3: 3.0, 4: '9,0'}, 11, None, 'koelcel: «9,0» als tekst in een dagcel → leeg (was «Ja»)'),
        (K, p + 1, {3: 3.0}, 11, None, 'norm koelkast als tekst → leeg'),
        (KP, tk + 0, {3: hm(14, 0), 7: hm(18, 0), 8: 5.0}, 11, None,
         'terugkoelen zonder starttemperatuur → leeg (was «Ja»)'),
        (KP, tk + 1, {3: hm(14, 0), 4: 'heet', 7: hm(18, 0), 8: 5.0}, 11, None, 'terugkoelen: starttemp. als tekst → leeg'),
        (KP, tk + 2, {3: hm(14, 0), 4: 80.0, 5: hm(16, 0), 6: 'koud', 7: hm(18, 0), 8: 5.0}, 11, None,
         'terugkoelen: 2-uursmeting als tekst → leeg'),
        (KP, tk + 3, {3: '14.00', 4: 80.0, 7: hm(18, 0), 8: 5.0}, 11, None, 'terugkoelen: starttijd als tekst → leeg'),
        (KP, tk + 4, {3: hm(14, 0), 4: 80.0, 7: hm(18, 0), 8: 'zes'}, 11, None, 'terugkoelen: eindtemp. als tekst → leeg'),
        (KP, tk + 5, {3: hm(14, 0), 4: 80.0, 7: hm(18, 0)}, 11, None, 'terugkoelen zonder eindtemperatuur → leeg'),
        (KP, rk, {3: hm(17, 30), 4: hm(17, 55), 5: 'heet'}, 7, None, 'regenereren: kerntemp. als tekst → leeg (was «Ja»)'),
        (KP, rk + 1, {3: '17.30', 4: hm(17, 55), 5: 70.0}, 7, None, 'regenereren: starttijd als tekst → leeg'),
        (KP, hk, {4: 65.0}, 5, None, 'norm warmhouden als tekst → leeg'),
        (O, o1, {4: 'Gekoeld', 6: 'koud'}, 7, None, 'ontvangst: tekst als temperatuur → leeg'),
        (T, t1, {4: 'nul'}, 6, None, 'thermometer: tekst als meting → leeg'),
        (VB, e_vb + 1, {5: '4,0'}, 11, None, 'Voorbeeld koelkast: tekst in een dagcel → leeg'),
        (VB, vst['koken'], {4: 'tachtig'}, 5, None, 'Voorbeeld koken: tekst → leeg'),
        (VB, vst['terug'], {4: None}, 11, None, 'Voorbeeld terugkoelen zonder starttemperatuur → leeg'),
        (VB, vst['regen'], {5: 'heet'}, 7, None, 'Voorbeeld regenereren: tekst → leeg'),
        (VB, vst['warm'], {4: 'warm'}, 5, None, 'Voorbeeld warmhouden: tekst → leeg'),
        (VB, e_vb + 3, {}, 11, 'Ja', 'Voorbeeld barkoeling ongewijzigd → Ja'),
    ]
    extra3 = [(KP, tk + 3, 9), (KP, rk + 1, 6), (T, t1, 5)]
    res3, ex3 = gevallen_toetsen(gevallen3, {(K, f'E{T0 + 2}'): 'zeven', (KP, V['warm_t'].replace('$', '')): 'zestig'},
                                 extra=extra3)
    assert all(ex3[x] in (None, '') for x in extra3), ex3  # duur en afwijking met tekst: leeg, geen #WAARDE!
    for blad, omschr, verw, w in res + res2 + res3:
        print(f'  {"OK " if verw == w else "KO "} [{blad}] {omschr} → {w!r} (verwacht {verw!r})')
    assert all(verw == w for _, _, verw, w in res + res2 + res3), 'Gate logica KO'
    return len(res) + len(res2) + len(res3)


def gate_gepubliceerd(wk, st, o1, t1, vb):
    wv = load_workbook(XLSX, data_only=True)
    assert wv.sheetnames == [K, KP, O, T, VB], wv.sheetnames
    for blad in (K, VB):
        ws = wv[blad]
        assert [ws.cell(row=T0 + 1 + i, column=2).value for i in range(N_APP)] == [n for n, _ in APPARATEN]
        assert [ws.cell(row=T0 + 1 + i, column=5).value for i in range(N_APP)] == [w for _, w in APPARATEN]
        bron = [ws.cell(row=T0 + 1 + i, column=6).value.replace(NB, ' ') for i in range(N_APP)]
        assert bron == [WET_KOEL] * 4 + [WET_VRIES] * 2, bron
    ws = wv[K]
    for e in wk:
        assert ws.cell(row=e - 2, column=2).value is None
        for i in range(N_APP):
            assert ws.cell(row=e + i, column=1).value == APPARATEN[i][0], (e, i)
            n = APPARATEN[i][1]
            assert ws.cell(row=e + i, column=2).value.replace(NB, ' ') == (
                f'−{abs(n)} °C of kouder' if n < 0 else f'max. {n} °C'), (e, i)
            for k in list(range(3, 11)) + [12, 13]:
                assert ws.cell(row=e + i, column=k).value is None, (e + i, k)
            assert ws.cell(row=e + i, column=11).value in (None, ''), (e + i, 11)
    ks = wv[KP]
    assert [ks.cell(row=N0 + 1 + i, column=5).value for i in range(len(NORMEN))] == [75, 75, 20, 7, 5, 60, 60, 60]
    assert ks['A1'].value == 'HACCP-lijst kritische punten (koken, terugkoelen, regenereren) en warmhouden', ks['A1'].value
    assert NOTA_WARM in ks['A2'].value.replace(NB, ' '), ks['A2'].value
    bronnen = [ks.cell(row=N0 + 1 + i, column=8).value.replace(NB, ' ') for i in range(len(NORMEN))]
    assert bronnen == [BRON_KOKEN, BRON_CODE26, 'Hygiënecode voor de Horeca 2026 (richtwaarde)', BRON_CODE, BRON_CODE,
                       BRON_REGEN, BRON_CODE26, 'Wet: art. 15 lid 2 Warenwetbesluit Bereiding en behandeling van '
                       'levensmiddelen'], bronnen
    banden = [ks.cell(row=st[a] - 2, column=1).value.replace(NB, ' ') for a in CCP_ORDE]
    assert banden == ['Koken – kerntemperatuur ten minste 75 °C',
                      'Terugkoelen – van ten minste 75 °C naar ten hoogste 7 °C binnen 5 uur · richtwaarde na 2 uur: '
                      'ten hoogste 20 °C',
                      'Regenereren – binnen 60 minuten tot een kerntemperatuur van ten minste 60 °C',
                      'Warmhouden – ten minste 60 °C, gemeten op de koudste plek · elke week meten; vastleggen '
                      'aanbevolen, verplicht bij een afwijking'], banden
    for a in CCP_ORDE:
        for z in range(st[a], st[a] + N_RIJEN):
            for k in range(1, 14):
                assert ks.cell(row=z, column=k).value in (None, ''), (a, z, k)
    os_ = wv[O]
    assert [os_.cell(row=O0 + 1 + i, column=3).value for i in range(3)] == [7, 4, -15]
    for z in range(o1, o1 + O_N):
        assert all(os_.cell(row=z, column=k).value in (None, '') for k in range(1, 10)), z
    ts = wv[T]
    assert ts.cell(row=TH_NORM, column=3).value == 1
    for z in range(t1, t1 + TH_N):
        assert ts.cell(row=z, column=3).value == 0, z
        assert all(ts.cell(row=z, column=k).value in (None, '') for k in (1, 2, 4, 5, 6, 7, 8)), z
    # Voorbeeld: precies één afwijking, met maatregel; de rest «Ja»
    vs = wv[VB]
    e, vst = vb
    oks = [(vs.cell(row=e + i, column=1).value, vs.cell(row=e + i, column=11).value) for i in range(N_APP)]
    oks += [(a, vs.cell(row=vst[a], column=OK_KOL[a]).value) for a in CCP_ORDE]
    afwijkingen = []
    for i in range(N_APP):
        if vs.cell(row=e + i, column=11).value == 'NEE':
            assert vs.cell(row=e + i, column=12).value, 'afwijking zonder maatregel'
            dagen = [f"{DAGEN[k - 3].lower()} {vs.cell(row=e + i, column=k).value:.1f}".replace('.', ',') + ' °C' for k in range(3, 10)
                     if vs.cell(row=e + i, column=k).value > APPARATEN[i][1]]
            afwijkingen.append(f'{APPARATEN[i][0]} ' + ', '.join(dagen))
    assert [w for _, w in oks].count('NEE') == 1 and [w for _, w in oks].count('Ja') == len(oks) - 1, oks
    assert abs(minuten(vs.cell(row=vst['terug'], column=9).value) - 270) < 1e-6
    assert vs.cell(row=vst['regen'], column=6).value == 25
    assert vs.cell(row=W0, column=2).value == VB_WEEK
    # Teksten, bronnen, links, validaties, één geselecteerd tabblad
    wf = load_workbook(XLSX)
    alles = {b.title: ' '.join(str(c.value) for row in b.iter_rows() for c in row if c.value).replace(NB, ' ')
             for b in wf.worksheets}
    for n in (NOTA_WET, NOTA_REGISTRATIE, NOTA_BEWAAR, NOTA_2016, NOTA_HULP):
        assert n in alles[K], n
    assert NOTA_CODE in alles[KP] and NOTA_BEWAAR in alles[KP] and NOTA_HULP in alles[KP]
    assert NOTA_ONTVANGST in alles[O] and NOTA_HULP in alles[O] and NOTA_HULP in alles[T]
    assert not any(x in ' '.join(alles.values()) for x in VERBODEN), [x for x in VERBODEN if x in ' '.join(alles.values())]
    for b in wf.worksheets:
        assert any(c.hyperlink and c.hyperlink.target == ARTIKEL for row in b.iter_rows() for c in row), b.title
        assert b.data_validations.dataValidation, b.title
        assert all(d.showErrorMessage and d.error for d in b.data_validations.dataValidation), b.title
        assert str(b.page_setup.paperSize) == '9', b.title  # A4
    z = zipfile.ZipFile(XLSX)
    # Kleur van de 2-uursmeting (terugkoelen) volgt het resultaat: rood alleen bij «NEE», oranje anders (Let op)
    for blad, e in ((KP, st['terug']), (VB, vb[1]['terug'])):
        regels = {}
        for bereik in wf[blad].conditional_formatting:
            if str(bereik.sqref).split(':')[0] == f'F{e}':  # «F33» als het blok één rij heeft
                for regel in bereik.rules:
                    regels[regel.dxf.fill.fgColor.rgb[-6:]] = regel.formula[0]
        assert regels.get('F8CBAD', '').endswith(f'K{e}="NEE")') and regels.get('FFE699', '').endswith(
            f'K{e}<>"NEE")'), (blad, regels)
    gekozen = [n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml$', n)
               and 'tabSelected="1"' in z.read(n).decode('utf-8')]
    assert gekozen == ['xl/worksheets/sheet1.xml'], gekozen
    return afwijkingen


def gate_pdf():
    warnings.filterwarnings('ignore')
    from pypdf import PdfReader
    rd = PdfReader(str(PDF))
    n = len(rd.pages)
    assert n == 4, n
    for p in rd.pages:
        assert abs(float(p.mediabox.width) - 595.28) < 1 and abs(float(p.mediabox.height) - 841.89) < 1, p.mediabox
    teksten = [' '.join(p.extract_text().replace(NB, ' ').split()) for p in rd.pages]
    for verw in ('HACCP-lijst koelingen en vriezers', 'max. 7 °C', '–18 °C of kouder', 'Ma', 'Zo',
                 'gekalibreerde thermometer', 'art. 15 Warenwetbesluit Bereiding en behandeling', 'voorverpakt',
                 'Warenwetregeling Diepgevroren levensmiddelen', 'registreren verplicht bij een afwijking',
                 'minimaal zes maanden (advies KHN)', '31 maart 2027', 'geen officieel formulier van de NVWA of KHN',
                 'aichef.pro/nl/blog/hygienecode'):
        assert verw in teksten[0], ('pagina 1', verw)
    for verw in ('HACCP-lijst kritische punten (koken, terugkoelen, regenereren) en warmhouden', 'Koken', 'Terugkoelen',
                 'Regenereren', 'Warmhouden', 'ten minste 75 °C', 'binnen 5 uur', 'na 2 uur: ten hoogste 20 °C',
                 'Binnen 60 minuten', 'geen wetsartikelen', 'art. 15 lid 2', 'nieuwe Hygiënecode Horeca (2026)',
                 'formulieren van KHN', 'De NVWA adviseert kip en gehakt', 'Warmhouden: elke week meten',
                 'verplicht bij een afwijking', 'aichef.pro/nl/blog/hygienecode'):
        assert verw in teksten[1], ('pagina 2', verw)
    assert 'Hygiënecode voor de Horeca 2026 en advies van de NVWA' not in teksten[1]
    for verw in ('HACCP-lijst ontvangst – alleen afwijkingen', 'Gekoeld', 'max. 7 °C', 'Rauw gevogelte', 'max. 4 °C',
                 'Diepvries', '–15 °C of kouder', 'vastleggen hoeft alleen bij een afwijking', 'Leverancier',
                 'Binnen de norm?', 'geweigerd', 'geen officieel formulier van de NVWA of KHN',
                 'aichef.pro/nl/blog/hygienecode'):
        assert verw in teksten[2], ('pagina 3', verw)
    for verw in ('Controle van de thermometers – jaarlijks', 'minimaal één keer per jaar', 'smeltend ijs', '± 1,0 °C',
                 'Referentie (°C)', 'Afwijking (°C)', 'kalibreren', 'geen officieel formulier van de NVWA of KHN',
                 'aichef.pro/nl/blog/hygienecode'):
        assert verw in teksten[3], ('pagina 4', verw)
    lettergrootten = set()
    for pg in rd.pages:
        pg.extract_text(visitor_text=lambda tekst, cm, tm, fd, fs: lettergrootten.add(round(fs * tm[0], 2))
                        if tekst.strip() else None)
    assert min(lettergrootten) >= 6.5, sorted(lettergrootten)
    alles = ' '.join(teksten)
    assert not any(x in alles for x in VERBODEN), [x for x in VERBODEN if x in alles]
    return n


def main():
    wb = Workbook()
    wb.remove(wb.active)
    wk = blad_koelingen(wb)
    st = blad_kritisch(wb)
    o1 = blad_ontvangst(wb)
    t1 = blad_thermometer(wb)
    vb = blad_voorbeeld(wb)
    for i, ws in enumerate(wb.worksheets):
        ws.sheet_view.tabSelected = (i == 0)
    wb.active = 0
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.title = 'HACCP-lijsten horeca'
    XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb.save(XLSX)
    print(injecteren(XLSX))
    afw = gate_gepubliceerd(wk, st, o1, t1, vb)
    n = gate_logica(wk, st, o1, t1, vb)
    pdf_druk()
    paginas = gate_pdf()
    print(f'OK {XLSX.name} · 5 tabbladen · {N_WEKEN} weken × {N_APP} apparaten · kritische punten 4 × {N_RIJEN} · '
          f'ontvangst {O_N} · thermometer {TH_N} · Voorbeeld afwijkingen {afw} · gate logica {n}/{n} · '
          f'{PDF.name} ({paginas} pagina\'s)')


if __name__ == '__main__':
    main()
