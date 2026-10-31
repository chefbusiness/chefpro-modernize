#!/usr/bin/env python3
"""
tandas_docx.py — Plan de Negocio: Hamburguesería Smash ES 1.0 (F1-camino §4): prepara y valida las dos tandas de
redacción del plan de negocio (docx). Copia adaptada de `plan-sushi/tandas_docx.py`.

Las 61 ranuras de texto del docx del Food Truck ES (131 párrafos, 10 Heading 1; mapa en
`business-plans-en-4/docx_es_cat.json`) se escriben NUEVAS, en español, para la hamburguesería:
  ham_es_a = §1-5 (29 ranuras) · ham_es_b = §6-10 (32 ranuras).
Gemela de FORMATO: el texto del Sushi Bar ES 1.0 en la misma ranura (`plan-sushi/textos/sus_es_{a,b}.json`, la misma
rejilla: comensal y rotación encendida, el más nuevo y ya revisado): sirve para ver cómo se escribe una ranura con tokens,
nunca su contenido. No hay versión anterior: el material es el research (`F1-research-hamburgueseria.md`) y las pistas de
abajo. Las cifras del Excel (y de la calculadora de la carne, las patatas y el escandallo) van SIEMPRE como token {ASI}
(`cifras_caso_es.json`, con `--calc`); `docx_ham_es.py` las resuelve al ensamblar. Sólo lee JSON.

    python3 tandas_docx.py preparar                       # tandas/ham_es_{a,b}.entrada.json
    python3 tandas_docx.py check --tanda ham_es_a         # valida textos/ham_es_a.json (salida del redactor)

Lo usan también `barrido_es.py` (PROHIBIDOS, PERMITIR, AVISOS y `art30_mal` sobre los xlsx y el docx) y `docx_ham_es.py`.
Sesión Claude Code, 31-oct-2026.
"""
import argparse
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BP4 = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
GEMELA = os.path.join(os.path.dirname(AQUI), 'plan-sushi', 'textos')
TANDAS, TEXTOS = os.path.join(AQUI, 'tandas'), os.path.join(AQUI, 'textos')
CIFRAS = os.path.join(AQUI, 'cifras_caso_es.json')
RESEARCH = 'scripts/productos-digitales/plan-hamburgueseria/F1-research-hamburgueseria.md'

SECCIONES = {
    1: '1. Resumen Ejecutivo', 2: '2. Concepto y Propuesta de Valor', 3: '3. Análisis de Mercado',
    4: '4. Análisis Competitivo', 5: '5. Plan de Marketing y Captación', 6: '6. Plan de Operaciones',
    7: '7. Estructura Organizativa y RRHH', 8: '8. Plan Financiero', 9: '9. Aspectos Legales y Licencias',
    10: '10. Conclusiones y Plan de Acción',
}

#: La jerga del oficio (R §5): se glosa la PRIMERA vez que sale en el Word; y lo que no se dice.
JERGA = ('smash (la bola de carne que se aplasta contra la plancha muy caliente hasta que hace costra) · bola (la porción '
         'de carne cruda: 100 g en el caso) · smasher (la prensa con la que se aplasta) · costra (la superficie tostada que '
         'deja la plancha) · fry-top (la plancha de acero de cocina profesional) · blend (la mezcla de cortes de la carne '
         'picada: aguja, falda y pecho, con un 20 % de grasa) · línea de montaje (la mesa refrigerada donde se monta cada '
         'hamburguesa) · runner (quien lleva la bandeja del mostrador a la mesa) · rider (el repartidor de la plataforma) · '
         'pan brioche y pan de patata o potato bun · patatas cargadas (con queso y bacon) · estilo Oklahoma (la smash con '
         'cebolla muy fina aplastada con la carne). QUÉ NO DECIR: una temperatura de cocción «legal» u «obligatoria» (en '
         'España no existe: la AESAN recomienda 70 °C durante 2 minutos y el APPCC decide); 75 °C (no hay tal regla para la '
         'hamburguesa; los 74 °C son del recalentado) ni los 155 °F o los 68 °C de Estados Unidos; la carne madurada o «dry '
         'aged» como reclamo (Madrid Salud, Inf26008); guardar la picada del local de un día para otro como si se pudiera; '
         '«7 días» de nada; −18 °C como regla general (sólo es el equipo del art. 5 del RD 1021/2022, y con «confírmalo con tu '
         'inspector»); «al punto» o «poco hecha» como promesa; freír a 180 o 190 °C; «sin gluten» como promesa; «auténtica» '
         'o «gourmet» como sello; las cifras de una franquicia o de Goiko como si fueran el caso; el Día de la Hamburguesa '
         '(sin fuente); «pan común» salvo para decir que el pan de hamburguesa no lo es; un medidor de polares «obligatorio»; '
         '«food truck» salvo dentro del nombre «Plan de Negocio: Food Truck»; «validado» (di «justificado ante sanidad» o «que '
         'respalde tu APPCC»); «tapa» ni de un envase (di «cierre»)')

