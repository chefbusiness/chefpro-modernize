#!/usr/bin/env python3
"""
tandas_docx.py — Pollería y Asador de Pollos ES 1.0 (F1-camino §4): prepara y valida las dos tandas de redacción del
plan de negocio (docx). Copia adaptada de `plan-taqueria/tandas_docx.py`.

Las 61 ranuras de texto del docx del Food Truck ES (131 párrafos, 10 Heading 1; mapa en
`business-plans-en-4/docx_es_cat.json`) se escriben NUEVAS, en español, para la pollería:
  pol_es_a = §1-5 (29 ranuras) · pol_es_b = §6-10 (32 ranuras).
Gemela de FORMATO: el texto de la Taquería ES 1.0 en la misma ranura (`plan-taqueria/textos/taq_es_{a,b}.json`, la ES
1.0 de local fijo con tokens, ya revisada): sirve para ver cómo se escribe una ranura con tokens, nunca su contenido.
No hay versión anterior: el material es el research (`F1-research-polleria.md`) y las pistas de abajo (las cinco
corrientes —española con el pollo al ast, peruana, venezolana, rôtisserie francesa y churrasqueira portuguesa— van
como contenido de guía en §2-§4, §6 y §9). Las cifras del Excel (y de la calculadora del pollo, el asador y el
escandallo) van SIEMPRE como token {ASI} (`cifras_caso_es.json`, con `--calc`); `docx_pol_es.py` las resuelve al
ensamblar. Sólo lee JSON: corre en el Mac.

    python3 tandas_docx.py preparar                       # tandas/pol_es_{a,b}.entrada.json
    python3 tandas_docx.py check --tanda pol_es_a         # valida textos/pol_es_a.json (salida del redactor)

Sesión Claude Code, 29-oct-2026.
"""
import argparse
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BP4 = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
GEMELA = os.path.join(os.path.dirname(AQUI), 'plan-taqueria', 'textos')
TANDAS, TEXTOS = os.path.join(AQUI, 'tandas'), os.path.join(AQUI, 'textos')
CIFRAS = os.path.join(AQUI, 'cifras_caso_es.json')
RESEARCH = 'scripts/productos-digitales/plan-polleria/F1-research-polleria.md'

SECCIONES = {
    1: '1. Resumen Ejecutivo', 2: '2. Concepto y Propuesta de Valor', 3: '3. Análisis de Mercado',
    4: '4. Análisis Competitivo', 5: '5. Plan de Marketing y Captación', 6: '6. Plan de Operaciones',
    7: '7. Estructura Organizativa y RRHH', 8: '8. Plan Financiero', 9: '9. Aspectos Legales y Licencias',
    10: '10. Conclusiones y Plan de Acción',
}

#: La jerga del oficio (R §5): se glosa la PRIMERA vez que sale en el Word; y lo que no se dice.
JERGA = ('asador de pollos (la máquina de espadas y también el local; «asador» a secas en España es también el de cordero '
         'o el de carne a la brasa: di siempre «asador de pollos») · espada o espetón (la barra donde se ensartan los '
         'pollos; «espetar») · carga o tanda (los pollos que entran a la vez en el asador; la calculadora dice «tanda») · '
         'bandeja de goteo · vitrina caliente · encargo (el pedido con hora de recogida, sobre todo el del domingo) · '
         'pollo bridado (atado) · pollo de asar (calibre de 1,3-1,6 kg) · cuarto (muslo o pechuga) · pollo al ast o '
         'pollastre a l\'ast (Cataluña: pollo de asador con allioli y patates rostides) · pollo a la brasa (Perú: adobo '
         'con sillao —salsa de soja—, ají panca, comino y cerveza negra, en horno rotativo de leña o carbón, el rotombo) · '
         'cremas (Perú: ají, huacatay, ocopa y mayonesa) · mostrito (Perú: cuarto de pollo con arroz chaufa y papas) · '
         'pollo en brasa venezolano (adobo de ajo, comino y onoto; guasacaca, salsa de aguacate) · rôtisserie (Francia: '
         'patatas que se doran bajo las espadas con el jugo) · churrasqueira y piri-piri (Portugal: pollo abierto a la '
         'parrilla de carbón con guindilla piri-piri). QUÉ NO DECIR: «asador» suelto por el negocio; «broaster» como '
         'asado (es pollo FRITO a presión); «pollería» sin aclarar que en España también es la tienda de pollo crudo; '
         'marcas de cadenas o salsas; «auténtico» como promesa o sello; «tortilla» sólo si es la de patatas del asador')

