#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
datos_ejemplo.py - JUEGO DE DATOS ÚNICO del producto «Manual del Chef Ejecutivo»
(SPEC: scripts/productos-digitales/manual-chef-ejecutivo-SPEC.md, D8).

Los 7 libros de Excel, el guion del manual (`guion_manual_chef_ejecutivo.py`) y
el bonus «12 situaciones resueltas en cocina» usan ESTAS partidas, ESTA brigada
y ESTAS 52 semanas. Regla de la familia: una sola fuente de cifras. Si un número
cambia, cambia aquí y se regeneran los libros.

CONTRATO CON LOS DOS PRODUCTOS HERMANOS (SPEC D8) - lo importante de este fichero
=================================================================================
Este juego de datos NO reinventa el restaurante: lo IMPORTA.

  · de `../manual-manager/datos_ejemplo.py`  -> RESTAURANTE, PLANTILLA (12
    personas), ESTACIONES (6 unidades), NIVELES_POLIVALENCIA, POLIVALENCIA,
    PLAN_CROSS_TRAINING, SEMANAS (52 semanas ISO), MESES, DIAS_MES_2026 y
    SS_EMPRESA;
  · de `../guia-food-cost/datos_ejemplo.py`  -> PLATOS (la carta de 20), LOS_12
    (los 12 platos de ejemplo), FICHA y `coste_ficha()`.

Es COPIA DECLARADA, no vínculo (SPEC D4: cero fórmulas entre ficheros). Lo que
este manual añade es la capa de COCINA: partidas, producción, merma por partida,
tiempos de pase, alérgenos de proceso, brigada del convenio, evaluación técnica,
desarrollo de carta, comidas testigo y banquetes, y auditoría interna de cocina.

TODO LO QUE HAY AQUÍ SON DATOS DE EJEMPLO DE UN CASO MODELADO («La Encina»), no
de un cliente real y no de «una cocina media». No hay ni una sola cifra «de
mercado» inventada: los datos del sector y de la ley NO viven en este fichero,
se referencian por id (`CE-*` normativa de cocina, `CS-*` datos del sector,
`MM-*` reutilizados del Manual del Manager) del JSON
`auditorias/guias-v2-research-sector.json`, que lleva fuente, URL y fiabilidad de
cada uno. Aquí solo aparece el id y, como mucho, la norma y su URL en una línea.

En particular (SPEC D10): los OBJETIVOS de KPI de `PARAMETROS_COCINA` son
objetivos DE LA CASA de este caso modelado. No existe un estándar publicado de
KPI de cocina en español y este producto no cita ninguno: los KPI se MIDEN, no
se comparan con un benchmark inventado.

TERMINOLOGÍA (SPEC D9): la unidad de trabajo se llama SIEMPRE «partida». Solo en
la primera mención de cada libro o documento se glosa «(estación)», que es como
la llama la matriz de polivalencia del Manual del Manager. `PARTIDAS` se
construye a partir de `ESTACIONES` para que la equivalencia sea automática.

Fecha de verificación legal de todo el bloque normativo: 06-09-2026.
Todos los textos de este fichero son WinAnsi (cp1252): lo comprueba `checks()`.

