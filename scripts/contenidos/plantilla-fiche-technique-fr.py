#!/usr/bin/env python3
"""Fiche technique de cuisine VIERGE (FR), gratuite — lead magnet de /fr/blog/fiche-technique-cuisine.

LowFruits FR (nov-2026): «fiche technique cuisine vierge» 320, «… vierge pdf» 260, «… pdf gratuit» 140.
Sale:
  - astro-site/public/descargas/fiche-technique-cuisine-vierge-aichef.xlsx — 2 feuilles :
      «Exemple blanquette» (l'exemple chiffré du post, mêmes chiffres : 3,65 € → 20,6 %, coef ≈ 4,9)
      et «Fiche vierge» (mêmes formules, cellules vides).
  - astro-site/public/descargas/fiche-technique-cuisine-vierge-aichef.pdf — A4 vierge à imprimer.
L'xlsx passe par inject_cache.py (valeurs calculées) et un gate data_only sur les cellules.
Après : python3 scripts/productos-digitales/parche_xml_xlsx.py --check <xlsx>
`/descargas/*` est en noindex (netlify.toml).
"""
import subprocess
import sys
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

RAIZ = Path(__file__).resolve().parents[2]
XLSX = RAIZ / 'astro-site/public/descargas/fiche-technique-cuisine-vierge-aichef.xlsx'
PDF = RAIZ / 'astro-site/public/descargas/fiche-technique-cuisine-vierge-aichef.pdf'
GUIDE = 'https://aichef.pro/fr/blog/fiche-technique-cuisine'

NOIR, OR, GRIS = '111111', 'FFD700', 'F3F3F3'
fin = Side(style='thin', color='BBBBBB')
bord = Border(left=fin, right=fin, top=fin, bottom=fin)
saisie = PatternFill('solid', fgColor='FFF8D6')
EUR = '#,##0.00 "€"'

# (ingrédient, grammage net g, perte, prix d'achat HT €/kg, coût forfaitaire €) — les chiffres du post
BLANQUETTE = [
    ('Épaule de veau', 180, 0, 14.00, None),
    ('Carottes', 60, 0, 1.80, None),
    ('Oignons grelots', 40, 0, 3.50, None),
    ('Champignons de Paris', 50, 0, 6.00, None),
    ('Crème entière', 40, 0, 4.50, None),
    ('Beurre', 15, 0, 9.00, None),
    ('Farine', 10, 0, 1.20, None),
    ('Riz', 60, 0, 2.50, None),
    ('Bouquet garni et assaisonnement (forfait)', None, None, None, 0.10),
]
ETAPES = [
    ('Blanchir l\'épaule de veau détaillée en cubes, rafraîchir, puis mouiller à hauteur avec carotte et bouquet garni.', '10 min', 'départ à froid'),
    ('Cuire à frémissement jusqu\'à ce que la viande soit tendre, en écumant.', '1 h 30', 'frémissement'),
    ('Cuire les oignons grelots et les champignons à blanc à part.', '15 min', ''),
    ('Faire un roux blanc avec le beurre et la farine, mouiller avec le bouillon de cuisson passé, crémer.', '10 min', 'nappant'),
    ('Réunir viande, garniture et sauce ; cuire le riz à part et dresser.', '15 min', ''),
]
ALLERGENES = ['Céréales contenant du gluten', 'Crustacés', 'Œufs', 'Poissons', 'Arachides', 'Soja', 'Lait',
              'Fruits à coque', 'Céleri', 'Moutarde', 'Graines de sésame', 'Anhydride sulfureux et sulfites',
              'Lupin', 'Mollusques']
assert len(ALLERGENES) == 14
CONTIENT_BLANQUETTE = {'Céréales contenant du gluten', 'Lait'}


def titre(ws, ligne, texte, fin_col=7):
    c = ws.cell(row=ligne, column=1, value=texte)
    c.font = Font(bold=True, color='FFFFFF')
    c.fill = PatternFill('solid', fgColor=NOIR)
    ws.merge_cells(start_row=ligne, start_column=1, end_row=ligne, end_column=fin_col)


def cel(ws, ligne, col, valeur=None, fmt=None, entree=False, gras=False):
    c = ws.cell(row=ligne, column=col, value=valeur)
    c.border = bord
    if fmt:
        c.number_format = fmt
    if entree:
        c.fill = saisie
    if gras:
        c.font = Font(bold=True)
    c.alignment = Alignment(wrap_text=True, vertical='top')
    return c


