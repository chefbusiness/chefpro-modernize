#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_carta-de-apertura-y-escandallo-churro.py - libro 3 de «Cómo Montar una
Churrería-Chocolatería» (producto 51, `guia-churreria-chocolateria`; SPEC
`scripts/productos-digitales/guia-churreria-SPEC.md`, §2.1 fila 3, §2.2, §3.3 y §3.5).

Molde H+N: se calca la estructura de
`guia-chocolateria/gen_carta-de-apertura-y-escandallo-chocolate.py` (Parámetros con
fuente y nota por fila, Coste Hora, Mix y Ticket, Decisión de Surtido, cierre con
inject_cache + data_only + mapa + demo con pycel) y es NUEVO: Escandallo por kg de
Masa, Absorción de Aceite y Merma, Chocolate a la Taza, Ración, Docena o Kilo y Los
Dos Márgenes.

Hojas (`datos_ejemplo.HOJAS[3]`): Instrucciones · Parámetros · Escandallo por kg de
Masa · Absorción de Aceite y Merma · Chocolate a la Taza · Coste Hora · Ración,
Docena o Kilo · Mix y Ticket Canal y Temporada · Los Dos Márgenes · Decisión de
Surtido.

ESTE LIBRO ABRE EL GRAFO (D16)
------------------------------
Es el primero del orden de relleno y es ORIGEN de X1, X2, X2 bis, X5, X8, X11 y X17.
Sus celdas de origen son el CONTRATO que fija `datos_ejemplo.CRUCES`: en cada hoja de
origen, rótulo en la columna K y valor en la L desde la fila 5, en el orden de
`CRUCES`. `main()` comprueba al cerrar que cada una de esas celdas devuelve, al
céntimo, el `valor_defecto` que `datos_ejemplo` calcula para El Molinete (es el valor
con el que nacen las celdas verdes de los libros receptores). Este libro no recibe
ningún cruce: no tiene ni una celda «cópialo del libro N».

DECISIONES TÉCNICAS
-------------------
* Una «ración» es la unidad de venta media de la carta ponderada por el mix (la
  definición de `datos_ejemplo.ticket_sin_iva`): una ración de churros, una taza, un
  café o una docena cuentan como una cada una.
* El coste de materia de cada referencia incluye el ACEITE ABSORBIDO (A9): es lo que
  el plan financiero resta por ración. La RENOVACIÓN del aceite (el descarte) es del
  libro 4, y el 6 suma las dos, cada una con su fuente (C1).
* El precio del aceite (EUR/L, base imponible) vive en UNA celda de todo el paquete:
  la fila del aceite de la tabla de insumos de «Parámetros», publicada en
  «Parámetros»!L5. La densidad (kg/L) es un supuesto declarado en celda verde: sin
  ella la absorción (en % del peso frito) no se podría pasar a litros sin meter una
  constante en la fórmula.
* IVA por referencia (D11, V-04, SR-16): sala al 10 %; para llevar, la categoría de
  cada referencia apunta a UNA celda de «Parámetros». Chocolate y bebidas para llevar
  al 10 % en celda verde con aviso; granizado y horchata para llevar al 21 %
  (FC-IVA-04). El food cost se calcula sobre base imponible en los dos lados.
* «Los Dos Márgenes» (D6): el margen sobre materia prima (comparable al «más del
  60 % en producto» de Loomis, CUS-01) y el margen tras aceite y mano de obra
  (comparable, con cautela, al «un poquito más del 50 %» de rentabilidad que declara
  Javier, gestor de La Artesana, CUS-30). Cada cifra con su definición pegada.
* La taza (V-06): la carta usa la denominación que figura en la etiqueta del
  preparado; con menos del 35 % de cacao seco total o con grasa vegetal, aviso
  «consulta a tu servicio de consumo antes de imprimir la carta». Nunca una regla de
  «sólo puedes llamarlo así si...».
* El coste hora de mano de obra es una celda verde con el valor que sale de la
  plantilla de El Molinete (`datos_ejemplo.coste_hora_mano_obra`): el 3 va antes que
  el 8 y lo SUPONE; el libro 8 lo cuadra (X8).
* Cero constantes en las fórmulas salvo las conversiones de unidad (1000 g/kg,
  100 de un porcentaje, 60 min/h, 12 de la docena); IFERROR en toda división; «sin
  dato» = ""; semáforos con ISNUMBER; DV contra un RANGO de la propia hoja.

FRONTERAS (en «Instrucciones»)
------------------------------
Ni el Kit de Escandallos ni la Guía Food Cost costean masa frita por kilo con
absorción y merma (R9): eso es este libro. Las franjas del día viven en el libro 5;
la plantilla y el convenio, en el 8; la renovación del aceite, en el 4.

Salida: build/carta-de-apertura-y-escandallo-churro.xlsx + build/mapa-...json.
Uso: /usr/local/bin/python3 gen_carta-de-apertura-y-escandallo-churro.py
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

LIBRO = 3
NOMBRE = os.path.splitext(D.LIBROS[LIBRO])[0]
FICHERO = D.LIBROS[LIBRO]
TITULO = 'Carta de Apertura y Escandallo del Churro'
SUBJECT = CC.PRODUCTO + ' · Versión 1.0 · octubre 2026'

(H_INS, H_PAR, H_ESC, H_ABS, H_CHO, H_CH, H_RDK, H_MIX, H_DOS, H_SUR) = D.HOJAS[LIBRO]
assert NOMBRE == 'carta-de-apertura-y-escandallo-churro'


def Q(hoja):
    return "'" + hoja + "'!"


def ABS_(hoja, coord):
    """Referencia absoluta a otra hoja del MISMO libro."""
    m = re.match(r'([A-Z]+)(\d+)$', coord)
    return Q(hoja) + '$' + m.group(1) + '$' + m.group(2)


# --------------------------------------------------------------------------
# Formato y utilidades (segunda capa; la primera es `_comun_churreria.py`)
# --------------------------------------------------------------------------
ORO = 'FFD700'
GRIS = '888888'
CAB_BG, CAB_FG = '2D2D2D', 'FFFFFF'
CREMA = 'FFF8E1'
EUR = motor.FMT_EUR
EUR4 = '#,##0.0000 €'
PCT = motor.FMT_PCT
ENT = motor.FMT_ENT
DEC = '#,##0.00'
DEC1 = '#,##0.0'
DEC3 = '#,##0.000'
DEC4 = '#,##0.0000'

NOTAS_LEGALES = []
VERDES = []

ETIQUETA_LISTAS = CC.ETIQUETA_LISTAS


def cabecera_hoja(ws, titulo, nota_txt=None):
    motor.val(ws, 'A1', titulo, bold=True)
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
    """`cols` = [(letra, texto, ancho|None), ...]."""
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
        raise SystemExit('entrada(%s!%s, «%s») sin valor por defecto: ninguna celda '
                         'verde puede quedar vacía' % (ws.title, coord, etiqueta))
    cel = motor.val(ws, coord, valor, fmt=fmt, verde_=True)
    VERDES.append((ws.title, coord, etiqueta, valor))
    return cel


def formula(ws, coord, texto, fmt=None, bold=None, destacar=False):
    cel = motor.f(ws, coord, texto, fmt=fmt, bold=bold)
    if destacar:
        crema(cel)
    return cel


def nota_legal(ws, coord, pid):
    texto = D.nota_legal(pid)
    if not texto:
        raise SystemExit('nota_legal(%r) vacía: gate_legal() debería haber abortado' % pid)
    ws[coord].comment = Comment(texto, 'AI Chef Pro', height=130, width=470)
    NOTAS_LEGALES.append((ws.title, coord, pid))
    return texto


#: Patrón de id de fuente (cualquier id del producto, con su sufijo).
RX_ID = D.RX_ID


def ids_de(fuente):
    return RX_ID.findall(fuente or '')


def nota_fuente(ws, coord, fuente, extra=None):
    """Comentario de procedencia de un dato de SECTOR (CUS-*, CHS-*, FC-IVA-*): id,
    URL y fiabilidad de la ficha del JSON común. NO copia el «tema» de la ficha: hay
    temas que nombran a propósito una cifra de la lista negra para refutarla."""
    partes = []
    for pid in ids_de(fuente):
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
    """«supuesto» -> «supuesto declarado»; un id se deja tal cual."""
    if not fuente:
        return ''
    if fuente == 'supuesto':
        return 'supuesto declarado'
    if fuente.startswith('heredado'):
        return 'heredado de la hermana o del motor'
    return fuente



#: Notas que `datos_ejemplo` escribe para el equipo (con códigos de decisión) y que el
#: comprador lee en otras palabras. Un concepto, una fuente: la CIFRA sigue saliendo de
#: `datos_ejemplo`; aquí sólo cambia la frase que la explica.
NOTAS_PUBLICAS = {
    'iva_llevar_refresco_azucarado': ('Aviso, no regla: El Molinete pone el 21 % por prudencia. Desde '
                                      'el 1-1-2021 las bebidas refrescantes con azúcares añadidos '
                                      'para llevar quedan fuera del tipo reducido y no hay una '
                                      'consulta que diga si tu granizado o tu horchata lo son. Es '
                                      'zona gris: consúltalo con tu asesor y, si te confirma el '
                                      '10 %, cámbialo aquí. En sala siguen al 10 % (servicio de '
                                      'hostelería).'),
    'iva_llevar_chocolate': ('El Molinete aplica el 10 % y lo deja en celda verde: es una zona gris '
                             'y el tipo lo decide tu asesor, no este libro.'),
    'iva_llevar_bebidas': ('El mismo aviso vale para todas las bebidas para llevar, leche con cacao '
                           'incluida. El refresco con azúcar añadido para llevar va al tipo '
                           'general: tiene su propia fila.'),
    'g_masa_churro': 'Supuesto de El Molinete: pesa diez churros de tu masa y divide.',
    'g_masa_porra': 'Supuesto de El Molinete: pesa diez porras de tu masa y divide.',
    'absorcion_aceite_pct': ('Supuesto, sin fuente pública; pon el tuyo. Aceite que se queda en la '
                             'pieza, en % de lo que pesa ya frita: pesa una tanda de masa antes y '
                             'después de freír.'),
    'densidad_aceite_kg_l': ('Supuesto, sin fuente pública; pon el tuyo (lo trae la ficha técnica '
                             'del aceite). Hace falta porque la absorción va en peso y el aceite '
                             'se compra por litros.'),
    'cacao_seco_total_preparado_pct': ('Lo que dice la etiqueta del preparado del ejemplo. Copia el '
                                       'de la etiqueta de TU preparado.'),
    'mix_churros': ('Precio de una caja de 6 sacos de 4 kg, impuestos excluidos (tienda del '
                    'proveedor, leída el 03-10-2026). Cada saco prepara unos 11,5 kg de masa.'),
}
_RX_CODIGO = re.compile(r'\s*\((?:V-\d+|D\d+|SR-\d+|§[\d.]+)[^)]*\)')


def publica(clave, texto):
    """La nota que ve el comprador: la pública si existe; si no, la de `datos_ejemplo`
    sin los códigos internos entre paréntesis («(V-06)», «(§3.5)»...)."""
    if clave in NOTAS_PUBLICAS:
        return NOTAS_PUBLICAS[clave]
    return _RX_CODIGO.sub('', texto or '')


def setup(ws, apaisado=True, titulos=None):
    CC.pagina(ws, apaisado=apaisado, titulos=titulos)


def version_al_pie(ws, fila, col='A'):
    motor.val(ws, '%s%d' % (col, fila), CC.VERSION_LINE)
    ws['%s%d' % (col, fila)].font = Font(size=8, italic=True)


def bloque_contrato(ws, filas, titulo='Lo que Copian Otros Libros (No Muevas Estas Celdas)'):
    """El CONTRATO de `datos_ejemplo.CRUCES`: rótulo en K y valor en L desde la fila 5.

    `filas` = [(fila, rótulo, fórmula, formato)]. En la M, a qué libro y hoja viaja
    cada cifra (sin la frase de las celdas receptoras, que es de los otros libros)."""
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


# ==========================================================================
# Datos que el libro necesita (todos de `datos_ejemplo`)
# ==========================================================================
CARTA = D.CARTA
NR = len(CARTA)
INSUMOS = list(D.INSUMOS.items())
NI = len(INSUMOS)
CHOC_TAZA = 'Taza de chocolate'
CHOC_MEDIA = 'Media taza de chocolate'
PSEUDO_CHOC = {'taza': CHOC_TAZA, 'media_taza': CHOC_MEDIA}
TIPOS_PIEZA = ('churro', 'porra', 'sin masa')
CUANDO = ('Siempre', 'Sólo para llevar')
SI_NO = ('Sí', 'No')
MASAS = ('Preparado comercial', 'Mix propio')
VEREDICTOS = ('Mantener', 'Revisar precio', 'Vigilar rotación', 'Retirar')

#: Categoría de IVA para llevar de cada clave de PARAMS (la sala es una sola).
CATEGORIA_IVA = {
    'iva_llevar_comida': 'Comida para llevar',
    'iva_llevar_chocolate': 'Chocolate para llevar (zona gris)',
    'iva_llevar_bebidas': 'Bebida para llevar (zona gris)',
    'iva_llevar_refresco_azucarado': 'Refresco azucarado para llevar',
}

# Líneas de receta y envase: (id, referencia, insumo, cantidad, unidad, cuándo).
LINEAS = []
for _r in CARTA:
    for _ins, _q in _r['receta']:
        if _ins in PSEUDO_CHOC:
            LINEAS.append((_r['id'], _r['nombre'], PSEUDO_CHOC[_ins], _q, 'Siempre'))
        else:
            LINEAS.append((_r['id'], _r['nombre'], D.INSUMOS[_ins]['nombre'], _q, 'Siempre'))
    for _ins, _q in _r['envase_llevar']:
        LINEAS.append((_r['id'], _r['nombre'], D.INSUMOS[_ins]['nombre'], _q, 'Sólo para llevar'))
NL = len(LINEAS)

# ==========================================================================
# Posiciones
# ==========================================================================
# ---- Parámetros ----------------------------------------------------------
IVA_KEYS = ('iva_sala', 'iva_llevar_comida', 'iva_llevar_chocolate', 'iva_llevar_bebidas',
            'iva_llevar_refresco_azucarado', 'iva_general', 'iva_compra_alimentos')
MASA_KEYS = ('g_masa_churro', 'g_masa_porra', 'merma_masa_pct', 'kg_fritos_por_kg_masa',
             'absorcion_aceite_pct', 'densidad_aceite_kg_l', 'azucar_g_por_100g_masa',
             'kg_mix_por_kg_masa')
P_SEC_IVA = 4
PROW = {}
for _i, _k in enumerate(IVA_KEYS):
    PROW[_k] = P_SEC_IVA + 1 + _i                       # 5..11
P_SEC_MASA = PROW[IVA_KEYS[-1]] + 2                     # 13
for _i, _k in enumerate(MASA_KEYS):
    PROW[_k] = P_SEC_MASA + 1 + _i                      # 14..21
P_MASA_SEL = PROW[MASA_KEYS[-1]] + 1                    # 22
P_SEC_VASO = P_MASA_SEL + 2                             # 24
P_VASO = P_SEC_VASO + 1                                 # 25
P_SEC_UMB = P_VASO + 2                                  # 27
P_UMB_MARGEN = P_SEC_UMB + 1                            # 28
P_UMB_ROT = P_SEC_UMB + 2                               # 29
P_SEC_INS = P_UMB_ROT + 2                               # 31
P_INS_CAB = P_SEC_INS + 1                               # 32
P_INS_INI = P_INS_CAB + 1                               # 33
P_INS_FIN = P_INS_INI + NI - 1
INS_ROW = dict((k, P_INS_INI + i) for i, (k, _v) in enumerate(INSUMOS))
P_LISTAS = P_INS_FIN + 3


def PB(clave):
    """Celda absoluta del valor de un parámetro de PARAMS en «Parámetros»."""
    return ABS_(H_PAR, 'B%d' % PROW[clave])


def PRECIO(insumo):
    """Precio sin IVA por unidad (columna G) de un insumo."""
    return ABS_(H_PAR, 'G%d' % INS_ROW[insumo])


def COL_INSUMOS(letra):
    return "%s$%s$%d:$%s$%d" % (Q(H_PAR), letra, P_INS_INI, letra, P_INS_FIN)


TABLA_NOMBRES = COL_INSUMOS('A')

