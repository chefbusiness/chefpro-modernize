#!/usr/bin/env python3
"""
tandas_docx.py — Finca de Eventos y Bodas ES 1.0 (SPEC D10/D11): prepara y valida las dos tandas de redacción del plan de
negocio (docx). Copia adaptada de `plan-heladeria/tandas_docx.py`.

Las 61 ranuras de texto del docx del Food Truck ES (131 párrafos, 10 Heading 1; mapa en
`business-plans-en-4/docx_es_cat.json`) se escriben NUEVAS, en español, para la finca:
  fin_es_a = §1-5 (29 ranuras) · fin_es_b = §6-10 (32 ranuras).
Gemela de FORMATO: el texto de la Heladería ES 1.0 en la misma ranura (`plan-heladeria/textos/hel_es_{a,b}.json`, formato
ES 1.0 sin «versión anterior» y con tokens): sirve para ver cómo se escribe una ranura con tokens, nunca su contenido.
No hay versión anterior: el material es el research (`F1-research-finca.md`), `F2-NOTAS.md` y las pistas de abajo. Las
cifras del Excel van SIEMPRE como token {ASI} (`cifras_caso_es.json`); `docx_fin_es.py` las resuelve al ensamblar. Sólo
lee JSON: corre en el Mac.

    python3 tandas_docx.py preparar                       # tandas/fin_es_{a,b}.entrada.json
    python3 tandas_docx.py check --tanda fin_es_a         # valida textos/fin_es_a.json (salida del redactor)

Sesión Claude Code, 25-oct-2026.
"""
import argparse
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
BP4 = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
GEMELA = os.path.join(os.path.dirname(AQUI), 'plan-heladeria', 'textos')
TANDAS, TEXTOS = os.path.join(AQUI, 'tandas'), os.path.join(AQUI, 'textos')
CIFRAS = os.path.join(AQUI, 'cifras_caso_es.json')
RESEARCH = 'scripts/productos-digitales/plan-finca-eventos/F1-research-finca.md'

SECCIONES = {
    1: '1. Resumen Ejecutivo', 2: '2. Concepto y Propuesta de Valor', 3: '3. Análisis de Mercado',
    4: '4. Análisis Competitivo', 5: '5. Plan de Marketing y Captación', 6: '6. Plan de Operaciones',
    7: '7. Estructura Organizativa y RRHH', 8: '8. Plan Financiero', 9: '9. Aspectos Legales y Licencias',
    10: '10. Conclusiones y Plan de Acción',
}

#: Hechos fijos del modelo (SPEC D2, D4, D5): iguales en el Word, el Excel, la calculadora y el contrato.
MODELO = ('FINCA ARRENDADA con edificaciones existentes (no se compra: 1-3 M€) + CATERING EXCLUSIVO CONCESIONADO que paga '
          'un canon. La finca factura al cliente el espacio y los servicios del evento (ceremonia, mobiliario, '
          'coordinación, limpieza, aparcamiento) con IVA del 21 %; el catering factura DIRECTAMENTE al cliente el menú y '
          'la barra con IVA del 10 % y paga a la finca un canon (supuesto editable, «negócialo»; IVA del 21 %). Sin cocina '
          'de producción ni brigada propia: los camareros y la cocina los pone el catering, y la seguridad alimentaria '
          'del menú es suya. Mezcla de 120 eventos al año: 30 bodas (120 invitados, 47 € por invitado), 35 eventos de '
          'empresa (80, 34 €), 40 celebraciones privadas (70, 29 €) y 15 eventos pequeños (40, 30 €); precios sin IVA para '
          'la finca. Intermediarios (wedding planners y agencias): {INTERMEDIARIOS_PCT} de las ventas con una comisión '
          'del {COMISION_INTERMEDIARIOS}. Mes 1 del Excel = MARZO. Contrato de arrendamiento de «quince años» (en letra). '
          'El crecimiento de los años 2 y 3 se cuenta en EVENTOS EQUIVALENTES ({EVENTOS_EQUIVALENTES_A2} y '
          '{EVENTOS_EQUIVALENTES_A3}), no en invitados')