#: Lo que tiene que contar cada sección (español de España, para el mercado español; R §0-§7). Cifras del Excel y de
#: la calculadora = tokens.
PISTAS = {
    1: 'Qué es el negocio: una hamburguesería de smash burgers de servicio rápido (glosa «smash» la primera vez) con '
       'cocina a la vista, mostrador de pedidos con pantalla de turnos, una sala de 30 plazas y 6 taburetes en una barra '
       'de ventana ({AFORO} plazas en total) y una zona de empaquetado y de recogida de los repartidores junto a la '
       'puerta, en un local de unos 90 m² que ya fue de restauración, con salida de humos a cubierta posible, sin '
       'traspaso, en un barrio con vida de noche o una zona universitaria de una ciudad de 150.000 a 500.000 habitantes (o '
       'en un barrio de Madrid, Barcelona o Valencia). Una SL unipersonal con el titular de gerente y jefe de plancha, un '
       'cocinero de plancha, un cocinero de montaje y freidora, un encargado de mostrador y pedidos, un auxiliar de sala y '
       'empaquetado y un refuerzo de viernes a domingo. Carta corta de unas 14 referencias, con IVA: la smash simple con '
       'queso a 8,90 €, la doble a 11,90 €, la triple a 14,50 €, la ración de patatas a 3,90 € y el menú de doble con '
       'patatas y refresco a 15,90 €. Tres canales: la sala (alrededor del 54 % de las ventas), los pedidos para recoger '
       '(un 22 %, por la web y el teléfono, sin comisión) y la plataforma con su reparto ({DELIVERY_PCT}, con techo y sin '
       'reparto propio). Abre en ENERO (el Mes 1 del Excel es enero, en el orden del calendario), de martes a domingo de '
       '13:00 a 16:30 y de 20:00 a 24:00; cierra los lunes y 10 días en la segunda quincena de enero. Cifras clave por '
       'token: {COMENSALES_DIA} comensales EQUIVALENTES al día (escribe siempre la palabra: unos {COMENSALES_SALA} en sala '
       'y el resto, los unos {PEDIDOS_DIA} pedidos al día para llevar y a domicilio, contando cada pedido como 1,7 '
       'comensales) a {TICKET} por comensal sin IVA y {DIAS_APERTURA} días; ventas {VENTAS_A1}, resultado neto {NETO_A1} '
       '({NETO_PCT_A1}), inversión {INVERSION_TOTAL} (de la que {INVERSION_PARTIDAS} son obra, cocina, frío, equipo y '
       'puesta en marcha), préstamo {PRESTAMO} y equilibrio de caja en {BE_COMENSALES_DIA_CAJA} comensales al día. Qué '
       'contiene el kit: este plan de negocio de 10 secciones, el Excel del plan financiero de 9 hojas, el checklist de '
       'apertura de 80 tareas en 6 fases, la calculadora de la carne, las patatas y el escandallo (el coste por kilo útil '
       'de la carne comprada picada y de la pieza picada en el local, las bolas que salen de cada kilo, el coste de cada '
       'ración de patatas y del aceite, y el escandallo de 14 productos con su margen en sala, para llevar y en '
       'plataforma) y la guía de equivalencias para Latinoamérica (el marco legal del plan es el español). Lo que lo '
       'distingue, en una frase: la carne con números ({BOLAS_KG} bolas de 100 g por kilo y unos {CARNE_DIA_KG} kilos de '
       'carne al día, estimaciones del kit que mides tú) y la norma de la carne picada y de la freidora contada bien: el '
       'art. 7.2 del RD 1021/2022 si picas en el local, nada de carne madurada, la cocción sin temperatura legal que '
       'decide tu APPCC y la acrilamida, con la fritura por debajo de 175 °C.',
    2: 'Tipos de hamburguesería y por qué esta (R §3, sin cifras de Excel para las otras): (A) la de sólo reparto a '
       'domicilio en 40-60 m² y sin sala (si el reparto es la actividad principal, el IAE es el 677.9; una cadena '
       'española nació con el 90 % de su venta a domicilio, según la prensa): para esa, la Guía Dark Kitchen de AI Chef '
       'Pro; (B) la smash de servicio rápido con sala, para llevar y a domicilio (la de este plan); (C) la hamburguesería '
       'con servicio de mesa en 120-150 m² y 60-80 plazas, con un ticket de 25-30 € y la bola gruesa de 180 g que el '
       'cliente pide poco hecha: su riesgo es la cocción, que decide el APPCC (ver §9), y su inversión, la de una '
       'franquicia; (D) el carrito o el puesto de smash en la calle y en eventos: para ese, el Plan de Negocio: Food '
       'Truck de AI Chef Pro; (E) la franquicia (ver §4). GLOSA LA JERGA la primera vez (ver `jerga` de la entrada): '
       'smash, bola, smasher, costra, fry-top, blend, línea de montaje, runner, rider. El ticket de {TICKET} es por '
       'comensal equivalente y sin IVA ({TICKET_IVA} con IVA) y sale de tres canales, con estas cifras exactas: el '
       'comensal de sala deja 17,00 € con IVA (15,45 € sin IVA: hamburguesa, patatas, bebida y algún extra, con el '
       'descuento del menú); el pedido para recoger, de media 29,10 € con IVA (casi dos menús), sale a 15,56 € por '
       'comensal equivalente; y el de plataforma, con la carta un 15 % más cara, 33,47 € con IVA, a 17,90 € por comensal '
       'equivalente. Mezcla de ventas: comida {PCT_COMIDA} y bebida {PCT_BEBIDA} (en sala, la bebida es un 19 % de lo que '
       'se vende; fuera, un 12 %). La propuesta: carta corta, bola de 100 g con costra, pan tostado, patatas fritas con su '
       'guía de colores, el pedido en el mostrador con pantalla de turnos, la recogida en el local empujada con precio y la '
       'plataforma con techo.',
    3: 'Mercado en España con fuente. Las hamburgueserías facturaron 3.730 millones de euros en 2025, un 5,2 % más, el 61 '
       '% de la comida rápida, con las aperturas creciendo un 0,8 % (DBK, publicado en septiembre de 2026); las cinco '
       'grandes cadenas de comida rápida suman unos 3.000 locales y alrededor del 75 % del valor (no las nombres). La '
       'hamburguesa es el plato más pedido a domicilio en España por tercer año (Gastrómetro de Just Eat 2025, publicado '
       'en prensa en diciembre de 2025): por eso el plan cuenta con la plataforma. El smash es el formato de moda: una '
       'cadena portuguesa de smash con 35 locales abrió en Madrid a finales de septiembre de 2026 (Alimarket). Búsquedas '
       'mensuales en Google España (DataForSEO, 31 de octubre de 2026): «smash burger» 49.500, «hamburguesería» 22.200, '
       '«pan brioche» 14.800, «patatas fritas» 12.100, «batido» 4.400, «hamburguesería smash» 2.900 y «hamburguesas a '
       'domicilio» 1.000; y quien va a abrir busca poco: «franquicia hamburguesería» 210 y «cómo montar una '
       'hamburguesería» o «plan de negocio hamburguesería», 10. En México, «smash burger» 18.100 y «negocio de '
       'hamburguesas» 320. El consumidor busca muchísimo; el que va a abrir decide con datos. Precio en carta, con IVA '
       '(cartas leídas en octubre de 2026, sin nombres): una cadena de smash de Málaga vende la hamburguesa a 11,50 € con '
       'bola de 100 g, los menús de 13,90 a 21,90 €, las patatas a 4,00 € y la lata a 2,50 €; en Barcelona, la smash a '
       '13 € y el menú a 15 €. El caso pone la doble a 11,90 € y el menú a 15,90 €. NO hay una cifra fiable del número de '
       'hamburgueserías en España ni de su ticket medio: no las des. ESTACIONALIDAD del plan, con el Mes 1 en ENERO y en '
       'el orden del calendario: enero es el valle (un 7,2 % del año, con el cierre de 10 días y la cuesta de enero), '
       'mayo es el pico (un 8,9 %, con el buen tiempo y el fin de curso), junio le sigue (un 8,8 %) y agosto baja (un 7,6 '
       '%, con la ciudad vacía); entre el mejor mes y el peor hay un 24 %. En la costa, julio y agosto suben: gira la fila '
       'de la Tesorería. El hueco: la SERP da páginas de software y de modelos con inversiones sin fuente («en torno a '
       '80.000 €», «60.000-80.000 € para 30-50 m²»), foros y un curso; nadie cuenta el art. 7 del RD 1021/2022, la carne '
       'madurada, la acrilamida ni el coste de cada bola por canal. NADA de tamaños de mercado sin fuente.',
    4: 'Competencia por categorías: las grandes cadenas de comida rápida (sin nombres); las cadenas de hamburguesería '
       'con sala y servicio de mesa y las de smash; las dark kitchens que sólo venden por plataforma; y la hamburguesería '
       'de barrio. AVISO DE MERCADO, no caso: Goiko vendió 109 millones de euros en 2025, un 11,2 % menos, y perdió 36,4 '
       'millones (Alimarket): el tamaño no garantiza nada. FRANQUICIA FRENTE A MARCA PROPIA, razonado: La Pepita Burger '
       'Bar pide 250.000 € de inversión en un local de 140 m² o más, con un canon de 30.000 € y un 4,5 % más un 1,5 % de '
       'royalty y publicidad (emprendedores.es); otras cadenas de hamburguesas piden de 200.000 a 300.000 € en 120-180 m² '
       'según los portales de franquicias (compruébalo con cada marca). La franquicia trae marca, proveedores, formación '
       'y carta a cambio del canon, la cuota y un local más grande que el de este plan; con marca propia, la inversión es '
       '{INVERSION_TOTAL} en 90 m² y te quedas el margen, pero la carta, la carne y la plancha son tuyas. Las cifras de '
       'franquicia NO sirven para un local de 90 m²: compara las dos cuentas antes de firmar. Dónde gana este concepto: '
       'una carta corta, la carne con su ficha técnica y dos proveedores, el coste de cada bola (el kilo útil del blend '
       'comprado picado sale a {COSTE_KG_UTIL_BLEND} y el de la pieza picada en el local a {COSTE_KG_UTIL_PIEZA} antes de '
       'la mano de obra de limpiarla y picarla, con los valores del kit), el escandallo por canal y la recogida en el '
       'local. Los riesgos: el precio de la carne, la plataforma (en ella el margen del menú cae casi un tercio: de '
       '{MARGEN_SALA_MENU} en sala a {MARGEN_PLATAFORMA_MENU}), un solo proveedor de carne y la plancha como cuello de '
       'botella del servicio; cómo se defiende (dos proveedores, escandallo por canal, recogida en el local, carta corta y '
       'un segundo que sepa llevar la plancha).',
    5: 'Marketing y captación: apertura en enero (los curiosos llegan el primer mes; la clientela fija y la nota en las '
       'plataformas tardan un trimestre); ficha de Google Business con el horario, fotos reales y respuesta a cada reseña; '
       'redes con vídeo (la smash se vende en vídeo: el aplastado y la costra); la zona universitaria y las oficinas a '
       'mediodía; el calendario: mayo y junio (el buen tiempo y el fin de curso, los picos del año), la vuelta de '
       'septiembre, octubre con el fútbol y Halloween y enero, el valle, con promociones de recogida; fidelización '
       'sencilla (pedido propio por la web o el teléfono para recoger) sin cifras de conversión inventadas. PLATAFORMA '
       'FRENTE A RECOGIDA (razonado, con el Excel): el plan vende por plataforma con su reparto un {DELIVERY_PCT} de las '
       'ventas ({VENTAS_PLATAFORMA_A1} al año) y paga una comisión del {COMISION_DELIVERY} ({COMISIONES_DELIVERY_A1} al '
       'año); las guías del sector sitúan el plan básico de Uber Eats en torno al 30 % más IVA, Glovo entre el 15 y el 35 % '
       'según la zona y Just Eat entre el 13 y el 35 %, más las promociones y la caja. La hamburguesa viaja bien; las '
       'patatas, peor: cucurucho ventilado y fritas al final. Pasar 10 puntos de las ventas de la plataforma a la recogida '
       'en el local ahorra unos 13.700 € de comisión al año (menos lo que dejes de cobrar por el precio más alto de la '
       'plataforma); si la plataforma llegara a un tercio de las ventas, pagarías unos 12.300 € más; y con el 45 % de una '
       'cadena que nació casi sólo a domicilio, unos 28.700 € más: la recogida no paga comisión, empújala con precio. Un '
       'repartidor propio sólo con contrato laboral y cuando el volumen lo pague. Presupuesto de marketing {MARKETING_ANO} '
       'al año, más la marca, la web, las fotos y el vídeo de lanzamiento, que van en la inversión ({MARCA_LANZAMIENTO}).',
    6: 'Operaciones de la plancha, la freidora y la línea. LA CARNE CON NÚMEROS (la calculadora del pack, valores por '
       'defecto que son estimación del kit y editables): el blend de vacuno comprado ya picado (aguja, falda y pecho con un '
       '20 % de grasa) a 8,90 € el kilo sin IVA sale a {COSTE_KG_UTIL_BLEND} el kilo útil con la merma de cierre del 3 %; '
       'la pieza para picar en el local, a 7,50 € el kilo con un 90 % de aprovechamiento (sin fuente: mídelo), a '
       '{COSTE_KG_UTIL_PIEZA} antes de la mano de obra, y la calculadora te dice hasta qué coste de limpiar y picar te '
       'compensa. De un kilo salen {BOLAS_KG} bolas de 100 g en crudo, cinco hamburguesas dobles (la pregunta que más se '
       'busca), y {BOLAS_KG_NETAS} con la merma de cierre; con unas 1,6 bolas por comensal, el caso pide unos '
       '{CARNE_DIA_KG} kilos de carne al día, que dimensionan el pedido diario y, si picas, el picado del día del art. 7.2. '
       'EL ESCANDALLO, siempre sobre el precio SIN IVA: la smash simple con queso cuesta {COSTE_SIMPLE} (un {FC_SIMPLE} '
       'de 8,09 € sin IVA, 8,90 € con IVA) y la doble {COSTE_DOBLE} (un {FC_DOBLE} de 10,82 € sin IVA, 11,90 € con IVA), '
       'con una loncha de queso de 20 g por bola; la ración de patatas congeladas sale a {COSTE_RACION_PATATA_CONG} y la '
       'fresca cortada en casa a {COSTE_RACION_PATATA_FRESCA} antes de la mano de obra de pelar, cortar y remojar (la '
       'calculadora dice hasta qué coste te compensa); el aceite pone {ACEITE_RACION} en cada ración; la semana ponderada '
       'del kit, un {FC_PONDERADO}. El plan usa patata congelada: la fresca es una decisión de marca, no de coste. EQUIPO '
       'con precio y fuente: plancha fry-top de acero a gas de 100 cm y tostador de pan {PLANCHA} (una de 80 cm va de unos '
       '771 a 1.399 € sin IVA según la gama), dos freidoras de doble cuba y el mantenedor de patatas {FREIDORAS} (dos, '
       'para no mezclar las patatas con los rebozados), campana extractora {CAMPANA}, mesa refrigerada de montaje y bajo '
       'plancha refrigerado para las bolas {MESA_REFRIGERADA}, frío {FRIO} (el armario de carne a 2 °C o menos), barra '
       'de batidos y cerveza {BARRA} y el conducto exclusivo a cubierta {CONDUCTO}. Oficio, orientativo: plancha a '
       '220-250 °C, unos 90 segundos del primer lado y 60 del segundo. Horario: de martes a domingo de 13:00 a 16:30 y de '
       '20:00 a 24:00; la producción (porcionar las bolas, las salsas, la verdura cortada, reponer la línea) se hace '
       'antes de abrir. HIGIENE EN LA OPERACIÓN: armario de carne a 2 °C o menos; la bola se sala en la plancha (salada '
       'antes, es preparado de carne y va a 4 °C o menos); si picas en el local, sólo lo del día; espátulas, pinzas y '
       'bandejas de crudo separadas de las de lo hecho; una bola por tanda medida con sonda, con la temperatura que fije '
       'tu APPCC (la AESAN recomienda 70 °C durante 2 minutos); la verdura cortada a 4 °C o menos; la freidora por '
       'debajo de 175 °C con la guía de colores a la vista; los compuestos polares del aceite por debajo del 25 % y cada '
       'cambio anotado; el aceite usado, a un gestor autorizado. El Kit de Tareas Recurrentes: Hamburguesería de AI Chef '
       'Pro trae las hojas de la plancha, la freidora, la línea de montaje y el reparto: cítalo. PROVEEDORES: dos de carne '
       'con su ficha técnica (blend, porcentaje de grasa y fecha de sacrificio o de envasado en cada albarán), uno de pan '
       '(brioche o de patata, con sus alérgenos) y la patata con su ficha. Suministros {SUMINISTROS_MES} al mes de media '
       '(gas de la plancha, luz de las freidoras, extracción, frío y clima); mantenimiento {MANTENIMIENTO_ANO} al año (la '
       'limpieza de la campana extractora y del conducto, la plancha y el gas, las freidoras y el frío); residuos y aceite '
       'usado {RESIDUOS_ANO}.',
    7: 'Equipo (7 filas en la hoja Personal): el titular, gerente y jefe de plancha (compra la carne y elige el blend y '
       'los proveedores, firma la carta y el APPCC, lleva la plancha en el servicio fuerte, las plataformas y la gestión; '
       '{SUELDO_TITULAR} brutos al mes en 14 pagas; como administrador de la SL cotiza en el régimen de autónomos: '
       'confírmalo con tu gestoría); un cocinero de plancha (aplasta cada bola, saca la costra y lleva los tiempos: el '
       'jefe de plancha único es un riesgo, no un ahorro, porque si falta la plancha no sale); un cocinero de montaje y '
       'freidora (la línea, las patatas, las salsas, el porcionado de las bolas y la mise en place); un encargado de '
       'mostrador y pedidos (caja, pantalla de turnos, pedidos para recoger, las tablets de las plataformas, el '
       'empaquetado y la información de alérgenos); un auxiliar de sala y empaquetado de 30 horas (el runner que lleva '
       'las bandejas, recoge y friega); un refuerzo de viernes a domingo para la segunda plancha y el empaquetado (sin '
       'reparto propio); y las suplencias de vacaciones y descansos: {PLANTILLA_PERSONAS} personas y {JORNADAS} jornadas '
       'completas equivalentes, coste {PERSONAL_A1} ({PERSONAL_PCT_A1} de las ventas), cobertura de horas '
       '{COBERTURA_HORAS} ({HORAS_CONTRATADAS} horas contratadas frente a {HORAS_NECESARIAS} necesarias); el viernes y el '
       'sábado por la noche hacen falta seis personas (dos en la plancha, una en montaje y freidora, una en el mostrador, '
       'una empaquetando y una llevando bandejas) y el cuadrante anual no lo ve: ponlo en el turno. Salarios de mercado '
       'en los portales de empleo (octubre de 2026): un cocinero de cadena, de 22.000 a 25.000 € brutos al año; un '
       'ayudante de hamburguesería, de 16.000 a 18.000 €. La plancha es el cuello de botella: contrata a quien la va a '
       'llevar ANTES de la obra y que opine sobre la línea. La plantilla crece con personas: {INCORPORACIONES_A2} de '
       'incorporaciones el año 2 y otro tanto el año 3. Convenio provincial de hostelería: el art. 4 del VI Acuerdo '
       'Laboral de ámbito Estatal para el sector de Hostelería nombra expresamente las hamburgueserías; todos por encima '
       'del SMI de 2026 (1.221 € al mes en 14 pagas, Real Decreto 126/2026) en proporción a la jornada; contratos por '
       'escrito; registro de jornada obligatorio (art. 34.9 del Estatuto de los Trabajadores; NO digas que la ley lo exige '
       '«digital»); nunca autónomos que te facturan con tu horario (falso autónomo, art. 1.1). Repartidor propio, si algún '
       'día lo pones: contrato laboral del convenio de hostelería; en el reparto que organiza una plataforma por '
       'algoritmo, la ley presume la relación laboral (disposición adicional 23.ª del Estatuto). Formación de manipuladores '
       'acreditada por la empresa (el antiguo carné de manipulador ya no existe) con la carne picada, la sonda de cocción, '
       'el aceite de la freidora, los alérgenos y el contacto cruzado; formación de la línea (gramos de la bola, aplastado '
       'y montaje: pesa 10 bolas de cada persona); prevención de riesgos (quemaduras de la plancha y de las freidoras, '
       'resbalones con la grasa, cortes y cargas).',
    8: 'Plan financiero, TODO por token: inversión {INVERSION_TOTAL} = compras {CAPEX} (obra, cocina, frío, equipo y '
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
       'confírmalo con tu asesor). EL FOOD COST CON HONESTIDAD: la comida va al {FOOD_COST}, el lado prudente. El '
       'escandallo teórico de la calculadora sale en un {FC_PONDERADO} de media ponderada (la doble, en un {FC_DOBLE}, '
       'siempre sobre el precio SIN IVA), y la diferencia es lo que se pierde entre la receta y la caja: las bolas, el pan '
       'y las salsas que se tiran al cierre (un punto y medio), las comidas del personal, las invitaciones, los errores y '
       'las reclamaciones de la plataforma (otro punto y medio) y las promociones de la plataforma, el dos por uno o la '
       'primera compra (un punto): unos cuatro puntos. La carne es un precio estimado por el kit (no hay precio '
       'profesional publicado de la carne picada). Cada punto de food cost de la comida mueve unos {PUNTO_FOOD_COST_A1} '
       'al año; la carne es más o menos un 55 % de la compra de comida: si sube un 20 %, el resultado antes de impuestos '
       'baja unos 11.800 €. Mide tu consumo real (compras de comida ÷ ventas de comida del mes) el primer trimestre y '
       'cambia la celda. La palanca, si los números no salen, es el precio de la carta, nunca más deuda. CRECIMIENTO tal '
       'cual lo hace el Excel: suben los comensales un {CREC_A2} y un {CREC_A3} (de {COMENSALES_DIA} a '
       '{COMENSALES_DIA_A2} y {COMENSALES_DIA_A3} al día) con el mismo ticket, y la plantilla crece con personas '
       '({INCORPORACIONES_A2} al año), no con un porcentaje. IVA: la comida al 10 % (en sala, para llevar y a domicilio); '
       'de la bebida, la parte que sale del local con alcohol o con azúcares o edulcorantes añadidos (la cerveza y los '
       'refrescos, también los zero: {BEBIDA_21_PCT} de la bebida, la columna H de su línea, un {VENTAS_21_PCT} de las '
       'ventas) va al 21 % y el resto al 10 %: el IVA medio de la bebida es {IVA_BEBIDA_LINEA}. En las compras, el IVA '
       'soportado de la comida es {IVA_COMPRA_COMIDA} (el queso, el huevo, la leche, la patata fresca y la verdura se '
       'compran al 4 %; el pan de hamburguesa, que no es pan común, y el aceite de girasol, al 10 %) y el de la bebida '
       '{IVA_COMPRA_BEBIDA}. Equilibrio contable {BE_COMENSALES_DIA} comensales al día (ingresos {BE_INGRESOS}; holgura '
       '{HOLGURA_CONTABLE}); equilibrio de caja {BE_COMENSALES_DIA_CAJA} comensales al día y holgura {HOLGURA_CAJA}, que '
       'es la del PRIMER año (sólo intereses por la carencia); desde el segundo, con la devolución del principal, la '
       'holgura queda en {HOLGURA_CAJA_A2} ({BE_COMENSALES_DIA_CAJA_A2} comensales al día de equilibrio) y en el tercero '
       'en {HOLGURA_CAJA_A3} ({BE_COMENSALES_DIA_CAJA_A3}): esos años son los que hay que vigilar. ROTACIÓN: el caso pide '
       '{ROTACION_IMPLICITA} comensales por plaza y día con los pedidos dentro, frente a un techo físico de {ROT_MAX} '
       '(comidas y cenas con pedido en el mostrador y estancias de 30-40 minutos); el equilibrio de caja pide '
       '{ROT_BE_CAJA}; la rotación real de la sala, sin los pedidos, ronda {ROT_SALA}. DSCR mínimo {DSCR_MIN}. TESORERÍA: '
       'el Mes 1 es ENERO, en el orden del calendario; la rampa arranca al {RAMPA_MES1} y llega al ritmo de crucero en '
       '{MESES_RAMPA} meses (abril); el saldo mínimo es {SALDO_MINIMO} en el mes {MES_SALDO_MINIMO} '
       '({MES_SALDO_MINIMO_NOMBRE}) y el año acaba, en diciembre, con {SALDO_MES12}; enero, el valle, y agosto se notan en '
       'la caja; las pagas extra salen en julio (Mes 7) y diciembre (Mes 12); el IVA se liquida por trimestres naturales '
       '(abril, julio, octubre y, el del cuarto trimestre, en enero del año siguiente). PAYBACK antes de la deuda: el token '
       'puede ser una cifra sin unidad o el texto «Más de 3 años» (hoy es una cifra): escribe una frase que lea bien con '
       'los dos («El payback antes de la deuda, en años, …: «{PAYBACK}» con el fondo de maniobra dentro y '
       '«{PAYBACK_CAPEX}» sin él»), nunca «años» detrás del token. Escenarios: pesimista ({ESC_PES_COMENSALES} '
       'comensales a {ESC_PES_TICKET} y {ESC_PES_DIAS} días: ventas {ESC_PES_VENTAS}, neto {ESC_PES_NETO}) y optimista '
       '({ESC_OPT_COMENSALES} comensales a {ESC_OPT_TICKET} y {ESC_OPT_DIAS} días: ventas {ESC_OPT_VENTAS}, neto '
       '{ESC_OPT_NETO}). El Excel manda: si cambias una celda verde, el documento se queda atrás.',
    9: 'Marco legal con su cita (sólo esto, dicho así; lo marcado «compruébalo», dilo así y sin cifra): SL unipersonal '
       '(capital desde 1 €, Ley 18/2022) o autónomo. IAE (RDLeg 1175/1990): con comedor, el grupo 671 (restaurantes, por '
       'categoría); de barra y mostrador sin comedor separado, el 673; la nota común de esos grupos faculta para vender '
       'para llevar; si el reparto a domicilio fuera la actividad principal, el 677.9: la gestoría decide. Alta censal con '
       'el modelo 036; exento de cuota con menos de 1 millón de cifra de negocio (art. 82.1.c de la Ley de Haciendas '
       'Locales). Apertura: los restaurantes no están en el anexo de la Ley 12/2012: licencia o declaración responsable '
       'según la ordenanza de tu ayuntamiento, con una consulta urbanística previa (uso, extracción a cubierta, potencia, '
       'gas, aforo). Humos: lo decide la ordenanza de cada ayuntamiento; ejemplo leído, Madrid (Ordenanza 4/2021 de '
       'Calidad del Aire): conducto exclusivo a cubierta que supere en 1 m la altura de lo que haya en 15 m (art. 12 y '
       'anexo I), limpieza al menos una vez al año (art. 23) y sólo se libra lo eléctrico de hasta 4 kW sin olores (art. '
       '24), que no es una plancha con dos freidoras; en tu ciudad, pide la ordenanza (sin cifras de otras). Gas: '
       'instalación por empresa habilitada, certificado y puesta en marcha de cada aparato e inspección o revisión cada 5 '
       'años (RD 919/2006). Sanidad: declaración responsable al registro sanitario de tu comunidad autónoma (RD '
       '1021/2022); el RGSEAA sólo aplica si suministras a otros negocios por encima de lo que permite su art. 3. LA CARNE '
       'PICADA, leída en el BOE: el RD 1021/2022 se aplica a la restauración (su art. 2.2.a incluye los «establecimientos '
       'de restauración y hostelería» en el comercio al por menor); carne picada a 2 °C o menos y preparados de carne a 4 '
       '°C o menos (art. 4.1); la bola sin sal es carne picada («menos de 1 % de sal», Reglamento (CE) 853/2004, anexo I, '
       '1.13) y salada o aliñada antes de la plancha pasa a preparado de carne (1.15): la smash se sala en la plancha. Si '
       'picas en el local: «El picado de la carne se efectuará a petición y a la vista del comprador. No obstante, el '
       'picado podrá realizarse con carácter previo, con arreglo a las necesidades del despacho diario, no pudiendo '
       'conservarse de un día para otro» (art. 7.2), y cumples los capítulos II y III de la sección V del anexo III del '
       'Reglamento (CE) 853/2004 (art. 7.3): sólo músculo esquelético con su grasa, sin recortes ni desperdicios, la carne '
       'a 7 °C o menos al picarla, picada dentro de los 6 días siguientes al sacrificio (15 si es vacuno deshuesado y '
       'envasado al vacío) y a 2 °C o menos nada más picarla. Si la compras picada a una carnicería, ese suministro entre '
       'minoristas tiene que ser marginal, localizado y restringido (art. 3). CARNE MADURADA: Madrid Salud (informe '
       'Inf26008, febrero de 2026) dejó escrito que no se puede elaborar carne picada con carne madurada más de quince '
       'días, y la Comunidad de Madrid, que no es una práctica permitida: nada de «dry aged burger». CONGELAR BOLAS '
       'PROPIAS: el plan compra y no congela; si congelas, el art. 5 del RD 1021/2022 pide envasarlas y etiquetarlas con '
       'las fechas de elaboración, congelación y caducidad, un equipo que las lleve a −18 °C o menos en el centro con un '
       'descenso ininterrumpido (no un arcón de mantenimiento), registro, descongelación en frío y no recongelar; con carne '
       'picada en el local, confírmalo antes con tu inspector, porque el art. 7.2 no deja guardarla para otro día. LA '
       'COCCIÓN: en España no hay una temperatura legal de cocción de la hamburguesa. El art. 30 del RD 1086/2020, en la '
       'redacción que le dio el RD 1021/2022 (nunca lo atribuyas al RD 1021/2022 a secas), fija el mantenimiento en '
       'caliente a 63 °C o más (30.2), las refrigeradas a 4 °C u 8 °C (30.3), el enfriado de 60 a 10 °C en menos de 2 '
       'horas (30.6) y el recalentado a 74 °C durante 15 segundos (30.7), no una temperatura de cocinado. La AESAN '
       'RECOMIENDA el cocinado completo a 70 °C o más durante al menos 2 minutos y dice que las hamburguesas de carne '
       'picada deben cocinarse completamente; si la etiqueta del proveedor pide cocinarla, no se sirve poco hecha. No hay '
       'obligación de aviso en carta: no la afirmes. Tu APPCC fija el punto de control crítico con sonda; la smash fina '
       'sale hecha en la plancha y el riesgo es la bola gruesa que se pide poco hecha. ACRILAMIDA (Reglamento (UE) '
       '2017/2158): la restauración aplica el anexo II, parte A (art. 2.2): patatas con poco azúcar y «las patatas deberán '
       'almacenarse a una temperatura superior a 6 °C»; la fresca, en remojo en agua fría de 30 minutos a 2 horas (o unos '
       'minutos en caliente) y enjuagada, mejor escaldada; la congelada, con las instrucciones del fabricante; «las '
       'temperaturas al freír serán inferiores a 175 °C y, en cualquier caso, lo más bajas posible»; espumar el aceite; '
       'una guía de colores a la vista del personal, también para el pan tostado; sin muestreo, pero con pruebas de que lo '
       'aplicas; una franquicia con suministro central añade la parte B; el nivel de referencia de las patatas fritas es '
       'de 500 µg/kg (anexo IV). ACEITE (Orden de 26 de enero de 1989, vigente): «el contenido en componentes polares '
       'será inferior al 25 por 100» (art. 6.3), en bares y en las cocinas de comida para llevar (art. 3); nada se añade al '
       'baño y el aceite usado no vuelve a la cadena alimentaria (art. 9): gestor autorizado. La norma no obliga a un '
       'medidor: el APPCC elige tiras, medidor o cambio por frecuencia. Comidas preparadas en caliente (salsas cocinadas): '
       'el art. 30 del RD 1086/2020. Verdura cortada a 4 °C o menos (RD 1021/2022, art. 4.1). ETIQUETA: lo que se vende sin '
       'envasar o se envasa a petición del cliente informa de la denominación y los alérgenos (RD 126/2015, art. 4); las '
       'hamburguesas que se envuelven ANTES del pedido para tenerlas listas son envasado para la venta inmediata y llevan '
       'las menciones de los arts. 9 y 10 del Reglamento (UE) 1169/2011 salvo la nutricional (art. 5). Alérgenos: por '
       'escrito o de palabra si la información se registra por escrito o en formato electrónico en el local y es '
       'accesible (RD 126/2015, arts. 4.1.b y 6.5.a), y en la venta a distancia, disponible antes de comprar, en la ficha '
       'de cada plato de cada plataforma (Reglamento (UE) 1169/2011, art. 14); en una hamburguesería: el pan (gluten, '
       'huevo y leche, sésamo en el de semillas y soja en algunos), el queso (leche), las salsas (huevo y mostaza), los '
       'encurtidos (mostaza y sulfitos según la marca), los rebozados (gluten, huevo y leche) y los batidos (leche, y '
       'gluten o frutos de cáscara de los toppings). «Sin gluten» sólo con 20 mg/kg o menos tal como se vende '
       '(Reglamento de Ejecución (UE) 828/2014): con pan de trigo en la misma plancha y una freidora compartida con los '
       'rebozados, no se promete; dos freidoras separan las patatas de los rebozados. IVA (Ley 37/1992, art. 91): en sala, '
       'todo al 10 % (91.Uno.2.2.º); para llevar y a domicilio, la comida al 10 %, pero se excluyen del reducido las '
       'bebidas alcohólicas y las bebidas refrescantes, zumos y gaseosas con azúcares o edulcorantes añadidos '
       '(91.Uno.1.1.º a y b): la cerveza y los refrescos, también los zero, que salen del local van al 21 %; el batido de '
       'leche no es una bebida refrescante y el plan lo lleva al 10 % (confírmalo con tu gestoría); el menú que sale del '
       'local se desglosa por componentes (compruébalo con tu gestoría); en las compras, el pan común va al 4 %, pero el '
       'pan de hamburguesa no es pan común y va al 10 % (91.Dos.1.1.º a); el queso, el huevo, la leche, la patata fresca y '
       'la verdura, al 4 % (d, e y f); sólo los aceites de oliva van al 4 % (g): el de girasol, al 10 %. Alcohol para '
       'llevar o a domicilio: horarios y limitaciones de cada comunidad autónoma y nunca a menores: consulta la normativa '
       'de la tuya (sin cifras). Ley 1/2025, art. 8: el cliente puede llevarse lo que no consuma sin coste y el local lo '
       'avisa de forma visible, mejor en la carta. Ley 7/2022, art. 55: el envase de plástico de un solo uso para llevar '
       'se cobra aparte en el tique. Personal: convenio provincial de hostelería (ALEH VI, art. 4), SMI de 2026 (RD '
       '126/2026), Estatuto de los Trabajadores (arts. 1.1 y 34.9 y disposición adicional 23.ª), Ley 31/1995 de '
       'prevención. Facturación con software Veri*factu (consulta con tu gestoría la fecha que te aplica). El marco legal '
       'del plan es el ESPAÑOL: en México y el resto de Latinoamérica los trámites (fiscales, municipales y sanitarios) y la '
       'norma de la carne molida, del aceite y de la acrilamida son otros y este plan no los cubre; la guía de '
       'equivalencias del pack adapta los términos. Lo que no esté aquí no se afirma: «compruébalo con tu gestoría, tu '
       'ayuntamiento o el inspector».',
    10: 'Conclusiones con tokens (viabilidad, holgura de caja del año 1 y de los años 2 y 3, DSCR mínimo, saldo mínimo, '
        'payback leído como en el §8) y los 13 errores de una hamburguesería y cómo se evitan (R §6, uno por uno): picar '
        'hoy para mañana, cuando la picada del local no se guarda de un día para otro (art. 7.2 del RD 1021/2022); la «dry '
        'aged burger» con carne madurada más de quince días (Inf26008); las bolas saladas en la cámara a 4 °C creyendo que '
        'son carne picada (son preparado, y la picada va a 2 °C o menos); prometer el punto sin sonda ni APPCC, o servir '
        'poco hecha una carne cuyo proveedor pide cocinarla; freír demasiado caliente y cambiar el aceite «cuando huele» '
        '(por debajo de 175 °C y polares por debajo del 25 %); una sola freidora para las patatas y los rebozados y luego '
        'prometer «patatas sin gluten»; la plataforma sin techo (comisión, IVA de la comisión y caja; la hamburguesa viaja '
        'bien, las patatas no; techo del {DELIVERY_PCT}); el precio del menú sin escandallo por canal (en plataforma el '
        'margen del menú cae casi un tercio); la carta larga, con merma de pan y de ingredientes; un solo proveedor de '
        'carne y sin ficha técnica del blend; cobrar al 10 % la cerveza o el refresco zero para llevar; copiar la '
        'inversión de una franquicia de 140-180 m² para un local de 90 m²; y abrir sin cuadrante del viernes y el sábado, '
        'cuando la plancha es el cuello de botella. El plan de acción en 6 fases del checklist (80 tareas: '
        '12/15/14/13/13/13). Cierra con el siguiente paso: completar el Excel con tus cifras, pesar 10 bolas y medir la '
        'merma de cocción y las raciones de patata por kilo con la calculadora, y comparar tu consumo real con el '
        '{FOOD_COST} del plan el primer trimestre.',
}

