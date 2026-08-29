# -*- coding: utf-8 -*-
"""
contenido_guia_restaurante_gastronomico/b.py — contenido del **grupo B**
(checklists y cronograma, `guias-v2-SPEC.md` §3) para la guía
**Cómo Montar un Restaurante Gastronómico (65 plazas, 85 EUR)**.

Aquí sólo hay datos: las filas, los textos, los importes y los parámetros
PROPIOS de esta guía. La mecánica (detección de molde, inserción por categoría,
renumerado, reparación de rangos, barra del Gantt, formato condicional) vive en
`grupo_b.py` y vale para las 8.

FUENTE DE CADA CIFRA — es la regla dura de este paquete
------------------------------------------------------
Cada fila lleva `fuente`, y sólo hay cuatro valores posibles:

  · `SPEC §x`            — el importe está escrito en `guias-v2-SPEC.md`.
  · `R1 <id>`            — el importe lo midió la ronda 1 adversarial citando
                           el fichero o el capítulo del que sale.
  · `fichero original`   — el importe ya estaba en el `.xlsx` y no se toca.
  · `parametrizado`      — **no hay fuente**: la celda de coste se deja VACÍA
                           (que en esta familia significa «sin dato»; nunca `0`,
                           que en una columna de presupuesto se lee «gratis») y
                           la nota dice que hay que pedir presupuesto. La celda
                           es verde y editable: eso ES el parámetro.

No se teclea ni un importe del sector que no venga de una de las tres primeras.
De las 75 filas que se añaden aquí, **5 llevan importe con fuente** (las que la
SPEC §3.4 cifra) y **70 van a presupuestar**: es la diferencia entre completar
un checklist y engordar un total con cifras inventadas.

RECUENTOS QUE HAY QUE ALCANZAR (medidos el 2026-08-29 · anunciados en
`src/pages/GuiaRestauranteGastronomicoDashboard.tsx:42-49`)

    fichero                              medido   anunciado   aquí
    checklist-equipamiento-cocina.xlsx     54        90         +37 → 91
    checklist-appcc.xlsx                   45        55         +10 → 55
    checklist-vajilla-cristaleria.xlsx     43        50          +7 → 50
    checklist-inspeccion-michelin…xlsx     40        45          +5 → 45
    checklist-diseno-sala.xlsx             31        35          +4 → 35
    checklist-marketing-preapertura.xlsx   30        35          +5 → 35
    checklist-legal.xlsx                   40        40          +8 → 48
    checklist-contratacion.xlsx            30        30          +0 → 30

`checklist-legal` sube aunque ya cuadraba: los ocho ítems nuevos son el bloque
«Local» (DOM-23) y el laboral vigente (DOM-12/DOM-38/COM-15), que no son relleno
sino lo que faltaba. `checklist-contratacion` no sube ni una fila: sus dos
defectos son de REDACCIÓN, y añadirle ítems sólo para engordar el número sería
exactamente lo que la SPEC llama relleno.

DÓNDE VA CADA OBLIGACIÓN LABORAL NUEVA (decisión, no descuido)
-------------------------------------------------------------
DOM-38 pide añadir «registro retributivo» y «protocolo de acoso» a
`checklist-contratacion`; §3.1 y COM-15 los piden «en todas las guías» y sitúan
el bloque laboral vigente en `checklist-legal`. Ponerlos en los dos ficheros
haría que el cliente marque dos veces la misma obligación y contaría dos veces
en el presupuesto de apertura. **Van una sola vez, en `checklist-legal`**
(categoría `Laboral`), que es la lista de trámites del producto; en
`checklist-contratacion` se aplican los dos arreglos de redacción de DOM-38 y se
deja constancia con una nota que remite al checklist legal.

⚠️ ESPACIO FINO (U+202F) y GUION NO SEPARABLE (U+2011): se referencian por
escape (`N`, `G`), nunca escribiendo el carácter. Al pasar por un heredoc del
shell degeneran en espacio y guion normales y ninguna sustitución encuentra su
patrón (CLAUDE.md).
"""

N = '\u202f'      # espacio fino (U+202F), SIEMPRE por escape
G = '\u2011'      # guion no separable (U+2011), SIEMPRE por escape

#: Nota estándar de la celda de coste vacía. Lo que evita que un checklist
#: «completo» mienta: 70 de las 75 filas nuevas no tienen precio tasado.
PRESUPUESTAR = ('Sin importe tasado en la guía: pide presupuesto y escríbelo '
                'aquí (la celda es editable y el TOTAL se recalcula).')


def _rango(a, b):
    """`12.000-30.000` con guion no separable, como el resto de la familia."""
    return a + G + b


