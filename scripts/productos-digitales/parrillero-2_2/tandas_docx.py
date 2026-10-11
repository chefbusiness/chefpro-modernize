#!/usr/bin/env python3
"""
tandas_docx.py — Parrillero / Asador ES 2.2 (SPEC D11): prepara y valida las dos tandas de redacción del plan de negocio
(docx). Copia adaptada de `paellero-2_2/tandas_docx.py`.

Las 61 ranuras de texto del docx del Food Truck ES (131 párrafos, 10 Heading 1; mapa en
`business-plans-en-4/docx_es_cat.json`) se escriben NUEVAS, en español, para el parrillero:
  par_es_a = §1-5 (29 ranuras) · par_es_b = §6-10 (32 ranuras).
Gemela de argumento: el texto del Paellero ES 2.2 en la misma ranura (`paellero-2_2/textos/pae_es_{a,b}.json`).
Material: el docx de la 1.1 (`fuente_par_11.json`, sólo contenido; sus cifras están prohibidas).
Las cifras del Excel van SIEMPRE como token {ASI} (`cifras_caso_es.json`); `docx_par_es.py` las resuelve al ensamblar.
Sólo lee JSON: corre en el Mac.

    python3 tandas_docx.py preparar                       # tandas/par_es_{a,b}.entrada.json
    python3 tandas_docx.py check --tanda par_es_a         # valida textos/par_es_a.json (salida del redactor)

Sesión Claude Code, 12-oct-2026.
"""
import argparse
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BP4 = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
PAE = os.path.join(os.path.dirname(AQUI), 'paellero-2_2', 'textos')
TANDAS, TEXTOS = os.path.join(AQUI, 'tandas'), os.path.join(AQUI, 'textos')
CIFRAS = os.path.join(AQUI, 'cifras_caso_es.json')

SECCIONES = {
    1: '1. Resumen Ejecutivo', 2: '2. Concepto y Propuesta de Valor', 3: '3. Análisis de Mercado',
    4: '4. Análisis Competitivo', 5: '5. Plan de Marketing y Captación', 6: '6. Plan de Operaciones',
    7: '7. Estructura Organizativa y RRHH', 8: '8. Plan Financiero', 9: '9. Aspectos Legales y Licencias',
    10: '10. Conclusiones y Plan de Acción',
}

#: Lo que tiene que contar cada sección (español de España, para el mercado español). Cifras del Excel = tokens.
_MEZCLA = ('12 bodas, prebodas y eventos en finca de 110 invitados a 42 € (entrantes, tres o cuatro cortes con vacuno '
           'madurado, guarniciones y postre a la brasa); 30 eventos de empresa (comidas, team building, show cooking y '
           'Navidad) de 70 invitados a 31 €; 45 celebraciones privadas (cumpleaños, comuniones, peñas, urbanizaciones) '
           'de 40 invitados a 25 €; 8 fiestas o ferias por encargo de un ayuntamiento o una comisión (chuletada o '
           'costillada de 300 g) de 300 invitados a 10 €; precios por invitado sin IVA')
