#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
datos_ejemplo.py - JUEGO DE DATOS ÚNICO del producto «Cómo Montar una Pastelería»
(SPEC: scripts/productos-digitales/guia-pasteleria-SPEC.md, §3).

Los 8 libros de Excel, el guion (`guion_guia_pasteleria_obrador.py`), el bonus 1
(business plan modelo relleno) y el bonus 2 («12 decisiones de apertura
resueltas») beben de ESTE fichero. Regla de la familia: una sola fuente de
cifras. Si un número cambia, cambia aquí y se regeneran los libros.

QUÉ ES «LA CLARA» Y QUÉ NO ES
=============================
«La Clara» es un CASO MODELADO, no un cliente real y no «la pastelería media de
España». Es el juego de datos que permite que las fórmulas de los 8 libros
tengan qué calcular y que el lector vea una hoja rellena antes de borrarla y
poner la suya. Nada de lo que hay aquí es un benchmark.

Por eso todo dato lleva su procedencia en un campo `fuente`, y sólo hay tres
clases de procedencia (lo comprueba `comprobar()`):

  1. **`PS-*` / `PA-*`** - id del research de sector / de normativa, con fuente,
     URL y fiabilidad en `auditorias/guia-pasteleria-ids-PS.json` y en
     `auditorias/guia-pasteleria-research-L3-normativa.md`. Son datos de
     terceros, publicados y citables.
  2. **`kit-escandallos/…` / `kit-tareas-pasteleria/…`** - COPIA DECLARADA de
     una celda de un producto del catálogo. Copia, nunca vínculo entre libros
     (SPEC §3): un cliente que tenga los dos productos no puede ver dos costes
     distintos del mismo croissant.
  3. **`supuesto`** - dato de ejemplo inventado para que el modelo funcione. No
     tiene fuente porque no la hay, y así se dice. Un supuesto NUNCA se escribe
     en la prosa como si fuera un dato del sector.

LOS 30 ESCANDALLOS SON DATOS DE EJEMPLO
=======================================
Tres de las treinta referencias -Tarta de chocolate 70 %, Croissants y
Macarons- son COPIA EXACTA de `kit-escandallos/05-pasteleria.xlsx`: mismos
ingredientes, mismas cantidades, mismos precios de compra, mismo rendimiento
por tanda. `comprobar()` abre el xlsx y los compara línea a línea.

Las otras veintisiete son escandallos de EJEMPLO. Los gramajes, los minutos de
mano de obra y los PVP son supuestos; los precios de compra reutilizan los
diecinueve del kit siempre que el ingrediente aparece allí, y son supuestos en
el resto. No son recetas con pretensión de exactitud y este producto no es un
recetario: son los datos que hacen que el escandallo por tanda del libro 4
tenga qué calcular. El bonus 3 «recetario de escandallos base» se DESCARTÓ por
esto mismo (SPEC §2.4).

DECISIONES DE LA SPEC QUE ESTE FICHERO MATERIALIZA
==================================================
  · **D22** - 90 m² (obrador 45 · despacho 22 · cámara y almacén 12 · aseos y
    vestuario 11) y 5 personas / 3,5 jornadas con los nombres LITERALES de los
    4 perfiles de `kit-tareas-pasteleria/04-tareas-perfiles.xlsx`, con DOS
    personas en Dependiente Vitrina. «Oficial» no existe en el kit y está
    prohibido como nombre de perfil.
  · **D23** - UNA sola regla de margen. Aquí se guarda un único parámetro,
    `food_cost_objetivo`; `margen_bruto_objetivo()` lo deriva. El libro 4 pide
    uno de los dos y calcula el otro, nunca los dos.
  · **D11** - el libro 4 devuelve DOS salidas separadas y ninguna es «vida
    útil»: `plazo_legal()` (24 h o «no aplica») y `temperatura_legal()` (el
    MÍNIMO entre el art. 4.1 fila 9 y el art. 9.3, diciendo cuál manda). La
    vida útil la declara el lector en celda verde: aquí vale `None` a propósito.
  · **D21** - ninguna celda verde se queda vacía por depender de otro producto.
    Toda partida de `EQUIPAMIENTO` sin precio verificado trae
    `supuesto_por_defecto`, y se distingue de `valor_verificado`.
  · **D17** - toda línea de precio de equipamiento lleva su base fiscal
    (`base_iva`: 'sin IVA' / 'con IVA' / 'no declarada') y su tipo. Sin esa
    columna el CAPEX sale un 21 % desviado.
  · **D7 / D8 / D10 / D15** - lo normativo NO se redacta aquí: se referencia
    por id `PA-*` y la nota la sirve `nota_legal()` desde la verificación legal
    del 10-sep. `gate_legal()` aborta si falta alguno de los ids que citan los
    libros 4 y 6.

LO QUE NO ENTRA (lista negra del §5 de la SPEC)
===============================================
Ni «11.729 pastelerías», ni «facturación media de 1,08 M€», ni el rango
inventado «84.000-180.000 €/año», ni ticket medio «de pastelería» (N-11: no
existe dato público; el de aquí se CALCULA desde la carta y se declara
supuesto), ni PS-60 como benchmark (D23: sus tres pares implican márgenes del
71-80 %), ni «110 m²» (D22), ni cifras de inflación. `comprobar()` barre el
módulo entero buscando esas cifras.

VOCABULARIO (SPEC §6)
=====================
pastelería (nunca «dulcería», que en México es la tienda de golosinas) ·
obrador · escandallo · vitrina · tarta · encargo · artesanal (nunca
«artesana») · coste.

WinAnsi: todo el texto de este fichero cabe en cp1252, y lo comprueba
`comprobar()`. Nada de flechas, signos de «menor o igual», «aproximadamente»,
espacios finos ni guiones no separables: los caracteres decorativos de los
`.md` no entran en el código.