#: Prohibidos en el texto (F1-camino §4 y §7 F2 (4)-(5)): sellos y palabras vetadas, normas derogadas, la rentabilidad
#: que contradice el caso, restos de los moldes (Food Truck, Tapas Bar, Heladería, Pizzería, la Taquería, la Pollería y
#: el Sushi Bar —la semilla—), las frases del motor sin traducir y los errores legales de la carne. SALEN `helad` (el
#: batido lleva helado: barra e IVA de compras) y `pan común` (pasa a AVISO: el pan de hamburguesa no lo es); NO entran
#: «pescado» ni «soja» (alérgenos) ni «vitrina» a secas (etiquetado del art. 5). `mochi` va con límite de palabra (la
#: «mochila» del repartidor). Los usa también `barrido_es.py` sobre los xlsx y el docx, después de borrar `PERMITIR`.
PROHIBIDOS = [
    r'\bfreelance', r'validad[oa]s?', r'Espa[ñn]a,? 2026', r'carn[eé]t? de manipulador(?! ya no existe)',
    r'tarifa plana', r'\bCNAE\b', r'(?<!inscrito en el )\bRGSEAA\b(?!.{0,80}(s[oó]lo|otros (establecimientos|negocios)))',
    r'licencia de apertura', r'895/2013', r'393/2007', r'15 ?(-|–|a|y el) ?25 ?%',
    r'versi[oó]n (1\.1|2\.2|anterior)', r'\bv1\.1\b', r'solopreneur',
    # restos del Food Truck (el nombre «Plan de Negocio: Food Truck» se borra antes: PERMITIR)
    r'food ?truck', r'\bcami[oó]n\b', r'ventanilla', r'generador', r'aparcamiento',
    # restos del Tapas Bar
    r'\btapas?\b', r'gastrobar', r'vermut', r'\bpinchos?\b', r'tapeo', r'afterwork', r'salamandra', r'rational',
    r'[Ff]ichero v1\.1',
    # restos de la Heladería (sin `helad`: el batido lleva helado)
    r'sorbete', r'granizad', r'horchata', r'mantec',
    # restos de la Pizzería
    r'pizz', r'napol[ei]t', r'margherita', r'levadura', r'amasad', r'bolas? de masa', r'fior di latte', r'mozzarella',
    r'c[uú]pula', r'\bETG\b', r'pliego', r'97/2010', r'AVPN', r'\ble[ñn]a\b',
    # restos de la Taquería
    r'taquer', r'trompo', r'\btacos?\b', r'\bcomal', r'al pastor', r'gringa', r'nixtamal', r'tortillas? de',
    r'tortiller[oa]', r'mezcal', r'tequila', r'aguas? frescas?', r'carnitas', r'suadero', r'cochinita', r'guacamole',
    r'salsa macha',
    # restos de la Pollería («pollo crujiente» sí vale)
    r'poller', r'asador de pollos', r'pollo a la brasa', r'broaster', r'pollo asado',
    # restos del Sushi Bar (la semilla)
    r'sushi', r'sashimi', r'nigiri', r'\bmakis?\b', r'uramaki', r'temaki', r'\bpoke\b', r'itamae', r'sushiman',
    r'\bshari\b', r'\bnori\b', r'\bnetas?\b', r'wasabi', r'\bsake\b', r'gyozas?', r'edamame', r'\bmochis?\b', r'tempura',
    r'anisakis', r'hangiri', r'arroceras?', r'ph-metro', r'japon[eé]s', r'combinados?', r'salm[oó]n', r'\bat[uú]n\b',
    r'surimi', r'vitrina refrigerada de sushi', r'[−-]20 ?°C', r'1420/2006',
    # errores legales de la carne (F1-camino §4): 75 °C no existe en España (el 74 °C es del recalentado; `(?<!\d)`
    # para no cazar los 175 °C de la acrilamida) y 155 °F o 68 °C son de EE. UU.
    r'(?<!\d)75 ?°C', r'155 ?°F', r'(?<!\d)68 ?°C',
    # frases del motor sin traducir y pids de los moldes
    r'alcohol (que sale por|del canal de) delivery', r'harinas panificables',
    r'plan-negocio-(tapas-bar|heladeria|pizzeria|taqueria|polleria|sushi-bar)',
]
#: Frases legítimas que se borran ANTES de buscar los prohibidos (= `gate_restos_ft.py --permitir`): la variante D del
#: Word remite al Plan de Negocio: Food Truck de AI Chef Pro.
PERMITIR = re.compile(r'Plan de Negocio: Food Truck', re.I)

