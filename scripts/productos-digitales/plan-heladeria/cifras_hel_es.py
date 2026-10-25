#!/usr/bin/env python3
"""
cifras_hel_es.py — Heladería Artesanal ES 1.0 (copia de `parrillero-2_2/cifras_par_es.py`; rótulos de línea A medidos
sobre el libro generado el 25-oct-2026): lee la CACHÉ del plan financiero (después de `inject_cache`, que hace
`main.py`) por RÓTULO, escribe `cifras_caso_es.json` (los tokens {ASI} del docx, SPEC D15) y pasa los gates del caso
(SPEC D9): DSCR mínimo ≥ 1,25 · saldo mínimo de tesorería > 0 · cobertura de horas ≥ 98 % · holgura sobre el
equilibrio de caja del año 1 ≥ 15 % (las de los años 2 y 3, informativas, ≥ 0) · exceso de financiación (origen −
usos) ≥ 0 y < 5 % · resultado neto ≤ 9 % de las ventas en los tres años. Corre en el VPS (openpyxl).

    /root/venv-guias/bin/python cifras_hel_es.py --xlsx <plan-financiero-heladeria.xlsx>

Sesión Claude Code, 25-oct-2026.
"""
import argparse
import json
import math
import os
import re
import sys

import openpyxl

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, 'cifras_caso_es.json')

#: Mes 1 = marzo (SPEC D6): nombre del mes del calendario de cada «Mes n» de la Tesorería.
MESES = ('marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre',
         'enero', 'febrero')

#: token → (hoja, regex del rótulo de la columna A, columna, formato). Formatos: eur (miles con punto, sin
#: decimales) · eur2 · pct (1 decimal) · pct0 · dec1 · dec2 · int · int_up (redondeo hacia arriba).
SUP, PYG, INV, PE, TES, FIN, PER, ESC = ('0. Supuestos', 'PyG 3 Años', 'Inversión Inicial', 'Punto Equilibrio',
                                         'Tesorería 12 meses', 'Financiación', 'Personal', 'Escenarios')