# ---- Escandallo por kg de Masa ---------------------------------------------
E_COM_CAB = 6
E_COM_MIX = 7
E_COM_AGUA = 8
E_COM_TOT = 9
E_PRO_CAB = 12
E_PRO_HAR = 13
E_PRO_SAL = 14
E_PRO_AGUA = 15
E_PRO_TOT = 16
E_AHORRO = 18
E_COSTE_MASA = 19
E_MASA_USADA = 20
E_PZ_CAB = 23
E_PZ = dict(g=24, gfr=25, pzkg=26, masa=27, aceite=28, azucar=29, total=30, docena=31)
E_REF_SEC = 33
E_REF_CAB = 34
E_REF_INI = 35
E_REF_FIN = E_REF_INI + NR - 1
E_LIN_SEC = E_REF_FIN + 3
E_LIN_CAB = E_LIN_SEC + 1
E_LIN_INI = E_LIN_CAB + 1
E_LIN_FIN = E_LIN_INI + NL - 1
E_LISTAS = E_LIN_FIN + 3
FILA_ESC = dict((r['id'], E_REF_INI + i) for i, r in enumerate(CARTA))
COSTE_MASA = ABS_(H_ESC, 'B%d' % E_COSTE_MASA)

# ---- Absorción de Aceite y Merma -------------------------------------------
A_ROW = dict(kfr=5, abs=6, kgac=7, dens=8, lac=9, precio=10, eurkg=11,
             merma=14, prod=15, coste_merma=16,
             kgrac=19, acrac=20, lrac=21, peso=22)
A_ESC_CAB = 26
A_ESC_INI = 27
ESC_FACTORES = (0.6, 0.8, 1.0, 1.2, 1.4)
A_ESC_FIN = A_ESC_INI + len(ESC_FACTORES) - 1
ACEITE_EURKG = ABS_(H_ABS, 'B%d' % A_ROW['eurkg'])

# ---- Chocolate a la Taza -----------------------------------------------------
C_ROW = dict(precio=6, kgform=7, rinde=8, kgl=9, cprep=10, leche=11, clitro=12,
             ml_taza=13, ml_media=14, taza=15, media=16,
             denom=20, cacao=21, grasa=22, minimo=23, aviso=24, nombre=25,
             iva=28, aviso_iva=29)
C_TZ_CAB = 32
TAZAS = [r for r in CARTA if r['familia'] == 'Chocolate a la taza']
C_TZ_INI = C_TZ_CAB + 1
C_TZ_FIN = C_TZ_INI + len(TAZAS) - 1
C_LISTAS = C_TZ_FIN + 4
COSTE_TAZA = ABS_(H_CHO, 'B%d' % C_ROW['taza'])
COSTE_MEDIA = ABS_(H_CHO, 'B%d' % C_ROW['media'])

# ---- Coste Hora --------------------------------------------------------------
H_ROW = dict(chora=5, minut=6, rach=7, morac=8, ticket=9, peso=10, mopz=12, mokg=13)
MO_RACION = ABS_(H_CH, 'B%d' % H_ROW['morac'])

# ---- Mix y Ticket Canal y Temporada ---------------------------------------------
M_RES_CAB = 5
M_RES = dict(ticket=6, materia=7, margen_eur=8, margen_pct=9, pct=10, kg=11, cuadre=12)
M_CAB = 16
M_INI = 17
M_FIN = M_INI + NR - 1
M_TOT = M_FIN + 1
M_LISTAS = M_TOT + 4
FILA_MIX = dict((r['id'], M_INI + i) for i, r in enumerate(CARTA))
#: Columnas del resumen: (columna, temporada, canal).
M_COLS = (('B', 'invierno', 'sala'), ('C', 'invierno', 'llevar'), ('D', 'invierno', 'total'),
          ('E', 'verano', 'sala'), ('F', 'verano', 'llevar'), ('G', 'verano', 'total'))

# ---- Ración, Docena o Kilo -----------------------------------------------------------
CHURROS = [r for r in CARTA if r['familia'] == 'Churros y porras']
R_CAB = 6
R_INI = 7
R_FIN = R_INI + len(CHURROS) - 1
R_RES = R_FIN + 3

# ---- Los Dos Márgenes ----------------------------------------------------------------
DM = dict(cab=5, m1=6, m2=7, e1=8, e2=9, ref_cab=12, loomis=13, artesana=14,
          cmp_cab=17, c1=18, c2=19, d1=20, d2=21)

# ---- Decisión de Surtido -------------------------------------------------------------
S_CAB = 6
S_INI = 7
S_FIN = S_INI + NR - 1
S_TOT = S_FIN + 1
S_CNT = S_TOT + 3
S_LISTAS = S_CNT + len(VEREDICTOS) + 6


# ==========================================================================
# Hoja «Instrucciones»
# ==========================================================================
def _orden_relleno():
    partes = ['%d (%s)' % (n, D.LIBROS[n]) for n in D.ORDEN_RELLENO if n != 7]
    return ('Orden de relleno del paquete: ' + ', luego '.join(partes)
            + '. El libro 7 (%s) no depende de ninguno: rellénalo cuando quieras. '
              'Este es el libro 3 y va el PRIMERO: los demás copian sus cifras.' % D.LIBROS[7])


def _destinos_texto():
    """Una línea por celda de origen, con los libros que la copian."""
    por_celda = {}
    for c in D.CRUCES:
        if c['origen'] != LIBRO:
            continue
        clave = (c['hoja_origen'], c['celda_origen'])
        por_celda.setdefault(clave, {'concepto': c['concepto'], 'destinos': []})
        por_celda[clave]['destinos'].append('libro %d (%s)' % (c['receptor'], c['x']))
    lineas = []
    for (hoja, celda), d in sorted(por_celda.items(), key=lambda kv: (D.HOJAS[LIBRO].index(kv[0][0]),
                                                                       int(kv[0][1][1:]))):
        lineas.append('%s!%s - %s. Lo copia: %s.' % (hoja, celda, d['concepto'],
                                                    ', '.join(sorted(set(d['destinos'])))))
    return lineas


PASOS = [
    '1. Hoja «Parámetros». Arriba, el IVA de cada canal: la sala al 10 % y, para llevar, '
    'una celda por categoría. Chocolate y bebidas para llevar van al 10 % en celda verde '
    'con un aviso (consulta a tu asesor: con agua y un preparado azucarado podría ser el '
    '21 %); granizado y horchata para llevar llevan el 21 % por prudencia, también en celda '
    'verde y con el mismo aviso (es zona gris: lo decide tu asesor). Abajo, '
    'los supuestos de la masa y del aceite, y la tabla de insumos: es la ÚNICA tabla donde '
    'se tocan los precios. El del aceite es la celda única de todo el paquete.',
    '2. Hoja «Escandallo por kg de Masa». Cuánto cuesta un kilo de masa con el preparado '
    'comercial y con un mix propio, cuánto cuesta un churro y una porra, y de la masa a '
    'cada una de las 24 referencias de la carta. Al pie, la receta y el envase de cada '
    'referencia: el envase sólo cuenta cuando se vende para llevar.',
    '3. Hoja «Absorción de Aceite y Merma». Los euros de aceite que se lleva cada kilo de '
    'masa frita y lo que cuesta la masa que se fríe y no se vende. Aquí sólo está el aceite '
    'ABSORBIDO; la renovación del aceite de la cuba la calcula el libro 4.',
    '4. Hoja «Chocolate a la Taza». Lo que cuesta una taza y qué dice la etiqueta de tu '
    'preparado. La carta usa la denominación que figura en esa etiqueta; si el cacao seco '
    'total baja del 35 % o lleva grasa vegetal, la hoja te pide consultar a tu servicio de '
    'consumo antes de imprimir la carta.',
    '5. Hoja «Coste Hora». El coste de empresa de una hora de tu plantilla y los minutos de '
    'mano de obra que lleva cada ración. Nace con el de El Molinete; cuando rellenes el '
    'libro 8, su fila de CUADRE te dirá si este número se ha quedado viejo.',
    '6. Hoja «Ración, Docena o Kilo». Los siete formatos de churro y porra, comparados por '
    'los euros que deja cada kilo de masa que fríes.',
    '7. Hoja «Mix y Ticket Canal y Temporada». El PVP con IVA de cada referencia, la parte '
    'que se vende para llevar y el mix de invierno (septiembre a junio) y de verano (julio '
    'y agosto). De aquí salen el ticket sin IVA y el coste de materia por canal y '
    'temporada, que copian los libros 5 y 6.',
    '8. Hoja «Los Dos Márgenes». Tu margen sobre materia prima y tu margen tras aceite y '
    'mano de obra, al lado de las dos cifras publicadas con las que se suelen comparar, '
    'cada una con su definición. No son la misma cosa y no se mezclan.',
    '9. Hoja «Decisión de Surtido». Margen en euros por unidad contra rotación: qué '
    'mantener, a qué revisarle el precio, qué vigilar y qué retirar.',
]

NOTAS_LIBRO = [
    'UNA RACIÓN, EN ESTE PAQUETE, ES LA UNIDAD DE VENTA MEDIA DE LA CARTA. Una ración de '
    'churros, una taza, un café o una docena cuentan como una cada una, ponderadas por el '
    'mix. Es la unidad con la que los libros 1, 4, 5 y 6 cuentan raciones al día y al año.',
    'EL COSTE DE MATERIA INCLUYE EL ACEITE QUE SE LLEVA LA MASA. Es el que el plan '
    'financiero resta por ración. El aceite que tiras al cambiar la cuba (la renovación) no '
    'está aquí: lo calcula el libro 4 y el 6 suma las dos partes, cada una con su fuente.',
    'LOS DOS MÁRGENES NO SON LA MISMA COSA. «Márgenes superiores al 60 % en producto» '
    '(Loomis Pay, proveedor de TPV) es un margen sobre materia prima, sin método publicado. '
    '«Un poquito más del 50 %» es la rentabilidad que declara de palabra Javier, gestor de '
    'La Artesana (Palma): no es un margen sobre materia prima. El plan financiero usa el '
    'margen de TU escandallo, nunca ninguno de los dos.',
    'EL IVA SE APLICA POR REFERENCIA Y POR CANAL. En sala, todo al 10 % (servicio de '
    'hostelería). Para llevar, churros y porras al 10 %; chocolate y demás bebidas para '
    'llevar, al 10 % en celda verde con aviso; granizado y horchata para llevar, al 21 % por '
    'prudencia (llevan azúcar añadido y es zona gris), en celda verde y con el mismo aviso. '
    'El capítulo 03 de la guía lo explica. El food cost se calcula SIEMPRE sobre base '
    'imponible en los dos lados.',
    'LOS SUPUESTOS DE LA MASA Y DEL ACEITE NO SON DATOS DEL SECTOR. Los gramos por pieza, la '
    'absorción, la densidad, la merma y los kilos fritos por kilo de masa son supuestos '
    'declarados de El Molinete, sin fuente pública. Pon los tuyos: pesa diez piezas, pesa '
    'la masa de una tanda y lo que sale de la freidora, y apunta lo que tiras al cierre.',
    'DÓNDE NO ESTÁ LO QUE AQUÍ NO ESTÁ. Ni el Kit de Escandallos ni la Guía Food Cost '
    'costean masa frita por kilo, con absorción de aceite y merma: eso es este libro. Las '
    'franjas del día viven en el libro 5; la plantilla, el convenio y la madrugada, en el 8; '
    'el cambio del aceite y el gestor de aceite usado, en el 4.',
]

CADENCIA = ('Cada cuánto se usa este libro: los precios de insumos, cada vez que te suba un '
            'proveedor (el aceite, como mínimo una vez al mes). Los gramos por pieza, la '
            'absorción y la merma, al abrir y cada vez que cambies de masa o de freidora. El '
            'mix y los PVP, a los tres meses de abrir con las ventas del TPV, y otra vez al '
            'pasar a la carta de verano. Cada vez que cambie una cifra del bloque «Lo que '
            'Copian Otros Libros», cópiala de nuevo en los libros que la usan.')


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS, 0)
    ws.column_dimensions['A'].width = 100.0
    cabecera_hoja(ws, TITULO)
    motor.val(ws, 'A3', 'Para qué sirve: decidir a cuánto vendes la ración, la docena, el '
                        'kilo y la taza, con el coste real de la masa frita y del aceite que '
                        'se lleva, y saber qué margen te queda de verdad.')
    ws['A3'].font = Font(italic=True, size=9)
    fila = 5
    seccion(ws, 'A%d' % fila, 'Instrucciones de Uso')
    fila += 1
    entrada(ws, 'A%d' % fila, motor.NOTA_VERDES, etiqueta='Leyenda de celdas verdes')
    fila += 1
    motor.val(ws, 'A%d' % fila, 'Las celdas en crema son resultados que el libro calcula; '
                                'las blancas con fórmula, también. No escribas encima.', wrap=True)
    fila += 2
    for paso in PASOS:
        motor.val(ws, 'A%d' % fila, paso, wrap=True)
        ws.row_dimensions[fila].height = 58
        fila += 1
    fila += 1
    seccion(ws, 'A%d' % fila, 'Orden de Relleno y Lo que Este Libro Pasa a los Demás')
    fila += 1
    motor.val(ws, 'A%d' % fila, _orden_relleno(), wrap=True)
    ws.row_dimensions[fila].height = 58
    fila += 1
    motor.val(ws, 'A%d' % fila,
              'Las cifras que viajan están en el bloque «Lo que Copian Otros Libros» de cada '
              'hoja (rótulo en la columna K, valor en la L). Ningún libro se vincula con otro '
              'por fórmula: el libro que la recibe tiene una celda verde para copiarla a mano '
              'y una fila de CUADRE que avisa si se ha quedado vieja.', wrap=True)
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
        ws.row_dimensions[fila].height = 72
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, CADENCIA, wrap=True)
    ws.row_dimensions[fila].height = 58
    fila += 2
    motor.val(ws, 'A%d' % fila, CC.NOTA_DESPROTEGER, wrap=True)
    fila += 2
    motor.val(ws, 'A%d' % fila, CC.BIO, wrap=True)
    fila += 1
    version_al_pie(ws, fila)
    setup(ws, apaisado=False)
    return ws


# ==========================================================================
# Hoja «Parámetros»
# ==========================================================================
def fila_param(ws, fila, etiqueta, valor, fmt, unidad, fuente, nota, ids_legales=(),
               form=None, pct=False):
    motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
    if form is not None:
        cel = formula(ws, 'B%d' % fila, form, fmt=fmt, bold=True, destacar=True)
    else:
        cel = entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
        if pct:
            motor.dv_porcentaje(ws, [cel.coordinate])
        elif isinstance(valor, (int, float)) and not isinstance(valor, bool):
            motor.dv_numerica(ws, [cel.coordinate], minimo=0)
    motor.val(ws, 'C%d' % fila, unidad)
    motor.val(ws, 'D%d' % fila, texto_fuente(fuente), wrap=True)
    ws['D%d' % fila].font = Font(size=8, color=GRIS)
    gris(ws, 'E%d' % fila, nota)
    ws.row_dimensions[fila].height = 44
    for pid in ids_legales:
        nota_legal(ws, cel.coordinate, pid)
    if not ids_legales:
        nota_fuente(ws, cel.coordinate, fuente)
    return cel


ETIQUETAS_PARAM = {
    'iva_sala': ('IVA en sala, barra y terraza (servicio de hostelería)', 'tipo'),
    'iva_llevar_comida': ('IVA de churros y porras para llevar', 'tipo'),
    'iva_llevar_chocolate': ('IVA del chocolate a la taza para llevar', 'tipo'),
    'iva_llevar_bebidas': ('IVA de las demás bebidas para llevar (café, leche con cacao, zumo, '
                           'agua, batido)', 'tipo'),
    'iva_llevar_refresco_azucarado': ('IVA del granizado y la horchata para llevar', 'tipo'),
    'iva_general': ('IVA general (envases, equipamiento, servicios)', 'tipo'),
    'iva_compra_alimentos': ('IVA soportado de los alimentos que compras', 'tipo'),
    'g_masa_churro': ('Gramos de masa por churro (lo que se vende)', 'g/pieza'),
    'g_masa_porra': ('Gramos de masa por porra (lo que se vende)', 'g/pieza'),
    'merma_masa_pct': ('Merma: masa que se fríe y no se vende', 'sobre lo frito'),
    'kg_fritos_por_kg_masa': ('Kilos fritos que salen de un kilo de masa', 'kg/kg'),
    'absorcion_aceite_pct': ('Absorción de aceite, en % del peso frito', 'del peso frito'),
    'densidad_aceite_kg_l': ('Densidad del aceite', 'kg/L'),
    'azucar_g_por_100g_masa': ('Azúcar para espolvorear por cada 100 g de masa vendida', 'g/100 g'),
    'kg_mix_por_kg_masa': ('Kilos de preparado comercial por kilo de masa', 'kg/kg'),
}
LEGALES_PARAM = {
    'iva_sala': ('CHN-71c',),
    'iva_llevar_chocolate': ('CUN-18',),
    'iva_llevar_bebidas': ('CUN-18',),
    'iva_llevar_refresco_azucarado': ('CUN-17',),
    'iva_general': ('CHN-71c',),
}
FMT_PARAM = {'g_masa_churro': DEC1, 'g_masa_porra': DEC1, 'kg_fritos_por_kg_masa': DEC,
             'densidad_aceite_kg_l': DEC, 'azucar_g_por_100g_masa': DEC1,
             'kg_mix_por_kg_masa': DEC4}
