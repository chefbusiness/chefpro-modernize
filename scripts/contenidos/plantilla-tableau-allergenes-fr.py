#!/usr/bin/env python3
"""Tableau des allergènes VIERGE (FR) pour restaurant, gratuit — lead magnet de /fr/blog/tableau-des-allergenes.

LowFruits FR (nov-2026) : «tableau allergène restaurant» 210, «les 14 allergènes» 170, «fiche allergène restaurant» 50,
«tableau des allergènes pdf» 30. Le post promet (section « Tableau des allergènes vierge gratuit ») un Excel de 30 lignes,
les 14 allergènes en colonnes, une liste déroulante C/T/N dans chaque case, l'exemple des cinq plats et le nombre
d'allergènes calculé seul ; et un PDF A4 paysage d'une seule page, à remplir à la main.
Sale :
  - astro-site/public/descargas/tableau-allergenes-restaurant-vierge-aichef.xlsx — 2 feuilles :
      «Tableau vierge» (active, 30 lignes vides) et «Exemple» (les 5 plats fictifs du post, mêmes détails).
  - astro-site/public/descargas/tableau-allergenes-restaurant-vierge-aichef.pdf — A4 paysage, 1 page, à imprimer.
Pourquoi les en-têtes d'allergènes sont tournés à 90° : plat + 14 allergènes + détail doivent tenir sur la largeur
d'une A4 paysage ; à l'horizontale, « Anhydride sulfureux et sulfites » imposerait des colonnes de 30 caractères. La
hauteur de la ligne d'en-tête laisse le nom le plus long sur UNE ligne (aucune dépendance au retour à la ligne du
texte tourné, que tous les tableurs ne gèrent pas pareil) ; le retour à la ligne reste activé en secours.
Les noms sont ceux de l'annexe II du règlement INCO (UE 1169/2011), identiques à la liste ALLERGENES de
plantilla-fiche-technique-fr.py, pour que la fiche technique et le tableau se répondent.
L'xlsx passe par inject_cache.py (valeurs calculées) et un gate data_only ; le PDF par un gate pypdf (1 page, accents).
Après : python3 scripts/productos-digitales/parche_xml_xlsx.py --check <xlsx>
`/descargas/*` est en noindex (netlify.toml).
"""
import datetime
import subprocess
import sys
import warnings
import zipfile
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

RAIZ = Path(__file__).resolve().parents[2]
XLSX = RAIZ / 'astro-site/public/descargas/tableau-allergenes-restaurant-vierge-aichef.xlsx'
PDF = RAIZ / 'astro-site/public/descargas/tableau-allergenes-restaurant-vierge-aichef.pdf'
GUIDE = 'https://aichef.pro/fr/blog/tableau-des-allergenes'
TITRE = 'Tableau des allergènes — restaurant'

NOIR, OR, GRIS = '111111', 'FFD700', 'F3F3F3'
fin = Side(style='thin', color='BBBBBB')
bord = Border(left=fin, right=fin, top=fin, bottom=fin)
saisie = PatternFill('solid', fgColor='FFF8D6')
noir = PatternFill('solid', fgColor=NOIR)

ALLERGENES = ['Céréales contenant du gluten', 'Crustacés', 'Œufs', 'Poissons', 'Arachides', 'Soja', 'Lait',
              'Fruits à coque', 'Céleri', 'Moutarde', 'Graines de sésame', 'Anhydride sulfureux et sulfites',
              'Lupin', 'Mollusques']
# En-têtes courts du PDF, même ordre ; « <br/> » = retour à la ligne dans la cellule.
COURTS = ['Gluten', 'Crustacés', 'Œufs', 'Poissons', 'Arachides', 'Soja', 'Lait', 'Fruits à<br/>coque', 'Céleri',
          'Moutarde', 'Sésame', 'Sulfites', 'Lupin', 'Mollusques']
assert len(ALLERGENES) == len(COURTS) == 14

