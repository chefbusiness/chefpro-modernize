#!/usr/bin/env python3
"""
formulas_rp_manual.py — las 9 fórmulas con texto de RESTP/PANP SIN gemela exacta en FT/CAF (derivar_formulas.py las
deja pendientes). EN escrita a mano con la redacción de `../business-plans-en/formulas_en.py`, las MISMAS
referencias y la misma lógica que el ES (sesión Claude Code, 4-oct-2026, F2 tanda 1). Notas por celda:

  RESTP C50   la del CAF C50 sin la cifra del docx ES («1,8 rotaciones»: el Word EN se reescribe con tokens).
  RESTP D13   lista de partidas de obra del bloque del restaurante (A8-A10), en minúscula como FT/CAF.
  RESTP D55   partidas que no se amortizan del restaurante (A7, A11, A12, A37-A39, A41, A42, A44, A45, A47).
  RESTP A29   la de FT A26 con «covers» y las referencias del restaurante (una fila más abajo).
  PANP  C9    la de FT C9 + la parte exenta de la línea de pan (col. H, E3) que baja la media.
  PANP  D28   partidas de obra del obrador (A9-A12, A23).
  PANP  D38   la de CAF D42 con las referencias de la panadería.
  PANP  F13   la de FT F13; la 2.ª frase ES (harinas al 4 %, soportado ponderado) ya no aplica con E2 (G13 = B41 = 0).
  PANP  A26   la de FT A26 con «transactions» (mismas referencias que FT).
"""

MANUAL = {
    'RESTP|0. Supuestos|C50': (
        '=IFERROR("That is "&TEXT(INT(ROUND(B50,1)),"0")&"."&TEXT(ROUND(MOD(ROUND(B50,1),1)*10,0),"0")&" seat turns '
        'per day on the "&TEXT($B$51,"0")&" seats in the cell below. Compare this daily average with your real meal '
        'periods and with the table turns you can sustain at peak before you rely on it.","")'),
    'RESTP|1. Inversión Inicial|D13': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$55,"0%")&" of the BUILD-OUT items of this block (build-out, '
        'architect and permit drawings, interior design), not of the whole block: the other items are left out. No '
        'lender funds a build-out without a cushion: the percentage is in ""0. Assumptions""","")'),
    'RESTP|1. Inversión Inicial|D55': (
        '=IFERROR("Not depreciated, because they are not fixed assets: broker and lease review fees, security deposit, '
        'pre-opening rent, brand design, website and Google Business Profile, grand opening campaign, entity formation '
        'and legal, liquor license and permits, opening food and bar inventory and the working capital reserve. They '
        'add up to "&TEXT(B48-B53-B54,"#,##0")&" of the "&TEXT(B48,"#,##0")&" total investment.","")'),
    'RESTP|3. Punto Equilibrio|A29': (
        '=IFERROR("With the average check excl. sales tax above, you need "&TEXT(ROUNDUP(B16,0),"0")&" covers a day '
        'over your "&TEXT(B12,"0")&" opening days to avoid losing money (accounting break-even, depreciation '
        'included), and "&TEXT(ROUNDUP(B21,0),"0")&" for cash to hold (cash break-even: depreciation out, because it '
        'is not paid, and the year\'s loan payment in"&IF(B13=0,"; no principal is repaid this year (interest-only '
        'period or no loan)","")&"). The ""Revenue needed per year"" rows show the same figures in your currency.","")'),
    'PANP|0. Supuestos|C9': (
        '=IFERROR("Average check excl. sales tax plus the weighted sales tax of your sales lines ("&TEXT(SUMPRODUCT('
        '\'3-Year P&L\'!$E$10:$E$11,\'3-Year P&L\'!$G$10:$G$11)*100,"0")&"%), rounded: the tax-exempt share of the '
        'bakery line (column H of ""3-Year P&L"") lowers it. In the US, prices usually exclude sales tax and it is '
        'added at the register; in the UK, prices include VAT.","")'),
    'PANP|Inversión Inicial|D28': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$55,"0%")&" of the BUILD-OUT items of this block (architect and '
        'building permits, construction, electrical service upgrade for the ovens, oven ventilation and exhaust, '
        'signage), not of the whole block: the other items are left out. No lender funds a build-out without a '
        'cushion: the percentage is in ""0. Assumptions""","")'),
    'PANP|Inversión Inicial|D38': (
        '=IFERROR("Not depreciated, because they are not fixed assets: entity formation and legal, licenses and health '
        'plan review, launch marketing, opening inventory, security deposit, pre-opening rent and the working capital '
        'reserve. They add up to "&TEXT(B31-B36-B37,"#,##0")&" of the "&TEXT(B31,"#,##0")&" total investment.","")'),
    'PANP|PyG 3 Años|F13': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$13,"0%")&" of FOOD sales, not of total sales: beverages have their '
        'own line · In the US the sales tax you pay on ingredients is a cost, not a credit, so column G of this row is '
        '0","")'),
    'PANP|Punto Equilibrio|A26': (
        '=IFERROR("With the average check excl. sales tax above, you need "&TEXT(ROUNDUP(B15,0),"0")&" transactions a '
        'day over your "&TEXT(B11,"0")&" opening days to avoid losing money (accounting break-even, depreciation '
        'included), and "&TEXT(ROUNDUP(B20,0),"0")&" for cash to hold (cash break-even: depreciation out, because it '
        'is not paid, and the year\'s loan payment in"&IF(B12=0,"; no principal is repaid this year (interest-only '
        'period or no loan)","")&"). The ""Revenue needed per year"" rows show the same figures in your currency.","")'),
}
