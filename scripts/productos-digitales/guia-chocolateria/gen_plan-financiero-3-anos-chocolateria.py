#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_plan-financiero-3-anos-chocolateria.py — libro 7 de «Cómo Montar una
Chocolatería» (SPEC §2.2, fila 7; constructor C4, que va solo).

Hojas (ONCE): Instrucciones · 0. Supuestos · Inversión Inicial · PyG 3 Años ·
Punto de Equilibrio · Escenarios · Personal · Tesorería 12 meses ·
Financiación · Canales y Punto Muerto · Talleres y Regalo Corporativo.

QUÉ DECIDE ESTE LIBRO
---------------------
Si el negocio se sostiene, qué canal lo sostiene y si el taller da dinero o te
ocupa el obrador en el peor momento. Es la FUENTE ÚNICA de las cifras del texto
financiero de la guía: ningún euro del capítulo financiero se escribe fuera de
aquí.

LIBRO HÍBRIDO (SPEC §2.2)
------------------------
Calca la estructura y las fórmulas encadenadas del molde `planes-v2_0` motor 2.2
—el mismo que verificó `plan-negocio-panaderia/plan-financiero-panaderia.xlsx` y
que reutilizó el libro 5 de Pastelería— y le añade DOS hojas propias: «Canales y
Punto Muerto» (cinco canales, D19) y «Talleres y Regalo Corporativo» (D7, la
hoja que absorbe el libro que la SPEC descartó). **Manda la línea de versión de
la familia de GUÍAS** (1.0 · septiembre 2026), no la del motor de planes, y se
declara en «Instrucciones».

LOS TRES CRUCES QUE RECIBE Y EL QUE ORIGINA (D32, §2.3)
-------------------------------------------------------
Cero fórmulas que nombren otro fichero. Cada cruce es una CELDA VERDE con su
valor por defecto declarado más una FILA DE CUADRE con semáforo:

* **7 ← 1** capacidad diaria del obrador, en la hoja de Tesorería, para calcular
  HACIA ATRÁS la fecha límite de cierre de pedidos de Navidad (aritmética de
  días y de índices de mes: `NETWORKDAYS` está prohibida).
* **7 ← 3** precio de la cobertura EN BASE IMPONIBLE, nunca el de la fuente con
  IVA (A-2): con la base equivocada el food cost sale un 9 % alto.
* **7 ← 2** CAPEX **SIN** el fondo de maniobra. La hoja «Inversión Inicial» NO
  vuelve a pedir las nueve partidas: pide esa única cifra. Traer el total del
  libro 2 —que lleva el fondo dentro— y dotar además el fondo aquí lo contaría
  DOS VECES, que es el defecto ALTO que Pastelería pagó.
* **2 ← 7** el fondo de maniobra SE DOTA AQUÍ, con los meses de colchón y los
  gastos fijos de este libro, y viaja al libro 2 **ya calculado**. Por eso este
  generador publica en `build/mapa-…json` las dos celdas citables: «gastos fijos
  mensuales del año de crucero» y «fondo de maniobra».

DECISIONES TÉCNICAS
-------------------
* **El año 2 ES el año de crucero.** El año 1 lleva la rampa (0,55 → 1,00 en
  seis meses) y el año 3 crece sobre el crucero. Así la columna «Año 2»
  reproduce al céntimo `datos_ejemplo.cuenta_resultados_crucero()`, que es lo
  que citan el guion y el bonus 1.
* **La estacionalidad lleva el valle de agosto dentro** (D36): doce coeficientes
  de media 1,000 exacta con agosto en el mínimo y diciembre en el máximo. Agosto
  NO vale cero: lo que para es el OBRADOR, no la tienda.
* **El sueldo del titular ya está en la nómina** (es el Encargado, P1): lo que va
  como renglón propio de los fijos es su CUOTA DE AUTÓNOMOS. Ponerle además una
  «retribución del propietario» sería contarlo dos veces —lo dice
  `datos_ejemplo.NOTA_PLANTILLA`—, y un negocio que sólo es rentable porque su
  dueño no cobra no es rentable.
* **Amortización y gastos financieros van DENTRO de los costes fijos**, y los
  financieros son los del AÑO DE CRUCERO: con los del año 1 (el de la carencia)
  el libro 2 y éste publicarían dos inversiones totales distintas.
* **El coste de ventas del P&L se DERIVA de una sola regla**: food cost de
  escandallo de la carta × (1 + packaging). Al lado va el food cost objetivo de
  la casa con su margen bruto DERIVADO (nunca los dos guardados aparte) y la
  brecha entre ambos, con semáforo.
* **El tipo de IVA del taller va SIN CIFRA** (D42.e): lo que está cerrado es que
  NO está exento (art. 20.Uno.10.º); el TIPO no.
* **Columna de escenario de formato** (D1): bombonería frente a bombonería +
  taza y churros, en columnas CONTIGUAS, en el P&L y en el punto muerto.
* Cero constantes dentro de las fórmulas; `IFERROR(...,"")` en toda división;
  «sin dato» = `""`, nunca `0`; semáforos con `ISNUMBER`; desplegables contra
  RANGO; A4 con `print_setup`; textos WinAnsi. Prohibidas INDIRECT, COUNTA, PMT,
  OFFSET, XLOOKUP, LET, LAMBDA, RANK, NETWORKDAYS e IRR: cero usos.

Salida fija: build/plan-financiero-3-anos-chocolateria.xlsx
             + build/mapa-plan-financiero-3-anos-chocolateria.json
