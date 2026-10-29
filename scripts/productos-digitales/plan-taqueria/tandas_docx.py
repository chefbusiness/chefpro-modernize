#!/usr/bin/env python3
"""
tandas_docx.py — Taquería ES 1.0 (F1-camino §4): prepara y valida las dos tandas de redacción del plan de negocio
(docx). Copia adaptada de `plan-pizzeria/tandas_docx.py`.

Las 61 ranuras de texto del docx del Food Truck ES (131 párrafos, 10 Heading 1; mapa en
`business-plans-en-4/docx_es_cat.json`) se escriben NUEVAS, en español, para la taquería:
  taq_es_a = §1-5 (29 ranuras) · taq_es_b = §6-10 (32 ranuras).
Gemela de FORMATO: el texto de la Pizzería ES 1.0 en la misma ranura (`plan-pizzeria/textos/piz_es_{a,b}.json`, la ES
1.0 de local fijo con tokens, ya revisada): sirve para ver cómo se escribe una ranura con tokens, nunca su contenido.
No hay versión anterior: el material es el research (`F1-research-taqueria.md`) y las pistas de abajo. Las cifras del
Excel (y de la calculadora del trompo y escandallo) van SIEMPRE como token {ASI} (`cifras_caso_es.json`, con `--calc`);
`docx_taq_es.py` las resuelve al ensamblar. Sólo lee JSON: corre en el Mac.

    python3 tandas_docx.py preparar                       # tandas/taq_es_{a,b}.entrada.json
    python3 tandas_docx.py check --tanda taq_es_a         # valida textos/taq_es_a.json (salida del redactor)

Sesión Claude Code, 29-oct-2026.
"""
import argparse
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BP4 = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
GEMELA = os.path.join(os.path.dirname(AQUI), 'plan-pizzeria', 'textos')
TANDAS, TEXTOS = os.path.join(AQUI, 'tandas'), os.path.join(AQUI, 'textos')
CIFRAS = os.path.join(AQUI, 'cifras_caso_es.json')
RESEARCH = 'scripts/productos-digitales/plan-taqueria/F1-research-taqueria.md'

SECCIONES = {
    1: '1. Resumen Ejecutivo', 2: '2. Concepto y Propuesta de Valor', 3: '3. Análisis de Mercado',
    4: '4. Análisis Competitivo', 5: '5. Plan de Marketing y Captación', 6: '6. Plan de Operaciones',
    7: '7. Estructura Organizativa y RRHH', 8: '8. Plan Financiero', 9: '9. Aspectos Legales y Licencias',
    10: '10. Conclusiones y Plan de Acción',
}

#: La jerga del oficio (R §5): mexicanismos que son el producto, tal cual, glosados la PRIMERA vez que salen en el Word.
JERGA = ('trompo (asador vertical de carne al pastor) · taquero/a · al pastor (cerdo marinado en adobo de chiles y '
         'achiote, asado en el trompo con piña) · carnitas (cerdo confitado) · suadero (corte de res entre el vientre y '
         'la pierna, confitado) · campechano (mezcla de dos carnes) · cochinita pibil · barbacoa · gringa (tortilla de '
         'harina con pastor y queso) · orden (porción de 3-5 tacos del mismo guiso; en España, «ración») · «con todo» '
         '(cebolla y cilantro) · dorado (taco frito) · salsa macha (aceite con chiles secos, ajo y cacahuete o sésamo) · '
         'nixtamal y nixtamalizar (cocer el maíz con cal) · comal (plancha de barro o acero para la tortilla) · '
         'guisados (cazuelas de relleno) · totopos (no «nachos») · aguas frescas (jamaica, horchata, tamarindo) · '
         'taquiza (tacos para eventos fuera del local: no es este plan). QUÉ NO DECIR: «tex-mex», «gyro» como sinónimo, '
         'burritos o nachos como plato central, el 5 de mayo como fiesta nacional de México (no lo es: mejor no '
         'citarlo), «tortilla» a secas cuando se habla de la de maíz, «auténtico» como promesa o sello')

