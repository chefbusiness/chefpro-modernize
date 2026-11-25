#!/usr/bin/env python3
"""HACCP-Vorlagen (DE): Temperaturkontrolle und Reinigungsplan, GRATIS — lead magnet de /de/blog/haccp-konzept.

Gemelo alemán de plantilla-releve-temperatures-haccp-fr.py (mismo diseño, colores, inject_cache, caché «texto vacío»
y gate de lógica), ADAPTADO a Alemania. Solo valores dados y con su fuente; nada de DIN 10508 ni de la Leitlinie
del DEHOGA (de pago, no verificadas):
  - «Kühlung und Tiefkühlung»: 31 días × morgens/abends, 3 equipos editables, «In Ordnung?» automático. Límites por
    defecto editables: Kühlraum Fleischzubereitungen/Geflügel ≤ +4 °C y Kühlschrank Hackfleisch ≤ +2 °C
    (VO (EG) Nr. 853/2004), Tiefkühlung ≤ −18 °C (TLMV, kurzzeitig höchstens 3 °C Abweichung).
  - «Heißhalten und Abkühlen»: Heißhalten ≥ 60 °C an allen Stellen, ≤ 3 h; Abkühlen 60 °C → ≤ 7 °C en ≤ 120 min;
    Garen/Regenerieren 72 °C Kern ≥ 2 min. Recomendaciones del BfR (no límites legales) en celdas editables; duración
    con MOD(…;1) (cruce de medianoche) y «In Ordnung?» como en la hoja francesa.
  - «Reinigungsplan»: Bereich · Was · Wann · Womit · Wie · Wer · Erledigt, 15 filas de ejemplo editables + 10 vacías.
Keywords DE (nov-2026): «temperaturliste kühlschrank vorlage» 70, «reinigungsplan gastronomie vorlage» 70,
«haccp vorlage» 70.

Uso:  python3 scripts/contenidos/plantilla-haccp-vorlagen-de.py
Sale: astro-site/public/descargas/haccp-vorlagen-temperatur-reinigung-aichef.xlsx  (3 hojas, celdas de lectura vacías)
      astro-site/public/descargas/haccp-vorlagen-temperatur-reinigung-aichef.pdf   (A4, 2 páginas, a mano)
La lógica de «In Ordnung?» se prueba en COPIAS temporales (la salida publicada no lleva valores de prueba). Después:
  python3 scripts/productos-digitales/parche_xml_xlsx.py --check astro-site/public/descargas/haccp-vorlagen-temperatur-reinigung-aichef.xlsx
`/descargas/*` está en noindex (netlify.toml). Sesión Claude Code, 25-nov-2026.
"""
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

RAIZ = Path(__file__).resolve().parents[2]
XLSX = RAIZ / 'astro-site/public/descargas/haccp-vorlagen-temperatur-reinigung-aichef.xlsx'
PDF = RAIZ / 'astro-site/public/descargas/haccp-vorlagen-temperatur-reinigung-aichef.pdf'
INJECT = RAIZ / 'scripts/productos-digitales/inject_cache.py'
ARTIKEL = 'https://aichef.pro/de/blog/haccp-konzept'
FUSS = 'Kostenlose Vorlage von AI Chef Pro · Leitfaden: aichef.pro/de/blog/haccp-konzept'

SCHWARZ, GOLD, GRAU = '111111', 'FFD700', 'F3F3F3'
duenn = Side(style='thin', color='BBBBBB')
rahmen = Border(left=duenn, right=duenn, top=duenn, bottom=duenn)
rahmen_tag = Border(left=duenn, right=duenn, top=duenn, bottom=Side(style='thin', color='555555'))
eingabe = PatternFill('solid', fgColor='FFF8D6')
rot = PatternFill('solid', fgColor='F8CBAD')
grau = PatternFill('solid', fgColor=GRAU)
schwarz = PatternFill('solid', fgColor=SCHWARZ)
NB = ' '
F_TEMP = '+0.0;-0.0;0.0'
F_GRENZE = '+0.0;-0.0;0'
F_UHR = 'hh:mm'
F_DAUER = '[h]" h "mm" min"'
F_MIN = '[m]" min"'
F_DATUM = 'dd.mm.yyyy'

# (Bezeichnung, Höchstwert °C, Vorgabe und Quelle) — nur belegte Werte, sonst nichts
GERAETE = [
    ('Kühlraum – Fleischzubereitungen und Geflügel', 4,
     'Höchstwert +4 °C aus VO (EG) Nr. 853/2004 (für Ware, die den Betrieb verlässt)'),
    ('Kühlschrank – Hackfleisch', 2, 'Höchstwert +2 °C aus VO (EG) Nr. 853/2004 (für Ware, die den Betrieb verlässt)'),
    ('Tiefkühlung', -18, 'TLMV: −18 °C oder kälter; Abweichung nach oben höchstens 3 °C, nur kurzzeitig'),
]
ALLGEMEIN = ('Eine tägliche Temperaturkontrolle ist gute Praxis; gesetzlich vorgeschrieben ist eine dokumentierte '
             'Eigenkontrolle nach Art und Größe des Betriebs (VO (EG) Nr. 852/2004).')
BFR = ('Empfehlungen des Bundesinstituts für Risikobewertung (BfR), keine gesetzlichen Grenzwerte; legen Sie Ihre '
       'Werte in Ihrem HACCP-Konzept fest.')
REINIGUNG_HINWEIS = 'Beispielwerte; Mittel und Dosierung laut Herstellerangabe.'

# Vorgaben der Hitzeschritte (Schlüssel, Beschriftung, Wert, Einheit) — BfR-Empfehlungen, in gelben Zellen änderbar
VORGABEN = [
    ('heiss_t', 'Heißhalten – Temperatur an allen Stellen mindestens', 60, '°C'),
    ('heiss_d', 'Heißhalten – Dauer höchstens', 180, 'Minuten'),
    ('abk_start', 'Abkühlen – Zeitmessung ab einer Kerntemperatur von', 60, '°C'),
    ('abk_ende', 'Abkühlen – Kerntemperatur am Ende höchstens', 7, '°C'),
    ('abk_d', 'Abkühlen – Dauer höchstens', 120, 'Minuten'),
    ('garen_t', 'Garen / Regenerieren – Kerntemperatur mindestens', 72, '°C'),
    ('garen_d', 'Garen / Regenerieren – Haltezeit mindestens', 2, 'Minuten'),
]
V_ERSTE = 5  # erste Zeile der Vorgaben im Blatt «Heißhalten und Abkühlen»
V = {k: f'$F${V_ERSTE + i}' for i, (k, _, _, _) in enumerate(VORGABEN)}
N_ZEILEN = 12  # Zeilen je Block (Heißhalten, Abkühlen, Garen)