MAPA = {
    'CLIENTES_DIA': (SUP, r'^clientes/d[ií]a \(media', 2, 'int'),
    'TICKET': (SUP, r'^ticket medio sin iva', 2, 'eur2'),
    'TICKET_IVA': (SUP, r'^pvp equivalente con iva', 2, 'eur2'),
    'DIAS_APERTURA': (SUP, r'^d[ií]as de apertura al a[ñn]o', 2, 'int'),
    'CREC_A2': (SUP, r'^crecimiento de volumen del a[ñn]o 2', 2, 'pct0'),
    'CREC_A3': (SUP, r'^crecimiento de volumen del a[ñn]o 3', 2, 'pct0'),
    'PCT_COMIDA': (SUP, r'^ventas de comida sobre el total', 2, 'pct0'),
    'FOOD_COST': (SUP, r'^coste de mercanc[ií]a sobre las ventas de comida', 2, 'pct0'),
    'BEBIDA_COST': (SUP, r'^coste de mercanc[ií]a sobre las ventas de bebida', 2, 'pct0'),
    'CONSUMIBLES_PCT': (SUP, r'^consumibles sobre ventas', 2, 'pct0'),
    'DELIVERY_PCT': (SUP, r'^ventas por delivery', 2, 'pct0'),
    'COMISION_DELIVERY': (SUP, r'^comisi[oó]n de la plataforma', 2, 'pct0'),
    'ALQUILER_MES': (SUP, r'^alquiler mensual del local', 2, 'eur'),
    'SUMINISTROS_MES': (SUP, r'^suministros mensuales', 2, 'eur'),
    'SEGUROS_ANO': (SUP, r'^seguros', 2, 'eur'),
    'RECURSOS_PROPIOS': (SUP, r'^recursos propios', 2, 'eur'),
    'TIPO_PRESTAMO': (SUP, r'^tipo de inter[eé]s nominal', 2, 'pct0'),
    'PLAZO_PRESTAMO': (SUP, r'^plazo del pr[eé]stamo', 2, 'int'),
    'CARENCIA': (SUP, r'^carencia de principal', 2, 'int'),
    'DIAS_COBRO': (SUP, r'^d[ií]as medios de cobro', 2, 'int'),
    'AFORO': (SUP, r'^aforo del local', 2, 'int'),
    'RAMPA_MES1': (SUP, r'^actividad del mes 1', 2, 'pct0'),
    'MESES_RAMPA': (SUP, r'^meses hasta alcanzar', 2, 'int'),
    'IS_GENERAL': (SUP, r'^impuesto de sociedades, tipo general', 2, 'pct0'),         # revisión final m3
    'HOLGURA_MINIMA': (SUP, r'^holgura m[ií]nima sobre el punto de equilibrio', 2, 'pct0'),  # revisión final M1
    'VENTAS_A1': (PYG, r'^ingresos totales', 2, 'eur'),
    'VENTAS_A2': (PYG, r'^ingresos totales', 3, 'eur'),
    'VENTAS_A3': (PYG, r'^ingresos totales', 4, 'eur'),
    'CLIENTES_DIA_A2': (PYG, r'^clientes/d[ií]a \(media\)', 3, 'int'),
    'CLIENTES_DIA_A3': (PYG, r'^clientes/d[ií]a \(media\)', 4, 'int'),
    'COSTES_VARIABLES_A1': (PYG, r'^total costes variables', 2, 'eur'),
    'MARGEN_BRUTO_A1': (PYG, r'^margen bruto$', 2, 'eur'),
    'MARGEN_BRUTO_PCT_A1': (PYG, r'^margen bruto / ventas', 2, 'pct'),
    'ALQUILER_ANO': (PYG, r'^alquiler del local', 2, 'eur'),
    'ALQUILER_PCT_A1': (PYG, r'^alquiler / ventas', 2, 'pct'),
    'PERSONAL_A1': (PYG, r'^personal \(n[oó]minas', 2, 'eur'),
    'PERSONAL_A2': (PYG, r'^personal \(n[oó]minas', 3, 'eur'),
    'PERSONAL_A3': (PYG, r'^personal \(n[oó]minas', 4, 'eur'),
    'PERSONAL_PCT_A1': (PYG, r'^coste de personal / ventas', 2, 'pct'),
    'MERCANCIA_PCT_A1': (PYG, r'^coste de mercanc[ií]a / ventas', 2, 'pct'),
    'MARKETING_ANO': (PYG, r'^marketing y publicidad', 2, 'eur'),
    'TASA_TERRAZA': (PYG, r'^tasa de terraza', 2, 'eur'),
    'MANTENIMIENTO_FRIO': (PYG, r'^mantenimiento del fr[ií]o', 2, 'eur'),
    'AMORTIZACION_A1': (PYG, r'^amortizaci[oó]n del inmovilizado', 2, 'eur'),
    'INTERESES_A1': (PYG, r'^gastos financieros', 2, 'eur'),
    'FIJOS_A1': (PYG, r'^total costes fijos', 2, 'eur'),
    'RAI_A1': (PYG, r'^resultado antes de impuestos', 2, 'eur'),
    'RAI_A2': (PYG, r'^resultado antes de impuestos', 3, 'eur'),
    'RAI_A3': (PYG, r'^resultado antes de impuestos', 4, 'eur'),
    'NETO_A1': (PYG, r'^resultado neto$', 2, 'eur'),
    'NETO_A2': (PYG, r'^resultado neto$', 3, 'eur'),
    'NETO_A3': (PYG, r'^resultado neto$', 4, 'eur'),
    'NETO_PCT_A1': (PYG, r'^resultado neto / ventas', 2, 'pct'),
    'NETO_PCT_A2': (PYG, r'^resultado neto / ventas', 3, 'pct'),
    'NETO_PCT_A3': (PYG, r'^resultado neto / ventas', 4, 'pct'),
    'CAPEX': (INV, r'^capex', 2, 'eur'),
    'FONDO_MANIOBRA': (INV, r'^fondo de maniobra$', 2, 'eur'),
    'INVERSION_TOTAL': (INV, r'^inversi[oó]n total', 2, 'eur'),
    'IVA_INVERSION': (INV, r'^iva soportado sobre la inversi', 2, 'eur'),
    'NECESIDAD_CAJA': (INV, r'^necesidad total de caja', 2, 'eur'),
    'FIANZA': (INV, r'^fianza del alquiler', 2, 'eur'),
    'RENTA_PREVIA': (INV, r'^alquiler de los meses previos', 2, 'eur'),
    'IMPREVISTOS': (INV, r'^imprevistos de obra', 2, 'eur'),
    'OBRA': (INV, r'^obra y acondicionamiento', 2, 'eur'),
    'INSTALACION_ELECTRICA': (INV, r'^instalaci[oó]n el[eé]ctrica', 2, 'eur'),
    'PASTEURIZADOR': (INV, r'^pasteurizador', 2, 'eur'),
    'MANTECADORA': (INV, r'^mantecadora', 2, 'eur'),
    'ABATIDOR': (INV, r'^abatidor', 2, 'eur'),
    'ARMARIOS': (INV, r'^armarios de conservaci', 2, 'eur'),
    'VITRINA': (INV, r'^vitrina ventilada', 2, 'eur'),
    'MOBILIARIO': (INV, r'^mobiliario del local', 2, 'eur'),
    'FORMACION': (INV, r'^formaci[oó]n t[eé]cnica', 2, 'eur'),
    'BASE_OBRA': (INV, r'^obra, instalaciones y acondicionamiento$', 2, 'eur'),
    'BASE_MAQUINARIA': (INV, r'^maquinaria, mobiliario y equipos', 2, 'eur'),
    'PRESTAMO': (FIN, r'^pr[eé]stamo bancario$', 2, 'eur'),
    'ORIGEN_FONDOS': (FIN, r'^total origen de fondos', 2, 'eur'),
    'DIFERENCIA_FONDOS': (FIN, r'^diferencia \(origen - usos\)', 2, 'eur'),
    'DIFERENCIA_FONDOS_PCT': (FIN, r'^diferencia sobre los usos', 2, 'pct'),
    'CUOTA_ANUAL': (FIN, r'^cuota anual durante la amortizaci', 2, 'eur'),
    'DSCR_A2': (FIN, r'^dscr del a[ñn]o 2', 2, 'dec2'),
    'DSCR_A3': (FIN, r'^dscr del a[ñn]o 3', 2, 'dec2'),
    'DSCR_MIN': (FIN, r'^dscr m[ií]nimo de todo el cuadro', 2, 'dec2'),
    'SALDO_MINIMO': (TES, r'^saldo m[ií]nimo del a[ñn]o', 2, 'eur'),
    'MES_SALDO_MINIMO': (TES, r'^mes en el que la caja toca fondo', 2, 'int'),
    'SALDO_MES12': (TES, r'^saldo acumulado de caja', 13, 'eur'),
    'PAYBACK': (TES, r'^payback del proyecto', 2, 'dec1'),
    'PAYBACK_CAPEX': (TES, r'^payback sobre el capex', 2, 'dec1'),
    'COSTE_VAR_CLIENTE': (PE, r'^coste variable por cliente', 2, 'eur2'),
    'MARGEN_CLIENTE': (PE, r'^margen de contribuci[oó]n por cliente', 2, 'eur2'),
    'BE_CLIENTES_DIA': (PE, r'^clientes necesarios al d[ií]a$', 2, 'int_up'),
    'BE_CLIENTES_DIA_CAJA': (PE, r'^clientes necesarios al d[ií]a \(caja\)', 2, 'int_up'),
    'BE_CLIENTES_DIA_CAJA_A2': (PE, r'^clientes necesarios al d[ií]a \(caja\)', 3, 'int_up'),
    'BE_CLIENTES_DIA_CAJA_A3': (PE, r'^clientes necesarios al d[ií]a \(caja\)', 4, 'int_up'),
    'BE_INGRESOS': (PE, r'^ingresos necesarios al a[ñn]o$', 2, 'eur'),
    'BE_INGRESOS_CAJA': (PE, r'^ingresos necesarios al a[ñn]o \(caja\)', 2, 'eur'),
    'BE_INGRESOS_CAJA_A2': (PE, r'^ingresos necesarios al a[ñn]o \(caja\)', 3, 'eur'),
    'BE_INGRESOS_CAJA_A3': (PE, r'^ingresos necesarios al a[ñn]o \(caja\)', 4, 'eur'),
    'HOLGURA_CAJA': (PE, r'^holgura sobre el equilibrio de caja', 2, 'pct'),
    'HOLGURA_CAJA_A2': (PE, r'^holgura sobre el equilibrio de caja', 3, 'pct'),
    'HOLGURA_CAJA_A3': (PE, r'^holgura sobre el equilibrio de caja', 4, 'pct'),
    'COBERTURA_HORAS': (PER, r'^cobertura \(contratadas', 2, 'pct0'),
    'PLANTILLA_PERSONAS': (PER, r'^total plantilla', 2, 'int'),
    'SUELDO_TITULAR': (PER, r'^titular', 4, 'eur'),                                    # revisión final m2 (bruto mes)
    'JORNADAS': (PER, r'^total plantilla', 3, 'dec2'),
    'HORAS_DIA': (PER, r'^horas de servicio al d[ií]a', 2, 'dec1'),
    'HORAS_PRODUCCION': (PER, r'^horas de producci[oó]n', 2, 'dec2'),
    'HORAS_NECESARIAS': (PER, r'^horas de servicio a cubrir al a[ñn]o', 2, 'int'),
    'HORAS_CONTRATADAS': (PER, r'^horas contratadas al a[ñn]o', 2, 'int'),
    'ESC_PES_CLIENTES': (ESC, r'^clientes/d[ií]a$', 2, 'int'),
    'ESC_OPT_CLIENTES': (ESC, r'^clientes/d[ií]a$', 4, 'int'),
    'ESC_PES_TICKET': (ESC, r'^ticket medio sin iva', 2, 'eur2'),
    'ESC_OPT_TICKET': (ESC, r'^ticket medio sin iva', 4, 'eur2'),
    'ESC_PES_DIAS': (ESC, r'^d[ií]as de apertura', 2, 'int'),
    'ESC_OPT_DIAS': (ESC, r'^d[ií]as de apertura', 4, 'int'),
    'ESC_PES_VENTAS': (ESC, r'^ingresos anuales', 2, 'eur'),
    'ESC_OPT_VENTAS': (ESC, r'^ingresos anuales', 4, 'eur'),
    'ESC_PES_NETO': (ESC, r'^resultado neto$', 2, 'eur'),
    'ESC_OPT_NETO': (ESC, r'^resultado neto$', 4, 'eur'),
}