GLUTEN, SULFITES = 'Céréales contenant du gluten', 'Anhydride sulfureux et sulfites'
# (plat, allergènes « C », détail) — le tableau d'exemple du post, mot pour mot ; tout le reste vaut « N ».
EXEMPLE = [
    ('Velouté de champignons', {GLUTEN, 'Lait', 'Céleri'}, 'Gluten (liaison), lait (crème), céleri (bouillon)'),
    ('Tartare de bœuf', {'Œufs', 'Moutarde', GLUTEN}, 'Œufs (jaune), moutarde (condiment), gluten (toasts)'),
    ('Risotto aux gambas', {'Crustacés', 'Lait', SULFITES}, 'Crustacés, lait (beurre et parmesan), sulfites (vin blanc)'),
    ('Magret, sauce au poivre', {'Lait', SULFITES}, 'Lait (crème), sulfites (cognac et fond déglacé au vin)'),
    ('Tarte aux noix', {GLUTEN, 'Fruits à coque', 'Œufs', 'Lait'}, 'Gluten (pâte), fruits à coque (noix), œufs, lait (beurre)'),
]
RECOMPTES = [3, 3, 3, 2, 4]
assert all(a <= set(ALLERGENES) for _, a, _ in EXEMPLE) and [len(a) for _, a, _ in EXEMPLE] == RECOMPTES

LEGENDE = 'C = contient · T = peut contenir des traces · N = ne contient pas'
DECRET = ("En restaurant, l'information sur les allergènes doit être disponible par écrit, de façon lisible et visible, "
          "ou un affichage écrit doit indiquer où la consulter librement (décret n° 2015-447).")
NOTES = [
    "Remplissez chaque ligne à partir de la fiche technique du plat, jamais de mémoire : base, sauce, garniture, "
    "produits achetés prêts à l'emploi, huile de friture.",
    "« T » (traces) est facultatif : à n'utiliser qu'en dernier recours, après avoir évalué un vrai risque de "
    "contamination croisée.",
    DECRET,
    "Mettez le tableau à jour à chaque changement de recette, de carte ou de fournisseur.",
]
CONSIGNE = ('Remplissez les cellules jaunes : une ligne par plat, une lettre par allergène (liste déroulante). '
            "Le nombre d'allergènes se calcule seul.")
AVERTISSEMENT_EXEMPLE = ("Exemple fictif et illustratif : les cinq plats du guide. Les allergènes de vos plats dépendent "
                         "de vos recettes et de vos fournisseurs : remplissez votre tableau à partir de vos fiches techniques.")

# Disposition (colonnes 1-based) : A plat · B-O les 14 allergènes · P détail · Q nombre d'allergènes « C ».
C_PLAT, C_PREM_ALG, C_DERN_ALG, C_DETAIL, C_NB = 1, 2, 15, 16, 17
L_CHAMPS1, L_CHAMPS2, L_LEGENDE, L_GROUPE, L_ENTETE, PREMIERE = 4, 5, 7, 8, 9, 10
NB_LIGNES = 30


def bloc(ws, ligne, c1, c2, valeur=None, entree=False, gras=False, fmt=None, align=None):
    """Cellule (fusionnée de c1 à c2) bordée ; à la fusion, openpyxl recopie la bordure sur le pourtour."""
    c = ws.cell(row=ligne, column=c1, value=valeur)
    c.border = bord
    if entree:
        c.fill = saisie
    if gras:
        c.font = Font(bold=True, size=10)
    if fmt:
        c.number_format = fmt
    c.alignment = align or Alignment(vertical='center', wrap_text=True)
    if c2 > c1:
        ws.merge_cells(start_row=ligne, start_column=c1, end_row=ligne, end_column=c2)
    return c