# (Bereich/Gegenstand, Was, Wann, Womit, Wie, Wer) — Beispielwerte, alles in gelben Zellen änderbar
REINIGUNG = [
    ('Arbeitsflächen (Edelstahl)', 'Reinigen und desinfizieren', 'Nach jedem Arbeitsgang und bei Schichtende',
     'Reiniger und Flächendesinfektion', 'Abräumen, reinigen, klar abspülen, desinfizieren; Einwirkzeit einhalten',
     'Postenkoch'),
    ('Schneidbretter (Farbsystem)', 'Reinigen und desinfizieren', 'Nach jeder Verwendung',
     'Spülmaschine oder Reiniger und Desinfektion', 'Spülen, trocken lagern; Bretter mit tiefen Schnittriefen ersetzen',
     'Postenkoch'),
    ('Messer, Kleingeräte, Schöpfkellen', 'Reinigen', 'Nach jeder Verwendung', 'Spülmaschine oder Handspülmittel',
     'Spülen, trocknen, sauber und getrennt lagern', 'Postenkoch'),
    ('Kühlschränke (innen, Dichtungen)', 'Reinigen und desinfizieren', 'Wöchentlich; Verschüttetes sofort',
     'Reiniger und Flächendesinfektion', 'Ware kühl umlagern, auswischen, Dichtungen reinigen, trocknen, einräumen',
     'Frühschicht'),
    ('Kühlraum (Regale, Boden)', 'Reinigen', 'Boden täglich, Regale wöchentlich', 'Reiniger, für Regale zusätzlich '
     'Desinfektion', 'Regal für Regal leeren und auswischen; Boden nass wischen', 'Frühschicht'),
    ('Tiefkühlgeräte', 'Abtauen und reinigen', 'Nach Bedarf (bei Eisbildung)', 'Reiniger',
     'Ware in ein anderes Tiefkühlgerät umlagern, abtauen, auswischen, trocknen', 'Küchenleitung'),
    ('Dunstabzugshaube, Fettfilter', 'Fettfilter reinigen, Haube abwischen', 'Wöchentlich, bei starker Nutzung öfter',
     'Fettlöser', 'Filter ausbauen, einweichen oder in der Spülmaschine reinigen, trocknen, einsetzen', 'Spülkraft'),
    ('Fritteuse', 'Öl prüfen und wechseln, Becken reinigen', 'Öl täglich prüfen; Becken bei jedem Ölwechsel',
     'Fritteusenreiniger', 'Abkühlen lassen, Öl ablassen, Becken reinigen, gründlich spülen und trocknen',
     'Postenkoch'),
    ('Herd, Grill, Plancha', 'Reinigen', 'Täglich nach dem Service', 'Grillreiniger oder Fettlöser',
     'Abschaben, Reiniger auftragen, klar nachwischen', 'Postenkoch'),
    ('Kombidämpfer, Backofen', 'Reinigen', 'Täglich nach Betriebsende', 'Reinigungsmittel des Geräteherstellers',
     'Reinigungsprogramm starten, Türdichtung abwischen', 'Spätschicht'),
    ('Spülmaschine', 'Reinigen, Siebe leeren, Temperaturanzeige prüfen', 'Täglich nach Betriebsende',
     'Reiniger; Entkalker nach Bedarf', 'Wasser ablassen, Siebe und Sprüharme reinigen, offen trocknen lassen',
     'Spülkraft'),
    ('Böden und Abläufe (Küche)', 'Reinigen', 'Täglich nach Betriebsende, bei Verschmutzung sofort', 'Bodenreiniger',
     'Kehren, nass wischen, Abläufe und Siebe reinigen', 'Spülkraft'),
    ('Abfallbehälter', 'Leeren und reinigen', 'Leeren täglich, reinigen wöchentlich', 'Reiniger und Desinfektion',
     'Leeren, auswaschen, desinfizieren, trocknen, neuen Beutel einlegen', 'Spülkraft'),
    ('Türgriffe, Schalter, Gerätegriffe', 'Reinigen und desinfizieren', 'Täglich', 'Flächendesinfektion',
     'Abwischen; Einwirkzeit einhalten', 'Spätschicht'),
    ('Handwaschbecken, Seifen- und Papierspender', 'Reinigen und auffüllen', 'Täglich', 'Sanitärreiniger',
     'Becken reinigen, Spender auffüllen, Funktion prüfen', 'Spätschicht'),
]
assert 12 <= len(REINIGUNG) <= 15 and all(len(r) == 6 for r in REINIGUNG)
R_LEER = 10


def de(s):
    """Deutsche Typografie: geschütztes Leerzeichen zwischen Zahl und Einheit und in «z. B.», «Nr. 852»."""
    if not isinstance(s, str) or s.startswith('='):
        return s
    s = s.replace('z. B.', f'z.{NB}B.')
    s = re.sub(r'(§|Abs\.|Nr\.) (\d)', r'\1' + NB + r'\2', s)
    return re.sub(r'(\d) (°C|h|min|Minuten|Stunden|%)(?![\wäöüß])', r'\1' + NB + r'\2', s)


def zelle(ws, zeile, spalte, wert=None, fmt=None, eing=False, fett=False, fond=None, umbruch=True, mitte=False):
    c = ws.cell(row=zeile, column=spalte, value=de(wert))
    c.border = rahmen
    if fmt:
        c.number_format = fmt
    if eing:
        c.fill = eingabe
    elif fond:
        c.fill = fond
    if fett:
        c.font = Font(bold=True)
    c.alignment = Alignment(wrap_text=umbruch, vertical='center' if mitte else 'top',
                            horizontal='center' if mitte else None)
    return c


def verbinden(ws, zeile, s1, s2, z2=None):
    ws.merge_cells(start_row=zeile, start_column=s1, end_row=z2 or zeile, end_column=s2)


def rahmen_bereich(ws, zeile, s1, s2, fond=None):
    for s in range(s1, s2 + 1):
        ws.cell(row=zeile, column=s).border = rahmen
        if fond:
            ws.cell(row=zeile, column=s).fill = fond


def blattkopf(ws, titel, anleitung, letzte):
    ws['A1'] = de(titel)
    ws['A1'].font = Font(bold=True, size=16, color=GOLD)
    ws['A1'].fill = schwarz
    verbinden(ws, 1, 1, letzte)
    ws.row_dimensions[1].height = 24
    ws['A2'] = de(anleitung)
    ws['A2'].font = Font(italic=True, color='555555')
    ws['A2'].alignment = Alignment(wrap_text=True, vertical='top')
    verbinden(ws, 2, 1, letzte)
    ws.row_dimensions[2].height = 30


def kopfzeile(ws, zeile, koepfe, hoehe=44, z2=None):
    for s, txt in enumerate(koepfe, start=1):
        if txt is None:
            continue
        c = ws.cell(row=zeile, column=s, value=de(txt))
        c.font = Font(bold=True, color='FFFFFF')
        c.fill = schwarz
        c.alignment = Alignment(wrap_text=True, horizontal='center', vertical='center')
        c.border = rahmen
        if z2:
            ws.cell(row=z2, column=s).border = rahmen
            ws.cell(row=z2, column=s).fill = schwarz
    ws.row_dimensions[zeile].height = hoehe


def notizen(ws, zeile, texte, letzte, hoehe=30):
    for i, n in enumerate(texte):
        c = ws.cell(row=zeile + i, column=1, value=de(n))
        c.font = Font(italic=True, color='555555')
        c.alignment = Alignment(wrap_text=True, vertical='top')
        verbinden(ws, zeile + i, 1, letzte)
        ws.row_dimensions[zeile + i].height = hoehe
    return zeile + len(texte)


def artikel_link(ws, zeile, letzte, bis=5):
    ws.cell(row=zeile, column=1, value='Leitfaden zum HACCP-Konzept (7 Grundsätze, Muster-Plan):').font = Font(bold=True)
    verbinden(ws, zeile, 1, bis)
    c = ws.cell(row=zeile, column=bis + 1, value=ARTIKEL)
    c.hyperlink = ARTIKEL
    c.font = Font(color='0563C1', underline='single')
    verbinden(ws, zeile, bis + 1, letzte)


def seite(ws, titel_zeilen, fixieren, breiten):
    for s, w in breiten.items():
        ws.column_dimensions[s].width = w
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = fixieren
    if titel_zeilen:
        ws.print_title_rows = titel_zeilen
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True


def pruefung_temp(ws, bereich, mini, maxi):
    dv = DataValidation(type='decimal', operator='between', formula1=str(mini), formula2=str(maxi), allow_blank=True,
                        showErrorMessage=True, errorTitle='Temperatur',
                        error=de(f'Geben Sie eine Temperatur in °C zwischen {mini} und {maxi} ein (z. B. 3,5 oder -18).'))
    ws.add_data_validation(dv)
    for b in bereich.split():
        dv.add(b)


