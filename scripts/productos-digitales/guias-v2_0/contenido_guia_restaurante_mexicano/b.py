# -*- coding: utf-8 -*-
"""
contenido_guia_restaurante_mexicano/b.py — contenido del **grupo B**
(checklists y cronograma, `guias-v2-SPEC.md` §3) para «Cómo Montar un
Restaurante Mexicano» (80 plazas, 65 EUR).

Mexicano lleva **6** checklists (molde A: legal, contratación, APPCC, diseño
de sala mexicana + barra tequilas, equipamiento de cocina mexicana, marketing
pre-apertura — NO lleva `vajilla-cristalería` ni `inspeccion-michelin-repsol`,
que sólo tiene el representante) más `cronograma-apertura-gantt.xlsx`.

DIFERENCIA CON EL REPRESENTANTE Y CON CASUAL — recuentos por debajo de lo
medido, no por encima
--------------------------------------------------------------------------
El dashboard de mexicano (`GuiaRestauranteMexicanoDashboard.tsx:41-46`)
anuncia MENOS de lo que el censo mide hoy en los 6 checklists:

  · checklist-legal.xlsx:       anuncia 32, medido **38** (A5:A42)
  · checklist-equipamiento:     anuncia 35, medido **35** (A5:A39) — cuadra
  · checklist-appcc.xlsx:       anuncia 33, medido **37** (A5:A41)
  · checklist-diseno-sala:      anuncia 30, medido **32** (A5:A36)
  · checklist-contratacion:     anuncia 24, medido **28** (A5:A32)
  · checklist-marketing:        anuncia 25, medido **27** (A5:A31)

Es el defecto CONTRARIO al COM-17/COM-18 del representante (que prometía MÁS
de lo que el fichero tenía): aquí el fichero ya trae MÁS ítems de los que la
tarjeta anuncia, así que el gate «recuento ≥ anunciado» YA pasa antes de
añadir un solo ítem nuevo, y sigue pasando después (los recuentos sólo suben).
No es una corrección que haya que aplicar al xlsx: es una cifra de venta
desactualizada, y **queda anotada para que T8 la actualice** con el número
real (igual que hizo casual con sus 6 recuentos, en la dirección contraria).

CENSO DE SUSTITUCIONES — verificado abriendo el fichero, no asumido del
representante ni de casual
--------------------------------------------------------------------------
  · **No hay «Libro de visitas de la Inspección de Trabajo»** en
    `checklist-legal` (38 filas, categoría «Laboral» con sólo 3 ítems:
    contratos, PRL, calendario laboral — verificado una a una): no hay nada
    que sustituir por DOM-12; el registro de jornada entra como ítem NUEVO.
  · **No hay «Licencia C3»**: el ítem 9 ya dice «Licencia de actividad /
    declaración responsable», sin atribuir el nombre C3 a nada. DOM-11/COM-28
    **no aplica** como sustitución (nada que corregir); se deja constancia.
  · **No hay duplicado de alta censal** (una sola fila, «Alta censal en
    Hacienda (modelo 036/037)», categoría Empresa): RD-32 (dedup del
    representante) no aplica; el ítem de facturación verificable
    (RD 1007/2023) entra como NUEVO, no liberando una fila existente — mismo
    patrón que casual (RD-CASUAL-01), aquí RD-MEX-01.
  · **No hay «Plan de igualdad (si >50 empleados)»** ni «Cláusula de
    confidencialidad y no competencia»: el checklist de contratación de
    mexicano (28 ítems) no las tenía. DOM-38 no aplica como sustitución aquí
    (14 puestos, muy lejos del umbral de 50); no se inventa una fila sobre un
    supuesto que esta guía no vende. Se deja una nota de remisión, igual que
    en casual.
  · **SÍ hay un ítem PARCIAL de anisakis**: `checklist-appcc` fila 34,
    categoría «Pescado», «Congelación previa -20°C/24h para ceviche
    (anisakis)», sin cita normativa, sin la alternativa de -35°C/15h y sin
    los dos ítems complementarios (registro de lotes, información al
    comensal) que sí exige §3.2/DOM-14. **Este es el único caso de los tres
    hermanos verificados (representante, casual, mexicano) donde el ítem NO
    está totalmente ausente**: se SUSTITUYE (no se duplica) por la redacción
    completa con la cita correcta, y se completa con las dos filas
    complementarias como NUEVAS — justificado porque el propio Matrix de
    menu-engineering de esta guía vende un «Ceviche mexicano de lubina»
    (fila 12), pescado crudo curado en cítrico.

DÓNDE VA CADA OBLIGACIÓN LABORAL NUEVA: igual que el representante y casual,
**una sola vez**, en `checklist-legal`, categoría `Laboral` (§3.1, COM-15): así
no se cuenta dos veces en el presupuesto de apertura.

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
# checklist-legal.xlsx — 38 ítems medidos (A5:A42). §3.1 + DOM-23
# ==========================================================================
LEGAL = {
    'anuncia': 32,
    # No hay «Libro de visitas» ni «Licencia C3» que sustituir (ver cabecera
    # del módulo): la lista de sustituciones queda vacía a propósito.
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
         'notas': ('No estaba en ninguna de las 38 filas del checklist. Es '
                   'de las infracciones más sancionadas en hostelería, y con '
                   '14 puestos en dos turnos (cocina + sala, cuadrante '
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
        {'id': 'RD-MEX-01',
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
                   '«carencia» no aparecían en ninguno de los 15 xlsx de '
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
         'notas': ('El cronograma de esta misma guía tarda desde el mes 5 '
                   '(obra) hasta el mes 9-10 (licencias resueltas) en llegar '
                   'a la apertura: sin carencia, son meses de renta antes de '
                   'facturar un euro.')},
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
# checklist-contratacion.xlsx — 28 ítems medidos. Redacción, no sustitución.
# ==========================================================================
CONTRATACION = {
    'anuncia': 24,
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
# checklist-appcc.xlsx — 37 ítems medidos. §3.2 (DOM-14/DOM-15)
# ==========================================================================
APPCC = {
    'anuncia': 33,
    # El único de los tres hermanos verificados con un ítem PARCIAL de
    # anisakis: se sustituye por la redacción completa, con la cita legal
    # correcta (Decisión ANISAKIS-2026-08-29: RD 1021/2022, no el RD
    # 1420/2006 derogado) y la alternativa de -35°C/15h.
    'sustituciones': [
        {'id': 'DOM-14',
         'fuente': 'SPEC §3.2 · RD 1021/2022, art. 8.1 (que derogó el '
                   'RD 1420/2006)',
         'buscar': 'Congelación previa -20°C/24h para ceviche (anisakis)',
         'tarea': ('Congelación preventiva (' + G + '20' + N + '°C durante '
                   'al menos 24' + N + 'h, o ' + G + '35' + N + '°C durante '
                   '15' + N + 'h) para el ceviche y cualquier pescado de '
                   'consumo crudo o marinado — RD 1021/2022, art.' + N
                   + '8.1 (que derogó el RD 1420/2006) y Rgto. (CE) '
                   '853/2004, Anexo III, Secc. VIII, Cap. III.D'),
         'responsable': 'Jefe cocina', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El ítem original citaba «-20°C/24h» sin base normativa y '
                   'sin la alternativa de -35°C/15h. El «Ceviche mexicano de '
                   'lubina» de menu-engineering-matrix.xlsx (fila 12) es '
                   'pescado crudo curado en cítrico: la congelación '
                   'preventiva es obligatoria, no opcional. El binomio legal '
                   'son 24' + N + 'h a ' + G + '20' + N + '°C EN TODO EL '
                   'PRODUCTO; los «5' + N + 'días» que circulan son la '
                   'recomendación para congeladores DOMÉSTICOS, que no '
                   'garantizan esa temperatura. La congelación puede haberla '
                   'hecho el proveedor si está justificado documentalmente '
                   '(art.' + N + '8.1 del RD 1021/2022): guarda ese '
                   'justificante. ' + PRESUPUESTAR)},
    ],
    'nuevas': [
        {'id': 'DOM-14', 'fuente': 'SPEC §3.2', 'categoria': 'Pescado',
         'tarea': 'Registro de lotes congelados preventivamente',
         'responsable': 'Jefe cocina', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Producto, lote, fecha y hora de entrada y salida del '
                   'congelador: lo que acredita el tratamiento ante la '
                   'inspección.')},
        {'id': 'DOM-14', 'fuente': 'SPEC §3.2', 'categoria': 'Pescado',
         'tarea': ('Información al comensal de que el ceviche ha sido '
                   'congelado'),
         'responsable': 'Encargado sala', 'estado': 'Pendiente', 'coste': None,
         'notas': 'En carta y en el discurso de sala (art. 8.2 RD 1021/2022).'},
        # --- baja temperatura y vacío (DOM-15) — familia(8), aunque
        # mexicano no presupuesta roner/envasadora: se deja como buena
        # práctica ligera, no como bloque completo, precisamente porque el
        # propio checklist de equipamiento de esta guía no incluye esos
        # equipos (verificado: las cadenas «roner» y «envasadora» no
        # aparecen en los 35 ítems).
        {'id': 'DOM-15', 'fuente': 'SPEC §3.2 (adaptado: sin roner/envasadora '
                                   'en el equipamiento de esta guía)',
         'categoria': 'Baja temperatura y vacío',
         'tarea': ('Si en algún momento incorporas cocción a baja '
                   'temperatura o envasado al vacío (por ejemplo, para la '
                   'carne de pastor o las carnitas): registro de sonda por '
                   'lote y enfriamiento a ≤10' + N + '°C en menos de '
                   '2' + N + 'h'),
         'responsable': 'Jefe cocina', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El checklist de equipamiento de mexicano NO presupuesta '
                   'roner ni envasadora: esta guía cuece la carne de pastor '
                   'en el trompo y ahúma en el smoker, no al vacío. Se deja '
                   'como aviso condicional en lugar del bloque completo que '
                   'sí lleva el representante (que sí presupuesta ambos '
                   'equipos).')},
    ],
}

# ==========================================================================
# checklist-diseno-sala-mexicana.xlsx — 32 ítems medidos. DOM-39
# ==========================================================================
DISENO_SALA = {
    'anuncia': 30,
    'nuevas': [
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Acústica',
         'tarea': ('Limitador' + G + 'registrador acústico homologado y '
                   'estudio de impacto acústico'),
         'responsable': 'Ingeniero acústico', 'estado': 'Pendiente',
         'coste': None,
         'notas': ('El checklist ya lleva «paneles absorbentes» y «sistema '
                   'de música» (confort acústico) pero no el limitador '
                   'homologado que exige la licencia en buena parte de las '
                   'ordenanzas municipales para locales con música y barra '
                   'de tequilas hasta tarde. ' + PRESUPUESTAR)},
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Accesibilidad',
         'tarea': ('Alumbrado de emergencia y señalización de evacuación '
                   '(CTE DB' + G + 'SUA / DB' + G + 'SI)'),
         'responsable': 'Instalador', 'estado': 'Pendiente', 'coste': None,
         'notas': ('«Señalética interior temática mexicana» ya existía; el '
                   'ALUMBRADO de emergencia (autónomo, con batería) es otra '
                   'instalación y no estaba. ' + PRESUPUESTAR)},
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Personal',
         'tarea': ('Vestuario de personal con taquillas, separado de los '
                   'aseos de clientes (RD 486/1997)'),
         'responsable': 'Arquitecto', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Los aseos del checklist son de clientes (con PMR): no '
                   'hay ninguna línea para el vestuario de los 14 puestos de '
                   'plantilla-turnos-brigada.xlsx. ' + PRESUPUESTAR)},
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Accesibilidad',
         'tarea': ('Certificación de aforo y anchura de los recorridos de '
                   'evacuación'),
         'responsable': 'Arquitecto', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El aforo declarado tiene que cuadrar con las 80 plazas '
                   'del plano (fila 6) y con la terraza adicional (filas '
                   '30-32).')},
    ],
}

# ==========================================================================
# checklist-equipamiento-cocina-mexicana.xlsx — 35 ítems medidos. DOM-20
# ==========================================================================
#: A diferencia del representante, mexicano YA presupuesta el horno mixto
#: (12.000 EUR, fila 16) y una «Salida de humos reglamentaria (sobredimen-
#: sionada)» (4.000 EUR, fila 29): DOM-20 no encuentra el mismo defecto de
#: fondo. Lo que sí falta, verificado fila a fila, es la extinción automática
#: en campana — obligada por el CTE DB-SI y por la aseguradora en cuanto hay
#: freidora (fila 17) y trompo de pastor a gas (fila 8), y que ni el
#: representante ni casual ni mexicano tenían.
EQUIPAMIENTO = {
    'anuncia': 35,
    'notas': [
        {'id': 'DOM-20', 'buscar': 'Campana extractora reforzada + filtros',
         'notas': ('Cubre la campana y el filtrado; la extinción automática '
                   'va en la línea nueva de abajo, que es un sistema '
                   'distinto exigido por el CTE DB' + G + 'SI en cuanto hay '
                   'freidora y trompo de pastor a gas.')},
    ],
    'nuevas': [
        {'id': 'DOM-20', 'fuente': 'SPEC §3.4 (' + _rango('2.500', '4.000')
                                   + N + '€)', 'categoria': 'Extracción',
         'tarea': ('Sistema automático de extinción en campana '
                   '(CTE DB' + G + 'SI y aseguradora)'),
         'responsable': 'Instalador', 'estado': 'Pendiente', 'coste': 2500,
         'notas': ('Rango ' + _rango('2.500', '4.000') + N + '€; precargado '
                   'el mínimo. Con freidora doble (fila 17) y trompo de '
                   'pastor a gas (fila 8) es exigible, y la aseguradora lo '
                   'pide para emitir la póliza. La cadena «extinción» no '
                   'aparecía en ninguna de las 35 filas.')},
    ],
}

# ==========================================================================
# checklist-marketing-preapertura.xlsx — 27 ítems medidos. DOM-40
# ==========================================================================
#: A diferencia del representante y de casual, mexicano YA presupuesta una
#: sesión fotográfica de 400 EUR (fila 17, «platos + decoración + tequilas»):
#: sigue estando por debajo del rango real que fija la SPEC
#: (1.500-3.000 EUR), así que SÍ se sustituye — igual que en casual, sólo que
#: partiendo de una cifra distinta.
MARKETING = {
    'anuncia': 25,
    'sustituciones': [
        {
            'id': 'DOM-40',
            'fuente': 'SPEC §3.4 (' + _rango('1.500', '3.000') + N + '€)',
            'buscar': ('Sesión fotográfica profesional (platos + decoración '
                       '+ tequilas)'),
            'tarea': ('Sesión fotográfica profesional (platos + decoración + '
                      'tequilas) (' + _rango('15', '25') + N + 'platos)'),
            'coste': 1500,
            'notas': ('Rango real ' + _rango('1.500', '3.000') + N + '€ '
                      '(SPEC §3.4). Va precargado el MÍNIMO. Los 400' + N
                      + '€ anteriores ni siquiera llegan a los 500' + N + '€ '
                      'del representante y no compran fotografía '
                      'gastronómica profesional para toda la carta.'),
        },
    ],
    'nuevas': [
        {'id': 'DOM-40', 'fuente': 'parametrizado', 'categoria': 'Digital',
         'tarea': ('Página de reservas propia con seguimiento de origen '
                   '(UTM) y confirmación por email'),
         'responsable': 'Agencia web', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Sin UTM no se sabe qué canal (Google Ads, Instagram Ads, '
                   'TheFork) trae reservas de verdad. ' + PRESUPUESTAR)},
        {'id': 'DOM-40', 'fuente': 'parametrizado', 'categoria': 'Medición',
         'tarea': 'Cuadro de mando: reservas por origen y coste por cliente',
         'responsable': 'Marketing', 'estado': 'Pendiente', 'coste': None,
         'notas': ''},
    ],
}

# ==========================================================================
# Mapa fichero → configuración (lo lee `grupo_b.post`)
# ==========================================================================
CHECKLISTS = {
    'checklist-legal.xlsx': LEGAL,
    'checklist-contratacion.xlsx': CONTRATACION,
    'checklist-appcc.xlsx': APPCC,
    'checklist-diseno-sala-mexicana.xlsx': DISENO_SALA,
    'checklist-equipamiento-cocina-mexicana.xlsx': EQUIPAMIENTO,
    'checklist-marketing-preapertura.xlsx': MARKETING,
}

# ==========================================================================
# cronograma-apertura-gantt.xlsx — molde de 12 meses, rejilla YA marcada
# con 'X' (variante «hermanos»/T2 del Gantt: `_deducir_de_marcas` calcula
# Mes inicio/Duración SOLO. No hace falta ninguna tarea nueva: mexicano YA
# incluye «Negociación alquiler y contrato» (fila 8) y «Plan financiero y
# búsqueda financiación» (fila 6) — los dos huecos que DOM-22/DOM-23
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