#: Lo que tiene que contar cada sección (español de España; research §0-§3 y §6, F2-NOTAS y SPEC). Cifras del Excel = tokens.
PISTAS = {
    1: 'Qué es el negocio: una finca de eventos y bodas en una finca ARRENDADA con edificaciones existentes (casa o '
       'masía, jardín, salón y, si el clima lo pide, carpa) con un catering exclusivo concesionado. Quién hace qué: la '
       'finca factura el espacio y los servicios del evento (con IVA del 21 %, {PCT_ESPACIO} de las ventas, '
       '{VENTAS_ESPACIO_A1}) y el catering factura el menú y la barra al cliente (10 %) y paga a la finca un canon '
       '({PCT_CANON} de las ventas, {CANON_A1}). {EVENTOS_ANO} eventos al año (bodas, eventos de empresa, celebraciones '
       'privadas y eventos pequeños) con {INVITADOS_EVENTO} invitados de media y {PRECIO_INVITADO} por invitado sin IVA '
       '({PRECIO_INVITADO_IVA} con IVA). Cifras clave por token: ventas {VENTAS_A1}, resultado neto {NETO_A1}, '
       'inversión total {INVERSION_TOTAL} (de la que {INVERSION_PARTIDAS} son acondicionamiento de la finca), préstamo '
       '{PRESTAMO}, equilibrio de caja en {BE_EVENTOS_ANO_CAJA} eventos al año. Se avisa ya aquí de que la licencia en '
       'suelo rústico es lo que decide si hay negocio. Qué contiene el kit: este plan de negocio de 10 secciones, el Excel '
       'del plan financiero de 9 hojas, el checklist de apertura de 84 tareas en 6 fases, la calculadora de presupuesto '
       'del espacio, los modelos de contrato (reserva con los novios y condiciones del catering exclusivo) y la guía de '
       'equivalencias para Latinoamérica.',
    2: 'Los tres modelos de finca que conviven en España: catering propio (la finca cocina y sirve el banquete), catering '
       'exclusivo concesionado (el catering de la casa sirve el menú y paga canon) y solo alquiler con un pago fijo (el '
       'cliente trae su catering; ejemplos de escaparate con pago fijo de 2.500 € y menú mínimo de 130 €). Por qué el '
       'plan elige el concesionado: no hace falta cocina de producción (80.000-120.000 € más) ni brigada, la seguridad '
       'alimentaria del menú es del catering, y el solo alquiler no cubre el equilibrio de caja (sin canon, las ventas '
       'bajan a unos 284.000 € frente a los {BE_INGRESOS_CAJA} que hacen falta). El catering propio es otro negocio: '
       'ventas de 0,8-1 M€, mercancía de un 30 % y personal de un 35-38 % de las ventas, para hosteleros; ese lector '
       'debe ir al Plan de Negocio de Catering Temático para Eventos. La finca NO se compra (comprarla son 1-3 M€, '
       'ejemplo de una finca de 21.000 m² en venta por 980.000 €): se arrienda con edificaciones existentes (lo exigen '
       'Madrid, Cataluña y la vía rápida valenciana) o se cede la familiar con renta de mercado ({RENTA_MES} al mes, el '
       '{RENTA_PCT_A1} de las ventas), con contrato de «quince años» o más, condición suspensiva de licencias, carencia '
       'durante las obras y reversión de mejoras. Qué vende la finca: el espacio, la ceremonia, el montaje, la '
       'coordinación del día y la calma de tener a un solo catering responsable; tabla o comparación de los tres modelos '
       'si cabe en prosa. El día a día de un evento medio ({HORAS_EVENTO} horas de equipo de la finca) y el ingreso por '
       'evento medio ({VENTA_EVENTO_MEDIO}).',
    3: 'Mercado de bodas con fuente: INE, 175.364 matrimonios en 2024 (+1,7 %), el 83,6 % civiles; de mayo a octubre se '
       'concentra el 63,7 % de las bodas y los picos son septiembre (13,1 %) y junio (12,8 %); enero se queda en el 3,8 %. '
       'Según el Informe del Sector Nupcial 2026 de Bodas.net (encuesta a sus usuarios, que sobrerrepresenta la boda '
       'grande), el 28 % de las parejas celebra en una finca, la boda se prepara con 12-18 meses de antelación (13 de '
       'media), piden información a 6 espacios y visitan 3, y el 64 % busca en webs especializadas. Demanda de clientes en '
       'Google España (DataForSEO, octubre de 2026): unas 4.000 búsquedas al mes con «finca». Las bodas son solo parte del '
       'negocio: empresas (jornadas, convenciones, comidas de Navidad, team building), comuniones, bautizos, cumpleaños '
       'y eventos pequeños llenan lo que las bodas no. Precios de escaparate (95-200 € por comensal en Castilla-La Mancha; '
       '140-145 € más IVA todo incluido en Barcelona; espacio entre 2.500 € y 14.000 € según finca y temporada) con '
       'cautela: son precios de escaparate. La estacionalidad del plan, con el Mes 1 en marzo, y el hueco: nadie publica un '
       'plan español con Excel vivo. NADA de tamaños de mercado sin fuente.',
    4: 'Clientes: parejas (la boda grande, pero también la íntima), empresas, familias que celebran comuniones y '
       'cumpleaños, y los intermediarios que traen clientes (wedding planners y agencias de eventos, {INTERMEDIARIOS_PCT} '
       'de las ventas con comisión). Qué decide cada uno (fecha, aforo, entorno, catering, precio, alojamiento, plan B '
       'de lluvia). Competencia por categorías, SIN nombres ni cifras inventadas: otras fincas con catering propio, '
       'fincas con catering exclusivo, fincas de solo alquiler con pago fijo, hoteles y restaurantes con salón, '
       'masías y haciendas con encanto, salones de banquetes urbanos y espacios singulares (bodegas, palacetes, '
       'jardines). Cómo gana este concepto: calendario claro y fechas bien vendidas, un solo interlocutor para la '
       'comida, precio del espacio visible, plan B de lluvia con salón y carpa, y venta de entresemana para empresas. '
       'El riesgo: la guerra de precios de las fechas de sábado y que el cliente quiera traer su catering.',
    5: 'Captación con 12-18 meses de antelación. Escaparates de bodas (fichas en portales especializados), ferias '
       'nupciales, jornadas de puertas abiertas con el catering exclusivo y cata del menú, visitas a la finca (piden '
       'información a 6 espacios y visitan 3: cómo se prepara la visita), wedding planners y agencias de eventos con una '
       'comisión del {COMISION_INTERMEDIARIOS} (el {INTERMEDIARIOS_PCT} de las ventas entra por ellos), web con '
       'calendario de disponibilidad, fotografía y vídeo de las cuatro estaciones, reseñas, redes sociales, ferias y '
       'puertas abiertas {FERIAS_ANO} al año y marketing {MARKETING_ANO} al año más el lanzamiento en la inversión. '
       'LA CLAVE DE LA PRIMERA TEMPORADA: las fechas de la primera temporada se reservan durante los meses de licencia y '
       'obra, antes de abrir, como reservas condicionadas a la licencia con devolución íntegra si no llega, que pasan a '
       'firmes al obtenerla (nunca confirmar fechas en firme sin licencia). Empresas y comuniones entre semana y fuera de temporada; precios de temporada alta, media y baja con '
       'descuentos visibles para viernes, domingos y de noviembre a marzo.',
    6: 'Un sábado tipo con horas orientativas: montaje de mañana, prueba de sonido, llegada del catering, ceremonia, '
       'cóctel, banquete, baile y recogida; quién hace qué (la finca: coordinación, montaje del espacio, limpieza, '
       'aparcamiento y mantenimiento; el catering: menú, barra, camareros y su cocina). Plan B de lluvia: salón y '
       'carpa ({CARPA} la carpa, {SALON} el salón). Infraestructura: aforo de {AFORO} personas, aseos ({ASEOS}), '
       'aparcamiento ({APARCAMIENTO}; una plaza por cada 2,5-3 invitados), grupo electrógeno ({GRUPO_ELECTROGENO}), '
       'acústica y sonido ({ACUSTICA} y {SONIDO}), climatización, fosa séptica y potencia eléctrica. Ruido: '
       'límites de inmisión del RD 1367/2007 (de noche manda el límite de 45 dBA en zona residencial), limitador-'
       'registrador, baile final en interior y altavoces de espaldas a las viviendas. Agua de pozo propio, si aplica: el '
       'RD 3/2023 convierte la finca con actividad comercial en una zona de abastecimiento y el titular responde de la '
       'calidad hasta el grifo (analíticas y protocolo). La relación con el catering: prueba de menú, comida testigo en '
       'toda boda o encargo de más de 40 personas (RD 1086/2020, art. 30: una ración de al menos 100 g, a 4 °C o menos o a '
       '−18 °C o menos, durante 7 días, la guarda quien sirve), gestión de alérgenos, inscripción en el registro sanitario '
       'de la cocina que use, seguro de intoxicación, horarios y canon auditable (derecho a revisar sus cubiertos). '
       'Mantenimiento y jardinería ({JARDINERIA_ANO} al año), suministros {SUMINISTROS_MES} al mes, seguros '
       '{SEGUROS_ANO} al año. Fuego, bengalas y barbacoas en época de peligro de incendios: prohibidos.',
    7: 'Equipo propio SIN camareros ni cocina (los pone el catering): gerente (el titular, {SUELDO_TITULAR} al mes), '
       'coordinación de eventos (fijo discontinuo), mantenimiento y jardinería, auxiliares de evento (fijos discontinuos), '
       'comercial de bodas a tiempo parcial y limpieza a tiempo parcial. {PLANTILLA_PERSONAS} personas, '
       '{JORNADAS_EQUIVALENTES} jornadas completas equivalentes, coste {PERSONAL_A1} ({PERSONAL_PCT_A1} de las ventas), '
       'cobertura de horas {COBERTURA_HORAS} ({HORAS_CONTRATADAS} horas contratadas frente a {HORAS_NECESARIAS} '
       'necesarias; {PERSONAS_EVENTO} personas de la finca por evento de media). Contrato fijo discontinuo por escrito '
       'con llamamiento por escrito (art. 16 del Estatuto de los Trabajadores), nunca autónomos que te facturan (falso '
       'autónomo), registro de jornada (art. 34.9), y el convenio provincial de hostelería como referencia salarial '
       'prudente: el VI Acuerdo Laboral de ámbito Estatal para el sector de Hostelería incluye a quien presta servicio '
       'de comida y bebida, y la finca que solo alquila no está en su lista (que no es exhaustiva): confírmalo con tu '
       'asesoría. Cómo se coordina con el equipo del catering el día del evento. Formación en prevención de riesgos, '
       'primeros auxilios y evacuación; el catering forma a su propio personal.',
    8: 'Plan financiero, TODO por token: inversión total {INVERSION_TOTAL} = compras {CAPEX} (acondicionamiento '
       '{INVERSION_PARTIDAS} incluidos {IMPREVISTOS} de imprevistos, más la fianza {FIANZA} de {FIANZA_MESES} meses y '
       '{RENTA_PREVIA} de renta anterior a la apertura) + fondo de maniobra {FONDO_MANIOBRA} ({MESES_FONDO} meses); IVA de '
       'la inversión {IVA_INVERSION}; necesidad de caja {NECESIDAD_CAJA}; financiación {RECURSOS_PROPIOS} propios + '
       'préstamo {PRESTAMO} al {TIPO_PRESTAMO}, {PLAZO_PRESTAMO} años con {CARENCIA} año de carencia, cuota '
       '{CUOTA_ANUAL}. Cuenta de resultados de 3 años: ventas {VENTAS_A1}/{VENTAS_A2}/{VENTAS_A3}; margen bruto '
       '{MARGEN_BRUTO_PCT_A1}; personal {PERSONAL_A1}; renta {RENTA_ANO} ({RENTA_PCT_A1}); neto '
       '{NETO_A1}/{NETO_A2}/{NETO_A3}. EL AÑO 1 CUENTA {EVENTOS_ANO} EVENTOS COMPLETOS: el texto tiene que explicar que '
       'eso solo es posible si la primera temporada se vende con reservas condicionadas a la licencia durante la '
       'tramitación y la obra, que pasan a firmes al obtenerla, y '
       'remitir al escenario pesimista del Excel ({ESC_PES_EVENTOS} eventos de {ESC_PES_INVITADOS} invitados a '
       '{ESC_PES_PRECIO}: ventas {ESC_PES_VENTAS}, neto {ESC_PES_NETO}) si no se consigue; NO decir que el año 1 da '
       'pérdidas, porque el Excel no lo dice (el fondo de maniobra aguanta la primavera de arranque y la temporada, el primer invierno). Escenario optimista '
       '({ESC_OPT_EVENTOS} eventos de {ESC_OPT_INVITADOS} invitados a {ESC_OPT_PRECIO}: neto {ESC_OPT_NETO}). '
       'CRECIMIENTO: se cuenta en eventos equivalentes, {EVENTOS_EQUIVALENTES_A2} en el año 2 (+{CREC_A2}) y '
       '{EVENTOS_EQUIVALENTES_A3} en el año 3 (+{CREC_A3}), con el mismo precio por invitado; en el libro crece el tamaño '
       'medio del evento ({INVITADOS_EVENTO_A2} y {INVITADOS_EVENTO_A3} invitados). EQUILIBRIO: contable '
       '{BE_EVENTOS_ANO} eventos al año ({BE_INVITADOS_EVENTO} invitados por evento; ingresos {BE_INGRESOS}; holgura '
       '{HOLGURA_CONTABLE}); de caja {BE_EVENTOS_ANO_CAJA} eventos en el año 1 (holgura {HOLGURA_CAJA}, de carencia), '
       '{BE_EVENTOS_CAJA_A2} en el 2 ({HOLGURA_CAJA_A2}) y {BE_EVENTOS_CAJA_A3} en el 3 ({HOLGURA_CAJA_A3}). DSCR mínimo '
       '{DSCR_MIN}. TESORERÍA: el Mes 1 es marzo, la rampa arranca al {RAMPA_MES1} y llega al ritmo de crucero en '
       '{MESES_RAMPA} meses (las bodas se reservan con 12-18 meses); saldo mínimo {SALDO_MINIMO} en el mes '
       '{MES_SALDO_MINIMO} ({MES_SALDO_MINIMO_NOMBRE}); el año acaba (febrero) con {SALDO_MES12}. Cada punto de canon '
       'vale unos {CANON_PUNTO}: negócialo. IVA: las dos líneas al 21 % ({IVA_REPERCUTIDO_A1} de IVA repercutido en el '
       'año 1). Payback: {PAYBACK} (el token ya es texto: no le añadas «años»). Alternativas SIN Excel, razonadas: '
       'catering propio y solo alquiler, con su cifra de la pista del §2. El Excel manda: si cambias una celda verde, el '
       'documento se queda atrás.',
    9: 'Marco legal con su cita (solo esto, dicho así). URBANISMO EN SUELO RÚSTICO, que decide el negocio; en suelo '
       'urbano basta el uso compatible del plan municipal y la licencia de actividad. Madrid: Ley 8/2012 art. 9 (actos '
       'sociales y eventos familiares en edificaciones existentes) + calificación urbanística del art. 148 de la Ley 9/2001 '
       '(informe en 1 mes, resolución en 3, silencio negativo). Andalucía: LISTA art. 22 (actuación extraordinaria, '
       'autorización previa, silencio desestimatorio y prestación compensatoria del 10 % del presupuesto de las obras). '
       'Cataluña: TRLU art. 47.3 bis, solo masías y casas rurales catalogadas. Comunitat Valenciana: TRLOTUP, declaración '
       'de interés comunitario (arts. 216 y 221, canon del 2 %) o la excepción del art. 219 por reutilizar arquitectura '
       'tradicional. Lo común: edificios existentes, informe previo y 6-12 meses o más antes de la licencia. NO CONFIRMAR '
       'FECHAS EN FIRME SIN LICENCIA (antes, solo reservas condicionadas con devolución íntegra) y condición suspensiva en el arrendamiento. Resto de comunidades: «pregunta en urbanismo qué '
       'figura usa tu comunidad». ESPECTÁCULOS: la boda es privada, pero la finca que la alquila a terceros es un '
       'establecimiento público (en la C. Valenciana, «salón de banquetes»): ley autonómica de espectáculos públicos y '
       'actividades recreativas, y su seguro obligatorio de responsabilidad civil (Madrid añade incendio); cifras solo '
       'de Andalucía, y como orientativo (aforo de 101 a 300 personas: 526.000 €); en las demás, «compruébalo». '
       'AUTOPROTECCIÓN: Directriz Básica de Autoprotección, Orden INT/1068/2026 (BOE de 10-10-2026), plan obligatorio '
       'desde 1.000 personas en edificio o carpa y 5.000 al aire libre en recinto delimitado; con {AFORO} personas queda '
       'fuera de la norma estatal, salvo que tu comunidad sea más exigente o la Administración te lo pida por estar en un '
       'entorno de riesgo (como el forestal). RUIDO: RD 1367/2007. AGUA: RD 3/2023. COMIDA TESTIGO: RD 1086/2020, '
       'art. 30. IVA: espacio al 21 % ({IVA_LINEA_ESPACIO}), canon al 21 % ({IVA_LINEA_CANON}), menú del catering al '
       '10 %; un precio único con todo al 10 % es arriesgado: precio propio o consulta vinculante a la DGT (LIVA art. '
       '91). IAE: epígrafe del espacio criterio de tu asesoría; exento de cuota con menos de 1 M€ de cifra de negocio. '
       'ARRENDAMIENTO: uso distinto de vivienda, LAU arts. 3 y 4, pacto libre; la fianza ({FIANZA_MESES} meses) lo habitual, '
       'compruébalo con tu abogado. CONSUMO: señal y penalizaciones proporcionales y recíprocas (TRLGDCU arts. 85.6, 87.2, '
       '90.2 y 103.l). Personal: ET arts. 16 y 34.9. Todo lo demás: «compruébalo en tu ayuntamiento, tu comunidad o tu '
       'asesoría». Lo que no esté aquí no se afirma.',
    10: 'Conclusiones con tokens (viabilidad, holgura del año 1 y de los años 2 y 3, DSCR mínimo, saldo mínimo, payback) '
        'y el PLAN DE ACCIÓN EN 90 DÍAS (semanas 1-4: constituir la sociedad, cerrar el arrendamiento con condición '
        'suspensiva, consulta urbanística; semanas 5-8: proyecto técnico, solicitud de calificación o autorización y '
        'selección del catering exclusivo; semanas 9-13: contrato del catering, marca, web, fotografía, primeras visitas y '
        'preventa de fechas condicionada a la licencia), y el checklist de 84 tareas (12/16/15/13/14/14). RIESGOS y cómo se '
        'mitigan: la licencia (silencio negativo, plazos de 6-12 meses o más); la ocupación por debajo de unos '
        '{BE_EVENTOS_ANO_CAJA} eventos al año, donde no hay caja; la dependencia del catering (dos homologados, contrato '
        'con plazo, canon y salida); la lluvia (salón y carpa); el ruido y los vecinos (limitador, baile en interior); '
        'comprar la finca; arrendarla poco tiempo; vivir solo de los sábados de mayo a octubre; el seguro corto; falsos '
        'autónomos para el montaje. Las alternativas razonadas del §2 (catering propio, solo alquiler) como plan B. Cierra '
        'con el siguiente paso: completar el Excel con tus cifras y consultar a tu ayuntamiento antes de gastar un euro.',
}