def pruefung_minuten(ws, bereich):
    dv = DataValidation(type='whole', operator='between', formula1='1', formula2='1440', allow_blank=True,
                        showErrorMessage=True, errorTitle='Minuten',
                        error='Geben Sie eine ganze Zahl von Minuten zwischen 1 und 1440 ein.')
    ws.add_data_validation(dv)
    for b in bereich.split():
        dv.add(b)


def pruefung_uhrzeit(ws, bereich):
    dv = DataValidation(type='time', operator='between', formula1='0', formula2='0.999305556', allow_blank=True,
                        showErrorMessage=True, errorTitle='Uhrzeit',
                        error=de('Geben Sie eine Uhrzeit im Format hh:mm ein (z. B. 14:30).'))
    ws.add_data_validation(dv)
    for b in bereich.split():
        dv.add(b)


def pruefung_datum(ws, bereich):
    dv = DataValidation(type='date', operator='greaterThanOrEqual', formula1='36526', allow_blank=True,
                        showErrorMessage=True, errorTitle='Datum', error=de('Geben Sie ein Datum ein, z. B. 25.11.2026.'))
    ws.add_data_validation(dv)
    for b in bereich.split():
        dv.add(b)


# ---------------------------------------------------------------- Blatt 1: Kühlung und Tiefkühlung
def blatt_kuehlung(wb):
    ws = wb.create_sheet('Kühlung und Tiefkühlung')
    blattkopf(ws, 'HACCP-Temperaturliste – Kühlung und Tiefkühlung',
              'Füllen Sie die gelben Zellen aus. Die Spalte „In Ordnung?“ berechnet sich automatisch; Maßnahme und '
              'Kürzel trägt die Person ein, die misst.', 9)
    for i, k in enumerate(['Betrieb', 'Monat und Jahr', 'Verantwortlich']):
        zelle(ws, 3 + i, 1, k, fett=True)
        verbinden(ws, 3 + i, 1, 2)
        zelle(ws, 3 + i, 3, None, eing=True)
        for s in (4, 5):
            ws.cell(row=3 + i, column=s).border = rahmen
        verbinden(ws, 3 + i, 3, 5)

    # Geräte (A7:I10) — Bezeichnung und Grenzwert änderbar
    for s, txt in ((1, 'Gerät'), (3, 'Bezeichnung (änderbar)'), (6, 'Max. °C'), (7, 'Vorgabe und Quelle')):
        zelle(ws, 7, s, txt, fett=True, fond=grau)
    for a, b in ((1, 2), (3, 5), (7, 9)):
        rahmen_bereich(ws, 7, a, b, grau)
        verbinden(ws, 7, a, b)
    for i, (name, tmax, quelle) in enumerate(GERAETE):
        z = 8 + i
        zelle(ws, z, 1, f'Gerät {i + 1}', fett=True)
        zelle(ws, z, 3, name, eing=True)
        zelle(ws, z, 6, tmax, F_GRENZE, eing=True, fett=True, mitte=True)
        zelle(ws, z, 7, quelle).font = Font(size=9)
        ws.cell(row=z, column=7).alignment = Alignment(vertical='center', wrap_text=True)
        for a, b in ((1, 2), (3, 5), (7, 9)):
            rahmen_bereich(ws, z, a, b)
            verbinden(ws, z, a, b)
        # 18 pt statt 30: Zeilen 1–14 sind fixiert (D15), so bleibt beim Blättern mehr Platz für die Messungen
        ws.row_dimensions[z].height = 18
    pruefung_temp(ws, 'F8:F10', -40, 30)
    grenze = ['$F$8', '$F$9', '$F$10']
    notizen(ws, 11, ['Tragen Sie Ihre Geräte und die Grenzwerte aus Ihrem HACCP-Konzept ein. Die Vorgaben gelten für die '
                     'genannte Ware; lagern Sie verschiedene Waren zusammen, gilt der strengste Wert.'], 9, 18)
    ws['A11'].font = Font(italic=True, color='555555', size=10)  # 10 pt: eine Zeile über A:I

    # Kopf der Liste (2 Zeilen: Gerätename, dann Grenzwert — beide folgen den Angaben oben)
    kz = 13
    kopfzeile(ws, kz, ['Tag', 'Messung', 'Uhrzeit', None, None, None, 'In Ordnung?', 'Maßnahme (bei Abweichung)',
                       'Kürzel'], hoehe=48, z2=kz + 1)
    for s in (1, 2, 3, 7, 8, 9):
        verbinden(ws, kz, s, s, z2=kz + 1)
    for k, s in enumerate((4, 5, 6)):
        for z, f in ((kz, f'=C{8 + k}'), (kz + 1, f'="max. "&IF({grenze[k]}>0,"+","")&{grenze[k]}&"{NB}°C"')):
            c = ws.cell(row=z, column=s, value=f)
            c.font = Font(bold=True, color=GOLD if z == kz + 1 else 'FFFFFF')
            c.fill = schwarz
            c.alignment = Alignment(wrap_text=True, horizontal='center', vertical='center')
            c.border = rahmen
    ws.row_dimensions[kz + 1].height = 18

    p1 = kz + 2
    z = p1
    for tag in range(1, 32):
        for messung in ('Morgens', 'Abends'):
            zelle(ws, z, 1, tag, mitte=True)
            zelle(ws, z, 2, messung)
            zelle(ws, z, 3, None, F_UHR, eing=True, mitte=True)
            for s in (4, 5, 6):
                zelle(ws, z, s, None, F_TEMP, eing=True, mitte=True)
            ws.cell(row=z, column=7, value=(
                f'=IF(COUNT(D{z}:F{z})=0,"",IF(AND(OR(D{z}="",D{z}<={grenze[0]}),OR(E{z}="",E{z}<={grenze[1]}),'
                f'OR(F{z}="",F{z}<={grenze[2]})),"Ja","NEIN"))'))
            ws.cell(row=z, column=7).alignment = Alignment(horizontal='center', vertical='center')
            ws.cell(row=z, column=7).border = rahmen
            zelle(ws, z, 8, None, eing=True)
            zelle(ws, z, 9, None, eing=True)
            if messung == 'Abends':
                for s in range(1, 10):
                    ws.cell(row=z, column=s).border = rahmen_tag
            z += 1
    pn = z - 1
    assert pn - p1 + 1 == 62
    pruefung_uhrzeit(ws, f'C{p1}:C{pn}')
    pruefung_temp(ws, f'D{p1}:F{pn}', -40, 30)
    ws.conditional_formatting.add(f'G{p1}:G{pn}', CellIsRule(operator='equal', formula=['"NEIN"'], fill=rot,
                                                             font=Font(bold=True)))
    for k, s in enumerate('DEF'):
        ws.conditional_formatting.add(f'{s}{p1}:{s}{pn}',
                                      FormulaRule(formula=[f'AND({s}{p1}<>"",{s}{p1}>{grenze[k]})'], fill=rot))

    fz = notizen(ws, pn + 2, [
        ALLGEMEIN,
        'Messen Sie mit einem geprüften Thermometer und verlassen Sie sich nicht allein auf die Anzeige des Geräts. '
        'Die Messung am Abend ist optional; die Häufigkeit legen Sie in Ihrem HACCP-Konzept fest.',
        'Tiefkühlung: Nach der TLMV ist eine Abweichung nach oben um höchstens 3 °C nur kurzzeitig zulässig. „In '
        'Ordnung?“ prüft immer gegen den eingetragenen Grenzwert; notieren Sie bei einem höheren Wert die Ursache und '
        'messen Sie nach.',
        'Jeder rote Wert braucht eine schriftliche Maßnahme und eine Nachmessung, die zeigt, dass der Grenzwert wieder '
        'eingehalten wird.',
        'Prüfen Sie Ihre Thermometer regelmäßig und bewahren Sie die Listen so lange auf, wie es Ihr HACCP-Konzept '
        'vorsieht.',
    ], 9)
    artikel_link(ws, fz + 1, 9)
    seite(ws, f'{kz}:{kz + 1}', f'D{p1}',
          {'A': 6, 'B': 10, 'C': 8, 'D': 20, 'E': 20, 'F': 20, 'G': 12, 'H': 44, 'I': 10})
    return p1