def feuille(wb, nom, exemple):
    ws = wb.create_sheet(nom)
    ws['A1'] = 'Fiche technique de cuisine'
    ws['A1'].font = Font(bold=True, size=16, color=OR)
    ws['A1'].fill = PatternFill('solid', fgColor=NOIR)
    ws.merge_cells('A1:G1')
    ws['A2'] = 'Remplissez les cellules jaunes. Le grammage brut, le coût par portion et les ratios se calculent seuls.'
    ws['A2'].font = Font(italic=True, color='555555')
    ws.merge_cells('A2:G2')

    titre(ws, 4, 'Informations générales')
    infos = [('Plat', 'Blanquette de veau' if exemple else ''), ('Catégorie', 'Viandes' if exemple else ''),
             ('Nombre de portions', 1 if exemple else None), ('Temps total', 'Environ 2 h 20' if exemple else ''),
             ('Auteur', ''), ('Date et version', 'jj-mm-aaaa · v1.0')]
    for i, (k, v) in enumerate(infos):
        lg = 5 + i
        cel(ws, lg, 1, k, gras=True)
        cel(ws, lg, 2, v or None, entree=True)
        ws.merge_cells(start_row=lg, start_column=2, end_row=lg, end_column=7)

    titre(ws, 12, 'Ingrédients (pour une portion)')
    entetes = ['Ingrédient', 'Grammage net (g)', 'Perte (%)', 'Grammage brut (g)', "Prix d'achat HT (€/kg)", 'Coût portion (€)', 'Allergènes']
    for col, txt in enumerate(entetes, start=1):
        c = cel(ws, 13, col, txt, gras=True)
        c.fill = PatternFill('solid', fgColor=GRIS)
    premiere = 14
    lignes = (BLANQUETTE if exemple else []) + [None] * (4 if exemple else 14)
    for i, item in enumerate(lignes):
        lg = premiere + i
        if item:
            nom_i, net, perte, prix, forfait = item
            cel(ws, lg, 1, nom_i, entree=True)
            cel(ws, lg, 2, net, '0', entree=True)
            cel(ws, lg, 3, perte, '0%', entree=True)
            cel(ws, lg, 5, prix, EUR, entree=True)
            alg = {'Crème entière': 'Lait', 'Beurre': 'Lait', 'Farine': 'Gluten (blé)'}.get(nom_i, '')
            cel(ws, lg, 7, alg or None, entree=True)
        else:
            for col, fmt in ((1, None), (2, '0'), (3, '0%'), (5, EUR), (7, None)):
                cel(ws, lg, col, None, fmt, entree=True)
            forfait = None
        # brut = net / (1 − perte), arrondi au gramme supérieur
        cel(ws, lg, 4, f'=IF(OR(B{lg}="",N(C{lg})>=1),"",ROUNDUP(B{lg}/(1-N(C{lg})),0))', '0')
        if forfait is not None:
            cel(ws, lg, 6, forfait, EUR, entree=True)  # forfait saisi à la main
        else:
            cel(ws, lg, 6, f'=IF(OR(D{lg}="",E{lg}=""),"",ROUND(D{lg}/1000*E{lg},2))', EUR)
    derniere = premiere + len(lignes) - 1
    dvp = DataValidation(type='decimal', operator='between', formula1='0', formula2='0.99',
                         error='La perte va de 0 % à 99 %.', errorTitle='Perte')
    ws.add_data_validation(dvp)
    dvp.add(f'C{premiere}:C{derniere}')

    fp = derniere + 2
    titre(ws, fp, 'Progression')
    for col, txt in ((1, 'Étape'), (2, 'Ce qui se fait'), (6, 'Temps'), (7, 'Température / point')):
        c = cel(ws, fp + 1, col, txt, gras=True)
        c.fill = PatternFill('solid', fgColor=GRIS)
    ws.merge_cells(start_row=fp + 1, start_column=2, end_row=fp + 1, end_column=5)
    etapes = (ETAPES if exemple else []) + [('', '', '')] * (2 if exemple else 8)
    for i, (txt, temps, temp) in enumerate(etapes):
        lg = fp + 2 + i
        cel(ws, lg, 1, i + 1)
        cel(ws, lg, 2, txt or None, entree=True)
        ws.merge_cells(start_row=lg, start_column=2, end_row=lg, end_column=5)
        cel(ws, lg, 6, temps or None, entree=True)
        cel(ws, lg, 7, temp or None, entree=True)
        ws.row_dimensions[lg].height = 42

    fa = fp + 2 + len(etapes) + 1
    titre(ws, fa, 'Allergènes (règlement INCO, UE 1169/2011)')
    dv = DataValidation(type='list', formula1='"Contient,Peut contenir des traces,Ne contient pas"', allow_blank=True)
    ws.add_data_validation(dv)
    for i, a in enumerate(ALLERGENES):
        lg = fa + 1 + i
        cel(ws, lg, 1, a)
        v = ('Contient' if a in CONTIENT_BLANQUETTE else 'Ne contient pas') if exemple else None
        c = cel(ws, lg, 2, v, entree=True)
        dv.add(c.coordinate)
    if exemple:
        ws.cell(row=fa + 1 + ALLERGENES.index('Céleri'), column=3,
                value='À vérifier si votre bouquet garni contient du céleri.').font = Font(italic=True, color='555555')

    fc = fa + 1 + len(ALLERGENES) + 1
    titre(ws, fc, 'Conservation et HACCP')
    for i, (k, v) in enumerate([('Conservation', 'Refroidir rapidement, filmer, étiqueter et conserver au froid positif.' if exemple else ''),
                                ('Points critiques (selon votre PMS)', 'Refroidissement après cuisson ; remise en température.' if exemple else ''),
                                ('Durée de vie', 'Celle fixée par votre plan de maîtrise sanitaire.' if exemple else '')]):
        lg = fc + 1 + i
        cel(ws, lg, 1, k, gras=True)
        cel(ws, lg, 2, v or None, entree=True)
        ws.merge_cells(start_row=lg, start_column=2, end_row=lg, end_column=7)
    fd = fc + 5
    titre(ws, fd, 'Dressage')
    for i, (k, v) in enumerate([('Montage', 'Riz en dôme, blanquette nappée à côté, champignons et oignons sur le dessus.' if exemple else ''),
                                ('Vaisselle', 'Assiette creuse.' if exemple else ''), ('Photo de référence', 'Collez ici la photo du plat dressé.')]):
        lg = fd + 1 + i
        cel(ws, lg, 1, k, gras=True)
        cel(ws, lg, 2, v or None, entree=True)
        ws.merge_cells(start_row=lg, start_column=2, end_row=lg, end_column=7)

    fx = fd + 5
    titre(ws, fx, 'Coût et prix')
    b = fx + 1
    bloc = [
        ('Coût matière par portion', f'=SUM(F{premiere}:F{derniere})', EUR, False),
        ('Prix carte TTC', 19.50 if exemple else None, EUR, True),
        ('TVA (restauration sur place en France : 10 %)', 0.10, '0%', True),
        ('Prix de vente HT', f'=IF(B{b + 1}="","",B{b + 1}/(1+B{b + 2}))', EUR, False),
        ('Ratio matière (coût ÷ prix HT)', f'=IF(OR(B{b + 3}="",B{b}=0),"",B{b}/B{b + 3})', '0.0%', False),
        ('Coefficient multiplicateur (prix HT ÷ coût)', f'=IF(OR(B{b + 3}="",B{b}=0),"",B{b + 3}/B{b})', '0.00', False),
    ]
    for i, (k, v, fmt, ent) in enumerate(bloc):
        cel(ws, b + i, 1, k, gras=True)
        c = cel(ws, b + i, 2, v, fmt, entree=ent, gras=True)
        if not ent:
            c.fill = PatternFill('solid', fgColor=GRIS)
    fn = b + len(bloc) + 1
    ws.cell(row=fn, column=1, value='Guide avec l\'exemple expliqué :')
    ws.cell(row=fn, column=2, value=GUIDE).hyperlink = GUIDE
    ws.cell(row=fn, column=2).font = Font(color='0563C1', underline='single')
    ws.cell(row=fn + 1, column=1, value='Le ratio matière se calcule sur le prix HORS TAXES, jamais sur le TTC.').font = Font(italic=True, color='555555')

    for col, w in {'A': 34, 'B': 13, 'C': 10, 'D': 13, 'E': 16, 'F': 14, 'G': 20}.items():
        ws.column_dimensions[col].width = w
    ws.sheet_view.showGridLines = False
    return premiere, b


