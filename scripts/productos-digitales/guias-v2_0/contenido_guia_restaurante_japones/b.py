# -*- coding: utf-8 -*-
"""
contenido_guia_restaurante_japones/b.py — contenido del **grupo B**
(checklists y cronograma, `guias-v2-SPEC.md` §3) para «Cómo Montar un
Restaurante Japonés» (60 plazas, 65 EUR).

Japonés lleva **6** checklists (molde A: legal, contratación, APPCC, diseño
de sala japonesa + barra sushi + barra sake, equipamiento de cocina japonesa,
marketing pre-apertura — NO lleva `vajilla-cristalería` ni
`inspeccion-michelin-repsol`, que sólo tiene el representante) más
`cronograma-apertura-gantt.xlsx`.

DIFERENCIA CON EL REPRESENTANTE (COM-17/18) — recuentos, medidos, frente al
dashboard `GuiaRestauranteJaponesDashboard.tsx:41-46`
--------------------------------------------------------------------------
A diferencia de casual/mexicano/peruano (donde el dashboard anunciaba las
MISMAS 6 cifras copiadas entre hermanos, 32/35/33/30/24/25), **el dashboard
de japonés SÍ trae sus propias cifras, y las 6 CUADRAN con el fichero real**
(única guía de las cuatro verificadas hasta ahora en T6 donde esto ocurre):
  · checklist-legal.xlsx:        anuncia 42, medido **42** (A5:A46) ✅
  · checklist-equipamiento:      anuncia 36, medido **36** (A5:A40) ✅
  · checklist-appcc.xlsx:        anuncia 46, medido **46** (A5:A50) ✅
  · checklist-diseno-sala:       anuncia 32, medido **32** (A5:A36) ✅
  · checklist-contratacion.xlsx: anuncia 31, medido **31** (A5:A35) ✅
  · checklist-marketing.xlsx:    anuncia 31, medido **32** (A5:A36) — el
    fichero ya mide UNA más que la tarjeta, no hace falta completar nada
    para cumplir el anuncio.
No hay ninguna cifra que «completar hasta lo anunciado» (§3.4/§6.5): las
correcciones de contenido de abajo se aplican igual (son obligaciones legales
y sanitarias de familia, no relleno para cuadrar un número), y en los 6 casos
el recuento SUBE por encima del anunciado — nunca por debajo, que es la única
dirección prohibida por la SPEC.

CENSO DE SUSTITUCIONES — verificado abriendo el fichero, no asumido de los
hermanos anteriores
--------------------------------------------------------------------------
  · **No hay «Libro de visitas de la Inspección de Trabajo»** en
    `checklist-legal` (42 filas, categoría «Laboral» con sólo 4 ítems:
    contratos, contrato itamae, PRL, calendario laboral — verificado una a
    una): no hay nada que sustituir por DOM-12; el registro de jornada y la
    comunicación de apertura entran como ítems NUEVOS.
  · **No hay «Licencia C3»**: el ítem 9 ya dice «Licencia de actividad /
    declaración responsable», sin atribuir el nombre C3 a nada, y no hay
    ninguna mención a «CIRCE». DOM-11/COM-28 **no aplica** como sustitución
    (nada que corregir); se deja constancia.
  · **No hay duplicado de alta censal** (una sola fila, «Alta censal en
    Hacienda (modelo 036/037)», categoría Empresa): el ítem de facturación
    verificable (RD 1007/2023) entra como NUEVO, no liberando una fila
    existente — mismo patrón que casual/mexicano/peruano (aquí RD-JP-01).
  · **No hay «Plan de igualdad (si >50 empleados)»** ni «Cláusula de
    confidencialidad y no competencia»: el checklist de contratación de
    japonés (31 ítems) no las tenía. DOM-38 no aplica como sustitución aquí
    (14 puestos en `plantilla-turnos-brigada.xlsx`, muy lejos del umbral de
    50); no se inventa una fila sobre un supuesto que esta guía no vende. Se
    deja una nota de remisión, igual que en casual/mexicano/peruano.
  · **SÍ hay las CINCO piezas de anisakis, más completo que los tres
    hermanos verificados hasta ahora** (`checklist-appcc` filas 13-18,
    categoría «Anisakis (PCC)»): congelación previa (fila 13), congelador con
    registro automático (fila 14), registro por lote (fila 15), archivo 12
    meses (fila 16), certificado proveedor acuicultura (fila 17) e
    **información al cliente en carta** (fila 18) — las SEIS piezas que exige
    §3.2/DOM-14 ya están, salvo que la fila 13 cita «-20°C/24h» **sin base
    normativa y sin la alternativa de -35°C/15h**: sólo hace falta la
    SUSTITUCIÓN de la cita legal, cero ítems nuevos para anisakis. Coherente
    con que esta guía es la que MÁS pescado crudo vende de la familia
    (sashimi, sushi, chirashi — 4 de los 15 platos de
    `menu-engineering-matrix.xlsx` llevan pescado crudo: sashimi moriawase,
    nigiri salmón, nigiri toro, chirashi bowl).

DÓNDE VA CADA OBLIGACIÓN LABORAL NUEVA: igual que el representante, casual,
mexicano y peruano, **una sola vez**, en `checklist-legal`, categoría
`Laboral` (§3.1, COM-15): así no se cuenta dos veces en el presupuesto de
apertura.

⚠️ ESPACIO FINO (U+202F) y GUION NO SEPARABLE (U+2011): por escape (`N`, `G`),
nunca escribiendo el carácter (CLAUDE.md).
"""

