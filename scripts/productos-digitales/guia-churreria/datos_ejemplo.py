#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
datos_ejemplo.py - JUEGO DE DATOS ÚNICO de «Cómo Montar una Churrería-Chocolatería»
(producto 51, `guia-churreria-chocolateria`; SPEC: scripts/productos-digitales/
guia-churreria-SPEC.md, §3, con las decisiones firmadas de
guia-churreria-DECISIONES-2026-10-03.md).

Los 8 libros de Excel, el guion (`guion_guia_churreria_chocolateria.py`, F2), el bonus 1
(business plan relleno) y el bonus 2 («12 decisiones de apertura resueltas») beben de
ESTE fichero. Regla de la familia: una sola fuente de cifras. Si un número cambia,
cambia aquí y se regeneran los libros.

QUÉ ES «EL MOLINETE» Y QUÉ NO ES
================================
Es un CASO MODELADO, no un cliente real y no «la churrería media de España». Es el juego
de datos que permite que las fórmulas de los 8 libros tengan algo que calcular y que el
lector vea una hoja rellena antes de borrarla y poner la suya. Nada de lo que hay aquí
es un benchmark. No hay recetas con pretensión de exactitud: las cantidades por kilo de
masa, por taza o por vaso son DATOS DE EJEMPLO para que las fórmulas calculen. Y no hay
temperatura de fritura del churro en ningún sitio (V-02 resuelta, rama B: sin fuente
primaria).

D17 · COMPROBACIÓN DE MARCA, hecha el 03-10-2026 y declarada aquí
  · TMview (`tmdn.org/tmview/api/search/results`, oficinas ES y EM, clases 30 y 43):
    curl termina con el código 56 y WebFetch con ECONNRESET. La API del localizador de
    la OEPM (`consultas5.oepm.es/ApiLocalizadorMarcas`) exige un token de reCAPTCHA y
    sin él responde «false». REGISTRO NO CONSULTABLE desde el Mac el 03-10-2026.
  · Búsqueda web: existe un negocio VIVO del mismo sector con el nombre de la SPEC,
    «Bar - Cafetería - Churrería La Rueda», en la calle Pozo 13 de Ronda (Málaga), con
    horario de 8:00 a 13:00 y sin señal de cierre (ficha de Trip.com leída el
    03-10-2026). Es justo el caso que D17 manda evitar.
  · Decisión: el caso pasa a llamarse «Churrería-Chocolatería El Molinete», el primer
    candidato del encargo. Dos búsquedas («El Molinete» churrería; «El Molinete»
    cafetería, bar, restaurante o chocolatería) no devuelven ningún negocio de
    hostelería con ese nombre (sólo «Molinet Cafè Antic», en Barcelona, que es otro
    nombre). Si al abrir el registro apareciese una marca viva en la clase 30 o 43, el
    nombre se cambia AQUÍ (queda «La Taza de Barrio», sin resultados en la web) y se
    regeneran los ocho libros. La SPEC y el guion tienen que recoger el cambio.

LA REGLA DE PROCEDENCIA (SPEC §3): CUATRO ORÍGENES, NO HAY QUINTO
=================================================================
Cada cifra lleva su origen en el propio `.py`, en un campo `fuente`:
  1. Un id `CUN-*` o `CUS-*` de las fichas de este producto, CON su sufijo cuando sólo
     existe con sufijo (CUS-31a, CUS-32a, CUS-33a, CUS-44h...).
  2. Un id `CHN-*`, `CHS-*` o `FC-IVA-*` reutilizado del JSON común
     `auditorias/guias-v2-research-sector.json` (837 datos), con su sufijo.
  3. «supuesto declarado» (en el campo, «supuesto»): dato de ejemplo sin fuente
     pública, con su razonamiento en la nota. Un supuesto NUNCA se escribe en la prosa,
     la FAQ ni el copy como si fuera un dato del sector (C3).
  4. «heredado»: un supuesto que ya declaró la hermana (`guia-chocolateria/
     datos_ejemplo.py`) o `guias-v2_0/motor.py`, citado por estructura y campo.
Además: «calculado» (sale de otros campos de este fichero, nunca se teclea) y la cita
de un fichero ya publicado del catálogo como `fichero.xlsx!Hoja` (el Pack APPCC 09).
Los ids de fiabilidad «baja» entran sólo como orden de magnitud y lo dicen.

LO QUE SE LEYÓ ANTES DE FIJAR UN SOLO DATO (un xlsx cada vez, `read_only=True`)
=============================================================================
  · `pack-appcc/09-control-aceite-fritura.xlsx`: tres hojas. «Control Aceite» registra
    fecha, freidora, tipo de test, % de compuestos polares, temperatura máxima
    alcanzada, estado, acción realizada y firma (tres filas de ejemplo, una de ellas
    con la acción «Cambio de aceite y limpieza de cuba»); su columna «Estado» lleva los
    umbrales DENTRO de la fórmula, que es la deuda que D8 deja para la sesión v2.x de
    ese pack. «Retirada de aceite usado» registra fecha, litros retirados, gestor
    autorizado, número de documento, firma y observaciones (LER 20 01 25). La
    frecuencia recomendada es un test por freidora y semana. CONSECUENCIA: el libro 4
    CITA ese registro y no lo duplica. Los días entre cambios del lector salen de contar
    las filas con «cambio de aceite» en «Control Aceite», y los litros al gestor se
    contrastan con «Retirada de aceite usado». La temperatura máxima que trae la hoja
    es un criterio del operador (D8) y este paquete no la usa ni la repite.
  · `guia-chocolateria-obrador/calculadora-capex-chocolateria.xlsx!Variante del
    Formato`: la hermana publica para la variante «taza y churros» una sola cifra, la
    chocolatera Ugolini Delice 3 a 527 € sin IVA (`CHS-46a`, celda E37), y deja
    «Sin cifra» la churrera, la freidora, la extracción y la campana con su conducto
    (E38 a E41) y la franquicia Maestro Churrero (E47). FRONTERA: El Molinete NO usa la
    Ugolini (lleva dos Irimar MCH-5 de `CUS-37a`; son máquinas distintas y no se
    contradicen), y la v1.0.1 de la hermana remitirá E38-E41 y E47 a este paquete con
    su id (D7, B5): `CUS-M14` ya publica la inversión de esa franquicia, fechada.

DECISIONES QUE ESTE FICHERO MATERIALIZA (y dónde)
=================================================
  · D2: el caso cifrado es el local de 75 m² con sala (`NEGOCIO`); despacho, caseta y
    franquicia son columnas de `VARIANTES`, sin caso cifrado para la caseta.
  · D6 / A9: el margen del P&L sale del ESCANDALLO (materia prima más aceite
    absorbido); `MARGENES_DE_CONTRASTE` guarda los dos números publicados, cada uno con
    su definición, sólo para la hoja «Los Dos Márgenes».
  · D9 / A1 / A7: convenio de Madrid como EJEMPLO vencido (tablas de 2025), dos figuras
    de nocturnidad que nunca se mezclan (`analisis_nocturnidad()`), suelo del SMI 2026.
  · D10 / D13 / A4 / A5 / A6 / SR-11: horario de Madrid como ejemplo, primera fila del
    checklist «¿la extracción necesita proyecto?», filtros a 1,20 m con gas, la bombona
    pequeña sólo en la caseta, y la nota 2 del CTE con la extinción automática.
  · D11 / V-04: el IVA del chocolate y de las bebidas para llevar es una CELDA VERDE al
    10 % con aviso; nunca un tipo afirmado en prosa.
  · D14 / A3: el verano tiene tres salidas que se comparan por CONTRIBUCIÓN en euros;
    la nota del IAE sobre los locales de temporada no entra en ningún Excel.
  · D15 / SR-02: el techo de traspaso con sala son los 82.000 € pedidos de `CUS-02`.
  · D16 / C1 / C2: `CRUCES` sin ciclos y `ORDEN_RELLENO`; el fondo de maniobra se
    calcula SÓLO en el libro 6 y el CAPEX no lo contiene.
  · V-06 / SR-01: la carta usa la denominación de la etiqueta del preparado; el libro 3
    pide el cacao seco total y si lleva grasa vegetal, y avisa por debajo del 35 %.
  · SR-06: núcleo 8.618,35 € y 9.117,35 € con el Testo, al céntimo; la rellenadora va
    sin cifra (importe del lector).
  · SR-17: el cuadrante completo se cierra aquí y `comprobar()` exige cero huecos.

NOMBRES DE HOJA QUE LA SPEC NO PUEDE USAR TAL CUAL
==================================================
Excel no admite los dos puntos en el nombre de una hoja ni más de 31 caracteres. Cinco
nombres de §2.1 incumplen una de las dos reglas y aquí van corregidos (`HOJAS`), sin
cambiar su contenido: «El Verano (Tres Salidas)», «Mix y Ticket Canal y Temporada»,
«Franquicia o Independiente», «Nocturnidad ET y Convenio» e «Identifica tu Convenio».
`CRUCES` usa ya los nombres corregidos.

LO QUE NO ENTRA
===============
Toda la lista negra del §5 de la SPEC (con sus doce prohibiciones de la verificación
legal) y las cifras de la refutación del research. `comprobar()` barre el fichero
entero, docstring incluido, con `LISTA_NEGRA`; sólo se salta las líneas marcadas
`LN-OK`, que son las que enumeran lo prohibido para poder buscarlo.

VOCABULARIO (SPEC §6)
=====================
churro · porra · churrería-chocolatería · chocolate a la taza · churrera ·
dosificadora · escandallo · puesto · caseta · remolque · obrador. Los regionalismos y
las equivalencias de LATAM son cosa del guion, en su primera mención.

ESTILO Y CODIFICACIÓN
=====================
Prosa con tildes, también en los comentarios (`gate_tildes()` mide los literales contra
el léxico del grupo y contra la hermana). Todo el texto cabe en WinAnsi (cp1252): sin
flechas, sin signos de «menor o igual», sin espacios finos ni guiones no separables.

