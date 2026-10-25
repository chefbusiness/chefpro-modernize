#!/usr/bin/env python3
"""
tandas_docx.py — Pizzería Napolitana ES 1.0 (SPEC D16): prepara y valida las dos tandas de redacción del plan de negocio
(docx). Copia adaptada de `plan-heladeria/tandas_docx.py`.

Las 61 ranuras de texto del docx del Food Truck ES (131 párrafos, 10 Heading 1; mapa en
`business-plans-en-4/docx_es_cat.json`) se escriben NUEVAS, en español, para la pizzería:
  piz_es_a = §1-5 (29 ranuras) · piz_es_b = §6-10 (32 ranuras).
Gemela de FORMATO: el texto de la Heladería ES 1.0 en la misma ranura (`plan-heladeria/textos/hel_es_{a,b}.json`, la ES
1.0 de local fijo con tokens): sirve para ver cómo se escribe una ranura con tokens, nunca su contenido. No hay versión
anterior: el material es el research (`F1-research-pizzeria.md`) y las pistas de abajo. Las cifras del Excel (y de la
calculadora de masa y escandallo) van SIEMPRE como token {ASI} (`cifras_caso_es.json`); `docx_piz_es.py` las resuelve
al ensamblar. Sólo lee JSON: corre en el Mac.

    python3 tandas_docx.py preparar                       # tandas/piz_es_{a,b}.entrada.json
    python3 tandas_docx.py check --tanda piz_es_a         # valida textos/piz_es_a.json (salida del redactor)

Sesión Claude Code, 25-oct-2026.
"""
import argparse
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BP4 = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
GEMELA = os.path.join(os.path.dirname(AQUI), 'plan-heladeria', 'textos')
TANDAS, TEXTOS = os.path.join(AQUI, 'tandas'), os.path.join(AQUI, 'textos')
CIFRAS = os.path.join(AQUI, 'cifras_caso_es.json')
RESEARCH = 'scripts/productos-digitales/plan-pizzeria/F1-research-pizzeria.md'

SECCIONES = {
    1: '1. Resumen Ejecutivo', 2: '2. Concepto y Propuesta de Valor', 3: '3. Análisis de Mercado',
    4: '4. Análisis Competitivo', 5: '5. Plan de Marketing y Captación', 6: '6. Plan de Operaciones',
    7: '7. Estructura Organizativa y RRHH', 8: '8. Plan Financiero', 9: '9. Aspectos Legales y Licencias',
    10: '10. Conclusiones y Plan de Acción',
}

#: El nombre de la carta (SPEC D11, no negociable): igual en el Word, el checklist, la calculadora, la ficha y el correo.
NOMBRE_CARTA = ('«Pizza Napoletana» es una especialidad tradicional garantizada (ETG) CON reserva de nombre desde el '
                '18-12-2022 (Reglamento de Ejecución (UE) 2022/2313), y el Reglamento (UE) 2024/1143 la protege contra '
                'todo uso indebido, imitación o evocación «aunque el nombre protegido esté traducido» (art. 68.1). Sólo '
                'puede llamarse «pizza napolitana» (o «napoletana») la pizza que cumple el pliego (Reglamento (UE) '
                '97/2010: horno de leña, masa del día a temperatura ambiente, estirado a mano, mozzarella de búfala '
                'campana DOP o «Mozzarella» ETG) Y ha pasado la verificación oficial previa (arts. 72-73: comunicación '
                'a la autoridad, autocontrol y verificación por la autoridad o un organismo delegado acreditado). La '
                'AVPN es una asociación privada: su certificación no sustituye la verificación oficial. El caso NO usa '
                'el nombre: su carta dice «Margherita», «Marinara», «Diavola», «masa de fermentación larga» y «horno de '
                'leña»; la ETG es una opción que se explica (sin Excel). «Estilo napolitano» o «napolitana» en el '
                'rótulo es zona gris (posible evocación): «consúltalo antes». Nunca «certificada», «ETG» o «verace» como '
                'sello del lector ni del producto. El título del producto («Pizzería Napolitana») nombra el tipo de '
                'negocio, no etiqueta un alimento')
#: El pliego de la ETG como receta de referencia, con sus cifras (research §0.3 y §1.b; Reglamento (UE) 97/2010).
PLIEGO = ('por 1 litro de agua: 1.800 g de harina de trigo tierno (W 220-380, proteína 11-12,5 %), 50-55 g de sal y 3 g '
          'de levadura de cerveza (un 55,6 % de hidratación, ≈ 2,9 % de sal y 0,17 % de levadura sobre la harina); '
          '10 minutos de incorporación y 20 de amasado lento; 2 horas de primera fermentación en bloque; bolas a mano '
          'de 180-250 g; 4-6 horas de segunda fermentación a temperatura ambiente (unos 25 °C) y uso en las 6 horas '
          'siguientes, todo en ciclo continuo (sin frío, ni biga ni poolish); disco de 35 cm como máximo, centro de '
          '0,4 cm y cornisa («cornicione») de 1-2 cm, sin rodillo ni prensa; solera a unos 485 °C y bóveda a unos '
          '430 °C, 60-90 segundos, exclusivamente horno de leña. 1 kg de harina da unos 1.586 g de masa: 6 bolas de '
          '250 g (8 de 200 g)')