N = ' '      # espacio fino (U+202F), SIEMPRE por escape
G = '‑'      # guion no separable (U+2011), SIEMPRE por escape

PRESUPUESTAR = ('Sin importe tasado en la guía: pide presupuesto y escríbelo '
                'aquí (la celda es editable y el TOTAL se recalcula).')


def _rango(a, b):
    return a + G + b


# ==========================================================================
# checklist-legal.xlsx — 42 ítems medidos (A5:A46). §3.1 + DOM-23
# ==========================================================================
LEGAL = {
    'anuncia': 42,
    # No hay «Libro de visitas» ni «Licencia C3»/«CIRCE» que sustituir (ver
    # cabecera del módulo): la lista de sustituciones queda vacía a propósito.
    'sustituciones': [],
    'sustituciones_extra': [],
    'notas': [],
    'nuevas': [
        # --- §3.1: laboral vigente, sin umbral de plantilla ---------------
        {'id': 'DOM-12', 'fuente': 'SPEC §3.1', 'categoria': 'Laboral',
         'tarea': ('Registro diario de jornada (RD' + G + 'ley 8/2019, '
                   'art.' + N + '34.9 ET): sistema de fichaje y '
                   'conservación 4 años'),
         'responsable': 'Asesor laboral', 'estado': 'Pendiente', 'coste': None,
         'notas': ('No estaba en ninguna de las 42 filas del checklist. Es '
                   'de las infracciones más sancionadas en hostelería, y con '
                   '14 puestos entre cocina y sala (cuadrante parcialmente '
                   'partido) el control horario no es opcional. '
                   + PRESUPUESTAR)},
        {'id': 'DOM-12', 'fuente': 'SPEC §3.1', 'categoria': 'Laboral',
         'tarea': ('Comunicación de apertura del centro de trabajo a la '
                   'autoridad laboral'),
         'responsable': 'Asesor laboral', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Obligatoria al iniciar la actividad (art.' + N + '6 '
                   'RD 337/2010). La tramita tu asesoría. ' + PRESUPUESTAR)},
        {'id': 'DOM-38/COM-15', 'fuente': 'SPEC §3.1', 'categoria': 'Laboral',
         'tarea': 'Registro retributivo (RD 902/2020)',
         'responsable': 'Asesor laboral', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Obligatorio para TODAS las empresas, sin umbral de '
                   'plantilla — un restaurante de 14 puestos también lo '
                   'necesita. ' + PRESUPUESTAR)},
        {'id': 'DOM-38', 'fuente': 'SPEC §3.1', 'categoria': 'Laboral',
         'tarea': ('Protocolo de prevención del acoso sexual '
                   '(LO 3/2007 art.' + N + '48)'),
         'responsable': 'Abogado / SPA', 'estado': 'Pendiente', 'coste': None,
         'notas': 'También sin umbral de plantilla. ' + PRESUPUESTAR},
        # --- RD 1007/2023: sistema de facturación verificable (Verifactu) --
        {'id': 'RD-JP-01',
         'fuente': 'SPEC §3.1 (patrón del representante, sin duplicado que '
                   'liberar en esta guía) · RD 1007/2023',
         'categoria': 'Fiscal',
         'tarea': ('Sistema informático de facturación verificable en el '
                   'TPV (RD 1007/2023 y su Orden de desarrollo)'),
         'responsable': 'Asesor fiscal + proveedor de TPV',
         'estado': 'Pendiente', 'coste': None,
         'notas': ('No hay una fila duplicada de alta censal que liberar en '
                   'este checklist (a diferencia del representante): se '
                   'añade como ítem nuevo. Tu TPV + pantallas de cocina '
                   '(partida de Inversión) tiene que emitir facturas con los '
                   'registros que exige la norma. ' + PRESUPUESTAR)},
        # --- §3.1 / DOM-23: el bloque «Local», que no existía --------------
        {'id': 'DOM-23', 'fuente': 'SPEC §3.1', 'categoria': 'Local',
         'tarea': ('Contrato de arrendamiento para uso distinto de vivienda '
                   '(duración, prórrogas, renta y actualización)'),
         'responsable': 'Abogado', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Las cadenas «arrendamiento», «fianza», «traspaso» y '
                   '«carencia» no aparecían en ninguno de los 19 xlsx de '
                   'esta guía. ' + PRESUPUESTAR)},
        {'id': 'DOM-23', 'fuente': 'SPEC §3.1', 'categoria': 'Local',
         'tarea': ('Fianza legal de 2 mensualidades y garantía adicional '
                   '(aval o depósito)'),
         'responsable': 'Propiedad', 'estado': 'Pendiente', 'coste': None,
         'notas': ('La fianza legal de 2 mensualidades la fija el '
                   'art.' + N + '36 LAU; la garantía adicional se negocia. '
                   'Escribe aquí el importe de TU renta.')},
        {'id': 'DOM-23', 'fuente': 'SPEC §3.1', 'categoria': 'Local',
         'tarea': ('Carencia de renta durante la obra y la tramitación de la '
                   'licencia, pactada por escrito'),
         'responsable': 'Abogado', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El cronograma de esta misma guía tarda desde el mes 3 '
                   '(local/licencias) hasta el mes 5 (obra e instalaciones) '
                   'en avanzar sin facturar un euro, y la búsqueda del '
                   'itamae —tarea crítica— puede tardar hasta el mes 8: sin '
                   'carencia, son meses de renta antes de abrir.')},
        {'id': 'DOM-23', 'fuente': 'SPEC §3.1', 'categoria': 'Local',
         'tarea': 'Cláusula de cesión y traspaso pactada expresamente',
         'responsable': 'Abogado', 'estado': 'Pendiente', 'coste': None,
         'notas': 'Sin ella, vender el negocio depende del criterio de la propiedad.'},
        {'id': 'DOM-23', 'fuente': 'SPEC §3.1', 'categoria': 'Local',
         'tarea': ('Condición suspensiva por denegación de la licencia de '
                   'actividad o de la licencia de terraza'),
         'responsable': 'Abogado', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Si el ayuntamiento deniega alguna de las dos licencias, '
                   'el contrato decae y recuperas la fianza.')},
    ],
}