#: Lo que tiene que contar cada sección (español de España, para el mercado español; R §0-§7). Cifras del Excel y de
#: la calculadora = tokens.
PISTAS = {
    1: 'Qué es el negocio: una taquería con trompo de gas a la vista y barra de salsas, con 32 plazas (24 en mesa y 8 en '
       'barra) y una terraza de 16 de abril a octubre, en una ciudad media (150.000-300.000 habitantes), en una calle '
       'con paso cerca de una zona universitaria o de ocio; local de 80 m² con salida de humos a cubierta posible (el '
       'filtro del local), sin traspaso. Una SL unipersonal con el titular de taquero jefe, un segundo taquero, un '
       'cocinero de producción y salsas, el encargado de sala, barra y mostrador, un camarero de cenas y fines de '
       'semana y un refuerzo de fin de semana. Tortilla de maíz comprada. Carta corta: 8-10 tacos (el pastor a 3,00 € '
       'con IVA, la orden de 3 a 8,50 €), gringa a 7,50 €, quesadilla a 6,00 €, guacamole con totopos a 6,50 €, aguas '
       'frescas a 3,00 €, cerveza mexicana a 3,80 €, mezcal a 7 €. Para llevar (recogida en el local, sin comisión) y '
       'plataforma con su reparto, con techo (sin reparto propio). Abre en ENERO (el Mes 1 del Excel es enero, en el '
       'orden del calendario), de martes a domingo, comidas y cenas; cierra los lunes y 12 días en enero. Cifras clave '
       'por token: {COMENSALES_DIA} comensales equivalentes al día (sala, para llevar y domicilio) a {TICKET} por '
       'comensal sin IVA y {DIAS_APERTURA} días, ventas {VENTAS_A1}, resultado neto {NETO_A1} ({NETO_PCT_A1}), '
       'inversión {INVERSION_TOTAL} (de la que {INVERSION_PARTIDAS} son obra, cocina, equipo y puesta en marcha), '
       'préstamo {PRESTAMO} y equilibrio en {BE_COMENSALES_DIA} comensales al día. Qué contiene el kit: este plan de '
       'negocio de 10 secciones, el Excel del plan financiero de 9 hojas, el checklist de apertura de 80 tareas en 6 '
       'fases, la calculadora del trompo y escandallo (rendimiento del cono y de otras proteínas, tortilla comprada '
       'frente a nixtamal propio y escandallo de 8 tacos, la orden y la gringa con el margen en sala, para llevar y en '
       'plataforma) y la guía de equivalencias para Latinoamérica (el marco legal del plan es el español). Lo que lo '
       'distingue, en una frase: el rendimiento del trompo con números ({TACOS_POR_CONO} tacos de un cono de 15 kg en '
       'el ejemplo, estimación editable que mides tú) y todo en euros y con la norma española.',
    2: 'Tipos de taquería y por qué esta (R §3): la de barrio de mostrador y barra, con plancha y comal y sin trompo '
       '(unos 60 m², 22 plazas, ticket de unos 12,50 € sin IVA: margen justo y sin la seña del trompo); la de trompo y '
       'barra de salsas (la de este plan); la taquería-mezcalería con tortillería propia (unos 120 m², 44 plazas y '
       'terraza, ticket de unos 19,50 €): esa ya es un restaurante mexicano y la cubre la Guía Restaurante Mexicano de '
       'AI Chef Pro; y en los extremos, la de volumen (taco a 1-1,50 €, colas) y la de autor (7-8 € el taco). La '
       'propuesta: pastor del trompo a la vista, tortilla de maíz nixtamalizado, carnitas y guisados del día, barra de '
       'salsas con reglas, aguas frescas de la casa y la orden «para armar» para llevar. GLOSA LA JERGA la primera vez '
       '(ver `jerga` de la entrada): trompo, orden, gringa, campechano, suadero, «con todo». El ticket de {TICKET} es '
       'por comensal y sin IVA ({TICKET_IVA} con IVA): en sala, una orden de 3 tacos (8,50 €), medio taco suelto '
       '(1,50 €), algo de gringa o quesadilla (2,10 €), algún entrante (1,30 €), 1,1 bebidas (3,63 €) y algún postre '
       '(0,40 €) suman unos 17,43 € con IVA; el caso se queda en {TICKET} sin IVA por los combos de mediodía. Mezcla '
       'de ventas: comida {PCT_COMIDA} y bebida {PCT_BEBIDA}; en sala unos 74 % de las ventas, para llevar unos 14 % '
       'y por plataforma {DELIVERY_PCT}. Qué NO es: ni tex-mex ni burritos o nachos de plato central (se dicen '
       '«totopos»): eso pierde al cliente mexicano y al que busca la taquería.',
    3: 'Mercado en España con fuente. Búsquedas mensuales en Google España (DataForSEO, 28 de octubre de 2026): '
       '«cochinita pibil» 18.100, «tacos al pastor» 8.100, «tortillas de maíz» 4.400, «taquería» 4.400, «suadero» '
       '1.900, «salsa macha» 1.600, «comal» 1.300, «aguas frescas» 1.000, «nixtamal» 210, «masa de maíz» 110 y «trompo '
       'al pastor» 70; y apenas 10 «plan de negocio taquería», «cómo montar una taquería» o «abrir una taquería»: el '
       'oficio y el consumidor buscan mucho, el que va a abrir busca poco y decide con datos. En México, «taquería» '
       'tiene 135.000 búsquedas al mes. Precio del taco en carta, con IVA (cartas leídas en octubre de 2026, sin '
       'nombres): en Madrid, una taquería del centro con el pastor a 2,50 € (tacos desde 1,50 €) y otra de barrio con '
       'el pastor y las carnitas a 4,50 € y la gringa a 9,90 €; en Valencia, 10,90 € los 4; en Bilbao, 5,50 € los 2; '
       'en Barcelona, 16 € los 2 de autor. Lectura: taquería casual de ciudad, 2,50-3,50 € el taco; la de volumen, '
       '1-1,50 €; la de autor, 7-8 €. El caso, 3,00 €. Estacionalidad del plan, con el Mes 1 en ENERO y en el orden del '
       'calendario: enero y agosto son los meses más flojos (un 7 % del año cada uno), diciembre el pico (un 9,6 %), '
       'septiembre (la Independencia de México, el 15 y el 16) y noviembre (el Día de Muertos, el 1 y el 2) algo más '
       'fuertes, y la terraza suma de abril a octubre; entre el mejor mes y el peor hay un 37 % de diferencia: una '
       'taquería de barrio es un negocio bastante plano. El hueco: para «plan de negocio taquería» Google España no '
       'trae un solo resultado escrito para España ni en euros (planes en pesos mexicanos, trabajos de clase y foros); '
       'nadie cuenta el rendimiento del trompo con números, la temperatura del pastor marinado y de la verdura cortada '
       '(4 °C), el 21 % de las aguas frescas azucaradas para llevar, la macha en el cartel de alérgenos, la cuenta de '
       'la tortilla comprada frente al nixtamal ni el importador de chiles como riesgo. NADA de tamaños de mercado sin '
       'fuente.',
    4: 'Competencia por categorías, sin nombres de empresas ni cifras inventadas: las taquerías de volumen (taco a '
       '1-1,50 €, colas y rotación); las taquerías casuales de ciudad (2,50-3,50 €); las de autor (7-8 €, producto '
       'ibérico, reservas); los restaurantes mexicanos de mesa con barra de tequilas; las cadenas de comida «mexicana» '
       'de centro comercial (burritos y nachos); las cocinas que sólo venden por plataforma; y el kebab, que comparte '
       'el asador vertical y el cliente de cena rápida. Dónde gana este concepto: el trompo a la vista, la tortilla de '
       'maíz nixtamalizado, la barra de salsas, un precio casual (la orden de 3 a 8,50 €), la orden «para armar» para '
       'llevar y una carta corta que se escandalla taco a taco. El riesgo: la guerra de precios con las de volumen, la '
       'dependencia de la plataforma y la de un solo importador de chiles; cómo se defiende (producto, rendimiento del '
       'trompo medido, escandallo, recogida en el local, clientela que repite).',
    5: 'Marketing y captación: apertura en enero (los curiosos llegan el primer mes; la clientela fija, en un '
       'trimestre); ficha de Google Business con el horario de comidas y cenas, fotos del trompo y respuesta a cada '
       'reseña; redes con el montaje del cono, el corte y el taco de la semana; el público universitario y de ocio '
       'cercano (combos de mediodía); el calendario mexicano: la Independencia (15 y 16 de septiembre) y el Día de '
       'Muertos (1 y 2 de noviembre), sin más fechas; fidelización sencilla (tarjeta '
       'de sellos) sin cifras de conversión inventadas. PLATAFORMA FRENTE A REPARTO PROPIO (sin Excel, razonado): el '
       'plan vende por plataforma con su reparto un {DELIVERY_PCT} de las ventas ({VENTAS_PLATAFORMA_A1} al año) y paga '
       'una comisión del {COMISION_DELIVERY} ({COMISIONES_DELIVERY_A1} al año); las guías del sector sitúan el plan '
       'básico de Uber Eats en torno al 30 % más IVA, Glovo entre el 15 y el 35 % según la zona y Just Eat entre el 25 '
       'y el 35 % con su reparto, más las promociones y el envase. La tortilla llega peor tras el viaje: la orden «para '
       'armar» (tortilla y relleno aparte) lo aguanta, y por eso el techo del plan es ese {DELIVERY_PCT}. Un repartidor '
       'propio de viernes a domingo (0,35 jornada, unos 8.800 € al año con la Seguridad Social) más moto, seguro y '
       'gasolina (unos 2.500 €) cuesta unos 11.300 € para repartir esa misma venta: un 26 %, poco menos que la '
       'comisión, pero sin el escaparate de la plataforma, que es la que trae el pedido, y con el riesgo laboral; sólo '
       'compensa con pedidos propios (web o teléfono) o con una zona corta y densa, y siempre con contrato laboral. La '
       'recogida en el local no paga comisión: empújala con precio. Presupuesto de marketing {MARKETING_ANO} al año, '
       'más la marca, la web, las fotos y el lanzamiento, que van en la inversión ({MARCA_LANZAMIENTO}).',
    6: 'Operaciones de la cocina, el trompo y la sala. EL TROMPO CON NÚMEROS (la calculadora del pack, valores por '
       'defecto que son estimación del kit y editables): un cono de 15 kg de carne cruda, con un 8 % de adobo, un 35 % '
       'de merma de cocción y goteo y un 5 % de recortes, rinde un {RENDIMIENTO_TROMPO} y da {TACOS_POR_CONO} tacos de '
       '35 g servidos, unos 18,5 por kg crudo; un puesto de Ciudad de México sirve unos 25 por kg (prensa: 1.250-2.500 '
       'tacos de un trompo de 50-100 kg, unos 40 g de carne cruda por taco). Ninguna fuente publica la merma de '
       'cocción del pastor: MÍDELA (pesa el cono crudo y el sobrante al cierre con la hoja de rendimiento del Kit de '
       'Tareas Recurrentes: Taquería Mexicana y lleva la media a la calculadora: «mide en el kit, recalcula en el '
       'plan»). El taco al pastor de la carta cuesta {COSTE_TACO_PASTOR} con merma y sale a un {FC_TACO_PASTOR} de food '
       'cost sobre 3,00 € con IVA; carnitas, suadero y barbacoa rinden menos (confitado y cocción larga). Producción '
       'del caso: unos 255 tacos al día más unas 25 gringas y quesadillas, unas 280 tortillas al día; el pastor es un '
       '45 % de los tacos, unos 115 al día, unos 6,2 kg de carne cruda al día y 10-11 kg el sábado: un asador de cuatro '
       'quemadores y 35 kg cubre el pico con un cono de 15-20 kg. EQUIPO con precio y fuente: trompo {TROMPO} (en '
       'catálogo, de 1.279 a 1.784 € sin IVA), plancha y comal {PLANCHA}, freidora, fogón de carnitas, baño maría y '
       'mantenedor de tortillas {FREIDORA}, campana extractora {CAMPANA}, frío con la mesa refrigerada de salsas {FRIO} '
       'y el conducto exclusivo a cubierta {CONDUCTO}. TROMPO DE GAS O DE CARBÓN: el de gas (el del plan) cabe en una '
       'salida de humos normal, con instalación por empresa habilitada y revisión cada 5 años; el de carbón (y la '
       'parrilla de carne asada) pide además filtro de partículas en el conducto: variante SIN Excel, más inversión y '
       'una ordenanza que la admita. TORTILLA COMPRADA O NIXTAMAL PROPIO (variante SIN Excel): el caso compra unas 280 '
       'tortillas al día (unas 84.000 al año, unos 12.000 €); hacerlas ahorra unos 0,10 € por tortilla, pero pide un '
       'tortillero de 0,75 jornada (unos 18.900 € al año) y 15.000-25.000 € de molino, cocedor y tortilladora (una '
       'tortilladora automática cuesta 7.808 $ en Estados Unidos; en España no hay precio publicado): el equilibrio '
       'sale en unas {EQUILIBRIO_TORTILLAS_DIA} tortillas al día, así que el nixtamal es una decisión de producto, no '
       'de ahorro. La TAQUERÍA-MEZCALERÍA con tortillería propia, en una línea: es otro negocio, el de la Guía '
       'Restaurante Mexicano. Horario: de martes a domingo, comidas de 13:30 a 16:30 y cenas de 20:00 a 23:30; cierra '
       'los lunes y 12 días en enero. HIGIENE EN LA OPERACIÓN: el pastor marinado es preparado de carne, en cámara a '
       '4 °C o menos; sonda al inicio y a mitad del servicio y la hora límite del cono montado la fija tu APPCC '
       '(ninguna norma la da); salsas crudas, guacamole y verdura cortada a 4 °C o menos; barra de salsas con reglas '
       '(recipiente limpio en cada reposición, hora de puesta y de descarte, un utensilio por salsa); carnitas y '
       'guisados en caliente a 63 °C o más, enfriados de 60 a 10 °C en menos de 2 horas y recalentados a 74 °C durante '
       '15 segundos (art. 30 del RD 1086/2020, en la redacción del RD 1021/2022). EL IMPORTADOR de chiles secos, achiote '
       'y producto mexicano tarda semanas: stock de seguridad y segundo proveedor. Suministros {SUMINISTROS_MES} al mes '
       'de media; mantenimiento {MANTENIMIENTO_CAMPANA} al año (limpieza de la campana extractora y del conducto al '
       'menos una vez al año, el gas y el frío).',
    7: 'Equipo (7 filas en la hoja Personal): el titular, taquero jefe (marinado, trompo, compras —el importador de '
       'chiles incluido— y gestión; {SUELDO_TITULAR} brutos al mes en 14 pagas; como administrador de la SL cotiza en '
       'el régimen de autónomos: confírmalo con tu gestoría); un segundo taquero de trompo, plancha y comal que sabe '
       'marinar y cortar (el taquero único es un riesgo, no un ahorro: una baja cierra la taquería); un cocinero de '
       'producción y salsas de 30 horas (carnitas, guisados, salsas, aguas frescas y mise en place); un encargado/a de '
       'sala, barra y mostrador todo el año (caja, pedidos para llevar, la tablet de las plataformas y la información '
       'de alérgenos); un camarero/a de cenas y fines de semana de 20 horas; un refuerzo de viernes a domingo (barra, '
       'terraza y recogidas; sin reparto propio); y las suplencias de vacaciones y descansos: {PLANTILLA_PERSONAS} '
       'personas y {JORNADAS} jornadas completas equivalentes, coste {PERSONAL_A1} ({PERSONAL_PCT_A1} de las ventas), '
       'cobertura de horas {COBERTURA_HORAS} ({HORAS_CONTRATADAS} horas contratadas frente a {HORAS_NECESARIAS} '
       'necesarias); el sábado por la noche hacen falta cinco personas y el cuadrante anual no lo ve: ponlo en el turno. '
       'La plantilla crece con personas: {INCORPORACIONES_A2} de incorporaciones el año 2 y otro tanto el año 3. '
       'Convenio provincial de hostelería: el art. 4 del VI Acuerdo Laboral de ámbito Estatal para el sector de '
       'Hostelería no nombra la palabra «taquería», pero incluye los restaurantes y el reparto de comidas preparadas; '
       'todos por encima del SMI de 2026 (1.221 € al mes en 14 pagas, Real Decreto 126/2026) en proporción a la '
       'jornada; contratos por escrito; registro de jornada obligatorio (art. 34.9 del Estatuto de los Trabajadores; '
       'NO digas que la ley lo exige «digital»); nunca autónomos que te facturan con tu horario (falso autónomo, art. '
       '1.1). Repartidor propio, si algún día lo pones: contrato laboral del convenio de hostelería; en el reparto que '
       'organiza una plataforma por algoritmo, la ley presume la relación laboral (disposición adicional 23.ª del '
       'Estatuto). Formación de manipuladores acreditada por la empresa (el antiguo carné de manipulador ya no existe) '
       'con las temperaturas del trompo y de las salsas, los alérgenos y el contacto cruzado; formación del trompo '
       '(marinado, montaje del cono, corte y gramaje); prevención de riesgos (cortes en el trompo, quemaduras de la '
       'plancha y la freidora, gas y calor).',
    8: 'Plan financiero, TODO por token: inversión {INVERSION_TOTAL} = compras {CAPEX} (obra, conducto, cocina, equipo y '
       'puesta en marcha {INVERSION_PARTIDAS}, más la fianza {FIANZA} y {RENTA_PREVIA} de renta antes de abrir) + fondo '
       'de maniobra {FONDO_MANIOBRA}; IVA de la inversión {IVA_INVERSION}; necesidad de caja {NECESIDAD_CAJA}; '
       'financiación {RECURSOS_PROPIOS} propios + préstamo {PRESTAMO} al {TIPO_PRESTAMO}, {PLAZO_PRESTAMO} años con '
       '{CARENCIA} de carencia, cuota {CUOTA_ANUAL}. Cuenta de resultados de 3 años: ventas {VENTAS_A1}/{VENTAS_A2}/'
       '{VENTAS_A3}; margen bruto {MARGEN_BRUTO_PCT_A1} (después de TODOS los costes variables: mercancía '
       '{MERCANCIA_PCT_A1}, envases, plataforma, medios de pago y varios); personal {PERSONAL_A1}; alquiler '
       '{ALQUILER_ANO} ({ALQUILER_PCT_A1}); tasa de terraza y residuos {TASAS_TERRAZA_RESIDUOS} («pon la de tu '
       'ayuntamiento»); resultado de explotación antes de amortizaciones e intereses {EBITDA_A1} ({EBITDA_PCT_A1}); '
       'neto {NETO_A1}/{NETO_A2}/{NETO_A3} ({NETO_PCT_A1}/{NETO_PCT_A2}/{NETO_PCT_A3}; el año 3 tributa ya al tipo '
       'general del Impuesto de Sociedades). EL FOOD COST CON HONESTIDAD: la comida va al {FOOD_COST} (la media de '
       'TODA la carta más la merma, no el taco al pastor), por debajo del 28-33 % que publica nuestra Guía Restaurante '
       'Mexicano para un restaurante de mesa: el plan estima la carne del pastor a 5,50 € el kilo (en Makro, la paleta '
       'de cerdo sin hueso de gama selecta estaba a 6,99 € con IVA en octubre de 2026: en mayorista va de unos 5,50-7 € '
       'según corte y calidad) y la tortilla de maíz a 0,14 € (en Makro, unos 0,11-0,12 €: el caso va del lado '
       'prudente); cada punto de food cost de la comida mueve unos 2.900 € al año, y con la comida al 30 % el neto '
       'del año 2 baja a un 8 % (cálculo del kit con este mismo Excel): pon los precios de tu proveedor. CRECIMIENTO tal '
       'cual lo hace el Excel: suben los comensales un {CREC_A2} y un {CREC_A3} (de {COMENSALES_DIA} a '
       '{COMENSALES_DIA_A2} y {COMENSALES_DIA_A3} al día) con el mismo ticket, y la plantilla crece con personas '
       '({INCORPORACIONES_A2} al año), no con un porcentaje. IVA: la comida al 10 % (en sala, para llevar y a '
       'domicilio); de la bebida, la parte que sale del local con alcohol o con azúcares o edulcorantes añadidos (las '
       'aguas frescas azucaradas incluidas: {BEBIDA_21_PCT} de la bebida, la columna H de su línea, un {VENTAS_21_PCT} '
       'de las ventas) va al 21 % y el resto al 10 %: el IVA medio de la bebida es {IVA_BEBIDA_LINEA}. En las compras, '
       'el IVA soportado de la comida es {IVA_COMPRA_COMIDA} y el de la bebida {IVA_COMPRA_BEBIDA}. Equilibrio contable '
       '{BE_COMENSALES_DIA} comensales al día (ingresos {BE_INGRESOS}; holgura {HOLGURA_CONTABLE}); equilibrio de caja '
       '{BE_COMENSALES_DIA_CAJA} comensales al día y holgura {HOLGURA_CAJA}, que es la del PRIMER año (sólo intereses '
       'por la carencia); desde el segundo, con la devolución del principal, la holgura baja a {HOLGURA_CAJA_A2} '
       '({BE_COMENSALES_DIA_CAJA_A2} comensales al día de equilibrio) y en el tercero queda en {HOLGURA_CAJA_A3} '
       '({BE_COMENSALES_DIA_CAJA_A3}): esos años son los que hay que vigilar. Rotación: los {COMENSALES_DIA} comensales '
       'equivalentes sobre {AFORO} plazas dan {ROTACION_IMPLICITA} al día, pero incluyen a quien se lleva los tacos o '
       'los recibe en casa, que no ocupa mesa (la de la sala ronda 1,8). DSCR mínimo {DSCR_MIN}. TESORERÍA: el Mes 1 es '
       'ENERO, en el orden del calendario; la rampa arranca al {RAMPA_MES1} y llega al ritmo de crucero en '
       '{MESES_RAMPA} meses (abril), así que cae sobre enero y febrero, los meses más flojos, y por eso el fondo de '
       'maniobra cuenta; el saldo mínimo es {SALDO_MINIMO} en el mes {MES_SALDO_MINIMO} ({MES_SALDO_MINIMO_NOMBRE}) y '
       'el año acaba (diciembre) con {SALDO_MES12}; las pagas extra salen en julio (Mes 7) y diciembre (Mes 12); el IVA '
       'se liquida por trimestres naturales (abril, julio, octubre y, el del cuarto trimestre, en enero del año '
       'siguiente). PAYBACK antes de la deuda: {PAYBACK} con el fondo de maniobra dentro y {PAYBACK_CAPEX} sin él; el '
       'token puede ser una cifra sin unidad o el texto «Más de 3 años»: escribe una frase que lea bien con los dos '
       '(«El payback antes de la deuda, en años, …: «{PAYBACK}» con el fondo de maniobra dentro y «{PAYBACK_CAPEX}» sin '
       'él»), nunca «no se recupera en tres años» ni «años» detrás del token. Escenarios: pesimista '
       '({ESC_PES_COMENSALES} comensales a {ESC_PES_TICKET} y {ESC_PES_DIAS} días: ventas {ESC_PES_VENTAS}, neto '
       '{ESC_PES_NETO}) y optimista ({ESC_OPT_COMENSALES} comensales a {ESC_OPT_TICKET} y {ESC_OPT_DIAS} días: ventas '
       '{ESC_OPT_VENTAS}, neto {ESC_OPT_NETO}). El Excel manda: si cambias una celda verde, el documento se queda atrás.',
    9: 'Marco legal con su cita (sólo esto, dicho así; lo marcado «compruébalo», dilo así y sin cifra): SL unipersonal '
       '(capital desde 1 €, Ley 18/2022) o autónomo. IAE (RDLeg 1175/1990): con comedor y servicio de mesa, grupo 671 '
       '«servicios en restaurantes», por categoría; de barra y mostrador sin comedor separado, grupo 673 (cafés y bares '
       'con comida); y el epígrafe 677.9 para la venta para llevar y a domicilio: confírmalo con tu gestoría; alta '
       'censal con el modelo 036; exento de cuota con menos de 1 millón de cifra de negocio (art. 82.1.c de la Ley de '
       'Haciendas Locales). Apertura: los restaurantes no están en el anexo de la Ley 12/2012: licencia o declaración '
       'responsable según la ordenanza de tu ayuntamiento, con una consulta urbanística previa (uso, salida de humos a '
       'cubierta, potencia, aforo); la terraza es ocupación de la vía pública y va siempre aparte (art. 2.2). Humos: la '
       'cocina de un restaurante NO es actividad potencialmente contaminadora de la atmósfera (catálogo del RD '
       '100/2011, actualizado por el RD 1042/2017): lo decide la ordenanza de cada ayuntamiento; ejemplo leído, Madrid '
       '(Ordenanza 4/2021 de Calidad del Aire, BOCM de 16-04-2021): conducto exclusivo a cubierta que supere en 1 m la '
       'altura del edificio propio y la de cualquier otro en 15 m de radio (art. 12 y anexo I), limpieza al menos una '
       'vez al año y, con carbón u otro combustible sólido, sistemas específicos de filtrado de partículas (art. 23); '
       'en tu ciudad, pide la ordenanza (sin cifras de otras). Gas del trompo, la plancha y el comal: empresa '
       'instaladora habilitada, puesta en marcha certificada de cada aparato e inspección o revisión cada 5 años (RD '
       '919/2006, ITC-ICG 07 e ITC-ICG 08). Sanidad: declaración responsable al registro sanitario de tu comunidad '
       'autónoma (RD 1021/2022); el RGSEAA sólo aplica si suministras a otros negocios por encima de lo que permite su '
       'art. 3 (por ejemplo, si vendes tortilla o masa a otras taquerías); APPCC con la flexibilidad del art. 20 del RD '
       '1021/2022. TEMPERATURAS, leídas en el BOE: el art. 4.1 del RD 1021/2022 fija los preparados de carne (el pastor '
       'marinado lo es) a 4 °C o menos, la carne picada a 2 °C o menos, la carne de ungulados a 7 °C o menos y las '
       '«frutas y vegetales cortados o pelados… listos para consumo» (cebolla, cilantro y piña picados, aguacate '
       'cortado) a 4 °C o menos; lo que no está en esa tabla (quesos, tortilla envasada), a la temperatura de su '
       'etiqueta (art. 4.2); el transporte de lo que sale, en medios que mantengan la temperatura (art. 4.3). Las '
       'comidas preparadas (carnitas, guisados, salsas) siguen el art. 30 del RD 1086/2020, en la redacción que le dio '
       'el RD 1021/2022 (nunca lo atribuyas al RD 1021/2022 a secas): en caliente, «a una temperatura superior o igual a 63 °C» '
       '(30.2); refrigeradas, a 4 °C o menos si su vida útil pasa de 24 horas y a 8 °C o menos si es menor (30.3); el '
       'enfriamiento, «de 60 °C a 10 °C en menos de dos horas» (30.6); y el recalentado, «por lo menos 74 °C durante al '
       'menos quince segundos en el centro del alimento… en el término de una hora» desde que sale del frigorífico '
       '(30.7). El trompo no tiene norma española propia: las guías de buenas prácticas del asador vertical piden sonda '
       'al inicio y a mitad del servicio, y la hora límite del cono montado la fija tu APPCC. Pescado crudo (aguachile, '
       'ceviche): «–20 °C durante un mínimo de veinticuatro horas o –35 °C durante un mínimo de quince horas» (art. 8.1 '
       'del RD 1021/2022), o pescado ya tratado por el proveedor. Alérgenos: lo que se sirve sin envasar informa de los '
       '14 alérgenos (RD 126/2015, art. 4.1.b), por escrito o de palabra si la información «se registre de forma '
       'escrita o electrónica en el establecimiento» y es accesible (art. 6.5.a), y en la venta a distancia, disponible '
       'antes de comprar (Reglamento (UE) 1169/2011, art. 14); en la taquería, la salsa macha (cacahuete o sésamo), la '
       'tortilla de harina de la gringa y la cerveza (gluten) y los quesos y la crema (leche). «Sin gluten» sólo con 20 '
       'mg/kg o menos tal como se vende (Reglamento de Ejecución (UE) 828/2014): con comal, freidora o pinzas '
       'compartidos con la tortilla de harina, no se promete. IVA (Ley 37/1992, art. 91): en sala, todo al 10 % («el '
       'suministro de comidas y bebidas para consumir en el acto», 91.Uno.2.2.º); para llevar y a domicilio, la comida '
       'al 10 % pero se excluyen del reducido «a) Las bebidas alcohólicas» y «b) Las bebidas refrescantes, zumos y '
       'gaseosas con azúcares o edulcorantes añadidos» (91.Uno.1.1.º): las aguas frescas azucaradas, la cerveza y el '
       'mezcal que salen del local van al 21 %. En las compras, los quesos y las frutas, verduras y hortalizas '
       'naturales (aguacate, tomate, cebolla, cilantro, lima, piña) van al 4 % (91.Dos.1.1.º). Alcohol para llevar o a '
       'domicilio: horarios y limitaciones de cada comunidad autónoma y nunca a menores: consulta la normativa de la '
       'tuya (sin cifras). Ley 1/2025 de desperdicio alimentario, art. 8: el cliente puede llevarse lo que no consuma '
       'sin coste (salvo el del envase de plástico de un solo uso) y la taquería lo avisa de forma visible, mejor en la '
       'carta. Ley 7/2022, art. 55: el envase de plástico de un solo uso para llevar se cobra aparte en el tique; las '
       'bandejas de cartón no son plástico y las de aluminio, consúltalo con tu proveedor. Personal: convenio '
       'provincial de hostelería (ALEH VI, art. 4, que no nombra la taquería), SMI de 2026 (RD 126/2026), Estatuto de '
       'los Trabajadores (arts. 1.1 y 34.9 y disposición adicional 23.ª), Ley 31/1995 de prevención. Facturación con '
       'software Veri*factu (consulta con tu gestoría la fecha que te aplica). El marco legal del plan es el ESPAÑOL: en '
       'México y el resto de Latinoamérica los trámites (fiscales, municipales y sanitarios) son otros y este plan no '
       'los cubre; la guía de equivalencias del pack adapta los términos. Lo que no esté aquí no se afirma: '
       '«compruébalo con tu gestoría, tu ayuntamiento o el inspector».',
    10: 'Conclusiones con tokens (viabilidad, holgura de caja del año 1 y de los años 2 y 3, DSCR mínimo, saldo mínimo, '
        'payback leído como en el §8) y los riesgos de una taquería y cómo se mitigan (R §6, uno por uno): firmar un '
        'local sin salida de humos a cubierta (el error número uno: sin ella no hay trompo, plancha ni comal); montar el '
        'trompo sin protocolo (cono sin hora de montaje ni hora límite, carne marinada por encima de 4 °C, capas '
        'cortadas antes de estar hechas); no medir el rendimiento del trompo (la merma y el sobrante se comen 3-5 '
        'puntos de margen: mide en el kit y recalcula en el plan); la barra de salsas sin reglas; prometer «sin gluten» '
        'con comal y freidora compartidos; cobrar al 10 % las aguas frescas azucaradas y la cerveza para llevar (van al '
        '21 %); depender de un solo importador de chiles; hacer nixtamal por ahorrar por debajo de unas '
        '{EQUILIBRIO_TORTILLAS_DIA} tortillas al día; abrirse a la plataforma sin cuentas (techo del {DELIVERY_PCT}); el '
        'taquero único; vender la taquería como tex-mex. El plan de acción en 6 fases del checklist (80 tareas: '
        '12/15/14/13/13/13). Cierra con el siguiente paso: completar el Excel con tus cifras, medir el trompo con el Kit '
        'de Tareas y escandallar tu carta con la calculadora.',
}