#: Lo que tiene que contar cada sección (español de España, para el mercado español; research §0-§6). Cifras del
#: Excel y de la calculadora = tokens.
PISTAS = {
    1: 'Qué es el negocio: una pizzería con horno de leña a la vista y sala de 50 plazas (más una terraza de 24 de abril '
       'a octubre) en una ciudad media (150.000-300.000 habitantes), en una calle de barrio con paso o junto a una '
       'plaza; local de 130 m² con salida de humos a cubierta posible (el filtro del local), sin traspaso. Una SL '
       'unipersonal con el titular de pizzaiolo jefe, un segundo pizzaiolo, ayudante, sala de dos servicios y refuerzo '
       'de fin de semana. Carta corta de 14-16 pizzas de masa de fermentación larga (de 9,50 a 15,50 € con IVA; la '
       'Margherita a 10 €), 5 entrantes y 3 postres. Para llevar y a domicilio: la recogida en el local, sin comisión, '
       'y la plataforma con su reparto, con techo (sin reparto propio). Abre en SEPTIEMBRE (el Mes 1 del Excel es '
       'septiembre), de martes a domingo, comidas y cenas, y cierra los lunes y dos semanas en enero. Cifras clave por '
       'token: {COMENSALES_DIA} comensales equivalentes al día (sala, para llevar y domicilio) a {TICKET} por comensal '
       'sin IVA y {DIAS_APERTURA} días de apertura, ventas {VENTAS_A1}, resultado neto {NETO_A1} ({NETO_PCT_A1}), '
       'inversión {INVERSION_TOTAL} (de la que {INVERSION_PARTIDAS} son obra, horno, equipo y puesta en marcha), '
       'préstamo {PRESTAMO} y equilibrio en {BE_COMENSALES_DIA} comensales al día. Qué contiene el kit: este plan de '
       'negocio de 10 secciones, el Excel del plan financiero de 9 hojas, el checklist de apertura de 80 tareas en 6 '
       'fases, la calculadora de masa y escandallo (masa por litro de agua con las cifras del pliego y por porcentaje '
       'panadero, y el escandallo de 8 pizzas) y la guía de equivalencias para Latinoamérica. Y el hallazgo que lo '
       'distingue, en una frase: desde 2022 «pizza napolitana» es un nombre reservado, y este plan te dice qué puedes '
       'poner en la carta (el detalle va en el §2).',
    2: 'Tipos de pizzería y por qué esta: napolitana de sala con horno de leña (la de este plan), pizza al corte, sólo '
       'reparto (cocina sin sala) y franquicia; cada una con otra inversión, otro local y otro margen. La propuesta: '
       'masa de fermentación larga hecha cada día, horno de leña a la vista, carta corta, producto italiano y '
       'entrantes napolitanos (frittatina, montanarina, burrata), postres caseros. EL NOMBRE DE LA CARTA, tal cual y '
       'sin suavizarlo (SPEC D11): ' + NOMBRE_CARTA + '. Dilo como ventaja, sin miedo y sin asustar: el lector sabrá '
       'qué escribir en su carta, en su web y en su ficha de la plataforma. El ticket de {TICKET} es por comensal y '
       'sin IVA ({TICKET_IVA} con IVA): en sala, medio entrante (3,50 €), una pizza (12,50 €), 1,3 bebidas (3,90 €), '
       'algún postre (1,80 €) y café (0,30 €), unos 22 € con IVA. Mezcla de ventas: comida {PCT_COMIDA} y bebida '
       '{PCT_BEBIDA}; en sala unos 77 % de las ventas, para llevar unos 13 % y por plataforma {DELIVERY_PCT}.',
    3: 'Mercado en España con fuente. Búsquedas mensuales en Google España (DataForSEO, 25 de octubre de 2026): '
       '«fior di latte» 12.100, «pizzaiolo» 12.100, «pizza napolitana» 8.100, «pizzería napolitana» 4.400, «pizza '
       'napoletana» 2.900, «biga» 2.900, «harina caputo» 1.900, «masa pizza napolitana» 720; y apenas 20 «montar una '
       'pizzería», 10 «plan de negocio pizzería» y 10 «cuánto cuesta montar una pizzería»: el oficio busca mucho y el '
       'que va a abrir busca poco y decide con datos. Reparto a domicilio en restauración: 2.821 millones de euros en '
       '12 meses (−4 %), un 90 % más que en 2019 (datos de Circana publicados por Alimarket en febrero de 2025); la '
       'pizza no es el plato más pedido en Just Eat en 2025 (hamburguesa, maki y durum por delante, según The '
       'Objective). Precio de la Margherita en carta, con IVA, en 14 pizzerías de Madrid, Barcelona, Valencia, Marbella '
       'y Tenerife (octubre de 2026): mediana de 10,90 €; en carta propia, 10,50-12,90 € en Madrid y Barcelona y 8-9 € '
       'en Canarias. La estacionalidad del plan, con el Mes 1 en septiembre: diciembre es el pico (cenas de empresa y '
       'de grupo), enero y febrero los meses más flojos, la terraza sube de abril a junio y agosto cae (la ciudad se '
       'vacía y el horno a 450 °C con 38 °C fuera); entre el mejor mes y el peor hay un 41 % de diferencia: una '
       'pizzería de barrio es un negocio bastante plano. El hueco: lo que sale en Google para «cómo montar una pizzería» son guías '
       'genéricas, foros y PDF de planes latinoamericanos, con horquillas de inversión sin desglose; nadie cuenta el '
       'nombre protegido, el pliego con sus cifras, el IAE de la sala y del reparto, la ordenanza de humos, el IVA de la '
       'bebida para llevar, la Ley 1/2025 en la carta ni la caja con la comisión de la plataforma. NADA de tamaños de '
       'mercado sin fuente.',
    4: 'Competencia por categorías, sin nombres de empresas ni cifras inventadas: las cadenas de pizza a domicilio '
       '(precio y promoción permanente); las cadenas italianas de sala en centros comerciales; las pizzerías '
       'napolitanas de autor de las grandes ciudades (ticket alto, listas de espera); la pizzería de barrio de toda la '
       'vida (horno eléctrico o de gas, carta larga); la pizza congelada y refrigerada del supermercado; las cocinas '
       'que sólo venden por plataforma. Dónde gana este concepto: horno de leña a la vista, masa de fermentación larga '
       'del día, carta corta con producto italiano, una sala de barrio con ticket de unos 22 € con IVA, la recogida en '
       'el local y la honestidad en el nombre (la competencia que escribe «pizza napolitana» sin pliego ni verificación '
       'se arriesga a tener que retirarlo de la carta, de la web y de la ficha de la plataforma). El riesgo: la guerra '
       'de precios y la dependencia de la plataforma; cómo se defiende (producto, experiencia de sala, recogida, '
       'escandallo de cada pizza, clientela de barrio).',
    5: 'Marketing y captación: apertura en septiembre con degustación para el barrio, los comercios y los colegios; '
       'ficha de Google Business con el horario de comidas y cenas, fotos del horno y respuesta a cada reseña; redes '
       'sociales con el montaje del horno, el primer fuego, la masa y la pizza de la semana; carta clara con el nombre '
       'de cada receta (sin el nombre protegido); cenas de empresa y de grupo en diciembre; fidelización sencilla '
       '(tarjeta de sellos o club de la pizza del mes) sin cifras de conversión inventadas. PLATAFORMA FRENTE A REPARTO '
       'PROPIO (sin Excel, razonado): el plan vende por plataforma con su reparto un {DELIVERY_PCT} de las ventas '
       '({VENTAS_PLATAFORMA_A1} al año) y paga una comisión del {COMISION_DELIVERY} ({COMISIONES_DELIVERY_A1} al año); '
       'las guías del sector sitúan las comisiones con reparto de la plataforma entre el 25 y el 35 % más IVA según la '
       'zona, más las promociones (un 8-12 % de la venta del canal) y la caja de cartón (≈ 1 €); la pizza de masa '
       'blanda llega peor que otros platos, por eso el techo del plan es ese {DELIVERY_PCT}. Un repartidor propio de '
       'viernes a domingo (0,35 jornada, unos 8.800 € al año con la Seguridad Social) más moto, seguro y gasolina (unos '
       '2.500 €) cuesta unos 11.300 € para repartir esa misma venta: un 29 %, lo mismo que la plataforma pero con el '
       'riesgo laboral y sin su escaparate; compensa a partir de unos 60.000-70.000 € de venta a domicilio al año o con '
       'una zona de reparto corta y densa, y siempre con contrato laboral. La recogida en el local no paga comisión: '
       'empújala con precio. Presupuesto de marketing {MARKETING_ANO} al año, más la marca, la web, las fotos y el '
       'lanzamiento, que van en la inversión ({MARCA_LANZAMIENTO}).',
    6: 'Operaciones del obrador, el horno y la sala. LA MASA: el pliego de la ETG es la receta oficial con cifras: '
       + PLIEGO + '. La masa que se hace hoy en muchas pizzerías españolas (biga o poolish, 60-75 % de hidratación, '
       '24-72 horas en frío) es buena masa, pero queda FUERA del pliego: no la llames «napolitana». La calculadora del '
       'pack hace las dos (por litro de agua con las cifras del pliego y por porcentaje panadero): coste por bola '
       '{COSTE_BOLA}, y la Margherita de ejemplo cuesta {COSTE_MARGHERITA} y sale a un {FC_MARGHERITA} de food cost; '
       'con búfala, burrata o embutido italiano, más. Producción del caso: unas 75 pizzas al día de media y unas 140 el '
       'sábado, unos 19 kg de masa al día (unos 12 kg de harina); un horno de seis pizzas a 90 segundos da en teoría '
       '150-200 pizzas por hora de pico, y una amasadora de 30-40 kg cubre el sábado en dos amasadas. EL HORNO, LEÑA, GAS '
       'O ELÉCTRICO, con precio y fuente: el de leña de 120-130 cm del caso {HORNO} (los prefabricados profesionales con '
       'precio publicado van de 2.750 a 5.505 €; los artesanos napolitanos no publican tarifa: pide oferta con el '
       'montaje), con la chimenea a cubierta y el filtro de partículas {CHIMENEA} y la leña como coste fijo, {LENA_ANO} '
       'al año (unos 5 kg por hora de fuego, 11 horas al día y 300 días, a unos 0,22 € el kg: se quema por hora '
       'encendido, no por pizza; leña seca y sin tratar, de encina, roble, haya u olivo); el de gas (instalación por '
       'empresa habilitada y revisión cada 5 años, el gas también va fijo); el eléctrico (un napolitano de seis pizzas '
       'cuesta unos 13.140 € sin IVA, llega a 515 °C y pide 16,4 kW en trifásica; no te libra de la campana extractora '
       'ni del conducto por los vahos). VARIANTE ELÉCTRICA SIN EXCEL, razonada: horno eléctrico en lugar del de leña '
       '(−9.000 €) y sin filtro de partículas (unos −3.000 € de la chimenea): unos 1.100 € más de inversión, 16,4 kW '
       'más contratados, sin leña (unos 3.600 € menos al año) y SIN poder usar el nombre protegido. Resto del equipo: '
       'amasadora {AMASADORA}, mesa fría {MESA_FRIA}, armarios para las cajas de bolas {ARMARIOS}, campana extractora '
       'con freidora y fogón {CAMPANA}. Horario: de martes a domingo, comidas de 13:30 a 16:00 y cenas de 20:00 a '
       '23:30; cierra los lunes, el 25 de diciembre y dos semanas en enero. Higiene en la operación: tiempos y '
       'temperaturas de las bolas en el APPCC, quesos a la temperatura de su etiqueta, aceite en la mesa en envase '
       'irrellenable, cajas que mantengan la temperatura, limpieza de la campana extractora al menos una vez al año, '
       'mantenimiento {MANTENIMIENTO_HORNO} al año. Suministros {SUMINISTROS_MES} al mes de media (unos 25 kW en '
       'trifásica).',
    7: 'Equipo (7 filas en la hoja Personal): el titular, pizzaiolo jefe (masa, horno en el turno fuerte, compras y '
       'gestión; {SUELDO_TITULAR} brutos al mes en 14 pagas; como administrador de la SL cotiza en el régimen de '
       'autónomos: confírmalo con tu gestoría); un segundo pizzaiolo de horno y estirado que sabe hacer la masa (el '
       'pizzaiolo único es un riesgo, no un ahorro: una baja cierra la pizzería); un ayudante de cocina y masa de 30 '
       'horas; un encargado/a de sala y barra todo el año; un camarero/a de cenas y fines de semana de 25 horas; un '
       'refuerzo de viernes a domingo (sala, terraza, recogida y tablet de las plataformas; sin reparto propio); y las '
       'suplencias de vacaciones y descansos: {PLANTILLA_PERSONAS} personas y {JORNADAS} jornadas completas '
       'equivalentes, coste {PERSONAL_A1} ({PERSONAL_PCT_A1} de las ventas), cobertura de horas {COBERTURA_HORAS} '
       '({HORAS_CONTRATADAS} horas contratadas frente a {HORAS_NECESARIAS} necesarias); el sábado por la noche hacen '
       'falta unas cinco personas (entran el refuerzo y el camarero de cenas). La plantilla crece con personas: '
       '{INCORPORACIONES_A2} de incorporaciones el año 2 y otro tanto el año 3. Convenio provincial de hostelería (el '
       'art. 4 del VI Acuerdo Laboral de ámbito Estatal para el sector de Hostelería nombra las «pizzerías» y el '
       'reparto propio o por encargo); todos por encima del SMI de 2026 (1.221 € al mes en 14 pagas, Real Decreto '
       '126/2026) en proporción a la jornada; contratos por escrito; registro de jornada (art. 34.9 del Estatuto de los '
       'Trabajadores); nunca autónomos que te facturan con tu horario (falso autónomo, art. 1.1); menores de 18 años '
       'sin trabajo nocturno ni horas extraordinarias (art. 6): confírmalo con tu gestoría si las cenas acaban a '
       'medianoche. Repartidor propio, si algún día lo pones: contrato laboral del convenio de hostelería; en el reparto '
       'que organiza una plataforma por algoritmo, la ley presume la relación laboral (disposición adicional 23.ª del '
       'Estatuto). Formación de manipuladores acreditada por la empresa (el antiguo carné de manipulador ya no existe) '
       'con temperaturas de la masa y de los quesos, alérgenos y contacto cruzado; formación de pizzaiolo (masa, fuego, '
       'pala); prevención de riesgos (quemaduras del horno, cortes, cargas de leña y de sacos de harina, humo y calor).',
    8: 'Plan financiero, TODO por token: inversión {INVERSION_TOTAL} = compras {CAPEX} (obra, horno, equipo y puesta en '
       'marcha {INVERSION_PARTIDAS}, más la fianza {FIANZA} y {RENTA_PREVIA} de renta antes de abrir) + fondo de '
       'maniobra {FONDO_MANIOBRA}; IVA de la inversión {IVA_INVERSION}; necesidad de caja {NECESIDAD_CAJA}; financiación '
       '{RECURSOS_PROPIOS} propios + préstamo {PRESTAMO} al {TIPO_PRESTAMO}, {PLAZO_PRESTAMO} años con {CARENCIA} de '
       'carencia, cuota {CUOTA_ANUAL}. Cuenta de resultados de 3 años: ventas {VENTAS_A1}/{VENTAS_A2}/{VENTAS_A3}; '
       'margen bruto {MARGEN_BRUTO_PCT_A1} (después de TODOS los costes variables: mercancía {MERCANCIA_PCT_A1}, cajas '
       'y envases, plataforma, medios de pago y varios); personal {PERSONAL_A1}; alquiler {ALQUILER_ANO} '
       '({ALQUILER_PCT_A1}); leña {LENA_ANO} y tasa de terraza y residuos {TASAS_TERRAZA_RESIDUOS} («pon la de tu '
       'ayuntamiento»); resultado de explotación antes de amortizaciones e intereses {EBITDA_A1} ({EBITDA_PCT_A1}); '
       'neto {NETO_A1}/{NETO_A2}/{NETO_A3} ({NETO_PCT_A1}/{NETO_PCT_A2}/{NETO_PCT_A3}; el año 3 tributa ya al tipo '
       'general del Impuesto de Sociedades). Honestidad: una pizzería de barrio bien llevada deja en torno a un 9 % '
       'neto; las rentabilidades mucho más altas que circulan por internet no se sostienen con una plantilla legal. '
       'CRECIMIENTO tal cual lo hace el Excel: suben los comensales un {CREC_A2} y un {CREC_A3} (de {COMENSALES_DIA} a '
       '{COMENSALES_DIA_A2} y {COMENSALES_DIA_A3} al día) con el mismo ticket, y la plantilla crece con personas '
       '({INCORPORACIONES_A2} al año), no con un porcentaje. IVA: la comida al 10 % (en sala, para llevar y a '
       'domicilio); de la bebida, la parte que sale del local con alcohol o con azúcares añadidos ({BEBIDA_21_PCT} de '
       'la bebida, la columna H de su línea) va al 21 % y el resto al 10 %: el IVA medio de la bebida es '
       '{IVA_BEBIDA_LINEA}. Equilibrio contable {BE_COMENSALES_DIA} comensales al día (ingresos {BE_INGRESOS}; holgura '
       '{HOLGURA_CONTABLE}); equilibrio de caja {BE_COMENSALES_DIA_CAJA} comensales al día y holgura {HOLGURA_CAJA}, que '
       'es la del PRIMER año (sólo intereses por la carencia); desde el segundo, con la devolución del principal, la '
       'holgura baja a {HOLGURA_CAJA_A2} ({BE_COMENSALES_DIA_CAJA_A2} comensales al día de equilibrio) y en el tercero '
       'queda en {HOLGURA_CAJA_A3} ({BE_COMENSALES_DIA_CAJA_A3}): esos años son los que hay que vigilar. Rotación: los '
       '{COMENSALES_DIA} comensales equivalentes sobre {AFORO} plazas dan {ROTACION_IMPLICITA} al día, pero incluyen a '
       'quien se lleva la pizza o la recibe en casa, que no ocupa mesa. DSCR mínimo {DSCR_MIN}. TESORERÍA: el Mes 1 es '
       'septiembre; la rampa arranca al {RAMPA_MES1} y llega al ritmo de crucero en {MESES_RAMPA} meses (en Navidad); '
       'el saldo mínimo es {SALDO_MINIMO} en el mes {MES_SALDO_MINIMO} ({MES_SALDO_MINIMO_NOMBRE}) y el año acaba '
       '(agosto) con {SALDO_MES12}; enero y febrero (Meses 5 y 6) son los más flojos y llegan con el fondo intacto; las '
       'pagas extra salen en diciembre (Mes 4) y julio (Mes 11); el IVA se liquida por trimestres naturales (octubre, '
       'enero, abril y julio), no por los del plan. Payback del proyecto: {PAYBACK} (el token ya es texto: no le añadas '
       '«años»). Escenarios: pesimista ({ESC_PES_COMENSALES} comensales a {ESC_PES_TICKET} y {ESC_PES_DIAS} días: '
       'ventas {ESC_PES_VENTAS}, neto {ESC_PES_NETO}) y optimista ({ESC_OPT_COMENSALES} comensales a {ESC_OPT_TICKET} y '
       '{ESC_OPT_DIAS} días: ventas {ESC_OPT_VENTAS}, neto {ESC_OPT_NETO}). El Excel manda: si cambias una celda verde, '
       'el documento se queda atrás.',
    9: 'Marco legal con su cita (sólo esto, dicho así; lo marcado «compruébalo», dilo así y sin cifra): SL unipersonal '
       '(capital desde 1 €, Ley 18/2022) o autónomo; IAE (RDLeg 1175/1990): grupo 671 «servicios en restaurantes», por '
       'categoría (de uno a cinco tenedores), para la sala, y epígrafe 677.9 «otros servicios de alimentación propios '
       'de la restauración» para la venta para llevar y a domicilio (sin comedor separado, el grupo 673): confírmalo '
       'con tu gestoría; alta censal con el modelo 036; exento de cuota con menos de 1 millón de cifra de negocio (art. '
       '82.1.c de la Ley de Haciendas Locales). Apertura: el 671 y el 677.9 no están en el anexo de la Ley 12/2012: '
       'licencia o declaración responsable según la ordenanza de tu ayuntamiento; la terraza es ocupación de la vía '
       'pública y va siempre aparte (art. 2.2). Humos: un horno de restaurante (de menos de 1 MW) NO es actividad '
       'potencialmente contaminadora de la atmósfera (catálogo del RD 100/2011, actualizado por el RD 1042/2017): lo '
       'decide la ordenanza de humos de cada ayuntamiento; ejemplo leído, Madrid (Ordenanza 4/2021 de Calidad del Aire, '
       'BOCM de 16-04-2021): conducto exclusivo a cubierta que supere en 1 m la altura del edificio propio y la de '
       'cualquier otro en 15 m de radio (art. 12 y anexo I), limpieza al menos una vez al año y, con leña o carbón, '
       'sistemas específicos de filtrado de partículas (art. 23); en tu ciudad, pide la ordenanza (sin cifras de otras). '
       'Gas: instalación por empresa instaladora habilitada y control cada 5 años (RD 919/2006, ITC-ICG 07). Sanidad: '
       'declaración responsable al registro sanitario de tu comunidad autónoma (RD 1021/2022); el RGSEAA sólo aplica si '
       'suministras a otros negocios por encima de lo que permite su art. 3; APPCC (Reglamento (CE) 852/2004 y la '
       'flexibilidad del art. 20 del RD 1021/2022); la temperatura de los quesos, embutidos y masas la marca la etiqueta '
       'del fabricante (art. 4.2); el transporte de lo que sale, en medios que mantengan la temperatura (art. 4.3). '
       'Alérgenos: por escrito, o de palabra con registro escrito y cartel (RD 126/2015), y en la venta a distancia '
       'disponibles antes de comprar (Reglamento (UE) 1169/2011, art. 14). «Sin gluten» sólo con 20 mg/kg o menos tal '
       'como se vende (Reglamento de Ejecución (UE) 828/2014): con harina en el aire del obrador, no lo prometas salvo '
       'protocolo y analítica. Aceite en la mesa en envase etiquetado con cierre irrecuperable que impida reutilizarlo '
       '(RD 760/2021, art. 7). Ley 1/2025 de desperdicio alimentario, art. 8: el cliente puede llevarse lo que no '
       'consuma sin coste (salvo el del envase de plástico de un solo uso) y la pizzería lo avisa de forma visible, '
       'mejor en la carta; el plan de prevención y los convenios de donación no obligan a las microempresas (art. 6). '
       'Ley 7/2022, art. 55: el envase de plástico de un solo uso para llevar se cobra aparte en el tique; la caja de '
       'cartón no es plástico (si lleva película plástica, consúltalo con el proveedor). IVA (Ley 37/1992, art. 91): la '
       'comida al 10 % en sala, para llevar y a domicilio; la cerveza, el vino y los refrescos con azúcares añadidos que '
       'salen del local, al 21 %; en sala, todo al 10 %. Personal: convenio provincial de hostelería (ALEH VI, art. 4), '
       'SMI de 2026 (RD 126/2026), Estatuto de los Trabajadores (arts. 1.1, 6, 34.9 y disposición adicional 23.ª). '
       'Facturación con software Veri*factu (consulta con tu gestoría la fecha que te aplica). El nombre de la carta: '
       + NOMBRE_CARTA + '; la ETG es una opción: comunicar a la autoridad, autocontrol documentado y verificación previa '
       '(Reglamento (UE) 2024/1143, arts. 72-73), con costes que pueden ser tuyos; quién la verifica en España y cuánto '
       'cuesta: pregúntalo en tu comunidad autónoma. Lo que no esté aquí no se afirma: «compruébalo con tu gestor, tu ayuntamiento o '
       'el inspector».',
    10: 'Conclusiones con tokens (viabilidad, holgura de caja del año 1 y de los años 2 y 3, DSCR mínimo, saldo mínimo, '
        'payback) y los riesgos de una pizzería y cómo se mitigan (research §6, uno por uno): firmar un local sin salida '
        'de humos a cubierta (el error número uno: sin chimenea exclusiva no hay horno de leña, y el eléctrico tampoco '
        'se libra de la campana extractora); llamar «napolitana» a la pizza sin pliego ni verificación (retirada de la '
        'carta, de la web y de la ficha de la plataforma); escandallar sólo la Margherita (con búfala, burrata, embutido '
        'italiano y la comisión de la plataforma, la que más se vende puede irse al 25-35 %); abrirse a la plataforma '
        'sin cuentas (comisión, promociones y caja se comen el margen; techo del {DELIVERY_PCT}); subestimar la leña y el '
        'mantenimiento del horno ({LENA_ANO} al año; la leña húmeda o tratada ensucia el horno, el humo y la pizza); '
        'masa sin protocolo (bolas pasadas un sábado flojo y faltas uno lleno); prometer «sin gluten» con harina en el '
        'aire; aceite en botella rellenable y no ofrecer llevarse lo que sobra; el pizzaiolo único; el reparto propio '
        'con «autónomos»; darse de alta sólo en el 671 y olvidar el 677.9. El plan de acción en 6 fases del checklist '
        '(80 tareas: 12/15/14/13/13/13). Cierra con el siguiente paso: completar el Excel con tus cifras y escandallar '
        'tu carta con la calculadora.',
}