PCT_PARAM = set(IVA_KEYS) | {'merma_masa_pct', 'absorcion_aceite_pct'}


def hoja_parametros(wb):
    ws = wb.create_sheet(H_PAR)
    cabecera_hoja(ws, H_PAR, 'Todo lo que el resto de hojas da por sabido vive aquí. Ninguna '
                             'fórmula de este libro lleva un número de IVA, de margen o de '
                             'umbral dentro.')
    for letra, ancho in (('A', 50), ('B', 15), ('C', 13), ('D', 22), ('E', 66), ('F', 10),
                         ('G', 15), ('H', 16), ('I', 60)):
        ws.column_dimensions[letra].width = ancho

    seccion(ws, 'A%d' % P_SEC_IVA, 'IVA por Canal (El Capítulo 03 de la Guía lo Explica)')
    for k in IVA_KEYS:
        valor, fuente, nota = D.PARAMS[k]
        nota = publica(k, nota)
        etq, uni = ETIQUETAS_PARAM[k]
        if k in ('iva_llevar_chocolate', 'iva_llevar_bebidas'):
            nota = ('Consulta a tu asesor: con agua y un preparado azucarado podría ser el '
                    '21 %. ' + nota)
        fila_param(ws, PROW[k], etq, valor, PCT, uni, fuente, nota,
                   ids_legales=LEGALES_PARAM.get(k, ()), pct=True)

    seccion(ws, 'A%d' % P_SEC_MASA, 'Masa, Fritura y Aceite (Supuestos Declarados de El Molinete)')
    for k in MASA_KEYS:
        valor, fuente, nota = D.PARAMS[k]
        nota = publica(k, nota)
        etq, uni = ETIQUETAS_PARAM[k]
        fila_param(ws, PROW[k], etq, valor, PCT if k in PCT_PARAM else FMT_PARAM[k], uni,
                   fuente, nota, pct=k in PCT_PARAM)
    motor.val(ws, 'A%d' % P_MASA_SEL, 'Masa con la que costeas la carta', wrap=True)
    entrada(ws, 'B%d' % P_MASA_SEL, MASAS[0], etiqueta='Masa con la que costeas la carta')
    motor.val(ws, 'C%d' % P_MASA_SEL, 'lista')
    motor.val(ws, 'D%d' % P_MASA_SEL, 'decisión 5', wrap=True)
    ws['D%d' % P_MASA_SEL].font = Font(size=8, color=GRIS)
    gris(ws, 'E%d' % P_MASA_SEL, 'El Molinete compra el preparado comercial. Cambia a «Mix '
                                 'propio» para ver el escandallo con tu mezcla (hoja '
                                 '«Escandallo por kg de Masa»).', alto=36)

    seccion(ws, 'A%d' % P_SEC_VASO, 'El Vaso para Llevar, Cobrado Aparte')
    v = D.CARGO_VASO
    cel = fila_param(ws, P_VASO, v['nombre'] + ': importe con IVA', v['pvp'], EUR, 'EUR/vaso',
                     v['fuente_pvp'], v['nota'] + ' Su IVA es el de «las demás bebidas para '
                     'llevar» (fila %d).' % PROW['iva_llevar_bebidas'],
                     ids_legales=(v['fuente_obligacion'],))

    seccion(ws, 'A%d' % P_SEC_UMB, 'Umbrales de la Decisión de Surtido (Criterio de la Casa)')
    fila_param(ws, P_UMB_MARGEN, 'Margen mínimo por unidad para no revisar el precio', 0.50, EUR,
               'EUR/unidad', 'supuesto',
               'Criterio de la casa, no del sector: es el margen en EUROS de la unidad de '
               'venta. Un margen alto en porcentaje sobre un churro de 0,30 EUR no paga la '
               'renta.')
    fila_param(ws, P_UMB_ROT, 'Rotación mínima para no vigilar una referencia', 2.0, DEC1,
               '% del mix', 'supuesto',
               'Por debajo de este peso en el mix de invierno Y en el de verano, la '
               'referencia ocupa carta, stock y cabeza sin vender.')

    seccion(ws, 'A%d' % P_SEC_INS, 'Insumos: La Única Tabla Donde se Tocan los Precios')
    encabezados(ws, P_INS_CAB, [
        ('A', 'Insumo', None), ('B', 'Precio del formato (EUR)', None),
        ('C', '¿El precio lleva IVA?', None), ('D', 'Tipo de IVA', None),
        ('E', 'Cantidad del formato', None), ('F', 'Unidad', None),
        ('G', 'Precio SIN IVA por unidad (EUR)', None), ('H', 'Fuente', None),
        ('I', 'Base de IVA declarada y nota', None)], alto=44, congelar=False)
    coords_sino = []
    for k, ins in INSUMOS:
        fila = INS_ROW[k]
        motor.val(ws, 'A%d' % fila, ins['nombre'], wrap=True)
        b = entrada(ws, 'B%d' % fila, ins['precio_formato'], fmt=EUR,
                    etiqueta='Precio del formato de %s' % ins['nombre'])
        motor.dv_numerica(ws, [b.coordinate], minimo=0)
        entrada(ws, 'C%d' % fila, 'No', etiqueta='¿Lleva IVA? %s' % ins['nombre'])
        coords_sino.append('C%d' % fila)
        tipo = 'iva_compra_alimentos' if k in D.INSUMOS_ALIMENTO else 'iva_general'
        formula(ws, 'D%d' % fila, '=%s' % PB(tipo), fmt=PCT)
        e = entrada(ws, 'E%d' % fila, ins['cantidad_formato'], fmt=DEC,
                    etiqueta='Cantidad del formato de %s' % ins['nombre'])
        motor.dv_numerica(ws, [e.coordinate], minimo=0)
        motor.val(ws, 'F%d' % fila, ins['unidad'])
        formula(ws, 'G%d' % fila,
                '=IFERROR(IF(C%d="Sí",B%d/(1+D%d),B%d)/E%d,"")' % (fila, fila, fila, fila, fila),
                fmt=EUR4, bold=True, destacar=True)
        motor.val(ws, 'H%d' % fila, texto_fuente(ins['fuente']))
        ws['H%d' % fila].font = Font(size=8, color=GRIS)
        gris(ws, 'I%d' % fila, 'Base de la fuente: %s. %s' % (ins['base_iva'], publica(k, ins['nota'])))
        ws.row_dimensions[fila].height = 40 if ins['nota'] else 24
        nota_fuente(ws, b.coordinate, ins['fuente'])
    refs, _fin = CC.bloque_listas(ws, P_LISTAS, (('Sí o no', SI_NO), ('Masa', MASAS)))
    CC.dv_rango(ws, coords_sino, refs['Sí o no'], '¿Lleva IVA?',
                'Elige «Sí» si el precio que has escrito lleva el IVA dentro, o «No».')
    CC.dv_rango(ws, ['B%d' % P_MASA_SEL], refs['Masa'], 'Masa',
                'Elige «Preparado comercial» o «Mix propio».')

    # --- el CONTRATO (X2, X17) ---------------------------------------------
    bloque_contrato(ws, [
        (5, 'Precio del aceite (base imponible), EUR/L', '=G%d' % INS_ROW['aceite'], EUR4),
        (6, 'Absorción de aceite, en % del peso frito', '=B%d' % PROW['absorcion_aceite_pct'], PCT),
        (7, 'Densidad del aceite, kg/L', '=B%d' % PROW['densidad_aceite_kg_l'], DEC),
        (8, 'Precio del preparado para masa (base imponible), EUR/kg',
         '=G%d' % INS_ROW['mix_churros'], EUR4),
        (9, 'Kilos fritos que salen de un kilo de masa, kg/kg',
         '=B%d' % PROW['kg_fritos_por_kg_masa'], DEC),
    ] + [(10 + i, 'Precio del insumo «%s» (base imponible), EUR/unidad' % D.INSUMOS[k]['nombre'],
          '=G%d' % INS_ROW[k], EUR4)
         for i, k in enumerate(enmiendas_churreria.INSUMOS_STOCK_X17)])
    version_al_pie(ws, P_LISTAS + 6)
    setup(ws, apaisado=True, titulos='%d:%d' % (P_INS_CAB, P_INS_CAB))
    return ws