Ejecutar `/usr/local/bin/python3 datos_ejemplo.py` corre `comprobar()` e imprime el
resumen. Python del Mac: 3.7 (el del sistema no trae openpyxl).
"""

import ast
import importlib.util
import json
import os
import re
import tokenize

_AQUI = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.normpath(os.path.join(_AQUI, '..', '..', '..'))
_DL = os.path.join(_REPO, 'astro-site', 'public', 'dl')
_AUDIT = os.path.normpath(os.path.join(_AQUI, '..', 'auditorias'))
_GUIAS_V2 = os.path.normpath(os.path.join(_AQUI, '..', 'guias-v2_0'))

#: El producto.
PRODUCT_ID = 'guia-churreria-chocolateria'
PID = PRODUCT_ID
N_LIBROS = 8

#: Fecha de los datos y de las dos verificaciones legales que se citan.
FECHA_DATOS = '03-10-2026'
FECHA_VERIFICACION_CUN = '03-10-2026'     # fichas CUN de este producto
FECHA_VERIFICACION_CHN = '12-09-2026'     # fichas CHN reutilizadas de la hermana

#: Los ocho libros (§2.1), con su nombre firmado.
LIBROS = {
    1: 'produccion-hora-punta-y-local.xlsx',
    2: 'calculadora-capex-churreria.xlsx',
    3: 'carta-de-apertura-y-escandallo-churro.xlsx',
    4: 'aceite-de-fritura-coste-y-cambio.xlsx',
    5: 'temporada-franjas-y-ferias.xlsx',
    6: 'plan-financiero-3-anos-churreria.xlsx',
    7: 'checklist-legal-fritura-y-licencias.xlsx',
    8: 'turnos-plantilla-y-madrugada.xlsx',
}

#: Hojas de cada libro, en orden. Cinco nombres de §2.1 corregidos para que Excel los
#: acepte (ver el docstring); el resto, literales de la SPEC.
HOJAS = {
    1: ('Instrucciones', 'Parámetros', 'Zonas y m²', 'Equipos y Capacidad',
        'Freidoras, Potencia y Riesgo', 'Cuello de Botella', 'Día Tipo y Día Punta',
        'Ficha de Visita a Local'),
    2: ('Instrucciones', 'Parámetros', 'CAPEX por Bloque', 'Equipamiento Línea a Línea',
        'Variante del Formato', 'Franquicia o Independiente', 'Traspaso vs Obra Nueva',
        'IVA y Tesorería', 'Proveedores', 'Resumen'),
    3: ('Instrucciones', 'Parámetros', 'Escandallo por kg de Masa',
        'Absorción de Aceite y Merma', 'Chocolate a la Taza', 'Coste Hora',
        'Ración, Docena o Kilo', 'Mix y Ticket Canal y Temporada', 'Los Dos Márgenes',
        'Decisión de Surtido'),
    4: ('Instrucciones', 'Parámetros', 'Consumo y Reposición', 'Punto Económico de Cambio',
        'Escenarios de Precio del Aceite', 'Gestor de Aceite Usado'),
    5: ('Instrucciones', 'Parámetros', 'Peso sobre el Año', 'Franjas del Día',
        'Capacidad contra el Pico', 'Cola del Domingo', 'Refuerzo por Pico',
        'El Verano (Tres Salidas)', 'Punto Muerto por Evento', 'Calendario de Ferias'),
    6: ('0. Supuestos', 'Inversión Inicial', 'PyG 3 Años', 'Punto de Equilibrio',
        'Escenarios', 'Personal', 'Tesorería 12 meses', 'Financiación',
        'Canales y Punto Muerto', 'Instrucciones'),
    7: ('Instrucciones', 'Checklist Legal (F1-F6)', 'Árbol IAE y CNAE por Formato',
        'Régimen de Apertura y Horario', 'Licencia, Humos y Gas',
        'Árbol de Registro Sanitario', 'Ferias y Venta Ambulante',
        'Alérgenos y Aceite Compartido', 'PRL de la Fritura', 'Registro de Formación',
        'Cronograma y Ruta Crítica'),
    8: ('Instrucciones', 'Parámetros', 'Cuadrante por Franja', 'Nocturnidad ET y Convenio',
        'Coste de Plantilla', 'Identifica tu Convenio', 'Horas del Titular'),
}

#: Los cinco nombres de §2.1 que Excel no admite, y el que se usa en su lugar.
HOJAS_RENOMBRADAS = {
    'El Verano: Cerrar, Carta de Verano o Ferias': 'El Verano (Tres Salidas)',
    'Mix y Ticket por Canal y Temporada': 'Mix y Ticket Canal y Temporada',
    'Franquicia frente a Independiente': 'Franquicia o Independiente',
    'Nocturnidad: ET y Convenio': 'Nocturnidad ET y Convenio',
    'Convenio: Cómo Identificar el Tuyo': 'Identifica tu Convenio',
}

#: Orden de relleno firmado (D16). El libro 7 no depende de nadie y va el último.
ORDEN_RELLENO = (3, 1, 4, 5, 8, 2, 6, 7)

#: Ficheros del catálogo que el paquete CITA y nunca vincula.
F_PACK_APPCC_09_CONTROL = 'pack-appcc/09-control-aceite-fritura.xlsx!Control Aceite'
F_PACK_APPCC_09_RETIRADA = 'pack-appcc/09-control-aceite-fritura.xlsx!Retirada de aceite usado'
PACK_APPCC_09 = os.path.join(_DL, 'pack-appcc', '09-control-aceite-fritura.xlsx')

MESES = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
         'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
DIAS = ('L', 'M', 'X', 'J', 'V', 'S', 'D')
NOMBRE_DIA = {'L': 'lunes', 'M': 'martes', 'X': 'miércoles', 'J': 'jueves',
              'V': 'viernes', 'S': 'sábado', 'D': 'domingo'}


def dato(estructura, clave):
    """Valor de un parámetro guardado como (valor, fuente, nota)."""
    return estructura[clave][0]


# ==========================================================================
# 1. EL NEGOCIO: «El Molinete», 75 m² en seis zonas y terraza aparte
# ==========================================================================
#: Cada entrada es (valor, fuente, nota).
NEGOCIO = {
    'nombre': ('Churrería-Chocolatería El Molinete', 'supuesto',
               'Nombre neutro del caso modelado. Sustituye a «La Rueda», que tiene un '
               'homónimo vivo en el sector (ver el docstring, D17).'),
    'nombre_corto': ('El Molinete', 'supuesto', ''),
    'ciudad': ('Ciudad media española sin nombre propio', 'supuesto',
               'Los parámetros de Madrid (horario, ordenanza de humos y convenio) van '
               'como EJEMPLO declarado: el lector pone los de su municipio.'),
    'formato': ('Local fijo con obrador de masa a la vista, freidora bajo campana, '
                'barra, sala, terraza y despacho a calle', 'supuesto',
                'D2 (a): el único caso cifrado del producto.'),
    'm2_total': (75.0, 'CHS-37a + CUS-02',
                 'Convergencia de dos traspasos reales del mismo formato: 75 m² en Elche '
                 'y 74 m² en Vallecas. El reparto por zonas es supuesto.'),
    'm2_terraza': (20.0, 'supuesto',
                   'Aparte de los 75 m² y con autorización propia: la ocupación de la '
                   'vía pública queda fuera del régimen de la Ley 12/2012 (CUN-35).'),
    'renta_mensual': (910.0, 'CUS-02',
                      'La renta del local de Vallecas de 74 m² (anuncio del 06-07-2026, '
                      'lectura de L4 no reabierta por el captcha). Nace en el libro 2 y '
                      'la recibe el 6 por el cruce X18.'),
    'meses_fianza': (2, 'supuesto',
                     'Meses de fianza y garantía que pide el arrendador. Cambia por '
                     'comunidad y por contrato.'),
    'entrada_al_local': ('Obra nueva en un local sin salida de humos', 'supuesto',
                         'El caso más duro y el de la primera fila del checklist. El '
                         'traspaso de CUS-02 es la alternativa de la decisión 2.'),
    'clasificacion_horaria_ejemplo': ('Cafetería o bar', 'CUN-34',
                                      'Para abrir a las 6:00 y a las 7:00 en el ejemplo '
                                      'de Madrid hay que clasificarse como cafetería o '
                                      'bar: como chocolatería no se abre antes de las '
                                      '8:00 (decisión 8, D10).'),
    'epigrafes_iae': ('676 o 673 por la sala, más 644.6 por la venta al peso para llevar',
                      'CUN-09 + CUN-10 + CUN-14',
                      'Inferencia declarada: el 676 no lleva la nota que deja vender en '
                      'el propio establecimiento, así que la venta al peso pide además el '
                      '644.6. Va como pregunta al asesor, nunca como dato.'),
    'mes_apertura': (9, 'supuesto',
                     'Abre el 1 de septiembre: un mes de rodaje antes del pico de '
                     'octubre a marzo y el valle de verano al final del año 1 (§3.6).'),
    'dia_apertura': (1, 'supuesto', ''),
    'dias_cierre_anio': (5, 'supuesto',
                         'Cinco días al año con la persiana bajada, todos a la vez, para '
                         'la limpieza a fondo y la puesta a punto de la línea.'),
    'festivos_entre_semana': (12, 'supuesto',
                              'Festivos que caen de lunes a viernes y que se trabajan '
                              'como un domingo (día punta). Cambia cada año y en cada '
                              'municipio.'),
}

#: Seis zonas que suman 75 m² (§3.1). El reparto es supuesto.
ZONAS = [
    # (zona, m², fuente, nota)
    ('Obrador de masa a la vista', 10.0, 'supuesto',
     'Amasadora, dosificadora y mesa de trabajo. A la vista del cliente: es parte del '
     'reclamo, y obliga a que esté siempre presentable.'),
    ('Fritura bajo campana', 6.0, 'supuesto',
     'La freidora de gas de 25 L y el escurridor, bajo la campana de 1.200 mm. Es la zona '
     'que decide si el local sirve: conducto, potencia y gas.'),
    ('Barra y despacho a calle', 12.0, 'supuesto',
     'Cafetera, chocolateras, caja y la ventanilla del despacho para llevar.'),
    ('Sala', 32.0, 'supuesto', 'Mesas y sillas del consumo en el local.'),
    ('Aseos y vestuario', 8.0, 'supuesto',
     'Aseo de público y vestuario de personal. Si no caben, el local no sirve.'),
    ('Almacén de harina, aceite, envase y bidón de aceite usado', 7.0, 'supuesto',
     'El bidón del aceite usado espera aquí al gestor autorizado.'),
]

#: Bloques del resumen de «Zonas y m²» del libro 1.
ZONA_A_BLOQUE = {
    'Obrador de masa a la vista': 'Producción',
    'Fritura bajo campana': 'Producción',
    'Barra y despacho a calle': 'Atención al cliente',
    'Sala': 'Atención al cliente',
    'Aseos y vestuario': 'Servicios',
    'Almacén de harina, aceite, envase y bidón de aceite usado': 'Servicios',
}


# ==========================================================================
# 2. HORARIO Y FRANJAS: la franja del día vive SÓLO aquí y en el libro 5
# ==========================================================================
#: Horas de apertura por día de la semana, en horas decimales; un fin mayor que 24 es
#: la madrugada del día siguiente. Lectura declarada de §3.2: la pausa de 13:00 a 16:30
#: se aplica todos los días, porque la carta no tiene franja de comida. Los festivos
#: abren y cierran como el domingo.
HORARIO = {
    'L': ((7.0, 13.0), (16.5, 21.0)),
    'M': ((7.0, 13.0), (16.5, 21.0)),
    'X': ((7.0, 13.0), (16.5, 21.0)),
    'J': ((7.0, 13.0), (16.5, 21.0)),
    'V': ((7.0, 13.0), (16.5, 25.0)),
    'S': ((6.0, 13.0), (16.5, 25.0)),
    'D': ((6.0, 13.0), (16.5, 21.0)),
}
FUENTE_HORARIO = 'supuesto'
NOTA_HORARIO = (
    'Supuesto declarado de §3.2: de lunes a viernes de 7:00 a 13:00 y de 16:30 a 21:00; '
    'sábados, domingos y festivos desde las 6:00; viernes y sábados hasta la 1:00; '
    'domingos y festivos hasta las 21:00. Abrir antes de las 8:00 sólo cabe, en el '
    'ejemplo de Madrid, clasificándose como cafetería o bar (CUN-34): es la decisión 8, '
    'y el semáforo que lo avisa vive en la hoja «Franjas del Día» del libro 5.')

#: Hora mínima de apertura del ejemplo de Madrid, por clasificación (CUN-34). El libro
#: 7 la cita y remite al 5, que es donde el lector pone su hora (SR-07).
HORA_MINIMA_APERTURA_MADRID = {
    'cafeteria_bar': (6.0, 'CUN-34', 'Cafeterías, bares y cafés-bares: desde las 6:00 '
                      'hasta las 2:00.'),
    'chocolateria': (8.0, 'CUN-34', 'Chocolaterías, heladerías y salones de té: desde '
                     'las 8:00 hasta la 1:00. No se extrapola a otras comunidades.'),
}

#: Días con franja de noche y días sin ella.
DIAS_CON_NOCHE = ('V', 'S')

#: Las cuatro franjas (§3.2), con su horario por día y su peso en las raciones del día.
#: Los días sin noche pasan su 5 % a la merienda, que es la franja que la noche alarga:
#: así cada día suma cien. Supuestos declarados.
FRANJAS = [
    {'clave': 'desayuno', 'nombre': 'Desayuno',
     'tramos': {'L': (7.0, 10.0), 'M': (7.0, 10.0), 'X': (7.0, 10.0), 'J': (7.0, 10.0),
                'V': (7.0, 10.0), 'S': (6.0, 10.0), 'D': (6.0, 10.0)},
     'pct_con_noche': 50.0, 'pct_sin_noche': 50.0, 'fuente': 'supuesto',
     'nota': 'La mitad del día se despacha antes de las 10:00. Es la franja del pico.'},
    {'clave': 'media_manana', 'nombre': 'Media mañana',
     'tramos': dict((d, (10.0, 13.0)) for d in DIAS),
     'pct_con_noche': 10.0, 'pct_sin_noche': 10.0, 'fuente': 'supuesto', 'nota': ''},
    {'clave': 'merienda', 'nombre': 'Merienda',
     'tramos': dict((d, (16.5, 21.0)) for d in DIAS),
     'pct_con_noche': 35.0, 'pct_sin_noche': 40.0, 'fuente': 'supuesto',
     'nota': ('El 35 % de las raciones del viernes y del sábado; el resto de días se queda '
              'además con el 5 % de la noche.')},
    {'clave': 'noche', 'nombre': 'Noche (viernes y sábado)',
     'tramos': {'V': (21.0, 25.0), 'S': (21.0, 25.0)},
     'pct_con_noche': 5.0, 'pct_sin_noche': 0.0, 'fuente': 'supuesto',
     'nota': 'Sólo viernes y sábado, hasta la 1:00.'},
]


def dias_apertura_anio():
    return 365 - dato(NEGOCIO, 'dias_cierre_anio')


def horas_apertura_dia(dia):
    return sum(b - a for a, b in HORARIO[dia])


def horas_apertura_semana():
    return sum(horas_apertura_dia(d) for d in DIAS)


def pct_franja(franja, dia):
    return franja['pct_con_noche'] if dia in DIAS_CON_NOCHE else franja['pct_sin_noche']


def horas_semana_franja(clave):
    """Horas de apertura de una franja en la semana tipo (cruce X7 del libro 5 al 8)."""
    for f in FRANJAS:
        if f['clave'] == clave:
            return sum(b - a for a, b in f['tramos'].values())
    raise KeyError(clave)


# ==========================================================================
# 3. CONVENIO DE EJEMPLO, PLANTILLA, TURNOS Y LAS DOS FIGURAS DE NOCTURNIDAD
# ==========================================================================
#: D9 / V-01 rama A: el convenio de hostelería de la Comunidad de Madrid, clase C,
#: como EJEMPLO declarado. Venció el 31-12-2025 y está en negociación; mientras no se
#: publique el nuevo se aplican sus tablas de 2025 (CUN-V01). La provincia va en celda
#: verde: el lector busca el suyo con el método de la hoja «Identifica tu Convenio».
CONVENIO = {
    'codigo': ('28002085011981', 'CUN-39', 'Código REGCON del convenio de ejemplo.'),
    'denominacion': ('Hostelería y Actividades Turísticas de la Comunidad de Madrid',
                     'CUN-39', ''),
    'clase': ('C', 'CUN-39',
              'La clase C agrupa cafeterías de una taza, chocolaterías, cafés-bares y '
              'bares; el convenio nombra freidurías, quioscos y chocolaterías.'),
    'tablas': ('2025 · convenio vencido el 31-12-2025, en negociación; se aplican sus '
               'tablas mientras no se publique el nuevo', 'CUN-39 + CUN-V01',
               'Etiqueta obligatoria de toda celda que use estas cuantías (V-01, rama A). '
               'Antes de cada versión 2.x, mirar el BOCM.'),
    'provincia': ('Madrid', 'supuesto', 'Celda verde: el lector pone la suya.'),
    'pagas': (14, 'supuesto',
              'Dos gratificaciones del art. 26 de una mensualidad cada una: compruébalo en '
              'tu convenio (SR-04). Es aritmética del ejemplo, no una cifra de la ficha.'),
    'plus_convenio_mes': (191.22, 'CUN-39', 'Plus de convenio de la clase C en 2025.'),
    'meses_plus_convenio': (11, 'CUN-39', 'El plus se cobra durante once meses.'),
    'plus_noche_22_0': (0.01, 'CUN-40',
                        'De 22:00 a 0:00, cada hora lleva un 1 % más sobre el salario base.'),
    'plus_noche_0_8': (0.25, 'CUN-40',
                       'De 0:00 a 8:00, cada hora lleva un 25 % más sobre el salario base.'),
    'umbral_jornada_nocturna_h': (5.0, 'CUN-40',
                                  'Con cinco o más horas entre las 22:00 y las 8:00, toda '
                                  'la jornada cuenta como nocturna a efectos del plus.'),
    # --- suelo del SMI 2026 y jornada: los parámetros de la familia, sin un número
    # nuevo. El SMI caduca el 31-12-2026 y vive en el anexo, nunca cosido en la prosa.
    'smi_mensual': (1221.0, 'CHN-67', 'Real Decreto del SMI 2026: 1.221 euros al mes.'),
    'smi_anual': (17094.0, 'CHN-67 + heredado: motor.PARAMETROS[smi_anual]',
                  'Cuantía anual de referencia, en celda verde. El real decreto no dice «14 '
                  'pagas». Coste por puesto = MAX(salario; SMI anual a su jornada).'),
    'jornada_anual_h': (1780.0, 'heredado: guia-chocolateria/datos_ejemplo.py PARAMS[horas_anuales_contrato]',
                        'Horas efectivas de un contrato a jornada completa en el ejemplo. La del '
                        'convenio de Madrid no está verificada: celda verde.'),
    'horas_semana_completa': (40.0, 'heredado: guia-chocolateria/datos_ejemplo.py PARAMS[horas_semana_jornada_completa]',
                              'Jornada completa de 40 horas a la semana (1,0).'),
    'aleh_vigencia': ('31-12-2030', 'CUN-32',
                      'El VI Acuerdo Laboral estatal de hostelería sigue vigente hasta esa '
                      'fecha; su lista de actividades nombra freidurías, quioscos y '
                      'chocolaterías y no la palabra churrería (CUN-31).'),
}

#: Salario base mensual de 2025 de la clase C, por nivel (CUN-39). El encaje de cada
#: puesto en un nivel es una ASIMILACIÓN DE FUNCIONES PROPUESTA: ninguna ficha recoge el
#: artículo del ALEH que la sostenga, así que va con la etiqueta «compruébala con tu
#: asesor» (D9). La ficha sugiere el nivel III para quien amasa y fríe.
NIVELES = {
    'III': (1160.37, 'CUN-39'),
    'IV': (1127.42, 'CUN-39'),
    'V': (1086.31, 'CUN-39'),
}
ASIMILACION = 'asimilación propuesta: compruébala con tu asesor'

#: Las dos figuras de A1, separadas. El ET define el TRABAJADOR NOCTURNO por el periodo
#: de 22:00 a 6:00 (al menos tres horas de la jornada diaria, o un tercio de la anual);
#: el convenio paga un PLUS por horas en otras franjas. Nunca se confunden.
TRABAJO_NOCTURNO_ET = {
    'inicio': (22.0, 'CUN-29', 'Trabajo nocturno: el realizado entre las 22:00 y las 6:00.'),
    'fin': (30.0, 'CUN-29', 'Las 6:00 del día siguiente, en horas decimales.'),
    'horas_diarias_minimas': (3.0, 'CUN-29',
                              'Trabajador nocturno: quien realiza NORMALMENTE en ese '
                              'periodo al menos tres horas de su jornada diaria.'),
    'fraccion_jornada_anual': (1.0 / 3.0, 'CUN-29',
                               'O quien se prevé que realice en él un tercio de su '
                               'jornada anual.'),
}

#: Salarios de MERCADO, nunca convenio: ofertas reales de JobToday con las pagas sin
#: declarar (A7). Con doce pagas, 1.300 euros al mes quedan por debajo del SMI anual: es
#: justo lo que enseña el semáforo del libro 8.
SALARIOS_MERCADO = [
    # (puesto que publica la oferta, mínimo €/mes, máximo €/mes, fuente, nota)
    ('Aprendiz de churrero (Valdemoro)', 1300.0, 1500.0, 'CUS-54',
     'Jornada completa; la oferta no dice ni las pagas ni si es bruto.'),
    ('Ayudante de cocina de una churrería (San Blas-Canillejas)', 1500.0, 1600.0, 'CUS-55',
     'Pide tres años de experiencia y empezar a las 5:30. Media hora en el periodo '
     'nocturno legal no hace trabajador nocturno (CUN-29).'),
]
NOTA_SALARIOS_MERCADO = (
    'Rango de mercado, pagas sin declarar. Sirve para saber si lo que vas a ofrecer está '
    'dentro de mercado; lo que te OBLIGA es tu convenio, y por debajo de todo, el SMI.')

#: Método «identifica el tuyo» (V-05 rama B matizada): el convenio provincial de
#: Toledo nombra los obradores de masas fritas. Alcanza a un OBRADOR de churros; si el
#: tuyo es un despacho con sala, te lo confirma un laboralista (nivel C).
CONVENIO_METODO = {
    'toledo_codigo': ('45000145011981', 'CUN-V05 + CHN-93', ''),
    'toledo_ambito': ('obradores de Confitería, Pastelería, fábricas de Mazapán y/o '
                       'Turrones Masas Fritas y Fábricas de Chocolates', 'CUN-V05',
                       'Literal del ámbito funcional, reproducido por una base jurídica '
                       'privada; el boletín provincial no se abrió.'),
    'toledo_vigencia': ('01-01-2025 a 31-12-2026', 'CUN-V05', ''),
    'como_buscar': ('Busca el tuyo en REGCON por denominación y ámbito; este es sólo un '
               'ejemplo del método', 'CHN-93', ''),
}

#: La plantilla de §3.2: titular en nómina (heredado de la hermana), dos churreros a
#: jornada completa, un camarero de sala y un refuerzo a media jornada.
PLANTILLA = [
    {'id': 'P1', 'puesto': 'Titular (encargado/a)', 'jornada': 1.0, 'nivel': 'III',
     'es_titular': True, 'cotiza_ss_empresa': False,
     'fuente': 'supuesto + heredado: guia-chocolateria/datos_ejemplo.py PLANTILLA[P1]',
     'nota': ('Su retribución va en el coste de plantilla como un puesto más (heredado de '
              'la hermana), al nivel III de la tabla de ejemplo: un plan que sólo cuadra si '
              'el titular trabaja gratis no sirve. Es autónomo: cotiza por su cuota, que va '
              'en los gastos fijos, y por eso su retribución no lleva la Seguridad Social de '
              'empresa. Las horas que hace de más no se pagan: son las «Horas del Titular».')},
    {'id': 'P2', 'puesto': 'Churrero/a 1', 'jornada': 1.0, 'nivel': 'III',
     'es_titular': False, 'cotiza_ss_empresa': True, 'fuente': 'supuesto + CUN-39',
     'nota': 'Amasa y fríe. Nivel III por ' + ASIMILACION + '.'},
    {'id': 'P3', 'puesto': 'Churrero/a 2', 'jornada': 1.0, 'nivel': 'III',
     'es_titular': False, 'cotiza_ss_empresa': True, 'fuente': 'supuesto + CUN-39',
     'nota': ('Abre la freidora el fin de semana y, entre semana, atiende la barra y el '
              'despacho por la mañana. Nivel III por ' + ASIMILACION + '.')},
    {'id': 'P4', 'puesto': 'Camarero/a de sala', 'jornada': 1.0, 'nivel': 'IV',
     'es_titular': False, 'cotiza_ss_empresa': True, 'fuente': 'supuesto + CUN-39',
     'nota': ('Barra y sala por la tarde; cierra el viernes y el sábado y, de 21:00 a 1:00, '
              'atiende solo. Nivel IV por ' + ASIMILACION + '.')},
    {'id': 'P5', 'puesto': 'Refuerzo de fin de semana', 'jornada': 0.5, 'nivel': 'V',
     'es_titular': False, 'cotiza_ss_empresa': True, 'fuente': 'supuesto + CUN-39',
     'nota': ('Polivalente: segunda persona en la línea del pico del fin de semana y barra '
              'el lunes por la tarde. Nivel V por ' + ASIMILACION + '.')},
]

#: Los dos puestos: línea de fritura y barra (barra, sala y despacho a calle).
PUESTOS = {'L': 'Línea de fritura', 'B': 'Barra, sala y despacho'}

#: El cuadrante completo de la semana tipo (SR-17). Cada turno es
#: (persona, día, inicio, fin, puesto); un fin mayor que 24 es la madrugada siguiente.
#: Los tres primeros bloques son los casos didácticos de A1, literales de §3.2:
#:   · Churrero/a 1, de lunes a viernes de 6:00 a 14:00.
#:   · Churrero/a 2, sábado y domingo (y festivos) de 4:30 a 12:30.
#:   · Quien cierra el viernes y el sábado, de 17:00 a 1:00.
#: Los festivos se cubren con el turno del domingo y se compensan con descanso: el
#: cuadrante es la semana tipo, sin festivos.
TURNOS = (
    [('P2', d, 6.0, 14.0, 'L') for d in ('L', 'M', 'X', 'J', 'V')]
    + [('P3', 'S', 4.5, 12.5, 'L'), ('P3', 'D', 4.5, 12.5, 'L')]
    + [('P4', 'V', 17.0, 21.0, 'B'), ('P4', 'V', 21.0, 25.0, 'L'),
       ('P4', 'S', 17.0, 21.0, 'B'), ('P4', 'S', 21.0, 25.0, 'L')]
    # --- resto del cuadrante -------------------------------------------------
    + [('P3', d, 7.0, 13.0, 'B') for d in ('M', 'X', 'J', 'V')]
    + [('P4', d, 16.0, 21.5, 'B') for d in ('M', 'X', 'J')]
    + [('P4', 'D', 16.5, 21.0, 'B')]
    + [('P5', 'S', 6.0, 10.0, 'L'), ('P5', 'S', 10.0, 13.0, 'B'),
       ('P5', 'D', 6.0, 10.0, 'L'), ('P5', 'D', 10.0, 13.0, 'B'),
       ('P5', 'L', 16.0, 21.5, 'B')]
    + [('P1', 'L', 7.0, 13.0, 'B'), ('P1', 'L', 16.0, 21.5, 'L')]
    + [('P1', d, 16.0, 21.5, 'L') for d in ('M', 'X', 'J')]
    + [('P1', 'V', 16.0, 21.0, 'L'),
       ('P1', 'S', 6.0, 10.0, 'B'), ('P1', 'S', 12.5, 13.0, 'L'), ('P1', 'S', 16.0, 21.0, 'L'),
       ('P1', 'D', 6.0, 10.0, 'B'), ('P1', 'D', 12.5, 13.0, 'L'), ('P1', 'D', 16.0, 21.5, 'L')]
)
FUENTE_TURNOS = 'supuesto'

#: Cobertura mínima de El Molinete por tramo: (días, inicio, fin, personas, de ellas en
#: la línea). Supuestos declarados. El pico es el desayuno del fin de semana, con dos
#: personas en la línea (cruce X6). La apertura de tarde (16:30-17:00) la hace una
#: persona sola, y la noche también: con el 5 % de las raciones, quien cierra fríe y
#: cobra.
MINIMOS_COBERTURA = [
    ('LMXJV', 7.0, 13.0, 2, 1, 'Mañana entre semana: una persona fríe y otra atiende.'),
    ('SD', 6.0, 10.0, 3, 2, 'Pico del fin de semana: dos en la línea y una en la barra.'),
    ('SD', 10.0, 13.0, 2, 1, 'Media mañana del fin de semana.'),
    ('LMXJVSD', 16.5, 17.0, 1, 1, 'Apertura de tarde: pone la freidora a punto y atiende.'),
    ('LMXJVSD', 17.0, 21.0, 2, 1, 'Merienda: una persona fríe y otra atiende.'),
    ('VS', 21.0, 25.0, 1, 1, 'Noche: quien cierra fríe y cobra.'),
]

#: Reglas prudentes con las que se ha diseñado el cuadrante del ejemplo, sólo para los
#: empleados (el titular es autónomo): doce horas entre jornadas, día y medio seguido de
#: descanso a la semana y nueve horas de trabajo al día como tope. Compruébalas con tu
#: convenio; no son una cita normativa de este paquete.
REGLAS_CUADRANTE = {'descanso_entre_jornadas_h': 12.0, 'descanso_semanal_h': 36.0,
                    'horas_dia_max': 9.0}


def persona(pid):
    for p in PLANTILLA:
        if p['id'] == pid:
            return p
    raise KeyError('Persona desconocida: %r' % pid)


def turnos_de(pid):
    return [t for t in TURNOS if t[0] == pid]


def horas_semana(pid):
    return sum(t[3] - t[2] for t in turnos_de(pid))


def _solape(a1, b1, a2, b2):
    return max(0.0, min(b1, b2) - max(a1, a2))


def _medias_horas(a, b):
    x = a
    while x < b - 1e-9:
        yield x
        x += 0.5


def huecos_de_cobertura():
    """Medias horas de apertura en las que el cuadrante no llega al mínimo. Tiene que
    devolver una lista vacía (SR-17)."""
    huecos = []
    for dias, ini, fin, n_total, n_linea, _nota in MINIMOS_COBERTURA:
        for d in dias:
            for s in _medias_horas(ini, fin):
                en_l = sum(1 for t in TURNOS if t[1] == d and t[2] <= s < t[3] and t[4] == 'L')
                en_b = sum(1 for t in TURNOS if t[1] == d and t[2] <= s < t[3] and t[4] == 'B')
                if en_l < n_linea or en_l + en_b < n_total:
                    huecos.append((d, s, n_total - en_l - en_b, max(0, n_linea - en_l)))
    return huecos


def tramos_sin_minimo():
    """Medias horas de apertura que ningún mínimo cubre: tiene que ser cero, o la regla
    de cobertura tendría agujeros."""
    fuera = []
    for d in DIAS:
        for a, b in HORARIO[d]:
            for s in _medias_horas(a, b):
                if not any(d in m[0] and m[1] <= s < m[2] for m in MINIMOS_COBERTURA):
                    fuera.append((d, s))
    return fuera


def problemas_del_cuadrante():
    """Las reglas prudentes de `REGLAS_CUADRANTE`, persona a persona (sin el titular),
    más el tope de su jornada contratada."""
    problemas = []
    for p in PLANTILLA:
        if p['es_titular']:
            continue
        pid = p['id']
        tope = p['jornada'] * dato(CONVENIO, 'horas_semana_completa')
        if horas_semana(pid) > tope + 1e-9:
            problemas.append('%s pasa de su jornada: %.1f h de %.1f' % (pid, horas_semana(pid), tope))
        por_dia = {}
        for _p, d, a, b, _r in turnos_de(pid):
            por_dia.setdefault(DIAS.index(d), []).append((a, b))
        for di, tramos in por_dia.items():
            if sum(b - a for a, b in tramos) > REGLAS_CUADRANTE['horas_dia_max'] + 1e-9:
                problemas.append('%s pasa de nueve horas el %s' % (pid, NOMBRE_DIA[DIAS[di]]))
        bloques = sorted((di * 24.0 + min(a for a, b in t), di * 24.0 + max(b for a, b in t))
                         for di, t in por_dia.items())
        descansos = []
        for i, (_ini, fin) in enumerate(bloques):
            siguiente = bloques[(i + 1) % len(bloques)][0] + (168.0 if i + 1 == len(bloques) else 0.0)
            descansos.append(siguiente - fin)
        if min(descansos) < REGLAS_CUADRANTE['descanso_entre_jornadas_h'] - 1e-9:
            problemas.append('%s descansa %.1f h entre dos jornadas' % (pid, min(descansos)))
        if max(descansos) < REGLAS_CUADRANTE['descanso_semanal_h'] - 1e-9:
            problemas.append('%s no tiene día y medio seguido de descanso' % pid)
    return problemas


def analisis_nocturnidad(pid):
    """Las DOS figuras de A1, en dos columnas que no se mezclan:
      · ET art. 36.1 (CUN-29): horas entre 22:00 y 6:00, días con tres horas o más y peso
        sobre la jornada -> «sí», «no» o «revísalo con tu asesor» (el «normalmente» del
        artículo no está interpretado en ninguna ficha).
      · Plus del convenio de ejemplo (CUN-40): horas de 22:00 a 0:00 y de 0:00 a 8:00, y
        días en que la jornada entera cuenta como nocturna (cinco horas o más)."""
    ini_et = dato(TRABAJO_NOCTURNO_ET, 'inicio')
    fin_et = dato(TRABAJO_NOCTURNO_ET, 'fin')
    minimo = dato(TRABAJO_NOCTURNO_ET, 'horas_diarias_minimas')
    tercio = dato(TRABAJO_NOCTURNO_ET, 'fraccion_jornada_anual')
    umbral = dato(CONVENIO, 'umbral_jornada_nocturna_h')
    et_por_dia, conv_por_dia = {}, {}
    h_22_0 = h_0_8 = 0.0
    for _p, d, a, b, _r in turnos_de(pid):
        # periodo legal: 22:00-6:00 del mismo día y 0:00-6:00 de ese mismo día
        h_et = _solape(a, b, ini_et, fin_et) + _solape(a, b, 0.0, fin_et - 24.0)
        et_por_dia[d] = et_por_dia.get(d, 0.0) + h_et
        h22 = _solape(a, b, 22.0, 24.0)
        h08 = _solape(a, b, 0.0, 8.0) + _solape(a, b, 24.0, 32.0)
        h_22_0 += h22
        h_0_8 += h08
        conv_por_dia[d] = conv_por_dia.get(d, 0.0) + _solape(a, b, 22.0, 32.0) + _solape(a, b, 0.0, 8.0)
    dias = sorted(et_por_dia, key=DIAS.index)
    dias_3h = [d for d in dias if et_por_dia[d] >= minimo - 1e-9]
    horas_et = sum(et_por_dia.values())
    semana = horas_semana(pid)
    peso = horas_et / semana if semana else 0.0
    if not dias_3h and peso < tercio:
        veredicto = 'no'
    elif (dias and len(dias_3h) == len(dias)) or peso >= tercio:
        veredicto = 'sí'
    else:
        veredicto = 'revísalo con tu asesor'
    return {'horas_22_6_semana': horas_et, 'dias_trabajados': len(dias),
            'dias_con_3h_o_mas': len(dias_3h), 'peso_sobre_la_jornada': peso,
            'trabajador_nocturno_et': veredicto,
            'horas_plus_22_0': h_22_0, 'horas_plus_0_8': h_0_8,
            'dias_jornada_nocturna_convenio': sum(1 for v in conv_por_dia.values()
                                                  if v >= umbral - 1e-9)}


# ==========================================================================
# 4. PARÁMETROS (IVA por canal, aceite, producción y supuestos de C3)
# ==========================================================================
#: Cada entrada es (valor, fuente, nota). UN concepto, UNA fuente: ninguna de estas
#: claves vuelve a aparecer en otra estructura del fichero (lo vigila `comprobar()`).
PARAMS = {
    # --- Seguridad Social (heredada de la familia) ---------------------------
    'ss_empresa': (0.33, 'heredado: motor.PARAMETROS[ss_empresa]',
                   'Cotización empresarial aproximada sobre el bruto, la misma de toda la '
                   'familia. Ajústala a tus contratos.'),
    'cubrir_vacaciones_con_sustitutos': (True, 'supuesto',
                                         'Cada contrato trabaja sus horas anuales, no las 52 '
                                         'semanas: las semanas de vacaciones y de descanso por '
                                         'festivo se cubren con sustitutos al coste hora del '
                                         'escandallo. Sin esta línea, el cuadrante sólo tiene '
                                         'cero huecos en la semana tipo.'),
    # --- IVA (se explica en el cap. 03, que es donde el libro 3 lo aplica) ----
    'iva_sala': (0.10, 'CHN-71c + FC-IVA-01',
                 'Servicio de hostelería: lo que se consume en barra, sala o terraza, '
                 'bebidas incluidas, va al tipo reducido.'),
    'iva_llevar_comida': (0.10, 'FC-IVA-02',
                          'Churros y porras para llevar: entrega de un alimento.'),
    'iva_llevar_chocolate': (0.10, 'CUN-18',
                             'CELDA VERDE con aviso (V-04, rama B): «consulta a tu asesor: '
                             'con agua y un preparado azucarado podría ser el 21 %». Nunca '
                             'se afirma un tipo en la prosa (D11).'),
    'iva_llevar_bebidas': (0.10, 'CUN-18 + CHN-71c',
                           'CELDA VERDE con el mismo aviso en todas las bebidas para llevar '
                           '(leche con cacao incluida, SR-16): el refresco azucarado para '
                           'llevar va al tipo general.'),
    'iva_llevar_refresco_azucarado': (0.21, 'FC-IVA-04 + CUN-17',
                                      'Granizado y horchata PARA LLEVAR: la exclusión de las bebidas '
                                      'refrescantes con azúcares añadidos del tipo reducido desde el '
                                      '1-1-2021 los lleva al tipo general. En sala siguen al '
                                      '10 % (servicio de hostelería). CELDA VERDE: si tu receta no '
                                      'añade azúcar, consúltalo con tu asesor.'),
    'iva_general': (0.21, 'CHN-71c', 'Tipo general: equipamiento, obra, envases y servicios.'),
    'iva_compra_alimentos': (0.10, 'supuesto',
                             'IVA soportado del mix, el aceite y el preparado: compruébalo '
                             'en cada factura, el aceite ha tenido tipos rebajados '
                             'temporales.'),
    # --- masa, fritura y aceite (supuestos declarados de C3) ------------------
    'g_masa_churro': (20.0, 'supuesto', 'Gramos de masa por churro (§3.5).'),
    'g_masa_porra': (60.0, 'supuesto', 'Gramos de masa por porra (§3.5).'),
    'merma_masa_pct': (0.05, 'supuesto',
                       'Masa que se fríe y no se vende: restos, piezas rotas y el sobrante '
                       'del cierre. Se produce y se fríe igual.'),
    'kg_fritos_por_kg_masa': (0.90, 'supuesto',
                              'La masa pierde agua al freírse y gana aceite: lo que pesa la '
                              'pieza frita frente a la masa cruda. Sin fuente pública.'),
    'absorcion_aceite_pct': (0.10, 'supuesto',
                             'Supuesto, sin fuente pública; pon el tuyo. Aceite absorbido, en '
                             '% del peso frito (N-12 prohíbe usar la grasa de los churros de '
                             'maíz de un estudio como dato).'),
    'densidad_aceite_kg_l': (0.92, 'supuesto',
                             'Supuesto, sin fuente pública; pon el tuyo. Sin este factor el '
                             'libro 3 y el 4 meterían una constante dentro de la fórmula, '
                             'porque la absorción va en peso y el precio en litros.'),
    'azucar_g_por_100g_masa': (5.0, 'supuesto',
                               'Azúcar para espolvorear, por cada 100 g de masa vendida.'),
    'kg_mix_por_kg_masa': (4.0 / 11.5, 'CUS-21',
                           'El vendedor declara que cada saco de 4 kg prepara unos 11,5 kg '
                           'de masa; el resto hasta el kilo es agua, sin coste.'),
    'ml_taza': (200.0, 'supuesto', 'Mililitros de una taza de chocolate.'),
    'ml_media_taza': (120.0, 'supuesto', 'Mililitros de media taza.'),
    'cacao_seco_total_preparado_pct': (35.0, 'supuesto',
                                       'Lo que dice la etiqueta del preparado del ejemplo, '
                                       'cuya etiqueta dice «chocolate a la taza» (V-06). El '
                                       'lector copia el SUYO de la etiqueta.'),
    'preparado_con_grasa_vegetal': (False, 'supuesto',
                                    'Lo que dice la etiqueta del preparado del ejemplo.'),
    'cacao_minimo_chocolate_taza_pct': (35.0, 'CUN-42',
                                        'Cacao seco total mínimo del producto «chocolate a '
                                        'la taza» (apartado 1.11 del RD 1055/2003). Con '
                                        'menos, o con grasa vegetal, el libro 3 muestra '
                                        '«consulta a tu servicio de consumo antes de '
                                        'imprimir la carta».'),
    # --- verano, pico y refuerzo ---------------------------------------------
    'factor_hora_punta': (1.5, 'supuesto',
                          'La hora más cargada de una franja lleva un 50 % más que la media '
                          'de la franja.'),
    'dias_refuerzo_navidad_reyes': (8, 'supuesto',
                                    'Días punta de Navidad y Reyes con una persona más en la '
                                    'mañana, por encima del medio refuerzo fijo.'),
    'horas_refuerzo_dia': (7.0, 'supuesto', 'De 6:00 a 13:00.'),
    # --- plan financiero (heredados de la hermana) ---------------------------
    'meses_colchon': (6, 'heredado: guia-chocolateria/datos_ejemplo.py PARAMS[meses_colchon_fondo_maniobra]',
                      'Meses de gastos fijos de caja que hay que tener el día que abres. El '
                      'fondo de maniobra se calcula SÓLO en el libro 6 (D16).'),
    'anios_amortizacion': (10, 'heredado: guia-chocolateria/datos_ejemplo.py PARAMS[anios_amortizacion]',
                           'Vida útil contable del inmovilizado.'),
    'anio_crucero': (2, 'heredado: guia-chocolateria/datos_ejemplo.py PARAMS[anio_crucero]',
                     'El año 1 va en rampa y con carencia: la foto de un año normal es el 2.'),
    'horizonte_traspaso_anios': (5, 'heredado: guia-chocolateria/datos_ejemplo.py PARAMS[horizonte_comparacion_anios]',
                                 'Horizonte de «Traspaso vs Obra Nueva».'),
}


def P(clave):
    return PARAMS[clave][0]


#: Los dos márgenes publicados, SÓLO para contrastar en «Los Dos Márgenes» (D6). Cada
#: uno con su definición. El de El Molinete sale de su escandallo.
MARGENES_DE_CONTRASTE = [
    {'quien': 'Loomis Pay (proveedor de TPV)', 'cifra': 'márgenes superiores al 60 % en '
     'producto', 'definicion': 'margen sobre materia prima, sin método publicado',
     'fuente': 'CUS-01'},
    {'quien': 'Javier, gestor de La Artesana (Palma)', 'cifra': '«un poquito más del 50 %»',
     'definicion': 'rentabilidad declarada de palabra, no un margen sobre materia prima',
     'fuente': 'CUS-30'},
]


# ==========================================================================
# 5. INSUMOS: UN SOLO PRECIO POR INSUMO, en base imponible
# ==========================================================================
#: El precio de cada insumo se escribe UNA vez, aquí, tal y como lo trae su fuente, y
#: de aquí lo leen el escandallo, el stock inicial y el libro 4. `comprobar()` exige que
#: los números de las fichas aparezcan una sola vez en todo el código.
INSUMOS = {
    'mix_churros': {
        'nombre': 'Preparado para masa de churro (caja de 6 sacos de 4 kg)',
        'precio_formato': 34.80, 'cantidad_formato': 24.0, 'unidad': 'kg',
        'base_iva': 'sin IVA, declarada en la ficha («Impuestos excluidos»)',
        'fuente': 'CUS-21',
        'nota': ('Re-comprobar al construir el libro 3: la ficha dice «Caja 6 sacos» en una '
                 'dirección de «pack de 3 cajas», y si los 34,80 € fueran del pack el precio '
                 'por kilo estaría mal por un factor 3.')},
    'aceite': {
        'nombre': 'Aceite especial de fritura (garrafa de 25 L)',
        'precio_formato': 49.90, 'cantidad_formato': 25.0, 'unidad': 'L',
        'base_iva': 'sin IVA, declarada en la ficha («Impuestos excluidos»)',
        'fuente': 'CUS-23',
        'nota': ('El techo de las dos garrafas de la ficha. Es la CELDA ÚNICA del precio del '
                 'aceite de todo el paquete: vive en el libro 3 y la copian el 4 y el 2.')},
    'preparado_taza': {
        'nombre': 'Chocolate a la taza en polvo (bolsa de 800 g, rinde 4,3 L)',
        'precio_formato': 5.75, 'cantidad_formato': 0.8, 'unidad': 'kg',
        'rinde_l_por_formato': 4.3,
        'base_iva': 'sin IVA, declarada en la ficha («Impuestos excluidos»)',
        'fuente': 'CUS-24',
        'nota': ('El techo por kilo de la ficha. La ficha no dice a qué denominación del RD '
                 '1055/2003 corresponde: la carta usa la de la etiqueta (V-06).')},
    'cobertura': {
        'nombre': 'Cobertura de chocolate negro (1 kg)',
        'precio_formato': 6.50, 'cantidad_formato': 1.0, 'unidad': 'kg',
        'base_iva': 'sin IVA, declarada en la ficha («Impuestos excluidos»)',
        'fuente': 'CUS-24', 'nota': 'Para rellenar y bañar churros.'},
    'cucurucho': {
        'nombre': 'Cucurucho de cartón para churros (caja de 100)',
        'precio_formato': 15.00, 'cantidad_formato': 100.0, 'unidad': 'ud',
        'base_iva': 'sin IVA, inferida (celda «¿lleva IVA?» en verde, «no» por defecto)',
        'fuente': 'CUS-25',
        'nota': ('Su composición está por confirmar: no se presenta como conforme a la ley de '
                 'plásticos.')},
    'harina_mix_propio': {
        'nombre': 'Harina especial para churros (mix propio)', 'precio_formato': 0.80,
        'cantidad_formato': 1.0, 'unidad': 'kg', 'base_iva': 'supuesto, sin IVA',
        'fuente': 'supuesto',
        'nota': ('Sólo para la decisión 5: el proveedor verificado no publica precio.')},
    'sal': {'nombre': 'Sal', 'precio_formato': 0.40, 'cantidad_formato': 1.0, 'unidad': 'kg',
            'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto', 'nota': 'Mix propio.'},
    'azucar': {'nombre': 'Azúcar para espolvorear y sobres', 'precio_formato': 1.00,
               'cantidad_formato': 1.0, 'unidad': 'kg', 'base_iva': 'supuesto, sin IVA',
               'fuente': 'supuesto',
               'nota': 'El azúcar glas que publica CUS-25 es otro producto.'},
    'leche': {'nombre': 'Leche', 'precio_formato': 0.85, 'cantidad_formato': 1.0, 'unidad': 'L',
              'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto', 'nota': ''},
    'cafe': {'nombre': 'Café en grano', 'precio_formato': 18.00, 'cantidad_formato': 1.0,
             'unidad': 'kg', 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto',
             'nota': 'Sin fuente de precio de café en el research.'},
    'infusion': {'nombre': 'Infusión (sobre)', 'precio_formato': 0.06, 'cantidad_formato': 1.0,
                 'unidad': 'ud', 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto', 'nota': ''},
    'cacao_soluble': {'nombre': 'Cacao soluble', 'precio_formato': 6.00, 'cantidad_formato': 1.0,
                      'unidad': 'kg', 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto',
                      'nota': ''},
    'naranja': {'nombre': 'Naranja para zumo', 'precio_formato': 1.10, 'cantidad_formato': 1.0,
                'unidad': 'kg', 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto', 'nota': ''},
    'agua': {'nombre': 'Agua (botella de 50 cl)', 'precio_formato': 0.22, 'cantidad_formato': 1.0,
             'unidad': 'ud', 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto', 'nota': ''},
    'base_granizado': {'nombre': 'Base de granizado (por vaso)', 'precio_formato': 0.45,
                       'cantidad_formato': 1.0, 'unidad': 'ud', 'base_iva': 'supuesto, sin IVA',
                       'fuente': 'supuesto', 'nota': 'Comprada ya preparada.'},
    'horchata': {'nombre': 'Horchata a granel', 'precio_formato': 2.20, 'cantidad_formato': 1.0,
                 'unidad': 'L', 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto', 'nota': ''},
    'helado': {'nombre': 'Helado (por bola)', 'precio_formato': 0.45, 'cantidad_formato': 1.0,
               'unidad': 'ud', 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto',
               'nota': 'Comprado a un obrador: El Molinete no fabrica helado.'},
    'sirope': {'nombre': 'Sirope (por batido)', 'precio_formato': 0.05, 'cantidad_formato': 1.0,
               'unidad': 'ud', 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto', 'nota': ''},
    'vaso_llevar': {'nombre': 'Vaso de papel plastificado con tapa', 'precio_formato': 0.08,
                    'cantidad_formato': 1.0, 'unidad': 'ud', 'base_iva': 'supuesto, sin IVA',
                    'fuente': 'supuesto', 'nota': 'Lleva plástico: se cobra aparte (CUN-41).'},
    'papel_antigrasa': {'nombre': 'Papel antigrasa para sueltos', 'precio_formato': 0.02,
                        'cantidad_formato': 1.0, 'unidad': 'ud', 'base_iva': 'supuesto, sin IVA',
                        'fuente': 'supuesto', 'nota': ''},
    'caja_kilo': {'nombre': 'Caja de cartón para el kilo', 'precio_formato': 0.25,
                  'cantidad_formato': 1.0, 'unidad': 'ud', 'base_iva': 'supuesto, sin IVA',
                  'fuente': 'supuesto', 'nota': ''},
}

#: Tipo de IVA soportado de cada insumo (para el stock inicial y la tesorería).
INSUMOS_ALIMENTO = ('mix_churros', 'aceite', 'preparado_taza', 'cobertura', 'harina_mix_propio',
                    'sal', 'azucar', 'leche', 'cafe', 'infusion', 'cacao_soluble', 'naranja',
                    'agua', 'base_granizado', 'horchata', 'helado', 'sirope')


def precio_insumo(clave):
    """Precio por unidad (kg, L o ud) en base imponible."""
    i = INSUMOS[clave]
    return i['precio_formato'] / i['cantidad_formato']


def iva_compra_insumo(clave):
    return P('iva_compra_alimentos') if clave in INSUMOS_ALIMENTO else P('iva_general')


def precio_aceite_eur_l():
    return precio_insumo('aceite')


def precio_mix_eur_kg():
    return precio_insumo('mix_churros')


# ==========================================================================
# 6. LA CARTA: 24 referencias en 5 familias, con IVA declarado
# ==========================================================================
FAMILIAS = ('Churros y porras', 'Rellenos y especiales', 'Chocolate a la taza',
            'Cafés y bebidas', 'Carta de verano')
FAMILIAS_ESPERADO = {'Churros y porras': 7, 'Rellenos y especiales': 2,
                     'Chocolate a la taza': 5, 'Cafés y bebidas': 6, 'Carta de verano': 4}

#: Claves de cada referencia:
#:   id · nombre · familia · piezas (churros o porras de la unidad) · tipo_pieza
#:   · kg_fritos (sólo el kilo) · pvp (CON IVA, precio de mostrador) · fuente_pvp
#:   · anio_pvp (A8: el año va en la fila) · iva_llevar (clave de PARAMS)
#:   · pct_llevar (parte de las unidades que se venden para llevar)
#:   · mix_invierno y mix_verano (% de las unidades; cada uno suma 100)
#:   · receta (insumo, cantidad por unidad) · envase_llevar (insumo, cantidad)
#:   · cargo_vaso (si el vaso de plástico se cobra aparte al llevar, CUN-41)
#:   · alergenos (por la receta del ejemplo; el lector confirma con sus etiquetas) · nota
#: El IVA de la sala es el mismo en todas: PARAMS['iva_sala'].
#: El mix de invierno es el de septiembre a junio; el de verano, el de julio y agosto.
CARTA = [
    # ------------------------- CHURROS Y PORRAS (7) ---------------------------
    {'id': 'CH1', 'nombre': 'Ración de churros (6 uds)', 'familia': 'Churros y porras',
     'piezas': 6, 'tipo_pieza': 'churro', 'kg_fritos': None, 'pvp': 2.60,
     'fuente_pvp': 'CUS-17', 'anio_pvp': 2025, 'iva_llevar': 'iva_llevar_comida',
     'pct_llevar': 0.15, 'mix_invierno': 20.0, 'mix_verano': 12.0,
     'receta': [], 'envase_llevar': [('cucurucho', 1.0)], 'cargo_vaso': False,
     'alergenos': ('gluten',),
     'nota': ('Precio de La Artesana (Palma, 21-10-2025). Esa ración no declara el número de '
              'churros: las seis unidades son supuesto, con el formato de CUS-15.')},
    {'id': 'CH2', 'nombre': 'Media ración de churros (3 uds)', 'familia': 'Churros y porras',
     'piezas': 3, 'tipo_pieza': 'churro', 'kg_fritos': None, 'pvp': 1.40,
     'fuente_pvp': 'CUS-17', 'anio_pvp': 2025, 'iva_llevar': 'iva_llevar_comida',
     'pct_llevar': 0.0, 'mix_invierno': 4.0, 'mix_verano': 3.0,
     'receta': [], 'envase_llevar': [], 'cargo_vaso': False, 'alergenos': ('gluten',),
     'nota': 'Precio de La Artesana (Palma, 21-10-2025).'},
    {'id': 'CH3', 'nombre': 'Ración de porras (3 uds)', 'familia': 'Churros y porras',
     'piezas': 3, 'tipo_pieza': 'porra', 'kg_fritos': None, 'pvp': 2.70,
     'fuente_pvp': 'supuesto', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_comida',
     'pct_llevar': 0.25, 'mix_invierno': 6.0, 'mix_verano': 3.0,
     'receta': [], 'envase_llevar': [('cucurucho', 1.0)], 'cargo_vaso': False,
     'alergenos': ('gluten',),
     'nota': 'Supuesto: un poco por encima de la ración de churros, porque lleva más masa.'},
    {'id': 'CH4', 'nombre': 'Churro suelto', 'familia': 'Churros y porras',
     'piezas': 1, 'tipo_pieza': 'churro', 'kg_fritos': None, 'pvp': 0.30,
     'fuente_pvp': 'CUS-16', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_comida',
     'pct_llevar': 1.0, 'mix_invierno': 6.0, 'mix_verano': 4.0,
     'receta': [], 'envase_llevar': [('papel_antigrasa', 1.0)], 'cargo_vaso': False,
     'alergenos': ('gluten',),
     'nota': 'Precio de la Churrería Antonio (Vallecas, 21-09-2026).'},
    {'id': 'CH5', 'nombre': 'Porra suelta', 'familia': 'Churros y porras',
     'piezas': 1, 'tipo_pieza': 'porra', 'kg_fritos': None, 'pvp': 0.60,
     'fuente_pvp': 'CUS-16', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_comida',
     'pct_llevar': 1.0, 'mix_invierno': 3.0, 'mix_verano': 2.0,
     'receta': [], 'envase_llevar': [('papel_antigrasa', 1.0)], 'cargo_vaso': False,
     'alergenos': ('gluten',),
     'nota': 'Precio de la Churrería Antonio (Vallecas, 21-09-2026).'},
    {'id': 'CH6', 'nombre': 'Docena de churros para llevar', 'familia': 'Churros y porras',
     'piezas': 12, 'tipo_pieza': 'churro', 'kg_fritos': None, 'pvp': 3.50,
     'fuente_pvp': 'supuesto', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_comida',
     'pct_llevar': 1.0, 'mix_invierno': 6.0, 'mix_verano': 3.0,
     'receta': [], 'envase_llevar': [('cucurucho', 1.0)], 'cargo_vaso': False,
     'alergenos': ('gluten',),
     'nota': 'Supuesto: algo por debajo de doce churros sueltos.'},
    {'id': 'CH7', 'nombre': 'Kilo de churros para llevar', 'familia': 'Churros y porras',
     'piezas': None, 'tipo_pieza': 'churro', 'kg_fritos': 1.0, 'pvp': 10.00,
     'fuente_pvp': 'supuesto', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_comida',
     'pct_llevar': 1.0, 'mix_invierno': 2.0, 'mix_verano': 1.0,
     'receta': [], 'envase_llevar': [('caja_kilo', 1.0)], 'cargo_vaso': False,
     'alergenos': ('gluten',),
     'nota': ('Se vende por peso frito: la masa que pide sale de dividir el kilo entre los kg '
              'fritos por kg de masa. Es la decisión 7: el formato con menos euros por kilo.')},
    # ------------------------ RELLENOS Y ESPECIALES (2) ------------------------
    {'id': 'RE1', 'nombre': 'Churro relleno de chocolate (ud)', 'familia': 'Rellenos y especiales',
     'piezas': 1, 'tipo_pieza': 'porra', 'kg_fritos': None, 'pvp': 1.20,
     'fuente_pvp': 'supuesto', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_comida',
     'pct_llevar': 0.0, 'mix_invierno': 3.0, 'mix_verano': 2.0,
     'receta': [('cobertura', 0.020)], 'envase_llevar': [], 'cargo_vaso': False,
     'alergenos': ('gluten', 'leche', 'soja'),
     'nota': ('Una pieza del tamaño de la porra rellena con manga: El Molinete no compra '
              'rellenadora. Oferta descrita sin precios en CUS-09. Leche y soja: compruébalo '
              'en la ficha de la cobertura.')},
    {'id': 'RE2', 'nombre': 'Ración de churros con cobertura de chocolate (6 uds)',
     'familia': 'Rellenos y especiales', 'piezas': 6, 'tipo_pieza': 'churro', 'kg_fritos': None,
     'pvp': 3.50, 'fuente_pvp': 'supuesto', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_comida',
     'pct_llevar': 0.0, 'mix_invierno': 2.0, 'mix_verano': 1.0,
     'receta': [('cobertura', 0.030)], 'envase_llevar': [], 'cargo_vaso': False,
     'alergenos': ('gluten', 'leche', 'soja'), 'nota': ''},
    # ------------------------- CHOCOLATE A LA TAZA (5) ------------------------
    {'id': 'CT1', 'nombre': 'Chocolate a la taza en barra', 'familia': 'Chocolate a la taza',
     'piezas': 0, 'tipo_pieza': None, 'kg_fritos': None, 'pvp': 2.00,
     'fuente_pvp': 'CUS-15', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_chocolate',
     'pct_llevar': 0.0, 'mix_invierno': 12.0, 'mix_verano': 4.0,
     'receta': [('taza', 1.0)], 'envase_llevar': [], 'cargo_vaso': False,
     'alergenos': ('leche',),
     'nota': ('Precio de La Churrería de Granada (2026). La denominación de la carta es la '
              'de la etiqueta del preparado (V-06).')},
    {'id': 'CT2', 'nombre': 'Chocolate a la taza en terraza', 'familia': 'Chocolate a la taza',
     'piezas': 0, 'tipo_pieza': None, 'kg_fritos': None, 'pvp': 2.50,
     'fuente_pvp': 'CUS-15', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_chocolate',
     'pct_llevar': 0.0, 'mix_invierno': 4.0, 'mix_verano': 2.0,
     'receta': [('taza', 1.0)], 'envase_llevar': [], 'cargo_vaso': False,
     'alergenos': ('leche',), 'nota': 'Precio de La Churrería de Granada (2026).'},
    {'id': 'CT3', 'nombre': 'Chocolate con churros (taza y ración de 6)',
     'familia': 'Chocolate a la taza', 'piezas': 6, 'tipo_pieza': 'churro', 'kg_fritos': None,
     'pvp': 3.80, 'fuente_pvp': 'supuesto', 'anio_pvp': 2026,
     'iva_llevar': 'iva_llevar_chocolate', 'pct_llevar': 0.0, 'mix_invierno': 10.0,
     'mix_verano': 4.0, 'receta': [('taza', 1.0)], 'envase_llevar': [], 'cargo_vaso': False,
     'alergenos': ('gluten', 'leche'),
     'nota': ('Supuesto dentro del rango de 3,50-4 € con chocolate que publica CHS-32 '
              '(genérico de un proveedor de TPV).')},
    {'id': 'CT4', 'nombre': 'Chocolate a la taza para llevar', 'familia': 'Chocolate a la taza',
     'piezas': 0, 'tipo_pieza': None, 'kg_fritos': None, 'pvp': 2.20,
     'fuente_pvp': 'supuesto', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_chocolate',
     'pct_llevar': 1.0, 'mix_invierno': 3.0, 'mix_verano': 1.0,
     'receta': [('taza', 1.0)], 'envase_llevar': [('vaso_llevar', 1.0)], 'cargo_vaso': True,
     'alergenos': ('leche',),
     'nota': 'Su IVA es la celda verde del 10 % con aviso (V-04); el vaso se cobra aparte.'},
    {'id': 'CT5', 'nombre': 'Media taza de chocolate', 'familia': 'Chocolate a la taza',
     'piezas': 0, 'tipo_pieza': None, 'kg_fritos': None, 'pvp': 1.30,
     'fuente_pvp': 'supuesto', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_chocolate',
     'pct_llevar': 0.0, 'mix_invierno': 2.0, 'mix_verano': 1.0,
     'receta': [('media_taza', 1.0)], 'envase_llevar': [], 'cargo_vaso': False,
     'alergenos': ('leche',), 'nota': ''},
    # --------------------------- CAFÉS Y BEBIDAS (6) --------------------------
    {'id': 'CB1', 'nombre': 'Café solo', 'familia': 'Cafés y bebidas',
     'piezas': 0, 'tipo_pieza': None, 'kg_fritos': None, 'pvp': 1.30,
     'fuente_pvp': 'supuesto', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_bebidas',
     'pct_llevar': 0.25, 'mix_invierno': 4.0, 'mix_verano': 4.0,
     'receta': [('cafe', 0.007), ('azucar', 0.008)], 'envase_llevar': [('vaso_llevar', 1.0)],
     'cargo_vaso': True, 'alergenos': (), 'nota': 'Sin fuente de precio de café (RES §4.2).'},
    {'id': 'CB2', 'nombre': 'Café con leche', 'familia': 'Cafés y bebidas',
     'piezas': 0, 'tipo_pieza': None, 'kg_fritos': None, 'pvp': 1.60,
     'fuente_pvp': 'supuesto', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_bebidas',
     'pct_llevar': 0.40, 'mix_invierno': 6.0, 'mix_verano': 5.0,
     'receta': [('cafe', 0.007), ('leche', 0.15), ('azucar', 0.008)],
     'envase_llevar': [('vaso_llevar', 1.0)], 'cargo_vaso': True, 'alergenos': ('leche',),
     'nota': ''},
    {'id': 'CB3', 'nombre': 'Infusión', 'familia': 'Cafés y bebidas',
     'piezas': 0, 'tipo_pieza': None, 'kg_fritos': None, 'pvp': 1.40,
     'fuente_pvp': 'supuesto', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_bebidas',
     'pct_llevar': 0.0, 'mix_invierno': 1.0, 'mix_verano': 1.0,
     'receta': [('infusion', 1.0), ('azucar', 0.008)], 'envase_llevar': [], 'cargo_vaso': False,
     'alergenos': (), 'nota': ''},
    {'id': 'CB4', 'nombre': 'Leche con cacao', 'familia': 'Cafés y bebidas',
     'piezas': 0, 'tipo_pieza': None, 'kg_fritos': None, 'pvp': 1.60,
     'fuente_pvp': 'supuesto', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_bebidas',
     'pct_llevar': 0.30, 'mix_invierno': 2.0, 'mix_verano': 2.0,
     'receta': [('leche', 0.20), ('cacao_soluble', 0.015)], 'envase_llevar': [('vaso_llevar', 1.0)],
     'cargo_vaso': True, 'alergenos': ('leche',),
     'nota': 'Celda de IVA para llevar en verde, como el chocolate (SR-16).'},
    {'id': 'CB5', 'nombre': 'Zumo de naranja natural', 'familia': 'Cafés y bebidas',
     'piezas': 0, 'tipo_pieza': None, 'kg_fritos': None, 'pvp': 2.50,
     'fuente_pvp': 'supuesto', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_bebidas',
     'pct_llevar': 0.25, 'mix_invierno': 2.0, 'mix_verano': 4.0,
     'receta': [('naranja', 0.45)], 'envase_llevar': [('vaso_llevar', 1.0)], 'cargo_vaso': True,
     'alergenos': (), 'nota': ''},
    {'id': 'CB6', 'nombre': 'Agua (botella de 50 cl)', 'familia': 'Cafés y bebidas',
     'piezas': 0, 'tipo_pieza': None, 'kg_fritos': None, 'pvp': 1.20,
     'fuente_pvp': 'supuesto', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_bebidas',
     'pct_llevar': 0.50, 'mix_invierno': 2.0, 'mix_verano': 5.0,
     'receta': [('agua', 1.0)], 'envase_llevar': [], 'cargo_vaso': False, 'alergenos': (),
     'nota': ''},
    # --------------------------- CARTA DE VERANO (4) --------------------------
    {'id': 'CV1', 'nombre': 'Granizado', 'familia': 'Carta de verano',
     'piezas': 0, 'tipo_pieza': None, 'kg_fritos': None, 'pvp': 3.00,
     'fuente_pvp': 'CUS-11', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_refresco_azucarado',
     'pct_llevar': 0.40, 'mix_invierno': 0.0, 'mix_verano': 12.0,
     'receta': [('base_granizado', 1.0)], 'envase_llevar': [('vaso_llevar', 1.0)],
     'cargo_vaso': True, 'alergenos': (),
     'nota': 'Precio de la carta de helados de Chocolatería 1902 (2026).'},
    {'id': 'CV2', 'nombre': 'Horchata', 'familia': 'Carta de verano',
     'piezas': 0, 'tipo_pieza': None, 'kg_fritos': None, 'pvp': 3.00,
     'fuente_pvp': 'CUS-11', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_refresco_azucarado',
     'pct_llevar': 0.40, 'mix_invierno': 0.0, 'mix_verano': 10.0,
     'receta': [('horchata', 0.25)], 'envase_llevar': [('vaso_llevar', 1.0)], 'cargo_vaso': True,
     'alergenos': (), 'nota': 'Precio de Chocolatería 1902 (2026).'},
    {'id': 'CV3', 'nombre': 'Helado (bola)', 'familia': 'Carta de verano',
     'piezas': 0, 'tipo_pieza': None, 'kg_fritos': None, 'pvp': 2.20,
     'fuente_pvp': 'supuesto', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_comida',
     'pct_llevar': 0.0, 'mix_invierno': 0.0, 'mix_verano': 9.0,
     'receta': [('helado', 1.0)], 'envase_llevar': [], 'cargo_vaso': False,
     'alergenos': ('leche',), 'nota': 'Sin precio publicado de la bola: supuesto declarado.'},
    {'id': 'CV4', 'nombre': 'Batido', 'familia': 'Carta de verano',
     'piezas': 0, 'tipo_pieza': None, 'kg_fritos': None, 'pvp': 4.00,
     'fuente_pvp': 'CUS-11', 'anio_pvp': 2026, 'iva_llevar': 'iva_llevar_bebidas',
     'pct_llevar': 0.20, 'mix_invierno': 0.0, 'mix_verano': 5.0,
     'receta': [('leche', 0.25), ('helado', 1.0), ('sirope', 1.0)],
     'envase_llevar': [('vaso_llevar', 1.0)], 'cargo_vaso': True, 'alergenos': ('leche',),
     'nota': 'El suelo del rango de 4-4,50 € de Chocolatería 1902 (2026).'},
]

#: El vaso de plástico o de papel plastificado se cobra aparte en el ticket desde el
#: 1-1-2023 (CUN-41): fila propia de la carta, fuera de las 24 referencias.
CARGO_VASO = {'nombre': 'Vaso para llevar (plástico o papel plastificado), cobrado aparte',
              'pvp': 0.10, 'fuente_pvp': 'supuesto', 'fuente_obligacion': 'CUN-41',
              'iva': 'iva_llevar_bebidas',
              'nota': ('El importe es un supuesto: la ley obliga a cobrarlo aparte, no fija '
                       'cuánto. Su IVA, el de la bebida, en celda verde.')}

#: Las dos cantidades de chocolate de la carta («taza» y «media_taza» en las recetas).
RECETAS_CHOCOLATE = {'taza': 'ml_taza', 'media_taza': 'ml_media_taza'}


def ref(rid):
    for r in CARTA:
        if r['id'] == rid:
            return r
    raise KeyError('Referencia desconocida: %r' % rid)


def por_familia(familia):
    return [r for r in CARTA if r['familia'] == familia]


def g_por_pieza(tipo):
    return P('g_masa_churro') if tipo == 'churro' else P('g_masa_porra')


def piezas_por_kg_masa(tipo):
    return 1000.0 / g_por_pieza(tipo)


def masa_vendida_kg(r):
    """Kilos de masa que acaban en la unidad que se vende."""
    if r['kg_fritos']:
        return r['kg_fritos'] / P('kg_fritos_por_kg_masa')
    if not r['piezas']:
        return 0.0
    return r['piezas'] * g_por_pieza(r['tipo_pieza']) / 1000.0


def masa_producida_kg(r):
    """La masa que hay que producir y freír para vender la unidad: incluye la merma."""
    return masa_vendida_kg(r) / (1.0 - P('merma_masa_pct'))


def coste_masa_eur_kg(mix_propio=False):
    """Coste de un kilo de masa. Con el preparado comercial (CUS-21) o con el mix propio
    de la decisión 5, que es un ejemplo para que la comparación calcule."""
    if mix_propio:
        return sum(precio_insumo(i) * q for i, q in RECETA_MIX_PROPIO)
    return precio_mix_eur_kg() * P('kg_mix_por_kg_masa')


#: Mix propio por kilo de masa, SOLO para la decisión 5: proporciones de ejemplo, no una
#: receta. El resto hasta el kilo es agua.
RECETA_MIX_PROPIO = [('harina_mix_propio', 0.45), ('sal', 0.008)]


def escandallo_kg_masa(mix_propio=False):
    """El escandallo de UN KILO DE MASA (hoja «Escandallo por kg de Masa» del libro 3), con
    la base de IVA de cada precio. Datos de ejemplo para que las fórmulas calculen: no es
    una receta con pretensión de exactitud."""
    if mix_propio:
        lineas = [(INSUMOS[i]['nombre'], q, INSUMOS[i]['unidad'], precio_insumo(i),
                   INSUMOS[i]['base_iva'], INSUMOS[i]['fuente']) for i, q in RECETA_MIX_PROPIO]
    else:
        i = INSUMOS['mix_churros']
        lineas = [(i['nombre'], P('kg_mix_por_kg_masa'), 'kg', precio_insumo('mix_churros'),
                   i['base_iva'], i['fuente'])]
    agua = 1.0 - sum(l[1] for l in lineas)
    lineas.append(('Agua', agua, 'L', 0.0, 'sin coste', 'calculado'))
    return [{'concepto': c, 'cantidad': q, 'unidad': u, 'precio': p, 'base_iva': b, 'fuente': f,
             'importe': q * p} for c, q, u, p, b, f in lineas]


def aceite_absorbido_eur_kg_masa():
    """Euros de aceite que se lleva cada kilo de masa frita."""
    kg_aceite = P('kg_fritos_por_kg_masa') * P('absorcion_aceite_pct')
    return kg_aceite / P('densidad_aceite_kg_l') * precio_aceite_eur_l()


def coste_chocolate(ml):
    prep = INSUMOS['preparado_taza']
    kg_prep = prep['cantidad_formato'] / prep['rinde_l_por_formato'] * ml / 1000.0
    return kg_prep * precio_insumo('preparado_taza') + ml / 1000.0 * precio_insumo('leche')


def coste_receta(r):
    total = 0.0
    for insumo, q in r['receta']:
        if insumo in RECETAS_CHOCOLATE:
            total += coste_chocolate(P(RECETAS_CHOCOLATE[insumo])) * q
        else:
            total += precio_insumo(insumo) * q
    return total


def coste_materia_unidad(r, canal):
    """Materia prima de una unidad SIN el aceite: masa (con merma), azúcar, receta y, al
    llevar, el envase."""
    masa = masa_producida_kg(r) * coste_masa_eur_kg()
    azucar = masa_vendida_kg(r) * P('azucar_g_por_100g_masa') / 100.0 * precio_insumo('azucar')
    envase = 0.0
    if canal == 'llevar':
        envase = sum(precio_insumo(i) * q for i, q in r['envase_llevar'])
    return masa + azucar + coste_receta(r) + envase


def aceite_absorbido_unidad(r):
    return masa_producida_kg(r) * aceite_absorbido_eur_kg_masa()


def coste_escandallo_unidad(r, canal):
    """Lo que el P&L resta por unidad (A9): materia prima más aceite absorbido."""
    return coste_materia_unidad(r, canal) + aceite_absorbido_unidad(r)


def iva_de(r, canal):
    return P('iva_sala') if canal == 'sala' else P(r['iva_llevar'])


def pvp_sin_iva(r, canal):
    return r['pvp'] / (1.0 + iva_de(r, canal))


def ingreso_unidad(r, canal):
    """Ingreso sin IVA de una unidad; al llevar suma el vaso cobrado aparte."""
    ingreso = pvp_sin_iva(r, canal)
    if canal == 'llevar' and r['cargo_vaso']:
        ingreso += CARGO_VASO['pvp'] / (1.0 + P(CARGO_VASO['iva']))
    return ingreso


def _peso(r, temporada, canal):
    mix = r['mix_invierno'] if temporada == 'invierno' else r['mix_verano']
    if canal == 'sala':
        return mix * (1.0 - r['pct_llevar'])
    if canal == 'llevar':
        return mix * r['pct_llevar']
    return mix


def _media(fun, temporada, canal):
    pesos = [(_peso(r, temporada, canal), r) for r in CARTA]
    total = sum(w for w, _r in pesos)
    if not total:
        return 0.0
    if canal == 'total':
        return sum(w * (r['pct_llevar'] * fun(r, 'llevar') + (1.0 - r['pct_llevar']) * fun(r, 'sala'))
                   for w, r in pesos) / total
    return sum(w * fun(r, canal) for w, r in pesos) / total


def ticket_sin_iva(temporada='invierno', canal='total'):
    """Ingreso medio sin IVA por ración. En este paquete una «ración» es la unidad de venta
    media de la carta: una ración de churros, una taza, un café o una docena cuentan como
    una cada una, ponderadas por el mix."""
    return _media(ingreso_unidad, temporada, canal)


def materia_por_racion(temporada='invierno', canal='total'):
    """Coste de materia por ración, aceite absorbido incluido (cruces X5 y X11)."""
    return _media(coste_escandallo_unidad, temporada, canal)


def aceite_absorbido_por_racion(temporada='invierno'):
    return _media(lambda r, c: aceite_absorbido_unidad(r), temporada, 'total')


def kg_masa_por_racion_media(temporada='invierno'):
    """Kilos de masa producida (merma incluida) por ración media (cruces X1 y X2 bis)."""
    return _media(lambda r, c: masa_producida_kg(r), temporada, 'total')


def pct_raciones(canal, temporada='invierno'):
    total = sum(_peso(r, temporada, 'total') for r in CARTA)
    return sum(_peso(r, temporada, canal) for r in CARTA) / total


def margen_sobre_materia(temporada='invierno'):
    """El primer margen de «Los Dos Márgenes»: tras la materia prima y el aceite absorbido."""
    t = ticket_sin_iva(temporada)
    return 1.0 - materia_por_racion(temporada) / t


def euros_por_kg_masa(rid):
    """Decisión 7: euros sin IVA que deja cada kilo de masa en cada formato."""
    r = ref(rid)
    canal = 'llevar' if r['pct_llevar'] >= 0.5 else 'sala'
    return (ingreso_unidad(r, canal) - coste_escandallo_unidad(r, canal)) / masa_producida_kg(r)


def chocolate_pide_aviso():
    """V-06: con menos del 35 % de cacao seco total, o con grasa vegetal, el libro 3
    avisa antes de imprimir la carta."""
    return (P('cacao_seco_total_preparado_pct') < P('cacao_minimo_chocolate_taza_pct')
            or P('preparado_con_grasa_vegetal'))


# ==========================================================================
# 7. PRODUCCIÓN: la línea, la freidora, los kW y la demanda base (libro 1)
# ==========================================================================
#: La DEMANDA BASE nace aquí, en el libro 1 (C2): raciones del día tipo y del día punta.
#: El reparto por mes y por franja vive en el libro 5.
PRODUCCION = {
    'raciones_dia_tipo': (250, 'supuesto',
                          'De lunes a viernes. Supuesto apoyado en CUS-27: La Artesana '
                          'declara 200-300 raciones entre semana.'),
    'raciones_dia_punta': (400, 'supuesto',
                           'Sábados, domingos y festivos. Supuesto apoyado en CUS-27: unas '
                           '400 el fin de semana.'),
    'kg_masa_h_linea': (12.0, 'supuesto',
                        'Kilos de masa por hora que la línea de dosificado y fritura saca DE '
                        'VERDAD con su churrero/a. Nunca el máximo del fabricante (N-8, '
                        'CUS-26).'),
    'carga_tanda_kg': (1.0, 'supuesto', 'Kilos de masa que caben en una tanda de la freidora.'),
    'minutos_tanda': (4.0, 'supuesto', 'Minutos de una tanda, de la carga al escurrido.'),
    'kg_por_amasado': (30.0, 'CUS-35a', 'Capacidad declarada de la amasadora automática.'),
    'minutos_amasado': (20.0, 'supuesto', 'Minutos de un amasado completo.'),
    'personas_en_linea_pico': (2, 'supuesto',
                               'Personas en la línea en el pico del fin de semana: viaja al '
                               'libro 8 (cruce X6), que comprueba el cuadrante.'),
    'litros_freidora': (25.0, 'CUS-33a', 'Una sola freidora de churros de una cuba de 25 L.'),
    'tipo_aparato': ('gas', 'CUS-33a', 'La freidora del ejemplo es de gas.'),
    'kw_por_litro_freidora': (1.0, 'CUN-26', 'Las freidoras se computan a 1 kW por litro.'),
    'kw_otros_aparatos': (3.0, 'supuesto',
                          'Potencia de los demás aparatos de cocción, en celda verde: dos '
                          'chocolateras al baño maría de 1,5 kW (míralo en su placa). Qué '
                          'aparatos computan lo fija la nota de la tabla 2.1 del DB-SI: '
                          'releerla antes de construir el libro 1 y citarla en la celda.'),
    'riesgo_bajo_desde_kw': (20.0, 'CUN-26', 'Local de riesgo especial bajo: de 20 a 30 kW.'),
    'riesgo_medio_desde_kw': (30.0, 'CUN-26', 'Riesgo medio: de 30 a 50 kW.'),
    'riesgo_alto_desde_kw': (50.0, 'CUN-26',
                             'Riesgo alto por encima de 50 kW, donde la extinción automática '
                             'es obligatoria.'),
    'protege_con_extincion_automatica': (False, 'supuesto',
                                         'Celda verde. El Molinete no la instala: no la '
                                         'necesita. Si la instalaras, la cocina dejaría de '
                                         'ser local de riesgo especial (nota 2) aunque te '
                                         'seguiría aplicando la nota 3 (SR-11).'),
    'uso_hospitalario_o_residencial': (False, 'supuesto', 'Una churrería no lo es.'),
    'distancia_filtro_gas_m': (1.20, 'CUN-26', 'Filtros a más de 1,20 m del foco con gas.'),
    'distancia_filtro_parrilla_m': (1.20, 'CUN-26', 'Lo mismo si el aparato es de parrilla.'),
    'distancia_filtro_otro_m': (0.50, 'CUN-26', 'A más de 0,50 m con los demás aparatos.'),
}


def kw_computables():
    return (dato(PRODUCCION, 'litros_freidora') * dato(PRODUCCION, 'kw_por_litro_freidora')
            + dato(PRODUCCION, 'kw_otros_aparatos'))


def riesgo_cocina():
    kw = kw_computables()
    if kw > dato(PRODUCCION, 'riesgo_alto_desde_kw'):
        return 'alto'
    if kw > dato(PRODUCCION, 'riesgo_medio_desde_kw'):
        return 'medio'
    if kw > dato(PRODUCCION, 'riesgo_bajo_desde_kw'):
        return 'bajo'
    return 'no es local de riesgo especial'


def necesita_extincion_automatica():
    """Cruce X9 (1 o 0): obligatoria por encima de 50 kW. Se decide UNA vez, en el 1."""
    return 1 if kw_computables() > dato(PRODUCCION, 'riesgo_alto_desde_kw') else 0


def veredicto_nota_2():
    if (dato(PRODUCCION, 'protege_con_extincion_automatica')
            and not dato(PRODUCCION, 'uso_hospitalario_o_residencial')):
        return 'no es local de riesgo especial (nota 2 del CTE), aunque te sigue aplicando la nota (3)'
    return 'local de riesgo especial ' + riesgo_cocina()


def distancia_filtro_m():
    tipo = dato(PRODUCCION, 'tipo_aparato')
    clave = {'gas': 'distancia_filtro_gas_m', 'parrilla': 'distancia_filtro_parrilla_m'}.get(
        tipo, 'distancia_filtro_otro_m')
    return dato(PRODUCCION, clave)


def capacidades_kg_h():
    """Kilos de masa por hora que aguanta cada eslabón (hoja «Cuello de Botella»)."""
    return {'Línea de dosificado y fritura': dato(PRODUCCION, 'kg_masa_h_linea'),
            'Freidora': dato(PRODUCCION, 'carga_tanda_kg') * 60.0 / dato(PRODUCCION, 'minutos_tanda'),
            'Amasadora': dato(PRODUCCION, 'kg_por_amasado') * 60.0 / dato(PRODUCCION, 'minutos_amasado')}


def equipo_que_manda():
    cap = capacidades_kg_h()
    return min(cap, key=cap.get)


def capacidad_raciones_h():
    """Raciones por hora que aguanta el conjunto (cruce X4)."""
    return min(capacidades_kg_h().values()) / kg_masa_por_racion_media('invierno')


def kg_fritos_dia(tipo_dia):
    raciones = dato(PRODUCCION, 'raciones_dia_tipo' if tipo_dia == 'tipo' else 'raciones_dia_punta')
    return raciones * kg_masa_por_racion_media('invierno') * P('kg_fritos_por_kg_masa')


#: Ficha de visita del libro 1: los eliminatorios, en este orden (A4).
FICHA_VISITA_ELIMINATORIOS = [
    ('¿La extracción necesita proyecto?', 'CUN-35',
     'Si el conducto tiene que subir a cubierta o cruzar fachada o patio, casi siempre: '
     'licencia de obra y técnico, aunque la actividad vaya por declaración responsable.'),
    ('¿Se puede llevar un conducto a cubierta?', 'CUN-23 + CUN-24',
     'En el ejemplo de Madrid, quien cocina evacua por conducto a cubierta; la excepción de '
     'los 4 kW eléctricos no ampara una freidora de baño abierto.'),
    ('¿Hay gas, o hay que llevarlo?', 'CHN-48',
     'Gas con instalación receptora (inspección cada cinco años) o freidora eléctrica con su '
     'potencia contratada. La bombona pequeña no vale para un local (CUN-28).'),
    ('¿Aguanta la potencia y el riesgo de incendio?', 'CUN-26',
     'Freidoras a 1 kW por litro: por encima de 20 kW la cocina es local de riesgo especial.'),
]


# ==========================================================================
# 8. ACEITE: renovación, reposición y gestor (libro 4)
# ==========================================================================
#: El precio del aceite NO está aquí: vive en `INSUMOS['aceite']` (libro 3) y el 4 lo
#: recibe por el cruce X2. Tampoco la absorción ni la densidad: son de `PARAMS`.
ACEITE = {
    'dias_entre_cambios': (6, 'supuesto',
                           'Supuesto declarado. Si tienes el Pack APPCC, usa tu registro: '
                           'cuenta los días entre dos filas con «cambio de aceite».'),
    'subidas_de_precio': ((0.10, 0.20, 0.30), 'supuesto',
                          'Tres escenarios de subida del precio del aceite.'),
    'compuestos_polares_max_pct': (25.0, 'CUN-02',
                                   'El límite legal es inferior al 25 %, demostrado por el '
                                   'método del anexo 1 en laboratorio. El medidor de mano te '
                                   'dice cuándo cambiar; el 25 % se demuestra en laboratorio.'),
    'coste_gestor_mes': (0.0, 'supuesto + CUS-44h',
                         'El gestor de ejemplo recoge a cambio de obsequios, servicios '
                         'gratuitos o valoración económica: la recogida no cuesta. Lo que hay '
                         'que guardar son los justificantes de cada retirada (CUN-27).'),
}
REGISTRO_DEL_LECTOR = (F_PACK_APPCC_09_CONTROL, F_PACK_APPCC_09_RETIRADA)


def raciones_dia_medio_semana():
    t = dato(PRODUCCION, 'raciones_dia_tipo')
    p = dato(PRODUCCION, 'raciones_dia_punta')
    return (5.0 * t + 2.0 * p) / 7.0


def renovacion_litros_dia():
    return dato(PRODUCCION, 'litros_freidora') / dato(ACEITE, 'dias_entre_cambios')


def renovacion_por_racion():
    """Euros de RENOVACIÓN (el aceite que se tira al cambiar la cuba) por ración, sobre la
    ración media de la semana tipo. Cruce X12. Distinto del aceite absorbido, que ya va en
    el escandallo (X11)."""
    return renovacion_litros_dia() * precio_aceite_eur_l() / raciones_dia_medio_semana()


def reposicion_litros_dia(tipo_dia='tipo'):
    """Lo que hay que reponer cada día para que la cuba no baje: el aceite que se lleva el
    producto. Es el valor por defecto de la celda del libro 4; el lector pone el suyo y la
    fila de contraste le dice si su absorción del libro 3 es realista."""
    return kg_fritos_dia(tipo_dia) * P('absorcion_aceite_pct') / P('densidad_aceite_kg_l')


def consumo_aceite_litros_dia(tipo_dia='tipo'):
    """Lo que se compra al día: la renovación de la cuba más la reposición."""
    return renovacion_litros_dia() + reposicion_litros_dia(tipo_dia)


def litros_al_gestor_mes():
    return renovacion_litros_dia() * 365.0 / 12.0


# ==========================================================================
# 9. EQUIPAMIENTO LÍNEA A LÍNEA (libro 2)
# ==========================================================================
#: Cada línea: clave · partida · bloque (1 a 11) · precio_fuente (como lo publica la
#: ficha) · uds · base_iva ('sin IVA declarada en la ficha', 'con IVA en la ficha',
#: 'supuesto, sin IVA' o 'importe del lector') · fuente · en_b (dotación B, el local
#: con sala) · en_a (dotación A, el despacho) · en_capex (entra en el CAPEX de El
#: Molinete) · es_desde · fecha · nota. Precios de hosteleria10.com con descuento
#: vigente: RE-COMPROBAR Y FECHAR cada celda el día de construir el libro 2. Ninguna línea
#: lleva plazo de entrega: vive SÓLO en el libro 7.
EQUIPAMIENTO = [
    # --- dotación B, con precio de ficha (CUS-59 suma estas siete) ------------
    {'clave': 'freidora_gas_25l', 'partida': 'Freidora de churros de gas de 25 L (ClimaHosteleria EMPLK002)',
     'bloque': 3, 'precio_fuente': 1907.00, 'uds': 1, 'base_iva': 'sin IVA declarada en la ficha',
     'fuente': 'CUS-33a', 'en_b': True, 'en_a': False, 'en_capex': True, 'es_desde': False,
     'nota': 'Gas: le tocan los filtros a 1,20 m (CUN-26).'},
    {'clave': 'dosificadora_ch_5kg', 'partida': 'Dosificadora automática de 5 kg de masa (ClimaHosteleria CH)',
     'bloque': 3, 'precio_fuente': 1798.00, 'uds': 1, 'base_iva': 'sin IVA declarada en la ficha',
     'fuente': 'CUS-34c', 'en_b': True, 'en_a': False, 'en_capex': True, 'es_desde': False,
     'nota': ''},
    {'clave': 'amasadora_auto', 'partida': 'Amasadora automática con rascador (30 kg)',
     'bloque': 3, 'precio_fuente': 2550.00, 'uds': 1, 'base_iva': 'sin IVA declarada en la ficha',
     'fuente': 'CUS-35a', 'en_b': True, 'en_a': False, 'en_capex': True, 'es_desde': False,
     'nota': ''},
    {'clave': 'campana_1200', 'partida': 'Campana extractora de 1.200 mm con turbina y filtros',
     'bloque': 2, 'precio_fuente': 990.00, 'uds': 1, 'base_iva': 'sin IVA declarada en la ficha',
     'fuente': 'CUS-36a', 'en_b': True, 'en_a': True, 'en_capex': True, 'es_desde': False,
     'nota': 'No incluye el conducto a cubierta ni el proyecto: van en su propia línea.'},
    {'clave': 'chocolatera_mch5', 'partida': 'Chocolatera Irimar MCH-5 (5 L)',
     'bloque': 4, 'precio_fuente': 412.70, 'uds': 2, 'base_iva': 'sin IVA declarada en la ficha',
     'fuente': 'CUS-37a', 'en_b': True, 'en_a': True, 'en_capex': True, 'es_desde': False,
     'nota': 'Dos en el local con sala; una en el despacho.'},
    {'clave': 'bandeja_escurridor', 'partida': 'Bandeja escurridor de 50 × 60 cm (Inblan)',
     'bloque': 3, 'precio_fuente': 499.20, 'uds': 1, 'base_iva': 'sin IVA declarada en la ficha',
     'fuente': 'CUS-39', 'en_b': True, 'en_a': False, 'en_capex': True, 'es_desde': False,
     'nota': ''},
    {'clave': 'balanza_6kg', 'partida': 'Balanza de 6 kg (Baxtran PD LCD)',
     'bloque': 6, 'precio_fuente': 48.75, 'uds': 1, 'base_iva': 'sin IVA declarada en la ficha',
     'fuente': 'CUS-41', 'en_b': True, 'en_a': True, 'en_capex': True, 'es_desde': False,
     'nota': ''},
    # --- el medidor de polares: precio CON IVA en la ficha (SR-06) -----------
    {'clave': 'testo_270', 'partida': 'Medidor de compuestos polares Testo 270 BT',
     'bloque': 6, 'precio_fuente': 603.79, 'uds': 1, 'base_iva': 'con IVA en la ficha',
     'fuente': 'CUS-38', 'en_b': True, 'en_a': True, 'en_capex': True, 'es_desde': False,
     'nota': ('La tienda lo publica con IVA: la base imponible se calcula. Ayuda a decidir el '
              'cambio de aceite; no es la prueba legal del 25 % (CUN-02).')},
    # --- la rellenadora: sin cifra con fuente (SR-06) -------------------------
    {'clave': 'rellenadora', 'partida': 'Rellenadora de churros', 'bloque': 6,
     'precio_fuente': 0.0, 'uds': 1, 'base_iva': 'importe del lector', 'fuente': 'supuesto',
     'en_b': False, 'en_a': False, 'en_capex': True, 'es_desde': False,
     'nota': ('Sin precio con fuente: pon tu presupuesto. El Molinete rellena con manga y no '
              'la compra; por eso su importe por defecto es cero.')},
    # --- dotación A, el despacho (CUS-58) --------------------------------------
    {'clave': 'equipo_mundigas_ch1d', 'partida': 'Equipo completo de churros Mundigas CH-1-D (dosificador de 1,5 kg y caldero de 14 L)',
     'bloque': 3, 'precio_fuente': 2188.00, 'uds': 1, 'base_iva': 'sin IVA declarada en la ficha',
     'fuente': 'CUS-32a', 'en_b': False, 'en_a': True, 'en_capex': False, 'es_desde': False,
     'nota': 'La alternativa de la decisión 3: equipo completo frente a línea separada.'},
    {'clave': 'caldero_cald50', 'partida': 'Caldero amasador Inhospan CALD50', 'bloque': 3,
     'precio_fuente': 247.00, 'uds': 1, 'base_iva': 'sin IVA declarada en la ficha',
     'fuente': 'CUS-35a', 'en_b': False, 'en_a': True, 'en_capex': False, 'es_desde': False,
     'nota': 'La alternativa artesanal a la amasadora.'},
    {'clave': 'pala_amasar', 'partida': 'Pala de amasar', 'bloque': 3, 'precio_fuente': 39.00,
     'uds': 1, 'base_iva': 'sin IVA declarada en la ficha', 'fuente': 'CUS-35a', 'en_b': False,
     'en_a': True, 'en_capex': False, 'es_desde': True, 'nota': 'Precio «desde».'},
    {'clave': 'escurridor_escl', 'partida': 'Escurridor Inhospan ESCL', 'bloque': 3,
     'precio_fuente': 260.00, 'uds': 1, 'base_iva': 'sin IVA declarada en la ficha',
     'fuente': 'CUS-39', 'en_b': False, 'en_a': True, 'en_capex': False, 'es_desde': True,
     'nota': 'Precio «desde».'},
    # --- la alternativa eléctrica de la decisión 4 ----------------------------
    {'clave': 'freidora_electrica_25l', 'partida': 'Freidora de churros eléctrica de 25 L (ClimaHosteleria EMPLK003)',
     'bloque': 3, 'precio_fuente': 2053.00, 'uds': 1, 'base_iva': 'sin IVA declarada en la ficha',
     'fuente': 'CUS-33b', 'en_b': False, 'en_a': False, 'en_capex': False, 'es_desde': False,
     'nota': 'La salida eléctrica de la decisión 4: sin instalación de gas, con más potencia contratada.'},
    # --- lo que no tiene precio con fuente (CUS-43, CUS-36b): supuestos ------
    {'clave': 'conducto_cubierta', 'partida': 'Conducto de evacuación a cubierta, obra y proyecto de ventilación',
     'bloque': 2, 'precio_fuente': 9000.00, 'uds': 1, 'base_iva': 'supuesto, sin IVA',
     'fuente': 'supuesto', 'en_b': False, 'en_a': False, 'en_capex': True, 'es_desde': False,
     'nota': ('Sin precio con fuente (CUS-36b): pide presupuesto al técnico. Es la partida que '
              'decide la licencia de obra (CUN-35) y la primera fila del checklist.')},
    {'clave': 'cafetera_2g', 'partida': 'Cafetera de dos grupos', 'bloque': 4, 'precio_fuente': 4200.00,
     'uds': 1, 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto', 'en_b': False, 'en_a': False,
     'en_capex': True, 'es_desde': False, 'nota': 'Sin precio con fuente (CUS-43).'},
    {'clave': 'molinillo', 'partida': 'Molinillo de café', 'bloque': 4, 'precio_fuente': 650.00,
     'uds': 1, 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto', 'en_b': False, 'en_a': False,
     'en_capex': True, 'es_desde': False, 'nota': ''},
    {'clave': 'mostrador', 'partida': 'Mostrador y barra', 'bloque': 5, 'precio_fuente': 6500.00,
     'uds': 1, 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto', 'en_b': False, 'en_a': False,
     'en_capex': True, 'es_desde': False, 'nota': 'Sin precio con fuente (CUS-43).'},
    {'clave': 'vitrina_calefactada', 'partida': 'Vitrina calefactada', 'bloque': 5,
     'precio_fuente': 1400.00, 'uds': 1, 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto',
     'en_b': False, 'en_a': False, 'en_capex': True, 'es_desde': False, 'nota': ''},
    {'clave': 'mobiliario_sala', 'partida': 'Mesas y sillas de la sala', 'bloque': 5,
     'precio_fuente': 5500.00, 'uds': 1, 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto',
     'en_b': False, 'en_a': False, 'en_capex': True, 'es_desde': False, 'nota': ''},
    {'clave': 'mobiliario_terraza', 'partida': 'Mesas, sillas y sombrillas de la terraza', 'bloque': 5,
     'precio_fuente': 1800.00, 'uds': 1, 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto',
     'en_b': False, 'en_a': False, 'en_capex': True, 'es_desde': False, 'nota': ''},
    {'clave': 'vajilla', 'partida': 'Vajilla, tazas y menaje', 'bloque': 5, 'precio_fuente': 1500.00,
     'uds': 1, 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto', 'en_b': False, 'en_a': False,
     'en_capex': True, 'es_desde': False, 'nota': ''},
    {'clave': 'lavavajillas', 'partida': 'Lavavajillas', 'bloque': 5, 'precio_fuente': 2200.00,
     'uds': 1, 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto', 'en_b': False, 'en_a': False,
     'en_capex': True, 'es_desde': False, 'nota': ''},
    {'clave': 'frio_barra', 'partida': 'Frigorífico de barra y arcón para el helado del verano',
     'bloque': 5, 'precio_fuente': 1900.00, 'uds': 1, 'base_iva': 'supuesto, sin IVA',
     'fuente': 'supuesto', 'en_b': False, 'en_a': False, 'en_capex': True, 'es_desde': False,
     'nota': ''},
    {'clave': 'extintor_clase_f', 'partida': 'Extintor de clase F para aceites', 'bloque': 6,
     'precio_fuente': 130.00, 'uds': 1, 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto',
     'en_b': False, 'en_a': False, 'en_capex': True, 'es_desde': False,
     'nota': 'El agente tiene que ser el adecuado a la clase de fuego (CUN-38); el precio, supuesto.'},
    {'clave': 'filtrado_aceite', 'partida': 'Filtrado de aceite (filtro y portafiltros)', 'bloque': 6,
     'precio_fuente': 350.00, 'uds': 1, 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto',
     'en_b': False, 'en_a': False, 'en_capex': True, 'es_desde': False, 'nota': ''},
    {'clave': 'tpv', 'partida': 'TPV con impresora de tiques', 'bloque': 7, 'precio_fuente': 1300.00,
     'uds': 1, 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto', 'en_b': False, 'en_a': False,
     'en_capex': True, 'es_desde': False, 'nota': ''},
    {'clave': 'rotulo', 'partida': 'Rótulo de fachada', 'bloque': 7, 'precio_fuente': 1600.00,
     'uds': 1, 'base_iva': 'supuesto, sin IVA', 'fuente': 'supuesto', 'en_b': False, 'en_a': False,
     'en_capex': True, 'es_desde': False, 'nota': ''},
]


def equipo(clave):
    for e in EQUIPAMIENTO:
        if e['clave'] == clave:
            return e
    raise KeyError('Línea de equipamiento desconocida: %r' % clave)


def importe_sin_iva(e):
    """Base imponible de una línea (precio por unidades). Si la ficha publica CON IVA, se
    divide por el tipo general: sin ese paso el CAPEX sale un 21 % desviado."""
    base = e['precio_fuente']
    if e['base_iva'] == 'con IVA en la ficha':
        base = base / (1.0 + P('iva_general'))
    return round(base, 2) * e['uds']


def dotacion_b_nucleo():
    """Las siete líneas con precio de ficha del local con sala: 8.618,35 € (CUS-59)."""
    return sum(importe_sin_iva(e) for e in EQUIPAMIENTO if e['en_b'] and e['clave'] != 'testo_270')


def dotacion_b_con_testo():
    """Más el Testo: 9.117,35 € (SR-06). Sin la rellenadora, que no tiene cifra."""
    return dotacion_b_nucleo() + importe_sin_iva(equipo('testo_270'))


def dotacion_a_nucleo():
    """El despacho: 4.185,45 € (CUS-58)."""
    return sum(importe_sin_iva(e) for e in EQUIPAMIENTO if e['en_a'] and e['clave'] != 'testo_270'
               and e['clave'] != 'chocolatera_mch5') + equipo('chocolatera_mch5')['precio_fuente']


def dotacion_a_con_testo():
    """El despacho con el Testo: 4.684,45 €."""
    return dotacion_a_nucleo() + importe_sin_iva(equipo('testo_270'))


# ==========================================================================
# 10. CAPEX POR BLOQUE (libro 2), SIN FONDO DE MANIOBRA
# ==========================================================================
#: Once bloques (§3.4). El fondo de maniobra NO es un bloque ni una fila de este libro:
#: se calcula SÓLO en el libro 6 (D16) y por eso aquí no aparece (lo vigila
#: `comprobar()`). Los bloques 2 a 7 suman las líneas de `EQUIPAMIENTO` de El Molinete;
#: los demás, las partidas de `CAPEX_PARTIDAS`.
BLOQUES_CAPEX = {
    1: 'Obra civil y acondicionamiento',
    2: 'Extracción y conducto',
    3: 'Fritura, dosificación y amasado',
    4: 'Chocolate y café',
    5: 'Barra, sala y terraza',
    6: 'Control y seguridad',
    7: 'TPV y rótulo',
    8: 'Licencias, proyecto de actividad y tasas',
    9: 'Fianza y garantías',
    10: 'Stock inicial y envase',
    11: 'Marketing de apertura',
}

#: Partidas que no son equipamiento. (bloque, partida, importe sin IVA, tipo de IVA
#: (clave de PARAMS o None si no lleva), fuente, amortizable, nota). Los importes a None
#: se calculan.
CAPEX_PARTIDAS = [
    (1, 'Obra y acondicionamiento del local en bruto (380 €/m²)', None, 'iva_general', 'supuesto', True,
     'Supuesto declarado: ninguna ficha publica un coste de obra por m² de churrería. Se '
     'calcula con los m² de NEGOCIO.'),
    (8, 'Proyecto técnico de actividad y de la extracción', 4200.0, 'iva_general', 'supuesto', True,
     'Supuesto declarado. Nunca la horquilla de licencias de nuestro post (N-4).'),
    (8, 'Licencia de obra del conducto y tasas municipales', 1900.0, None, 'supuesto', True,
     'Las tasas no llevan IVA y cambian en cada ayuntamiento: es la cifra que hay que ir a '
     'buscar, no copiar.'),
    (8, 'Sistema automático de extinción en la campana (sólo si X9 = 1)', 2800.0, 'iva_general',
     'supuesto', True,
     'Obligatorio por encima de 50 kW. El Molinete no lo necesita (cruce X9 = 0) y la línea '
     'suma cero; es la otra salida de la decisión 4, con su coste (SR-11).'),
    (9, 'Fianza y garantías (meses de fianza por la renta)', None, None, 'calculado', False,
     'No es un gasto: se recupera. Por eso no se amortiza.'),
    (10, 'Stock inicial de mix, aceite, preparado, envase y bebida', None, None, 'calculado', False,
     'Se calcula con los precios de los insumos (el aceite y el mix llegan por el cruce X17) '
     'y las cantidades de STOCK_INICIAL.'),
    (11, 'Marketing de apertura', 2000.0, 'iva_general', 'supuesto', False,
     'Gasto del primer año, no inmovilizado.'),
]
OBRA_EUR_M2 = (380.0, 'supuesto', 'Coste de obra y acondicionamiento por m² de local en bruto.')

#: Cantidades del stock inicial (supuestos), a los precios de INSUMOS.
STOCK_INICIAL = [
    ('mix_churros', 96.0), ('aceite', 75.0), ('preparado_taza', 8.0), ('cobertura', 5.0),
    ('cucurucho', 1000.0), ('vaso_llevar', 500.0), ('papel_antigrasa', 1000.0), ('caja_kilo', 100.0),
    ('cafe', 6.0), ('leche', 60.0), ('azucar', 25.0), ('cacao_soluble', 3.0), ('infusion', 100.0),
    ('agua', 120.0),
]


def stock_inicial_sin_iva():
    return sum(precio_insumo(i) * q for i, q in STOCK_INICIAL)


def _importe_partida(p):
    bloque, partida, importe = p[0], p[1], p[2]
    if partida.startswith('Obra y acondicionamiento'):
        return OBRA_EUR_M2[0] * dato(NEGOCIO, 'm2_total')
    if partida.startswith('Fianza'):
        return dato(NEGOCIO, 'meses_fianza') * dato(NEGOCIO, 'renta_mensual')
    if partida.startswith('Stock inicial'):
        return stock_inicial_sin_iva()
    if partida.startswith('Sistema automático de extinción'):
        return importe if necesita_extincion_automatica() else 0.0
    return importe


def capex_bloque(n):
    equipos = sum(importe_sin_iva(e) for e in EQUIPAMIENTO if e['en_capex'] and e['bloque'] == n)
    partidas = sum(_importe_partida(p) for p in CAPEX_PARTIDAS if p[0] == n)
    return equipos + partidas


def capex_total():
    """El CAPEX de El Molinete, SIN fondo de maniobra (cruce X10 al libro 6)."""
    return sum(capex_bloque(n) for n in BLOQUES_CAPEX)


def capex_amortizable():
    total = sum(importe_sin_iva(e) for e in EQUIPAMIENTO if e['en_capex'])
    total += sum(_importe_partida(p) for p in CAPEX_PARTIDAS if p[5])
    return total


def iva_soportado_capex():
    """IVA que hay que adelantar el día que abres y que vuelve después."""
    total = sum(importe_sin_iva(e) * P('iva_general') for e in EQUIPAMIENTO if e['en_capex'])
    for p in CAPEX_PARTIDAS:
        if p[3] and not p[1].startswith('Stock'):
            total += _importe_partida(p) * P(p[3])
    total += sum(precio_insumo(i) * q * iva_compra_insumo(i) for i, q in STOCK_INICIAL)
    return total


#: La única referencia de contraste que publica la hoja de instrucciones del libro 2: la
#: dotación completa que declara el traspaso de Vallecas para un local de 74 m².
DOTACION_COMPLETA_DECLARADA = (50000.0, 'CUS-02',
                               'Equipos «valorados en 50.000 €» incluidos en el traspaso: '
                               'freidora, dosificadores, calientachocolates, cafetera, '
                               'campana, frío y TPV. Es declaración del anunciante.')


def equipamiento_y_mobiliario():
    """Bloques 2 a 7: lo que se compara con la dotación completa declarada."""
    return sum(capex_bloque(n) for n in range(2, 8))


# ==========================================================================
# 11. VARIANTES DEL FORMATO (D2): local con sala · despacho · caseta · franquicia
# ==========================================================================
#: Cuatro columnas de escenario en «Variante del Formato» del libro 2. Sólo el local
#: con sala es caso cifrado; la caseta remite al food truck y no lleva caso.
VARIANTES = {
    'local_con_sala': {
        'nombre': 'Local con sala, terraza y despacho a calle (el caso de El Molinete)',
        'dotacion_con_fuente': 'dotacion_b_con_testo', 'm2': '75 m²',
        'regimen': ('Con mesas (676 o 673) la actividad sale del Anexo de la Ley 12/2012: '
                    'manda tu ayuntamiento. Las obras con proyecto, con su licencia.'),
        'fuente': 'CUS-59 + CUN-35 + CHN-49c', 'caso_cifrado': True},
    'despacho': {
        'nombre': 'Despacho para llevar', 'dotacion_con_fuente': 'dotacion_a_con_testo',
        'm2': '25-40 m²',
        'regimen': ('La ACTIVIDAD del despacho (644.6, hasta 750 m²) va por declaración '
                    'responsable; las obras que requieren proyecto, el conducto a cubierta '
                    'incluido, siguen necesitando su licencia y su técnico.'),
        'fuente': 'CUS-58 + CUN-35 + CUN-09', 'caso_cifrado': False},
    'caseta': {
        'nombre': 'Caseta, remolque o carrito de feria',
        'equipos': [('Remolque de 3 × 2 × 2,10 m con cartel', 14800.0),
                    ('Mini carrito para eventos y mercados', 6190.0),
                    ('Churrería portátil para exteriores de cafeterías', 4190.0)],
        'm2': 'el del puesto',
        'regimen': ('663.1 si sólo vende masas fritas (CUN-11); 675 o 674.7 con mesas '
                    '(CUN-13). La bombona de menos de 15 kg sólo libra de la instalación '
                    'receptora a un aparato de utilización móvil (CUN-28).'),
        'remite_a': ('plan-negocio-food-truck', 'kit-tareas-food-truck'),
        'fuente': 'CUS-42 + CUN-11 + CUN-13 + CUN-28', 'caso_cifrado': False},
    'franquicia': {
        'nombre': 'Franquicia', 'ver': 'FRANQUICIAS', 'm2': 'el que pida la enseña',
        'regimen': 'El de su formato, más el contrato de franquicia.',
        'fuente': 'CUS-M12 + CUS-M14 + CUS-M15', 'caso_cifrado': False},
}

#: Lo que queda fuera del comparador, con una línea cada uno (D2 e y f).
VARIANTES_FUERA = [
    ('Churros en una cafetería o un bar', 'Epígrafe con remisión al Plan de Negocio de '
     'Cafetería: la churrería es una línea más de su carta.', 'plan-negocio-cafeteria'),
    ('Obrador que sirve a otros negocios', 'Fuera del producto: si fabricas para otros dejas de '
     'ser minorista (419.3, CUN-12; la churrería que sirve a la cafetería, CUN-30).', ''),
]


# ==========================================================================
# 12. FRANQUICIAS: orden de magnitud publicado y FECHADO, sin recomendar marca
# ==========================================================================
#: Declarado por el franquiciador vía agregador, sin fecha de dato por marca: es orden de
#: magnitud, no precio de contrato. Fecha de consulta: 03-10-2026. De Maestro Churrero
#: sólo entra la inversión que publica CUS-M14 (la otra cifra que circula está vetada).
FRANQUICIAS = [
    {'marca': 'Chocolaterías Valor', 'inversion': 125000.0, 'que_incluye': 'local en bruto con obra, maquinaria y mobiliario',
     'canon': 24040.0, 'royalty_pct': 5.0, 'locales': '39 (32 franquiciados)', 'fuente': 'CUS-M12 + CUS-03'},
    {'marca': 'Maestro Churrero', 'inversion': 115000.0, 'que_incluye': 'inversión inicial «desde»',
     'canon': 15000.0, 'royalty_pct': 5.0, 'locales': None, 'fuente': 'CUS-M14',
     'nota': 'Más un 1 % de canon publicitario.'},
    {'marca': 'Churros Factory', 'inversion': 45000.0, 'que_incluye': 'inversión total',
     'canon': 12000.0, 'royalty_pct': 6.0, 'locales': None, 'fuente': 'CUS-M15',
     'nota': 'Contrato de 10 años renovables.'},
    {'marca': 'Madrid1883', 'inversion': 96000.0, 'que_incluye': 'inversión total aproximada',
     'canon': 20000.0, 'royalty_pct': 4.0, 'locales': None, 'fuente': 'CUS-M16',
     'nota': 'Más un 2 % de publicidad. Su facturación esperada es proyección: no entra.'},
    {'marca': 'Pinocho Churros Gourmet', 'inversion': 73000.0, 'que_incluye': 'inversión total según el dossier (58.000 € de capital propio)',
     'canon': None, 'royalty_pct': None, 'locales': '10 implantaciones', 'fuente': 'CUS-M17 + CUS-14',
     'nota': 'El objetivo de expansión del franquiciador no es un dato.'},
    {'marca': "Tejeringo's Coffee", 'inversion': 320000.0, 'que_incluye': 'inversión aproximada más IVA, canon incluido',
     'canon': 20000.0, 'royalty_pct': None, 'locales': None, 'fuente': 'CUS-M18'},
    {'marca': 'Kukuchurro', 'inversion': 75000.0, 'que_incluye': 'inversión inicial «desde», más IVA, canon incluido',
     'canon': 15000.0, 'royalty_pct': None, 'locales': None, 'fuente': 'CUS-M19'},
    {'marca': 'ChurroWay', 'inversion': 75000.0, 'que_incluye': 'inversión inicial «desde», sin IVA, fianzas ni existencias',
     'canon': 15000.0, 'royalty_pct': None, 'locales': None, 'fuente': 'CUS-M20'},
    {'marca': 'Churritopping', 'inversion': 42600.0, 'que_incluye': 'inversión inicial aproximada, sin la obra',
     'canon': None, 'royalty_pct': 5.0, 'locales': None, 'fuente': 'CUS-M21',
     'nota': 'Más un 2 % de publicidad.'},
    {'marca': 'King Churro', 'inversion': 20000.0, 'que_incluye': 'inversión inicial «desde» (hasta 25.000 €)',
     'canon': None, 'royalty_pct': None, 'locales': None, 'fuente': 'CUS-M22'},
    {'marca': 'Churro Planet', 'inversion': 44000.0, 'que_incluye': 'inversión «desde», sin la obra, canon de 5.000 € incluido',
     'canon': 5000.0, 'royalty_pct': None, 'locales': None, 'fuente': 'CUS-D6'},
    {'marca': 'ChurroFácil', 'inversion': 6000.0, 'que_incluye': '«franquicia» desde: el negocio de la marca es vender mezcla, máquinas y remolques',
     'canon': None, 'royalty_pct': None, 'locales': None, 'fuente': 'CUS-M23'},
]
ETIQUETA_FRANQUICIAS = ('Orden de magnitud publicado por el franquiciador a través de un '
                        'agregador, consultado el 03-10-2026: no es precio de contrato ni '
                        'una recomendación de marca.')


# ==========================================================================
# 13. TRASPASOS: precios PEDIDOS, no pagados (D15)
# ==========================================================================
#: El techo con sala son los 82.000 € pedidos y negociables de Vallecas (CUS-02). Los
#: anuncios reeditados durante años no entran en ningún rango (D15).
TRASPASOS = [
    {'zona': 'Granada capital', 'tipo': 'Churrería, bocadillería, patatas asadas y kebab', 'm2': 80,
     'precio_pedido': 19500.0, 'fuente': 'CUS-31a', 'fiabilidad': 'media', 'nota': 'Publicado hace unas horas.'},
    {'zona': 'Granada (Zaidín)', 'tipo': 'Churrería y patatas asadas, por jubilación', 'm2': 60,
     'precio_pedido': 16000.0, 'fuente': 'CUS-31b', 'fiabilidad': 'media',
     'nota': 'El único con motivo declarado.'},
    {'zona': 'Granada (centro)', 'tipo': 'Cafetería-churrería en funcionamiento', 'm2': 70,
     'precio_pedido': 40000.0, 'fuente': 'CUS-31c', 'fiabilidad': 'media',
     'nota': 'Seis meses sin venderse: el precio pedido no se cierra.'},
    {'zona': 'Granada (Genil)', 'tipo': 'Cafetería y churrería', 'm2': 70, 'precio_pedido': 40000.0,
     'fuente': 'CUS-31d', 'fiabilidad': 'media', 'nota': 'Casi cuatro meses publicado.'},
    {'zona': 'Montefrío (Granada)', 'tipo': 'Heladería y churrería', 'm2': 105, 'precio_pedido': 65000.0,
     'fuente': 'CUS-31e', 'fiabilidad': 'media', 'nota': 'Helado en verano, churro en invierno.'},
    {'zona': 'Ibiza', 'tipo': 'Heladería y churrería', 'm2': 120, 'precio_pedido': 60000.0,
     'fuente': 'CUS-31f', 'fiabilidad': 'baja', 'nota': 'Sin URL: sólo como orden de magnitud.'},
    {'zona': 'Valdemoro (Madrid)', 'tipo': 'Cafetería-churrería en el centro', 'm2': 240,
     'precio_pedido': 65000.0, 'fuente': 'CUS-31g', 'fiabilidad': 'media',
     'nota': 'Tres anuncios del mismo local: cuenta uno.'},
    {'zona': 'Madrid (Vallecas)', 'tipo': 'Churrería-chocolatería con sala', 'm2': 74,
     'precio_pedido': 82000.0, 'fuente': 'CUS-02', 'fiabilidad': 'media',
     'nota': ('Precio pedido y negociable, con los equipos declarados de DOTACION_COMPLETA_'
              'DECLARADA incluidos y la misma renta que El Molinete. Lectura de L4, no '
              're-verificada por el captcha: se reabre antes de publicar (SR-10).')},
]
#: Supuestos de la alternativa de la decisión 2 (traspaso frente a obra nueva).
TRASPASO_ALTERNATIVA = {
    'adaptacion': (6000.0, 'supuesto', 'Lo que habría que gastar para adaptar el local traspasado.'),
    'meses_hasta_abrir': (3, 'supuesto', 'Un traspaso en marcha abre antes que una obra nueva.'),
}


def rango_traspasos(fuentes):
    precios = [t['precio_pedido'] for t in TRASPASOS if t['fuente'] in fuentes]
    return min(precios), max(precios)


# ==========================================================================
# 14. TEMPORADA: doce coeficientes supuestos, media 1,00 (libro 5)
# ==========================================================================
#: Supuestos declarados con la forma cualitativa de CUS-29 y CUS-V17: pico de octubre a
#: marzo con Navidad arriba y valle en julio y agosto. La serie de búsquedas no vale.
COEFICIENTES_MES = (1.25, 1.15, 1.10, 0.95, 0.85, 0.70, 0.55, 0.50, 0.80, 1.10, 1.30, 1.75)
FUENTE_COEFICIENTES = 'supuesto'
MESES_PICO = (10, 11, 12, 1, 2, 3)
MESES_VERANO = (7, 8)

#: Las tres salidas del verano (D14), que el libro 5 compara por CONTRIBUCIÓN en euros:
#: los fijos son los mismos en las tres y los resta el libro 6.
SALIDAS_VERANO = ('cerrar', 'carta de verano', 'ferias')
SALIDA_VERANO_ELEGIDA = 'carta de verano'

#: Todo lo de la temporada en una vista (los mismos objetos, sin copiar ningún valor).
TEMPORADA = {
    'coeficientes': COEFICIENTES_MES, 'fuente': FUENTE_COEFICIENTES,
    'meses_pico': MESES_PICO, 'meses_verano': MESES_VERANO,
    'salidas_verano': SALIDAS_VERANO, 'salida_elegida': SALIDA_VERANO_ELEGIDA,
    'nota': ('Doce supuestos declarados con media 1,00: pico de octubre a marzo con Navidad '
             'arriba y valle en julio y agosto. Las tres salidas del verano se comparan por '
             'contribución en euros; ninguna reducción del IAE entra en el cálculo (D14).'),
}


def raciones_anio():
    """Raciones de un año de crucero: días tipo y días punta por su demanda base."""
    abiertos = dias_apertura_anio()
    punta = 104 + dato(NEGOCIO, 'festivos_entre_semana')
    tipo = abiertos - punta
    return tipo * dato(PRODUCCION, 'raciones_dia_tipo') + punta * dato(PRODUCCION, 'raciones_dia_punta')


def raciones_mes(mes):
    return raciones_anio() * COEFICIENTES_MES[mes - 1] / 12.0


def raciones_verano():
    return sum(raciones_mes(m) for m in MESES_VERANO)


def demanda_hora_punta_domingo(mes):
    """Raciones por hora en la hora punta del desayuno del domingo de ese mes."""
    desayuno = FRANJAS[0]
    a, b = desayuno['tramos']['D']
    raciones = dato(PRODUCCION, 'raciones_dia_punta') * COEFICIENTES_MES[mes - 1]
    return raciones * pct_franja(desayuno, 'D') / 100.0 / (b - a) * P('factor_hora_punta')


def cola_del_domingo(mes):
    """Raciones por hora que la línea no llega a servir en la hora punta del domingo."""
    return max(0.0, demanda_hora_punta_domingo(mes) - capacidad_raciones_h())


def horas_refuerzo_pico():
    """Cruce X7: horas de refuerzo de Navidad y Reyes, por encima del medio fijo."""
    return P('dias_refuerzo_navidad_reyes') * P('horas_refuerzo_dia')


# ==========================================================================
# 15. CANALES: sala, para llevar y ferias
# ==========================================================================
#: Mix de canales en % de las raciones (supuesto declarado, sin fuente cuantitativa).
#: El de sala y para llevar sale de la carta (cada referencia declara qué parte se lleva)
#: y `comprobar()` exige que dé 70/30 en invierno. Ferias: cero, porque El Molinete elige
#: la carta de verano (decisión 9).
CANALES = [
    {'canal': 'Sala (barra, mesas y terraza)', 'clave': 'sala', 'pct_raciones': 70.0, 'fuente': 'supuesto'},
    {'canal': 'Para llevar (despacho a calle)', 'clave': 'llevar', 'pct_raciones': 30.0, 'fuente': 'supuesto'},
    {'canal': 'Ferias', 'clave': 'ferias', 'pct_raciones': 0.0, 'fuente': 'supuesto'},
]


# ==========================================================================
# 16. FERIAS: el método del punto muerto por evento (libro 5), sin caso cifrado
# ==========================================================================
#: Eventos de EJEMPLO (D2: método, no caso). Todo supuesto declarado. El ticket de feria
#: es otro concepto que el del local: la carta y el precio de un puesto no son los de la
#: barra. La materia por ración es la del canal para llevar (cruce X5). Ninguno entra en
#: el año de El Molinete (`va` = False): por eso el resultado anual de ferias es cero.
FERIAS = [
    {'id': 'E1', 'evento': 'Feria local de cinco días (tasa fija)', 'mes': 8, 'dias': 5, 'horas_dia': 10.0,
     'tasa_fija': 450.0, 'tasa_m2_dia': 0.0, 'm2': 12.0, 'desplazamiento': 120.0, 'montaje': 300.0,
     'personas': 2, 'horas_personal_extra': 50.0, 'afluencia_h': 250.0, 'conversion': 0.06,
     'raciones_por_compra': 1.5, 'ticket_feria': 3.00, 'va': False, 'fuente': 'supuesto'},
    {'id': 'E2', 'evento': 'Fiestas patronales de tres días (tasa por m² y día)', 'mes': 7, 'dias': 3,
     'horas_dia': 12.0, 'tasa_fija': 0.0, 'tasa_m2_dia': 5.0, 'm2': 12.0, 'desplazamiento': 60.0,
     'montaje': 200.0, 'personas': 2, 'horas_personal_extra': 36.0, 'afluencia_h': 300.0,
     'conversion': 0.05, 'raciones_por_compra': 1.4, 'ticket_feria': 3.00, 'va': False, 'fuente': 'supuesto'},
    {'id': 'E3', 'evento': 'Mercado navideño de quince días (tasa fija)', 'mes': 12, 'dias': 15,
     'horas_dia': 8.0, 'tasa_fija': 900.0, 'tasa_m2_dia': 0.0, 'm2': 9.0, 'desplazamiento': 150.0,
     'montaje': 400.0, 'personas': 2, 'horas_personal_extra': 120.0, 'afluencia_h': 200.0,
     'conversion': 0.07, 'raciones_por_compra': 1.3, 'ticket_feria': 2.80, 'va': False, 'fuente': 'supuesto'},
    {'id': 'E4', 'evento': 'Romería de dos días (tasa fija)', 'mes': 5, 'dias': 2, 'horas_dia': 14.0,
     'tasa_fija': 250.0, 'tasa_m2_dia': 0.0, 'm2': 15.0, 'desplazamiento': 90.0, 'montaje': 250.0,
     'personas': 3, 'horas_personal_extra': 56.0, 'afluencia_h': 400.0, 'conversion': 0.05,
     'raciones_por_compra': 1.5, 'ticket_feria': 3.00, 'va': False, 'fuente': 'supuesto'},
]

#: Referencias reales, sólo para leer el orden de las cosas y nunca como orden de
#: magnitud nacional.
FERIAS_REFERENCIAS = [
    {'que': 'Fallas de Valencia 2026', 'dato': '146 puestos de churros autorizados, abiertos 17 días (del 2 al 19 de marzo)',
     'fuente': 'CUS-29'},
    {'que': 'Ochavillo del Río (Córdoba)', 'dato': 'tasa por toda la feria para churrerías con terraza; ejemplo de un pueblo pequeño, nunca un orden de magnitud',
     'fuente': 'CUN-37'},
]


def raciones_evento(e):
    return e['afluencia_h'] * e['horas_dia'] * e['dias'] * e['conversion'] * e['raciones_por_compra']


def resultado_evento(e):
    """Contribución de un evento en euros: ventas sin IVA menos materia, tasas,
    desplazamiento, montaje y el personal que se contrata sólo para él."""
    raciones = raciones_evento(e)
    ventas = raciones * e['ticket_feria'] / (1.0 + P('iva_llevar_comida'))
    materia = raciones * materia_por_racion('invierno', 'llevar')
    tasa = e['tasa_fija'] + e['tasa_m2_dia'] * e['m2'] * e['dias']
    personal = e['horas_personal_extra'] * coste_hora_mano_obra()
    return ventas - materia - tasa - e['desplazamiento'] - e['montaje'] - personal


def orden_eventos():
    """Orden de los eventos por resultado, como lo hará el libro 5 con COUNTIF (nunca
    RANK): un evento va primero si ningún otro le gana."""
    res = dict((e['id'], resultado_evento(e)) for e in FERIAS)
    return sorted(res, key=lambda k: (sum(1 for v in res.values() if v > res[k]), k))


def resultado_anual_ferias():
    """Cruce X14: la línea de ferias del libro 6. Cero en El Molinete."""
    return sum(resultado_evento(e) for e in FERIAS if e['va'])


def contribucion_verano(salida):
    """Contribución de julio y agosto de cada salida, en euros (cruce X16 para la
    elegida). Los fijos son los mismos en las tres y los resta el libro 6."""
    if salida == 'cerrar':
        return 0.0
    if salida == 'carta de verano':
        return raciones_verano() * (ticket_sin_iva('verano') - materia_por_racion('verano'))
    if salida == 'ferias':
        return sum(resultado_evento(e) for e in FERIAS if e['mes'] in MESES_VERANO)
    raise KeyError(salida)


# ==========================================================================
# 17. GASTOS FIJOS MENSUALES (libro 6; nacen sólo allí)
# ==========================================================================
#: Supuestos declarados (SR-13), cada uno con su razonamiento. La renta (X18) y la
#: plantilla (X15) no están aquí: llegan por sus cruces. «Heredado» no vale para los
#: suministros: el consumo de una freidora no se parece al de una bombonería.
GASTOS_FIJOS_MENSUALES = [
    ('Suministros: gas de la freidora', 170.0, 'supuesto',
     'Una freidora de gas de 25 L encendida dos turnos al día. Pide la simulación a la '
     'comercializadora con la potencia del proyecto.'),
    ('Suministros: electricidad', 320.0, 'supuesto',
     'Chocolateras, cafetera, extracción, frío y luz, con la potencia contratada.'),
    ('Suministros: agua', 45.0, 'supuesto', ''),
    ('Limpieza de conductos y campana', 60.0, 'supuesto + CUN-23',
     'Dos limpiezas al año prorrateadas. En el ejemplo de Madrid la ordenanza pide al menos '
     'una al año.'),
    ('Mantenimiento de equipos y revisión del gas', 90.0, 'supuesto + CHN-48',
     'Incluye la parte de la inspección periódica de la instalación receptora de gas, cada '
     'cinco años.'),
    ('Seguros (multirriesgo y responsabilidad civil)', 75.0, 'supuesto',
     'El seguro de responsabilidad civil va sin cifra con fuente, como en la hermana.'),
    ('Asesoría laboral, fiscal y contable', 190.0, 'supuesto', 'Cuatro nóminas y la contabilidad.'),
    ('TPV, facturación y comisiones del datáfono', 110.0, 'supuesto + CHN-75',
     'Con Verifactu en el horizonte: 2027, no 2026.'),
    ('Gestor de aceite usado', 0.0, 'supuesto + CUS-44h',
     'La recogida no cuesta: el gestor de ejemplo recoge gratis o con valoración. Lo que '
     'cuesta es no guardar los justificantes (CUN-27).'),
    ('Telefonía e internet', 50.0, 'supuesto', ''),
    ('Limpieza, papel y consumibles', 160.0, 'supuesto', ''),
    ('Publicidad y redes', 120.0, 'supuesto', ''),
    ('Tasas municipales de basuras y terraza', 60.0, 'supuesto',
     'La terraza paga su propia tasa por ocupar la vía pública.'),
    ('Cuota de autónomos del titular', 320.0,
     'heredado: guia-chocolateria/datos_ejemplo.py GASTOS_FIJOS_MENSUALES[Cuota de autónomos del titular]',
     'Su retribución ya va en el coste de plantilla: aquí sólo su cuota.'),
    ('Otros gastos de estructura', 100.0, 'supuesto', ''),
]


def gastos_fijos_mes():
    return sum(g[1] for g in GASTOS_FIJOS_MENSUALES)


# ==========================================================================
# 18. FINANCIACIÓN (heredada de la hermana) y principal como punto fijo
# ==========================================================================
_H_FIN = 'heredado: guia-chocolateria/datos_ejemplo.py FINANCIACION'
FINANCIACION = {
    'pct_recursos_propios': (0.40, _H_FIN + '[pct_recursos_propios]', ''),
    'pct_prestamo': (0.60, _H_FIN + '[pct_prestamo]', ''),
    'tipo_nominal': (0.062, _H_FIN + '[tipo_nominal]', ''),
    'plazo_meses': (84, _H_FIN + '[plazo_meses]', ''),
    'carencia_meses': (6, _H_FIN + '[carencia_meses]', ''),
}
#: Rampa de arranque heredada: el primer mes al 55 % y seis meses hasta el 100 %.
RAMPA = {'mes1': (0.55, 'heredado: guia-chocolateria/datos_ejemplo.py RAMPA[mes1]', ''),
         'meses': (6, 'heredado: guia-chocolateria/datos_ejemplo.py RAMPA[meses]', '')}


def rampa_mensual():
    m1, n = dato(RAMPA, 'mes1'), dato(RAMPA, 'meses')
    return tuple(min(1.0, m1 + (1.0 - m1) * i / float(max(1, n - 1))) for i in range(12))


# ==========================================================================
# 19. PROVEEDORES VERIFICADOS (sólo con URL abierta)
# ==========================================================================
PROVEEDORES = [
    # (nombre, qué ofrece, URL, fuente, nota)
    ('Churrofácil CB (Linares, Jaén)', 'Mix de churros y porras, aceite, chocolate en polvo, cucuruchos, maquinaria y remolques',
     'https://www.churrofacil.com/', 'CUS-44a',
     'Precios publicados sin IVA: de aquí salen el mix, el aceite, el preparado y el cucurucho. '
     'Da formación con la maquinaria.'),
    ('Harinas Sánchez Palencia', 'Harina especial para churros (sin precio publicado)',
     'https://www.harinassp.es/', 'CUS-44b', ''),
    ('Fabricantes de maquinaria: Inblan, J.L. Blanco, Inhospan, Mundigas, Repagas y NTGAS',
     'Churreras, freidoras, dosificadoras, amasadoras y chocolateras',
     'https://www.inblan.com/maquinaria-para-churreria/', 'CUS-44e',
     'Inblan no publica precios; los demás aparecen con precio en el listado de un distribuidor.'),
    ('HostelShop España', 'Maquinaria para churrerías (sin precios en la página)',
     'https://hostelshopespana.com/maquinaria-de-hosteleria-para-churrerias/', 'CUS-44f', ''),
    ('Reseave (Mejorada del Campo, Madrid)', 'Gestor autorizado de aceite de cocina usado',
     'https://www.reseave.es/', 'CUS-44h',
     'Ejemplo para Madrid, sin relación comercial: entrega documento de identificación, '
     'contrato y certificado de eliminación.'),
]
NOTA_PROVEEDORES = ('No se publican los proveedores que sólo salen en directorios, ni los '
                    'formatos profesionales de chocolate sin fuente, ni listados antiguos sin '
                    'reconfirmar.')


# ==========================================================================
# 20. CHECKLIST LEGAL POR FASES (libro 7), ÁRBOL IAE/CNAE Y CRONOGRAMA
# ==========================================================================
FASES_CHECKLIST = {
    'F1': 'Antes de firmar: el local, la extracción, el gas y el horario',
    'F2': 'Sociedad, altas fiscales y proyecto técnico',
    'F3': 'Licencias de obra y de actividad, gas y terraza',
    'F4': 'Obra, instalaciones y maquinaria',
    'F5': 'Registro sanitario, autocontrol, aceite, alérgenos y formación',
    'F6': 'Apertura: plantilla, horario y carta',
}

#: (fase, trámite, responsable, plazo orientativo en días, fuente, cambia por CCAA,
#: nota). La PRIMERA fila es la bifurcación de A4 / D13, delante de la del Anexo. El
#: coste de cada trámite no se repite aquí: el que tiene cifra vive en el libro 2.
CHECKLIST_LEGAL = [
    ('F1', '¿La extracción necesita proyecto?', 'Promotor y técnico', 10, 'CUN-35 + CUN-23 + CUN-24', True,
     'Casi siempre que hay conducto a cubierta, o que cruza fachada o patio: entonces van '
     'licencia de obra y técnico, aunque la actividad vaya por declaración responsable '
     '(Ley 12/2012, art. 3.3-3.4).'),
    ('F1', '¿Tu actividad está en el Anexo de la Ley 12/2012?', 'Promotor', 5, 'CUN-35 + CHN-49b + CHN-49c', False,
     'La actividad de un despacho para llevar (644.6, hasta 750 m²) va por declaración '
     'responsable; con mesas (676 o 673) sale del Anexo y manda tu ayuntamiento.'),
    ('F1', 'Comprobar la salida de humos del local', 'Promotor y técnico', 5, 'CUN-23 + CUN-24', True,
     'En el ejemplo de Madrid: captación, filtrado y conducto a cubierta, con limpieza al menos '
     'una vez al año. Los requisitos de otras ciudades no están verificados.'),
    ('F1', 'Comprobar la potencia de la freidora y el riesgo de incendio', 'Técnico', 5, 'CUN-26', False,
     'Freidoras a 1 kW por litro; local de riesgo especial desde 20 kW; extinción automática '
     'por encima de 50 kW; filtros a 1,20 m del foco con gas o parrilla.'),
    ('F1', 'Decidir el gas: instalación receptora o freidora eléctrica', 'Promotor', 5, 'CHN-48 + CUN-28', False,
     'En un local, gas con instalación receptora e inspección cada cinco años, o eléctrico con '
     'su potencia. La bombona pequeña sólo vale para un aparato de utilización móvil (feria).'),
    ('F1', 'Comprobar el horario que te permite tu clasificación', 'Promotor', 3, 'CUN-34', True,
     'Ejemplo de Madrid: cafetería o bar desde las 6:00; chocolatería desde las 8:00. Tu hora '
     'de apertura se pone en la hoja «Franjas del Día» del libro 5.'),
    ('F2', 'Constituir la sociedad o darse de alta como autónomo', 'Promotor', 20, 'CHN-75', False,
     'Verifactu: 2027 para sociedades y autónomos, no 2026.'),
    ('F2', 'Alta censal con doble código CNAE, como pregunta al asesor', 'Gestoría', 3, 'CUN-16 + CHN-74b + CUN-15', False,
     'La correspondencia del IAE con el CNAE-2025 no está publicada: se pregunta, con el '
     'código de 2025 y el de 2009. Ojo: el 47.81 de 2025 es de vehículos de motor.'),
    ('F2', 'Alta en el IAE: la sala y la venta al peso', 'Gestoría', 3, 'CUN-09 + CUN-14 + CHN-73 + CHN-94', False,
     'Alta sí, pago casi nunca: exención por debajo de un millón de euros de cifra de negocio. '
     'Una cuota faculta sólo para su actividad.'),
    ('F2', 'Encargar el proyecto técnico de actividad y de la extracción', 'Ingeniería', 30, 'CUN-35', False,
     'Su coste es un supuesto del libro 2, bloque 8.'),
    ('F2', 'Firmar el arrendamiento y depositar la fianza', 'Promotor', 5, 'supuesto', True,
     'La fianza se deposita en el organismo de tu comunidad.'),
    ('F3', 'Pedir la licencia de obra del conducto, si la primera fila dijo que sí', 'Técnico', 60, 'CUN-35', True, ''),
    ('F3', 'Presentar la declaración responsable o pedir la licencia de actividad', 'Técnico', 30, 'CUN-35 + CHN-49c', True,
     'El modelo depende de la segunda fila: nunca «necesitas licencia» o «no la necesitas» sin '
     'decir cuál.'),
    ('F3', 'Certificar la instalación receptora de gas', 'Instalador', 15, 'CHN-48', False, ''),
    ('F3', 'Pedir la autorización de la terraza', 'Promotor', 30, 'CUN-35', True,
     'La ocupación de la vía pública va aparte (art. 2.2 de la Ley 12/2012).'),
    ('F4', 'Hacer la obra y el conducto', 'Promotor', 60, 'CUN-23', False, ''),
    ('F4', 'Instalar la campana con los filtros a su distancia y el extintor de clase F', 'Instalador', 10, 'CUN-26 + CUN-38', False, ''),
    ('F4', 'Pedir la maquinaria crítica con el plazo de entrega por escrito', 'Promotor', 45, 'supuesto', False,
     'El plazo de entrega vive SÓLO en este libro (`PLAZO_ENTREGA_MAQUINARIA_SEMANAS`).'),
    ('F4', 'Contratar un gestor autorizado del aceite usado y guardar los justificantes', 'Promotor', 5, 'CUN-27 + CUS-44h', False,
     'La recogida separada del aceite de cocina usado es obligatoria.'),
    ('F5', 'Comunicar la actividad al registro sanitario autonómico', 'Promotor', 15, 'CHN-39 + CUN-30', True,
     'El minorista queda fuera del registro general; si sirves churros a una cafetería de otro '
     'titular, cambia la cosa (actividad restringida).'),
    ('F5', 'Plan de autocontrol con responsable y registro del aceite', 'Encargado/a', 10, 'CHN-32 + CUN-01 + CUN-02 + CUN-03', False,
     'La norma de aceites alcanza a la churrería; polares por debajo del 25 %; el artículo 9 '
     'sigue vivo. El registro se lleva en el Pack APPCC 09.'),
    ('F5', 'Alérgenos de la carta por escrito y aceite compartido', 'Encargado/a', 5, 'CHN-34 + CHN-33 + CHN-37', False,
     'Gluten siempre; la freidora que fríe otra cosa contamina; «sin gluten» casi nunca se '
     'puede decir.'),
    ('F5', 'Acrilamida: buena práctica en el churro, parte A si fríes patatas', 'Encargado/a', 5, 'CUN-04 + CUN-05 + CUN-06 + CUN-07', False,
     'El churro no está nombrado en el reglamento; la parte B sólo alcanza a quien sigue las '
     'instrucciones de un suministro centralizado (art. 2.3).'),
    ('F5', 'Registro de formación del personal', 'Encargado/a', 5, 'CHN-69', False, ''),
    ('F5', 'Denominación del chocolate según la etiqueta del preparado', 'Encargado/a', 3, 'CUN-42 + CUN-V06', False,
     'Qué preparado compras y qué dice su etiqueta; con menos del 35 % de cacao seco total o '
     'con grasa vegetal, consulta a tu servicio de consumo antes de imprimir la carta.'),
    ('F5', 'Cobrar aparte el vaso de plástico para llevar', 'Encargado/a', 1, 'CUN-41', False, ''),
    ('F6', 'Contratos, altas y convenio aplicable', 'Gestoría', 10, 'CUN-39 + CUN-V01 + CHN-93 + CUN-V05', True,
     'El de Madrid es el ejemplo; busca el tuyo en REGCON.'),
    ('F6', 'Nocturnidad: las dos figuras, persona a persona', 'Gestoría', 3, 'CUN-29 + CUN-40', False,
     'El trabajador nocturno del Estatuto y el plus del convenio son dos cosas distintas.'),
    ('F6', 'Registro diario de jornada', 'Encargado/a', 1, 'CHN-68', False, ''),
    ('F6', 'Salarios por encima del SMI', 'Gestoría', 1, 'CHN-67', False, ''),
]

#: Plazo de entrega de la maquinaria crítica: UNA sola fuente en todo el paquete, el
#: libro 7 (el 2 no lo pide).
PLAZO_ENTREGA_MAQUINARIA_SEMANAS = (6, 'supuesto', 'Pídelo por escrito al proveedor.')

#: Árbol IAE y CNAE por formato: el CNAE va SIEMPRE como pregunta al asesor con doble
#: código (V-03, rama B), nunca como dato.
ARBOL_IAE = [
    {'formato': 'Local con sala', 'iae': '676 (chocolatería) o 673 (cafés y bares), más 644.6 si vendes al peso',
     'cnae_a_preguntar': '56.11 o 56.30 (CNAE-2025), con su código de 2009', 'fuente': 'CUN-10 + CUN-14 + CUN-09 + CUN-16'},
    {'formato': 'Despacho para llevar', 'iae': '644.6 (masas fritas y preparados de chocolate)',
     'cnae_a_preguntar': '47.24 o 56.11, con su código de 2009', 'fuente': 'CUN-09 + CUN-16'},
    {'formato': 'Caseta o feria', 'iae': '663.1; 675 o 674.7 con mesas',
     'cnae_a_preguntar': '56.12, con su código de 2009 (y nunca el 47.81)', 'fuente': 'CUN-11 + CUN-13 + CUN-15'},
    {'formato': 'Obrador que sirve a otros', 'iae': '419.3 (industria de masas fritas)',
     'cnae_a_preguntar': '10.71, con su código de 2009', 'fuente': 'CUN-12 + CUN-16'},
]

#: Cronograma en MESES (sin funciones de fecha prohibidas): (id, hito, meses, previos).
#: Arranca en noviembre del año anterior para abrir el 1 de septiembre.
MES_INICIO_PROYECTO = 11
GANTT = [
    ('H1', 'Búsqueda y ficha de visita de locales', 2.0, ()),
    ('H2', 'Firma del arrendamiento y fianza', 0.5, ('H1',)),
    ('H3', 'Proyecto técnico de actividad y de la extracción', 1.5, ('H2',)),
    ('H4', 'Licencia de obra del conducto', 2.0, ('H3',)),
    ('H5', 'Declaración responsable o licencia de actividad', 1.0, ('H3',)),
    ('H6', 'Obra y conducto a cubierta', 2.0, ('H4',)),
    ('H7', 'Pedido y entrega de la maquinaria crítica', None, ('H3',)),
    ('H8', 'Instalación receptora de gas y su certificado', 0.5, ('H6',)),
    ('H9', 'Montaje y prueba de la línea de fritura', 0.5, ('H7', 'H8')),
    ('H10', 'Comunicación al registro sanitario autonómico', 0.5, ('H5', 'H9')),
    ('H11', 'Autocontrol, registro del aceite, alérgenos y formación', 0.5, ('H9',)),
    ('H12', 'Contratación y altas', 0.5, ('H9',)),
    ('H13', 'Pruebas de masa y carta de apertura', 0.5, ('H10', 'H11', 'H12')),
    ('H14', 'Apertura', 0.0, ('H13',)),
]
FUENTE_GANTT = 'supuesto'


def _duracion(h):
    if h[2] is None:
        return PLAZO_ENTREGA_MAQUINARIA_SEMANAS[0] * 7.0 / (365.0 / 12.0)
    return h[2]


def ruta_critica():
    """(meses hasta abrir, camino crítico, holgura por hito), con aritmética de meses."""
    ini, fin, previo = {}, {}, {}
    for h in GANTT:
        hid, deps = h[0], h[3]
        if deps:
            mejor = max(deps, key=lambda x: fin[x])
            ini[hid], previo[hid] = fin[mejor], mejor
        else:
            ini[hid], previo[hid] = 0.0, None
        fin[hid] = ini[hid] + _duracion(h)
    ultimo = GANTT[-1][0]
    camino, cur = [], ultimo
    while cur is not None:
        camino.append(cur)
        cur = previo[cur]
    camino.reverse()
    total = fin[ultimo]
    holgura = {}
    for h in GANTT:
        sucesores = [x[0] for x in GANTT if h[0] in x[3]]
        limite = min(ini[s] for s in sucesores) if sucesores else total
        holgura[h[0]] = round(limite - fin[h[0]], 2)
    return total, camino, holgura


def mes_apertura_calculado():
    total, _c, _h = ruta_critica()
    return ((MES_INICIO_PROYECTO - 1 + int(round(total))) % 12) + 1


# ==========================================================================
# 21. CRUCES ENTRE LIBROS: el grafo sin ciclos (D16)
# ==========================================================================
#: Cada cruce es UNA celda verde «cópialo del libro N: <fichero>!<Hoja>!<Celda>» en el
#: libro receptor, con su valor por defecto (`valor_defecto`, el de El Molinete) y una
#: FILA DE CUADRE con semáforo en la misma hoja. Nunca una fórmula entre ficheros.
#:
#: CONTRATO ENTRE CONSTRUCTORES (`celda_origen`): en cada hoja de origen, las cifras que
#: viajan viven en el bloque «Lo que copian otros libros», rótulo en la columna K y
#: valor en la L, desde la fila 5 y en el orden de esta lista. Si un constructor necesita
#: otra celda, se cambia AQUÍ primero. En el receptor, todas las celdas de cruce van en
#: «Parámetros» (en el libro 6, «0. Supuestos»).
_RECEPTORA = {1: 'Parámetros', 2: 'Parámetros', 4: 'Parámetros', 5: 'Parámetros',
              8: 'Parámetros', 6: '0. Supuestos'}

_ESPEC_CRUCES = [
    # (x, origen, receptor, concepto, unidad, hoja de origen, celda, función que da el valor)
    ('X1', 3, 1, 'kg de masa por ración media (mix de invierno, merma incluida)', 'kg/ración',
     'Mix y Ticket Canal y Temporada', 'L5', 'kg_masa_por_racion_media'),
    ('X2', 3, 4, 'Precio del aceite (base imponible)', '€/L', 'Parámetros', 'L5', 'precio_aceite_eur_l'),
    ('X2', 3, 4, 'Absorción de aceite, en % del peso frito', '%', 'Parámetros', 'L6', '_absorcion'),
    ('X2', 3, 4, 'Densidad del aceite', 'kg/L', 'Parámetros', 'L7', '_densidad'),
    ('X2 bis', 3, 4, 'kg de masa por ración media', 'kg/ración',
     'Mix y Ticket Canal y Temporada', 'L5', 'kg_masa_por_racion_media'),
    ('X2 bis', 3, 4, 'Aceite absorbido por ración (mix de invierno)', '€/ración',
     'Absorción de Aceite y Merma', 'L5', 'aceite_absorbido_por_racion'),
    ('X3', 1, 4, 'kg fritos en un día tipo', 'kg/día', 'Día Tipo y Día Punta', 'L5', '_kg_fritos_tipo'),
    ('X3', 1, 4, 'kg fritos en un día punta', 'kg/día', 'Día Tipo y Día Punta', 'L6', '_kg_fritos_punta'),
    ('X3', 1, 4, 'Litros totales de cuba', 'L', 'Freidoras, Potencia y Riesgo', 'L5', '_litros_cuba'),
    ('X3 bis', 1, 4, 'Raciones del día tipo', 'raciones', 'Día Tipo y Día Punta', 'L7', '_raciones_tipo'),
    ('X3 bis', 1, 4, 'Raciones del día punta', 'raciones', 'Día Tipo y Día Punta', 'L8', '_raciones_punta'),
    ('X4', 1, 5, 'Raciones del día tipo', 'raciones', 'Día Tipo y Día Punta', 'L7', '_raciones_tipo'),
    ('X4', 1, 5, 'Raciones del día punta', 'raciones', 'Día Tipo y Día Punta', 'L8', '_raciones_punta'),
    ('X4', 1, 5, 'Capacidad del conjunto', 'raciones/h', 'Cuello de Botella', 'L5', 'capacidad_raciones_h'),
    ('X5', 3, 5, 'Ticket sin IVA por ración en verano (carta de verano)', '€/ración',
     'Mix y Ticket Canal y Temporada', 'L6', '_ticket_verano'),
    ('X5', 3, 5, 'Coste de materia por ración en verano, aceite absorbido incluido', '€/ración',
     'Mix y Ticket Canal y Temporada', 'L7', '_materia_verano'),
    ('X5', 3, 5, 'Coste de materia por ración para llevar, aceite absorbido incluido', '€/ración',
     'Mix y Ticket Canal y Temporada', 'L8', '_materia_llevar'),
    ('X5', 3, 5, 'Coste hora de mano de obra', '€/h', 'Coste Hora', 'L5', 'coste_hora_mano_obra'),
    ('X6', 1, 8, 'Personas en la línea en el pico', 'personas', 'Equipos y Capacidad', 'L5', '_personas_pico'),
    ('X7', 5, 8, 'Horas semanales de la franja de desayuno', 'h/semana', 'Franjas del Día', 'L5', '_horas_desayuno'),
    ('X7', 5, 8, 'Horas semanales de la franja de media mañana', 'h/semana', 'Franjas del Día', 'L6', '_horas_media'),
    ('X7', 5, 8, 'Horas semanales de la franja de merienda', 'h/semana', 'Franjas del Día', 'L7', '_horas_merienda'),
    ('X7', 5, 8, 'Horas semanales de la franja de noche', 'h/semana', 'Franjas del Día', 'L8', '_horas_noche'),
    ('X7', 5, 8, 'Horas de refuerzo de Navidad y Reyes al año', 'h/año', 'Refuerzo por Pico', 'L5', 'horas_refuerzo_pico'),
    ('X8', 3, 8, 'Coste hora de mano de obra usado en el escandallo', '€/h', 'Coste Hora', 'L5', 'coste_hora_mano_obra'),
    ('X9', 1, 2, '¿Necesitas extinción automática? (1 sí, 0 no)', '1/0', 'Freidoras, Potencia y Riesgo', 'L6',
     'necesita_extincion_automatica'),
    ('X10', 2, 6, 'CAPEX SIN fondo de maniobra', '€', 'Resumen', 'L5', 'capex_total'),
    ('X11', 3, 6, 'Coste de materia por ración en sala (invierno), aceite absorbido incluido', '€/ración',
     'Mix y Ticket Canal y Temporada', 'L9', '_materia_sala'),
    ('X11', 3, 6, 'Coste de materia por ración para llevar (invierno), aceite absorbido incluido', '€/ración',
     'Mix y Ticket Canal y Temporada', 'L8', '_materia_llevar'),
    ('X11', 3, 6, 'Ticket sin IVA por ración en sala (invierno)', '€/ración',
     'Mix y Ticket Canal y Temporada', 'L10', '_ticket_sala'),
    ('X11', 3, 6, 'Ticket sin IVA por ración para llevar (invierno)', '€/ración',
     'Mix y Ticket Canal y Temporada', 'L11', '_ticket_llevar'),
    ('X11', 3, 6, 'Raciones en sala, en % (el resto, para llevar)', '%',
     'Mix y Ticket Canal y Temporada', 'L12', '_pct_sala'),
    ('X12', 4, 6, 'Renovación de aceite por ración', '€/ración', 'Consumo y Reposición', 'L5', 'renovacion_por_racion'),
    ('X13', 5, 6, 'Raciones del año', 'raciones', 'Peso sobre el Año', 'L5', 'raciones_anio'),
] + [
    ('X13', 5, 6, 'Coeficiente de ' + MESES[i].lower(), 'coeficiente', 'Peso sobre el Año', 'L%d' % (6 + i),
     '_coef_%02d' % (i + 1)) for i in range(12)
] + [
    ('X14', 5, 6, 'Resultado anual de ferias', '€', 'Calendario de Ferias', 'L5', 'resultado_anual_ferias'),
    ('X15', 8, 6, 'Coste anual de plantilla', '€', 'Coste de Plantilla', 'L5', 'coste_plantilla_anual'),
    ('X16', 5, 6, 'Contribución de julio y agosto de la salida elegida', '€', 'El Verano (Tres Salidas)', 'L5',
     '_contribucion_verano_elegida'),
    ('X17', 3, 2, 'Precio del aceite (base imponible)', '€/L', 'Parámetros', 'L5', 'precio_aceite_eur_l'),
    ('X17', 3, 2, 'Precio del mix (base imponible)', '€/kg', 'Parámetros', 'L8', 'precio_mix_eur_kg'),
    ('X18', 2, 6, 'Renta mensual', '€/mes', 'Parámetros', 'L5', '_renta'),
]

CRUCES = []
for _n, (_x, _o, _r, _c, _u, _ho, _co, _f) in enumerate(_ESPEC_CRUCES, 1):
    CRUCES.append({'n': _n, 'x': _x, 'origen': _o, 'receptor': _r, 'concepto': _c, 'unidad': _u,
                   'fichero_origen': LIBROS[_o], 'hoja_origen': _ho, 'celda_origen': _co,
                   'fichero_receptor': LIBROS[_r], 'hoja_receptor': _RECEPTORA[_r],
                   'calcula': _f, 'valor_defecto': None})

#: Las quince aristas de §2.2, y nada más (3 -> 2 es la de X17).
ARISTAS_SPEC = {(3, 1), (3, 4), (1, 4), (1, 5), (3, 5), (1, 8), (5, 8), (3, 8), (1, 2), (2, 6),
                (3, 6), (4, 6), (5, 6), (8, 6), (3, 2)}


def rotulo_cruce(c):
    return 'cópialo del libro %d: %s!%s!%s' % (c['origen'], c['fichero_origen'], c['hoja_origen'],
                                             c['celda_origen'])


def aristas(cruces=None):
    return set((c['origen'], c['receptor']) for c in (cruces if cruces is not None else CRUCES))


def orden_topologico(arcos, nodos):
    """Kahn. Devuelve (orden, nodos que quedan en un ciclo)."""
    entrada = dict((n, 0) for n in nodos)
    for _a, b in arcos:
        entrada[b] += 1
    libres = sorted(n for n in nodos if entrada[n] == 0)
    orden = []
    while libres:
        n = libres.pop(0)
        orden.append(n)
        for a, b in sorted(arcos):
            if a == n:
                entrada[b] -= 1
                if entrada[b] == 0:
                    libres.append(b)
                    libres.sort()
    return orden, sorted(n for n in nodos if n not in orden)


def es_orden_valido(orden, arcos):
    pos = dict((n, i) for i, n in enumerate(orden))
    return all(pos[a] < pos[b] for a, b in arcos)


# ==========================================================================
# 22. LAS 12 DECISIONES: lo que elige El Molinete (bonus 2)
# ==========================================================================
#: Cada decisión, con su hoja y la elección del caso. Las cifras y los umbrales los
#: calcula `cifras_decisiones()` con este mismo juego de datos.
DECISIONES = [
    (1, 'Sala o sólo despacho', '2!Variante del Formato + 7!Checklist Legal', 'Sala, con despacho a calle'),
    (2, 'Traspaso u obra nueva', '2!Traspaso vs Obra Nueva', 'Obra nueva en un local sin salida de humos'),
    (3, 'Equipo completo o línea separada', '1!Cuello de Botella', 'Línea separada (dotación B)'),
    (4, 'Gas con instalación receptora o eléctrico', '1!Freidoras, Potencia y Riesgo', 'Gas, sin extinción automática'),
    (5, 'Mix propio o preparado comercial', '3!Escandallo por kg de Masa', 'Preparado comercial'),
    (6, 'Qué preparado compras para la taza y qué dice su etiqueta', '3!Chocolate a la Taza',
     'Un preparado cuya etiqueta dice «chocolate a la taza»'),
    (7, 'Ración, docena o kilo', '3!Ración, Docena o Kilo', 'Los tres, con la ración como formato de la sala'),
    (8, 'Abrir antes de las 8:00', '7!Régimen de Apertura y Horario + 5!Franjas del Día',
     'Sí, clasificada como cafetería o bar en el ejemplo de Madrid'),
    (9, 'Verano: cerrar, carta de verano o ferias', '5!El Verano (Tres Salidas) + 6!Escenarios', 'Carta de verano'),
    (10, 'Cuánta madrugada asumes tú', '8!Horas del Titular', 'La del fin de semana desde las 6:00'),
    (11, 'Freidora dedicada o compartida', '7!Alérgenos y Aceite Compartido', 'Dedicada al churro y a la porra'),
    (12, 'Franquicia o por tu cuenta', '2!Franquicia o Independiente', 'Por su cuenta'),
]


# ==========================================================================
# 23. NOTAS LEGALES: nota_legal() y gate_legal()
# ==========================================================================
#: Cada celda con un dato legal lleva la nota «Verificado el <fecha> · norma y artículo
#: · URL». No se escribe a mano en ningún constructor: se pide aquí. Las fichas CUN se
#: leen de la verificación legal de este producto (03-10-2026) y las CHN reutilizadas,
#: de la de la hermana (12-09-2026), con la fecha de cada una.
VERIFICACION_LEGAL_CUN = os.path.join(_AUDIT, 'guia-churreria-verificacion-legal-2026-10-03.json')
VERIFICACION_LEGAL_CUN_EXCLUIDOS = os.path.join(
    _AUDIT, 'guia-churreria-verificacion-legal-2026-10-03-EXCLUIDOS.json')
VERIFICACION_LEGAL_CHN = os.path.join(_AUDIT, 'guia-chocolateria-verificacion-legal-2026-09-12.json')
JSON_COMUN = os.path.join(_AUDIT, 'guias-v2-research-sector.json')

_CACHE = {}


def _carga_lista(ruta):
    """Lista de fichas de un JSON (lista, o dict con la lista dentro). {} si falta."""
    if ruta in _CACHE:
        return _CACHE[ruta]
    filas = {}
    if os.path.exists(ruta):
        with open(ruta, 'rb') as fh:
            crudo = json.loads(fh.read().decode('utf-8'))
        lista = crudo
        if isinstance(crudo, dict):
            lista = crudo.get('datos') or next((v for v in crudo.values() if isinstance(v, list)), [])
        for f in lista:
            if isinstance(f, dict) and f.get('id'):
                filas[str(f['id']).strip()] = f
    _CACHE[ruta] = filas
    return filas


def ficha_comun(pid):
    return _carga_lista(JSON_COMUN).get(pid)


def id_existe_en_json_comun(pid):
    return pid in _carga_lista(JSON_COMUN)


_TOKENS_ARTICULO = ('art.', 'arts.', 'artículo', 'articulo', 'ap.', 'aps.', 'apartado', 'anexo',
                    'epígrafe', 'epigrafe')
_RX_ABREV = re.compile(r'\b([Aa]rt|[Aa]ps?)\.')
_MARCA = '\x01'


def _tiene_cita_articulo(texto):
    t = (texto or '').lower()
    return any(tok in t for tok in _TOKENS_ARTICULO)


def _ventana(frase):
    if len(frase) <= 140:
        return frase
    tl = frase.lower()
    pos = min(tl.find(t) for t in _TOKENS_ARTICULO if t in tl)
    ini, fin = max(0, pos - 60), min(len(frase), pos + 80)
    return ('...' if ini else '') + frase[ini:fin].strip() + ('...' if fin < len(frase) else '')


def _cita_articulo(fila):
    """La frase de la ficha que YA lleva artículo, apartado, anexo o epígrafe (port de la
    hermana: no se inventa ningún número)."""
    for campo in ('nota', 'dato', 'cita_literal', 'tema'):
        texto = _RX_ABREV.sub(lambda m: m.group(1) + _MARCA, fila.get(campo) or '')
        for frase in re.split(r'(?<=[.;])\s+', texto):
            frase = re.sub(r'\s+', ' ', frase.replace(_MARCA, '.')).strip()
            if _tiene_cita_articulo(frase):
                frase = _ventana(frase)
                if _tiene_cita_articulo(frase):
                    return frase
    return None


def nota_legal(pid):
    """«Verificado el <fecha> · <norma y artículo> · <URL>», o None si no se puede
    construir (los constructores llaman antes a `gate_legal()`)."""
    if pid.startswith('CUN-'):
        fila, fecha = _carga_lista(VERIFICACION_LEGAL_CUN).get(pid), FECHA_VERIFICACION_CUN
    elif pid.startswith('CHN-'):
        fila, fecha = _carga_lista(VERIFICACION_LEGAL_CHN).get(pid), FECHA_VERIFICACION_CHN
    else:
        return None
    if not fila:
        return None
    norma = re.sub(r'\s+', ' ', (fila.get('fuente_titulo') or '').strip())
    url = (fila.get('url') or '').strip()
    if not norma or not url.lower().startswith('http'):
        return None
    if not _tiene_cita_articulo(norma):
        extra = _cita_articulo(fila)
        if extra and extra not in norma:
            norma = '%s (%s)' % (norma[:177].rstrip() + ('...' if len(norma) > 180 else ''), extra)
    if len(norma) > 300:
        norma = norma[:297].rstrip() + '...'
    return 'Verificado el %s %s %s %s %s' % (fecha, chr(183), norma, chr(183), url)


#: Los ids CUN y CHN que citan los libros según la SPEC (§2.1, §3 y §4), con su libro.
IDS_LEGALES_REQUERIDOS = {
    # --- libro 1: humos, potencia y gas -----------------------------------
    'CUN-23': ('Madrid: campana con filtro de grasas y conducto a cubierta', (1, 7)),
    'CUN-24': ('Madrid: la excepción de 4 kW no ampara una freidora', (1, 7)),
    'CUN-26': ('CTE DB-SI: 1 kW por litro, riesgo especial, extinción automática y 1,20 m', (1, 7)),
    'CUN-35': ('Actividad por declaración responsable; las obras con proyecto, no', (1, 2, 7)),
    'CHN-48': ('Gas: inspección de la instalación receptora cada cinco años', (1, 7)),
    # --- libro 2 -------------------------------------------------------------
    'CUN-38': ('Extintor adecuado a la clase de fuego: clase F para aceites', (2, 7)),
    'CHN-71c': ('IVA: 10 % en sala y 21 % de tipo general', (2, 3)),
    # --- libro 3: carta, chocolate e IVA ----------------------------------
    'CHN-05': ('Chocolate a la taza y su mención obligatoria', (3,)),
    'CUN-42': ('El «chocolate a la taza» del RD es un producto: 35 % de cacao seco total', (3,)),
    'CUN-V06': ('Qué nombre puede llevar la taza: interpretación de nivel B/C', (3, 7)),
    'CUN-18': ('IVA del chocolate y de las bebidas para llevar: zona gris', (3,)),
    'CUN-17': ('Definición de bebida refrescante, que sostiene la zona gris', (3,)),
    'CUN-41': ('Vaso de plástico para llevar cobrado aparte desde 2023', (3, 7)),
    'CHN-34': ('Alérgenos de los productos sin envasar', (3, 7)),
    # --- libro 4: aceite ---------------------------------------------------
    'CUN-01': ('La norma de aceites calentados alcanza a la churrería', (4, 7)),
    'CUN-02': ('Polares por debajo del 25 %, demostrado en laboratorio', (4, 7)),
    'CUN-03': ('Artículos derogados y artículo vivo de la norma de aceites', (4, 7)),
    'CUN-27': ('Recogida separada obligatoria del aceite de cocina usado', (4, 7)),
    'CUN-05': ('Acrilamida: parte A para quien fríe patatas; parte B sólo con suministro centralizado', (4, 7)),
    # --- libro 5 -------------------------------------------------------------
    'CUN-34': ('Madrid: chocolatería desde las 8:00, cafetería o bar desde las 6:00', (5, 7)),
    'CUN-37': ('Tasa de feria de un pueblo pequeño: ejemplo, no orden de magnitud', (5, 7)),
    # --- libro 7: el checklist ---------------------------------------------
    'CUN-04': ('El churro no está nombrado en el reglamento de la acrilamida', (7,)),
    'CUN-06': ('La recomendación de la UE sí nombra los churros', (7,)),
    'CUN-07': ('Informe oficial: no hay valor de referencia para los churros', (7,)),
    'CUN-08': ('Revisión de la acrilamida en marcha', (7,)),
    'CUN-09': ('IAE 644.6: despacho de churros con obrador', (7,)),
    'CUN-10': ('IAE 676: chocolaterías, heladerías y horchaterías', (7,)),
    'CUN-11': ('IAE 663.1: venta fuera de establecimiento permanente', (7,)),
    'CUN-12': ('IAE 419.3: industria de masas fritas', (7,)),
    'CUN-13': ('IAE 675 y 674.7: quioscos, barracas y recintos feriales', (7,)),
    'CUN-14': ('La nota de venta en el propio establecimiento sólo alcanza al 671-673', (7,)),
    'CUN-15': ('CNAE-2025: las clases que interesan, y la trampa del 47.81', (7,)),
    'CUN-19': ('El RD de venta ambulante de 2010 está derogado', (7,)),
    'CUN-20': ('La autorización de venta ambulante no es indefinida', (7,)),
    'CUN-21': ('La caseta provisional es comercio al por menor', (7,)),
    'CUN-22': ('Requisitos higiénicos de los locales ambulantes', (7,)),
    'CUN-25': ('Madrid: cocinar en suelo de uso público', (7,)),
    'CUN-28': ('La bombona de menos de 15 kg, sólo para un aparato de utilización móvil', (7,)),
    'CUN-30': ('La churrería que sirve a una cafetería: actividad restringida', (7,)),
    'CUN-36': ('Ordenanzas que siguen citando la norma derogada', (7,)),
    'CUN-V03': ('El INE no resuelve la correspondencia IAE-CNAE', (7,)),
    'CHN-32': ('Autocontrol simplificado con responsable', (7,)),
    'CHN-33': ('Alérgenos y limpieza de equipo: el aceite compartido', (7,)),
    'CHN-37': ('«Sin gluten»: umbral analítico', (7,)),
    'CHN-39': ('El minorista está excluido del registro general', (7,)),
    'CHN-49b': ('El grupo 644 está en el Anexo de la Ley 12/2012', (7,)),
    'CHN-49c': ('La chocolatería de taza no entra en la Ley 12/2012', (7,)),
    'CHN-69': ('El «carnet» no existe: registro de formación', (7,)),  # LN-OK
    'CHN-73': ('IAE: alta sí, pago casi nunca', (7,)),
    'CHN-74b': ('Al darte de alta comunicas dos códigos CNAE', (7,)),
    'CHN-75': ('Verifactu: 2027', (6, 7)),
    'CHN-77': ('Libertad horaria del comercio de menos de 300 m²', (7,)),
    'CHN-94': ('Una cuota faculta sólo para su actividad', (7,)),
    # --- libro 8: turnos y convenio ---------------------------------------
    'CUN-29': ('ET art. 36.1: trabajo nocturno y trabajador nocturno', (8,)),
    'CUN-31': ('ALEH VI: freidurías, quioscos y chocolaterías', (8,)),
    'CUN-32': ('ALEH VI vigente hasta el 31-12-2030', (8,)),
    'CUN-39': ('Convenio de Madrid, clase C, tablas de 2025', (8,)),
    'CUN-40': ('Plus de nocturnidad del convenio de Madrid', (8,)),
    'CUN-V01': ('Estado del convenio de Madrid a 03-10-2026', (8,)),
    'CUN-V05': ('Convenio de Toledo: obradores de masas fritas', (8,)),
    'CHN-67': ('SMI 2026', (8,)),
    'CHN-68': ('Registro de jornada', (8,)),
    'CHN-93': ('Convenios de sector que nombran el chocolate: el método', (8,)),
}

#: Ids que se citan como HALLAZGO NEGATIVO y no pueden llevar nota de verificación: no
#: hay URL que poner. Existen en el JSON común; `gate_legal()` no los exige.
IDS_SIN_NOTA_LEGAL = {
    'CUN-16': 'No hay tabla oficial IAE-CNAE para 644.6, 676 y 663.1: va como pregunta al asesor.',
    'CUN-33': 'Convenio propio de churrerías: no localizado, búsqueda no exhaustiva.',
}

#: Ids cuya ficha no permite componer artículo, apartado, anexo ni epígrafe, revisados
#: uno a uno: fuente no normativa, o norma que se cita por sección y tabla.
EXCEPCIONES_SIN_ARTICULO = {
    'CUN-26': 'El CTE se cita por sección, tabla y nota (SI 1, tabla 2.1, notas 2 y 3), no por artículo.',
    'CUN-07': 'Informe oficial de una autoridad sanitaria autonómica: no es una norma.',
    'CUN-08': 'Fuente secundaria sobre una revisión en marcha: no es una norma.',
    'CUN-15': 'Catálogo de códigos del CNAE-2025, sin articulado propio para una clase.',
    'CUN-30': 'Guía informativa de la Comunidad de Madrid, citada por página: no es una norma.',
    'CUN-36': 'Borrador de ordenanza municipal, citado como ejemplo de una remisión obsoleta.',
    'CUN-V03': 'Notas explicativas del INE, citadas por clase: no son una norma.',
    'CUN-V05': 'Convenio citado por su cláusula 1, «Ámbito funcional»: cláusula, no artículo.',
    'CHN-74b': 'Cita una disposición adicional (excepción heredada de la hermana).',
    'CHN-93': 'Consulta pública del registro REGCON, no una norma (excepción heredada).',
}

#: Ids PROHIBIDOS (§2.3 y §5.1): no pueden ser la fuente de nada. «a secas» = sin sufijo.
IDS_PROHIBIDOS = {
    'CUS-31h': 'anuncio reeditado durante años (D15)',          # LN-OK
    'CUS-31i': 'anuncio reeditado durante años (D15)',          # LN-OK
    'CUS-56': 'sueldos de un agregador, por debajo del SMI (A7)',  # LN-OK
    'CUS-M05': 'curso de un anuncio de 2016 (A10)',             # LN-OK
    'CUS-05': 'personal de un artículo de un proveedor de TPV (N-5)',  # LN-OK
    'CUS-40': 'rellenadora sin precio utilizable (SR-06)',      # LN-OK
    'CHS-37b': 'lectura antigua del traspaso de Vallecas (SR-02)',  # LN-OK
    'CUS-31': 'a secas: agrega los anuncios reeditados (A2)',   # LN-OK
    'CHS-31': 'a secas: el margen de la hermana sin fuente (D6)',  # LN-OK
}

#: El patrón de id de este producto (§2.3).
RX_ID = re.compile(r'\b(?:CHN|CHS|CUN|CUS|FC-IVA)-(?:[MVD])?[0-9]+[a-z]*\b')


def gate_legal(ids_requeridos=None, abortar=True):
    """Exige una nota legal, con artículo, apartado, anexo o epígrafe, para CADA id que
    citan los libros. Aborta listando los que faltan (o los devuelve si abortar=False)."""
    ids = list(ids_requeridos or IDS_LEGALES_REQUERIDOS)
    faltan = [i for i in ids if nota_legal(i) is None]
    sin_art = [i for i in ids if i not in faltan and i not in EXCEPCIONES_SIN_ARTICULO
               and not _tiene_cita_articulo(nota_legal(i))]
    if not faltan and not sin_art:
        return []
    detalle = ['  - %s: SIN NOTA (%s)' % (i, IDS_LEGALES_REQUERIDOS.get(i, ('?',))[0]) for i in faltan]
    detalle += ['  - %s: SIN ARTÍCULO, APARTADO, ANEXO NI EPÍGRAFE (%s)'
                % (i, IDS_LEGALES_REQUERIDOS.get(i, ('?',))[0]) for i in sin_art]
    mensaje = 'gate_legal: %d sin nota y %d sin artículo, de %d ids\n%s' % (
        len(faltan), len(sin_art), len(ids), '\n'.join(detalle))
    if abortar:
        raise SystemExit(mensaje)
    return faltan + sin_art


# ==========================================================================
# 24. ECONOMÍA: plantilla, coste hora, año de crucero, fondo y financiación
# ==========================================================================
def bruto_anual_nivel(nivel):
    base = NIVELES[nivel][0]
    return (base * dato(CONVENIO, 'pagas')
            + dato(CONVENIO, 'plus_convenio_mes') * dato(CONVENIO, 'meses_plus_convenio'))


def base_hora(nivel):
    """Salario base por hora, sobre el que se calcula el plus de nocturnidad."""
    return NIVELES[nivel][0] * dato(CONVENIO, 'pagas') / dato(CONVENIO, 'jornada_anual_h')


def semanas_trabajadas():
    return dato(CONVENIO, 'jornada_anual_h') / dato(CONVENIO, 'horas_semana_completa')


def plus_nocturnidad_anual(pid):
    p = persona(pid)
    if p['es_titular']:
        return 0.0
    a = analisis_nocturnidad(pid)
    semana = (a['horas_plus_22_0'] * dato(CONVENIO, 'plus_noche_22_0')
              + a['horas_plus_0_8'] * dato(CONVENIO, 'plus_noche_0_8')) * base_hora(p['nivel'])
    return semana * semanas_trabajadas()


def salario_anual(pid):
    """Bruto del puesto a su jornada más el plus. Antes del suelo del SMI."""
    p = persona(pid)
    return bruto_anual_nivel(p['nivel']) * p['jornada'] + plus_nocturnidad_anual(pid)


def suelo_smi(pid):
    return dato(CONVENIO, 'smi_anual') * persona(pid)['jornada']


def por_debajo_del_smi(pid):
    return salario_anual(pid) < suelo_smi(pid) - 1e-9


def coste_puesto_anual(pid):
    """MAX(salario; SMI anual a la jornada), más la Seguridad Social de empresa si cotiza
    (A7). El titular no la lleva: cotiza por su cuota de autónomos."""
    p = persona(pid)
    salario = max(salario_anual(pid), suelo_smi(pid))
    return salario * (1.0 + P('ss_empresa')) if p['cotiza_ss_empresa'] else salario


def horas_plantilla_anio():
    return sum(p['jornada'] for p in PLANTILLA) * dato(CONVENIO, 'jornada_anual_h')


def coste_puestos_anual():
    return sum(coste_puesto_anual(p['id']) for p in PLANTILLA)


def coste_hora_mano_obra():
    """Coste de la plantilla por hora contratada (cruces X5 y X8): el que usa el escandallo."""
    return coste_puestos_anual() / horas_plantilla_anio()


def semanas_abiertas():
    return dias_apertura_anio() / 7.0


def horas_sustitucion_anio():
    """Horas del cuadrante que nadie de la plantilla hace porque está de vacaciones o
    descansando un festivo: cada contrato trabaja sus semanas, el local abre todas. El
    titular no entra: sus vacaciones las decide él."""
    if not P('cubrir_vacaciones_con_sustitutos'):
        return 0.0
    hueco = max(0.0, semanas_abiertas() - semanas_trabajadas())
    return sum(horas_semana(p['id']) for p in PLANTILLA if not p['es_titular']) * hueco


def coste_plantilla_anual():
    """Cruce X15: los puestos, el refuerzo de Navidad y Reyes y las sustituciones."""
    return coste_puestos_anual() + (horas_refuerzo_pico() + horas_sustitucion_anio()) * coste_hora_mano_obra()


def minutos_mano_obra_por_racion():
    return horas_plantilla_anio() * 60.0 / raciones_anio()


def margen_tras_mano_de_obra(temporada='invierno'):
    """El segundo margen de «Los Dos Márgenes»: tras materia, aceite absorbido y mano de
    obra, comparable a la rentabilidad declarada de CUS-30."""
    t = ticket_sin_iva(temporada)
    mo = minutos_mano_obra_por_racion() / 60.0 * coste_hora_mano_obra()
    return 1.0 - (materia_por_racion(temporada) + mo) / t


def horas_titular():
    return horas_semana('P1')


def horas_titular_0_8():
    return sum(_solape(t[2], t[3], 0.0, 8.0) for t in turnos_de('P1'))


def ventas_y_contribucion():
    """Año de crucero: ventas sin IVA y contribución. De septiembre a junio con la carta
    de invierno; julio y agosto con la salida elegida (cruce X16). La renovación del aceite
    se resta en todas las raciones (cruce X12)."""
    ventas = contribucion = 0.0
    for mes in range(1, 13):
        r = raciones_mes(mes)
        if mes in MESES_VERANO:
            continue
        ventas += r * ticket_sin_iva('invierno')
        contribucion += r * (ticket_sin_iva('invierno') - materia_por_racion('invierno'))
    if SALIDA_VERANO_ELEGIDA == 'carta de verano':
        ventas += raciones_verano() * ticket_sin_iva('verano')
    contribucion += contribucion_verano(SALIDA_VERANO_ELEGIDA)
    contribucion -= raciones_anio() * renovacion_por_racion()
    contribucion += resultado_anual_ferias()
    return ventas, contribucion


_PRINCIPAL = {'valor': None, 'provisional': None}


def fijos_caja_mes(intereses_anuales):
    """Gastos fijos de CAJA de un mes: plantilla, renta, fijos e intereses. La amortización
    no es caja y no entra en el colchón."""
    return (coste_plantilla_anual() / 12.0 + dato(NEGOCIO, 'renta_mensual') + gastos_fijos_mes()
            + intereses_anuales / 12.0)


def _cuadro(principal):
    i = dato(FINANCIACION, 'tipo_nominal') / 12.0
    n, car = dato(FINANCIACION, 'plazo_meses'), dato(FINANCIACION, 'carencia_meses')
    cuota = principal * i / (1.0 - (1.0 + i) ** (-(n - car)))
    saldo, filas = principal, []
    for mes in range(1, n + 1):
        interes = saldo * i
        amort = 0.0 if mes <= car else cuota - interes
        filas.append((mes, saldo, interes, amort, interes + amort))
        saldo -= amort
    return filas


def _intereses_anio(principal, anio):
    return sum(f[2] for f in _cuadro(principal) if (anio - 1) * 12 < f[0] <= anio * 12)


def principal_prestamo():
    """El 60 % de la inversión total (CAPEX sin fondo más el fondo de maniobra), redondeado
    a centenas. Es un PUNTO FIJO: el fondo incluye los intereses, que dependen del
    principal (patrón de la hermana)."""
    if _PRINCIPAL['valor'] is not None:
        return _PRINCIPAL['valor']
    pr = round(dato(FINANCIACION, 'pct_prestamo') * capex_total(), -2)
    for _ in range(60):
        fondo = P('meses_colchon') * fijos_caja_mes(_intereses_anio(pr, P('anio_crucero')))
        nuevo = round(dato(FINANCIACION, 'pct_prestamo') * (capex_total() + fondo), -2)
        if abs(nuevo - pr) < 1.0:
            pr = nuevo
            break
        pr = nuevo
    _PRINCIPAL['valor'] = pr
    return pr


def cuadro_frances():
    return _cuadro(principal_prestamo())


def intereses_anio(anio):
    return _intereses_anio(principal_prestamo(), anio)


def fondo_maniobra():
    """SÓLO aquí y en el libro 6 (D16): meses de colchón por los fijos de caja del mes."""
    return P('meses_colchon') * fijos_caja_mes(intereses_anio(P('anio_crucero')))


def inversion_total():
    return capex_total() + fondo_maniobra()


def amortizacion_anual():
    return capex_amortizable() / P('anios_amortizacion')


def fijos_anuales():
    """Lo que el libro 6 resta a la contribución: plantilla, renta, fijos, amortización e
    intereses del año de crucero."""
    return (coste_plantilla_anual() + 12.0 * dato(NEGOCIO, 'renta_mensual') + 12.0 * gastos_fijos_mes()
            + amortizacion_anual() + intereses_anio(P('anio_crucero')))


def cuenta_resultados_crucero():
    ventas, contribucion = ventas_y_contribucion()
    fijos = fijos_anuales()
    beneficio = contribucion - fijos
    return {'ventas': ventas, 'contribucion': contribucion, 'fijos': fijos,
            'beneficio': beneficio, 'margen_neto': beneficio / ventas if ventas else 0.0}


def punto_equilibrio_raciones_dia():
    """Raciones al día que pagan los fijos, con la contribución media por ración del año."""
    _v, contribucion = ventas_y_contribucion()
    por_racion = contribucion / raciones_anio()
    return fijos_anuales() / por_racion / dias_apertura_anio()


def verano_con_fijos(salida):
    """La fila de «Escenarios» del libro 6: la contribución de julio y agosto de cada
    salida menos dos meses de fijos (los mismos en las tres)."""
    return contribucion_verano(salida) - 2.0 * fijos_anuales() / 12.0


# --- funciones de una línea que dan el valor de los cruces --------------------
def _absorcion():
    return P('absorcion_aceite_pct')


def _densidad():
    return P('densidad_aceite_kg_l')


def _kg_fritos_tipo():
    return kg_fritos_dia('tipo')


def _kg_fritos_punta():
    return kg_fritos_dia('punta')


def _litros_cuba():
    return dato(PRODUCCION, 'litros_freidora')


def _raciones_tipo():
    return dato(PRODUCCION, 'raciones_dia_tipo')


def _raciones_punta():
    return dato(PRODUCCION, 'raciones_dia_punta')


def _ticket_verano():
    return ticket_sin_iva('verano')


def _materia_verano():
    return materia_por_racion('verano')


def _materia_llevar():
    return materia_por_racion('invierno', 'llevar')


def _materia_sala():
    return materia_por_racion('invierno', 'sala')


def _ticket_sala():
    return ticket_sin_iva('invierno', 'sala')


def _ticket_llevar():
    return ticket_sin_iva('invierno', 'llevar')


def _pct_sala():
    return 100.0 * pct_raciones('sala')


def _personas_pico():
    return dato(PRODUCCION, 'personas_en_linea_pico')


def _horas_desayuno():
    return horas_semana_franja('desayuno')


def _horas_media():
    return horas_semana_franja('media_manana')


def _horas_merienda():
    return horas_semana_franja('merienda')


def _horas_noche():
    return horas_semana_franja('noche')


def _contribucion_verano_elegida():
    return contribucion_verano(SALIDA_VERANO_ELEGIDA)


def _renta():
    return dato(NEGOCIO, 'renta_mensual')


def _coef(mes):
    return COEFICIENTES_MES[mes - 1]


for _i in range(1, 13):
    globals()['_coef_%02d' % _i] = (lambda m: (lambda: _coef(m)))(_i)


def valor_cruce(c):
    return globals()[c['calcula']]()


def _c(v, dec=2):
    """Número con coma decimal y punto de miles, como lo escribe el guion."""
    texto = ('{:,.%df}' % dec).format(v)
    return texto.replace(',', '#').replace('.', ',').replace('#', '.')


def cifras_decisiones():
    """La cifra que resuelve cada decisión del bonus 2 en El Molinete, y el umbral a partir
    del cual elegirías lo contrario (C7)."""
    ahorro_kg = coste_masa_eur_kg() - coste_masa_eur_kg(mix_propio=True)
    kg_anio = raciones_anio() * kg_masa_por_racion_media('invierno')
    obra = sum(capex_bloque(n) for n in range(1, 9))
    vallecas = [t for t in TRASPASOS if t['fuente'] == 'CUS-02'][0]
    adaptacion = dato(TRASPASO_ALTERNATIVA, 'adaptacion')
    meses_cola = [MESES[m - 1].lower() for m in range(1, 13) if cola_del_domingo(m) > 0]
    margen_verano = ticket_sin_iva('verano') - materia_por_racion('verano')
    dias_verano = 62.0
    refuerzo_medio = (bruto_anual_nivel('V') * 0.5 * (1.0 + P('ss_empresa')))
    electrica = importe_sin_iva(equipo('freidora_electrica_25l')) - importe_sin_iva(equipo('freidora_gas_25l'))
    return {
        1: 'el %s %% de las raciones se consume en sala: sin sala, el local vendería sólo la parte '
           'para llevar' % _c(_pct_sala(), 0),
        2: 'obra nueva (bloques 1 a 8) %s € frente a traspaso pedido más adaptación %s €; el '
           'traspaso gana si se cierra por debajo de %s €'
           % (_c(obra, 0), _c(vallecas['precio_pedido'] + adaptacion, 0), _c(obra - adaptacion, 0)),
        3: 'capacidad %s raciones/h frente a %s en la hora punta del domingo de diciembre; hay cola '
           'en: %s' % (_c(capacidad_raciones_h(), 0), _c(demanda_hora_punta_domingo(12), 0),
                      ', '.join(meses_cola) or 'ningún mes'),
        4: '%s kW computables, riesgo %s, extinción automática %s, filtros a %s m; la freidora '
           'eléctrica cuesta %s € más y no pide instalación de gas'
           % (_c(kw_computables(), 0), riesgo_cocina(), 'sí' if necesita_extincion_automatica() else 'no',
              _c(distancia_filtro_m()), _c(electrica, 0)),
        5: 'el mix propio ahorra %s €/kg de masa: %s € al año sobre %s kg, antes de pagar el pesado '
           'y la regularidad' % (_c(ahorro_kg), _c(ahorro_kg * kg_anio, 0), _c(kg_anio, 0)),
        6: 'cacao seco total de la etiqueta %s %% frente al mínimo de %s %%; aviso: %s'
           % (_c(P('cacao_seco_total_preparado_pct'), 0), _c(P('cacao_minimo_chocolate_taza_pct'), 0),
              'sí' if chocolate_pide_aviso() else 'no'),
        7: 'euros por kg de masa: ración %s, docena %s, kilo %s'
           % (_c(euros_por_kg_masa('CH1')), _c(euros_por_kg_masa('CH6')), _c(euros_por_kg_masa('CH7'))),
        8: 'abre a las %d:00 el fin de semana; como chocolatería no podría antes de las %d:00'
           % (int(HORARIO['S'][0][0]), int(HORA_MINIMA_APERTURA_MADRID['chocolateria'][0])),
        9: 'contribución de julio y agosto: cerrar %s €, carta de verano %s €, ferias %s €; la carta '
           'de verano deja de ganar por debajo de %s raciones al día'
           % (_c(contribucion_verano('cerrar'), 0), _c(contribucion_verano('carta de verano'), 0),
              _c(contribucion_verano('ferias'), 0),
              _c(contribucion_verano('ferias') / margen_verano / dias_verano, 0)),
        10: 'el titular hace %s h a la semana, %s de ellas entre las 0:00 y las 8:00; otro medio '
            'refuerzo de nivel V cuesta %s € al año'
            % (_c(horas_titular(), 1), _c(horas_titular_0_8(), 1), _c(refuerzo_medio, 0)),
        11: 'freidora dedicada: el aceite sólo toca masa de churro y de porra (gluten siempre)',
        12: 'inversión independiente %s € frente a franquicias de %s a %s € (orden de magnitud)'
            % (_c(inversion_total(), 0), _c(min(f['inversion'] for f in FRANQUICIAS), 0),
               _c(max(f['inversion'] for f in FRANQUICIAS), 0)),
    }


# ==========================================================================
# 25. LISTA NEGRA, GATE DE TILDES Y COMPROBACIONES
# ==========================================================================
#: Cadenas del §5 de la SPEC (y de la refutación del research) que no pueden aparecer en
#: el fichero. Se barre el código ENTERO, docstring incluido; sólo se saltan las líneas
#: marcadas LN-OK, que son estas. Una aguja que empieza por «re:» es una expresión regular.
LISTA_NEGRA = (
    ('85-90', 'D6: el margen de la hermana sin fuente'),                       # LN-OK
    ('85 y 90', 'D6'),                                                         # LN-OK
    ('107.000', 'D15: anuncio reeditado'),                                     # LN-OK
    ('120.000', 'D15: anuncio reeditado'),                                     # LN-OK
    ('95.000', 'D15 y SR-02: lectura antigua de Vallecas'),                    # LN-OK
    ('290 €', 'A10: el curso de un anuncio de 2016'),                          # LN-OK
    ('290 euros', 'A10'),                                                      # LN-OK
    ('1.343', 'A7: sueldos de un agregador'),                                  # LN-OK
    ('16.116', 'A7'),                                                          # LN-OK
    ('2.400', 'N-5: personal de un artículo de un proveedor de TPV'),          # LN-OK
    ('55 raciones', 'N-5: el punto de equilibrio de ese artículo'),            # LN-OK
    ('9.800', 'N-6: escenarios del mismo artículo'),                           # LN-OK
    ('540 kg', 'N-8: el máximo del fabricante'),                               # LN-OK
    ('absorbe un 30', 'N-7: ficha comercial'),                                 # LN-OK
    ('dura el doble', 'N-7'),                                                  # LN-OK
    ('docena a 12', 'N-14: errata de un artículo'),                            # LN-OK
    ('12 euros la docena', 'N-14'),                                            # LN-OK
    ('facturamos', 'CUS-50: titular sin método'),                              # LN-OK
    ('150 franquicias', 'CUS-14: objetivo del franquiciador'),                 # LN-OK
    ('re:maestro churrero[^\n]{0,80}75[.]?000', 'SR-20: la cifra vetada'),     # LN-OK
    ('12.000-50.000', 'N-3: la tabla de nuestro post'),                        # LN-OK
    ('12.000 y 50.000', 'N-3'),                                                # LN-OK
    ('40.000-60.000', 'N-2'),                                                  # LN-OK
    ('2.000-6.000', 'N-4'),                                                    # LN-OK
    ('re:\\b1[6-9][0-9]\\s?(°|º|grados)', 'V-02: temperatura de fritura'),    # LN-OK
    ('brecha', 'A8: la plaza mueve el ticket un 50 %, no más'),                # LN-OK
    ('posición 1', 'D20 y B2'),                                                # LN-OK
    ('primera posición', 'D20 y B2'),                                          # LN-OK
    ('carnet de manipulador', 'CHN-69'),                                       # LN-OK
    ('carné de manipulador', 'CHN-69'),                                        # LN-OK
    ('convenio de churrerías', 'D9'),                                          # LN-OK
    ('categoría de churrero', 'D9'),                                           # LN-OK
    ('media cuota', 'D14 y A3'),                                               # LN-OK
    ('cumplimiento acrilamida', 'D12'),                                        # LN-OK
    ('entra a las 4', 'A1'),                                                   # LN-OK
    ('verificado contra el boe', 'regla de la casa'),                          # LN-OK
    ('100 % legal', 'regla de la casa'),                                       # LN-OK
    ('toda hispanoamérica', 'regla de la casa'),                               # LN-OK
    ('plan gratuito', 'regla de la casa'),                                     # LN-OK
    ('comparativa de aceites', 'D4 y C5'),                                     # LN-OK
    ('una dueña', 'SR-05'),                                                    # LN-OK
    ('no existe ninguna guía', 'verificación §6.12'),                          # LN-OK
    ('1562/1998', 'CUN-34: orden derogada'),                                   # LN-OK
    ('23,7', 'N-12'),                                                          # LN-OK
    ('35,2', 'N-12'),                                                          # LN-OK
    ('3.400 m', 'N-16'),                                                       # LN-OK
    ('4.228', 'N-11'),                                                         # LN-OK
    ('7.306', 'N-14'),                                                         # LN-OK
    ('13,5 m', 'N-14'),                                                        # LN-OK
    ('rentabilidad del 70', 'N-15'),                                           # LN-OK
    ('1,10 €/m', 'N-18'),                                                      # LN-OK
    ('750-3.000', 'N-18'),                                                     # LN-OK
    ('demuestra el 25', 'A12'),                                                # LN-OK
    ('te evita la instalación', 'A6'),                                         # LN-OK
    ('cumple la ley de plásticos', 'SR-08'),                                   # LN-OK
)

#: Homógrafos que se escriben sin tilde cuando son otra palabra: el demostrativo «esta»
#: no es el verbo «está», el relativo «quien» o «cual» no es el interrogativo, y el verbo
#: «publica» o «fabrica» no es el adjetivo ni el sustantivo. Sólo los que el fichero usa.
AMBIGUAS = {'esta', 'estas', 'quien', 'cual', 'publica', 'fabrica', 'fabricas'}
_DOCUMENTOS = {}


def _documentos():
    """El detector de documentos.py (léxico, tokenizador y normalizador), importado tal
    cual: no se reescribe."""
    if 'm' not in _DOCUMENTOS:
        ruta = os.path.join(_GUIAS_V2, 'documentos.py')
        spec = importlib.util.spec_from_file_location('documentos_guias_v2', ruta)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _DOCUMENTOS['m'] = mod
    return _DOCUMENTOS['m']


_RX_NO_TEXTO = [
    re.compile(r'`[^`]*`'),                                     # código entre comillas inversas
    re.compile(r'https?://\S+'),                                # URL
    re.compile(r'\S+\.(?:xlsx|json|md|py|docx|pdf)\b\S*'),     # ficheros y rutas
    re.compile(r'\b[\w-]+\.(?:com|es|pro|org|net)\b'),          # dominios
    re.compile(r'\b[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)+(?:\[[^\]]*\])?'),  # nombres con punto
    re.compile(r'\b[A-Z_]{3,}\[[^\]]*\]'),                      # ESTRUCTURA[clave]
    re.compile(r'\b\w+_\w+\b'),                                 # identificadores
    re.compile(r'\b[a-z0-9]+(?:-[a-z0-9]+){2,}\b'),             # slugs
]


def _literales(ruta):
    """Todos los literales de texto de un .py, con los fragmentos de código fuera:
    claves, rutas, expresiones regulares y nombres de estructuras del propio fichero."""
    with open(ruta, 'rb') as fh:
        arbol = ast.parse(fh.read().decode('utf-8'))
    estructuras = set()
    for nodo in arbol.body:
        if isinstance(nodo, ast.Assign):
            estructuras.update(t.id for t in nodo.targets if isinstance(t, ast.Name) and t.id.isupper())
    rx_estructuras = re.compile(r'\b(?:%s)\b' % '|'.join(sorted(estructuras))) if estructuras else None
    textos = []
    for nodo in ast.walk(arbol):
        valor = None
        if isinstance(nodo, ast.Str):
            valor = nodo.s
        elif hasattr(ast, 'Constant') and isinstance(nodo, ast.Constant) and isinstance(nodo.value, str):
            valor = nodo.value
        if not valor or re.match(r'^[a-z][a-z0-9_]*$', valor):
            continue                                     # claves y códigos, no prosa
        if re.match(r'^[\w.\-/!\[\]%]+$', valor) and re.search(r'[_./!\-]', valor):
            continue
        if '\\' in valor or '(?' in valor:
            continue                                     # expresiones regulares
        for rx in _RX_NO_TEXTO:
            valor = rx.sub(' ', valor)
        if rx_estructuras is not None:
            valor = rx_estructuras.sub(' ', valor)
        textos.append(valor)
    return textos


def _tasa_tildes(textos):
    letras = sum(1 for t in textos for ch in t if ch.isalpha())
    con_tilde = sum(1 for t in textos for ch in t if ch in 'áéíóúÁÉÍÓÚ')
    return 1000.0 * con_tilde / letras if letras else 0.0


def erratas_de_tilde(textos):
    """{palabra escrita sin tilde: forma con tilde del léxico}, con la frecuencia mínima
    del detector de documentos.py y sin los homógrafos de AMBIGUAS."""
    doc = _documentos()
    lex = doc.lexico()
    erratas = {}
    for t in textos:
        for tok in doc.RX_TOKEN.findall(t):
            if any(ch in 'áéíóúüñÁÉÍÓÚÜÑ' for ch in tok):
                continue
            n = doc._norm_tok(tok)
            if n in AMBIGUAS or n not in lex:
                continue
            forma, freq = lex[n]
            if forma != n and freq >= doc.MIN_FREQ_LEXICO:
                erratas[tok] = forma
    return erratas


def gate_tildes(ruta=None, hermana=None):
    """DoD de F1: 0 palabras escritas sin tilde que el léxico del grupo tenga con tilde
    (frecuencia >= MIN_FREQ_LEXICO de documentos.py) en los literales del módulo, más la
    tasa de letras con tilde por 1.000 letras frente a la hermana."""
    doc = _documentos()
    ruta = ruta or os.path.abspath(__file__)
    hermana = hermana or os.path.normpath(os.path.join(_AQUI, '..', 'guia-chocolateria', 'datos_ejemplo.py'))
    textos = _literales(ruta)
    erratas = erratas_de_tilde(textos)
    letra_caida = doc.erratas_ortograficas('\n'.join(textos))
    return {'erratas': erratas, 'tasa': _tasa_tildes(textos),
            'tasa_hermana': _tasa_tildes(_literales(hermana)) if os.path.exists(hermana) else None,
            'letra_caida': letra_caida}


_RX_FUENTE = re.compile(
    r'^(supuesto|calculado'
    r'|(?:CHN|CHS|CUN|CUS|FC-IVA)-(?:[MVD])?[0-9]+[a-z]*'
    r'|heredado: motor\.PARAMETROS\[[a-z_]+\]'
    r'|heredado: guia-chocolateria/datos_ejemplo\.py [A-Z_]+\[[^\]]+\]'
    r'|[a-z0-9\-]+/[a-z0-9\-]+\.xlsx![^!+]+)$')


def _fuente_ok(f):
    if not isinstance(f, str) or not f.strip():
        return False
    return all(_RX_FUENTE.match(t.strip()) for t in f.split(' + '))


_DICCIONARIOS_PARAMETRO = ('NEGOCIO', 'PARAMS', 'PRODUCCION', 'ACEITE', 'CONVENIO', 'FINANCIACION',
                           'TRABAJO_NOCTURNO_ET', 'CONVENIO_METODO', 'TRASPASO_ALTERNATIVA', 'RAMPA',
                           'HORA_MINIMA_APERTURA_MADRID')


def _todas_las_fuentes():
    f = []
    for nombre in _DICCIONARIOS_PARAMETRO:
        f += [v[1] for v in globals()[nombre].values()]
    f += [v[1] for v in NIVELES.values()]
    f += [OBRA_EUR_M2[1], DOTACION_COMPLETA_DECLARADA[1], PLAZO_ENTREGA_MAQUINARIA_SEMANAS[1],
          FUENTE_HORARIO, FUENTE_TURNOS, FUENTE_COEFICIENTES, FUENTE_GANTT,
          CARGO_VASO['fuente_pvp'], CARGO_VASO['fuente_obligacion']]
    f += [z[2] for z in ZONAS] + [x['fuente'] for x in FRANJAS]
    f += [s[3] for s in SALARIOS_MERCADO] + [p['fuente'] for p in PLANTILLA]
    f += [m['fuente'] for m in MARGENES_DE_CONTRASTE] + [i['fuente'] for i in INSUMOS.values()]
    f += [r['fuente_pvp'] for r in CARTA] + [x[1] for x in FICHA_VISITA_ELIMINATORIOS]
    f += [e['fuente'] for e in EQUIPAMIENTO] + [p[4] for p in CAPEX_PARTIDAS]
    f += [v['fuente'] for v in VARIANTES.values()] + [x['fuente'] for x in FRANQUICIAS]
    f += [t['fuente'] for t in TRASPASOS] + [c['fuente'] for c in CANALES]
    f += [e['fuente'] for e in FERIAS] + [x['fuente'] for x in FERIAS_REFERENCIAS]
    f += [g[2] for g in GASTOS_FIJOS_MENSUALES] + [p[3] for p in PROVEEDORES]
    f += [c[4] for c in CHECKLIST_LEGAL] + [a['fuente'] for a in ARBOL_IAE]
    return f


def _codigo_sin_ln_ok():
    with open(os.path.abspath(__file__), 'rb') as fh:
        fuente = fh.read().decode('utf-8')
    return fuente, '\n'.join(l for l in fuente.split('\n') if 'LN-OK' not in l)


def _tokens_numericos():
    with open(os.path.abspath(__file__), 'rb') as fh:
        toks = list(tokenize.tokenize(fh.readline))
    cuenta = {}
    for t in toks:
        if t.type == tokenize.NUMBER:
            cuenta[t.string] = cuenta.get(t.string, 0) + 1
    return cuenta


def _hoja_valida(nombre):
    return len(nombre) <= 31 and not any(c in nombre for c in '[]:*?/\\')


def comprobar():
    fallos, avisos = [], []

    def exige(cond, mensaje):
        if not cond:
            fallos.append(mensaje)

    # ---- precondición: sin parámetros vacíos no se calcula nada (C3) ---------
    vacios = ['%s[%s]' % (nombre, clave) for nombre in _DICCIONARIOS_PARAMETRO
              for clave, v in globals()[nombre].items() if v[0] is None]
    vacios += ['GASTOS_FIJOS_MENSUALES[%s]' % g[0] for g in GASTOS_FIJOS_MENSUALES if g[1] is None]
    vacios += ['CARTA[%s]' % r['id'] for r in CARTA
               if any(r[k] is None for k in ('pvp', 'mix_invierno', 'mix_verano', 'pct_llevar'))]
    vacios += ['COEFICIENTES_MES'] if any(c is None for c in COEFICIENTES_MES) else []
    if vacios or _ERROR_CRUCES:
        print('PARÁMETROS SIN VALOR (C3): %s%s' % (', '.join(vacios),
              ('\nLos cruces no se pudieron calcular: %s' % _ERROR_CRUCES) if _ERROR_CRUCES else ''))
        raise SystemExit(1)

    fuente_py, barrible = _codigo_sin_ln_ok()

    # ---- 0. WinAnsi ------------------------------------------------------------
    try:
        fuente_py.encode('cp1252')
    except UnicodeEncodeError as e:
        fallos.append('Carácter fuera de WinAnsi en la posición %d: %r'
                      % (e.start, fuente_py[max(0, e.start - 40):e.start + 40]))

    # ---- 1. lista negra, ids prohibidos y procedencia --------------------------
    bajo = barrible.lower()
    for aguja, motivo in LISTA_NEGRA:
        m = re.search(aguja[3:], bajo) if aguja.startswith('re:') else None
        i = (m.start() if m else -1) if aguja.startswith('re:') else bajo.find(aguja)
        exige(i < 0, 'Lista negra %r (%s): %r' % (aguja, motivo, barrible[max(0, i - 60):i + 60]))
    for pid in IDS_PROHIBIDOS:
        rx = re.compile(r'\b%s\b(?![a-z])' % re.escape(pid))
        exige(not rx.search(barrible), 'Id prohibido %s fuera de las líneas LN-OK' % pid)
    fuentes = [str(f) for f in _todas_las_fuentes()]
    for f in fuentes:
        exige(_fuente_ok(f), 'Fuente que no es ninguno de los cuatro orígenes: %r' % f)
        for tramo in f.split(' + '):
            exige(tramo.strip() not in IDS_PROHIBIDOS, 'Fuente con un id prohibido: %r' % f)
            for pid in RX_ID.findall(tramo):
                exige(id_existe_en_json_comun(pid), 'Fuente con un id que no existe: %r' % f)
    citados = set(RX_ID.findall(barrible))
    for pid in sorted(citados):
        exige(id_existe_en_json_comun(pid), 'El id %s no existe en el JSON común' % pid)

    # ---- 2. el local -------------------------------------------------------------
    m2 = sum(z[1] for z in ZONAS)
    exige(abs(m2 - 75.0) < 1e-9 and dato(NEGOCIO, 'm2_total') == 75.0, 'El local no suma 75 m²: %.1f' % m2)
    exige(len(ZONAS) == 6 and all(z[0] in ZONA_A_BLOQUE for z in ZONAS), 'Zonas mal asignadas')
    exige(dato(NEGOCIO, 'mes_apertura') not in MESES_PICO, 'La apertura cae dentro del pico')

    # ---- 3. horario, franjas, cuadrante y nocturnidad --------------------------
    exige(abs(horas_apertura_semana() - 83.5) < 1e-9, 'Horas de apertura: %.1f' % horas_apertura_semana())
    for d in DIAS:
        exige(abs(sum(pct_franja(f, d) for f in FRANJAS if d in f['tramos']) - 100.0) < 1e-9,
              'Las franjas del %s no suman 100' % NOMBRE_DIA[d])
    exige(not tramos_sin_minimo(), 'Horas de apertura sin mínimo de cobertura: %s' % tramos_sin_minimo()[:5])
    exige(not huecos_de_cobertura(), 'HUECOS DE COBERTURA: %s' % huecos_de_cobertura()[:8])
    exige(not problemas_del_cuadrante(), 'Cuadrante: %s' % problemas_del_cuadrante())
    exige(('P2', 'L', 6.0, 14.0, 'L') in TURNOS and ('P3', 'S', 4.5, 12.5, 'L') in TURNOS
          and ('P4', 'V', 17.0, 21.0, 'B') in TURNOS and ('P4', 'V', 21.0, 25.0, 'L') in TURNOS,
          'Faltan los turnos didácticos literales de §3.2')
    a2, a3, a4 = analisis_nocturnidad('P2'), analisis_nocturnidad('P3'), analisis_nocturnidad('P4')
    exige(a2['horas_22_6_semana'] == 0.0 and abs(a2['horas_plus_0_8'] - 10.0) < 1e-9,
          'Churrero/a 1: 0 h en 22-6 y 2 h con plus al día')
    exige(a3['trabajador_nocturno_et'] == 'no' and abs(a3['horas_22_6_semana'] - 3.0) < 1e-9,
          'Churrero/a 2: 1,5 h en 22-6 por día de fin de semana, NO es trabajador nocturno')
    exige(a4['trabajador_nocturno_et'] == 'revísalo con tu asesor' and a4['dias_con_3h_o_mas'] == 2,
          'Quien cierra: 3 h en 22-6 dos días por semana -> «revísalo con tu asesor»')
    for p in PLANTILLA:
        exige(not por_debajo_del_smi(p['id']), '%s cobra por debajo del SMI 2026' % p['id'])
        exige(coste_puesto_anual(p['id']) >= suelo_smi(p['id']) - 1e-9, '%s: coste bajo el suelo' % p['id'])
    for nivel in NIVELES:
        exige(bruto_anual_nivel(nivel) >= dato(CONVENIO, 'smi_anual'), 'El nivel %s queda por debajo del SMI' % nivel)
    for _n, mn, _mx, _f, _nota in SALARIOS_MERCADO:
        exige(mn >= dato(CONVENIO, 'smi_mensual'), 'Un salario de mercado mensual por debajo del SMI mensual')
    exige(dato(CONVENIO, 'pagas') == 14 and CONVENIO['pagas'][1] == 'supuesto', 'SR-04: 14 pagas, supuesto')

    # ---- 4. la carta -------------------------------------------------------------
    exige(len(CARTA) == 24, 'La carta tiene %d referencias' % len(CARTA))
    conteo = dict((f, len(por_familia(f))) for f in FAMILIAS)
    exige(conteo == FAMILIAS_ESPERADO, 'Reparto por familias: %s' % conteo)
    exige(len(set(r['id'] for r in CARTA)) == 24 and len(set(r['nombre'] for r in CARTA)) == 24,
          'Ids o nombres repetidos en la carta')
    mix_i, mix_v = sum(r['mix_invierno'] for r in CARTA), sum(r['mix_verano'] for r in CARTA)
    exige(abs(mix_i - 100.0) < 1e-9 and abs(mix_v - 100.0) < 1e-9, 'Mix %.2f / %.2f' % (mix_i, mix_v))
    exige(abs(pct_raciones('llevar') - 0.30) < 1e-9 and abs(pct_raciones('sala') - 0.70) < 1e-9,
          'El mix de canales de la carta no da 70/30: %.4f' % pct_raciones('llevar'))
    exige(abs(sum(c['pct_raciones'] for c in CANALES) - 100.0) < 1e-9
          and abs([c for c in CANALES if c['clave'] == 'llevar'][0]['pct_raciones'] - 100.0 * pct_raciones('llevar')) < 1e-9,
          'CANALES no cuadra con la carta')
    for r in CARTA:
        exige(r['iva_llevar'] in PARAMS and 0.0 <= r['pct_llevar'] <= 1.0, '%s: IVA o canal' % r['id'])
        exige(r['anio_pvp'] in (2025, 2026), '%s: falta el año del precio (A8)' % r['id'])
        for canal in ('sala', 'llevar'):
            exige(ingreso_unidad(r, canal) > coste_escandallo_unidad(r, canal), '%s vende a pérdida' % r['id'])
        for insumo, _q in r['receta'] + r['envase_llevar']:
            exige(insumo in INSUMOS or insumo in RECETAS_CHOCOLATE, '%s usa %r' % (r['id'], insumo))
    for clave in ('iva_llevar_chocolate', 'iva_llevar_bebidas'):
        exige('CELDA VERDE' in PARAMS[clave][2] and 'CUN-18' in PARAMS[clave][1], 'D11: %s' % clave)
    exige(not chocolate_pide_aviso(), 'El preparado del ejemplo debería cumplir su etiqueta')

    # ---- 5. un único precio por insumo y por línea, un concepto por clave ------
    numeros = _tokens_numericos()
    unicos = [('%.2f' % i['precio_formato']) for i in INSUMOS.values() if i['fuente'] != 'supuesto']
    unicos += ['%.2f' % e['precio_fuente'] for e in EQUIPAMIENTO if e['fuente'] != 'supuesto']
    unicos += ['910.0', '82000.0']
    for n in unicos:
        exige(numeros.get(n, 0) == 1, 'El número %s aparece %d veces en el código' % (n, numeros.get(n, 0)))
    vistas = {}
    for nombre in _DICCIONARIOS_PARAMETRO:
        for clave in globals()[nombre]:
            exige(clave not in vistas, 'El concepto %r está en %s y en %s' % (clave, vistas.get(clave), nombre))
            vistas[clave] = nombre
    for nombre in _DICCIONARIOS_PARAMETRO:
        for clave, v in globals()[nombre].items():
            exige(v[0] is not None, '%s[%s] sin valor (C3)' % (nombre, clave))
    exige(all(g[1] is not None for g in GASTOS_FIJOS_MENSUALES), 'Un gasto fijo sin valor (SR-13)')
    for r in CARTA:
        exige(all(r[k] is not None for k in ('pvp', 'mix_invierno', 'mix_verano', 'pct_llevar')),
              '%s: un parámetro del neto sin valor' % r['id'])
    exige(all(i['precio_formato'] is not None and i['cantidad_formato'] for i in INSUMOS.values()),
          'Un insumo sin precio')
    exige(all(e[k] is not None for e in FERIAS for k in e), 'Un evento con un campo sin valor')
    exige(all(c is not None for c in COEFICIENTES_MES), 'Un coeficiente sin valor')
    for valor in (coste_plantilla_anual(), gastos_fijos_mes(), amortizacion_anual(),
                  intereses_anio(P('anio_crucero')), renovacion_por_racion(), fondo_maniobra()):
        exige(valor is not None and valor == valor, 'Un parámetro del neto o del punto de equilibrio sin valor')
    exige('densidad_aceite_kg_l' in PARAMS and 'absorcion_aceite_pct' in PARAMS, 'Falta un supuesto de C3')

    # ---- 6. dotación y CAPEX sin fondo de maniobra ----------------------------
    exige(abs(dotacion_b_nucleo() - 8618.35) < 0.005, 'Núcleo B: %.2f' % dotacion_b_nucleo())
    exige(abs(dotacion_b_con_testo() - 9117.35) < 0.005, 'B con Testo: %.2f' % dotacion_b_con_testo())
    exige(abs(dotacion_a_nucleo() - 4185.45) < 0.005, 'Núcleo A: %.2f' % dotacion_a_nucleo())
    exige(abs(dotacion_a_con_testo() - 4684.45) < 0.005, 'A con Testo: %.2f' % dotacion_a_con_testo())
    rell = equipo('rellenadora')
    exige(rell['precio_fuente'] == 0.0 and rell['base_iva'] == 'importe del lector', 'SR-06: rellenadora')
    exige(equipo('testo_270')['base_iva'] == 'con IVA en la ficha', 'SR-06: el Testo no es «sin IVA en ficha»')
    textos_capex = list(BLOQUES_CAPEX.values()) + [p[1] for p in CAPEX_PARTIDAS] + [e['partida'] for e in EQUIPAMIENTO]
    exige(not any('fondo' in t.lower() for t in textos_capex), 'D16: el CAPEX contiene un fondo de maniobra')
    exige(len(BLOQUES_CAPEX) == 11 and all(capex_bloque(n) > 0 for n in BLOQUES_CAPEX), 'Bloques de CAPEX')
    exige(necesita_extincion_automatica() == 0 and riesgo_cocina() == 'bajo', 'Riesgo: %s' % riesgo_cocina())
    exige(abs(distancia_filtro_m() - 1.20) < 1e-9, 'A5: con gas, filtros a 1,20 m')

    # ---- 7. temporada y verano -----------------------------------------------
    exige(len(COEFICIENTES_MES) == 12 and abs(sum(COEFICIENTES_MES) / 12.0 - 1.0) < 1e-9, 'Media de coeficientes')
    exige(all(COEFICIENTES_MES[m - 1] > 1.0 for m in MESES_PICO), 'El pico octubre-marzo no está por encima de 1')
    exige(min(COEFICIENTES_MES) == COEFICIENTES_MES[7], 'Agosto no es el mínimo')
    mejor = max(SALIDAS_VERANO, key=contribucion_verano)
    exige(mejor == SALIDA_VERANO_ELEGIDA, 'La salida elegida no es la de mayor contribución: %s' % mejor)

    # ---- 8. cruces: el grafo sin ciclos (D16) ---------------------------------
    arcos = aristas()
    exige(arcos == ARISTAS_SPEC, 'Aristas fuera de §2.2: %s' % sorted(arcos ^ ARISTAS_SPEC))
    orden, en_ciclo = orden_topologico(arcos, set(LIBROS))
    exige(not en_ciclo, 'CICLO entre libros: %s' % en_ciclo)
    exige(sorted(ORDEN_RELLENO) == sorted(LIBROS) and es_orden_valido(ORDEN_RELLENO, arcos),
          'ORDEN_RELLENO no es un orden topológico')
    exige(not any(7 in a for a in arcos), 'El libro 7 aparece en un cruce')
    _o, canario = orden_topologico(arcos | {(6, 3)}, set(LIBROS))
    exige(bool(canario), 'El detector de ciclos no caza un ciclo sintético')
    exige(not es_orden_valido(ORDEN_RELLENO, arcos | {(6, 2)}), 'No caza una arista hacia atrás')
    celdas = {}
    for c in CRUCES:
        exige(c['valor_defecto'] is not None, 'Cruce %d sin valor por defecto' % c['n'])
        exige(c['hoja_origen'] in HOJAS[c['origen']] and c['hoja_receptor'] in HOJAS[c['receptor']],
              'Cruce %d: hoja inexistente' % c['n'])
        clave = (c['fichero_origen'], c['hoja_origen'], c['celda_origen'])
        exige(celdas.setdefault(clave, c['calcula']) == c['calcula'], 'Cruce %d: celda de origen con dos cifras' % c['n'])
    exige(len(CRUCES) == 52, 'CRUCES: %d celdas' % len(CRUCES))
    for n, hojas in HOJAS.items():
        for h in hojas:
            exige(_hoja_valida(h), 'Nombre de hoja no válido en Excel: %r' % h)

    # ---- 9. legal, franquicias, traspasos y cronograma --------------------------
    for pid in list(IDS_LEGALES_REQUERIDOS) + list(IDS_SIN_NOTA_LEGAL):
        exige(id_existe_en_json_comun(pid), 'Id legal %s fuera del JSON común' % pid)
    faltan = gate_legal(abortar=False)
    exige(not faltan, 'gate_legal: faltan %s' % faltan)
    mc = [f for f in FRANQUICIAS if f['marca'] == 'Maestro Churrero'][0]
    exige(mc['inversion'] == 115000.0 and mc['fuente'] == 'CUS-M14', 'SR-20: Maestro Churrero')
    exige(rango_traspasos(('CUS-02',))[1] == max(t['precio_pedido'] for t in TRASPASOS), 'D15: techo con sala')
    exige(mes_apertura_calculado() == dato(NEGOCIO, 'mes_apertura'), 'El cronograma no abre en septiembre')
    exige(ruta_critica()[2]['H7'] >= 0, 'La maquinaria llega tarde')

    # ---- 10. economía ----------------------------------------------------------
    pyg = cuenta_resultados_crucero()
    exige(pyg['ventas'] > 0 and pyg['beneficio'] > 0, 'El año de crucero no da beneficio')
    exige(0.0 < pyg['margen_neto'] < 0.25, 'Margen neto fuera de lo creíble: %.1f %%' % (100 * pyg['margen_neto']))
    exige(punto_equilibrio_raciones_dia() < raciones_anio() / dias_apertura_anio(),
          'La demanda no llega al punto de equilibrio')
    exige(abs(principal_prestamo() / inversion_total() - dato(FINANCIACION, 'pct_prestamo')) <= 0.005,
          'El punto fijo del principal no ha convergido')

    # ---- 11. tildes ----------------------------------------------------------------
    # El canario se compone en tiempo de ejecución: escrito entero sería un literal del
    # propio fichero y el gate lo denunciaría.
    canario = erratas_de_tilde(['La raci' + 'on del dia y el caf' + 'e con leche'])
    exige(set(canario) == {'racion', 'cafe'}, 'El gate de tildes no caza su canario: %s' % canario)
    t = gate_tildes()
    exige(not t['erratas'], 'Palabras sin tilde que el léxico tiene con tilde: %s' % sorted(t['erratas'].items())[:20])
    if t['letra_caida']:
        avisos.append('documentos.erratas_ortograficas marca %d palabras (letra caída): %s'
                      % (len(t['letra_caida']), ', '.join(d['errata'] for d in t['letra_caida'][:12])))

    # ---- 12. contraste con el Pack APPCC 09 (un xlsx, read_only) ----------------
    try:
        import openpyxl                                        # noqa: PLC0415
        wb = openpyxl.load_workbook(PACK_APPCC_09, read_only=True)
        try:
            hojas = wb.sheetnames
        finally:
            wb.close()
        exige('Control Aceite' in hojas and 'Retirada de aceite usado' in hojas,
              'El Pack APPCC 09 ya no tiene las hojas que cita el libro 4: %s' % hojas)
    except Exception as e:                                     # noqa: BLE001
        avisos.append('No se pudo abrir el Pack APPCC 09: %s' % e)

    _resumen(pyg, t, a2, a3, a4)
    for a in avisos:
        print('AVISO: %s' % a)
    if fallos:
        print('\n%d FALLO(S):' % len(fallos))
        for f in fallos:
            print('  x %s' % f)
        raise SystemExit(1)
    print('\nTODAS LAS COMPROBACIONES EN VERDE.')
    return True


def _eur(v):
    return ('%.2f' % v).replace('.', ',')


def _resumen(pyg, t, a2, a3, a4):
    print('«%s» - juego de datos único de «Cómo Montar una Churrería-Chocolatería»' % dato(NEGOCIO, 'nombre'))
    print('Datos a %s · verificación legal CUN %s · CHN %s\n'
          % (FECHA_DATOS, FECHA_VERIFICACION_CUN, FECHA_VERIFICACION_CHN))
    print('LOCAL Y HORARIO')
    print('  %.0f m² en %d zonas + terraza de %.0f m² · %.1f h de apertura a la semana'
          % (dato(NEGOCIO, 'm2_total'), len(ZONAS), dato(NEGOCIO, 'm2_terraza'), horas_apertura_semana()))
    print('  apertura el %d de %s · renta %s €/mes · huecos de cobertura: %d'
          % (dato(NEGOCIO, 'dia_apertura'), MESES[dato(NEGOCIO, 'mes_apertura') - 1].lower(),
             _eur(dato(NEGOCIO, 'renta_mensual')), len(huecos_de_cobertura())))
    print('\nPLANTILLA Y NOCTURNIDAD (convenio de ejemplo %s, tablas 2025)' % dato(CONVENIO, 'codigo'))
    for p in PLANTILLA:
        a = analisis_nocturnidad(p['id'])
        print('  %s %-27s %4.1f h/sem · nivel %-3s · coste %9s € · 22-6: %.1f h, ET: %s · plus %s €'
              % (p['id'], p['puesto'], horas_semana(p['id']), p['nivel'], _eur(coste_puesto_anual(p['id'])),
                 a['horas_22_6_semana'], a['trabajador_nocturno_et'] if not p['es_titular'] else 'titular',
                 _eur(plus_nocturnidad_anual(p['id']))))
    print('  coste hora %s €/h · plantilla anual (X15) %s € · titular %.1f h/sem (%.1f h de 0 a 8)'
          % (_eur(coste_hora_mano_obra()), _eur(coste_plantilla_anual()), horas_titular(), horas_titular_0_8()))
    print('\nCARTA (PVP con IVA · base sin IVA en sala · mix invierno / verano)')
    for r in CARTA:
        print('  %-4s %-52s %-22s %6s € %6s € %5.1f / %4.1f'
              % (r['id'], r['nombre'][:52], r['familia'][:22], _eur(r['pvp']), _eur(pvp_sin_iva(r, 'sala')),
                 r['mix_invierno'], r['mix_verano']))
    print('  ticket sin IVA: invierno %s € (sala %s, llevar %s) · verano %s €'
          % (_eur(ticket_sin_iva('invierno')), _eur(_ticket_sala()), _eur(_ticket_llevar()), _eur(_ticket_verano())))
    print('  materia + aceite absorbido por ración: invierno %s € · verano %s € · kg de masa por ración %.4f'
          % (_eur(materia_por_racion('invierno')), _eur(materia_por_racion('verano')), kg_masa_por_racion_media()))
    print('  los dos márgenes: sobre materia %.1f %% · tras mano de obra %.1f %% (%.1f min por ración)'
          % (100 * margen_sobre_materia(), 100 * margen_tras_mano_de_obra(), minutos_mano_obra_por_racion()))
    print('\nPRODUCCIÓN Y ACEITE')
    print('  %.0f kW computables, riesgo %s; capacidad %.0f raciones/h (manda: %s)'
          % (kw_computables(), riesgo_cocina(), capacidad_raciones_h(), equipo_que_manda()))
    print('  cola del domingo de diciembre: %.1f raciones/h · kg fritos: tipo %.1f, punta %.1f'
          % (cola_del_domingo(12), kg_fritos_dia('tipo'), kg_fritos_dia('punta')))
    print('  aceite %s €/L · renovación %s €/ración · reposición %.2f L/día · %.0f L al gestor al mes'
          % (_eur(precio_aceite_eur_l()), _eur(renovacion_por_racion()), reposicion_litros_dia(), litros_al_gestor_mes()))
    print('\nINVERSIÓN (sin fondo de maniobra) Y PLAN')
    print('  dotación B %s € / con Testo %s € · dotación A %s € / con Testo %s €'
          % (_eur(dotacion_b_nucleo()), _eur(dotacion_b_con_testo()), _eur(dotacion_a_nucleo()), _eur(dotacion_a_con_testo())))
    print('  CAPEX %s € (equipamiento y mobiliario %s € frente a los %s € declarados en Vallecas) · IVA a adelantar %s €'
          % (_eur(capex_total()), _eur(equipamiento_y_mobiliario()), _eur(DOTACION_COMPLETA_DECLARADA[0]),
             _eur(iva_soportado_capex())))
    print('  fondo de maniobra (sólo libro 6) %s € · inversión total %s € · préstamo %s €'
          % (_eur(fondo_maniobra()), _eur(inversion_total()), _eur(principal_prestamo())))
    print('  año de crucero: %.0f raciones · ventas %s € · beneficio %s € · margen neto %.1f %%'
          % (raciones_anio(), _eur(pyg['ventas']), _eur(pyg['beneficio']), 100 * pyg['margen_neto']))
    print('  punto de equilibrio %.0f raciones/día · verano con fijos: %s'
          % (punto_equilibrio_raciones_dia(), ' / '.join('%s %s €' % (s, _eur(verano_con_fijos(s))) for s in SALIDAS_VERANO)))
    print('\nCRUCES Y DECISIONES')
    print('  %d celdas cruzadas, %d aristas, orden %s · %d ids legales en verde'
          % (len(CRUCES), len(aristas()), ' -> '.join(str(x) for x in ORDEN_RELLENO), len(IDS_LEGALES_REQUERIDOS)))
    for n, texto in sorted(cifras_decisiones().items()):
        print('  %2d. %s' % (n, texto))
    print('\nGATE DE TILDES')
    print('  palabras sin tilde que el léxico tiene con tilde: %d' % len(t['erratas']))
    print('  letras con tilde por 1.000 letras: %.2f (la hermana: %s)'
          % (t['tasa'], '%.2f' % t['tasa_hermana'] if t['tasa_hermana'] is not None else 'sin dato'))


_ERROR_CRUCES = None


def _rellenar_valores_cruces():
    """Calcula el valor por defecto de cada celda cruzada. Si un parámetro se queda sin
    valor, el error no revienta la importación: lo informa `comprobar()`."""
    global _ERROR_CRUCES
    try:
        for c in CRUCES:
            c['valor_defecto'] = valor_cruce(c)
        _ERROR_CRUCES = None
    except Exception as e:                                     # noqa: BLE001
        _ERROR_CRUCES = repr(e)


_rellenar_valores_cruces()


if __name__ == '__main__':
    comprobar()
