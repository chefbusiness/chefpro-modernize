#!/usr/bin/env python3
"""
formulas_en.py — fórmulas con literales de texto de los 2 planes financieros, ya en EN (SPEC D7, D8, D11).

Las importa `mapas.py` en `mapas.FORMULAS_EN`: (corto, hoja ES, celda) → fórmula EN FINAL (pestañas EN, literales
EN, comillas dobles rectas para citar pestañas y filas, sin «€»: D8). Son 16 celdas en FTP y 17 en CAFP (censo:
`formulas_texto`). Las referencias de celda y la lógica numérica son las del ES; lo único que cambia es el texto
(y, en C50 de la CAF, la coma decimal que el ES construía a mano → punto; en D33/D42 el formato de miles «#,##0»).
Las listas de partidas de D23/D32 y D33/D42 se describen en minúscula, sin calcar los rótulos de las filas (que
escriben los traductores): así no se desincronizan.
"""
from collections import OrderedDict

S = "'0. Assumptions'!"                 # 0. Supuestos
P = "'3-Year P&L'!"                     # PyG 3 Años

_COMUNES = OrderedDict([
    ('0. Supuestos', OrderedDict([
        ('C9', '=IFERROR("Average check excl. sales tax plus the weighted sales tax of your sales lines ("&TEXT('
               'SUMPRODUCT(' + P + '$E$10:$E$11,' + P + '$G$10:$G$11)*100,"0")&"%), rounded. In the US, menu prices '
               'usually exclude sales tax and it is added at the register; in the UK, menu prices include VAT.","")'),
    ])),
    ('PyG 3 Años', OrderedDict([
        ('F13', '=IFERROR("At "&TEXT(' + S + '$B$13,"0%")&" of FOOD sales, not of total sales: beverages have their '
                'own line","")'),
        ('F14', '=IFERROR("At "&TEXT(' + S + '$B$14,"0%")&" of BEVERAGE sales","")'),
        ('F18', '=IFERROR("At "&TEXT(' + S + '$B$28,"0%")&" of sales. It is a VARIABLE cost: it moves with revenue, '
                'so it cannot sit in fixed costs","")'),
    ])),
    ('Personal', OrderedDict([
        ('A2', '=IFERROR("Payroll — "&TEXT(' + S + '$B$21,"0")&" pay periods + employer taxes "&TEXT(' + S +
               '$B$20*100,"0")&"%","")'),
    ])),
    ('Tesorería 12 meses', OrderedDict([
        ('O11', '=IFERROR("Food and beverage purchases, consumables, fees and contingencies, each at ITS tax rate '
                '(column G of the P&L; 0 in the US, where the sales tax you pay is part of the cost) and with the '
                'supplier payment days from ""0. Assumptions""."&IF(' + S + '$B$59=0,""," With "&TEXT(' + S +
                '$B$59,"0")&" payment days, the last purchases of the year are paid next year: the ""Year"" column '
                'of this row holds "&TEXT(MAX(0,12-ROUNDUP(' + S + '$B$59/30,0)),"0")&" months of purchases, not the '
                'year\'s cost."),"")'),
    ])),
])