# ==========================================================================
# checklist-legal.xlsx — 40 ítems medidos (A5:A44). §3.1 + DOM-23
# ==========================================================================
LEGAL = {
    'anuncia': 48,
    'sustituciones': [
        {
            'id': 'DOM-12/COM-15',
            'fuente': 'SPEC §3.1',
            # Fila 37 del fichero (ítem 33, categoría Laboral, responsable
            # «Papelería», 20 €). El libro de visitas está suprimido por la Ley
            # 23/2015 y la Orden ESS/1452/2016: desde entonces el inspector
            # extiende diligencia y no hay libro que comprar ni conservar.
            'buscar': 'Libro de visitas de la Inspección de Trabajo',
            'tarea': ('Registro diario de jornada (RD' + G + 'ley 8/2019, '
                      'art.' + N + '34.9 ET): sistema de fichaje y '
                      'conservación 4 años'),
            'responsable': 'Asesor laboral',
            'coste': None,
            'notas': ('Sustituye al libro de visitas, derogado (Ley 23/2015 y '
                      'Orden ESS/1452/2016). Es de las infracciones más '
                      'sancionadas en hostelería. ' + PRESUPUESTAR),
        },
        {
            # RD-32 · «Alta censal en Hacienda (Modelo 036/037)» (fila 9,
            # Constitución) y «Alta en el censo de empresarios (Modelo 036)»
            # (fila 41, Fiscal) son EL MISMO trámite escrito dos veces, y
            # duplicar un ítem en una lista que el cliente tacha es
            # exactamente el relleno que §3.4 prohíbe. La fila liberada se usa
            # para un trámite fiscal REAL que no estaba: el sistema de
            # facturación verificable, que en hostelería se implanta en el TPV.
            'id': 'RD-32',
            'fuente': 'SPEC §3.4 (sin duplicados) · RD 1007/2023',
            'buscar': 'Alta en el censo de empresarios (Modelo 036)',
            'tarea': ('Sistema informático de facturación verificable en el '
                      'TPV (RD 1007/2023 y su Orden de desarrollo)'),
            'responsable': 'Asesor fiscal + proveedor de TPV',
            'coste': None,
            'notas': ('El alta censal ya está en el bloque «Constitución» '
                      '(Modelo 036/037): estaba dos veces. Aquí va lo que '
                      'faltaba de verdad — que tu TPV emita facturas con los '
                      'registros y la huella que exige la norma. '
                      + PRESUPUESTAR),
        },
        {
            'id': 'DOM-11/COM-28',
            'fuente': 'SPEC §3.1 (redacción única en los cuatro sitios)',
            'buscar': 'Licencia de actividad C3 (restaurante)',
            'tarea': ('Licencia de actividad clasificada de restaurante — la '
                      'clasificación y el nombre dependen de la ordenanza '
                      'municipal y del catálogo autonómico; en algunos '
                      'municipios se denomina C3'),
            'notas': ('No es una categoría nacional: en Cataluña, Andalucía o '
                      'Valencia ese epígrafe no existe. Consulta el catálogo '
                      'de tu CCAA y la ordenanza de tu municipio. Plazo '
                      'orientativo ' + _rango('4', '8') + N + 'meses '
                      '(cap.' + N + '5).'),
        },
    ],
    #: RC-15/RD-33 · el bloque «Local» aportaba 0,00 € al presupuesto y su
    #: partida más cara —la fianza legal del art. 36 LAU— son dos mensualidades
    #: de la renta que el propio pack precarga: 34.000 €, más que el TOTAL
    #: entero del checklist. No se teclea: se calcula desde la renta.
    'costes_formula': [
        {'id': 'RC-15/DOM-23',
         'buscar': 'Fianza legal de 2 mensualidades y garantía adicional',
         'etiqueta': 'Renta mensual del local (€)',
         'valor': 17000,
         'nota': ('Alquiler mensual del escenario realista de '
                  'pl-mensual-escenarios.xlsx (§7-bis.7: una sola cifra por '
                  'magnitud). Escribe el tuyo y la fianza se recalcula.'),
         'formula': '=IF(<param>="","",2*<param>)',
         'notas': ('Dos mensualidades de la renta, que es el mínimo legal del '
                   'art.' + N + '36 LAU para uso distinto de vivienda. La '
                   'garantía adicional (aval o depósito) se negocia aparte y '
                   'suele ser de otras ' + _rango('2', '6') + N + 'mensualidades: '
                   'añádela a mano si tu propiedad la pide.')},
    ],
    'sustituciones_extra': [],
    'notas': [
        {
            'id': 'DOM-23',
            'buscar': 'Informe de compatibilidad urbanística',
            'notas': ('Pídelo ANTES de firmar el arrendamiento: con una '
                      'licencia de ' + _rango('4', '8') + N + 'meses por '
                      'delante, firmar sin esto son meses de renta sobre un '
                      'local que quizá no pueda abrir.'),
        },
    ],
    'nuevas': [
        # --- §3.1: laboral vigente, sin umbral de plantilla ---------------
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
                   'plantilla. ' + PRESUPUESTAR)},
        {'id': 'DOM-38', 'fuente': 'SPEC §3.1', 'categoria': 'Laboral',
         'tarea': ('Protocolo de prevención del acoso sexual '
                   '(LO 3/2007 art.' + N + '48)'),
         'responsable': 'Abogado / SPA', 'estado': 'Pendiente', 'coste': None,
         'notas': ('También sin umbral de plantilla. Va acompañado de '
                   'formación al equipo. ' + PRESUPUESTAR)},
        # --- §3.1 / DOM-23: el bloque «Local», que no existía -------------
        {'id': 'DOM-23', 'fuente': 'SPEC §3.1', 'categoria': 'Local',
         'tarea': ('Contrato de arrendamiento para uso distinto de vivienda '
                   '(duración, prórrogas, renta y actualización)'),
         'responsable': 'Abogado', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Las cadenas «arrendamiento», «fianza», «traspaso» y '
                   '«carencia» no aparecían en ninguno de los 22 entregables. '
                   'Es el documento más caro de negociar de la apertura. '
                   + PRESUPUESTAR)},
        {'id': 'DOM-23', 'fuente': 'SPEC §3.1', 'categoria': 'Local',
         'tarea': ('Fianza legal de 2 mensualidades y garantía adicional '
                   '(aval o depósito)'),
         'responsable': 'Propiedad', 'estado': 'Pendiente', 'coste': None,
         'notas': ('La fianza legal de 2 mensualidades la fija el '
                   'art.' + N + '36 LAU para uso distinto de vivienda; la '
                   'garantía adicional se negocia. Escribe aquí el importe de '
                   'TU renta.')},
        {'id': 'DOM-23', 'fuente': 'SPEC §3.1', 'categoria': 'Local',
         'tarea': ('Carencia de renta durante la obra y la tramitación de la '
                   'licencia, pactada por escrito'),
         'responsable': 'Abogado', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Con licencia de ' + _rango('4', '8') + N + 'meses y obra '
                   'por delante son ' + _rango('6', '10') + N + 'meses de '
                   'renta antes de facturar un euro. Es la cláusula que más '
                   'dinero ahorra de toda la lista.')},
        {'id': 'DOM-23', 'fuente': 'SPEC §3.1', 'categoria': 'Local',
         'tarea': 'Cláusula de cesión y traspaso pactada expresamente',
         'responsable': 'Abogado', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Sin ella, vender el negocio depende del criterio de la '
                   'propiedad.')},
        {'id': 'RD-28', 'fuente': 'parametrizado (ordenanza municipal)',
         'categoria': 'Licencias',
         'tarea': ('Arqueta separadora de grasas y autorización o declaración '
                   'de vertido a la red de saneamiento'),
         'responsable': 'Arquitecto / instalador', 'estado': 'Pendiente',
         'coste': None,
         'notas': ('Las cadenas «grasa», «separador» y «vertido» no aparecían '
                   'en ninguno de los 18 entregables, y este pack presupuesta '
                   'freidora de doble cuba, parrilla de brasa y fregadero de '
                   'doble seno. La mayoría de ordenanzas municipales lo exigen '
                   'para conceder la licencia de actividad, y su ausencia es '
                   'causa clásica de acta desfavorable. Va en obra: pídelo en '
                   'el proyecto técnico. ' + PRESUPUESTAR)},
        {'id': 'DOM-23', 'fuente': 'SPEC §3.1', 'categoria': 'Local',
         'tarea': ('Condición suspensiva por denegación de la licencia de '
                   'actividad'),
         'responsable': 'Abogado', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Si el ayuntamiento deniega la licencia, el contrato decae '
                   'y recuperas la fianza. Es la contrapartida de firmar '
                   'antes de tenerla.')},
    ],
}

# ==========================================================================
# checklist-contratacion.xlsx — 30 ítems medidos. DOM-38 (sólo redacción)
# ==========================================================================
CONTRATACION = {
    'anuncia': 30,
    'notas': [
        {
            'id': 'DOM-12/COM-15',
            # La fila 33 («Registro de jornada digital») y la fila nueva del
            # checklist legal («Registro diario de jornada… conservación 4
            # años») son la MISMA obligación vista desde dos sitios: aquí, el
            # sistema que se implanta; allí, el trámite y la conservación. La
            # nota lo dice para que no se lea como dos tareas distintas ni se
            # presupueste dos veces.
            'buscar': 'Registro de jornada digital (obligatorio)',
            'notas': ('Es la implantación del sistema de fichaje. La '
                      'obligación y la conservación 4 años están en el '
                      'checklist legal, categoría Laboral: son la misma cosa, '
                      'no dos gastos.'),
        },
    ],
    'sustituciones': [
        {
            'id': 'DOM-38',
            'fuente': 'SPEC §3.1',
            # Fila 34 del fichero (ítem 30). El «>50» deja fuera justo a la
            # empresa de 50, que sí está obligada desde marzo de 2022.
            'buscar': 'Plan de igualdad (si >50 empleados)',
            'tarea': ('Plan de igualdad (50 o más personas trabajadoras)'),
            'notas': ('El umbral es «50 o más», no «más de 50»: escrito con '
                      '«>50» dejaba fuera justo a la empresa de 50.'),
        },
        {
            'id': 'DOM-38',
            'fuente': 'SPEC §3.1',
            # Fila 20 del fichero (ítem 16). Sin compensación económica el
            # pacto es NULO y el cliente cree tener una protección que no
            # tiene.
            'buscar': 'Cláusula de confidencialidad y no competencia (chef)',
            'tarea': ('Pacto de no competencia postcontractual CON '
                      'compensación económica pactada (art.' + N + '21.2 ET; '
                      'máx.' + N + '2 años para técnicos)'),
            'responsable': 'Abogado',
            'notas': ('Sin compensación económica adecuada el pacto es NULO. '
                      'La confidencialidad durante el contrato es otra cosa y '
                      'sí se puede pactar sin compensación. Registro '
                      'retributivo y protocolo de acoso están en el checklist '
                      'legal, categoría Laboral.'),
        },
    ],
}