def feuille(wb, nom, exemple):
    ws = wb.create_sheet(nom)
    lignes = EXEMPLE if exemple else [None] * NB_LIGNES
    derniere = PREMIERE + len(lignes) - 1

    ws['A1'] = TITRE
    ws['A1'].font = Font(bold=True, size=16, color=OR)
    ws['A1'].fill = noir
    ws['A1'].alignment = Alignment(vertical='center')
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=C_NB)
    ws.row_dimensions[1].height = 30
    ws['A2'] = AVERTISSEMENT_EXEMPLE if exemple else CONSIGNE
    ws['A2'].font = Font(italic=True, bold=exemple, color='555555')
    ws['A2'].alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=C_NB)
    ws.row_dimensions[2].height = 30 if exemple else 16  # l'avertissement de l'exemple tient sur deux lignes
    ws.row_dimensions[3].height = 6

    champs = [(L_CHAMPS1, 'Établissement', 'Restaurant fictif (exemple du guide)', None,
               'Carte / période', "Carte d'automne"),
              (L_CHAMPS2, 'Mis à jour le', 'jj/mm/aaaa (à chaque changement de carte)', None,
               'Validé par (chef ou responsable)', 'Le chef de cuisine')]
    for lg, k1, v1, fmt1, k2, v2 in champs:
        bloc(ws, lg, 1, 1, k1, gras=True)
        bloc(ws, lg, 2, 8, v1 if exemple else None, entree=True, fmt=fmt1,
             align=Alignment(horizontal='left', vertical='center'))
        bloc(ws, lg, 9, 14, k2, gras=True)
        bloc(ws, lg, 15, C_NB, v2 if exemple else None, entree=True)
        ws.row_dimensions[lg].height = 20
    ws.row_dimensions[6].height = 6

    ws.cell(row=L_LEGENDE, column=1, value=LEGENDE).font = Font(bold=True, size=10)
    ws.merge_cells(start_row=L_LEGENDE, start_column=1, end_row=L_LEGENDE, end_column=C_NB)
    ws.row_dimensions[L_LEGENDE].height = 18

    for col in range(1, C_NB + 1):
        ws.cell(row=L_GROUPE, column=col).fill = noir
    g = ws.cell(row=L_GROUPE, column=C_PREM_ALG, value='Les 14 allergènes — annexe II du règlement INCO (UE 1169/2011)')
    g.font = Font(bold=True, size=9, color='FFFFFF')
    g.alignment = Alignment(horizontal='center', vertical='center')
    ws.merge_cells(start_row=L_GROUPE, start_column=C_PREM_ALG, end_row=L_GROUPE, end_column=C_DERN_ALG)

    gris = PatternFill('solid', fgColor=GRIS)
    entetes = {C_PLAT: 'Plat (et ses composants : sauce, garniture, condiments)',
               C_DETAIL: "Détail (d'où vient l'allergène)", C_NB: "Nb d'allergènes (C)"}
    for col in range(1, C_NB + 1):
        c = ws.cell(row=L_ENTETE, column=col)
        c.border = bord
        c.fill = gris
        if C_PREM_ALG <= col <= C_DERN_ALG:
            c.value = ALLERGENES[col - C_PREM_ALG]
            c.font = Font(bold=True, size=9)
            # 90° = de bas en haut ; la ligne fait 126 pt : « Anhydride sulfureux et sulfites » (~116 pt en
            # Calibri gras 9) y tient sur une ligne ; wrap_text en secours pour les polices plus larges.
            c.alignment = Alignment(text_rotation=90, horizontal='center', vertical='bottom', wrap_text=True)
        else:
            c.value = entetes[col]
            c.font = Font(bold=True, size=10)
            c.alignment = Alignment(horizontal='left' if col != C_NB else 'center', vertical='bottom', wrap_text=True)
    ws.row_dimensions[L_ENTETE].height = 126

    centre = Alignment(horizontal='center', vertical='center')
    for i, item in enumerate(lignes):
        lg = PREMIERE + i
        plat, contient, detail = item if item else (None, set(), None)
        bloc(ws, lg, C_PLAT, C_PLAT, plat, entree=True)
        for col in range(C_PREM_ALG, C_DERN_ALG + 1):
            v = ('C' if ALLERGENES[col - C_PREM_ALG] in contient else 'N') if item else None
            bloc(ws, lg, col, col, v, entree=True, align=centre)
        bloc(ws, lg, C_DETAIL, C_DETAIL, detail, entree=True)
        nb = bloc(ws, lg, C_NB, C_NB, f'=IF(A{lg}="","",COUNTIF(B{lg}:O{lg},"C"))', fmt='0', align=centre)
        nb.fill = gris
        nb.font = Font(bold=True)
        ws.row_dimensions[lg].height = 30 if exemple else 22

    zone = f'B{PREMIERE}:O{derniere}'
    dv = DataValidation(type='list', formula1='"C,T,N"', allow_blank=True, showErrorMessage=True,
                        errorTitle='Allergènes',
                        error='Saisissez C (contient), T (peut contenir des traces) ou N (ne contient pas).')
    ws.add_data_validation(dv)
    dv.add(zone)
    # Lecture d'un coup d'œil : C en rouge, T en orangé, N en gris (la cellule vide garde le jaune de saisie).
    ws.conditional_formatting.add(zone, CellIsRule(operator='equal', formula=['"C"'], font=Font(bold=True, color='9C1C1C'),
                                                   fill=PatternFill('solid', fgColor='F8D7DA', bgColor='F8D7DA')))
    ws.conditional_formatting.add(zone, CellIsRule(operator='equal', formula=['"T"'], font=Font(bold=True, color='8A5300'),
                                                   fill=PatternFill('solid', fgColor='FFE3B3', bgColor='FFE3B3')))
    ws.conditional_formatting.add(zone, CellIsRule(operator='equal', formula=['"N"'], font=Font(color='8A8A8A')))

    fn = derniere + 2
    for i, note in enumerate(NOTES):
        c = ws.cell(row=fn + i, column=1, value=note)
        c.font = Font(italic=True, color='555555', size=10)
        c.alignment = Alignment(wrap_text=True, vertical='top')
        ws.merge_cells(start_row=fn + i, start_column=1, end_row=fn + i, end_column=C_NB)
        ws.row_dimensions[fn + i].height = 27 if len(note) > 140 else 15
    fl = fn + len(NOTES)
    ws.cell(row=fl, column=1, value="Guide complet avec l'exemple expliqué :").font = Font(size=10)
    lien = ws.cell(row=fl, column=2, value=GUIDE)
    lien.hyperlink = GUIDE
    lien.font = Font(color='0563C1', underline='single', size=10)
    ws.merge_cells(start_row=fl, start_column=2, end_row=fl, end_column=C_NB)

    ws.column_dimensions['A'].width = 46
    for col in range(C_PREM_ALG, C_DERN_ALG + 1):
        ws.column_dimensions[get_column_letter(col)].width = 5
    ws.column_dimensions['P'].width = 46
    ws.column_dimensions['Q'].width = 12
    ws.freeze_panes = f'B{PREMIERE}'
    ws.sheet_view.showGridLines = False
    ws.print_title_rows = f'{L_GROUPE}:{L_ENTETE}'
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins.left = ws.page_margins.right = 0.4
    return ws, derniere


