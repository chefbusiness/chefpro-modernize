#!/usr/bin/env python3
"""
tandas_docx.py — Catering ES 2.0 (SPEC D8): prepara y valida las dos tandas de redacción del plan de negocio (docx).

Las 61 ranuras de texto del docx del Food Truck ES (131 párrafos, 10 Heading 1; mapa en
`business-plans-en-4/docx_es_cat.json`, el mismo que usó el EN) se escriben NUEVAS, en español, para el catering:
  cat_es_a = §1-5 (29 ranuras) · cat_es_b = §6-10 (32 ranuras).
Las cifras del Excel van SIEMPRE como token {ASI} (`cifras_caso_es.json`); `docx_cat_es.py` las resuelve al ensamblar.
Sólo lee JSON: corre en el Mac.

    python3 tandas_docx.py preparar                       # tandas/cat_es_{a,b}.entrada.json
    python3 tandas_docx.py check --tanda cat_es_a         # valida textos/cat_es_a.json (salida del redactor)

Sesión Claude Code, 11-oct-2026.
"""
import argparse
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BP4 = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
TANDAS, TEXTOS = os.path.join(AQUI, 'tandas'), os.path.join(AQUI, 'textos')
CIFRAS = os.path.join(AQUI, 'cifras_caso_es.json')

SECCIONES = {
    1: '1. Resumen Ejecutivo', 2: '2. Concepto y Propuesta de Valor', 3: '3. Análisis de Mercado',
    4: '4. Análisis Competitivo', 5: '5. Plan de Marketing y Captación', 6: '6. Plan de Operaciones',
    7: '7. Estructura Organizativa y RRHH', 8: '8. Plan Financiero', 9: '9. Aspectos Legales y Licencias',
    10: '10. Conclusiones y Plan de Acción',
}

