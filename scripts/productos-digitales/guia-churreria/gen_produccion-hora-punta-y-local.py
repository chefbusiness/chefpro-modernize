#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_produccion-hora-punta-y-local.py - libro 1 de «Cómo Montar una
Churrería-Chocolatería» (producto 51, `guia-churreria-chocolateria`; SPEC
`scripts/productos-digitales/guia-churreria-SPEC.md`, §2.1 fila 1, §2.2, §3.1 y §3.5).

Molde H+N: se calca de `guia-chocolateria/gen_capacidad-obrador-y-clima.py` la
estructura de Zonas y m², Capacidad por Equipo, Cuello de Botella y Ficha de Visita
(SIN la hoja de clima), y es NUEVO: Freidoras, Potencia y Riesgo, y Día Tipo y Día
Punta. El cierre (inject_cache + data_only + contrato + mapa + demo con pycel) se
calca del libro 3 de este mismo producto.

Hojas (`datos_ejemplo.HOJAS[1]`): Instrucciones · Parámetros · Zonas y m² · Equipos y
Capacidad · Freidoras, Potencia y Riesgo · Cuello de Botella · Día Tipo y Día Punta ·
Ficha de Visita a Local.

CRUCES (D16)
------------
* RECIBE X1 (kg de masa por ración media) y X1 bis (kilos fritos por kilo de masa), los dos
  del libro 3 (X1 bis, enmienda R-05a de la refutación: antes era una verde propia aquí y
  otra en el 3). Celda verde en «Parámetros»
  con el rótulo literal de `datos_ejemplo.rotulo_cruce()`, su valor por defecto
  (`valor_defecto` de `CRUCES`) y una fila de CUADRE con semáforo. Ninguna fórmula
  entre ficheros.
* ES ORIGEN de X3, X3 bis, X4, X6, X9 y X9 bis (superficie útil, `Zonas y m²`!L5). Celdas de origen = el CONTRATO de
  `datos_ejemplo.CRUCES`: rótulo en K y valor en L desde la fila 5 de cada hoja de
  origen. `main()` comprueba que cada una devuelve, a la precisión de la máquina, el
  `valor_defecto` que calcula `datos_ejemplo`.

DB-SI, RELEÍDO EL 03-10-2026 ANTES DE CONSTRUIR (SR-11)
------------------------------------------------------
Se abrió `codigotecnico.org/pdf/Documentos/SI/DBSI.pdf` (SI 1, tabla 2.1, fila
«Cocinas según potencia instalada P(2)(3)»: 20<P<=30 bajo, 30<P<=50 medio, P>50 alto).
La regla de qué aparatos computan NO está en una nota (1): está en la NOTA (2), junto a
la de 1 kW por litro y a la de la extinción automática; los filtros a 1,20/0,50 m son de
la nota (3), que sólo alcanza a las cocinas que son local de riesgo especial (o que lo
serían sin la extinción automática). La literal va en `NOTA_2_DBSI` y se cita en la
celda de los kW de los demás aparatos.

Frontera: sin «Demanda por Franja» ni «Cola del Domingo» (son del libro 5, C2); sin
clima ni carga térmica; no sustituye al proyecto técnico de la extracción.

Salida: build/produccion-hora-punta-y-local.xlsx + build/mapa-...json.
Uso: /usr/local/bin/python3 gen_produccion-hora-punta-y-local.py
Via: Claude Code
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

import openpyxl
from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Font, PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..'))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import _comun_churreria as CC                                  # noqa: E402
import motor                                                   # noqa: E402


