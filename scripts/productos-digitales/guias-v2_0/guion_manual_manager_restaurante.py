#!/usr/bin/env python3
"""
guion_manual_manager_restaurante.py — GUION del «Manual del Manager de
Restaurante» v1.0 (SPEC `manual-manager-SPEC.md`, §4 y §4.2).

Mismo esquema que el representante de la familia
(`guion_guia_food_cost_ingenieria_menu.py`, de ayer): un capítulo no se le pide
a un redactor con un título, se le pide con un guion CERRADO. Por capítulo van
(a) el objetivo, (b) 4-6 epígrafes, (c) las **cifras del propio producto**
citadas por `fichero.xlsx!Hoja!Celda` —que `documentos.py` resuelve con openpyxl
`data_only` antes de escribir el prompt, así que el redactor recibe el NÚMERO,
no el fichero—, (d) los datos del sector por `id` de
`auditorias/guias-v2-research-sector.json` (ids `MM-*`; la entrada sin `cifra`
llega al prompt como «REGLA SIN CIFRA» y se escribe sin número, no como hueco),
(e) las tablas exigidas —que las construye el maquetador desde el xlsx, no el
redactor—, (f) el presupuesto de palabras y (g) lo que NO debe decir.

NOVEDAD DE LA LÍNEA (John, 2026-09-04): el texto de los productos digitales ya
NO lo escribe `bridge.py`. `dump_prompts.py` vuelca los prompts exactos que
construye `documentos.py` y un subagente Anthropic escribe cada bloque en la
caché `txt/`, verificándolo con `check_bloque.py`. Este guion gobierna esa
prosa: es lo único que separa 54 bloques escritos por 54 agentes de 54 textos
que no dicen lo mismo.

FUENTE ÚNICA DE CIFRAS (SPEC §7-bis.7 de la familia): los SIETE libros de
`astro-site/public/dl/manual-manager-restaurante/`, que se LEEN y no se tocan.
Mientras el producto no esté copiado a producción viven en
`scripts/productos-digitales/manual-manager/build/`, y sus mapas de celdas
(`mapa-*.json`) son el contrato: toda coordenada de este guion sale de ahí o
está verificada abriendo el libro con `data_only`. El juego de datos del caso
modelado es `manual-manager/datos_ejemplo.py` (D13).

Presupuesto (SPEC §4 y D17): 20 capítulos, 85 páginas prometidas, 30.000
palabras objetivo, 1.400-1.600 palabras por capítulo (el 11 y el 19 llevan
1.800 por cargar la matriz de jornada y el bloque entero de seguridad
alimentaria y local). Bonus: 12 situaciones resueltas de 600-660 palabras,
7.500 palabras y 25 páginas prometidas.

DECISIONES QUE ESTE GUION MATERIALIZA (no se reabren aquí): D1 (ancla externa
homogénea: Last.app Growth 1.140 €/año sin IVA, sin plan Starter y sin
porcentaje), D4 (el libro legal absorbe topes, permisos y régimen
disciplinario, y el cap. 01 dice qué es del pack y qué es cross-sell), D5
(cotización empresarial completa, y el 23,60 % es sólo contingencias comunes),
D6 (permiso parental: DOS figuras), D7 (organigrama con el ALEH VI real), D8
(las correcciones legales de la refutación), D9 (INE con su etiqueta exacta),
D10 (las citas acotadas en la propia frase; el 65 %/55 % como criterio de la
casa), D11 (lista negra ampliada), D12 (cada tabla legal con «Verificado el
04-09-2026 · norma · URL»), D13 («La Encina», caso modelado), D19 (`tipo_doc` y
`categoria_doc` de manual), D22 (el marco legal es español y se dice).

Via: Claude Code
"""

PID = 'manual-manager-restaurante'

# --------------------------------------------------------------------------
# Cabecera del documento
# --------------------------------------------------------------------------
BIO = (
    'John Guerrero es CEO de AI Chef Pro y fundador de ChefBusiness Group. En '
    'cocina desde los 17 años y consultor gastronómico desde 2010, ha asesorado '
    'la apertura de más de 200 establecimientos, incluidos restaurantes con '
    'Estrella MICHELIN y Soles Repsol en España y Europa. Más sobre su trabajo '
    'en johnguerrero.es.')

LEGAL = (
    '*Este manual es un documento de trabajo profesional, no un dictamen '
    'laboral, fiscal, jurídico ni de prevención de riesgos. El marco normativo '
    'que se explica es el ESPAÑOL, y su estado se verificó contra el Boletín '
    'Oficial del Estado el 4 de septiembre de 2026, incluida la modificación '
    'del ALEH VI publicada ese mismo día: cada afirmación legal lleva su norma '
    'y su artículo para que puedas comprobarla y para que sepas dónde mirar '
    'cuando cambie. Los plazos, tipos de cotización, umbrales y periodicidades '
    'viven en celdas editables de las hojas de cálculo precisamente porque '
    'cambian, y porque fuera de España cambian del todo: si cambia el dato, se '
    'cambia la celda y todo el libro se recalcula. Los salarios, costes, '
    'importes y porcentajes son valores de ejemplo de un restaurante modelado '
    'que acompaña a este pack y sirven para que los sustituyas por los tuyos: '
    'ninguno es una previsión de tus resultados. La calificación de un caso '
    'concreto —si un contrato está bien causado, si una falta es grave o muy '
    'grave, si una obligación te alcanza— depende de los hechos de ese caso y '
    'del convenio provincial que te aplique. Antes de firmar un contrato, '
    'sancionar, despedir o cambiar la forma en la que facturas, contrasta con '
    'tu asesoría laboral y fiscal.*')

GUIA = {
    'pid': PID,
    'titulo': 'Manual del Manager de Restaurante',
    'subtitulo': 'Operaciones, personas, números, servicio y ley — el criterio '
                 'del día a día, verificado contra el BOE',
    'autor_linea': 'John Guerrero · AI Chef Pro · aichef.pro',
    'cabecera': 'AI Chef Pro · Manual del Manager de Restaurante',
    'fecha': 'septiembre de 2026',
    'version': '1.0',
    'tipo_doc': 'manual',
    'tipo_doc_art': 'del manual',  # «un tramo del capítulo … del manual profesional» (prompt_bloque)
    'tipo_doc_dem': 'este manual',
    'categoria_doc': 'Manual profesional',
    'bio': BIO,
    'legal': LEGAL,
    'portada_texto': (
        '20 capítulos, 7 herramientas en Excel con fórmulas vivas y un bonus de '
        '12 situaciones resueltas para dirigir un restaurante que ya está '
        'abierto: los números de la semana, el equipo, el servicio y la ley que '
        'te obliga hoy. No es un manual de apertura ni otro paquete de '
        'checklists: es el criterio que decide qué se hace con lo que sale de '
        'ellos. Todas las cifras del caso salen de los libros de este mismo '
        'pack, así que el texto y las hojas de cálculo dicen lo mismo; y cada '
        'afirmación legal va con su norma, su artículo y su enlace, verificados '
        'contra el Boletín Oficial del Estado el 4 de septiembre de 2026.'),
    'gates': {
        'paginas_prometidas': 75,  # 2026-09-05: medidas 77 (~530 palabras/página en esta plantilla)
        'palabras_objetivo': 30000,
        'min_palabras_cap': 1200,
        # Cifras con separador de miles que el texto puede escribir y que NO
        # están en ninguna celda de los siete libros ni en el research. Se
        # admiten UNA A UNA y por SIGNIFICADO (lección RD-21 del representante:
        # que las celdas existan no basta para dar por buena una derivada).
        #  · 1.140 € = coste anual, por local y sin IVA, del plan Growth de
        #    Last.app, precio oficial. Es la ÚNICA ancla externa autorizada por
        #    la decisión D1 de la SPEC para explicar por qué un pago único de
        #    55 € no se compara con una suscripción. No sale de ninguna celda
        #    porque no es un dato del pack: es el precio de mercado contra el
        #    que se contrasta. El plan Starter, la horquilla «1.140-2.100» y
        #    cualquier porcentaje de comparación están PROHIBIDOS (D11).
        # No se admite ninguna más: todas las demás cifras con separador de
        # miles que necesita este manual (SMI y su cómputo anual, tope de base
        # de cotización, tramos de sanción de la LISOS, de la Ley 17/2011, del
        # TRLGDCU, de la Ley 37/2003 y de la Ley 1/2025, los 1.300 m², las
        # tablas salariales provinciales y las series del INE) llegan por su
        # ficha `MM-*` del research, y `valores_admitidos()` ya las da por
        # buenas leyendo el JSON.
        'cifras_extra': ('1.140', '1.140,00'),
        'cifras_ignorar': (),
        # «la semana cierra con un prime cost del 71 %» no es mortalidad de
        # restaurantes: es contabilidad. Ninguna otra formulación se admite —
        # este manual NO escribe cifras de cierre ni de fracaso (NO_COMUN).
        'mortalidad_permitida': ['cierra', 'cierran'],
        # Se hereda la lista de ayer y se completa al final del fichero con el
        # vocabulario propio de este manual.
        'erratas_permitidas': ('actas', 'canta', 'cantó', 'canto', 'atendió', 'atendio', 'desapareció', 'desaparecio', 'rendía', 'rendia', 'alegar', 'anular', 'auditado', 'califica', 'cometido', 'contó', 'conto', 'digan', 'emitió', 'emitio', 'escribirá', 'escribira', 'fisco', 'libren', 'manía', 'mania', 'ofreció', 'ofrecio', 'proporcionales', 'vicio', 'ocurrió', 'ocurrio', 'acusa', 'acusando', 'señalado', 'senalado', ),
    },
}

# --------------------------------------------------------------------------
# Los siete libros del pack (SPEC §2.2). Se referencian por NOMBRE de fichero:
# documentos.py los busca en astro-site/public/dl/<pid>/.
# --------------------------------------------------------------------------
X_SEM = 'cuadro-de-mando-semanal-manager.xlsx'
X_POLI = 'matriz-formacion-polivalencia.xlsx'
X_QUEJ = 'quejas-reclamaciones-resenas.xlsx'
X_SEL = 'seleccion-scorecard-entrevista.xlsx'
X_LEG = 'calendario-cumplimiento-legal.xlsx'
X_REU = 'reuniones-acuerdos-plan-90-dias.xlsx'
X_AUD = 'auditoria-interna-servicio.xlsx'

# Pie obligatorio de toda tabla que fije un dato legal (SPEC D12).
V_ET = 'Verificado el 04-09-2026 · Art. 34.9 y concordantes del Estatuto de los Trabajadores (RDLeg 2/2015) · https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430'
V_ALEH = 'Verificado el 04-09-2026 · ALEH VI (BOE-A-2023-6344), modificado por la Resolución de la DGT de 25-08-2026 (BOE-A-2026-18630) · https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-18630'
V_COTIZA = 'Verificado el 04-09-2026 · Orden PJC/297/2026, de 30 de marzo, arts. 4, 16 y 33.2, y disposición adicional 61.ª del TRLGSS · https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-7296'
V_TEMP = 'Verificado el 04-09-2026 · Art. 30 del RD 1086/2020 en la redacción del RD 1021/2022, y art. 8.1 del RD 1021/2022 · https://www.boe.es/buscar/act.php?id=BOE-A-2020-15872'


def C(etiqueta, ref, fmt='eur2'):
    return (etiqueta, ref, fmt)


# --------------------------------------------------------------------------
# Prohibiciones transversales: van en TODOS los capítulos y en las 12
# situaciones del bonus. Son, en este orden: (1) higiene de citación legal,
# (2) régimen de cifras, (3) la LISTA NEGRA íntegra de la SPEC §8 —que es el
# §11 de la síntesis del research más los añadidos de la refutación—,
# (4) el ámbito del producto y (5) el vocabulario de la D12 y de la D22.
# --------------------------------------------------------------------------
NO_COMUN = [
    # ---- 1. Higiene de citación legal ------------------------------------
    'Las letras y apartados de un artículo de ley se escriben «letra g» o '
    '«apartado 2», NUNCA «g)» ni «2)»: un paréntesis de cierre suelto se lee '
    'como una errata.',
    'Los números de las normas y las referencias del BOE se copian TAL CUAL, '
    'sin separador de miles: se escribe «RD 1021/2022», «RD 1086/2020», '
    '«RD 1619/2012», «Ley 31/1995» y «BOE-A-2026-18630»; nunca '
    '«RD 1.021/2022» ni «BOE-A-2026-18.630».',
    'TODA afirmación legal va con su norma y su artículo la primera vez que '
    'aparece en el capítulo («el art. 34.9 del Estatuto de los Trabajadores»), '
    'nunca «es obligatorio» a secas. Y cuando la norma sea una de las '
    'verificadas para esta edición, se dice expresamente «verificado el 4 de '
    'septiembre de 2026».',
    # ---- 2. Régimen de cifras --------------------------------------------
    'NO escribas ningún importe, coste, salario, porcentaje, plazo, umbral ni '
    'sanción que no esté en la lista de cifras del producto o en los datos del '
    'sector que te doy. Ni «ronda los», ni «suele estar en», ni un ejemplo '
    'inventado para ilustrar. Si necesitas un número, es uno de los que tienes; '
    'si no lo tienes, la frase se escribe sin número.',
    'NO hagas cuentas nuevas con las cifras que te doy: no sumes, no restes, no '
    'calcules porcentajes y no proyectes a doce meses para escribir un total '
    'que no te he dado. Los totales ya están calculados en los libros.',
    'NO cites ninguna encuesta, informe ni estudio del sector que no venga en '
    'los datos del sector de este capítulo. En particular, NO escribas ningún '
    'porcentaje atribuido a TheFork, ManpowerGroup, Square, American Express, '
    'Randstad, Synergie, Linkers, Delectatech, Circana, CoverManager o '
    'CaixaBank que no te haya llegado con su ficha y su fuente: para este '
    'documento esas cifras no están verificadas y no existen.',
    # ---- 3. Lista negra (SPEC §8) — cifras -------------------------------
    'PROHIBIDO escribir ninguna cifra de cierre, quiebra, fracaso o mortalidad '
    'de restaurantes, NI SIQUIERA PARA NEGARLA O DESMENTIRLA. No existe «el '
    '60 % de los restaurantes cierra»: no hay fuente oficial de mortalidad de '
    'restaurantes en España. Lo único que se puede escribir es la serie de '
    'SUPERVIVENCIA del INE, en positivo («sobrevive el tanto por ciento a los N '
    'años»), con su etiqueta exacta y con la cohorte y el año; nunca dada la '
    'vuelta como «no sobrevive», «desaparece» o «fracasa».',
    'PROHIBIDO escribir que «el 63,5 % de las empresas de hostelería cierra a '
    'los tres años»: el 63,5 % es la tasa de supervivencia a los DOS años y de '
    'TODAS las actividades. La serie de hostelería es otra y llega, si toca, en '
    'los datos del sector.',
    'PROHIBIDO escribir la tasa de rotación del 63,8 % en hostelería y el coste '
    'de reemplazar a un empleado de 2.800 a 5.000 euros: el informe original no '
    'está publicado y en el propio research aparece con dos emisores distintos. '
    'La rotación y el coste de una baja se calculan con los datos del lector, '
    'que para eso está la herramienta.',
    'PROHIBIDO atribuir a la hostelería la cifra de absentismo del «sector '
    'servicios»: el dato de hostelería existe, es del INE y es otro; sólo se '
    'escribe si te llega en los datos del sector.',
    'PROHIBIDO dar un «salario del gerente de restaurante» como cifra única: '
    'las fuentes van de 18.000 a 95.200 euros al año y ninguna explica la '
    'diferencia. Si hay que hablar de sueldo, se remite al convenio provincial '
    'y a REGCON.',
    'PROHIBIDO presentar el prime cost del 60-65 % como dato español ni '
    'atribuirlo a Toast: es una convención de Estados Unidos. El umbral de '
    '65 % con servicio en mesa y 55 % en barra o autoservicio es CRITERIO DE LA '
    'CASA derivado de la estructura de costes de referencia, y hay que '
    'presentarlo así, con esas palabras.',
    'PROHIBIDO comparar el precio de este manual con «un mes del plan Starter» '
    'de ningún software, y prohibido escribir ningún porcentaje del tipo «5,7 %» '
    'como proporción entre el precio del manual y el de una suscripción. La '
    'única comparación autorizada es el coste anual del plan Growth, por local '
    'y sin IVA, frente a un pago único.',
    'PROHIBIDO mezclar en la misma frase o en la misma tabla las cifras del INE '
    'con las de la patronal Hostelería de España: son metodologías distintas, y '
    'un recuento de EMPRESAS del directorio no es lo mismo que un recuento de '
    'LOCALES.',
    'PROHIBIDO escribir cifras de la Inspección de Trabajo y Seguridad Social '
    '(porcentaje de infracciones que se lleva la hostelería, puestos '
    'irregulares aflorados, trabajadores afectados por horas extra no pagadas): '
    'no se pudieron verificar en la memoria original.',
    'PROHIBIDO dar tarifas en euros al mes de la SGAE o de AGEDI-AIE, un ticket '
    'medio de alta cocina, márgenes por segmento de restauración o cubiertos '
    'por camarero: ningún organismo los publica en España.',
    'PROHIBIDO dar una cifra única de coste de personal, de nómina o de '
    'recargo sobre el salario bruto para Hispanoamérica: cambia enormemente de '
    'un país a otro, y por eso en las herramientas es una casilla editable.',
    # ---- 3-bis. Lista negra (SPEC §8) — normativa ------------------------
    'PROHIBIDO escribir que la jornada máxima es de 37,5 horas: esa reducción '
    'fue rechazada y no está vigente. Lo que rige es el máximo de 40 horas '
    'semanales de promedio en cómputo anual.',
    'PROHIBIDO escribir que el registro de jornada tiene que ser digital, que '
    'ya existe un sistema homologado obligatorio o que operar sin él es '
    'sancionable: ese real decreto NO está publicado en el BOE. Lo exigible es '
    'el registro diario del art. 34.9 del Estatuto de los Trabajadores, que '
    'admite papel o una hoja de cálculo. Y prohibido citar multas por ese '
    'concepto.',
    'PROHIBIDO escribir que Verifactu obliga en 2025 o en 2026, y prohibido '
    'decir que habrá que emitir una factura electrónica por cada mesa: las '
    'facturas simplificadas quedan fuera de la factura electrónica entre '
    'empresas, salvo las cualificadas.',
    'PROHIBIDO citar el RD 3484/2000 para las temperaturas y el RD 1420/2006 '
    'para el anisakis: los dos están derogados desde el 22 de diciembre de '
    '2022. Prohibido citar el RD 3250/1983 de perros guía, derogado el 17 de '
    'junio de 2025. Y prohibido citar un «RD 830/2022 de biocidas», que no '
    'existe.',
    'PROHIBIDO escribir que la posibilidad de llevarse la comida sobrante '
    'obliga desde la Ley 1/2025 o desde el 15 de diciembre de 2022: obliga '
    'desde el 22 de diciembre de 2022, por el art. 18.5 del RD 1021/2022, y '
    'tiene una excepción para el bufé libre y los formatos en los que la comida '
    'no está limitada.',
    'PROHIBIDO escribir que un restaurante de menos de 1.300 metros cuadrados '
    'está exento de la Ley 1/2025: la exención alcanza sólo a UNO de los '
    'apartados de su art. 6; los demás obligan a todo restaurante que no sea '
    'microempresa.',
    'PROHIBIDO escribir que se aplica el ALEH V: el vigente es el VI, y se '
    'modificó el 4 de septiembre de 2026. Y prohibido decir que el ALEH '
    'tipifica los cargos de «encargado», «director» o «administrador»: son '
    'denominaciones de uso de la casa, no categorías del convenio, que clasifica '
    'por áreas funcionales y grupos profesionales.',
    'PROHIBIDO decir que «la Seguridad Social a cargo de la empresa es el '
    '23,60 %»: ese 23,60 % son SÓLO las contingencias comunes. El coste-empresa '
    'completo es el que te llega en los datos del sector y se compone de varias '
    'partidas.',
    'PROHIBIDO decir que el permiso parental es retribuido, y prohibido decir '
    'que no lo es sin distinguir: son DOS figuras distintas que se solapan casi '
    'punto por punto, una no retribuida y otra retribuida, y hay que nombrar '
    'las dos con su artículo. Y prohibido escribir «5 días por fallecimiento»: '
    'son 2 días, ampliables en 2 más si hay desplazamiento; los 5 días son los '
    'de accidente o enfermedad graves, hospitalización o intervención '
    'quirúrgica.',
    'PROHIBIDO escribir que los reconocimientos médicos son obligatorios: son '
    'voluntarios y sólo caben con el consentimiento de la persona, salvo las '
    'excepciones tasadas del art. 22.1 de la Ley 31/1995 y previo informe de la '
    'representación de la plantilla. Y la empresa nunca recibe el informe '
    'médico, sólo las conclusiones de aptitud.',
    'PROHIBIDO escribir que existe el carné oficial de manipulador de '
    'alimentos: se derogó en 2010 y la obligación es del titular de la empresa, '
    'por puesto. Prohibido decir que el cartel de «consulte al personal» basta '
    'para los alérgenos. Prohibido decir que se puede rechazar el efectivo o '
    'que la Ley 18/2022 «Crea y Crece» regula su aceptación: no la menciona.',
    'PROHIBIDO escribir que se puede fumar en las terrazas «con menos de tres '
    'paredes»: el máximo son DOS. Y el proyecto de ley que prohibiría fumar en '
    'todas las terrazas está en tramitación y NO está en vigor: no se escribe '
    'como si ya obligara.',
    'PROHIBIDO citar las consultas vinculantes V3095-17 y V2236-13 de la '
    'Dirección General de Tributos al hablar de propinas: la primera es de '
    'casinos y juegos de azar y la segunda no está verificada para este '
    'documento. Las propinas se explican con la ley del IRPF, con su reglamento '
    'y con lo que dice —y lo que no dice— la norma de cotización, y con nada '
    'más.',
    'PROHIBIDO presentar como obligación legal con periodicidad fija la '
    'limpieza de campana y conductos, la calibración de termómetros, el control '
    'de plagas, la medición del aceite de fritura o la frecuencia de la '
    'formación: ninguna tiene periodicidad fijada por una norma estatal. La ley '
    'exige el RESULTADO, no el calendario, y decirlo así es parte del valor de '
    'este manual.',
    'PROHIBIDO decir que hay que inscribirse en el Registro General Sanitario '
    'de Empresas Alimentarias: a un restaurante que sirve al consumidor final '
    'le basta la comunicación o declaración responsable al registro autonómico, '
    'salvo que supere los umbrales de suministro a terceros.',
    # ---- 4. Ámbito del producto -----------------------------------------
    'NO conviertas esto en un manual de apertura: aquí no se habla de licencia '
    'de actividad, de obra, de inversión inicial, de plan de negocio ni de '
    'financiación. El lector ya tiene el local abierto, la carta puesta y el '
    'equipo contratado; su problema es dirigirlo.',
    'NO expliques desde cero qué es un turno, una comanda, un cuadrante o un '
    'arqueo: esto es para quien YA dirige un restaurante o un turno. La primera '
    'frase de cada bloque asume ese punto de partida. Lo que aporta el capítulo '
    'es el criterio, el caso límite y la decisión, no la definición de oficio.',
    'NO reproduzcas los checklists del Kit de Tareas, ni las plantillas del Kit '
    'de Gestión de Personal, ni los registros del Pack APPCC, ni el escandallo '
    'ni la matriz de carta de la Guía Food Cost: se CITAN por su nombre y se '
    'dice qué resuelven, no se copian. Este manual da el criterio que decide '
    'qué se hace con lo que sale de ellos.',
    'El restaurante del caso es un local MODELADO, «La Encina», no un cliente '
    'real: no escribas que es un caso real, no le pongas ciudad concreta más '
    'allá de la provincia del convenio y no le atribuyas declaraciones a nadie.',
    'No prometas resultados («con este manual bajarás X puntos de prime cost», '
    '«reducirás la rotación»): el manual da método y herramientas, y el '
    'resultado depende de los datos y del negocio del lector. Y no lo presentes '
    'como sustituto de una asesoría laboral, fiscal o de prevención de riesgos.',
    # ---- 5. Vocabulario D12 y ámbito geográfico D22 ----------------------
    'VOCABULARIO OBLIGATORIO (español de España, con la equivalencia de '
    'Hispanoamérica SÓLO la primera vez que el término aparece en el capítulo y '
    'nunca más): «manager (gerente/encargado)», «cuadrante (horario del '
    'personal)», «arqueo (corte de caja)», «nómina (planilla)», «sala (salón)», '
    '«camarero (mesero)». Escrito el paréntesis una vez, el resto del capítulo '
    'usa la forma española a secas. No repitas «manager (gerente/encargado)» '
    'dos veces en el mismo capítulo.',
    'NO uses anglicismos que tengan término español asentado en el oficio: se '
    'escribe «cuadrante», no «schedule»; «rotación», no «turnover»; «coste de '
    'personal», no «payroll»; «reseña», no «review». Sí se usan tal cual, '
    'porque son los del oficio, «food cost», «labor cost», «prime cost», '
    '«briefing», «handover», «no-show», «delivery», «catering» y «scorecard».',
    'El marco legal que se explica es el ESPAÑOL, y hay que decirlo cuando se '
    'entra en materia normativa. Lo que viaja fuera de España es el método y '
    'la herramienta, porque sus parámetros son casillas editables: se remite a '
    '«consulta tu normativa local» en vez de fingir que la regla española vale '
    'en todas partes.',
    'No cites años anteriores a 2026 junto a precios o tendencias. Un año '
    'pasado sólo aparece si va con su norma, su sentencia o su fuente fechada.',
    'No menciones el proceso de edición ni palabras como «maquetador», '
    '«prompt», «instrucciones», «guion» o «capítulo anterior»: el lector compra '
    'un libro, no ve el taller. Tampoco escribas tu propio razonamiento.',
]