Ejecutar `python3 datos_ejemplo.py` corre `comprobar()` e imprime el resumen.
Python del Mac: `/usr/local/bin/python3` (el del sistema no trae openpyxl).
"""

import json
import os
import re

_AQUI = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.normpath(os.path.join(_AQUI, '..', '..', '..'))
_DL = os.path.join(_REPO, 'astro-site', 'public', 'dl')
_AUDIT = os.path.normpath(os.path.join(_AQUI, '..', 'auditorias'))

#: Fecha de corte de todo el bloque normativo (SPEC D16 y D28).
FECHA_VERIFICACION_LEGAL = '10-09-2026'

#: Ficheros del catálogo de los que se COPIA (nunca se vinculan).
KIT_ESCANDALLOS = os.path.join(_DL, 'kit-escandallos', '05-pasteleria.xlsx')
KIT_PLAN = os.path.join(_DL, 'kit-tareas-pasteleria', '10-plan-produccion-semanal.xlsx')
KIT_ALERGENOS = os.path.join(_DL, 'kit-tareas-pasteleria', '12-control-alergenos-vitrina.xlsx')
KIT_PERFILES = os.path.join(_DL, 'kit-tareas-pasteleria', '04-tareas-perfiles.xlsx')

#: Etiquetas de procedencia de los tres escandallos copiados del kit (SPEC §3).
F_KIT_TC = 'kit-escandallos/05-pasteleria.xlsx!Tarta Chocolate'
F_KIT_CR = 'kit-escandallos/05-pasteleria.xlsx!Croissants'
F_KIT_MA = 'kit-escandallos/05-pasteleria.xlsx!Macarons'

#: Nombres LITERALES de los 4 perfiles del kit (verificado abriendo el fichero
#: el 10-09-2026: las cuatro pestañas de `04-tareas-perfiles.xlsx` se llaman
#: exactamente así). D22 prohíbe «Oficial», que no existe en el kit.  LN-OK
PERFILES_KIT = ('Jefe Pastelero', 'Pastelero', 'Ayudante', 'Dependiente Vitrina')


# ==========================================================================
# 1. EL NEGOCIO: «La Clara», 90 m² por zonas
# ==========================================================================
#: Las 7 zonas obligatorias de PS-86d, agrupadas en los 4 bloques de D22 y
#: sumando los 90 m² del caso publicado de La Hostelera (PS-85a/b/c usan ese
#: mismo local de referencia: por eso los 600/900/1.200 €/m² de obra casan sin
#: retoques). El reparto de m² DENTRO de cada bloque es supuesto.
ZONAS = [
    # (zona, bloque de D22, m², fuente del m², nota)
    ('Obrador', 'Obrador', 45.0, 'PS-86d + D22',
     'Zona de elaboración, inaccesible al público (art. 2.2.h del RD 1021/2022, PA-03b). '
     'Principio de marcha adelante: la materia prima entra por un extremo y el producto '
     'terminado sale por el otro sin cruzarse con ella.'),
    ('Zona de venta (despacho)', 'Despacho', 22.0, 'PS-86d + D22',
     'Mostrador, vitrina refrigerada, vitrina de ambiente y espacio de cola.'),
    ('Almacén de materia prima', 'Cámara y almacén', 5.0, 'PS-86d + supuesto',
     'Harinas, azúcares y secos sobre estantería, nunca en el suelo.'),
    ('Cámara frigorífica', 'Cámara y almacén', 4.0, 'PS-86d + supuesto',
     'Conservación a 4 °C o menos de lo relleno (art. 4.1 fila 9, PA-12).'),
    ('Almacén de producto terminado', 'Cámara y almacén', 3.0, 'PS-86d + supuesto',
     'Producto estable a temperatura ambiente y packaging montado.'),
    ('Vestuarios y aseos de personal', 'Aseos y vestuario', 8.0, 'PS-86d + supuesto',
     'Aseo de personal separado del de clientes, con taquillas.'),
    ('Almacén de residuos', 'Aseos y vestuario', 3.0, 'PS-86d + supuesto',
     'Cerrado, con contenedores identificados; no puede abrir al obrador.'),
]

#: Los 4 bloques de D22 con sus m², tal y como los publica la SPEC.
BLOQUES_M2 = {'Obrador': 45.0, 'Despacho': 22.0,
              'Cámara y almacén': 12.0, 'Aseos y vestuario': 11.0}

NEGOCIO = {
    'nombre': 'Pastelería «La Clara»',
    'nombre_corto': 'La Clara',
    'formato': ('Obrador propio más despacho a calle, en una ciudad media española '
                'SIN nombre propio: el lector la sustituye por la suya'),
    'fuente_formato': 'PS-05',
    'm2_total': 90.0,
    'fuente_m2': 'D22 + PS-85a + PS-85b + PS-85c',
    'zonas': ZONAS,
    'bloques_m2': BLOQUES_M2,

    # Potencia. PS-86a fija 20-80 kW SOLO para los hornos; el resto de la
    # instalación (frío, amasado, climatización, iluminación) es supuesto.
    'potencia_hornos_kw': 34.0,
    'fuente_potencia_hornos': 'PS-86a',
    'potencia_instalada_kw': 62.0,
    'fuente_potencia_instalada': 'supuesto',
    'nota_potencia': ('PS-86a da 20-80 kW SOLO para los hornos. Los 62 kW de potencia '
                      'instalada suman además frío, amasado, climatización e iluminación, '
                      'y son un supuesto: la potencia a contratar la fija el proyecto '
                      'eléctrico, no una tabla.'),

    # Jornada y calendario comercial.
    'horas_turno': 8.0,
    'fuente_horas_turno': 'supuesto',
    'dias_apertura_semana': 6,
    'dias_apertura_anio': 300,
    'fuente_dias_apertura': 'supuesto',
    'nota_dias_apertura': ('6 días por semana × 52 semanas = 312, menos 12 días de cierre '
                           'por vacaciones en agosto = 300. Los festivos NO se descuentan: '
                           'la pastelería tiene libertad horaria por ley estatal cuando es '
                           'la actividad principal (PA-39).'),

    # Apertura recomendada: fuera de pico y con margen para llegar rodado a
    # Reyes (cap. 20 y decisión 9 del bonus 2).
    'mes_apertura_recomendado': 9,
    'nombre_mes_apertura': 'septiembre',
    'fuente_mes_apertura': 'supuesto',
    'nota_mes_apertura': ('Septiembre no es ninguno de los 6 picos y deja 3,5 meses de '
                          'rodaje antes de Reyes, que es la campaña que decide el año.'),

    # Local en alquiler: el escenario base es obra nueva sobre local alquilado.
    'renta_mensual': 1200.0,
    'fuente_renta': 'supuesto',
    'nota_renta': ('Supuesto para una ciudad media. Los cinco traspasos de Barcelona de '
                   'PS-69 se mueven entre 850 y 1.300 €/mes para 63-85 m²; aquí se toma '
                   'la parte baja porque Barcelona no es una ciudad media.'),
    'meses_fianza': 2,
    'fuente_fianza': 'supuesto',
}

MESES = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')


# ==========================================================================
# 2. CONVENIO Y PLANTILLA
# ==========================================================================
#: Los 6 grupos del Convenio de Comercio e Industria de Confitería, Pastelería,
#: Bollería, Repostería, Heladería y Platos Cocinados de la Comunidad de Madrid
#: (código 28001025011981), revisión 2026 publicada en el BOCM núm. 50 de
#: 28-feb-2026. Verificado literal el 10-09-2026 (PA-33). Son **15 pagas**, no
#: 14, y eso cambia el coste mes a mes. Van en celda verde: el lector los
#: sustituye por los de su convenio provincial.
CONVENIO = [
    # (n, grupo profesional, €/mes, €/año, áreas funcionales, puestos que cita)
    (1, 'Técnicos y titulados superiores', 1733.88, 26008.20,
     ('ADMINISTRACIÓN',), ''),
    (2, 'Dirección, jefes y encargados', 1427.89, 21418.35,
     ('OBRADOR', 'COMERCIO', 'ADMINISTRACIÓN'), 'maestro de obrador'),
    (3, 'Personal especialista', 1376.91, 20653.65,
     ('OBRADOR', 'COMERCIO'),
     'oficial 1.ª de producción, encargado de sección, dependiente mayor'),
    (4, 'Personal cualificado', 1249.42, 18741.30,
     ('OBRADOR', 'COMERCIO'),
     'oficial 2.ª de producción, oficial 1.ª de envasado, dependiente, conductor'),
    (5, 'Personal de apoyo', 1192.42, 17886.30,
     ('OBRADOR', 'COMERCIO'),
     'ayudante de producción, oficial de acabado, ayudante de comercio'),
    (6, 'Personal de ayuda en servicios auxiliares', 1192.42, 17886.30,
     ('OBRADOR', 'COMERCIO'), 'peón, limpiador, almacenero'),
]
FUENTE_CONVENIO = 'PA-33'
CONVENIO_CODIGO = '28001025011981'
CONVENIO_PUBLICACION = 'BOCM núm. 50, de 28 de febrero de 2026'
CONVENIO_VIGENCIA = '1-ene-2026 a 31-dic-2026'
CONVENIO_PAGAS = 15

#: 5 personas / 3,5 jornadas (D22). Los cuatro nombres de perfil son LITERALES
#: de las pestañas del kit; el quinto renglón es la SEGUNDA persona del perfil
#: «Dependiente Vitrina», que es como se cubren los 4 perfiles con 5 personas.
PLANTILLA = [
    # (id, perfil, jornada, grupo de convenio, área, horas/semana, turno)
    ('P1', 'Jefe Pastelero',        1.0, 2, 'OBRADOR',  40, 'Madrugada (04:30-12:30)'),
    ('P2', 'Pastelero',             1.0, 3, 'OBRADOR',  40, 'Madrugada (05:00-13:00)'),
    ('P3', 'Ayudante',              0.5, 5, 'OBRADOR',  20, 'Mañana (07:00-11:00)'),
    ('P4', 'Dependiente Vitrina A', 0.5, 4, 'COMERCIO', 20, 'Mañana (08:00-12:00)'),
    ('P5', 'Dependiente Vitrina B', 0.5, 4, 'COMERCIO', 20, 'Tarde (16:30-20:30)'),
]
FUENTE_PLANTILLA = 'D22 + kit-tareas-pasteleria/04-tareas-perfiles.xlsx'


# ==========================================================================
# 3. PARÁMETROS
# ==========================================================================
#: `ss_empresa` y `smi_anual` son los MISMOS parámetros de la familia
#: (`guias-v2_0/motor.py`: `PARAMETROS['ss_empresa']` = 0,33 y
#: `PARAMETROS['smi_anual']` = 17.094 €). No se duplica el valor con otro
#: número: se copia el de la familia y se dice de dónde sale.
PARAMS = {
    # --- laboral ---------------------------------------------------------
    'pagas_convenio': (15, 'PA-33',
                       'El convenio de Madrid paga 15, no 14: cambia el coste mes a mes.'),
    'ss_empresa': (0.33, 'motor.PARAMETROS[ss_empresa]',
                   'Cotización empresarial aproximada sobre el bruto (contingencias '
                   'comunes, desempleo, FOGASA y formación). Es el mismo parámetro que '
                   'usa el resto de la familia. Ajústala a tu convenio y a tus contratos.'),
    'smi_mensual': (1221.0, 'PA-32', 'RD 126/2026, 14 pagas, vigente del 1-ene al 31-dic-2026.'),
    'smi_pagas': (14, 'PA-32', ''),
    'smi_anual': (17094.0, 'PA-32 + motor.PARAMETROS[smi_anual]',
                  'Referencia ANUAL en cómputo global (art. 3 del RD 126/2026), no un '
                  'mínimo por concepto. En pastelería manda el convenio: el grupo más '
                  'bajo de Madrid (17.886,30 €/año) ya lo supera.'),
    'horas_semana_jornada_completa': (40, 'supuesto',
                                      'La jornada anual del convenio de Madrid NO se ha '
                                      'verificado: 40 h/semana es el supuesto de trabajo.'),
    'horas_anuales_contrato': (1780, 'supuesto',
                               '40 h × 52 semanas = 2.080, menos 30 días naturales de '
                               'vacaciones y los festivos del calendario laboral.'),
    'ratio_horas_productivas': (0.85, 'supuesto',
                                'Parte de la jornada que se pasa a pie de mesa. El 15 % '
                                'restante es recepción, limpieza, formación y reuniones.'),

    # --- IVA (PA-36, PA-36b, PA-36c, PA-36d; verificado el 10-09-2026) ----
    'iva_producto': (0.10, 'PA-36',
                     'Bollería, pastelería, confitería, repostería y chocolate van al '
                     '10 % por la regla general de alimentos del art. 91.Uno.1.1.º de '
                     'la Ley 37/1992: NO porque un precepto los nombre, sino porque no '
                     'están en la lista cerrada del 4 % ni excluidos del 10 %.'),
    'iva_pan': (0.04, 'PA-36b',
                'TODOS los productos del RD 308/2019 (pan común, pan especial y '
                'semielaborados, con o sin gluten) van al 4 % desde la Resolución '
                'vinculante de la DGT de 24-02-2025, que acoge la STS 1610/2024 con '
                'efectos ex tunc. El cruasán sigue al 10 %: el RD 308/2019 sólo regula '
                'el pan y no menciona la bollería.'),
    'iva_degustacion': (0.10, 'PA-36c',
                        'En zona de degustación todo va al 10 % (art. 91.Uno.2.2.º): ahí '
                        'no vendes un bien, prestas un servicio de hostelería.'),
    'iva_equipamiento': (0.21, 'PA-36 + art. 90.Uno de la Ley 37/1992',
                         'Tipo general. Sin la columna «lleva IVA» el CAPEX sale un '
                         '21 % desviado (D17).'),
    'iva_obra': (0.21, 'PA-36 + art. 90.Uno de la Ley 37/1992', 'Tipo general.'),
    'iva_general': (0.21, 'art. 90.Uno de la Ley 37/1992', 'Tipo general.'),

    # --- margen: UNA SOLA REGLA (D23) ------------------------------------
    'food_cost_objetivo': (0.32, 'PS-55 + PS-56',
                           'REGLA ÚNICA. PS-55 (margen bruto 65-70 %) y PS-56 (food cost '
                           '30-35 %) son la misma regla dicha dos veces: 0,32 es el punto '
                           'medio de la banda. `margen_bruto_objetivo()` la deriva. El '
                           'libro 4 pide UNO de los dos y calcula el otro, nunca los dos.'),
    'merma_objetivo': (0.05,
                       'kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Resumen por Partida',
                       'Objetivo de merma precargado en el kit. Criterio del propio kit: '
                       'la merma de una pastelería artesanal suele moverse entre el 3 % y '
                       'el 8 %; por encima del 10 % hay que revisar el plan de producción.'),
    'packaging_pct_coste': (0.10, 'PS-59',
                            'Packaging entre el 5 % y el 15 % del coste total del '
                            'producto. Aquí, el punto medio de esa horquilla.'),

    # --- comercial (todo supuesto; N-11 prohíbe el ticket medio «de pastelería») ---
    'tickets_dia_crucero': (183, 'supuesto',
                            'Clientes por día en velocidad de crucero. NO es un dato del '
                            'sector: no existe dato público de tráfico de pastelería.'),
    'piezas_por_ticket': (2.6, 'supuesto',
                          'De aquí sale el ticket medio, que NO se teclea: se calcula '
                          'como PVP medio ponderado de la carta × piezas por ticket. '
                          'N-11 prohíbe publicar un «ticket medio de pastelería».'),
    'meses_colchon_fondo_maniobra': (4, 'supuesto',
                                     'Meses de gastos fijos que hay que tener en caja el '
                                     'día que abres. Es una partida del CAPEX, no una propina.'),
}


def P(clave):
    """Valor de un parámetro. `PARAMS[clave]` es (valor, fuente, nota)."""
    return PARAMS[clave][0]


def margen_bruto_objetivo():
    """D23: UNA sola regla. El margen bruto se DERIVA del food cost objetivo;
    nunca se guardan los dos números por separado."""
    return 1.0 - P('food_cost_objetivo')


# ==========================================================================
# 4. PRECIOS DE COMPRA
# ==========================================================================
#: Precio por unidad de compra, sin IVA. Los diecinueve primeros son COPIA
#: EXACTA de `kit-escandallos/05-pasteleria.xlsx` (columna «Precio/Ud (€)» de
#: las hojas Tarta Chocolate, Croissants y Macarons): son los que hacen que el
#: mismo croissant cueste lo mismo en los dos productos. El resto son
#: supuestos plausibles de compra profesional en España, 2026.
#:
#: OJO con la mantequilla (SPEC §5, «errores de método»): los 386 €/100 kg de
#: PS-66 son la COTIZACIÓN DE COMMODITY a granel del Milk Market Observatory,
#: no el precio de la mantequilla de laminado 82-84 % que compra un obrador.
#: No se mezclan. PS-66 sirve para MODELAR la volatilidad (cap. 11), nunca para
#: fijar un precio de compra.
PRECIOS_COMPRA = {
    # --- copiados del kit (precio exacto) ---------------------------------
    'Chocolate negro 70%':                    (18.00, 'kg', F_KIT_TC),
    'Mantequilla':                            (9.00, 'kg', F_KIT_TC),
    'Huevos (unidades)':                      (3.60, 'docena', F_KIT_TC),
    'Azúcar':                                 (1.20, 'kg', F_KIT_TC),
    'Harina floja':                           (0.90, 'kg', F_KIT_TC),
    'Nata 35% MG':                            (3.80, 'L', F_KIT_TC),
    'Cacao en polvo':                         (12.00, 'kg', F_KIT_TC),
    'Sal':                                    (0.60, 'kg', F_KIT_TC),
    'Harina de fuerza':                       (1.10, 'kg', F_KIT_CR),
    'Mantequilla seca (82% MG)':              (12.00, 'kg', F_KIT_CR),
    'Leche entera':                           (1.10, 'L', F_KIT_CR),
    'Levadura fresca':                        (5.00, 'kg', F_KIT_CR),
    'Huevo (para pintar)':                    (3.60, 'docena', F_KIT_CR),
    'Harina de almendra':                     (14.00, 'kg', F_KIT_MA),
    'Azúcar glas':                            (2.50, 'kg', F_KIT_MA),
    'Claras de huevo':                        (6.00, 'kg', F_KIT_MA),
    'Frambuesa congelada':                    (9.00, 'kg', F_KIT_MA),
    'Chocolate blanco':                       (15.00, 'kg', F_KIT_MA),
    'Colorante rojo (bote 50 g · 2 g/tanda)': (4.00, 'ud', F_KIT_MA),
    # --- supuestos --------------------------------------------------------
    'Harina panificable':                     (1.05, 'kg', 'supuesto'),
    'Harina integral de centeno':             (1.75, 'kg', 'supuesto'),
    'Almidón de maíz':                        (2.10, 'kg', 'supuesto'),
    'Levadura química (impulsor)':            (8.50, 'kg', 'supuesto'),
    'Manteca de cerdo':                       (4.40, 'kg', 'supuesto'),
    'Aceite de girasol':                      (1.80, 'L', 'supuesto'),
    'Aceite de oliva virgen extra':           (7.20, 'L', 'supuesto'),
    'Queso crema':                            (8.90, 'kg', 'supuesto'),
    'Cobertura de leche 40%':                 (15.50, 'kg', 'supuesto'),
    'Manzana':                                (1.60, 'kg', 'supuesto'),
    'Zanahoria':                              (1.10, 'kg', 'supuesto'),
    'Fresa fresca':                           (6.20, 'kg', 'supuesto'),
    'Kiwi':                                   (2.60, 'kg', 'supuesto'),
    'Frutos rojos congelados':                (10.50, 'kg', 'supuesto'),
    'Limón':                                  (2.20, 'kg', 'supuesto'),
    'Naranja confitada':                      (7.80, 'kg', 'supuesto'),
    'Pasas':                                  (5.20, 'kg', 'supuesto'),
    'Nueces':                                 (15.00, 'kg', 'supuesto'),
    'Almendra molida':                        (13.50, 'kg', 'supuesto'),
    'Almendra marcona cruda':                 (15.50, 'kg', 'supuesto'),
    'Piñón':                                  (72.00, 'kg', 'supuesto'),
    'Miel':                                   (8.20, 'kg', 'supuesto'),
    'Mermelada de albaricoque':               (4.20, 'kg', 'supuesto'),
    'Gelatina neutra de brillo':              (11.50, 'kg', 'supuesto'),
    'Gelatina en hoja':                       (42.00, 'kg', 'supuesto'),
    'Yema pasteurizada (ovoproducto)':        (6.80, 'kg', 'supuesto'),
    'Vainilla en pasta':                      (92.00, 'kg', 'supuesto'),
    'Canela molida':                          (18.00, 'kg', 'supuesto'),
    'Agua de azahar':                         (14.00, 'L', 'supuesto'),
    'Ron':                                    (9.80, 'L', 'supuesto'),
}


# ==========================================================================
# 5. LA CARTA DE APERTURA: 30 referencias en 5 familias
# ==========================================================================
#: Familias del cap. 03 (SPEC §3): bollería 6 · pastelería individual 6 ·
#: tartas y entremets 6 · panes de acompañamiento 4 · temporada 8.
FAMILIAS = ('Bollería', 'Pastelería individual', 'Tartas y entremets',
            'Panes de acompañamiento', 'Temporada')

#: Las cinco vías legales del huevo del art. 9 del RD 1021/2022 (PA-14), tal y
#: como las tiene que elegir el lector en la hoja «Decisión de Huevo y
#: Temperatura» del libro 4.
#:
#: «estable a ambiente» NO es una vía distinta del art. 9: es la vía 1.a) cuando
#: el producto resultante SÍ es estable a temperatura ambiente, y por eso se le
#: cae encima el art. 9.3 (ni 8 °C ni 24 h) y también la excepción de la fila 9
#: del art. 4.1. Se lista aparte porque es la decisión que el pastelero toma de
#: verdad y la que cambia toda la logística de la vitrina.
#:
#: «63/20 + consumo inmediato» está en la lista y NINGUNA de las 30 referencias
#: la usa: es la vía de los huevos fritos y las tortillas del art. 9.1.b), no la
#: de la pastelería. Decirlo es parte del valor de la hoja.
VIAS_HUEVO = (
    '70/2',
    '63/20',
    'ovoproducto',
    'sin huevo',
    'estable a ambiente',
)
VIAS_HUEVO_TEXTO = {
    '70/2': ('Tratamiento térmico de 70 °C durante 2 s en el centro del producto, o '
             'cualquier combinación equivalente (art. 9.1.a).'),
    '63/20': ('63 °C durante 20 s en el centro Y servido para consumo inmediato '
              '(art. 9.1.b): huevos fritos, tortillas. No es una vía de pastelería.'),
    'ovoproducto': ('El producto se consume sin un tratamiento térmico que cumpla el '
                    'apartado 1, así que el huevo crudo se sustituye por ovoproducto de '
                    'establecimiento autorizado (art. 9.2).'),
    'sin huevo': 'La elaboración no lleva huevo en ninguna forma: el art. 9 no le aplica.',
    'estable a ambiente': ('Vía 1.a) y el producto terminado ES estable a temperatura '
                           'ambiente: el art. 9.3 no le fija ni temperatura ni plazo, y la '
                           'fila 9 del art. 4.1 lo exceptúa aunque vaya relleno.'),
}

#: Cada referencia es un dict. Claves:
#:   id · nombre · familia · tanda (uds por elaboración) · unidad_venta ·
#:   gramaje_g · lineas (escandallo) · minutos_mo_tanda · pvp_con_iva · iva ·
#:   mix_pct · via_huevo · relleno · estable_ambiente · pico · fuentes · nota
#:
#: `lineas` = (ingrediente, cantidad, unidad de uso, factor, merma en tanto por
#: uno), con el MISMO convenio del kit: cantidad bruta = cantidad / (1 - merma)
#: y coste = cantidad bruta / factor × precio de compra. El «factor» convierte
#: la unidad de compra en la de uso (12 para docena a unidad, 1,0 si coinciden).
#:
#: `relleno` alimenta la fila 9 del art. 4.1 (PA-12) y `estable_ambiente` es la
#: excepción de esa misma fila y la condición del art. 9.3 (PA-14, PA-15).
#: `vida_util` NO existe a propósito (D11): la declara el lector en celda verde.
CARTA = [
    # ---------------------------- BOLLERÍA (6) ---------------------------
    {'id': 'B1', 'nombre': 'Croissant de mantequilla', 'familia': 'Bollería',
     'tanda': 20, 'unidad_venta': 'pieza', 'gramaje_g': 50,
     'lineas': [
         ('Harina de fuerza', 0.5, 'kg', 1.0, 0.08),
         ('Mantequilla seca (82% MG)', 0.28, 'kg', 1.0, 0.03),
         ('Leche entera', 0.15, 'L', 1.0, 0.03),
         ('Azúcar', 0.06, 'kg', 1.0, 0.02),
         ('Levadura fresca', 0.02, 'kg', 1.0, 0.05),
         ('Sal', 0.01, 'kg', 1.0, 0.02),
         ('Huevo (para pintar)', 1, 'ud', 12.0, 0),
     ],
     'minutos_mo_tanda': 55, 'pvp_con_iva': 1.60, 'iva': 0.10, 'mix_pct': 12.0,
     'via_huevo': 'estable a ambiente', 'relleno': False, 'estable_ambiente': True,
     'pico': None,
     'fuente_escandallo': F_KIT_CR, 'fuente_pvp': 'supuesto',
     'fuente_gramaje': 'kit-escandallos/05-pasteleria.xlsx!Croissants (1,02 kg de masa / 20 uds)',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Plan Semanal · '
                          '12-control-alergenos-vitrina.xlsx!Matriz Alérgenos'),
     'nota': ('COPIA EXACTA del kit de escandallos. El kit deriva además un PVP teórico '
              'desde un food cost objetivo del 25 %; aquí el PVP es el de mostrador '
              '(supuesto) y el food cost se calcula al revés, que es lo que enseña el '
              'cap. 12. El huevo sólo pinta la pieza y el horno pasa de sobra de los '
              '70 °C/2 s: producto estable a temperatura ambiente.')},

    {'id': 'B2', 'nombre': 'Pain au chocolat', 'familia': 'Bollería',
     'tanda': 20, 'unidad_venta': 'pieza', 'gramaje_g': 55,
     'lineas': [
         ('Harina de fuerza', 0.5, 'kg', 1.0, 0.08),
         ('Mantequilla seca (82% MG)', 0.28, 'kg', 1.0, 0.03),
         ('Leche entera', 0.15, 'L', 1.0, 0.03),
         ('Azúcar', 0.06, 'kg', 1.0, 0.02),
         ('Levadura fresca', 0.02, 'kg', 1.0, 0.05),
         ('Sal', 0.01, 'kg', 1.0, 0.02),
         ('Chocolate negro 70%', 0.20, 'kg', 1.0, 0.02),
         ('Huevo (para pintar)', 1, 'ud', 12.0, 0),
     ],
     'minutos_mo_tanda': 55, 'pvp_con_iva': 1.85, 'iva': 0.10, 'mix_pct': 8.0,
     'via_huevo': 'estable a ambiente', 'relleno': False, 'estable_ambiente': True,
     'pico': None,
     'fuente_escandallo': 'supuesto (misma masa que B1, del kit, más dos barras por pieza)',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Plan Semanal · '
                          '12-control-alergenos-vitrina.xlsx!Matriz Alérgenos'),
     'nota': ('El chocolate en barra no convierte la pieza en «producto relleno» del '
              'art. 4.1 fila 9: sigue siendo estable a temperatura ambiente.')},

    {'id': 'B3', 'nombre': 'Napolitana de crema', 'familia': 'Bollería',
     'tanda': 20, 'unidad_venta': 'pieza', 'gramaje_g': 60,
     'lineas': [
         ('Harina de fuerza', 0.5, 'kg', 1.0, 0.08),
         ('Mantequilla seca (82% MG)', 0.28, 'kg', 1.0, 0.03),
         ('Leche entera', 0.15, 'L', 1.0, 0.03),
         ('Azúcar', 0.06, 'kg', 1.0, 0.02),
         ('Levadura fresca', 0.02, 'kg', 1.0, 0.05),
         ('Sal', 0.01, 'kg', 1.0, 0.02),
         ('Leche entera', 0.60, 'L', 1.0, 0.02),
         ('Azúcar', 0.14, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 4, 'ud', 12.0, 0),
         ('Almidón de maíz', 0.05, 'kg', 1.0, 0.02),
         ('Vainilla en pasta', 0.002, 'kg', 1.0, 0),
         ('Huevo (para pintar)', 1, 'ud', 12.0, 0),
     ],
     'minutos_mo_tanda': 65, 'pvp_con_iva': 1.85, 'iva': 0.10, 'mix_pct': 7.0,
     'via_huevo': '70/2', 'relleno': True, 'estable_ambiente': False,
     'pico': None,
     'fuente_escandallo': 'supuesto (masa del kit más crema pastelera de ejemplo)',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Plan Semanal · '
                          '12-control-alergenos-vitrina.xlsx!Matriz Alérgenos'),
     'nota': ('La pieza que más sorprende del mostrador: la crema pastelera la convierte '
              'en producto de pastelería RELLENO y no estable, así que se le caen encima '
              'los 4 °C de la fila 9 del art. 4.1 y las 24 h del art. 9.3, con registro '
              'de fecha y hora de elaboración. No es la vitrina de ambiente: es la '
              'refrigerada.')},

    {'id': 'B4', 'nombre': 'Palmera de hojaldre', 'familia': 'Bollería',
     'tanda': 24, 'unidad_venta': 'pieza', 'gramaje_g': 45,
     'lineas': [
         ('Harina floja', 0.45, 'kg', 1.0, 0.08),
         ('Mantequilla seca (82% MG)', 0.36, 'kg', 1.0, 0.03),
         ('Azúcar', 0.30, 'kg', 1.0, 0.02),
         ('Sal', 0.01, 'kg', 1.0, 0.02),
     ],
     'minutos_mo_tanda': 40, 'pvp_con_iva': 1.70, 'iva': 0.10, 'mix_pct': 4.5,
     'via_huevo': 'sin huevo', 'relleno': False, 'estable_ambiente': True,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Plan Semanal · '
                          '12-control-alergenos-vitrina.xlsx!Matriz Alérgenos'),
     'nota': 'Sin huevo y estable: ni art. 9 ni fila 9. Es la pieza más simple de la vitrina.'},

    {'id': 'B5', 'nombre': 'Caracola de pasas', 'familia': 'Bollería',
     'tanda': 20, 'unidad_venta': 'pieza', 'gramaje_g': 65,
     'lineas': [
         ('Harina de fuerza', 0.45, 'kg', 1.0, 0.08),
         ('Mantequilla seca (82% MG)', 0.22, 'kg', 1.0, 0.03),
         ('Leche entera', 0.14, 'L', 1.0, 0.03),
         ('Azúcar', 0.05, 'kg', 1.0, 0.02),
         ('Levadura fresca', 0.018, 'kg', 1.0, 0.05),
         ('Sal', 0.009, 'kg', 1.0, 0.02),
         ('Pasas', 0.15, 'kg', 1.0, 0.02),
         ('Ron', 0.03, 'L', 1.0, 0),
         ('Leche entera', 0.35, 'L', 1.0, 0.02),
         ('Azúcar', 0.08, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 2, 'ud', 12.0, 0),
         ('Almidón de maíz', 0.03, 'kg', 1.0, 0.02),
         ('Huevo (para pintar)', 1, 'ud', 12.0, 0),
     ],
     'minutos_mo_tanda': 60, 'pvp_con_iva': 1.85, 'iva': 0.10, 'mix_pct': 3.5,
     'via_huevo': '70/2', 'relleno': True, 'estable_ambiente': False,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Plan Semanal · '
                          '12-control-alergenos-vitrina.xlsx!Matriz Alérgenos'),
     'nota': ('La espiral lleva crema pastelera entre las capas: misma clasificación que '
              'la napolitana, aunque todo el mundo la ponga en la bandeja de ambiente.')},

    {'id': 'B6', 'nombre': 'Ensaimada', 'familia': 'Bollería',
     'tanda': 16, 'unidad_venta': 'pieza', 'gramaje_g': 70,
     'lineas': [
         ('Harina de fuerza', 0.60, 'kg', 1.0, 0.08),
         ('Manteca de cerdo', 0.20, 'kg', 1.0, 0.03),
         ('Azúcar', 0.12, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 3, 'ud', 12.0, 0),
         ('Levadura fresca', 0.02, 'kg', 1.0, 0.05),
         ('Sal', 0.008, 'kg', 1.0, 0.02),
         ('Azúcar glas', 0.04, 'kg', 1.0, 0.02),
     ],
     'minutos_mo_tanda': 70, 'pvp_con_iva': 1.95, 'iva': 0.10, 'mix_pct': 3.0,
     'via_huevo': 'estable a ambiente', 'relleno': False, 'estable_ambiente': True,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Plan Semanal · '
                          '12-control-alergenos-vitrina.xlsx!Matriz Alérgenos'),
     'nota': ('La ensaimada lisa es la referencia con la que Pastelerías Pomar mide su '
              'pico (PS-41): de 25-30 al día a 150-200 en temporada alta.')},

    # ------------------- PASTELERÍA INDIVIDUAL (6) -----------------------
    {'id': 'PI1', 'nombre': 'Milhojas', 'familia': 'Pastelería individual',
     'tanda': 18, 'unidad_venta': 'pieza', 'gramaje_g': 90,
     'lineas': [
         ('Harina floja', 0.35, 'kg', 1.0, 0.08),
         ('Mantequilla seca (82% MG)', 0.28, 'kg', 1.0, 0.03),
         ('Sal', 0.008, 'kg', 1.0, 0.02),
         ('Leche entera', 0.80, 'L', 1.0, 0.02),
         ('Azúcar', 0.18, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 5, 'ud', 12.0, 0),
         ('Almidón de maíz', 0.06, 'kg', 1.0, 0.02),
         ('Vainilla en pasta', 0.002, 'kg', 1.0, 0),
         ('Nata 35% MG', 0.30, 'L', 1.0, 0.03),
         ('Azúcar glas', 0.05, 'kg', 1.0, 0.02),
     ],
     'minutos_mo_tanda': 75, 'pvp_con_iva': 3.60, 'iva': 0.10, 'mix_pct': 4.0,
     'via_huevo': '70/2', 'relleno': True, 'estable_ambiente': False,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': 'kit-tareas-pasteleria/12-control-alergenos-vitrina.xlsx!Matriz Alérgenos',
     'nota': '4 °C y 24 h: crema pastelera y nata montada entre hojaldres.'},

    {'id': 'PI2', 'nombre': 'Éclair', 'familia': 'Pastelería individual',
     'tanda': 24, 'unidad_venta': 'pieza', 'gramaje_g': 85,
     'lineas': [
         ('Harina floja', 0.18, 'kg', 1.0, 0.08),
         ('Mantequilla', 0.14, 'kg', 1.0, 0.03),
         ('Huevos (unidades)', 6, 'ud', 12.0, 0),
         ('Sal', 0.004, 'kg', 1.0, 0.02),
         ('Leche entera', 0.70, 'L', 1.0, 0.02),
         ('Azúcar', 0.16, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 4, 'ud', 12.0, 0),
         ('Almidón de maíz', 0.055, 'kg', 1.0, 0.02),
         ('Vainilla en pasta', 0.002, 'kg', 1.0, 0),
         ('Chocolate negro 70%', 0.12, 'kg', 1.0, 0.02),
         ('Azúcar glas', 0.06, 'kg', 1.0, 0.02),
     ],
     'minutos_mo_tanda': 65, 'pvp_con_iva': 3.20, 'iva': 0.10, 'mix_pct': 3.5,
     'via_huevo': '70/2', 'relleno': True, 'estable_ambiente': False,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': 'kit-tareas-pasteleria/12-control-alergenos-vitrina.xlsx!Matriz Alérgenos',
     'nota': 'La pasta choux se hornea muy por encima de los 70 °C; el relleno manda el frío.'},

    {'id': 'PI3', 'nombre': 'Macarons de frambuesa', 'familia': 'Pastelería individual',
     'tanda': 30, 'unidad_venta': 'pieza', 'gramaje_g': 25,
     'lineas': [
         ('Harina de almendra', 0.15, 'kg', 1.0, 0.02),
         ('Azúcar glas', 0.15, 'kg', 1.0, 0.02),
         ('Claras de huevo', 0.11, 'kg', 1.0, 0.05),
         ('Azúcar', 0.15, 'kg', 1.0, 0.02),
         ('Frambuesa congelada', 0.10, 'kg', 1.0, 0.07),
         ('Chocolate blanco', 0.08, 'kg', 1.0, 0.12),
         ('Colorante rojo (bote 50 g · 2 g/tanda)', 0.04, 'ud', 1.0, 0),
     ],
     'minutos_mo_tanda': 80, 'pvp_con_iva': 2.10, 'iva': 0.10, 'mix_pct': 7.0,
     'via_huevo': '70/2', 'relleno': True, 'estable_ambiente': False,
     'pico': None,
     'fuente_escandallo': F_KIT_MA, 'fuente_pvp': 'supuesto',
     'fuente_gramaje': 'kit-escandallos/05-pasteleria.xlsx!Macarons (0,78 kg / 30 uds)',
     'nombre_en_el_kit': 'kit-tareas-pasteleria/12-control-alergenos-vitrina.xlsx!Matriz Alérgenos',
     'nombre_literal_en_kit': 'Macarons (caja de 6)',
     'nota': ('COPIA EXACTA del kit de escandallos, que lo escandalla por tanda de 30 '
              'unidades. En vitrina se despacha suelto o en caja de 6, que es como lo '
              'llama la matriz de alérgenos del kit. La concha se hornea (vía 1.a) y la '
              'ganache lo convierte en producto relleno. Si tu ganache es estable a '
              'temperatura ambiente y lo justificas en tu plan de APPCC, cambia la vía a '
              '«estable a ambiente»: esa justificación es tuya, no del real decreto.')},

    {'id': 'PI4', 'nombre': 'Tartaleta de frutas', 'familia': 'Pastelería individual',
     'tanda': 20, 'unidad_venta': 'pieza', 'gramaje_g': 95,
     'lineas': [
         ('Harina floja', 0.40, 'kg', 1.0, 0.08),
         ('Mantequilla', 0.20, 'kg', 1.0, 0.03),
         ('Azúcar glas', 0.12, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 2, 'ud', 12.0, 0),
         ('Sal', 0.004, 'kg', 1.0, 0.02),
         ('Leche entera', 0.50, 'L', 1.0, 0.02),
         ('Azúcar', 0.11, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 3, 'ud', 12.0, 0),
         ('Almidón de maíz', 0.04, 'kg', 1.0, 0.02),
         ('Fresa fresca', 0.35, 'kg', 1.0, 0.12),
         ('Kiwi', 0.20, 'kg', 1.0, 0.18),
         ('Frutos rojos congelados', 0.15, 'kg', 1.0, 0.03),
         ('Gelatina neutra de brillo', 0.08, 'kg', 1.0, 0.02),
     ],
     'minutos_mo_tanda': 85, 'pvp_con_iva': 3.80, 'iva': 0.10, 'mix_pct': 3.0,
     'via_huevo': '70/2', 'relleno': True, 'estable_ambiente': False,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': 'kit-tareas-pasteleria/12-control-alergenos-vitrina.xlsx!Matriz Alérgenos',
     'nota': ('La fruta fresca cortada tiene además su propia fila en el art. 4.1 (fila 10, '
              '4 °C): aquí coincide con la de producto relleno y no cambia el resultado.')},

    {'id': 'PI5', 'nombre': 'Lionesa o profiterol', 'familia': 'Pastelería individual',
     'tanda': 40, 'unidad_venta': 'pieza', 'gramaje_g': 45,
     'lineas': [
         ('Harina floja', 0.20, 'kg', 1.0, 0.08),
         ('Mantequilla', 0.16, 'kg', 1.0, 0.03),
         ('Huevos (unidades)', 7, 'ud', 12.0, 0),
         ('Sal', 0.004, 'kg', 1.0, 0.02),
         ('Nata 35% MG', 0.55, 'L', 1.0, 0.03),
         ('Azúcar glas', 0.06, 'kg', 1.0, 0.02),
         ('Chocolate negro 70%', 0.10, 'kg', 1.0, 0.02),
     ],
     'minutos_mo_tanda': 60, 'pvp_con_iva': 2.30, 'iva': 0.10, 'mix_pct': 3.0,
     'via_huevo': '70/2', 'relleno': True, 'estable_ambiente': False,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': 'kit-tareas-pasteleria/12-control-alergenos-vitrina.xlsx!Matriz Alérgenos',
     'nota': 'Nata montada dentro: 4 °C y 24 h.'},

    {'id': 'PI6', 'nombre': 'Entremet individual', 'familia': 'Pastelería individual',
     'tanda': 16, 'unidad_venta': 'pieza', 'gramaje_g': 110,
     'lineas': [
         ('Harina floja', 0.10, 'kg', 1.0, 0.08),
         ('Azúcar', 0.22, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 4, 'ud', 12.0, 0),
         ('Chocolate negro 70%', 0.28, 'kg', 1.0, 0.02),
         ('Nata 35% MG', 0.45, 'L', 1.0, 0.03),
         ('Yema pasteurizada (ovoproducto)', 0.09, 'kg', 1.0, 0.02),
         ('Gelatina en hoja', 0.006, 'kg', 1.0, 0),
         ('Frutos rojos congelados', 0.18, 'kg', 1.0, 0.03),
         ('Cobertura de leche 40%', 0.12, 'kg', 1.0, 0.02),
     ],
     'minutos_mo_tanda': 95, 'pvp_con_iva': 4.50, 'iva': 0.10, 'mix_pct': 1.5,
     'via_huevo': 'ovoproducto', 'relleno': True, 'estable_ambiente': False,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': 'kit-tareas-pasteleria/12-control-alergenos-vitrina.xlsx!Matriz Alérgenos',
     'nota': ('El caso que hay que enseñar: la mousse lleva yema y el almíbar de un '
              'merengue italiano NO garantiza 70 °C durante 2 s en el CENTRO del producto. '
              'Si no lo mides con sonda y lo registras, la vía no es la 1.a): es el '
              'ovoproducto pasteurizado del art. 9.2. Y con ovoproducto entran igual los '
              '8 °C y las 24 h del 9.3, que aquí bajan a 4 °C por ir relleno.')},

    # -------------------- TARTAS Y ENTREMETS (6) -------------------------
    # Unidad de venta: la RACIÓN. La tanda es una tarta de 12 raciones, igual
    # que en el kit de escandallos, porque la tarta por encargo se cotiza por
    # ración (cap. 12) y así las dos herramientas dicen lo mismo.
    {'id': 'T1', 'nombre': 'Tarta de chocolate 70 %', 'familia': 'Tartas y entremets',
     'tanda': 12, 'unidad_venta': 'ración', 'gramaje_g': 125,
     'lineas': [
         ('Chocolate negro 70%', 0.4, 'kg', 1.0, 0.12),
         ('Mantequilla', 0.25, 'kg', 1.0, 0.03),
         ('Huevos (unidades)', 6, 'ud', 12.0, 0),
         ('Azúcar', 0.2, 'kg', 1.0, 0.02),
         ('Harina floja', 0.12, 'kg', 1.0, 0.08),
         ('Nata 35% MG', 0.2, 'L', 1.0, 0.03),
         ('Cacao en polvo', 0.03, 'kg', 1.0, 0.05),
         ('Sal', 0.003, 'kg', 1.0, 0.02),
     ],
     'minutos_mo_tanda': 45, 'pvp_con_iva': 3.60, 'iva': 0.10, 'mix_pct': 1.2,
     'via_huevo': '70/2', 'relleno': True, 'estable_ambiente': False,
     'pico': None,
     'fuente_escandallo': F_KIT_TC, 'fuente_pvp': 'supuesto',
     'fuente_gramaje': 'kit-escandallos/05-pasteleria.xlsx!Tarta Chocolate (1,50 kg / 12 raciones)',
     'nombre_en_el_kit': 'kit-escandallos/05-pasteleria.xlsx!Tarta Chocolate',
     'nota': ('COPIA EXACTA del kit: «Tarta de Chocolate 70% - 12 raciones». El bizcocho '
              'pasa de los 70 °C, pero la cobertura de nata y chocolate no es estable a '
              'temperatura ambiente, así que va a 4 °C y con el plazo del art. 9.3.')},

    {'id': 'T2', 'nombre': 'Tarta de queso', 'familia': 'Tartas y entremets',
     'tanda': 12, 'unidad_venta': 'ración', 'gramaje_g': 120,
     'lineas': [
         ('Queso crema', 0.90, 'kg', 1.0, 0.02),
         ('Azúcar', 0.22, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 5, 'ud', 12.0, 0),
         ('Nata 35% MG', 0.25, 'L', 1.0, 0.03),
         ('Harina floja', 0.03, 'kg', 1.0, 0.08),
     ],
     'minutos_mo_tanda': 30, 'pvp_con_iva': 3.40, 'iva': 0.10, 'mix_pct': 1.5,
     'via_huevo': '70/2', 'relleno': False, 'estable_ambiente': False,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Plan Semanal · '
                          '12-control-alergenos-vitrina.xlsx!Matriz Alérgenos'),
     'nota': ('El contraejemplo que hace ver que 4 °C y 8 °C no son un conflicto sino dos '
              'topes distintos: la tarta de queso NO es un producto RELLENO (es una masa '
              'homogénea horneada), así que la fila 9 del art. 4.1 no le aplica y su techo '
              'es el del art. 9.3: 8 °C. El plazo de 24 h sí le aplica.')},

    {'id': 'T3', 'nombre': 'Tarta de manzana', 'familia': 'Tartas y entremets',
     'tanda': 12, 'unidad_venta': 'ración', 'gramaje_g': 130,
     'lineas': [
         ('Harina floja', 0.30, 'kg', 1.0, 0.08),
         ('Mantequilla', 0.15, 'kg', 1.0, 0.03),
         ('Azúcar', 0.10, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 2, 'ud', 12.0, 0),
         ('Manzana', 1.10, 'kg', 1.0, 0.22),
         ('Mermelada de albaricoque', 0.10, 'kg', 1.0, 0.02),
         ('Canela molida', 0.003, 'kg', 1.0, 0),
     ],
     'minutos_mo_tanda': 40, 'pvp_con_iva': 3.20, 'iva': 0.10, 'mix_pct': 1.1,
     'via_huevo': 'estable a ambiente', 'relleno': False, 'estable_ambiente': True,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Plan Semanal · '
                          '12-control-alergenos-vitrina.xlsx!Matriz Alérgenos'),
     'nota': ('Sin crema y con la fruta horneada y abrillantada: estable a temperatura '
              'ambiente. Es la tarta que puede estar en la vitrina de ambiente. Si le '
              'pones crema pastelera debajo, cambia de clasificación y de mueble.')},

    {'id': 'T4', 'nombre': 'Tarta de zanahoria', 'familia': 'Tartas y entremets',
     'tanda': 12, 'unidad_venta': 'ración', 'gramaje_g': 125,
     'lineas': [
         ('Zanahoria', 0.55, 'kg', 1.0, 0.20),
         ('Harina floja', 0.30, 'kg', 1.0, 0.08),
         ('Azúcar', 0.28, 'kg', 1.0, 0.02),
         ('Aceite de girasol', 0.22, 'L', 1.0, 0),
         ('Huevos (unidades)', 4, 'ud', 12.0, 0),
         ('Nueces', 0.10, 'kg', 1.0, 0.05),
         ('Canela molida', 0.005, 'kg', 1.0, 0),
         ('Levadura química (impulsor)', 0.012, 'kg', 1.0, 0),
         ('Queso crema', 0.35, 'kg', 1.0, 0.02),
         ('Azúcar glas', 0.14, 'kg', 1.0, 0.02),
         ('Mantequilla', 0.08, 'kg', 1.0, 0.03),
     ],
     'minutos_mo_tanda': 45, 'pvp_con_iva': 3.30, 'iva': 0.10, 'mix_pct': 0.9,
     'via_huevo': '70/2', 'relleno': True, 'estable_ambiente': False,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Plan Semanal · '
                          '12-control-alergenos-vitrina.xlsx!Matriz Alérgenos'),
     'nota': 'El frosting de queso va entre bizcochos: producto relleno y no estable.'},

    {'id': 'T5', 'nombre': 'Tarta Sacher', 'familia': 'Tartas y entremets',
     'tanda': 12, 'unidad_venta': 'ración', 'gramaje_g': 115,
     'lineas': [
         ('Chocolate negro 70%', 0.30, 'kg', 1.0, 0.02),
         ('Mantequilla', 0.18, 'kg', 1.0, 0.03),
         ('Azúcar', 0.20, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 6, 'ud', 12.0, 0),
         ('Harina floja', 0.14, 'kg', 1.0, 0.08),
         ('Mermelada de albaricoque', 0.20, 'kg', 1.0, 0.02),
         ('Nata 35% MG', 0.12, 'L', 1.0, 0.03),
     ],
     'minutos_mo_tanda': 55, 'pvp_con_iva': 3.80, 'iva': 0.10, 'mix_pct': 0.8,
     'via_huevo': 'estable a ambiente', 'relleno': True, 'estable_ambiente': True,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Plan Semanal · '
                          '12-control-alergenos-vitrina.xlsx!Matriz Alérgenos'),
     'nota': ('El único caso de la carta en el que la excepción de la fila 9 hace trabajo: '
              'la Sacher SÍ es un producto relleno (mermelada de albaricoque) y aun así '
              'queda fuera de los 4 °C, porque el conjunto -mermelada y glaseado, sin '
              'nata- es estable a temperatura ambiente. El azúcar es el conservante.')},

    {'id': 'T6', 'nombre': 'Tarta de nata y fresas', 'familia': 'Tartas y entremets',
     'tanda': 12, 'unidad_venta': 'ración', 'gramaje_g': 135,
     'lineas': [
         ('Harina floja', 0.16, 'kg', 1.0, 0.08),
         ('Azúcar', 0.20, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 6, 'ud', 12.0, 0),
         ('Nata 35% MG', 0.75, 'L', 1.0, 0.03),
         ('Azúcar glas', 0.08, 'kg', 1.0, 0.02),
         ('Fresa fresca', 0.45, 'kg', 1.0, 0.12),
         ('Gelatina neutra de brillo', 0.05, 'kg', 1.0, 0.02),
     ],
     'minutos_mo_tanda': 50, 'pvp_con_iva': 3.50, 'iva': 0.10, 'mix_pct': 1.0,
     'via_huevo': '70/2', 'relleno': True, 'estable_ambiente': False,
     'pico': 'Comuniones',
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': 'nueva en la guía: no está precargada en el kit',
     'nota': ('Es la tarta de encargo por excelencia: la que se vende por raciones para '
              'comuniones y cumpleaños. Cap. 16: anticipo, calendario y anulación.')},

    # ----------------- PANES DE ACOMPAÑAMIENTO (4) -----------------------
    # IVA 4 %: son productos del RD 308/2019 y la Resolución vinculante de la
    # DGT de 24-02-2025 les aplica el tipo superreducido, pan especial incluido
    # (PA-36b). Es la única familia de la carta que no va al 10 %.
    {'id': 'PA1', 'nombre': 'Barra', 'familia': 'Panes de acompañamiento',
     'tanda': 40, 'unidad_venta': 'pieza', 'gramaje_g': 250,
     'lineas': [
         ('Harina panificable', 6.0, 'kg', 1.0, 0.03),
         ('Levadura fresca', 0.06, 'kg', 1.0, 0.05),
         ('Sal', 0.12, 'kg', 1.0, 0.02),
     ],
     'minutos_mo_tanda': 35, 'pvp_con_iva': 1.20, 'iva': 0.04, 'mix_pct': 16.0,
     'via_huevo': 'sin huevo', 'relleno': False, 'estable_ambiente': True,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Plan Semanal · '
                          '12-control-alergenos-vitrina.xlsx!Matriz Alérgenos'),
     'nota': ('Pan común del RD 308/2019: IVA 4 %. Es la referencia que trae gente a la '
              'tienda todos los días, no la que deja margen. Si vendes pan, además del '
              'IVA entra el RD 308/2019 entero (PA-25).')},

    {'id': 'PA2', 'nombre': 'Chapata', 'familia': 'Panes de acompañamiento',
     'tanda': 24, 'unidad_venta': 'pieza', 'gramaje_g': 200,
     'lineas': [
         ('Harina panificable', 4.2, 'kg', 1.0, 0.03),
         ('Levadura fresca', 0.03, 'kg', 1.0, 0.05),
         ('Sal', 0.09, 'kg', 1.0, 0.02),
         ('Aceite de oliva virgen extra', 0.05, 'L', 1.0, 0),
     ],
     'minutos_mo_tanda': 30, 'pvp_con_iva': 1.60, 'iva': 0.04, 'mix_pct': 4.0,
     'via_huevo': 'sin huevo', 'relleno': False, 'estable_ambiente': True,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Plan Semanal · '
                          '12-control-alergenos-vitrina.xlsx!Matriz Alérgenos'),
     'nota': 'Pan especial del RD 308/2019, y desde 2025 también al 4 % (PA-36b).'},

    {'id': 'PA3', 'nombre': 'Hogaza de masa madre', 'familia': 'Panes de acompañamiento',
     'tanda': 12, 'unidad_venta': 'pieza', 'gramaje_g': 550,
     'lineas': [
         ('Harina panificable', 5.5, 'kg', 1.0, 0.03),
         ('Harina integral de centeno', 0.6, 'kg', 1.0, 0.03),
         ('Sal', 0.13, 'kg', 1.0, 0.02),
     ],
     'minutos_mo_tanda': 40, 'pvp_con_iva': 3.90, 'iva': 0.04, 'mix_pct': 3.5,
     'via_huevo': 'sin huevo', 'relleno': False, 'estable_ambiente': True,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Plan Semanal · '
                          '12-control-alergenos-vitrina.xlsx!Matriz Alérgenos'),
     'nota': ('La masa madre no se escandalla aparte: es harina y agua refrescadas, y el '
              'coste ya está dentro de la harina. Ojo con las menciones del RD 308/2019 '
              'para llamarla «masa madre» en la etiqueta (PA-25).')},

    {'id': 'PA4', 'nombre': 'Pan de molde', 'familia': 'Panes de acompañamiento',
     'tanda': 10, 'unidad_venta': 'pieza', 'gramaje_g': 500,
     'lineas': [
         ('Harina de fuerza', 3.2, 'kg', 1.0, 0.03),
         ('Leche entera', 1.4, 'L', 1.0, 0.02),
         ('Mantequilla', 0.25, 'kg', 1.0, 0.03),
         ('Azúcar', 0.16, 'kg', 1.0, 0.02),
         ('Levadura fresca', 0.07, 'kg', 1.0, 0.05),
         ('Sal', 0.06, 'kg', 1.0, 0.02),
     ],
     'minutos_mo_tanda': 30, 'pvp_con_iva': 3.20, 'iva': 0.04, 'mix_pct': 2.5,
     'via_huevo': 'sin huevo', 'relleno': False, 'estable_ambiente': True,
     'pico': None,
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/10-plan-produccion-semanal.xlsx!Plan Semanal · '
                          '12-control-alergenos-vitrina.xlsx!Matriz Alérgenos'),
     'nota': 'Pan especial del RD 308/2019: 4 %.'},

    # --------------------------- TEMPORADA (8) ---------------------------
    # Las ocho de la categoría «Temporada» de la matriz de alérgenos del kit,
    # con sus nombres literales. Cada una cuelga de uno de los 6 picos.
    {'id': 'TP1', 'nombre': 'Roscón de Reyes', 'familia': 'Temporada',
     'tanda': 12, 'unidad_venta': 'pieza', 'gramaje_g': 600,
     'lineas': [
         ('Harina de fuerza', 3.0, 'kg', 1.0, 0.08),
         ('Mantequilla', 0.60, 'kg', 1.0, 0.03),
         ('Azúcar', 0.60, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 12, 'ud', 12.0, 0),
         ('Leche entera', 0.75, 'L', 1.0, 0.02),
         ('Levadura fresca', 0.12, 'kg', 1.0, 0.05),
         ('Sal', 0.04, 'kg', 1.0, 0.02),
         ('Agua de azahar', 0.04, 'L', 1.0, 0),
         ('Naranja confitada', 0.35, 'kg', 1.0, 0.02),
         ('Almendra marcona cruda', 0.20, 'kg', 1.0, 0.03),
         ('Azúcar glas', 0.10, 'kg', 1.0, 0.02),
         ('Nata 35% MG', 2.40, 'L', 1.0, 0.03),
     ],
     'minutos_mo_tanda': 90, 'pvp_con_iva': 16.50, 'iva': 0.10, 'mix_pct': 1.2,
     'via_huevo': '70/2', 'relleno': True, 'estable_ambiente': False,
     'pico': 'Reyes',
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': ('kit-tareas-pasteleria/12-control-alergenos-vitrina.xlsx!Matriz '
                          'Alérgenos (categoría Temporada) · BONUS-02-calendario-anual-tareas.xlsx'),
     'nota': ('Roscón de 6 raciones RELLENO de nata. El roscón sin rellenar es estable a '
              'temperatura ambiente; el relleno lo baja a 4 °C y le mete las 24 h del '
              'art. 9.3 encima del día de más producción del año. Esa es la restricción '
              'operativa que decide cuánta nata se monta y a qué hora (cap. 15). '
              'Referencia de escala, no de precio: PS-35 (30 millones de roscones en '
              'España) y PS-46 (el supermercado entra a 9 €).')},

    {'id': 'TP2', 'nombre': 'Torrijas', 'familia': 'Temporada',
     'tanda': 30, 'unidad_venta': 'pieza', 'gramaje_g': 90,
     'lineas': [
         ('Harina de fuerza', 1.20, 'kg', 1.0, 0.08),
         ('Huevos (unidades)', 4, 'ud', 12.0, 0),
         ('Leche entera', 2.60, 'L', 1.0, 0.02),
         ('Azúcar', 0.45, 'kg', 1.0, 0.02),
         ('Canela molida', 0.006, 'kg', 1.0, 0),
         ('Aceite de girasol', 0.55, 'L', 1.0, 0.20),
         ('Limón', 0.12, 'kg', 1.0, 0.25),
     ],
     'minutos_mo_tanda': 70, 'pvp_con_iva': 2.40, 'iva': 0.10, 'mix_pct': 1.3,
     'via_huevo': '70/2', 'relleno': False, 'estable_ambiente': False,
     'pico': 'Semana Santa',
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': 'kit-tareas-pasteleria/12-control-alergenos-vitrina.xlsx!Matriz Alérgenos',
     'nota': ('No es un producto relleno, así que su techo es el del art. 9.3: 8 °C. '
              'Empapada en leche y huevo y frita: no es estable a temperatura ambiente.')},

    {'id': 'TP3', 'nombre': 'Buñuelos de viento', 'familia': 'Temporada',
     'tanda': 60, 'unidad_venta': 'pieza', 'gramaje_g': 35,
     'lineas': [
         ('Harina floja', 0.35, 'kg', 1.0, 0.08),
         ('Mantequilla', 0.25, 'kg', 1.0, 0.03),
         ('Huevos (unidades)', 10, 'ud', 12.0, 0),
         ('Sal', 0.005, 'kg', 1.0, 0.02),
         ('Aceite de girasol', 0.70, 'L', 1.0, 0.20),
         ('Azúcar', 0.15, 'kg', 1.0, 0.02),
         ('Leche entera', 0.80, 'L', 1.0, 0.02),
         ('Azúcar', 0.18, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 5, 'ud', 12.0, 0),
         ('Almidón de maíz', 0.06, 'kg', 1.0, 0.02),
     ],
     'minutos_mo_tanda': 75, 'pvp_con_iva': 1.60, 'iva': 0.10, 'mix_pct': 1.0,
     'via_huevo': '70/2', 'relleno': True, 'estable_ambiente': False,
     'pico': 'Todos los Santos',
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': 'kit-tareas-pasteleria/12-control-alergenos-vitrina.xlsx!Matriz Alérgenos',
     'nota': 'Rellenos de crema: 4 °C y 24 h en la semana de más volumen de otoño.'},

    {'id': 'TP4', 'nombre': 'Huesos de santo', 'familia': 'Temporada',
     'tanda': 40, 'unidad_venta': 'pieza', 'gramaje_g': 40,
     'lineas': [
         ('Almendra molida', 0.70, 'kg', 1.0, 0.02),
         ('Azúcar', 0.70, 'kg', 1.0, 0.02),
         ('Yema pasteurizada (ovoproducto)', 0.30, 'kg', 1.0, 0.02),
         ('Azúcar glas', 0.10, 'kg', 1.0, 0.02),
         ('Limón', 0.05, 'kg', 1.0, 0.25),
     ],
     'minutos_mo_tanda': 85, 'pvp_con_iva': 1.90, 'iva': 0.10, 'mix_pct': 0.8,
     'via_huevo': 'estable a ambiente', 'relleno': True, 'estable_ambiente': True,
     'pico': 'Todos los Santos',
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': 'kit-tareas-pasteleria/12-control-alergenos-vitrina.xlsx!Matriz Alérgenos',
     'nota': ('Segundo caso en el que la excepción de la fila 9 salva a un producto '
              'relleno: mazapán y yema confitada con almíbar, los dos con una '
              'concentración de azúcar que los hace estables a temperatura ambiente. '
              'Aun así se elabora con yema pasteurizada, que es lo que permite el '
              'volumen de la campaña sin depender de la sonda.')},

    {'id': 'TP5', 'nombre': 'Panellets', 'familia': 'Temporada',
     'tanda': 60, 'unidad_venta': 'pieza', 'gramaje_g': 30,
     'lineas': [
         ('Almendra molida', 1.00, 'kg', 1.0, 0.02),
         ('Azúcar', 0.90, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 2, 'ud', 12.0, 0),
         ('Piñón', 0.35, 'kg', 1.0, 0.02),
         ('Limón', 0.05, 'kg', 1.0, 0.25),
     ],
     'minutos_mo_tanda': 90, 'pvp_con_iva': 1.85, 'iva': 0.10, 'mix_pct': 0.7,
     'via_huevo': 'estable a ambiente', 'relleno': False, 'estable_ambiente': True,
     'pico': 'Todos los Santos',
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': 'kit-tareas-pasteleria/12-control-alergenos-vitrina.xlsx!Matriz Alérgenos',
     'nota': ('El piñón a 58 €/kg es el ingrediente más caro de toda la carta y es lo que '
              'hace que el panellet de piñón se venda al peso y no por unidad en media '
              'España. Precio supuesto: es el que más conviene renegociar cada año.')},

    {'id': 'TP6', 'nombre': 'Polvorón o mantecado', 'familia': 'Temporada',
     'tanda': 50, 'unidad_venta': 'pieza', 'gramaje_g': 35,
     'lineas': [
         ('Harina floja', 1.10, 'kg', 1.0, 0.08),
         ('Manteca de cerdo', 0.45, 'kg', 1.0, 0.03),
         ('Azúcar glas', 0.45, 'kg', 1.0, 0.02),
         ('Almendra molida', 0.25, 'kg', 1.0, 0.02),
         ('Canela molida', 0.008, 'kg', 1.0, 0),
     ],
     'minutos_mo_tanda': 55, 'pvp_con_iva': 1.20, 'iva': 0.10, 'mix_pct': 1.3,
     'via_huevo': 'sin huevo', 'relleno': False, 'estable_ambiente': True,
     'pico': 'Reyes',
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': 'kit-tareas-pasteleria/12-control-alergenos-vitrina.xlsx!Matriz Alérgenos',
     'nota': ('Se produce en noviembre y se vende hasta Reyes: es la referencia que mejor '
              'aguanta el stock y por eso la que menos tesorería inmoviliza por unidad '
              'de campaña. Va colgada del pico de Reyes en el libro 3.')},

    {'id': 'TP7', 'nombre': 'Turrón de almendra', 'familia': 'Temporada',
     'tanda': 20, 'unidad_venta': 'tableta de 250 g', 'gramaje_g': 250,
     'lineas': [
         ('Almendra marcona cruda', 3.20, 'kg', 1.0, 0.03),
         ('Miel', 1.10, 'kg', 1.0, 0.02),
         ('Azúcar', 0.80, 'kg', 1.0, 0.02),
         ('Claras de huevo', 0.10, 'kg', 1.0, 0.05),
     ],
     'minutos_mo_tanda': 65, 'pvp_con_iva': 10.50, 'iva': 0.10, 'mix_pct': 0.5,
     'via_huevo': 'estable a ambiente', 'relleno': False, 'estable_ambiente': True,
     'pico': 'Reyes',
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': 'kit-tareas-pasteleria/12-control-alergenos-vitrina.xlsx!Matriz Alérgenos',
     'nota': ('La referencia de más margen unitario de la campaña de Navidad (PS-51: 40 % '
              'de margen en el turrón, caso Pomar), y la que más tesorería inmoviliza: '
              'la almendra se compra en octubre y se cobra en diciembre.')},

    {'id': 'TP8', 'nombre': 'Mona de Pascua', 'familia': 'Temporada',
     'tanda': 14, 'unidad_venta': 'pieza', 'gramaje_g': 350,
     'lineas': [
         ('Harina de fuerza', 1.60, 'kg', 1.0, 0.08),
         ('Azúcar', 0.45, 'kg', 1.0, 0.02),
         ('Huevos (unidades)', 10, 'ud', 12.0, 0),
         ('Mantequilla', 0.30, 'kg', 1.0, 0.03),
         ('Leche entera', 0.40, 'L', 1.0, 0.02),
         ('Levadura fresca', 0.06, 'kg', 1.0, 0.05),
         ('Sal', 0.02, 'kg', 1.0, 0.02),
         ('Cobertura de leche 40%', 1.20, 'kg', 1.0, 0.02),
         ('Azúcar glas', 0.08, 'kg', 1.0, 0.02),
     ],
     'minutos_mo_tanda': 80, 'pvp_con_iva': 13.50, 'iva': 0.10, 'mix_pct': 0.7,
     'via_huevo': 'estable a ambiente', 'relleno': False, 'estable_ambiente': True,
     'pico': 'Semana Santa',
     'fuente_escandallo': 'supuesto', 'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nombre_en_el_kit': 'kit-tareas-pasteleria/12-control-alergenos-vitrina.xlsx!Matriz Alérgenos',
     'nota': ('Bollo y figura de chocolate: estable a temperatura ambiente mientras no se '
              'rellene de nata. La versión rellena cambia de mueble y de plazo.')},
]


# ==========================================================================
# 6. CÁLCULO DEL ESCANDALLO Y DE LA VÍA LEGAL
# ==========================================================================
def precio_compra(ingrediente):
    """(precio, unidad de compra, fuente) de un ingrediente."""
    if ingrediente not in PRECIOS_COMPRA:
        raise KeyError('Ingrediente sin precio de compra declarado: %r' % ingrediente)
    return PRECIOS_COMPRA[ingrediente]


def coste_linea(linea):
    """Coste de una línea del escandallo con el MISMO convenio del kit:
    cantidad bruta = cantidad / (1 - merma); coste = bruta / factor × precio."""
    ingrediente, cantidad, _ud_uso, factor, merma = linea
    precio = precio_compra(ingrediente)[0]
    bruta = cantidad / (1.0 - merma)
    return bruta / factor * precio


def coste_materia_tanda(ref):
    """Coste de materia prima de la TANDA completa, sin IVA."""
    return sum(coste_linea(l) for l in ref['lineas'])


def coste_materia_unidad(ref):
    """Coste de materia prima por unidad de venta, sin IVA."""
    return coste_materia_tanda(ref) / float(ref['tanda'])


def coste_hora_obrador():
    """€/hora de obrador. NO es un dato del sector: se CALCULA, y el cap. 12 lo
    enseña a calcular.

        coste empresa anual del obrador / horas productivas del obrador

    · Coste empresa anual = bruto de convenio × 15 pagas × jornada × (1 + SS).
      Sólo las personas de área OBRADOR: el despacho no fabrica.
    · Horas productivas = jornadas × horas anuales de contrato × ratio
      productivo. Las dos últimas son supuestos declarados en `PARAMS`.
    """
    ss = P('ss_empresa')
    pagas = P('pagas_convenio')
    coste = 0.0
    jornadas = 0.0
    for _pid, _perfil, jornada, grupo, area, _h, _turno in PLANTILLA:
        if area != 'OBRADOR':
            continue
        bruto_mes = CONVENIO[grupo - 1][2]
        coste += bruto_mes * pagas * jornada * (1.0 + ss)
        jornadas += jornada
    horas = jornadas * P('horas_anuales_contrato') * P('ratio_horas_productivas')
    return coste / horas


def coste_mano_obra_unidad(ref):
    """Coste de mano de obra imputado por unidad, sin IVA. Es lo que el cap. 12
    llama «dejar de regalar tu trabajo»: la unidad de costeo es la TANDA."""
    return (ref['minutos_mo_tanda'] / 60.0) * coste_hora_obrador() / float(ref['tanda'])


def pvp_sin_iva(ref):
    return ref['pvp_con_iva'] / (1.0 + ref['iva'])


def coste_total_unidad(ref):
    """Materia + mano de obra. NO incluye packaging ni merma: esos suben al
    P&L del libro 5, no al escandallo de la pieza."""
    return coste_materia_unidad(ref) + coste_mano_obra_unidad(ref)


def food_cost(ref):
    """Food cost de la referencia: materia sobre PVP sin IVA. Es el que se
    compara con `food_cost_objetivo` en el semáforo de surtido del libro 4."""
    return coste_materia_unidad(ref) / pvp_sin_iva(ref)


def margen_unidad(ref):
    """Margen de contribución por unidad, sin IVA, después de mano de obra."""
    return pvp_sin_iva(ref) - coste_total_unidad(ref)


def temperatura_legal(ref):
    """D11 y D10. Devuelve (temperatura en °C o None, cuál manda, explicación).

    NO hay «conflicto 4 °C / 8 °C»: son dos topes distintos y manda el más
    bajo de los que apliquen.
      · art. 4.1 fila 9 (PA-12): 4 °C a los productos de pastelería RELLENOS,
        salvo que sean estables a temperatura ambiente.
      · art. 9.3 (PA-14, PA-15): 8 °C a lo elaborado por la vía 1.a) que no
        sea estable a temperatura ambiente y a lo hecho con ovoproducto.
    """
    techos = []
    if ref['relleno'] and not ref['estable_ambiente']:
        techos.append((4, 'RD 1021/2022, art. 4.1, fila 9',
                       'Producto de pastelería relleno que no es estable a temperatura '
                       'ambiente.'))
    if ref['via_huevo'] in ('70/2', 'ovoproducto') and not ref['estable_ambiente']:
        techos.append((8, 'RD 1021/2022, art. 9.3',
                       'Elaborado por la vía del art. 9.1.a) sin ser estable a '
                       'temperatura ambiente, o con ovoproducto del art. 9.2.'))
    if not techos:
        return (None, 'Temperatura ambiente',
                'Ni la fila 9 del art. 4.1 ni el art. 9.3 le fijan techo: puede ir en '
                'vitrina de ambiente. La vida útil la fijas tú y va en tu plan de APPCC.')
    techos.sort(key=lambda t: t[0])
    manda = techos[0]
    if len(techos) == 2:
        explica = ('Le aplican los dos topes (%d °C por el %s y %d °C por el %s) y manda '
                   'el más bajo. No es un conflicto: son dos techos distintos.'
                   % (techos[0][0], techos[0][1], techos[1][0], techos[1][1]))
    else:
        explica = manda[2]
    return (manda[0], manda[1], explica)


def plazo_legal(ref):
    """D11. Devuelve (horas o None, base legal, explicación). Esto es el PLAZO
    LEGAL del art. 9.3, NO la vida útil: la vida útil la declara el lector en
    celda verde y este módulo no la calcula para ninguna de las 30."""
    if ref['via_huevo'] in ('70/2', 'ovoproducto') and not ref['estable_ambiente']:
        return (24, 'RD 1021/2022, art. 9.3',
                'Se consume en un máximo de 24 horas desde su elaboración y hay que '
                'REGISTRAR la fecha y la hora de elaboración. Es la obligación del '
                'art. 9.3 que casi nadie cuenta.')
    return (None, 'No aplica',
            'El plazo de 24 horas del art. 9.3 sólo alcanza a lo elaborado por la vía '
            'del art. 9.1.a) que no sea estable a temperatura ambiente y a lo hecho con '
            'ovoproducto (art. 9.2). No es una vida útil universal de la pastelería.')


#: D11: la vida útil NO se calcula. Es celda verde en el libro 4.
VIDA_UTIL_DECLARADA = None
NOTA_VIDA_UTIL = ('La fijas tú y debe constar en tu plan de APPCC: el RD 1021/2022 no la '
                  'establece. Lo que sí establece es el plazo del art. 9.3, que es otra '
                  'cosa y va en su propia columna.')


def por_familia(familia):
    return [r for r in CARTA if r['familia'] == familia]


def pvp_medio_ponderado():
    """PVP medio con IVA de la carta, ponderado por el mix de unidades."""
    return sum(r['pvp_con_iva'] * r['mix_pct'] for r in CARTA) / 100.0


def ticket_medio_con_iva():
    """N-11 prohíbe publicar un «ticket medio de pastelería»: no existe dato
    público. El de La Clara se CALCULA desde su carta y su mix, y por eso se
    puede publicar diciendo lo que es."""
    return pvp_medio_ponderado() * P('piezas_por_ticket')


def food_cost_carta():
    """Food cost de MATERIA de la carta entera, ponderado por el mix de
    unidades y por el PVP de cada referencia (que es como se pondera de
    verdad: por euros vendidos, no por piezas)."""
    ingresos = sum(pvp_sin_iva(r) * r['mix_pct'] for r in CARTA)
    materia = sum(coste_materia_unidad(r) * r['mix_pct'] for r in CARTA)
    return materia / ingresos


def food_cost_servido():
    """El food cost que llega al P&L del libro 5: al de escandallo hay que
    sumarle lo que se produce y no se vende (merma) y el packaging.

    Es la conversión que casi nadie hace y por la que el escandallo de la pieza
    y la cuenta de resultados nunca cuadran a la primera.
    """
    return food_cost_carta() / (1.0 - P('merma_objetivo')) * (1.0 + P('packaging_pct_coste'))


# ==========================================================================
# 7. EQUIPAMIENTO: dotación tipo línea a línea (D17 y D21)
# ==========================================================================
#: Cada línea lleva SU BASE FISCAL en `base_iva`, porque unos distribuidores
#: publican con IVA y otros sin él, y mezclarlos desvía el CAPEX un 21 % (D17).
#: Valores: 'sin IVA' · 'con IVA' · 'no declarada' (el distribuidor no lo dice;
#: se trata como base imponible y se marca, que es lo honesto).
#:
#: `valor_verificado` es el precio con id `PS-*`; `supuesto_por_defecto` es el
#: valor que se siembra en la celda verde cuando NO hay precio publicado, para
#: que no quede ni una celda verde vacía (D21). Nunca están los dos a la vez.
#:
#: `plazo_semanas` es SUPUESTO en todas: ningún distribuidor publica plazos. Es
#: la columna que mueve la fecha de apertura (libro 7 y ruta crítica del 6).
EQUIPAMIENTO = [
    # --- con precio verificado -------------------------------------------
    {'n': 1, 'partida': 'Horno de convección, 6 bandejas',
     'marca': 'UNOX', 'modelo': 'XB693 Bakerlux', 'categoria': 'Calor',
     'valor_verificado': 3354.12, 'supuesto_por_defecto': None,
     'base_iva': 'con IVA', 'tipo_iva': 0.21, 'fuente': 'PS-72',
     'opcional': False, 'plazo_semanas': 5, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': True,
     'nota': 'Precio publicado CON IVA en la ficha del distribuidor.'},
    {'n': 2, 'partida': 'Horno de convección, 4 bandejas',
     'marca': 'SMEG', 'modelo': 'ALFA420E1HDS', 'categoria': 'Calor',
     'valor_verificado': 2513.41, 'supuesto_por_defecto': None,
     'base_iva': 'con IVA', 'tipo_iva': 0.21, 'fuente': 'PS-72',
     'opcional': False, 'plazo_semanas': 5, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': True,
     'nota': 'Segundo horno: sin él no hay dos cocciones a distinta temperatura a la vez.'},
    {'n': 3, 'partida': 'Vitrina expositora pastelera refrigerada curva',
     'marca': 'Docriluc', 'modelo': 'VEPD-9-15-C', 'categoria': 'Tienda y vitrina',
     'valor_verificado': 2284.10, 'supuesto_por_defecto': None,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'PS-76',
     'opcional': False, 'plazo_semanas': 6, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Tienda y vitrina', 'dotacion_tipo': True,
     'nota': ('1505x900x1305 mm, 452 L, 0,93 m² de exposición, R-290. El precio lleva un '
              'descuento de campaña del 30 % sobre un PVP de 3.263,00 €: es un precio '
              'FECHADO el 10-09-2026 y puede caducar. Si lo reutilizas, vuelve a mirarlo '
              '(D17). Una sola vitrina, contada una sola vez.')},
    {'n': 4, 'partida': 'Puertas correderas traseras para la vitrina',
     'marca': 'Docriluc', 'modelo': 'accesorio VEPD-9-15', 'categoria': 'Tienda y vitrina',
     'valor_verificado': 120.40, 'supuesto_por_defecto': None,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'PS-77',
     'opcional': True, 'plazo_semanas': 6, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Tienda y vitrina', 'dotacion_tipo': False,
     'nota': 'Accesorio: no entra en el subtotal comparable de la dotación tipo.'},
    {'n': 5, 'partida': 'Abatidor de temperatura, 4 bandejas',
     'marca': 'Irinox', 'modelo': 'gama Multifresh', 'categoria': 'Frío negativo',
     'valor_verificado': 10037.00, 'supuesto_por_defecto': None,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'PS-78',
     'opcional': False, 'plazo_semanas': 8, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': True,
     'nota': ('La compra más cara y la que más se discute (decisión 2 del bonus 2). '
              'Ciclos de +85 °C a -40 °C. Un arcón doméstico NO vale como abatidor: el '
              'art. 5 del RD 1021/2022 exige potencia suficiente para llegar a -18 °C en '
              'el centro con un descenso ininterrumpido (PA-13).')},
    {'n': 6, 'partida': 'Laminadora automática de masa, hasta 40 cm',
     'marca': 'Sammic', 'modelo': 'DF-40', 'categoria': 'Laminación',
     'valor_verificado': 1215.00, 'supuesto_por_defecto': None,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'PS-79',
     'opcional': False, 'plazo_semanas': 4, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': True,
     'nota': '1.215,00 € sin IVA / 1.470,15 € con IVA, según la propia ficha.'},
    {'n': 7, 'partida': 'Batidora planetaria, 20 L',
     'marca': 'Sammic', 'modelo': 'BP-20', 'categoria': 'Amasado y batido',
     'valor_verificado': 595.04, 'supuesto_por_defecto': None,
     'base_iva': 'no declarada', 'tipo_iva': 0.21, 'fuente': 'PS-81',
     'opcional': False, 'plazo_semanas': 3, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': True,
     'nota': ('900 W, 95-392 rpm, temporizador 0-99 min. La ficha NO declara si el precio '
              'lleva IVA: se trata como base imponible y se marca. Es exactamente el caso '
              'que obliga a tener la columna.')},
    {'n': 8, 'partida': 'Atemperadora de chocolate, 12 kg',
     'marca': 'Selmi', 'modelo': 'One', 'categoria': 'Chocolate',
     'valor_verificado': 7400.00, 'supuesto_por_defecto': None,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'PS-82',
     'opcional': True, 'plazo_semanas': 7, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': False,
     'nota': ('OPCIONAL según el concepto: sólo si abres línea de bombonería o '
              'chocolatería. Por eso queda FUERA del subtotal comparable de la dotación '
              'tipo (D17): con ella dentro, un solo equipo era el 25 % del subtotal.')},

    # --- sin precio publicado: celda verde con supuesto por defecto (D21) --
    {'n': 9, 'partida': 'Horno de pisos modular (deck)',
     'marca': 'Salva', 'modelo': 'gama modular de 1 a 5 módulos', 'categoria': 'Calor',
     'valor_verificado': None, 'supuesto_por_defecto': 12000.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'PS-73 + supuesto',
     'opcional': True, 'plazo_semanas': 12, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': False,
     'nota': ('Salva vende por distribuidor y presupuesto: no hay precio publicado. '
              'Bongard, Wiesheu, Miwe y Sveba Dahlen, igual. El valor por defecto es un '
              'SUPUESTO para que la celda no quede vacía: pide tres presupuestos.')},
    {'n': 10, 'partida': 'Cámara de fermentación controlada (roll-in)',
     'marca': None, 'modelo': None, 'categoria': 'Frío positivo',
     'valor_verificado': None, 'supuesto_por_defecto': 8500.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'PS-83 + supuesto',
     'opcional': False, 'plazo_semanas': 9, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': False,
     'nota': ('PS-83 da un RANGO de categoría (hasta 19.438 € en la gama alta), no una '
              'ficha de producto: no es un precio. El valor por defecto es supuesto. Es '
              'lo que permite que la bollería esté horneada a las 7:00 sin entrar a las 3.')},
    {'n': 11, 'partida': 'Conducto de extracción de humos en acero inoxidable',
     'marca': None, 'modelo': None, 'categoria': 'Instalaciones',
     'valor_verificado': None, 'supuesto_por_defecto': 6500.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'PS-84 + supuesto',
     'opcional': False, 'plazo_semanas': 6, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': False,
     'nota': ('PS-84 dice «puede superar los 6.000 €»: es una frase, no un presupuesto. '
              'La partida que más locales tumba, y la que hay que resolver ANTES de '
              'firmar (cap. 06). El aire de la campana es categoría AE4 del RITE y no '
              'puede compartir conducto con el del despacho (PA-07b).')},
    {'n': 12, 'partida': 'Amasadora de espiral, 25 kg',
     'marca': None, 'modelo': None, 'categoria': 'Amasado y batido',
     'valor_verificado': None, 'supuesto_por_defecto': 5200.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'opcional': False, 'plazo_semanas': 6, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': False,
     'nota': ('PS-75 da 4.000-8.000 € para «amasadora industrial», pero es un rango sin '
              'marca ni modelo: se usa como orden de magnitud, no como precio.')},
    {'n': 13, 'partida': 'Cámara frigorífica modular de conservación (8 m³)',
     'marca': None, 'modelo': None, 'categoria': 'Frío positivo',
     'valor_verificado': None, 'supuesto_por_defecto': 4800.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'opcional': False, 'plazo_semanas': 7, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': False,
     'nota': 'Es la que sostiene los 4 °C de la fila 9 del art. 4.1 (PA-12).'},
    {'n': 14, 'partida': 'Armario de congelación -18 °C',
     'marca': None, 'modelo': None, 'categoria': 'Frío negativo',
     'valor_verificado': None, 'supuesto_por_defecto': 1900.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'opcional': False, 'plazo_semanas': 4, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': False,
     'nota': ('CONSERVA congelado; no congela. No sustituye al abatidor (art. 5 del '
              'RD 1021/2022, PA-13).')},
    {'n': 15, 'partida': 'Mesa de trabajo refrigerada con cajones (2 m)',
     'marca': None, 'modelo': None, 'categoria': 'Frío positivo',
     'valor_verificado': None, 'supuesto_por_defecto': 2400.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'opcional': False, 'plazo_semanas': 5, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': False, 'nota': ''},
    {'n': 16, 'partida': 'Mesas de acero inoxidable y estanterías (lote)',
     'marca': None, 'modelo': None, 'categoria': 'Mobiliario de obrador',
     'valor_verificado': None, 'supuesto_por_defecto': 2800.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'opcional': False, 'plazo_semanas': 4, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': False, 'nota': ''},
    {'n': 17, 'partida': 'Fregadero doble y lavamanos no manual de pedal',
     'marca': None, 'modelo': None, 'categoria': 'Instalaciones',
     'valor_verificado': None, 'supuesto_por_defecto': 1400.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'PS-86e + supuesto',
     'opcional': False, 'plazo_semanas': 3, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': False,
     'nota': 'PS-86e: lavamanos NO manual por zona. No es un extra, es un requisito.'},
    {'n': 18, 'partida': 'Mobiliario de despacho (mostrador, estanterías, rótulo interior)',
     'marca': None, 'modelo': None, 'categoria': 'Tienda y vitrina',
     'valor_verificado': None, 'supuesto_por_defecto': 7500.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'opcional': False, 'plazo_semanas': 8, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Tienda y vitrina', 'dotacion_tipo': False, 'nota': ''},
    {'n': 19, 'partida': 'TPV con software adaptado a Verifactu',
     'marca': None, 'modelo': None, 'categoria': 'Tienda y vitrina',
     'valor_verificado': None, 'supuesto_por_defecto': 1300.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'PA-37 + supuesto',
     'opcional': False, 'plazo_semanas': 3, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Tienda y vitrina', 'dotacion_tipo': False,
     'nota': ('El software que compres HOY ya tiene que estar adaptado: la obligación del '
              'fabricante es anterior a la tuya (PA-37). Y el TPV es el que separa el '
              '10 %, el 4 % y el 21 % de la venta para llevar (PA-36d).')},
    {'n': 20, 'partida': 'Vitrina o armario expositor de temperatura ambiente',
     'marca': None, 'modelo': None, 'categoria': 'Tienda y vitrina',
     'valor_verificado': None, 'supuesto_por_defecto': 1600.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'opcional': False, 'plazo_semanas': 6, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Tienda y vitrina', 'dotacion_tipo': False,
     'nota': ('Para lo estable a temperatura ambiente: palmeras, Sacher, huesos de santo, '
              'turrón y panes. Cuántos metros necesitas de este mueble y cuántos del '
              'refrigerado lo decide la hoja de huevo y temperatura del libro 4, no el gusto.')},
    {'n': 21, 'partida': 'Envasadora, selladora y utillaje de obrador (lote)',
     'marca': None, 'modelo': None, 'categoria': 'Mobiliario de obrador',
     'valor_verificado': None, 'supuesto_por_defecto': 3200.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'opcional': False, 'plazo_semanas': 4, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': False, 'nota': ''},
    {'n': 22, 'partida': 'Termómetros sonda, básculas y registradores de temperatura',
     'marca': None, 'modelo': None, 'categoria': 'Control',
     'valor_verificado': None, 'supuesto_por_defecto': 900.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'opcional': False, 'plazo_semanas': 2, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipamiento de obrador', 'dotacion_tipo': False,
     'nota': ('Sin sonda no puedes demostrar los 70 °C/2 s del art. 9.1.a) y la vía se te '
              'cae al ovoproducto. Es la compra más barata con más consecuencias.')},
]

#: Subtotal comparable de PS-85i: los seis equipos de la dotación tipo, TODOS
#: llevados a base sin IVA y con la atemperadora fuera. Sirve de gate: si la
#: suma se despega del id publicado, algo se ha tocado.
PS_85I_SUBTOTAL = 18980.14
PS_85I_TOLERANCIA = 0.60   # PS-85i redondeó la conversión del SMEG a 2.077,00 €


def precio_equipamiento_sin_iva(eq):
    """Precio de una línea llevado a base imponible. `base_iva` dice de dónde
    parte: sin ese dato el CAPEX sale un 21 % desviado (D17)."""
    precio = eq['valor_verificado'] if eq['valor_verificado'] is not None else eq['supuesto_por_defecto']
    if eq['base_iva'] == 'con IVA':
        return precio / (1.0 + eq['tipo_iva'])
    return precio        # 'sin IVA' y 'no declarada' se tratan como base imponible


def dotacion_tipo_sin_iva():
    """Los seis equipos de PS-85i, en una sola base y sin la atemperadora."""
    return sum(precio_equipamiento_sin_iva(e) for e in EQUIPAMIENTO if e['dotacion_tipo'])


def equipamiento_bloque_sin_iva(bloque, incluir_opcionales=False):
    return sum(precio_equipamiento_sin_iva(e) for e in EQUIPAMIENTO
               if e['bloque_capex'] == bloque and (incluir_opcionales or not e['opcional']))


def plazo_critico_semanas():
    """El plazo de entrega más largo de lo NO opcional: es el que mueve la
    fecha de apertura si se pide tarde (libro 7)."""
    return max(e['plazo_semanas'] for e in EQUIPAMIENTO if not e['opcional'])


# ==========================================================================
# 8. CAPEX
# ==========================================================================
#: Los tres escenarios de obra del caso publicado de La Hostelera, sobre el
#: MISMO local de referencia de 90 m² que usa La Clara (PS-85a/b/c). Por eso
#: casan sin retoques: con 110 m² el escenario se iba a unos 134.000 € y  LN-OK
#: dejaba de estar por debajo del caso publicado (D22).
ESCENARIOS_OBRA = {
    'Bajo':  (600.0, 54000.0, 'PS-85a'),
    'Medio': (900.0, 81000.0, 'PS-85b'),
    'Alto':  (1200.0, 108000.0, 'PS-85c'),
}
ESCENARIO_OBRA_BASE = 'Medio'

#: Los tres niveles de equipamiento del mismo escenario publicado (PS-85d).
#: Se muestran como CONTRASTE de la dotación tipo que construye el libro 7,
#: nunca como la dotación de La Clara.
NIVELES_EQUIPAMIENTO_PUBLICADOS = (15000.0, 29000.0, 46000.0, 'PS-85d')

#: CAPEX partida a partida. `base_iva` = base del importe; `tipo_iva` = tipo que
#: soporta la partida. Toda partida sin id lleva 'supuesto'.
CAPEX = [
    # (bloque, partida, importe, base_iva, tipo_iva, fuente, nota)
    ('Obra civil e instalaciones', 'Obra civil, escenario medio (900 €/m² × 90 m²)',
     81000.0, 'sin IVA', 0.21, 'PS-85b',
     'Escenario de referencia. Los otros dos, en `ESCENARIOS_OBRA`.'),
    ('Equipamiento de obrador', 'Equipamiento de obrador (dotación de La Clara)',
     None, 'sin IVA', 0.21, 'PS-72 + PS-78 + PS-79 + PS-81 + supuesto',
     'Se calcula desde EQUIPAMIENTO: `equipamiento_bloque_sin_iva()`.'),
    ('Tienda y vitrina', 'Tienda y vitrina (dotación de La Clara)',
     None, 'sin IVA', 0.21, 'PS-76 + PS-77 + supuesto',
     'Se calcula desde EQUIPAMIENTO.'),
    ('Licencias y proyecto técnico', 'Proyecto técnico visado',
     5000.0, 'sin IVA', 0.21, 'PS-85e', ''),
    ('Licencias y proyecto técnico', 'Asesoramiento profesional',
     1000.0, 'sin IVA', 0.21, 'PS-85f', ''),
    ('Licencias y proyecto técnico', 'Tasas municipales de licencia de actividad',
     1800.0, 'sin IVA', 0.00, 'supuesto',
     'Las tasas municipales no llevan IVA, y su importe cambia en cada ayuntamiento: '
     'es el número que hay que ir a buscar, no copiar (PA-05).'),
    ('Licencias y proyecto técnico', 'Comunicación o declaración responsable al registro autonómico',
     120.0, 'sin IVA', 0.00, 'PA-04 + supuesto',
     'No es una licencia y NO habilita para abrir: es un trámite de información que se '
     'presenta al iniciar la actividad (PA-04). El importe es supuesto y en varias CCAA '
     'es gratuito.'),
    ('Fianza y garantías', 'Fianza de arrendamiento (2 meses)',
     2400.0, 'sin IVA', 0.00, 'supuesto',
     'La fianza no es un gasto: es un depósito que se recupera. Va en el CAPEX porque '
     'hay que tenerla el día de la firma.'),
    ('Packaging inicial', 'Primer pedido de packaging, bolsas, cajas y etiquetas',
     2500.0, 'sin IVA', 0.21, 'supuesto',
     'Empieza con el mínimo del proveedor: el packaging personalizado obliga a pedidos '
     'grandes y es dinero parado en el almacén.'),
    ('Marketing de apertura', 'Marketing de apertura',
     5000.0, 'sin IVA', 0.21, 'PS-85g', ''),
    ('Fondo de maniobra', 'Colchón de tesorería (meses de gastos fijos)',
     None, 'sin IVA', 0.00, 'supuesto',
     'Se calcula: `meses_colchon_fondo_maniobra` × gastos fijos mensuales.'),
]

#: Traspasos reales para la hoja «Traspaso vs Obra Nueva» del libro 2. Son
#: precios PEDIDOS en un anuncio, NO precios pagados, y la tabla lo dice.
TRASPASOS = [
    # (ciudad o zona, tipo, m², precio pedido, renta mensual o None, fuente)
    ('Barcelona - Gràcia', 'Pastelería-repostería', 85, 43000.0, 1250.0, 'PS-69'),
    ('Barcelona - Poblenou', 'Pastelería take away', 69, 80000.0, 850.0, 'PS-69'),
    ('Barcelona - Sant Antoni', 'Obrador sin venta al público', 80, 25000.0, 1050.0, 'PS-69'),
    ('Barcelona - Pg. Maragall', 'Panadería-pastelería', 63, 18000.0, 1300.0, 'PS-69'),
    ('Barcelona - Sant Andreu', 'Pastelería artesanal', 63, 19000.0, 1300.0, 'PS-69'),
    ('Sevilla', 'Pastelería', None, 6000.0, None, 'PS-70'),
    ('Valencia', 'Despacho de pan', None, 15500.0, None, 'PS-70'),
    ('Valencia - Benimaclet', 'Pastelería', None, 18000.0, None, 'PS-70'),
    ('Madrid', 'Obrador pequeño', None, 20000.0, None, 'PS-70'),
    ('Madrid', 'Pastelería sin obrador, más de 25 años', None, 19500.0, None, 'PS-70'),
    ('Almería', 'Repostería creativa', None, 25000.0, None, 'PS-70'),
    ('Barcelona', 'Pastelería', None, 50000.0, None, 'PS-70'),
    ('Barcelona', 'Pastelería por jubilación', None, 75000.0, None, 'PS-70'),
    ('Gran Canaria', 'Pastelería', None, 65000.0, None, 'PS-70'),
    ('Lleida', 'Pastelería-cafetería, más de 36 años', None, 100000.0, None, 'PS-70'),
]
NOTA_TRASPASOS = ('Son precios PEDIDOS en anuncios de Milanuncios y negociosenventa.es '
                  'leídos el 10-09-2026, no precios pagados, y ninguno viene con su cuenta '
                  'de resultados. Sirven para ver la horquilla y para negociar, no para '
                  'valorar. La renta sólo consta en los cinco de Barcelona (PS-69).')
HORIZONTE_COMPARACION_ANIOS = 5
FUENTE_HORIZONTE = 'supuesto'


# ==========================================================================
# 9. GASTOS FIJOS Y ECONOMÍA DEL AÑO DE CRUCERO
# ==========================================================================
def coste_empresa_anual_persona(pid):
    """Bruto de convenio × 15 pagas × jornada × (1 + SS). Es el salto que más
    sorprende al lector (cap. 13): del bruto al coste empresa hay un 33 %."""
    for p in PLANTILLA:
        if p[0] != pid:
            continue
        bruto_mes = CONVENIO[p[3] - 1][2]
        return bruto_mes * P('pagas_convenio') * p[2] * (1.0 + P('ss_empresa'))
    raise KeyError(pid)


def coste_personal_anual():
    return sum(coste_empresa_anual_persona(p[0]) for p in PLANTILLA)


#: Gastos fijos mensuales del año de crucero. Todo supuesto salvo el personal,
#: que sale del convenio (PA-33) y del parámetro de SS de la familia.
#:
#: La RETRIBUCIÓN DEL PROPIETARIO va como renglón propio (SPEC cap. 18) y NO
#: está dentro de la plantilla de 5 personas: es la única forma de que la
#: rentabilidad publicada signifique algo. Un negocio que sólo es rentable
#: porque su dueño no cobra no es rentable.
GASTOS_FIJOS_MENSUALES = [
    # (partida, importe mensual, fuente, nota)
    ('Personal (coste empresa con SS)', None, 'PA-33 + motor.PARAMETROS[ss_empresa]',
     'Se calcula desde PLANTILLA y CONVENIO: 5 personas, 3,5 jornadas, 15 pagas.'),
    ('Retribución del propietario (incluida la cuota de autónomos)', 2400.0, 'supuesto',
     'Renglón propio (cap. 18). Si el dueño está en el obrador, su trabajo tiene un '
     'coste aunque no se lo pague a fin de mes.'),
    ('Alquiler del local', 1200.0, 'supuesto', 'Ver `NEGOCIO[renta_mensual]`.'),
    ('Suministros (electricidad, gas y agua)', 1450.0, 'supuesto',
     'Con 62 kW instalados y frío 24 horas, es la segunda partida del negocio. No se '
     'estima: se pide la simulación a la comercializadora con la potencia del proyecto.'),
    ('Seguros', 120.0, 'supuesto',
     'Responsabilidad civil y continente. El de RC no está verificado como obligatorio: '
     'depende de la CCAA (PA-41, NO VERIFICADO).'),
    ('Gestoría y asesoría', 220.0, 'supuesto', ''),
    ('Software, TPV y pasarela de cobro', 60.0, 'supuesto',
     'Con Verifactu en el horizonte (PA-37), esta cuota deja de ser opcional.'),
    ('Telefonía e internet', 55.0, 'supuesto', ''),
    ('Limpieza y consumibles', 180.0, 'supuesto', ''),
    ('Mantenimiento de equipos', 150.0, 'supuesto',
     'Si hay horno de gas, súmale la inspección periódica obligatoria cada 5 años, que '
     'se te repercute (PA-08).'),
    ('Publicidad y redes', 200.0, 'supuesto', ''),
    ('Otros gastos de estructura', 150.0, 'supuesto', ''),
    ('Amortización del inmovilizado', None, 'supuesto',
     'CAPEX amortizable / años de amortización. Sin ella, la rentabilidad publicada es '
     'mentira: los hornos se gastan.'),
    ('Gastos financieros del préstamo', None, 'supuesto',
     'Intereses del año 1 del préstamo de `FINANCIACION`.'),
]
ANIOS_AMORTIZACION = 10
FUENTE_AMORTIZACION = 'supuesto'


# ==========================================================================
# 10. FINANCIACIÓN
# ==========================================================================
FINANCIACION = {
    'principal': 60000.0,
    'tipo_nominal': 0.062,
    'plazo_meses': 84,
    'carencia_meses': 6,
    'fuente': 'supuesto',
    'nota': ('Todo supuesto: las condiciones las pone tu banco y dependen de la garantía. '
             'La carencia de 6 meses es la que hace que el préstamo no se coma la caja '
             'justo en la rampa de arranque, y es lo primero que hay que negociar. '
             'Durante la carencia sólo se pagan intereses.'),
}


def intereses_anio_1():
    """Intereses del año 1, con carencia de principal: durante la carencia se
    paga interés sobre el principal íntegro; después, sobre un saldo que baja
    en línea recta. Aproximación deliberada y declarada: el cuadro de
    amortización exacto lo construye el libro 5, no este fichero."""
    f = FINANCIACION
    i_mes = f['tipo_nominal'] / 12.0
    saldo = f['principal']
    cuota_principal = f['principal'] / float(f['plazo_meses'] - f['carencia_meses'])
    total = 0.0
    for mes in range(12):
        total += saldo * i_mes
        if mes >= f['carencia_meses']:
            saldo -= cuota_principal
    return total


# ==========================================================================
# 11. PROVEEDORES VERIFICADOS
# ==========================================================================
#: SÓLO los 9 con URL comprobada. Los 22 restantes del research NO se publican
#: (SPEC cap. 11). El orden es el de la SPEC.
PROVEEDORES = [
    ('Sosa Ingredients', 'Ingredientes premium y técnicos', 'https://www.sosa.cat/', 'PS-87',
     'Fundada en Cataluña en 1967, presente en más de 80 países.'),
    ('Puratos', 'Masas madre, mejorantes, mixes, rellenos y chocolate',
     'https://www.puratos.com/products', 'PS-88', ''),
    ('Barry Callebaut', 'Chocolate y coberturas', 'https://www.barry-callebaut.com/', 'PS-89',
     'Marcas Callebaut, Cacao Barry y Chocovic.'),
    ('Valrhona', 'Chocolate premium y formación', 'https://www.valrhona.com/', 'PS-90',
     'Distribuye la gama Sosa como marca socia.'),
    ('Debic (FrieslandCampina)', 'Mantequilla y nata profesional', 'https://www.debic.com/',
     'PS-91', 'Mantequillas de punto de fusión fijo para hojaldre y bollería.'),
    ('Elle & Vire Professionnel', 'Mantequilla de laminado', 'https://www.elle-et-vire.com/',
     'PS-92', 'Mantequilla seca de 84 % de materia grasa para hojaldre.'),
    ('Ylla 1878', 'Harinas profesionales', 'https://www.ylla1878.com/es/harinas-profesionales/',
     'PS-93', 'Panadería, pastelería, bollería, churrería y pizzería.'),
    ('Farinera Coromina', 'Harinas especiales', 'https://www.farineracoromina.com/', 'PS-94',
     'Fundada en 1897 en Girona. Península, Baleares, Canarias y sur de Francia.'),
    ('Cospan', 'Distribución de materias primas', 'https://cospan.es/', 'PS-95', ''),
]
NOTA_PROVEEDORES = ('Nueve proveedores con URL comprobada el 10-09-2026. El research '
                    'recogió otros 22 sin verificar y NO se publican: un directorio con '
                    'un enlace roto vale menos que uno corto. Directorio del grupo: '
                    'hosply.pro (TLS comprobado el 10-09-2026).')
HOSPLY_URL = ('https://hosply.pro/?utm_source=guia-pasteleria-obrador&utm_medium=producto'
              '&utm_campaign=cap11-proveedores')


# ==========================================================================
# 12. LOS SEIS PICOS DEL AÑO
# ==========================================================================
#: Los seis del `BONUS-02-calendario-anual-tareas.xlsx` del kit, para que el
#: lector reconozca el calendario. Frontera R5: el kit pone las FECHAS y el
#: qué; la guía pone los EUROS y el si aguantas.
#:
#: `factor_obrador` es el multiplicador de piezas/día del obrador entero
#: durante la campaña. PS-41 lo mide en un obrador real (Pastelerías Pomar):
#: ensaimadas de 25-30/día a 150-200/día y pastelería individual de 50-60 a
#: 500-600, es decir un factor de 5 a 10 en el pico gordo, no de 1,5. Los seis
#: factores de aquí son SUPUESTOS que se mueven dentro de ese marco, con el
#: 6,0 de Reyes como el único que llega a la zona de PS-41.
PICOS = [
    {
        'nombre': 'Reyes',
        'fechas': '2 a 6 de enero',
        'mes': 1,
        'dias_campana': 5,
        'producto_estrella': 'Roscón de Reyes',
        'uds_dia_normal': 0,
        'uds_dia_pico': 420,
        'factor_obrador': 6.0,
        'refuerzo_personas': 3,
        'refuerzo_horas_persona': 40,
        'antelacion_compra_semanas': 6,
        'fuente_factor': 'PS-41 + supuesto',
        'fuente_uds': 'supuesto',
        'nota': ('El pico que decide el año. Referencias de escala, nunca de precio ni de '
                 'cuota: PS-35 (unos 30 millones de roscones en España en la campaña '
                 '2025/26), PS-36 (más de 2,9 millones en la Comunidad de Madrid) y '
                 'PS-38 (El Corte Inglés 850.000, Viena Capellanes 72.000). PS-46: el '
                 'supermercado entra con roscones premiados a 9 €. El roscón relleno de '
                 'nata arrastra los 4 °C de la fila 9 y las 24 h del art. 9.3 justo el '
                 'día de más producción: eso limita la producción tanto como el horno.'),
    },
    {
        'nombre': 'San Valentín',
        'fechas': '13 y 14 de febrero',
        'mes': 2,
        'dias_campana': 2,
        'producto_estrella': 'Macarons de frambuesa',
        'uds_dia_normal': 95,
        'uds_dia_pico': 260,
        'factor_obrador': 1.8,
        'refuerzo_personas': 0,
        'refuerzo_horas_persona': 0,
        'antelacion_compra_semanas': 3,
        'fuente_factor': 'supuesto',
        'fuente_uds': 'supuesto',
        'nota': ('Campaña de dos días y de ticket alto, no de volumen: se gana con cajas '
                 'y presentación, no con más horno. En el kit, la producción especial de '
                 'esta fecha son tartas corazón, bombones y macarons.'),
    },
    {
        'nombre': 'Día del Padre y de la Madre',
        'fechas': '19 de marzo y primer domingo de mayo',
        'mes': 3,
        'dias_campana': 4,
        'producto_estrella': 'Tarta de chocolate 70 %',
        'uds_dia_normal': 16,
        'uds_dia_pico': 96,
        'factor_obrador': 1.9,
        'refuerzo_personas': 1,
        'refuerzo_horas_persona': 16,
        'antelacion_compra_semanas': 3,
        'fuente_factor': 'supuesto',
        'fuente_uds': 'supuesto',
        'nota': ('Dos fechas con el mismo patrón de trabajo -tarta con dedicatoria, por '
                 'encargo- y por eso van juntas como una sola campaña operativa. El kit '
                 'las separa en su calendario porque a él le importan las fechas; a la '
                 'guía le importa la carga de obrador.'),
    },
    {
        'nombre': 'Semana Santa',
        'fechas': 'del Domingo de Ramos al Domingo de Resurrección',
        'mes': 4,
        'dias_campana': 8,
        'producto_estrella': 'Torrijas',
        'uds_dia_normal': 0,
        'uds_dia_pico': 240,
        'factor_obrador': 2.4,
        'refuerzo_personas': 1,
        'refuerzo_horas_persona': 40,
        'antelacion_compra_semanas': 4,
        'fuente_factor': 'supuesto',
        'fuente_uds': 'supuesto',
        'nota': ('Ocho días seguidos de producción extra, que es más agotador que los '
                 'cinco de Reyes aunque el pico sea menor. Torrijas y monas a la vez: una '
                 'necesita freidora y frío, la otra horno y chocolate.'),
    },
    {
        'nombre': 'Comuniones',
        'fechas': 'de mediados de abril a mediados de junio',
        'mes': 5,
        'dias_campana': 20,
        'producto_estrella': 'Tarta de nata y fresas',
        'uds_dia_normal': 10,
        'uds_dia_pico': 34,
        'factor_obrador': 1.6,
        'refuerzo_personas': 1,
        'refuerzo_horas_persona': 60,
        'antelacion_compra_semanas': 5,
        'fuente_factor': 'supuesto',
        'fuente_uds': 'supuesto',
        'nota': ('No es un pico, es una MESETA de dos meses, y por eso se aguanta con '
                 'plantilla y no con horas extra. Todo va por encargo: anticipo, '
                 'calendario de entrega y riesgo de anulación (cap. 16). La herramienta '
                 'de gestión del encargo es el 11-control-encargos.xlsx del kit, que la '
                 'guía no rehace (R2).'),
    },
    {
        'nombre': 'Todos los Santos',
        'fechas': '30 y 31 de octubre y 1 de noviembre',
        'mes': 11,
        'dias_campana': 3,
        'producto_estrella': 'Buñuelos de viento',
        'uds_dia_normal': 0,
        'uds_dia_pico': 520,
        'factor_obrador': 2.6,
        'refuerzo_personas': 2,
        'refuerzo_horas_persona': 24,
        'antelacion_compra_semanas': 4,
        'fuente_factor': 'supuesto',
        'fuente_uds': 'supuesto',
        'nota': ('Tres días con tres referencias que sólo se hacen ahora: buñuelos, huesos '
                 'de santo y panellets. Los buñuelos van rellenos (4 °C y 24 h) y los '
                 'otros dos son estables a temperatura ambiente: por eso los buñuelos se '
                 'hacen el mismo día y los huesos de santo se pueden adelantar. Ese '
                 'detalle legal ES la planificación de la campaña.'),
    },
]

#: Coeficiente de actividad de cada mes sobre el mes medio. MEDIA = 1,000
#: exacta. Todo supuesto, construido con la forma que dan los 6 picos: enero
#: (Reyes), abril y mayo (Semana Santa, Día de la Madre y comuniones),
#: noviembre (Todos los Santos y arranque de Navidad) y diciembre (Navidad)
#: por encima; agosto muy por debajo porque La Clara cierra dos semanas.
#:
#: Febrero y marzo quedan por debajo de 1,00 aunque tengan pico: San Valentín
#: son DOS días y el Día del Padre uno, y ninguna campaña de esa longitud
#: levanta un mes entero (febrero, además, tiene 28 días). Sólo los picos de
#: 2,0x o más -Reyes, Semana Santa y Todos los Santos- mueven el coeficiente
#: de su mes, y eso es exactamente lo que comprueba `comprobar()`.
ESTACIONALIDAD_MENSUAL = (1.18, 0.94, 0.98, 1.05, 1.08, 0.98,
                          0.86, 0.68, 0.92, 0.96, 1.09, 1.28)
FUENTE_ESTACIONALIDAD = 'supuesto'


def estacionalidad_pesos():
    """Los mismos doce coeficientes expresados como PESOS que suman 1,000, que
    es como los pide el molde `planes-v2_0` del libro 5."""
    return tuple(c / 12.0 for c in ESTACIONALIDAD_MENSUAL)


#: Rampa de arranque, con el patrón del `plan-negocio-panaderia`
#: (`planes-v2_0/grupo_a.py`: `rampa_mes1` = 0,55 y `meses_rampa` = 6, subida
#: en línea recta hasta el 100 %). Un local que abre no factura desde el primer
#: día lo que factura a los seis meses, y proyectar el año 1 a velocidad de
#: crucero es el error que más planes de negocio tumba.
RAMPA = {'mes1': 0.55, 'meses': 6, 'fuente': 'planes-v2_0/grupo_a.py + supuesto'}


def rampa_mensual():
    """Doce coeficientes de rampa: sube en línea recta desde `mes1` hasta 1,00
    en `meses` meses y se queda en 1,00."""
    m1, n = RAMPA['mes1'], RAMPA['meses']
    return tuple(min(1.0, m1 + (1.0 - m1) * i / float(max(1, n - 1))) for i in range(12))


# ==========================================================================
# 13. CANALES
# ==========================================================================
#: Todo supuesto salvo la referencia de PS-53, que es la ÚNICA cifra publicada
#: de estructura de cobro de una pastelería española: 95 % de venta directa al
#: cliente y 5 % de venta a crédito a 30-60 días (Pastelerías Pomar). Aquí el
#: B2B es justo ese 5 %, y por eso el reparto no es un invento redondo.
CANALES = [
    {'canal': 'Mostrador', 'ventas_pct': 78.0, 'margen_bruto': 0.68,
     'coste_servir_pct': 0.0, 'comision_plataforma': 0.0, 'cobro_dias': 0,
     'fuente': 'supuesto',
     'nota': 'Cobro al contado. Es el canal que paga el alquiler.'},
    {'canal': 'Encargos', 'ventas_pct': 14.0, 'margen_bruto': 0.70,
     'coste_servir_pct': 0.02, 'comision_plataforma': 0.0, 'cobro_dias': 0,
     'fuente': 'supuesto',
     'nota': ('Anticipo del 30 % al reservar (supuesto): es lo que convierte una '
              'anulación en una molestia y no en una pérdida. Mejor margen porque el '
              'producto se hace contra pedido y la merma es cero.')},
    {'canal': 'B2B (cafeterías y restaurantes de la zona)', 'ventas_pct': 5.0,
     'margen_bruto': 0.52, 'coste_servir_pct': 0.03, 'comision_plataforma': 0.0,
     'cobro_dias': 45, 'fuente': 'PS-53 + supuesto',
     'nota': ('El 5 % sale de PS-53 (venta a crédito a 30-60 días). Peor margen y cobro '
              'a 45 días: financias tú. Y ojo, es el canal que puede meterte en el '
              'art. 3 del RD 1021/2022 si dejas de ser marginal, localizado o restringido '
              '(PA-02): basta con servir a UN solo cliente inscrito en el RGSEAA para '
              'perder el requisito de «restringido».')},
    {'canal': 'Online y envío', 'ventas_pct': 3.0, 'margen_bruto': 0.60,
     'coste_servir_pct': 0.09, 'comision_plataforma': 0.0, 'cobro_dias': 0,
     'fuente': 'supuesto',
     'nota': ('Comisión 0 % porque es web propia. Si vendes por marketplace, mete su '
              'comisión en la celda verde: es el número que decide si el canal existe. '
              'La venta a distancia YA está dentro de la definición de minorista '
              '(PA-01b y PA-27): vender online no te saca de este régimen. Y hay '
              'información obligatoria ANTES de la compra (PA-28).')},
]


# ==========================================================================
# 14. CHECKLIST LEGAL POR FASES (libro 6)
# ==========================================================================
#: Seis fases, F1 a F6. Cada ítem: trámite · responsable · plazo orientativo en
#: días · coste (con id o supuesto) · si cambia por CCAA.
#:
#: Las CCAA de ejemplo son CUATRO -Madrid, Cataluña, Andalucía y C. Valenciana-
#: y van DECLARADAS COMO EJEMPLOS (D27). Las 17 multiplican el mantenimiento
#: justo cuando se están adaptando al RD 1021/2022: Madrid legisló en 2026 y la
#: Comunitat Valenciana en 2025.
CCAA_EJEMPLO = ('Madrid', 'Cataluña', 'Andalucía', 'Comunitat Valenciana')

FASES_CHECKLIST = {
    'F1': 'Antes de firmar nada: viabilidad del local',
    'F2': 'Sociedad, altas y proyecto técnico',
    'F3': 'Licencia de actividad',
    'F4': 'Obra, equipamiento e instalaciones',
    'F5': 'Sanidad, APPCC y formación',
    'F6': 'Apertura: fiscal, laboral y comercial',
}

CHECKLIST_LEGAL = [
    # (fase, trámite, responsable, plazo en días, coste, fuente del coste, cambia por CCAA, nota)
    ('F1', 'Comprobar en el planeamiento si el uso admite obrador (industria artesanal) '
           'o sólo comercio', 'Promotor', 10, None, 'PA-06',
     False,
     'PA-06 NO está verificado: la clasificación urbanística de un obrador sólo tiene '
     'fuente comercial. Va como PREGUNTA al ayuntamiento, nunca como afirmación.'),
    ('F1', 'Confirmar que existe salida de humos hasta cubierta y quién la autoriza',
     'Promotor', 15, None, 'PS-86c + PA-07', False,
     'PS-86c: hasta cubierta y 1 m por encima de la cumbrera. Ojo: PA-07 corrige el '
     'research -el DB-HS 3 del CTE NO regula la ventilación de un local comercial, sólo '
     'viviendas y garajes-, así que lo que manda es el RITE más la ordenanza municipal. '
     'La comunidad de propietarios es el riesgo real, y no es normativo: es una junta.'),
    ('F1', 'Pedir por escrito a la comunidad de propietarios la autorización del conducto',
     'Promotor', 30, None, 'supuesto', False,
     'El plazo depende de cuándo se reúna la junta. Es la variable que menos controlas.'),
    ('F1', 'Comprobar potencia eléctrica disponible y coste del aumento',
     'Promotor', 15, None, 'PS-86a', False,
     'PS-86a: 20-80 kW SÓLO para los hornos.'),
    ('F1', 'Verificar que caben las 7 zonas obligatorias con marcha adelante',
     'Promotor', 5, None, 'PS-86d', False, ''),

    ('F2', 'Constituir la sociedad o darse de alta como autónomo', 'Promotor', 20, 600.0,
     'supuesto', False,
     'Importa para Verifactu: sociedad, 1-ene-2027; autónomo, 1-jul-2027 (PA-37).'),
    ('F2', 'Alta censal (modelo 036) y epígrafe de IAE', 'Gestoría', 3, None, 'PA-38',
     False,
     'PA-38 corrige el research: los epígrafes son 419.1, 419.2, 644.1, 644.2 y 644.3 del '
     'RDLeg 1175/1990 y NO se copian de la guía de panadería sin mirar cuál te toca. '
     'PA-38b: hay exención de cuota por cifra de negocio (art. 82.1.b y c del TRLRHL).'),
    ('F2', 'Alta en el régimen correspondiente de la Seguridad Social', 'Gestoría', 3,
     None, 'supuesto', False, ''),
    ('F2', 'Encargar el proyecto técnico visado', 'Ingeniería', 30, 5000.0, 'PS-85e', False,
     'Es el documento del que cuelga todo lo demás: sin él no hay licencia ni obra.'),
    ('F2', 'Firmar el arrendamiento y depositar la fianza', 'Promotor', 5, 2400.0,
     'supuesto', True,
     'El depósito de la fianza se hace en el organismo de vivienda de tu CCAA y el plazo '
     'cambia en cada una.'),

    ('F3', 'Presentar la declaración responsable o solicitar la licencia de actividad',
     'Ingeniería', 45, 1800.0, 'PA-05 + supuesto', True,
     'PA-05 NO está verificado (Directiva 2006/123/CE, Ley 20/2013, art. 69 de la Ley '
     '39/2015 y la ordenanza municipal). El régimen general es de declaración responsable, '
     'pero el procedimiento y la tasa los pone tu ayuntamiento: la guía entrega la '
     'plantilla para que rellenes el tuyo, no una afirmación nacional.'),
    ('F3', 'Solicitar la licencia de obra menor o mayor según el proyecto',
     'Ingeniería', 30, None, 'supuesto', True, ''),
    ('F3', 'Tramitar el rótulo y la ocupación de vía pública si la hay',
     'Promotor', 20, None, 'supuesto', True, ''),

    ('F4', 'Ejecutar la obra civil e instalaciones', 'Constructora', 60, 81000.0,
     'PS-85b', False, 'Escenario medio: 900 €/m² × 90 m².'),
    ('F4', 'Pedir el equipamiento con el plazo de entrega por escrito',
     'Promotor', 5, None, 'supuesto', False,
     'El plazo de entrega es lo que mueve la fecha de apertura, no el precio. Pídelo por '
     'escrito y mételo en el libro 7.'),
    ('F4', 'Certificado de instalación de gas y puesta en servicio (sólo si hay horno de gas)',
     'Instalador habilitado', 15, None, 'PA-08', False,
     'PA-08: con gas asumes certificado de empresa habilitada, puesta en servicio por el '
     'distribuidor e inspección periódica obligatoria cada 5 años, que se te repercute. '
     'Por debajo de 70 kW la inspección INCLUYE los aparatos, y mira la ventilación y el '
     'volumen mínimo del local.'),
    ('F4', 'Boletín eléctrico y legalización de la instalación',
     'Instalador habilitado', 10, None, 'supuesto', False, ''),
    ('F4', 'Comprobar accesibilidad del local', 'Ingeniería', 10, None, 'PA-40', False,
     'PA-40: RD 193/2023, arts. 17 y 25 y D.F. sexta. Verificado letra a letra el '
     '10-09-2026; mira el calendario dos veces.'),

    ('F5', 'Presentar la comunicación o declaración responsable al registro sanitario '
           'de tu CCAA', 'Promotor', 5, 120.0, 'PA-01 + PA-04', True,
     'NO es el RGSEAA: una pastelería que vende al consumidor final está EXCLUIDA del '
     'registro estatal (PA-01). Es un trámite autonómico que NO habilita para abrir. En '
     'Madrid, Decreto 26/2026, en vigor desde el 28-03-2026: se presenta a la vez que '
     'inicias la actividad, no antes, y las que ya estaban abiertas tienen hasta el '
     '28-03-2027 (PA-04).'),
    ('F5', 'Comprobar si tu B2B te obliga a inscribirte en el RGSEAA', 'Promotor', 5,
     None, 'PA-02', False,
     'Sólo aplica si suministras a otros comercios minoristas DE DISTINTA TITULARIDAD. Si '
     'entras, las tres condiciones son acumulativas -marginal Y localizado Y restringido- '
     'y dentro de «marginal» hay dos vías ALTERNATIVAS: 25 % del volumen anual o 500 kg a '
     'la semana en total. Lo de central y sucursales va aparte: son una sola unidad '
     'comercial, pero cada una se inscribe por separado (PA-03).'),
    ('F5', 'Redactar el plan de APPCC y designar por su nombre a la persona responsable',
     'Promotor', 20, 800.0, 'PA-10 + supuesto', False,
     'PA-10: el APPCC simplificado es legal y está escrito (art. 20 del RD 1021/2022). '
     'Las guías sectoriales son voluntarias.'),
    ('F5', 'Formación de manipuladores y registro de formación por persona',
     'Promotor', 10, 240.0, 'PA-11 + supuesto', False,
     'PA-11: el «carnet de manipulador» NO existe desde 2010. Lo que hay que tener es un '
     'REGISTRO de formación, y es responsabilidad de la empresa.'),
    ('F5', 'Matriz de alérgenos de vitrina publicada antes de abrir', 'Promotor', 5,
     None, 'PA-21', False,
     'R3: la matriz de vitrina la resuelve el 12-control-alergenos-vitrina.xlsx del kit y '
     'la guía NO la rehace. Lo que sí construye la guía es la de OBRADOR: materias primas '
     'por alérgeno y orden de elaboración, que es otra cosa (PA-22).'),
    ('F5', 'Fichar el sistema de registro de jornada', 'Gestoría', 5, None, 'PA-34', False,
     'PA-34: hoy vale papel o una hoja de cálculo, conservados 4 años. Hay una reforma de '
     'registro horario digital EN TRAMITACIÓN que lo prohibiría: comprueba el estado '
     'antes de comprar un sistema, y no des ninguna fecha por cierta.'),

    ('F6', 'Contratar al equipo con el convenio y el grupo correctos', 'Gestoría', 15,
     None, 'PA-33', True,
     'PA-33: el convenio es PROVINCIAL o autonómico. El de Madrid tiene 6 grupos y '
     '15 pagas. Los de Barcelona, Valencia y Sevilla NO están verificados: busca el tuyo. '
     'Y si abres pastelería-cafetería puede caerte el de hostelería, o convivir los dos '
     'por áreas funcionales: eso no está resuelto y es de dinero.'),
    ('F6', 'Comprobar que ningún grupo del convenio queda por debajo del SMI',
     'Gestoría', 2, None, 'PA-32', False,
     'PA-32: SMI 2026 de 1.221 €/mes en 14 pagas, 17.094 €/año como referencia ANUAL en '
     'cómputo global. En Madrid el grupo más bajo del convenio ya lo supera con '
     '17.886,30 €: manda el convenio. Y las dos cosas caducan el 31-12-2026.'),
    ('F6', 'Contratar el TPV y verificar que cumple Verifactu', 'Promotor', 5, None,
     'PA-37', False,
     'PA-37: 1-ene-2027 para sociedades y 1-jul-2027 para autónomos. NO es 2026. Pero el '
     'software que compres hoy ya debe estar adaptado.'),
    ('F6', 'Revisar las obligaciones de envases y de desperdicio alimentario',
     'Promotor', 5, None, 'PA-30 + PA-31', False,
     'PA-30: desde el 1-ene-2027, si tienes menos de 300 m², una referencia reutilizable '
     'de bebida. Y el art. 9.3 del RD 1055/2022 obliga a ACEPTAR el recipiente del cliente '
     'si vendes a granel: no es opcional. PA-31 y D15: de la Ley 1/2025 estás exento del '
     'PLAN del art. 6.4 si no pasas de 1.300 m², pero te siguen obligando el 6.2, el 6.3 y '
     'el 6.5; sólo si eres microempresa (6.6) quedas fuera del artículo entero. Nunca '
     'escribas «tu pastelería está exenta del plan» a secas.'),
    ('F6', 'Decidir el horario y publicarlo', 'Promotor', 2, None, 'PA-39', True,
     'PA-39: si la pastelería es la actividad PRINCIPAL tiene libertad horaria por ley '
     'estatal. No hay que pedir permiso para abrir en domingo. Los horarios generales sí '
     'los fija cada CCAA.'),
    ('F6', 'Contratar el seguro de responsabilidad civil', 'Promotor', 5, 1440.0,
     'PA-41 + supuesto', True,
     'PA-41 NO está verificado: si es obligatorio y con qué capital depende de la CCAA.'),
]


# ==========================================================================
# 15. CRONOGRAMA Y RUTA CRÍTICA (hoja absorbida del libro 6, D3)
# ==========================================================================
#: Duraciones en MESES, no en días laborables: el Gantt del libro 6 se calcula
#: con aritmética de índices de mes porque `NETWORKDAYS` está prohibida en toda
#: la familia. Todas las duraciones son SUPUESTOS.
MES_INICIO_PROYECTO = 1     # enero
GANTT = [
    # (id, hito, duración en meses, dependencias)
    ('H1',  'Búsqueda y cribado de local',                                  2.0, ()),
    ('H2',  'Firma del arrendamiento y fianza',                             0.5, ('H1',)),
    ('H3',  'Proyecto técnico visado',                                      1.0, ('H2',)),
    ('H4',  'Licencia de actividad o declaración responsable',              1.5, ('H3',)),
    ('H5',  'Obra civil e instalaciones',                                   2.0, ('H4',)),
    ('H6',  'Pedido y entrega del equipamiento',                            2.5, ('H3',)),
    ('H7',  'Montaje y puesta en marcha del equipamiento',                  0.5, ('H5', 'H6')),
    ('H8',  'Comunicación al registro sanitario autonómico',                0.5, ('H7',)),
    ('H9',  'Formación de manipuladores y plan de APPCC',                   0.5, ('H7',)),
    ('H10', 'Contratación del equipo y altas en Seguridad Social',          0.5, ('H7',)),
    ('H11', 'Pruebas de producción y cierre de la carta de apertura',       0.5, ('H8', 'H9', 'H10')),
    ('H12', 'Apertura',                                                     0.0, ('H11',)),
]
FUENTE_GANTT = 'supuesto'


def ruta_critica():
    """Devuelve (fin en meses, camino crítico, dict de holguras por hito).

    Aritmética de índices de mes, sin funciones de fecha: es lo que después se
    traduce a fórmulas en la hoja «Cronograma y Ruta Crítica» del libro 6.
    """
    dur = dict((h[0], h[2]) for h in GANTT)
    deps = dict((h[0], h[3]) for h in GANTT)
    inicio, fin, previo = {}, {}, {}
    for hid, _n, d, ds in GANTT:
        if not ds:
            inicio[hid], previo[hid] = 0.0, None
        else:
            mejor = max(ds, key=lambda x: fin[x])
            inicio[hid], previo[hid] = fin[mejor], mejor
        fin[hid] = inicio[hid] + d
    # El hito terminal es el que NO tiene sucesores, no el de mayor fin: la
    # apertura dura 0 meses y empata con el hito que la precede, así que un
    # max() a secas devolvía el penúltimo y el camino se quedaba sin «H12».
    con_sucesor = set()
    for _h, _n, _d, ds in GANTT:
        con_sucesor.update(ds)
    terminales = [h[0] for h in GANTT if h[0] not in con_sucesor]
    ultimo = max(terminales, key=lambda h: fin[h])
    camino, cur = [], ultimo
    while cur is not None:
        camino.append(cur)
        cur = previo[cur]
    camino.reverse()
    total = fin[ultimo]
    # Holgura: cuánto puede retrasarse un hito sin mover la apertura.
    holgura = {}
    for hid in dur:
        sucesores = [h for h in deps if hid in deps[h]]
        limite = min([inicio[s] for s in sucesores]) if sucesores else total
        holgura[hid] = round(limite - fin[hid], 2)
    return total, camino, holgura


def mes_apertura_calculado():
    """Mes natural en el que cae la apertura arrancando en `MES_INICIO_PROYECTO`.
    Con 8,5 meses de ruta crítica desde el 1 de enero, la apertura cae a mitad
    de septiembre: fuera de los seis picos y con 3,5 meses de rodaje antes de
    Reyes, que es exactamente lo que pide el cap. 20."""
    total, _camino, _h = ruta_critica()
    return int(MES_INICIO_PROYECTO + total)


# ==========================================================================
# 16. NOTAS LEGALES: nota_legal() y gate_legal()
# ==========================================================================
#: Regla de datos legales de la SPEC §2.2: *cada celda con un dato legal lleva
#: nota «Verificado el 10-09-2026 · norma y artículo · URL»*. Esa nota NO se
#: escribe a mano en ningún constructor: se pide aquí, y aquí se lee del
#: fichero de la verificación legal independiente (D16), que es la fuente de
#: verdad de lo legal.
VERIFICACION_LEGAL_JSON = os.path.join(
    _AUDIT, 'guia-pasteleria-verificacion-legal-2026-09-10.json')
VERIFICACION_LEGAL_MD = os.path.join(
    _AUDIT, 'guia-pasteleria-verificacion-legal-2026-09-10.md')

#: Nombres de campo que puede traer el JSON. Se aceptan varios a propósito: el
#: fichero lo escribe otro agente y lo único que este módulo necesita es la
#: norma con su artículo y la URL. Si mañana cambia el esquema, se añade el
#: nombre aquí y no hay que tocar los ocho constructores.
#: `fuente_titulo` va delante de `norma` a propósito: es el campo que el JSON
#: de la verificación legal usa para la norma CON su artículo
#: («RD 191/2011, art. 2.2, en la redacción dada por...»), que es exactamente
#: lo que tiene que salir en la nota de la celda.
_CAMPOS_NORMA = ('norma_y_articulo', 'norma_articulo', 'fuente_titulo', 'norma',
                 'articulo', 'titulo', 'asunto', 'valor_correcto', 'dato')
_CAMPOS_URL = ('url', 'fuente_url', 'enlace', 'fuente')

_LEGAL_CACHE = {'cargado': False, 'entradas': {}, 'error': None}


def _carga_verificacion_legal():
    """Carga (una vez) el JSON de la verificación legal. Tolerante con la
    forma: lista de entradas con `id`, o dict indexado por id, o dict con la
    lista dentro de una clave. Si el fichero no existe todavía -lo está
    escribiendo otro agente-, no revienta: deja el error anotado."""
    if _LEGAL_CACHE['cargado']:
        return _LEGAL_CACHE
    _LEGAL_CACHE['cargado'] = True
    if not os.path.exists(VERIFICACION_LEGAL_JSON):
        _LEGAL_CACHE['error'] = ('No existe %s. La verificación legal del 10-sep todavía '
                                 'no ha volcado su JSON.' % VERIFICACION_LEGAL_JSON)
        return _LEGAL_CACHE
    try:
        fh = open(VERIFICACION_LEGAL_JSON, 'rb')
        try:
            crudo = json.loads(fh.read().decode('utf-8'))
        finally:
            fh.close()
    except Exception as e:                                    # noqa: BLE001
        _LEGAL_CACHE['error'] = 'No se pudo leer %s: %s' % (VERIFICACION_LEGAL_JSON, e)
        return _LEGAL_CACHE

    filas = []
    if isinstance(crudo, list):
        filas = crudo
    elif isinstance(crudo, dict):
        for clave in ('entradas', 'ids', 'verificaciones', 'items', 'datos'):
            if isinstance(crudo.get(clave), list):
                filas = crudo[clave]
                break
        else:
            for k, v in crudo.items():
                if isinstance(v, dict):
                    v = dict(v)
                    v.setdefault('id', k)
                    filas.append(v)
    for fila in filas:
        if not isinstance(fila, dict):
            continue
        pid = fila.get('id')
        if pid:
            _LEGAL_CACHE['entradas'][str(pid).strip()] = fila
    if not _LEGAL_CACHE['entradas']:
        _LEGAL_CACHE['error'] = ('%s no trae ninguna entrada con `id`.'
                                 % VERIFICACION_LEGAL_JSON)
    return _LEGAL_CACHE


def _primer_campo(fila, campos):
    for c in campos:
        v = fila.get(c)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None


def nota_legal(id_pa):
    """Nota de celda para un dato legal, o `None` si no se puede construir.

    Devuelve: «Verificado el 10-09-2026 · <norma y artículo> · <URL>»

    Devuelve `None` -y no revienta- si el JSON de la verificación legal no
    existe todavía o si el id no está en él. Los constructores llaman antes a
    `gate_legal()`, que es quien aborta: así se puede importar este módulo
    mientras el fichero legal se está escribiendo.
    """
    cache = _carga_verificacion_legal()
    fila = cache['entradas'].get(str(id_pa).strip())
    if not fila:
        return None
    norma = _primer_campo(fila, ('norma_y_articulo', 'norma_articulo', 'fuente_titulo'))
    if not norma:
        n = _primer_campo(fila, ('norma', 'titulo', 'asunto'))
        a = _primer_campo(fila, ('articulo',))
        if n and a:
            norma = '%s, %s' % (n, a)
        else:
            norma = n or a or _primer_campo(fila, ('valor_correcto', 'dato'))
    url = _primer_campo(fila, _CAMPOS_URL)
    if not norma or not url or not url.lower().startswith('http'):
        return None
    # La nota va a una celda de Excel: se recorta el literal largo.
    norma = re.sub(r'\s+', ' ', norma).strip()
    if len(norma) > 220:
        norma = norma[:217].rstrip() + '...'
    return 'Verificado el %s · %s · %s' % (FECHA_VERIFICACION_LEGAL, norma, url)


#: Los ids `PA-*` que citan los libros 4 y 6 según la SPEC §2.2 y §4, más los
#: que este propio juego de datos usa (el IVA de la carta y el pan). Los
#: constructores llaman a `gate_legal(IDS_LEGALES_REQUERIDOS)` antes de
#: escribir una sola nota.
IDS_LEGALES_REQUERIDOS = {
    # --- libro 4: carta de apertura y escandallo -------------------------
    'PA-12': ('Temperaturas: fila 9 del art. 4.1 (producto de pastelería relleno)', 4),
    'PA-13': ('Congelación, descongelación y recongelación (art. 5)', 4),
    'PA-14': ('Huevo y ovoproductos: art. 9 y derogación del RD 1254/1991', 4),
    'PA-15': ('Las 24 h del art. 9.3: qué obliga y qué no', 4),
    'PA-21': ('Los 14 alérgenos en producto no envasado', 4),
    'PA-23': ('«Sin gluten»: umbral analítico de 20 mg/kg', 4),
    'PA-24': ('RD 496/2010, norma de calidad de confitería y pastelería', 4),
    'PA-25': ('RD 308/2019: si la pastelería vende pan', 4),
    'PA-36': ('IVA: el 10 % de la pastelería y la lista cerrada del 4 %', 4),
    'PA-36b': ('IVA del pan: 4 % a todos los productos del RD 308/2019', 4),
    # --- libro 6: checklist legal, licencias y cronograma ----------------
    # PA-05 (declaración responsable frente a licencia previa) NO entra en el
    # gate a propósito: la verificación legal del 10-sep lo deja como NO
    # VERIFICADO -no se abrieron la Directiva 2006/123/CE, la Ley 20/2013 ni el
    # art. 69 de la Ley 39/2015- y el producto lo trata como plantilla para que
    # el lector rellene el procedimiento de SU ayuntamiento, no como afirmación
    # nacional. Exigirle una nota legal sería exigir una fuente que no existe.
    'PA-01': ('La pastelería minorista NO va al RGSEAA', 6),
    'PA-02': ('Cuándo SÍ hay que inscribirse: art. 3 del RD 1021/2022', 6),
    'PA-03': ('Central y sucursales: una unidad comercial, inscripción independiente', 6),
    'PA-04': ('El registro autonómico y el transitorio de Madrid', 6),
    'PA-10': ('APPCC simplificado (art. 20)', 6),
    'PA-11': ('El carnet de manipulador no existe: registro de formación', 6),
    'PA-29': ('Art. 13: obrador en vivienda particular', 6),
    'PA-30': ('Envases: Ley 7/2022 y RD 1055/2022', 6),
    'PA-31': ('Ley 1/2025 de desperdicio alimentario: alcance real del art. 6', 6),
    'PA-32': ('SMI 2026', 6),
    'PA-33': ('Convenio de pastelería de Madrid, revisión 2026', 6),
    'PA-37': ('Verifactu: 1-ene-2027 y 1-jul-2027', 6),
    'PA-38': ('Epígrafes de IAE', 6),
    'PA-39': ('Libertad horaria de la pastelería', 6),
    'PA-40': ('Accesibilidad: RD 193/2023', 6),
}


def gate_legal(ids_requeridos=None, abortar=True):
    """Comprueba que la verificación legal sirve una nota para CADA id que los
    libros van a citar. Si falta alguno, aborta listándolos.

    Los constructores lo llaman ANTES de escribir notas: la alternativa es un
    xlsx publicado con una celda legal sin fuente, que es justo lo que la SPEC
    prohíbe. `abortar=False` devuelve la lista en vez de morir, para que
    `comprobar()` pueda informar sin tumbar el módulo mientras el fichero legal
    se está escribiendo en otro hilo.
    """
    ids = list(ids_requeridos or IDS_LEGALES_REQUERIDOS)
    cache = _carga_verificacion_legal()
    faltan = [i for i in ids if nota_legal(i) is None]
    if not faltan:
        return []
    detalle = []
    for i in faltan:
        para_que = IDS_LEGALES_REQUERIDOS.get(i, ('(sin descripción)', '?'))[0]
        detalle.append('  - %s: %s' % (i, para_que))
    mensaje = ('gate_legal: faltan %d de %d notas legales en %s\n%s'
               % (len(faltan), len(ids), VERIFICACION_LEGAL_JSON, '\n'.join(detalle)))
    if cache['error']:
        mensaje += '\n  Motivo: %s' % cache['error']
        mensaje += ('\n  El .md sí existe (%s): el JSON es lo que falta.'
                    % ('sí' if os.path.exists(VERIFICACION_LEGAL_MD) else 'no'))
    if abortar:
        raise SystemExit(mensaje)
    return faltan


# ==========================================================================
# 17. ECONOMÍA DEL AÑO DE CRUCERO
# ==========================================================================
def iva_medio_carta():
    """Tipo de IVA medio de la carta, ponderado por euros vendidos con IVA. No
    es un tipo legal: es el que hace falta para pasar de caja a ventas netas.
    Existe porque los panes van al 4 % y el resto al 10 % (PA-36 y PA-36b)."""
    con_iva = sum(r['pvp_con_iva'] * r['mix_pct'] for r in CARTA)
    sin_iva = sum(pvp_sin_iva(r) * r['mix_pct'] for r in CARTA)
    return con_iva / sin_iva - 1.0


def ventas_anuales_sin_iva():
    """Ventas del año de crucero, sin IVA. Salen de la CARTA y del tráfico
    supuesto: tickets/día × piezas por ticket × PVP medio ponderado."""
    dia_con_iva = P('tickets_dia_crucero') * ticket_medio_con_iva()
    return dia_con_iva / (1.0 + iva_medio_carta()) * NEGOCIO['dias_apertura_anio']


def piezas_dia_crucero():
    """Piezas al día en velocidad de crucero. Es la entrada del libro 1: el
    equipo que compras tiene que dar esto todos los días, y `factor_obrador`
    de cada pico dice cuánto más tiene que dar en campaña."""
    return P('tickets_dia_crucero') * P('piezas_por_ticket')


def capex_total_sin_iva():
    """CAPEX total, todo en base imponible. Las partidas calculadas (los dos
    bloques de equipamiento y el fondo de maniobra) se resuelven aquí."""
    total = 0.0
    for bloque, _partida, importe, _base, _tipo, _fuente, _nota in CAPEX:
        if importe is not None:
            total += importe
        elif bloque == 'Equipamiento de obrador':
            total += equipamiento_bloque_sin_iva('Equipamiento de obrador')
        elif bloque == 'Tienda y vitrina':
            total += equipamiento_bloque_sin_iva('Tienda y vitrina')
        elif bloque == 'Fondo de maniobra':
            total += P('meses_colchon_fondo_maniobra') * gastos_fijos_mensuales()
    return total


def capex_amortizable_sin_iva():
    """CAPEX que se amortiza: todo menos la fianza (es un depósito), el fondo
    de maniobra (es caja) y el packaging inicial (es existencias)."""
    fuera = ('Fianza y garantías', 'Fondo de maniobra', 'Packaging inicial')
    total = 0.0
    for bloque, _partida, importe, _base, _tipo, _fuente, _nota in CAPEX:
        if bloque in fuera:
            continue
        if importe is not None:
            total += importe
        elif bloque == 'Equipamiento de obrador':
            total += equipamiento_bloque_sin_iva('Equipamiento de obrador')
        elif bloque == 'Tienda y vitrina':
            total += equipamiento_bloque_sin_iva('Tienda y vitrina')
    return total


def iva_soportado_capex():
    """IVA soportado en la inversión. Se recupera vía declaraciones, pero hay
    que ADELANTARLO: es la partida que más sorprende en la hoja «IVA y
    Tesorería» del libro 2."""
    total = 0.0
    for bloque, _partida, importe, _base, tipo, _fuente, _nota in CAPEX:
        if bloque == 'Equipamiento de obrador':
            base = equipamiento_bloque_sin_iva('Equipamiento de obrador') if importe is None else importe
        elif bloque == 'Tienda y vitrina':
            base = equipamiento_bloque_sin_iva('Tienda y vitrina') if importe is None else importe
        elif bloque == 'Fondo de maniobra':
            continue
        else:
            base = importe or 0.0
        total += base * tipo
    return total


_FIJOS_CACHE = {}


def gastos_fijos_mensuales():
    """Gastos fijos de un mes de crucero, con el personal, la retribución del
    propietario, la amortización y los intereses dentro. Sin esos cuatro
    renglones la rentabilidad que publica un plan de negocio no significa nada."""
    if 'v' in _FIJOS_CACHE:
        return _FIJOS_CACHE['v']
    _FIJOS_CACHE['v'] = 0.0     # corta la recursión de capex -> fondo de maniobra
    total = 0.0
    for partida, importe, _fuente, _nota in GASTOS_FIJOS_MENSUALES:
        if importe is not None:
            total += importe
        elif partida.startswith('Personal'):
            total += coste_personal_anual() / 12.0
        elif partida.startswith('Amortización'):
            total += capex_amortizable_sin_iva() / ANIOS_AMORTIZACION / 12.0
        elif partida.startswith('Gastos financieros'):
            total += intereses_anio_1() / 12.0
    _FIJOS_CACHE['v'] = total
    return total


def cuenta_resultados_crucero():
    """P&L simplificado del año de crucero. El libro 5 lo hace bien -mes a mes,
    con estacionalidad, rampa, IVA y servicio de deuda-; esto es la foto anual
    que usan el guion y el bonus 1, y que sirve de gate de coherencia.

    El coste de ventas se calcula con `food_cost_objetivo`, que es la REGLA
    ÚNICA de la casa (D23), no con el food cost de escandallo de la carta. Los
    dos números conviven a propósito y la diferencia está explicada en
    `BRECHA_FOOD_COST`.
    """
    ventas = ventas_anuales_sin_iva()
    coste_ventas = ventas * P('food_cost_objetivo')
    fijos = gastos_fijos_mensuales() * 12.0
    beneficio = ventas - coste_ventas - fijos
    return {
        'ventas_sin_iva': ventas,
        'coste_de_ventas': coste_ventas,
        'margen_bruto': ventas - coste_ventas,
        'gastos_fijos': fijos,
        'beneficio_neto': beneficio,
        'margen_neto': beneficio / ventas,
    }


def punto_muerto_mensual():
    """Facturación mensual sin IVA a la que el beneficio es cero, con la regla
    única de margen (D23)."""
    return gastos_fijos_mensuales() / margen_bruto_objetivo()


#: PS-58 es el ÚNICO par publicado que cuadra con la regla única: 5.000 €/mes
#: de costes fijos dan una facturación de equilibrio de unos 7.200 €/mes, lo
#: que implica un margen bruto del 69,4 %. Se muestra como CONTRASTE de la
#: aritmética, nunca como el punto muerto de La Clara ni como benchmark.
#: El otro par publicado queda fuera de las cifras citables (D23): sus tres
#: escenarios implican márgenes del 71,4 %, 80,0 % y 80,0 %, incompatibles
#: entre sí y con la regla única. `comprobar()` vigila que ese id no aparezca
#: en ningún campo `fuente` del módulo.
PS_58_FIJOS = 5000.0
PS_58_EQUILIBRIO = 7200.0

#: La brecha entre el food cost de escandallo de la carta y la regla del 32 %.
#: Está medida, es grande y se explica: si no se explica, el lector cree que
#: una de las dos herramientas miente.
BRECHA_FOOD_COST = (
    'El escandallo de las 30 referencias da un food cost de materia MUY por debajo '
    'del 30-35 % de la regla del sector, y no es un error de ninguna de las dos '
    'cosas: la regla incluye lo que el escandallo de la pieza deja fuera. Cuatro '
    'partidas, en orden de tamaño: (1) el producto de TERCEROS que revende el '
    'despacho -bebida, café, helado, bombonería comprada-, que no tiene escandallo '
    'propio y compra a precio de distribuidor; (2) la merma real, que en producto '
    'fresco se va por encima del objetivo del 5 % que trae precargado el kit; '
    '(3) el packaging, entre el 5 % y el 15 % del coste del producto (PS-59); y '
    '(4) la subida de la materia prima, que en mantequilla y cacao no es teórica '
    '(PS-66, PS-67). Por eso el P&L del libro 5 se proyecta con la regla del 32 % '
    'y no con el escandallo: es el supuesto CONSERVADOR. El libro 4 mide el tuyo '
    'de verdad, y la diferencia entre los dos números es tu colchón.'
)


# ==========================================================================
# 18. LECTURA DE LOS FICHEROS DEL KIT (para las comprobaciones)
# ==========================================================================
#: Un xlsx cada vez, `read_only=True`, y se cierra antes de abrir el siguiente:
#: es la regla térmica del proyecto y además evita dejar handles abiertos.
def _abre(ruta):
    import openpyxl
    return openpyxl.load_workbook(ruta, read_only=True, data_only=True)


def _kit_escandallo(hoja):
    """Lee una hoja de escandallo de `kit-escandallos/05-pasteleria.xlsx` y
    devuelve (rendimiento, [(ingrediente, ud_compra, precio, cantidad, ud_uso,
    factor, merma), ...]).

    Las columnas se localizan POR NOMBRE de cabecera, no por letra: si el kit
    se regenera y mueve una columna, esto sigue funcionando.
    """
    wb = _abre(KIT_ESCANDALLOS)
    try:
        ws = wb[hoja]
        filas = [list(r) for r in ws.iter_rows(min_row=1, max_row=ws.max_row,
                                               max_col=ws.max_column, values_only=True)]
    finally:
        wb.close()
    cab_i = None
    for i, fila in enumerate(filas):
        if any(isinstance(c, str) and c.strip() == 'Ingrediente' for c in fila):
            cab_i = i
            break
    if cab_i is None:
        raise RuntimeError('No encuentro la cabecera «Ingrediente» en %s!%s'
                           % (KIT_ESCANDALLOS, hoja))
    cab = [(c.strip() if isinstance(c, str) else c) for c in filas[cab_i]]

    def col(nombre):
        for j, c in enumerate(cab):
            if c == nombre:
                return j
        raise RuntimeError('Falta la columna %r en %s!%s' % (nombre, KIT_ESCANDALLOS, hoja))

    c_ing, c_udc = col('Ingrediente'), col('Ud. Compra')
    c_pre, c_can = col('Precio/Ud (€)'), col('Cantidad')
    c_udu, c_fac, c_mer = col('Ud. Uso'), col('Factor'), col('Merma (%)')
    lineas, rendimiento = [], None
    for fila in filas[cab_i + 1:]:
        v = fila[c_ing] if c_ing < len(fila) else None
        if not isinstance(v, str) or not v.strip():
            continue
        etiqueta = v.strip()
        if etiqueta.startswith('COSTE TOTAL INGREDIENTES'):
            continue
        if etiqueta.startswith('Rendimiento'):
            for celda in fila[1:]:
                if isinstance(celda, (int, float)):
                    rendimiento = int(celda)
                    break
            continue
        if fila[c_pre] is None or fila[c_can] is None:
            continue
        lineas.append((etiqueta,
                       fila[c_udc],
                       round(float(fila[c_pre]), 6),
                       round(float(fila[c_can]), 6),
                       fila[c_udu],
                       round(float(fila[c_fac]), 6),
                       round(float(fila[c_mer] or 0), 6)))
    return rendimiento, lineas


def _kit_columna_a(ruta, hoja):
    """Valores de texto de la primera columna de una hoja del kit."""
    wb = _abre(ruta)
    try:
        ws = wb[hoja]
        out = [str(r[0]).strip() for r in ws.iter_rows(min_row=1, max_row=ws.max_row,
                                                       max_col=1, values_only=True)
               if r[0] is not None]
    finally:
        wb.close()
    return out


def _kit_hojas(ruta):
    wb = _abre(ruta)
    try:
        return list(wb.sheetnames)
    finally:
        wb.close()


#: Las tres referencias que se copian del kit, con su hoja de origen.
COPIADAS_DEL_KIT = (('T1', 'Tarta Chocolate'), ('B1', 'Croissants'), ('PI3', 'Macarons'))

#: Las tres que la SPEC §3 manda comprobar que están PRECARGADAS en el kit.
PRECARGADAS_A_COMPROBAR = ('Croissant de mantequilla', 'Pain au chocolat',
                           'Napolitana de crema')


# ==========================================================================
# 19. COMPROBACIONES
# ==========================================================================
#: Cifras y palabras de la lista negra del §5 de la SPEC. Si alguna aparece en
#: el módulo, es que se ha colado un dato prohibido.
#:
#: El barrido se hace sobre el CÓDIGO, no sobre los datos, porque un dato
#: prohibido puede colarse igual en un comentario o en una nota de celda. Eso
#: obliga a excluir dos zonas donde las agujas aparecen a propósito: el
#: docstring del módulo (que enumera lo que NO entra) y las líneas marcadas
#: con `LN-OK`, que son menciones deliberadas -«nunca escribas esto»- y no
#: usos. Sin esa exclusión el gate se denuncia a sí mismo y deja de servir.
CIFRAS_PROHIBIDAS = (
    ('11729', 'N-1: censo de pastelerías del CNAE'),                       # LN-OK
    ('1080000', 'N-2: facturación media inventada'),                       # LN-OK
    ('1,08 M', 'N-2: facturación media inventada'),                        # LN-OK
    ('84.000-180.000', 'N-2: rango de facturación inventado'),             # LN-OK
    ('84000', 'N-2: rango de facturación inventado'),                      # LN-OK
    ('1499', 'N-8: horno modular Salva a precio de folleto'),              # LN-OK
    ('1.499', 'N-8: horno modular Salva a precio de folleto'),             # LN-OK
    ('110 m', 'D22: la superficie de La Clara es 90 m2'),                  # LN-OK
    ('dulcer', 'SPEC 6: falso amigo, no se usa como sinónimo'),            # LN-OK
    ('artesana ', 'SPEC 6: la forma es «artesanal»'),                      # LN-OK
    ('Oficial', 'D22: no existe como perfil en el kit'),                   # LN-OK
    ('4 %-13 %', 'D18: la horquilla correcta de la línea hermana es otra'), # LN-OK
)

#: El id de sector que D23 saca de las cifras citables. No se busca en el
#: texto -mencionarlo para decir que se excluye es legítimo- sino en los
#: campos `fuente`, que es donde sería un uso y no una mención.
ID_SECTOR_EXCLUIDO = 'PS-' + '60'


def _texto_barrible(fuente_py):
    """El código sin el docstring del módulo y sin las líneas marcadas LN-OK."""
    cuerpo = fuente_py
    i = cuerpo.find('\"\"\"')
    if i >= 0:
        j = cuerpo.find('\"\"\"', i + 3)
        if j > i:
            cuerpo = cuerpo[:i] + cuerpo[j + 3:]
    return '\n'.join(l for l in cuerpo.split('\n') if 'LN-OK' not in l)

#: Patrones de procedencia admitidos en cualquier campo `fuente`.
_RE_FUENTE = re.compile(
    r'^(supuesto'
    r'|PS-\d+[a-z]?'
    r'|PA-\d+[a-z]?'
    r'|D\d+'
    r'|N-\d+'
    r'|kit-escandallos/[^!]+(![^!]+)*'
    r'|kit-tareas-pasteleria/[^!]+(![^!]+)*'
    r'|motor\.PARAMETROS\[[a-z_]+\]'
    r'|planes-v2_0/[A-Za-z_./]+'
    r'|art\. [^+]+'
    r'|Escenario[^+]*'
    r'|nueva en la guía[^+]*'
    r'|Se calcula[^+]*'
    r'|CTE[^+]*'
    r')$')


def _fuente_ok(fuente):
    """Una fuente puede ser una sola procedencia o varias unidas con ' + '."""
    if not isinstance(fuente, str) or not fuente.strip():
        return False
    for tramo in fuente.split(' + '):
        if not _RE_FUENTE.match(tramo.strip()):
            return False
    return True


def comprobar():
    fallos, avisos = [], []

    def exige(cond, mensaje):
        if not cond:
            fallos.append(mensaje)

    # ---- 0. WinAnsi: todo el fichero tiene que caber en cp1252 -----------
    fuente_py = ''
    try:
        fh = open(os.path.abspath(__file__), 'rb')
        try:
            fuente_py = fh.read().decode('utf-8')
        finally:
            fh.close()
        fuente_py.encode('cp1252')
    except UnicodeEncodeError as e:
        fallos.append('Carácter fuera de WinAnsi (cp1252) en la posición %d: %r'
                      % (e.start, fuente_py[max(0, e.start - 40):e.start + 40]))
    except IOError:
        avisos.append('No se pudo releer el fichero para el gate de WinAnsi')

    # ---- 1. lista negra del §5 -------------------------------------------
    barrible = _texto_barrible(fuente_py)
    for aguja, motivo in CIFRAS_PROHIBIDAS:
        if aguja in barrible:
            i = barrible.find(aguja)
            fallos.append('Cifra o palabra prohibida %r (%s): %r'
                          % (aguja, motivo, barrible[max(0, i - 60):i + 60]))
    fuentes_todas = [f[2] for f in PRECIOS_COMPRA.values()]
    fuentes_todas += [p[1] for p in PARAMS.values()]
    fuentes_todas += [e['fuente'] for e in EQUIPAMIENTO]
    fuentes_todas += [c[5] for c in CAPEX] + [t[5] for t in TRASPASOS]
    fuentes_todas += [c['fuente'] for c in CANALES] + [f[5] for f in CHECKLIST_LEGAL]
    fuentes_todas += [p[2] for p in PROVEEDORES] + [g[2] for g in GASTOS_FIJOS_MENSUALES]
    fuentes_todas += [r['fuente_escandallo'] for r in CARTA]
    fuentes_todas += [r['fuente_pvp'] for r in CARTA]
    fuentes_todas += [p['fuente_factor'] for p in PICOS] + [p['fuente_uds'] for p in PICOS]
    fuentes_todas += [NEGOCIO[k] for k in NEGOCIO if k.startswith('fuente_')]
    fuentes_todas += [FUENTE_CONVENIO, FUENTE_PLANTILLA, FUENTE_ESTACIONALIDAD,
                      FUENTE_AMORTIZACION, FUENTE_GANTT, FUENTE_HORIZONTE,
                      FINANCIACION['fuente'], RAMPA['fuente']]
    malas = [f for f in fuentes_todas if ID_SECTOR_EXCLUIDO in str(f)]
    exige(not malas,
          'D23: el id de sector excluido se usa como fuente en %d sitios' % len(malas))

    # ---- 2. el negocio ---------------------------------------------------
    exige(abs(sum(z[2] for z in ZONAS) - 90.0) < 1e-9,
          'Las 7 zonas no suman los 90 m² de D22: %.2f' % sum(z[2] for z in ZONAS))
    exige(abs(sum(BLOQUES_M2.values()) - 90.0) < 1e-9,
          'Los 4 bloques de D22 no suman 90 m²')
    exige(len(ZONAS) == 7, 'PS-86d declara 7 zonas obligatorias y hay %d' % len(ZONAS))
    for bloque, m2 in BLOQUES_M2.items():
        suma = sum(z[2] for z in ZONAS if z[1] == bloque)
        exige(abs(suma - m2) < 1e-9,
              'Las zonas del bloque «%s» suman %.2f m² y D22 dice %.2f' % (bloque, suma, m2))
    exige(NEGOCIO['m2_total'] == 90.0, 'NEGOCIO[m2_total] ya no son 90 m² (D22)')
    exige(20.0 <= NEGOCIO['potencia_hornos_kw'] <= 80.0,
          'La potencia de hornos se sale de los 20-80 kW de PS-86a')
    exige(NEGOCIO['potencia_instalada_kw'] > NEGOCIO['potencia_hornos_kw'],
          'La potencia instalada no puede ser menor que la de los hornos')

    # ---- 3. plantilla y convenio ----------------------------------------
    jornadas = sum(p[2] for p in PLANTILLA)
    exige(abs(jornadas - 3.5) < 1e-9,
          'Las jornadas suman %.2f y D22 fija 3,5' % jornadas)
    exige(len(PLANTILLA) == 5, 'La plantilla no tiene 5 personas (D22)')
    for pid, perfil, _j, grupo, area, _h, _t in PLANTILLA:
        base = perfil.rstrip(' AB')
        exige(base in PERFILES_KIT,
              '%s usa el perfil «%s», que no es uno de los 4 literales del kit' % (pid, perfil))
        exige(1 <= grupo <= len(CONVENIO), '%s apunta a un grupo de convenio inexistente' % pid)
        exige(area in CONVENIO[grupo - 1][4],
              '%s está en el área %s y su grupo de convenio no la contempla' % (pid, area))
    vitrina = [p for p in PLANTILLA if p[1].startswith('Dependiente Vitrina')]
    exige(len(vitrina) == 2, 'D22 y C8 exigen DOS personas en Dependiente Vitrina')
    cubiertos = set(p[1].rstrip(' AB') for p in PLANTILLA)
    exige(cubiertos == set(PERFILES_KIT),
          'Los 5 renglones no cubren los 4 perfiles del kit: %s' % sorted(cubiertos))

    exige(len(CONVENIO) == 6, 'El convenio de Madrid tiene 6 grupos y hay %d' % len(CONVENIO))
    exige(CONVENIO_PAGAS == 15, 'El convenio de Madrid paga 15, no %d' % CONVENIO_PAGAS)
    for n, nombre, mes, anio, _areas, _puestos in CONVENIO:
        exige(abs(mes * CONVENIO_PAGAS - anio) < 0.005,
              'Grupo %d (%s): %.2f x %d no da %.2f' % (n, nombre, mes, CONVENIO_PAGAS, anio))
    mas_bajo = min(c[3] for c in CONVENIO)
    exige(mas_bajo > P('smi_anual'),
          'El grupo más bajo del convenio (%.2f) ya no supera el SMI anual (%.2f): esa '
          'frase está en el cap. 13 y habría que reescribirla' % (mas_bajo, P('smi_anual')))

    # ---- 4. parámetros ---------------------------------------------------
    for clave, (valor, fuente, _nota) in PARAMS.items():
        exige(_fuente_ok(fuente), 'PARAMS[%s] tiene una fuente no reconocida: %r'
              % (clave, fuente))
        exige(valor is not None, 'PARAMS[%s] sin valor' % clave)
    exige(abs(P('food_cost_objetivo') + margen_bruto_objetivo() - 1.0) < 1e-9,
          'La regla única de margen no cierra (D23)')
    exige(0.30 <= P('food_cost_objetivo') <= 0.35,
          'El food cost objetivo se sale de la banda 30-35 % de PS-56')
    exige(abs(P('ss_empresa') - 0.33) < 1e-9,
          'ss_empresa se ha despegado del parámetro de la familia (motor.PARAMETROS)')
    exige(abs(P('smi_anual') - 17094.0) < 1e-9,
          'smi_anual se ha despegado del parámetro de la familia (motor.PARAMETROS)')
    exige(abs(P('smi_mensual') * P('smi_pagas') - P('smi_anual')) < 0.5,
          'El SMI mensual por 14 pagas no da el SMI anual (PA-32)')

    # ---- 5. la carta ------------------------------------------------------
    exige(len(CARTA) == 30, 'La carta tiene %d referencias y la SPEC fija 30' % len(CARTA))
    conteo = dict((f, len(por_familia(f))) for f in FAMILIAS)
    esperado = {'Bollería': 6, 'Pastelería individual': 6, 'Tartas y entremets': 6,
                'Panes de acompañamiento': 4, 'Temporada': 8}
    exige(conteo == esperado,
          'El reparto por familia no es el de la SPEC: %s frente a %s' % (conteo, esperado))
    mix = sum(r['mix_pct'] for r in CARTA)
    exige(abs(mix - 100.0) < 1e-6, 'El mix suma %.4f %% y tiene que sumar 100' % mix)
    ids = [r['id'] for r in CARTA]
    exige(len(set(ids)) == len(ids), 'Hay ids repetidos en la carta')
    nombres = [r['nombre'] for r in CARTA]
    exige(len(set(nombres)) == len(nombres), 'Hay nombres repetidos en la carta')

    for r in CARTA:
        exige(r['via_huevo'] in VIAS_HUEVO,
              '%s tiene una vía de huevo desconocida: %r' % (r['id'], r['via_huevo']))
        exige(isinstance(r['relleno'], bool) and isinstance(r['estable_ambiente'], bool),
              '%s: relleno y estable_ambiente tienen que ser booleanos' % r['id'])
        if r['via_huevo'] == 'estable a ambiente':
            exige(r['estable_ambiente'],
                  '%s dice vía «estable a ambiente» y estable_ambiente es False' % r['id'])
        exige(r['tanda'] >= 1 and r['gramaje_g'] > 0,
              '%s: tanda o gramaje inválidos' % r['id'])
        exige(r['minutos_mo_tanda'] > 0, '%s no declara minutos de mano de obra' % r['id'])
        esperado_iva = 0.04 if r['familia'] == 'Panes de acompañamiento' else 0.10
        exige(abs(r['iva'] - esperado_iva) < 1e-9,
              '%s lleva IVA %.2f y le toca %.2f (PA-36 / PA-36b)'
              % (r['id'], r['iva'], esperado_iva))
        exige(_fuente_ok(r['fuente_pvp']) or r['fuente_pvp'] == 'supuesto',
              '%s: fuente_pvp no reconocida' % r['id'])
        exige('supuesto' in r['fuente_escandallo'] or r['fuente_escandallo'].startswith('kit-'),
              '%s: fuente_escandallo tiene que decir «supuesto» o apuntar al kit' % r['id'])
        exige('supuesto' in r['fuente_gramaje'] or r['fuente_gramaje'].startswith('kit-'),
              '%s: fuente_gramaje tiene que decir «supuesto» o apuntar al kit' % r['id'])
        for linea in r['lineas']:
            exige(linea[0] in PRECIOS_COMPRA,
                  '%s usa el ingrediente %r y no tiene precio de compra' % (r['id'], linea[0]))
            exige(0.0 <= linea[4] < 1.0, '%s: merma fuera de rango en %r' % (r['id'], linea[0]))
        exige(pvp_sin_iva(r) > coste_total_unidad(r),
              '%s vende por debajo de coste (materia + mano de obra)' % r['id'])
        if r['familia'] == 'Temporada':
            exige(r['pico'] is not None, '%s es de temporada y no cuelga de ningún pico' % r['id'])
        if r['pico'] is not None:
            exige(r['pico'] in [p['nombre'] for p in PICOS],
                  '%s cuelga del pico %r, que no existe' % (r['id'], r['pico']))

    for ing, (precio, _ud, fuente) in PRECIOS_COMPRA.items():
        exige(precio > 0, 'El ingrediente %r no tiene precio' % ing)
        exige(_fuente_ok(fuente), 'El ingrediente %r tiene una fuente no reconocida: %r'
              % (ing, fuente))

    # ---- 6. las 3 copiadas, contra el xlsx del kit -----------------------
    if not os.path.exists(KIT_ESCANDALLOS):
        avisos.append('No existe %s: no se ha podido comprobar la copia declarada'
                      % KIT_ESCANDALLOS)
    else:
        try:
            for ref_id, hoja in COPIADAS_DEL_KIT:
                ref = [r for r in CARTA if r['id'] == ref_id][0]
                rendimiento, kit_lineas = _kit_escandallo(hoja)
                exige(rendimiento == ref['tanda'],
                      '%s: el kit rinde %s uds por tanda y aquí hay %s'
                      % (ref_id, rendimiento, ref['tanda']))
                exige(len(kit_lineas) == len(ref['lineas']),
                      '%s: el kit tiene %d líneas y aquí hay %d'
                      % (ref_id, len(kit_lineas), len(ref['lineas'])))
                for kit_l, mia in zip(kit_lineas, ref['lineas']):
                    k_ing, k_udc, k_pre, k_can, k_udu, k_fac, k_mer = kit_l
                    m_ing, m_can, m_udu, m_fac, m_mer = mia
                    precio, ud_compra, _f = precio_compra(m_ing)
                    exige(k_ing == m_ing,
                          '%s: el kit dice %r y aquí %r' % (ref_id, k_ing, m_ing))
                    exige(abs(k_pre - precio) < 0.005,
                          '%s / %s: precio del kit %.4f y aquí %.4f'
                          % (ref_id, k_ing, k_pre, precio))
                    exige(str(k_udc) == str(ud_compra),
                          '%s / %s: ud. de compra del kit %r y aquí %r'
                          % (ref_id, k_ing, k_udc, ud_compra))
                    exige(abs(k_can - m_can) < 1e-6,
                          '%s / %s: cantidad del kit %.6f y aquí %.6f'
                          % (ref_id, k_ing, k_can, m_can))
                    exige(str(k_udu) == str(m_udu),
                          '%s / %s: ud. de uso del kit %r y aquí %r'
                          % (ref_id, k_ing, k_udu, m_udu))
                    exige(abs(k_fac - m_fac) < 1e-6,
                          '%s / %s: factor del kit %.4f y aquí %.4f'
                          % (ref_id, k_ing, k_fac, m_fac))
                    exige(abs(k_mer - m_mer) < 1e-6,
                          '%s / %s: merma del kit %.4f y aquí %.4f'
                          % (ref_id, k_ing, k_mer, m_mer))
        except Exception as e:                                # noqa: BLE001
            fallos.append('No se pudo comparar contra %s: %s' % (KIT_ESCANDALLOS, e))

    # ---- 7. las precargadas del kit (SPEC §3: hay que abrirlo) -----------
    for ruta, hoja in ((KIT_PLAN, 'Plan Semanal'), (KIT_ALERGENOS, 'Matriz Alérgenos')):
        if not os.path.exists(ruta):
            avisos.append('No existe %s: no se han podido comprobar las precargadas' % ruta)
            continue
        try:
            col = _kit_columna_a(ruta, hoja)
        except Exception as e:                                # noqa: BLE001
            fallos.append('No se pudo leer %s!%s: %s' % (ruta, hoja, e))
            continue
        for nombre in PRECARGADAS_A_COMPROBAR:
            exige(nombre in col,
                  'La SPEC §3 afirma que «%s» viene precargada en %s!%s y NO está'
                  % (nombre, os.path.basename(ruta), hoja))
        for r in CARTA:
            if r['nombre_en_el_kit'].startswith('nueva en la guía'):
                continue
            # Alguna referencia se llama distinto en el kit (el macaron, que allí
            # es «Macarons (caja de 6)»): se compara el literal declarado.
            literal = r.get('nombre_literal_en_kit', r['nombre'])
            if os.path.basename(ruta) in r['nombre_en_el_kit'] and literal not in col:
                fallos.append('«%s» dice venir de %s!%s con el nombre «%s» y ese nombre '
                              'no está en la hoja'
                              % (r['nombre'], os.path.basename(ruta), hoja, literal))

    if not os.path.exists(KIT_PERFILES):
        avisos.append('No existe %s: no se han podido comprobar los 4 perfiles' % KIT_PERFILES)
    else:
        try:
            hojas = _kit_hojas(KIT_PERFILES)
            for perfil in PERFILES_KIT:
                exige(perfil in hojas,
                      'El perfil «%s» ya no es una pestaña de %s: %s'
                      % (perfil, os.path.basename(KIT_PERFILES), hojas))
        except Exception as e:                                # noqa: BLE001
            fallos.append('No se pudo leer %s: %s' % (KIT_PERFILES, e))

    # ---- 8. equipamiento (D17 y D21) -------------------------------------
    for eq in EQUIPAMIENTO:
        exige(eq['base_iva'] in ('sin IVA', 'con IVA', 'no declarada'),
              'Equipamiento %d: base_iva desconocida %r' % (eq['n'], eq['base_iva']))
        exige(eq['tipo_iva'] == 0.21,
              'Equipamiento %d: el equipamiento va al 21 %%' % eq['n'])
        tiene = (eq['valor_verificado'] is not None) + (eq['supuesto_por_defecto'] is not None)
        exige(tiene == 1,
              'Equipamiento %d (%s): tiene que traer valor verificado O supuesto por '
              'defecto, y trae %d (D21)' % (eq['n'], eq['partida'], tiene))
        if eq['valor_verificado'] is None:
            exige(eq['supuesto_por_defecto'] > 0,
                  'Equipamiento %d: celda verde vacía (D21)' % eq['n'])
            exige('supuesto' in eq['fuente'],
                  'Equipamiento %d no tiene precio verificado y su fuente no dice '
                  '«supuesto»' % eq['n'])
        exige(_fuente_ok(eq['fuente']),
              'Equipamiento %d: fuente no reconocida %r' % (eq['n'], eq['fuente']))
        exige(eq['plazo_semanas'] > 0 and eq['fuente_plazo'] == 'supuesto',
              'Equipamiento %d: el plazo de entrega es supuesto y tiene que decirlo' % eq['n'])
    dot = dotacion_tipo_sin_iva()
    exige(abs(dot - PS_85I_SUBTOTAL) <= PS_85I_TOLERANCIA,
          'La dotación tipo suma %.2f € sin IVA y PS-85i publica %.2f (tolerancia %.2f)'
          % (dot, PS_85I_SUBTOTAL, PS_85I_TOLERANCIA))
    exige(not any(e['dotacion_tipo'] and e['partida'].startswith('Atemperadora')
                  for e in EQUIPAMIENTO),
          'La atemperadora ha vuelto a entrar en el subtotal comparable (D17)')
    vitrinas = [e for e in EQUIPAMIENTO if e['dotacion_tipo'] and 'Vitrina' in e['partida']]
    exige(len(vitrinas) == 1,
          'La vitrina Docriluc se está contando %d veces en la dotación tipo (D17)'
          % len(vitrinas))

    # ---- 9. CAPEX y traspasos --------------------------------------------
    for bloque, partida, importe, base, tipo, fuente, _nota in CAPEX:
        exige(_fuente_ok(fuente), 'CAPEX «%s»: fuente no reconocida %r' % (partida, fuente))
        exige(base in ('sin IVA', 'con IVA'), 'CAPEX «%s»: base_iva desconocida' % partida)
        exige(tipo in (0.0, 0.04, 0.10, 0.21), 'CAPEX «%s»: tipo de IVA raro' % partida)
    for escenario, (eur_m2, total, fuente) in ESCENARIOS_OBRA.items():
        exige(abs(eur_m2 * NEGOCIO['m2_total'] - total) < 1e-6,
              'Escenario de obra «%s»: %.0f €/m² x %.0f m² no da %.0f'
              % (escenario, eur_m2, NEGOCIO['m2_total'], total))
        exige(fuente.startswith('PS-85'), 'Escenario «%s» sin id de PS-85' % escenario)
    exige(ESCENARIO_OBRA_BASE in ESCENARIOS_OBRA, 'El escenario de obra base no existe')
    for t in TRASPASOS:
        exige(t[5] in ('PS-69', 'PS-70'), 'Traspaso %r sin id de anuncio' % (t[0],))
        exige(t[3] > 0, 'Traspaso %r sin precio pedido' % (t[0],))
    exige(len([t for t in TRASPASOS if t[5] == 'PS-69']) == 5,
          'PS-69 recoge 5 anuncios de Barcelona')
    exige(len([t for t in TRASPASOS if t[5] == 'PS-70']) == 10,
          'PS-70 recoge 10 anuncios de España')
    exige(all(t[4] is not None for t in TRASPASOS if t[5] == 'PS-69'),
          'Los cinco de PS-69 son los únicos que traen renta: falta alguna')
    exige(all(t[4] is None for t in TRASPASOS if t[5] == 'PS-70'),
          'PS-70 no publica renta: alguien se la ha inventado')

    # ---- 10. picos, estacionalidad y rampa -------------------------------
    exige(len(PICOS) == 6, 'La SPEC fija 6 picos y hay %d' % len(PICOS))
    nombres_pico = [p['nombre'] for p in PICOS]
    exige(nombres_pico == ['Reyes', 'San Valentín', 'Día del Padre y de la Madre',
                           'Semana Santa', 'Comuniones', 'Todos los Santos'],
          'Los 6 picos no son los del BONUS-02 del kit: %s' % nombres_pico)
    for p in PICOS:
        exige(1.0 < p['factor_obrador'] <= 10.0,
              'Pico %s: el factor de obrador se sale del marco de PS-41 (hasta 10x)'
              % p['nombre'])
        exige(p['dias_campana'] > 0 and p['antelacion_compra_semanas'] > 0,
              'Pico %s: campaña o antelación sin declarar' % p['nombre'])
        exige(p['producto_estrella'] in nombres,
              'Pico %s: el producto estrella «%s» no está en la carta'
              % (p['nombre'], p['producto_estrella']))
        exige(p['uds_dia_pico'] > p['uds_dia_normal'],
              'Pico %s: el pico no supera al día normal' % p['nombre'])
        exige('supuesto' in p['fuente_factor'] and 'supuesto' in p['fuente_uds'],
              'Pico %s: los multiplicadores son supuestos y tienen que decirlo' % p['nombre'])
    exige(max(p['factor_obrador'] for p in PICOS) >= 5.0,
          'Ningún pico llega al 5x de PS-41: el capítulo 15 no se sostiene')

    exige(len(ESTACIONALIDAD_MENSUAL) == 12, 'La estacionalidad no tiene 12 meses')
    media = sum(ESTACIONALIDAD_MENSUAL) / 12.0
    exige(abs(media - 1.0) < 1e-9,
          'La media de los coeficientes de estacionalidad es %.6f y tiene que ser 1,000' % media)
    exige(abs(sum(estacionalidad_pesos()) - 1.0) < 1e-9,
          'Los pesos de estacionalidad no suman 1,000 (los pide así el molde de planes)')
    # Sólo los picos de 2,0x o más levantan el coeficiente de su mes: una
    # campaña de dos días no mueve un mes de 28. Ver la nota de
    # ESTACIONALIDAD_MENSUAL.
    for p in PICOS:
        if p['factor_obrador'] >= 2.0:
            exige(ESTACIONALIDAD_MENSUAL[p['mes'] - 1] >= 1.0,
                  'El pico «%s» multiplica por %.1f y su mes (%s) tiene un coeficiente '
                  'por debajo de 1,00' % (p['nombre'], p['factor_obrador'],
                                          MESES[p['mes'] - 1]))
    r = rampa_mensual()
    exige(len(r) == 12 and abs(r[0] - RAMPA['mes1']) < 1e-9 and abs(r[-1] - 1.0) < 1e-9,
          'La rampa de arranque no va de %.2f a 1,00 en 12 meses' % RAMPA['mes1'])
    exige(all(r[i] <= r[i + 1] + 1e-12 for i in range(11)), 'La rampa no es creciente')
    exige(abs(r[RAMPA['meses'] - 1] - 1.0) < 1e-9,
          'La rampa no llega al 100 %% en el mes %d' % RAMPA['meses'])

    # ---- 11. canales ------------------------------------------------------
    suma_canales = sum(c['ventas_pct'] for c in CANALES)
    exige(abs(suma_canales - 100.0) < 1e-9,
          'Los canales suman %.2f %% y tienen que sumar 100' % suma_canales)
    b2b = [c for c in CANALES if c['canal'].startswith('B2B')][0]
    exige(abs(b2b['ventas_pct'] - 5.0) < 1e-9,
          'El B2B deja de ser el 5 % de PS-53 y la nota del canal dejaría de ser cierta')
    for c in CANALES:
        exige(0.0 < c['margen_bruto'] < 1.0, 'Canal %s: margen fuera de rango' % c['canal'])
        exige(_fuente_ok(c['fuente']), 'Canal %s: fuente no reconocida' % c['canal'])

    # ---- 12. checklist legal y cronograma --------------------------------
    fases_usadas = set(f[0] for f in CHECKLIST_LEGAL)
    exige(fases_usadas == set(FASES_CHECKLIST),
          'El checklist no cubre las 6 fases: %s' % sorted(fases_usadas))
    for fase, tramite, _resp, plazo, _coste, fuente, cambia, _nota in CHECKLIST_LEGAL:
        exige(fase in FASES_CHECKLIST, 'Fase desconocida en «%s»' % tramite)
        exige(plazo > 0, 'El trámite «%s» no declara plazo orientativo' % tramite)
        exige(_fuente_ok(fuente), 'Trámite «%s»: fuente no reconocida %r' % (tramite, fuente))
        exige(isinstance(cambia, bool), 'Trámite «%s»: «cambia por CCAA» no es booleano' % tramite)
    exige(len(CCAA_EJEMPLO) == 4, 'D27 fija 4 CCAA de ejemplo')
    exige(any(f[6] for f in CHECKLIST_LEGAL),
          'Ningún trámite cambia por CCAA: el cuadro de las 4 CCAA no tendría sentido')

    total_meses, camino, holgura = ruta_critica()
    exige(len(GANTT) == 12, 'El cronograma no tiene 12 hitos')
    ids_gantt = set(h[0] for h in GANTT)
    for hid, hito, _d, deps in GANTT:
        for d in deps:
            exige(d in ids_gantt, 'El hito %s depende de %s, que no existe' % (hid, d))
    exige(camino[0] == 'H1' and camino[-1] == 'H12',
          'La ruta crítica no va del primer hito a la apertura: %s' % camino)
    mes_ap = mes_apertura_calculado()
    exige(mes_ap == NEGOCIO['mes_apertura_recomendado'],
          'La ruta crítica (%.1f meses desde %s) abre en %s y el mes recomendado es %s'
          % (total_meses, MESES[MES_INICIO_PROYECTO - 1], MESES[mes_ap - 1],
             MESES[NEGOCIO['mes_apertura_recomendado'] - 1]))
    exige(mes_ap not in [p['mes'] for p in PICOS],
          'La apertura cae en el mes de un pico (%s): el cap. 20 dice justo lo contrario'
          % MESES[mes_ap - 1])
    exige(holgura['H6'] > 0,
          'El pedido de equipamiento no tiene holgura: cualquier retraso movería la apertura')

    # ---- 13. economía ------------------------------------------------------
    pyg = cuenta_resultados_crucero()
    exige(0.08 <= pyg['margen_neto'] <= 0.12,
          'El margen neto del año de crucero es del %.1f %% y PS-48 (declarado por un '
          'pastelero de cuarta generación) sitúa la rentabilidad real en el 8-12 %%'
          % (100 * pyg['margen_neto']))
    exige(pyg['ventas_sin_iva'] > 0 and pyg['gastos_fijos'] > 0, 'El P&L no cuadra')
    exige(punto_muerto_mensual() * 12.0 < pyg['ventas_sin_iva'],
          'La facturación de crucero no llega al punto muerto')
    fc_carta, fc_serv = food_cost_carta(), food_cost_servido()
    exige(0.0 < fc_carta < P('food_cost_objetivo'),
          'El food cost de escandallo de la carta (%.1f %%) ya no está por debajo de la '
          'regla del %.0f %%: si lo supera, la brecha de BRECHA_FOOD_COST se invierte y '
          'hay que reescribirla' % (100 * fc_carta, 100 * P('food_cost_objetivo')))
    exige(fc_serv > fc_carta, 'La merma y el packaging tienen que subir el food cost')
    exige(10.0 <= coste_hora_obrador() <= 30.0,
          'El coste hora de obrador (%.2f €) se ha ido fuera de todo rango creíble'
          % coste_hora_obrador())
    exige(0.04 < iva_medio_carta() < 0.10,
          'El IVA medio de la carta tiene que caer entre el 4 %% y el 10 %%: sale %.4f'
          % iva_medio_carta())
    exige(piezas_dia_crucero() > 0, 'No hay producción diaria')
    for partida, importe, fuente, _nota in GASTOS_FIJOS_MENSUALES:
        exige(_fuente_ok(fuente), 'Gasto fijo «%s»: fuente no reconocida %r' % (partida, fuente))
        exige(importe is None or importe > 0, 'Gasto fijo «%s» sin importe' % partida)
    exige(any(p[0].startswith('Retribución del propietario') for p in GASTOS_FIJOS_MENSUALES),
          'Falta el sueldo del propietario como renglón propio (cap. 18)')
    exige(FINANCIACION['carencia_meses'] < FINANCIACION['plazo_meses'],
          'La carencia no puede ser mayor que el plazo')
    exige(intereses_anio_1() > 0, 'El préstamo no genera intereses')

    # ---- 14. proveedores ---------------------------------------------------
    exige(len(PROVEEDORES) == 9, 'Se publican SÓLO los 9 proveedores verificados')
    for nombre_p, _cat, url, fuente, _nota in PROVEEDORES:
        exige(url.startswith('https://'), 'Proveedor %s sin URL https' % nombre_p)
        exige(_fuente_ok(fuente), 'Proveedor %s: fuente no reconocida' % nombre_p)
    exige(len(set(p[2] for p in PROVEEDORES)) == 9, 'Hay una URL de proveedor repetida')

    # ---- 15. vías de huevo y salidas legales derivadas --------------------
    for r in CARTA:
        temp, manda, _exp = temperatura_legal(r)
        plazo, base, _exp2 = plazo_legal(r)
        exige(temp in (None, 4, 8), '%s: temperatura derivada rara (%r)' % (r['id'], temp))
        if r['relleno'] and not r['estable_ambiente']:
            exige(temp == 4, '%s va relleno y no estable: le toca 4 °C por la fila 9' % r['id'])
        if r['via_huevo'] in ('70/2', 'ovoproducto') and not r['estable_ambiente']:
            exige(plazo == 24, '%s cae en el art. 9.3 y no le sale el plazo de 24 h' % r['id'])
        else:
            exige(plazo is None, '%s no cae en el art. 9.3 y le sale un plazo' % r['id'])
        if temp is None:
            exige(manda == 'Temperatura ambiente', '%s: la base legal no cuadra' % r['id'])
        else:
            exige('RD 1021/2022' in manda, '%s: la base legal no cita la norma' % r['id'])
        exige(base is not None, '%s: el plazo tiene que decir su base legal' % r['id'])
    exige(VIDA_UTIL_DECLARADA is None,
          'D11: la vida útil NO se calcula para las 30 referencias, es celda verde')
    usadas = set(r['via_huevo'] for r in CARTA)
    exige('63/20' not in usadas,
          'Alguna referencia usa la vía 63/20, que es la de huevos fritos y tortillas')
    exige(len(usadas) >= 4, 'La carta sólo usa %d vías: no enseña la decisión' % len(usadas))

    # ---- 16. verificación legal (informativo, no tumba el módulo) --------
    faltan_legales = gate_legal(abortar=False)
    if faltan_legales:
        avisos.append('gate_legal: faltan %d de %d notas legales (%s). Los constructores '
                      'de los libros 4 y 6 NO pueden arrancar hasta que exista el JSON.'
                      % (len(faltan_legales), len(IDS_LEGALES_REQUERIDOS),
                         ', '.join(faltan_legales[:6]) +
                         ('...' if len(faltan_legales) > 6 else '')))

    # ================= resumen =================
    print('«La Clara» - juego de datos único de «Cómo Montar una Pastelería»')
    print('Verificación legal de referencia: %s' % FECHA_VERIFICACION_LEGAL)
    print('')
    print('LOCAL Y PLANTILLA')
    print('  %.0f m² en %d zonas: %s'
          % (sum(z[2] for z in ZONAS), len(ZONAS),
             ' · '.join('%s %.0f' % (b, m) for b, m in
                        sorted(BLOQUES_M2.items(), key=lambda x: -x[1]))))
    print('  %d personas / %.1f jornadas · %d grupos de convenio · %d pagas'
          % (len(PLANTILLA), jornadas, len(CONVENIO), CONVENIO_PAGAS))
    print('  coste empresa del personal %.0f €/año · coste hora de obrador %.2f €/h'
          % (coste_personal_anual(), coste_hora_obrador()))
    print('  el grupo más bajo del convenio (%.2f €/año) supera el SMI anual (%.0f €)'
          % (mas_bajo, P('smi_anual')))
    print('')
    print('CARTA')
    print('  %d referencias en %d familias: %s'
          % (len(CARTA), len(FAMILIAS), ' · '.join('%s %d' % (f, conteo[f]) for f in FAMILIAS)))
    print('  mix %.1f %% · PVP medio %.2f € con IVA · ticket medio %.2f € (%.1f piezas)'
          % (mix, pvp_medio_ponderado(), ticket_medio_con_iva(), P('piezas_por_ticket')))
    print('  food cost de escandallo %.1f %% · con merma y packaging %.1f %% · '
          'regla única de la casa %.0f %%'
          % (100 * fc_carta, 100 * fc_serv, 100 * P('food_cost_objetivo')))
    vias = {}
    for ref in CARTA:
        vias[ref['via_huevo']] = vias.get(ref['via_huevo'], 0) + 1
    print('  vías de huevo: %s' % ' · '.join('%s %d' % (k, v) for k, v in sorted(vias.items())))
    n4 = sum(1 for ref in CARTA if temperatura_legal(ref)[0] == 4)
    n8 = sum(1 for ref in CARTA if temperatura_legal(ref)[0] == 8)
    n24 = sum(1 for ref in CARTA if plazo_legal(ref)[0] == 24)
    print('  %d a 4 °C (art. 4.1 fila 9) · %d a 8 °C (art. 9.3) · %d a temperatura ambiente'
          % (n4, n8, len(CARTA) - n4 - n8))
    print('  %d con plazo legal de 24 h y registro de fecha y hora de elaboración' % n24)
    print('  3 escandallos COPIADOS del kit y comprobados contra el xlsx: %s'
          % ', '.join('%s (%s)' % (i, h) for i, h in COPIADAS_DEL_KIT))
    print('')
    print('INVERSIÓN')
    print('  dotación tipo (PS-85i) %.2f € sin IVA · obrador %.0f € · tienda y vitrina %.0f €'
          % (dot, equipamiento_bloque_sin_iva('Equipamiento de obrador'),
             equipamiento_bloque_sin_iva('Tienda y vitrina')))
    print('  %d líneas de equipamiento: %d con precio verificado, %d con supuesto por defecto'
          % (len(EQUIPAMIENTO),
             sum(1 for e in EQUIPAMIENTO if e['valor_verificado'] is not None),
             sum(1 for e in EQUIPAMIENTO if e['supuesto_por_defecto'] is not None)))
    print('  plazo de entrega crítico: %d semanas' % plazo_critico_semanas())
    print('  CAPEX total %.0f € sin IVA · IVA soportado que hay que adelantar %.0f €'
          % (capex_total_sin_iva(), iva_soportado_capex()))
    print('  obra: %s' % ' · '.join('%s %.0f €/m² = %.0f €' % (k, v[0], v[1])
                                    for k, v in sorted(ESCENARIOS_OBRA.items())))
    print('  %d traspasos reales (precios PEDIDOS, no pagados): %.0f a %.0f €'
          % (len(TRASPASOS), min(t[3] for t in TRASPASOS), max(t[3] for t in TRASPASOS)))
    print('')
    print('AÑO DE CRUCERO')
    print('  ventas %.0f € sin IVA · %d clientes/día × %d días · %.0f piezas/día'
          % (pyg['ventas_sin_iva'], P('tickets_dia_crucero'),
             NEGOCIO['dias_apertura_anio'], piezas_dia_crucero()))
    print('  gastos fijos %.0f €/mes · punto muerto %.0f €/mes'
          % (gastos_fijos_mensuales(), punto_muerto_mensual()))
    print('  beneficio %.0f € · margen neto %.1f %% (PS-48 sitúa lo real en 8-12 %%)'
          % (pyg['beneficio_neto'], 100 * pyg['margen_neto']))
    print('  estacionalidad %s (media %.3f)'
          % ('/'.join('%.2f' % c for c in ESTACIONALIDAD_MENSUAL), media))
    print('  rampa %s' % '/'.join('%.2f' % c for c in rampa_mensual()[:RAMPA['meses']]))
    print('')
    print('CAMPAÑAS, CANALES Y TRÁMITES')
    print('  %d picos: %s' % (len(PICOS), ' · '.join('%s x%.1f' % (p['nombre'], p['factor_obrador'])
                                                     for p in PICOS)))
    print('  %d canales: %s' % (len(CANALES), ' · '.join('%s %.0f %%' % (c['canal'].split(' (')[0],
                                                                        c['ventas_pct'])
                                                         for c in CANALES)))
    print('  checklist legal: %d trámites en %d fases · %d cambian por CCAA (%s)'
          % (len(CHECKLIST_LEGAL), len(FASES_CHECKLIST),
             sum(1 for f in CHECKLIST_LEGAL if f[6]), ', '.join(CCAA_EJEMPLO)))
    print('  ruta crítica %.1f meses: %s' % (total_meses, ' -> '.join(camino)))
    print('  apertura en %s (fuera de los 6 picos) · holgura del pedido de equipos %.1f meses'
          % (MESES[mes_ap - 1], holgura['H6']))
    print('  %d ids legales requeridos por los libros 4 y 6' % len(IDS_LEGALES_REQUERIDOS))
    print('  %d proveedores verificados con URL' % len(PROVEEDORES))
    print('')
    if avisos:
        for a in avisos:
            print('AVISO: %s' % a)
        print('')
    if fallos:
        print('%d FALLO(S):' % len(fallos))
        for f in fallos:
            print('  x %s' % f)
        raise SystemExit(1)
    print('TODAS LAS COMPROBACIONES EN VERDE.')
    return True


if __name__ == '__main__':
    comprobar()
