#!/usr/bin/env python3
"""
tanda2_wed.py — Wedding Venue Business Plan Kit (EN) · completa las entradas de la TANDA 2 (Word, `tandas/wed_a` ‖
`tandas/wed_b`) que escribe `bp9.py preparar_tandas` con lo que el común no pone: el valor FINAL de cada token
(`cifras_caso.json`, del `aplicar_en` real: solo para entender el caso; en el texto se escribe el token), las cifras
del resto del kit (calculadora y contratos), las decisiones de orquestador del 27-oct y el comando de verificación.
Solo JSON (Mac). Sesión Claude Code, 27-oct-2026 (F2-EN, paso 3). Correr SIEMPRE después de `preparar_tandas`.

    python3 bp9.py preparar_tandas && python3 bp9.py tanda2
"""
import json
import os
import sys
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
REL = 'scripts/productos-digitales/business-plans-en-9'

KIT = OrderedDict([
    ('calculadora (wedding-venue-pricing-calculator.xlsx)',
     'Couple / Corporate; Wedding $8,000 · Corporate event $3,500 · Private celebration $4,000 · Micro wedding / '
     'elopement $2,000 (Saturday, shoulder season); Peak +15% / Shoulder 0 / Off-peak −20% (May, June, September, '
     'October = peak; April, July, August, November = shoulder; December-March = off-peak); Saturday 0 · Friday or Sunday '
     '−15% · Weekday −30%; guest minimum 100 / 75 / 50; extras: ceremony on site $750, additional hour $500, premium '
     'decor & lighting $800, rehearsal $400; caterer commission 10% (assumption); payments Couple 25% / 35% at 180 days / '
     '40% at 30 days, Corporate 30 / 30 at 60 / 40 at 15; cancellation tiers 10/25/50/75/100% (couples) and '
     '5/15/35/60/100% (corporate) at 12/6/3/1/0 months, «a reasonable estimate of the venue\'s loss, not a penalty» with a '
     'rebooking credit. Example: a peak Saturday wedding for 130 guests = $9,200 venue rental fee, $11,750 with extras.'),
    ('contratos (wedding-venue-rental-agreement-templates.docx)',
     'Model 1 · Venue Rental Agreement (Couples & Private Events) + Corporate & Organization Addendum + Model 2 · '
     'Exclusive Caterer Agreement; cabecera «Template, not legal advice»; retainer aplicado al precio; 2A Contingent '
     'booking before permits; rebooking credit; Cooling-Off Rule solo como «ask your attorney whether…»; 12 páginas.'),
    ('checklist (wedding-venue-startup-checklist.xlsx)',
     '84 tareas en 6 fases: Phase 1 - Business Setup · Phase 2 - Zoning & Permits · Phase 3 - Build-Out & Equipment · '
     'Phase 4 - Staff & Caterer · Phase 5 - Brand & Bookings · Phase 6 - Season & Events.'),
])
REGLAS = [
    'Cada cifra del caso, con su token {{…}} (valores abajo SOLO para entender el caso): nada de escribir «$612,000»; sí '
    '{{ventas_a1}}. Cifras de mercado solo con fuente leída; lo «(resumen)» de research como «typical range, get local '
    'quotes» o «ask…» (decisión de orquestador 4: sin The Knot, NY A20-51S, Missouri, §1671, 40 CFR 141.2, Wisconsin).',
    'Arrendamiento (decisión de orquestador 1): lease cuya duración CONTANDO LAS PRÓRROGAS sea al menos la del préstamo '
    '(«SBA lenders typically require…; confirm with your lender»), purchase option o right of first refusal, '
    'consentimiento del propietario a la obra y a usar el lease como garantía, TI allowance, lease contingent on CUP '
    'approval; comprar con SBA 504 = variante razonada sin Excel.',
    'FTC Cooling-Off Rule (decisión de orquestador 2): NUNCA afirmar que aplica; única forma: «If you sign couples at '
    'bridal shows or off-site, ask your attorney whether the FTC Cooling-Off Rule or your state\'s home-solicitation law '
    'applies; many venues give a short cancellation window for show-floor signings anyway.»',
    'El Word dice la verdad: año 1 = {{dias}} eventos (≈ 35 bodas), neto {{margen_neto_a1}}; ninguna fecha firme sin CUP '
    'y certificate of occupancy; no prometer que un permiso basta, licencia de alcohol del venue ni «non-refundable» sin '
    'la tabla. Lo que el Word promete, el Excel, la calculadora o los contratos lo hacen.',
    'Jerga research §9 (guests · revenue per guest · events per year · venue rental fee / site fee · exclusive caterer · '
    'caterer commission · retainer · seasonal W-2); «venue» en prosa; cero rastro de pizza, panadería, España o «finca». '
    'Unidades: sq ft con m² entre paréntesis.',
]


def main():
    cif = json.load(open(os.path.join(AQUI, 'cifras_caso.json'), encoding='utf-8'))['wed']
    for t in ('wed_a', 'wed_b'):
        p = os.path.join(AQUI, 'tandas', '%s.entrada.json' % t)
        e = json.load(open(p, encoding='utf-8'), object_pairs_hook=OrderedDict)
        e['valores_del_caso (SOLO para entender; en el texto escribe el token)'] = OrderedDict(
            (k, v['texto']) for k, v in cif.items())
        e['resto_del_kit (lo que el Word puede citar sin token: son datos de los otros ficheros)'] = KIT
        e['reglas_wed (mandan sobre las notas en lo que choquen)'] = REGLAS
        e['verificacion'] = 'python3 %s/bp9.py check_textos --tanda %s' % (REL, t)
        with open(p, 'w', encoding='utf-8') as fh:
            json.dump(e, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
        print('tandas/%s.entrada.json: %d párrafos, %d palabras · %d tokens con su valor final · %d párrafos con nota' % (
            t, e['n_parrafos'], e['n_palabras'], len(cif), sum(1 for x in e['parrafos'] if x.get('nota'))))
    return 0


if __name__ == '__main__':
    sys.exit(main())
