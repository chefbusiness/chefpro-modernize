#!/usr/bin/env python3
"""
tandas_docx.py — Paellero ES 2.2 (SPEC D11): prepara y valida las dos tandas de redacción del plan de negocio (docx).
Copia adaptada de `catering-es-2_0/tandas_docx.py`.

Las 61 ranuras de texto del docx del Food Truck ES (131 párrafos, 10 Heading 1; mapa en
`business-plans-en-4/docx_es_cat.json`) se escriben NUEVAS, en español, para el paellero:
  pae_es_a = §1-5 (29 ranuras) · pae_es_b = §6-10 (32 ranuras).
Gemela de argumento: el texto del Catering ES 2.2 en la misma ranura (`catering-es-2_0/textos/cat_es_{a,b}.json`).
Material: el docx de la 1.2 (`fuente_pae_12.json`, sólo contenido; sus cifras están prohibidas).
Las cifras del Excel van SIEMPRE como token {ASI} (`cifras_caso_es.json`); `docx_pae_es.py` las resuelve al ensamblar.
Sólo lee JSON: corre en el Mac.

    python3 tandas_docx.py preparar                       # tandas/pae_es_{a,b}.entrada.json
    python3 tandas_docx.py check --tanda pae_es_a         # valida textos/pae_es_a.json (salida del redactor)

Sesión Claude Code, 11-oct-2026.
"""
import argparse
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BP4 = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
CAT = os.path.join(os.path.dirname(AQUI), 'catering-es-2_0', 'textos')
TANDAS, TEXTOS = os.path.join(AQUI, 'tandas'), os.path.join(AQUI, 'textos')
CIFRAS = os.path.join(AQUI, 'cifras_caso_es.json')

SECCIONES = {
    1: '1. Resumen Ejecutivo', 2: '2. Concepto y Propuesta de Valor', 3: '3. Análisis de Mercado',
    4: '4. Análisis Competitivo', 5: '5. Plan de Marketing y Captación', 6: '6. Plan de Operaciones',
    7: '7. Estructura Organizativa y RRHH', 8: '8. Plan Financiero', 9: '9. Aspectos Legales y Licencias',
    10: '10. Conclusiones y Plan de Acción',
}

#: Lo que tiene que contar cada sección (español de España, para el mercado español). Cifras del Excel = tokens.
_MEZCLA = ('15 bodas, preboda y cenas de paellas en finca de 120 invitados a 28 € (dos variedades y entrantes); 30 '
           'comidas de empresa, team building y Navidad de 70 invitados a 24 €; 50 fiestas privadas (cumpleaños, '
           'comuniones, peñas, urbanizaciones) de 40 invitados a 18 €; 10 fiestas populares de ayuntamientos o '
           'comisiones de 400 raciones a 5 €; precios por ración sin IVA')