# ==========================================================================
# checklist-contratacion.xlsx — 31 ítems medidos. Redacción, no sustitución.
# ==========================================================================
CONTRATACION = {
    'anuncia': 31,
    # DOM-38 (plan de igualdad / no-competencia): no aplica como sustitución
    # (ver cabecera del módulo). Se deja una NOTA de remisión al checklist
    # legal, para que el registro retributivo y el protocolo de acoso no se
    # cuenten dos veces si el cliente los ve aquí primero.
    'notas': [
        {
            'id': 'DOM-38/COM-15',
            'buscar': 'Alta Seguridad Social',
            'notas': ('El registro retributivo (RD 902/2020) y el protocolo '
                      'de prevención del acoso sexual (LO 3/2007) están en '
                      'el checklist legal, categoría Laboral: son la misma '
                      'obligación de empresa, no una tarea de contratación '
                      'individual, y no se presupuestan dos veces.'),
        },
    ],
    'sustituciones': [],
}

# ==========================================================================
# checklist-appcc.xlsx — 46 ítems medidos. §3.2 (DOM-14/DOM-15)
# ==========================================================================
APPCC = {
    'anuncia': 46,
    # El bloque MÁS COMPLETO de los cuatro hermanos verificados: registro de
    # lotes (fila 15), archivo 12 meses (fila 16), certificado de acuicultura
    # (fila 17) e INFORMACIÓN AL CLIENTE (fila 18) ya están. Sólo falta la
    # cita legal correcta (Decisión ANISAKIS-2026-08-29: RD 1021/2022, no el
    # RD 1420/2006 derogado) y la alternativa de -35°C/15h en la fila del
    # PCC en sí (fila 13).
    'sustituciones': [
        {'id': 'DOM-14',
         'fuente': 'SPEC §3.2 · RD 1021/2022, art. 8.1 (que derogó el '
                   'RD 1420/2006)',
         'buscar': 'CONGELACIÓN PREVIA obligatoria -20°C/24h todo pescado crudo',
         'tarea': ('Congelación preventiva (' + G + '20' + N + '°C durante '
                   'al menos 24' + N + 'h, o ' + G + '35' + N + '°C durante '
                   '15' + N + 'h) para todo pescado de consumo crudo o '
                   'marinado (sashimi, sushi, chirashi) — RD 1021/2022, '
                   'art.' + N + '8.1 (que derogó el RD 1420/2006) y Rgto. '
                   '(CE) 853/2004, Anexo III, Secc. VIII, Cap. III.D'),
         'responsable': 'Itamae', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El ítem original citaba «-20°C/24h» sin base normativa y '
                   'sin la alternativa de -35°C/15h. Esta es la guía con MÁS '
                   'pescado crudo de la familia — sashimi, sushi, chirashi — '
                   'y las otras cinco piezas del bloque (congelador con '
                   'registro automático, registro de lotes, archivo 12 '
                   'meses, certificado de proveedor de acuicultura e '
                   'información al cliente en carta, filas 14-18) ya están '
                   'completas: sólo faltaba la cita legal exacta. El binomio '
                   'legal son 24' + N + 'h a ' + G + '20' + N + '°C EN TODO '
                   'EL PRODUCTO; los «5' + N + 'días» que circulan son la '
                   'recomendación para congeladores DOMÉSTICOS, que no '
                   'garantizan esa temperatura. La congelación puede '
                   'haberla hecho el proveedor si está justificado '
                   'documentalmente (art.' + N + '8.1 del RD 1021/2022): '
                   'guarda ese justificante. ' + PRESUPUESTAR)},
    ],
    'nuevas': [
        # --- baja temperatura y vacío (DOM-15) — familia(8), aunque japonés
        # no presupuesta roner/envasadora: se deja como buena práctica
        # ligera, no como bloque completo, precisamente porque el propio
        # checklist de equipamiento de esta guía no incluye esos equipos
        # (verificado: las cadenas «roner» y «envasadora» no aparecen en las
        # 36 filas — la cocción a temperatura controlada de esta cocina va
        # por horno mixto y salamandra, no por vacío).
        {'id': 'DOM-15', 'fuente': 'SPEC §3.2 (adaptado: sin roner/envasadora '
                                   'en el equipamiento de esta guía)',
         'categoria': 'Baja temperatura y vacío',
         'tarea': ('Si en algún momento incorporas cocción a baja '
                   'temperatura o envasado al vacío (por ejemplo, para el '
                   'chashu del ramen o el pato laqueado): registro de sonda '
                   'por lote y enfriamiento a ≤10' + N + '°C en menos de '
                   '2' + N + 'h'),
         'responsable': 'Jefe cocina', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El checklist de equipamiento de japonés NO presupuesta '
                   'roner ni envasadora: esta guía cuece el chashu y los '
                   'caldos tonkotsu/shoyu en olla y horno mixto, no al '
                   'vacío. Se deja como aviso condicional en lugar del '
                   'bloque completo que sí lleva el representante (que sí '
                   'presupuesta ambos equipos).')},
    ],
}