def fmt(v, f):
    return _fmt(v, f).replace('-', '\u2212', 1) if v < 0 else _fmt(v, f)   # revisión final m12: signo menos tipográfico


def _fmt(v, f):
    if f in ('int', 'int_up'):
        n = math.ceil(v - 1e-9) if f == 'int_up' else round(v)
        return '{:,}'.format(int(n)).replace(',', '.')
    if f == 'eur':
        return '{:,}'.format(int(round(v))).replace(',', '.') + ' €'
    if f == 'eur2':
        return '{:,.2f}'.format(v).replace(',', 'X').replace('.', ',').replace('X', '.') + ' €'
    if f in ('pct', 'pct0'):
        txt = ('{:.1f}' if f == 'pct' else '{:.0f}').format(v * 100).replace('.', ',')
        return txt + ' %'
    if f in ('dec1', 'dec2'):
        return ('{:.1f}' if f == 'dec1' else '{:.2f}').format(v).replace('.', ',')
    raise ValueError(f)


def leer(path):
    wb = openpyxl.load_workbook(path, data_only=True)
    crudo, falta, textos = {}, [], {}
    for tok, (hoja, rx, col, f) in MAPA.items():
        ws = wb[hoja]
        v = None
        for r in range(1, ws.max_row + 1):
            a = ws.cell(r, 1).value
            if isinstance(a, str) and re.search(rx, a.strip(), re.I):
                v = ws.cell(r, col).value
                break
        if isinstance(v, str) and tok.startswith('PAYBACK') and v.strip():   # «Más de 3 años»: texto del libro
            textos[tok] = v.strip()
            continue
        if not isinstance(v, (int, float)):
            falta.append('%s (%s · %s): %r' % (tok, hoja, rx, v))
            continue
        crudo[tok] = (float(v), f)
    # derivados
    if all(k in crudo for k in ('CAPEX', 'FIANZA', 'RENTA_PREVIA')):    # las 19 partidas + imprevistos (research: 117.150)
        crudo['INVERSION_PARTIDAS'] = (crudo['CAPEX'][0] - crudo['FIANZA'][0] - crudo['RENTA_PREVIA'][0], 'eur')
    if all(k in crudo for k in ('CLIENTES_DIA', 'BE_CLIENTES_DIA')):    # holgura sobre el equilibrio CONTABLE, año 1
        cd = MAPA['BE_CLIENTES_DIA']
        be = _valor(wb, cd[0], cd[1], cd[2])
        crudo['HOLGURA_CONTABLE'] = (crudo['CLIENTES_DIA'][0] / be - 1, 'pct')
    if 'MES_SALDO_MINIMO' in crudo:
        textos['MES_SALDO_MINIMO_NOMBRE'] = MESES[int(round(crudo['MES_SALDO_MINIMO'][0])) - 1]
    if all(k in crudo for k in ('ORIGEN_FONDOS', 'NECESIDAD_CAJA')):
        crudo['EXCESO_FINANCIACION'] = (crudo['ORIGEN_FONDOS'][0] - crudo['NECESIDAD_CAJA'][0], 'eur')
    return crudo, falta, textos


