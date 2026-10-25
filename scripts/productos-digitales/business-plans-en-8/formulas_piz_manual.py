#!/usr/bin/env python3
"""
formulas_piz_manual.py — las fórmulas con texto de PIZP SIN gemela (SPEC D143; inv. §2.1). `derivar_formulas_piz.py`
las deja pendientes; aquí, EN escrita a mano con la redacción del Bar EN (`../business-plans-en-3/formulas_bar.json`),
las MISMAS referencias y la misma lógica que el ES (sesión Claude Code, 25-oct-2026, F2-EN paso 1a):

  C9    el texto del precio con impuesto: la del Bar EN + la columna H de la línea de bebida (E5) en vez del 10/21 %.
  C50   rotaciones: incluye take-out y delivery (no ocupan mesa); sin la cifra del caso ES («51 comensales de sala»)
        para que no se quede vieja si se calibra B4.
  D27   imprevistos sobre las partidas de OBRA del bloque (filas 7-11 = B35 de la amortización), rótulos de D139.
  D37   lo que no se amortiza (filas 22, 23, 24, 25, 26 y 29); miles con «#,##0» (el ES usaba «0» y «€»).
  F13   nota del food cost: sin los tipos de IVA de los alimentos (4 %/10 %): el distribuidor y la calculadora.
  A28   (Break-Even) la del Bar EN tal cual: el ES solo cambia «cubiertos» → «comensales» y el EN ya dice «covers».
"""

MANUAL = {
    'PIZP|0. Supuestos|C9': (
        '=IFERROR("Average check excl. sales tax plus the weighted sales tax of your sales lines ("&TEXT(SUMPRODUCT('
        '\'3-Year P&L\'!$E$10:$E$11,\'3-Year P&L\'!$G$10:$G$11)*100,"0")&"%), rounded. In the US, menu prices usually '
        'exclude sales tax and it is added at the register; the beverage share in column H of the beverage line of the '
        'P&L only moves this average if your state taxes alcohol at another rate. In the UK, menu prices include '
        'VAT.","")'),
    'PIZP|0. Supuestos|C50': (
        '=IFERROR("That is "&TEXT(INT(ROUND(B50,1)),"0")&"."&TEXT(ROUND(MOD(ROUND(B50,1),1)*10,0),"0")&" seat turns '
        'per day on the "&TEXT($B$51,"0")&" seats in the cell below. It includes the take-out and delivery covers, '
        'which do not take a table: the real turns of your dining room are lower (in the example, about three quarters '
        'of the covers eat in). Compare it with the ceiling on seat turns typed in ""Break-Even"".","")'),
    'PIZP|Inversión Inicial|D27': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$55,"0%")&" of the BUILD-OUT items of this block (architect, MEP, hood '
        '& flue drawings and permit fees; build-out, signage & facade; flue/chimney, spark arrestor & hearth pad; '
        'electrical service & panel; plumbing, grease interceptor, HVAC & makeup air), not of the whole block: the '
        'oven, the equipment and the other items are left out. No lender funds a build-out without a cushion: the '
        'percentage is in ""0. Assumptions""","")'),
    'PIZP|Inversión Inicial|D37': (
        '=IFERROR("Not depreciated, because they are not fixed assets: LLC, legal and food safety plan; branding, '
        'website, training and launch; opening inventory; security deposit; pre-opening rent and the working capital '
        'reserve. They add up to "&TEXT(B30-B35-B36,"#,##0")&" of the "&TEXT(B30,"#,##0")&" total investment.","")'),
    'PIZP|PyG 3 Años|F13': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$13,"0%")&" of FOOD sales, not of total sales: beverages have their '
        'own line · 00 flour, cheeses (fior di latte, mozzarella di bufala), San Marzano tomatoes, cured meats and '
        'olive oil: check it against your distributor invoices and the Pizza Dough & Food Cost Calculator","")'),
    'PIZP|Punto Equilibrio|A28': (
        '=IFERROR("With the average check excl. sales tax above, you need "&TEXT(ROUNDUP(B15,0),"0")&" covers a day '
        'over your "&TEXT(B11,"0")&" opening days to avoid losing money (accounting break-even, depreciation included), '
        'and "&TEXT(ROUNDUP(B20,0),"0")&" for cash to hold (cash break-even: depreciation out, because it is not paid, '
        'and the year\'s loan payment in"&IF(B12=0,"; no principal is repaid this year (interest-only period or no '
        'loan)","")&"). The ""Revenue needed per year"" rows show the same figures in your currency.","")'),
}