PISTAS = {
    1: 'Qué es el negocio: parrilla y asado cocinados EN DIRECTO en el evento, con carbón y leña y un plan B de gas '
       'para cuando una alerta de incendios prohíbe la brasa, y show de fuego; multi-concepto (asado argentino, '
       'cordero a la cruz, parrilla uruguaya, BBQ texano, rodizio, asador criollo-castellano, parrilla mediterránea, '
       'llanera, show de fuego y brunch de empresa); sin local propio: una SL unipersonal con una cocina de apoyo '
       'compartida y autorizada para marinados, salmueras, porcionado y cámara de la carne, una furgoneta '
       'frigorífica con ATP, un remolque-parrilla con cruz, un segundo parrillero y dos auxiliares fijos '
       'discontinuos. Cuatro clientes: bodas, empresas, celebraciones privadas y fiestas o ferias. Cifras clave por '
       'token: {EVENTOS_ANO} eventos de {INVITADOS_EVENTO} invitados de media a {PRECIO_INVITADO} por invitado sin '
       'IVA (es una MEDIA que baja por las fiestas: no es el precio de una boda), ventas {VENTAS_A1}, resultado neto '
       '{NETO_A1}, inversión {INVERSION_TOTAL}, préstamo {PRESTAMO} y equilibrio en {BE_EVENTOS_ANO} eventos al '
       'año. Qué contiene el kit (Excel de 9 hojas, checklist de 83 tareas, calculadora de presupuestos con IVA, '
       'contratos para particulares y empresas, carta de 12 cortes, 10 experiencias, manual técnico con la tabla de '
       'escalado por invitados, catálogo de equipamiento, 93 proveedores y guía de 8 sistemas con el roadmap food '
       'truck).',
    2: 'La propuesta: el fuego y el corte hechos delante del invitado como experiencia (la brasa, el punto con '
       'sonda, el corte en mesa, el cordero girando en la cruz), la carta de 12 cortes y las 10 experiencias del kit, '
       'carne con trazabilidad (la denominación de la etiqueta: ternera, añojo o vaca; «madurada» sólo con el '
       'documento del proveedor), alérgenos resueltos, plan B de gas, puntualidad y limpieza (brasas y cenizas '
       'recogidas). La mezcla de cuatro tipos de evento del plan (tabla de Instrucciones del Excel: ' + _MEZCLA + ') y '
       'por qué da {PRECIO_INVITADO} y {INVITADOS_EVENTO} de media. El asado para llevar (bandejas de cordero, '
       'cochinillo o costillar sin servicio) es un 5 % de las ventas. El show cooking por jornada en un restaurante '
       'es una línea extra que el plan NO cuenta en su caso: menciónala sin cifras.',
    3: 'Mercado en España con fuente: búsquedas mensuales (DataForSEO, octubre de 2026): «parrillero» 590 (ambigua: '
       'también es el oficio y el empleo), «barbacoa a domicilio» 320, «asador a domicilio» 140, «cordero a la '
       'cruz» 140, «parrillada a domicilio» 90, «catering barbacoa» 90, «parrillero para eventos» 70 y «asado '
       'argentino a domicilio» 70: unas 1.000 búsquedas al mes de clientes que buscan proveedor. Precios de '
       'referencia con fuente: barbacoa para eventos 18-30 € por persona la básica, 30-55 € la completa y 55-90 € '
       'la premium con servicio de mesa (directorio artistealo, sin indicar si lleva IVA); buffet de barbacoa en '
       'Madrid a 15,95-19,95 € más IVA desde 50 personas con 500 g de carne cruda (tarifa publicada de un '
       'proveedor); asado argentino para bodas a 40-100 € por invitado (ficha de un proveedor en Bodas.net). '
       'Estacionalidad del plan: de mayo a octubre con el pico en septiembre, la Navidad de empresa y el cordero o '
       'cochinillo a la cruz en diciembre; agosto pierde por el calor y la época de peligro de incendios; enero, '
       'febrero y noviembre son los meses bajos. El hueco: nadie explica la finca en zona forestal, la brasa en época '
       'de peligro con su plan B de gas ni las temperaturas de la carne. NADA de tamaño del sector sin fuente (fuera '
       'los millones de euros, los porcentajes de crecimiento y las bodas al año de la versión anterior).',
    4: 'Competencia por categorías (sin nombres de empresas ni cifras inventadas): parrilleros independientes sin '
       'marca, contrato ni seguro; caterings generalistas que ponen la barbacoa como un plato más; proveedores de '
       'buffet de barbacoa por volumen; directorios y marketplaces de eventos; asadores con local que salen a '
       'eventos; cadenas con una página por ciudad. Dónde gana este concepto: show de fuego y corte en directo, carta '
       'de 12 cortes y 10 experiencias, trazabilidad de la carne, contrato y seguro con incendio, plan B de gas, '
       'precio por invitado claro por tipo de evento. Riesgo de guerra de precios en la barbacoa básica (18-30 € por '
       'persona) y cómo se defiende.',
    5: 'Captación: wedding planners y fincas (degustación en directo), directorios de bodas (Bodas.net, Zankyou), '
       'directorios de eventos para empresas y Hosply, LinkedIn y agencias, ayuntamientos y comisiones de fiestas '
       '(encargo por contrato menor y Plataforma de Contratación), Google Business y reseñas, web con formulario de '
       'presupuesto y unas preguntas frecuentes que respondan lo que se busca (¿se puede hacer una barbacoa en una '
       'finca privada?, ¿cuánto cuesta un asado para 50 personas?, ¿qué pasa si hay alerta de incendios?), '
       'Instagram/TikTok con cocciones reales. Presupuesto de marketing {MARKETING_ANO} al año más el lanzamiento '
       'incluido en la inversión. Política comercial: señal del 30 % para bloquear la fecha.',
    6: 'Operaciones de un evento, de la reserva al cobro: briefing (D-30); visita técnica (D-21: punto de fuego, '
       'viento y humo, carpas a 3 m o más de la parrilla, agua, terreno forestal o su franja); presupuesto y señal '
       'del 30 %; menú y alergias (D-7); pedido de carne (5-7 días antes) y recepción con sonda: carne a 7 °C o '
       'menos, despojos a 3 °C, aves y preparados a 4 °C y picada a 2 °C (Reglamento (CE) 853/2004, como estándar '
       'del APPCC); marinados, salmueras y porcionado en la cocina de apoyo, nunca en casa; carga, montaje y brasa '
       '(45-60 minutos); cocción con sonda: 70 °C en el centro de la carne y 74 °C en las aves (recomendación de '
       'AESAN), «poco hecho» sólo en piezas enteras de vacuno o cordero y a petición; lo caliente a 63 °C o más y '
       'comida testigo; brasas y cenizas apagadas con agua en un contenedor metálico; factura. Escalado del manual: '
       '350-450 g de carne cruda por invitado con entrantes (500-600 g sin entrantes), una parrilla de 120 cm y un '
       'parrillero por cada 60-80 invitados (40-50 con cortes en mesa), ayudante desde 40 invitados, 0,7-1 kg de '
       'carbón por kg de carne, un cordero de 10-12 kg da 15-20 raciones. Cocina de apoyo ({CUOTA_COCINA_MES} al '
       'mes), furgoneta frigorífica con ATP, remolque-parrilla ({REMOLQUE}), plan B de gas ({PLAN_B_GAS}): una '
       'botella de menos de 15 kg por aparato. Chuletón con vértebra sólo de vacuno de origen de riesgo '
       'insignificante (España) o de menos de 30 meses, y nunca deshuesado por el parrillero (RD 1086/2020, art. '
       '26.2). Política comercial de los contratos del kit: particulares 30 % de señal al firmar, 40 % siete días '
       'antes y 30 % en las 48 horas siguientes (en efectivo, sólo por debajo de 1.000 €; factura de cada pago); si '
       'cancela el cliente, con 60 días o más se retiene la señal, de 30 a 59 días el 50 % del total, de 7 a 29 '
       'días el 75 % y con menos de 7 el 100 %; si cancela el parrillero, devuelve todo más un 10 %; empresas: 30 % '
       'al confirmar y 70 % a 30 días de la factura, con cancelación del 20, 50, 75 o 100 % (30 días o más, 15-29, '
       '7-14 y menos de 7); los ayuntamientos no adelantan nada.',
    7: 'Equipo: el propietario/a parrillero titular a jornada completa, un segundo parrillero fijo discontinuo al '
       '30 % de jornada y dos auxiliares fijos discontinuos al 32 % (parrilla y montaje; servicio y emplatado): '
       '{PLANTILLA_PERSONAS} personas, coste {PERSONAL_A1} ({PERSONAL_PCT_A1} de las ventas), cobertura de horas '
       '{COBERTURA_HORAS}. Fijo discontinuo (art. 16 ET), falso autónomo (art. 1.1), registro de jornada (art. 34.9), '
       'convenio provincial de hostelería (ALEH V, art. 4). Formación en higiene alimentaria a cargo de la empresa '
       '(el carné de manipulador ya no existe), con carne cruda, temperaturas y alérgenos; PRL (quemaduras, humo, '
       'calor y cargas); guion del show de fuego (flambeados sólo con extintor a mano y nunca en alerta); segundo '
       'parrillero en los eventos grandes según la tabla de escalado.',
    8: 'Plan financiero, TODO por token: inversión {INVERSION_TOTAL} (compras {CAPEX} + fondo de maniobra '
       '{FONDO_MANIOBRA}), IVA de la inversión {IVA_INVERSION}, necesidad de caja {NECESIDAD_CAJA}; financiación '
       '{RECURSOS_PROPIOS} propios + préstamo {PRESTAMO} al {TIPO_PRESTAMO}, {PLAZO_PRESTAMO} años con {CARENCIA} de '
       'carencia, cuota {CUOTA_ANUAL}; cuenta de resultados de 3 años ({VENTAS_A1}/{VENTAS_A2}/{VENTAS_A3}; neto '
       '{NETO_A1}/{NETO_A2}/{NETO_A3}); margen bruto {MARGEN_BRUTO_PCT_A1}, mercancía {MERCANCIA_PCT_A1}. '
       'CRECIMIENTO, contado tal cual lo hace el Excel: los ingresos crecen con el volumen, no con el precio: sube un '
       '{CREC_A2} y un {CREC_A3} los invitados por evento (de {INVITADOS_EVENTO} a {INVITADOS_EVENTO_A2} y '
       '{INVITADOS_EVENTO_A3}) con los mismos {EVENTOS_ANO} eventos y el mismo precio. Equilibrio contable '
       '{BE_INVITADOS_EVENTO} invitados por evento con los eventos del plan, o {BE_EVENTOS_ANO} eventos al año con el '
       'evento medio de {TICKET_EVENTO} (ingresos {BE_INGRESOS}); equilibrio de caja {BE_EVENTOS_ANO_CAJA} eventos y '
       'holgura {HOLGURA_CAJA}, que es la del PRIMER año (sólo intereses por la carencia); desde el segundo, con la '
       'devolución del principal, el equilibrio de caja sube a {BE_INGRESOS_CAJA_A2} y la holgura baja a '
       '{HOLGURA_CAJA_A2} (sin crecer harían falta unos {BE_EVENTOS_CAJA_A2} eventos) y en el tercero a '
       '{HOLGURA_CAJA_A3} ({BE_EVENTOS_CAJA_A3} eventos sin crecer): esos dos años son los que hay que vigilar. '
       'DSCR mínimo {DSCR_MIN}; saldo mínimo de tesorería {SALDO_MINIMO} en el mes {MES_SALDO_MINIMO}; payback del '
       'proyecto: {PAYBACK} (el token ya es texto: no le añadas «años»), y {PAYBACK_CAPEX} años sobre las compras; '
       'escenarios pesimista ({ESC_PES_EVENTOS} eventos: neto {ESC_PES_NETO}) y optimista ({ESC_OPT_EVENTOS} '
       'eventos: neto {ESC_OPT_NETO}). Las señales de los particulares no se modelan: la caja real es algo mejor. A '
       'los proveedores se les paga a 15 días y las nóminas cada mes. El Excel manda: si cambias una celda verde, el '
       'documento se queda atrás.',
    9: 'Marco legal verificado (cítalo así): SL unipersonal (capital desde 1 €) o autónomo; IAE 677.9, actividad '
       'empresarial: tus facturas NO llevan retención de IRPF (Reglamento del IRPF, art. 95.6); IVA 10 % del '
       'servicio de comidas en el evento, alcohol incluido (Ley 37/1992, art. 91.Uno.2.2.º), 21 % en el alcohol del '
       'asado para llevar y en lo facturado aparte, y factura de cada pago, también de la señal (art. 75.Dos); '
       'registro sanitario autonómico previa declaración responsable (RD 1021/2022, que reescribe el art. 2 del RD '
       '191/2011; RGSEAA sólo si suministras a otros establecimientos); prohibido preparar en casa para eventos (RD '
       '1021/2022, art. 13.5.b); APPCC y formación (Reglamento (CE) 852/2004); temperaturas de recepción de la carne '
       '(Reglamento (CE) 853/2004, como estándar), mantenimiento a 63 °C y comida testigo (RD 1086/2020, art. 30), '
       'material de riesgo y deshuesado del chuletón con vértebra (RD 1086/2020, art. 26.2), trazabilidad '
       '(Reglamento (CE) 178/2002, art. 18), alérgenos (Reglamento (UE) 1169/2011 y RD 126/2015); GAS del plan B: '
       'una botella de menos de 15 kg conectada a un solo aparato no es instalación y la conecta el usuario con '
       'regulador y tubo flexible (RD 919/2006, art. 2.1.h; ITC-ICG 08), botellas de 35 kg o en batería las monta '
       'una empresa instaladora (ITC-ICG 06), transporte de hasta 333 kg de gas por vehículo en la exención del ADR '
       '(1.1.3.6) con extintor; FUEGO: lo regula cada comunidad en montes y zonas colindantes (Ley 43/2003, art. '
       '44.3), con franja y época de peligro, y la licencia de la finca no levanta la restricción; una alerta puede '
       'prohibir también el gas: cláusula de fuerza mayor y plan B (ver el anexo por comunidades); en suelo urbano, '
       'la ordenanza de humos de cada ayuntamiento (sin cifras); FIESTAS: el encargo es un contrato menor (Ley '
       '9/2017, art. 118), con pago a 30 días (art. 198.4) y factura electrónica por FACe si eres SL (Ley 25/2013, '
       'art. 4), salvo que el ayuntamiento exima las de hasta 5.000 €; si te adjudican la barra o un puesto con canon '
       'y vendes tú al público, es venta no sedentaria con autorización municipal (Ley 7/1996, arts. 53-54); '
       'personal (ET arts. 1.1, 16 y 34.9); sin derecho de desistimiento en un servicio de comida con fecha (TRLGDCU, '
       'art. 103.l); efectivo con particulares sólo por debajo de 1.000 € (Ley 7/2012, art. 7); RGPD/LOPDGDD y LSSI; '
       'seguro de RC con incendio e intoxicación alimentaria ≥ 600.000 €. El último párrafo: la furgoneta '
       'frigorífica (ATP, RD 237/2000), el remolque y el transporte de las botellas y del carbón (con su ficha de '
       'datos de seguridad).',
    10: 'Conclusiones con tokens (viabilidad, holgura del año 1 y de los años 2 y 3, DSCR, payback), los riesgos del '
        'parrillero y cómo se mitigan (alerta de incendios que prohíbe la brasa: plan B de gas o cambio de fecha; '
        'lluvia y viento; intoxicación por rotura de frío o carne poco hecha fuera de las piezas enteras; quemaduras '
        'y fuego en carpas; humo en suelo urbano; subida del vacuno; avería de la furgoneta o del remolque; impago o '
        'retraso de un ayuntamiento; dependencia de pocos planners; falta de personal en temporada alta) y el plan de '
        'acción en 6 fases del checklist (83 tareas: 12/16/14/10/16/15). Cierra con el siguiente paso: completar el '
        'Excel con tus cifras.',
}