#: Prohibidos en el texto (F1-camino §2): sellos y palabras vetadas, normas derogadas, la rentabilidad que contradice el
#: caso, restos de los moldes (Food Truck, Tapas Bar, Heladería, Pizzería —la semilla—) y las frases del motor sin
#: traducir. SALEN de la lista de la Pizzería por ser oficio de la taquería: horchata, tarrina, mantec (carnitas), cubeta
#: (de cervezas) y raciones (orden = ración). Harina (gringa), masa (de maíz) y horno (cochinita) son oficio. Los usa
#: también `barrido_es.py` sobre los xlsx y el docx.
PROHIBIDOS = [
    r'\bfreelance', r'validad[oa]s?', r'Espa[ñn]a,? 2026', r'carn[eé]t? de manipulador(?! ya no existe)',
    r'tarifa plana', r'\bCNAE\b', r'(?<!inscrito en el )\bRGSEAA\b(?!.{0,80}(s[oó]lo|otros (establecimientos|negocios)))',
    r'licencia de apertura', r'895/2013', r'393/2007', r'15 ?(-|–|a|y el) ?25 ?%',
    r'versi[oó]n (1\.1|2\.2|anterior)', r'\bv1\.1\b', r'solopreneur',
    # restos del Food Truck
    r'food ?truck', r'\bcami[oó]n\b', r'ventanilla', r'generador', r'aparcamiento',
    # restos del Tapas Bar
    r'\btapas?\b', r'gastrobar', r'vermut', r'\bpinchos?\b', r'tapeo', r'afterwork', r'salamandra', r'rational',
    r'[Ff]ichero v1\.1',
    # restos de la Heladería (sin horchata, tarrina, mantec ni cubeta: son oficio)
    r'helad', r'sorbete', r'pasteuriz', r'granizad',
    # restos de la Pizzería (la semilla)
    r'pizz', r'napol[ei]t', r'margherita', r'\ble[ñn]a\b', r'levadura', r'amasad', r'bolas? de masa', r'fior di latte',
    r'mozzarella', r'chimenea', r'c[uú]pula', r'\bETG\b', r'pliego', r'97/2010', r'AVPN',
    # frases del motor sin traducir y pids de los moldes
    r'alcohol (que sale por|del canal de) delivery', r'pan com[uú]n', r'plan-negocio-(tapas-bar|heladeria|pizzeria)',
]
#: «art. 30» siempre con «RD 1086/2020» (F1-camino §7 F2 (3)): ERROR si un «art. 30» / «artículo 30» no tiene
#: «1086/2020» a menos de 160 caracteres, o si se atribuye al RD 1021/2022.
RX_ART30 = re.compile(r'\bart(?:[ií]culo|\.)\s*30\b', re.I)
RX_ART30_MAL = re.compile(r'\bart(?:[ií]culo|\.)\s*30\.?\d*\s*(?:,\s*)?del (?:RD|Real Decreto) 1021/2022', re.I)


