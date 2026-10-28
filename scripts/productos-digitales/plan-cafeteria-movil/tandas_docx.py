#!/usr/bin/env python3
"""
tandas_docx.py — Cafetería Móvil para Eventos ES 1.0 (SPEC D15): prepara y valida las dos tandas de redacción del plan de
negocio (docx). Copia adaptada de `plan-pizzeria/tandas_docx.py`.

Las 61 ranuras de texto del docx del Food Truck ES (131 párrafos, 10 Heading 1; mapa en
`business-plans-en-4/docx_es_cat.json`) se escriben NUEVAS, en español, para la cafetería móvil:
  caf_es_a = §1-5 (29 ranuras) · caf_es_b = §6-10 (32 ranuras).
Gemelas: el texto de la Finca 1.0 en la misma ranura (`plan-finca-eventos/textos/fin_es_{a,b}.json`, la ES 1.0 de la
línea de eventos con tokens: FORMATO) y el del Parrillero 2.2 (`parrillero-2_2/textos/par_es_{a,b}.json`, el oficio
itinerante con furgoneta y base): sirven para ver cómo se escribe una ranura con tokens, nunca su contenido. No hay
versión anterior: el material es el research (`F1-research-cafeteria-movil.md`), la SPEC (D10-D16) y las pistas de
abajo. Las cifras del Excel, de la calculadora y de la tabla de escalado van SIEMPRE como token {ASI}
(`cifras_caso_es.json`); `docx_caf_es.py` las resuelve al ensamblar. Sólo lee JSON: corre en el Mac.

    python3 tandas_docx.py preparar                       # tandas/caf_es_{a,b}.entrada.json
    python3 tandas_docx.py check --tanda caf_es_a         # valida textos/caf_es_a.json (salida del redactor)

Sesión Claude Code, 28-oct-2026.
"""
import argparse
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BP4 = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
GEMELA_FORMATO = os.path.join(os.path.dirname(AQUI), 'plan-finca-eventos', 'textos')
GEMELA_OFICIO = os.path.join(os.path.dirname(AQUI), 'parrillero-2_2', 'textos')
TANDAS, TEXTOS = os.path.join(AQUI, 'tandas'), os.path.join(AQUI, 'textos')
CIFRAS = os.path.join(AQUI, 'cifras_caso_es.json')
RESEARCH = 'scripts/productos-digitales/plan-cafeteria-movil/F1-research-cafeteria-movil.md'

SECCIONES = {
    1: '1. Resumen Ejecutivo', 2: '2. Concepto y Propuesta de Valor', 3: '3. Análisis de Mercado',
    4: '4. Análisis Competitivo', 5: '5. Plan de Marketing y Captación', 6: '6. Plan de Operaciones',
    7: '7. Estructura Organizativa y RRHH', 8: '8. Plan Financiero', 9: '9. Aspectos Legales y Licencias',
    10: '10. Conclusiones y Plan de Acción',
}

#: Cobro y cancelación (SPEC D16, fuente única: iguales en calculadora, contrato, Word y ficha).
COBRO = ('COBRO (SPEC D16, literal en el fondo): particular, señal del 30 % a cuenta del precio al firmar y el 70 % siete '
         'días antes del evento; empresa, agencia o congreso, el 30 % al confirmar y el 70 % a 30 días de la factura; '
         'venta directa en ferias y mercados, en el acto, con el canon del organizador ({CANON_FERIAS} en el caso). Cada '
         'pago se factura, también la señal (art. 75.Dos de la Ley 37/1992). CANCELACIÓN en cuatro tramos «de X a menos '
         'de Y», sin huecos: particular con cortes en 60, 30 y 7 días antes del evento; empresa con cortes en 30, 15 y 7 '
         'días; se retiene el 10 %, el 30 % o el 60 % del precio y, en el último tramo, el 100 % MENOS los costes que '
         'la cafetería se ahorra (consumibles, café y leche sin gastar, refuerzo y desplazamiento); y es recíproca: si '
         'cancela la cafetería, devuelve lo cobrado y paga lo que corresponde al mismo tramo. Un contrato con un '
         'consumidor cerrado a distancia no tiene desistimiento de 14 días por ser un servicio de ocio con fecha (art. '
         '103.l del TRLGDCU); el plan B de lluvia no es fuerza mayor; el fuero, el del domicilio del consumidor (art. '
         '90.2). La señal es a cuenta del precio, no «arras»')
#: Electricidad (SPEC D11): igual en Word, checklist, calculadora, contrato y ficha.
ELECTRICIDAD = ('ELECTRICIDAD (SPEC D11, igual en todos los ficheros): una cafetera de dos grupos consume de 2,4 a 4,5 kW; '
                'un enchufe de 16 A a 230 V da unos {TE_KW_ENCHUFE} kW; por eso la del caso es de 3,5 kW como máximo o se '
                'pide una toma dedicada; si no la hay, generador inverter (de 5 kVA o más) o baterías de litio, '
                'silenciosas para las bodas. El contrato del kit pide la toma por escrito. Nunca «enchufa en cualquier '
                'finca»')