#: Prohibidos (SPEC D11): importados de `barrido_es.py` (sin «generador» ni «aparcamiento», legítimos aquí) + los de D11
#: por si el barrido cambia + «aviso» de «15 años» (se escribe «quince años»).
try:
    from barrido_es import PROHIBIDOS as _BARRIDO
except Exception:                                           # pragma: no cover
    _BARRIDO = []
PROHIBIDOS = list(_BARRIDO) + [
    r'393/2007', r'carn[eé]t? de manipulador(?! ya no existe)', r'Espa[ñn]a,? 2026', r'\bfreelance', r'validad',
]
RX_15 = re.compile(r'\b15 a[ñn]os')
#: Cifras que el texto puede llevar escritas (normas, research con fuente, mezcla del caso y estructura de la finca).
PERMITIDAS = set('''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 20 21 22 25 28 30 35 40 45 47 50 51 55 60 64 70 75 80
90 91 95 98 100 101 103 120 148 216 219 221 300 526.000 1.000 5.000 20.000 4.000 6-12 12-18 1-3 85.6 87.2 90.2 34.9
47.3 30.8 2,5-3 2.500 130 140-145 95-200 14.000 21.000 980.000 80.000-120.000 175.364 83,6 63,7 13,1 12,8 3,8 1,7
0,8-1 35-38 8/2012 9/2001 3/2023 1367/2007 1086/2020 1068/2026 10-10-2026 37/1992 1175/1990 2026 2025 2024 2027 2023
2012 2007 2001 2020 2.2 2.2.º 1.1 2.000 3.600 1.500 5.000-6.000 −18 100-150 34 29 120-125 7-8 1,5 0,5 45-30 2-3 9 3-4'''.split())
RX_NUM = re.compile(r'(?<![\w{])[−+]?\d[\d.,/:−-]*\d|(?<![\w{])\d')
#: Caracteres admitidos además del latín básico/extendido: tipografía española y los signos de temperatura (−, ≤, ≥).
RX_RARO = re.compile(r'[^\x00-ɏ‐-‧€°→ ‑«»¿¡ºª·…–—“”‘’−≤≥²]')