def pdf_vierge():
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    # Helvetica (police standard, encodage WinAnsi) : Œ, é, è, ç, « », ·, — et ° y sont, et le texte s'extrait tel quel.
    page = landscape(A4)
    mx, my = 12 * mm, 9 * mm
    doc = SimpleDocTemplate(str(PDF), pagesize=page, leftMargin=mx, rightMargin=mx, topMargin=my, bottomMargin=my,
                            title=TITRE, author='AI Chef Pro', subject='Modèle vierge à imprimer et à remplir à la main')
    W = page[0] - 2 * mx
    trait = colors.HexColor('#999999')
    s_lab = ParagraphStyle('lab', fontName='Helvetica-Bold', fontSize=8.5, leading=10)
    # splitLongWords=0 : sinon reportlab coupe « Mollusques » en « Mollusqu / es » dans une colonne étroite.
    s_ent = ParagraphStyle('ent', fontName='Helvetica-Bold', fontSize=7, leading=8.5, alignment=TA_CENTER, splitLongWords=0)
    s_plat = ParagraphStyle('plat', fontName='Helvetica-Bold', fontSize=8.5, leading=10)
    s_leg = ParagraphStyle('leg', fontName='Helvetica', fontSize=9, leading=11)
    s_note = ParagraphStyle('note', fontName='Helvetica', fontSize=7.5, leading=9.5)
    s_pied = ParagraphStyle('pied', fontName='Helvetica-Oblique', fontSize=8, leading=10, textColor=colors.HexColor('#555555'))

    el = []
    bandeau = Table([[TITRE]], colWidths=[W])
    bandeau.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#' + NOIR)),
                                 ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#' + OR)),
                                 ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                                 ('FONTSIZE', (0, 0), (-1, -1), 16), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                 ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 10)]))
    el += [bandeau, Spacer(1, 5)]

    champs = Table([[Paragraph('Établissement', s_lab), '', Paragraph('Mis à jour le', s_lab), '',
                     Paragraph('Validé par (chef ou responsable)', s_lab), '']],
                   colWidths=[W * x for x in (0.10, 0.30, 0.10, 0.12, 0.22, 0.16)], rowHeights=20)
    champs.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, trait), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                *[('BACKGROUND', (c, 0), (c, 0), colors.HexColor('#' + GRIS)) for c in (0, 2, 4)]]))
    el += [champs, Spacer(1, 5)]
    el += [Paragraph('<b>C</b> = contient · <b>T</b> = peut contenir des traces · <b>N</b> = ne contient pas', s_leg),
           Spacer(1, 3)]

    col_alg = 41  # « Mollusques » en gras 7 pt = 38,5 pt + 2 pt de marge
    col_plat = W - 14 * col_alg
    entete = [Paragraph('Plat <font name="Helvetica" size="6.5">(et ses composants : sauce, garniture, condiments)</font>',
                        s_plat)] + [Paragraph(c, s_ent) for c in COURTS]
    nb_lignes, haut_ligne = 18, 22  # 7,8 mm : de quoi écrire à la main
    matrice = Table([entete] + [[''] * 15 for _ in range(nb_lignes)], colWidths=[col_plat] + [col_alg] * 14,
                    rowHeights=[26] + [haut_ligne] * nb_lignes, repeatRows=1)
    matrice.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, trait),
                                 ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor('#' + NOIR)),
                                 ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#' + GRIS)),
                                 ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#FAFAFA')]),
                                 ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
                                 ('LEFTPADDING', (1, 0), (-1, 0), 1), ('RIGHTPADDING', (1, 0), (-1, 0), 1)]))
    el += [matrice, Spacer(1, 5)]
    el += [Paragraph("Les 14 allergènes de l'annexe II du règlement INCO (UE 1169/2011) · Gluten = céréales contenant "
                     "du gluten · Sésame = graines de sésame · Sulfites = anhydride sulfureux et sulfites.", s_note),
           Paragraph(DECRET, s_note), Spacer(1, 4),
           Paragraph('Modèle gratuit AI Chef Pro · guide : aichef.pro/fr/blog/tableau-des-allergenes', s_pied)]
    doc.build(el)