PISTAS = {
    1: 'Qué es el negocio: paella y arroces cocinados EN DIRECTO en el evento (gas y leña donde se pueda), con show '
       'cooking, sin local propio: una SL unipersonal con una cocina de apoyo compartida y autorizada para caldos y '
       'preparación, una furgoneta isoterma y un ayudante y dos auxiliares fijos discontinuos. Cuatro clientes: bodas, '
       'empresas, fiestas privadas y fiestas populares. Cifras clave por token: {EVENTOS_ANO} eventos de '
       '{INVITADOS_EVENTO} invitados de media a {PRECIO_INVITADO} por ración sin IVA (es una MEDIA que baja por las '
       'fiestas populares: no es el precio de una boda), ventas {VENTAS_A1}, resultado neto {NETO_A1}, inversión '
       '{INVERSION_TOTAL}, préstamo {PRESTAMO} y equilibrio en {BE_EVENTOS_ANO} eventos al año. Qué contiene el kit '
       '(Excel de 9 hojas, checklist de 83 tareas, calculadora de precios, contratos, carta de 12 arroces, 10 '
       'experiencias, manual técnico, catálogo, 88 proveedores, guía de sistemas de cocción y roadmap food truck).',
    2: 'La propuesta: el ritual de la paella hecho delante del invitado (sofrito, caldo, socarrat) como experiencia, '
       'la carta de 12 arroces y las 10 experiencias del kit, arroz y producto con denominación de origen, alérgenos '
       'resueltos, puntualidad y limpieza. La mezcla de cuatro tipos de evento del plan (tabla de Instrucciones del '
       'Excel: ' + _MEZCLA + ') y por qué da {PRECIO_INVITADO} y {INVITADOS_EVENTO} de media. La paella para recoger '
       '(sin servicio) es un 5 % de las ventas.',
    3: 'Mercado en España con fuente: búsquedas mensuales (DataForSEO, octubre 2026): «paellas a domicilio» 1.900, '
       '«paellas gigantes» 390, «catering paellas» 170, «paella para eventos» 110; la demanda es del cliente que '
       'busca proveedor. Precios de referencia con fuente: paella sola para grupos 11-14 € por persona (tarifa '
       'publicada de un proveedor de Cataluña, 2026), paella en directo con experiencia 20-39 €, paella gigante 3-10 € '
       'por invitado (Bodas.net), fiesta popular de Sayalonga 2025: 400 raciones por 1.480 € (Plataforma de '
       'Contratación del Sector Público). Estacionalidad del plan: mayo-octubre (bodas, comuniones y fiestas '
       'patronales de agosto y septiembre), Navidad de empresa; enero, febrero y noviembre flojos; Fallas sólo en el '
       'Levante. NADA de cifras de tamaño del sector sin fuente (fuera los 3.200 M€ y porcentajes de la versión '
       'anterior).',
    4: 'Competencia por categorías (sin nombres de empresas ni cifras inventadas): paelleros tradicionales sin marca, '
       'caterings generalistas que ponen la paella como un plato más, marketplaces y directorios de paelleros, '
       'restaurantes de arroces que hacen eventos, proveedores de paella gigante por volumen. Dónde gana este '
       'concepto: show cooking con narrativa, carta de 12 arroces, producto con DO, contrato y seguro profesionales, '
       'precio por ración claro por tipo de evento. Riesgo de guerra de precios en la paella sola y cómo se defiende.',
    5: 'Captación: wedding planners y fincas (degustación en directo), directorios de bodas (Bodas.net, Zankyou), '
       'directorios de eventos para empresas y Hosply, LinkedIn y agencias, ayuntamientos y comisiones de fiestas '
       '(contrato menor y Plataforma de Contratación), Google Business y reseñas, web con formulario de presupuesto, '
       'Instagram/TikTok con cocciones reales. Presupuesto de marketing {MARKETING_ANO} al año más el lanzamiento '
       'incluido en la inversión. Política comercial: anticipo del 30 % para bloquear la fecha.',
    6: 'Operaciones de un evento, de la reserva al cobro: briefing (D-30), visita técnica (D-21, punto de fuego, '
       'viento, agua, franja forestal), presupuesto y anticipo del 30 %, menú y alergias (D-7), pedidos y marisco el '
       'día antes, caldos y mise en place en la cocina de apoyo (nunca en casa), carga con la lista del manual, montaje '
       'y encendido, cocción y show cooking, servicio a 63 °C o más, recogida y fotos, factura. Escalado del manual: '
       'raciones por diámetro (90 cm: 30-40; 120 cm: 60-80; 150 cm: 90-120; 100 g de arroz por ración), un paellero '
       'hasta 3 paelleras, ayudante desde 4 paelleras u 80 invitados, segundo paellero desde unos 150. Cocina de apoyo '
       '({CUOTA_COCINA_MES} al mes), furgoneta isoterma con ATP, gas: una botella de menos de 15 kg por quemador. '
       'Política comercial de los contratos del kit: particulares 30 % al firmar y 70 % el día del evento (en efectivo '
       'sólo hasta 1.000 €), cancelación del cliente 30 % del total con más de 60 días, 50 % entre 60 y 30, 75 % con '
       'menos de 30 y 100 % en las 72 horas previas (simétrica si cancela el paellero); empresas 30 % y 70 % a 30 días '
       'de la factura, con retención del 0, 30 o 60 % del anticipo (más 200 € de gestión) y 100 % a menos de 15 días.',
    7: 'Equipo: el propietario/a paellero titular a jornada completa, un ayudante y segundo paellero fijo discontinuo '
       'al 65 % y dos auxiliares de evento fijos discontinuos para bodas y fiestas populares: {PLANTILLA_PERSONAS} '
       'personas, coste {PERSONAL_A1} ({PERSONAL_PCT_A1} de las ventas), cobertura de horas {COBERTURA_HORAS}. Fijo '
       'discontinuo (art. 16 ET), falso autónomo (art. 1.1), registro de jornada (art. 34.9), convenio provincial de '
       'hostelería (ALEH V, art. 4). Formación en higiene alimentaria a cargo de la empresa (el carné de manipulador '
       'ya no existe), alérgenos, PRL (quemaduras, gas, calor) y guion del show cooking.',
    8: 'Plan financiero, TODO por token: inversión {INVERSION_TOTAL} (compras {CAPEX} + fondo de maniobra '
       '{FONDO_MANIOBRA}), IVA de la inversión {IVA_INVERSION}, necesidad de caja {NECESIDAD_CAJA}; financiación '
       '{RECURSOS_PROPIOS} propios + préstamo {PRESTAMO} al {TIPO_PRESTAMO}, {PLAZO_PRESTAMO} años con {CARENCIA} de '
       'carencia, cuota {CUOTA_ANUAL}; cuenta de resultados de 3 años ({VENTAS_A1}/{VENTAS_A2}/{VENTAS_A3}; neto '
       '{NETO_A1}/{NETO_A2}/{NETO_A3}); margen bruto {MARGEN_BRUTO_PCT_A1}. CRECIMIENTO, contado tal cual lo hace el '
       'Excel: los ingresos crecen con el volumen, no con el precio: sube un {CREC_A2} y un {CREC_A3} las raciones '
       'por evento (de {INVITADOS_EVENTO} a {INVITADOS_EVENTO_A2} y {INVITADOS_EVENTO_A3}) con los mismos '
       '{EVENTOS_ANO} eventos y el mismo precio. Equilibrio contable {BE_INVITADOS_EVENTO} invitados por evento con los '
       'eventos del plan, o {BE_EVENTOS_ANO} eventos al año con el evento medio (ingresos {BE_INGRESOS}); equilibrio de '
       'caja {BE_EVENTOS_ANO_CAJA} eventos y holgura {HOLGURA_CAJA}, que es la del PRIMER año (sólo intereses por la '
       'carencia); desde el segundo, con la devolución del principal, el equilibrio de caja sube a '
       '{BE_INGRESOS_CAJA_A2}: el crecimiento lo cubre con una holgura de {HOLGURA_CAJA_A2}, pero sin crecer harían '
       'falta unos {BE_EVENTOS_CAJA_A2} eventos. DSCR mínimo {DSCR_MIN}; saldo mínimo de tesorería {SALDO_MINIMO} en el '
       'mes {MES_SALDO_MINIMO}; payback {PAYBACK} años; escenarios pesimista ({ESC_PES_EVENTOS} eventos: neto '
       '{ESC_PES_NETO}) y optimista ({ESC_OPT_EVENTOS} eventos: neto {ESC_OPT_NETO}). Los anticipos de particulares no '
       'se modelan: la caja real es algo mejor. A los proveedores se les paga a 20 días y las nóminas cada mes. El '
       'Excel manda: si cambias una celda verde, el documento se queda atrás.',
    9: 'Marco legal verificado (cítalo así): SL unipersonal (capital desde 1 €) o autónomo; IAE 677.9; IVA 10 % del '
       'servicio de comidas en el evento, alcohol incluido (Ley 37/1992, art. 91.Uno.2.2.º), 21 % en el alcohol de '
       'la paella para recoger y en lo facturado aparte; registro sanitario autonómico previa declaración responsable '
       '(RD 1021/2022, que reescribe el art. 2 del RD 191/2011; RGSEAA sólo si suministras a otros establecimientos); '
       'prohibido preparar en casa para eventos (RD 1021/2022, art. 13.5.b); APPCC y formación (Reglamento (CE) '
       '852/2004), temperaturas (RD 1086/2020, art. 30), alérgenos (Reglamento (UE) 1169/2011 y RD 126/2015); GAS: '
       'una botella de menos de 15 kg conectada a un solo aparato no es instalación y la conecta el usuario con '
       'regulador y tubo flexible (RD 919/2006, art. 2.1.h; ITC-ICG 08), botellas de 35 kg o en batería las monta una '
       'empresa instaladora (ITC-ICG 06), transporte de hasta 333 kg de gas por vehículo en la exención del ADR '
       '(1.1.3.6) con extintor; FUEGO: lo regula cada comunidad en montes y zonas colindantes (Ley 43/2003, art. '
       '44.3), con franja y época de peligro, y una alerta puede prohibir también el gas: cláusula de fuerza mayor y '
       'plan B (ver el anexo por comunidades); FIESTAS POPULARES: contrato menor (Ley 9/2017, art. 118), pago a 30 '
       'días (art. 198.4), factura electrónica por FACe si eres SL (Ley 25/2013, art. 4); vender raciones al público '
       'por tu cuenta es venta no sedentaria con autorización municipal (Ley 7/1996, arts. 53-54); personal (ET '
       'arts. 1.1, 16 y 34.9); sin derecho de desistimiento en un servicio de comida con fecha (TRLGDCU, art. '
       '103.l); efectivo con particulares hasta 1.000 € (Ley 7/2012, art. 7); RGPD/LOPDGDD y LSSI; seguro de RC con '
       'incendio, explosión e intoxicación alimentaria ≥ 600.000 €. El último párrafo: la furgoneta (ATP, RD '
       '237/2000) y el transporte de las botellas.',
    10: 'Conclusiones con tokens (viabilidad, holgura del año 1 y del año 2, DSCR, payback), los riesgos del paellero '
        'y cómo se mitigan (prohibición de fuego por alerta de incendios, lluvia y viento, intoxicación y arroz '
        'tibio, accidente con el gas, avería o robo del equipo, impago o retraso de un ayuntamiento, dependencia de '
        'pocos planners, subida del arroz y del marisco, falta de ayudantes en temporada alta) y el plan de acción en '
        '6 fases del checklist (83 tareas: 12/16/14/10/16/15). Cierra con el siguiente paso: completar el Excel con '
        'tus cifras.',
}