#: Lo que tiene que contar cada sección (español de España, para el mercado español; research §0-§8 y SPEC D10-D16).
#: Cifras del Excel, de la calculadora y de la tabla de escalado = tokens.
PISTAS = {
    1: 'Qué es el negocio: una barra de café de especialidad para eventos que va en furgoneta, con barra-carro, cafetera '
       'de dos grupos, molinos y su propia energía, y que trabaja POR ENCARGO para bodas, empresas, congresos y '
       'celebraciones privadas, con unas pocas jornadas de venta directa en mercados y festivales con canon del '
       'organizador. No es venta diaria en la calle (ese es otro negocio). Una SL unipersonal con el titular de '
       'barista y un camarero/a fijo discontinuo, y su almacén base (nave o garaje con fregadero). Arranca en MARZO '
       '(el Mes 1 del Excel es marzo). Cifras clave por token: {EVENTOS_ANO} eventos al año de {INVITADOS_EVENTO} '
       'invitados de media a {PRECIO_INVITADO} por invitado sin IVA (la factura media de un evento es de '
       '{VENTA_EVENTO_MEDIO}), ventas {VENTAS_A1}, resultado neto {NETO_A1} ({NETO_PCT_A1}), inversión '
       '{INVERSION_TOTAL} (de la que {INVERSION_14_PARTIDAS} son el equipo y la puesta en marcha), préstamo {PRESTAMO} '
       'y equilibrio de caja en {BE_EVENTOS_ANO_CAJA} eventos del tamaño medio. Qué contiene el kit: este plan de '
       'negocio de 10 secciones, el Excel del plan financiero de 9 hojas, el checklist de apertura de 80 tareas en 6 '
       'fases, la calculadora de escandallo y presupuesto (coste de 10 bebidas y precio por invitado con su logística, '
       'su cobro y su cancelación), el modelo de contrato de servicio y la guía de equivalencias para Latinoamérica. Y '
       'el hallazgo que lo distingue, en una frase: el negocio es mano de obra y kilómetros, no mercancía; la mercancía '
       'es la partida pequeña ({MERCANCIA_PCT_A1} de las ventas) y el personal la grande ({PERSONAL_PCT_A1}).',
    2: 'Tipos de barra y por qué esta: barra-carro con furgoneta (la del caso: entra en salones, hoteles y pabellones), '
       'Piaggio Ape (vende la foto en las bodas, pero es un ciclomotor de 45 km/h como máximo: para ir lejos va en '
       'remolque o furgoneta y no entra en un pabellón) y remolque cafetería homologado (hasta 750 kg no lleva matrícula '
       'propia y sí tarjeta ITV). LAS TRES CONFIGURACIONES (sin Excel, del research): mínima, con barra-carro, cafetera '
       'de dos grupos o reacondicionada, un molino, depósitos y menaje, con vehículo propio y sin generador, unos '
       '12.000-15.000 € (para probar con empresas y fincas con toma de 16 A; sin enchufe no hay servicio); la del caso, '
       'furgoneta + barra-carro + generador, {INVERSION_14_PARTIDAS}; y la de imagen, Ape o remolque homologado más el '
       'vehículo de traslado, unos 55.000-65.000 € (bodas premium y activaciones de marca). La propuesta: café de '
       'especialidad (sólo con la ficha del tostador, 80 puntos SCA o más; nada de torrefacto), leches vegetales con su '
       'jarra, loza en bodas y empresa, bollería de obrador servida tal cual y un precio claro por invitado con su '
       'logística. Las dos líneas del Excel: dulces y bollería {PCT_DULCES} y bebidas {PCT_BEBIDAS}, todo al 10 % de '
       'IVA. Sin alcohol en la carta (la barra de cócteles es otro plan). La MEZCLA del caso, con su lógica: 30 bodas '
       '(120 invitados a 9,00 € sin IVA, {TICKET_BODAS} por boda), 40 eventos de empresa (80 a 8,00 €, '
       '{TICKET_EMPRESA}), 22 jornadas de congreso o feria con stand de marca (300 asistentes a 4,50 €, '
       '{TICKET_CONGRESOS}), 25 celebraciones privadas y rodajes (50 a 9,50 €, {TICKET_PRIVADOS}) y 12 jornadas de '
       'venta directa (unas 250 tazas a 3,00 €, {TICKET_VENTA_DIRECTA} brutos): {MEZCLA_SERVICIOS} servicios y '
       '{MEZCLA_VENTAS}, que el Excel redondea a {EVENTOS_ANO} eventos de {INVITADOS_EVENTO} invitados a '
       '{PRECIO_INVITADO} ({PRECIO_INVITADO_IVA} con IVA). La venta directa es {CUOTA_FERIAS} de las ventas.',
    3: 'Mercado en España con fuente. Búsquedas mensuales en Google España (DataForSEO, 28 de octubre de 2026): «coffee '
       'truck», «coffee cart» y «food truck cafetería» 90 cada una; «café para eventos» y «carrito de café» 40; '
       '«cafetería móvil» y «barra de café» 30; «barista para eventos» 20; «montar una cafetería móvil», sin dato. En '
       'México busca bastante más: «cafetería móvil» 590, «barra de café para eventos» 480, «carrito de café» 480. '
       'Lectura: el que va a montar uno busca poco y decide con datos; el cliente (novios, empresas, agencias) llega por '
       'portales de bodas, planners y recomendación. La intención de «café para eventos» mezcla el coffee break del '
       'catering con la barra de barista: el hueco es la barra. Precios publicados en Bodas.net (consulta del 28 de '
       'octubre de 2026, precios «desde» de escaparate y sin desglose: sirven para situarse, no son precios cerrados): desde 295 € (2 horas '
       'ilimitadas, Osuna), 300 € (Piaggio Ape, Málaga), 450 € (de 20 a 100 invitados, Málaga), 650 € (3 horas, hasta '
       '250 invitados, Barcelona), 700 € (de 50 a 800, Barcelona) y 1.300 € con IVA (Madrid); señal del 30-50 %, horas '
       'extra de 37 a 50 € y desplazamiento por kilómetro (0,45 € en una ficha) o con un recargo fijo. Nadie publica precio por invitado y hora: la '
       'calculadora del kit lo hace. Estacionalidad del plan con el Mes 1 en marzo: los picos son mayo y junio (bodas, '
       'comuniones y congresos) y septiembre y octubre; los valles, agosto y enero. El hueco de lo que sale en Google '
       '(tableros de Pinterest, vendedores de vehículos y una guía de un vendedor de vasos): nadie explica el precio por '
       'invitado, la electricidad, la comida testigo, el vaso «compostable» ante la Ley 7/2022 ni la diferencia entre '
       'evento contratado y venta ambulante. NADA de tamaños de mercado sin fuente ni «demanda creciente».',
    4: 'Competencia por categorías, sin nombres de empresas ni cifras inventadas: los tostadores que montan su propia '
       'barra móvil (el rival más fuerte en ferias y congresos); los coffee carts y coffee trucks para bodas de las '
       'grandes ciudades (el pack de 3 horas con mínimo es el estándar urbano); los Ape de un solo barista (precio bajo, '
       'poco radio y poca capacidad); el coffee break del catering (cafeteras de cápsula o termos, sin barista); el '
       'alquiler de cafeteras sin barista; las barras para ferias sin acometida de agua. Dónde gana este concepto: '
       'precio por invitado y hora con su mínimo y sus kilómetros (nadie lo publica), bebidas por invitado y baristas '
       'por pico, la electricidad resuelta antes de firmar, la loza frente al vaso con precio aparte, los alérgenos de '
       'las bebidas vegetales y un contrato claro (señal, cancelación por tramos, toma de corriente y agua exigidas al '
       'recinto). El riesgo: la agenda (por debajo de {BE_EVENTOS_ANO_CAJA} servicios del tamaño medio el primer año, y de '
       '{BE_EVENTOS_CAJA_A2} y {BE_EVENTOS_CAJA_A3} el segundo y el tercero, no hay caja) y los kilómetros; cómo se defiende '
       '(planners y fincas fijas, empresas que repiten, congresos con calendario).',
    5: 'Marketing y captación: el café se contrata DESPUÉS que la finca y el catering (de una semana a seis meses de '
       'antelación según el proveedor), así que la captación va a quien decide antes: wedding planners y fincas de tu '
       'zona (correo personal y cata con la barra montada), portales de bodas con fotos y precio «desde» con lo que '
       'incluye, una feria nupcial al año, agencias de eventos y organizadores de congresos (pausas de café y stands de '
       'marca: es la tipología que sostiene el equilibrio), empresas (pop-up en la oficina, presentaciones, Navidad; '
       'LinkedIn), Instagram y TikTok con servicios reales, perfil de empresa en Google con reseñas tras cada evento y '
       'WhatsApp Business. Venta directa: elige mercados y festivales por su público y su canon (porcentaje o cuota fija '
       'convertida a porcentaje), sin pisar la calle. Presupuesto de marketing {MARKETING_ANO} al año más la marca, la '
       'web, las fotos y el dossier ({MARCA_WEB}) y el lanzamiento ({LANZAMIENTO}), que van en la inversión. CÓMO SE '
       'PRESUPUESTA (la calculadora del kit): por invitado y por horas, con el desplazamiento aparte por kilómetro y sin '
       'margen; su boda de ejemplo (120 invitados, barra de 3 horas tras la cena, en loza) sale a un precio MÍNIMO de '
       '{EJ_BODA_PRECIO} por invitado sin IVA para llegar al margen objetivo del 55 % ({EJ_BODA_TOTAL} con IVA y desplazamiento); la boda media del '
       'plan, a 9,00 €, deja más margen; el congreso de ejemplo (300 asistentes, jornada con dos pausas) sale a '
       '{EJ_CONGRESO_PRECIO} por asistente. ' + COBRO + '.',
    6: 'Operaciones. UN EVENTO TIPO, de principio a fin: briefing (invitados, horas, carta, alergias, toma eléctrica, '
       'agua y acceso), visita técnica o fotos del recinto, cálculo con la calculadora, pedido de café, leche y '
       'bollería, carga con lista (depósitos llenos de agua de red, leche en neveras con acumuladores), salida con '
       'margen y llegada una hora antes, montaje y calibrado del molino, servicio (una jarra por cada leche y purga '
       'entre leches), desmontaje, limpieza, agua gris a un punto autorizado y vuelta a la base: un servicio «de 2 '
       'horas» es una jornada de 7 a 9 horas. LA TABLA DE ESCALADO (la misma que la calculadora y la hoja Instrucciones; '
       'estimación del kit con ratios de EE. UU.), para una barra de {TE_HORAS} horas con {TE_BEBIDAS_INVITADO} bebidas '
       'por invitado: 50 invitados, {TE50_BEBIDAS} bebidas, {TE50_BARISTAS} barista, {TE50_CAFETERAS} cafetera, '
       '{TE50_KG_CAFE} kg de café, {TE50_L_LECHE} l de leche, {TE50_KW} kW ({TE50_TOMA}); 100 invitados, '
       '{TE100_BEBIDAS} bebidas, {TE100_BARISTAS} baristas, {TE100_CAFETERAS} cafetera, {TE100_KG_CAFE} kg y '
       '{TE100_L_LECHE} l; 200 invitados, {TE200_BEBIDAS} bebidas, {TE200_BARISTAS} baristas, {TE200_CAFETERAS} '
       'cafeteras, {TE200_KG_CAFE} kg, {TE200_L_LECHE} l y {TE200_KW} kW ({TE200_TOMA}); 300 invitados, '
       '{TE300_BEBIDAS} bebidas, {TE300_BARISTAS} baristas y {TE300_CAFETERAS} cafeteras. Bebidas por invitado: hasta '
       '2 horas 1,0; de 2 a 4 horas 1,3-1,5; de 4 a 6 horas 1,5-1,8; jornada 2,0-2,5; por la mañana un 20-30 % más y '
       'en una boda de noche un 10 % menos; un barista con dos grupos saca unas 50-60 bebidas por hora. ' + ELECTRICIDAD
       + '. Coste de las bebidas (calculadora): un espresso {COSTE_ESPRESSO} de producto, un latte {COSTE_LATTE}, y la '
       'mezcla {COSTE_MEDIO_BEBIDA} de media más {COSTE_MEDIO_ENVASE} de vaso y tapa cuando no es loza; el coste de '
       'mercancía del Excel ({COSTE_BEBIDAS} de las bebidas) es la media del año con la merma, no la receta de una '
       'bebida. Equipo del caso: furgoneta usada con rotulación {FURGONETA}, barra-carro con carpa e iluminación '
       '{BARRA}, cafetera {CAFETERA}, molinos {MOLINOS} (el de descafeinado, porque el invitado español lo pide de '
       'máquina), energía {ENERGIA}, agua e higiene {AGUA}, frío {FRIO}, menaje y loza para 150 {MENAJE}. Base: '
       '{CUOTA_BASE_MES} al mes. Vasos: loza en bodas y empresa; el de un solo uso, con su precio aparte en el tique, '
       'en la venta directa; en ferias y festivales, el sistema de vaso reutilizable del organizador. Mantenimiento de '
       'la cafetera y los molinos {MANTENIMIENTO_CAFETERA} al año.',
    7: 'Equipo (4 filas en la hoja Personal): el titular, barista, que vende, compra, conduce y sirve en cada evento '
       '({SUELDO_TITULAR} brutos al mes en 14 pagas; como administrador de la SL cotiza en el régimen de autónomos: '
       'confírmalo con tu gestoría; como autónomo sin SL, su sueldo es el beneficio); un camarero/a de barra fijo '
       'discontinuo al 36 % de jornada (unas 650 horas al año: segundo barista en bodas, congresos, ferias y la mitad '
       'de los eventos de empresa; {BRUTO_CAMARERO} brutos al mes de su fila); y dos filas pequeñas de la bolsa de fijos '
       'discontinuos: suplencias y refuerzo de temporada, y un tercer barista para los eventos grandes que piden una '
       'segunda estación (una baja concreta se cubre con contrato de sustitución, art. 15.3). {PLANTILLA_PERSONAS} filas y {JORNADAS} jornadas completas equivalentes, coste {PERSONAL_A1} '
       '({PERSONAL_PCT_A1} de las ventas), cobertura de horas {COBERTURA_HORAS} ({HORAS_CONTRATADAS} horas contratadas '
       'frente a {HORAS_NECESARIAS} de eventos: {HORAS_EVENTO} horas por evento con {PERSONAS_EVENTO} personas de '
       'media; el resto son la oficina, las compras y la limpieza de la base). La plantilla crece con personas: '
       '{INCORPORACIONES_A2} de incorporaciones el año 2 y otro tanto el año 3. «Barista» no es categoría del convenio: '
       'se contrata como camarero/a del convenio provincial de hostelería (el art. 4 del VI Acuerdo Laboral de ámbito '
       'Estatal para el sector de Hostelería incluye las «instalaciones fijas o móviles»), fijo discontinuo con '
       'llamamiento (art. 16 del Estatuto de los Trabajadores), siempre por encima del SMI de 2026 ({SMI_ANUAL} al '
       'año) en proporción a la jornada; alta en la Seguridad Social antes de cada llamamiento; registro de jornada '
       '(art. 34.9); nunca autónomos que te facturan con tu horario (falso autónomo, art. 1.1). Formación de higiene '
       'acreditada por la empresa (el antiguo título de manipulador ya no se exige) con leche, agua y alérgenos; '
       'formación de barista (receta de la casa, calibrado, texturizado); prevención de riesgos (vapor, cargas, '
       'conducción).',
    8: 'Plan financiero, TODO por token: inversión {INVERSION_TOTAL} = compras {CAPEX} (furgoneta, equipo y puesta en '
       'marcha {INVERSION_PARTIDAS} con los imprevistos de la furgoneta, más la fianza {FIANZA} y {RENTA_PREVIA} de '
       'cuota antes del primer evento) + fondo de maniobra {FONDO_MANIOBRA}; IVA de la inversión {IVA_INVERSION}; '
       'necesidad de caja {NECESIDAD_CAJA}; financiación {RECURSOS_PROPIOS} propios + préstamo {PRESTAMO} al '
       '{TIPO_PRESTAMO}, {PLAZO_PRESTAMO} años con {CARENCIA} de carencia, cuota {CUOTA_ANUAL}. Cuenta de resultados de '
       '3 años: ventas {VENTAS_A1}/{VENTAS_A2}/{VENTAS_A3}; margen bruto {MARGEN_BRUTO_PCT_A1} (después de TODOS los '
       'costes variables: mercancía {MERCANCIA_PCT_A1}, consumibles, canon de ferias, medios de pago y varios); personal '
       '{PERSONAL_A1}; cuota del almacén base {CUOTA_BASE_ANO}; resultado de explotación antes de amortizaciones e '
       'intereses {EBITDA_A1} ({EBITDA_PCT_A1}); neto {NETO_A1}/{NETO_A2}/{NETO_A3} '
       '({NETO_PCT_A1}/{NETO_PCT_A2}/{NETO_PCT_A3}; el año 3 tributa ya al tipo general del Impuesto de Sociedades). '
       'CRECIMIENTO tal cual lo hace el Excel: suben los invitados por evento un {CREC_A2} y un {CREC_A3} (de '
       '{INVITADOS_EVENTO} a {INVITADOS_EVENTO_A2} y {INVITADOS_EVENTO_A3}) con los mismos eventos, que en euros es como '
       'hacer unos {EVENTOS_EQUIVALENTES_A2} y {EVENTOS_EQUIVALENTES_A3} eventos del tamaño del año 1; la plantilla '
       'crece con personas ({INCORPORACIONES_A2} al año), no con un porcentaje. IVA: todo al 10 %, en la barra y en la '
       'feria. EQUILIBRIO, con las dos lecturas separadas y cada una con su nombre: contable, {BE_INVITADOS_EVENTO} '
       'invitados por evento con los {EVENTOS_ANO} eventos del caso, o {BE_EVENTOS_ANO} eventos del tamaño medio '
       '(ingresos {BE_INGRESOS}; holgura {HOLGURA_CONTABLE}); de caja, {BE_EVENTOS_ANO_CAJA} eventos del tamaño medio y '
       'holgura {HOLGURA_CAJA}, que es la del PRIMER año (sólo intereses por la carencia); desde el segundo, con la '
       'devolución del principal, la holgura baja a {HOLGURA_CAJA_A2} ({BE_EVENTOS_CAJA_A2} eventos del tamaño del año '
       '1) y en el tercero queda en {HOLGURA_CAJA_A3} ({BE_EVENTOS_CAJA_A3}): esos son los años que hay que vigilar. '
       'DSCR mínimo {DSCR_MIN}. TESORERÍA: el Mes 1 es marzo; la rampa arranca al {RAMPA_MES1} y llega al ritmo de '
       'crucero en {MESES_RAMPA} meses; el saldo mínimo es {SALDO_MINIMO} en el Mes {MES_SALDO_MINIMO} '
       '({MES_SALDO_MINIMO_NOMBRE}) y el año acaba (febrero) con {SALDO_MES12}; las pagas extra salen en julio (Mes 5) '
       'y diciembre (Mes 10); las señales de los particulares no se modelan: la caja real es algo mejor. Payback: el '
       'Excel marca «{PAYBACK}» en la fila «Payback del proyecto (años), antes de la deuda» (cítalo así, entre '
       'comillas, o en mitad de frase como «{PAYBACK_TEXTO}»), y {PAYBACK_CAPEX} años sobre el CAPEX sin el fondo de '
       'maniobra. Escenarios: pesimista ({ESC_PES_EVENTOS} eventos de {ESC_PES_INVITADOS} invitados a '
       '{ESC_PES_PRECIO}: ventas {ESC_PES_VENTAS}, neto {ESC_PES_NETO}) y optimista ({ESC_OPT_EVENTOS} de '
       '{ESC_OPT_INVITADOS} a {ESC_OPT_PRECIO}: ventas {ESC_OPT_VENTAS}, neto {ESC_OPT_NETO}). El Excel manda: si '
       'cambias una celda verde, el documento se queda atrás.',
    9: 'Marco legal con su cita (sólo esto, dicho así; lo marcado «compruébalo», dilo así y sin cifra): SL unipersonal '
       '(capital desde 1 €, Ley 18/2022) o autónomo; IAE (RDLeg 1175/1990): epígrafe 677.9 para los eventos contratados '
       'y, si vendes en mercados o en la vía pública, también el 675, como criterio de asesoría: confírmalo con tu '
       'gestoría; exento de cuota con menos de 1 millón de cifra de negocio; tus facturas a empresas no llevan '
       'retención de IRPF (art. 95.6 del Reglamento del IRPF). Sanidad: declaración responsable en el registro '
       'sanitario de la comunidad autónoma donde tiene su base (RD 1021/2022); el vehículo y la barra forman parte del '
       'establecimiento; el RGSEAA sólo si vendes a otros negocios; la base con fregadero (art. '
       '13.5.b: lo que se sirve en eventos no se prepara en casa). Comida testigo (RD 1086/2020, arts. 2.h, 30.8.d y '
       '30.10): con salado (sándwiches, tostas, quiches), a 4 °C o menos (o congelada), '
       'una ración de 100 g o más de cada uno durante 7 días, en cada evento; las bebidas y la bollería servida tal '
       'cual quedan fuera según nuestra lectura, sin criterio oficial: confírmalo con tu autoridad sanitaria. Agua de '
       'los depósitos: agua de consumo, de la que respondes hasta el punto de uso (RD 3/2023, arts. 2.a, 65.3 y 66.b). '
       'Alérgenos (RD 126/2015): leche, también la sin lactosa, soja, frutos de cáscara y avena, que es cereal con '
       'gluten salvo la certificada; una jarra por cada leche; cartel o información oral registrada por escrito. Vasos: '
       'el de papel con forro de PE o PLA también es plástico (Ley 7/2022, art. 2.aa) y se cobra aparte en el tique '
       '(art. 55.2); pajitas y agitadores de plástico, prohibidos (art. 56); los promotores de eventos festivos tienen '
       'que ofrecer alternativas al vaso de un solo uso (RD 1055/2022, art. 7.6); no está claro que una boda o un evento '
       'de empresa cuenten como evento festivo, así que loza por defecto en bodas y empresa. Venta en mercados y vía pública: venta no sedentaria con autorización municipal (RD 199/2010); el '
       'evento contratado en un recinto privado es un servicio. Vehículo: remolque de hasta 750 kg sin matrícula propia y con '
       'tarjeta ITV (Reglamento General de Vehículos, arts. 25-26); la furgoneta con mueble, fregadero o depósitos '
       'fijos es una reforma: informe e ITV (compruébalo con tu estación de ITV); el Ape 50 es un ciclomotor (45 km/h). '
       'IVA (Ley 37/1992, art. 91): todo lo que se sirve, al 10 %; extras con precio propio, al 21 %. Contratos con '
       'consumidores: sin desistimiento en un servicio de ocio con fecha cerrado a distancia (art. 103.l del TRLGDCU), '
       'fuero del consumidor (art. 90.2), señal a cuenta del precio. Personal: convenio provincial de hostelería (ALEH '
       'VI, art. 4), Estatuto de los Trabajadores (arts. 1.1, 16 y 34.9). Facturación con software Veri*factu (consulta '
       'con tu gestoría la fecha que te aplica). Ruido del generador y ordenanzas: pregunta en tu ayuntamiento y en el '
       'recinto. Lo que no esté aquí no se afirma: «compruébalo con tu gestor, tu ayuntamiento o tu autoridad '
       'sanitaria».',
    10: 'Conclusiones con tokens (viabilidad, holgura de caja del año 1 y de los años 2 y 3, DSCR mínimo, saldo mínimo, '
        'payback citado como en el §8) y los riesgos de una cafetería móvil y cómo se mitigan (research §0 y §8, uno '
        'por uno): la agenda (por debajo de los equilibrios de caja de cada año no hay caja: congresos con calendario, planners y '
        'empresas que repiten); presupuestar el servicio de 2 horas como si fueran 2 horas (es una jornada de 7 a 9); '
        'firmar sin saber la potencia eléctrica (toma por escrito o generador); el vaso «compostable» como si no fuera '
        'plástico; anunciar «café de especialidad» sin la ficha del tostador; la jarra única para todas las leches '
        '(alérgenos); vender en la calle como si fuera un evento (autorización municipal); los kilómetros sin cobrar '
        '(desplazamiento aparte); y el barista como autónomo que factura (falso autónomo). El plan de acción en 6 fases '
        'del checklist (80 tareas: 12/16/14/10/14/14) y los primeros 90 días: tres catas con planners y fincas, alta en '
        'los portales de bodas, dos agencias de congresos, el primer evento y la revisión de costes reales frente a la '
        'calculadora. Cierra con el siguiente paso: completar el Excel con tus cifras y presupuestar tu primer evento '
        'con la calculadora y el contrato del kit.',
}

