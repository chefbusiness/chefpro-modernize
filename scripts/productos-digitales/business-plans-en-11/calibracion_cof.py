#!/usr/bin/env python3
"""
calibracion_cof.py — Coffee Cart Business Plan Kit (EN) · D15 de la SPEC (D220) sobre el informe de `aplicar_en --json`
y el `cifras_caso.json` que deja al lado. Solo JSON (Mac o VPS). Sesión Claude Code, 28-oct-2026 (paso 1a). Clon de
`../business-plans-en-9/calibracion_wed.py` con los umbrales de la línea de eventos (BBQ / Paella: D15 de la research).

Gates del caso (D220): holgura de caja año 1 ≥ 15 % · DSCR mínimo ≥ 1.25 · saldo mínimo de Tesorería > 0 (el valle es
JULIO) · cobertura ≥ 98 % · neto año 1 ≥ 5 % y año 3 ≤ 16 % · exceso de fondos (origen − usos) entre 0 y 5 % · los
umbrales D225 del P&L en verde los 3 años (margen bruto ≥ 72 %, mercancía ≤ 20 %, personal ≤ 40 %, commissary ≤ 6 %,
neto ≥ 5 %; los del año 1 son los peores). Si algo falla, dice la palanca de D220 en su orden (holgura → B4 +10 hasta
190 · saldo ≤ 0 → B35 3 → 4 antes de tocar el precio · DSCR → B30 +$5,000 · cobertura → Staffing B18/B19).

    python3 bp11.py calibracion /root/tmp-cof/dry.json [--cifras /root/tmp-cof/dry/cifras_caso.json]
"""
import argparse
import json
import os
import sys

PLAN = 'cof'
UMBRALES = (('holgura_caja_pct', '>=', 0.15), ('dscr_min', '>=', 1.25), ('saldo_minimo', '>', 0.0),
            ('cobertura_horas', '>=', 0.98))
NETO_A1_MIN, NETO_A3_MAX = 0.05, 0.16          # año 3: tope de cordura de la finca (D160), no de la research
EXCESO = (0.0, 0.05)
PALANCAS = [
    ('holgura_caja_pct', 'holgura < 15 % → B4 +10 eventos (hasta 190); anótalo en CALIBRACION_D15 y F2-NOTAS §3'),
    ('saldo_minimo', 'saldo mínimo ≤ 0 (valle de julio) → B35 3 → 4 meses de fondo de maniobra antes de tocar el precio'),
    ('dscr_min', 'DSCR < 1.25 → B30 +$5,000 (recursos propios)'),
    ('cobertura_horas', 'cobertura < 98 % → Staffing B18/B19 o el FTE del lead barista, nunca sin nota'),
    ('neto_a1', 'neto año 1 < 5 % → revisa B5 (precio por invitado) frente a Flashquotes antes que los costes'),
    ('neto_a3', 'neto año 3 > 16 % → B7/B8 (crecimiento) a 8 % / 5 %'),
    ('exceso_fondos', 'exceso de fondos fuera de 0-5 % → revisa el préstamo calibrado (B31) y el fondo de maniobra'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('informe')
    ap.add_argument('--cifras', default=None)
    a = ap.parse_args()
    inf = json.load(open(a.informe, encoding='utf-8'))
    cal = inf['calibracion'][PLAN]['metricas']
    p_c = a.cifras or os.path.join(os.path.dirname(inf['carpetas'][PLAN]), 'cifras_caso.json')
    if not os.path.exists(p_c):
        p_c = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cifras_caso.json')
    cif = json.load(open(p_c, encoding='utf-8'))[PLAN]
    fallos = []
    for t, s, u in UMBRALES:
        v = cal[t]
        ok = v >= u if s == '>=' else v > u
        print('  %-18s %10.4f %s %s → %s' % (t, v, s, u, 'OK' if ok else 'FALLA'))
        if not ok:
            fallos.append(t)
    ventas = [cif['ventas_a%d' % k]['valor'] for k in (1, 2, 3)]
    netos = [cif['resultado_neto_a%d' % k]['valor'] / ventas[k - 1] for k in (1, 2, 3)]
    print('  ventas A1-A3        %s' % ['%.0f' % x for x in ventas])
    print('  neto A1-A3          %s (año 1 ≥ %.0f %% · año 3 ≤ %.0f %%)' % (
        ['%.1f%%' % (x * 100) for x in netos], NETO_A1_MIN * 100, NETO_A3_MAX * 100))
    if netos[0] < NETO_A1_MIN:
        fallos.append('neto_a1')
    if netos[2] > NETO_A3_MAX:
        fallos.append('neto_a3')
    if 'exceso_fondos_pct' in cif:
        exc = cif['exceso_fondos_pct']['valor']
    else:                                      # línea de eventos: origen (propios + préstamo) − usos (inversión total)
        usos = cif['inversion_total']['valor']
        exc = (cif['fondos_propios']['valor'] + cif['prestamo']['valor'] - usos) / usos
    ok = EXCESO[0] - 1e-9 <= exc <= EXCESO[1] + 1e-9
    print('  exceso de fondos    %.2f%% (0-5 %%) → %s' % (exc * 100, 'OK' if ok else 'FALLA'))
    if not ok:
        fallos.append('exceso_fondos')
    for rot, r in cal.get('ratios_pyg', {}).items():
        ok = all(r['cumple'])
        print('  %-30s %s %s %.3f → %s' % (rot, ['%.3f' % v for v in r['valores']], r['sentido'], r['umbral'],
                                            'OK' if ok else 'ÁMBAR'))
        if not ok:
            fallos.append('D225 ' + rot)
    if inf.get('fallos'):
        fallos += ['aplicar_en: %s' % x for x in inf['fallos']]
    print('  préstamo %s · CAPEX %.0f · inversión total %.0f · DSCR mín %.2f · equilibrio %s / caja %s eventos · '
          'saldo mínimo %.0f (mes %s)' % (
              inf['prestamos'], cif['capex']['valor'], cif['inversion_total']['valor'], cif['dscr_min']['valor'],
              cif['equilibrio_eventos']['texto'], cif['equilibrio_caja_eventos']['texto'], cif['saldo_minimo']['valor'],
              cif.get('mes_saldo_minimo', {}).get('texto', '?')))
    if fallos:
        print('CALIBRACIÓN D15: FALLA %s' % fallos)
        for t, p in PALANCAS:
            if t in fallos:
                print('  palanca: ' + p)
        return 1
    print('CALIBRACIÓN D15: VERDE (préstamo %s)' % inf['prestamos'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