def gate_xlsx():
    with zipfile.ZipFile(XLSX) as z:
        vues = [z.read(f'xl/worksheets/sheet{i}.xml').decode('utf-8').count('tabSelected="1"') for i in (1, 2)]
    assert vues == [1, 0], f'tabSelected : {vues}'
    wf = load_workbook(XLSX)
    assert wf.sheetnames == ['Tableau vierge', 'Exemple'] and wf.active.title == 'Tableau vierge', wf.sheetnames
    for ws, n in ((wf['Tableau vierge'], NB_LIGNES), (wf['Exemple'], len(EXEMPLE))):
        derniere = PREMIERE + n - 1
        assert [ws.cell(row=L_ENTETE, column=c).value for c in range(C_PREM_ALG, C_DERN_ALG + 1)] == ALLERGENES
        assert all(ws.cell(row=L_ENTETE, column=c).alignment.text_rotation == 90 for c in range(C_PREM_ALG, C_DERN_ALG + 1))
        assert ws.freeze_panes == f'B{PREMIERE}', ws.freeze_panes
        dvs = ws.data_validations.dataValidation
        assert len(dvs) == 1 and dvs[0].formula1 == '"C,T,N"' and dvs[0].showErrorMessage, dvs
        assert str(dvs[0].sqref) == f'B{PREMIERE}:O{derniere}', dvs[0].sqref
        for r in range(PREMIERE, derniere + 1):
            assert ws.cell(row=r, column=C_NB).value == f'=IF(A{r}="","",COUNTIF(B{r}:O{r},"C"))'
        assert ws.cell(row=derniere + 1, column=C_NB).value is None
    wv = load_workbook(XLSX, data_only=True)
    ex = wv['Exemple']
    recomptes = [ex.cell(row=PREMIERE + i, column=C_NB).value for i in range(len(EXEMPLE))]
    assert all(isinstance(v, (int, float)) for v in recomptes), recomptes
    recomptes = [int(v) for v in recomptes]
    assert recomptes == RECOMPTES, recomptes
    for i in range(len(EXEMPLE)):
        lettres = [ex.cell(row=PREMIERE + i, column=c).value for c in range(C_PREM_ALG, C_DERN_ALG + 1)]
        assert sum(v is not None for v in lettres) == 14 and set(lettres) <= {'C', 'N'}, lettres
        assert lettres.count('C') == recomptes[i]
    vg = wv['Tableau vierge']
    for r in range(PREMIERE, PREMIERE + NB_LIGNES):
        assert all(vg.cell(row=r, column=c).value is None for c in range(1, C_DETAIL + 1)), r
        assert vg.cell(row=r, column=C_NB).value in (None, ''), r
    return recomptes