#: Lo que tiene que contar cada sección (español de España, para el mercado español; R §0-§7). Cifras del Excel y de
#: la calculadora = tokens. Las cinco corrientes (R §5) son contenido de guía repartido en §2, §3, §4, §6 y §9.
PISTAS = {
    1: 'Qué es el negocio: una pollería-asador de barrio con un asador de pollos de gas de doce espadas a la vista, '
       'mostrador con vitrina caliente y encargos, y una sala de 20 plazas (16 en mesa y 4 en barra), en un barrio '
       'residencial de una ciudad media (100.000-300.000 habitantes), cómodo para parar el coche y recoger el encargo; '
       'local de 80 m² con salida de humos a cubierta posible (el filtro del local), sin traspaso. Una SL unipersonal con '
       'el titular de maestro asador, un segundo asador-cocinero, un dependiente de mostrador y caja, un camarero de '
       'sala, un ayudante de fin de semana y un refuerzo de sábado, domingo y festivos. Carta corta con combos: pollo '
       'entero a 12,90 € con IVA, medio a 7,00 €, patatas a 3,50 €, croquetas caseras (las 8) a 8,50 €, ensaladilla a '
       '5,50 €, ensalada a 4,50 €, alioli y salsas, pan, refrescos, agua, cerveza y vino; en sala, el menú de cuarto de '
       'pollo con patatas y ensalada a 9,50 € y el medio pollo a la brasa al estilo peruano con papas, ensalada y cremas '
       'a 14,50 € (adobo peruano en el mismo asador de gas). Canales: para llevar en el mostrador y por encargo (unos '
       '61 % de las ventas, sin comisión), plataforma con su reparto ({DELIVERY_PCT}, con techo y sin reparto propio) y '
       'sala (unos 28 %). Abre en ENERO (el Mes 1 del Excel es enero, en el orden del calendario), de martes a domingo '
       'de 12:00 a 16:30 y de jueves a sábado también de 20:00 a 23:00; cierra los lunes y 10 días en enero, y los '
       'festivos abren como un domingo. Cifras clave por token: {PEDIDOS_DIA} pedidos al día (mostrador, encargos, '
       'plataforma y clientes de sala) a {TICKET} por pedido sin IVA y {DIAS_APERTURA} días, unos {POLLOS_SEMANA} pollos '
       'a la semana, ventas {VENTAS_A1}, resultado neto {NETO_A1} ({NETO_PCT_A1}), inversión {INVERSION_TOTAL} (de la '
       'que {INVERSION_PARTIDAS} son obra, asador, equipo y puesta en marcha), préstamo {PRESTAMO} y equilibrio en '
       '{BE_PEDIDOS_DIA} pedidos al día. Qué contiene el kit: este plan de negocio de 10 secciones, el Excel del plan '
       'financiero de 9 hojas, el checklist de apertura de 80 tareas en 6 fases, la calculadora del pollo, el asador y '
       'el escandallo (cuánto rinde un pollo, cuántos salen del asador antes de las tres del domingo y el escandallo de '
       '12 productos y 6 combos con su margen en el mostrador, por encargo, en sala y en plataforma) y la guía de '
       'equivalencias para Latinoamérica (el marco legal del plan es el español). Lo que lo distingue, en una frase: el '
       'pollo y el asador con números ({POLLOS_POR_TANDA} pollos por tanda y {CAPACIDAD_DOMINGO} asados antes de las tres '
       'del domingo en el ejemplo, estimaciones editables que mides tú) y todo en euros y con la norma española.',
    2: 'Tipos de pollería y por qué esta (R §3, sin cifras de Excel para las otras): el asador SOLO para llevar de '
       'viernes a domingo y festivos (50-60 m², sin sala, plantilla de temporada: el clásico de fin de semana); la '
       'pollería-asador de barrio con mostrador, encargos y sala (la de este plan, que sirve al cliente del asador '
       'español y al de la pollería latina); la pollería peruana con sala y horno de brasa de leña o carbón (120-150 m², '
       '50-60 plazas: otro local, otro conducto y otra inversión; un restaurante peruano de mesa lo cubre la Guía '
       'Restaurante Peruano de AI Chef Pro); y la churrasqueira de carbón. Aclara en una frase que en España «pollería» '
       'es también la tienda de pollo crudo y huevos: este plan es el ASADOR DE POLLOS. LAS CINCO CORRIENTES que caben en '
       'el mostrador (contenido de guía, sin Excel propio): el asador español (sal, ajo, pimentón, hierbas y limón según '
       'la casa; patatas, croquetas, ensaladilla y pimientos; el encargo del domingo); el pollo al ast catalán (allioli y '
       'patates rostides); el pollo a la brasa peruano (adobo con sillao, ají panca, comino y cerveza negra; papas, '
       'ensalada y cremas; nació hacia 1950 en La Granja Azul, en Perú); el pollo en brasa venezolano (ajo, comino y '
       'onoto; yuca y guasacaca); la rôtisserie francesa (pollo de granja con las patatas dorándose debajo, con el jugo) '
       'y la churrasqueira portuguesa con piri-piri (pollo abierto a la parrilla de carbón). El caso hace el asador '
       'español y el medio pollo a la brasa al estilo peruano en el mismo asador de gas. GLOSA LA JERGA la primera vez '
       '(ver `jerga` de la entrada): espada, carga o tanda, encargo, cuarto, cremas, sillao, mostrito, churrasqueira, '
       'piri-piri; y «broaster» es pollo FRITO a presión, una línea complementaria de la pollería andina, no un asado. '
       'El ticket de {TICKET} es por pedido y sin IVA ({TICKET_IVA} con IVA): el pedido de mostrador (0,8 pollos, 0,85 '
       'raciones de patatas, algún extra, pan, salsas y bebida) suma unos 17,70 € con IVA; el de plataforma, unos 20,50 € '
       'con su precio más alto; el cliente de sala (el menú de cuarto o el medio a la brasa, algo para compartir, 1,1 '
       'bebidas y postre), unos 16,08 €. Mezcla de ventas: comida {PCT_COMIDA} y bebida {PCT_BEBIDA}. La propuesta: '
       'pollo de calibre fijo bien hecho y sondeado, encargos del domingo con hora, combos que dan el margen y una sala '
       'pequeña con el medio pollo a la brasa.',
    3: 'Mercado en España con fuente. El sector vende unos 2,5 millones de pollos a la semana en unos 12.000 '
       'establecimientos, con el pollo entero a 10-14 € y el verano un 15 % más fuerte en el interior y hasta un 35 % en '
       'la costa (Interempresas y Efeagro, julio de 2026): unos 208 pollos por asador y semana de media; el caso vende '
       'unos {POLLOS_SEMANA}. La semana del 15 de agosto es la más fuerte del año (Diari de Tarragona, julio de 2025). '
       'Búsquedas mensuales en Google España (DataForSEO, 29 de octubre de 2026): «asador de pollos» 8.100, «pollo al '
       'ast» 6.600, «pollo piri piri» 2.900, «pollo a la brasa peruano» 2.400, «churrasqueira» 1.600, «pollos asados '
       'para llevar» 590 y «pollería peruana» 260; y apenas 10-30 «cómo montar una pollería», «plan de negocio pollería» '
       'o «franquicia pollos asados»: el oficio y el consumidor buscan mucho, el que va a abrir busca poco y decide con '
       'datos. En México, «pollo rostizado» tiene 60.500 búsquedas y «rosticería» 22.200; en Perú, «pollo a la brasa» '
       '60.500 y «pollería» 33.100. Precio en carta, con IVA (cartas y guías leídas en 2026, sin nombres): el asador '
       'español vende el pollo entero a 11-14 € (en Getxo, 11 €; en Sevilla, de 12 a 14 € con patatas); el pollo al ast '
       'de Barcelona, de 13,90 a 20,50 €; la pollería peruana de Madrid, el medio con papas a 14,50-16 € y el entero con '
       'todo a 25,50-27 €; en las plataformas, 1,50-2 € más por pieza. El caso, 12,90 € el entero. Estacionalidad del '
       'plan, con el Mes 1 en ENERO y en el orden del calendario: al revés que otros locales, el verano SUBE: enero y '
       'febrero son los meses más flojos (un 7 % del año), julio y agosto el pico (un 9,6 y un 9,8 %) y diciembre repunta '
       'con los encargos de Nochebuena y Nochevieja; entre el mejor mes y el peor hay un 40 %. En la costa el verano sube '
       'más (hasta un 35 %) y en el centro de una gran ciudad agosto baja: gira la fila de la Tesorería. El hueco: '
       'ningún resultado español da una cuenta de resultados en euros (planes en dólares o en soles, trabajos de clase, '
       'foros y vendedores de maquinaria); nadie cuenta cuántos pollos salen del asador antes de las tres del domingo, '
       'la etiqueta de lo envasado antes del pedido, el ovoproducto del alioli y las cremas, el IAE 677.9 frente al 642.5 '
       'ni el sobrante convertido en croqueta con su enfriado. NADA de tamaños de mercado sin fuente.',
    4: 'Competencia por categorías, sin nombres salvo la franquicia: los asadores de barrio para llevar de fin de semana '
       '(precio y costumbre del domingo); los asadores de franquicia (Asasur, que se presenta como la única franquicia '
       'en España de asadores de pollos y comida para llevar, pide desde 45.000 € de inversión y un canon de entrada de '
       '6.600 €; sus fichas no coinciden en el royalty: pregúntalo por escrito); las pollerías peruanas con sala (medio '
       'pollo a la brasa con papas a 14,50-16 €); las churrasqueiras y el pollo piri-piri; las rostisserias del pollo al '
       'ast en Cataluña; y la comida para llevar por plataforma. FRANQUICIA FRENTE A MARCA PROPIA, razonado: la '
       'franquicia trae marca, proveedor y formación a cambio del canon y de la cuota mensual; con marca propia, este '
       'plan pone la inversión en {INVERSION_TOTAL} y te quedas el margen, pero el oficio lo aprendes tú: compara las dos '
       'cuentas antes de firmar. Dónde gana este concepto: pollo de calibre fijo y sondeado, encargos del domingo con '
       'hora, combos (el margen no está en el pollo, está en lo que lo acompaña), una sala pequeña para el mediodía de '
       'diario y el medio pollo a la brasa al estilo peruano. Los riesgos: el precio del pollo (se movió un 10-12 % en '
       'un año), la guerra de precios del pollo entero, la plataforma y el asador pequeño para el domingo; cómo se '
       'defiende (dos proveedores, escandallo por combo, capacidad del asador medida, recogida en el mostrador, clientela '
       'de barrio que encarga cada semana).',
    5: 'Marketing y captación: apertura en enero (los curiosos llegan el primer mes; los encargos del domingo, en un '
       'trimestre); ficha de Google Business con el horario, fotos del asador y respuesta a cada reseña; tarjetas de '
       'encargo, buzoneo en el barrio con el teléfono y WhatsApp para encargar, y el teléfono en cada bolsa; redes con el '
       'asador cargado y el pollo saliendo; el calendario: el verano (la semana del 15 de agosto), los encargos de '
       'Nochebuena y Nochevieja y, si haces el medio pollo a la brasa, el Día del Pollo a la Brasa (tercer domingo de '
       'julio, fecha peruana); fidelización sencilla (tarjeta de sellos del encargo) sin cifras de conversión '
       'inventadas. PLATAFORMA FRENTE A REPARTO PROPIO (sin Excel, razonado): el plan vende por plataforma con su reparto '
       'un {DELIVERY_PCT} de las ventas ({VENTAS_PLATAFORMA_A1} al año) y paga una comisión del {COMISION_DELIVERY} '
       '({COMISIONES_DELIVERY_A1} al año); las guías del sector sitúan el plan básico de Uber Eats en torno al 30 % más '
       'IVA, Glovo entre el 15 y el 35 % según la zona y Just Eat entre el 13 y el 35 %, más las promociones y el envase. '
       'El pollo entero aguanta bien el viaje; las patatas fritas llegan blandas: en la plataforma, mejor patatas asadas '
       'o al horno, y por eso el techo del plan es ese {DELIVERY_PCT}. Un repartidor propio de viernes a domingo (0,35 '
       'jornada, unos 8.800 € al año con la Seguridad Social) más moto, seguro y gasolina (unos 2.500 €) cuesta unos '
       '11.300 € para repartir esa misma venta: un 28 %, poco menos que la comisión, pero sin el escaparate de la '
       'plataforma, que es la que trae el pedido, y con el riesgo laboral; sólo compensa con pedidos propios (teléfono, '
       'WhatsApp o web) y una zona corta y densa, y siempre con contrato laboral. La recogida en el mostrador no paga '
       'comisión: empújala con precio. Presupuesto de marketing {MARKETING_ANO} al año, más la marca, la web, las fotos y '
       'el lanzamiento, que van en la inversión ({MARCA_LANZAMIENTO}).',
    6: 'Operaciones del obrador, el asador y el mostrador. EL POLLO CON NÚMEROS (la calculadora del pack, valores por '
       'defecto que son estimación del kit y editables): un pollo de 1,45 kg en canal a 3,05 € el kilo sin IVA, más 0,13 € '
       'de sazón, aceite y sal, cuesta {COSTE_POLLO_ENTERO}; con un rendimiento del asado del {RENDIMIENTO_POLLO} (el '
       'USDA da un 78 % para el pollo entero asado con piel, de un 68 a un 84 %, pero es un dato de horno, no de asador '
       'de espadas) sale de unos 1,10 kg asado; vendido entero a 12,90 € con IVA, su food cost es un {FC_POLLO_ENTERO} '
       'sobre el precio SIN IVA (11,73 €). Pesa cinco pollos crudos y asados de la misma tanda y lleva tu rendimiento a la '
       'hoja «Pollo» de la calculadora. EL ASADOR Y EL DOMINGO: el domingo hace un tercio de los pollos de la semana (unos '
       '106 un domingo medio y unos 122 en agosto); con doce espadas y 5 pollos por espada (la ficha da de 4 a 6) salen '
       '{POLLOS_POR_TANDA} pollos por tanda y, con tandas de unos 90 minutos con la carga y la descarga (el tiempo de '
       'asado no lo publica ningún fabricante: MÍDELO), {CAPACIDAD_DOMINGO} asados antes de las tres; con ocho espadas, '
       'unos 120: justo en agosto y en los festivos. Por eso el caso lleva doce espadas: la hoja «Asador» de la '
       'calculadora hace esta cuenta con tus datos. Producción del caso: unos {POLLOS_SEMANA} pollos a la semana y unos '
       '{POLLOS_ANO} al año. EQUIPO con precio y fuente: asador {ASADOR} (en catálogo, de 4.373 a 5.967 € sin IVA el de '
       'doce espadas y de 2.493 a 4.126 € el de ocho, con las espadas aparte; el de ocho declara 56 kW), vitrina caliente '
       'y mantenedor de patatas {VITRINA}, freidora doble y fogón {FREIDORA}, campana extractora {CAMPANA} (de 1.800 a '
       '2.200 m³/h para doce espadas), frío {FRIO} y el conducto exclusivo a cubierta {CONDUCTO}. GAS, ELÉCTRICO O BRASA: '
       'el asador de gas (el del plan) cabe en una salida de humos normal, con instalación por empresa habilitada y '
       'revisión cada 5 años; el eléctrico de ocho espadas pide 8-10 kW trifásicos; el horno de brasa de leña o carbón '
       'de la pollería peruana (el rotombo) y la parrilla de la churrasqueira piden además filtro de partículas en el '
       'conducto y no tienen precio publicado en España: variantes SIN Excel, más inversión y una ordenanza que las '
       'admita. Horario: de martes a domingo de 12:00 a 16:30 y de jueves a sábado también de 20:00 a 23:00; el domingo '
       'se enciende a las 10:30. HIGIENE EN LA OPERACIÓN: pollo crudo a 4 °C o menos, mollejas a 3 °C o menos y el pollo '
       'adobado crudo, que es preparado de carne, a 4 °C o menos; mesa de espetar SEPARADA de la de servir y el pollo '
       'crudo sin lavar; sonda en el muslo en cada tanda (74 °C o más es el criterio del APPCC del caso: ninguna norma '
       'fija la temperatura de cocción); vitrina a 63 °C o más con una hora límite que fija tu APPCC; el SOBRANTE: o se '
       'mantiene a 63 °C, o se enfría de 60 a 10 °C en menos de 2 horas y al día siguiente se convierte en croquetas o '
       'ensalada de pollo, recalentando a 74 °C durante 15 segundos (art. 30 del RD 1086/2020, en la redacción del RD '
       '1021/2022); alioli, mayonesa, ensaladilla y cremas con ovoproducto, a 8 °C o menos y consumidos en 24 horas con '
       'la fecha y la hora anotadas. PROVEEDORES: dos proveedores de pollo con calibre fijo (1,4-1,5 kg) y la temperatura '
       'de recepción anotada: un calibre irregular descuadra las tandas y el escandallo. ENCARGOS: teléfono y WhatsApp '
       'con nombre y hora de recogida, cerrados el sábado: con ellos sabes cuántos pollos cargar. Suministros '
       '{SUMINISTROS_MES} al mes de media; mantenimiento {MANTENIMIENTO_CAMPANA} al año (dos limpiezas de la campana '
       'extractora y del conducto por la grasa del asador, el gas, el asador y el frío).',
    7: 'Equipo (7 filas en la hoja Personal): el titular, maestro asador (compra del pollo, adobos, asador, encargos y '
       'gestión; {SUELDO_TITULAR} brutos al mes en 14 pagas; como administrador de la SL cotiza en el régimen de '
       'autónomos: confírmalo con tu gestoría); un segundo asador-cocinero que espeta, lleva la freidora, las guarniciones '
       'y las croquetas y sabe sondear y trinchar (el asador único es un riesgo, no un ahorro: si falta, no abre el día '
       'que hace un tercio de la semana); un dependiente de mostrador y caja (encargos, teléfono, plataformas y la '
       'información de alérgenos); un camarero de sala de 30 horas (mediodías y cenas de jueves a sábado); un ayudante de '
       'cocina y friegue el sábado y el domingo por la mañana; un refuerzo de sábado, domingo y festivos para el '
       'mostrador y los encargos (sin reparto propio); y las suplencias de vacaciones y descansos: {PLANTILLA_PERSONAS} '
       'personas y {JORNADAS} jornadas completas equivalentes, coste {PERSONAL_A1} ({PERSONAL_PCT_A1} de las ventas), '
       'cobertura de horas {COBERTURA_HORAS} ({HORAS_CONTRATADAS} horas contratadas frente a {HORAS_NECESARIAS} '
       'necesarias); el domingo de 11:00 a 15:30 hacen falta seis personas y el cuadrante anual no lo ve: ponlo en el '
       'turno. La plantilla crece con personas: {INCORPORACIONES_A2} de incorporaciones el año 2 y otro tanto el año 3. '
       'Convenio provincial de hostelería: el art. 4 del VI Acuerdo Laboral de ámbito Estatal para el sector de '
       'Hostelería no nombra la pollería ni el asador de pollos, pero incluye los restaurantes y el reparto de comidas '
       'preparadas; todos por encima del SMI de 2026 (1.221 € al mes en 14 pagas, Real Decreto 126/2026) en proporción a '
       'la jornada; contratos por escrito; registro de jornada obligatorio (art. 34.9 del Estatuto de los Trabajadores; '
       'NO digas que la ley lo exige «digital»); nunca autónomos que te facturan con tu horario (falso autónomo, art. '
       '1.1). Repartidor propio, si algún día lo pones: contrato laboral del convenio de hostelería; en el reparto que '
       'organiza una plataforma por algoritmo, la ley presume la relación laboral (disposición adicional 23.ª del '
       'Estatuto). Formación de manipuladores acreditada por la empresa (el antiguo carné de manipulador ya no existe) con '
       'el crudo y el cocinado separados, la sonda, la vitrina, el enfriado, el ovoproducto y los alérgenos; formación del '
       'asador (calibre, espetado, orden de carga, sonda y trinchado); prevención de riesgos (quemaduras del asador, de '
       'las espadas calientes y de la freidora, cortes al trinchar y al espetar, gas y calor).',
    8: 'Plan financiero, TODO por token: inversión {INVERSION_TOTAL} = compras {CAPEX} (obra, conducto, asador, equipo y '
       'puesta en marcha {INVERSION_PARTIDAS}, más la fianza {FIANZA} y {RENTA_PREVIA} de renta antes de abrir) + fondo '
       'de maniobra {FONDO_MANIOBRA}; IVA de la inversión {IVA_INVERSION}; necesidad de caja {NECESIDAD_CAJA}; '
       'financiación {RECURSOS_PROPIOS} propios + préstamo {PRESTAMO} al {TIPO_PRESTAMO}, {PLAZO_PRESTAMO} años con '
       '{CARENCIA} de carencia, cuota {CUOTA_ANUAL}. Cuenta de resultados de 3 años: ventas {VENTAS_A1}/{VENTAS_A2}/'
       '{VENTAS_A3}; margen bruto {MARGEN_BRUTO_PCT_A1} (después de TODOS los costes variables: mercancía '
       '{MERCANCIA_PCT_A1}, envases, plataforma, medios de pago y varios); personal {PERSONAL_A1}; alquiler '
       '{ALQUILER_ANO} ({ALQUILER_PCT_A1}); residuos y aceite usado {RESIDUOS_ANO} («pon la tasa de tu ayuntamiento»); '
       'resultado de explotación antes de amortizaciones e intereses {EBITDA_A1} ({EBITDA_PCT_A1}); neto '
       '{NETO_A1}/{NETO_A2}/{NETO_A3} ({NETO_PCT_A1}/{NETO_PCT_A2}/{NETO_PCT_A3}; el año 3 tributa al tipo general del '
       'Impuesto de Sociedades, un 25 %: si tu cifra de negocios no llega a 1 millón de euros, el tuyo será más bajo, '
       'confírmalo con tu asesor). EL FOOD COST CON HONESTIDAD: la comida va al {FOOD_COST}, la media de TODA la carta '
       'más la merma (el pollo entero solo sale a {FC_POLLO_ENTERO}, siempre sobre el precio SIN IVA; las patatas, a un '
       '28 %; las croquetas, a un 22 %): el margen de una pollería está en lo que acompaña al pollo. El plan estima el '
       'pollo a 3,05 € el kilo sin IVA, un precio estimado por el kit (en origen se pagaba a unos 2,96 €, según el Diari '
       'de Tarragona; en Makro, el pollo entero limpio estaba a 3,25 € el kilo sin IVA en octubre de 2026): con el precio '
       'de Makro, la comida sube a un 33,5 %, el resultado de explotación del año 1 baja unos 4.900 € y el neto del año 3 '
       'queda en un 6,7 % (cálculo del kit con este mismo Excel): cada punto de food cost de la comida mueve unos 3.300 € '
       'al año, y la palanca es el precio del pollo entero (a 13,50 € sigue dentro de los 11-14 € del mercado), nunca más '
       'deuda. Pon el precio de tu proveedor. CRECIMIENTO tal cual lo hace el Excel: suben los pedidos un {CREC_A2} y un '
       '{CREC_A3} (de {PEDIDOS_DIA} a {PEDIDOS_DIA_A2} y {PEDIDOS_DIA_A3} al día) con el mismo ticket, y la plantilla '
       'crece con personas ({INCORPORACIONES_A2} al año), no con un porcentaje. IVA: la comida al 10 % (para llevar, por '
       'plataforma y en sala; el pan común que se vende suelto va al 4 %, pero es una parte mínima y el Excel lo deja en '
       'la comida); de la bebida, la parte que sale del local con alcohol o con azúcares o edulcorantes añadidos (la '
       'cerveza, el vino y los refrescos azucarados o edulcorados: {BEBIDA_21_PCT} de la bebida, la columna H de su '
       'línea, un {VENTAS_21_PCT} de las ventas) va al 21 % y el resto al 10 %: el IVA medio de la bebida es '
       '{IVA_BEBIDA_LINEA}. En las compras, el IVA soportado de la comida es {IVA_COMPRA_COMIDA} y el de la bebida '
       '{IVA_COMPRA_BEBIDA}. Equilibrio contable {BE_PEDIDOS_DIA} pedidos al día (ingresos {BE_INGRESOS}; holgura '
       '{HOLGURA_CONTABLE}); equilibrio de caja {BE_PEDIDOS_DIA_CAJA} pedidos al día (unos '
       '{POLLOS_SEMANA_EQUILIBRIO_CAJA} pollos a la semana) y holgura {HOLGURA_CAJA}, que es la del PRIMER año (sólo '
       'intereses por la carencia); desde el segundo, con la devolución del principal, la holgura baja a '
       '{HOLGURA_CAJA_A2} ({BE_PEDIDOS_DIA_CAJA_A2} pedidos al día de equilibrio) y en el tercero queda en '
       '{HOLGURA_CAJA_A3} ({BE_PEDIDOS_DIA_CAJA_A3}): esos años son los que hay que vigilar. Las {AFORO} plazas de la sala '
       'no son el techo del negocio: lo es el asador el domingo. DSCR mínimo {DSCR_MIN}. TESORERÍA: el Mes 1 es ENERO, en '
       'el orden del calendario; la rampa arranca al {RAMPA_MES1} y llega al ritmo de crucero en {MESES_RAMPA} meses '
       '(abril), así que cae sobre enero y febrero, los meses más flojos, y por eso el fondo de maniobra cuenta; el saldo '
       'mínimo es {SALDO_MINIMO} en el mes {MES_SALDO_MINIMO} ({MES_SALDO_MINIMO_NOMBRE}) y el año acaba (diciembre) con '
       '{SALDO_MES12}; julio y agosto, el pico, llenan la caja; las pagas extra salen en julio (Mes 7) y diciembre (Mes '
       '12); el IVA se liquida por trimestres naturales (abril, julio, octubre y, el del cuarto trimestre, en enero del '
       'año siguiente). PAYBACK antes de la deuda: el token puede ser una cifra sin unidad o el texto «Más de 3 años» '
       '(hoy, con el fondo de maniobra dentro, es el texto): escribe una frase que lea bien con los dos («El payback antes '
       'de la deuda, en años, …: «{PAYBACK}» con el fondo de maniobra dentro y «{PAYBACK_CAPEX}» sin él»), nunca «no se '
       'recupera en tres años» ni «años» detrás del token. Escenarios: pesimista ({ESC_PES_PEDIDOS} pedidos a '
       '{ESC_PES_TICKET} y {ESC_PES_DIAS} días: ventas {ESC_PES_VENTAS}, neto {ESC_PES_NETO}) y optimista '
       '({ESC_OPT_PEDIDOS} pedidos a {ESC_OPT_TICKET} y {ESC_OPT_DIAS} días: ventas {ESC_OPT_VENTAS}, neto '
       '{ESC_OPT_NETO}). El Excel manda: si cambias una celda verde, el documento se queda atrás.',
    9: 'Marco legal con su cita (sólo esto, dicho así; lo marcado «compruébalo», dilo así y sin cifra): SL unipersonal '
       '(capital desde 1 €, Ley 18/2022) o autónomo. IAE (RDLeg 1175/1990): el epígrafe 677.9 comprende «la '
       'condimentación y venta de alimentos para ser consumidos fuera del lugar de elaboración en raciones»: es el del '
       'asador para llevar; con sala, el grupo 671 (restaurante, por categoría) o el 673.2, cuya nota común faculta a '
       '«vender, en el propio establecimiento, los productos objeto del respectivo servicio», más el 677.9 si la venta '
       'para llevar es la principal: la gestoría decide. El 642.5 («comercio al por menor de huevos, aves, conejos de '
       'granja, caza…», la pollería de crudos) NO ampara asar ni vender comida preparada. Alta censal con el modelo 036; '
       'exento de cuota con menos de 1 millón de cifra de negocio (art. 82.1.c de la Ley de Haciendas Locales). '
       'Apertura: los restaurantes no están en el anexo de la Ley 12/2012: licencia o declaración responsable según la '
       'ordenanza de tu ayuntamiento, con una consulta urbanística previa (uso, salida de humos a cubierta, potencia '
       'trifásica, aforo). Humos: la cocina de un restaurante NO es actividad potencialmente contaminadora de la '
       'atmósfera (catálogo del RD 100/2011, actualizado por el RD 1042/2017): lo decide la ordenanza de cada '
       'ayuntamiento; ejemplo leído, Madrid (Ordenanza 4/2021 de Calidad del Aire, BOCM de 16-04-2021): conducto '
       'exclusivo a cubierta que supere en 1 m la altura del edificio propio y la de cualquier otro en 15 m de radio '
       '(art. 12 y anexo I), limpieza al menos una vez al año y, con leña, carbón u otro combustible sólido, sistemas '
       'específicos de filtrado de partículas (art. 23); en tu ciudad, pide la ordenanza (sin cifras de otras). Gas del '
       'asador, la freidora y el fogón: empresa instaladora habilitada, puesta en marcha certificada de cada aparato e '
       'inspección o revisión cada 5 años (RD 919/2006, ITC-ICG 07 e ITC-ICG 08). Sanidad: declaración responsable al '
       'registro sanitario de tu comunidad autónoma (RD 1021/2022); el RGSEAA sólo aplica si suministras a otros negocios '
       'por encima de lo que permite su art. 3 (venta marginal, localizada y restringida: por ejemplo, pollo asado o '
       'croquetas a un bar de otro titular); APPCC con la flexibilidad del art. 20 del RD 1021/2022. TEMPERATURAS, leídas '
       'en el BOE: el art. 4.1 del RD 1021/2022 fija la «carne de aves de corral» a 4 °C o menos, los despojos de aves '
       '(mollejas) a 3 °C o menos, los preparados de carne (el pollo adobado crudo lo es) a 4 °C o menos y los vegetales '
       'cortados o pelados listos para consumo (la guasacaca, la ensalada) a 4 °C o menos; lo que no está en esa tabla, a '
       'la temperatura de su etiqueta (art. 4.2); el transporte de lo que sale, en medios que mantengan la temperatura '
       '(art. 4.3). Las comidas preparadas (el pollo asado en vitrina, las croquetas, la ensaladilla) siguen el art. 30 '
       'del RD 1086/2020, en la redacción que le dio el RD 1021/2022, al que remite su art. 6 (nunca lo atribuyas al RD '
       '1021/2022 a secas): en caliente, «a una temperatura superior o igual a 63 °C» (30.2); refrigeradas, a 4 °C o menos '
       'si su vida útil pasa de 24 horas y a 8 °C o menos si es menor (30.3); el enfriamiento, «de 60 °C a 10 °C en menos '
       'de dos horas» (30.6); y el recalentado, «por lo menos 74 °C durante al menos quince segundos en el centro del '
       'alimento… en el término de una hora» desde que sale del frigorífico (30.7). La cocción del pollo NO tiene '
       'temperatura legal: la fija tu APPCC (el caso, 74 °C en el muslo con sonda); y ninguna norma fija el tiempo máximo '
       'en vitrina: también tu APPCC. HUEVO: lo que lleva huevo y no se cocina (alioli, mayonesa, ensaladilla, cremas) se '
       'hace con «ovoproductos procedentes de establecimientos autorizados», se conserva «a una temperatura igual o '
       'inferior a 8 °C», se consume «en un máximo de veinticuatro horas» y se registra «la fecha y hora de elaboración» '
       '(art. 9.2 y 9.3 del RD 1021/2022). ETIQUETA: lo que se vende sin envasar o se envasa a petición del cliente (el '
       'pollo que se embolsa al pedirlo, el encargo preparado a su nombre) informa de la denominación y los alérgenos '
       '(RD 126/2015, art. 4); lo que el propio local envasa ANTES del pedido para su venta inmediata (las bandejas ya '
       'cerradas en la vitrina del domingo) lleva todas las menciones de los arts. 9 y 10 del Reglamento (UE) 1169/2011 '
       'salvo la información nutricional: ingredientes, alérgenos resaltados, peso, fecha y conservación (art. 5); '
       'opcional, el cartel de «elaboración propia» (art. 11 del RD 1021/2022). Alérgenos: por escrito o de palabra si la '
       'información «se registre de forma escrita o electrónica en el establecimiento» y es accesible (RD 126/2015, arts. '
       '4.1.b y 6.5.a), y en la venta a distancia, disponible antes de comprar (Reglamento (UE) 1169/2011, art. 14); en '
       'la pollería, la soja y el gluten del adobo peruano (sillao, cerveza negra), el huevo del alioli y de las cremas, '
       'la leche y el cacahuete de algunas cremas según la receta, el gluten, la leche y el huevo de las croquetas y los '
       'sulfitos de la patata pelada envasada o de un adobo con vino. «Sin gluten» sólo con 20 mg/kg o menos tal como se '
       'vende (Reglamento de Ejecución (UE) 828/2014): con freidora compartida con las croquetas, no se promete. IVA (Ley '
       '37/1992, art. 91): en sala, todo al 10 % («el suministro de comidas y bebidas para consumir en el acto», '
       '91.Uno.2.2.º); para llevar y por plataforma, la comida al 10 % pero se excluyen del reducido «a) Las bebidas '
       'alcohólicas» y «b) Las bebidas refrescantes, zumos y gaseosas con azúcares o edulcorantes añadidos» '
       '(91.Uno.1.1.º): la cerveza, el vino y los refrescos azucarados o edulcorados que salen del local van al 21 %; el '
       'pan común, al 4 % (91.Dos.1.1.º a). La versión del art. 91 que entra en vigor el 1 de diciembre de 2026 no cambia '
       'nada de esto para la restauración. Alcohol para llevar o a domicilio: horarios y limitaciones de cada comunidad '
       'autónoma y nunca a menores: consulta la normativa de la tuya (sin cifras). Ley 1/2025 de desperdicio alimentario, '
       'art. 8: el cliente puede llevarse lo que no consuma sin coste (salvo el del envase de plástico de un solo uso) y '
       'el local lo avisa de forma visible, mejor en la carta. Ley 7/2022, art. 55: el envase de plástico de un solo uso '
       'para llevar se cobra aparte en el tique; las bandejas de cartón sin recubrimiento de plástico no lo son y la '
       'bolsa de pollo con lámina y la bandeja de aluminio, consúltalo con tu proveedor. Aceite de la freidora y grasa '
       'del asador: gestor autorizado con certificado de cada recogida. Personal: convenio provincial de hostelería '
       '(ALEH VI, art. 4, que no nombra la pollería), SMI de 2026 (RD 126/2026), Estatuto de los Trabajadores (arts. 1.1 '
       'y 34.9 y disposición adicional 23.ª), Ley 31/1995 de prevención. Facturación con software Veri*factu (consulta '
       'con tu gestoría la fecha que te aplica). El asador ambulante de mercadillo es otro negocio (grupo 675 del IAE, '
       'venta ambulante). El marco legal del plan es el ESPAÑOL: en Perú, México y el resto de Latinoamérica los trámites '
       '(fiscales, municipales y sanitarios) son otros y este plan no los cubre; la guía de equivalencias del pack adapta '
       'los términos. Lo que no esté aquí no se afirma: «compruébalo con tu gestoría, tu ayuntamiento o el inspector».',
    10: 'Conclusiones con tokens (viabilidad, holgura de caja del año 1 y de los años 2 y 3, DSCR mínimo, saldo mínimo, '
        'payback leído como en el §8) y los riesgos de una pollería y cómo se mitigan (R §6, uno por uno): firmar un local '
        'sin salida de humos a cubierta o sin potencia (el error número uno: sin conducto no hay asador ni freidora); '
        'darse de alta sólo en el 642.5; un asador pequeño para el domingo (o grande para el martes: la hoja «Asador» de '
        'la calculadora lo mide); no sondear (dorado por fuera y crudo junto al hueso) y mezclar crudo y cocinado en la '
        'mesa de espetar; el sobrante del domingo sin plan de enfriado ni destino; alioli, ensaladilla o cremas con huevo '
        'crudo; envasar el domingo por la mañana sin la etiqueta completa; olvidar los alérgenos del adobo; cobrar al 10 % '
        'la cerveza y los refrescos azucarados para llevar; vender el pollo solo, sin combos (el entero sale a '
        '{FC_POLLO_ENTERO}); un solo proveedor de pollo y sin calibre fijo; la brasa de leña o carbón sin proyecto; el '
        'maestro asador único y el domingo sin refuerzo; abrirse a la plataforma sin cuentas (techo del {DELIVERY_PCT}). '
        'El plan de acción en 6 fases del checklist (80 tareas: 12/15/14/13/13/13). Cierra con el siguiente paso: '
        'completar el Excel con tus cifras, medir el rendimiento del pollo y el tiempo de tanda de tu asador y '
        'escandallar tu carta con la calculadora.',
}