def pdf_vierge():
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    st = getSampleStyleSheet()
    h = st['Heading2']; h.textColor = colors.HexColor('#111111'); h.spaceBefore = 4; h.spaceAfter = 3; h.fontSize = 12; h.leading = 14
    doc = SimpleDocTemplate(str(PDF), pagesize=A4, leftMargin=14 * mm, rightMargin=14 * mm, topMargin=12 * mm, bottomMargin=12 * mm,
                            title='Fiche technique de cuisine vierge', author='AI Chef Pro')
    grille = TableStyle([('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#999999')),
                         ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#F3F3F3')),
                         ('FONTSIZE', (0, 0), (-1, -1), 8), ('VALIGN', (0, 0), (-1, -1), 'TOP')])
    W = A4[0] - 28 * mm
    el = []
    bandeau = Table([['Fiche technique de cuisine']], colWidths=[W])
    bandeau.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#111111')),
                                 ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#FFD700')),
                                 ('FONTSIZE', (0, 0), (-1, -1), 16), ('BOTTOMPADDING', (0, 0), (-1, -1), 8)]))
    el += [bandeau, Spacer(1, 4)]
    info = Table([['Plat', '', 'Catégorie', ''], ['Nombre de portions', '', 'Temps total', ''], ['Auteur', '', 'Date et version', '']],
                 colWidths=[W * 0.18, W * 0.32, W * 0.18, W * 0.32], rowHeights=16)
    info.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#999999')), ('FONTSIZE', (0, 0), (-1, -1), 8)]))
    el += [info, Paragraph('Ingrédients (pour une portion)', h)]
    ing = Table([['Ingrédient', 'Net (g)', 'Perte (%)', 'Brut (g)', 'Prix HT (€/kg)', 'Coût (€)', 'Allergènes']] + [[''] * 7 for _ in range(11)],
                colWidths=[W * x for x in (0.27, 0.09, 0.09, 0.09, 0.13, 0.1, 0.23)], rowHeights=15)
    ing.setStyle(grille)
    el += [ing, Paragraph('Progression', h)]
    prog = Table([['Étape', 'Ce qui se fait', 'Temps', 'Température / point']] + [[str(i), '', '', ''] for i in range(1, 7)],
                 colWidths=[W * 0.08, W * 0.6, W * 0.12, W * 0.2], rowHeights=[15] + [20] * 6)
    prog.setStyle(grille)
    el += [prog, Paragraph('Allergènes (INCO, UE 1169/2011)', h), Paragraph('C = contient · T = peut contenir des traces · N = ne contient pas', st['Italic']), Spacer(1, 4)]
    paires = [ALLERGENES[i:i + 2] for i in range(0, 14, 2)]
    alg = Table([[a, 'C  T  N', b_, 'C  T  N'] for a, b_ in paires], colWidths=[W * 0.35, W * 0.15, W * 0.35, W * 0.15], rowHeights=13)
    alg.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#999999')), ('FONTSIZE', (0, 0), (-1, -1), 8)]))
    el += [alg, Paragraph('Conservation, HACCP et dressage', h)]
    cons = Table([['Conservation', ''], ['Points critiques (PMS)', ''], ['Dressage et vaisselle', '']], colWidths=[W * 0.25, W * 0.75], rowHeights=18)
    cons.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#999999')), ('FONTSIZE', (0, 0), (-1, -1), 8)]))
    el += [cons, Paragraph('Coût et prix', h)]
    cout = Table([['Coût matière par portion', '', 'Prix carte TTC', ''], ['Prix de vente HT (TTC ÷ 1,10)', '', 'Ratio matière (coût ÷ HT)', ''],
                  ['Coefficient (HT ÷ coût)', '', '', '']], colWidths=[W * 0.3, W * 0.2, W * 0.3, W * 0.2], rowHeights=16)
    cout.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#999999')), ('FONTSIZE', (0, 0), (-1, -1), 8)]))
    el += [cout, Spacer(1, 4), Paragraph('Modèle gratuit AI Chef Pro · Guide et exemple chiffré : aichef.pro/fr/blog/fiche-technique-cuisine', st['Italic'])]
    doc.build(el)


