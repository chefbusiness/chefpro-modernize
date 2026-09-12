#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
datos_ejemplo.py - JUEGO DE DATOS UNICO del producto «Como Montar una Chocolateria»
(SPEC: scripts/productos-digitales/guia-chocolateria-SPEC.md, §3).

Los 9 libros de Excel, el guion (`guion_guia_chocolateria_obrador.py`), el bonus 1
(business plan modelo relleno) y el bonus 2 («12 decisiones de apertura resueltas»)
beben de ESTE fichero. Regla de la familia: una sola fuente de cifras. Si un numero
cambia, cambia aqui y se regeneran los libros.

QUE ES «LA ALMENDRA» Y QUE NO ES
================================
«La Almendra» es un CASO MODELADO, no un cliente real y no «la bomboneria media de
Espana». Es el juego de datos que permite que las formulas de los 9 libros tengan
que calcular y que el lector vea una hoja rellena antes de borrarla y poner la suya.
Nada de lo que hay aqui es un benchmark.

D51 - COMPROBACION DE MARCA, hecha el 12-09-2026 y declarada aqui:
  · El API de TMview (`tmdn.org/tmview/api/search/results`, oficinas ES+EM, clase 30)
    devolvio error de conexion desde este Mac (curl exit 56, y WebFetch ECONNRESET).
    El buscador de la EUIPO (eSearch) sirve la cascara de la SPA, sin resultados.
    REGISTRO NO CONSULTABLE EL 12-09-2026 DESDE EL MAC.
  · Busqueda web con dos consultas distintas («La Almendra» + chocolateria /
    bomboneria / marca registrada, y «La Almendra» + bombones + obrador): NINGUN
    negocio vivo de chocolate con ese nombre. Lo que sale son productos («bombon
    almendrado», «bombones de almendra») de otras casas, no una marca homonima.
  · Decision: se mantiene «La Almendra». Si al abrir el registro apareciese una
    marca VIVA en clase 30, se cambia el nombre AQUI (candidatos anotados:
    «La Cacaotera», «Bomboneria del Mercado») y se regeneran los nueve libros.

LA REGLA DE PROCEDENCIA (SPEC §3): SOLO HAY CUATRO ORIGENES
===========================================================
Cada campo lleva su origen escrito en el propio `.py`, en un campo `fuente` o en el
comentario de encima. Solo hay cuatro origenes validos, y `comprobar()` lo verifica:

  1. **`CHN-*` / `CHS-*`** - id del JSON comun
     `auditorias/guias-v2-research-sector.json` (635 entradas: 411 heredadas + 109
     CHN de normativa + 115 CHS de sector). **Citados con su sufijo cuando solo
     existen con sufijo** (D44): CHS-24a..d, CHS-25a..d, CHS-27a/b, CHS-28a..d,
     CHS-37a/b/c, CHS-38a..e, CHS-41a..j, CHS-42a..j, CHS-45a/b, CHS-46a..f,
     CHS-47a/b, CHS-69a..d. **`CHS-41` a secas esta PROHIBIDO** (§5.2): existe sin
     sufijo pero es un AGREGADO sin fuente unica, fiabilidad baja.
  2. **El kit publicado**, citado por `fichero.xlsx!Hoja`. La guia CITA el kit, no
     lo reescribe, y donde la guia necesita un numero que el kit ya publica, usa EL
     DEL KIT (D30, D31, D35, D36, D40).
  3. **«supuesto declarado»** - dato de ejemplo para que el modelo funcione. No
     tiene fuente porque no la hay, y asi se dice. Un supuesto NUNCA se escribe en
     la prosa como si fuera un dato del sector.
  4. **`PA-*`** - id de Pasteleria dentro del mismo JSON comun, citado como
     REUTILIZACION y con su fecha de verificacion (10-09-2026). Es lo que sostiene
     el tope de 100 kg/semana del art. 13.9 (`PA-29c`), que ninguna ficha `CHN-*`
     cubre.

No hay un quinto origen. Copiar una redaccion legal de otro kit sin id y sin fecha
sigue prohibido (§5.3).

LO QUE SE LEYO DEL KIT ANTES DE FIJAR UN SOLO DATO (SPEC §1.B, releido hoy)
==========================================================================
`openpyxl.load_workbook(..., read_only=True, data_only=True)`, un fichero cada vez,
con `istats cpu temp` entre lecturas (47,7-53,3 grados C en toda la pasada):

  · `02-partidas-produccion.xlsx!Templado` - coberturas negra 55-70 % de cacao,
    con leche 35-40 %, blanca 28-33 %. Las tres curvas de templado se quedan en el
    kit: la guia NO las repite (K1).
  · `02-partidas-produccion.xlsx!Moldeado` - la tabla de vida util al pie, diez
    filas, y la regla de merma: «El chocolate sin relleno y sin contaminar se puede
    refundir; el que lleva ganache o fruta, a residuo» -> DOS tasas de merma (D40).
  · `04-tareas-perfiles.xlsx` - tres hojas de perfil y sus nombres LITERALES:
    `Chocolatero` · `Dependiente` · `Encargado`.
  · `06-eventos-temporada.xlsx` - solo tres hojas de campana (Navidad, San Valentin,
    Pascua): el calendario completo esta en el BONUS-02.
  · `BONUS-02-calendario-anual-tareas.xlsx!Calendario` - 12 filas, 7 «Alta»
    (feb, mar, abr, may, oct, nov, dic), 4 «Media» (ene, jun, jul, sep) y 1 «Baja»
    (ago), con las COMUNIONES de abril a junio.
  · `08-apertura-cierre-negocio.xlsx!Apertura del Negocio` - tarea 17 (obrador
    18-20 grados C y 50-60 % de humedad) y tarea 16 (vitrina 16-18 grados C y menos
    del 55 % de humedad). Es la hoja que manda en D31.
  · `01-apertura-cierre.xlsx!Apertura` - camara 15-18 grados C / 50-60 %, nevera de
    rellenos 0-4 grados C, sala de tienda 20-22 grados C.
  · `kit-escandallos/05-pasteleria.xlsx` - seis hojas, entre ellas `Tarta Chocolate`.
    Se cita como FRONTERA (D38), no se copia: costea una elaboracion por unidad; lo
    que no existe en el catalogo es el escandallo del obrador de bomboneria.

DECISIONES DE LA SPEC QUE ESTE FICHERO MATERIALIZA
==================================================
  · **D1** - bomboneria con obrador como caso central; taza y churros como COLUMNA
    DE ESCENARIO (`VARIANTES`), nunca como producto aparte.
  · **D2** - bean-to-bar como variante SIN cifras de maquinaria: lista de la compra
    y preguntas al proveedor (`VARIANTES['bean-to-bar']`).
  · **D23a/b/c** - moldes como RANGO (24,20-42,83 euros/ud, `CHS-45a`), mantenedor
    como «desde» (`CHS-41i`), escenarios A y B como RANGO con la etiqueta «BASE
    MIXTA de IVA, no es presupuesto de apertura» pegada.
  · **D30** - las diez vidas utiles son las del kit y la guia NO las reescribe:
    `VIDA_UTIL_KIT` es una COPIA declarada de `02!Moldeado`.
  · **D31** - CINCO temperaturas unicas, las del kit, en `CLIMA`. El semaforo de la
    vitrina solo avisa por encima de 20 grados C.
  · **D32** - los OCHO cruces entre libros viven en `CRUCES`: celda verde + fila de
    cuadre, jamas formula entre ficheros.
  · **D35** - las 12 filas del `BONUS-02` bajan a `CAMPANAS`, fila a fila, con las
    COMUNIONES como campana propia (`CAMPANA_COMUNIONES`).
  · **D36** - el valle es AGOSTO y lo que para es el OBRADOR, no la caja: un mes
    «Baja» de doce, mix distinto en julio y agosto, envios parados de junio a
    septiembre (dato de canal ONLINE).
  · **D37** - dos capas: el 25 % del bombon se calcula SOBRE EL PESO TOTAL con el
    relleno dentro (`CHN-10`), y las tres magnitudes de la norma (materia seca
    total, manteca y desgrasada) se COPIAN de la ficha tecnica del proveedor.
  · **D40** - dos tasas de merma por referencia: recuperable y NO recuperable.
  · **D42e** - el tipo de IVA del taller va SIN CIFRA: no esta exento, pero el tipo
    no se cierra.
  · **D43** - una sola tabla salarial, la de Madrid, marcada EJEMPLO; los salarios
    de mercado (`CHS-69a..d`) van AL LADO y nunca como convenio.
  · **D44** - los ids se citan con su sufijo; `CHS-41` a secas esta prohibido.
  · **D47** - cada referencia declara si se despacha ENVASADA CON ETIQUETA o A
    GRANEL: no es el mismo regimen.
  · **D48** - `PROVEEDORES` lleva la columna «operador / operador posterior /
    comerciante» VACIA para que la rellene el lector, y el numero de DDS solo se
    pide en la primera rama. Y hay una SEGUNDA tabla, `CLIENTES_B2B`.
  · **D52** - 28 referencias en 5 familias, cada una con su denominacion legal del
    RD 1055/2003 y su fila de la matriz 28 x 8 de alergenos de `CHN-34b`.
  · **D53(a)** - la guia publica los OCHO alergenos del Anexo II. La regeneracion
    del kit a 2.1 es una PROPUESTA para John y NO bloquea nada de aqui.

LO QUE NO ENTRA (lista negra del §5 de la SPEC)
===============================================
Ni el censo de chocolaterias, ni las facturaciones agregadas de eInforma, ni el
ticket medio de chocolateria, ni el reparto mensual de ventas como dato, ni la
aritmetica «12 moldes por 30 euros», ni el mantenedor como precio cerrado, ni la
resta de los dos escenarios de dotacion, ni «valle de junio-agosto», ni «los cinco
alergenos de una bomboneria», ni el «carnet de manipulador», ni la lista de
calificativos de calidad, ni la fecha del EUDR «pase lo que pase».
`comprobar()` barre el modulo entero buscando esas cadenas.

VOCABULARIO (SPEC §6)
=====================
chocolateria artesanal (nunca «artesana») · bomboneria · obrador · cobertura ·
templado (nunca «temperado» en el cuerpo) · escandallo · vitrina · bombon (y «trufa»
y «praline» son TIPOS de bombon, no sinonimos) · tableta · chocolate a la taza ·
bean-to-bar (no se traduce) · taller y cata · fat bloom y sugar bloom · coste.
«Dulceria» NO se usa como sinonimo en ninguna parte del producto.

ESTILO: la prosa de los comentarios va SIN TILDES a proposito, y no es descuido. Este
fichero se escribe y se parchea desde el shell, y `CLAUDE.md` documenta que los
caracteres decorativos degeneran al pasar por un heredoc: un parche que «no encuentra»
un texto que ves en el fichero suele ser eso. Renunciando a las tildes en los
comentarios, cualquier script puede localizar y sustituir un literal sin sorpresas.
Los literales que SI se publican al lector -denominaciones legales, literales del kit
y citas del BOE- van tal y como los dice su fuente.

WinAnsi: todo el texto de este fichero cabe en cp1252, y lo comprueba `comprobar()`.
Nada de flechas, signos de «menor o igual», «aproximadamente», espacios finos ni
guiones no separables: los caracteres decorativos de los `.md` no entran en el codigo.

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

#: Fecha de corte de todo el bloque normativo (SPEC §2.3, regla 1).
FECHA_VERIFICACION_LEGAL = '12-09-2026'

#: El producto.
PRODUCT_ID = 'guia-chocolateria-obrador'

#: Ficheros del catalogo de los que se CITA o se COPIA (nunca se vinculan).
KIT_DIR = os.path.join(_DL, 'kit-tareas-chocolateria')
KIT_PARTIDAS = os.path.join(KIT_DIR, '02-partidas-produccion.xlsx')
KIT_PERFILES = os.path.join(KIT_DIR, '04-tareas-perfiles.xlsx')
KIT_EVENTOS = os.path.join(KIT_DIR, '06-eventos-temporada.xlsx')
KIT_APERTURA_NEGOCIO = os.path.join(KIT_DIR, '08-apertura-cierre-negocio.xlsx')
KIT_APERTURA_CIERRE = os.path.join(KIT_DIR, '01-apertura-cierre.xlsx')
KIT_CALENDARIO = os.path.join(KIT_DIR, 'BONUS-02-calendario-anual-tareas.xlsx')
KIT_ESCANDALLOS = os.path.join(_DL, 'kit-escandallos', '05-pasteleria.xlsx')

#: Etiquetas de procedencia del kit, tal y como se escriben en los campos `fuente`.
F_KIT_TEMPLADO = 'kit-tareas-chocolateria/02-partidas-produccion.xlsx!Templado'
F_KIT_MOLDEADO = 'kit-tareas-chocolateria/02-partidas-produccion.xlsx!Moldeado'
F_KIT_PERFILES = 'kit-tareas-chocolateria/04-tareas-perfiles.xlsx'
F_KIT_CALENDARIO = 'kit-tareas-chocolateria/BONUS-02-calendario-anual-tareas.xlsx!Calendario'
F_KIT_08_APERTURA = 'kit-tareas-chocolateria/08-apertura-cierre-negocio.xlsx!Apertura del Negocio'
F_KIT_01_APERTURA = 'kit-tareas-chocolateria/01-apertura-cierre.xlsx!Apertura'

#: Nombres LITERALES de los tres perfiles del kit: son los nombres de las HOJAS de
#: `04-tareas-perfiles.xlsx`, verificados abriendo el fichero el 12-09-2026.
#: §1.B.5 prohibe «maestro chocolatero», «bombonero» y «oficial» como perfiles.  # LN-OK
#: OJO: la hoja `Instrucciones` del kit y el titulo de la fila 1 de cada hoja usan
#: rotulos largos («Maestro Chocolatero / Obrador», «Dependiente de Tienda»,
#: «Encargado de Turno»). Lo que la SPEC declara literal son los NOMBRES DE HOJA,
#: y son estos tres.
PERFILES_KIT = ('Chocolatero', 'Dependiente', 'Encargado')

MESES = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')


# ==========================================================================
# 1. EL NEGOCIO: «La Almendra», 75 m2 en SEIS zonas
# ==========================================================================
#: Seis zonas, 75 m2. NO es el reparto de Pasteleria: aqui no hay zona de horno ni
#: de fermentacion, y si hay camara climatizada de chocolate. El total (75 m2) es
#: supuesto declarado apoyado en la convergencia de cuatro fuentes con su formato
#: dicho (§3.1); el reparto POR ZONA tambien es supuesto.
ZONAS = [
    # (zona, m2, fuente del m2, nota)
    ('Obrador de templado y moldeado', 26.0, 'supuesto',
     'La zona que manda sobre el local: aqui van la atemperadora, la mesa de marmol '  # LN-OK
     'o granito, la enrobadora y los moldes. Clima propio (18-20 grados C y 50-60 % '
     'de humedad, F_KIT_08_APERTURA) y marcha adelante: la cobertura entra por un '
     'extremo y el bombon acabado sale por el otro sin cruzarse con ella.'),
    ('Camara de chocolate', 6.0, 'supuesto',
     'Zona propia y climatizada a 15-18 grados C con 50-60 % de humedad '
     '(F_KIT_01_APERTURA). No es una nevera: el chocolate acabado NO va a 4 grados C. '
     'Dentro de ella, o al lado, la nevera de rellenos y ganaches a 0-4 grados C.'),
    ('Almacen de cobertura y materias primas', 8.0, 'supuesto',
     'La cobertura llega en cajas de 5 a 25 kg y es el inmovilizado mas grande del '
     'obrador: el libro 3 calcula cuantas semanas de stock caben aqui. En oscuridad '
     'y lejos de olores fuertes: el cacao los absorbe (F_KIT_MOLDEADO).'),
    ('Envasado y packaging', 5.0, 'supuesto',
     'Mesa de montaje de cajas, etiquetadora y almacen de packaging de campana. Es '
     'la zona que se desborda en Navidad y la que nadie dibuja en el plano.'),
    ('Tienda y mostrador', 22.0, 'supuesto',
     'Sala a 20-22 grados C (F_KIT_01_APERTURA) con la vitrina de bomboneria a '
     '16-18 grados C. Los dos climas son distintos y conviven en la misma sala: es '
     'el motivo de que la vitrina lleve su propio control.'),
    ('Aseos y vestuario', 8.0, 'supuesto',
     'Vestuario de personal separado del aseo de publico. Si no caben los dos, el '
     'local no sirve: es una de las eliminatorias de la ficha de visita.'),
]

BLOQUES_M2 = {'Produccion': 45.0, 'Tienda': 22.0, 'Servicios': 8.0}

#: A que bloque pertenece cada zona (para el resumen de «Zonas y m2» del libro 1).
ZONA_A_BLOQUE = {
    'Obrador de templado y moldeado': 'Produccion',
    'Camara de chocolate': 'Produccion',
    'Almacen de cobertura y materias primas': 'Produccion',
    'Envasado y packaging': 'Produccion',
    'Tienda y mostrador': 'Tienda',
    'Aseos y vestuario': 'Servicios',
}

#: Las CINCO temperaturas unicas de D31, y las cinco son las del kit. La guia NO
#: publica la discrepancia interna del kit (R3-M2): para el obrador se cita SOLO
#: `08-apertura-cierre-negocio.xlsx!Apertura del Negocio`, que dice 50-60 % hoy y
#: lo seguira diciendo si el kit pasa a 2.1.
#:
#: El semaforo de la vitrina (libro 5) se construye con el rango de trabajo que el
#: lector teclea en celda verde y SOLO avisa por encima de `vitrina_umbral_alarma`.
#: Queda PROHIBIDO un semaforo que ponga en rojo los 16-18 grados C del propio kit.
CLIMA = {
    'obrador': {
        'concepto': 'Obrador de templado y moldeado',
        't_min': 18.0, 't_max': 20.0, 'hr_min': 50.0, 'hr_max': 60.0,
        'fuente': F_KIT_08_APERTURA,
        'literal': ('Verificar la temperatura y la humedad del obrador: objetivo '
                    '18-20 grados C y 50-60 %'),
        'nota': ('Es la tarea 17 de la hoja, y es el objetivo mas restrictivo que '
                 'publica el kit: es el que manda. `CHS-44` publica 18-22 grados C '
                 'como rango de trabajo de un tercero, y entra en la prosa del '
                 'cap. 07 como tal, nunca como objetivo del juego de datos.')},
    'camara': {
        'concepto': 'Camara de conservacion de chocolate',
        't_min': 15.0, 't_max': 18.0, 'hr_min': 50.0, 'hr_max': 60.0,
        'fuente': F_KIT_01_APERTURA,
        'literal': ('Comprobar que la camara de conservacion ha funcionado toda la '
                    'noche (sin cortes ni alarmas) y registrar la temperatura: '
                    'objetivo 15-18 grados C y 50-60 % de humedad'),
        'nota': 'Tarea 2. Es la misma ventana en la que el kit declara las vidas utiles.'},
    'nevera_rellenos': {
        'concepto': 'Nevera de rellenos y ganaches',
        't_min': 0.0, 't_max': 4.0, 'hr_min': None, 'hr_max': None,
        'fuente': F_KIT_01_APERTURA,
        'literal': ('Comprobar que la nevera de rellenos y ganaches ha funcionado '
                    'toda la noche y registrar la temperatura: objetivo 0-4 grados C'),
        'nota': ('Tarea 3. Es la nevera del RELLENO, no la del bombon acabado: el '
                 'chocolate terminado no va a 4 grados C, condensa.')},
    'sala_tienda': {
        'concepto': 'Sala de tienda',
        't_min': 20.0, 't_max': 22.0, 'hr_min': None, 'hr_max': None,
        'fuente': F_KIT_01_APERTURA,
        'literal': 'Encender aire acondicionado - mantener sala 20-22 grados C',
        'nota': ('Tarea 6. Confundir la temperatura de la SALA con la de la CAMARA '
                 'es uno de los errores de metodo que la SPEC prohibe: son dos cosas '
                 'distintas y conviven en el mismo local.')},
    'vitrina': {
        'concepto': 'Vitrina de bomboneria',
        't_min': 16.0, 't_max': 18.0, 'hr_min': None, 'hr_max': 55.0,
        'fuente': F_KIT_08_APERTURA,
        'literal': ('Comprobar que las vitrinas temperadas han alcanzado 16-18 '        # LN-OK
                    'grados C y menos del 55 % de humedad antes de montar el genero'),  # LN-OK
        'nota': ('Tarea 16. Es el OBJETIVO OPERATIVO, lo que se comprueba cada '
                 'manana. `CHS-43` publica ademas el RANGO DE TRABAJO de un equipo '
                 'real (+14/+17 grados C, Docriluc WB-6-6-R, base SIN IVA declarada), '
                 'que es otra cosa. El semaforo del libro 5 se alimenta del rango que '
                 'el lector teclea y solo avisa por encima de 20 grados C.')},
}

#: El unico umbral que dispara el semaforo de vitrina: el punto en el que la manteca
#: de cacao empieza a fundir. Es el que publica el kit
#: (`01-apertura-cierre.xlsx!Instrucciones` y `!Apertura`, tarea 5).
VITRINA_UMBRAL_ALARMA_C = 20.0
FUENTE_VITRINA_UMBRAL = F_KIT_01_APERTURA

NEGOCIO = {
    'nombre': 'Bomboneria «La Almendra»',
    'nombre_corto': 'La Almendra',
    'fuente_nombre': 'supuesto',
    'nota_nombre': ('Supuesto declarado, neutro y sin marca real; paralelo a «La '
                    'Encina» (Food Cost y Manual del Manager) y «La Clara» '
                    '(Pasteleria). D51: el registro de marcas NO fue consultable el '
                    '12-09-2026 desde el Mac (TMview y EUIPO caidos para consulta '
                    'automatizada) y la busqueda web no devolvio ningun negocio vivo '
                    'de chocolate con ese nombre. Ver el docstring del modulo.'),

    'formato': ('Obrador propio mas tienda a calle, en una ciudad media espanola SIN '
                'nombre propio: el lector la sustituye por la suya'),
    'fuente_formato': 'CHS-03',
    'nota_formato': ('`CHS-03` describe el sub-concepto «bomboneria/chocolateria '
                     'artesana con obrador + tienda»: 60-100 m2, 1-2 empleados. Es '  # LN-OK
                     'el eje del producto (D1). La chocolateria de taza y churros es '
                     'OTRO negocio y entra como columna de escenario (`VARIANTES`).'),

    'm2_total': 75.0,
    'fuente_m2': 'supuesto',
    'nota_m2': ('Supuesto declarado, elegido por convergencia de cuatro fuentes CON '
                'SU FORMATO DICHO: `CHS-03` (bomboneria artesana, 60-100 m2), '
                '`CHS-38a` (pasteleria-bomboneria con obrador, 90 m2 y 26.000 euros '
                'de traspaso: el comparable mas cercano del censo), `CHS-58` (minimo '
                'de franquicia, 55 m2) y, como referencia de OTRO formato, los '
                'traspasos de churreria-chocolateria `CHS-37a` (75 m2) y `CHS-37b` '
                '(74 m2). Se elige 75 por estar dentro de `CHS-03` y por debajo de '
                '`CHS-38a`. El reparto por zona tambien es supuesto.'),
    'zonas': ZONAS,
    'bloques_m2': BLOQUES_M2,

    # Potencia. NINGUNA fuente publica la potencia instalada de un obrador de
    # chocolate: es supuesto entero, y por eso el libro 1 lo pide en celda verde.
    'potencia_instalada_kw': 28.0,
    'fuente_potencia_instalada': 'supuesto',
    'nota_potencia': ('Supuesto. Un obrador de chocolate NO tiene hornos: lo que '
                      'consume es el frio (camara, nevera de rellenos y vitrina, 24 '
                      'horas), la climatizacion con deshumidificacion y la '
                      'atemperadora. La potencia a contratar la fija el proyecto '
                      'electrico, no una tabla: el libro 1 la pide en celda verde.'),

    # Clima: la partida que nadie presupuesta y que aqui tiene bloque de CAPEX propio.
    'clima': CLIMA,
    't_exterior_agosto_c': 36.0,
    'fuente_t_exterior': 'supuesto',
    'nota_t_exterior': ('Supuesto de ciudad media espanola de interior en agosto. Es '
                        'una CELDA VERDE del libro 1: el lector pone la de su ciudad, '
                        'y con ella el semaforo compara la temperatura objetivo del '
                        'obrador con la potencia frigorifica que le OFREZCA EL '
                        'INSTALADOR. El libro NO calcula carga termica (D33): no hay '
                        'un solo coeficiente con fuente.'),
    'potencia_frigorifica_ofertada_kw': 9.0,
    'fuente_potencia_frigorifica': 'supuesto',

    # Jornada y calendario comercial.
    'horas_turno': 8.0,
    'fuente_horas_turno': 'supuesto',
    'dias_apertura_semana': 6,
    'dias_apertura_anio': 304,
    'fuente_dias_apertura': 'supuesto',
    'nota_dias_apertura': ('6 dias por semana x 52 semanas = 312, menos 8 dias de '
                           'cierre por festivos = 304. En agosto la TIENDA NO CIERRA: '
                           'lo que para es el obrador (D36, y el literal del kit '
                           'dice «la tienda abre para el turista aunque el obrador '
                           'pare»). Una bomboneria de menos de 300 m2 tiene libertad '
                           'horaria por el art. 5.2 de la Ley 1/2004, no por el 5.1 '
                           '(`CHN-77`).'),

    # Apertura: 1 de junio, mes «Media» del propio calendario del kit.
    'mes_apertura_recomendado': 6,
    'dia_apertura_recomendado': 1,
    'nombre_mes_apertura': 'junio',
    'fuente_mes_apertura': 'supuesto',
    'nota_mes_apertura': ('Supuesto declarado. Junio es «Media» en el calendario del '
                          'kit (F_KIT_CALENDARIO), deja SEIS meses de rodaje antes de '
                          'Navidad y mete el valle de agosto dentro del arranque, que '
                          'es cuando sale barato. Abrir dentro de una campana «Alta» '
                          'es el error que el cronograma del libro 8 avisa.'),

    # Local en alquiler: el escenario base es obra nueva sobre local alquilado.
    'renta_mensual': 1300.0,
    'fuente_renta': 'supuesto',
    'nota_renta': ('Supuesto para una ciudad media. La renta observada en los ocho '
                   'traspasos verificados va de 910 euros/mes (`CHS-37b`, 74 m2 en '
                   'Madrid-Vallecas) a 2.200 euros/mes (`CHS-38c`, 180 m2 en '
                   'Barcelona); aqui se toma la parte baja porque ninguna de esas '
                   'dos ciudades es una ciudad media.'),
    'meses_fianza': 2,
    'fuente_fianza': 'supuesto',
}


# ==========================================================================
# 2. CONVENIO, SALARIOS DE MERCADO Y PLANTILLA
# ==========================================================================
#: D43: esta PROBADO que NO existe convenio estatal del chocolate. REGCON con
#: autoridad laboral «Estatal» devuelve «No se ha encontrado ningun acuerdo con los
#: parametros seleccionados» para chocolate, bombones, confiteria y pasteleria, y el
#: control con «turrones» devuelve 29 tramites, asi que la consulta funciona
#: (`CHN-66`). Por eso entra UNA sola tabla salarial, la de Madrid, MARCADA COMO
#: EJEMPLO y en celda verde, mas el metodo para identificar el convenio del lector.
#: Queda PROHIBIDA cualquier otra tabla salarial.
CONVENIO = [
    # (n, grupo profesional, euros/mes, euros/ano, areas funcionales, puestos que cita)
    (1, 'Tecnicos y titulados superiores', 1733.88, 26008.20,
     ('ADMINISTRACION',), ''),
    (2, 'Direccion, jefes y encargados', 1427.89, 21418.35,
     ('OBRADOR', 'TIENDA', 'ADMINISTRACION'), 'maestro de obrador, encargado'),
    (3, 'Personal especialista', 1376.91, 20653.65,
     ('OBRADOR', 'TIENDA'), 'especialista de produccion, encargado de seccion'),
    (4, 'Personal cualificado', 1249.42, 18741.30,
     ('OBRADOR', 'TIENDA'), 'personal cualificado de produccion y de envasado, dependiente'),
    (5, 'Personal de apoyo', 1192.42, 17886.30,
     ('OBRADOR', 'TIENDA'), 'ayudante de produccion, ayudante de comercio'),
    (6, 'Personal de ayuda en servicios auxiliares', 1192.42, 17886.30,
     ('OBRADOR', 'TIENDA'), 'peon, limpiador, almacenero'),
]
FUENTE_CONVENIO = 'CHN-65b'
CONVENIO_CODIGO = '28001025011981'
CONVENIO_DENOMINACION = 'CONFITERIAS PASTELERIAS Y REPOSTERIA (COMERCIO E INDUSTRIA)'
FUENTE_CONVENIO_DENOMINACION = 'CHN-65c'
CONVENIO_AUTORIDAD = 'Madrid'
CONVENIO_VIGENCIA = '01/01/2024 a 31/12/2026'
CONVENIO_REVISION_SALARIAL = '28/02/2026'
CONVENIO_PAGAS = 15
CONVENIO_ES_EJEMPLO = True
NOTA_CONVENIO = (
    'TABLA DE EJEMPLO, en celda verde y sustituible. El codigo y la denominacion '
    'son los oficiales del REGCON (`CHN-65c`, fila literal), y las cuantias de 2026 '
    'a 15 pagas son las de `CHN-65b`. «BOLLERIAS» NO aparece en la denominacion del '
    'registro: «Confiteria, Pasteleria, Bolleria y Reposteria» es texto del art. 2 '
    'del articulado (`CHN-65`), y quien busque por ese nombre en REGCON no encuentra '
    'el convenio. Es justo lo que ensena el cap. 17. Aviso de `CHN-65`: el despacho '
    'de bombones esta dentro del ambito sin condiciones; la FABRICACION va '
    'condicionada. Las tablas CADUCAN el 31-12-2026.')

#: Los cuatro convenios de sector de ambito igual o superior a la provincia que SI
#: nombran chocolates o bombones (`CHN-93`). Se publican como tales, nunca como
#: tabla salarial: el ambito funcional entre los dos provinciales queda EXCLUIDO de
#: la verificacion legal y va como pregunta para un laboralista, no como respuesta.
CONVENIOS_QUE_NOMBRAN_CHOCOLATE = [
    ('45000145011981', 'Toledo', '', 'CHN-93'),
    ('80000725012008', 'Comunitat Valenciana',
     'CHOCOLATES, TORREFACTORES DE CAFES Y SUCEDANEOS (01/01/2023-31/12/2026)', 'CHN-93'),
    ('01000425011981', 'Alava', 'caducado', 'CHN-93'),
    ('22001125012010', 'Huesca', '', 'CHN-93'),
]

#: Salarios de MERCADO, orientativos y NUNCA como convenio (`N-20` lo prohibe).
#: Se publican AL LADO de la tabla del convenio, no dentro, con su fiabilidad a la
#: vista. «Oficial de primera», «auxiliar» y «bombonero» son las ETIQUETAS DE LA
#: FUENTE salarial -el `tema` de `CHS-69a` es literalmente «Salarios de mercado -
#: Chocolatero / bombonero especializado»-, no perfiles de La Almendra: van
#: entrecomilladas y con su equivalencia con los tres perfiles del kit.
SALARIOS_MERCADO = [
    # (etiqueta de la fuente, min euros/h, max euros/h, equivalencia con el kit, id)
    ('«Chocolatero / bombonero especializado»', 13.0, 16.0, 'Chocolatero', 'CHS-69a'),   # LN-OK
    ('«Oficial de primera»', 11.0, 13.0, 'Chocolatero', 'CHS-69b'),                      # LN-OK
    ('«Auxiliar / ayudante»', 8.0, 9.50, 'Dependiente', 'CHS-69c'),                      # LN-OK
    ('«Encargado / maestro»', 15.0, 20.0, 'Encargado', 'CHS-69d'),                       # LN-OK
]
NOTA_SALARIOS_MERCADO = (
    'Orientativos, fiabilidad media, y NUNCA se presentan como tabla de convenio '
    '(`N-20`). Las etiquetas entrecomilladas son las de la fuente salarial, no los '
    'perfiles de La Almendra: los perfiles son los tres del kit, y la columna de '
    'equivalencia esta para eso. Sirven para saber si lo que vas a ofrecer esta '
    'dentro de mercado; lo que te OBLIGA es tu convenio.')

#: 3 personas / 2,5 jornadas. Los tres nombres son LITERALES de las hojas del kit
#: (`PERFILES_KIT`). Las jornadas son supuesto declarado. Dimension coherente con
#: `CHS-70` («1-2 empleados» en 60-100 m2) mas el titular.
PLANTILLA = [
    # (id, perfil, jornada, grupo de convenio, area, horas/semana, turno)
    ('P1', 'Encargado',    1.0, 2, 'OBRADOR', 40, 'Partido (08:00-13:00 y 17:00-20:00)'),
    ('P2', 'Chocolatero',  1.0, 3, 'OBRADOR', 40, 'Manana (07:00-15:00)'),
    ('P3', 'Dependiente',  0.5, 4, 'TIENDA',  20, 'Tarde (16:30-20:30)'),
]
FUENTE_PLANTILLA = 'CHS-70 + supuesto'
NOTA_PLANTILLA = (
    'El Encargado ES el titular, y por eso su retribucion va en la nomina y no como '
    'renglon aparte de «retribucion del propietario»: lo que si va aparte es su '
    'cuota de autonomos. Las jornadas (1,0 + 1,0 + 0,5 = 2,5) son supuesto '
    'declarado. «Maestro chocolatero», «bombonero» y «oficial» estan PROHIBIDOS '     # LN-OK
    'como nombre de perfil: no existen en el kit.')


# ==========================================================================
# 3. PARAMETROS
# ==========================================================================
#: `ss_empresa` y `smi_anual` son los MISMOS parametros de la familia
#: (`guias-v2_0/motor.py`: `PARAMETROS['ss_empresa']` = 0,33 y
#: `PARAMETROS['smi_anual']` = 17.094 euros). No se duplica el valor con otro
#: numero: se copia el de la familia y se dice de donde sale.
PARAMS = {
    # --- laboral ---------------------------------------------------------
    'pagas_convenio': (15, 'CHN-65b',
                       'El convenio de Madrid paga 15, no 14: cambia el coste mes a mes.'),
    'ss_empresa': (0.33, 'motor.PARAMETROS[ss_empresa]',
                   'Cotizacion empresarial aproximada sobre el bruto (contingencias '
                   'comunes, desempleo, FOGASA y formacion). Es el mismo parametro '
                   'que usa el resto de la familia. Ajustala a tu convenio y a tus '
                   'contratos.'),
    'smi_mensual': (1221.0, 'CHN-67',
                    'RD del SMI 2026: 40,70 euros/dia o 1.221 euros/mes. Caduca el '
                    '31-12-2026, asi que vive en el ANEXO y en celda verde, nunca '
                    'cosido en la prosa.'),
    'smi_anual': (17094.0, 'CHN-67 + motor.PARAMETROS[smi_anual]',
                  'Cuantia ANUAL de referencia. El real decreto NO dice «14 pagas»: '
                  'multiplicar por 14 es aritmetica nuestra. En una bomboneria manda '
                  'el convenio, y el grupo mas bajo de la tabla de Madrid '
                  '(17.886,30 euros/ano) ya lo supera.'),
    'horas_semana_jornada_completa': (40, 'supuesto',
                                      'La jornada anual del convenio de Madrid NO se '
                                      'ha verificado: 40 h/semana es el supuesto de '
                                      'trabajo.'),
    'horas_anuales_contrato': (1780, 'supuesto',
                               '40 h x 52 semanas = 2.080, menos 30 dias naturales '
                               'de vacaciones y los festivos del calendario laboral.'),
    'ratio_horas_productivas': (0.85, 'supuesto',
                                'Parte de la jornada que se pasa a pie de mesa. El '
                                '15 % restante es recepcion, limpieza, formacion y '
                                'reuniones.'),

    # --- IVA (`CHN-71`, `CHN-71b`, `CHN-71c`; verificado el 12-09-2026) ---
    'iva_producto': (0.10, 'CHN-71',
                     'El chocolate va al 10 % POR EXCLUSION, no porque un precepto '
                     'lo nombre: la lista del 4 % del art. 91.Dos.1.1.o es cerrada y '
                     'tiene siete letras, el chocolate no esta en ninguna, y tampoco '
                     'esta entre las dos exclusiones del 10 % (bebidas alcoholicas y '
                     'refrescantes).'),
    'iva_taza_servida': (0.10, 'CHN-71c',
                         'La taza servida en sala es prestacion de servicio de '
                         'hosteleria, no entrega de un bien. Va al 10 % por el '
                         'art. 91.Uno.2.2.o.'),
    'iva_taller': (None, 'CHN-71b',
                   'SIN CIFRA A PROPOSITO (D42e). Lo que SI esta cerrado: un taller '
                   'de bomboneria NO esta exento de IVA, porque el art. 20.Uno.10.o '
                   'excluye las clases «para cuya realizacion sea necesario darse de '
                   'alta en las tarifas de actividades empresariales o artisticas '
                   'del IAE». Lo que NO esta cerrado es el TIPO: el art. 91 no '
                   'nombra los talleres. Va en celda verde y la guia no publica '
                   'ningun tipo.'),
    'iva_equipamiento': (0.21, 'art. 90.Uno de la Ley 37/1992',
                         'Tipo general. Sin la columna «lleva IVA» el CAPEX sale un '
                         '21 % desviado (regla 3 de §2.3).'),
    'iva_obra': (0.21, 'art. 90.Uno de la Ley 37/1992', 'Tipo general.'),
    'iva_general': (0.21, 'art. 90.Uno de la Ley 37/1992', 'Tipo general.'),

    # --- margen: UNA SOLA REGLA -------------------------------------------
    'food_cost_objetivo': (0.30, 'supuesto',
                           'REGLA UNICA de la casa, y es SUPUESTO: no existe dato '
                           'publico de food cost de bomboneria. '
                           '`margen_bruto_objetivo()` deriva el margen sobre PVP, '
                           'que con este food cost es el 70 %. El libro 4 pide UNO de '
                           'los dos numeros y calcula el otro: margen bruto y food '
                           'cost son la misma regla dicha dos veces, y publicarlos '
                           'como dos reglas es un error de metodo prohibido. '
                           'Se calcula SIEMPRE sobre base imponible en los DOS lados '
                           'del cociente (regla 3 de §2.3).'),
    'packaging_pct_coste': (0.12, 'supuesto',
                            'Peso del packaging sobre el coste total de la pieza. En '
                            'bomboneria pesa mas que en pasteleria: la caja ES el '
                            'producto en las campanas de regalo. Supuesto.'),

    # --- comercial (todo supuesto; `N-13` prohibe el ticket medio de chocolateria) ---
    'tickets_dia_crucero': (67, 'supuesto',
                            'Clientes por dia en velocidad de crucero. NO es un dato '
                            'del sector: `N-13` prohibe publicar un ticket medio de '
                            'chocolateria o un reparto mensual de ventas como dato, '
                            'porque no existe dato publico. La guia ensena a medirlo '
                            'con el TPV en dos semanas. Esta calibrado para que el '
                            'margen neto del ano de crucero caiga entre el 9 % y el '
                            '11 %: por encima, el caso se lee como optimista y un '
                            'refutador lo tumba con razon. Es la UNICA palanca que se '
                            'toca para mover el margen; los costes no se maquillan.'),
    'piezas_por_ticket': (1.4, 'supuesto',
                          'De aqui sale el ticket medio, que NO se teclea: se calcula '
                          'como PVP medio ponderado de la carta x piezas por ticket. '
                          'En bomboneria es BAJO -1,4- porque la unidad de venta real '
                          'es la caja, no la pieza: quien entra a por un regalo se '
                          'lleva UNA caja de 20 euros, no ocho bombones sueltos.'),

    # --- fondo de maniobra: vive SOLO en el libro 7 (R4-A1) ---------------
    'meses_colchon_fondo_maniobra': (6, 'supuesto',
                                     'Meses de gastos fijos que hay que tener en caja '
                                     'el dia que abres. PARAMETRO UNICO, y vive en el '
                                     'LIBRO 7: alli estan los gastos fijos con los que '
                                     'se multiplica. El libro 2 NO lo pide -si lo '
                                     'pidiera, el fondo se calcularia dos veces y los '
                                     'dos libros publicarian dos inversiones totales '
                                     'distintas, que es el defecto ALTO que Pasteleria '
                                     'pago-: recibe el fondo YA CALCULADO por celda '
                                     'verde mas fila de cuadre (cruce 2 <- 7 de '
                                     '`CRUCES`).'),
    'anios_amortizacion': (10, 'supuesto',
                           'Vida util contable del inmovilizado amortizable. Sin '
                           'amortizacion, la rentabilidad publicada es mentira: la '
                           'atemperadora se gasta.'),
    'anio_crucero': (2, 'supuesto',
                     'El ano 1 va en rampa y con carencia de principal, asi que la '
                     'foto «de un mes normal» es la del ano 2. Lo usan los gastos '
                     'fijos y, a traves suyo, el fondo de maniobra.'),
    'horizonte_comparacion_anios': (5, 'supuesto',
                                    'Horizonte de la comparacion «traspaso vs obra '
                                    'nueva» del libro 2.'),
}


def P(clave):
    """Valor de un parametro. `PARAMS[clave]` es (valor, fuente, nota)."""
    return PARAMS[clave][0]


def margen_bruto_objetivo():
    """REGLA UNICA. El margen bruto se DERIVA del food cost objetivo; nunca se
    guardan los dos numeros por separado."""
    return 1.0 - P('food_cost_objetivo')


# ==========================================================================
# 4. LAS COBERTURAS: la celda mas critica de todo el paquete
# ==========================================================================
#: UN CONCEPTO, UNA FUENTE. El precio de la cobertura vive SOLO aqui y en el libro 3;
#: los libros 4 y 7 lo COPIAN por celda verde con fila de cuadre (cruces 4 <- 3 y
#: 7 <- 3 de `CRUCES`), nunca por formula entre ficheros.
#:
#: REGLA DE IVA (§2.3, regla 3, ampliada a la materia prima): `CHS-28a` esta
#: declarada en el JSON como «base CON IVA declarada explicitamente por la ficha».
#: Un escandallo se calcula con precios SIN IVA -el soportado es deducible-, asi que
#: el libro 3 publica el precio en LAS DOS BASES y lo que copian el 4 y el 7 es la
#: BASE IMPONIBLE. Con la base equivocada el food cost sale un 9 % alto.
#:
#: Los porcentajes de cacao por tipo son los que el kit ya precarga
#: (`02-partidas-produccion.xlsx!Templado`, filas 6, 7 y 8) y la guia usa los mismos.
#:
#: Las TRES magnitudes que la norma pide de verdad -materia seca TOTAL de cacao,
#: MANTECA de cacao y materia seca DESGRASADA- NO estan en la bolsa: una bolsa de
#: Callebaut 811 publica «54,5 %» y nada mas. Por eso van en TRES CELDAS VERDES que
#: el lector COPIA DE LA FICHA TECNICA DEL PROVEEDOR (capa (b) de D37), y los
#: valores que hay aqui son supuestos de ejemplo declarados.
COBERTURAS = {
    'negra': {
        'nombre': 'Cobertura de chocolate negro (marca, 54,5 % de cacao)',
        'cacao_min_pct': 55.0, 'cacao_max_pct': 70.0,
        'fuente_rango_cacao': F_KIT_TEMPLADO,
        'precio_fuente': 25.02, 'unidad': 'euros/kg',
        'base_iva': 'con IVA', 'tipo_iva': 0.10,
        'fuente_precio': 'CHS-28a',
        'formato': 'bloque de 5 kg a 125,08 euros',
        'es_celda_unica': True,
        # Capa (b) de D37: se COPIAN de la ficha tecnica del proveedor.
        'materia_seca_total_pct': 54.5, 'manteca_pct': 31.0, 'desgrasada_pct': 23.5,
        'fuente_tres_magnitudes': 'supuesto',
        'nota': ('LA CELDA MAS CRITICA DEL PAQUETE. Base CON IVA declarada por la '
                 'ficha (`CHS-28a`): el libro 3 la publica en las dos bases y lo que '
                 'viaja al 4 y al 7 es la base imponible. Las tres magnitudes de '
                 'arriba son SUPUESTO: pidesela a tu proveedor, la bolsa solo trae '
                 'el total.')},
    'origen': {
        'nombre': 'Cobertura de chocolate de origen (70 % de cacao)',
        'cacao_min_pct': 55.0, 'cacao_max_pct': 70.0,
        'fuente_rango_cacao': F_KIT_TEMPLADO,
        'precio_fuente': 37.48, 'unidad': 'euros/kg',
        'base_iva': 'no declarada', 'tipo_iva': 0.10,
        'fuente_precio': 'CHS-28c',
        'formato': 'pepitas de 400 g a 14,99 euros',
        'es_celda_unica': False,
        'materia_seca_total_pct': 70.0, 'manteca_pct': 42.0, 'desgrasada_pct': 28.0,
        'fuente_tres_magnitudes': 'supuesto',
        'nota': ('Factor 1,5 frente a la de marca, y es la decision de '
                 'posicionamiento mas cara del negocio (decision 5 del bonus 2). La '
                 'pagina no declara si el precio lleva IVA: se trata como base '
                 'imponible y se marca.')},
    'leche': {
        'nombre': 'Cobertura de chocolate con leche (38 % de cacao)',
        'cacao_min_pct': 35.0, 'cacao_max_pct': 40.0,
        'fuente_rango_cacao': F_KIT_TEMPLADO,
        'precio_fuente': 19.50, 'unidad': 'euros/kg',
        'base_iva': 'sin IVA', 'tipo_iva': 0.10,
        'fuente_precio': 'supuesto',
        'formato': 'saco de 10 kg',
        'es_celda_unica': False,
        'materia_seca_total_pct': 38.0, 'manteca_pct': 21.0, 'desgrasada_pct': 17.0,
        'fuente_tres_magnitudes': 'supuesto',
        'nota': ('SUPUESTO declarado: no hay precio verificado de cobertura con leche '
                 'en el research. Celda verde con valor por defecto (regla 2 de '
                 '§2.3: ninguna celda verde vacia).')},
    'blanca': {
        'nombre': 'Cobertura de chocolate blanco (30 % de cacao)',
        'cacao_min_pct': 28.0, 'cacao_max_pct': 33.0,
        'fuente_rango_cacao': F_KIT_TEMPLADO,
        'precio_fuente': 21.00, 'unidad': 'euros/kg',
        'base_iva': 'sin IVA', 'tipo_iva': 0.10,
        'fuente_precio': 'supuesto',
        'formato': 'saco de 10 kg',
        'es_celda_unica': False,
        'materia_seca_total_pct': 30.0, 'manteca_pct': 30.0, 'desgrasada_pct': 0.0,
        'fuente_tres_magnitudes': 'supuesto',
        'nota': ('SUPUESTO declarado. Ojo al chocolate blanco: NO lleva materia seca '
                 'desgrasada de cacao, y por eso el art. 6.d) del RD 1055/2003 NO le '
                 'obliga a la mencion «cacao: X % minimo» (`CHN-07`).')},
}

#: Tipo de IVA con el que se convierte el precio de la cobertura a base imponible.
#: Es el del producto (`CHN-71`), no el general.
IVA_COBERTURA = 0.10


def precio_cobertura_base_imponible(clave):
    """El precio de una cobertura llevado a BASE IMPONIBLE, que es la unica base
    valida para un escandallo. Es lo que copian los libros 4 y 7 (cruces 4 <- 3 y
    7 <- 3), nunca el precio «como lo trae la fuente»."""
    c = COBERTURAS[clave]
    if c['base_iva'] == 'con IVA':
        return c['precio_fuente'] / (1.0 + c['tipo_iva'])
    return c['precio_fuente']


def precio_cobertura_como_la_fuente(clave):
    """El precio tal y como lo publica la fuente, con su base declarada. Es la otra
    columna del libro 3, y la que NUNCA debe alimentar un escandallo."""
    c = COBERTURAS[clave]
    return c['precio_fuente'], c['base_iva']


# ==========================================================================
# 5. PRECIOS DE COMPRA DE LOS INGREDIENTES
# ==========================================================================
#: Precio por unidad de compra, EN BASE IMPONIBLE. Las cuatro coberturas se sirven
#: desde `COBERTURAS` para que no haya dos precios del mismo concepto; el resto son
#: SUPUESTOS declarados, porque el research no verifico ningun precio de materia
#: prima de relleno.
PRECIOS_COMPRA = {
    # (precio sin IVA, unidad de compra, fuente)
    'Cobertura negra': (None, 'kg', 'CHS-28a'),
    'Cobertura de origen': (None, 'kg', 'CHS-28c'),
    'Cobertura con leche': (None, 'kg', 'supuesto'),
    'Cobertura blanca': (None, 'kg', 'supuesto'),
    'Nata 35 % MG fresca': (4.20, 'L', 'supuesto'),
    'Nata 35 % MG UHT': (3.10, 'L', 'supuesto'),
    'Mantequilla': (9.80, 'kg', 'supuesto'),
    'Glucosa': (3.40, 'kg', 'supuesto'),
    'Sorbitol': (6.20, 'kg', 'supuesto'),
    'Azucar': (1.15, 'kg', 'supuesto'),
    'Praline de avellana 50 %': (14.80, 'kg', 'supuesto'),
    'Praline de cacahuete 50 %': (9.60, 'kg', 'supuesto'),
    'Pasta pura de avellana': (22.50, 'kg', 'supuesto'),
    'Almendra marcona repelada': (12.40, 'kg', 'supuesto'),
    'Avellana tostada': (13.90, 'kg', 'supuesto'),
    'Pasta de sesamo': (8.90, 'kg', 'supuesto'),
    'Barquillo triturado': (7.60, 'kg', 'supuesto'),
    'Ron anejo': (16.00, 'L', 'supuesto'),
    'Naranja confitada': (9.20, 'kg', 'supuesto'),
    'Yema de huevo pasteurizada': (4.60, 'L', 'supuesto'),
    'Manteca de cacao': (18.60, 'kg', 'supuesto'),
    'Almidon de maiz': (2.10, 'kg', 'supuesto'),
    'Leche en polvo desnatada': (6.40, 'kg', 'supuesto'),
    'Cacao en polvo desgrasado': (11.50, 'kg', 'supuesto'),
    'Sal': (0.90, 'kg', 'supuesto'),
    'Vainilla en pasta': (140.00, 'kg', 'supuesto'),
}

#: Que cobertura sirve el precio de cada entrada «Cobertura *» de `PRECIOS_COMPRA`.
COBERTURA_DE_INGREDIENTE = {
    'Cobertura negra': 'negra',
    'Cobertura de origen': 'origen',
    'Cobertura con leche': 'leche',
    'Cobertura blanca': 'blanca',
}


def precio_compra(ingrediente):
    """(precio sin IVA, unidad de compra, fuente). Las coberturas no guardan su
    precio aqui: lo sirve `COBERTURAS`, que es la celda unica."""
    precio, unidad, fuente = PRECIOS_COMPRA[ingrediente]
    if precio is None:
        precio = precio_cobertura_base_imponible(COBERTURA_DE_INGREDIENTE[ingrediente])
    return precio, unidad, fuente


# ==========================================================================
# 6. LOS RELLENOS: formula por kilo, actividad de agua y familia de vida util
# ==========================================================================
#: Formulas de EJEMPLO, declaradas. NO son recetas con pretension de exactitud y
#: este producto NO es un recetario: el bonus «recetario de bombones con curvas de
#: templado» se DESCARTO a proposito (§2.7), porque una curva mal publicada arruina
#: produccion. Lo que hacen estas formulas es dar al libro 4 algo que costear.
#:
#: `aw` es SUPUESTO en las doce: la actividad de agua se MIDE, y por eso en el libro
#: 5 es celda verde con valor por defecto. `familia_kit` apunta a la fila de la tabla
#: de vida util que el kit ya publica (`VIDA_UTIL_KIT`): la guia la CITA, no la
#: reescribe (D30).
RELLENOS = {
    'ganache negra fresca': {
        'nombre': 'Ganache de chocolate negro con nata fresca',
        'lineas': [('Nata 35 % MG fresca', 0.40), ('Cobertura negra', 0.52),
                   ('Mantequilla', 0.06), ('Glucosa', 0.04)],
        'aw': 0.88, 'fuente_aw': 'supuesto',
        'familia_kit': 'Bombones de ganache con nata fresca',
        'nota': ('La ganache que obliga a decidir el modelo de negocio: agua '
                 'disponible alta, y el kit le da 10-15 dias. Es la que manda en la '
                 'decision 3 del bonus 2.')},
    'ganache leche estabilizada': {
        'nombre': 'Ganache de chocolate con leche, nata UHT y sorbitol',
        'lineas': [('Nata 35 % MG UHT', 0.34), ('Cobertura con leche', 0.56),
                   ('Sorbitol', 0.06), ('Mantequilla', 0.05)],
        'aw': 0.82, 'fuente_aw': 'supuesto',
        'familia_kit': 'Bombones de ganache con nata UHT, sorbato o alcohol',
        'nota': ('La misma pieza con otra formulacion: el kit le da 4-8 semanas. '
                 'Entre esta y la anterior hay un factor DE TRES A CINCO, y esa es '
                 'una decision de modelo de negocio, no tecnica.')},
    'praline avellana': {
        'nombre': 'Praline de avellana',
        'lineas': [('Praline de avellana 50 %', 0.70), ('Cobertura con leche', 0.28),
                   ('Manteca de cacao', 0.04)],
        'aw': 0.42, 'fuente_aw': 'supuesto',
        'familia_kit': 'Bombones de praline, gianduja y frutos secos',
        'nota': ('«Praline» NO es un nombre comercial: el punto 10 de la parte A del '
                 'Anexo I de la Directiva 2000/36/CE se titula «Bombon de chocolate '
                 'o praline» (`CHN-82`), con el mismo minimo del 25 %.')},
    'gianduja avellana': {
        'nombre': 'Gianduja de avellana',
        'lineas': [('Pasta pura de avellana', 0.45), ('Cobertura con leche', 0.40),
                   ('Azucar', 0.17)],
        'aw': 0.38, 'fuente_aw': 'supuesto',
        'familia_kit': 'Bombones de praline, gianduja y frutos secos',
        'nota': ('La gianduja tiene su propio apartado en la norma (1.6.b.3), con '
                 'avellanas entre 20 y 40 g por 100 g. Aqui es RELLENO de un bombon, '
                 'asi que la denominacion de venta es la del bombon.')},
    'trufa': {
        'nombre': 'Trufa de chocolate negro',
        'lineas': [('Nata 35 % MG UHT', 0.36), ('Cobertura negra', 0.54),
                   ('Mantequilla', 0.06), ('Glucosa', 0.04)],
        'aw': 0.80, 'fuente_aw': 'supuesto',
        'familia_kit': 'Trufas y rocas recubiertas',
        'nota': ('«Trufa» no aparece ni una vez en el RD 1055/2003 (`CHN-03b`): es un '
                 'TIPO de bombon, no una categoria legal ni un sinonimo de bombon.')},
    'licor': {
        'nombre': 'Licor cristalizado de ron',
        'lineas': [('Ron anejo', 0.22), ('Azucar', 0.72), ('Glucosa', 0.06)],
        'aw': 0.72, 'fuente_aw': 'supuesto',
        'familia_kit': 'Bombones de licor y cristalizados',
        'nota': ('El alcohol baja la actividad de agua. Vigilar la cristalizacion del '
                 'azucar en la cascara: revienta y gotea (nota literal del kit).')},
    'caramelo salado': {
        'nombre': 'Caramelo salado',
        'lineas': [('Azucar', 0.36), ('Nata 35 % MG UHT', 0.28), ('Mantequilla', 0.22),
                   ('Glucosa', 0.16), ('Sal', 0.008)],
        'aw': 0.68, 'fuente_aw': 'supuesto',
        'familia_kit': 'Bombones de ganache con nata UHT, sorbato o alcohol',
        'nota': 'Azucar alto y agua baja: aguanta mas que una ganache fresca.'},
    'praline cacahuete': {
        'nombre': 'Praline de cacahuete',
        'lineas': [('Praline de cacahuete 50 %', 0.72), ('Cobertura con leche', 0.26),
                   ('Manteca de cacao', 0.04)],
        'aw': 0.40, 'fuente_aw': 'supuesto',
        'familia_kit': 'Bombones de praline, gianduja y frutos secos',
        'nota': ('EL CACAHUETE ES EL PUNTO 5 DEL ANEXO II y NO es un fruto de '
                 'cascara (`CHN-34b`): esta referencia se etiqueta con su propio '
                 'alergeno, no dentro de «frutos secos».')},
    'crujiente sesamo': {
        'nombre': 'Crujiente de sesamo y barquillo',
        'lineas': [('Pasta de sesamo', 0.34), ('Barquillo triturado', 0.22),
                   ('Cobertura con leche', 0.44)],
        'aw': 0.28, 'fuente_aw': 'supuesto',
        'familia_kit': 'Barquillos y crujientes banados',
        'nota': ('DOS alergenos independientes en una sola pieza: granos de sesamo '
                 '(punto 11) y cereales con gluten del barquillo (punto 1). El kit '
                 'le da 3-4 semanas, y no por seguridad: pierde el crujiente mucho '
                 'antes.')},
    'naranja confitada': {
        'nombre': 'Naranja confitada',
        'lineas': [('Naranja confitada', 0.62), ('Cobertura negra', 0.38)],
        'aw': 0.65, 'fuente_aw': 'supuesto',
        'familia_kit': 'Frutos secos garrapinados y frutas confitadas banadas',
        'nota': ('La fruta confitada suele llevar SULFITOS (punto 12 del Anexo II), '
                 'que es el octavo alergeno y el que mas se olvida. Pidele a tu '
                 'proveedor la ficha tecnica: el umbral de declaracion es 10 mg/kg.')},
    'praline de tableta': {
        'nombre': 'Praline de avellana para tableta rellena',
        'lineas': [('Praline de avellana 50 %', 0.80), ('Cobertura con leche', 0.22)],
        'aw': 0.40, 'fuente_aw': 'supuesto',
        'familia_kit': 'Bombones de praline, gianduja y frutos secos',
        'nota': ('En una TABLETA RELLENA la denominacion es «chocolate relleno» '
                 '(ap. 1.10) y el exterior tiene que ser al menos el 25 % del peso '
                 'total (`CHN-04`), calculado SOBRE EL PESO TOTAL con el relleno '
                 'dentro (`CHN-10`).')},
    'masa a la taza': {
        'nombre': 'Masa de chocolate a la taza (azucar, cacao desgrasado y almidon)',
        'lineas': [('Azucar', 0.62), ('Cacao en polvo desgrasado', 0.30),
                   ('Almidon de maiz', 0.08)],
        'aw': 0.25, 'fuente_aw': 'supuesto',
        'familia_kit': 'Tabletas y chocolate sin relleno',
        'nota': ('NO es un relleno: es la otra mitad de la formula del chocolate a la '
                 'taza, que NO se hace solo con cobertura. Va aqui para que el '
                 'escandallo pueda costearla. El almidon es DE MAIZ a proposito: la '
                 'norma admite trigo, arroz o maiz hasta el 8 %, y con el de trigo '
                 'habria que declarar gluten.')},
    'yema tostada': {
        'nombre': 'Yema tostada',
        'lineas': [('Yema de huevo pasteurizada', 0.40), ('Azucar', 0.56),
                   ('Almidon de maiz', 0.05)],
        'aw': 0.85, 'fuente_aw': 'supuesto',
        'familia_kit': 'Bombones de ganache con nata fresca',
        'nota': ('La UNICA referencia del surtido con huevo, y va con ovoproducto '
                 'pasteurizado de establecimiento autorizado, que es la tercera via '
                 'del art. 9 del RD 1021/2022 (`CHN-31`). Con huevo crudo habria que '
                 'llegar a 70 grados C durante 2 s en el centro.')},
}


def coste_relleno_kg(clave):
    """Coste de materia de un kilo de relleno, en base imponible."""
    total = 0.0
    for ing, cantidad in RELLENOS[clave]['lineas']:
        precio, _ud, _f = precio_compra(ing)
        total += cantidad * precio
    return total


# ==========================================================================
# 7. VIDA UTIL: LA TABLA ES DEL KIT Y LA GUIA LA CITA (D30)
# ==========================================================================
#: COPIA DECLARADA de `02-partidas-produccion.xlsx!Moldeado`, tabla al pie titulada
#: «VIDA UTIL Y CONSERVACION ORIENTATIVAS A 15-18 grados C Y 50-60 % DE HUMEDAD -
#: ajustala a tu formula y a tu obrador». Diez filas, leidas una a una el 12-09-2026.
#:
#: LA GUIA NO REESCRIBE ESTA TABLA. Lo que construye el libro 5 es lo que el kit NO
#: tiene: actividad de agua por tipo de relleno, vida util DECLARADA POR TI (celda
#: verde, NUNCA calculada), lote economico y merma por caducidad en euros/ano.
#:
#: REGLA DURA (`CHN-30`): la vida util la declara el operador en su plan de APPCC.
#: El libro nunca la calcula ni la presenta como norma.
VIDA_UTIL_KIT = [
    # (familia literal del kit, plazo literal del kit, nota literal del kit)
    ('Tabletas y chocolate sin relleno', '12-18 meses',
     'El enemigo no es el tiempo: es la humedad, la luz y los olores. Sellado y en oscuridad'),
    ('Figuras huecas y piezas macizas', '6-12 meses',
     'Igual que la tableta, pero la pieza hueca se raja con los cambios bruscos de temperatura'),
    ('Bombones de ganache con nata fresca', '10-15 dias',
     'Actividad de agua alta: en refrigeracion a 0-4 grados C y atemperar CERRADOS '
     'antes de abrir, o condensan'),
    ('Bombones de ganache con nata UHT, sorbato o alcohol', '4-8 semanas',
     'El conservante y el alcohol bajan la actividad de agua; sin ellos no se llega '
     'ni a la mitad'),
    ('Bombones de praline, gianduja y frutos secos', '2-4 meses',
     'La grasa del fruto seco se enrancia y el frio no lo evita: manda la fecha, no el aspecto'),
    ('Trufas y rocas recubiertas', '3-4 semanas',
     'Si llevan nata o mantequilla, se cuentan como ganache fresca'),
    ('Bombones de licor y cristalizados', '3-6 meses',
     'Vigilar la cristalizacion del azucar en la cascara: revienta y gotea'),
    ('Frutos secos garrapinados y frutas confitadas banadas', '1-3 meses',
     'Se apelmazan con la humedad; envasado hermetico con desecante si tu obrador es humedo'),
    ('Barquillos y crujientes banados', '3-4 semanas',
     'Pierden el crujiente mucho antes que la seguridad: se retiran por calidad'),
    ('Chocolate acabado: NO congelar', 'Nunca',
     'Al descongelar condensa, el agua disuelve el azucar de la superficie y deja '
     'sugar bloom. Solo el granel de ganache admite -18 grados C 1-2 meses, '
     'descongelado 24 h en camara y sin abrir'),
]
FUENTE_VIDA_UTIL = F_KIT_MOLDEADO
NOTA_VIDA_UTIL = (
    'Tabla del KIT, citada por fichero y hoja, NO reescrita (D30). `CHS-56` («maximo '
    '8 dias» sin sorbitol y «5 o 6 semanas» con el) deja de ser la fuente de los '
    'plazos y pasa a ser la cita de oficio que explica POR QUE: el agua disponible '
    'de la ganache. Y el titular no es «factor 5»: con los plazos del kit, de 10-15 '  # LN-OK
    'dias a 4-8 semanas es 3,7 veces en el peor caso y 5,6 en el mejor, asi que la '
    'frase publicable es «entre la ganache fresca y la estabilizada hay un factor de '
    'tres a cinco, y esa es una decision de modelo de negocio, no tecnica».')

#: La vida util que el lector DECLARA. Vale `None` a proposito: es celda verde y la
#: fija el operador en su APPCC (`CHN-30`). El libro 5 NUNCA la calcula.
VIDA_UTIL_DECLARADA = None


# ==========================================================================
# 8. LOS OCHO ALERGENOS DE UNA BOMBONERIA (`CHN-34b`)
# ==========================================================================
#: SON OCHO, NO CINCO. Cacahuetes (punto 5), frutos de cascara (punto 8) y granos de
#: sesamo (punto 11) son entradas INDEPENDIENTES del Anexo II del Rgto. 1169/2011, y
#: falta ademas el sulfito (punto 12). Escribir «los cinco alergenos de una  # LN-OK
#: bomboneria» esta PROHIBIDO (§5.1, prohibicion 11).  # LN-OK
#:
#: NOTA-PUENTE para quien ya tiene el kit de 12 euros (D53c): «si usas el Kit de
#: Tareas Chocolateria, desglosa la celda "frutos secos" en cacahuetes, frutos de
#: cascara y sesamo, que son entradas independientes del Anexo II». El kit publica
#: hoy seis, seis y cinco en sus tres celdas de declaracion; su regeneracion a 2.1
#: es una PROPUESTA para John y NO bloquea nada de aqui.
ALERGENOS = (
    ('leche', 'Leche y sus derivados (incluida la lactosa)', 7),
    ('huevos', 'Huevos y productos a base de huevo', 3),
    ('gluten', 'Cereales que contengan gluten y productos derivados', 1),
    ('soja', 'Soja y productos a base de soja', 6),
    ('cacahuetes', 'Cacahuetes y productos a base de cacahuetes', 5),
    ('frutos_cascara', 'Frutos de cascara (almendra, avellana, nuez, anacardo...)', 8),
    ('sesamo', 'Granos de sesamo y productos a base de granos de sesamo', 11),
    ('sulfitos', 'Dioxido de azufre y sulfitos en concentraciones superiores a 10 mg/kg', 12),
)
ALERGENOS_CLAVES = tuple(a[0] for a in ALERGENOS)
FUENTE_ALERGENOS = 'CHN-34b'
NOTA_ALERGENOS = (
    'La lecitina de SOJA esta en casi todas las coberturas industriales, asi que la '
    'columna «soja» se marca por defecto en todo lo que lleve cobertura de marca: '
    'comprueba la ficha tecnica de la tuya antes de quitarla. Los alergenos pueden '
    'ir en cartel en producto sin envasar, pero la fecha no (`CHN-89`), y el equipo '
    'usado con un alergeno no se reutiliza sin limpiar (`CHN-33`).')


# ==========================================================================
# 9. LA CARTA DE APERTURA: 28 referencias en 5 familias (D52)
# ==========================================================================
#: El NUMERO de referencias (28) es supuesto declarado. Lo que NO es supuesto es la
#: columna de denominacion legal, que sale del RD 1055/2003 verificado el 12-09-2026,
#: ni la de alergenos, que sale del Anexo II del Rgto. 1169/2011.
FAMILIAS = ('Bombones de coleccion', 'Tabletas', 'Chocolate a la taza',
            'Turrones, figuras y temporada', 'Cajas y regalo')

#: Cuantas referencias tiene cada familia (§3.2).
FAMILIAS_ESPERADO = {'Bombones de coleccion': 10, 'Tabletas': 6,
                     'Chocolate a la taza': 3, 'Turrones, figuras y temporada': 5,
                     'Cajas y regalo': 4}

#: Las dos vias de D47. NO son el mismo regimen y la salida del libro 5 cambia de
#: columna en cada una.
VIAS_DESPACHO = ('envasado con etiqueta', 'a granel')
VIAS_DESPACHO_TEXTO = {
    'envasado con etiqueta': (
        'Sale envasado con SU etiqueta. El art. 4.2 del RD 1021/2022 fija la '
        'temperatura de conservacion POR LA ETIQUETA que pone quien ha producido y '
        'envasado: la que tu has escrito te obliga a ti. Y con etiqueta entran '
        'ademas las doce menciones del art. 9.1 del Rgto. 1169/2011 (`CHN-35`) mas '
        'el lote, que NO viene de ese reglamento sino del RD 1808/1991 (`CHN-36`).'),
    'a granel': (
        'Se despacha a granel en la vitrina, sin etiqueta. Entonces la referencia NO '
        'es el art. 4.2: es TU sistema de autocontrol, y la temperatura y la vida '
        'util las declaras tu y constan en el (`CHN-30`, y `CHN-87`: «chocolate», '
        '«cacao», «bombon» y «confiteria» aparecen 0 veces en todo el RD 1021/2022). '
        'Los alergenos pueden ir en cartel (`CHN-89`) y el lote tiene tres vias de '
        'exencion (`CHN-36`).'),
}
FUENTE_VIAS_DESPACHO = 'CHN-30 + CHN-35 + CHN-36 + CHN-87 + CHN-89'

#: Claves de cada referencia:
#:   id · nombre · familia · denominacion_legal · fuente_denominacion · minimo_legal
#:   · mencion_cacao (`CHN-07`) · via (D47) · relleno (clave de `RELLENOS` o None)
#:   · cobertura (clave de `COBERTURAS`) · g_chocolate · g_relleno · piezas_molde
#:   · moldes_tanda · minutos_mo_tanda · merma_recuperable_pct · merma_no_recuperable_pct
#:   · pvp_con_iva · iva · mix_pct · mix_verano_pct · alergenos · familia_vida_util
#:   · fuente_pvp · fuente_gramaje · nota
#:
#: `g_chocolate` y `g_relleno` son los gramos POR PIEZA VENDIBLE, y su suma es el
#: peso total: con esos dos numeros el libro 4 calcula solo el 25 % del ap. 1.13
#: SOBRE EL PESO TOTAL, relleno incluido (capa (a) de D37, `CHN-10`). Escribir que
#: ese 25 % se calcula descontando el relleno esta PROHIBIDO: da un resultado mas
#: favorable que el legal y deja pasar por el semaforo una referencia que no cumple.
#:
#: DOS tasas de merma por referencia (D40, y la regla es del kit): el chocolate SIN
#: relleno y sin contaminar se refunde y vuelve a la cuba (`merma_recuperable_pct`);
#: el que lleva ganache o fruta va a residuo (`merma_no_recuperable_pct`).
def _al(*presentes):
    """Fila de la matriz de alergenos: los que NO se nombran van a False."""
    fila = dict((k, False) for k in ALERGENOS_CLAVES)
    for k in presentes:
        if k not in fila:
            raise KeyError('Alergeno desconocido: %r' % k)
        fila[k] = True
    return fila


CARTA = [
    # --------------------- BOMBONES DE COLECCION (10) ---------------------
    {'id': 'BC1', 'nombre': 'Bombon de ganache de chocolate negro 70 %',
     'familia': 'Bombones de coleccion',
     'denominacion_legal': 'Bombon de chocolate',
     'fuente_denominacion': 'CHN-03', 'minimo_legal': '25 % de chocolate sobre el peso TOTAL',
     'mencion_cacao': False, 'via': 'a granel',
     'relleno': 'ganache negra fresca', 'cobertura': 'negra',
     'g_chocolate': 5.5, 'g_relleno': 6.5,
     'piezas_molde': 24, 'moldes_tanda': 6, 'minutos_mo_tanda': 155,
     'merma_recuperable_pct': 0.04, 'merma_no_recuperable_pct': 0.03,
     'pvp_con_iva': 2.00, 'iva': 0.10, 'mix_pct': 6.0, 'mix_verano_pct': 2.0,
     'alergenos': _al('leche', 'soja'), 'familia_vida_util': 'Bombones de ganache con nata fresca',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('La referencia que mas margen deja y la que antes caduca. Con 5,5 g de '
              'chocolate sobre 12 g de pieza, el chocolate es el 45,8 % del peso '
              'total: cumple el 25 % del ap. 1.13 con holgura. En julio y agosto baja '
              'a un tercio de su mix: es la primera que sale del catalogo de verano '
              '(literal del kit para junio: «menos ganache fresca»).')},
    {'id': 'BC2', 'nombre': 'Bombon de ganache de leche y vainilla',
     'familia': 'Bombones de coleccion',
     'denominacion_legal': 'Bombon de chocolate',
     'fuente_denominacion': 'CHN-03', 'minimo_legal': '25 % de chocolate sobre el peso TOTAL',
     'mencion_cacao': False, 'via': 'a granel',
     'relleno': 'ganache leche estabilizada', 'cobertura': 'leche',
     'g_chocolate': 5.5, 'g_relleno': 6.5,
     'piezas_molde': 24, 'moldes_tanda': 6, 'minutos_mo_tanda': 155,
     'merma_recuperable_pct': 0.04, 'merma_no_recuperable_pct': 0.03,
     'pvp_con_iva': 1.95, 'iva': 0.10, 'mix_pct': 5.0, 'mix_verano_pct': 4.0,
     'alergenos': _al('leche', 'soja'),
     'familia_vida_util': 'Bombones de ganache con nata UHT, sorbato o alcohol',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('Misma pieza que BC1 con otra formulacion: nata UHT y sorbitol. El kit '
              'le da 4-8 semanas frente a los 10-15 dias de BC1. Es LA decision de '
              'modelo de negocio del producto, y el libro 5 la cuantifica en euros de '
              'merma por caducidad al ano.')},
    {'id': 'BC3', 'nombre': 'Bombon de praline de avellana',
     'familia': 'Bombones de coleccion',
     'denominacion_legal': 'Bombon de chocolate (praline)',
     'fuente_denominacion': 'CHN-03 + CHN-82',
     'minimo_legal': '25 % de chocolate sobre el peso TOTAL',
     'mencion_cacao': False, 'via': 'a granel',
     'relleno': 'praline avellana', 'cobertura': 'leche',
     'g_chocolate': 5.0, 'g_relleno': 7.0,
     'piezas_molde': 24, 'moldes_tanda': 6, 'minutos_mo_tanda': 140,
     'merma_recuperable_pct': 0.04, 'merma_no_recuperable_pct': 0.02,
     'pvp_con_iva': 2.10, 'iva': 0.10, 'mix_pct': 6.0, 'mix_verano_pct': 5.0,
     'alergenos': _al('leche', 'soja', 'frutos_cascara'),
     'familia_vida_util': 'Bombones de praline, gianduja y frutos secos',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('«Praline» SI significa algo legalmente: es la denominacion de venta '
              'europea del bombon de chocolate (`CHN-82`), con el mismo minimo del '
              '25 %. Escribir lo contrario esta prohibido (§5.1, prohibicion 7).')},
    {'id': 'BC4', 'nombre': 'Bombon de gianduja de avellana',
     'familia': 'Bombones de coleccion',
     'denominacion_legal': 'Bombon de chocolate',
     'fuente_denominacion': 'CHN-03', 'minimo_legal': '25 % de chocolate sobre el peso TOTAL',
     'mencion_cacao': False, 'via': 'a granel',
     'relleno': 'gianduja avellana', 'cobertura': 'leche',
     'g_chocolate': 5.0, 'g_relleno': 7.0,
     'piezas_molde': 24, 'moldes_tanda': 5, 'minutos_mo_tanda': 130,
     'merma_recuperable_pct': 0.04, 'merma_no_recuperable_pct': 0.02,
     'pvp_con_iva': 2.10, 'iva': 0.10, 'mix_pct': 4.0, 'mix_verano_pct': 3.0,
     'alergenos': _al('leche', 'soja', 'frutos_cascara'),
     'familia_vida_util': 'Bombones de praline, gianduja y frutos secos',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('La gianduja tiene apartado propio en la norma (1.6.b.3), pero aqui va '
              'DENTRO de un bombon: la denominacion de venta que manda es la del '
              'producto que vendes, no la del relleno.')},
    {'id': 'BC5', 'nombre': 'Trufa de chocolate negro al cacao',
     'familia': 'Bombones de coleccion',
     'denominacion_legal': 'Bombon de chocolate',
     'fuente_denominacion': 'CHN-03 + CHN-03b',
     'minimo_legal': '25 % de chocolate sobre el peso TOTAL',
     'mencion_cacao': False, 'via': 'a granel',
     'relleno': 'trufa', 'cobertura': 'negra',
     'g_chocolate': 4.0, 'g_relleno': 9.0,
     'piezas_molde': 40, 'moldes_tanda': 4, 'minutos_mo_tanda': 120,
     'merma_recuperable_pct': 0.03, 'merma_no_recuperable_pct': 0.04,
     'pvp_con_iva': 1.90, 'iva': 0.10, 'mix_pct': 5.0, 'mix_verano_pct': 2.0,
     'alergenos': _al('leche', 'soja'), 'familia_vida_util': 'Trufas y rocas recubiertas',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('Aqui el 25 % se pelea: 4 g de chocolate sobre 13 g de pieza son el '
              '30,8 %, y bajando el bano un gramo se cae por debajo del minimo legal. '
              'Es el ejemplo con el que el semaforo del libro 4 ensena para que sirve. '
              '«Trufa» no es una categoria legal espanola (`CHN-03b`).')},
    {'id': 'BC6', 'nombre': 'Bombon de licor de ron',
     'familia': 'Bombones de coleccion',
     'denominacion_legal': 'Bombon de chocolate',
     'fuente_denominacion': 'CHN-03', 'minimo_legal': '25 % de chocolate sobre el peso TOTAL',
     'mencion_cacao': False, 'via': 'a granel',
     'relleno': 'licor', 'cobertura': 'negra',
     'g_chocolate': 6.0, 'g_relleno': 8.0,
     'piezas_molde': 24, 'moldes_tanda': 4, 'minutos_mo_tanda': 145,
     'merma_recuperable_pct': 0.05, 'merma_no_recuperable_pct': 0.04,
     'pvp_con_iva': 2.30, 'iva': 0.10, 'mix_pct': 3.0, 'mix_verano_pct': 3.0,
     'alergenos': _al('soja'), 'familia_vida_util': 'Bombones de licor y cristalizados',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('Cascara mas gruesa (6 g) porque el licor la ataca. La unica del '
              'surtido sin leche: si la vendes a granel al lado de las demas, la '
              'contaminacion cruzada en la pinza se come esa ventaja.')},
    {'id': 'BC7', 'nombre': 'Bombon de caramelo salado',
     'familia': 'Bombones de coleccion',
     'denominacion_legal': 'Bombon de chocolate',
     'fuente_denominacion': 'CHN-03', 'minimo_legal': '25 % de chocolate sobre el peso TOTAL',
     'mencion_cacao': False, 'via': 'a granel',
     'relleno': 'caramelo salado', 'cobertura': 'leche',
     'g_chocolate': 5.5, 'g_relleno': 6.5,
     'piezas_molde': 24, 'moldes_tanda': 6, 'minutos_mo_tanda': 150,
     'merma_recuperable_pct': 0.04, 'merma_no_recuperable_pct': 0.03,
     'pvp_con_iva': 2.00, 'iva': 0.10, 'mix_pct': 4.0, 'mix_verano_pct': 2.0,
     'alergenos': _al('leche', 'soja'),
     'familia_vida_util': 'Bombones de ganache con nata UHT, sorbato o alcohol',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': 'Azucar alto y agua baja: aguanta mucho mas que una ganache fresca.'},
    {'id': 'BC8', 'nombre': 'Bombon de praline de cacahuete',
     'familia': 'Bombones de coleccion',
     'denominacion_legal': 'Bombon de chocolate (praline)',
     'fuente_denominacion': 'CHN-03 + CHN-82',
     'minimo_legal': '25 % de chocolate sobre el peso TOTAL',
     'mencion_cacao': False, 'via': 'a granel',
     'relleno': 'praline cacahuete', 'cobertura': 'leche',
     'g_chocolate': 5.0, 'g_relleno': 7.0,
     'piezas_molde': 24, 'moldes_tanda': 5, 'minutos_mo_tanda': 135,
     'merma_recuperable_pct': 0.04, 'merma_no_recuperable_pct': 0.02,
     'pvp_con_iva': 1.95, 'iva': 0.10, 'mix_pct': 3.0, 'mix_verano_pct': 3.0,
     'alergenos': _al('leche', 'soja', 'cacahuetes'),
     'familia_vida_util': 'Bombones de praline, gianduja y frutos secos',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('LA REFERENCIA QUE DEMUESTRA POR QUE SON OCHO Y NO CINCO: el cacahuete '
              'es el punto 5 del Anexo II y NO es un fruto de cascara (punto 8). '
              'Meterlo dentro de «frutos secos» es un error de etiquetado que puede '
              'mandar a alguien al hospital.')},
    {'id': 'BC9', 'nombre': 'Bombon crujiente de sesamo y barquillo',
     'familia': 'Bombones de coleccion',
     'denominacion_legal': 'Bombon de chocolate',
     'fuente_denominacion': 'CHN-03', 'minimo_legal': '25 % de chocolate sobre el peso TOTAL',
     'mencion_cacao': False, 'via': 'a granel',
     'relleno': 'crujiente sesamo', 'cobertura': 'leche',
     'g_chocolate': 5.0, 'g_relleno': 7.0,
     'piezas_molde': 24, 'moldes_tanda': 5, 'minutos_mo_tanda': 140,
     'merma_recuperable_pct': 0.04, 'merma_no_recuperable_pct': 0.02,
     'pvp_con_iva': 2.05, 'iva': 0.10, 'mix_pct': 3.0, 'mix_verano_pct': 3.0,
     'alergenos': _al('leche', 'soja', 'gluten', 'sesamo'),
     'familia_vida_util': 'Barquillos y crujientes banados',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('Dos alergenos mas que sus companeras, y los dos independientes: '
              'granos de sesamo (punto 11) y cereales con gluten del barquillo '
              '(punto 1). El kit le da 3-4 semanas, y no por seguridad: pierde el '
              'crujiente mucho antes.')},
    {'id': 'BC10', 'nombre': 'Bombon de naranja confitada y chocolate negro',
     'familia': 'Bombones de coleccion',
     'denominacion_legal': 'Bombon de chocolate',
     'fuente_denominacion': 'CHN-03', 'minimo_legal': '25 % de chocolate sobre el peso TOTAL',
     'mencion_cacao': False, 'via': 'a granel',
     'relleno': 'naranja confitada', 'cobertura': 'negra',
     'g_chocolate': 5.5, 'g_relleno': 6.5,
     'piezas_molde': 24, 'moldes_tanda': 5, 'minutos_mo_tanda': 145,
     'merma_recuperable_pct': 0.03, 'merma_no_recuperable_pct': 0.05,
     'pvp_con_iva': 2.05, 'iva': 0.10, 'mix_pct': 3.0, 'mix_verano_pct': 3.0,
     'alergenos': _al('soja', 'sulfitos'),
     'familia_vida_util': 'Frutos secos garrapinados y frutas confitadas banadas',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('La unica del surtido con SULFITOS, que es el octavo alergeno y el que '
              'mas se olvida: la fruta confitada suele llevarlos y el umbral de '
              'declaracion es de 10 mg/kg. La fruta ademas contamina el recorte: su '
              'merma NO recuperable es la mas alta de la carta (D40).')},

    # ------------------------------ TABLETAS (6) --------------------------
    {'id': 'TB1', 'nombre': 'Tableta de chocolate negro de origen 70 %, 100 g',
     'familia': 'Tabletas',
     'denominacion_legal': 'Chocolate',
     'fuente_denominacion': 'CHN-02 + CHN-13',
     'minimo_legal': 'ap. 1.6: minimos calculados DESCONTANDO los ingredientes anadidos del ap. 3',
     'mencion_cacao': True, 'via': 'envasado con etiqueta',
     'relleno': None, 'cobertura': 'origen',
     'g_chocolate': 100.0, 'g_relleno': 0.0,
     'piezas_molde': 3, 'moldes_tanda': 10, 'minutos_mo_tanda': 55,
     'merma_recuperable_pct': 0.06, 'merma_no_recuperable_pct': 0.01,
     'pvp_con_iva': 8.50, 'iva': 0.10, 'mix_pct': 7.0, 'mix_verano_pct': 11.0,
     'alergenos': _al('soja'), 'familia_vida_util': 'Tabletas y chocolate sin relleno',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('La referencia que vende el posicionamiento: cobertura de origen a '
              '37,48 euros/kg (`CHS-28c`) frente a los 25,02 de la de marca '
              '(`CHS-28a`), factor 1,5. Lleva la mencion «cacao: X % minimo» '
              'obligatoria (`CHN-07`) y es la que mas sube en verano: no lleva agua, '
              'aguanta 12-18 meses y viaja. Y es la referencia con el food cost '
              'MAS ALTO de la carta, con diferencia: comprar cobertura de origen y '
              'ponerle precio de cobertura de marca es como se regala el trabajo. El '
              'libro 3 lo ensena con el escenario de subida del cacao.')},
    {'id': 'TB2', 'nombre': 'Tableta de chocolate con leche 38 %, 100 g',
     'familia': 'Tabletas',
     'denominacion_legal': 'Chocolate con leche',
     'fuente_denominacion': 'CHN-02 + CHN-13',
     'minimo_legal': 'ap. 1.7: minimos calculados DESCONTANDO los ingredientes anadidos del ap. 3',
     'mencion_cacao': True, 'via': 'envasado con etiqueta',
     'relleno': None, 'cobertura': 'leche',
     'g_chocolate': 100.0, 'g_relleno': 0.0,
     'piezas_molde': 3, 'moldes_tanda': 10, 'minutos_mo_tanda': 55,
     'merma_recuperable_pct': 0.06, 'merma_no_recuperable_pct': 0.01,
     'pvp_con_iva': 5.90, 'iva': 0.10, 'mix_pct': 6.0, 'mix_verano_pct': 9.0,
     'alergenos': _al('leche', 'soja'), 'familia_vida_util': 'Tabletas y chocolate sin relleno',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': 'Tambien lleva la mencion «cacao: X % minimo» (`CHN-07`).'},
    {'id': 'TB3', 'nombre': 'Tableta de chocolate blanco 30 %, 100 g',
     'familia': 'Tabletas',
     'denominacion_legal': 'Chocolate blanco',
     'fuente_denominacion': 'CHN-02 + CHN-13',
     'minimo_legal': 'ap. 1.9: 20 % de manteca, 14 % de materia seca lactea, 3,5 % de grasa lactea',
     'mencion_cacao': False, 'via': 'envasado con etiqueta',
     'relleno': None, 'cobertura': 'blanca',
     'g_chocolate': 100.0, 'g_relleno': 0.0,
     'piezas_molde': 3, 'moldes_tanda': 8, 'minutos_mo_tanda': 55,
     'merma_recuperable_pct': 0.07, 'merma_no_recuperable_pct': 0.01,
     'pvp_con_iva': 5.90, 'iva': 0.10, 'mix_pct': 4.0, 'mix_verano_pct': 6.0,
     'alergenos': _al('leche', 'soja'), 'familia_vida_util': 'Tabletas y chocolate sin relleno',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('El chocolate blanco NO lleva la mencion «cacao: X % minimo»: '
              '`CHN-07` acota esa obligacion a los apartados 1.4, 1.5, 1.6, 1.7, '
              '1.8, 1.11 y 1.12, y el blanco es el 1.9. Escribir que la mencion es '
              'obligatoria en todos los chocolates esta prohibido (§5.1, 27).')},
    {'id': 'TB4', 'nombre': 'Tableta de chocolate negro con almendra marcona, 100 g',
     'familia': 'Tabletas',
     'denominacion_legal': 'Chocolate con almendras',
     'fuente_denominacion': 'CHN-02 + CHN-09 + CHN-13',
     'minimo_legal': ('ap. 1.6 con materias comestibles anadidas del ap. 3: no pueden '
                      'exceder el 40 % del peso total del producto acabado'),
     'mencion_cacao': True, 'via': 'envasado con etiqueta',
     'relleno': None, 'cobertura': 'negra',
     'g_chocolate': 78.0, 'g_relleno': 22.0,
     'piezas_molde': 3, 'moldes_tanda': 8, 'minutos_mo_tanda': 65,
     'merma_recuperable_pct': 0.05, 'merma_no_recuperable_pct': 0.02,
     'pvp_con_iva': 6.50, 'iva': 0.10, 'mix_pct': 5.0, 'mix_verano_pct': 8.0,
     'alergenos': _al('soja', 'frutos_cascara'),
     'familia_vida_util': 'Tabletas y chocolate sin relleno',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('La almendra va en `g_relleno` porque es materia comestible ANADIDA del '
              'ap. 3, y su tope es el 40 % del peso total (`CHN-09`). Con 22 g sobre '
              '100 esta en el 22 %: dentro. La almendra enrancia, y el frio no lo '
              'evita: manda la fecha, no el aspecto (nota del kit).')},
    {'id': 'TB5', 'nombre': 'Tableta de chocolate con leche y avellana, 100 g',
     'familia': 'Tabletas',
     'denominacion_legal': 'Chocolate con leche y avellanas',
     'fuente_denominacion': 'CHN-02 + CHN-09 + CHN-13',
     'minimo_legal': 'ap. 1.7 con materias comestibles anadidas del ap. 3 (tope 40 %)',
     'mencion_cacao': True, 'via': 'envasado con etiqueta',
     'relleno': None, 'cobertura': 'leche',
     'g_chocolate': 80.0, 'g_relleno': 20.0,
     'piezas_molde': 3, 'moldes_tanda': 8, 'minutos_mo_tanda': 65,
     'merma_recuperable_pct': 0.05, 'merma_no_recuperable_pct': 0.02,
     'pvp_con_iva': 6.50, 'iva': 0.10, 'mix_pct': 4.0, 'mix_verano_pct': 6.0,
     'alergenos': _al('leche', 'soja', 'frutos_cascara'),
     'familia_vida_util': 'Tabletas y chocolate sin relleno',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': 'La avellana va como materia anadida del ap. 3, igual que la almendra de TB4.'},
    {'id': 'TB6', 'nombre': 'Tableta rellena de praline, 100 g',
     'familia': 'Tabletas',
     'denominacion_legal': 'Chocolate relleno',
     'fuente_denominacion': 'CHN-04 + CHN-10 + CHN-13',
     'minimo_legal': ('ap. 1.10: el exterior de chocolate tiene que ser al menos el '
                      '25 % del peso TOTAL del producto acabado, relleno incluido'),
     'mencion_cacao': False, 'via': 'envasado con etiqueta',
     'relleno': 'praline de tableta', 'cobertura': 'leche',
     'g_chocolate': 55.0, 'g_relleno': 45.0,
     'piezas_molde': 3, 'moldes_tanda': 6, 'minutos_mo_tanda': 105,
     'merma_recuperable_pct': 0.05, 'merma_no_recuperable_pct': 0.03,
     'pvp_con_iva': 7.50, 'iva': 0.10, 'mix_pct': 3.0, 'mix_verano_pct': 4.0,
     'alergenos': _al('leche', 'soja', 'frutos_cascara'),
     'familia_vida_util': 'Bombones de praline, gianduja y frutos secos',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('La segunda referencia del ap. 1.10, y la que ensena la base de calculo: '
              '55 g de chocolate sobre 100 g de pieza son el 55 %, calculado SOBRE EL '
              'PESO TOTAL con el relleno dentro (`CHN-10`). Si alguien lo calculase '
              'descontando el relleno le saldria el 100 % y el semaforo dejaria pasar '
              'cualquier cosa: por eso invertir las dos bases esta prohibido. Y NO es '
              'chocolate relleno lo que lleva interior de panaderia, pasteleria, '
              'galleteria, bolleria o helado (`CHN-04`).')},

    # ------------------------- CHOCOLATE A LA TAZA (3) --------------------
    {'id': 'CT1', 'nombre': 'Tableta de chocolate a la taza, 200 g',
     'familia': 'Chocolate a la taza',
     'denominacion_legal': 'Chocolate a la taza',
     'fuente_denominacion': 'CHN-05',
     'minimo_legal': ('ap. 1.11: 35 % de materia seca total de cacao, 18 % de manteca, '
                      '14 % de desgrasada y hasta 8 % de harina o almidon de trigo, '
                      'arroz o maiz'),
     'mencion_cacao': True, 'via': 'envasado con etiqueta',
     'relleno': 'masa a la taza', 'cobertura': 'negra',
     'g_chocolate': 80.0, 'g_relleno': 120.0,
     'piezas_molde': 2, 'moldes_tanda': 8, 'minutos_mo_tanda': 70,
     'merma_recuperable_pct': 0.05, 'merma_no_recuperable_pct': 0.01,
     'pvp_con_iva': 6.50, 'iva': 0.10, 'mix_pct': 3.0, 'mix_verano_pct': 1.0,
     'alergenos': _al('soja'), 'familia_vida_util': 'Tabletas y chocolate sin relleno',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('El almidon (9,6 g sobre 200, el 4,8 %) esta por debajo del tope del 8 %. '
              'Se usa ALMIDON DE MAIZ a proposito: con almidon de TRIGO habria que '
              'declarar gluten, y la norma admite los tres. La etiqueta lleva ademas '
              'la expresion «para su consumo cocido» (ap. 6.e): es una ADICION '
              'ESPANOLA que NO existe en la Directiva 2000/36/CE (`CHN-83`), asi que '
              'no se escribe que sea un requisito europeo.')},
    {'id': 'CT2', 'nombre': 'Caja de 6 sobres monodosis de chocolate a la taza',
     'familia': 'Chocolate a la taza',
     'denominacion_legal': 'Chocolate a la taza',
     'fuente_denominacion': 'CHN-05',
     'minimo_legal': 'ap. 1.11: 35 % cacao total, 18 % manteca, 14 % desgrasada, almidon hasta 8 %',
     'mencion_cacao': True, 'via': 'envasado con etiqueta',
     'relleno': 'masa a la taza', 'cobertura': 'negra',
     'g_chocolate': 72.0, 'g_relleno': 108.0,
     'piezas_molde': 6, 'moldes_tanda': 6, 'minutos_mo_tanda': 95,
     'merma_recuperable_pct': 0.05, 'merma_no_recuperable_pct': 0.01,
     'pvp_con_iva': 7.80, 'iva': 0.10, 'mix_pct': 2.0, 'mix_verano_pct': 0.5,
     'alergenos': _al('soja'), 'familia_vida_util': 'Tabletas y chocolate sin relleno',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('Seis sobres de 30 g. Ojo al art. 2.2.c) del RD 1808/1991: los envases '
              'cuya cara mayor mide menos de 10 cm2 estan exentos de lote, pero la '
              'CAJA que los contiene no (`CHN-36`).')},
    {'id': 'CT3', 'nombre': 'Chocolate a la taza servido en sala, 200 ml',
     'familia': 'Chocolate a la taza',
     'denominacion_legal': 'Chocolate a la taza',
     'fuente_denominacion': 'CHN-05',
     'minimo_legal': 'ap. 1.11 sobre el producto que sirves, no sobre la taza preparada',
     'mencion_cacao': False, 'via': 'a granel',
     'relleno': 'masa a la taza', 'cobertura': 'negra',
     'g_chocolate': 18.0, 'g_relleno': 27.0,
     'piezas_molde': 1, 'moldes_tanda': 1, 'minutos_mo_tanda': 3,
     'merma_recuperable_pct': 0.0, 'merma_no_recuperable_pct': 0.06,
     'pvp_con_iva': 3.20, 'iva': 0.10, 'mix_pct': 3.0, 'mix_verano_pct': 0.5,
     'alergenos': _al('soja'), 'familia_vida_util': 'Tabletas y chocolate sin relleno',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('Aqui NO entregas un bien: prestas un servicio de hosteleria, y el IVA '
              'va al 10 % por el art. 91.Uno.2.2.o (`CHN-71c`). No lleva etiqueta, '
              'asi que su referencia es tu sistema de autocontrol (D47). Y si pones '
              'mesas, el art. 8 de la Ley 1/2025 te obliga a facilitar que el cliente '
              'se lleve lo que no ha consumido, aunque seas microempresa: la '
              'exclusion del art. 6.6 NO alcanza al art. 8 (`CHN-92`). Es la pieza '
              'que sube el ticket del churro un 40-60 % en la variante de taza '
              '(`CHS-32`), y es OTRO negocio (D1).')},

    # --------------------- TURRONES, FIGURAS Y TEMPORADA (5) --------------
    {'id': 'TF1', 'nombre': 'Huevo de Pascua de chocolate con leche, 250 g',
     'familia': 'Turrones, figuras y temporada',
     'denominacion_legal': 'Chocolate con leche',
     'fuente_denominacion': 'CHN-02 + CHN-13',
     'minimo_legal': 'ap. 1.7: minimos descontando los ingredientes anadidos del ap. 3',
     'mencion_cacao': True, 'via': 'envasado con etiqueta',
     'relleno': None, 'cobertura': 'leche',
     'g_chocolate': 250.0, 'g_relleno': 0.0,
     'piezas_molde': 2, 'moldes_tanda': 6, 'minutos_mo_tanda': 150,
     'merma_recuperable_pct': 0.09, 'merma_no_recuperable_pct': 0.02,
     'pvp_con_iva': 18.50, 'iva': 0.10, 'mix_pct': 2.0, 'mix_verano_pct': 0.0,
     'alergenos': _al('leche', 'soja'),
     'familia_vida_util': 'Figuras huecas y piezas macizas',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('La merma recuperable mas alta del catalogo: la pieza hueca se raja con '
              'los cambios bruscos de temperatura (nota del kit) y lo que se rompe '
              'SIN relleno vuelve entero a la cuba. Cero mix en verano: es de '
              'campana.')},
    {'id': 'TF2', 'nombre': 'Mona de Pascua de chocolate, 400 g',
     'familia': 'Turrones, figuras y temporada',
     'denominacion_legal': 'Chocolate con leche',
     'fuente_denominacion': 'CHN-02 + CHN-13',
     'minimo_legal': 'ap. 1.7 con materias comestibles anadidas del ap. 3 (tope 40 %)',
     'mencion_cacao': True, 'via': 'envasado con etiqueta',
     'relleno': None, 'cobertura': 'leche',
     'g_chocolate': 380.0, 'g_relleno': 20.0,
     'piezas_molde': 1, 'moldes_tanda': 6, 'minutos_mo_tanda': 210,
     'merma_recuperable_pct': 0.09, 'merma_no_recuperable_pct': 0.02,
     'pvp_con_iva': 26.00, 'iva': 0.10, 'mix_pct': 1.5, 'mix_verano_pct': 0.0,
     'alergenos': _al('leche', 'soja'),
     'familia_vida_util': 'Figuras huecas y piezas macizas',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('Pieza de autor y la que mas minutos de obrador se lleva: 210 por tanda '
              'de seis. La decoracion va como materia anadida del ap. 3. Es la '
              'referencia que pone a prueba la capacidad del libro 1 en abril.')},
    {'id': 'TF3', 'nombre': 'Hueso de santo banado en chocolate',
     'familia': 'Turrones, figuras y temporada',
     'denominacion_legal': 'Producto de confiteria recubierto de chocolate',
     'fuente_denominacion': 'CHN-15',
     'minimo_legal': ('RD 348/2011: si el producto esta relleno, recubierto o '
                      'grageado, la denominacion de venta tiene que decirlo'),
     'mencion_cacao': False, 'via': 'a granel',
     'relleno': 'yema tostada', 'cobertura': 'negra',
     'g_chocolate': 9.0, 'g_relleno': 21.0,
     'piezas_molde': 30, 'moldes_tanda': 4, 'minutos_mo_tanda': 170,
     'merma_recuperable_pct': 0.02, 'merma_no_recuperable_pct': 0.06,
     'pvp_con_iva': 1.60, 'iva': 0.10, 'mix_pct': 1.0, 'mix_verano_pct': 0.0,
     'alergenos': _al('huevos', 'soja'),
     'familia_vida_util': 'Bombones de ganache con nata fresca',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('LA REFERENCIA QUE ROMPE LA REGLA, y por eso esta aqui: 9 g de '
              'chocolate sobre 30 g de pieza son el 30 %, pero NO es un bombon de '
              'chocolate, porque el 1.13 pide una pieza «del tamano de un bocado '
              'constituida por chocolate», y esto es un producto de confiteria '
              'RECUBIERTO. Su denominacion sale del RD 348/2011 (`CHN-15`), no del '
              'RD 1055/2003. La UNICA con huevo, por la yema, y va con ovoproducto '
              'pasteurizado (`CHN-31`). Esta literalmente en el calendario del kit: '
              '«Todos los Santos (1): panellets y huesos de santo banados».')},
    {'id': 'TF4', 'nombre': 'Turron de chocolate con almendra, 250 g',
     'familia': 'Turrones, figuras y temporada',
     'denominacion_legal': 'Chocolate con almendras',
     'fuente_denominacion': 'CHN-02 + CHN-09 + CHN-13',
     'minimo_legal': 'ap. 1.6 con materias comestibles anadidas del ap. 3 (tope 40 %)',
     'mencion_cacao': True, 'via': 'envasado con etiqueta',
     'relleno': None, 'cobertura': 'negra',
     'g_chocolate': 168.0, 'g_relleno': 82.0,
     'piezas_molde': 4, 'moldes_tanda': 6, 'minutos_mo_tanda': 120,
     'merma_recuperable_pct': 0.05, 'merma_no_recuperable_pct': 0.02,
     'pvp_con_iva': 13.50, 'iva': 0.10, 'mix_pct': 2.0, 'mix_verano_pct': 1.0,
     'alergenos': _al('soja', 'frutos_cascara'),
     'familia_vida_util': 'Tabletas y chocolate sin relleno',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('HUECO DECLARADO: la denominacion que publica este juego de datos es la '
              'del RD 1055/2003, porque la norma de calidad de TURRONES no se abrio '
              'en la verificacion legal del 12-09-2026 y ninguna ficha `CHN-*` la '
              'cubre. «Turron de chocolate con almendra» es el NOMBRE COMERCIAL; '
              'antes de imprimir la etiqueta hay que comprobar si la norma de '
              'turrones te obliga a otra denominacion de venta. La almendra (82 g '
              'sobre 250, el 32,8 %) esta dentro del tope del 40 % del ap. 3 '
              '(`CHN-09`).')},
    {'id': 'TF5', 'nombre': 'Almendras marcona banadas en chocolate, bolsa de 150 g',
     'familia': 'Turrones, figuras y temporada',
     'denominacion_legal': 'Grageas o confites de chocolate',
     'fuente_denominacion': 'CHN-15',
     'minimo_legal': ('RD 348/2011, ap. 1.3: la denominacion de venta se complementa '
                      'con «relleno», «recubierto» o «grageado» segun el caso'),
     'mencion_cacao': False, 'via': 'envasado con etiqueta',
     'relleno': None, 'cobertura': 'negra',
     'g_chocolate': 88.0, 'g_relleno': 62.0,
     'piezas_molde': 40, 'moldes_tanda': 1, 'minutos_mo_tanda': 95,
     'merma_recuperable_pct': 0.04, 'merma_no_recuperable_pct': 0.02,
     'pvp_con_iva': 7.40, 'iva': 0.10, 'mix_pct': 3.5, 'mix_verano_pct': 8.0,
     'alergenos': _al('soja', 'frutos_cascara'),
     'familia_vida_util': 'Frutos secos garrapinados y frutas confitadas banadas',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('La que da nombre a la casa, y su denominacion NO sale del RD 1055/2003 '
              'sino del RD 348/2011: «grageas o confites de chocolate» (`CHN-15`). Se '
              'hace en bombo, no en molde: `moldes_tanda` vale 1 y los 95 minutos '
              'son de la tanda entera, de la que salen 40 bolsas. Es la segunda que mas sube en '
              'verano: no lleva agua y es souvenir (literal del kit para julio: '
              '«packs souvenir y colaboraciones locales»).')},

    # --------------------------- CAJAS Y REGALO (4) -----------------------
    {'id': 'CJ1', 'nombre': 'Caja surtida de 12 bombones',
     'familia': 'Cajas y regalo',
     'denominacion_legal': 'Chocolates rellenos surtidos',
     'fuente_denominacion': 'CHN-13',
     'minimo_legal': ('ap. 6.a) y 6.c): la denominacion va por pieza o, si el surtido '
                      'es de los aps. 1.6 a 1.10 y 1.13, se sustituye por la de '
                      'surtido, con una unica lista de ingredientes. Es una DECISION '
                      'de etiquetado, no una obligacion'),
     'mencion_cacao': False, 'via': 'envasado con etiqueta',
     'relleno': None, 'cobertura': 'negra',
     'g_chocolate': 0.0, 'g_relleno': 0.0,
     'piezas_molde': 1, 'moldes_tanda': 1, 'minutos_mo_tanda': 4,
     'merma_recuperable_pct': 0.0, 'merma_no_recuperable_pct': 0.005,
     'pvp_con_iva': 20.00, 'iva': 0.10, 'mix_pct': 5.0, 'mix_verano_pct': 7.0,
     'alergenos': _al('leche', 'soja', 'gluten', 'cacahuetes', 'frutos_cascara',
                      'sesamo', 'sulfitos'),
     'familia_vida_util': 'Bombones de ganache con nata UHT, sorbato o alcohol',
     'fuente_pvp': 'CHS-29', 'fuente_gramaje': 'supuesto',
     'nota': ('PVP de `CHS-29`, precio de MOSTRADOR (con IVA) y base de IVA NO '
              'declarada por la fuente: entra con su columna «lleva IVA» y el libro 4 '
              'publica el PVP base por formula, porque el libro 7 pide el ticket medio '
              'SIN IVA. 12 unidades a 20,00 euros son 1,67 euros por bombon. Su coste '
              'de materia NO se teclea: se COMPONE de las referencias que lleva '
              'dentro (`composicion_caja`), y por eso `g_chocolate` vale 0. Los siete '
              'alergenos son la UNION de lo que va dentro: en un surtido a granel no '
              'puedes prometer que una pinza no ha tocado otra cosa.'),
     'composicion_caja': [('BC1', 2), ('BC2', 2), ('BC3', 2), ('BC5', 1),
                          ('BC7', 2), ('BC8', 1), ('BC9', 1), ('BC10', 1)],
     'uds_caja': 12},
    {'id': 'CJ2', 'nombre': 'Caja surtida de 20 bombones',
     'familia': 'Cajas y regalo',
     'denominacion_legal': 'Chocolates rellenos surtidos',
     'fuente_denominacion': 'CHN-13',
     'minimo_legal': 'ap. 6.a) y 6.c), igual que CJ1',
     'mencion_cacao': False, 'via': 'envasado con etiqueta',
     'relleno': None, 'cobertura': 'negra',
     'g_chocolate': 0.0, 'g_relleno': 0.0,
     'piezas_molde': 1, 'moldes_tanda': 1, 'minutos_mo_tanda': 6,
     'merma_recuperable_pct': 0.0, 'merma_no_recuperable_pct': 0.005,
     'pvp_con_iva': 28.00, 'iva': 0.10, 'mix_pct': 3.0, 'mix_verano_pct': 5.0,
     'alergenos': _al('leche', 'soja', 'gluten', 'cacahuetes', 'frutos_cascara',
                      'sesamo', 'sulfitos'),
     'familia_vida_util': 'Bombones de ganache con nata UHT, sorbato o alcohol',
     'fuente_pvp': 'CHS-29', 'fuente_gramaje': 'supuesto',
     'nota': '1,40 euros por bombon: un 16 % menos que en la caja de 12.',
     'composicion_caja': [('BC1', 3), ('BC2', 3), ('BC3', 3), ('BC4', 2), ('BC5', 3),
                          ('BC6', 1), ('BC7', 2), ('BC8', 1), ('BC9', 1), ('BC10', 1)],
     'uds_caja': 20},
    {'id': 'CJ3', 'nombre': 'Caja surtida de 35 bombones',
     'familia': 'Cajas y regalo',
     'denominacion_legal': 'Chocolates rellenos surtidos',
     'fuente_denominacion': 'CHN-13',
     'minimo_legal': 'ap. 6.a) y 6.c), igual que CJ1',
     'mencion_cacao': False, 'via': 'envasado con etiqueta',
     'relleno': None, 'cobertura': 'negra',
     'g_chocolate': 0.0, 'g_relleno': 0.0,
     'piezas_molde': 1, 'moldes_tanda': 1, 'minutos_mo_tanda': 9,
     'merma_recuperable_pct': 0.0, 'merma_no_recuperable_pct': 0.005,
     'pvp_con_iva': 45.00, 'iva': 0.10, 'mix_pct': 2.0, 'mix_verano_pct': 2.0,
     'alergenos': _al('leche', 'soja', 'gluten', 'cacahuetes', 'frutos_cascara',
                      'sesamo', 'sulfitos'),
     'familia_vida_util': 'Bombones de ganache con nata UHT, sorbato o alcohol',
     'fuente_pvp': 'CHS-29', 'fuente_gramaje': 'supuesto',
     'nota': ('1,29 euros por bombon: un 23 % menos que en la caja de 12. Esa escalera '
              'es la decision 4 del bonus 2, y el libro 4 la resuelve comparando el '
              'precio de la caja con la suma de sus unidades sueltas.'),
     'composicion_caja': [('BC1', 5), ('BC2', 5), ('BC3', 5), ('BC4', 3), ('BC5', 4),
                          ('BC6', 2), ('BC7', 4), ('BC8', 3), ('BC9', 2), ('BC10', 2)],
     'uds_caja': 35},
    {'id': 'CJ4', 'nombre': 'Estuche corporativo personalizado de 24 bombones',
     'familia': 'Cajas y regalo',
     'denominacion_legal': 'Chocolates rellenos surtidos',
     'fuente_denominacion': 'CHN-13',
     'minimo_legal': 'ap. 6.a) y 6.c), igual que CJ1',
     'mencion_cacao': False, 'via': 'envasado con etiqueta',
     'relleno': None, 'cobertura': 'negra',
     'g_chocolate': 0.0, 'g_relleno': 0.0,
     'piezas_molde': 1, 'moldes_tanda': 1, 'minutos_mo_tanda': 11,
     'merma_recuperable_pct': 0.0, 'merma_no_recuperable_pct': 0.005,
     'pvp_con_iva': 34.00, 'iva': 0.10, 'mix_pct': 1.0, 'mix_verano_pct': 1.0,
     'alergenos': _al('leche', 'soja', 'gluten', 'cacahuetes', 'frutos_cascara',
                      'sesamo', 'sulfitos'),
     'familia_vida_util': 'Bombones de ganache con nata UHT, sorbato o alcohol',
     'fuente_pvp': 'supuesto', 'fuente_gramaje': 'supuesto',
     'nota': ('SUPUESTO: `CHS-29` no cubre el estuche corporativo. Lo que SI esta '
              'verificado es su regla operativa: 14 dias de plazo minimo desde la '
              'aprobacion de la muestra (`CHS-55`), que es lo que decide si aceptas '
              'un pedido de empresa en diciembre. Y es el canal que te saca de la '
              'nota del epigrafe 644.5 y te mete en la tabla de CLIENTES del art. '
              '5.3.b) del EUDR (`CHN-24`, D48).'),
     'composicion_caja': [('BC1', 3), ('BC2', 3), ('BC3', 4), ('BC4', 2), ('BC5', 3),
                          ('BC6', 1), ('BC7', 3), ('BC8', 2), ('BC9', 2), ('BC10', 1)],
     'uds_caja': 24},
]


# ==========================================================================
# 10. FUNCIONES DERIVADAS DE LA CARTA
# ==========================================================================
def ref(rid):
    """La referencia con ese id."""
    for r in CARTA:
        if r['id'] == rid:
            return r
    raise KeyError('Referencia desconocida: %r' % rid)


def por_familia(familia):
    return [r for r in CARTA if r['familia'] == familia]


def es_caja(r):
    return 'composicion_caja' in r


def peso_total_g(r):
    """Peso de la pieza vendible. Para una caja, la suma de lo que lleva dentro."""
    if es_caja(r):
        return sum(ref(i)['g_chocolate'] + ref(i)['g_relleno'] * 1.0
                   for i, n in r['composicion_caja'] for _ in range(n))
    return r['g_chocolate'] + r['g_relleno']


def pct_chocolate_sobre_peso_total(r):
    """CAPA (a) DE D37, la que SI se calcula con el escandallo: el porcentaje de
    chocolate SOBRE EL PESO TOTAL del producto acabado, RELLENO INCLUIDO
    (`CHN-10`, apartado 4, cita literal). Es la base de los apartados 1.10
    (chocolate relleno) y 1.13 (bombon).

    Invertirla -calcularla descontando el relleno- da un resultado MAS FAVORABLE
    que el legal y deja pasar por el semaforo una referencia que no cumple. Esta
    PROHIBIDO, y es una de las cuatro prohibiciones que anadio esta SPEC.
    """
    if es_caja(r):
        num = sum(ref(i)['g_chocolate'] * n for i, n in r['composicion_caja'])
        den = sum((ref(i)['g_chocolate'] + ref(i)['g_relleno']) * n
                  for i, n in r['composicion_caja'])
        return 100.0 * num / den if den else 0.0
    total = r['g_chocolate'] + r['g_relleno']
    return 100.0 * r['g_chocolate'] / total if total else 0.0


#: Las referencias a las que la norma exige el 25 % sobre el peso total: las del
#: apartado 1.13 (bombon) y las del 1.10 (chocolate relleno).
MINIMO_25_PCT = 25.0
FUENTE_MINIMO_25 = 'CHN-03 + CHN-04 + CHN-10'


def exige_25_pct(r):
    """True si a esa referencia le aplica el minimo del 25 % de los aps. 1.10/1.13."""
    d = r['denominacion_legal']
    return d.startswith('Bombon de chocolate') or d == 'Chocolate relleno' \
        or d == 'Chocolates rellenos surtidos'


def coste_materia_unidad(r):
    """Coste de materia de una pieza vendible, en base imponible y SIN merma.
    Una caja se COMPONE de sus referencias: no tiene escandallo propio."""
    if es_caja(r):
        return sum(coste_materia_unidad(ref(i)) * n for i, n in r['composicion_caja'])
    precio_cob = precio_cobertura_base_imponible(r['cobertura'])
    coste = (r['g_chocolate'] / 1000.0) * precio_cob
    if r['relleno']:
        coste += (r['g_relleno'] / 1000.0) * coste_relleno_kg(r['relleno'])
    elif r['g_relleno']:
        # Materias comestibles anadidas del ap. 3 (almendra, avellana, almidon).
        coste += (r['g_relleno'] / 1000.0) * _precio_anadido(r)
    return coste


#: Que materia comestible anadida del ap. 3 lleva cada referencia sin relleno.
ANADIDOS = {
    'TB4': 'Almendra marcona repelada',
    'TB5': 'Avellana tostada',
    'TF2': 'Almendra marcona repelada',
    'TF4': 'Almendra marcona repelada',
    'TF5': 'Almendra marcona repelada',
}


def _precio_anadido(r):
    return precio_compra(ANADIDOS[r['id']])[0]


def coste_materia_con_merma(r):
    """D40, DOS TASAS. La regla es del kit (`02!Moldeado`): «El chocolate sin relleno
    y sin contaminar se puede refundir; el que lleva ganache o fruta, a residuo».

    · La merma RECUPERABLE vuelve a la cuba, asi que NO es coste: lo unico que
      cuesta es volver a templarla, y eso lo cobra la mano de obra.
    · La merma NO RECUPERABLE va a residuo y SI es coste: se reparte entre las
      piezas buenas.
    """
    base = coste_materia_unidad(r)
    return base / (1.0 - r['merma_no_recuperable_pct'])


def coste_hora_obrador():
    """Coste de una hora de obrador: coste empresa de las personas del area OBRADOR
    dividido entre sus horas PRODUCTIVAS. No es el bruto ni el bruto con SS: es lo
    que de verdad cuesta un minuto de templado, y es lo que el libro 4 imputa por
    pieza. Del bruto al coste empresa hay un 33 %, y ese es el salto que mas
    sorprende al lector (cap. 17)."""
    total, horas = 0.0, 0.0
    for pid, _perfil, jornada, grupo, area, _h, _t in PLANTILLA:
        if area != 'OBRADOR':
            continue
        bruto_anual = CONVENIO[grupo - 1][3] * jornada
        total += bruto_anual * (1.0 + P('ss_empresa'))
        horas += P('horas_anuales_contrato') * jornada * P('ratio_horas_productivas')
    return total / horas if horas else 0.0


def piezas_por_tanda(r):
    return r['piezas_molde'] * r['moldes_tanda']


def coste_mano_obra_unidad(r):
    """Minutos de la tanda repartidos entre las piezas BUENAS de la tanda: la merma
    recuperable se vuelve a templar, y ese trabajo lo paga la pieza que sale bien."""
    piezas = piezas_por_tanda(r)
    if not piezas:
        return 0.0
    buenas = piezas * (1.0 - r['merma_no_recuperable_pct'])
    minutos_por_pieza = r['minutos_mo_tanda'] / buenas
    return minutos_por_pieza / 60.0 * coste_hora_obrador()


def pvp_sin_iva(r):
    """El PVP en BASE IMPONIBLE. `CHS-29` publica precios de MOSTRADOR (con IVA) y
    el libro 7 pide el ticket medio SIN IVA: los dos tienen que dar el mismo food
    cost, y solo lo dan si el cociente se calcula con las dos patas en la misma
    base (regla 3 de §2.3)."""
    return r['pvp_con_iva'] / (1.0 + r['iva'])


def coste_total_unidad(r):
    return coste_materia_con_merma(r) + coste_mano_obra_unidad(r)


def food_cost(r):
    """Coste de MATERIA sobre PVP, los dos en base imponible."""
    p = pvp_sin_iva(r)
    return coste_materia_con_merma(r) / p if p else 0.0


def margen_unidad(r):
    return pvp_sin_iva(r) - coste_total_unidad(r)


def pvp_medio_ponderado(verano=False):
    clave = 'mix_verano_pct' if verano else 'mix_pct'
    return sum(r['pvp_con_iva'] * r[clave] for r in CARTA) / 100.0


def ticket_medio_con_iva(verano=False):
    return pvp_medio_ponderado(verano) * P('piezas_por_ticket')


def food_cost_carta(verano=False):
    """Food cost de escandallo de la carta entera, ponderado por euros vendidos."""
    clave = 'mix_verano_pct' if verano else 'mix_pct'
    coste = sum(coste_materia_con_merma(r) * r[clave] for r in CARTA)
    venta = sum(pvp_sin_iva(r) * r[clave] for r in CARTA)
    return coste / venta if venta else 0.0


def food_cost_servido(verano=False):
    """El de arriba mas el packaging. Es el que hay que usar para el punto muerto:
    el de escandallo se queda corto y hace creer que el margen es mayor."""
    return food_cost_carta(verano) * (1.0 + P('packaging_pct_coste'))


def iva_medio_carta():
    """Tipo de IVA medio de la carta, ponderado por euros vendidos con IVA. Hoy son
    todos el 10 % (`CHN-71`): la funcion existe para que el dia que entre una
    referencia con otro tipo, el libro 7 no tenga que tocarse."""
    con_iva = sum(r['pvp_con_iva'] * r['mix_pct'] for r in CARTA)
    sin_iva = sum(pvp_sin_iva(r) * r['mix_pct'] for r in CARTA)
    return con_iva / sin_iva - 1.0 if sin_iva else 0.0


def matriz_alergenos():
    """Las 28 filas x 8 columnas, en el orden de `ALERGENOS`."""
    return [(r['id'], r['nombre'], tuple(r['alergenos'][k] for k in ALERGENOS_CLAVES))
            for r in CARTA]


def referencias_con(alergeno):
    return [r['id'] for r in CARTA if r['alergenos'][alergeno]]


def vida_util_kit_de(familia_literal):
    """El plazo LITERAL del kit para esa familia. La guia lo CITA, no lo reescribe."""
    for fam, plazo, nota in VIDA_UTIL_KIT:
        if fam == familia_literal:
            return plazo, nota, FUENTE_VIDA_UTIL
    raise KeyError('Familia de vida util que no esta en el kit: %r' % familia_literal)


# ==========================================================================
# 11. EQUIPAMIENTO: dotacion tipo linea a linea
# ==========================================================================
#: REGLA DE IVA (§2.3, regla 3): cada linea lleva SU BASE FISCAL en `base_iva`,
#: porque unos distribuidores publican con IVA y otros sin el, y mezclarlos desvia
#: el CAPEX un 21 %. Valores: 'sin IVA' · 'con IVA' · 'no declarada' (el
#: distribuidor no lo dice; se trata como base imponible y SE MARCA, que es lo
#: honesto).
#:
#: `valor_verificado` es el precio con id `CHS-*`; `supuesto_por_defecto` es el
#: valor que se siembra en la celda verde cuando NO hay precio publicado, para que
#: no quede ni una celda verde vacia (regla 2 de §2.3). Nunca estan los dos a la vez.
#:
#: `es_desde` marca los precios que son un SUELO COMERCIAL y no el precio de la
#: unidad concreta (D23b): el mantenedor se publica como «desde 570,00 euros,
#: presupuestar», JAMAS como precio cerrado.
#:
#: `rango_min` / `rango_max` marcan las lineas que solo pueden publicarse como RANGO
#: (D23a): los moldes de policarbonato valen entre 24,20 y 42,83 euros/ud
#: (`CHS-45a`), y 30 euros/ud es un punto elegido sin fuente propia.
#:
#: `plazo_semanas` es SUPUESTO en todas: ningun distribuidor publica plazos. Es la
#: columna que de verdad mueve la fecha de apertura, y por eso viaja al libro 8 por
#: celda verde con fila de cuadre (cruce 8 <- 9 de `CRUCES`).
EQUIPAMIENTO = [
    # --- templado y moldeado (con precio verificado) ----------------------
    {'n': 1, 'partida': 'Atemperadora continua de sobremesa, 12 kg (55 kg/h)',
     'marca': 'Selmi', 'modelo': 'One', 'categoria': 'Templado',
     'valor_verificado': 8500.00, 'supuesto_por_defecto': None,
     'base_iva': 'no declarada', 'tipo_iva': 0.21, 'fuente': 'CHS-41a',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': False, 'plazo_semanas': 10, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipo de templado y moldeado', 'dotacion_tipo': True,
     'nota': ('El corazon del obrador y la decision 2 del bonus 2. Base de IVA NO '
              'declarada: la ficha trae el indicio «/Neto» en la linea de embalaje, '
              'que no es confirmable. La escalera completa va de esta a la Cento EX '
              'de 100 kg (`CHS-41g`), y la eleccion la decide los kg/semana que salga '
              'en la hoja de capacidad del libro 1.')},
    {'n': 2, 'partida': 'Embalaje, transporte y puesta en marcha de la atemperadora',
     'marca': 'Selmi', 'modelo': 'servicio', 'categoria': 'Templado',
     'valor_verificado': 1045.00, 'supuesto_por_defecto': None,
     'base_iva': 'no declarada', 'tipo_iva': 0.21, 'fuente': 'CHS-41a',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': False, 'plazo_semanas': 10, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipo de templado y moldeado', 'dotacion_tipo': True,
     'nota': ('La linea que nadie presupuesta: es el 12 % del precio de la maquina. '
              'La ficha la marca «Neto», que es un INDICIO de base sin IVA, no una '
              'declaracion: por eso va como «no declarada».')},
    {'n': 3, 'partida': 'Enrobadora de banda, 200 mm',
     'marca': 'Selmi', 'modelo': 'R200 Legend', 'categoria': 'Moldeado',
     'valor_verificado': 6800.00, 'supuesto_por_defecto': None,
     'base_iva': 'no declarada', 'tipo_iva': 0.21, 'fuente': 'CHS-42a',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': False, 'plazo_semanas': 10, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipo de templado y moldeado', 'dotacion_tipo': True,
     'nota': 'Base de IVA NO declarada por la ficha del distribuidor.'},
    {'n': 4, 'partida': 'Placa dosificadora de rellenos',
     'marca': 'Selmi', 'modelo': 'placa dosificadora', 'categoria': 'Moldeado',
     'valor_verificado': 1495.00, 'supuesto_por_defecto': None,
     'base_iva': 'no declarada', 'tipo_iva': 0.21, 'fuente': 'CHS-42i',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': False, 'plazo_semanas': 8, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipo de templado y moldeado', 'dotacion_tipo': True,
     'nota': 'Base de IVA NO declarada por la ficha del distribuidor.'},
    {'n': 5, 'partida': 'Temperador de bano maria digital, 22 L',
     'marca': 'Utilcentre', 'modelo': 'bano maria digital 22 L', 'categoria': 'Templado',
     'valor_verificado': 2650.00, 'supuesto_por_defecto': None,
     'base_iva': 'no declarada', 'tipo_iva': 0.21, 'fuente': 'CHS-41j',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': False, 'plazo_semanas': 6, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipo de templado y moldeado', 'dotacion_tipo': True,
     'nota': 'Segunda linea de templado: sin ella no se trabajan dos coberturas a la vez.'},
    {'n': 6, 'partida': 'Mantenedor de 1 cubeta, digital',
     'marca': 'Utilcentre', 'modelo': 'mantenedor 1 cubeta digital', 'categoria': 'Templado',
     'valor_verificado': 570.00, 'supuesto_por_defecto': None,
     'base_iva': 'no declarada', 'tipo_iva': 0.21, 'fuente': 'CHS-41i',
     'es_desde': True, 'rango_min': None, 'rango_max': None,
     'opcional': False, 'plazo_semanas': 5, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipo de templado y moldeado', 'dotacion_tipo': True,
     'nota': ('ES UN «DESDE», NO UN PRECIO (D23b): la ficha publica «desde 570,00 '
              'euros» y eso es un SUELO comercial, no el precio de la unidad que vas '
              'a comprar. Se presupuesta. Publicarlo como precio cerrado esta '
              'prohibido, y el techo del escenario B solo puede subir por su culpa.')},
    {'n': 7, 'partida': 'Atemperadora de arranque, 4,5 L (unos 3 kg)',
     'marca': 'Pavoni', 'modelo': 'MINITEMPER', 'categoria': 'Templado',
     'valor_verificado': 1960.00, 'supuesto_por_defecto': None,
     'base_iva': 'no declarada', 'tipo_iva': 0.21, 'fuente': 'CHS-41h',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': True, 'plazo_semanas': 4, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipo de templado y moldeado', 'dotacion_tipo': False,
     'nota': ('NO esta en la dotacion de La Almendra: es la maquina del ESCENARIO B, '
              'el arranque minimo, y aparece para que el lector vea la escalera. '
              'Cubeta adicional, 165,30 euros (`CHS-41h`).')},
    {'n': 8, 'partida': 'Cubeta adicional para la atemperadora de arranque',
     'marca': 'Pavoni', 'modelo': 'cubeta MINITEMPER', 'categoria': 'Templado',
     'valor_verificado': 165.30, 'supuesto_por_defecto': None,
     'base_iva': 'no declarada', 'tipo_iva': 0.21, 'fuente': 'CHS-41h',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': True, 'plazo_semanas': 4, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Equipo de templado y moldeado', 'dotacion_tipo': False,
     'nota': 'Accesorio del escenario B.'},

    # --- frio -------------------------------------------------------------
    {'n': 9, 'partida': 'Vitrina refrigerada especifica para chocolate',
     'marca': 'Docriluc', 'modelo': 'WB-6-6-R', 'categoria': 'Frio',
     'valor_verificado': 2684.99, 'supuesto_por_defecto': None,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'CHS-43',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': False, 'plazo_semanas': 7, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Frio', 'dotacion_tipo': True,
     'nota': ('600x730x1380 mm. RANGO DE TRABAJO DEL EQUIPO: +14 a +17 grados C, con '
              'base SIN IVA declarada literalmente por la ficha. NO son los +2/+4 '
              'grados C de una vitrina de pasteleria, que arruina el bombon por '
              'condensacion, sugar bloom y perdida de brillo. El OBJETIVO OPERATIVO '
              'es otra cosa y lo pone el kit: 16-18 grados C y menos del 55 % de '
              'humedad. El semaforo del libro 5 solo avisa por encima de 20 grados C, '
              'y queda PROHIBIDO uno que ponga en rojo los 16-18 del propio kit. '
              'Precio de oferta (antes 3.487,00 euros): esta FECHADO el 12-09-2026 y '
              'puede caducar.')},
    {'n': 10, 'partida': 'Camara climatizada de chocolate, unos 6 m2',
     'marca': None, 'modelo': None, 'categoria': 'Frio',
     'valor_verificado': None, 'supuesto_por_defecto': 6400.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': False, 'plazo_semanas': 8, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Frio', 'dotacion_tipo': True,
     'nota': ('SUPUESTO declarado: ninguna fuente del research publica el precio de '
              'una camara de chocolate. Celda verde con valor por defecto. No es una '
              'nevera: trabaja a 15-18 grados C y 50-60 % de humedad, y ese control de '
              'HUMEDAD es lo que la encarece frente a una camara de pasteleria.')},
    {'n': 11, 'partida': 'Nevera de rellenos y ganaches',
     'marca': None, 'modelo': None, 'categoria': 'Frio',
     'valor_verificado': None, 'supuesto_por_defecto': 1450.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': False, 'plazo_semanas': 5, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Frio', 'dotacion_tipo': True,
     'nota': ('SUPUESTO. Es la del RELLENO, a 0-4 grados C, no la del bombon acabado. '
              'Confundirlas es el error de metodo que la SPEC persigue.')},

    # --- packaging y moldes ------------------------------------------------
    {'n': 12, 'partida': 'Moldes de policarbonato para bomboneria (24 unidades)',
     'marca': 'Chocolate World', 'modelo': 'varios (CF0246, CW12064, CW1000L07)',
     'categoria': 'Moldes',
     'valor_verificado': None, 'supuesto_por_defecto': 804.36,
     'base_iva': 'no declarada', 'tipo_iva': 0.21, 'fuente': 'CHS-45a',
     'es_desde': False, 'rango_min': 580.80, 'rango_max': 1027.92,
     'opcional': False, 'plazo_semanas': 4, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Packaging y moldes', 'dotacion_tipo': False,
     'nota': ('SE PUBLICA COMO RANGO (D23a). El unico dato medido es 24,20-42,83 '
              'euros/ud (`CHS-45a`): 24 moldes valen entre 580,80 y 1.027,92 euros. '
              'El valor por defecto (804,36) es el punto medio del rango, y es '
              'SUPUESTO. Escribir una multiplicacion con un precio unitario elegido a '
              'ojo esta prohibido. Y los moldes de policarbonato NO pagan el impuesto '
              'al plastico: no estan sujetos por el art. 73.d) de la Ley 7/2022 '
              '(`CHN-62c`), porque no se entregan junto con la mercancia.')},
    {'n': 13, 'partida': 'Primer pedido de packaging: cajas, estuches, cintas y etiquetas',
     'marca': None, 'modelo': None, 'categoria': 'Packaging',
     'valor_verificado': None, 'supuesto_por_defecto': 2200.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': False, 'plazo_semanas': 5, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Packaging y moldes', 'dotacion_tipo': False,
     'nota': ('SUPUESTO: la web del proveedor de packaging verificado devolvio HTTP '
              '403 y no publica precio (`CHS-54`). En bomboneria la caja ES el '
              'producto en campana, y el personalizado obliga a pedidos grandes: es '
              'dinero parado en el almacen. Si lo compras fuera de Espana, mira el '
              'contador de plastico del libro 2 (`PLASTICO`).')},

    # --- tienda -------------------------------------------------------------
    {'n': 14, 'partida': 'Mobiliario de tienda, mostrador y estanteria',
     'marca': None, 'modelo': None, 'categoria': 'Tienda',
     'valor_verificado': None, 'supuesto_por_defecto': 6900.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': False, 'plazo_semanas': 6, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Mobiliario y tienda', 'dotacion_tipo': True,
     'nota': 'SUPUESTO declarado. Celda verde con valor por defecto.'},
    {'n': 15, 'partida': 'TPV, ordenador, impresora de etiquetas y rotulo',
     'marca': None, 'modelo': None, 'categoria': 'Tienda',
     'valor_verificado': None, 'supuesto_por_defecto': 3200.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': False, 'plazo_semanas': 4, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'TPV, informatica y rotulo', 'dotacion_tipo': True,
     'nota': ('SUPUESTO. La impresora de etiquetas deja de ser opcional en cuanto una '
              'sola referencia sale envasada con etiqueta (D47). Y Verifactu no es '
              '2026, es 2027: 1-ene para sociedades y 1-jul para autonomos '
              '(`CHN-75`).')},
    {'n': 16, 'partida': 'Climatizacion del obrador con deshumidificacion',
     'marca': None, 'modelo': None, 'categoria': 'Clima',
     'valor_verificado': None, 'supuesto_por_defecto': 7600.00,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'supuesto',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': False, 'plazo_semanas': 9, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Climatizacion y deshumidificacion', 'dotacion_tipo': True,
     'nota': ('SUPUESTO declarado, y es la partida que nadie presupuesta. El libro 1 '
              'NO calcula carga termica (D33): no hay un solo coeficiente con fuente '
              'ni de transmitancia, ni por m3, ni de aportes, ni de renovaciones. Lo '
              'que hace es (a) un semaforo de coherencia entre la temperatura '
              'objetivo, la exterior de agosto de TU ciudad y la potencia frigorifica '
              'que te OFREZCA EL INSTALADOR, y (b) una ficha de preguntas para el '
              'instalador. PROHIBIDO el climatizador evaporativo: anade humedad, que '
              'es justo lo contrario de lo que necesita un obrador de chocolate.')},

    # --- variante de taza y churros (D1), fuera de la dotacion tipo --------
    {'n': 17, 'partida': 'Chocolatera de 3 L para la variante de taza',
     'marca': 'Ugolini', 'modelo': 'Delice 3', 'categoria': 'Taza',
     'valor_verificado': 527.00, 'supuesto_por_defecto': None,
     'base_iva': 'sin IVA', 'tipo_iva': 0.21, 'fuente': 'CHS-46a',
     'es_desde': False, 'rango_min': None, 'rango_max': None,
     'opcional': True, 'plazo_semanas': 4, 'fuente_plazo': 'supuesto',
     'bloque_capex': 'Mobiliario y tienda', 'dotacion_tipo': False,
     'nota': ('Base SIN IVA declarada literalmente por la ficha. Solo entra en el '
              'escenario de taza y churros, que es OTRO negocio (D1): la Ley 12/2012 '
              'los separa sola, porque su Anexo incluye el epigrafe 644.5 de bombones '
              'y caramelos y NO contiene ningun grupo de la agrupacion 67, donde esta '
              'la chocolateria de taza (`CHN-49c`).')},
]

#: Subtotal comparable con el escenario publicado: la dotacion tipo de La Almendra,
#: TODA llevada a base imponible. Los opcionales quedan fuera.
def precio_equipamiento_sin_iva(eq):
    """Precio de una linea llevado a base imponible. `base_iva` dice de donde parte:
    sin ese dato el CAPEX sale un 21 % desviado."""
    precio = eq['valor_verificado'] if eq['valor_verificado'] is not None \
        else eq['supuesto_por_defecto']
    if eq['base_iva'] == 'con IVA':
        return precio / (1.0 + eq['tipo_iva'])
    return precio        # 'sin IVA' y 'no declarada' se tratan como base imponible


def dotacion_tipo_sin_iva():
    return sum(precio_equipamiento_sin_iva(e) for e in EQUIPAMIENTO if e['dotacion_tipo'])


def equipamiento_bloque_sin_iva(bloque, incluir_opcionales=False):
    return sum(precio_equipamiento_sin_iva(e) for e in EQUIPAMIENTO
               if e['bloque_capex'] == bloque and (incluir_opcionales or not e['opcional']))


def plazo_critico_semanas():
    """El plazo de entrega mas largo de lo NO opcional. Es el que de verdad mueve la
    fecha de apertura, y por eso viaja al libro 8 (cruce 8 <- 9 de `CRUCES`): si la
    ruta critica del cronograma es mas corta que este plazo, la fecha la manda la
    maquinaria, no el papeleo."""
    return max(e['plazo_semanas'] for e in EQUIPAMIENTO if not e['opcional'])


def equipo_plazo_critico():
    for e in sorted(EQUIPAMIENTO, key=lambda x: -x['plazo_semanas']):
        if not e['opcional']:
            return e
    return None


# --------------------------------------------------------------------------
# Los dos escenarios publicados de DOTACION: RANGO y etiqueta pegada (D23c)
# --------------------------------------------------------------------------
#: NO son presupuestos de apertura y NO se pueden restar ni comparar
#: aritmeticamente: sus lineas tienen bases de IVA distintas (seis con base no
#: declarada, una «sin impuestos» y otra con el indicio «/Neto» no confirmable).
#: La frase publicable es: «el arranque minimo con atemperadora de sobremesa y el
#: profesional con continua se diferencian en un factor 4; cualquier cifra publicada
#: que no diga cual de los dos describe no sirve».
ESCENARIOS_DOTACION = {
    'A': {'nombre': 'Escenario A: profesional de entrada',
          'min': 24000.0, 'max': 24300.0, 'fuente': 'CHS-47a',
          'etiqueta': 'BASE MIXTA de IVA, no es presupuesto de apertura',
          'nota': ('Suma de las lineas con precio verificado: atemperadora Selmi One '
                   '(`CHS-41a`) + puesta en marcha + enrobadora R200 (`CHS-42a`) + '
                   'placa dosificadora (`CHS-42i`) + moldes en RANGO (`CHS-45a`) + '
                   'temperador de bano maria (`CHS-41j`) + mantenedor «desde» '
                   '(`CHS-41i`). Se publica como RANGO porque dos de sus sumandos no '
                   'son numeros cerrados.')},
    'B': {'nombre': 'Escenario B: arranque minimo viable',
          'min': 5700.0, 'max': 5900.0, 'fuente': 'CHS-47b',
          'etiqueta': 'BASE MIXTA de IVA, no es presupuesto de apertura',
          'nota': ('5.670,69 a 5.894,25 euros aplicando a `CHS-47b` (5.740,29) el '
                   'rango de moldes de D23a. El mantenedor es un «desde», asi que el '
                   'techo solo puede subir. El suelo de 5.500 euros que se publico '
                   'primero estaba 170 euros por debajo de lo que produce el propio '
                   'metodo.')},
}
NOTA_ESCENARIOS = (
    'PROHIBIDO restar o comparar aritmeticamente los dos escenarios, y prohibido '
    'presentar cualquiera de los dos totales como cifra fiscal. Lo que SI se conserva '
    'es el hallazgo cualitativo: entre el arranque minimo y el profesional de entrada '
    'hay un factor 4. Y el contraste con los 20.000-30.000 euros de `CHS-03` pierde '
    'la aritmetica y conserva la leccion: una cifra de inversion que no dice cual de '
    'los dos escenarios describe no sirve para decidir nada.')


# ==========================================================================
# 12. CAPEX: NUEVE BLOQUES, y el fondo de maniobra en FILA PROPIA
# ==========================================================================
#: NO son los ocho del molde de Pasteleria calcados: son esos ocho con
#: CLIMATIZACION y TPV/ROTULO en lugar de marketing de apertura, y con el FONDO DE
#: MANIOBRA conservando SU FILA PROPIA. Es de esa fila de donde el «Resumen» del
#: libro 2 saca la linea «Del cual, fondo de maniobra (es caja, no inversion)», y de
#: donde se deriva el «CAPEX sin el fondo» que viaja al libro 7 (cruce 7 <- 2).
#:
#: El fondo NO se calcula aqui con unos meses de colchon propios: llega YA CALCULADO
#: del libro 7 por celda verde con fila de cuadre (cruce 2 <- 7). Si el libro 2 lo
#: calculase por su cuenta, el fondo se calcularia DOS VECES y los dos libros
#: publicarian DOS INVERSIONES TOTALES DISTINTAS con el mismo nombre, que es el
#: defecto ALTO que esta familia ya pago en Pasteleria.
CAPEX = [
    # (bloque, partida, importe, base_iva, tipo_iva, fuente, nota)
    ('Obra y adecuacion', 'Obra y adecuacion del local (75 m2 x 380 euros/m2)',
     28500.0, 'sin IVA', 0.21, 'supuesto',
     'SUPUESTO declarado: ninguna fuente del research publica un coste de obra por m2 '
     'de obrador de chocolate. Es mas barata que la de una pasteleria por un motivo '
     'estructural: un obrador de chocolate NO genera humos, asi que no hay conducto a '
     'cubierta ni la conversacion con la comunidad de propietarios que lo acompana. '
     'Publicar esta cifra como dato verificado esta prohibido (§5.1, 28).'),
    ('Climatizacion y deshumidificacion', 'Climatizacion del obrador con deshumidificacion',
     None, 'sin IVA', 0.21, 'supuesto',
     'Se calcula desde EQUIPAMIENTO: `equipamiento_bloque_sin_iva()`. Bloque propio '
     'porque en chocolate el clima NO es una partida de confort: es la que decide si '
     'la cobertura cristaliza.'),
    ('Equipo de templado y moldeado', 'Tren de templado, moldeado y dosificacion',
     None, 'sin IVA', 0.21, 'CHS-41a + CHS-41i + CHS-41j + CHS-42a + CHS-42i',
     'Se calcula desde EQUIPAMIENTO. Cinco lineas con precio verificado y una que es '
     'un «desde».'),
    ('Frio', 'Camara de chocolate, nevera de rellenos y vitrina',
     None, 'sin IVA', 0.21, 'CHS-43 + supuesto',
     'Se calcula desde EQUIPAMIENTO. Solo la vitrina tiene precio verificado.'),
    ('Mobiliario y tienda', 'Mobiliario de tienda, mostrador y estanteria',
     None, 'sin IVA', 0.21, 'supuesto',
     'Se calcula desde EQUIPAMIENTO.'),
    ('Packaging y moldes', 'Moldes de policarbonato y primer pedido de packaging',
     None, 'sin IVA', 0.21, 'CHS-45a + supuesto',
     'Se calcula desde EQUIPAMIENTO. Los moldes entran como RANGO (D23a) y NO pagan '
     'el impuesto al plastico (`CHN-62c`).'),
    ('TPV, informatica y rotulo', 'TPV, ordenador, impresora de etiquetas y rotulo',
     None, 'sin IVA', 0.21, 'supuesto',
     'Se calcula desde EQUIPAMIENTO.'),
    ('Fianza y licencias', 'Fianza de arrendamiento (2 meses)',
     2600.0, 'sin IVA', 0.00, 'supuesto',
     'La fianza NO es un gasto: es un deposito que se recupera. Va en el CAPEX porque '
     'hay que tenerla el dia de la firma, y por eso no se amortiza.'),
    ('Fianza y licencias', 'Proyecto tecnico visado',
     4500.0, 'sin IVA', 0.21, 'supuesto',
     'SUPUESTO declarado. `CHN-50` (coste de proyecto tecnico) esta en EXCLUIDOS de la '
     'verificacion legal: no hay fuente, y publicar una cifra de proyecto tecnico como '
     'dato verificado esta prohibido (§5.1, 28).'),
    ('Fianza y licencias', 'Tasas municipales',
     1200.0, 'sin IVA', 0.00, 'supuesto',
     'Las tasas municipales no llevan IVA y su importe cambia en cada ayuntamiento: es '
     'el numero que hay que ir a buscar, no copiar. Y ojo: ningun ayuntamiento puede '
     'exigirte LICENCIA PREVIA de instalacion, funcionamiento o actividad hasta 750 m2 '
     'de superficie util de exposicion y venta, porque el epigrafe 644.5 esta en el '
     'Anexo de la Ley 12/2012 (`CHN-49`, `CHN-49b`). Decir que tramite pide Madrid o '
     'Barcelona esta PROHIBIDO: no se ha abierto ninguna ordenanza.'),
    ('Fianza y licencias', 'Comunicacion o declaracion responsable al registro autonomico',
     120.0, 'sin IVA', 0.00, 'CHN-39 + supuesto',
     'NO es una licencia y NO habilita para abrir: es el tramite de informacion del '
     'minorista, que esta EXCLUIDO del RGSEAA (`CHN-39`). El importe es supuesto y en '
     'varias comunidades es gratuito; en la Comunitat Valenciana lleva tasa y es '
     'condicion unica y suficiente para iniciar la actividad, y en Madrid se presenta '
     'simultaneamente al inicio y no habilita (`CHN-43`).'),
    ('Fondo de maniobra', 'Colchon de tesoreria (meses de gastos fijos)',
     None, 'sin IVA', 0.00, 'supuesto',
     'LLEGA YA CALCULADO DEL LIBRO 7 por celda verde con fila de cuadre (cruce 2 <- 7). '
     'El libro 2 NO pide «meses de colchon»: los dos factores del fondo -los meses y '
     'los gastos fijos del ano de crucero- viven en el libro 7. Es caja, no inversion, '
     'y por eso el «Resumen» publica DOS lineas: «CAPEX sin el fondo de maniobra» (la '
     'que viaja al libro 7) y «Del cual, fondo de maniobra».'),
]

#: Bloques COMPARABLES con un escenario de dotacion publicado. Fianza y licencias,
#: packaging y moldes, y fondo de maniobra quedan FUERA, enteros: un deposito, unas
#: existencias y una caja no se comparan contra un presupuesto de obra y equipamiento.
#: El bloque «fianza y licencias» sale ENTERO, no medio: partirlo para rescatar las
#: licencias seria inventar un decimo bloque sin dato propio.
BLOQUES_COMPARABLES = ('Obra y adecuacion', 'Climatizacion y deshumidificacion',
                       'Equipo de templado y moldeado', 'Frio',
                       'Mobiliario y tienda', 'TPV, informatica y rotulo')

BLOQUES_CAPEX = ('Obra y adecuacion', 'Climatizacion y deshumidificacion',
                 'Equipo de templado y moldeado', 'Frio', 'Mobiliario y tienda',
                 'Packaging y moldes', 'TPV, informatica y rotulo',
                 'Fianza y licencias', 'Fondo de maniobra')


# ==========================================================================
# 13. VARIANTES DEL FORMATO (D1 y D2)
# ==========================================================================
#: Las dos variantes NO son productos aparte: son una COLUMNA DE ESCENARIO en el
#: libro 2 y, la de taza y churros, tambien en el P&L del libro 7.
VARIANTES = {
    'bean-to-bar': {
        'nombre': 'Bean-to-bar: del grano a la tableta',
        'lleva_cifras_maquinaria': False,
        'capex_extra': None,
        'fuente': 'CHS-48 + CHS-51',
        'lista_de_la_compra': (
            'Tostador de grano', 'Bandeja de enfriado', 'Descascarilladora',
            'Winnower (aventadora)', 'Melanger o refinadora de piedra',
            'Concha', 'Prensa de manteca (solo si separas manteca)',
            'Tamizadora', 'Balanza de precision para la formulacion',
        ),
        'preguntas_al_proveedor': (
            'Precio de la maquina puesta en Espana, con transporte, aduana y puesta '
            'en marcha desglosados: los catalogos existen y estan verificados, pero '
            'los precios NO son publicos (venta a presupuesto o tienda fuera de la UE).',
            'Plazo de entrega real y quien hace el mantenimiento en Espana.',
            'Potencia electrica y si necesita trifasica.',
            'Ruido en dB a un metro: el tostador y el winnower son los dos equipos '
            'ruidosos de un obrador que por lo demas es silencioso.',
            'Rendimiento en kg de grano por hora y merma de cascarilla.',
        ),
        'nota': ('SIN CIFRAS DE MAQUINARIA A PROPOSITO (D2): no existe precio publico '
                 'verificado del tren bean-to-bar, y lo que se entrega es la lista de '
                 'la compra y las preguntas que hay que hacer. Inventar el precio '
                 'seria justo el patron que la casa prohibe.\n'
                 'Y la variante SUBE DE VALOR por dos motivos legales: (1) si importas '
                 'grano ERES OPERADOR a efectos del EUDR, con diligencia debida '
                 'completa, declaracion presentada previamente y registro cinco anos '
                 '(`CHN-25`), no operador posterior; (2) el TOSTADO te puede meter en '
                 'el CAPCA, y la nota (2) de su Anexo sube de grupo C a B cuando la '
                 'actividad se desarrolla a menos de 500 m de un NUCLEO DE POBLACION '
                 '(`CHN-47b`), es decir, en ciudad SIEMPRE. Ojo: «cacao» y «chocolate» '
                 'tienen 0 ocurrencias en el CAPCA, asi que encajar el tostado de '
                 'cacao en «cafe o similares» es INTERPRETACION, no mencion expresa '
                 '(`CHN-47`).')},
    'taza-y-churros': {
        'nombre': 'Chocolateria de taza y churros',
        'lleva_cifras_maquinaria': True,
        'capex_extra': None,
        'fuente': 'CHS-46a + CHN-48 + CHN-49c',
        'equipos_con_precio': (('Chocolatera Ugolini Delice 3 (3 L)', 527.00, 'CHS-46a',
                                'sin IVA'),),
        'equipos_sin_precio': ('Churrera', 'Freidora', 'Extraccion de humos',
                               'Campana y conducto a cubierta'),
        'obligacion_extra': ('Si hay freidora de gas, inspeccion periodica obligatoria '
                             'de la instalacion receptora CADA CINCO ANOS, que en '
                             'instalaciones de hasta 70 kW incluye los aparatos y '
                             'comprueba la ventilacion y el volumen minimo del local '
                             '(`CHN-48`).'),
        'nota': ('ES OTRO NEGOCIO, y la norma lo separa sola (D1): el Anexo de la Ley '
                 '12/2012 incluye el epigrafe 644.5 «Comercio al por menor de bombones '
                 'y caramelos» y NO contiene ningun grupo de la agrupacion 67, donde '
                 'esta la chocolateria de taza (grupo 676). O sea que la bomboneria se '
                 'libra de la licencia previa hasta 750 m2 y la chocolateria de taza '
                 'no (`CHN-49`, `CHN-49b`, `CHN-49c`).\n'
                 'Lo que SI aporta: el chocolate convierte una racion de churros de '
                 '2,50 euros en 3,50-4 euros, un 40-60 % mas de ticket (`CHS-32`), y '
                 'el margen bruto del churro es del 85-90 % (`CHS-31`) - aunque un '
                 'maestro churrero citado lo rebaja a «un poco mas del 50 %», y los '
                 'dos numeros se publican con su por que, no se elige el mas bonito.\n'
                 'Lo que cuesta: freidora, extraccion de humos y la licencia que la '
                 'bomboneria se ahorra. Los precios de churrera, freidora y extraccion '
                 'NO estan verificados (`CHS-49`).')},
}

#: Traspasos reales de churreria-chocolateria, que son de OTRO formato (D1) y se
#: publican como tales: sirven para dimensionar la variante, no la bomboneria.
TRASPASOS_VARIANTE_TAZA = [
    # (zona, m2, traspaso pedido, renta, fuente)
    ('Elche (Alicante)', 75, None, None, 'CHS-37a'),
    ('Madrid (Vallecas)', 74, 88500.0, 910.0, 'CHS-37b'),
    ('Mataro (Barcelona)', 118, 58000.0, None, 'CHS-37c'),
]


# ==========================================================================
# 14. FRANQUICIA FRENTE A INDEPENDIENTE (D11)
# ==========================================================================
#: ORDEN DE MAGNITUD PUBLICADO, NUNCA DATO AUDITADO, y con su marca, su portal y su
#: fecha dentro. `N-6` prohibe usar cualquier cifra de franquicia como dato auditado
#: y `N-10` prohibe las de Casa Cacao, Lluc Crusellas y la franquicia Valor via
#: infofranquicias. Donde dos lentes se contradicen se publican las dos con su fuente
#: o ninguna: aqui solo hay UNA ficha admitida con id.
FRANQUICIAS = [
    {'marca': 'Chok', 'formato': 'casual bakery + casual chocolate boutique',
     'inversion_desde': 100000.0, 'canon': 30000.0, 'royalty_pct': None,
     'm2_minimos': 55, 'contrato_anios': 5, 'establecimientos': 42,
     'fuente': 'CHS-58', 'fecha_consulta': '12-09-2026',
     'etiqueta': 'orden de magnitud publicado por el portal de franquicias, no dato auditado',
     'nota': ('El local mas pequeno de todo el research: 55 m2. Prueba que el formato '
              'chocolate-boutique cabe donde una pasteleria no. Barcelona, 2012.')},
    {'marca': 'Maestro Churrero', 'formato': 'churreria-chocolateria (variante de taza)',
     'inversion_desde': None, 'canon': None, 'royalty_pct': None,
     'm2_minimos': None, 'contrato_anios': None, 'establecimientos': None,
     'fuente': 'sin id verificado',
     'fecha_consulta': None,
     'etiqueta': 'HUECO DECLARADO: no hay ficha con id en el JSON comun',
     'nota': ('HUECO DELIBERADO. La SPEC menciona esta franquicia en D11 como segunda '
              'ficha admitida, pero al censar el JSON comun el 12-09-2026 NO existe '
              'ninguna entrada `CHS-*` con sus cifras: la unica ficha que la roza es '
              '`CHS-31`, que solo publica el margen bruto del churro. La regla de la '
              'casa es que ninguna cifra con pretension de dato real entra sin id, '
              'asi que aqui va la fila con la marca y SIN numeros. Si alguien quiere '
              'publicarlos, primero hay que crear su ficha con URL y fecha.')},
]
NOTA_FRANQUICIAS = (
    'Canon mas royalty mas compra obligada a central: una franquicia es cuatro o '
    'cinco veces la inversion del formato independiente de `CHS-03`. La columna '
    'existe para que el lector compare, no para recomendar. Y toda cifra va con su '
    'etiqueta: es lo que publica un portal de franquicias, no una cuenta auditada.')


# ==========================================================================
# 15. TRASPASOS: la horquilla real del mercado
# ==========================================================================
#: Son precios PEDIDOS en anuncios, NO precios pagados, y ninguno viene con su
#: cuenta de resultados. Sirven para ver la horquilla y para negociar, no para
#: valorar. El caso mas informativo es `CHS-38a`: 26.000 euros por 90 m2 con obrador
#: equipado y 40 anos de clientela.
TRASPASOS = [
    # (zona, tipo, m2, traspaso pedido, renta mensual, fuente)
    ('El Prat de Llobregat (Barcelona)', 'Pasteleria-bomboneria con obrador (40+ anos)',
     90, 26000.0, 1100.0, 'CHS-38a'),
    ('Reus (Tarragona)', 'Pasteleria-bomboneria historica (34 anos)',
     300, 73000.0, None, 'CHS-38b'),
    ('Barcelona (Sagrada Familia)', 'Pasteleria-bomboneria con obrador a la vista',
     180, 140000.0, 2200.0, 'CHS-38c'),
    ('Valencia (Abastos)', 'Pasteleria con obrador profesional',
     100, 180000.0, None, 'CHS-38d'),
    ("Llica d'Amunt (Barcelona)", 'Obrador de pasteleria y panaderia',
     400, 210000.0, None, 'CHS-38e'),
]
TRASPASO_RANGO = (26000.0, 210000.0, 'CHS-39')
RENTA_OBSERVADA_RANGO = (910.0, 2200.0, 'CHS-37b + CHS-38c')
NOTA_TRASPASOS = (
    'Cinco traspasos de pasteleria-bomboneria leidos el 12-09-2026 en portales de '
    'anuncios (`CHS-38a` a `CHS-38e`), mas los tres de churreria-chocolateria de '
    '`TRASPASOS_VARIANTE_TAZA`, que son de OTRO formato. El rango publicado va de '
    '26.000 a 210.000 euros (`CHS-39`) y la renta observada de 910 a 2.200 euros/mes. '
    'Traspasar puede salir mas barato que montar de cero, y esa es la comparacion a '
    'cinco anos que hace el libro 2. Pero son precios PEDIDOS, no pagados.')


# ==========================================================================
# 16. IMPUESTO AL PLASTICO NO REUTILIZABLE (`CHN-62`, `CHN-62b`, `CHN-62c`)
# ==========================================================================
#: El libro 2 NO explica el impuesto: emite una ALERTA cuando se pasa el umbral, y
#: la explicacion entera vive en el cap. 13. Aqui estan los tres datos que necesita
#: la alerta.
PLASTICO = {
    'tipo_euros_kg': 0.45,
    'fuente_tipo': 'CHN-62',
    'umbral_kg_mes': 5.0,
    'fuente_umbral': 'CHN-62b',
    'kg_mes_ejemplo': 3.2,
    'fuente_kg_mes': 'supuesto',
    'que_grava': ('la fabricacion, la importacion y la adquisicion intracomunitaria '
                  'de envases NO reutilizables que contengan plastico; NO la compra '
                  'en Espana a un proveedor espanol, que ya lo lleva repercutido'),
    'que_exime': ('el art. 75.f) exime la IMPORTACION o ADQUISICION INTRACOMUNITARIA '
                  'que no exceda de 5 kilogramos en un mes, y SOLO de los envases del '
                  'art. 68.1.a): NO exime la fabricacion, NI los semielaborados, NI '
                  'los cierres'),
    'moldes_no_sujetos': True,
    'fuente_moldes': 'CHN-62c',
    'registro_territorial': ('el art. 82.3 obliga a inscribirse en el Registro '
                            'territorial «salvo aquellos que se determine mediante '
                            'Orden»'),
    'nota': ('Los moldes de policarbonato NO pagan: no estan sujetos por el art. 73.d) '
             'porque, pudiendo contener, no estan disenados para entregarse junto con '
             'la mercancia, y ademas el impuesto solo grava envases NO reutilizables '
             '(`CHN-62c`). Estan PROHIBIDAS las dos frases faciles: «el impuesto no te '
             'afecta si compras los envases» y su contrario «te afecta siempre». Lo '
             'que decide es DONDE compras y QUE compras, y por eso el libro 2 pide los '
             'kg/mes importados o adquiridos en otro pais de la UE, no los kg totales.')}


# ==========================================================================
# 17. GASTOS FIJOS Y ECONOMIA DEL ANO DE CRUCERO
# ==========================================================================
def coste_empresa_anual_persona(pid):
    """Bruto de convenio x 15 pagas x jornada x (1 + SS). Del bruto al coste empresa
    hay un 33 %, y ese es el salto que mas sorprende al lector (cap. 17)."""
    for p in PLANTILLA:
        if p[0] != pid:
            continue
        bruto_anual = CONVENIO[p[3] - 1][3]
        return bruto_anual * p[2] * (1.0 + P('ss_empresa'))
    raise KeyError('Persona desconocida: %r' % pid)


def coste_personal_anual():
    return sum(coste_empresa_anual_persona(p[0]) for p in PLANTILLA)


GASTOS_FIJOS_MENSUALES = [
    # (partida, importe mensual, fuente, nota)
    ('Personal (coste empresa con Seguridad Social)', None,
     'CHN-65b + motor.PARAMETROS[ss_empresa]',
     'Se calcula desde PLANTILLA y CONVENIO: 3 personas, 2,5 jornadas, 15 pagas. La '
     'tabla salarial es la de Madrid y va MARCADA COMO EJEMPLO (D43).'),
    ('Cuota de autonomos del titular', 320.0, 'supuesto',
     'El titular es el Encargado y su retribucion YA esta en la nomina: lo que va '
     'aparte es su cuota. Ponerle ademas un renglon de «retribucion del propietario» '
     'seria contarlo dos veces.'),
    ('Alquiler del local', 1300.0, 'supuesto', 'Ver `NEGOCIO[renta_mensual]`.'),
    ('Suministros (electricidad, agua y climatizacion)', 780.0, 'supuesto',
     'Un obrador de chocolate no tiene hornos, pero tiene TRES equipos de frio y una '
     'climatizacion con deshumidificacion funcionando 24 horas, y en agosto a pleno. '
     'No se estima: se pide la simulacion a la comercializadora con la potencia del '
     'proyecto electrico.'),
    ('Seguros', 110.0, 'supuesto',
     'Responsabilidad civil y continente. `CHN-70` (seguro de RC) esta en EXCLUIDOS de '
     'la verificacion legal: no esta verificado como obligatorio y depende de la '
     'comunidad autonoma. Publicar una cifra de seguro de RC como dato verificado esta '
     'prohibido (§5.1, 28).'),
    ('Gestoria y asesoria', 200.0, 'supuesto', ''),
    ('Software, TPV y pasarela de cobro', 60.0, 'supuesto',
     'Con Verifactu en el horizonte (`CHN-75`: 1-ene-2027 para sociedades y '
     '1-jul-2027 para autonomos, NO 2026), esta cuota deja de ser opcional.'),
    ('Telefonia e internet', 55.0, 'supuesto', ''),
    ('Limpieza y consumibles', 140.0, 'supuesto',
     'Incluye guantes y utillaje dedicado: el equipo usado con un alergeno no se '
     'reutiliza para otro alimento sin limpiarlo (`CHN-33`).'),
    ('Mantenimiento de equipos', 130.0, 'supuesto',
     'Si la variante de taza y churros lleva freidora de gas, suma la inspeccion '
     'periodica obligatoria cada cinco anos, que se repercute (`CHN-48`).'),
    ('Publicidad y redes', 180.0, 'supuesto', ''),
    ('Otros gastos de estructura', 130.0, 'supuesto', ''),
    ('Amortizacion del inmovilizado', None, 'supuesto',
     'CAPEX amortizable / anos de amortizacion. Sin ella, la rentabilidad publicada es '
     'mentira: la atemperadora se gasta.'),
    ('Gastos financieros del prestamo', None, 'supuesto',
     'Intereses del ANO DE CRUCERO (el ano 2), no los del ano 1, que es el de la '
     'carencia: esta lista es la foto de un mes normal. Con los del ano 1, la '
     'calculadora de CAPEX y el plan financiero publicarian dos inversiones totales '
     'distintas para la misma bomboneria.'),
]


# ==========================================================================
# 18. FINANCIACION (todo supuesto declarado)
# ==========================================================================
#: 40 % recursos propios / 60 % prestamo a 7 anos. NO existe dato publico de
#: estructura de financiacion del sector: los cuatro numeros son supuestos y van en
#: celda verde con el supuesto escrito al lado.
FINANCIACION = {
    'pct_recursos_propios': 0.40,
    'pct_prestamo': 0.60,
    'principal': None,          # SE DERIVA: ver `principal_prestamo()`
    'tipo_nominal': 0.062,
    'plazo_meses': 84,
    'carencia_meses': 6,
    'fuente': 'supuesto',
    'nota': ('Todo supuesto: las condiciones las pone tu banco y dependen de la '
             'garantia. La carencia de 6 meses es la que hace que el prestamo no se '
             'coma la caja justo en la rampa de arranque, y es lo primero que hay que '
             'negociar. Durante la carencia solo se pagan intereses.\n'
             'EL PRINCIPAL NO SE TECLEA: lo DERIVA `principal_prestamo()` como el 60 % '
             'de la inversion total, redondeado a centenas. Si manana cambia una sola '
             'partida del CAPEX, el principal se mueve SOLO y la estructura 40/60 sigue '
             'saliendo exacta. Antes era un numero fijo que habia que acordarse de '
             'ajustar a mano, y esa es la definicion del defecto que esta familia ya '
             'pago en Pasteleria.')}


#: El principal es un PUNTO FIJO, y por eso hace falta una funcion y no una constante:
#: la inversion total incluye el fondo de maniobra, el fondo son seis meses de gastos
#: fijos, y los gastos fijos incluyen los intereses del prestamo, que dependen del
#: principal. La iteracion converge en tres o cuatro pasadas porque el termino que se
#: realimenta es diminuto: 0,60 x 6 x (interes mensual / principal) es del orden del
#: 2 %, asi que cada vuelta reduce el error a la quincuagesima parte.
_PRINCIPAL = {'valor': None, 'provisional': None}


def _principal_en_uso():
    """El principal con el que trabajar AHORA MISMO. Durante la iteracion del punto
    fijo devuelve el provisional; despues, el definitivo. `cuadro_frances()` lo llama
    en vez de leer una constante."""
    if _PRINCIPAL['valor'] is not None:
        return _PRINCIPAL['valor']
    if _PRINCIPAL['provisional'] is not None:
        return _PRINCIPAL['provisional']
    # Fuera de la iteracion, RESOLVER EL PUNTO FIJO, nunca devolver una semilla.
    # Esto fue un bug real y no daba ningun error: si el primero que preguntaba por
    # los gastos fijos era el P&L -y no `principal_prestamo()`-, `_FIJOS_CACHE` se
    # quedaba cacheado con los intereses de una SEMILLA de 53.500 euros, el P&L
    # publicaba 22.015 euros de beneficio donde habia 20.093, y el unico sintoma era
    # un margen neto un punto mas alto. Lo cazo el assert de la banda 9-11 %.
    # No hay recursion: `principal_prestamo()` publica su provisional ANTES de pedir
    # los gastos fijos, asi que toda llamada anidada sale por la rama de arriba.
    return principal_prestamo()


def principal_prestamo():
    """El 60 % de la inversion total, redondeado a centenas. SE DERIVA, no se teclea."""
    if _PRINCIPAL['valor'] is not None:
        return _PRINCIPAL['valor']
    pr = round(FINANCIACION['pct_prestamo'] * capex_sin_fondo_de_maniobra(), -2)
    for _ in range(60):
        _PRINCIPAL['provisional'] = pr
        _FIJOS_CACHE.pop('v', None)
        total = (capex_sin_fondo_de_maniobra()
                 + P('meses_colchon_fondo_maniobra') * gastos_fijos_mensuales())
        nuevo = round(FINANCIACION['pct_prestamo'] * total, -2)
        if abs(nuevo - pr) < 1.0:
            pr = nuevo
            break
        pr = nuevo
    _PRINCIPAL['provisional'] = None
    _PRINCIPAL['valor'] = pr
    _FIJOS_CACHE.pop('v', None)   # los fijos definitivos, con el principal definitivo
    return pr


def cuadro_frances():
    """Intereses MES A MES del prestamo: interes sobre el saldo vivo, carencia de
    principal y cuota francesa algebraica. Vive aqui, y no solo en el generador del
    libro 7, porque los intereses del ano de crucero entran en los gastos fijos y de
    ahi en el fondo de maniobra."""
    saldo = _principal_en_uso()
    i = FINANCIACION['tipo_nominal'] / 12.0
    n_total = FINANCIACION['plazo_meses']
    n_car = FINANCIACION['carencia_meses']
    n_amort = n_total - n_car
    cuota = saldo * i / (1.0 - (1.0 + i) ** (-n_amort)) if i else saldo / n_amort
    filas = []
    for mes in range(1, n_total + 1):
        interes = saldo * i
        if mes <= n_car:
            principal = 0.0
            pago = interes
        else:
            principal = cuota - interes
            pago = cuota
        filas.append((mes, saldo, interes, principal, pago))
        saldo -= principal
    return filas


def intereses_anio(n):
    filas = cuadro_frances()
    return sum(f[2] for f in filas if (n - 1) * 12 < f[0] <= n * 12)


def intereses_anio_1():
    return intereses_anio(1)


def intereses_anio_crucero():
    return intereses_anio(P('anio_crucero'))


# ==========================================================================
# 19. PROVEEDORES VERIFICADOS Y EL ARBOL DEL EUDR (D48)
# ==========================================================================
#: SOLO los seis con URL comprobada. Los marcados con lupa en el research NO se
#: publican: un directorio con un enlace roto vale menos que uno corto.
#:
#: `papel_eudr` va VACIO A PROPOSITO: es la celda verde de TRES valores que el lector
#: rellena preguntando a su proveedor. El art. 5.3.a) del EUDR obliga a guardar los
#: datos del proveedor SIEMPRE, pero el numero de referencia de su declaracion de
#: diligencia debida «unicamente en el caso de que su proveedor sea un operador»
#: (`CHN-24`). Un semaforo que lo pidiera a todos SUSPENDERIA a proveedores que
#: cumplen: por eso es un ARBOL, no una columna con semaforo.
PAPELES_EUDR = ('operador', 'operador posterior', 'comerciante')
PAPELES_EUDR_TEXTO = {
    'operador': ('Hace la PRIMERA comercializacion en el mercado de la Union, o '
                 'exporta. Si es tu caso -por ejemplo, importas grano para '
                 'bean-to-bar-, te toca diligencia debida COMPLETA antes de introducir '
                 'en el mercado, declaracion presentada previamente, asuncion de '
                 'responsabilidad y registro de las declaraciones durante cinco anos '
                 '(`CHN-25`). A ESTE proveedor SI hay que pedirle el numero de '
                 'referencia de su DDS.'),
    'operador posterior': ('Introduce en el mercado productos elaborados con otros '
                           'productos YA amparados por una declaracion de diligencia '
                           'debida (`CHN-23`, art. 2.15 ter). Es lo que normalmente '
                           'sera una chocolateria que compra cobertura ya '
                           'comercializada en la UE. A este NO se le pide el numero de '
                           'DDS por el art. 5.3.a).'),
    'comerciante': ('Ni introduce ni exporta: comercia dentro. Tampoco se le pide el '
                    'numero de DDS.'),
}
NOTA_EUDR = (
    'REDACCION OBLIGATORIA, y el paso es INFERENCIA DECLARADA, no nivel A: «si tu '
    'cobertura llega ya comercializada en la UE y amparada por una declaracion de '
    'diligencia debida, eres operador posterior (art. 2.15 ter) y el aplazamiento del '
    'art. 38.3 -que es para operadores- no te alcanza: tu fecha es el 30 de diciembre '
    'de 2026. Si tu cobertura NO esta amparada (compra anterior al EUDR, proveedor que '
    'no lo acredita), la calificacion deja de ser automatica y hay que revisarla». '
    'Estan PROHIBIDAS «siempre eres operador posterior» y «tu fecha es el 30-12-2026 '
    'pase lo que pase». Y la exclusion de los operadores posteriores del punto 15 se '
    'PARAFRASEA, no se entrecomilla: consta en la nota de `CHN-22`, no entre las 81 '
    'citas del gate de literalidad. Verificado a 12-09-2026: comprueba el estado del '
    'EUDR antes de comprar cacao.')

PROVEEDORES = [
    # (nombre, categoria, url, fuente, papel_eudr (vacio: lo rellena el lector), nota)
    ('Callebaut / Barry Callebaut Iberica', 'Coberturas y chocolate profesional',
     'https://www.callebaut.com/es-ES/', 'CHS-50', '',
     'Mayor grupo del sector con presencia industrial en Espana. De aqui sale la '
     'referencia de precio del juego de datos (`CHS-28a`): Callebaut 811, bloque de '
     '5 kg a 125,08 euros CON IVA, o sea 25,02 euros/kg.'),
    ('Asociacion Chocolate Bean to Bar Espana', 'Grano de cacao para bean-to-bar',
     'https://www.chocolatebeantobar.com/asociados/', 'CHS-51', '',
     'La via fiable para el grano: su listado publico permite identificar a los '
     'makers y a los importadores. Se publica como «MAS DE 40 MIEMBROS», nunca con '
     'una cifra cerrada (`N-18` prohibe «45 miembros»). Ojo: las webs individuales de '  # LN-OK
     'los proveedores de grano NO se abrieron, asi que no se publica ninguna.'),
    ('Utilcentre', 'Maquinaria de chocolate (distribuidor Selmi y Pavoni)',
     'https://www.utilcentre.com/maquinaria-chocolate.html', 'CHS-52', '',
     'Precios publicos, y es de donde salen `CHS-41a` a `CHS-41j` y `CHS-42a` a '
     '`CHS-42j`. Base de IVA NO declarada en casi todas sus fichas: es exactamente la '
     'trampa que explica el cap. 08.'),
    ('RestorHome', 'Moldes de bomboneria y utensilios',
     'https://www.restorhome.es/471-moldes-bomboneria-Chocolate-World', 'CHS-53', '',
     'Moldes Chocolate World, Pavoni y Martellato. De aqui sale el rango de '
     '24,20-42,83 euros/ud (`CHS-45a`) que el juego de datos publica COMO RANGO.'),
    ('SelfPackaging', 'Packaging: cajas y estuches para bombones',
     'https://selfpackaging.es/90-cajas-para-bombones', 'CHS-54', '',
     'Personalizacion con logo desde pocas unidades. Su web devolvio HTTP 403 al '
     'intentar leer precios, asi que el packaging del CAPEX es SUPUESTO.'),
    ('Gift Campaign', 'Regalo corporativo B2B',
     'https://www.giftcampaign.es/dulces-personalizados/chocolates.html', 'CHS-55', '',
     'Dos reglas operativas verificadas del canal corporativo: plazo de entrega de '
     '14-16 dias desde la aprobacion de la muestra virtual, y minimos de fabricacion '
     'de 10 a 25 cajas. El plazo es lo que decide si aceptas un pedido de empresa en '
     'diciembre.'),
]
NOTA_PROVEEDORES = (
    'Seis proveedores con URL comprobada el 12-09-2026. El research recogio muchos mas '
    'sin verificar y NO se publican. La columna «papel EUDR» va VACIA: la rellena el '
    'lector preguntando, y el numero de DDS solo se pide en la rama «operador» (D48). '
    'Directorio del grupo: hosply.pro, y su TLS se comprueba ANTES de enlazarlo desde '
    'el cap. 13 (precedente: ingredientsindex.pro tiene el certificado roto y 62 posts '
    'del blog enlazan a un aviso de seguridad).')
HOSPLY_URL = ('https://hosply.pro/?utm_source=guia-chocolateria-obrador'
              '&utm_medium=producto&utm_campaign=cap13-proveedores')

#: LA SEGUNDA TABLA DEL LIBRO 9, y la que no existe en ningun libro del catalogo.
#: El art. 5.3.b) del EUDR obliga a registrar tambien el nombre de los operadores
#: posteriores y comerciantes «a los que hayan suministrado los productos
#: pertinentes» (`CHN-24`). Se conserva CINCO ANOS. Cierra el circulo con D19: los
#: canales que se salen de la nota del epigrafe 644.5 son justo los que hay que
#: registrar.
CLIENTES_B2B = [
    # (nombre FICTICIO, tipo, canal, poblacion, producto suministrado)
    ('Cafeteria El Mirador', 'Hosteleria', 'B2B hosteleria', 'Ciudad de ejemplo',
     'Bombones de coleccion a granel y tabletas'),
    ('Hotel Plaza Mayor (A&B)', 'Hosteleria', 'B2B hosteleria', 'Ciudad de ejemplo',
     'Bombon de cortesia de habitacion y cajas de 12'),
    ('Industrias Nogal, S.L.', 'Empresa', 'Regalo corporativo', 'Ciudad de ejemplo',
     'Estuche corporativo personalizado de 24 bombones'),
    ('Tienda gourmet La Despensa', 'Minorista de distinta titularidad',
     'B2B hosteleria', 'Ciudad de ejemplo',
     'Tabletas de origen y almendras banadas'),
]
FUENTE_CLIENTES_B2B = 'supuesto'
NOTA_CLIENTES_B2B = (
    'CUATRO CLIENTES FICTICIOS DECLARADOS, para que la tabla del libro 9 tenga forma. '
    'Lo que NO es ficticio es la obligacion: registrar a quien suministras (art. '
    '5.3.b) del EUDR, `CHN-24`) y conservarlo cinco anos. Escribir «basta con '
    'registrar a tus proveedores» esta PROHIBIDO (§5.1, prohibicion 3).\n'
    'Y el cuarto cliente es el que cambia tu regimen sanitario: «Tienda gourmet La '
    'Despensa» es un MINORISTA DE DISTINTA TITULARIDAD, asi que activa el art. 3 del '
    'RD 1021/2022 (`CHN-41`). Basta con que UNO de tus clientes este inscrito en el '
    'RGSEAA para romper el requisito de «restringido», y los tres requisitos son '
    'ACUMULATIVOS.')


# ==========================================================================
# 20. LAS 12 FILAS DEL CALENDARIO DEL KIT (D35)
# ==========================================================================
#: COPIA DECLARADA, FILA A FILA, de `BONUS-02-calendario-anual-tareas.xlsx!Calendario`,
#: leida el 12-09-2026. Temporada declarada por el kit: SIETE meses «Alta» (feb, mar,
#: abr, may, oct, nov, dic), CUATRO «Media» (ene, jun, jul, sep) y UNO «Baja» (ago).
#:
#: POR QUE AQUI SI SE COPIA Y EN EL LIBRO 5 NO: en el 5 la tabla del kit ES el
#: entregable, asi que se cita y no se reescribe (D30); en el 6 las 12 filas son el
#: EJE sobre el que se calculan los euros, asi que bajan como ETIQUETAS DE FILA
#: declaradas como copia. Sus «Acciones clave» y sus «Productos destacados» se citan
#: literales y NO se reescriben, y el cap. 18 NO repite el calendario: remite al kit
#: y solo narra los euros.
#:
#: Los campos economicos (`uds_dia_normal`, `uds_dia_pico`, `pvp_campana`,
#: `dias_campana`, `refuerzo_*`, `antelacion_*`) son SUPUESTOS declarados: el kit
#: pone las fechas y el que, y este juego de datos pone los euros.
CAMPANAS = [
    {'mes': 1, 'nombre_mes': 'Enero', 'temporada': 'Media',
     'acciones_kit': ('Reyes (6): liquidar turron y figuras de Navidad · rebajas '
                      'post-Navidad · lanzar la coleccion de invierno · planificar '
                      'San Valentin'),
     'productos_kit': 'Trufas, bombones especiados, chocolate caliente',
     'campana': 'Reyes', 'campana_propia': False,
     'producto_estrella': 'TF1', 'uds_dia_normal': 0, 'uds_dia_pico': 40,
     'pvp_campana': 18.50, 'dias_campana': 5,
     'refuerzo_personas': 0, 'refuerzo_horas_persona': 0,
     'antelacion_moldes_semanas': 0, 'antelacion_packaging_semanas': 0,
     'fuente_fila': F_KIT_CALENDARIO, 'fuente_economia': 'supuesto',
     'nota': ('Fecha menor: cierra la produccion de Navidad y liquida el stock. Lo '
              'que se produce para Reyes ya esta hecho en diciembre.')},
    {'mes': 2, 'nombre_mes': 'Febrero', 'temporada': 'Alta',
     'acciones_kit': ('San Valentin (14): corazones y edicion limitada · fecha limite '
                      'de encargos el dia 10 · entregas expres los dias 13 y 14'),
     'productos_kit': 'Corazones, bombones premium, tabletas personalizadas',
     'campana': 'San Valentin', 'campana_propia': True,
     'producto_estrella': 'CJ1', 'uds_dia_normal': 8, 'uds_dia_pico': 55,
     'pvp_campana': 20.00, 'dias_campana': 6,
     'refuerzo_personas': 1, 'refuerzo_horas_persona': 30,
     'antelacion_moldes_semanas': 8, 'antelacion_packaging_semanas': 6,
     'fuente_fila': F_KIT_CALENDARIO, 'fuente_economia': 'supuesto',
     'nota': ('El pico de regalo. `CHS-34` mide que las ventas de chocolates y dulces '
              'pueden DUPLICAR el promedio anual en San Valentin, y que hay companias '
              'que hacen en ese solo evento hasta el 10 % de su venta anual: ese 10 % '
              'es de una compania concreta, no una regla del sector. La fecha limite '
              'de encargos la publica el propio kit: el dia 10.')},
    {'mes': 3, 'nombre_mes': 'Marzo', 'temporada': 'Alta',
     'acciones_kit': ('Dia del Padre (19) · preparacion de Pascua (fecha movil) · '
                      'talleres infantiles de Semana Santa'),
     'productos_kit': 'Figuras, huevos, monas de chocolate',
     'campana': 'Dia del Padre', 'campana_propia': False,
     'producto_estrella': 'CJ1', 'uds_dia_normal': 8, 'uds_dia_pico': 26,
     'pvp_campana': 20.00, 'dias_campana': 4,
     'refuerzo_personas': 0, 'refuerzo_horas_persona': 0,
     'antelacion_moldes_semanas': 6, 'antelacion_packaging_semanas': 4,
     'fuente_fila': F_KIT_CALENDARIO, 'fuente_economia': 'supuesto',
     'nota': ('Fecha menor, y el mes en el que ya hay que estar produciendo Pascua. '
              'Los talleres infantiles de Semana Santa son la primera vez del ano en '
              'que la sala factura por hora en vez de por bombon.')},
    {'mes': 4, 'nombre_mes': 'Abril', 'temporada': 'Alta',
     'acciones_kit': ('Semana Santa y Pascua: monas y huevos · arrancan las COMUNIONES '
                      '(abril-junio): detalles de mesa, figuras y cajas personalizadas'),
     'productos_kit': 'Huevos, conejos, bombones florales',
     'campana': 'Pascua', 'campana_propia': True,
     'producto_estrella': 'TF1', 'uds_dia_normal': 2, 'uds_dia_pico': 30,
     'pvp_campana': 18.50, 'dias_campana': 10,
     'refuerzo_personas': 1, 'refuerzo_horas_persona': 40,
     'antelacion_moldes_semanas': 10, 'antelacion_packaging_semanas': 6,
     'fuente_fila': F_KIT_CALENDARIO, 'fuente_economia': 'supuesto',
     'nota': ('Campana de FIGURA Y MOLDE: la compra de moldes va MUY por delante, y es '
              'tesoreria inmovilizada que el libro 6 cuantifica. Fecha movil: si la '
              'Pascua cae pronto, marzo se come parte de abril.')},
    {'mes': 5, 'nombre_mes': 'Mayo', 'temporada': 'Alta',
     'acciones_kit': ('Dia de la Madre (1.er domingo) · pico de COMUNIONES · edicion '
                      'regalo premium'),
     'productos_kit': 'Bombones premium, cestas regalo, tabletas grabadas',
     'campana': 'COMUNIONES (pico) y Dia de la Madre', 'campana_propia': True,
     'producto_estrella': 'CJ4', 'uds_dia_normal': 1, 'uds_dia_pico': 14,
     'pvp_campana': 34.00, 'dias_campana': 14,
     'refuerzo_personas': 1, 'refuerzo_horas_persona': 50,
     'antelacion_moldes_semanas': 8, 'antelacion_packaging_semanas': 10,
     'fuente_fila': F_KIT_CALENDARIO, 'fuente_economia': 'supuesto',
     'nota': ('El pico de las comuniones, y el mes con mas dias de campana del primer '
              'semestre. El packaging personalizado va con MAS antelacion que los '
              'moldes: es lo contrario de Pascua.')},
    {'mes': 6, 'nombre_mes': 'Junio', 'temporada': 'Media',
     'acciones_kit': ('Ultimas comuniones · inicio del verano: adaptar catalogo (menos '
                      'ganache fresca, mas tableta y producto estable)'),
     'productos_kit': 'Tabletas con fruta, bombones en camara',
     'campana': 'COMUNIONES (ultimas)', 'campana_propia': True,
     'producto_estrella': 'CJ2', 'uds_dia_normal': 1, 'uds_dia_pico': 9,
     'pvp_campana': 28.00, 'dias_campana': 8,
     'refuerzo_personas': 0, 'refuerzo_horas_persona': 0,
     'antelacion_moldes_semanas': 6, 'antelacion_packaging_semanas': 8,
     'fuente_fila': F_KIT_CALENDARIO, 'fuente_economia': 'supuesto',
     'nota': ('El mes de apertura de La Almendra (1 de junio): «Media», con seis meses '
              'de rodaje por delante hasta Navidad. Y el mes en el que el catalogo '
              'EMPIEZA a cambiar, literal del kit: «menos ganache fresca, mas tableta '
              'y producto estable». Aqui arranca tambien la parada de ENVIOS, que es '
              'de canal online, no de mostrador.')},
    {'mes': 7, 'nombre_mes': 'Julio', 'temporada': 'Media',
     'acciones_kit': ('Temporada turistica: packs souvenir y colaboraciones locales · '
                      'vigilar a diario la temperatura de tienda y vitrina'),
     'productos_kit': 'Tabletas souvenir, bombones regionales',
     'campana': 'Temporada turistica', 'campana_propia': False,
     'producto_estrella': 'TF5', 'uds_dia_normal': 6, 'uds_dia_pico': 18,
     'pvp_campana': 7.40, 'dias_campana': 26,
     'refuerzo_personas': 0, 'refuerzo_horas_persona': 0,
     'antelacion_moldes_semanas': 0, 'antelacion_packaging_semanas': 4,
     'fuente_fila': F_KIT_CALENDARIO, 'fuente_economia': 'supuesto',
     'nota': ('El turista no compra ganache: compra souvenir que viaja. Por eso julio '
              'ya usa el MIX DE VERANO, y por eso el kit manda vigilar A DIARIO la '
              'temperatura de tienda y vitrina.')},
    {'mes': 8, 'nombre_mes': 'Agosto', 'temporada': 'Baja',
     'acciones_kit': ('Asuncion (15): festivo nacional, la tienda abre para el turista '
                      'aunque el obrador pare · mantenimiento profundo · vacaciones '
                      'escalonadas · cerrar el pedido de coberturas de Navidad'),
     'productos_kit': 'Produccion reducida, planificacion Q4',
     'campana': 'Valle del obrador', 'campana_propia': False,
     'producto_estrella': 'TB1', 'uds_dia_normal': 5, 'uds_dia_pico': 9,
     'pvp_campana': 6.90, 'dias_campana': 26,
     'refuerzo_personas': 0, 'refuerzo_horas_persona': 0,
     'antelacion_moldes_semanas': 0, 'antelacion_packaging_semanas': 0,
     'fuente_fila': F_KIT_CALENDARIO, 'fuente_economia': 'supuesto',
     'nota': ('EL UNICO MES «BAJA» DE LOS DOCE. Lo que para es el OBRADOR, no la caja: '
              'el literal del kit es «la tienda abre para el turista aunque el obrador '
              'pare». Y es el mes en el que se CIERRA EL PEDIDO DE COBERTURAS DE '
              'NAVIDAD, que es la decision de tesoreria mas grande del ano.')},
    {'mes': 9, 'nombre_mes': 'Septiembre', 'temporada': 'Media',
     'acciones_kit': ('Vuelta a la rutina · coleccion de otono · ferias gastronomicas '
                      '· abrir la agenda de pedidos corporativos de Navidad'),
     'productos_kit': 'Bombones de frutos secos, praline, especiados',
     'campana': 'Apertura de agenda corporativa', 'campana_propia': False,
     'producto_estrella': 'CJ4', 'uds_dia_normal': 1, 'uds_dia_pico': 4,
     'pvp_campana': 34.00, 'dias_campana': 20,
     'refuerzo_personas': 0, 'refuerzo_horas_persona': 0,
     'antelacion_moldes_semanas': 0, 'antelacion_packaging_semanas': 12,
     'fuente_fila': F_KIT_CALENDARIO, 'fuente_economia': 'supuesto',
     'nota': ('El mes que decide diciembre: aqui se abre la agenda corporativa, y el '
              'plazo minimo de un pedido de empresa es de 14 dias desde la aprobacion '
              'de la muestra (`CHS-55`). Vender un estuche corporativo el 15 de '
              'diciembre no es una venta: es una promesa que no se puede cumplir.')},
    {'mes': 10, 'nombre_mes': 'Octubre', 'temporada': 'Alta',
     'acciones_kit': ('Halloween (31): figuras y bombones de temporada · produccion '
                      'navidena a pleno · publicar el catalogo de Navidad'),
     'productos_kit': 'Figuras Halloween, bombones calabaza, tabletas oscuras',
     'campana': 'Halloween', 'campana_propia': True,
     'producto_estrella': 'TF1', 'uds_dia_normal': 1, 'uds_dia_pico': 12,
     'pvp_campana': 18.50, 'dias_campana': 6,
     'refuerzo_personas': 0, 'refuerzo_horas_persona': 0,
     'antelacion_moldes_semanas': 8, 'antelacion_packaging_semanas': 6,
     'fuente_fila': F_KIT_CALENDARIO, 'fuente_economia': 'supuesto',
     'nota': ('Arranque de la temporada alta. Lo importante de octubre NO es Halloween: '
              'es que la produccion de Navidad ya va a pleno y se PAGA aqui, para '
              'cobrarse en diciembre. Ese desfase es lo que el libro 7 pone en la '
              'tesoreria mes a mes.')},
    {'mes': 11, 'nombre_mes': 'Noviembre', 'temporada': 'Alta',
     'acciones_kit': ('Todos los Santos (1): panellets y huesos de santo banados · '
                      'Black Friday (ultimo viernes) · preventa de Navidad · turrones '
                      'y cestas'),
     'productos_kit': ('Panellets y huesos de santo banados, turrones, cestas '
                       'corporativas, figuras navidenas'),
     'campana': 'Todos los Santos y Black Friday', 'campana_propia': True,
     'producto_estrella': 'TF3', 'uds_dia_normal': 0, 'uds_dia_pico': 90,
     'pvp_campana': 1.60, 'dias_campana': 5,
     'refuerzo_personas': 1, 'refuerzo_horas_persona': 25,
     'antelacion_moldes_semanas': 4, 'antelacion_packaging_semanas': 8,
     'fuente_fila': F_KIT_CALENDARIO, 'fuente_economia': 'supuesto',
     'nota': ('Dos campanas en un mes y ninguna se parece: Todos los Santos es '
              'produccion de obrador a pieza pequena (los huesos de santo, TF3, la '
              'unica referencia con huevo), y Black Friday es canal ONLINE con '
              'descuento. Ojo con el descuento: subir en noviembre para «rebajar» en '
              'diciembre NO cumple la regla de los 30 dias del art. 20 de la Ley '
              '7/1996 en la redaccion del RDL 24/2021 (`CHN-76`) - que NO es el art. '
              '20 del TRLGDCU.')},
    {'mes': 12, 'nombre_mes': 'Diciembre', 'temporada': 'Alta',
     'acciones_kit': ('NAVIDAD, maxima produccion · puente de la Constitucion y la '
                      'Inmaculada (6-8): fin de semana largo de maxima venta en tienda '
                      '· fecha limite de encargos y horarios especiales del 24 y el 31'),
     'productos_kit': 'Turrones, figuras, bombones navidenos, cestas',
     'campana': 'Navidad', 'campana_propia': True,
     'producto_estrella': 'CJ3', 'uds_dia_normal': 2, 'uds_dia_pico': 22,
     'pvp_campana': 45.00, 'dias_campana': 22,
     'refuerzo_personas': 2, 'refuerzo_horas_persona': 70,
     'antelacion_moldes_semanas': 12, 'antelacion_packaging_semanas': 14,
     'fuente_fila': F_KIT_CALENDARIO, 'fuente_economia': 'supuesto',
     'nota': ('LA CAMPANA MAYOR, y la que decide el ano. Su pedido corporativo se '
              'cierra en octubre y su limite de produccion lo calcula el libro 7 HACIA '
              'ATRAS desde la capacidad del libro 1 (cruce 7 <- 1 de `CRUCES`). La '
              'fecha limite de encargos y los horarios del 24 y el 31 los publica el '
              'propio kit.')},
]

#: Las COMUNIONES son CAMPANA PROPIA (D35) y sostienen abril, mayo y junio. Su
#: diferencia con Pascua no es el producto: es la ANTELACION DE PEDIDO y el detalle
#: de mesa personalizado.
CAMPANA_COMUNIONES = {
    'nombre': 'COMUNIONES',
    'meses': (4, 5, 6),
    'fuente': F_KIT_CALENDARIO,
    'literal_kit_abril': 'arrancan las COMUNIONES (abril-junio)',
    'literal_kit_mayo': 'pico de COMUNIONES',
    'literal_kit_junio': 'Ultimas comuniones',
    'antelacion_pedido_semanas': 6,
    'fuente_antelacion': 'supuesto',
    'producto_estrella': 'CJ4',
    'detalle_mesa_personalizado': True,
    'nota': ('Campana PROPIA, no una prolongacion de Pascua. Lo que la distingue es '
             'que el cliente encarga con SEIS SEMANAS de antelacion un detalle de mesa '
             'personalizado (nombre, fecha, color), asi que el obrador trabaja contra '
             'pedido firme y con senal: merma cero y tesoreria a favor. Y es la unica '
             'campana que reparte su carga en TRES meses en lugar de concentrarla en '
             'una semana. El research la dejaba fuera y el calendario del kit la '
             'nombra tres veces.')}


# ==========================================================================
# 21. EL VALLE: AGOSTO, Y LO QUE PARA ES EL OBRADOR (D36)
# ==========================================================================
#: UN MES «BAJA» DE DOCE, no tres. Estan PROHIBIDAS las frases «valle de
#: junio-agosto», «un valle de tres meses» y «fijos que siguen corriendo con la caja
#: parada»: contradicen el calendario que la propia casa publica.
VALLE = {
    'mes': 8,
    'nombre_mes': 'Agosto',
    'temporada_kit': 'Baja',
    'fuente': F_KIT_CALENDARIO,
    'para_el_obrador': True,
    'para_la_tienda': False,
    'literal_kit': ('la tienda abre para el turista aunque el obrador pare'),
    'envios_parados_meses': (6, 7, 8, 9),
    'fuente_envios': 'supuesto declarado sobre un dato de CANAL ONLINE',
    'nota_envios': ('La parada de ENVIOS de junio a septiembre es de CANAL ONLINE, no '
                    'de mostrador: viene del operador que apaga los envios el 12 de '
                    'junio. El mostrador sigue vivo los cuatro meses, y en julio y '
                    'agosto con turista. Meter los dos en el mismo saco es el error '
                    'que produce «el valle de junio-agosto».'),  # LN-OK
    'meses_mix_verano': (7, 8),
    'que_calcula_la_hoja': ('la CAIDA DEL MARGEN al cambiar el mix -menos ganache '
                            'fresca, mas tableta y producto estable- y los gastos '
                            'fijos contra una facturacion MENOR PERO NO NULA'),
    'nota': ('El obrador para en agosto por tres motivos que el kit nombra: '
             'mantenimiento profundo, vacaciones escalonadas y el cierre del pedido de '
             'coberturas de Navidad. La tienda no. Y la unica linea del negocio que '
             'funciona en agosto y no depende del precio del cacao son los talleres: '
             'por eso su hoja calcula euros/hora de sala dando taller frente a '
             'euros/hora de la misma sala vendiendo.')}

#: Doce coeficientes de estacionalidad, media 1,000 EXACTA. Son SUPUESTOS declarados
#: -`N-13` prohibe publicar un reparto mensual de ventas como dato- y su forma la
#: dicta el calendario del kit: diciembre arriba, agosto abajo y siete meses «Alta».
ESTACIONALIDAD_MENSUAL = (0.92, 1.12, 1.02, 1.08, 1.10, 0.92,
                          0.82, 0.60, 0.86, 1.02, 1.10, 1.44)
FUENTE_ESTACIONALIDAD = 'supuesto'
NOTA_ESTACIONALIDAD = (
    'Media 1,000 exacta y agosto en el minimo (0,60), que es la traduccion a euros de '
    'la unica fila «Baja» del calendario del kit. Agosto NO vale cero: la tienda abre. '
    'Diciembre (1,44) es el maximo, y febrero (1,12) el segundo pico del primer '
    'semestre. SON SUPUESTOS: `N-13` prohibe publicar un reparto mensual de ventas de '
    'chocolateria como dato, porque no existe dato publico, y la guia ensena a medirlo '
    'con el TPV.')

#: Dias de apertura de cada mes. En agosto NO se cierra: lo que para es el obrador.
DIAS_APERTURA_MES = (26, 24, 26, 25, 26, 25, 27, 26, 25, 26, 25, 23)


def estacionalidad_pesos():
    """Los mismos doce coeficientes expresados como PESOS que suman 1,000, que es como
    los pide el molde `planes-v2_0` del libro 7."""
    return tuple(c / 12.0 for c in ESTACIONALIDAD_MENSUAL)


#: Rampa de arranque, con el patron del `plan-negocio-panaderia`
#: (`planes-v2_0/grupo_a.py`: `rampa_mes1` = 0,55 y `meses_rampa` = 6, subida en linea
#: recta hasta el 100 %). Un local que abre no factura desde el primer dia lo que
#: factura a los seis meses, y proyectar el ano 1 a velocidad de crucero es el error
#: que mas planes de negocio tumba. Y aqui hay un motivo extra: La Almendra abre el 1
#: de junio, asi que sus seis meses de rampa caen justo sobre el valle de agosto.
RAMPA = {'mes1': 0.55, 'meses': 6, 'fuente': 'planes-v2_0/grupo_a.py + supuesto'}


def rampa_mensual():
    m1, n = RAMPA['mes1'], RAMPA['meses']
    return tuple(min(1.0, m1 + (1.0 - m1) * i / float(max(1, n - 1))) for i in range(12))


def campana(mes):
    for c in CAMPANAS:
        if c['mes'] == mes:
            return c
    raise KeyError('Mes fuera de rango: %r' % mes)


def meses_por_temporada(temporada):
    return [c['mes'] for c in CAMPANAS if c['temporada'] == temporada]


# ==========================================================================
# 22. LOS CINCO CANALES (D19)
# ==========================================================================
#: TRES DE LOS CINCO caen FUERA de la nota del epigrafe 644.5, y ese es el argumento
#: legal mas util del producto. La nota es literal: el 644.5 «Comercio al por menor
#: de bombones y caramelos» faculta para «la fabricacion de bombones y caramelos en
#: el propio establecimiento, siempre que su comercializacion se realice en las
#: propias dependencias de venta» (`CHN-72`).
#:
#: LA HOJA NO EMITE UN EPIGRAFE DE IAE POR CANAL, y esto no es una omision: NINGUNA
#: FUENTE LO DA. La salida es la PREGUNTA redactada para el asesor, igual que D33
#: resolvio la carga termica. Lo que si esta verificado y entra:
#:   · Regla 4.a.1: «el pago de la cuota correspondiente a una actividad faculta,
#:     exclusivamente, para el ejercicio de esa actividad» (`CHN-94`).
#:   · Regla 4.a.2.D): el comercio al por menor se define por el DESTINO -uso o
#:     consumo directo- y comprende expresamente el realizado SIN almacen ni
#:     establecimiento, asi que LA VENTA ONLINE AL CONSUMIDOR SI ES MINORISTA
#:     (`CHN-95`).
#:   · Regla 4.a.2.A): el epigrafe INDUSTRIAL (donde esta el 421.1) faculta para la
#:     venta al por mayor Y al por menor (`CHN-96`) - pero eso te saca del amparo de
#:     la Ley 12/2012, cuyo Anexo lista el 644.5 y no el 421.1 (`CHN-49b`).
#:
#: PROHIBIDO escribir «con el 644.5 puedes vender a hosteleria, a empresas y por
#: envio sin mas», y prohibido dar un epigrafe de IAE por canal como veredicto.
NOTA_644_5 = (
    'la fabricacion de bombones y caramelos en el propio establecimiento, siempre que '
    'su comercializacion se realice en las propias dependencias de venta')
FUENTE_NOTA_644_5 = 'CHN-72'
PREGUNTA_AL_ASESOR = (
    'Mi epigrafe es el 644.5, cuya nota permite fabricar bombones «siempre que su '
    'comercializacion se realice en las propias dependencias de venta». Voy a vender '
    'ademas por este canal: [CANAL]. Con la Regla 4.a.1 del RDLeg 1175/1990 delante '
    '-una cuota faculta exclusivamente para su actividad-, ¿ese canal me obliga a dar '
    'otra alta, y cual? Y si la respuesta es el epigrafe industrial 421.1, ¿que '
    'consecuencias tiene que el Anexo de la Ley 12/2012 liste el 644.5 y no el 421.1?')

CANALES = [
    {'canal': 'Mostrador', 'ventas_pct': 62.0, 'margen_bruto': 0.70,
     'coste_servir_pct': 0.0, 'comision_plataforma': 0.0, 'coste_envio_refrigerado': 0.0,
     'cobro_dias': 0, 'pedido_minimo': None, 'sale_de_la_nota_644_5': 'no',
     'fuente': 'supuesto', 'fuente_legal': 'CHN-72',
     'nota': ('Cobro al contado y dentro de la nota del 644.5 sin discusion: vendes en '
              'las propias dependencias. Es el canal que paga el alquiler.')},
    {'canal': 'Online con envio refrigerado', 'ventas_pct': 12.0, 'margen_bruto': 0.58,
     'coste_servir_pct': 0.04, 'comision_plataforma': 0.0, 'coste_envio_refrigerado': 8.50,
     'cobro_dias': 0, 'pedido_minimo': 35.0, 'sale_de_la_nota_644_5': 'no lo se',
     'fuente': 'supuesto', 'fuente_legal': 'CHN-95 + CHN-59 + CHN-88 + CHN-90 + CHN-57',
     'nota': ('LO QUE SI ESTA VERIFICADO: vender online al consumidor SIGUE SIENDO '
              'comercio al por menor a efectos del IAE, porque la Regla 4.a.2.D) lo '
              'define por el destino y comprende el realizado sin establecimiento '
              '(`CHN-95`); y vender por internet NO cambia tu registro sanitario '
              '(`CHN-90`). LO QUE NO ESTA VERIFICADO es si la condicion de la nota del '
              '644.5 sobre la FABRICACION se rompe al comercializar fuera de las '
              'dependencias: eso es lo que hay que preguntar al asesor. Lo que si '
              'cambia: te conviertes en ENVASADOR (`CHN-59`) y respondes de la '
              'temperatura en el camion (`CHN-88`), mas la informacion obligatoria '
              'ANTES de pagar (`CHN-57`). Coste de envio refrigerado de 8,50 euros: '
              'SUPUESTO, y es el numero que decide si el canal existe. PARADO de junio '
              'a septiembre (`VALLE`).')},
    {'canal': 'B2B a hosteleria', 'ventas_pct': 11.0, 'margen_bruto': 0.48,
     'coste_servir_pct': 0.03, 'comision_plataforma': 0.0, 'coste_envio_refrigerado': 0.0,
     'cobro_dias': 45, 'pedido_minimo': 120.0, 'sale_de_la_nota_644_5': 'no lo se',
     'fuente': 'supuesto', 'fuente_legal': 'CHN-41 + CHN-72 + CHN-94',
     'nota': ('Peor margen y cobro a 45 dias: financias tu. Y es el canal que puede '
              'meterte en el art. 3 del RD 1021/2022 si dejas de ser marginal, '
              'localizado o restringido - los TRES requisitos son ACUMULATIVOS, y '
              'basta con servir a UN SOLO cliente inscrito en el RGSEAA para perder '
              '«restringido» (`CHN-41`). «Marginal» tiene DOS vias independientes: '
              'hasta el 25 % del volumen anual O hasta 500 kg/semana. Y los 500 kg NO '
              'incluyen el mostrador: el art. 3 solo habla del suministro a otros '
              'minoristas de distinta titularidad.')},
    {'canal': 'Regalo corporativo', 'ventas_pct': 9.0, 'margen_bruto': 0.55,
     'coste_servir_pct': 0.03, 'comision_plataforma': 0.0, 'coste_envio_refrigerado': 0.0,
     'cobro_dias': 30, 'pedido_minimo': 250.0, 'sale_de_la_nota_644_5': 'no lo se',
     'fuente': 'CHS-55 + supuesto', 'fuente_legal': 'CHN-24 + CHN-72 + CHN-94',
     'nota': ('PLAZO MINIMO VERIFICADO: 14 dias desde la aprobacion de la muestra, con '
              'minimos de fabricacion de 10 a 25 cajas (`CHS-55`). Es lo que decide si '
              'aceptas un pedido de empresa el 15 de diciembre. Y es el canal que '
              'obliga a la SEGUNDA TABLA del libro 9: el art. 5.3.b) del EUDR exige '
              'registrar a quien suministras, y conservarlo cinco anos (`CHN-24`, '
              'D48). El pedido minimo (250 euros) y los 30 dias de cobro son '
              'supuestos.')},
    {'canal': 'Talleres y catas', 'ventas_pct': 6.0, 'margen_bruto': 0.82,
     'coste_servir_pct': 0.05, 'comision_plataforma': 0.0, 'coste_envio_refrigerado': 0.0,
     'cobro_dias': 0, 'pedido_minimo': None, 'sale_de_la_nota_644_5': 'no',
     'fuente': 'CHS-30 + supuesto', 'fuente_legal': 'CHN-71b',
     'precio_persona_min': 25.0, 'precio_persona_max': 45.0,
     'minimo_personas': 6, 'duracion_min_minutos': 90, 'duracion_max_minutos': 150,
     'aforo': 12, 'horas_docente': 3.0,
     'nota': ('25-45 euros/persona, minimo habitual de 6 personas y 90-150 minutos '
              '(`CHS-30`). El aforo de 12 y las 3 horas de docente (preparacion y '
              'recogida incluidas) son SUPUESTOS. LA UNICA LINEA QUE FUNCIONA EN '
              'AGOSTO y que no depende del precio del cacao: por eso su hoja calcula '
              'euros/hora de sala dando taller frente a euros/hora de la misma sala '
              'vendiendo. IVA: NO esta exento (el art. 20.Uno.10.o excluye las clases '
              'para cuya realizacion haya que darse de alta en las tarifas '
              'empresariales del IAE, `CHN-71b`), pero el TIPO NO SE CIERRA y la guia '
              'NO publica ninguna cifra de tipo (D42e). Y ojo con la columna del '
              '644.5: el taller NO comercializa bombones fuera de tus dependencias, '
              'asi que no rompe la nota del epigrafe. Lo que si abre es otra pregunta, '
              'y es la del propio `CHN-71b`: si la Hacienda entiende que hay que darse '
              'de alta por esta actividad, eso es un alta distinta, no un problema de '
              'la nota del 644.5. Los TRES canales que la rompen son el online, el B2B '
              'y el corporativo.')},
]


# ==========================================================================
# 23. LOS OCHO CRUCES ENTRE LIBROS (D32)
# ==========================================================================
#: CERO FORMULAS QUE NOMBREN OTRO FICHERO. Donde un libro necesita el dato de otro,
#: el libro RECEPTOR lleva una CELDA VERDE etiquetada «trae aqui la cifra de
#: <fichero>.xlsx!<Hoja>!<Celda>» con su VALOR POR DEFECTO declarado, mas una FILA DE
#: CUADRE con semaforo que avisa si lo tecleado se aleja del origen.
#:
#: Lo prohibe la convencion de familia, lo promete la FAQ 11 al comprador, y es el
#: defecto ALTO que cazo la refutacion de Pasteleria: el fondo de maniobra calculado
#: dos veces publico DOS INVERSIONES TOTALES DISTINTAS en el mismo pack.
#:
#: Los cruces 7 <- 2 y 2 <- 7 son LOS DOS LADOS DE LA MISMA INVERSION TOTAL partida
#: en dos: el libro 2 publica el CAPEX ya DEPURADO de fondo, y el libro 7 dota el
#: fondo con SUS meses de colchon y SUS fijos y lo devuelve YA CALCULADO. Fundirlos
#: en uno solo («trae el CAPEX total») reintroduce la doble cuenta; y devolver los
#: FIJOS en vez del FONDO deja «meses de colchon» duplicado en los dos libros, que es
#: la otra mitad del mismo defecto.
#:
#: `gate_libros.py` comprueba dos cosas: que ninguna formula menciona otro fichero, y
#: que hay EXACTAMENTE OCHO filas de cuadre, contadas contra esta lista.
CRUCES = [
    {'n': 1, 'receptor': 6, 'origen': 1,
     'concepto': 'Deficit de capacidad del pico',
     'fichero_origen': 'capacidad-obrador-y-clima.xlsx', 'hoja_origen': 'Cuello de Botella',
     'fichero_receptor': 'campanas-y-valle-del-ano.xlsx', 'hoja_receptor': 'Capacidad vs Demanda del Pico',
     'nota': 'El 6 no puede saber si aguantas Navidad sin la capacidad que calcula el 1.'},
    {'n': 2, 'receptor': 7, 'origen': 1,
     'concepto': 'Capacidad diaria, para calcular hacia atras la fecha limite de pedidos de Navidad',
     'fichero_origen': 'capacidad-obrador-y-clima.xlsx', 'hoja_origen': 'Cuello de Botella',
     'fichero_receptor': 'plan-financiero-3-anos-chocolateria.xlsx', 'hoja_receptor': 'Tesoreria 12 meses',
     'nota': 'La fecha limite de encargos de Navidad NO es comercial: la fija la capacidad del obrador.'},
    {'n': 3, 'receptor': 9, 'origen': 2,
     'concepto': 'CAPEX por bloque, para medir la desviacion contra el precio real negociado',
     'fichero_origen': 'calculadora-capex-chocolateria.xlsx', 'hoja_origen': 'CAPEX por Bloque',
     'fichero_receptor': 'checklist-equipamiento-y-proveedores-cacao.xlsx', 'hoja_receptor': 'Equipamiento',
     'nota': 'El 9 es donde se anota lo que de verdad pagaste; el 2, lo que presupuestaste.'},
    {'n': 4, 'receptor': 4, 'origen': 3,
     'concepto': 'Precio de cobertura por referencia, EN BASE IMPONIBLE',
     'fichero_origen': 'sensibilidad-al-precio-del-cacao.xlsx',
     'hoja_origen': 'Coste de Cobertura por Referencia',
     'fichero_receptor': 'carta-de-apertura-y-escandallo-chocolate.xlsx',
     'hoja_receptor': 'Escandallo por Molde/Tanda',
     'nota': ('LA DE BASE IMPONIBLE, NUNCA la de base con IVA. `CHS-28a` esta declarada '
              'CON IVA y un escandallo con precios con IVA sale un 9 % alto.')},
    {'n': 5, 'receptor': 7, 'origen': 3,
     'concepto': 'Precio de cobertura EN BASE IMPONIBLE, para el coste de materia del P&L',
     'fichero_origen': 'sensibilidad-al-precio-del-cacao.xlsx',
     'hoja_origen': 'Coste de Cobertura por Referencia',
     'fichero_receptor': 'plan-financiero-3-anos-chocolateria.xlsx', 'hoja_receptor': 'PyG 3 Anos',
     'nota': 'Mismo precio que el 4: un concepto, una fuente, y una sola celda de origen.'},
    {'n': 6, 'receptor': 7, 'origen': 2,
     'concepto': 'CAPEX SIN el fondo de maniobra',
     'fichero_origen': 'calculadora-capex-chocolateria.xlsx', 'hoja_origen': 'Resumen',
     'fichero_receptor': 'plan-financiero-3-anos-chocolateria.xlsx', 'hoja_receptor': 'Inversion Inicial',
     'nota': ('LO QUE VIAJA NO ES «EL CAPEX TOTAL». El total del libro 2 INCLUYE el '
              'bloque «fondo de maniobra», asi que importarlo entero y pedir ademas el '
              'fondo lo contaria DOS VECES y volveria a publicar dos inversiones '
              'totales distintas. La hoja «Inversion Inicial» del 7 NO vuelve a pedir '
              'las nueve partidas: pide esta unica cifra.')},
    {'n': 7, 'receptor': 8, 'origen': 9,
     'concepto': 'Plazo de entrega critico de maquinaria, en semanas',
     'fichero_origen': 'checklist-equipamiento-y-proveedores-cacao.xlsx', 'hoja_origen': 'Equipamiento',
     'fichero_receptor': 'checklist-legal-licencias-y-cacao.xlsx', 'hoja_receptor': 'Cronograma y Ruta Critica',
     'nota': ('El 8 calcula la fecha de apertura con duraciones SUPUESTAS; lo que de '
              'verdad la mueve lo teclea el lector en el 9. La fila de cuadre avisa si '
              'la ruta critica es MAS CORTA que ese plazo: entonces la fecha la manda '
              'la maquinaria.')},
    {'n': 8, 'receptor': 2, 'origen': 7,
     'concepto': 'Fondo de maniobra YA CALCULADO (la magnitud, no sus factores)',
     'fichero_origen': 'plan-financiero-3-anos-chocolateria.xlsx', 'hoja_origen': 'Inversion Inicial',
     'fichero_receptor': 'calculadora-capex-chocolateria.xlsx', 'hoja_receptor': 'CAPEX por Bloque',
     'nota': ('EL CRUCE QUE CIERRA EL CIRCULO. El fondo es «meses de colchon x gastos '
              'fijos mensuales» y LOS DOS FACTORES VIVEN EN EL LIBRO 7. Por eso «meses '
              'de colchon» DEJA DE SER entrada del libro 2: si siguiera siendolo, el '
              'fondo se calcularia dos veces y los dos libros publicarian dos '
              'inversiones totales distintas con el mismo nombre. La fila de cuadre '
              'compara este valor con la linea «fondo de maniobra» del bloque de CAPEX '
              'del propio libro 2.')},
]


# ==========================================================================
# 24. CHECKLIST LEGAL POR FASES (libro 8)
# ==========================================================================
#: Seis fases, F1 a F6. Cada item: tramite · responsable · plazo orientativo en dias
#: · coste (con id o supuesto) · si cambia por comunidad autonoma.
#:
#: Las comunidades de ejemplo van DECLARADAS COMO EJEMPLOS: el mismo tramite funciona
#: distinto en cada una (`CHN-43`), y esta PROHIBIDO decir que tramite pide un
#: ayuntamiento concreto, porque no se ha abierto ninguna ordenanza (`CHN-49d` esta
#: en EXCLUIDOS).
CCAA_EJEMPLO = ('Madrid', 'Cataluna', 'Andalucia', 'Comunitat Valenciana')

FASES_CHECKLIST = {
    'F1': 'Antes de firmar nada: viabilidad del local',
    'F2': 'Sociedad, altas fiscales y proyecto tecnico',
    'F3': 'Registro sanitario y comunicacion autonomica',
    'F4': 'Obra, clima y equipamiento',
    'F5': 'APPCC, alergenos y formacion',
    'F6': 'Apertura: fiscal, laboral y comercial',
}

CHECKLIST_LEGAL = [
    # (fase, tramite, responsable, plazo dias, coste, fuente, cambia por CCAA, nota)
    ('F1', 'Comprobar en el planeamiento si el uso admite obrador o solo comercio',
     'Promotor', 10, None, 'supuesto', True,
     'SUPUESTO: la clasificacion urbanistica de un obrador no tiene fuente verificada. '
     'Va como PREGUNTA al ayuntamiento, nunca como afirmacion.'),
    ('F1', 'Comprobar que ningun ayuntamiento puede exigirte licencia previa de actividad',
     'Promotor', 5, None, 'CHN-49 + CHN-49b', False,
     'Para las actividades del Anexo de la Ley 12/2012 en establecimientos permanentes '
     'de hasta 750 m2 de superficie util de exposicion y venta al publico, NINGUNA '
     'administracion puede exigir licencia previa de instalacion, funcionamiento o '
     'actividad (`CHN-49`), y el Anexo incluye el grupo 644 completo, con el 644.5 de '
     'bombones y caramelos (`CHN-49b`). OJO: la chocolateria de TAZA queda fuera, '
     'porque el Anexo no contiene ningun grupo de la agrupacion 67 (`CHN-49c`). Y esta '
     'PROHIBIDO decir que tramite pide Madrid o Barcelona.'),
    ('F1', 'Comprobar que el DB-HS 3 del CTE NO regula tu local y que lo que manda es el RITE',
     'Promotor', 5, None, 'CHN-45 + CHN-46', False,
     'Un obrador de chocolate NO genera aire AE4 (`CHN-46`) y el DB-HS 3 del CTE no '
     'regula la ventilacion de un local comercial (`CHN-45`): las reglas de chimenea '
     'que circulan son las de las viviendas. Lo que si aplica es el RITE, por la '
     'climatizacion.'),
    ('F1', 'Verificar que caben las seis zonas con marcha adelante y los dos aseos',
     'Promotor', 5, None, 'supuesto', False,
     'Es una de las eliminatorias de la ficha de visita del libro 1.'),
    ('F1', 'Pedir al instalador la potencia frigorifica ofertada y las preguntas de la ficha',
     'Promotor', 15, None, 'supuesto', False,
     'El libro 1 NO calcula carga termica (D33): compara tu temperatura objetivo, la '
     'exterior de agosto de tu ciudad y la potencia que te OFREZCAN, y te da la ficha '
     'de preguntas.'),

    ('F2', 'Constituir la sociedad o darse de alta como autonomo', 'Promotor', 20, 600.0,
     'supuesto', False,
     'Importa para Verifactu: sociedad, 1-ene-2027; autonomo, 1-jul-2027 (`CHN-75`). '
     'NO es 2026.'),
    ('F2', 'Alta censal (modelo 036) con los DOS codigos CNAE', 'Gestoria', 3, None,
     'CHN-74 + CHN-74b', False,
     'CNAE-2025: 10.82 «Fabricacion de cacao, chocolate y productos de confiteria» y '
     '47.24 «Comercio al por menor de pan, productos de panaderia y confiteria» '
     '(`CHN-74`). Y al darte de alta HOY comunicas DOS codigos, no uno: el CNAE-2025 y '
     'ademas el CNAE-2009 mientras no entre en vigor la tarifa de primas adaptada '
     '(`CHN-74b`).'),
    ('F2', 'Alta en el epigrafe 644.5 del IAE, con su nota literal delante',
     'Gestoria', 3, None, 'CHN-72 + CHN-73 + CHN-94', False,
     'El 644.5 «Comercio al por menor de bombones y caramelos» FACULTA para fabricar '
     'bombones en el propio establecimiento «siempre que su comercializacion se realice '
     'en las propias dependencias de venta» (`CHN-72`). Alta si, pago casi nunca: hay '
     'exencion por cifra de negocio (`CHN-73`). Y la Regla 4.a.1 dice que una cuota '
     'faculta EXCLUSIVAMENTE para su actividad (`CHN-94`): de ahi salen las cinco filas '
     'de canal.'),
    ('F2', 'Alta en el regimen correspondiente de la Seguridad Social', 'Gestoria', 3,
     None, 'supuesto', False, ''),
    ('F2', 'Encargar el proyecto tecnico visado', 'Ingenieria', 30, 4500.0, 'supuesto', False,
     'Coste SUPUESTO: `CHN-50` esta en EXCLUIDOS. Es el documento del que cuelga todo '
     'lo demas.'),
    ('F2', 'Firmar el arrendamiento y depositar la fianza', 'Promotor', 5, 2600.0,
     'supuesto', True,
     'El deposito de la fianza se hace en el organismo de vivienda de tu comunidad y el '
     'plazo cambia en cada una.'),

    ('F3', 'Presentar la comunicacion o declaracion responsable al registro autonomico',
     'Promotor', 15, 120.0, 'CHN-39 + CHN-43', True,
     'El minorista esta EXCLUIDO del RGSEAA y se inscribe en el registro de su comunidad '
     'mediante comunicacion o declaracion responsable QUE NO HABILITA (`CHN-39`). Y el '
     'mismo tramite funciona distinto: en Madrid se presenta simultaneamente al inicio '
     'de la actividad y no habilita; en la Comunitat Valenciana es condicion unica y '
     'suficiente para iniciar y lleva tasa (`CHN-43`). PROHIBIDO escribir «necesitas el '
     'RGSEAA para abrir».'),
    ('F3', 'Resolver el arbol: tener obrador NO te saca de minorista',
     'Promotor', 5, None, 'CHN-40 + CHN-40b', False,
     'Tener obrador NO te saca del regimen minorista (`CHN-40b`). La clave y las '
     'actividades del RGSEAA solo entran cuando SI toca (`CHN-40`).'),
    ('F3', 'Resolver los TRES semaforos del art. 3 si suministras a otros minoristas',
     'Promotor', 5, None, 'CHN-41', False,
     'PUERTA DE ENTRADA: ¿suministras a otros minoristas de DISTINTA TITULARIDAD? Si la '
     'respuesta es no, el art. 3 no te aplica. Si es si, tres semaforos INDEPENDIENTES '
     'y ACUMULATIVOS: MARGINAL por la via a) hasta el 25 % del volumen anual O por la b) '
     'hasta 500 kg/semana -son dos entradas distintas-; LOCALIZADO, misma zona de salud '
     'o hasta 50 km en el caso interautonomico; RESTRINGIDO, que ninguno de tus clientes '
     'este inscrito en el RGSEAA. PROHIBIDO «los 500 kg incluyen el mostrador».'),
    ('F3', 'Comprobar si tu comunidad ha ampliado la lista del art. 13.8 por la letra e)',
     'Promotor', 10, None, 'CHN-44 + CHN-44-int + CHN-44b', True,
     'La lista estatal del obrador en vivienda tiene CINCO letras y la quinta es '
     'ABIERTA: «otros alimentos que las autoridades competentes de las comunidades '
     'autonomas permitan en sus territorios» (`CHN-44`). Por defecto el chocolate no '
     'encaja en la letra b), pero eso es INTERPRETACION DECLARADA (`CHN-44-int`), no '
     'nivel A: compruebalo en tu comunidad. La letra b) valenciana anade «confiteria», '
     'NO «chocolate» (`CHN-44b`). PROHIBIDO «hacer bombones en casa para vender es '
     'ilegal en Espana». Y el tope de 100 kg/semana del art. 13.9 solo se activa si '
     'esta casilla esta en «si»: son TRES requisitos, no uno -volumen PROPORCIONAL AL '
     'TAMANO DE LAS INSTALACIONES, tope de 100 kg/semana y demostrable documentalmente- '
     'y el que de verdad limita es el primero (`PA-29c`, reutilizado de Pasteleria y '
     'verificado el 10-09-2026).'),

    ('F4', 'Contratar la obra y la adecuacion', 'Promotor', 45, 28500.0, 'supuesto', False,
     'Coste SUPUESTO. Sin humos, la obra de un obrador de chocolate es mas barata que '
     'la de una pasteleria.'),
    ('F4', 'Contratar la climatizacion con deshumidificacion', 'Promotor', 40, 7600.0,
     'supuesto', False,
     'La partida que nadie presupuesta y la que decide si la cobertura cristaliza.'),
    ('F4', 'Pedir el equipamiento de templado con su plazo por escrito',
     'Promotor', 70, None, 'CHS-41a + CHS-42a + supuesto', False,
     'ES EL PLAZO QUE MUEVE LA FECHA DE APERTURA. Se teclea en el libro 9 y viaja al '
     'cronograma del 8 por celda verde con fila de cuadre (cruce 8 <- 9).'),
    ('F4', 'Inscribirse en el Registro territorial del impuesto al plastico si te toca',
     'Gestoria', 15, None, 'CHN-62 + CHN-62b', False,
     'Solo si FABRICAS, IMPORTAS o haces ADQUISICION INTRACOMUNITARIA de envases no '
     'reutilizables con plastico. La exencion del art. 75.f) (5 kg/mes) cubre solo la '
     'importacion y la adquisicion intracomunitaria, y solo los envases del art. '
     '68.1.a): NO la fabricacion, NI los semielaborados, NI los cierres (`CHN-62b`).'),
    ('F4', 'Si hay freidora de gas en la variante de taza, programar la inspeccion',
     'Promotor', 10, None, 'CHN-48', False,
     'Inspeccion periodica obligatoria de la instalacion receptora CADA CINCO ANOS, que '
     'en instalaciones de hasta 70 kW incluye los aparatos y comprueba la ventilacion y '
     'el volumen minimo del local (`CHN-48`).'),

    ('F5', 'Redactar el plan de APPCC con RESPONSABLE DESIGNADO CON NOMBRE',
     'Promotor', 20, None, 'CHN-32', False,
     'El procedimiento permanente basado en el APPCC puede aplicarse de manera '
     'SIMPLIFICADA conforme a la Comunicacion 2020/C 199/01, pero debe contar con una '
     'persona responsable de su aplicacion (`CHN-32`). En el APPCC va la vida util que '
     'TU declaras (`CHN-30`).'),
    ('F5', 'Montar el registro de formacion del personal', 'Promotor', 10, None,
     'CHN-69', False,
     'EL CARNET DE MANIPULADOR NO EXISTE. La obligacion viva es del empresario: '
     'garantizar la formacion de cada persona de acuerdo con su actividad laboral y '
     'PODER ACREDITARLA (`CHN-69`). PROHIBIDO escribir «hay que sacarse el carnet de '
     'manipulador».'),
    ('F5', 'Montar la declaracion de los OCHO alergenos y el protocolo de limpieza',
     'Promotor', 10, None, 'CHN-34b + CHN-33 + CHN-89', False,
     'OCHO, no cinco (`CHN-34b`). El equipo usado con un alergeno no se reutiliza para '
     'otro alimento sin limpiarlo (`CHN-33`). En producto sin envasar los alergenos '
     'pueden ir en cartel, pero la fecha no (`CHN-89`).'),
    ('F5', 'Decidir por referencia si va ENVASADA CON ETIQUETA o A GRANEL',
     'Promotor', 5, None, 'CHN-30 + CHN-35 + CHN-36 + CHN-87', False,
     'NO ES EL MISMO REGIMEN (D47). Con etiqueta te obliga lo que tu has escrito en '
     'ella (art. 4.2 del RD 1021/2022) mas las doce menciones del art. 9.1 del Rgto. '
     '1169/2011 (`CHN-35`) y el lote, que viene del RD 1808/1991 y NO de ese reglamento '
     '(`CHN-36`). A granel, la referencia es TU sistema de autocontrol.'),
    ('F5', 'Decidir si necesitas analitica de cadmio y con que frecuencia',
     'Promotor', 15, None, 'CHN-16 + CHN-16b + CHN-84', False,
     'LO QUE ES CHOCOLATE PARA LA DENOMINACION NO LO ES PARA LOS CONTAMINANTES: la nota '
     '(14) del Anexo I del Rgto. 2023/915 remite SOLO a los puntos 2, 3 y 4 de la parte '
     'A del Anexo I de la Directiva 2000/36/CE -cacao en polvo, chocolate y chocolate '
     'con leche- (`CHN-16b`). El BOMBON NO TIENE LIMITE PROPIO DE CADMIO: se le aplica '
     'la regla de alimentos compuestos del art. 3 (`CHN-84`). PROHIBIDO «tu bombon '
     'tiene un limite de cadmio de X».'),
    ('F5', 'Resolver tu papel en la cadena EUDR y pedir los papeles que te toquen',
     'Promotor', 20, None, 'CHN-20 + CHN-21 + CHN-22 + CHN-23 + CHN-24 + CHN-25', False,
     'El Anexo I incluye la partida 1806 «Chocolate y demas preparaciones alimenticias '
     'que contengan cacao», y el reglamento cubre tambien la EXPORTACION (`CHN-20`, '
     '`CHN-60`). Fecha general: 30 de diciembre de 2026 (`CHN-21`). El aplazamiento a '
     '30-06-2027 del art. 38.3 es SOLO para «operadores» persona fisica, microempresa o '
     'pequena empresa establecidos a 31-12-2024, y el art. 2.15 excluye de esa palabra '
     'a los operadores posteriores (`CHN-22`, `CHN-23`). VERIFICADO A 12-09-2026: '
     'comprueba el estado del EUDR antes de comprar cacao.'),

    ('F6', 'Comprobar que tu comunicacion sanitaria esta presentada antes de vender',
     'Promotor', 3, None, 'CHN-39', True, ''),
    ('F6', 'Contratar al equipo con el convenio que TE toca, identificado en el REGCON',
     'Gestoria', 15, None, 'CHN-65 + CHN-65c + CHN-66 + CHN-93', True,
     'NO EXISTE convenio estatal del chocolate (`CHN-66`). La tabla que trae el producto '
     'es la de Madrid y va MARCADA COMO EJEMPLO. Busca el tuyo por AMBITO FUNCIONAL, no '
     'por el nombre que te suene: la denominacion oficial del de Madrid es '
     '«CONFITERIAS PASTELERIAS Y REPOSTERIA (COMERCIO E INDUSTRIA)» y quien busque '
     '«bollerias» no lo encuentra (`CHN-65c`). Cuatro convenios de sector nombran '
     'chocolates o bombones (`CHN-93`).'),
    ('F6', 'Montar el registro de jornada', 'Gestoria', 5, None, 'CHN-68', False, ''),
    ('F6', 'Comprobar tu libertad horaria y decidir si abres en domingo',
     'Promotor', 3, None, 'CHN-77', True,
     'Una bomboneria NO esta en la lista del art. 5.1 de la Ley 1/2004 -que nombra '
     '«pasteleria y reposteria, pan, platos preparados, prensa, combustibles y '
     'carburantes, floristerias y plantas»-: le viene por el art. 5.2, establecimientos '
     'de venta de reducida dimension de menos de 300 m2 (`CHN-77`). PROHIBIDO decir que '
     'le viene por el 5.1, y prohibido «hay que pedir permiso para abrir en domingo».'),
    ('F6', 'Comprobar la accesibilidad del local', 'Promotor', 10, None, 'CHN-78', False, ''),
    ('F6', 'Decidir si publicas precios anteriores, y con la regla de los 30 dias delante',
     'Promotor', 3, None, 'CHN-76', False,
     'Subir en noviembre para «rebajar» en diciembre NO cumple la regla de los 30 dias '
     'del art. 20 de la LEY 7/1996 en la redaccion del RDL 24/2021 (`CHN-76`) - que NO '
     'es el art. 20 del TRLGDCU. Por eso este producto sale SIN precio tachado.'),
    ('F6', 'Si sirves taza y tienes mesas, facilitar que el cliente se lleve lo que no consume',
     'Promotor', 3, None, 'CHN-64 + CHN-92', False,
     'El art. 6.6 de la Ley 1/2025 EXCLUYE a las microempresas de las obligaciones de '
     'TODOS los apartados anteriores del art. 6 -plan, convenios de donacion, jerarquia- '
     '(`CHN-64`). Lo que sigue en pie no es una obligacion tuya: es que cualquier '
     'clausula contractual que prohiba donar es nula de pleno derecho. PERO la exclusion '
     'NO alcanza al ART. 8 (`CHN-92`), que obliga a las empresas de hosteleria y otros '
     'proveedores de servicios alimentarios a facilitar que el consumidor se lleve lo '
     'que no ha consumido. PROHIBIDAS las dos frases: «te siguen obligando el 6.2 y el '
     '6.5» y «no te obliga nada de la ley de desperdicio».'),
]

#: LA FILA NUEVA OBLIGATORIA DE D19: canal -> ¿te saca de la nota del 644.5?
#: Se construye desde `CANALES` para que no haya dos listas de canales. La salida es
#: si / no / no lo se MAS la pregunta redactada para el asesor. LA HOJA NO EMITE UN
#: EPIGRAFE DE IAE POR CANAL: ninguna fuente lo da.
def filas_canal_644_5():
    filas = []
    for c in CANALES:
        filas.append({
            'canal': c['canal'],
            'sale_de_la_nota': c['sale_de_la_nota_644_5'],
            'nota_literal_644_5': NOTA_644_5,
            'pregunta_al_asesor': PREGUNTA_AL_ASESOR.replace('[CANAL]', c['canal']),
            'fuente': c['fuente_legal'],
        })
    return filas


#: LA FILA DE D10 (B-6): artesania alimentaria. Es una acreditacion VOLUNTARIA, y
#: esta PROHIBIDO escribir que sin ella no puedes llamarte artesanal.
FILA_ARTESANIA = {
    'pregunta': '¿Vas a inscribirte como artesano alimentario? (comunidad autonoma + enlace)',
    'respuesta': '',
    'es_voluntaria': True,
    'fuente': 'CHN-52 + CHN-53',
    'nota': ('Cataluna tiene articulado con el chocolate dentro: su repertorio de '
             'artesania alimentaria incluye «Pasteleria: elaboracion de productos de '
             'confiteria, pasteleria, bolleria y reposteria, INCLUIDOS TURRONES Y '
             'CHOCOLATES» (`CHN-52`). Es una ACREDITACION VOLUNTARIA y queda PROHIBIDO '
             'escribir que sin ella no puedes llamarte artesanal. Y queda PROHIBIDO '
             'usar ese decreto como prueba de que es «reposteria» para el RD 1021/2022: '
             'es otro registro, otra competencia y otro fin. «Chocolate artesano» no '
             'tiene definicion estatal: «artesano», «artesanal» y «casero» tienen CERO '
             'ocurrencias en el RD 1055/2003 y en el RD 496/2010 (`CHN-53`). En el '
             'resto de comunidades, enlace a su registro.')}


# ==========================================================================
# 25. CRONOGRAMA Y RUTA CRITICA (libro 8)
# ==========================================================================
#: Duraciones en MESES, no en dias laborables: el Gantt se calcula con ARITMETICA DE
#: INDICES DE MES porque `NETWORKDAYS` esta prohibida en toda la familia. Todas las
#: duraciones son SUPUESTOS; lo que NO lo es son los plazos de entrega de maquinaria,
#: que el lector teclea en el libro 9 y viajan al 8 por celda verde con fila de cuadre.
#:
#: El proyecto arranca en OCTUBRE del ano anterior para que la apertura caiga el 1 de
#: junio: mes «Media» del calendario del kit, con seis meses de rodaje antes de Navidad
#: y con el valle de agosto dentro del arranque, que es cuando sale barato.
MES_INICIO_PROYECTO = 10     # octubre del ano anterior
GANTT = [
    # (id, hito, duracion en meses, dependencias)
    ('H1',  'Busqueda y cribado de local',                              2.0, ()),
    ('H2',  'Firma del arrendamiento y fianza',                         0.5, ('H1',)),
    ('H3',  'Proyecto tecnico visado',                                  1.0, ('H2',)),
    ('H4',  'Declaracion responsable de actividad (no licencia previa)', 1.0, ('H3',)),
    ('H5',  'Obra y adecuacion del local',                              1.5, ('H4',)),
    ('H6',  'Pedido y entrega del equipamiento de templado',            2.5, ('H3',)),
    ('H7',  'Climatizacion y deshumidificacion',                        1.0, ('H5',)),
    ('H8',  'Montaje y puesta en marcha del equipamiento',              0.5, ('H6', 'H7')),
    ('H9',  'Comunicacion al registro sanitario autonomico',            0.5, ('H8',)),
    ('H10', 'Plan de APPCC, alergenos y registro de formacion',         0.5, ('H8',)),
    ('H11', 'Contratacion del equipo y altas en Seguridad Social',      0.5, ('H8',)),
    ('H12', 'Pruebas de templado y cierre de la carta de apertura',     0.5, ('H9', 'H10', 'H11')),
    ('H13', 'Apertura',                                                 0.0, ('H12',)),
]
FUENTE_GANTT = 'supuesto'


def ruta_critica():
    """(fin en meses, camino critico, dict de holguras por hito). Aritmetica de
    indices de mes, sin funciones de fecha: es lo que despues se traduce a formulas en
    la hoja «Cronograma y Ruta Critica» del libro 8."""
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
    holgura = {}
    for hid in dur:
        sucesores = [h for h in deps if hid in deps[h]]
        limite = min([inicio[s] for s in sucesores]) if sucesores else total
        holgura[hid] = round(limite - fin[hid], 2)
    return total, camino, holgura


def mes_apertura_calculado():
    """Mes natural en el que cae la apertura arrancando en `MES_INICIO_PROYECTO`."""
    total, _camino, _h = ruta_critica()
    return ((MES_INICIO_PROYECTO - 1 + int(total)) % 12) + 1


def cuadre_plazo_maquinaria():
    """El septimo cruce, calculado: si la ruta critica es MAS CORTA que el plazo de
    entrega del equipo critico, la fecha de apertura la manda la maquinaria y el
    semaforo del libro 8 avisa. Devuelve (meses de ruta critica, meses de plazo, avisa)."""
    total, _c, _h = ruta_critica()
    plazo_meses = plazo_critico_semanas() / 4.33
    return total, plazo_meses, plazo_meses > total


# ==========================================================================
# 26. NOTAS LEGALES: nota_legal() y gate_legal()
# ==========================================================================
#: REGLA 1 DE §2.3: *cada celda con un dato legal lleva nota «Verificado el
#: 12-09-2026 · norma y articulo · URL»*. Esa nota NO se escribe a mano en ningun
#: constructor: se pide aqui, y aqui se lee del fichero de la verificacion legal
#: independiente, que es la fuente de verdad de lo legal y MANDA sobre la sintesis y
#: sobre la lente L3, sin excepcion.
VERIFICACION_LEGAL_JSON = os.path.join(
    _AUDIT, 'guia-chocolateria-verificacion-legal-2026-09-12.json')
VERIFICACION_LEGAL_MD = os.path.join(
    _AUDIT, 'guia-chocolateria-verificacion-legal-2026-09-12.md')
VERIFICACION_LEGAL_EXCLUIDOS = os.path.join(
    _AUDIT, 'guia-chocolateria-verificacion-legal-2026-09-12-EXCLUIDOS.json')

#: El JSON comun, del que salen las cifras de sector y donde se fusionaron los 109
#: `CHN-*` y los 115 `CHS-*` (411 + 109 + 115 = 635).
JSON_COMUN = os.path.join(_AUDIT, 'guias-v2-research-sector.json')

_CAMPOS_NORMA = ('norma_y_articulo', 'norma_articulo', 'fuente_titulo', 'norma',
                 'articulo', 'titulo', 'asunto', 'valor_correcto', 'dato')
_CAMPOS_URL = ('url', 'fuente_url', 'enlace', 'fuente')

_LEGAL_CACHE = {'cargado': False, 'entradas': {}, 'error': None}
_COMUN_CACHE = {'cargado': False, 'ids': set(), 'entradas': {}, 'error': None}


def _carga_verificacion_legal():
    """Carga (una vez) el JSON de la verificacion legal. Tolerante con la forma: lista
    de entradas con `id`, o dict indexado por id, o dict con la lista dentro de una
    clave. Si el fichero no existe, no revienta: deja el error anotado."""
    if _LEGAL_CACHE['cargado']:
        return _LEGAL_CACHE
    _LEGAL_CACHE['cargado'] = True
    if not os.path.exists(VERIFICACION_LEGAL_JSON):
        _LEGAL_CACHE['error'] = ('No existe %s.' % VERIFICACION_LEGAL_JSON)
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
        _LEGAL_CACHE['error'] = '%s no trae ninguna entrada con `id`.' % VERIFICACION_LEGAL_JSON
    return _LEGAL_CACHE


def _carga_json_comun():
    """Carga (una vez) el JSON comun de 635 entradas. Es el que hace cumplir D44: un
    id de sector escrito SIN su sufijo no existe, y `verificar_guion.py` lo caza
    despues de gastar la redaccion. Aqui se caza antes."""
    if _COMUN_CACHE['cargado']:
        return _COMUN_CACHE
    _COMUN_CACHE['cargado'] = True
    if not os.path.exists(JSON_COMUN):
        _COMUN_CACHE['error'] = 'No existe %s.' % JSON_COMUN
        return _COMUN_CACHE
    try:
        fh = open(JSON_COMUN, 'rb')
        try:
            crudo = json.loads(fh.read().decode('utf-8'))
        finally:
            fh.close()
    except Exception as e:                                    # noqa: BLE001
        _COMUN_CACHE['error'] = 'No se pudo leer %s: %s' % (JSON_COMUN, e)
        return _COMUN_CACHE
    datos = crudo.get('datos') if isinstance(crudo, dict) else crudo
    for fila in datos or []:
        if isinstance(fila, dict) and fila.get('id'):
            _COMUN_CACHE['ids'].add(str(fila['id']).strip())
            _COMUN_CACHE['entradas'][str(fila['id']).strip()] = fila
    return _COMUN_CACHE


def _primer_campo(fila, campos):
    for c in campos:
        v = fila.get(c)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None


def nota_legal(id_chn):
    """Nota de celda para un dato legal, o `None` si no se puede construir.

    Devuelve: «Verificado el 12-09-2026 · <norma y articulo> · <URL>»

    Devuelve `None` -y no revienta- si el JSON de la verificacion legal no existe o
    si el id no esta en el. Los constructores llaman antes a `gate_legal()`, que es
    quien aborta.
    """
    cache = _carga_verificacion_legal()
    fila = cache['entradas'].get(str(id_chn).strip())
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
    norma = re.sub(r'\s+', ' ', norma).strip()
    if len(norma) > 220:
        norma = norma[:217].rstrip() + '...'
    return 'Verificado el %s %s %s %s %s' % (
        FECHA_VERIFICACION_LEGAL, chr(183), norma, chr(183), url)


#: Los ids `CHN-*` que citan los libros 4, 5, 8 y 9 segun la SPEC (§2.2, §3.5 y §5.1),
#: mas los que este propio juego de datos usa. Los constructores llaman a
#: `gate_legal(IDS_LEGALES_REQUERIDOS)` ANTES de escribir una sola nota: la
#: alternativa es un xlsx publicado con una celda legal sin fuente.
IDS_LEGALES_REQUERIDOS = {
    # --- libro 4: carta de apertura, denominaciones y escandallo ----------
    'CHN-01': ('Ambito del RD 1055/2003: tiene ARTICULO UNICO, nunca «el articulo 6»', 4),
    'CHN-02': ('Tabla completa de minimos por denominacion (aps. 1.1 a 1.13 y 6.g)', 4),
    'CHN-03': ('Bombon de chocolate: 25 % sobre el peso total', 4),
    'CHN-03b': ('Praline, trufa, artesano, artesanal y casero: 0 ocurrencias en el RD', 4),
    'CHN-04': ('Chocolate relleno: 25 % de exterior y exclusiones', 4),
    'CHN-05': ('Chocolate a la taza: 35/18/14 y la mencion «para su consumo cocido»', 4),
    'CHN-06': ('Grasas vegetales distintas de la manteca de cacao', 4),
    'CHN-06b': ('Formato exacto de la mencion de grasas vegetales', 4),
    'CHN-07': ('A que denominaciones obliga la mencion «cacao: X % minimo»', 4),
    'CHN-08': ('Calificativos de calidad: la norma NO da lista de palabras', 4),
    'CHN-09': ('Ingredientes anadidos: tope del 40 % y prohibiciones', 4),
    'CHN-10': ('LAS DOS BASES DE CALCULO, y la del bombon es el peso TOTAL', 4),
    'CHN-11': ('Sucedaneos de chocolate', 4),
    'CHN-12': ('Remision de etiquetado obsoleta: NO remitir al RD 1334/1999', 4),
    'CHN-13': ('Denominaciones obligatorias y cajas surtidas (ap. 6.a y 6.c)', 4),
    'CHN-15': ('RD 348/2011: grageas, confites y fruta banada', 4),
    'CHN-15b': ('Reconocimiento mutuo del RD 348/2011', 4),
    'CHN-81': ('Armonizacion total de la Directiva 2000/36/CE', 4),
    'CHN-82': ('«Praline» ES denominacion de venta europea', 4),
    'CHN-83': ('«Para su consumo cocido» es una adicion espanola', 4),
    'CHN-71': ('IVA del chocolate: 10 % por exclusion, no por mencion', 4),
    'CHN-71c': ('IVA de la taza servida en sala', 4),
    # --- libro 5: vida util, aw, etiqueta o granel, vitrina ---------------
    'CHN-30': ('NO hay temperatura legal del chocolate: la declaras tu en tu APPCC', 5),
    'CHN-30b': ('Frontera: la tarta de chocolate SI entra en la fila 9', 5),
    'CHN-31': ('Huevo crudo: las tres vias del art. 9', 5),
    'CHN-33': ('Alergenos y limpieza de equipo', 5),
    'CHN-34b': ('LOS OCHO ALERGENOS: cacahuete, frutos de cascara y sesamo son tres entradas', 5),
    'CHN-35': ('Las doce menciones del art. 9.1: el lote NO esta entre ellas', 5),
    'CHN-36': ('Lote: RD 1808/1991, la letra L y sus tres exenciones', 5),
    'CHN-37': ('«Sin gluten»: umbral analitico de 20 mg/kg', 5),
    'CHN-38': ('Congelacion: -18 grados C, etiqueta y prohibicion de recongelar', 5),
    'CHN-87': ('El RD 1021/2022 no nombra el chocolate ni una vez', 5),
    'CHN-88': ('Transporte al consumidor final', 5),
    'CHN-89': ('Los alergenos pueden ir en cartel, la fecha no', 5),
    # --- libro 8: checklist legal, licencias, cadmio, EUDR y cronograma ---
    'CHN-16': ('Cadmio en productos de cacao y chocolate', 8),
    'CHN-16b': ('Que es «producto de cacao y de chocolate» a efectos de cadmio', 8),
    'CHN-84': ('El bombon NO tiene limite propio de cadmio', 8),
    'CHN-17': ('Ocratoxina A', 8),
    'CHN-18': ('HAP en grano de cacao y en fibra de cacao', 8),
    'CHN-19': ('Las tres obligaciones del operador en contaminantes', 8),
    'CHN-20': ('EUDR: el chocolate terminado (partida 1806) esta dentro', 8),
    'CHN-21': ('EUDR: fecha general, 30 de diciembre de 2026', 8),
    'CHN-22': ('EUDR: el aplazamiento del art. 38.3 es para OPERADORES', 8),
    'CHN-23': ('EUDR: la figura de «operador posterior» (art. 2.15 ter)', 8),
    'CHN-25': ('EUDR: que exige al operador que importa grano', 8),
    'CHN-27': ('EUDR: el regimen simplificado NO es para el importador pequeno', 8),
    'CHN-28': ('EUDR: autoridad competente en Espana (nivel B, NO se entrecomilla)', 8),
    'CHN-29': ('EUDR: regla de inventario', 8),
    'CHN-60': ('EUDR: exportar tambien esta sujeto', 8),
    'CHN-85': ('EUDR: la pyme no se registra ni verifica', 8),
    'CHN-32': ('APPCC simplificado CON RESPONSABLE DESIGNADO', 8),
    'CHN-39': ('El minorista esta EXCLUIDO del RGSEAA', 8),
    'CHN-40': ('Clave y actividades del RGSEAA para el chocolate', 8),
    'CHN-40b': ('Tener obrador NO te saca del regimen minorista', 8),
    'CHN-41': ('Marginal, localizado y restringido: los tres son ACUMULATIVOS', 8),
    'CHN-42': ('Obrador central y sucursales', 8),
    'CHN-43': ('El mismo tramite funciona distinto por comunidad autonoma', 8),
    'CHN-44': ('Las CINCO letras del art. 13.8, y la e) es abierta', 8),
    'CHN-44-int': ('INTERPRETACION DECLARADA: el chocolate y la letra b)', 8),
    'CHN-44b': ('La letra b) valenciana anade «confiteria», no «chocolate»', 8),
    'CHN-45': ('El DB-HS 3 del CTE no regula un local comercial', 8),
    'CHN-46': ('El obrador de chocolate no genera aire AE4', 8),
    'CHN-47': ('Tostado de cacao y CAPCA: «cafe o similares» es INTERPRETACION', 8),
    'CHN-47b': ('La nota (2) del CAPCA incluye los NUCLEOS DE POBLACION', 8),
    'CHN-48': ('Gas: inspeccion cada cinco anos', 8),
    'CHN-49': ('Ninguna licencia previa de actividad hasta 750 m2', 8),
    'CHN-49b': ('El epigrafe 644.5 esta en el Anexo de la Ley 12/2012', 8),
    'CHN-49c': ('La chocolateria de taza NO entra en la Ley 12/2012', 8),
    'CHN-52': ('Cataluna incluye el chocolate en la artesania alimentaria', 8),
    'CHN-53': ('«Chocolate artesano» no tiene definicion estatal', 8),
    'CHN-62': ('Impuesto al plastico: quien lo paga y cuanto', 8),
    'CHN-62b': ('La exencion de 5 kg/mes tiene DOS limites', 8),
    'CHN-62c': ('Los moldes de policarbonato NO pagan el impuesto', 8),
    'CHN-64': ('Ley 1/2025: la microempresa queda fuera del art. 6 ENTERO', 8),
    'CHN-92': ('El art. 8 de la Ley 1/2025 NO queda excluido por el 6.6', 8),
    'CHN-65': ('Convenio de Madrid: la fabricacion de bombones va condicionada', 8),
    'CHN-65b': ('Tablas salariales 2026 del convenio de Madrid', 8),
    'CHN-65c': ('Datos oficiales del convenio de Madrid en REGCON', 8),
    'CHN-66': ('NO existe convenio estatal del chocolate', 8),
    'CHN-93': ('Los cuatro convenios de sector que SI nombran el chocolate', 8),
    'CHN-67': ('SMI 2026: caduca el 31-12-2026, vive en el anexo', 8),
    'CHN-68': ('Registro de jornada', 8),
    'CHN-69': ('El «carnet de manipulador» no existe: registro de formacion', 8),  # LN-OK
    'CHN-72': ('Epigrafe 644.5 y SU NOTA LITERAL, que es la que lo limita', 8),
    'CHN-73': ('IAE: alta si, pago casi nunca', 8),
    'CHN-74': ('CNAE-2025: los codigos del chocolate', 8),
    'CHN-74b': ('Al darte de alta hoy comunicas DOS codigos, no uno', 8),
    'CHN-75': ('Verifactu no es 2026, es 2027', 8),
    'CHN-76': ('Precio anterior: los 30 dias, y es la Ley 7/1996, NO el TRLGDCU', 8),
    'CHN-77': ('Libertad horaria: le viene por el art. 5.2, NO por el 5.1', 8),
    'CHN-78': ('Accesibilidad', 8),
    'CHN-94': ('Regla 4.a.1: una cuota faculta SOLO para su actividad', 8),
    'CHN-95': ('Regla 4.a.2.D): la venta online al consumidor ES minorista', 8),
    'CHN-96': ('El epigrafe industrial faculta para mayor y menor', 8),
    'CHN-71b': ('Talleres y catas: NO exentos de IVA, y el TIPO va SIN CIFRA', 8),
    'CHN-51': ('Degustacion y comidas preparadas', 8),
    'CHN-55': ('«ELABORACION PROPIA»', 8),
    'CHN-63': ('Taper del cliente y bebida reutilizable', 8),
    'CHN-91': ('Cataluna: umbral ambiental de un obrador vegetal', 8),
    # --- libro 9: equipamiento, proveedores y clientes --------------------
    'CHN-24': ('EUDR art. 5.3: el nº de DDS SOLO si el proveedor es operador, y la '
               'tabla de CLIENTES del 5.3.b)', 9),
    'CHN-26': ('EUDR: el numero de referencia lo comunica el operador', 9),
    'CHN-56': ('Vender online a toda Espana no rompe «localizado»', 9),
    'CHN-57': ('Venta a distancia: informacion ANTES de pagar', 9),
    'CHN-59': ('Vender online te convierte en envasador', 9),
    'CHN-61': ('Envases de servicio: quien se inscribe', 9),
    'CHN-86': ('EUDR: hay una rectificacion en el consolidado', 9),
}

#: El unico id que NO es `CHN-*` y que sostiene una salida del libro 8: el tope de
#: 100 kg/semana del art. 13.9. Ninguna ficha `CHN-*` lo cubre, y por eso la SPEC
#: declara una CUARTA procedencia valida: un id `PA-*` del mismo JSON comun, citado
#: como REUTILIZACION de Pasteleria y con su fecha de verificacion (10-09-2026).
ID_REUTILIZADO_PASTELERIA = {
    'PA-29c': ('Art. 13.9: los TRES requisitos -volumen proporcional al tamano de las '
               'instalaciones, tope de 100 kg/semana y demostrable documentalmente-, '
               'reutilizado de Pasteleria y verificado el 10-09-2026', 8),
}


def gate_legal(ids_requeridos=None, abortar=True):
    """Comprueba que la verificacion legal sirve una nota para CADA id que los libros
    van a citar. Si falta alguno, ABORTA listandolos.

    Los constructores lo llaman ANTES de escribir notas. `abortar=False` devuelve la
    lista en vez de morir, para que `comprobar()` pueda informar sin tumbar el modulo.
    """
    ids = list(ids_requeridos or IDS_LEGALES_REQUERIDOS)
    cache = _carga_verificacion_legal()
    faltan = [i for i in ids if nota_legal(i) is None]
    if not faltan:
        return []
    detalle = []
    for i in faltan:
        para_que = IDS_LEGALES_REQUERIDOS.get(i, ('(sin descripcion)', '?'))[0]
        detalle.append('  - %s: %s' % (i, para_que))
    mensaje = ('gate_legal: faltan %d de %d notas legales en %s\n%s'
               % (len(faltan), len(ids), VERIFICACION_LEGAL_JSON, '\n'.join(detalle)))
    if cache['error']:
        mensaje += '\n  Motivo: %s' % cache['error']
    if abortar:
        raise SystemExit(mensaje)
    return faltan


def id_existe_en_json_comun(pid):
    """True si ese id existe LITERALMENTE en el JSON comun. Es lo que hace cumplir
    D44: `CHS-28` no existe; `CHS-28a` si."""
    return str(pid).strip() in _carga_json_comun()['ids']


def ficha(pid):
    """La entrada completa del JSON comun, o None."""
    return _carga_json_comun()['entradas'].get(str(pid).strip())


# ==========================================================================
# 27. ECONOMIA DEL ANO DE CRUCERO
# ==========================================================================
def capex_bloque_sin_iva(bloque):
    """Total de un bloque de CAPEX. Los importes a None se calculan desde
    EQUIPAMIENTO; el fondo de maniobra llega del libro 7 (cruce 2 <- 7)."""
    if bloque == 'Fondo de maniobra':
        return fondo_maniobra()
    total = 0.0
    for b, _partida, importe, _base, _tipo, _fuente, _nota in CAPEX:
        if b != bloque:
            continue
        total += importe if importe is not None else 0.0
    calculados = equipamiento_bloque_sin_iva(bloque)
    return total + calculados


def capex_sin_fondo_de_maniobra():
    """La linea que VIAJA al libro 7 (cruce 7 <- 2). NO es «el CAPEX total»: el total
    incluye el bloque «fondo de maniobra», y llevarlo entero al 7 -que vuelve a dotar
    el fondo- lo contaria dos veces."""
    return sum(capex_bloque_sin_iva(b) for b in BLOQUES_CAPEX if b != 'Fondo de maniobra')


def capex_comparable_sin_iva():
    """Los SEIS bloques comparables con un escenario de dotacion publicado. Fianza y
    licencias, packaging y moldes, y fondo de maniobra quedan fuera, enteros."""
    return sum(capex_bloque_sin_iva(b) for b in BLOQUES_COMPARABLES)


def inversion_total_sin_iva():
    """CAPEX sin el fondo MAS el fondo. Es UNA sola cifra en todo el paquete, y los
    libros 2 y 7 la publican identica POR CONSTRUCCION (cruces 7 <- 2 y 2 <- 7)."""
    return capex_sin_fondo_de_maniobra() + fondo_maniobra()


def capex_amortizable_sin_iva():
    """Todo lo que se amortiza. La FIANZA no: es un deposito que se recupera. El fondo
    de maniobra tampoco: es caja."""
    total = 0.0
    for b, partida, importe, _base, _tipo, _fuente, _nota in CAPEX:
        if b == 'Fondo de maniobra':
            continue
        if partida.startswith('Fianza de arrendamiento'):
            continue
        total += importe if importe is not None else 0.0
    for bloque in BLOQUES_CAPEX:
        if bloque != 'Fondo de maniobra':
            total += equipamiento_bloque_sin_iva(bloque)
    return total


def iva_soportado_capex():
    """El IVA que hay que ADELANTAR el dia que abres y que vuelve despues. Sin esta
    linea, el plan de tesoreria del primer trimestre esta mal por definicion."""
    total = 0.0
    for b, _partida, importe, _base, tipo, _fuente, _nota in CAPEX:
        if b == 'Fondo de maniobra':
            continue
        if importe is not None:
            total += importe * tipo
    for e in EQUIPAMIENTO:
        if e['opcional']:
            continue
        total += precio_equipamiento_sin_iva(e) * e['tipo_iva']
    return total


_FIJOS_CACHE = {}


def gastos_fijos_mensuales():
    """Total de gastos fijos de UN MES del ano de crucero. Es uno de los DOS factores
    del fondo de maniobra, y los dos viven aqui (libro 7)."""
    if 'v' in _FIJOS_CACHE:
        return _FIJOS_CACHE['v']
    total = 0.0
    for partida, importe, _fuente, _nota in GASTOS_FIJOS_MENSUALES:
        if importe is not None:
            total += importe
        elif partida.startswith('Personal'):
            total += coste_personal_anual() / 12.0
        elif partida.startswith('Amortizacion'):
            total += capex_amortizable_sin_iva() / P('anios_amortizacion') / 12.0
        elif partida.startswith('Gastos financieros'):
            total += intereses_anio_crucero() / 12.0
    _FIJOS_CACHE['v'] = total
    return total


def fondo_maniobra():
    """meses de colchon x gastos fijos mensuales. SE CALCULA UNA SOLA VEZ, aqui, con
    los dos factores del libro 7, y viaja al libro 2 YA CALCULADO (cruce 2 <- 7)."""
    return P('meses_colchon_fondo_maniobra') * gastos_fijos_mensuales()


def ventas_anuales_sin_iva():
    return (P('tickets_dia_crucero') * NEGOCIO['dias_apertura_anio']
            * ticket_medio_con_iva() / (1.0 + iva_medio_carta()))


def piezas_dia_crucero():
    return P('tickets_dia_crucero') * P('piezas_por_ticket')


def cuenta_resultados_crucero():
    ventas = ventas_anuales_sin_iva()
    variable = ventas * food_cost_servido()
    fijos = gastos_fijos_mensuales() * 12.0
    beneficio = ventas - variable - fijos
    return {'ventas_sin_iva': ventas, 'coste_variable': variable,
            'margen_contribucion': ventas - variable, 'gastos_fijos': fijos,
            'beneficio_neto': beneficio,
            'margen_neto': beneficio / ventas if ventas else 0.0}


def punto_muerto_mensual():
    mc = 1.0 - food_cost_servido()
    return gastos_fijos_mensuales() / mc if mc else 0.0


def margen_contribucion_canal(c):
    return c['margen_bruto'] - c['coste_servir_pct'] - c['comision_plataforma']


def asistentes_punto_muerto_taller():
    """Cuantas personas tiene que traer un taller para cubrir su propio coste. Usa el
    PRECIO MINIMO del rango de `CHS-30` y el coste hora de obrador como coste de
    docente, que es el criterio mas conservador."""
    t = [c for c in CANALES if c['canal'].startswith('Talleres')][0]
    coste = t['horas_docente'] * coste_hora_obrador()
    neto_persona = t['precio_persona_min'] * (1.0 - t['coste_servir_pct'])
    return coste / neto_persona if neto_persona else 0.0


# ==========================================================================
# 28. COMPROBACIONES
# ==========================================================================
#: Cifras y palabras de la lista negra del §5 de la SPEC. Si alguna aparece en el
#: modulo, es que se ha colado un dato prohibido.
#:
#: El barrido se hace sobre el CODIGO, no sobre los datos, porque un dato prohibido
#: puede colarse igual en un comentario o en una nota de celda. Eso obliga a excluir
#: dos zonas donde las agujas aparecen a proposito: el docstring del modulo (que
#: enumera lo que NO entra) y las lineas marcadas con `LN-OK`, que son menciones
#: deliberadas -«nunca escribas esto»- y no usos. Sin esa exclusion el gate se
#: denuncia a si mismo y deja de servir.
CIFRAS_PROHIBIDAS = (
    ('3.000-4.500', 'N-1: la cotizacion del cacao de la prensa latinoamericana'),  # LN-OK
    ('80.000-250.000', 'N-2: la inversion inventada de la FAQ de consultoria'),    # LN-OK
    ('6.000-18.000', 'N-2: la vitrina refrigerada de la misma FAQ'),               # LN-OK
    ('18,2 %', 'N-16: el peso de los bombones de 2022; el vigente es otro'),       # LN-OK
    ('89 unidades', 'N-5: el punto de equilibrio de CHS-40 como cifra de portada'), # LN-OK
    ('7.400', 'N-12: Selmi One a precio de tienda mexicana'),                      # LN-OK
    ('35.000 ', 'N-11: «Utopick abrio con 35.000 euros en 2014»'),                 # LN-OK
    ('45 miembros', 'N-18: la Asociacion Bean to Bar se publica como «mas de 40»'), # LN-OK
    ('125.000', 'N-10: la franquicia Valor via infofranquicias'),                  # LN-OK
    ('24.040', 'N-10: el canon de la franquicia Valor'),                           # LN-OK
    ('12 x 30', 'D23a: los moldes van como RANGO, no como multiplicacion'),        # LN-OK
    ('12 moldes', 'D23a: los moldes van como RANGO'),                              # LN-OK
    ('dulcer', 'SPEC 6: falso amigo mexicano, no se usa como sinonimo'),           # LN-OK
    ('artesana ', 'SPEC 6: la forma es «artesanal»'),                              # LN-OK
    ('re:\\btemperado\\b', 'SPEC 6: la forma del cuerpo es «templado»'),          # LN-OK
    ('valle de junio', 'D36: el valle es AGOSTO, un mes de doce'),                 # LN-OK
    ('factor 5', 'D30: el factor del kit es DE TRES A CINCO'),                     # LN-OK
    ('13 ficheros', 'D38: kit-escandallos SI tiene hoja de chocolate'),            # LN-OK
    ('carnet de manipulador', 'CHN-69: no existe desde 2010'),                     # LN-OK
    ('cinco alergenos', 'CHN-34b: son OCHO'),                                      # LN-OK
    ('maestro chocolatero', 'B.5: no es un perfil del kit'),                       # LN-OK
    ('fino', 'CHN-08: la norma NO da lista de calificativos de calidad'),          # LN-OK
    ('caja parada', 'D36: en agosto para el obrador, no la caja'),                 # LN-OK
)

#: El id de sector que esta PROHIBIDO citar aunque exista (R3-M3 y §5.2): `CHS-41` a
#: secas es un AGREGADO sin fuente unica, cifra 14 (el «factor entre extremos»),
#: fiabilidad baja. Las atemperadoras se citan una a una, con sufijo.
#: No se busca en el texto -mencionarlo para decir que se excluye es legitimo- sino
#: en los campos `fuente`, que es donde seria un uso y no una mencion.
ID_SECTOR_PROHIBIDO = 'CHS-' + '41'

#: Las once familias de ids que SOLO existen con sufijo (D44). Si alguien escribe el
#: id bare, `verificar_guion.py` lo cazaria DESPUES de gastar la redaccion; aqui se
#: caza antes.
FAMILIAS_SOLO_CON_SUFIJO = ('CHS-24', 'CHS-25', 'CHS-27', 'CHS-28', 'CHS-37', 'CHS-38',
                            'CHS-42', 'CHS-45', 'CHS-46', 'CHS-47', 'CHS-69')


def _texto_barrible(fuente_py):
    """El codigo sin el docstring del modulo y sin las lineas marcadas LN-OK."""
    cuerpo = fuente_py
    i = cuerpo.find('\"\"\"')
    if i >= 0:
        j = cuerpo.find('\"\"\"', i + 3)
        if j > i:
            cuerpo = cuerpo[:i] + cuerpo[j + 3:]
    return '\n'.join(l for l in cuerpo.split('\n') if 'LN-OK' not in l)


#: Patrones de procedencia admitidos en cualquier campo `fuente`. Son los CUATRO
#: origenes de §3 y nada mas.
_RE_FUENTE = re.compile(
    r'^(supuesto'
    r'|supuesto declarado[^+]*'
    r'|sin id verificado'
    r'|CHN-\d+[a-z]?(-int)?'
    r'|CHS-\d+[a-z]?'
    r'|PA-\d+[a-z]?'
    r'|D\d+[a-z]?'
    r'|N-\d+'
    r'|kit-tareas-chocolateria/[^!]+(![^!]+)*'
    r'|kit-escandallos/[^!]+(![^!]+)*'
    r'|motor\.PARAMETROS\[[a-z_]+\]'
    r'|planes-v2_0/[A-Za-z_./]+'
    r'|art\. [^+]+'
    r'|Se calcula[^+]*'
    r')$')


def _fuente_ok(fuente):
    """Una fuente puede ser una sola procedencia o varias unidas con ' + '."""
    if not isinstance(fuente, str) or not fuente.strip():
        return False
    for tramo in fuente.split(' + '):
        if not _RE_FUENTE.match(tramo.strip()):
            return False
    return True


def _todas_las_fuentes():
    f = [p[2] for p in PRECIOS_COMPRA.values()]
    f += [p[1] for p in PARAMS.values()]
    f += [e['fuente'] for e in EQUIPAMIENTO] + [e['fuente_plazo'] for e in EQUIPAMIENTO]
    f += [c[5] for c in CAPEX] + [t[5] for t in TRASPASOS]
    f += [t[4] for t in TRASPASOS_VARIANTE_TAZA]
    f += [c['fuente'] for c in CANALES] + [c['fuente_legal'] for c in CANALES]
    f += [x[5] for x in CHECKLIST_LEGAL]
    f += [p[3] for p in PROVEEDORES]
    f += [g[2] for g in GASTOS_FIJOS_MENSUALES]
    f += [r['fuente_pvp'] for r in CARTA] + [r['fuente_gramaje'] for r in CARTA]
    f += [r['fuente_denominacion'] for r in CARTA]
    f += [c['fuente_fila'] for c in CAMPANAS] + [c['fuente_economia'] for c in CAMPANAS]
    f += [c['fuente_precio'] for c in COBERTURAS.values()]
    f += [c['fuente_rango_cacao'] for c in COBERTURAS.values()]
    f += [c['fuente_tres_magnitudes'] for c in COBERTURAS.values()]
    f += [r['fuente_aw'] for r in RELLENOS.values()]
    f += [v['fuente'] for v in VARIANTES.values()]
    f += [x['fuente'] for x in FRANQUICIAS]
    f += [s[4] for s in SALARIOS_MERCADO]
    f += [c[3] for c in CONVENIOS_QUE_NOMBRAN_CHOCOLATE]
    f += [NEGOCIO[k] for k in NEGOCIO if k.startswith('fuente_')]
    f += [FUENTE_CONVENIO, FUENTE_CONVENIO_DENOMINACION, FUENTE_PLANTILLA,
          FUENTE_ESTACIONALIDAD, FUENTE_GANTT, FUENTE_ALERGENOS, FUENTE_CLIENTES_B2B,
          FUENTE_NOTA_644_5, FUENTE_MINIMO_25, FILA_ARTESANIA['fuente'],
          FINANCIACION['fuente'], RAMPA['fuente'], PLASTICO['fuente_tipo'],
          PLASTICO['fuente_umbral'], PLASTICO['fuente_kg_mes'],
          PLASTICO['fuente_moldes'], TRASPASO_RANGO[2], RENTA_OBSERVADA_RANGO[2],
          CAMPANA_COMUNIONES['fuente'], CAMPANA_COMUNIONES['fuente_antelacion'],
          VALLE['fuente'], ESCENARIOS_DOTACION['A']['fuente'],
          ESCENARIOS_DOTACION['B']['fuente']]
    return f


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
        fallos.append('Caracter fuera de WinAnsi (cp1252) en la posicion %d: %r'
                      % (e.start, fuente_py[max(0, e.start - 40):e.start + 40]))
    except IOError:
        avisos.append('No se pudo releer el fichero para el gate de WinAnsi')

    # ---- 1. lista negra del §5 -------------------------------------------
    barrible = _texto_barrible(fuente_py)
    for aguja, motivo in CIFRAS_PROHIBIDAS:
        # Una aguja que empieza por «re:» es una expresion regular. Existe por
        # «temperado»: la palabra esta PROHIBIDA en el cuerpo, pero «atemperadora»  # LN-OK
        # la contiene y es el nombre correcto de la maquina. Un gate que no
        # distinga las dos cosas se dispara siempre y acaba desactivado.
        if aguja.startswith('re:'):
            m_ln = re.search(aguja[3:], barrible)
            i = m_ln.start() if m_ln else -1
        else:
            i = barrible.find(aguja)
        if i >= 0:
            fallos.append('Cifra o palabra prohibida %r (%s): %r'
                          % (aguja, motivo, barrible[max(0, i - 70):i + 70]))

    fuentes = [str(f) for f in _todas_las_fuentes()]
    malas = [f for f in fuentes if re.search(r'\bCHS-41\b(?![a-z])', f)]
    exige(not malas,
          'R3-M3: `CHS-41` a secas se usa como fuente en %d sitios. Es un AGREGADO sin '
          'fuente unica (fiabilidad baja) y esta PROHIBIDO: las atemperadoras se citan '
          'CHS-41a a CHS-41j, una a una' % len(malas))
    for fam in FAMILIAS_SOLO_CON_SUFIJO:
        bare = [f for f in fuentes if re.search(r'\b%s\b(?![a-z])' % re.escape(fam), f)]
        exige(not bare,
              'D44: el id %s se usa SIN SUFIJO en %d fuentes, y en el JSON comun solo '
              'existe con sufijo' % (fam, len(bare)))
    for f in fuentes:
        exige(_fuente_ok(f), 'Fuente no reconocida (no es ninguno de los CUATRO '
                             'origenes validos de §3): %r' % f)

    # ---- 2. el negocio y las seis zonas ----------------------------------
    suma_zonas = sum(z[1] for z in ZONAS)
    exige(abs(suma_zonas - 75.0) < 1e-9,
          'Las zonas no suman los 75 m2 de §3.1: %.2f' % suma_zonas)
    exige(len(ZONAS) == 6, '§3.1 fija SEIS zonas y hay %d' % len(ZONAS))
    exige(abs(sum(BLOQUES_M2.values()) - 75.0) < 1e-9, 'Los bloques no suman 75 m2')
    for zona, m2, _f, _n in ZONAS:
        exige(zona in ZONA_A_BLOQUE, 'La zona %r no esta asignada a ningun bloque' % zona)
    for bloque, m2 in BLOQUES_M2.items():
        suma = sum(z[1] for z in ZONAS if ZONA_A_BLOQUE[z[0]] == bloque)
        exige(abs(suma - m2) < 1e-9,
              'Las zonas del bloque «%s» suman %.2f m2 y BLOQUES_M2 dice %.2f'
              % (bloque, suma, m2))
    exige(NEGOCIO['m2_total'] == 75.0, 'NEGOCIO[m2_total] ya no son 75 m2')
    exige(NEGOCIO['mes_apertura_recomendado'] == 6 and NEGOCIO['dia_apertura_recomendado'] == 1,
          'La apertura deja de ser el 1 de junio')
    exige(campana(NEGOCIO['mes_apertura_recomendado'])['temporada'] != 'Alta',
          'La apertura cae en un mes de temporada Alta del calendario del kit')

    # ---- 3. las cinco temperaturas del kit (D31) -------------------------
    exige(len(CLIMA) == 5, 'D31 fija CINCO temperaturas unicas y hay %d' % len(CLIMA))
    esperado_clima = {'obrador': (18.0, 20.0, 50.0, 60.0),
                      'camara': (15.0, 18.0, 50.0, 60.0),
                      'nevera_rellenos': (0.0, 4.0, None, None),
                      'sala_tienda': (20.0, 22.0, None, None),
                      'vitrina': (16.0, 18.0, None, 55.0)}
    for k, (tmin, tmax, hrmin, hrmax) in esperado_clima.items():
        c = CLIMA[k]
        exige(c['t_min'] == tmin and c['t_max'] == tmax,
              'CLIMA[%s] se ha despegado del kit: %s-%s' % (k, c['t_min'], c['t_max']))
        exige(c['hr_min'] == hrmin and c['hr_max'] == hrmax,
              'CLIMA[%s]: la humedad se ha despegado del kit' % k)
        exige(c['fuente'].startswith('kit-tareas-chocolateria/'),
              'CLIMA[%s] no cita el kit como fuente' % k)
    exige(CLIMA['obrador']['fuente'] == F_KIT_08_APERTURA,
          'R3-M2: el obrador tiene que citar SOLO 08-apertura-cierre-negocio.xlsx')
    exige(VITRINA_UMBRAL_ALARMA_C == 20.0,
          'El semaforo de vitrina solo puede avisar por encima de 20 grados C')
    exige(VITRINA_UMBRAL_ALARMA_C > CLIMA['vitrina']['t_max'],
          'PROHIBIDO un semaforo que ponga en rojo los 16-18 grados C del propio kit')

    # ---- 4. plantilla y convenio -----------------------------------------
    jornadas = sum(p[2] for p in PLANTILLA)
    exige(abs(jornadas - 2.5) < 1e-9,
          'Las jornadas suman %.2f y §3.1 fija 2,5' % jornadas)
    exige(len(PLANTILLA) == 3, 'La plantilla no tiene 3 personas (§3.1)')
    for pid, perfil, _j, grupo, area, _h, _t in PLANTILLA:
        exige(perfil in PERFILES_KIT,
              '%s usa el perfil «%s», que no es uno de los TRES literales del kit'
              % (pid, perfil))
        exige(1 <= grupo <= len(CONVENIO), '%s apunta a un grupo de convenio inexistente' % pid)
        exige(area in CONVENIO[grupo - 1][4],
              '%s esta en el area %s y su grupo de convenio no la contempla' % (pid, area))
    exige(set(p[1] for p in PLANTILLA) == set(PERFILES_KIT),
          'Los tres renglones no cubren los tres perfiles del kit')
    exige(len([p for p in PLANTILLA if p[4] == 'OBRADOR']) == 2,
          'Tienen que ser dos personas en OBRADOR para que el coste hora tenga sentido')

    exige(CONVENIO_PAGAS == 15, 'El convenio de Madrid paga 15, no %d' % CONVENIO_PAGAS)
    exige(CONVENIO_ES_EJEMPLO, 'D43: la tabla salarial va MARCADA COMO EJEMPLO')
    exige(CONVENIO_CODIGO == '28001025011981', 'El codigo del convenio ha cambiado')
    exige('BOLLERIA' not in CONVENIO_DENOMINACION.upper(),
          'R2-B1: «BOLLERIAS» no esta en la denominacion oficial del REGCON')
    for n, nombre, mes, anio, _areas, _puestos in CONVENIO:
        exige(abs(mes * CONVENIO_PAGAS - anio) < 0.005,
              'Grupo %d (%s): %.2f x %d no da %.2f' % (n, nombre, mes, CONVENIO_PAGAS, anio))
    mas_bajo = min(c[3] for c in CONVENIO)
    exige(mas_bajo > P('smi_anual'),
          'El grupo mas bajo del convenio (%.2f) ya no supera el SMI anual (%.2f)'
          % (mas_bajo, P('smi_anual')))
    exige(len(SALARIOS_MERCADO) == 4, 'Los salarios de mercado son CHS-69a a CHS-69d')
    for etiqueta, mn, mx, equiv, _f in SALARIOS_MERCADO:
        exige(etiqueta.startswith(chr(171)) and etiqueta.endswith(chr(187)),
              'C-7: las etiquetas de la fuente salarial van ENTRECOMILLADAS: %r' % etiqueta)
        exige(equiv in PERFILES_KIT,
              'El salario de mercado %r no equivale a ningun perfil del kit' % etiqueta)
        exige(mn < mx, 'Rango salarial invertido en %r' % etiqueta)

    # ---- 5. parametros ----------------------------------------------------
    for clave, (valor, fuente, _nota) in PARAMS.items():
        exige(_fuente_ok(fuente), 'PARAMS[%s] tiene una fuente no reconocida: %r'
              % (clave, fuente))
        if clave != 'iva_taller':
            exige(valor is not None, 'PARAMS[%s] sin valor' % clave)
    exige(P('iva_taller') is None,
          'D42e: el tipo de IVA del taller va SIN CIFRA, y aqui tiene un valor')
    exige(abs(P('food_cost_objetivo') + margen_bruto_objetivo() - 1.0) < 1e-9,
          'La regla UNICA de margen no cierra')
    exige(abs(P('ss_empresa') - 0.33) < 1e-9,
          'ss_empresa se ha despegado del parametro de la familia (motor.PARAMETROS)')
    exige(abs(P('smi_anual') - 17094.0) < 1e-9,
          'smi_anual se ha despegado del parametro de la familia (motor.PARAMETROS)')
    exige(P('meses_colchon_fondo_maniobra') == 6,
          'El colchon de tesoreria son 6 meses de fijos (§3.4)')
    entradas_libro2 = [c[1] for c in CAPEX]
    exige(not any('meses de colchon' in x.lower() for x in entradas_libro2),
          'R4-A1: «meses de colchon» NO puede ser una entrada del libro 2')

    # ---- 6. las coberturas: UN precio, DOS bases --------------------------
    negras = [k for k, c in COBERTURAS.items() if c.get('es_celda_unica')]
    exige(len(negras) == 1,
          'Tiene que haber UNA sola celda unica de precio de cobertura y hay %d' % len(negras))
    exige(abs(COBERTURAS['negra']['precio_fuente'] - 25.02) < 1e-9,
          'El precio de la cobertura negra se ha despegado de CHS-28a')
    exige(COBERTURAS['negra']['base_iva'] == 'con IVA',
          'A-2: CHS-28a esta declarada CON IVA, y de ahi sale todo el ajuste de base')
    base = precio_cobertura_base_imponible('negra')
    exige(abs(base - 25.02 / 1.10) < 1e-6,
          'La base imponible de la cobertura negra no sale de 25,02 / 1,10')
    exige(base < COBERTURAS['negra']['precio_fuente'],
          'La base imponible no puede ser mayor que el precio con IVA')
    exige(abs(COBERTURAS['origen']['precio_fuente'] - 37.48) < 1e-9,
          'El precio de la cobertura de origen se ha despegado de CHS-28c')
    for k, c in COBERTURAS.items():
        exige(c['fuente_rango_cacao'] == F_KIT_TEMPLADO,
              'Los porcentajes de cacao de %s tienen que citar el kit' % k)
        exige(c['base_iva'] in ('con IVA', 'sin IVA', 'no declarada'),
              'Base de IVA desconocida en la cobertura %s' % k)
        exige(c['fuente_tres_magnitudes'] == 'supuesto',
              'D37 capa (b): las tres magnitudes se COPIAN de la ficha del proveedor, '
              'asi que aqui solo pueden ser supuesto (%s)' % k)
    exige(COBERTURAS['negra']['cacao_min_pct'] == 55.0
          and COBERTURAS['negra']['cacao_max_pct'] == 70.0,
          'El rango de cacao de la negra se ha despegado del kit (55-70 %)')
    exige(COBERTURAS['leche']['cacao_min_pct'] == 35.0
          and COBERTURAS['leche']['cacao_max_pct'] == 40.0,
          'El rango de cacao de la de leche se ha despegado del kit (35-40 %)')
    exige(COBERTURAS['blanca']['cacao_min_pct'] == 28.0
          and COBERTURAS['blanca']['cacao_max_pct'] == 33.0,
          'El rango de cacao de la blanca se ha despegado del kit (28-33 %)')

    # ---- 7. la carta -------------------------------------------------------
    exige(len(CARTA) == 28, 'La carta tiene %d referencias y la SPEC fija 28' % len(CARTA))
    conteo = dict((f, len(por_familia(f))) for f in FAMILIAS)
    exige(conteo == FAMILIAS_ESPERADO,
          'El reparto por familia no es el de §3.2: %s frente a %s'
          % (conteo, FAMILIAS_ESPERADO))
    mix = sum(r['mix_pct'] for r in CARTA)
    mix_v = sum(r['mix_verano_pct'] for r in CARTA)
    exige(abs(mix - 100.0) < 1e-6, 'El mix anual suma %.4f %% y tiene que sumar 100' % mix)
    exige(abs(mix_v - 100.0) < 1e-6,
          'El mix de verano suma %.4f %% y tiene que sumar 100' % mix_v)
    exige(mix != mix_v or any(r['mix_pct'] != r['mix_verano_pct'] for r in CARTA),
          'D36: el mix de julio y agosto tiene que ser DISTINTO del anual')
    ganache_fresca = [r for r in CARTA
                      if r['familia_vida_util'] == 'Bombones de ganache con nata fresca']
    exige(sum(r['mix_verano_pct'] for r in ganache_fresca)
          < sum(r['mix_pct'] for r in ganache_fresca),
          'D36: en verano baja la ganache fresca, y aqui no baja')
    tabletas = por_familia('Tabletas')
    exige(sum(r['mix_verano_pct'] for r in tabletas) > sum(r['mix_pct'] for r in tabletas),
          'D36: en verano sube la tableta y el producto estable, y aqui no sube')

    ids = [r['id'] for r in CARTA]
    exige(len(set(ids)) == len(ids), 'Hay ids repetidos en la carta')
    nombres = [r['nombre'] for r in CARTA]
    exige(len(set(nombres)) == len(nombres), 'Hay nombres repetidos en la carta')

    for r in CARTA:
        exige(bool(r.get('denominacion_legal')),
              '%s no declara denominacion legal (D52)' % r['id'])
        exige(_fuente_ok(r['fuente_denominacion']),
              '%s: la denominacion legal no cita ningun id' % r['id'])
        exige(r['via'] in VIAS_DESPACHO,
              '%s no declara via etiqueta/granel valida: %r (D47)' % (r['id'], r['via']))
        exige(isinstance(r['alergenos'], dict)
              and set(r['alergenos']) == set(ALERGENOS_CLAVES),
              '%s: su fila de alergenos no tiene las OCHO columnas' % r['id'])
        exige(r['familia_vida_util'] in [f[0] for f in VIDA_UTIL_KIT],
              '%s apunta a una familia de vida util que no esta en el kit: %r'
              % (r['id'], r['familia_vida_util']))
        exige(0.0 <= r['merma_recuperable_pct'] < 1.0
              and 0.0 <= r['merma_no_recuperable_pct'] < 1.0,
              '%s: merma fuera de rango' % r['id'])
        exige(r['minutos_mo_tanda'] > 0, '%s no declara minutos de mano de obra' % r['id'])
        exige(piezas_por_tanda(r) >= 1, '%s: piezas por tanda invalidas' % r['id'])
        exige(abs(r['iva'] - 0.10) < 1e-9,
              '%s lleva IVA %.2f y el chocolate va al 10 %% (CHN-71)' % (r['id'], r['iva']))
        exige(r['fuente_pvp'] == 'supuesto' or r['fuente_pvp'].startswith('CHS-'),
              '%s: fuente_pvp no reconocida' % r['id'])
        if r['relleno']:
            exige(r['relleno'] in RELLENOS,
                  '%s usa el relleno %r, que no existe' % (r['id'], r['relleno']))
        if not es_caja(r):
            exige(r['cobertura'] in COBERTURAS,
                  '%s usa una cobertura que no existe' % r['id'])
            exige(r['g_chocolate'] > 0, '%s no declara gramos de chocolate' % r['id'])
            exige(pvp_sin_iva(r) > coste_total_unidad(r),
                  '%s vende por debajo de coste: PVP base %.3f, coste %.3f'
                  % (r['id'], pvp_sin_iva(r), coste_total_unidad(r)))
        if exige_25_pct(r):
            pct = pct_chocolate_sobre_peso_total(r)
            exige(pct >= MINIMO_25_PCT,
                  '%s se llama «%s» y solo tiene el %.1f %% de chocolate sobre el peso '
                  'TOTAL: no llega al 25 %% del ap. 1.10/1.13 (CHN-10)'
                  % (r['id'], r['denominacion_legal'], pct))

    # la matriz 28 x 8 completa y con los ocho alergenos usados al menos una vez
    m = matriz_alergenos()
    exige(len(m) == 28 and all(len(f[2]) == 8 for f in m),
          'La matriz de alergenos no es de 28 x 8')
    for clave, nombre_al, _punto in ALERGENOS:
        exige(referencias_con(clave),
              'El alergeno «%s» no aparece en ninguna referencia: la matriz no ensena '
              'nada sobre el' % nombre_al)
    exige(len(referencias_con('cacahuetes')) >= 1 and len(referencias_con('sesamo')) >= 1
          and len(referencias_con('frutos_cascara')) >= 1,
          'CHN-34b: cacahuete, sesamo y frutos de cascara son entradas INDEPENDIENTES '
          'y las tres tienen que estar representadas')

    # las cajas: su fila de alergenos es la UNION de lo que llevan dentro
    for r in CARTA:
        if not es_caja(r):
            continue
        exige(sum(n for _i, n in r['composicion_caja']) == r['uds_caja'],
              '%s dice %d unidades y su composicion suma %d'
              % (r['id'], r['uds_caja'], sum(n for _i, n in r['composicion_caja'])))
        union = dict((k, False) for k in ALERGENOS_CLAVES)
        for i, _n in r['composicion_caja']:
            for k in ALERGENOS_CLAVES:
                union[k] = union[k] or ref(i)['alergenos'][k]
        exige(union == r['alergenos'],
              '%s: su fila de alergenos no es la UNION de lo que lleva dentro. '
              'Declarada %s, calculada %s'
              % (r['id'], sorted(k for k in union if r['alergenos'][k]),
                 sorted(k for k in union if union[k])))

    # los precios de compra
    for ing, (precio, _ud, fuente) in PRECIOS_COMPRA.items():
        exige(_fuente_ok(fuente), 'El ingrediente %r tiene una fuente no reconocida: %r'
              % (ing, fuente))
        exige(precio_compra(ing)[0] > 0, 'El ingrediente %r no tiene precio' % ing)
    for clave, r in RELLENOS.items():
        exige(coste_relleno_kg(clave) > 0, 'El relleno %r sale a coste cero' % clave)
        exige(0.0 < r['aw'] < 1.0, 'El relleno %r tiene una aw imposible' % clave)
        exige(r['familia_kit'] in [f[0] for f in VIDA_UTIL_KIT],
              'El relleno %r apunta a una familia de vida util que no esta en el kit' % clave)
        for ing, _c in r['lineas']:
            exige(ing in PRECIOS_COMPRA,
                  'El relleno %r usa %r y no tiene precio de compra' % (clave, ing))

    # ---- 8. vida util: es la del kit, y no se reescribe -------------------
    exige(len(VIDA_UTIL_KIT) == 10,
          'La tabla de vida util del kit tiene DIEZ filas y aqui hay %d' % len(VIDA_UTIL_KIT))
    exige(FUENTE_VIDA_UTIL == F_KIT_MOLDEADO,
          'D30: la tabla de vida util se cita por fichero y hoja del kit')
    exige(VIDA_UTIL_DECLARADA is None,
          'CHN-30: la vida util la declara el operador en su APPCC; aqui es celda verde')
    plazos = dict((f[0], f[1]) for f in VIDA_UTIL_KIT)
    exige(plazos.get('Bombones de ganache con nata fresca') == '10-15 dias',
          'El plazo de la ganache fresca se ha despegado del literal del kit')
    exige(plazos.get('Bombones de ganache con nata UHT, sorbato o alcohol') == '4-8 semanas',
          'El plazo de la ganache estabilizada se ha despegado del literal del kit')
    exige(plazos.get('Tabletas y chocolate sin relleno') == '12-18 meses',
          'El plazo de la tableta se ha despegado del literal del kit')

    # ---- 9. equipamiento, escenarios y CAPEX ------------------------------
    for e in EQUIPAMIENTO:
        exige(e['base_iva'] in ('con IVA', 'sin IVA', 'no declarada'),
              'La linea %d no declara base de IVA valida (regla 3 de §2.3)' % e['n'])
        exige(e['tipo_iva'] is not None,
              'La linea %d no declara tipo de IVA' % e['n'])
        tiene = (e['valor_verificado'] is not None) != (e['supuesto_por_defecto'] is not None)
        exige(tiene,
              'La linea %d tiene los dos valores o ninguno: `valor_verificado` y '
              '`supuesto_por_defecto` son excluyentes' % e['n'])
        exige(precio_equipamiento_sin_iva(e) > 0,
              'La linea %d se queda con precio cero: seria una celda verde vacia' % e['n'])
        exige(e['plazo_semanas'] > 0, 'La linea %d no declara plazo de entrega' % e['n'])
        if e['valor_verificado'] is None and e['rango_min'] is None:
            exige(e['fuente'] == 'supuesto' or 'supuesto' in e['fuente'],
                  'La linea %d no tiene precio verificado ni rango, y su fuente no dice '
                  '«supuesto»' % e['n'])
        if e['rango_min'] is not None:
            exige(e['valor_verificado'] is None,
                  'D23a: la linea %d va como RANGO, asi que no puede tener ademas un '
                  'valor cerrado verificado' % e['n'])
    mantenedor = [e for e in EQUIPAMIENTO if e['es_desde']]
    exige(len(mantenedor) == 1 and abs(mantenedor[0]['valor_verificado'] - 570.0) < 1e-9,
          'D23b: el mantenedor es el unico «desde» del catalogo y vale 570,00 euros')
    moldes = [e for e in EQUIPAMIENTO if e['rango_min'] is not None]
    exige(len(moldes) == 1, 'D23a: los moldes son la unica linea que va como RANGO')
    mo = moldes[0]
    exige(mo['rango_min'] < mo['supuesto_por_defecto'] < mo['rango_max'],
          'D23a: el valor por defecto de los moldes tiene que caer DENTRO de su rango')
    exige(abs(mo['rango_min'] - 24.20 * 24) < 0.01 and abs(mo['rango_max'] - 42.83 * 24) < 0.01,
          'D23a: el rango de moldes no sale de los 24,20-42,83 euros/ud de CHS-45a')

    for k, esc in ESCENARIOS_DOTACION.items():
        exige(esc['min'] < esc['max'],
              'El escenario %s no es un RANGO: min >= max' % k)
        exige('BASE MIXTA' in esc['etiqueta'],
              'D23c: el escenario %s tiene que llevar pegada la etiqueta de base mixta' % k)
    exige(ESCENARIOS_DOTACION['A']['min'] / ESCENARIOS_DOTACION['B']['max'] > 3.5,
          'El factor 4 entre los dos escenarios ha dejado de ser cierto y la frase '
          'publicable habria que reescribirla')

    bloques_en_capex = set(c[0] for c in CAPEX)
    exige(bloques_en_capex == set(BLOQUES_CAPEX),
          'Los bloques de CAPEX no son los NUEVE de §3.3: %s' % sorted(bloques_en_capex))
    exige(len(BLOQUES_CAPEX) == 9, 'R4-M1: son NUEVE bloques de CAPEX')
    exige('Fondo de maniobra' in BLOQUES_CAPEX,
          'R4-M1: el fondo de maniobra conserva SU FILA PROPIA')
    exige(len(BLOQUES_COMPARABLES) == 6,
          'R4-M1: los bloques comparables son SEIS')
    for b in BLOQUES_COMPARABLES:
        exige(b in BLOQUES_CAPEX, 'El bloque comparable %r no esta en el CAPEX' % b)
    for b in ('Fianza y licencias', 'Packaging y moldes', 'Fondo de maniobra'):
        exige(b not in BLOQUES_COMPARABLES,
              'R4-M1: %r queda FUERA de la comparacion, entero' % b)
    for b in BLOQUES_CAPEX:
        exige(capex_bloque_sin_iva(b) > 0, 'El bloque de CAPEX %r suma cero' % b)
    bloques_equipo = set(e['bloque_capex'] for e in EQUIPAMIENTO)
    for b in bloques_equipo:
        exige(b in BLOQUES_CAPEX,
              'La linea de equipamiento apunta al bloque %r, que no existe en el CAPEX' % b)

    exige(abs(inversion_total_sin_iva()
              - (capex_sin_fondo_de_maniobra() + fondo_maniobra())) < 0.005,
          'D32: la inversion total no cuadra con sus dos mitades')
    exige(capex_sin_fondo_de_maniobra() < inversion_total_sin_iva(),
          'El CAPEX sin el fondo tiene que ser MENOR que la inversion total')
    exige(abs(fondo_maniobra()
              - P('meses_colchon_fondo_maniobra') * gastos_fijos_mensuales()) < 0.005,
          'El fondo de maniobra no sale de meses de colchon x gastos fijos')
    exige(20000.0 < capex_comparable_sin_iva() < 80000.0,
          'Los seis bloques comparables suman %.0f euros y se salen de la horquilla '
          'publicada de CHS-03 (20.000-80.000 euros «segun el proyecto»): si es a '
          'proposito, hay que reescribir la nota que los compara'
          % capex_comparable_sin_iva())

    # ---- 10. los OCHO cruces ----------------------------------------------
    exige(len(CRUCES) == 8, 'D32: son OCHO cruces y hay %d' % len(CRUCES))
    pares = [(c['receptor'], c['origen']) for c in CRUCES]
    exige(len(set(pares)) == 8, 'Hay cruces repetidos: %s' % pares)
    esperados = {(6, 1), (7, 1), (9, 2), (4, 3), (7, 3), (7, 2), (8, 9), (2, 7)}
    exige(set(pares) == esperados,
          'La lista de cruces no es la de §2.3: %s' % sorted(set(pares) ^ esperados))
    for c in CRUCES:
        exige(c['receptor'] != c['origen'], 'El cruce %d apunta a si mismo' % c['n'])
        exige(c['fichero_origen'].endswith('.xlsx')
              and c['fichero_receptor'].endswith('.xlsx'),
              'El cruce %d no nombra dos ficheros .xlsx' % c['n'])
    c62 = [c for c in CRUCES if (c['receptor'], c['origen']) == (7, 2)][0]
    exige('SIN el fondo' in c62['concepto'],
          'R3-A2: lo que viaja del 2 al 7 es el CAPEX SIN el fondo de maniobra')
    c27 = [c for c in CRUCES if (c['receptor'], c['origen']) == (2, 7)][0]
    exige('Fondo de maniobra' in c27['concepto'] and 'YA CALCULADO' in c27['concepto'],
          'R4-A1: lo que viaja del 7 al 2 es la MAGNITUD ya calculada, no sus factores')

    # ---- 11. campanas, valle y estacionalidad -----------------------------
    exige(len(CAMPANAS) == 12,
          'D35: las 12 filas del BONUS-02 del kit, y hay %d' % len(CAMPANAS))
    exige([c['mes'] for c in CAMPANAS] == list(range(1, 13)),
          'Las 12 filas no estan en orden de mes o falta alguno')
    temporadas = dict((t, len(meses_por_temporada(t))) for t in ('Alta', 'Media', 'Baja'))
    exige(temporadas == {'Alta': 7, 'Media': 4, 'Baja': 1},
          'El kit declara 7 Alta, 4 Media y 1 Baja, y aqui hay %s' % temporadas)
    exige(meses_por_temporada('Alta') == [2, 3, 4, 5, 10, 11, 12],
          'Los meses «Alta» no son los del kit (feb, mar, abr, may, oct, nov, dic)')
    exige(meses_por_temporada('Baja') == [8],
          'D36: el unico mes «Baja» es agosto')
    exige(any('COMUNIONES' in c['campana'] for c in CAMPANAS),
          'D35: las COMUNIONES tienen que estar entre las campanas')
    exige(CAMPANA_COMUNIONES['meses'] == (4, 5, 6),
          'D35: las comuniones van de abril a junio')
    for c in CAMPANAS:
        exige(c['fuente_fila'] == F_KIT_CALENDARIO,
              'La fila de %s no se declara como copia del calendario del kit' % c['nombre_mes'])
        exige(c['producto_estrella'] in [r['id'] for r in CARTA],
              '%s: producto estrella %r que no esta en la carta'
              % (c['nombre_mes'], c['producto_estrella']))
        exige(c['uds_dia_pico'] >= c['uds_dia_normal'],
              '%s: el pico no puede vender menos que un dia normal' % c['nombre_mes'])
        exige(c['pvp_campana'] > 0, '%s: sin PVP de campana' % c['nombre_mes'])
        exige(c['dias_campana'] >= 0, '%s: dias de campana negativos' % c['nombre_mes'])

    exige(VALLE['mes'] == 8 and VALLE['temporada_kit'] == 'Baja',
          'D36: el valle es AGOSTO y es el unico mes Baja')
    exige(VALLE['para_el_obrador'] and not VALLE['para_la_tienda'],
          'D36: lo que para es el OBRADOR, no la caja')
    exige(VALLE['meses_mix_verano'] == (7, 8),
          'D36: el mix distinto es el de julio y agosto')
    exige(VALLE['envios_parados_meses'] == (6, 7, 8, 9),
          'D36: los envios (canal ONLINE) paran de junio a septiembre')

    media = sum(ESTACIONALIDAD_MENSUAL) / 12.0
    exige(abs(media - 1.0) < 1e-9,
          'Los coeficientes de estacionalidad tienen media %.6f y tiene que ser 1,000' % media)
    exige(min(ESTACIONALIDAD_MENSUAL) == ESTACIONALIDAD_MENSUAL[7],
          'Agosto tiene que ser el minimo de los doce coeficientes')
    exige(ESTACIONALIDAD_MENSUAL[7] > 0.0,
          'Agosto NO vale cero: la tienda abre, lo que para es el obrador')
    exige(max(ESTACIONALIDAD_MENSUAL) == ESTACIONALIDAD_MENSUAL[11],
          'Diciembre tiene que ser el maximo')
    exige(len(DIAS_APERTURA_MES) == 12
          and sum(DIAS_APERTURA_MES) == NEGOCIO['dias_apertura_anio'],
          'Los dias de apertura por mes (%d) no suman los del ano (%d)'
          % (sum(DIAS_APERTURA_MES), NEGOCIO['dias_apertura_anio']))
    exige(DIAS_APERTURA_MES[7] > 0,
          'D36: en agosto la tienda NO cierra')
    ra = rampa_mensual()
    exige(len(ra) == 12 and abs(ra[0] - RAMPA['mes1']) < 1e-9 and abs(ra[-1] - 1.0) < 1e-9,
          'La rampa de arranque no va de %.2f a 1,00 en 12 meses' % RAMPA['mes1'])
    exige(all(ra[i] <= ra[i + 1] + 1e-12 for i in range(11)), 'La rampa no es creciente')

    # ---- 12. canales -------------------------------------------------------
    exige(len(CANALES) == 5, 'Los canales son CINCO y hay %d' % len(CANALES))
    suma_canales = sum(c['ventas_pct'] for c in CANALES)
    exige(abs(suma_canales - 100.0) < 1e-9,
          'Los canales suman %.2f %% y tienen que sumar 100' % suma_canales)
    for c in CANALES:
        exige(0.0 < c['margen_bruto'] < 1.0, 'Canal %s: margen fuera de rango' % c['canal'])
        exige(c['sale_de_la_nota_644_5'] in ('si', 'no', 'no lo se'),
              'Canal %s: la respuesta a la nota del 644.5 tiene que ser si / no / no lo se'
              % c['canal'])
        exige('epigrafe' not in str(c.get('epigrafe_iae', '')),
              'D19: la hoja NO emite un epigrafe de IAE por canal')
        exige(margen_contribucion_canal(c) > 0,
              'Canal %s: margen de contribucion negativo' % c['canal'])
    fuera = [c for c in CANALES if c['sale_de_la_nota_644_5'] != 'no']
    exige(len(fuera) == 3,
          'D19: TRES de los cinco canales caen fuera de la nota del 644.5, y aqui hay %d'
          % len(fuera))
    filas = filas_canal_644_5()
    exige(len(filas) == 5 and all('[CANAL]' not in f['pregunta_al_asesor'] for f in filas),
          'Las cinco filas de canal no traen su pregunta redactada para el asesor')
    taller = [c for c in CANALES if c['canal'].startswith('Talleres')][0]
    exige(taller['precio_persona_min'] == 25.0 and taller['precio_persona_max'] == 45.0,
          'El precio del taller se ha despegado de CHS-30 (25-45 euros/persona)')
    exige(taller['minimo_personas'] == 6,
          'El minimo del taller se ha despegado de CHS-30 (6 personas)')
    exige(taller['duracion_min_minutos'] == 90 and taller['duracion_max_minutos'] == 150,
          'La duracion del taller se ha despegado de CHS-30 (90-150 min)')
    corp = [c for c in CANALES if c['canal'].startswith('Regalo')][0]
    exige(corp['cobro_dias'] > 0 and corp['pedido_minimo'] > 0,
          'El canal corporativo tiene que declarar dias de cobro y pedido minimo')

    # ---- 13. proveedores y clientes ---------------------------------------
    exige(len(PROVEEDORES) == 6, 'Se publican SOLO los SEIS proveedores verificados')
    for nombre_p, _cat, url, fuente, papel, _nota in PROVEEDORES:
        exige(url.startswith('https://'), 'Proveedor %s sin URL https' % nombre_p)
        exige(_fuente_ok(fuente), 'Proveedor %s: fuente no reconocida' % nombre_p)
        exige(papel == '',
              'D48: la columna «papel EUDR» de %s va VACIA: la rellena el lector' % nombre_p)
    exige(len(set(p[2] for p in PROVEEDORES)) == 6, 'Hay una URL de proveedor repetida')
    exige(set(PAPELES_EUDR) == set(PAPELES_EUDR_TEXTO),
          'Los tres papeles del EUDR no cuadran con su texto')
    exige(len(PAPELES_EUDR) == 3, 'D48: son TRES papeles, no dos')
    exige('operador' in PAPELES_EUDR_TEXTO
          and 'numero de referencia de su DDS' in PAPELES_EUDR_TEXTO['operador'],
          'D48: el numero de DDS solo se pide en la rama «operador»')
    exige('NO se le pide el numero de DDS' in PAPELES_EUDR_TEXTO['operador posterior'],
          'D48: al operador posterior NO se le pide el numero de DDS')
    exige(3 <= len(CLIENTES_B2B) <= 4,
          'D48: la tabla de clientes lleva 3-4 clientes ficticios declarados')
    exige(FUENTE_CLIENTES_B2B == 'supuesto',
          'Los clientes de ejemplo tienen que ir declarados como supuesto')
    exige(any('distinta titularidad' in c[2].lower() or 'Minorista' in c[1]
              for c in CLIENTES_B2B),
          'Falta el cliente que activa el art. 3: un minorista de distinta titularidad')

    # ---- 14. checklist legal y cronograma ---------------------------------
    fases_usadas = set(f[0] for f in CHECKLIST_LEGAL)
    exige(fases_usadas == set(FASES_CHECKLIST),
          'El checklist no cubre las SEIS fases F1-F6: %s' % sorted(fases_usadas))
    for fase, tramite, _resp, plazo, _coste, fuente, cambia, _nota in CHECKLIST_LEGAL:
        exige(fase in FASES_CHECKLIST, 'Fase desconocida en «%s»' % tramite)
        exige(plazo > 0, 'El tramite «%s» no declara plazo orientativo' % tramite)
        exige(_fuente_ok(fuente), 'Tramite «%s»: fuente no reconocida %r' % (tramite, fuente))
        exige(isinstance(cambia, bool),
              'Tramite «%s»: «cambia por comunidad» no es booleano' % tramite)
    exige(len(CCAA_EJEMPLO) == 4, 'Cuatro comunidades de ejemplo')
    exige(any(f[6] for f in CHECKLIST_LEGAL),
          'Ningun tramite cambia por comunidad: el cuadro de las cuatro no tendria sentido')
    exige(FILA_ARTESANIA['es_voluntaria'] and FILA_ARTESANIA['respuesta'] == '',
          'D10 (B-6): la fila de artesania es una acreditacion VOLUNTARIA y su celda '
          'verde va vacia para que la rellene el lector')

    total_meses, camino, holgura = ruta_critica()
    exige(len(GANTT) == 13, 'El cronograma tiene 13 hitos y hay %d' % len(GANTT))
    ids_gantt = set(h[0] for h in GANTT)
    for hid, hito, _d, deps in GANTT:
        for d in deps:
            exige(d in ids_gantt, 'El hito %s depende de %s, que no existe' % (hid, d))
    exige(camino[0] == 'H1' and camino[-1] == 'H13',
          'La ruta critica no va del primer hito a la apertura: %s' % camino)
    mes_ap = mes_apertura_calculado()
    exige(mes_ap == NEGOCIO['mes_apertura_recomendado'],
          'La ruta critica (%.1f meses desde %s) abre en %s y el mes recomendado es %s'
          % (total_meses, MESES[MES_INICIO_PROYECTO - 1], MESES[mes_ap - 1],
             MESES[NEGOCIO['mes_apertura_recomendado'] - 1]))
    exige(campana(mes_ap)['temporada'] != 'Alta',
          'La apertura cae en un mes de campana Alta (%s)' % MESES[mes_ap - 1])
    exige(holgura['H6'] >= 0,
          'El pedido de equipamiento tiene holgura negativa: la ruta critica no cuadra')
    rc, plazo_m, avisa = cuadre_plazo_maquinaria()
    exige(not avisa,
          'El plazo de entrega critico (%.1f meses) es MAYOR que la ruta critica '
          '(%.1f meses): la fecha de apertura la manda la maquinaria y el semaforo del '
          'libro 8 avisaria' % (plazo_m, rc))

    # ---- 15. economia -------------------------------------------------------
    pyg = cuenta_resultados_crucero()
    exige(pyg['ventas_sin_iva'] > 0 and pyg['gastos_fijos'] > 0, 'El P&L no cuadra')
    exige(0.09 <= pyg['margen_neto'] <= 0.11,
          'El margen neto del ano de crucero es del %.2f %% y la banda acordada es el '
          '9-11 %%: fuera de ella el caso se lee como optimista. La UNICA palanca que se '
          'toca es `tickets_dia_crucero`' % (100 * pyg['margen_neto']))
    exige(punto_muerto_mensual() * 12.0 < pyg['ventas_sin_iva'],
          'La facturacion de crucero no llega al punto muerto')
    fc_carta, fc_serv = food_cost_carta(), food_cost_servido()
    exige(0.0 < fc_carta < P('food_cost_objetivo'),
          'El food cost de escandallo de la carta (%.1f %%) ya no esta por debajo de la '
          'regla unica del %.0f %%' % (100 * fc_carta, 100 * P('food_cost_objetivo')))
    exige(fc_serv > fc_carta, 'El packaging tiene que subir el food cost')
    exige(10.0 <= coste_hora_obrador() <= 35.0,
          'El coste hora de obrador (%.2f euros) se ha ido fuera de todo rango creible'
          % coste_hora_obrador())
    exige(abs(iva_medio_carta() - 0.10) < 1e-9,
          'Todas las referencias van al 10 %%, asi que el IVA medio tiene que ser 0,10: '
          'sale %.4f' % iva_medio_carta())
    for partida, importe, fuente, _nota in GASTOS_FIJOS_MENSUALES:
        exige(_fuente_ok(fuente), 'Gasto fijo «%s»: fuente no reconocida %r' % (partida, fuente))
        exige(importe is None or importe > 0, 'Gasto fijo «%s» sin importe' % partida)
    exige(not any('propietario' in p[0].lower() for p in GASTOS_FIJOS_MENSUALES),
          'El titular es el Encargado y su retribucion ya esta en la nomina: un renglon '
          'de «retribucion del propietario» lo contaria dos veces')
    exige(FINANCIACION['carencia_meses'] < FINANCIACION['plazo_meses'],
          'La carencia no puede ser mayor que el plazo')
    exige(FINANCIACION['plazo_meses'] == 84, 'El prestamo es a 7 anos (§3.4)')
    exige(abs(FINANCIACION['pct_recursos_propios'] + FINANCIACION['pct_prestamo'] - 1.0) < 1e-9,
          'La estructura 40/60 no suma 100 %')
    exige(FINANCIACION['principal'] is None,
          'El principal del prestamo NO se teclea: lo deriva `principal_prestamo()`')
    ratio = principal_prestamo() / inversion_total_sin_iva()
    exige(abs(ratio - FINANCIACION['pct_prestamo']) <= 0.005,
          'El principal (%.0f euros) es el %.2f %% de la inversion total (%.0f euros) y '
          'la estructura declarada es el %.0f %%: el punto fijo no ha convergido'
          % (principal_prestamo(), 100 * ratio,
             inversion_total_sin_iva(), 100 * FINANCIACION['pct_prestamo']))
    exige(abs(principal_prestamo() % 100.0) < 1e-6,
          'El principal tiene que estar redondeado a centenas: %.2f' % principal_prestamo())
    exige(intereses_anio_1() > 0, 'El prestamo no genera intereses')
    exige(asistentes_punto_muerto_taller() < taller['aforo'],
          'El taller necesita %.1f asistentes para cubrir su coste y su aforo es %d: no '
          'sale nunca' % (asistentes_punto_muerto_taller(), taller['aforo']))

    # ---- 16. plastico y franquicias ---------------------------------------
    exige(abs(PLASTICO['tipo_euros_kg'] - 0.45) < 1e-9,
          'El tipo del impuesto al plastico se ha despegado de CHN-62')
    exige(abs(PLASTICO['umbral_kg_mes'] - 5.0) < 1e-9,
          'El umbral del art. 75.f) son 5 kg/mes (CHN-62b)')
    exige(PLASTICO['moldes_no_sujetos'] is True,
          'CHN-62c: los moldes de policarbonato NO estan sujetos')
    for f in FRANQUICIAS:
        if f['fuente'] == 'sin id verificado':
            exige(f['inversion_desde'] is None and f['canon'] is None,
                  'La franquicia %r no tiene id en el JSON comun: no puede publicar '
                  'cifras' % f['marca'])
        else:
            exige(id_existe_en_json_comun(f['fuente']) or _carga_json_comun()['error'],
                  'La franquicia %r cita un id que no existe en el JSON comun' % f['marca'])
            exige('orden de magnitud' in f['etiqueta'],
                  'D11: la franquicia %r tiene que llevar pegada su etiqueta' % f['marca'])

    # ---- 17. todos los ids citados existen en el JSON comun (D44) ---------
    comun = _carga_json_comun()
    if comun['error']:
        avisos.append('No se pudo abrir el JSON comun (%s): no se ha podido comprobar '
                      'que los ids existan' % comun['error'])
    else:
        citados = set()
        for f in fuentes:
            for m2 in re.findall(r'\b(CH[NS]-\d+[a-z]?(?:-int)?|PA-\d+[a-z]?)\b', f):
                citados.add(m2)
        for pid in sorted(citados):
            exige(id_existe_en_json_comun(pid),
                  'D44: el id %s se cita como fuente y NO existe en el JSON comun de '
                  '635 entradas' % pid)
        for pid in sorted(IDS_LEGALES_REQUERIDOS):
            exige(id_existe_en_json_comun(pid),
                  'El id legal requerido %s no existe en el JSON comun' % pid)
        for pid in sorted(ID_REUTILIZADO_PASTELERIA):
            exige(id_existe_en_json_comun(pid),
                  'El id reutilizado de Pasteleria %s no existe en el JSON comun' % pid)

    # ---- 18. gate legal ----------------------------------------------------
    faltan_legales = gate_legal(abortar=False)
    exige(not faltan_legales,
          'gate_legal: faltan %d de %d notas legales (%s). Los constructores de los '
          'libros 4, 5, 8 y 9 NO pueden arrancar sin ellas'
          % (len(faltan_legales), len(IDS_LEGALES_REQUERIDOS),
             ', '.join(faltan_legales[:8]) + ('...' if len(faltan_legales) > 8 else '')))

    # ---- 19. contraste opcional contra los xlsx del kit --------------------
    try:
        import openpyxl                                       # noqa: PLC0415
    except ImportError:
        avisos.append('openpyxl no disponible: no se ha contrastado contra los xlsx del kit')
    else:
        if not os.path.exists(KIT_PERFILES):
            avisos.append('No existe %s: no se ha podido comprobar los perfiles' % KIT_PERFILES)
        else:
            try:
                wb = openpyxl.load_workbook(KIT_PERFILES, read_only=True, data_only=True)
                try:
                    hojas = tuple(h for h in wb.sheetnames if h != 'Instrucciones')
                finally:
                    wb.close()
                exige(hojas == PERFILES_KIT,
                      'Los perfiles del kit son %s y aqui se declaran %s'
                      % (list(hojas), list(PERFILES_KIT)))
            except Exception as e:                            # noqa: BLE001
                avisos.append('No se pudo leer %s: %s' % (KIT_PERFILES, e))

    # ================= resumen =================
    print('«La Almendra» - juego de datos unico de «Como Montar una Chocolateria»')
    print('Verificacion legal de referencia: %s' % FECHA_VERIFICACION_LEGAL)
    print('')
    print('LOCAL, CLIMA Y PLANTILLA')
    print('  %.0f m2 en %d zonas: %s'
          % (suma_zonas, len(ZONAS),
             ' / '.join('%s %.0f' % (z[0].split(' ')[0], z[1]) for z in ZONAS)))
    print('  clima (los CINCO valores son del kit): %s'
          % ' / '.join('%s %g-%g C' % (k, c['t_min'], c['t_max'])
                       for k, c in sorted(CLIMA.items())))
    print('  %d personas / %.1f jornadas: %s'
          % (len(PLANTILLA), jornadas, ' / '.join('%s %.1f' % (p[1], p[2]) for p in PLANTILLA)))
    print('  convenio %s (%s), %d pagas, EJEMPLO'
          % (CONVENIO_CODIGO, CONVENIO_AUTORIDAD, CONVENIO_PAGAS))
    print('  coste empresa del personal %.0f euros/ano / coste hora de obrador %.2f euros/h'
          % (coste_personal_anual(), coste_hora_obrador()))
    print('')
    print('CARTA')
    print('  %d referencias en %d familias: %s'
          % (len(CARTA), len(FAMILIAS), ' / '.join('%s %d' % (f, conteo[f]) for f in FAMILIAS)))
    print('  mix anual %.1f %% / mix de verano %.1f %% (julio y agosto)' % (mix, mix_v))
    print('  PVP medio ponderado %.2f euros con IVA / ticket medio %.2f euros (%.1f piezas)'
          % (pvp_medio_ponderado(), ticket_medio_con_iva(), P('piezas_por_ticket')))
    print('  food cost de escandallo %.1f %% / con packaging %.1f %% / regla unica %.0f %%'
          % (100 * fc_carta, 100 * fc_serv, 100 * P('food_cost_objetivo')))
    n_gr = sum(1 for r in CARTA if r['via'] == 'a granel')
    print('  via de despacho: %d envasadas con etiqueta / %d a granel (D47)'
          % (len(CARTA) - n_gr, n_gr))
    print('  matriz de alergenos %d x %d, los OCHO del Anexo II: %s'
          % (len(m), len(ALERGENOS),
             ' / '.join('%s %d' % (a[0], len(referencias_con(a[0]))) for a in ALERGENOS)))
    print('  cobertura negra: %.2f euros/kg CON IVA (CHS-28a) -> %.4f euros/kg base imponible'
          % (COBERTURAS['negra']['precio_fuente'], precio_cobertura_base_imponible('negra')))
    print('')
    print('INVERSION')
    print('  dotacion tipo %.2f euros sin IVA / plazo de entrega critico %d semanas (%s)'
          % (dotacion_tipo_sin_iva(), plazo_critico_semanas(),
             equipo_plazo_critico()['partida']))
    print('  %d lineas de equipamiento: %d con precio verificado, %d con supuesto por defecto'
          % (len(EQUIPAMIENTO),
             sum(1 for e in EQUIPAMIENTO if e['valor_verificado'] is not None),
             sum(1 for e in EQUIPAMIENTO if e['supuesto_por_defecto'] is not None)))
    print('  CAPEX sin el fondo %.0f euros / fondo de maniobra %.0f euros / '
          'inversion total %.0f euros'
          % (capex_sin_fondo_de_maniobra(), fondo_maniobra(), inversion_total_sin_iva()))
    print('  seis bloques comparables %.0f euros (CHS-03 publica 20.000-30.000, hasta '
          '80.000 «segun el proyecto»)' % capex_comparable_sin_iva())
    print('  IVA soportado que hay que adelantar %.0f euros' % iva_soportado_capex())
    print('  escenarios de dotacion publicados: A %.0f-%.0f / B %.0f-%.0f euros (%s)'
          % (ESCENARIOS_DOTACION['A']['min'], ESCENARIOS_DOTACION['A']['max'],
             ESCENARIOS_DOTACION['B']['min'], ESCENARIOS_DOTACION['B']['max'],
             ESCENARIOS_DOTACION['A']['etiqueta']))
    print('  %d traspasos reales (precios PEDIDOS, no pagados): %.0f a %.0f euros'
          % (len(TRASPASOS), TRASPASO_RANGO[0], TRASPASO_RANGO[1]))
    print('')
    print('ANO DE CRUCERO')
    print('  ventas %.0f euros sin IVA / %d tickets/dia x %d dias / %.0f piezas/dia'
          % (pyg['ventas_sin_iva'], P('tickets_dia_crucero'),
             NEGOCIO['dias_apertura_anio'], piezas_dia_crucero()))
    print('  gastos fijos %.0f euros/mes / punto muerto %.0f euros/mes'
          % (gastos_fijos_mensuales(), punto_muerto_mensual()))
    print('  beneficio %.0f euros / margen neto %.1f %%'
          % (pyg['beneficio_neto'], 100 * pyg['margen_neto']))
    print('  financiacion %.0f %% propios / %.0f %% prestamo de %.0f euros a %d meses '
          '(%.1f %% real)'
          % (100 * FINANCIACION['pct_recursos_propios'], 100 * FINANCIACION['pct_prestamo'],
             principal_prestamo(), FINANCIACION['plazo_meses'], 100 * ratio))
    print('  estacionalidad %s (media %.3f, minimo agosto)'
          % ('/'.join('%.2f' % c for c in ESTACIONALIDAD_MENSUAL), media))
    print('')
    print('CAMPANAS, CANALES Y TRAMITES')
    print('  %d filas del calendario del kit: %d Alta / %d Media / %d Baja'
          % (len(CAMPANAS), temporadas['Alta'], temporadas['Media'], temporadas['Baja']))
    print('  campanas propias: %s'
          % ' / '.join(c['campana'] for c in CAMPANAS if c['campana_propia']))
    print('  valle: %s, y lo que para es el obrador. Envios parados %s'
          % (VALLE['nombre_mes'],
             '-'.join(MESES[x - 1][:3] for x in (VALLE['envios_parados_meses'][0],
                                                 VALLE['envios_parados_meses'][-1]))))
    print('  %d canales: %s'
          % (len(CANALES), ' / '.join('%s %.0f %%' % (c['canal'].split(' (')[0], c['ventas_pct'])
                                      for c in CANALES)))
    print('  %d de los 5 canales caen FUERA de la nota del 644.5 (salida: pregunta al '
          'asesor, NUNCA un epigrafe)' % len(fuera))
    print('  taller: %.1f asistentes para cubrir su coste, aforo %d'
          % (asistentes_punto_muerto_taller(), taller['aforo']))
    print('  checklist legal: %d tramites en %d fases / %d cambian por comunidad (%s)'
          % (len(CHECKLIST_LEGAL), len(FASES_CHECKLIST),
             sum(1 for f in CHECKLIST_LEGAL if f[6]), ', '.join(CCAA_EJEMPLO)))
    print('  ruta critica %.1f meses desde %s: %s'
          % (total_meses, MESES[MES_INICIO_PROYECTO - 1], ' > '.join(camino)))
    print('  apertura el %d de %s (temporada «%s» del kit) / holgura del pedido de '
          'equipos %.1f meses'
          % (NEGOCIO['dia_apertura_recomendado'], MESES[mes_ap - 1],
             campana(mes_ap)['temporada'], holgura['H6']))
    print('  %d cruces entre libros, todos por celda verde + fila de cuadre: %s'
          % (len(CRUCES), ' / '.join('%d<-%d' % (c['receptor'], c['origen']) for c in CRUCES)))
    print('  %d ids legales requeridos por los libros 4, 5, 8 y 9 / %d proveedores '
          'verificados / %d clientes de ejemplo'
          % (len(IDS_LEGALES_REQUERIDOS), len(PROVEEDORES), len(CLIENTES_B2B)))
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
