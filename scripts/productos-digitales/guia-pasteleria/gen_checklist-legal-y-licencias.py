#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_checklist-legal-y-licencias.py — libro 6 de «Cómo Montar una Pastelería»
(SPEC §2.2 fila 6; decisiones D3, D8, D9, D13, D21, D27 y D28).

Hojas: Instrucciones · Checklist Legal (F1-F6) · Árbol de Registro Sanitario ·
Suministro a Otros Minoristas · Ruta Doméstica · Registro de Formación ·
Cronograma y Ruta Crítica.

QUÉ DECIDE ESTE LIBRO
---------------------
Qué papel te toca, en qué orden, **si te basta la comunicación autonómica** y
cuándo abres. Es el libro más diferencial del bloque legal, porque corrige el
error número uno del nicho: la pastelería minorista que vende al consumidor
final **NO va al RGSEAA**, y hay consultoras cobrando por tramitarlo.

MOLDE
-----
Molde B de checklists (casilla, contador con `COUNTIF`, formato condicional),
como `guia-panaderia-obrador/checklist-legal.xlsx`, PERO con columnas de coste
previsto, coste real y fecha, con tres árboles de decisión con fórmulas y con un
cronograma que calcula la ruta crítica. El Gantt del molde de panadería tiene
CERO fórmulas; éste las tiene.

DECISIONES TÉCNICAS
-------------------
* **El art. 3 se escribe con su estructura real (D8).** Puerta de entrada
  primero -sólo aplica si suministras a otros minoristas de DISTINTA
  titularidad-, luego las tres condiciones ACUMULATIVAS (marginal Y localizado Y
  restringido) y, dentro de «marginal», las dos vías ALTERNATIVAS: el 25 % del
  volumen anual O los 500 kg a la semana incluyendo el consumidor final. Está
  prohibido escribir «los 500 kg incluyen el mostrador, así que puedes pasarte
  sin un solo B2B»: describe una trampa que no existe.
* **La ruta doméstica lleva los TRES límites del art. 13.9** (D13): el tope
  absoluto de 100 kg/semana, la proporcionalidad con el tamaño de las
  instalaciones -que va marcada como CRITERIO PROPIO DE LA CASA, no como norma,
  porque la norma no da número- y el «se demostrará documentalmente». Y la lista
  blanca del art. 13.8 se publica con sus CINCO letras, incluida la e), que
  remite a las comunidades autónomas: por eso «la tarta de nata desde casa no es
  legal» NO se puede escribir como afirmación nacional.
* **La ruta crítica se calcula con aritmética de índices de mes**, no con
  funciones de fecha: `NETWORKDAYS` está prohibida en toda la familia. La
  holgura sale de una matriz de dependencias visible, con un valor centinela
  para poder usar `MIN` sin que un texto se cuele en el rango.
* **Cuatro CCAA de ejemplo** (D27), declaradas como ejemplos, más cómo encontrar
  la tuya. Las 17 multiplican el mantenimiento justo cuando se están adaptando
  al RD 1021/2022.
* Cada dato legal lleva su nota «Verificado el 10-09-2026 · norma y artículo ·
  URL» como comentario de celda; `gate_legal()` corre antes de escribir una sola.
* Los trámites sin importe conocido NO se rellenan a ojo: la celda verde dice
  «A presupuestar», que es la etiqueta de la familia, y un contador te dice
  cuántos te faltan por pedir.