#: Citas legales que son ERROR (F1-camino §4 y §7 F2 (5); nombre histórico de la familia: empezó con el art. 30):
#: «art. 30» sin «1086/2020» a menos de 160 caracteres o atribuido al RD 1021/2022; «7 días» a ±80 de congelación,
#: picada, bola o −18 °C; una temperatura «legal» u «obligatoria» (u «obligatori…») a ±80 de la cocción o de 70 °C sin
#: negación delante; «de un día para otro» sin negación delante.
RX_ART30 = re.compile(r'\bart(?:[ií]culo|\.)\s*30\b', re.I)
RX_ART30_MAL = re.compile(r'\bart(?:[ií]culo|\.)\s*30\.?\d*\s*(?:,\s*)?del (?:RD|Real Decreto) 1021/2022', re.I)
RX_7DIAS = re.compile(r'(?:\b7|siete) d[ií]as[^.;]{0,80}(?:congel|picad|bola|[−-]18)|'
                      r'(?:congel|picad|bola|[−-]18)[^.;]{0,80}(?:\b7|siete) d[ií]as', re.I)
RX_COCCION = re.compile(r'cocci[oó]n|cocinad[oa]s?\b|cocinarl[ao]s?\b|(?<!\d)70 ?°C', re.I)
RX_OBLIG = re.compile(r'temperaturas? legal(?:es)?|obligatori\w*', re.I)
RX_DIA_OTRO = re.compile(r'de un d[ií]a para otro', re.I)
RX_NEG = re.compile(r'\b(no|sin|ninguna?|ni|nunca|tampoco|jam[aá]s)\b', re.I)
RX_NEG_DIA = re.compile(r'\b(no|sin|ni|nunca|jam[aá]s|errore?s?|evita\w*)\b|prohib', re.I)