#: Prohibidos en el texto (F1-camino §4): sellos y palabras vetadas, normas derogadas, la rentabilidad que contradice el
#: caso, restos de los moldes (Food Truck, Tapas Bar, Heladería, Pizzería y la Taquería —la semilla—) y las frases del
#: motor sin traducir. SALEN de la lista por ser oficio de la pollería: leña y horno (brasa peruana), tarrina y raciones
#: (literal del 677.9) y «pan común» (el pan se vende y va al 4 %); «chimenea» pasa a aviso. VUELVEN horchata, mantec y
#: cubeta (no son oficio aquí). «Tortilla» a secas NO se prohíbe (la de patatas es guarnición del asador; el
#: coordinador, 29-oct): sólo la de maíz o de harina y el tortillero. Los usa también `barrido_es.py` sobre los xlsx y
#: el docx.
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
    # restos de la Heladería
    r'helad', r'sorbete', r'granizad',  # «pasteuriz» fuera: el ovoproducto pasteurizado es la norma (RD 1021/2022 art. 9)
    r'horchata', r'mantec', r'cubeta',
    # restos de la Pizzería (sin leña ni horno: son oficio de la brasa peruana; la chimenea va a AVISOS)
    r'pizz', r'napol[ei]t', r'margherita', r'levadura', r'amasad', r'bolas? de masa', r'fior di latte', r'mozzarella',
    r'c[uú]pula', r'\bETG\b', r'pliego', r'97/2010', r'AVPN',
    # restos de la Taquería (la semilla)
    r'taquer', r'trompo', r'\btacos?\b', r'\bcomal', r'\bpastor\b', r'gringa', r'nixtamal', r'tortillas? de (ma[ií]z|harina)',
    r'tortiller[oa]', r'mezcal', r'tequila', r'aguas? frescas?', r'carnitas', r'suadero', r'cochinita', r'guacamole',
    r'salsa macha',
    # frases del motor sin traducir y pids de los moldes
    r'alcohol (que sale por|del canal de) delivery', r'harinas panificables',
    r'plan-negocio-(tapas-bar|heladeria|pizzeria|taqueria)',
]
#: «art. 30» siempre con «RD 1086/2020» (F1-camino §7 F2 (5)): ERROR si un «art. 30» / «artículo 30» no tiene
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


