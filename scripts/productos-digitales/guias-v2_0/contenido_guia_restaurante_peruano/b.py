# -*- coding: utf-8 -*-
"""
contenido_guia_restaurante_peruano/b.py — contenido del **grupo B**
(checklists y cronograma, `guias-v2-SPEC.md` §3) para «Cómo Montar un
Restaurante Peruano» (80 plazas, 65 EUR).

Peruano lleva **6** checklists (molde A: legal, contratación, APPCC, diseño
de sala peruana + barra piscos, equipamiento de cocina peruana, marketing
pre-apertura — NO lleva `vajilla-cristalería` ni `inspeccion-michelin-repsol`,
que sólo tiene el representante) más `cronograma-apertura-gantt.xlsx`.

DIFERENCIA CON EL REPRESENTANTE (COM-17/18) — recuentos, medidos, frente al
dashboard `GuiaRestaurantePeruanoDashboard.tsx:41-46`
--------------------------------------------------------------------------
  · checklist-legal.xlsx:       anuncia 32, medido **39** (A5:A43)
  · checklist-equipamiento:     anuncia 35, medido **32** (A5:A36) — POR
    DEBAJO del anuncio: es el ÚNICO de los seis checklists de esta guía, y el
    único caso entre los tres hermanos verificados hasta ahora (casual,
    mexicano), donde el fichero mide MENOS que la tarjeta. Ver EQUIPAMIENTO
    abajo: el gate exige 3 ítems nuevos como mínimo (no 1), para no dejar el
    recuento por debajo del anunciado.
  · checklist-appcc.xlsx:       anuncia 33, medido **39** (A5:A43)
  · checklist-diseno-sala:      anuncia 30, medido **32** (A5:A36)
  · checklist-contratacion.xlsx: anuncia 24, medido **29** (A5:A33)
  · checklist-marketing.xlsx:   anuncia 25, medido **28** (A5:A32)

Los 6 números anunciados (32/35/33/30/24/25) son EXACTAMENTE los mismos que
mexicano y casual anunciaban en sus propios dashboards: el componente de
tarjetas de esta familia se copió entre hermanos sin actualizar la cifra a la
guía concreta (mismo defecto de fondo que COM-17/18 documentó para el
representante, en la dirección de «anuncia menos» en 5 de los 6 checklists y
de «anuncia más» sólo en equipamiento). Se completa el contenido hasta cubrir
lo anunciado (§3.4, §6.5) y **se anota para T8**, que actualizará las 6
cifras del dashboard con el recuento real.

CENSO DE SUSTITUCIONES — verificado abriendo el fichero, no asumido de los
hermanos anteriores
--------------------------------------------------------------------------
  · **No hay «Libro de visitas de la Inspección de Trabajo»** en
    `checklist-legal` (39 filas, categoría «Laboral» con sólo 3 ítems:
    contratos, PRL, calendario laboral — verificado una a una): no hay nada
    que sustituir por DOM-12; el registro de jornada entra como ítem NUEVO.
  · **No hay «Licencia C3»**: el ítem 9 ya dice «Licencia de actividad /
    declaración responsable», sin atribuir el nombre C3 a nada. DOM-11/COM-28
    **no aplica** como sustitución (nada que corregir); se deja constancia.
  · **No hay duplicado de alta censal** (una sola fila, «Alta censal en
    Hacienda (modelo 036/037)», categoría Empresa): RD-32 (dedup del
    representante) no aplica; el ítem de facturación verificable
    (RD 1007/2023) entra como NUEVO, no liberando una fila existente — mismo
    patrón que casual (RD-CASUAL-01) y mexicano (RD-MEX-01), aquí RD-PERU-03.
  · **No hay «Plan de igualdad (si >50 empleados)»** ni «Cláusula de
    confidencialidad y no competencia»: el checklist de contratación de
    peruano (29 ítems) no las tenía. DOM-38 no aplica como sustitución aquí
    (14 puestos, muy lejos del umbral de 50); no se inventa una fila sobre un
    supuesto que esta guía no vende. Se deja una nota de remisión, igual que
    en casual y mexicano.
  · **SÍ hay un ítem PARCIAL de anisakis, más completo que el de mexicano**:
    `checklist-appcc` fila 16, categoría «Pescado crudo», «CONGELACIÓN PREVIA
    obligatoria -20°C/24h (anisakis)», sin cita normativa y sin la
    alternativa de -35°C/15h — pero la fila 17, «Registro de congelación por
    lote de pescado», YA cubre lo que en mexicano hacía falta añadir como
    ítem nuevo. Único de los tres hermanos verificados donde falta apenas UNA
    de las tres piezas que exige §3.2/DOM-14 (registro de lotes YA existe;
    falta la cita legal completa —se SUSTITUYE— y la información al comensal
    —entra como NUEVA—). Justificado porque el propio Matrix de
    menu-engineering de esta guía vende un «Tiradito de lubina al ají
    amarillo» (fila 10) y un «Ceviche clásico de corvina» (fila 5), los dos
    pescado crudo curado en cítrico.

DÓNDE VA CADA OBLIGACIÓN LABORAL NUEVA: igual que el representante, casual y
mexicano, **una sola vez**, en `checklist-legal`, categoría `Laboral` (§3.1,
COM-15): así no se cuenta dos veces en el presupuesto de apertura.

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
# checklist-legal.xlsx — 39 ítems medidos (A5:A43). §3.1 + DOM-23
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
         'notas': ('No estaba en ninguna de las 39 filas del checklist. Es '
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
        {'id': 'RD-PERU-03',
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
         'notas': ('El cronograma de esta misma guía tarda desde el mes 4 '
                   '(obra) hasta el mes 9 (licencias resueltas) en llegar a '
                   'la apertura: sin carencia, son meses de renta antes de '
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
# checklist-contratacion.xlsx — 29 ítems medidos. Redacción, no sustitución.
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
# checklist-appcc.xlsx — 39 ítems medidos. §3.2 (DOM-14/DOM-15)
# ==========================================================================
APPCC = {
    'anuncia': 33,
    # De los tres hermanos verificados, el ítem de anisakis MÁS COMPLETO:
    # sólo falta la cita legal correcta (Decisión ANISAKIS-2026-08-29:
    # RD 1021/2022, no el RD 1420/2006 derogado) y la alternativa de
    # -35°C/15h. El registro de lotes YA existe (fila 17) y no se duplica.
    'sustituciones': [
        {'id': 'DOM-14',
         'fuente': 'SPEC §3.2 · RD 1021/2022, art. 8.1 (que derogó el '
                   'RD 1420/2006)',
         'buscar': 'CONGELACIÓN PREVIA obligatoria -20°C/24h (anisakis)',
         'tarea': ('Congelación preventiva (' + G + '20' + N + '°C durante '
                   'al menos 24' + N + 'h, o ' + G + '35' + N + '°C durante '
                   '15' + N + 'h) para el ceviche, el tiradito y cualquier '
                   'pescado de consumo crudo o marinado — RD 1021/2022, '
                   'art.' + N + '8.1 (que derogó el RD 1420/2006) y Rgto. '
                   '(CE) 853/2004, Anexo III, Secc. VIII, Cap. III.D'),
         'responsable': 'Cevichero', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El ítem original citaba «-20°C/24h» sin base normativa y '
                   'sin la alternativa de -35°C/15h. El «Tiradito de lubina '
                   'al ají amarillo» y el «Ceviche clásico de corvina» de '
                   'menu-engineering-matrix.xlsx (filas 5 y 10) son pescado '
                   'crudo curado en cítrico: la congelación preventiva es '
                   'obligatoria, no opcional. El binomio legal son 24' + N
                   + 'h a ' + G + '20' + N + '°C EN TODO EL PRODUCTO; los '
                   '«5' + N + 'días» que circulan son la recomendación para '
                   'congeladores DOMÉSTICOS, que no garantizan esa '
                   'temperatura. La congelación puede haberla hecho el '
                   'proveedor si está justificado documentalmente '
                   '(art.' + N + '8.1 del RD 1021/2022): guarda ese '
                   'justificante. ' + PRESUPUESTAR)},
    ],
    'nuevas': [
        # El registro de lotes YA existe (fila 17, «Registro de congelación '
        # por lote de pescado»): sólo falta la pieza de información al
        # comensal, que el propio art. 8.2 exige y que ninguna de las 39
        # filas cubre.
        {'id': 'DOM-14', 'fuente': 'SPEC §3.2', 'categoria': 'Pescado crudo',
         'tarea': ('Información al comensal de que el pescado ha sido '
                   'congelado (ceviche, tiradito)'),
         'responsable': 'Encargado sala', 'estado': 'Pendiente', 'coste': None,
         'notas': 'En carta y en el discurso de sala (art. 8.2 RD 1021/2022).'},
        # --- baja temperatura y vacío (DOM-15) — familia(8), aunque
        # peruano no presupuesta roner/envasadora: se deja como buena
        # práctica ligera, no como bloque completo, precisamente porque el
        # propio checklist de equipamiento de esta guía no incluye esos
        # equipos (verificado: las cadenas «roner» y «envasadora» no
        # aparecen en los 32 ítems).
        {'id': 'DOM-15', 'fuente': 'SPEC §3.2 (adaptado: sin roner/envasadora '
                                   'en el equipamiento de esta guía)',
         'categoria': 'Baja temperatura y vacío',
         'tarea': ('Si en algún momento incorporas cocción a baja '
                   'temperatura o envasado al vacío (por ejemplo, para el '
                   'pollo a la brasa o los guisos criollos): registro de '
                   'sonda por lote y enfriamiento a ≤10' + N + '°C en menos '
                   'de 2' + N + 'h'),
         'responsable': 'Jefe cocina', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El checklist de equipamiento de peruano NO presupuesta '
                   'roner ni envasadora: esta guía cuece el pollo a la '
                   'brasa en horno y usa salamandra, no cocina al vacío. Se '
                   'deja como aviso condicional en lugar del bloque completo '
                   'que sí lleva el representante (que sí presupuesta ambos '
                   'equipos).')},
    ],
}

# ==========================================================================
# checklist-diseno-sala-peruana.xlsx — 32 ítems medidos. DOM-39
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
                   'de piscos hasta tarde. ' + PRESUPUESTAR)},
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Accesibilidad',
         'tarea': ('Alumbrado de emergencia y señalización de evacuación '
                   '(CTE DB' + G + 'SUA / DB' + G + 'SI)'),
         'responsable': 'Instalador', 'estado': 'Pendiente', 'coste': None,
         'notas': ('«Señalética interior con identidad peruana» ya existía; '
                   'el ALUMBRADO de emergencia (autónomo, con batería) es '
                   'otra instalación y no estaba. ' + PRESUPUESTAR)},
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Personal',
         'tarea': ('Vestuario de personal con taquillas, separado de los '
                   'aseos de clientes (RD 486/1997)'),
         'responsable': 'Arquitecto', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Los aseos del checklist (fila 6 y 29) son de clientes '
                   '(con PMR): no hay ninguna línea para el vestuario de los '
                   '14 puestos de plantilla-turnos-brigada.xlsx. '
                   + PRESUPUESTAR)},
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Accesibilidad',
         'tarea': ('Certificación de aforo y anchura de los recorridos de '
                   'evacuación'),
         'responsable': 'Arquitecto', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El aforo declarado tiene que cuadrar con las 80 plazas '
                   'del plano (fila 2) y con la terraza adicional (filas '
                   '26-28).')},
    ],
}

# ==========================================================================
# checklist-equipamiento-cocina-peruana.xlsx — 32 ítems medidos. DOM-20
# ==========================================================================
#: A diferencia del representante, peruano YA presupuesta el horno mixto
#: (12.000 EUR, fila 10) y una «Salida de humos reglamentaria
#: (sobredimensionada)» (4.000 EUR, fila 23): DOM-20 no encuentra el mismo
#: defecto de fondo. Lo que sí falta, verificado fila a fila, es la
#: extinción automática en campana — obligada por el CTE DB-SI y por la
#: aseguradora en cuanto hay freidora (fila 11) y parrilla de anticuchos a
#: carbón/gas (fila 3), y que ni el representante ni casual ni mexicano
#: tenían tampoco.
#:
#: ÚNICO checklist de los tres hermanos verificados donde el recuento (32)
#: queda POR DEBAJO del anunciado por el dashboard (35): el gate «recuento >=
#: anunciado» exige aquí, a diferencia de los demás, un MÍNIMO de 3 ítems
#: nuevos, no basta con DOM-20. Las dos filas adicionales no son relleno: la
#: primera es una partida real del propio capítulo de CAPEX del
#: representante que en peruano no tiene línea propia (instalación/puesta en
#: marcha del equipamiento), y la segunda liga el equipamiento con la
#: obligación de trazabilidad de la congelación preventiva de DOM-14/§3.2 —
#: hoy sin ningún instrumento de medición dedicado en las 32 filas.
EQUIPAMIENTO = {
    'anuncia': 35,
    'notas': [
        {'id': 'DOM-20', 'buscar': 'Campana extractora reforzada',
         'notas': ('Cubre la campana y el filtrado; la extinción automática '
                   'va en la línea nueva de abajo, que es un sistema '
                   'distinto exigido por el CTE DB' + G + 'SI en cuanto hay '
                   'freidora y parrilla de anticuchos a carbón/gas.')},
    ],
    'nuevas': [
        {'id': 'DOM-20', 'fuente': 'SPEC §3.4 (' + _rango('2.500', '4.000')
                                   + N + '€)', 'categoria': 'Extracción',
         'tarea': ('Sistema automático de extinción en campana '
                   '(CTE DB' + G + 'SI y aseguradora)'),
         'responsable': 'Instalador', 'estado': 'Pendiente', 'coste': 2500,
         'notas': ('Rango ' + _rango('2.500', '4.000') + N + '€; precargado '
                   'el mínimo. Con freidora doble (fila 11) y parrilla de '
                   'anticuchos a carbón/gas (fila 3) es exigible, y la '
                   'aseguradora lo pide para emitir la póliza. La cadena '
                   '«extinción» no aparecía en ninguna de las 32 filas.')},
        {'id': 'RD-PERU-04',
         'fuente': 'parametrizado (partida del CAPEX del representante sin '
                   'línea propia en esta guía: «instalación, transporte y '
                   'puesta en marcha, 12 %» de calculadora-capex-'
                   'gastronomico.xlsx)',
         'categoria': 'Cocción',
         'tarea': ('Instalación, transporte y puesta en marcha del '
                   'equipamiento de cocina'),
         'responsable': 'Proveedor', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El equipamiento de esta guía (horno mixto, cocina 6 '
                   'fuegos, freidora, cámaras, tren de lavado…) se compra a '
                   'varios proveedores y cada uno cobra transporte e '
                   'instalación aparte: presupuesta un 10-12 % adicional '
                   'sobre el total de equipamiento, como ya hace el '
                   'representante. ' + PRESUPUESTAR)},
        {'id': 'RD-PERU-04',
         'fuente': 'SPEC §3.2 · DOM-14 · RD 1021/2022, art. 8.1',
         'categoria': 'Frío',
         'tarea': ('Sonda/data logger de temperatura dedicado a verificar y '
                   'registrar la congelación preventiva del pescado '
                   '(' + G + '20' + N + '°C / 24' + N + 'h) en la cámara de '
                   'congelación'),
         'responsable': 'Jefe cocina', 'estado': 'Pendiente', 'coste': 300,
         'notas': ('La cámara de congelación (fila 14) ya está presupuestada '
                   'pero ninguna de las 32 filas incluye el instrumento que '
                   'ACREDITA el tratamiento ante la inspección — es el '
                   'mismo registro que exige checklist-appcc.xlsx, fila 17, '
                   'y sin sonda propia se comparte con la de servicio (fila '
                   '9 de ese checklist), lo que no permite un registro '
                   'continuo de 24' + N + 'h.')},
    ],
}

# ==========================================================================
# checklist-marketing-preapertura.xlsx — 28 ítems medidos. DOM-40
# ==========================================================================
#: A diferencia del representante, casual y mexicano, peruano YA presupuesta
#: DOS piezas de contenido separadas por 400 y 500 EUR (fila 13 «Sesión
#: fotográfica profesional» y fila 14 «Vídeo cevichero preparando ceviche»):
#: la de FOTOGRAFÍA sigue estando por debajo del rango real que fija la SPEC
#: (1.500-3.000 EUR), así que SÍ se sustituye — el vídeo (fila 14) es una
#: pieza distinta (contenido para redes, no fotografía de producto para
#: carta/plataformas) y no se toca.
MARKETING = {
    'anuncia': 25,
    'sustituciones': [
        {
            'id': 'DOM-40',
            'fuente': 'SPEC §3.4 (' + _rango('1.500', '3.000') + N + '€)',
            'buscar': ('Sesión fotográfica profesional (ceviches + '
                       'decoración + piscos)'),
            'tarea': ('Sesión fotográfica profesional (ceviches + '
                      'decoración + piscos) (' + _rango('15', '25') + N
                      + 'platos)'),
            'coste': 1500,
            'notas': ('Rango real ' + _rango('1.500', '3.000') + N + '€ '
                      '(SPEC §3.4). Va precargado el MÍNIMO. Los 400' + N
                      + '€ anteriores ni siquiera llegan a los 500' + N + '€ '
                      'del representante y no compran fotografía '
                      'gastronómica profesional para toda la carta.'),
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
    'checklist-diseno-sala-peruana.xlsx': DISENO_SALA,
    'checklist-equipamiento-cocina-peruana.xlsx': EQUIPAMIENTO,
    'checklist-marketing-preapertura.xlsx': MARKETING,
}

# ==========================================================================
# cronograma-apertura-gantt.xlsx — molde de 12 meses, rejilla YA marcada
# con 'X' (variante «hermanos»/T2 del Gantt: `_deducir_de_marcas` calcula
# Mes inicio/Duración SOLO. No hace falta ninguna tarea nueva: peruano YA
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