def art30_mal(texto):
    """Fragmentos con una cita legal mal: «art. 30» sin «1086/2020» cerca o atribuido al RD 1021/2022, «7 días» de
    congelación o de picada, una temperatura de cocción «legal» u «obligatoria» afirmada y «de un día para otro» sin
    negación (F1-camino §4)."""
    malos = []
    for m in RX_ART30.finditer(texto):
        ventana = texto[max(0, m.start() - 160):m.end() + 160]
        if '1086/2020' not in ventana:
            malos.append(texto[max(0, m.start() - 50):m.end() + 60])
    for m in RX_ART30_MAL.finditer(texto):
        malos.append(texto[max(0, m.start() - 30):m.end() + 30])
    for m in RX_7DIAS.finditer(texto):
        malos.append('«7 días» de congelación o de picada: ' + texto[max(0, m.start() - 30):m.end() + 30])
    for m in RX_OBLIG.finditer(texto):
        if not RX_COCCION.search(texto[max(0, m.start() - 80):m.end() + 80]):
            continue
        if not RX_NEG.search(texto[max(0, m.start() - 50):m.start()]):
            malos.append('cocción «legal» u «obligatoria» sin negación: ' + texto[max(0, m.start() - 60):m.end() + 40])
    for m in RX_DIA_OTRO.finditer(texto):
        if not RX_NEG_DIA.search(texto[max(0, m.start() - 60):m.start()]):
            malos.append('«de un día para otro» sin negación: ' + texto[max(0, m.start() - 60):m.end() + 10])
    return malos