def _valor(wb, hoja, rx, col):
    ws = wb[hoja]
    for r in range(1, ws.max_row + 1):
        a = ws.cell(r, 1).value
        if isinstance(a, str) and re.search(rx, a.strip(), re.I):
            return float(ws.cell(r, col).value)
    raise KeyError(rx)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--xlsx', required=True)
    ap.add_argument('--salida', default=SALIDA)
    a = ap.parse_args()
    crudo, falta, textos = leer(a.xlsx)
    tokens = dict((k, fmt(v, f)) for k, (v, f) in crudo.items())
    tokens.update(textos)
    json.dump({'fuente': os.path.basename(a.xlsx), 'tokens': tokens,
               'valores': dict((k, v) for k, (v, _f) in crudo.items())},
              open(a.salida, 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)
    v = dict((k, x[0]) for k, x in crudo.items())
    netos = [v.get('NETO_PCT_A%d' % i, 1) for i in (1, 2, 3)]
    gates = [
        ('DSCR mínimo ≥ 1,25', v.get('DSCR_MIN', 0) >= 1.25),
        ('saldo mínimo de tesorería > 0', v.get('SALDO_MINIMO', -1) > 0),
        ('cobertura de horas ≥ 98 %', v.get('COBERTURA_HORAS', 0) >= 0.98),
        ('holgura sobre el equilibrio de caja del año 1 ≥ 15 %', v.get('HOLGURA_CAJA', 0) >= 0.15),
        ('holgura de caja del año 2 (sin carencia) ≥ 0 % (informativa)', v.get('HOLGURA_CAJA_A2', -1) >= 0),
        ('holgura de caja del año 3 ≥ 0 % (informativa)', v.get('HOLGURA_CAJA_A3', -1) >= 0),
        ('exceso de financiación (origen - usos) ≥ 0 y < 5 %', 0 <= v.get('DIFERENCIA_FONDOS_PCT', -1) < 0.05),
        ('resultado neto ≤ 9 % de las ventas (años 1-3)', max(netos) <= 0.09),
    ]
    for tok in ('CLIENTES_DIA', 'TICKET', 'DIAS_APERTURA', 'VENTAS_A1', 'VENTAS_A2', 'VENTAS_A3', 'RAI_A1', 'NETO_A1',
                'NETO_A2', 'NETO_A3', 'NETO_PCT_A1', 'NETO_PCT_A2', 'NETO_PCT_A3', 'INVERSION_PARTIDAS', 'CAPEX',
                'INVERSION_TOTAL', 'NECESIDAD_CAJA', 'RECURSOS_PROPIOS', 'PRESTAMO', 'DIFERENCIA_FONDOS',
                'DIFERENCIA_FONDOS_PCT', 'DSCR_A2', 'DSCR_A3', 'DSCR_MIN', 'SALDO_MINIMO', 'MES_SALDO_MINIMO',
                'MES_SALDO_MINIMO_NOMBRE', 'SALDO_MES12', 'BE_CLIENTES_DIA', 'BE_CLIENTES_DIA_CAJA', 'HOLGURA_CONTABLE',
                'HOLGURA_CAJA', 'HOLGURA_CAJA_A2', 'HOLGURA_CAJA_A3', 'COBERTURA_HORAS', 'PAYBACK', 'MARGEN_BRUTO_PCT_A1',
                'PERSONAL_PCT_A1', 'ESC_PES_NETO', 'ESC_OPT_NETO'):
        print('  %-26s %s' % (tok, tokens.get(tok, '—')))
    for nombre, ok in gates:
        print('  [%s] %s' % ('OK' if ok else 'ROJO', nombre))
    for f in falta:
        print('  FALTA', f)
    ok_total = all(ok for _n, ok in gates) and not falta
    print('cifras_caso_es.json: %d tokens · gates del caso D9 %s' % (len(tokens), 'VERDE' if ok_total else 'ROJA'))
    sys.exit(0 if ok_total else 1)


if __name__ == '__main__':
    main()
