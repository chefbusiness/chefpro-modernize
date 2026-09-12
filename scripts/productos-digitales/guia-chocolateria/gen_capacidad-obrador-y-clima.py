#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_capacidad-obrador-y-clima.py — libro 1 de «Cómo Montar una Chocolatería»
(SPEC §2.2 fila 1; decisiones D31, D32, D33 y §3.1).

Hojas: Instrucciones · Parámetros · Zonas y m2 · Clima del Obrador ·
Capacidad por Equipo · Cuello de Botella · Ficha de Visita a Local.

QUÉ DECIDE ESTE LIBRO
---------------------
Si ESE local sirve, y cuántos bombones al día aguanta el equipo que estás
comprando. Las dos se contestan ANTES de firmar nada, y en chocolate hay una
tercera que no existe en pastelería: si el local se puede climatizar para que
la cobertura cristalice.

MOLDE Y DIFERENCIAS CON LA HERMANA (SPEC §2.4)
----------------------------------------------
Se calca `guia-pasteleria/gen_capacidad-obrador-y-local.py` (Zonas y m2,
Capacidad por Equipo, Cuello de Botella, Ficha de Visita). **Fuera: horno,
salida de humos y fermentación.** **Nuevo: la hoja «Clima del Obrador»**, con
el semáforo de coherencia y la ficha de preguntas al instalador (D33).

* **PROHIBIDO CALCULAR CARGA TÉRMICA (D33).** No hay un solo coeficiente con
  fuente —ni transmitancia, ni coeficiente por m3, ni aportes, ni
  renovaciones—, y las dos salidas posibles están prohibidas: inventar
  constantes, o dejar celdas verdes que el lector no sabe rellenar. Lo que sí
  es construible, y sigue siendo diferencial, es (a) un semáforo de coherencia
  entre la temperatura objetivo, la exterior de agosto de SU ciudad y la
  potencia frigorífica que le OFREZCA EL INSTALADOR, y (b) una ficha de
  preguntas al instalador. La única cifra derivada que publica la hoja
  —kW por m2 climatizado— sale de lo que el lector teclea, va SIN semáforo y
  dice en su propia nota que no es un criterio de dimensionado: es la cifra
  que le enseña al segundo instalador para comparar dos ofertas.
* **Las cinco temperaturas son las del kit (D31)**, y la del obrador cita SÓLO
  `08-apertura-cierre-negocio.xlsx!Apertura del Negocio`: la discrepancia
  interna del kit no se publica (R3-M2).
* **No hay temperatura legal del chocolate** (`CHN-30`, `CHN-87`): el art. 4.2
  del RD 1021/2022 va por la etiqueta de quien envasa, y ese decreto no nombra
  el chocolate ni una vez. Quien fija la temperatura de la vitrina y de la
  cámara es TU sistema de autocontrol. La hoja lo dice y lo lleva en nota.

LO QUE NO HACE, Y DÓNDE SE HACE (SPEC §2.7)
-------------------------------------------
* **No publica curvas de templado ni fichas de moldeado** (K1): eso es
  `kit-tareas-chocolateria/02-partidas-produccion.xlsx`. Aquí sólo hay
  capacidad y clima, no técnica.
* **No repite el calendario de campañas** (K2, `BONUS-02`). El pico entra sólo
  como multiplicador de bombones al día; los euros de cada campaña son el
  libro 6.
* **No dimensiona la plantilla.** Las horas de turno entran como parámetro; el
  personal es la hoja «Personal» del libro 7 (§2.7: aquí NO hay
  `plantilla-turnos-y-coste-personal`, y es la única baja frente al molde).
* **El precio y el plazo de cada equipo son los libros 2 y 9.** Aquí el equipo
  entra sólo por su CAPACIDAD.

DECISIONES TÉCNICAS
-------------------
* **La unidad de capacidad es el BOMBÓN EQUIVALENTE**, y no es un invento: es
  el minuto de obrador de la tanda de referencia (`BC1`: 24 cavidades x 6
  moldes en 155 minutos, `datos_ejemplo.CARTA`). Una caja de 35 bombones no es
  una pieza: son 35 bombones moldeados más el montaje de la caja. Contarla
  como una sola pieza -que es lo que sale de `piezas_dia_crucero()`- subestima
  el obrador por un factor 5, y ése es justo el error de bulto que esta hoja
  existe para evitar.
* **Un solo modelo de capacidad para los once equipos**, y por eso se pueden
  comparar: `capacidad por ciclo x piezas por unidad de capacidad` = piezas
  por ciclo; `INT(minutos disponibles / minutos por ciclo)` = ciclos al día; y
  el **porcentaje del surtido que pasa por ese equipo** convierte su producción
  en los bombones de obrador que permite.
* El **cuello de botella es un `MIN` sobre una columna visible**, no un
  `SUMPRODUCT` que nadie puede auditar, y el equipo que limita sale con
  `INDEX/MATCH` sobre esa misma columna. Los equipos que no tienes devuelven
  `""` y `MIN` los ignora.
* **La ficha de visita distingue el dato medido del juicio**, y cuatro ítems
  tienen umbral numérico calculado desde «Parámetros». Uno de ellos se compara
  al REVÉS (la superficie de venta contra los 750 m2 de la Ley 12/2012), y por
  eso cada ítem declara su sentido.
* Cero constantes dentro de las fórmulas de cálculo; `IFERROR(...,"")` en toda
  división; «sin dato» = `""`; semáforos con `ISNUMBER`; desplegables contra
  RANGO; prohibidas `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`,
  `LAMBDA`, `RANK`, `NETWORKDAYS` e `IRR`: cero usos. Textos WinAnsi (cp1252).
* **Cero fórmulas que crucen ficheros.** Este libro es ORIGEN de dos de los
  ocho cruces (6 <- 1 y 7 <- 1) y receptor de ninguno, así que no lleva
  ninguna celda «trae aquí la cifra de»: las que la llevan son el 6 y el 7.

