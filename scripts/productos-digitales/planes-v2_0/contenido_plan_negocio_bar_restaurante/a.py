#!/usr/bin/env python3
"""
Contenido de `plan-negocio-bar-restaurante` para el grupo A (§2 de la SPEC).

Aquí NO hay lógica: sólo los datos propios de este plan —supuestos, plantilla,
partidas, umbrales y textos legales del checklist— con **la fuente de cada
cifra**. La mecánica (dónde va cada celda, qué fórmula la enlaza y cómo se
reconstruye la hoja) es de `grupo_a.py`, que sirve a los cinco productos de
línea A.

DE DÓNDE SALE CADA NÚMERO — tres orígenes, siempre declarados:

  * «fichero v1.1» — estaba ya en `plan-financiero-bar-restaurante.xlsx` o en
    `checklist-apertura-bar-restaurante.xlsx` y se conserva.
  * «SPEC/R1» — lo fija `planes-v2-SPEC.md` o el hallazgo del R1 que se cita.
  * «parametrizado» — no está en la SPEC ni en el fichero, así que va en celda
    VERDE editable con su nota. Ninguna cifra del sector se teclea sin marcarla
    como parámetro: es la regla dura 6 del encargo.

RECALIBRACIÓN DEL CASO BASE (§7-bis.17, DOM-13, TEC-01)
------------------------------------------------------
El defecto que hunde los cinco planes de línea A es que el P&L imputa 115.200 €
de personal mientras su propia hoja `Personal` suma **209.171,20 €**. Con la
cifra correcta el coste laboral es el **66,3 %** de las ventas, casi el doble
del 35 % que fija `Instrucciones!A13`, y el plan es inviable con sus propios
datos. La SPEC obliga a recalibrar hasta que el caso base pase su propio
semáforo, «por los dos lados y dentro de rangos con fuente», y prohíbe
cuadrarlo tocando un porcentaje escondido.

Lo que se ha hecho, y por qué se puede defender ante un banco:

1. **La plantilla estaba sobredimensionada para el aforo.** El pack describe
   12 mesas × 4 sillas + 8 taburetes = **56 plazas** (`'1. Inversion
   Inicial'!A26:A27` del fichero v1.1) y el propio docx trabaja con **1,8
   rotaciones**, es decir un techo de ~100 cubiertos/día. Siete personas a
   jornada completa (209.171 €) sólo se pagan con ~600.000 € de ventas, que ese
   aforo no da. Se redimensiona por horas de servicio a **6 puestos, dos de
   ellos a tiempo parcial**, con los brutos del propio fichero como referencia
   y el SMI 2026 como suelo.
2. **El ticket pasa a declararse SIN IVA** (TEC-11, DOM-30). Los 18,50 € del
   fichero v1.1 son PVP —así se habla en hostelería—; sin IVA, con el mix
   65/35 de comida y bebida, equivalen a 16,25 €. Se fija **17,20 € sin IVA**,
   que son 19,58 € de PVP: dentro del rango «15-22 EUR» que declara
   `Instrucciones!A19` del propio fichero.
3. **Los cubiertos suben de 55 a 80** (1,43 rotaciones sobre 56 plazas), por
   debajo del techo de 1,8 que usa el propio documento y del que se deduce de
   `'3. Punto Equilibrio'`.
4. **El alquiler baja de 3.000 a 2.900 €/mes**, dentro del rango
   «2.000-4.500 EUR/mes» de `Instrucciones!A20` y respetando el techo de
   8-10 % sobre ventas de `Instrucciones!A14`, que con 3.000 € se incumplía.
5. **Aparecen los costes fijos que el plan no tenía y que el checklist sí
   obliga a contratar** (TEC-18): residuos y aceite usado, DDD, derechos de
   autor por la música, PRL, lavandería y reposición de menaje. Todos en celda
   verde con nota de «pide presupuesto en tu zona».

Resultado del caso base: coste de personal **34,5 %** (techo 35 %), alquiler
**8,2 %** (techo 10 %), coste de mercancía **27,2 %** (techo 32 %) y resultado
neto **9,6 %**, dentro del «5-10 %» que el propio libro declara como margen
medio del sector. **El plan ya no se suspende a sí mismo.** Las tres
demostraciones que lo comprueban son las 3, 5 y 6 de §2.11 y las corre
`grupo_a.demos()`.
"""