def _importar_datos():
    spec = importlib.util.spec_from_file_location(
        'datos_ejemplo_churreria', os.path.join(AQUI, 'datos_ejemplo.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


D = _importar_datos()
import enmiendas_churreria                                     # noqa: E402
enmiendas_churreria.aplicar(D)      # R-04/05/06/13/14/15: el contrato de cruces enmendado
motor.CTX['producto'] = CC.PID

LIBRO = 1
FICHERO = D.LIBROS[LIBRO]
NOMBRE = os.path.splitext(FICHERO)[0]
TITULO = 'Producción, Hora Punta y Local'
SUBJECT = CC.PRODUCTO + ' · Versión 1.0 · octubre 2026'
assert NOMBRE == 'produccion-hora-punta-y-local'

(H_INS, H_PAR, H_ZON, H_EQU, H_FRE, H_CUE, H_DIA, H_FIC) = D.HOJAS[LIBRO]

PR = D.PRODUCCION


def dp(clave):
    return D.dato(PR, clave)


#: Nota (2) de la tabla 2.1 del DB-SI, copiada del PDF oficial el 03-10-2026.
NOTA_2_DBSI = ('Nota (2) de la tabla 2.1 (DB-SI, SI 1): «Para determinar la potencia '
               'instalada sólo se considerarán los aparatos directamente destinados a la '
               'preparación de alimentos y susceptibles de provocar ignición. Las freidoras '
               'y las sartenes basculantes se computarán a razón de 1 kW por cada litro de '
               'capacidad, independientemente de la potencia que tengan. En usos distintos '
               'de Hospitalario y Residencial Público no se consideran locales de riesgo '
               'especial las cocinas cuyos aparatos estén protegidos con un sistema '
               'automático de extinción, aunque incluso en dicho caso les es de aplicación '
               'lo que se establece en la nota (3).» Leída el 03-10-2026.')


def Q(hoja):
    return "'" + hoja + "'!"


def ABS_(hoja, coord):
    m = re.match(r'([A-Z]+)(\d+)$', coord)
    return Q(hoja) + '$' + m.group(1) + '$' + m.group(2)


# --------------------------------------------------------------------------
# Formato y utilidades (segunda capa; la primera es `_comun_churreria.py`)
# --------------------------------------------------------------------------
ORO = 'FFD700'
GRIS = '888888'
CAB_BG, CAB_FG = '2D2D2D', 'FFFFFF'
CREMA = 'FFF8E1'
PCT = motor.FMT_PCT
ENT = motor.FMT_ENT
DEC = '#,##0.00'
DEC1 = '#,##0.0'
DEC4 = '#,##0.0000'
M2 = CC.FMT_M2
METROS = '0.00 "m"'

NOTAS_LEGALES = []
VERDES = []
RECEPTORAS = []      # (hoja, coord del valor, rótulo, cruce)
CUADRES = []         # (hoja, coord)

SI_NO = ('Sí', 'No')
TIPOS_APARATO = ('Gas', 'Parrilla', 'Otro')
RESPUESTAS = ('Sí', 'No', 'Por comprobar')


def sino(b):
    return 'Sí' if b else 'No'


def cabecera_hoja(ws, titulo, nota_txt=None):
    motor.val(ws, 'A1', CC.titulo_hoja(titulo), bold=True)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    motor.val(ws, 'A2', CC.SUBTITULO)
    ws['A2'].font = Font(size=10, color=GRIS)
    if nota_txt:
        motor.val(ws, 'A3', nota_txt)
        ws['A3'].font = Font(italic=True, size=9)


def seccion(ws, coord, texto):
    motor.val(ws, coord, texto, bold=True)
    ws[coord].font = Font(bold=True, size=12, color=ORO)


def gris(ws, coord, texto, alto=None):
    motor.val(ws, coord, texto, wrap=True)
    ws[coord].font = Font(size=8, color=GRIS)
    if alto:
        ws.row_dimensions[int(re.sub(r'[A-Z]', '', coord))].height = alto
    return ws[coord]


def encabezados(ws, fila, cols, alto=42, congelar=True):
    for letra, texto, ancho in cols:
        cel = ws[letra + str(fila)]
        cel.value = texto
        cel.font = Font(bold=True, color=CAB_FG, size=9)
        cel.fill = PatternFill('solid', fgColor=CAB_BG)
        cel.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        if ancho is not None:
            ws.column_dimensions[letra].width = ancho
    ws.row_dimensions[fila].height = alto
    if congelar:
        ws.freeze_panes = 'A%d' % (fila + 1)


def crema(cel):
    cel.fill = PatternFill('solid', fgColor=CREMA)
    return cel


def entrada(ws, coord, valor, fmt=None, etiqueta=''):
    """Celda VERDE con su valor por defecto. Ninguna verde vacía."""
    if valor is None or (isinstance(valor, str) and not valor.strip()):
        raise SystemExit('entrada(%s!%s, «%s») sin valor por defecto' % (ws.title, coord, etiqueta))
    cel = motor.val(ws, coord, valor, fmt=fmt, verde_=True)
    VERDES.append((ws.title, coord, etiqueta, valor))
    return cel


def formula(ws, coord, texto, fmt=None, bold=None, destacar=False):
    cel = motor.f(ws, coord, texto, fmt=fmt, bold=bold)
    if destacar:
        crema(cel)
    return cel


def nota_legal(ws, coord, pid, extra=None):
    texto = D.nota_legal(pid)
    if not texto:
        raise SystemExit('nota_legal(%r) vacía: gate_legal() debería haber abortado' % pid)
    if extra:
        texto = texto + ' | ' + extra
    ws[coord].comment = Comment(texto, 'AI Chef Pro', height=170, width=520)
    NOTAS_LEGALES.append((ws.title, coord, pid))
    return texto


RX_ID = D.RX_ID


def nota_fuente(ws, coord, fuente, extra=None):
    """Procedencia de un dato de SECTOR (CUS-*, CHS-*): id, fiabilidad y URL. No copia
    el «tema» de la ficha (hay temas que nombran una cifra vetada para refutarla)."""
    partes = []
    for pid in RX_ID.findall(fuente or ''):
        if pid in D.IDS_PROHIBIDOS:
            raise SystemExit('El id %s está PROHIBIDO (SPEC §5.1) y no puede ser fuente' % pid)
        if pid.startswith('CUN-') or pid.startswith('CHN-'):
            continue
        f = D.ficha_comun(pid)
        if not f:
            raise SystemExit('El id %s no existe en el JSON común' % pid)
        url = str(f.get('url') or '').strip()
        fiab = str(f.get('fiabilidad') or '').strip()
        partes.append('%s%s%s' % (pid, ' · fiabilidad ' + fiab if fiab else '',
                                  ' · ' + url if url else ''))
    if extra:
        partes.append(extra)
    if not partes:
        return None
    ws[coord].comment = Comment('Fuente: ' + ' | '.join(partes), 'AI Chef Pro',
                                height=110, width=440)
    return partes


def texto_fuente(fuente):
    if not fuente:
        return ''
    if fuente == 'supuesto':
        return 'supuesto declarado'
    if fuente.startswith('heredado'):
        return 'heredado de la hermana'
    return fuente


def setup(ws, apaisado=True, titulos=None):
    CC.pagina(ws, apaisado=apaisado, titulos=titulos)


def bloque_contrato(ws, filas, titulo='Lo que Copian Otros Libros (No Muevas Estas Celdas)'):
    """El CONTRATO de `datos_ejemplo.CRUCES`: rótulo en K y valor en L desde la fila 5."""
    seccion(ws, 'K4', titulo)
    for fila, rotulo, form, fmt in filas:
        motor.val(ws, 'K%d' % fila, rotulo, wrap=True)
        ws['K%d' % fila].font = Font(bold=True, size=9)
        formula(ws, 'L%d' % fila, form, fmt=fmt, bold=True, destacar=True)
        destinos = []
        for c in D.CRUCES:
            if c['origen'] == LIBRO and c['hoja_origen'] == ws.title and c['celda_origen'] == 'L%d' % fila:
                destinos.append('libro %d (%s, hoja %s, %s)' % (c['receptor'], c['fichero_receptor'],
                                                               c['hoja_receptor'], c['x']))
        if destinos:
            gris(ws, 'M%d' % fila, 'Lo copia: ' + '; '.join(sorted(set(destinos))))
        ws.row_dimensions[fila].height = max(ws.row_dimensions[fila].height or 15, 30)
    ws.column_dimensions['K'].width = max(ws.column_dimensions['K'].width or 0, 40)
    ws.column_dimensions['L'].width = max(ws.column_dimensions['L'].width or 0, 14)
    ws.column_dimensions['M'].width = max(ws.column_dimensions['M'].width or 0, 48)


def listas(ws, fila, defs, col='A'):
    refs, sig = CC.bloque_listas(ws, fila, defs, col=col)
    return refs, sig


# ==========================================================================
# Posiciones
# ==========================================================================
# ---- Parámetros ----------------------------------------------------------
P = {}
_fila = 6
for _k in ('m2_total', 'm2_terraza'):
    P[_k] = _fila
    _fila += 1
P_SEC_CTE = _fila                         # 8
_fila += 1
for _k in ('kw_por_litro_freidora', 'riesgo_bajo_desde_kw', 'riesgo_medio_desde_kw',
           'riesgo_alto_desde_kw', 'distancia_filtro_gas_m', 'distancia_filtro_parrilla_m',
           'distancia_filtro_otro_m'):
    P[_k] = _fila
    _fila += 1
P_SEC_PROD = _fila                        # 16
_fila += 1
for _k in ('dias_tipo_semana', 'dias_punta_semana', 'minutos_hora',
           'tolerancia_cuadre'):
    P[_k] = _fila
    _fila += 1
P_SEC_CRU = _fila                         # 22
P_X1 = P_SEC_CRU + 1                      # 23
P_X1_ORIG = P_X1 + 1
P_X1_DESV = P_X1 + 2
P_X1_CUAD = P_X1 + 3
#: X1 bis (R-05a): los kilos fritos por kilo de masa dejan de ser una verde propia del 1 y
#: se copian del libro 3, donde nacen. La celda recibida ES `P['kg_fritos_por_kg_masa']`.
P_X1B = P_X1_CUAD + 1
P_X1B_ORIG = P_X1B + 1
P_X1B_DESV = P_X1B + 2
P_X1B_CUAD = P_X1B + 3
P['kg_fritos_por_kg_masa'] = P_X1B


def PB(clave):
    return ABS_(H_PAR, 'B%d' % P[clave])


X1_CELDA = ABS_(H_PAR, 'B%d' % P_X1)

# ---- Zonas y m² --------------------------------------------------------------
Z_INI = 6
Z_FIN = Z_INI + len(D.ZONAS) - 1
Z_TOT = Z_FIN + 2
Z = dict(decl=Z_TOT + 1, desc=Z_TOT + 2, prod=Z_TOT + 4, prod_pct=Z_TOT + 5,
         aten=Z_TOT + 6, aten_pct=Z_TOT + 7, serv=Z_TOT + 8, terr=Z_TOT + 9)

# ---- Equipos y Capacidad ------------------------------------------------------
E_PERS = 5
E_CAB = 8
EQUIPOS = [
    # (eslabón, modo, kg por ciclo, minutos por ciclo, kg/h directos, fuentes, nota)
    ('Línea de dosificado y fritura (con su churrero/a)', 'directo', None, None,
     dp('kg_masa_h_linea'), D.PRODUCCION['kg_masa_h_linea'][1],
     'Los kilos de masa por hora que la línea saca DE VERDAD con la persona que la '
     'trabaja. Nunca el máximo del folleto del fabricante: mídelo un domingo, pesando la '
     'masa que entra en una hora.'),
    ('Freidora (por tandas)', 'ciclo', dp('carga_tanda_kg'), dp('minutos_tanda'), None,
     D.PRODUCCION['carga_tanda_kg'][1],
     'Kilos de masa que caben en una tanda y minutos de la carga al escurrido. Con dos '
     'cubas, la freidora deja de mandar; mira antes qué le pasa al riesgo de incendio en '
     'la hoja «Freidoras, Potencia y Riesgo».'),
    ('Amasadora', 'ciclo', dp('kg_por_amasado'), dp('minutos_amasado'), None,
     D.PRODUCCION['kg_por_amasado'][1],
     'Capacidad declarada de la amasadora automática del ejemplo y minutos de un amasado '
     'completo (supuesto). Casi nunca manda: amasa mucho más deprisa de lo que se fríe.'),
]
E_INI = E_CAB + 1
E_FIN = E_INI + len(EQUIPOS) - 1
E_PORPERS = E_FIN + 3
EQ_ROW = dict((e[0], E_INI + i) for i, e in enumerate(EQUIPOS))
FILA_FREIDORA = E_INI + 1
FILA_AMASADORA = E_INI + 2

# ---- Freidoras, Potencia y Riesgo -----------------------------------------------
F_CAB = 5
FREIDORAS = [
    ('Freidora de churros de una cuba', True, dp('litros_freidora'),
     dp('tipo_aparato').capitalize(), D.PRODUCCION['litros_freidora'][1],
     'La freidora de gas de 25 L del ejemplo, bajo la campana. Si es eléctrica, cambia el '
     'tipo a «Otro»: la distancia del filtro baja y la potencia a contratar sube.'),
    ('Segunda freidora (la decisión «¿una churrera o dos?»)', False, dp('litros_freidora'),
     dp('tipo_aparato').capitalize(), 'supuesto',
     'Marcada «No» a propósito. Cámbiala a «Sí» y mira cómo se mueven los kW computables, '
     'el riesgo de la cocina y la extinción automática ANTES de comprarla.'),
]
F_INI = F_CAB + 1
F_FIN = F_INI + len(FREIDORAS) - 1
F = {}
_f = F_FIN + 2
for _k in ('litros', 'kw_fre', 'kw_otros', 'kw', 'riesgo', 'ext_num', 'ext_txt'):
    F[_k] = _f
    _f += 1
_f += 1
F['sec_nota2'] = _f
_f += 1
for _k in ('protege', 'uso', 'veredicto', 'nota3', 'dist', 'obliga'):
    F[_k] = _f
    _f += 1
F_LISTAS = _f + 2

# ---- Cuello de Botella ------------------------------------------------------------
K = dict(cap_kg=6, manda=7, seg_kg=8, seg=9, kgrac=10, cap_rac=11, por_pers=12,
         sec_h=14, h_tipo=15, h_punta=16, sobra_punta=17)

# ---- Día Tipo y Día Punta ---------------------------------------------------------
DT = dict(cab=5, rac=6, kgrac=7, masa=8, fpk=9, fritos=10, tandas=11, amasados=12, horas=13,
          sec_sem=15, rac_sem=16, masa_sem=17, rac_media=18)

# ---- Ficha de Visita a Local --------------------------------------------------------
L_CAB = 5
L_INI = 6


def _items_ficha():
    """Los cuatro eliminatorios de `datos_ejemplo`, en su orden, y los no eliminatorios.
    (ítem, ¿elim?, cómo, respuesta, descarta, obliga, dato (fórmula o None), fmt, nota, ids)"""
    elim = D.FICHA_VISITA_ELIMINATORIOS
    como = [
        'Pregunta al técnico, con el plano delante, por dónde subiría el conducto. Si cruza '
        'fachada, patio o cubierta comunitaria, la obra lleva proyecto.',
        'Sube a la cubierta con el propietario y pide por escrito el permiso de la comunidad '
        'ANTES de firmar.',
        'Pide el certificado de la última inspección de la instalación de gas del local o '
        'pregunta a la distribuidora si llega la acometida.',
        'Lleva los kW de la hoja «Freidoras, Potencia y Riesgo» a la visita y pregunta al '
        'técnico si la cocina puede quedar sectorizada como local de riesgo especial.',
    ]
    resp_molinete = [
        ('Sí', 'Ninguna', 'Sí'),     # obra nueva sin salida de humos: lleva proyecto
        ('Sí', 'No', 'Ninguna'),
        ('Sí', 'No', 'Ninguna'),
        ('Sí', 'No', 'Ninguna'),
    ]
    out = []
    for i, (item, pid, notatxt) in enumerate(elim):
        r, desc, obl = resp_molinete[i]
        dato = None
        if i == 3:
            # R-02: el DATO (kW computables y veredicto), no el rótulo de la fila
            dato = ('=ROUND(%s,0)&" kW · "&%s' % (ABS_(H_FRE, 'D%d' % F['kw']),
                                                  ABS_(H_FRE, 'D%d' % F['riesgo'])), None)
        out.append((item, 'Sí', como[i], r, desc, obl, dato, notatxt, pid))
    out += [
        ('¿La superficie útil llega a los m² que has repartido por zonas?', 'No',
         'Superficie útil real, sin muros ni patinillos. El anuncio suele dar la construida.',
         'Sí', 'No', 'Ninguna', ('=%s' % ABS_(H_ZON, 'D%d' % Z_TOT), M2),
         'Entre la superficie construida y la útil se van con facilidad diez metros. El dato '
         'de la derecha es lo que has repartido en «Zonas y m²».', None),
        ('¿Caben el aseo de público y el vestuario del personal?', 'No',
         'Dibújalos sobre el plano con sus puertas antes de firmar.', 'Sí', 'No', 'Ninguna',
         None, 'Si no caben, el local no sirve aunque el resto encaje: es obra o es otro local.',
         None),
        ('¿Hay sitio para el almacén y el bidón del aceite usado?', 'No',
         'Mide el hueco del almacén: harina, aceite nuevo, envases y el bidón que espera al '
         'gestor.', 'Sí', 'No', 'Ninguna', None,
         'El bidón del aceite usado no puede quedarse en la zona de fritura ni en la sala.',
         None),
        ('¿La acera admite terraza y el ayuntamiento la autoriza?', 'No',
         'Pregunta en el ayuntamiento por la ocupación de la vía pública en esa calle.',
         'Por comprobar', 'No', 'Ninguna', None,
         'La terraza va con autorización propia, aparte de la actividad: la ocupación de la '
         'vía pública queda fuera del régimen de declaración responsable.', 'CUN-35'),
    ]
    return out


ITEMS = []
L_FIN = None


# ==========================================================================
# Hoja «Instrucciones»
# ==========================================================================
PASOS = [
    '1. Hoja «Parámetros». La superficie del local, los umbrales del Código Técnico para '
    'las cocinas (1 kW por litro de freidora, riesgo bajo, medio y alto, distancia de los '
    'filtros) y las dos celdas verdes donde copias del libro 3 los kilos de masa por ración '
    'media y los kilos fritos por kilo de masa, cada una con su fila de CUADRE.',
    '2. Hoja «Zonas y m²». Reparte los metros del local en sus seis zonas. La terraza va '
    'aparte y con su propia autorización.',
    '3. Hoja «Equipos y Capacidad». Los kilos de masa por hora que saca de verdad cada '
    'eslabón: la línea con su churrero/a, la freidora por tandas y la amasadora. Y cuántas '
    'personas hay en la línea en el pico del fin de semana.',
    '4. Hoja «Freidoras, Potencia y Riesgo». Los litros y el tipo de cada freidora, los kW '
    'de los demás aparatos de cocción y si proteges los aparatos con extinción automática. '
    'Sale el riesgo de la cocina, si la extinción automática es obligatoria y a qué '
    'distancia van los filtros.',
    '5. Hoja «Cuello de Botella». El eslabón que manda y las raciones por hora que aguanta '
    'el conjunto, y cuántas horas de línea te pide el día tipo y el día punta.',
    '6. Hoja «Día Tipo y Día Punta». Las raciones de un día de diario y de un sábado, '
    'domingo o festivo. Es la ÚNICA fuente de la demanda base de todo el paquete: de aquí '
    'salen los kilos de masa, los kilos fritos, las tandas y los amasados.',
    '7. Hoja «Ficha de Visita a Local». Imprímela y llévala a cada visita. Los cuatro '
    'eliminatorios van primero y en este orden: la extracción, el conducto a cubierta, el '
    'gas y la potencia con el riesgo de incendio.',
]

NOTAS_LIBRO = [
    'UNA RACIÓN, EN ESTE PAQUETE, ES LA UNIDAD DE VENTA MEDIA DE LA CARTA (la define el libro '
    '3): una ración de churros, una taza, un café o una docena cuentan como una cada una. Por '
    'eso los kilos de masa por ración media se copian del libro 3 y no se calculan aquí.',
    'LA CAPACIDAD SE MIDE EN KILOS DE MASA, NO EN CHURROS. La línea, la freidora y la '
    'amasadora se comparan en la misma unidad, y sólo al final se pasan a raciones por hora. '
    'Los valores de El Molinete son supuestos declarados: el que vale es el que midas tú.',
    'EL RIESGO DE INCENDIO NO DEPENDE DE LA POTENCIA DE LA FREIDORA, SINO DE SUS LITROS. El '
    'Código Técnico computa las freidoras a 1 kW por litro de capacidad, se pongan como se '
    'pongan, y suma los demás aparatos de cocción. Por encima de 20 kW la cocina es local de '
    'riesgo especial; por encima de 50 kW la extinción automática es obligatoria.',
    'ESTE LIBRO NO SUSTITUYE AL PROYECTO TÉCNICO DE LA EXTRACCIÓN. Te dice qué preguntar y '
    'qué umbral te toca; el caudal, la sección y el trazado del conducto los fija el técnico. '
    'La actividad puede ir por declaración responsable, pero las obras que necesitan '
    'proyecto -el conducto a cubierta, casi siempre- siguen necesitando su licencia de obra.',
    'DÓNDE NO ESTÁ LO QUE AQUÍ NO ESTÁ. El reparto de la demanda por franjas del día, la '
    'capacidad contra el pico y la cola del domingo viven en el libro 5; el coste de las '
    'máquinas y de la obra, en el 2; la plantilla y los turnos, en el 8; el papeleo de la '
    'licencia, los humos y el gas, en el 7. Este libro no calcula clima ni carga térmica.',
]

CADENCIA = ('Cada cuánto se usa este libro: la «Ficha de Visita a Local», una vez por cada '
            'local que visites, y guarda las de los que descartes. «Freidoras, Potencia y '
            'Riesgo», antes de firmar y cada vez que cambies de freidora. «Equipos y '
            'Capacidad» y «Día Tipo y Día Punta», al abrir con tus propias medidas y a los '
            'tres meses con las raciones reales del TPV. Cada vez que cambie una cifra del '
            'bloque «Lo que Copian Otros Libros», cópiala de nuevo en los libros que la usan.')


def _orden_relleno():
    partes = ['%d (%s)' % (n, D.LIBROS[n]) for n in D.ORDEN_RELLENO if n != 7]
    return ('Orden de relleno del paquete: ' + ', luego '.join(partes)
            + '. El libro 7 (%s) no depende de ninguno: rellénalo cuando quieras. Este es el '
              'libro 1 y va el SEGUNDO: antes, el libro 3, del que copias los kilos de masa por '
              'ración media.' % D.LIBROS[7])


def _destinos_texto():
    por_celda = {}
    for c in D.CRUCES:
        if c['origen'] != LIBRO:
            continue
        clave = (c['hoja_origen'], c['celda_origen'])
        por_celda.setdefault(clave, {'concepto': c['concepto'], 'destinos': []})
        por_celda[clave]['destinos'].append('libro %d (%s)' % (c['receptor'], c['x']))
    lineas = []
    for (hoja, celda), d in sorted(por_celda.items(),
                                    key=lambda kv: (D.HOJAS[LIBRO].index(kv[0][0]), int(kv[0][1][1:]))):
        lineas.append('%s!%s - %s. Lo copia: %s.' % (hoja, celda, d['concepto'],
                                                    ', '.join(sorted(set(d['destinos'])))))
    return lineas


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS, 0)
    ws.column_dimensions['A'].width = 100.0
    cabecera_hoja(ws, TITULO)
    motor.val(ws, 'A3', 'Para qué sirve: decidir si ese local admite una freidora y cuánto '
                        'produce tu línea, con la demanda base de un día de diario y de un día '
                        'punta. Responde a dos preguntas: ¿una churrera o dos? y ¿ese local sirve?')
    ws['A3'].font = Font(italic=True, size=9)
    fila = 5
    seccion(ws, 'A%d' % fila, 'Instrucciones de Uso')
    fila += 1
    entrada(ws, 'A%d' % fila, motor.NOTA_VERDES, etiqueta='Leyenda de celdas verdes')
    fila += 1
    motor.val(ws, 'A%d' % fila, 'Las celdas en crema son resultados que el libro calcula; las '
                                'blancas con fórmula, también. No escribas encima.', wrap=True)
    fila += 2
    for paso in PASOS:
        motor.val(ws, 'A%d' % fila, paso, wrap=True)
        ws.row_dimensions[fila].height = 46
        fila += 1
    fila += 1
    seccion(ws, 'A%d' % fila, 'Orden de Relleno y Lo que Este Libro Pasa a los Demás')
    fila += 1
    motor.val(ws, 'A%d' % fila, _orden_relleno(), wrap=True)
    ws.row_dimensions[fila].height = 58
    fila += 1
    motor.val(ws, 'A%d' % fila,
              'Ningún libro se vincula con otro por fórmula. Lo que este libro necesita del 3 '
              'se copia a mano en la celda verde de «Parámetros», y una fila de CUADRE avisa si '
              'se ha quedado vieja. Lo que este libro pasa a los demás está en el bloque «Lo '
              'que Copian Otros Libros» de cada hoja (rótulo en la columna K, valor en la L):',
              wrap=True)
    ws.row_dimensions[fila].height = 44
    fila += 1
    for linea in _destinos_texto():
        motor.val(ws, 'A%d' % fila, linea, wrap=True)
        ws['A%d' % fila].font = Font(size=9)
        ws.row_dimensions[fila].height = 28
        fila += 1
    fila += 1
    seccion(ws, 'A%d' % fila, 'Lo que Conviene Saber Antes de Empezar')
    fila += 1
    for txt in NOTAS_LIBRO:
        motor.val(ws, 'A%d' % fila, txt, wrap=True)
        ws.row_dimensions[fila].height = 62
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, CADENCIA, wrap=True)
    ws.row_dimensions[fila].height = 58
    fila += 2
    motor.val(ws, 'A%d' % fila, CC.NOTA_DESPROTEGER, wrap=True)
    fila += 2
    motor.val(ws, 'A%d' % fila, CC.BIO, wrap=True)
    fila += 1
    motor.val(ws, 'A%d' % fila, CC.VERSION_LINE)
    ws['A%d' % fila].font = Font(size=8, italic=True)
    setup(ws, apaisado=False)
    return ws


