#!/usr/bin/env python3
"""
formulas_bur_manual.py — las fórmulas con texto de BURP SIN gemela (F1-camino §6): las 4 que la hamburguesería ES escribe
distinto del sushi bar ES (medido el 31-oct sobre 17117feb: C50, D27, D37 y F13). `derivar_formulas_bur.py` las deja
pendientes; aquí, el EN del Sushi EN (`../business-plans-en-14/formulas_sus_manual.py`) con las MISMAS referencias y la
misma lógica que el ES (sesión Claude Code, 31-oct-2026, F2-EN):

  C50   rotaciones: incluye take-out y delivery (1 order = 1.6 covers, F1-camino §6; el ES dice 1,7), que no ocupan mesa;
        sin la cifra del caso ES («1,5 por plaza») para que no se quede vieja si se calibra B4 (en el caso US, ≈ 107 de 195
        comen en sala).
  D27   imprevistos sobre las partidas de OBRA del bloque (filas 7-11 = B35 de la amortización), con los rótulos de
        datos_bur.FIJOS_NUEVOS.
  D37   lo que no se amortiza (filas 22, 23, 24, 25, 26 y 29; miles con «#,##0», = Sushi EN).
  F13   nota del food cost de la hamburguesería (carne, buns, queso, fries, aceite…) sin los tipos de IVA y con la
        calculadora del kit.
Cada literal ≤ 255 caracteres (Excel): los largos van troceados con «"…"&"…"».
"""

MANUAL = {
    'BURP|0. Supuestos|C50': (
        '=IFERROR("That is "&TEXT(INT(ROUND(B50,1)),"0")&"."&TEXT(ROUND(MOD(ROUND(B50,1),1)*10,0),"0")&" seat turns '
        'per day on the "&TEXT($B$51,"0")&" seats in the cell below. "&"It includes the take-out and delivery covers (1 '
        'order = 1.6 covers), which do not take a seat: the real turns of your dining room are lower (in the example, '
        'a little over half of the covers eat in). Compare it with the ceiling on seat turns typed in ""Break-Even"".","")'),
    'BURP|Inversión Inicial|D27': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$55,"0%")&" of the BUILD-OUT items of this block (architect, MEP & '
        'hood drawings, plan review & permit fees; build-out with order counter, signage & facade; hood exhaust duct to '
        'the roof & makeup air; "&"electrical service, panel & HVAC; plumbing, gas lines & grease interceptor), not of '
        'the whole block: the flat-tops, the fryers, the hood, the refrigeration and the other items are left out. '
        '"&"No lender funds a build-out without a cushion: the percentage is in ""0. Assumptions""","")'),
    'BURP|Inversión Inicial|D37': (
        '=IFERROR("Not depreciated, because they are not fixed assets: LLC, legal, licenses, food safety plan & '
        'pre-opening training; branding, website, photos & launch video; opening inventory; security deposit; '
        'pre-opening rent and the working capital "&"reserve. They add up to "&TEXT(B30-B35-B36,"#,##0")&" of the "'
        '&TEXT(B30,"#,##0")&" total investment.","")'),
    'BURP|PyG 3 Años|F13': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$13,"0%")&" of FOOD sales, not of total sales: beverages have their '
        'own line · "&"ground beef, potato buns, American cheese, fries, frying oil, chicken, bacon, produce and sauces: '
        'check it against your distributor invoices and the Smash Burger Patty, Fries & Costing Calculator","")'),
}