Ejecutar `python3 datos_ejemplo.py` corre `checks()` e imprime el resumen.
"""

import datetime as dt
import importlib.util
import os

_AQUI = os.path.dirname(os.path.abspath(__file__))


def _carga(nombre_modulo, *tramos):
    """Carga un datos_ejemplo.py hermano con un nombre de módulo PROPIO. Si se
    importara como `datos_ejemplo` chocaría con este mismo fichero cuando lo
    carga un constructor."""
    ruta = os.path.normpath(os.path.join(_AQUI, *tramos))
    if not os.path.exists(ruta):
        raise RuntimeError(
            'Falta %s. El juego de datos del Manual del Chef Ejecutivo NO se '
            'puede construir sin el contrato de la SPEC D8.' % ruta)
    spec = importlib.util.spec_from_file_location(nombre_modulo, ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


MANAGER = _carga('datos_manual_manager', '..', 'manual-manager', 'datos_ejemplo.py')
FOODCOST = _carga('datos_guia_food_cost', '..', 'guia-food-cost', 'datos_ejemplo.py')

# --- lo que se importa del Manual del Manager (SPEC D8) --------------------
RESTAURANTE = MANAGER.RESTAURANTE
PLANTILLA = MANAGER.PLANTILLA
ESTACIONES = MANAGER.ESTACIONES
NIVELES_POLIVALENCIA = MANAGER.NIVELES_POLIVALENCIA
POLIVALENCIA = MANAGER.POLIVALENCIA
PLAN_CROSS_TRAINING = MANAGER.PLAN_CROSS_TRAINING
SEMANAS = MANAGER.SEMANAS
MESES = MANAGER.MESES
DIAS_MES_2026 = MANAGER.DIAS_MES_2026
SEMANAS_FUERA_DE_OBJETIVO = MANAGER.SEMANAS_FUERA_DE_OBJETIVO
SS_EMPRESA = MANAGER.SS_EMPRESA

# --- lo que se importa de la Guía Food Cost -------------------------------
PLATOS = FOODCOST.PLATOS
LOS_12 = FOODCOST.LOS_12
FICHA = FOODCOST.FICHA
coste_ficha = FOODCOST.coste_ficha

# Tabla de tres filas que va impresa en «Instrucciones» de los libros 1 y 4
# (SPEC D8): qué se copia de dónde y qué NO hay que volver a teclear.
CONTRATO_ENTRE_MANUALES = [
    ('Manual del Manager de Restaurante',
     'Las 12 personas de la plantilla, las 6 unidades (aquí «partidas»), la matriz de '
     'polivalencia y las 52 semanas ISO con sus cubiertos',
     'No vuelvas a teclear la plantilla ni los cubiertos: si ya tienes el Manager, '
     'copia y pega de su cuadro semanal'),
    ('Guía Food Cost + Ingeniería de Menú',
     'La carta de 20 platos, el mix de venta de los 12 de ejemplo y el coste por '
     'ración de la ficha de escandallo',
     'El coste por ración de la ficha técnica de proceso se COPIA del escandallo '
     '(celda verde); este pack no lo recalcula'),
    ('Este manual',
     'Producción y merma por partida, tiempos de pase, incidencias de alérgenos, '
     'horas de cocina, evaluación técnica, banquetes y auditoría de cocina',
     'Es la capa que no cubre ninguno de los dos anteriores'),
]


# ==========================================================================
# 1. LAS PARTIDAS (SPEC D9)
# ==========================================================================
# «Partida» es el término único de este producto. Son LAS MISMAS SEIS UNIDADES
# que la matriz de polivalencia del Manual del Manager llama «estación»: la
# lista se construye a partir de `ESTACIONES` para que no puedan desincronizarse.
#
# De las seis, CUATRO producen raciones en cocina y son las que llevan
# producción y merma en el cuadro de mando. Las otras dos (sala y caja) existen
# en el negocio y en la matriz del Manager, pero no producen raciones: sus
# columnas van vacías («sin dato» = "" por convención de familia, y el semaforo
# las ignora por `ISNUMBER`). Esa es, además, la demostración del mecanismo de
# «partidas activas» de la SPEC D7: el libro trae seis columnas y cada cocina
# rellena las que tenga.
#
# columnas: nombre, produce_raciones, que produce, equivalencia con el Manager
PARTIDAS = [
    (ESTACIONES[0], True,
     'Principales calientes: plancha, brasa, horno, arroces y salsas del pase',
     'Equivale a la columna «%s» de la matriz de polivalencia del Manual del Manager' % ESTACIONES[0]),
    (ESTACIONES[1], True,
     'Entrantes fríos y calientes de entrada: ensaladas, cazuelas, fritos y raciones',
     'Equivale a la columna «%s» de la matriz de polivalencia del Manual del Manager' % ESTACIONES[1]),
    (ESTACIONES[2], True,
     'Postres de plato, masas y pan de la casa',
     'Equivale a la columna «%s» de la matriz de polivalencia del Manual del Manager' % ESTACIONES[2]),
    (ESTACIONES[3], True,
     'Elaboraciones de barra: zumos naturales, vermut, coctelería y aperitivo',
     'Equivale a la columna «%s» de la matriz de polivalencia del Manual del Manager' % ESTACIONES[3]),
    (ESTACIONES[4], False,
     'Servicio de sala: no produce raciones, por eso su columna va vacía',
     'Equivale a la columna «%s» de la matriz de polivalencia del Manual del Manager' % ESTACIONES[4]),
    (ESTACIONES[5], False,
     'Caja y cierre: no produce raciones, por eso su columna va vacía',
     'Equivale a la columna «%s» de la matriz de polivalencia del Manual del Manager' % ESTACIONES[5]),
]

# Indices comodos (nunca se escriben a mano en un constructor)
IDX_PASE, IDX_FRIOS, IDX_POSTRES, IDX_BARRA = 0, 1, 2, 3
PARTIDAS_PRODUCCION = [p[0] for p in PARTIDAS if p[1]]
# Las tres partidas de COCINA propiamente dicha: son las que evalúa la rúbrica
# de competencias técnicas del libro 4 (la barra es área 3.ª del ALEH).
PARTIDAS_COCINA = [ESTACIONES[IDX_PASE], ESTACIONES[IDX_FRIOS], ESTACIONES[IDX_POSTRES]]

# SPEC D9. La glosa se escribe UNA sola vez por libro o documento, en la primera
# mención; a partir de ahí, siempre «partida» a secas. La nota de equivalencia es
# la que va en el libro 4, junto a «próxima partida a aprender».
GLOSA_PRIMERA_MENCION = 'partida (estación)'
NOTA_EQUIVALENCIA_PARTIDA = ('Equivale a la columna «estación» de la matriz de polivalencia '
                             'del Manual del Manager.')
# Área funcional del ALEH VI a la que pertenece la brigada (tal cual la escribe
# PLANTILLA en el Manual del Manager).
AREA_COCINA = 'Área 2ª'


# ==========================================================================
# 2. PARAMETROS DE COCINA (hoja «Parámetros» del libro 1)
# ==========================================================================
# TODOS los objetivos son OBJETIVOS DE LA CASA de este caso modelado, en celda
# verde y obligatorios: mientras la celda este vacía el semaforo queda GRIS
# (SPEC D10). Este producto no publica benchmarks de merma, de tiempo de pase ni
# de horas de formación, porque no existe ninguno verificado en español.
PARAMETROS_COCINA = {
    'tipo_carta': 'Carta de temporada con menú del mediodía',
    'tipos_carta_lista': ['Carta fija', 'Carta de temporada con menú del mediodía',
                          'Menú degustación', 'Solo menú del día', 'Banquetes y eventos'],
    # SPEC D7: la celda «partidas activas» gobierna cuantas columnas de partida
    # se muestran (3 a 8). La Encina declara las SEIS unidades del contrato con
    # el Manager; cuatro de ellas producen raciones.
    'partidas_activas': 6,
    'partidas_con_produccion': 4,
    # Peso medio de materia prima NETA por ración de cada partida, medido sobre
    # la carta completa de 20 platos. Celda editable: es lo que convierte la
    # merma (kg) y la producción (raciones) en un porcentaje comparable.
    'kg_racion': {
        ESTACIONES[IDX_PASE]: 0.36,
        ESTACIONES[IDX_FRIOS]: 0.22,
        ESTACIONES[IDX_POSTRES]: 0.14,
        ESTACIONES[IDX_BARRA]: 0.09,
    },
    # Raciones que sirve cada partida por cubierto, a partir de las unidades/mes
    # de la carta de la Guía Food Cost. Se recalcula en `raciones_por_cubierto()`:
    # aquí solo queda como referencia del orden de magnitud.
    'objetivos': {
        # merma sobre el peso producido, por partida
        'merma_' + ESTACIONES[IDX_PASE]: 0.035,
        'merma_' + ESTACIONES[IDX_FRIOS]: 0.055,
        'merma_' + ESTACIONES[IDX_POSTRES]: 0.030,
        'merma_' + ESTACIONES[IDX_BARRA]: 0.045,
        # tiempo de pase por familia de plato, en minutos desde la comanda
        'pase_entrantes_min': 10.0,
        'pase_principales_min': 18.0,
        'pase_postres_min': 8.0,
        # incidencias de alérgenos por cada 1.000 cubiertos
        'incidencias_alergenos_1000': 0.50,
        # horas de cocina trabajadas por cubierto servido
        'horas_cocina_cubierto': 0.260,
        # platos devueltos y retrabajados por cada 1.000 cubiertos
        'devueltos_1000': 6.0,
        'retrabajados_1000': 16.0,
        # conformidad del pase con la ficha técnica (libro 5)
        'cumplimiento_ficha': 0.90,
    },
    # Días que un plato puede estar «en prueba» sin ficha técnica cerrada antes
    # de que el libro 5 encienda la alerta.
    'dias_max_en_prueba_sin_ficha': 30,
    'fecha_corte_normativa': '2026-09-06',
    'fecha_inicio_plan_90': RESTAURANTE['fecha_inicio_plan_90'],
}

# Los SIETE KPI de cocina. Encuadre obligatorio (SPEC D10): «no existe un
# estándar publicado de KPI de cocina en español; esta es nuestra lista, por qué
# cada uno y su error típico».
# columnas: kpi, fórmula en palabras, unidad, error típico, cadencia
KPI_COCINA = [
    ('Merma por partida',
     'Merma de la partida (kg) / (raciones producidas x kg por ración de esa partida)',
     '%',
     'Mirar la merma total de la cocina en vez de la de cada partida: la de una '
     'partida se compensa con la de otra y el problema no aparece nunca',
     'Semanal'),
    ('Tiempo de pase por familia de plato',
     'Media de los tiempos muestreados entre comanda y salida, separando entrantes, '
     'principales y postres',
     'minutos',
     'Dar una sola media para toda la carta: un postre y un arroz no compiten en la '
     'misma liga y la media los esconde a los dos',
     'Semanal'),
    ('Incidencias de alérgenos por 1.000 cubiertos',
     'Incidencias registradas x 1.000 / cubiertos servidos',
     'incidencias/1.000',
     'Contar solo las que llegaron al cliente: la que se detecta en el pase es la que '
     'te dice dónde está el fallo del proceso',
     'Semanal'),
    ('Horas de cocina por cubierto',
     'Horas realmente trabajadas por la brigada / cubiertos servidos',
     'h/cubierto',
     'Alimentarlo con las horas del contrato en lugar de las del registro de jornada, '
     'y meter dentro las horas de sala',
     'Semanal'),
    ('Cumplimiento de ficha técnica',
     'Muestreos conformes con la ficha / muestreos hechos en el pase',
     '%',
     'Preguntar «tenemos ficha?» en vez de «se ha seguido?»: tener la ficha escrita no '
     'es cumplirla',
     'Semanal'),
    ('Platos devueltos y retrabajados por 1.000 cubiertos',
     '(Devueltos + retrabajados) x 1.000 / cubiertos servidos',
     'platos/1.000',
     'Registrar solo la devolución del cliente: el plato que se rehace antes de salir '
     'no se ve en la cuenta y es el que más dinero cuesta',
     'Semanal'),
    ('Rotación de la brigada',
     'Bajas de cocina del periodo / plantilla media de cocina del periodo',
     '%',
     'Mezclarla con la rotación de sala: en un restaurante con temporada son dos '
     'realidades distintas y se corrigen distinto',
     'Trimestral'),
]


# ==========================================================================
# 3. EL AÑO SEMANAL DE COCINA: 52 SEMANAS ISO DE 2026
# ==========================================================================
# Es EL MISMO año y EL MISMO restaurante que el cuadro semanal del Manual del
# Manager, visto desde la cocina. La columna de cubiertos es COPIA LITERAL de
# `SEMANAS` (columna 10 del Manager) y `checks()` la compara semana a semana: si
# alguien toca el Manager y no toca esto, el gate lo canta.
#
# Como se construyo cada columna:
#   · producción por partida = cubiertos x raciones por cubierto de esa partida
#     (de las unidades/mes de la carta de la Guía Food Cost), con la variación
#     semanal propia de un servicio real;
#   · merma en kg = producción x kg por ración x el porcentaje de merma de la
#     semana;
#   · tiempos de pase = media de los muestreos de la semana, por familia;
#   · horas de cocina = jornada contratada de la brigada (área 2.ª: P02, P04,
#     P05, P06 y P12 = 190 h/semana, más P07 con 40 h en su campaña de marzo a
#     noviembre = 230 h) más la parte proporcional del exceso de horas que ya
#     registra el Manager esa semana. Nunca menos que el contrato.
#
# CUATRO SEMANAS MALAS, y cuentan dos historias distintas:
#   · semana  7 (9-15 feb) ..... el PASE se descontrola: 25,6 min de media en
#     principales contra un objetivo de 18, 9 platos devueltos y 19 retrabajados,
#     y una incidencia de alérgeno de gravedad 3. Es la semana que el Manager ya
#     tiene fuera de objetivo de prime cost (72,0 %).
#   · semanas 33, 34 y 35 (ago) . la MERMA DE LA PARTIDA DE FRÍOS se dispara TRES
#     SEMANAS SEGUIDAS (9,2 %, 10,7 % y 9,7 % contra un objetivo del 5,5 %). Es
#     la situación 7 del bonus, y explica por dentro dos de las semanas que el
#     Manager ve fuera de objetivo desde fuera (33 y 35). Además es la partida
#     que la matriz de polivalencia del Manager marca como PUNTO ÚNICO DE FALLO:
#     solo Laura S. (P05) la sostiene, y en agosto libra.
#
# columnas:
#   semana ISO, mes (del jueves), cubiertos,
#   producción en raciones por partida (6, las dos últimas None),
#   merma en kg por partida (6, las dos últimas None),
#   tiempos de pase en minutos (entrantes, principales, postres),
#   incidencias de alérgenos, gravedad máxima (0-3),
#   horas de cocina trabajadas, platos devueltos, platos retrabajados
SEMANA_COCINA = [
    ( 1,  1,  829, (441, 371, 233, 296, None, None), (  5.2,   3.6,  0.7,  1.1, None, None), ( 9.8, 18.2,  6.5), 0, 0, 198,  5,  9),
    ( 2,  1,  785, (404, 339, 222, 292, None, None), (  4.3,   3.6,  0.8,  1.1, None, None), ( 9.7, 16.8,  5.6), 0, 0, 193,  3,  6),
    ( 3,  1,  764, (385, 338, 225, 286, None, None), (  4.8,   3.8,  0.7,  0.9, None, None), ( 8.6, 15.0,  5.9), 0, 0, 190,  2,  6),
    ( 4,  1,  792, (416, 361, 229, 285, None, None), (  4.7,   3.5,  0.8,  1.1, None, None), ( 7.4, 13.9,  7.0), 1, 1, 193,  3,  9),
    ( 5,  1,  774, (410, 342, 216, 279, None, None), (  4.5,   3.9,  0.8,  1.0, None, None), ( 6.9, 14.0,  7.7), 0, 0, 193,  4, 10),
    ( 6,  2,  807, (410, 348, 231, 303, None, None), (  5.1,   3.7,  0.7,  1.0, None, None), ( 7.6, 15.3,  7.1), 0, 0, 197,  5, 10),
    ( 7,  2,  753, (383, 338, 222, 279, None, None), (  4.1,   3.3,  0.8,  1.1, None, None), (13.8, 25.6, 10.9), 1, 3, 193,  9, 19),
    ( 8,  2,  775, (411, 352, 221, 277, None, None), (  4.8,   4.0,  0.8,  0.9, None, None), ( 9.8, 18.4,  5.6), 0, 0, 196,  2,  6),
    ( 9,  2,  795, (416, 346, 222, 290, None, None), (  5.1,   3.5,  0.7,  1.0, None, None), ( 9.7, 18.5,  6.5), 0, 0, 199,  3,  7),
    (10,  3,  776, (391, 338, 226, 292, None, None), (  4.1,   3.5,  0.8,  1.1, None, None), ( 8.6, 17.4,  7.5), 0, 0, 217,  4,  9),
    (11,  3,  802, (414, 364, 236, 293, None, None), (  5.0,   4.1,  0.8,  1.0, None, None), ( 7.4, 15.7,  7.5), 0, 0, 219,  4, 11),
    (12,  3,  824, (439, 370, 232, 294, None, None), (  5.1,   3.6,  0.7,  1.1, None, None), ( 6.9, 14.2,  6.4), 1, 2, 220,  3, 10),
    (13,  3,  839, (433, 362, 236, 311, None, None), (  4.6,   4.0,  0.9,  1.2, None, None), ( 7.6, 13.8,  5.5), 0, 0, 220,  3,  8),
    (14,  4, 1045, (527, 461, 307, 393, None, None), (  6.6,   5.1,  1.0,  1.3, None, None), ( 8.9, 14.7,  5.9), 0, 0, 242,  5,  8),
    (15,  4,  894, (468, 408, 260, 322, None, None), (  5.2,   3.9,  0.9,  1.2, None, None), ( 9.8, 16.4,  7.1), 0, 0, 224,  5,  9),
    (16,  4,  881, (468, 391, 246, 316, None, None), (  5.2,   4.4,  0.9,  1.1, None, None), ( 9.7, 18.0,  7.7), 1, 1, 223,  5, 11),
    (17,  4,  870, (443, 375, 248, 326, None, None), (  5.5,   3.9,  0.8,  1.1, None, None), ( 8.6, 18.6,  7.0), 0, 0, 223,  3, 11),
    (18,  4,  864, (438, 386, 255, 321, None, None), (  4.6,   3.8,  0.9,  1.3, None, None), ( 7.3, 17.9,  5.8), 0, 0, 224,  3, 10),
    (19,  5,  902, (477, 410, 259, 322, None, None), (  5.6,   4.7,  0.9,  1.1, None, None), ( 6.9, 16.3,  5.6), 0, 0, 231,  4,  8),
    (20,  5,  899, (473, 393, 251, 327, None, None), (  5.7,   3.9,  0.8,  1.2, None, None), ( 7.6, 14.7,  6.6), 0, 0, 232,  5,  7),
    (21,  5,  894, (451, 388, 259, 337, None, None), (  4.7,   4.1,  0.9,  1.3, None, None), ( 8.9, 13.8,  7.6), 1, 2, 232,  4,  9),
    (22,  5,  906, (465, 410, 267, 333, None, None), (  5.7,   4.6,  0.9,  1.1, None, None), ( 9.8, 14.2,  7.4), 0, 0, 233,  3, 12),
    (23,  6,  962, (512, 434, 272, 343, None, None), (  5.9,   4.2,  0.9,  1.3, None, None), ( 9.7, 15.7,  6.3), 0, 0, 238,  3, 12),
    (24,  6,  979, (508, 424, 275, 361, None, None), (  5.5,   4.7,  1.0,  1.3, None, None), ( 8.5, 17.5,  5.5), 0, 0, 238,  5, 10),
    (25,  6,  996, (501, 437, 292, 375, None, None), (  6.3,   4.7,  0.9,  1.2, None, None), ( 7.3, 18.5,  6.0), 1, 1, 238,  6,  8),
    (26,  6, 1010, (526, 460, 295, 366, None, None), (  5.7,   4.5,  1.0,  1.4, None, None), ( 6.9, 18.3,  7.2), 0, 0, 238,  5,  9),
    (27,  7, 1022, (543, 455, 286, 366, None, None), (  6.1,   5.2,  1.0,  1.3, None, None), ( 7.6, 17.0,  7.7), 0, 0, 239,  3, 11),
    (28,  7, 1029, (526, 444, 293, 384, None, None), (  6.5,   4.6,  0.9,  1.3, None, None), ( 8.9, 15.2,  6.9), 0, 0, 240,  4, 13),
    (29,  7, 1027, (520, 457, 303, 383, None, None), (  5.5,   4.6,  1.1,  1.5, None, None), ( 9.8, 14.0,  5.7), 2, 2, 241,  6, 12),
    (30,  7, 1020, (538, 465, 294, 365, None, None), (  6.4,   5.3,  1.0,  1.2, None, None), ( 9.6, 13.9,  5.6), 0, 0, 242,  6, 10),
    (31,  7,  962, (507, 422, 269, 348, None, None), (  6.1,   4.1,  0.8,  1.3, None, None), ( 8.5, 15.1,  6.7), 1, 1, 237,  4,  8),
    (32,  8,  847, (428, 367, 244, 319, None, None), (  4.5,   3.9,  0.9,  1.2, None, None), ( 7.3, 16.8,  7.6), 0, 0, 225,  3,  8),
    (33,  8,  809, (414, 365, 239, 298, None, None), (  5.1,   7.4,  0.8,  1.0, None, None), ( 8.2, 20.1,  7.4), 0, 0, 221,  5, 14),
    (34,  8,  819, (435, 371, 233, 292, None, None), (  4.9,   8.7,  0.8,  1.1, None, None), ( 9.0, 20.5,  6.2), 1, 2, 222,  7, 15),
    (35,  8,  845, (440, 367, 237, 310, None, None), (  4.8,   7.8,  0.9,  1.1, None, None), (10.3, 19.5,  5.5), 0, 0, 224,  7, 14),
    (36,  9,  903, (455, 395, 264, 340, None, None), (  5.7,   4.2,  0.8,  1.1, None, None), ( 9.8, 15.9,  6.1), 0, 0, 229,  4,  8),
    (37,  9,  958, (497, 436, 280, 348, None, None), (  5.4,   4.3,  1.0,  1.4, None, None), ( 9.6, 14.4,  7.3), 0, 0, 234,  3,  8),
    (38,  9,  981, (522, 438, 275, 351, None, None), (  6.0,   5.0,  1.0,  1.2, None, None), ( 8.5, 13.8,  7.7), 1, 1, 235,  4, 10),
    (39,  9,  969, (497, 418, 274, 361, None, None), (  6.1,   4.2,  0.8,  1.3, None, None), ( 7.3, 14.5,  6.8), 0, 0, 233,  6, 12),
    (40, 10,  892, (450, 396, 263, 334, None, None), (  4.7,   4.1,  0.9,  1.3, None, None), ( 6.9, 16.2,  5.7), 0, 0, 224,  5, 11),
    (41, 10,  909, (478, 414, 263, 326, None, None), (  5.8,   4.7,  0.9,  1.1, None, None), ( 7.7, 17.8,  5.7), 0, 0, 227,  3, 10),
    (42, 10,  894, (473, 394, 250, 323, None, None), (  5.6,   3.8,  0.8,  1.2, None, None), ( 9.0, 18.6,  6.7), 0, 0, 227,  3,  7),
    (43, 10,  869, (441, 375, 250, 327, None, None), (  4.7,   4.1,  0.9,  1.2, None, None), ( 9.8, 18.1,  7.7), 1, 2, 226,  4,  7),
    (44, 10,  857, (437, 385, 253, 317, None, None), (  5.5,   4.3,  0.8,  1.0, None, None), ( 9.6, 16.6,  7.3), 0, 0, 226,  5,  9),
    (45, 11,  830, (441, 377, 237, 296, None, None), (  4.9,   3.6,  0.8,  1.1, None, None), ( 8.5, 14.9,  6.1), 0, 0, 224,  4, 11),
    (46, 11,  840, (439, 365, 235, 307, None, None), (  4.8,   4.1,  0.9,  1.1, None, None), ( 7.3, 13.9,  5.5), 0, 0, 225,  3, 10),
    (47, 11,  849, (428, 370, 247, 320, None, None), (  5.4,   3.9,  0.8,  1.1, None, None), ( 6.9, 14.1,  6.2), 1, 1, 225,  3,  8),
    (48, 11,  872, (451, 396, 256, 318, None, None), (  4.8,   3.9,  0.9,  1.2, None, None), ( 7.7, 15.5,  7.4), 0, 0, 226,  4,  7),
    (49, 12,  989, (527, 444, 278, 353, None, None), (  6.1,   5.1,  1.0,  1.2, None, None), ( 9.0, 17.2,  7.6), 0, 0, 215,  6,  9),
    (50, 12, 1068, (550, 461, 301, 396, None, None), (  6.7,   4.6,  0.9,  1.4, None, None), ( 9.9, 18.4,  6.7), 1, 1, 221,  5, 12),
    (51, 12, 1120, (565, 495, 329, 420, None, None), (  5.9,   5.1,  1.2,  1.6, None, None), ( 9.6, 18.4,  5.6), 1, 2, 226,  4, 15),
    (52, 12, 1140, (597, 520, 331, 411, None, None), (  7.3,   5.9,  1.1,  1.4, None, None), ( 8.4, 17.2,  5.7), 0, 0, 228,  4, 13),
]

# Semanas que el manual y el bonus citan por su número.
SEMANAS_MALAS_COCINA = (7, 33, 34, 35)
SEMANAS_MERMA_FRIOS = (33, 34, 35)     # bonus, situación 7
SEMANA_PASE_DESCONTROLADO = 7          # bonus, situación 5

# Jornada contratada de la brigada (área 2.ª del ALEH), por semana. No es una
# cifra nueva: sale de la columna «jornada_h_semana» de PLANTILLA. La calcula
# `horas_contrato_cocina()`; estas dos constantes solo documentan el resultado.
CAMPANA_FIJO_DISCONTINUO = tuple(range(3, 12))   # P07: de marzo a noviembre


# ==========================================================================
# 4. COMPARATIVA ENTRE UNIDADES (hoja del libro 1, SPEC D6)
# ==========================================================================
# «Una cocina, con las herramientas para comparar varias». Los KPI son los del
# MES CERRADO de agosto de 2026 (semanas ISO 32 a 35). Los de «La Encina» NO se
# teclean: `checks()` los recalcula desde SEMANA_COCINA y exige que coincidan.
# Las otras dos unidades son datos de ejemplo de un grupo pequeño.
UNIDADES_MES = {'anio': 2026, 'mes': 8, 'semanas': (32, 33, 34, 35)}

# columnas: unidad, cubiertos, merma global %, tiempo de pase en principales
#           (min), incidencias de alérgenos/1.000, horas de cocina/cubierto,
#           platos devueltos/1.000
UNIDADES = [
    ('La Encina (unidad de referencia)', 3320, 0.0463, 19.2, 0.30, 0.269, 6.63),
    ('La Encina Norte',                  2860, 0.0382, 17.4, 0.35, 0.249, 4.90),
    ('La Encina Playa',                  4180, 0.0541, 21.3, 0.72, 0.288, 8.61),
]
# Estándar del grupo: es el OBJETIVO propio del grupo (celda verde), no un
# benchmark del sector (SPEC D10).
ESTANDAR_GRUPO = {
    'merma_global': 0.0400,
    'pase_principales_min': 18.0,
    'incidencias_alergenos_1000': 0.50,
    'horas_cocina_cubierto': 0.260,
    'devueltos_1000': 6.00,
}


# ==========================================================================
# 5. PLANIFICACIÓN DE PRODUCCIÓN (libro 2)
# ==========================================================================
# Semana tipo = semana ISO 37 (7 a 13 de septiembre de 2026), la que arranca el
# plan de 90 días del Manual del Manager. Sus 958 cubiertos son los mismos que
# los de `SEMANA_COCINA` y los de `SEMANAS` del Manager: `checks()` lo comprueba.
SEMANA_TIPO_PREVISION = 37

# columnas: día, servicio, reservas confirmadas, histórico del mismo servicio
#           (media de las 4 semanas anteriores), previsión de cubiertos
PREVISION_CUBIERTOS = [
    ('Martes',    'Comida',  34,  58,  60),
    ('Martes',    'Cena',    22,  41,  40),
    ('Miercoles', 'Comida',  38,  62,  64),
    ('Miercoles', 'Cena',    26,  45,  46),
    ('Jueves',    'Comida',  41,  68,  70),
    ('Jueves',    'Cena',    34,  56,  58),
    ('Viernes',   'Comida',  46,  76,  78),
    ('Viernes',   'Cena',    68, 102, 105),
    ('Sabado',    'Comida',  55,  89,  92),
    ('Sabado',    'Cena',    79, 115, 118),
    ('Domingo',   'Comida',  88, 128, 132),
    ('Domingo',   'Cena',    56,  93,  95),
]

# Mix de venta de los 12 platos de ejemplo de la Guía Food Cost. El % de mix NO
# se teclea: se deriva de las unidades/mes de la carta y de los cubiertos/mes de
# `RESTAURANTE` (lo hace `mix_venta()`). Lo único propio de este manual es la
# PARTIDA que produce cada plato, la unidad de ración y su peso de materia prima
# neta, que es lo que convierte «raciones» en «kg» en el cuadro de mando.
#
# columnas: id, partida, unidad de ración, peso de materia prima neta (kg)
MIX_VENTA_PARTIDA = [
    ('E1', ESTACIONES[IDX_FRIOS],   '6 croquetas',                     0.18),
    ('E2', ESTACIONES[IDX_FRIOS],   '1 ración de ensalada',            0.26),
    ('E3', ESTACIONES[IDX_FRIOS],   '1 cazuela',                       0.19),
    ('E4', ESTACIONES[IDX_FRIOS],   '1 ración para compartir',         0.24),
    ('P1', ESTACIONES[IDX_PASE],    '1 ración (solomillo y puré)',     0.40),
    ('P2', ESTACIONES[IDX_PASE],    '1 lomo confitado',                0.30),
    ('P3', ESTACIONES[IDX_PASE],    '1 hamburguesa con guarnición',    0.34),
    ('P4', ESTACIONES[IDX_PASE],    '1 ración de arroz (mínimo 2 pax)', 0.36),
    ('P5', ESTACIONES[IDX_PASE],    '1 chuletón de 500 g',             0.52),
    ('D1', ESTACIONES[IDX_POSTRES], '1 porción',                       0.14),
    ('D2', ESTACIONES[IDX_POSTRES], '1 torrija con helado',            0.15),
    ('D3', ESTACIONES[IDX_POSTRES], '1 coulant',                       0.13),
]

# Stock ya elaborado el lunes 7 de septiembre de 2026, antes de lanzar la
# producción de la semana 37. Es lo que se RESTA de la producción prevista
# (cantidad a producir = cubiertos x mix - stock elaborado).
# columnas: id del plato, elaboración, partida, raciones en cámara,
#           fecha de elaboración, vida útil en días, conservación
STOCK_ELABORADO = [
    ('E1', 'Masa de croqueta ya formada y empanada', ESTACIONES[IDX_FRIOS], 140,
     '2026-09-05', 3, 'Refrigeración a 4 °C'),
    ('E2', 'Sin stock: se monta a la comanda', ESTACIONES[IDX_FRIOS], 0,
     '', 0, 'No aplica'),
    ('E3', 'Gamba pelada y racionada', ESTACIONES[IDX_FRIOS], 32,
     '2026-09-06', 1, 'Refrigeración a 4 °C'),
    ('E4', 'Patata confitada', ESTACIONES[IDX_FRIOS], 90,
     '2026-09-05', 4, 'Refrigeración a 4 °C'),
    ('P1', 'Puré de boniato', ESTACIONES[IDX_PASE], 60,
     '2026-09-06', 3, 'Refrigeración a 4 °C'),
    ('P2', 'Bacalao desalado y porcionado', ESTACIONES[IDX_PASE], 24,
     '2026-09-05', 2, 'Refrigeración a 4 °C'),
    ('P3', 'Hamburguesa formada', ESTACIONES[IDX_PASE], 80,
     '2026-09-06', 2, 'Refrigeración a 4 °C'),
    ('P4', 'Fondo de arroz y sofrito', ESTACIONES[IDX_PASE], 110,
     '2026-09-04', 5, 'Refrigeración a 4 °C'),
    ('P5', 'Sin stock: se raciona en el momento', ESTACIONES[IDX_PASE], 0,
     '', 0, 'No aplica'),
    ('D1', 'Tarta de queso cuajada', ESTACIONES[IDX_POSTRES], 46,
     '2026-09-06', 4, 'Refrigeración a 4 °C'),
    ('D2', 'Torrija empapada, sin caramelizar', ESTACIONES[IDX_POSTRES], 32,
     '2026-09-05', 3, 'Refrigeración a 4 °C'),
    ('D3', 'Coulant crudo congelado', ESTACIONES[IDX_POSTRES], 120,
     '2026-08-28', 60, 'Congelación a -18 °C'),
]


# ==========================================================================
# 6. FICHA TÉCNICA DE PROCESO (libro 3) - ejemplo relleno
# ==========================================================================
# Se elige P1 a propósito: es el ÚNICO plato de la carta cuyo coste por ración
# sale de una ficha de escandallo completa en la Guía Food Cost, así que se
# puede demostrar la regla de la SPEC D4 sin inventar nada.
#
# SPEC D4: la ficha técnica de proceso NO calcula el coste. Trae una celda verde
# «coste por ración (copialo de tu escandallo)». Aquí va ya rellena con el valor
# que devuelve `coste_ficha()` de la Guía Food Cost, y la nota dice que es una
# COPIA. Cero fórmulas entre ficheros.
#
# SPEC D5 (séptima regla de no-solape): los alérgenos que lleva esta ficha son
# los ALERGENOS DE PROCESO de ESTA elaboración. La declaración de carta (las 14
# columnas por plato) vive en `pack-appcc/08-matriz-alergenos.xlsx` y aquí solo
# se remite a ella. Nunca las dos declaraciones completas.
FICHA_TECNICA_EJEMPLO = {
    'id_plato': 'P1',
    'plato': FICHA['plato'],
    'familia': FICHA['familia'],
    'partida': ESTACIONES[IDX_PASE],
    'raciones_ficha': 1,
    'version': '1.2',
    'fecha_revision': '2026-09-06',
    'revisada_por': 'P02 (jefe de cocina)',
    # SPEC D4: copiado del escandallo, no calculado aquí.
    'coste_racion_copiado': coste_ficha(),
    'nota_coste': ('Copiado de la ficha de escandallo del plato en el Kit de '
                   'Escandallos / Guía Food Cost. Esta hoja NO recalcula costes: '
                   'si cambia el precio de compra, se actualiza allí y se vuelve '
                   'a copiar aquí.'),
    'pasos': [
        (1, 'Atemperar el solomillo 20 minutos fuera de cámara y salpimentar.'),
        (2, 'Cocer el boniato pelado en agua con sal 18 minutos, escurrir y triturar '
            'con la mantequilla y la nata calientes. Pasar por colador fino.'),
        (3, 'Pochar la cebolla en juliana a fuego suave 25 minutos, sin coger color.'),
        (4, 'Desglasar la cebolla con el Pedro Ximénez, reducir a la mitad, añadir el '
            'caldo de carne y reducir hasta napar. Colar.'),
        (5, 'Marcar el solomillo en plancha muy caliente 2 minutos por cara.'),
        (6, 'Terminar en horno a 180 °C hasta 58 °C en el centro '
            '(punto al punto). Reposar 4 minutos antes de cortar.'),
        (7, 'Crujiente de panceta: horno a 170 °C, 12 minutos entre dos papeles.'),
        (8, 'Montar: base de puré caliente, solomillo cortado en dos medallones, salsa '
            'alrededor, crujiente de panceta y brotes de rúcula.'),
    ],
    # Un «Punto de control» por paso (columna F de la hoja «Ficha (ejemplo)»):
    # lo que hay que COMPROBAR antes de seguir, no una repetición del paso.
    'puntos_control': [
        (1, 'Salpimentado uniforme y sin jugo en la bandeja: el solomillo pierde '
            'el frío de cámara al tacto.'),
        (2, 'El puré pasa por el colador sin grumos y sale a 63 °C o más.'),
        (3, 'Cebolla transparente y blanda, sin ningún punto dorado.'),
        (4, 'La salsa napa el dorso de una cuchara y sale colada, sin grumos.'),
        (5, 'Marca dorada uniforme en las dos caras, sin jugo en la plancha.'),
        (6, 'Sonda al centro: 58 °C antes del reposo.'),
        (7, 'Panceta dorada y crujiente entre los dos papeles, sin quemarse en '
            'los bordes.'),
        (8, 'Peso de la ración y foto de referencia.'),
    ],
    'tecnicas': 'Plancha, horno, pochado, reducción y triturado fino',
    'tiempos': {
        'mise_en_place_min': 45,
        'pase_min': 9,
        'reposo_min': 4,
    },
    'punto': 'Al punto: 58 °C en el centro de la pieza tras el reposo',
    'temperatura_servicio_c': 63,
    'nota_temperatura': ('Si el plato o alguno de sus componentes se mantiene en '
                         'caliente antes de servir, la temperatura no puede bajar de '
                         '63 °C (CE-10, RD 1086/2020 art. 30.2). '
                         'Verificado el 06-09-2026 - '
                         'https://www.boe.es/buscar/act.php?id=BOE-A-2020-15872'),
    'montaje': ('Plato hondo de 26 cm. Puré en el centro con la cuchara, dos medallones '
                'apoyados en diagonal, salsa por fuera del puré, crujiente de pie y '
                'cinco brotes. Foto de referencia en la hoja.'),
    # ALERGENOS DE PROCESO (SPEC D5). Estados: «Presente», «Traza en esta
    # elaboración», «Utensilio o superficie compartidos», «No interviene».
    # columnas: alérgeno, estado en esta elaboración, dónde entra, sustitución posible
    'alergenos_proceso': [
        ('Leche', 'Presente', 'Mantequilla y nata del puré de boniato',
         'Sí: puré ligado con aceite de oliva virgen extra y agua de cocción'),
        ('Sulfitos', 'Presente', 'Vino Pedro Ximénez de la salsa',
         'Sí: reducción de caldo de carne sin vino, con un punto de miel'),
        ('Apio', 'Traza en esta elaboración',
         'Puede venir en el caldo de carne comercial: comprobar la ficha del proveedor',
         'Sí: caldo de carne propio sin apio'),
        ('Gluten', 'Utensilio o superficie compartidos',
         'La misma plancha tuesta el pan del servicio',
         'Sí: marcar en sartén limpia reservada'),
        ('Frutos de cáscara', 'No interviene', '', ''),
        ('Mostaza', 'No interviene', '', ''),
    ],
    'nota_alergenos': ('Esta tabla es de PROCESO: dice dónde entra cada alérgeno en '
                       'ESTA elaboración y si se puede sustituir. La declaración de '
                       'carta (los 14 alérgenos por plato, para el cliente) se hace en '
                       'la matriz de alérgenos del Pack APPCC; no se duplica aquí. '
                       'El cartel de «consulte al personal» no basta sin soporte '
                       'escrito (CE-06, MM-31).'),
    'conservacion': [
        ('Puré de boniato', 'Refrigeración a 4 °C, tapado', 3),
        ('Salsa de Pedro Ximénez', 'Refrigeración a 4 °C', 4),
        ('Crujiente de panceta', 'Ambiente, en hermético con desecante', 2),
        ('Solomillo racionado', 'Refrigeración a 4 °C', 2),
    ],
    'vida_util_nota': ('No existe una cifra legal general de días de vida útil para una '
                       'elaboración propia (CE-37). Los días de esta tabla son de la '
                       'casa y salen de las pruebas hechas en el propio local; si el '
                       'plato favorece el crecimiento de Listeria hay que documentar un '
                       'estudio de vida útil (CE-08).'),
}


# ==========================================================================
# 7. LA BRIGADA: PUESTOS DEL CONVENIO Y MATRIZ RACI (libro 4)
# ==========================================================================
# Los DIEZ puestos del área funcional 2.a (Cocina y economato) del ALEH VI, con
# su grupo profesional y las funciones LITERALES del art. 17.B. La modificación
# del 04-09-2026 (BOE-A-2026-18630) normaliza el lenguaje de genero pero NO toca
# estas funciones.
#
# columnas: puesto, grupo profesional, funciones literales (art. 17.B),
#           nivel de delegación, quien lo ocupa en La Encina
FUENTE_ALEH_ART17 = ('ALEH VI, art. 17.B (BOE-A-2023-6344) - las FUNCIONES de '
                     'esta columna no las toca la Resolución de 25-08-2026 '
                     '(BOE-A-2026-18630, BOE de 04-09-2026), que solo '
                     'normaliza el lenguaje de género en los NOMBRES de los '
                     'puestos de los arts. 15 a 17. Verificado el 06-09-2026 '
                     '- consolidado (art. 17.B): '
                     'https://www.boe.es/buscar/act.php?id=BOE-A-2023-6344 '
                     '- resolución de 2026: '
                     'https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-18630')

PUESTOS_ALEH = [
    ('Jefe/a de cocina', 'Grupo I',
     'Realizar de manera cualificada, funciones de planificación, organización y control '
     'de todas las tareas propias del departamento de cocina y repostería. Organizar, '
     'dirigir y coordinar el trabajo del personal a su cargo. Dirigir y planificar el '
     'conjunto de actividades de su área. Realizar inventarios y controles de materiales, '
     'mercancías, etc. Diseñar platos y participar en su elaboración. Realizar propuestas '
     'de pedidos de mercancías y materias primas y gestionar su conservación, '
     'almacenamiento y rendimiento. Supervisar y controlar el mantenimiento y uso de '
     'maquinaria, materiales, utillaje, etc. Colaborar en la instrucción del personal a '
     'su cargo',
     'Cualificado, autónomo y responsable', 'P02'),
    ('Segundo/a jefe/a de cocina', 'Grupo I',
     'Realizar de manera cualificada las funciones de planificación, organización y '
     'control de todas las tareas propias del departamento de cocina y repostería. '
     'Colaborar y sustituir al jefe/a de cocina en las tareas propias del mismo',
     'Cualificado, autónomo y responsable', ''),
    ('Jefe/a de catering', 'Grupo I',
     'Realizar de manera cualificada y responsable de la dirección, control y seguimiento '
     'del proceso de elaboración y distribución de comidas. Organizar, controlar y '
     'coordinar todo el proceso de preparación y distribución de la producción a su cargo. '
     'Cuidar de que la producción reuna las condiciones exigidas, tanto higiénicas como de '
     'montaje. Organizar, instruir y evaluar al personal a su cargo',
     'Cualificado, autónomo y responsable', ''),
    ('Jefe/a de partida', 'Grupo II',
     'Realizar de manera cualificada las funciones de control y supervisión de la partida '
     'y/o servicio que le sea asignado bajo la dirección del jefe/a de cocina. Las mismas '
     'del cocinero/a, y además: participar en el control de aprovisionamientos, '
     'conservación y almacenamiento de mercancías. Elaborar informes sobre la gestión de '
     'los recursos y procesos de su partida y/o servicio. Colaborar en la instrucción del '
     'personal a su cargo',
     'Cualificado, autónomo y responsable', ''),
    ('Cocinero/a', 'Grupo II',
     'Realizar de manera cualificada, autónoma y responsable, la preparación, aderezo y '
     'presentación de platos utilizando las técnicas más idóneas. Colaborar en los pedidos '
     'y conservación de materias primas. Colaborar en la planificación de menús y cartas. '
     'Colaborar en la gestión de costes e inventarios, así como en las compras',
     'Cualificado, autónomo y responsable', 'P04, P05'),
    ('Repostero/a', 'Grupo II',
     'Realizar de manera cualificada y autónoma, la preparación y presentación de postres '
     'y dulces en general, así como bollería y masas. Realizar el cálculo de costes, '
     'relacionados con sus cometidos. Organizar y controlar el personal a su cargo',
     'Cualificado, autónomo y responsable', ''),
    ('Encargado/a de economato', 'Grupo II',
     'Realizar de forma cualificada la dirección, control y supervisión del conjunto de '
     'tareas que se desarrollan en su departamento. Establecer las necesidades de '
     'mercancías y material. Elaborar las peticiones de ofertas, evaluación y '
     'recomendación de las adjudicaciones. Controlar y planificar las existencias, en '
     'coordinación con otras secciones del establecimiento',
     'Cualificado, autónomo y responsable', ''),
    ('Ayudante/a de cocina', 'Grupo II',
     'Participar con alguna autonomía y responsabilidad en las elaboraciones de cocina '
     'bajo supervisión. Realizar las preparaciones básicas, así como cualquier otra '
     'relacionada con las elaboraciones culinarias que le sean encomendadas',
     'Con alguna autonomía, bajo supervisión', 'P06, P07'),
    ('Ayudante/a de economato', 'Grupo II',
     'Realizar de manera cualificada, autónoma y responsable, la compra y gestión de '
     'mercancías y materiales. Recibir las mercancías y material pedidos y controlar las '
     'fechas de caducidad. Vigilar y controlar las existencias',
     'Con alguna autonomía, bajo supervisión', ''),
    ('Auxiliar de cocina y economato', 'Grupo III',
     'Realizar sin cualificación las tareas de limpieza de útiles, maquinaria y menaje del '
     'restaurante y cocina, para lo cual no requiere una formación específica y que trabaja '
     'bajo supervisión. Preparar e higienizar los alimentos. Transportar pedidos',
     'Sin cualificación, bajo supervisión', 'P12'),
]

# Los tres niveles de delegación salen del propio convenio, no de una escala
# inventada por el chef: es la lectura que vale por todo el capitulo 04.
NIVELES_DELEGACION = [
    ('Cualificado, autónomo y responsable',
     'Jefe/a de cocina, segundo/a, jefe/a de catering, jefe/a de partida, cocinero/a, '
     'repostero/a y encargado/a de economato',
     'Se le encarga el RESULTADO. No se supervisa el cómo'),
    ('Con alguna autonomía, bajo supervisión',
     'Ayudante/a de cocina y ayudante/a de economato',
     'Se le encarga la TAREA con el estándar escrito delante, y se comprueba'),
    ('Sin cualificación, bajo supervisión',
     'Auxiliar de cocina y economato',
     'Se le enseña la tarea, se hace con el la primera vez y se comprueba siempre'),
]

# «Chef ejecutivo», «chef corporativo» y «sous chef» NO son categorías del ALEH
# VI: son denominaciones de USO. Quien las lleva se clasifica por las funciones
# que hace, y por eso el manual da la equivalencia.
# columnas: denominación de uso, está en el convenio, puesto del ALEH equivalente
DENOMINACIONES_USO = [
    ('Chef ejecutivo', False, 'Jefe/a de cocina (Grupo I, área 2.ª)'),
    ('Chef corporativo', False,
     'No existe en el ALEH VI. Quien dirige varias cocinas se encuadra por las funciones '
     'que hace: normalmente jefe/a de cocina del Grupo I, y su relación con cada unidad se '
     'define en el contrato, no en el convenio'),
    ('Sous chef', False, 'Segundo/a jefe/a de cocina (Grupo I, área 2.ª)'),
    ('Chef de partie', False, 'Jefe/a de partida (Grupo II, área 2.ª)'),
    ('Commis', False, 'Ayudante/a de cocina (Grupo II, área 2.ª)'),
    ('Marmitón o pinche', False, 'Auxiliar de cocina y economato (Grupo III, área 2.ª)'),
]

# --- Matriz RACI Cocina - Sala - Dirección (SPEC D11, capitulo 19) ---------
# R = hace · A = responde (uno y solo uno) · C = se le consulta antes ·
# I = se le informa después · "" = no interviene.
ROLES_RACI = ('Chef ejecutivo', 'Segundo/a de cocina', 'Jefe/a de partida',
              'Jefe/a de sala', 'Gerencia', 'Propiedad')

# columnas: decisión, (RACI por rol, en el orden de ROLES_RACI)
RACI = [
    ('Autorizar un 86: retirar un plato de la carta en mitad del servicio',
     ('A', 'R', 'C', 'I', 'I', '')),
    ('Aprobar una ficha técnica nueva antes de subir el plato a la carta',
     ('A', 'R', 'C', 'I', 'I', '')),
    ('Fijar el PVP de un plato nuevo',
     ('C', '', '', 'I', 'R', 'A')),
    ('Aceptar un encargo de grupo de más de 40 comensales',
     ('C', 'I', '', 'R', 'A', 'I')),
    ('Gestionar una incidencia de alérgeno detectada en el pase',
     ('A', 'R', 'R', 'R', 'I', '')),
    ('Comprar fuera de escandallo un producto de temporada sin precio cerrado',
     ('R', 'I', 'C', '', 'A', 'I')),
    ('Cambiar de proveedor en una familia de producto',
     ('R', 'C', 'C', '', 'A', 'I')),
    ('Retirar de la carta un plato con margen bajo pero muy vendido',
     ('R', 'C', 'I', 'C', 'A', 'I')),
    ('Parar el pase por una avería de frío',
     ('A', 'R', 'C', 'I', 'I', '')),
    ('Autorizar horas extraordinarias en cocina un fin de semana',
     ('R', 'C', 'I', '', 'A', 'I')),
    ('Contratar a un cocinero o cocinera',
     ('R', 'C', 'C', '', 'A', 'I')),
    ('Aprobar el menú de un banquete y su producción',
     ('A', 'R', 'C', 'C', 'C', 'I')),
    ('Responder a una reseña que critica un plato',
     ('C', '', '', 'R', 'A', 'I')),
    ('Decidir el destino del excedente de un servicio (donación o doggy bag)',
     ('A', 'R', 'C', 'I', 'C', 'I')),
    ('Modificar el gramaje de un plato que ya está en carta',
     ('A', 'R', 'C', 'I', 'C', '')),
]


# ==========================================================================
# 8. RÚBRICA DE COMPETENCIAS TECNICAS Y EVALUACIÓN (libro 4)
# ==========================================================================
# SIETE competencias, con descriptor de los cinco niveles. Se puntua POR PRUEBA
# PRÁCTICA, no por autoevaluación ni por impresión del jefe.
# columnas: competencia, (descriptor del nivel 1, 2, 3, 4, 5)
COMPETENCIAS_TECNICAS = [
    ('Cortes y manejo de cuchillo', (
        'Corta con inseguridad, tamaño irregular y merma alta; no afila',
        'Corta los formatos básicos con lentitud y regularidad justa',
        'Corta con regularidad y a ritmo de servicio los formatos de su partida',
        'Corta todos los formatos de la carta con merma baja y mantiene el filo',
        'Enseña a cortar, corrige la postura de otros y fija el estándar de corte')),
    ('Cocciones y puntos', (
        'Necesita que le digan el punto y el tiempo en cada pieza',
        'Acierta el punto en las piezas fáciles; falla con las gruesas',
        'Acierta el punto de las piezas de su partida de forma repetible',
        'Acierta el punto de toda la carta y corrige sobre la marcha',
        'Define puntos y tiempos de un plato nuevo y los deja escritos en la ficha')),
    ('Fondos, salsas y bases', (
        'No los elabora',
        'Elabora fondos siguiendo la ficha, con supervisión',
        'Elabora y conserva los fondos y salsas de su partida sin supervisión',
        'Ajusta ligazón, sazón y acidez sin receta y aprovecha recortes',
        'Diseña bases nuevas, las escandalla con el jefe de cocina y las documenta')),
    ('Emplatado y montaje', (
        'El plato no se parece a la foto de la ficha',
        'Reproduce el montaje con la foto delante y despacio',
        'Reproduce el montaje de memoria y a ritmo de pase',
        'Mantiene el montaje idéntico en un servicio de 120 cubiertos',
        'Diseña el montaje de un plato nuevo y hace la foto de la ficha')),
    ('Higiene de manipulación y APPCC en el puesto', (
        'Hay que recordarle los básicos de higiene y de registro',
        'Cumple cuando se le supervisa; olvida registros',
        'Cumple y registra sin que se lo recuerden',
        'Detecta y corrige desviaciones de otros en su partida',
        'Forma a los nuevos en higiene del puesto y prepara la visita de Sanidad')),
    ('Conocimiento y aplicación de la ficha técnica', (
        'No consulta la ficha',
        'Consulta la ficha pero se aparta de gramajes y tiempos',
        'Aplica la ficha de los platos de su partida sin desviaciones',
        'Aplica la ficha de toda la carta y avisa cuando la ficha está mal',
        'Escribe y revisa fichas y forma al equipo en el cambio de carta')),
    ('Gestión de la merma de su partida', (
        'No mide la merma de su partida',
        'Anota la merma cuando se le pide',
        'Anota la merma a diario y conoce el objetivo de su partida',
        'Ajusta la producción para bajar la merma y propone aprovechamientos',
        'Analiza la serie de merma de su partida y presenta el plan de corrección')),
]

# Pesos de cada competencia POR PUESTO (0 a 3). Un peso 0 significa que la
# competencia no aplica a ese puesto y sale de la media ponderada.
# columnas: puesto (uno de PUESTOS_ALEH), pesos en el orden de COMPETENCIAS_TECNICAS
PESOS_COMPETENCIA_PUESTO = [
    ('Jefe/a de cocina',               (2, 3, 3, 3, 3, 3, 3)),
    ('Segundo/a jefe/a de cocina',     (2, 3, 3, 3, 3, 3, 3)),
    ('Jefe/a de partida',              (3, 3, 3, 3, 3, 3, 3)),
    ('Cocinero/a',                     (3, 3, 3, 2, 3, 3, 2)),
    ('Repostero/a',                    (2, 3, 3, 3, 3, 3, 2)),
    ('Ayudante/a de cocina',           (3, 2, 2, 2, 3, 2, 2)),
    ('Auxiliar de cocina y economato', (2, 1, 1, 1, 3, 1, 1)),
]

# Evaluación técnica de LAS DOCE PERSONAS de la plantilla, con la prueba
# práctica de septiembre de 2026. Reglas de coherencia (las verifica `checks()`):
#
#   · el puesto de la rúbrica es el puesto EN LA PARTIDA, no el del contrato:
#     Marta L. (gerente) y Nuria C. (jefa de sala) cubren cocina a nivel 1, y se
#     les evalúa como ayudantes, que es lo que hacen cuando entran;
#   · quien tiene nivel 0 en las TRES partidas de cocina (Pase, Fríos y Postres)
#     no hace la prueba: sus siete casillas van a N/A. Son las cuatro personas de
#     sala pura (P08, P09, P10 y P11). Su evaluación genérica vive en el Kit de
#     Gestión de Personal, no aquí;
#   · la media ponderada va en la banda de su nivel de polivalencia en cocina:
#     nivel 3 -> 3,80 a 5,00 · nivel 2 -> 3,00 a 3,79 · nivel 1 -> 1,80 a 2,99.
#     Eso es el capitulo 18: COBERTURA NO ES COMPETENCIA.
#
# Un dato que cuenta la historia del año: Laura S. (P05) es la mejor técnica de
# la casa y la única que sostiene la partida de fríos, y su nota más baja es
# justo «gestión de la merma de su partida» (3) - la partida cuya merma se
# dispara en las semanas 33, 34 y 35.
#
# columnas: id, puesto de la rúbrica, fecha de la prueba, evaluador,
#           puntuaciones 1-5 en el orden de COMPETENCIAS_TECNICAS (None = N/A)
EVALUACIONES = [
    ('P01', 'Ayudante/a de cocina', '2026-09-02', 'P02', (2, 2, None, 2, 4, 3, None)),
    ('P02', 'Jefe/a de cocina', '2026-09-01', 'Dirección', (4, 5, 5, 4, 5, 5, 4)),
    ('P03', 'Ayudante/a de cocina', '2026-09-02', 'P02', (2, 2, None, 3, 4, 2, None)),
    ('P04', 'Cocinero/a', '2026-09-01', 'P02', (4, 4, 4, 4, 4, 4, 3)),
    ('P05', 'Cocinero/a', '2026-09-01', 'P02', (5, 4, 4, 5, 4, 5, 3)),
    ('P06', 'Ayudante/a de cocina', '2026-09-02', 'P02', (3, 3, 3, 4, 4, 3, 3)),
    ('P07', 'Ayudante/a de cocina', '2026-09-02', 'P02', (4, 4, 4, 5, 4, 4, 3)),
    ('P08', 'No evaluado en la rúbrica de cocina', '', '', (None,) * 7),
    ('P09', 'No evaluado en la rúbrica de cocina', '', '', (None,) * 7),
    ('P10', 'No evaluado en la rúbrica de cocina', '', '', (None,) * 7),
    ('P11', 'No evaluado en la rúbrica de cocina', '', '', (None,) * 7),
    ('P12', 'Auxiliar de cocina y economato', '2026-09-03', 'P02', (2, 2, None, 2, 4, 2, None)),
]

BANDAS_NIVEL_COMPETENCIA = {3: (3.80, 5.00), 2: (3.00, 3.79), 1: (1.80, 2.99)}

# Guion de la prueba práctica: una prueba por competencia. Es lo que convierte
# la rúbrica en una nota defendible delante de quien la recibe.
# columnas: competencia, prueba, minutos, material, qué es un 5, qué es un 1
PRUEBA_PRACTICA = [
    ('Cortes y manejo de cuchillo',
     'Brunoise de 200 g de cebolla, juliana de 200 g de puerro y racionado de un '
     'solomillo de cerdo en medallones de 110 g',
     20, 'Tabla, cuchillo cebollero, puntilla, báscula',
     'Corte regular, dentro de peso en los seis medallones y merma por debajo del '
     'objetivo de la partida, a ritmo',
     'Corte irregular, medallones fuera de peso y merma por encima del doble del objetivo'),
    ('Cocciones y puntos',
     'Marcar y terminar dos solomillos: uno al punto y otro poco hecho, con sonda a la '
     'vista del evaluador',
     25, 'Plancha, horno, sonda calibrada',
     'Los dos puntos clavados con menos de 2 °C de desviación y reposo respetado',
     'Los dos puntos fuera y sin usar la sonda'),
    ('Fondos, salsas y bases',
     'Elaborar la salsa de Pedro Ximénez de la ficha de P1 a partir del fondo del día',
     30, 'Rondon, chino, ficha técnica del plato',
     'Ligazón, sazón y acidez de la ficha, colada y enfriada según conservación',
     'Salsa desligada o quemada, o sin enfriar según el procedimiento'),
    ('Emplatado y montaje',
     'Montar tres raciones seguidas del plato P1 con la foto de la ficha tapada',
     15, 'Vajilla de servicio, ficha con la foto tapada',
     'Los tres platos idénticos entre si y a la foto, en menos de 3 minutos cada uno',
     'Los tres platos distintos entre si o fuera del montaje de la ficha'),
    ('Higiene de manipulación y APPCC en el puesto',
     'Recepción simulada de un pedido de pescado y carne: comprobación, etiquetado y '
     'registro hasta cámara',
     20, 'Termómetro, etiquetas, hojas de registro del plan APPCC',
     'Comprueba temperatura y etiquetado, rechaza lo que procede, registra y coloca por '
     'orden de caducidad',
     'No mide temperatura, no registra o rompe el orden de caducidad'),
    ('Conocimiento y aplicación de la ficha técnica',
     'Ejecutar un plato de otra partida solo con la ficha delante',
     30, 'Ficha técnica del plato, mise en place estándar',
     'Sale igual que el de la partida titular, con gramajes y tiempos de la ficha',
     'Se aparta de gramajes o tiempos sin darse cuenta'),
    ('Gestión de la merma de su partida',
     'Analizar la serie de cuatro semanas de merma de su partida y proponer dos acciones '
     'con su ahorro estimado',
     20, 'Cuadro de mando de cocina, hoja de la partida',
     'Identifica la causa real, propone dos acciones concretas y estima el ahorro con la '
     'herramienta',
     'No sabe cuál es el objetivo de su partida ni de dónde sale su merma'),
]

# Planes de desarrollo individual. Los dos primeros enlazan literalmente con el
# Plan de Cross-Training del Manual del Manager (P06 hacia fríos el 15-10-2026 y
# P12 hacia pase el 31-01-2027): el PDI NO repite ese plan, lo remite.
# columnas: id, objetivo, competencias a trabajar (indices de COMPETENCIAS_TECNICAS),
#           acciones, responsable, fecha objetivo, estado, remite a
PDI = [
    ('P06',
     'Sostener la partida de fríos en un servicio de 75 cubiertos (nivel 2)',
     (0, 5, 6),
     'Dos servicios por semana en fríos con P05 al lado; ejecutar los cuatro entrantes con '
     'la ficha delante; anotar merma a diario durante seis semanas',
     'P05', '2026-10-15', 'En curso',
     'Plan de Cross-Training del Manual del Manager, fila 1'),
    ('P12',
     'Cubrir el pase en caliente a nivel 2 antes de la temporada alta',
     (0, 1, 4),
     'Rotación de dos servicios por semana en pase; prueba práctica de cortes y de puntos '
     'en enero',
     'P04', '2027-01-31', 'Planificado',
     'Plan de Cross-Training del Manual del Manager, fila 7'),
    ('P05',
     'Subir de 3 a 4 en gestión de la merma de su partida tras el verano',
     (6,),
     'Analizar las semanas 33, 34 y 35 con el cuadro de mando; fijar producción diaria de '
     'fríos con la lista de producción; revisión quincenal con el jefe de cocina',
     'P02', '2026-11-30', 'En curso',
     'Cuadro de mando de cocina, hoja Semana'),
    ('P04',
     'Preparar el paso a jefe de partida de caliente',
     (3, 6),
     'Llevar el pase de los viernes y sábados; escribir dos fichas técnicas nuevas de la '
     'carta de otoño; presentar el informe de merma de su partida en la reunión mensual',
     'P02', '2027-03-31', 'Planificado',
     'Fichas de puesto del libro de brigada, «Jefe/a de partida»'),
]


# ==========================================================================
# 9. DESARROLLO DE CARTA Y CONTROL DE CALIDAD DEL PASE (libro 5)
# ==========================================================================
# Carta de otoño-invierno 2026-2027: cinco platos nuevos con sus cinco hitos.
# La fila de la crema de calabaza es la que dispara la alerta del libro: lleva
# más de los 30 días del parámetro «en prueba», se descartó en su tercera
# prueba (24-09, ver PRUEBAS_PLATO) y todavía no tiene ficha cerrada.
# columnas: id, plato, partida, f. probar, f. costear, f. documentar (ficha),
#           f. formar, f. lanzar, estado, ficha cerrada (Sí/No)
#: N1 y N2 llevan «ficha cerrada» = Sí y su fecha de «documentar» (índice 5)
#: alimenta la «Fecha de revisión» de la ficha en el Índice de Fichas del
#: libro 3 (ver `nuevo[5]` en gen_ficha-tecnica-proceso.py::hoja_indice). Esa
#: fecha tiene que caer ANTES de PARAMETROS_COCINA['fecha_corte_normativa']
#: (2026-09-06, la «hoy» del libro) o la «Antigüedad de la ficha (días)» sale
#: negativa, que no tiene sentido para una ficha que ya está cerrada. Cazado
#: el 2026-09-06: un ajuste hecho a mano en el .xlsx publicado en vez de aquí.
CALENDARIO_TEMPORADA = [
    # N1/N2: fichas ya cerradas (documentadas el 22 y el 24 de agosto), con
    # formación hecha y lanzamiento con la carta de otoño (6 de octubre). Los
    # cinco hitos van en orden (probar < costear < documentar < formar <
    # lanzar): el 06-09-2026 el fixer de documentos adelantó sólo «documentar»
    # a agosto y dejó probar/costear en septiembre; se corrige la secuencia entera.
    ('N1', 'Alcachofas confitadas con panceta y yema curada', ESTACIONES[IDX_FRIOS],
     '2026-08-04', '2026-08-11', '2026-08-22', '2026-08-31', '2026-10-06', 'En curso', 'Sí'),
    ('N2', 'Guiso de carrilleras al vino tinto con puré de apionabo', ESTACIONES[IDX_PASE],
     '2026-08-06', '2026-08-13', '2026-08-24', '2026-09-02', '2026-10-06', 'En curso', 'Sí'),
    # Descartado tras su 3.a prueba (24-09): sin fecha de lanzar. El aviso de
    # días en prueba se sigue disparando igual (depende de J='No' y de los
    # días desde la primera prueba, no del estado) - B9 de la refutación xlsx.
    ('N3', 'Crema de calabaza asada con aceite de pipas', ESTACIONES[IDX_FRIOS],
     '2026-07-28', '2026-08-11', '', '', '', 'Descartado', 'No'),
    ('N4', 'Arroz de setas de temporada y castañas', ESTACIONES[IDX_PASE],
     '2026-09-15', '2026-09-22', '2026-09-29', '2026-10-13', '2026-10-20', 'Planificado', 'No'),
    ('N5', 'Tarta de manzana con helado de canela', ESTACIONES[IDX_POSTRES],
     '2026-09-22', '2026-09-29', '2026-10-06', '2026-10-13', '2026-10-20', 'Planificado', 'No'),
]
HITOS_TEMPORADA = ('Probar', 'Costear', 'Documentar', 'Formar', 'Lanzar')

# Registro de pruebas de plato. Un plato entra en carta con 3 pruebas de media.
# columnas: fecha, id, n. de prueba, partida, resultado (1-5),
#           coste estimado por ración, observación, decisión
PRUEBAS_PLATO = [
    ('2026-07-28', 'N3', 1, ESTACIONES[IDX_FRIOS], 3, 1.05,
     'Poco sabor de asado; la calabaza suelta agua al triturar', 'Repetir'),
    ('2026-08-11', 'N3', 2, ESTACIONES[IDX_FRIOS], 3, 1.15,
     'Mejor con asado a 200 °C, pero el aceite de pipas enrancia en dos días',
     'Repetir'),
    ('2026-09-08', 'N1', 1, ESTACIONES[IDX_FRIOS], 4, 3.20,
     'Buen equilibrio; ajustar el punto de la yema curada', 'Repetir'),
    ('2026-09-10', 'N2', 1, ESTACIONES[IDX_PASE], 4, 4.60,
     'Guiso correcto; el puré de apionabo queda basto', 'Repetir'),
    ('2026-09-14', 'N1', 2, ESTACIONES[IDX_FRIOS], 5, 3.05,
     'Yema curada 24 h en sal y azúcar; ración de 4 alcachofas', 'Aprobar'),
    ('2026-09-16', 'N2', 2, ESTACIONES[IDX_PASE], 4, 4.35,
     'Apionabo pasado por colador fino; se reduce la salsa 10 minutos más', 'Repetir'),
    ('2026-09-21', 'N2', 3, ESTACIONES[IDX_PASE], 5, 4.20,
     'Listo para ficha; rinde 12 raciones por olla', 'Aprobar'),
    ('2026-09-24', 'N3', 3, ESTACIONES[IDX_FRIOS], 2, 1.10,
     'Sigue sin diferenciarse de la crema de la competencia', 'Descartar'),
]

# Muestreo del pase: 30 muestras del servicio de la semana 37 (7 a 13 de
# septiembre de 2026). Alimenta los tiempos de pase del libro 1 y el KPI de
# cumplimiento de ficha.
# columnas: fecha, servicio, id del plato, familia, temperatura de emplatado
#           (°C), tiempo de pase (min), conforme a la ficha (Sí/No),
#           devuelto (Sí/No), observación, ¿se mantiene en caliente? (Sí/No)
# El P1 (solomillo con puré) es la ÚNICA elaboración de este juego de datos
# que se sirve desde un hold en caliente durante el servicio fuerte: por eso
# es la única marcada «Sí», y la fila del 10-09 (61 °C) es la que demuestra
# el aviso de B6 de la refutación xlsx: por debajo de los 63 °C del CE-10.
CONTROL_PASE = [
    ('2026-09-08', 'Cena',   'P1', 'Principales', 68, 14.0, 'Sí', 'No', '', 'Sí'),
    ('2026-09-08', 'Cena',   'E2', 'Entrantes',    9,  7.5, 'Sí', 'No', '', 'No'),
    ('2026-09-09', 'Comida', 'P3', 'Principales', 71, 12.5, 'Sí', 'No', '', 'No'),
    ('2026-09-09', 'Comida', 'E1', 'Entrantes',   74,  8.0, 'Sí', 'No', '', 'No'),
    ('2026-09-09', 'Cena',   'P4', 'Principales', 76, 21.0, 'Sí', 'No', 'Arroz, tiempo de ficha', 'No'),
    ('2026-09-09', 'Cena',   'D1', 'Postres',      7,  5.5, 'Sí', 'No', '', 'No'),
    ('2026-09-10', 'Comida', 'P2', 'Principales', 65, 15.5, 'Sí', 'No', '', 'No'),
    ('2026-09-10', 'Comida', 'E3', 'Entrantes',   78,  9.0, 'Sí', 'No', '', 'No'),
    ('2026-09-10', 'Cena',   'P1', 'Principales', 61, 16.0, 'No', 'No',
     'Sale por debajo de 63 °C: se rehace', 'Sí'),
    ('2026-09-10', 'Cena',   'D3', 'Postres',     66,  8.5, 'Sí', 'No', '', 'No'),
    ('2026-09-11', 'Comida', 'E4', 'Entrantes',   72,  9.5, 'Sí', 'No', '', 'No'),
    ('2026-09-11', 'Comida', 'P3', 'Principales', 70, 13.0, 'Sí', 'No', '', 'No'),
    ('2026-09-11', 'Cena',   'P5', 'Principales', 64, 19.5, 'Sí', 'No', '', 'No'),
    ('2026-09-11', 'Cena',   'E2', 'Entrantes',    8,  8.0, 'Sí', 'No', '', 'No'),
    ('2026-09-11', 'Cena',   'D2', 'Postres',     58,  7.0, 'Sí', 'No', '', 'No'),
    ('2026-09-12', 'Comida', 'P1', 'Principales', 69, 15.0, 'Sí', 'No', '', 'Sí'),
    ('2026-09-12', 'Comida', 'E1', 'Entrantes',   75,  8.5, 'No', 'No',
     'Ración de 5 croquetas en vez de 6', 'No'),
    ('2026-09-12', 'Comida', 'D1', 'Postres',      6,  6.0, 'Sí', 'No', '', 'No'),
    ('2026-09-12', 'Cena',   'P4', 'Principales', 77, 22.5, 'Sí', 'No', '', 'No'),
    ('2026-09-12', 'Cena',   'E3', 'Entrantes',   79, 10.5, 'Sí', 'No', '', 'No'),
    ('2026-09-12', 'Cena',   'P2', 'Principales', 66, 17.0, 'Sí', 'No', '', 'No'),
    ('2026-09-12', 'Cena',   'D3', 'Postres',     64,  9.0, 'Sí', 'No', '', 'No'),
    ('2026-09-13', 'Comida', 'P3', 'Principales', 68, 14.5, 'Sí', 'No', '', 'No'),
    ('2026-09-13', 'Comida', 'E4', 'Entrantes',   71, 10.0, 'Sí', 'No', '', 'No'),
    ('2026-09-13', 'Comida', 'P1', 'Principales', 67, 18.0, 'No', 'Sí',
     'Punto pasado: el cliente lo devuelve', 'Sí'),
    ('2026-09-13', 'Comida', 'D2', 'Postres',     57,  7.5, 'Sí', 'No', '', 'No'),
    ('2026-09-13', 'Cena',   'P5', 'Principales', 63, 20.0, 'Sí', 'No', '', 'No'),
    ('2026-09-13', 'Cena',   'E2', 'Entrantes',    9,  8.5, 'Sí', 'No', '', 'No'),
    ('2026-09-13', 'Cena',   'P4', 'Principales', 75, 23.0, 'No', 'No',
     'Sale 5 minutos por encima del tiempo de ficha', 'No'),
    ('2026-09-13', 'Cena',   'D1', 'Postres',      7,  6.5, 'Sí', 'No', '', 'No'),
]


# ==========================================================================
# 10. COMIDAS TESTIGO Y BANQUETES (libro 6)
# ==========================================================================
# Parámetros legales de las comidas testigo. TODOS vienen del art. 30, apartados
# 8, 9 y 10 del RD 1086/2020 en la redacción del RD 1021/2022 (id CE-11). El
# umbral de 40 comensales es lo que convierte cualquier banquete mediano en una
# obligación legal que casi ningún chef conoce.
PARAMETROS_COMIDA_TESTIGO = {
    'umbral_comensales': 40,
    'gramos_minimos': 100,
    'dias_conservacion': 7,
    'temp_refrigeracion_c': 4,
    'temp_congelacion_c': -18,
    'ce_id': 'CE-11',
    'norma': 'RD 1086/2020, art. 30, apartados 8, 9 y 10 (redacción del RD 1021/2022)',
    'url': 'https://www.boe.es/buscar/act.php?id=BOE-A-2020-15872',
    'verificado': '2026-09-06',
    'supuestos_obligados': [
        'Residencias, hospitales y comedores escolares',
        'Comedores colectivos con menú común',
        'Medios de transporte',
        'Eventos cuando esa sea la actividad principal',
        'Cualquier encargo, de quien sea, para grupos o eventos de más de 40 personas',
    ],
}

# El evento del ejemplo: banquete de boda de 120 comensales el sábado 19 de
# septiembre de 2026. Dispara la obligación (120 > 40). Se elabora y se sirve
# en el mismo establecimiento (jardín de La Encina): el art. 30.9 (doble toma
# de catering entre establecimientos distintos, B3 de la refutación xlsx) no
# se dispara en este caso, y por eso todas las muestras son de «Toma única».
EVENTO_EJEMPLO = {
    'id': 'EV-2026-014',
    'nombre': 'Banquete de boda',
    'fecha': '2026-09-19',
    'comensales': 120,
    'hora_servicio': '14:30',
    'ubicacion_muestras': 'Cámara 3 (postres), balda superior, caja rotulada COMIDAS TESTIGO',
    'responsable': 'P02',
    'fecha_destruccion': '2026-09-26',
    # Art. 30.9 RD 1086/2020: si la elaboración y el servicio se hacen en
    # establecimientos distintos, hacen falta DOS tomas (salida del obrador y
    # servicio). Aquí las dos cosas pasan en la misma cocina.
    'elaboracion_servicio_distintos': 'No',
}

# columnas: id de muestra, id del plato o elaboración, plato, lote,
#           fecha y hora de recogida, gramos, ubicación, temperatura (°C),
#           fecha de destrucción prevista, responsable, momento de la toma
#           (Salida del obrador / En el servicio / Toma única - art. 30.9)
COMIDAS_TESTIGO = [
    ('CT-2026-014-1', 'E1', 'Croquetas de jamón ibérico', 'L260918-CRO',
     '2026-09-19 14:20', 120, 'Cámara 3, balda superior', 4, '2026-09-26', 'P02',
     'Toma única'),
    ('CT-2026-014-2', 'E2', 'Ensalada de tomate rosa, ventresca y cebolleta', 'L260919-TOM',
     '2026-09-19 14:20', 110, 'Cámara 3, balda superior', 4, '2026-09-26', 'P02',
     'Toma única'),
    ('CT-2026-014-3', 'E6', 'Alcachofas confitadas con jamón', 'L260918-ALC',
     '2026-09-19 14:25', 105, 'Cámara 3, balda superior', 4, '2026-09-26', 'P05',
     'Toma única'),
    ('CT-2026-014-4', 'P1', 'Solomillo de cerdo ibérico con puré de boniato', 'L260919-SOL',
     '2026-09-19 15:10', 130, 'Cámara 3, balda superior', 4, '2026-09-26', 'P04',
     'Toma única'),
    ('CT-2026-014-5', 'P2', 'Bacalao confitado al pil-pil', 'L260919-BAC',
     '2026-09-19 15:10', 115, 'Cámara 3, balda superior', 4, '2026-09-26', 'P04',
     'Toma única'),
    ('CT-2026-014-6', 'D1', 'Tarta de queso cremosa', 'L260918-TAR',
     '2026-09-19 16:00', 100, 'Congelador 1, cesta 2', -18, '2026-09-26', 'P07',
     'Toma única'),
]

# Ficha de producción del MISMO evento. La producción por partida sale del menú
# y de los 120 comensales; no es una cifra suelta.
# columnas: momento del menú, id del plato, plato, partida, raciones,
#           raciones por unidad de producción, unidades de producción
BANQUETE_MENU = [
    ('Aperitivo',  'E1', 'Croquetas de jamón ibérico (6 ud)', ESTACIONES[IDX_FRIOS], 120, 30, 4),
    ('Aperitivo',  'E6', 'Alcachofas confitadas con jamón',   ESTACIONES[IDX_FRIOS], 120, 40, 3),
    ('Entrante',   'E2', 'Ensalada de tomate rosa, ventresca y cebolleta',
     ESTACIONES[IDX_FRIOS], 120, 20, 6),
    ('Principal 1', 'P2', 'Bacalao confitado al pil-pil',     ESTACIONES[IDX_PASE], 48, 12, 4),
    ('Principal 2', 'P1', 'Solomillo de cerdo ibérico con puré de boniato',
     ESTACIONES[IDX_PASE], 72, 12, 6),
    ('Postre',     'D1', 'Tarta de queso cremosa',            ESTACIONES[IDX_POSTRES], 120, 12, 10),
]

# Timing del evento: de la mise en place al último pase.
# columnas: hora, hito, partida o área, responsable
BANQUETE_TIMING = [
    ('2026-09-18 09:00', 'Recepción de pescado y verdura; comprobación y etiquetado',
     'Economato', 'P06'),
    ('2026-09-18 11:00', 'Masa de croqueta, alcachofas confitadas y tarta de queso',
     ESTACIONES[IDX_FRIOS], 'P05'),
    ('2026-09-18 17:00', 'Desalado del bacalao y racionado del solomillo',
     ESTACIONES[IDX_PASE], 'P04'),
    ('2026-09-19 08:30', 'Puré de boniato, salsa de Pedro Ximénez y fondo de pil-pil',
     ESTACIONES[IDX_PASE], 'P04'),
    ('2026-09-19 10:00', 'Montaje de ensaladas en bandeja y frito de croquetas de prueba',
     ESTACIONES[IDX_FRIOS], 'P05'),
    ('2026-09-19 13:30', 'Aperitivo en el jardin', ESTACIONES[IDX_FRIOS], 'P05'),
    ('2026-09-19 14:20', 'Toma de las comidas testigo del aperitivo y el entrante',
     'Cocina', 'P02'),
    ('2026-09-19 14:30', 'Entrante en mesa', ESTACIONES[IDX_FRIOS], 'P05'),
    ('2026-09-19 15:10', 'Principales en mesa y toma de sus comidas testigo',
     ESTACIONES[IDX_PASE], 'P02'),
    ('2026-09-19 16:00', 'Postre y toma de su comida testigo',
     ESTACIONES[IDX_POSTRES], 'P07'),
    ('2026-09-19 17:30', 'Limpieza, registro APPCC y cierre del evento', 'Cocina', 'P12'),
]

# Personal asignado al evento. Las horas son EXTRA sobre la jornada ordinaria y
# por eso el evento aparece en las horas de cocina de la semana 38.
# columnas: id, puesto en el evento, horas, día
BANQUETE_PERSONAL = [
    ('P02', 'Jefe de cocina: pase y comidas testigo', 11.0, '2026-09-19'),
    ('P04', 'Partida de caliente', 10.0, '2026-09-19'),
    ('P05', 'Partida de fríos y aperitivo', 10.0, '2026-09-19'),
    ('P06', 'Apoyo a caliente y economato', 9.0, '2026-09-19'),
    ('P07', 'Postres y montaje', 8.0, '2026-09-19'),
    ('P12', 'Office y limpieza', 8.0, '2026-09-19'),
]


# ==========================================================================
# 11. AUDITORÍA INTERNA DE COCINA (libro 7)
# ==========================================================================
# 50 puntos en 5 áreas de 10. EXCLUYE a propósito limpieza, plagas y
# temperaturas de cámara: eso es el Pack APPCC, y mezclarlo produciría un
# checklist que no sirve ni para una cosa ni para la otra. Lo que mide esta hoja
# es la DISCIPLINA DE COCINA.
#
# El área de PRL va SEMBRADA con cinco puntos de base legal verificada
# (CE-21, CE-22, CE-23, CE-25 y CE-26), cada uno con su norma y su URL. Así el
# bloque de prevención tiene herramienta sin añadir un octavo libro.
#
# columnas: n., área, punto de control, peso (1-3), id, norma, URL
AREAS_AUDITORIA_COCINA = ('Orden y mise en place',
                          'Aplicación de fichas técnicas',
                          'Mermas por partida',
                          'Prevención de riesgos laborales',
                          'Alérgenos en el pase')

_U486 = 'https://www.boe.es/buscar/act.php?id=BOE-A-1997-8669'
_U773 = 'https://www.boe.es/buscar/act.php?id=BOE-A-1997-12735'
_U1215 = 'https://www.boe.es/buscar/doc.php?id=BOE-A-1997-17824'

AUDITORIA_COCINA = [
    ( 1, AREAS_AUDITORIA_COCINA[0], 'Cada partida tiene su mise en place montada antes de la hora de apertura', 3, '', '', ''),
    ( 2, AREAS_AUDITORIA_COCINA[0], 'Los cubetos están etiquetados con producto y fecha de elaboración', 2, '', '', ''),
    ( 3, AREAS_AUDITORIA_COCINA[0], 'La cámara está ordenada por orden de caducidad y sin producto sin tapar', 3, '', '', ''),
    ( 4, AREAS_AUDITORIA_COCINA[0], 'El pase está despejado y con el material de emplatado a mano', 2, '', '', ''),
    ( 5, AREAS_AUDITORIA_COCINA[0], 'Los cuchillos están afilados y guardados en su soporte, no en el cajon', 2, '', '', ''),
    ( 6, AREAS_AUDITORIA_COCINA[0], 'No hay producto elaborado sin identificar en ninguna partida', 3, '', '', ''),
    ( 7, AREAS_AUDITORIA_COCINA[0], 'El office está al día al empezar el servicio', 2, '', '', ''),
    ( 8, AREAS_AUDITORIA_COCINA[0], 'Las estanterías de seco están rotuladas y sin cajas en el suelo', 1, '', '', ''),
    ( 9, AREAS_AUDITORIA_COCINA[0], 'Cada partida deja su puesto montado para el turno siguiente', 2, '', '', ''),
    (10, AREAS_AUDITORIA_COCINA[0], 'El parte de incidencias del servicio anterior está escrito y leído', 2, '', '', ''),
    (11, AREAS_AUDITORIA_COCINA[1], 'Todos los platos de la carta tienen ficha técnica cerrada y firmada', 3, '', '', ''),
    (12, AREAS_AUDITORIA_COCINA[1], 'La ficha está accesible en la partida que produce el plato', 3, '', '', ''),
    (13, AREAS_AUDITORIA_COCINA[1], 'Los gramajes servidos coinciden con los de la ficha (pesado de 3 raciones)', 3, '', '', ''),
    (14, AREAS_AUDITORIA_COCINA[1], 'El montaje coincide con la foto de la ficha', 2, '', '', ''),
    (15, AREAS_AUDITORIA_COCINA[1], 'La versión de la ficha en la partida es la última revisada', 3, '', '', ''),
    (16, AREAS_AUDITORIA_COCINA[1], 'Las sustituciones de producto están anotadas y comunicadas a sala', 2, '', '', ''),
    (17, AREAS_AUDITORIA_COCINA[1], 'Los platos nuevos no salen a carta sin ficha cerrada', 2, '', '', ''),
    (18, AREAS_AUDITORIA_COCINA[1], 'El tiempo de pase real está dentro del tiempo de la ficha', 3, '', '', ''),
    (19, AREAS_AUDITORIA_COCINA[1], 'Las fichas revisadas en el último trimestre están fechadas', 2, '', '', ''),
    (20, AREAS_AUDITORIA_COCINA[1], 'El equipo sabe dónde está la ficha y la consulta sin pedir permiso', 2, '', '', ''),
    (21, AREAS_AUDITORIA_COCINA[2], 'Cada partida pesa y anota su merma a diario, y el total de la semana se lleva a la hoja Semana del cuadro de mando', 3, '', '', ''),
    (22, AREAS_AUDITORIA_COCINA[2], 'La merma se pesa, no se estima a ojo', 3, '', '', ''),
    (23, AREAS_AUDITORIA_COCINA[2], 'El objetivo de merma de cada partida está escrito y el equipo lo conoce', 2, '', '', ''),
    (24, AREAS_AUDITORIA_COCINA[2], 'Los recortes aprovechables se separan y se usan en la elaboración prevista', 3, '', '', ''),
    (25, AREAS_AUDITORIA_COCINA[2], 'No hay producto caducado ni deteriorado en cámara', 2, '', '', ''),
    (26, AREAS_AUDITORIA_COCINA[2], 'La producción del día sale de la lista, no de la costumbre', 2, '', '', ''),
    (27, AREAS_AUDITORIA_COCINA[2], 'El sobrante del servicio anterior se descuenta de la producción del día', 3, '', '', ''),
    (28, AREAS_AUDITORIA_COCINA[2], 'Las tres semanas de peor merma del trimestre tienen causa escrita', 2, '', '', ''),
    (29, AREAS_AUDITORIA_COCINA[2], 'El excedente apto se gestiona según la jerarquía de la Ley 1/2025', 2, 'CE-31',
     'Ley 1/2025, art. 5.1 y 5.2', 'https://www.boe.es/buscar/act.php?id=BOE-A-2025-6597'),
    (30, AREAS_AUDITORIA_COCINA[2], 'El plato que sale por la puerta se envasa y se registra como marca el protocolo', 2, '', '', ''),
    (31, AREAS_AUDITORIA_COCINA[3],
     'La temperatura del local está dentro del rango que fija la evaluación de riesgos para la '
     'categoría de trabajo de la cocina', 3, 'CE-21', 'RD 486/1997, Anexo III, punto 3', _U486),
    (32, AREAS_AUDITORIA_COCINA[3],
     'Los suelos son fijos, estables y no resbaladizos, sin irregularidades ni pendientes peligrosas',
     3, 'CE-22', 'RD 486/1997, Anexo I, punto 3, apartado 1.º', _U486),
    (33, AREAS_AUDITORIA_COCINA[3],
     'Hay guante de protección mecánica y calzado antideslizante para todo el que los necesita, '
     'entregados gratuitamente y repuestos', 3, 'CE-23', 'RD 773/1997, art. 3.c) y Anexo III', _U773),
    (34, AREAS_AUDITORIA_COCINA[3],
     'Cortadora, picadora y batidora tienen sus resguardos puestos y en uso',
     3, 'CE-25', 'RD 1215/1997, Anexo I, punto 1.8', _U1215),
    (35, AREAS_AUDITORIA_COCINA[3],
     'Las comprobaciones periódicas de los equipos están documentadas y conservadas',
     3, 'CE-26', 'RD 1215/1997, art. 4', _U1215),
    (36, AREAS_AUDITORIA_COCINA[3], 'Las freidoras se vacían y se filtran en frío, con el procedimiento escrito', 2, '', '', ''),
    (37, AREAS_AUDITORIA_COCINA[3], 'El botiquín está completo y hay quien sepa usarlo en cada turno', 2, '', '', ''),
    (38, AREAS_AUDITORIA_COCINA[3], 'Las cargas pesadas se mueven con ayuda o con carro; nadie levanta solo lo que no debe', 3, 'CE-24',
     'RD 487/1997, Anexo, puntos 1 a 5 (la norma no fija ninguna cifra en kilos)',
     'https://www.boe.es/buscar/act.php?id=BOE-A-1997-8670'),
    (39, AREAS_AUDITORIA_COCINA[3], 'Los pasillos de cocina están libres y las zonas mojadas señalizadas', 2, '', '', ''),
    (40, AREAS_AUDITORIA_COCINA[3], 'La formación de PRL del puesto está hecha y acreditada para toda la brigada', 2, 'CE-27',
     'Ley 31/1995, art. 19 (el coste nunca recae en el trabajador)',
     'https://www.boe.es/buscar/act.php?id=BOE-A-1995-24292'),
    (41, AREAS_AUDITORIA_COCINA[4], 'La comanda con alergia llega marcada a cocina y se canta en voz alta', 3, '', '', ''),
    (42, AREAS_AUDITORIA_COCINA[4], 'El plato con alergia se elabora con material limpio y reservado', 3, 'CE-01',
     'Reglamento (CE) 852/2004, Anexo II, Cap. IX, punto 9',
     'https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02004R0852-20210324'),
    (43, AREAS_AUDITORIA_COCINA[4], 'El plato con alergia sale identificado y se entrega en mano a la mesa', 3, '', '', ''),
    (44, AREAS_AUDITORIA_COCINA[4], 'Hay soporte escrito de alérgenos accesible, no solo el cartel', 3, 'CE-06',
     'Reglamento (UE) 1169/2011, art. 44.1 y RD 126/2015, art. 6.5',
     'https://www.boe.es/buscar/act.php?id=BOE-A-2015-2293'),
    (45, AREAS_AUDITORIA_COCINA[4], 'Las fichas de proceso indican dónde entra cada alérgeno y su sustitución', 2, '', '', ''),
    (46, AREAS_AUDITORIA_COCINA[4], 'Los cambios de proveedor se revisan por si cambia el alérgeno', 3, '', '', ''),
    (47, AREAS_AUDITORIA_COCINA[4], 'Nadie de la brigada dice «creo que no lleva»: se comprueba o no se sirve', 2, '', '', ''),
    (48, AREAS_AUDITORIA_COCINA[4], 'Las incidencias de alérgenos del trimestre están registradas con su causa', 3, '', '', ''),
    (49, AREAS_AUDITORIA_COCINA[4], 'Si se anuncia un plato sin gluten, hay control del límite y del proceso', 2, 'CE-07',
     'Reglamento (UE) 828/2014, arts. 1 a 3 y 5 (20 mg/kg sin gluten, 100 mg/kg muy bajo en gluten)',
     'https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32014R0828'),
    (50, AREAS_AUDITORIA_COCINA[4], 'La brigada nueva recibe formación de alérgenos antes de tocar el pase', 2, 'CE-04',
     'Reglamento (CE) 852/2004, Anexo II, Cap. XII, punto 1 (formación según la actividad del puesto)',
     'https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02004R0852-20210324'),
]

# Dos auditorías hechas, con puntuación 0-5 en cada uno de los 50 puntos, en el
# orden de AUDITORIA_COCINA. La media ponderada sube (3,09 a 3,55) pero UN área
# EMPEORA: «Mermas por partida», de 3,70 a 2,60 - y no es casualidad, la segunda
# visita es después del agosto en el que la merma de fríos se disparo tres
# semanas seguidas. Eso es lo que una media global esconde y lo que la hoja
# «Resumen por Área» tiene que hacer visible.
# columnas: n. de visita, fecha, auditor, puntuaciones (50)
AUDITORIAS_COCINA_HECHAS = [
    (1, '2026-06-19', 'P02 (autoauditoría)', [
        4, 3, 4, 3, 3, 4, 3, 4, 3, 3,
        3, 3, 2, 3, 3, 2, 3, 2, 3, 3,
        4, 4, 4, 3, 4, 4, 3, 4, 4, 3,
        3, 3, 2, 3, 4, 3, 2, 3, 4, 3,
        3, 3, 2, 3, 3, 2, 3, 2, 3, 4,
    ]),
    (2, '2026-09-04', 'Dirección, con el chef delante', [
        5, 4, 4, 4, 4, 4, 4, 4, 4, 3,
        4, 4, 3, 4, 4, 3, 4, 3, 4, 3,
        3, 3, 2, 2, 3, 3, 2, 3, 3, 2,
        4, 4, 3, 4, 5, 4, 3, 4, 4, 3,
        4, 4, 3, 4, 4, 3, 4, 3, 4, 4,
    ]),
]

# Hoja «Estado Normativo» del libro 7 (SPEC D19). Fecha de corte y URL
# editables: es lo que permite al comprador comprobar por si mismo si algo ha
# cambiado desde que compro el manual, sin creerse nada.
# columnas: norma, estado a la fecha de corte, qué hace el chef, fecha de corte,
#           id, URL
ESTADO_NORMATIVO = [
    ('Reglamento (CE) 852/2004, con la modificación 2021/382',
     'Vigente; la modificación se aplica desde el 24-03-2021',
     'La cultura de seguridad alimentaria es obligación de la dirección, no del último que '
     'entró: hay que poder demostrarla (Cap. XI bis)',
     '2026-09-06', 'CE-02',
     'https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02004R0852-20210324'),
    ('Reglamento (UE) 1169/2011 y RD 126/2015',
     'Vigentes',
     'Los 14 alérgenos, por escrito y accesibles. El cartel de «consulte al personal» no '
     'basta sin soporte escrito',
     '2026-09-06', 'CE-06',
     'https://www.boe.es/buscar/act.php?id=BOE-A-2015-2293'),
    ('Reglamento (UE) 828/2014 (gluten)',
     'Vigente desde el 20-07-2016',
     'Si anuncias un plato «sin gluten» te obligas a 20 mg/kg; «muy bajo en gluten», 100 mg/kg',
     '2026-09-06', 'CE-07',
     'https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32014R0828'),
    ('Reglamento (CE) 2073/2005 (criterios microbiológicos)',
     'Vigente, consolidado a 08-03-2020',
     'Si el plato favorece el crecimiento de Listeria, el estudio de vida útil se documenta: '
     'no hay un número de días fijado por ley',
     '2026-09-06', 'CE-08',
     'https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02005R2073-20200308'),
    ('RD 1086/2020 (redacción del RD 1021/2022), art. 30',
     'Vigente; última actualización 22-12-2022',
     'Las cinco temperaturas y el binomio de enfriamiento van en la ficha de cada plato que '
     'se mantenga o se regenere',
     '2026-09-06', 'CE-10',
     'https://www.boe.es/buscar/act.php?id=BOE-A-2020-15872'),
    ('RD 1086/2020, art. 30, apartados 8, 9 y 10 (comidas testigo)',
     'Vigente',
     'Más de 40 comensales en un encargo: 100 g por elaboración, 7 días, a 4 °C o a '
     '-18 °C, identificada y fechada',
     '2026-09-06', 'CE-11',
     'https://www.boe.es/buscar/act.php?id=BOE-A-2020-15872'),
    ('RD 1021/2022, art. 11 (elaboración propia)',
     'Vigente desde el 22-12-2022',
     'La mención es voluntaria; fraccionar, envasar, deshuesar carne fresca o limpiar pescado '
     'NO es elaboración',
     '2026-09-06', 'CE-12',
     'https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681'),
    ('RD 1021/2022, art. 8 (anisakis)',
     'Vigente. El RD 1420/2006 está DEROGADO con efectos del 22-12-2022',
     'Congelación a -20 °C durante 24 horas, o a -35 °C durante 15 horas, '
     'salvo el pescado de aguas continentales (excluido) y salvo la '
     'acuicultura marina con declaración del operador de origen por lote; '
     'hay que informar al consumidor por cartel o carta-menú. El plazo de '
     'siete días que circula por el sector viene de una norma derogada',
     '2026-09-06', 'CE-14',
     'https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681'),
    ('Orden de 26-01-1989 sobre aceites de fritura, art. 6.3',
     'Vigente (otros artículos derogados por el RD 176/2013)',
     'Por debajo del 25 % de compuestos polares. Se mide, no se mira el color',
     '2026-09-06', 'CE-17',
     'https://www.boe.es/buscar/act.php?id=BOE-A-1989-2265'),
    ('Reglamento (UE) 2023/915 (contaminantes)',
     'Vigente desde mayo de 2023; derogó el Reglamento 1881/2006',
     'Vincula al COMPRAR: es la garantía que se le pide al proveedor, no un análisis de cocina',
     '2026-09-06', 'CE-18',
     'https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32023R0915'),
    ('Reglamento (UE) 2017/2158 (acrilamida)',
     'Vigente desde el 11-04-2018; no nombra a los restaurantes como sujeto obligado',
     'Los niveles de referencia no son un límite sancionable: freír la patata por debajo de '
     '175 °C es la medida práctica',
     '2026-09-06', 'CE-19',
     'https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32017R2158'),
    ('RD 486/1997, Anexo III (temperatura del local)',
     'Vigente, actualizado en 2025',
     'La categoría de trabajo la fija TU evaluación de riesgos, y el Anexo III admite '
     'condicionantes del local: 17-27 °C sedentario, 14-25 °C ligero y sin rango '
     'para el trabajo pesado. La cocina no tiene un rango propio en la norma: el suyo sale de '
     'la evaluación de riesgos del local',
     '2026-09-06', 'CE-21', _U486),
    ('RD 773/1997 (equipos de protección individual)',
     'Vigente, modificado por el RD 1076/2021',
     'El uso regular de cuchillos y los ambientes húmedos están en el Anexo III: el EPI se '
     'entrega gratis y se repone',
     '2026-09-06', 'CE-23', _U773),
    ('Ley 1/2025 de prevención de pérdidas y desperdicio alimentario',
     'Publicada en el BOE el 02-04-2025; las obligaciones del art. 6 son '
     'exigibles desde el 02-04-2026 (DF vigésima)',
     'Las microempresas quedan excluidas de las obligaciones del art. 6, pero el doggy bag del '
     'art. 8 les sigue obligando',
     '2026-09-06', 'CE-33',
     'https://www.boe.es/buscar/act.php?id=BOE-A-2025-6597'),
]


# ==========================================================================
# 12. PIE DE LOS LIBROS
# ==========================================================================
VERSION_LINE = ('Versión 1.0 · septiembre 2026 · '
                'aichef.pro/manual-chef-ejecutivo · info@aichef.pro')
BIO = ('Diseñado por John Guerrero — chef y consultor gastronómico desde 2010 '
       '· johnguerrero.es')
NOTA_DESPROTEGER = ('Para editar la estructura o una celda que no este en '
                    'verde, desprotege la hoja (sin contraseña).')


# ==========================================================================
# 13. FUNCIONES DERIVADAS (lo que usan los constructores)
# ==========================================================================
def _lunes_iso(anio, semana):
    """Lunes de la semana ISO indicada. `date.fromisocalendar` es de Python 3.8
    y aquí se ejecuta también con 3.7."""
    ene4 = dt.date(anio, 1, 4)
    return ene4 - dt.timedelta(days=ene4.isoweekday() - 1) + dt.timedelta(weeks=semana - 1)


def _fecha(s):
    return dt.datetime.strptime(s, '%Y-%m-%d').date()


def raciones_por_cubierto():
    """Raciones que sirve cada partida por cubierto, derivadas de las unidades
    al mes de la carta de la Guía Food Cost. No es una cifra tecleada."""
    fam_partida = {'Entrantes': ESTACIONES[IDX_FRIOS],
                   'Principales': ESTACIONES[IDX_PASE],
                   'Postres': ESTACIONES[IDX_POSTRES]}
    out = {}
    for _id, _n, familia, _c, _p, uds in PLATOS:
        part = fam_partida[familia]
        out[part] = out.get(part, 0) + uds
    cub = float(RESTAURANTE['cubiertos_mes'])
    return dict((k, v / cub) for k, v in out.items())


def mix_venta():
    """Los 12 platos de ejemplo con su partida, su ración y su % de mix. El mix
    NO se teclea: sale de las unidades/mes de la carta y de los cubiertos/mes."""
    por_id = dict((p[0], p) for p in LOS_12)
    cub = float(RESTAURANTE['cubiertos_mes'])
    out = []
    for pid, partida, unidad, peso in MIX_VENTA_PARTIDA:
        _i, nombre, familia, coste, pvp, uds = por_id[pid]
        out.append({'id': pid, 'plato': nombre, 'familia': familia, 'partida': partida,
                    'unidad_racion': unidad, 'peso_racion_kg': peso,
                    'uds_mes': uds, 'mix': uds / cub,
                    'coste_racion': coste, 'pvp_sin_iva': pvp})
    return out


# Los 12 platos del mix, ya resueltos (es lo que leen los constructores).
MIX_VENTA = mix_venta()

# Ficha de producción del banquete: una sola estructura con todo lo que necesita
# la hoja «Producción y Ficha de Banquete» del libro 6.
BANQUETE = {
    'evento': EVENTO_EJEMPLO,
    'cubiertos': EVENTO_EJEMPLO['comensales'],
    'menu': BANQUETE_MENU,
    'timing': BANQUETE_TIMING,
    'personal': BANQUETE_PERSONAL,
    'raciones_por_partida': dict(
        (nombre, sum(f[4] for f in BANQUETE_MENU if f[3] == nombre))
        for nombre in PARTIDAS_PRODUCCION
        if any(f[3] == nombre for f in BANQUETE_MENU)),
    'horas_totales_personal': sum(f[2] for f in BANQUETE_PERSONAL),
}


def horas_contrato_cocina(mes):
    """Horas semanales contratadas de la brigada (área 2.ª del ALEH) en un mes.
    Sale de PLANTILLA, no de una constante: P07 es fijo-discontinuo de marzo a
    noviembre."""
    total = 0
    for p in PLANTILLA:
        if p[3] != AREA_COCINA:
            continue
        if 'discontinuo' in p[5].lower() and mes not in CAMPANA_FIJO_DISCONTINUO:
            continue
        total += p[6]
    return total


def semanas_cocina_calculadas():
    """Recalcula los KPI de cocina de cada semana. Devuelve una lista de dicts."""
    kgr = PARAMETROS_COCINA['kg_racion']
    out = []
    for fila in SEMANA_COCINA:
        (sem, mes, cub, prod, merma, pase, inc, grav, horas, dev, ret) = fila
        kg_prod = 0.0
        kg_merma = 0.0
        merma_pct = []
        for j, (nombre, produce, _q, _e) in enumerate(PARTIDAS):
            if not produce or prod[j] is None:
                merma_pct.append(None)
                continue
            kg = prod[j] * kgr[nombre]
            kg_prod += kg
            kg_merma += merma[j]
            merma_pct.append(merma[j] / kg if kg else None)
        out.append({
            'semana': sem, 'mes': mes, 'lunes': _lunes_iso(2026, sem), 'cubiertos': cub,
            'produccion': prod, 'merma_kg': merma, 'merma_pct': merma_pct,
            'kg_producidos': kg_prod, 'kg_merma': kg_merma,
            'merma_global': (kg_merma / kg_prod) if kg_prod else None,
            'pase_entrantes': pase[0], 'pase_principales': pase[1], 'pase_postres': pase[2],
            'incidencias': inc, 'gravedad_max': grav,
            'incidencias_1000': 1000.0 * inc / cub,
            'horas_cocina': horas, 'horas_por_cubierto': horas / float(cub),
            'devueltos': dev, 'retrabajados': ret,
            'devueltos_1000': 1000.0 * dev / cub,
            'retrabajados_1000': 1000.0 * ret / cub,
        })
    return out


def media_ponderada_evaluacion(id_persona):
    """Media ponderada de la evaluación técnica, ignorando los N/A (que es
    distinto de puntuar 0). Devuelve None si no se hizo la prueba."""
    pesos_por_puesto = dict(PESOS_COMPETENCIA_PUESTO)
    for pid, puesto, _f, _ev, punt in EVALUACIONES:
        if pid != id_persona:
            continue
        if puesto not in pesos_por_puesto:
            return None
        pesos = pesos_por_puesto[puesto]
        num = sum(p * w for p, w in zip(punt, pesos) if p is not None and w > 0)
        den = sum(w for p, w in zip(punt, pesos) if p is not None and w > 0)
        return (num / float(den)) if den else None
    return None


def nivel_cocina(id_persona):
    """Nivel máximo de polivalencia de una persona en las TRES partidas de
    cocina (pase, fríos y postres). Sale de la matriz del Manual del Manager."""
    idx = [ESTACIONES.index(p) for p in PARTIDAS_COCINA]
    for pid, niveles in POLIVALENCIA:
        if pid == id_persona:
            return max(niveles[i] for i in idx)
    return None


def kpi_mes_unidad_referencia():
    """Los KPI de agosto de 2026 de La Encina, recalculados desde SEMANA_COCINA.
    Es lo que la hoja «Comparativa entre Unidades» debe mostrar en su fila de
    referencia: no se teclean."""
    sc = [s for s in semanas_cocina_calculadas() if s['semana'] in UNIDADES_MES['semanas']]
    cub = sum(s['cubiertos'] for s in sc)
    kg = sum(s['kg_producidos'] for s in sc)
    mm = sum(s['kg_merma'] for s in sc)
    return {
        'cubiertos': cub,
        'merma_global': mm / kg,
        'pase_principales': sum(s['pase_principales'] for s in sc) / float(len(sc)),
        'incidencias_1000': 1000.0 * sum(s['incidencias'] for s in sc) / cub,
        'horas_por_cubierto': sum(s['horas_cocina'] for s in sc) / float(cub),
        'devueltos_1000': 1000.0 * sum(s['devueltos'] for s in sc) / cub,
    }


# ==========================================================================
# 14. VERIFICACIÓN
# ==========================================================================
def checks():
    fallos = []
    avisos = []

    def exige(cond, mensaje):
        if not cond:
            fallos.append(mensaje)

    ids = [p[0] for p in PLANTILLA]

    # ---- 0. WinAnsi: todo el fichero tiene que caber en cp1252 -----------
    try:
        with open(os.path.abspath(__file__), 'rb') as fh:
            fuente = fh.read().decode('utf-8')
        fuente.encode('cp1252')
    except UnicodeEncodeError as e:
        fallos.append('Hay un carácter fuera de WinAnsi (cp1252) en la posición %d: %r'
                      % (e.start, fuente[max(0, e.start - 30):e.start + 30]))
    except IOError:
        avisos.append('No se pudo releer el fichero para el gate de WinAnsi')

    # ---- 1. contrato con el Manual del Manager (SPEC D8) -----------------
    exige(len(PLANTILLA) == 12, 'La plantilla importada no tiene 12 personas')
    exige(len(ESTACIONES) == 6, 'El Manual del Manager ya no declara 6 unidades')
    exige(len(SEMANAS) == 52, 'El año semanal del Manager ya no tiene 52 filas')
    exige([p[0] for p in PARTIDAS] == list(ESTACIONES),
          'PARTIDAS ya no reproduce las 6 unidades del Manual del Manager')
    exige(all(p[3].startswith('Equivale a la columna') for p in PARTIDAS),
          'Alguna partida se ha quedado sin su nota de equivalencia (SPEC D9)')
    exige(len(PARTIDAS_PRODUCCION) == PARAMETROS_COCINA['partidas_con_produccion'],
          'Las partidas que producen no son las que declara PARAMETROS_COCINA')
    exige(PARAMETROS_COCINA['partidas_activas'] == len(PARTIDAS),
          'La celda «partidas activas» no coincide con las partidas declaradas')
    exige(len(CONTRATO_ENTRE_MANUALES) == 3,
          'La tabla «qué se copia de dónde» debe tener tres filas (SPEC D8)')
    exige('estación' in GLOSA_PRIMERA_MENCION and 'partida' in GLOSA_PRIMERA_MENCION,
          'La glosa de la primera mención tiene que dar las dos palabras (SPEC D9)')
    exige('estación' in NOTA_EQUIVALENCIA_PARTIDA and 'Manual del Manager' in NOTA_EQUIVALENCIA_PARTIDA,
          'La nota de equivalencia del libro 4 no es la de la SPEC D9')
    exige(MIX_VENTA == mix_venta(), 'MIX_VENTA no es el mix resuelto de los 12 platos')
    exige(BANQUETE['cubiertos'] == EVENTO_EJEMPLO['comensales'] and
          BANQUETE['menu'] is BANQUETE_MENU and BANQUETE['timing'] is BANQUETE_TIMING and
          BANQUETE['personal'] is BANQUETE_PERSONAL,
          'La ficha BANQUETE no reune el evento, el menú, el timing y el personal')
    exige(sum(BANQUETE['raciones_por_partida'].values()) ==
          sum(f[4] for f in BANQUETE_MENU),
          'Las raciones por partida del banquete no suman las del menú')

    # ---- 2. contrato con la Guía Food Cost -------------------------------
    exige(len(LOS_12) == 12, 'Los 12 platos de ejemplo de la Guía ya no son 12')
    exige(len(PLATOS) == 20, 'La carta de la Guía Food Cost ya no tiene 20 platos')
    exige(abs(coste_ficha() - FICHA_TECNICA_EJEMPLO['coste_racion_copiado']) < 0.005,
          'El coste copiado en la ficha técnica ya no es el de la ficha de escandallo')
    exige(FICHA_TECNICA_EJEMPLO['plato'] == FICHA['plato'],
          'La ficha técnica de ejemplo no es la del plato escandallado en la Guía')

    # ---- 3. las 52 semanas de cocina -------------------------------------
    sc = semanas_cocina_calculadas()
    exige(len(SEMANA_COCINA) == 52, 'El año de cocina no tiene 52 filas')
    exige([s['semana'] for s in sc] == list(range(1, 53)),
          'Las semanas ISO de cocina no van de 1 a 52 en orden')
    # cubiertos: idénticos a los del Manager, semana a semana (desviación 0 %)
    desajustes = [(SEMANA_COCINA[i][0], SEMANA_COCINA[i][2], SEMANAS[i][9])
                  for i in range(52)
                  if SEMANA_COCINA[i][2] != SEMANAS[i][9] or SEMANA_COCINA[i][0] != SEMANAS[i][0]
                  or SEMANA_COCINA[i][1] != SEMANAS[i][1]]
    exige(not desajustes,
          'Los cubiertos (o el mes) de cocina no coinciden con los del Manager: %s' % desajustes[:3])
    cub_cocina = sum(s['cubiertos'] for s in sc)
    cub_manager = sum(f[9] for f in SEMANAS)
    exige(cub_cocina == cub_manager,
          'Los cubiertos anuales de cocina (%d) no son los del Manager (%d)' % (cub_cocina, cub_manager))
    exige(abs(cub_cocina - RESTAURANTE['cubiertos_mes'] * 12) / float(RESTAURANTE['cubiertos_mes'] * 12) <= 0.03,
          'Los cubiertos anuales se apartan más del 3 %% de los 3.900/mes del caso modelado')

    # producción coherente con la carta
    rc = raciones_por_cubierto()
    for nombre in PARTIDAS_COCINA:
        j = ESTACIONES.index(nombre)
        prod = sum(s['produccion'][j] for s in sc)
        esperado = cub_cocina * rc[nombre]
        d = 100.0 * (prod / esperado - 1.0)
        exige(abs(d) <= 3.0,
              'La producción anual de «%s» se desvia %.2f %% de la carta de la Guía (tope 3 %%)'
              % (nombre, d))
    for s in sc:
        for j, (nombre, produce, _q, _e) in enumerate(PARTIDAS):
            if produce:
                exige(s['produccion'][j] is not None and s['merma_kg'][j] is not None,
                      'La partida «%s» produce y le falta dato en la semana %d' % (nombre, s['semana']))
            else:
                exige(s['produccion'][j] is None and s['merma_kg'][j] is None,
                      'La partida «%s» no produce y trae dato en la semana %d' % (nombre, s['semana']))

    # Horas de cocina coherentes con la plantilla. Una semana suelta puede cerrar
    # POR DEBAJO de la jornada contratada (vacaciones, permisos y libranzas), igual
    # que le pasa al año semanal del Manual del Manager; lo que no puede es
    # despegarse del contrato ni del reparto cocina/sala de la casa.
    for s in sc:
        contrato = horas_contrato_cocina(s['mes'])
        exige(contrato * 0.90 <= s['horas_cocina'] <= contrato * 1.30,
              'La semana %d tiene %d h de cocina y el contrato de la brigada son %d h'
              % (s['semana'], s['horas_cocina'], contrato))
    for i, s in enumerate(sc):
        cuota = s['horas_cocina'] / float(SEMANAS[i][12])
        exige(0.44 <= cuota <= 0.52,
              'La semana %d dedica a cocina el %.1f %% de las horas trabajadas del Manager, '
              'y la brigada es el %.1f %% de la jornada contratada de la casa'
              % (s['semana'], 100 * cuota,
                 100.0 * horas_contrato_cocina(s['mes']) / sum(p[6] for p in PLANTILLA)))
    horas_anio = sum(s['horas_cocina'] for s in sc)
    contrato_anio = sum(horas_contrato_cocina(s['mes']) for s in sc)
    exige(0.97 <= horas_anio / float(contrato_anio) <= 1.08,
          'Las horas de cocina del año (%d) no cuadran con el contrato de la brigada (%d)'
          % (horas_anio, contrato_anio))
    # la brigada es la de área 2.ª del Manager: ni una persona más ni una menos
    cocina_ids = [p[0] for p in PLANTILLA if p[3] == AREA_COCINA]
    exige(len(cocina_ids) == 6,
          'El área 2.ª de la plantilla del Manager ya no tiene 6 personas: %s' % cocina_ids)

    # las cuatro semanas malas y sus dos historias
    obj = PARAMETROS_COCINA['objetivos']
    j_frios = ESTACIONES.index(ESTACIONES[IDX_FRIOS])
    malas_frios = [s['semana'] for s in sc
                   if s['merma_pct'][j_frios] > 1.5 * obj['merma_' + ESTACIONES[IDX_FRIOS]]]
    exige(tuple(malas_frios) == SEMANAS_MERMA_FRIOS,
          'La merma de fríos debería dispararse en las semanas %s y se dispara en %s'
          % (str(SEMANAS_MERMA_FRIOS), str(tuple(malas_frios))))
    exige(malas_frios == sorted(malas_frios) and
          malas_frios[-1] - malas_frios[0] == len(malas_frios) - 1,
          'Las semanas de merma de fríos no son consecutivas (situación 7 del bonus)')
    peor_pase = max(sc, key=lambda s: s['pase_principales'])
    exige(peor_pase['semana'] == SEMANA_PASE_DESCONTROLADO,
          'La peor semana de pase es la %d y el bonus cuenta la %d'
          % (peor_pase['semana'], SEMANA_PASE_DESCONTROLADO))
    exige(max(s['gravedad_max'] for s in sc) == 3,
          'No hay ninguna incidencia de alérgenos de gravedad 3 en todo el año')
    exige([s['semana'] for s in sc if s['gravedad_max'] == 3] == [SEMANA_PASE_DESCONTROLADO],
          'La incidencia grave de alérgenos no cae en la semana del pase descontrolado')
    exige(set(SEMANAS_MALAS_COCINA) & set(SEMANAS_FUERA_DE_OBJETIVO),
          'Ninguna semana mala de cocina coincide con las que el Manager ve fuera de objetivo')
    # las medias del año quedan dentro de objetivo: el problema es puntual
    exige(sum(s['kg_merma'] for s in sc) / sum(s['kg_producidos'] for s in sc) <= 0.05,
          'La merma global del año se sale de lo razonable para el caso modelado')
    exige(horas_anio / float(cub_cocina) <= obj['horas_cocina_cubierto'],
          'Las horas de cocina por cubierto del año superan el objetivo de la casa')

    # ---- 4. KPI y parámetros ---------------------------------------------
    exige(len(KPI_COCINA) == 7, 'Los KPI de cocina deben ser SIETE (SPEC D10)')
    exige(all(len(k) == 5 and all(k) for k in KPI_COCINA),
          'Algun KPI se ha quedado sin fórmula, unidad, error típico o cadencia')
    exige(len(set(k[0] for k in KPI_COCINA)) == 7, 'Hay dos KPI de cocina con el mismo nombre')
    exige(set(PARAMETROS_COCINA['kg_racion']) == set(PARTIDAS_PRODUCCION),
          'El peso por ración no cubre exactamente las partidas que producen')
    exige(PARAMETROS_COCINA['tipo_carta'] in PARAMETROS_COCINA['tipos_carta_lista'],
          'El tipo de carta del caso no está en la lista de validación')
    exige(PARAMETROS_COCINA['fecha_corte_normativa'] == '2026-09-06',
          'La fecha de corte normativa de este producto es el 06-09-2026')

    # ---- 5. comparativa entre unidades (SPEC D6) -------------------------
    exige(len(UNIDADES) == 3, 'La comparativa no tiene 3 unidades')
    ref = kpi_mes_unidad_referencia()
    fila = UNIDADES[0]
    exige(fila[1] == ref['cubiertos'],
          'Los cubiertos de agosto de la unidad de referencia (%d) no son los de SEMANA_COCINA (%d)'
          % (fila[1], ref['cubiertos']))
    for pos, clave, tol in ((2, 'merma_global', 0.0001), (3, 'pase_principales', 0.05),
                            (4, 'incidencias_1000', 0.005), (5, 'horas_por_cubierto', 0.0005),
                            (6, 'devueltos_1000', 0.005)):
        exige(abs(fila[pos] - ref[clave]) <= tol,
              'La unidad de referencia declara %s = %s y SEMANA_COCINA da %.4f'
              % (clave, fila[pos], ref[clave]))
    exige(len(ESTANDAR_GRUPO) == 5, 'El estándar de grupo no tiene los 5 indicadores')
    mejores = [u for u in UNIDADES if u[2] < ESTANDAR_GRUPO['merma_global']]
    peores = [u for u in UNIDADES if u[2] > ESTANDAR_GRUPO['merma_global']]
    exige(mejores and peores,
          'La comparativa no separa ninguna unidad del estándar del grupo: no enseña nada')

    # ---- 6. planificación de producción ----------------------------------
    exige(len(PREVISION_CUBIERTOS) == 12,
          'La previsión debe tener los 12 servicios de la semana (6 días x 2)')
    exige(not any(p[0] == 'Lunes' for p in PREVISION_CUBIERTOS),
          'La Encina cierra los lunes: no puede haber previsión de ese día')
    prev = sum(p[4] for p in PREVISION_CUBIERTOS)
    fila_37 = [s for s in sc if s['semana'] == SEMANA_TIPO_PREVISION][0]
    exige(prev == fila_37['cubiertos'],
          'La previsión de la semana tipo suma %d cubiertos y la semana %d tiene %d'
          % (prev, SEMANA_TIPO_PREVISION, fila_37['cubiertos']))
    exige(all(p[2] <= p[4] for p in PREVISION_CUBIERTOS),
          'Hay un servicio con más reservas confirmadas que cubiertos previstos')
    exige(0.45 <= sum(p[2] for p in PREVISION_CUBIERTOS) / float(prev) <= 0.75,
          'El peso de las reservas sobre la previsión no es creíble')

    mv = mix_venta()
    exige(len(mv) == 12, 'El mix de venta no trae los 12 platos de la Guía Food Cost')
    exige(len(set(m['id'] for m in mv)) == 12, 'Hay un plato repetido en el mix de venta')
    exige(all(m['partida'] in PARTIDAS_PRODUCCION for m in mv),
          'Hay un plato asignado a una partida que no produce')
    exige(0.90 <= sum(m['mix'] for m in mv) <= 1.05,
          'El mix de los 12 platos no cuadra con los cubiertos del mes')
    for nombre in PARTIDAS_COCINA:
        filas = [m for m in mv if m['partida'] == nombre]
        if not filas:
            continue
        peso_medio = (sum(m['peso_racion_kg'] * m['uds_mes'] for m in filas) /
                      float(sum(m['uds_mes'] for m in filas)))
        kgr = PARAMETROS_COCINA['kg_racion'][nombre]
        exige(abs(peso_medio - kgr) / kgr <= 0.15,
              'El peso medio de ración de «%s» (%.3f kg) no cuadra con el parámetro (%.3f kg)'
              % (nombre, peso_medio, kgr))
    exige(len(STOCK_ELABORADO) == 12, 'El stock elaborado no cubre los 12 platos del mix')
    exige([s[0] for s in STOCK_ELABORADO] == [m['id'] for m in mv],
          'El stock elaborado no sigue el orden de los 12 platos del mix')
    for s in STOCK_ELABORADO:
        exige(s[3] >= 0, 'Stock elaborado negativo en %s' % s[0])
        if s[3] > 0:
            _fecha(s[4])
            exige(s[5] > 0, 'Hay stock de %s sin vida útil declarada' % s[0])

    # ---- 7. ficha técnica de proceso (SPEC D4 y D5) ----------------------
    ft = FICHA_TECNICA_EJEMPLO
    exige(len(ft['pasos']) >= 6, 'La ficha técnica de ejemplo tiene menos de 6 pasos')
    exige([p[0] for p in ft['pasos']] == list(range(1, len(ft['pasos']) + 1)),
          'Los pasos de la ficha técnica no están numerados en orden')
    exige(len(ft['puntos_control']) == len(ft['pasos']),
          'La ficha técnica de ejemplo no trae un punto de control por cada paso')
    exige([p[0] for p in ft['puntos_control']] == list(range(1, len(ft['puntos_control']) + 1)),
          'Los puntos de control de la ficha técnica no están numerados en orden')
    exige(all(p[1].strip() for p in ft['puntos_control']),
          'Hay un punto de control vacío en la ficha técnica de ejemplo')
    exige('copiado' in ft['nota_coste'].lower() or 'copiad' in ft['nota_coste'].lower(),
          'La nota del coste no dice que es una COPIA del escandallo (SPEC D4)')
    exige(ft['temperatura_servicio_c'] == 63,
          'La temperatura de servicio en caliente de la ficha debe ser 63 °C (CE-10)')
    exige('CE-10' in ft['nota_temperatura'] and 'boe.es' in ft['nota_temperatura'],
          'La nota de temperatura no lleva su id y su URL verificados')
    estados = set(a[1] for a in ft['alergenos_proceso'])
    exige(estados <= {'Presente', 'Traza en esta elaboración',
                      'Utensilio o superficie compartidos', 'No interviene'},
          'Hay un estado de alérgeno de proceso fuera de los cuatro previstos: %s' % estados)
    exige(len(ft['alergenos_proceso']) < 14,
          'La ficha de proceso no puede traer la declaración de carta completa (SPEC D5)')
    exige(any(a[1] == 'Presente' for a in ft['alergenos_proceso']) and
          any(a[1] == 'Utensilio o superficie compartidos' for a in ft['alergenos_proceso']),
          'La ficha de proceso no enseña los estados que la diferencian de la matriz de carta')
    exige('APPCC' in ft['nota_alergenos'] or 'Pack APPCC' in ft['nota_alergenos'],
          'La nota de alérgenos no remite a la matriz de alérgenos del Pack APPCC (SPEC D5)')
    exige(ft['partida'] in PARTIDAS_PRODUCCION, 'La ficha de ejemplo apunta a una partida que no produce')

    # ---- 8. brigada, RACI y denominaciones -------------------------------
    exige(len(PUESTOS_ALEH) == 10, 'El área 2.ª del ALEH VI tiene 10 puestos, no %d' % len(PUESTOS_ALEH))
    exige(all(p[1] in ('Grupo I', 'Grupo II', 'Grupo III') for p in PUESTOS_ALEH),
          'Hay un puesto con un grupo profesional que no es I, II o III')
    exige(all(len(p[2]) > 120 for p in PUESTOS_ALEH),
          'Hay un puesto sin sus funciones literales del art. 17')
    exige(len(set(p[0] for p in PUESTOS_ALEH)) == 10, 'Hay un puesto del ALEH repetido')
    niveles_dec = set(p[3] for p in PUESTOS_ALEH)
    exige(niveles_dec == set(n[0] for n in NIVELES_DELEGACION),
          'Los niveles de delegación de los puestos no son los tres del convenio')
    ocupados = set()
    for p in PUESTOS_ALEH:
        for pid in [x.strip() for x in p[4].split(',') if x.strip()]:
            exige(pid in ids, 'El puesto «%s» lo ocupa %s, que no está en la plantilla' % (p[0], pid))
            ocupados.add(pid)
    exige(ocupados == set(cocina_ids),
          'Los puestos ocupados (%s) no son las 6 personas del área 2.ª (%s)'
          % (sorted(ocupados), sorted(cocina_ids)))
    nombres_aleh = set(p[0] for p in PUESTOS_ALEH)
    exige('Chef corporativo' not in nombres_aleh,
          '«Chef corporativo» no es un puesto del ALEH VI y no puede estar en PUESTOS_ALEH')
    exige(any(d[0] == 'Chef corporativo' and d[1] is False for d in DENOMINACIONES_USO),
          '«Chef corporativo» tiene que figurar como denominación de uso FUERA del convenio')
    exige(all(d[1] is False for d in DENOMINACIONES_USO),
          'Alguna denominación de uso figura como si estuviera en el convenio')

    exige(12 <= len(RACI) <= 15, 'La matriz RACI debe tener entre 12 y 15 decisiones')
    exige(len(ROLES_RACI) == 6, 'La matriz RACI no tiene los 6 roles')
    for dec, celdas in RACI:
        exige(len(celdas) == 6, 'La decisión «%s» no tiene 6 celdas' % dec[:40])
        exige(all(c in ('R', 'A', 'C', 'I', '') for c in celdas),
              'La decisión «%s» tiene una letra que no es R/A/C/I' % dec[:40])
        exige(list(celdas).count('A') == 1,
              'La decisión «%s» tiene %d responsables últimos y debe tener uno'
              % (dec[:40], list(celdas).count('A')))
        exige('R' in celdas, 'La decisión «%s» no tiene a nadie que la ejecute' % dec[:40])
    exige(sum(1 for _d, c in RACI if c[0] == 'A') >= 5,
          'El chef ejecutivo responde de menos de 5 decisiones: el capitulo 19 se queda sin materia')
    exige(sum(1 for _d, c in RACI if c[4] == 'A') >= 4,
          'La gerencia no responde de ninguna decisión: la frontera con el Manager desaparece')

    # ---- 9. competencias, evaluación, PDI y prueba práctica --------------
    exige(len(COMPETENCIAS_TECNICAS) == 7, 'La rúbrica no tiene 7 competencias')
    exige(all(len(c[1]) == 5 and all(c[1]) for c in COMPETENCIAS_TECNICAS),
          'Alguna competencia no tiene descritos los cinco niveles')
    exige(len(PESOS_COMPETENCIA_PUESTO) == 7, 'Faltan pesos por puesto en la rúbrica')
    exige(all(len(p[1]) == 7 for p in PESOS_COMPETENCIA_PUESTO),
          'Hay un puesto con un número de pesos distinto de 7')
    exige(all(0 <= w <= 3 for p in PESOS_COMPETENCIA_PUESTO for w in p[1]),
          'Hay un peso de competencia fuera de 0-3')
    exige(all(p[0] in nombres_aleh for p in PESOS_COMPETENCIA_PUESTO),
          'Hay un puesto en los pesos de la rúbrica que no es del ALEH VI')

    exige(len(EVALUACIONES) == 12, 'La evaluación técnica no cubre a las 12 personas')
    exige([e[0] for e in EVALUACIONES] == ids, 'La evaluación no sigue el orden de la plantilla')
    for pid, puesto, fecha, evaluador, punt in EVALUACIONES:
        exige(len(punt) == 7, 'La evaluación de %s no tiene 7 puntuaciones' % pid)
        exige(all(p is None or 1 <= p <= 5 for p in punt),
              'Puntuación fuera de 1-5 en la evaluación de %s' % pid)
        nivel = nivel_cocina(pid)
        media = media_ponderada_evaluacion(pid)
        if nivel == 0:
            exige(all(p is None for p in punt),
                  '%s tiene nivel 0 en las partidas de cocina y aun así trae puntuaciones' % pid)
            exige(media is None, '%s no debería tener media: no hace la prueba' % pid)
            exige(fecha == '' and evaluador == '',
                  '%s no hace la prueba y aun así tiene fecha o evaluador' % pid)
        else:
            exige(media is not None, '%s hace la prueba y no tiene media' % pid)
            _fecha(fecha)
            exige(evaluador, 'La evaluación de %s no dice quien la hizo' % pid)
            lo, hi = BANDAS_NIVEL_COMPETENCIA[nivel]
            exige(media is not None and lo <= media <= hi,
                  'La media de %s es %.2f y su nivel de polivalencia (%d) pide entre %.2f y %.2f'
                  % (pid, media if media is not None else -1, nivel, lo, hi))
    evaluados = [e[0] for e in EVALUACIONES if any(p is not None for p in e[4])]
    exige(len(evaluados) == 8,
          'Deberían hacer la prueba las 8 personas con nivel de cocina y la hacen %d' % len(evaluados))
    n_na = sum(1 for e in EVALUACIONES if any(p is not None for p in e[4])
               for p in e[4] if p is None)
    exige(n_na > 0, 'Ninguna casilla N/A en la rúbrica: no se ve el mecanismo que ignora los N/A')
    # la historia de P05: la mejor técnica de la casa suspende en gestión de merma
    p05 = dict((e[0], e[4]) for e in EVALUACIONES)['P05']
    exige(p05[6] == min(p for p in p05 if p is not None),
          'La nota más baja de P05 debería ser la gestión de la merma de su partida')

    exige(3 <= len(PDI) <= 4, 'Los planes de desarrollo individual deben ser 3 o 4')
    exige(all(p[0] in ids for p in PDI), 'Hay un PDI de alguien que no está en la plantilla')
    exige(all(all(0 <= i < 7 for i in p[2]) for p in PDI),
          'Hay un PDI que apunta a una competencia que no existe')
    exige(all(p[5] and _fecha(p[5]) for p in PDI), 'Hay un PDI sin fecha objetivo')
    exige(all(p[7] for p in PDI), 'Hay un PDI que no remite a la herramienta de la que sale')
    # los dos primeros PDI tienen que cuadrar con el Plan de Cross-Training del Manager
    cross = dict((c[0], c) for c in PLAN_CROSS_TRAINING)
    for pid, fecha_esperada in (('P06', cross['P06'][5]), ('P12', cross['P12'][5])):
        fila = [p for p in PDI if p[0] == pid]
        exige(fila and fila[0][5] == fecha_esperada,
              'El PDI de %s debería vencer el %s, como su fila del Plan de Cross-Training del Manager'
              % (pid, fecha_esperada))

    exige(len(PRUEBA_PRACTICA) == 7, 'Falta el guion de prueba de alguna competencia')
    exige([p[0] for p in PRUEBA_PRACTICA] == [c[0] for c in COMPETENCIAS_TECNICAS],
          'Las pruebas prácticas no siguen el orden de las competencias')
    exige(all(p[2] > 0 and p[4] and p[5] for p in PRUEBA_PRACTICA),
          'Hay una prueba práctica sin duración o sin criterio de qué es un 5 y de qué es un 1')

    # ---- 10. desarrollo de carta y control del pase -----------------------
    exige(4 <= len(CALENDARIO_TEMPORADA) <= 6, 'El calendario de temporada debe traer de 4 a 6 platos')
    exige(all(c[2] in PARTIDAS_PRODUCCION for c in CALENDARIO_TEMPORADA),
          'Hay un plato nuevo asignado a una partida que no produce')
    exige(len(HITOS_TEMPORADA) == 5, 'Los hitos del calendario de temporada son cinco')
    corte = _fecha(PARAMETROS_COCINA['fecha_corte_normativa'])
    alerta = []
    for c in CALENDARIO_TEMPORADA:
        exige(c[9] in ('Sí', 'No'), 'La columna «ficha cerrada» solo admite Sí/No')
        if c[3] and c[9] == 'No':
            dias = (corte - _fecha(c[3])).days
            if dias > PARAMETROS_COCINA['dias_max_en_prueba_sin_ficha']:
                alerta.append((c[0], dias))
    exige(len(alerta) == 1,
          'Debería haber exactamente un plato en prueba pasado de plazo sin ficha y hay %d' % len(alerta))
    exige(len(PRUEBAS_PLATO) >= 6, 'El registro de pruebas de plato se ha quedado corto')
    ids_cal = set(c[0] for c in CALENDARIO_TEMPORADA)
    exige(all(p[1] in ids_cal for p in PRUEBAS_PLATO),
          'Hay una prueba de un plato que no está en el calendario de temporada')
    exige(all(1 <= p[4] <= 5 for p in PRUEBAS_PLATO), 'Resultado de prueba fuera de 1-5')
    exige(all(p[7] in ('Repetir', 'Aprobar', 'Descartar') for p in PRUEBAS_PLATO),
          'Hay una decisión de prueba fuera de Repetir/Aprobar/Descartar')
    aprobados = set(p[1] for p in PRUEBAS_PLATO if p[7] == 'Aprobar')
    con_ficha = set(c[0] for c in CALENDARIO_TEMPORADA if c[9] == 'Sí')
    exige(aprobados == con_ficha,
          'Los platos con ficha cerrada (%s) no son los aprobados en las pruebas (%s)'
          % (sorted(con_ficha), sorted(aprobados)))

    exige(len(CONTROL_PASE) >= 25, 'El muestreo del pase se ha quedado corto')
    ids_platos = set(p[0] for p in PLATOS)
    exige(all(m[2] in ids_platos for m in CONTROL_PASE),
          'Hay un muestreo del pase sobre un plato que no está en la carta')
    exige(all(m[6] in ('Sí', 'No') and m[7] in ('Sí', 'No') for m in CONTROL_PASE),
          'Las columnas de conformidad y devolución solo admiten Sí/No')
    conformes = sum(1 for m in CONTROL_PASE if m[6] == 'Sí')
    pct_conf = conformes / float(len(CONTROL_PASE))
    exige(0.80 <= pct_conf <= 0.95,
          'La conformidad del pase (%.0f %%) no deja ver ni el problema ni el estándar' % (100 * pct_conf))
    exige(all(m[7] == 'No' or m[6] == 'No' for m in CONTROL_PASE),
          'Hay un plato devuelto que figura como conforme con la ficha')
    calientes = [m for m in CONTROL_PASE if m[3] == 'Principales']
    frios_pase = [m for m in CONTROL_PASE if m[4] < 15]
    exige(any(m[4] < 63 for m in calientes),
          'Ningún principal sale por debajo de 63 °C: el ejemplo no enseña la desviación')
    exige(frios_pase, 'No hay ningún muestreo de plato frío: el termómetro solo mira al caliente')
    for m in CONTROL_PASE:
        if m[3] == 'Principales' and m[4] < 63:
            exige(m[6] == 'No',
                  'El muestreo de %s a %d °C figura como conforme y está por debajo de 63'
                  % (m[2], m[4]))
    exige(all(m[9] in ('Sí', 'No') for m in CONTROL_PASE),
          'La columna «¿se mantiene en caliente?» solo admite Sí/No (B6 de la refutación xlsx)')
    exige(any(m[9] == 'Sí' and m[4] < 63 for m in CONTROL_PASE),
          'Ninguna muestra que se mantiene en caliente está por debajo de 63 °C: '
          'B6 de la refutación xlsx no queda demostrado')

    # ---- 11. comidas testigo y banquete (CE-11) ---------------------------
    pct = PARAMETROS_COMIDA_TESTIGO
    exige(pct['umbral_comensales'] == 40 and pct['gramos_minimos'] == 100
          and pct['dias_conservacion'] == 7 and pct['temp_refrigeracion_c'] == 4
          and pct['temp_congelacion_c'] == -18,
          'Los parámetros de comidas testigo no son los del art. 30.8-30.10 (CE-11)')
    exige(pct['ce_id'] == 'CE-11' and 'boe.es' in pct['url'] and pct['verificado'] == '2026-09-06',
          'Los parámetros de comidas testigo no llevan id, URL y fecha de verificación')
    exige(len(pct['supuestos_obligados']) == 5,
          'Faltan supuestos obligados de comidas testigo (art. 30.8)')
    exige(EVENTO_EJEMPLO['comensales'] > pct['umbral_comensales'],
          'El evento de ejemplo no dispara la obligación: no enseña nada')
    exige((_fecha(EVENTO_EJEMPLO['fecha_destruccion']) - _fecha(EVENTO_EJEMPLO['fecha'])).days
          == pct['dias_conservacion'],
          'La fecha de destrucción del evento no respeta los 7 días de conservación')
    exige(len(COMIDAS_TESTIGO) >= 5, 'Hay menos muestras que elaboraciones servidas en el evento')
    for m in COMIDAS_TESTIGO:
        exige(m[5] >= pct['gramos_minimos'],
              'La muestra %s tiene %d g y el mínimo legal son %d g' % (m[0], m[5], pct['gramos_minimos']))
        exige(m[7] in (pct['temp_refrigeracion_c'], pct['temp_congelacion_c']),
              'La muestra %s se guarda a %s °C, que no es ni 4 ni -18' % (m[0], m[7]))
        exige((_fecha(m[8]) - _fecha(EVENTO_EJEMPLO['fecha'])).days >= pct['dias_conservacion'],
              'La muestra %s se destruye antes de los 7 días' % m[0])
        exige(m[9] in ids, 'La muestra %s la guarda alguien que no está en la plantilla' % m[0])
        exige(m[1] in ids_platos, 'La muestra %s no corresponde a un plato de la carta' % m[0])
        exige(m[10] in ('Salida del obrador', 'En el servicio', 'Toma única'),
              'La muestra %s tiene un momento de la toma que no es de la lista (art. 30.9)' % m[0])
    if EVENTO_EJEMPLO['elaboracion_servicio_distintos'] == 'No':
        exige(all(m[10] == 'Toma única' for m in COMIDAS_TESTIGO),
              'El evento se elabora y sirve en el mismo establecimiento: no debería '
              'haber ninguna muestra con doble toma (art. 30.9)')
    exige(any(m[7] == pct['temp_congelacion_c'] for m in COMIDAS_TESTIGO),
          'Ninguna muestra se conserva congelada: no se ve la segunda opción del art. 30')

    raciones_menu = {}
    for _mom, pid, _plato, partida, raciones, por_ud, uds in BANQUETE_MENU:
        exige(pid in ids_platos, 'El menú del banquete lleva un plato que no está en la carta')
        exige(partida in PARTIDAS_PRODUCCION, 'El menú del banquete carga una partida que no produce')
        exige(raciones <= EVENTO_EJEMPLO['comensales'],
              'El plato %s produce más raciones que comensales tiene el evento' % pid)
        exige(por_ud * uds >= raciones,
              'Las unidades de producción de %s no llegan a las raciones del menú' % pid)
        raciones_menu[partida] = raciones_menu.get(partida, 0) + raciones
    principales = sum(r for _m, _p, _n, _pa, r, _u, _x in BANQUETE_MENU if _m.startswith('Principal'))
    exige(principales == EVENTO_EJEMPLO['comensales'],
          'Los principales del banquete suman %d raciones y hay %d comensales'
          % (principales, EVENTO_EJEMPLO['comensales']))
    exige(len(BANQUETE_TIMING) >= 8, 'El timing del banquete se ha quedado corto')
    horas_timing = [t[0] for t in BANQUETE_TIMING]
    exige(horas_timing == sorted(horas_timing), 'El timing del banquete no va en orden cronológico')
    exige(any('testigo' in t[1].lower() for t in BANQUETE_TIMING),
          'El timing del banquete no incluye la toma de las comidas testigo')
    exige(all(p[0] in cocina_ids for p in BANQUETE_PERSONAL),
          'Hay alguien en el banquete que no es de la brigada de cocina')
    exige(len(BANQUETE_PERSONAL) == len(cocina_ids),
          'El banquete no moviliza a toda la brigada de cocina')

    # ---- 12. auditoría interna de cocina ---------------------------------
    exige(len(AUDITORIA_COCINA) == 50, 'La auditoría de cocina no tiene 50 puntos')
    exige([a[0] for a in AUDITORIA_COCINA] == list(range(1, 51)),
          'Los puntos de la auditoría no van de 1 a 50')
    exige(all(a[1] in AREAS_AUDITORIA_COCINA for a in AUDITORIA_COCINA),
          'Hay un punto de auditoría en un área desconocida')
    for area in AREAS_AUDITORIA_COCINA:
        exige(sum(1 for a in AUDITORIA_COCINA if a[1] == area) == 10,
              'El área «%s» no tiene 10 puntos' % area)
    exige(all(1 <= a[3] <= 3 for a in AUDITORIA_COCINA), 'Peso de auditoría fuera de 1-3')
    prohibidas = ('plaga', 'desratiz', 'desinsect', 'temperatura de cámara', 'legionela')
    for a in AUDITORIA_COCINA:
        low = a[2].lower()
        for pal in prohibidas:
            exige(pal not in low,
                  'El punto %d entra en territorio del Pack APPCC («%s»)' % (a[0], pal))
    prl = [a for a in AUDITORIA_COCINA if a[1] == 'Prevención de riesgos laborales']
    sembrados = set(a[4] for a in prl if a[4])
    exige({'CE-21', 'CE-22', 'CE-23', 'CE-25', 'CE-26'} <= sembrados,
          'El área de PRL no está sembrada con los cinco ids verificados: %s' % sorted(sembrados))
    for a in AUDITORIA_COCINA:
        if a[4]:
            exige(a[5] and a[6].startswith('http'),
                  'El punto %d cita el id %s sin norma o sin URL' % (a[0], a[4]))
    for a in prl:
        if a[4] == 'CE-21':
            exige('evaluación de riesgos' in a[2].lower(),
                  'El punto de temperatura no puede afirmar que la cocina tenga un rango '
                  'legal propio: la categoría la fija la evaluación de riesgos (SPEC D15b)')
    for a in AUDITORIA_COCINA:
        exige('25 kg' not in a[2] and '25 kilos' not in a[2],
              'El punto %d repite el mito de los 25 kg (CE-24)' % a[0])

    exige(len(AUDITORIAS_COCINA_HECHAS) == 2, 'No hay 2 auditorías de cocina hechas')
    exige(all(len(v[3]) == 50 for v in AUDITORIAS_COCINA_HECHAS),
          'Alguna visita no tiene 50 puntuaciones')
    exige(all(all(0 <= x <= 5 for x in v[3]) for v in AUDITORIAS_COCINA_HECHAS),
          'Puntuación de auditoría fuera de 0-5')
    pesos_aud = [a[3] for a in AUDITORIA_COCINA]
    pond = [sum(p * s for p, s in zip(pesos_aud, v[3])) / float(sum(pesos_aud))
            for v in AUDITORIAS_COCINA_HECHAS]
    exige(pond[0] < pond[1], 'La auditoría de cocina no mejora entre la visita 1 y la 2')
    por_area = {}
    for area in AREAS_AUDITORIA_COCINA:
        idx = [i for i, a in enumerate(AUDITORIA_COCINA) if a[1] == area]
        por_area[area] = [sum(v[3][i] for i in idx) / float(len(idx))
                          for v in AUDITORIAS_COCINA_HECHAS]
    empeoran = [a for a, m in por_area.items() if m[1] < m[0]]
    exige(len(empeoran) == 1,
          'Debería empeorar exactamente un área entre las dos visitas y empeoran %d' % len(empeoran))
    exige(empeoran and empeoran[0] == 'Mermas por partida',
          'El área que empeora debería ser la de mermas, que es la que cuenta el agosto de fríos')
    exige(_fecha(AUDITORIAS_COCINA_HECHAS[1][1]) > _lunes_iso(2026, max(SEMANAS_MERMA_FRIOS)),
          'La segunda auditoría es anterior a las semanas de merma disparada: la historia no cuadra')

    # ---- 13. estado normativo --------------------------------------------
    exige(10 <= len(ESTADO_NORMATIVO) <= 14,
          'El estado normativo debe traer entre 10 y 14 normas y trae %d' % len(ESTADO_NORMATIVO))
    exige(all(e[3] == PARAMETROS_COCINA['fecha_corte_normativa'] for e in ESTADO_NORMATIVO),
          'Alguna fila del estado normativo no lleva la fecha de corte del producto')
    exige(all(e[4].startswith('CE-') for e in ESTADO_NORMATIVO),
          'Alguna fila del estado normativo no referencia un id CE-*')
    exige(len(set(e[4] for e in ESTADO_NORMATIVO)) == len(ESTADO_NORMATIVO),
          'Hay un id repetido en el estado normativo')
    exige(all(e[5].startswith('http') for e in ESTADO_NORMATIVO),
          'Alguna fila del estado normativo no lleva URL')
    exige(all(e[1] and e[2] for e in ESTADO_NORMATIVO),
          'Alguna fila del estado normativo no dice ni el estado ni qué hace el chef')

    # ---- 14. lista negra de la SPEC §8 sobre TODO el texto del fichero ----
    try:
        texto = fuente
    except NameError:
        texto = ''
    # Las agujas se arman por TROZOS a propósito: si se escribieran enteras, este
    # mismo gate se dispararía contra su propio codigo fuente.
    negras = [
        (('49', ',9'), 'la comparación salarial prohibida por la SPEC D16'),
        (('la temperatura ', 'legal de la cocina'), 'prohibido por la SPEC D15b'),
        (('-20 °C ', 'durante 7 días'), 'el anisakis nunca son 7 días (CE-14)'),
        (('RD 1420/2006 ', 'está vigente'), 'el RD 1420/2006 está derogado'),
        (('RD 3484/2000 ', 'está vigente'), 'el RD 3484/2000 está derogado'),
        (('110 € ', 'los dos manuales'), 'los dos manuales son 120 €'),
        (('estacion', ' a aprender'), 'el término único es «partida» (SPEC D9)'),
    ]
    for trozos, motivo in negras:
        aguja = ''.join(trozos)
        exige(aguja not in texto, 'Aparece «%s» en el fichero: %s' % (aguja, motivo))
    exige(texto.count('estacion') <= 30,
          'La palabra «estación» aparece demasiadas veces: el término único es «partida» (SPEC D9)')

    # ---- 15. pie ----------------------------------------------------------
    exige('manual-chef-ejecutivo' in VERSION_LINE and 'info@aichef.pro' in VERSION_LINE,
          'La linea de versión no apunta a este producto')
    exige('johnguerrero.es' in BIO, 'La bio no lleva la marca personal anclada')
    exige('desproteg' in NOTA_DESPROTEGER, 'Falta la nota de desproteger la hoja')

    # ---- resumen ---------------------------------------------------------
    print('=' * 78)
    print('MANUAL DEL CHEF EJECUTIVO - juego de datos de la cocina de «La Encina»')
    print('=' * 78)
    print('CONTRATO CON LOS HERMANOS (SPEC D8)')
    print('  Manual del Manager .... %d personas · %d unidades · %d semanas ISO · SS empresa %.0f %%'
          % (len(PLANTILLA), len(ESTACIONES), len(SEMANAS), 100 * SS_EMPRESA))
    print('  Guía Food Cost ........ %d platos en carta · 12 de ejemplo · ficha P1 a %.2f €/ración'
          % (len(PLATOS), coste_ficha()))
    print('')
    print('PARTIDAS (SPEC D9: el término único es «partida»)')
    for nombre, produce, que, _eq in PARTIDAS:
        print('  %-22s %s  %s' % (nombre, 'produce raciones' if produce else 'sin producción ',
                                  que[:44]))
    print('')
    print('BRIGADA (área 2.ª del ALEH VI)')
    for pid in cocina_ids:
        p = [x for x in PLANTILLA if x[0] == pid][0]
        nivel = nivel_cocina(pid)
        media = media_ponderada_evaluacion(pid)
        print('  %s %-12s %-38s nivel %d · rúbrica %s'
              % (pid, p[1], p[2][:38], nivel,
                 ('%.2f' % media) if media is not None else 'N/A'))
    print('  contrato semanal: %d h en campaña (marzo a noviembre) · %d h el resto'
          % (horas_contrato_cocina(6), horas_contrato_cocina(1)))
    print('')
    print('AÑO DE COCINA (52 semanas ISO de 2026)')
    print('  cubiertos %s (idénticos a los del Manager)  ·  horas de cocina %s (%.1f %% sobre contrato)'
          % ('{:,.0f}'.format(cub_cocina).replace(',', '.'),
             '{:,.0f}'.format(horas_anio).replace(',', '.'),
             100.0 * (horas_anio / float(contrato_anio) - 1)))
    print('  horas por cubierto %.3f (objetivo de la casa %.3f)'
          % (horas_anio / float(cub_cocina), obj['horas_cocina_cubierto']))
    print('  merma por partida en el año:')
    for nombre in PARTIDAS_PRODUCCION:
        j = ESTACIONES.index(nombre)
        kg = sum(s['produccion'][j] * PARAMETROS_COCINA['kg_racion'][nombre] for s in sc)
        mm = sum(s['merma_kg'][j] for s in sc)
        o = obj['merma_' + nombre]
        print('    %-22s %7.1f kg producidos · %6.1f kg de merma · %.2f %% (objetivo %.1f %%)'
              % (nombre, kg, mm, 100 * mm / kg, 100 * o))
    print('  incidencias de alérgenos: %d en el año (%.2f por 1.000 cubiertos, objetivo %.2f)'
          % (sum(s['incidencias'] for s in sc),
             1000.0 * sum(s['incidencias'] for s in sc) / cub_cocina,
             obj['incidencias_alergenos_1000']))
    print('  semanas malas de cocina: %s de 52' % ', '.join(str(x) for x in SEMANAS_MALAS_COCINA))
    for s in sc:
        if s['semana'] not in SEMANAS_MALAS_COCINA:
            continue
        dom = s['lunes'] + dt.timedelta(days=6)
        etiqueta = ''
        if s['semana'] in SEMANAS_MERMA_FRIOS:
            etiqueta = '  <- merma de fríos %.1f %% (situación 7 del bonus)' % (100 * s['merma_pct'][IDX_FRIOS])
        elif s['semana'] == SEMANA_PASE_DESCONTROLADO:
            etiqueta = '  <- el pase se descontrola (situación 5 del bonus)'
        print('    semana %2d (%s a %s): pase %.1f min · %d devueltos · %d retrabajados%s'
              % (s['semana'], s['lunes'].strftime('%d-%m'), dom.strftime('%d-%m'),
                 s['pase_principales'], s['devueltos'], s['retrabajados'], etiqueta))
    print('  el Manager ve fuera de objetivo de prime cost las semanas %s'
          % ', '.join(str(x) for x in SEMANAS_FUERA_DE_OBJETIVO))
    print('')
    print('COMPARATIVA ENTRE UNIDADES (agosto de 2026, SPEC D6)')
    for u in UNIDADES:
        print('  %-34s %5d cub · merma %.2f %% · pase %.1f min · %.3f h/cub · %.2f dev/1.000'
              % (u[0], u[1], 100 * u[2], u[3], u[5], u[6]))
    print('  estándar del grupo (objetivo propio): merma %.2f %% · pase %.1f min · %.3f h/cub'
          % (100 * ESTANDAR_GRUPO['merma_global'], ESTANDAR_GRUPO['pase_principales_min'],
             ESTANDAR_GRUPO['horas_cocina_cubierto']))
    print('')
    print('CARTA, PASE Y BANQUETES')
    print('  previsión de la semana %d: %d cubiertos en 12 servicios · reservas %.0f %%'
          % (SEMANA_TIPO_PREVISION, prev,
             100.0 * sum(p[2] for p in PREVISION_CUBIERTOS) / prev))
    print('  calendario de temporada: %d platos nuevos · alerta en %s (%d días en prueba sin ficha)'
          % (len(CALENDARIO_TEMPORADA), alerta[0][0], alerta[0][1]))
    print('  muestreo del pase: %d muestras · conformidad %.0f %% (objetivo %.0f %%)'
          % (len(CONTROL_PASE), 100 * pct_conf, 100 * obj['cumplimiento_ficha']))
    print('  evento %s: %d comensales -> comidas testigo OBLIGATORIAS (CE-11, umbral %d)'
          % (EVENTO_EJEMPLO['id'], EVENTO_EJEMPLO['comensales'], PARAMETROS_COMIDA_TESTIGO['umbral_comensales']))
    print('    %d muestras de %d g mínimo, %d días, a %d o a %d °C'
          % (len(COMIDAS_TESTIGO), PARAMETROS_COMIDA_TESTIGO['gramos_minimos'],
             PARAMETROS_COMIDA_TESTIGO['dias_conservacion'],
             PARAMETROS_COMIDA_TESTIGO['temp_refrigeracion_c'],
             PARAMETROS_COMIDA_TESTIGO['temp_congelacion_c']))
    print('')
    print('BRIGADA, RACI Y AUDITORÍA')
    print('  puestos del ALEH VI: %d · denominaciones de uso fuera del convenio: %d'
          % (len(PUESTOS_ALEH), len(DENOMINACIONES_USO)))
    print('  RACI: %d decisiones · el chef responde de %d, la gerencia de %d'
          % (len(RACI), sum(1 for _d, c in RACI if c[0] == 'A'),
             sum(1 for _d, c in RACI if c[4] == 'A')))
    print('  evaluación técnica: %d de 12 hacen la prueba · %d casillas N/A' % (len(evaluados), n_na))
    print('  auditoría de cocina: media ponderada %.2f -> %.2f · empeora «%s» (%.1f -> %.1f)'
          % (pond[0], pond[1], empeoran[0], por_area[empeoran[0]][0], por_area[empeoran[0]][1]))
    print('  estado normativo: %d normas con fecha de corte %s y URL'
          % (len(ESTADO_NORMATIVO), PARAMETROS_COCINA['fecha_corte_normativa']))
    print('')
    if avisos:
        for a in avisos:
            print('AVISO: %s' % a)
    if fallos:
        print('%d FALLO(S):' % len(fallos))
        for f in fallos:
            print('  x %s' % f)
        raise SystemExit(1)
    print('TODAS LAS COMPROBACIONES EN VERDE.')
    return True


if __name__ == '__main__':
    checks()