#: Lo que tiene que contar cada sección (español de España, para el mercado español). Cifras del Excel = tokens.
PISTAS = {
    1: 'Qué es el negocio: catering temático multi-concepto para eventos, con estaciones de cocinas del mundo en '
       'directo (show cooking), sin restaurante y con una cocina central compartida y autorizada. Dos motores: empresas '
       'entre semana (coffee breaks, cócteles, comidas y Navidad: 65 % de los eventos) y particulares el fin de semana '
       '(bodas, comuniones, cumpleaños). Las cifras clave por token: {EVENTOS_ANO} eventos de {INVITADOS_EVENTO} '
       'invitados a {PRECIO_INVITADO} sin IVA, ventas {VENTAS_A1}, resultado neto {NETO_A1}, inversión '
       '{INVERSION_TOTAL}, préstamo {PRESTAMO} y equilibrio en {BE_EVENTOS_ANO} eventos al año. Para quién es el plan y '
       'qué contiene el kit (Excel de 9 hojas, checklist de 82 tareas, calculadora, contratos, menús y fichas).',
    2: 'La propuesta: estaciones temáticas en directo (sushi, tacos al pastor, parrilla argentina, wok, tandoor, '
       'vegano…), empezando por las 2-3 que domines y añadiendo una cuando se venda; dietas especiales y alérgenos al '
       'mismo nivel que el menú general; marca del cliente en el evento corporativo; prueba de menú cobrada y '
       'descontable. La mezcla de cinco tipos de evento del plan (tabla de Instrucciones del Excel: coffee break 35 '
       'eventos × 35 invitados × 16 €; cóctel 35 × 80 × 40 €; comida de empresa 15 × 100 × 62 €; boda 15 × 110 × 98 €; '
       'celebración familiar 30 × 45 × 48 €, precios sin IVA) y por qué da {PRECIO_INVITADO} y {INVITADOS_EVENTO} de '
       'media.',
    3: 'Mercado en España con fuente: búsquedas mensuales (DataForSEO, octubre 2026): «catering para eventos» 1.000, '
       '«empresa de catering» 590, «catering empresas» 480, «catering bodas» 390; Bodas.net, Informe del Sector '
       'Nupcial 2026: coste medio de la boda 25.183 € y 115 invitados (118 en la generación Z). Estacionalidad del '
       'plan: bodas de mayo a octubre, comuniones en mayo, Navidad de empresa en diciembre, agosto y enero flojos. '
       'Clientes: empresas, agencias, hoteles y fincas sin cocina propia, particulares. NADA de cifras de tamaño del '
       'sector sin fuente.',
    4: 'Competencia: caterings grandes con cocina industrial, restaurantes y hoteles que hacen catering, fincas con '
       'catering exclusivo o que cobran canon al externo, caterings baratos de bandeja. Dónde gana este concepto: show '
       'cooking temático, dietas especiales bien resueltas, flexibilidad de tamaño, precio por invitado claro. Riesgo '
       'de copia y cómo se defiende (marca, recetas propias, relación con planners). Sin cifras de competidores '
       'inventadas.',
    5: 'Captación: wedding planners y fincas (degustaciones, visitas), directorios de bodas (Bodas.net, Zankyou), '
       'LinkedIn y propuesta a empresas, hoteles y agencias, Google Business y reseñas, web con formulario de '
       'presupuesto, Instagram/TikTok con cada evento, ferias de novios, programa de recomendación. Presupuesto de '
       'marketing {MARKETING_ANO} al año más el lanzamiento incluido en la inversión. Política comercial: anticipo del '
       '40 % para bloquear la fecha.',
    6: 'Operaciones de un evento, de la reserva al cobro: briefing (D-60), visita técnica (D-30), presupuesto y '
       'anticipo, menús y alergias cerrados (D-14), compras (D-7 a D-1), producción y mise en place en la cocina central '
       '(D-1), carga con lista por estación, montaje de 60-90 minutos, servicio, recogida, factura en 24-48 h. Cocina '
       'central compartida ({CUOTA_COCINA_MES} al mes), furgoneta frigorífica con certificado ATP, temperaturas del '
       'APPCC (≥ 63 °C en caliente; ≤ 4-8 °C en frío). Política comercial de los contratos del kit: particulares 40 % '
       'al firmar y el resto 7 días antes, cancelación > 21 días sin coste del servicio, 21-7 días 50 %, < 7 días 100 % '
       '(y < 48 h, además, el 50 % del total); empresas 40/30/30 con tramos de 28, 14 y 7 días.',
    7: 'Equipo: cuatro fijos (propietario/a chef y ventas, jefe/a de cocina de producción, ayudante-conductor/a) y una '
       'bolsa de fijos discontinuos (coordinadora-maître, camareros, barra y cocineros de estación): {PLANTILLA_PERSONAS} '
       'personas en plantilla, coste {PERSONAL_A1} ({PERSONAL_PCT_A1} de las ventas), cobertura de horas '
       '{COBERTURA_HORAS}. Fijo discontinuo (art. 16 ET), eventual ≤ 90 días al año (art. 15.2), falso autónomo (art. '
       '1.1). Convenio provincial de hostelería (ALEH V, art. 4). Ratios de sala (estimación del kit): 1 camarero por '
       '10-12 invitados sentados, 1 por 20-25 en cóctel. Formación en higiene, alérgenos, PRL y registro de jornada.',
    8: 'Plan financiero, TODO por token: inversión {INVERSION_TOTAL} (compras {CAPEX} + fondo de maniobra '
       '{FONDO_MANIOBRA}), IVA de la inversión {IVA_INVERSION}, necesidad de caja {NECESIDAD_CAJA}; financiación '
       '{RECURSOS_PROPIOS} propios + préstamo {PRESTAMO} al {TIPO_PRESTAMO}, {PLAZO_PRESTAMO} años con {CARENCIA} de '
       'carencia, cuota {CUOTA_ANUAL}; cuenta de resultados de 3 años ({VENTAS_A1}/{VENTAS_A2}/{VENTAS_A3}; neto '
       '{NETO_A1}/{NETO_A2}/{NETO_A3}); margen bruto {MARGEN_BRUTO_PCT_A1}; equilibrio contable {BE_INVITADOS_EVENTO} '
       'invitados por evento con los {EVENTOS_ANO} eventos del plan, o {BE_EVENTOS_ANO} eventos al año con el evento '
       'medio de {INVITADOS_EVENTO} invitados (ingresos {BE_INGRESOS}); equilibrio de caja {BE_EVENTOS_ANO_CAJA} '
       'eventos; holgura {HOLGURA_CAJA}; DSCR mínimo {DSCR_MIN}; saldo mínimo de tesorería {SALDO_MINIMO} en el mes '
       '{MES_SALDO_MINIMO}; payback {PAYBACK} años; escenarios pesimista ({ESC_PES_EVENTOS} eventos: neto '
       '{ESC_PES_NETO}) y optimista ({ESC_OPT_EVENTOS} eventos: neto {ESC_OPT_NETO}). Los anticipos de particulares no '
       'se modelan: la caja real es algo mejor. El Excel manda: si cambias una celda verde, el documento se queda atrás.',
    9: 'Marco legal verificado (cítalo así): SL unipersonal (capital desde 1 €) o autónomo; IAE 677.9 (su nota incluye '
       'el catering); IVA 10 % del catering con servicio, alcohol incluido (Ley 37/1992, art. 91.Uno.2.2.º), 21 % en '
       'el alcohol del drop-off y en los servicios facturados aparte; registro sanitario autonómico previa declaración '
       'responsable (RD 1021/2022, que reescribe el art. 2 del RD 191/2011; RGSEAA sólo si suministras a otros '
       'establecimientos); prohibido cocinar en casa para eventos (RD 1021/2022, art. 13.5.b); APPCC y formación '
       '(Reglamento (CE) 852/2004), temperaturas (RD 1086/2020, art. 30), alérgenos (Reglamento (UE) 1169/2011 y RD '
       '126/2015), furgoneta ATP (RD 237/2000); personal (ET arts. 1.1, 15.2, 16 y 34.9; convenio provincial); sin '
       'derecho de desistimiento en un servicio de comida con fecha (TRLGDCU, art. 103.l); RGPD/LOPDGDD y LSSI; seguro '
       'de RC con intoxicación alimentaria ≥ 600.000 €; autorizaciones municipales para vía pública y fuego. El último '
       'párrafo: la furgoneta y el transporte.',
    10: 'Conclusiones con tokens (viabilidad, holgura, DSCR, payback), los nueve riesgos del catering y cómo se mitigan '
        '(cancelación, intoxicación, avería del frío, impago de empresa, falta de personal en temporada alta, alergias, '
        'lluvia, competencia barata, coordinación de varias estaciones) y el plan de acción en 6 fases del checklist '
        '(82 tareas: 12/15/14/10/16/15). Cierra con el siguiente paso: completar el Excel con tus cifras.',
}