# ==========================================================================
# Hoja «Escandallo por kg de Masa»
# ==========================================================================
def hoja_escandallo(wb):
    ws = wb.create_sheet(H_ESC)
    cabecera_hoja(ws, H_ESC, 'Datos de ejemplo para que las fórmulas calculen: las cantidades '
                             'no son una receta. Todos los precios, SIN IVA, de la tabla de '
                             'insumos de «Parámetros».')
    for letra, ancho in (('A', 44), ('B', 16), ('C', 14), ('D', 15), ('E', 14), ('F', 15),
                         ('G', 13), ('H', 13), ('I', 13), ('J', 13), ('K', 13), ('L', 13),
                         ('M', 13), ('N', 14), ('O', 14)):
        ws.column_dimensions[letra].width = ancho
    cols_kg = [('A', 'Concepto', None), ('B', 'Cantidad por kg de masa', None),
               ('C', 'Unidad', None), ('D', 'Precio SIN IVA por unidad (EUR)', None),
               ('E', 'Importe (EUR)', None), ('F', 'Fuente', None)]

    # --- 1. preparado comercial ---------------------------------------------
    seccion(ws, 'A%d' % (E_COM_CAB - 1), '1. Un Kilo de Masa con el Preparado Comercial')
    encabezados(ws, E_COM_CAB, cols_kg, alto=36, congelar=False)
    mix = D.INSUMOS['mix_churros']
    motor.val(ws, 'A%d' % E_COM_MIX, mix['nombre'], wrap=True)
    formula(ws, 'B%d' % E_COM_MIX, '=%s' % PB('kg_mix_por_kg_masa'), fmt=DEC4)
    motor.val(ws, 'C%d' % E_COM_MIX, 'kg')
    formula(ws, 'D%d' % E_COM_MIX, '=%s' % PRECIO('mix_churros'), fmt=EUR4)
    formula(ws, 'E%d' % E_COM_MIX, '=IFERROR(B%d*D%d,"")' % (E_COM_MIX, E_COM_MIX), fmt=EUR4)
    motor.val(ws, 'F%d' % E_COM_MIX, mix['fuente'])
    motor.val(ws, 'A%d' % E_COM_AGUA, 'Agua (sin coste)')
    formula(ws, 'B%d' % E_COM_AGUA, '=1-B%d' % E_COM_MIX, fmt=DEC4)
    motor.val(ws, 'C%d' % E_COM_AGUA, 'L')
    motor.val(ws, 'D%d' % E_COM_AGUA, 'sin coste')
    motor.val(ws, 'F%d' % E_COM_AGUA, 'calculado')
    motor.val(ws, 'A%d' % E_COM_TOT, 'COSTE DE 1 KG DE MASA CON EL PREPARADO (EUR)', bold=True)
    formula(ws, 'E%d' % E_COM_TOT, '=SUM(E%d:E%d)' % (E_COM_MIX, E_COM_AGUA), fmt=EUR4,
            bold=True, destacar=True)

    # --- 2. mix propio ----------------------------------------------------
    seccion(ws, 'A%d' % (E_PRO_CAB - 1), '2. Un Kilo de Masa con Mix Propio (Decisión 5)')
    encabezados(ws, E_PRO_CAB, cols_kg, alto=36, congelar=False)
    for fila, (k, q) in zip((E_PRO_HAR, E_PRO_SAL), D.RECETA_MIX_PROPIO):
        ins = D.INSUMOS[k]
        motor.val(ws, 'A%d' % fila, ins['nombre'], wrap=True)
        b = entrada(ws, 'B%d' % fila, q, fmt=DEC4, etiqueta='Mix propio: %s' % ins['nombre'])
        motor.dv_numerica(ws, [b.coordinate], minimo=0, maximo=1)
        motor.val(ws, 'C%d' % fila, ins['unidad'])
        formula(ws, 'D%d' % fila, '=%s' % PRECIO(k), fmt=EUR4)
        formula(ws, 'E%d' % fila, '=IFERROR(B%d*D%d,"")' % (fila, fila), fmt=EUR4)
        motor.val(ws, 'F%d' % fila, texto_fuente(ins['fuente']))
    motor.val(ws, 'A%d' % E_PRO_AGUA, 'Agua (sin coste)')
    formula(ws, 'B%d' % E_PRO_AGUA, '=1-SUM(B%d:B%d)' % (E_PRO_HAR, E_PRO_SAL), fmt=DEC4)
    motor.val(ws, 'C%d' % E_PRO_AGUA, 'L')
    motor.val(ws, 'D%d' % E_PRO_AGUA, 'sin coste')
    motor.val(ws, 'F%d' % E_PRO_AGUA, 'calculado')
    motor.val(ws, 'A%d' % E_PRO_TOT, 'COSTE DE 1 KG DE MASA CON MIX PROPIO (EUR)', bold=True)
    formula(ws, 'E%d' % E_PRO_TOT, '=SUM(E%d:E%d)' % (E_PRO_HAR, E_PRO_AGUA), fmt=EUR4,
            bold=True, destacar=True)
    gris(ws, 'G%d' % E_PRO_HAR, 'Proporciones de EJEMPLO para que la comparación calcule, no '
                                'una receta. El ahorro del mix propio se paga con pesar, '
                                'tamizar y con la regularidad de la masa.')
    ws.merge_cells('G%d:L%d' % (E_PRO_HAR, E_PRO_SAL))

    motor.val(ws, 'A%d' % E_AHORRO, 'Ahorro del mix propio por kg de masa (EUR)')
    formula(ws, 'B%d' % E_AHORRO, '=E%d-E%d' % (E_COM_TOT, E_PRO_TOT), fmt=EUR4, destacar=True)
    motor.val(ws, 'A%d' % E_COSTE_MASA, 'COSTE DEL KG DE MASA CON EL QUE COSTEAS (EUR)', bold=True)
    formula(ws, 'B%d' % E_COSTE_MASA, '=IF(%s="%s",E%d,E%d)'
            % (ABS_(H_PAR, 'B%d' % P_MASA_SEL), MASAS[1], E_PRO_TOT, E_COM_TOT),
            fmt=EUR4, bold=True, destacar=True)
    motor.val(ws, 'A%d' % E_MASA_USADA, 'Masa elegida en «Parámetros»')
    formula(ws, 'B%d' % E_MASA_USADA, '=%s' % ABS_(H_PAR, 'B%d' % P_MASA_SEL))

    # --- 3. la pieza ----------------------------------------------------
    seccion(ws, 'A%d' % (E_PZ_CAB - 1), '3. La Pieza: Churro y Porra')
    encabezados(ws, E_PZ_CAB, [('A', 'Concepto', None), ('B', 'Churro', None),
                               ('C', 'Porra', None)], alto=24, congelar=False)
    etiquetas = (
        ('g', 'Gramos de masa por pieza (lo que se vende)', DEC1),
        ('gfr', 'Gramos de masa que hay que freír por pieza (con la merma)', DEC1),
        ('pzkg', 'Piezas por kilo de masa vendida', DEC1),
        ('masa', 'Coste de la masa por pieza (EUR)', EUR4),
        ('aceite', 'Aceite absorbido por pieza (EUR)', EUR4),
        ('azucar', 'Azúcar de espolvorear por pieza (EUR)', EUR4),
        ('total', 'COSTE DE MATERIA DE LA PIEZA (EUR)', EUR4),
        ('docena', 'Coste de materia de una docena (EUR)', EUR),
    )
    for clave, etq, fmt in etiquetas:
        fila = E_PZ[clave]
        motor.val(ws, 'A%d' % fila, etq, bold=clave == 'total')
        for col, gkey in (('B', 'g_masa_churro'), ('C', 'g_masa_porra')):
            c = '%s%d' % (col, fila)
            if clave == 'g':
                f = '=%s' % PB(gkey)
            elif clave == 'gfr':
                f = '=IFERROR(%s%d/(1-%s),"")' % (col, E_PZ['g'], PB('merma_masa_pct'))
            elif clave == 'pzkg':
                f = '=IFERROR(1000/%s%d,"")' % (col, E_PZ['g'])
            elif clave == 'masa':
                f = '=IFERROR(%s%d/1000*$B$%d,"")' % (col, E_PZ['gfr'], E_COSTE_MASA)
            elif clave == 'aceite':
                f = '=IFERROR(%s%d/1000*%s,"")' % (col, E_PZ['gfr'], ACEITE_EURKG)
            elif clave == 'azucar':
                f = '=IFERROR(%s%d/1000*%s/100*%s,"")' % (col, E_PZ['g'], PB('azucar_g_por_100g_masa'),
                                                         PRECIO('azucar'))
            elif clave == 'total':
                f = '=SUM(%s%d:%s%d)' % (col, E_PZ['masa'], col, E_PZ['azucar'])
            else:
                f = '=IFERROR(%s%d*12,"")' % (col, E_PZ['total'])
            formula(ws, c, f, fmt=fmt, bold=clave == 'total', destacar=clave in ('total', 'docena'))

    # --- 4. de la masa a cada referencia ------------------------------------
    seccion(ws, 'A%d' % E_REF_SEC, '4. De la Masa a Cada Referencia de la Carta')
    encabezados(ws, E_REF_CAB, [
        ('A', 'Id y referencia', None), ('B', 'Familia', None), ('C', 'Piezas de la unidad', None),
        ('D', 'Tipo de pieza', None), ('E', 'Kilos fritos (sólo si se vende al peso)', None),
        ('F', 'Masa vendida (kg)', None), ('G', 'Masa que se fríe, con merma (kg)', None),
        ('H', 'Coste de la masa (EUR)', None), ('I', 'Azúcar (EUR)', None),
        ('J', 'Receta, sin envase (EUR)', None), ('K', 'Envase para llevar (EUR)', None),
        ('L', 'Aceite absorbido (EUR)', None), ('M', 'MATERIA EN SALA, aceite incluido (EUR)', None),
        ('N', 'MATERIA PARA LLEVAR, aceite y envase incluidos (EUR)', None)], alto=58)
    lin_ref = '$A$%d:$A$%d' % (E_LIN_INI, E_LIN_FIN)
    lin_siempre = '$I$%d:$I$%d' % (E_LIN_INI, E_LIN_FIN)
    lin_llevar = '$J$%d:$J$%d' % (E_LIN_INI, E_LIN_FIN)
    coords_tipo = []
    for r in CARTA:
        fila = FILA_ESC[r['id']]
        motor.val(ws, 'A%d' % fila, '%s · %s' % (r['id'], r['nombre']), wrap=True)
        motor.val(ws, 'B%d' % fila, r['familia'])
        c = entrada(ws, 'C%d' % fila, r['piezas'] or 0, fmt=ENT, etiqueta='Piezas de %s' % r['id'])
        motor.dv_numerica(ws, [c.coordinate], minimo=0)
        entrada(ws, 'D%d' % fila, r['tipo_pieza'] or 'sin masa', etiqueta='Tipo de pieza de %s' % r['id'])
        coords_tipo.append('D%d' % fila)
        e = entrada(ws, 'E%d' % fila, r['kg_fritos'] or 0, fmt=DEC3,
                    etiqueta='Kilos fritos de %s' % r['id'])
        motor.dv_numerica(ws, [e.coordinate], minimo=0)
        formula(ws, 'F%d' % fila,
                '=IF(E{f}>0,IFERROR(E{f}/{kf},""),IFERROR(C{f}*IF(D{f}="porra",{gp},'
                'IF(D{f}="churro",{gc},0))/1000,""))'.format(
                    f=fila, kf=PB('kg_fritos_por_kg_masa'), gp=PB('g_masa_porra'),
                    gc=PB('g_masa_churro')), fmt=DEC4)
        formula(ws, 'G%d' % fila, '=IFERROR(F%d/(1-%s),"")' % (fila, PB('merma_masa_pct')), fmt=DEC4)
        formula(ws, 'H%d' % fila, '=IFERROR(G%d*$B$%d,"")' % (fila, E_COSTE_MASA), fmt=EUR4)
        formula(ws, 'I%d' % fila, '=IFERROR(F%d*%s/100*%s,"")'
                % (fila, PB('azucar_g_por_100g_masa'), PRECIO('azucar')), fmt=EUR4)
        formula(ws, 'J%d' % fila, '=SUMIF(%s,"%s",%s)' % (lin_ref, r['id'], lin_siempre), fmt=EUR4)
        formula(ws, 'K%d' % fila, '=SUMIF(%s,"%s",%s)' % (lin_ref, r['id'], lin_llevar), fmt=EUR4)
        formula(ws, 'L%d' % fila, '=IFERROR(G%d*%s,"")' % (fila, ACEITE_EURKG), fmt=EUR4)
        formula(ws, 'M%d' % fila, '=IFERROR(H{f}+I{f}+J{f}+L{f},"")'.format(f=fila), fmt=EUR4,
                bold=True, destacar=True)
        formula(ws, 'N%d' % fila, '=IFERROR(M%d+K%d,"")' % (fila, fila), fmt=EUR4, bold=True,
                destacar=True)
        ws.row_dimensions[fila].height = 26

    # --- 5. receta y envase -------------------------------------------------
    seccion(ws, 'A%d' % E_LIN_SEC, '5. Receta y Envase de Cada Referencia')
    gris(ws, 'F%d' % E_LIN_SEC, 'Una línea por insumo. El envase sólo cuenta cuando la '
                                'referencia se vende para llevar. El chocolate entra por taza '
                                'o media taza, con el coste de la hoja «Chocolate a la Taza».')
    ws.merge_cells('F%d:N%d' % (E_LIN_SEC, E_LIN_SEC))
    encabezados(ws, E_LIN_CAB, [
        ('A', 'Id', None), ('B', 'Referencia', None), ('C', 'Insumo', None),
        ('D', 'Cantidad por unidad vendida', None), ('E', 'Unidad', None),
        ('F', 'Cuándo cuenta', None), ('G', 'Precio SIN IVA por unidad (EUR)', None),
        ('H', 'Importe (EUR)', None), ('I', 'Cuenta siempre (EUR)', None),
        ('J', 'Cuenta sólo para llevar (EUR)', None)], alto=44, congelar=False)
    coords_ins, coords_cuando = [], []
    for i, (rid, rnom, insumo, q, cuando) in enumerate(LINEAS):
        fila = E_LIN_INI + i
        motor.val(ws, 'A%d' % fila, rid)
        motor.val(ws, 'B%d' % fila, rnom, wrap=True)
        entrada(ws, 'C%d' % fila, insumo, etiqueta='Insumo de la línea %d' % (i + 1))
        coords_ins.append('C%d' % fila)
        d = entrada(ws, 'D%d' % fila, q, fmt=DEC3, etiqueta='Cantidad de la línea %d' % (i + 1))
        motor.dv_numerica(ws, [d.coordinate], minimo=0)
        formula(ws, 'E%d' % fila, '=IF(OR(C{f}="{t}",C{f}="{m}"),"ud",IFERROR(INDEX({col},MATCH(C{f},{nom},0)),""))'
                .format(f=fila, t=CHOC_TAZA, m=CHOC_MEDIA, col=COL_INSUMOS('F'), nom=TABLA_NOMBRES))
        entrada(ws, 'F%d' % fila, cuando, etiqueta='Cuándo cuenta la línea %d' % (i + 1))
        coords_cuando.append('F%d' % fila)
        formula(ws, 'G%d' % fila, '=IF(C{f}="{t}",{ct},IF(C{f}="{m}",{cm},IFERROR(INDEX({col},MATCH(C{f},{nom},0)),"")))'
                .format(f=fila, t=CHOC_TAZA, m=CHOC_MEDIA, ct=COSTE_TAZA, cm=COSTE_MEDIA,
                        col=COL_INSUMOS('G'), nom=TABLA_NOMBRES), fmt=EUR4)
        formula(ws, 'H%d' % fila, '=IFERROR(D%d*G%d,"")' % (fila, fila), fmt=EUR4)
        formula(ws, 'I%d' % fila, '=IF(F%d="%s",H%d,0)' % (fila, CUANDO[0], fila), fmt=EUR4)
        formula(ws, 'J%d' % fila, '=IF(F%d="%s",H%d,0)' % (fila, CUANDO[1], fila), fmt=EUR4)
    nombres_insumo = tuple(ins['nombre'] for _k, ins in INSUMOS) + (CHOC_TAZA, CHOC_MEDIA)
    refs, _fin = CC.bloque_listas(ws, E_LISTAS, (('Tipo de pieza', TIPOS_PIEZA),
                                                 ('Cuándo cuenta', CUANDO),
                                                 ('Insumo', nombres_insumo)))
    CC.dv_rango(ws, coords_tipo, refs['Tipo de pieza'], 'Tipo de pieza',
                'Elige churro, porra o «sin masa».')
    CC.dv_rango(ws, coords_cuando, refs['Cuándo cuenta'], 'Cuándo cuenta',
                'Elige «Siempre» o «Sólo para llevar».')
    CC.dv_rango(ws, coords_ins, refs['Insumo'], 'Insumo',
                'Elige un insumo de la tabla de «Parámetros» o una taza de chocolate.')
    version_al_pie(ws, E_LISTAS + len(nombres_insumo) + 4)
    setup(ws, apaisado=True, titulos='%d:%d' % (E_REF_CAB, E_REF_CAB))
    return ws


# ==========================================================================
# Hoja «Absorción de Aceite y Merma»
# ==========================================================================
def hoja_absorcion(wb):
    ws = wb.create_sheet(H_ABS)
    cabecera_hoja(ws, H_ABS, 'El aceite que se lleva la masa frita, en euros. La renovación '
                             'del aceite de la cuba (el descarte) la calcula el libro 4.')
    for letra, ancho in (('A', 56), ('B', 15), ('C', 13), ('D', 15), ('E', 15), ('F', 15),
                         ('G', 40)):
        ws.column_dimensions[letra].width = ancho
    R = A_ROW
    MIXL5 = ABS_(H_MIX, 'L5')
    filas = (
        ('kfr', 'Kilos fritos que salen de un kilo de masa', '=%s' % PB('kg_fritos_por_kg_masa'), DEC, 'kg/kg'),
        ('abs', 'Absorción de aceite, en % del peso frito', '=%s' % PB('absorcion_aceite_pct'), PCT, ''),
        ('kgac', 'Kilos de aceite que se lleva un kilo de masa', '=IFERROR(B%d*B%d,"")' % (R['kfr'], R['abs']), DEC4, 'kg'),
        ('dens', 'Densidad del aceite', '=%s' % PB('densidad_aceite_kg_l'), DEC, 'kg/L'),
        ('lac', 'Litros de aceite que se lleva un kilo de masa', '=IFERROR(B%d/B%d,"")' % (R['kgac'], R['dens']), DEC4, 'L'),
        ('precio', 'Precio del aceite (base imponible)', '=%s' % ABS_(H_PAR, 'L5'), EUR4, 'EUR/L'),
        ('eurkg', 'EUROS DE ACEITE ABSORBIDO POR KILO DE MASA', '=IFERROR(B%d*B%d,"")' % (R['lac'], R['precio']), EUR4, 'EUR/kg'),
        ('merma', 'Merma: masa que se fríe y no se vende', '=%s' % PB('merma_masa_pct'), PCT, ''),
        ('prod', 'Kilos de masa que hay que freír por kilo vendido', '=IFERROR(1/(1-B%d),"")' % R['merma'], DEC4, 'kg/kg'),
        ('coste_merma', 'Coste de la merma por kilo vendido (masa y aceite)',
         '=IFERROR((B%d-1)*(%s+B%d),"")' % (R['prod'], COSTE_MASA, R['eurkg']), EUR4, 'EUR/kg'),
        ('kgrac', 'Kilos de masa que se fríen por ración media (mix de invierno)', '=%s' % MIXL5, DEC4, 'kg/ración'),
        ('acrac', 'ACEITE ABSORBIDO POR RACIÓN MEDIA', '=IFERROR(B%d*B%d,"")' % (R['kgrac'], R['eurkg']), EUR4, 'EUR/ración'),
        ('lrac', 'Litros de aceite absorbido cada 100 raciones', '=IFERROR(B%d*B%d*100,"")' % (R['kgrac'], R['lac']), DEC, 'L'),
        ('peso', 'Peso del aceite absorbido en la materia de la ración media',
         '=IFERROR(B%d/%s,"")' % (R['acrac'], ABS_(H_MIX, 'D%d' % M_RES['materia'])), PCT, ''),
    )
    seccion(ws, 'A4', 'Del Aceite al Euro por Kilo de Masa')
    for clave, etq, f, fmt, uni in filas:
        fila = R[clave]
        motor.val(ws, 'A%d' % fila, etq, bold=clave in ('eurkg', 'acrac'))
        formula(ws, 'B%d' % fila, f, fmt=fmt, bold=clave in ('eurkg', 'acrac'),
                destacar=clave in ('eurkg', 'acrac', 'coste_merma'))
        motor.val(ws, 'C%d' % fila, uni)
    seccion(ws, 'A%d' % (R['merma'] - 1), 'La Merma')
    seccion(ws, 'A%d' % (R['kgrac'] - 1), 'Por Ración Media')
    gris(ws, 'D%d' % R['kgrac'], 'La ración media es la unidad de venta media de la carta, '
                                 'ponderada por el mix de invierno (hoja «Mix y Ticket Canal y '
                                 'Temporada»).', alto=40)
    ws.merge_cells('D%d:G%d' % (R['kgrac'], R['kgrac']))
    gris(ws, 'D%d' % R['acrac'], 'El libro 4 recibe esta cifra para la fila de contraste '
                                 '«aceite absorbido (3) más renovación (4) = aceite total por '
                                 'ración». El 6 suma las dos, cada una con su fuente.', alto=40)
    ws.merge_cells('D%d:G%d' % (R['acrac'], R['acrac']))

    # --- escenarios de absorción -------------------------------------------
    seccion(ws, 'A%d' % (A_ESC_CAB - 1), 'Si la Absorción Fuera Otra (Pon las Tuyas)')
    encabezados(ws, A_ESC_CAB, [
        ('A', 'Absorción de aceite, en % del peso frito', None),
        ('B', 'EUR de aceite por kilo de masa', None),
        ('C', 'EUR de aceite por ración media', None),
        ('D', 'Diferencia por ración frente a tu absorción (EUR)', None),
        ('E', 'Diferencia cada 1.000 raciones (EUR)', None)], alto=44, congelar=False)
    base = D.P('absorcion_aceite_pct')
    for i, fac in enumerate(ESC_FACTORES):
        fila = A_ESC_INI + i
        a = entrada(ws, 'A%d' % fila, round(base * fac, 4), fmt=PCT,
                    etiqueta='Absorción del escenario %d' % (i + 1))
        motor.dv_porcentaje(ws, [a.coordinate])
        formula(ws, 'B%d' % fila, '=IFERROR($B${kf}*A{f}/$B${d}*$B${p},"")'.format(
            kf=R['kfr'], f=fila, d=R['dens'], p=R['precio']), fmt=EUR4)
        formula(ws, 'C%d' % fila, '=IFERROR(B%d*$B$%d,"")' % (fila, R['kgrac']), fmt=EUR4)
        formula(ws, 'D%d' % fila, '=IFERROR(C%d-$B$%d,"")' % (fila, R['acrac']), fmt=EUR4)
        formula(ws, 'E%d' % fila, '=IFERROR(D%d*1000,"")' % fila, fmt=EUR)
        motor.semaforo_isnumber(ws, 'E%d' % fila, '$E$%d' % fila, '>', '0')
    gris(ws, 'A%d' % (A_ESC_FIN + 2), 'La absorción es un supuesto declarado, sin fuente '
                                      'pública: mídela pesando una tanda de masa antes y '
                                      'después de freír. Cambiar de aceite o de freidora la '
                                      'mueve.', alto=36)
    ws.merge_cells('A%d:E%d' % (A_ESC_FIN + 2, A_ESC_FIN + 2))

    bloque_contrato(ws, [(5, 'Aceite absorbido por ración media (mix de invierno), EUR',
                          '=B%d' % R['acrac'], EUR4)])
    version_al_pie(ws, A_ESC_FIN + 4)
    setup(ws, apaisado=True)
    return ws