# ==========================================================================
# checklist-diseno-sala-japonesa.xlsx — 32 ítems medidos. DOM-39
# ==========================================================================
DISENO_SALA = {
    'anuncia': 32,
    'nuevas': [
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Acústica',
         'tarea': ('Limitador' + G + 'registrador acústico homologado y '
                   'estudio de impacto acústico'),
         'responsable': 'Ingeniero acústico', 'estado': 'Pendiente',
         'coste': None,
         'notas': ('El checklist ya lleva «paneles absorbentes» y «sistema '
                   'de música» (confort acústico, ambiente silencioso de '
                   'inspiración japonesa) pero no el limitador homologado '
                   'que exige la licencia en buena parte de las ordenanzas '
                   'municipales para locales con música. ' + PRESUPUESTAR)},
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Accesibilidad',
         'tarea': ('Alumbrado de emergencia y señalización de evacuación '
                   '(CTE DB' + G + 'SUA / DB' + G + 'SI)'),
         'responsable': 'Instalador', 'estado': 'Pendiente', 'coste': None,
         'notas': ('«Señalética interior con identidad japonesa» (fila 35) '
                   'ya existía; el ALUMBRADO de emergencia (autónomo, con '
                   'batería) es otra instalación y no estaba. '
                   + PRESUPUESTAR)},
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Personal',
         'tarea': ('Vestuario de personal con taquillas, separado de los '
                   'aseos de clientes (RD 486/1997)'),
         'responsable': 'Arquitecto', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Los aseos del checklist (fila 10 y 33) son de clientes '
                   '(con PMR): no hay ninguna línea para el vestuario de los '
                   '14 puestos de plantilla-turnos-brigada.xlsx. '
                   + PRESUPUESTAR)},
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Accesibilidad',
         'tarea': ('Certificación de aforo y anchura de los recorridos de '
                   'evacuación'),
         'responsable': 'Arquitecto', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El aforo declarado tiene que cuadrar con las 60 plazas '
                   'del plano (fila 2: barra sushi 8-12 + mesas).')},
    ],
}

