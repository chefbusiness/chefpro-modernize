#!/usr/bin/env python3
"""
calibracion_wed.py — Wedding Venue Business Plan Kit (EN) · D15 de la SPEC (D160) sobre el informe de `aplicar_en --json`
y el `cifras_caso.json` que deja al lado. Solo JSON (Mac o VPS). Sesión Claude Code, 27-oct-2026 (F2-EN, paso 1a). Clon de
`../business-plans-en-8/calibracion_piz.py`.

Gates del caso (D160): holgura de caja año 1 ≥ 15 % · DSCR mínimo ≥ 1.30 (más estricto que el 1.25 común) · saldo mínimo
de Tesorería > 0 · cobertura ≥ 98 % · neto año 3 ≤ 16 % · exceso de fondos (origen − usos) entre 0 y 5 % · los umbrales
D165 del P&L en verde (margen bruto, personal y neto los 3 años desde el informe; coste directo y renta del año 1, que
son los peores: el coste directo es un % fijo y la renta baja al crecer las ventas). Si algo falla, dice la palanca de D160
en su orden (holgura → B5 +$2 o B24 $4,500 · neto A3 > 16 % → B7/B8 6/4 % · DSCR → B30 +$25,000 · cobertura →
Staffing!B22/B23).

    python3 bp9.py calibracion /tmp/wed-dry.json [--cifras /tmp/wed-dry/cifras_caso.json]
"""
import argparse
import json
import os
import sys

UMBRALES = (('holgura_caja_pct', '>=', 0.15), ('dscr_min', '>=', 1.30), ('saldo_minimo', '>', 0.0),
            ('cobertura_horas', '>=', 0.98))
NETO_A3_MAX = 0.16
EXCESO = (0.0, 0.05)
PALANCAS = [
    ('holgura_caja_pct', 'holgura < 15 % → B5 +$2 (revenue per guest) o B24 $4,500 (rent)'),
    ('neto_a3', 'neto año 3 > 16 % → B7/B8 6 % / 4 % (crecimiento)'),
    ('dscr_min', 'DSCR < 1.30 → B30 +$25,000 (recursos propios)'),
    ('cobertura_horas', 'cobertura < 98 % → Staffing B22/B23 (horas de estructura), nunca la plantilla sin nota'),
    ('exceso_fondos', 'exceso de fondos fuera de 0-5 % → revisa el préstamo calibrado (B31) y el fondo de maniobra'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('informe')
    ap.add_argument('--cifras', default=None)
    a = ap.parse_args()
    inf = json.load(open(a.informe, encoding='utf-8'))
    cal = inf['calibracion']['wed']['metricas']
    p_c = a.cifras or os.path.join(os.path.dirname(inf['carpetas']['wed']), 'cifras_caso.json')
    if not os.path.exists(p_c):
        p_c = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cifras_caso.json')
    cif = json.load(open(p_c, encoding='utf-8'))['wed']
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
    print('  neto A1-A3          %s (año 3 ≤ %.0f %%)' % (['%.1f%%' % (x * 100) for x in netos], NETO_A3_MAX * 100))
    if netos[2] > NETO_A3_MAX:
        fallos.append('neto_a3')
    exc = cif['exceso_fondos_pct']['valor']
    ok = EXCESO[0] - 1e-9 <= exc <= EXCESO[1] + 1e-9
    print('  exceso de fondos    %.2f%% (0-5 %%) → %s' % (exc * 100, 'OK' if ok else 'FALLA'))
    if not ok:
        fallos.append('exceso_fondos')
    for rot, r in cal['ratios_pyg'].items():
        ok = all(r['cumple'])
        print('  %-30s %s %s %.3f → %s' % (rot, ['%.3f' % v for v in r['valores']], r['sentido'], r['umbral'],
                                            'OK' if ok else 'ÁMBAR'))
        if not ok:
            fallos.append('D165 ' + rot)
    for tok, umbral, rot in (('coste_directo_ventas_pct', 0.15, 'Coste directo / Ventas (año 1)'),
                             ('ocupacion_pct', 0.12, 'Renta / Ventas (año 1)')):
        v = cif[tok]['valor']
        ok = v <= umbral + 1e-9
        print('  %-30s %.3f <= %.3f → %s' % (rot, v, umbral, 'OK' if ok else 'ÁMBAR'))
        if not ok:
            fallos.append('D165 ' + rot)
    if inf.get('fallos'):
        fallos += ['aplicar_en: %s' % x for x in inf['fallos']]
    print('  préstamo %s · CAPEX %.0f · necesidad de caja %.0f · DSCR mín %.2f · equilibrio de caja %s eventos' % (
        inf['prestamos'], cif['capex']['valor'], cif['necesidad_caja']['valor'], cif['dscr_min']['valor'],
        cif['equilibrio_caja_eventos']['texto']))
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