CONCEPTO = 'Bar-Restaurante / Restaurante Casual'

# ==========================================================================
# §2.1 — `0. Supuestos`
# {clave: (coord, etiqueta, valor, formato, nota, fuente)}
# `None` en coord/etiqueta/formato/nota = se queda el que trae `grupo_a`.
# ==========================================================================
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 80, None,
        'Sobre 56 plazas (12 mesas × 4 sillas + 8 taburetes de barra, hoja de '
        'Inversión) son 1,43 rotaciones al día, por debajo del techo de 1,8 '
        'que usa el propio plan',
        'recalibrado §7-bis.17 (v1.1: 55)'),
    'ticket_medio': (
        None, None, 17.20, None,
        'SIN IVA. Con el mix 65/35 equivale a 19,58 € de PVP, dentro del '
        'rango 15-22 € que declara este mismo libro para el restaurante '
        'casual',
        'recalibrado por TEC-11/DOM-30 (v1.1: 18,50 € sin declarar si '
        'llevaba IVA)'),
    'dias_apertura': (
        None, None, 310, None,
        'Cierre semanal de un día y vacaciones. El MISMO dato lo usan el P&L, '
        'el punto de equilibrio y los escenarios',
        'fichero v1.1'),
    'crec_a2': (None, None, 0.10, None,
                'Segundo año con la clientela ya asentada',
                'parametrizado (v1.1 implicaba 55 → 65 cubiertos = +18 %)'),
    'crec_a3': (None, None, 0.06, None,
                'Tercer año, cerca del techo de rotación del local',
                'parametrizado (v1.1 implicaba 65 → 75 = +15 %)'),
    'coste_comida': (
        None, None, 0.30, None,
        'Food cost objetivo del bar-restaurante casual: 28-32 % según las '
        'referencias de este mismo libro. Se aplica SOLO a la comida',
        'fichero v1.1 (Instrucciones: «Food cost objetivo 28-32 %»)'),
    'coste_bebida': (
        None, None, 0.22, None,
        'Coste de la bebida sobre las ventas de bebida, no sobre el total',
        'fichero v1.1 (rótulo de la fila «Bebidas cost»)'),
    'pct_consumibles': (
        None, None, 0.015, None,
        'Servilletas, papel, productos de limpieza y envases de llevar',
        'parametrizado (v1.1: 4.800 € fijos = 1,5 % de sus ventas)'),
    'pct_delivery': (
        None, None, 0.0, None,
        'A CERO por defecto: si no repartes no arrastras un coste inventado. '
        'Súbelo al peso REAL del canal y la comisión se aplica sólo sobre esa '
        'parte',
        'TEC-23/DOM-34 (v1.1 cobraba el 5 % de TODA la facturación)'),
    'comision_delivery': (
        None, None, 0.28, None,
        'Comisión típica de las plataformas sobre el pedido servido por ese '
        'canal; confírmala en tu contrato antes de proyectar',
        'parametrizado'),
    'comision_tpv': (
        None, None, 0.008, None,
        'Tarjeta y bizum sobre el total facturado; pide oferta a dos '
        'proveedores de TPV',
        'parametrizado (el plan v1.1 no lo contemplaba)'),
    'alquiler_mes': (
        None, None, 2900, None,
        'Dentro del rango 2.000-4.500 €/mes que declara este libro para un '
        'local de 80-120 m² en zona urbana, y respetando el techo del 10 % '
        'sobre ventas',
        'recalibrado (v1.1: 3.000 €/mes = 11,4 % de sus ventas, por encima '
        'de su propio techo)'),
    'fianza_meses': (None, None, 3, None,
                     'Tres meses de renta, como en el contrato tipo de local '
                     'de negocio', 'fichero v1.1'),
    'suministros_mes': (
        None, None, 1800, None,
        'Luz, agua y gas de una cocina con horno, cámaras y campana: pide el '
        'histórico del local antes de firmar',
        'recalibrado (v1.1: 1.200 €/mes, 3,4 % de ventas, por debajo de lo '
        'que consume una cocina caliente)'),
    'seguros_ano': (None, None, 2000, None,
                    'Responsabilidad civil + multirriesgo del local + '
                    'convenio', 'fichero v1.1'),
    'pct_varios': (None, None, 0.02, None,
                   'Colchón de gasto corriente no presupuestado',
                   'fichero v1.1 (rótulo «Varios e imprevistos (2%)»)'),
    'recursos_propios': (
        None, None, 75000, None,
        'Aportación de los socios. Con menos, el banco no entra: pide un '
        '35-40 % de fondos propios sobre la inversión',
        'parametrizado'),
    'prestamo': (
        None, None, 110000, None,
        'Principal solicitado. La hoja de Financiación comprueba que origen y '
        'usos cuadran',
        'parametrizado'),
    'tipo_prestamo': (None, None, 0.06, None,
                      'Tipo nominal anual; pide oferta a dos entidades y a '
                      'una línea ICO antes de fijarlo', 'parametrizado'),
    'plazo_prestamo': (None, None, 7, None, 'Años totales, carencia incluida',
                       'parametrizado'),
    'carencia_prestamo': (None, None, 1, None,
                          'Primer año sólo intereses, que es cuando la caja '
                          'está más tensa', 'parametrizado'),
    'meses_fondo': (
        None, None, 3, None,
        'Mínimo que exige este mismo libro: «Fondo de maniobra: mínimo 3 '
        'meses de costes fijos antes de abrir»',
        'SPEC §2.2 / TEC-07 (v1.1 dotaba 30.000 €, que eran 1,8 meses)'),
    'vida_obra': (None, None, 10, None,
                  'Obra, instalaciones y decoración. Coeficientes de la tabla '
                  'del art. 12.1 LIS: confírmalo con tu asesor',
                  'fichero v1.1 (rótulo «Amortizacion equipos (10 anos)»)'),
    'vida_maquinaria': (
        None, None, 8, None,
        'Maquinaria de cocina, mobiliario y equipos. Coeficientes de la tabla '
        'del art. 12.1 LIS: confírmalo con tu asesor',
        'parametrizado'),
}