def ranuras():
    d = json.load(open(os.path.join(BP4, 'docx_es_cat.json'), encoding='utf-8'))['parrafos']
    gem = {}
    for t in ('hel_es_a', 'hel_es_b'):
        p = os.path.join(GEMELA, t + '.json')
        if os.path.exists(p):
            gem.update(json.load(open(p, encoding='utf-8')))
    fuera = []
    for k in sorted(d, key=int):
        v = d[k]
        if v['rol'] != 'cuerpo':
            continue
        sec = int(v['seccion'])
        fuera.append({'i': int(k), 'seccion': sec, 'palabras_objetivo': int(v['palabras']),
                      'molde_ft_es': v['texto'], 'gemela_formato_heladeria_es': gem.get(k, '')})
    return fuera


def preparar():
    cif = json.load(open(CIFRAS, encoding='utf-8'))['tokens'] if os.path.exists(CIFRAS) else {}
    os.makedirs(TANDAS, exist_ok=True)
    rs = ranuras()
    for tanda, secs in (('fin_es_a', range(1, 6)), ('fin_es_b', range(6, 11))):
        sel = [r for r in rs if r['seccion'] in secs]
        ent = {
            'tanda': tanda, 'producto': 'Plan de Negocio: Finca de Eventos y Bodas ES 1.0 (aichef.pro, 45 €)',
            'salida': 'scripts/productos-digitales/plan-finca-eventos/textos/%s.json' % tanda,
            'formato_salida': '{"<i>": "<párrafo en español>", …} con TODOS los "i" de "parrafos" y nada más',
            'brief': 'scripts/productos-digitales/plan-finca-eventos/BRIEF-REDACTORES.md (léelo entero antes)',
            'research': RESEARCH + ' (§0-§3 y §6: material de apoyo; la pista de la sección manda) y F2-NOTAS.md §2 y §7',
            'modelo (SPEC D2, D4, D5, literal en el fondo)': MODELO,
            'secciones': dict((s, {'titulo': SECCIONES[s], 'pista': PISTAS[s]}) for s in secs),
            'n_parrafos': len(sel), 'n_palabras_objetivo': sum(r['palabras_objetivo'] for r in sel),
            'tokens': cif,
            'parrafos': sel,
        }
        p = os.path.join(TANDAS, tanda + '.entrada.json')
        json.dump(ent, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('%s: %d ranuras · %d palabras objetivo · %d tokens → %s' % (
            tanda, len(sel), ent['n_palabras_objetivo'], len(cif), os.path.relpath(p, AQUI)))


def check(tanda):
    pe, ps = os.path.join(TANDAS, tanda + '.entrada.json'), os.path.join(TEXTOS, tanda + '.json')
    if not os.path.exists(pe):
        print('ERROR no existe %s: corre primero `python3 tandas_docx.py preparar`' % os.path.relpath(pe, AQUI))
        return 1
    if not os.path.exists(ps):
        print('ERROR no existe %s: el redactor aún no ha entregado esta tanda' % os.path.relpath(ps, AQUI))
        print('%s: 0 párrafos · ROJO (1 error, 0 avisos)' % tanda)
        return 1
    ent = json.load(open(pe, encoding='utf-8'))
    try:
        sal = json.load(open(ps, encoding='utf-8'))
    except ValueError as e:
        print('ERROR %s no es JSON válido: %s' % (os.path.relpath(ps, AQUI), e))
        return 1
    tokens = set(ent['tokens'])
    err, avi = [], []
    esperadas = set(str(r['i']) for r in ent['parrafos'])
    if set(sal) != esperadas:
        err.append('ranuras: faltan %s · sobran %s' % (sorted(esperadas - set(sal)), sorted(set(sal) - esperadas)))
    total = 0
    for r in ent['parrafos']:
        t = sal.get(str(r['i']), '')
        if not isinstance(t, str):
            err.append('%d: la ranura no es texto' % r['i'])
            continue
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
        if RX_15.search(t):
            avi.append('%d: «15 años» con cifra: escribe «quince años» (censo bio_vieja)' % r['i'])
        sin_tok = re.sub(r'\{[A-Z0-9_]+\}', '', t)
        for num in RX_NUM.findall(sin_tok):
            if num.rstrip('.,') not in PERMITIDAS:
                avi.append('%d: cifra escrita «%s» (¿debería ser token o tiene fuente?)' % (r['i'], num))
        if RX_RARO.search(t):
            err.append('%d: caracteres no latinos «%s»' % (r['i'], RX_RARO.search(t).group(0)))
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
    if a.accion == 'check' and not a.tanda:
        ap.error('check necesita --tanda')
    sys.exit(preparar() or 0 if a.accion == 'preparar' else check(a.tanda))