# ==========================================================================
# checklist-appcc.xlsx — 45 ítems medidos, 55 anunciados. §3.2 (DOM-14/15)
# ==========================================================================
APPCC = {
    'anuncia': 55,
    'nuevas': [
        # --- anisakis (DOM-14): la cadena no aparecía en ninguno de los 141 --
        {'id': 'DOM-14', 'fuente': 'SPEC §3.2 · RD 1420/2006',
         'categoria': 'Temperaturas',
         'tarea': ('Congelación preventiva (' + G + '20' + N + '°C durante al '
                   'menos 24' + N + 'h en todo el producto, o ' + G + '35' + N
                   + '°C durante 15' + N + 'h) para pescado de consumo en crudo, '
                   'marinado, escabechado o en salazón — RD 1420/2006 y '
                   'Reg. (CE) 853/2004'),
         'responsable': 'Chef', 'estado': 'Pendiente', 'coste': None,
         'equivale_a': ('Congelación preventiva anisakis',
                        'Protocolo de congelación preventiva anisakis'),
         'notas': ('El cap.' + N + '8 sitúa ceviches y tartares en el cuarto '
                   'frío y el cap.' + N + '22 promociona los crudos: esto es '
                   'obligatorio, no opcional. El binomio legal son 24' + N + 'h '
                   'a ' + G + '20' + N + '°C EN TODO EL PRODUCTO (RD 1420/2006 y '
                   'anexo III, secc.' + N + 'VIII, cap.' + N + 'III del '
                   'Reg. (CE) 853/2004); los «5' + N + 'días» son la '
                   'recomendación de AESAN para congeladores DOMÉSTICOS, que no '
                   'garantizan esa temperatura. Si tu abatidor no la certifica, '
                   'usa un margen mayor y dilo por escrito como margen propio, '
                   'no como requisito legal. ' + PRESUPUESTAR)},
        {'id': 'DOM-14', 'fuente': 'SPEC §3.2', 'categoria': 'Temperaturas',
         'tarea': 'Registro de lotes congelados preventivamente',
         'responsable': 'Resp. APPCC', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Producto, lote, fecha y hora de entrada y salida del '
                   'congelador. Es lo que acredita el tratamiento ante la '
                   'inspección.')},
        {'id': 'DOM-14', 'fuente': 'SPEC §3.2', 'categoria': 'Temperaturas',
         'tarea': ('Información al consumidor de que el pescado ha sido '
                   'congelado'),
         'responsable': 'Maître', 'estado': 'Pendiente', 'coste': None,
         'notas': 'En carta, en el menú degustación y en el discurso de sala.'},
        {'id': 'DOM-14', 'fuente': 'parametrizado (buena práctica de APPCC)',
         'categoria': 'Temperaturas',
         'tarea': ('Verificación anual de la calibración de termómetros y '
                   'sondas, con certificado'),
         'responsable': 'Resp. APPCC', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El checklist ya pedía termómetros calibrados, pero no el '
                   'certificado que lo demuestra. ' + PRESUPUESTAR)},
        # --- baja temperatura y vacío (DOM-15): el proceso de más riesgo ---
        {'id': 'DOM-15', 'fuente': 'SPEC §3.2',
         'categoria': 'Baja temperatura y vacío',
         'tarea': ('Tabla de binomios tiempo' + G + 'temperatura validados por '
                   'producto'),
         'responsable': 'Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El checklist de equipamiento presupuesta envasadora '
                   '(2.500' + N + '€) y roner (1.500' + N + '€) y el bloque '
                   'PCC no tenía un solo binomio. Es lo primero que pide un '
                   'inspector en una cocina con roner.')},
        {'id': 'DOM-15', 'fuente': 'SPEC §3.2',
         'categoria': 'Baja temperatura y vacío',
         'tarea': ('Registro de sonda por lote en cada cocción a baja '
                   'temperatura'),
         'responsable': 'Jefes partida', 'estado': 'Pendiente', 'coste': None,
         'notas': 'Temperatura en el corazón del producto, no la del baño.'},
        {'id': 'DOM-15', 'fuente': 'SPEC §3.2',
         'categoria': 'Baja temperatura y vacío',
         'tarea': ('Enfriamiento a ≤10' + N + '°C en menos de 2' + N + 'h tras '
                   'cocción prolongada'),
         'responsable': 'Sous Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Con el abatidor que ya está presupuestado; el registro es '
                   'lo que falta.')},
        {'id': 'DOM-15', 'fuente': 'SPEC §3.2',
         'categoria': 'Baja temperatura y vacío',
         'tarea': ('Etiquetado del envasado al vacío con vida útil '
                   'justificada'),
         'responsable': 'Resp. APPCC', 'estado': 'Pendiente', 'coste': None,
         'notas': ('«Justificada» quiere decir con el estudio o la referencia '
                   'que sostiene la fecha, no una fecha a ojo.')},
        {'id': 'DOM-15', 'fuente': 'SPEC §3.2',
         'categoria': 'Baja temperatura y vacío',
         'tarea': ('Validación documental del proceso de cocción a baja '
                   'temperatura y vacío'),
         'responsable': 'Consultor APPCC', 'estado': 'Pendiente',
         'coste': None, 'notas': PRESUPUESTAR},
        {'id': 'DOM-14', 'fuente': 'parametrizado (buena práctica de APPCC)',
         'categoria': 'Trazabilidad',
         'tarea': ('Registro de descongelación controlada (producto, lote, '
                   'fecha y responsable)'),
         'responsable': 'Resp. APPCC', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Cierra el círculo del registro de congelación preventiva: '
                   'sin él no se puede trazar qué lote se sirvió crudo.')},
    ],
}

# ==========================================================================
# checklist-diseno-sala.xlsx — 31 medidos, 35 anunciados. DOM-39
# ==========================================================================
DISENO_SALA = {
    'anuncia': 35,
    'nuevas': [
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Acústica',
         'tarea': ('Limitador' + G + 'registrador acústico homologado y '
                   'estudio de impacto acústico'),
         'responsable': 'Ingeniero acústico', 'estado': 'Pendiente',
         'coste': None,
         'notas': ('La cadena «limitador» no aparecía en ninguno de los 141 '
                   'ficheros de la familia. En Cataluña el estudio es '
                   'obligatorio y en buena parte de las ordenanzas del resto '
                   'de CCAA también, para locales con música. Condiciona la '
                   'licencia. ' + PRESUPUESTAR)},
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Accesibilidad',
         'tarea': ('Alumbrado de emergencia y señalización de evacuación '
                   '(CTE DB' + G + 'SUA / DB' + G + 'SI)'),
         'responsable': 'Instalador', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Baños',
         'tarea': ('Aseos y vestuarios de personal separados de los de '
                   'clientes (RD 486/1997)'),
         'responsable': 'Arquitecto', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El checklist cubría los baños de clientes y el adaptado, '
                   'pero no los del equipo: son ' + _rango('22', '30')
                   + N + 'personas según el cap.' + N + '13. ' + PRESUPUESTAR)},
        {'id': 'DOM-39', 'fuente': 'SPEC §3.4', 'categoria': 'Accesibilidad',
         'tarea': ('Certificación de aforo y anchura de los recorridos de '
                   'evacuación'),
         'responsable': 'Arquitecto', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El aforo declarado tiene que cuadrar con las 65 plazas '
                   'del plano (fila 1) y con el cartel de aforo del checklist '
                   'legal.')},
    ],
}

