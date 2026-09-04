#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
datos_ejemplo.py — JUEGO DE DATOS ÚNICO del producto «Manual del Manager de
Restaurante» (SPEC: scripts/productos-digitales/manual-manager-SPEC.md, D13).

Los 7 libros de Excel, el guion del manual (`guion_manual_manager_restaurante.py`)
y el bonus «12 situaciones resueltas» usan ESTA plantilla, ESTAS estaciones y
ESTAS semanas. Regla de la familia (§7-bis.7 de guias-v2-SPEC.md): una sola
fuente de cifras. Si un número cambia, cambia aquí y se regeneran los libros.

TODO LO QUE HAY AQUÍ SON DATOS DE EJEMPLO DE UN CASO MODELADO, no de un cliente
real y no de «un restaurante medio». No hay ni una sola cifra «de mercado»
inventada: los datos del sector NO viven en este fichero, se referencian por id
`MM-*` del JSON `auditorias/guias-v2-research-sector.json` (que lleva fuente,
URL y fiabilidad de cada uno) y los recoge el constructor de cada libro. Aquí
sólo aparece el id y, como mucho, el artículo de la norma en una línea: los
textos legales largos NO se copian.

Importes SIN IVA salvo que el nombre de la variable diga lo contrario.

El restaurante es el MISMO que el de la «Guía Food Cost + Ingeniería de Menú»
(`../guia-food-cost/datos_ejemplo.py`): «La Encina», 70 plazas, servicio en
mesa, 52 servicios/mes, 3.900 cubiertos/mes, food cost objetivo 30 %, IVA de
sala 10 %. Lo que este manual añade es la capa de PERSONAS, SERVICIO y LEY:
plantilla de 12, seis estaciones, 52 semanas ISO, quejas, selección,
cumplimiento legal, reuniones y auditoría interna.

CUADRE CON LA GUÍA FOOD COST (lo comprueba `checks()`):
  · el año semanal reproduce el año MENSUAL de la Guía dentro del ±3 % en
    ventas, consumo, compras, salarios y otros costes de personal;
  · la suma de los salarios brutos de las 12 personas, con la Seguridad Social
    a cargo de la empresa, cuadra con el coste de personal mensual de la Guía;
  · el año semanal cuadra en total anual (±3 %) en ventas, consumo, salarios y
    cubiertos.