# ---------------------------------------------------------------- Blatt 2: Heißhalten und Abkühlen (+ Garen)
BLOECKE = [
    ('heiss', f'="Heißhalten – mindestens "&{V["heiss_t"]}&"{NB}°C an allen Stellen, höchstens "&{V["heiss_d"]}'
              f'&"{NB}Minuten"',
     ['Datum', 'Speise', 'Uhrzeit Beginn', 'Temperatur Beginn (°C)', 'Uhrzeit Messung', 'Niedrigste Temperatur (°C)',
      'Dauer', 'In Ordnung?', 'Maßnahme (bei Abweichung)', 'Kürzel']),
    ('abk', f'="Abkühlen – von "&{V["abk_start"]}&"{NB}°C auf höchstens "&{V["abk_ende"]}&"{NB}°C Kerntemperatur '
            f'in höchstens "&{V["abk_d"]}&"{NB}Minuten"',
     ['Datum', 'Speise', 'Uhrzeit Beginn', 'Kerntemperatur Beginn (°C)', 'Uhrzeit Ende', 'Kerntemperatur Ende (°C)',
      'Dauer', 'In Ordnung?', 'Maßnahme (bei Abweichung)', 'Kürzel']),
    ('garen', f'="Garen / Regenerieren – Kerntemperatur mindestens "&{V["garen_t"]}&"{NB}°C für mindestens "'
              f'&{V["garen_d"]}&"{NB}Minuten"',
     ['Datum', 'Speise', 'Uhrzeit Kerntemperatur erreicht', 'Kerntemperatur (°C)', 'Uhrzeit Ende Haltezeit',
      'Kerntemperatur Ende (°C)', 'Haltezeit', 'In Ordnung?', 'Maßnahme (bei Abweichung)', 'Kürzel']),
]


def formel_ok(art, z):
    """«In Ordnung?» je Block; Dauer in G (MOD … 1: über Mitternacht), auf ganze Minuten gerundet. Abkühlen prüft
    auch die Starttemperatur in D, wenn eingetragen."""
    if art == 'heiss':
        return (f'=IF(OR(G{z}="",F{z}=""),"",IF(AND(ROUND(G{z}*1440,0)<={V["heiss_d"]},F{z}>={V["heiss_t"]},'
                f'OR(D{z}="",D{z}>={V["heiss_t"]})),"Ja","NEIN"))')
    if art == 'abk':
        return (f'=IF(OR(G{z}="",F{z}=""),"",IF(AND(ROUND(G{z}*1440,0)<={V["abk_d"]},F{z}<={V["abk_ende"]},'
                f'OR(D{z}="",D{z}>={V["abk_start"]})),"Ja","NEIN"))')
    # Garen: G < 0,5 (unter 12 h) fängt vertauschte Uhrzeiten ab (12:05 → 12:00 ergäbe sonst 1435 min und «Ja»)
    return (f'=IF(OR(G{z}="",D{z}=""),"",IF(AND(ROUND(G{z}*1440,0)>={V["garen_d"]},G{z}<0.5,D{z}>={V["garen_t"]},'
            f'OR(F{z}="",F{z}>={V["garen_t"]})),"Ja","NEIN"))')


def blatt_heiss(wb):
    ws = wb.create_sheet('Heißhalten und Abkühlen')
    blattkopf(ws, 'HACCP-Temperaturliste – Heißhalten, Abkühlen, Garen',
              'Füllen Sie die gelben Zellen aus (Uhrzeiten im Format hh:mm). Dauer und „In Ordnung?“ berechnen sich '
              'automatisch nach den Vorgaben in der Tabelle darunter.', 10)
    vz = V_ERSTE - 1
    for (a, b), txt in (((1, 5), 'Vorgabe (änderbar)'), ((6, 6), 'Wert'), ((7, 10), 'Einheit')):
        zelle(ws, vz, a, txt, fett=True, fond=grau)
        rahmen_bereich(ws, vz, a, b, grau)
        verbinden(ws, vz, a, b)
    for i, (_, text, wert, einheit) in enumerate(VORGABEN):
        z = V_ERSTE + i
        zelle(ws, z, 1, text)
        rahmen_bereich(ws, z, 1, 5)
        verbinden(ws, z, 1, 5)
        zelle(ws, z, 6, wert, eing=True, fett=True, mitte=True)
        zelle(ws, z, 7, einheit)
        rahmen_bereich(ws, z, 7, 10)
        verbinden(ws, z, 7, 10)
        ws.row_dimensions[z].height = 18
    temps = ' '.join(V[k].replace('$', '') for k in ('heiss_t', 'abk_start', 'abk_ende', 'garen_t'))
    minuten = ' '.join(V[k].replace('$', '') for k in ('heiss_d', 'abk_d', 'garen_d'))
    pruefung_temp(ws, temps, -30, 110)
    pruefung_minuten(ws, minuten)
    vl = V_ERSTE + len(VORGABEN)
    c = ws.cell(row=vl, column=1, value=de(BFR))
    c.font = Font(bold=True, italic=True, color='555555')
    c.alignment = Alignment(wrap_text=True, vertical='top')
    verbinden(ws, vl, 1, 10)
    ws.row_dimensions[vl].height = 30

    starts = {}
    z = vl + 2
    for art, balken, koepfe in BLOECKE:
        b = ws.cell(row=z, column=1, value=de(balken))
        b.font = Font(bold=True, size=12, color=GOLD)
        b.fill = schwarz
        b.alignment = Alignment(vertical='center')
        verbinden(ws, z, 1, 10)
        ws.row_dimensions[z].height = 22
        kopfzeile(ws, z + 1, koepfe)
        q1 = z + 2
        starts[art] = q1
        for r in range(q1, q1 + N_ZEILEN):
            zelle(ws, r, 1, None, F_DATUM, eing=True, mitte=True)
            zelle(ws, r, 2, None, eing=True)
            zelle(ws, r, 3, None, F_UHR, eing=True, mitte=True)
            zelle(ws, r, 4, None, F_TEMP, eing=True, mitte=True)
            zelle(ws, r, 5, None, F_UHR, eing=True, mitte=True)
            zelle(ws, r, 6, None, F_TEMP, eing=True, mitte=True)
            zelle(ws, r, 7, f'=IF(OR(C{r}="",E{r}=""),"",MOD(E{r}-C{r},1))', F_MIN if art == 'garen' else F_DAUER,
                  mitte=True)
            zelle(ws, r, 8, formel_ok(art, r), mitte=True)
            zelle(ws, r, 9, None, eing=True)
            zelle(ws, r, 10, None, eing=True)
            ws.row_dimensions[r].height = 22
        qn = q1 + N_ZEILEN - 1
        pruefung_datum(ws, f'A{q1}:A{qn}')
        pruefung_uhrzeit(ws, f'C{q1}:C{qn} E{q1}:E{qn}')
        pruefung_temp(ws, f'D{q1}:D{qn} F{q1}:F{qn}', -30, 110)
        ws.conditional_formatting.add(f'H{q1}:H{qn}', CellIsRule(operator='equal', formula=['"NEIN"'], fill=rot,
                                                                 font=Font(bold=True)))
        if art == 'heiss':
            regeln = [('D', f'AND(D{q1}<>"",D{q1}<{V["heiss_t"]})'), ('F', f'AND(F{q1}<>"",F{q1}<{V["heiss_t"]})'),
                      ('G', f'AND(ISNUMBER(G{q1}),G{q1}*1440>{V["heiss_d"]}+0.5)')]
        elif art == 'abk':
            regeln = [('D', f'AND(D{q1}<>"",D{q1}<{V["abk_start"]})'), ('F', f'AND(F{q1}<>"",F{q1}>{V["abk_ende"]})'),
                      ('G', f'AND(ISNUMBER(G{q1}),G{q1}*1440>{V["abk_d"]}+0.5)')]
        else:
            regeln = [('D', f'AND(D{q1}<>"",D{q1}<{V["garen_t"]})'), ('F', f'AND(F{q1}<>"",F{q1}<{V["garen_t"]})'),
                      ('G', f'AND(ISNUMBER(G{q1}),G{q1}*1440<{V["garen_d"]}-0.5)')]
        for s, f in regeln:
            ws.conditional_formatting.add(f'{s}{q1}:{s}{qn}', FormulaRule(formula=[f], fill=rot))
        z = qn + 2

    fz = notizen(ws, z, [
        '„In Ordnung?“ vergleicht mit den Vorgaben oben (gelbe Zellen). Die Dauer berücksichtigt einen Wechsel über '
        'Mitternacht.',
        'Heißhalten: Messen Sie an der kältesten Stelle und tragen Sie den niedrigsten Wert ein.',
        'Abkühlen: Starten Sie die Zeitmessung, sobald der Kern die Starttemperatur aus den Vorgaben erreicht hat.',
        'Garen / Regenerieren: Tragen Sie die Uhrzeit ein, zu der der Kern die Mindesttemperatur erreicht, und die '
        'Uhrzeit am Ende der Haltezeit.',
    ], 10, 18)
    artikel_link(ws, fz + 1, 10)
    seite(ws, None, 'C3', {'A': 12, 'B': 28, 'C': 11, 'D': 13, 'E': 11, 'F': 13, 'G': 11, 'H': 11, 'I': 34, 'J': 9})
    return starts