# ==========================================================================
# checklist-vajilla-cristaleria.xlsx — 43 medidos, 50 anunciados. DOM-21
# ==========================================================================
#: DOM-21 — NO se redimensiona la dotación de carta (§7.1: es correcta para su
#: supuesto). Se añade una segunda columna con la regla explícita
#: `piezas = plazas × factor por comensal × rotación de lavado`.
#:
#: Los factores precargados son sólo los que se pueden ATAR a un número que ya
#: dice el producto: las copas al maridaje de 5-7 vinos (R1 DOM-21) y los
#: platos a los 8-12 pases del menú largo (cap. 15). El resto —cubertería,
#: mantelería, petit menage— se deja en blanco: no hay dato del que colgarlo y
#: la columna calculada devuelve `""`, no un `0` que se leería como «no
#: necesitas ninguna».
VAJILLA = {
    'anuncia': 50,
    'columna_calculada': {
        'cabecera_entrada': 'Factor por comensal (menú degustación)',
        'cabecera_calculada': 'Menú degustación (uds)',
        'parametros': [
            {'etiqueta': 'Plazas de sala', 'valor': 65, 'formato': '#,##0',
             'nota': ('65 plazas — es el supuesto del propio producto (título '
                      'del pack y checklist-diseno-sala fila 1: «Plano de '
                      'sala con 65 plazas»).')},
            {'etiqueta': 'Rotación de lavado (veces por servicio)',
             'valor': 1.5, 'formato': '#,##0.0',
             'nota': ('1,5 — la regla de dotación del §3.4 de la SPEC: '
                      'piezas = plazas × factor por comensal × rotación. Con '
                      '1,0 no hay margen para lavar entre pases.')},
        ],
        #: Suman 10, que es el número de pases del menú largo (cap. 15: 8-12).
        #: Si tu menú tiene 8 o 12 pases, ajusta estos factores.
        'precarga': {
            'Plato llano principal (×100)': 2,
            'Plato hondo / sopero (×80)': 1,
            'Plato postre (×80)': 1,
            'Platos presentación / show plate (×70)': 1,
            'Boles variados para entrantes (×60)': 3,
            'Pizarras / bandejas presentación (×20)': 1,
            'Vajilla petit fours / mignardises (×70)': 1,
            # Copas: 2+2+1+1 = 6 copas de vino por comensal, el centro del
            # rango 5-7 que mide el R1 (DOM-21) para un maridaje completo.
            'Copa vino tinto Burgundy (×80)': 2,
            'Copa vino tinto Bordeaux (×80)': 2,
            'Copa vino blanco (×80)': 1,
            'Copa champán / espumoso (×60)': 1,
            # RD-16 · la columna estaba rellena en 11 de 50 filas y el bloque
            # de CUBERTERÍA entero iba vacío, que es justo donde el menú de
            # 8-12 pases exige el cálculo: cada pase se come una pieza y no
            # se lava entre medias.
            'Plato pan (×80)': 1,
            'Vaso de agua (×80)': 1,
            'Copa de cóctel / aperitivo (×40)': 1,
            'Copa de postre / licor (×40)': 1,
            'Copa de vino generoso / jerez (×40)': 1,
            # Cubertería: un menú largo cambia cubierto en cada pase. 10 pases
            # = 10 piezas por comensal repartidas por tipo, que es el mismo
            # reparto que suman los platos de arriba.
            'Cuchillo mesa principal (×80)': 2,
            'Tenedor mesa principal (×80)': 2,
            'Cuchara sopera (×80)': 1,
            'Pala pescado (×80)': 2,
            'Tenedor postre (×80)': 1,
            'Cuchara postre (×80)': 1,
            'Cuchillo mantequilla (×80)': 1,
            'Cucharilla café / infusión (×80)': 1,
            'Cuchara de degustación / amuse-bouche (×100)': 2,
            'Cubertería de crudos y tartar (tenedor y cucharilla pequeños, ×80)': 1,
            # Petit menage y mantelería: por comensal, no por pase.
            'Servilletas tela (×120)': 2,
            'Manteles individuales o de mesa (×40)': 1,
        },
        # RD-17 · la dotación calculada no tocaba el dinero: el cliente leía
        # que necesita 585 copas donde el presupuesto compra 300 y seguía
        # llevando al banco el importe de la dotación de carta.
        'cabecera_dotacion': 'Dotación de carta (uds)',
        'cabecera_coste': 'Coste ajustado a menú degustación (€)',
    },
    'nuevas': [
        {'id': 'DOM-21', 'fuente': 'parametrizado (dotación de degustación)',
         'categoria': 'Cristalería',
         'tarea': 'Copa de cata ISO para sommelier y formación (×12)',
         'responsable': 'Sommelier', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'DOM-21', 'fuente': 'parametrizado (dotación de degustación)',
         'categoria': 'Cristalería',
         'tarea': 'Copa de vino generoso / jerez (×40)',
         'responsable': 'Sommelier', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Un maridaje largo abre y cierra con generosos: sin copa '
                   'propia se sirven en la de blanco. ' + PRESUPUESTAR)},
        {'id': 'DOM-21', 'fuente': 'parametrizado (dotación de degustación)',
         'categoria': 'Cristalería',
         'tarea': 'Cubiteras y soportes de pie para espumosos (×6)',
         'responsable': 'Sommelier', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'DOM-21', 'fuente': 'parametrizado (dotación de degustación)',
         'categoria': 'Cubertería',
         'tarea': 'Cuchara de degustación / amuse-bouche (×100)',
         'responsable': 'Maître', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Un menú de ' + _rango('8', '12') + N + 'pases empieza con '
                   'snacks: es la pieza que más rota. ' + PRESUPUESTAR)},
        {'id': 'DOM-21', 'fuente': 'parametrizado (dotación de degustación)',
         'categoria': 'Cubertería',
         'tarea': ('Cubertería de crudos y tartar (tenedor y cucharilla '
                   'pequeños, ×80)'),
         'responsable': 'Maître', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'DOM-21', 'fuente': 'parametrizado (dotación de degustación)',
         'categoria': 'Mantelería',
         'tarea': 'Paños de lino para abrillantado de copas (×40)',
         'responsable': 'Maître', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Con ' + _rango('300', '600') + N + 'copas por servicio, el '
                   'abrillantado es una tarea de brigada, no un detalle. '
                   + PRESUPUESTAR)},
        {'id': 'DOM-21', 'fuente': 'parametrizado (dotación de degustación)',
         'categoria': 'Reposición',
         'tarea': 'Cajas y fundas de almacenaje y transporte de cristalería (×10)',
         'responsable': 'Sommelier', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
    ],
}