# --------------------------------------------------------------------------
# Los 20 capítulos (SPEC §4, con los cambios de su tabla; índice del §8 de la
# síntesis del research). Presupuesto: 1.400-1.600 palabras, 1.800 los caps. 11
# y 19. Suma exacta: 30.000.
# --------------------------------------------------------------------------
CAPITULOS = [
    {
        'n': 1,
        'titulo': 'Qué es Exactamente un Manager de Restaurante (y para Quién es Este Manual)',
        'resumen_indice': 'el organigrama real del convenio, el mapa de problema a capítulo y a herramienta, y qué está en este pack y qué en otro.',
        'palabras': 1400, 'bloques': 2,
        'objetivo': 'Que el lector sepa en cinco minutos si este manual le '
                    'sirve, por dónde entrar según el problema que tenga hoy y '
                    'con qué libro del pack se resuelve cada cosa. Y que sepa '
                    'lo que NO hay aquí —ni apertura, ni checklists nuevos— '
                    'para que no lo busque.',
        'epigrafes': [
            'Gerente, encargado, director, jefe de sala: qué dice el convenio y qué es uso de la casa',
            'El organigrama del ALEH VI: áreas funcionales y grupos profesionales',
            'Tu problema, su capítulo y su herramienta',
            'Qué trae este pack y qué está en los otros productos del catálogo',
            'Cómo llamamos aquí a cada cosa',
        ],
        'puntos': [
            'Resolver el lío de nombres con el convenio en la mano: el ALEH VI '
            'clasifica por áreas funcionales y grupos profesionales, y ahí es '
            'donde encajan «gerente de centro» y «jefe o jefa de restaurante o '
            'sala». «Encargado», «director» y «administrador» son '
            'denominaciones de uso —«administrador» es el término dominante en '
            'Colombia, Chile y Perú—, no categorías del convenio, y hay que '
            'decirlo con esas palabras.',
            'Dejar claro que este manual NO es de apertura y que su lector ya '
            'dirige: el punto de partida es un local abierto, con equipo y con '
            'carta puesta.',
            'Explicar la división del trabajo del catálogo, sin vender humo: el '
            'Kit de Tareas aporta los checklists del día, el Kit de Gestión de '
            'Personal el cuadrante y el control de horas, el Pack APPCC los '
            'registros de seguridad alimentaria y la Guía Food Cost el '
            'escandallo y la carta. Este manual aporta el CRITERIO que decide '
            'qué se hace con lo que sale de todos ellos, y siete herramientas '
            'que ninguno de los otros tiene.',
            'Presentar el restaurante del caso —«La Encina», servicio en mesa, '
            'la plantilla y las estaciones que verá en todos los libros— como '
            'el hilo que recorre el documento, y decir expresamente que es un '
            'caso modelado y no un cliente real.',
            'Anunciar el glosario mínimo con la equivalencia de '
            'Hispanoamérica, y avisar de que el marco legal que se explica es '
            'el español, con las casillas de las herramientas editables para '
            'quien trabaje fuera.',
        ],
        'cifras': [
            C('Tipo de negocio con el que está configurado el pack', f'{X_SEM}!Parámetros!B5', 'txt'),
            C('Personas de la plantilla del caso', f'{X_POLI}!Cobertura por Estación!C27', 'num'),
            C('Estaciones de trabajo del caso', f'{X_POLI}!Cobertura por Estación!C26', 'num'),
            C('Horas de apertura al público de una semana completa', f'{X_SEM}!Parámetros!B37', 'num'),
            C('Ventas netas del año del caso', f'{X_SEM}!Semana!E57', 'eur'),
            C('Cubiertos del año del caso', f'{X_SEM}!Semana!S57', 'num'),
            C('Objetivo de prime cost en vigor en el cuadro de mando', f'{X_SEM}!Parámetros!B13', 'pct0'),
            C('Puntos de control de la auditoría interna de servicio', f'{X_AUD}!Resumen por Área!B16', 'num'),
        ],
        'sector': ['MM-14', 'MM-15'],
        'tablas': [
            {
                'titulo': 'Tu problema, el capítulo que lo trata y la herramienta que lo resuelve',
                'cabecera': ['Si tu problema es…', 'Capítulo', 'Herramienta'],
                'filas': [
                    ['No sé qué números mirar ni cada cuánto', '2 y 3', 'cuadro-de-mando-semanal-manager.xlsx'],
                    ['Vendo y no gano', '4', 'cuadro-de-mando-semanal-manager.xlsx'],
                    ['El día se me va en apagar fuegos', '5', 'auditoria-interna-servicio.xlsx'],
                    ['La caja no cuadra', '6', 'cuadro-de-mando-semanal-manager.xlsx'],
                    ['Mando pero no me siguen', '7', 'reuniones-acuerdos-plan-90-dias.xlsx'],
                    ['No sé qué convenio me aplica', '8', 'calendario-cumplimiento-legal.xlsx'],
                    ['Voy a contratar y me da miedo el contrato', '9', 'calendario-cumplimiento-legal.xlsx'],
                    ['Elijo mal a la gente', '10', 'seleccion-scorecard-entrevista.xlsx'],
                    ['El cuadrante y el registro me tienen frito', '11', 'calendario-cumplimiento-legal.xlsx'],
                    ['Piden un permiso y no sé qué contestar', '12', 'calendario-cumplimiento-legal.xlsx'],
                    ['Se me va la gente y no sé cuánto me cuesta', '13', 'matriz-formacion-polivalencia.xlsx'],
                    ['Tengo que corregir o despedir a alguien', '14', 'calendario-cumplimiento-legal.xlsx'],
                    ['Somos pocos, ¿esto también me obliga?', '15', 'calendario-cumplimiento-legal.xlsx'],
                    ['Cocina y sala están enfrentadas', '16', 'reuniones-acuerdos-plan-90-dias.xlsx'],
                    ['Las quejas y las reseñas me superan', '17', 'quejas-reclamaciones-resenas.xlsx'],
                    ['Reservas que no aparecen', '18', 'quejas-reclamaciones-resenas.xlsx'],
                    ['Viene una inspección y no sé qué me van a pedir', '19', 'calendario-cumplimiento-legal.xlsx'],
                    ['Tengo el diagnóstico y no lo aplico', '20', 'reuniones-acuerdos-plan-90-dias.xlsx'],
                ],
                'nota': 'Los siete libros comparten el mismo restaurante modelado y la misma '
                        'plantilla, así que puedes saltar al capítulo que te interese sin '
                        'perder el hilo de las cifras.',
            },
            {
                'titulo': 'Qué incluye este pack y qué está en otro producto del catálogo',
                'cabecera': ['Lo que necesitas', 'Dónde está', 'Qué hace este manual con ello'],
                'filas': [
                    ['Cuadro de mando semanal, KPI y definiciones', 'En este pack', 'Caps. 2, 3, 4 y 6'],
                    ['Matriz de polivalencia y coste de una baja', 'En este pack', 'Cap. 13'],
                    ['Quejas, reclamaciones formales y reseñas', 'En este pack', 'Caps. 17 y 18'],
                    ['Scorecard de selección y guion de entrevista', 'En este pack', 'Cap. 10'],
                    ['Calendario legal, topes, permisos y régimen disciplinario', 'En este pack', 'Caps. 8, 9, 11, 12, 14, 15, 19 y 20'],
                    ['Reuniones, acuerdos y plan de 90 días', 'En este pack', 'Caps. 7, 16 y 20'],
                    ['Auditoría interna de servicio', 'En este pack', 'Caps. 5 y 20'],
                    ['Checklists de apertura, servicio y cierre', 'Kit de Tareas', 'Se cita en el cap. 5; aquí va el criterio, no la lista'],
                    ['Arqueo de caja diario', 'Kit de Tareas', 'Se cita en el cap. 6'],
                    ['Cuadrante de turnos y control de horas', 'Kit de Gestión de Personal', 'Se cita en el cap. 11'],
                    ['Coste laboral por persona, onboarding, vacaciones y evaluación', 'Kit de Gestión de Personal', 'Se cita en los caps. 4, 10, 12 y 14'],
                    ['Registros de APPCC, limpieza y temperaturas', 'Pack APPCC', 'Se cita en el cap. 19'],
                    ['Escandallo, precios y matriz de carta', 'Guía Food Cost + Ingeniería de Menú', 'Se cita en los caps. 4 y 6'],
                ],
                'nota': 'Este manual no reproduce ninguna de las plantillas de la columna de la '
                        'derecha: las cita por su nombre y explica qué decisión se toma con lo '
                        'que sale de ellas. Quien tenga los dos productos no duplica nada.',
            },
        ],
        'prohibido': None,
    },
    {
        'n': 2,
        'titulo': 'Los Números que Gobiernan tu Turno: las Definiciones que Casi Nadie Distingue',
        'resumen_indice': 'qué mide cada indicador, con qué se confunde y cuál manda en cada decisión.',
        'palabras': 1500, 'bloques': 2,
        'objetivo': 'Que el lector deje de llamar a tres cosas distintas por el '
                    'mismo nombre. Fijar qué mide cada indicador, cuál es el '
                    'error típico que lo estropea y en qué decisión manda cada '
                    'uno, con las cifras del año del caso delante.',
        'epigrafes': [
            'Ventas netas, consumo y food cost: qué entra y qué no entra',
            'Coste de personal: del bruto a lo que sale de la caja',
            'Prime cost y margen tras prime cost',
            'Ticket medio, gasto por cubierto y ventas por hora: tres cosas distintas',
            'Rotación, absentismo y temporalidad no son sinónimos',
        ],
        'puntos': [
            'La tesis del capítulo: casi todos los errores de gestión de un '
            'restaurante empiezan en una definición, no en una decisión. Quien '
            'llama ticket medio al gasto por cubierto toma decisiones de carta '
            'con el número equivocado.',
            'Explicar que el consumo de materia prima NO son las compras: es '
            'stock inicial más compras menos stock final. Usar las compras '
            'cuando el almacén ha subido o bajado da un food cost falso ese '
            'periodo.',
            'Explicar que el coste de personal es el bruto MÁS la cotización a '
            'cargo de la empresa, y que quedarse en el bruto deja fuera casi un '
            'tercio del coste real. El desglose completo se ve en el capítulo '
            'de prime cost.',
            'Separar los tres indicadores de personas: la rotación mide bajas '
            'sobre plantilla media, el absentismo mide horas no trabajadas '
            'sobre horas pactadas y la temporalidad mide contratos, no '
            'personas. Mezclarlos es lo que hace circular cifras que nadie '
            'puede sostener.',
            'Cerrar con la regla de uso: para decidir sobre la carta manda el '
            'margen; para decidir sobre la compra manda el food cost; para '
            'saber si el negocio aguanta manda el prime cost; y para saber si '
            'la sala rinde manda las ventas por hora trabajada, no los '
            'cubiertos por hora de apertura, que miden la demanda.',
        ],
        'cifras': [
            C('Ventas netas totales del año', f'{X_SEM}!Semana!E57', 'eur'),
            C('Consumo de materia prima del año', f'{X_SEM}!Semana!I57', 'eur'),
            C('Food cost del año, ponderado', f'{X_SEM}!Semana!J57', 'pct1'),
            C('Coste de personal con Seguridad Social del año', f'{X_SEM}!Semana!M57', 'eur'),
            C('Labor cost del año, ponderado', f'{X_SEM}!Semana!N57', 'pct1'),
            C('Prime cost del año, ponderado', f'{X_SEM}!Semana!O57', 'pct1'),
            C('Margen tras prime cost del año', f'{X_SEM}!Semana!R57', 'eur'),
            C('Ticket medio del año', f'{X_SEM}!Semana!U57', 'eur2'),
            C('Gasto medio por cubierto del año', f'{X_SEM}!Semana!V57', 'eur2'),
            C('Ventas por hora trabajada del año', f'{X_SEM}!Semana!Z57', 'eur2'),
        ],
        'sector': ['MM-41', 'MM-42', 'MM-47'],
        'tablas': [{
            'titulo': 'Cada indicador, cómo se calcula, en qué se estropea y cada cuánto se mira (cuadro-de-mando-semanal-manager.xlsx, hoja «KPI y Definiciones»)',
            'src': (X_SEM, 'KPI y Definiciones'),
            'cols': [('Indicador', 'A', 'txt'), ('Cómo se calcula', 'B', 'txt'),
                     ('Unidad', 'C', 'txt'), ('Error típico', 'D', 'txt'),
                     ('Cadencia', 'E', 'txt')],
            'filas': (5, 18),
            'nota': 'La columna del error típico es la que más se usa: casi todos los '
                    'indicadores de un restaurante se estropean por cómo se alimentan, no '
                    'por cómo se calculan.',
        }],
        'prohibido': None,
    },
    {
        'n': 3,
        'titulo': 'El Cuadro de Mando Semanal: por Qué la Semana y no el Mes',
        'resumen_indice': 'qué se rellena cada lunes en quince minutos, cómo se lee un semáforo y qué esconde el promedio del mes.',
        'palabras': 1500, 'bloques': 2,
        'objetivo': 'Convencer con un caso, no con una arenga: enseñar la '
                    'semana concreta en la que el prime cost se disparó y '
                    'mostrar que el promedio del mes se la habría tragado '
                    'entera. Y dejar el ritual de los quince minutos del lunes '
                    'montado.',
        'epigrafes': [
            'Qué mide el cierre del mes y qué no puede medir',
            'Las columnas que se rellenan cada lunes, y de dónde sale cada dato',
            'Cómo se lee un semáforo sin discutirlo',
            'La semana mala que el promedio mensual esconde',
            'Quince minutos, un día fijo y el cuaderno cerrado',
        ],
        'puntos': [
            'La tesis: el mes es contabilidad y la semana es alerta temprana. '
            'Cuando el cierre mensual dice que algo ha ido mal, el mal ya '
            'ocurrió cuatro semanas seguidas y no hay forma de saber en cuál.',
            'Explicar qué se rellena y qué se calcula solo: se escriben ventas '
            'de comida y bebida, stock inicial, compras, stock final, salarios '
            'brutos, otros costes de personal, cubiertos, tickets y horas '
            'trabajadas. El food cost, el labor cost, el prime cost, el margen '
            'y el semáforo salen de ahí sin tocar nada.',
            'Enseñar la lectura del semáforo como un umbral pactado de '
            'antemano y no como una opinión: el objetivo está en una casilla, '
            'se decide una vez y luego no se discute cada lunes.',
            'Trabajar la semana mala del caso: prime cost por encima del '
            'objetivo con food cost y labor cost disparados a la vez, y qué '
            'preguntas se hacen ese lunes por la mañana con esos tres números '
            'delante.',
            'Explicar por qué el total del año es un PONDERADO y no la media de '
            'las 52 semanas: una semana floja pesa lo que factura, no una '
            'cincuentaidosava parte.',
        ],
        'cifras': [
            C('Prime cost del año, ponderado', f'{X_SEM}!Semana!O57', 'pct1'),
            C('Objetivo de prime cost en vigor', f'{X_SEM}!Parámetros!B13', 'pct0'),
            C('Semana ISO en la que se dispara el prime cost', f'{X_SEM}!Semana!A37', 'num'),
            C('Prime cost de esa semana', f'{X_SEM}!Semana!O37', 'pct1'),
            C('Food cost de esa semana', f'{X_SEM}!Semana!J37', 'pct1'),
            C('Labor cost de esa semana', f'{X_SEM}!Semana!N37', 'pct1'),
            C('Ventas netas de esa semana', f'{X_SEM}!Semana!E37', 'eur'),
            C('Margen tras prime cost de esa semana', f'{X_SEM}!Semana!R37', 'eur'),
            C('Cubiertos por hora de apertura del año', f'{X_SEM}!Semana!X57', 'num1'),
            C('Horas de apertura registradas en el año', f'{X_SEM}!Semana!W57', 'num'),
        ],
        'sector': ['MM-41', 'MM-44'],
        'tablas': [{
            'titulo': 'Nueve semanas seguidas, con la mala en medio (cuadro-de-mando-semanal-manager.xlsx, hoja «Semana»)',
            'src': (X_SEM, 'Semana'),
            'cols': [('Semana ISO', 'A', 'num'), ('Ventas netas (€)', 'E', 'eur'),
                     ('Food cost (%)', 'J', 'pct1'), ('Labor cost (%)', 'N', 'pct1'),
                     ('Prime cost (%)', 'O', 'pct1'), ('Objetivo (%)', 'P', 'pct1'),
                     ('Lectura', 'Q', 'txt'), ('Margen tras prime cost (€)', 'R', 'eur')],
            'filas': (33, 41),
            'nota': 'Mira la columna del margen, no sólo la del porcentaje: es la que dice '
                    'cuántos euros quedaron esa semana para pagar alquiler, suministros y '
                    'todo lo demás.',
        }],
        'prohibido': None,
    },
    {
        'n': 4,
        'titulo': 'Prime Cost y Coste de Personal: Dónde se Pierde el Margen',
        'resumen_indice': 'del salario bruto al coste-empresa, partida a partida, y el umbral de la casa para sala y para barra.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Sacar al lector del food cost como métrica única y '
                    'enseñarle a calcular el coste real de una persona. Que '
                    'salga del capítulo sabiendo pasar de un salario bruto a un '
                    'coste-empresa sin quedarse corto, y sabiendo qué umbral de '
                    'prime cost aplica a su formato y de dónde sale ese umbral.',
        'epigrafes': [
            'Qué suma el prime cost y por qué se miran juntos',
            'Del salario bruto al coste-empresa: la cotización, partida a partida',
            'El umbral de la casa: 65 % en sala, 55 % en barra',
            'Vasos comunicantes: elaborar en casa o comprar elaborado',
            'El sector paga poco y forma menos: qué significa eso para tu presupuesto',
        ],
        'puntos': [
            'La tesis: el food cost y el coste de personal son vasos '
            'comunicantes. Elaborar más en casa baja el food cost y sube las '
            'horas; comprar elaborado hace justo lo contrario. Sólo el prime '
            'cost ve las dos cosas a la vez, y por eso es la cifra que impide '
            'engañarse.',
            'Desmontar el error más caro de este capítulo: el 23,60 % que casi '
            'todo el mundo llama «la Seguridad Social de la empresa» son SÓLO '
            'las contingencias comunes. Al coste-empresa hay que sumarle '
            'desempleo, FOGASA, formación profesional, la prima de accidentes '
            'de trabajo y enfermedades profesionales y el mecanismo de equidad '
            'intergeneracional. Quien presupuesta con el 23,60 % se queda '
            'sistemáticamente corto.',
            'Explicar el umbral con honestidad de origen: el 65 % con servicio '
            'en mesa y el 55 % en barra o autoservicio son criterio de la casa, '
            'derivados de la estructura de costes de referencia española. No '
            'son un dato de fuente, y presentarlos como tal sería exactamente '
            'lo que este manual critica del resto.',
            'Enseñar la casilla del tipo de negocio: cambiarla cambia los tres '
            'objetivos a la vez, porque un local de barra con el objetivo de '
            'sala se estaría midiendo con la vara equivocada.',
            'Aterrizar los datos del INE sobre coste laboral y formación: el '
            'sector es el que menos paga y el que menos forma, y eso no es una '
            'queja moral, es un dato de presupuesto. Quien quiera retener gente '
            'compite contra ese suelo, y quien quiera polivalencia tiene que '
            'presupuestar la formación que el sector no presupuesta.',
            'Cross-sell honesto: el coste de cada persona, contrato a contrato, '
            'lo calcula la plantilla de coste laboral del Kit de Gestión de '
            'Personal; aquí se trabaja el agregado de la semana y el criterio.',
        ],
        'cifras': [
            C('Food cost del año, ponderado', f'{X_SEM}!Semana!J57', 'pct1'),
            C('Labor cost del año, ponderado', f'{X_SEM}!Semana!N57', 'pct1'),
            C('Prime cost del año, ponderado', f'{X_SEM}!Semana!O57', 'pct1'),
            C('Coste de personal con Seguridad Social del año', f'{X_SEM}!Semana!M57', 'eur'),
            C('Salarios brutos del año', f'{X_SEM}!Semana!K57', 'eur'),
            C('Margen tras prime cost del año', f'{X_SEM}!Semana!R57', 'eur'),
            C('Objetivo de food cost en vigor', f'{X_SEM}!Parámetros!B11', 'pct0'),
            C('Objetivo de labor cost en vigor', f'{X_SEM}!Parámetros!B12', 'pct0'),
            C('Objetivo de prime cost en vigor', f'{X_SEM}!Parámetros!B13', 'pct0'),
            C('Seguridad Social a cargo de la empresa configurada en el libro', f'{X_SEM}!Parámetros!B22', 'pct0'),
        ],
        'sector': ['MM-16', 'MM-17', 'MM-53', 'MM-41', 'MM-42', 'MM-57'],
        'tablas': [
            {
                'titulo': 'Los objetivos cambian con el formato de negocio (cuadro-de-mando-semanal-manager.xlsx, hoja «Parámetros»)',
                'src': (X_SEM, 'Parámetros'),
                'cols': [('Tipo de negocio', 'A', 'txt'), ('Objetivo de food cost (%)', 'B', 'pct0'),
                         ('Objetivo de labor cost (%)', 'C', 'pct0'),
                         ('Objetivo de prime cost (%)', 'D', 'pct0')],
                'filas': (8, 9),
                'nota': 'Los tres objetivos son criterio de la casa derivado de la estructura de '
                        'costes de referencia española, no una cifra de fuente. Son casillas '
                        'editables: si tu negocio no es ninguno de los dos, pones los tuyos.',
            },
            # Esta tabla NO se construye desde el xlsx a propósito, aunque el
            # desglose viva en «Parámetros!A25:C31». Motivo medido el
            # 2026-09-04: `construir_tabla` detecta que la segunda celda de la
            # fila acaba en «%» y reformatea TODA la fila a un decimal, así que
            # el 0,75 % del MEI se imprimía como «0,8 %» —una cuantía legal
            # redondeada mal, sin que fallara nada— y la columna de notas
            # arrastraba los ids «MM-17» y «MM-53», que son del taller. Los
            # valores son los mismos que las celdas verdes del libro.
            {
                'titulo': 'Del salario bruto al coste-empresa: qué se le suma y por qué',
                'cabecera': ['Partida', 'Tipo a cargo de la empresa', 'Qué hay que saber'],
                'filas': [
                    ['Contingencias comunes', '23,60 %',
                     'Es lo que casi todo el mundo llama, mal, «la Seguridad Social de la empresa». La persona trabajadora aporta además su parte'],
                    ['Desempleo, contrato indefinido a tiempo completo', '5,50 %',
                     'Los contratos de duración determinada cotizan por encima de este tipo'],
                    ['Fondo de Garantía Salarial', '0,20 %', ''],
                    ['Formación profesional', '0,60 %', ''],
                    ['Accidentes de trabajo y enfermedades profesionales', 'Según tarifa',
                     'Depende de la actividad, según la tarifa de primas de la disposición adicional 61.ª del TRLGSS'],
                    ['Mecanismo de Equidad Intergeneracional, parte empresarial', '0,75 %',
                     'Art. 16 de la Orden PJC/297/2026'],
                    ['TOTAL a cargo de la empresa en hostelería, 2026', '32,15 % / 33,35 %',
                     'El primero, con contrato indefinido a tiempo completo; el segundo, con contrato de duración determinada'],
                ],
                'nota': V_COTIZA,
            },
        ],
        'prohibido': None,
    },
    {
        'n': 5,
        'titulo': 'El Día del Manager: Apertura, Servicio, Cierre y Handover',
        'resumen_indice': 'qué decide cada bloque del día, qué se delega, qué firma el manager y qué encuentra escrito el turno siguiente.',
        'palabras': 1400, 'bloques': 2,
        'objetivo': 'Dar el criterio que hay detrás del checklist, no otro '
                    'checklist. Que el lector sepa qué decisión toma en cada '
                    'bloque del día, qué puede delegar, qué no puede delegar '
                    'nunca y qué tiene que quedar escrito para el turno que '
                    'entra.',
        'epigrafes': [
            'Los cuatro bloques del día y qué decide cada uno',
            'Apertura: lo que hay que ver antes de abrir la puerta',
            'Servicio: dónde está el manager y qué mira',
            'Cierre y handover: lo que el turno siguiente tiene que encontrar escrito',
            'Qué se delega, qué se supervisa y qué no se delega nunca',
        ],
        'puntos': [
            'La tesis: un checklist sin criterio se firma sin mirar. Lo que '
            'convierte una lista en control es saber qué decisión depende de '
            'cada línea y quién la toma.',
            'Apertura: las decisiones que sólo se pueden tomar antes de abrir '
            '—dotación del turno frente a la reserva del día, producto que hay '
            'que sacar o cambiar, y qué queda sin cubrir— y por qué después ya '
            'no hay margen para ninguna de las tres.',
            'Servicio: el sitio físico del manager cambia con el momento del '
            'servicio, y lo que mira también. Explicar los tres puntos de '
            'observación —la puerta, el pase y la mesa que lleva más tiempo '
            'esperando— y qué se corrige en el momento y qué se anota para '
            'después.',
            'Cierre y handover: el traspaso entre turnos es un documento, no '
            'una conversación en la puerta. Lo que no queda escrito se pierde, '
            'y lo que se pierde reaparece como queja al día siguiente.',
            'La regla de delegación: se delega la EJECUCIÓN y se supervisa el '
            'RESULTADO; no se delegan la firma de un registro obligatorio, la '
            'decisión sobre una persona ni la respuesta a una reclamación '
            'formal.',
            'Cross-sell explícito: los checklists de apertura, servicio y '
            'cierre ya existen en el Kit de Tareas y no se repiten aquí. Lo que '
            'este capítulo añade es el criterio y la auditoría interna que '
            'comprueba si el criterio se está aplicando.',
        ],
        'cifras': [
            C('Puntos de control de la auditoría interna', f'{X_AUD}!Resumen por Área!B16', 'num'),
            C('Escala máxima de puntuación de la auditoría', f'{X_AUD}!Auditoría!D75', 'num'),
            C('Umbral verde de la auditoría', f'{X_AUD}!Auditoría!D76', 'num'),
            C('Puntuación ponderada de la primera visita', f'{X_AUD}!Auditoría!E71', 'num2'),
            C('Puntuación ponderada de la tercera visita', f'{X_AUD}!Auditoría!I71', 'num2'),
            C('Cumplimiento de la tercera visita', f'{X_AUD}!Auditoría!I72', 'pct1'),
            C('Horas de apertura al público de una semana completa', f'{X_SEM}!Parámetros!B37', 'num'),
            C('Cubiertos por hora de apertura del año', f'{X_SEM}!Semana!X57', 'num1'),
        ],
        'sector': [],
        'tablas': [{
            'titulo': 'Las seis áreas del servicio, puntuadas tres veces con la misma vara (auditoria-interna-servicio.xlsx, hoja «Resumen por Área»)',
            'src': (X_AUD, 'Resumen por Área'),
            'cols': [('Área', 'A', 'txt'), ('Puntos de control', 'B', 'num'),
                     ('Peso del área', 'C', 'num'), ('Visita 1 (0-5)', 'D', 'num2'),
                     ('Visita 3 (0-5)', 'F', 'num2'),
                     ('Variación de la 1 a la 3', 'G', 'num2'),
                     ('Tendencia', 'H', 'txt'),
                     ('Cumplimiento visita 3 (%)', 'I', 'pct1')],
            'filas': (10, 16),
            'nota': 'La auditoría de este pack puntúa experiencia de cliente y estándares de '
                    'marca; deja fuera a propósito la seguridad alimentaria, que tiene su '
                    'propio sistema de registros.',
        }],
        'prohibido': None,
    },
    {
        'n': 6,
        'titulo': 'La Caja y el Tique: Corte, Arqueo, Cierre — y lo que Viene',
        'resumen_indice': 'los tres pasos y sus tres firmas, el descuadre que se repite, el tique, el efectivo, las propinas y las dos fechas que vienen.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Que el lector deje de llamar cierre al arqueo, sepa buscar '
                    'un descuadre que se repite, sepa qué tiene que llevar un '
                    'tique y hasta dónde llega, sepa que no puede ser cashless '
                    'y sepa qué hacer con las propinas. Y que tenga claras las '
                    'dos fechas que sí le van a afectar.',
        'epigrafes': [
            'Corte, arqueo y cierre: tres pasos, tres momentos y tres firmas',
            'Un descuadre que se repite: cómo se busca sin acusar a nadie',
            'El tique: contenido mínimo y hasta dónde llega la factura simplificada',
            'Efectivo: por qué un restaurante no puede ser cashless',
            'Las propinas: IRPF, retención y qué cambia si el bote lo reparte la casa',
            'Verifactu y factura electrónica: qué fecha te afecta y qué preguntarle a tu proveedor',
        ],
        'puntos': [
            'Separar los tres pasos con precisión y decir que en México «corte '
            'de caja» nombra el paso intermedio, no el cierre: quien sólo hace '
            'uno de los tres se queda ciego ante las fugas que aparecen en los '
            'otros dos.',
            'Protocolo del descuadre repetido: primero se descarta el error de '
            'sistema (anulaciones, invitaciones, cambios de forma de pago), '
            'luego se acota por turno y por persona con los datos que ya '
            'existen, y sólo al final se habla con alguien. Acusar antes de '
            'acotar destruye la confianza del equipo y no encuentra el euro.',
            'Fijar el límite de la factura simplificada en hostelería y el '
            'límite general, y explicar la tercera figura que casi nadie '
            'conoce: la factura simplificada CUALIFICADA, la que lleva los '
            'datos fiscales del cliente. Es la que sí entra en la factura '
            'electrónica entre empresas, y por eso hace falta una regla de tres '
            'casillas en el TPV.',
            'Explicar que negarse a aceptar efectivo es una infracción de '
            'consumo y cuál es el rango legal de cobro en efectivo, sin '
            'convertirlo en un consejo fiscal.',
            'Propinas: son rendimiento del trabajo en el IRPF siempre; la '
            'obligación de retener nace cuando es la empresa quien reparte el '
            'bote, porque el reglamento del IRPF nombra ese supuesto. Sobre '
            'cotización, decir exactamente lo que hay: no existe norma expresa '
            'que la mencione. Nada de consultas vinculantes.',
            'Cerrar con las dos fechas: el aplazamiento de Verifactu y el '
            'estado real de la factura electrónica entre empresas. Y con la '
            'pregunta operativa: pedirle por escrito al proveedor del TPV la '
            'fecha de su versión adaptada.',
        ],
        'cifras': [
            C('Ventas netas totales del año', f'{X_SEM}!Semana!E57', 'eur'),
            C('Tickets del año', f'{X_SEM}!Semana!T57', 'num'),
            C('Ticket medio del año', f'{X_SEM}!Semana!U57', 'eur2'),
            C('Cubiertos del año', f'{X_SEM}!Semana!S57', 'num'),
            C('Gasto medio por cubierto del año', f'{X_SEM}!Semana!V57', 'eur2'),
            C('Quejas registradas en el trimestre', f'{X_QUEJ}!Resumen!D11', 'num'),
            C('Quejas por cobro incorrecto', f'{X_QUEJ}!Resumen!C26', 'num'),
            C('Peso de las quejas por cobro incorrecto sobre el total', f'{X_QUEJ}!Resumen!D26', 'pct1'),
        ],
        'sector': ['MM-37', 'MM-39', 'MM-24', 'MM-25'],
        'tablas': [
            {
                'titulo': 'Corte, arqueo y cierre: qué es cada uno y qué queda firmado',
                'cabecera': ['Paso', 'Cuándo', 'Qué se verifica', 'Quién firma'],
                'filas': [
                    ['Corte', 'Al cambiar de turno', 'Se cuenta y se traspasa el fondo; no hay verificación contable', 'Quien entrega y quien recibe'],
                    ['Arqueo', 'Al terminar el servicio', 'Efectivo contado contra efectivo esperado; se anota la diferencia', 'Quien cierra el turno'],
                    ['Cierre', 'Al terminar el día', 'Todas las formas de pago contra el informe del TPV, con anulaciones e invitaciones', 'El manager'],
                ],
                'nota': 'La plantilla diaria de arqueo está en el Kit de Tareas; aquí lo que se '
                        'fija es qué verifica cada paso y quién responde de él. En México «corte '
                        'de caja» nombra el segundo paso, no el tercero.',
            },
            {
                'titulo': 'Las dos normas de facturación que vienen, y su fecha real (calendario-cumplimiento-legal.xlsx, hoja «Estado Normativo»)',
                'src': (X_LEG, 'Estado Normativo'),
                'cols': [('Norma', 'B', 'txt'), ('Estado a la fecha de corte', 'C', 'txt'),
                         ('Qué obliga hoy y qué hace el manager', 'D', 'txt')],
                'filas': (9, 10),
                'nota': 'Verificado el 04-09-2026 · RDL 15/2025, art. 3, y RD 1619/2012, arts. 4 y 7.2, '
                        'con el art. 4.1 del RD 238/2026 · https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696',
            },
        ],
        'prohibido': None,
    },
    {
        'n': 7,
        'titulo': 'Mandar sin Quemar al Equipo: Autoridad, Delegación y Cómo Defender un Cambio con Números',
        'resumen_indice': 'autoridad formal frente a autoridad real, señales de desgaste, la propuesta al propietario y la conversación difícil.',
        'palabras': 1400, 'bloques': 2,
        'objetivo': 'Darle al manager que no es dueño lo único que sí controla: '
                    'la calidad de su argumento. Y darle al que dirige un '
                    'equipo cansado un protocolo para detectar el desgaste '
                    'antes de que se convierta en una baja o en una carta de '
                    'dimisión.',
        'epigrafes': [
            'Autoridad formal y autoridad real: en qué se nota la diferencia',
            'Delegar sin perder el control: qué se delega y con qué límite',
            'Señales tempranas de que alguien se está quemando',
            'Cómo llevar una propuesta al propietario con la cifra de la semana',
            'La conversación difícil: preparación, guion y acuerdo escrito',
        ],
        'puntos': [
            'La tesis: el manager que no es propietario no puede decidir la '
            'inversión, pero sí puede decidir con qué dato entra en el '
            'despacho. Una propuesta con la cifra de la semana y el impacto '
            'estimado se discute; una propuesta con una impresión se archiva.',
            'El guion de la propuesta, en cuatro movimientos: el número que ha '
            'cambiado, qué lo explica, qué se propone hacer, y qué se '
            'compromete a medir dentro de un plazo concreto. Y una regla: se '
            'lleva UNA propuesta cada vez.',
            'Delegación con límite escrito: se delega la ejecución con un '
            'importe, un plazo o un supuesto claro por encima del cual hay que '
            'consultar. Sin ese límite, delegar es abandonar.',
            'Señales de desgaste que sí se pueden observar sin invadir a nadie: '
            'cambios sostenidos en el rendimiento, en la puntualidad y en el '
            'trato, y aumento de las ausencias cortas. Se observan durante '
            'semanas, no un día malo, y se llevan a un uno-a-uno, nunca al pase '
            'delante del equipo.',
            'La conversación difícil se prepara por escrito y se cierra por '
            'escrito: un hecho concreto, el efecto que tuvo, lo que se espera a '
            'partir de ahora y una fecha de seguimiento. Lo que no queda en el '
            'acta no ocurrió.',
        ],
        'cifras': [
            C('Prime cost de la semana en la que se dispara', f'{X_SEM}!Semana!O37', 'pct1'),
            C('Objetivo de prime cost en vigor', f'{X_SEM}!Parámetros!B13', 'pct0'),
            C('Margen tras prime cost del año', f'{X_SEM}!Semana!R57', 'eur'),
            C('Acuerdos registrados en el trimestre', f'{X_REU}!Actas y Acuerdos!D46', 'num'),
            C('Acuerdos cerrados', f'{X_REU}!Actas y Acuerdos!D47', 'num'),
            C('Acuerdos abiertos', f'{X_REU}!Actas y Acuerdos!D49', 'num'),
            C('Acuerdos cerrados sobre el total', f'{X_REU}!Actas y Acuerdos!D52', 'pct0'),
            C('Acuerdos cerrados dentro de plazo', f'{X_REU}!Actas y Acuerdos!D53', 'pct0'),
            C('Personas del equipo con seguimiento individual', f'{X_REU}!Uno-a-uno!D30', 'num'),
        ],
        'sector': ['MM-44'],
        'tablas': [{
            'titulo': 'Los acuerdos del trimestre, repartidos por responsable (reuniones-acuerdos-plan-90-dias.xlsx, hoja «Actas y Acuerdos»)',
            'src': (X_REU, 'Actas y Acuerdos'),
            'cols': [('Responsable', 'B', 'txt'), ('Acuerdos', 'C', 'num'),
                     ('Abiertos', 'D', 'num'), ('Vencidos', 'E', 'num')],
            'filas': (62, 73),
            'nota': 'Una columna de vencidos concentrada en una sola persona no es un problema '
                    'de esa persona: casi siempre es un problema de reparto o de plazo.',
        }],
        'prohibido': None,
    },
    {
        'n': 8,
        'titulo': 'El Convenio que te Aplica: ALEH VI, tu Provincia y lo que no se Negocia',
        'resumen_indice': 'qué fija el acuerdo estatal, qué no puede tocar el convenio provincial, cómo se busca en REGCON y qué pasa cuando caduca.',
        'palabras': 1400, 'bloques': 2,
        'objetivo': 'Que el lector sepa cuál es exactamente su norma '
                    'convencional, sepa buscarla él solo y sepa distinguir lo '
                    'que su convenio provincial puede cambiar de lo que está '
                    'reservado al acuerdo estatal. Es el capítulo que evita '
                    'aplicar la regla de otra provincia.',
        'epigrafes': [
            'ALEH VI, no ALEH V: qué es y qué cubre',
            'Las materias reservadas: lo que tu convenio provincial no puede tocar',
            'Cómo se busca tu convenio en REGCON, paso a paso',
            'Por qué el mismo puesto cobra distinto según la provincia',
            'Ultraactividad: qué pasa cuando tu convenio caduca',
        ],
        'puntos': [
            'Fijar la arquitectura de dos pisos: el acuerdo laboral estatal de '
            'hostelería se ocupa de clasificación profesional, periodo de '
            'prueba, contratos formativos y régimen disciplinario, y remite las '
            'tablas salariales al convenio provincial. Ningún acuerdo estatal '
            'de hostelería fija salarios.',
            'Contar que el acuerdo estatal se modificó y se publicó el 4 de '
            'septiembre de 2026, con qué artículos toca y qué capítulos nuevos '
            'añade, y hasta cuándo está pactada su vigencia. Es la razón por la '
            'que este manual puede decir lo que dice.',
            'Enseñar la búsqueda en REGCON como un procedimiento reproducible: '
            'ámbito funcional de hostelería, ámbito territorial de la '
            'provincia, y comprobación de la fecha de publicación y del estado '
            'de vigencia. Y avisar de que se busca por provincia del CENTRO DE '
            'TRABAJO, no del domicilio de la empresa.',
            'Explicar la diferencia salarial entre provincias con el dato del '
            'sector, para justificar por qué este manual NO da una cifra de '
            'nómina y por qué cualquier plantilla que la diera estaría mal en '
            'la mitad de España.',
            'Ultraactividad: un convenio expirado se sigue aplicando mientras '
            'no haya otro, y lo que hay que vigilar es la publicación del '
            'nuevo, con retroactividad y atrasos. Es un vencimiento del '
            'calendario del manager, no un tema de la asesoría.',
        ],
        'cifras': [
            C('Normas en seguimiento en la hoja de estado normativo', f'{X_LEG}!Estado Normativo!C21', 'num'),
            C('Normas con su ficha de investigación citada', f'{X_LEG}!Estado Normativo!C22', 'num'),
            C('Filas del cuadro del régimen disciplinario', f'{X_LEG}!Régimen Disciplinario ALEH!E18', 'num'),
            C('Faltas leves tipificadas en el cuadro', f'{X_LEG}!Régimen Disciplinario ALEH!E19', 'num'),
            C('Faltas graves tipificadas en el cuadro', f'{X_LEG}!Régimen Disciplinario ALEH!E20', 'num'),
            C('Faltas muy graves tipificadas en el cuadro', f'{X_LEG}!Régimen Disciplinario ALEH!E21', 'num'),
            C('Días de vigencia que le quedan a la modificación del ALEH VI', f'{X_LEG}!Régimen Disciplinario ALEH!E25', 'num'),
        ],
        'sector': ['MM-14', 'MM-15', 'MM-11'],
        'tablas': [{
            'titulo': 'El acuerdo estatal y tu convenio provincial, con su estado a la fecha de corte (calendario-cumplimiento-legal.xlsx, hoja «Estado Normativo»)',
            'src': (X_LEG, 'Estado Normativo'),
            'cols': [('Norma', 'B', 'txt'), ('Estado a la fecha de corte', 'C', 'txt'),
                     ('Qué obliga hoy y qué hace el manager', 'D', 'txt')],
            'filas': (13, 14),
            'nota': V_ALEH,
        }],
        'prohibido': None,
    },
    {
        'n': 9,
        'titulo': 'Contratar sin Fabricar un Indefinido por Accidente',
        'resumen_indice': 'las dos causas de temporalidad que quedan, el encadenamiento, el fijo-discontinuo y el periodo de prueba de hostelería.',
        'palabras': 1500, 'bloques': 2,
        'objetivo': 'Que el lector sepa qué contrato cabe en cada situación '
                    'real de un restaurante —un refuerzo de verano, una baja, '
                    'una temporada— y sepa exactamente qué gesto convierte una '
                    'contratación temporal en una relación indefinida sin que '
                    'nadie lo haya decidido.',
        'epigrafes': [
            'El punto de partida: el contrato se presume indefinido',
            'Las dos causas que quedan: circunstancias de la producción y sustitución',
            'Encadenamiento: cómo se fabrica un fijo sin querer',
            'Fijo-discontinuo: el contrato de la temporada y su antigüedad',
            'Periodo de prueba y contratos formativos en hostelería',
        ],
        'puntos': [
            'La tesis: desde la reforma, lo indefinido es la regla y lo '
            'temporal es la excepción causal. El contrato de obra y servicio '
            'desapareció, y seguir razonando con él es el origen de la mayoría '
            'de los fraudes involuntarios del sector.',
            'Explicar las dos causas que quedan con el detalle operativo: qué '
            'tiene que constar por escrito en cada una, qué duración máxima '
            'tienen y por qué en la sustitución hay que identificar a la '
            'persona sustituida y la causa.',
            'El encadenamiento, que es el error más caro y el más fácil de '
            'cometer: se cuenta por PUESTO y por persona a lo largo de un '
            'periodo, y no hace falta que los contratos sean seguidos. Además, '
            'el fraude se sanciona por cada trabajador afectado, así que un '
            'mismo error repetido con cinco personas son cinco infracciones.',
            'Fijo-discontinuo: es un contrato INDEFINIDO de trabajo estacional, '
            'obligatoriamente por escrito y con llamamiento también por '
            'escrito; su antigüedad se calcula por toda la relación, no sólo '
            'por los periodos trabajados. Es la figura que resuelve de verdad '
            'la temporada, y casi nadie la usa bien.',
            'Periodo de prueba: lo fija el acuerdo estatal por grupo '
            'profesional y el convenio provincial NO puede modificarlo; es nulo '
            'si la persona ya desempeñó las mismas funciones en la empresa. Es '
            'la trampa clásica del extra que vuelve.',
            'Cross-sell: el alta, la documentación y el seguimiento de cada '
            'contrato viven en el Kit de Gestión de Personal; aquí se decide '
            'QUÉ contrato cabe.',
        ],
        'cifras': [
            C('Personas de la plantilla del caso', f'{X_POLI}!Cobertura por Estación!C27', 'num'),
            C('Salarios brutos del año', f'{X_SEM}!Semana!K57', 'eur'),
            C('Coste de personal con Seguridad Social del año', f'{X_SEM}!Semana!M57', 'eur'),
            C('Puesto que se cubre en el ejemplo de selección del pack', f'{X_SEL}!Scorecard!D4', 'txt'),
            C('Encuadre de ese puesto en el ALEH VI', f'{X_SEL}!Scorecard!D5', 'txt'),
            C('Jornada del puesto del ejemplo', f'{X_SEL}!Scorecard!D6', 'txt'),
        ],
        'sector': ['MM-09', 'MM-10', 'MM-11', 'MM-23'],
        'tablas': [{
            'titulo': 'Qué contrato cabe, cuánto dura y qué lo convierte en indefinido',
            'cabecera': ['Figura', 'Duración', 'Qué la convierte en indefinida', 'Norma'],
            'filas': [
                ['Circunstancias de la producción',
                 'Máximo 6 meses, ampliables a 1 año por convenio sectorial',
                 'Superar el plazo, o encadenar más de 18 meses en un periodo de 24',
                 'Art. 15.2 ET, redacción del RDL 32/2021'],
                ['Sustitución',
                 'Mientras dure la causa que la justifica',
                 'No identificar a la persona sustituida y la causa en el contrato',
                 'Art. 15.3 ET'],
                ['Fijo-discontinuo',
                 'Indefinido: se activa y se interrumpe por temporada',
                 'Ya es indefinido; el riesgo es el llamamiento sin forma escrita',
                 'Art. 16 ET'],
                ['Contrato de obra y servicio',
                 'No existe: desapareció el 30 de marzo de 2022',
                 'Usarlo hoy es fraude desde el primer día',
                 'Disposición transitoria 3.ª del RDL 32/2021'],
                ['Periodo de prueba, contrato indefinido',
                 '90, 60 o 45 días naturales según grupo profesional',
                 'Es nulo si la persona ya desempeñó las mismas funciones en la empresa',
                 'Art. 21 ALEH VI y art. 14 ET'],
                ['Periodo de prueba, temporal de más de 3 meses',
                 '75, 45 o 30 días naturales según grupo profesional',
                 'Ídem',
                 'Art. 21 ALEH VI'],
                ['Periodo de prueba, temporal de hasta 3 meses',
                 '60, 30 o 15 días naturales según grupo profesional',
                 'Ídem',
                 'Art. 21 ALEH VI'],
            ],
            'nota': V_ET,
        }],
        'prohibido': None,
    },
    {
        'n': 10,
        'titulo': 'Selección con Criterio y los Primeros 30 Días',
        'resumen_indice': 'competencias con peso antes de ver a nadie, entrevista estructurada, lo que no se puede preguntar y las cuatro formaciones.',
        'palabras': 1400, 'bloques': 2,
        'objetivo': 'Sustituir la corazonada por un método reproducible: pesar '
                    'las competencias antes de conocer a nadie, preguntar lo '
                    'mismo a todos, puntuar por separado y comparar al final. '
                    'Y montar los primeros treinta días de forma que la persona '
                    'llegue al mes sabiendo qué se espera de ella.',
        'epigrafes': [
            'El scorecard: competencias con peso antes de ver a nadie',
            'La entrevista estructurada: las mismas preguntas para todos',
            'Lo que no se puede preguntar',
            'Los primeros 30 días: acogida, acompañamiento y prueba',
            'Las cuatro formaciones que no son la misma',
        ],
        'puntos': [
            'La tesis: el sesgo no se combate con buena voluntad, se combate '
            'con orden. Pesar las competencias ANTES de ver el primer '
            'currículum es lo que impide reescribir el perfil para que encaje '
            'con quien te ha caído bien.',
            'Explicar la diferencia entre media simple y media ponderada con el '
            'caso del pack: dos candidatos pueden empatar en media simple y '
            'separarse en la ponderada, y la ponderada es la que refleja lo que '
            'de verdad importa en ese puesto.',
            'Preguntas de conducta, no de opinión: se pregunta por una '
            'situación que ya ocurrió y por lo que la persona hizo, no por lo '
            'que haría. Y se puntúa justo después de cada entrevista, no al '
            'final del día.',
            'Lo que no se puede preguntar: hay materias sobre las que no se '
            'puede indagar en un proceso de selección, y saberlo protege a la '
            'empresa y a la persona. Va con su norma y su artículo.',
            'Las cuatro formaciones que se confunden en una sola: la acogida al '
            'puesto, la formación en prevención de riesgos en el momento de la '
            'contratación y dentro de jornada, la formación en manipulación de '
            'alimentos —que es obligación del titular, por puesto, y no un '
            'carné— y la formación específica en el sistema de autocontrol.',
            'Cerrar con el dato del INE sobre gasto en formación: el sector '
            'forma muy por debajo de la media española, y eso convierte la '
            'formación en un diferenciador barato de retención.',
        ],
        'cifras': [
            C('Puesto del ejemplo de selección', f'{X_SEL}!Scorecard!D4', 'txt'),
            C('Umbral de recomendación configurado', f'{X_SEL}!Scorecard!D7', 'num1'),
            C('Competencias que pesa el scorecard', f'{X_SEL}!Comparativa de Candidatos!D6', 'num'),
            C('Candidatos evaluados', f'{X_SEL}!Comparativa de Candidatos!D14', 'num'),
            C('Mejor media ponderada', f'{X_SEL}!Comparativa de Candidatos!D16', 'num2'),
            C('Distancia entre el primero y el segundo', f'{X_SEL}!Comparativa de Candidatos!D17', 'num2'),
            C('Candidatos que alcanzan el umbral', f'{X_SEL}!Comparativa de Candidatos!D18', 'num'),
            C('Preguntas del guion de entrevista', f'{X_SEL}!Preguntas por Competencia!E34', 'num'),
        ],
        'sector': ['MM-30', 'MM-43'],
        'tablas': [
            {
                'titulo': 'Las competencias del puesto, con su peso y las cuatro puntuaciones (seleccion-scorecard-entrevista.xlsx, hoja «Scorecard»)',
                'src': (X_SEL, 'Scorecard'),
                'cols': [('#', 'A', 'num'), ('Competencia', 'B', 'txt'),
                         ('Peso (1-3)', 'C', 'num'), ('Candidata A', 'D', 'num'),
                         ('Candidato B', 'E', 'num'), ('Candidata C', 'F', 'num'),
                         ('Candidato D', 'G', 'num')],
                'filas': (13, 20),
            },
            {
                'titulo': 'La comparación final: media ponderada, media simple y recomendación (seleccion-scorecard-entrevista.xlsx, hoja «Comparativa de Candidatos»)',
                'src': (X_SEL, 'Comparativa de Candidatos'),
                'cols': [('Candidato', 'B', 'txt'), ('Media ponderada', 'C', 'num2'),
                         ('Media simple', 'D', 'num2'),
                         ('Competencias valoradas', 'E', 'num'),
                         ('Puesto en el ranking', 'G', 'num'),
                         ('Recomendación', 'H', 'txt')],
                'filas': (9, 12),
                'nota': 'Compara las dos primeras columnas de números: cuando la media simple y '
                        'la ponderada no ordenan igual, es que el peso está haciendo su trabajo.',
            },
        ],
        'prohibido': None,
    },
]