#: Avisos (F1-camino §4): no son error, pero cada uno se revisa a mano.
AVISOS = [
    ('«art. 30 del RD 1021/2022» (es del RD 1086/2020)', re.compile(r'art(?:[ií]culo|\.)\s*30[^.;]{0,20}1021/2022',
                                                                    re.I)),
    ('«sin gluten» prometido', re.compile(r'(?<!no prometer )(?<!nada de )(?<!ni )«?sin gluten»?', re.I)),
    ('«tortilla»: sólo la de patatas del asador', re.compile(r'tortillas?(?! de patatas?)', re.I)),
    ('«mexican…» (resto de la taquería)', re.compile(r'mexican', re.I)),
    ('«chimenea» (resto de la pizzería; aquí, conducto)', re.compile(r'chimenea', re.I)),
    ('«642.5» sin decir que NO ampara asar', re.compile(r'642\.5(?![^.;]{0,200}(no ampara|no cubre|no sirve|no vale))',
                                                       re.I)),
    ('«obligatori…» junto a 74 °C (no hay temperatura legal de cocción)',
     re.compile(r'obligatori\w*[^.;]{0,80}74 ?°C|74 ?°C[^.;]{0,80}obligatori', re.I)),
    ('«broaster» (es pollo frito a presión, no asado)', re.compile(r'broaster', re.I)),
    ('«auténtic» como promesa', re.compile(r'aut[eé]ntic', re.I)),
    ('registro horario «digital obligatorio»', re.compile(r'digital(es)? obligatori|obligatori\w* (en formato )?digital',
                                                          re.I)),
]
#: Cifras que el texto puede llevar escritas: normas y artículos, y TODAS las que traen las pistas y la jerga (research
#: con fuente, carta y estructura del caso, producción, variantes sin Excel, la cuenta del reparto propio y la
#: sensibilidad del food cost). El resto, token o nada.
_BASE = set('''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 33 35 36 40 45 50 60 63 70
74 75 80 90 100 120 150 180 200 300 671 673.2 677.9 642.5 675 1.000 1.221 1/2025 7/2022 37/1992 12/2012 18/2022 31/1995
100/2011 1042/2017 919/2006 4/2021 126/2026 1175/1990 1021/2022 1086/2020 126/2015 1169/2011 828/2014 852/2004 2027 2026
2025 2024 2023 2022 2021 2020 2017 2015 2014 2012 2011 2006 2004 1995 1992 1990 1950 16-04-2021 82.1 91.Uno.1.1 91.Uno.2.2
91.Dos.1.1 1.1 4.1 4.2 4.3 9.2 9.3 30.2 30.3 30.6 30.7 34.9 23.ª 12/15/14/13/13/13 −18 −20 −35'''.split())
RX_NUM = re.compile(r'(?<![\w{])[−+]?\d[\d.,/:−-]*\d|(?<![\w{])\d')
PERMITIDAS = _BASE | set(x.rstrip('.,') for x in RX_NUM.findall(re.sub(r'\{[A-Z0-9_]+\}', '', ' '.join(
    list(PISTAS.values()) + [JERGA]))))