#: Prohibidos en el texto (SPEC D12: los 12 del research §8 + los del brief de la pizzería; F1-camino §3): sellos y
#: palabras vetadas, normas derogadas, restos de los moldes (Food Truck —semilla—, Parrillero —contenido—, Finca) y las
#: frases del motor sin traducir. SIN «bollería», «leche», «generador», «furgoneta», «remolque» ni «aparcamiento»:
#: aquí son el oficio. Los usa también `barrido_es.py` sobre los xlsx y los docx.
PROHIBIDOS = [
    # familia y SPEC D12 (brief de la pizzería)
    r'\bfreelance', r'validad[oa]s?', r'Espa[ñn]a,? 2026', r'carn[eé]t? de manipulador(?! ya no existe)',
    r'tarifa plana', r'\bCNAE\b', r'(?<!inscrito en el )\bRGSEAA\b(?!.{0,80}(s[oó]lo|otros (establecimientos|negocios)))',
    r'licencia de apertura', r'393/2007', r'versi[oó]n (1\.1|2\.2|anterior)', r'\bv1\.1\b', r'solopreneur',
    r'\bde \d+(,\d+)? ?%', r'Comunitat', r'\b15 a[ñn]os', r'[a-záéíóúñ,;] Payback\b', r'demanda creciente',
    r'sin licencias?\b', r'sin registro sanitario', r'tarifas? (de|del) mercado',
    # research §8 (los 12)
    r'comida testigo no (se )?aplica nunca', r'nunca (se )?aplica la comida testigo',
    r'compostables?[^.;]{0,40}sin pl[aá]stico', r'exent[oa]s? de la Ley 7/2022',
    r'\b(ofrec\w*|incluy\w*|pon\w*|reparte\w*) (las |los |unas |unos )?(pajitas|agitadores) de pl[aá]stico',
    r'(enchuf\w*|conect\w*)[^.;]{0,30}cualquier (finca|enchufe|toma)', r'cualquier enchufe (sirve|vale|basta)',
    r'desde 3\.000 ?€', r'cafetera dom[eé]stica (sirve|vale|basta)',
    r'(facturaci[oó]n|ingresos|beneficios?|rentabilidad|ventas) garantizad', r'recuperas? la inversi[oó]n en \d',
    r'servicio (de barra |de caf[eé] )?(va |tributa |se factura )?al 21',
    r'Ape[^.;]{0,40}(va|circula|puede ir) por (autov[ií]a|autopista)',
    r'\bcervezas?\b', r'espresso martini', r'alcohol (que sale|del canal|servido|incluido)',
    # restos del Food Truck (semilla)
    r'(?<!«)food ?truck', r'\bcami[oó]n\b', r'ventanilla',
    # restos del Parrillero (contenido clonado) y de la Finca
    r'parrill', r'\basad[oa]s?\b', r'\bbrasas?\b', r'carb[oó]n', r'\bcarnes?\b', r'cocina de apoyo', r'show de fuego',
    r'\bATP\b', r'\bcruz\b', r'canon del catering', r'plan-negocio-(parrillero|food-truck|finca)',
    # frases del motor sin traducir
    r'\bclientes?/d[ií]a', r'\bd[ií]as de apertura', r'\bdel local\b', r'\bel local\b', r'\ben sala\b', r'\bticket\b',
    r'\bdelivery\b', r'\bcubiertos?\b', r'\bcomensal', r'pan com[uú]n',
]
#: Cifras que el texto puede llevar escritas (normas, research con fuente, mezcla y estructura del caso, equipo,
#: electricidad, checklist). Todo lo demás, token.
PERMITIDAS = set('''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 35 36 37 38
40 45 50 55 56 60 65 66 70 75 80 90 99 100 103 110 120 126 130 140 150 160 170 180 200 230 250 300 390 400 450 480 500
590 650 675 677.9 700 750 800 1.000 1.021 1.055 1.086 1.175 1.300 2.000 3.000 1,0 1,3-1,5 1,5-1,8 2,0-2,5 1,1 1,4 1,6
2,4 2,4-4,5 4,5 3,5 3,7 0,45 37-50 30-50 50-60 100-120 7-9 20-30 150-200 12.000-15.000 55.000-65.000 4.300-5.350
6.000-10.000 300.000-600.000 8,50 9,00 8,00 4,50 9,50 3,00 22.200 2.900 8.100 2.a 2.aa 2.h 13.5.b 30.8.d 30.10 55.2 65.3
66.b 7.6 75.Dos 91.Uno.2.2 91.Uno.1.1 95.6 103.l 90.2 34.9 16 25-26 1.1 18/2022 1175/1990 1021/2022 1086/2020 3/2023
126/2015 7/2022 1055/2022 199/2010 37/1992 31/1995 1169/2011 852/2004 1007/2023 2822/1998 15.3 2026 2025 2024 2023 2022
2010 2015 2020 1992 1990 1998 1995 12/16/14/10/14/14 28 B96'''.split())
RX_NUM = re.compile(r'(?<![\w{])[−+]?\d[\d.,/:−-]*\d|(?<![\w{])\d')
#: Caracteres admitidos además del latín básico/extendido: tipografía española y los signos (−, ≤, ≥, ≈, ×).
RX_RARO = re.compile(r'[^\x00-ɏ‐-‧€°→ ‑«»¿¡ºª·…–—“”‘’−≤≥≈²×]')


