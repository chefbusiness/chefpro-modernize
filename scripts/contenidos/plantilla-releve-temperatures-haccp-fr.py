#!/usr/bin/env python3
"""Relevé de températures HACCP (FR), gratuit — lead magnet de /fr/blog/haccp.

Gemelo francés de plantilla-registro-temperaturas-appcc-gratis.py (mismo diseño, colores y gate), ADAPTADO a Francia:
  - límites por defecto del arrêté du 21 décembre 2009, annexe I («en tous points du produit»): +3 °C préparations
    élaborées à l'avance, +4 °C denrées très périssables, −18 °C congelés (autres denrées congelées −12 °C), en celdas
    amarillas editables (art. 3: GBPH validé o analyse des dangers validée → cada local pone los de SU PMS);
  - frecuencia del GBPH Restaurateur: al menos un relevé al día con termómetro → 31 días × matin/soir (soir facultatif);
  - refroidissement rapide (objetivo editable, +10 °C por defecto, ≤ 2 h) y remise en température (≥ +63 °C, ≤ 1 h).
LowFruits FR (nov-2026): «normes haccp restauration pdf» 140, «fiche haccp» 90, «relevé de température haccp» 40,
«fiche relevé température» 30.

Uso:  python3 scripts/contenidos/plantilla-releve-temperatures-haccp-fr.py
Sale: astro-site/public/descargas/releve-temperatures-haccp-gratuit-aichef.xlsx  (3 hojas, celdas de lectura vacías)
      astro-site/public/descargas/releve-temperatures-haccp-gratuit-aichef.pdf   (A4, 2 páginas, a rellenar a mano)
El xlsx pasa por inject_cache.py y un gate data_only; la lógica de «Conforme ?» se prueba en una COPIA temporal con
valores de prueba (la salida publicada no lleva ninguno). Después:
  python3 scripts/productos-digitales/parche_xml_xlsx.py --check astro-site/public/descargas/releve-temperatures-haccp-gratuit-aichef.xlsx
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
XLSX = RAIZ / 'astro-site/public/descargas/releve-temperatures-haccp-gratuit-aichef.xlsx'
PDF = RAIZ / 'astro-site/public/descargas/releve-temperatures-haccp-gratuit-aichef.pdf'
INJECT = RAIZ / 'scripts/productos-digitales/inject_cache.py'
GUIDE = 'https://aichef.pro/fr/blog/haccp'
PIED = 'Modèle gratuit AI Chef Pro · guide : aichef.pro/fr/blog/haccp'

NOIR, OR, GRIS = '111111', 'FFD700', 'F3F3F3'
fin = Side(style='thin', color='BBBBBB')
bord = Border(left=fin, right=fin, top=fin, bottom=fin)
bord_jour = Border(left=fin, right=fin, top=fin, bottom=Side(style='thin', color='555555'))
saisie = PatternFill('solid', fgColor='FFF8D6')
rouge = PatternFill('solid', fgColor='F8CBAD')
gris = PatternFill('solid', fgColor=GRIS)
NB = '\u00a0'
F_TEMP = '+0.0;-0.0;0.0'
F_LIM = '+0;-0;0'
F_HEURE = 'hh:mm'
F_DUREE = '[h]" h "mm'
F_DATE = 'dd/mm/yyyy'

# (nom par défaut, T° max °C, valeur de l'annexe I) — faits vérifiés, rien d'autre
ENCEINTES = [
    ("Chambre froide — préparations élaborées à l'avance", 3, "Préparations élaborées à l'avance : +3 °C maximum"),
    ('Réfrigérateur — denrées très périssables', 4,
     "Denrées très périssables : +4 °C maximum (autres denrées : voir l'annexe I)"),
    ('Congélateur', -18,
     'Glaces, viandes hachées et produits de la pêche congelés : −18 °C (autres denrées congelées : −12 °C)'),
]
OBJECTIF_REFROIDISSEMENT = 10
N_LIGNES = 20


def fr(s):
    """Typographie française : espace insécable avant « : ; ? ! », à l'intérieur des guillemets et avant l'unité."""
    if not isinstance(s, str) or s.startswith('='):
        return s
    s = re.sub(r' ([:;?!»])', NB + r'\1', s)
    s = s.replace('« ', '«' + NB)
    s = re.sub(r'(\d) (°C|h|min|m³|%)(?!\w)', r'\1' + NB + r'\2', s)
    return s


def cel(ws, ligne, col, valeur=None, fmt=None, entree=False, gras=False, fond=None, wrap=True, centre=False):
    c = ws.cell(row=ligne, column=col, value=fr(valeur))
    c.border = bord
    if fmt:
        c.number_format = fmt
    if entree:
        c.fill = saisie
    elif fond:
        c.fill = fond
    if gras:
        c.font = Font(bold=True)
    c.alignment = Alignment(wrap_text=wrap, vertical='center' if centre else 'top',
                            horizontal='center' if centre else None)
    return c


def fusion(ws, ligne, c1, c2, l2=None):
    ws.merge_cells(start_row=ligne, start_column=c1, end_row=l2 or ligne, end_column=c2)


def en_tete_feuille(ws, titre, consigne, derniere_col):
    ws['A1'] = fr(titre)
    ws['A1'].font = Font(bold=True, size=16, color=OR)
    ws['A1'].fill = PatternFill('solid', fgColor=NOIR)
    fusion(ws, 1, 1, derniere_col)
    ws.row_dimensions[1].height = 24
    ws['A2'] = fr(consigne)
    ws['A2'].font = Font(italic=True, color='555555')
    ws['A2'].alignment = Alignment(wrap_text=True, vertical='top')
    fusion(ws, 2, 1, derniere_col)
    ws.row_dimensions[2].height = 30


def ligne_entetes(ws, ligne, entetes, hauteur=44, l2=None):
    for col, txt in enumerate(entetes, start=1):
        if txt is None:
            continue
        c = ws.cell(row=ligne, column=col, value=fr(txt))
        c.font = Font(bold=True, color='FFFFFF')
        c.fill = PatternFill('solid', fgColor=NOIR)
        c.alignment = Alignment(wrap_text=True, horizontal='center', vertical='center')
        c.border = bord
        if l2:
            ws.cell(row=l2, column=col).border = bord
            ws.cell(row=l2, column=col).fill = PatternFill('solid', fgColor=NOIR)
    ws.row_dimensions[ligne].height = hauteur


def notes(ws, ligne, textes, derniere_col, hauteur=30):
    for i, n in enumerate(textes):
        c = ws.cell(row=ligne + i, column=1, value=fr(n))
        c.font = Font(italic=True, color='555555')
        c.alignment = Alignment(wrap_text=True, vertical='top')
        fusion(ws, ligne + i, 1, derniere_col)
        ws.row_dimensions[ligne + i].height = hauteur
    return ligne + len(textes)


def lien_guide(ws, ligne, derniere_col):
    ws.cell(row=ligne, column=1, value=fr('Guide HACCP en restauration (7 principes, températures, exemple) :')).font = Font(bold=True)
    fusion(ws, ligne, 1, 5)
    c = ws.cell(row=ligne, column=6, value=GUIDE)
    c.hyperlink = GUIDE
    c.font = Font(color='0563C1', underline='single')
    fusion(ws, ligne, 6, derniere_col)


def mise_en_page(ws, titres, gel, largeurs):
    for col, w in largeurs.items():
        ws.column_dimensions[col].width = w
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = gel
    ws.print_title_rows = titres
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True


def validation_temp(ws, plage, mini, maxi):
    dv = DataValidation(type='decimal', operator='between', formula1=str(mini), formula2=str(maxi), allow_blank=True,
                        showErrorMessage=True, errorTitle='Température',
                        error=fr(f'Saisissez une température en °C entre {mini} et {maxi} (par exemple 3,5 ou -18).'))
    ws.add_data_validation(dv)
    for p in plage.split():
        dv.add(p)


def validation_heure(ws, plage):
    dv = DataValidation(type='time', operator='between', formula1='0', formula2='0.999305556', allow_blank=True,
                        showErrorMessage=True, errorTitle='Heure',
                        error=fr('Saisissez une heure au format hh:mm (par exemple 14:30).'))
    ws.add_data_validation(dv)
    for p in plage.split():
        dv.add(p)


# ---------------------------------------------------------------- feuille 1 : enceintes froides
def feuille_enceintes(wb):
    ws = wb.create_sheet('Enceintes froides')
    en_tete_feuille(ws, 'Relevé de températures HACCP — enceintes froides',
                    "Remplissez les cellules jaunes. La colonne « Conforme ? » se calcule seule ; l'action corrective "
                    'et le visa sont à compléter par la personne qui fait le relevé.', 9)
    for i, k in enumerate(['Établissement', 'Mois et année', 'Responsable']):
        cel(ws, 3 + i, 1, k, gras=True)
        fusion(ws, 3 + i, 1, 2)
        cel(ws, 3 + i, 3, None, entree=True)
        for col in (4, 5):
            ws.cell(row=3 + i, column=col).border = bord
        fusion(ws, 3 + i, 3, 5)

    # Paramètres des enceintes (A7:I10) — noms et limites modifiables
    for col, txt in ((1, 'Enceinte'), (3, "Nom de l'enceinte (modifiable)"), (6, 'T° max (°C)'),
                     (7, 'Valeur par défaut (arrêté du 21 décembre 2009, annexe I)')):
        cel(ws, 7, col, txt, gras=True, fond=gris)
    for a, b in ((1, 2), (3, 5), (7, 9)):
        for col in range(a, b + 1):
            ws.cell(row=7, column=col).border = bord
            ws.cell(row=7, column=col).fill = gris
        fusion(ws, 7, a, b)
    for i, (nom, tmax, ref) in enumerate(ENCEINTES):
        lg = 8 + i
        cel(ws, lg, 1, f'Enceinte {i + 1}', gras=True)
        cel(ws, lg, 3, nom, entree=True)
        cel(ws, lg, 6, tmax, F_LIM, entree=True, gras=True, centre=True)
        cel(ws, lg, 7, ref)
        for a, b in ((1, 2), (3, 5), (7, 9)):
            for col in range(a, b + 1):
                ws.cell(row=lg, column=col).border = bord
            fusion(ws, lg, a, b)
        ws.row_dimensions[lg].height = 30
    validation_temp(ws, 'F8:F10', -40, 30)
    lim = ['$F$8', '$F$9', '$F$10']
    notes(ws, 11, ["Températures exigées « en tous points du produit ». L'arrêté (article 3) admet une autre température "
                   "si elle est prévue par un GBPH validé ou par une analyse des dangers validée : reportez ici les "
                   'valeurs de VOTRE plan de maîtrise sanitaire (PMS).'], 9, 32)

    # En-têtes du relevé (2 lignes : nom de l'enceinte, puis sa limite — les deux suivent les paramètres)
    ft = 13
    ligne_entetes(ws, ft, ['Jour', 'Relevé', 'Heure', None, None, None, 'Conforme ?',
                           'Action corrective (si non conforme)', 'Visa'], hauteur=48, l2=ft + 1)
    for col in (1, 2, 3, 7, 8, 9):
        fusion(ws, ft, col, col, l2=ft + 1)
    for k, col in enumerate((4, 5, 6)):
        for lg, f in ((ft, f'=C{8 + k}'), (ft + 1, f'="max "&IF({lim[k]}>0,"+","")&{lim[k]}&"{NB}°C"')):
            c = ws.cell(row=lg, column=col, value=f)
            c.font = Font(bold=True, color=OR if lg == ft + 1 else 'FFFFFF')
            c.fill = PatternFill('solid', fgColor=NOIR)
            c.alignment = Alignment(wrap_text=True, horizontal='center', vertical='center')
            c.border = bord
    ws.row_dimensions[ft + 1].height = 18

    p1 = ft + 2
    r = p1
    for jour in range(1, 32):
        for moment in ('Matin', 'Soir'):
            cel(ws, r, 1, jour, centre=True)
            cel(ws, r, 2, moment)
            cel(ws, r, 3, None, F_HEURE, entree=True, centre=True)
            for col in (4, 5, 6):
                cel(ws, r, col, None, F_TEMP, entree=True, centre=True)
            ws.cell(row=r, column=7, value=(
                f'=IF(COUNT(D{r}:F{r})=0,"",IF(AND(OR(D{r}="",D{r}<={lim[0]}),OR(E{r}="",E{r}<={lim[1]}),'
                f'OR(F{r}="",F{r}<={lim[2]})),"Oui","NON"))'))
            ws.cell(row=r, column=7).alignment = Alignment(horizontal='center', vertical='center')
            ws.cell(row=r, column=7).border = bord
            cel(ws, r, 8, None, entree=True)
            cel(ws, r, 9, None, entree=True)
            if moment == 'Soir':
                for col in range(1, 10):
                    ws.cell(row=r, column=col).border = bord_jour
            r += 1
    pn = r - 1
    assert pn - p1 + 1 == 62
    validation_heure(ws, f'C{p1}:C{pn}')
    validation_temp(ws, f'D{p1}:F{pn}', -40, 30)
    ws.conditional_formatting.add(f'G{p1}:G{pn}', CellIsRule(operator='equal', formula=['"NON"'], fill=rouge,
                                                             font=Font(bold=True)))
    for k, col in enumerate('DEF'):
        ws.conditional_formatting.add(f'{col}{p1}:{col}{pn}',
                                      FormulaRule(formula=[f'AND({col}{p1}<>"",{col}{p1}>{lim[k]})'], fill=rouge))

    fn = notes(ws, pn + 2, [
        "Fréquence : le GBPH Restaurateur recommande de contrôler les enceintes froides au moins une fois par jour "
        "avec un thermomètre, en plus de la lecture de l'afficheur. Le relevé du soir est facultatif.",
        "En surveillance visuelle, l'enregistrement obligatoire se limite aux non-conformités et aux actions "
        'correctives (instruction technique DGAL 2023-756) ; un relevé complet reste la meilleure preuve lors d\'un '
        'contrôle.',
        'Le GBPH prévoit un enregistrement automatique pour les équipements de froid négatif de plus de 10 m³.',
        'Chaque relevé en rouge appelle une action corrective écrite, puis un nouveau relevé pour vérifier le retour '
        'dans les limites.',
        'Vérifiez vos thermomètres et conservez ces relevés selon ce que prévoit votre PMS.',
    ], 9)
    lien_guide(ws, fn + 1, 9)
    mise_en_page(ws, f'{ft}:{ft + 1}', f'D{p1}',
                 {'A': 6, 'B': 9, 'C': 8, 'D': 18, 'E': 18, 'F': 18, 'G': 11, 'H': 46, 'I': 10})
    return p1


# ---------------------------------------------------------------- feuille 2 : refroidissement rapide
def feuille_refroidissement(wb):
    ws = wb.create_sheet('Refroidissement rapide')
    en_tete_feuille(ws, 'Relevé de refroidissement rapide (HACCP)',
                    'Remplissez les cellules jaunes (heures au format hh:mm). La durée et la colonne « Conforme ? » '
                    'se calculent seules.', 10)
    cel(ws, 4, 1, 'Objectif de température à cœur en fin de refroidissement (°C)', gras=True)
    fusion(ws, 4, 1, 5)
    cel(ws, 4, 6, OBJECTIF_REFROIDISSEMENT, F_LIM, entree=True, gras=True, centre=True)
    validation_temp(ws, 'F4', -10, 30)
    cel(ws, 5, 1, 'Durée maximale du refroidissement', gras=True)
    fusion(ws, 5, 1, 5)
    cel(ws, 5, 6, '2 h', fond=gris, gras=True, centre=True)
    notes(ws, 6, ["Restauration collective (annexe IV de l'arrêté) : de +63 °C à +10 °C à cœur en moins de 2 heures, "
                  'obligatoire. Restaurant commercial : le GBPH Restaurateur vise moins de +6 °C à cœur en 2 heures '
                  '(pièces volumineuses non portionnables : à déterminer). Ensuite, stockage entre 0 et +3 °C.'], 10, 44)
    ft = 8
    ligne_entetes(ws, ft, ['Date', 'Préparation', 'Heure début', 'T° à cœur début (≥ +63 °C)', 'Heure fin',
                           'T° à cœur fin (°C)', 'Durée', 'Conforme ?', 'Action corrective', 'Visa'])
    q1 = ft + 1
    for r in range(q1, q1 + N_LIGNES):
        cel(ws, r, 1, None, F_DATE, entree=True, centre=True)
        cel(ws, r, 2, None, entree=True)
        cel(ws, r, 3, None, F_HEURE, entree=True, centre=True)
        cel(ws, r, 4, None, F_TEMP, entree=True, centre=True)
        cel(ws, r, 5, None, F_HEURE, entree=True, centre=True)
        cel(ws, r, 6, None, F_TEMP, entree=True, centre=True)
        cel(ws, r, 7, f'=IF(OR(C{r}="",E{r}=""),"",MOD(E{r}-C{r},1))', F_DUREE, centre=True)
        cel(ws, r, 8, f'=IF(OR(G{r}="",F{r}=""),"",IF(AND(ROUND(G{r}*1440,0)<=120,F{r}<=$F$4),"Oui","NON"))',
            centre=True)
        cel(ws, r, 9, None, entree=True)
        cel(ws, r, 10, None, entree=True)
        ws.row_dimensions[r].height = 22
    qn = q1 + N_LIGNES - 1
    validation_heure(ws, f'C{q1}:C{qn} E{q1}:E{qn}')
    validation_temp(ws, f'D{q1}:D{qn} F{q1}:F{qn}', -30, 110)
    ws.conditional_formatting.add(f'H{q1}:H{qn}', CellIsRule(operator='equal', formula=['"NON"'], fill=rouge,
                                                             font=Font(bold=True)))
    ws.conditional_formatting.add(f'F{q1}:F{qn}', FormulaRule(formula=[f'AND(F{q1}<>"",F{q1}>$F$4)'], fill=rouge))
    ws.conditional_formatting.add(f'G{q1}:G{qn}', FormulaRule(formula=[f'AND(ISNUMBER(G{q1}),G{q1}*1440>120.5)'],
                                                              fill=rouge))
    fn = notes(ws, qn + 2, ['« Conforme ? » : durée de 2 h au plus et température à cœur finale inférieure ou égale à '
                            "l'objectif. La durée tient compte d'un passage de minuit."], 10, 30)
    lien_guide(ws, fn + 1, 10)
    mise_en_page(ws, f'{ft}:{ft}', f'C{q1}',
                 {'A': 12, 'B': 30, 'C': 9, 'D': 14, 'E': 9, 'F': 12, 'G': 9, 'H': 11, 'I': 36, 'J': 10})
    return q1


# ---------------------------------------------------------------- feuille 3 : remise en température
def feuille_remise(wb):
    ws = wb.create_sheet('Remise en température')
    en_tete_feuille(ws, 'Relevé de remise en température (HACCP)',
                    'Remplissez les cellules jaunes (heures au format hh:mm). La durée et la colonne « Conforme ? » '
                    'se calculent seules.', 9)
    cel(ws, 4, 1, 'Température à cœur à atteindre', gras=True)
    fusion(ws, 4, 1, 5)
    cel(ws, 4, 6, 'au moins +63 °C', fond=gris, gras=True, centre=True)
    cel(ws, 4, 7, None, fond=gris)
    fusion(ws, 4, 6, 7)
    cel(ws, 5, 1, 'Durée maximale de la remise en température', gras=True)
    fusion(ws, 5, 1, 5)
    cel(ws, 5, 6, '1 h', fond=gris, gras=True, centre=True)
    cel(ws, 5, 7, None, fond=gris)
    fusion(ws, 5, 6, 7)
    notes(ws, 6, ["Atteindre au moins +63 °C à cœur en moins d'une heure ; consommer dans la continuité ; ne jamais "
                  'refroidir une seconde fois. Obligatoire en restauration collective, référence du GBPH pour les '
                  'restaurants.'], 9, 30)
    ft = 8
    ligne_entetes(ws, ft, ['Date', 'Préparation', 'Heure début', 'Heure à +63 °C', 'T° à cœur atteinte (°C)',
                           'Durée', 'Conforme ?', 'Action corrective', 'Visa'])
    q1 = ft + 1
    for r in range(q1, q1 + N_LIGNES):
        cel(ws, r, 1, None, F_DATE, entree=True, centre=True)
        cel(ws, r, 2, None, entree=True)
        cel(ws, r, 3, None, F_HEURE, entree=True, centre=True)
        cel(ws, r, 4, None, F_HEURE, entree=True, centre=True)
        cel(ws, r, 5, None, F_TEMP, entree=True, centre=True)
        cel(ws, r, 6, f'=IF(OR(C{r}="",D{r}=""),"",MOD(D{r}-C{r},1))', F_DUREE, centre=True)
        cel(ws, r, 7, f'=IF(OR(F{r}="",E{r}=""),"",IF(AND(ROUND(F{r}*1440,0)<=60,E{r}>=63),"Oui","NON"))',
            centre=True)
        cel(ws, r, 8, None, entree=True)
        cel(ws, r, 9, None, entree=True)
        ws.row_dimensions[r].height = 22
    qn = q1 + N_LIGNES - 1
    validation_heure(ws, f'C{q1}:D{qn}')
    validation_temp(ws, f'E{q1}:E{qn}', -30, 110)
    ws.conditional_formatting.add(f'G{q1}:G{qn}', CellIsRule(operator='equal', formula=['"NON"'], fill=rouge,
                                                             font=Font(bold=True)))
    ws.conditional_formatting.add(f'E{q1}:E{qn}', FormulaRule(formula=[f'AND(E{q1}<>"",E{q1}<63)'], fill=rouge))
    ws.conditional_formatting.add(f'F{q1}:F{qn}', FormulaRule(formula=[f'AND(ISNUMBER(F{q1}),F{q1}*1440>60.5)'],
                                                              fill=rouge))
    fn = notes(ws, qn + 2, ['« Conforme ? » : +63 °C à cœur atteints en 1 h au plus. La durée tient compte d\'un '
                            'passage de minuit.'], 9, 18)
    lien_guide(ws, fn + 1, 9)
    mise_en_page(ws, f'{ft}:{ft}', f'C{q1}',
                 {'A': 12, 'B': 30, 'C': 9, 'D': 10, 'E': 13, 'F': 9, 'G': 11, 'H': 40, 'I': 10})
    return q1


# ---------------------------------------------------------------- PDF à imprimer
def pdf_imprimable():
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    def t(s):
        """Texte PDF : typographie française + jeu WinAnsi des polices standard (Helvetica pinte Œ, é, « », °)."""
        s = fr(s).replace('−', '-')
        s.encode('cp1252')  # lève UnicodeEncodeError si un caractère ne s'afficherait pas (≥, ≤…)
        return s

    gris_l, noir, or_ = colors.HexColor('#999999'), colors.HexColor('#111111'), colors.HexColor('#FFD700')
    s_h = ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=11, leading=13, spaceBefore=6, spaceAfter=3,
                         textColor=noir)
    s_txt = ParagraphStyle('t', fontName='Helvetica', fontSize=8, leading=10)
    s_note = ParagraphStyle('n', fontName='Helvetica-Oblique', fontSize=7.5, leading=9.2, textColor=colors.HexColor('#333333'))
    s_th = ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=7.5, leading=8.6, alignment=1, textColor=colors.white)
    W = A4[0] - 28 * mm

    def bandeau(texte):
        b = Table([[t(texte)]], colWidths=[W])
        b.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), noir), ('TEXTCOLOR', (0, 0), (-1, -1), or_),
                               ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 14),
                               ('TOPPADDING', (0, 0), (-1, -1), 6), ('BOTTOMPADDING', (0, 0), (-1, -1), 8)]))
        return b

    def pied(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica-Oblique', 7.5)
        canvas.setFillColor(colors.HexColor('#555555'))
        canvas.drawCentredString(A4[0] / 2, 7 * mm, t(PIED))
        canvas.restoreState()

    def grille_saisie(entetes, largeurs, n):
        tb = Table([[Paragraph(t(x), s_th) for x in entetes]] + [[''] * len(entetes) for _ in range(n)],
                   colWidths=[W * x for x in largeurs], rowHeights=[31] + [21] * n)
        assert abs(sum(largeurs) - 1) < 1e-9
        tb.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, gris_l), ('BACKGROUND', (0, 0), (-1, 0), noir),
                                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, 0), 3),
                                ('RIGHTPADDING', (0, 0), (-1, 0), 3), ('TOPPADDING', (0, 0), (-1, 0), 2),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 2)]))
        return tb

    doc = SimpleDocTemplate(str(PDF), pagesize=A4, leftMargin=14 * mm, rightMargin=14 * mm, topMargin=11 * mm,
                            bottomMargin=14 * mm, title=t('Relevé de températures HACCP'), author='AI Chef Pro',
                            subject=t('Enceintes froides, refroidissement rapide et remise en température'))
    el = [bandeau('Relevé des enceintes froides — mois de ……………………'), Spacer(1, 4)]
    info = Table([[t('Établissement :'), '', t('Responsable :'), '']],
                 colWidths=[W * 0.15, W * 0.4, W * 0.13, W * 0.32], rowHeights=17)
    info.setStyle(TableStyle([('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 8.5),
                              ('LINEBELOW', (1, 0), (1, 0), 0.5, gris_l), ('LINEBELOW', (3, 0), (3, 0), 0.5, gris_l),
                              ('VALIGN', (0, 0), (-1, -1), 'BOTTOM')]))
    el += [info, Spacer(1, 5)]

    noms = [('Chambre froide', 'max +3 °C'), ('Réfrigérateur', 'max +4 °C'), ('Congélateur', 'max -18 °C')]
    l0 = [t('Jour')] + sum([[t(n), ''] for n, _ in noms], []) + [t('Action corrective (si hors limite)'), t('Visa')]
    l1 = [''] + sum([[t(m), ''] for _, m in noms], []) + ['', '']
    l2 = [''] + ['Matin', 'Soir'] * 3 + ['', '']
    lignes = [l0, l1, l2] + [[str(j)] + [''] * 8 for j in range(1, 32)]
    larg = [0.055] + [0.093] * 6 + [0.277, 0.11]
    assert abs(sum(larg) - 1) < 1e-9
    tb = Table(lignes, colWidths=[W * x for x in larg], rowHeights=[13, 12, 12] + [19.3] * 31, repeatRows=3)
    style = [('GRID', (0, 0), (-1, -1), 0.5, gris_l),
             ('BACKGROUND', (0, 0), (-1, 2), noir), ('TEXTCOLOR', (0, 0), (-1, 2), colors.white),
             ('TEXTCOLOR', (1, 1), (6, 1), or_),
             ('FONTNAME', (0, 0), (-1, 2), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 2), 7.5),
             ('FONTNAME', (0, 3), (0, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 3), (-1, -1), 9),
             ('ALIGN', (0, 0), (-2, -1), 'CENTER'), ('ALIGN', (-1, 0), (-1, 2), 'CENTER'),
             ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
             ('SPAN', (0, 0), (0, 2)), ('SPAN', (7, 0), (7, 2)), ('SPAN', (8, 0), (8, 2))]
    for k in range(3):
        c = 1 + 2 * k
        style += [('SPAN', (c, 0), (c + 1, 0)), ('SPAN', (c, 1), (c + 1, 1)),
                  ('LINEAFTER', (c + 1, 0), (c + 1, -1), 1.2, noir)]
    for j in range(1, 32):  # repère visuel une semaine sur deux
        if ((j - 1) // 7) % 2 == 1:
            style.append(('BACKGROUND', (0, 2 + j), (0, 2 + j), colors.HexColor('#F3F3F3')))
    tb.setStyle(TableStyle(style))
    el += [tb, Spacer(1, 4), Paragraph(t(
        "Limites par défaut (arrêté du 21 décembre 2009, annexe I, « en tous points du produit ») : +3 °C préparations "
        "élaborées à l'avance ; +4 °C denrées très périssables ; −18 °C glaces, viandes hachées et produits de la "
        'pêche congelés (autres denrées congelées : −12 °C). Reportez les enceintes et les limites de votre PMS. '
        'Contrôle au moins une fois par jour au thermomètre (GBPH Restaurateur) ; le relevé du soir est facultatif.'),
        s_note), PageBreak()]

    el += [bandeau('Refroidissement rapide et remise en température'), Paragraph(t('Refroidissement rapide'), s_h),
           Paragraph(t('Départ : au moins +63 °C à cœur. Objectif en fin de refroidissement : ……… °C à cœur en 2 h '
                       'maximum (par défaut +10 °C ; voir les repères ci-dessous). Colonne « Conforme ? » : oui ou non.'), s_txt),
           Spacer(1, 3),
           grille_saisie(['Date', 'Préparation', 'Heure début', 'T° à cœur début', 'Heure fin', 'T° à cœur fin',
                          'Durée', 'Conforme ?', 'Action corrective', 'Visa'],
                         [0.08, 0.17, 0.075, 0.085, 0.075, 0.085, 0.07, 0.1, 0.17, 0.09], 10),
           Paragraph(t('Remise en température'), s_h),
           Paragraph(t("Atteindre au moins +63 °C à cœur en moins d'une heure. Colonne « Conforme ? » : oui ou non."), s_txt),
           Spacer(1, 3),
           grille_saisie(['Date', 'Préparation', 'Heure début', 'Heure à +63 °C', 'T° à cœur atteinte', 'Durée',
                          'Conforme ?', 'Action corrective', 'Visa'],
                         [0.08, 0.2, 0.08, 0.09, 0.095, 0.075, 0.1, 0.19, 0.09], 10),
           Paragraph(t('Repères réglementaires (abrégés)'), s_h)]
    for n in [
        "Froid : arrêté du 21 décembre 2009, annexe I. Une autre température est possible si un GBPH validé ou une "
        'analyse des dangers validée la prévoit (article 3) : suivez votre plan de maîtrise sanitaire (PMS).',
        "Surveillance visuelle : l'enregistrement obligatoire se limite aux non-conformités et aux actions correctives "
        "(instruction technique DGAL 2023-756) ; un relevé complet reste la meilleure preuve lors d'un contrôle. Froid "
        'négatif de plus de 10 m³ : enregistrement automatique prévu par le GBPH.',
        'Refroidissement : en restauration collective (annexe IV), de +63 °C à +10 °C à cœur en moins de 2 heures, '
        'obligatoire. En restaurant commercial, le GBPH Restaurateur vise moins de +6 °C à cœur en 2 heures (pièces '
        'volumineuses non portionnables : à déterminer). Ensuite, stockage entre 0 et +3 °C.',
        "Remise en température : au moins +63 °C à cœur en moins d'une heure ; consommer dans la continuité ; ne jamais "
        'refroidir une seconde fois. Obligatoire en restauration collective, référence du GBPH pour les restaurants.',
    ]:
        el += [Paragraph(t(n), s_note), Spacer(1, 2)]
    doc.build(el, onFirstPage=pied, onLaterPages=pied)


# ---------------------------------------------------------------- gate
def cache_texte_vide(chemin):
    """inject_cache.py n'injecte pas le résultat « "" » : la cellule garde un cache vide (<v></v>, lu comme 0), et les
    visionneuses qui ne recalculent pas (Aperçu macOS, mobile) affichent « 0 » dans « Conforme ? » et « Durée ».
    On écrit ici le cache « texte vide » comme le fait Excel (t="str" + <v></v>), sans toucher au reste du zip."""
    motif = re.compile(r'<c r="([A-Z]+[0-9]+)"((?:(?!\st=)[^>])*)>(<f>[^<]*</f>)(?:<v>\s*</v>|<v\s*/>)?</c>')
    with zipfile.ZipFile(chemin) as z:
        parties = [(i, z.read(i.filename)) for i in z.infolist()]
    n = 0
    with zipfile.ZipFile(str(chemin) + '.tmp', 'w', zipfile.ZIP_DEFLATED) as zout:
        for info, data in parties:
            if re.match(r'xl/worksheets/sheet[0-9]+\.xml$', info.filename):
                xml, k = motif.subn(r'<c r="\1"\2 t="str">\3<v></v></c>', data.decode('utf-8'))
                data, n = xml.encode('utf-8'), n + k
            zout.writestr(info, data)
    shutil.move(str(chemin) + '.tmp', str(chemin))
    return n


def injecter(chemin):
    out = subprocess.run([sys.executable, str(INJECT), str(chemin)], check=True, capture_output=True, text=True).stdout
    assert 'fallos_pycel=0' in out, out
    m = re.search(r'formulas=(\d+) cache_inyectado=(\d+)', out)
    vides = cache_texte_vide(chemin)
    assert int(m.group(1)) == int(m.group(2)) + vides, (out, vides)  # toute formule a un cache (valeur ou texte vide)
    return f'{out.strip()} cache_texte_vide={vides}'


def hm(h, m):
    return (h * 60 + m) / 1440


def gate_logique(p1, q1_ref, q1_rem):
    """Valeurs de test dans une COPIE temporaire : la sortie publiée reste vierge."""
    cas = []  # (feuille, ligne, {col: valeur}, attendu, description)
    E, R, M = 'Enceintes froides', 'Refroidissement rapide', 'Remise en température'
    cas += [(E, p1 + 0, {4: 2.5}, 'Oui', 'chambre froide 2,5 °C (limite +3)'),
            (E, p1 + 1, {4: 4.1}, 'NON', 'chambre froide 4,1 °C (limite +3)'),
            (E, p1 + 2, {6: -19}, 'Oui', 'congélateur −19 °C (limite −18)'),
            (E, p1 + 3, {6: -15}, 'NON', 'congélateur −15 °C (limite −18)'),
            (E, p1 + 4, {5: 4.0}, 'Oui', 'réfrigérateur 4,0 °C, pile à la limite +4'),
            (E, p1 + 5, {3: hm(8, 0), 4: 2.5, 5: 3.8, 6: -19}, 'Oui', 'trois enceintes dans les limites'),
            (E, p1 + 6, {3: hm(18, 0), 4: 2.5, 5: 4.5, 6: -19}, 'NON', 'une seule enceinte hors limite (réfrigérateur 4,5)'),
            (E, p1 + 7, {3: hm(9, 0), 8: 'texte seul', 9: 'MG'}, None, 'heure + action + visa, sans lecture → vide'),
            (E, p1 + 8, {}, None, 'ligne vide → vide'),
            (R, q1_ref + 0, {3: hm(12, 0), 4: 65, 5: hm(13, 40), 6: 9}, 'Oui', '1 h 40, de 65 °C à 9 °C, objectif 10'),
            (R, q1_ref + 1, {3: hm(12, 0), 4: 65, 5: hm(14, 10), 6: 9}, 'NON', '2 h 10, de 65 °C à 9 °C'),
            (R, q1_ref + 2, {3: hm(12, 0), 4: 65, 5: hm(14, 0), 6: 10}, 'Oui', '2 h 00 pile à 10 °C (bornes incluses)'),
            (R, q1_ref + 3, {3: hm(12, 0), 4: 65, 5: hm(13, 30), 6: 11}, 'NON', '1 h 30 mais 11 °C > objectif 10'),
            (R, q1_ref + 4, {3: hm(23, 30), 4: 70, 5: hm(1, 0), 6: 8}, 'Oui', '23:30 → 01:00 (minuit), 8 °C'),
            (R, q1_ref + 5, {2: 'Blanquette', 3: hm(12, 0), 4: 65}, None, 'sans heure ni T° de fin → vide'),
            (R, q1_ref + 6, {}, None, 'ligne vide → vide'),
            (M, q1_rem + 0, {3: hm(12, 0), 4: hm(12, 45), 5: 66}, 'Oui', '45 min, 66 °C à cœur'),
            (M, q1_rem + 1, {3: hm(12, 0), 4: hm(12, 50), 5: 61}, 'NON', '50 min, 61 °C à cœur'),
            (M, q1_rem + 2, {3: hm(12, 0), 4: hm(13, 0), 5: 63}, 'Oui', '1 h 00 pile à 63 °C (bornes incluses)'),
            (M, q1_rem + 3, {3: hm(12, 0), 4: hm(13, 5), 5: 70}, 'NON', '1 h 05 à 70 °C'),
            (M, q1_rem + 4, {}, None, 'ligne vide → vide')]
    col_conf = {E: 7, R: 8, M: 7}
    with tempfile.TemporaryDirectory() as tmp:
        copie = Path(tmp) / 'test.xlsx'
        shutil.copy(XLSX, copie)
        wb = load_workbook(copie)
        for f, lg, vals, _, _ in cas:
            for col, v in vals.items():
                wb[f].cell(row=lg, column=col, value=v)
        wb.save(copie)
        injecter(copie)
        wv = load_workbook(copie, data_only=True)
        res = []
        for f, lg, _, att, desc in cas:
            obt = wv[f].cell(row=lg, column=col_conf[f]).value
            obt = None if obt == '' else obt
            res.append((f, desc, att, obt))
        duree = wv[R].cell(row=q1_ref, column=7).value
    for f, desc, att, obt in res:
        print(f'  {"OK " if att == obt else "KO "} [{f}] {desc} → {obt!r} (attendu {att!r})')
    assert all(att == obt for _, _, att, obt in res), 'gate logique KO'
    minutes = duree.total_seconds() / 60 if hasattr(duree, 'total_seconds') else duree * 1440  # openpyxl lit [h]:mm en timedelta
    assert abs(minutes - 100) < 1e-6, duree
    return len(res)


def gate_publie(p1, q1_ref, q1_rem):
    wv = load_workbook(XLSX, data_only=True)
    assert wv.sheetnames == ['Enceintes froides', 'Refroidissement rapide', 'Remise en température'], wv.sheetnames
    ws = wv['Enceintes froides']
    entetes = [(ws.cell(row=13, column=c).value, ws.cell(row=14, column=c).value) for c in (4, 5, 6)]
    assert entetes == [(ENCEINTES[0][0], f'max +3{NB}°C'), (ENCEINTES[1][0], f'max +4{NB}°C'),
                       ('Congélateur', f'max -18{NB}°C')], entetes
    for r in range(p1, p1 + 62):
        for c in range(3, 10):
            assert ws.cell(row=r, column=c).value in (None, ''), (r, c, ws.cell(row=r, column=c).value)
    for nom, q1, cols in (('Refroidissement rapide', q1_ref, range(1, 11)), ('Remise en température', q1_rem, range(1, 10))):
        for r in range(q1, q1 + N_LIGNES):
            for c in cols:
                assert wv[nom].cell(row=r, column=c).value in (None, ''), (nom, r, c)
    assert wv['Refroidissement rapide']['F4'].value == OBJECTIF_REFROIDISSEMENT
    wf = load_workbook(XLSX)
    assert all(any(c.hyperlink and c.hyperlink.target == GUIDE for row in s.iter_rows() for c in row) for s in wf.worksheets)
    z = zipfile.ZipFile(XLSX)
    sel = [n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml$', n)
           and 'tabSelected="1"' in z.read(n).decode('utf-8')]
    assert sel == ['xl/worksheets/sheet1.xml'], sel
    assert '<dataValidation' in z.read('xl/worksheets/sheet1.xml').decode('utf-8')


def gate_pdf():
    warnings.filterwarnings('ignore')
    from pypdf import PdfReader
    rd = PdfReader(str(PDF))
    n = len(rd.pages)
    assert n in (1, 2), n
    texte = ' '.join(p.extract_text() for p in rd.pages).replace(NB, ' ')
    for attendu in ('+63 °C', 'é', 'cœur', 'Relevé des enceintes froides', 'aichef.pro/fr/blog/haccp',
                    '2023-756', '« en tous points du produit »'):
        assert attendu in texte, attendu
    assert '74' not in texte and '10 °C → 3' not in texte
    return n


def main():
    wb = Workbook()
    wb.remove(wb.active)
    p1 = feuille_enceintes(wb)
    q1_ref = feuille_refroidissement(wb)
    q1_rem = feuille_remise(wb)
    for i, ws in enumerate(wb.worksheets):
        ws.sheet_view.tabSelected = (i == 0)
    wb.active = 0
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.title = 'Relevé de températures HACCP'
    XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb.save(XLSX)
    print(injecter(XLSX))
    gate_publie(p1, q1_ref, q1_rem)
    n_cas = gate_logique(p1, q1_ref, q1_rem)
    pdf_imprimable()
    pages = gate_pdf()
    print(f'OK {XLSX.name} · 3 feuilles · 62 relevés + 2 × {N_LIGNES} lignes, vierges · gate logique {n_cas}/{n_cas} '
          f'· + {PDF.name} ({pages} pages)')


if __name__ == '__main__':
    main()