#: Prohibidos en el texto (SPEC D11 y D15 · cifras y errores de la 1.2 · restos del molde FT y del catering).
PROHIBIDOS = [
    r'\bfreelance', r'validad[oa]s?', r'Espa[ñn]a,? 2026', r'(?<!roadmap )food ?truck', r'\bcami[oó]n\b',
    r'ventanilla', r'generador', r'cocina central', r'estaci[oó]n(es)? tem[aá]tica', r'catering tem[aá]tico',
    r'drop-?off', r'carn[eé]t? de manipulador(?! ya no existe)', r'sin licencia', r'tarifa plana', r'solopreneur',
    r'\bRGSEAA\b(?!.{0,80}(s[oó]lo|otros establecimientos))', r'PATRICOVA', r'INFOCYL', r'PIDOM',
    r'excepci[oó]n cultural', r'3\.790', r'9\.670', r'23\.110', r'3\.500', r'8\.500', r'214\.950', r'215\.000',
    r'245\.000', r'109\.822', r'47\.000', r'62\.000', r'10,18', r'18-22 eventos', r'\b51 ?%', r'80 ?€ ?(/|al) ?mes',
    r'120 ?€ ?(/|por) ?jornada', r'4-7 veces', r'3\.200 M', r'\b38 ?% de (las )?bodas',
]
#: Cifras que el texto puede llevar escritas (normas, política comercial, research con fuente, mezcla del plan).
PERMITIDAS = set('''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 18 20 21 24 25 26 28 30 31 34 35 38 39 40 44 45 50 53 54 60 63 65
70 72 75 80 83 88 90 91 100 103 110 118 120 126 150 170 191 198 200 237 333 347 390 400 426 500 513 677 852 919 1.000
1.021 1.086 1.169 1.175 1.480 1.900 600.000 3.005,06 2026 2025 2022 2020 2017 2016 2015 2013 2012 2011 2006 2004 2003
2000 1996 1995 1992 1990 677.9 13.5 2.1 44.3 198.4 1.1 34.9 1.1.3.6 06 08 3,70 11-14 20-39 3-10 3-6 30-40 60-80 90-120
12/16/14/10/16/15'''.split())
RX_NUM = re.compile(r'(?<![\w{])\d[\d.,]*\d|(?<![\w{])\d')