Uso: /usr/local/bin/python3 gen_plan-financiero-3-anos-chocolateria.py
Via: Claude Code
"""
import datetime
import math
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import _comun_libro_7 as C                                     # noqa: E402
import datos_ejemplo as D                                      # noqa: E402
import motor                                                   # noqa: E402

NOMBRE = 'plan-financiero-3-anos-chocolateria'
TITULO = 'Plan financiero a 3 años'

H_INS = 'Instrucciones'
H_SUP = '0. Supuestos'
H_INV = 'Inversión Inicial'
H_PYG = 'PyG 3 Años'
H_PEQ = 'Punto de Equilibrio'
H_ESC = 'Escenarios'
H_PER = 'Personal'
H_TES = 'Tesorería 12 meses'
H_FIN = 'Financiación'
H_CAN = 'Canales y Punto Muerto'
H_TAL = 'Talleres y Regalo Corporativo'

Q_SUP = "'" + H_SUP + "'!"
Q_INV = "'" + H_INV + "'!"
Q_PYG = "'" + H_PYG + "'!"
Q_PEQ = "'" + H_PEQ + "'!"
Q_PER = "'" + H_PER + "'!"
Q_TES = "'" + H_TES + "'!"
Q_FIN = "'" + H_FIN + "'!"
Q_CAN = "'" + H_CAN + "'!"

MESES_COL = ('B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M')

N = motor.NARROW

#: Los ids legales que cita ESTE libro. `gate_legal()` los comprueba ANTES de
#: escribir una sola nota (regla 1 de §2.3).
IDS_LEGALES = (
    'CHN-65', 'CHN-65b', 'CHN-65c', 'CHN-66', 'CHN-67', 'CHN-71', 'CHN-71b',
    'CHN-71c', 'CHN-72', 'CHN-75', 'CHN-77', 'CHN-93', 'CHN-94', 'CHN-95',
    'CHN-24', 'CHN-41', 'CHN-48',
)

#: Los cinco canales, en el orden de `datos_ejemplo.CANALES`.
CANALES = D.CANALES
TALLER = [c for c in CANALES if c['canal'].startswith('Talleres')][0]
I_TALLER = CANALES.index(TALLER)
I_B2B = [i for i, c in enumerate(CANALES) if c['canal'].startswith('B2B')][0]
I_CORP = [i for i, c in enumerate(CANALES)
          if c['canal'].startswith('Regalo')][0]
I_MOST = [i for i, c in enumerate(CANALES)
          if c['canal'].startswith('Mostrador')][0]

SALE_644 = {'no': 'No', 'si': 'Sí', 'no lo se': 'No lo sé'}


def ie(expr):
    return motor.iferror(expr)


# ==========================================================================
# Filas fijas de cada hoja
# ==========================================================================
# --- 0. Supuestos ---------------------------------------------------------
S = {
    'tickets': 6, 'piezas': 7, 'pvp': 8, 'ticket_iva': 9, 'ticket_sin': 10,
    'dias': 11, 'factor_a1': 12, 'crec_a3': 13,
    'iva_prod': 15, 'iva_taza': 16, 'iva_taller': 17, 'iva_gen': 18,
    'iva_compras': 19, 'iva_medio': 20,
    'fc_escandallo': 22, 'packaging': 23, 'food_cost': 24, 'fc_objetivo': 25,
    'margen_obj': 26, 'brecha': 27,
    'ss': 29, 'pagas': 30, 'smi': 31, 'horas_sem': 32,
    'renta': 34, 'fianza_meses': 35, 'suministros': 36, 'autonomos': 37,
    'subida': 38,
    'propios': 40, 'principal': 41, 'tipo': 42, 'plazo': 43, 'carencia': 44,
    'colchon': 45,
    'is_nueva': 47, 'is_gen': 48, 'bases_neg': 49,
    'anios_amort': 51,
    'rampa1': 53, 'rampa_meses': 54, 'mes_apertura': 55, 'dias_semana': 56,
    'dias_cobro': 58, 'dias_pago': 59, 'extra1': 60, 'extra2': 61,
    'extra3': 62,
    'dscr_min': 64, 'dscr_obj': 65, 'holgura': 66, 'neto_suelo': 67,
    'neto_techo': 68, 'techo_personal': 69, 'techo_alquiler': 70,
    'paso_sens': 71, 'tolerancia': 72,
}
SEC_SUP = {5: 'ACTIVIDAD', 14: 'IVA Y TIPOS', 21: 'COSTE DE VENTAS',
           28: 'PERSONAL', 33: 'LOCAL Y GASTOS FIJOS', 39: 'FINANCIACIÓN',
           46: 'FISCAL', 50: 'AMORTIZACIÓN', 52: 'ARRANQUE',
           57: 'COBROS Y PAGOS', 63: 'UMBRALES Y SUELOS DE CONTROL'}


def sup(clave):
    return Q_SUP + '$B$' + str(S[clave])


# --- Inversión Inicial ----------------------------------------------------
IV = {'sec_cruce': 5, 'capex_trae': 6, 'capex_orig': 7, 'capex_desv': 8,
      'capex_cuadre': 9, 'iva_sop': 10, 'amortizable': 11,
      'sec_fondo': 13, 'fijos_mes': 14, 'colchon': 15, 'fondo': 16,
      'sec_inv': 18, 'capex': 19, 'fdm': 20, 'total': 21, 'iva': 22,
      'necesidad': 23,
      'sec_am': 25, 'base': 26, 'amort': 27,
      'nota': 29}

# --- PyG 3 Años -----------------------------------------------------------
P = {'cab': 5, 'sec_ing': 6, 'tickets': 7, 'ticket': 8, 'dias': 9,
     'actividad': 10, 'ingresos': 11,
     'sec_var': 12, 'coste_ventas': 13, 'tot_var': 14, 'margen': 15,
     'sec_fijos': 16, 'personal': 17, 'autonomos': 18, 'alquiler': 19,
     'suministros': 20, 'seguros': 21, 'gestoria': 22, 'software': 23,
     'telefonia': 24, 'limpieza': 25, 'mantenimiento': 26, 'publicidad': 27,
     'otros': 28, 'amortizacion': 29, 'financieros': 30, 'tot_fijos': 31,
     'iva_var': 32, 'iva_fijos': 33, 'rai': 34, 'bases_ini': 35,
     'base_imp': 36, 'ejercicios': 37, 'tipo_is': 38, 'is': 39,
     'bases_fin': 40, 'neto': 41,
     'sec_ratios': 42, 'cab_ratios': 43, 'r_margen': 44, 'r_coste': 45,
     'r_personal': 46, 'r_alquiler': 47, 'r_neto': 48, 'r_banda': 49,
     'r_equilibrio': 50,
     'sec_formato': 52, 'cab_formato': 53, 'f_clientes': 54, 'f_pvp_min': 55,
     'f_pvp_max': 56, 'f_pvp': 57, 'f_margen_pct': 58, 'f_personal': 59,
     'f_otros': 60, 'f_ventas': 61, 'f_var': 62, 'f_mb': 63, 'f_fijos': 64,
     'f_rai': 65, 'f_neto': 66, 'f_mneto': 67, 'f_veredicto': 68,
     'sec_cob': 70, 'cob_trae': 71, 'cob_orig': 72, 'cob_desv': 73,
     'cob_cuadre': 74, 'cob_kg': 75, 'cob_coste': 76, 'cob_peso': 77,
     'cob_subida': 78, 'cob_impacto': 79, 'cob_neto': 80,
     'nota': 82}

#: Los ocho fijos que se teclean AQUÍ (los otros seis salen de otra hoja o de
#: «0. Supuestos»). El importe por defecto es el MENSUAL de
#: `datos_ejemplo.GASTOS_FIJOS_MENSUALES`, llevado a año.
FIJOS_VERDES = [
    ('seguros', 4, 0.0,
     'Responsabilidad civil y continente. `CHN-70` (seguro de RC) está en los '
     'EXCLUIDOS de la verificación legal: NO está verificado como obligatorio '
     'y depende de tu comunidad autónoma, así que aquí va como supuesto y sin '
     'cifra de norma detrás. Las operaciones de seguro están exentas de IVA, y '
     'por eso su tipo va a cero.'),
    ('gestoria', 5, 0.21, 'Supuesto.'),
    ('software', 6, 0.21,
     'Supuesto. Con Verifactu en el horizonte (1 de enero de 2027 para '
     'sociedades y 1 de julio de 2027 para autónomos, no 2026) esta cuota deja '
     'de ser opcional.'),
    ('telefonia', 7, 0.21, 'Supuesto.'),
    ('limpieza', 8, 0.21,
     'Supuesto. Incluye guantes y utillaje dedicado: el equipo que has usado '
     'con un alérgeno no se reutiliza para otro alimento sin limpiarlo.'),
    ('mantenimiento', 9, 0.21,
     'Supuesto. Si montas la variante de taza y churros con freidora de gas, '
     'súmale la inspección periódica obligatoria cada cinco años, que se te '
     'repercute.'),
    ('publicidad', 10, 0.21, 'Supuesto.'),
    ('otros', 11, 0.21, 'Supuesto.'),
]

# --- Punto de Equilibrio --------------------------------------------------
E = {'cab': 5, 'sec_base': 6, 'fijos_anio': 7, 'fijos_mes': 8, 'ticket': 9,
     'cv_ticket': 10, 'mc_ticket': 11, 'dias': 12, 'principal': 13,
     'sec_cont': 14, 'tk_anio': 15, 'tk_dia': 16, 'ing_anio': 17,
     'ing_mes': 18,
     'sec_caja': 19, 'fijos_caja': 20, 'tkc_anio': 21, 'tkc_dia': 22,
     'ingc_anio': 23,
     'sec_contraste': 24, 'tk_previstos': 25, 'holgura': 26, 'semaforo': 27,
     'nota': 28,
     'sec_formato': 30, 'cab_formato': 31, 'pm_fijos': 32, 'pm_mc': 33,
     'pm_mes': 34, 'pm_dia': 35, 'pm_nota': 36,
     'sec_sens': 38, 'sens_cab': 39, 'sens_ini': 40, 'sens_fin': 44,
     'sens_nota': 46}

# --- Escenarios -----------------------------------------------------------
X = {'cab': 5, 'tickets': 6, 'ticket': 7, 'dias': 8, 'ingresos': 9,
     'coste': 10, 'tot_var': 11, 'margen': 12, 'fijos': 13, 'rai': 14,
     'is': 15, 'neto': 16, 'margen_neto': 17, 'tk_equilibrio': 18,
     'sec_exige': 19, 'personal_ventas': 20, 'ventas_jornada': 21,
     'saldo_est': 22, 'saldo_real': 23, 'nota': 25}

# --- Personal -------------------------------------------------------------
R_CAB = 5
R_INI = 6
R_FIN = R_INI + len(D.PLANTILLA) - 1             # 8
R_TOT = R_FIN + 1                                # 9
R_SEC_CONV = R_TOT + 2                           # 11
R_CONV_CAB = R_SEC_CONV + 1                      # 12
R_CONV_INI = R_CONV_CAB + 1                      # 13
R_CONV_FIN = R_CONV_INI + len(D.CONVENIO) - 1    # 18
R_SEC_SMI = R_CONV_FIN + 2                       # 20
R_SUELO = R_SEC_SMI + 1                          # 21
R_SMI = R_SEC_SMI + 2                            # 22
R_VEREDICTO = R_SEC_SMI + 3                      # 23
R_SEC_MERC = R_SEC_SMI + 5                       # 25
R_MERC_CAB = R_SEC_MERC + 1                      # 26
R_MERC_INI = R_MERC_CAB + 1                      # 27
R_MERC_FIN = R_MERC_INI + len(D.SALARIOS_MERCADO) - 1   # 30
R_SEC_CONVCH = R_MERC_FIN + 2                    # 32
R_CONVCH_CAB = R_SEC_CONVCH + 1                  # 33
R_CONVCH_INI = R_CONVCH_CAB + 1                  # 34
R_CONVCH_FIN = (R_CONVCH_INI
                + len(D.CONVENIOS_QUE_NOMBRAN_CHOCOLATE) - 1)    # 37
R_SEC_HORAS = R_CONVCH_FIN + 2                   # 39
R_HORAS = R_SEC_HORAS + 1                        # 40
R_JORNADAS = R_SEC_HORAS + 2                     # 41
R_AVISOS = R_SEC_HORAS + 3                       # 42
R_HORAS_ANIO = R_SEC_HORAS + 4                   # 43
R_RATIO = R_SEC_HORAS + 5                        # 44
R_HORA_OBR = R_SEC_HORAS + 6                     # 45
R_NOTA = R_SEC_HORAS + 8                         # 47

# --- Tesorería 12 meses ---------------------------------------------------
T = {'cab': 5, 'estacionalidad': 6, 'rampa': 7, 'reparto': 8,
     'sec_cobros': 9, 'ventas': 10,
     'sec_pagos': 11, 'compras': 12, 'fijos': 13, 'nominas': 14,
     'intereses': 15, 'principal': 16,
     'iva_rep': 17, 'iva_sop': 18, 'iva_arr': 19, 'iva_liq': 20,
     'iva_pago': 21,
     'flujo': 22, 'saldo': 23, 'saldo_min': 24, 'mes_fondo': 25,
     'sec_retorno': 27, 'fcf1': 28, 'fcf2': 29, 'fcf3': 30, 'inversion': 31,
     'payback': 32,
     'sec_nav': 34, 'cap_trae': 35, 'cap_orig': 36, 'cap_desv': 37,
     'cap_cuadre': 38, 'base_dia': 39, 'excedente': 40, 'piezas_nav': 41,
     'dias_prod': 42, 'dias_nat': 43, 'entrega': 44, 'limite': 45,
     'mes_limite': 46, 'veredicto_nav': 47, 'nota_nav': 48,
     'nota': 50}

# --- Financiación ---------------------------------------------------------
F = {'sec_origen': 5, 'propios': 6, 'prestamo': 7, 'otras': 8,
     'tot_origen': 9,
     'sec_usos': 10, 'necesidad': 11, 'diferencia': 12, 'dif_pct': 13,
     'ajuste': 14,
     'sec_cond': 15, 'principal': 16, 'tipo': 17, 'tipo_mes': 18,
     'plazo': 19, 'carencia': 20, 'meses_am': 21, 'cuota': 22,
     'nota_cuota': 23, 'cab': 25}
F_MES_INI = 26
F_MESES = 84
F_MES_FIN = F_MES_INI + F_MESES - 1              # 109
F_TOL = F_MES_FIN + 1                            # 110
F_PENDIENTE = F_MES_FIN + 2                      # 111
F_CIERRA = F_MES_FIN + 3                         # 112
F_SEC_ANIO = F_MES_FIN + 5                       # 114
F_ANIO_CAB = F_MES_FIN + 6                       # 115
F_ANIO_INI = F_MES_FIN + 7                       # 116
F_ANIOS = 7
F_ANIO_FIN = F_ANIO_INI + F_ANIOS - 1            # 122
F_DSCR_MIN = F_ANIO_FIN + 1                      # 123
F_DSCR_SEM = F_ANIO_FIN + 2                      # 124
F_NOTA = F_ANIO_FIN + 4                          # 126

# --- Canales y Punto Muerto -----------------------------------------------
K_CAB = 5
K_INI = 6
K_FIN = K_INI + len(CANALES) - 1                 # 10
K_TOT = K_FIN + 1                                # 11
K_B2B = K_INI + I_B2B
K_MOST = K_INI + I_MOST
K_TAL = K_INI + I_TALLER
K_SEC_PM = K_TOT + 2                             # 13
K_FIJOS = K_SEC_PM + 1
K_FIJOS_MES = K_SEC_PM + 2
K_MC = K_SEC_PM + 3
K_REGLA = K_SEC_PM + 4
K_DIF_MC = K_SEC_PM + 5
K_PM_CON = K_SEC_PM + 6
K_PM_SIN = K_SEC_PM + 7
K_PM_DIF = K_SEC_PM + 8
K_SOSTIENE = K_SEC_PM + 9
K_APORTE = K_SEC_PM + 10
K_SEC_644 = K_SEC_PM + 12                        # 25
K_FUERA = K_SEC_644 + 1
K_PREGUNTA = K_SEC_644 + 2
K_SEC_ART3 = K_SEC_644 + 4                       # 29
K_PESO_B2B = K_SEC_ART3 + 1
K_UMBRAL = K_SEC_ART3 + 2
K_VEREDICTO = K_SEC_ART3 + 3
K_COBRO = K_SEC_ART3 + 5                         # 34
K_SEC_ENVIO = K_SEC_ART3 + 7                     # 36
K_PEDIDO = K_SEC_ENVIO + 1                       # 37
K_ENVIO_PCT = K_SEC_ENVIO + 2                    # 38
K_MC_ENVIO = K_SEC_ENVIO + 3                     # 39
K_VER_ENVIO = K_SEC_ENVIO + 4                    # 40
K_NOTA = K_SEC_ENVIO + 6                         # 42
K_LISTAS = K_NOTA + 2                            # 44

# --- Talleres y Regalo Corporativo ----------------------------------------
W = {'sec_taller': 5, 'precio_min': 6, 'precio_max': 7, 'precio': 8,
     'aforo': 9, 'minimo': 10, 'dur_min': 11, 'dur_max': 12, 'horas_doc': 13,
     'coste_hora': 14, 'coste_doc': 15, 'materia': 16, 'servir': 17,
     'neto_persona': 18, 'asistentes_pm': 19, 'asistentes_pm_mat': 20,
     'veredicto_pm': 21,
     'sec_sala': 23, 'horas_sala': 24, 'ingreso_lleno': 25, 'hora_taller': 26,
     'ventas_most': 27, 'horas_anio': 28, 'hora_vendiendo': 29, 'dif': 30,
     'veredicto_sala': 31,
     'sec_volumen': 33, 'talleres_mes': 34, 'asistentes_medios': 35,
     'ingresos_anio': 36, 'canal_anio': 37, 'dif_canal': 38,
     'veredicto_vol': 39,
     'sec_iva': 41, 'iva': 42, 'nota_iva': 43,
     'sec_corp': 45, 'pedido_min': 46, 'cobro_dias': 47, 'plazo_muestra': 48,
     'cajas_min': 49, 'cajas_max': 50, 'pedidos_anio': 51, 'facturacion': 52,
     'margen': 53, 'circulante': 54, 'coste_fin': 55, 'cierre_agenda': 56,
     'veredicto_corp': 57,
     'nota': 59}


# ==========================================================================
# Valores por defecto calculados (ningún número tecleado a ojo)
# ==========================================================================
#: Los tres cruces que RECIBE este libro, con la celda exacta del libro origen.
CRUCE_CAPEX = [c for c in D.CRUCES if c['n'] == 6][0]
CRUCE_CAP = [c for c in D.CRUCES if c['n'] == 2][0]
CRUCE_COB = [c for c in D.CRUCES if c['n'] == 5][0]

#: Celdas de origen, leídas de los mapas que publicaron C1 y C2 (§2.5). Se citan
#: como TEXTO en la hoja: no hay ni una fórmula que nombre otro fichero.
#: A4 (refutación 2026-09-12): la SPEC y `datos_ejemplo.CRUCES[5]` fijan
#: «Resumen» como la hoja de origen de este cruce -es la que el libro 2
#: llama «las cifras que hay que llevar al banco»-, no una fila intermedia
#: de la hoja de trabajo de 69 filas. El VALOR es el mismo (`Resumen!B7` es
#: literalmente `='CAPEX por Bloque'!L44`).
ORIGEN_CAPEX = ('calculadora-capex-chocolateria.xlsx!Resumen!B7 '
                '(«CAPEX SIN el fondo de maniobra»)')
ORIGEN_IVA = ('calculadora-capex-chocolateria.xlsx!CAPEX por Bloque!M40 '
              '(«IVA soportado total»)')
ORIGEN_CAP = ('capacidad-obrador-y-clima.xlsx!Cuello de Botella!B7 '
              '(«Bombones al día que permite el conjunto»)')
ORIGEN_COB = ('sensibilidad-al-precio-del-cacao.xlsx!Coste de Cobertura!G7 '
              '(«precio de la cobertura negra EN BASE IMPONIBLE»)')

DEF_CAPEX = round(D.capex_sin_fondo_de_maniobra(), 2)      # 89.219,35 €
DEF_IVA_CAPEX = round(D.iva_soportado_capex(), 2)          # 17.912,86 €
DEF_AMORTIZABLE = round(D.capex_amortizable_sin_iva(), 2)  # 86.619,35 €
DEF_CAPACIDAD = 512                                        # libro 1
DEF_BASE_DIA = 472                                         # libro 1
DEF_COBERTURA = round(D.precio_cobertura_base_imponible('negra'), 4)
DEF_PVP = round(D.pvp_medio_ponderado(), 4)
DEF_FC_CARTA = round(D.food_cost_carta(), 6)
DEF_NECESIDAD = D.inversion_total_sin_iva() + D.iva_soportado_capex()
DEF_PROPIOS = (math.ceil((DEF_NECESIDAD - D.principal_prestamo()) * 100.0)
               / 100.0)
DEF_COSTE_HORA = round(D.coste_hora_obrador(), 4)
#: Kilos de cobertura NEGRA que se van al año, del libro 3 (su hoja «Stock y
#: Cobertura de Compra»). Es una COPIA declarada, como el precio.
DEF_KG_COBERTURA = 462.1

#: Coste de personal del escenario de formato: media jornada más del grupo 4 del
#: convenio (el de «personal cualificado», que es el del Dependiente), con la
#: Seguridad Social a cargo de la empresa dentro. Supuesto declarado.
DEF_PERSONAL_TAZA = round(D.CONVENIO[3][3] * 0.5 * (1.0 + D.P('ss_empresa')),
                          2)


# ==========================================================================
# Hoja «Instrucciones»
# ==========================================================================
PASOS = [
    '1. Hoja «0. Supuestos»: es el cuadro de mandos. Aquí se teclean las TASAS '
    'y los DRIVERS —clientes al día, piezas por ticket, días de apertura, '
    'tipos de IVA, food cost, condiciones del préstamo, umbrales de control— y '
    'el resto del libro se recalcula solo. Las partidas de gasto se teclean en '
    'su hoja, no aquí.',
    '2. Hoja «Inversión Inicial»: NO vuelve a pedirte las nueve partidas del '
    'CAPEX. Te pide UNA cifra —el CAPEX SIN el fondo de maniobra, que publica '
    'el libro «calculadora-capex-chocolateria»— y dota aquí el fondo de '
    'maniobra con TUS meses de colchón y TUS gastos fijos. El fondo se calcula '
    'una sola vez en todo el pack, y es esta hoja la que lo calcula.',
    '3. Hoja «PyG 3 Años»: la cuenta de resultados. El AÑO 2 es el año de '
    'crucero; el año 1 lleva la rampa de arranque y el año 3 crece sobre el '
    'crucero. La amortización y los intereses van DENTRO de los costes fijos, '
    'y la cuota de autónomos del titular también. Abajo, el escenario de '
    'formato: bombonería frente a bombonería con taza y churros, lado a lado.',
    '4. Hoja «Punto de Equilibrio»: cuántos clientes al día hay que hacer para '
    'no perder dinero, en dos versiones. La CONTABLE incluye la amortización; '
    'la de CAJA le quita la amortización (que no se paga) y le suma la '
    'devolución de principal (que sí). La segunda es la que decide si llegas a '
    'fin de mes.',
    '5. Hoja «Escenarios»: el mismo modelo con tres juegos de clientes, ticket '
    'medio y días de apertura. La columna «Realista» LEE el año de crucero del '
    'P&L, así que no puede desviarse de él.',
    '6. Hoja «Personal»: tres personas y dos jornadas y media, con el bruto del '
    'convenio en celda verde y la Seguridad Social a cargo de la empresa '
    'DENTRO. Del bruto al coste empresa hay un tercio más: es el salto que más '
    'sorprende. Al lado, los salarios de MERCADO, que son orientativos y no '
    'son un convenio.',
    '7. Hoja «Tesorería 12 meses»: el P&L dice si el negocio gana dinero; esta '
    'hoja dice si le queda caja para llegar a fin de mes. Trae la '
    'estacionalidad con el valle de agosto dentro, la rampa de arranque, el '
    'desfase de cobros y pagos, la liquidación trimestral del IVA y la FECHA '
    'LÍMITE de cierre de pedidos de Navidad, calculada hacia atrás desde la '
    'capacidad de tu obrador.',
    '8. Hoja «Financiación»: de dónde sale el dinero y cuánto cuesta '
    'devolverlo. El cuadro de amortización es MENSUAL, con 84 filas, porque la '
    'carencia de este caso son seis meses y un cuadro anual no sabe expresar '
    'medio año. Abajo, el DSCR año a año: es el número que decide la operación '
    'bancaria.',
    '9. Hoja «Canales y Punto Muerto»: mostrador, online con envío '
    'refrigerado, B2B a hostelería, regalo corporativo y talleres, cada uno '
    'con su margen, su coste de servir, su coste de envío y sus días de cobro. '
    'Dice qué canal sostiene el negocio, qué pasa con el punto muerto si '
    'quitas el B2B y cuáles de los cinco te sacan de la nota del epígrafe '
    '644.5 del IAE.',
    '10. Hoja «Talleres y Regalo Corporativo»: cuántos asistentes necesita un '
    'taller para cubrir su propio coste, y cuánto deja una hora de sala dando '
    'taller frente a la misma hora vendiendo. Más el pedido mínimo del regalo '
    'corporativo, sus días de cobro y el plazo mínimo desde que el cliente '
    'aprueba la muestra.',
    '11. Y una regla de uso: cambia SIEMPRE los supuestos antes de discutir el '
    'resultado. Este libro no está para darte la razón, está para que veas qué '
    'hace falta que pase.',
]

NOTAS_LIBRO = [
    'ESTE LIBRO ES LA FUENTE ÚNICA DE LAS CIFRAS FINANCIERAS DE LA GUÍA. Si un '
    'euro del texto no sale de una celda de aquí, es que está inventado. '
    'Cámbialo aquí y el capítulo entero deja de cuadrar contigo: eso es '
    'exactamente lo que tiene que pasar.',
    'LIBRO HÍBRIDO. La estructura y las fórmulas encadenadas son las del molde '
    'de planes de negocio de la casa (nueve hojas, con tesorería, IVA y '
    'financiación de verdad), y encima van las dos hojas propias de esta guía: '
    '«Canales y Punto Muerto» y «Talleres y Regalo Corporativo». La versión '
    'que manda es la de la FAMILIA DE GUÍAS, la que está al pie de esta hoja, '
    'no la del motor de planes.',
    'NO HAY NI UNA FÓRMULA QUE APUNTE A OTRO FICHERO, en todo el pack. Lo que '
    'viene de otro libro viene COPIADO, declarado y con una fila de CUADRE que '
    'te avisa si las dos cifras han dejado de decir lo mismo. Un enlace entre '
    'ficheros se rompe en cuanto alguien mueve una carpeta, y entonces el '
    'libro miente sin avisar. Este recibe tres cifras así (el CAPEX sin el '
    'fondo de maniobra, la capacidad diaria del obrador y el precio de la '
    'cobertura en base imponible) y devuelve una: el fondo de maniobra.',
    'EL FONDO DE MANIOBRA SE CALCULA AQUÍ Y SÓLO AQUÍ. Es «meses de colchón x '
    'gastos fijos mensuales», y los dos factores viven en este libro. El de '
    'CAPEX no te vuelve a preguntar los meses de colchón: recibe el fondo ya '
    'calculado. Si se calculara en los dos, los dos libros publicarían dos '
    'inversiones totales distintas con el mismo nombre.',
    'EL SUELDO DEL TITULAR YA ESTÁ EN LA NÓMINA. En este caso el titular es el '
    'Encargado, y su retribución está en la plantilla de la hoja de Personal. '
    'Lo que va como renglón propio de los fijos es su CUOTA DE AUTÓNOMOS: '
    'ponerle además una «retribución del propietario» sería contarlo dos '
    'veces. Lo que no cambia es el fondo del asunto: un negocio que sólo es '
    'rentable porque su dueño no cobra no es rentable.',
    'EL FOOD COST DEL P&L NO ES EL DE UNA PIEZA SUELTA, Y NO ES UN ERROR. El '
    'escandallo del libro «carta-de-apertura-y-escandallo-chocolate» mide la '
    'materia prima de la pieza; lo que proyecta este P&L es esa misma materia '
    'MÁS el packaging, que en bombonería pesa porque la caja ES el producto en '
    'las campañas de regalo. Al lado tienes el food cost objetivo de la casa y '
    'la brecha entre los dos, con su semáforo: esa brecha es tu colchón.',
    'MARGEN BRUTO Y FOOD COST SON LA MISMA REGLA DICHA DOS VECES. Por eso el '
    'libro guarda UNO —el food cost objetivo— y DERIVA el otro. Publicarlos '
    'como dos reglas independientes es un error de método: antes o después '
    'dicen cosas distintas.',
    'EL TIPO DE IVA DEL TALLER VA SIN CIFRA, A PROPÓSITO. Lo que sí está '
    'cerrado es que un taller de bombonería NO está exento: el art. 20.Uno.10.º '
    'de la Ley del IVA excluye las clases para cuya realización haya que darse '
    'de alta en las tarifas empresariales del IAE. Lo que NO está cerrado es el '
    'TIPO, y esta guía no publica ninguna cifra que no pueda sostener. '
    'Pregúntaselo a tu asesor y escríbelo tú en «0. Supuestos».',
    'TODAS LAS CIFRAS VAN SIN IVA salvo donde la hoja diga lo contrario. La '
    'tesorería es caja: ahí el IVA entra y sale, y la liquidación trimestral lo '
    'devuelve a su sitio. Las columnas de los años 2 y 3 están en euros del año '
    '1 mientras la «Subida anual de los costes fijos» de «0. Supuestos» valga '
    'cero.',
]

FRONTERA = [
    ('kit-tareas-chocolateria (12 €)',
     'La operación del obrador que ya tienes: partidas de producción, curvas '
     'de templado, calendario anual de campañas y fichas de tarea por perfil.',
     'Este libro NO planifica producción ni templa nada. Toma su resultado en '
     'euros y lo proyecta a tres años. Los tres perfiles de la hoja de '
     'Personal son los de ese kit, con sus nombres.'),
    ('El libro «sensibilidad-al-precio-del-cacao» de esta misma guía',
     'El precio de la cobertura, en las dos bases de IVA, y qué pasa con cada '
     'referencia si el cacao sube un 40 %.',
     'Aquí el coste de la materia entra como UN porcentaje sobre las ventas. '
     'El precio de la cobertura en base imponible se trae de allí por celda '
     'verde, con su fila de cuadre.'),
    ('El libro «calculadora-capex-chocolateria» de esta misma guía',
     'El CAPEX partida a partida, con su columna de IVA por línea, la variante '
     'del formato y la comparación entre traspaso y obra nueva.',
     'Aquí entra UNA cifra: el CAPEX SIN el fondo de maniobra. El fondo lo '
     'dota esta hoja y vuelve allí ya calculado.'),
    ('El libro «capacidad-obrador-y-clima» de esta misma guía',
     'Cuántos bombones al día aguanta el equipo que vas a comprar y cuál es el '
     'que limita.',
     'Aquí esa capacidad sólo sirve para una cosa, y es importante: calcular '
     'hacia atrás la fecha límite de cierre de pedidos de Navidad.'),
    ('plan-negocio-bar-restaurante y los demás planes de negocio (35 €)',
     'El dossier completo que se le entrega al banco, con memoria escrita.',
     'Este libro es el motor de números de una GUÍA de apertura. Si vas a '
     'pedir financiación de verdad, el dossier del banco es aquel producto.'),
]


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS, 0)
    C.anchos(ws, {'A': 44, 'B': 44, 'C': 44})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=C.ORO)
    ws.row_dimensions[1].height = 26
    motor.val(ws, 'A2', C.SUBTITULO)
    ws['A2'].font = Font(size=9, color=C.GRIS_TXT)
    motor.val(ws, 'A3', 'Para qué sirve: saber si el negocio se sostiene, qué '
                        'canal lo sostiene y si el taller da dinero o te ocupa '
                        'el obrador en el peor momento.')
    ws['A3'].font = Font(italic=True, size=9)

    fila = 5
    C.seccion(ws, 'A%d' % fila, 'Instrucciones de uso')
    fila += 1
    for paso in PASOS:
        C.parrafo(ws, fila, paso, 'A', 'C', alto=56)
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
              'Qué hace este libro y qué hace otro (para no teclear dos veces)')
    fila += 1
    C.cabecera(ws, fila, [('A', 'Producto o libro'), ('B', 'Qué aporta'),
                          ('C', 'Qué NO hace este libro')], altura=26)
    fila += 1
    for producto, aporta, no_hace in FRONTERA:
        motor.val(ws, 'A%d' % fila, producto, bold=True, wrap=True)
        motor.val(ws, 'B%d' % fila, aporta, wrap=True)
        motor.val(ws, 'C%d' % fila, no_hace, wrap=True)
        ws.row_dimensions[fila].height = 66
        fila += 1
    fila += 1

    C.seccion(ws, 'A%d' % fila, 'Cada cuánto se usa este libro')
    fila += 1
    C.parrafo(ws, fila,
              'Cadencia: «0. Supuestos» e «Inversión Inicial», MIENTRAS BUSCAS '
              'LOCAL y pides presupuestos, tantas veces como haga falta. El '
              'P&L, el punto de equilibrio y los escenarios, UNA VEZ ANTES DE '
              'FIRMAR y otra antes de sentarte con el banco. «Tesorería 12 '
              'meses», CADA MES durante el primer año, sustituyendo la '
              'previsión por lo que pasó de verdad. «Canales y Punto Muerto» y '
              '«Talleres y Regalo Corporativo», cada vez que te plantees abrir '
              'o cerrar un canal, y en septiembre, cuando se cierra la agenda '
              'corporativa de Navidad.', 'A', 'C', alto=80)
    fila += 2

    C.parrafo(ws, fila, C.NOTA_DESPROTEGER, 'A', 'C', alto=28)
    fila += 2
    C.pie(ws, fila, 'A', 'C')
    C.pagina(ws, apaisado=False, area='A1:C%d' % (fila + 1))
    return ws


# ==========================================================================
# Hoja «0. Supuestos»
# ==========================================================================
def hoja_supuestos(wb):
    ws = wb.create_sheet(H_SUP)
    C.anchos(ws, {'A': 56, 'B': 17, 'C': 98})
    C.encabezar(ws, 'Supuestos: las tasas y los drivers del modelo',
                'Cambia las celdas VERDES y el resto del libro se recalcula '
                'solo. Las partidas de gasto se teclean en su hoja, no aquí. '
                'Cada supuesto lleva al lado de dónde sale y qué pasa si lo '
                'mueves.', col_fin='C')
    for fila, texto in SEC_SUP.items():
        C.banda(ws, fila, 'ABC', texto)

    def ent(clave, etiqueta, valor, fmt, nota_txt, id_chn=None, id_chs=None):
        fila = S[clave]
        motor.val(ws, 'A%d' % fila, etiqueta)
        C.entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
        C.nota(ws, 'C%d' % fila, nota_txt)
        if id_chn:
            C.nota_celda(ws, 'B%d' % fila, id_chn)
        elif id_chs:
            C.nota_fuente(ws, 'B%d' % fila, id_chs)
        return 'B%d' % fila

    def fx(clave, etiqueta, formula, fmt, nota_txt):
        fila = S[clave]
        motor.val(ws, 'A%d' % fila, etiqueta)
        motor.f(ws, 'B%d' % fila, formula, fmt=fmt)
        C.nota(ws, 'C%d' % fila, nota_txt)
        return 'B%d' % fila

    # --- ACTIVIDAD --------------------------------------------------------
    ent('tickets', 'Clientes al día en velocidad de crucero',
        D.P('tickets_dia_crucero'), C.ENT,
        'SUPUESTO, y de los gordos: no existe dato público de tráfico de una '
        'bombonería española, así que este número no es un benchmark. '
        'Cuéntalos tú en la puerta de tres bombonerías parecidas a la que '
        'quieres abrir, un sábado y un martes, y trae el tuyo. Es la ÚNICA '
        'palanca que hay que tocar para mover el resultado: los costes no se '
        'maquillan.')
    ent('piezas', 'Piezas por ticket', D.P('piezas_por_ticket'), C.DEC1,
        'SUPUESTO. En bombonería es BAJO -1,4- porque la unidad de venta real '
        'es la CAJA, no la pieza: quien entra a por un regalo se lleva una '
        'caja de 20 euros, no ocho bombones sueltos. De aquí sale el ticket '
        'medio, que NO se teclea: se calcula.')
    ent('pvp', 'PVP medio ponderado de la carta, CON IVA (€/pieza)', DEF_PVP,
        C.EUR,
        'Sale de las 28 referencias del libro '
        '«carta-de-apertura-y-escandallo-chocolate», ponderadas por su mix de '
        'ventas. Si cambias la carta allí, trae aquí el nuevo PVP medio: es '
        'COPIA declarada, no un vínculo entre ficheros.')
    fx('ticket_iva', 'Ticket medio CON IVA (€)',
       ie('$B$%d*$B$%d' % (S['piezas'], S['pvp'])), C.EUR,
       'Piezas por ticket x PVP medio ponderado. Es lo que ve el cliente en el '
       'datáfono.')
    fx('ticket_sin', 'Ticket medio SIN IVA (€)',
       ie('$B$%d/(1+$B$%d)' % (S['ticket_iva'], S['iva_medio'])), C.EUR,
       'Es el que entra en el P&L: la cuenta de resultados va siempre sin IVA. '
       'Se divide por el IVA MEDIO de la carta, no por un tipo suelto, para '
       'que el día que entre una referencia a otro tipo el libro siga '
       'cuadrando.')
    ent('dias', 'Días de apertura al año', D.NEGOCIO['dias_apertura_anio'],
        C.ENT,
        'SUPUESTO: 6 días por semana x 52 semanas = 312, menos 8 días de '
        'cierre por festivos. En AGOSTO NO SE CIERRA: lo que para es el '
        'obrador, no la tienda, y el literal del kit lo dice («la tienda abre '
        'para el turista aunque el obrador pare»). Una bombonería de menos de '
        '300 m2 tiene libertad horaria por el art. 5.2 de la Ley de Horarios '
        'Comerciales, no por el 5.1.', id_chn='CHN-77')
    fx('factor_a1', 'Actividad del año 1 sobre la de crucero (%)',
       ie('SUMPRODUCT(%sB%d:M%d,%sB%d:M%d)'
          % (Q_TES, T['estacionalidad'], T['estacionalidad'],
             Q_TES, T['rampa'], T['rampa'])), C.PCT,
       'NO se teclea: sale de la estacionalidad y de la rampa de la hoja de '
       'Tesorería. Un local que abre no factura desde el primer día lo que '
       'factura a los seis meses, y proyectar el año 1 a velocidad de crucero '
       'es el error que más planes de negocio tumba. Aquí además la apertura '
       'es el 1 de junio, así que la rampa cae justo sobre el valle de agosto.')
    ent('crec_a3', 'Crecimiento de volumen del año 3 (%)', 0.04, C.PCT,
        'SUPUESTO. El año 2 ya es el de crucero: el año 3 sólo crece lo que dé '
        'la clientela fija y la agenda corporativa que repite, no un salto de '
        'negocio. Un 4 % es prudente; si pones más, tendrás que decir de dónde '
        'sale.')

    # --- IVA Y TIPOS ------------------------------------------------------
    ent('iva_prod', 'IVA del chocolate y la bombonería (%)',
        D.P('iva_producto'), C.PCT,
        'El 10 % sale POR EXCLUSIÓN, no porque un precepto nombre al '
        'chocolate: la lista del 4 % del art. 91.Dos.1.1.o es cerrada y tiene '
        'siete letras, el chocolate no está en ninguna, y tampoco está entre '
        'las dos exclusiones del 10 % (bebidas alcohólicas y refrescantes).',
        id_chn='CHN-71')
    ent('iva_taza', 'IVA del chocolate a la taza SERVIDO en sala (%)',
        D.P('iva_taza_servida'), C.PCT,
        'La taza servida en sala es una prestación de servicio de hostelería, '
        'no la entrega de un bien: va al 10 % por el art. 91.Uno.2.2.o. La '
        'tableta para taza que te llevas a casa es una entrega de bien, y va '
        'por la línea de arriba.', id_chn='CHN-71c')
    fila = S['iva_taller']
    motor.val(ws, 'A%d' % fila, 'IVA de los talleres y catas (%)')
    C.entrada(ws, 'B%d' % fila, 'Pregúntaselo a tu asesor',
              etiqueta='IVA de los talleres y catas')
    C.nota_celda(ws, 'B%d' % fila, 'CHN-71b')
    C.nota(ws, 'C%d' % fila,
           'VA SIN CIFRA A PROPÓSITO, y no es un olvido. Lo que SÍ está '
           'cerrado: un taller de bombonería NO está exento de IVA, porque el '
           'art. 20.Uno.10.o excluye de la exención las clases «para cuya '
           'realización sea necesario darse de alta en las tarifas de '
           'actividades empresariales o artísticas del IAE». Lo que NO está '
           'cerrado es el TIPO: el art. 91 no nombra los talleres. Esta guía '
           'no publica una cifra que no pueda sostener; escribe tú la que te '
           'diga tu asesor.')
    ws.row_dimensions[fila].height = 30
    ent('iva_gen', 'IVA general (%)', D.P('iva_general'), C.PCT,
        'Tipo general del art. 90.Uno de la Ley 37/1992. Es el que soportas en '
        'obra, maquinaria, moldes, packaging y servicios. Sin la columna de '
        'IVA por línea el CAPEX sale hasta un 21 % desviado, que es el error '
        'más caro de todo el proceso.')
    ent('iva_compras', 'IVA medio de las compras de materia prima (%)',
        D.P('iva_producto'), C.PCT,
        'SUPUESTO de trabajo: la cobertura y los frutos secos van al 10 % y el '
        'packaging al 21 %. Sólo afecta a la TESORERÍA (lo que adelantas al '
        'proveedor), nunca al resultado. Pídele a tu distribuidor una factura '
        'de ejemplo y afínalo.')
    fx('iva_medio', 'IVA medio ponderado de la carta (%)',
       ie('$B$%d' % S['iva_prod']), C.PCT2,
       'Hoy toda la carta va al 10 %, así que el IVA medio es ése. Esta celda '
       'existe para que el día que entres una referencia a otro tipo -una '
       'bebida, por ejemplo- no haya que tocar el libro entero: cambias aquí y '
       'el ticket sin IVA, la tesorería y el modelo 303 te siguen.')

    # --- COSTE DE VENTAS --------------------------------------------------
    ent('fc_escandallo', 'Food cost de escandallo de la carta (%)',
        DEF_FC_CARTA, C.PCT2,
        'Coste de MATERIA sobre PVP, los dos en BASE IMPONIBLE, ponderado por '
        'los euros que vende cada referencia. Sale del libro '
        '«carta-de-apertura-y-escandallo-chocolate». Ojo con la base: el '
        'precio de la cobertura que publica la fuente lleva el IVA dentro, y '
        'un escandallo hecho con esa base sale un 9 % alto.')
    ent('packaging', 'Peso del packaging sobre el coste de la pieza (%)',
        D.P('packaging_pct_coste'), C.PCT,
        'SUPUESTO. En bombonería pesa más que en pastelería: la caja ES el '
        'producto en las campañas de regalo, y el 23 % de diferencia de precio '
        'por bombón entre la caja de 12 y la de 35 se juega ahí.')
    fx('food_cost', 'Coste de ventas sobre las ventas (food cost del P&L, %)',
       ie('$B$%d*(1+$B$%d)' % (S['fc_escandallo'], S['packaging'])), C.PCT2,
       'SE DERIVA: escandallo + packaging. Es el que proyecta el P&L, y es '
       'MAYOR que el de una pieza suelta a propósito. Si además revendes '
       'producto de terceros o tienes merma de producto fresco por encima de '
       'la que ya lleva el escandallo, súbelo tú.')
    ent('fc_objetivo', 'Food cost OBJETIVO de la casa (regla única, %)',
        D.P('food_cost_objetivo'), C.PCT,
        'SUPUESTO declarado: no existe dato público de food cost de '
        'bombonería. Es la regla única de la casa, y el margen bruto objetivo '
        'de la línea de abajo se DERIVA de él: guardar los dos por separado es '
        'un error de método, porque antes o después dicen cosas distintas.')
    fx('margen_obj', 'Margen bruto objetivo (%)',
       ie('1-$B$%d' % S['fc_objetivo']), C.PCT,
       'Se DERIVA del food cost objetivo. Margen bruto y food cost son la '
       'misma regla dicha dos veces.')
    fx('brecha', 'Brecha entre el food cost del P&L y el objetivo (puntos)',
       ie('$B$%d-$B$%d' % (S['food_cost'], S['fc_objetivo'])), C.PCT2,
       'En NEGATIVO estás por debajo del objetivo, y esa diferencia es tu '
       'colchón. En positivo, tu carta no llega a la regla de la casa: o suben '
       'los precios, o baja el coste de la cobertura, o cambia el mix.')
    motor.semaforo_isnumber(ws, 'B%d:B%d' % (S['brecha'], S['brecha']),
                            '$B$%d' % S['brecha'], operador='>', umbral='0')

    # --- PERSONAL ---------------------------------------------------------
    motor.escribir_parametro(ws, S['ss'], 'A', 'B', 'ss_empresa', col_nota='C')
    C.VERDES.append((ws.title, 'B%d' % S['ss'],
                     motor.PARAMETROS['ss_empresa']['etiqueta'],
                     motor.PARAMETROS['ss_empresa']['valor']))
    ent('pagas', 'Número de pagas del convenio', D.P('pagas_convenio'), C.ENT,
        'El convenio de referencia paga 15, no 14, y eso cambia el coste mes a '
        'mes y el reparto de la tesorería. Busca el tuyo: NO existe convenio '
        'estatal del chocolate, está comprobado en el registro oficial.',
        id_chn='CHN-65b')
    motor.escribir_parametro(ws, S['smi'], 'A', 'B', 'smi_anual', col_nota='C')
    C.VERDES.append((ws.title, 'B%d' % S['smi'],
                     motor.PARAMETROS['smi_anual']['etiqueta'],
                     motor.PARAMETROS['smi_anual']['valor']))
    C.nota_celda(ws, 'B%d' % S['smi'], 'CHN-67')
    ent('horas_sem', 'Jornada completa (horas/semana)',
        D.P('horas_semana_jornada_completa'), C.ENT,
        'SUPUESTO: la jornada anual del convenio de referencia no se ha '
        'verificado. Comprueba la del tuyo antes de dimensionar turnos.')

    # --- LOCAL Y GASTOS FIJOS ---------------------------------------------
    ent('renta', 'Alquiler mensual del local (€)', D.NEGOCIO['renta_mensual'],
        C.EUR,
        'SUPUESTO para una ciudad media. La renta observada en los ocho '
        'traspasos verificados va de 910 €/mes (74 m2 en Madrid-Vallecas) a '
        '2.200 €/mes (180 m2 en Barcelona); aquí se toma la parte baja porque '
        'ninguna de esas dos ciudades es una ciudad media.')
    ent('fianza_meses', 'Fianza del alquiler (meses de renta)',
        D.NEGOCIO['meses_fianza'], C.ENT,
        'SUPUESTO. La fianza no es un gasto: es un depósito que se recupera. '
        'Está dentro del CAPEX del libro 2 porque hay que tenerla el día de la '
        'firma, y por eso no se amortiza.')
    ent('suministros', 'Suministros mensuales de luz, agua y climatización (€)',
        780.0, C.EUR,
        'SUPUESTO. Un obrador de chocolate NO tiene hornos, pero tiene TRES '
        'equipos de frío y una climatización con deshumidificación funcionando '
        '24 horas, y en agosto a pleno. No se estima: se le pide la simulación '
        'a la comercializadora con la potencia del proyecto eléctrico.')
    ent('autonomos', 'Cuota de autónomos del titular (€/mes)', 320.0, C.EUR,
        'SUPUESTO, y va como renglón propio de los fijos. El titular de este '
        'caso es el Encargado, y su retribución YA está en la nómina de la '
        'hoja de Personal: ponerle además una «retribución del propietario» '
        'sería contarlo dos veces. Lo que va aparte es la cuota.')
    ent('subida', 'Subida anual de los costes fijos (%)', 0.0, C.PCT,
        'A CERO: las tres columnas del P&L están en euros del año 1 (términos '
        'reales). Súbela si quieres proyectar en euros corrientes, pero '
        'entonces sube también el ticket medio o estarás proyectando una '
        'pérdida de margen que no has decidido.')

    # --- FINANCIACIÓN -----------------------------------------------------
    ent('propios', 'Recursos propios aportados (€)', DEF_PROPIOS, C.EUR,
        'SUPUESTO sembrado para que el plan quede financiado: es la necesidad '
        'total de caja menos el préstamo. Míralo dos veces, porque es mucho '
        'dinero: si no lo tienes, o baja la inversión (mira la hoja «Traspaso '
        'vs Obra Nueva» del libro de CAPEX) o sube el préstamo, y entonces '
        'vigila el DSCR de la hoja de Financiación.')
    ent('principal', 'Préstamo bancario solicitado (€)',
        D.principal_prestamo(), C.EUR,
        'SUPUESTO: el 60 % de la inversión total, redondeado a centenas, que '
        'es la estructura 40/60 del caso. Las condiciones las pone tu banco y '
        'dependen de la garantía. Pide oferta a dos entidades y a una línea '
        'ICO antes de fijarlo.')
    ent('tipo', 'Tipo de interés nominal anual (%)',
        D.FINANCIACION['tipo_nominal'], C.PCT2, 'SUPUESTO.')
    ent('plazo', 'Plazo total del préstamo (meses)',
        D.FINANCIACION['plazo_meses'], C.ENT,
        'SUPUESTO: 7 años, carencia incluida. El cuadro de amortización de la '
        'hoja de Financiación tiene 84 filas; si alargas el plazo por encima '
        'de 84 meses, tendrás que añadirlas.')
    ent('carencia', 'Carencia de principal (meses)',
        D.FINANCIACION['carencia_meses'], C.ENT,
        'SUPUESTO, y es lo PRIMERO que hay que negociar: la carencia es lo que '
        'hace que el préstamo no se coma la caja justo en la rampa de '
        'arranque. Durante la carencia sólo se pagan intereses.')
    ent('colchon', 'Fondo de maniobra (meses de gastos fijos)',
        D.P('meses_colchon_fondo_maniobra'), C.ENT,
        'SUPUESTO, y ESTE ES EL ÚNICO SITIO DEL PACK DONDE SE DECIDE. Meses de '
        'gastos fijos que hay que tener en caja el día que abres. El libro de '
        'CAPEX no te lo vuelve a preguntar: recibe el fondo ya calculado desde '
        'aquí. Si se pidiera en los dos, el fondo se calcularía dos veces y '
        'los dos libros publicarían dos inversiones totales distintas.')

    # --- FISCAL -----------------------------------------------------------
    ent('is_nueva', 'Impuesto de Sociedades, entidad de nueva creación (%)',
        0.15, C.PCT,
        'Art. 29.1 de la Ley del Impuesto sobre Sociedades: se aplica al '
        'PRIMER ejercicio con base imponible positiva y al siguiente, no a los '
        'dos primeros años naturales. Si eres autónomo y no sociedad, esta '
        'línea no te aplica: tributas en IRPF.')
    ent('is_gen', 'Impuesto de Sociedades, tipo general (%)', 0.25, C.PCT,
        'A partir del tercer ejercicio con base positiva.')
    ent('bases_neg', 'Bases negativas de ejercicios anteriores (€)', 0.0,
        C.EUR,
        'Pérdidas pendientes de compensar al empezar. En una apertura son '
        'cero: se rellena si arrancas dentro de una sociedad que ya existía.')

    # --- AMORTIZACIÓN -----------------------------------------------------
    ent('anios_amort', 'Años de amortización del inmovilizado',
        D.P('anios_amortizacion'), C.ENT,
        'SUPUESTO, y en la práctica obra y maquinaria tienen coeficientes '
        'distintos. Sin amortización la rentabilidad publicada es mentira: la '
        'atemperadora se gasta.')

    # --- ARRANQUE ---------------------------------------------------------
    ent('rampa1', 'Actividad del mes 1 sobre la de crucero (%)',
        D.RAMPA['mes1'], C.PCT,
        'SUPUESTO. Con el 100 % eliminas la rampa y el año 1 se proyecta como '
        'si abrieras a pleno rendimiento, que es justo lo que no pasa.')
    ent('rampa_meses', 'Meses hasta alcanzar el régimen de crucero',
        D.RAMPA['meses'], C.ENT,
        'SUPUESTO. La rampa sube en línea recta desde el porcentaje de arriba '
        'hasta el 100 % en este número de meses.')
    ent('mes_apertura', 'Mes de apertura (1-12)',
        D.NEGOCIO['mes_apertura_recomendado'], C.ENT,
        'SUPUESTO: el 1 de junio. Junio es «Media» en el calendario de '
        'campañas del kit, deja SEIS meses de rodaje antes de Navidad y mete '
        'el valle de agosto dentro del arranque, que es cuando sale barato. '
        'Abrir dentro de una campaña «Alta» es el error que avisa el '
        'cronograma del libro de licencias.')
    ent('dias_semana', 'Días de apertura a la semana',
        D.NEGOCIO['dias_apertura_semana'], C.ENT,
        'SUPUESTO. Lo usa el cálculo de la fecha límite de Navidad para pasar '
        'de días de PRODUCCIÓN a días de calendario: si produces seis días de '
        'cada siete, cada día de obrador son 1,17 días naturales.')

    # --- COBROS Y PAGOS ---------------------------------------------------
    fx('dias_cobro', 'Días medios de cobro',
       ie('SUMPRODUCT(%sB%d:B%d,%sG%d:G%d)'
          % (Q_CAN, K_INI, K_FIN, Q_CAN, K_INI, K_FIN)), C.DEC1,
       'NO se teclea: sale de la hoja «Canales y Punto Muerto», ponderando los '
       'días de cobro de cada canal por su peso en las ventas. El mostrador y '
       'el taller cobran al contado; el corporativo, a 30 días, y el B2B a 45: '
       'ahí financias tú.')
    ent('dias_pago', 'Días medios de pago a proveedor', 30, C.ENT,
        'SUPUESTO. Es lo que te financian tus proveedores, y lo primero que se '
        'pierde si te retrasas en un pago. Ojo en septiembre y octubre: es '
        'cuando se paga la cobertura de Navidad.')
    ent('extra1', 'Mes de la primera paga extra (1-12)', 7, C.ENT,
        'SUPUESTO. Con 15 pagas hay TRES meses en los que la nómina sale '
        'doble; escribe aquí en cuáles cae en tu convenio.')
    ent('extra2', 'Mes de la segunda paga extra (1-12)', 12, C.ENT,
        'SUPUESTO. Diciembre es el mes de más caja y de más nómina a la vez.')
    ent('extra3', 'Mes de la tercera paga extra (1-12)', 3, C.ENT,
        'SUPUESTO. Si tu convenio paga 14, pon aquí un número fuera de 1-12 '
        '(por ejemplo 0) y baja a 14 las pagas de arriba.')

    # --- UMBRALES ---------------------------------------------------------
    ent('dscr_min', 'DSCR mínimo aceptable', 1.0, C.DEC,
        'Por debajo de 1 el negocio no genera lo suficiente para pagar el '
        'préstamo. Pon el que te exija tu banco en el contrato.')
    ent('dscr_obj', 'DSCR objetivo (verde)', 1.25, C.DEC,
        'Lo que suele pedir una entidad para dar el préstamo sin garantías '
        'adicionales.')
    ent('holgura', 'Holgura mínima sobre el punto de equilibrio (%)', 0.15,
        C.PCT,
        'Cuánto puedes caer sobre lo previsto antes de entrar en pérdidas. Con '
        'un negocio tan estacional como éste, la holgura no es un lujo: es lo '
        'que te deja llegar a octubre.')
    ent('neto_suelo', 'Margen neto de referencia, suelo (%)', 0.08, C.PCT,
        'SUPUESTO DE CONTROL, no un dato del sector: NO existe rentabilidad '
        'publicada de bombonería artesana en España. Está aquí para que '
        'contrastes tu proyección, no para que la persigas.')
    ent('neto_techo', 'Margen neto de referencia, techo (%)', 0.12, C.PCT,
        'SUPUESTO DE CONTROL. Si tu proyección sale por encima, desconfía '
        'antes de enseñarla: casi siempre falta un coste.')
    ent('techo_personal', 'Techo de coste de personal sobre ventas (%)', 0.35,
        C.PCT,
        'SUPUESTO de control. En un obrador con tienda el personal es la '
        'primera partida; por encima de este techo, o subes precios o '
        'redimensionas turnos.')
    ent('techo_alquiler', 'Techo de alquiler sobre ventas (%)', 0.10, C.PCT,
        'SUPUESTO de control. Un alquiler por encima del 10 % de las ventas se '
        'come el margen de todo lo demás, y no se renegocia una vez firmado.')
    ent('paso_sens', 'Paso de la sensibilidad del coste variable (€)', 0.20,
        C.EUR,
        'Cuánto sube y baja el coste variable por ticket en la tabla de '
        'sensibilidad del punto de equilibrio. Con el cacao como está, la '
        'columna de la derecha no es un ejercicio teórico.')
    ent('tolerancia', 'Tolerancia de los cuadres entre libros (%)', 0.02,
        C.PCT,
        'Cuánto puede alejarse una cifra traída de otro libro antes de que su '
        'fila de CUADRE se ponga en rojo. Un 2 % tolera el redondeo; una '
        'máquina distinta, no.')

    ws.freeze_panes = 'A6'
    C.pagina(ws, apaisado=False, titulos='$5:$5',
             area='A1:C%d' % S['tolerancia'])
    return ws


# ==========================================================================
# Hoja «Inversión Inicial» (cruce 7 <- 2 y origen del cruce 2 <- 7)
# ==========================================================================
def hoja_inversion(wb):
    ws = wb.create_sheet(H_INV)
    C.anchos(ws, {'A': 60, 'B': 17, 'C': 14, 'D': 92})
    C.encabezar(ws, 'Inversión inicial: la cifra que viene y la que se dota '
                    'aquí',
                'Esta hoja NO te vuelve a pedir las nueve partidas del CAPEX: '
                'eso lo hace el libro «calculadora-capex-chocolateria». Aquí '
                'entra UNA cifra suya -el CAPEX SIN el fondo de maniobra- y se '
                'DOTA el fondo de maniobra con tus meses de colchón y tus '
                'gastos fijos. El fondo se calcula una sola vez en todo el '
                'pack, y es aquí.', col_fin='D')

    def linea(clave, etiqueta, formula=None, fmt=C.EUR, nota_txt=None,
              verde=None, bold=None):
        fila = IV[clave]
        motor.val(ws, 'A%d' % fila, etiqueta, bold=bold, wrap=True)
        if verde is not None:
            C.entrada(ws, 'B%d' % fila, verde, fmt=fmt, etiqueta=etiqueta,
                      bold=bold)
        elif formula is not None:
            motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=bold)
        if nota_txt:
            C.nota(ws, 'D%d' % fila, nota_txt)
        return 'B%d' % fila

    # --- cruce 7 <- 2 -----------------------------------------------------
    C.banda(ws, IV['sec_cruce'], 'ABCD',
            'LO QUE VIENE DEL LIBRO DE CAPEX (cruce 7 ' + chr(60) + '- 2)')
    linea('capex_trae',
          'CAPEX SIN el fondo de maniobra: trae aquí la cifra de '
          + ORIGEN_CAPEX, verde=DEF_CAPEX,
          nota_txt='CÓPIALA A MANO. No hay ninguna fórmula entre ficheros: un '
                   'enlace se rompe en cuanto alguien mueve una carpeta, y '
                   'entonces el libro miente sin avisar. Y OJO CON CUÁL '
                   'COPIAS: NO es «el CAPEX total». El total de aquel libro '
                   'lleva DENTRO el bloque «fondo de maniobra», y este libro '
                   'vuelve a dotarlo tres filas más abajo: traer el total '
                   'contaría el fondo dos veces y publicaría dos inversiones '
                   'totales distintas para la misma bombonería. VALOR POR '
                   'DEFECTO DECLARADO: el del caso «La Almendra».')
    ws.row_dimensions[IV['capex_trae']].height = 44
    linea('capex_orig', 'Cifra que publica hoy esa celda del libro de CAPEX',
          verde=DEF_CAPEX,
          nota_txt='Anota aquí lo que ves en el libro 2 la última vez que lo '
                   'abriste. Si arriba tecleas otra cosa -porque has cerrado '
                   'un presupuesto mejor, o porque el instalador te ha subido '
                   'la climatización-, la fila de CUADRE te avisa en vez de '
                   'dejar las dos cifras separadas en silencio.')
    motor.val(ws, 'A%d' % IV['capex_desv'], 'Desviación entre las dos')
    motor.f(ws, 'B%d' % IV['capex_desv'],
            ie('ABS(B%d-B%d)/B%d'
               % (IV['capex_trae'], IV['capex_orig'], IV['capex_orig'])),
            fmt=C.PCT2)
    motor.val(ws, 'A%d' % IV['capex_cuadre'],
              'CUADRE DEL CAPEX: lo que usas frente a lo que publica el libro 2',
              bold=True)
    motor.f(ws, 'B%d' % IV['capex_cuadre'],
            ie('IF(NOT(ISNUMBER(B%d)),"",IF(B%d<=%s,"CUADRA","REVISA: el '
               'CAPEX que estás usando no es el que publica el libro 2"))'
               % (IV['capex_desv'], IV['capex_desv'], sup('tolerancia'))),
            bold=True)
    C.destacado(ws, 'B%d' % IV['capex_cuadre'])
    motor.semaforo_texto(ws, 'B%d' % IV['capex_cuadre'],
                         (('REVISA: el CAPEX que estás usando no es el que '
                           'publica el libro 2', motor.CF_ROJO_BG,
                           motor.CF_ROJO_FG),
                          ('CUADRA', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    C.nota(ws, 'D%d' % IV['capex_cuadre'],
           'Es la red de seguridad de todo el pack: dos libros que dicen cosas '
           'distintas sobre la misma inversión es el defecto que más caro sale '
           'y el que menos se nota.')
    linea('iva_sop', 'IVA soportado sobre la inversión, traído del libro 2',
          verde=DEF_IVA_CAPEX,
          nota_txt='Copia de ' + ORIGEN_IVA + '. Se recupera por el modelo '
                   '303, pero hay que ADELANTARLO: la hoja de Tesorería lo '
                   'arrastra trimestre a trimestre, y esa espera es la partida '
                   'que más sorprende al que abre.')
    ws.row_dimensions[IV['iva_sop']].height = 30
    linea('amortizable', 'Inmovilizado amortizable, traído del libro 2',
          verde=DEF_AMORTIZABLE,
          nota_txt='El CAPEX menos la FIANZA (que es un depósito y se '
                   'recupera) y menos el primer pedido de packaging y moldes '
                   'de consumo (que son existencias, no inmovilizado). De aquí '
                   'sale la amortización anual que entra en los costes fijos.')
    ws.row_dimensions[IV['amortizable']].height = 30

    # --- el fondo de maniobra, dotado aquí --------------------------------
    C.banda(ws, IV['sec_fondo'], 'ABCD',
            'EL FONDO DE MANIOBRA SE DOTA AQUÍ (y viaja al libro 2 ya '
            'calculado: cruce 2 ' + chr(60) + '- 7)')
    linea('fijos_mes', 'Gastos fijos mensuales del año de crucero (€)',
          formula=ie('%sC%d/12' % (Q_PYG, P['tot_fijos'])), bold=True,
          nota_txt='El total de costes fijos del AÑO 2 del P&L dividido entre '
                   'doce. Es la foto de un mes normal: por eso lleva dentro la '
                   'amortización y los intereses del AÑO DE CRUCERO, no los '
                   'del año 1, que es el de la carencia. Ésta es una de las '
                   'dos celdas que cita el resto del pack.')
    C.total_fila(ws, IV['fijos_mes'], 'ABCD')
    linea('colchon', 'Meses de colchón (de «0. Supuestos»)',
          formula=ie(sup('colchon')), fmt=C.ENT,
          nota_txt='Se decide en «0. Supuestos», y sólo allí. El libro de '
                   'CAPEX no lo pregunta.')
    linea('fondo', 'FONDO DE MANIOBRA (€)',
          formula=ie('B%d*B%d' % (IV['fijos_mes'], IV['colchon'])), bold=True,
          nota_txt='Meses de colchón x gastos fijos mensuales. ES LA CIFRA QUE '
                   'VIAJA AL LIBRO 2: cópiala allí en su celda verde del '
                   'cruce, y su fila de CUADRE te dirá si las dos siguen '
                   'diciendo lo mismo. No es inversión que se compra: es caja, '
                   'y es lo que te deja llegar a octubre del primer año.')
    C.total_fila(ws, IV['fondo'], 'ABCD')

    # --- la inversión, en dos líneas --------------------------------------
    C.banda(ws, IV['sec_inv'], 'ABCD', 'LA INVERSIÓN, EN DOS LÍNEAS')
    linea('capex', 'CAPEX (lo que se compra, sin el fondo de maniobra)',
          formula=ie('B%d' % IV['capex_trae']),
          nota_txt='Obra, climatización, equipo de templado, frío, mobiliario, '
                   'packaging y moldes, TPV y rótulo, fianza y licencias.')
    motor.f(ws, 'C%d' % IV['capex'],
            ie('B%d/B%d' % (IV['capex'], IV['total'])), fmt=C.PCT)
    linea('fdm', 'Del cual NO forma parte: el fondo de maniobra (es caja)',
          formula=ie('B%d' % IV['fondo']))
    motor.f(ws, 'C%d' % IV['fdm'],
            ie('B%d/B%d' % (IV['fdm'], IV['total'])), fmt=C.PCT)
    linea('total', 'INVERSIÓN TOTAL (lo que se compra más la caja del '
                   'arranque)',
          formula=ie('B%d+B%d' % (IV['capex'], IV['fdm'])), bold=True,
          nota_txt='Esta cifra y la que publica el libro de CAPEX tienen que '
                   'ser IDÉNTICAS, y lo son por construcción: aquel libro '
                   'publica el CAPEX ya depurado de fondo y éste le devuelve '
                   'el fondo ya calculado.')
    C.total_fila(ws, IV['total'], 'ABCD')
    linea('iva', 'IVA soportado sobre la inversión (recuperable, pero hay que '
                 'ADELANTARLO)',
          formula=ie('B%d' % IV['iva_sop']))
    linea('necesidad', 'NECESIDAD TOTAL DE CAJA AL ARRANQUE',
          formula=ie('B%d+B%d' % (IV['total'], IV['iva'])), bold=True,
          nota_txt='Es la cifra que tiene que cubrir la hoja de Financiación. '
                   'Si el origen de fondos no llega aquí, el plan no está '
                   'financiado, y da igual lo bonito que sea el P&L.')
    C.total_fila(ws, IV['necesidad'], 'ABCD')

    # --- bases de amortización --------------------------------------------
    C.banda(ws, IV['sec_am'], 'ABCD',
            'BASES DE AMORTIZACIÓN (no suman a la inversión)')
    linea('base', 'Inmovilizado amortizable',
          formula=ie('B%d' % IV['amortizable']),
          nota_txt='El que has traído del libro 2. Ni la fianza ni el fondo de '
                   'maniobra se amortizan: la primera se recupera y el segundo '
                   'es caja.')
    linea('amort', 'Amortización anual del inmovilizado',
          formula=ie('B%d/MAX(1,%s)' % (IV['base'], sup('anios_amort'))),
          nota_txt='Es la línea que entra en los costes fijos del P&L. Sin '
                   'ella la rentabilidad publicada es mentira: la atemperadora '
                   'se gasta, y la cámara de chocolate también.')

    C.parrafo(ws, IV['nota'],
              'Todas las cifras van en BASE SIN IVA. El IVA de la inversión se '
              'trae aparte, arriba, para que puedas ver cuánto dinero tienes '
              'que adelantar y cuánto vas a recuperar. Y una advertencia que '
              'vale dinero: la renta que pagues ANTES de abrir no está aquí. '
              'Si la vas a pagar, súmala en el libro de CAPEX a la línea de '
              'fianza y dilo en su nota, para que los dos libros sigan '
              'diciendo lo mismo.', 'A', 'D', alto=46)
    C.pagina(ws, apaisado=False, area='A1:D%d' % IV['nota'])
    return ws


# ==========================================================================
# Hoja «PyG 3 Años»
# ==========================================================================
def hoja_pyg(wb):
    ws = wb.create_sheet(H_PYG)
    C.anchos(ws, {'A': 58, 'B': 15, 'C': 15, 'D': 15, 'E': 13, 'F': 13,
                  'G': 80})
    C.encabezar(ws, 'Cuenta de resultados a 3 años',
                'El AÑO 2 es el año de crucero: es el que citan la guía y el '
                'business plan. El año 1 lleva la rampa de arranque -y el '
                'valle de agosto dentro- y el año 3 crece sobre el crucero. '
                'Amortización, intereses y la cuota de autónomos del titular '
                'van DENTRO de los costes fijos.', col_fin='G')
    C.cabecera(ws, P['cab'], [('A', 'Concepto'), ('B', 'Año 1 (arranque)'),
                              ('C', 'Año 2 (crucero)'), ('D', 'Año 3'),
                              ('E', '% s/ventas (año 2)'),
                              ('F', 'Tipo de IVA de la línea'), ('G', 'Notas')])

    def sec(fila, texto):
        C.banda(ws, fila, 'ABCDEFG', texto)

    def pct(fila):
        motor.f(ws, 'E%d' % fila, ie('C%d/$C$%d' % (fila, P['ingresos'])),
                fmt=C.PCT)

    # --- ingresos ---------------------------------------------------------
    sec(P['sec_ing'], 'INGRESOS')
    motor.val(ws, 'A%d' % P['tickets'], 'Clientes al día')
    motor.f(ws, 'B%d' % P['tickets'], ie(sup('tickets')), fmt=C.ENT)
    motor.f(ws, 'C%d' % P['tickets'], ie(sup('tickets')), fmt=C.ENT)
    motor.f(ws, 'D%d' % P['tickets'],
            ie('C%d*(1+%s)' % (P['tickets'], sup('crec_a3'))), fmt=C.ENT)
    C.nota(ws, 'G%d' % P['tickets'],
           'Los años 1 y 2 comparten el tráfico de crucero; lo que separa al '
           'año 1 es la rampa de la fila de abajo, no menos clientes al día en '
           'el mes 12.')

    motor.val(ws, 'A%d' % P['ticket'], 'Ticket medio sin IVA (€)')
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['ticket']), ie(sup('ticket_sin')),
                fmt=C.EUR)
    C.nota(ws, 'G%d' % P['ticket'],
           'Constante en euros del año 1: una subida de precios es una '
           'decisión aparte, y se toma en la carta, no aquí.')

    motor.val(ws, 'A%d' % P['dias'], 'Días de apertura al año')
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['dias']), ie(sup('dias')), fmt=C.ENT)

    motor.val(ws, 'A%d' % P['actividad'],
              'Actividad sobre la velocidad de crucero (%)')
    motor.f(ws, 'B%d' % P['actividad'], ie(sup('factor_a1')), fmt=C.PCT)
    C.entrada(ws, 'C%d' % P['actividad'], 1.0, fmt=C.PCT,
              etiqueta='Actividad del año 2 sobre el crucero')
    C.entrada(ws, 'D%d' % P['actividad'], 1.0, fmt=C.PCT,
              etiqueta='Actividad del año 3 sobre el crucero')
    C.nota(ws, 'G%d' % P['actividad'],
           'El año 1 lo calcula «0. Supuestos» desde la rampa y la '
           'estacionalidad de la hoja de Tesorería. Los años 2 y 3 están al '
           '100 % porque el año 2 es, por definición, el de crucero: si crees '
           'que vas a tardar más en llegar, bájalos.')

    motor.val(ws, 'A%d' % P['ingresos'], 'INGRESOS TOTALES (sin IVA)',
              bold=True)
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['ingresos']),
                ie('IF({0}{1}*{0}{2}*{0}{3}*{0}{4}=0,"",{0}{1}*{0}{2}*{0}{3}'
                   '*{0}{4})'.format(col, P['tickets'], P['ticket'],
                                     P['dias'], P['actividad'])),
                fmt=C.EUR, bold=True)
    pct(P['ingresos'])
    motor.f(ws, 'F%d' % P['ingresos'], ie(sup('iva_medio')), fmt=C.PCT2)
    C.nota_celda(ws, 'F%d' % P['ingresos'], 'CHN-71')
    C.total_fila(ws, P['ingresos'], 'ABCDEFG')
    C.nota(ws, 'G%d' % P['ingresos'],
           'Clientes x ticket medio sin IVA x días x actividad. El reparto por '
           'canal está en la hoja «Canales y Punto Muerto»: aquí es UNA cifra, '
           'porque lo que cambia por canal es el MARGEN, no el precio.')

    # --- variables --------------------------------------------------------
    sec(P['sec_var'], 'COSTES VARIABLES')
    motor.val(ws, 'A%d' % P['coste_ventas'],
              'Coste de ventas (cobertura, rellenos, packaging y merma)')
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['coste_ventas']),
                ie('IF({0}{1}="","",{0}{1}*{2})'
                   .format(col, P['ingresos'], sup('food_cost'))), fmt=C.EUR)
    pct(P['coste_ventas'])
    motor.f(ws, 'F%d' % P['coste_ventas'], ie(sup('iva_compras')), fmt=C.PCT)
    C.nota(ws, 'G%d' % P['coste_ventas'],
           'Al food cost DERIVADO de «0. Supuestos»: el de escandallo de la '
           'carta más el packaging. La materia prima que manda aquí es la '
           'cobertura, y su precio vive en el libro '
           '«sensibilidad-al-precio-del-cacao» EN BASE IMPONIBLE: si copias el '
           'precio con IVA, este renglón sale un 9 % alto.')

    motor.val(ws, 'A%d' % P['tot_var'], 'TOTAL COSTES VARIABLES', bold=True)
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['tot_var']),
                ie('IF({0}{1}="","",{0}{2})'
                   .format(col, P['ingresos'], P['coste_ventas'])),
                fmt=C.EUR, bold=True)
    pct(P['tot_var'])
    C.total_fila(ws, P['tot_var'], 'ABCDEFG')

    motor.val(ws, 'A%d' % P['margen'], 'MARGEN BRUTO', bold=True)
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['margen']),
                ie('IF({0}{1}="","",{0}{1}-{0}{2})'
                   .format(col, P['ingresos'], P['tot_var'])),
                fmt=C.EUR, bold=True)
    pct(P['margen'])
    C.total_fila(ws, P['margen'], 'ABCDEFG')

    # --- fijos ------------------------------------------------------------
    sec(P['sec_fijos'], 'COSTES FIJOS')
    motor.val(ws, 'A%d' % P['personal'],
              'Personal (nóminas y Seguridad Social)')
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['personal']),
                ie('IF({0}{1}="","",{2}$I${3})'
                   .format(col, P['ingresos'], Q_PER, R_TOT)), fmt=C.EUR)
    pct(P['personal'])
    motor.val(ws, 'F%d' % P['personal'], 0.0, fmt=C.PCT)
    C.nota(ws, 'G%d' % P['personal'],
           'Sale de la hoja de Personal: es el MISMO número, no una estimación '
           'aparte, y dentro va la retribución del titular, que es el '
           'Encargado. Las nóminas no llevan IVA. El refuerzo de campañas NO '
           'está aquí: se dimensiona en el libro «campanas-y-valle-del-ano».')

    for clave, etiqueta, sup_clave in (
            ('autonomos', 'Cuota de autónomos del titular', 'autonomos'),
            ('alquiler', 'Alquiler del local', 'renta'),
            ('suministros', 'Suministros (luz, agua y climatización)',
             'suministros')):
        fila = P[clave]
        motor.val(ws, 'A%d' % fila, etiqueta)
        motor.f(ws, 'B%d' % fila,
                ie('IF(B%d="","",%s*12)' % (P['ingresos'], sup(sup_clave))),
                fmt=C.EUR)
        motor.f(ws, 'C%d' % fila,
                ie('IF(C%d="","",B%d*(1+%s))'
                   % (P['ingresos'], fila, sup('subida'))), fmt=C.EUR)
        motor.f(ws, 'D%d' % fila,
                ie('IF(D%d="","",C%d*(1+%s))'
                   % (P['ingresos'], fila, sup('subida'))), fmt=C.EUR)
        pct(fila)
    motor.val(ws, 'F%d' % P['autonomos'], 0.0, fmt=C.PCT)
    motor.f(ws, 'F%d' % P['alquiler'], ie(sup('iva_gen')), fmt=C.PCT)
    motor.f(ws, 'F%d' % P['suministros'], ie(sup('iva_gen')), fmt=C.PCT)
    C.nota(ws, 'G%d' % P['autonomos'],
           'RENGLÓN PROPIO, y es lo ÚNICO que va aparte del titular: su sueldo '
           'ya está en la nómina de arriba, porque el titular de este caso es '
           'el Encargado. Ponerle además una «retribución del propietario» '
           'sería contarlo dos veces.')
    C.nota(ws, 'G%d' % P['alquiler'],
           'El importe mensual está en «0. Supuestos»; aquí se multiplica por '
           'doce. El arrendamiento de local de negocio lleva IVA al tipo '
           'general.')
    C.nota(ws, 'G%d' % P['suministros'],
           'Luz va al 21 % y el agua al 10 %. El libro aplica a toda la '
           'partida el tipo de la columna de al lado: si el agua te pesa, '
           'sepárala en su propia línea. Y ojo en agosto: la climatización con '
           'deshumidificación no para aunque pare el obrador.')

    for clave, i_fijo, tipo, nota_txt in FIJOS_VERDES:
        fila = P[clave]
        etiqueta = D.GASTOS_FIJOS_MENSUALES[i_fijo][0]
        valor = round(D.GASTOS_FIJOS_MENSUALES[i_fijo][1] * 12.0, 2)
        motor.val(ws, 'A%d' % fila, etiqueta)
        C.entrada(ws, 'B%d' % fila, valor, fmt=C.EUR, etiqueta=etiqueta)
        motor.f(ws, 'C%d' % fila,
                ie('IF(C%d="","",B%d*(1+%s))'
                   % (P['ingresos'], fila, sup('subida'))), fmt=C.EUR)
        motor.f(ws, 'D%d' % fila,
                ie('IF(D%d="","",C%d*(1+%s))'
                   % (P['ingresos'], fila, sup('subida'))), fmt=C.EUR)
        pct(fila)
        C.entrada(ws, 'F%d' % fila, tipo, fmt=C.PCT, etiqueta=etiqueta)
        C.nota(ws, 'G%d' % fila, nota_txt + ' Importe ANUAL: el mensual del '
                                 'caso, por doce.')
    C.nota_celda(ws, 'B%d' % P['software'], 'CHN-75')
    C.nota_celda(ws, 'B%d' % P['mantenimiento'], 'CHN-48')

    motor.val(ws, 'A%d' % P['amortizacion'], 'Amortización del inmovilizado')
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['amortizacion']),
                ie('IF({0}{1}="","",{2}$B${3})'
                   .format(col, P['ingresos'], Q_INV, IV['amort'])), fmt=C.EUR)
    pct(P['amortizacion'])
    motor.val(ws, 'F%d' % P['amortizacion'], 0.0, fmt=C.PCT)
    C.nota(ws, 'G%d' % P['amortizacion'],
           'Sale de la base de amortización de la hoja de Inversión. No sube '
           'con el IPC: es un reparto contable de una inversión ya hecha.')

    motor.val(ws, 'A%d' % P['financieros'], 'Gastos financieros del préstamo')
    for col, anio in (('B', 0), ('C', 1), ('D', 2)):
        motor.f(ws, '%s%d' % (col, P['financieros']),
                ie('IF({0}{1}="","",{2}$B${3})'
                   .format(col, P['ingresos'], Q_FIN, F_ANIO_INI + anio)),
                fmt=C.EUR)
    pct(P['financieros'])
    motor.val(ws, 'F%d' % P['financieros'], 0.0, fmt=C.PCT)
    C.nota(ws, 'G%d' % P['financieros'],
           'Sólo los INTERESES son gasto. La devolución del principal sale de '
           'la caja pero no del resultado: va en la hoja de Tesorería. Los que '
           'usa el fondo de maniobra son los del AÑO 2, no los del año 1, que '
           'es el de la carencia.')

    motor.val(ws, 'A%d' % P['tot_fijos'], 'TOTAL COSTES FIJOS', bold=True)
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['tot_fijos']),
                ie('IF({0}{1}="","",SUM({0}{2}:{0}{3}))'
                   .format(col, P['ingresos'], P['personal'],
                           P['financieros'])), fmt=C.EUR, bold=True)
    pct(P['tot_fijos'])
    C.total_fila(ws, P['tot_fijos'], 'ABCDEFG')
    C.nota(ws, 'G%d' % P['tot_fijos'],
           'De esta celda, columna del año 2 y dividida entre doce, sale el '
           'fondo de maniobra de todo el pack.')

    motor.val(ws, 'A%d' % P['iva_var'],
              'IVA soportado de los costes variables')
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['iva_var']),
                ie('IF({0}{1}="","",{0}{2}*$F${2})'
                   .format(col, P['ingresos'], P['coste_ventas'])), fmt=C.EUR)
    motor.val(ws, 'A%d' % P['iva_fijos'], 'IVA soportado de los costes fijos')
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['iva_fijos']),
                ie('IF({0}{1}="","",SUMPRODUCT({0}{2}:{0}{3},$F${2}:$F${3}))'
                   .format(col, P['ingresos'], P['personal'],
                           P['financieros'])), fmt=C.EUR)
    C.nota(ws, 'G%d' % P['iva_fijos'],
           'Cada línea a SU tipo, leído de la columna de al lado. Es lo que la '
           'hoja de Tesorería paga de más a los proveedores y luego recupera '
           'en el modelo 303.')

    # --- resultado --------------------------------------------------------
    motor.val(ws, 'A%d' % P['rai'], 'RESULTADO ANTES DE IMPUESTOS', bold=True)
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['rai']),
                ie('IF({0}{1}="","",{0}{2}-{0}{3})'
                   .format(col, P['ingresos'], P['margen'], P['tot_fijos'])),
                fmt=C.EUR, bold=True)
    pct(P['rai'])
    C.total_fila(ws, P['rai'], 'ABCDEFG')

    motor.val(ws, 'A%d' % P['bases_ini'],
              'Bases negativas pendientes al inicio')
    motor.f(ws, 'B%d' % P['bases_ini'],
            ie('IF(B%d="","",%s)' % (P['ingresos'], sup('bases_neg'))),
            fmt=C.EUR)
    motor.f(ws, 'C%d' % P['bases_ini'],
            ie('IF(C%d="","",B%d)' % (P['ingresos'], P['bases_fin'])),
            fmt=C.EUR)
    motor.f(ws, 'D%d' % P['bases_ini'],
            ie('IF(D%d="","",C%d)' % (P['ingresos'], P['bases_fin'])),
            fmt=C.EUR)
    C.nota(ws, 'G%d' % P['bases_ini'],
           'Art. 26 de la Ley del Impuesto sobre Sociedades: las pérdidas de '
           'un ejercicio se compensan con los beneficios de los siguientes.')

    motor.val(ws, 'A%d' % P['base_imp'],
              'Base imponible (después de compensar)')
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['base_imp']),
                ie('IF({0}{1}="","",MAX(0,{0}{2}-{0}{3}))'
                   .format(col, P['ingresos'], P['rai'], P['bases_ini'])),
                fmt=C.EUR)
    motor.val(ws, 'A%d' % P['ejercicios'],
              'Ejercicios con base positiva (acumulado)')
    motor.f(ws, 'B%d' % P['ejercicios'],
            ie('IF(B%d="","",IF(B%d>0,1,0))'
               % (P['ingresos'], P['base_imp'])), fmt=C.ENT)
    for col, ant in (('C', 'B'), ('D', 'C')):
        motor.f(ws, '%s%d' % (col, P['ejercicios']),
                ie('IF({0}{1}="","",{2}{3}+IF({0}{4}>0,1,0))'
                   .format(col, P['ingresos'], ant, P['ejercicios'],
                           P['base_imp'])), fmt=C.ENT)
    motor.val(ws, 'A%d' % P['tipo_is'],
              'Tipo de Impuesto de Sociedades aplicado')
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['tipo_is']),
                ie('IF({0}{1}="","",IF({0}{2}<=0,"",IF({0}{3}<=2,{4},{5})))'
                   .format(col, P['ingresos'], P['base_imp'], P['ejercicios'],
                           sup('is_nueva'), sup('is_gen'))), fmt=C.PCT)
    C.nota(ws, 'G%d' % P['tipo_is'],
           'El 15 % de entidad de nueva creación se aplica al PRIMER ejercicio '
           'con base positiva y al siguiente, no a los dos primeros años '
           'naturales. Si tributas en IRPF, esta línea no te aplica.')
    motor.val(ws, 'A%d' % P['is'], 'Impuesto de Sociedades')
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['is']),
                ie('IF({0}{1}="","",IF({0}{2}="",0,{0}{3}*{0}{2}))'
                   .format(col, P['ingresos'], P['tipo_is'], P['base_imp'])),
                fmt=C.EUR)
    motor.val(ws, 'A%d' % P['bases_fin'],
              'Bases negativas pendientes al cierre')
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['bases_fin']),
                ie('IF({0}{1}="","",MAX(0,{0}{2}-{0}{3}))'
                   .format(col, P['ingresos'], P['bases_ini'], P['rai'])),
                fmt=C.EUR)
    motor.val(ws, 'A%d' % P['neto'], 'RESULTADO NETO', bold=True)
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['neto']),
                ie('IF({0}{1}="","",{0}{2}-{0}{3})'
                   .format(col, P['ingresos'], P['rai'], P['is'])),
                fmt=C.EUR, bold=True)
    pct(P['neto'])
    C.total_fila(ws, P['neto'], 'ABCDEFG')
    motor.semaforo_isnumber(ws, 'B%d:D%d' % (P['neto'], P['neto']),
                            'B%d' % P['neto'], operador='<', umbral='0')

    # --- ratios -----------------------------------------------------------
    sec(P['sec_ratios'], 'RATIOS CLAVE')
    C.cabecera(ws, P['cab_ratios'],
               [('A', 'Ratio'), ('B', 'Año 1'), ('C', 'Año 2'), ('D', 'Año 3'),
                ('E', 'Umbral'), ('F', ''), ('G', 'Comentario')], altura=22)
    RATIOS = (
        ('r_margen', 'Margen bruto / ventas', P['margen'], 'margen_obj',
         'El suelo es la regla única de margen del propio libro. Por debajo, o '
         'suben los precios o baja el coste de la cobertura.'),
        ('r_coste', 'Coste de ventas / ventas', P['coste_ventas'],
         'fc_objetivo',
         'Es el food cost proyectado. Cuando midas el tuyo de verdad, con tres '
         'meses de compras y de ventas, cámbialo en «0. Supuestos» y mira qué '
         'le pasa a este cuadro.'),
        ('r_personal', 'Coste de personal / ventas', P['personal'],
         'techo_personal',
         'En un obrador con tienda el personal es la primera partida. Por '
         'encima del techo, o subes precios o redimensionas turnos.'),
        ('r_alquiler', 'Alquiler / ventas', P['alquiler'], 'techo_alquiler',
         'Un alquiler por encima del techo se come el margen de todo lo demás, '
         'y no se renegocia una vez firmado.'),
        ('r_neto', 'Resultado neto / ventas', P['neto'], 'neto_suelo',
         'El suelo es un SUPUESTO de control, no un dato del sector: no existe '
         'rentabilidad publicada de bombonería artesana española.'),
    )
    for clave, etiqueta, fila_origen, umbral, nota_txt in RATIOS:
        fila = P[clave]
        motor.val(ws, 'A%d' % fila, etiqueta)
        for col in 'BCD':
            motor.f(ws, '%s%d' % (col, fila),
                    ie('IF({0}{1}="","",{0}{2}/{0}{1})'
                       .format(col, P['ingresos'], fila_origen)), fmt=C.PCT)
        motor.f(ws, 'E%d' % fila, ie(sup(umbral)), fmt=C.PCT)
        C.nota(ws, 'G%d' % fila, nota_txt)

    motor.val(ws, 'A%d' % P['r_banda'],
              'Margen neto dentro de la banda de referencia')
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['r_banda']),
                ie('IF({0}{1}="","",IF(AND({0}{1}>={2},{0}{1}<={3}),"Sí",'
                   '"No: revísalo"))'.format(col, P['r_neto'],
                                             sup('neto_suelo'),
                                             sup('neto_techo'))))
    C.nota(ws, 'G%d' % P['r_banda'],
           'Si sale por ENCIMA del techo, desconfía antes de enseñarlo: casi '
           'siempre falta un coste. Si sale por debajo del suelo, el negocio '
           'no está mal planteado por fuerza, pero tiene poco donde caerse.')

    motor.val(ws, 'A%d' % P['r_equilibrio'], 'Punto de equilibrio alcanzado')
    for col in 'BCD':
        motor.f(ws, '%s%d' % (col, P['r_equilibrio']),
                ie('IF({0}{1}="","",IF({0}{1}>={2}${0}${3},"Sí","No"))'
                   .format(col, P['ingresos'], Q_PEQ, E['ing_anio'])))
    C.nota(ws, 'G%d' % P['r_equilibrio'],
           'Compara las ventas de CADA año con el umbral contable de ese mismo '
           'año, que calcula la hoja «Punto de Equilibrio». El umbral de caja, '
           'que es el que de verdad te deja dormir, está allí.')

    # --- escenario de formato (D1) ----------------------------------------
    sec(P['sec_formato'], 'ESCENARIO DE FORMATO: BOMBONERÍA FRENTE A '
                          'BOMBONERÍA CON TAZA Y CHURROS (año de crucero)')
    C.cabecera(ws, P['cab_formato'],
               [('A', 'Concepto (año 2)'), ('B', 'Bombonería'),
                ('C', 'Bombonería + taza y churros'), ('D', ''), ('E', ''),
                ('F', ''), ('G', 'Notas')], altura=30)

    def fent(clave, etiqueta, valor, fmt, nota_txt, id_chs=None):
        fila = P[clave]
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
        C.entrada(ws, 'C%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
        C.nota(ws, 'G%d' % fila, nota_txt)
        if id_chs:
            C.nota_fuente(ws, 'C%d' % fila, id_chs)

    fent('f_clientes', 'Clientes al día que añade el servicio de taza y '
                       'churros', 35, C.ENT,
         'SUPUESTO. Es OTRO negocio, con otro horario y otro público: no son '
         'los mismos clientes comprando más, son clientes nuevos a otra hora.')
    fent('f_pvp_min', 'PVP con IVA de la ración con chocolate, mínimo '
                      'publicado (€)', 3.50, C.EUR,
         'Dato de mercado: el chocolate convierte una ración de churros de '
         '2,50 € en 3,50-4 €, entre un 40 y un 60 % más de ticket. Se publica '
         'el RANGO, y el libro usa el mínimo.', id_chs='CHS-32')
    fent('f_pvp_max', 'PVP con IVA de la ración con chocolate, máximo '
                      'publicado (€)', 4.00, C.EUR,
         'El techo del mismo rango. Si tu carta está por encima, dilo aquí y '
         'mira cómo se mueve la columna de la derecha.', id_chs='CHS-32')
    motor.val(ws, 'A%d' % P['f_pvp'],
              'PVP con IVA que usa el escenario (el mínimo: criterio '
              'conservador)', wrap=True)
    motor.f(ws, 'C%d' % P['f_pvp'], ie('C%d' % P['f_pvp_min']), fmt=C.EUR)
    C.nota(ws, 'G%d' % P['f_pvp'],
           'Se usa el mínimo del rango a propósito: un escenario que se '
           'defiende con el techo del rango no es un escenario, es un deseo.')
    fent('f_margen_pct', 'Margen bruto de la línea de taza y churros (%)',
         0.50, C.PCT,
         'SE PUBLICAN LAS DOS CIFRAS QUE HAY, no la más bonita: el margen '
         'bruto del churro se cita entre el 85 y el 90 %, y un maestro '
         'churrero lo rebaja a «un poco más del 50 %». El libro usa el 50 % '
         'porque es el que aguanta una discusión con el banco.',
         id_chs='CHS-31')
    fent('f_personal', 'Coste de personal adicional al año (€)',
         DEF_PERSONAL_TAZA, C.EUR,
         'SUPUESTO: media jornada más del grupo de convenio del Dependiente, '
         'con la Seguridad Social a cargo de la empresa dentro. La taza se '
         'sirve, y servir es mano de obra: sin esta línea el escenario sale '
         'redondo y es mentira.')
    fent('f_otros', 'Otros costes fijos adicionales al año (€)', 1200.0,
         C.EUR,
         'SUPUESTO: mantenimiento de freidora y extracción, y la inspección '
         'periódica de la instalación de gas cada cinco años, repercutida. Y '
         'una que no es un euro pero cuesta tiempo: la bombonería se libra de '
         'la licencia previa de actividad hasta 750 m2 y la chocolatería de '
         'taza NO, porque su grupo de IAE no está en el Anexo de esa ley.')
    C.nota_celda(ws, 'C%d' % P['f_otros'], 'CHN-48')

    def flinea(clave, etiqueta, expr_b, expr_c, fmt=C.EUR, bold=None,
               nota_txt=None):
        fila = P[clave]
        motor.val(ws, 'A%d' % fila, etiqueta, bold=bold, wrap=True)
        motor.f(ws, 'B%d' % fila, ie(expr_b), fmt=fmt, bold=bold)
        motor.f(ws, 'C%d' % fila, ie(expr_c), fmt=fmt, bold=bold)
        if nota_txt:
            C.nota(ws, 'G%d' % fila, nota_txt)

    flinea('f_ventas', 'Ventas del año sin IVA (€)',
           'C%d' % P['ingresos'],
           'B{0}+C{1}*C{2}/(1+{3})*C{4}'.format(
               P['f_ventas'], P['f_clientes'], P['f_pvp'], sup('iva_taza'),
               P['dias']),
           bold=True,
           nota_txt='La taza servida en sala va al 10 % por ser prestación de '
                    'servicio de hostelería, no entrega de un bien: por eso el '
                    'PVP se pasa a base imponible con ESE tipo.')
    C.nota_celda(ws, 'C%d' % P['f_ventas'], 'CHN-71c')
    flinea('f_var', 'Costes variables (€)',
           'C%d' % P['tot_var'],
           'B{0}+(C{1}-B{1})*(1-C{2})'.format(P['f_var'], P['f_ventas'],
                                              P['f_margen_pct']))
    flinea('f_mb', 'Margen bruto (€)',
           'B%d-B%d' % (P['f_ventas'], P['f_var']),
           'C%d-C%d' % (P['f_ventas'], P['f_var']))
    flinea('f_fijos', 'Costes fijos (€)',
           'C%d' % P['tot_fijos'],
           'B{0}+C{1}+C{2}'.format(P['f_fijos'], P['f_personal'],
                                   P['f_otros']))
    flinea('f_rai', 'Resultado antes de impuestos (€)',
           'B%d-B%d' % (P['f_mb'], P['f_fijos']),
           'C%d-C%d' % (P['f_mb'], P['f_fijos']), bold=True)
    flinea('f_neto', 'Resultado neto (€)',
           'B{0}-MAX(0,B{0})*{1}'.format(P['f_rai'], sup('is_nueva')),
           'C{0}-MAX(0,C{0})*{1}'.format(P['f_rai'], sup('is_nueva')),
           bold=True)
    C.total_fila(ws, P['f_neto'], 'ABC')
    flinea('f_mneto', 'Margen neto (%)',
           'B%d/B%d' % (P['f_neto'], P['f_ventas']),
           'C%d/C%d' % (P['f_neto'], P['f_ventas']), fmt=C.PCT)
    motor.val(ws, 'A%d' % P['f_veredicto'], 'VEREDICTO DEL FORMATO', bold=True)
    motor.f(ws, 'B%d' % P['f_veredicto'],
            ie('IF(OR(B{0}="",C{0}=""),"",IF(C{0}>B{0},"La taza y los churros '
               'suman: aporta más margen del que se come en fijos",'
               '"La taza y los churros restan: con estos supuestos te ocupan '
               'sala y personal para nada"))'.format(P['f_mneto'])),
            bold=True)
    C.destacado(ws, 'B%d' % P['f_veredicto'])
    C.nota(ws, 'G%d' % P['f_veredicto'],
           'Son DOS NEGOCIOS, y la norma los separa sola: el Anexo de la Ley '
           '12/2012 incluye el epígrafe 644.5 de bombones y caramelos y no '
           'contiene ningún grupo de la agrupación 67, donde está la '
           'chocolatería de taza. Antes de mirar el margen, mira eso: la '
           'bombonería se libra de la licencia previa de actividad hasta '
           '750 m2 y la taza no.')
    C.nota_celda(ws, 'B%d' % P['f_veredicto'], 'CHN-49')

    # --- cruce 7 <- 3: el precio de la cobertura --------------------------
    sec(P['sec_cob'],
        'DE DÓNDE SALE EL COSTE DE VENTAS: EL PRECIO DE LA COBERTURA (cruce 7 '
        + chr(60) + '- 3)')
    motor.val(ws, 'A%d' % P['cob_trae'],
              'Precio de la cobertura negra EN BASE IMPONIBLE: trae aquí la '
              'cifra de ' + ORIGEN_COB, wrap=True)
    C.entrada(ws, 'B%d' % P['cob_trae'], DEF_COBERTURA, fmt=C.EUR,
              etiqueta='Precio de la cobertura en base imponible')
    motor.val(ws, 'C%d' % P['cob_trae'], '€/kg')
    C.nota(ws, 'G%d' % P['cob_trae'],
           'CÓPIALA A MANO, y cópiala BIEN: es la celda más crítica de todo el '
           'pack. La fuente publica 25,02 €/kg CON EL IVA DENTRO, y un '
           'escandallo se calcula con precios SIN IVA porque el soportado es '
           'deducible. Con la base equivocada el food cost sale un 9 % alto y '
           'este P&L entero está mal. Por eso lo que se copia es la celda de '
           'BASE IMPONIBLE, nunca la de la fuente.')
    ws.row_dimensions[P['cob_trae']].height = 44
    motor.val(ws, 'A%d' % P['cob_orig'],
              'Cifra que publica hoy esa celda del libro 3')
    C.entrada(ws, 'B%d' % P['cob_orig'], DEF_COBERTURA, fmt=C.EUR,
              etiqueta='Precio de cobertura que publica el libro 3')
    C.nota(ws, 'G%d' % P['cob_orig'],
           'Anota aquí lo que ves en el libro '
           '«sensibilidad-al-precio-del-cacao» la última vez que lo abriste. '
           'Si arriba tecleas otra cosa -porque te han pasado tarifa nueva-, '
           'la fila de CUADRE te avisa.')
    motor.val(ws, 'A%d' % P['cob_desv'], 'Desviación entre las dos')
    motor.f(ws, 'B%d' % P['cob_desv'],
            ie('ABS(B%d-B%d)/B%d'
               % (P['cob_trae'], P['cob_orig'], P['cob_orig'])), fmt=C.PCT2)
    motor.val(ws, 'A%d' % P['cob_cuadre'],
              'CUADRE DE LA COBERTURA: el precio que usas frente al del '
              'libro 3', bold=True)
    motor.f(ws, 'B%d' % P['cob_cuadre'],
            ie('IF(NOT(ISNUMBER(B%d)),"",IF(B%d<=%s,"CUADRA","REVISA: el '
               'precio de cobertura que usas no es el del libro 3"))'
               % (P['cob_desv'], P['cob_desv'], sup('tolerancia'))), bold=True)
    C.destacado(ws, 'B%d' % P['cob_cuadre'])
    motor.semaforo_texto(ws, 'B%d' % P['cob_cuadre'],
                         (('REVISA: el precio de cobertura que usas no es el '
                           'del libro 3', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('CUADRA', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    motor.val(ws, 'A%d' % P['cob_kg'],
              'Kilos de cobertura negra que se van al año')
    C.entrada(ws, 'B%d' % P['cob_kg'], DEF_KG_COBERTURA, fmt=C.DEC1,
              etiqueta='Kilos de cobertura negra al año')
    motor.val(ws, 'C%d' % P['cob_kg'], 'kg/año')
    C.nota(ws, 'G%d' % P['cob_kg'],
           'También del libro 3, que los calcula referencia a referencia. Es '
           'la cobertura MÁS USADA de la carta, no toda la que compras.')
    motor.val(ws, 'A%d' % P['cob_coste'],
              'Coste anual de esa cobertura (€)')
    motor.f(ws, 'B%d' % P['cob_coste'],
            ie('B%d*B%d' % (P['cob_trae'], P['cob_kg'])), fmt=C.EUR)
    motor.val(ws, 'A%d' % P['cob_peso'],
              'Peso sobre el coste de ventas del año de crucero (%)')
    motor.f(ws, 'B%d' % P['cob_peso'],
            ie('IF(C%d="","",B%d/C%d)'
               % (P['coste_ventas'], P['cob_coste'], P['coste_ventas'])),
            fmt=C.PCT)
    motor.val(ws, 'A%d' % P['cob_subida'],
              'Subida del precio del cacao que quieres simular (%)')
    C.entrada(ws, 'B%d' % P['cob_subida'], 0.40, fmt=C.PCT,
              etiqueta='Subida del cacao a simular')
    C.nota(ws, 'G%d' % P['cob_subida'],
           'El 40 % no es un número de miedo: es uno de los escenarios que '
           'trabaja el libro «sensibilidad-al-precio-del-cacao», y allí está '
           'referencia a referencia. Aquí sólo se mira lo que le hace a la '
           'cuenta de resultados entera.')
    motor.val(ws, 'A%d' % P['cob_impacto'],
              'Lo que te costaría esa subida al año (€)')
    motor.f(ws, 'B%d' % P['cob_impacto'],
            ie('B%d*B%d' % (P['cob_coste'], P['cob_subida'])), fmt=C.EUR,
            bold=True)
    motor.val(ws, 'A%d' % P['cob_neto'],
              'Margen neto del año de crucero DESPUÉS de esa subida (%)',
              bold=True)
    motor.f(ws, 'B%d' % P['cob_neto'],
            ie('IF(C{0}="","",(C{1}-B{2})/C{0})'
               .format(P['ingresos'], P['neto'], P['cob_impacto'])),
            fmt=C.PCT, bold=True)
    C.total_fila(ws, P['cob_neto'], 'AB')
    motor.semaforo_isnumber(ws, 'B%d:B%d' % (P['cob_neto'], P['cob_neto']),
                            '$B$%d' % P['cob_neto'], operador='<',
                            umbral=sup('neto_suelo'))
    C.nota(ws, 'G%d' % P['cob_neto'],
           'Es la pregunta que hay que saber responder antes de firmar un '
           'alquiler: si el cacao sube lo que ya ha subido otras veces, ¿el '
           'negocio sigue en pie? Si esta celda se pone en rojo, tu plan '
           'depende del precio del cacao más de lo que crees, y la respuesta '
           'no es esperar: es gramaje, mix o precio.')

    C.parrafo(ws, P['nota'],
              'Todas las cifras van SIN IVA. Las columnas de los años 2 y 3 '
              'están en euros del año 1 mientras la «Subida anual de los '
              'costes fijos» de «0. Supuestos» valga cero. Y una advertencia '
              'que vale dinero: si tu proyección del año 1 sale en positivo, '
              'míralo dos veces. Casi ninguna apertura gana dinero el primer '
              'año, y lo que decide si sobrevives no es este cuadro sino la '
              'hoja de Tesorería.', 'A', 'G', alto=46)
    ws.freeze_panes = 'A%d' % (P['cab'] + 1)
    C.pagina(ws, titulos='$%d:$%d' % (P['cab'], P['cab']),
             area='A1:G%d' % P['nota'])
    return ws


# ==========================================================================
# Hoja «Punto de Equilibrio»
# ==========================================================================
def hoja_equilibrio(wb):
    ws = wb.create_sheet(H_PEQ)
    C.anchos(ws, {'A': 56, 'B': 15, 'C': 15, 'D': 15, 'E': 82})
    C.encabezar(ws, 'Punto de equilibrio: cuántos clientes al día',
                'Dos umbrales, y no dicen lo mismo. El CONTABLE incluye la '
                'amortización; el de CAJA le quita la amortización (que no se '
                'paga) y le suma la devolución de principal (que sí). El '
                'segundo es el que decide si llegas a fin de mes.', col_fin='E')
    C.cabecera(ws, E['cab'], [('A', 'Variable'), ('B', 'Año 1'),
                              ('C', 'Año 2'), ('D', 'Año 3'), ('E', 'Notas')])

    def sec(fila, texto):
        C.banda(ws, fila, 'ABCDE', texto)

    def linea(fila, etiqueta, plantilla, fmt, nota_txt=None, bold=None):
        motor.val(ws, 'A%d' % fila, etiqueta, bold=bold)
        for col in 'BCD':
            motor.f(ws, '%s%d' % (col, fila), plantilla(col), fmt=fmt,
                    bold=bold)
        if nota_txt:
            C.nota(ws, 'E%d' % fila, nota_txt)

    def g(col, expr):
        return ie('IF({0}{1}{2}="","",{3})'.format(Q_PYG, col, P['ingresos'],
                                                   expr))

    sec(E['sec_base'], 'DATOS BASE POR AÑO')
    linea(E['fijos_anio'], 'Costes fijos anuales',
          lambda c: g(c, '%s%s%d' % (Q_PYG, c, P['tot_fijos'])), C.EUR,
          'Los MISMOS costes fijos del P&L. Cada año tiene los suyos: por eso '
          'el umbral no puede ser uno solo para los tres.')
    linea(E['fijos_mes'], 'Costes fijos mensuales',
          lambda c: g(c, '%s%d/12' % (c, E['fijos_anio'])), C.EUR)
    linea(E['ticket'], 'Ticket medio sin IVA (€)',
          lambda c: g(c, '%s%s%d' % (Q_PYG, c, P['ticket'])), C.EUR)
    linea(E['cv_ticket'], 'Coste variable por ticket (€)',
          lambda c: g(c, '{0}{1}{2}/({0}{1}{3}*{0}{1}{4}*{0}{1}{5})'
                      .format(Q_PYG, c, P['tot_var'], P['tickets'],
                              P['dias'], P['actividad'])), C.EUR,
          'Sale del total de costes variables del P&L dividido por los '
          'clientes de ese año, no de una estimación aparte.')
    linea(E['mc_ticket'], 'Margen de contribución por ticket (€)',
          lambda c: g(c, '%s%d-%s%d' % (c, E['ticket'], c, E['cv_ticket'])),
          C.EUR,
          'Ticket menos coste variable unitario. Es lo que deja cada cliente '
          'para pagar los fijos. En bombonería es alto y los fijos también: '
          'las dos cosas van juntas.')
    linea(E['dias'], 'Días de apertura al año',
          lambda c: g(c, '%s%s%d' % (Q_PYG, c, P['dias'])), C.ENT)
    motor.val(ws, 'A%d' % E['principal'],
              'Devolución de principal del año (sale de caja)')
    for col, anio in (('B', 0), ('C', 1), ('D', 2)):
        motor.f(ws, '%s%d' % (col, E['principal']),
                g(col, '%s$C$%d' % (Q_FIN, F_ANIO_INI + anio)), fmt=C.EUR)
    C.nota(ws, 'E%d' % E['principal'],
           'El principal NO es gasto del P&L, pero sale de la caja. Sin él, el '
           'umbral de equilibrio se publica por debajo de lo que de verdad hay '
           'que facturar.')

    sec(E['sec_cont'],
        'PUNTO DE EQUILIBRIO CONTABLE (incluye la amortización)')
    linea(E['tk_anio'], 'Clientes necesarios al año',
          lambda c: g(c, 'IF({0}{1}<=0,"",{0}{2}/{0}{1})'
                      .format(c, E['mc_ticket'], E['fijos_anio'])), C.ENT)
    linea(E['tk_dia'], 'Clientes necesarios al día',
          lambda c: g(c, '%s%d/%s%d' % (c, E['tk_anio'], c, E['dias'])),
          C.DEC1)
    linea(E['ing_anio'], 'Ingresos necesarios al año (sin IVA)',
          lambda c: g(c, '%s%d*%s%d' % (c, E['tk_anio'], c, E['ticket'])),
          C.EUR, bold=True)
    linea(E['ing_mes'], 'Ingresos necesarios al mes (sin IVA)',
          lambda c: g(c, '%s%d/12' % (c, E['ing_anio'])), C.EUR, bold=True)
    C.total_fila(ws, E['ing_anio'], 'ABCDE')
    C.total_fila(ws, E['ing_mes'], 'ABCDE')

    sec(E['sec_caja'],
        'PUNTO DE EQUILIBRIO DE CAJA (incluye la cuota del préstamo)')
    linea(E['fijos_caja'], 'Costes fijos de caja más el principal del año',
          lambda c: g(c, '{0}{1}-{2}{0}{3}+{0}{4}'
                      .format(c, E['fijos_anio'], Q_PYG, P['amortizacion'],
                              E['principal'])), C.EUR,
          'Los fijos del P&L sin la amortización (que no se paga) y CON la '
          'devolución de principal (que sí). Es el umbral que decide si '
          'sobrevives, no el contable.')
    linea(E['tkc_anio'], 'Clientes necesarios al año (caja)',
          lambda c: g(c, 'IF({0}{1}<=0,"",{0}{2}/{0}{1})'
                      .format(c, E['mc_ticket'], E['fijos_caja'])), C.ENT)
    linea(E['tkc_dia'], 'Clientes necesarios al día (caja)',
          lambda c: g(c, '%s%d/%s%d' % (c, E['tkc_anio'], c, E['dias'])),
          C.DEC1, bold=True)
    linea(E['ingc_anio'], 'Ingresos necesarios al año (caja, sin IVA)',
          lambda c: g(c, '%s%d*%s%d' % (c, E['tkc_anio'], c, E['ticket'])),
          C.EUR)
    C.total_fila(ws, E['tkc_dia'], 'ABCDE')

    sec(E['sec_contraste'], 'CONTRASTE CON EL PLAN')
    linea(E['tk_previstos'], 'Clientes al día previstos en el plan',
          lambda c: g(c, '{0}{1}{2}*{0}{1}{3}'
                      .format(Q_PYG, c, P['tickets'], P['actividad'])),
          C.DEC1)
    linea(E['holgura'], 'Holgura sobre el equilibrio de CAJA (%)',
          lambda c: g(c, 'IF({0}{1}<=0,"",{0}{2}/{0}{1}-1)'
                      .format(c, E['tkc_dia'], E['tk_previstos'])), C.PCT,
          'Cuánto puedes caer sobre lo previsto antes de no poder pagar los '
          'fijos y la cuota. El mínimo exigible está en «0. Supuestos».')
    linea(E['semaforo'], 'Lectura de la holgura',
          lambda c: g(c, 'IF({0}{1}<0,"Por debajo del equilibrio",'
                      'IF({0}{1}<{2},"Ajustada","Suficiente"))'
                      .format(c, E['holgura'], sup('holgura'))), None)
    motor.semaforo_isnumber(ws, 'B%d:D%d' % (E['holgura'], E['holgura']),
                            'B%d' % E['holgura'], operador='<', umbral='0')
    C.parrafo(ws, E['nota'],
              'Lectura rápida: si los clientes al día previstos están por '
              'debajo de los clientes al día de CAJA, el negocio no genera '
              'para pagar los fijos y la cuota, y da igual lo que diga el '
              'resultado contable. Si están justo por encima, no tienes margen '
              'para un mes malo -y aquí los meses malos están en el '
              'calendario, no en la mala suerte-: negocia carencia, baja '
              'inversión o revisa el ticket medio antes de firmar nada.',
              'A', 'E', alto=44)

    # --- punto muerto POR FORMATO (D1), en columnas contiguas -------------
    sec(E['sec_formato'], 'EL PUNTO MUERTO, POR FORMATO (año de crucero)')
    C.cabecera(ws, E['cab_formato'],
               [('A', 'Concepto'), ('B', 'Bombonería'),
                ('C', 'Bombonería + taza y churros'), ('D', ''),
                ('E', 'Notas')], altura=30)
    for clave, etiqueta, expr_b, expr_c, fmt in (
            ('pm_fijos', 'Costes fijos mensuales (€)',
             '{0}B{1}/12'.format(Q_PYG, P['f_fijos']),
             '{0}C{1}/12'.format(Q_PYG, P['f_fijos']), C.EUR),
            ('pm_mc', 'Margen de contribución sobre ventas (%)',
             '{0}B{1}/{0}B{2}'.format(Q_PYG, P['f_mb'], P['f_ventas']),
             '{0}C{1}/{0}C{2}'.format(Q_PYG, P['f_mb'], P['f_ventas']),
             C.PCT)):
        fila = E[clave]
        motor.val(ws, 'A%d' % fila, etiqueta)
        motor.f(ws, 'B%d' % fila, ie(expr_b), fmt=fmt)
        motor.f(ws, 'C%d' % fila, ie(expr_c), fmt=fmt)
    motor.val(ws, 'A%d' % E['pm_mes'], 'PUNTO MUERTO MENSUAL (€ sin IVA)',
              bold=True)
    for col in 'BC':
        motor.f(ws, '%s%d' % (col, E['pm_mes']),
                ie('IF({0}{1}<=0,"",{0}{2}/{0}{1})'
                   .format(col, E['pm_mc'], E['pm_fijos'])), fmt=C.EUR,
                bold=True)
    C.total_fila(ws, E['pm_mes'], 'ABC')
    motor.val(ws, 'A%d' % E['pm_dia'], 'Punto muerto por día de apertura (€)')
    for col in 'BC':
        motor.f(ws, '%s%d' % (col, E['pm_dia']),
                ie('{0}{1}*12/{2}'.format(col, E['pm_mes'], sup('dias'))),
                fmt=C.EUR)
    C.nota(ws, 'E%d' % E['pm_mes'],
           'El formato con taza y churros factura más, pero también arrastra '
           'más fijos y un margen bruto mucho peor en esa línea. Lo que decide '
           'no es cuál factura más: es cuál necesita menos para no perder '
           'dinero.')
    C.parrafo(ws, E['pm_nota'],
              'Los dos formatos comparten obrador, alquiler y titular; lo que '
              'cambia es la sala, el personal de servicio y la licencia. Si el '
              'punto muerto de la derecha sale MÁS ALTO, la taza y los churros '
              'te están obligando a facturar más para estar igual: puede '
              'seguir mereciendo la pena por tráfico y por horario, pero eso '
              'ya es una decisión tuya y no un resultado del libro.',
              'A', 'E', alto=44)

    # --- sensibilidad ------------------------------------------------------
    sec(E['sec_sens'],
        'SENSIBILIDAD DEL PUNTO DE EQUILIBRIO (año de crucero)')
    motor.val(ws, 'A%d' % E['sens_cab'],
              'Clientes al día necesarios: ticket medio (columnas) x coste '
              'variable por ticket (filas)', wrap=True)
    ws.row_dimensions[E['sens_cab']].height = 30
    for i, col in enumerate(('B', 'C', 'D', 'E')):
        desp = i - 1
        if desp == 0:
            expr = '$C$%d' % E['ticket']
        elif desp < 0:
            expr = '$C$%d-1' % E['ticket']
        else:
            expr = '$C$%d+%d' % (E['ticket'], desp)
        motor.f(ws, '%s%d' % (col, E['sens_cab']), ie(expr), fmt=C.EUR,
                bold=True)
    for j in range(5):
        fila = E['sens_ini'] + j
        desp = j - 2
        if desp == 0:
            expr = '$C$%d' % E['cv_ticket']
        elif desp < 0:
            expr = '$C$%d-%d*%s' % (E['cv_ticket'], -desp, sup('paso_sens'))
        else:
            expr = '$C$%d+%d*%s' % (E['cv_ticket'], desp, sup('paso_sens'))
        motor.f(ws, 'A%d' % fila, ie(expr), fmt=C.EUR, bold=True)
        for col in ('B', 'C', 'D', 'E'):
            motor.f(ws, '%s%d' % (col, fila),
                    ie('IF({0}${1}-$A{2}<=0,"",$C${3}/({0}${1}-$A{2})/$C${4})'
                       .format(col, E['sens_cab'], fila, E['fijos_anio'],
                               E['dias'])), fmt=C.DEC1)
    C.parrafo(ws, E['sens_nota'],
              'La celda del centro es tu escenario. Muévete una columna a la '
              'izquierda y estarás viendo qué pasa si tienes que bajar el '
              'ticket medio un euro; una fila hacia abajo, qué pasa si el '
              'cacao te sube el coste variable. Los dos movimientos han pasado '
              'en los últimos tres años, y el segundo tiene su propio libro en '
              'esta guía.', 'A', 'E', alto=42)
    C.pagina(ws, titulos='$%d:$%d' % (E['cab'], E['cab']),
             area='A1:E%d' % E['sens_nota'])
    return ws


# ==========================================================================
# Hoja «Escenarios»
# ==========================================================================
def hoja_escenarios(wb):
    ws = wb.create_sheet(H_ESC)
    C.anchos(ws, {'A': 54, 'B': 16, 'C': 16, 'D': 16, 'E': 82})
    C.encabezar(ws, 'Escenarios: pesimista, realista y optimista',
                'La columna «Realista» LEE el año de crucero del P&L, así que '
                'no puede desviarse de él. Las otras dos son verdes: son tus '
                'apuestas, y la de la izquierda es la que hay que poder '
                'sobrevivir.', col_fin='E')
    C.cabecera(ws, X['cab'], [('A', 'Métrica'), ('B', 'Pesimista'),
                              ('C', 'Realista'), ('D', 'Optimista'),
                              ('E', 'Notas')])

    ENTRADAS = (
        (X['tickets'], 'Clientes al día', 48, 85, C.ENT, P['tickets'],
         'SUPUESTOS los dos extremos. El pesimista no es «un mal día»: es el '
         'año entero yendo mal, con una Navidad floja dentro.'),
        (X['ticket'], 'Ticket medio sin IVA (€)', 8.20, 11.50, C.EUR,
         P['ticket'],
         'SUPUESTOS. En bombonería el ticket lo mueve el MIX, no el precio: si '
         'la gente compra cajas de 12 en vez de cajas de 35, el ticket cae sin '
         'que hayas bajado un solo precio.'),
        (X['dias'], 'Días de apertura al año', 290, 310, C.ENT, P['dias'],
         'SUPUESTOS. Ojo con creer que abrir más días arregla un año malo: lo '
         'que arregla un año malo es Navidad.'))
    for fila, etiqueta, pes, opt, fmt, fila_pyg, nota_txt in ENTRADAS:
        motor.val(ws, 'A%d' % fila, etiqueta)
        C.entrada(ws, 'B%d' % fila, pes, fmt=fmt, etiqueta=etiqueta + ' (pes.)')
        motor.f(ws, 'C%d' % fila, ie('%sC%d' % (Q_PYG, fila_pyg)), fmt=fmt)
        C.entrada(ws, 'D%d' % fila, opt, fmt=fmt, etiqueta=etiqueta + ' (opt.)')
        C.nota(ws, 'E%d' % fila, nota_txt)

    def linea(fila, etiqueta, plantilla, fmt, nota_txt=None, bold=None):
        motor.val(ws, 'A%d' % fila, etiqueta, bold=bold)
        for col in 'BCD':
            motor.f(ws, '%s%d' % (col, fila), plantilla(col), fmt=fmt,
                    bold=bold)
        if nota_txt:
            C.nota(ws, 'E%d' % fila, nota_txt)

    def g(col, expr):
        return ie('IF({0}{1}="","",{2})'.format(col, X['ingresos'], expr))

    linea(X['ingresos'], 'INGRESOS ANUALES (sin IVA)',
          lambda c: ie('IF({0}{1}*{0}{2}*{0}{3}=0,"",{0}{1}*{0}{2}*{0}{3})'
                       .format(c, X['tickets'], X['ticket'], X['dias'])),
          C.EUR, bold=True)
    C.total_fila(ws, X['ingresos'], 'ABCDE')
    linea(X['coste'], 'Coste de ventas (food cost del P&L)',
          lambda c: g(c, '%s%d*%s' % (c, X['ingresos'], sup('food_cost'))),
          C.EUR)
    linea(X['tot_var'], 'TOTAL COSTES VARIABLES',
          lambda c: g(c, '{0}{1}'.format(c, X['coste'])), C.EUR)
    linea(X['margen'], 'MARGEN BRUTO',
          lambda c: g(c, '%s%d-%s%d' % (c, X['ingresos'], c, X['tot_var'])),
          C.EUR, bold=True)
    linea(X['fijos'], 'COSTES FIJOS (los del año de crucero del P&L)',
          lambda c: g(c, '%s$C$%d' % (Q_PYG, P['tot_fijos'])), C.EUR,
          'Los costes fijos no cambian con el escenario: por eso son fijos. Si '
          'en el pesimista se disparan sobre las ventas, el ajuste hay que '
          'hacerlo en la hoja de Personal, no aquí.')
    linea(X['rai'], 'RESULTADO ANTES DE IMPUESTOS',
          lambda c: g(c, '%s%d-%s%d' % (c, X['margen'], c, X['fijos'])),
          C.EUR, bold=True)
    linea(X['is'], 'Impuesto de Sociedades',
          lambda c: g(c, 'MAX(0,%s%d-%s)*%s'
                      % (c, X['rai'], sup('bases_neg'), sup('is_nueva'))),
          C.EUR,
          'Al tipo de entidad de nueva creación, compensando las bases '
          'negativas anteriores. Con resultado negativo no hay cuota.')
    linea(X['neto'], 'RESULTADO NETO',
          lambda c: g(c, '%s%d-%s%d' % (c, X['rai'], c, X['is'])), C.EUR,
          bold=True)
    C.total_fila(ws, X['neto'], 'ABCDE')
    motor.semaforo_isnumber(ws, 'B%d:D%d' % (X['neto'], X['neto']),
                            'B%d' % X['neto'], operador='<', umbral='0')
    linea(X['margen_neto'], 'Margen neto (%)',
          lambda c: g(c, '%s%d/%s%d' % (c, X['neto'], c, X['ingresos'])),
          C.PCT,
          'Contrástalo con la banda de referencia de «0. Supuestos», que es un '
          'supuesto de control y no un dato del sector. El optimista que se va '
          'muy por encima suele estar olvidándose de un coste, no '
          'descubriendo un negocio mejor.')
    linea(X['tk_equilibrio'], 'Clientes al día para el equilibrio',
          lambda c: g(c, 'IF({0}{1}-{0}{2}/({0}{3}*{0}{4})<=0,"",'
                      '{0}{5}/({0}{1}-{0}{2}/({0}{3}*{0}{4}))/{0}{4})'
                      .format(c, X['ticket'], X['tot_var'], X['tickets'],
                              X['dias'], X['fijos'])), C.DEC1)

    C.banda(ws, X['sec_exige'], 'ABCDE', 'LO QUE CADA ESCENARIO EXIGE')
    linea(X['personal_ventas'], 'Coste de personal / ventas',
          lambda c: g(c, '%s$C$%d/%s%d' % (Q_PYG, P['personal'], c,
                                           X['ingresos'])), C.PCT,
          'La MISMA plantilla en los tres escenarios: tres personas y dos '
          'jornadas y media. En el pesimista es donde se ve si esa plantilla '
          'se sostiene.')
    linea(X['ventas_jornada'], 'Ventas al año por jornada equivalente (€)',
          lambda c: g(c, '%s%d/%s$C$%d' % (c, X['ingresos'], Q_PER, R_TOT)),
          C.EUR,
          'Cuánto tendría que facturar cada jornada completa del cuadro de '
          'Personal. En el optimista dice si hace falta contratar antes de '
          'llegar ahí -y en bombonería contratar en noviembre ya es tarde-.')
    linea(X['saldo_est'],
          'Saldo de caja estimado al cierre del año 1 (mismo método en los '
          'tres)',
          lambda c: g(c, '{0}$B${1}+{2}{3}+{4}$C${5}-{6}$C${7}'
                      .format(Q_INV, IV['fondo'], c, X['neto'], Q_PYG,
                              P['amortizacion'], Q_FIN, F_ANIO_INI)), C.EUR,
          'Fondo de maniobra más el resultado del año, devolviendo la '
          'amortización (que no se paga) y restando el principal (que sí). Es '
          'una ESTIMACIÓN: el saldo de verdad, con su desfase de cobros y su '
          'liquidación de IVA, está en la hoja de Tesorería.')
    motor.val(ws, 'A%d' % X['saldo_real'],
              'Saldo real del mes 12 de la hoja de Tesorería (sólo el '
              'realista)')
    motor.f(ws, 'C%d' % X['saldo_real'],
            ie('IF(C%d="","",%sM%d)' % (X['ingresos'], Q_TES, T['saldo'])),
            fmt=C.EUR)
    C.nota(ws, 'E%d' % X['saldo_real'],
           'Sólo existe para el caso base: la tesorería mes a mes está '
           'construida sobre el año 1 del P&L, no sobre los escenarios.')
    C.parrafo(ws, X['nota'],
              'La columna «Realista» lee sus tres datos del año de crucero del '
              'P&L, así que reproduce EXACTAMENTE ese año. Si quieres mover el '
              'caso base, muévelo en «0. Supuestos» y esta columna te sigue.',
              'A', 'E', alto=30)
    ws.freeze_panes = 'A%d' % (X['cab'] + 1)
    C.pagina(ws, titulos='$%d:$%d' % (X['cab'], X['cab']),
             area='A1:E%d' % X['nota'])
    return ws


# ==========================================================================
# Hoja «Personal»
# ==========================================================================
def hoja_personal(wb):
    ws = wb.create_sheet(H_PER)
    C.anchos(ws, {'A': 34, 'B': 10, 'C': 10, 'D': 12, 'E': 14, 'F': 14,
                  'G': 14, 'H': 14, 'I': 15, 'J': 11, 'K': 13, 'L': 62})
    C.encabezar(ws, 'Personal: tres personas y dos jornadas y media',
                'Los tres perfiles son los del kit de tareas de chocolatería, '
                'con sus nombres: Encargado, Chocolatero y Dependiente. El '
                'bruto sale del convenio, en celda verde, y la Seguridad '
                'Social a cargo de la empresa va DENTRO: del bruto al coste '
                'empresa hay un tercio más.', col_fin='L')
    C.cabecera(ws, R_CAB,
               [('A', 'Persona y perfil'), ('B', 'Personas'), ('C', 'Jornada'),
                ('D', 'Grupo de convenio'), ('E', 'Bruto mes del grupo (€)'),
                ('F', 'Bruto mes del puesto (€)'),
                ('G', 'Seguridad Social a cargo de la empresa (€)'),
                ('H', 'Coste mes (€)'), ('I', 'Coste año (€)'),
                ('J', 'Horas/semana'), ('K', 'Área'), ('L', 'Notas')])

    for i, (pid, perfil, jornada, grupo, area, horas, turno) in \
            enumerate(D.PLANTILLA):
        fila = R_INI + i
        etiqueta = pid + ' · ' + perfil
        motor.val(ws, 'A%d' % fila, etiqueta)
        C.entrada(ws, 'B%d' % fila, 1, fmt=C.ENT, etiqueta=etiqueta,
                  align='center')
        C.entrada(ws, 'C%d' % fila, jornada, fmt=C.DEC1, etiqueta=etiqueta,
                  align='center')
        C.entrada(ws, 'D%d' % fila, 'Grupo %d' % grupo, etiqueta=etiqueta,
                  align='center')
        motor.f(ws, 'E%d' % fila,
                ie('INDEX($E$%d:$E$%d,MATCH(D%d,$A$%d:$A$%d,0))'
                   % (R_CONV_INI, R_CONV_FIN, fila, R_CONV_INI, R_CONV_FIN)),
                fmt=C.EUR)
        motor.f(ws, 'F%d' % fila, ie('E%d*C%d*B%d' % (fila, fila, fila)),
                fmt=C.EUR)
        motor.f(ws, 'G%d' % fila, ie('F%d*%s' % (fila, sup('ss'))), fmt=C.EUR)
        motor.f(ws, 'H%d' % fila, ie('F%d+G%d' % (fila, fila)), fmt=C.EUR)
        motor.f(ws, 'I%d' % fila, ie('H%d*MAX(12,%s)' % (fila, sup('pagas'))),
                fmt=C.EUR)
        C.entrada(ws, 'J%d' % fila, horas, fmt=C.ENT, etiqueta=etiqueta,
                  align='center')
        C.entrada(ws, 'K%d' % fila, area, etiqueta=etiqueta, align='center')
        C.nota(ws, 'L%d' % fila, 'Turno de %s.' % turno)

    motor.val(ws, 'A%d' % R_TOT, 'TOTAL PLANTILLA', bold=True)
    for letra in ('B', 'C', 'F', 'G', 'H', 'I', 'J'):
        fmt = C.EUR if letra in 'FGHI' else (C.DEC1 if letra == 'C'
                                             else C.ENT)
        motor.f(ws, '%s%d' % (letra, R_TOT),
                ie('IF(COUNT(E%d:E%d)=0,"",SUM(%s%d:%s%d))'
                   % (R_INI, R_FIN, letra, R_INI, letra, R_FIN)), fmt=fmt,
                bold=True)
    C.total_fila(ws, R_TOT, 'ABCDEFGHIJKL')
    C.nota(ws, 'L%d' % R_TOT,
           'Este «Coste año» es el que lee el P&L. No hay una segunda '
           'estimación de personal en ninguna parte del libro. Y dentro va la '
           'retribución del titular, que en este caso es el Encargado: lo '
           'único que va aparte, en los fijos, es su cuota de autónomos.')

    # --- el convenio -------------------------------------------------------
    C.seccion(ws, 'A%d' % R_SEC_CONV,
              'EL CONVENIO DE REFERENCIA (sustitúyelo por el tuyo)')
    C.cabecera(ws, R_CONV_CAB,
               [('A', 'Grupo'), ('B', 'Denominación del grupo'),
                ('E', 'Bruto mes (€)'), ('F', 'Bruto año (€)'),
                ('G', 'Áreas funcionales'), ('I', 'Puestos que cita')],
               altura=26)
    ws.merge_cells('B%d:D%d' % (R_CONV_CAB, R_CONV_CAB))
    ws.merge_cells('G%d:H%d' % (R_CONV_CAB, R_CONV_CAB))
    ws.merge_cells('I%d:L%d' % (R_CONV_CAB, R_CONV_CAB))
    for i, (n, nombre, mes, anio, areas, puestos) in enumerate(D.CONVENIO):
        fila = R_CONV_INI + i
        motor.val(ws, 'A%d' % fila, 'Grupo %d' % n)
        ws.merge_cells('B%d:D%d' % (fila, fila))
        motor.val(ws, 'B%d' % fila, nombre, wrap=True)
        C.entrada(ws, 'E%d' % fila, mes, fmt=C.EUR,
                  etiqueta='Bruto mes del grupo %d' % n)
        motor.f(ws, 'F%d' % fila, ie('E%d*MAX(12,%s)' % (fila, sup('pagas'))),
                fmt=C.EUR)
        ws.merge_cells('G%d:H%d' % (fila, fila))
        motor.val(ws, 'G%d' % fila, ' / '.join(areas), wrap=True)
        ws.merge_cells('I%d:L%d' % (fila, fila))
        motor.val(ws, 'I%d' % fila, puestos or '-', wrap=True)
        ws.row_dimensions[fila].height = 26
    C.nota_celda(ws, 'E%d' % R_CONV_INI, 'CHN-65b',
                 'TABLA DE EJEMPLO: convenio ' + D.CONVENIO_CODIGO
                 + ', «' + D.CONVENIO_DENOMINACION + '» ('
                 + D.CONVENIO_AUTORIDAD + '), vigencia ' + D.CONVENIO_VIGENCIA
                 + ', tablas de 2026 a ' + str(D.CONVENIO_PAGAS)
                 + ' pagas. CADUCAN el 31-12-2026.')
    C.nota_celda(ws, 'A%d' % R_SEC_CONV, 'CHN-65c',
                 'El código y la denominación son los LITERALES del registro '
                 'oficial. Ojo: «BOLLERÍAS» no aparece en esa denominación, '
                 'así que quien busque por ese nombre no encuentra el '
                 'convenio.')
    C.dv_rango(ws, ['D%d' % (R_INI + i) for i in range(len(D.PLANTILLA))],
               "'%s'!$A$%d:$A$%d" % (H_PER, R_CONV_INI, R_CONV_FIN),
               'Elige un grupo del convenio',
               'Escribe uno de los grupos de la tabla del convenio de abajo.')

    # --- contraste con el SMI ---------------------------------------------
    C.seccion(ws, 'A%d' % R_SEC_SMI, 'CONTRASTE CON EL SMI')
    motor.val(ws, 'A%d' % R_SUELO, 'Bruto anual del grupo más bajo (€)')
    motor.f(ws, 'B%d' % R_SUELO,
            ie('IF(COUNT(F%d:F%d)=0,"",MIN(F%d:F%d))'
               % (R_CONV_INI, R_CONV_FIN, R_CONV_INI, R_CONV_FIN)), fmt=C.EUR)
    motor.val(ws, 'A%d' % R_SMI, 'SMI anual de referencia (€)')
    motor.f(ws, 'B%d' % R_SMI, ie(sup('smi')), fmt=C.EUR)
    C.nota_celda(ws, 'B%d' % R_SMI, 'CHN-67')
    motor.val(ws, 'A%d' % R_VEREDICTO,
              '¿Algún grupo queda por debajo del SMI?')
    motor.f(ws, 'B%d' % R_VEREDICTO,
            ie('IF(B%d="","",IF(B%d<B%d,"Sí: revísalo con tu asesor",'
               '"No: aquí manda el convenio"))'
               % (R_SUELO, R_SUELO, R_SMI)))
    C.nota(ws, 'L%d' % R_VEREDICTO,
           'El SMI es una referencia ANUAL en cómputo global, no un mínimo por '
           'concepto. En este sector manda el convenio: el grupo más bajo de '
           'la tabla de ejemplo ya lo supera. Las dos cosas caducan el '
           '31-12-2026.')

    # --- salarios de mercado ----------------------------------------------
    C.seccion(ws, 'A%d' % R_SEC_MERC,
              'SALARIOS DE MERCADO (orientativos, y NUNCA un convenio)')
    C.cabecera(ws, R_MERC_CAB,
               [('A', 'Etiqueta de la fuente salarial'), ('B', 'Mín. (€/h)'),
                ('C', 'Máx. (€/h)'), ('D', 'Equivale a'),
                ('E', 'Coste año a jornada completa (€)'),
                ('L', 'Notas')], altura=30)
    for i, (etiq, mini, maxi, equiv, idc) in enumerate(D.SALARIOS_MERCADO):
        fila = R_MERC_INI + i
        motor.val(ws, 'A%d' % fila, etiq, wrap=True)
        C.entrada(ws, 'B%d' % fila, mini, fmt=C.EUR,
                  etiqueta=etiq + ' (mín.)')
        C.entrada(ws, 'C%d' % fila, maxi, fmt=C.EUR,
                  etiqueta=etiq + ' (máx.)')
        motor.val(ws, 'D%d' % fila, equiv)
        motor.f(ws, 'E%d' % fila,
                ie('B%d*$B$%d*(1+%s)' % (fila, R_HORAS_ANIO, sup('ss'))),
                fmt=C.EUR)
        C.nota_fuente(ws, 'B%d' % fila, idc)
    C.nota(ws, 'L%d' % R_MERC_INI,
           'Fiabilidad media, y NUNCA se presentan como tabla de convenio. Las '
           'etiquetas entrecomilladas son las de la FUENTE salarial, no los '
           'perfiles de esta casa: los perfiles son los tres del kit, y la '
           'columna «Equivale a» está para eso. Sirven para saber si lo que '
           'vas a ofrecer está dentro de mercado; lo que te OBLIGA es tu '
           'convenio.')

    # --- los convenios que sí nombran el chocolate ------------------------
    C.seccion(ws, 'A%d' % R_SEC_CONVCH,
              'LOS CUATRO CONVENIOS DE ÁMBITO PROVINCIAL O SUPERIOR QUE SÍ '
              'NOMBRAN CHOCOLATES O BOMBONES')
    C.cabecera(ws, R_CONVCH_CAB,
               [('A', 'Código'), ('B', 'Ámbito'), ('E', 'Denominación'),
                ('L', 'Notas')], altura=22)
    ws.merge_cells('B%d:D%d' % (R_CONVCH_CAB, R_CONVCH_CAB))
    ws.merge_cells('E%d:K%d' % (R_CONVCH_CAB, R_CONVCH_CAB))
    for i, (codigo, ambito, denom, idl) in enumerate(
            D.CONVENIOS_QUE_NOMBRAN_CHOCOLATE):
        fila = R_CONVCH_INI + i
        motor.val(ws, 'A%d' % fila, codigo)
        ws.merge_cells('B%d:D%d' % (fila, fila))
        motor.val(ws, 'B%d' % fila, ambito)
        ws.merge_cells('E%d:K%d' % (fila, fila))
        motor.val(ws, 'E%d' % fila, denom or '-', wrap=True)
    C.nota_celda(ws, 'A%d' % R_CONVCH_INI, 'CHN-93')
    C.nota(ws, 'L%d' % R_CONVCH_INI,
           'ESTÁ PROBADO que NO existe convenio ESTATAL del chocolate: el '
           'registro oficial devuelve «no se ha encontrado ningún acuerdo» '
           'para chocolate, bombones, confitería y pastelería, y el control '
           'con «turrones» devuelve 29 trámites, así que la consulta funciona. '
           'Estos cuatro existen y nombran el producto, pero su ámbito '
           'FUNCIONAL es una pregunta para un laboralista, no una respuesta de '
           'esta guía.')
    C.nota_celda(ws, 'B%d' % R_CONVCH_INI, 'CHN-66')

    # --- horas y dimensionado ---------------------------------------------
    C.seccion(ws, 'A%d' % R_SEC_HORAS, 'HORAS, DIMENSIONADO Y COSTE HORA')
    motor.val(ws, 'A%d' % R_HORAS, 'Horas contratadas a la semana')
    motor.f(ws, 'B%d' % R_HORAS, ie('J%d' % R_TOT), fmt=C.ENT)
    motor.val(ws, 'A%d' % R_JORNADAS, 'Jornadas completas equivalentes')
    motor.f(ws, 'B%d' % R_JORNADAS, ie('C%d' % R_TOT), fmt=C.DEC1)
    motor.val(ws, 'A%d' % R_AVISOS,
              'Personas con más horas de las que da su jornada')
    motor.f(ws, 'B%d' % R_AVISOS,
            ie('SUMPRODUCT((J%d:J%d>C%d:C%d*%s)*1)'
               % (R_INI, R_FIN, R_INI, R_FIN, sup('horas_sem'))), fmt=C.ENT)
    motor.semaforo_isnumber(ws, 'B%d:B%d' % (R_AVISOS, R_AVISOS),
                            '$B$%d' % R_AVISOS, operador='>', umbral='0')
    C.nota(ws, 'L%d' % R_AVISOS,
           'Tiene que valer cero. Si se pone en rojo, alguien está contratado '
           'a media jornada y trabajando más horas de las que cobra: eso no es '
           'un ahorro, es una inspección.')
    motor.val(ws, 'A%d' % R_HORAS_ANIO, 'Horas anuales de contrato')
    C.entrada(ws, 'B%d' % R_HORAS_ANIO, D.P('horas_anuales_contrato'),
              fmt=C.ENT, etiqueta='Horas anuales de contrato')
    C.nota(ws, 'L%d' % R_HORAS_ANIO,
           'SUPUESTO: 40 h x 52 semanas = 2.080, menos 30 días naturales de '
           'vacaciones y los festivos del calendario laboral.')
    motor.val(ws, 'A%d' % R_RATIO, 'Parte de la jornada a pie de mesa (%)')
    C.entrada(ws, 'B%d' % R_RATIO, D.P('ratio_horas_productivas'), fmt=C.PCT,
              etiqueta='Ratio de horas productivas')
    C.nota(ws, 'L%d' % R_RATIO,
           'SUPUESTO. El resto es recepción de mercancía, limpieza, formación '
           'y reuniones. Si lo pones al 100 % estarás repartiendo el coste de '
           'personal entre horas que no existen.')
    motor.val(ws, 'A%d' % R_HORA_OBR, 'COSTE DE UNA HORA DE OBRADOR (€)',
              bold=True)
    motor.f(ws, 'B%d' % R_HORA_OBR,
            ie('SUMPRODUCT((K{0}:K{1}="OBRADOR")*I{0}:I{1})'
               '/SUMPRODUCT((K{0}:K{1}="OBRADOR")*C{0}:C{1}*B{0}:B{1})'
               '/$B${2}/$B${3}'.format(R_INI, R_FIN, R_HORAS_ANIO, R_RATIO)),
            fmt=C.EUR, bold=True)
    C.total_fila(ws, R_HORA_OBR, 'AB')
    C.nota(ws, 'L%d' % R_HORA_OBR,
           'Coste empresa de las personas del ÁREA OBRADOR dividido entre sus '
           'horas PRODUCTIVAS. No es el bruto ni el bruto con Seguridad '
           'Social: es lo que de verdad cuesta un minuto de templado, y es el '
           'número que usan el escandallo del libro 4 y la hoja de talleres '
           'para saber lo que cuesta un docente.')
    C.parrafo(ws, R_NOTA,
              'El refuerzo de las campañas NO está en este cuadro: la '
              'estacionalidad manda horas extra en Navidad, en San Valentín y '
              'en comuniones, y eso se dimensiona y se cuesta en el libro '
              '«campanas-y-valle-del-ano». Aquí está la plantilla ESTABLE, que '
              'es la que entra en los costes fijos del P&L. Y una nota de '
              'método: los tres nombres de perfil son los de las hojas del kit '
              'de tareas -Encargado, Chocolatero y Dependiente-, no «maestro '
              'chocolatero» ni «bombonero», que son etiquetas de fuentes '
              'salariales y no puestos de esta casa.', 'A', 'L', alto=58)
    ws.freeze_panes = 'A%d' % (R_CAB + 1)
    C.pagina(ws, titulos='$%d:$%d' % (R_CAB, R_CAB), area='A1:L%d' % R_NOTA)
    return ws


# ==========================================================================
# Hoja «Tesorería 12 meses» (recibe el cruce 7 <- 1)
# ==========================================================================
def hoja_tesoreria(wb):
    ws = wb.create_sheet(H_TES)
    C.anchos(ws, dict([('A', 52)] + [(c, 13) for c in MESES_COL]
                      + [('N', 15), ('O', 86)]))
    C.encabezar(ws, 'Tesorería de los 12 primeros meses',
                'El P&L dice si el negocio gana dinero; esta hoja dice si le '
                'queda caja para llegar a fin de mes. Es la primera que mira '
                'un banco, y la que más aperturas ha salvado. Abajo, la fecha '
                'límite de cierre de pedidos de Navidad, calculada hacia atrás '
                'desde la capacidad de tu obrador.', col_fin='O')
    C.cabecera(ws, T['cab'],
               [('A', 'Concepto')]
               + [(c, 'Mes %d' % (i + 1)) for i, c in enumerate(MESES_COL)]
               + [('N', 'Año (€)'), ('O', 'Notas')])

    LETRAS = ['A'] + list(MESES_COL) + ['N', 'O']

    def sec(fila, texto):
        C.banda(ws, fila, LETRAS, texto)

    # OJO: las filas de estacionalidad, rampa y reparto NO pueden llevar la
    # guarda contra el P&L. «0. Supuestos» calcula desde ellas la actividad del
    # año 1, y el P&L calcula sus ingresos desde ese dato: guardarlas contra el
    # P&L cierra una referencia circular que Excel detecta y pycel no resuelve.
    def g(expr):
        return ie('IF({0}$B${1}="","",{2})'.format(Q_PYG, P['ingresos'], expr))

    # --- estacionalidad y rampa -------------------------------------------
    motor.val(ws, 'A%d' % T['estacionalidad'],
              'Estacionalidad del mes (tiene que sumar 100 %)')
    for i, col in enumerate(MESES_COL):
        C.entrada(ws, '%s%d' % (col, T['estacionalidad']),
                  round(D.estacionalidad_pesos()[i], 6), fmt=C.PCT2,
                  etiqueta='Estacionalidad del mes %d' % (i + 1))
    motor.f(ws, 'N%d' % T['estacionalidad'],
            ie('SUM(B%d:M%d)' % (T['estacionalidad'], T['estacionalidad'])),
            fmt=C.PCT)
    C.nota(ws, 'O%d' % T['estacionalidad'],
           'DICIEMBRE manda, y AGOSTO es el suelo: son los doce coeficientes '
           'del calendario de campañas del kit traducidos a euros, con media '
           '1,000 exacta. Agosto NO vale cero -la tienda abre para el turista '
           'aunque el obrador pare-, y por eso el valle se nota en el margen y '
           'no en la persiana. SON SUPUESTOS: no existe reparto mensual '
           'publicado de las ventas de una chocolatería, y la guía te enseña a '
           'medir el tuyo con el TPV.')
    ws.row_dimensions[T['estacionalidad']].height = 30

    motor.val(ws, 'A%d' % T['rampa'],
              'Rampa de arranque (% de la actividad de crucero)')
    for i, col in enumerate(MESES_COL):
        motor.f(ws, '%s%d' % (col, T['rampa']),
                ie('MIN(1,{0}+(1-{0})*{1}/MAX(1,{2}-1))'
                   .format(sup('rampa1'), i, sup('rampa_meses'))), fmt=C.PCT)
    C.nota(ws, 'O%d' % T['rampa'],
           'Sube en línea recta desde el porcentaje del mes 1 hasta el 100 % '
           'en los meses que digas en «0. Supuestos». Con el 100 % en el mes 1 '
           'la rampa desaparece, y entonces estás proyectando una apertura que '
           'no existe. Ojo al calendario: este caso abre el 1 de junio, así '
           'que el mes 3 de la rampa es agosto.')

    motor.val(ws, 'A%d' % T['reparto'],
              'Reparto de la actividad por mes (calculado)')
    for col in MESES_COL:
        motor.f(ws, '%s%d' % (col, T['reparto']),
                ie('{0}{1}*{0}{2}/SUMPRODUCT($B${1}:$M${1},$B${2}:$M${2})'
                   .format(col, T['estacionalidad'], T['rampa'])), fmt=C.PCT2)
    motor.f(ws, 'N%d' % T['reparto'],
            ie('SUM(B%d:M%d)' % (T['reparto'], T['reparto'])), fmt=C.PCT)
    C.nota(ws, 'O%d' % T['reparto'],
           'Estacionalidad x rampa, normalizado al 100 %: el AÑO factura lo '
           'que dice el P&L, pero repartido como lo reparte la realidad.')

    # --- cobros ------------------------------------------------------------
    sec(T['sec_cobros'], 'COBROS')
    motor.val(ws, 'A%d' % T['ventas'],
              'Ventas cobradas (con el IVA repercutido dentro)')
    for i, col in enumerate(MESES_COL):
        base = '{0}$B${1}*(1+{2})'.format(Q_PYG, P['ingresos'],
                                          sup('iva_medio'))
        if i == 0:
            reparto = '{0}{1}*(1-{2}/30)'.format(col, T['reparto'],
                                                 sup('dias_cobro'))
        else:
            ant = MESES_COL[i - 1]
            reparto = ('{0}{1}*(1-{3}/30)+{2}{1}*({3}/30)'
                       .format(col, T['reparto'], ant, sup('dias_cobro')))
        motor.f(ws, '%s%d' % (col, T['ventas']),
                g('%s*(%s)' % (base, reparto)), fmt=C.EUR)
    motor.f(ws, 'N%d' % T['ventas'],
            g('SUM(B%d:M%d)' % (T['ventas'], T['ventas'])), fmt=C.EUR)
    C.nota(ws, 'O%d' % T['ventas'],
           'Ventas del mes con el IVA repercutido, corregidas por los días '
           'medios de cobro que calcula la hoja de canales. El mostrador y el '
           'taller cobran al contado; el corporativo a 30 días y el B2B a 45, '
           'y ahí financias tú.')

    # --- pagos -------------------------------------------------------------
    sec(T['sec_pagos'], 'PAGOS')
    motor.val(ws, 'A%d' % T['compras'],
              'Compras y coste de ventas (IVA incluido)')
    for i, col in enumerate(MESES_COL):
        base = '{0}$B${1}*(1+{0}$F${1})'.format(Q_PYG, P['coste_ventas'])
        if i == 0:
            reparto = '{0}{1}*(1-{2}/30)'.format(col, T['reparto'],
                                                 sup('dias_pago'))
        else:
            ant = MESES_COL[i - 1]
            reparto = ('{0}{1}*(1-{3}/30)+{2}{1}*({3}/30)'
                       .format(col, T['reparto'], ant, sup('dias_pago')))
        # El mes 1 no paga nada (pago a 30 días) y la negación de un cero da
        # CERO NEGATIVO, que se imprime «-0 €» en el documento que va al banco.
        # El «+0» lo devuelve a cero positivo.
        motor.f(ws, '%s%d' % (col, T['compras']),
                g('-%s*(%s)+0' % (base, reparto)), fmt=C.EUR)
    motor.f(ws, 'N%d' % T['compras'],
            g('SUM(B%d:M%d)' % (T['compras'], T['compras'])), fmt=C.EUR)
    C.nota(ws, 'O%d' % T['compras'],
           'Con los días medios de pago a proveedor de «0. Supuestos». A 30 '
           'días el mes 1 no paga nada: el proveedor te está financiando el '
           'arranque, y por eso perder ese crédito por un retraso sale tan '
           'caro. Ojo a la compra de cobertura de Navidad, que se paga en '
           'octubre y se cobra en diciembre.')

    motor.val(ws, 'A%d' % T['fijos'],
              'Costes fijos de explotación (IVA incluido)')
    for col in MESES_COL:
        motor.f(ws, '%s%d' % (col, T['fijos']),
                g('-(({0}$B${1}-{0}$B${2}-{0}$B${3}-{0}$B${4})+{0}$B${5})/12'
                  .format(Q_PYG, P['tot_fijos'], P['personal'],
                          P['amortizacion'], P['financieros'],
                          P['iva_fijos'])), fmt=C.EUR)
    motor.f(ws, 'N%d' % T['fijos'],
            g('SUM(B%d:M%d)' % (T['fijos'], T['fijos'])), fmt=C.EUR)
    C.nota(ws, 'O%d' % T['fijos'],
           'Los fijos que salen de caja, cada uno con su tipo de IVA: sin las '
           'nóminas (van abajo), sin la amortización (no se paga) y sin los '
           'intereses (van aparte). La cuota de autónomos del titular SÍ está '
           'aquí: se paga todos los meses, también en agosto.')

    motor.val(ws, 'A%d' % T['nominas'], 'Nóminas y Seguridad Social')
    for i, col in enumerate(MESES_COL):
        mes = i + 1
        extras = '+'.join('IF(%d=%s,1,0)' % (mes, sup(k))
                          for k in ('extra1', 'extra2', 'extra3'))
        motor.f(ws, '%s%d' % (col, T['nominas']),
                g('-{0}$B${1}/MAX(12,{2})*(1+{3})'
                  .format(Q_PYG, P['personal'], sup('pagas'), extras)),
                fmt=C.EUR)
    motor.f(ws, 'N%d' % T['nominas'],
            g('SUM(B%d:M%d)' % (T['nominas'], T['nominas'])), fmt=C.EUR)
    C.nota(ws, 'O%d' % T['nominas'],
           'Doce mensualidades más las pagas extra en los meses que digas. Con '
           '15 pagas hay tres meses que salen dobles, y siempre pillan a '
           'contrapié: uno de ellos suele caer en el mes flojo.')

    motor.val(ws, 'A%d' % T['intereses'], 'Intereses del préstamo')
    motor.val(ws, 'A%d' % T['principal'],
              'Devolución de principal del préstamo')
    for i, col in enumerate(MESES_COL):
        fila_mes = F_MES_INI + i
        for clave, letra in (('intereses', 'C'), ('principal', 'D')):
            motor.f(ws, '%s%d' % (col, T[clave]),
                    g('-IF({0}{1}{2}="",0,{0}{1}{2})'
                      .format(Q_FIN, letra, fila_mes)), fmt=C.EUR)
    for clave in ('intereses', 'principal'):
        motor.f(ws, 'N%d' % T[clave],
                g('SUM(B%d:M%d)' % (T[clave], T[clave])), fmt=C.EUR)
    C.nota(ws, 'O%d' % T['principal'],
           'Sale del cuadro MENSUAL de la hoja de Financiación. Durante la '
           'carencia esta fila vale cero, y ése es justo el efecto que se '
           'negocia con el banco.')

    # --- IVA ---------------------------------------------------------------
    motor.val(ws, 'A%d' % T['iva_rep'], 'IVA repercutido del mes (memoria)')
    motor.val(ws, 'A%d' % T['iva_sop'], 'IVA soportado del mes (memoria)')
    for col in MESES_COL:
        motor.f(ws, '%s%d' % (col, T['iva_rep']),
                g('{0}$B${1}*{2}{3}*{4}'
                  .format(Q_PYG, P['ingresos'], col, T['reparto'],
                          sup('iva_medio'))), fmt=C.EUR)
        motor.f(ws, '%s%d' % (col, T['iva_sop']),
                g('{0}$B${1}*{2}{3}+{0}$B${4}/12'
                  .format(Q_PYG, P['iva_var'], col, T['reparto'],
                          P['iva_fijos'])), fmt=C.EUR)
    for clave in ('iva_rep', 'iva_sop'):
        motor.f(ws, 'N%d' % T[clave],
                g('SUM(B%d:M%d)' % (T[clave], T[clave])), fmt=C.EUR)

    motor.val(ws, 'A%d' % T['iva_arr'],
              'IVA a compensar arrastrado (inversión incluida)')
    motor.val(ws, 'A%d' % T['iva_liq'],
              'Resultado de la liquidación trimestral')
    motor.val(ws, 'A%d' % T['iva_pago'], 'Pago del IVA (modelo 303)')
    TRIM = (('E', 'B', 'D', None), ('H', 'E', 'G', 'E'), ('K', 'H', 'J', 'H'))
    for col, ini, fin, previo in TRIM:
        if previo is None:
            motor.f(ws, '%s%d' % (col, T['iva_arr']),
                    g('%s$B$%d' % (Q_INV, IV['iva'])), fmt=C.EUR)
        else:
            motor.f(ws, '%s%d' % (col, T['iva_arr']),
                    g('MAX(0,-%s%d)' % (previo, T['iva_liq'])), fmt=C.EUR)
        motor.f(ws, '%s%d' % (col, T['iva_liq']),
                g('SUM({0}{2}:{1}{2})-SUM({0}{3}:{1}{3})-{4}{5}'
                  .format(ini, fin, T['iva_rep'], T['iva_sop'], col,
                          T['iva_arr'])), fmt=C.EUR)
        motor.f(ws, '%s%d' % (col, T['iva_pago']),
                g('IF({0}{1}<=0,"",-{0}{1})'.format(col, T['iva_liq'])),
                fmt=C.EUR)
    motor.f(ws, 'N%d' % T['iva_pago'],
            g('IF(E{0}="",0,E{0})+IF(H{0}="",0,H{0})+IF(K{0}="",0,K{0})'
              .format(T['iva_pago'])), fmt=C.EUR)
    C.nota(ws, 'O%d' % T['iva_arr'],
           'El IVA soportado de la INVERSIÓN entra aquí y se compensa contra '
           'el repercutido de los trimestres siguientes. Con una inversión '
           'grande tardas medio año en recuperarlo, y ese medio año lo '
           'financias tú.')
    C.nota(ws, 'O%d' % T['iva_pago'],
           'Sólo sale caja cuando el resultado del trimestre es positivo. Los '
           'meses sin liquidación van en BLANCO, no a cero: un cero '
           'significaría «liquidé y no pagué nada», que es otra cosa. El '
           'cuarto trimestre se liquida en enero del año siguiente y por eso '
           'no aparece.')

    # --- flujo y saldo -----------------------------------------------------
    motor.val(ws, 'A%d' % T['flujo'], 'FLUJO DEL MES', bold=True)
    for col in MESES_COL:
        motor.f(ws, '%s%d' % (col, T['flujo']),
                g('SUM({0}{1}:{0}{2})+IF({0}{3}="",0,{0}{3})'
                  .format(col, T['ventas'], T['principal'], T['iva_pago'])),
                fmt=C.EUR, bold=True)
    motor.f(ws, 'N%d' % T['flujo'],
            g('SUM(B%d:M%d)' % (T['flujo'], T['flujo'])), fmt=C.EUR, bold=True)
    C.total_fila(ws, T['flujo'], LETRAS)

    motor.val(ws, 'A%d' % T['saldo'], 'SALDO ACUMULADO DE CAJA', bold=True)
    for i, col in enumerate(MESES_COL):
        if i == 0:
            expr = '%s$B$%d+%s%d' % (Q_INV, IV['fondo'], col, T['flujo'])
        else:
            expr = '%s%d+%s%d' % (MESES_COL[i - 1], T['saldo'], col,
                                  T['flujo'])
        motor.f(ws, '%s%d' % (col, T['saldo']), g(expr), fmt=C.EUR, bold=True)
    C.total_fila(ws, T['saldo'], LETRAS)
    motor.semaforo_isnumber(ws, 'B%d:M%d' % (T['saldo'], T['saldo']),
                            'B%d' % T['saldo'], operador='<', umbral='0')

    motor.val(ws, 'A%d' % T['saldo_min'], 'Saldo mínimo del año (€)')
    motor.f(ws, 'B%d' % T['saldo_min'],
            g('IF(COUNT(B{0}:M{0})=0,"",MIN(B{0}:M{0}))'.format(T['saldo'])),
            fmt=C.EUR)
    motor.semaforo_isnumber(ws, 'B%d:B%d' % (T['saldo_min'], T['saldo_min']),
                            '$B$%d' % T['saldo_min'], operador='<', umbral='0')
    C.nota(ws, 'O%d' % T['saldo_min'],
           'Si es negativo te quedas sin caja: sube el fondo de maniobra, sube '
           'el préstamo o negocia más carencia. No lo dejes para verlo pasar.')
    motor.val(ws, 'A%d' % T['mes_fondo'], 'Mes en el que la caja toca fondo')
    motor.f(ws, 'B%d' % T['mes_fondo'],
            g('IF(COUNT(B{0}:M{0})=0,"",MATCH(MIN(B{0}:M{0}),B{0}:M{0},0))'
              .format(T['saldo'])), fmt=C.ENT)
    C.nota(ws, 'O%d' % T['mes_fondo'],
           'Es la respuesta a la pregunta que decide una operación bancaria: '
           'en qué mes se agota la caja. Abriendo el 1 de junio, ese mes cae '
           'casi siempre en el valle.')

    # --- retorno -----------------------------------------------------------
    sec(T['sec_retorno'], 'RETORNO DE LA INVERSIÓN')
    for clave, col_pyg, anio in (('fcf1', 'B', 0), ('fcf2', 'C', 1),
                                 ('fcf3', 'D', 2)):
        motor.val(ws, 'A%d' % T[clave],
                  'Flujo de caja libre antes de la deuda, año %d' % (anio + 1))
        motor.f(ws, 'B%d' % T[clave],
                g('{0}{1}{2}+{0}{1}{3}+{4}$B${5}'
                  .format(Q_PYG, col_pyg, P['neto'], P['amortizacion'],
                          Q_FIN, F_ANIO_INI + anio)), fmt=C.EUR)
    C.nota(ws, 'O%d' % T['fcf1'],
           'Resultado neto más amortización (que no se paga) más los intereses '
           'de ese año: el principal no se resta porque este flujo se compara '
           'con la inversión, no con la deuda.')
    motor.val(ws, 'A%d' % T['inversion'],
              'Inversión a recuperar (sin el IVA, que se recupera por el 303)')
    motor.f(ws, 'B%d' % T['inversion'],
            g('%s$B$%d-%s$B$%d' % (Q_INV, IV['necesidad'], Q_INV, IV['iva'])),
            fmt=C.EUR)
    motor.val(ws, 'A%d' % T['payback'],
              'Payback del proyecto (años), antes de la deuda')
    motor.f(ws, 'B%d' % T['payback'],
            g('IF(B{1}>=B{0},ROUND(B{0}/B{1},1),'
              'IF(B{1}+B{2}>=B{0},ROUND(1+(B{0}-B{1})/B{2},1),'
              'IF(B{1}+B{2}+B{3}>=B{0},ROUND(2+(B{0}-B{1}-B{2})/B{3},1),'
              '"Más de 3 años")))'
              .format(T['inversion'], T['fcf1'], T['fcf2'], T['fcf3'])),
            fmt=C.DEC1)
    C.nota(ws, 'O%d' % T['payback'],
           'Cuánto tarda el negocio en devolver la inversión con lo que genera '
           'ANTES de pagar al banco. Si sale «Más de 3 años», este libro no '
           'proyecta lo suficiente para decírtelo: es una señal, no un fallo.')

    # --- cruce 7 <- 1 y la fecha límite de Navidad ------------------------
    sec(T['sec_nav'],
        'LA FECHA LÍMITE DE CIERRE DE PEDIDOS DE NAVIDAD (cruce 7 '
        + chr(60) + '- 1, calculada HACIA ATRÁS desde tu capacidad)')
    motor.val(ws, 'A%d' % T['cap_trae'],
              'Capacidad del obrador en jornada normal (bombones/día): trae '
              'aquí la cifra de ' + ORIGEN_CAP, wrap=True)
    C.entrada(ws, 'B%d' % T['cap_trae'], DEF_CAPACIDAD, fmt=C.ENT,
              etiqueta='Capacidad diaria traída del libro 1')
    C.nota(ws, 'O%d' % T['cap_trae'],
           'CÓPIALA A MANO del libro «capacidad-obrador-y-clima»: la casilla de '
           'bombones al día que permite el equipo que limita. No hay ninguna '
           'fórmula entre ficheros. VALOR POR DEFECTO DECLARADO: los 512 '
           'bombones al día del caso, con el puesto de envasado y montaje de '
           'cajas como cuello de botella. Si cambias de atemperadora, de '
           'moldes o de puesto de envasado, vuelve a copiarlo.')
    ws.row_dimensions[T['cap_trae']].height = 44
    motor.val(ws, 'A%d' % T['cap_orig'],
              'Cifra que publica hoy esa hoja del libro 1')
    C.entrada(ws, 'B%d' % T['cap_orig'], DEF_CAPACIDAD, fmt=C.ENT,
              etiqueta='Capacidad que publica el libro 1')
    C.nota(ws, 'O%d' % T['cap_orig'],
           'Anota aquí lo que ves en el libro 1 la última vez que lo abriste. '
           'Si arriba tecleas otra cosa -porque te lo dijo el instalador, o '
           'porque cuentas con horas extra-, la fila de CUADRE te avisa en vez '
           'de dejar las dos cifras separadas en silencio.')
    motor.val(ws, 'A%d' % T['cap_desv'], 'Desviación entre las dos')
    motor.f(ws, 'B%d' % T['cap_desv'],
            ie('ABS(B%d-B%d)/B%d'
               % (T['cap_trae'], T['cap_orig'], T['cap_orig'])), fmt=C.PCT2)
    motor.val(ws, 'A%d' % T['cap_cuadre'],
              'CUADRE DE LA CAPACIDAD: la que usas frente a la del libro 1',
              bold=True)
    motor.f(ws, 'B%d' % T['cap_cuadre'],
            ie('IF(NOT(ISNUMBER(B%d)),"",IF(B%d<=%s,"CUADRA","REVISA: la '
               'capacidad que estás usando no es la que calcula el libro 1"))'
               % (T['cap_desv'], T['cap_desv'], sup('tolerancia'))), bold=True)
    C.destacado(ws, 'B%d' % T['cap_cuadre'])
    motor.semaforo_texto(ws, 'B%d' % T['cap_cuadre'],
                         (('REVISA: la capacidad que estás usando no es la que '
                           'calcula el libro 1', motor.CF_ROJO_BG,
                           motor.CF_ROJO_FG),
                          ('CUADRA', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))

    motor.val(ws, 'A%d' % T['base_dia'],
              'Bombones de obrador al día en velocidad de crucero')
    C.entrada(ws, 'B%d' % T['base_dia'], DEF_BASE_DIA, fmt=C.ENT,
              etiqueta='Bombones de obrador al día en crucero')
    C.nota(ws, 'O%d' % T['base_dia'],
           'Lo que sale del obrador un día normal, contado en BOMBONES DE '
           'OBRADOR: una caja de 35 es una venta y treinta y seis piezas. Sale '
           'del mismo libro 1; medir el pico en tickets es lo que hace creer '
           'que Navidad cabe.')
    motor.val(ws, 'A%d' % T['excedente'],
              'Excedente diario para adelantar producción (bombones/día)')
    motor.f(ws, 'B%d' % T['excedente'],
            ie('B%d-B%d' % (T['cap_trae'], T['base_dia'])), fmt=C.ENT)
    motor.semaforo_isnumber(ws, 'B%d:B%d' % (T['excedente'], T['excedente']),
                            '$B$%d' % T['excedente'], operador='<=',
                            umbral='0')
    C.nota(ws, 'O%d' % T['excedente'],
           'Lo que te sobra cada día para ir haciendo Navidad por delante. Si '
           'sale cero o negativo, no hay fecha límite que valga: no puedes '
           'adelantar nada y la campaña se resuelve con horas extra, con '
           'refuerzo o diciendo que no. Eso se dimensiona en el libro '
           '«campanas-y-valle-del-ano».')
    motor.val(ws, 'A%d' % T['piezas_nav'],
              'Bombones de la campaña de Navidad que quieres tener hechos POR '
              'ADELANTADO', wrap=True)
    C.entrada(ws, 'B%d' % T['piezas_nav'], 2400, fmt=C.ENT,
              etiqueta='Bombones de Navidad fabricados por adelantado')
    C.nota(ws, 'O%d' % T['piezas_nav'],
           'SUPUESTO, y OJO CON LO QUE ES: NO es lo que vas a vender en '
           'diciembre, que es muchísimo más. Es lo que quieres tener '
           'FABRICADO Y GUARDADO antes de que empiece la punta, y por eso sólo '
           'caben las referencias que aguantan -tabletas, turrones, figuras y '
           'bombones estabilizados-, nunca la ganache fresca. Todo lo que no '
           'quepa aquí se resuelve con horas extra y refuerzo, y eso se '
           'dimensiona y se cuesta en el libro «campanas-y-valle-del-ano».')
    ws.row_dimensions[T['piezas_nav']].height = 30
    motor.val(ws, 'A%d' % T['dias_prod'],
              'Días de obrador que hacen falta para fabricarlos')
    motor.f(ws, 'B%d' % T['dias_prod'],
            ie('IF(B%d<=0,"",B%d/B%d)'
               % (T['excedente'], T['piezas_nav'], T['excedente'])),
            fmt=C.DEC1)
    motor.val(ws, 'A%d' % T['dias_nat'],
              'Días de calendario que hay que empezar antes')
    motor.f(ws, 'B%d' % T['dias_nat'],
            ie('IF(B%d="","",ROUND(B%d*7/%s,0))'
               % (T['dias_prod'], T['dias_prod'], sup('dias_semana'))),
            fmt=C.ENT)
    C.nota(ws, 'O%d' % T['dias_nat'],
           'De días de PRODUCCIÓN a días de calendario: si abres seis días de '
           'cada siete, cada día de obrador son 1,17 días naturales. Sin '
           'NETWORKDAYS, que esta familia tiene prohibida: aritmética de días '
           'y de índices de mes, que se entiende y se audita.')
    motor.val(ws, 'A%d' % T['entrega'],
              'Fecha en la que tiene que estar todo hecho')
    C.entrada(ws, 'B%d' % T['entrega'], datetime.date(2027, 12, 20),
              fmt=C.FECHA, etiqueta='Fecha de entrega de la campaña de Navidad')
    C.nota(ws, 'O%d' % T['entrega'],
           'SUPUESTO: el 20 de diciembre, que es cuando se lleva el grueso de '
           'los encargos. Ponla del año que estés planificando.')
    motor.val(ws, 'A%d' % T['limite'],
              'FECHA LÍMITE DE CIERRE DE PEDIDOS DE NAVIDAD', bold=True)
    motor.f(ws, 'B%d' % T['limite'],
            ie('IF(B%d="","",B%d-B%d)'
               % (T['dias_nat'], T['entrega'], T['dias_nat'])), fmt=C.FECHA,
            bold=True)
    C.total_fila(ws, T['limite'], ['A', 'B'])
    C.nota(ws, 'O%d' % T['limite'],
           'A partir de aquí, cada pedido nuevo de Navidad te obliga a comprar '
           'horas o a decir que no. NO es una fecha comercial: la fija tu '
           'obrador, y por eso se calcula hacia atrás desde la capacidad y no '
           'desde el calendario de marketing.')
    motor.val(ws, 'A%d' % T['mes_limite'],
              'Mes en el que cae esa fecha (índice 1-12)')
    motor.f(ws, 'B%d' % T['mes_limite'],
            ie('IF(B%d="","",MONTH(B%d))' % (T['limite'], T['limite'])),
            fmt=C.ENT)
    motor.val(ws, 'A%d' % T['veredicto_nav'], 'LECTURA', bold=True)
    motor.f(ws, 'B%d' % T['veredicto_nav'],
            ie('IF(B{0}="","No hay excedente diario: no puedes adelantar nada '
               'y la campaña se resuelve con refuerzo",IF(B{1}<=10,'
               '"Cierras en octubre o antes: la agenda corporativa y la de '
               'encargos tienen que estar montadas en septiembre",'
               '"Cierras dentro de noviembre o diciembre: vas justo, y una '
               'avería te deja sin campaña"))'
               .format(T['dias_nat'], T['mes_limite'])), bold=True)
    C.destacado(ws, 'B%d' % T['veredicto_nav'])
    C.parrafo(ws, T['nota_nav'],
              'Esta fecha es la que convierte la capacidad del obrador en una '
              'decisión comercial: hasta ella coges encargos, después empiezas '
              'a comprar horas. Y explica por qué el pedido de regalo '
              'corporativo se cierra en octubre: entre que el cliente aprueba '
              'la muestra y tú fabricas pasan catorce días como mínimo, y esos '
              'catorce días caen ENCIMA de los que acabas de calcular.',
              'A', 'O', alto=44)

    C.parrafo(ws, T['nota'],
              'Escribe los ingresos y los gastos SIN IVA en el resto del '
              'libro: la capa de IVA de esta hoja lo añade, porque la '
              'tesorería es caja. El Impuesto de Sociedades no está en este '
              'cuadro: se paga en julio del año siguiente, fuera de los doce '
              'meses.', 'A', 'O', alto=32)
    ws.freeze_panes = 'B%d' % (T['cab'] + 1)
    C.pagina(ws, titulos='$%d:$%d' % (T['cab'], T['cab']),
             area='A1:O%d' % T['nota'])
    return ws


# ==========================================================================
# Hoja «Financiación»
# ==========================================================================
def hoja_financiacion(wb):
    ws = wb.create_sheet(H_FIN)
    C.anchos(ws, {'A': 52, 'B': 16, 'C': 16, 'D': 18, 'E': 16, 'F': 17,
                  'G': 14, 'H': 76})
    C.encabezar(ws, 'Financiación: de dónde sale y cuánto cuesta devolverlo',
                'El cuadro de amortización es MENSUAL, con 84 filas, porque la '
                'carencia de este caso son seis meses y un cuadro anual no '
                'sabe expresar medio año. La cuota es una anualidad algebraica '
                'del sistema francés: PMT está prohibida en esta familia.',
                col_fin='H')

    def sec(fila, texto):
        C.banda(ws, fila, 'ABCDEFGH', texto)

    def linea(fila, etiqueta, formula, fmt, nota_txt=None, bold=None,
              verde=None):
        motor.val(ws, 'A%d' % fila, etiqueta, bold=bold)
        if verde is not None:
            C.entrada(ws, 'B%d' % fila, verde, fmt=fmt, etiqueta=etiqueta,
                      bold=bold)
        else:
            motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=bold)
        if nota_txt:
            C.nota(ws, 'H%d' % fila, nota_txt)

    sec(F['sec_origen'], 'ORIGEN DE FONDOS')
    linea(F['propios'], 'Recursos propios aportados', ie(sup('propios')),
          C.EUR,
          'Aportación de los socios o del promotor. Un banco quiere ver un '
          '25-30 % de fondos propios sobre la necesidad total antes de '
          'sentarse a hablar. Aquí es el 40 %, que es la estructura declarada '
          'del caso.')
    linea(F['prestamo'], 'Préstamo bancario', ie(sup('principal')), C.EUR)
    linea(F['otras'], 'Otras fuentes (ICO, ENISA, subvenciones, socios)', None,
          C.EUR,
          'A cero por defecto. Las subvenciones suelen cobrarse DESPUÉS de '
          'justificar el gasto: no cuentes con ellas para pagar la obra.',
          verde=0.0)
    linea(F['tot_origen'], 'TOTAL ORIGEN DE FONDOS',
          ie('IF(COUNT(B%d:B%d)=0,"",SUM(B%d:B%d))'
             % (F['propios'], F['otras'], F['propios'], F['otras'])), C.EUR,
          bold=True)
    C.total_fila(ws, F['tot_origen'], 'ABCDEFGH')

    sec(F['sec_usos'], 'USOS')
    linea(F['necesidad'], 'Necesidad total de caja al arranque',
          ie('%s$B$%d' % (Q_INV, IV['necesidad'])), C.EUR,
          'Inversión total -CAPEX más fondo de maniobra- y el IVA que hay que '
          'adelantar.')
    linea(F['diferencia'], 'Diferencia (origen menos usos)',
          ie('B%d-B%d' % (F['tot_origen'], F['necesidad'])), C.EUR,
          'En negativo el plan NO está financiado. Muy por encima de cero '
          'tampoco es gratis: son intereses que pagas sin necesitarlos.')
    motor.semaforo_isnumber(ws, 'B%d:B%d' % (F['diferencia'], F['diferencia']),
                            '$B$%d' % F['diferencia'], operador='<',
                            umbral='0')
    linea(F['dif_pct'], 'Diferencia sobre los usos (%)',
          ie('B%d/B%d' % (F['diferencia'], F['necesidad'])), C.PCT)
    linea(F['ajuste'], 'Préstamo que ajustaría el origen a la necesidad',
          ie('MAX(0,B%d-B%d+B%d)'
             % (F['necesidad'], F['tot_origen'], F['prestamo'])), C.EUR,
          'Cópialo en «Préstamo bancario solicitado» de «0. Supuestos» y la '
          'diferencia de arriba se pone a cero. Después mira el DSCR: pedir '
          'más siempre se puede, devolverlo no.')

    sec(F['sec_cond'], 'CONDICIONES DEL PRÉSTAMO')
    linea(F['principal'], 'Importe del principal',
          ie('IF(%s=0,"",%s)' % (sup('principal'), sup('principal'))), C.EUR)
    linea(F['tipo'], 'Tipo de interés nominal anual', ie(sup('tipo')), C.PCT2)
    linea(F['tipo_mes'], 'Tipo mensual', ie('B%d/12' % F['tipo']), C.PCT4)
    linea(F['plazo'], 'Plazo total (meses)', ie(sup('plazo')), C.ENT)
    linea(F['carencia'], 'Carencia de principal aplicada (meses)',
          ie('IF(%s>=%s,%s-1,%s)' % (sup('carencia'), sup('plazo'),
                                     sup('plazo'), sup('carencia'))), C.ENT,
          'Una carencia igual o mayor que el plazo no existe: la hoja la anula '
          'en origen.')
    linea(F['meses_am'], 'Meses de amortización',
          ie('B%d-B%d' % (F['plazo'], F['carencia'])), C.ENT)
    linea(F['cuota'], 'Cuota mensual durante la amortización',
          ie('IF(B{0}<=0,"",IF(B{1}=0,B{2}/B{0},'
             'B{2}*B{1}/(1-(1+B{1})^(-B{0}))))'
             .format(F['meses_am'], F['tipo_mes'], F['principal'])), C.EUR,
          bold=True)
    C.total_fila(ws, F['cuota'], 'ABCDEFGH')
    C.parrafo(ws, F['nota_cuota'],
              'Sistema francés, escrito como anualidad algebraica: capital x '
              'tipo mensual dividido por uno menos (uno más el tipo) elevado a '
              'menos el número de cuotas. Con el tipo al 0 % es el principal '
              'entre los meses de amortización. No se usa la función PMT: esta '
              'familia la tiene prohibida porque no todos los motores de hoja '
              'de cálculo la evalúan igual.', 'A', 'H', alto=40)

    # --- cuadro mensual ----------------------------------------------------
    C.cabecera(ws, F['cab'],
               [('A', 'Mes'), ('B', 'Capital pendiente (€)'),
                ('C', 'Intereses (€)'), ('D', 'Amortización de principal (€)'),
                ('E', 'Cuota total (€)'), ('F', 'Capital al cierre (€)'),
                ('G', ''), ('H', 'Notas')])
    for i in range(F_MESES):
        fila = F_MES_INI + i
        motor.val(ws, 'A%d' % fila, i + 1, fmt=C.ENT, align='center')
        if i == 0:
            motor.f(ws, 'B%d' % fila,
                    ie('IF($B$%d="","",$B$%d)'
                       % (F['principal'], F['principal'])), fmt=C.EUR)
        else:
            motor.f(ws, 'B%d' % fila,
                    ie('IF(OR(A{0}>$B${1},F{2}=""),"",F{2})'
                       .format(fila, F['plazo'], fila - 1)), fmt=C.EUR)
        motor.f(ws, 'C%d' % fila,
                ie('IF(OR(A{0}>$B${1},B{0}=""),"",B{0}*$B${2})'
                   .format(fila, F['plazo'], F['tipo_mes'])), fmt=C.EUR)
        motor.f(ws, 'D%d' % fila,
                ie('IF(OR(A{0}>$B${1},B{0}=""),"",IF(A{0}<=$B${2},0,'
                   'MIN(B{0},$B${3}-C{0})))'
                   .format(fila, F['plazo'], F['carencia'], F['cuota'])),
                fmt=C.EUR)
        motor.f(ws, 'E%d' % fila,
                ie('IF(C{0}="","",C{0}+D{0})'.format(fila)), fmt=C.EUR)
        motor.f(ws, 'F%d' % fila,
                ie('IF(D{0}="","",B{0}-D{0})'.format(fila)), fmt=C.EUR)
    C.nota(ws, 'H%d' % F_MES_INI,
           'Durante la carencia la columna de amortización vale cero y sólo se '
           'pagan intereses. Es lo que hace que el préstamo no se coma la caja '
           'en la rampa de arranque, y es lo primero que hay que negociar.')

    motor.val(ws, 'A%d' % F_TOL, 'Tolerancia de cierre del cuadro (€)')
    C.entrada(ws, 'B%d' % F_TOL, 0.01, fmt=C.EUR,
              etiqueta='Tolerancia de cierre del cuadro')
    motor.val(ws, 'A%d' % F_PENDIENTE, 'Capital pendiente al vencimiento')
    motor.f(ws, 'B%d' % F_PENDIENTE,
            ie('IF($B${0}="","",ROUND($B${0}-SUM(D{1}:D{2}),2))'
               .format(F['principal'], F_MES_INI, F_MES_FIN)), fmt=C.EUR)
    motor.val(ws, 'A%d' % F_CIERRA, '¿Cierra el cuadro de amortización?')
    motor.f(ws, 'B%d' % F_CIERRA,
            ie('IF(B{0}="","",IF(ABS(B{0})<=B{1},"Sí","No: revisa el plazo"))'
               .format(F_PENDIENTE, F_TOL)))
    C.nota(ws, 'H%d' % F_CIERRA,
           'Tiene que decir «Sí»: el principal devuelto en el cuadro tiene que '
           'ser el prestado. Si dice que no, el plazo no da para amortizarlo '
           'con esa cuota y queda capital sin devolver al vencimiento.')

    # --- resumen por año ---------------------------------------------------
    C.seccion(ws, 'A%d' % F_SEC_ANIO,
              'RESUMEN POR AÑO Y COBERTURA DEL SERVICIO DE LA DEUDA (DSCR)')
    C.cabecera(ws, F_ANIO_CAB,
               [('A', 'Año'), ('B', 'Intereses (€)'),
                ('C', 'Principal devuelto (€)'), ('D', 'Cuota total (€)'),
                ('E', 'Flujo disponible para la deuda (€)'), ('F', 'DSCR'),
                ('G', ''), ('H', 'Notas')], altura=30)
    for k in range(F_ANIOS):
        fila = F_ANIO_INI + k
        ini = F_MES_INI + k * 12
        fin = ini + 11
        motor.val(ws, 'A%d' % fila, k + 1, fmt=C.ENT, align='center')
        motor.f(ws, 'B%d' % fila, ie('SUM(C%d:C%d)' % (ini, fin)), fmt=C.EUR)
        motor.f(ws, 'C%d' % fila, ie('SUM(D%d:D%d)' % (ini, fin)), fmt=C.EUR)
        motor.f(ws, 'D%d' % fila, ie('B%d+C%d' % (fila, fila)), fmt=C.EUR)
        col_pyg = 'BCD'[k] if k < 3 else 'D'
        motor.f(ws, 'E%d' % fila,
                ie('{0}{1}{2}-{0}{1}{3}+{0}{1}{4}+B{5}'
                   .format(Q_PYG, col_pyg, P['rai'], P['is'],
                           P['amortizacion'], fila)), fmt=C.EUR)
        motor.f(ws, 'F%d' % fila,
                ie('IF(OR(D{0}="",D{0}=0),"",E{0}/D{0})'.format(fila)),
                fmt=C.DEC)
    C.nota(ws, 'H%d' % F_ANIO_INI,
           'El flujo disponible se calcula ANTES de la deuda y DESPUÉS de '
           'impuestos: al resultado antes de impuestos se le resta la cuota '
           'del Impuesto de Sociedades y se le suma la amortización, que no se '
           'paga. Del año 4 en adelante se mantiene el flujo del año 3: este '
           'libro no proyecta más lejos, y decirlo es más honesto que '
           'inventarse un crecimiento.')
    motor.val(ws, 'A%d' % F_DSCR_MIN, 'DSCR mínimo de todo el cuadro',
              bold=True)
    motor.f(ws, 'B%d' % F_DSCR_MIN,
            ie('IF(COUNT(F{0}:F{1})=0,"",MIN(F{0}:F{1}))'
               .format(F_ANIO_INI, F_ANIO_FIN)), fmt=C.DEC, bold=True)
    C.total_fila(ws, F_DSCR_MIN, 'ABCDEFGH')
    motor.val(ws, 'A%d' % F_DSCR_SEM, 'Lectura del DSCR')
    motor.f(ws, 'B%d' % F_DSCR_SEM,
            ie('IF(B{0}="","",IF(B{0}<{1},"Por debajo del mínimo",'
               'IF(B{0}<{2},"Entre el mínimo y el objetivo","En objetivo")))'
               .format(F_DSCR_MIN, sup('dscr_min'), sup('dscr_obj'))))
    motor.semaforo_isnumber(ws, 'B%d:B%d' % (F_DSCR_MIN, F_DSCR_MIN),
                            '$B$%d' % F_DSCR_MIN, operador='<',
                            umbral=sup('dscr_min'))
    C.nota(ws, 'H%d' % F_DSCR_MIN,
           'Es el PEOR año de los que dura el préstamo, no el mejor de los '
           'tres que proyecta el P&L. Es el número que decide la operación.')
    C.parrafo(ws, F_NOTA,
              'El año de carencia infla el DSCR: con sólo intereses en el '
              'denominador el ratio se dispara y no está midiendo el negocio, '
              'está midiendo que todavía no devuelves nada. Mira el año 2 y el '
              'año 3, que es cuando la cuota está completa.', 'A', 'H',
              alto=32)
    ws.freeze_panes = 'A%d' % (F['cab'] + 1)
    C.pagina(ws, titulos='$%d:$%d' % (F['cab'], F['cab']),
             area='A1:H%d' % F_NOTA)
    return ws


# ==========================================================================
# Hoja «Canales y Punto Muerto» (D19: los CINCO canales)
# ==========================================================================
def hoja_canales(wb):
    ws = wb.create_sheet(H_CAN)
    C.anchos(ws, {'A': 40, 'B': 11, 'C': 11, 'D': 11, 'E': 11, 'F': 13,
                  'G': 10, 'H': 13, 'I': 15, 'J': 15, 'K': 14, 'L': 76})
    C.encabezar(ws, 'Canales y punto muerto: qué canal sostiene el negocio',
                'Cinco canales, cada uno con su margen, su coste de servir, su '
                'comisión, su coste de envío y sus días de cobro. La suma no '
                'es lo interesante: lo interesante es qué pasa con el punto '
                'muerto cuando quitas uno, y cuáles de los cinco te sacan de '
                'la nota del epígrafe 644.5 del IAE.', col_fin='L')
    C.cabecera(ws, K_CAB,
               [('A', 'Canal'), ('B', '% de las ventas'),
                ('C', 'Margen bruto (%)'), ('D', 'Coste de servir (%)'),
                ('E', 'Comisión de plataforma (%)'),
                ('F', 'Envío refrigerado (€/pedido)'), ('G', 'Días de cobro'),
                ('H', 'Margen de contribución (%)'),
                ('I', 'Ventas del año de crucero (€)'),
                ('J', 'Margen de contribución (€)'),
                ('K', '¿Te saca de la nota del 644.5?'), ('L', 'Notas')])

    refs, _fila_listas = C.bloque_listas(
        ws, K_LISTAS, [('Respuesta del 644.5',
                        ['Sí', 'No', 'No lo sé'])], col='A')

    for i, c in enumerate(CANALES):
        fila = K_INI + i
        motor.val(ws, 'A%d' % fila, c['canal'], wrap=True)
        C.entrada(ws, 'B%d' % fila, round(c['ventas_pct'] / 100.0, 4),
                  fmt=C.PCT, etiqueta=c['canal'] + ' · % de ventas')
        C.entrada(ws, 'C%d' % fila, c['margen_bruto'], fmt=C.PCT,
                  etiqueta=c['canal'] + ' · margen bruto')
        C.entrada(ws, 'D%d' % fila, c['coste_servir_pct'], fmt=C.PCT,
                  etiqueta=c['canal'] + ' · coste de servir')
        C.entrada(ws, 'E%d' % fila, c['comision_plataforma'], fmt=C.PCT,
                  etiqueta=c['canal'] + ' · comisión de plataforma')
        C.entrada(ws, 'F%d' % fila, c['coste_envio_refrigerado'], fmt=C.EUR,
                  etiqueta=c['canal'] + ' · envío refrigerado')
        C.entrada(ws, 'G%d' % fila, c['cobro_dias'], fmt=C.ENT,
                  etiqueta=c['canal'] + ' · días de cobro', align='center')
        motor.f(ws, 'H%d' % fila, ie('C{0}-D{0}-E{0}'.format(fila)), fmt=C.PCT)
        motor.f(ws, 'I%d' % fila,
                ie('IF({0}$C${1}="","",{0}$C${1}*B{2})'
                   .format(Q_PYG, P['ingresos'], fila)), fmt=C.EUR)
        motor.f(ws, 'J%d' % fila, ie('IF(H{0}="","",I{0}*H{0})'.format(fila)),
                fmt=C.EUR)
        C.entrada(ws, 'K%d' % fila, SALE_644[c['sale_de_la_nota_644_5']],
                  etiqueta=c['canal'] + ' · 644.5', align='center')
        C.nota(ws, 'L%d' % fila, c['nota'])
        ws.row_dimensions[fila].height = 62
    C.dv_rango(ws, ['K%d' % (K_INI + i) for i in range(len(CANALES))],
               refs['Respuesta del 644.5'], 'Responde Sí, No o No lo sé',
               'Elige una de las tres respuestas de la lista del pie de la '
               'hoja.')
    C.nota_celda(ws, 'K%d' % K_INI, 'CHN-72')
    C.comentario(ws, 'F%d' % (K_INI + 1),
                 'SUPUESTO DECLARADO: no hay tarifa pública de envío '
                 'refrigerado de bombonería. Es el número que decide si ese '
                 'canal existe, y por eso está en celda verde y tiene su '
                 'propio bloque al pie de la hoja.')
    C.nota_celda(ws, 'A%d' % K_B2B, 'CHN-41')
    C.nota_celda(ws, 'A%d' % (K_INI + I_CORP), 'CHN-24')
    C.nota_fuente(ws, 'A%d' % K_TAL, 'CHS-30')

    motor.val(ws, 'A%d' % K_TOT, 'TOTAL', bold=True)
    for letra in ('B', 'I', 'J'):
        motor.f(ws, '%s%d' % (letra, K_TOT),
                ie('IF(COUNT({0}{1}:{0}{2})=0,"",SUM({0}{1}:{0}{2}))'
                   .format(letra, K_INI, K_FIN)),
                fmt=(C.PCT if letra == 'B' else C.EUR), bold=True)
    motor.f(ws, 'H%d' % K_TOT, ie('J%d/I%d' % (K_TOT, K_TOT)), fmt=C.PCT,
            bold=True)
    C.total_fila(ws, K_TOT, 'ABCDEFGHIJKL')
    C.nota(ws, 'L%d' % K_TOT,
           'La columna «% de las ventas» tiene que sumar 100 %. Si no suma, '
           'todo lo de abajo está mal.')

    def linea(fila, etiqueta, formula, fmt=None, nota_txt=None, bold=None,
              verde=None, id_chn=None):
        motor.val(ws, 'A%d' % fila, etiqueta, bold=bold, wrap=True)
        if verde is not None:
            C.entrada(ws, 'B%d' % fila, verde, fmt=fmt, etiqueta=etiqueta)
        elif formula is not None:
            motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=bold)
        if id_chn:
            C.nota_celda(ws, 'B%d' % fila, id_chn)
        if nota_txt:
            C.nota(ws, 'L%d' % fila, nota_txt)

    C.banda(ws, K_SEC_PM, 'ABCDEFGHIJKL', 'EL PUNTO MUERTO, CANAL A CANAL')
    linea(K_FIJOS, 'Costes fijos del año de crucero (€)',
          ie('%s$C$%d' % (Q_PYG, P['tot_fijos'])), C.EUR)
    linea(K_FIJOS_MES, 'Costes fijos mensuales (€)',
          ie('B%d/12' % K_FIJOS), C.EUR)
    linea(K_MC, 'Margen de contribución medio ponderado (%)',
          ie('H%d' % K_TOT), C.PCT)
    linea(K_REGLA, 'Margen bruto objetivo de la regla única (%)',
          ie(sup('margen_obj')), C.PCT)
    linea(K_DIF_MC, 'Lo que se llevan servir, cobrar y las comisiones (%)',
          ie('B%d-B%d' % (K_REGLA, K_MC)), C.PCT,
          'La diferencia entre el margen bruto objetivo de la carta y el '
          'margen de contribución real. No es un error de ninguno de los dos: '
          'es lo que cuesta poner el bombón en manos del cliente por cada vía.')
    linea(K_PM_CON, 'Punto muerto mensual CON todos los canales (€)',
          ie('IF(B{0}<=0,"",B{1}/B{0})'.format(K_MC, K_FIJOS_MES)), C.EUR,
          bold=True)
    linea(K_PM_SIN, 'Punto muerto mensual SIN el canal B2B (€)',
          ie('IF(OR(I{0}-I{1}<=0,(J{0}-J{1})/(I{0}-I{1})<=0),"",'
             'B{2}/((J{0}-J{1})/(I{0}-I{1})))'
             .format(K_TOT, K_B2B, K_FIJOS_MES)), C.EUR, bold=True)
    linea(K_PM_DIF, 'Diferencia (€/mes)',
          ie('IF(OR(B{0}="",B{1}=""),"",B{0}-B{1})'
             .format(K_PM_SIN, K_PM_CON)), C.EUR,
          'Si sale NEGATIVA, quitar el B2B te BAJA el punto muerto: ese canal '
          'estaba tirando del margen medio hacia abajo, y lo que aporta es '
          'volumen, no rentabilidad. Ojo, eso no dice que haya que cerrarlo: '
          'dice qué tienes que exigirle. Y en chocolate el B2B tiene un coste '
          'extra que no está en esta fila: es el que te puede meter en el '
          'art. 3 del RD 1021/2022.')
    C.total_fila(ws, K_PM_CON, 'ABCDEFGHIJKL')
    C.total_fila(ws, K_PM_SIN, 'ABCDEFGHIJKL')
    linea(K_SOSTIENE, 'Canal que sostiene el negocio',
          ie('IF(COUNT(J{0}:J{1})=0,"",INDEX($A${0}:$A${1},'
             'MATCH(MAX($J${0}:$J${1}),$J${0}:$J${1},0)))'
             .format(K_INI, K_FIN)), None, bold=True)
    linea(K_APORTE, 'Aporte de ese canal al margen de contribución (%)',
          ie('IF(J{0}="","",MAX($J${1}:$J${2})/J{0})'
             .format(K_TOT, K_INI, K_FIN)), C.PCT,
          'Es el canal que paga el alquiler. Todo lo que pongas en marcha en '
          'los otros cuatro se financia con éste, así que lo primero que hay '
          'que proteger es su margen.')

    C.banda(ws, K_SEC_644, 'ABCDEFGHIJKL',
            'LA NOTA DEL EPÍGRAFE 644.5: QUÉ CANALES TE SACAN DE ELLA')
    linea(K_FUERA, 'Canales que hay que consultar con tu asesor',
          ie('COUNTIF(K%d:K%d,"No lo sé")' % (K_INI, K_FIN)), C.ENT,
          'La nota del epígrafe 644.5 faculta para «la fabricación de bombones '
          'y caramelos en el propio establecimiento, siempre que su '
          'comercialización se realice en las propias dependencias de venta». '
          'El mostrador y el taller no la rompen; el online, el B2B y el '
          'corporativo comercializan FUERA de tus dependencias, y ésa es la '
          'pregunta. Esta hoja NO emite un epígrafe de IAE por canal, y no es '
          'un olvido: ninguna fuente lo da.', id_chn='CHN-72')
    motor.val(ws, 'A%d' % K_PREGUNTA, 'La pregunta, redactada para el asesor',
              wrap=True)
    motor.val(ws, 'B%d' % K_PREGUNTA, D.PREGUNTA_AL_ASESOR, wrap=True)
    ws.merge_cells('B%d:L%d' % (K_PREGUNTA, K_PREGUNTA))
    ws.row_dimensions[K_PREGUNTA].height = 60
    C.nota_celda(ws, 'B%d' % K_PREGUNTA, 'CHN-94',
                 'Regla 4.a.1: el pago de la cuota de una actividad faculta '
                 'exclusivamente para el ejercicio de ESA actividad. Y la '
                 'regla 4.a.2.D) define el comercio al por menor por el '
                 'DESTINO y comprende el realizado sin establecimiento, así '
                 'que la venta online al consumidor SÍ es minorista.')

    # B5 (refutación 2026-09-12): esta hoja calculaba «la vía a) del art.
    # 3.2» con una base distinta a la del libro 8 -euros de TODO el canal
    # B2B (hostelería incluida) contra volumen SÓLO de minoristas de
    # distinta titularidad- y publicaba un segundo número (11 %) que
    # contradecía al del libro 8 (14 %) para el mismo test legal. Ahora sólo
    # queda el dato informativo (cuánto pesa el B2B en la cuenta) y el
    # puntero al libro que de verdad resuelve el art. 3, sin repetir su
    # cálculo con una base distinta.
    C.banda(ws, K_SEC_ART3, 'ABCDEFGHIJKL',
            'EL AVISO DEL ART. 3: CUÁNDO EL B2B TE CAMBIA DE RÉGIMEN')
    linea(K_PESO_B2B, 'Peso del canal B2B sobre las ventas, en euros '
          '(referencia; NO es el test del art. 3)',
          ie('B%d' % K_B2B), C.PCT)
    motor.val(ws, 'A%d' % K_UMBRAL,
              'La vía a) del art. 3.2 se mide en VOLUMEN (kg), no en euros, y '
              'sólo cuenta a los minoristas de distinta titularidad -no toda '
              'hostelería ni el regalo corporativo-. Se resuelve en '
              '«checklist-legal-licencias-y-cacao.xlsx», hoja «Suministro a '
              'Otros Minoristas».', wrap=True)
    ws.merge_cells('A%d:L%d' % (K_UMBRAL, K_UMBRAL))
    ws.row_dimensions[K_UMBRAL].height = 40
    motor.val(ws, 'A%d' % K_VEREDICTO,
              'La vía a) del art. 3.2 se resuelve en '
              'checklist-legal-licencias-y-cacao.xlsx!Suministro a Otros '
              'Minoristas!B26', bold=True, wrap=True)
    ws.merge_cells('A%d:L%d' % (K_VEREDICTO, K_VEREDICTO))
    C.destacado(ws, 'A%d' % K_VEREDICTO)
    C.parrafo(ws, K_VEREDICTO + 1,
              'El art. 3 del RD 1021/2022 sólo se activa si suministras a '
              'establecimientos minoristas de DISTINTA titularidad. Si entras, '
              'hay que presentar declaración responsable y llevar registro de '
              'destinatarios, cantidades y fechas. Este aviso mira sólo el '
              'porcentaje EN EUROS del B2B, como referencia de negocio; el '
              'árbol legal completo -con el test en volumen- está en el libro '
              '«checklist-legal-licencias-y-cacao».', 'A', 'L', alto=48)

    linea(K_COBRO, 'Días medios de cobro ponderados', ie(sup('dias_cobro')),
          C.DEC1,
          'Es el número que usa la hoja de Tesorería para desfasar los cobros. '
          'Sube solo en cuanto crecen el B2B y el corporativo, y ése es su '
          'coste oculto: no es sólo que dejen menos margen, es que lo dejan '
          'más tarde -y el corporativo lo deja en enero, no en diciembre-.')

    C.banda(ws, K_SEC_ENVIO, 'ABCDEFGHIJKL',
            'EL ENVÍO REFRIGERADO: EL NÚMERO QUE DECIDE SI EL CANAL ONLINE '
            'EXISTE')
    linea(K_PEDIDO, 'Pedido medio del canal online (€ sin IVA)', None, C.EUR,
          'SUPUESTO, y es el pedido MÍNIMO del caso. Si tu pedido medio baja '
          'de aquí, el envío se come el canal: no es que gane menos, es que '
          'trabajas para el transportista.',
          verde=round(CANALES[1]['pedido_minimo'], 2))
    linea(K_ENVIO_PCT, 'Coste del envío sobre el pedido medio (%)',
          ie('IF(B{0}<=0,"",F{1}/B{0})'.format(K_PEDIDO, K_INI + 1)), C.PCT)
    linea(K_MC_ENVIO,
          'Margen de contribución del online DESPUÉS del envío (%)',
          ie('IF(B{0}="","",H{1}-B{0})'.format(K_ENVIO_PCT, K_INI + 1)),
          C.PCT, bold=True)
    motor.semaforo_isnumber(ws, 'B%d:B%d' % (K_MC_ENVIO, K_MC_ENVIO),
                            '$B$%d' % K_MC_ENVIO, operador='<', umbral='0')
    linea(K_VER_ENVIO, 'VEREDICTO DEL CANAL ONLINE',
          ie('IF(B{0}="","",IF(B{0}<=0,"El envío se come el canal: sube el '
             'pedido mínimo o cierra el online",IF(B{0}<B{1},"Aguanta, pero '
             'deja menos que el mostrador: úsalo para llegar donde no llegas, '
             'no para sustituirlo","Aguanta bien")))'
             .format(K_MC_ENVIO, K_MC)), None, bold=True)
    C.destacado(ws, 'B%d' % K_VER_ENVIO)
    C.nota(ws, 'L%d' % K_VER_ENVIO,
           'Y hay una cosa que no se ve en el margen: los envíos de este caso '
           'PARAN de junio a septiembre. El chocolate no viaja en verano sin '
           'cadena de frío, y eso no es un problema de coste, es de calendario.')

    C.parrafo(ws, K_NOTA,
              'Los porcentajes de esta hoja son SUPUESTOS: no existe reparto '
              'publicado por canal de una bombonería española. Son una '
              'hipótesis de trabajo coherente con el caso -mostrador '
              'mayoritario, online pequeño y parado en verano, B2B y '
              'corporativo con cobro aplazado y taller pequeño pero con el '
              'mejor margen-, y lo primero que hay que sustituir por tus '
              'propios datos del TPV en cuanto tengas tres meses.', 'A', 'L',
              alto=46)
    ws.freeze_panes = 'A%d' % (K_CAB + 1)
    C.pagina(ws, titulos='$%d:$%d' % (K_CAB, K_CAB), area='A1:L%d' % K_NOTA)
    return ws


# ==========================================================================
# Hoja «Talleres y Regalo Corporativo» (D7: absorbe el libro descartado)
# ==========================================================================
def hoja_talleres(wb):
    ws = wb.create_sheet(H_TAL)
    C.anchos(ws, {'A': 56, 'B': 16, 'C': 16, 'D': 88})
    C.encabezar(ws, 'Talleres y regalo corporativo: las dos líneas que no '
                    'dependen del cacao',
                'El taller es la única línea que funciona en agosto y a la que '
                'no le afecta el precio de la cobertura. Y el regalo '
                'corporativo es el que llena diciembre, pero cobra en enero. '
                'Esta hoja dice cuántos asistentes necesita un taller para '
                'cubrirse y qué deja una hora de sala dando taller frente a la '
                'misma hora vendiendo.', col_fin='D')

    def ent(clave, etiqueta, valor, fmt, unidad, nota_txt, id_chs=None,
            id_chn=None):
        fila = W[clave]
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
        C.entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
        motor.val(ws, 'C%d' % fila, unidad)
        C.nota(ws, 'D%d' % fila, nota_txt)
        if id_chs:
            C.nota_fuente(ws, 'B%d' % fila, id_chs)
        if id_chn:
            C.nota_celda(ws, 'B%d' % fila, id_chn)
        return 'B%d' % fila

    def fx(clave, etiqueta, formula, fmt, unidad='', nota_txt=None,
           bold=None):
        fila = W[clave]
        motor.val(ws, 'A%d' % fila, etiqueta, bold=bold, wrap=True)
        motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=bold)
        if unidad:
            motor.val(ws, 'C%d' % fila, unidad)
        if nota_txt:
            C.nota(ws, 'D%d' % fila, nota_txt)
        return 'B%d' % fila

    # --- el taller ---------------------------------------------------------
    C.banda(ws, W['sec_taller'], 'ABCD',
            'EL TALLER: CUÁNTOS ASISTENTES HACEN FALTA PARA QUE SE PAGUE SOLO')
    ent('precio_min', 'Precio por persona, mínimo del rango publicado',
        TALLER['precio_persona_min'], C.EUR, '€/persona',
        'Dato de mercado: los talleres y catas de bombonería se mueven entre '
        '25 y 45 € por persona, con un mínimo habitual de 6 personas y una '
        'duración de 90 a 150 minutos. Se publica el RANGO, y el libro trabaja '
        'con el mínimo.', id_chs='CHS-30')
    ent('precio_max', 'Precio por persona, máximo del rango publicado',
        TALLER['precio_persona_max'], C.EUR, '€/persona',
        'El techo del mismo rango. Cobrar el techo exige otra cosa: cata '
        'guiada, orígenes, material para llevarse a casa.', id_chs='CHS-30')
    ent('precio', 'Precio por persona que vas a cobrar',
        TALLER['precio_persona_min'], C.EUR, '€/persona',
        'Sembrado con el MÍNIMO a propósito: si el taller se paga solo al '
        'precio más bajo del rango, se paga solo. Súbelo cuando tengas la '
        'sala llena dos sábados seguidos.')
    ent('aforo', 'Aforo del taller', TALLER['aforo'], C.ENT, 'personas',
        'SUPUESTO: doce personas es lo que cabe alrededor de una mesa de '
        'mármol sin que nadie tenga que mirar por encima de otro. Tu aforo lo '
        'manda tu sala, no este número.')
    ent('minimo', 'Mínimo de personas para hacerlo',
        TALLER['minimo_personas'], C.ENT, 'personas',
        'El mínimo habitual del mercado. Por debajo de este número, el taller '
        'se pospone: no es tacañería, es que el docente cuesta lo mismo con '
        'tres que con doce.', id_chs='CHS-30')
    ent('dur_min', 'Duración mínima publicada', TALLER['duracion_min_minutos'],
        C.ENT, 'minutos', 'Rango publicado de mercado.', id_chs='CHS-30')
    ent('dur_max', 'Duración máxima publicada', TALLER['duracion_max_minutos'],
        C.ENT, 'minutos', 'Rango publicado de mercado.', id_chs='CHS-30')
    ent('horas_doc', 'Horas de docente por taller',
        TALLER['horas_docente'], C.DEC1, 'horas',
        'SUPUESTO: la sesión más la preparación y la recogida. El error clásico '
        'es contar sólo los 90 minutos de cara al público: montar y desmontar '
        'un taller de templado se lleva casi otro tanto.')
    fx('coste_hora', 'Coste de una hora de obrador (€)',
       ie('%s$B$%d' % (Q_PER, R_HORA_OBR)), C.EUR, '€/hora',
       'Sale de la hoja de Personal: coste empresa del área de obrador entre '
       'sus horas productivas. El docente no es gratis aunque seas tú: tu hora '
       'dando taller es una hora que no estás templando.')
    fx('coste_doc', 'Coste del docente por taller (€)',
       ie('B%d*B%d' % (W['horas_doc'], W['coste_hora'])), C.EUR, '€/taller')
    ent('materia', 'Coste de materia y material por asistente (€)', 3.50,
        C.EUR, '€/persona',
        'SUPUESTO: cobertura para templar, moldes de un uso, caja para '
        'llevarse lo que ha hecho y delantal. Es lo que convierte un taller en '
        'un recuerdo, y por eso no se recorta.')
    fx('servir', 'Coste de servir el canal de talleres (%)',
       ie('%sD%d' % (Q_CAN, K_TAL)), C.PCT, '',
       'Sale de la hoja de canales: reservas, pasarela de cobro y las horas de '
       'tienda que se van en atender la inscripción.')
    fx('neto_persona', 'Ingreso neto por asistente (€)',
       ie('B%d*(1-B%d)' % (W['precio'], W['servir'])), C.EUR, '€/persona')
    fx('asistentes_pm',
       'ASISTENTES NECESARIOS PARA CUBRIR EL PUNTO MUERTO DEL TALLER',
       ie('IF(B%d<=0,"",B%d/B%d)'
          % (W['neto_persona'], W['coste_doc'], W['neto_persona'])), C.DEC1,
       'personas', bold=True,
       nota_txt='Sólo contra el coste del DOCENTE, que es el criterio más '
                'conservador y el que se puede defender: es el coste que '
                'existe aunque no venga nadie. Es el número que decide si '
                'abres el calendario de talleres.')
    C.total_fila(ws, W['asistentes_pm'], 'ABCD')
    fx('asistentes_pm_mat',
       'Asistentes necesarios contando también la materia y el material',
       ie('IF(B%d-B%d<=0,"",B%d/(B%d-B%d))'
          % (W['neto_persona'], W['materia'], W['coste_doc'],
             W['neto_persona'], W['materia'])), C.DEC1, 'personas',
       nota_txt='El mismo cálculo con el material dentro. La diferencia entre '
                'los dos números es lo que te puedes permitir regalar en una '
                'primera edición para llenar la sala.')
    fx('veredicto_pm', 'LECTURA FRENTE AL MÍNIMO DE PERSONAS',
       ie('IF(B{0}="","",IF(B{0}<=B{1},"El mínimo habitual de mercado ya cubre '
          'el taller: el resto es margen","Con el mínimo de mercado NO se '
          'cubre: sube el precio o baja el coste de docente"))'
          .format(W['asistentes_pm_mat'], W['minimo'])), None, bold=True)
    C.destacado(ws, 'B%d' % W['veredicto_pm'])

    # --- euros por hora de sala -------------------------------------------
    C.banda(ws, W['sec_sala'], 'ABCD',
            'LA PREGUNTA DE VERDAD: €/HORA DE SALA DANDO TALLER FRENTE A '
            '€/HORA VENDIENDO')
    fx('horas_sala', 'Horas que la sala está ocupada por el taller',
       ie('B%d' % W['horas_doc']), C.DEC1, 'horas',
       'Las mismas del docente: mientras montas, das y recoges, esa sala no '
       'vende. Si tu taller es fuera del horario de tienda, pon aquí las horas '
       'que de verdad solapan.')
    fx('ingreso_lleno', 'Ingreso del taller a aforo completo (€)',
       ie('B%d*B%d' % (W['aforo'], W['precio'])), C.EUR, '€/taller')
    fx('hora_taller', 'Margen por hora de sala DANDO TALLER (€/hora)',
       ie('IF(B{0}<=0,"",(B{1}-B{2}*B{3}-B{4})/B{0})'
          .format(W['horas_sala'], W['ingreso_lleno'], W['materia'],
                  W['aforo'], W['coste_doc'])), C.EUR, '€/hora', bold=True)
    fx('ventas_most', 'Ventas de mostrador del año de crucero (€)',
       ie('%sI%d' % (Q_CAN, K_MOST)), C.EUR, '€/año')
    ent('horas_anio', 'Horas de tienda abierta al año',
        float(D.NEGOCIO['dias_apertura_anio'] * 10), C.ENT, 'horas/año',
        'SUPUESTO: los días de apertura del año por diez horas de persiana '
        'levantada. Cámbialo por tu horario real, que es lo que hace que esta '
        'comparación signifique algo.')
    fx('hora_vendiendo', 'Margen por hora de sala VENDIENDO (€/hora)',
       ie('IF(B{0}<=0,"",B{1}*{2}H{3}/B{0})'
          .format(W['horas_anio'], W['ventas_most'], Q_CAN, K_MOST)), C.EUR,
       '€/hora', bold=True,
       nota_txt='Margen de contribución del mostrador repartido entre las '
                'horas que la tienda está abierta. Es la comparación honesta: '
                'margen contra margen, hora contra hora.')
    fx('dif', 'Diferencia a favor del taller (€/hora)',
       ie('IF(OR(B%d="",B%d=""),"",B%d-B%d)'
          % (W['hora_taller'], W['hora_vendiendo'], W['hora_taller'],
             W['hora_vendiendo'])), C.EUR, '€/hora')
    motor.semaforo_isnumber(ws, 'B%d:B%d' % (W['dif'], W['dif']),
                            '$B$%d' % W['dif'], operador='<', umbral='0')
    fx('veredicto_sala', 'VEREDICTO DE LA HORA DE SALA',
       ie('IF(B{0}="","",IF(B{0}>0,"La hora de taller deja más que la hora '
          'vendiendo: el calendario de talleres se defiende solo","La hora de '
          'taller deja MENOS que vender: hazlos fuera del horario de tienda o '
          'en agosto, cuando esa hora no vende"))'.format(W['dif'])), None,
       bold=True)
    C.destacado(ws, 'B%d' % W['veredicto_sala'])

    # --- volumen -----------------------------------------------------------
    C.banda(ws, W['sec_volumen'], 'ABCD',
            'CUÁNTOS TALLERES HACEN EL 6 % DE VENTAS QUE DICE LA HOJA DE '
            'CANALES')
    ent('talleres_mes', 'Talleres al mes', 4, C.ENT, 'talleres/mes',
        'SUPUESTO: uno por semana, normalmente en sábado. En agosto es la '
        'única línea que sigue funcionando.')
    ent('asistentes_medios', 'Asistentes medios por taller', 8, C.ENT,
        'personas',
        'SUPUESTO: dos tercios del aforo. Llenar los doce todas las semanas es '
        'una previsión, no un supuesto.')
    fx('ingresos_anio', 'Ingresos de talleres al año (€)',
       ie('B%d*12*B%d*B%d' % (W['talleres_mes'], W['asistentes_medios'],
                              W['precio'])), C.EUR, '€/año', bold=True)
    fx('canal_anio', 'Ventas del canal «talleres» según la hoja de canales (€)',
       ie('%sI%d' % (Q_CAN, K_TAL)), C.EUR, '€/año')
    fx('dif_canal', 'Diferencia entre las dos (€)',
       ie('IF(OR(B%d="",B%d=""),"",B%d-B%d)'
          % (W['ingresos_anio'], W['canal_anio'], W['ingresos_anio'],
             W['canal_anio'])), C.EUR, '€/año')
    fx('veredicto_vol', 'LECTURA',
       ie('IF(B{0}="","",IF(ABS(B{0})<B{1},"Cuadra: el calendario de talleres '
          'sostiene el peso que le da la hoja de canales","No cuadra: o haces '
          'más talleres, o llenas más, o baja el peso del canal en la hoja de '
          'canales"))'.format(W['dif_canal'], W['canal_anio'])), None,
       bold=True)
    C.destacado(ws, 'B%d' % W['veredicto_vol'])
    C.nota(ws, 'D%d' % W['veredicto_vol'],
           'Es un CUADRE interno de este libro, no un cruce con otro fichero: '
           'sirve para que el 6 % de ventas que le da la hoja de canales al '
           'taller no sea un número puesto a ojo, sino algo que cabe en un '
           'calendario de verdad.')

    # --- IVA del taller ----------------------------------------------------
    C.banda(ws, W['sec_iva'], 'ABCD', 'EL IVA DEL TALLER')
    fx('iva', 'Tipo de IVA que vas a aplicar al taller',
       ie(sup('iva_taller')), None, '',
       'Viene de «0. Supuestos», y VA SIN CIFRA a propósito.')
    C.nota_celda(ws, 'B%d' % W['iva'], 'CHN-71b')
    C.parrafo(ws, W['nota_iva'],
              'Lo que SÍ está cerrado: un taller de bombonería NO está exento '
              'de IVA. El art. 20.Uno.10.º de la Ley del IVA excluye de la '
              'exención de la enseñanza las clases «para cuya realización sea '
              'necesario darse de alta en las tarifas de actividades '
              'empresariales o artísticas del IAE», que es exactamente tu '
              'caso. Lo que NO está cerrado es el TIPO: el art. 91 no nombra '
              'los talleres, y esta guía no publica una cifra que no pueda '
              'sostener. Y ojo, que son dos preguntas distintas: el taller no '
              'rompe la nota del epígrafe 644.5 -no comercializas bombones '
              'fuera de tus dependencias-, pero sí abre la pregunta de si hay '
              'que darse de alta por esta actividad, que es un alta distinta.',
              'A', 'D', alto=76)

    # --- regalo corporativo -----------------------------------------------
    C.banda(ws, W['sec_corp'], 'ABCD',
            'EL REGALO CORPORATIVO: LLENA DICIEMBRE Y COBRA EN ENERO')
    corp = CANALES[I_CORP]
    ent('pedido_min', 'Pedido mínimo que aceptas (€ sin IVA)',
        corp['pedido_minimo'], C.EUR, '€/pedido',
        'SUPUESTO. Por debajo de un mínimo, un pedido de empresa cuesta más en '
        'muestras, llamadas y personalización de lo que deja.')
    ent('cobro_dias', 'Días de cobro del canal corporativo',
        corp['cobro_dias'], C.ENT, 'días',
        'SUPUESTO: 30 días. Lo que significa de verdad es que la caja de '
        'diciembre entra en enero, justo después de haber pagado la cobertura '
        'en octubre y las extras en diciembre.')
    ent('plazo_muestra', 'Plazo mínimo desde que aprueban la muestra',
        14, C.ENT, 'días',
        'DATO DE MERCADO VERIFICADO: catorce días desde la aprobación de la '
        'muestra, con mínimos de fabricación de 10 a 25 cajas. Es lo que '
        'decide si aceptas un pedido de empresa el 15 de diciembre: la '
        'respuesta casi siempre es que no.', id_chs='CHS-55')
    ent('cajas_min', 'Mínimo de fabricación, suelo del rango', 10, C.ENT,
        'cajas', 'Rango publicado de mercado.', id_chs='CHS-55')
    ent('cajas_max', 'Mínimo de fabricación, techo del rango', 25, C.ENT,
        'cajas', 'Rango publicado de mercado.', id_chs='CHS-55')
    ent('pedidos_anio', 'Pedidos corporativos al año', 40, C.ENT,
        'pedidos/año',
        'SUPUESTO. La mayoría se concentran en noviembre y diciembre, y por '
        'eso la agenda se cierra en octubre.')
    fx('facturacion', 'Facturación del canal corporativo (€/año)',
       ie('B%d*B%d' % (W['pedidos_anio'], W['pedido_min'])), C.EUR, '€/año')
    fx('margen', 'Margen de contribución que deja (€/año)',
       ie('B%d*%sH%d' % (W['facturacion'], Q_CAN, K_INI + I_CORP)), C.EUR,
       '€/año')
    fx('circulante', 'Caja inmovilizada por el aplazamiento (€)',
       ie('B%d*B%d/365' % (W['facturacion'], W['cobro_dias'])), C.EUR, '€',
       nota_txt='Lo que tienes prestado a tus clientes de empresa en todo '
                'momento. No es un gasto, pero es dinero que no está en tu '
                'cuenta, y en diciembre es justo cuando hace falta.')
    fx('coste_fin', 'Lo que cuesta financiar esa caja (€/año)',
       ie('B%d*%s' % (W['circulante'], sup('tipo'))), C.EUR, '€/año',
       nota_txt='Al mismo tipo que tu préstamo. Es pequeño comparado con el '
                'margen del canal, y aun así conviene verlo escrito: financiar '
                'a un cliente no es gratis.')
    fx('cierre_agenda', 'FECHA LÍMITE PARA ACEPTAR UN PEDIDO CORPORATIVO',
       ie('IF({0}$B${1}="","",{0}$B${1}-B{2})'
          .format(Q_TES, T['limite'], W['plazo_muestra'])), C.FECHA, '',
       bold=True,
       nota_txt='La fecha límite de cierre de pedidos de Navidad que calcula '
                'la hoja de Tesorería, MENOS los catorce días que van desde '
                'que el cliente aprueba la muestra hasta que puedes servir. '
                'Los dos plazos se suman, y por eso la agenda corporativa se '
                'cierra antes que la de particulares.')
    C.total_fila(ws, W['cierre_agenda'], 'ABCD')
    fx('veredicto_corp', 'LECTURA DEL CANAL CORPORATIVO',
       ie('IF(B{0}="","",IF(MONTH(B{0})<=10,"Tienes que cerrar la agenda '
          'corporativa en octubre o antes: septiembre es el mes de llamar",'
          '"Llegas a noviembre, pero vas justo: una muestra rechazada te deja '
          'sin el pedido"))'.format(W['cierre_agenda'])), None, bold=True)
    C.destacado(ws, 'B%d' % W['veredicto_corp'])

    C.parrafo(ws, W['nota'],
              'Las dos líneas de esta hoja tienen algo en común y conviene '
              'decirlo: NO dependen del precio del cacao. El taller vende '
              'tiempo y experiencia, y el corporativo vende un encargo cerrado '
              'con precio pactado. Por eso son las dos que sostienen un año en '
              'el que la cobertura suba un 40 %, y por eso el taller es lo '
              'único que funciona en agosto, cuando el obrador está parado y '
              'la tienda vive del turista. Lo que no son es un plan B: son dos '
              'canales con su propio coste de personal y su propio '
              'calendario.', 'A', 'D', alto=62)
    C.pagina(ws, apaisado=False, area='A1:D%d' % W['nota'])
    return ws


# ==========================================================================
# Mapa de celdas citables
# ==========================================================================
def mapa():
    m = [
        # --- supuestos ----------------------------------------------------
        ('Clientes al día en velocidad de crucero', H_SUP,
         'B%d' % S['tickets'], 'entrada'),
        ('Piezas por ticket', H_SUP, 'B%d' % S['piezas'], 'entrada'),
        ('PVP medio ponderado de la carta con IVA', H_SUP,
         'B%d' % S['pvp'], 'entrada'),
        ('Ticket medio con IVA', H_SUP, 'B%d' % S['ticket_iva'], 'salida'),
        ('Ticket medio sin IVA', H_SUP, 'B%d' % S['ticket_sin'], 'salida'),
        ('Días de apertura al año', H_SUP, 'B%d' % S['dias'], 'entrada'),
        ('Actividad del año 1 sobre la de crucero', H_SUP,
         'B%d' % S['factor_a1'], 'salida'),
        ('IVA del chocolate', H_SUP, 'B%d' % S['iva_prod'], 'parametro'),
        ('IVA del taller (sin cifra a propósito)', H_SUP,
         'B%d' % S['iva_taller'], 'parametro'),
        ('Food cost de escandallo de la carta', H_SUP,
         'B%d' % S['fc_escandallo'], 'entrada'),
        ('Food cost del P&L (escandallo + packaging)', H_SUP,
         'B%d' % S['food_cost'], 'salida'),
        ('Food cost objetivo de la casa (regla única)', H_SUP,
         'B%d' % S['fc_objetivo'], 'entrada'),
        ('Margen bruto objetivo (derivado)', H_SUP,
         'B%d' % S['margen_obj'], 'salida'),
        ('Meses de colchón del fondo de maniobra', H_SUP,
         'B%d' % S['colchon'], 'entrada'),
        ('Préstamo bancario solicitado', H_SUP, 'B%d' % S['principal'],
         'entrada'),
        ('Recursos propios aportados', H_SUP, 'B%d' % S['propios'],
         'entrada'),
        ('Días medios de cobro ponderados', H_SUP, 'B%d' % S['dias_cobro'],
         'salida'),

        # --- inversión y los dos cruces del fondo -------------------------
        ('CAPEX sin el fondo de maniobra (traído del libro 2)', H_INV,
         'B%d' % IV['capex_trae'], 'entrada'),
        ('CUADRE del CAPEX con el libro 2', H_INV,
         'B%d' % IV['capex_cuadre'], 'salida'),
        ('Gastos fijos mensuales del año de crucero', H_INV,
         'B%d' % IV['fijos_mes'], 'salida'),
        ('Fondo de maniobra', H_INV, 'B%d' % IV['fondo'], 'salida'),
        ('Inversión total', H_INV, 'B%d' % IV['total'], 'salida'),
        ('IVA soportado de la inversión', H_INV, 'B%d' % IV['iva'], 'salida'),
        ('Necesidad total de caja al arranque', H_INV,
         'B%d' % IV['necesidad'], 'salida'),
        ('Amortización anual del inmovilizado', H_INV, 'B%d' % IV['amort'],
         'salida'),

        # --- P&L -----------------------------------------------------------
        ('Ingresos del año 1', H_PYG, 'B%d' % P['ingresos'], 'salida'),
        ('Ingresos del año de crucero', H_PYG, 'C%d' % P['ingresos'],
         'salida'),
        ('Ingresos del año 3', H_PYG, 'D%d' % P['ingresos'], 'salida'),
        ('Coste de ventas del año de crucero', H_PYG,
         'C%d' % P['coste_ventas'], 'salida'),
        ('Margen bruto del año de crucero', H_PYG, 'C%d' % P['margen'],
         'salida'),
        ('Coste de personal del año de crucero', H_PYG, 'C%d' % P['personal'],
         'salida'),
        ('Total costes fijos del año de crucero', H_PYG,
         'C%d' % P['tot_fijos'], 'salida'),
        ('Resultado antes de impuestos del año de crucero', H_PYG,
         'C%d' % P['rai'], 'salida'),
        ('Resultado neto del año de crucero', H_PYG, 'C%d' % P['neto'],
         'salida'),
        ('Margen neto del año de crucero', H_PYG, 'E%d' % P['neto'],
         'salida'),
        ('Coste de personal sobre ventas', H_PYG, 'C%d' % P['r_personal'],
         'salida'),
        ('Ventas del formato con taza y churros', H_PYG,
         'C%d' % P['f_ventas'], 'salida'),
        ('Margen neto del formato con taza y churros', H_PYG,
         'C%d' % P['f_mneto'], 'salida'),
        ('VEREDICTO del escenario de formato', H_PYG,
         'B%d' % P['f_veredicto'], 'salida'),
        ('Precio de la cobertura en base imponible (traído del libro 3)',
         H_PYG, 'B%d' % P['cob_trae'], 'entrada'),
        ('CUADRE de la cobertura con el libro 3', H_PYG,
         'B%d' % P['cob_cuadre'], 'salida'),
        ('Peso de la cobertura sobre el coste de ventas', H_PYG,
         'B%d' % P['cob_peso'], 'salida'),
        ('Lo que costaría al año una subida del cacao del 40 %', H_PYG,
         'B%d' % P['cob_impacto'], 'salida'),
        ('Margen neto del año de crucero tras esa subida', H_PYG,
         'B%d' % P['cob_neto'], 'salida'),

        # --- punto de equilibrio ------------------------------------------
        ('Clientes al día para el equilibrio contable (crucero)', H_PEQ,
         'C%d' % E['tk_dia'], 'salida'),
        ('Clientes al día para el equilibrio de caja (crucero)', H_PEQ,
         'C%d' % E['tkc_dia'], 'salida'),
        ('Ingresos necesarios al mes para el equilibrio contable', H_PEQ,
         'C%d' % E['ing_mes'], 'salida'),
        ('Holgura sobre el equilibrio de caja (crucero)', H_PEQ,
         'C%d' % E['holgura'], 'salida'),
        ('Punto muerto mensual de la bombonería', H_PEQ,
         'B%d' % E['pm_mes'], 'salida'),
        ('Punto muerto mensual con taza y churros', H_PEQ,
         'C%d' % E['pm_mes'], 'salida'),

        # --- escenarios ----------------------------------------------------
        ('Resultado neto del escenario pesimista', H_ESC, 'B%d' % X['neto'],
         'salida'),
        ('Resultado neto del escenario optimista', H_ESC, 'D%d' % X['neto'],
         'salida'),

        # --- personal ------------------------------------------------------
        ('Coste de personal al año', H_PER, 'I%d' % R_TOT, 'salida'),
        ('Jornadas completas equivalentes', H_PER, 'B%d' % R_JORNADAS,
         'salida'),
        ('Coste de una hora de obrador', H_PER, 'B%d' % R_HORA_OBR, 'salida'),

        # --- tesorería y la fecha de Navidad ------------------------------
        ('Saldo mínimo de caja del año 1', H_TES, 'B%d' % T['saldo_min'],
         'salida'),
        ('Mes en el que la caja toca fondo', H_TES, 'B%d' % T['mes_fondo'],
         'salida'),
        ('Saldo de caja al cierre del mes 12', H_TES, 'M%d' % T['saldo'],
         'salida'),
        ('Payback del proyecto', H_TES, 'B%d' % T['payback'], 'salida'),
        ('Capacidad diaria del obrador traída del libro 1', H_TES,
         'B%d' % T['cap_trae'], 'entrada'),
        ('CUADRE de la capacidad con el libro 1', H_TES,
         'B%d' % T['cap_cuadre'], 'salida'),
        ('Excedente diario para adelantar producción', H_TES,
         'B%d' % T['excedente'], 'salida'),
        ('Días de calendario de antelación de la campaña de Navidad', H_TES,
         'B%d' % T['dias_nat'], 'salida'),
        ('FECHA LÍMITE de cierre de pedidos de Navidad', H_TES,
         'B%d' % T['limite'], 'salida'),
        ('Mes en el que cae la fecha límite de Navidad', H_TES,
         'B%d' % T['mes_limite'], 'salida'),

        # --- financiación ---------------------------------------------------
        ('Cuota mensual del préstamo', H_FIN, 'B%d' % F['cuota'], 'salida'),
        ('Diferencia entre origen de fondos y necesidad', H_FIN,
         'B%d' % F['diferencia'], 'salida'),
        ('DSCR mínimo de todo el cuadro', H_FIN, 'B%d' % F_DSCR_MIN,
         'salida'),
        ('Intereses del año de crucero', H_FIN, 'B%d' % (F_ANIO_INI + 1),
         'salida'),
        ('¿Cierra el cuadro de amortización?', H_FIN, 'B%d' % F_CIERRA,
         'salida'),

        # --- canales --------------------------------------------------------
        ('Margen de contribución medio ponderado', H_CAN, 'B%d' % K_MC,
         'salida'),
        ('Punto muerto mensual con todos los canales', H_CAN,
         'B%d' % K_PM_CON, 'salida'),
        ('Punto muerto mensual sin el canal B2B', H_CAN, 'B%d' % K_PM_SIN,
         'salida'),
        ('Canal que sostiene el negocio', H_CAN, 'B%d' % K_SOSTIENE,
         'salida'),
        ('Canales que hay que consultar por la nota del 644.5', H_CAN,
         'B%d' % K_FUERA, 'salida'),
        ('Margen de contribución del online después del envío', H_CAN,
         'B%d' % K_MC_ENVIO, 'salida'),
        ('VEREDICTO del canal online', H_CAN, 'B%d' % K_VER_ENVIO, 'salida'),

        # --- talleres y corporativo ----------------------------------------
        ('Asistentes necesarios para cubrir el punto muerto del taller',
         H_TAL, 'B%d' % W['asistentes_pm'], 'salida'),
        ('Asistentes necesarios contando la materia', H_TAL,
         'B%d' % W['asistentes_pm_mat'], 'salida'),
        ('Margen por hora de sala dando taller', H_TAL,
         'B%d' % W['hora_taller'], 'salida'),
        ('Margen por hora de sala vendiendo', H_TAL,
         'B%d' % W['hora_vendiendo'], 'salida'),
        ('VEREDICTO de la hora de sala', H_TAL, 'B%d' % W['veredicto_sala'],
         'salida'),
        ('Ingresos de talleres al año', H_TAL, 'B%d' % W['ingresos_anio'],
         'salida'),
        ('Facturación del canal corporativo', H_TAL, 'B%d' % W['facturacion'],
         'salida'),
        ('Caja inmovilizada por el aplazamiento corporativo', H_TAL,
         'B%d' % W['circulante'], 'salida'),
        ('FECHA LÍMITE para aceptar un pedido corporativo', H_TAL,
         'B%d' % W['cierre_agenda'], 'salida'),
    ]
    return m


NOTAS_MAPA = (
    'Libro 7, HÍBRIDO: molde `planes-v2_0` motor 2.2 más las dos hojas propias '
    'de esta guía («Canales y Punto Muerto» y «Talleres y Regalo '
    'Corporativo»). Manda la línea de versión de la familia de GUÍAS (1.0 · '
    'septiembre 2026). Es la FUENTE ÚNICA de las cifras financieras del texto: '
    'ningún euro del capítulo financiero se escribe fuera de aquí, y el AÑO 2 '
    'es el año de crucero. LAS DOS CELDAS QUE CITA EL RESTO DEL PACK son '
    '«Gastos fijos mensuales del año de crucero» y «Fondo de maniobra», las '
    'dos en la hoja «' + H_INV + '»: la segunda es la que viaja al libro 2 por '
    'el cruce 2 <- 7, ya CALCULADA, porque sus dos factores -meses de colchón '
    'y gastos fijos- viven aquí. Este libro RECIBE tres cifras por celda verde '
    'con fila de cuadre: el CAPEX SIN el fondo de maniobra (7 <- 2), la '
    'capacidad diaria del obrador (7 <- 1) y el precio de la cobertura en base '
    'imponible, que llega incorporado al food cost de escandallo (7 <- 3). '
    'CERO fórmulas que nombren otro fichero.'
)


# ==========================================================================
# Demostraciones con pycel
# ==========================================================================
def demo(ruta):
    exc = C.compilador(ruta)
    pruebas = []

    def ev(ref):
        return exc.evaluate(ref)

    r_ing2 = "'%s'!C%d" % (H_PYG, P['ingresos'])
    r_neto2 = "'%s'!C%d" % (H_PYG, P['neto'])
    r_fijos2 = "'%s'!C%d" % (H_PYG, P['tot_fijos'])
    r_tickets = "'%s'!B%d" % (H_SUP, S['tickets'])

    # 1. el total de fijos es la suma de sus catorce renglones
    total = ev(r_fijos2)
    partes = sum(ev("'%s'!C%d" % (H_PYG, f))
                 for f in range(P['personal'], P['financieros'] + 1))
    pruebas.append(('El total de costes fijos suma sus catorce renglones',
                    abs(total - partes) < 0.01,
                    'total %.2f frente a suma %.2f' % (total, partes)))

    # 2. el año 2 del P&L reproduce el año de crucero del juego de datos
    esperado = D.cuenta_resultados_crucero()
    pruebas.append(('El año 2 del P&L es el año de crucero del juego de datos',
                    abs(ev(r_ing2) - esperado['ventas_sin_iva']) < 1.0,
                    'libro %.2f frente a datos_ejemplo %.2f'
                    % (ev(r_ing2), esperado['ventas_sin_iva'])))

    # 3. LAS DOS CELDAS QUE CITA EL PACK: fijos mensuales y fondo de maniobra.
    #    Si éstas se mueven, el libro 2 publica otra inversión total.
    fijos_mes = ev("'%s'!B%d" % (H_INV, IV['fijos_mes']))
    fondo = ev("'%s'!B%d" % (H_INV, IV['fondo']))
    pruebas.append(('Los gastos fijos mensuales y el fondo de maniobra son los '
                    'que importó el libro 2',
                    abs(fijos_mes - D.gastos_fijos_mensuales()) < 0.01
                    and abs(fondo - D.fondo_maniobra()) < 0.01,
                    'fijos %.2f (datos %.2f) · fondo %.2f (datos %.2f)'
                    % (fijos_mes, D.gastos_fijos_mensuales(), fondo,
                       D.fondo_maniobra())))

    # 4. la inversión total del libro es la misma que la del libro 2
    total_inv = ev("'%s'!B%d" % (H_INV, IV['total']))
    pruebas.append(('La inversión total coincide con la del libro de CAPEX',
                    abs(total_inv - D.inversion_total_sin_iva()) < 0.01,
                    'libro %.2f frente a datos_ejemplo %.2f'
                    % (total_inv, D.inversion_total_sin_iva())))

    # 5. el cuadro de amortización cierra
    pend = ev("'%s'!B%d" % (H_FIN, F_PENDIENTE))
    pruebas.append(('El cuadro de amortización devuelve todo el principal',
                    abs(pend) <= 0.01,
                    'pendiente al vencimiento %.2f' % pend))

    # 6. la financiación nace cuadrada
    dif = ev("'%s'!B%d" % (H_FIN, F['diferencia']))
    pruebas.append(('El origen de fondos cubre la necesidad de caja de fábrica',
                    0 <= dif < 1.0, 'diferencia origen - usos %.2f €' % dif))

    # 7. quitar el B2B mueve el punto muerto
    pm_con = ev("'%s'!B%d" % (H_CAN, K_PM_CON))
    pm_sin = ev("'%s'!B%d" % (H_CAN, K_PM_SIN))
    pruebas.append(('El punto muerto cambia al quitar el canal B2B',
                    abs(pm_con - pm_sin) > 1.0,
                    'con B2B %.2f, sin B2B %.2f' % (pm_con, pm_sin)))

    # 8. la fecha límite de Navidad se calcula hacia atrás y el corporativo
    #    se cierra ANTES que ella
    entrega = ev("'%s'!B%d" % (H_TES, T['entrega']))
    limite = ev("'%s'!B%d" % (H_TES, T['limite']))
    mes_lim = ev("'%s'!B%d" % (H_TES, T['mes_limite']))
    agenda = ev("'%s'!B%d" % (H_TAL, W['cierre_agenda']))
    pruebas.append(('La fecha límite de Navidad va hacia atrás, cae en octubre '
                    'y la agenda corporativa se cierra antes todavía',
                    limite < entrega and agenda < limite and mes_lim == 10,
                    'entrega %s · límite %s (mes %s) · agenda %s'
                    % (entrega, limite, mes_lim, agenda)))

    # 9. los asistentes del punto muerto del taller son los del juego de datos
    asis = ev("'%s'!B%d" % (H_TAL, W['asistentes_pm']))
    pruebas.append(('Los asistentes que cubren el taller son los del juego de '
                    'datos',
                    abs(asis - D.asistentes_punto_muerto_taller()) < 0.01,
                    'libro %.3f frente a datos_ejemplo %.3f'
                    % (asis, D.asistentes_punto_muerto_taller())))

    # 10. «sin dato» es cadena vacía, nunca cero
    exc.set_value(r_tickets, '')
    vacio = exc.evaluate(r_ing2)
    pruebas.append(('Sin clientes al día los ingresos salen VACÍOS, no a cero',
                    vacio == '', 'devuelve %r' % (vacio,)))

    # 11. el resultado responde a la entrada (compilador limpio: pycel no
    #     reevalúa bien un grafo al que ya se le ha inyectado un valor)
    otro = C.compilador(ruta)
    neto_base = otro.evaluate(r_neto2)
    otro.set_value(r_tickets, 40)
    neto_bajo = otro.evaluate(r_neto2)
    pruebas.append(('El resultado responde a la entrada de clientes al día',
                    neto_bajo < neto_base,
                    'con 40 clientes %.2f, con %d clientes %.2f'
                    % (neto_bajo, D.P('tickets_dia_crucero'), neto_base)))

    # 12. la fila de CUADRE del CAPEX avisa si alguien pisa la cifra del
    #     libro 2 (es la red de seguridad del cruce 7 <- 2)
    tercero = C.compilador(ruta)
    r_cuadre = "'%s'!B%d" % (H_INV, IV['capex_cuadre'])
    cuadre0 = tercero.evaluate(r_cuadre)
    tercero.set_value("'%s'!B%d" % (H_INV, IV['capex_trae']),
                      DEF_CAPEX * 1.30)
    cuadre1 = tercero.evaluate(r_cuadre)
    pruebas.append(('La fila de CUADRE avisa si el CAPEX deja de ser el del '
                    'libro 2',
                    cuadre0 == 'CUADRA' and str(cuadre1).startswith('REVISA'),
                    'de %r a %r' % (cuadre0, cuadre1)))

    # 13. la fila de CUADRE de la cobertura caza el defecto A-2: copiar el
    #     precio CON IVA de la fuente en vez del de base imponible
    cuarto = C.compilador(ruta)
    r_cob = "'%s'!B%d" % (H_PYG, P['cob_cuadre'])
    cob0 = cuarto.evaluate(r_cob)
    cuarto.set_value("'%s'!B%d" % (H_PYG, P['cob_trae']),
                     D.precio_cobertura_como_la_fuente('negra')[0])
    cob1 = cuarto.evaluate(r_cob)
    pruebas.append(('La fila de CUADRE caza el precio de cobertura CON IVA '
                    '(el defecto A-2)',
                    cob0 == 'CUADRA' and str(cob1).startswith('REVISA'),
                    'con la base imponible %r · con el precio de la fuente %r'
                    % (cob0, cob1)))

    return pruebas


def main():
    D.gate_legal(IDS_LEGALES)
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_supuestos(wb)
    hoja_inversion(wb)
    hoja_pyg(wb)
    hoja_equilibrio(wb)
    hoja_escenarios(wb)
    hoja_personal(wb)
    hoja_tesoreria(wb)
    hoja_financiacion(wb)
    hoja_canales(wb)
    hoja_talleres(wb)
    res = C.cerrar(wb, NOMBRE, TITULO, mapa(), NOTAS_MAPA)
    C.resumen(NOMBRE, res, demo(res['ruta']))


if __name__ == '__main__':
    main()