# ==========================================================================
# §2.3.2 — líneas de venta y su peso (resuelve el doble conteo de la bebida)
# (rótulo, peso sobre ventas, grupo, nota, fuente)
# ==========================================================================
LINEAS_INGRESO = (
    ('Ventas de comida (cocina y barra)', 0.65, 'comida',
     'Menú del mediodía, carta y raciones',
     'fichero v1.1: el rótulo de la fila de bebidas decía «ingresos bebida '
     '~35%», así que la comida es el 65 % restante'),
    ('Ventas de bebida (cañas, vinos, cafés y copas)', 0.35, 'bebida',
     'Se calcula como el resto: comida + bebida = 100 %',
     'fichero v1.1'),
)

# ==========================================================================
# §2.6 — plantilla redimensionada (puesto, personas, bruto mes TOTAL, nota)
# ==========================================================================
PLANTILLA = (
    ('Gerente / Propietario', 1, 1900,
     'Trabaja en sala: compras, cierre de caja, proveedores y RRSS',
     'recalibrado (v1.1: 2.200 €)'),
    ('Jefe de cocina', 1, 1800,
     'Escandallos, pedidos y línea caliente',
     'recalibrado (v1.1: 2.000 €)'),
    ('Ayudante de cocina', 1, 1250,
     'Mise en place, fríos y limpieza de cocina. Por encima del SMI de '
     'jornada completa', 'recalibrado (v1.1: 1.300 €)'),
    ('Camarero/a de barra y sala', 1, 1300,
     'Jornada completa, con el servicio de mediodía y el de noche',
     'fichero v1.1'),
    ('Camarero/a a tiempo parcial (30 h)', 1, 1000,
     'Refuerzo de los dos servicios fuertes. El SMI proporcional de 30 h son '
     '915 €/mes', 'recalibrado (v1.1: dos camareros a jornada completa)'),
    ('Extra de fin de semana (20 h)', 1, 650,
     'Viernes, sábado y domingo. El SMI proporcional de 20 h son 610 €/mes',
     'parametrizado'),
)