# ==========================================================================
# Hoja «Parámetros»
# ==========================================================================
def fila_param(ws, fila, etiqueta, valor, fmt, unidad, fuente, nota, ids_legales=(),
               pct=False, verde=True, extra_legal=None):
    motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
    if verde:
        cel = entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
        if pct:
            motor.dv_porcentaje(ws, [cel.coordinate])
        elif isinstance(valor, (int, float)) and not isinstance(valor, bool):
            motor.dv_numerica(ws, [cel.coordinate], minimo=0)
    else:
        cel = motor.val(ws, 'B%d' % fila, valor, fmt=fmt)
    motor.val(ws, 'C%d' % fila, unidad)
    motor.val(ws, 'D%d' % fila, texto_fuente(fuente), wrap=True)
    ws['D%d' % fila].font = Font(size=8, color=GRIS)
    gris(ws, 'E%d' % fila, nota)
    ws.row_dimensions[fila].height = 44
    for pid in ids_legales:
        nota_legal(ws, cel.coordinate, pid, extra=extra_legal)
    if not ids_legales:
        nota_fuente(ws, cel.coordinate, fuente)
    return cel


def _bloque_receptor(ws, c, filas, fmt, desc, que_cuadra):
    """Un cruce recibido: la celda verde con el rótulo literal, lo que publica hoy la celda de
    origen (anótalo), la desviación y la fila de CUADRE (la misma plantilla para X1 y X1 bis)."""
    rec, orig, desv, cuad = filas
    rot = D.rotulo_cruce(c)
    libro = c['origen']
    motor.val(ws, 'A%d' % rec, rot, wrap=True)
    ws['A%d' % rec].font = Font(bold=True, size=9)
    entrada(ws, 'B%d' % rec, c['valor_defecto'], fmt=fmt, etiqueta='%s %s' % (c['x'], c['concepto']))
    motor.dv_numerica(ws, ['B%d' % rec], minimo=0)
    motor.val(ws, 'C%d' % rec, c['unidad'])
    motor.val(ws, 'D%d' % rec, 'cruce %s (libro %d)' % (c['x'], libro))
    ws['D%d' % rec].font = Font(size=8, color=GRIS)
    gris(ws, 'E%d' % rec, desc)
    ws.row_dimensions[rec].height = 52
    RECEPTORAS.append((H_PAR, 'B%d' % rec, rot, c))

    motor.val(ws, 'A%d' % orig, 'Lo que publica hoy esa celda del libro %d (anótalo cada vez que '
                                'lo abras)' % libro, wrap=True)
    entrada(ws, 'B%d' % orig, c['valor_defecto'], fmt=fmt,
            etiqueta='%s lo que publica el libro %d' % (c['x'], libro))
    motor.dv_numerica(ws, ['B%d' % orig], minimo=0)
    motor.val(ws, 'C%d' % orig, c['unidad'])
    gris(ws, 'E%d' % orig, 'Si arriba usas otra cifra -porque has cambiado la carta o la masa-, la '
                           'fila de CUADRE te avisa en vez de dejar las dos separadas en silencio.')
    ws.row_dimensions[orig].height = 40
    motor.val(ws, 'A%d' % desv, 'Desviación entre las dos')
    formula(ws, 'B%d' % desv, '=IFERROR(ABS(B%d-B%d)/B%d,"")' % (rec, orig, orig), fmt=PCT)
    motor.semaforo_isnumber(ws, 'B%d' % desv, '$B$%d' % desv, '>', '$B$%d' % P['tolerancia_cuadre'])
    motor.val(ws, 'A%d' % cuad, 'CUADRE: %s' % que_cuadra, wrap=True)
    ws['A%d' % cuad].font = Font(bold=True)
    ko = 'REVISA: no es lo que publica el libro %d' % libro
    formula(ws, 'B%d' % cuad,
            '=IF(NOT(ISNUMBER(B%d)),"",IF(B%d<=B%d,"CUADRA","%s"))'
            % (desv, desv, P['tolerancia_cuadre'], ko), bold=True, destacar=True)
    motor.semaforo_texto(ws, 'B%d' % cuad, (('CUADRA', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                                            (ko, motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    ws.row_dimensions[cuad].height = 34
    CUADRES.append((H_PAR, 'B%d' % cuad))


def hoja_parametros(wb):
    ws = wb.create_sheet(H_PAR)
    cabecera_hoja(ws, H_PAR, 'Lo que vale para todo el libro. Ninguna fórmula lleva un número '
                             'dentro: los umbrales, las distancias y las conversiones viven aquí.')
    encabezados(ws, 4, [('A', 'Parámetro', 46), ('B', 'Valor', 16), ('C', 'Unidad', 14),
                        ('D', 'Procedencia', 22), ('E', 'Nota', 80)])
    N = D.NEGOCIO
    seccion(ws, 'A5', 'El Local')
    fila_param(ws, P['m2_total'], 'Superficie útil del local', D.dato(N, 'm2_total'), DEC1, 'm²',
               N['m2_total'][1],
               'El caso de El Molinete: 75 m² en seis zonas, la cifra en la que convergen dos '
               'traspasos reales del mismo formato. Pon la útil de tu local, no la del anuncio.')
    fila_param(ws, P['m2_terraza'], 'Terraza (aparte de la superficie útil)',
               D.dato(N, 'm2_terraza'), DEC1, 'm²', N['m2_terraza'][1],
               'Supuesto de El Molinete. Va aparte de los metros del local y con su propia '
               'autorización de ocupación de la vía pública.')

    seccion(ws, 'A%d' % P_SEC_CTE, 'Cocina y Riesgo de Incendio (Código Técnico, DB-SI)')
    nl = 'Umbral de la tabla 2.1 del DB-SI para las cocinas según su potencia instalada.'
    fila_param(ws, P['kw_por_litro_freidora'], 'kW que computa cada litro de freidora',
               dp('kw_por_litro_freidora'), DEC1, 'kW por litro', 'CUN-26',
               'Las freidoras se computan a 1 kW por litro de capacidad, tengan la potencia que '
               'tengan. Es la nota (2) de la tabla 2.1 del DB-SI.', ids_legales=('CUN-26',),
               extra_legal=NOTA_2_DBSI)
    fila_param(ws, P['riesgo_bajo_desde_kw'], 'Riesgo especial BAJO con más de',
               dp('riesgo_bajo_desde_kw'), DEC1, 'kW', 'CUN-26',
               nl + ' Hasta aquí la cocina no es local de riesgo especial.', ids_legales=('CUN-26',))
    fila_param(ws, P['riesgo_medio_desde_kw'], 'Riesgo especial MEDIO con más de',
               dp('riesgo_medio_desde_kw'), DEC1, 'kW', 'CUN-26', nl, ids_legales=('CUN-26',))
    fila_param(ws, P['riesgo_alto_desde_kw'], 'Riesgo especial ALTO (y extinción automática '
               'obligatoria) con más de', dp('riesgo_alto_desde_kw'), DEC1, 'kW', 'CUN-26',
               nl + ' Por encima, el sistema automático de extinción es obligatorio (SI 4).',
               ids_legales=('CUN-26',))
    fila_param(ws, P['distancia_filtro_gas_m'], 'Distancia mínima del filtro al foco: aparato de gas',
               dp('distancia_filtro_gas_m'), METROS, 'm', 'CUN-26',
               'Nota (3) de la tabla 2.1: más de 1,20 m si el aparato es de gas o de parrilla.',
               ids_legales=('CUN-26',))
    fila_param(ws, P['distancia_filtro_parrilla_m'], 'Distancia mínima del filtro al foco: '
               'aparato de parrilla', dp('distancia_filtro_parrilla_m'), METROS, 'm', 'CUN-26',
               'Nota (3) de la tabla 2.1: lo mismo que el gas, más de 1,20 m.',
               ids_legales=('CUN-26',))
    fila_param(ws, P['distancia_filtro_otro_m'], 'Distancia mínima del filtro al foco: otros '
               'aparatos', dp('distancia_filtro_otro_m'), METROS, 'm', 'CUN-26',
               'Nota (3) de la tabla 2.1: más de 0,50 m con los demás tipos (la freidora '
               'eléctrica, por ejemplo); con gas o parrilla son 1,20 m.', ids_legales=('CUN-26',))

    seccion(ws, 'A%d' % P_SEC_PROD, 'Producción y Calendario')
    dias_punta = sum(1 for d in D.DIAS if d in ('S', 'D'))
    dias_tipo = len(D.DIAS) - dias_punta
    fila_param(ws, P['dias_tipo_semana'], 'Días tipo por semana (de lunes a viernes)', dias_tipo,
               ENT, 'días', 'calendario',
               'El festivo entre semana se trabaja como un domingo: cuéntalo como día punta.')
    fila_param(ws, P['dias_punta_semana'], 'Días punta por semana (sábado y domingo)', dias_punta,
               ENT, 'días', 'calendario',
               'Sábados, domingos y festivos: la demanda del día punta.')
    fila_param(ws, P['minutos_hora'], 'Minutos que tiene una hora', 60, ENT, 'min/h',
               'conversión', 'Conversión de unidades. Vive aquí para que ninguna fórmula lleve '
               'un número dentro.', verde=False)
    fila_param(ws, P['tolerancia_cuadre'], 'Tolerancia de la fila de CUADRE', 0.02, PCT,
               'desviación', 'heredado: guia-chocolateria (Tolerancia de las filas de CUADRE)',
               'Por encima de esta desviación, la fila de CUADRE avisa de que lo que has copiado '
               'del libro 3 ya no es lo que aquel publica.', pct=True)

    # ---- X1 y X1 bis ----------------------------------------------------------
    seccion(ws, 'A%d' % P_SEC_CRU, 'Lo que Copias de Otros Libros')
    cruces = [c for c in D.CRUCES if c['receptor'] == LIBRO]
    assert [c['x'] for c in cruces] == ['X1', 'X1 bis'], cruces
    _bloque_receptor(
        ws, cruces[0], (P_X1, P_X1_ORIG, P_X1_DESV, P_X1_CUAD), DEC4,
        'Kilos de masa (merma incluida) por ración media de tu carta, mix de invierno. Con este '
        'número las raciones por hora salen de los kilos por hora de la línea. Nace con el de '
        'El Molinete.',
        'los kilos por ración que usas frente a los que publica el libro 3')
    _bloque_receptor(
        ws, cruces[1], (P_X1B, P_X1B_ORIG, P_X1B_DESV, P_X1B_CUAD), DEC,
        'Supuesto de El Molinete, que nace en el libro 3 (hoja «Parámetros»): pesa una tanda de '
        'masa antes y después de freír. Se copia de allí para que la masa tenga una sola cifra '
        'en todo el paquete; con él se pasan los kilos de masa a kilos fritos.',
        'los kilos fritos por kilo de masa que usas frente a los que publica el libro 3')
    setup(ws, titulos='4:4')
    return ws


# ==========================================================================
# Hoja «Zonas y m²»
# ==========================================================================
def hoja_zonas(wb):
    ws = wb.create_sheet(H_ZON)
    cabecera_hoja(ws, H_ZON, 'Las seis zonas de una churrería-chocolatería con obrador de masa a '
                             'la vista, freidora bajo campana, barra y sala. La terraza, aparte.')
    encabezados(ws, 5, [('A', 'Nº', 5), ('B', 'Zona', 42), ('C', 'Bloque', 18), ('D', 'm²', 11),
                        ('E', '% del local', 11), ('F', 'Qué tiene que cumplir', 90)])
    for i, (zona, m2, fuente, notatxt) in enumerate(D.ZONAS):
        r = Z_INI + i
        motor.val(ws, 'A%d' % r, i + 1, fmt=ENT)
        motor.val(ws, 'B%d' % r, zona, wrap=True)
        motor.val(ws, 'C%d' % r, D.ZONA_A_BLOQUE[zona])
        entrada(ws, 'D%d' % r, m2, fmt=DEC1, etiqueta='m² de ' + zona)
        formula(ws, 'E%d' % r, '=IFERROR(D%d/$D$%d,"")' % (r, Z_TOT), fmt=PCT)
        motor.val(ws, 'F%d' % r, notatxt, wrap=True)
        ws.row_dimensions[r].height = 36
    motor.dv_numerica(ws, ['D%d' % r for r in range(Z_INI, Z_FIN + 1)], minimo=0)
    nota_legal(ws, 'F%d' % (Z_INI + 1), 'CUN-23')

    motor.val(ws, 'B%d' % Z_TOT, 'TOTAL repartido', bold=True)
    formula(ws, 'D%d' % Z_TOT, '=SUM(D%d:D%d)' % (Z_INI, Z_FIN), fmt=DEC1, bold=True, destacar=True)
    formula(ws, 'E%d' % Z_TOT, '=SUM(E%d:E%d)' % (Z_INI, Z_FIN), fmt=PCT, bold=True)
    motor.val(ws, 'B%d' % Z['decl'], 'Superficie útil declarada en «Parámetros»')
    formula(ws, 'D%d' % Z['decl'], '=%s' % PB('m2_total'), fmt=DEC1)
    motor.val(ws, 'B%d' % Z['desc'], 'Descuadre (m²)')
    formula(ws, 'D%d' % Z['desc'], '=IFERROR(D%d-D%d,"")' % (Z_TOT, Z['decl']), fmt=DEC1)
    motor.regla_expresion(ws, 'D%d' % Z['desc'], '=AND(ISNUMBER($D$%d),$D$%d<>0)' % (Z['desc'], Z['desc']))
    motor.val(ws, 'F%d' % Z['desc'], 'Si no es cero, o te sobran metros sin asignar o has repartido '
                                    'más de los que tiene el local.', wrap=True)
    filas = [
        (Z['prod'], 'Metros de producción (obrador de masa y fritura)', 'Producción', DEC1),
        (Z['aten'], 'Metros de atención al cliente (barra, despacho y sala)', 'Atención al cliente', DEC1),
        (Z['serv'], 'Metros de servicios (aseos, vestuario y almacén)', 'Servicios', DEC1),
    ]
    for r, etq, bloque, fmt in filas:
        motor.val(ws, 'B%d' % r, etq)
        formula(ws, 'D%d' % r, '=SUMIF(C%d:C%d,"%s",D%d:D%d)' % (Z_INI, Z_FIN, bloque, Z_INI, Z_FIN),
                fmt=fmt)
    motor.val(ws, 'B%d' % Z['prod_pct'], 'Parte del local dedicada a producción')
    formula(ws, 'D%d' % Z['prod_pct'], '=IFERROR(D%d/D%d,"")' % (Z['prod'], Z_TOT), fmt=PCT)
    motor.val(ws, 'B%d' % Z['aten_pct'], 'Parte del local dedicada al cliente')
    formula(ws, 'D%d' % Z['aten_pct'], '=IFERROR(D%d/D%d,"")' % (Z['aten'], Z_TOT), fmt=PCT)
    motor.val(ws, 'B%d' % Z['terr'], 'Terraza, aparte (de «Parámetros»)')
    formula(ws, 'D%d' % Z['terr'], '=%s' % PB('m2_terraza'), fmt=DEC1)
    motor.val(ws, 'F%d' % Z['terr'], 'No suma a la superficie útil y va con autorización propia '
                                    'de ocupación de la vía pública.', wrap=True)
    CC.parrafo(ws, Z['terr'] + 2,
               'LA ZONA QUE DECIDE SI EL LOCAL SIRVE ES LA MÁS PEQUEÑA. Los seis metros de '
               'fritura bajo campana son los que piden conducto a cubierta, gas o potencia y '
               'el riesgo de incendio del Código Técnico. Antes de repartir el resto, '
               'comprueba en la «Ficha de Visita a Local» que esa zona tiene salida.',
               col_ini='B', col_fin='F', alto=46)
    bloque_contrato(ws, [(5, 'Superficie útil del local (m²)', '=%s' % PB('m2_total'), DEC1)])
    setup(ws, titulos='5:5')
    return ws


# ==========================================================================
# Hoja «Equipos y Capacidad»
# ==========================================================================
def hoja_equipos(wb):
    ws = wb.create_sheet(H_EQU)
    cabecera_hoja(ws, H_EQU, 'Todo en kilos de masa por hora: la línea con su churrero/a, la '
                             'freidora por tandas y la amasadora. Mide el tuyo; el del folleto no vale.')
    seccion(ws, 'A4', 'Personas')
    motor.val(ws, 'A%d' % E_PERS, 'Personas en la línea en el pico del fin de semana')
    ws.merge_cells('A%d:C%d' % (E_PERS, E_PERS))
    entrada(ws, 'D%d' % E_PERS, dp('personas_en_linea_pico'), fmt=ENT,
            etiqueta='Personas en la línea en el pico')
    motor.dv_numerica(ws, ['D%d' % E_PERS], minimo=0)
    gris(ws, 'F%d' % E_PERS, 'Supuesto de El Molinete: dos personas en la línea el sábado y el '
                             'domingo por la mañana. Viaja al libro 8, que comprueba el cuadrante.')
    ws.row_dimensions[E_PERS].height = 34
    bloque_contrato(ws, [(5, 'Personas en la línea en el pico', '=D%d' % E_PERS, ENT)])

    encabezados(ws, E_CAB, [('A', 'Nº', 5), ('B', 'Eslabón', 40), ('C', '¿Cuenta para el cuello?', 12),
                            ('D', 'kg de masa por ciclo', 12), ('E', 'Minutos por ciclo', 11),
                            ('F', 'kg de masa por hora', 12), ('G', 'Cuenta (kg/h)', 11),
                            ('H', 'Procedencia', 16), ('I', 'Nota', 70)])
    for i, (nombre, modo, kg, minutos, kgh, fuente, notatxt) in enumerate(EQUIPOS):
        r = E_INI + i
        motor.val(ws, 'A%d' % r, i + 1, fmt=ENT)
        motor.val(ws, 'B%d' % r, nombre, wrap=True)
        entrada(ws, 'C%d' % r, 'Sí', etiqueta='¿Cuenta? ' + nombre)
        if modo == 'directo':
            motor.val(ws, 'D%d' % r, 'No aplica')
            motor.val(ws, 'E%d' % r, 'No aplica')
            cel = entrada(ws, 'F%d' % r, kgh, fmt=DEC1, etiqueta='kg/h ' + nombre)
            motor.dv_numerica(ws, ['F%d' % r], minimo=0)
            nota_fuente(ws, cel.coordinate, fuente)
        else:
            c1 = entrada(ws, 'D%d' % r, kg, fmt=DEC1, etiqueta='kg por ciclo ' + nombre)
            entrada(ws, 'E%d' % r, minutos, fmt=DEC1, etiqueta='minutos por ciclo ' + nombre)
            motor.dv_numerica(ws, ['D%d' % r, 'E%d' % r], minimo=0)
            nota_fuente(ws, c1.coordinate, fuente)
            formula(ws, 'F%d' % r, '=IFERROR(D%d*%s/E%d,"")' % (r, PB('minutos_hora'), r), fmt=DEC1)
        formula(ws, 'G%d' % r, '=IF(C%d="Sí",F%d,"")' % (r, r), fmt=DEC1)
        motor.val(ws, 'H%d' % r, texto_fuente(fuente), wrap=True)
        ws['H%d' % r].font = Font(size=8, color=GRIS)
        motor.val(ws, 'I%d' % r, notatxt, wrap=True)
        ws.row_dimensions[r].height = 58
    motor.val(ws, 'B%d' % E_PORPERS, 'kg de masa por hora y persona en la línea')
    formula(ws, 'F%d' % E_PORPERS, '=IFERROR(F%d/D%d,"")' % (E_INI, E_PERS), fmt=DEC1)
    motor.val(ws, 'I%d' % E_PORPERS, 'Lo que rinde cada persona de la línea. Si la segunda persona '
                                    'no sube los kilos por hora, no está en la línea: está '
                                    'despachando.', wrap=True)
    ws.row_dimensions[E_PORPERS].height = 34
    refs, fila = listas(ws, E_PORPERS + 3, [('Sí o No', SI_NO)], col='B')
    CC.dv_rango(ws, ['C%d' % r for r in range(E_INI, E_FIN + 1)], refs['Sí o No'],
                '¿Cuenta para el cuello?', 'Elige «Sí» o «No» de la lista.')
    setup(ws, titulos='%d:%d' % (E_CAB, E_CAB))
    return ws


# ==========================================================================
# Hoja «Freidoras, Potencia y Riesgo»
# ==========================================================================
def hoja_freidoras(wb):
    ws = wb.create_sheet(H_FRE)
    cabecera_hoja(ws, H_FRE, 'Los kW que computa tu cocina según el Código Técnico, el riesgo '
                             'de incendio que te toca y a qué distancia van los filtros.')
    encabezados(ws, F_CAB, [('A', 'Nº', 5), ('B', 'Freidora', 40), ('C', '¿La tienes?', 10),
                            ('D', 'Litros de cuba', 10), ('E', 'Tipo de aparato', 11),
                            ('F', 'kW computables', 11), ('G', 'Distancia mínima del filtro', 12),
                            ('H', 'Procedencia', 14), ('I', 'Nota', 60)])
    for i, (nombre, tiene, litros, tipo, fuente, notatxt) in enumerate(FREIDORAS):
        r = F_INI + i
        motor.val(ws, 'A%d' % r, i + 1, fmt=ENT)
        motor.val(ws, 'B%d' % r, nombre, wrap=True)
        entrada(ws, 'C%d' % r, sino(tiene), etiqueta='¿La tienes? ' + nombre)
        c1 = entrada(ws, 'D%d' % r, litros, fmt=DEC1, etiqueta='litros ' + nombre)
        nota_fuente(ws, c1.coordinate, fuente)
        entrada(ws, 'E%d' % r, tipo, etiqueta='tipo ' + nombre)
        formula(ws, 'F%d' % r, '=IF(C%d="Sí",D%d*%s,"")' % (r, r, PB('kw_por_litro_freidora')), fmt=DEC1)
        formula(ws, 'G%d' % r, '=IF(C%d="Sí",IF(E%d="Gas",%s,IF(E%d="Parrilla",%s,%s)),"")'
                % (r, r, PB('distancia_filtro_gas_m'), r, PB('distancia_filtro_parrilla_m'),
                   PB('distancia_filtro_otro_m')), fmt=METROS)
        motor.val(ws, 'H%d' % r, texto_fuente(fuente), wrap=True)
        ws['H%d' % r].font = Font(size=8, color=GRIS)
        motor.val(ws, 'I%d' % r, notatxt, wrap=True)
        ws.row_dimensions[r].height = 52
    motor.dv_numerica(ws, ['D%d' % r for r in range(F_INI, F_FIN + 1)], minimo=0)
    nota_legal(ws, 'F%d' % F_INI, 'CUN-26', extra=NOTA_2_DBSI)

    # La etiqueta va en B (A es la columna estrecha del Nº).
    def etq(clave, texto):
        motor.val(ws, 'B%d' % F[clave], texto, wrap=True)

    r = F
    etq('litros', 'Litros totales de cuba (freidoras que tienes)')
    formula(ws, 'D%d' % r['litros'], '=SUMIF(C%d:C%d,"Sí",D%d:D%d)' % (F_INI, F_FIN, F_INI, F_FIN),
            fmt=DEC1)
    etq('kw_fre', 'kW computables de las freidoras')
    formula(ws, 'D%d' % r['kw_fre'], '=SUM(F%d:F%d)' % (F_INI, F_FIN), fmt=DEC1)
    etq('kw_otros', 'kW de los demás aparatos de cocción (míralo en su placa)')
    cel = entrada(ws, 'D%d' % r['kw_otros'], dp('kw_otros_aparatos'), fmt=DEC1,
                  etiqueta='kW de los demás aparatos de cocción')
    motor.dv_numerica(ws, [cel.coordinate], minimo=0)
    nota_legal(ws, cel.coordinate, 'CUN-26', extra=NOTA_2_DBSI)
    gris(ws, 'I%d' % r['kw_otros'],
         'Sólo computan los aparatos directamente destinados a preparar alimentos y '
         'susceptibles de provocar ignición (nota 2 de la tabla 2.1 del DB-SI, leída el '
         '03-10-2026). El Molinete cuenta sus dos chocolateras al baño maría: confirma con tu '
         'técnico si las tuyas computan; si no, pon 0.', alto=58)
    etq('kw', 'kW COMPUTABLES DE TU COCINA')
    formula(ws, 'D%d' % r['kw'], '=SUM(D%d:D%d)' % (r['kw_fre'], r['kw_otros']), fmt=DEC1,
            bold=True, destacar=True)
    etq('riesgo', 'Riesgo de la cocina')
    kw = 'D%d' % r['kw']
    formula(ws, 'D%d' % r['riesgo'],
            '=IF(NOT(ISNUMBER(%s)),"",IF(%s>%s,"Riesgo alto",IF(%s>%s,"Riesgo medio",IF(%s>%s,'
            '"Riesgo bajo","No es local de riesgo especial"))))'
            % (kw, kw, PB('riesgo_alto_desde_kw'), kw, PB('riesgo_medio_desde_kw'), kw,
               PB('riesgo_bajo_desde_kw')), bold=True, destacar=True)
    motor.semaforo_texto(ws, 'D%d' % r['riesgo'],
                         (('Riesgo alto', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('Riesgo medio', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          ('Riesgo bajo', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          ('No es local de riesgo especial', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    gris(ws, 'I%d' % r['riesgo'], 'De 20 a 30 kW, bajo; de 30 a 50, medio; por encima de 50, '
                                 'alto. Un local de riesgo especial pide conductos EI 30 y '
                                 'sectorización: es obra con proyecto y entra en el libro 2.')
    etq('ext_num', '¿Extinción automática obligatoria? (1 sí, 0 no)')
    formula(ws, 'D%d' % r['ext_num'], '=IF(ISNUMBER(%s),IF(%s>%s,1,0),"")'
            % (kw, kw, PB('riesgo_alto_desde_kw')), fmt=ENT)
    etq('ext_txt', '¿Extinción automática obligatoria?')
    formula(ws, 'D%d' % r['ext_txt'], '=IF(NOT(ISNUMBER(D%d)),"",IF(D%d=1,"Sí, obligatoria",'
            '"No obligatoria"))' % (r['ext_num'], r['ext_num']), bold=True)
    motor.semaforo_texto(ws, 'D%d' % r['ext_txt'],
                         (('Sí, obligatoria', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('No obligatoria', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    gris(ws, 'I%d' % r['ext_txt'], 'Por encima de 50 kW, el sistema automático de extinción es '
                                  'obligatorio (DB-SI, SI 4). Esta cifra viaja al libro 2, que '
                                  'presupuesta el sistema sólo si sale 1.')

    seccion(ws, 'B%d' % r['sec_nota2'], 'Si Proteges los Aparatos con Extinción Automática')
    etq('protege', '¿Proteges los aparatos con un sistema automático de extinción?')
    entrada(ws, 'D%d' % r['protege'], sino(dp('protege_con_extincion_automatica')),
            etiqueta='¿Proteges con extinción automática?')
    gris(ws, 'I%d' % r['protege'], 'El Molinete no la instala: con su potencia no la necesita. '
                                  'Ponerla aunque no sea obligatoria es la otra salida de la '
                                  'decisión 4, con su coste en el libro 2.')
    etq('uso', '¿El edificio es de uso hospitalario o residencial público?')
    entrada(ws, 'D%d' % r['uso'], sino(dp('uso_hospitalario_o_residencial')),
            etiqueta='¿Uso hospitalario o residencial público?')
    gris(ws, 'I%d' % r['uso'], 'Una churrería no lo es. Dentro de un hotel o un hospital, la nota '
                              '(2) no te libra y los umbrales son otros.')
    etq('veredicto', 'VEREDICTO DEL CÓDIGO TÉCNICO PARA TU COCINA')
    prot, uso = 'D%d' % r['protege'], 'D%d' % r['uso']
    formula(ws, 'D%d' % r['veredicto'],
            '=IF(NOT(ISNUMBER(%s)),"",IF(%s<=%s,"No es local de riesgo especial (no pasa del '
            'umbral bajo)",IF(AND(%s="Sí",%s="No"),"No es local de riesgo especial (nota 2 del '
            'CTE), aunque te sigue aplicando la nota (3)",IF(%s>%s,"Riesgo alto sin extinción '
            'automática: es obligatoria","Local de riesgo especial: "&LOWER(D%d)))))'
            % (kw, kw, PB('riesgo_bajo_desde_kw'), prot, uso, kw, PB('riesgo_alto_desde_kw'),
               r['riesgo']), bold=True, destacar=True)
    ws.merge_cells('D%d:H%d' % (r['veredicto'], r['veredicto']))
    ws.row_dimensions[r['veredicto']].height = 34
    nota_legal(ws, 'D%d' % r['veredicto'], 'CUN-26', extra=NOTA_2_DBSI)
    etq('nota3', '¿Te aplica la nota (3) (campana, conductos EI 30 y filtros)?')
    formula(ws, 'D%d' % r['nota3'], '=IF(NOT(ISNUMBER(%s)),"",IF(%s>%s,"Sí","No"))'
            % (kw, kw, PB('riesgo_bajo_desde_kw')), bold=True)
    gris(ws, 'I%d' % r['nota3'], 'La nota (3) alcanza a la cocina que es local de riesgo especial, '
                                'y la sigue alcanzando aunque la extinción automática la saque de '
                                'esa categoría.')
    etq('dist', 'Distancia mínima del filtro al foco de calor')
    formula(ws, 'D%d' % r['dist'], '=IFERROR(IF(COUNTIF(C%d:C%d,"Sí")=0,"",MAX(G%d:G%d)),"")'
            % (F_INI, F_FIN, F_INI, F_FIN), fmt=METROS, bold=True, destacar=True)
    gris(ws, 'I%d' % r['dist'], 'Más de 1,20 m si el aparato es de gas o de parrilla; más de 0,50 m '
                               'con los demás. Con varias freidoras manda la más exigente.')
    etq('obliga', 'Qué te obliga a pedir en la visita')
    formula(ws, 'D%d' % r['obliga'],
            '=IF(D%d="","",IF(D%d="Sí","Campana separada de materiales no A1, conductos EI 30 '
            'y filtros a la distancia de arriba","Campana y conducto según la ordenanza de tu '
            'municipio"))' % (r['nota3'], r['nota3']))
    ws.merge_cells('D%d:H%d' % (r['obliga'], r['obliga']))
    ws.row_dimensions[r['obliga']].height = 34

    bloque_contrato(ws, [
        (5, 'Litros totales de cuba', '=D%d' % r['litros'], DEC1),
        (6, '¿Necesitas extinción automática? (1 sí, 0 no)', '=D%d' % r['ext_num'], ENT),
    ])
    refs, _sig = listas(ws, F_LISTAS, [('Sí o No', SI_NO), ('Tipo de aparato', TIPOS_APARATO)],
                        col='B')
    CC.dv_rango(ws, ['C%d' % x for x in range(F_INI, F_FIN + 1)] + [prot, uso], refs['Sí o No'],
                'Sí o No', 'Elige «Sí» o «No» de la lista.')
    CC.dv_rango(ws, ['E%d' % x for x in range(F_INI, F_FIN + 1)], refs['Tipo de aparato'],
                'Tipo de aparato', 'Elige «Gas», «Parrilla» u «Otro» de la lista.')
    setup(ws, titulos='%d:%d' % (F_CAB, F_CAB))
    return ws


# ==========================================================================
# Hoja «Cuello de Botella»
# ==========================================================================
def hoja_cuello(wb):
    ws = wb.create_sheet(H_CUE)
    cabecera_hoja(ws, H_CUE, 'El eslabón que manda y las raciones por hora que aguanta el '
                             'conjunto. Cómo se reparte la demanda por franjas y si aguantas el '
                             'pico del domingo lo calcula el libro 5 con esta capacidad.')
    ws.column_dimensions['A'].width = 52
    ws.column_dimensions['B'].width = 30
    ws.column_dimensions['D'].width = 70
    rng_g = "%s$G$%d:$G$%d" % (Q(H_EQU), E_INI, E_FIN)
    rng_b = "%s$B$%d:$B$%d" % (Q(H_EQU), E_INI, E_FIN)
    seccion(ws, 'A5', 'Capacidad del Conjunto')
    filas = [
        ('cap_kg', 'Kilos de masa por hora que aguanta el conjunto', '=IFERROR(MIN(%s),"")' % rng_g, DEC1,
         'El eslabón más lento marca el ritmo de toda la línea.'),
        ('manda', 'El eslabón que manda', '=IFERROR(INDEX(%s,MATCH(B%d,%s,0)),"")' % (rng_b, K['cap_kg'], rng_g),
         None, 'Es el que hay que mejorar primero. Comprar otro equipo antes es dinero parado.'),
        ('seg_kg', 'Kilos por hora del segundo eslabón más justo', '=IFERROR(SMALL(%s,2),"")' % rng_g, DEC1,
         'Si está muy cerca del primero, resolver sólo el cuello te sube poco la capacidad.'),
        ('seg', 'Y es', '=IFERROR(INDEX(%s,MATCH(B%d,%s,0)),"")' % (rng_b, K['seg_kg'], rng_g), None, ''),
        ('kgrac', 'Kilos de masa por ración media (copiados del libro 3)', '=%s' % X1_CELDA, DEC4,
         'Viene de la celda verde de «Parámetros», con su fila de CUADRE.'),
        ('cap_rac', 'RACIONES POR HORA QUE AGUANTA EL CONJUNTO', '=IFERROR(B%d/B%d,"")' % (K['cap_kg'], K['kgrac']),
         DEC1, 'Es la cifra que viaja al libro 5, que la cruza con tus franjas y con la cola del domingo.'),
        ('por_pers', 'Raciones por hora y persona en la línea',
         '=IFERROR(B%d/%s,"")' % (K['cap_rac'], ABS_(H_EQU, 'D%d' % E_PERS)), DEC1, ''),
    ]
    for clave, etq, form, fmt, nt in filas:
        rr = K[clave]
        motor.val(ws, 'A%d' % rr, etq, wrap=True)
        destacar = clave in ('cap_rac', 'manda')
        formula(ws, 'B%d' % rr, form, fmt=fmt, bold=destacar, destacar=destacar)
        if nt:
            gris(ws, 'D%d' % rr, nt)
        ws.row_dimensions[rr].height = 30
    seccion(ws, 'A%d' % K['sec_h'], 'Horas de Línea que Te Pide el Día')
    filas_h = [
        ('h_tipo', 'Horas de línea a pleno ritmo en el día tipo', H_DIA, 'B'),
        ('h_punta', 'Horas de línea a pleno ritmo en el día punta', H_DIA, 'C'),
    ]
    for clave, etq, hoja, col in filas_h:
        rr = K[clave]
        motor.val(ws, 'A%d' % rr, etq, wrap=True)
        formula(ws, 'B%d' % rr, '=IFERROR(%s/B%d,"")' % (ABS_(hoja, '%s%d' % (col, DT['masa'])), K['cap_kg']),
                fmt=DEC1, bold=True)
        ws.row_dimensions[rr].height = 30
    gris(ws, 'D%d' % K['h_tipo'], 'Son horas de fritura si la línea no parase nunca. La demanda no '
                                  'llega repartida: la mitad del día se concentra en el desayuno.', alto=40)
    motor.val(ws, 'A%d' % K['sobra_punta'], '¿Una churrera o dos?', bold=True)
    formula(ws, 'B%d' % K['sobra_punta'],
            '=IF(B%d="","","El veredicto está en el libro 5, hoja «Capacidad contra el Pico», '
            'celda E23: allí esta capacidad se cruza con tus franjas")' % K['cap_rac'])
    gris(ws, 'D%d' % K['sobra_punta'], 'La respuesta no está en el total del día sino en la hora '
                                       'punta del domingo, y esa hora sólo existe en el libro 5. '
                                       'Aquí ves el eslabón que manda y cuánto sube la capacidad '
                                       'si lo mejoras; allí, con esa capacidad copiada, sale el '
                                       'veredicto «una, con refuerzo, o dos». Si dice que hace falta '
                                       'más línea, activa la segunda freidora aquí y vuelve a copiar '
                                       'la capacidad.',
         alto=64)
    bloque_contrato(ws, [(5, 'Capacidad del conjunto (raciones por hora)', '=B%d' % K['cap_rac'], DEC1)])
    setup(ws)
    return ws


# ==========================================================================
# Hoja «Día Tipo y Día Punta»
# ==========================================================================
def hoja_dia(wb):
    ws = wb.create_sheet(H_DIA)
    cabecera_hoja(ws, H_DIA, 'La ÚNICA fuente de la demanda base del paquete: las raciones de un '
                             'día de diario y de un sábado, domingo o festivo. El reparto por mes '
                             'y por franja lo hace el libro 5.')
    encabezados(ws, DT['cab'], [('A', 'Concepto', 46), ('B', 'Día tipo (lunes a viernes)', 16),
                                ('C', 'Día punta (sábado, domingo y festivo)', 16),
                                ('D', 'Nota', 70)])
    motor.val(ws, 'A%d' % DT['rac'], 'Raciones al día', bold=True)
    b = entrada(ws, 'B%d' % DT['rac'], dp('raciones_dia_tipo'), fmt=ENT, etiqueta='Raciones del día tipo')
    c = entrada(ws, 'C%d' % DT['rac'], dp('raciones_dia_punta'), fmt=ENT, etiqueta='Raciones del día punta')
    motor.dv_numerica(ws, [b.coordinate, c.coordinate], minimo=0)
    nota_fuente(ws, b.coordinate, 'CUS-27', extra='supuesto declarado de El Molinete, apoyado en '
                                                  'lo que declara La Artesana entre semana')
    nota_fuente(ws, c.coordinate, 'CUS-27', extra='supuesto declarado de El Molinete, apoyado en '
                                                  'lo que declara La Artesana el fin de semana')
    gris(ws, 'D%d' % DT['rac'], 'Supuesto de El Molinete, no un dato del sector. Pon las tuyas: al '
                               'principio, una estimación; a los tres meses, las del TPV.', alto=34)
    filas = [
        ('kgrac', 'Kilos de masa por ración media (de «Parámetros»)', '=%s' % X1_CELDA, DEC4,
         'Copiados del libro 3, merma incluida.'),
        ('masa', 'Kilos de masa al día', '=IFERROR({c}%d*{c}%d,"")' % (DT['rac'], DT['kgrac']), DEC1,
         'Lo que hay que amasar, dosificar y freír.'),
        ('fpk', 'Kilos fritos por kilo de masa (de «Parámetros»)', '=%s' % PB('kg_fritos_por_kg_masa'), DEC, ''),
        ('fritos', 'KILOS FRITOS AL DÍA', '=IFERROR({c}%d*{c}%d,"")' % (DT['masa'], DT['fpk']), DEC1,
         'Es lo que viaja al libro 4 para calcular el aceite que se lleva el producto.'),
        ('tandas', 'Tandas de freidora al día',
         '=IFERROR(ROUNDUP({c}%d/%s,0),"")' % (DT['masa'], ABS_(H_EQU, 'D%d' % FILA_FREIDORA)), ENT, ''),
        ('amasados', 'Amasados al día',
         '=IFERROR(ROUNDUP({c}%d/%s,0),"")' % (DT['masa'], ABS_(H_EQU, 'D%d' % FILA_AMASADORA)), ENT,
         'Con una amasadora grande, uno o dos al día; el resto del tiempo está parada.'),
        ('horas', 'Horas de línea a pleno ritmo',
         '=IFERROR({c}%d/%s,"")' % (DT['masa'], ABS_(H_CUE, 'B%d' % K['cap_kg'])), DEC1,
         'Con el eslabón que manda en la hoja «Cuello de Botella».'),
    ]
    for clave, etq, form, fmt, nt in filas:
        rr = DT[clave]
        motor.val(ws, 'A%d' % rr, etq, bold=clave == 'fritos')
        for col in ('B', 'C'):
            formula(ws, '%s%d' % (col, rr), form.replace('{c}', col), fmt=fmt,
                    bold=clave == 'fritos', destacar=clave == 'fritos')
        if nt:
            gris(ws, 'D%d' % rr, nt)
    seccion(ws, 'A%d' % DT['sec_sem'], 'La Semana Tipo')
    motor.val(ws, 'A%d' % DT['rac_sem'], 'Raciones de la semana tipo')
    formula(ws, 'B%d' % DT['rac_sem'], '=IFERROR(B%d*%s+C%d*%s,"")'
            % (DT['rac'], PB('dias_tipo_semana'), DT['rac'], PB('dias_punta_semana')), fmt=ENT)
    motor.val(ws, 'A%d' % DT['masa_sem'], 'Kilos de masa de la semana tipo')
    formula(ws, 'B%d' % DT['masa_sem'], '=IFERROR(B%d*%s+C%d*%s,"")'
            % (DT['masa'], PB('dias_tipo_semana'), DT['masa'], PB('dias_punta_semana')), fmt=DEC1)
    motor.val(ws, 'A%d' % DT['rac_media'], 'Raciones de un día medio de la semana')
    formula(ws, 'B%d' % DT['rac_media'], '=IFERROR(B%d/(%s+%s),"")'
            % (DT['rac_sem'], PB('dias_tipo_semana'), PB('dias_punta_semana')), fmt=DEC1)
    gris(ws, 'D%d' % DT['rac_sem'], 'Sin estacionalidad: las raciones del año, mes a mes, las '
                                   'reparte el libro 5 con sus doce coeficientes.')
    bloque_contrato(ws, [
        (5, 'kg fritos en un día tipo', '=B%d' % DT['fritos'], DEC1),
        (6, 'kg fritos en un día punta', '=C%d' % DT['fritos'], DEC1),
        (7, 'Raciones del día tipo', '=B%d' % DT['rac'], ENT),
        (8, 'Raciones del día punta', '=C%d' % DT['rac'], ENT),
    ])
    setup(ws, titulos='%d:%d' % (DT['cab'], DT['cab']))
    return ws


# ==========================================================================
# Hoja «Ficha de Visita a Local»
# ==========================================================================
L_RES = {}


def hoja_ficha(wb):
    global ITEMS, L_FIN
    ITEMS = _items_ficha()
    L_FIN = L_INI + len(ITEMS) - 1
    ws = wb.create_sheet(H_FIC)
    cabecera_hoja(ws, H_FIC, 'Imprímela y llévala a cada visita. Los cuatro eliminatorios van '
                             'primero y en este orden. Una respuesta que descarta en un '
                             'eliminatorio y el veredicto es DESCARTAR.')
    encabezados(ws, L_CAB, [('A', 'Nº', 5), ('B', 'Qué se comprueba', 40), ('C', '¿Eliminatorio?', 11),
                            ('D', 'Cómo se comprueba', 40), ('E', 'Respuesta', 13),
                            ('F', 'Respuesta que descarta', 12), ('G', 'Respuesta que obliga a obra con licencia', 13),
                            ('H', 'Dato de tu proyecto', 18), ('I', 'Veredicto', 18),
                            ('J', 'Nota y norma', 70)], alto=58)
    for i, (item, elim, como, resp, desc, obl, dato, notatxt, pid) in enumerate(ITEMS):
        r = L_INI + i
        motor.val(ws, 'A%d' % r, i + 1, fmt=ENT)
        motor.val(ws, 'B%d' % r, item, wrap=True)
        motor.val(ws, 'C%d' % r, elim)
        motor.val(ws, 'D%d' % r, como, wrap=True)
        entrada(ws, 'E%d' % r, resp, etiqueta='Respuesta: ' + item)
        motor.val(ws, 'F%d' % r, desc)
        motor.val(ws, 'G%d' % r, obl)
        if dato:
            formula(ws, 'H%d' % r, dato[0], fmt=dato[1])
        formula(ws, 'I%d' % r,
                '=IF(E%d="","",IF(E%d="Por comprobar",IF(C%d="Sí","Pendiente","Por comprobar"),'
                'IF(E%d=F%d,IF(C%d="Sí","DESCARTAR","Punto débil"),IF(E%d=G%d,"Con obra y licencia",'
                '"OK"))))' % (r, r, r, r, r, r, r, r), bold=True)
        motor.val(ws, 'J%d' % r, notatxt, wrap=True)
        if pid:
            ids = [x.strip() for x in pid.split('+')]
            nota_legal(ws, 'J%d' % r, ids[0])
            for x in ids[1:]:
                nota_legal(ws, 'D%d' % r, x)
        ws.row_dimensions[r].height = 64
    # Segundo eliminatorio: además de la ordenanza que obliga al conducto (CUN-23, en J),
    # la excepción de 4 kW que no ampara una freidora (CUN-24) va en la D.
    motor.semaforo_texto(ws, 'I%d:I%d' % (L_INI, L_FIN),
                         (('DESCARTAR', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('Punto débil', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          ('Con obra y licencia', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          ('Por comprobar', motor.CF_GRIS_BG, motor.CF_GRIS_FG),
                          ('Pendiente', motor.CF_GRIS_BG, motor.CF_GRIS_FG),
                          ('OK', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    f = L_FIN + 2
    res = [
        ('desc', 'Motivos de descarte', '=COUNTIF(I%d:I%d,"DESCARTAR")' % (L_INI, L_FIN)),
        ('pend', 'Eliminatorios sin comprobar', '=COUNTIF(I%d:I%d,"Pendiente")' % (L_INI, L_FIN)),
        ('obra', 'Obligan a obra con proyecto y licencia', '=COUNTIF(I%d:I%d,"Con obra y licencia")'
         % (L_INI, L_FIN)),
        ('debil', 'Puntos débiles y cosas por comprobar', '=COUNTIF(I%d:I%d,"Punto débil")+COUNTIF(I%d:I%d,'
         '"Por comprobar")' % (L_INI, L_FIN, L_INI, L_FIN)),
        ('ok', 'Resueltos sin problema', '=COUNTIF(I%d:I%d,"OK")' % (L_INI, L_FIN)),
    ]
    for k, (clave, etq, form) in enumerate(res):
        L_RES[clave] = f + k
        motor.val(ws, 'B%d' % (f + k), etq)
        formula(ws, 'E%d' % (f + k), form, fmt=ENT)
    L_RES['primero'] = f + len(res)
    motor.val(ws, 'B%d' % L_RES['primero'], 'El primer eliminatorio que tumba el local')
    formula(ws, 'E%d' % L_RES['primero'],
            '=IFERROR(INDEX(B%d:B%d,MATCH("DESCARTAR",I%d:I%d,0)),"Ninguno")' % (L_INI, L_FIN, L_INI, L_FIN))
    ws.merge_cells('E%d:J%d' % (L_RES['primero'], L_RES['primero']))
    L_RES['ver'] = f + len(res) + 1
    motor.val(ws, 'B%d' % L_RES['ver'], 'VEREDICTO DEL LOCAL', bold=True)
    formula(ws, 'E%d' % L_RES['ver'],
            '=IF(E%d>0,"DESCARTAR ESTE LOCAL",IF(E%d>0,"NO DECIDAS TODAVÍA",IF(E%d+E%d>0,'
            '"SIGUE ADELANTE CON RESERVAS","SIGUE ADELANTE")))'
            % (L_RES['desc'], L_RES['pend'], L_RES['obra'], L_RES['debil']), bold=True, destacar=True)
    ws.merge_cells('E%d:H%d' % (L_RES['ver'], L_RES['ver']))
    motor.semaforo_texto(ws, 'E%d' % L_RES['ver'],
                         (('DESCARTAR ESTE LOCAL', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('NO DECIDAS TODAVÍA', motor.CF_GRIS_BG, motor.CF_GRIS_FG),
                          ('SIGUE ADELANTE CON RESERVAS', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          ('SIGUE ADELANTE', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    fila = L_RES['ver'] + 2
    refs, fila = listas(ws, fila, [('Respuesta', RESPUESTAS)], col='B')
    CC.dv_rango(ws, ['E%d' % r for r in range(L_INI, L_FIN + 1)], refs['Respuesta'], 'Respuesta',
                'Elige «Sí», «No» o «Por comprobar» de la lista.')
    CC.parrafo(ws, fila,
               'POR QUÉ ESTE ORDEN. Primero, si la extracción necesita proyecto: la actividad '
               'puede ir por declaración responsable, pero la obra del conducto no, y eso cambia '
               'plazos y dinero. Después, si el conducto puede llegar a cubierta: si no puede, '
               'no hay freidora. Luego el gas o la potencia para una freidora eléctrica (la '
               'bombona pequeña no vale para un local fijo). Y al final, si la cocina puede ser '
               'local de riesgo especial con los kW que vas a instalar. Lo que no es eliminatorio '
               'encarece la obra: llévalo al libro 2 como partida.',
               col_ini='B', col_fin='J', alto=72)
    setup(ws, titulos='%d:%d' % (L_CAB, L_CAB))
    return ws


# ==========================================================================
# Mapa de celdas citables
# ==========================================================================
def mapa_celdas():
    m = [
        # --- las 8 celdas del contrato (origen de X3, X3 bis, X4, X6 y X9)
        ('kg fritos en un día tipo', H_DIA, 'L5', 'salida'),
        ('kg fritos en un día punta', H_DIA, 'L6', 'salida'),
        ('Raciones del día tipo', H_DIA, 'L7', 'salida'),
        ('Raciones del día punta', H_DIA, 'L8', 'salida'),
        ('Litros totales de cuba', H_FRE, 'L5', 'salida'),
        ('¿Necesitas extinción automática? (1 sí, 0 no)', H_FRE, 'L6', 'salida'),
        ('Capacidad del conjunto en raciones por hora', H_CUE, 'L5', 'salida'),
        ('Personas en la línea en el pico', H_EQU, 'L5', 'salida'),
        ('Superficie útil del local (celda de origen del cruce al libro 2)', H_ZON, 'L5', 'salida'),
        # --- cruce recibido
        ('kg de masa por ración media copiados del libro 3 (X1)', H_PAR, 'B%d' % P_X1, 'entrada'),
        ('Cuadre de los kg de masa por ración con el libro 3', H_PAR, 'B%d' % P_X1_CUAD, 'salida'),
        ('Kilos fritos por kilo de masa copiados del libro 3 (X1 bis)', H_PAR, 'B%d' % P_X1B, 'entrada'),
        ('Cuadre de los kilos fritos por kilo de masa con el libro 3', H_PAR, 'B%d' % P_X1B_CUAD, 'salida'),
        # --- parámetros
        ('Superficie útil del local', H_PAR, 'B%d' % P['m2_total'], 'parametro'),
        ('Terraza aparte', H_PAR, 'B%d' % P['m2_terraza'], 'parametro'),
        ('kW por litro de freidora (CTE)', H_PAR, 'B%d' % P['kw_por_litro_freidora'], 'parametro'),
        ('Umbral de riesgo especial bajo', H_PAR, 'B%d' % P['riesgo_bajo_desde_kw'], 'parametro'),
        ('Umbral de riesgo especial medio', H_PAR, 'B%d' % P['riesgo_medio_desde_kw'], 'parametro'),
        ('Umbral de riesgo alto y extinción automática', H_PAR, 'B%d' % P['riesgo_alto_desde_kw'], 'parametro'),
        ('Distancia mínima del filtro con gas', H_PAR, 'B%d' % P['distancia_filtro_gas_m'], 'parametro'),
        ('Distancia mínima del filtro con otros aparatos', H_PAR, 'B%d' % P['distancia_filtro_otro_m'], 'parametro'),
        # --- zonas
        ('m² repartidos por zonas', H_ZON, 'D%d' % Z_TOT, 'salida'),
        ('m² de producción', H_ZON, 'D%d' % Z['prod'], 'salida'),
        ('Parte del local dedicada a producción', H_ZON, 'D%d' % Z['prod_pct'], 'salida'),
        ('m² de atención al cliente', H_ZON, 'D%d' % Z['aten'], 'salida'),
        ('m² de la zona de fritura bajo campana', H_ZON, 'D%d' % (Z_INI + 1), 'entrada'),
        # --- equipos
        ('kg de masa por hora de la línea', H_EQU, 'F%d' % E_INI, 'entrada'),
        ('kg de masa por hora de la freidora', H_EQU, 'F%d' % FILA_FREIDORA, 'salida'),
        ('kg de masa por hora de la amasadora', H_EQU, 'F%d' % FILA_AMASADORA, 'salida'),
        ('kg de masa por hora y persona en la línea', H_EQU, 'F%d' % E_PORPERS, 'salida'),
        # --- freidoras
        ('Litros de la freidora del ejemplo', H_FRE, 'D%d' % F_INI, 'entrada'),
        ('kW de los demás aparatos de cocción', H_FRE, 'D%d' % F['kw_otros'], 'entrada'),
        ('kW computables de la cocina', H_FRE, 'D%d' % F['kw'], 'salida'),
        ('Riesgo de la cocina', H_FRE, 'D%d' % F['riesgo'], 'salida'),
        ('¿Extinción automática obligatoria?', H_FRE, 'D%d' % F['ext_txt'], 'salida'),
        ('Veredicto del Código Técnico para la cocina', H_FRE, 'D%d' % F['veredicto'], 'salida'),
        ('¿Aplica la nota (3) del CTE?', H_FRE, 'D%d' % F['nota3'], 'salida'),
        ('Distancia mínima del filtro al foco', H_FRE, 'D%d' % F['dist'], 'salida'),
        # --- cuello
        ('Kilos de masa por hora del conjunto', H_CUE, 'B%d' % K['cap_kg'], 'salida'),
        ('Eslabón que manda', H_CUE, 'B%d' % K['manda'], 'salida'),
        ('Segundo eslabón más justo', H_CUE, 'B%d' % K['seg'], 'salida'),
        ('Horas de línea a pleno ritmo en el día tipo', H_CUE, 'B%d' % K['h_tipo'], 'salida'),
        ('Horas de línea a pleno ritmo en el día punta', H_CUE, 'B%d' % K['h_punta'], 'salida'),
        # --- día tipo y punta
        ('kg de masa en un día tipo', H_DIA, 'B%d' % DT['masa'], 'salida'),
        ('kg de masa en un día punta', H_DIA, 'C%d' % DT['masa'], 'salida'),
        ('Tandas de freidora en un día punta', H_DIA, 'C%d' % DT['tandas'], 'salida'),
        ('Amasados en un día punta', H_DIA, 'C%d' % DT['amasados'], 'salida'),
        ('Raciones de la semana tipo', H_DIA, 'B%d' % DT['rac_sem'], 'salida'),
        ('Raciones de un día medio de la semana', H_DIA, 'B%d' % DT['rac_media'], 'salida'),
        # --- ficha
        ('Veredicto de la ficha de visita', H_FIC, 'E%d' % L_RES['ver'], 'salida'),
        ('Primer eliminatorio que tumba el local', H_FIC, 'E%d' % L_RES['primero'], 'salida'),
        ('Ítems que obligan a obra con proyecto y licencia', H_FIC, 'E%d' % L_RES['obra'], 'salida'),
    ]
    for i, it in enumerate(ITEMS[:4]):
        m.append(('Ficha, eliminatorio %d: %s' % (i + 1, it[0]), H_FIC, 'I%d' % (L_INI + i), 'salida'))
    return m


# ==========================================================================
# Cierre
# ==========================================================================
_PROHIBIDAS = ('INDIRECT', 'COUNTA', 'PMT(', 'OFFSET', 'XLOOKUP', 'LET(', 'LAMBDA', 'RANK(',
               'NETWORKDAYS', 'IRR(')
RX_CONST_DEC = re.compile(r'[*/]\s*\d{1,3}[.,]\d{1,4}(?!\d)')
RX_CONST_ENT = re.compile(r'[*/+\-<>=]\s*(\d+)(?![\d.,]*["!])')


def _textos(wbf):
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                if isinstance(c.value, str):
                    yield ws.title, c.coordinate, c.value
                if c.comment is not None:
                    yield ws.title, c.coordinate + ' (nota)', c.comment.text


def _gate_lista_negra(wbf):
    fallos = []
    rotulos_ok = set((h, c) for h, c, _r, _x in RECEPTORAS)
    rotulos_ok = set((h, 'A' + c[1:]) for h, c in rotulos_ok)
    for hoja, coord, texto in _textos(wbf):
        donde = '%s!%s' % (hoja, coord)
        bajo = texto.lower()
        for aguja, motivo in D.LISTA_NEGRA:
            if aguja.startswith('re:'):
                if re.search(aguja[3:], bajo):
                    fallos.append('%s: /%s/ (%s)' % (donde, aguja[3:], motivo))
            elif aguja.lower() in bajo:
                fallos.append('%s: «%s» (%s)' % (donde, aguja, motivo))
        for pid in RX_ID.findall(texto):
            if pid in D.IDS_PROHIBIDOS:
                fallos.append('%s: id prohibido %s' % (donde, pid))
        for frase in ('cópialo del libro', 'trae aquí la cifra de'):
            if frase in bajo and (hoja, coord) not in rotulos_ok:
                fallos.append('%s: «%s» fuera de las celdas declaradas en CRUCES' % (donde, frase))
        if '0,50 m' in texto and '1,20 m' not in texto:
            fallos.append('%s: filtros a 0,50 m sin los 1,20 m de gas o parrilla (A5)' % donde)
        if re.search(r'\bpor declaración responsable\b', bajo) and 'obra' not in bajo:
            fallos.append('%s: declaración responsable sin la condición de obra (A4)' % donde)
    if fallos:
        raise SystemExit('LISTA NEGRA en %s:\n  %s' % (NOMBRE, '\n  '.join(fallos[:40])))


def _gate_contrato(wbv):
    if D._ERROR_CRUCES:
        raise SystemExit('datos_ejemplo no pudo calcular los cruces: %s' % D._ERROR_CRUCES)
    fallos, filas = [], []
    for c in D.CRUCES:
        if c['origen'] != LIBRO:
            continue
        hoja, celda = c['hoja_origen'], c['celda_origen']
        if not re.match(r'^L\d+$', celda) or int(celda[1:]) < 5:
            fallos.append('%s: la celda de origen %s no está en la L desde la fila 5' % (c['x'], celda))
            continue
        rot = wbv[hoja]['K' + celda[1:]].value
        if not isinstance(rot, str) or not rot.strip():
            fallos.append('%s: %s!K%s sin rótulo' % (c['x'], hoja, celda[1:]))
        v = wbv[hoja][celda].value
        e = c['valor_defecto']
        if not isinstance(v, (int, float)) or abs(v - e) > max(1e-9, abs(e) * 1e-9):
            fallos.append('%s: %s!%s = %r y datos_ejemplo dice %r (%s)' % (c['x'], hoja, celda, v, e,
                                                                        c['concepto']))
        filas.append((c['x'], hoja, celda, v, e))
    if fallos:
        raise SystemExit('CONTRATO DE CRUCES ROTO en %s:\n  %s' % (NOMBRE, '\n  '.join(fallos)))
    return filas


def _gate_receptor(wbf, wbv):
    """Cada cruce con receptor = 1: celda verde con el rótulo literal, el valor por defecto
    de `CRUCES` y una fila de CUADRE en la misma hoja. Nada más con «cópialo del libro»."""
    esperados = [c for c in D.CRUCES if c['receptor'] == LIBRO]
    if len(RECEPTORAS) != len(esperados) or len(CUADRES) != len(esperados):
        raise SystemExit('Receptoras %d, CUADRES %d y CRUCES con receptor 1: %d'
                         % (len(RECEPTORAS), len(CUADRES), len(esperados)))
    n_rot = 0
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and 'cópialo del libro' in c.value.lower():
                    n_rot += 1
    if n_rot != len(esperados):
        raise SystemExit('Rótulos «cópialo del libro» en el libro: %d; CRUCES declara %d' % (n_rot, len(esperados)))
    for (hoja, coord, rot, c), (hc, cc) in zip(RECEPTORAS, CUADRES):
        cel = wbf[hoja][coord]
        if not motor.es_verde(cel) or cel.protection.locked:
            raise SystemExit('%s!%s (cruce %s) no es verde editable' % (hoja, coord, c['x']))
        if wbf[hoja]['A' + coord[1:]].value != D.rotulo_cruce(c):
            raise SystemExit('%s!A%s no lleva el rótulo literal de CRUCES' % (hoja, coord[1:]))
        if abs(wbv[hoja][coord].value - c['valor_defecto']) > 1e-12:
            raise SystemExit('%s!%s no nace con el valor_defecto de CRUCES' % (hoja, coord))
        if hc != hoja or not str(wbf[hoja]['A' + cc[1:]].value).startswith('CUADRE'):
            raise SystemExit('El cruce %s no tiene su fila de CUADRE en %s' % (c['x'], hoja))
        if wbv[hc][cc].value != 'CUADRA':
            raise SystemExit('La fila de CUADRE %s!%s no cuadra con los valores por defecto' % (hc, cc))


def cerrar(wb):
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.lastModifiedBy = 'AI Chef Pro'
    wb.properties.title = TITULO
    wb.properties.subject = SUBJECT
    enmiendas_churreria.sanear_libro(wb)       # R-09: sin texto interno de la fábrica
    CC.barrer_cp1252(wb)
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and (motor.NARROW in c.value or motor.NOBRK in c.value):
                    raise SystemExit('%s!%s lleva espacio fino o guion no separable' % (ws.title, c.coordinate))
                if c.comment is not None:
                    try:
                        c.comment.text.encode('cp1252')
                    except UnicodeEncodeError:
                        raise SystemExit('%s!%s: la nota no cabe en WinAnsi' % (ws.title, c.coordinate))
    for ws in wb.worksheets:
        motor.retirar_verde_de_calculadas(ws)
        motor.proteger(ws)
    if wb.sheetnames[0] != H_INS:
        raise SystemExit('La primera hoja no es «Instrucciones»')
    if tuple(wb.sheetnames) != tuple(D.HOJAS[LIBRO]):
        raise SystemExit('Hojas %r frente a las de datos_ejemplo %r' % (wb.sheetnames, D.HOJAS[LIBRO]))

    destino = CC.BUILD_DIR
    if not os.path.isdir(destino):
        os.makedirs(destino)
    ruta = os.path.join(destino, FICHERO)
    wb.save(ruta)

    otros = [os.path.splitext(f)[0] for n, f in D.LIBROS.items() if n != LIBRO]
    problemas = []
    for hoja, coord, form in motor.REGISTRO:
        arriba = form.upper()
        for p in _PROHIBIDAS:
            if p in arriba:
                problemas.append('%s!%s usa %s' % (hoja, coord, p))
        bajo = form.lower()
        if '.xlsx' in bajo or '[' in form or any(o in bajo for o in otros):
            problemas.append('%s!%s parece referencia a otro libro: %s' % (hoja, coord, form[:70]))
        sin_texto = re.sub(r'"[^"]*"', '', form)
        sin_ref = re.sub(r"'[^']*'!", '', sin_texto)
        sin_ref = re.sub(r'\$?[A-Z]{1,2}\$?\d+', '', sin_ref)
        for m in RX_CONST_DEC.finditer(sin_ref):
            problemas.append('%s!%s constante tecleada %s' % (hoja, coord, m.group(0)))
        for m in RX_CONST_ENT.finditer(sin_ref):
            if m.group(1) not in ('0', '1', '2'):
                problemas.append('%s!%s constante entera %s en %s' % (hoja, coord, m.group(1), form[:80]))
        if '/' in sin_texto and 'IFERROR' not in arriba:
            problemas.append('%s!%s división sin IFERROR: %s' % (hoja, coord, form[:70]))
    if problemas:
        raise SystemExit('FÓRMULAS con problemas en %s:\n  %s' % (NOMBRE, '\n  '.join(problemas[:40])))

    res = subprocess.run([sys.executable, os.path.join(RAIZ, 'inject_cache.py'), ruta],
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    salida_cache = res.stdout.decode('utf-8', 'replace')
    if res.returncode != 0:
        raise SystemExit('inject_cache falló:\n' + salida_cache)

    wbf = openpyxl.load_workbook(ruta)
    wbv = openpyxl.load_workbook(ruta, data_only=True)
    sin_valor, con_error, sin_dato, pendientes = [], [], [], []
    for hoja, coord, form in motor.REGISTRO:
        v = wbv[hoja][coord].value
        if v is None:
            pendientes.append((hoja, coord, form))
        elif isinstance(v, str) and v.startswith('#'):
            con_error.append('%s!%s  %s -> %s' % (hoja, coord, form[:60], v))
    if pendientes:
        from pycel import ExcelCompiler
        xl = ExcelCompiler(ruta)
        for hoja, coord, form in pendientes:
            try:
                r = xl.evaluate("'%s'!%s" % (hoja, coord))
            except Exception as e:                            # noqa: BLE001
                sin_valor.append('%s!%s  %s -> pycel: %s' % (hoja, coord, form[:60], e))
                continue
            if r == '' or (r is None and '""' in form):
                sin_dato.append('%s!%s' % (hoja, coord))
            else:
                sin_valor.append('%s!%s  %s -> %r' % (hoja, coord, form[:60], r))
    if sin_valor or con_error:
        raise SystemExit('VERIFICACIÓN data_only FALLIDA en %s\n  sin valor (%d):\n   %s\n  con error '
                         '(%d):\n   %s' % (NOMBRE, len(sin_valor), '\n   '.join(sin_valor[:40]),
                                           len(con_error), '\n   '.join(con_error[:40])))
    incoherentes = CC.gate_sum_rango(wbv)
    if incoherentes:
        raise SystemExit('TOTALES con caché incoherente:\n  ' + '\n  '.join(incoherentes))

    verdes_vacias, n_verdes = [], 0
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                if motor.es_verde(c):
                    n_verdes += 1
                    if c.protection.locked:
                        verdes_vacias.append('%s!%s bloqueada' % (ws.title, c.coordinate))
                    if c.value is None or (isinstance(c.value, str) and not c.value.strip()):
                        verdes_vacias.append('%s!%s' % (ws.title, c.coordinate))
    if verdes_vacias:
        raise SystemExit('CELDAS VERDES VACÍAS O BLOQUEADAS:\n  ' + ', '.join(verdes_vacias))

    _gate_lista_negra(wbf)
    contrato = _gate_contrato(wbv)
    _gate_receptor(wbf, wbv)

    requeridos = [i for i, (_t, libros) in D.IDS_LEGALES_REQUERIDOS.items() if LIBRO in libros]
    puestos = set(pid for _h, _c, pid in NOTAS_LEGALES)
    faltan = [i for i in requeridos if i not in puestos]
    if faltan:
        raise SystemExit('Faltan notas legales del libro 1: %s' % ', '.join(faltan))

    # Comprobaciones del caso contra datos_ejemplo (no sólo el contrato).
    vfre = wbv[H_FRE]
    chequeos = [
        ('kW computables', vfre['D%d' % F['kw']].value, D.kw_computables()),
        ('distancia del filtro', vfre['D%d' % F['dist']].value, D.distancia_filtro_m()),
        ('eslabón que manda', wbv[H_CUE]['B%d' % K['manda']].value, None),
    ]
    for etq, v, e in chequeos[:2]:
        if not isinstance(v, (int, float)) or abs(v - e) > 1e-9:
            raise SystemExit('%s: el libro da %r y datos_ejemplo %r' % (etq, v, e))
    eq = D.equipo_que_manda()
    if not str(chequeos[2][1]).lower().startswith(eq.lower()):
        raise SystemExit('Eslabón que manda: el libro da %r y datos_ejemplo %r' % (chequeos[2][1], eq))
    riesgo = vfre['D%d' % F['riesgo']].value
    if riesgo.lower() != ('riesgo ' + D.riesgo_cocina()).lower():
        raise SystemExit('Riesgo: el libro da %r y datos_ejemplo %r' % (riesgo, D.riesgo_cocina()))

    mapa = {}
    for etiqueta, hoja, coord, tipo in mapa_celdas():
        if tipo not in ('entrada', 'salida', 'parametro'):
            raise SystemExit('Tipo de mapa no válido: %r' % tipo)
        v = wbv[hoja][coord].value
        if v is None:
            raise SystemExit('El mapa cita %s!%s («%s») y está VACÍA' % (hoja, coord, etiqueta))
        if etiqueta in mapa:
            raise SystemExit('Etiqueta de mapa repetida: %r' % etiqueta)
        mapa[etiqueta] = {'ref': '%s!%s!%s' % (FICHERO, hoja, coord), 'valor': v, 'tipo': tipo}
    for x, hoja, celda, _v, _e in contrato:
        if not any(d['ref'] == '%s!%s!%s' % (FICHERO, hoja, celda) for d in mapa.values()):
            raise SystemExit('El mapa no cita la celda de origen %s!%s (%s)' % (hoja, celda, x))
    with open(os.path.join(destino, 'mapa-' + NOMBRE + '.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(mapa, ensure_ascii=False, indent=1))

    return {'ruta': ruta, 'hojas': len(wbf.worksheets), 'formulas': len(motor.REGISTRO),
            'sin_dato': len(sin_dato), 'verdes': n_verdes, 'verdes_vacias': verdes_vacias,
            'notas_legales': len(NOTAS_LEGALES), 'mapa': len(mapa), 'contrato': contrato,
            'cache': (salida_cache.strip().splitlines() or [''])[-1],
            'veredicto_ficha': wbv[H_FIC]['E%d' % L_RES['ver']].value,
            'veredicto_cte': vfre['D%d' % F['veredicto']].value}


# ==========================================================================
# Demostraciones con pycel
# ==========================================================================
def demo(ruta):
    from pycel import ExcelCompiler
    ok, fallos = [], []

    def prueba(nombre, cond, detalle=''):
        (ok if cond else fallos).append(nombre + (' - ' + detalle if detalle else ''))

    def ev(xl, hoja, coord):
        return xl.evaluate("'%s'!%s" % (hoja, coord))

    def sv(xl, hoja, coord, v):
        xl.set_value("'%s'!%s" % (hoja, coord), v)

    # 1. Subir las raciones del día punta mueve los kg fritos del día punta (X3) y X4.
    xl = ExcelCompiler(ruta)
    k0, r0 = ev(xl, H_DIA, 'L6'), ev(xl, H_DIA, 'L8')   # pycel: evaluar antes de set_value
    sv(xl, H_DIA, 'C%d' % DT['rac'], dp('raciones_dia_punta') * 1.25)
    k1, r1 = ev(xl, H_DIA, 'L6'), ev(xl, H_DIA, 'L8')
    prueba('25 % más de raciones el día punta sube un 25 % los kg fritos del día punta',
           abs(k1 / k0 - 1.25) < 1e-9 and abs(r1 / r0 - 1.25) < 1e-9,
           'kg fritos %.3f -> %.3f · raciones %s -> %s' % (k0, k1, r0, r1))

    # 2. La segunda freidora: litros (X3), kW, riesgo y extinción automática (X9).
    xl = ExcelCompiler(ruta)
    l0, e0, rg0 = ev(xl, H_FRE, 'L5'), ev(xl, H_FRE, 'L6'), ev(xl, H_FRE, 'D%d' % F['riesgo'])
    ev(xl, H_FRE, 'D%d' % F['veredicto'])      # pycel: evaluar ANTES de cambiar la entrada
    ev(xl, H_FRE, 'D%d' % F['nota3'])
    sv(xl, H_FRE, 'C%d' % (F_INI + 1), 'Sí')
    l1, e1, rg1 = ev(xl, H_FRE, 'L5'), ev(xl, H_FRE, 'L6'), ev(xl, H_FRE, 'D%d' % F['riesgo'])
    v1 = ev(xl, H_FRE, 'D%d' % F['veredicto'])
    prueba('poner la segunda freidora dobla los litros, pasa la cocina a riesgo alto y hace '
           'obligatoria la extinción automática', l1 == 2 * l0 and e0 == 0 and e1 == 1
           and rg1 == 'Riesgo alto' and v1.startswith('Riesgo alto sin extinción'),
           'litros %s -> %s · %s -> %s · extinción %s -> %s' % (l0, l1, rg0, rg1, e0, e1))
    # 3. Y si proteges los aparatos con extinción automática: nota 2 del CTE.
    sv(xl, H_FRE, 'D%d' % F['protege'], 'Sí')
    v2 = ev(xl, H_FRE, 'D%d' % F['veredicto'])
    n3 = ev(xl, H_FRE, 'D%d' % F['nota3'])
    prueba('con extinción automática y uso no hospitalario: no es local de riesgo especial, '
           'aunque sigue la nota (3)', v2.startswith('No es local de riesgo especial (nota 2')
           and n3 == 'Sí', repr(v2))

    # 4. Freidora eléctrica (tipo «Otro»): el filtro baja de 1,20 a 0,50 m.
    xl = ExcelCompiler(ruta)
    d0 = ev(xl, H_FRE, 'D%d' % F['dist'])
    sv(xl, H_FRE, 'E%d' % F_INI, 'Otro')
    d1 = ev(xl, H_FRE, 'D%d' % F['dist'])
    prueba('cambiar la freidora a «Otro» baja la distancia mínima del filtro',
           abs(d0 - dp('distancia_filtro_gas_m')) < 1e-12 and abs(d1 - dp('distancia_filtro_otro_m')) < 1e-12,
           '%.2f -> %.2f m' % (d0, d1))

    # 5. El cruce X1: si la ración media pesa más, bajan las raciones por hora (X4) y la
    #    fila de CUADRE avisa; si la línea sube por encima de la freidora, manda la freidora.
    xl = ExcelCompiler(ruta)
    c0 = ev(xl, H_CUE, 'L5')
    ev(xl, H_PAR, 'B%d' % P_X1_CUAD)
    sv(xl, H_PAR, 'B%d' % P_X1, D.CRUCES[0]['valor_defecto'] * 1.1)
    c1 = ev(xl, H_CUE, 'L5')
    cu = ev(xl, H_PAR, 'B%d' % P_X1_CUAD)
    prueba('una ración media un 10 % más pesada baja la capacidad en raciones por hora y el '
           'CUADRE avisa', c1 < c0 and abs(c0 / c1 - 1.1) < 1e-9 and cu.startswith('REVISA'),
           '%.2f -> %.2f raciones/h · %s' % (c0, c1, cu))
    xl = ExcelCompiler(ruta)
    m0 = ev(xl, H_CUE, 'B%d' % K['manda'])
    sv(xl, H_EQU, 'F%d' % E_INI, dp('kg_masa_h_linea') * 2)
    m1 = ev(xl, H_CUE, 'B%d' % K['manda'])
    prueba('si la línea saca el doble, el eslabón que manda pasa a ser la freidora',
           str(m0).startswith('Línea') and str(m1).startswith('Freidora'), '%r -> %r' % (m0, m1))

    # 5 bis. X1 bis (R-05a): kilos fritos por kilo de masa copiados del libro 3.
    xl = ExcelCompiler(ruta)
    ev(xl, H_PAR, 'B%d' % P_X1B_CUAD)
    k0 = ev(xl, H_DIA, 'L5')
    sv(xl, H_PAR, 'B%d' % P_X1B, 0.99)
    k1 = ev(xl, H_DIA, 'L5')
    cu = ev(xl, H_PAR, 'B%d' % P_X1B_CUAD)
    prueba('copiar otros kilos fritos por kilo de masa (X1 bis) mueve los kg fritos del día tipo '
           '(X3) y la fila de CUADRE avisa', abs(k1 / k0 - 0.99 / 0.90) < 1e-9
           and cu.startswith('REVISA'), '%.3f -> %.3f kg · %s' % (k0, k1, cu))

    # 5 ter. R-02: el dato de la ficha es «kW · riesgo», no el rótulo de la fila.
    xl = ExcelCompiler(ruta)
    h0 = ev(xl, H_FIC, 'H%d' % (L_INI + 3))
    sv(xl, H_FRE, 'C%d' % (F_INI + 1), 'Sí')
    h1 = ev(xl, H_FIC, 'H%d' % (L_INI + 3))
    prueba('el dato del eliminatorio 4 de la ficha dice los kW y el riesgo, y con la segunda '
           'freidora pasa a «Riesgo alto»', str(h0) == '28 kW · Riesgo bajo'
           and str(h1) == '53 kW · Riesgo alto', '%r -> %r' % (h0, h1))

    # 6. Ficha: si el conducto no puede ir a cubierta, el local se descarta.
    xl = ExcelCompiler(ruta)
    f0 = ev(xl, H_FIC, 'E%d' % L_RES['ver'])
    ev(xl, H_FIC, 'E%d' % L_RES['primero'])
    sv(xl, H_FIC, 'E%d' % (L_INI + 1), 'No')
    f1 = ev(xl, H_FIC, 'E%d' % L_RES['ver'])
    p1 = ev(xl, H_FIC, 'E%d' % L_RES['primero'])
    prueba('un «No» al conducto a cubierta descarta el local y lo nombra como primer eliminatorio',
           f0 == 'SIGUE ADELANTE CON RESERVAS' and f1 == 'DESCARTAR ESTE LOCAL'
           and p1 == ITEMS[1][0], '%s -> %s · %s' % (f0, f1, p1))
    return ok, fallos


# ==========================================================================
def main():
    requeridos = [i for i, (_t, libros) in D.IDS_LEGALES_REQUERIDOS.items() if LIBRO in libros]
    D.gate_legal(requeridos)
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_zonas(wb)
    hoja_equipos(wb)
    hoja_freidoras(wb)
    hoja_cuello(wb)
    hoja_dia(wb)
    hoja_ficha(wb)
    orden = list(D.HOJAS[LIBRO])
    wb._sheets.sort(key=lambda ws: orden.index(ws.title))

    res = cerrar(wb)
    print('escrito: %s' % res['ruta'])
    print('hojas: %d · fórmulas: %d · celdas verdes: %d · verdes vacías: %d'
          % (res['hojas'], res['formulas'], res['verdes'], len(res['verdes_vacias'])))
    print('fórmulas que devuelven «sin dato» a propósito: %d' % res['sin_dato'])
    print('notas legales: %d · etiquetas en el mapa: %d' % (res['notas_legales'], res['mapa']))
    print('cruces recibidos: %d (X1 y X1 bis, cada uno con su CUADRE) · celdas de origen: %d'
          % (len(RECEPTORAS), len(res['contrato'])))
    print('inject_cache: %s' % res['cache'])
    print('veredicto CTE de El Molinete: %s' % res['veredicto_cte'])
    print('veredicto de la ficha de visita: %s' % res['veredicto_ficha'])
    print('contrato (celdas de origen = valor de datos_ejemplo):')
    for x, hoja, celda, v, e in res['contrato']:
        print('  %-7s %s!%s = %.6f (datos_ejemplo %.6f)' % (x, hoja, celda, v, e))
    ok, fallos = demo(res['ruta'])
    for t in ok:
        print('  demo OK    · %s' % t)
    for t in fallos:
        print('  demo FALLA · %s' % t)
    if fallos:
        raise SystemExit('demos con fallos: %d' % len(fallos))
    return res, len(ok), len(fallos)


if __name__ == '__main__':
    main()