#: Prohibidos en el texto (SPEC D12; F1-camino §3): sellos y palabras vetadas, normas derogadas, la rentabilidad que
#: contradice el caso, restos de los moldes (Food Truck, Tapas Bar —semilla—, Heladería —formato—) y las frases del
#: motor sin traducir. SIN los restos de panadería del gemelo: harina, masa, levadura y amasado son el oficio. Los usa
#: también `barrido_es.py` sobre los xlsx y el docx.
PROHIBIDOS = [
    r'\bfreelance', r'validad[oa]s?', r'Espa[ñn]a,? 2026', r'carn[eé]t? de manipulador(?! ya no existe)',
    r'tarifa plana', r'\bCNAE\b', r'(?<!inscrito en el )\bRGSEAA\b(?!.{0,80}(s[oó]lo|otros (establecimientos|negocios)))',
    r'licencia de apertura', r'895/2013', r'393/2007', r'15 ?(-|–|a|y el) ?25 ?%',
    r'versi[oó]n (1\.1|2\.2|anterior)', r'\bv1\.1\b', r'solopreneur',
    # restos del Food Truck
    r'food ?truck', r'\bcami[oó]n\b', r'ventanilla', r'generador', r'aparcamiento',
    # restos del Tapas Bar (semilla)
    r'\btapas?\b', r'gastrobar', r'vermut', r'\braciones\b', r'\bpinchos?\b', r'tapeo', r'afterwork', r'salamandra',
    r'rational', r'[Ff]ichero v1\.1',
    # restos de la Heladería (formato)
    r'helad', r'mantec', r'cubeta', r'sorbete', r'pasteuriz', r'granizad', r'horchata', r'tarrina',
    # frases del motor sin traducir y pids de los moldes
    r'alcohol (que sale por|del canal de) delivery', r'pan com[uú]n', r'plan-negocio-(tapas-bar|heladeria)',
]
#: Avisos del nombre de la carta (SPEC D11): no son error (el Word explica la ETG), pero cada uno se revisa.
RX_D11 = re.compile(r'(?<!no )\b(es|son) (una |la )?pizzas? napol[ei]tanas?\b|napol[ei]tanas? (certificadas?|verace|'
                    r'aut[eé]nticas?)|certificad[oa]s? (por la |de la )?AVPN|AVPN.{0,40}(obligatori|necesari|exig)|'
                    r'\b(nuestra|tu|la) pizza napol[ei]tana\b', re.I)