# ==========================================================================
# §2.3 — costes fijos que el plan v1.1 no tenía y el checklist sí obliga
# (rótulo, importe, nota, fuente)
# ==========================================================================
FIJOS_EXTRA = (
    ('Limpieza, lavandería y lencería', 3600,
     'Mantelería, paños y uniformes. Pide presupuesto en tu zona: es un '
     'importe orientativo y editable', 'parametrizado (TEC-18)'),
    ('Gestión de residuos y de aceite vegetal usado', 1200,
     'Gestor autorizado. Lo pide la inspección y el aceite no puede ir al '
     'desagüe', 'parametrizado (TEC-18)'),
    ('Desinsectación, desratización y desinfección (DDD)', 900,
     'Empresa inscrita en el ROESB; forma parte del plan APPCC',
     'parametrizado (TEC-18)'),
    ('Derechos de autor por música ambiental', 900,
     'SGAE y AGEDI-AIE son dos licencias distintas; el importe depende de los '
     'metros y del aforo', 'parametrizado (TEC-18)'),
    ('Prevención de riesgos laborales y vigilancia de la salud', 600,
     'El plan de prevención es obligatorio; el proveedor externo, no (art. '
     '30.5 de la Ley 31/1995)', 'parametrizado (DOM-26)'),
    ('Comisiones de reservas online', 2400,
     'TheFork y similares cobran por comensal sentado: mira la letra pequeña '
     'antes de firmar', 'parametrizado'),
    ('Reposición de menaje, cristalería y vajilla', 2400,
     'Roturas del ejercicio. En un casual con barra se rompe más de lo que '
     'se presupuesta', 'parametrizado'),
)

# ==========================================================================
# §2.9 — umbrales que auditan el caso base (clave, rótulo, valor, comentario)
# Los rótulos los pone `grupo_a`; aquí van el valor y el comentario.
# ==========================================================================
UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.65,
     'Por debajo, revisa precios de carta y escandallos'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.32,
     'Techo del propio libro: «Food cost objetivo 28-32 %»'),
    ('r_personal', 'Coste de personal / Ventas', 0.35,
     'Techo del propio libro: «Coste personal: no superar 35 % de los '
     'ingresos»'),
    ('r_alquiler', 'Alquiler / Ventas', 0.10,
     'Techo del propio libro: «Alquiler: no superar 8-10 % de los ingresos»'),
    ('r_neto', 'Resultado neto / Ventas', 0.05,
     'Suelo del propio libro: «Margen neto medio sector: 5-10 %»'),
)

# ==========================================================================
# §2.5 — escenarios extremos (cubiertos/día, ticket sin IVA, días)
# El «Realista» NO se teclea: lo lee de Supuestos y reproduce el P&L.
# ==========================================================================
ESCENARIOS = {
    'pesimista': (58, 15.90, 300),
    'optimista': (95, 18.50, 320),
}