# ---------------------------------------------------------------- Blatt 3: Reinigungsplan
def blatt_reinigung(wb):
    ws = wb.create_sheet('Reinigungsplan')
    blattkopf(ws, 'Reinigungsplan – Gastronomieküche',
              'Passen Sie die gelben Zellen an Ihre Küche an: Bereiche, Häufigkeit, Mittel und Zuständigkeit. Tragen '
              'Sie unter „Erledigt“ Datum und Kürzel ein.', 7)
    for i, k in enumerate(['Betrieb', 'Gültig ab', 'Verantwortlich']):
        zelle(ws, 3 + i, 1, k, fett=True)
        zelle(ws, 3 + i, 2, None, F_DATUM if k == 'Gültig ab' else None, eing=True)
        rahmen_bereich(ws, 3 + i, 2, 3)
        verbinden(ws, 3 + i, 2, 3)
    pruefung_datum(ws, 'B4')
    kz = 7
    kopfzeile(ws, kz, ['Bereich / Gegenstand', 'Was', 'Wann (Häufigkeit)', 'Womit (Mittel, Dosierung)', 'Wie', 'Wer',
                       'Erledigt (Datum / Kürzel)'], hoehe=32)
    r1 = kz + 1
    for i, eintrag in enumerate(REINIGUNG + [None] * R_LEER):
        z = r1 + i
        for s in range(1, 7):
            zelle(ws, z, s, eintrag[s - 1] if eintrag else None, eing=True)
        zelle(ws, z, 7, None, eing=True)
        ws.row_dimensions[z].height = 32 if eintrag else 22
    rn = r1 + len(REINIGUNG) + R_LEER - 1
    dv = DataValidation(type='textLength', operator='lessThanOrEqual', formula1='250', allow_blank=True,
                        showErrorMessage=True, errorTitle='Text', error='Höchstens 250 Zeichen je Zelle.')
    ws.add_data_validation(dv)
    dv.add(f'A{r1}:G{rn}')
    fz = notizen(ws, rn + 2, [REINIGUNG_HINWEIS,
                              'Reinigen Sie immer vor dem Desinfizieren, und halten Sie die Einwirkzeit des '
                              'Desinfektionsmittels ein.'], 7, 18)
    artikel_link(ws, fz + 1, 7, bis=3)
    seite(ws, f'{kz}:{kz}', f'B{r1}', {'A': 30, 'B': 24, 'C': 26, 'D': 28, 'E': 44, 'F': 14, 'G': 20})
    return r1