#: Cifras que el texto puede llevar escritas (normas, research con fuente, carta y estructura del caso, pliego).
PERMITIDAS = set('''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 28 29 30 31 35 38 40 41 45 46
50 51 53 55 60 63 65 68 70 72 73 75 77 80 82 90 91 99 100 110 120 126 130 140 150 180 200 250 300 400 430 450 485 515
671 673 677.9 720 760 828 852 1.000 1.021 1.042 1.100 1.143 1.169 1.175 1.221 1.350 1.586 1.800 1.900 2.500 2.821 2.900
3.000 3.600 4.400 8.100 8.800 9.000 11.300 12.100 13.140 2.313 97/2010 2022/2313 2024/1143 828/2014 1169/2011 852/2004
1021/2022 126/2015 760/2021 1/2025 7/2022 37/1992 12/2012 18/2022 31/1995 100/2011 1042/2017 919/2006 4/2021 126/2026
1175/1990 2026 2025 2024 2023 2022 2021 2019 2017 2015 2014 2012 2011 2010 2006 2004 1995 1992 1990 18-12-2022 16-04-2021
55,6 2,9 0,17 0,4 0,35 0,22 1,33 10,90 10,50-12,90 8-9 9,50 15,50 12,50 3,50 3,90 1,80 0,30 16,4 11-12,5 220-380 50-55
180-250 4-6 60-90 1-2 60-75 24-72 150-200 30-40 120-130 2.750 5.505 13:30 16:00 20:00 23:30 150.000-300.000 25-35 8-12
22-30 60.000-70.000 25-28 22-28 20-28 12/15/14/13/13/13 82.1 91.Uno.1.1 91.Uno.2.2 1.1 6.4 34.9 4.1 4.2 4.3 5.3 72-73 23.ª
150.000 300.000 1,5 20 25'''.split())
RX_NUM = re.compile(r'(?<![\w{])[−+]?\d[\d.,/:−-]*\d|(?<![\w{])\d')
#: Caracteres admitidos además del latín básico/extendido: tipografía española y los signos de temperatura (−, ≤, ≥, ≈).
RX_RARO = re.compile(r'[^\x00-ɏ‐-‧€°→ ‑«»¿¡ºª·…–—“”‘’−≤≥≈²]')


