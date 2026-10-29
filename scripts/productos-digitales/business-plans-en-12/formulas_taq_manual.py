#!/usr/bin/env python3
"""
formulas_taq_manual.py — las fórmulas con texto de TAQP SIN gemela (F1-camino §6): las 4 que la taquería ES escribe
distinto de la pizzería ES (medido el 29-oct en f5c5b269). `derivar_formulas_taq.py` las deja pendientes; aquí, EN escrita
a mano con la redacción de la Pizza EN (`../business-plans-en-8/formulas_piz_manual.py`), las MISMAS referencias y la
misma lógica que el ES (sesión Claude Code, 29-oct-2026, F2-EN). C9 y Break-Even!A28 casan con la Pizza EN (mismo ES).

  C50   rotaciones: incluye take-out y delivery (no ocupan mesa); sin la cifra del caso ES («57 comensales de sala»)
        para que no se quede vieja si se calibra B4 (en el caso US, ≈ 60 de 115 comen en sala: «about half»).
  D27   imprevistos sobre las partidas de OBRA del bloque (filas 7-11 = B35 de la amortización), rótulos de datos_taq.
  D37   lo que no se amortiza (filas 22, 23, 24, 25, 26 y 29); miles con «#,##0» (el ES usaba «0» y «€»).
  F13   nota del food cost: sin los tipos de IVA de los alimentos (4 %/10 %): el distribuidor y la calculadora.
Cada literal ≤ 255 caracteres (Excel): los largos van troceados con «"…"&"…"».
"""

MANUAL = {
    'TAQP|0. Supuestos|C50': (
        '=IFERROR("That is "&TEXT(INT(ROUND(B50,1)),"0")&"."&TEXT(ROUND(MOD(ROUND(B50,1),1)*10,0),"0")&" seat turns '
        'per day on the "&TEXT($B$51,"0")&" seats in the cell below. "&"It includes the take-out and delivery covers, '
        'which do not take a seat: the real turns of your dining room are lower (in the example, about half of the '
        'covers eat in). Compare it with the ceiling on seat turns typed in ""Break-Even"".","")'),
    'TAQP|Inversión Inicial|D27': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$55,"0%")&" of the BUILD-OUT items of this block (architect, MEP & '
        'hood drawings and permit fees; build-out, signage & facade; Type I hood, UL 300 fire suppression & makeup air; '
        '"&"electrical service, panel & gas lines; plumbing, grease interceptor & HVAC), not of the whole block: the '
        'trompos, the equipment and the other items are left out. No lender funds a build-out without a cushion: the '
        'percentage is in ""0. Assumptions""","")'),
    'TAQP|Inversión Inicial|D37': (
        '=IFERROR("Not depreciated, because they are not fixed assets: LLC, legal and food safety plan; branding, '
        'website, photos and launch; opening inventory; security deposit; pre-opening rent and the working capital '
        'reserve. They add up to "&TEXT(B30-B35-B36,"#,##0")&" of the "&TEXT(B30,"#,##0")&" total investment.","")'),
    'TAQP|PyG 3 Años|F13': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$13,"0%")&" of FOOD sales, not of total sales: beverages have their '
        'own line · pork shoulder and other meats, corn tortillas, chiles, produce, avocados and cheese: check it '
        'against your distributor invoices and the Taco Cost & Trompo Yield Calculator","")'),
}