def art30_mal(texto):
    """Lista de fragmentos con un «art. 30» mal citado (sin «1086/2020» cerca o atribuido al RD 1021/2022)."""
    malos = []
    for m in RX_ART30.finditer(texto):
        ventana = texto[max(0, m.start() - 160):m.end() + 160]
        if '1086/2020' not in ventana:
            malos.append(texto[max(0, m.start() - 50):m.end() + 60])
    for m in RX_ART30_MAL.finditer(texto):
        malos.append(texto[max(0, m.start() - 30):m.end() + 30])
    return malos


#: Avisos (F1-camino §2, en lugar del RX_D11 de la Pizzería): no son error, pero cada uno se revisa a mano.
AVISOS = [
    ('«art. 30 del RD 1021/2022» (es del RD 1086/2020)', re.compile(r'art(?:[ií]culo|\.)\s*30[^.;]{0,20}1021/2022',
                                                                    re.I)),
    ('«sin gluten» prometido', re.compile(r'(?<!no prometer )(?<!nada de )(?<!ni )«?sin gluten»?', re.I)),
    ('«tex-mex» o «auténtic» como promesa', re.compile(r'tex-?mex|aut[eé]ntic', re.I)),
    ('Cinco de Mayo como fiesta nacional', re.compile(r'cinco de mayo|5 de mayo', re.I)),
    ('registro horario «digital obligatorio»', re.compile(r'digital(es)? obligatori|obligatori\w* (en formato )?digital',
                                                          re.I)),
]
#: Cifras que el texto puede llevar escritas (normas, research con fuente, carta y estructura del caso, producción,
#: variantes sin Excel y la cuenta del reparto propio de las pistas). El resto, token o nada.
PERMITIDAS = set('''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 35 36 37
38 40 41 44 45 46 50 54 55 57 60 62 63 64 65 66 70 72 74 75 77 80 82 85 90 91 100 110 115 120 125 126 135 140 150 160 180
200 210 250 255 278 280 300 400 671 673 677.9 700 760 828 852 1.000 1.021 1.042 1.086 1.100 1.169 1.175 1.221 1.250 1.279
1.300 1.350 1.450 1.500 1.600 1.784 1.800 1.900 2.400 2.500 2.900 3.000 3.500 4.400 8.100 8.800 11.300 12.000 18.100
18.900 84.000 135.000 150.000 300.000 7.808 1/2025 7/2022 37/1992 12/2012 18/2022 31/1995 100/2011 1042/2017 919/2006
4/2021 126/2026 1175/1990 1021/2022 1086/2020 126/2015 1169/2011 828/2014 852/2004 2027 2026 2025 2024 2023 2022 2021 2020
2017 2015 2014 2012 2011 2006 2004 1995 1992 1990 16-04-2021 1-1,50 2,50-3,50 7-8 2,50 1,50 3,00 3,50 3,80 3,90 4,50 5,50
6,00 6,50 7,50 8,50 9,90 10,90 12,50 15,50 17,43 19,50 2,10 1,30 3,63 0,40 0,10 0,14 0,32 0,35 0,61 0,75 1,1 1,5 1,8 6,2
18,5 18-19 10-11 15-20 30-35 50-100 1.250-2.500 1.279-1.784 15.000-25.000 150.000-300.000 22-28 26-30 28-33 3-5 8-10 12-15
15-35 25-35 7-15 13:30 16:30 20:00 23:30 12/15/14/13/13/13 82.1 91.Uno.1.1 91.Uno.2.2 91.Dos.1.1 1.1 4.1 4.2 4.3 8.1 30.2
30.3 30.6 30.7 34.9 23.ª 9,6 −18 −20 −35 –20 –35 1,25 2,2 1,37 5,50-7 6,99 0,11-0,12'''.split())
RX_NUM = re.compile(r'(?<![\w{])[−+]?\d[\d.,/:−-]*\d|(?<![\w{])\d')
#: Caracteres admitidos además del latín básico/extendido: tipografía española y los signos de temperatura (−, ≤, ≥, ≈).
RX_RARO = re.compile(r'[^\x00-ɏ‐-‧€°→ ‑«»¿¡ºª·…–—“”‘’−≤≥≈²$]')


