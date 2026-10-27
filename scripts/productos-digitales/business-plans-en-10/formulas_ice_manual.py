#!/usr/bin/env python3
"""
formulas_ice_manual.py — las fórmulas con texto de HELP SIN gemela (SPEC D197; inv. §2.1). `derivar_formulas_ice.py`
las deja pendientes; aquí, EN escrita a mano con la redacción de la Pizza EN (`../business-plans-en-8/
formulas_piz_manual.py`), las MISMAS referencias y la misma lógica que el ES (sesión Claude Code, 27-oct-2026, F2-EN
paso 1a). Cada literal de texto ≤ 255 caracteres (límite de Excel): los largos se trocean con «"…"&"…"».

  C9    el texto del precio con impuesto: ticket + sales tax medio ponderado de las líneas; sin el 10 % / art. 91 del
        IVA español; el pint envasado y la tarta entera pueden ir exentos en algunos estados (D195).
  D28   imprevistos sobre las partidas de OBRA del bloque (filas 7-11 = B36 de la amortización), rótulos de D193.
  D38   lo que no se amortiza (filas 22-27 y 30, D193); miles con «#,##0» (el ES usaba «0» y «€»).
  F13   food cost sobre las ventas de helado: base, aromas e inclusiones, conos, samples y merma; SIN afirmaciones de
        impuestos de compra (el ES citaba el IVA soportado al 4/10 %: en EE. UU. no hay crédito, B41 = 0).
"""

MANUAL = {
    'HELP|0. Supuestos|C9': (
        '=IFERROR("Average check excl. sales tax plus the weighted sales tax of your sales lines ("&TEXT(SUMPRODUCT('
        '\'3-Year P&L\'!$E$10:$E$11,\'3-Year P&L\'!$G$10:$G$11)*100,"0")&"%), rounded. In the US, menu prices usually '
        'exclude sales tax and it is added at the register. "&"The example uses one rate for scoops, pints, cakes and '
        'drinks; some states tax packaged pints and whole cakes as groceries: then use your blended rate. In the UK, '
        'menu prices include VAT.","")'),
    'HELP|Inversión Inicial|D28': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$55,"0%")&" of the BUILD-OUT items of this block (architect, MEP '
        'drawings, plan review & permit fees; build-out of production room & shop; electrical service & panel; '
        'plumbing, floor sinks, hand sinks, HVAC & condenser ventilation; "&"signage & storefront), not of the whole '
        'block: the equipment and the other items are left out. No lender funds a build-out without a cushion: the '
        'percentage is in ""0. Assumptions""","")'),
    'HELP|Inversión Inicial|D38': (
        '=IFERROR("Not depreciated, because they are not fixed assets: ice cream training course; branding, website, '
        'photos & launch; LLC, legal, permits & food safety plan; opening inventory; "&"security deposit; pre-opening '
        'rent and the working capital reserve. They add up to "&TEXT(B31-B36-B37,"#,##0")&" of the "&TEXT(B31,'
        '"#,##0")&" total investment.","")'),
    'HELP|PyG 3 Años|F13': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$13,"0%")&" of FOOD sales (the ice cream line), not of total sales: '
        'beverages have their own line · purchased base, flavorings, mix-ins and toppings, cones, "&"tasting samples and '
        'production waste: check it against your dairy and distributor invoices","")'),
}
