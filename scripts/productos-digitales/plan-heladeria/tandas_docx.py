#!/usr/bin/env python3
"""
tandas_docx.py — Heladería Artesanal ES 1.0 (SPEC D15): prepara y valida las dos tandas de redacción del plan de negocio
(docx). Copia adaptada de `parrillero-2_2/tandas_docx.py`.

Las 61 ranuras de texto del docx del Food Truck ES (131 párrafos, 10 Heading 1; mapa en
`business-plans-en-4/docx_es_cat.json`) se escriben NUEVAS, en español, para la heladería:
  hel_es_a = §1-5 (29 ranuras) · hel_es_b = §6-10 (32 ranuras).
Gemela de FORMATO: el texto del Parrillero ES 2.2 en la misma ranura (`parrillero-2_2/textos/par_es_{a,b}.json`, la
única ES 2.2 con tokens): sirve para ver cómo se escribe una ranura con tokens, nunca su contenido. No hay versión
anterior: el material es el research (`F1-research-heladeria.md`) y las pistas de abajo. Las cifras del Excel van
SIEMPRE como token {ASI} (`cifras_caso_es.json`); `docx_hel_es.py` las resuelve al ensamblar. Sólo lee JSON: corre
en el Mac.

    python3 tandas_docx.py preparar                       # tandas/hel_es_{a,b}.entrada.json
    python3 tandas_docx.py check --tanda hel_es_a         # valida textos/hel_es_a.json (salida del redactor)

Sesión Claude Code, 25-oct-2026.
"""
import argparse
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BP4 = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
GEMELA = os.path.join(os.path.dirname(AQUI), 'parrillero-2_2', 'textos')
TANDAS, TEXTOS = os.path.join(AQUI, 'tandas'), os.path.join(AQUI, 'textos')
CIFRAS = os.path.join(AQUI, 'cifras_caso_es.json')
RESEARCH = 'scripts/productos-digitales/plan-heladeria/F1-research-heladeria.md'

SECCIONES = {
    1: '1. Resumen Ejecutivo', 2: '2. Concepto y Propuesta de Valor', 3: '3. Análisis de Mercado',
    4: '4. Análisis Competitivo', 5: '5. Plan de Marketing y Captación', 6: '6. Plan de Operaciones',
    7: '7. Estructura Organizativa y RRHH', 8: '8. Plan Financiero', 9: '9. Aspectos Legales y Licencias',
    10: '10. Conclusiones y Plan de Acción',
}

#: Orden del proceso (SPEC D11, seguridad, no negociable): igual en el Word, el checklist y este brief.
ORDEN_PROCESO = ('secos con el azúcar; después los líquidos; las grasas (nata, mantequilla), las yemas y los '
                 'emulsionantes entran al subir la temperatura, a 40-50 °C, ANTES de pasteurizar; pasteurización a '
                 '85 °C; enfriado rápido a 4 °C o menos; maduración a 2-4 °C (de 4 a 12 horas; con huevo, se manteca '
                 'dentro de las 24 horas); mantecación; abatimiento a −18 °C en el corazón; conservación a −18 °C o '
                 'menos. DESPUÉS de pasteurizar sólo entra lo que no necesita tratamiento térmico (pastas puras, '
                 'variegatos, fruta lavada en los sorbetes): nunca yema ni nata cruda')
_CARTA = ('carta del caso, precios CON IVA: 1 bola 3,20 €, 2 bolas 4,80 €, 3 bolas 6,00 €, medio litro para llevar '
          '10 €, un litro 18 €, tarta helada de 8 raciones 30 €, crepe o gofre 4,50-5,50 €, chocolate a la taza 3 €, '
          'batido o granizado 4 €')