def gate_pdf():
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        from pypdf import PdfReader
        lecteur = PdfReader(str(PDF))
        pages = len(lecteur.pages)
        assert pages == 1, f'{pages} pages'
        p = lecteur.pages[0]
        assert float(p.mediabox.width) > float(p.mediabox.height), 'pas en paysage'
        texte = p.extract_text()
    manquants = [m for m in ('Œufs', 'Céleri', 'Fruits à', 'Crustacés', 'Mollusques', 'Arachides',
                             'Validé par (chef ou responsable)', 'allergènes', 'façon', 'décret n° 2015-447',
                             TITRE, 'aichef.pro/fr/blog/tableau-des-allergenes') if m not in texte]
    assert not manquants, manquants
    return pages


def main():
    wb = Workbook()
    wb.remove(wb.active)
    vierge, _ = feuille(wb, 'Tableau vierge', False)
    exemple, _ = feuille(wb, 'Exemple', True)
    vierge.sheet_view.tabSelected = True
    exemple.sheet_view.tabSelected = False
    wb.active = 0
    XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb.save(XLSX)
    subprocess.run([sys.executable, str(RAIZ / 'scripts/productos-digitales/inject_cache.py'), str(XLSX)],
                   check=True, stdout=subprocess.DEVNULL)
    recomptes = gate_xlsx()
    pdf_vierge()
    pages = gate_pdf()
    print(f'OK {XLSX.name} · vierge {NB_LIGNES} lignes × 14 allergènes (A-Q) · exemple recomptes {recomptes} '
          f'· {PDF.name} {pages} page')


if __name__ == '__main__':
    main()