# ==========================================================================
# checklist-inspeccion-michelin-repsol.xlsx — 40 medidos, 45 anunciados
# COM-34 (separar «Reputación») + DOM-36 (Estrella Verde)
# ==========================================================================
MICHELIN = {
    'anuncia': 45,
    #: COM-34 — no se borra la categoría (son acciones legítimas de prensa):
    #: se rotula para que deje de sugerir, por vecindad con ítems de estrella,
    #: lo que el propio cap. 17 niega («inspectores anónimos que evalúan
    #: exclusivamente lo que hay en el plato»).
    'renombrar_categoria': {
        'Reputación': 'Prensa y notoriedad (NO influye en la inspección)',
    },
    #: RD-31 · «Mínimo 18-24 meses de operación consistente antes de aspirar»
    #: colgaba del bloque «Prensa y notoriedad (NO influye en la inspección)»,
    #: que le dice al cliente exactamente lo contrario de lo que el ítem
    #: significa: los meses de servicio consistente SÍ condicionan cuándo tiene
    #: sentido aspirar. Se mueve a su propio bloque de requisitos previos.
    'sustituciones': [
        {'id': 'RD-31', 'fuente': 'SPEC §3.4 (clasificación correcta)',
         'buscar': 'Mínimo 18-24 meses de operación consistente antes de aspirar',
         'tarea': ('Mínimo ' + _rango('18', '24') + N + 'meses de operación '
                   'consistente antes de aspirar'),
         'categoria': 'Requisitos previos',
         'notas': ('Esto SÍ cuenta: no es comunicación. Los inspectores '
                   'necesitan varias visitas en fechas distintas para juzgar '
                   'la regularidad, y ése es el reloj que manda. Estaba '
                   'clasificado en «Prensa y notoriedad», donde el propio '
                   'rótulo dice que no influye.')},
    ],
    'notas': [
        {'id': 'COM-34',
         'buscar': 'Invitaciones estratégicas a críticos y periodistas',
         'notas': ('NO aplica a los inspectores: son anónimos y pagan su '
                   'cuenta (cap.' + N + '17). Esto es prensa, no estrella.')},
    ],
    'nuevas': [
        {'id': 'DOM-36', 'fuente': 'SPEC §3.4', 'categoria': 'Estrella Verde',
         'tarea': ('Política de sostenibilidad escrita y comunicada al '
                   'comensal'),
         'responsable': 'Gerente', 'estado': 'Pendiente', 'coste': None,
         'notas': ('La Estrella Verde se evalúa aparte de la estrella '
                   'gastronómica y tiene sus propios criterios.')},
        {'id': 'DOM-36', 'fuente': 'SPEC §3.4', 'categoria': 'Estrella Verde',
         'tarea': ('Medición del desperdicio alimentario y de la gestión de '
                   'residuos (kg/mes)'),
         'responsable': 'Sous Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Medido, no declarado: sin cifra mensual no hay nada que '
                   'enseñar.')},
        {'id': 'DOM-36', 'fuente': 'SPEC §3.4', 'categoria': 'Estrella Verde',
         'tarea': ('Proveedores de proximidad y de temporada documentados '
                   '(km y trazabilidad)'),
         'responsable': 'Resp. compras', 'estado': 'Pendiente', 'coste': None,
         'notas': ''},
        {'id': 'DOM-36', 'fuente': 'SPEC §3.4', 'categoria': 'Estrella Verde',
         'tarea': ('Consumo de energía y agua medido, con medidas de '
                   'eficiencia aplicadas'),
         'responsable': 'Gerente', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'DOM-36', 'fuente': 'SPEC §3.4', 'categoria': 'Estrella Verde',
         'tarea': ('Equipo formado en las prácticas sostenibles y condiciones '
                   'laborales documentadas'),
         'responsable': 'Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El apartado de sostenibilidad de las guías incluye a las '
                   'personas, no sólo al producto.')},
    ],
}

# ==========================================================================
# checklist-marketing-preapertura.xlsx — 30 medidos, 35 anunciados
# DOM-35 (fuera Resy) + DOM-40 (sesión de fotos a precio real)
# ==========================================================================
MARKETING = {
    'anuncia': 35,
    'sustituciones': [
        {
            'id': 'DOM-40',
            'fuente': 'SPEC §3.4 (1.500' + G + '3.000' + N + '€)',
            'buscar': 'Sesión de fotos profesional de platos (15-25 platos)',
            'tarea': ('Sesión de fotos profesional de platos '
                      '(' + _rango('15', '25') + N + 'platos)'),
            'coste': 1500,
            'notas': ('Rango real ' + _rango('1.500', '3.000') + N + '€ '
                      '(SPEC §3.4). Va precargado el MÍNIMO: ajústalo con '
                      'presupuesto. Los 500' + N + '€ anteriores no compraban '
                      'fotografía gastronómica profesional y contradecían el '
                      'propio rango de lanzamiento de '
                      + _rango('5.000', '30.000') + N + '€ del libro.'),
        },
        {
            'id': 'DOM-35',
            'fuente': 'SPEC §3.4',
            'buscar': 'Sistema de reservas configurado (Tock/Resy/TheFork)',
            'tarea': ('Sistema de reservas configurado (Tock, TheFork, Cover '
                      'Manager o Restoo)'),
            'notas': ('Resy fuera: no opera en España y era la única cifra en '
                      'dólares de todo el producto '
                      '(' + _rango('300', '500') + N + 'USD/mes). Las cuatro '
                      'alternativas sí están disponibles aquí y facturan en '
                      'euros.'),
        },
    ],
    'nuevas': [
        {'id': 'DOM-40', 'fuente': 'parametrizado', 'categoria': 'Digital',
         'tarea': ('Sesión de fotos del equipo, la sala y la cocina (no sólo '
                   'platos)'),
         'responsable': 'Fotógrafo', 'estado': 'Pendiente', 'coste': None,
         'notas': ('La prensa gastronómica pide retrato de chef y de sala; '
                   'sin ellas la nota de prensa sale sin foto. '
                   + PRESUPUESTAR)},
        {'id': 'DOM-40', 'fuente': 'parametrizado', 'categoria': 'Digital',
         'tarea': ('Página de reservas propia con seguimiento de origen (UTM) '
                   'y confirmación por email'),
         'responsable': 'Agencia web', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Sin UTM no se sabe qué canal trae reservas y todo el '
                   'presupuesto de lanzamiento se gasta a ciegas.')},
        {'id': 'DOM-40', 'fuente': 'parametrizado', 'categoria': 'PR/Prensa',
         'tarea': ('Dossier de prensa y kit de imágenes en alta resolución '
                   'descargable'),
         'responsable': 'Agencia PR', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'DOM-40', 'fuente': 'parametrizado', 'categoria': 'Medición',
         'tarea': ('Presupuesto de lanzamiento repartido por canal y por mes'),
         'responsable': 'Marketing', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El libro maneja un rango de lanzamiento de '
                   + _rango('5.000', '30.000') + N + '€: repártelo antes de '
                   'gastarlo.')},
        {'id': 'DOM-40', 'fuente': 'parametrizado', 'categoria': 'Medición',
         'tarea': ('Cuadro de mando: reservas por origen y coste de captación '
                   'por cliente'),
         'responsable': 'Marketing', 'estado': 'Pendiente', 'coste': None,
         'notas': ''},
    ],
}