#: Prohibidos en el texto (SPEC D12 · research §5-D4 · vocabulario del molde FT).
PROHIBIDOS = [
    r'\bfreelance', r'validad[oa]s?', r'Espa[ñn]a,? 2026', r'food ?truck', r'\bcami[oó]n\b', r'ventanilla',
    r'generador', r'\b173 eventos',
    # el ticket de la 1.x (2.200 / 4.500 € por evento); 2.200 € a secas es legítimo (los seguros del caso 2.2)
    r'(ticket|evento)[^.]{0,40}(2\.200|4\.500)|(2\.200|4\.500)\s?€?\s?(/|por)\s?evento', r'10\.560', r'8\.520', r'21\.410', r'54\.440', r'603\.700',
    r'846\.7', r'14 eventos', r'5\.500', r'11\.500', r'4\.585', r'4\.885', r'sin licencia de actividad',
    r'\b38 ?% de (las )?bodas', r'\b58 ?%', r'\b73 ?% (de los )?millennials', r'tarifa plana', r'\bRGSEAA\b(?!.{0,80}(s[oó]lo|otros establecimientos))',
]
#: Cifras que el texto puede llevar escritas (normas, política comercial, research con fuente, mezcla del plan).
PERMITIDAS = set('''1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 18 20 21 23 24 25 26 28 30 31 32 33 34 35 38 40 45 48 50 60 62
63 65 70 80 82 90 98 100 110 115 118 120 126 150 191 237 390 347 349 390 480 590 852 1.000 1.086 1.021 1.169 1.175
1.007 600.000 3.005,06 2026 2025 2011 2022 2020 2015 2000 2004 2007 2010 2013 1992 1990 1995 2023 25.183 677.9 677
91 13.5 103 16,0 1.1 15.2 34.9 56.21'''.split())
RX_NUM = re.compile(r'(?<![\w{])\d[\d.,]*\d|(?<![\w{])\d')


def ranuras():
    d = json.load(open(os.path.join(BP4, 'docx_es_cat.json'), encoding='utf-8'))['parrafos']
    en = {}
    for t in ('cat_a', 'cat_b'):
        en.update(json.load(open(os.path.join(BP4, 'docx_en_%s.json' % t), encoding='utf-8')))
    fuera = []
    for k in sorted(d, key=int):
        v = d[k]
        if v['rol'] != 'cuerpo':
            continue
        sec = int(v['seccion'])
        fuera.append({'i': int(k), 'seccion': sec, 'palabras_objetivo': int(v['palabras']),
                      'molde_ft_es': v['texto'], 'gemela_en_catering': en.get(k, '')})
    return fuera