# ==========================================================================
# §2.7 — reparto de la actividad por mes (suma 1)
# ==========================================================================
#: Estacionalidad de un bar-restaurante urbano: agosto flojo por vacaciones,
#: diciembre fuerte por comidas de empresa. Es un PARÁMETRO editable: si tu
#: zona es de costa, el perfil se invierte.
ESTACIONALIDAD = (0.070, 0.072, 0.082, 0.085, 0.090, 0.088,
                  0.085, 0.062, 0.085, 0.088, 0.087, 0.106)

# ==========================================================================
# §2.9 — textos de la hoja de Instrucciones
# ==========================================================================
INSTRUCCIONES = {
    'uso': [
        '6. La hoja «6. Tesorería 12 meses» responde la pregunta que decide '
        'una operación bancaria: en qué mes se agota la caja. El saldo mínimo '
        'del año nunca puede salir en rojo.',
        '7. La hoja «7. Financiación» cuadra lo que hace falta con lo que se '
        'aporta y monta el cuadro de amortización del préstamo. Si la '
        'diferencia sale en rojo, el plan no está financiado.',
    ],
    'referencias': [
        ('Ticket medio de restaurante casual (PVP)', '15-22 €',
         'Fichero v1.1. El de este plan son 19,58 € con IVA'),
        ('Alquiler de local de 80-120 m² en zona urbana', '2.000-4.500 €/mes',
         'Fichero v1.1'),
        ('Food cost objetivo', '28-32 %', 'Fichero v1.1'),
        ('Coste de personal sobre ventas', 'máx. 35 %', 'Fichero v1.1'),
        ('Margen neto medio del sector', '5-10 %', 'Fichero v1.1'),
        ('Punto de equilibrio', 'alcanzable en menos de 12 meses',
         'Fichero v1.1'),
        ('Convenio colectivo aplicable', 'PROVINCIAL de hostelería',
         'No existe una tabla salarial estatal única (DOM-24)'),
    ],
}