def ranuras():
    d = json.load(open(os.path.join(BP4, 'docx_es_cat.json'), encoding='utf-8'))['parrafos']
    gem = {}
    for t in ('hel_es_a', 'hel_es_b'):
        gem.update(json.load(open(os.path.join(GEMELA, t + '.json'), encoding='utf-8')))
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
    if not os.path.exists(CIFRAS):
        raise SystemExit('falta %s: corre antes cifras_piz_es.py en el VPS y cópialo aquí' % CIFRAS)
    cif = json.load(open(CIFRAS, encoding='utf-8'))['tokens']
    usados = set(re.findall(r'\{([A-Z0-9_]+)\}', ' '.join(PISTAS.values())))
    sin = sorted(usados - set(cif))
    if sin:
        raise SystemExit('las PISTAS citan tokens que no están en cifras_caso_es.json: %s' % sin)
    os.makedirs(TANDAS, exist_ok=True)
    rs = ranuras()
    for tanda, secs in (('piz_es_a', range(1, 6)), ('piz_es_b', range(6, 11))):
        sel = [r for r in rs if r['seccion'] in secs]
        ent = {
            'tanda': tanda, 'producto': 'Plan de Negocio: Pizzería Napolitana ES 1.0 (aichef.pro, 35 €)',
            'salida': 'scripts/productos-digitales/plan-pizzeria/textos/%s.json' % tanda,
            'formato_salida': '{"<i>": "<párrafo en español>", …} con TODOS los "i" de "parrafos" y nada más',
            'brief': 'scripts/productos-digitales/plan-pizzeria/BRIEF-REDACTORES.md (léelo entero antes)',
            'research': RESEARCH + ' (§0 hallazgos, §1 normativa, §2 precios, §3 caso, §4 SERP, §6 errores y riesgos: '
                                   'material de apoyo; la pista de la sección manda)',
            'nombre_de_la_carta (SPEC D11, literal en el fondo)': NOMBRE_CARTA,
            'pliego_de_la_masa (Reglamento (UE) 97/2010)': PLIEGO,
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
        print('ERROR falta --tanda (piz_es_a o piz_es_b)')
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
        m = RX_D11.search(t)
        if m:
            avi.append('%d: ¿el nombre «napolitana» como sello o afirmación? (SPEC D11) «%s»' % (r['i'], m.group(0)))
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