# ==========================================================================
# Hoja «Chocolate a la Taza»
# ==========================================================================
def hoja_chocolate(wb):
    ws = wb.create_sheet(H_CHO)
    cabecera_hoja(ws, H_CHO, 'Lo que cuesta una taza y qué dice la etiqueta de tu preparado. '
                             'La carta usa la denominación que figura en esa etiqueta.')
    for letra, ancho in (('A', 56), ('B', 18), ('C', 14), ('D', 14), ('E', 14), ('F', 14),
                         ('G', 50)):
        ws.column_dimensions[letra].width = ancho
    R = C_ROW
    prep = D.INSUMOS['preparado_taza']
    seccion(ws, 'A5', '1. Lo que Cuesta el Chocolate')
    motor.val(ws, 'A%d' % R['precio'], 'Precio del preparado SIN IVA (EUR/kg)')
    formula(ws, 'B%d' % R['precio'], '=%s' % PRECIO('preparado_taza'), fmt=EUR4)
    motor.val(ws, 'A%d' % R['kgform'], 'Kilos de preparado del formato que compras')
    formula(ws, 'B%d' % R['kgform'], '=%s' % ABS_(H_PAR, 'E%d' % INS_ROW['preparado_taza']), fmt=DEC3)
    motor.val(ws, 'A%d' % R['rinde'], 'Litros de chocolate que rinde ese formato (lo dice el envase)')
    c = entrada(ws, 'B%d' % R['rinde'], prep['rinde_l_por_formato'], fmt=DEC1,
                etiqueta='Litros que rinde el formato')
    motor.dv_numerica(ws, [c.coordinate], minimo=0)
    nota_fuente(ws, c.coordinate, prep['fuente'])
    motor.val(ws, 'A%d' % R['kgl'], 'Kilos de preparado por litro de chocolate')
    formula(ws, 'B%d' % R['kgl'], '=IFERROR(B%d/B%d,"")' % (R['kgform'], R['rinde']), fmt=DEC4)
    motor.val(ws, 'A%d' % R['cprep'], 'Coste del preparado por litro de chocolate (EUR)')
    formula(ws, 'B%d' % R['cprep'], '=IFERROR(B%d*B%d,"")' % (R['kgl'], R['precio']), fmt=EUR4)
    motor.val(ws, 'A%d' % R['leche'], 'Leche, litro por litro de chocolate (EUR/L)')
    formula(ws, 'B%d' % R['leche'], '=%s' % PRECIO('leche'), fmt=EUR4)
    motor.val(ws, 'A%d' % R['clitro'], 'COSTE DEL CHOCOLATE POR LITRO (EUR)', bold=True)
    formula(ws, 'B%d' % R['clitro'], '=B%d+B%d' % (R['cprep'], R['leche']), fmt=EUR4, bold=True,
            destacar=True)
    for clave, k, etq in (('ml_taza', 'ml_taza', 'Mililitros de una taza'),
                          ('ml_media', 'ml_media_taza', 'Mililitros de media taza')):
        motor.val(ws, 'A%d' % R[clave], etq)
        c = entrada(ws, 'B%d' % R[clave], D.P(k), fmt=ENT, etiqueta=etq)
        motor.dv_numerica(ws, [c.coordinate], minimo=0)
        gris(ws, 'C%d' % R[clave], 'supuesto declarado')
    motor.val(ws, 'A%d' % R['taza'], 'COSTE DE UNA TAZA (EUR)', bold=True)
    formula(ws, 'B%d' % R['taza'], '=IFERROR(B%d/1000*B%d,"")' % (R['ml_taza'], R['clitro']),
            fmt=EUR4, bold=True, destacar=True)
    motor.val(ws, 'A%d' % R['media'], 'Coste de media taza (EUR)')
    formula(ws, 'B%d' % R['media'], '=IFERROR(B%d/1000*B%d,"")' % (R['ml_media'], R['clitro']),
            fmt=EUR4, destacar=True)

    # --- 2. la etiqueta (V-06) --------------------------------------------
    seccion(ws, 'A%d' % (R['denom'] - 1), '2. Qué Dice la Etiqueta de Tu Preparado')
    motor.val(ws, 'A%d' % R['denom'], 'Denominación que figura en la etiqueta del preparado (cópiala tal cual)')
    c = entrada(ws, 'B%d' % R['denom'], 'Chocolate a la taza', etiqueta='Denominación de la etiqueta')
    nota_legal(ws, c.coordinate, 'CHN-05')
    gris(ws, 'C%d' % R['denom'], 'Supuesto del ejemplo: un preparado comercial cuya etiqueta '
                                 'dice «chocolate a la taza». Pon la de TU preparado.', alto=36)
    ws.merge_cells('C%d:G%d' % (R['denom'], R['denom']))
    motor.val(ws, 'A%d' % R['cacao'], 'Cacao seco total que declara la etiqueta')
    c = entrada(ws, 'B%d' % R['cacao'], D.P('cacao_seco_total_preparado_pct') / 100.0, fmt=PCT,
                etiqueta='Cacao seco total del preparado')
    motor.dv_porcentaje(ws, [c.coordinate])
    gris(ws, 'C%d' % R['cacao'], publica('cacao_seco_total_preparado_pct', ''))
    ws.merge_cells('C%d:G%d' % (R['cacao'], R['cacao']))
    motor.val(ws, 'A%d' % R['grasa'], '¿La etiqueta declara grasa vegetal distinta de la manteca de cacao?')
    entrada(ws, 'B%d' % R['grasa'], 'Sí' if D.P('preparado_con_grasa_vegetal') else 'No',
            etiqueta='¿Lleva grasa vegetal?')
    motor.val(ws, 'A%d' % R['minimo'], 'Cacao seco total mínimo del producto «chocolate a la taza»')
    c = entrada(ws, 'B%d' % R['minimo'], D.P('cacao_minimo_chocolate_taza_pct') / 100.0, fmt=PCT,
                etiqueta='Mínimo del chocolate a la taza')
    motor.dv_porcentaje(ws, [c.coordinate])
    nota_legal(ws, c.coordinate, 'CUN-42')
    motor.val(ws, 'A%d' % R['aviso'], 'AVISO ANTES DE IMPRIMIR LA CARTA', bold=True)
    c = formula(ws, 'B%d' % R['aviso'],
                '=IF(NOT(ISNUMBER(B{c})),"",IF(OR(B{c}<B{m},B{g}="Sí"),"Consulta a tu servicio de '
                'consumo antes de imprimir la carta","Sin aviso: la carta usa la denominación de '
                'la etiqueta"))'.format(c=R['cacao'], m=R['minimo'], g=R['grasa']),
                bold=True, destacar=True)
    nota_legal(ws, c.coordinate, 'CUN-V06')
    ws.merge_cells('B%d:G%d' % (R['aviso'], R['aviso']))
    motor.regla_expresion(ws, 'B%d' % R['aviso'], '=LEFT($B$%d,8)="Consulta"' % R['aviso'])
    motor.val(ws, 'A%d' % R['nombre'], 'Nombre con el que la taza va en tu carta')
    formula(ws, 'B%d' % R['nombre'], '=B%d' % R['denom'], destacar=True)
    gris(ws, 'C%d' % R['nombre'], 'Es una interpretación, no una regla del Real Decreto: la carta repite la '
                                  'denominación de la etiqueta y, si hay aviso, lo consultas '
                                  'antes de imprimir. La decisión 6 es qué preparado compras y '
                                  'qué dice su etiqueta.', alto=54)
    ws.merge_cells('C%d:G%d' % (R['nombre'], R['nombre']))

    # --- 3. IVA para llevar -------------------------------------------
    seccion(ws, 'A%d' % (R['iva'] - 1), '3. El IVA de la Taza para Llevar')
    motor.val(ws, 'A%d' % R['iva'], 'IVA que aplicas a la taza para llevar (de «Parámetros»)')
    c = formula(ws, 'B%d' % R['iva'], '=%s' % PB('iva_llevar_chocolate'), fmt=PCT, destacar=True)
    nota_legal(ws, c.coordinate, 'CUN-18')
    gris(ws, 'A%d' % R['aviso_iva'], 'Zona gris: El Molinete aplica el 10 % en celda verde. '
                                     'Consulta a tu asesor: con agua y un preparado azucarado '
                                     'podría ser el 21 %. Se cambia en «Parámetros», en una '
                                     'sola celda.', alto=36)
    ws.merge_cells('A%d:G%d' % (R['aviso_iva'], R['aviso_iva']))

    # --- 4. las tazas de la carta --------------------------------------
    seccion(ws, 'A%d' % (C_TZ_CAB - 1), '4. Las Tazas de la Carta')
    encabezados(ws, C_TZ_CAB, [
        ('A', 'Referencia', None), ('B', 'PVP con IVA (EUR)', None),
        ('C', 'Ingreso medio SIN IVA (EUR)', None), ('D', 'Materia media (EUR)', None),
        ('E', 'Margen por unidad (EUR)', None), ('F', 'Margen sobre materia', None),
        ('G', 'Nota', None)], alto=44, congelar=False)
    for i, r in enumerate(TAZAS):
        fila = C_TZ_INI + i
        fm = FILA_MIX[r['id']]
        motor.val(ws, 'A%d' % fila, '%s · %s' % (r['id'], r['nombre']), wrap=True)
        formula(ws, 'B%d' % fila, '=%s' % ABS_(H_MIX, 'D%d' % fm), fmt=EUR)
        formula(ws, 'C%d' % fila, '=%s' % ABS_(H_MIX, 'O%d' % fm), fmt=EUR4)
        formula(ws, 'D%d' % fila, '=%s' % ABS_(H_MIX, 'R%d' % fm), fmt=EUR4)
        formula(ws, 'E%d' % fila, '=IFERROR(C%d-D%d,"")' % (fila, fila), fmt=EUR4, destacar=True)
        formula(ws, 'F%d' % fila, '=IFERROR(1-D%d/C%d,"")' % (fila, fila), fmt=PCT)
        gris(ws, 'G%d' % fila, publica(None, r['nota']))
        ws.row_dimensions[fila].height = 30
    refs, _fin = CC.bloque_listas(ws, C_LISTAS, (('Sí o no', SI_NO),))
    CC.dv_rango(ws, ['B%d' % R['grasa']], refs['Sí o no'], 'Grasa vegetal',
                'Elige «Sí» o «No», según la etiqueta.')
    version_al_pie(ws, C_LISTAS + 5)
    setup(ws, apaisado=True)
    return ws


# ==========================================================================
# Hoja «Coste Hora»
# ==========================================================================
def hoja_coste_hora(wb):
    ws = wb.create_sheet(H_CH)
    cabecera_hoja(ws, H_CH, 'El coste de empresa de una hora de tu plantilla y la mano de obra '
                            'que lleva cada ración. La plantilla y el convenio viven en el '
                            'libro 8.')
    for letra, ancho in (('A', 56), ('B', 15), ('C', 13), ('D', 70)):
        ws.column_dimensions[letra].width = ancho
    R = H_ROW
    seccion(ws, 'A4', 'La Hora y la Ración')
    motor.val(ws, 'A%d' % R['chora'], 'COSTE HORA DE MANO DE OBRA (coste de empresa por hora '
                                      'contratada)', bold=True, wrap=True)
    c = entrada(ws, 'B%d' % R['chora'], D.coste_hora_mano_obra(), fmt=EUR,
                etiqueta='Coste hora de mano de obra')
    motor.dv_numerica(ws, [c.coordinate], minimo=0)
    motor.val(ws, 'C%d' % R['chora'], 'EUR/h')
    gris(ws, 'D%d' % R['chora'],
         'Supuesto calculado con la plantilla de El Molinete (titular, dos churreros, un '
         'camarero y el medio refuerzo; convenio de ejemplo con tablas de 2025, suelo del SMI '
         '2026 y Seguridad Social de empresa). Este libro va antes que el 8 y lo SUPONE: '
         'cuando rellenes el 8, su fila de CUADRE compara este número con el de tu plantilla.',
         alto=66)
    motor.val(ws, 'A%d' % R['minut'], 'Minutos de mano de obra por ración', wrap=True)
    c = entrada(ws, 'B%d' % R['minut'], D.minutos_mano_obra_por_racion(), fmt=DEC,
                etiqueta='Minutos de mano de obra por ración')
    motor.dv_numerica(ws, [c.coordinate], minimo=0)
    motor.val(ws, 'C%d' % R['minut'], 'min/ración')
    gris(ws, 'D%d' % R['minut'],
         'Supuesto calculado: las horas contratadas de la plantilla al año, por 60, entre las '
         'raciones del año de El Molinete. Con tus números: horas de tu plantilla (libro 8) '
         'por 60 entre tus raciones del año (libro 5).', alto=44)
    filas = (
        ('rach', 'Raciones por hora de mano de obra', '=IFERROR(60/B%d,"")' % R['minut'], DEC1,
         'raciones/h'),
        ('morac', 'COSTE DE MANO DE OBRA POR RACIÓN', '=IFERROR(B%d*B%d/60,"")' % (R['chora'], R['minut']),
         EUR4, 'EUR/ración'),
        ('ticket', 'Ticket SIN IVA por ración (mix de invierno)',
         '=%s' % ABS_(H_MIX, 'D%d' % M_RES['ticket']), EUR4, 'EUR/ración'),
        ('peso', 'Peso de la mano de obra sobre el ticket', '=IFERROR(B%d/B%d,"")' % (R['morac'], R['ticket']),
         PCT, ''),
    )
    for clave, etq, f, fmt, uni in filas:
        motor.val(ws, 'A%d' % R[clave], etq, bold=clave == 'morac')
        formula(ws, 'B%d' % R[clave], f, fmt=fmt, bold=clave == 'morac',
                destacar=clave in ('morac', 'peso'))
        motor.val(ws, 'C%d' % R[clave], uni)
    seccion(ws, 'A%d' % (R['mopz'] - 1), 'Lo que Vale un Minuto')
    motor.val(ws, 'A%d' % R['mopz'], 'Coste de un minuto de mano de obra (EUR)')
    formula(ws, 'B%d' % R['mopz'], '=IFERROR(B%d/60,"")' % R['chora'], fmt=EUR4)
    motor.val(ws, 'A%d' % R['mokg'], 'Mano de obra cada 100 raciones (EUR)')
    formula(ws, 'B%d' % R['mokg'], '=IFERROR(B%d*100,"")' % R['morac'], fmt=EUR, destacar=True)
    gris(ws, 'A%d' % (R['mokg'] + 2),
         'Por qué está aquí: el margen de la carta no paga sólo la materia. «Los Dos Márgenes» '
         'resta este coste para que veas el margen que te queda tras aceite y mano de obra. El '
         'libro 5 lo usa para valorar las horas de refuerzo, y el 8 lo cuadra con tu plantilla.',
         alto=44)
    ws.merge_cells('A%d:D%d' % (R['mokg'] + 2, R['mokg'] + 2))
    bloque_contrato(ws, [(5, 'Coste hora de mano de obra, EUR/h', '=B%d' % R['chora'], EUR)])
    version_al_pie(ws, R['mokg'] + 4)
    setup(ws, apaisado=True)
    return ws


