#!/usr/bin/env python3
"""
formulas_sus_manual.py — las fórmulas con texto de SUSP SIN gemela (F1-camino §6): las 4 que el sushi bar ES escribe
distinto de la taquería ES (medido el 31-oct sobre 51060183: C50, D27, D37 y F13, las mismas 4 que la taquería frente a la
pizzería). `derivar_formulas_sus.py` las deja pendientes; aquí, el EN del Taco EN (`../business-plans-en-12/
formulas_taq_manual.py`), con las MISMAS referencias y la misma lógica que el ES (sesión Claude Code, 31-oct-2026, F2-EN):

  C50   rotaciones: incluye take-out y delivery (1 order = 1.6 covers, = ES), que no ocupan mesa; sin la cifra del caso ES
        («1,25 por plaza») para que no se quede vieja si se calibra B4 (en el caso US, ≈ 70 de 115 comen en sala).
  D27   imprevistos sobre las partidas de OBRA del bloque (filas 7-11 = B35 de la amortización), rótulos de datos_sus
        (el hood de ≈ 10 ft) y «the sushi case, the rice cookers, the equipment…» fuera.
  D37   = Taco EN (lo que no se amortiza: filas 22, 23, 24, 25, 26 y 29; miles con «#,##0»).
  F13   nota del food cost del sushi (pescado, arroz, nori, imitation crab, aguacate…) sin los tipos de IVA y con la
        calculadora del kit.
Cada literal ≤ 255 caracteres (Excel): los largos van troceados con «"…"&"…"».
"""

MANUAL = {
    'SUSP|0. Supuestos|C50': (
        '=IFERROR("That is "&TEXT(INT(ROUND(B50,1)),"0")&"."&TEXT(ROUND(MOD(ROUND(B50,1),1)*10,0),"0")&" seat turns '
        'per day on the "&TEXT($B$51,"0")&" seats in the cell below. "&"It includes the take-out and delivery covers (1 '
        'order = 1.6 covers), which do not take a seat: the real turns of your dining room are lower (in the example, '
        'about six in ten covers eat in). Compare it with the ceiling on seat turns typed in ""Break-Even"".","")'),
    'SUSP|Inversión Inicial|D27': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$55,"0%")&" of the BUILD-OUT items of this block (architect, MEP & '
        'hood drawings and permit fees; build-out with the sushi bar counter, signage & facade; Type I hood (about 10 '
        'ft), UL 300 fire suppression & makeup air; "&"electrical service & panel; plumbing, grease interceptor, HVAC & '
        'gas lines), not of the whole block: the sushi case, the rice cookers, the equipment and the other items are '
        'left out. "&"No lender funds a build-out without a cushion: the percentage is in ""0. Assumptions""","")'),
    'SUSP|Inversión Inicial|D37': (
        '=IFERROR("Not depreciated, because they are not fixed assets: LLC, legal and food safety plan; branding, '
        'website, photos and launch; opening inventory; security deposit; pre-opening rent and the working capital '
        'reserve. They add up to "&TEXT(B30-B35-B36,"#,##0")&" of the "&TEXT(B30,"#,##0")&" total investment.","")'),
    'SUSP|PyG 3 Años|F13': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$13,"0%")&" of FOOD sales, not of total sales: beverages have their '
        'own line · "&"fish and seafood, sushi rice, nori, imitation crab, avocado, produce, sauces and tempura '
        'ingredients: check it against your distributor invoices and the Sushi Fish, Rice & Costing Calculator","")'),
}
