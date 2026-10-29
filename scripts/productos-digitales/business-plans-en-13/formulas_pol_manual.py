#!/usr/bin/env python3
"""
formulas_pol_manual.py — las fórmulas con texto de POLP SIN gemela (F1-camino §6): las 5 que la pollería ES escribe
distinto de la taquería ES (medido el 29-oct sobre 8c34fa09). `derivar_formulas_pol.py` las deja pendientes; aquí, el EN
del Taco EN (`../business-plans-en-12/formulas_taq.json` publicado), con las MISMAS referencias y la misma lógica que el ES
(sesión Claude Code, 29-oct-2026, F2-EN):

  C9    = Taco EN (el ES solo cambia «a domicilio» → «por plataforma»; el EN US no lo dice).
  D27   = Taco EN con las partidas de obra de datos_pol (la campana de ≈ 14 ft) y «the rotisseries» por «the trompos».
  D37   = Taco EN (el ES solo cambia el rótulo del stock; el EN dice «opening inventory»).
  F13   nota del food cost de la pollería (pollo, marinado, aceite, yuca y patatas, arroz y frijoles…) y la calculadora.
  A26   = Taco EN A28 (el ES dice «pedidos»; el caso US cuenta covers; la fila sube 2 por la rotación apagada).
Cada literal ≤ 255 caracteres (Excel): los largos van troceados con «"…"&"…"».
"""

MANUAL = {
    'POLP|0. Supuestos|C9': (
        '=IFERROR("Average check excl. sales tax plus the weighted sales tax of your sales lines ("&TEXT(SUMPRODUCT(\'3-Year P&L\'!$E$10:$E$11,\'3-Year P&L\'!$G$10:$G$11)*100,"0")&"%), rounded. In the US, menu prices usually exclude sales tax and it is added at the register; the beverage share in column H of the beverage line of the P&L only moves this average if your state taxes alcohol at another rate. "&"In the UK, menu prices include VAT.","")'),
    'POLP|Inversión Inicial|D27': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$55,"0%")&" of the BUILD-OUT items of this block (architect, MEP & hood drawings and permit fees; build-out, signage & facade; Type I hood (about 14 ft), UL 300 fire suppression & makeup air; "&"electrical service, panel & gas lines; plumbing, grease interceptor & HVAC), not of the whole block: the rotisseries, the equipment and the other items are left out. No lender funds a build-out without a cushion: the percentage is in ""0. Assumptions""","")'),
    'POLP|Inversión Inicial|D37': (
        '=IFERROR("Not depreciated, because they are not fixed assets: LLC, legal and food safety plan; branding, website, photos and launch; opening inventory; security deposit; pre-opening rent and the working capital reserve. They add up to "&TEXT(B30-B35-B36,"#,##0")&" of the "&TEXT(B30,"#,##0")&" total investment.","")'),
    'POLP|PyG 3 Años|F13': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$13,"0%")&" of FOOD sales, not of total sales: beverages have their own line · "&"whole chickens, marinade, cooking oil, frozen yuca and fries, rice, beans, produce and sauce ingredients: check it against your distributor invoices and the Rotisserie Chicken Yield & Costing Calculator","")'),
    'POLP|Punto Equilibrio|A26': (
        '=IFERROR("With the average check excl. sales tax above, you need "&TEXT(ROUNDUP(B15,0),"0")&" covers a day over your "&TEXT(B11,"0")&" opening days to avoid losing money (accounting break-even, depreciation included), and "&TEXT(ROUNDUP(B20,0),"0")&" for cash to hold (cash break-even: depreciation out, because it is not paid, and the year\'s loan payment in"&IF(B12=0,"; no principal is repaid this year (interest-only period or no loan)","")&"). The ""Revenue needed per year"" rows show the same figures in your currency.","")'),
}