# ==========================================================================
# Hoja «Mix y Ticket Canal y Temporada»
# ==========================================================================
def hoja_mix(wb):
    ws = wb.create_sheet(H_MIX)
    cabecera_hoja(ws, H_MIX, 'El PVP con IVA de cada referencia, la parte que se vende para '
                             'llevar y dos mixes: invierno (septiembre a junio) y verano '
                             '(julio y agosto). Cada mix suma 100.')
    anchos = {'A': 34, 'B': 13, 'C': 13, 'D': 13, 'E': 13, 'F': 13, 'G': 13, 'H': 22,
              'I': 10, 'J': 10, 'K': 13, 'L': 13, 'M': 11, 'N': 13, 'O': 13, 'P': 13, 'Q': 13,
              'R': 13, 'S': 11, 'T': 11, 'U': 11, 'V': 11, 'W': 11, 'X': 11, 'Y': 12, 'Z': 22}
    for letra, ancho in anchos.items():
        ws.column_dimensions[letra].width = ancho

    # --- tabla por referencia (filas 16-41) -----------------------------
    encabezados(ws, M_CAB, [
        ('A', 'Id y referencia', None), ('B', 'Familia', None), ('C', 'Año del precio', None),
        ('D', 'PVP con IVA (EUR)', None), ('E', 'Fuente del precio', None),
        ('F', 'Parte que se vende para llevar', None),
        ('G', '¿Vaso cobrado aparte al llevar?', None),
        ('H', 'IVA para llevar: categoría', None), ('I', 'IVA en sala', None),
        ('J', 'IVA para llevar', None), ('K', 'PVP SIN IVA en sala (EUR)', None),
        ('L', 'PVP SIN IVA para llevar (EUR)', None), ('M', 'Vaso SIN IVA (EUR)', None),
        ('N', 'Ingreso SIN IVA para llevar (EUR)', None), ('O', 'Ingreso medio SIN IVA (EUR)', None),
        ('P', 'Materia en sala (EUR)', None), ('Q', 'Materia para llevar (EUR)', None),
        ('R', 'Materia media (EUR)', None), ('S', 'Mix de invierno (%)', None),
        ('T', 'Mix de julio y agosto (%)', None), ('U', 'Peso sala invierno', None),
        ('V', 'Peso llevar invierno', None), ('W', 'Peso sala verano', None),
        ('X', 'Peso llevar verano', None), ('Y', 'Masa que se fríe (kg)', None),
        ('Z', 'Alérgenos de la receta del ejemplo', None)], alto=62, congelar=False)
    nota_legal(ws, 'Z%d' % M_CAB, 'CHN-34')
    coords_vaso = []
    for r in CARTA:
        fila = FILA_MIX[r['id']]
        fe = FILA_ESC[r['id']]
        motor.val(ws, 'A%d' % fila, '%s · %s' % (r['id'], r['nombre']), wrap=True)
        motor.val(ws, 'B%d' % fila, r['familia'], wrap=True)
        entrada(ws, 'C%d' % fila, r['anio_pvp'], fmt='0', etiqueta='Año del precio de %s' % r['id'])
        d = entrada(ws, 'D%d' % fila, r['pvp'], fmt=EUR, etiqueta='PVP de %s' % r['id'])
        motor.dv_numerica(ws, [d.coordinate], minimo=0)
        nota_fuente(ws, d.coordinate, r['fuente_pvp'])
        entrada(ws, 'E%d' % fila, texto_fuente(r['fuente_pvp']), etiqueta='Fuente del PVP de %s' % r['id'])
        f = entrada(ws, 'F%d' % fila, r['pct_llevar'], fmt=PCT, etiqueta='Parte para llevar de %s' % r['id'])
        motor.dv_porcentaje(ws, [f.coordinate])
        entrada(ws, 'G%d' % fila, 'Sí' if r['cargo_vaso'] else 'No',
                etiqueta='¿Vaso aparte? %s' % r['id'])
        coords_vaso.append('G%d' % fila)
        motor.val(ws, 'H%d' % fila, CATEGORIA_IVA[r['iva_llevar']], wrap=True)
        formula(ws, 'I%d' % fila, '=%s' % PB('iva_sala'), fmt=PCT)
        formula(ws, 'J%d' % fila, '=%s' % PB(r['iva_llevar']), fmt=PCT)
        formula(ws, 'K%d' % fila, '=IFERROR(D%d/(1+I%d),"")' % (fila, fila), fmt=EUR4)
        formula(ws, 'L%d' % fila, '=IFERROR(D%d/(1+J%d),"")' % (fila, fila), fmt=EUR4)
        formula(ws, 'M%d' % fila, '=IF(G{f}="Sí",IFERROR({v}/(1+{iv}),""),0)'.format(
            f=fila, v=ABS_(H_PAR, 'B%d' % P_VASO), iv=PB(D.CARGO_VASO['iva'])), fmt=EUR4)
        formula(ws, 'N%d' % fila, '=IFERROR(L%d+M%d,"")' % (fila, fila), fmt=EUR4)
        formula(ws, 'O%d' % fila, '=IFERROR((1-F{f})*K{f}+F{f}*N{f},"")'.format(f=fila), fmt=EUR4,
                destacar=True)
        formula(ws, 'P%d' % fila, '=%s' % ABS_(H_ESC, 'M%d' % fe), fmt=EUR4)
        formula(ws, 'Q%d' % fila, '=%s' % ABS_(H_ESC, 'N%d' % fe), fmt=EUR4)
        formula(ws, 'R%d' % fila, '=IFERROR((1-F{f})*P{f}+F{f}*Q{f},"")'.format(f=fila), fmt=EUR4,
                destacar=True)
        s = entrada(ws, 'S%d' % fila, r['mix_invierno'], fmt=DEC1, etiqueta='Mix de invierno de %s' % r['id'])
        t = entrada(ws, 'T%d' % fila, r['mix_verano'], fmt=DEC1, etiqueta='Mix de verano de %s' % r['id'])
        motor.dv_numerica(ws, [s.coordinate, t.coordinate], minimo=0, maximo=100)
        formula(ws, 'U%d' % fila, '=IFERROR(S{f}*(1-F{f}),"")'.format(f=fila), fmt=DEC3)
        formula(ws, 'V%d' % fila, '=IFERROR(S{f}*F{f},"")'.format(f=fila), fmt=DEC3)
        formula(ws, 'W%d' % fila, '=IFERROR(T{f}*(1-F{f}),"")'.format(f=fila), fmt=DEC3)
        formula(ws, 'X%d' % fila, '=IFERROR(T{f}*F{f},"")'.format(f=fila), fmt=DEC3)
        formula(ws, 'Y%d' % fila, '=%s' % ABS_(H_ESC, 'G%d' % fe), fmt=DEC4)
        motor.val(ws, 'Z%d' % fila, ', '.join(r['alergenos']) or 'ninguno en la receta del ejemplo',
                  wrap=True)
        ws.row_dimensions[fila].height = 28
    motor.val(ws, 'A%d' % M_TOT, 'TOTAL', bold=True)
    for col in ('S', 'T', 'U', 'V', 'W', 'X'):
        formula(ws, '%s%d' % (col, M_TOT), '=SUM(%s%d:%s%d)' % (col, M_INI, col, M_FIN),
                fmt=DEC1, bold=True)
    motor.val(ws, 'A%d' % (M_TOT + 1), 'Vaso para llevar cobrado aparte (fila propia del ticket): '
                                       'el importe está en «Parámetros» y se suma al ingreso de '
                                       'cada bebida que lo lleva.', wrap=True)
    ws['A%d' % (M_TOT + 1)].font = Font(size=8, color=GRIS)
    ws.merge_cells('A%d:N%d' % (M_TOT + 1, M_TOT + 1))
    ws.row_dimensions[M_TOT + 1].height = 26

    # --- resumen por canal y temporada (filas 4-12) ------------------------
    seccion(ws, 'A4', 'Ticket y Materia por Canal y Temporada')
    encabezados(ws, M_RES_CAB, [
        ('A', 'Por ración', None), ('B', 'Invierno · sala', None),
        ('C', 'Invierno · para llevar', None), ('D', 'Invierno · total', None),
        ('E', 'Verano · sala', None), ('F', 'Verano · para llevar', None),
        ('G', 'Verano · total', None)], alto=36, congelar=False)
    rng = lambda col: '%s%d:%s%d' % (col, M_INI, col, M_FIN)   # noqa: E731
    peso = {('invierno', 'sala'): 'U', ('invierno', 'llevar'): 'V', ('invierno', 'total'): 'S',
            ('verano', 'sala'): 'W', ('verano', 'llevar'): 'X', ('verano', 'total'): 'T'}
    ingreso = {'sala': 'K', 'llevar': 'N', 'total': 'O'}
    materia = {'sala': 'P', 'llevar': 'Q', 'total': 'R'}
    etiquetas = {'ticket': 'Ticket SIN IVA por ración (EUR)',
                 'materia': 'Coste de materia por ración, aceite absorbido incluido (EUR)',
                 'margen_eur': 'Margen sobre materia por ración (EUR)',
                 'margen_pct': 'Margen sobre materia (%)',
                 'pct': 'Parte de las raciones del canal',
                 'kg': 'Kilos de masa que se fríen por ración media'}
    for clave, etq in etiquetas.items():
        motor.val(ws, 'A%d' % M_RES[clave], etq, wrap=True)
        ws.row_dimensions[M_RES[clave]].height = 28
    for col, temp, canal in M_COLS:
        w = peso[(temp, canal)]
        wt = peso[(temp, 'total')]
        tot = '%s$%d' % (w, M_TOT)
        formula(ws, '%s%d' % (col, M_RES['ticket']),
                '=IFERROR(SUMPRODUCT(%s,%s)/%s,"")' % (rng(w), rng(ingreso[canal]), tot),
                fmt=EUR4, bold=True, destacar=True)
        formula(ws, '%s%d' % (col, M_RES['materia']),
                '=IFERROR(SUMPRODUCT(%s,%s)/%s,"")' % (rng(w), rng(materia[canal]), tot),
                fmt=EUR4, bold=True, destacar=True)
        formula(ws, '%s%d' % (col, M_RES['margen_eur']),
                '=IFERROR(%s%d-%s%d,"")' % (col, M_RES['ticket'], col, M_RES['materia']), fmt=EUR4)
        formula(ws, '%s%d' % (col, M_RES['margen_pct']),
                '=IFERROR(1-%s%d/%s%d,"")' % (col, M_RES['materia'], col, M_RES['ticket']), fmt=PCT)
        formula(ws, '%s%d' % (col, M_RES['pct']),
                '=IFERROR(%s/%s$%d,"")' % (tot, wt, M_TOT), fmt=PCT)
        formula(ws, '%s%d' % (col, M_RES['kg']),
                '=IFERROR(SUMPRODUCT(%s,%s)/%s,"")' % (rng(w), rng('Y'), tot), fmt=DEC4)
    motor.val(ws, 'A%d' % M_RES['cuadre'], 'Comprobación: cada mix suma 100', bold=True)
    c = formula(ws, 'B%d' % M_RES['cuadre'],
                '=IF(OR(NOT(ISNUMBER(S{t})),NOT(ISNUMBER(T{t}))),"",IF(AND(ROUND(S{t},6)=100,'
                'ROUND(T{t},6)=100),"CUADRAN los dos mixes","REVISA: algún mix no suma 100"))'
                .format(t=M_TOT), bold=True)
    ws.merge_cells('B%d:G%d' % (M_RES['cuadre'], M_RES['cuadre']))
    motor.regla_expresion(ws, 'B%d' % M_RES['cuadre'], '=LEFT($B$%d,6)="REVISA"' % M_RES['cuadre'])
    gris(ws, 'A%d' % (M_RES['cuadre'] + 1),
         'El ticket incluye, al llevar, el vaso cobrado aparte. La materia incluye el aceite '
         'absorbido y, al llevar, el envase. Las franjas del día no están aquí: viven en el '
         'libro 5.', alto=30)
    ws.merge_cells('A%d:G%d' % (M_RES['cuadre'] + 1, M_RES['cuadre'] + 1))

    # --- el CONTRATO (X1, X2 bis, X5, X11) -------------------------------
    bloque_contrato(ws, [
        (5, 'Kilos de masa por ración media (mix de invierno, merma incluida)',
         '=D%d' % M_RES['kg'], DEC4),
        (6, 'Ticket SIN IVA por ración en verano (carta de verano), EUR', '=G%d' % M_RES['ticket'], EUR4),
        (7, 'Coste de materia por ración en verano, aceite absorbido incluido, EUR',
         '=G%d' % M_RES['materia'], EUR4),
        (8, 'Coste de materia por ración para llevar (invierno), aceite absorbido incluido, EUR',
         '=C%d' % M_RES['materia'], EUR4),
        (9, 'Coste de materia por ración en sala (invierno), aceite absorbido incluido, EUR',
         '=B%d' % M_RES['materia'], EUR4),
        (10, 'Ticket SIN IVA por ración en sala (invierno), EUR', '=B%d' % M_RES['ticket'], EUR4),
        (11, 'Ticket SIN IVA por ración para llevar (invierno), EUR', '=C%d' % M_RES['ticket'], EUR4),
        (12, 'Raciones en sala, en fracción (0,70 = 70 %; el resto, para llevar)',
         '=B%d' % M_RES['pct'], '0.0%'),
    ])
    refs, _fin = CC.bloque_listas(ws, M_LISTAS, (('Sí o no', SI_NO),))
    CC.dv_rango(ws, coords_vaso, refs['Sí o no'], 'Vaso aparte',
                'Elige «Sí» si al llevar el vaso de plástico se cobra aparte, o «No».')
    version_al_pie(ws, M_LISTAS + 5)
    ws.freeze_panes = 'B%d' % (M_CAB + 1)
    setup(ws, apaisado=True, titulos='%d:%d' % (M_CAB, M_CAB))
    return ws


# ==========================================================================
# Hoja «Ración, Docena o Kilo»
# ==========================================================================
def hoja_racion(wb):
    ws = wb.create_sheet(H_RDK)
    cabecera_hoja(ws, H_RDK, 'Los formatos de churro y porra, comparados por los euros SIN IVA '
                             'que deja cada kilo de masa que fríes (decisión 7).')
    encabezados(ws, R_CAB, [
        ('A', 'Formato', 40), ('B', 'Piezas', 9), ('C', 'PVP con IVA (EUR)', 12),
        ('D', 'Precio por pieza con IVA (EUR)', 13), ('E', 'Canal que manda', 13),
        ('F', 'Ingreso SIN IVA (EUR)', 13), ('G', 'Materia, aceite incluido (EUR)', 13),
        ('H', 'Margen por unidad (EUR)', 13), ('I', 'Masa que se fríe (kg)', 12),
        ('J', 'EUR QUE DEJA CADA KG DE MASA', 15), ('K', 'Año y fuente del precio', 26)], alto=52)
    for i, r in enumerate(CHURROS):
        fila = R_INI + i
        fm = FILA_MIX[r['id']]
        fe = FILA_ESC[r['id']]
        motor.val(ws, 'A%d' % fila, '%s · %s' % (r['id'], r['nombre']), wrap=True)
        formula(ws, 'B%d' % fila, '=%s' % ABS_(H_ESC, 'C%d' % fe), fmt=ENT)
        formula(ws, 'C%d' % fila, '=%s' % ABS_(H_MIX, 'D%d' % fm), fmt=EUR)
        formula(ws, 'D%d' % fila, '=IF(B{f}>0,IFERROR(C{f}/B{f},""),"")'.format(f=fila), fmt=EUR4)
        pl = ABS_(H_MIX, 'F%d' % fm)
        formula(ws, 'E%d' % fila, '=IF(%s>=1-%s,"Para llevar","Sala")' % (pl, pl))
        formula(ws, 'F%d' % fila, '=IF(E%d="Para llevar",%s,%s)'
                % (fila, ABS_(H_MIX, 'N%d' % fm), ABS_(H_MIX, 'K%d' % fm)), fmt=EUR4)
        formula(ws, 'G%d' % fila, '=IF(E%d="Para llevar",%s,%s)'
                % (fila, ABS_(H_ESC, 'N%d' % fe), ABS_(H_ESC, 'M%d' % fe)), fmt=EUR4)
        formula(ws, 'H%d' % fila, '=IFERROR(F%d-G%d,"")' % (fila, fila), fmt=EUR4)
        formula(ws, 'I%d' % fila, '=%s' % ABS_(H_ESC, 'G%d' % fe), fmt=DEC4)
        formula(ws, 'J%d' % fila, '=IFERROR(H%d/I%d,"")' % (fila, fila), fmt=EUR, bold=True,
                destacar=True)
        formula(ws, 'K%d' % fila, '=%s&" · "&%s' % (ABS_(H_MIX, 'C%d' % fm), ABS_(H_MIX, 'E%d' % fm)))
        ws.row_dimensions[fila].height = 28
    rngj = 'J%d:J%d' % (R_INI, R_FIN)
    rnga = 'A%d:A%d' % (R_INI, R_FIN)
    res = (
        ('El formato que más deja por kilo de masa', '=IFERROR(INDEX(%s,MATCH(MAX(%s),%s,0)),"")' % (rnga, rngj, rngj), None),
        ('Lo que deja ese formato por kilo de masa (EUR)', '=MAX(%s)' % rngj, EUR),
        ('El formato que menos deja por kilo de masa', '=IFERROR(INDEX(%s,MATCH(MIN(%s),%s,0)),"")' % (rnga, rngj, rngj), None),
        ('Lo que deja ese formato por kilo de masa (EUR)', '=MIN(%s)' % rngj, EUR),
        ('Ración de churros frente al kilo: EUR más por kilo de masa',
         '=IFERROR(J%d-J%d,"")' % (R_INI + CHURROS.index(D.ref('CH1')), R_INI + CHURROS.index(D.ref('CH7'))), EUR),
    )
    seccion(ws, 'A%d' % (R_RES - 1), 'Lo que Dice la Comparación')
    for i, (etq, f, fmt) in enumerate(res):
        fila = R_RES + i
        motor.val(ws, 'A%d' % fila, etq, wrap=True)
        formula(ws, 'B%d' % fila, f, fmt=fmt, bold=True, destacar=True)
        ws.merge_cells('B%d:E%d' % (fila, fila))
    gris(ws, 'A%d' % (R_RES + len(res) + 1),
         'El kilo es el formato con menos euros por kilo de masa porque se vende por peso '
         'frito, al precio más bajo por pieza. No es un error que lo tengas: es el que trae el '
         'pedido grande del domingo. Lo que esta hoja te dice es cuánto cuesta cada formato en '
         'masa, en aceite y en freidora, para que el precio de cada uno sea una decisión. El '
         'canal que manda es el de la mayor parte de sus ventas (hoja «Mix y Ticket Canal y '
         'Temporada»).', alto=66)
    ws.merge_cells('A%d:K%d' % (R_RES + len(res) + 1, R_RES + len(res) + 1))
    version_al_pie(ws, R_RES + len(res) + 3)
    setup(ws, apaisado=True, titulos='%d:%d' % (R_CAB, R_CAB))
    return ws