Salida fija: build/checklist-legal-y-licencias.xlsx + su mapa de celdas.
Via: Claude Code
"""
import datetime
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import _comun_libros_5_6 as C                                  # noqa: E402
import motor                                                   # noqa: E402
import datos_ejemplo as D                                      # noqa: E402

NOMBRE = 'checklist-legal-y-licencias'
TITULO = 'Checklist legal, licencias y cronograma de apertura'

H_INS = 'Instrucciones'
H_CHK = 'Checklist Legal (F1-F6)'
H_ARB = 'Árbol de Registro Sanitario'
H_SUM = 'Suministro a Otros Minoristas'
H_DOM = 'Ruta Doméstica'
H_FOR = 'Registro de Formación'
H_GAN = 'Cronograma y Ruta Crítica'

Q_CHK = "'" + H_CHK + "'!"
Q_ARB = "'" + H_ARB + "'!"
Q_SUM = "'" + H_SUM + "'!"
Q_DOM = "'" + H_DOM + "'!"
Q_GAN = "'" + H_GAN + "'!"

# Hallazgo A5 (2026-09-10): los símbolos ☐/✓ están fuera de WinAnsi (cp1252).
# El libro 7 resolvió el mismo caso (estado de un trámite) con vocabulario en
# vez de símbolos; aquí se sigue el mismo criterio.
HECHO, PENDIENTE, NOAPLICA = 'Hecho', 'Pendiente', 'N/A'
SI, NO = 'Sí', 'No'
SIN_IMPORTE = 'A presupuestar'
SIN_PAGAR = 'Sin pagar'
FECHA_BASE = datetime.date(2026, 9, 10)

CCAA_LISTA = list(D.CCAA_EJEMPLO) + ['Otra (busca su decreto)']


def ie(expr):
    return motor.iferror(expr)


# ==========================================================================
# Hoja «Checklist Legal (F1-F6)»: filas
# ==========================================================================
K_CAB = 5
_fila = K_CAB + 1
FASES = []                       # (fase, titulo, fila_sec, ini, fin, fila_cont)
for _f in sorted(D.FASES_CHECKLIST):
    _items = [i for i, it in enumerate(D.CHECKLIST_LEGAL) if it[0] == _f]
    _sec = _fila
    _ini = _sec + 1
    _fin = _ini + len(_items) - 1
    _cont = _fin + 1
    FASES.append((_f, D.FASES_CHECKLIST[_f], _sec, _ini, _fin, _cont, _items))
    _fila = _cont + 2
K_INI = FASES[0][3]
K_FIN = FASES[-1][4]
K_SEC_RES = _fila
K_TOTAL = K_SEC_RES + 1
K_HECHOS = K_SEC_RES + 2
K_NA = K_SEC_RES + 3
K_AVANCE = K_SEC_RES + 4
K_PREV = K_SEC_RES + 5
K_REAL = K_SEC_RES + 6
K_DESV = K_SEC_RES + 7
K_SINIMP = K_SEC_RES + 8
K_CCAA = K_SEC_RES + 9
K_NOTA = K_SEC_RES + 11
K_LISTAS = K_SEC_RES + 13


# ==========================================================================
# Filas del resto de hojas
# ==========================================================================
A = {'sec_preg': 5, 'final': 6, 'b2b': 7, 'sucursales': 8, 'ccaa': 9,
     'sec_ver': 11, 'regimen': 12, 'tramite': 13, 'habilita': 14,
     'plazo': 15, 'aviso_suc': 16,
     'sec_tabla': 18, 'cab': 19, 'caso1': 20, 'caso2': 21, 'caso3': 22,
     'nota': 24, 'listas': 26}

U = {'sec_puerta': 5, 'puerta': 6, 'aviso_puerta': 7,
     'sec_dest': 9, 'cab': 10, 'ini': 11, 'fin': 16, 'tot': 17,
     'sec_marg': 19, 'umbral_a': 20, 'tu_pct': 21, 'via_a': 22,
     'umbral_b': 23, 'total_kg': 24, 'via_b': 25, 'marginal': 26,
     'sec_loc': 28, 'misma_zona': 29, 'radio': 30, 'max_km': 31,
     'otra_ccaa': 32, 'localizado': 33,
     'sec_res': 35, 'inscritos': 36, 'restringido': 37,
     'sec_ver': 39, 'cumplidas': 40, 'veredicto': 41, 'ademas': 42,
     'nota': 44, 'listas': 46}

M = {'sec_datos': 5, 'm2': 6, 'kg': 7, 'registro': 8, 'amplia': 9, 'ccaa': 10,
     'sec_lim': 12, 'tope': 13, 'sem_tope': 14, 'prop': 15, 'kg_m2': 16,
     'sem_prop': 17, 'demostrable': 18,
     'sec_blanca': 20, 'cab_blanca': 21, 'blanca_ini': 22, 'blanca_fin': 26,
     'aviso_e': 27,
     'sec_prohib': 29, 'cab_prohib': 30, 'prohib_ini': 31, 'prohib_fin': 33,
     'sec_etiq': 35, 'etiqueta': 36,
     'sec_val': 38, 'val1': 39, 'val2': 40,
     'sec_ver': 42, 'veredicto': 43, 'nota': 45, 'listas': 47}

R_CAB = 5
R_INI = 6
R_FIN = R_INI + len(D.PLANTILLA) - 1
R_SEC_PAR = R_FIN + 2
R_VALIDEZ = R_SEC_PAR + 1
R_CONTROL = R_SEC_PAR + 2
R_SEC_RES = R_SEC_PAR + 4
R_CON = R_SEC_RES + 1
R_CADUCADAS = R_SEC_RES + 2
R_PROXIMAS = R_SEC_RES + 3
R_NOTA = R_SEC_RES + 5

G_ARRANQUE = 5
G_CENTINELA = 6
G_CAB = 8
G_INI = 9
G_FIN = G_INI + len(D.GANTT) - 1
G_SEC_MAT = G_FIN + 2
G_MAT_CAB = G_SEC_MAT + 1
G_MAT_INI = G_MAT_CAB + 1
G_MAT_FIN = G_MAT_INI + len(D.GANTT) - 1
G_SEC_RES = G_MAT_FIN + 2
G_DURACION = G_SEC_RES + 1
G_CRITICOS = G_SEC_RES + 2
G_MES_AP = G_SEC_RES + 3
G_NOMBRE_MES = G_SEC_RES + 4
G_EN_PICO = G_SEC_RES + 5
G_AVISO = G_SEC_RES + 6
G_SEC_PICOS = G_SEC_RES + 8
G_PICOS_CAB = G_SEC_PICOS + 1
G_PICOS_INI = G_PICOS_CAB + 1
G_PICOS_FIN = G_PICOS_INI + len(D.PICOS) - 1
G_NOTA = G_PICOS_FIN + 2
G_LISTAS = G_PICOS_FIN + 4
COLS_MAT = ('C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N')


# ==========================================================================
# Hoja «Instrucciones»
# ==========================================================================
PASOS = [
    '1. Hoja «Checklist Legal (F1-F6)»: los treinta trámites en el orden en que '
    'hay que hacerlos, repartidos en seis fases. Marca la casilla, escribe el '
    'coste que te presupuestan y el que acabas pagando, y pon las dos fechas. '
    'Cada fase lleva su contador y su porcentaje de avance; abajo está el '
    'resumen de todo y la desviación entre lo previsto y lo real.',
    '2. Hoja «Árbol de Registro Sanitario»: tres preguntas y un veredicto. Es '
    'la hoja que corrige el error más caro del sector: una pastelería que vende '
    'al consumidor final está EXCLUIDA del registro estatal (RGSEAA) y lo que '
    'le toca es una comunicación o declaración responsable a su comunidad '
    'autónoma, que además NO habilita para abrir.',
    '3. Hoja «Suministro a Otros Minoristas»: el árbol del art. 3 del '
    'RD 1021/2022, con su puerta de entrada delante. Si no sirves a otros '
    'comercios de distinta titularidad, este artículo no te aplica y la hoja te '
    'lo dice en la primera línea. Si te aplica, las tres condiciones son '
    'ACUMULATIVAS y dentro de «marginal» hay DOS vías alternativas.',
    '4. Hoja «Ruta Doméstica»: si te planteas empezar desde casa. Los tres '
    'límites del art. 13.9 (el tope de kilos, la proporcionalidad con el '
    'tamaño y el «se demostrará documentalmente»), la lista blanca del art. '
    '13.8 con sus CINCO letras y las cinco prohibiciones del 13.5 agrupadas '
    'por su régimen. Ojo con la letra e): tu comunidad puede haber ampliado la '
    'lista, y una ya lo ha hecho.',
    '5. Hoja «Registro de Formación»: una línea por persona con la fecha, el '
    'contenido y la caducidad que TÚ fijas. El «carnet de manipulador» no '
    'existe desde 2010: lo que hay que tener es este registro, y la '
    'responsabilidad de tenerlo es de la empresa.',
    '6. Hoja «Cronograma y Ruta Crítica»: doce hitos con su duración y sus '
    'dependencias. La hoja calcula cuándo empieza y acaba cada uno, cuánta '
    'holgura tiene, cuáles están en la ruta crítica -los que si se retrasan un '
    'día retrasan la apertura un día- y en qué mes acabas abriendo. Y te avisa '
    'si esa fecha cae dentro de una campaña.',
]

NOTAS_LIBRO = [
    'EL ERROR NÚMERO UNO DEL SECTOR ESTÁ EN LA SEGUNDA HOJA. Una pastelería '
    'minorista que vende al consumidor final NO se inscribe en el Registro '
    'General Sanitario de Empresas Alimentarias y Alimentos. Está excluida por '
    'norma. Lo que le toca es comunicárselo a su comunidad autónoma. Hay '
    'consultoras cobrando por tramitar un registro que no hace falta, y hay '
    'quien retrasa una apertura semanas esperando una inscripción que nadie le '
    'ha pedido.',
    'LA COMUNICACIÓN AUTONÓMICA NO HABILITA PARA ABRIR, y eso corta en los dos '
    'sentidos: no tienes que esperar a que te contesten, pero tampoco te '
    'protege de nada si el resto no está en regla.',
    'LO QUE CAMBIA POR COMUNIDAD AUTÓNOMA VA MARCADO. En el checklist hay una '
    'columna que lo dice trámite a trámite. Aquí se usan cuatro comunidades '
    'como EJEMPLO -Madrid, Cataluña, Andalucía y la Comunitat Valenciana- '
    'porque son las que se están adaptando ahora mismo al RD 1021/2022. Si la '
    'tuya no está, busca «registro sanitario establecimientos alimentarios '
    'menores» más el nombre de tu comunidad: el decreto que salga es el tuyo.',
    'LOS COSTES QUE NO CONOCEMOS NO SE INVENTAN. Los trámites cuyo importe '
    'depende de tu ayuntamiento o de tu proveedor vienen con «A presupuestar» '
    'en la celda verde, y el resumen te dice cuántos te quedan por pedir. Un '
    'número puesto a ojo en una tasa municipal es peor que un hueco: el hueco '
    'lo ves.',
    'LAS FECHAS CADUCAN. El convenio y el salario mínimo, el 31-12-2026. '
    'Verifactu entra el 1-01-2027 para sociedades y el 1-07-2027 para '
    'autónomos. Los envases reutilizables, el 1-01-2027. Y el régimen '
    'transitorio de Madrid termina el 28-03-2027. Todo eso está en celdas y en '
    'notas, no cosido en un párrafo, para que se pueda actualizar de una en '
    'una.',
    'ESTE LIBRO NO ES UN DICTAMEN JURÍDICO. Cada dato normativo lleva en su '
    'celda un comentario con la norma, el artículo y el enlace al texto '
    'consolidado, verificados el 10 de septiembre de 2026. Lo que hay que '
    'hacer con eso es leerlos y contrastarlos con tu ayuntamiento y con tu '
    'comunidad, no fiarte de una casilla.',
]

FRONTERA = [
    ('pack-appcc (14 €)',
     'Los registros del plan de APPCC ya montados y listos para rellenar.',
     'Aquí sólo hay una FILA de checklist que dice «redacta el plan y designa '
     'por su nombre al responsable». El plan en sí es aquel producto.'),
    ('kit-tareas-pasteleria (12 €)',
     'La matriz de alérgenos de vitrina y el registro de temperaturas de '
     'recepción, ya construidos.',
     'Aquí hay una fila que te recuerda publicar la matriz antes de abrir. La '
     'guía no rehace ninguna de las dos.'),
    ('El libro «checklist-equipamiento-y-proveedores» de esta misma guía',
     'El plazo de entrega de cada equipo, que es lo que de verdad mueve la '
     'fecha de apertura.',
     'El cronograma de este libro trabaja en MESES y con una duración por '
     'hito. Cuando tengas los plazos por escrito, tráelos al hito «Pedido y '
     'entrega del equipamiento».'),
    ('El libro «plan-financiero-3-anos-pasteleria» de esta misma guía',
     'Los euros: qué cuesta cada bloque de inversión y cuándo sale de caja.',
     'Los costes de este checklist son los de los TRÁMITES. La obra, el '
     'equipamiento y el fondo de maniobra están allí, y allí es donde se '
     'suman.'),
]


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS, 0)
    C.anchos(ws, {'A': 44, 'B': 44, 'C': 44})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=C.ORO)
    ws.row_dimensions[1].height = 26
    motor.val(ws, 'A2', C.SUBTITULO)
    ws['A2'].font = Font(size=9, color=C.GRIS_TXT)
    motor.val(ws, 'A3', 'Para qué sirve: saber qué papel te toca, en qué '
                        'orden, si te basta la comunicación autonómica y '
                        'cuándo abres.')
    ws['A3'].font = Font(italic=True, size=9)

    fila = 5
    C.seccion(ws, 'A%d' % fila, 'Instrucciones de uso')
    fila += 1
    for paso in PASOS:
        C.parrafo(ws, fila, paso, 'A', 'C', alto=62)
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, C.NOTA_VERDES)
    ws['A%d' % fila].fill = PatternFill('solid', fgColor=motor.VERDE)
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Lo que conviene saber antes de empezar')
    fila += 1
    for texto in NOTAS_LIBRO:
        C.parrafo(ws, fila, texto, 'A', 'C', alto=72)
        fila += 1
    fila += 1

    C.seccion(ws, 'A%d' % fila,
              'QUÉ HACE ESTE LIBRO Y QUÉ HACE OTRO (para no teclear dos veces)')
    fila += 1
    C.cabecera(ws, fila, [('A', 'Producto o libro'), ('B', 'Qué aporta'),
                          ('C', 'Qué NO hace este libro')], altura=26)
    fila += 1
    for producto, aporta, no_hace in FRONTERA:
        motor.val(ws, 'A%d' % fila, producto, bold=True, wrap=True)
        motor.val(ws, 'B%d' % fila, aporta, wrap=True)
        motor.val(ws, 'C%d' % fila, no_hace, wrap=True)
        ws.row_dimensions[fila].height = 62
        fila += 1
    fila += 1

    C.seccion(ws, 'A%d' % fila, 'Cada cuánto se usa este libro')
    fila += 1
    C.parrafo(ws, fila,
              'Cadencia: el checklist y el cronograma, UNA VEZ A LA SEMANA '
              'desde que decides abrir hasta que abres. Los tres árboles '
              '-registro sanitario, suministro a otros minoristas y ruta '
              'doméstica-, UNA VEZ AL PRINCIPIO y otra cada vez que cambies de '
              'canal: el día que aceptes servir a la cafetería de al lado '
              'estarás cambiando de régimen sin darte cuenta. El registro de '
              'formación, cada vez que entra alguien y cuando caduca la '
              'formación de alguien.', 'A', 'C', alto=72)
    fila += 2

    C.parrafo(ws, fila, C.NOTA_DESPROTEGER, 'A', 'C', alto=28)
    fila += 2
    C.pie(ws, fila, 'A', 'C')
    C.pagina(ws, apaisado=False, area='A1:C%d' % (fila + 1))
    return ws


# ==========================================================================
# Hoja «Checklist Legal (F1-F6)»
# ==========================================================================
def hoja_checklist(wb):
    ws = wb.create_sheet(H_CHK)
    C.anchos(ws, {'A': 6, 'B': 7, 'C': 62, 'D': 20, 'E': 11, 'F': 15,
                  'G': 15, 'H': 14, 'I': 14, 'J': 13, 'K': 90})
    C.encabezar(ws, 'Checklist legal y de licencias, en seis fases',
                'Treinta trámites en el orden en que hay que hacerlos. Marca '
                'la casilla, escribe lo que te presupuestan y lo que acabas '
                'pagando, y pon las dos fechas. Lo que cambia según tu '
                'comunidad autónoma va marcado en su columna.', col_fin='K')
    C.cabecera(ws, K_CAB,
               [('A', ''), ('B', 'Fase'), ('C', 'Trámite'),
                ('D', 'Responsable'), ('E', 'Plazo (días)'),
                ('F', 'Coste previsto (€)'), ('G', 'Coste real (€)'),
                ('H', 'Fecha objetivo'), ('I', 'Fecha hecha'),
                ('J', '¿Cambia por CCAA?'), ('K', 'Notas')])

    refs, fila_listas = C.bloque_listas(
        ws, K_LISTAS,
        [('Estado del trámite', [PENDIENTE, HECHO, NOAPLICA]),
         ('Sí o No', [SI, NO])], col='A')

    casillas, ccaas = [], []
    for fase, titulo, sec, ini, fin, cont, items in FASES:
        C.seccion(ws, 'A%d' % sec, '%s · %s' % (fase, titulo))
        for letra in 'BCDEFGHIJK':
            motor.val(ws, letra + str(sec), '')
            ws[letra + str(sec)].fill = PatternFill('solid',
                                                    fgColor=C.CABECERA)
        for pos, idx in enumerate(items):
            (f, tramite, responsable, plazo, coste, fuente, cambia,
             nota_txt) = D.CHECKLIST_LEGAL[idx]
            fila = ini + pos
            C.entrada(ws, 'A%d' % fila, PENDIENTE, etiqueta=tramite,
                      align='center')
            casillas.append('A%d' % fila)
            motor.val(ws, 'B%d' % fila, fase, align='center')
            motor.val(ws, 'C%d' % fila, tramite, wrap=True)
            motor.val(ws, 'D%d' % fila, responsable)
            C.entrada(ws, 'E%d' % fila, plazo, fmt=C.ENT, etiqueta=tramite,
                      align='center')
            C.entrada(ws, 'F%d' % fila,
                      coste if coste is not None else SIN_IMPORTE,
                      fmt=(C.EUR if coste is not None else None),
                      etiqueta=tramite)
            C.entrada(ws, 'G%d' % fila, SIN_PAGAR, etiqueta=tramite)
            C.entrada(ws, 'H%d' % fila, FECHA_BASE, fmt=C.FECHA,
                      etiqueta=tramite)
            C.entrada(ws, 'I%d' % fila, FECHA_BASE, fmt=C.FECHA,
                      etiqueta=tramite)
            C.entrada(ws, 'J%d' % fila, SI if cambia else NO, etiqueta=tramite,
                      align='center')
            ccaas.append('J%d' % fila)
            C.nota(ws, 'K%d' % fila,
                   (nota_txt or '') + ('  [Fuente: %s]' % fuente if fuente
                                       else ''))
            ws.row_dimensions[fila].height = 34
            # Hallazgo B2 (2026-09-10): PA-07 es un hallazgo NEGATIVO («el CTE
            # DB-HS 3 NO se aplica a un obrador: remite al RITE»), pero
            # `nota_legal()` sólo compone «Verificado · norma · URL» y nunca
            # el `dato`, así que ponerlo como comentario de celda se leía como
            # una verificación positiva del CTE -exactamente lo contrario de
            # lo que dice el texto visible de la columna K en esta fila-. La
            # base correcta para el comentario es PA-07b (RITE), que es la que
            # de verdad respalda «salida de humos hasta cubierta».
            for pa in [t.strip() for t in fuente.replace('+', ' ').split()
                       if t.strip().startswith('PA-')]:
                if pa == 'PA-07':
                    pa = 'PA-07b'
                if D.nota_legal(pa):
                    C.nota_celda(ws, 'C%d' % fila, pa)
                    break
        motor.val(ws, 'C%d' % cont, 'AVANCE DE LA FASE ' + fase, bold=True)
        motor.f(ws, 'D%d' % cont,
                ie('COUNTIF(A%d:A%d,"%s")' % (ini, fin, HECHO)), fmt=C.ENT,
                bold=True)
        motor.f(ws, 'E%d' % cont,
                ie('COUNTIF(B%d:B%d,"%s")' % (ini, fin, fase)), fmt=C.ENT)
        motor.f(ws, 'F%d' % cont, ie('SUMIF(F%d:F%d,">=0")' % (ini, fin)),
                fmt=C.EUR)
        motor.f(ws, 'G%d' % cont, ie('SUMIF(G%d:G%d,">=0")' % (ini, fin)),
                fmt=C.EUR)
        motor.f(ws, 'J%d' % cont,
                ie('IF(E{0}=0,"",(D{0}+COUNTIF(A{1}:A{2},"{3}"))/E{0})'
                   .format(cont, ini, fin, NOAPLICA)), fmt=C.PCT, bold=True)
        C.total_fila(ws, cont, 'ABCDEFGHIJK')
        motor.semaforo_isnumber(ws, 'J%d:J%d' % (cont, cont), '$J$%d' % cont,
                                operador='<', umbral='1',
                                bg=motor.CF_AMBAR_BG, fg=motor.CF_AMBAR_FG)
        C.nota(ws, 'K%d' % cont,
               'Hechos · trámites de la fase · coste previsto · coste real · '
               '% de avance (los «N/A» cuentan como resueltos).')

    C.dv_rango(ws, casillas, refs['Estado del trámite'],
               'Marca el estado del trámite',
               'Elige %s, %s o %s de la lista del pie de la hoja.'
               % (PENDIENTE, HECHO, NOAPLICA))
    C.dv_rango(ws, ccaas, refs['Sí o No'], 'Marca Sí o No',
               'Elige «Sí» o «No» de la lista del pie de la hoja.')

    C.seccion(ws, 'A%d' % K_SEC_RES, 'RESUMEN DE TODO EL EXPEDIENTE')
    for letra in 'BCDEFGHIJK':
        motor.val(ws, letra + str(K_SEC_RES), '')
        ws[letra + str(K_SEC_RES)].fill = PatternFill('solid',
                                                      fgColor=C.CABECERA)

    def res(fila, etiqueta, formula, fmt=None, nota_txt=None, bold=None):
        motor.val(ws, 'C%d' % fila, etiqueta, bold=bold)
        motor.f(ws, 'D%d' % fila, formula, fmt=fmt, bold=bold)
        if nota_txt:
            C.nota(ws, 'K%d' % fila, nota_txt)

    res(K_TOTAL, 'Trámites del expediente',
        ie('COUNTIF(B%d:B%d,"F*")' % (K_INI, K_FIN)), C.ENT)
    res(K_HECHOS, 'Trámites hechos',
        ie('COUNTIF(A%d:A%d,"%s")' % (K_INI, K_FIN, HECHO)), C.ENT)
    res(K_NA, 'Trámites que no te aplican (N/A)',
        ie('COUNTIF(A%d:A%d,"%s")' % (K_INI, K_FIN, NOAPLICA)), C.ENT)
    res(K_AVANCE, 'Avance del expediente (%)',
        ie('IF(D{0}=0,"",(D{1}+D{2})/D{0})'
           .format(K_TOTAL, K_HECHOS, K_NA)), C.PCT, bold=True)
    motor.semaforo_isnumber(ws, 'D%d:D%d' % (K_AVANCE, K_AVANCE),
                            '$D$%d' % K_AVANCE, operador='<', umbral='1',
                            bg=motor.CF_AMBAR_BG, fg=motor.CF_AMBAR_FG)
    res(K_PREV, 'Coste previsto total del checklist (€)',
        ie('SUMIF(F%d:F%d,">=0")' % (K_INI, K_FIN)), C.EUR,
        'OJO: esta suma NO es «lo que cuestan los papeles». Dentro está la obra '
        'civil, que es la línea de la fase F4 y se lleva ella sola la mayor '
        'parte. Los euros de la apertura, ordenados por bloques y con su IVA, '
        'están en el libro «plan-financiero-3-anos-pasteleria»: aquí sólo se '
        'controla que cada trámite tenga su importe y su fecha.')
    res(K_REAL, 'Coste real total del checklist (€)',
        ie('SUMIF(G%d:G%d,">=0")' % (K_INI, K_FIN)), C.EUR,
        'Se rellena solo a medida que vas pagando. Mientras esté a cero, la '
        'desviación de abajo no dice nada.')
    res(K_DESV, 'Desviación (real menos previsto, €)',
        ie('D%d-D%d' % (K_REAL, K_PREV)), C.EUR, bold=True)
    motor.semaforo_isnumber(ws, 'D%d:D%d' % (K_DESV, K_DESV),
                            '$D$%d' % K_DESV, operador='>', umbral='0')
    res(K_SINIMP, 'Trámites sin importe (a presupuestar)',
        ie('COUNTIF(F%d:F%d,"%s")' % (K_INI, K_FIN, SIN_IMPORTE)), C.ENT,
        'Son los que dependen de tu ayuntamiento, de tu comunidad o de un '
        'proveedor. No se rellenan a ojo: se piden. Mientras esta cifra no sea '
        'cero, tu presupuesto de apertura está incompleto.')
    motor.semaforo_isnumber(ws, 'D%d:D%d' % (K_SINIMP, K_SINIMP),
                            '$D$%d' % K_SINIMP, operador='>', umbral='0',
                            bg=motor.CF_AMBAR_BG, fg=motor.CF_AMBAR_FG)
    res(K_CCAA, 'Trámites que cambian según tu comunidad autónoma',
        ie('COUNTIF(J%d:J%d,"%s")' % (K_INI, K_FIN, SI)), C.ENT,
        'Cada uno de estos hay que confirmarlo con TU comunidad. Los ejemplos '
        'del libro son Madrid, Cataluña, Andalucía y la Comunitat Valenciana, '
        'y son eso: ejemplos.')
    C.total_fila(ws, K_AVANCE, 'CD')
    C.total_fila(ws, K_DESV, 'CD')

    C.parrafo(ws, K_NOTA,
              'Los plazos en días son ORIENTATIVOS y casi todos dependen de un '
              'tercero: el ayuntamiento, la comunidad de propietarios, el '
              'ingeniero, el instalador. El único que controlas del todo es el '
              'de pedir las cosas pronto. Y hay uno que no controla nadie: la '
              'autorización de la comunidad de propietarios para el conducto '
              'de humos depende de cuándo se reúna la junta, y es la variable '
              'que más aperturas ha retrasado.', 'A', 'K', alto=48)
    ws.freeze_panes = 'C%d' % (K_CAB + 1)
    C.pagina(ws, titulos='$%d:$%d' % (K_CAB, K_CAB),
             area='A1:K%d' % fila_listas)
    return ws


# ==========================================================================
# Hoja «Árbol de Registro Sanitario»
# ==========================================================================
CASOS_REGISTRO = (
    ('Vendes sólo al consumidor final, en tu establecimiento y por tu web',
     'Comunicación o declaración responsable al registro de tu comunidad '
     'autónoma',
     'Estás EXCLUIDO del RGSEAA por norma. La venta a distancia ya está dentro '
     'de la definición de minorista: vender por internet no te saca de este '
     'régimen.'),
    ('Suministras además a otros minoristas de DISTINTA titularidad, y cumples '
     'las tres condiciones del art. 3',
     'La misma comunicación autonómica, MÁS declaración responsable del art. '
     '3.5 y registro de destinatarios, cantidades y fechas',
     'Sigues fuera del RGSEAA, pero con papeles añadidos. La hoja «Suministro '
     'a Otros Minoristas» comprueba las tres condiciones una a una.'),
    ('Suministras a otros minoristas y NO cumples alguna de las tres',
     'Inscripción en el RGSEAA',
     'Basta con fallar una: las tres son acumulativas. La que más fácil se '
     'rompe es «restringido», y basta un cliente inscrito en el RGSEAA.'),
)


def hoja_arbol(wb):
    ws = wb.create_sheet(H_ARB)
    C.anchos(ws, {'A': 58, 'B': 30, 'C': 96})
    C.encabezar(ws, '¿Registro autonómico o RGSEAA?',
                'Tres preguntas y un veredicto. Es la hoja que corrige el '
                'error más caro del sector: hay consultoras cobrando por '
                'tramitar un registro estatal que a una pastelería minorista '
                'no le hace falta.', col_fin='C')

    refs, fila_listas = C.bloque_listas(
        ws, A['listas'], [('Sí o No', [SI, NO]),
                          ('Comunidad autónoma', CCAA_LISTA)], col='A')

    def sec(fila, texto):
        C.seccion(ws, 'A%d' % fila, texto)
        for letra in 'BC':
            motor.val(ws, letra + str(fila), '')
            ws[letra + str(fila)].fill = PatternFill('solid',
                                                     fgColor=C.CABECERA)

    sec(A['sec_preg'], 'LAS TRES PREGUNTAS')
    preguntas = (
        (A['final'], '¿Vendes al consumidor final (mostrador, encargos o tu '
                     'propia web)?', SI,
         'Si la respuesta es «Sí», eres comercio al por menor. Y el comercio '
         'al por menor está EXCLUIDO de la obligación de inscribirse en el '
         'Registro General Sanitario de Empresas Alimentarias y Alimentos.',
         'PA-01'),
        (A['b2b'], '¿Suministras a otros establecimientos MINORISTAS de '
                   'distinta titularidad?', NO,
         'Ojo a «de distinta titularidad»: si el que recibe es una sucursal '
         'tuya, no cuenta como suministro entre minoristas. Si la respuesta es '
         '«Sí», ve a la hoja «Suministro a Otros Minoristas» antes de leer el '
         'veredicto.', 'PA-02'),
        (A['sucursales'], '¿Tienes sucursales de tu misma titularidad?', NO,
         'Central con obrador y sucursales son UNA sola unidad comercial y el '
         'suministro entre ellas no es B2B. Pero cada una se inscribe en el '
         'registro autonómico de manera independiente: la ventaja viene con su '
         'deber pegado.', 'PA-03'),
    )
    for fila, etiqueta, valor, nota_txt, pa in preguntas:
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
        C.entrada(ws, 'B%d' % fila, valor, etiqueta=etiqueta, align='center')
        C.nota(ws, 'C%d' % fila, nota_txt)
        C.nota_celda(ws, 'B%d' % fila, pa)
        ws.row_dimensions[fila].height = 30
    motor.val(ws, 'A%d' % A['ccaa'], 'Tu comunidad autónoma')
    C.entrada(ws, 'B%d' % A['ccaa'], D.CCAA_EJEMPLO[0], etiqueta='CCAA',
              align='center')
    C.nota(ws, 'C%d' % A['ccaa'],
           'Cuatro comunidades de EJEMPLO: son las que se están adaptando '
           'ahora mismo al RD 1021/2022. Si la tuya no está, elige «Otra» y '
           'busca «registro sanitario establecimientos alimentarios menores» '
           'más el nombre de tu comunidad.')
    C.dv_rango(ws, ['B%d' % A['final'], 'B%d' % A['b2b'],
                    'B%d' % A['sucursales']], refs['Sí o No'],
               'Marca Sí o No', 'Elige «Sí» o «No» de la lista del pie.')
    C.dv_rango(ws, ['B%d' % A['ccaa']], refs['Comunidad autónoma'],
               'Elige tu comunidad autónoma',
               'Elige una de la lista del pie de la hoja.')

    sec(A['sec_ver'], 'EL VEREDICTO')
    motor.val(ws, 'A%d' % A['regimen'], 'Régimen que te toca', bold=True)
    motor.f(ws, 'B%d' % A['regimen'],
            ie('IF(B{0}<>"{1}","Esto no es una pastelería minorista: pide '
               'asesoramiento, el art. 3 no te cubre",'
               'IF(B{2}="{3}","Te basta la comunicación o declaración '
               'responsable de tu comunidad autónoma: estás EXCLUIDO del '
               'RGSEAA",{4}$B${5}))'
               .format(A['final'], SI, A['b2b'], NO, Q_SUM, U['veredicto'])),
            bold=True)
    ws.merge_cells('B%d:C%d' % (A['regimen'], A['regimen']))
    ws['B%d' % A['regimen']].alignment = Alignment(vertical='top', wrap_text=True)
    ws.row_dimensions[A['regimen']].height = 34
    C.nota_celda(ws, 'B%d' % A['regimen'], 'PA-01')

    motor.val(ws, 'A%d' % A['tramite'], 'Trámite concreto')
    motor.f(ws, 'B%d' % A['tramite'],
            ie('IF(B{0}="{1}","Comunicación o declaración responsable al '
               'registro de establecimientos alimentarios menores de tu '
               'comunidad autónoma","Comunicación autonómica MÁS lo que diga '
               'la hoja de suministro a otros minoristas")'
               .format(A['b2b'], NO)))
    ws.merge_cells('B%d:C%d' % (A['tramite'], A['tramite']))
    ws.row_dimensions[A['tramite']].height = 28

    motor.val(ws, 'A%d' % A['habilita'], '¿Ese trámite te habilita para abrir?')
    motor.val(ws, 'B%d' % A['habilita'],
              'No. La comunicación o declaración responsable NO es habilitante: '
              'se presenta al iniciar la actividad, no antes, y no sustituye a '
              'la licencia municipal.', wrap=True)
    ws.merge_cells('B%d:C%d' % (A['habilita'], A['habilita']))
    ws.row_dimensions[A['habilita']].height = 30
    C.nota_celda(ws, 'B%d' % A['habilita'], 'PA-01')

    motor.val(ws, 'A%d' % A['plazo'], 'Plazo que aplica en tu comunidad')
    motor.f(ws, 'B%d' % A['plazo'],
            ie('IF(B{0}="{1}","Decreto 26/2026: se presenta A LA VEZ que '
               'inicias la actividad. Los establecimientos que ya estaban '
               'abiertos tienen hasta el 28-03-2027","Busca el decreto de tu '
               'comunidad: el plazo y el modelo los pone ella")'
               .format(A['ccaa'], D.CCAA_EJEMPLO[0])))
    ws.merge_cells('B%d:C%d' % (A['plazo'], A['plazo']))
    ws.row_dimensions[A['plazo']].height = 30
    C.nota_celda(ws, 'B%d' % A['plazo'], 'PA-04')

    motor.val(ws, 'A%d' % A['aviso_suc'], 'Si tienes sucursales')
    motor.f(ws, 'B%d' % A['aviso_suc'],
            ie('IF(B{0}="{1}","Central y sucursales son UNA unidad comercial y '
               'el suministro entre ellas no es B2B, PERO cada una se inscribe '
               'por separado en el registro autonómico","No aplica")'
               .format(A['sucursales'], SI)))
    ws.merge_cells('B%d:C%d' % (A['aviso_suc'], A['aviso_suc']))
    ws.row_dimensions[A['aviso_suc']].height = 30
    C.nota_celda(ws, 'B%d' % A['aviso_suc'], 'PA-03')

    sec(A['sec_tabla'], 'LOS TRES CASOS, PARA QUE SE VEA POR QUÉ')
    C.cabecera(ws, A['cab'], [('A', 'Tu situación'), ('B', 'Lo que te toca'),
                              ('C', 'Por qué')], altura=24)
    for i, (situacion, toca, porque) in enumerate(CASOS_REGISTRO):
        fila = A['caso1'] + i
        motor.val(ws, 'A%d' % fila, situacion, wrap=True)
        motor.val(ws, 'B%d' % fila, toca, wrap=True)
        C.nota(ws, 'C%d' % fila, porque)
        ws.row_dimensions[fila].height = 46
    C.parrafo(ws, A['nota'],
              'Una pastelería que vende al consumidor final está excluida de '
              'la inscripción en el RGSEAA por el art. 2.2 del RD 191/2011, en '
              'la redacción que le dio el RD 1021/2022. Lo que sí tiene que '
              'hacer es inscribirse en el registro de su comunidad autónoma '
              'previa comunicación o declaración responsable, que la propia '
              'norma dice que «no será habilitante». Todo eso está verificado '
              'contra el texto consolidado el 10 de septiembre de 2026, y el '
              'enlace está en el comentario de cada celda.', 'A', 'C', alto=54)
    C.pagina(ws, apaisado=False, area='A1:C%d' % fila_listas)
    return ws


# ==========================================================================
# Hoja «Suministro a Otros Minoristas» (árbol del art. 3, D8)
# ==========================================================================
DESTINATARIOS = (
    ('Cafetería de la esquina', 22.0, 0.018, 1.2, NO),
    ('Restaurante del barrio', 14.0, 0.011, 2.4, NO),
    ('Tienda gourmet del centro', 9.0, 0.007, 3.1, NO),
    ('Hotel de la avenida', 6.0, 0.005, 4.0, NO),
    ('(libre: escribe aquí tu quinto cliente)', 0.0, 0.0, 0.0, NO),
    ('(libre: escribe aquí tu sexto cliente)', 0.0, 0.0, 0.0, NO),
)


def hoja_suministro(wb):
    ws = wb.create_sheet(H_SUM)
    C.anchos(ws, {'A': 56, 'B': 20, 'C': 20, 'D': 14, 'E': 18, 'F': 92})
    C.encabezar(ws, 'Suministro a otros minoristas: el árbol del art. 3',
                'Primero la puerta de entrada: esto SÓLO te aplica si '
                'suministras a establecimientos minoristas de DISTINTA '
                'titularidad. Si entras, las tres condiciones son '
                'ACUMULATIVAS, y dentro de «marginal» hay dos vías '
                'ALTERNATIVAS.', col_fin='F')

    refs, fila_listas = C.bloque_listas(
        ws, U['listas'], [('Sí o No', [SI, NO])], col='A')

    def sec(fila, texto):
        C.seccion(ws, 'A%d' % fila, texto)
        for letra in 'BCDEF':
            motor.val(ws, letra + str(fila), '')
            ws[letra + str(fila)].fill = PatternFill('solid',
                                                     fgColor=C.CABECERA)

    def linea(fila, etiqueta, formula=None, fmt=None, nota_txt=None,
              verde=None, pa=None, bold=None):
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True, bold=bold)
        if verde is not None:
            C.entrada(ws, 'B%d' % fila, verde, fmt=fmt, etiqueta=etiqueta,
                      align='center')
        else:
            motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=bold)
        if pa:
            C.nota_celda(ws, 'B%d' % fila, pa)
        if nota_txt:
            C.nota(ws, 'F%d' % fila, nota_txt)
        return 'B%d' % fila

    sec(U['sec_puerta'], 'PUERTA DE ENTRADA: ¿TE APLICA SIQUIERA?')
    linea(U['puerta'],
          '¿Suministras alimentos de producción propia a establecimientos '
          'MINORISTAS de distinta titularidad?', verde=NO, pa='PA-02',
          nota_txt='Si la respuesta es «No», el art. 3 no te aplica y puedes '
                   'saltarte el resto de la hoja. Vender al consumidor final, '
                   'aunque sea por internet y a toda España, NO es suministrar '
                   'a otros minoristas.')
    C.dv_rango(ws, ['B%d' % U['puerta']], refs['Sí o No'], 'Marca Sí o No',
               'Elige «Sí» o «No» de la lista del pie.')
    motor.val(ws, 'A%d' % U['aviso_puerta'], 'Lectura de la puerta de entrada')
    motor.f(ws, 'B%d' % U['aviso_puerta'],
            ie('IF(B{0}="{1}","El art. 3 NO te aplica: nada de lo de abajo te '
               'obliga","Te aplica: sigue con las tres condiciones")'
               .format(U['puerta'], NO)))
    ws.merge_cells('B%d:E%d' % (U['aviso_puerta'], U['aviso_puerta']))

    sec(U['sec_dest'], 'TUS DESTINATARIOS')
    C.cabecera(ws, U['cab'],
               [('A', 'Destinatario'), ('B', 'Kilos a la semana'),
                ('C', '% del volumen anual'), ('D', 'Kilómetros'),
                ('E', '¿Inscrito en el RGSEAA?'), ('F', 'Notas')], altura=26)
    for i, (nombre, kg, pct, km, inscrito) in enumerate(DESTINATARIOS):
        fila = U['ini'] + i
        C.entrada(ws, 'A%d' % fila, nombre, etiqueta='Destinatario %d' % (i + 1))
        C.entrada(ws, 'B%d' % fila, kg, fmt=C.DEC1,
                  etiqueta='Kilos a la semana del destinatario %d' % (i + 1))
        C.entrada(ws, 'C%d' % fila, pct, fmt=C.PCT2,
                  etiqueta='%% del volumen anual del destinatario %d' % (i + 1))
        C.entrada(ws, 'D%d' % fila, km, fmt=C.DEC1,
                  etiqueta='Kilómetros al destinatario %d' % (i + 1))
        C.entrada(ws, 'E%d' % fila, inscrito,
                  etiqueta='RGSEAA del destinatario %d' % (i + 1),
                  align='center')
    C.dv_rango(ws, ['E%d' % (U['ini'] + i) for i in range(len(DESTINATARIOS))],
               refs['Sí o No'], 'Marca Sí o No',
               'Elige «Sí» o «No» de la lista del pie.')
    motor.val(ws, 'A%d' % U['tot'], 'TOTAL', bold=True)
    for letra, fmt in (('B', C.DEC1), ('C', C.PCT2)):
        motor.f(ws, '%s%d' % (letra, U['tot']),
                ie('SUM({0}{1}:{0}{2})'.format(letra, U['ini'], U['fin'])),
                fmt=fmt, bold=True)
    motor.f(ws, 'D%d' % U['tot'],
            ie('MAX(D%d:D%d)' % (U['ini'], U['fin'])), fmt=C.DEC1, bold=True)
    motor.f(ws, 'E%d' % U['tot'],
            ie('COUNTIF(E%d:E%d,"%s")' % (U['ini'], U['fin'], SI)), fmt=C.ENT,
            bold=True)
    C.total_fila(ws, U['tot'], 'ABCDEF')
    C.nota(ws, 'F%d' % U['tot'],
           'Los kilos y el porcentaje se suman; los kilómetros se toman al '
           'MÁXIMO (el destinatario más lejano es el que decide) y en la '
           'última columna se cuentan los que están inscritos en el RGSEAA.')

    sec(U['sec_marg'], 'CONDICIÓN 1 · MARGINAL (dos vías ALTERNATIVAS: basta '
                       'con cumplir una)')
    linea(U['umbral_a'], 'Vía a) · Umbral del volumen anual (%)', verde=0.25,
          fmt=C.PCT, pa='PA-02b',
          nota_txt='«El suministro de alimentos a otros establecimientos de '
                   'comercio al por menor es inferior o igual al 25 % del '
                   'volumen anual de alimentos comercializados».')
    linea(U['tu_pct'], 'Tu porcentaje a otros minoristas',
          ie('C%d' % U['tot']), C.PCT2)
    linea(U['via_a'], '¿Cumples la vía a)?',
          ie('IF(B{0}<=B{1},"{2}","{3}")'
             .format(U['tu_pct'], U['umbral_a'], SI, NO)), bold=True)
    linea(U['umbral_b'],
          'Vía b) · Comercialización TOTAL máxima a la semana (kg)', verde=500,
          fmt=C.ENT, pa='PA-02b',
          nota_txt='«Supone una comercialización total de un máximo de 500 kg '
                   'a la semana, INCLUYENDO el suministro a consumidor final y '
                   'a otros establecimientos de comercio al por menor». Ojo: '
                   'es el total, mostrador incluido, no el B2B solo.')
    linea(U['total_kg'],
          'Lo que comercializas en total a la semana, mostrador incluido (kg)',
          verde=380.0, fmt=C.DEC1,
          nota_txt='SUPUESTO sembrado. Cuéntalo de verdad: es el peso de todo '
                   'lo que sale por la puerta, no sólo lo que va al B2B. Si te '
                   'pasas de 500, la vía b) se cierra y sólo te queda la a).')
    linea(U['via_b'], '¿Cumples la vía b)?',
          ie('IF(B{0}<=B{1},"{2}","{3}")'
             .format(U['total_kg'], U['umbral_b'], SI, NO)), bold=True)
    linea(U['marginal'], '¿ES MARGINAL?',
          ie('IF(OR(B{0}="{2}",B{1}="{2}"),"{2}","{3}")'
             .format(U['via_a'], U['via_b'], SI, NO)), bold=True,
          nota_txt='Basta con cumplir UNA de las dos vías. Un obrador que '
                   'despacha 900 kg a la semana sigue siendo marginal si su '
                   'B2B no llega al 25 %.')
    motor.regla_expresion(ws, 'B%d:B%d' % (U['marginal'], U['marginal']),
                          '=$B$%d="%s"' % (U['marginal'], NO))

    sec(U['sec_loc'], 'CONDICIÓN 2 · LOCALIZADO')
    linea(U['misma_zona'],
          '¿Todos tus destinatarios están en tu unidad sanitaria local, zona de '
          'salud o territorio equivalente, o en una zona limítrofe?', verde=SI,
          pa='PA-02c',
          nota_txt='El texto no habla de kilómetros dentro de la misma '
                   'comunidad: habla de unidad sanitaria local, zona de salud '
                   'o territorio equivalente. Los kilómetros aparecen sólo '
                   'para el comercio ENTRE comunidades autónomas.')
    linea(U['radio'],
          'Radio máximo entre establecimientos de comunidades DISTINTAS (km)',
          verde=50, fmt=C.ENT, pa='PA-02c',
          nota_txt='Y sólo si los registros sanitarios autonómicos de origen y '
                   'destino son públicos y accesibles de forma efectiva.')
    linea(U['max_km'], 'Distancia al destinatario más lejano (km)',
          ie('D%d' % U['tot']), C.DEC1)
    linea(U['otra_ccaa'],
          '¿Alguno de tus destinatarios está en otra comunidad autónoma?',
          verde=NO)
    linea(U['localizado'], '¿ES LOCALIZADO?',
          ie('IF(AND(B{0}="{4}",OR(B{1}="{5}",B{2}<=B{3})),"{4}","{5}")'
             .format(U['misma_zona'], U['otra_ccaa'], U['max_km'], U['radio'],
                     SI, NO)), bold=True)
    motor.regla_expresion(ws, 'B%d:B%d' % (U['localizado'], U['localizado']),
                          '=$B$%d="%s"' % (U['localizado'], NO))
    C.dv_rango(ws, ['B%d' % U['misma_zona'], 'B%d' % U['otra_ccaa']],
               refs['Sí o No'], 'Marca Sí o No',
               'Elige «Sí» o «No» de la lista del pie.')

    sec(U['sec_res'], 'CONDICIÓN 3 · RESTRINGIDO')
    linea(U['inscritos'], 'Destinatarios inscritos en el RGSEAA',
          ie('E%d' % U['tot']), C.ENT, pa='PA-02d',
          nota_txt='«Una actividad se considerará restringida cuando no se '
                   'suministren productos alimenticios a establecimientos '
                   'inscritos en el RGSEAA». Es el requisito que más fácil se '
                   'rompe: basta UN cliente inscrito.')
    linea(U['restringido'], '¿ES RESTRINGIDO?',
          ie('IF(B%d=0,"%s","%s")' % (U['inscritos'], SI, NO)), bold=True)
    motor.regla_expresion(ws, 'B%d:B%d' % (U['restringido'], U['restringido']),
                          '=$B$%d="%s"' % (U['restringido'], NO))

    sec(U['sec_ver'], 'EL VEREDICTO')
    linea(U['cumplidas'], 'Condiciones cumplidas (de tres)',
          ie('COUNTIF(B{0}:B{0},"{3}")+COUNTIF(B{1}:B{1},"{3}")'
             '+COUNTIF(B{2}:B{2},"{3}")'
             .format(U['marginal'], U['localizado'], U['restringido'], SI)),
          C.ENT, bold=True)
    linea(U['veredicto'], 'VEREDICTO',
          ie('IF(B{0}="{4}","El art. 3 no te aplica: no suministras a otros '
             'minoristas de distinta titularidad",IF(B{1}=3,"Cumples las tres: '
             'sigues FUERA del RGSEAA, con la declaración responsable y el '
             'registro del art. 3.5","Te toca inscribirte en el RGSEAA: falla '
             'al menos una de las tres condiciones"))'
             .format(U['puerta'], U['cumplidas'], '', '', NO)), bold=True)
    ws.merge_cells('B%d:E%d' % (U['veredicto'], U['veredicto']))
    ws['B%d' % U['veredicto']].alignment = Alignment(vertical='top', wrap_text=True)
    ws.row_dimensions[U['veredicto']].height = 34
    C.nota_celda(ws, 'B%d' % U['veredicto'], 'PA-02')
    linea(U['ademas'], 'Lo que además tienes que hacer si haces B2B',
          ie('IF(B{0}="{1}","Nada de esto te aplica","Presentar declaración '
             'responsable de que cumples el art. 3 y llevar registro de '
             'destinatarios, cantidades y fechas")'
             .format(U['puerta'], NO)))
    ws.merge_cells('B%d:E%d' % (U['ademas'], U['ademas']))
    ws.row_dimensions[U['ademas']].height = 30
    C.nota_celda(ws, 'B%d' % U['ademas'], 'PA-02d')

    C.parrafo(ws, U['nota'],
              'Las tres condiciones son ACUMULATIVAS: hay que cumplir marginal '
              'Y localizado Y restringido. Lo que es alternativo son las dos '
              'vías DENTRO de «marginal». Y no existe la lectura de que «los '
              '500 kg incluyen el mostrador, así que puedes servir a quien '
              'quieras mientras no llegues a esa cifra»: si te pasas del 25 % '
              'y de los 500 kg dejas de ser marginal, y aunque seas marginal '
              'sigues teniendo que ser localizado y restringido.', 'A', 'F',
              alto=54)
    ws.freeze_panes = 'A4'          # hallazgo B12 (2026-09-10)
    C.pagina(ws, area='A1:F%d' % fila_listas)
    return ws


# ==========================================================================
# Hoja «Ruta Doméstica» (D13)
# ==========================================================================
LISTA_BLANCA = (
    ('a)', 'Comidas preparadas con tratamiento térmico suficiente',
     'Lo que no lleva tratamiento térmico suficiente.'),
    ('b)', 'Productos de panadería y repostería ESTABLES A TEMPERATURA '
           'AMBIENTE',
     'Una tarta rellena de nata NO entra por esta letra: no es estable a '
     'temperatura ambiente. Podría entrar por la e) si tu comunidad la ha '
     'añadido.'),
    ('c)', 'Mermeladas, confituras y jaleas con tratamiento térmico después '
           'del envasado',
     'Las que se envasan en frío.'),
    ('d)', 'Conservas vegetales con pH inferior a 4,5',
     'Las de pH más alto: ahí el riesgo cambia de categoría.'),
    ('e)', 'Otros alimentos que las autoridades competentes de las comunidades '
           'autónomas permitan en sus territorios',
     'Nada por defecto: esta letra está vacía hasta que TU comunidad la '
     'rellene. Una ya lo ha hecho.'),
)
PROHIBICIONES = (
    ('b)', 'Suministro a colectividades y a eventos',
     'INCONDICIONAL: no tiene salvedad autonómica.'),
    ('e)', 'Congelación',
     'Sólo se podrán mantener en congelación las materias primas que se '
     'adquieran ya congeladas.'),
    ('a), c) y d)',
     'Consumo in situ · venta en el propio domicilio · suministro a otros '
     'establecimientos minoristas',
     'Las tres llevan cláusula de escape autonómica: comprueba tu decreto '
     'antes de darlas por prohibidas.'),
)


def hoja_domestica(wb):
    ws = wb.create_sheet(H_DOM)
    C.anchos(ws, {'A': 58, 'B': 22, 'C': 96})
    C.encabezar(ws, 'Ruta doméstica: elaborar en vivienda particular',
                'El art. 13.9 pone TRES obligaciones, no una: un tope de '
                'kilos, la proporcionalidad con el tamaño de las instalaciones '
                'y el «se demostrará documentalmente». El tope casi nunca se '
                'alcanza; el que sí se incumple es el segundo.', col_fin='C')

    refs, fila_listas = C.bloque_listas(
        ws, M['listas'], [('Sí o No', [SI, NO]),
                          ('Comunidad autónoma', CCAA_LISTA)], col='A')

    def sec(fila, texto):
        C.seccion(ws, 'A%d' % fila, texto)
        for letra in 'BC':
            motor.val(ws, letra + str(fila), '')
            ws[letra + str(fila)].fill = PatternFill('solid',
                                                     fgColor=C.CABECERA)

    def linea(fila, etiqueta, formula=None, fmt=None, nota_txt=None,
              verde=None, pa=None, bold=None, coment=None):
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True, bold=bold)
        if verde is not None:
            C.entrada(ws, 'B%d' % fila, verde, fmt=fmt, etiqueta=etiqueta,
                      align='center')
        else:
            motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=bold)
        if pa:
            C.nota_celda(ws, 'B%d' % fila, pa)
        if coment:
            C.comentario(ws, 'B%d' % fila, coment)
        if nota_txt:
            C.nota(ws, 'C%d' % fila, nota_txt)
        ws.row_dimensions[fila].height = 28

    sec(M['sec_datos'], 'TUS DATOS')
    linea(M['m2'], 'Metros cuadrados ÚTILES dedicados a la elaboración',
          verde=12.0, fmt=C.DEC1,
          nota_txt='Útiles de verdad: la superficie de trabajo y el '
                   'almacenamiento dedicados, no los metros de la cocina '
                   'entera si además comes en ella.')
    linea(M['kg'], 'Kilos de producto que elaboras a la semana', verde=60.0,
          fmt=C.DEC1,
          nota_txt='SUPUESTO sembrado. Pésalo durante dos semanas: es el dato '
                   'que decide toda esta hoja y el único que un inspector te '
                   'va a pedir por escrito.')
    linea(M['registro'],
          '¿Llevas un registro documental del volumen que elaboras?', verde=NO,
          nota_txt='Sin él, el art. 13.9 no se cumple aunque el volumen sea '
                   'pequeño: la norma dice literalmente «lo cual se demostrará '
                   'documentalmente».')
    linea(M['amplia'],
          '¿Tu comunidad autónoma ha ampliado la lista del art. 13.8 por la '
          'letra e)?', verde=NO, pa='PA-29b',
          nota_txt='La Comunitat Valenciana ya lo hizo: su Decreto 13/2025 '
                   'pasa la lista de cinco letras a ocho. Lo que NO amplía es '
                   'la refrigeración: la repostería sigue teniendo que ser '
                   'estable a temperatura ambiente.')
    linea(M['ccaa'], 'Tu comunidad autónoma', verde=D.CCAA_EJEMPLO[0])
    C.dv_rango(ws, ['B%d' % M['registro'], 'B%d' % M['amplia']],
               refs['Sí o No'], 'Marca Sí o No',
               'Elige «Sí» o «No» de la lista del pie.')
    C.dv_rango(ws, ['B%d' % M['ccaa']], refs['Comunidad autónoma'],
               'Elige tu comunidad autónoma',
               'Elige una de la lista del pie de la hoja.')

    sec(M['sec_lim'], 'LOS TRES LÍMITES DEL ART. 13.9')
    # Hallazgo B9 (2026-09-10): el tope de 100 kg lo fija la NORMA, no el
    # lector -en el vocabulario del propio producto, «verde» = «campo
    # editable», y aquí el lector podría subirlo a 300 y la hoja le diría
    # «Dentro del tope». D13 no lo lista entre las entradas verdes de esta
    # hoja. Se deja bloqueado y sin relleno verde; el criterio propio de
    # `M['prop']`, un poco más abajo, SÍ es de la casa y sigue en verde.
    motor.val(ws, 'A%d' % M['tope'],
              'Tope absoluto de la norma (kg a la semana)', wrap=True)
    motor.val(ws, 'B%d' % M['tope'], 100, fmt=C.ENT, align='center')
    C.nota_celda(ws, 'B%d' % M['tope'], 'PA-29c')
    C.nota(ws, 'C%d' % M['tope'],
           '«En ningún caso podrán superar los 100 kilogramos semanales». '
           'Son unos 14 kg al día: una cocina doméstica no suele llegar, y '
           'por eso este contador casi siempre está en verde. No te fíes de '
           'eso.')
    ws.row_dimensions[M['tope']].height = 28
    linea(M['sem_tope'], 'Semáforo del tope de kilos',
          ie('IF(B{0}<=B{1},"Dentro del tope","FUERA: el art. 13.9 no lo '
             'permite")'.format(M['kg'], M['tope'])), bold=True)
    # Hallazgo A8 (2026-09-10): sin ISNUMBER, cualquier texto en B[kg] («60
    # kg», «unos 60») es «mayor» que un número en Excel, así que la regla
    # pintaba rojo -«te pasas del tope»- justo en la celda que no tiene un
    # dato numérico válido.
    motor.regla_expresion(ws, 'B%d:B%d' % (M['sem_tope'], M['sem_tope']),
                          '=AND(ISNUMBER($B$%d),ISNUMBER($B$%d),$B$%d>$B$%d)'
                          % (M['kg'], M['tope'], M['kg'], M['tope']))
    linea(M['prop'],
          'Criterio propio de proporcionalidad (kg por m2 útil y semana)',
          verde=8.0, fmt=C.DEC1,
          coment='CRITERIO PROPIO DE LA CASA, no de la norma. El art. 13.9 '
                 'exige que el volumen sea «proporcional al tamaño de las '
                 'instalaciones» pero NO da ningún número, así que aquí se '
                 'propone uno para poder medirlo. Es discutible y lo puedes '
                 'cambiar: lo que no puedes es ignorar el requisito, porque es '
                 'el que de verdad se incumple.',
          nota_txt='La norma no da cifra. Esta sí, y es nuestra: sirve para '
                   'que puedas enseñar un cálculo, no para citarla como si '
                   'fuera legal.')
    linea(M['kg_m2'], 'Tus kilos por metro cuadrado útil y semana',
          ie('IF(B{0}=0,"",B{1}/B{0})'.format(M['m2'], M['kg'])), C.DEC1)
    linea(M['sem_prop'], 'Semáforo de proporcionalidad',
          ie('IF(B{0}="","",IF(B{0}<=B{1},"Proporcional","Revísalo: mucho '
             'volumen para esos metros"))'.format(M['kg_m2'], M['prop'])),
          bold=True)
    motor.regla_expresion(ws, 'B%d:B%d' % (M['sem_prop'], M['sem_prop']),
                          '=AND(ISNUMBER($B$%d),$B$%d>$B$%d)'
                          % (M['kg_m2'], M['kg_m2'], M['prop']),
                          bg=motor.CF_AMBAR_BG, fg=motor.CF_AMBAR_FG)
    linea(M['demostrable'], '¿Lo puedes demostrar documentalmente?',
          ie('IF(B{0}="{1}","Sí","NO: el art. 13.9 exige demostrarlo '
             'documentalmente, y sin eso da igual el volumen")'
             .format(M['registro'], SI)), bold=True, pa='PA-29c')
    motor.regla_expresion(ws, 'B%d:B%d' % (M['demostrable'], M['demostrable']),
                          '=$B$%d<>"%s"' % (M['registro'], SI))

    sec(M['sec_blanca'], 'LA LISTA BLANCA DEL ART. 13.8: CINCO LETRAS')
    C.cabecera(ws, M['cab_blanca'],
               [('A', 'Letra y qué permite'), ('B', ''),
                ('C', 'Qué NO entra por ahí')], altura=22)
    for i, (letra, permite, no_entra) in enumerate(LISTA_BLANCA):
        fila = M['blanca_ini'] + i
        motor.val(ws, 'A%d' % fila, letra + ' ' + permite, wrap=True)
        C.nota(ws, 'C%d' % fila, no_entra)
        ws.row_dimensions[fila].height = 34
    C.nota_celda(ws, 'A%d' % (M['blanca_ini'] + 4), 'PA-29')
    C.parrafo(ws, M['aviso_e'],
              'Por eso NO se puede decir «la tarta de nata desde casa no es '
              'legal en España». Lo correcto es: por defecto el RD 1021/2022 '
              'sólo permite en vivienda repostería estable a temperatura '
              'ambiente, y una tarta rellena de nata no entra en la lista del '
              'art. 13.8 SALVO que tu comunidad la haya añadido por la letra '
              'e). Comprueba tu decreto autonómico.', 'A', 'C', alto=48)

    sec(M['sec_prohib'], 'LAS CINCO PROHIBICIONES DEL ART. 13.5, POR RÉGIMEN')
    C.cabecera(ws, M['cab_prohib'],
               [('A', 'Letra'), ('B', 'Qué prohíbe'), ('C', 'Régimen')],
               altura=22)
    for i, (letra, prohibe, regimen) in enumerate(PROHIBICIONES):
        fila = M['prohib_ini'] + i
        motor.val(ws, 'A%d' % fila, letra, wrap=True)
        motor.val(ws, 'B%d' % fila, prohibe, wrap=True)
        C.nota(ws, 'C%d' % fila, regimen)
        ws.row_dimensions[fila].height = 34
    C.nota_celda(ws, 'A%d' % M['prohib_ini'], 'PA-29')

    sec(M['sec_etiq'], 'ETIQUETA OBLIGATORIA')
    motor.val(ws, 'A%d' % M['etiqueta'],
              'Mención que tienen que llevar los alimentos elaborados en '
              'vivienda', wrap=True)
    motor.val(ws, 'B%d' % M['etiqueta'], 'Elaborado en vivienda particular',
              bold=True)
    C.nota(ws, 'C%d' % M['etiqueta'],
           'Más la fecha de elaboración, y además todo lo que ya exige la '
           'normativa de información alimentaria.')
    C.nota_celda(ws, 'B%d' % M['etiqueta'], 'PA-29d')

    sec(M['sec_val'], 'SI TU COMUNIDAD ES LA COMUNITAT VALENCIANA')
    C.parrafo(ws, M['val1'],
              'El Decreto 13/2025 del Consell amplía la lista de la vivienda '
              'privada a ocho letras: añade confitería, sidra, vino, cerveza y '
              'licores, elaborados de miel, aceite de oliva virgen y otros '
              'elaborados vegetales. Abre además la venta directa EN EL PROPIO '
              'DOMICILIO sin consumo in situ, permite el suministro a otros '
              'establecimientos alimentarios menores con una marginalidad de '
              '100 kg a la semana o el 25 %, y amplía el territorio de reparto '
              'a toda la Comunitat.', 'A', 'C', alto=54)
    C.parrafo(ws, M['val2'],
              'Lo que NO amplía es la refrigeración: la repostería sigue '
              'teniendo que ser estable a temperatura ambiente. Y la '
              'comunicación o declaración responsable es condición para '
              'empezar. Es la prueba de que la letra e) no es teórica.',
              'A', 'C', alto=34)

    sec(M['sec_ver'], 'EL VEREDICTO')
    motor.val(ws, 'A%d' % M['veredicto'],
              'Lectura conjunta de los tres límites', bold=True)
    motor.f(ws, 'B%d' % M['veredicto'],
            ie('IF(B{0}>B{1},"NO: te pasas del tope de kilos del art. 13.9",'
               'IF(B{2}<>"{5}","NO todavía: te falta el registro documental",'
               'IF(AND(ISNUMBER(B{3}),B{3}>B{4}),"Cuidado: dentro del tope, '
               'pero mucho volumen para esos metros","Dentro de los tres '
               'límites, con la lista del art. 13.8 por delante")))'
               .format(M['kg'], M['tope'], M['registro'], M['kg_m2'],
                       M['prop'], SI)), bold=True)
    ws.merge_cells('B%d:C%d' % (M['veredicto'], M['veredicto']))
    ws['B%d' % M['veredicto']].alignment = Alignment(vertical='top', wrap_text=True)
    ws.row_dimensions[M['veredicto']].height = 34
    C.parrafo(ws, M['nota'],
              'Estar dentro de los tres límites del art. 13.9 no basta por sí '
              'solo: lo que elabores tiene que estar además en la lista del '
              'art. 13.8, y no puedes hacer nada de lo que prohíbe el 13.5. '
              'Esta hoja es para decidir si la ruta doméstica es viable para '
              'ti, no para sustituir la consulta a tu comunidad autónoma.',
              'A', 'C', alto=42)
    ws.freeze_panes = 'A4'          # hallazgo B12 (2026-09-10)
    C.pagina(ws, apaisado=False, area='A1:C%d' % fila_listas)
    return ws


# ==========================================================================
# Hoja «Registro de Formación»
# ==========================================================================
FORMACION = (
    'Higiene alimentaria y buenas prácticas de manipulación',
    'Higiene alimentaria, alérgenos y contaminación cruzada',
    'Higiene alimentaria básica',
    'Higiene alimentaria y alérgenos en la venta al público',
    'Higiene alimentaria y alérgenos en la venta al público',
)


def hoja_formacion(wb):
    ws = wb.create_sheet(H_FOR)
    C.anchos(ws, {'A': 30, 'B': 24, 'C': 52, 'D': 9, 'E': 15, 'F': 15,
                  'G': 14, 'H': 78})
    C.encabezar(ws, 'Registro de formación de manipuladores',
                'El «carnet de manipulador de alimentos» NO existe desde 2010. '
                'Lo que hay que tener es este registro, y la responsabilidad '
                'de tenerlo es de la empresa, no del trabajador.', col_fin='H')
    C.cabecera(ws, R_CAB,
               [('A', 'Persona'), ('B', 'Perfil'),
                ('C', 'Contenido de la formación'), ('D', 'Horas'),
                ('E', 'Fecha de la formación'), ('F', 'Caduca el'),
                ('G', 'Días restantes'), ('H', 'Notas')])
    for i, (pid, perfil, _j, _g, area, _h, _t) in enumerate(D.PLANTILLA):
        fila = R_INI + i
        motor.val(ws, 'A%d' % fila, pid + ' · ' + perfil)
        motor.val(ws, 'B%d' % fila, area)
        C.entrada(ws, 'C%d' % fila, FORMACION[i], etiqueta=perfil)
        C.entrada(ws, 'D%d' % fila, 6, fmt=C.ENT, etiqueta=perfil,
                  align='center')
        C.entrada(ws, 'E%d' % fila, FECHA_BASE, fmt=C.FECHA, etiqueta=perfil)
        motor.f(ws, 'F%d' % fila,
                ie('IF(E{0}="","",E{0}+$B${1})'.format(fila, R_VALIDEZ)),
                fmt=C.FECHA)
        motor.f(ws, 'G%d' % fila,
                ie('IF(F{0}="","",F{0}-$B${1})'.format(fila, R_CONTROL)),
                fmt=C.ENT)
    motor.semaforo_isnumber(ws, 'G%d:G%d' % (R_INI, R_FIN), '$G%d' % R_INI,
                            operador='<', umbral='0')
    C.nota(ws, 'H%d' % R_INI,
           'El contenido y las horas son SUPUESTOS: los pone quien te dé la '
           'formación. Lo que no es supuesto es que tiene que quedar por '
           'escrito y con nombre y apellidos.')

    C.seccion(ws, 'A%d' % R_SEC_PAR, 'PARÁMETROS DE LA CASA')
    for letra in 'BCDEFGH':
        motor.val(ws, letra + str(R_SEC_PAR), '')
        ws[letra + str(R_SEC_PAR)].fill = PatternFill('solid',
                                                      fgColor=C.CABECERA)
    motor.val(ws, 'A%d' % R_VALIDEZ,
              'Validez interna de la formación (días)')
    C.entrada(ws, 'B%d' % R_VALIDEZ, 730, fmt=C.ENT,
              etiqueta='Validez interna de la formación')
    C.comentario(ws, 'B%d' % R_VALIDEZ,
                 'CRITERIO PROPIO DE LA CASA. La norma no fija caducidad para '
                 'la formación: lo que exige es que la formación sea adecuada '
                 'y demostrable. Dos años es un plazo razonable para repasarla '
                 'y dejar constancia; ponlo en lo que tú decidas y cúmplelo.')
    C.nota(ws, 'H%d' % R_VALIDEZ,
           'No es un plazo legal: es tu propia política, y tenerla escrita es '
           'lo que la hace defendible.')
    motor.val(ws, 'A%d' % R_CONTROL, 'Fecha de control')
    C.entrada(ws, 'B%d' % R_CONTROL, FECHA_BASE, fmt=C.FECHA,
              etiqueta='Fecha de control')
    C.nota(ws, 'H%d' % R_CONTROL,
           'Cámbiala por la de hoy cada vez que revises la hoja.')

    C.seccion(ws, 'A%d' % R_SEC_RES, 'RESUMEN')
    for letra in 'BCDEFGH':
        motor.val(ws, letra + str(R_SEC_RES), '')
        ws[letra + str(R_SEC_RES)].fill = PatternFill('solid',
                                                      fgColor=C.CABECERA)
    motor.val(ws, 'A%d' % R_CON, 'Personas con formación registrada')
    motor.f(ws, 'B%d' % R_CON,
            ie('COUNTIF(E%d:E%d,">0")' % (R_INI, R_FIN)), fmt=C.ENT)
    motor.val(ws, 'A%d' % R_CADUCADAS, 'Formaciones caducadas')
    motor.f(ws, 'B%d' % R_CADUCADAS,
            ie('COUNTIF(G%d:G%d,"<0")' % (R_INI, R_FIN)), fmt=C.ENT)
    motor.semaforo_isnumber(ws, 'B%d:B%d' % (R_CADUCADAS, R_CADUCADAS),
                            '$B$%d' % R_CADUCADAS, operador='>', umbral='0')
    motor.val(ws, 'A%d' % R_PROXIMAS,
              'Formaciones que caducan en menos de 90 días')
    motor.f(ws, 'B%d' % R_PROXIMAS,
            ie('COUNTIF(G{0}:G{1},"<90")-B{2}'
               .format(R_INI, R_FIN, R_CADUCADAS)), fmt=C.ENT)
    C.nota(ws, 'H%d' % R_PROXIMAS,
           'Los 90 días son un aviso propio para que te dé tiempo a organizar '
           'la sesión sin parar el obrador.')
    C.parrafo(ws, R_NOTA,
              'El «carnet de manipulador de alimentos» no existe desde 2010: '
              'lo derogó el RD 109/2010 al suprimir el RD 202/2000. Lo que '
              'obliga hoy es el Reglamento (CE) 852/2004, que exige que los '
              'manipuladores estén supervisados e instruidos en materia de '
              'higiene alimentaria de forma proporcionada a su cometido, y esa '
              'responsabilidad es de la EMPRESA. Guarda el temario, la '
              'duración, la fecha y quién la impartió: eso es lo que se '
              'enseña en una inspección.', 'A', 'H', alto=54)
    C.nota_celda(ws, 'A%d' % R_NOTA, 'PA-11')
    C.pagina(ws, titulos='$%d:$%d' % (R_CAB, R_CAB), area='A1:H%d' % R_NOTA)
    return ws


# ==========================================================================
# Hoja «Cronograma y Ruta Crítica» (absorbida, D3)
# ==========================================================================
SIN_DEP = '-'
FMT_CENTINELA = '[=999]"";0.0'
NOTAS_GANTT = {
    'H1': 'La búsqueda es lo único que puedes acelerar tú solo, y es donde se '
          'deciden la salida de humos y la potencia eléctrica: mira la ficha '
          'de visita del libro de capacidad ANTES de enamorarte de un local.',
    'H4': 'Depende de tu ayuntamiento. Es el hito con más varianza de todo el '
          'cuadro, y por eso lo que se negocia es empezar a pedir el '
          'equipamiento en paralelo.',
    'H6': 'Va en PARALELO a la obra porque depende del proyecto, no de la '
          'licencia. Es lo que le da holgura: si la pides tarde, esa holgura '
          'desaparece y el equipamiento pasa a mandar sobre la apertura.',
    'H12': 'Duración cero: la apertura es un instante, no una tarea. Lo que '
           'tiene delante son las pruebas de producción, y ésas no se '
           'recortan.',
}


def hoja_gantt(wb):
    ws = wb.create_sheet(H_GAN)
    C.anchos(ws, dict([('A', 8), ('B', 52)]
                      + [(c, 11) for c in COLS_MAT] + [('O', 82)]))
    C.encabezar(ws, 'Cronograma y ruta crítica de la apertura',
                'Doce hitos con su duración y sus dependencias. La hoja '
                'calcula cuándo empieza y acaba cada uno, cuánta holgura '
                'tiene, cuáles están en la ruta crítica y en qué mes acabas '
                'abriendo. Todo en MESES y con aritmética de índices: no hay '
                'ni una función de fecha.', col_fin='O')

    refs, fila_listas = C.bloque_listas(
        ws, G_LISTAS,
        [('Hitos y «sin dependencia»', [SIN_DEP] + [h[0] for h in D.GANTT]),
         ('Meses del año', list(D.MESES))], col='A')
    ref_meses = refs['Meses del año']

    motor.val(ws, 'A%d' % G_ARRANQUE, 'Mes en que arranca el proyecto (1-12)')
    ws.merge_cells('A%d:B%d' % (G_ARRANQUE, G_ARRANQUE))
    C.entrada(ws, 'C%d' % G_ARRANQUE, D.MES_INICIO_PROYECTO, fmt=C.ENT,
              etiqueta='Mes de arranque del proyecto', align='center')
    C.nota(ws, 'O%d' % G_ARRANQUE,
           'El mes natural en el que das el primer paso. De aquí sale la fecha '
           'de apertura estimada, y por eso conviene probar dos o tres: mover '
           'el arranque dos meses puede sacarte de una campaña o meterte en '
           'ella.')
    motor.val(ws, 'A%d' % G_CENTINELA,
              'Valor centinela de la matriz de dependencias (meses)')
    ws.merge_cells('A%d:B%d' % (G_CENTINELA, G_CENTINELA))
    # Hallazgo A7 (2026-09-10): 999 es una constante de implementación (un
    # truco para que MIN() ignore las celdas que no aplican), no un dato del
    # lector. En verde invitaba a tocarla: si el lector escribe ahí un 3, las
    # once holguras y la ruta crítica cambian sin un solo aviso. Se deja
    # bloqueada y sin relleno verde.
    motor.val(ws, 'C%d' % G_CENTINELA, 999, fmt=C.ENT, align='center')
    C.nota(ws, 'O%d' % G_CENTINELA,
           'Truco de cálculo, no un dato: en la matriz de dependencias las '
           'casillas que no aplican llevan este número en vez de quedarse '
           'vacías, para que MIN pueda trabajar sólo con números. El formato '
           'de la matriz lo esconde. No lo cambies salvo que tu proyecto dure '
           'más de 999 meses.')

    C.cabecera(ws, G_CAB,
               [('A', 'Id'), ('B', 'Hito'), ('C', 'Duración (meses)'),
                ('D', 'Depende de (1)'), ('E', 'Depende de (2)'),
                ('F', 'Depende de (3)'), ('G', 'Empieza (mes del proyecto)'),
                ('H', 'Acaba (mes del proyecto)'), ('I', 'Holgura (meses)'),
                ('J', '¿Ruta crítica?'), ('K', 'Mes natural de fin'),
                ('L', ''), ('M', ''), ('N', ''), ('O', 'Notas')])

    fila_de = {}
    for i, (hid, hito, dur, deps) in enumerate(D.GANTT):
        fila_de[hid] = G_INI + i
    deps_coords = []
    for i, (hid, hito, dur, deps) in enumerate(D.GANTT):
        fila = G_INI + i
        motor.val(ws, 'A%d' % fila, hid, align='center')
        motor.val(ws, 'B%d' % fila, hito, wrap=True)
        C.entrada(ws, 'C%d' % fila, dur, fmt=C.DEC1,
                  etiqueta='Duración de ' + hid, align='center')
        lista = list(deps) + [SIN_DEP] * (3 - len(deps))
        for j, letra in enumerate(('D', 'E', 'F')):
            C.entrada(ws, '%s%d' % (letra, fila), lista[j],
                      etiqueta='Dependencia %d de %s' % (j + 1, hid),
                      align='center')
            deps_coords.append('%s%d' % (letra, fila))
        arriba = fila - 1
        trozos = []
        for letra in ('D', 'E', 'F'):
            trozos.append('IFERROR(INDEX($H$%d:H%d,MATCH(%s%d,$A$%d:A%d,0)),0)'
                          % (G_CAB, arriba, letra, fila, G_CAB, arriba))
        motor.f(ws, 'G%d' % fila, ie('MAX(%s)' % ','.join(trozos)), fmt=C.DEC1)
        motor.f(ws, 'H%d' % fila, ie('G%d+C%d' % (fila, fila)), fmt=C.DEC1)
        if hid in NOTAS_GANTT:
            C.nota(ws, 'O%d' % fila, NOTAS_GANTT[hid])
        ws.row_dimensions[fila].height = 26
    C.dv_rango(ws, deps_coords, refs['Hitos y «sin dependencia»'],
               'Elige un hito o «-»',
               'Escribe el identificador de otro hito, o «-» si este hito no '
               'depende de ninguno. Sólo puede depender de hitos que estén '
               'MÁS ARRIBA en la tabla.')

    # --- matriz de dependencias -------------------------------------------
    C.seccion(ws, 'A%d' % G_SEC_MAT,
              'MATRIZ DE DEPENDENCIAS: QUÉ HITO BLOQUEA A CUÁL')
    for letra in list('B') + list(COLS_MAT) + ['O']:
        motor.val(ws, letra + str(G_SEC_MAT), '')
        ws[letra + str(G_SEC_MAT)].fill = PatternFill('solid',
                                                      fgColor=C.CABECERA)
    C.cabecera(ws, G_MAT_CAB,
               [('A', 'Sucesor'), ('B', 'empieza en el mes...')]
               + [(COLS_MAT[k], D.GANTT[k][0]) for k in range(len(D.GANTT))]
               + [('O', 'Notas')], altura=22)
    for i, (hid, hito, dur, deps) in enumerate(D.GANTT):
        fila = G_MAT_INI + i
        fila_h = G_INI + i
        motor.val(ws, 'A%d' % fila, hid, align='center')
        motor.f(ws, 'B%d' % fila, ie('G%d' % fila_h), fmt=C.DEC1)
        for k in range(len(D.GANTT)):
            fila_pred = G_INI + k
            motor.f(ws, '%s%d' % (COLS_MAT[k], fila),
                    ie('IF(OR($D${0}=$A${1},$E${0}=$A${1},$F${0}=$A${1}),'
                       '$G${0},$C${2})'
                       .format(fila_h, fila_pred, G_CENTINELA)),
                    fmt=FMT_CENTINELA)
    C.nota(ws, 'O%d' % G_MAT_INI,
           'Se lee por COLUMNAS: en la columna de H5 aparece el mes en que '
           'empieza cada hito que depende de H5. La holgura de H5 es la '
           'distancia entre cuando acaba y el primero de esos meses. Las '
           'casillas vacías no lo están: llevan el centinela y el formato las '
           'esconde.')

    for i, (hid, hito, dur, deps) in enumerate(D.GANTT):
        fila_h = G_INI + i
        col = COLS_MAT[i]
        rango = '%s%d:%s%d' % (col, G_MAT_INI, col, G_MAT_FIN)
        motor.f(ws, 'I%d' % fila_h,
                ie('MIN(MIN({0}),MAX($H${1}:$H${2}))-H{3}'
                   .format(rango, G_INI, G_FIN, fila_h)), fmt=C.DEC1)
        motor.f(ws, 'J%d' % fila_h,
                ie('IF(ROUND(I{0},3)<=0,"{1}","{2}")'.format(fila_h, SI, NO)))
        motor.f(ws, 'K%d' % fila_h,
                ie('INDEX({0},ROUNDDOWN(MOD($C${1}-1+H{2},12),0)+1)'
                   .format(ref_meses, G_ARRANQUE, fila_h)))
    motor.regla_expresion(ws, 'J%d:J%d' % (G_INI, G_FIN),
                          '=$J%d="%s"' % (G_INI, SI),
                          bg=motor.CF_AMBAR_BG, fg=motor.CF_AMBAR_FG)

    # --- resultados --------------------------------------------------------
    C.seccion(ws, 'A%d' % G_SEC_RES, 'LO QUE SALE DE TODO ESTO')
    for letra in list('B') + list(COLS_MAT) + ['O']:
        motor.val(ws, letra + str(G_SEC_RES), '')
        ws[letra + str(G_SEC_RES)].fill = PatternFill('solid',
                                                      fgColor=C.CABECERA)

    def res(fila, etiqueta, formula, fmt=None, nota_txt=None, bold=None):
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True, bold=bold)
        ws.merge_cells('A%d:B%d' % (fila, fila))
        motor.f(ws, 'C%d' % fila, formula, fmt=fmt, bold=bold)
        if nota_txt:
            C.nota(ws, 'O%d' % fila, nota_txt)

    res(G_DURACION, 'Duración total del proyecto (meses)',
        ie('MAX(H%d:H%d)' % (G_INI, G_FIN)), C.DEC1, bold=True,
        nota_txt='Desde el primer día de búsqueda hasta el día que abres la '
                 'puerta. No incluye lo que tardes en decidirte.')
    res(G_CRITICOS, 'Hitos SIN holgura (ruta crítica)',
        ie('COUNTIF(J%d:J%d,"%s")' % (G_INI, G_FIN, SI)), C.ENT,
        nota_txt='Los que si se retrasan un día retrasan la apertura un día. '
                 'Son los únicos que hay que vigilar a diario; los demás '
                 'tienen colchón, y saber cuáles son te ahorra media úlcera. '
                 'Cuenta TODOS los de holgura cero, que son más que los del '
                 'camino más largo: dos hitos en paralelo de la misma duración '
                 'no tienen holgura ninguno de los dos.')
    res(G_MES_AP, 'Mes natural en el que abres (1-12)',
        ie('ROUNDDOWN(MOD($C${0}-1+C{1},12),0)+1'
           .format(G_ARRANQUE, G_DURACION)), C.ENT, bold=True)
    res(G_NOMBRE_MES, 'Nombre de ese mes',
        ie('INDEX(%s,C%d)' % (ref_meses, G_MES_AP)), None, bold=True)
    res(G_EN_PICO, '¿Esa apertura cae dentro de una campaña?',
        ie('IF(COUNTIF($C${0}:$C${1},C{2})>0,"{3}","{4}")'
           .format(G_PICOS_INI, G_PICOS_FIN, G_MES_AP, SI, NO)))
    res(G_AVISO, 'Aviso',
        ie('IF(C{0}="{1}","Abres DENTRO de una campaña: el equipo estrena '
           'obrador el mes de más carga del año, y eso se paga en mermas y en '
           'encargos que no salen","Abres fuera de campaña: tienes rodaje '
           'antes del siguiente pico")'.format(G_EN_PICO, SI)), bold=True)
    ws.merge_cells('C%d:N%d' % (G_AVISO, G_AVISO))
    ws['C%d' % G_AVISO].alignment = Alignment(vertical='top', wrap_text=True)
    ws.row_dimensions[G_AVISO].height = 30
    motor.regla_expresion(ws, 'C%d:C%d' % (G_EN_PICO, G_EN_PICO),
                          '=$C$%d="%s"' % (G_EN_PICO, SI),
                          bg=motor.CF_AMBAR_BG, fg=motor.CF_AMBAR_FG)

    C.seccion(ws, 'A%d' % G_SEC_PICOS, 'LAS SEIS CAMPAÑAS DEL AÑO')
    for letra in list('B') + list(COLS_MAT) + ['O']:
        motor.val(ws, letra + str(G_SEC_PICOS), '')
        ws[letra + str(G_SEC_PICOS)].fill = PatternFill('solid',
                                                        fgColor=C.CABECERA)
    C.cabecera(ws, G_PICOS_CAB,
               [('A', 'Campaña'), ('B', 'Fechas'), ('C', 'Mes'),
                ('D', 'Días de campaña'),
                ('E', 'Multiplicador de producción'), ('O', 'Notas')],
               altura=24)
    for i, pico in enumerate(D.PICOS):
        fila = G_PICOS_INI + i
        motor.val(ws, 'A%d' % fila, pico['nombre'])
        motor.val(ws, 'B%d' % fila, pico['fechas'])
        C.entrada(ws, 'C%d' % fila, pico['mes'], fmt=C.ENT,
                  etiqueta='Mes de ' + pico['nombre'], align='center')
        motor.val(ws, 'D%d' % fila, pico['dias_campana'], fmt=C.ENT,
                  align='center')
        motor.val(ws, 'E%d' % fila, pico['factor_obrador'], fmt=C.DEC1,
                  align='center')
    C.nota(ws, 'O%d' % G_PICOS_INI,
           'Los euros de cada campaña y si tu equipo aguanta el multiplicador '
           'están en el libro «estacionalidad-y-picos». Aquí sólo se usan los '
           'meses, para avisarte de si vas a abrir en mitad de una.')

    C.parrafo(ws, G_NOTA,
              'Las duraciones son SUPUESTOS y casi todas dependen de un '
              'tercero. Cámbialas por las tuyas en cuanto tengas un plazo por '
              'escrito, empezando por el del equipamiento: es el que más '
              'silenciosamente mueve la fecha de apertura, porque no falla, '
              'sólo llega tarde. La hoja no usa funciones de fecha a '
              'propósito: trabaja en meses decimales, así que medio mes es '
              '0,5 y se puede sumar sin discutir con el calendario laboral.',
              'A', 'O', alto=54)
    ws.freeze_panes = 'C%d' % (G_CAB + 1)
    C.pagina(ws, titulos='$%d:$%d' % (G_CAB, G_CAB),
             area='A1:O%d' % fila_listas)
    return ws


# ==========================================================================
# Mapa de celdas citables
# ==========================================================================
def mapa():
    m = [
        ('Trámites del expediente', H_CHK, 'D%d' % K_TOTAL, 'salida'),
        ('Trámites hechos', H_CHK, 'D%d' % K_HECHOS, 'salida'),
        ('Avance del expediente', H_CHK, 'D%d' % K_AVANCE, 'salida'),
        ('Coste previsto total del checklist', H_CHK, 'D%d' % K_PREV,
         'salida'),
        ('Trámites sin importe conocido', H_CHK, 'D%d' % K_SINIMP, 'salida'),
        ('Trámites que cambian según la comunidad autónoma', H_CHK,
         'D%d' % K_CCAA, 'salida'),
    ]
    for fase, titulo, sec, ini, fin, cont, items in FASES:
        m.append(('Trámites de la fase %s' % fase, H_CHK, 'E%d' % cont,
                  'salida'))
        m.append(('Coste previsto de la fase %s del checklist' % fase, H_CHK,
                  'F%d' % cont, 'salida'))
        m.append(('Avance de la fase %s' % fase, H_CHK, 'J%d' % cont,
                  'salida'))
    m += [
        ('Coste del proyecto técnico visado', H_CHK,
         'F%d' % (FASES[1][3] + 3), 'entrada'),
        ('Coste de la licencia de actividad o declaración responsable', H_CHK,
         'F%d' % FASES[2][3], 'entrada'),
        ('Coste de la comunicación al registro sanitario autonómico', H_CHK,
         'F%d' % FASES[4][3], 'entrada'),
        # --- árbol de registro sanitario ----------------------------------
        ('Régimen de registro sanitario que te toca', H_ARB,
         'B%d' % A['regimen'], 'salida'),
        ('Trámite concreto del registro sanitario', H_ARB,
         'B%d' % A['tramite'], 'salida'),
        ('La comunicación autonómica habilita para abrir', H_ARB,
         'B%d' % A['habilita'], 'salida'),
        ('Plazo del registro sanitario en la comunidad de ejemplo', H_ARB,
         'B%d' % A['plazo'], 'salida'),
        # --- suministro a otros minoristas --------------------------------
        ('Puerta de entrada del art. 3', H_SUM, 'B%d' % U['puerta'],
         'entrada'),
        ('Lectura de la puerta de entrada del art. 3', H_SUM,
         'B%d' % U['aviso_puerta'], 'salida'),
        ('Kilos a la semana servidos a otros minoristas', H_SUM,
         'B%d' % U['tot'], 'salida'),
        ('Porcentaje del volumen anual servido a otros minoristas', H_SUM,
         'C%d' % U['tot'], 'salida'),
        ('Umbral de la vía a) del art. 3.2', H_SUM, 'B%d' % U['umbral_a'],
         'parametro'),
        ('Cumple la vía a) del art. 3.2', H_SUM, 'B%d' % U['via_a'], 'salida'),
        ('Umbral de la vía b) del art. 3.2', H_SUM, 'B%d' % U['umbral_b'],
         'parametro'),
        ('Comercialización total a la semana', H_SUM, 'B%d' % U['total_kg'],
         'entrada'),
        ('Cumple la vía b) del art. 3.2', H_SUM, 'B%d' % U['via_b'], 'salida'),
        ('Semáforo de marginal', H_SUM, 'B%d' % U['marginal'], 'salida'),
        ('Radio máximo entre comunidades autónomas', H_SUM,
         'B%d' % U['radio'], 'parametro'),
        ('Semáforo de localizado', H_SUM, 'B%d' % U['localizado'], 'salida'),
        ('Destinatarios inscritos en el RGSEAA', H_SUM, 'B%d' % U['inscritos'],
         'salida'),
        ('Semáforo de restringido', H_SUM, 'B%d' % U['restringido'], 'salida'),
        ('Condiciones del art. 3 cumplidas', H_SUM, 'B%d' % U['cumplidas'],
         'salida'),
        ('Veredicto del art. 3', H_SUM, 'B%d' % U['veredicto'], 'salida'),
        ('Papeles añadidos del art. 3.5', H_SUM, 'B%d' % U['ademas'],
         'salida'),
        # --- ruta doméstica ------------------------------------------------
        ('Metros útiles de la ruta doméstica', H_DOM, 'B%d' % M['m2'],
         'entrada'),
        ('Kilos a la semana de la ruta doméstica', H_DOM, 'B%d' % M['kg'],
         'entrada'),
        ('Tope absoluto del art. 13.9', H_DOM, 'B%d' % M['tope'], 'parametro'),
        ('Semáforo del tope de 100 kg', H_DOM, 'B%d' % M['sem_tope'],
         'salida'),
        ('Criterio propio de proporcionalidad', H_DOM, 'B%d' % M['prop'],
         'parametro'),
        ('Kilos por metro cuadrado útil y semana', H_DOM, 'B%d' % M['kg_m2'],
         'salida'),
        ('Semáforo de proporcionalidad', H_DOM, 'B%d' % M['sem_prop'],
         'salida'),
        ('Aviso de demostrable documentalmente', H_DOM,
         'B%d' % M['demostrable'], 'salida'),
        ('Mención obligatoria de la etiqueta doméstica', H_DOM,
         'B%d' % M['etiqueta'], 'parametro'),
        ('Veredicto de la ruta doméstica', H_DOM, 'B%d' % M['veredicto'],
         'salida'),
        # --- registro de formación -----------------------------------------
        ('Validez interna de la formación', H_FOR, 'B%d' % R_VALIDEZ,
         'parametro'),
        ('Personas con formación registrada', H_FOR, 'B%d' % R_CON, 'salida'),
        ('Formaciones caducadas', H_FOR, 'B%d' % R_CADUCADAS, 'salida'),
        ('Caducidad de la formación del Jefe Pastelero', H_FOR,
         'F%d' % R_INI, 'salida'),
        # --- cronograma ------------------------------------------------------
        ('Mes de arranque del proyecto', H_GAN, 'C%d' % G_ARRANQUE, 'entrada'),
        ('Duración total del proyecto en meses', H_GAN, 'C%d' % G_DURACION,
         'salida'),
        ('Hitos sin holgura en la ruta crítica', H_GAN, 'C%d' % G_CRITICOS,
         'salida'),
        ('Mes natural de la apertura', H_GAN, 'C%d' % G_MES_AP, 'salida'),
        ('Nombre del mes de la apertura', H_GAN, 'C%d' % G_NOMBRE_MES,
         'salida'),
        ('La apertura cae dentro de una campaña', H_GAN, 'C%d' % G_EN_PICO,
         'salida'),
        ('Aviso de la fecha de apertura', H_GAN, 'C%d' % G_AVISO, 'salida'),
    ]
    for i, (hid, hito, dur, deps) in enumerate(D.GANTT):
        fila = G_INI + i
        m.append(('Duración del hito %s' % hid, H_GAN, 'C%d' % fila,
                  'entrada'))
        m.append(('Fin del hito %s (mes del proyecto)' % hid, H_GAN,
                  'H%d' % fila, 'salida'))
        m.append(('Holgura del hito %s' % hid, H_GAN, 'I%d' % fila, 'salida'))
        m.append(('El hito %s está en la ruta crítica' % hid, H_GAN,
                  'J%d' % fila, 'salida'))
    return m


NOTAS_MAPA = (
    'Libro legal y de cronograma. Los tres árboles se leen en cadena: la hoja '
    '«Árbol de Registro Sanitario» toma su veredicto de «Suministro a Otros '
    'Minoristas» cuando hay B2B. Las cuatro comunidades autónomas son EJEMPLOS '
    'declarados (D27). El criterio de proporcionalidad de la ruta doméstica y '
    'la caducidad de la formación son CRITERIOS PROPIOS DE LA CASA, no normas: '
    'están así marcados en el comentario de su celda y no se pueden citar como '
    'obligación legal. Todo lo normativo lleva su nota «Verificado el '
    '10-09-2026 · norma y artículo · URL».'
)


# ==========================================================================
# Demos con pycel
# ==========================================================================
def demo(ruta):
    exc = C.compilador(ruta)
    pruebas = []

    def ev(ref):
        return exc.evaluate(ref)

    r_puerta = "'%s'!B%d" % (H_SUM, U['puerta'])
    r_veredicto = "'%s'!B%d" % (H_SUM, U['veredicto'])
    r_kg = "'%s'!B%d" % (H_DOM, M['kg'])
    r_sem_tope = "'%s'!B%d" % (H_DOM, M['sem_tope'])
    r_dur = "'%s'!C%d" % (H_GAN, G_DURACION)
    r_mes = "'%s'!C%d" % (H_GAN, G_MES_AP)

    # 1. el cronograma reproduce la ruta crítica del juego de datos
    total, camino, holgura = D.ruta_critica()
    pruebas.append(('La ruta crítica del cronograma cuadra con el juego de '
                    'datos', abs(ev(r_dur) - total) < 0.001,
                    'libro %.2f meses vs datos_ejemplo %.2f' % (ev(r_dur),
                                                                total)))
    # 2. la holgura por hito coincide una a una
    malas = []
    for i, (hid, _h, _d, _deps) in enumerate(D.GANTT):
        v = ev("'%s'!I%d" % (H_GAN, G_INI + i))
        if abs(v - holgura[hid]) > 0.001:
            malas.append('%s: libro %.2f vs %.2f' % (hid, v, holgura[hid]))
    pruebas.append(('La holgura de los doce hitos coincide con el cálculo de '
                    'referencia', not malas, malas[0] if malas
                    else 'los 12 hitos cuadran; %d en la ruta crítica'
                    % len(camino)))
    # 3. el mes de apertura es el que dice el juego de datos
    pruebas.append(('El mes natural de apertura es el del juego de datos',
                    ev(r_mes) == D.mes_apertura_calculado(),
                    'libro %s vs datos_ejemplo %s'
                    % (ev(r_mes), D.mes_apertura_calculado())))
    # 4. el semáforo de los 100 kg no se enciende con un valor dentro
    pruebas.append(('El semáforo del tope de kilos lee «dentro» con el valor '
                    'sembrado', ev(r_sem_tope) == 'Dentro del tope',
                    'devuelve %r con %s kg' % (ev(r_sem_tope), ev(r_kg))))
    # 5. sin B2B, el art. 3 no aplica; con B2B y tres condiciones, sí cumple
    pruebas.append(('Sin B2B el veredicto del art. 3 dice que no te aplica',
                    'no te aplica' in ev(r_veredicto),
                    'devuelve %r' % (ev(r_veredicto),)))
    # 6. el contador del checklist responde a la casilla
    otro = C.compilador(ruta)
    r_avance = "'%s'!D%d" % (H_CHK, K_AVANCE)
    r_hechos = "'%s'!D%d" % (H_CHK, K_HECHOS)
    base = otro.evaluate(r_hechos)
    # pycel sólo deja escribir en una celda que ya esté en su mapa: hay que
    # evaluarla antes de tocarla.
    otro.evaluate("'%s'!A%d" % (H_CHK, K_INI))
    otro.set_value("'%s'!A%d" % (H_CHK, K_INI), HECHO)
    despues = otro.evaluate(r_hechos)
    pruebas.append(('Marcar una casilla mueve el contador y el avance',
                    despues == base + 1,
                    'de %s a %s trámites hechos; avance inicial %.4f'
                    % (base, despues, exc.evaluate(r_avance))))
    # 7. el veredicto del art. 3 cambia al abrir la puerta de entrada
    tercero = C.compilador(ruta)
    tercero.evaluate(r_veredicto)
    tercero.evaluate(r_puerta)
    tercero.set_value(r_puerta, SI)
    con_b2b = tercero.evaluate(r_veredicto)
    pruebas.append(('Al declarar B2B el veredicto del art. 3 pasa a evaluar '
                    'las tres condiciones', 'no te aplica' not in con_b2b,
                    'devuelve %r' % (con_b2b,)))
    return pruebas


def main():
    D.gate_legal()
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_checklist(wb)
    hoja_arbol(wb)
    hoja_suministro(wb)
    hoja_domestica(wb)
    hoja_formacion(wb)
    hoja_gantt(wb)
    res = C.cerrar(wb, NOMBRE, TITULO, mapa(), NOTAS_MAPA)
    C.resumen(NOMBRE, res, demo(res['ruta']))


if __name__ == '__main__':
    main()