#: Caracteres admitidos además del latín básico/extendido: tipografía española y los signos de temperatura (−, ≤, ≥, ≈).
RX_RARO = re.compile(r'[^\x00-ɏ‐-‧€°→ ‑«»¿¡ºª·…–—“”‘’−≤≥≈²$]')


def ranuras():
    d = json.load(open(os.path.join(BP4, 'docx_es_cat.json'), encoding='utf-8'))['parrafos']
    gem = {}
    for t in ('taq_es_a', 'taq_es_b'):
        gem.update(json.load(open(os.path.join(GEMELA, t + '.json'), encoding='utf-8')))
    fuera = []
    for k in sorted(d, key=int):
        v = d[k]
        if v['rol'] != 'cuerpo':
            continue
        sec = int(v['seccion'])
        fuera.append({'i': int(k), 'seccion': sec, 'palabras_objetivo': int(v['palabras']),
                      'molde_ft_es': v['texto'], 'gemela_formato_taqueria_es': gem.get(k, '')})
    return fuera


def preparar():
    if not os.path.exists(CIFRAS):
        raise SystemExit('falta %s: corre antes cifras_pol_es.py --calc en el VPS y cópialo aquí' % CIFRAS)
    cif = json.load(open(CIFRAS, encoding='utf-8'))['tokens']
    usados = set(re.findall(r'\{([A-Z0-9_]+)\}', ' '.join(PISTAS.values())))
    sin = sorted(usados - set(cif))
    if sin:
        raise SystemExit('las PISTAS citan tokens que no están en cifras_caso_es.json: %s (¿falta --calc?)' % sin)
    for s, p in PISTAS.items():                                   # las pistas también cumplen la regla del art. 30
        assert not art30_mal(p), (s, art30_mal(p))
    os.makedirs(TANDAS, exist_ok=True)
    rs = ranuras()
    for tanda, secs in (('pol_es_a', range(1, 6)), ('pol_es_b', range(6, 11))):
        sel = [r for r in rs if r['seccion'] in secs]
        ent = {
            'tanda': tanda, 'producto': 'Plan de Negocio: Pollería y Asador de Pollos ES 1.0 (aichef.pro, 35 €)',
            'salida': 'scripts/productos-digitales/plan-polleria/textos/%s.json' % tanda,
            'formato_salida': '{"<i>": "<párrafo en español>", …} con TODOS los "i" de "parrafos" y nada más',
            'brief': 'scripts/productos-digitales/plan-polleria/BRIEF-REDACTORES.md (léelo entero antes)',
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
        print('ERROR falta --tanda (pol_es_a o pol_es_b)')
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
