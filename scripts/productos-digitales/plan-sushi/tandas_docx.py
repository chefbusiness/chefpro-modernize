#!/usr/bin/env python3
"""
tandas_docx.py — Plan de Negocio: Sushi Bar ES 1.0 (F1-camino §4): prepara y valida las dos tandas de redacción del
plan de negocio (docx). Copia adaptada de `plan-polleria/tandas_docx.py`.

Las 61 ranuras de texto del docx del Food Truck ES (131 párrafos, 10 Heading 1; mapa en
`business-plans-en-4/docx_es_cat.json`) se escriben NUEVAS, en español, para el sushi bar:
  sus_es_a = §1-5 (29 ranuras) · sus_es_b = §6-10 (32 ranuras).
Gemela de FORMATO: el texto de la Taquería ES 1.0 en la misma ranura (`plan-taqueria/textos/taq_es_{a,b}.json`, la misma
rejilla: comensal y rotación encendida, ya revisada): sirve para ver cómo se escribe una ranura con tokens, nunca su
contenido. No hay versión anterior: el material es el research (`F1-research-sushi.md`) y las pistas de abajo. Las cifras
del Excel (y de la calculadora del pescado, el arroz y el escandallo) van SIEMPRE como token {ASI}
(`cifras_caso_es.json`, con `--calc`); `docx_sus_es.py` las resuelve al ensamblar. Sólo lee JSON: corre en el Mac.

    python3 tandas_docx.py preparar                       # tandas/sus_es_{a,b}.entrada.json
    python3 tandas_docx.py check --tanda sus_es_a         # valida textos/sus_es_a.json (salida del redactor)

Sesión Claude Code, 31-oct-2026.
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
RESEARCH = 'scripts/productos-digitales/plan-sushi/F1-research-sushi.md'

SECCIONES = {
    1: '1. Resumen Ejecutivo', 2: '2. Concepto y Propuesta de Valor', 3: '3. Análisis de Mercado',
    4: '4. Análisis Competitivo', 5: '5. Plan de Marketing y Captación', 6: '6. Plan de Operaciones',
    7: '7. Estructura Organizativa y RRHH', 8: '8. Plan Financiero', 9: '9. Aspectos Legales y Licencias',
    10: '10. Conclusiones y Plan de Acción',
}

#: La jerga del oficio (R §5): se glosa la PRIMERA vez que sale en el Word; y lo que no se dice.
JERGA = ('itamae (el jefe de barra: compra, limpia y corta el pescado y firma la carta) · sushiman o sushiwoman (quien '
         'monta las piezas en la barra; en México, Colombia y Argentina es el término del oficio) · neta (lo que va '
         'sobre el arroz: el pescado o el marisco cortado) · shari (el arroz de sushi ya aliñado) · sushi-zu (el aliño '
         'de vinagre de arroz, azúcar y sal) · saku (el bloque limpio de pescado listo para cortar) · hangiri (la tina '
         'de madera donde se aliña y se enfría el shari) · nigiri (bola de shari con una loncha de neta encima) · '
         'sashimi (el pescado cortado, sin arroz) · hosomaki (rollo fino con el alga por fuera) · uramaki (rollo con el '
         'arroz por fuera) · temaki (cono de alga) · combinado (la bandeja de piezas variadas, la que más sale para '
         'llevar) · poke (bol de arroz con pescado crudo marinado y verduras) · vitrina de neta (la vitrina refrigerada '
         'de la barra) · omakase (menú que decide el itamae, en barra y con reserva) · kaiten (la cinta giratoria). '
         'QUÉ NO DECIR: «sushi grade» o «sashimi grade» como garantía (no es una categoría legal: di «pescado apto para '
         'consumo en crudo, congelado o con su documento»); «auténtico» como promesa o sello; el RD 1420/2006 (está '
         'derogado: la norma del anisakis es el RD 1021/2022, art. 8); los días de congelación de Estados Unidos (en '
         'España, −20 °C 24 horas o −35 °C 15 horas); «−18 °C» como temperatura del anisakis (es la del congelado '
         'general); un pH o un tiempo «legal» para el arroz (no existe en España); marcas de cadenas como modelo del '
         'caso; «sin gluten» como promesa')

#: Lo que tiene que contar cada sección (español de España, para el mercado español; R §0-§7). Cifras del Excel y de
#: la calculadora = tokens.
PISTAS = {
    1: 'Qué es el negocio: un sushi bar de barrio con una barra de sushi a la vista de 8 taburetes y su vitrina de neta, '
       'una sala de 28 plazas en mesa ({AFORO} plazas en total) y una zona de empaquetado de pedidos junto a la puerta, en '
       'un local de unos 95 m² que ya fue de restauración, con salida de humos a cubierta posible y cocina eléctrica, sin '
       'traspaso, en un barrio con vida de noche de una ciudad de 150.000 a 500.000 habitantes (o en un barrio de Madrid, '
       'Barcelona o Valencia). Una SL unipersonal con el titular de itamae y gerente, un sushiman, un cocinero de cocina '
       'caliente y arroz, un encargado de sala y pedidos, un camarero de cenas y un refuerzo de viernes a domingo. Carta '
       'corta de unas 35 referencias, con IVA: el nigiri de salmón a 5,20 € las dos piezas, el uramaki California a '
       '9,60 € los ocho, el sashimi de salmón a 7,50 €, el poke de salmón a 12,90 €, el combinado de 24 piezas a 29,00 € y '
       'las gyozas a 7,00 €, más un menú del día de mediodía de martes a viernes a 14,90 €. Tres canales: la sala (unos '
       '63 % de las ventas), los pedidos para recoger (unos 13 %) y la plataforma con su reparto ({DELIVERY_PCT}, con '
       'techo y sin reparto propio). Abre en ENERO (el Mes 1 del Excel es enero, en el orden del calendario), de martes a '
       'domingo de 13:00 a 16:00 y de 20:00 a 23:30; cierra los lunes y 10 días en agosto. Cifras clave por token: '
       '{COMENSALES_DIA} comensales equivalentes al día (unos {COMENSALES_SALA} en sala y el resto, los pedidos para '
       'llevar y a domicilio, contando cada pedido como 1,6 comensales) a {TICKET} por comensal sin IVA y '
       '{DIAS_APERTURA} días; ventas {VENTAS_A1}, resultado neto {NETO_A1} ({NETO_PCT_A1}), inversión {INVERSION_TOTAL} '
       '(de la que {INVERSION_PARTIDAS} son obra, barra, frío, equipo y puesta en marcha), préstamo {PRESTAMO} y '
       'equilibrio de caja en {BE_COMENSALES_DIA_CAJA} comensales al día. Qué contiene el kit: este plan de negocio de 10 '
       'secciones, el Excel del plan financiero de 9 hojas, el checklist de apertura de 80 tareas en 6 fases, la '
       'calculadora del pescado, el arroz y el escandallo (el coste por kilo útil del salmón entero, del lomo comprado '
       'limpio y del atún; el shari y los nigiris que salen de un kilo de arroz; el escandallo de 14 productos con su '
       'margen en sala, para llevar y en plataforma) y la guía de equivalencias para Latinoamérica (el marco legal del '
       'plan es el español). Lo que lo distingue, en una frase: el pescado y el arroz con números ({NIGIRIS_KG_ARROZ} '
       'nigiris por kilo de arroz crudo y el kilo útil de salmón entero a {COSTE_KG_UTIL_SALMON}, estimaciones del kit que '
       'mides tú) y la norma del pescado crudo y del arroz contada bien: el anisakis con el art. 8 del RD 1021/2022 y el '
       'shari con el art. 30.5 del RD 1086/2020.',
    2: 'Tipos de sushi bar y por qué este (R §3, sin cifras de Excel para los otros): el de sólo para llevar y a domicilio '
       '(40-60 m², con 0-6 plazas o ninguna; la franquicia de quiosco más barata pide 39.950 € más la obra en 38 m², según '
       'emprendedores.es; si los pedidos son la actividad principal, el IAE es el 677.9); el sushi bar de barrio con barra '
       'y mesas, para llevar y a domicilio (el de este plan); la barra omakase de 10-12 plazas con reserva (un ticket de '
       '80-150 € según la Guía Restaurante Japonés de AI Chef Pro: otro negocio, otra carta y otro pescado); el kaiten o el '
       'buffet libre (150-250 m² y 80-120 plazas a precio cerrado, de menos de 20 € a 28,50 € en Valencia según el día: '
       'volumen y merma propios); la cocina nikkei (la remite a la Guía Restaurante Nikkei de AI Chef Pro) y el japonés '
       'completo con ramen, izakaya o robata (la Guía Restaurante Japonés). GLOSA LA JERGA la primera vez (ver `jerga` de '
       'la entrada): itamae, sushiman, neta, shari, sushi-zu, saku, hangiri, nigiri, sashimi, hosomaki, uramaki, temaki, '
       'combinado, omakase, kaiten. El ticket de {TICKET} es por comensal equivalente y sin IVA ({TICKET_IVA} con IVA) y '
       'sale de tres canales: el comensal de sala deja unos 22,26 € sin IVA (el menú del día de 14,90 € con IVA es un 30 % '
       'de la sala; la cena o el fin de semana, unos 28,60 € con IVA con la bebida); el pedido para recoger (un combinado '
       'de 24 piezas y un extra, unos 27,00 € con IVA) sale a unos 15,34 € por comensal equivalente; y el de plataforma, '
       'con el precio un 15 % más alto, a unos 18,47 €. Mezcla de ventas: comida {PCT_COMIDA} y bebida {PCT_BEBIDA} (en '
       'sala, la bebida es un 22 % de lo que se vende; fuera, un 4 %). La propuesta: el itamae a la vista en la barra, '
       'pescado con su documento o congelado como manda la norma, shari medido y aliñado en el día, una carta corta que '
       'no llena la vitrina de neta que se tira, combinados que viajan bien y un menú del día que llena la sala a mediodía.',
    3: 'Mercado en España con fuente. El maki es el segundo plato más pedido a domicilio en España, sólo por detrás de la '
       'hamburguesa (Gastrómetro de Just Eat 2025, publicado en prensa en diciembre de 2025): por eso el plan cuenta con la '
       'plataforma. Búsquedas mensuales en Google España (DataForSEO, 31 de octubre de 2026): «sushi» 301.000, «poke» '
       '74.000, «uramaki» 33.100, «nigiri» 27.100, «restaurante japonés» 22.200, «sushi bar» 8.100, «omakase» 8.100, '
       '«arroz para sushi» 4.400, «sushi a domicilio» 1.900 y «restaurante de sushi» 1.900; y quien va a abrir busca poco: '
       '«franquicia sushi» 90 y «plan de negocio sushi» o «negocio de sushi», 10. En México, «sushi» 368.000 y «negocio de '
       'sushi» 70. El consumidor busca muchísimo; el que va a abrir decide con datos. Precio en carta, con IVA (cartas '
       'leídas en octubre de 2026, sin nombres): una cadena de sushi de León vende el nigiri a 2,60 € la pieza y los '
       'combinados de 24 piezas de 24,90 a 30,60 €; un restaurante de Valencia, el nigiri a 2,50 € la pieza; un menú del '
       'día de sushi ronda los 13,95 €; el buffet libre de Valencia va de menos de 20 € entre semana a 28,50 € el fin de '
       'semana. El caso pone el nigiri de salmón a 2,60 € la pieza y el combinado de 24 a 29,00 €. NO hay una cifra fiable '
       'del número de restaurantes japoneses en España: no la des. ESTACIONALIDAD del plan, con el Mes 1 en ENERO y en el '
       'orden del calendario: diciembre es el pico (un 9,2 % del año, con las bandejas de Nochebuena y Nochevieja), '
       'febrero sube con San Valentín (un 8,6 %) y agosto es el valle (un 6,6 %, con el cierre de 10 días y la ciudad '
       'vacía); entre el mejor mes y el peor hay un 39 %. En la costa, agosto sube: gira la fila de la Tesorería. El hueco: '
       'la SERP da páginas de modelos con inversiones sin fuente («50.000-160.000 €», «230.000-790.000 $»), franquicias, '
       'vídeos y foros; nadie cuenta el coste de cada pieza, ni el art. 8.2 del anisakis (informar al cliente), ni que el '
       'shari a temperatura ambiente sólo cabe por el art. 30.5 del RD 1086/2020. NADA de tamaños de mercado sin fuente.',
    4: 'Competencia por categorías, sin nombres salvo las franquicias con sus cifras publicadas: los japoneses de barrio '
       'con carta larga y buffet; las cadenas y franquicias de sushi (según emprendedores.es: Sibuya, unos 300.000 € de '
       'inversión, 180 m², canon de 30.000 € y un 4 % más un 1 % de royalty y publicidad; Miss Sushi, desde 200.000 € en '
       '120 m², canon de 29.000 €; Sushimore, 39.950 € más la obra en 38 m²); el sushi de supermercado y de las tiendas de '
       'comida para llevar; las dark kitchens de sushi que sólo venden por plataforma; y el poke, que compite por el mismo '
       'cliente de mediodía. FRANQUICIA FRENTE A MARCA PROPIA, razonado: la franquicia trae marca, proveedores, formación y '
       'carta a cambio del canon, la cuota y un local que suele ser más grande que el de este plan; con marca propia, la '
       'inversión es {INVERSION_TOTAL} y te quedas el margen, pero necesitas al itamae. Las cifras de franquicia (180 m², '
       '300.000 €) NO sirven para un local de 95 m²: compara las dos cuentas antes de firmar. Dónde gana este concepto: el '
       'itamae a la vista, el pescado limpio en casa (el kilo útil del salmón entero sale a {COSTE_KG_UTIL_SALMON} frente '
       'a {COSTE_KG_UTIL_LOMO} el del lomo comprado limpio, con los valores del kit), una carta corta, combinados con su '
       'escandallo por canal y el menú del día. Los riesgos: el precio del salmón, la plataforma (en ella el margen del '
       'combinado de 24 cae de {MARGEN_SALA_COMB24} en sala a {MARGEN_PLATAFORMA_COMB24}), un solo proveedor de pescado y '
       'el itamae único; cómo se defiende (dos proveedores, escandallo por canal, recogida en el local, carta corta y un '
       'segundo que corte).',
    5: 'Marketing y captación: apertura en enero (los curiosos llegan el primer mes; la clientela fija y la nota en las '
       'plataformas tardan un trimestre); ficha de Google Business con el horario, fotos reales de la barra y de las piezas '
       'y respuesta a cada reseña; redes con el itamae cortando y el combinado saliendo; el menú del día de mediodía para '
       'las oficinas y los vecinos; el calendario: San Valentín (febrero), las bandejas de Nochebuena y Nochevieja por '
       'encargo (diciembre, el pico del año) y la vuelta de septiembre; fidelización sencilla (pedido propio por teléfono, '
       'WhatsApp o web para recoger) sin cifras de conversión inventadas. PLATAFORMA FRENTE A RECOGIDA (sin Excel, '
       'razonado): el plan vende por plataforma con su reparto un {DELIVERY_PCT} de las ventas ({VENTAS_PLATAFORMA_A1} al '
       'año) y paga una comisión del {COMISION_DELIVERY} ({COMISIONES_DELIVERY_A1} al año); las guías del sector sitúan el '
       'plan básico de Uber Eats en torno al 30 % más IVA, Glovo entre el 15 y el 35 % según la zona y Just Eat entre el '
       '13 y el 35 %, más las promociones y la caja. El combinado viaja bien; la tempura y las gyozas llegan blandas: en la '
       'plataforma, fuera o con envase ventilado. Pasar 10 puntos de las ventas de la plataforma a la recogida en el local '
       'ahorra unos 14.000 € de comisión al año (menos lo que dejes de cobrar por el precio más alto de la plataforma): la '
       'recogida no paga comisión, empújala con precio. Un repartidor propio sólo con contrato laboral y cuando el volumen '
       'lo pague. Presupuesto de marketing {MARKETING_ANO} al año, más la marca, la web, las fotos y el lanzamiento, que '
       'van en la inversión ({MARCA_LANZAMIENTO}).',
    6: 'Operaciones de la barra, el frío y la cocina. EL PESCADO CON NÚMEROS (la calculadora del pack, valores por defecto '
       'que son estimación del kit y editables): el salmón entero de acuicultura a 9,50 € el kilo sin IVA, con un 55 % de '
       'lomo limpio y un 15 % de recorte que se reaprovecha en tartar, maki y poke, y un 5 % de merma de vitrina, sale a '
       '{COSTE_KG_UTIL_SALMON} el kilo útil; el lomo de salmón comprado limpio (21,80 € el kilo), a {COSTE_KG_UTIL_LOMO}; '
       'el atún aleta amarilla en saku ultracongelado (26,00 € el kilo), a {COSTE_KG_UTIL_ATUN}. Los blogs de gestión dan '
       'un 50-60 % de lomo limpio del salmón entero, sin fuente técnica: limpia y pesa 3 salmones y lleva tu rendimiento a '
       'la hoja «Pescado», que te dice hasta qué coste de limpieza te compensa comprarlo entero. EL ARROZ CON NÚMEROS: un '
       'kilo de arroz crudo da {KG_SHARI_KG_ARROZ} kilos de shari (× 2,2 al cocerlo y un 10 % de sushi-zu) y unos '
       '{NIGIRIS_KG_ARROZ} nigiris con 20 g de shari; con unos 150 g de shari por comensal, el caso cuece unos '
       '{ARROZ_DIA_KG} kilos de arroz crudo al día. El arroz es barato (de 1,81 a 1,85 € el kilo sin IVA en sacos de 5 kg '
       'de mayorista): el coste está en el pescado y en la mano del itamae. Pesa 10 lonchas y 10 bolas de shari de cada '
       'persona de la barra: la neta y el shari que pesan de más son food cost que no sale en el escandallo. EL '
       'ESCANDALLO: el nigiri de salmón sale a un {FC_NIGIRI_SALMON} de su precio SIN IVA (4,73 € sin IVA, 5,20 € con IVA) '
       'y el combinado de 24 piezas a un {FC_COMBINADO_24}; la semana ponderada del kit, a un {FC_PONDERADO}. EQUIPO con '
       'precio y fuente: vitrina refrigerada de sushi {VITRINA} (una de 6 cubetas GN 1/3 ronda los 999 € sin IVA y la de '
       'barra de gama alta pasa de 4.500 €), arroceras, mantenedor y hangiri {ARROCERAS} (la arrocera de 8 litros ronda '
       'los 484 € sin IVA), armario congelador de −20 °C con registrador y arcón {CONGELADOR}, cocina caliente de '
       'inducción, freidora de tempura y plancha de gyozas {COCINA_CALIENTE}, campana extractora {CAMPANA}, frío '
       '{FRIO} (el armario de pescado a 0-2 °C) y el conducto exclusivo a cubierta {CONDUCTO}. Horario: de martes a domingo '
       'de 13:00 a 16:00 y de 20:00 a 23:30; la producción (el shari del día, el corte y la limpieza del pescado, las '
       'salsas) se hace antes de abrir. HIGIENE EN LA OPERACIÓN: el recorrido del pescado es recepción, frío, limpieza '
       'en su zona, corte en la barra; pescado fresco entre 0 y 4 °C en la cámara y en la vitrina (RD 1021/2022, art. '
       '4.1); descongelación en cámara; el punto de control crítico del anisakis con su registro por lote; el pH del shari '
       'en cada tanda con un pH-metro calibrado (el Kit de Tareas Sushi Bar de AI Chef Pro trae la hoja); tablas por '
       'colores y cuchillos separados para el crudo; la temperatura de cada entrega y cuidado con el atún (la histamina no '
       'se va ni con la congelación ni con la cocción). PROVEEDORES: dos de pescado con su documentación (congelación o '
       'acuicultura) y uno de arroz para sushi, nori y salsas con su ficha técnica; las temporadas cambian el precio (el '
       'bonito del norte de junio a octubre, el atún rojo de almadraba de abril a junio). Suministros {SUMINISTROS_MES} al '
       'mes de media (la cocina es eléctrica y el frío trabaja todo el día); mantenimiento {MANTENIMIENTO_FRIO} al año (el '
       'frigorista, el congelador que tiene que seguir llegando a −20 °C, la campana extractora y la calibración del '
       'pH-metro).',
    7: 'Equipo (7 filas en la hoja Personal): el titular, itamae y gerente (compra, limpia y corta el pescado, lleva la '
       'barra en el servicio fuerte, firma la carta y el APPCC del anisakis y gestiona; {SUELDO_TITULAR} brutos al mes en '
       '14 pagas; como administrador de la SL cotiza en el régimen de autónomos: confírmalo con tu gestoría); un '
       'sushiman o sushiwoman (el shari, los rolls y los combinados de la plataforma, y la barra cuando el itamae no está: '
       'el itamae único es un riesgo, no un ahorro, porque si falta no abre la barra); un cocinero de cocina caliente y '
       'arroz (las arroceras, las gyozas, la tempura, la sopa de miso y el office); un encargado de sala y pedidos (caja, '
       'pedidos para recoger, las tablets de las plataformas y la información de alérgenos); un camarero de cenas y fines '
       'de semana de 30 horas; un refuerzo de viernes a domingo para la sala y el empaquetado (sin reparto propio); y las '
       'suplencias de vacaciones y descansos: {PLANTILLA_PERSONAS} personas y {JORNADAS} jornadas completas equivalentes, '
       'coste {PERSONAL_A1} ({PERSONAL_PCT_A1} de las ventas), cobertura de horas {COBERTURA_HORAS} '
       '({HORAS_CONTRATADAS} horas contratadas frente a {HORAS_NECESARIAS} necesarias); el viernes y el sábado por la '
       'noche hacen falta seis personas (dos en la barra, una en caliente, dos en sala y una empaquetando) y el cuadrante '
       'anual no lo ve: ponlo en el turno. El itamae es la contratación difícil: las ofertas de sushiman de los portales de '
       'empleo van de 12.000 a 22.000 € brutos al año (muchas, a media jornada) y las de un omakase de Ibiza pasan de '
       '2.500 € al mes; contrátalo ANTES de la obra y que opine sobre la barra y el frío. La plantilla crece con personas: '
       '{INCORPORACIONES_A2} de incorporaciones el año 2 y otro tanto el año 3. Convenio provincial de hostelería: el art. '
       '4 del VI Acuerdo Laboral de ámbito Estatal para el sector de Hostelería no nombra el sushi bar, pero incluye los '
       'restaurantes y el reparto de comidas preparadas; todos por encima del SMI de 2026 (1.221 € al mes en 14 pagas, '
       'Real Decreto 126/2026) en proporción a la jornada; contratos por escrito; registro de jornada obligatorio (art. '
       '34.9 del Estatuto de los Trabajadores; NO digas que la ley lo exige «digital»); nunca autónomos que te facturan con '
       'tu horario (falso autónomo, art. 1.1). Repartidor propio, si algún día lo pones: contrato laboral del convenio de '
       'hostelería; en el reparto que organiza una plataforma por algoritmo, la ley presume la relación laboral '
       '(disposición adicional 23.ª del Estatuto). Formación de manipuladores acreditada por la empresa (el antiguo carné '
       'de manipulador ya no existe) con el pescado crudo: congelación del anisakis, temperaturas de la vitrina, pH del '
       'shari, alérgenos y contacto cruzado; formación de la barra (corte, gramos de neta y de shari); prevención de '
       'riesgos (cortes con los cuchillos de la barra, quemaduras de la freidora y la plancha, el frío del congelador y '
       'las cargas).',
    8: 'Plan financiero, TODO por token: inversión {INVERSION_TOTAL} = compras {CAPEX} (obra, barra, frío, equipo y '
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
       'escandallo teórico de la calculadora sale en un {FC_PONDERADO} de media (el nigiri de salmón, en un '
       '{FC_NIGIRI_SALMON}, siempre sobre el precio SIN IVA), pero la cuenta real es lo que compras frente a lo que vendes: '
       'se pierden la merma del pescado que no se vende en la vitrina y del recorte que no se reaprovecha, la neta y el '
       'shari que pesan más que en el escandallo, el shari, el nori y las salsas que se tiran al cierre, las comidas del '
       'personal, las invitaciones y los errores de pedido y el menú del día, que deja poco margen; y el pescado es un '
       'precio estimado por el kit (Makro y Mercamadrid no publican el precio profesional del salmón fresco). Un japonés con '
       'pescado de calidad trabaja con un 30-35 % (Guía Restaurante Japonés). Cada punto de food cost de la comida mueve '
       'unos {PUNTO_FOOD_COST_A1} al año; si el salmón sube un 20 % (es más o menos un 35 % de la compra de comida), el '
       'resultado baja unos 8.200 €. Mide tu consumo real (compras de comida ÷ ventas de comida del mes) el primer '
       'trimestre y cambia la celda. La palanca, si los números no salen, es el precio de la carta, nunca más deuda. '
       'CRECIMIENTO tal cual lo hace el Excel: suben los comensales un {CREC_A2} y un {CREC_A3} (de {COMENSALES_DIA} a '
       '{COMENSALES_DIA_A2} y {COMENSALES_DIA_A3} al día) con el mismo ticket, y la plantilla crece con personas '
       '({INCORPORACIONES_A2} al año), no con un porcentaje. IVA: la comida al 10 % (en sala, para llevar y a domicilio); '
       'de la bebida, la parte que sale del local con alcohol o con azúcares o edulcorantes añadidos (la cerveza, el sake, '
       'el vino y los refrescos azucarados o edulcorados: {BEBIDA_21_PCT} de la bebida, la columna H de su línea, un 1,05 % '
       'de las ventas) va al 21 % y el resto al 10 %: el IVA medio de la bebida es {IVA_BEBIDA_LINEA}. En las compras, el '
       'IVA soportado de la comida es {IVA_COMPRA_COMIDA} (el arroz, la verdura, el aguacate, el huevo y el queso se '
       'compran al 4 %) y el de la bebida {IVA_COMPRA_BEBIDA}. Equilibrio contable {BE_COMENSALES_DIA} comensales al día '
       '(ingresos {BE_INGRESOS}; holgura {HOLGURA_CONTABLE}); equilibrio de caja {BE_COMENSALES_DIA_CAJA} comensales al '
       'día y holgura {HOLGURA_CAJA}, que es la del PRIMER año (sólo intereses por la carencia); desde el segundo, con la '
       'devolución del principal, la holgura baja a {HOLGURA_CAJA_A2} ({BE_COMENSALES_DIA_CAJA_A2} comensales al día de '
       'equilibrio) y en el tercero queda en {HOLGURA_CAJA_A3} ({BE_COMENSALES_DIA_CAJA_A3}): esos años son los que hay que '
       'vigilar. ROTACIÓN: el caso pide {ROTACION_IMPLICITA} comensales por plaza y día con los pedidos dentro, frente a '
       'un techo físico de {ROT_MAX} (comida, cena y un segundo turno el viernes y el sábado); el equilibrio de caja pide '
       '{ROT_BE_CAJA}; la rotación real de la sala, sin los pedidos, ronda {ROT_SALA}. DSCR mínimo {DSCR_MIN}. TESORERÍA: '
       'el Mes 1 es ENERO, en el orden del calendario; la rampa arranca al {RAMPA_MES1} y llega al ritmo de crucero en '
       '{MESES_RAMPA} meses (abril); el saldo mínimo es {SALDO_MINIMO} en el mes {MES_SALDO_MINIMO} '
       '({MES_SALDO_MINIMO_NOMBRE}) y el año acaba (diciembre, el pico) con {SALDO_MES12}; agosto, el valle, se nota en la '
       'caja; las pagas extra salen en julio (Mes 7) y diciembre (Mes 12); el IVA se liquida por trimestres naturales '
       '(abril, julio, octubre y, el del cuarto trimestre, en enero del año siguiente). PAYBACK antes de la deuda: el '
       'token puede ser una cifra sin unidad o el texto «Más de 3 años» (hoy es una cifra): escribe una frase que lea bien '
       'con los dos («El payback antes de la deuda, en años, …: «{PAYBACK}» con el fondo de maniobra dentro y '
       '«{PAYBACK_CAPEX}» sin él»), nunca «años» detrás del token. Escenarios: pesimista ({ESC_PES_COMENSALES} '
       'comensales a {ESC_PES_TICKET} y {ESC_PES_DIAS} días: ventas {ESC_PES_VENTAS}, neto {ESC_PES_NETO}) y optimista '
       '({ESC_OPT_COMENSALES} comensales a {ESC_OPT_TICKET} y {ESC_OPT_DIAS} días: ventas {ESC_OPT_VENTAS}, neto '
       '{ESC_OPT_NETO}). El Excel manda: si cambias una celda verde, el documento se queda atrás.',
    9: 'Marco legal con su cita (sólo esto, dicho así; lo marcado «compruébalo», dilo así y sin cifra): SL unipersonal '
       '(capital desde 1 €, Ley 18/2022) o autónomo. IAE (RDLeg 1175/1990): con comedor y servicio de mesa, el grupo 671 '
       '(restaurantes, por categoría); de barra sin comedor separado, el 673; la nota común de esos grupos faculta para '
       'vender para llevar; si los pedidos fueran la actividad principal (sólo para llevar y a domicilio), el 677.9: la '
       'gestoría decide. Alta censal con el modelo 036; exento de cuota con menos de 1 millón de cifra de negocio (art. '
       '82.1.c de la Ley de Haciendas Locales). Apertura: los restaurantes no están en el anexo de la Ley 12/2012: '
       'licencia o declaración responsable según la ordenanza de tu ayuntamiento, con una consulta urbanística previa '
       '(uso, extracción a cubierta para la freidora y la plancha, potencia eléctrica, aforo). Humos: lo decide la '
       'ordenanza de cada ayuntamiento; ejemplo leído, Madrid (Ordenanza 4/2021 de Calidad del Aire): conducto exclusivo '
       'a cubierta que supere en 1 m la altura de lo que haya en 15 m (art. 12 y anexo I) y limpieza al menos una vez al '
       'año (art. 23); en tu ciudad, pide la ordenanza (sin cifras de otras). Sanidad: declaración responsable al '
       'registro sanitario de tu comunidad autónoma (RD 1021/2022); el RGSEAA sólo aplica si suministras a otros negocios '
       'por encima de lo que permite su art. 3. ANISAKIS, leído en el BOE: el RD 1420/2006 está DEROGADO desde el 22 de '
       'diciembre de 2022 (nunca lo cites como vigente); la norma es el art. 8 del RD 1021/2022: el pescado que se va a '
       'consumir crudo o casi crudo se congela a −20 °C o menos en la totalidad del producto durante al menos 24 horas, o a '
       '−35 °C o menos durante al menos 15 horas, en tu local o en una etapa anterior con su documento (8.1); la '
       'acuicultura queda exenta sólo si el proveedor acredita por escrito que está libre de parásitos (Reglamento (CE) '
       '853/2004, anexo III, sección VIII, capítulo III, parte D); y hay que «informar a las personas consumidoras de que '
       'dichos productos han sido congelados o, en su caso, que proceden de sistemas de acuicultura que garantizan que '
       'están libres de anisakis, mediante… carteles o cartas-menú» (8.2). En la Unión Europea el atún salvaje NO está '
       'exento. El congelador del anisakis tiene que llegar a −20 °C en el centro del pescado: uno que sólo marca −18 °C no '
       'sirve. TEMPERATURAS: el pescado fresco, entre 0 y 4 °C (art. 4.1 del RD 1021/2022); lo que no está en esa tabla, a '
       'la temperatura de su etiqueta (4.2); el transporte de lo que sale, en medios que mantengan la temperatura (4.3). '
       'EL SHARI: las comidas preparadas siguen el art. 30 del RD 1086/2020, en la redacción que le dio el RD 1021/2022 '
       '(nunca lo atribuyas al RD 1021/2022 a secas): «se servirán para su consumo cuanto antes, a menos que se refrigeren, '
       'congelen o se mantengan a una temperatura superior o igual a 63 °C» (30.2); refrigeradas, a 4 °C o menos si su '
       'vida útil pasa de 24 horas y a 8 °C o menos si es menor (30.3); y el 30.5 deja al operador «establecer '
       'temperaturas de conservación diferentes… siempre que demuestre a la autoridad competente que estas temperaturas '
       'están basadas en evidencias científicas». Esa es la ÚNICA vía del shari a temperatura ambiente: tu APPCC lo '
       'justifica (pH de cada tanda y un tiempo máximo) y lo demuestras a sanidad; si no, refrigerado. Ninguna norma '
       'española fija un pH ni un tiempo para el arroz de sushi: el pH de 4,6 o menos es el límite crítico del APPCC del '
       'Kit de Tareas Sushi Bar (criterio del Codex), no una cifra legal; apuntar a 4,2-4,3 da margen. La cocina caliente '
       '(gyozas, tempura, miso): caliente a 63 °C o más, enfriado de 60 a 10 °C en menos de 2 horas (30.6 del RD '
       '1086/2020) y recalentado a 74 °C durante 15 segundos en el centro (30.7). ETIQUETA: lo que se vende sin envasar o '
       'se envasa a petición del cliente informa de la denominación y los alérgenos (RD 126/2015, art. 4); las bandejas '
       'de combinado que preparas ANTES del pedido para la vitrina o para recoger son envasado para la venta inmediata y '
       'llevan las menciones de los arts. 9 y 10 del Reglamento (UE) 1169/2011 salvo la nutricional: ingredientes, '
       'alérgenos resaltados, peso, fecha y conservación (art. 5). Alérgenos: por escrito o de palabra si la información '
       'se registra por escrito o en formato electrónico en el local y es accesible (RD 126/2015, arts. 4.1.b y 6.5.a), y '
       'en la venta a distancia, disponible antes de comprar (Reglamento (UE) 1169/2011, art. 14); en el sushi no caben '
       'en «pescado y soja»: pescado, crustáceos (langostino, ebi), moluscos (pulpo, vieira), soja y el trigo de la salsa '
       'de soja, sésamo, huevo (tamago, mayonesa japonesa), leche (queso crema), el gluten de la tempura, el panko y el '
       'surimi, la mostaza de algunas pastas de wasabi (la AESAN alertó en 2020 de mostaza no declarada en unos snacks de '
       'wasabi: lee cada etiqueta) y los sulfitos del vino. «Sin gluten» sólo con 20 mg/kg o menos tal como se vende '
       '(Reglamento de Ejecución (UE) 828/2014): con salsa de soja de trigo, tempura y freidora compartida, no se promete. '
       'IVA (Ley 37/1992, art. 91): en sala, todo al 10 % (91.Uno.2.2.º); para llevar y a domicilio, la comida al 10 %, '
       'pero se excluyen del reducido las bebidas alcohólicas y las bebidas refrescantes, zumos y gaseosas con azúcares o '
       'edulcorantes añadidos (91.Uno.1.1.º a y b): la cerveza, el sake, el vino y los refrescos azucarados o edulcorados '
       'que salen del local van al 21 %; en las compras, el arroz, la verdura, el huevo y el queso van al 4 % (91.Dos.1.1.º '
       'd, e y f). Alcohol para llevar o a domicilio: horarios y limitaciones de cada comunidad autónoma y nunca a '
       'menores: consulta la normativa de la tuya (sin cifras). Ley 1/2025, art. 8: el cliente puede llevarse lo que no '
       'consuma sin coste y el local lo avisa de forma visible, mejor en la carta. Ley 7/2022, art. 55: el envase de '
       'plástico de un solo uso para llevar se cobra aparte en el tique; pregunta a tu proveedor cuáles de tus cajas de '
       'sushi lo son. Aceite de la freidora: gestor autorizado. Personal: convenio provincial de hostelería (ALEH VI, '
       'art. 4), SMI de 2026 (RD 126/2026), Estatuto de los Trabajadores (arts. 1.1 y 34.9 y disposición adicional 23.ª), '
       'Ley 31/1995 de prevención. Facturación con software Veri*factu (consulta con tu gestoría la fecha que te aplica). '
       'El marco legal del plan es el ESPAÑOL: en México y el resto de Latinoamérica los trámites (fiscales, municipales '
       'y sanitarios) y la norma del pescado crudo son otros y este plan no los cubre; la guía de equivalencias del pack '
       'adapta los términos. Lo que no esté aquí no se afirma: «compruébalo con tu gestoría, tu ayuntamiento o el '
       'inspector».',
    10: 'Conclusiones con tokens (viabilidad, holgura de caja del año 1 y de los años 2 y 3, DSCR mínimo, saldo mínimo, '
        'payback leído como en el §8) y los 13 errores de un sushi bar y cómo se evitan (R §6, uno por uno): abrir sin '
        'itamae o con uno solo; citar el RD 1420/2006, que está derogado, o creer que el salmón «fresco» se sirve sin '
        'papeles (el de acuicultura necesita el documento; el salvaje y el atún, congelación); un congelador que sólo '
        'llega a −18 °C usado para el anisakis; el shari a temperatura ambiente sin validar ante sanidad (art. 30.5 del '
        'RD 1086/2020) ni registro de pH; la plataforma sin techo (comisión, IVA de la comisión y caja: el combinado viaja '
        'bien, la tempura no; techo del {DELIVERY_PCT}); una carta larga que llena la vitrina de neta que se tira; el '
        'precio del combinado sin escandallo por canal (en plataforma el margen cae casi a la mitad); un solo proveedor de '
        'pescado; los alérgenos incompletos (el pescado, la mostaza del wasabi, el trigo de la soja y del surimi); las '
        'bandejas cerradas en la vitrina sin la etiqueta del art. 5 del RD 126/2015; cobrar al 10 % la cerveza y los '
        'refrescos azucarados para llevar; prometer «sin gluten»; y copiar cifras de franquicia (180 m², 300.000 €) para '
        'un local de 95 m². El plan de acción en 6 fases del checklist (80 tareas: 12/15/14/13/13/13). Cierra con el '
        'siguiente paso: completar el Excel con tus cifras, medir el rendimiento del salmón y los gramos reales de neta y '
        'de shari con la calculadora, y comparar tu consumo real con el {FOOD_COST} del plan el primer trimestre.',
}

#: Prohibidos en el texto (F1-camino §4): sellos y palabras vetadas, normas derogadas, la rentabilidad que contradice el
#: caso, restos de los moldes (Food Truck, Tapas Bar, Heladería, Pizzería, la Taquería —la semilla— y la Pollería) y las
#: frases del motor sin traducir. SALE «cubeta» (la vitrina de sushi va en cubetas GN: oficio) y NO entra «espada» (pez
#: espada). Los usa también `barrido_es.py` sobre los xlsx y el docx.
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
    r'helad', r'sorbete', r'granizad', r'horchata', r'mantec',
    # restos de la Pizzería
    r'pizz', r'napol[ei]t', r'margherita', r'levadura', r'amasad', r'bolas? de masa', r'fior di latte', r'mozzarella',
    r'c[uú]pula', r'\bETG\b', r'pliego', r'97/2010', r'AVPN', r'\ble[ñn]a\b',
    # restos de la Taquería (la semilla)
    r'taquer', r'trompo', r'\btacos?\b', r'\bcomal', r'\bpastor\b', r'gringa', r'nixtamal', r'tortillas? de (ma[ií]z|harina)',
    r'tortiller[oa]', r'mezcal', r'tequila', r'aguas? frescas?', r'carnitas', r'suadero', r'cochinita', r'guacamole',
    r'salsa macha',
    # restos de la Pollería
    r'poller', r'asador de pollos', r'pollo a la brasa', r'broaster', r'pollo asado',
    # frases del motor sin traducir y pids de los moldes
    r'alcohol (que sale por|del canal de) delivery', r'harinas panificables', r'pan com[uú]n',
    r'plan-negocio-(tapas-bar|heladeria|pizzeria|taqueria|polleria)',
]
#: Citas legales que son ERROR (F1-camino §4 y §7 F2 (5)): «art. 30» sin «1086/2020» a menos de 160 caracteres o atribuido
#: al RD 1021/2022; el RD 1420/2006 sin decir que está derogado; «7 días» junto a anisakis o congelación (es la opción de
#: la FDA de EE. UU., no la española).
RX_ART30 = re.compile(r'\bart(?:[ií]culo|\.)\s*30\b', re.I)
RX_ART30_MAL = re.compile(r'\bart(?:[ií]culo|\.)\s*30\.?\d*\s*(?:,\s*)?del (?:RD|Real Decreto) 1021/2022', re.I)
RX_1420 = re.compile(r'1420/2006', re.I)
RX_7DIAS = re.compile(r'(?:\b7|siete) d[ií]as[^.;]{0,120}(?:anisakis|congel)|(?:anisakis|congel)[^.;]{0,120}(?:\b7|siete) '
                      r'd[ií]as', re.I)


def art30_mal(texto):
    """Fragmentos con una cita legal mal (nombre histórico: empezó con el art. 30): «art. 30» sin «1086/2020» cerca o
    atribuido al RD 1021/2022, «RD 1420/2006» sin «derog» a ±160 caracteres y «7 días» de congelación."""
    malos = []
    for m in RX_ART30.finditer(texto):
        ventana = texto[max(0, m.start() - 160):m.end() + 160]
        if '1086/2020' not in ventana:
            malos.append(texto[max(0, m.start() - 50):m.end() + 60])
    for m in RX_ART30_MAL.finditer(texto):
        malos.append(texto[max(0, m.start() - 30):m.end() + 30])
    for m in RX_1420.finditer(texto):
        if not re.search(r'derog', texto[max(0, m.start() - 160):m.end() + 160], re.I):
            malos.append('RD 1420/2006 sin «derogado»: ' + texto[max(0, m.start() - 50):m.end() + 60])
    for m in RX_7DIAS.finditer(texto):
        malos.append('«7 días» de congelación: ' + texto[max(0, m.start() - 30):m.end() + 30])
    return malos


#: Avisos (F1-camino §4): no son error, pero cada uno se revisa a mano.
AVISOS = [
    ('«sushi grade» o «sashimi grade» (no es categoría legal)', re.compile(r'(sushi|sashimi)[ -]grade', re.I)),
    ('«auténtic» como promesa', re.compile(r'aut[eé]ntic', re.I)),
    ('«sin gluten» prometido', re.compile(r'(?<!no prometer )(?<!nada de )(?<!ni )«?sin gluten»?', re.I)),
    ('«obligatori…» junto a pH o a horas (no hay pH ni tiempo legal del shari)',
     re.compile(r'obligatori\w*[^.;]{0,80}(\bpH\b|\d+ horas)|(\bpH\b|\d+ horas)[^.;]{0,80}obligatori', re.I)),
    ('«−18 °C» junto a anisakis (el del anisakis es −20 °C)',
     re.compile(r'[−-]18 ?°C[^.;]{0,120}anisakis|anisakis[^.;]{0,120}[−-]18 ?°C', re.I)),
    ('registro horario «digital obligatorio»', re.compile(r'digital(es)? obligatori|obligatori\w* (en formato )?digital',
                                                          re.I)),
    ('franquicia: sus cifras no son el caso', re.compile(r'franquici', re.I)),
    ('«tortilla» o «mexican…» (restos de la taquería)', re.compile(r'tortilla|mexican', re.I)),
    ('«chimenea» (aquí, conducto)', re.compile(r'chimenea', re.I)),
]
#: Cifras que el texto puede llevar escritas: normas y artículos, y TODAS las que traen las pistas y la jerga. El resto,
#: token o nada.
_BASE = set('''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 33 35 36 40 45 50 60 63 70
74 75 80 90 100 120 150 180 200 300 671 673 677.9 1.000 1.221 1/2025 7/2022 37/1992 12/2012 18/2022 31/1995 4/2021
126/2026 1175/1990 1021/2022 1086/2020 126/2015 1169/2011 828/2014 852/2004 853/2004 1276/2011 1420/2006 2027 2026 2025
2024 2023 2022 2021 2020 2015 2014 2012 2011 2006 2004 1995 1992 1990 82.1 91.Uno.1.1 91.Uno.2.2 91.Dos.1.1 1.1 4.1 4.2
4.3 8.1 8.2 30.2 30.3 30.5 30.6 30.7 34.9 23.ª 12/15/14/13/13/13 −18 −20 −35 4,6 4,2 4,3 0-4 0-2'''.split())
RX_NUM = re.compile(r'(?<![\w{])[−+]?\d[\d.,/:−-]*\d|(?<![\w{])\d')
PERMITIDAS = _BASE | set(x.rstrip('.,') for x in RX_NUM.findall(re.sub(r'\{[A-Z0-9_]+\}', '', ' '.join(
    list(PISTAS.values()) + [JERGA]))))
#: Caracteres admitidos además del latín básico/extendido: tipografía española y los signos de temperatura (−, ≤, ≥, ≈).
RX_RARO = re.compile(r'[^\x00-ɏ‐-‧€°→ ‑«»¿¡ºª·…–—“”‘’−≤≥≈²$×÷]')


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
        raise SystemExit('falta %s: corre antes cifras_sus_es.py --calc en el VPS y cópialo aquí' % CIFRAS)
    cif = json.load(open(CIFRAS, encoding='utf-8'))['tokens']
    usados = set(re.findall(r'\{([A-Z0-9_]+)\}', ' '.join(PISTAS.values())))
    sin = sorted(usados - set(cif))
    if sin:
        raise SystemExit('las PISTAS citan tokens que no están en cifras_caso_es.json: %s (¿falta --calc?)' % sin)
    for s, p in PISTAS.items():                                   # las pistas también cumplen la regla del art. 30
        assert not art30_mal(p), (s, art30_mal(p))
    os.makedirs(TANDAS, exist_ok=True)
    rs = ranuras()
    for tanda, secs in (('sus_es_a', range(1, 6)), ('sus_es_b', range(6, 11))):
        sel = [r for r in rs if r['seccion'] in secs]
        ent = {
            'tanda': tanda, 'producto': 'Plan de Negocio: Sushi Bar ES 1.0 (aichef.pro, 35 €)',
            'salida': 'scripts/productos-digitales/plan-sushi/textos/%s.json' % tanda,
            'formato_salida': '{"<i>": "<párrafo en español>", …} con TODOS los "i" de "parrafos" y nada más',
            'brief': 'scripts/productos-digitales/plan-sushi/BRIEF-REDACTORES.md (léelo entero antes)',
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
        print('ERROR falta --tanda (sus_es_a o sus_es_b)')
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
            err.append('%d: cita legal mal (art. 30 sin el RD 1086/2020, RD 1420/2006 sin «derogado» o «7 días»): …%s…' % (r['i'], frag))
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