# ---------------------------------------------------------------- PDF zum Ausdrucken
def pdf_druck():
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    def t(s):
        """PDF-Text: deutsche Typografie + WinAnsi der Standardschrift (Helvetica: ä, ö, ü, ß, „ “, –, °). Das
        Minuszeichen U+2212 fehlt in WinAnsi: der Halbgeviertstrich «–» (0x96) ersetzt es, nicht der Bindestrich."""
        s = de(s).replace('−', '–')
        s.encode('cp1252')  # UnicodeEncodeError, falls ein Zeichen nicht darstellbar wäre (≤, ≥ …)
        return s

    linie, sw, gold = colors.HexColor('#999999'), colors.HexColor('#111111'), colors.HexColor('#FFD700')
    s_h = ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=10.5, leading=12.5, spaceBefore=5, spaceAfter=2,
                         textColor=sw)
    s_txt = ParagraphStyle('t', fontName='Helvetica', fontSize=8, leading=10)
    s_note = ParagraphStyle('n', fontName='Helvetica-Oblique', fontSize=7.3, leading=9, textColor=colors.HexColor('#333333'))
    s_th = ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=7.2, leading=8.3, alignment=1, textColor=colors.white)
    s_zelle = ParagraphStyle('z', fontName='Helvetica', fontSize=6.9, leading=8)
    s_zelle_f = ParagraphStyle('zf', parent=s_zelle, fontName='Helvetica-Bold')
    W = A4[0] - 28 * mm

    def band(text):
        b = Table([[t(text)]], colWidths=[W])
        b.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), sw), ('TEXTCOLOR', (0, 0), (-1, -1), gold),
                               ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 13),
                               ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 7)]))
        return b

    def fuss(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica-Oblique', 7.5)
        canvas.setFillColor(colors.HexColor('#555555'))
        canvas.drawCentredString(A4[0] / 2, 7 * mm, t(FUSS))
        canvas.restoreState()

    def raster(koepfe, anteile, n, hoehe=18):
        assert abs(sum(anteile) - 1) < 1e-9
        tb = Table([[Paragraph(t(x), s_th) for x in koepfe]] + [[''] * len(koepfe) for _ in range(n)],
                   colWidths=[W * x for x in anteile], rowHeights=[26] + [hoehe] * n)
        tb.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, linie), ('BACKGROUND', (0, 0), (-1, 0), sw),
                                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, 0), 2),
                                ('RIGHTPADDING', (0, 0), (-1, 0), 2), ('TOPPADDING', (0, 0), (-1, 0), 2),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 2)]))
        return tb

    doc = SimpleDocTemplate(str(PDF), pagesize=A4, leftMargin=14 * mm, rightMargin=14 * mm, topMargin=11 * mm,
                            bottomMargin=14 * mm, title=t('HACCP-Vorlagen: Temperaturkontrolle und Reinigungsplan'),
                            author='AI Chef Pro',
                            subject=t('Kühlung, Tiefkühlung, Heißhalten, Abkühlen, Garen und Reinigungsplan'))
    # Seite 1 — Kühlung und Tiefkühlung, ein Monat
    el = [band('Temperaturliste Kühlung und Tiefkühlung – Monat: ……………………'), Spacer(1, 4)]
    info = Table([['Betrieb:', '', 'Verantwortlich:', '']], colWidths=[W * 0.1, W * 0.45, W * 0.15, W * 0.3],
                 rowHeights=17)
    info.setStyle(TableStyle([('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 8.5),
                              ('LINEBELOW', (1, 0), (1, 0), 0.5, linie), ('LINEBELOW', (3, 0), (3, 0), 0.5, linie),
                              ('VALIGN', (0, 0), (-1, -1), 'BOTTOM')]))
    el += [info, Spacer(1, 5)]
    namen = [('Kühlraum (Fleischzubereitungen, Geflügel)', 'max. +4 °C'), ('Kühlschrank (Hackfleisch)', 'max. +2 °C'),
             ('Tiefkühlung', 'max. –18 °C')]
    s_th0 = ParagraphStyle('th0', parent=s_th, fontSize=7, leading=8)
    z0 = [Paragraph('Tag', s_th0)] + sum([[Paragraph(t(n), s_th0), ''] for n, _ in namen], []) + \
         [Paragraph(t('Maßnahme (bei Abweichung)'), s_th0), Paragraph(t('Kürzel'), s_th0)]
    z1 = [''] + sum([[t(m), ''] for _, m in namen], []) + ['', '']
    z2 = [''] + ['Morgens', 'Abends'] * 3 + ['', '']
    zeilen = [z0, z1, z2] + [[str(j)] + [''] * 8 for j in range(1, 32)]
    anteile = [0.055] + [0.093] * 6 + [0.277, 0.11]
    assert abs(sum(anteile) - 1) < 1e-9
    tb = Table(zeilen, colWidths=[W * x for x in anteile], rowHeights=[29, 12, 12] + [19] * 31, repeatRows=3)  # Zeile 0: bis zu 3 Zeilen Gerätename
    stil = [('GRID', (0, 0), (-1, -1), 0.5, linie),
            ('BACKGROUND', (0, 0), (-1, 2), sw), ('TEXTCOLOR', (0, 0), (-1, 2), colors.white),
            ('TEXTCOLOR', (1, 1), (6, 1), gold),
            ('FONTNAME', (0, 0), (-1, 2), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 2), 7.2),
            ('FONTNAME', (0, 3), (0, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 3), (-1, -1), 9),
            ('ALIGN', (0, 0), (-2, -1), 'CENTER'), ('ALIGN', (-1, 0), (-1, 2), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, 0), 2),
            ('RIGHTPADDING', (0, 0), (-1, 0), 2),
            ('SPAN', (0, 0), (0, 2)), ('SPAN', (7, 0), (7, 2)), ('SPAN', (8, 0), (8, 2))]
    for k in range(3):
        c = 1 + 2 * k
        stil += [('SPAN', (c, 0), (c + 1, 0)), ('SPAN', (c, 1), (c + 1, 1)),
                 ('LINEAFTER', (c + 1, 0), (c + 1, -1), 1.2, sw)]
    for j in range(1, 32):  # Orientierung: jede zweite Woche grau
        if ((j - 1) // 7) % 2 == 1:
            stil.append(('BACKGROUND', (0, 2 + j), (0, 2 + j), colors.HexColor('#F3F3F3')))
    tb.setStyle(TableStyle(stil))
    el += [tb, Spacer(1, 4),
           Paragraph(t('Beispiel-Grenzwerte – Höchstwerte aus VO (EG) Nr. 853/2004 (für Ware, die den Betrieb '
                       'verlässt) und TLMV: Fleischzubereitungen und Geflügelfleisch höchstens +4 °C, Hackfleisch '
                       'höchstens +2 °C; Tiefkühlung −18 °C oder kälter, nach oben höchstens 3 °C Abweichung und nur '
                       'kurzzeitig. Tragen Sie Ihre Geräte und die Grenzwerte Ihres HACCP-Konzepts ein; die Messung am '
                       'Abend ist optional.'), s_note),
           Spacer(1, 2), Paragraph(t(ALLGEMEIN), s_note), PageBreak()]

    # Seite 2 — Heißhalten, Abkühlen, Garen + Reinigungsplan (Kurzfassung)
    el += [band('Heißhalten, Abkühlen, Garen und Reinigungsplan')]
    kopf_heiss = ['Datum', 'Speise', 'Uhrzeit Beginn', 'Temp. Beginn (°C)', 'Uhrzeit Messung', 'Niedrigste Temp. (°C)',
                  'Dauer', 'In Ordnung?', 'Maßnahme', 'Kürzel']
    kopf_abk = ['Datum', 'Speise', 'Uhrzeit Beginn', 'Kerntemp. Beginn (°C)', 'Uhrzeit Ende', 'Kerntemp. Ende (°C)',
                'Dauer', 'In Ordnung?', 'Maßnahme', 'Kürzel']
    kopf_garen = ['Datum', 'Speise', 'Uhrzeit Kern erreicht', 'Kerntemp. (°C)', 'Uhrzeit Ende Haltezeit',
                  'Kerntemp. Ende (°C)', 'Haltezeit', 'In Ordnung?', 'Maßnahme', 'Kürzel']
    anteile2 = [0.08, 0.17, 0.075, 0.085, 0.08, 0.09, 0.07, 0.08, 0.18, 0.09]
    el += [Paragraph(t('Heißhalten'), s_h),
           Paragraph(t('Mindestens 60 °C an allen Stellen, höchstens 3 Stunden. Messen Sie an der kältesten Stelle. '
                       '„In Ordnung?“: ja oder nein.'), s_txt), Spacer(1, 2), raster(kopf_heiss, anteile2, 4),
           Paragraph(t('Abkühlen'), s_h),
           Paragraph(t('Von 60 °C auf höchstens 7 °C Kerntemperatur in höchstens 120 Minuten; Zeitmessung ab 60 °C. '
                       '„In Ordnung?“: ja oder nein.'), s_txt), Spacer(1, 2), raster(kopf_abk, anteile2, 4),
           Paragraph(t('Garen und Regenerieren'), s_h),
           Paragraph(t('Kerntemperatur 72 °C für mindestens 2 Minuten. „In Ordnung?“: ja oder nein.'), s_txt),
           Spacer(1, 2), raster(kopf_garen, anteile2, 4), Spacer(1, 3),
           Paragraph(t('Alle Werte dieser Seite: ' + BFR), s_note)]

    el += [Paragraph(t('Reinigungsplan (Kurzfassung)'), s_h)]
    anteile3 = [0.25, 0.23, 0.27, 0.11, 0.14]
    assert abs(sum(anteile3) - 1) < 1e-9
    rz = [[Paragraph(t(x), s_th) for x in ('Bereich / Gegenstand', 'Was', 'Wann', 'Wer', 'Erledigt (Datum / Kürzel)')]]
    rz += [[Paragraph(t(b), s_zelle_f), Paragraph(t(w), s_zelle), Paragraph(t(wann), s_zelle), Paragraph(t(wer), s_zelle),
            ''] for b, w, wann, _, _, wer in REINIGUNG]
    rt = Table(rz, colWidths=[W * x for x in anteile3], repeatRows=1)
    rt.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, linie), ('BACKGROUND', (0, 0), (-1, 0), sw),
                            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('TOPPADDING', (0, 0), (-1, -1), 1.3),
                            ('BOTTOMPADDING', (0, 0), (-1, -1), 1.3),
                            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#FAFAFA')])]))
    el += [rt, Spacer(1, 3),
           Paragraph(t(REINIGUNG_HINWEIS + ' Der vollständige Plan mit „Womit“ und „Wie“ steht in der Excel-Datei.'),
                     s_note)]
    doc.build(el, onFirstPage=fuss, onLaterPages=fuss)


# ---------------------------------------------------------------- Gates
def cache_text_leer(pfad):
    """inject_cache.py injiziert das Ergebnis «""» nicht: die Zelle behält einen leeren Cache (<v></v>, als 0 gelesen),
    und Betrachter ohne Neuberechnung (macOS-Vorschau, Handy) zeigen «0» in «In Ordnung?» und «Dauer». Hier wird der
    Cache «leerer Text» wie in Excel geschrieben (t="str" + <v></v>), ohne den Rest des Zip anzufassen."""
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
    assert int(m.group(1)) == int(m.group(2)) + leer, (aus, leer)  # jede Formel hat einen Cache (Wert oder leerer Text)
    return f'{aus.strip()} cache_texte_vide={leer}'