#: Prohibidos en el texto (SPEC D11 y D15 · cifras y errores de la 1.1 · restos del molde FT, del catering y del
#: paellero). «retención» sólo como la afirmación falsa de la 1.1 (7 %/15 %): decir que NO hay retención es correcto.
PROHIBIDOS = [
    r'\bfreelance', r'validad[oa]s?', r'Espa[ñn]a,? 2026', r'(?<!roadmap )food ?truck', r'\bcami[oó]n\b',
    r'ventanilla', r'generador', r'cocina central', r'estaci[oó]n(es)? tem[aá]tica', r'catering tem[aá]tico',
    r'drop-?off', r'carn[eé]t? de manipulador(?! ya no existe)', r'sin licencia', r'tarifa plana', r'solopreneur',
    r'\bRGSEAA\b(?!.{0,80}(s[oó]lo|otros establecimientos))', r'PATRICOVA', r'INFOCYL', r'PIDOM',
    r'excepci[oó]n cultural', r'\bpaell', r'socarrat', r'\barroz', r'\barroces',
    r'retenci[oó]n (del? )?(7|15)', r'7 ?%? ?/ ?15 ?%', r'\bCNAE\b',
    r'3\.500', r'(?<!hasta )(?<![\d.])5\.000 ?€', r'4\.356', r'10\.406', r'21\.036', r'57\.200',
    r'130\.800', r'237\.000', r'240\.000', r'21\.370', r'53\.730', r'97\.140', r'8\.830', r'2\.800', r'5,44',
    r'8-10 eventos', r'\b37 ?%', r'\b41 ?%', r'\b55-60 ?%', r'\b58 ?%', r'80 ?€ ?(/|al) ?mes',
    r'80-120 ?€', r'320-360', r'4-7 veces', r'1\.800-2\.100', r'80-120 M', r'165\.000', r'ordenanza 4/2021',
]
#: Cifras que el texto puede llevar escritas (normas, política comercial, research con fuente, mezcla del plan).
PERMITIDAS = set('''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 18 20 21 24 25 26 28 29 30 31 32 34 35 39 40 42 44 45 48 50 53
54 59 60 63 70 72 74 75 80 83 90 91 93 95 100 103 110 118 120 126 140 150 178 191 198 237 300 320 333 350 390 400 450
500 513 590 600 677 852 853 919 1.000 1.021 1.086 1.169 1.175 1.760 5.000 15.000 600.000 3.005,06 2026 2025 2023
2022 2021 2020 2017 2016 2015 2013 2012 2011 2007 2006 2004 2003 2002 2000 1996 1995 1992 1990 677.9 13.5 2.1 44.3
198.4 1.1 34.9 1.1.3.6 26.2 30.8 75.Dos 95.6 06 08 0,7-1 10-12 15-20 18-30 30-55 55-90 15,95-19,95 40-100 350-450
500-600 60-80 40-50 45-60 30-59 7-29 15-29 7-14 400-500 12/16/14/10/16/15'''.split())
RX_NUM = re.compile(r'(?<![\w{])\d[\d.,]*\d|(?<![\w{])\d')