def _inversion(c_dep, c_rent, c_cont, c_wc, c_pct, c_tax, c_d1, c_d2, c_nd, fila_wc, fila_tot, fila_b1, fila_b2,
               lista_obra, lista_nd):
    return OrderedDict([
        (c_dep, '=IFERROR(""&TEXT(' + S + '$B$25,"0")&IF(' + S + '$B$25=1," month"," months")&" of rent, from '
                '""0. Assumptions"". Refundable when the lease ends: it is not depreciated and carries no tax","")'),
        (c_rent, '=IFERROR("Rent "&IF(' + S + '$B$54=1,"for the month","for the "&TEXT(' + S + '$B$54,"0")&" '
                 'months")&" of build-out and permits before opening. It does not overlap the P&L, which starts on '
                 'opening day: its twelve months are twelve trading months","")'),
        (c_cont, '=IFERROR("At "&TEXT(' + S + '$B$55,"0%")&" of the BUILD-OUT items of this block (' + lista_obra +
                 '), not of the whole block: the other items are left out. No lender funds a build-out without a '
                 'cushion: the percentage is in ""0. Assumptions""","")'),
        (c_wc, '=IFERROR("Covers "&TEXT(' + S + '$B$35,"0")&IF(' + S + '$B$35=1," month"," months")&" of year-1 '
               'CASH fixed costs (the P&L fixed costs minus depreciation, which is not paid out), the minimum the '
               'Instructions of this workbook ask for","")'),
        (c_pct, '=IFERROR("The percentages in column C are read on this figure, which includes the working capital ("'
                '&TEXT(C%d,"0%%")&" of the total). To compare the breakdown with another plan, use the CAPEX row '
                'below.","")' % fila_wc),
        (c_tax, '=IFERROR("At "&TEXT(' + S + '$B$41,"0%")&" on the items marked ""Yes"" in the tax column. US: the '
                'sales tax you pay on equipment is part of its cost and is not recovered, so this rate is 0. UK '
                '(VAT-registered): 20%, reclaimed on your VAT return, but you pay it first, so the loan has to cover '
                'it","")'),
        (c_d1, '=IFERROR("Depreciated over "&TEXT(' + S + '$B$44,"0")&" years","")'),
        (c_d2, '=IFERROR("Depreciated over "&TEXT(' + S + '$B$45,"0")&" years","")'),
        (c_nd, '=IFERROR("Not depreciated, because they are not fixed assets: ' + lista_nd + '. They add up to "&TEXT('
               'B%d-B%d-B%d,"#,##0")&" of the "&TEXT(B%d,"#,##0")&" total investment.","")'
               % (fila_tot, fila_b1, fila_b2, fila_tot)),
    ])


_PE = ('=IFERROR("With the average check excl. sales tax above, you need "&TEXT(ROUNDUP(B15,0),"0")&" customers a day '
       'over your "&TEXT(B11,"0")&" opening days to avoid losing money (accounting break-even, depreciation '
       'included), and "&TEXT(ROUNDUP(B20,0),"0")&" for cash to hold (cash break-even: depreciation out, because it '
       'is not paid, and the year\'s loan payment in"&IF(B12=0,"; no principal is repaid this year (interest-only '
       'period or no loan)","")&"). The ""Revenue needed per year"" rows show the same figures in your '
       'currency.","")')

FORMULAS_EN = OrderedDict()
for _corto in ('FTP', 'CAFP'):
    for _h, _d in _COMUNES.items():
        for _c, _f in _d.items():
            FORMULAS_EN[(_corto, _h, _c)] = _f
FORMULAS_EN[('FTP', 'Punto Equilibrio', 'A26')] = _PE
FORMULAS_EN[('CAFP', 'Punto Equilibrio', 'A28')] = _PE
for _c, _f in _inversion('D21', 'D22', 'D23', 'D25', 'D26', 'D28', 'D31', 'D32', 'D33', 24, 26, 31, 32,
                         'used truck, build-out and wrap, propane and fire suppression, water tanks and handwashing '
                         'sinks, plan review and drawings',
                         'entity formation and legal, first-year permits, opening inventory, launch marketing, '
                         'security deposit, pre-opening rent and the working capital reserve').items():
    FORMULAS_EN[('FTP', 'Inversión Inicial', _c)] = _f
for _c, _f in _inversion('D30', 'D31', 'D32', 'D34', 'D35', 'D37', 'D40', 'D41', 'D42', 33, 35, 40, 41,
                         'architect and building permits, construction, electrical and HVAC, plumbing, decor and '
                         'lighting, signage',
                         'entity formation and legal, licenses and health plan review, launch marketing, opening '
                         'inventory, security deposit, pre-opening rent and the working capital reserve').items():
    FORMULAS_EN[('CAFP', 'Inversión Inicial', _c)] = _f
FORMULAS_EN[('CAFP', '0. Supuestos', 'C50')] = (
    '=IFERROR("That is "&TEXT(INT(ROUND(B50,1)),"0")&"."&TEXT(ROUND(MOD(ROUND(B50,1),1)*10,0),"0")&" seat turns per '
    'day on the "&TEXT($B$51,"0")&" seats in the cell below. This workbook assumes 2-3 table turns at weekend '
    'brunch: compare this average with your real opening hours before you rely on it.","")')