CAPITULOS += [
    {
        'n': 11,
        'titulo': 'Jornada, Cuadrante y Registro de Jornada: Tres Documentos que no Son lo Mismo',
        'resumen_indice': 'los topes que no se pactan a la baja, el cómputo de los descansos, las horas extra y el estado real del registro.',
        'palabras': 1800, 'bloques': 3,
        'objetivo': 'Cerrar de una vez el capítulo peor contado del sector. '
                    'Separar los tres documentos, dejar la tabla completa de '
                    'topes con su artículo, decir qué exige HOY el registro de '
                    'jornada y qué no exige todavía, y explicar que desde el 4 '
                    'de septiembre de 2026 no llevarlo también es materia '
                    'disciplinaria interna.',
        'epigrafes': [
            'Cuadrante, registro y calendario laboral: tres papeles distintos',
            'Los topes que no se pueden pactar a la baja',
            'Los quince minutos del bocadillo y otras trampas del cómputo',
            'Horas extraordinarias y horas complementarias: dos cosas distintas',
            'Qué exige hoy el registro de jornada, y qué no exige todavía',
            'El registro como materia disciplinaria: la novedad del ALEH VI',
        ],
        'puntos': [
            'Separar los tres documentos con precisión, porque en el 90 % de '
            'los locales se llaman todos «el horario»: el cuadrante es '
            'planificación y mira hacia delante; el registro es constancia y '
            'mira hacia atrás; el calendario laboral anual es un documento '
            'distinto que además tiene que estar expuesto en lugar visible del '
            'centro de trabajo.',
            'Recorrer los topes uno a uno con su artículo: jornada máxima de '
            'promedio en cómputo anual, jornada ordinaria diaria, descanso '
            'entre jornadas, descanso semanal acumulable, y por qué el descanso '
            'semanal acumulable es exactamente lo que permite el cuadrante de '
            'hostelería sin incumplir nada.',
            'La trampa del descanso en jornada continuada: existe el derecho, '
            'pero sólo cuenta como tiempo de trabajo efectivo si lo dice el '
            'convenio o el contrato. Es la fuente número uno de discusiones '
            'evitables en un pase.',
            'Diferenciar horas extraordinarias de complementarias: las extra '
            'tienen tope anual por persona y se reducen en proporción en la '
            'jornada parcial; las complementarias sólo caben con pacto '
            'específico por escrito y sobre contratos con un mínimo de horas '
            'semanales, con sus propios límites.',
            'Estado REAL del registro de jornada: lo exigible es el registro '
            'diario con hora de inicio y de fin, conservado cuatro años a '
            'disposición de la plantilla, de su representación y de la '
            'Inspección, y admite papel o una hoja de cálculo. El real decreto '
            'del registro digital no está publicado. Decirlo con esa claridad, '
            'porque quien afirma lo contrario suele estar vendiendo software.',
            'La consecuencia más dura y menos conocida: en el contrato a tiempo '
            'parcial, si no se lleva el registro diario totalizado mensualmente '
            'y con copia a la persona trabajadora, el contrato se presume '
            'celebrado a jornada completa.',
            'La novedad del 4 de septiembre de 2026: el acuerdo estatal ha '
            'tipificado los incumplimientos del registro como falta leve, grave '
            'o muy grave según cuántos se acumulen en un mes. El registro deja '
            'de ser sólo un riesgo administrativo y pasa a ser régimen '
            'disciplinario interno, con lo que eso obliga a documentar.',
        ],
        'cifras': [
            C('Jornada máxima legal de promedio', f'{X_LEG}!Topes de Jornada!D19', 'num'),
            C('Horas semanales pactadas de promedio en el caso', f'{X_LEG}!Topes de Jornada!D20', 'num'),
            C('Tope legal de horas extraordinarias al año por persona', f'{X_LEG}!Topes de Jornada!D23', 'num'),
            C('Margen de horas extraordinarias que le queda al caso', f'{X_LEG}!Topes de Jornada!D25', 'num'),
            C('Aviso cuando se supere este porcentaje del tope', f'{X_LEG}!Topes de Jornada!D27', 'pct0'),
            C('Horas de apertura al público de una semana completa', f'{X_SEM}!Parámetros!B37', 'num'),
            C('Horas de apertura registradas en el año', f'{X_SEM}!Parámetros!B39', 'num'),
            C('Personas de la plantilla del caso', f'{X_POLI}!Cobertura por Estación!C27', 'num'),
            C('Filas del cuadro del régimen disciplinario', f'{X_LEG}!Régimen Disciplinario ALEH!E18', 'num'),
        ],
        'sector': ['MM-01', 'MM-02', 'MM-03', 'MM-04', 'MM-05', 'MM-06', 'MM-07'],
        'tablas': [
            {
                'titulo': 'Los topes de jornada, con su valor y su artículo (calendario-cumplimiento-legal.xlsx, hoja «Topes de Jornada»)',
                'src': (X_LEG, 'Topes de Jornada'),
                'cols': [('#', 'A', 'num'), ('Concepto', 'B', 'txt'),
                         ('Valor', 'C', 'txt'), ('Artículo', 'D', 'txt')],
                'filas': (6, 16),
                'nota': V_ET,
            },
            {
                'titulo': 'No registrar la jornada, ahora también es falta (calendario-cumplimiento-legal.xlsx, hoja «Régimen Disciplinario ALEH»)',
                'src': (X_LEG, 'Régimen Disciplinario ALEH'),
                'cols': [('Falta o figura', 'B', 'txt'), ('Gravedad', 'D', 'txt'),
                         ('Umbral o detalle', 'E', 'txt'),
                         ('Sanción posible', 'F', 'txt'), ('Artículo', 'G', 'txt')],
                'filas': (6, 10),
                'nota': V_ALEH,
            },
        ],
        'prohibido': None,
    },
    {
        'n': 12,
        'titulo': 'Permisos, Vacaciones y Conciliación sin Sustos',
        'resumen_indice': 'los días que son y los que no, las dos figuras del permiso parental, la guarda legal y el silencio que concede.',
        'palabras': 1500, 'bloques': 2,
        'objetivo': 'Que el manager pueda contestar en el momento, y bien, a '
                    'las peticiones que llegan a mitad de servicio. Y que sepa '
                    'cuáles de esas peticiones NO decide él, porque la ley ya '
                    'las ha decidido.',
        'epigrafes': [
            'Vacaciones: días naturales, calendario y preaviso',
            'Fallecimiento, accidente y enfermedad grave: los días que son y los que no',
            'El permiso parental son DOS figuras y sólo una se paga',
            'Nacimiento y cuidado de menor: qué cambió y qué hay que planificar',
            'Guarda legal y adaptación de jornada: quién decide y qué pasa con el silencio',
        ],
        'puntos': [
            'Vacaciones: el mínimo legal se cuenta en días naturales, no son '
            'sustituibles por dinero salvo extinción del contrato, y el '
            'calendario tiene que conocerse con la antelación que fija la '
            'norma. Esa antelación es lo que convierte las vacaciones en un '
            'problema de planificación y no en una negociación de última hora.',
            'Corregir el error más repetido del sector: el permiso por '
            'fallecimiento NO son cinco días. Son dos, ampliables en dos más si '
            'hay desplazamiento. Los cinco días son los del accidente o '
            'enfermedad graves, hospitalización o intervención quirúrgica sin '
            'hospitalización que precise reposo domiciliario, y alcanzan a más '
            'gente de la que se cree.',
            'Explicar las DOS figuras del permiso parental sin mezclarlas, '
            'porque se solapan casi punto por punto y sólo una se paga: la de '
            'ocho semanas es una suspensión del contrato y no está retribuida; '
            'la de dos semanas sí lo está y tiene su prestación. Nombrar las '
            'dos, con su artículo, y decir por qué confundirlas cuesta dinero '
            'en las dos direcciones.',
            'Nacimiento y cuidado de menor: la duración actual por progenitor y '
            'la ampliación en familias monoparentales, y lo que eso significa '
            'para un cuadrante que hay que cubrir durante meses. Es '
            'planificación, no una sorpresa.',
            'Guarda legal y adaptación de jornada, que son las dos que más '
            'discusiones producen: en la reducción por guarda legal la '
            'concreción horaria la elige la persona trabajadora dentro de su '
            'jornada ordinaria; en la adaptación por conciliación, si la '
            'empresa no contesta dentro del plazo, la solicitud se entiende '
            'concedida. El silencio de la empresa no es neutral.',
            'Cerrar con la consecuencia operativa: cada una de estas figuras se '
            'anota en el calendario del equipo el día que se pide, no el día '
            'que empieza, porque lo que hunde un cuadrante no es el permiso, es '
            'enterarse tarde.',
        ],
        'cifras': [
            C('Figuras recogidas en la hoja de permisos', f'{X_LEG}!Permisos y Cómputo!D18', 'num'),
            C('De ellas, retribuidas', f'{X_LEG}!Permisos y Cómputo!D19', 'num'),
            C('De ellas, no retribuidas', f'{X_LEG}!Permisos y Cómputo!D20', 'num'),
            C('Personas de la plantilla del caso', f'{X_POLI}!Cobertura por Estación!C27', 'num'),
            C('Personas del equipo con seguimiento individual', f'{X_REU}!Uno-a-uno!D30', 'num'),
            C('Horas de apertura al público de una semana completa', f'{X_SEM}!Parámetros!B37', 'num'),
        ],
        'sector': ['MM-08', 'MM-26', 'MM-27', 'MM-54'],
        'tablas': [{
            'titulo': 'Permisos y cómputo, con las dos figuras del permiso parental separadas (calendario-cumplimiento-legal.xlsx, hoja «Permisos y Cómputo»)',
            'src': (X_LEG, 'Permisos y Cómputo'),
            'cols': [('#', 'A', 'num'), ('Permiso o figura', 'B', 'txt'),
                     ('Duración o cómputo', 'C', 'txt'),
                     ('¿Retribuido?', 'D', 'txt'), ('Artículo', 'F', 'txt')],
            'filas': (6, 15),
            'nota': V_ET,
        }],
        'prohibido': None,
    },
    {
        'n': 13,
        'titulo': 'Rotación, Absentismo y Polivalencia: Qué se Puede Medir de Verdad',
        'resumen_indice': 'la fórmula de cada indicador, qué dato existe para hostelería, el punto único de fallo y el coste real de una baja.',
        'palabras': 1400, 'bloques': 2,
        'objetivo': 'Dar tres fórmulas limpias, decir con honestidad qué dato '
                    'existe y cuál no, y sustituir las cifras de coste de '
                    'reemplazo que circulan sin fuente por un cálculo hecho con '
                    'los datos del propio lector.',
        'epigrafes': [
            'Tres indicadores distintos y una fórmula para cada uno',
            'Qué dato existe para hostelería y cuál no',
            'La matriz de polivalencia y el punto único de fallo',
            'El plan de cross-training: quién enseña a quién y para cuándo',
            'Cuánto te cuesta de verdad una baja',
        ],
        'puntos': [
            'Las tres fórmulas, escritas para que se puedan aplicar el mismo '
            'día: rotación como bajas del periodo sobre plantilla media del '
            'periodo; absentismo como horas no trabajadas por ausencia sobre '
            'horas pactadas, con las vacaciones FUERA del numerador; y '
            'temporalidad como contratos temporales sobre asalariados.',
            'Honestidad sobre las fuentes, que es el argumento del capítulo: la '
            'tasa de rotación del sector que circula por todas partes no tiene '
            'informe publicado y se le atribuyen dos emisores distintos, así '
            'que no se cita. El absentismo de hostelería SÍ existe, y es del '
            'INE, con horas pactadas y horas no trabajadas por trabajador y '
            'mes. Un manual que sabe cuál de las dos citar es lo que se está '
            'comprando.',
            'Explicar la supervivencia empresarial en positivo y con su '
            'etiqueta exacta: la serie del INE por cohorte, y la de la sección '
            'de hostelería frente a la del conjunto de actividades. Y decir por '
            'qué NO se puede convertir en una tasa de fracaso de restaurantes.',
            'La matriz de polivalencia: nivel mínimo para dar una estación por '
            'cubierta, nivel a partir del cual alguien puede enseñarla, y el '
            'umbral de punto único de fallo. La estación con una sola persona '
            'capaz de sostenerla es un riesgo operativo con nombre y apellido, '
            'y en el caso del pack hay exactamente una.',
            'El plan de cross-training convierte el diagnóstico en fechas: '
            'quién sube de nivel, en qué estación, quién le enseña y para '
            'cuándo. Sin las cuatro cosas, la matriz sólo sirve para '
            'preocuparse.',
            'El coste de una baja calculado en dos bloques: el coste directo '
            '—horas de selección, horas de quien enseña y horas de la persona '
            'nueva a rendimiento bajo— y la venta que se deja de hacer mientras '
            'el equipo va corto. La suma suele sorprender, y es la cifra con la '
            'que se defiende un plan de formación ante el propietario.',
        ],
        'cifras': [
            C('Personas registradas en la matriz', f'{X_POLI}!Cobertura por Estación!C27', 'num'),
            C('Estaciones registradas', f'{X_POLI}!Cobertura por Estación!C26', 'num'),
            C('Estaciones en riesgo de punto único de fallo', f'{X_POLI}!Cobertura por Estación!C28', 'num'),
            C('Peso de las estaciones en riesgo sobre el total', f'{X_POLI}!Cobertura por Estación!C31', 'pct1'),
            C('Personas que sostienen «Fríos y entrantes»', f'{X_POLI}!Cobertura por Estación!B13', 'num'),
            C('Cobertura de «Fríos y entrantes»', f'{X_POLI}!Cobertura por Estación!E13', 'pct1'),
            C('Coste directo de cubrir una baja', f'{X_POLI}!Coste de una Baja!B15', 'eur2'),
            C('Margen que no se gana mientras el equipo recupera el ritmo', f'{X_POLI}!Coste de una Baja!B22', 'eur2'),
            C('Impacto estimado total de la baja', f'{X_POLI}!Coste de una Baja!B28', 'eur2'),
            C('Acciones registradas en el plan de cross-training', f'{X_POLI}!Plan de Cross-Training!C32', 'num'),
        ],
        'sector': ['MM-42', 'MM-43', 'MM-56', 'MM-55', 'MM-48'],
        'tablas': [
            {
                'titulo': 'Cobertura por estación: quién la sostiene, quién puede enseñarla y dónde salta la alerta (matriz-formacion-polivalencia.xlsx, hoja «Cobertura por Estación»)',
                'src': (X_POLI, 'Cobertura por Estación'),
                'cols': [('Estación', 'A', 'txt'), ('Personas que la sostienen', 'B', 'num'),
                         ('Personas que pueden enseñarla', 'C', 'num'),
                         ('Cobertura (%)', 'E', 'pct1'), ('Alerta', 'F', 'txt')],
                'filas': (12, 17),
            },
            {
                'titulo': 'El coste directo de cubrir una baja, concepto a concepto (matriz-formacion-polivalencia.xlsx, hoja «Coste de una Baja»)',
                'src': (X_POLI, 'Coste de una Baja'),
                'cols': [('Concepto', 'A', 'txt'), ('Valor', 'B', 'num2'), ('Nota', 'C', 'txt')],
                'filas': (6, 15),
                'nota': 'Las horas y los costes por hora son casillas editables: pon los tuyos y '
                        'el total se recalcula. Este bloque es sólo el coste directo; la venta '
                        'que se deja de hacer se calcula aparte, en la misma hoja.',
            },
        ],
        'prohibido': None,
    },
    {
        'n': 14,
        'titulo': 'Evaluar, Corregir y, si Toca, Despedir',
        'resumen_indice': 'el estándar escrito, el régimen disciplinario del ALEH VI, la audiencia previa de dos días y los números del despido.',
        'palabras': 1500, 'bloques': 2,
        'objetivo': 'Que el lector sepa corregir sin abrir un conflicto y, '
                    'cuando no haya más remedio, sepa el procedimiento exacto. '
                    'El foco del capítulo es la novedad que casi nadie ha '
                    'incorporado todavía: la audiencia previa al despido '
                    'disciplinario.',
        'epigrafes': [
            'Evaluar es comparar contra un estándar escrito',
            'Corregir en el momento: la amonestación que sirve de algo',
            'El régimen disciplinario del ALEH VI, falta por falta',
            'La audiencia previa: dos días, su excepción y qué pasa si te la saltas',
            'Objetivo, improcedente y finiquito: los números del despido',
        ],
        'puntos': [
            'La tesis: no se puede corregir lo que no estaba escrito antes. '
            'Evaluar es comparar contra un estándar que la persona conocía; sin '
            'estándar, cualquier corrección se vive como algo personal y '
            'cualquier sanción es discutible.',
            'La amonestación útil: hecho concreto, efecto, expectativa y fecha '
            'de seguimiento, dicha en privado y anotada. La que no sirve es la '
            'que se dice en el pase, delante de todos y en general.',
            'Recorrer el régimen disciplinario del acuerdo estatal tal y como '
            'ha quedado tras la modificación del 4 de septiembre de 2026, '
            'incluidas las faltas nuevas, y explicar que sancionar exige '
            'tipificar: hay que decir qué falta es y por qué, no «por mal '
            'comportamiento».',
            'La audiencia previa al despido disciplinario, que es la novedad '
            'del capítulo: antes de entregar la carta hay que informar de los '
            'hechos imputados y de su posible calificación jurídica y dar dos '
            'días para contestar; si se aparta a la persona del servicio esos '
            'días, son permiso retribuido. La propia norma trae una excepción, '
            'y hay que decirla también. Saltárselo abre la puerta a la '
            'improcedencia.',
            'Los números del despido, con su artículo: la indemnización del '
            'despido objetivo con su tope y la obligación de ponerla a '
            'disposición junto con la carta, la del improcedente con el suyo, y '
            'el régimen de los contratos anteriores a la reforma de 2012. Y '
            'recordar que el finiquito no es la indemnización.',
            'Cross-sell: la ficha de evaluación del desempeño está en el Kit de '
            'Gestión de Personal; aquí se decide qué se hace con el resultado.',
        ],
        'cifras': [
            C('Filas del cuadro del régimen disciplinario', f'{X_LEG}!Régimen Disciplinario ALEH!E18', 'num'),
            C('Faltas leves tipificadas', f'{X_LEG}!Régimen Disciplinario ALEH!E19', 'num'),
            C('Faltas graves tipificadas', f'{X_LEG}!Régimen Disciplinario ALEH!E20', 'num'),
            C('Faltas muy graves tipificadas', f'{X_LEG}!Régimen Disciplinario ALEH!E21', 'num'),
            C('Días de vigencia que le quedan a la modificación del ALEH VI', f'{X_LEG}!Régimen Disciplinario ALEH!E25', 'num'),
            C('Personas de la plantilla del caso', f'{X_POLI}!Cobertura por Estación!C27', 'num'),
            C('Acuerdos registrados en el trimestre', f'{X_REU}!Actas y Acuerdos!D46', 'num'),
        ],
        'sector': ['MM-12', 'MM-13'],
        'tablas': [{
            'titulo': 'El régimen disciplinario del ALEH VI tras la modificación del 4 de septiembre de 2026 (calendario-cumplimiento-legal.xlsx, hoja «Régimen Disciplinario ALEH»)',
            'src': (X_LEG, 'Régimen Disciplinario ALEH'),
            'cols': [('Falta o figura', 'B', 'txt'), ('Tipo', 'C', 'txt'),
                     ('Gravedad', 'D', 'txt'), ('Umbral o detalle', 'E', 'txt'),
                     ('Artículo', 'G', 'txt')],
            'filas': (6, 15),
            'nota': V_ALEH,
        }],
        'prohibido': None,
    },
    {
        'n': 15,
        'titulo': 'Lo que Obliga Aunque Seáis Tres: Igualdad, Acoso, Desconexión y PRL',
        'resumen_indice': 'lo que no tiene umbral de plantilla, cómo se cuenta de verdad la plantilla y por qué el reconocimiento médico es voluntario.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Desmontar la creencia más cara del pequeño hostelero: '
                    '«esto es para empresas grandes». Hay obligaciones sin '
                    'umbral de plantilla que un bar de dos personas tiene que '
                    'cumplir, y hay otras que dependen de un cómputo que casi '
                    'nadie hace bien.',
        'epigrafes': [
            'Registro retributivo: sin umbral de plantilla',
            'Protocolo frente al acoso: sin umbral, y qué tiene que decir',
            'Plan de igualdad desde 50: cómo se cuenta la plantilla de verdad',
            'Desconexión digital: el grupo de WhatsApp del servicio',
            'PRL: plan, evaluación, emergencias y formación en el momento de contratar',
            'Por qué el reconocimiento médico es voluntario',
        ],
        'puntos': [
            'Empezar por lo que no admite discusión: el registro retributivo y '
            'el protocolo frente al acoso NO tienen umbral de plantilla. Un '
            'local con dos personas contratadas los necesita, y las dos cosas '
            'están entre lo primero que pide una inspección.',
            'Explicar qué tiene que recoger el registro retributivo y por qué '
            'incluye al personal directivo, sin convertirlo en una clase de '
            'derecho: lo que el manager necesita saber es qué documento debe '
            'existir y quién lo mantiene actualizado.',
            'El cómputo real de la plantilla para el plan de igualdad, que es '
            'donde se equivoca todo el mundo: entran los fijos-discontinuos, '
            'los temporales y el personal de empresas de trabajo temporal, cada '
            'persona a tiempo parcial cuenta como una persona, y los temporales '
            'ya extinguidos suman según la regla que fija la norma. Un '
            'restaurante estacional puede cruzar el umbral sin notarlo.',
            'Desconexión digital: la empresa tiene que elaborar una política '
            'interna escrita, previa audiencia de la representación de la '
            'plantilla, y alcanza también a los puestos directivos. Aterrizarlo '
            'en el sitio donde de verdad ocurre en un restaurante: el grupo de '
            'mensajería del servicio, los cambios de turno a medianoche y las '
            'fotos del pase en el día libre.',
            'PRL en cuatro documentos que sí o sí existen —plan de prevención, '
            'evaluación de riesgos, planificación de la actividad preventiva y '
            'medidas de emergencia— y una obligación de formación que va en el '
            'momento de la contratación, dentro de jornada, y cuyo coste no '
            'recae en ningún caso sobre la persona trabajadora.',
            'El error más frecuente de todo el bloque: los reconocimientos '
            'médicos son voluntarios y sólo caben con el consentimiento de la '
            'persona, salvo las excepciones tasadas de la norma y previo '
            'informe de la representación de la plantilla. Y la empresa nunca '
            'recibe el informe médico, sólo las conclusiones de aptitud.',
        ],
        'cifras': [
            C('Documentos obligatorios registrados en el libro legal', f'{X_LEG}!Documentación Obligatoria!D25', 'num'),
            C('Puntos de control registrados en el calendario', f'{X_LEG}!Calendario y Vencimientos!D38', 'num'),
            C('Puntos con periodicidad fijada por una norma estatal', f'{X_LEG}!Calendario y Vencimientos!D39', 'num'),
            C('Puntos cuya periodicidad es criterio de la casa', f'{X_LEG}!Calendario y Vencimientos!D40', 'num'),
            C('Personas de la plantilla del caso', f'{X_POLI}!Cobertura por Estación!C27', 'num'),
            C('Normas en seguimiento en la hoja de estado normativo', f'{X_LEG}!Estado Normativo!C21', 'num'),
        ],
        'sector': ['MM-18', 'MM-19', 'MM-20', 'MM-21', 'MM-28'],
        'tablas': [{
            'titulo': 'Qué obliga con qué plantilla, y qué documento lo acredita',
            'cabecera': ['Obligación', 'Desde cuántas personas', 'Qué documento existe', 'Norma'],
            'filas': [
                ['Registro retributivo',
                 'Sin umbral: desde la primera persona contratada',
                 'Registro con la media aritmética y la mediana de lo realmente devengado, desglosado por sexo y por grupo',
                 'Art. 28.2 ET y RD 902/2020'],
                ['Protocolo frente al acoso sexual y por razón de sexo',
                 'Sin umbral',
                 'Procedimiento escrito de prevención y de cauce de las denuncias, publicado y accesible',
                 'Art. 48 de la Ley Orgánica 3/2007'],
                ['Política escrita de desconexión digital',
                 'Sin umbral',
                 'Política interna elaborada previa audiencia de la representación de la plantilla',
                 'Art. 88 de la Ley Orgánica 3/2018'],
                ['Plan de prevención, evaluación de riesgos y medidas de emergencia',
                 'Sin umbral',
                 'Los cuatro documentos, en el centro de trabajo',
                 'Arts. 16, 20 y 23 de la Ley 31/1995'],
                ['Formación en prevención de riesgos',
                 'Sin umbral',
                 'Justificante de la formación recibida en el momento de la contratación, dentro de jornada',
                 'Art. 19 de la Ley 31/1995'],
                ['Plan de igualdad',
                 'A partir de 50 personas, con el cómputo de la norma',
                 'Plan negociado e inscrito en el registro público',
                 'Art. 45 de la Ley Orgánica 3/2007 y RD 901/2020'],
                ['Conjunto planificado de medidas LGTBI',
                 'A partir de más de 50 personas',
                 'Medidas acordadas mediante negociación colectiva',
                 'Art. 15.1 de la Ley 4/2023 y RD 1026/2024'],
            ],
            'nota': 'Verificado el 04-09-2026 · Estatuto de los Trabajadores (RDLeg 2/2015), Ley 31/1995, '
                    'Ley Orgánica 3/2007, Ley Orgánica 3/2018 y Ley 4/2023 · '
                    'https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430',
        }],
        'prohibido': None,
    },
    {
        'n': 16,
        'titulo': 'El Servicio: Estándares, Briefing y la Conversación Cocina-Sala',
        'resumen_indice': 'los tres formatos de reunión, el guion de siete minutos, los estándares escritos y el conflicto que es de sistema.',
        'palabras': 1400, 'bloques': 2,
        'objetivo': 'Que el lector monte los tres rituales de comunicación que '
                    'sostienen un servicio —briefing, reunión y handover— con '
                    'guion, duración y responsable, y que deje de tratar el '
                    'conflicto entre cocina y sala como un problema de '
                    'caracteres.',
        'epigrafes': [
            'Briefing, reunión y handover: tres formatos, tres momentos',
            'El briefing de siete minutos: qué entra y qué no entra',
            'Estándares escritos: sin ellos no se puede corregir',
            'Cocina y sala: un problema de sistema, no de personas',
            'Corregir en el momento sin humillar a nadie',
        ],
        'puntos': [
            'Separar los tres formatos: el briefing es previo al servicio, '
            'diario y de pie; la reunión es semanal o mensual, se sienta y deja '
            'acta con responsable y fecha; el handover es el traspaso entre '
            'turnos y es un documento. Llamarlos a todos «la reunión» es lo que '
            'hace que no se celebre ninguno.',
            'El guion del briefing, con los puntos y el reparto de minutos: '
            'qué hay hoy, qué falta, qué reservas y qué alergias, quién está en '
            'cada estación y una sola cosa que se quiere mejorar respecto de '
            'ayer. Lo que NO entra: broncas, temas de una sola persona y nada '
            'que requiera discusión.',
            'La reunión semanal con guion cerrado y duración pactada: sin '
            'guion, se va en quejas; con guion, se cierra en el tiempo previsto '
            'y produce acuerdos. Y el punto que trae el equipo por turno '
            'rotatorio, que es el que la convierte en algo que la gente quiere '
            'que ocurra.',
            'Los estándares escritos como condición previa de todo lo anterior: '
            'tiempos objetivo entre pases, cómo se canta una comanda, qué se '
            'hace con un plato devuelto. Sin estándar no hay corrección '
            'posible, sólo opinión contra opinión.',
            'El conflicto cocina-sala reformulado: un plato que sale tarde, una '
            'comanda mal cantada o una alergia que no llega a cocina casi nunca '
            'son un problema de actitud; son un problema de protocolo de '
            'comunicación. Se arregla cambiando el sistema —quién canta, quién '
            'confirma, dónde se anota la alergia—, no reuniendo a las dos '
            'partes a que se expliquen.',
            'La corrección en caliente: se corrige el HECHO, en corto, sin '
            'público y sin adjetivos, y se vuelve a ello después del servicio '
            'si hace falta. Humillar delante del equipo cuesta más servicio del '
            'que salva.',
        ],
        'cifras': [
            C('Puntos del guion de la reunión semanal', f'{X_REU}!Guion de Reunión Semanal!D18', 'num'),
            C('Duración total del guion', f'{X_REU}!Guion de Reunión Semanal!D19', 'num'),
            C('Duración objetivo de la reunión', f'{X_REU}!Guion de Reunión Semanal!D20', 'num'),
            C('Reuniones registradas en el trimestre', f'{X_REU}!Calendario de Reuniones!D32', 'num'),
            C('Minutos de reunión del trimestre', f'{X_REU}!Calendario de Reuniones!D38', 'num'),
            C('Horas de reunión del trimestre', f'{X_REU}!Calendario de Reuniones!D40', 'num1'),
            C('Duración media de una reunión', f'{X_REU}!Calendario de Reuniones!D39', 'num1'),
            C('Puntos de control de la auditoría interna', f'{X_AUD}!Resumen por Área!B16', 'num'),
        ],
        'sector': [],
        'tablas': [
            {
                'titulo': 'El guion de la reunión semanal, punto a punto y minuto a minuto (reuniones-acuerdos-plan-90-dias.xlsx, hoja «Guion de Reunión Semanal»)',
                'src': (X_REU, 'Guion de Reunión Semanal'),
                'cols': [('Orden', 'A', 'num'), ('Punto', 'B', 'txt'),
                         ('Minutos', 'C', 'num'),
                         ('Herramienta de la que salen los datos', 'D', 'txt'),
                         ('Responsable', 'E', 'txt')],
                'filas': (6, 15),
            },
            {
                'titulo': 'Las seis preguntas del uno-a-uno, y para qué sirve cada una (reuniones-acuerdos-plan-90-dias.xlsx, hoja «Uno-a-uno»)',
                'src': (X_REU, 'Uno-a-uno'),
                'cols': [('#', 'A', 'num'), ('Pregunta', 'B', 'txt'),
                         ('Para qué sirve', 'C', 'txt')],
                'filas': (6, 11),
                'nota': 'El uno-a-uno no es una evaluación ni una bronca: es el único sitio donde '
                        'se entera uno de lo que no se dice en el pase.',
            },
        ],
        'prohibido': None,
    },
    {
        'n': 17,
        'titulo': 'Quejas, Hojas de Reclamaciones y Reseñas: Tres Cosas Distintas',
        'resumen_indice': 'el protocolo en sala, la hoja oficial y sus plazos autonómicos, quién responde las reseñas y qué dicen tus quejas contadas.',
        'palabras': 1500, 'bloques': 2,
        'objetivo': 'Separar tres cosas que en la práctica se tratan igual y '
                    'no lo son: una queja en sala, una reclamación formal con '
                    'plazo legal de respuesta y una reseña pública. Cada una '
                    'tiene su protocolo, su plazo y su responsable.',
        'epigrafes': [
            'La queja en sala: el protocolo de los primeros cinco minutos',
            'La hoja de reclamaciones: qué es, qué obliga y quién pone los plazos',
            'Los plazos de tu comunidad y cómo se cuentan',
            'Reseñas: quién responde, en cuántos días y con qué tono',
            'Qué te dicen tus quejas cuando las cuentas',
        ],
        'puntos': [
            'La queja en sala se resuelve en el sitio o no se resuelve: '
            'escuchar sin interrumpir, no discutir el hecho, ofrecer una '
            'solución concreta y anotarla. Lo que la convierte en gestión es lo '
            'último, no lo tercero.',
            'La hoja de reclamaciones NO es una queja: es un procedimiento '
            'administrativo con competencia AUTONÓMICA. Hay que tenerla, hay '
            'que anunciarla con cartel y hay un plazo para contestar por '
            'escrito que cambia según la comunidad. Negarse a entregarla es una '
            'infracción por sí misma.',
            'Explicar que el plazo se cuenta distinto según la comunidad —en '
            'días naturales en unas y en días hábiles en otras— y que ésa es la '
            'razón por la que la herramienta trae una casilla editable para el '
            'resto de comunidades: aquí sólo se dan los plazos verificados.',
            'Reseñas: se responde a todas dentro de un plazo propio, responde '
            'siempre la misma persona, y el tono es el mismo tanto si la reseña '
            'es justa como si no. Lo que NO se hace: discutir hechos en '
            'público, insinuar que el cliente miente ni pedir la retirada.',
            'El giro del capítulo: una queja suelta es una anécdota; treinta '
            'quejas clasificadas por motivo son un plan de trabajo. Enseñar el '
            'recuento del caso, cuál es el motivo que más se repite y qué '
            'decisión sale de ahí.',
            'El acuerdo de nivel de servicio de la casa: cada gravedad tiene su '
            'plazo de cierre en días, y lo que se mide no es la queja, es si '
            'se cerró dentro del plazo que uno mismo se puso.',
        ],
        'cifras': [
            C('Quejas registradas en el trimestre', f'{X_QUEJ}!Resumen!D11', 'num'),
            C('Motivo de queja más repetido', f'{X_QUEJ}!Resumen!D12', 'txt'),
            C('Quejas de ese motivo', f'{X_QUEJ}!Resumen!D13', 'num'),
            C('Tiempo medio hasta el cierre de una queja, en días', f'{X_QUEJ}!Resumen!D16', 'num1'),
            C('Quejas cerradas dentro del plazo de la casa', f'{X_QUEJ}!Resumen!D17', 'num'),
            C('Cumplimiento del plazo de cierre', f'{X_QUEJ}!Resumen!D19', 'pct1'),
            C('Reclamaciones formales registradas', f'{X_QUEJ}!Resumen!D40', 'num'),
            C('Reclamaciones contestadas dentro de plazo', f'{X_QUEJ}!Resumen!D43', 'pct1'),
            C('Reseñas registradas', f'{X_QUEJ}!Resumen!D46', 'num'),
            C('Media de estrellas de las reseñas', f'{X_QUEJ}!Resumen!D47', 'num2'),
        ],
        'sector': ['MM-45', 'MM-40'],
        'tablas': [
            {
                'titulo': 'El plazo para contestar una reclamación formal depende de tu comunidad (quejas-reclamaciones-resenas.xlsx, hoja «Parámetros»)',
                'src': (X_QUEJ, 'Parámetros'),
                'cols': [('Comunidad', 'A', 'txt'), ('Plazo legal', 'B', 'txt'),
                         ('Días para el aviso', 'C', 'num'), ('Se cuentan', 'D', 'txt')],
                'filas': (15, 17),
                'saltar_vacias': False,
                'nota': 'Verificado el 04-09-2026 · Cataluña: Decret 121/2013 y art. 126-9 de la Llei 22/2010; '
                        'Andalucía: Decreto 82/2022, arts. 4, 7 y 12 · '
                        'https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430 — la tercera fila es una '
                        'casilla editable: consulta la norma de tu comunidad y escribe ahí tu plazo.',
            },
            {
                'titulo': 'Las quejas del trimestre, contadas por motivo (quejas-reclamaciones-resenas.xlsx, hoja «Resumen»)',
                'src': (X_QUEJ, 'Resumen'),
                'cols': [('Motivo', 'A', 'txt'), ('Quejas', 'C', 'num'),
                         ('Porcentaje del total', 'D', 'pct1'),
                         ('Días medios hasta el cierre', 'E', 'num1'),
                         ('Fuera del plazo de la casa', 'F', 'num')],
                'filas': (22, 31),
            },
        ],
        'prohibido': None,
    },
    {
        'n': 18,
        'titulo': 'Reservas, No-shows y Datos del Cliente',
        'resumen_indice': 'la reserva como contrato, qué baja de verdad el no-show, la política de garantía y el RGPD sin consentimiento.',
        'palabras': 1400, 'bloques': 2,
        'objetivo': 'Que el lector deje de tratar el no-show como mala suerte y '
                    'monte una política de reservas con niveles, sabiendo qué '
                    'puede pedir, cómo se comunica y qué base legal sostiene el '
                    'tratamiento de los datos del cliente.',
        'epigrafes': [
            'La reserva es un contrato: qué se puede pedir y qué no',
            'No-show: cómo se mide y qué lo baja de verdad',
            'La política de garantía y cómo se comunica sin espantar',
            'La espera: qué cuesta y qué se puede hacer con ella',
            'RGPD en la reserva: base legal, registro de tratamiento y marketing aparte',
        ],
        'puntos': [
            'Encuadrar la reserva como lo que es: un compromiso recíproco. Eso '
            'es lo que permite pedir una garantía, y también lo que obliga a '
            'cumplir por el lado del restaurante cuando la mesa no está a la '
            'hora.',
            'Medir el no-show antes de combatirlo: reservas no presentadas '
            'sobre reservas confirmadas, por franja y por día de la semana. Sin '
            'ese desglose no se sabe si el problema es del viernes noche o de '
            'todo el año, y se acaba aplicando una política general a un '
            'problema local.',
            'Los tres niveles de garantía, de menos a más fricción: '
            'reconfirmación, tarjeta en garantía y prepago. Cada uno se aplica '
            'a un supuesto distinto —grupo grande, franja de máxima demanda, '
            'menú cerrado— y se comunica ANTES de que el cliente reserve, nunca '
            'después.',
            'El dato del sector se usa con su acotación: la tasa media de '
            'no-show del sector español y la caída cuando la reserva va '
            'garantizada con tarjeta, dichas con la fuente y con el año, y '
            'advirtiendo de que la cifra de la reconfirmación por mensaje viene '
            'de un solo día y de un subgrupo de reservas.',
            'RGPD sin mitos: los datos de la reserva se tratan por ejecución '
            'del contrato, así que NO hace falta pedir consentimiento para '
            'gestionarla; lo que sí exige consentimiento separado es el '
            'marketing posterior. Y un restaurante sí debe llevar registro de '
            'actividades de tratamiento.',
            'La espera como parte del servicio: se comunica un tiempo, se '
            'cumple o se corrige el tiempo comunicado, y se anota. La mesa que '
            'espera sin información es la que acaba en la columna de «espera '
            'excesiva» del registro de quejas.',
        ],
        'cifras': [
            C('Cubiertos del año', f'{X_SEM}!Semana!S57', 'num'),
            C('Tickets del año', f'{X_SEM}!Semana!T57', 'num'),
            C('Gasto medio por cubierto del año', f'{X_SEM}!Semana!V57', 'eur2'),
            C('Cubiertos por hora de apertura del año', f'{X_SEM}!Semana!X57', 'num1'),
            C('Quejas por reserva no encontrada', f'{X_QUEJ}!Resumen!C28', 'num'),
            C('Peso de esas quejas sobre el total', f'{X_QUEJ}!Resumen!D28', 'pct1'),
            C('Quejas por espera excesiva', f'{X_QUEJ}!Resumen!C22', 'num'),
            C('Días medios hasta cerrar una queja por espera', f'{X_QUEJ}!Resumen!E22', 'num1'),
        ],
        'sector': ['MM-46'],
        'tablas': [{
            'titulo': 'Los tres niveles de garantía de una reserva, y cuándo tiene sentido cada uno',
            'cabecera': ['Nivel', 'Qué se le pide al cliente', 'Cuándo tiene sentido', 'Qué hay que decirle antes de reservar'],
            'filas': [
                ['Reconfirmación',
                 'Confirmar por mensaje o por teléfono el mismo día',
                 'Reservas normales de dos a cuatro personas',
                 'Que se le escribirá y que sin respuesta la mesa se libera a una hora concreta'],
                ['Tarjeta en garantía',
                 'Los datos de una tarjeta, sin cargo',
                 'Grupos grandes, franjas de máxima demanda y fechas señaladas',
                 'El importe que se cargaría por persona si no acude y con cuánta antelación puede anular sin coste'],
                ['Prepago',
                 'El pago por adelantado del menú',
                 'Menús cerrados, eventos y servicios con producto encargado a medida',
                 'Qué incluye, qué pasa si anula y en qué plazo se devuelve'],
            ],
            'nota': 'La regla que sostiene los tres niveles: la condición se comunica ANTES de '
                    'que el cliente confirme la reserva, por escrito y con el importe exacto. '
                    'Una garantía comunicada después no es una garantía, es una discusión.',
        }],
        'prohibido': None,
    },
    {
        'n': 19,
        'titulo': 'Seguridad Alimentaria y el Local: de lo que Responde el Manager',
        'resumen_indice': 'cultura de seguridad alimentaria, alérgenos, temperaturas vigentes, y el local: ruido, música, horarios, terraza y envases.',
        'palabras': 1800, 'bloques': 3,
        'objetivo': 'Reunir en un capítulo todo lo que le van a pedir al '
                    'manager cuando entre alguien con una carpeta, con las '
                    'normas VIGENTES y no con las que sigue citando medio '
                    'sector. Es el capítulo que más citas caducadas corrige.',
        'epigrafes': [
            'La cultura de seguridad alimentaria es obligación de la dirección',
            'Autocontrol: principios, responsable designado y qué se registra',
            'Alérgenos: por qué el cartel no basta',
            'Temperaturas, anisakis y trazabilidad: las cifras vigentes',
            'El local: ruido, música, horarios y las dos paredes de la terraza',
            'Agua, envases, comida sobrante y perros de asistencia',
        ],
        'puntos': [
            'Abrir por donde nadie abre: la cultura de seguridad alimentaria es '
            'una obligación de la DIRECCIÓN, no del último que entró en cocina. '
            'Eso convierte al manager en responsable de que exista, se comunique '
            'y se demuestre.',
            'El sistema de autocontrol explicado como lo que el manager tiene '
            'que sostener: un procedimiento permanente basado en los principios '
            'del sistema, con responsable designado, que se revisa cada vez que '
            'cambia un producto, un proceso o un proveedor. Los registros '
            'concretos ya están en el Pack APPCC y no se repiten aquí.',
            'Alérgenos: la información es obligatoria también en los platos sin '
            'envasar, y el cartel de «consulte al personal» no basta por sí '
            'solo: hace falta soporte escrito o electrónico accesible. Añadir '
            'la parte operativa: quién actualiza la ficha cuando cambia un '
            'proveedor.',
            'Las cifras vigentes de temperatura y de congelación preventiva, '
            'con la norma que las fija HOY, y decir expresamente que el real '
            'decreto de comidas preparadas que casi todo el sector sigue '
            'citando está derogado desde diciembre de 2022. Es la cita legal '
            'caducada más repetida del oficio.',
            'Trazabilidad de un paso atrás como obligación práctica: saber de '
            'quién viene cada producto y poder demostrarlo. Y el registro '
            'autonómico frente al registro general sanitario, con el umbral que '
            'lo cambia todo.',
            'El local, que casi nunca está en ningún manual: poner altavoces de '
            'música ambiental reclasifica la actividad y obliga a limitador '
            'registrador precintado; los derechos de autor y los conexos son '
            'DOS pagos distintos; los horarios son competencia autonómica; y '
            'una terraza es legal a efectos de tabaco si no está cubierta o si, '
            'estándolo, no tiene más de dos paredes.',
            'Cerrar con lo que el cliente ve: el agua no envasada gratuita que '
            'hay que OFRECER, no sólo dar si la piden; la obligación de '
            'permitir llevarse lo no consumido, con su excepción y con la '
            'obligación de informar de ello; y el acceso de los perros de '
            'asistencia, con la norma nueva.',
        ],
        'cifras': [
            C('Puntos de control registrados en el calendario', f'{X_LEG}!Calendario y Vencimientos!D38', 'num'),
            C('Puntos con periodicidad fijada por una norma estatal', f'{X_LEG}!Calendario y Vencimientos!D39', 'num'),
            C('Puntos cuya periodicidad es criterio de la casa', f'{X_LEG}!Calendario y Vencimientos!D40', 'num'),
            C('Puntos vencidos en la fecha de corte', f'{X_LEG}!Calendario y Vencimientos!D43', 'num'),
            C('Puntos en verde', f'{X_LEG}!Calendario y Vencimientos!D47', 'pct0'),
            C('Documentos obligatorios registrados', f'{X_LEG}!Documentación Obligatoria!D25', 'num'),
        ],
        'sector': ['MM-29', 'MM-31', 'MM-32', 'MM-33', 'MM-34', 'MM-35', 'MM-36',
                   'MM-38', 'MM-49', 'MM-50', 'MM-51', 'MM-52'],
        'tablas': [
            {
                'titulo': 'Las temperaturas y los tiempos que rigen hoy',
                'cabecera': ['Situación', 'Valor vigente', 'Norma'],
                'filas': [
                    ['Conservación en caliente', '63 °C o más', 'Art. 30 del RD 1086/2020'],
                    ['Refrigeración de comidas que se consumen en menos de 24 horas', '8 °C o menos', 'Art. 30 del RD 1086/2020'],
                    ['Refrigeración de comidas que se consumen en más de 24 horas', '4 °C o menos', 'Art. 30 del RD 1086/2020'],
                    ['Congelación', '−18 °C o menos', 'Art. 30 del RD 1086/2020'],
                    ['Enfriamiento rápido tras la cocción', 'De 60 °C a 10 °C en menos de 2 horas', 'Art. 30 del RD 1086/2020'],
                    ['Recalentado', '74 °C durante 15 segundos en el centro del producto', 'Art. 30 del RD 1086/2020'],
                    ['Congelación preventiva del anisakis', '−20 °C durante 24 horas, o −35 °C durante 15 horas, en la totalidad del producto', 'Art. 8.1 del RD 1021/2022'],
                ],
                'nota': V_TEMP + ' — el RD 3484/2000 y el RD 1420/2006 están derogados desde el '
                        '22 de diciembre de 2022: si tu documentación los cita, está caducada.',
            },
            {
                'titulo': 'Qué documentación te van a pedir, dónde tiene que estar y quién la pide (calendario-cumplimiento-legal.xlsx, hoja «Documentación Obligatoria»)',
                'src': (X_LEG, 'Documentación Obligatoria'),
                'cols': [('#', 'A', 'num'), ('Documento', 'B', 'txt'),
                         ('Dónde debe estar', 'C', 'txt'), ('Quién lo pide', 'D', 'txt')],
                'filas': (7, 22),
                'nota': 'Las columnas de «¿Disponible en el local?» y «Última comprobación» son '
                        'casillas editables: la hoja calcula sola el porcentaje de documentación '
                        'completada.',
            },
        ],
        'prohibido': None,
    },
    {
        'n': 20,
        'titulo': 'El Calendario del Manager, la Auditoría Interna y los 90 Días Siguientes',
        'resumen_indice': 'qué tiene fecha fijada por norma y qué no, la auditoría puntuable, y cómo se convierte todo lo anterior en trece semanas.',
        'palabras': 1400, 'bloques': 2,
        'objetivo': 'Cerrar el manual convirtiéndolo en trabajo: qué vence y '
                    'cuándo, qué se audita y con qué vara, y cómo se pasa de un '
                    'diagnóstico a veinte decisiones con responsable, semana y '
                    'fecha. El capítulo que evita que el libro se quede en la '
                    'estantería.',
        'epigrafes': [
            'Qué tiene fecha fijada por una norma y qué se vende como si la tuviera',
            'El calendario de vencimientos: cómo se monta y cómo se lee',
            'La auditoría interna: puntuar el servicio con la misma vara tres veces',
            'De la auditoría al plan: veinte decisiones con responsable y semana',
            'Qué se mide el primer día y qué se mide a los noventa',
        ],
        'puntos': [
            'El criterio que ningún blog del sector puede permitirse dar, '
            'porque casi todos venden el servicio: de todos los puntos de '
            'mantenimiento que se le venden a un restaurante, sólo unos pocos '
            'tienen periodicidad fijada por una norma estatal. Los demás son '
            'criterio de la casa, y decirlo así no es relajar el control: es '
            'saber dónde está la obligación y dónde está la buena práctica.',
            'Explicar la columna que hace ese trabajo en la herramienta —«¿lo '
            'fija una norma estatal?»— y qué se hace con cada respuesta: si es '
            'sí, la fecha no se negocia; si es no, se decide la periodicidad y '
            'se anota por qué.',
            'La auditoría interna como instrumento de dirección, no de castigo: '
            'los mismos puntos de control, el mismo peso por área y la misma '
            'escala en cada visita. Lo que interesa no es la nota, es la '
            'variación entre visitas y qué área empeora.',
            'El puente entre diagnóstico y ejecución, que es donde mueren casi '
            'todos los planes: cada decisión sale de una herramienta concreta, '
            'tiene un área, un responsable, una semana del uno al trece y un '
            'impacto estimado. Sin las cinco cosas no es una decisión, es una '
            'intención.',
            'Cerrar con la medición: qué se anota el primer día para poder '
            'comparar a los noventa, y por qué el prime cost de la semana, el '
            'cumplimiento del plazo de las quejas y la cobertura por estación '
            'son tres buenas cifras de arranque.',
            'Y el cierre honesto del manual: la ley cambia, y por eso cada '
            'afirmación de este libro va con su norma y su fecha de corte, y '
            'cada parámetro de las herramientas vive en una casilla editable. '
            'Lo que envejece es el documento; el método y la herramienta, no.',
        ],
        'cifras': [
            C('Puntos de control registrados en el calendario', f'{X_LEG}!Calendario y Vencimientos!D38', 'num'),
            C('Puntos con periodicidad fijada por una norma estatal', f'{X_LEG}!Calendario y Vencimientos!D39', 'num'),
            C('Puntos cuya periodicidad es criterio de la casa', f'{X_LEG}!Calendario y Vencimientos!D40', 'num'),
            C('Puntos vencidos en la fecha de corte', f'{X_LEG}!Calendario y Vencimientos!D43', 'num'),
            C('Puntos en verde', f'{X_LEG}!Calendario y Vencimientos!D47', 'pct0'),
            C('Puntuación ponderada de la primera visita de auditoría', f'{X_AUD}!Auditoría!E71', 'num2'),
            C('Puntuación ponderada de la tercera visita', f'{X_AUD}!Auditoría!I71', 'num2'),
            C('Cumplimiento de la tercera visita', f'{X_AUD}!Auditoría!I72', 'pct1'),
            C('Decisiones registradas en el plan de 90 días', f'{X_REU}!Plan 90 Días!D36', 'num'),
            C('Semanas que dura el plan', f'{X_REU}!Plan 90 Días!D48', 'num'),
        ],
        'sector': ['MM-02', 'MM-22', 'MM-35', 'MM-40'],
        'tablas': [
            {
                'titulo': 'El calendario de vencimientos: qué lo fija una norma y qué es criterio de la casa (calendario-cumplimiento-legal.xlsx, hoja «Calendario y Vencimientos»)',
                'src': (X_LEG, 'Calendario y Vencimientos'),
                'cols': [('Punto de control', 'B', 'txt'),
                         ('Periodicidad (meses)', 'D', 'num'),
                         ('¿Lo fija una norma estatal?', 'E', 'txt'),
                         ('Estado', 'H', 'txt')],
                'filas': (10, 35),
                'nota': 'Verificado el 04-09-2026 · las fuentes y los enlaces de cada punto están '
                        'en las columnas de la propia hoja · '
                        'https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430 — una periodicidad '
                        'de cero meses significa que el punto no vence porque se hace cada día.',
            },
            {
                'titulo': 'Las decisiones del trimestre, repartidas por área (reuniones-acuerdos-plan-90-dias.xlsx, hoja «Plan 90 Días»)',
                'src': (X_REU, 'Plan 90 Días'),
                'cols': [('Área', 'B', 'txt'), ('Decisiones', 'C', 'num'),
                         ('Impacto estimado (€/mes)', 'D', 'eur')],
                'filas': (56, 60),
                'nota': 'El impacto estimado es una hipótesis del propio manager, no una promesa: '
                        'se escribe al decidir y se compara a los noventa días con el impacto que '
                        'de verdad se consiguió.',
            },
        ],
        'prohibido': None,
    },
]