# ==========================================================================
# Hoja «Los Dos Márgenes»
# ==========================================================================
def hoja_dos_margenes(wb):
    ws = wb.create_sheet(H_DOS)
    cabecera_hoja(ws, H_DOS, 'Dos márgenes que no son la misma cosa, al lado de las dos cifras '
                             'publicadas con las que se suelen comparar. Cada cifra, con su '
                             'definición pegada.')
    for letra, ancho in (('A', 52), ('B', 15), ('C', 15), ('D', 80)):
        ws.column_dimensions[letra].width = ancho
    mix = lambda col, clave: ABS_(H_MIX, '%s%d' % (col, M_RES[clave]))   # noqa: E731
    seccion(ws, 'A4', 'Tus Dos Márgenes (Salen de Tu Escandallo)')
    encabezados(ws, DM['cab'], [('A', 'Margen', None), ('B', 'Invierno', None),
                                ('C', 'Julio y agosto', None), ('D', 'Definición', None)],
                alto=24, congelar=False)
    motor.val(ws, 'A%d' % DM['m1'], '1. Margen sobre materia prima', bold=True)
    formula(ws, 'B%d' % DM['m1'], '=%s' % mix('D', 'margen_pct'), fmt=PCT, bold=True, destacar=True)
    formula(ws, 'C%d' % DM['m1'], '=%s' % mix('G', 'margen_pct'), fmt=PCT, bold=True, destacar=True)
    gris(ws, 'D%d' % DM['m1'], '1 menos (materia prima más aceite absorbido) entre el ticket SIN '
                               'IVA, con el mix de la temporada. Es el comparable al «más del '
                               '60 % en producto». Es el que usa el plan financiero (libro 6).',
         alto=40)
    motor.val(ws, 'A%d' % DM['m2'], '2. Margen tras aceite y mano de obra', bold=True)
    formula(ws, 'B%d' % DM['m2'], '=IFERROR(1-(%s+%s)/%s,"")'
            % (mix('D', 'materia'), MO_RACION, mix('D', 'ticket')), fmt=PCT, bold=True, destacar=True)
    formula(ws, 'C%d' % DM['m2'], '=IFERROR(1-(%s+%s)/%s,"")'
            % (mix('G', 'materia'), MO_RACION, mix('G', 'ticket')), fmt=PCT, bold=True, destacar=True)
    gris(ws, 'D%d' % DM['m2'], '1 menos (materia, aceite absorbido y mano de obra por ración, '
                               'de la hoja «Coste Hora») entre el ticket SIN IVA. Sin renta, '
                               'suministros ni amortización: no es la rentabilidad del negocio, '
                               'que sale del libro 6.', alto=40)
    motor.val(ws, 'A%d' % DM['e1'], 'Margen 1 en euros por ración')
    formula(ws, 'B%d' % DM['e1'], '=%s' % mix('D', 'margen_eur'), fmt=EUR4)
    formula(ws, 'C%d' % DM['e1'], '=%s' % mix('G', 'margen_eur'), fmt=EUR4)
    motor.val(ws, 'A%d' % DM['e2'], 'Margen 2 en euros por ración')
    formula(ws, 'B%d' % DM['e2'], '=IFERROR(%s-%s-%s,"")' % (mix('D', 'ticket'), mix('D', 'materia'), MO_RACION), fmt=EUR4)
    formula(ws, 'C%d' % DM['e2'], '=IFERROR(%s-%s-%s,"")' % (mix('G', 'ticket'), mix('G', 'materia'), MO_RACION), fmt=EUR4)

    seccion(ws, 'A%d' % (DM['ref_cab'] - 1), 'Con Qué se Suelen Comparar (Cada Una con Su Definición)')
    encabezados(ws, DM['ref_cab'], [('A', 'Quién lo publica', None), ('B', 'Cifra (como número)', None),
                                    ('C', 'Fuente', None), ('D', 'Qué mide de verdad', None)],
                alto=24, congelar=False)
    publicadas = {m['fuente']: m for m in D.MARGENES_DE_CONTRASTE}
    for fila, pid, valor in ((DM['loomis'], 'CUS-01', 0.60), (DM['artesana'], 'CUS-30', 0.50)):
        m = publicadas[pid]
        motor.val(ws, 'A%d' % fila, m['quien'], wrap=True)
        c = entrada(ws, 'B%d' % fila, valor, fmt=PCT, etiqueta='Cifra publicada %s' % pid)
        motor.dv_porcentaje(ws, [c.coordinate])
        nota_fuente(ws, c.coordinate, pid)
        motor.val(ws, 'C%d' % fila, pid)
        gris(ws, 'D%d' % fila, 'Dice: %s. Qué mide: %s.' % (m['cifra'], m['definicion']), alto=34)
    gris(ws, 'A%d' % (DM['artesana'] + 1),
         'Fiabilidad baja la del «un poquito más del 50 %»: lo dice de palabra el gestor de La '
         'Artesana en una entrevista, sin método. Ninguna de las dos cifras entra en el plan '
         'financiero.', alto=30)
    ws.merge_cells('A%d:D%d' % (DM['artesana'] + 1, DM['artesana'] + 1))

    seccion(ws, 'A%d' % (DM['cmp_cab'] - 1), 'La Comparación, en Invierno')
    filas = (
        ('c1', 'Tu margen 1 frente a «más del 60 % en producto»',
         '=IF(NOT(ISNUMBER(B{m})),"",IF(B{m}>B{r},"Por encima: tu carta deja más sobre materia '
         'que esa referencia","Por debajo: revisa precios o mermas antes de abrir"))'.format(
             m=DM['m1'], r=DM['loomis'])),
        ('c2', 'Tu margen 2 frente al «un poquito más del 50 %»',
         '=IF(NOT(ISNUMBER(B{m})),"",IF(B{m}>B{r},"Por encima, con cautela: aquella cifra es '
         'rentabilidad declarada, no este margen","Por debajo, con cautela: aquella cifra es '
         'rentabilidad declarada, no este margen"))'.format(m=DM['m2'], r=DM['artesana'])),
        ('d1', 'Puntos de diferencia del margen 1', '=IFERROR(B%d-B%d,"")' % (DM['m1'], DM['loomis'])),
        ('d2', 'Puntos de diferencia del margen 2', '=IFERROR(B%d-B%d,"")' % (DM['m2'], DM['artesana'])),
    )
    for clave, etq, f in filas:
        fila = DM[clave]
        motor.val(ws, 'A%d' % fila, etq, wrap=True)
        fmt = PCT if clave.startswith('d') else None
        formula(ws, 'B%d' % fila, f, fmt=fmt, bold=True, destacar=True)
        if clave.startswith('c'):
            ws.merge_cells('B%d:D%d' % (fila, fila))
        else:
            motor.semaforo_isnumber(ws, 'B%d' % fila, '$B$%d' % fila, '<', '0')
        ws.row_dimensions[fila].height = 28
    gris(ws, 'A%d' % (DM['d2'] + 2),
         'Por qué dos márgenes: el primero dice si el PRECIO cubre la materia; el segundo, si '
         'además cubre las manos que la fríen. Un margen sobre materia muy alto es normal en '
         'una churrería, porque la masa es barata: lo caro es la madrugada. Por eso el plan '
         'financiero toma el margen 1 de tu escandallo y resta la nómina aparte.', alto=54)
    ws.merge_cells('A%d:D%d' % (DM['d2'] + 2, DM['d2'] + 2))
    version_al_pie(ws, DM['d2'] + 4)
    setup(ws, apaisado=True)
    return ws


# ==========================================================================
# Hoja «Decisión de Surtido»
# ==========================================================================
def hoja_surtido(wb):
    ws = wb.create_sheet(H_SUR)
    cabecera_hoja(ws, H_SUR, 'Margen en EUROS por unidad contra rotación. Los dos umbrales '
                             'están en «Parámetros» y son criterio de la casa.')
    encabezados(ws, S_CAB, [
        ('A', 'Id y referencia', 38), ('B', 'Familia', 18), ('C', 'Ingreso medio SIN IVA (EUR)', 12),
        ('D', 'Materia media (EUR)', 12), ('E', 'Margen por unidad (EUR)', 12),
        ('F', 'Margen sobre ingreso', 11), ('G', 'Mix de invierno (%)', 10),
        ('H', 'Mix de julio y agosto (%)', 10),
        ('I', 'Margen cada 100 raciones de invierno (EUR)', 13),
        ('J', '¿Margen por encima del umbral?', 11), ('K', '¿Rotación por encima del umbral?', 11),
        ('L', 'Veredicto', 16), ('M', 'Qué hacer', 56)], alto=60)
    umb_m = ABS_(H_PAR, 'B%d' % P_UMB_MARGEN)
    umb_r = ABS_(H_PAR, 'B%d' % P_UMB_ROT)
    for i, r in enumerate(CARTA):
        fila = S_INI + i
        fm = FILA_MIX[r['id']]
        motor.val(ws, 'A%d' % fila, '%s · %s' % (r['id'], r['nombre']), wrap=True)
        motor.val(ws, 'B%d' % fila, r['familia'], wrap=True)
        formula(ws, 'C%d' % fila, '=%s' % ABS_(H_MIX, 'O%d' % fm), fmt=EUR4)
        formula(ws, 'D%d' % fila, '=%s' % ABS_(H_MIX, 'R%d' % fm), fmt=EUR4)
        formula(ws, 'E%d' % fila, '=IFERROR(C%d-D%d,"")' % (fila, fila), fmt=EUR4, destacar=True)
        formula(ws, 'F%d' % fila, '=IFERROR(E%d/C%d,"")' % (fila, fila), fmt=PCT)
        formula(ws, 'G%d' % fila, '=%s' % ABS_(H_MIX, 'S%d' % fm), fmt=DEC1)
        formula(ws, 'H%d' % fila, '=%s' % ABS_(H_MIX, 'T%d' % fm), fmt=DEC1)
        formula(ws, 'I%d' % fila, '=IFERROR(E%d*G%d,"")' % (fila, fila), fmt=EUR)
        formula(ws, 'J%d' % fila, '=IF(NOT(ISNUMBER(E{f})),"",IF(E{f}>={u},"Sí","No"))'.format(f=fila, u=umb_m))
        formula(ws, 'K%d' % fila, '=IF(MAX(G{f},H{f})>={u},"Sí","No")'.format(f=fila, u=umb_r))
        formula(ws, 'L%d' % fila,
                '=IF(OR(J{f}="",K{f}=""),"",IF(AND(J{f}="Sí",K{f}="Sí"),"{v0}",IF(AND(J{f}="No",'
                'K{f}="Sí"),"{v1}",IF(J{f}="Sí","{v2}","{v3}"))))'.format(
                    f=fila, v0=VEREDICTOS[0], v1=VEREDICTOS[1], v2=VEREDICTOS[2], v3=VEREDICTOS[3]),
                bold=True)
        if r['familia'] == 'Carta de verano':
            txt = ('Sólo se vende en julio y agosto: léela con el mix de verano, no con el de '
                   'invierno. Es la decisión 9 (libro 5).')
        elif r['id'] in ('CH4', 'CH5'):
            txt = ('La pieza suelta deja poco por unidad y mucho por kilo de masa: mira la hoja '
                   '«Ración, Docena o Kilo» antes de tocarle el precio.')
        else:
            txt = ('Si sale «Revisar precio», mira primero el PVP y el canal en «Mix y Ticket '
                   'Canal y Temporada»; si sale «Vigilar rotación», cuánto stock y cuánta carta '
                   'ocupa.')
        gris(ws, 'M%d' % fila, txt)
        ws.row_dimensions[fila].height = 30
    motor.val(ws, 'A%d' % S_TOT, 'TOTAL', bold=True)
    formula(ws, 'I%d' % S_TOT, '=SUM(I%d:I%d)' % (S_INI, S_FIN), fmt=EUR, bold=True, destacar=True)
    motor.semaforo_texto(ws, 'L%d:L%d' % (S_INI, S_FIN),
                         ((VEREDICTOS[3], 'FFC7CE', '9C0006'), (VEREDICTOS[1], 'FFEB9C', '9C6500'),
                          (VEREDICTOS[2], 'FFEB9C', '9C6500'), (VEREDICTOS[0], 'C6EFCE', '006100')))
    seccion(ws, 'A%d' % (S_CNT - 1), 'Recuento')
    for j, v in enumerate(VEREDICTOS):
        fila = S_CNT + j
        motor.val(ws, 'A%d' % fila, 'Referencias con veredicto «%s»' % v)
        formula(ws, 'B%d' % fila, '=COUNTIF(L%d:L%d,"%s")' % (S_INI, S_FIN, v), fmt=ENT, bold=True)
    gris(ws, 'A%d' % (S_CNT + len(VEREDICTOS) + 1),
         'El total de la columna I es el margen sobre materia de 100 raciones con el mix de '
         'invierno. No decidas el surtido con el margen en porcentaje: es lo que hace parecer '
         'rentable lo que sólo es barato.', alto=40)
    ws.merge_cells('A%d:M%d' % (S_CNT + len(VEREDICTOS) + 1, S_CNT + len(VEREDICTOS) + 1))
    version_al_pie(ws, S_CNT + len(VEREDICTOS) + 3)
    setup(ws, apaisado=True, titulos='%d:%d' % (S_CAB, S_CAB))
    return ws