#: Lo que tiene que contar cada sección (español de España, para el mercado español; research §4 y §6). Cifras del
#: Excel = tokens.
PISTAS = {
    1: 'Qué es el negocio: una heladería artesanal con obrador propio en una ciudad media (150.000-300.000 '
       'habitantes), en una calle comercial de barrio o un paseo junto a un parque o colegios: local de 85 m² con '
       'obrador de 20-25 m², vitrina de 18 cubetas, 20 plazas dentro y una terraza de 5 mesas en temporada, sin '
       'traspaso. Una SL unipersonal con el titular como maestro heladero, un dependiente/a de todo el año y '
       'fijos discontinuos de temporada. Abre en MARZO (el Mes 1 del Excel es marzo) para llegar al primer invierno '
       'con la caja del verano, y en invierno sigue abierta con crepes y gofres, chocolate, tartas y turrón helado '
       'por encargo y helado para restaurantes, con tres semanas de cierre en enero. Cifras clave por token: '
       '{CLIENTES_DIA} clientes al día de media a {TICKET} por persona sin IVA y {DIAS_APERTURA} días de apertura, '
       'ventas {VENTAS_A1}, resultado neto {NETO_A1}, inversión {INVERSION_TOTAL} (de la que {INVERSION_PARTIDAS} '
       'son obra, maquinaria y puesta en marcha), préstamo {PRESTAMO} y equilibrio en {BE_CLIENTES_DIA} clientes al '
       'día. Qué contiene el kit: este plan de negocio de 10 secciones, el Excel del plan financiero de 9 hojas, el '
       'checklist de apertura de 80 tareas en 6 fases y la guía de equivalencias para Latinoamérica.',
    2: 'Tipos de heladería y por qué este: con obrador propio (el de este plan), vitrina sin obrador (compra el '
       'helado hecho), quiosco de temporada y franquicia; cada uno con otra inversión, otra licencia y otro margen. '
       'La propuesta: helado elaborado cada día en el obrador, 18 sabores en verano y 10-12 en invierno, clásicos, '
       'de temporada y alguno de autor, sorbetes sin lácteos; denominaciones honestas («helado crema», «mantecado», '
       '«sorbete» sólo si la receta cumple el art. 3 del RD 618/1998) y «ELABORACIÓN PROPIA» en lugar de «artesano» '
       'si no tienes la calificación artesanal de tu comunidad; alérgenos resueltos. La ' + _CARTA + '. La venta: '
       'mostrador (bola, copa, cucurucho) 58 % del total, para llevar y tartas heladas 17 %, invierno 10 %, '
       'restaurantes y eventos 5 % y cafetería y bebidas 10 %. El ticket de {TICKET} es por persona y sin IVA ({TICKET_IVA} '
       'con IVA): un tique de caja de unos 7 € sin IVA es de 1,45 personas de media. El invierno: crepes y gofres '
       '(sólo si la ordenanza permite la salida de humos; si no, chocolate, tartas y turrón), chocolate a la taza, '
       'tartas y turrón helado de Navidad por encargo, helado para restaurantes y catering de helado.',
    3: 'Mercado en España con fuente (MAPA, nota de prensa del 12 de agosto de 2026, datos de junio de 2025 a mayo de '
       '2026): los hogares compraron 151,97 millones de litros de helado (+11,7 %) por 762,68 millones de euros '
       '(+16,3 %), a 5,02 € el litro de media (4,77 € en el supermercado y 7,72 € en la tienda tradicional), 3,23 '
       'litros y 16,20 € por persona; el supermercado se lleva el 87,6 % del volumen. Fuera del hogar, 31,24 millones '
       '(+5,2 %), 0,87 por persona y año en unas 7 ocasiones, sobre todo en el segundo y el tercer trimestre. El 81,6 % '
       'del volumen de los hogares se consume de abril a septiembre: julio el 20 %, junio el 17,8 % y agosto el '
       '17,1 %. Precio de la bola: de 2 a 4 €, hasta 6 € en las gourmet (prensa local, mayo de 2026). Búsquedas '
       'mensuales en Google España (DataForSEO, octubre de 2026): «heladería artesanal» 2.400 (5.400 en el pico del '
       'verano), «helado artesanal» 590, «mantecadora» 210, «franquicia heladería» 170 y apenas 20 «cómo montar una '
       'heladería» y 10 «plan de negocio heladería»: el que va a abrir busca poco y decide con datos. La '
       'estacionalidad del plan, con el Mes 1 en marzo: de abril a septiembre el 73 % de la venta (menos que el 81,6 % '
       'de los hogares, porque el invierno vende crepes, chocolate y Navidad), pico en julio y valle en enero. El '
       'hueco: nadie publica un plan español con Excel vivo; lo que hay son guías de blog o planes latinoamericanos '
       'en PDF. NADA de tamaños de mercado sin fuente.',
    4: 'Competencia por categorías, sin nombres de empresas ni cifras inventadas: el helado industrial del '
       'supermercado (87,6 % del volumen de los hogares, a 4,77 € el litro frente a 7,72 € en la tienda tradicional, '
       'MAPA); las franquicias de helado; otras heladerías artesanas del barrio o del centro; heladerías de estilo '
       'italiano que venden «gelato»; cafeterías y pastelerías que sirven helado comprado; quioscos de temporada; las '
       'plataformas de reparto con marcas de helado. Dónde gana este concepto: obrador a la vista y helado del día, '
       'sabores de temporada, denominaciones honestas, «ELABORACIÓN PROPIA» con razón, invierno con tartas y Navidad, '
       'y venta a restaurantes de la zona. El riesgo: la guerra de precios de la bola y el súper en casa; cómo se '
       'defiende (producto, experiencia, tarrina para llevar, encargos).',
    5: 'Marketing de temporada: apertura en marzo con degustación para el barrio, colegios y comercios; redes sociales '
       'con el sabor del día y el obrador en directo; ficha de Google Business con el horario de cada temporada y '
       'respuesta a las reseñas; encargos de tartas heladas (comuniones en mayo, cumpleaños, Navidad) y turrón '
       'helado; tarrinas de medio litro y de litro por plataforma de reparto las noches de verano (un {DELIVERY_PCT} '
       'de las ventas, con una comisión del {COMISION_DELIVERY}); helado para restaurantes de la zona; fidelización '
       'sencilla (tarjeta de sellos o club de sabores) sin cifras de conversión inventadas. Presupuesto de marketing '
       '{MARKETING_ANO} al año más la marca, la web, las fotos y el lanzamiento, que van en la inversión. El primer '
       'invierno se trabaja desde septiembre: carta de invierno y encargos de Navidad.',
    6: 'Operaciones del obrador y del mostrador. El proceso en ESTE orden, tal cual: ' + ORDEN_PROCESO + '. El '
       'equipo, con precio y fuente: pasteurizador de 30 litros {PASTEURIZADOR} (14.601,75 € sin IVA en la tarifa de '
       'un distribuidor, octubre de 2026), mantecadora horizontal de 6-12 litros por ciclo {MANTECADORA} (las marcas '
       'profesionales no publican tarifa; una vertical de entrada de 26-30 l/h cuesta unos 4.200 € sin IVA), abatidor '
       '{ABATIDOR}, armarios de conservación y maduración {ARMARIOS} y vitrina ventilada de 18 cubetas {VITRINA} (dos '
       'módulos de 10 cubetas a unos 5.090 € cada uno en la tarifa del fabricante). La capacidad: unos 7.150 kg de '
       'helado al año (unos 10.500 litros); en julio, unos 38 kg al día, unas 11 cubetas de 5 litros, con un ciclo '
       'diario del pasteurizador y 6-7 ciclos de mantecadora: la vitrina de 18 cubetas deja holgura para tartas y '
       'restaurantes. Densidad: 430 g por litro como mínimo legal (RD 618/1998); el artesano suele ir a 0,6-0,75 kg '
       'por litro. Vitrina a la temperatura que fije tu APPCC (ninguna norma estatal la fija; −11/−14 °C es lo '
       'habitual); conservación a −18 °C o menos y sin recongelar. Contacto cruzado: una espátula por cubeta y '
       'lavaporcionador con agua corriente. Horario: temporada alta (de mediados de abril a septiembre) de 12:00 a '
       '24:00 todos los días; marzo, primera quincena de abril y octubre, 8 horas y seis días; de noviembre a '
       'febrero, 6 horas entre semana y más el fin de semana, cerrada los lunes y tres semanas de cierre de mediados '
       'de enero a primeros de febrero. Potencia: unos 30 kW en trifásica (cada módulo de vitrina gasta unos 23 kWh '
       'al día); suministros {SUMINISTROS_MES} al mes de media. Merma del 5-8 % de la producción; mantenimiento con '
       'frigorista certificado ({MANTENIMIENTO_FRIO} al año); envases sin poliestireno expandido y cucharillas de '
       'madera o compostables.',
    7: 'Equipo: el titular maestro heladero a jornada completa; un dependiente/a y encargado/a de turno todo el año; '
       'un dependiente/a de temporada fijo discontinuo de abril a septiembre a jornada completa; uno de verano fijo '
       'discontinuo de junio a septiembre de 30 horas; un ayudante de obrador fijo discontinuo de mayo a septiembre '
       'a media jornada; y suplencias de vacaciones y descansos: {PLANTILLA_PERSONAS} personas y {JORNADAS} jornadas '
       'completas equivalentes, coste {PERSONAL_A1} ({PERSONAL_PCT_A1} de las ventas), cobertura de horas '
       '{COBERTURA_HORAS} ({HORAS_CONTRATADAS} horas contratadas frente a {HORAS_NECESARIAS} necesarias); en julio y '
       'agosto el cuadrante va justo: el titular hace horas de más o entra un extra de fin de semana. Contrato fijo '
       'discontinuo por escrito con llamamiento por escrito (art. 16 del Estatuto de los Trabajadores), nunca '
       'autónomos que te facturan (falso autónomo, art. 1.1), registro de jornada (art. 34.9), convenio provincial de '
       'hostelería (VI Acuerdo Laboral de ámbito Estatal para el sector de Hostelería, art. 4, que nombra las '
       'heladerías). Si contratas a menores de 18 años, sin trabajo nocturno ni horas extraordinarias (art. 6 ET): '
       'confírmalo con tu gestoría. Formación de manipuladores acreditada por la empresa (el antiguo carné de '
       'manipulador ya no existe) con temperaturas, alérgenos y el orden de la pasteurización; formación técnica de '
       'balanceo de mezclas; prevención de riesgos (frío, cargas, cortes).',
    8: 'Plan financiero, TODO por token: inversión {INVERSION_TOTAL} = compras {CAPEX} (obra y equipo '
       '{INVERSION_PARTIDAS}, más la fianza {FIANZA} y {RENTA_PREVIA} de renta antes de abrir) + fondo de maniobra '
       '{FONDO_MANIOBRA}; IVA de la inversión {IVA_INVERSION}; necesidad de caja {NECESIDAD_CAJA}; financiación '
       '{RECURSOS_PROPIOS} propios + préstamo {PRESTAMO} al {TIPO_PRESTAMO}, {PLAZO_PRESTAMO} años con {CARENCIA} de '
       'carencia, cuota {CUOTA_ANUAL}. Cuenta de resultados de 3 años: ventas {VENTAS_A1}/{VENTAS_A2}/{VENTAS_A3}; '
       'margen bruto {MARGEN_BRUTO_PCT_A1}; mercancía {MERCANCIA_PCT_A1}; personal {PERSONAL_A1}; alquiler '
       '{ALQUILER_ANO} ({ALQUILER_PCT_A1}); neto {NETO_A1}/{NETO_A2}/{NETO_A3} (el año 3 tributa ya al tipo general '
       'del Impuesto de Sociedades). CRECIMIENTO tal cual lo hace el Excel: suben los clientes un {CREC_A2} y un '
       '{CREC_A3} (de {CLIENTES_DIA} a {CLIENTES_DIA_A2} y {CLIENTES_DIA_A3} al día) con el mismo ticket, y la '
       'plantilla crece con personas, no con un porcentaje. Equilibrio contable {BE_CLIENTES_DIA} clientes al día '
       '(ingresos {BE_INGRESOS}; holgura {HOLGURA_CONTABLE}); equilibrio de caja {BE_CLIENTES_DIA_CAJA} clientes al '
       'día y holgura {HOLGURA_CAJA}, que es la del PRIMER año (sólo intereses por la carencia); desde el segundo, con '
       'la devolución del principal, la holgura baja a {HOLGURA_CAJA_A2} ({BE_CLIENTES_DIA_CAJA_A2} clientes al día de '
       'equilibrio) y en el tercero queda en {HOLGURA_CAJA_A3}: esos años son los que hay que vigilar. DSCR mínimo '
       '{DSCR_MIN}. TESORERÍA: el Mes 1 es marzo; la rampa arranca al {RAMPA_MES1} y llega al ritmo de crucero en '
       '{MESES_RAMPA} meses; el saldo mínimo es {SALDO_MINIMO} en el mes {MES_SALDO_MINIMO} ({MES_SALDO_MINIMO_NOMBRE}) '
       'y el año acaba (febrero) con {SALDO_MES12}; de noviembre a febrero entra alrededor del 15 % de la venta del '
       'año con los fijos planos: el verano paga el invierno, y por eso el plan no abre en otoño. El personal se '
       'reparte en doce meses en la tesorería aunque los fijos discontinuos sólo cobran en temporada: el invierno '
       'sale más caro que en la realidad (lado prudente). Payback del proyecto: {PAYBACK} (el token ya es texto: no '
       'le añadas «años»). Escenarios: pesimista, un verano frío y lluvioso ({ESC_PES_CLIENTES} clientes a '
       '{ESC_PES_TICKET} y {ESC_PES_DIAS} días: ventas {ESC_PES_VENTAS}, neto {ESC_PES_NETO}) y optimista '
       '({ESC_OPT_CLIENTES} clientes a {ESC_OPT_TICKET} y {ESC_OPT_DIAS} días: neto {ESC_OPT_NETO}). Dos alternativas '
       'SIN Excel, razonadas: la variante de ahorro (pasteurizadora-mantecadora combinada o maquinaria de ocasión '
       'revisada, que según las guías publicadas cuesta un 40-60 % menos: la inversión bajaría a unos 90.000 €) y el '
       'cierre de noviembre a febrero (se ahorran meses de personal de mostrador y suministros con el llamamiento de '
       'los fijos discontinuos, pero se pierden la Navidad, los encargos y la clientela de invierno, y se sigue '
       'pagando el alquiler y la cuota del préstamo). El Excel manda: si cambias una celda verde, el documento se '
       'queda atrás.',
    9: 'Marco legal con su cita (sólo esto, dicho así): SL unipersonal (capital desde 1 €) o autónomo; IAE (RDLeg '
       '1175/1990): epígrafe 644.4 «comercio al por menor de helados», que te permite fabricar helado y tartas '
       'heladas en el propio local para venderlos allí, y grupo 676 para el consumo en el local; el 414.4 sólo si '
       'fabricas para otros a escala industrial; exento de cuota con menos de 1 millón de cifra de negocio. Apertura: '
       'el 644.4 está en el anexo de la Ley 12/2012: declaración responsable, sin licencia previa, hasta 750 m² (arts. '
       '2-4); la parte de hostelería (mesas, 676) va por el régimen de tu ayuntamiento (licencia o declaración '
       'responsable según la ordenanza); la terraza es ocupación de la vía pública y nunca entra en la Ley 12/2012 '
       '(art. 2.2): autorización municipal aparte. Sanidad: declaración responsable al registro sanitario de tu '
       'comunidad autónoma (RD 1021/2022); el RGSEAA sólo aplica si sirves a otros negocios fuera del art. 3 del RD '
       '1021/2022, que permite el suministro marginal (el 25 % del volumen anual o 500 kg a la semana como máximo), '
       'localizado y restringido, con declaración responsable y registro de destinatarios, cantidades y fechas; APPCC '
       '(Reglamento (CE) 852/2004 y la flexibilidad del art. 20 del RD 1021/2022); huevo: la mezcla a 70 °C durante 2 '
       'segundos o más (85 °C en la práctica) u ovoproducto (art. 9), y la mezcla con huevo, mantecada en las 24 '
       'horas siguientes (art. 9.3; cómo aplica al helado ya congelado, pregúntalo al inspector); conservación a −18 °C '
       'o menos y sin recongelar (arts. 4.1 y 5.9); la temperatura de la vitrina no la fija ninguna norma estatal, la '
       'fija tu APPCC. Denominaciones (RD 618/1998, vivo sólo en eso, arts. 2, 3 y 17.1): «helado crema», «helado de '
       'leche», «sorbete», «mantecado» con un 4 % de yema o más, «granizado», y 430 g por litro como mínimo; '
       '«artesano» sólo con el documento de calificación artesanal de tu comunidad (art. 2.9); «ELABORACIÓN PROPIA» '
       'es la mención segura, sólo en el local donde se elabora o en sus sucursales (RD 1021/2022, art. 11). '
       'Alérgenos a granel por escrito o de palabra con registro escrito y cartel (RD 126/2015, arts. 4 y 6) y '
       'etiqueta completa en las tarrinas preenvasadas (art. 5). IVA: 10 % todo el helado, en el local o para llevar '
       '(Ley 37/1992, art. 91.Uno.1.1.º y 2.2.º); los refrescos con azúcares añadidos para llevar, al 21 %. Personal: '
       'ET arts. 1.1, 16 y 34.9 y el convenio provincial de hostelería (ALEH VI, art. 4). Facturación con software '
       'Veri*factu (consulta la fecha que te aplica con tu gestoría). La carga de gases refrigerantes, sólo por un '
       'técnico certificado. Lo que no esté aquí no se afirma: «compruébalo con tu gestor o con el inspector».',
    10: 'Conclusiones con tokens (viabilidad, holgura del año 1 y de los años 2 y 3, DSCR mínimo, saldo mínimo, '
        'payback), los riesgos de una heladería y cómo se mitigan: abrir en otoño; la caja del invierno sin plan de '
        'invierno; el local equivocado (monofásico, sin ventilación para los condensadores ni desagüe, sin salida de '
        'humos para las crepes); una vitrina sobredimensionada (24 cubetas son merma y consumo); mermas y averías del '
        'frío en agosto (seguro con deterioro de mercancía y contrato con frigorista); el clima (un verano frío y '
        'lluvioso es el escenario pesimista); materias primas que se disparan (pistacho, cacao, vainilla: escandallo y '
        'precio revisados cada temporada); «artesano» sin papeles y «elaboración propia» con helado comprado; '
        'contratar el verano con eventuales o «autónomos» en vez de fijos discontinuos; alérgenos en el '
        'lavaporcionador; recetas sin balancear. El plan de acción en 6 fases del checklist (80 tareas: '
        '12/15/15/12/13/13). Cierra con el siguiente paso: completar el Excel con tus cifras.',
}