# ==========================================================================
# checklist-equipamiento-cocina.xlsx — 54 medidos, 90 anunciados
# DOM-20 (horno mixto, extracción, extinción, instalación) · DOM-33 · DOM-34
# COM-17 (déficit del 40 %, la mayor desviación del pack) · COM-23
# ==========================================================================
EQUIPAMIENTO = {
    'anuncia': 90,
    #: DOM-20 — «Instalación, transporte y puesta en marcha» como PORCENTAJE
    #: calculado sobre el resto de las partidas. Un importe fijo aquí sería una
    #: cifra inventada; un porcentaje en celda es un parámetro que el cliente
    #: negocia con su instalador y que se recalcula solo cuando cambia el
    #: equipamiento.
    'fila_porcentual': {
        'tarea': ('Instalación, transporte y puesta en marcha (% sobre el '
                  'equipamiento)'),
        'etiqueta': 'Instalación, transporte y puesta en marcha (%)',
        'valor': 0.12,
        # RD-19 · el 12 % se aplicaba también sobre las tres líneas que YA son
        # obra e instalación (conducto hasta cubierta, aportación de aire,
        # extinción en campana: 17.500 €) y sobre el bloque de Tecnología
        # (9.900 €), que instala otro proveedor: 2.100 € de instalación sobre
        # la instalación.
        'excluir_categorias': ('Extracción e instalaciones', 'Tecnología'),
        'nota': ('12' + N + '% sobre la suma del resto de partidas de este '
                 'checklist (SPEC §3.4). Es lo que cuesta subir, colocar, '
                 'conexionar y poner en marcha la maquinaria, y no estaba '
                 'presupuestado en ninguna línea. NO se aplica sobre las '
                 'categorías «Extracción e instalaciones» ni «Tecnología»: la '
                 'primera YA es obra e instalación y la segunda la monta otro '
                 'proveedor. Cámbialo y el importe se recalcula.'),
    },
    #: RD-18/RC-23 · dos parejas de líneas MUTUAMENTE EXCLUYENTES entraban las
    #: dos en el mismo sumatorio: en cuanto el cliente tase la alternativa, el
    #: TOTAL presupuesta las dos opciones a la vez. Estas dos van a «No» por
    #: defecto (la opción estándar es la que ya está tasada); cambiar el
    #: desplegable cambia el TOTAL y los subtotales.
    'alternativas': (
        'Túnel de lavado',
        'Bloque modular de cocción de alta gama',
    ),
    'notas': [
        {'id': 'DOM-20', 'buscar': 'Campana extractora industrial',
         'notas': ('Esto es SÓLO la campana. El sistema completo hasta '
                   'cubierta —conducto, ventilador, silenciador y aportación '
                   'de aire— va en las líneas nuevas del bloque «Extracción e '
                   'instalaciones»: el cap.' + N + '5 lo llama «obstáculo '
                   'técnico número 1» y estaba presupuestado en '
                   '2.500' + N + '€ en total.')},
        {'id': 'DOM-33', 'buscar': 'Lavavajillas de capota 50×50',
         'notas': ('Elige UNA de las dos: capota o túnel de lavado (línea '
                   'nueva del bloque Plonge/Lavado). Con menú degustación y '
                   'maridaje —' + _rango('300', '600') + N + 'copas por '
                   'servicio— la capota no da abasto. Si eliges el túnel, pon '
                   'esta línea a 0.')},
        {'id': 'DOM-34', 'buscar': 'Cocina industrial 6 fuegos + horno',
         'notas': ('Escalón de gama PROFESIONAL ESTÁNDAR. El bloque modular '
                   'de alta gama es la línea nueva de esta misma categoría: '
                   'en un gastronómico que aspira a estrella son dos '
                   'decisiones distintas, no la misma partida.')},
    ],
    'nuevas': [
        # ---- Cuarto Frío -------------------------------------------------
        {'id': 'COM-23', 'fuente': 'parametrizado (cap.' + N + '9 lo nombra)',
         'categoria': 'Cuarto Frío',
         'tarea': 'Robot térmico tipo Thermomix', 'responsable': 'Chef',
         'estado': 'Pendiente', 'coste': None,
         'notas': ('La tarjeta del cap.' + N + '9 lo nombra como gancho y no '
                   'aparecía en ninguno de los 141 ficheros de la familia. '
                   + PRESUPUESTAR)},
        {'id': 'COM-17', 'fuente': 'parametrizado', 'categoria': 'Cuarto Frío',
         'tarea': 'Deshidratadora profesional de bandejas',
         'responsable': 'Jefe Partida', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'COM-17', 'fuente': 'parametrizado', 'categoria': 'Cuarto Frío',
         'tarea': ('Sifones de 1' + N + 'L y cargas de N₂O (set)'),
         'responsable': 'Jefe Partida', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'COM-17', 'fuente': 'parametrizado', 'categoria': 'Cuarto Frío',
         'tarea': 'Termoselladora de barquetas para mise en place',
         'responsable': 'Sous Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'COM-17', 'fuente': 'parametrizado', 'categoria': 'Cuarto Frío',
         'tarea': 'Armario de maduración y curado controlado',
         'responsable': 'Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        # ---- Partida Carnes ----------------------------------------------
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Partida Carnes',
         'tarea': 'Ahumador en frío / pistola de humo con virutas',
         'responsable': 'Jefe Partida', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Partida Carnes',
         'tarea': ('Cuchillería profesional y estación de afilado (piedras y '
                   'chaira)'),
         'responsable': 'Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Partida Carnes',
         'tarea': 'Rebanadora de producto congelado para tataki y carpaccios',
         'responsable': 'Jefe Partida', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        # ---- Partida Pescados --------------------------------------------
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Partida Pescados',
         'tarea': 'Máquina de hielo en escamas y cuba de conservación',
         'responsable': 'Sous Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Partida Pescados',
         'tarea': 'Expositor de pescado sobre hielo para mise en place',
         'responsable': 'Jefe Partida', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'DOM-14', 'fuente': 'SPEC §3.2 · RD 1420/2006',
         'categoria': 'Partida Pescados',
         'tarea': ('Verificar que el abatidor alcanza ' + G + '20' + N + '°C / '
                   + G + '35' + N + '°C para la congelación preventiva de '
                   'anisakis'),
         'responsable': 'Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': ('No todos los abatidores llegan. Si el tuyo no baja de '
                   + G + '20' + N + '°C, necesitas un congelador de choque: '
                   'sin él no puedes servir crudos ni marinados. Va unido al '
                   'bloque de anisakis del checklist APPCC.')},
        # ---- Cocina Caliente ---------------------------------------------
        {'id': 'DOM-20', 'fuente': 'SPEC §3.4 · R1 DOM-20 (docx tabla 1: '
                                   '«Horno racional combi 10 GN | Rational '
                                   'iCombi Pro | 17.500€»)',
         'categoria': 'Cocina Caliente',
         'tarea': 'Horno mixto 10 GN (Rational o equivalente)',
         'responsable': 'Chef', 'estado': 'Pendiente', 'coste': 17500,
         'notas': ('Es el equipo nº' + N + '1 de la tabla 1 del propio libro y '
                   'NO estaba en las 54 filas del checklist. La única línea '
                   'de horno era el de convección de pastelería '
                   '(6.000' + N + '€), que es otra cosa.')},
        {'id': 'DOM-34', 'fuente': 'parametrizado (segundo escalón de gama)',
         'categoria': 'Cocina Caliente',
         'tarea': ('Bloque modular de cocción de alta gama (alternativa al '
                   'bloque estándar)'),
         'responsable': 'Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El bloque de 6 fuegos está presupuestado a '
                   '5.200' + N + '€ —precio de hostelería estándar— en una '
                   'guía que enseña a aspirar a estrella. Son dos escalones '
                   'distintos: elige uno y pon el otro a 0. ' + PRESUPUESTAR)},
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Cocina Caliente',
         'tarea': 'Placa de inducción de alto rendimiento para el pase (2 zonas)',
         'responsable': 'Sous Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'DOM-15', 'fuente': 'parametrizado',
         'categoria': 'Cocina Caliente',
         'tarea': 'Segundo roner y cuba termostática para servicio en paralelo',
         'responsable': 'Sous Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Con un solo roner no se sostienen dos binomios distintos '
                   'en el mismo servicio. ' + PRESUPUESTAR)},
        {'id': 'DOM-15', 'fuente': 'SPEC §3.2',
         'categoria': 'Cocina Caliente',
         'tarea': ('Sonda multipunto con registro para cocción a baja '
                   'temperatura'),
         'responsable': 'Resp. APPCC', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Es el equipo que produce el «registro de sonda por lote» '
                   'que pide el bloque nuevo del APPCC. ' + PRESUPUESTAR)},
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Cocina Caliente',
         'tarea': 'Juego completo de cubetas gastronorm y contenedores herméticos',
         'responsable': 'Sous Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        # ---- Pastelería/Obrador ------------------------------------------
        {'id': 'COM-23', 'fuente': 'parametrizado (cap.' + N + '9 lo nombra)',
         'categoria': 'Pastelería/Obrador',
         'tarea': 'Pacojet (helados, purés y polvos en frío)',
         'responsable': 'Chef Pastelero', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Como el Thermomix: la tarjeta del cap.' + N + '9 lo '
                   'nombra y no existía en ningún fichero. ' + PRESUPUESTAR)},
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Pastelería/Obrador',
         'tarea': 'Armario de fermentación controlada (panadería propia)',
         'responsable': 'Chef Pastelero', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El checklist Michelin pide «pan y petit fours de '
                   'producción propia»: esto es lo que hace falta para '
                   'cumplirlo. ' + PRESUPUESTAR)},
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Pastelería/Obrador',
         'tarea': 'Pistola de pintura para chocolate con compresor',
         'responsable': 'Chef Pastelero', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Pastelería/Obrador',
         'tarea': 'Pasteurizador / madurador de mezcla de helado',
         'responsable': 'Chef Pastelero', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        # ---- Pase/Expedición ---------------------------------------------
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Pase/Expedición',
         'tarea': ('Carro caliente de mantenimiento para eventos y comedor '
                   'privado'),
         'responsable': 'Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El checklist de sala presupuesta un comedor privado / '
                   "chef's table de " + _rango('8', '10') + N + 'plazas: hay '
                   'que llegar hasta allí con el plato caliente. '
                   + PRESUPUESTAR)},
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Pase/Expedición',
         'tarea': 'Temporizadores de pase y reloj de cocina (set)',
         'responsable': 'Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': ('El checklist Michelin exige «tiempos entre pases '
                   'controlados y fluidos». ' + PRESUPUESTAR)},
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Pase/Expedición',
         'tarea': 'Mesa de apoyo refrigerada para el pase de fríos',
         'responsable': 'Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        # ---- Almacenamiento ----------------------------------------------
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Almacenamiento',
         'tarea': 'Estanterías desmontables de polipropileno para cámaras',
         'responsable': 'Sous Chef', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Desmontables porque el plan de limpieza del APPCC exige '
                   'limpiar la cámara por dentro. ' + PRESUPUESTAR)},
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Almacenamiento',
         'tarea': 'Impresora de etiquetas de trazabilidad y consumibles',
         'responsable': 'Resp. APPCC', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Es lo que hace posible el «etiquetado de productos con '
                   'fecha y lote» del APPCC. ' + PRESUPUESTAR)},
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Almacenamiento',
         'tarea': ('Báscula de recepción de mercancía (hasta 60' + N + 'kg)'),
         'responsable': 'Resp. compras', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        # ---- Plonge/Lavado -----------------------------------------------
        {'id': 'DOM-33', 'fuente': 'R1 DOM-33 '
                                   '(' + _rango('12.000', '25.000') + N + '€)',
         'categoria': 'Plonge/Lavado',
         'tarea': ('Túnel de lavado con mesas de entrada y salida '
                   '(ALTERNATIVA a la capota)'),
         'responsable': 'Instalador', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Rango medido ' + _rango('12.000', '25.000') + N + '€. Va '
                   'SIN importe a propósito: es una alternativa al '
                   'lavavajillas de capota, no una partida adicional. Elige '
                   'una de las dos y pon la otra a 0, o el presupuesto '
                   'contará dos veces el mismo lavado.')},
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Plonge/Lavado',
         'tarea': 'Lavavasos independiente para la cristalería de maridaje',
         'responsable': 'Responsable', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'COM-17', 'fuente': 'parametrizado',
         'categoria': 'Plonge/Lavado',
         'tarea': 'Descalcificador y tratamiento de agua para el lavado',
         'responsable': 'Instalador', 'estado': 'Pendiente', 'coste': None,
         'notas': ('Sin él, la cristalería de maridaje sale velada. '
                   + PRESUPUESTAR)},
        # ---- Tecnología ---------------------------------------------------
        {'id': 'COM-17', 'fuente': 'parametrizado', 'categoria': 'Tecnología',
         'tarea': 'KDS: pantallas de comandas en cocina',
         'responsable': 'Gerente', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'COM-17', 'fuente': 'parametrizado', 'categoria': 'Tecnología',
         'tarea': 'SAI/UPS para TPV, cámaras y comunicaciones',
         'responsable': 'Instalador', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        {'id': 'COM-17', 'fuente': 'parametrizado', 'categoria': 'Tecnología',
         'tarea': 'Software de escandallos y APPCC digital',
         'responsable': 'Gerente', 'estado': 'Pendiente', 'coste': None,
         'notas': PRESUPUESTAR},
        # ---- Extracción e instalaciones (categoría nueva, va la ÚLTIMA) ---
        {'id': 'DOM-20', 'fuente': 'SPEC §3.4 '
                                   '(' + _rango('12.000', '30.000') + N + '€)',
         'categoria': 'Extracción e instalaciones',
         'tarea': ('Conducto de extracción hasta cubierta + ventilador + '
                   'silenciador'),
         'responsable': 'Instalador', 'estado': 'Pendiente', 'coste': 12000,
         'notas': ('Rango ' + _rango('12.000', '30.000') + N + '€ según '
                   'recorrido y altura; va precargado el MÍNIMO. El '
                   'cap.' + N + '5 lo llama «obstáculo técnico número 1» y '
                   'toda la extracción estaba presupuestada en '
                   '2.500' + N + '€.')},
        {'id': 'DOM-20', 'fuente': 'SPEC §3.4 '
                                   '(' + _rango('3.000', '6.000') + N + '€)',
         'categoria': 'Extracción e instalaciones',
         'tarea': 'Sistema de aportación de aire (compensación)',
         'responsable': 'Instalador', 'estado': 'Pendiente', 'coste': 3000,
         'notas': ('Rango ' + _rango('3.000', '6.000') + N + '€; precargado el '
                   'mínimo. Sin aportación de aire la campana no extrae y la '
                   'sala se queda en depresión.')},
        {'id': 'DOM-20', 'fuente': 'SPEC §3.4 '
                                   '(' + _rango('2.500', '4.000') + N + '€)',
         'categoria': 'Extracción e instalaciones',
         'tarea': ('Sistema automático de extinción en campana '
                   '(CTE DB' + G + 'SI y aseguradora)'),
         'responsable': 'Instalador', 'estado': 'Pendiente', 'coste': 2500,
         'notas': ('Rango ' + _rango('2.500', '4.000') + N + '€; precargado el '
                   'mínimo. Con freidora es exigible, y la aseguradora lo '
                   'pide para emitir la póliza. La cadena «extinción» no '
                   'aparecía en ningún fichero de la familia.')},
        {'id': 'DOM-20', 'fuente': 'SPEC §3.4 (12' + N + '%, calculado)',
         'categoria': 'Extracción e instalaciones',
         'tarea': ('Instalación, transporte y puesta en marcha (% sobre el '
                   'equipamiento)'),
         'responsable': 'Instalador', 'estado': 'Pendiente', 'coste': None,
         'notas': ('CALCULADO: es el porcentaje de la hoja «Instrucciones» '
                   'aplicado a la suma del resto de partidas de este '
                   'checklist. No hace falta que lo escribas: cambia solo '
                   'cuando cambias el equipamiento.')},
    ],
}