# ==========================================================================
# Mapa de celdas citables
# ==========================================================================
def mapa_celdas():
    m = [
        # --- las 14 celdas del contrato (origen de X1, X2, X2 bis, X5, X8, X11 y X17)
        ('Precio del aceite (base imponible) EUR/L', H_PAR, 'L5', 'salida'),
        ('Absorción de aceite en % del peso frito', H_PAR, 'L6', 'salida'),
        ('Densidad del aceite kg/L', H_PAR, 'L7', 'salida'),
        ('Precio del preparado para masa (base imponible) EUR/kg', H_PAR, 'L8', 'salida'),
        ('Kilos fritos por kilo de masa (celda de origen del cruce al libro 1)', H_PAR, 'L9', 'salida'),
        ('Kilos de masa por ración media (invierno)', H_MIX, 'L5', 'salida'),
        ('Ticket sin IVA por ración en verano', H_MIX, 'L6', 'salida'),
        ('Materia por ración en verano', H_MIX, 'L7', 'salida'),
        ('Materia por ración para llevar (invierno)', H_MIX, 'L8', 'salida'),
        ('Materia por ración en sala (invierno)', H_MIX, 'L9', 'salida'),
        ('Ticket sin IVA por ración en sala (invierno)', H_MIX, 'L10', 'salida'),
        ('Ticket sin IVA por ración para llevar (invierno)', H_MIX, 'L11', 'salida'),
        ('Raciones en sala, en fracción', H_MIX, 'L12', 'salida'),
        ('Aceite absorbido por ración media', H_ABS, 'L5', 'salida'),
        ('Coste hora de mano de obra', H_CH, 'L5', 'salida'),
        # --- precios de los insumos del stock inicial (origen de X17 hacia el libro 2)
    ] + [('Precio sin IVA de «%s» (celda de origen del cruce al libro 2)' % D.INSUMOS[k]['nombre'],
          H_PAR, 'L%d' % (10 + i), 'salida')
         for i, k in enumerate(enmiendas_churreria.INSUMOS_STOCK_X17)] + [
        # --- parámetros
        ('IVA en sala', H_PAR, 'B%d' % PROW['iva_sala'], 'parametro'),
        ('IVA de churros y porras para llevar', H_PAR, 'B%d' % PROW['iva_llevar_comida'], 'parametro'),
        ('IVA del chocolate para llevar', H_PAR, 'B%d' % PROW['iva_llevar_chocolate'], 'parametro'),
        ('IVA de las demás bebidas para llevar', H_PAR, 'B%d' % PROW['iva_llevar_bebidas'], 'parametro'),
        ('IVA del granizado y la horchata para llevar', H_PAR,
         'B%d' % PROW['iva_llevar_refresco_azucarado'], 'parametro'),
        ('Gramos de masa por churro', H_PAR, 'B%d' % PROW['g_masa_churro'], 'parametro'),
        ('Gramos de masa por porra', H_PAR, 'B%d' % PROW['g_masa_porra'], 'parametro'),
        ('Merma de masa', H_PAR, 'B%d' % PROW['merma_masa_pct'], 'parametro'),
        ('Kilos fritos por kilo de masa', H_PAR, 'B%d' % PROW['kg_fritos_por_kg_masa'], 'parametro'),
        ('Importe del vaso para llevar cobrado aparte', H_PAR, 'B%d' % P_VASO, 'parametro'),
        ('Precio del aceite por garrafa', H_PAR, 'B%d' % INS_ROW['aceite'], 'entrada'),
        ('Precio de la caja de preparado para masa', H_PAR, 'B%d' % INS_ROW['mix_churros'], 'entrada'),
        # --- escandallo
        ('Coste de 1 kg de masa con el preparado', H_ESC, 'E%d' % E_COM_TOT, 'salida'),
        ('Coste de 1 kg de masa con mix propio', H_ESC, 'E%d' % E_PRO_TOT, 'salida'),
        ('Ahorro del mix propio por kg de masa', H_ESC, 'B%d' % E_AHORRO, 'salida'),
        ('Coste de materia de un churro', H_ESC, 'B%d' % E_PZ['total'], 'salida'),
        ('Coste de materia de una porra', H_ESC, 'C%d' % E_PZ['total'], 'salida'),
        ('Coste de materia de una docena de churros', H_ESC, 'B%d' % E_PZ['docena'], 'salida'),
        ('Piezas de churro por kilo de masa', H_ESC, 'B%d' % E_PZ['pzkg'], 'salida'),
        # --- aceite
        ('Euros de aceite absorbido por kilo de masa', H_ABS, 'B%d' % A_ROW['eurkg'], 'salida'),
        ('Litros de aceite que se lleva un kilo de masa', H_ABS, 'B%d' % A_ROW['lac'], 'salida'),
        ('Coste de la merma por kilo vendido', H_ABS, 'B%d' % A_ROW['coste_merma'], 'salida'),
        ('Peso del aceite absorbido en la materia de la ración', H_ABS, 'B%d' % A_ROW['peso'], 'salida'),
        # --- chocolate
        ('Coste del chocolate por litro', H_CHO, 'B%d' % C_ROW['clitro'], 'salida'),
        ('Coste de una taza de chocolate', H_CHO, 'B%d' % C_ROW['taza'], 'salida'),
        ('Cacao seco total del preparado del ejemplo', H_CHO, 'B%d' % C_ROW['cacao'], 'entrada'),
        ('Cacao seco total mínimo del chocolate a la taza', H_CHO, 'B%d' % C_ROW['minimo'], 'parametro'),
        ('Aviso de la taza antes de imprimir la carta', H_CHO, 'B%d' % C_ROW['aviso'], 'salida'),
        # --- coste hora
        ('Minutos de mano de obra por ración', H_CH, 'B%d' % H_ROW['minut'], 'entrada'),
        ('Coste de mano de obra por ración', H_CH, 'B%d' % H_ROW['morac'], 'salida'),
        # --- ración, docena o kilo
        ('Formato que más deja por kilo de masa', H_RDK, 'B%d' % R_RES, 'salida'),
        ('Euros por kilo de masa del mejor formato', H_RDK, 'B%d' % (R_RES + 1), 'salida'),
        ('Euros por kilo de masa del peor formato', H_RDK, 'B%d' % (R_RES + 3), 'salida'),
        # --- mix
        ('Ticket sin IVA por ración (invierno)', H_MIX, 'D%d' % M_RES['ticket'], 'salida'),
        ('Materia por ración (invierno)', H_MIX, 'D%d' % M_RES['materia'], 'salida'),
        ('Margen sobre materia por ración en euros (invierno)', H_MIX, 'D%d' % M_RES['margen_eur'], 'salida'),
        ('Comprobación de los dos mixes', H_MIX, 'B%d' % M_RES['cuadre'], 'salida'),
        # --- los dos márgenes
        ('Margen sobre materia prima (invierno)', H_DOS, 'B%d' % DM['m1'], 'salida'),
        ('Margen sobre materia prima (julio y agosto)', H_DOS, 'C%d' % DM['m1'], 'salida'),
        ('Margen tras aceite y mano de obra (invierno)', H_DOS, 'B%d' % DM['m2'], 'salida'),
        ('Margen tras aceite y mano de obra (julio y agosto)', H_DOS, 'C%d' % DM['m2'], 'salida'),
        ('Cifra de contraste de Loomis (CUS-01)', H_DOS, 'B%d' % DM['loomis'], 'parametro'),
        ('Cifra de contraste de La Artesana (CUS-30)', H_DOS, 'B%d' % DM['artesana'], 'parametro'),
        # --- surtido
        ('Margen de 100 raciones de invierno', H_SUR, 'I%d' % S_TOT, 'salida'),
    ]
    for j, v in enumerate(VEREDICTOS):
        m.append(('Referencias con veredicto %s' % v, H_SUR, 'B%d' % (S_CNT + j), 'salida'))
    for rid in ('CH1', 'CH6', 'CH7'):
        r = D.ref(rid)
        m.append(('Euros por kilo de masa de %s' % r['nombre'], H_RDK,
                  'J%d' % (R_INI + CHURROS.index(r)), 'salida'))
    return m


# ==========================================================================
# Cierre: guardar, cachear, verificar, contrato, lista negra y mapa
# ==========================================================================
_PROHIBIDAS = ('INDIRECT', 'COUNTA', 'PMT(', 'OFFSET', 'XLOOKUP', 'LET(', 'LAMBDA', 'RANK(',
               'NETWORKDAYS', 'IRR(')
RX_CONST_DEC = re.compile(r'[*/]\s*\d{1,3}[.,]\d{1,4}(?!\d)')


def _textos(wbf):
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                if isinstance(c.value, str):
                    yield '%s!%s' % (ws.title, c.coordinate), c.value
                if c.comment is not None:
                    yield '%s!%s (nota)' % (ws.title, c.coordinate), c.comment.text


def _gate_lista_negra(wbf):
    fallos = []
    for donde, texto in _textos(wbf):
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
            if frase in bajo:
                fallos.append('%s: el libro 3 no recibe cruces y no puede llevar «%s»' % (donde, frase))
    if fallos:
        raise SystemExit('LISTA NEGRA / IDS PROHIBIDOS en %s:\n  %s' % (NOMBRE, '\n  '.join(fallos[:40])))


def _gate_contrato(wbf, wbv):
    """Cada celda de origen de `CRUCES` (origen = 3) tiene rótulo en K, valor en L y el
    valor por defecto que `datos_ejemplo` calcula para El Molinete."""
    if D._ERROR_CRUCES:
        raise SystemExit('datos_ejemplo no pudo calcular los cruces: %s' % D._ERROR_CRUCES)
    fallos, filas = [], []
    for c in D.CRUCES:
        if c['origen'] != LIBRO:
            continue
        if c['fichero_origen'] != FICHERO:
            fallos.append('%s: fichero de origen %s' % (c['x'], c['fichero_origen']))
            continue
        hoja, celda = c['hoja_origen'], c['celda_origen']
        if not re.match(r'^L\d+$', celda) or int(celda[1:]) < 5:
            fallos.append('%s: la celda de origen %s no está en la L desde la fila 5' % (c['x'], celda))
            continue
        rot = wbf[hoja]['K' + celda[1:]].value
        if not isinstance(rot, str) or not rot.strip():
            fallos.append('%s: %s!K%s sin rótulo' % (c['x'], hoja, celda[1:]))
        v = wbv[hoja][celda].value
        esperado = c['valor_defecto']
        if not isinstance(v, (int, float)) or abs(v - esperado) > max(1e-9, abs(esperado) * 1e-9):
            fallos.append('%s: %s!%s = %r y datos_ejemplo dice %r (%s)'
                          % (c['x'], hoja, celda, v, esperado, c['concepto']))
        filas.append((c['x'], hoja, celda, v, esperado))
    if fallos:
        raise SystemExit('CONTRATO DE CRUCES ROTO en %s:\n  %s' % (NOMBRE, '\n  '.join(fallos)))
    return filas


def cerrar(wb, mapa_celdas_):
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
    ruta = os.path.join(destino, NOMBRE + '.xlsx')
    wb.save(ruta)

    # --- fórmulas: prohibidas, externas, constantes, divisiones -----------------
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
        for m in RX_CONST_DEC.finditer(sin_texto):
            problemas.append('%s!%s constante tecleada %s en %s' % (hoja, coord, m.group(0), form[:70]))
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
    contrato = _gate_contrato(wbf, wbv)

    # --- notas legales: cada id que el libro 3 debe citar está puesto ------------
    requeridos = [i for i, (_t, libros) in D.IDS_LEGALES_REQUERIDOS.items() if LIBRO in libros]
    puestos = set(pid for _h, _c, pid in NOTAS_LEGALES)
    faltan = [i for i in requeridos if i not in puestos]
    if faltan:
        raise SystemExit('Faltan notas legales del libro 3: %s' % ', '.join(faltan))

    mapa = {}
    for etiqueta, hoja, coord, tipo in mapa_celdas_:
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
            'cache': (salida_cache.strip().splitlines() or [''])[-1]}


# ==========================================================================
# Demostraciones con pycel
# ==========================================================================
def demo(ruta):
    from pycel import ExcelCompiler
    ok, fallos = [], []

    def prueba(nombre, cond, detalle=''):
        (ok if cond else fallos).append(nombre + (' - ' + detalle if detalle else ''))

    def nuevo():
        return ExcelCompiler(ruta)

    def ev(xl, hoja, coord):
        return xl.evaluate("'%s'!%s" % (hoja, coord))

    # 1. Subir el precio de la garrafa de aceite mueve el precio publicado (X2, X17), el
    #    aceite absorbido por ración (X2 bis) y la materia en sala (X11).
    xl = nuevo()
    a0 = ev(xl, H_PAR, 'L5')
    r0 = ev(xl, H_ABS, 'L5')
    m0 = ev(xl, H_MIX, 'L9')
    xl.set_value("'%s'!B%d" % (H_PAR, INS_ROW['aceite']), D.INSUMOS['aceite']['precio_formato'] * 1.5)
    a1, r1, m1 = ev(xl, H_PAR, 'L5'), ev(xl, H_ABS, 'L5'), ev(xl, H_MIX, 'L9')
    prueba('subir un 50 % la garrafa de aceite sube el precio por litro un 50 % y el aceite '
           'absorbido por ración, y encarece la materia en sala',
           abs(a1 / a0 - 1.5) < 1e-9 and abs(r1 / r0 - 1.5) < 1e-9 and m1 > m0,
           'EUR/L %.4f -> %.4f · aceite/ración %.5f -> %.5f · materia sala %.4f -> %.4f'
           % (a0, a1, r0, r1, m0, m1))

    # 2. Si el precio del aceite se escribe CON IVA, el libro lo pasa a base imponible.
    xl = nuevo()
    ev(xl, H_PAR, 'L5')
    xl.set_value("'%s'!C%d" % (H_PAR, INS_ROW['aceite']), 'Sí')
    a2 = ev(xl, H_PAR, 'L5')
    prueba('marcar «el precio lleva IVA» saca el IVA antes de publicar el EUR/L',
           abs(a2 - a0 / (1 + D.P('iva_compra_alimentos'))) < 1e-9, '%.4f -> %.4f' % (a0, a2))

    # 3. Pasar a mix propio abarata la masa y la materia en sala.
    xl = nuevo()
    ev(xl, H_MIX, 'L9')
    xl.set_value("'%s'!B%d" % (H_PAR, P_MASA_SEL), MASAS[1])
    m3 = ev(xl, H_MIX, 'L9')
    prueba('elegir «Mix propio» abarata la materia por ración en sala',
           m3 < m0, '%.4f -> %.4f' % (m0, m3))

    # 4. V-06: con menos del 35 % de cacao seco total, aviso antes de imprimir la carta.
    xl = nuevo()
    aviso0 = ev(xl, H_CHO, 'B%d' % C_ROW['aviso'])
    xl.set_value("'%s'!B%d" % (H_CHO, C_ROW['cacao']), 0.30)
    aviso1 = ev(xl, H_CHO, 'B%d' % C_ROW['aviso'])
    prueba('la taza avisa con menos del 35 % de cacao seco total',
           aviso0.startswith('Sin aviso') and aviso1.startswith('Consulta a tu servicio de consumo'),
           '%r -> %r' % (aviso0, aviso1))

    # 5. Subir al 21 % el IVA del chocolate para llevar baja el ticket para llevar (X11).
    xl = nuevo()
    t0 = ev(xl, H_MIX, 'L11')
    xl.set_value("'%s'!B%d" % (H_PAR, PROW['iva_llevar_chocolate']), D.P('iva_general'))
    t1 = ev(xl, H_MIX, 'L11')
    prueba('el IVA del chocolate para llevar al 21 % baja el ticket SIN IVA para llevar',
           t1 < t0, '%.4f -> %.4f' % (t0, t1))

    # 6. Los dos márgenes: el segundo resta la mano de obra y queda por debajo del primero;
    #    subir el coste hora lo baja y no toca el primero.
    xl = nuevo()
    g1 = ev(xl, H_DOS, 'B%d' % DM['m1'])
    g2 = ev(xl, H_DOS, 'B%d' % DM['m2'])
    xl.set_value("'%s'!B%d" % (H_CH, H_ROW['chora']), D.coste_hora_mano_obra() * 1.2)
    g1b = ev(xl, H_DOS, 'B%d' % DM['m1'])
    g2b = ev(xl, H_DOS, 'B%d' % DM['m2'])
    prueba('el margen tras mano de obra es menor que el margen sobre materia y sólo él se '
           'mueve con el coste hora', g2 < g1 and abs(g1b - g1) < 1e-12 and g2b < g2,
           'margen 1 %.4f · margen 2 %.4f -> %.4f' % (g1, g2, g2b))

    # 7. Los valores del ejemplo cuadran con datos_ejemplo (márgenes y ración frente a kilo).
    xl = nuevo()
    e_ch1 = ev(xl, H_RDK, 'J%d' % (R_INI + CHURROS.index(D.ref('CH1'))))
    e_ch7 = ev(xl, H_RDK, 'J%d' % (R_INI + CHURROS.index(D.ref('CH7'))))
    prueba('euros por kilo de masa de la ración y del kilo, y los dos márgenes, iguales a '
           'datos_ejemplo', abs(e_ch1 - D.euros_por_kg_masa('CH1')) < 1e-9
           and abs(e_ch7 - D.euros_por_kg_masa('CH7')) < 1e-9
           and abs(g1 - D.margen_sobre_materia('invierno')) < 1e-9
           and abs(g2 - D.margen_tras_mano_de_obra('invierno')) < 1e-6,
           'ración %.4f · kilo %.4f · margen 1 %.4f · margen 2 %.4f' % (e_ch1, e_ch7, g1, g2))
    return ok, fallos


# ==========================================================================
def main():
    requeridos = [i for i, (_t, libros) in D.IDS_LEGALES_REQUERIDOS.items() if LIBRO in libros]
    D.gate_legal(requeridos)
    if NR != sum(D.FAMILIAS_ESPERADO.values()):
        raise SystemExit('La carta tiene %d referencias y la SPEC firma %d'
                         % (NR, sum(D.FAMILIAS_ESPERADO.values())))
    for familia, n in D.FAMILIAS_ESPERADO.items():
        if len(D.por_familia(familia)) != n:
            raise SystemExit('La familia «%s» no tiene %d referencias' % (familia, n))
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_escandallo(wb)
    hoja_absorcion(wb)
    hoja_chocolate(wb)
    hoja_coste_hora(wb)
    hoja_racion(wb)
    hoja_mix(wb)
    hoja_dos_margenes(wb)
    hoja_surtido(wb)
    # orden firmado de las hojas
    orden = list(D.HOJAS[LIBRO])
    wb._sheets.sort(key=lambda ws: orden.index(ws.title))

    res = cerrar(wb, mapa_celdas())
    print('escrito: %s' % res['ruta'])
    print('hojas: %d · fórmulas: %d · celdas verdes: %d · verdes vacías: %d'
          % (res['hojas'], res['formulas'], res['verdes'], len(res['verdes_vacias'])))
    print('fórmulas que devuelven «sin dato» a propósito: %d' % res['sin_dato'])
    print('notas legales: %d · etiquetas en el mapa: %d' % (res['notas_legales'], res['mapa']))
    print('inject_cache: %s' % res['cache'])
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