#: Prohibidos en el texto (SPEC D12): sellos y palabras vetadas, restos del molde FT y de la panadería, y frases que
#: contradicen el caso o la ley. Los usa también `barrido_es.py` sobre los xlsx y el docx.
PROHIBIDOS = [
    r'\bfreelance', r'validad[oa]s?', r'Espa[ñn]a,? 2026', r'food ?truck', r'\bcami[oó]n\b', r'ventanilla',
    r'generador', r'aparcamiento', r'carn[eé]t? de manipulador(?! ya no existe)', r'tarifa plana', r'\bCNAE\b',
    r'(?<!inscrito en el )\bRGSEAA\b(?!.{0,80}(s[oó]lo|otros (establecimientos|negocios)))', r'licencia de apertura',
    r'versi[oó]n (1\.1|2\.2|anterior)', r'\bv1\.1\b', r'solopreneur',
    r'panader', r'\bpan\b', r'boller', r'harina', r'masa madre', r'hornada', r'horno de pisos', r'amasad',
    r'levadura', r'madrugada', r'pan com[uú]n', r'superreducido', r'transacci',
    r'12-22 ?%', r'28-35 ?%', r'10-18 ?%', r'12-18 ?%', r'70-80 ?%',
]
#: Cifras que el texto puede llevar escritas (normas, research con fuente, carta y estructura del caso).
PERMITIDAS = set('''0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 20 21 23 24 25 26 30 31 38 40 44 45 50 58 60 70 74 75
80 85 90 91 100 115 126 150 170 210 236 300 375 414.4 430 500 590 618 644.4 676 750 852 1.000 1.021 1.169 1.175 2.400
5.090 5.400 7.150 10.500 14.601,75 4.200 90.000 150.000-300.000 300.000 2026 2025 2027 2023 2022 2020 2015 2012 2011
2010 2004 2002 1998 1995 1992 1990 2.9 2.2 3.3 3.5 3.6 4.1 5.9 9.3 34.9 1.1 2,5 3,20 4,80 6,00 4,50-5,50 4,77 5,02 7,72
11,7 16,3 3,23 16,20 87,6 31,24 5,2 0,87 81,6 17,8 17,1 151,97 762,68 0,6-0,75 2-4 4-12 40-50 26-30 6-12 6-7 10-12
20-25 40-60 5-8 1,45 12/15/15/12/13/13 −11/−14 −18 −20/−25 +2/+4 12:00 24:00 1,5'''.split())
RX_NUM = re.compile(r'(?<![\w{])[−+]?\d[\d.,/:−-]*\d|(?<![\w{])\d')
#: Avisos de seguridad (SPEC D11): grasa, nata o yema DESPUÉS de pasteurizar (la errata del Kit ES del 24-oct).
RX_ERRATA = re.compile(r'(yemas?|nata|grasas?)[^.;]{0,50}(despu[eé]s|tras) (de )?pasteuriz', re.I)
#: Caracteres admitidos además del latín básico/extendido: tipografía española y los signos de temperatura (−, ≤, ≥).
RX_RARO = re.compile(r'[^\x00-ɏ‐-‧€°→ ‑«»¿¡ºª·…–—“”‘’−≤≥²]')