# --------------------------------------------------------------------------
# Prohibiciones ESPECÍFICAS por capítulo (1-3 cada uno). Se suman al NO_COMUN
# más abajo: `prohibido` = NO_COMUN + éstas.
# --------------------------------------------------------------------------
ESPECIFICAS = {
    1: [
        'NO presentes este manual como sustituto de los otros productos del '
        'catálogo ni digas que hacen falta para usarlo: son complementarios y '
        'hay que decirlo así, con su nombre y con lo que aporta cada uno.',
        'NO dibujes un organigrama con cinco cargos como si el convenio los '
        'tipificara. Lo que el convenio tiene son áreas funcionales y grupos '
        'profesionales; los cargos son denominaciones de uso de cada casa.',
    ],
    2: [
        'NO conviertas el capítulo en un glosario alfabético: cada indicador '
        'entra por el error que corrige, no por su definición de manual.',
        'NO confundas el margen tras prime cost con el beneficio: de ese margen '
        'todavía no han salido alquiler, suministros, seguros ni amortización, '
        'y hay que decirlo expresamente.',
    ],
    3: [
        'NO des un porcentaje de desviación «aceptable» entre una semana y otra '
        'ni un umbral de alarma que no esté en las cifras: lo que se enseña es '
        'a comparar contra el objetivo de la casilla y a mirar la tendencia.',
        'NO digas que el cierre mensual sobra: el mes sigue siendo la '
        'contabilidad. Lo que se defiende es que la semana llega a tiempo y el '
        'mes no.',
    ],
    4: [
        'NO escribas «el coste de la Seguridad Social es del 23,60 %» ni ninguna '
        'variante: ese porcentaje son sólo las contingencias comunes y el '
        'capítulo existe precisamente para corregir esa frase.',
        'NO presentes el 65 % y el 55 % como una cifra publicada por nadie: son '
        'criterio de la casa, derivado, y se dicen con esas palabras.',
        'NO calcules el coste de una persona concreta ni des una nómina de '
        'ejemplo: eso depende del convenio provincial y se remite a la '
        'plantilla de coste laboral del Kit de Gestión de Personal.',
    ],
    5: [
        'NO escribas otro checklist. Si aparece una lista, es de DECISIONES, no '
        'de tareas: las tareas ya están en el Kit de Tareas y se cita.',
        'NO metas en este capítulo los controles de seguridad alimentaria: '
        'tienen su propio capítulo y su propio producto.',
    ],
    6: [
        'NO des instrucciones de liquidación de impuestos ni expliques cómo se '
        'rellena ningún modelo tributario: eso es de la asesoría. Aquí se '
        'explica qué documento hay que emitir y qué obligación existe.',
        'NO afirmes que las propinas cotizan ni que no cotizan como si hubiera '
        'norma expresa: se dice exactamente lo que hay, que es que la norma de '
        'cotización no las menciona.',
        'NO sugieras que se puede dejar de aceptar efectivo «si se avisa»: no se '
        'puede, y ésa es la frase que el capítulo viene a corregir.',
    ],
    7: [
        'NO prometas al lector que conseguirá autonomía ni que su propietario '
        'le hará caso: lo que se le da es la forma de llevar una propuesta con '
        'un dato, que es lo único que sí controla.',
        'NO conviertas las señales de desgaste en un diagnóstico clínico: se '
        'describen conductas observables en el trabajo y se lleva la '
        'conversación a un uno-a-uno, sin etiquetar a nadie.',
    ],
    8: [
        'NO publiques tablas salariales de ninguna provincia ni des una cifra '
        'de salario por categoría: se remite a REGCON y al convenio provincial, '
        'que es donde están y donde cambian.',
        'NO digas que el acuerdo estatal fija los salarios: los remite '
        'expresamente al convenio provincial.',
    ],
    9: [
        'NO menciones el contrato de obra y servicio como si todavía existiera, '
        'ni siquiera como alternativa descartada sin decir que desapareció.',
        'NO des por buena ninguna duración de contrato temporal que no esté en '
        'la tabla o en los datos del sector, y no inventes supuestos de '
        'sustitución.',
    ],
    10: [
        'NO enumeres las materias sobre las que no se puede preguntar sin citar '
        'su norma y su artículo, y no conviertas ese epígrafe en una lista de '
        'anécdotas de entrevista.',
        'NO llames «carné de manipulador» a la formación en manipulación de '
        'alimentos: no existe ese carné desde 2010 y la obligación es del '
        'titular de la empresa.',
    ],
    11: [
        'NO escribas que el registro tiene que ser digital, ni que hay un '
        'sistema homologado, ni cites multas por no tenerlo digitalizado: el '
        'real decreto no está publicado y éste es el capítulo donde más daño '
        'haría escribirlo.',
        'NO digas que los quince minutos del descanso en jornada continuada son '
        'siempre tiempo de trabajo efectivo: sólo lo son si lo establece el '
        'convenio o el contrato.',
        'NO mezcles horas extraordinarias con horas complementarias: son dos '
        'figuras distintas, con topes distintos y para contratos distintos.',
    ],
    12: [
        'NO escribas «cinco días por fallecimiento»: son dos, ampliables en dos '
        'más si hay desplazamiento. Este capítulo existe en buena parte para '
        'corregir esa frase.',
        'NO trates el permiso parental como una sola figura: son dos, y hay que '
        'nombrar las dos con su artículo y decir cuál se paga.',
        'NO digas que la empresa decide la concreción horaria de la reducción '
        'por guarda legal: la elige la persona trabajadora dentro de su jornada '
        'ordinaria.',
    ],
    13: [
        'NO escribas ninguna tasa de rotación del sector: la que circula no '
        'tiene informe publicado. La rotación se calcula con los datos del '
        'lector.',
        'NO atribuyas a la hostelería el absentismo del «sector servicios»: el '
        'dato de hostelería es el del INE que te llega en los datos del sector.',
        'NO conviertas la supervivencia empresarial del INE en una tasa de '
        'cierre de restaurantes ni la escribas en negativo.',
    ],
    14: [
        'NO describas el despido disciplinario sin la audiencia previa: es la '
        'novedad del 4 de septiembre de 2026 y omitirla es el defecto que este '
        'capítulo viene a evitar. Y cita también su excepción.',
        'NO redactes una carta de despido ni des una plantilla de carta: se '
        'explica el procedimiento y se remite a la asesoría laboral.',
        'NO confundas el finiquito con la indemnización: son dos cosas '
        'distintas y hay que decirlo.',
    ],
    15: [
        'NO digas que el registro retributivo o el protocolo frente al acoso '
        'sólo obligan a partir de un número de personas: no tienen umbral.',
        'NO afirmes que los reconocimientos médicos son obligatorios, y cuando '
        'expliques las excepciones, cítalas con su artículo.',
        'NO des cuantías de sanción que no estén en los datos del sector de '
        'este capítulo.',
    ],
    16: [
        'NO conviertas el conflicto entre cocina y sala en un problema de '
        'caracteres ni propongas «hablar las cosas» como solución: se cambia el '
        'protocolo de comunicación, y eso es lo que hay que describir.',
        'NO metas en el briefing lo que no cabe en él (broncas, temas '
        'individuales, decisiones que requieren discusión): decir qué NO entra '
        'es la mitad del valor del guion.',
    ],
    17: [
        'NO des plazos de respuesta de comunidades autónomas que no estén en la '
        'tabla: sólo hay dos verificadas, y para el resto se remite al lector a '
        'la norma de su comunidad y a la casilla editable.',
        'NO trates la hoja de reclamaciones como una queja más: es un '
        'procedimiento con plazo legal, y negarse a entregarla es una '
        'infracción por sí misma.',
        'NO aconsejes pedir la retirada de una reseña ni discutir hechos en '
        'público con un cliente.',
    ],
    18: [
        'NO escribas ninguna cifra de no-show, de efecto de la reconfirmación '
        'ni de coste de la espera que no esté en los datos del sector, y cuando '
        'la escribas, ve con su acotación: la del mensaje de reconfirmación '
        'viene de un solo día y de un subgrupo de reservas.',
        'NO digas que hace falta el consentimiento del cliente para gestionar '
        'su reserva: la base es la ejecución del contrato. El consentimiento '
        'separado es para el marketing.',
    ],
    19: [
        'NO cites el RD 3484/2000 ni el RD 1420/2006 más que para decir que '
        'están derogados: es el error de cita más repetido del sector y aquí se '
        'corrige expresamente.',
        'NO presentes la limpieza de campana, el control de plagas, la '
        'calibración de termómetros ni la medición del aceite como obligaciones '
        'con periodicidad legal: no la tienen.',
        'NO escribas que un restaurante de menos de 1.300 metros cuadrados '
        'queda exento de la ley de desperdicio alimentario: la exención alcanza '
        'sólo a uno de los apartados de su artículo.',
    ],
    20: [
        'NO conviertas el capítulo en un resumen de los diecinueve anteriores: '
        'lo que aporta es el calendario, la auditoría y el plan, es decir, el '
        'paso de saber a hacer.',
        'NO prometas un resultado a los noventa días: se enseña qué medir el '
        'primer día para poder comparar, no cuánto se va a mejorar.',
    ],
}