Salida fija: build/capacidad-obrador-y-clima.xlsx + mapa-capacidad-obrador-y-clima.json
Via: Claude Code
"""
import json
import os
import subprocess
import sys

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..'))
sys.path.insert(0, os.path.join(RAIZ, 'guias-v2_0'))
sys.path.insert(0, AQUI)

import motor                                                   # noqa: E402
import datos_ejemplo as D                                      # noqa: E402
import _comun_chocolateria as C                                # noqa: E402

motor.CTX['producto'] = C.PID

NOMBRE = 'capacidad-obrador-y-clima'
TITULO = 'Capacidad del obrador, clima y ficha de visita al local'

H_PAR = 'Parámetros'
H_ZON = 'Zonas y m2'
H_CLI = 'Clima del Obrador'
H_CAP = 'Capacidad por Equipo'
H_CUE = 'Cuello de Botella'
H_LOC = 'Ficha de Visita a Local'

#: Ids legales que este libro cita en celda. Se comprueban ANTES de escribir.
IDS_LEGALES = {
    'CHN-30': ('NO hay temperatura legal del chocolate: la declaras tú en tu '
               'APPCC', 1),
    'CHN-87': ('El RD 1021/2022 no nombra el chocolate ni una vez', 1),
    'CHN-45': ('El DB-HS 3 del CTE no regula un local comercial', 1),
    'CHN-46': ('El obrador de chocolate no genera aire AE4', 1),
    'CHN-48': ('Gas: inspección cada cinco años (variante de taza y churros)', 1),
    'CHN-49': ('Ninguna licencia previa de actividad hasta 750 m2', 1),
    'CHN-49b': ('El epígrafe 644.5 está en el Anexo de la Ley 12/2012', 1),
    'CHN-49c': ('La chocolatería de taza NO entra en la Ley 12/2012', 1),
    'CHN-78': ('Accesibilidad: RD 193/2023', 1),
    'CHN-32': ('APPCC con responsable designado con nombre', 1),
}

SI_NO = ('Sí', 'No')
RESPUESTAS = ('Sí', 'No', 'Por comprobar')
POR_ESCRITO = ('Sí', 'No', 'Por pedir')

#: Umbral de la Ley 12/2012: 750 m2 de superficie útil de exposición y venta
#: (`CHN-49`, `CHN-49b`). Vive en «Parámetros», nunca dentro de una fórmula.
UMBRAL_750 = 750.0


# --------------------------------------------------------------------------
# La unidad de capacidad: el BOMBÓN EQUIVALENTE
# --------------------------------------------------------------------------
#: Minutos de obrador de UN bombón de la tanda de referencia (`BC1`). Todo lo
#: demás se mide contra él. No es un coeficiente inventado: sale de
#: `minutos_mo_tanda` y `piezas_por_tanda` de la propia carta.
_BASE = D.ref('BC1')
MIN_POR_BOMBON = _BASE['minutos_mo_tanda'] / D.piezas_por_tanda(_BASE)


def equiv_bombones(r):
    """Bombones equivalentes de obrador de UNA unidad vendible.

    Una caja NO es una pieza: son sus bombones moldeados (uno a uno) más el
    montaje de la caja, que la carta mide en `minutos_mo_tanda`. Contarla como
    una pieza subestima el obrador por un factor 5.
    """
    if D.es_caja(r):
        return (sum(n for _i, n in r['composicion_caja'])
                + r['minutos_mo_tanda'] / MIN_POR_BOMBON)
    return (r['minutos_mo_tanda'] / D.piezas_por_tanda(r)) / MIN_POR_BOMBON


#: Equivalencia MEDIA PONDERADA de la carta por el mix: cuántos bombones de
#: obrador hay detrás de cada pieza vendible que sale por el mostrador.
EQUIV_MEDIA = round(sum(r['mix_pct'] * equiv_bombones(r) for r in D.CARTA)
                    / sum(r['mix_pct'] for r in D.CARTA), 2)
#: Lo que el obrador tiene que sacar un día normal, en bombones equivalentes.
OBJETIVO_DIA = D.piezas_dia_crucero() * EQUIV_MEDIA


def factor_pico(c):
    """Multiplicador del día de campaña sobre el día normal.

    Sale del producto estrella de esa campaña -que pone el kit- llevado a
    bombones equivalentes: `(uds de campaña - uds normales) x equivalencia`.
    Los campos económicos de `CAMPANAS` son supuestos declarados, y esta
    derivación también: por eso la celda es VERDE.
    """
    r = D.ref(c['producto_estrella'])
    extra = (c['uds_dia_pico'] - c['uds_dia_normal']) * equiv_bombones(r)
    return round(1.0 + extra / OBJETIVO_DIA, 2)


# --------------------------------------------------------------------------
# Parámetros del libro: (etiqueta, valor, unidad, procedencia, nota)
# --------------------------------------------------------------------------
P_INI = 6
PARAMS_LIBRO = [
    ('Horas de turno del obrador', D.NEGOCIO['horas_turno'], 'h por turno',
     D.NEGOCIO['fuente_horas_turno'],
     'Duración del turno de obrador. Es el número que multiplica todo lo '
     'demás: con dos turnos, la capacidad se duplica sin comprar una sola '
     'máquina, y en chocolate el segundo turno es más barato que en '
     'pastelería porque no hay madrugada.'),
    ('Turnos de obrador al día', 1, 'turnos', 'supuesto',
     'La Almendra trabaja a un turno. Súbelo a 2 y mira la hoja «Cuello de '
     'Botella» antes de comprar una máquina más grande.'),
    ('Horas productivas sobre la jornada', D.P('ratio_horas_productivas'), '%',
     D.PARAMS['ratio_horas_productivas'][1],
     D.PARAMS['ratio_horas_productivas'][2]),
    ('Minutos disponibles al día', None, 'minutos', 'Se calcula',
     'Horas de turno x turnos x horas productivas x 60. De aquí salen los '
     'ciclos al día de cada equipo.'),
    ('Días de apertura a la semana', D.NEGOCIO['dias_apertura_semana'], 'días',
     D.NEGOCIO['fuente_dias_apertura'], D.NEGOCIO['nota_dias_apertura']),
    ('Días de apertura al año', D.NEGOCIO['dias_apertura_anio'], 'días',
     D.NEGOCIO['fuente_dias_apertura'],
     '6 días por semana x 52 semanas = 312, menos 8 días de cierre por '
     'festivos. En agosto la TIENDA no cierra: lo que para es el obrador.'),
    ('Piezas vendibles al día en velocidad de crucero',
     round(D.piezas_dia_crucero(), 1), 'piezas al día', 'supuesto',
     'Clientes al día x piezas por ticket, los dos supuestos: no existe dato '
     'público de tráfico de bombonería, y `N-13` prohíbe publicar uno. Una '
     '«pieza vendible» es lo que entra en la bolsa: un bombón suelto, una '
     'tableta o UNA CAJA. Si ya tienes el Kit de Tareas Chocolatería, '
     'sustitúyelo por tu dato real de '
     'kit-tareas-chocolateria/02-partidas-produccion.xlsx.'),
    ('Bombones equivalentes por pieza vendible', EQUIV_MEDIA,
     'bombones por pieza', 'supuesto derivado de la carta',
     'LA COLUMNA QUE EVITA EL ERROR DE BULTO. Una caja de 35 bombones no es '
     'una pieza de obrador: son 35 bombones moldeados más el montaje de la '
     'caja. Sale de los minutos de mano de obra por tanda de cada referencia '
     'de la carta, medidos contra la tanda de referencia (24 cavidades x 6 '
     'moldes en 155 minutos). Con tu propio mix, recalcúlala.'),
    ('Bombones equivalentes al día en velocidad de crucero', None,
     'bombones al día', 'Se calcula',
     'Piezas vendibles x bombones equivalentes por pieza. Es el número contra '
     'el que se mide TODA la capacidad de este libro.'),
    ('Margen de seguridad exigido sobre la capacidad', 0.10, '%', 'supuesto',
     'Holgura mínima que quieres tener sobre el día normal. Por debajo de '
     'ella el libro avisa: una avería del frío, una baja o un pedido '
     'corporativo te dejan sin género aunque en teoría llegues.'),
    ('Superficie total del local', D.NEGOCIO['m2_total'], 'm2',
     D.NEGOCIO['fuente_m2'], D.NEGOCIO['nota_m2']),
    ('Parte mínima del local dedicada a producción', 0.55, '%', 'supuesto',
     'Criterio de la casa, no norma: por debajo de esto la tienda se come al '
     'obrador y acabas comprando bombón hecho. En chocolate la zona de '
     'producción son cuatro zonas, no una: obrador, cámara, almacén de '
     'cobertura y envasado.'),
    ('Potencia eléctrica instalada total prevista',
     D.NEGOCIO['potencia_instalada_kw'], 'kW',
     D.NEGOCIO['fuente_potencia_instalada'], D.NEGOCIO['nota_potencia']),
    ('Temperatura exterior de tu ciudad en agosto',
     D.NEGOCIO['t_exterior_agosto_c'], 'grados C',
     D.NEGOCIO['fuente_t_exterior'], D.NEGOCIO['nota_t_exterior']),
    ('Potencia frigorífica que te OFRECE el instalador',
     D.NEGOCIO['potencia_frigorifica_ofertada_kw'], 'kW',
     D.NEGOCIO['fuente_potencia_frigorifica'],
     'LA QUE TE OFRECE ÉL, no la que calcula este libro: este libro NO calcula '
     'carga térmica, y lo dice en la hoja «Clima del Obrador». Pídela por '
     'escrito con el salto de temperatura de diseño al lado.'),
    ('Salto de temperatura de diseño que declara el instalador', 16.0,
     'grados C', 'supuesto',
     'El salto de temperatura para el que ha dimensionado su equipo. Es la '
     'pregunta que casi '
     'nadie hace, y la que decide si esa oferta sirve en agosto: si ha '
     'diseñado para un salto menor que el tuyo, el equipo no llega el día que '
     'de verdad hace falta.'),
    ('Altura libre mínima que exiges al local', 2.7, 'm', 'supuesto',
     'Un obrador de chocolate no lleva campana ni conducto a cubierta, así '
     'que necesita menos altura que una pastelería. Lo que sí necesita es '
     'sitio para la unidad interior de la climatización y para el conducto de '
     'la deshumidificación.'),
    ('Número de zonas del local', len(D.ZONAS), 'zonas', 'supuesto',
     'Las seis zonas de La Almendra. NO es el reparto de una pastelería: aquí '
     'no hay zona de horno ni de fermentación, y sí cámara climatizada.'),
    ('Superficie máxima de venta sin licencia previa (Ley 12/2012)',
     UMBRAL_750, 'm2', 'CHN-49 + CHN-49b',
     'Ningún ayuntamiento puede exigirte licencia previa de instalación, de '
     'funcionamiento o de actividad hasta 750 m2 de superficie útil de '
     'exposición y venta al público, porque el epígrafe 644.5 «Comercio al '
     'por menor de bombones y caramelos» está en el Anexo de la Ley 12/2012. '
     'OJO: la chocolatería de TAZA (grupo 676) NO está en ese Anexo '
     '(`CHN-49c`), así que la variante de taza y churros no se libra.'),
]
P_HORAS, P_TURNOS, P_PROD, P_MIN_DIA = 0, 1, 2, 3
P_DIAS_SEM, P_DIAS_ANIO, P_PIEZAS, P_EQUIV, P_OBJ = 4, 5, 6, 7, 8
P_MARGEN, P_M2, P_MIN_PROD, P_POT = 9, 10, 11, 12
P_TEXT, P_POTFRIG, P_DT_INST, P_ALTURA, P_ZONAS, P_750 = 13, 14, 15, 16, 17, 18


def fila_par(i):
    return P_INI + i


# --------------------------------------------------------------------------
# Equipos que marcan capacidad. Todo lo que no es capacidad (precio, plazo,
# IVA) vive en los libros 2 y 9: aquí el equipo entra sólo por lo que produce.
#
# (nombre, categoría, ¿lo tienes?, capacidad por ciclo, unidad, piezas por
#  unidad, minutos por ciclo, % del surtido, procedencia, nota)
# --------------------------------------------------------------------------
C_INI = 6
#: Bombones que salen de un kilo de cobertura, con los 5,5 g de chocolate por
#: pieza de la tanda de referencia (`datos_ejemplo.CARTA`, `BC1`).
BOMBONES_POR_KG = round(1000.0 / _BASE['g_chocolate'])

EQUIPOS_CAPACIDAD = [
    ('Atemperadora continua de sobremesa, 12 kg (55 kg/h) — Selmi One',
     'Templado', 'Sí', 12, 'kg de cobertura por carga de cuba',
     BOMBONES_POR_KG, 180, 1.00, 'CHS-41a',
     'El corazón del obrador, la decisión 2 del bonus 2 y la máquina que más '
     'se mira al presupuestar. Fíjate en dónde queda en el cuello de botella: '
     'templar NO es lo que limita una bombonería artesana. Los bombones por '
     'kilo salen de los 5,5 g de chocolate de la tanda de referencia; cámbialos '
     'si tu pieza pesa otra cosa.'),
    ('Temperador de baño maría digital, 22 L — segunda cobertura',
     'Templado', 'Sí', 8, 'kg de cobertura por carga',
     BOMBONES_POR_KG, 180, 0.35, 'CHS-41j',
     'La segunda línea de templado. Sin ella no se trabajan dos coberturas a '
     'la vez, y el 35 % es la parte del surtido que lleva una cobertura '
     'distinta de la principal.'),
    ('Mantenedor de 1 cubeta, digital', 'Templado', 'Sí', 5,
     'kg mantenidos a punto', BOMBONES_POR_KG, 240, 0.20, 'CHS-41i',
     'Mantiene la cobertura en curva mientras se moldea. Su precio se publica '
     'como un «desde» (libro 2); su capacidad, aquí, en kilos.'),
    ('Moldes de policarbonato (24 moldes de 24 cavidades)', 'Moldeado', 'Sí',
     24, 'moldes por ciclo de cristalización', 24, 90, 0.72, 'CHS-45a',
     'LOS MOLDES QUE TIENES SON CAPACIDAD, no utillaje. El ciclo incluye '
     'llenado, vibrado, raspado, cristalización y desmoldeo: 90 minutos es un '
     'supuesto, mídelo con tu cobertura y tu cámara. Los 24 moldes valen entre '
     '580,80 y 1.027,92 euros (libro 2), y comprar 12 más es la forma más '
     'barata que hay de subir capacidad.'),
    ('Puesto de moldeado y desmoldeo (mesa de mármol o granito)',
     'Moldeado', 'Sí', 2, 'puestos trabajando en paralelo',
     D.piezas_por_tanda(_BASE), _BASE['minutos_mo_tanda'], 0.95, 'supuesto',
     'LAS MANOS, QUE SON LO QUE DE VERDAD LIMITA. Dos puestos son las dos '
     'personas de obrador de La Almendra (Encargado y Chocolatero). Los '
     'minutos por ciclo y las piezas por tanda salen de la tanda de referencia '
     'de la carta, no de una estimación: 24 cavidades x 6 moldes en 155 '
     'minutos.'),
    ('Placa dosificadora de rellenos — Selmi', 'Moldeado', 'Sí', 6,
     'moldes dosificados por ciclo', 24, 12, 0.68, 'CHS-42i',
     'Dosifica el relleno en el molde ya encamisado. Es rápida y por eso no '
     'limita: lo que limita es lo que pasa antes y después de ella.'),
    ('Enrobadora de banda, 200 mm — Selmi R200 Legend', 'Bañado', 'Sí', 1,
     'horas de banda en marcha', 640, 60, 0.18, 'CHS-42a',
     'Sólo el 18 % del surtido va bañado: el resto es moldeado. Una enrobadora '
     'con una banda de 200 mm produce muy por encima de lo que una bombonería '
     'artesana necesita, y ése es el dato que hay que tener delante antes de '
     'comprarla.'),
    ('Cámara climatizada de chocolate, unos 6 m2', 'Frío y cristalización',
     'Sí', 6, 'm3 útiles por rotación', 480, 240, 0.85, 'supuesto',
     'Aquí el «ciclo» es una rotación de la cámara. NO es una nevera: trabaja a '
     '15-18 grados C con 50-60 % de humedad, y es lo que sostiene la '
     'cristalización y la vida útil que declares en tu APPCC.'),
    ('Puesto de envasado y montaje de cajas', 'Envasado', 'Sí', 1,
     'puestos de envasado', 128, 100, 1.00, 'supuesto',
     'LA ZONA QUE NADIE DIBUJA EN EL PLANO Y QUE SE DESBORDA EN NAVIDAD. En '
     'bombonería la caja ES el producto en campaña: montarla, pesarla, '
     'etiquetarla y cerrarla cuesta tiempo de obrador, y ese tiempo no está en '
     'la ficha de ninguna máquina.'),
    ('Vitrina refrigerada específica para chocolate — Docriluc WB-6-6-R',
     'Tienda y vitrina', 'Sí', 0.6, 'm2 de exposición por reposición', 520,
     150, 0.55, 'CHS-43',
     'Rango de trabajo del equipo +14/+17 grados C. NO son los +2/+4 de una '
     'vitrina de pastelería, que arruina el bombón por condensación y pérdida '
     'de brillo. El objetivo operativo de cada mañana lo pone el kit: 16-18 '
     'grados C y menos del 55 % de humedad.'),
    ('Atemperadora de arranque, 4,5 L (unos 3 kg) — Pavoni MINITEMPER',
     'Templado', 'No', 3, 'kg de cobertura por carga', BOMBONES_POR_KG, 45,
     1.00, 'CHS-41h',
     'OPCIONAL, y marcada «No» a propósito: es la máquina del ESCENARIO B, el '
     'arranque mínimo. Cámbiala a «Sí» y mira cómo se mueve el cuello de '
     'botella antes de gastarte el dinero de la continua.'),
]

# --------------------------------------------------------------------------
# Clima: las CINCO temperaturas del kit (D31) y su orden lógico
# --------------------------------------------------------------------------
CLAVES_CLIMA = ('obrador', 'camara', 'nevera_rellenos', 'sala_tienda',
                'vitrina')
L_CLI_INI = 7          # primera fila de la tabla de climas

#: Comprobaciones de coherencia ENTRE ventanas. (etiqueta, clave A, campo A,
#: operador, clave B, campo B, nota). Todas son aritmética sobre lo que el
#: lector teclea: ni un coeficiente.
COHERENCIAS = [
    ('La cámara está por debajo del obrador', 'camara', 'max', '<=',
     'obrador', 'min',
     'El bombón acabado sale del obrador y entra en la cámara: si la cámara '
     'está más caliente que el obrador, la cámara no conserva nada.'),
    ('La sala de tienda está por encima del obrador', 'sala_tienda', 'min',
     '>=', 'obrador', 'max',
     'La sala es para el cliente y el obrador para el chocolate. Son dos '
     'climas distintos que conviven en el mismo local, y por eso la puerta '
     'entre los dos importa.'),
    ('La vitrina está por debajo de la sala', 'vitrina', 'max', '<=',
     'sala_tienda', 'min',
     'La vitrina tiene su propio control porque la sala la calienta. Si el '
     'escaparate da al sol de mediodía, esto deja de cumplirse solo.'),
    ('La nevera de rellenos está por debajo de la cámara', 'nevera_rellenos',
     'max', '<=', 'camara', 'min',
     'La nevera es la del RELLENO, a 0-4 grados C. El bombón acabado NO va a 4 '
     'grados C: condensa, y el agua de la condensación disuelve el azúcar de '
     'la superficie.'),
]

#: Ficha de preguntas al instalador (D33.b). (pregunta, unidad, tipo, valor
#: por defecto, por qué importa). `tipo` = 'num' o 'sino'.
F_INST_INI = 6
PREGUNTAS_INSTALADOR = [
    ('¿Qué volumen en m3 has tomado para el obrador?', 'm3', 'num', 78.0,
     'Los metros cuadrados de la hoja «Zonas y m2» por la altura libre. Si el '
     'número que ha usado no se parece al tuyo, ha dimensionado otro local.'),
    ('¿Para qué salto de temperatura de diseño lo has calculado?',
     'grados C', 'num', 16.0,
     'Es LA pregunta. Un equipo dimensionado para un salto de 10 grados no '
     'sostiene 18-20 grados C dentro con 36 fuera, y en agosto es cuando se '
     'nota.'),
    ('¿Qué aportes internos has contado?', 'kW', 'num', 3.5,
     'La atemperadora, el temperador, las luces y las personas calientan el '
     'obrador desde dentro. Un equipo calculado sin ellos se queda corto '
     'justo cuando estás produciendo.'),
    ('¿Cuántas renovaciones de aire por hora has previsto?', 'ren/h', 'num',
     2.0,
     'Cada renovación mete aire de la calle a la temperatura y la humedad de '
     'la calle. Es la partida que más sube la potencia y la que menos se '
     'mira.'),
    ('¿Qué capacidad de deshumidificación lleva, y a qué humedad la '
     'mantiene?', 'litros/24 h', 'num', 30.0,
     'En chocolate la HUMEDAD es tan importante como la temperatura: por '
     'encima del 60 % la cobertura templada pierde brillo y el bombón suda al '
     'salir de la cámara.'),
    ('¿El equipo deshumidifica SIN bajar la temperatura por debajo del '
     'objetivo?', 'Sí o No', 'sino', 'Sí',
     'Muchos equipos deshumidifican enfriando. Si el tuyo baja de 18 grados '
     'para secar el aire, la cobertura se te queda dura en la cuba.'),
    ('¿Lleva climatizador evaporativo?', 'Sí o No', 'sino', 'No',
     'TIENE QUE SER «No». Un evaporativo enfría AÑADIENDO humedad, que es '
     'exactamente lo contrario de lo que necesita un obrador de chocolate. Es '
     'el error más caro de esta lista porque parece barato.'),
    ('¿Está incluida la puesta en marcha y el equilibrado de la instalación?',
     'Sí o No', 'sino', 'Sí',
     'Un equipo bien elegido y mal equilibrado no mantiene la ventana. Que lo '
     'diga el presupuesto, no el comercial.'),
    ('¿Qué garantía y qué contrato de mantenimiento ofreces?', 'meses', 'num',
     24.0,
     'El frío y la climatización son lo que no puede pararse un 20 de '
     'diciembre. El mantenimiento es un gasto fijo del libro 7, no un extra.'),
    ('¿Qué consumo eléctrico tiene en agosto a plena carga?', 'kW', 'num',
     4.2,
     'Va a la potencia a contratar de la ficha de visita y al renglón de '
     'suministros del plan financiero. Un obrador de chocolate no tiene '
     'hornos: lo que consume es esto y el frío.'),
]

# --------------------------------------------------------------------------
# Ficha de visita: (ítem, eliminatorio, cómo se comprueba, respuesta por
#  defecto, dato medido o None, clave de umbral o None, sentido, nota, id)
# `sentido` = '>=' (el dato tiene que llegar al umbral) o '<=' (no pasarlo).
# --------------------------------------------------------------------------
L_INI = 6
VISITA = [
    ('La potencia eléctrica contratable llega a la que vas a instalar', 'Sí',
     'Pide el boletín eléctrico del local y consulta a la distribuidora la '
     'potencia disponible en la acometida.', 'Sí', 34.0, 'POTENCIA', '>=',
     'Un obrador de chocolate no tiene hornos, pero tiene TRES equipos de frío '
     'y una climatización con deshumidificación funcionando 24 horas. Subir la '
     'potencia de una acometida puede costar más que la obra entera y depende '
     'de la distribuidora, no de tu presupuesto.', None),
    ('El local admite climatizar el obrador con deshumidificación', 'Sí',
     'Lleva la ficha de preguntas de la hoja «Clima del Obrador» a la visita y '
     'mira dónde iría la unidad exterior y por dónde saldría el condensado.',
     'Sí', None, None, None,
     'ES LA ELIMINATORIA PROPIA DE UNA CHOCOLATERÍA. Sin 18-20 grados C y '
     '50-60 % de humedad en el obrador, la cobertura no cristaliza y el bombón '
     'sale mate o con fat bloom. Un local que no se puede climatizar no es un '
     'local barato: es otro negocio.', None),
    ('La superficie útil llega a los m2 que has repartido por zonas', 'No',
     'Superficie útil real, sin contar muros ni patinillos. Compárala con el '
     'total de la hoja «Zonas y m2».', 'Sí', 77.0, 'SUPERFICIE', '>=',
     'La superficie de un anuncio suele ser construida. La que te sirve es la '
     'útil, y entre una y otra se van con facilidad 10 m2.', None),
    ('La altura libre del local llega a la que has fijado', 'No',
     'Metro láser desde el suelo terminado a la cara inferior del forjado, en '
     'el punto más bajo. Mide donde iría la unidad interior del clima.', 'Sí',
     3.1, 'ALTURA', '>=',
     'Sin campana ni conducto a cubierta, una chocolatería necesita menos '
     'altura que una pastelería. Lo que sí necesita es sitio para la '
     'climatización y para el conducto de la deshumidificación.', None),
    ('La superficie de exposición y venta está por debajo del umbral de la '
     'Ley 12/2012', 'No',
     'Mide sólo la zona a la que entra el público. La de la hoja «Zonas y m2» '
     'es la de partida.', 'Sí', 22.0, 'UMBRAL750', '<=',
     'Por debajo de 750 m2 de superficie útil de exposición y venta al público, '
     'ninguna administración puede exigirte licencia previa de instalación, de '
     'funcionamiento o de actividad: el epígrafe 644.5 está en el Anexo de la '
     'Ley 12/2012. Decir qué trámite pide Madrid o Barcelona está PROHIBIDO en '
     'esta guía: no se ha abierto ninguna ordenanza.', 'CHN-49'),
    ('El obrador puede quedar inaccesible al público', 'Sí',
     'Dibuja las seis zonas sobre el plano antes de firmar. Si no caben con la '
     'puerta donde está, no caben.', 'Sí', None, None, None,
     'El obrador es zona de elaboración, no una cocina a la vista. Y tu sistema '
     'de autocontrol tiene que designar con NOMBRE a la persona responsable: no '
     'vale «el encargado».', 'CHN-32'),
    ('El obrador NO necesita salida de humos, porque no hay combustión', 'No',
     'Comprueba que en tu proyecto no entra ni freidora ni fogón. Si entra, '
     'este ítem deja de valer y pasas al siguiente.', 'Sí', None, None, None,
     'LA VENTAJA QUE MÁS LOCALES ABRE. Un obrador de chocolate no fríe ni asa: '
     'no genera aire de categoría AE4, así que no necesita campana ni conducto '
     'a cubierta, que es la partida que tumba la mayoría de los locales de una '
     'pastelería. Y ojo con la norma que se cita mal: el CTE DB-HS 3 se aplica '
     'a viviendas y, en edificios de otro uso, sólo a aparcamientos y garajes.',
     'CHN-46'),
    ('Si vas a montar la variante de taza y churros, el local admite freidora, '
     'campana y conducto a cubierta', 'No',
     'Sube a la cubierta con el propietario. Pídelo por escrito antes de '
     'firmar, y pide también el certificado de la última inspección de gas.',
     'Por comprobar', None, None, None,
     'La chocolatería de TAZA es otro negocio y la norma lo separa sola: el '
     'Anexo de la Ley 12/2012 NO incluye ningún grupo de la agrupación 67, así '
     'que la bombonería se libra de la licencia previa hasta 750 m2 y la de '
     'taza no. Y si hay freidora de gas, la instalación receptora se '
     'inspecciona cada cinco años.', 'CHN-49c'),
    ('Los estatutos de la comunidad de propietarios no prohíben la actividad',
     'Sí',
     'Pide los estatutos inscritos y el acta de la última junta. Que el vecino '
     'de al lado sea un bar no basta.', 'Sí', None, None, None,
     'Una prohibición estatutaria inscrita se impone aunque el ayuntamiento no '
     'te pida nada. Y aquí hay un matiz de chocolatería: la unidad exterior de '
     'la climatización va en fachada o en cubierta, las dos zona común, así '
     'que la conversación con la comunidad existe igual aunque no haya humos.',
     None),
    ('El planeamiento urbanístico admite la actividad en esa finca', 'Sí',
     'Consulta de compatibilidad urbanística en el ayuntamiento, por escrito y '
     'a nombre del local, no una llamada.', 'Sí', None, None, None,
     'Un local que hoy es un comercio no admite automáticamente un obrador: es '
     'actividad de transformación de alimentos, aunque sea silenciosa y sin '
     'humos.', None),
    ('Caben aseo de público y vestuario de personal separados', 'No',
     'Cuenta los metros y mira dónde están los bajantes. Un aseo nuevo sin '
     'bajante cerca es obra grande.', 'Sí', None, None, None,
     'El personal necesita su aseo y su taquilla; el cliente, el suyo. Los 8 '
     'm2 de la hoja de zonas ya lo contemplan.', None),
    ('Se puede descargar la cobertura sin cruzar la zona de clientes', 'No',
     'Ve a la hora a la que descargarías. Mira si hay carga y descarga y si el '
     'portal lo permite.', 'Sí', None, None, None,
     'La cobertura llega en cajas de 5 a 25 kg y el packaging de campaña llega '
     'en palés. Si entra por la puerta de la tienda, entra por delante del '
     'cliente.', None),
    ('La basura y el cartón salen sin abrir al obrador', 'No',
     'Localiza el cuarto de residuos y su puerta. Debe estar cerrado y con '
     'contenedores identificados.', 'Sí', None, None, None,
     'En bombonería el residuo de volumen es el CARTÓN del packaging, y se '
     'acumula en campaña justo en la zona de envasado.', None),
    ('Hay acometida de agua fría y caliente y desagüe donde van los equipos',
     'No',
     'Localiza el desagüe existente. Mover un desagüe obliga a levantar el '
     'suelo del local entero.', 'Sí', None, None, None,
     'El temperador de baño maría, la cámara y el fregadero necesitan desagüe '
     'en su punto. Y la climatización necesita evacuación de condensados, que '
     'es el desagüe que nadie prevé.', None),
    ('Suelos y paredes admiten acabado liso, lavable e impermeable', 'No',
     'Mira el estado real: azulejo roto, yeso, hormigón visto. El acabado del '
     'obrador es obra, no pintura.', 'Sí', None, None, None,
     'Superficies lisas, lavables e impermeables y lavamanos no manual. No es '
     'un extra: es requisito, y en chocolate además importa que el suelo no '
     'suelte polvo.', None),
    ('El escaparate y la vitrina quedan fuera del sol de mediodía', 'No',
     'Ve al local a las 14:00, no a las 10:00, y mira dónde da el sol.', 'Sí',
     None, None, None,
     'La vitrina de bombonería trabaja a 16-18 grados C. Un escaparate a '
     'poniente en julio la obliga a ciclar sin parar, sube la humedad interior '
     'y te deja el bombón mate. Se arregla con lámina solar y toldo, que son '
     'partida del libro 2, pero hay que saberlo antes.', None),
    ('El local es accesible o admite ajustes razonables', 'No',
     'Mide el escalón de entrada y el ancho de la puerta. Un escalón en '
     'fachada puede depender del ayuntamiento, no de ti.', 'Sí', None, None,
     None,
     'El calendario para titularidad privada es el 1-ene-2029 en bienes y '
     'servicios nuevos y el 1-ene-2030 en los existentes, y la obligación de '
     'garantizar la accesibilidad o hacer ajustes razonables no tiene umbral '
     'de superficie.', 'CHN-78'),
    ('El contrato y las cargas del local están claros antes de firmar', 'Sí',
     'Nota simple del Registro, contrato de arrendamiento leído entero y quién '
     'paga la obra de adecuación.', 'Por comprobar', None, None, None,
     'Quién paga la obra, cuántos años dura el contrato y qué pasa con la obra '
     'al terminar son tres números del libro 2, no tres detalles.', None),
]


# --------------------------------------------------------------------------
def nl(idd):
    """Nota legal de la verificación del 12-sep, o aborta."""
    n = D.nota_legal(idd)
    if n is None:
        raise SystemExit('nota_legal(%s) devolvió None: gate_legal debería '
                         'haberlo cazado antes.' % idd)
    return n


NOTAS_LEGALES = {'n': 0}


def nota_legal_celda(ws, coord, idd):
    from openpyxl.comments import Comment
    com = Comment(nl(idd), 'AI Chef Pro')
    com.width = 420
    com.height = 130
    ws[coord].comment = com
    NOTAS_LEGALES['n'] += 1


# --------------------------------------------------------------------------
# Hoja «Instrucciones»
# --------------------------------------------------------------------------
PASOS = [
    '1. Hoja «Parámetros»: lo primero. Horas de turno, turnos al día, piezas '
    'que quieres vender, superficie, potencia, temperatura exterior de tu '
    'ciudad en agosto y la potencia frigorífica que te ofrezcan. Todo lo demás '
    'del libro se recalcula desde aquí; no hay ni un número escondido dentro '
    'de una fórmula.',
    '2. Hoja «Zonas y m2»: reparte los metros entre las seis zonas y numera el '
    'recorrido de la marcha adelante, del 1 al 6. La hoja te dice si el '
    'reparto cuadra con la superficie declarada, qué parte del local es '
    'producción y si el recorrido tiene un cruce.',
    '3. Hoja «Clima del Obrador»: las cinco temperaturas objetivo, el semáforo '
    'de coherencia entre lo que quieres, el agosto de tu ciudad y lo que te '
    'ofrece el instalador, y la ficha de preguntas que hay que hacerle. Esta '
    'hoja NO calcula la carga térmica de tu obrador, y no lo hace a propósito: '
    'lo explica dentro.',
    '4. Hoja «Capacidad por Equipo»: una fila por máquina y por puesto de '
    'trabajo. Di si lo tienes, cuánto cabe en un ciclo, cuántos bombones salen '
    'de esa cantidad, cuántos minutos dura el ciclo y qué parte de tu surtido '
    'pasa por ahí. La hoja devuelve los bombones al día que ESO permite al '
    'obrador entero.',
    '5. Hoja «Cuello de Botella»: el resultado. Cuál es el equipo que manda, '
    'cuántos bombones al día aguanta el conjunto, cuánta holgura te queda y '
    'qué pasa en cada una de las doce campañas del año. Aquí se ve si Navidad '
    'y San Valentín te caben en el obrador que estás comprando.',
    '6. Hoja «Ficha de Visita a Local»: imprímela y llévala a cada visita. '
    'Dieciocho comprobaciones, seis de ellas eliminatorias. Un solo «No» en un '
    'ítem eliminatorio y el veredicto es DESCARTAR: no es pesimismo, es que '
    'ese defecto no se arregla con dinero razonable.',
]

NOTAS_LIBRO = [
    'ESTE LIBRO DECIDE UNA COMPRA, NO UNA SEMANA DE TRABAJO. Las curvas de '
    'templado, las fichas de moldeado y el plan del día a día están en '
    'kit-tareas-chocolateria/02-partidas-produccion.xlsx. Aquí sólo se '
    'contesta cuántos bombones al día permite el equipo que estás a punto de '
    'pagar, que es la pregunta que ya no se puede contestar después.',
    'UNA CAJA DE 35 BOMBONES NO ES UNA PIEZA. Es el error de bulto de '
    'cualquier cuenta de capacidad de una bombonería: se cuentan las piezas '
    'que salen por el mostrador -cajas incluidas- y sale un obrador cinco '
    'veces más pequeño del que hace falta. Por eso toda la capacidad de este '
    'libro se mide en BOMBONES EQUIVALENTES, y la equivalencia está en '
    '«Parámetros», a la vista y editable.',
    'EL CUELLO DE BOTELLA DE UNA BOMBONERÍA CASI NUNCA ES LA ATEMPERADORA. Es '
    'la máquina que más cuesta y la que más se mira, y produce chocolate '
    'templado muy por encima de lo que dos personas moldean. Lo que limita son '
    'los moldes que tienes, los ciclos de cristalización que caben en la '
    'jornada y el puesto de envasado. Mira la columna «Cuenta para el cuello» '
    'antes de decidir en qué gastas.',
    'EL CLIMA NO ES CONFORT: ES LA PARTIDA QUE DECIDE SI LA COBERTURA '
    'CRISTALIZA. 18-20 grados C y 50-60 % de humedad en el obrador, y una '
    'cámara a 15-18 grados C que no es una nevera. Este libro no calcula tu '
    'carga térmica -no hay un solo coeficiente publicado y verificable para '
    'hacerlo- pero sí comprueba que lo que quieres, el agosto de tu ciudad y '
    'lo que te ofrecen son coherentes entre sí, y te da la lista de preguntas '
    'que hay que hacerle al instalador.',
    'NO HAY UNA TEMPERATURA LEGAL DEL CHOCOLATE. El RD 1021/2022 no nombra el '
    'chocolate ni una sola vez, y su artículo 4.2 va por la temperatura que '
    'ponga en su etiqueta quien ha producido y envasado. Para el bombón que '
    'despachas a granel no hay etiqueta: la referencia es TU sistema de '
    'autocontrol, y la temperatura la declaras tú. Las cinco de este libro son '
    'las que ya publica el Kit de Tareas Chocolatería.',
    'NO HAY SALIDA DE HUMOS, Y ESO ABRE LOCALES. Un obrador de chocolate no '
    'fríe ni asa: no genera aire de categoría AE4 y no necesita campana ni '
    'conducto a cubierta. Es la partida que tumba la mitad de los locales de '
    'una pastelería y aquí no existe. Cuidado sólo con la variante de taza y '
    'churros, que sí lleva freidora y sí lo necesita.',
    'LOS PRECIOS Y LOS PLAZOS NO ESTÁN AQUÍ. Cuánto cuesta cada máquina es el '
    'libro 2 (CAPEX) y cuántas semanas tarda en llegar es el libro 9 '
    '(equipamiento y proveedores). Este libro sólo mira lo que producen.',
]

CADENCIA = ('Cadencia: la hoja «Ficha de Visita a Local», UNA VEZ POR LOCAL que '
            'visites, y se guarda aunque lo descartes -comparar tres fichas es '
            'lo que enseña qué estás aceptando sin darte cuenta-. La hoja '
            '«Clima del Obrador», una vez por cada oferta de instalador que '
            'recibas. Las hojas de capacidad, cada vez que cambies un equipo '
            'del presupuesto y, después de abrir, UNA VEZ AL AÑO en septiembre, '
            'antes de arrancar la campaña de Navidad.')


def hoja_instrucciones(wb):
    ws = wb.create_sheet('Instrucciones', 0)
    C.anchos(ws, {'A': 46, 'B': 46, 'C': 46})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=C.ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', C.SUBTITULO)
    motor.val(ws, 'A3', 'Para qué sirve: decidir si ESE local sirve, si se '
                        'puede climatizar y cuántos bombones al día aguanta el '
                        'equipo que estás comprando.')
    ws['A3'].font = Font(italic=True, size=9)

    C.seccion(ws, 'A5', 'Instrucciones de uso')
    fila = 6
    for paso in PASOS:
        ws.merge_cells('A%d:C%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, paso, wrap=True)
        ws.row_dimensions[fila].height = 68
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, C.NOTA_VERDES)
    ws['A%d' % fila].fill = PatternFill('solid', fgColor=motor.VERDE)
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Lo que conviene saber antes de empezar')
    fila += 1
    for texto in NOTAS_LIBRO:
        ws.merge_cells('A%d:C%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, texto, wrap=True)
        ws.row_dimensions[fila].height = 74
        fila += 1
    fila += 1

    C.seccion(ws, 'A%d' % fila, 'Dónde acaba este libro y dónde sigue el Kit '
                                'de Tareas Chocolatería')
    fila += 1
    C.cabecera(ws, fila, [('A', 'Lo que necesitas'),
                          ('B', 'Dónde está'),
                          ('C', 'Por qué no está aquí')], altura=26)
    fila += 1
    FRONTERAS = [
        ('Las curvas de templado de cada cobertura y las fichas de moldeado',
         'kit-tareas-chocolateria/02-partidas-produccion.xlsx',
         'El kit las publica y esta guía NO las repite. Aquí sólo hay '
         'capacidad y clima, no técnica de templado.'),
        ('Las fechas de cada campaña y qué se hace en cada una',
         'kit-tareas-chocolateria/BONUS-02-calendario-anual-tareas.xlsx',
         'El kit pone las fechas y el qué. Aquí la campaña entra sólo como '
         'multiplicador de bombones al día; los euros de cada una son el '
         'libro 6 de esta guía.'),
        ('Cuánta gente hace falta y cuánto cuesta con la Seguridad Social',
         'Libro 7 de esta guía, hoja «Personal»',
         'Un obrador de chocolate no tiene jornada de madrugada, así que esta '
         'guía no lleva libro de turnos: el personal se resuelve en el plan '
         'financiero. Aquí las horas de turno son un parámetro de capacidad.'),
        ('Cuánto cuesta cada máquina y cuánto tarda en llegar',
         'Libros 2 (CAPEX) y 9 (equipamiento y proveedores)',
         'El precio y el plazo no cambian la capacidad. Se separan a propósito '
         'para poder decidir primero qué necesitas y después qué te cuesta.'),
        ('Qué temperatura y qué vida útil declaras en tu etiqueta',
         'Libro 5 de esta guía: vida útil y rotación',
         'Aquí está el clima del LOCAL. Lo que declaras por referencia -y si '
         'va envasada con etiqueta o a granel- es otra decisión y otro libro.'),
    ]
    for que, donde, porque in FRONTERAS:
        motor.val(ws, 'A%d' % fila, que, wrap=True)
        motor.val(ws, 'B%d' % fila, donde, wrap=True)
        motor.val(ws, 'C%d' % fila, porque, wrap=True)
        ws.row_dimensions[fila].height = 58
        fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila,
              'Es COPIA declarada, no vínculo: en toda la guía no hay ni una '
              'fórmula que apunte a otro fichero. Un enlace entre libros se '
              'rompe en cuanto alguien mueve una carpeta, y entonces el libro '
              'miente sin avisar. Donde una celda verde traería un dato del '
              'Kit de Tareas Chocolatería o de otro libro, viene con un valor '
              'por defecto propio, declarado como supuesto, y su nota te dice '
              'qué lo sustituye.', wrap=True)
    ws['A%d' % fila].font = Font(italic=True, size=9)
    ws.row_dimensions[fila].height = 62
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Cada cuánto se usa este libro')
    fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila, CADENCIA, wrap=True)
    ws.row_dimensions[fila].height = 62
    fila += 2

    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila, C.NOTA_DESPROTEGER, wrap=True)
    fila += 2
    C.pie(ws, fila)
    C.pagina(ws, apaisado=False)
    return ws


# --------------------------------------------------------------------------
# Hoja «Parámetros»
# --------------------------------------------------------------------------
P_FILA = {}


def hoja_parametros(wb):
    ws = wb.create_sheet(H_PAR)
    C.anchos(ws, {'A': 50, 'B': 14, 'C': 20, 'D': 22, 'E': 86})
    C.encabezar(ws, 'Parámetros', 'Todo lo que el libro calcula sale de aquí. '
                                  'Ni un número vive dentro de una fórmula.',
                col_fin='E')
    C.cabecera(ws, 5, [('A', 'Parámetro'), ('B', 'Valor'), ('C', 'Unidad'),
                       ('D', 'Procedencia'), ('E', 'Qué es y de dónde sale')])
    for i, (etq, valor, unidad, fuente, notatxt) in enumerate(PARAMS_LIBRO):
        fila = fila_par(i)
        P_FILA[etq] = fila
        motor.val(ws, 'A%d' % fila, etq, wrap=True)
        if valor is None:
            pass                                   # se rellena más abajo
        elif unidad == '%':
            motor.val(ws, 'B%d' % fila, valor, fmt=C.FMT_PCT, verde_=True)
        elif isinstance(valor, str):
            motor.val(ws, 'B%d' % fila, valor, verde_=True)
        elif isinstance(valor, int):
            motor.val(ws, 'B%d' % fila, valor, fmt=C.FMT_ENT, verde_=True)
        else:
            motor.val(ws, 'B%d' % fila, float(valor), fmt=C.FMT_DEC1,
                      verde_=True)
        motor.val(ws, 'C%d' % fila, unidad)
        motor.val(ws, 'D%d' % fila, fuente)
        motor.val(ws, 'E%d' % fila, notatxt, wrap=True)
        ws.row_dimensions[fila].height = 46

    motor.f(ws, 'B%d' % fila_par(P_MIN_DIA),
            motor.iferror('B%d*B%d*B%d*60'
                          % (fila_par(P_HORAS), fila_par(P_TURNOS),
                             fila_par(P_PROD))), fmt=C.FMT_ENT)
    motor.f(ws, 'B%d' % fila_par(P_OBJ),
            motor.iferror('B%d*B%d' % (fila_par(P_PIEZAS), fila_par(P_EQUIV))),
            fmt=C.FMT_ENT)
    nota_legal_celda(ws, 'A%d' % fila_par(P_750), 'CHN-49b')

    fila = fila_par(len(PARAMS_LIBRO)) + 1
    C.parrafo(ws, fila,
              'Los valores marcados «supuesto» son los de la bombonería de '
              'ejemplo «La Almendra» (75 m2, 45 de producción y 22 de tienda, '
              'un turno, tres personas y 2,5 jornadas). NO son datos de '
              'sector: son un punto de partida coherente para que puedas ver '
              'el libro funcionando antes de meter los tuyos.',
              col_ini='A', col_fin='E', alto=48)
    fila += 2
    C.parrafo(ws, fila,
              'La temperatura exterior de agosto, la potencia frigorífica '
              'ofertada y el salto de diseño del instalador son las TRES '
              'celdas con las que trabaja el semáforo de coherencia de la hoja '
              '«Clima del Obrador». Este libro NO calcula la carga térmica de '
              'tu obrador: no existe un coeficiente publicado y verificable '
              'para hacerlo, y publicar uno inventado sería peor que no '
              'publicar nada. Lo que hace es comprobar que las tres cifras '
              'encajan entre sí y darte las preguntas que le tienes que hacer '
              'a quien sí puede calcularla.',
              col_ini='A', col_fin='E', alto=62)
    C.pagina(ws, apaisado=True, titulos='5:5')
    return ws


# --------------------------------------------------------------------------
# Hoja «Zonas y m2»
# --------------------------------------------------------------------------
#: Paso del recorrido de marcha adelante, por nombre de zona (supuesto, verde).
ORDEN_MARCHA = {
    'Almacen de cobertura y materias primas': 1,
    'Obrador de templado y moldeado': 2,
    'Camara de chocolate': 3,
    'Envasado y packaging': 4,
    'Tienda y mostrador': 5,
    'Aseos y vestuario': 6,
}
Z_FILA = {}
Z_REF = {}
Z_INI = 6


def hoja_zonas(wb):
    ws = wb.create_sheet(H_ZON)
    C.anchos(ws, {'A': 5, 'B': 38, 'C': 16, 'D': 11, 'E': 12, 'F': 13,
                  'G': 92})
    C.encabezar(ws, 'Zonas y metros cuadrados',
                'Las seis zonas de una bombonería con obrador y el recorrido '
                'de marcha adelante. No es el reparto de una pastelería: aquí '
                'no hay zona de horno ni de fermentación, y sí cámara '
                'climatizada.', col_fin='G')
    C.cabecera(ws, 5, [('A', 'Nº'), ('B', 'Zona'), ('C', 'Bloque'),
                       ('D', 'm2'), ('E', '% del local'),
                       ('F', 'Paso del recorrido'),
                       ('G', 'Qué tiene que cumplir')])
    fila = Z_INI
    for i, (zona, m2, _fuente, notatxt) in enumerate(D.ZONAS):
        Z_FILA[zona] = fila
        motor.val(ws, 'A%d' % fila, i + 1, fmt=C.FMT_ENT)
        motor.val(ws, 'B%d' % fila, zona, wrap=True)
        motor.val(ws, 'C%d' % fila, D.ZONA_A_BLOQUE[zona])
        motor.val(ws, 'D%d' % fila, m2, fmt=C.FMT_DEC1, verde_=True)
        motor.val(ws, 'F%d' % fila, ORDEN_MARCHA[zona], fmt=C.FMT_ENT,
                  verde_=True)
        motor.val(ws, 'G%d' % fila, notatxt, wrap=True)
        ws.row_dimensions[fila].height = 52
        fila += 1
    z_fin = fila - 1
    f_tot = z_fin + 2
    Z_REF['z_fin'] = z_fin
    Z_REF['total'] = f_tot
    for r in range(Z_INI, z_fin + 1):
        motor.f(ws, 'E%d' % r, motor.iferror('D%d/$D$%d' % (r, f_tot)),
                fmt=C.FMT_PCT)
    nota_legal_celda(ws, 'G%d' % Z_FILA['Obrador de templado y moldeado'],
                     'CHN-32')
    nota_legal_celda(ws, 'G%d' % Z_FILA['Camara de chocolate'], 'CHN-30')

    motor.val(ws, 'B%d' % f_tot, 'TOTAL repartido', bold=True)
    motor.f(ws, 'D%d' % f_tot, '=SUM(D%d:D%d)' % (Z_INI, z_fin),
            fmt=C.FMT_DEC1, bold=True)
    motor.f(ws, 'E%d' % f_tot, '=SUM(E%d:E%d)' % (Z_INI, z_fin), fmt=C.FMT_PCT,
            bold=True)
    C.destacado(ws, 'D%d' % f_tot)

    f_dec = f_tot + 1
    motor.val(ws, 'B%d' % f_dec, 'Superficie declarada en «Parámetros»')
    motor.f(ws, 'D%d' % f_dec, "='%s'!B%d" % (H_PAR, fila_par(P_M2)),
            fmt=C.FMT_DEC1)
    f_desc = f_tot + 2
    motor.val(ws, 'B%d' % f_desc, 'Descuadre (m2)')
    motor.f(ws, 'D%d' % f_desc, motor.iferror('D%d-D%d' % (f_tot, f_dec)),
            fmt=C.FMT_DEC1)
    motor.val(ws, 'G%d' % f_desc,
              'Si no es cero, o te sobran metros sin asignar o has repartido '
              'más de los que tiene el local.', wrap=True)
    motor.regla_expresion(ws, 'D%d' % f_desc,
                          '=AND(ISNUMBER($D$%d),ABS($D$%d)>0.05)'
                          % (f_desc, f_desc))

    Z_REF['descuadre'] = f_desc
    f_prod, f_pprod = f_tot + 4, f_tot + 5
    Z_REF['produccion_m2'] = f_prod
    Z_REF['produccion_pct'] = f_pprod
    motor.val(ws, 'B%d' % f_prod, 'Metros de zona de producción')
    motor.f(ws, 'D%d' % f_prod,
            '=SUMIF(C%d:C%d,"Produccion",D%d:D%d)'
            % (Z_INI, z_fin, Z_INI, z_fin), fmt=C.FMT_DEC1)
    motor.val(ws, 'B%d' % f_pprod, 'Parte del local dedicada a producción')
    motor.f(ws, 'D%d' % f_pprod, motor.iferror('D%d/D%d' % (f_prod, f_tot)),
            fmt=C.FMT_PCT)
    f_ven, f_pven = f_tot + 6, f_tot + 7
    Z_REF['venta_m2'] = f_ven
    Z_REF['venta_pct'] = f_pven
    motor.val(ws, 'B%d' % f_ven, 'Metros de tienda y mostrador')
    motor.f(ws, 'D%d' % f_ven,
            '=SUMIF(C%d:C%d,"Tienda",D%d:D%d)' % (Z_INI, z_fin, Z_INI, z_fin),
            fmt=C.FMT_DEC1)
    motor.val(ws, 'B%d' % f_pven, 'Parte del local dedicada a venta')
    motor.f(ws, 'D%d' % f_pven, motor.iferror('D%d/D%d' % (f_ven, f_tot)),
            fmt=C.FMT_PCT)
    motor.val(ws, 'G%d' % f_ven,
              'Es la superficie que se compara con los 750 m2 de la Ley '
              '12/2012 en la ficha de visita: la de EXPOSICIÓN Y VENTA al '
              'público, no la del local entero.', wrap=True)
    ws.row_dimensions[f_ven].height = 44

    f_min = f_tot + 8
    motor.val(ws, 'B%d' % f_min, 'Mínimo de producción que te has exigido')
    motor.f(ws, 'D%d' % f_min, "='%s'!B%d" % (H_PAR, fila_par(P_MIN_PROD)),
            fmt=C.FMT_PCT)
    f_ver_rep = f_tot + 9
    Z_REF['veredicto_reparto'] = f_ver_rep
    motor.val(ws, 'B%d' % f_ver_rep, 'Veredicto del reparto', bold=True)
    motor.f(ws, 'D%d' % f_ver_rep,
            '=IF(D%d="","",IF(D%d<D%d,"La producción se queda corta",'
            '"Reparto suficiente"))' % (f_pprod, f_pprod, f_min), bold=True)
    C.destacado(ws, 'D%d' % f_ver_rep)
    motor.semaforo_texto(ws, 'D%d' % f_ver_rep,
                         (('La producción se queda corta', motor.CF_ROJO_BG,
                           motor.CF_ROJO_FG),
                          ('Reparto suficiente', motor.CF_VERDE_BG,
                           motor.CF_VERDE_FG)))

    f_mar = f_tot + 11
    C.seccion(ws, 'B%d' % f_mar,
              'Marcha adelante: la cobertura entra por un extremo y el bombón '
              'sale por el otro')
    f_sum, f_deb, f_num = f_mar + 1, f_mar + 2, f_mar + 3
    motor.val(ws, 'B%d' % f_sum, 'Suma de los pasos que has numerado')
    motor.f(ws, 'D%d' % f_sum, '=SUM(F%d:F%d)' % (Z_INI, z_fin), fmt=C.FMT_ENT)
    motor.val(ws, 'B%d' % f_deb, 'Suma que debería dar (1 + 2 + ... + n)')
    motor.f(ws, 'D%d' % f_deb,
            motor.iferror("'%s'!B%d*('%s'!B%d+1)/2"
                          % (H_PAR, fila_par(P_ZONAS), H_PAR,
                             fila_par(P_ZONAS))), fmt=C.FMT_ENT)
    motor.val(ws, 'B%d' % f_num, '¿Están numerados del 1 al n sin repetir?')
    motor.f(ws, 'D%d' % f_num,
            '=IF(AND(D%d=D%d,MIN(F%d:F%d)=1,MAX(F%d:F%d)=\'%s\'!B%d),"Sí",'
            '"Revisa la numeración")'
            % (f_sum, f_deb, Z_INI, z_fin, Z_INI, z_fin, H_PAR,
               fila_par(P_ZONAS)))
    motor.val(ws, 'G%d' % f_num,
              'Comprobación de numeración: la suma tiene que cuadrar y los '
              'pasos ir del 1 al número de zonas. No detecta una permutación '
              'que sume igual; lo que detecta -y es lo que pasa siempre- es un '
              'número repetido o uno saltado.', wrap=True)
    ws.row_dimensions[f_num].height = 44

    c_ini = f_num + 1
    comprobaciones = [
        ('La cobertura entra antes que el obrador',
         'F%d<F%d' % (Z_FILA['Almacen de cobertura y materias primas'],
                      Z_FILA['Obrador de templado y moldeado'])),
        ('El bombón acabado pasa del obrador a la cámara',
         'F%d>F%d' % (Z_FILA['Camara de chocolate'],
                      Z_FILA['Obrador de templado y moldeado'])),
        ('El envasado va después de la cámara',
         'F%d>F%d' % (Z_FILA['Envasado y packaging'],
                      Z_FILA['Camara de chocolate'])),
        ('Lo envasado llega a la tienda sin volver atrás',
         'F%d<=F%d' % (Z_FILA['Envasado y packaging'],
                       Z_FILA['Tienda y mostrador'])),
        ('El vestuario no está en mitad del recorrido de producción',
         'F%d>F%d' % (Z_FILA['Aseos y vestuario'],
                      Z_FILA['Envasado y packaging'])),
    ]
    for k, (etq, cond) in enumerate(comprobaciones):
        fila_c = c_ini + k
        motor.val(ws, 'B%d' % fila_c, etq, wrap=True)
        motor.f(ws, 'D%d' % fila_c, '=IF(%s,"Sí","No")' % cond)
        motor.semaforo_texto(ws, 'D%d' % fila_c,
                             (('No', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                              ('Sí', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    c_fin = c_ini + len(comprobaciones) - 1
    f_ver_marcha = c_fin + 2
    Z_REF['veredicto_marcha'] = f_ver_marcha
    motor.val(ws, 'B%d' % f_ver_marcha, 'VEREDICTO DE MARCHA ADELANTE',
              bold=True)
    motor.f(ws, 'D%d' % f_ver_marcha,
            '=IF(COUNTIF(D%d:D%d,"No")>0,"Hay un cruce en el recorrido",'
            '"Marcha adelante correcta")' % (c_ini, c_fin), bold=True)
    C.destacado(ws, 'D%d' % f_ver_marcha)
    motor.semaforo_texto(ws, 'D%d' % f_ver_marcha,
                         (('Hay un cruce en el recorrido', motor.CF_ROJO_BG,
                           motor.CF_ROJO_FG),
                          ('Marcha adelante correcta', motor.CF_VERDE_BG,
                           motor.CF_VERDE_FG)))
    C.parrafo(ws, f_ver_marcha + 2,
              'La marcha adelante no es una preferencia de diseño: es que la '
              'materia prima y el producto terminado no se crucen nunca. En '
              'chocolate tiene además un motivo propio: el cacao absorbe los '
              'olores, así que el almacén de cobertura no puede compartir aire '
              'con la basura ni con el cuarto de limpieza. Cuando el local no '
              'permite el recorrido, no se arregla con un cartel ni con un '
              'horario; se arregla con obra o no se arregla. Por eso se dibuja '
              'sobre el plano ANTES de firmar.',
              col_ini='B', col_fin='G', alto=62)
    C.pagina(ws, apaisado=True, titulos='5:5')
    return ws


# --------------------------------------------------------------------------
# Hoja «Clima del Obrador»  (D33)
# --------------------------------------------------------------------------
CLI = {}


def hoja_clima(wb):
    ws = wb.create_sheet(H_CLI)
    C.anchos(ws, {'A': 44, 'B': 13, 'C': 13, 'D': 13, 'E': 13, 'F': 34,
                  'G': 60, 'H': 72})
    C.encabezar(ws, 'Clima del obrador',
                'Las cinco temperaturas objetivo son las que ya publica el Kit '
                'de Tareas Chocolatería. Esta hoja NO calcula la carga térmica '
                'de tu obrador: comprueba que lo que quieres, el agosto de tu '
                'ciudad y lo que te ofrece el instalador son coherentes, y te '
                'da las preguntas que hay que hacerle.', col_fin='H')

    C.seccion(ws, 'A5', 'Las cinco ventanas de temperatura y humedad')
    C.cabecera(ws, 6, [('A', 'Dónde'), ('B', 'T mínima'), ('C', 'T máxima'),
                       ('D', 'HR mínima'), ('E', 'HR máxima'),
                       ('F', 'De dónde sale'), ('G', 'Literal del kit'),
                       ('H', 'Qué pasa si te sales')], altura=40)
    fila = L_CLI_INI
    for clave in CLAVES_CLIMA:
        d = D.CLIMA[clave]
        CLI[clave] = fila
        motor.val(ws, 'A%d' % fila, d['concepto'], wrap=True)
        motor.val(ws, 'B%d' % fila, d['t_min'], fmt=C.FMT_DEC1, verde_=True)
        motor.val(ws, 'C%d' % fila, d['t_max'], fmt=C.FMT_DEC1, verde_=True)
        if d['hr_min'] is None:
            motor.val(ws, 'D%d' % fila, '')
        else:
            motor.val(ws, 'D%d' % fila, d['hr_min'], fmt=C.FMT_DEC1,
                      verde_=True)
        if d['hr_max'] is None:
            motor.val(ws, 'E%d' % fila, '')
        else:
            motor.val(ws, 'E%d' % fila, d['hr_max'], fmt=C.FMT_DEC1,
                      verde_=True)
        motor.val(ws, 'F%d' % fila, d['fuente'], wrap=True)
        motor.val(ws, 'G%d' % fila, d['literal'], wrap=True)
        motor.val(ws, 'H%d' % fila, d['nota'], wrap=True)
        ws.row_dimensions[fila].height = 58
        fila += 1
    cli_fin = fila - 1
    nota_legal_celda(ws, 'A%d' % L_CLI_INI, 'CHN-30')
    nota_legal_celda(ws, 'A%d' % CLI['vitrina'], 'CHN-87')

    f = cli_fin + 2
    ws.merge_cells('A%d:H%d' % (f, f))
    motor.val(ws, 'A%d' % f,
              'NO HAY UNA TEMPERATURA LEGAL DEL CHOCOLATE. El RD 1021/2022 no '
              'nombra el chocolate ni una sola vez, y su art. 4.2 se aplica a '
              'la temperatura que ponga en su etiqueta quien ha producido y '
              'envasado el producto. Para el bombón que despachas a granel no '
              'hay etiqueta: la referencia es TU sistema de autocontrol, y la '
              'temperatura la declaras tú en él. Las cinco de esta tabla son '
              'las que ya publica el Kit de Tareas Chocolatería, y por eso las '
              'usa la guía: un concepto, una fuente.', wrap=True)
    ws['A%d' % f].font = Font(italic=True, size=9)
    ws.row_dimensions[f].height = 62

    # --- coherencia entre ventanas ---------------------------------------
    co_tit = f + 2
    C.seccion(ws, 'A%d' % co_tit,
              'Primera comprobación: ¿son coherentes entre sí las cinco '
              'ventanas?')
    co_ini = co_tit + 1
    campo = {'min': 'B', 'max': 'C'}
    for k, (etq, ca, fa, op, cb, fb, notatxt) in enumerate(COHERENCIAS):
        r = co_ini + k
        motor.val(ws, 'A%d' % r, etq, wrap=True)
        motor.f(ws, 'F%d' % r,
                '=IF(OR(%s%d="",%s%d=""),"",IF(%s%d%s%s%d,"Sí","No"))'
                % (campo[fa], CLI[ca], campo[fb], CLI[cb],
                   campo[fa], CLI[ca], op, campo[fb], CLI[cb]))
        motor.val(ws, 'H%d' % r, notatxt, wrap=True)
        motor.semaforo_texto(ws, 'F%d' % r,
                             (('No', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                              ('Sí', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
        ws.row_dimensions[r].height = 46
    co_fin = co_ini + len(COHERENCIAS) - 1
    f_ven_fallos = co_fin + 1
    CLI['ven_fallos'] = f_ven_fallos
    motor.val(ws, 'A%d' % f_ven_fallos, 'Ventanas incoherentes entre sí')
    motor.f(ws, 'F%d' % f_ven_fallos,
            '=COUNTIF(F%d:F%d,"No")' % (co_ini, co_fin), fmt=C.FMT_ENT)

    # --- coherencia con la oferta del instalador --------------------------
    of_tit = f_ven_fallos + 2
    C.seccion(ws, 'A%d' % of_tit,
              'Segunda comprobación: ¿encaja lo que te ofrece el instalador?')
    o = of_tit + 1
    CLI['t_obj_max'] = o
    motor.val(ws, 'A%d' % o, 'Temperatura objetivo máxima del obrador')
    motor.f(ws, 'F%d' % o, '=C%d' % CLI['obrador'], fmt=C.FMT_DEC1)
    motor.val(ws, 'H%d' % o,
              'La de la primera fila de la tabla de arriba. Si la subes, el '
              'salto baja y la oferta encaja mejor: también te quedas sin '
              'margen para templar.', wrap=True)
    ws.row_dimensions[o].height = 44

    CLI['t_ext'] = o + 1
    motor.val(ws, 'A%d' % CLI['t_ext'],
              'Temperatura exterior de tu ciudad en agosto')
    motor.f(ws, 'F%d' % CLI['t_ext'],
            "='%s'!B%d" % (H_PAR, fila_par(P_TEXT)), fmt=C.FMT_DEC1)

    CLI['dt_real'] = o + 2
    motor.val(ws, 'A%d' % CLI['dt_real'],
              'Salto de temperatura que tiene que vencer el equipo', bold=True)
    motor.f(ws, 'F%d' % CLI['dt_real'],
            motor.iferror('F%d-F%d' % (CLI['t_ext'], o)), fmt=C.FMT_DEC1,
            bold=True)
    C.destacado(ws, 'F%d' % CLI['dt_real'])
    motor.val(ws, 'H%d' % CLI['dt_real'],
              'Aritmética pura, sin ningún coeficiente: la de fuera menos la '
              'que quieres dentro. Es el número que hay que llevar a la '
              'conversación con el instalador.', wrap=True)
    ws.row_dimensions[CLI['dt_real']].height = 44

    CLI['dt_inst'] = o + 3
    motor.val(ws, 'A%d' % CLI['dt_inst'],
              'Salto de diseño que declara el instalador')
    motor.f(ws, 'F%d' % CLI['dt_inst'],
            "='%s'!B%d" % (H_PAR, fila_par(P_DT_INST)), fmt=C.FMT_DEC1)

    CLI['pot'] = o + 4
    motor.val(ws, 'A%d' % CLI['pot'],
              'Potencia frigorífica que te OFRECE el instalador')
    motor.f(ws, 'F%d' % CLI['pot'],
            "='%s'!B%d" % (H_PAR, fila_par(P_POTFRIG)), fmt=C.FMT_DEC1)

    CLI['m2'] = o + 5
    motor.val(ws, 'A%d' % CLI['m2'], 'Metros de producción a climatizar')
    motor.f(ws, 'F%d' % CLI['m2'],
            "='%s'!D%d" % (H_ZON, Z_REF['produccion_m2']), fmt=C.FMT_DEC1)

    CLI['ratio'] = o + 6
    motor.val(ws, 'A%d' % CLI['ratio'],
              'Potencia ofertada por metro climatizado')
    motor.f(ws, 'F%d' % CLI['ratio'],
            motor.iferror('F%d/F%d' % (CLI['pot'], CLI['m2'])),
            fmt=C.FMT_DEC1)
    motor.val(ws, 'H%d' % CLI['ratio'],
              'NO ES UN CRITERIO DE DIMENSIONADO Y POR ESO NO LLEVA SEMÁFORO: '
              'es tu propia oferta dividida entre tus propios metros. Sirve '
              'para una sola cosa, y es útil: enseñársela al segundo '
              'instalador y preguntarle por qué la suya se parece o no se '
              'parece. Cualquier tabla que te diga «tantos kW por m2 de '
              'obrador de chocolate» está inventada.', wrap=True)
    ws.row_dimensions[CLI['ratio']].height = 62

    CLI['esc_pot'] = o + 7
    motor.val(ws, 'A%d' % CLI['esc_pot'],
              '¿Te ha dado la potencia por escrito?')
    motor.val(ws, 'F%d' % CLI['esc_pot'], 'Por pedir', verde_=True)
    CLI['esc_dt'] = o + 8
    motor.val(ws, 'A%d' % CLI['esc_dt'],
              '¿Te ha dicho por escrito para qué salto la ha calculado?')
    motor.val(ws, 'F%d' % CLI['esc_dt'], 'Por pedir', verde_=True)

    CLI['ver'] = o + 10
    motor.val(ws, 'A%d' % CLI['ver'], 'SEMÁFORO DE COHERENCIA', bold=True)
    motor.f(ws, 'F%d' % CLI['ver'],
            '=IF(OR(F%d="",F%d="",F%d=""),"",'
            'IF(F%d<F%d,"INCOHERENTE: el salto de diseño se queda corto",'
            'IF(F%d>0,"REVISA LA VENTANA CLIMÁTICA",'
            'IF(OR(F%d<>"Sí",F%d<>"Sí"),"PIDE LA OFERTA POR ESCRITO",'
            '"COHERENTE"))))'
            % (CLI['dt_real'], CLI['dt_inst'], CLI['pot'],
               CLI['dt_inst'], CLI['dt_real'],
               f_ven_fallos,
               CLI['esc_pot'], CLI['esc_dt']), bold=True)
    C.destacado(ws, 'F%d' % CLI['ver'])
    motor.semaforo_texto(ws, 'F%d' % CLI['ver'],
                         (('INCOHERENTE: el salto de diseño se queda corto',
                           motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('REVISA LA VENTANA CLIMÁTICA', motor.CF_ROJO_BG,
                           motor.CF_ROJO_FG),
                          ('PIDE LA OFERTA POR ESCRITO', motor.CF_AMBAR_BG,
                           motor.CF_AMBAR_FG),
                          ('COHERENTE', motor.CF_VERDE_BG,
                           motor.CF_VERDE_FG)))
    motor.val(ws, 'H%d' % CLI['ver'],
              'El semáforo compara TRES cifras que teclea el lector: lo que '
              'quiere dentro, lo que hace fuera en agosto y para qué salto ha '
              'dimensionado el instalador. No dice si la potencia es '
              'suficiente -eso no se puede decir sin calcular la carga '
              'térmica, y este libro no la calcula-: dice si la oferta está '
              'contestando a tu pregunta o a otra.', wrap=True)
    ws.row_dimensions[CLI['ver']].height = 62

    # --- ficha de preguntas al instalador --------------------------------
    pi_tit = CLI['ver'] + 2
    C.seccion(ws, 'A%d' % pi_tit,
              'Ficha de preguntas al instalador: llévala a la visita técnica')
    C.cabecera(ws, pi_tit + 1, [('A', 'Qué le preguntas'), ('B', 'Unidad'),
                                ('C', 'Respuesta'), ('D', '¿Por escrito?'),
                                ('H', 'Por qué importa')], altura=30)
    fila = pi_tit + 2
    CLI['preg_ini'] = fila
    coords_num, coords_sino, coords_esc = [], [], []
    for preg, unidad, tipo, defecto, porque in PREGUNTAS_INSTALADOR:
        motor.val(ws, 'A%d' % fila, preg, wrap=True)
        motor.val(ws, 'B%d' % fila, unidad)
        if tipo == 'num':
            motor.val(ws, 'C%d' % fila, float(defecto), fmt=C.FMT_DEC1,
                      verde_=True)
            coords_num.append('C%d' % fila)
        else:
            motor.val(ws, 'C%d' % fila, defecto, verde_=True)
            coords_sino.append('C%d' % fila)
        motor.val(ws, 'D%d' % fila, 'Por pedir', verde_=True)
        coords_esc.append('D%d' % fila)
        motor.val(ws, 'H%d' % fila, porque, wrap=True)
        ws.row_dimensions[fila].height = 52
        fila += 1
    preg_fin = fila - 1
    CLI['preg_fin'] = preg_fin
    motor.semaforo_texto(ws, 'D%d:D%d' % (CLI['preg_ini'], preg_fin),
                         (('No', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('Por pedir', motor.CF_GRIS_BG, motor.CF_GRIS_FG),
                          ('Sí', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))

    f = preg_fin + 2
    CLI['preg_total'] = f
    motor.val(ws, 'A%d' % f, 'Preguntas de la ficha')
    motor.f(ws, 'F%d' % f,
            '=COUNTIF(D%d:D%d,"Sí")+COUNTIF(D%d:D%d,"No")'
            '+COUNTIF(D%d:D%d,"Por pedir")'
            % (CLI['preg_ini'], preg_fin, CLI['preg_ini'], preg_fin,
               CLI['preg_ini'], preg_fin), fmt=C.FMT_ENT)
    CLI['preg_escritas'] = f + 1
    motor.val(ws, 'A%d' % (f + 1), 'Contestadas POR ESCRITO')
    motor.f(ws, 'F%d' % (f + 1),
            '=COUNTIF(D%d:D%d,"Sí")' % (CLI['preg_ini'], preg_fin),
            fmt=C.FMT_ENT)
    CLI['preg_pct'] = f + 2
    motor.val(ws, 'A%d' % (f + 2), 'Ficha cerrada')
    motor.f(ws, 'F%d' % (f + 2),
            motor.iferror('F%d/F%d' % (f + 1, f)), fmt=C.FMT_PCT)
    CLI['preg_ver'] = f + 3
    motor.val(ws, 'A%d' % (f + 3), 'VEREDICTO DE LA FICHA DEL INSTALADOR',
              bold=True)
    motor.f(ws, 'F%d' % (f + 3),
            '=IF(F%d="","",IF(F%d=F%d,"Oferta documentada",'
            'IF(F%d=0,"No has preguntado nada todavía",'
            '"Faltan respuestas por escrito")))'
            % (f + 1, f + 1, f, f + 1), bold=True)
    C.destacado(ws, 'F%d' % (f + 3))
    motor.semaforo_texto(ws, 'F%d' % (f + 3),
                         (('No has preguntado nada todavía', motor.CF_ROJO_BG,
                           motor.CF_ROJO_FG),
                          ('Faltan respuestas por escrito', motor.CF_AMBAR_BG,
                           motor.CF_AMBAR_FG),
                          ('Oferta documentada', motor.CF_VERDE_BG,
                           motor.CF_VERDE_FG)))

    fila = f + 5
    refs, fila = C.bloque_listas(
        ws, fila, [('Respuesta Sí o No', SI_NO), ('¿Por escrito?', POR_ESCRITO)],
        col='A')
    C.dv_rango(ws, coords_sino, refs['Respuesta Sí o No'], 'Respuesta',
               'Elige «Sí» o «No» de la lista.')
    C.dv_rango(ws, coords_esc + ['F%d' % CLI['esc_pot'],
                                 'F%d' % CLI['esc_dt']],
               refs['¿Por escrito?'], '¿Por escrito?',
               'Elige «Sí», «No» o «Por pedir» de la lista.')
    motor.dv_numerica(ws, coords_num, minimo=0,
                      titulo='Respuesta del instalador',
                      mensaje='Escribe un número mayor o igual que 0.')
    C.parrafo(ws, fila,
              'POR QUÉ ESTA HOJA NO CALCULA TU CARGA TÉRMICA. Para calcularla '
              'harían falta la transmitancia de cada cerramiento de TU local, '
              'un coeficiente por m3, los aportes internos reales y las '
              'renovaciones de aire, y no existe ninguna fuente publicada y '
              'verificable que dé esos números para un obrador de chocolate. '
              'Las dos salidas fáciles estaban prohibidas: inventarse los '
              'coeficientes, o dejarte celdas verdes que no sabrías rellenar. '
              'Lo que sí puede hacer un libro honesto es lo de esta hoja: '
              'comprobar que las tres cifras que tú sí conoces encajan entre '
              'sí, y ponerte delante las diez preguntas que separan un '
              'presupuesto de una conversación. Si tu instalador no contesta a '
              'las diez por escrito, no tienes una oferta: tienes un precio.',
              col_ini='A', col_fin='H', alto=90)
    C.pagina(ws, apaisado=True, titulos='6:6')
    return ws


# --------------------------------------------------------------------------
# Hoja «Capacidad por Equipo»
# --------------------------------------------------------------------------
def hoja_capacidad(wb):
    ws = wb.create_sheet(H_CAP)
    C.anchos(ws, {'A': 5, 'B': 44, 'C': 20, 'D': 12, 'E': 13, 'F': 28,
                  'G': 13, 'H': 13, 'I': 13, 'J': 11, 'K': 14, 'L': 14,
                  'M': 16, 'N': 16, 'O': 14, 'P': 84})
    C.encabezar(ws, 'Capacidad por equipo',
                'Un solo modelo para todas las máquinas y todos los puestos: '
                'lo que cabe en un ciclo, cuántos bombones salen de eso, '
                'cuánto dura el ciclo y qué parte de tu surtido pasa por ahí.',
                col_fin='P')
    C.cabecera(ws, 5, [
        ('A', 'Nº'), ('B', 'Equipo o puesto'), ('C', 'Categoría'),
        ('D', '¿Lo tienes?'), ('E', 'Capacidad por ciclo'),
        ('F', 'Unidad de la capacidad'), ('G', 'Bombones por unidad'),
        ('H', 'Bombones por ciclo'), ('I', 'Minutos por ciclo'),
        ('J', 'Ciclos al día'), ('K', 'Bombones al día del equipo'),
        ('L', '% del surtido que pasa'),
        ('M', 'Bombones/día de obrador que permite'),
        ('N', 'Cuenta para el cuello'), ('O', 'Procedencia'), ('P', 'Nota')],
        altura=58)
    fila = C_INI
    f_min_dia = fila_par(P_MIN_DIA)
    for i, (nombre, cat, tiene, cap, unidad, ppu, minutos, pct, fuente,
            notatxt) in enumerate(EQUIPOS_CAPACIDAD):
        motor.val(ws, 'A%d' % fila, i + 1, fmt=C.FMT_ENT)
        motor.val(ws, 'B%d' % fila, nombre, wrap=True)
        motor.val(ws, 'C%d' % fila, cat)
        motor.val(ws, 'D%d' % fila, tiene, verde_=True)
        motor.val(ws, 'E%d' % fila, float(cap), fmt=C.FMT_DEC1, verde_=True)
        motor.val(ws, 'F%d' % fila, unidad, wrap=True)
        motor.val(ws, 'G%d' % fila, float(ppu), fmt=C.FMT_DEC1, verde_=True)
        motor.f(ws, 'H%d' % fila, motor.iferror('E%d*G%d' % (fila, fila)),
                fmt=C.FMT_ENT)
        motor.val(ws, 'I%d' % fila, minutos, fmt=C.FMT_ENT, verde_=True)
        motor.f(ws, 'J%d' % fila,
                motor.iferror("INT('%s'!$B$%d/I%d)" % (H_PAR, f_min_dia, fila)),
                fmt=C.FMT_ENT)
        motor.f(ws, 'K%d' % fila, motor.iferror('H%d*J%d' % (fila, fila)),
                fmt=C.FMT_ENT)
        motor.val(ws, 'L%d' % fila, pct, fmt=C.FMT_PCT, verde_=True)
        motor.f(ws, 'M%d' % fila, motor.iferror('K%d/L%d' % (fila, fila)),
                fmt=C.FMT_ENT)
        motor.f(ws, 'N%d' % fila, '=IF(D%d="Sí",M%d,"")' % (fila, fila),
                fmt=C.FMT_ENT)
        motor.val(ws, 'O%d' % fila, fuente)
        motor.val(ws, 'P%d' % fila, notatxt, wrap=True)
        ws.row_dimensions[fila].height = 62
        fila += 1
    c_fin = fila - 1

    motor.semaforo_isnumber(ws, 'J%d:J%d' % (C_INI, c_fin),
                            '$J%d' % C_INI, operador='<', umbral='1')

    f = c_fin + 2
    motor.val(ws, 'B%d' % f, 'Minutos disponibles al día (de «Parámetros»)')
    motor.f(ws, 'E%d' % f, "='%s'!B%d" % (H_PAR, f_min_dia), fmt=C.FMT_ENT)
    motor.val(ws, 'B%d' % (f + 1), 'Equipos y puestos que dices tener')
    motor.f(ws, 'E%d' % (f + 1), '=COUNTIF(D%d:D%d,"Sí")' % (C_INI, c_fin),
            fmt=C.FMT_ENT)
    motor.val(ws, 'B%d' % (f + 2),
              'Equipos que no cuentan (ciclo más largo que la jornada)')
    motor.f(ws, 'E%d' % (f + 2), '=COUNTIF(J%d:J%d,0)' % (C_INI, c_fin),
            fmt=C.FMT_ENT)
    motor.val(ws, 'P%d' % (f + 2),
              'Un cero en «ciclos al día» quiere decir que el ciclo de esa '
              'máquina no cabe en la jornada que has declarado. No es un error '
              'del libro: es que con ese turno esa máquina no produce nada.',
              wrap=True)
    ws.row_dimensions[f + 2].height = 46

    fila = f + 4
    refs, fila = C.bloque_listas(ws, fila, [('¿Lo tienes?', SI_NO)], col='B')
    C.dv_rango(ws, ['D%d' % r for r in range(C_INI, c_fin + 1)],
               refs['¿Lo tienes?'], '¿Lo tienes?',
               'Elige «Sí» o «No» de la lista.')
    C.parrafo(ws, fila,
              'Las columnas verdes de esta hoja son las que tienes que pelear '
              'con el comercial: cuánto cabe de verdad en un ciclo, cuánto '
              'dura el ciclo COMPLETO -con carga, cristalización y desmoldeo, '
              'no el que pone el folleto- y qué parte de tu surtido pasa por '
              'ahí. Si ya tienes el Kit de Tareas Chocolatería, los tiempos '
              'reales de cada partida los sacas de '
              'kit-tareas-chocolateria/02-partidas-produccion.xlsx; mientras '
              'tanto, los valores por defecto son supuestos coherentes con la '
              'carta de 28 referencias de «La Almendra».',
              col_ini='B', col_fin='P', alto=62)
    fila += 2
    C.parrafo(ws, fila,
              'FÍJATE EN DÓNDE QUEDA LA ATEMPERADORA. Es la máquina que más '
              'cuesta y la que más se mira, y en una bombonería artesana está '
              'lejísimos de ser el cuello de botella: produce chocolate '
              'templado muy por encima de lo que dos personas moldean. Los que '
              'limitan son los moldes que tienes, los ciclos de cristalización '
              'que caben en la jornada y el puesto de envasado, que es el que '
              'nadie presupuesta. Comprar una atemperadora más grande cuando '
              'el cuello está en el envasado es tener el dinero parado.',
              col_ini='B', col_fin='P', alto=62)
    C.pagina(ws, apaisado=True, titulos='5:5')
    return ws


# --------------------------------------------------------------------------
# Hoja «Cuello de Botella»
# --------------------------------------------------------------------------
K_OBJ, K_CAP, K_EQU, K_HOL, K_HOLP, K_MAR, K_VER = 6, 7, 8, 9, 10, 11, 12
K_SEG, K_SEGE = 13, 14
K_PICO_CAB = 17
K_PICO_INI = 18


def hoja_cuello(wb):
    ws = wb.create_sheet(H_CUE)
    C.anchos(ws, {'A': 46, 'B': 22, 'C': 16, 'D': 16, 'E': 16, 'F': 15,
                  'G': 14, 'H': 16, 'I': 16, 'J': 80})
    C.encabezar(ws, 'Cuello de botella',
                'El equipo que manda y los bombones al día que aguanta el '
                'conjunto, en el día normal y en el segundo equipo más '
                'justo. Qué pasa en cada una de las doce campañas del año '
                '-con su propia demanda y su déficit- lo publica el libro 6 '
                '(«Campañas y Valle del Año»), que es a quien viaja esta '
                'capacidad.', col_fin='J')
    n_ini, n_fin = C_INI, C_INI + len(EQUIPOS_CAPACIDAD) - 1
    rng_n = "'%s'!$N$%d:$N$%d" % (H_CAP, n_ini, n_fin)
    rng_b = "'%s'!$B$%d:$B$%d" % (H_CAP, n_ini, n_fin)

    C.seccion(ws, 'A5', 'El día normal')
    motor.val(ws, 'A%d' % K_OBJ,
              'Bombones equivalentes al día que quieres sacar')
    motor.f(ws, 'B%d' % K_OBJ, "='%s'!B%d" % (H_PAR, fila_par(P_OBJ)),
            fmt=C.FMT_ENT)
    motor.val(ws, 'A%d' % K_CAP, 'Bombones al día que permite el conjunto')
    motor.f(ws, 'B%d' % K_CAP, motor.iferror('MIN(%s)' % rng_n), fmt=C.FMT_ENT,
            bold=True)
    C.destacado(ws, 'B%d' % K_CAP)
    motor.val(ws, 'J%d' % K_CAP,
              'ES LA CIFRA QUE VIAJA AL LIBRO 6 (campañas y valle del año, '
              'cruce nº 1): el 6 no puede saber si aguantas Navidad sin esta '
              'capacidad. El libro 6 la pide en CELDA VERDE y la cuadra '
              'contra este número; en toda la guía no hay una sola fórmula '
              'que apunte a otro fichero.', wrap=True)
    ws.row_dimensions[K_CAP].height = 58
    motor.val(ws, 'A%d' % K_EQU, 'El equipo que limita', bold=True)
    motor.f(ws, 'B%d' % K_EQU,
            motor.iferror('INDEX(%s,MATCH(B%d,%s,0))' % (rng_b, K_CAP, rng_n)),
            bold=True)
    C.destacado(ws, 'B%d' % K_EQU)
    motor.val(ws, 'A%d' % K_HOL, 'Holgura sobre el día normal (bombones)')
    motor.f(ws, 'B%d' % K_HOL, motor.iferror('B%d-B%d' % (K_CAP, K_OBJ)),
            fmt=C.FMT_ENT)
    motor.val(ws, 'A%d' % K_HOLP, 'Holgura sobre el día normal (%)')
    motor.f(ws, 'B%d' % K_HOLP, motor.iferror('B%d/B%d' % (K_HOL, K_OBJ)),
            fmt=C.FMT_PCT)
    motor.val(ws, 'A%d' % K_MAR, 'Margen de seguridad que te has exigido')
    motor.f(ws, 'B%d' % K_MAR, "='%s'!B%d" % (H_PAR, fila_par(P_MARGEN)),
            fmt=C.FMT_PCT)
    motor.val(ws, 'A%d' % K_VER, 'VEREDICTO DEL DÍA NORMAL', bold=True)
    motor.f(ws, 'B%d' % K_VER,
            '=IF(B%d="","",IF(B%d<B%d,"NO LLEGAS",IF(B%d<B%d,"AJUSTADO",'
            '"SUFICIENTE")))' % (K_CAP, K_CAP, K_OBJ, K_HOLP, K_MAR),
            bold=True)
    C.destacado(ws, 'B%d' % K_VER)
    motor.semaforo_texto(ws, 'B%d' % K_VER,
                         (('NO LLEGAS', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('AJUSTADO', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          ('SUFICIENTE', motor.CF_VERDE_BG,
                           motor.CF_VERDE_FG)))
    motor.val(ws, 'J%d' % K_VER,
              '«AJUSTADO» quiere decir que pasas el día normal, pero por debajo '
              'del margen de seguridad que tú mismo has pedido: una avería del '
              'frío, una baja o un pedido corporativo te dejan sin género.',
              wrap=True)
    ws.row_dimensions[K_VER].height = 46

    motor.val(ws, 'A%d' % K_SEG, 'El segundo equipo más justo permite')
    motor.f(ws, 'B%d' % K_SEG, motor.iferror('SMALL(%s,2)' % rng_n),
            fmt=C.FMT_ENT)
    motor.val(ws, 'A%d' % K_SEGE, 'Y es')
    motor.f(ws, 'B%d' % K_SEGE,
            motor.iferror('INDEX(%s,MATCH(B%d,%s,0))' % (rng_b, K_SEG, rng_n)))
    motor.val(ws, 'J%d' % K_SEGE,
              'Mira los dos juntos antes de comprar: si el segundo está muy '
              'cerca del primero, resolver sólo el cuello de botella te sube la '
              'capacidad cuatro bombones y te deja el dinero fuera.', wrap=True)
    ws.row_dimensions[K_SEGE].height = 46

    # A1 (refutación 2026-09-12): el bloque de las doce campañas -demanda,
    # déficit y veredicto de campaña- se quitó de esta hoja. SPEC §2.2 asigna
    # ese cálculo al libro 6 («Campañas y Valle del Año»); tenerlo aquí
    # TAMBIÉN, con un modelo distinto (factor de campaña sobre el día normal
    # en vez del reparto por `Peso sobre el Año` del libro 6), publicaba dos
    # demandas y dos déficits distintos para el mismo mes. Este libro se
    # queda con lo que de verdad le corresponde: capacidad por equipo,
    # cuello de botella y veredicto del día normal (y del segundo equipo).
    C.parrafo(ws, K_SEGE + 2,
              'LAS DOCE CAMPAÑAS DEL AÑO -demanda, déficit y qué producto '
              'manda cada pico- están en el libro 6 («Campañas y Valle del '
              'Año»), que es quien pide esta capacidad en celda verde y la '
              'cuadra. Aquí sólo vive el día normal y el equipo que lo '
              'limita: mézclalos y acabas con dos cifras distintas para la '
              'misma pregunta.',
              col_ini='A', col_fin='J', alto=62)
    C.pagina(ws, apaisado=True)
    return ws


# --------------------------------------------------------------------------
# Hoja «Ficha de Visita a Local»
# --------------------------------------------------------------------------
def hoja_local(wb):
    ws = wb.create_sheet(H_LOC)
    C.anchos(ws, {'A': 5, 'B': 52, 'C': 14, 'D': 46, 'E': 15, 'F': 14,
                  'G': 14, 'H': 15, 'I': 16, 'J': 86})
    C.encabezar(ws, 'Ficha de visita a local',
                'Imprímela y llévala a cada visita. Un solo «No» en un ítem '
                'eliminatorio y el veredicto es DESCARTAR.', col_fin='J')
    C.cabecera(ws, 5, [
        ('A', 'Nº'), ('B', 'Qué se comprueba'), ('C', '¿Eliminatorio?'),
        ('D', 'Cómo se comprueba'), ('E', 'Respuesta'), ('F', 'Dato medido'),
        ('G', 'Umbral'), ('H', '¿Cumple el dato?'), ('I', 'Veredicto'),
        ('J', 'Nota y norma')], altura=48)

    umbrales = {
        'POTENCIA': ("='%s'!B%d" % (H_PAR, fila_par(P_POT)), C.FMT_DEC1),
        'ALTURA': ("='%s'!B%d" % (H_PAR, fila_par(P_ALTURA)), C.FMT_DEC1),
        'SUPERFICIE': ("='%s'!B%d" % (H_PAR, fila_par(P_M2)), C.FMT_DEC1),
        'UMBRAL750': ("='%s'!B%d" % (H_PAR, fila_par(P_750)), C.FMT_DEC1),
    }
    fila = L_INI
    for i, (item, elim, como, resp, medido, umbral, sentido, notatxt,
            idlegal) in enumerate(VISITA):
        motor.val(ws, 'A%d' % fila, i + 1, fmt=C.FMT_ENT)
        motor.val(ws, 'B%d' % fila, item, wrap=True)
        motor.val(ws, 'C%d' % fila, elim)
        motor.val(ws, 'D%d' % fila, como, wrap=True)
        motor.val(ws, 'E%d' % fila, resp, verde_=True)
        if medido is not None:
            motor.val(ws, 'F%d' % fila, medido, fmt=umbrales[umbral][1],
                      verde_=True)
            motor.f(ws, 'G%d' % fila, umbrales[umbral][0],
                    fmt=umbrales[umbral][1])
            motor.f(ws, 'H%d' % fila,
                    '=IF(AND(ISNUMBER(F%d),ISNUMBER(G%d)),IF(F%d%sG%d,"Sí",'
                    '"No"),"")' % (fila, fila, fila, sentido, fila))
        else:
            motor.val(ws, 'G%d' % fila, 'No aplica')
            motor.val(ws, 'H%d' % fila, '')
        motor.f(ws, 'I%d' % fila,
                '=IF(H%d="No",IF(C%d="Sí","DESCARTAR","Punto débil"),'
                'IF(E%d="","",IF(E%d="No",IF(C%d="Sí","DESCARTAR",'
                '"Punto débil"),IF(E%d="Por comprobar","Pendiente","OK"))))'
                % (fila, fila, fila, fila, fila, fila))
        motor.val(ws, 'J%d' % fila, notatxt, wrap=True)
        if idlegal:
            nota_legal_celda(ws, 'J%d' % fila, idlegal)
        ws.row_dimensions[fila].height = 62
        fila += 1
    l_fin = fila - 1
    # El ítem de la salida de humos cita DOS fichas: la que dice que un
    # obrador de chocolate no genera aire AE4 (`CHN-46`, en la nota) y la que
    # desmonta la cita habitual del CTE DB-HS 3 (`CHN-45`, aquí). Son dos
    # afirmaciones distintas y cada una lleva la suya.
    nota_legal_celda(ws, 'D%d' % (L_INI + 6), 'CHN-45')
    nota_legal_celda(ws, 'D%d' % (L_INI + 7), 'CHN-48')
    motor.semaforo_texto(ws, 'I%d:I%d' % (L_INI, l_fin),
                         (('DESCARTAR', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('Punto débil', motor.CF_AMBAR_BG,
                           motor.CF_AMBAR_FG),
                          ('Pendiente', motor.CF_GRIS_BG, motor.CF_GRIS_FG),
                          ('OK', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    motor.semaforo_texto(ws, 'H%d:H%d' % (L_INI, l_fin),
                         (('No', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('Sí', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))

    f = l_fin + 2
    filas_res = [
        ('Ítems de la ficha', '=COUNTIF(C%d:C%d,"Sí")+COUNTIF(C%d:C%d,"No")'
         % (L_INI, l_fin, L_INI, l_fin), C.FMT_ENT),
        ('De los cuales, eliminatorios', '=COUNTIF(C%d:C%d,"Sí")'
         % (L_INI, l_fin), C.FMT_ENT),
        ('Motivos de descarte', '=COUNTIF(I%d:I%d,"DESCARTAR")'
         % (L_INI, l_fin), C.FMT_ENT),
        ('Puntos débiles', '=COUNTIF(I%d:I%d,"Punto débil")' % (L_INI, l_fin),
         C.FMT_ENT),
        ('Pendientes de comprobar', '=COUNTIF(I%d:I%d,"Pendiente")'
         % (L_INI, l_fin), C.FMT_ENT),
        ('Resueltos sin problema', '=COUNTIF(I%d:I%d,"OK")' % (L_INI, l_fin),
         C.FMT_ENT),
    ]
    for k, (etq, formula, fmt) in enumerate(filas_res):
        motor.val(ws, 'B%d' % (f + k), etq)
        motor.f(ws, 'E%d' % (f + k), formula, fmt=fmt)
    f_tot, f_desc_n, f_deb_n, f_pend = f, f + 2, f + 3, f + 4
    f_avance = f + len(filas_res)
    motor.val(ws, 'B%d' % f_avance, 'Ficha comprobada')
    motor.f(ws, 'E%d' % f_avance,
            motor.iferror('(E%d-E%d)/E%d' % (f_tot, f_pend, f_tot)),
            fmt=C.FMT_PCT)
    f_ver = f_avance + 1
    motor.val(ws, 'B%d' % f_ver, 'VEREDICTO DEL LOCAL', bold=True)
    motor.f(ws, 'E%d' % f_ver,
            '=IF(E%d>0,"DESCARTAR ESTE LOCAL",IF(E%d>0,'
            '"NO DECIDAS TODAVÍA",IF(E%d>0,"SIGUE ADELANTE CON RESERVAS",'
            '"SIGUE ADELANTE")))' % (f_desc_n, f_pend, f_deb_n), bold=True)
    C.destacado(ws, 'E%d' % f_ver)
    motor.semaforo_texto(ws, 'E%d' % f_ver,
                         (('DESCARTAR ESTE LOCAL', motor.CF_ROJO_BG,
                           motor.CF_ROJO_FG),
                          ('NO DECIDAS TODAVÍA', motor.CF_GRIS_BG,
                           motor.CF_GRIS_FG),
                          ('SIGUE ADELANTE CON RESERVAS', motor.CF_AMBAR_BG,
                           motor.CF_AMBAR_FG),
                          ('SIGUE ADELANTE', motor.CF_VERDE_BG,
                           motor.CF_VERDE_FG)))

    fila = f_ver + 2
    refs, fila = C.bloque_listas(ws, fila, [('Respuesta', RESPUESTAS)],
                                 col='B')
    C.dv_rango(ws, ['E%d' % r for r in range(L_INI, l_fin + 1)],
               refs['Respuesta'], 'Respuesta',
               'Elige «Sí», «No» o «Por comprobar» de la lista.')
    C.parrafo(ws, fila,
              'Los seis ítems eliminatorios no lo son por gusto: son los '
              'defectos que no se arreglan con dinero razonable o que no '
              'dependen de ti (la acometida, la climatización, la comunidad, el '
              'planeamiento, el contrato). El resto encarecen la obra y hay que '
              'llevarlos al libro 2 como partida, no descartar el local por '
              'ellos. Y guarda la ficha de los locales que descartes: comparar '
              'tres fichas es lo que enseña qué estás aceptando sin darte '
              'cuenta.',
              col_ini='B', col_fin='J', alto=62)
    fila += 2
    C.parrafo(ws, fila,
              'LA DIFERENCIA CON UNA PASTELERÍA CABE EN DOS LÍNEAS DE ESTA '
              'FICHA. Un obrador de chocolate no fríe ni asa, así que no '
              'necesita campana ni conducto a cubierta: se cae la partida que '
              'tumba la mitad de los locales. A cambio aparece otra que en '
              'pastelería no existe, y es eliminatoria: el local tiene que '
              'poder climatizarse con deshumidificación a 18-20 grados C. Un '
              'sótano fresco y húmedo es un mal local para el chocolate aunque '
              'esté regalado.',
              col_ini='B', col_fin='J', alto=62)
    C.pagina(ws, apaisado=True, titulos='5:5')
    return ws


# --------------------------------------------------------------------------
# Mapa de celdas citables
# --------------------------------------------------------------------------
def mapa_celdas():
    """`{etiqueta: {ref, tipo}}` — el `valor` lo rellena la verificación
    `data_only` después de `inject_cache`."""
    n_fin = C_INI + len(EQUIPOS_CAPACIDAD) - 1
    p_fin = K_PICO_INI + len(D.CAMPANAS) - 1
    l_fin = L_INI + len(VISITA) - 1
    f_res = l_fin + 2
    f_tot = Z_REF['total']
    m = {}

    def add(etq, hoja, celda, tipo):
        m[etq] = {'ref': '%s.xlsx!%s!%s' % (NOMBRE, hoja, celda),
                  'tipo': tipo}

    # --- Parámetros ------------------------------------------------------
    add('Horas de turno del obrador', H_PAR, 'B%d' % fila_par(P_HORAS),
        'entrada')
    add('Turnos de obrador al día', H_PAR, 'B%d' % fila_par(P_TURNOS),
        'entrada')
    add('Horas productivas sobre la jornada', H_PAR, 'B%d' % fila_par(P_PROD),
        'parametro')
    add('Minutos disponibles al día', H_PAR, 'B%d' % fila_par(P_MIN_DIA),
        'salida')
    add('Días de apertura al año', H_PAR, 'B%d' % fila_par(P_DIAS_ANIO),
        'entrada')
    add('Piezas vendibles al día en velocidad de crucero', H_PAR,
        'B%d' % fila_par(P_PIEZAS), 'entrada')
    add('Bombones equivalentes por pieza vendible', H_PAR,
        'B%d' % fila_par(P_EQUIV), 'entrada')
    add('Bombones equivalentes al día en velocidad de crucero', H_PAR,
        'B%d' % fila_par(P_OBJ), 'salida')
    add('Margen de seguridad exigido', H_PAR, 'B%d' % fila_par(P_MARGEN),
        'parametro')
    add('Superficie total del local', H_PAR, 'B%d' % fila_par(P_M2), 'entrada')
    add('Parte mínima del local dedicada a producción', H_PAR,
        'B%d' % fila_par(P_MIN_PROD), 'parametro')
    add('Potencia eléctrica instalada prevista', H_PAR,
        'B%d' % fila_par(P_POT), 'entrada')
    add('Temperatura exterior de tu ciudad en agosto', H_PAR,
        'B%d' % fila_par(P_TEXT), 'entrada')
    add('Potencia frigorífica ofertada por el instalador', H_PAR,
        'B%d' % fila_par(P_POTFRIG), 'entrada')
    add('Salto de diseño declarado por el instalador', H_PAR,
        'B%d' % fila_par(P_DT_INST), 'entrada')
    add('Altura libre mínima exigida', H_PAR, 'B%d' % fila_par(P_ALTURA),
        'entrada')
    add('Umbral de venta sin licencia previa (Ley 12/2012)', H_PAR,
        'B%d' % fila_par(P_750), 'parametro')

    # --- Zonas -----------------------------------------------------------
    add('Metros cuadrados repartidos entre las zonas', H_ZON, 'D%d' % f_tot,
        'salida')
    add('Descuadre de metros contra la superficie declarada', H_ZON,
        'D%d' % Z_REF['descuadre'], 'salida')
    add('Metros de zona de producción', H_ZON,
        'D%d' % Z_REF['produccion_m2'], 'salida')
    add('Parte del local dedicada a producción', H_ZON,
        'D%d' % Z_REF['produccion_pct'], 'salida')
    add('Metros de tienda y mostrador', H_ZON, 'D%d' % Z_REF['venta_m2'],
        'salida')
    add('Parte del local dedicada a venta', H_ZON, 'D%d' % Z_REF['venta_pct'],
        'salida')
    add('Veredicto del reparto de metros', H_ZON,
        'D%d' % Z_REF['veredicto_reparto'], 'salida')
    add('Veredicto de marcha adelante', H_ZON,
        'D%d' % Z_REF['veredicto_marcha'], 'salida')
    add('Metros del obrador de templado y moldeado (celda de entrada)', H_ZON,
        'D%d' % Z_FILA['Obrador de templado y moldeado'], 'entrada')
    add('Metros de la cámara de chocolate (celda de entrada)', H_ZON,
        'D%d' % Z_FILA['Camara de chocolate'], 'entrada')

    # --- Clima ------------------------------------------------------------
    add('Temperatura mínima objetivo del obrador', H_CLI,
        'B%d' % CLI['obrador'], 'entrada')
    add('Temperatura máxima objetivo del obrador', H_CLI,
        'C%d' % CLI['obrador'], 'entrada')
    add('Humedad máxima objetivo del obrador', H_CLI, 'E%d' % CLI['obrador'],
        'entrada')
    add('Temperatura máxima objetivo de la cámara de chocolate', H_CLI,
        'C%d' % CLI['camara'], 'entrada')
    add('Temperatura máxima objetivo de la vitrina', H_CLI,
        'C%d' % CLI['vitrina'], 'entrada')
    add('Ventanas climáticas incoherentes entre sí', H_CLI,
        'F%d' % CLI['ven_fallos'], 'salida')
    add('Salto de temperatura que tiene que vencer el equipo', H_CLI,
        'F%d' % CLI['dt_real'], 'salida')
    add('Potencia ofertada por metro climatizado', H_CLI,
        'F%d' % CLI['ratio'], 'salida')
    add('SEMÁFORO DE COHERENCIA DEL CLIMA', H_CLI, 'F%d' % CLI['ver'],
        'salida')
    add('Preguntas de la ficha del instalador', H_CLI,
        'F%d' % CLI['preg_total'], 'salida')
    add('Preguntas contestadas por escrito', H_CLI,
        'F%d' % CLI['preg_escritas'], 'salida')
    add('Ficha del instalador cerrada (%)', H_CLI, 'F%d' % CLI['preg_pct'],
        'salida')
    add('VEREDICTO DE LA FICHA DEL INSTALADOR', H_CLI,
        'F%d' % CLI['preg_ver'], 'salida')

    # --- Capacidad -------------------------------------------------------
    for i, eq in enumerate(EQUIPOS_CAPACIDAD):
        add('Bombones/día de obrador que permite: ' + eq[0], H_CAP,
            'M%d' % (C_INI + i), 'salida')
    add('Equipos y puestos que dices tener', H_CAP, 'E%d' % (n_fin + 3),
        'salida')
    add('Minutos disponibles al día (capacidad)', H_CAP, 'E%d' % (n_fin + 2),
        'salida')
    add('Bombones por ciclo del puesto de moldeado', H_CAP,
        'H%d' % (C_INI + 4), 'salida')
    add('Ciclos al día del puesto de moldeado', H_CAP, 'J%d' % (C_INI + 4),
        'salida')
    add('Parte del surtido que pasa por los moldes', H_CAP,
        'L%d' % (C_INI + 3), 'entrada')

    # --- Cuello de botella ------------------------------------------------
    add('Bombones al día objetivo', H_CUE, 'B%d' % K_OBJ, 'salida')
    add('Bombones al día que permite el conjunto', H_CUE, 'B%d' % K_CAP,
        'salida')
    add('El equipo que limita', H_CUE, 'B%d' % K_EQU, 'salida')
    add('Holgura sobre el día normal (bombones)', H_CUE, 'B%d' % K_HOL,
        'salida')
    add('Holgura sobre el día normal (%)', H_CUE, 'B%d' % K_HOLP, 'salida')
    add('Veredicto del día normal', H_CUE, 'B%d' % K_VER, 'salida')
    add('El segundo equipo más justo permite', H_CUE, 'B%d' % K_SEG, 'salida')
    add('El segundo equipo más justo es', H_CUE, 'B%d' % K_SEGE, 'salida')
    # A1 (refutación 2026-09-12): el déficit de capacidad por campaña y su
    # recuento se quitaron de este libro -SPEC §2.2 se los asigna al libro
    # 6- porque los dos calculaban la demanda con modelos distintos y
    # publicaban dos cifras para el mismo mes. Este libro sólo publica la
    # CAPACIDAD (K_CAP, «Bombones al día que permite el conjunto»), que es
    # lo que de verdad viaja al libro 6 (cruce nº 1 de `datos_ejemplo.CRUCES`).

    # --- Ficha de visita --------------------------------------------------
    add('Ítems de la ficha de visita', H_LOC, 'E%d' % f_res, 'salida')
    add('Ítems eliminatorios de la ficha', H_LOC, 'E%d' % (f_res + 1),
        'salida')
    add('Motivos de descarte del local', H_LOC, 'E%d' % (f_res + 2), 'salida')
    add('Puntos débiles del local', H_LOC, 'E%d' % (f_res + 3), 'salida')
    add('Pendientes de comprobar del local', H_LOC, 'E%d' % (f_res + 4),
        'salida')
    add('Ficha de visita comprobada (%)', H_LOC, 'E%d' % (f_res + 6), 'salida')
    add('VEREDICTO DEL LOCAL', H_LOC, 'E%d' % (f_res + 7), 'salida')
    add('Potencia contratable del local', H_LOC, 'F%d' % L_INI, 'entrada')
    add('Superficie útil medida en el local', H_LOC, 'F%d' % (L_INI + 2),
        'entrada')
    add('Altura libre medida en el local', H_LOC, 'F%d' % (L_INI + 3),
        'entrada')
    add('Superficie de exposición y venta medida', H_LOC, 'F%d' % (L_INI + 4),
        'entrada')
    return m


# --------------------------------------------------------------------------
def construir():
    D.gate_legal(IDS_LEGALES)
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_zonas(wb)
    hoja_clima(wb)
    hoja_capacidad(wb)
    hoja_cuello(wb)
    hoja_local(wb)

    wb.properties.creator = 'AI Chef Pro'
    wb.properties.lastModifiedBy = 'AI Chef Pro'
    wb.properties.title = TITULO
    wb.properties.subject = C.PRODUCTO + ' · Versión 1.0 · septiembre 2026'

    verdes = {}
    for ws in wb.worksheets:
        motor.retirar_verde_de_calculadas(ws)
        verdes[ws.title] = motor.proteger(ws)
    wb.calculation.fullCalcOnLoad = True

    destino = os.path.join(AQUI, 'build')
    if not os.path.isdir(destino):
        os.makedirs(destino)
    ruta = os.path.join(destino, NOMBRE + '.xlsx')
    wb.save(ruta)
    C.barrer_cp1252(wb)
    return ruta, verdes


def gate_totales(ruta):
    """`=SUM(rango)` recalculado a mano contra el caché: `pycel` cachea como 0
    un `SUM` que agrega una columna de fórmulas. Se llama DESPUÉS de
    `inject_cache.py`."""
    wbv = openpyxl.load_workbook(ruta, data_only=True)
    incoherentes = C.gate_sum_rango(wbv)
    wbv.close()
    if incoherentes:
        raise SystemExit('TOTALES con caché incoherente:\n  '
                         + '\n  '.join(incoherentes))


def gate_sin_referencias_externas(ruta):
    """Ninguna fórmula de este libro puede nombrar otro fichero (SPEC §2.3,
    cuarta regla dura). Se comprueba sobre el REGISTRO, que es todo lo que se
    ha escrito con `motor.f()`."""
    malas = [(h, c, f) for h, c, f in motor.REGISTRO
             if '.xlsx' in f or '[' in f]
    if malas:
        raise SystemExit('Fórmulas que cruzan ficheros:\n  '
                         + '\n  '.join('%s!%s  %s' % m for m in malas))
    prohibidas = ('INDIRECT', 'COUNTA', 'PMT', 'OFFSET', 'XLOOKUP', 'LET(',
                  'LAMBDA', 'RANK', 'NETWORKDAYS', 'IRR')
    usos = [(h, c, f) for h, c, f in motor.REGISTRO
            for p in prohibidas if p in f.upper()]
    if usos:
        raise SystemExit('Funciones prohibidas:\n  '
                         + '\n  '.join('%s!%s  %s' % u for u in usos))


def verificar_y_mapear(ruta):
    """`inject_cache` + comprobación `data_only` de CADA fórmula registrada +
    `mapa-<libro>.json` con el valor cacheado.

    Ojo con las fórmulas que devuelven `""`: openpyxl con `data_only=True` las
    lee como `None`, exactamente igual que una fórmula que se quedó SIN
    cachear. Distinguirlas a ojo es imposible, así que la comprobación pasa por
    pycel: sólo se acepta el `None` cuando pycel dice que esa fórmula vale
    cadena vacía -que es el «sin dato» de la familia-.
    """
    import logging
    logging.disable(logging.CRITICAL)
    from pycel import ExcelCompiler
    subprocess.check_call(['/usr/local/bin/python3',
                           os.path.join(RAIZ, 'inject_cache.py'), ruta])
    wb = openpyxl.load_workbook(ruta, data_only=True)
    calc = ExcelCompiler(ruta)
    fallos, vacias = [], 0
    for hoja, coord, formula in motor.REGISTRO:
        v = wb[hoja][coord].value
        if isinstance(v, str) and v.startswith('#'):
            fallos.append('%s!%s = %s (%s)' % (hoja, coord, v, formula[:60]))
            continue
        if v is not None:
            continue
        esperado = calc.evaluate("'%s'!%s" % (hoja, coord))
        if esperado == '':
            vacias += 1                     # «sin dato» legítimo, no un hueco
        else:
            fallos.append('%s!%s SIN VALOR, pycel dice %r (%s)'
                          % (hoja, coord, esperado, formula[:60]))
    m = mapa_celdas()
    for etq, d in m.items():
        _f, hoja, celda = d['ref'].split('!')
        v = wb[hoja][celda].value
        if v is None:
            # Una fórmula que devuelve "" se cachea como None: se le pregunta a
            # pycel para que el mapa publique la cadena vacía y no un `null`,
            # que un capítulo leería como «no se pudo calcular».
            v = calc.evaluate("'%s'!%s" % (hoja, celda))
        d['valor'] = v
    destino = os.path.dirname(ruta)
    with open(os.path.join(destino, 'mapa-' + NOMBRE + '.json'), 'w',
              encoding='utf-8') as fh:
        json.dump(m, fh, ensure_ascii=False, indent=1)
    return fallos, m, vacias


# --------------------------------------------------------------------------
def demo(ruta):
    """Comportamientos que el libro tiene que tener, probados con pycel sobre
    el fichero que se acaba de escribir.

    Regla de pycel: hay que **evaluar la salida ANTES de tocar la entrada**.
    `set_value()` invalida los nodos que ya están en el grafo, y los que no
    están todavía se construyen leyendo el valor CACHEADO del fichero: si se
    toca la entrada primero, la salida sale con el número viejo y la prueba
    pasa por casualidad.
    """
    import logging
    logging.disable(logging.CRITICAL)
    from pycel import ExcelCompiler
    resultados = []

    def prueba(nombre, ok, detalle=''):
        resultados.append((nombre, bool(ok), detalle))

    def compilador(salidas):
        c = ExcelCompiler(ruta)
        for a in salidas:
            c.evaluate(a)
        return c

    A_CAP = "'%s'!B%d" % (H_CUE, K_CAP)
    A_EQU = "'%s'!B%d" % (H_CUE, K_EQU)
    A_VER = "'%s'!B%d" % (H_CUE, K_VER)
    A_CLIMA = "'%s'!F%d" % (H_CLI, CLI['ver'])
    A_DT = "'%s'!F%d" % (H_CLI, CLI['dt_real'])
    l_fin = L_INI + len(VISITA) - 1
    A_LOC = "'%s'!E%d" % (H_LOC, l_fin + 2 + 7)

    # 1. El cuello de botella se identifica y el veredicto es coherente.
    c = compilador([A_CAP, A_EQU, A_VER])
    cap, equ, ver = c.evaluate(A_CAP), c.evaluate(A_EQU), c.evaluate(A_VER)
    prueba('El cuello de botella se identifica y trae nombre de equipo',
           isinstance(cap, (int, float)) and isinstance(equ, str) and equ
           and ver in ('NO LLEGAS', 'AJUSTADO', 'SUFICIENTE'),
           'capacidad=%s · equipo=%s · veredicto=%s' % (cap, equ, ver))

    # 2. Quitar el equipo que limita mueve el cuello a otro equipo.
    c = compilador([A_CAP, A_EQU])
    c.set_value("'%s'!D%d" % (H_CAP, C_INI + 8), 'No')   # puesto de envasado
    cap2, equ2 = c.evaluate(A_CAP), c.evaluate(A_EQU)
    prueba('Quitar el equipo que limita mueve el cuello a otro equipo',
           equ2 != equ and cap2 > cap,
           'ahora limita «%s» con %s bombones/día' % (equ2, round(cap2)))

    # 3. Doblar el turno cambia el veredicto del día normal.
    c = compilador([A_CAP, A_VER])
    c.set_value("'%s'!B%d" % (H_PAR, fila_par(P_TURNOS)), 2)
    cap3, ver3 = c.evaluate(A_CAP), c.evaluate(A_VER)
    prueba('Con dos turnos el veredicto del día normal pasa a SUFICIENTE',
           ver3 == 'SUFICIENTE' and cap3 > cap,
           'veredicto=%s · capacidad=%s' % (ver3, round(cap3)))

    # 4. El semáforo del clima caza un salto de diseño corto.
    c = compilador([A_CLIMA, A_DT])
    clima0, dt0 = c.evaluate(A_CLIMA), c.evaluate(A_DT)
    c.set_value("'%s'!B%d" % (H_PAR, fila_par(P_DT_INST)), 8.0)
    clima1 = c.evaluate(A_CLIMA)
    prueba('Un salto de diseño menor que el real enciende el semáforo del '
           'clima',
           clima1 == 'INCOHERENTE: el salto de diseño se queda corto'
           and clima0 != clima1,
           'salto real=%s · antes=%s · después=%s' % (dt0, clima0, clima1))

    # 5. Una ventana climática invertida se detecta.
    c = compilador([A_CLIMA])
    c.set_value("'%s'!C%d" % (H_CLI, CLI['camara']), 24.0)   # cámara > obrador
    clima2 = c.evaluate(A_CLIMA)
    prueba('Una cámara más caliente que el obrador rompe la ventana climática',
           clima2 == 'REVISA LA VENTANA CLIMÁTICA',
           'veredicto=%r' % clima2)

    # 6. Un «No» en un ítem eliminatorio manda DESCARTAR.
    c = compilador([A_LOC])
    base = c.evaluate(A_LOC)
    c.set_value("'%s'!E%d" % (H_LOC, L_INI + 1), 'No')   # climatización, elim.
    tras = c.evaluate(A_LOC)
    prueba('Un «No» en un ítem eliminatorio manda DESCARTAR',
           tras == 'DESCARTAR ESTE LOCAL' and base != tras,
           'antes=%s · después=%s' % (base, tras))

    # 7. El umbral de los 750 m2 se compara al revés y no da falso positivo.
    A_H750 = "'%s'!H%d" % (H_LOC, L_INI + 4)
    c = compilador([A_H750])
    ok750 = c.evaluate(A_H750)
    c.set_value("'%s'!F%d" % (H_LOC, L_INI + 4), 900.0)
    mal750 = c.evaluate(A_H750)
    prueba('El umbral de los 750 m2 se compara al revés (no pasarlo, no '
           'llegar a él)',
           ok750 == 'Sí' and mal750 == 'No',
           'con 22 m2 = %r · con 900 m2 = %r' % (ok750, mal750))

    # 8. Los metros de las zonas cuadran con la superficie declarada.
    c = ExcelCompiler(ruta)
    desc = c.evaluate("'%s'!D%d" % (H_ZON, Z_REF['descuadre']))
    tot = c.evaluate("'%s'!D%d" % (H_ZON, Z_REF['total']))
    prueba('El reparto de metros suma la superficie declarada',
           abs(desc) < 0.001 and abs(tot - D.NEGOCIO['m2_total']) < 0.001,
           'total=%s · descuadre=%s' % (tot, desc))
    return resultados


# --------------------------------------------------------------------------
def main():
    ruta, verdes = construir()
    print('escrito:', ruta)
    gate_sin_referencias_externas(ruta)
    fallos, m, vacias = verificar_y_mapear(ruta)
    gate_totales(ruta)
    res = demo(ruta)
    n_verdes = sum(verdes.values())
    print('-' * 70)
    print('unidad de capacidad  : bombón equivalente '
          '(%.3f min de obrador, tanda BC1)' % MIN_POR_BOMBON)
    print('equivalencia media   : %.2f bombones por pieza vendible' % EQUIV_MEDIA)
    print('objetivo del día     : %.1f bombones equivalentes' % OBJETIVO_DIA)
    print('fórmulas registradas : %d' % len(motor.REGISTRO))
    print('fórmulas sin valor   : %d' % len(fallos))
    for x in fallos[:20]:
        print('   ', x)
    print('fórmulas que dan ""  : %d  (sin dato legítimo)' % vacias)
    print('celdas verdes        : %d  %s' % (n_verdes, verdes))
    print('notas legales        : %d' % NOTAS_LEGALES['n'])
    print('etiquetas del mapa   : %d' % len(m))
    print('demos:')
    for nombre, ok, detalle in res:
        print('   [%s] %s — %s' % ('OK' if ok else 'FALLA', nombre, detalle))
    todo_ok = not fallos and all(ok for _n, ok, _d in res)
    print('-' * 70)
    print('RESULTADO:', 'VERDE' if todo_ok else 'ROJO')
    return 0 if todo_ok else 1


if __name__ == '__main__':
    sys.exit(main())