def ranuras():
    d = json.load(open(os.path.join(BP4, 'docx_es_cat.json'), encoding='utf-8'))['parrafos']
    gem = {}
    for t in ('par_es_a', 'par_es_b'):
        gem.update(json.load(open(os.path.join(GEMELA, t + '.json'), encoding='utf-8')))
    fuera = []
    for k in sorted(d, key=int):
        v = d[k]
        if v['rol'] != 'cuerpo':
            continue
        sec = int(v['seccion'])
        fuera.append({'i': int(k), 'seccion': sec, 'palabras_objetivo': int(v['palabras']),
                      'molde_ft_es': v['texto'], 'gemela_formato_parrillero_es': gem.get(k, '')})
    return fuera


def preparar():
    cif = json.load(open(CIFRAS, encoding='utf-8'))['tokens'] if os.path.exists(CIFRAS) else {}
    os.makedirs(TANDAS, exist_ok=True)
    rs = ranuras()
    for tanda, secs in (('hel_es_a', range(1, 6)), ('hel_es_b', range(6, 11))):
        sel = [r for r in rs if r['seccion'] in secs]
        ent = {
            'tanda': tanda, 'producto': 'Plan de Negocio: Heladería Artesanal ES 1.0 (aichef.pro, 35 €)',
            'salida': 'scripts/productos-digitales/plan-heladeria/textos/%s.json' % tanda,
            'formato_salida': '{"<i>": "<párrafo en español>", …} con TODOS los "i" de "parrafos" y nada más',
            'brief': 'scripts/productos-digitales/plan-heladeria/BRIEF-REDACTORES.md (léelo entero antes)',
            'research': RESEARCH + ' (§1 normativa, §3 caso, §4 SERP, §6 errores y riesgos: material de apoyo; '
                                   'la pista de la sección manda)',
            'orden_del_proceso (SPEC D11, literal en el fondo)': ORDEN_PROCESO,
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
        if RX_ERRATA.search(t):
            avi.append('%d: ¿grasa, nata o yema DESPUÉS de pasteurizar? (SPEC D11) «%s»' % (
                r['i'], RX_ERRATA.search(t).group(0)))
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