def ranuras():
    d = json.load(open(os.path.join(BP4, 'docx_es_cat.json'), encoding='utf-8'))['parrafos']
    fmt, ofi = {}, {}
    for t in ('fin_es_a', 'fin_es_b'):
        fmt.update(json.load(open(os.path.join(GEMELA_FORMATO, t + '.json'), encoding='utf-8')))
    for t in ('par_es_a', 'par_es_b'):
        ofi.update(json.load(open(os.path.join(GEMELA_OFICIO, t + '.json'), encoding='utf-8')))
    fuera = []
    for k in sorted(d, key=int):
        v = d[k]
        if v['rol'] != 'cuerpo':
            continue
        fuera.append({'i': int(k), 'seccion': int(v['seccion']), 'palabras_objetivo': int(v['palabras']),
                      'molde_ft_es': v['texto'], 'gemela_formato_finca_es': fmt.get(k, ''),
                      'gemela_oficio_parrillero_es': ofi.get(k, '')})
    return fuera


def preparar():
    if not os.path.exists(CIFRAS):
        raise SystemExit('falta %s: corre antes cifras_caf_es.py en el VPS y cópialo aquí' % CIFRAS)
    cif = json.load(open(CIFRAS, encoding='utf-8'))['tokens']
    usados = set(re.findall(r'\{([A-Z0-9_]+)\}', ' '.join(PISTAS.values())))
    sin = sorted(usados - set(cif))
    if sin:
        raise SystemExit('las PISTAS citan tokens que no están en cifras_caso_es.json: %s' % sin)
    os.makedirs(TANDAS, exist_ok=True)
    rs = ranuras()
    for tanda, secs in (('caf_es_a', range(1, 6)), ('caf_es_b', range(6, 11))):
        sel = [r for r in rs if r['seccion'] in secs]
        ent = {
            'tanda': tanda, 'producto': 'Plan de Negocio: Cafetería Móvil para Eventos ES 1.0 (aichef.pro, 45 €)',
            'salida': 'scripts/productos-digitales/plan-cafeteria-movil/textos/%s.json' % tanda,
            'formato_salida': '{"<i>": "<párrafo en español>", …} con TODOS los "i" de "parrafos" y nada más',
            'brief': 'scripts/productos-digitales/plan-cafeteria-movil/BRIEF-REDACTORES.md (léelo entero antes)',
            'research': RESEARCH + ' (§0 hallazgos, §1 modelo, §2 normativa, §3 precios, §4 caso, §5 competencia, §6 '
                                   'SERP, §8 prohibidos: material de apoyo; la pista de la sección manda)',
            'cobro_y_cancelacion (SPEC D16, literal en el fondo)': COBRO,
            'electricidad (SPEC D11, literal en el fondo)': ELECTRICIDAD,
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
    if not tanda:
        print('ERROR falta --tanda (caf_es_a o caf_es_b)')
        return 2
    pe = os.path.join(TANDAS, tanda + '.entrada.json')
    ps = os.path.join(TEXTOS, tanda + '.json')
    if not os.path.exists(pe):
        print('ERROR no existe la entrada %s: corre antes «tandas_docx.py preparar»' % os.path.relpath(pe, AQUI))
        return 2
    if not os.path.exists(ps):
        print('ERROR no existe la salida del redactor %s' % os.path.relpath(ps, AQUI))
        return 2
    ent = json.load(open(pe, encoding='utf-8'))
    crudo = open(ps, encoding='utf-8').read()
    if not crudo.strip():
        print('ERROR %s está vacío: el redactor tiene que escribir {"<i>": "<párrafo>", …} con las %d ranuras' % (
            os.path.relpath(ps, AQUI), len(ent['parrafos'])))
        return 1
    try:
        sal = json.loads(crudo)
    except ValueError as e:
        print('ERROR %s no es JSON válido (%s)' % (os.path.relpath(ps, AQUI), e))
        return 1
    if not isinstance(sal, dict):
        print('ERROR %s tiene que ser un objeto {"<i>": "<párrafo>"}, no %s' % (os.path.relpath(ps, AQUI),
                                                                             type(sal).__name__))
        return 1
    tokens = set(ent['tokens'])
    err, avi = [], []
    esperadas = set(str(r['i']) for r in ent['parrafos'])
    if set(sal) != esperadas:
        err.append('ranuras: faltan %s · sobran %s' % (sorted(esperadas - set(sal), key=int),
                                                       sorted(set(sal) - esperadas)))
    total = 0
    for r in ent['parrafos']:
        t = sal.get(str(r['i']), '')
        if not isinstance(t, str):
            err.append('%d: el valor tiene que ser texto' % r['i'])
            continue
        if not t.strip():
            if str(r['i']) in sal:
                err.append('%d: párrafo vacío' % r['i'])
            continue
        n = len(t.split())
        total += n
        if not (0.7 * r['palabras_objetivo'] <= n <= 1.35 * r['palabras_objetivo']):
            avi.append('%d: %d palabras (objetivo %d)' % (r['i'], n, r['palabras_objetivo']))
        for tok in re.findall(r'\{([A-Z0-9_]+)\}', t):
            if tok not in tokens:
                err.append('%d: token inexistente {%s}' % (r['i'], tok))
        for rx in PROHIBIDOS:
            if re.search(rx, t, re.I if not rx.startswith('[a-z') else 0):
                err.append('%d: prohibido /%s/' % (r['i'], rx))
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
    sys.exit(preparar() or 0 if a.accion == 'preparar' else check(a.tanda))
