#!/usr/bin/env python3
"""
calibracion_sus.py — Sushi Restaurant Business Plan Kit (EN) · D15 (F1-camino §6 y research US §8) sobre el informe de `aplicar_en --json`
y el `cifras_caso.json` que deja al lado. Solo JSON (Mac o VPS). Sesión Claude Code, 31-oct-2026 (F2-EN). Clon de
`../business-plans-en-13/calibracion_pol.py` (Rotisserie EN).

Comprueba lo que `aplicar_en` no mira (el D15 común solo exige DSCR, saldo, cobertura y holgura): neto a régimen
(año 3) ≤ 12 % y los 5 umbrales del P&L (research US §5.2) en verde los 3 años; y vuelve a imprimir los cuatro comunes. Si algo
falla, dice la palanca de research US §8 en su orden (holgura < 15 % → B30 +$20,000 o B5 $34.00 · neto > 12 % → B4
105 · DSCR < 1.25 → B30). La estacionalidad NO es palanca (Mes 1 = enero, F1-camino §6).

    python3 bp14.py calibracion /root/tmp-sus-en/dry.json [--cifras /root/tmp-sus-en/dry/cifras_caso.json]
"""
import argparse
import json
import os
import sys

UMBRALES = (('holgura_caja_pct', '>=', 0.15), ('dscr_min', '>=', 1.25), ('saldo_minimo', '>', 0.0),
            ('cobertura_horas', '>=', 0.98))
NETO_REGIMEN_MAX = 0.12
PALANCAS = [
    ('holgura_caja_pct', 'holgura < 15 % → B30 +$20,000 (recursos propios) o B5 $34.00 (ticket)'),
    ('neto_regimen', 'neto a régimen > 12 % → B4 105 covers/día'),
    ('dscr_min', 'DSCR < 1.25 → B30 (recursos propios); el plazo ya está en 10 años'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('informe')
    ap.add_argument('--cifras', default=None)
    a = ap.parse_args()
    inf = json.load(open(a.informe, encoding='utf-8'))
    cal = inf['calibracion']['sus']['metricas']
    p_c = a.cifras or os.path.join(os.path.dirname(inf['carpetas']['sus']), 'cifras_caso.json')
    if not os.path.exists(p_c):
        p_c = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cifras_caso.json')
    cif = json.load(open(p_c, encoding='utf-8'))['sus']
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
    print('  neto A1-A3          %s (régimen = año 3 ≤ %.0f %%)' % (['%.1f%%' % (x * 100) for x in netos],
                                                                    NETO_REGIMEN_MAX * 100))
    if netos[2] > NETO_REGIMEN_MAX:
        fallos.append('neto_regimen')
    for rot, r in cal['ratios_pyg'].items():
        ok = all(r['cumple'])
        print('  %-30s %s %s %.3f → %s' % (rot, ['%.3f' % v for v in r['valores']], r['sentido'], r['umbral'],
                                            'OK' if ok else 'ÁMBAR'))
        if not ok:
            fallos.append('umbral ' + rot)
    if inf.get('fallos'):
        fallos += ['aplicar_en: %s' % x for x in inf['fallos']]
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