for _cap in CAPITULOS:
    _cap['prohibido'] = NO_COMUN + ESPECIFICAS.get(_cap['n'], [])


# --------------------------------------------------------------------------
# El bonus: 12 situaciones resueltas (SPEC §4.2 y §8.1 de la síntesis)
#
# El molde es el del bonus de la Guía Food Cost —12 piezas de 600-660 palabras
# con tabla, un solo bloque cada una— pero el contenido es otro: no son
# ejercicios de cálculo, son SITUACIONES de manager. Los cinco epígrafes son
# los mismos en las doce, y ése es justamente el valor: el lector aprende el
# patrón de respuesta («qué NO hacer» antes que «qué hacer») y lo aplica a la
# situación 13, que será la suya.
# --------------------------------------------------------------------------
EPI_SIT = ['La situación',
           'Qué no hacer',
           'Protocolo paso a paso',
           'La norma que aplica',
           'La herramienta y el guion']

NO_COMUN_BONUS = NO_COMUN + [
    'Escribe la situación como una situación, no como un capítulo teórico: '
    'empieza por lo que está pasando, con la hora y el dato concretos, y '
    'termina con lo que el lector hace al salir de la oficina.',
    'El epígrafe «Qué no hacer» va ANTES del protocolo y es tan importante como '
    'él: son las reacciones reales que empeoran el caso, escritas en dos o tres '
    'frases cada una, no una lista de obviedades.',
    'El epígrafe «La norma que aplica» lleva la norma y el artículo, y cuando la '
    'norma sea de las verificadas para esta edición, la fecha: «verificado el 4 '
    'de septiembre de 2026». Si en la situación no aplica ninguna norma, se dice '
    'expresamente que es criterio de gestión y no obligación legal.',
    'Cuando la situación pida una conversación, escribe el GUION LITERAL de las '
    'frases de apertura entre comillas, no un resumen de lo que habría que '
    'decir. Es lo que el lector va a usar tal cual.',
    'No remitas al lector a «el capítulo tal de este manual» por su número: '
    'puedes decir de qué trata, porque este documento se lee suelto.',
]