def prohibido(texto):
    """El primer prohibido que casa en `texto` (después de borrar `PERMITIR`), o None."""
    t = PERMITIR.sub('', texto)
    for rx in PROHIBIDOS:
        m = re.search(rx, t, re.I)
        if m:
            return rx, m, t
    return None


#: Avisos (F1-camino §4): no son error, pero cada uno se revisa a mano.
AVISOS = [
    ('«−18 °C» (sólo con el art. 5 y «confírmalo con tu inspector»)', re.compile(r'[−-]18 ?°C', re.I)),
    ('carne madurada o «dry aged» (sólo como prohibición, Inf26008)', re.compile(r'madurad|dry[ -]?aged', re.I)),
    ('«al punto» o «poco hecha» (decisión del APPCC, nunca promesa)', re.compile(r'al punto|poco hech', re.I)),
    ('«sin gluten» prometido', re.compile(r'(?<!no prometer )(?<!nada de )(?<!ni )«?sin gluten»?', re.I)),
    ('«auténtic» como promesa', re.compile(r'aut[eé]ntic', re.I)),
    ('«gourmet» como promesa', re.compile(r'gourmet', re.I)),
    ('«batido» junto al 21 % (el batido de leche va al 10 %: confírmalo con tu gestoría)',
     re.compile(r'batidos?[^.;]{0,80}21 ?%|21 ?%[^.;]{0,80}batidos?', re.I)),
    ('Día de la Hamburguesa (sin fuente)', re.compile(r'd[ií]a de la hamburguesa', re.I)),
    ('registro horario «digital obligatorio»', re.compile(r'digital(es)? obligatori|obligatori\w* (en formato )?digital',
                                                          re.I)),
    ('franquicia o Goiko: sus cifras no son el caso', re.compile(r'franquici|goiko', re.I)),
    ('«180 °C» o «190 °C» (sólo como error)', re.compile(r'1[89]0 ?°C', re.I)),
    ('«pan común» (sólo para decir que el pan de hamburguesa no lo es)', re.compile(r'pan com[uú]n', re.I)),
    ('«recongelar» (sólo como prohibición)', re.compile(r'recongel', re.I)),
    ('«medidor» junto a «obligatori»', re.compile(r'medidor[^.;]{0,80}obligatori|obligatori\w*[^.;]{0,80}medidor', re.I)),
]
#: Cifras que el texto puede llevar escritas: normas y artículos, y TODAS las que traen las pistas y la jerga. El resto,
#: token o nada.
_BASE = set('''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 33 35 36 40 45 50 60 63 70
74 80 90 100 120 150 175 180 200 300 500 671 673 677.9 1.000 1.221 1/2025 7/2022 37/1992 12/2012 18/2022 31/1995 4/2021
126/2026 1175/1990 1021/2022 1086/2020 126/2015 1169/2011 828/2014 852/2004 853/2004 2017/2158 919/2006 1989 2027 2026
2025 2024 2023 2022 2021 2020 2015 2014 2012 2011 2006 2004 1995 1992 1990 82.1 91.Uno.1.1 91.Uno.2.2 91.Dos.1.1 1.1
1.13 1.15 2.2 4.1 4.2 4.3 5.3 5.4 5.5 5.6 5.8 5.9 6.3 7.2 7.3 30.2 30.3 30.6 30.7 34.9 23.ª 12/15/14/13/13/13 −18 1,7
1,6'''.split())
RX_NUM = re.compile(r'(?<![\w{])[−+]?\d[\d.,/:−-]*\d|(?<![\w{])\d')
PERMITIDAS = _BASE | set(x.rstrip('.,') for x in RX_NUM.findall(re.sub(r'\{[A-Z0-9_]+\}', '', ' '.join(
    list(PISTAS.values()) + [JERGA]))))