def preparar():
    cif = json.load(open(CIFRAS, encoding='utf-8'))['tokens'] if os.path.exists(CIFRAS) else {}
    fuente = json.load(open(os.path.join(BP4, 'fuente_es_cat.json'), encoding='utf-8'))['plan_docx_es']
    material = [p.get('texto', p) if isinstance(p, dict) else p for p in (fuente.get('parrafos') or [])]
    os.makedirs(TANDAS, exist_ok=True)
    rs = ranuras()
    for tanda, secs in (('cat_es_a', range(1, 6)), ('cat_es_b', range(6, 11))):
        sel = [r for r in rs if r['seccion'] in secs]
        ent = {
            'tanda': tanda, 'producto': 'Plan de Negocio Catering Temático Eventos ES 2.0 (aichef.pro, 45 €)',
            'salida': 'scripts/productos-digitales/catering-es-2_0/textos/%s.json' % tanda,
            'formato_salida': '{"<i>": "<párrafo en español>", …} con TODOS los "i" de "parrafos" y nada más',
            'brief': 'scripts/productos-digitales/catering-es-2_0/BRIEF-REDACTORES.md (léelo entero antes)',
            'secciones': dict((s, {'titulo': SECCIONES[s], 'pista': PISTAS[s]}) for s in secs),
            'n_parrafos': len(sel), 'n_palabras_objetivo': sum(r['palabras_objetivo'] for r in sel),
            'tokens': cif,
            'material_catering_1x (docx anterior: SOLO contenido; sus cifras están prohibidas)': material,
            'parrafos': sel,
        }
        p = os.path.join(TANDAS, tanda + '.entrada.json')
        json.dump(ent, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('%s: %d ranuras · %d palabras objetivo · %d tokens → %s' % (
            tanda, len(sel), ent['n_palabras_objetivo'], len(cif), os.path.relpath(p, AQUI)))


def check(tanda):
    ent = json.load(open(os.path.join(TANDAS, tanda + '.entrada.json'), encoding='utf-8'))
    sal = json.load(open(os.path.join(TEXTOS, tanda + '.json'), encoding='utf-8'))
    tokens = set(ent['tokens'])
    err, avi = [], []
    esperadas = set(str(r['i']) for r in ent['parrafos'])
    if set(sal) != esperadas:
        err.append('ranuras: faltan %s · sobran %s' % (sorted(esperadas - set(sal)), sorted(set(sal) - esperadas)))
    total = 0
    for r in ent['parrafos']:
        t = sal.get(str(r['i']), '')
        n = len(t.split())
        total += n
        if not (0.7 * r['palabras_objetivo'] <= n <= 1.35 * r['palabras_objetivo']):
            avi.append('%d: %d palabras (objetivo %d)' % (r['i'], n, r['palabras_objetivo']))
        for tok in re.findall(r'\{([A-Z0-9_]+)\}', t):
            if tok not in tokens:
                err.append('%d: token inexistente {%s}' % (r['i'], tok))
        for rx in PROHIBIDOS:
            if re.search(rx, t, re.I):
                err.append('%d: prohibido /%s/' % (r['i'], rx))
        sin_tok = re.sub(r'\{[A-Z0-9_]+\}', '', t)
        for num in RX_NUM.findall(sin_tok):
            if num.rstrip('.,') not in PERMITIDAS:
                avi.append('%d: cifra escrita «%s» (¿debería ser token o tiene fuente?)' % (r['i'], num))
        if re.search(r'[^\x00-ɏ‐-‧€°→ ‑«»¿¡ºª·…–—“”‘’]', t):
            err.append('%d: caracteres no latinos' % r['i'])
        if '\n' in t or t.strip().startswith(('-', '•', '*', '#')):
            err.append('%d: el párrafo no puede llevar saltos, viñetas ni Markdown' % r['i'])
    for x in err:
        print('ERROR', x)
    for x in avi:
        print('AVISO', x)
    print('%s: %d párrafos, %d palabras (objetivo %d) · %s (%d errores, %d avisos)' % (
        tanda, len(sal), total, ent['n_palabras_objetivo'], 'OK' if not err else 'ROJO', len(err), len(avi)))
    return 1 if err else 0


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('accion', choices=('preparar', 'check'))
    ap.add_argument('--tanda')
    a = ap.parse_args()
    sys.exit(preparar() or 0 if a.accion == 'preparar' else check(a.tanda))