# ==========================================================================
# §2.10 — checklist de apertura: legal vigente y sin inventos
# ==========================================================================
CHECKLIST = {
    # (patrón que busca, texto nuevo). Se aplica celda a celda.
    'reemplazos': [
        # DOM-08 / COM-11 — el carnet de manipulador está DEROGADO
        (r'^Carnet de manipulador',
         'Formación en higiene alimentaria de todo el equipo'),
        (r'^Obligatorio, online',
         'El «carnet de manipulador» está derogado (RD 109/2010): la '
         'formación la acredita la EMPRESA y se documenta en el plan APPCC'),
        # DOM-09 — el RGSEAA no aplica al minorista que sirve al consumidor
        (r'^Autorizaci[óo]n sanitaria de funcionamiento',
         'Inscripción en el Registro Sanitario de tu Comunidad Autónoma '
         '(declaración responsable de inicio de actividad alimentaria)'),
        (r'^Registro RGSEAA$',
         'El Registro General Sanitario estatal NO aplica al minorista que '
         'sirve al consumidor final (art. 2.2 del RD 191/2011): el que te '
         'toca es el autonómico'),
        # DOM-25 — la cuota de autónomo, parametrizada y con nota de año
        (r'^Tarifa plana 80 EUR/mes',
         'Cuota según la base mínima del tramo que te corresponda. Consulta '
         'el importe del ejercicio en curso y verifica con tu gestoría si te '
         'aplica la cuota reducida de inicio de actividad'),
        # DOM-26 — el PRL obligatorio es el PLAN, no el proveedor
        (r'^Obligatorio contratar servicio externo',
         'Obligatorio es el PLAN de prevención, no contratar un servicio '
         'ajeno: con menos de 25 trabajadores y un solo centro el empresario '
         'puede asumir la actividad preventiva (art. 30.5 de la Ley 31/1995 '
         'y art. 11 del RD 39/1997)'),
        # TEC-25 / DOM-33 — el epígrafe de IAE, con los dos que pueden tocar
        (r'^Alta en el IAE',
         'Alta en el IAE: epígrafe 671.4 (restaurantes de dos tenedores) o '
         '673.1 (servicios de bar especiales), según el peso de la barra'),
        (r'^Exento si facturaci[oó]n',
         'Exento mientras la cifra de negocio no llegue al millón de euros. '
         'La elección del epígrafe la valida tu gestor: condiciona '
         'inspecciones y licencia'),
        # DOM-13 / COM-08 — Crea y Crece, sin el depósito de 3.000 € inventado
        (r'^Ley Crea y Crece',
         'Ley 18/2022 (Crea y Crece): capital mínimo 1 €, con la obligación '
         'de destinar el 20 % del beneficio a reserva legal hasta que capital '
         'y reserva sumen 3.000 €, y responsabilidad solidaria de los socios '
         'por esa diferencia'),
        (r'^Capital social min 1 EUR',
         'Capital social mínimo 1 € (Ley 18/2022). No existe ningún depósito '
         'obligatorio de 3.000 € a cinco años'),
        # TEC-26 — la errata visible del entregable
        (r'Priorizarcexperiencia',
         'Prioriza la experiencia en hostelería'),
    ],
    # DOM-09 — la segunda fila del RGSEAA duplicaba el trámite
    'suprimir': [
        'Inscripcion Registro General Sanitario',
        'Inscripción Registro General Sanitario',
    ],
    # DOM-23 — UN solo cronograma, el conservador: si las licencias tardan
    # 1-3 meses y la obra 4-8 semanas, no se puede abrir el mes 6
    'fases': {
        r'^FASE 1': 'FASE 1: CONSTITUCIÓN DE LA EMPRESA (meses 1-2)',
        r'^FASE 2': 'FASE 2: LOCAL Y LICENCIAS (meses 2-6)',
        r'^FASE 3': 'FASE 3: OBRA Y EQUIPAMIENTO (meses 4-7)',
        r'^FASE 4': 'FASE 4: PERSONAL (mes 7)',
        r'^FASE 5': 'FASE 5: MARKETING Y LANZAMIENTO (meses 7-8)',
        r'^FASE 6': 'FASE 6: PRIMEROS 90 DÍAS (meses 8-11)',
    },
    'cabecera_altas': 'FASE 7: OBLIGACIONES QUE HAY QUE TENER CERRADAS ANTES '
                      'DE ABRIR (meses 6-8)',
    # TEC-18 — trámites que faltaban y cuestan dinero o multa
    # (hoja, categoría, tarea, responsable, plazo, nota)
    'altas': [
        ('.', 'Seguros',
         'Contratar el seguro de responsabilidad civil y el multirriesgo del '
         'local', 'Socios', 'Antes de abrir',
         'Está presupuestado en la hoja de Inversión y hasta ahora no había '
         'ninguna tarea que lo ejecutara'),
        ('.', 'Legal',
         'Hojas de reclamaciones oficiales y su cartel anunciador', 'Socios',
         '1 día',
         'El modelo y el texto del cartel los aprueba tu Comunidad '
         'Autónoma'),
        ('.', 'Laboral',
         'Registro horario diario de la jornada de todo el equipo',
         'Gestoría', 'Desde el primer contrato',
         'Art. 34.9 del Estatuto de los Trabajadores; se conserva cuatro '
         'años'),
        ('.', 'Legal',
         'Contrato con gestor autorizado de residuos y de aceite vegetal '
         'usado', 'Socios', '2 semanas',
         'Se comprueba en la inspección; el aceite usado no puede ir al '
         'desagüe'),
        ('.', 'APPCC',
         'Contrato de desinsectación, desratización y desinfección (DDD)',
         'Socios', '1 semana',
         'Empresa inscrita en el ROESB; el certificado forma parte del plan '
         'APPCC'),
        ('.', 'Legal',
         'Licencia de derechos de autor por la música ambiental', 'Socios',
         '2 semanas',
         'SGAE y AGEDI-AIE son dos licencias distintas y se pagan las dos'),
        ('.', 'APPCC',
         'Plan de prevención de las pérdidas y el desperdicio alimentario',
         'Cocina', '1 semana',
         'Ley 1/2025: obliga a tener un plan escrito y a ofrecer la comida '
         'sobrante para donación'),
        ('.', 'Obra',
         'Boletines de la instalación eléctrica y de la instalación de gas',
         'Instalador', 'Con la obra',
         'Sin ellos no hay alta de suministros ni licencia de actividad'),
        ('.', 'Laboral',
         'Comunicación de apertura del centro de trabajo a la autoridad '
         'laboral', 'Gestoría', 'Primeros 30 días',
         'Se presenta en los treinta días siguientes al inicio de la '
         'actividad'),
        ('.', 'Legal',
         'Cartel de prohibición de venta de alcohol y tabaco a menores',
         'Socios', '1 día',
         'La redacción exacta y el tamaño los fija tu Comunidad Autónoma'),
    ],
}