# ==========================================================================
# Mapa fichero → configuración (lo lee `grupo_b.post`)
# ==========================================================================
CHECKLISTS = {
    'checklist-legal.xlsx': LEGAL,
    'checklist-contratacion.xlsx': CONTRATACION,
    'checklist-appcc.xlsx': APPCC,
    'checklist-diseno-sala.xlsx': DISENO_SALA,
    'checklist-vajilla-cristaleria.xlsx': VAJILLA,
    'checklist-inspeccion-michelin-repsol.xlsx': MICHELIN,
    'checklist-marketing-preapertura.xlsx': MARKETING,
    'checklist-equipamiento-cocina.xlsx': EQUIPAMIENTO,
}


# ==========================================================================
# cronograma-apertura-gantt.xlsx — molde G1 (18 meses, F4:W4)
# TEC-14, TEC-15, DOM-37, COM-19, DOM-23
# ==========================================================================
#: El plan que se precarga es una HIPÓTESIS de planificación, no un dato del
#: sector, y las tres columnas son verdes y editables. Sólo dos duraciones
#: salen de un dato del propio producto y quedan citadas en su nota:
#:   · la licencia de actividad, «4-8 meses» (cap. 5, viñeta 51; R1 DOM-11),
#:     precargada en 6;
#:   · la formación del equipo, «2-4 semanas» (texto de la propia tarea),
#:     precargada en 1 mes.
#: El resto encadena esas dos con el horizonte de 18 meses que da nombre al
#: fichero. Ninguna suma supera M18: la regla de formato condicional en rojo
#: avisa si al editarlo se sale.
GANTT = {
    'sustituciones': [
        {
            'id': 'DOM-11/COM-28',
            'fuente': 'SPEC §3.1 (misma redacción que checklist-legal)',
            'buscar': 'Solicitud licencia de actividad C3',
            'tarea': ('Solicitud de licencia de actividad clasificada (el '
                      'nombre depende de la ordenanza municipal; C3 en '
                      'algunos municipios)'),
        },
    ],
    'nuevas_tareas': [
        {'id': 'DOM-23', 'fuente': 'SPEC §3.5',
         'despues_de': 'Búsqueda y selección de local',
         'tarea': 'Negociación y firma del arrendamiento (con carencia)',
         'responsable': 'Propietario + abogado', 'estado': 'Pendiente'},
        {'id': 'DOM-22/DOM-23', 'fuente': 'SPEC §3.5',
         'despues_de': 'Constitución de sociedad (SL)',
         'tarea': ('Dossier bancario, negociación de financiación, firma y '
                   'disposición'),
         'responsable': 'Propietario', 'estado': 'Pendiente'},
        # RD-29 · en una cocina con Josper, horno mixto de 10 GN, abatidor y
        # dos cámaras, la contratación y el aumento de potencia de luz, gas y
        # agua son meses de trámite y miles de euros de derechos de acometida.
        # El checklist legal pide los certificados de instalación y nadie
        # planificaba el alta.
        {'id': 'RD-29', 'fuente': 'parametrizado (trámite de suministros)',
         'despues_de': 'Proyecto técnico (arquitecto)',
         'tarea': ('Solicitud de acometidas y aumento de potencia (luz, gas y '
                   'agua)'),
         'responsable': 'Arquitecto + instalador', 'estado': 'Pendiente'},
        # RD-30 · la licencia de actividad se cerraba ANTES de que terminase la
        # obra, es decir, antes de que existieran el certificado final de obra
        # y el acta de comprobación que permiten iniciar la actividad. Ninguna
        # de las 24 tareas los mencionaba.
        {'id': 'RD-30', 'fuente': 'parametrizado (secuencia de licencias)',
         'despues_de': 'Obra civil y reforma integral',
         'tarea': ('Certificado final de obra y certificados de las '
                   'instalaciones (BT, gas, ventilación)'),
         'responsable': 'Arquitecto + instaladores', 'estado': 'Pendiente'},
        {'id': 'RD-30', 'fuente': 'parametrizado (secuencia de licencias)',
         'despues_de': ('Certificado final de obra y certificados de las '
                        'instalaciones (BT, gas, ventilación)'),
         'tarea': ('Resolución de la licencia de actividad y acta de '
                   'comprobación municipal'),
         'responsable': 'Ayuntamiento', 'estado': 'Pendiente'},
    ],
    #: tarea (tal como está escrita en la columna A) → mes de inicio,
    #: duración en meses y tarea de la que depende.
    #: RC-16 · el plan precargado incumplía en 7 de 20 la regla que sus propias
    #: Instrucciones enuncian («"Depende de" dice qué tarea tiene que estar
    #: terminada antes de empezar ésta»): tres tareas encadenadas caían en el
    #: mismo mes y el registro sanitario arrancaba a la vez que terminaba la
    #: obra de la que depende. Replanificado entero para que TODA tarea empiece
    #: el mes siguiente al fin de su predecesora, sin salirse de los 18 meses:
    #:
    #:   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18
    #:   viabilidad ▮▮ · local ▮▮▮ · SL ▮ · dossier ▮▮▮▮ · arrendamiento ▮▮
    #:   proyecto ▮▮ · licencias ▮▮▮/▮▮▮▮▮ · acometidas ▮▮▮▮ · obra ▮▮▮▮
    #:   certificados ▮ · resolución ▮ · equipos ▮▮ · pruebas ▮ · apertura ▮
    'tareas': {
        # FASE 1: PLANIFICACIÓN
        'Estudio de viabilidad financiera': {
            'mes': 1, 'duracion': 2, 'depende': ''},
        'Búsqueda y selección de local': {
            'mes': 1, 'duracion': 3, 'depende': ''},
        'Constitución de sociedad (SL)': {
            'mes': 2, 'duracion': 1, 'depende': ''},
        'Dossier bancario, negociación de financiación, firma y disposición': {
            'mes': 3, 'duracion': 4,
            'depende': 'Estudio de viabilidad financiera'},
        'Negociación y firma del arrendamiento (con carencia)': {
            'mes': 4, 'duracion': 2,
            'depende': 'Búsqueda y selección de local'},
        'Contratación arquitecto/interiorista': {
            'mes': 4, 'duracion': 1,
            'depende': 'Búsqueda y selección de local'},
        # FASE 2: LICENCIAS Y PROYECTO
        'Proyecto técnico (arquitecto)': {
            'mes': 5, 'duracion': 2,
            'depende': 'Contratación arquitecto/interiorista'},
        'Solicitud licencia de obras': {
            'mes': 7, 'duracion': 2,
            'depende': 'Proyecto técnico (arquitecto)'},
        'Solicitud de licencia de actividad clasificada (el nombre depende de '
        'la ordenanza municipal; C3 en algunos municipios)': {
            'mes': 7, 'duracion': 5,
            'depende': 'Proyecto técnico (arquitecto)'},
        'Solicitud de acometidas y aumento de potencia (luz, gas y agua)': {
            'mes': 7, 'duracion': 4,
            'depende': 'Proyecto técnico (arquitecto)'},
        # FASE 3: OBRA Y EQUIPAMIENTO
        'Obra civil y reforma integral': {
            'mes': 9, 'duracion': 4, 'depende': 'Solicitud licencia de obras'},
        'Certificado final de obra y certificados de las instalaciones (BT, '
        'gas, ventilación)': {
            'mes': 13, 'duracion': 1,
            'depende': 'Obra civil y reforma integral'},
        'Resolución de la licencia de actividad y acta de comprobación '
        'municipal': {
            'mes': 14, 'duracion': 1,
            'depende': ('Certificado final de obra y certificados de las '
                        'instalaciones (BT, gas, ventilación)')},
        'Registro sanitario CCAA': {
            'mes': 14, 'duracion': 1,
            'depende': ('Certificado final de obra y certificados de las '
                        'instalaciones (BT, gas, ventilación)')},
        'Instalación cocina profesional': {
            'mes': 13, 'duracion': 2,
            'depende': 'Obra civil y reforma integral'},
        'Mobiliario y decoración sala': {
            'mes': 13, 'duracion': 2,
            'depende': 'Obra civil y reforma integral'},
        'Instalación tecnología (TPV, etc.)': {
            'mes': 15, 'duracion': 1,
            'depende': 'Instalación cocina profesional'},
        # FASE 4: EQUIPO Y BODEGA
        'Selección y contratación brigada cocina': {
            'mes': 12, 'duracion': 3, 'depende': ''},
        'Selección equipo de sala': {'mes': 13, 'duracion': 2, 'depende': ''},
        'Compra vajilla/cristalería/cubertería': {
            'mes': 15, 'duracion': 1,
            'depende': 'Mobiliario y decoración sala'},
        'Selección proveedores y bodega': {
            'mes': 13, 'duracion': 2, 'depende': ''},
        # FASE 5: PRE-APERTURA
        'Formación de equipo (2-4 semanas)': {
            'mes': 15, 'duracion': 1,
            'depende': 'Selección y contratación brigada cocina'},
        'Pruebas de carta y menús': {
            'mes': 15, 'duracion': 1,
            'depende': 'Instalación cocina profesional'},
        'Fotografía profesional de platos': {
            'mes': 16, 'duracion': 1, 'depende': 'Pruebas de carta y menús'},
        'Marketing pre-apertura y prensa': {
            'mes': 15, 'duracion': 2, 'depende': ''},
        'Servicios de prueba (soft opening)': {
            'mes': 16, 'duracion': 1, 'depende': 'Pruebas de carta y menús'},
        # FASE 6: APERTURA
        'Apertura oficial': {
            'mes': 17, 'duracion': 1,
            'depende': 'Servicios de prueba (soft opening)'},
        'Primeros 30 días: monitorización': {
            'mes': 18, 'duracion': 1, 'depende': 'Apertura oficial'},
        'Ajustes de carta según feedback': {
            'mes': 18, 'duracion': 1, 'depende': 'Apertura oficial'},
    },
}