def ranuras():
    d = json.load(open(os.path.join(BP4, 'docx_es_cat.json'), encoding='utf-8'))['parrafos']
    gem = {}
    for t in ('cat_es_a', 'cat_es_b'):
        gem.update(json.load(open(os.path.join(CAT, t + '.json'), encoding='utf-8')))
    fuera = []
    for k in sorted(d, key=int):
        v = d[k]
        if v['rol'] != 'cuerpo':
            continue
        sec = int(v['seccion'])
        fuera.append({'i': int(k), 'seccion': sec, 'palabras_objetivo': int(v['palabras']),
                      'molde_ft_es': v['texto'], 'gemela_catering_es': gem.get(k, '')})
    return fuera


def preparar():
    cif = json.load(open(CIFRAS, encoding='utf-8'))['tokens'] if os.path.exists(CIFRAS) else {}
    fuente = json.load(open(os.path.join(AQUI, 'fuente_pae_12.json'), encoding='utf-8'))
    material = [p['texto'] for p in fuente['parrafos']] + [' | '.join(f) for t in fuente['tablas'] for f in t]
    os.makedirs(TANDAS, exist_ok=True)
    rs = ranuras()
    for tanda, secs in (('pae_es_a', range(1, 6)), ('pae_es_b', range(6, 11))):
        sel = [r for r in rs if r['seccion'] in secs]
        ent = {
            'tanda': tanda, 'producto': 'Plan de Negocio Paellero / Paella para Eventos ES 2.2 (aichef.pro, 45 €)',
            'salida': 'scripts/productos-digitales/paellero-2_2/textos/%s.json' % tanda,
            'formato_salida': '{"<i>": "<párrafo en español>", …} con TODOS los "i" de "parrafos" y nada más',
            'brief': 'scripts/productos-digitales/paellero-2_2/BRIEF-REDACTORES.md (léelo entero antes)',
            'secciones': dict((s, {'titulo': SECCIONES[s], 'pista': PISTAS[s]}) for s in secs),
            'n_parrafos': len(sel), 'n_palabras_objetivo': sum(r['palabras_objetivo'] for r in sel),
            'tokens': cif,
            'material_paellero_1_2 (docx anterior: SOLO contenido; sus cifras están prohibidas)': material,
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