def ranuras():
    d = json.load(open(os.path.join(BP4, 'docx_es_cat.json'), encoding='utf-8'))['parrafos']
    gem = {}
    for t in ('piz_es_a', 'piz_es_b'):
        gem.update(json.load(open(os.path.join(GEMELA, t + '.json'), encoding='utf-8')))
    fuera = []
    for k in sorted(d, key=int):
        v = d[k]
        if v['rol'] != 'cuerpo':
            continue
        sec = int(v['seccion'])
        fuera.append({'i': int(k), 'seccion': sec, 'palabras_objetivo': int(v['palabras']),
                      'molde_ft_es': v['texto'], 'gemela_formato_pizzeria_es': gem.get(k, '')})
    return fuera


def preparar():
    if not os.path.exists(CIFRAS):
        raise SystemExit('falta %s: corre antes cifras_taq_es.py --calc en el VPS y cópialo aquí' % CIFRAS)
    cif = json.load(open(CIFRAS, encoding='utf-8'))['tokens']
    usados = set(re.findall(r'\{([A-Z0-9_]+)\}', ' '.join(PISTAS.values())))
    sin = sorted(usados - set(cif))
    if sin:
        raise SystemExit('las PISTAS citan tokens que no están en cifras_caso_es.json: %s (¿falta --calc?)' % sin)
    for s, p in PISTAS.items():                                   # las pistas también cumplen la regla del art. 30
        assert not art30_mal(p), (s, art30_mal(p))
    os.makedirs(TANDAS, exist_ok=True)
    rs = ranuras()
    for tanda, secs in (('taq_es_a', range(1, 6)), ('taq_es_b', range(6, 11))):
        sel = [r for r in rs if r['seccion'] in secs]
        ent = {
            'tanda': tanda, 'producto': 'Plan de Negocio: Taquería ES 1.0 (aichef.pro, 35 €)',
            'salida': 'scripts/productos-digitales/plan-taqueria/textos/%s.json' % tanda,
            'formato_salida': '{"<i>": "<párrafo en español>", …} con TODOS los "i" de "parrafos" y nada más',
            'brief': 'scripts/productos-digitales/plan-taqueria/BRIEF-REDACTORES.md (léelo entero antes)',
            'research': RESEARCH + ' (§0 hallazgos, §1 normativa con citas literales, §2 precios, §3 caso, §4 SERP y '
                                   'hueco, §5 jerga, §6 errores y riesgos: material de apoyo; la pista de la sección '
                                   'manda)',
            'jerga (glosar la primera vez; y qué no decir)': JERGA,
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
        print('ERROR falta --tanda (taq_es_a o taq_es_b)')
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
            if re.search(rx, t, re.I):
                err.append('%d: prohibido /%s/' % (r['i'], rx))
        for frag in art30_mal(t):
            err.append('%d: «art. 30» sin el RD 1086/2020 o atribuido al RD 1021/2022: …%s…' % (r['i'], frag))
        for nombre, rx in AVISOS:
            m = rx.search(t)
            if m:
                avi.append('%d: %s — revisa: …%s…' % (r['i'], nombre, t[max(0, m.start() - 50):m.end() + 50]))
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