# ==========================================================================
# Registro de lo que cambia de valor respecto de la v1.1 (§1.3: «la
# diferencia entre el valor viejo y el nuevo queda anotada por fichero»)
# ==========================================================================
RECALIBRADO = (
    ('Coste de personal imputado al P&L', '115.200 €',
     '= hoja Personal, por fórmula',
     'TEC-01/DOM-01: el P&L decía «ver hoja Personal» y usaba otra cifra'),
    ('Plantilla', '7 personas / 209.171 €',
     '6 puestos (dos parciales) / ~147.100 €',
     '§7-bis.17: dimensionada por horas de servicio para 56 plazas; con la '
     'plantilla anterior el coste laboral era el 66,3 % de las ventas'),
    ('Cubiertos/día del año 1', '55', '80',
     '1,43 rotaciones sobre 56 plazas, por debajo del techo de 1,8 que usa '
     'el propio documento'),
    ('Ticket medio', '18,50 € (sin declarar IVA)', '17,20 € SIN IVA',
     'TEC-11/DOM-30: equivale a 19,58 € de PVP, dentro del rango 15-22 € del '
     'propio libro'),
    ('Alquiler', '3.000 €/mes', '2.900 €/mes',
     'Con 3.000 € el ratio alquiler/ventas incumplía el techo de 8-10 % que '
     'fija el propio libro'),
    ('Suministros', '1.200 €/mes', '1.800 €/mes',
     'Una cocina con horno, cámaras y campana no consume el 3,4 % de las '
     'ventas'),
    ('Fondo de maniobra', '30.000 € etiquetados «3 meses»',
     '= 3 × costes fijos mensuales, por fórmula',
     'TEC-07/DOM-12/NUEVO-01: los 30.000 € cubrían 1,8 meses'),
    ('Amortización', '5.000 €/año (base implícita 50.000 €)',
     '= base amortizable real / vida útil',
     'TEC-20: el inmovilizado del propio libro suma bastante más, y el fondo '
     'de maniobra no se amortiza'),
    ('Cuota del préstamo en el P&L', '7.200 €/año de cuota completa',
     'sólo los intereses; el principal va a tesorería',
     'TEC-10/DOM-15: meter la cuota entera antes del resultado convierte el '
     'P&L en un flujo de caja'),
    ('Impuesto de Sociedades', '25 % en los años 2 y 3, sin compensar la BIN',
     '15 % los dos primeros ejercicios con base positiva y compensación de '
     'bases negativas',
     'TEC-06/DOM-15: arts. 26 y 29.1 LIS'),
    ('Comisiones de delivery', '5 % de TODA la facturación, sin interruptor',
     '% del canal × comisión de la plataforma, a 0 por defecto',
     'TEC-23/DOM-34'),
    ('Coste de la bebida', 'food cost del 30 % sobre el total MÁS un 22 % '
     'sobre la bebida', 'cada familia paga su propio coste',
     'TEC-04/DOM-04: 33.119,63 € cobrados dos veces en el año 1'),
)