BONUS = [
    {
        'nombre': 'BONUS-12-situaciones-resueltas',
        'guia': {
            'titulo': '12 Situaciones Resueltas del Manager de Restaurante',
            'subtitulo': 'Bonus del pack «Manual del Manager de Restaurante» · '
                         'con los datos de las siete herramientas Excel',
            'cabecera': 'AI Chef Pro · 12 Situaciones Resueltas del Manager',
            'portada_texto': (
                'Doce situaciones que le pasan a cualquier manager: una baja a '
                'dos horas del servicio, la caja que no cuadra, un cliente que '
                'pide la hoja de reclamaciones, una inspección sin avisar, un '
                'despido que hay que hacer bien. Cada una con los datos del '
                'caso, lo que NO hay que hacer, el protocolo paso a paso, la '
                'norma que aplica con su artículo y la herramienta del pack que '
                'se usa; y cuando hay que hablar con alguien, el guion literal '
                'de la conversación. No hay ninguna cifra inventada: cada '
                'número sale de una celda que puedes abrir y comprobar.'),
        },
        'gates': {
            'paginas_prometidas': 25,
            'palabras_objetivo': 7500,
            'min_palabras_cap': 450,
            'cifras_extra': (),
            'cifras_ignorar': (),
            'mortalidad_permitida': ['cierra', 'cierran'],
            'erratas_permitidas': ('actas', 'canta', 'cantó', 'canto', 'atendió', 'atendio', 'desapareció', 'desaparecio', 'rendía', 'rendia', 'alegar', 'anular', 'auditado', 'califica', 'cometido', 'contó', 'conto', 'digan', 'emitió', 'emitio', 'escribirá', 'escribira', 'fisco', 'libren', 'manía', 'mania', 'ofreció', 'ofrecio', 'proporcionales', 'vicio', 'ocurrió', 'ocurrio', 'acusa', 'acusando', 'señalado', 'senalado', ),
            'meta': {'title': '12 Situaciones Resueltas del Manager de Restaurante',
                     'subject': 'Bonus del pack Manual del Manager de Restaurante · '
                                'Versión 1.0 · septiembre 2026'},
        },
        'capitulos': [
            {
                'n': 1,
                'titulo': 'Una Baja a Dos Horas del Servicio del Viernes',
                'resumen_indice': 'quién puede cubrir la estación que se queda vacía, y qué se hace cuando la respuesta es «nadie».',
                'palabras': 600, 'bloques': 1,
                'objetivo': 'Convertir el pánico de las seis de la tarde en un '
                            'procedimiento de dos minutos: mirar la matriz, '
                            'decidir la cobertura y avisar. Y dejar claro que la '
                            'decisión de verdad se tomó semanas antes, cuando se '
                            'aceptó tener una estación con una sola persona.',
                'epigrafes': EPI_SIT,
                'puntos': [
                    'La situación: llamada a dos horas del servicio del viernes, '
                    'la persona que falta sostiene una estación concreta y hay '
                    'reservas confirmadas. Dar el número de personas del equipo '
                    'y la cobertura real de esa estación.',
                    'Qué NO hacer: llamar a todo el grupo del equipo a la vez, '
                    'pedir a alguien que doble sin mirar su descanso entre '
                    'jornadas, ni decidir a ojo quién puede cubrir sin mirar la '
                    'matriz.',
                    'Protocolo: comprobar en la matriz quién sostiene esa '
                    'estación, llamar por orden de nivel y no de amistad, '
                    'comprobar el descanso entre jornadas antes de proponer '
                    'nada, y si no hay nadie, reducir la oferta de la carta o '
                    'los cubiertos aceptados en vez de servir mal.',
                    'La norma: el descanso mínimo entre jornadas y el descanso '
                    'semanal no se saltan por una urgencia, y si la solución '
                    'genera horas extra hay un tope anual que vigilar.',
                    'La herramienta y el guion: la matriz de polivalencia y la '
                    'hoja de coste de una baja. Y la frase con la que se pide '
                    'que alguien venga, que no es «te necesito» sino una '
                    'petición con hora de entrada, hora de salida y qué se '
                    'compensa.',
                ],
                'cifras': [
                    C('Personas del equipo', f'{X_POLI}!Cobertura por Estación!C27', 'num'),
                    C('Estaciones de trabajo', f'{X_POLI}!Cobertura por Estación!C26', 'num'),
                    C('Estaciones en riesgo de punto único de fallo', f'{X_POLI}!Cobertura por Estación!C28', 'num'),
                    C('Personas que sostienen «Fríos y entrantes»', f'{X_POLI}!Cobertura por Estación!B13', 'num'),
                    C('Personas que pueden enseñar «Fríos y entrantes»', f'{X_POLI}!Cobertura por Estación!C13', 'num'),
                    C('Cobertura de «Fríos y entrantes»', f'{X_POLI}!Cobertura por Estación!E13', 'pct1'),
                    C('Cobertura de «Pase y caliente»', f'{X_POLI}!Cobertura por Estación!E12', 'pct1'),
                    C('Impacto estimado total de una baja', f'{X_POLI}!Coste de una Baja!B28', 'eur2'),
                ],
                'sector': ['MM-03'],
                'tablas': [{
                    'titulo': 'Quién puede cubrir cada estación, hoy (matriz-formacion-polivalencia.xlsx, hoja «Cobertura por Estación»)',
                    'src': (X_POLI, 'Cobertura por Estación'),
                    'cols': [('Estación', 'A', 'txt'), ('Personas que la sostienen', 'B', 'num'),
                             ('Personas que pueden enseñarla', 'C', 'num'),
                             ('Cobertura (%)', 'E', 'pct1'), ('Alerta', 'F', 'txt')],
                    'filas': (12, 17),
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 2,
                'titulo': 'La Caja Descuadra 40 Euros Tres Días Seguidos',
                'resumen_indice': 'cómo se acota un descuadre repetido sin acusar a nadie, y en qué orden se descartan las causas.',
                'palabras': 620, 'bloques': 1,
                'objetivo': 'Dar el orden de descarte que evita el error más '
                            'caro de esta situación: empezar por sospechar de '
                            'una persona. Se empieza por el sistema, se sigue '
                            'por el proceso y sólo al final se habla con '
                            'alguien.',
                'epigrafes': EPI_SIT,
                'puntos': [
                    'La situación: tres cierres seguidos con la misma '
                    'diferencia y en el mismo turno. Situarla con el ticket '
                    'medio y el volumen de tickets del negocio, para que se vea '
                    'que es una cantidad pequeña que se repite, que es lo que '
                    'la hace significativa.',
                    'Qué NO hacer: preguntar en el grupo del equipo, cambiar a '
                    'la persona de turno «por si acaso», o dar el descuadre por '
                    'bueno porque «es poco dinero». Las tres cosas destruyen la '
                    'posibilidad de encontrarlo.',
                    'Protocolo en tres pasadas: primero el sistema '
                    '—anulaciones, invitaciones, cambios de forma de pago, '
                    'propinas cobradas por tarjeta—; después el proceso —fondo '
                    'de caja, cambios de turno sin corte, cobros con la caja '
                    'abierta—; y sólo entonces la conversación, que se tiene en '
                    'privado y con el dato delante, no con la sospecha.',
                    'La norma: aquí no hay norma que obligue a un procedimiento '
                    'concreto de arqueo, y hay que decirlo; lo que sí hay es '
                    'régimen disciplinario si al final aparece una conducta '
                    'tipificada, y entonces el procedimiento es el del manual, '
                    'con audiencia previa incluida.',
                    'La herramienta y el guion: el cuadro de mando semanal para '
                    'ver si el descuadre está moviendo el margen y el registro '
                    'de quejas por cobro incorrecto, que suele contar la otra '
                    'mitad de la historia. Y la frase de apertura de la '
                    'conversación, que empieza por el proceso y no por la '
                    'persona.',
                ],
                'cifras': [
                    C('Ticket medio del año', f'{X_SEM}!Semana!U57', 'eur2'),
                    C('Tickets del año', f'{X_SEM}!Semana!T57', 'num'),
                    C('Ventas netas totales del año', f'{X_SEM}!Semana!E57', 'eur'),
                    C('Margen tras prime cost del año', f'{X_SEM}!Semana!R57', 'eur'),
                    C('Quejas por cobro incorrecto en el trimestre', f'{X_QUEJ}!Resumen!C26', 'num'),
                    C('Peso de esas quejas sobre el total', f'{X_QUEJ}!Resumen!D26', 'pct1'),
                    C('Quejas registradas en el trimestre', f'{X_QUEJ}!Resumen!D11', 'num'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'El orden de descarte de un descuadre que se repite',
                    'cabecera': ['Pasada', 'Qué se revisa', 'Qué lo delata', 'Si aparece aquí…'],
                    'filas': [
                        ['1. Sistema', 'Anulaciones, invitaciones, cambios de forma de pago y propinas cobradas por tarjeta', 'La diferencia coincide con una operación concreta del informe del TPV', 'Se corrige el procedimiento de anulación y se acabó'],
                        ['2. Proceso', 'Fondo de caja, cortes de turno sin contar, cobros con la caja abierta, vueltas a ojo', 'La diferencia aparece siempre en el mismo momento del servicio', 'Se cambia el momento del corte y se vuelve a medir una semana'],
                        ['3. Personas', 'Coincidencia sostenida con un turno y una persona, con los dos pasos anteriores descartados', 'La diferencia sólo ocurre en los cierres de esa persona', 'Conversación en privado, con el dato delante y sin acusación'],
                    ],
                    'nota': 'Las dos primeras pasadas resuelven la mayoría de los descuadres '
                            'repetidos, y no cuestan una conversación incómoda. Saltárselas es lo '
                            'que rompe equipos por cuarenta euros.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 3,
                'titulo': 'Un Cliente Pide la Hoja de Reclamaciones',
                'resumen_indice': 'qué hay que entregar, en qué plazo hay que contestar y por qué eso depende de tu comunidad.',
                'palabras': 640, 'bloques': 1,
                'objetivo': 'Que el manager entregue la hoja sin discutir, sepa '
                            'qué pasa después y tenga el plazo de respuesta de '
                            'su comunidad anotado antes de que se lo pidan.',
                'epigrafes': EPI_SIT,
                'puntos': [
                    'La situación: un cliente pide la hoja en mitad del '
                    'servicio, delante de otras mesas. Lo que está en juego no '
                    'es la reclamación, es el minuto siguiente.',
                    'Qué NO hacer: decir que no hay, decir que hay que pedirla '
                    'por internet, intentar convencer al cliente de que no la '
                    'rellene, o rellenar la parte del establecimiento con prisa '
                    'y sin datos.',
                    'Protocolo: entregarla en el momento y sin condiciones, '
                    'retirar la conversación de la sala, cumplimentar la parte '
                    'del establecimiento con hechos y no con adjetivos, '
                    'quedarse con la copia que corresponde y anotar el día de '
                    'entrega, porque el plazo se cuenta desde ahí.',
                    'La norma: la hoja oficial es competencia autonómica; hay '
                    'obligación de tenerla, de anunciarla con cartel y de '
                    'contestar por escrito en el plazo de la comunidad, que en '
                    'unas se cuenta en días naturales y en otras en días '
                    'hábiles. Negarse a entregarla es una infracción por sí '
                    'misma.',
                    'La herramienta y el guion: la hoja de reclamaciones '
                    'formales del libro de quejas, que calcula sola los días '
                    'transcurridos y avisa si te vas de plazo. Y la frase con '
                    'la que se entrega, que es una sola y no admite '
                    'improvisación.',
                ],
                'cifras': [
                    C('Plazo legal de respuesta en Cataluña, en días', f'{X_QUEJ}!Parámetros!C15', 'num'),
                    C('Plazo legal de respuesta en Andalucía, en días', f'{X_QUEJ}!Parámetros!C16', 'num'),
                    C('Reclamaciones formales registradas', f'{X_QUEJ}!Resumen!D40', 'num'),
                    C('Contestadas dentro de plazo', f'{X_QUEJ}!Resumen!D41', 'num'),
                    C('Contestadas fuera de plazo', f'{X_QUEJ}!Resumen!D42', 'num'),
                    C('Días transcurridos de la reclamación que se pasó de plazo', f'{X_QUEJ}!Reclamaciones Formales!F6', 'num'),
                    C('Plazo aplicable a esa reclamación, en días', f'{X_QUEJ}!Reclamaciones Formales!G6', 'num'),
                    C('¿Se contestó dentro de plazo?', f'{X_QUEJ}!Reclamaciones Formales!I6', 'txt'),
                ],
                'sector': ['MM-40'],
                'tablas': [{
                    'titulo': 'El plazo de respuesta depende de tu comunidad (quejas-reclamaciones-resenas.xlsx, hoja «Parámetros»)',
                    'src': (X_QUEJ, 'Parámetros'),
                    'cols': [('Comunidad', 'A', 'txt'), ('Plazo legal', 'B', 'txt'),
                             ('Días para el aviso', 'C', 'num'), ('Se cuentan', 'D', 'txt')],
                    'filas': (15, 17),
                    'saltar_vacias': False,
                    'nota': 'Verificado el 04-09-2026 · Cataluña: Decret 121/2013 y art. 126-9 de la '
                            'Llei 22/2010; Andalucía: Decreto 82/2022, arts. 4, 7 y 12 · '
                            'https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430 — la tercera fila '
                            'es una casilla editable para tu comunidad.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 4,
                'titulo': 'Una Reseña de Una Estrella Acusa al Local de una Intoxicación',
                'resumen_indice': 'la respuesta pública, la investigación interna y por qué las dos son cosas distintas.',
                'palabras': 620, 'bloques': 1,
                'objetivo': 'Separar dos reacciones que se mezclan siempre: lo '
                            'que se escribe en público y lo que se investiga '
                            'dentro. La primera se hace hoy y en cuatro líneas; '
                            'la segunda se hace en frío y con los registros '
                            'delante.',
                'epigrafes': EPI_SIT,
                'puntos': [
                    'La situación: una reseña pública de la puntuación más baja '
                    'que atribuye al local un problema de salud, sin fecha '
                    'clara y sin mesa identificada. Situarla sobre el volumen '
                    'de reseñas y la media del negocio.',
                    'Qué NO hacer: responder en caliente, negar el hecho, '
                    'insinuar que el cliente miente, pedir la retirada de la '
                    'reseña, o contestar con datos de la mesa que identifiquen '
                    'a la persona en público.',
                    'Protocolo: responder en un plazo corto con una respuesta '
                    'breve que reconozca la preocupación, ofrezca un canal '
                    'privado y no admita ni niegue el hecho; y en paralelo, '
                    'abrir la revisión interna con los registros de '
                    'temperatura, la trazabilidad de ese servicio y las '
                    'incidencias del día.',
                    'La norma: no hay obligación de responder una reseña, y hay '
                    'que decirlo; lo que sí existe es la obligación de tener el '
                    'sistema de autocontrol y la trazabilidad que permiten '
                    'saber qué pasó, y la de no publicar datos personales de un '
                    'cliente en la respuesta.',
                    'La herramienta y el guion: la hoja de reseñas del libro de '
                    'quejas y el objetivo de reseñas respondidas de la casa. Y '
                    'las cuatro líneas de la respuesta pública, escritas tal '
                    'cual para copiar y adaptar.',
                ],
                'cifras': [
                    C('Reseñas registradas', f'{X_QUEJ}!Resumen!D46', 'num'),
                    C('Media de estrellas', f'{X_QUEJ}!Resumen!D47', 'num2'),
                    C('Reseñas respondidas', f'{X_QUEJ}!Resumen!D48', 'num'),
                    C('Porcentaje de reseñas respondidas', f'{X_QUEJ}!Resumen!D49', 'pct1'),
                    C('Objetivo de reseñas respondidas de la casa', f'{X_QUEJ}!Resumen!D6', 'pct0'),
                    C('Objetivo de media de estrellas de la casa', f'{X_QUEJ}!Resumen!D7', 'num1'),
                    C('Quejas por producto en mal estado en el trimestre', f'{X_QUEJ}!Resumen!C31', 'num'),
                ],
                'sector': ['MM-45', 'MM-29'],
                # No se usa aquí la tabla de «reseñas por mes» del mismo libro
                # aunque cuadre temáticamente: su primera columna es una FECHA y
                # `formatear` no tiene formato de fecha, así que se imprimiría
                # «2026-03-01 00:00:00» en mitad del PDF. Se usa el cuadro de
                # gravedades, que además es el que decide el plazo de respuesta
                # de esta situación.
                'tablas': [{
                    'titulo': 'Las tres gravedades y el plazo de cierre que se ha puesto la casa (quejas-reclamaciones-resenas.xlsx, hoja «Resumen»)',
                    'src': (X_QUEJ, 'Resumen'),
                    'cols': [('Gravedad', 'A', 'num'), ('Qué significa', 'B', 'txt'),
                             ('Quejas', 'C', 'num'),
                             ('Plazo de cierre (horas)', 'D', 'num'),
                             ('Días medios hasta el cierre', 'E', 'num1'),
                             ('Cumplimiento (%)', 'G', 'pct0')],
                    'filas': (35, 37),
                    'nota': 'Una acusación pública de riesgo sanitario entra por la gravedad más '
                            'alta, que es la que menos horas de plazo tiene y la única en la que '
                            'el cumplimiento de la casa se queda corto.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 5,
                'titulo': 'Un Camarero Lleva 19 Meses Encadenando Contratos Temporales',
                'resumen_indice': 'qué ha pasado ya, qué se puede hacer todavía y cuánto cuesta no hacerlo.',
                'palabras': 630, 'bloques': 1,
                'objetivo': 'Que el lector entienda que en esta situación la '
                            'decisión ya está tomada por la ley y lo único que '
                            'queda por decidir es cuándo se reconoce. Y que vea '
                            'el coste de la alternativa.',
                'epigrafes': EPI_SIT,
                'puntos': [
                    'La situación: una persona del equipo suma diecinueve meses '
                    'de contratos temporales en el mismo puesto, no seguidos, '
                    'con la campaña de verano en medio. Situarla sobre el '
                    'tamaño del equipo y sobre lo que ya se está pagando en '
                    'salarios y cotización.',
                    'Qué NO hacer: hacer un contrato nuevo «de otra cosa» para '
                    'reiniciar el contador, dejar pasar unas semanas y volver a '
                    'llamar, o preguntar a la persona si le importa seguir '
                    'igual. Nada de eso interrumpe el cómputo y todo eso empeora '
                    'la posición de la empresa.',
                    'Protocolo: reconstruir el historial real de contratos y '
                    'días trabajados en ese puesto, comprobar el cómputo con la '
                    'asesoría, y decidir entre reconocer la condición de fija o '
                    'reconvertir a fijo-discontinuo si el trabajo es realmente '
                    'estacional. Y avisar de que el fijo-discontinuo calcula la '
                    'antigüedad por toda la relación.',
                    'La norma: el encadenamiento por encima del límite legal en '
                    'un periodo de referencia convierte a la persona en fija, y '
                    'el fraude en la contratación temporal se sanciona por cada '
                    'trabajador afectado, lo que multiplica el importe cuando el '
                    'error se ha repetido con varias personas.',
                    'La herramienta y el guion: la hoja de permisos y cómputo y '
                    'el calendario legal para poner la fecha de revisión, y la '
                    'conversación con la persona, que se tiene ANTES de que la '
                    'tenga con un abogado.',
                ],
                'cifras': [
                    C('Personas del equipo', f'{X_POLI}!Cobertura por Estación!C27', 'num'),
                    C('Salarios brutos del año', f'{X_SEM}!Semana!K57', 'eur'),
                    C('Coste de personal con Seguridad Social del año', f'{X_SEM}!Semana!M57', 'eur'),
                    C('Labor cost del año', f'{X_SEM}!Semana!N57', 'pct1'),
                    C('Puesto del ejemplo de selección del pack', f'{X_SEL}!Scorecard!D4', 'txt'),
                    C('Encuadre de ese puesto en el ALEH VI', f'{X_SEL}!Scorecard!D5', 'txt'),
                ],
                'sector': ['MM-09', 'MM-10', 'MM-11', 'MM-23'],
                'tablas': [{
                    'titulo': 'Lo que interrumpe el cómputo y lo que no',
                    'cabecera': ['Maniobra habitual', '¿Interrumpe el cómputo?', 'Qué pasa de verdad'],
                    'filas': [
                        ['Dejar pasar unas semanas y volver a llamar', 'No', 'El cómputo mira el periodo de referencia completo, no exige continuidad'],
                        ['Firmar un contrato con otra denominación en el mismo puesto', 'No', 'Lo que cuenta es el puesto de trabajo desempeñado, no el nombre del contrato'],
                        ['Cambiar la causa del contrato sin que cambie el trabajo', 'No', 'La causa tiene que existir de verdad y constar por escrito'],
                        ['Que la persona acepte por escrito seguir como temporal', 'No', 'Los derechos reconocidos por norma imperativa no son renunciables'],
                        ['Convertir el puesto en fijo-discontinuo porque el trabajo es estacional', 'No aplica: ya es indefinido', 'Es la salida ordenada, con la antigüedad calculada por toda la relación'],
                    ],
                    'nota': V_ET,
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 6,
                'titulo': 'La Semana Cierra con un Prime Cost del 71 Por Ciento',
                'resumen_indice': 'las tres preguntas del lunes por la mañana cuando el semáforo se pone en rojo.',
                'palabras': 610, 'bloques': 1,
                'objetivo': 'Enseñar a leer una semana mala sin tocar la carta '
                            'el mismo lunes: primero se separa qué mitad del '
                            'prime cost se ha movido, luego se busca la causa y '
                            'sólo después se decide.',
                'epigrafes': EPI_SIT,
                'puntos': [
                    'La situación: el cuadro de mando devuelve un prime cost muy '
                    'por encima del objetivo en una semana concreta, con el food '
                    'cost y el labor cost movidos los dos. Dar la semana, los '
                    'tres porcentajes, las ventas y el margen que quedó.',
                    'Qué NO hacer: subir precios el lunes, recortar horas del '
                    'fin de semana siguiente a ciegas, o dar por bueno el dato '
                    'sin comprobar el inventario. Las tres reacciones son '
                    'frecuentes y las tres se toman antes de saber qué pasó.',
                    'Protocolo en tres preguntas: ¿el consumo es real o es que '
                    'el inventario está mal contado?; ¿las ventas cayeron o el '
                    'coste subió?; ¿las horas trabajadas se correspondieron con '
                    'los cubiertos que hubo? Contestarlas exige mirar cuatro '
                    'columnas de la propia hoja, y de ahí sale la decisión.',
                    'La norma: aquí no hay norma, y hay que decirlo. Lo que hay '
                    'es un objetivo que fijó la casa y una consecuencia '
                    'contable, no legal.',
                    'La herramienta y el guion: el cuadro de mando semanal y la '
                    'reunión del lunes. Y la forma de llevárselo al propietario '
                    'si la semana mala se repite: una propuesta, un dato y una '
                    'fecha de revisión.',
                ],
                'cifras': [
                    C('Semana ISO en la que se dispara el prime cost', f'{X_SEM}!Semana!A37', 'num'),
                    C('Prime cost de esa semana', f'{X_SEM}!Semana!O37', 'pct1'),
                    C('Food cost de esa semana', f'{X_SEM}!Semana!J37', 'pct1'),
                    C('Labor cost de esa semana', f'{X_SEM}!Semana!N37', 'pct1'),
                    C('Ventas netas de esa semana', f'{X_SEM}!Semana!E37', 'eur'),
                    C('Margen tras prime cost de esa semana', f'{X_SEM}!Semana!R37', 'eur'),
                    C('Objetivo de prime cost en vigor', f'{X_SEM}!Parámetros!B13', 'pct0'),
                    C('Objetivo de food cost en vigor', f'{X_SEM}!Parámetros!B11', 'pct0'),
                    C('Objetivo de labor cost en vigor', f'{X_SEM}!Parámetros!B12', 'pct0'),
                    C('Prime cost del año, ponderado', f'{X_SEM}!Semana!O57', 'pct1'),
                ],
                'sector': ['MM-41'],
                'tablas': [{
                    'titulo': 'La semana mala, con las cuatro anteriores y las cuatro siguientes (cuadro-de-mando-semanal-manager.xlsx, hoja «Semana»)',
                    'src': (X_SEM, 'Semana'),
                    'cols': [('Semana ISO', 'A', 'num'), ('Ventas netas (€)', 'E', 'eur'),
                             ('Consumo (€)', 'I', 'eur'), ('Food cost (%)', 'J', 'pct1'),
                             ('Labor cost (%)', 'N', 'pct1'), ('Prime cost (%)', 'O', 'pct1'),
                             ('Lectura', 'Q', 'txt'),
                             ('Margen tras prime cost (€)', 'R', 'eur')],
                    'filas': (33, 41),
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 7,
                'titulo': 'Una Reducción de Jornada por Guarda Legal Justo en el Viernes Noche',
                'resumen_indice': 'quién elige el horario, qué margen tiene la empresa y cómo se recompone el cuadrante.',
                'palabras': 640, 'bloques': 1,
                'objetivo': 'Que el manager sepa que en esta petición no está '
                            'decidiendo él, y que dedique su energía a lo único '
                            'que sí puede resolver: recomponer la cobertura de '
                            'la franja que se queda corta.',
                'epigrafes': EPI_SIT,
                'puntos': [
                    'La situación: una persona pide reducción de jornada por '
                    'guarda legal y la concreción que propone deja sin cubrir '
                    'la franja de más demanda de la semana. Situarla con las '
                    'horas de apertura y con la cobertura de esa estación.',
                    'Qué NO hacer: negarla, condicionarla a que la persona '
                    'acepte otro horario, pedirle que «lo hable con sus '
                    'compañeros», o contestar en el pase. Ninguna de las cuatro '
                    'cosas es una respuesta válida y todas empeoran la '
                    'posición de la empresa.',
                    'Protocolo: acusar recibo por escrito con fecha, comprobar '
                    'que la concreción está dentro de la jornada ordinaria de '
                    'la persona, y trabajar sobre el cuadrante en vez de sobre '
                    'la petición: quién más sostiene esa estación, quién puede '
                    'subir de nivel y en cuánto tiempo.',
                    'La norma: en la reducción por guarda legal la concreción '
                    'horaria la elige la persona trabajadora dentro de su '
                    'jornada ordinaria; y en la adaptación de jornada por '
                    'conciliación, que es otra figura, el silencio de la empresa '
                    'dentro del plazo la concede. Distinguir las dos es la '
                    'mitad del caso.',
                    'La herramienta y el guion: la hoja de permisos y cómputo '
                    'para no equivocarse de figura, la matriz de polivalencia '
                    'para recomponer la franja, y la frase con la que se '
                    'contesta a la persona el mismo día.',
                ],
                'cifras': [
                    C('Figuras recogidas en la hoja de permisos', f'{X_LEG}!Permisos y Cómputo!D18', 'num'),
                    C('De ellas, retribuidas', f'{X_LEG}!Permisos y Cómputo!D19', 'num'),
                    C('De ellas, no retribuidas', f'{X_LEG}!Permisos y Cómputo!D20', 'num'),
                    C('Horas de apertura al público de una semana completa', f'{X_SEM}!Parámetros!B37', 'num'),
                    C('Personas que sostienen «Sala y servicio»', f'{X_POLI}!Cobertura por Estación!B16', 'num'),
                    C('Cobertura de «Sala y servicio»', f'{X_POLI}!Cobertura por Estación!E16', 'pct1'),
                    C('Personas del equipo', f'{X_POLI}!Cobertura por Estación!C27', 'num'),
                ],
                'sector': ['MM-26', 'MM-27', 'MM-08'],
                'tablas': [{
                    'titulo': 'Permisos y cómputo: la figura que aplica y la que no (calendario-cumplimiento-legal.xlsx, hoja «Permisos y Cómputo»)',
                    'src': (X_LEG, 'Permisos y Cómputo'),
                    'cols': [('Permiso o figura', 'B', 'txt'),
                             ('Duración o cómputo', 'C', 'txt'),
                             ('¿Retribuido?', 'D', 'txt'),
                             ('Quién lo pide y cómo', 'E', 'txt'),
                             ('Artículo', 'F', 'txt')],
                    'filas': (14, 15),
                    'nota': V_ET,
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 8,
                'titulo': 'Se Presenta una Inspección de Sanidad sin Avisar',
                'resumen_indice': 'qué se enseña, quién acompaña, qué se firma y qué se hace con el acta.',
                'palabras': 620, 'bloques': 1,
                'objetivo': 'Convertir la visita en un trámite: si la '
                            'documentación está donde tiene que estar y una '
                            'persona sabe acompañar, una inspección dura menos '
                            'de una hora y no cambia nada del servicio.',
                'epigrafes': EPI_SIT,
                'puntos': [
                    'La situación: llega la inspección en pleno servicio. Lo que '
                    'decide el resultado ya está decidido: o la documentación '
                    'está o no está. Situarla con los documentos obligatorios '
                    'registrados y con el estado del calendario de '
                    'vencimientos.',
                    'Qué NO hacer: mandar a alguien a buscar papeles mientras la '
                    'persona inspectora espera, discutir en la cocina, firmar el '
                    'acta sin leerla, o negarse a firmarla creyendo que así no '
                    'vale.',
                    'Protocolo: una persona designada acompaña de principio a '
                    'fin, el servicio sigue, se entrega lo que se pide sin '
                    'añadir nada, se lee el acta entera, se firma haciendo '
                    'constar las observaciones que procedan —firmar no es '
                    'aceptar— y se pide copia. Y ese mismo día se abre una '
                    'decisión por cada punto anotado.',
                    'La norma: el sistema de autocontrol basado en los '
                    'principios del método, la información de alérgenos con '
                    'soporte accesible, las temperaturas vigentes y la '
                    'trazabilidad de un paso atrás. Con su norma y con la '
                    'advertencia de que la que casi todo el mundo cita está '
                    'derogada.',
                    'La herramienta y el guion: la hoja de documentación '
                    'obligatoria, que dice dónde tiene que estar cada papel y '
                    'quién lo pide, y la auditoría interna, que es el ensayo. Y '
                    'las dos frases con las que se recibe a la persona '
                    'inspectora.',
                ],
                'cifras': [
                    C('Documentos obligatorios registrados', f'{X_LEG}!Documentación Obligatoria!D25', 'num'),
                    C('Puntos de control registrados en el calendario', f'{X_LEG}!Calendario y Vencimientos!D38', 'num'),
                    C('Puntos vencidos en la fecha de corte', f'{X_LEG}!Calendario y Vencimientos!D43', 'num'),
                    C('Puntos en verde', f'{X_LEG}!Calendario y Vencimientos!D47', 'pct0'),
                    C('Puntuación ponderada de la última auditoría interna', f'{X_AUD}!Auditoría!I71', 'num2'),
                    C('Cumplimiento de la última auditoría interna', f'{X_AUD}!Auditoría!I72', 'pct1'),
                ],
                'sector': ['MM-29', 'MM-31', 'MM-32', 'MM-33', 'MM-34', 'MM-35'],
                'tablas': [{
                    'titulo': 'Qué te van a pedir, dónde tiene que estar y quién lo pide (calendario-cumplimiento-legal.xlsx, hoja «Documentación Obligatoria»)',
                    'src': (X_LEG, 'Documentación Obligatoria'),
                    'cols': [('#', 'A', 'num'), ('Documento', 'B', 'txt'),
                             ('Dónde debe estar', 'C', 'txt'), ('Quién lo pide', 'D', 'txt')],
                    'filas': (7, 22),
                    'nota': 'Verificado el 04-09-2026 · Reglamento (CE) 852/2004, RD 1021/2022 y '
                            'RD 1086/2020 · https://www.boe.es/buscar/act.php?id=BOE-A-2020-15872',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 9,
                'titulo': 'Una Empleada Comunica una Situación de Acoso',
                'resumen_indice': 'qué se activa en el momento, qué NO se hace nunca y por qué el protocolo tiene que existir antes.',
                'palabras': 630, 'bloques': 1,
                'objetivo': 'Dar la única respuesta correcta en los primeros '
                            'cinco minutos, y dejar claro que el trabajo de '
                            'verdad —tener el protocolo escrito y conocido— se '
                            'hace antes de que ocurra.',
                'epigrafes': EPI_SIT,
                'puntos': [
                    'La situación: una persona del equipo comunica al manager '
                    'una situación de acoso. Puede ocurrir en cualquier local, '
                    'del tamaño que sea, y no depende de tener plantilla '
                    'grande.',
                    'Qué NO hacer, que aquí es lo más importante: no valorar los '
                    'hechos, no pedir pruebas, no confrontar a las partes en el '
                    'momento, no comentarlo con nadie del equipo, no minimizar '
                    'ni bromear, y no dejarlo sin registrar porque «se va a '
                    'arreglar solo».',
                    'Protocolo: escuchar sin interrumpir y sin opinar, informar '
                    'de que existe un procedimiento y activarlo el mismo día, '
                    'proteger a la persona de contactos con la parte denunciada '
                    'mientras dure, dejar constancia escrita de la comunicación '
                    'con la fecha, y garantizar la confidencialidad.',
                    'La norma: toda empresa, sin umbral de plantilla, tiene que '
                    'arbitrar procedimientos específicos de prevención y de '
                    'cauce de las denuncias por acoso. La sanción por no '
                    'tenerlos está en el tramo más alto, y el manual da su '
                    'rango con su fuente.',
                    'La herramienta y el guion: la hoja de documentación '
                    'obligatoria, que es donde se comprueba que el protocolo '
                    'existe y es accesible, y el registro de acuerdos para dejar '
                    'constancia de las decisiones. Y las tres frases con las que '
                    'se responde en el minuto uno.',
                ],
                'cifras': [
                    C('Documentos obligatorios registrados', f'{X_LEG}!Documentación Obligatoria!D25', 'num'),
                    C('Puntos con periodicidad fijada por una norma estatal', f'{X_LEG}!Calendario y Vencimientos!D39', 'num'),
                    C('Personas del equipo', f'{X_POLI}!Cobertura por Estación!C27', 'num'),
                    C('Personas del equipo con seguimiento individual', f'{X_REU}!Uno-a-uno!D30', 'num'),
                    C('Acuerdos registrados en el trimestre', f'{X_REU}!Actas y Acuerdos!D46', 'num'),
                ],
                'sector': ['MM-19', 'MM-20', 'MM-22'],
                'tablas': [{
                    'titulo': 'Lo que tiene que existir ANTES de que ocurra',
                    'cabecera': ['Documento o medida', 'Desde cuántas personas', 'Dónde tiene que estar'],
                    'filas': [
                        ['Protocolo frente al acoso sexual y por razón de sexo', 'Sin umbral: desde la primera persona contratada', 'Publicado y accesible a toda la plantilla, no en un cajón'],
                        ['Canal de comunicación designado', 'Sin umbral', 'Con una persona responsable nombrada y conocida por el equipo'],
                        ['Registro escrito de la comunicación recibida', 'Sin umbral', 'Con fecha, confidencial y separado de cualquier expediente laboral'],
                        ['Formación e información al equipo sobre el protocolo', 'Sin umbral', 'Con constancia de que se comunicó y cuándo'],
                        ['Conjunto planificado de medidas LGTBI', 'A partir de más de 50 personas', 'Acordado mediante negociación colectiva'],
                    ],
                    'nota': 'Verificado el 04-09-2026 · Art. 48 de la Ley Orgánica 3/2007 y art. 15.1 de la '
                            'Ley 4/2023 · https://www.boe.es/buscar/act.php?id=BOE-A-2007-6115',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 10,
                'titulo': 'El Cocinero Clave se Va y Sólo Él Sabe Hacer la Partida Fría',
                'resumen_indice': 'las dos semanas de preaviso, lo que se puede transferir en ese tiempo y lo que ya no.',
                'palabras': 610, 'bloques': 1,
                'objetivo': 'Aprovechar la única ventana que queda —el preaviso— '
                            'para transferir lo transferible, y usar el coste '
                            'medido de esta baja para que no vuelva a haber una '
                            'estación con una sola persona.',
                'epigrafes': EPI_SIT,
                'puntos': [
                    'La situación: la persona que sostiene sola una estación '
                    'comunica que se va. Dar la cobertura real de esa estación, '
                    'cuántas personas pueden enseñarla y el impacto estimado de '
                    'la baja.',
                    'Qué NO hacer: intentar retenerla con una mejora improvisada '
                    'el mismo día, ocultárselo al resto del equipo, o dejar el '
                    'traspaso para la última semana. Y no convertir el preaviso '
                    'en un castigo: es el activo más valioso que queda.',
                    'Protocolo: aceptar la baja y pactar el plan de traspaso '
                    'por escrito el primer día; elegir a quién se le enseña '
                    'según la matriz y no según la disponibilidad; escribir lo '
                    'que sólo está en su cabeza —fichas, proveedores, tiempos, '
                    'trucos de la estación—; y programar las sesiones en el '
                    'cuadrante, no «cuando se pueda».',
                    'La norma: aquí lo que hay es el preaviso que fije el '
                    'convenio o el contrato y la liquidación correspondiente. '
                    'No hay obligación de traspaso de conocimiento: es criterio '
                    'de gestión, y hay que decirlo.',
                    'La herramienta y el guion: la matriz de polivalencia y el '
                    'plan de cross-training, que ya tenían identificada esa '
                    'estación como punto único de fallo, y la hoja de coste de '
                    'una baja, que es el argumento con el que se pide '
                    'presupuesto para que no se repita.',
                ],
                'cifras': [
                    C('Personas que sostienen «Fríos y entrantes»', f'{X_POLI}!Cobertura por Estación!B13', 'num'),
                    C('Personas que pueden enseñar «Fríos y entrantes»', f'{X_POLI}!Cobertura por Estación!C13', 'num'),
                    C('Cobertura de «Fríos y entrantes»', f'{X_POLI}!Cobertura por Estación!E13', 'pct1'),
                    C('Alerta que devuelve la hoja para esa estación', f'{X_POLI}!Cobertura por Estación!F13', 'txt'),
                    C('Coste directo de cubrir la baja', f'{X_POLI}!Coste de una Baja!B15', 'eur2'),
                    C('Margen que no se gana mientras el equipo recupera el ritmo', f'{X_POLI}!Coste de una Baja!B22', 'eur2'),
                    C('Impacto estimado total de la baja', f'{X_POLI}!Coste de una Baja!B28', 'eur2'),
                    C('Acciones registradas en el plan de cross-training', f'{X_POLI}!Plan de Cross-Training!C32', 'num'),
                ],
                'sector': ['MM-43'],
                'tablas': [{
                    'titulo': 'El plan de cross-training que ya existía: quién enseña a quién y para cuándo (matriz-formacion-polivalencia.xlsx, hoja «Plan de Cross-Training»)',
                    'src': (X_POLI, 'Plan de Cross-Training'),
                    'cols': [('#', 'A', 'num'), ('Nombre', 'C', 'txt'),
                             ('Estación objetivo', 'D', 'txt'),
                             ('Nivel actual', 'E', 'num'), ('Nivel objetivo', 'F', 'num'),
                             ('Quién le enseña', 'G', 'txt'),
                             ('Estado', 'I', 'txt'),
                             ('Situación del plazo', 'L', 'txt')],
                    'filas': (10, 17),
                    'nota': 'La estación que se queda descubierta ya estaba señalada en la hoja de '
                            'cobertura como punto único de fallo. El plan no evita la baja: evita '
                            'que la baja te deje sin servicio.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 11,
                'titulo': 'El Propietario Quiere Subir la Carta un 10 Por Ciento y Tú Tienes los Números',
                'resumen_indice': 'qué dicen tus cifras antes de tocar un precio, y cómo se lleva esa conversación con datos.',
                'palabras': 660, 'bloques': 1,
                'objetivo': 'Enseñar a convertir una orden en una conversación '
                            'técnica: no se discute la subida, se enseña qué '
                            'mitad del prime cost se ha movido y qué palancas '
                            'hay antes y después del precio.',
                'epigrafes': EPI_SIT,
                'puntos': [
                    'La situación: el propietario propone una subida lineal de '
                    'la carta. El manager tiene el cuadro de mando del año '
                    'delante. Dar el prime cost del año, el food cost, el labor '
                    'cost, el objetivo y el margen.',
                    'Qué NO hacer: decir que no sin datos, aplicar la subida '
                    'lineal a todos los platos sin mirar cuáles la aguantan, o '
                    'aceptar y no medir después. Una subida lineal trata igual '
                    'al plato que deja mucho y al que deja poco.',
                    'Protocolo: separar primero qué mitad del prime cost se ha '
                    'movido, porque si lo que ha subido es el coste de personal '
                    'una subida de carta no lo arregla; después mirar el ticket '
                    'medio y el gasto por cubierto para ver si el problema es de '
                    'precio o de mix; y sólo entonces plantear la subida donde '
                    'toca, con fecha de revisión a cuatro semanas.',
                    'La norma: no hay norma sobre el precio, y hay que decirlo; '
                    'lo que sí hay que respetar es la información de precios al '
                    'cliente y el cambio en las cartas visibles.',
                    'La herramienta y el guion: el cuadro de mando semanal para '
                    'el diagnóstico, y para decidir plato a plato, el escandallo '
                    'y la matriz de carta de la Guía Food Cost, que es donde vive '
                    'esa decisión. Y el guion de la conversación con el '
                    'propietario, en cuatro movimientos.',
                ],
                'cifras': [
                    C('Prime cost del año, ponderado', f'{X_SEM}!Semana!O57', 'pct1'),
                    C('Food cost del año, ponderado', f'{X_SEM}!Semana!J57', 'pct1'),
                    C('Labor cost del año, ponderado', f'{X_SEM}!Semana!N57', 'pct1'),
                    C('Objetivo de prime cost en vigor', f'{X_SEM}!Parámetros!B13', 'pct0'),
                    C('Ventas netas totales del año', f'{X_SEM}!Semana!E57', 'eur'),
                    C('Margen tras prime cost del año', f'{X_SEM}!Semana!R57', 'eur'),
                    C('Ticket medio del año', f'{X_SEM}!Semana!U57', 'eur2'),
                    C('Gasto medio por cubierto del año', f'{X_SEM}!Semana!V57', 'eur2'),
                    C('Cubiertos del año', f'{X_SEM}!Semana!S57', 'num'),
                ],
                'sector': ['MM-41', 'MM-44', 'MM-47'],
                'tablas': [{
                    'titulo': 'Qué palanca toca antes de subir el precio',
                    'cabecera': ['Si lo que se ha movido es…', 'La subida de carta…', 'Lo que sí lo corrige'],
                    'filas': [
                        ['El coste de materia prima', 'Ayuda, pero sólo si se aplica donde el margen es peor', 'Reescandallar los platos afectados y renegociar las referencias que más pesan'],
                        ['El coste de personal', 'No lo corrige', 'Revisar la dotación por franja y las ventas por hora trabajada'],
                        ['El mix de lo que se vende', 'No lo corrige', 'Cambiar el orden y la presencia de la carta, no el precio'],
                        ['Los cubiertos, que han bajado', 'Lo empeora', 'Trabajar la ocupación y la política de reservas antes de tocar nada'],
                        ['Nada: el margen está en objetivo', 'No hace falta', 'Dejar los precios y volver a mirarlo dentro de cuatro semanas'],
                    ],
                    'nota': 'La decisión plato a plato no se toma con el cuadro semanal: se toma con '
                            'el escandallo y la matriz de carta, que están en la Guía Food Cost + '
                            'Ingeniería de Menú. Aquí se decide SI hay que tocar el precio y por qué.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 12,
                'titulo': 'Hay que Despedir por Causas Disciplinarias',
                'resumen_indice': 'la audiencia previa de dos días, qué se escribe en la carta y qué pasa si te saltas el procedimiento.',
                'palabras': 620, 'bloques': 1,
                'objetivo': 'Que el lector no se salte el paso que casi nadie ha '
                            'incorporado todavía. Es la situación en la que un '
                            'error de procedimiento cuesta más que el propio '
                            'despido.',
                'epigrafes': EPI_SIT,
                'puntos': [
                    'La situación: hay hechos documentados que encajan en una '
                    'falta del régimen disciplinario y la empresa ha decidido '
                    'despedir. Situarla con el número de faltas tipificadas en '
                    'el cuadro y con la vigencia de la modificación del acuerdo '
                    'estatal.',
                    'Qué NO hacer: entregar la carta directamente, redactarla '
                    'con adjetivos en vez de con hechos y fechas, apartar a la '
                    'persona del servicio sin más, o hacerlo el mismo día en que '
                    'ocurrieron los hechos y en caliente.',
                    'Protocolo: comprobar que los hechos están documentados y '
                    'que encajan en una falta tipificada; informar por escrito a '
                    'la persona de los hechos imputados y de su posible '
                    'calificación jurídica; darle el plazo para contestar; leer '
                    'lo que conteste y dejar constancia; y sólo entonces decidir '
                    'y entregar la carta, con hechos, fechas y calificación.',
                    'La norma: la audiencia previa al despido disciplinario está '
                    'en vigor desde el 4 de septiembre de 2026 y hasta el final '
                    'de la vigencia pactada del acuerdo estatal; da un plazo '
                    'para contestar y convierte en permiso retribuido los días '
                    'en los que se aparta a la persona del servicio. Tiene una '
                    'excepción, y hay que citarla también. Y las indemnizaciones '
                    'del despido objetivo y del improcedente van con su '
                    'artículo.',
                    'La herramienta y el guion: la hoja de régimen disciplinario '
                    'del calendario legal, que trae la tipificación y la '
                    'vigencia, y la asesoría laboral, que redacta la carta. Y '
                    'las frases de la comunicación de la audiencia previa.',
                ],
                'cifras': [
                    C('Filas del cuadro del régimen disciplinario', f'{X_LEG}!Régimen Disciplinario ALEH!E18', 'num'),
                    C('Faltas leves tipificadas', f'{X_LEG}!Régimen Disciplinario ALEH!E19', 'num'),
                    C('Faltas graves tipificadas', f'{X_LEG}!Régimen Disciplinario ALEH!E20', 'num'),
                    C('Faltas muy graves tipificadas', f'{X_LEG}!Régimen Disciplinario ALEH!E21', 'num'),
                    C('Días de vigencia que le quedan a la modificación del ALEH VI', f'{X_LEG}!Régimen Disciplinario ALEH!E25', 'num'),
                    C('Personas del equipo', f'{X_POLI}!Cobertura por Estación!C27', 'num'),
                ],
                'sector': ['MM-12', 'MM-13'],
                'tablas': [{
                    'titulo': 'El cuadro disciplinario y el procedimiento, tras la modificación del 4 de septiembre de 2026 (calendario-cumplimiento-legal.xlsx, hoja «Régimen Disciplinario ALEH»)',
                    'src': (X_LEG, 'Régimen Disciplinario ALEH'),
                    'cols': [('Falta o figura', 'B', 'txt'), ('Tipo', 'C', 'txt'),
                             ('Gravedad', 'D', 'txt'), ('Umbral o detalle', 'E', 'txt'),
                             ('Artículo', 'G', 'txt')],
                    'filas': (6, 15),
                    'nota': V_ALEH,
                }],
                'prohibido': NO_COMUN_BONUS,
            },
        ],
    },
]


# --------------------------------------------------------------------------
# Erratas que el gate ortográfico marca y NO lo son: nombres propios, términos
# del oficio, vocabulario jurídico y extranjerismos que no están en el léxico
# del blog. El gate normaliza los acentos antes de buscar, así que también
# propone «reparar» palabras bien escritas con tilde que el corpus nunca usó.
# Se arranca con la lista que quedó cerrada ayer en la Guía Food Cost y se le
# añade el vocabulario propio de este manual (laboral, sanitario y de sala).
# --------------------------------------------------------------------------
_ERRATAS_OK = (
    # 2026-09-05: falsos positivos del léxico sobre el texto real del manual (todas correctas en
    # contexto; el reparador convertía «cantó» en «cuánto» y «ocurrió» en «ocurrido»).
    'actas', 'canta', 'cantó', 'canto', 'atendió', 'atendio', 'desapareció', 'desaparecio', 'rendía', 'rendia',
    'alegar', 'anular', 'auditado', 'califica', 'cometido', 'contó', 'conto', 'digan', 'emitió', 'emitio',
    'escribirá', 'escribira', 'fisco', 'libren', 'manía', 'mania', 'ofreció', 'ofrecio', 'proporcionales',
    'vicio', 'ocurrió', 'ocurrio', 'acusa', 'acusando', 'señalado', 'senalado',
    # Heredadas de la Guía Food Cost (2026-09-04)
    'esima', 'podar', 'tiraje', 'trasladado', 'anado', 'añado', 'arrancado',
    'coincidan', 'cumplio', 'cumplió', 'dependio', 'dependió', 'ensanchado',
    'levado', 'parta', 'costeado', 'manejado', 'puzles', 'pasterizada',
    'perdio', 'perdió',
    'escandallo', 'escandallos', 'escandallar', 'escandallado', 'costeo',
    'beverage', 'delivery', 'packaging', 'away', 'takeaway', 'catering',
    'buffet', 'Horeca', 'Hostelería', 'ponderado', 'ponderada',
    'superreducido', 'repercutido', 'soportado', 'deducible', 'vinculante',
    'edulcorantes', 'auditable', 'trazabilidad', 'reformular', 'retirar',
    'Repsol', 'Michelin',
    # Vocabulario del oficio y de sala propio de este manual
    'briefing', 'handover', 'scorecard', 'cuadrante', 'cuadrantes',
    'polivalencia', 'comanda', 'comandas', 'arqueo', 'arqueos', 'cubierto',
    'cubiertos', 'emplatado', 'partida', 'partidas', 'pase', 'mesero',
    'meseros', 'garzón', 'salón', 'planilla', 'gerente', 'encargado',
    'encargada', 'onboarding', 'anfitrión', 'sumiller',
    # Vocabulario jurídico y laboral
    'ultraactividad', 'fijo-discontinuo', 'discontinuo', 'discontinuos',
    'complementarias', 'extraordinarias', 'tipificada', 'tipificadas',
    'tipificar', 'imputados', 'improcedente', 'improcedencia', 'finiquito',
    'preaviso', 'cotización', 'cotizan', 'devengado', 'imperativa',
    'retribuido', 'retribuidas', 'reglamentariamente', 'sancionable',
    'sancionador', 'infracción', 'infracciones', 'inspectora', 'convencional',
    'monoparentalidad', 'conciliación', 'concreción', 'renunciables',
    'intransferible', 'suspensión', 'prestación', 'audiencia', 'disciplinario',
    'disciplinaria', 'amonestación', 'encadenamiento', 'encadenar',
    'formativos', 'estacional', 'llamamiento', 'antigüedad', 'jornada',
    'jornadas', 'absentismo', 'temporalidad', 'plantilla', 'asalariados',
    'representación', 'desconexión', 'acoso', 'igualdad', 'retributivo',
    'preventiva', 'aptitud', 'consentimiento', 'derogado', 'derogados',
    'derogada', 'vigencia', 'vigentes',
    # Vocabulario sanitario y del local
    'autocontrol', 'alérgenos', 'anisakis', 'cefalópodos', 'escabechados',
    'salazón', 'refrigerados', 'congelados', 'recalentar', 'recalentado',
    'enfriamiento', 'limitador', 'precintado', 'reclasifica', 'ambiental',
    'terraza', 'terrazas', 'envases', 'reutilizables', 'asistencia',
    'autonómico', 'autonómica', 'autonómicas', 'declaración', 'responsable',
    # Siglas, registros y nombres propios que el léxico no conoce
    'REGCON', 'ALEH', 'LISOS', 'TRLGSS', 'TRLGDCU', 'FOGASA', 'RGPD',
    'AGEDI', 'SGAE', 'AEMET', 'DIRCE', 'EACL', 'CNAE', 'MEI', 'RDLeg',
    'Girona', 'Cataluña', 'Andalucía', 'Encina',
    # Palabras correctas que el corpus del blog no contiene
    'reproducible', 'reconstruir', 'recomponer', 'recomposición',
    'contrastarlo', 'reformulado', 'aterrizarlo', 'transferible',
    'reescandallar', 'repricing',
)
GUIA['gates']['erratas_permitidas'] = _ERRATAS_OK
for _b in BONUS:
    _b['gates']['erratas_permitidas'] = _ERRATAS_OK