def hm(h, m):
    return (h * 60 + m) / 1440


K, H = 'Kühlung und Tiefkühlung', 'Heißhalten und Abkühlen'


def faelle_pruefen(faelle, vorgaben=None):
    """Testwerte in einer TEMPORÄREN Kopie (die veröffentlichte Datei bleibt leer); vorgaben = {(Blatt, Zelle): Wert}."""
    with tempfile.TemporaryDirectory() as tmp:
        kopie = Path(tmp) / 'test.xlsx'
        shutil.copy(XLSX, kopie)
        wb = load_workbook(kopie)
        for (blatt, ref), wert in (vorgaben or {}).items():
            wb[blatt][ref] = wert
        for blatt, z, werte, _, _, _ in faelle:
            for s, v in werte.items():
                wb[blatt].cell(row=z, column=s, value=v)
        wb.save(kopie)
        injizieren(kopie)
        wv = load_workbook(kopie, data_only=True)
        erg = []
        for blatt, z, _, s_ok, erw, beschr in faelle:
            v = wv[blatt].cell(row=z, column=s_ok).value
            erg.append((blatt, beschr, erw, None if v == '' else v))
        dauern = {(blatt, z): wv[blatt].cell(row=z, column=7).value for blatt, z, *_ in faelle if blatt == H}
    return erg, dauern


def minuten(d):
    return d.total_seconds() / 60 if hasattr(d, 'total_seconds') else d * 1440  # openpyxl liest [h]:mm als timedelta


def gate_logik(p1, st):
    h, a, g = st['heiss'], st['abk'], st['garen']
    faelle = [  # (Blatt, Zeile, {Spalte: Wert}, Spalte «In Ordnung?», erwartet, Beschreibung)
        (K, p1 + 0, {4: 3.5}, 7, 'Ja', 'Kühlraum 3,5 °C (Grenze +4)'),
        (K, p1 + 1, {4: 4.1}, 7, 'NEIN', 'Kühlraum 4,1 °C (Grenze +4)'),
        (K, p1 + 2, {5: 2.0}, 7, 'Ja', 'Hackfleisch 2,0 °C, genau an der Grenze +2'),
        (K, p1 + 3, {5: 2.5}, 7, 'NEIN', 'Hackfleisch 2,5 °C (Grenze +2)'),
        (K, p1 + 4, {6: -19}, 7, 'Ja', 'Tiefkühlung −19 °C (Grenze −18)'),
        (K, p1 + 5, {6: -16}, 7, 'NEIN', 'Tiefkühlung −16 °C: über dem eingetragenen Grenzwert'),
        (K, p1 + 6, {3: hm(8, 0), 4: 3, 5: 1.5, 6: -20}, 7, 'Ja', 'alle drei Geräte in Ordnung'),
        (K, p1 + 7, {3: hm(18, 0), 4: 3, 5: 3, 6: -20}, 7, 'NEIN', 'nur Hackfleisch über der Grenze'),
        (K, p1 + 8, {3: hm(9, 0), 8: 'nur Text', 9: 'MG'}, 7, None, 'Uhrzeit + Maßnahme + Kürzel ohne Messwert → leer'),
        (K, p1 + 9, {}, 7, None, 'leere Zeile → leer'),
        (H, h + 0, {3: hm(12, 0), 4: 75, 5: hm(14, 30), 6: 63}, 8, 'Ja', 'Heißhalten 2 h 30, niedrigster Wert 63 °C'),
        (H, h + 1, {3: hm(12, 0), 4: 75, 5: hm(15, 0), 6: 60}, 8, 'Ja', 'Heißhalten 3 h 00 und 60 °C (Grenzen inklusive)'),
        (H, h + 2, {3: hm(12, 0), 4: 75, 5: hm(15, 10), 6: 62}, 8, 'NEIN', 'Heißhalten 3 h 10'),
        (H, h + 3, {3: hm(12, 0), 4: 75, 5: hm(13, 0), 6: 58}, 8, 'NEIN', 'Heißhalten 58 °C an der kältesten Stelle'),
        (H, h + 4, {3: hm(12, 0), 4: 55, 5: hm(13, 0), 6: 62}, 8, 'NEIN', 'Heißhalten beginnt mit 55 °C'),
        (H, h + 5, {3: hm(22, 30), 4: 70, 5: hm(0, 30), 6: 65}, 8, 'Ja', 'Heißhalten 22:30 → 00:30 (Mitternacht)'),
        (H, h + 6, {2: 'Gulasch', 3: hm(12, 0), 4: 70}, 8, None, 'Heißhalten ohne Messung → leer'),
        (H, h + 7, {}, 8, None, 'leere Zeile → leer'),
        (H, a + 0, {3: hm(14, 0), 4: 60, 5: hm(15, 40), 6: 6}, 8, 'Ja', 'Abkühlen 1 h 40 auf 6 °C'),
        (H, a + 1, {3: hm(14, 0), 4: 60, 5: hm(16, 0), 6: 7}, 8, 'Ja', 'Abkühlen 120 min auf 7 °C (Grenzen inklusive)'),
        (H, a + 2, {3: hm(14, 0), 4: 60, 5: hm(16, 5), 6: 5}, 8, 'NEIN', 'Abkühlen 125 min'),
        (H, a + 3, {3: hm(14, 0), 4: 60, 5: hm(15, 30), 6: 9}, 8, 'NEIN', 'Abkühlen 90 min, aber 9 °C'),
        (H, a + 4, {3: hm(23, 15), 4: 60, 5: hm(0, 45), 6: 6}, 8, 'Ja', 'Abkühlen 23:15 → 00:45 (Mitternacht)'),
        (H, a + 5, {2: 'Rinderbrühe', 3: hm(14, 0), 4: 60}, 8, None, 'Abkühlen ohne Ende → leer'),
        (H, a + 6, {}, 8, None, 'leere Zeile → leer'),
        (H, a + 7, {3: hm(14, 0), 4: 50, 5: hm(15, 0), 6: 5}, 8, 'NEIN', 'Abkühlen beginnt mit 50 °C (Start unter 60)'),
        (H, a + 8, {3: hm(14, 0), 5: hm(15, 0), 6: 5}, 8, 'Ja', 'Abkühlen ohne Starttemperatur: Dauer und Ende'),
        (H, g + 0, {3: hm(12, 0), 4: 74, 5: hm(12, 2), 6: 73}, 8, 'Ja', 'Garen 74 °C, 2 min gehalten'),
        (H, g + 1, {3: hm(12, 0), 4: 72, 5: hm(12, 3)}, 8, 'Ja', 'Garen genau 72 °C, 3 min, ohne Endmessung'),
        (H, g + 2, {3: hm(12, 0), 4: 75, 5: hm(12, 1), 6: 75}, 8, 'NEIN', 'Garen nur 1 min gehalten'),
        (H, g + 3, {3: hm(12, 0), 4: 70, 5: hm(12, 5), 6: 72}, 8, 'NEIN', 'Garen: Kern 70 °C'),
        (H, g + 4, {3: hm(12, 0), 4: 74, 5: hm(12, 4), 6: 69}, 8, 'NEIN', 'Garen: Kern fällt in der Haltezeit auf 69 °C'),
        (H, g + 5, {3: hm(23, 59), 4: 75, 5: hm(0, 2), 6: 74}, 8, 'Ja', 'Garen 23:59 → 00:02 (Mitternacht)'),
        (H, g + 6, {}, 8, None, 'leere Zeile → leer'),
        (H, g + 7, {3: hm(12, 5), 4: 75, 5: hm(12, 0), 6: 74}, 8, 'NEIN', 'Garen: Uhrzeiten vertauscht (1435 min)'),
    ]
    erg, dauern = faelle_pruefen(faelle)
    assert abs(minuten(dauern[(H, h)]) - 150) < 1e-6, dauern[(H, h)]
    assert abs(minuten(dauern[(H, a)]) - 100) < 1e-6, dauern[(H, a)]
    assert abs(minuten(dauern[(H, g + 5)]) - 3) < 1e-6, dauern[(H, g + 5)]
    assert abs(minuten(dauern[(H, g + 7)]) - 1435) < 1e-6, dauern[(H, g + 7)]
    # Die Vorgaben sind änderbar: Heißhalten auf 65 °C, Kühlraum auf +5 °C → dieselben Formeln folgen.
    z_heiss_t = int(V['heiss_t'].split('$')[-1])
    faelle2 = [(H, h, {3: hm(12, 0), 4: 75, 5: hm(13, 0), 6: 63}, 8, 'NEIN', 'Vorgabe Heißhalten 65 °C: 63 °C'),
               (K, p1, {4: 4.5}, 7, 'Ja', 'Grenze Kühlraum auf +5 °C geändert: 4,5 °C')]
    erg2, _ = faelle_pruefen(faelle2, {(H, f'F{z_heiss_t}'): 65, (K, 'F8'): 5})
    for blatt, beschr, erw, v in erg + erg2:
        print(f'  {"OK " if erw == v else "KO "} [{blatt}] {beschr} → {v!r} (erwartet {erw!r})')
    assert all(erw == v for _, _, erw, v in erg + erg2), 'Gate Logik KO'
    return len(erg) + len(erg2)