#: Caracteres admitidos además del latín básico/extendido: tipografía española y los signos de temperatura (−, ≤, ≥, ≈).
RX_RARO = re.compile(r'[^\x00-ɏ‐-‧€°→ ‑«»¿¡ºª·…–—“”‘’−≤≥≈²$×÷µ]')


def ranuras():
    d = json.load(open(os.path.join(BP4, 'docx_es_cat.json'), encoding='utf-8'))['parrafos']
    gem = {}
    for t in ('sus_es_a', 'sus_es_b'):
        gem.update(json.load(open(os.path.join(GEMELA, t + '.json'), encoding='utf-8')))
    fuera = []
    for k in sorted(d, key=int):
        v = d[k]
        if v['rol'] != 'cuerpo':
            continue
        sec = int(v['seccion'])
        fuera.append({'i': int(k), 'seccion': sec, 'palabras_objetivo': int(v['palabras']),
                      'molde_ft_es': v['texto'], 'gemela_formato_sushi_es': gem.get(k, '')})
    return fuera


def preparar():
    if not os.path.exists(CIFRAS):
        raise SystemExit('falta %s: corre antes cifras_ham_es.py --calc en el VPS y cópialo aquí' % CIFRAS)
    cif = json.load(open(CIFRAS, encoding='utf-8'))['tokens']
    usados = set(re.findall(r'\{([A-Z0-9_]+)\}', ' '.join(PISTAS.values())))
    sin = sorted(usados - set(cif))
    if sin:
        raise SystemExit('las PISTAS citan tokens que no están en cifras_caso_es.json: %s (¿falta --calc?)' % sin)
    for s, p in PISTAS.items():                   # las pistas también cumplen las reglas legales y los prohibidos
        assert not art30_mal(p), (s, art30_mal(p))
        pr = prohibido(p)
        assert pr is None, (s, pr[0], pr[2][max(0, pr[1].start() - 40):pr[1].end() + 40])
    os.makedirs(TANDAS, exist_ok=True)
    rs = ranuras()
    for tanda, secs in (('ham_es_a', range(1, 6)), ('ham_es_b', range(6, 11))):
        sel = [r for r in rs if r['seccion'] in secs]
        ent = {
            'tanda': tanda, 'producto': 'Plan de Negocio: Hamburguesería Smash ES 1.0 (aichef.pro, 35 €)',
            'salida': 'scripts/productos-digitales/plan-hamburgueseria/textos/%s.json' % tanda,
            'formato_salida': '{"<i>": "<párrafo en español>", …} con TODOS los "i" de "parrafos" y nada más',
            'brief': 'scripts/productos-digitales/plan-hamburgueseria/BRIEF-REDACTORES.md (léelo entero antes)',
            'research': RESEARCH + ' (§0 hallazgos, §1 normativa con citas literales, §2 precios y escandallos, §3 caso, '
                                   '§4 SERP y hueco, §5 jerga, §6 errores y FAQ: material de apoyo; la pista de la '
                                   'sección manda)',
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
        print('ERROR falta --tanda (ham_es_a o ham_es_b)')
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
        tp = PERMITIR.sub('', t)
        for rx in PROHIBIDOS:
            if re.search(rx, tp, re.I):
                err.append('%d: prohibido /%s/' % (r['i'], rx))
        for frag in art30_mal(t):
            err.append('%d: cita legal mal (art. 30 sin el RD 1086/2020, «7 días», cocción «legal» u «obligatoria» o «de '
                       'un día para otro» sin negación): …%s…' % (r['i'], frag))
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