# ==========================================================================
# checklist-equipamiento-cocina-japonesa.xlsx — 36 ítems medidos. DOM-20
# ==========================================================================
#: A diferencia del representante, japonés YA presupuesta el horno mixto
#: (12.000 EUR, fila 17) y una campana extractora REFORZADA (10.000 EUR,
#: fila 30) más la salida de humos reglamentaria (6.000 EUR, fila 31): DOM-20
#: no encuentra el mismo defecto de fondo. Lo que sí falta, verificado fila a
#: fila, es la extinción automática en campana — obligada por el CTE DB-SI y
#: por la aseguradora en cuanto hay freidora (fila 19), robata de carbón
#: binchotan (checklist-equipamiento-cocina-japonesa se limita a la cocina;
#: la parrilla robata va tasada en `plan-financiero!Inversión` y en
#: `calculadora-capex`, no en este checklist, así que no aparece en las 36
#: filas) y tempura — y que ni el representante ni casual ni mexicano ni
#: peruano tenían tampoco.
EQUIPAMIENTO = {
    'anuncia': 36,
    'notas': [
        {'id': 'DOM-20', 'buscar': 'Campana extractora REFORZADA + filtros',
         'notas': ('Cubre la campana y el filtrado; la extinción automática '
                   'va en la línea nueva de abajo, que es un sistema '
                   'distinto exigido por el CTE DB' + G + 'SI en cuanto hay '
                   'freidora, robata y tempura.')},
    ],
    'nuevas': [
        {'id': 'DOM-20', 'fuente': 'SPEC §3.4 (' + _rango('2.500', '4.000')
                                   + N + '€)', 'categoria': 'Extracción',
         'tarea': ('Sistema automático de extinción en campana '
                   '(CTE DB' + G + 'SI y aseguradora)'),
         'responsable': 'Instalador', 'estado': 'Pendiente', 'coste': 2500,
         'notas': ('Rango ' + _rango('2.500', '4.000') + N + '€; precargado '
                   'el mínimo. Con freidora doble (fila 19), robata de '
                   'carbón binchotan (`plan-financiero!Inversión`, fila '
                   '«Parrilla robata carbón binchotan», 6.500 EUR) y '
                   'teppanyaki es exigible, y la aseguradora lo pide para '
                   'emitir la póliza. La cadena «extinción» no aparecía en '
                   'ninguna de las 36 filas.')},
        {'id': 'RD-JP-02',
         'fuente': 'parametrizado (partida del CAPEX del representante sin '
                   'línea propia en esta guía: «instalación, transporte y '
                   'puesta en marcha, 12 %» de calculadora-capex-'
                   'gastronomico.xlsx)',
         'categoria': 'Cocción',
         'tarea': ('Instalación, transporte y puesta en marcha del '
                   'equipamiento de cocina'),
         'responsable': 'Proveedor', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El equipamiento de esta guía (suihanki, ramen cooker, '
                   'robata, horno mixto, cámaras, tren de lavado…) se compra '
                   'a varios proveedores y cada uno cobra transporte e '
                   'instalación aparte: presupuesta un 10-12 % adicional '
                   'sobre el total de equipamiento, como ya hace el '
                   'representante. ' + PRESUPUESTAR)},
        {'id': 'RD-JP-02',
         'fuente': 'SPEC §3.2 · DOM-14 · RD 1021/2022, art. 8.1',
         'categoria': 'Frío',
         'tarea': ('Sonda/data logger de temperatura dedicado a verificar y '
                   'registrar la congelación preventiva del pescado '
                   '(' + G + '20' + N + '°C / 24' + N + 'h) en el congelador '
                   'certificado'),
         'responsable': 'Itamae', 'estado': 'Pendiente', 'coste': 300,
         'notas': ('El congelador certificado -20°C (fila 22) ya está '
                   'presupuestado y su registro automático propio también '
                   '(`checklist-appcc.xlsx` fila 14 lo trae de fábrica); '
                   'esta partida es la SONDA física del propio equipo de '
                   'cocina —no del checklist APPCC—, que ninguna de las 36 '
                   'filas de equipamiento incluye como línea de compra '
                   'independiente.')},
    ],
}