def gate_veroeffentlicht(p1, st, r1):
    wv = load_workbook(XLSX, data_only=True)
    assert wv.sheetnames == [K, H, 'Reinigungsplan'], wv.sheetnames
    ws = wv[K]
    koepfe = [(ws.cell(row=13, column=s).value, ws.cell(row=14, column=s).value) for s in (4, 5, 6)]
    assert koepfe == [(GERAETE[0][0], f'max. +4{NB}°C'), (GERAETE[1][0], f'max. +2{NB}°C'),
                      ('Tiefkühlung', f'max. -18{NB}°C')], koepfe
    assert [ws.cell(row=8 + i, column=6).value for i in range(3)] == [4, 2, -18]
    for z in range(p1, p1 + 62):
        for s in range(3, 10):
            assert ws.cell(row=z, column=s).value in (None, ''), (z, s, ws.cell(row=z, column=s).value)
    hs = wv[H]
    assert [hs.cell(row=V_ERSTE + i, column=6).value for i in range(len(VORGABEN))] == [60, 180, 60, 7, 120, 72, 2]
    balken = [hs.cell(row=st[art] - 2, column=1).value for art in ('heiss', 'abk', 'garen')]
    assert balken == [f'Heißhalten – mindestens 60{NB}°C an allen Stellen, höchstens 180{NB}Minuten',
                      f'Abkühlen – von 60{NB}°C auf höchstens 7{NB}°C Kerntemperatur in höchstens 120{NB}Minuten',
                      f'Garen / Regenerieren – Kerntemperatur mindestens 72{NB}°C für mindestens 2{NB}Minuten'], balken
    for q1 in st.values():
        for z in range(q1, q1 + N_ZEILEN):
            for s in range(1, 11):
                assert hs.cell(row=z, column=s).value in (None, ''), (z, s)
    rs = wv['Reinigungsplan']
    assert [rs.cell(row=r1 + i, column=1).value for i in range(len(REINIGUNG))] == [de(r[0]) for r in REINIGUNG]
    for z in range(r1, r1 + len(REINIGUNG) + R_LEER):
        assert rs.cell(row=z, column=7).value is None
    for z in range(r1 + len(REINIGUNG), r1 + len(REINIGUNG) + R_LEER):
        assert all(rs.cell(row=z, column=s).value is None for s in range(1, 8))
    wf = load_workbook(XLSX)
    alles = {b.title: ' '.join(str(c.value) for row in b.iter_rows() for c in row if c.value).replace(NB, ' ')
             for b in wf.worksheets}
    assert ALLGEMEIN in alles[K] and BFR in alles[H] and REINIGUNG_HINWEIS in alles['Reinigungsplan']
    assert 'VO (EG) Nr. 853/2004' in alles[K] and 'TLMV' in alles[K]
    assert not any(x in ' '.join(alles.values()) for x in ('DIN', 'DEHOGA', '65 °C')), 'verbotene Quelle oder Wert'
    for b in wf.worksheets:
        assert any(c.hyperlink and c.hyperlink.target == ARTIKEL for row in b.iter_rows() for c in row), b.title
        assert all(d.showErrorMessage for d in b.data_validations.dataValidation), b.title
        assert b.data_validations.dataValidation, b.title
    z = zipfile.ZipFile(XLSX)
    ausgew = [n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml$', n)
              and 'tabSelected="1"' in z.read(n).decode('utf-8')]
    assert ausgew == ['xl/worksheets/sheet1.xml'], ausgew


def gate_pdf():
    warnings.filterwarnings('ignore')
    from pypdf import PdfReader
    rd = PdfReader(str(PDF))
    n = len(rd.pages)
    assert n == 2, n
    texte = [' '.join(p.extract_text().replace(NB, ' ').split()) for p in rd.pages]
    for erwartet in ('Temperaturliste Kühlung und Tiefkühlung', 'max. +4 °C', 'max. +2 °C', 'max. –18 °C',
                     'VO (EG) Nr. 853/2004', 'TLMV', 'VO (EG) Nr. 852/2004', 'Morgens', 'Abends',
                     'aichef.pro/de/blog/haccp-konzept'):
        assert erwartet in texte[0], ('Seite 1', erwartet)
    for erwartet in ('Heißhalten', 'Abkühlen', 'Garen und Regenerieren', 'Mindestens 60 °C an allen Stellen',
                     'höchstens 3 Stunden', 'höchstens 7 °C', '120 Minuten', '72 °C für mindestens 2 Minuten',
                     'Bundesinstituts für Risikobewertung (BfR)', 'keine gesetzlichen Grenzwerte',
                     'Reinigungsplan (Kurzfassung)', 'Schneidbretter', 'Fettfilter', 'Fritteuse', 'Türgriffe',
                     'Mittel und Dosierung laut Herstellerangabe', 'aichef.pro/de/blog/haccp-konzept'):
        assert erwartet in texte[1], ('Seite 2', erwartet)
    alles = ' '.join(texte)
    assert not any(x in alles for x in ('DIN', 'DEHOGA', '65 °C')), 'verbotene Quelle oder Wert'
    return n


def main():
    wb = Workbook()
    wb.remove(wb.active)
    p1 = blatt_kuehlung(wb)
    st = blatt_heiss(wb)
    r1 = blatt_reinigung(wb)
    for i, ws in enumerate(wb.worksheets):
        ws.sheet_view.tabSelected = (i == 0)
    wb.active = 0
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.title = 'HACCP-Vorlagen: Temperaturkontrolle und Reinigungsplan'
    XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb.save(XLSX)
    print(injizieren(XLSX))
    gate_veroeffentlicht(p1, st, r1)
    n_faelle = gate_logik(p1, st)
    pdf_druck()
    seiten = gate_pdf()
    print(f'OK {XLSX.name} · 3 Blätter · 62 Messungen + 3 × {N_ZEILEN} Zeilen leer · Reinigungsplan {len(REINIGUNG)} '
          f'Beispiele + {R_LEER} leer · Gate Logik {n_faelle}/{n_faelle} · {PDF.name} ({seiten} Seiten)')


if __name__ == '__main__':
    main()