def ranuras():
    d = json.load(open(os.path.join(BP4, 'docx_es_cat.json'), encoding='utf-8'))['parrafos']
    gem = {}
    for t in ('pae_es_a', 'pae_es_b'):
        gem.update(json.load(open(os.path.join(PAE, t + '.json'), encoding='utf-8')))
    fuera = []
    for k in sorted(d, key=int):
        v = d[k]
        if v['rol'] != 'cuerpo':
            continue
        sec = int(v['seccion'])
        fuera.append({'i': int(k), 'seccion': sec, 'palabras_objetivo': int(v['palabras']),
                      'molde_ft_es': v['texto'], 'gemela_paellero_es': gem.get(k, '')})
    return fuera


def preparar():
    cif = json.load(open(CIFRAS, encoding='utf-8'))['tokens'] if os.path.exists(CIFRAS) else {}
    fuente = json.load(open(os.path.join(AQUI, 'fuente_par_11.json'), encoding='utf-8'))
    material = [p['texto'] for p in fuente['parrafos']] + [' | '.join(f) for t in fuente['tablas'] for f in t]
    os.makedirs(TANDAS, exist_ok=True)
    rs = ranuras()
    for tanda, secs in (('par_es_a', range(1, 6)), ('par_es_b', range(6, 11))):
        sel = [r for r in rs if r['seccion'] in secs]
        ent = {
            'tanda': tanda, 'producto': 'Plan de Negocio Parrillero / Asador para Eventos ES 2.2 (aichef.pro, 45 €)',
            'salida': 'scripts/productos-digitales/parrillero-2_2/textos/%s.json' % tanda,
            'formato_salida': '{"<i>": "<párrafo en español>", …} con TODOS los "i" de "parrafos" y nada más',
            'brief': 'scripts/productos-digitales/parrillero-2_2/BRIEF-REDACTORES.md (léelo entero antes)',
            'secciones': dict((s, {'titulo': SECCIONES[s], 'pista': PISTAS[s]}) for s in secs),
            'n_parrafos': len(sel), 'n_palabras_objetivo': sum(r['palabras_objetivo'] for r in sel),
            'tokens': cif,
            'material_parrillero_1_1 (docx anterior: SOLO contenido; sus cifras están prohibidas)': material,
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