Ejecutar `python3 datos_ejemplo.py` corre `checks()` e imprime el resumen.
"""

import datetime as dt
import importlib.util
import os

# ==========================================================================
# 1. EL RESTAURANTE MODELADO
# ==========================================================================
# Los seis primeros campos son LITERALMENTE los de la Guía Food Cost
# (`../guia-food-cost/datos_ejemplo.py`, RESTAURANTE). El resto es lo que
# añade el Manual del Manager.
RESTAURANTE = {
    'nombre': 'Restaurante de ejemplo «La Encina»',
    'formato': 'restaurante de carta, servicio en mesa, 70 plazas, ciudad media española',
    'servicios_mes': 52,            # comidas + cenas abiertas en un mes tipo
    'cubiertos_mes': 3900,          # ≈ 75 cubiertos por servicio
    'food_cost_objetivo': 0.30,     # objetivo de la casa (Guía Food Cost)
    'iva_sala': 0.10,

    # --- lo que añade el Manual del Manager -------------------------------
    'tipo_negocio': 'Sala',         # lista del libro 1: «Sala» / «Barra o autoservicio»
    'plazas': 70,
    'dias_apertura': 'De martes a domingo, comida y cena. Cierra los lunes.',
    'servicios_semana': 12,         # 6 días × 2 servicios = 52 servicios/mes
    'horas_apertura_semana': 42,    # 6 días × 7 h de apertura al público (13:00-16:30 y 20:00-23:30)
    # Provincia elegida para el convenio: GIRONA (Cataluña). Se elige una a
    # propósito porque el convenio de hostelería es PROVINCIAL sobre el ALEH VI
    # estatal (MM-14), y porque el plazo de respuesta de la hoja de
    # reclamaciones es autonómico: el de Cataluña (1 mes) es uno de los dos
    # verificados de la SPEC §2.2 libro 3. El manual NO publica las tablas
    # salariales de Girona: manda buscarlas en REGCON. La horquilla
    # Madrid-Barcelona del mismo puesto está en MM-15.
    'provincia': 'Girona',
    'comunidad': 'Cataluña',
    'convenio': ('Convenio provincial de hostelería y turismo de Girona, sobre el ALEH VI estatal '
                 '(BOE-A-2023-6344, modificado por BOE-A-2026-18630). Tablas: consultar en REGCON.'),
    # Objetivos de la casa (celdas verdes del libro 1). El 65 %/55 % es criterio
    # de la casa derivado de la estructura de costes de referencia (MM-41), no
    # una cifra de fuente: SPEC D10.
    'food_cost_objetivo_pct': 0.30,
    'labor_cost_objetivo_pct': 0.33,
    'prime_cost_objetivo_sala': 0.65,
    'prime_cost_objetivo_barra': 0.55,
    # Arranque del plan de 90 días: lunes 7 de septiembre de 2026 = semana ISO 37,
    # el lunes siguiente a la semana 36, que cerró fuera de objetivo (66,8 %).
    'fecha_inicio_plan_90': '2026-09-07',
    'fecha_corte_normativa': '2026-09-04',
}

# Cotización a cargo de la EMPRESA usada en todos los libros (SPEC D5).
# Es una CELDA EDITABLE, nunca una constante dentro de una fórmula.
# Desglose de las partidas que la componen (el porcentaje de AT/EP depende de
# la tarifa de primas del CNAE del local, por eso el total es una horquilla):
#   contingencias comunes ......... 23,60 %  ← es SÓLO esta partida la que
#                                              recoge MM-17; llamarla
#                                              «coste-empresa» es un error
#   desempleo (indefinido) ........  5,50 %
#   FOGASA ........................  0,20 %
#   formación profesional .........  0,60 %
#   AT/EP .........................  según la tarifa de primas de la DA 61.ª TRLGSS
#   MEI 2026 (parte empresarial) ..  0,75 %  (Orden PJC/297/2026, art. 16)
#                                   -------
#   total en hostelería 2026 ...... 32,15 % con indefinido · 33,35 % con temporal (MM-53)
# Fuentes: MM-17 (contingencias comunes y tope de base) y MM-53 (total a cargo
# de la empresa). El 33 % que usan los libros es la convención de familia
# (`kit-gestion-personal/03` y `guia-food-cost/cuadro-de-mando-prime-cost`) y
# cae dentro de esa horquilla; es celda editable.
SS_EMPRESA = 0.33
# M3 (auditoría 2026-09-04): el desglose visible sumaba 30,65 % contra el
# 33 % que usa B22, porque AT/EP se dejaba sin tipo (columna en blanco) y el
# TOTAL no llevaba fórmula. Reconstruido: 23,60+5,50+0,20+0,60+1,50+0,75 =
# 32,15 % exacto (el 1,50 % es la tarifa de primas de la DA 61.ª TRLGSS para
# el CNAE 56 «Servicios de comidas y bebidas»), y 32,15-5,50+6,70 = 33,35 %
# con contrato de duración determinada. El generador ahora escribe el TOTAL
# como SUM($B$25:$B$30) — nunca una constante — para que quien cambie
# cualquier partida vea el total recalcularse solo.
SS_EMPRESA_DESGLOSE = [
    # concepto, tipo, nota
    ('Contingencias comunes', 0.2360, 'A cargo de la empresa (el trabajador aporta el 4,70 %). MM-17'),
    ('Desempleo (contrato indefinido)', 0.0550, 'Los contratos temporales cotizan más'),
    ('FOGASA', 0.0020, ''),
    ('Formación profesional', 0.0060, ''),
    ('Accidentes de trabajo y enfermedades profesionales', 0.0150,
     'Tarifa de primas de la DA 61.ª TRLGSS, epígrafe del CNAE 56 «Servicios de comidas y bebidas»; comprueba el epígrafe de tu actividad'),
    ('MEI 2026 (parte empresarial)', 0.0075, 'Mecanismo de Equidad Intergeneracional. Orden PJC/297/2026, art. 16'),
    ('TOTAL a cargo de la empresa en hostelería 2026', None,
     '32,15 % con contrato indefinido a tiempo completo y 33,35 % con contrato de duración determinada (MM-53). '
     'El 33 % de más arriba (celda editable) redondea esta cifra como convención de la casa (SPEC D5).'),
]

# ==========================================================================
# 2. LA PLANTILLA: 12 PERSONAS
# ==========================================================================
# Puestos y encuadre según el ALEH VI (MM-14): SEIS áreas funcionales y TRES
# grupos profesionales. Aquí sólo aparecen las áreas 1ª, 2ª y 3ª, que son las
# que tiene un restaurante independiente.
#   Área 1ª — Recepción, conserjería, relaciones públicas, administración y gestión
#   Área 2ª — Cocina y economato
#   Área 3ª — Restaurante, sala, bar y similares
#   Grupo I   — jefaturas (jefe de cocina, jefe de sala/maître…)
#   Grupo II  — oficios cualificados (cocinero, camarero…)
#   Grupo III — apoyo (ayudante de cocina, ayudante de camarero, friegaplatos…)
# ⚠ «Encargado», «director», «gerente» y «administrador» son DENOMINACIONES DE
# USO, no categorías del ALEH VI (SPEC D7): quien lleva el local se clasifica
# por las funciones que hace, y el «gerente de centro» que sí nombra el ALEH
# pertenece a restauración moderna, no a un restaurante de carta.
#
# La suma de los salarios brutos anuales es 276.000 €. Con la Seguridad Social
# a cargo de la empresa (33 %) son 30.590 €/mes, que es el coste de personal
# mensual con el que la Guía Food Cost calcula el prime cost de La Encina
# (277.600 € de salarios brutos/año → 30.767 €/mes). Desviación -0,58 %.
# Lo verifica `checks()`.
#
# columnas: id, nombre, puesto, area_aleh, grupo_aleh, contrato,
#           jornada_h_semana, salario_bruto_anual, fecha_alta, estacion_principal
    # M8 (auditoría 2026-09-04): «gerente/encargado» (administrador) y
    # «sala» (salón) son vocabulario de España que la SPEC §0 pide glosar en
    # su primera aparición. Se glosa en el «puesto» de P01 y P03, que es
    # texto de EJEMPLO en celda verde (el lector lo sobrescribe con su
    # propia plantilla); la ESTACIÓN «Sala y servicio» no se toca, porque es
    # un valor de lista que la Cobertura por Estación referencia por texto
    # exacto.
PLANTILLA = [
    ('P01', 'Marta L.', 'Gerente / encargada general (manager; administrador, en el uso de otros países)', 'Área 1ª', 'Grupo I',
     'Indefinido', 40, 34500, '2021-03-01', 'Caja y cierre'),
    ('P02', 'Iván R.', 'Jefe de cocina', 'Área 2ª', 'Grupo I',
     'Indefinido', 40, 32000, '2019-09-16', 'Pase y caliente'),
    ('P03', 'Nuria C.', 'Jefa de sala (salón, en el uso de otros países)', 'Área 3ª', 'Grupo I',
     'Indefinido', 40, 27500, '2020-06-01', 'Sala y servicio'),
    ('P04', 'Diego M.', 'Cocinero (partida caliente)', 'Área 2ª', 'Grupo II',
     'Indefinido', 40, 25500, '2022-02-14', 'Pase y caliente'),
    ('P05', 'Laura S.', 'Cocinera (partida fría)', 'Área 2ª', 'Grupo II',
     'Indefinido', 40, 24000, '2023-04-03', 'Fríos y entrantes'),
    ('P06', 'Omar B.', 'Ayudante de cocina', 'Área 2ª', 'Grupo III',
     'Indefinido', 40, 21000, '2024-01-08', 'Pase y caliente'),
    ('P07', 'Rocío F.', 'Ayudante de cocina y postres', 'Área 2ª', 'Grupo III',
     'Fijo-discontinuo (campaña de marzo a noviembre)', 40, 15500, '2023-03-06', 'Postres y panadería'),
    ('P08', 'Carlos V.', 'Camarero, jefe de rango', 'Área 3ª', 'Grupo II',
     'Indefinido', 40, 23500, '2021-10-04', 'Sala y servicio'),
    ('P09', 'Elena T.', 'Camarera', 'Área 3ª', 'Grupo II',
     'Indefinido', 40, 22000, '2022-11-21', 'Barra y bebidas'),
    ('P10', 'Youssef A.', 'Camarero', 'Área 3ª', 'Grupo II',
     'Indefinido', 40, 21500, '2024-05-13', 'Sala y servicio'),
    ('P11', 'Paula G.', 'Ayudante de camarera', 'Área 3ª', 'Grupo III',
     'Formativo en alternancia', 25, 12500, '2025-09-15', 'Barra y bebidas'),
    ('P12', 'Andrés P.', 'Friegaplatos y office', 'Área 2ª', 'Grupo III',
     'Indefinido a tiempo parcial', 30, 16500, '2022-07-01', 'Pase y caliente'),
]
# Nota de coherencia: los 12 salarios brutos anuales están por encima del SMI
# (MM-16) también en proporción para las dos jornadas parciales. El periodo de
# prueba aplicable a cada contrato lo fija el ALEH y el convenio provincial NO
# lo puede modificar (MM-11); el encadenamiento de temporales (MM-09) no afecta
# a esta plantilla porque no hay ningún contrato por circunstancias de la
# producción vivo.

# ==========================================================================
# 3. ESTACIONES Y MATRIZ DE POLIVALENCIA
# ==========================================================================
ESTACIONES = [
    'Pase y caliente',
    'Fríos y entrantes',
    'Postres y panadería',
    'Barra y bebidas',
    'Sala y servicio',
    'Caja y cierre',
]

NIVELES_POLIVALENCIA = [
    (0, 'No formado'),
    (1, 'Formado, necesita supervisión'),
    (2, 'Autónomo: puede llevar la estación en un servicio'),
    (3, 'Puede formar a otra persona'),
]

# Matriz 12 × 6 con los niveles 0-3, en el orden de PLANTILLA y de ESTACIONES.
# Está diseñada a propósito para que el libro 2 encienda su alerta:
#   · PUNTO ÚNICO DE FALLO → «Fríos y entrantes»: sólo Laura S. (P05) está a
#     nivel ≥ 2. El jefe de cocina figura a nivel 1 y no es un descuido: la
#     matriz registra quién puede SOSTENER la estación en un servicio de 75
#     cubiertos, no quién se sabe las recetas. Es exactamente la situación 10
#     del bonus («el cocinero clave se va y sólo él sabe hacer la partida fría»).
#   · Estación mejor cubierta → «Sala y servicio»: 5 personas a nivel ≥ 2.
POLIVALENCIA = [
    # Pase  Fríos  Postres  Barra  Sala  Caja
    ('P01', [1,     0,      0,       2,     3,    3]),
    ('P02', [3,     1,      2,       0,     0,    1]),
    ('P03', [0,     0,      1,       3,     3,    3]),
    ('P04', [3,     1,      1,       0,     0,    0]),
    ('P05', [2,     3,      2,       0,     0,    0]),
    ('P06', [2,     1,      1,       0,     0,    0]),
    ('P07', [1,     1,      3,       0,     0,    0]),
    ('P08', [0,     0,      0,       2,     3,    2]),
    ('P09', [0,     0,      0,       3,     3,    1]),
    ('P10', [0,     0,      0,       1,     2,    1]),
    ('P11', [0,     0,      0,       1,     1,    0]),
    ('P12', [1,     0,      0,       0,     0,    0]),
]

# Plan de cross-training: la primera fila ataca el punto único de fallo.
# columnas: id_empleado, estación objetivo, nivel actual, nivel objetivo,
#           responsable, fecha objetivo, estado
PLAN_CROSS_TRAINING = [
    ('P06', 'Fríos y entrantes',   1, 2, 'P05', '2026-10-15', 'En curso'),
    ('P04', 'Fríos y entrantes',   1, 2, 'P05', '2026-11-30', 'Planificado'),
    ('P02', 'Fríos y entrantes',   1, 3, 'P05', '2026-12-15', 'Planificado'),
    ('P10', 'Barra y bebidas',     1, 2, 'P09', '2026-10-31', 'En curso'),
    ('P11', 'Sala y servicio',     1, 2, 'P03', '2026-11-15', 'Planificado'),
    ('P08', 'Caja y cierre',       2, 3, 'P01', '2026-10-20', 'En curso'),
    ('P12', 'Pase y caliente',     1, 2, 'P04', '2027-01-31', 'Planificado'),
    ('P07', 'Pase y caliente',     1, 2, 'P02', '2027-02-28', 'Planificado'),
]

# Coste de una baja. TODO son valores de EJEMPLO editables por el usuario: no
# pretenden ser una referencia de mercado y el libro los presenta como «pon los
# tuyos». El libro 2 calcula el coste con estas celdas, nunca con cifras
# nuestras metidas en la fórmula.
#
# A5 (auditoría 2026-09-04): el bloque B tenía dos fallos encadenados.
# 1) El % de caída se leía como «cuánto rinde de menos el CONJUNTO DEL
#    TURNO» (0,35) y se multiplicaba por la venta de TODO EL RESTAURANTE:
#    perder a 1 de 12 personas se llevaba por delante el 35 % de la
#    facturación de un mes entero. Ahora `pct_peso_persona_venta` es UN
#    solo coeficiente que ya neta el peso de esa persona en la venta DIARIA
#    del restaurante (no del turno): con 12 personas y puestos de peso
#    desigual, 0,05 (5 %) es una estimación conservadora para un puesto no
#    crítico — bájala o súbela según el puesto real.
# 2) B sumaba VENTA perdida (bruta) con A, que es GASTO real: no son la
#    misma clase de euro (A30 ya lo advertía y aun así se sumaban). Ahora
#    `margen_dia_medio` no es la venta bruta de un día: es el MARGEN tras
#    prime cost de un día medio, que sí es comparable con A. Sale de la
#    misma estructura que calcula el libro 1 de este pack
#    (cuadro-de-mando-semanal-manager.xlsx!Semana!O57, prime cost total
#    62,77 % → margen 37,23 % ≈ 37,2 %) aplicado a la venta diaria media
#    (3.370 €): 3.370 × 0,3723 ≈ 1.254,58 €/día. Es un valor de EJEMPLO
#    igual que los otros ocho: si tu prime cost real es otro, cambia esta
#    celda.
COSTE_BAJA = {
    'horas_seleccion': 12.0,
    'coste_hora_seleccion': 22.00,      # coste-empresa de quien selecciona
    'horas_formacion_formador': 25.0,
    'coste_hora_formador': 18.00,
    'horas_formacion_formado': 40.0,
    'coste_hora_formado': 12.00,
    'dias_menor_rendimiento': 30,
    'pct_peso_persona_venta': 0.05,     # peso de UNA persona en la venta DIARIA del restaurante
    'margen_dia_medio': 1254.58,        # margen tras prime cost de un día medio (37,2 % de 3.370 €)
}

# ==========================================================================
# 4. EL AÑO SEMANAL: 52 SEMANAS ISO DE 2026
# ==========================================================================
# Es el mismo año del mismo restaurante que el cuadro MENSUAL de la Guía Food
# Cost, visto por semanas. Cómo se construyó y por qué así:
#
# 1. 2026 tiene 53 semanas ISO (el 1 de enero cae en jueves). El libro trabaja
#    con las 52 primeras, que es la rejilla estándar de un cuadro semanal; la
#    semana 53 (28-dic-2026 → 3-ene-2027) ya pertenece al ejercicio siguiente.
#    La semana 1 empieza el lunes 29 de diciembre de 2025: es la convención ISO,
#    no una errata.
# 2. Cada semana se asigna al mes de su JUEVES (regla ISO). Enero, abril, julio
#    y octubre se quedan con 5 semanas; el resto, con 4.
# 3. El nivel de cada semana sale del RITMO DIARIO del mes correspondiente de la
#    Guía: venta del mes × 7 / días del mes. NO se reparte el total del mes
#    entre sus semanas, porque entonces un mes de 5 semanas mostraría semanas un
#    20 % más flojas que el mes vecino de 4 sin que hubiera pasado nada: 52
#    semanas son 364 días y no encajan en 12 meses naturales. Por eso el cuadre
#    con la Guía se comprueba comparando la VENTA MEDIA DIARIA de cada mes
#    (`checks()`), y sale dentro del ±3 % en todas las columnas.
# 4. Dentro de cada mes hay variación semanal real (fin de año, cuesta de enero,
#    Semana Santa —Pascua el 5 de abril de 2026—, comidas de empresa y Navidad).
# 5. El inventario está encadenado: el stock inicial de una semana es el final
#    de la anterior, y cada mes cierra en el nivel de stock que trae la Guía.
# 6. CUATRO semanas cierran por encima del objetivo de prime cost (65 % en sala)
#    y las 48 restantes en objetivo:
#       semana  7 (9-15 feb) ....... 72,0 %
#       semana 33 (10-16 ago) ...... 71,0 %  ← la semana del bonus
#       semana 35 (24-30 ago) ...... 72,2 %
#       semana 36 (31 ago-6 sep) ... 66,8 %  ← la semana anterior al plan de 90 días
#    Las tres primeras caen en meses que la Guía ya trae tensionados (febrero y
#    agosto). La cuarta es la interesante para el capítulo 03: septiembre cierra
#    el mes en 60 % y esa semana suelta se pierde en el promedio mensual.
#
# columnas:
#   semana ISO, mes (del jueves), ventas netas comida, ventas netas bebida,
#   stock inicial, compras, stock final, salarios brutos,
#   otros costes de personal, cubiertos, nº de tickets,
#   horas de apertura, horas trabajadas
SEMANAS = [
    ( 1,  1,  12327,   9119,  9700,  6762,  9834,  4898,  286,  829,  382, 35,  433),
    ( 2,  1,  11513,   8517,  9834,  5622,  9266,  4732,  276,  785,  357, 42,  421),
    ( 3,  1,  11164,   8259,  9266,  6570,  9834,  4660,  272,  764,  353, 42,  415),
    ( 4,  1,  11629,   8603,  9834,  5685,  9266,  4755,  277,  792,  378, 42,  422),
    ( 5,  1,  11513,   8517,  9266,  6324,  9400,  4732,  276,  774,  382, 42,  421),
    ( 6,  2,  12221,   9014,  9400,  6548,  9558,  5291,  292,  807,  403, 42,  431),
    ( 7,  2,  11616,   8568,  9558,  6747,  8920,  5160,  284,  753,  370, 42,  422),
    ( 8,  2,  12100,   8925,  8920,  6815,  9408,  5265,  290,  775,  367, 42,  429),
    ( 9,  2,  12463,   9193,  9408,  6208,  9100,  5344,  294,  795,  365, 42,  434),
    (10,  3,  12105,   8962,  9100,  6871,  9433,  4925,  278,  776,  353, 42,  429),
    (11,  3,  12352,   9145,  9433,  6208,  8970,  4975,  281,  802,  372, 42,  433),
    (12,  3,  12475,   9237,  8970,  7401,  9633,  5000,  283,  824,  396, 42,  435),
    (13,  3,  12475,   9237,  9633,  6604,  9500,  5000,  283,  839,  416, 42,  435),
    (14,  4,  15348,  11358,  9500,  8566,  9634,  5618,  332, 1045,  522, 49,  478),
    (15,  4,  13059,   9664,  9634,  6607,  9066,  5171,  306,  894,  437, 42,  444),
    (16,  4,  12925,   9565,  9066,  7668,  9634,  5145,  304,  881,  415, 42,  442),
    (17,  4,  12925,   9565,  9634,  6533,  9066,  5145,  304,  870,  398, 42,  442),
    (18,  4,  13059,   9664,  9066,  7309,  9200,  5171,  306,  864,  393, 42,  444),
    (19,  5,  13860,  10261,  9200,  8004,  9558,  5213,  315,  902,  420, 42,  456),
    (20,  5,  14000,  10365,  9558,  7284,  9120,  5239,  316,  899,  434, 42,  458),
    (21,  5,  14000,  10365,  9120,  8411,  9808,  5239,  316,  894,  445, 42,  458),
    (22,  5,  14140,  10468,  9808,  7691,  9700,  5265,  318,  906,  452, 42,  460),
    (23,  6,  14863,  10967,  9700,  8794,  9758,  5506,  334,  962,  468, 42,  470),
    (24,  6,  14863,  10967,  9758,  7998,  9020,  5506,  334,  979,  459, 42,  470),
    (25,  6,  14863,  10967,  9020,  9124,  9408,  5506,  334,  996,  455, 42,  470),
    (26,  6,  14863,  10967,  9408,  8328,  9000,  5506,  334, 1010,  461, 42,  470),
    (27,  7,  14933,  11043,  9000,  8702,  9274,  5594,  346, 1022,  478, 42,  472),
    (28,  7,  15084,  11155,  9274,  8085,  8846,  5623,  348, 1029,  499, 42,  474),
    (29,  7,  15235,  11266,  8846,  9306,  9554,  5651,  349, 1027,  512, 42,  476),
    (30,  7,  15386,  11378,  9554,  8255,  9126,  5679,  351, 1020,  507, 42,  478),
    (31,  7,  14782,  10932,  9126,  8617,  9400,  5566,  344,  962,  466, 42,  469),
    (32,  8,  13197,   9743,  9400,  7174,  9458,  5537,  311,  847,  395, 42,  446),
    (33,  8,  12680,   9361,  9458,  7387,  8720,  5427,  305,  809,  368, 42,  438),
    (34,  8,  12809,   9456,  8720,  7295,  9108,  5455,  307,  819,  375, 42,  440),
    (35,  8,  13068,   9647,  9108,  8355,  8700,  5509,  310,  845,  397, 42,  444),
    (36,  9,  13716,  10162,  8700,  9048,  9133,  5286,  306,  903,  441, 42,  454),
    (37,  9,  14281,  10581,  9133,  6659,  8770,  5394,  312,  958,  478, 42,  462),
    (38,  9,  14423,  10686,  8770,  7855,  9533,  5420,  313,  981,  487, 42,  464),
    (39,  9,  14140,  10477,  9533,  6919,  9500,  5367,  310,  969,  466, 42,  460),
    (40, 10,  13056,   9670,  9500,  7237,  9634,  5030,  297,  892,  414, 42,  444),
    (41, 10,  13456,   9966,  9634,  6753,  9066,  5106,  302,  909,  413, 42,  450),
    (42, 10,  13456,   9966,  9066,  7889,  9634,  5106,  302,  894,  410, 42,  450),
    (43, 10,  13323,   9868,  9634,  6681,  9066,  5081,  300,  869,  411, 42,  448),
    (44, 10,  13323,   9868,  9066,  7382,  9200,  5081,  300,  857,  420, 42,  448),
    (45, 11,  12982,   9633,  9200,  7288,  9558,  5177,  293,  830,  415, 42,  443),
    (46, 11,  13113,   9730,  9558,  6562,  9120,  5203,  294,  840,  416, 42,  445),
    (47, 11,  13113,   9730,  9120,  7688,  9808,  5203,  294,  849,  406, 42,  445),
    (48, 11,  13244,   9827,  9808,  6962,  9700,  5229,  295,  872,  403, 42,  447),
    (49, 12,  14784,  10920,  9700,  8472, 10108,  5360,  366,  989,  449, 42,  469),
    (50, 12,  15738,  11625, 10108,  8196,  9720,  5527,  377, 1068,  491, 42,  483),
    (51, 12,  16374,  12094,  9720,  9669, 10458,  5638,  385, 1120,  532, 42,  493),
    (52, 12,  16692,  12329, 10458,  9046, 10400,  5694,  389, 1140,  561, 35,  498),
]

# Copia literal del año MENSUAL de la Guía Food Cost, sólo como REFERENCIA de
# cuadre. Fuente: ../guia-food-cost/datos_ejemplo.py → CUADRO_MENSUAL.
# `checks()` importa el fichero original y comprueba que esta copia es idéntica:
# si alguien toca la Guía y no toca esto, el gate lo canta.
# columnas: ventas comida, ventas bebida, stock inicial, compras, stock final,
#           salarios brutos, otros costes de personal
REFERENCIA_GUIA_FOOD_COST = [
    (51500, 38100, 9700, 28100, 9400, 21600, 1260),
    (48400, 35700, 9400, 27000, 9100, 21600, 1190),
    (54700, 40500, 9100, 30700, 9500, 22300, 1260),
    (57700, 42700, 9500, 31400, 9200, 22500, 1330),
    (62000, 45900, 9200, 34700, 9700, 23200, 1400),
    (63700, 47000, 9700, 37700, 9000, 24200, 1470),
    (66800, 49400, 9000, 38100, 9400, 24900, 1540),
    (57300, 42300, 9400, 34400, 8700, 24900, 1400),
    (60600, 44900, 8700, 32600, 9500, 23000, 1330),
    (59000, 43700, 9500, 31800, 9200, 22500, 1330),
    (56200, 41700, 9200, 30500, 9700, 22300, 1260),
    (70400, 52000, 9700, 39100, 10400, 24600, 1680),
]
MESES = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
         'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
DIAS_MES_2026 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Semanas que el manual y el bonus citan por su número.
SEMANA_BONUS_PRIME_71 = 33      # bonus, situación 6: «la semana cierra con un prime cost del 71 %»
SEMANAS_FUERA_DE_OBJETIVO = (7, 33, 35, 36)

# ==========================================================================
# 5. KPI Y DEFINICIONES (hoja del libro 1)
# ==========================================================================
# Trece indicadores. La columna «error típico» es la que da valor: es lo que el
# capítulo 02 desarrolla («12 definiciones que casi nadie distingue»).
# columnas: kpi, fórmula en palabras, unidad, error típico, cadencia
KPI_DEFINICIONES = [
    ('Ventas netas',
     'Lo cobrado por comida y bebida SIN IVA, después de descuentos e invitaciones',
     '€',
     'Usar la cifra con IVA: infla las ventas un 10 % y hace parecer bueno un food cost que no lo es',
     'Semanal'),
    ('Consumo de materia prima',
     'Stock inicial + compras del periodo - stock final',
     '€',
     'Usar las compras en lugar del consumo: una semana con un pedido grande sale disparada y la siguiente, regalada',
     'Semanal'),
    ('Food cost %',
     'Consumo de materia prima ÷ ventas netas',
     '%',
     'Calcularlo sin contar el inventario, o mezclando comida y bebida cuando el objetivo de cada una es distinto',
     'Semanal'),
    ('Coste de personal',
     'Salarios brutos × (1 + Seguridad Social a cargo de la empresa) + otros costes de personal',
     '€',
     'Quedarse en el bruto y olvidar la cotización: se deja fuera aproximadamente un tercio del coste',
     'Semanal'),
    ('Labor cost %',
     'Coste de personal ÷ ventas netas',
     '%',
     'Compararlo con el de otro local sin mirar si aquel es de sala o de barra: no juegan la misma liga',
     'Semanal'),
    ('Prime cost %',
     'Food cost % + labor cost %',
     '%',
     'Mirar sólo el food cost: un 28 % de producto no salva un 40 % de personal',
     'Semanal'),
    ('Margen tras prime cost',
     'Ventas netas - consumo de materia prima - coste de personal',
     '€',
     'Confundirlo con el beneficio: de aquí todavía salen alquiler, suministros, amortización e impuestos',
     'Semanal'),
    ('Ticket medio',
     'Ventas netas ÷ número de tickets (mesas cobradas)',
     '€',
     'Llamarle ticket medio al gasto por cubierto: en una mesa de dos, el ticket es el doble',
     'Semanal'),
    ('Gasto medio por cubierto',
     'Ventas netas ÷ número de cubiertos (comensales)',
     '€',
     'Contar como cubierto a quien sólo toma café: distorsiona la serie y hace ilegible la comparación',
     'Semanal'),
    ('Cubiertos por hora de apertura',
     'Cubiertos ÷ horas de apertura al público',
     'cubiertos/h',
     'Usarlo para medir a la sala: mide la demanda y el aforo, no el rendimiento del equipo',
     'Semanal'),
    ('Ventas por hora trabajada',
     'Ventas netas ÷ horas realmente trabajadas por toda la plantilla',
     '€/h',
     'Alimentarlo con las horas del contrato en lugar de las del registro de jornada',
     'Semanal'),
    ('Rotación',
     'Bajas del periodo ÷ plantilla media del periodo',
     '%',
     'Mezclarla con el absentismo y con la temporalidad: son tres cosas distintas y se corrigen distinto',
     'Trimestral'),
    ('Absentismo',
     'Horas no trabajadas por ausencia ÷ horas pactadas efectivas',
     '%',
     'Meter las vacaciones dentro: las vacaciones son un derecho planificado, no una ausencia',
     'Mensual'),
    ('Cobertura por estación',
     'Personas a nivel 2 o 3 en la estación ÷ personas de esa área',
     '%',
     'Dar por cubierta una estación porque «todos han estado alguna vez»: nivel 1 no cubre un servicio',
     'Trimestral'),
]

# ==========================================================================
# 6. QUEJAS, RECLAMACIONES FORMALES Y RESEÑAS (libro 3)
# ==========================================================================
# Son TRES cosas distintas y por eso son tres hojas: la queja se resuelve en
# sala, la hoja oficial de reclamaciones tiene plazo legal autonómico y la
# reseña es pública y se responde. Capítulo 17 del manual.

MOTIVOS_QUEJA = [
    'Espera excesiva',
    'Plato frío o mal temperado',
    'Error en la comanda',
    'Trato del personal',
    'Cobro incorrecto',
    'Limpieza',
    'Reserva no encontrada',
    'Ruido',
    'Información de alérgenos',
    'Producto en mal estado',
]
CANALES_QUEJA = ['En sala', 'Teléfono', 'Correo electrónico', 'Reseña online',
                 'Redes sociales', 'Hoja de reclamaciones']

# 30 quejas de tres meses (junio, julio y agosto de 2026). Están diseñadas para
# que el resumen del libro cante UN motivo por encima del resto: «Espera
# excesiva», 10 de 30, y 6 de las 10 en julio, el mes de más presión. Es lo que
# convierte una lista de incidentes en un problema de proceso.
# columnas: fecha, canal, motivo, gravedad (1-3), responsable, acción, fecha de cierre
QUEJAS = [
    ('2026-06-05', 'En sala', 'Error en la comanda', 1, 'P03', 'Se rehace el plato y se invita al postre', '2026-06-05'),
    ('2026-06-07', 'Reseña online', 'Espera excesiva', 2, 'P01', 'Respuesta pública y llamada al cliente', '2026-06-08'),
    ('2026-06-11', 'En sala', 'Plato frío o mal temperado', 2, 'P02', 'Se repone el plato; revisión de la lámpara del pase', '2026-06-11'),
    ('2026-06-13', 'Teléfono', 'Reserva no encontrada', 2, 'P03', 'Se acomoda en terraza; revisión del cuaderno de reservas', '2026-06-14'),
    ('2026-06-18', 'En sala', 'Cobro incorrecto', 2, 'P01', 'Devolución en el acto y revisión del cierre de caja', '2026-06-18'),
    ('2026-06-20', 'En sala', 'Espera excesiva', 2, 'P03', 'Disculpa y aperitivo; se apunta la hora de comanda', '2026-06-21'),
    ('2026-06-25', 'Correo electrónico', 'Trato del personal', 3, 'P01', 'Reunión con la persona implicada y respuesta escrita', '2026-06-27'),
    ('2026-06-28', 'En sala', 'Limpieza', 1, 'P03', 'Refuerzo del repaso de aseos en el turno de tarde', '2026-06-30'),
    ('2026-07-02', 'En sala', 'Espera excesiva', 2, 'P03', 'Se avisa del tiempo real al sentar; aperitivo de cortesía', '2026-07-03'),
    ('2026-07-03', 'Reseña online', 'Espera excesiva', 2, 'P01', 'Respuesta pública en 24 h', '2026-07-04'),
    ('2026-07-04', 'En sala', 'Error en la comanda', 1, 'P08', 'Se rehace el plato', '2026-07-04'),
    ('2026-07-05', 'En sala', 'Espera excesiva', 3, 'P01', 'Se invita a la mesa; se abre el análisis de tiempos de pase', '2026-07-06'),
    ('2026-07-09', 'Teléfono', 'Ruido', 1, 'P03', 'Se reubica al cliente lejos de la barra en la próxima reserva', '2026-07-11'),
    ('2026-07-10', 'En sala', 'Espera excesiva', 2, 'P03', 'Se abre una segunda plancha en el pase los viernes', '2026-07-12'),
    ('2026-07-11', 'Hoja de reclamaciones', 'Espera excesiva', 3, 'P01', 'Entrega de hoja oficial y respuesta escrita', '2026-07-11'),
    ('2026-07-14', 'En sala', 'Plato frío o mal temperado', 2, 'P02', 'Se repone; revisión del orden de salida de la mesa', '2026-07-15'),
    ('2026-07-16', 'Correo electrónico', 'Información de alérgenos', 3, 'P02', 'Se revisa la ficha del plato y el soporte escrito de alérgenos', '2026-07-17'),
    ('2026-07-18', 'En sala', 'Error en la comanda', 1, 'P08', 'Se rehace el plato', '2026-07-18'),
    ('2026-07-19', 'Reseña online', 'Espera excesiva', 2, 'P01', 'Respuesta pública; se cita el cambio de organización del pase', '2026-07-21'),
    ('2026-07-22', 'En sala', 'Cobro incorrecto', 2, 'P01', 'Devolución y revisión de los precios cargados en el TPV', '2026-07-22'),
    ('2026-07-24', 'Redes sociales', 'Trato del personal', 2, 'P03', 'Respuesta en privado y conversación con el equipo', '2026-07-26'),
    ('2026-07-25', 'Hoja de reclamaciones', 'Producto en mal estado', 3, 'P02', 'Retirada del lote, revisión de trazabilidad y respuesta escrita', '2026-07-27'),
    ('2026-07-30', 'En sala', 'Limpieza', 1, 'P03', 'Cambio de la frecuencia de repaso de aseos en fin de semana', '2026-08-02'),
    ('2026-08-01', 'En sala', 'Espera excesiva', 2, 'P03', 'Nuevo orden de comandas por rangos', '2026-08-02'),
    ('2026-08-06', 'Teléfono', 'Reserva no encontrada', 2, 'P03', 'Se confirma por SMS toda reserva de más de 4 personas', '2026-08-07'),
    ('2026-08-08', 'En sala', 'Error en la comanda', 1, 'P08', 'Se rehace el plato; repaso del uso del TPV con P11', '2026-08-08'),
    ('2026-08-13', 'Reseña online', 'Trato del personal', 1, 'P01', 'Respuesta pública y repaso del protocolo de despedida', '2026-08-15'),
    ('2026-08-15', 'En sala', 'Espera excesiva', 2, 'P01', 'Se avisa del tiempo real al sentar', '2026-08-16'),
    ('2026-08-20', 'En sala', 'Ruido', 1, 'P03', 'Se baja el volumen del hilo musical en el turno de cena', '2026-08-22'),
    ('2026-08-27', 'Correo electrónico', 'Trato del personal', 2, 'P01', 'Respuesta escrita y seguimiento en el uno-a-uno', '2026-08-29'),
]

# Reclamaciones formales (hoja oficial). El establecimiento está en Girona, así
# que el plazo de respuesta es el de CATALUÑA: 1 mes. La segunda se contestó a
# los 39 días → fuera de plazo, que es justo lo que el libro tiene que enseñar
# a detectar.
# columnas: fecha de entrega, número de hoja, comunidad, fecha de respuesta
RECLAMACIONES = [
    ('2026-07-11', 'GI-2026-0417', 'Cataluña', '2026-07-30'),
    ('2026-07-25', 'GI-2026-0463', 'Cataluña', '2026-09-02'),
    ('2026-08-14', 'GI-2026-0521', 'Cataluña', '2026-08-28'),
]

# Parámetros del libro 3. El SLA es de la CASA (celda editable). Los plazos
# autonómicos sólo se siembran con los DOS verificados; el resto queda en
# blanco a propósito con la nota «consulta tu comunidad», porque inventarlos
# sería peor que dejarlos vacíos.
# M5 (auditoría 2026-09-04): el SLA se medía en HORAS pero «Fecha de la
# queja» y «Fecha de cierre» son columnas de fecha SIN hora, así que el
# resultado sólo podía ser 0, 24, 48, 72… (múltiplos de 24) y cualquier SLA
# por debajo de 24 h era inmedible. Se mide en DÍAS (3, 2, 1), que es lo que
# esas dos columnas pueden medir de verdad sin pedirle la hora al usuario.
PARAMETROS_QUEJAS = {
    'sla_dias_por_gravedad': {1: 3, 2: 2, 3: 1},
    'escala_gravedad': [(1, 'Leve: molestia sin impacto en la experiencia'),
                        (2, 'Media: afecta a la experiencia de la mesa'),
                        (3, 'Grave: riesgo sanitario, legal o reputacional')],
    'plazos_autonomicos': [
        # comunidad, plazo, nota (sólo lo verificado; el resto, en blanco)
        ('Cataluña', '1 mes', 'Verificado el 04-09-2026'),
        ('Andalucía', '10 días hábiles', 'Verificado el 04-09-2026. Hoja electrónica obligatoria desde mayo de 2026'),
        ('Otras comunidades', '', 'Consulta tu comunidad: la hoja de reclamaciones es competencia autonómica'),
    ],
}

# 40 reseñas de seis meses (marzo a agosto de 2026). La media MENSUAL baja en
# julio (3,25) y se recupera en agosto (4,33): es el mismo julio en el que se
# concentran las quejas por espera. El libro lo cruza en su hoja Resumen.
# columnas: plataforma, fecha, estrellas, tema, respondida
RESENAS = [
    ('Google', '2026-03-03', 5, 'Comida', 'Sí'),
    ('TripAdvisor', '2026-03-07', 5, 'Servicio', 'Sí'),
    ('Google', '2026-03-12', 4, 'Ambiente', 'Sí'),
    ('TheFork', '2026-03-16', 4, 'Comida', 'No'),
    ('Google', '2026-03-21', 5, 'Comida', 'Sí'),
    ('TripAdvisor', '2026-03-25', 3, 'Espera', 'Sí'),
    ('Google', '2026-03-29', 4, 'Servicio', 'No'),
    ('Google', '2026-04-04', 5, 'Comida', 'Sí'),
    ('TheFork', '2026-04-09', 4, 'Reserva', 'Sí'),
    ('Google', '2026-04-14', 5, 'Servicio', 'Sí'),
    ('Facebook', '2026-04-18', 4, 'Ambiente', 'No'),
    ('Google', '2026-04-23', 5, 'Comida', 'Sí'),
    ('TripAdvisor', '2026-04-28', 3, 'Precio', 'Sí'),
    ('Google', '2026-05-02', 5, 'Comida', 'Sí'),
    ('TheFork', '2026-05-08', 4, 'Servicio', 'Sí'),
    ('Google', '2026-05-13', 4, 'Ambiente', 'No'),
    ('TripAdvisor', '2026-05-17', 5, 'Comida', 'Sí'),
    ('Google', '2026-05-21', 3, 'Espera', 'Sí'),
    ('Facebook', '2026-05-26', 5, 'Servicio', 'No'),
    ('Google', '2026-05-30', 4, 'Comida', 'Sí'),
    ('Google', '2026-06-04', 4, 'Servicio', 'Sí'),
    ('TheFork', '2026-06-10', 5, 'Comida', 'Sí'),
    ('Google', '2026-06-15', 4, 'Ambiente', 'No'),
    ('TripAdvisor', '2026-06-19', 3, 'Espera', 'Sí'),
    ('Google', '2026-06-24', 5, 'Comida', 'Sí'),
    ('Google', '2026-06-29', 4, 'Servicio', 'No'),
    ('Google', '2026-07-03', 3, 'Espera', 'Sí'),
    ('TripAdvisor', '2026-07-06', 2, 'Espera', 'Sí'),
    ('Google', '2026-07-10', 4, 'Comida', 'Sí'),
    ('TheFork', '2026-07-13', 3, 'Servicio', 'No'),
    ('Google', '2026-07-17', 5, 'Comida', 'Sí'),
    ('Google', '2026-07-20', 3, 'Espera', 'Sí'),
    ('Facebook', '2026-07-24', 4, 'Ambiente', 'No'),
    ('TripAdvisor', '2026-07-28', 2, 'Servicio', 'Sí'),
    ('Google', '2026-08-04', 5, 'Comida', 'Sí'),
    ('TheFork', '2026-08-09', 4, 'Servicio', 'Sí'),
    ('Google', '2026-08-14', 5, 'Comida', 'Sí'),
    ('Google', '2026-08-19', 4, 'Ambiente', 'No'),
    ('TripAdvisor', '2026-08-24', 3, 'Precio', 'Sí'),
    ('Google', '2026-08-29', 5, 'Servicio', 'Sí'),
]
# Las cifras del EFECTO de las reseñas sobre los ingresos no están aquí: son
# dato de sector y el capítulo 17 las cita por id (MM-45), acotadas como manda
# la SPEC D10. Los no-shows, por MM-46.

# ==========================================================================
# 7. SELECCIÓN: SCORECARD Y ENTREVISTA ESTRUCTURADA (libro 4)
# ==========================================================================
SELECCION = {
    'puesto': 'Camarero/a de sala',
    'area_aleh': 'Área 3ª',
    'grupo_aleh': 'Grupo II',
    'jornada': '40 h/semana, turno partido',
    'umbral_recomendacion': 3.50,   # celda editable
    'competencias': [
        # competencia, peso (1-3)
        ('Experiencia en sala de carta con servicio en mesa', 3),
        ('Ritmo y aguante en un servicio de 75 cubiertos', 3),
        ('Trato con el cliente y gestión de una queja', 3),
        ('Coordinación con cocina', 2),
        ('Manejo de TPV, comanda y cobro', 2),
        ('Conocimiento de alérgenos y de la carta', 2),
        ('Idiomas de sala (inglés y francés)', 1),
        ('Disponibilidad para turno partido y fines de semana', 2),
    ],
    # candidato, puntuaciones 1-5 en el orden de las competencias.
    # `None` = N/A: NO se valoró. La media ponderada del libro excluye su peso,
    # que es distinto de puntuar 0. El candidato B llega con N/A en idiomas.
    'candidatos': [
        ('Candidata A', [4, 4, 5, 4, 3, 3, 4, 5]),
        ('Candidato B', [5, 4, 3, 3, 5, 4, None, 4]),
        ('Candidata C', [3, 3, 4, 4, 3, 2, 3, 3]),
        ('Candidato D', [2, 4, 3, 3, 4, 2, 2, 5]),
    ],
}

# Banco de preguntas: TRES por competencia, 24 en total, en el mismo orden.
# ⚠ NOTA LEGAL que va impresa en la hoja del libro 4: el art. 9.5 de la Ley
# 15/2022 prohíbe preguntar al aspirante por sus condiciones de salud. Por eso
# no hay aquí ni una sola pregunta sobre salud, embarazo, planes de maternidad
# o paternidad, cargas familiares, situación de pareja, religión, origen ni
# orientación sexual: no es una recomendación de estilo, es lo que separa una
# entrevista de una infracción. Todas las preguntas son de CONDUCTA («cuéntame
# una vez que…»), que además predicen mejor.
PREGUNTAS_COMPETENCIA = [
    # (competencia, pregunta)
    ('Experiencia en sala de carta con servicio en mesa', 'Descríbeme el servicio de un viernes noche en tu último trabajo: cuántas mesas llevabas y con qué apoyo.'),
    ('Experiencia en sala de carta con servicio en mesa', 'Cuéntame cómo levantabas y montabas un rango entre servicio y servicio.'),
    ('Experiencia en sala de carta con servicio en mesa', '¿Qué parte del servicio se te da peor y qué haces para compensarlo?'),
    ('Ritmo y aguante en un servicio de 75 cubiertos', 'Cuéntame el servicio más cargado que hayas hecho: qué pasó y cómo acabó.'),
    ('Ritmo y aguante en un servicio de 75 cubiertos', 'Cuando entran cuatro mesas a la vez, ¿en qué orden atiendes y por qué?'),
    ('Ritmo y aguante en un servicio de 75 cubiertos', 'Dime una vez que te quedaste atrás en el servicio. ¿Cómo lo recuperaste?'),
    ('Trato con el cliente y gestión de una queja', 'Cuéntame la última queja seria que atendiste y qué dijiste exactamente.'),
    ('Trato con el cliente y gestión de una queja', 'Un cliente dice que el plato está frío y tú sabes que salió bien. ¿Qué haces?'),
    ('Trato con el cliente y gestión de una queja', '¿Qué haces cuando un cliente pide la hoja de reclamaciones?'),
    ('Coordinación con cocina', 'Cuéntame un choque que hayas tenido con cocina y cómo se resolvió.'),
    ('Coordinación con cocina', '¿Cómo cantas una modificación de plato para que no se pierda en el pase?'),
    ('Coordinación con cocina', '¿Qué información necesitas del jefe de cocina antes de empezar el servicio?'),
    ('Manejo de TPV, comanda y cobro', '¿Con qué TPV has trabajado y qué sabes hacer sin ayuda?'),
    ('Manejo de TPV, comanda y cobro', 'Cuéntame cómo dividirías una cuenta de una mesa de ocho con tres formas de pago.'),
    ('Manejo de TPV, comanda y cobro', '¿Qué haces si al cerrar la caja falta dinero?'),
    ('Conocimiento de alérgenos y de la carta', '¿Qué le dices a un cliente que pregunta si un plato lleva gluten?'),
    ('Conocimiento de alérgenos y de la carta', '¿Por qué no basta con el cartel de «consulte al personal»?'),
    ('Conocimiento de alérgenos y de la carta', 'Descríbeme cómo aprendes una carta nueva de veinte platos.'),
    ('Idiomas de sala (inglés y francés)', 'Explícame en inglés dos platos de nuestra carta.'),
    ('Idiomas de sala (inglés y francés)', '¿Cómo te desenvuelves si la mesa habla francés y tú no?'),
    ('Idiomas de sala (inglés y francés)', '¿Qué vocabulario de sala manejas en otros idiomas?'),
    # B2 (auditoría 2026-09-04): las dos preguntas que había aquí («¿Qué te
    # hizo dejar el último puesto?» y «¿Qué esperas de este trabajo dentro
    # de un año?») no miden disponibilidad. Sustituidas por festivos/
    # temporada alta y por el cierre de noche seguido de apertura, que son
    # los dos puntos donde de verdad se rompe la disponibilidad en un
    # restaurante.
    ('Disponibilidad para turno partido y fines de semana', 'Nuestro horario es de martes a domingo, turno partido. ¿Encaja con lo que buscas?'),
    ('Disponibilidad para turno partido y fines de semana', 'Cuéntame una temporada en la que tuvieras que trabajar festivos seguidos (Navidad, Semana Santa, puentes): ¿cómo la llevaste?'),
    ('Disponibilidad para turno partido y fines de semana', 'Cerramos de noche y a veces hay que abrir temprano al día siguiente. ¿Te ha tocado antes un cierre seguido de una apertura? ¿Tienes algún compromiso que choque con eso?'),
]

# ==========================================================================
# 8. CUMPLIMIENTO LEGAL (libro 5)
# ==========================================================================
# La columna que hace único a este calendario es «¿lo fija una norma estatal?».
# De los 18 puntos, sólo CUATRO familias tienen la periodicidad fijada por una
# norma estatal: el registro de jornada (diario), la inspección del ascensor,
# la de la instalación de gas y los extintores (cuyos cuatro vencimientos son
# un mismo punto). Campana, plagas, termómetros y formación se venden como
# «obligación legal cada X meses» y NO lo son: la ley exige el resultado, no el
# calendario. Lo verifica `checks()`.
PUNTOS_PERIODICIDAD_ESTATAL = ('registro-jornada', 'ascensor', 'extintores', 'gas')

# columnas: punto, familia, última actuación, periodicidad en meses (editable),
#           ¿lo fija una norma estatal?, mm_id, nota
# periodicidad 0 = no es un vencimiento periódico (obligación diaria o hito con fecha).
CUMPLIMIENTO = [
    ('Registro de jornada (diario) y conservación durante 4 años', 'registro-jornada',
     '2026-09-04', 0, 'Sí', 'MM-02',
     'No vence: se hace cada día. Los 4 años de conservación los fija el art. 34.9 ET'),
    ('Inspección periódica del ascensor', 'ascensor',
     '2025-04-18', 24, 'Sí', '', 'Local con ascensor de uso público'),
    ('Extintores: revisión trimestral por el titular', 'extintores',
     '2026-07-01', 3, 'Sí', '', 'La hace el propio establecimiento y se anota en la etiqueta'),
    ('Extintores: mantenimiento anual por empresa mantenedora', 'extintores',
     '2025-11-12', 12, 'Sí', '', ''),
    ('Extintores: retimbrado (prueba de presión)', 'extintores',
     '2021-05-09', 60, 'Sí', '', ''),
    ('Extintores: retirada del servicio a los 20 años', 'extintores',
     '2012-03-01', 240, 'Sí', '', 'Se cuenta desde la fecha de fabricación grabada en el aparato'),
    ('Revisión periódica de la instalación de gas', 'gas',
     '2022-10-20', 60, 'Sí', '', ''),
    ('Control de plagas (desinsectación y desratización)', 'plagas',
     '2026-06-15', 3, 'No', 'MM-29',
     'La ley exige un plan de control de plagas EFICAZ dentro del APPCC, no una periodicidad. Los 3 meses son criterio de la casa'),
    ('Limpieza de campana y conductos de extracción', 'campana',
     '2026-03-10', 6, 'No', '',
     'Ninguna norma estatal dice cada cuánto. Lo marcan tu plan de limpieza y, en su caso, la póliza del seguro'),
    ('Verificación de termómetros y sondas', 'termometros',
     '2026-01-20', 12, 'No', 'MM-32',
     'El APPCC exige que la medida sea fiable; la periodicidad la fijas tú en el plan'),
    ('Analítica de agua (sólo con depósito o tratamiento propio)', 'agua',
     '2026-02-05', 12, 'No', '',
     'Si el local se abastece de la red municipal sin depósito intermedio, no aplica. Consulta a tu comunidad'),
    ('Formación de manipuladores de alimentos', 'manipuladores',
     '2025-06-02', 24, 'No', 'MM-30',
     'No existe carné oficial desde 2010: la obligación es del titular, que debe garantizar y poder acreditar la formación'),
    ('Formación de PRL del puesto de trabajo', 'prl-formacion',
     '2025-09-30', 24, 'No', '',
     'La ley la exige al contratar y cuando cambien las funciones o los riesgos, no cada X meses'),
    ('Revisión de la evaluación de riesgos laborales', 'evaluacion-riesgos',
     '2024-11-15', 36, 'No', 'MM-22',
     'Se revisa cuando cambian las condiciones de trabajo o tras un daño a la salud'),
    ('Actualización del registro retributivo', 'registro-retributivo',
     '2026-01-31', 12, 'No', 'MM-18',
     'El registro es obligatorio siempre y su periodo de referencia es el año natural; lo que la norma no fija es una fecha de revisión'),
    ('Revisión del plan de prevención de pérdidas y desperdicio alimentario', 'desperdicio',
     '2026-04-02', 12, 'No', 'MM-36',
     'Obligatorio para quien no sea microempresa. La revisión anual es criterio de la casa'),
    ('Renovación del seguro de responsabilidad civil', 'seguro-rc',
     '2026-01-01', 12, 'No', '',
     'Obligación contractual; algunas comunidades lo exigen para la licencia de actividad'),
    ('Adaptación del TPV a Verifactu', 'tpv-verifactu',
     '2026-09-04', 0, 'No', '',
     'No es una periodicidad, es un hito con fecha: 1-01-2027 sociedades y 1-07-2027 el resto'),
]

# Hoja «Estado Normativo»: las normas EN MOVIMIENTO, con fecha de corte editable.
# El constructor saca el dato y la URL del JSON por el id; aquí sólo va el id.
# columnas: norma, estado a la fecha de corte, qué hace el manager, fecha de corte, mm_id
ESTADO_NORMATIVO = [
    ('Registro horario digital',
     'En tramitación: el real decreto no está publicado en el BOE (dictamen desfavorable del Consejo de Estado de 23-03-2026)',
     'Sigue rigiendo el art. 34.9 ET: registro diario, 4 años de conservación, papel o Excel válidos',
     '2026-09-04', 'MM-02'),
    ('Verifactu',
     'Aplazado por el RDL 15/2025: 1 de enero de 2027 para sociedades y 1 de julio de 2027 para el resto',
     'Pedir por escrito al proveedor del TPV la fecha de su versión adaptada',
     '2026-09-04', 'MM-58'),
    ('Factura electrónica B2B',
     'Reglamento aprobado (RD 238/2026) pero aún no exigible: cuenta 12 o 24 meses desde la orden ministerial',
     'Las facturas simplificadas quedan fuera SALVO las cualificadas, las que llevan NIF del cliente',
     '2026-09-04', 'MM-39'),
    ('Prohibición de fumar en terrazas',
     'Proyecto de ley aprobado por el Consejo de Ministros el 21-07-2026: no está vigente',
     'Hoy lo que define una terraza legal es tener como máximo dos paredes (Ley 28/2005, art. 2.2)',
     '2026-09-04', 'MM-59'),
    ('Salario mínimo interprofesional 2026',
     'Vigente (RD 126/2026)',
     'Comprobar que ningún salario de la plantilla queda por debajo, también en las jornadas parciales',
     '2026-09-04', 'MM-16'),
    ('ALEH VI (acuerdo laboral estatal de hostelería)',
     'Modificado y publicado el 04-09-2026 (BOE-A-2026-18630); vigente hasta el 31-12-2030',
     'Aplicar la audiencia previa en el despido disciplinario y el nuevo régimen del registro de jornada, móvil y tabaco',
     '2026-09-04', 'MM-13'),
    ('Convenio provincial de hostelería de Girona',
     'Vigente; las tablas se consultan en REGCON',
     'El convenio provincial NO puede tocar clasificación profesional, periodo de prueba, contratos formativos ni régimen disciplinario',
     '2026-09-04', 'MM-11'),
]

# Hoja «Documentación Obligatoria»: 12 documentos que tienen que estar y dónde.
# columnas: documento, dónde debe estar, quién lo pide
DOCUMENTACION_OBLIGATORIA = [
    ('Hojas de reclamaciones y cartel anunciador', 'En el local, a la vista y a disposición del cliente', 'Inspección de consumo (autonómica)'),
    ('Registro de jornada de los últimos 4 años', 'En el centro de trabajo, accesible de forma inmediata', 'Inspección de Trabajo'),
    ('Contratos, altas en la Seguridad Social y nóminas', 'En el centro de trabajo o accesibles en remoto', 'Inspección de Trabajo'),
    ('Plan de prevención, evaluación de riesgos y planificación preventiva', 'En el centro de trabajo', 'Inspección de Trabajo'),
    ('Protocolo frente al acoso sexual y por razón de sexo', 'Publicado y accesible a toda la plantilla', 'Inspección de Trabajo'),
    ('Registro retributivo', 'En el centro de trabajo y a disposición de la representación legal', 'Inspección de Trabajo'),
    ('Política escrita de desconexión digital', 'Accesible a toda la plantilla', 'Inspección de Trabajo'),
    ('Plan APPCC y sus registros', 'En el local, a disposición del inspector', 'Sanidad (autonómica)'),
    ('Acreditación de la formación en manipulación de alimentos', 'En el local, por cada persona', 'Sanidad (autonómica)'),
    ('Información escrita de alérgenos de todos los platos', 'En el local, disponible para el cliente y para el personal de sala', 'Sanidad y consumo'),
    ('Albaranes de trazabilidad y justificante de congelación del pescado para consumo en crudo', 'En el local, un paso atrás', 'Sanidad (autonómica)'),
    ('Comunicación o declaración responsable de inicio de actividad y licencia', 'En el local', 'Ayuntamiento y Sanidad'),
]

# ==========================================================================
# 9. REFERENCIA LEGAL DE LAS TRES HOJAS NUEVAS DEL LIBRO 5 (SPEC D4)
# ==========================================================================
# Los textos legales largos NO viven aquí: llegan por id `MM-*`. Estas tablas
# sólo llevan el concepto, el valor corto, el id y el artículo.
# columnas: concepto, valor, mm_id, norma
TOPES_JORNADA = [
    ('Jornada máxima', '40 h/semana de promedio en cómputo anual', 'MM-01', 'Art. 34.1 ET'),
    ('Jornada ordinaria diaria máxima', '9 h, salvo distribución irregular pactada', 'MM-03', 'Art. 34.3 ET'),
    ('Descanso mínimo entre jornadas', '12 h', 'MM-03', 'Art. 34.3 ET'),
    ('Descanso semanal', '1,5 días, acumulables en periodos de hasta 14 días', 'MM-03', 'Art. 37.1 ET'),
    ('Descanso en jornada continuada de más de 6 h', '15 min; son tiempo de trabajo sólo si lo dice el convenio', 'MM-04', 'Art. 34.4 ET'),
    ('Horas extraordinarias', '80 h/año por persona, en proporción en la jornada parcial', 'MM-05', 'Art. 35.2 ET'),
    ('Horas complementarias pactadas', '30 % de las ordinarias, ampliable hasta el 60 % por convenio', 'MM-06', 'Art. 12.5 ET'),
    ('Horas complementarias voluntarias', '15 % adicional', 'MM-06', 'Art. 12.5 ET'),
    ('Registro de jornada', 'Diario, con hora de inicio y de fin', 'MM-02', 'Art. 34.9 ET'),
    ('Conservación del registro', '4 años', 'MM-02', 'Art. 34.9 ET'),
    ('Contrato a tiempo parcial sin registro', 'Se presume celebrado a jornada completa', 'MM-07', 'Art. 12.4.c ET'),
]

PERMISOS = [
    ('Vacaciones anuales', '30 días naturales, no sustituibles por dinero salvo extinción', 'MM-08', 'Art. 38 ET'),
    ('Preaviso del calendario de vacaciones', '2 meses antes del disfrute', 'MM-08', 'Art. 38.3 ET'),
    ('Fallecimiento de cónyuge, pareja de hecho o pariente hasta 2.º grado',
     '2 días, ampliables a 4 si hay desplazamiento', 'MM-27', 'Art. 37.3.b ET'),
    ('Accidente o enfermedad graves, hospitalización o intervención que precise reposo',
     '5 días', 'MM-27', 'Art. 37.3.b ET'),
    ('Fuerza mayor familiar', 'Hasta 4 días al año, computados POR HORAS', 'MM-27', 'Art. 37.9 ET'),
    ('Permiso parental hasta los 8 años', '8 semanas NO retribuidas', 'MM-26', 'Art. 48 bis ET'),
    ('Permiso parental retribuido hasta los 8 años', '2 semanas retribuidas', 'MM-26',
     'Art. 48.4.c ET (RDL 9/2025); prestación del art. 177 LGSS'),
    ('Nacimiento y cuidado de menor', '19 semanas por progenitor (32 en monoparentalidad)', 'MM-54', 'Art. 48.4 ET (RDL 9/2025)'),
    ('Guarda legal: reducción de jornada',
     'La concreción horaria la elige la persona trabajadora dentro de su jornada ordinaria', '', 'Art. 37.6 y 37.7 ET'),
    ('Adaptación de jornada por conciliación',
     'Si la empresa no contesta en el plazo legal, se entiende CONCEDIDA', '', 'Art. 34.8 ET'),
]
# ⚠ Las DOS figuras del permiso parental van siempre juntas (SPEC D6): decir
# «el permiso parental es retribuido» a secas, o «no es retribuido» a secas,
# está en la lista negra del guion.

REGIMEN_DISCIPLINARIO = [
    ('Falta LEVE: no registrar la jornada', '2 incumplimientos en un mes', '', 'Art. 38.10 ALEH VI (BOE-A-2026-18630)'),
    ('Falta LEVE: uso no autorizado del móvil durante el servicio', '', '', 'Art. 38.12 ALEH VI'),
    ('Falta GRAVE: no registrar la jornada', '3 o 4 incumplimientos en un mes', '', 'Art. 39.21 ALEH VI'),
    ('Falta GRAVE: fumar en zonas no permitidas', '', '', 'Art. 39.20 ALEH VI'),
    ('Falta MUY GRAVE: no registrar la jornada', '5 o más incumplimientos en un mes', '', 'Art. 40.14 ALEH VI'),
    ('Audiencia previa al despido disciplinario',
     '2 días para contestar; si se aparta del servicio, con permiso retribuido', 'MM-13',
     'Art. 41.3 ALEH VI, con su excepción, y remisión al art. 55.1 ET'),
    ('Vigencia de la modificación del ALEH VI', 'Del 04-09-2026 al 31-12-2030', 'MM-13', 'BOE-A-2026-18630'),
    ('Indemnización por despido objetivo',
     '20 días por año, tope de 12 mensualidades, a disposición con la carta', 'MM-12', 'Art. 53 ET'),
    ('Indemnización por despido improcedente', '33 días por año, tope de 24 mensualidades', 'MM-12', 'Art. 56 ET'),
    ('Periodo de prueba en hostelería',
     '90 / 60 / 45 días naturales según grupo; el convenio provincial no lo puede modificar', 'MM-11', 'ALEH VI'),
]

# ==========================================================================
# 10. REUNIONES, ACUERDOS Y PLAN DE 90 DÍAS (libro 6)
# ==========================================================================
# NO hay briefing: el briefing de servicio es DIARIO y ya existe veinte veces en
# el catálogo (kit-tareas/BONUS-01, kit-gestion-personal/BONUS-01). Este libro
# se ocupa de las tres cadencias que no cubre nadie: semanal, mensual y
# uno-a-uno. Las 12 reuniones son las del trimestre CERRADO (junio-agosto de
# 2026), el mismo del registro de quejas y de las tres auditorías; todas caen en
# lunes, que es el día que el restaurante cierra.
# columnas: fecha, tipo, cadencia, asistentes, duración (min), responsable, estado
REUNIONES = [
    ('2026-06-01', 'Mensual de resultados', 'Mensual', 'P01, P02, P03', 60, 'P01', 'Celebrada'),
    ('2026-06-08', 'Semanal de equipo', 'Semanal', 'Todo el equipo', 30, 'P01', 'Celebrada'),
    ('2026-06-15', 'Uno-a-uno', 'Mensual', 'P01 y P08', 30, 'P01', 'Celebrada'),
    ('2026-06-22', 'Semanal de equipo', 'Semanal', 'Todo el equipo', 30, 'P01', 'Celebrada'),
    ('2026-07-06', 'Mensual de resultados', 'Mensual', 'P01, P02, P03', 60, 'P01', 'Celebrada'),
    ('2026-07-13', 'Semanal de equipo', 'Semanal', 'Todo el equipo', 30, 'P01', 'Celebrada'),
    ('2026-07-20', 'Uno-a-uno', 'Mensual', 'P01 y P05', 30, 'P01', 'Celebrada'),
    ('2026-07-27', 'Semanal de equipo', 'Semanal', 'Todo el equipo', 30, 'P01', 'Celebrada'),
    ('2026-08-03', 'Mensual de resultados', 'Mensual', 'P01, P02, P03', 60, 'P01', 'Celebrada'),
    ('2026-08-10', 'Semanal de equipo', 'Semanal', 'Todo el equipo', 30, 'P01', 'Celebrada'),
    ('2026-08-17', 'Uno-a-uno', 'Mensual', 'P01 y P09', 30, 'P01', 'Celebrada'),
    ('2026-08-24', 'Semanal de equipo', 'Semanal', 'Todo el equipo', 30, 'P01', 'Celebrada'),
]

# Guion de la reunión semanal: 30 minutos, siete puntos, y el último es el que
# convierte la conversación en trabajo.
# columnas: orden, punto, minutos, herramienta de la que salen los datos
GUION_REUNION_SEMANAL = [
    (1, 'Los números de la semana que cierra', 5, 'Cuadro de mando semanal'),
    (2, 'Qué hay detrás de cada semáforo en rojo', 5, 'Cuadro de mando semanal'),
    (3, 'Quejas y reseñas de la semana: qué se repite', 4, 'Quejas, reclamaciones y reseñas'),
    (4, 'Acuerdos de la semana anterior: cerrados y pendientes', 4, 'Actas y Acuerdos'),
    (5, 'La semana que entra: reservas, eventos y cuadrante', 5, 'Cuadrante (Kit de Gestión de Personal)'),
    (6, 'Un punto que trae el equipo, por turno rotatorio', 4, ''),
    (7, 'Acuerdos nuevos: qué, quién y para cuándo', 3, 'Actas y Acuerdos'),
]

# Uno-a-uno: seis preguntas. Ninguna sobre salud, familia ni vida privada.
UNO_A_UNO = [
    '¿Qué te está saliendo bien desde la última vez que hablamos?',
    '¿Qué te está costando y qué necesitas de mí para desatascarlo?',
    '¿Hay algo del servicio que tú harías de otra manera?',
    '¿Qué estación te gustaría aprender o dominar mejor?',
    '¿Hay algo que yo debería saber y que no te he preguntado?',
    '¿Qué compromiso concreto nos llevamos cada uno de esta conversación?',
]

# 25 acuerdos de esas reuniones. Cuatro están VENCIDOS a la fecha de corte
# (2026-09-04): fecha de compromiso pasada y estado distinto de «Cerrado». Es
# lo que el libro tiene que enseñar a ver de un vistazo.
# columnas: id, fecha de la reunión, acuerdo, responsable, fecha de compromiso, estado,
#           fecha de cierre real (vacía si no está «Cerrado»)
# M6 (auditoría 2026-09-04): los 15 acuerdos «Cerrado» sembraban SIN fecha de
# cierre real, así que «% cerrados en plazo» salía vacío y la columna
# «Situación» nunca mostraba «Cerrado en plazo» / «Cerrado fuera de plazo» en
# el fichero que compra el cliente. A08 y A14 se cierran DESPUÉS de su fecha
# de seguimiento a propósito, para que se vea también «Cerrado fuera de plazo».
ACUERDOS = [
    ('A01', '2026-06-01', 'Publicar el cuadrante de julio con 15 días de antelación', 'P01', '2026-06-15', 'Cerrado', '2026-06-14'),
    ('A02', '2026-06-01', 'Revisar el escandallo de los cinco platos más vendidos', 'P02', '2026-06-30', 'Cerrado', '2026-06-28'),
    ('A03', '2026-06-01', 'Cambiar el proveedor de pescado por rendimiento', 'P02', '2026-07-15', 'Cerrado', '2026-07-14'),
    ('A04', '2026-06-08', 'Anotar la hora de comanda de todas las mesas del viernes', 'P08', '2026-06-19', 'Cerrado', '2026-06-18'),
    ('A05', '2026-06-08', 'Repasar con P11 el cobro dividido en el TPV', 'P03', '2026-06-22', 'Cerrado', '2026-06-20'),
    ('A06', '2026-06-15', 'Formar a P10 en barra hasta nivel 2', 'P09', '2026-10-31', 'En curso', ''),
    # M8 (auditoría 2026-09-04): «arqueo» es vocabulario de España; en buena
    # parte de LATAM se dice «corte de caja». Primera y única aparición del
    # término en este libro.
    ('A07', '2026-06-15', 'Dar a P08 la firma del arqueo (corte de caja, en el uso de otros países) dos días por semana', 'P01', '2026-07-01', 'Cerrado', '2026-06-30'),
    ('A08', '2026-06-22', 'Pedir presupuesto de limpieza de conductos', 'P01', '2026-07-10', 'Cerrado', '2026-07-14'),
    ('A09', '2026-06-22', 'Escribir el soporte de alérgenos de los platos nuevos', 'P02', '2026-08-15', 'En curso', ''),
    ('A10', '2026-07-06', 'Analizar los tiempos de pase de los viernes noche', 'P02', '2026-07-31', 'Cerrado', '2026-07-30'),
    ('A11', '2026-07-06', 'Abrir una segunda plancha los viernes y sábados', 'P02', '2026-07-24', 'Cerrado', '2026-07-23'),
    ('A12', '2026-07-06', 'Avisar del tiempo real de espera al sentar a la mesa', 'P03', '2026-07-17', 'Cerrado', '2026-07-16'),
    ('A13', '2026-07-13', 'Contestar todas las reseñas en menos de 48 horas', 'P01', '2026-07-31', 'Cerrado', '2026-07-29'),
    ('A14', '2026-07-13', 'Confirmar por SMS las reservas de más de cuatro personas', 'P03', '2026-08-07', 'Cerrado', '2026-08-11'),
    ('A15', '2026-07-20', 'Empezar el cross-training de P06 en la partida fría', 'P05', '2026-10-15', 'En curso', ''),
    ('A16', '2026-07-20', 'Preparar la ficha de evaluación de P05 para septiembre', 'P01', '2026-09-15', 'Pendiente', ''),
    ('A17', '2026-07-27', 'Actualizar el cartel de la hoja de reclamaciones', 'P01', '2026-08-10', 'Cerrado', '2026-08-09'),
    ('A18', '2026-07-27', 'Contestar por escrito la reclamación GI-2026-0463', 'P01', '2026-08-25', 'Pendiente', ''),
    ('A19', '2026-08-03', 'Renegociar el precio del solomillo con el proveedor', 'P02', '2026-09-30', 'En curso', ''),
    ('A20', '2026-08-03', 'Revisar el retimbrado de los extintores', 'P01', '2026-08-31', 'Pendiente', ''),
    ('A21', '2026-08-03', 'Cerrar el plan de vacaciones de invierno', 'P01', '2026-10-31', 'En curso', ''),
    ('A22', '2026-08-10', 'Repasar el orden de salida de platos por mesa', 'P02', '2026-08-24', 'Cerrado', '2026-08-23'),
    ('A23', '2026-08-10', 'Bajar el volumen del hilo musical en el turno de cena', 'P03', '2026-08-21', 'Cerrado', '2026-08-20'),
    ('A24', '2026-08-17', 'Definir la ruta de P09 hacia jefa de rango', 'P01', '2026-08-31', 'Pendiente', ''),
    ('A25', '2026-08-24', 'Preparar el plan de 90 días con las siete herramientas', 'P01', '2026-09-07', 'En curso', ''),
]

# Plan de 90 días: 20 decisiones que SALEN de las otras seis herramientas.
# Arranca el lunes 7 de septiembre de 2026 (semana ISO 37), el lunes siguiente a
# la semana 36, que cerró en 66,8 % de prime cost. El impacto en euros es una
# ESTIMACIÓN editable del usuario, no una promesa.
# áreas: Personas · Servicio · Operaciones · Cumplimiento · Finanzas
# columnas: área, herramienta de origen, decisión, responsable, semana (1-13),
#           impacto €/mes estimado, estado
PLAN_90 = [
    ('Personas', 'Matriz de formación y polivalencia',
     'Llevar a P06 a nivel 2 en la partida fría: es el único punto único de fallo del equipo', 'P05', 1, 0.0, 'En curso'),
    ('Finanzas', 'Cuadro de mando semanal',
     'Cerrar el cuadro todos los lunes antes de las 12:00 y publicar el semáforo', 'P01', 1, 0.0, 'En curso'),
    ('Servicio', 'Quejas, reclamaciones y reseñas',
     'Avisar del tiempo real de espera al sentar en todos los servicios de viernes y sábado', 'P03', 1, 220.0, 'En curso'),
    ('Cumplimiento', 'Calendario de cumplimiento legal',
     'Contratar el retimbrado de los extintores, vencido desde mayo', 'P01', 2, 0.0, 'Pendiente'),
    # B1 (auditoría 2026-09-04): la herramienta de origen de ESTA decisión es
    # el libro de quejas (Reclamaciones Formales!A6, 39 días contra un plazo
    # de 30/28), no el calendario de cumplimiento legal.
    ('Cumplimiento', 'Quejas, reclamaciones y reseñas',
     'Contestar por escrito la reclamación GI-2026-0463 y revisar por qué se pasó el mes', 'P01', 2, 0.0, 'Pendiente'),
    ('Servicio', 'Auditoría interna de servicio',
     'Recuperar el área de aseos y limpieza, la única que empeora entre la visita 1 y la 3', 'P03', 2, 0.0, 'Pendiente'),
    ('Finanzas', 'Cuadro de mando semanal',
     'Analizar las cuatro semanas fuera de objetivo del año y qué tuvieron en común', 'P01', 3, 0.0, 'Pendiente'),
    ('Operaciones', 'Cuadro de mando semanal',
     'Ajustar el pedido de la semana 33 y 35 tipo: en agosto se compró para una demanda que no llegó', 'P02', 3, 380.0, 'Pendiente'),
    ('Personas', 'Reuniones, acuerdos y plan de 90 días',
     'Cerrar los cuatro acuerdos vencidos antes de abrir ninguno nuevo', 'P01', 3, 0.0, 'Pendiente'),
    ('Servicio', 'Quejas, reclamaciones y reseñas',
     'Responder toda reseña en menos de 48 h, con un responsable nombrado', 'P01', 4, 0.0, 'Pendiente'),
    ('Personas', 'Scorecard de selección',
     'Cubrir la vacante de camarero/a con el scorecard y las 24 preguntas, sin entrevista libre', 'P01', 4, 0.0, 'Pendiente'),
    ('Operaciones', 'Auditoría interna de servicio',
     'Escribir el estándar de los diez puntos peor puntuados en la visita 3', 'P03', 5, 0.0, 'Pendiente'),
    ('Personas', 'Matriz de formación y polivalencia',
     'Segunda persona a nivel 2 en la partida fría (P04) antes de la campaña de Navidad', 'P05', 6, 0.0, 'Pendiente'),
    ('Finanzas', 'Cuadro de mando semanal',
     'Revisar el precio de los cinco platos con peor margen de la carta', 'P02', 6, 640.0, 'Pendiente'),
    ('Cumplimiento', 'Calendario de cumplimiento legal',
     'Poner por escrito la política de desconexión digital y comunicarla al equipo', 'P01', 7, 0.0, 'Pendiente'),
    ('Personas', 'Reuniones, acuerdos y plan de 90 días',
     'Uno-a-uno con las doce personas del equipo, uno por semana', 'P01', 8, 0.0, 'Pendiente'),
    ('Servicio', 'Quejas, reclamaciones y reseñas',
     'Medir el tiempo de espera de la primera bebida en todas las mesas durante dos semanas', 'P08', 9, 0.0, 'Pendiente'),
    ('Operaciones', 'Cuadro de mando semanal',
     'Cuadrar horas trabajadas y horas de apertura en las cuatro semanas de más venta', 'P01', 10, 520.0, 'Pendiente'),
    ('Cumplimiento', 'Calendario de cumplimiento legal',
     'Pedir por escrito al proveedor del TPV la fecha de su versión adaptada a Verifactu', 'P01', 11, 0.0, 'Pendiente'),
    ('Finanzas', 'Reuniones, acuerdos y plan de 90 días',
     'Presentar al propietario el mes 0 contra el mes 3 con el cuadro semanal delante', 'P01', 13, 0.0, 'Pendiente'),
]
AREAS_PLAN_90 = ('Personas', 'Servicio', 'Operaciones', 'Cumplimiento', 'Finanzas')
HERRAMIENTAS_PACK = (
    'Cuadro de mando semanal',
    'Matriz de formación y polivalencia',
    'Quejas, reclamaciones y reseñas',
    'Scorecard de selección',
    'Calendario de cumplimiento legal',
    'Reuniones, acuerdos y plan de 90 días',
    'Auditoría interna de servicio',
)

# ==========================================================================
# 11. AUDITORÍA INTERNA DE SERVICIO (libro 7)
# ==========================================================================
# 60 puntos en 6 áreas. EXCLUYE a propósito APPCC y seguridad alimentaria: eso
# es el Pack APPCC, y mezclarlo aquí produciría un checklist que no sirve ni
# para una cosa ni para la otra. Lo que mide esta hoja es la EXPERIENCIA y el
# estándar de marca, que es lo que un cliente ve y ningún registro sanitario
# recoge.
# columnas: nº, área, punto de control, peso (1-3)
AUDITORIA = [
    (1, 'Llegada y reserva', 'La reserva telefónica se atiende antes de cuatro tonos', 2),
    (2, 'Llegada y reserva', 'Se confirma nombre, hora, número de comensales y teléfono', 2),
    (3, 'Llegada y reserva', 'Se pregunta por alergias e intolerancias al reservar', 3),
    (4, 'Llegada y reserva', 'La reserva online se confirma por escrito el mismo día', 2),
    (5, 'Llegada y reserva', 'Hay alguien recibiendo en la puerta al abrir el servicio', 3),
    (6, 'Llegada y reserva', 'Se saluda y se acompaña a la mesa en menos de un minuto', 3),
    (7, 'Llegada y reserva', 'La mesa está montada y limpia cuando llega el cliente', 3),
    (8, 'Llegada y reserva', 'Se ofrece dónde dejar abrigos y bolsos', 1),
    (9, 'Llegada y reserva', 'Si hay demora, se informa del tiempo real de espera', 3),
    (10, 'Llegada y reserva', 'El acceso está libre de obstáculos y es practicable', 2),
    (11, 'Sala y ambiente', 'Temperatura agradable en toda la sala, también junto a la puerta', 2),
    (12, 'Sala y ambiente', 'Volumen de la música adecuado al turno', 2),
    (13, 'Sala y ambiente', 'Iluminación correcta en mesas y zonas de paso', 2),
    (14, 'Sala y ambiente', 'Mantelería y servilletas sin manchas ni roturas', 3),
    (15, 'Sala y ambiente', 'Cristalería sin marcas de agua ni de cal', 3),
    (16, 'Sala y ambiente', 'Cubertería pulida y completa en cada montaje', 3),
    (17, 'Sala y ambiente', 'Cartas limpias, sin roturas y sin precios corregidos a mano', 3),
    (18, 'Sala y ambiente', 'Sillas y mesas estables y sin desperfectos', 2),
    (19, 'Sala y ambiente', 'Decoración y plantas en buen estado', 1),
    (20, 'Sala y ambiente', 'Paso entre mesas suficiente para servir sin molestar', 2),
    (21, 'Servicio y tiempos', 'Se toma la comanda de bebida en menos de tres minutos', 3),
    (22, 'Servicio y tiempos', 'La primera bebida llega en menos de cinco minutos', 3),
    (23, 'Servicio y tiempos', 'El personal conoce la carta y sabe recomendar', 3),
    (24, 'Servicio y tiempos', 'El personal informa de los alérgenos sin remitir al cartel', 3),
    (25, 'Servicio y tiempos', 'Los entrantes salen en menos de quince minutos', 3),
    (26, 'Servicio y tiempos', 'Los platos de una misma mesa salen a la vez', 3),
    (27, 'Servicio y tiempos', 'Se retira el plato sucio antes de servir el siguiente', 2),
    (28, 'Servicio y tiempos', 'Se ofrece postre, café y sobremesa', 2),
    (29, 'Servicio y tiempos', 'La cuenta llega en menos de cinco minutos desde que se pide', 3),
    (30, 'Servicio y tiempos', 'Se despide al cliente en la puerta', 2),
    (31, 'Producto y presentación', 'El plato llega a la temperatura correcta', 3),
    (32, 'Producto y presentación', 'La presentación coincide con el estándar de la ficha', 3),
    (33, 'Producto y presentación', 'La ración coincide con el gramaje escandallado', 3),
    (34, 'Producto y presentación', 'El pan es del día y se sirve como está definido', 2),
    (35, 'Producto y presentación', 'Las guarniciones son las de la ficha, sin sustituciones mudas', 2),
    (36, 'Producto y presentación', 'El vino se sirve a la temperatura y en la cristalería correctas', 2),
    (37, 'Producto y presentación', 'La cerveza de barril sale con su corona y sin exceso de espuma', 2),
    (38, 'Producto y presentación', 'El café se sirve caliente y con su acompañamiento', 2),
    (39, 'Producto y presentación', 'Los postres se montan en el momento, no con antelación', 2),
    (40, 'Producto y presentación', 'No hay platos agotados sin avisar al empezar el servicio', 3),
    (41, 'Aseos y limpieza', 'Los aseos se revisan al menos una vez por turno y queda anotado', 3),
    (42, 'Aseos y limpieza', 'Hay papel, jabón y secamanos en todos los aseos', 3),
    (43, 'Aseos y limpieza', 'Inodoros y lavabos sin suciedad visible', 3),
    (44, 'Aseos y limpieza', 'Suelo del aseo seco y sin residuos', 2),
    (45, 'Aseos y limpieza', 'Papelera con tapa y sin desbordar', 2),
    (46, 'Aseos y limpieza', 'Espejo y grifería sin cal', 1),
    (47, 'Aseos y limpieza', 'Olor neutro, sin ambientador que tape', 2),
    (48, 'Aseos y limpieza', 'Aseo accesible señalizado y practicable', 2),
    (49, 'Aseos y limpieza', 'Suelo de sala sin restos entre servicios', 2),
    (50, 'Aseos y limpieza', 'Entrada, cristales y terraza limpios al abrir', 2),
    (51, 'Marca y digital', 'La carta publicada en la web coincide con la de la sala', 3),
    (52, 'Marca y digital', 'Los precios de la web y de las plataformas están actualizados', 3),
    (53, 'Marca y digital', 'El horario publicado en Google coincide con el real, festivos incluidos', 3),
    (54, 'Marca y digital', 'Las fotos publicadas corresponden a los platos actuales', 2),
    (55, 'Marca y digital', 'Las reseñas de los últimos 30 días están respondidas', 2),
    (56, 'Marca y digital', 'Teléfono y enlace de reserva visibles en el perfil', 2),
    (57, 'Marca y digital', 'La información de alérgenos está también en la web', 2),
    (58, 'Marca y digital', 'El cartel de la hoja de reclamaciones está a la vista', 3),
    (59, 'Marca y digital', 'Los precios expuestos al público incluyen el IVA', 3),
    (60, 'Marca y digital', 'Hay publicación en redes en el último mes', 1),
]
AREAS_AUDITORIA = ('Llegada y reserva', 'Sala y ambiente', 'Servicio y tiempos',
                   'Producto y presentación', 'Aseos y limpieza', 'Marca y digital')

# Tres visitas del trimestre cerrado, con puntuación 0-5 en cada uno de los 60
# puntos, en el orden de AUDITORIA. La tendencia global sube (3,33 → 3,65 →
# 3,92 de media simple) pero UN área empeora visita tras visita —«Aseos y
# limpieza», 4,0 → 3,6 → 3,1—, que es justo lo que una media global esconde y
# lo que la hoja «Resumen por Área» tiene que hacer visible.
# columnas: nº de visita, fecha, auditor, puntuaciones (60)
AUDITORIAS_HECHAS = [
    (1, '2026-06-12', 'P01 (visita propia)', [
        4, 4, 3, 2, 3, 4, 3, 2, 3, 4, 4, 4,
        3, 3, 4, 4, 3, 3, 3, 4, 3, 2, 2, 3,
        4, 3, 2, 2, 4, 4, 4, 3, 3, 5, 4, 3,
        3, 4, 5, 4, 3, 3, 4, 5, 4, 3, 4, 5,
        5, 4, 2, 2, 3, 3, 2, 2, 3, 4, 3, 2,
    ]),
    (2, '2026-07-17', 'Cliente misterioso externo', [
        5, 4, 3, 3, 4, 4, 4, 3, 3, 4, 5, 3,
        3, 4, 5, 4, 3, 3, 4, 5, 4, 3, 3, 4,
        4, 3, 3, 3, 4, 4, 4, 3, 4, 5, 5, 3,
        3, 4, 5, 4, 3, 3, 4, 5, 3, 3, 3, 5,
        4, 3, 2, 3, 4, 4, 3, 3, 4, 4, 3, 2,
    ]),
    (3, '2026-08-21', 'P01 (visita propia)', [
        5, 4, 3, 4, 5, 5, 3, 3, 4, 5, 4, 3,
        4, 5, 5, 4, 3, 4, 5, 5, 4, 3, 4, 5,
        5, 3, 3, 4, 5, 4, 4, 4, 5, 5, 4, 3,
        4, 5, 5, 4, 2, 3, 4, 4, 3, 2, 3, 4,
        4, 2, 3, 4, 5, 4, 3, 3, 4, 5, 4, 3,
    ]),
]

# ==========================================================================
# 12. PIE DE LOS LIBROS
# ==========================================================================
VERSION_LINE = ('Versión 1.0 · septiembre 2026 · '
                'aichef.pro/manual-manager-restaurante · info@aichef.pro')
BIO = ('Diseñado por John Guerrero — chef y consultor gastronómico desde 2010 '
       '· johnguerrero.es')
NOTA_DESPROTEGER = ('Para editar la estructura o una celda que no esté en '
                    'verde, desprotege la hoja (sin contraseña).')


# ==========================================================================
# 13. VERIFICACIÓN
# ==========================================================================
def _lunes_iso(anio, semana):
    """Lunes de la semana ISO indicada. `date.fromisocalendar` es de Python 3.8
    y aquí se ejecuta también con 3.7."""
    ene4 = dt.date(anio, 1, 4)
    return ene4 - dt.timedelta(days=ene4.isoweekday() - 1) + dt.timedelta(weeks=semana - 1)


def _fecha(s):
    return dt.datetime.strptime(s, '%Y-%m-%d').date()


def _guia_food_cost():
    """Importa el datos_ejemplo.py de la Guía Food Cost con un nombre de módulo
    PROPIO. Si se importara como `datos_ejemplo` chocaría con este mismo fichero
    cuando lo carga un constructor. Devuelve None si no está el fichero."""
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'guia-food-cost', 'datos_ejemplo.py')
    ruta = os.path.normpath(ruta)
    if not os.path.exists(ruta):
        return None
    spec = importlib.util.spec_from_file_location('datos_guia_food_cost', ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _pct(a, b):
    return 100.0 * (a / float(b) - 1.0)


def semanas_calculadas():
    """Recalcula los KPI de cada semana. Devuelve una lista de dicts."""
    out = []
    for fila in SEMANAS:
        (sem, mes, vcom, vbeb, si, compras, sf, salarios, otros,
         cubiertos, tickets, h_apertura, h_trabajadas) = fila
        ventas = vcom + vbeb
        consumo = si + compras - sf
        personal = salarios * (1 + SS_EMPRESA) + otros
        out.append({
            'semana': sem, 'mes': mes, 'lunes': _lunes_iso(2026, sem),
            'ventas': ventas, 'consumo': consumo, 'personal': personal,
            'salarios': salarios, 'otros': otros, 'compras': compras,
            'stock_ini': si, 'stock_fin': sf,
            'food_cost': consumo / float(ventas),
            'labor_cost': personal / float(ventas),
            'prime_cost': (consumo + personal) / float(ventas),
            'margen_tras_prime': ventas - consumo - personal,
            'ticket_medio': ventas / float(tickets),
            'gasto_cubierto': ventas / float(cubiertos),
            'cubiertos': cubiertos, 'tickets': tickets,
            'cubiertos_hora': cubiertos / float(h_apertura),
            'ventas_hora': ventas / float(h_trabajadas),
        })
    return out


def checks():
    fallos = []
    avisos = []

    def exige(cond, mensaje):
        if not cond:
            fallos.append(mensaje)

    # ---- 1. plantilla ----------------------------------------------------
    exige(len(PLANTILLA) == 12, 'La plantilla no tiene 12 personas')
    bruto_anual = sum(p[7] for p in PLANTILLA)
    coste_mes_plantilla = bruto_anual * (1 + SS_EMPRESA) / 12.0
    ids = [p[0] for p in PLANTILLA]
    exige(len(set(ids)) == 12, 'Hay ids repetidos en la plantilla')
    exige(all(p[9] in ESTACIONES for p in PLANTILLA),
          'Alguien tiene una estación principal que no está en ESTACIONES')
    exige(all(p[3] in ('Área 1ª', 'Área 2ª', 'Área 3ª') for p in PLANTILLA),
          'Área funcional del ALEH fuera de las tres que tiene un restaurante')
    exige(all(p[4] in ('Grupo I', 'Grupo II', 'Grupo III') for p in PLANTILLA),
          'Grupo profesional del ALEH fuera de I/II/III')

    # ---- 2. coherencia con la Guía Food Cost -----------------------------
    G = _guia_food_cost()
    if G is None:
        avisos.append('No se encontró ../guia-food-cost/datos_ejemplo.py: '
                      'el cuadre se comprueba contra la copia local')
        guia_mensual = REFERENCIA_GUIA_FOOD_COST
    else:
        guia_mensual = G.CUADRO_MENSUAL
        exige(list(map(tuple, guia_mensual)) == list(map(tuple, REFERENCIA_GUIA_FOOD_COST)),
              'REFERENCIA_GUIA_FOOD_COST ya no coincide con el CUADRO_MENSUAL de la Guía Food Cost')
        for campo in ('nombre', 'formato', 'servicios_mes', 'cubiertos_mes',
                      'food_cost_objetivo', 'iva_sala'):
            exige(RESTAURANTE[campo] == G.RESTAURANTE[campo],
                  'El campo %s de RESTAURANTE no coincide con el de la Guía Food Cost' % campo)

    guia_salarios_anual = sum(m[5] for m in guia_mensual)
    guia_otros_anual = sum(m[6] for m in guia_mensual)
    guia_coste_mes = guia_salarios_anual * (1 + SS_EMPRESA) / 12.0
    desv_plantilla = _pct(coste_mes_plantilla, guia_coste_mes)
    exige(abs(desv_plantilla) <= 5.0,
          'El coste de personal de la plantilla se desvía %.2f %% del de la Guía (tope 5 %%)' % desv_plantilla)

    # ---- 3. semanas ------------------------------------------------------
    sc = semanas_calculadas()
    exige(len(SEMANAS) == 52, 'El año semanal no tiene 52 filas')
    exige([s['semana'] for s in sc] == list(range(1, 53)),
          'Las semanas ISO no van de 1 a 52 en orden')
    for s in sc:
        jueves = s['lunes'] + dt.timedelta(days=3)
        exige(jueves.month == s['mes'],
              'La semana %d está asignada al mes %d y su jueves cae en el %d' % (s['semana'], s['mes'], jueves.month))
    for i in range(1, len(SEMANAS)):
        exige(SEMANAS[i][4] == SEMANAS[i - 1][6],
              'El stock inicial de la semana %d no es el final de la anterior' % SEMANAS[i][0])

    # cuadre mensual: se compara la VENTA MEDIA DIARIA (ver §4)
    peor = 0.0
    for m in range(1, 13):
        fs = [s for s in sc if s['mes'] == m]
        n = len(fs)
        dias = DIAS_MES_2026[m - 1]
        g = guia_mensual[m - 1]
        objetivos = [
            ('ventas', sum(f['ventas'] for f in fs) / n * dias / 7.0, g[0] + g[1]),
            ('consumo', sum(f['consumo'] for f in fs) / n * dias / 7.0, g[2] + g[3] - g[4]),
            ('compras', sum(f['compras'] for f in fs) / n * dias / 7.0, g[3]),
            ('salarios', sum(f['salarios'] for f in fs) / n * dias / 7.0, g[5]),
            ('otros', sum(f['otros'] for f in fs) / n * dias / 7.0, g[6]),
        ]
        for nombre, calc, ref in objetivos:
            d = _pct(calc, ref)
            peor = max(peor, abs(d))
            exige(abs(d) <= 3.0,
                  '%s de %s se desvía %.2f %% del año mensual de la Guía (tope 3 %%)' % (nombre, MESES[m - 1], d))

    ventas_anio = sum(s['ventas'] for s in sc)
    consumo_anio = sum(s['consumo'] for s in sc)
    salarios_anio = sum(s['salarios'] for s in sc)
    otros_anio = sum(s['otros'] for s in sc)
    personal_anio = salarios_anio * (1 + SS_EMPRESA) + otros_anio
    cubiertos_anio = sum(s['cubiertos'] for s in sc)
    tickets_anio = sum(s['tickets'] for s in sc)
    guia_ventas_anio = sum(m[0] + m[1] for m in guia_mensual)
    guia_consumo_anio = sum(m[2] + m[3] - m[4] for m in guia_mensual)
    for nombre, calc, ref in (
            ('ventas', ventas_anio, guia_ventas_anio),
            ('consumo', consumo_anio, guia_consumo_anio),
            ('salarios', salarios_anio, guia_salarios_anual),
            ('cubiertos', cubiertos_anio, RESTAURANTE['cubiertos_mes'] * 12)):
        d = _pct(calc, ref)
        exige(abs(d) <= 3.0, 'El total anual de %s se desvía %.2f %% (tope 3 %%)' % (nombre, d))

    objetivo = RESTAURANTE['prime_cost_objetivo_sala']
    malas = [s for s in sc if s['prime_cost'] > objetivo]
    exige(len(malas) == 4,
          'Hay %d semanas por encima del objetivo de prime cost y deberían ser 4' % len(malas))
    exige(tuple(s['semana'] for s in malas) == SEMANAS_FUERA_DE_OBJETIVO,
          'Las semanas fuera de objetivo no son las declaradas en SEMANAS_FUERA_DE_OBJETIVO')
    bonus = [s for s in sc if s['semana'] == SEMANA_BONUS_PRIME_71][0]
    exige(abs(bonus['prime_cost'] - 0.71) <= 0.0015,
          'La semana del bonus cierra en %.2f %% y el bonus dice 71,0 %%' % (100 * bonus['prime_cost']))

    ticket_medio_anio = ventas_anio / float(tickets_anio)
    gasto_cubierto_anio = ventas_anio / float(cubiertos_anio)
    exige(50.0 <= ticket_medio_anio <= 60.0,
          'El ticket medio anual (%.2f €) se sale de la banda coherente con la carta de La Encina' % ticket_medio_anio)
    exige(24.0 <= gasto_cubierto_anio <= 29.0,
          'El gasto medio por cubierto (%.2f €) no cuadra con los PVP de la carta' % gasto_cubierto_anio)
    exige(all(2.0 <= s['ticket_medio'] / s['gasto_cubierto'] <= 2.3 for s in sc),
          'Hay semanas con un número de comensales por ticket poco creíble')

    # ---- 4. polivalencia -------------------------------------------------
    exige(len(POLIVALENCIA) == 12, 'La matriz de polivalencia no tiene 12 filas')
    exige([p[0] for p in POLIVALENCIA] == ids, 'La matriz no sigue el orden de la plantilla')
    exige(all(len(p[1]) == 6 for p in POLIVALENCIA), 'Alguna fila de la matriz no tiene 6 estaciones')
    exige(all(all(0 <= n <= 3 for n in p[1]) for p in POLIVALENCIA), 'Nivel de polivalencia fuera de 0-3')
    cobertura = []
    for j, est in enumerate(ESTACIONES):
        cobertura.append((est, sum(1 for p in POLIVALENCIA if p[1][j] >= 2)))
    puntos_unicos = [e for e, c in cobertura if c == 1]
    exige(len(puntos_unicos) == 1,
          'Debería haber exactamente un punto único de fallo y hay %d' % len(puntos_unicos))
    exige(puntos_unicos and puntos_unicos[0] == 'Fríos y entrantes',
          'El punto único de fallo no es la partida fría (situación 10 del bonus)')
    exige(max(c for _, c in cobertura) >= 5, 'Ninguna estación está bien cubierta')
    exige(all(p[1][ESTACIONES.index(p_est)] >= 1
              for p, p_est in zip(POLIVALENCIA, [x[9] for x in PLANTILLA])),
          'Alguien tiene nivel 0 en su propia estación principal')
    exige(all(f[0] in ids and f[1] in ESTACIONES for f in PLAN_CROSS_TRAINING),
          'El plan de cross-training apunta a alguien o a alguna estación que no existe')
    exige(6 <= len(PLAN_CROSS_TRAINING) <= 8, 'El plan de cross-training debe tener entre 6 y 8 filas')

    # ---- 5. quejas, reclamaciones y reseñas ------------------------------
    exige(len(QUEJAS) == 30, 'No hay 30 quejas')
    exige(all(q[2] in MOTIVOS_QUEJA for q in QUEJAS), 'Hay una queja con un motivo fuera de la lista cerrada')
    exige(all(q[1] in CANALES_QUEJA for q in QUEJAS), 'Hay una queja con un canal fuera de la lista cerrada')
    exige(all(q[3] in (1, 2, 3) for q in QUEJAS), 'Gravedad de queja fuera de 1-3')
    exige(all(q[4] in ids for q in QUEJAS), 'Hay una queja asignada a alguien que no está en la plantilla')
    conteo = {}
    for q in QUEJAS:
        conteo[q[2]] = conteo.get(q[2], 0) + 1
    orden = sorted(conteo.items(), key=lambda kv: -kv[1])
    motivo_top, n_top = orden[0]
    exige(n_top >= 2 * orden[1][1],
          'Ningún motivo de queja destaca con claridad sobre el segundo')

    exige(len(RECLAMACIONES) == 3, 'No hay 3 reclamaciones formales')
    fuera = []
    for f_entrega, num, com, f_resp in RECLAMACIONES:
        dias = (_fecha(f_resp) - _fecha(f_entrega)).days
        if com == 'Cataluña' and dias > 31:
            fuera.append((num, dias))
    exige(len(fuera) == 1, 'Debería haber exactamente una reclamación fuera de plazo y hay %d' % len(fuera))

    exige(len(RESENAS) == 40, 'No hay 40 reseñas')
    exige(all(1 <= r[2] <= 5 for r in RESENAS), 'Estrellas fuera de 1-5')
    medias = []
    for mes in range(3, 9):
        vals = [r[2] for r in RESENAS if _fecha(r[1]).month == mes]
        exige(len(vals) > 0, 'El mes %d no tiene reseñas' % mes)
        medias.append((mes, sum(vals) / float(len(vals))))
    caidas = [i for i in range(1, len(medias) - 1)
              if medias[i][1] <= medias[i - 1][1] - 0.5 and medias[i + 1][1] >= medias[i][1] + 0.5]
    exige(len(caidas) == 1, 'La media de reseñas debe bajar un mes y recuperarse al siguiente')

    # ---- 6. selección ----------------------------------------------------
    comp = SELECCION['competencias']
    exige(len(comp) == 8, 'El scorecard no tiene 8 competencias')
    exige(all(1 <= c[1] <= 3 for c in comp), 'Peso de competencia fuera de 1-3')
    exige(len(SELECCION['candidatos']) == 4, 'No hay 4 candidatos')
    n_na = sum(1 for _, punt in SELECCION['candidatos'] for p in punt if p is None)
    exige(n_na == 1, 'Debe haber exactamente un N/A en el scorecard y hay %d' % n_na)
    medias_cand = []
    for nombre, punt in SELECCION['candidatos']:
        exige(len(punt) == 8, 'El candidato %s no tiene 8 puntuaciones' % nombre)
        exige(all(p is None or 1 <= p <= 5 for p in punt), 'Puntuación fuera de 1-5 en %s' % nombre)
        num = sum(p * c[1] for p, c in zip(punt, comp) if p is not None)
        den = sum(c[1] for p, c in zip(punt, comp) if p is not None)
        medias_cand.append((nombre, num / float(den)))
    umbral = SELECCION['umbral_recomendacion']
    exige(any(m >= umbral for _, m in medias_cand) and any(m < umbral for _, m in medias_cand),
          'El umbral no separa a ningún candidato: el ejemplo no enseña nada')

    exige(len(PREGUNTAS_COMPETENCIA) == 24, 'No hay 24 preguntas de entrevista')
    for c, _ in comp:
        n = sum(1 for x in PREGUNTAS_COMPETENCIA if x[0] == c)
        exige(n == 3, 'La competencia «%s» tiene %d preguntas y deben ser 3' % (c, n))
    prohibidas = ('salud', 'enferm', 'embaraz', 'hijo', 'hijos', 'familia', 'pareja',
                  'casad', 'religi', 'baja médica', 'discapacid')
    for _, preg in PREGUNTAS_COMPETENCIA:
        low = preg.lower()
        for pal in prohibidas:
            exige(pal not in low,
                  'La pregunta «%s» toca «%s»: art. 9.5 de la Ley 15/2022' % (preg[:50], pal))

    # ---- 7. cumplimiento legal -------------------------------------------
    familias_si = sorted(set(c[1] for c in CUMPLIMIENTO if c[4] == 'Sí'))
    exige(familias_si == sorted(PUNTOS_PERIODICIDAD_ESTATAL),
          'Las familias con periodicidad fijada por norma estatal no son las cuatro declaradas: %s' % familias_si)
    exige(all(c[4] in ('Sí', 'No') for c in CUMPLIMIENTO), 'La columna de norma estatal admite sólo Sí/No')
    exige(all(c[3] >= 0 for c in CUMPLIMIENTO), 'Periodicidad negativa')
    for c in CUMPLIMIENTO:
        _fecha(c[2])          # revienta si la fecha está mal escrita
    exige(len(ESTADO_NORMATIVO) == 7, 'El estado normativo no tiene 7 filas')
    exige(all(e[3] == RESTAURANTE['fecha_corte_normativa'] for e in ESTADO_NORMATIVO),
          'Alguna fila del estado normativo no lleva la fecha de corte del producto')
    exige(len(DOCUMENTACION_OBLIGATORIA) == 12, 'La documentación obligatoria no tiene 12 filas')
    exige(len(TOPES_JORNADA) >= 10 and len(PERMISOS) >= 10 and len(REGIMEN_DISCIPLINARIO) >= 10,
          'Alguna de las tres tablas de referencia legal se ha quedado corta')
    for tabla, nombre in ((TOPES_JORNADA, 'TOPES_JORNADA'), (PERMISOS, 'PERMISOS'),
                          (REGIMEN_DISCIPLINARIO, 'REGIMEN_DISCIPLINARIO')):
        exige(all(len(f) == 4 for f in tabla), '%s tiene filas con un número de columnas raro' % nombre)
        exige(all(f[3] for f in tabla), '%s tiene una fila sin norma citada' % nombre)

    # ---- 8. reuniones, acuerdos y plan de 90 días -------------------------
    exige(len(REUNIONES) == 12, 'No hay 12 reuniones en el trimestre')
    exige(not any('briefing' in r[1].lower() for r in REUNIONES),
          'El libro de reuniones no lleva briefing (decisión D3)')
    exige(all(_fecha(r[0]).isoweekday() == 1 for r in REUNIONES),
          'Alguna reunión no cae en lunes, que es el día de cierre')
    exige(sum(m for _, _, m, _ in GUION_REUNION_SEMANAL) == 30,
          'El guion de la reunión semanal no suma 30 minutos')
    exige(len(GUION_REUNION_SEMANAL) == 7, 'El guion semanal no tiene 7 puntos')
    exige(len(UNO_A_UNO) == 6, 'El uno-a-uno no tiene 6 preguntas')
    exige(len(ACUERDOS) == 25, 'No hay 25 acuerdos')
    exige(all(a[3] in ids for a in ACUERDOS), 'Hay un acuerdo con un responsable que no está en la plantilla')
    corte = _fecha(RESTAURANTE['fecha_corte_normativa'])
    vencidos = [a for a in ACUERDOS if a[5] != 'Cerrado' and _fecha(a[4]) < corte]
    exige(len(vencidos) >= 3, 'Deberían quedar acuerdos vencidos a la fecha de corte y hay %d' % len(vencidos))
    exige(len(PLAN_90) == 20, 'El plan de 90 días no tiene 20 decisiones')
    exige(all(d[0] in AREAS_PLAN_90 for d in PLAN_90), 'Área del plan fuera de las cinco')
    exige(all(d[1] in HERRAMIENTAS_PACK for d in PLAN_90), 'Herramienta de origen fuera de los 7 libros')
    exige(all(1 <= d[4] <= 13 for d in PLAN_90), 'Semana del plan fuera de 1-13')
    exige(all(d[3] in ids for d in PLAN_90), 'Responsable del plan fuera de la plantilla')
    exige(len(set(d[1] for d in PLAN_90)) >= 6, 'El plan sólo bebe de unas pocas herramientas')

    # ---- 9. auditoría interna --------------------------------------------
    exige(len(AUDITORIA) == 60, 'La auditoría no tiene 60 puntos')
    exige([a[0] for a in AUDITORIA] == list(range(1, 61)), 'Los puntos de auditoría no van de 1 a 60')
    exige(all(a[1] in AREAS_AUDITORIA for a in AUDITORIA), 'Área de auditoría desconocida')
    for area in AREAS_AUDITORIA:
        exige(sum(1 for a in AUDITORIA if a[1] == area) == 10,
              'El área «%s» no tiene 10 puntos' % area)
    exige(all(1 <= a[3] <= 3 for a in AUDITORIA), 'Peso de auditoría fuera de 1-3')
    exige(len(AUDITORIAS_HECHAS) == 3, 'No hay 3 visitas de auditoría')
    exige(all(len(v[3]) == 60 for v in AUDITORIAS_HECHAS), 'Alguna visita no tiene 60 puntuaciones')
    exige(all(all(0 <= x <= 5 for x in v[3]) for v in AUDITORIAS_HECHAS), 'Puntuación de auditoría fuera de 0-5')
    pesos = [a[3] for a in AUDITORIA]
    pond = []
    for v in AUDITORIAS_HECHAS:
        pond.append(sum(p * s for p, s in zip(pesos, v[3])) / float(sum(pesos)))
    exige(pond[0] < pond[1] < pond[2], 'La auditoría no mejora entre la visita 1 y la 3')
    por_area = {}
    for area in AREAS_AUDITORIA:
        idx = [i for i, a in enumerate(AUDITORIA) if a[1] == area]
        por_area[area] = [sum(v[3][i] for i in idx) / float(len(idx)) for v in AUDITORIAS_HECHAS]
    empeoran = [a for a, m in por_area.items() if m[2] < m[0]]
    exige(len(empeoran) == 1,
          'Debería empeorar exactamente un área entre la visita 1 y la 3, y empeoran %d' % len(empeoran))

    # ---- resumen ---------------------------------------------------------
    print('=' * 78)
    print('MANUAL DEL MANAGER DE RESTAURANTE — juego de datos de «La Encina»')
    print('=' * 78)
    print('Provincia (convenio): %s (%s)' % (RESTAURANTE['provincia'], RESTAURANTE['comunidad']))
    print('')
    print('PLANTILLA')
    print('  12 personas · salarios brutos %s €/año' % ('{:,.0f}'.format(bruto_anual).replace(',', '.')))
    print('  coste de personal con SS al %.0f %%: %.0f €/mes' % (100 * SS_EMPRESA, coste_mes_plantilla))
    print('  Guía Food Cost (salarios × SS): %.0f €/mes  →  desviación %+.2f %% (tope ±5 %%)'
          % (guia_coste_mes, desv_plantilla))
    print('  Guía Food Cost con «otros costes de personal»: %.0f €/mes'
          % ((guia_salarios_anual * (1 + SS_EMPRESA) + guia_otros_anual) / 12.0))
    print('')
    print('AÑO SEMANAL (52 semanas ISO de 2026)')
    print('  ventas netas %s €  ·  food cost %.2f %%  ·  labor cost %.2f %%  ·  prime cost %.2f %%'
          % ('{:,.0f}'.format(ventas_anio).replace(',', '.'),
             100.0 * consumo_anio / ventas_anio,
             100.0 * personal_anio / ventas_anio,
             100.0 * (consumo_anio + personal_anio) / ventas_anio))
    print('  cubiertos %s  ·  tickets %s  ·  ticket medio %.2f €  ·  gasto por cubierto %.2f €'
          % ('{:,.0f}'.format(cubiertos_anio).replace(',', '.'),
             '{:,.0f}'.format(tickets_anio).replace(',', '.'),
             ticket_medio_anio, gasto_cubierto_anio))
    print('  cuadre mensual contra la Guía Food Cost: peor desviación %.2f %% (tope 3 %%)' % peor)
    print('  semanas fuera del objetivo de prime cost (%.0f %%): %d de 52'
          % (100 * objetivo, len(malas)))
    for s in malas:
        dom = s['lunes'] + dt.timedelta(days=6)
        etiqueta = '  ← la semana del bonus' if s['semana'] == SEMANA_BONUS_PRIME_71 else ''
        print('    semana %2d (%s → %s): prime cost %.1f %%  [food %.1f %% + personal %.1f %%]%s'
              % (s['semana'], s['lunes'].strftime('%d-%m'), dom.strftime('%d-%m'),
                 100 * s['prime_cost'], 100 * s['food_cost'], 100 * s['labor_cost'], etiqueta))
    print('')
    print('POLIVALENCIA')
    for est, c in cobertura:
        marca = '  ← PUNTO ÚNICO DE FALLO' if c == 1 else ('  ← la mejor cubierta' if c == max(x for _, x in cobertura) else '')
        print('  %-22s %d persona(s) a nivel ≥ 2%s' % (est, c, marca))
    print('')
    print('SERVICIO Y PERSONAS')
    print('  quejas: 30 en 3 meses · motivo más repetido «%s» (%d de 30, el siguiente %d)'
          % (motivo_top, n_top, orden[1][1]))
    print('  reclamaciones formales: 3, una fuera del plazo de Cataluña (%s, %d días)'
          % (fuera[0][0], fuera[0][1]))
    print('  reseñas: 40 en 6 meses · medias por mes: %s'
          % ' · '.join('%s %.2f' % (MESES[m - 1][:3], v) for m, v in medias))
    print('  selección: %s' % ' · '.join('%s %.2f' % (n, v) for n, v in medias_cand)
          + '  (umbral %.2f)' % umbral)
    print('')
    print('CUMPLIMIENTO Y GESTIÓN')
    print('  calendario legal: %d puntos, %d con periodicidad fijada por norma estatal (%s)'
          % (len(CUMPLIMIENTO), len(familias_si), ', '.join(familias_si)))
    print('  acuerdos vencidos a %s: %d de 25' % (corte.isoformat(), len(vencidos)))
    print('  auditoría interna: media ponderada %.2f → %.2f → %.2f · empeora «%s» (%.1f → %.1f)'
          % (pond[0], pond[1], pond[2], empeoran[0], por_area[empeoran[0]][0], por_area[empeoran[0]][2]))
    print('')
    if avisos:
        for a in avisos:
            print('AVISO: %s' % a)
    if fallos:
        print('%d FALLO(S):' % len(fallos))
        for f in fallos:
            print('  ✗ %s' % f)
        raise SystemExit(1)
    print('TODAS LAS COMPROBACIONES EN VERDE.')
    return True


if __name__ == '__main__':
    checks()
