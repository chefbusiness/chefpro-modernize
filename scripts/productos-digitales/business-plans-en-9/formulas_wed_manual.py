#!/usr/bin/env python3
"""
formulas_wed_manual.py — las fórmulas con texto de WEDP SIN gemela (SPEC D166; inv. §2.2). `derivar_formulas_wed.py`
las deja pendientes; aquí, EN escrita a mano con la redacción de la Pizza EN (`../business-plans-en-8/formulas_piz.json`),
las MISMAS referencias y la misma lógica que el ES (sesión Claude Code, 27-oct-2026, F2-EN paso 1a):

  C9    precio por invitado con impuesto: sin el 21 % ni el 10 % del menú (el venue no vende comida ni bebida).
  D28   imprevistos sobre las partidas de OBRA de las filas 7, 9, 10, 12, 13, 15, 16, 20, 21 y 22 (rótulos de D162).
  D38   lo que no se amortiza (filas 8, 23, 24, 25, 26, 27 y el fondo de maniobra), miles con «#,##0» (el ES usaba «0» y €).
  F13   coste directo del evento: sin el IVA soportado del 21 % ni la SGAE (limpieza, restrooms, generador, parking).
  F14   la comisión del caterer no tiene coste.
  A26   (Break-Even) la de la Pizza EN con invitados por evento y eventos al año; sin «carencia» (el caso no la tiene,
        pero la rama se conserva como en la pizza).
  O11   compras con su tipo (0 en EE. UU.) y los días de pago: la de la Pizza EN sin «food and beverage».
"""

MANUAL = {
    'WEDP|0. Supuestos|C9': (
        '=IFERROR("Revenue per guest excl. sales tax plus the weighted sales tax of your two sales lines ("&TEXT('
        'SUMPRODUCT(\'3-Year P&L\'!$E$10:$E$11,\'3-Year P&L\'!$G$10:$G$11)*100,"0")&"%), rounded. It is what the venue '
        'bills per guest (venue rental & services plus the caterer commission), not what the couple pays for the whole '
        'wedding: the caterer bills the menu and the bar, with its own sales tax, and they are not in this workbook. In '
        'the UK, prices to private clients include VAT.","")'),
    'WEDP|Inversión Inicial|D28': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$55,"0%")&" of the BUILD-OUT items of this block (architect, engineer '
        '& code consultant; barn renovation; fire sprinkler system; ADA-compliant restrooms; electrical service & '
        'lighting; HVAC; caterer\'s prep & warming kitchen; parking lot & driveway; landscaping; fire alarm, exit signs & '
        'accessible routes), not of the whole block: the other items are left out. Sprinklers on a tank and fire pump, a '
        'new septic system or a strict county can push these lines far above the example. No lender funds a build-out '
        'without a cushion: the percentage is in ""0. Assumptions""","")'),
    'WEDP|Inversión Inicial|D38': (
        '=IFERROR("Not depreciated, because they are not fixed assets: conditional use permit, studies and permit fees; '
        'website, photography, video & brand; LLC formation & attorney; launch; lease security deposit; rent during '
        'permitting and build-out, and the working capital reserve. They add up to "&TEXT(B31-B36-B37,"#,##0")&" of the '
        '"&TEXT(B31,"#,##0")&" total investment.","")'),
    'WEDP|PyG 3 Años|F13': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$13,"0%")&" of VENUE RENTAL & SERVICES sales, not of total sales: the '
        'caterer commission has its own line · Cleaning and turnover, restroom restocking, generator fuel, parking '
        'attendants and security for each event: check it against your invoices and the Pricing & Quote Calculator","")'),
    'WEDP|PyG 3 Años|F14': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$14,"0%")&" of CATERER COMMISSION sales: the commission has no cost '
        'for the venue","")'),
    'WEDP|Punto Equilibrio|A26': (
        '=IFERROR("With the revenue per guest excl. sales tax above, you need "&TEXT(ROUNDUP(B15,0),"0")&" guests per '
        'event over your "&TEXT(B11,"0")&" events a year to avoid losing money (accounting break-even, depreciation '
        'included), and "&TEXT(ROUNDUP(B20,0),"0")&" for cash to hold (cash break-even: depreciation out, because it is '
        'not paid, and the year\'s loan payment in"&IF(B12=0,"; no principal is repaid this year (interest-only period '
        'or no loan)","")&"). The ""Revenue needed per year"" rows show the same figures in your currency.","")'),
    'WEDP|Tesorería 12 meses|O11': (
        '=IFERROR("Direct event costs, consumables, commissions and contingencies, each at ITS tax rate (column G of the '
        'P&L; 0 in the US, where the sales tax you pay is part of the cost) and with the supplier payment days from '
        '""0. Assumptions""."&IF(\'0. Assumptions\'!$B$59=0,""," With "&TEXT(\'0. Assumptions\'!$B$59,"0")&" payment '
        'days, the last purchases of the year are paid next year: the ""Year"" column of this row holds "&TEXT(MAX(0,'
        '12-ROUNDUP(\'0. Assumptions\'!$B$59/30,0)),"0")&" months of purchases, not the year\'s cost."),"")'),
}