def main():
    wb = Workbook()
    wb.remove(wb.active)
    p_ex, b_ex = feuille(wb, 'Exemple blanquette', True)
    feuille(wb, 'Fiche vierge', False)
    XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb.save(XLSX)
    subprocess.run([sys.executable, str(RAIZ / 'scripts/productos-digitales/inject_cache.py'), str(XLSX)],
                   check=True, stdout=subprocess.DEVNULL)
    wv = load_workbook(XLSX, data_only=True)['Exemple blanquette']
    couts = [round(float(wv.cell(row=p_ex + i, column=6).value), 2) for i in range(9)]
    assert couts == [2.52, 0.11, 0.14, 0.30, 0.18, 0.14, 0.01, 0.15, 0.10], couts
    total = round(float(wv.cell(row=b_ex, column=2).value), 2)
    ht = round(float(wv.cell(row=b_ex + 3, column=2).value), 2)
    ratio = round(float(wv.cell(row=b_ex + 4, column=2).value) * 100, 1)
    coef = round(float(wv.cell(row=b_ex + 5, column=2).value), 1)
    assert (total, ht, ratio, coef) == (3.65, 17.73, 20.6, 4.9), (total, ht, ratio, coef)
    pdf_vierge()
    print(f'OK {XLSX.name} · coûts {couts} · total {total} · HT {ht} · ratio {ratio} % · coef {coef} · + {PDF.name}')


if __name__ == '__main__':
    main()
