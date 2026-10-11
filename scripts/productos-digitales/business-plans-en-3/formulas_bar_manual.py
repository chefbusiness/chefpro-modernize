#!/usr/bin/env python3
"""
formulas_bar_manual.py — las 3 fórmulas con texto de BARP SIN gemela (SPEC D59; F1-inventario-delta §3.2).
`derivar_formulas_bar.py` las deja pendientes; aquí, EN escrita a mano con la redacción de
`../business-plans-en/formulas_en.py`, las MISMAS referencias y la misma lógica que el ES (sesión Claude Code,
11-oct-2026, F2 paso 1):

  C50   la de CAF/REST C50 sin la cifra del docx ES («1,8 servicios… 3,3 rotaciones»): compara con el techo de
        "Break-Even" (D59). Coma decimal construida a mano → punto, como la CAF.
  D27   imprevistos sobre las partidas de OBRA del bloque (filas 9, 10, 11, 12, 16, 20 y 21 = B35 de la amortización),
        descritas en minúscula con los rótulos de D54.
  D37   lo que no se amortiza (filas 7, 8, 22, 23, 25, 26 y 29), con la nota de D54 sobre la licencia comprada; miles
        con «#,##0» (el ES usaba «0» y «€»).
"""

MANUAL = {
    'BARP|0. Supuestos|C50': (
        '=IFERROR("That is "&TEXT(INT(ROUND(B50,1)),"0")&"."&TEXT(ROUND(MOD(ROUND(B50,1),1)*10,0),"0")&" seat turns '
        'per day on the "&TEXT($B$51,"0")&" seats in the cell below. Compare it with the ceiling on seat turns typed '
        'in ""Break-Even"" and with the turns your opening hours and your room really allow before you rely on either '
        'figure.","")'),
    'BARP|Inversión Inicial|D27': (
        '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$55,"0%")&" of the BUILD-OUT items of this block (architect and MEP '
        'drawings, build-out, electrical and HVAC, plumbing, grease interceptor and hood, draft beer system, decor and '
        'lighting, signage), not of the whole block: the other items are left out. No lender funds a build-out without '
        'a cushion: the percentage is in ""0. Assumptions""","")'),
    'BARP|Inversión Inicial|D37': (
        '=IFERROR("Not depreciated, because they are not fixed assets: LLC formation and legal, liquor license and local '
        'permits (a license bought from another owner is an intangible asset: ask your CPA), launch marketing, opening '
        'inventory, security deposit, pre-opening rent and the working capital reserve. They add up to "&TEXT('
        'B30-B35-B36,"#,##0")&" of the "&TEXT(B30,"#,##0")&" total investment.","")'),
}