# ==========================================================================
# checklist-marketing-preapertura.xlsx — 32 ítems medidos. DOM-40
# ==========================================================================
#: A diferencia del representante y de casual/mexicano, japonés YA
#: presupuesta DOS piezas de contenido separadas (fila 19 «Sesión
#: fotográfica profesional» 600 EUR y filas 20-21 dos vídeos, 700+500 EUR):
#: la de FOTOGRAFÍA sigue estando por debajo del rango real que fija la SPEC
#: (1.500-3.000 EUR) — incluso más lejos que en peruano (400 EUR) o el
#: representante (500 EUR), 600 EUR sigue sin comprar fotografía gastronómica
#: profesional completa para sushi + ramen + robata + decoración—; los dos
#: vídeos (filas 20-21) son piezas distintas (contenido para redes, no
#: fotografía de producto para carta/plataformas) y no se tocan.
MARKETING = {
    'anuncia': 31,
    'sustituciones': [
        {
            'id': 'DOM-40',
            'fuente': 'SPEC §3.4 (' + _rango('1.500', '3.000') + N + '€)',
            'buscar': ('Sesión fotográfica profesional (sushi, ramen, '
                       'robata, decoración)'),
            'tarea': ('Sesión fotográfica profesional (sushi, ramen, robata, '
                      'decoración) (' + _rango('15', '25') + N + 'platos)'),
            'coste': 1500,
            'notas': ('Rango real ' + _rango('1.500', '3.000') + N + '€ '
                      '(SPEC §3.4). Va precargado el MÍNIMO. Los 600' + N
                      + '€ anteriores no llegan ni a los 500' + N + '€ del '
                      'representante y no compran fotografía gastronómica '
                      'profesional para toda la carta.'),
        },
    ],
    'nuevas': [],
}

# ==========================================================================
# Mapa fichero → configuración (lo lee `grupo_b.post`)
# ==========================================================================
CHECKLISTS = {
    'checklist-legal.xlsx': LEGAL,
    'checklist-contratacion.xlsx': CONTRATACION,
    'checklist-appcc.xlsx': APPCC,
    'checklist-diseno-sala-japonesa.xlsx': DISENO_SALA,
    'checklist-equipamiento-cocina-japonesa.xlsx': EQUIPAMIENTO,
    'checklist-marketing-preapertura.xlsx': MARKETING,
}

# ==========================================================================
# cronograma-apertura-gantt.xlsx — molde de 12 meses, rejilla YA marcada
# con 'X' (variante «hermanos»/T2 del Gantt: `_deducir_de_marcas` calcula
# Mes inicio/Duración SOLO. No hace falta ninguna tarea nueva: japonés YA
# incluye «Negociación alquiler y contrato» (fila 8) y «Plan financiero y
# búsqueda financiación» (fila 2) — los dos huecos que DOM-22/DOM-23
# encontraron vacíos en el representante). §3.5, TEC-14, TEC-15.
# ==========================================================================
GANTT = {
    # Ninguna sustitución: «Licencia actividad / declaración responsable»
    # (fila 9) ya usa el nombre genérico, sin atribuirlo a C3 (igual que en
    # checklist-legal).
    'sustituciones': [],
    'nuevas_tareas': [],
    'tareas': {},
}
