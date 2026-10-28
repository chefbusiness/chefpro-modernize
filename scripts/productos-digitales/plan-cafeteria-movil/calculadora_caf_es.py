#!/usr/bin/env python3
"""
calculadora_caf_es.py — Plan de Negocio: Cafetería Móvil para Eventos ES (SPEC D13): `calculadora-escandallo-presupuesto-cafe-eventos.xlsx`,
del coste de la taza al precio por invitado y al presupuesto completo. Fork de `parrillero-2_2/calculadora_par_es.py` (hoja
Calculadora, Ejemplos, Instrucciones) con el bloque Escandallo de `plan-pizzeria/calculadora_piz_es.py`:
  · Escandallo: 16 insumos (10 de producto y 6 de envase y mesa) × 10 bebidas en g, ml o unidades → coste con y sin envase, PVP sin
    IVA, food cost con semáforo, margen, PVP recomendado y coste de la MEZCLA (lo lee la hoja Calculadora);
  · Calculadora: canal Particular / Empresa / Feria (desplegable); margen objetivo, canon, cobro y cancelación por tramos de cada
    canal en una tabla VISIBLE (nada de puntos tecleados en una fórmula); formato (bebidas por invitado según las horas) y horario;
  · logística por la TABLA DE ESCALADO de `datos_escalado.py` (fuente única): baristas, cafeteras, grupos, molinos, kg de café,
    l de leche, vasos o tazas, potencia, toma eléctrica o generador y agua;
  · precio por invitado sin IVA (redondeo 0,50 € hacia arriba) y con IVA del 10 %, equivalente por hora y por bebida;
    desplazamiento en línea aparte SIN margen; cobro (señal + resto); cancelación por tramos «de X a menos de Y» sin huecos;
  · Feria: venta directa (tazas × ticket − canon − coste) y tazas para cubrir los costes;
  · aviso de electricidad (SPEC D11: un enchufe de 16 A da ≈ 3,7 kW);
  · 3 ejemplos (boda, congreso con pausas, jornada de feria) por las mismas fórmulas; autotest pycel ± 0,01 €.
Hojas `Escandallo` · `Calculadora` · `Ejemplos` · `Instrucciones` (firma `calc-beta` de `motor.detectar`). A4, protegida sin
contraseña, verdes desbloqueadas. Corre en el VPS (openpyxl + pycel).

    /root/venv-guias/bin/python calculadora_caf_es.py --salida <dir>      # genera + inject_cache + autotest
    /root/venv-guias/bin/python calculadora_caf_es.py --salida <dir> --autotest

Sesión Claude Code, 28-oct-2026.
"""
import argparse
import math
import os
import re
import sys
from collections import OrderedDict

import openpyxl
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Font, PatternFill, Protection
from openpyxl.worksheet.datavalidation import DataValidation

AQUI = os.path.dirname(os.path.abspath(__file__))
PD = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(PD, 'planes-v2_0'))
import motor                                                                       # noqa: E402
import datos_escalado as DE                                                        # noqa: E402  (fuente única de la tabla)
try:
    import caf_version                                                             # noqa: E402,F401  (1.0 · octubre 2026)
except ImportError:                                                                # el implementador del plan lo crea aparte
    motor.VERSION, motor.VERSION_MES = '1.0', 'octubre 2026'
    motor.VERSION_FMT = ('Versión ' + motor.VERSION + ' · ' + motor.VERSION_MES + ' · aichef.pro/{pid} · info@aichef.pro')

PID = 'plan-negocio-cafeteria-movil-eventos'
FICHERO = 'calculadora-escandallo-presupuesto-cafe-eventos.xlsx'
TITULO = 'Calculadora de escandallo y presupuesto de cafetería móvil para eventos'
HE, H1, H2, H3 = 'Escandallo', 'Calculadora', 'Ejemplos', 'Instrucciones'
VERDE = PatternFill('solid', fgColor='E8F5E9')
GRIS = PatternFill('solid', fgColor='F2F2F2')
ROJO = PatternFill('solid', bgColor='F8CBAD', fgColor='F8CBAD')
AMBAR = PatternFill('solid', bgColor='FFE699', fgColor='FFE699')
OK = PatternFill('solid', bgColor='C6E0B4', fgColor='C6E0B4')
FUENTE = 'Calibri'
CANALES = ['Particular', 'Empresa', 'Feria']
EUR, ENT, PCT, DEC, EUR3 = '#,##0.00 €', '#,##0', '0%', '#,##0.0', '#,##0.000 €'
FC_OK, FC_VIG, FC_ALTO = 'En objetivo', 'Vigila el coste', 'Por encima del objetivo'
MZ_OK, MZ_NO = 'Correcto: la mezcla suma el cien por cien', 'Revisa la mezcla: no suma el cien por cien'
SERVICIOS = ['Loza (tazas reutilizables)', 'Vaso de un solo uso']
ELEC = ['Enchufe de 16 A', 'Toma dedicada', 'Sin toma (generador o baterías)']
TXT_TOMA_NO = 'Toma dedicada o generador'
TXT_AV_GEN = 'Sin toma: lleva generador o baterías (kVA mínimos en su fila)'
TXT_AV_MAL = 'AVISO: este enchufe no basta para tus cafeteras; pide toma dedicada por escrito o lleva generador'
TXT_AV_OK = 'Potencia cubierta: confirma por escrito en el contrato la toma y su potencia'

# ---------------------------------------------------------------------------------------------------------------------
# Escandallo: insumos (nombre, precio, merma, origen, unidad de la receta: 'g' | 'ml' | 'ud'). Sin IVA. F1-research §3.b.
# ---------------------------------------------------------------------------------------------------------------------
INSUMOS = [
    ('Café en grano (g · €/kg)', 22.00, 0.10, 'Research §3.b: 18-28 €/kg, caso 22 €/kg [estimado]; 10 % de merma por purga y calibrado.', 'g'),
    ('Leche entera (ml · €/l)', 1.05, 0.10, 'Research §3.b: ≈ 1,05 €/l [estimado].', 'ml'),
    ('Leche sin lactosa (ml · €/l)', 1.35, 0.10, 'Estimación del kit.', 'ml'),
    ('Bebida de avena barista (ml · €/l)', 2.50, 0.10, 'Research §3.b: ≈ 2,50 €/l [estimado].', 'ml'),
    ('Bebida de soja barista (ml · €/l)', 1.90, 0.10, 'Estimación del kit.', 'ml'),
    ('Cacao en polvo (g · €/kg)', 9.00, 0.05, 'Estimación del kit.', 'g'),
    ('Concentrado de chai (ml · €/l)', 6.00, 0.05, 'Estimación del kit.', 'ml'),
    ('Sirope de vainilla o caramelo (ml · €/l)', 6.00, 0.05, 'Estimación del kit.', 'ml'),
    ('Té e infusiones (g · €/kg)', 40.00, 0.05, 'Hueco para tu carta de infusiones: vacío en el ejemplo.', 'g'),
    ('Azúcar (g · €/kg)', 1.50, 0.0, 'Estimación del kit.', 'g'),
    ('Vaso de 4 oz (ud. · €/ud.)', 0.05, 0.03, 'Research §3.b: vaso, tapa, servilleta y removedor ≈ 0,13 € por bebida [cálculo].', 'ud'),
    ('Vaso de 8 oz (ud. · €/ud.)', 0.07, 0.03, 'Ídem.', 'ud'),
    ('Vaso de 12 oz (ud. · €/ud.)', 0.09, 0.03, 'Ídem.', 'ud'),
    ('Tapa (ud. · €/ud.)', 0.03, 0.03, 'Ídem.', 'ud'),
    ('Removedor de madera (ud. · €/ud.)', 0.01, 0.03, 'Ídem. Los agitadores de plástico están prohibidos (Ley 7/2022, art. 56).', 'ud'),
    ('Servilleta (ud. · €/ud.)', 0.01, 0.03, 'Ídem.', 'ud'),
]
NI = len(INSUMOS)
N_PROD = 10                                                                        # los 10 primeros son producto; el resto, envase y mesa
IX = dict((n[0].split(' (')[0], i) for i, n in enumerate(INSUMOS))
#: receta por bebida: ml de cacao/chai/sirope/azúcar/té (g o ml) y envase. La leche y el café salen de `datos_escalado`.
RECETA = {
    'Espresso': dict(env=('Vaso de 4 oz', 'Removedor de madera', 'Servilleta')),
    'Americano': dict(env=('Vaso de 8 oz', 'Tapa', 'Removedor de madera', 'Servilleta')),
    'Cortado': dict(env=('Vaso de 4 oz', 'Removedor de madera', 'Servilleta')),
    'Café con leche': dict(env=('Vaso de 8 oz', 'Tapa', 'Removedor de madera', 'Servilleta')),
    'Flat white': dict(env=('Vaso de 8 oz', 'Tapa', 'Removedor de madera', 'Servilleta')),
    'Capuchino': dict(otros={'Cacao en polvo': 2}, env=('Vaso de 8 oz', 'Tapa', 'Removedor de madera', 'Servilleta')),
    'Latte': dict(otros={'Sirope de vainilla o caramelo': 10}, env=('Vaso de 12 oz', 'Tapa', 'Removedor de madera', 'Servilleta')),
    'Mocha': dict(otros={'Cacao en polvo': 15, 'Azúcar': 8}, env=('Vaso de 12 oz', 'Tapa', 'Removedor de madera', 'Servilleta')),
    'Chai latte': dict(otros={'Concentrado de chai': 60}, env=('Vaso de 12 oz', 'Tapa', 'Removedor de madera', 'Servilleta')),
    'Chocolate a la taza': dict(otros={'Cacao en polvo': 25, 'Azúcar': 10},
                                env=('Vaso de 8 oz', 'Tapa', 'Removedor de madera', 'Servilleta')),
}
BEB = OrderedDict((b[0], b) for b in DE.BEBIDAS)
NB = len(BEB)
BCOL = [openpyxl.utils.get_column_letter(5 + j) for j in range(NB)]                # E..N
OCOL = openpyxl.utils.get_column_letter(5 + NB)                                    # O: origen del precio


def _leche_repartida(ml):
    """Reparte los ml de una bebida entre las cuatro leches; el resto del redondeo va a la entera."""
    partes = [int(round(ml * s)) for _n, s in DE.LECHES[1:]]
    return [ml - sum(partes)] + partes


def grid():
    """[insumo][bebida] en g, ml o unidades (las fórmulas de la fila del café se calculan en la hoja: aquí su valor)."""
    g = [[0.0] * NB for _ in range(NI)]
    for j, (nom, (_n, mez, dob, leche, _oz, _pvp)) in enumerate(BEB.items()):
        g[IX['Café en grano']][j] = dob * DE.G_POR_DOBLE
        for k, v in enumerate(_leche_repartida(leche)):
            g[1 + k][j] = float(v)
        for n, q in RECETA[nom].get('otros', {}).items():
            g[IX[n]][j] = float(q)
        for n in RECETA[nom]['env']:
            g[IX[n]][j] = 1.0
    return g


ESC_IN = [('iva', 'IVA de la bebida servida (%)', PCT, 0.10,
           'Bebida para consumir en el acto o para llevar: 10 % (Ley 37/1992, art. 91). Los extras con precio propio van al 21 %.'),
          ('obj', 'Food cost objetivo (% sobre el precio sin IVA)', PCT, 0.25,
           'Estimación del kit: referencia de cafetería de 22 a 30 %. Pon el que te marque tu plan financiero.'),
          ('tol', 'Margen de vigilancia sobre el objetivo (puntos)', PCT, 0.05,
           'Hasta este margen por encima del objetivo, el semáforo dice «Vigila el coste»; más allá, «Por encima del objetivo».'),
          ('gdoble', 'Gramos de café por doble (g)', DEC, float(DE.G_POR_DOBLE),
           'Research §3.b: un doble de especialidad lleva 16-18 g. Mueve los gramos de la fila del café de todas las bebidas.')]
E = OrderedDict((k, 5 + i) for i, (k, *_r) in enumerate(ESC_IN))
E_CAB = 5 + len(ESC_IN) + 1
E_PVP, E_MIX, E_DOB = E_CAB + 1, E_CAB + 2, E_CAB + 3
E_I0 = E_DOB + 1
E_I1 = E_I0 + NI - 1
E_P1 = E_I0 + N_PROD - 1                                                           # última fila de producto
E_R = E_I1 + 2
RES = [('leche', 'Leche y bebida vegetal en total (ml)', DEC), ('c_prod', 'Coste de producto (€)', EUR3),
       ('c_env', 'Coste de envase y mesa (€)', EUR3), ('c_tot', 'Coste total con envase (€)', EUR3),
       ('pvp_sin', 'Precio de carta sin IVA (€)', EUR), ('fc_sin', 'Food cost sin envase', '0.0%'),
       ('fc', 'Food cost con envase', '0.0%'), ('sem', 'Semáforo del food cost', 'General'),
       ('margen', 'Margen por bebida (€)', EUR), ('pvp_obj', 'Precio de carta con IVA para llegar al objetivo (€)', EUR)]
RW = OrderedDict((k, E_R + 1 + i) for i, (k, *_r) in enumerate(RES))
E_M0 = E_R + 1 + len(RES) + 1
MZ = [('suma', 'Suma de la mezcla de ventas', PCT), ('chk', 'Comprobación de la mezcla', 'General'),
      ('m_prod', 'Coste medio por bebida sin envase (€)', EUR3), ('m_env', 'Coste medio de envase y mesa por bebida (€)', EUR3),
      ('m_tot', 'Coste medio por bebida con envase (€)', EUR3), ('m_cafe', 'Café medio por bebida (g)', DEC),
      ('m_leche', 'Leche media por bebida (ml)', DEC), ('m_ticket', 'Ticket medio sin IVA de tu carta (€)', EUR),
      ('m_fc', 'Food cost de la mezcla (con envase)', '0.0%')]
MR = OrderedDict((k, E_M0 + 1 + i) for i, (k, *_r) in enumerate(MZ))
E_FIN = E_M0 + 1 + len(MZ) + 1


def esc_ref(k):
    return "'%s'!$B$%d" % (HE, MR[k])


# ---------------------------------------------------------------------------------------------------------------------
# Calculadora: política por canal, formatos, horarios
# ---------------------------------------------------------------------------------------------------------------------
FORMATOS = OrderedDict((n, v) for n, _h, v, _r in DE.BEBIDAS_POR_INVITADO)
HORARIOS = OrderedDict(DE.AJUSTE_HORARIO)
#: política por canal: Particular · Empresa · Feria
CANAL_TAB = OrderedDict([
    ('margen', ('Margen bruto objetivo sobre el precio', PCT, (0.55, 0.50, 0.20),
                'Lo que queda del precio tras bebidas, bollería, personal del evento, generador y canon. Con él pagas vehículo, seguros, '
                'base, publicidad y tu beneficio. Estimación del kit: la boda particular lleva más que la empresa; en feria el margen '
                'es menor porque vendes volumen.')),
    ('canon', ('Canon del organizador (% de la venta)', PCT, (0.0, 0.0, 0.15),
               'Solo ferias, mercados y festivales (research §3.a: porcentaje de la venta o cuota fija). El canon fijo se escribe aparte.')),
    ('pc_senal', ('Cobro: señal al reservar (% del total)', PCT, (0.30, 0.30, 0.0),
                  'Particular y Empresa, el 30 % al firmar. La señal es a cuenta del precio. Feria: no hay señal al cliente.')),
    ('pc_antes', ('Cobro: resto antes del evento (% del total)', PCT, (0.70, 0.0, 0.0), 'Particular: el 70 % restante, siete días antes del evento.')),
    ('pc_30d', ('Cobro: resto a 30 días de la factura (% del total)', PCT, (0.0, 0.70, 0.0), 'Empresa: el 70 % restante, a 30 días de la factura.')),
    ('pc_acto', ('Cobro: en el momento de la venta (% del total)', PCT, (0.0, 0.0, 1.0), 'Feria: venta directa, cobras en el acto (datáfono o efectivo).')),
    ('d1', ('Cancelación: primer corte (días antes del evento)', ENT, (60, 30, 30),
            'Desde este número de días o más: tramo 1. Los cortes bajan de uno a otro y no dejan huecos.')),
    ('d2', ('Cancelación: segundo corte (días antes del evento)', ENT, (30, 15, 15), 'Desde aquí hasta menos del primer corte: tramo 2.')),
    ('d3', ('Cancelación: tercer corte (días antes del evento)', ENT, (7, 7, 7),
            'Desde aquí hasta menos del segundo corte: tramo 3. Por debajo de este número de días: tramo 4.')),
    ('cn1', ('Cancelación tramo 1 (% del total que retienes)', PCT, (0.10, 0.10, 0.0),
             'Particular y Empresa: el 10 % del total. Feria: no se aplica.')),
    ('cn2', ('Cancelación tramo 2 (% del total que retienes)', PCT, (0.30, 0.30, 0.0), 'Particular y Empresa: el 30 % del total.')),
    ('cn3', ('Cancelación tramo 3 (% del total que retienes)', PCT, (0.60, 0.60, 0.0), 'Particular y Empresa: el 60 % del total.')),
    ('cn4', ('Cancelación tramo 4 (% del total que retienes)', PCT, (1.0, 1.0, 0.0),
             'Menos de siete días o no presentación: el 100 % menos los costes que te ahorras: consumibles, café y leche sin gastar, refuerzo y desplazamiento. En Feria se rige por las bases del organizador.')),
])
LABELS = OrderedDict([('lab1', 'Tramo 1'), ('lab2', 'Tramo 2'), ('lab3', 'Tramo 3'), ('lab4', 'Tramo 4')])

ENTRADAS = [
    ('canal', 'Cliente', '@', 'Particular',
     'Particular, Empresa o Feria: cambian el margen objetivo, el canon, el cobro y los tramos de cancelación (tabla del final). '
     'En Feria, «invitados» son las tazas que esperas vender.'),
    ('guests', 'Invitados previstos (en Feria, tazas previstas)', ENT, 120, 'Número entero de invitados a los que sirves.'),
    ('formato', 'Formato del servicio (fija las bebidas por invitado)', '@', 'Más de 2 y hasta 4 horas',
     'Bebidas por invitado según las horas de barra: tabla del final (estimación del kit con ratios de EE. UU.). En Feria no se usa.'),
    ('horario', 'Horario', '@', 'Noche (después de la cena)',
     'Mañana +25 %, boda de noche −10 % (research §1). Ajusta las bebidas por invitado. En Feria no se usa.'),
    ('serv', 'Servicio en', '@', 'Loza (tazas reutilizables)',
     'Loza: sin coste de vaso ni tapa. Vaso de un solo uso: suma el envase y, en el ticket, el precio aparte del vaso de plástico '
     '(Ley 7/2022, art. 55). El compostable con forro de PE o PLA también es plástico.'),
    ('hours', 'Horas de servicio con la barra abierta', DEC, 3, 'Se usan para el ritmo de bebidas por hora y para el personal.'),
    ('h_extra', 'Horas por persona fuera del servicio (carga, viaje, montaje y limpieza)', DEC, 5,
     'Estimación del kit: un servicio de dos horas es una jornada de siete a nueve (research §1). Pon las reales.'),
    ('dulces', 'Bollería o dulce por invitado (coste, sin IVA)', EUR, 0.40,
     'Lo que te cuesta el dulce que añades al pack. 0 si no ofreces bollería.'),
    ('rentals', 'Alquileres repercutidos (carpa, cubierta, mesas, loza extra)', EUR, 0.0,
     'Lo que te cobra el alquilador para este evento. Si lo facturas aparte sin ser accesorio, ese importe va al 21 % de IVA.'),
    ('elec', 'Electricidad en el lugar', '@', 'Enchufe de 16 A',
     'Un enchufe de 16 A a 230 V da unos 3,7 kW. Tu cafetera de dos grupos gasta de 2,4 a 4,5 kW: con una de 3,5 kW o menos cabe; '
     'si no, toma dedicada o generador inverter o baterías.'),
    ('gen_cost', 'Generador o baterías: coste por evento (si no hay toma)', EUR, 90.0,
     'Estimación del kit: combustible o carga y desgaste. Solo se suma si eliges «Sin toma».'),
    ('kw_maq', 'Potencia de tu cafetera de dos grupos (kW)', DEC, DE.KW_MAQUINA,
     'La del caso: 3,5 kW o menos para caber en un enchufe de 16 A. Mira la placa de tu máquina.'),
    ('wage', 'Coste bruto por hora de un barista', EUR, 13.0,
     'Estimación del kit: del titular (14,2 €/h) y del camarero fijo discontinuo (11,0 €/h) con 14 pagas y 1.780 horas. Copia tu convenio.'),
    ('ss', 'Seguridad Social a cargo de la empresa', PCT, 0.33,
     '30,65 % de contingencias, desempleo, FOGASA, formación y MEI, más AT/EP (fijos discontinuos, art. 16 ET).'),
    ('km', 'Kilómetros de ida (base → lugar)', ENT, 35, 'Se cobran ida y vuelta, en una línea aparte y sin margen (en Feria son coste tuyo).'),
    ('per_km', 'Tarifa por kilómetro de desplazamiento', EUR, 0.45,
     'Referencia de escaparate de 2026: 0,45 €/km (La Galería del Café, en Bodas.net). Pon la tuya.'),
    ('iva', 'IVA del servicio', PCT, 0.10, 'Ley 37/1992, art. 91: bebida para consumir en el acto, 10 %. Lo que facturas aparte con precio propio, 21 %.'),
    ('tkt', 'Feria: ticket medio por taza que cobrarás (sin IVA)', EUR, 3.00,
     'Research §4: ≈ 3,00 € sin IVA por taza. Mira el ticket medio de tu carta en la hoja «%s». Solo cuenta si el cliente es Feria.' % HE),
    ('canon_fijo', 'Feria: canon fijo del organizador (€)', EUR, 0.0, 'Cuota fija por emplazamiento, si el organizador la cobra. Solo cuenta en Feria.'),
    ('dias', 'Días que faltan para el evento si el cliente cancela', ENT, 45,
     'Elige los días y la hoja te dice el tramo y lo que retienes.'),
]
K = OrderedDict((k, 5 + i) for i, (k, *_r) in enumerate(ENTRADAS))
F_CALC = 5 + len(ENTRADAS) + 1

# nombre, rótulo, formato, expresión, nota. Expresión None = cabecera de bloque.
SALIDAS = [
    ('h_esc', 'LOGÍSTICA (tabla de escalado)', None, None, ''),
    ('beb_inv', 'Bebidas por invitado del formato', '0.00', '{t_beb_inv}', 'Busca el formato en la tabla del final.'),
    ('ajuste', 'Ajuste por horario', PCT, '{t_ajuste}', 'Busca el horario en la tabla del final.'),
    ('bebidas', 'Bebidas que se sirven (ud.)', ENT, 'IF({is_feria},{guests},ROUNDUP(ROUND({guests}*{beb_inv}*(1+{ajuste}),2),0))',
     'Invitados × bebidas por invitado × (1 + ajuste), hacia arriba. En Feria, las tazas previstas.'),
    ('por_hora', 'Bebidas por hora (media)', DEC, '{bebidas}/{hours}', ''),
    ('baristas', 'Baristas necesarios', ENT, 'MAX(1,ROUNDUP(ROUND({por_hora}*{r_pico}/{r_cap_barista},2),0))',
     'Bebidas por hora × factor de pico ÷ lo que saca un barista, hacia arriba.'),
    ('estaciones', 'Cafeteras de dos grupos (estaciones)', ENT, 'ROUNDUP({baristas}/{r_bar_maq},0)',
     'Dos baristas por cafetera; una segunda estación entra cuando el pico no cabe en una.'),
    ('grupos', 'Grupos en total', ENT, '{estaciones}*{r_grupos_maq}', ''),
    ('molinos', 'Molinos', ENT, '{estaciones}+{r_molinos_extra}', 'Uno por estación más uno de reserva (descafeinado o filtro).'),
    ('kg_cafe', 'Café en grano (kg)', DEC, 'ROUNDUP({bebidas}*{esc_cafe}/1000+{r_purga},1)',
     'Bebidas × café medio de tu mezcla (hoja «%s») más la purga y el calibrado.' % HE),
    ('l_leche', 'Leche y bebidas vegetales (l)', ENT, 'ROUNDUP(ROUND({bebidas}*{esc_leche}/1000,2),0)', 'Bebidas × leche media de tu mezcla.'),
    ('vasos', 'Vasos desechables o tazas de loza (ud.)', ENT,
     'IF({is_loza},ROUNDUP(ROUND({guests}*{r_loza_inv},2),0),ROUNDUP(ROUND({bebidas}*(1+{r_reserva}),2),0))',
     'Loza: tazas por invitado con reposición para el lavado. Vaso de un solo uso: bebidas más la reserva.'),
    ('agua', 'Agua limpia (l)', ENT, 'ROUNDUP(ROUND({bebidas}*{r_agua_beb}+{r_agua_base},2),0)',
     'Lleva un depósito de aguas grises al menos igual: no se vierte en el recinto. El agua de los depósitos es tu responsabilidad hasta el punto de uso.'),
    ('h_ele', 'ELECTRICIDAD (aviso del contrato)', None, None, ''),
    ('kw', 'Potencia de las cafeteras (kW)', DEC, '{estaciones}*{kw_maq}', 'Estaciones × kW de tu cafetera.'),
    ('amp', 'Intensidad (A)', DEC, '{kw}*1000/{r_tension}', 'kW × 1.000 ÷ tensión.'),
    ('kw_enchufe', 'Potencia de un enchufe (kW)', '0.00', '{r_amp_enchufe}*{r_tension}/1000',
     'SPEC D11: un enchufe de 16 A a 230 V da unos 3,7 kW (3,68). Los molinos, la nevera y la iluminación van aparte: déjales margen.'),
    ('kva', 'Generador inverter mínimo (kVA)', ENT, 'ROUNDUP(ROUND({kw}*{r_factor_kva},2),0)',
     'kW × factor de margen, hacia arriba: una cafetera de 3,5 kW pide 5 kVA. Baterías de litio con inversor: la misma potencia, más silenciosas.'),
    ('toma', 'Toma que hace falta', 'General', 'IF({kw}<={kw_enchufe},$A${e1},"%s")' % TXT_TOMA_NO,
     'Con una cafetera de 3,5 kW o menos basta un enchufe de 16 A; con dos estaciones, no.'),
    ('aviso', 'AVISO de electricidad', 'General',
     'IF({elec}=$A${e3},"%s",IF(AND({kw}>{kw_enchufe},{elec}=$A${e1}),"%s","%s"))' % (TXT_AV_GEN, TXT_AV_MAL, TXT_AV_OK),
     'El contrato del kit pide la toma por escrito: cantidad de kW, distancia y cuadro.'),
    ('h_cos', 'COSTE DIRECTO', None, None, ''),
    ('c_beb', 'Coste de las bebidas', EUR, '{bebidas}*IF({is_loza},{esc_sin},{esc_con})',
     'Bebidas × coste medio de la mezcla del Escandallo (con envase si es vaso de un solo uso).'),
    ('c_dulces', 'Coste de bollería o dulces', EUR, '{dulces}*{guests}', ''),
    ('c_staff', 'Coste de personal (salario + Seguridad Social)', EUR, '{baristas}*({hours}+{h_extra})*{wage}*(1+{ss})',
     'Baristas × (horas de servicio + horas fuera del servicio) × coste por hora. Si cobras tú de barista, cuéntate: es tu coste de oportunidad.'),
    ('c_gen', 'Generador o baterías', EUR, 'IF({elec}=$A${e3},{gen_cost},0)', ''),
    ('c_rent', 'Alquileres repercutidos', EUR, '{rentals}', ''),
    ('c_desp_f', 'Desplazamiento a la feria (coste tuyo)', EUR, 'IF({is_feria},{km}*2*{per_km},0)',
     'En Feria nadie te paga el viaje: entra en el coste. En los demás clientes va en su línea aparte.'),
    ('c_total', 'Coste directo total', EUR, '{c_beb}+{c_dulces}+{c_staff}+{c_gen}+{c_rent}+{c_desp_f}', ''),
    ('c_guest', 'Coste directo por invitado', EUR, '{c_total}/{guests}', ''),
    ('h_pre', 'PRECIO Y PRESUPUESTO', None, None, ''),
    ('margen', 'Margen objetivo del cliente elegido', PCT, '{t_margen}', 'De la tabla por cliente del final.'),
    ('canon', 'Canon del organizador (cliente elegido)', PCT, '{t_canon}', 'De la tabla por cliente del final. Solo Feria.'),
    ('price', 'PRECIO POR INVITADO SIN IVA', EUR, 'ROUNDUP({c_total}/(1-{margen}-{canon})/{guests}*2,0)/2',
     'Coste ÷ (1 − margen − canon) ÷ invitados, redondeado a los 0,50 € de arriba. Es el precio de las empresas («+ IVA»). '
     'En Feria es el ticket mínimo por taza que cubre coste, canon y margen: compáralo con el tuyo.'),
    ('price_iva', 'PRECIO POR INVITADO CON IVA', EUR, '{price}*(1+{iva})',
     'Es el que ve un particular: en una oferta a consumidores el precio va con impuestos incluidos.'),
    ('subtotal', 'Subtotal de bebidas sin IVA', EUR, '{price}*{guests}', 'Precio por invitado × invitados.'),
    ('price_h', 'Equivalente por hora de barra (sin IVA)', EUR, '{subtotal}/{hours}', 'Subtotal ÷ horas de servicio: para comparar con tarifas por hora.'),
    ('price_taza', 'Equivalente por bebida (sin IVA)', EUR, '{subtotal}/{bebidas}', 'Subtotal ÷ bebidas: para comparar con tarifas por consumición.'),
    ('desp', 'Desplazamiento aparte (ida y vuelta, sin margen)', EUR, 'IF({is_feria},0,{km}*2*{per_km})', 'Línea aparte del presupuesto.'),
    ('base', 'Base imponible', EUR, '{subtotal}+{desp}', ''),
    ('iva_amt', 'IVA', EUR, '{base}*{iva}', ''),
    ('total', 'TOTAL DEL PRESUPUESTO (con IVA)', EUR, '{base}+{iva_amt}', ''),
    ('h_cob', 'COBRO', None, None, ''),
    ('cb1', 'Importe del cobro 1: señal al reservar', EUR, '{total}*{t_pc_senal}', 'A cuenta del precio. Factura de cada pago, también de la señal.'),
    ('cb2', 'Importe del cobro 2: resto antes del evento', EUR, '{total}*{t_pc_antes}', 'Particular: siete días antes.'),
    ('cb3', 'Importe del cobro 3: resto a 30 días de la factura', EUR, '{total}*{t_pc_30d}', 'Empresa.'),
    ('cb4', 'Importe del cobro 4: en el momento de la venta', EUR, '{total}*{t_pc_acto}', 'Feria.'),
    ('canon_amt', 'Canon del organizador sobre el subtotal', EUR, '{subtotal}*{canon}', ''),
    ('profit', 'Margen bruto en euros', EUR, '{subtotal}-{c_total}-{canon_amt}', 'Sobre el subtotal, sin el desplazamiento.'),
    ('margin_calc', 'Margen bruto (calculado)', '0.0%', 'IF({subtotal}=0,0,{profit}/{subtotal})',
     'Sale de los costes, nunca se teclea. Queda igual o por encima del objetivo por el redondeo del precio.'),
    ('h_can', 'CANCELACIÓN (tramos sin huecos)', None, None, ''),
    ('tramo', 'Tramo que corresponde a los días elegidos', 'General',
     'IF({dias}>={t_d1},{t_lab1},IF({dias}>={t_d2},{t_lab2},IF({dias}>={t_d3},{t_lab3},{t_lab4})))', 'Mira los días de la entrada «Días que faltan».'),
    ('ret_pct', 'Porcentaje que retienes en ese tramo', PCT,
     'IF({dias}>={t_d1},{t_cn1},IF({dias}>={t_d2},{t_cn2},IF({dias}>={t_d3},{t_cn3},{t_cn4})))', ''),
    ('ret', 'Importe que retienes si cancela ese día', EUR, '{total}*{ret_pct}', ''),
    ('can1', 'Importe retenido: tramo 1 (el más lejano)', EUR, '{total}*{t_cn1}', 'Los cortes de cada cliente están en la tabla del final.'),
    ('can2', 'Importe retenido: tramo 2', EUR, '{total}*{t_cn2}', ''),
    ('can3', 'Importe retenido: tramo 3', EUR, '{total}*{t_cn3}', ''),
    ('can4', 'Importe retenido: tramo 4 (el más cercano o no presentación)', EUR, '{total}*{t_cn4}', ''),
    ('h_fer', 'FERIA: PREVISIÓN DE LA JORNADA (solo si el cliente es Feria)', None, None, ''),
    ('c_var', 'Coste variable por taza (bebida + dulce)', EUR, '({c_beb}+{c_dulces})/{guests}', ''),
    ('f_venta', 'Venta prevista (tazas × ticket, sin IVA)', EUR, 'IF({is_feria},{guests}*{tkt},0)', ''),
    ('f_canon', 'Canon del organizador (% de la venta + cuota fija)', EUR, 'IF({is_feria},{f_venta}*{canon}+{canon_fijo},0)', ''),
    ('f_result', 'Resultado de la jornada (venta − canon − coste)', EUR, 'IF({is_feria},{f_venta}-{f_canon}-{c_total},0)',
     'Antes de impuestos y de los costes fijos del negocio (vehículo, seguros, base).'),
    ('f_eq', 'Tazas para cubrir los costes de la jornada', ENT,
     'IF({is_feria},IF({tkt}*(1-{canon})-{c_var}<=0,0,ROUNDUP(({c_staff}+{c_gen}+{c_rent}+{c_desp_f}+{canon_fijo})/({tkt}*(1-{canon})-{c_var}),0)),0)',
     'Costes de la jornada que no dependen de las tazas ÷ lo que te deja cada taza tras el canon.'),
]
S = OrderedDict()
_fila = F_CALC
for _s in SALIDAS:
    _fila += 1
    if _s[3] is not None:
        S[_s[0]] = _fila
F_FIN_SAL = _fila

# --- bloques del pie -------------------------------------------------------------------------------------------------
F_REGLAS = F_FIN_SAL + 2
RG = OrderedDict((k, F_REGLAS + 1 + i) for i, (k, *_r) in enumerate(DE.REGLAS))
F_FORM = F_REGLAS + 1 + len(DE.REGLAS) + 1
F_HOR = F_FORM + 1 + len(FORMATOS) + 1
F_SERV = F_HOR + 1 + len(HORARIOS) + 1
F_ELEC = F_SERV + 1 + len(SERVICIOS) + 1
F_CAN = F_ELEC + 1 + len(ELEC) + 1
CT = OrderedDict((k, F_CAN + 1 + i) for i, k in enumerate(list(CANAL_TAB) + list(LABELS)))
F_ESC = F_CAN + 1 + len(CT) + 1
ESC_HORAS = F_ESC + 1                                                              # fila de las horas del evento tipo
ESC_F0 = ESC_HORAS + 1                                                             # 1.ª fila de resultados de la tabla
F_ULT = ESC_F0 + len(DE.FILAS_TABLA)

EJEMPLOS = OrderedDict([
    ('Boda con barra tras la cena', dict(
        canal='Particular', guests=120, formato='Más de 2 y hasta 4 horas', horario='Noche (después de la cena)',
        serv='Loza (tazas reutilizables)', hours=3, h_extra=5, dulces=0.40, rentals=0.0, elec='Enchufe de 16 A',
        gen_cost=90.0, kw_maq=3.5, wage=13.0, ss=0.33, km=35, per_km=0.45, iva=0.10, tkt=3.00, canon_fijo=0.0, dias=45)),
    ('Congreso con dos pausas de café', dict(
        canal='Empresa', guests=300, formato='Congreso con pausas de café', horario='Tarde o jornada mixta',
        serv='Loza (tazas reutilizables)', hours=8, h_extra=2, dulces=0.0, rentals=0.0, elec='Toma dedicada',
        gen_cost=90.0, kw_maq=3.5, wage=13.0, ss=0.33, km=25, per_km=0.45, iva=0.10, tkt=3.00, canon_fijo=0.0, dias=20)),
    ('Jornada de feria con venta directa', dict(
        canal='Feria', guests=250, formato='Más de 2 y hasta 4 horas', horario='Tarde o jornada mixta',
        serv='Vaso de un solo uso', hours=10, h_extra=2, dulces=0.0, rentals=0.0, elec='Sin toma (generador o baterías)',
        gen_cost=90.0, kw_maq=3.5, wage=13.0, ss=0.33, km=40, per_km=0.45, iva=0.10, tkt=3.00, canon_fijo=0.0, dias=45)),
])
EJ_NOTAS = OrderedDict([
    ('Boda con barra tras la cena', 'Particular, 120 invitados (la boda del caso del plan financiero), barra de dos a cuatro horas '
     'tras la cena en loza, con un dulce de 0,40 € por invitado. El precio con IVA es el que ve el particular; cobro del 30 % al '
     'reservar y el 70 % siete días antes. Con 45 días de margen, si cancela retienes el 30 %. Dos baristas en una cafetera y un '
     'enchufe de 16 A: la cafetera de 3,5 kW cabe.'),
    ('Congreso con dos pausas de café', 'Empresa, 300 asistentes, jornada de 8 horas con dos pausas (1,6 bebidas por asistente, mezcla '
     'del caso), loza y toma dedicada. El precio se presupuesta «+ IVA»; cobro del 30 % al firmar y el 70 % a 30 días de la factura. '
     'Con 20 días de margen el tramo es el segundo y retienes el 30 %.'),
    ('Jornada de feria con venta directa', 'Feria: 250 tazas en una jornada de 10 horas, vaso de un solo uso (con su precio aparte en '
     'el ticket), generador y canon del 15 % del organizador. El «precio por invitado» es el ticket mínimo por taza; con el ticket de '
     '3,00 € la jornada deja unos {res} € antes de costes fijos, y por debajo de {eq} tazas pierdes.'),
])

# Escandallo: precio de carta por bebida y su ticket (Calculadora lo lee como `tkt`)


# ---------------------------------------------------------------------------------------------------------------------
# Cálculo en Python (espejo de las fórmulas) — la fuente del autotest
# ---------------------------------------------------------------------------------------------------------------------
def _ceil(x, dec=0):
    f = 10 ** dec
    return math.ceil(round(x * f, 9)) / float(f)


def calcular_escandallo(g=None, ing=None, mezcla=None, pvp=None, iva=0.10, obj=0.25, tol=0.05):
    """Resultados por bebida y de la mezcla con los datos por defecto (o los pasados)."""
    g = g or grid()
    ing = ing or [(p, m) for _n, p, m, _o, _u in INSUMOS]
    mezcla = mezcla or [b[1] / 100.0 for b in BEB.values()]
    pvp = pvp or [b[5] for b in BEB.values()]
    neto = [p / (1 - m) for p, m in ing]
    r = OrderedDict()
    r['neto'] = neto
    r['bebidas'] = []
    for j in range(NB):
        d = OrderedDict()
        d['leche'] = sum(g[i][j] for i in range(1, 5))
        d['c_prod'] = sum(g[i][j] * neto[i] for i in range(N_PROD)) / 1000.0
        d['c_env'] = sum(g[i][j] * neto[i] for i in range(N_PROD, NI))
        d['c_tot'] = d['c_prod'] + d['c_env']
        d['pvp_sin'] = pvp[j] / (1 + iva)
        d['fc_sin'] = d['c_prod'] / d['pvp_sin']
        d['fc'] = d['c_tot'] / d['pvp_sin']
        d['sem'] = FC_OK if d['fc'] <= obj else (FC_VIG if d['fc'] <= obj + tol else FC_ALTO)
        d['margen'] = d['pvp_sin'] - d['c_tot']
        d['pvp_obj'] = d['c_tot'] / obj * (1 + iva)
        r['bebidas'].append(d)
    suma = sum(mezcla)
    wp = lambda f: 0 if suma == 0 else sum(mezcla[j] * f(j) for j in range(NB)) / suma
    r['mz'] = OrderedDict(
        suma=suma, chk=MZ_OK if round(suma, 2) == 1 else MZ_NO,
        m_prod=wp(lambda j: r['bebidas'][j]['c_prod']), m_env=wp(lambda j: r['bebidas'][j]['c_env']),
        m_cafe=wp(lambda j: g[0][j]), m_leche=wp(lambda j: r['bebidas'][j]['leche']),
        m_ticket=wp(lambda j: r['bebidas'][j]['pvp_sin']))
    r['mz']['m_tot'] = r['mz']['m_prod'] + r['mz']['m_env']
    r['mz']['m_fc'] = r['mz']['m_tot'] / r['mz']['m_ticket']
    return r


ESC = calcular_escandallo()


def calcular(e, esc=None):
    esc = esc or ESC
    mz = esc['mz']
    r = OrderedDict()
    ic = CANALES.index(e['canal'])
    t = lambda k: CANAL_TAB[k][2][ic]
    reg = dict(DE.R)
    feria = e['canal'] == CANALES[2]
    loza = e['serv'] == SERVICIOS[0]
    r['beb_inv'] = FORMATOS[e['formato']]
    r['ajuste'] = HORARIOS[e['horario']]
    r['bebidas'] = e['guests'] if feria else DE._cu(e['guests'] * r['beb_inv'] * (1 + r['ajuste']))
    r['por_hora'] = r['bebidas'] / float(e['hours'])
    r['baristas'] = max(1, DE._cu(r['por_hora'] * reg['pico'] / reg['cap_barista']))
    r['estaciones'] = int(_ceil(r['baristas'] / float(reg['bar_maq'])))
    r['grupos'] = r['estaciones'] * reg['grupos_maq']
    r['molinos'] = r['estaciones'] + reg['molinos_extra']
    r['kg_cafe'] = _ceil(r['bebidas'] * mz['m_cafe'] / 1000.0 + reg['purga'], 1)
    r['l_leche'] = DE._cu(r['bebidas'] * mz['m_leche'] / 1000.0)
    r['vasos'] = DE._cu(e['guests'] * reg['loza_inv']) if loza else DE._cu(r['bebidas'] * (1 + reg['reserva']))
    r['agua'] = DE._cu(r['bebidas'] * reg['agua_beb'] + reg['agua_base'])
    r['kw'] = r['estaciones'] * e['kw_maq']
    r['amp'] = r['kw'] * 1000.0 / reg['tension']
    r['kw_enchufe'] = reg['amp_enchufe'] * reg['tension'] / 1000.0
    r['kva'] = DE._cu(r['kw'] * reg['factor_kva'])
    r['toma'] = ELEC[0] if r['kw'] <= r['kw_enchufe'] else TXT_TOMA_NO
    r['aviso'] = (TXT_AV_GEN if e['elec'] == ELEC[2] else
                  (TXT_AV_MAL if (r['kw'] > r['kw_enchufe'] and e['elec'] == ELEC[0]) else TXT_AV_OK))
    r['c_beb'] = r['bebidas'] * (mz['m_prod'] if loza else mz['m_tot'])
    r['c_dulces'] = e['dulces'] * e['guests']
    r['c_staff'] = r['baristas'] * (e['hours'] + e['h_extra']) * e['wage'] * (1 + e['ss'])
    r['c_gen'] = e['gen_cost'] if e['elec'] == ELEC[2] else 0
    r['c_rent'] = e['rentals']
    r['c_desp_f'] = e['km'] * 2 * e['per_km'] if feria else 0
    r['c_total'] = r['c_beb'] + r['c_dulces'] + r['c_staff'] + r['c_gen'] + r['c_rent'] + r['c_desp_f']
    r['c_guest'] = r['c_total'] / e['guests']
    r['margen'] = t('margen')
    r['canon'] = t('canon')
    r['price'] = _ceil(r['c_total'] / (1 - r['margen'] - r['canon']) / e['guests'] * 2) / 2
    r['price_iva'] = r['price'] * (1 + e['iva'])
    r['subtotal'] = r['price'] * e['guests']
    r['price_h'] = r['subtotal'] / e['hours']
    r['price_taza'] = r['subtotal'] / r['bebidas']
    r['desp'] = 0 if feria else e['km'] * 2 * e['per_km']
    r['base'] = r['subtotal'] + r['desp']
    r['iva_amt'] = r['base'] * e['iva']
    r['total'] = r['base'] + r['iva_amt']
    r['cb1'] = r['total'] * t('pc_senal')
    r['cb2'] = r['total'] * t('pc_antes')
    r['cb3'] = r['total'] * t('pc_30d')
    r['cb4'] = r['total'] * t('pc_acto')
    r['canon_amt'] = r['subtotal'] * r['canon']
    r['profit'] = r['subtotal'] - r['c_total'] - r['canon_amt']
    r['margin_calc'] = 0 if r['subtotal'] == 0 else r['profit'] / r['subtotal']
    d1, d2, d3 = t('d1'), t('d2'), t('d3')
    labs = etiquetas(d1, d2, d3)
    if e['dias'] >= d1:
        k = 0
    elif e['dias'] >= d2:
        k = 1
    elif e['dias'] >= d3:
        k = 2
    else:
        k = 3
    r['tramo'] = labs[k]
    r['ret_pct'] = t('cn%d' % (k + 1))
    r['ret'] = r['total'] * r['ret_pct']
    for i in (1, 2, 3, 4):
        r['can%d' % i] = r['total'] * t('cn%d' % i)
    r['c_var'] = (r['c_beb'] + r['c_dulces']) / e['guests']
    r['f_venta'] = e['guests'] * e['tkt'] if feria else 0
    r['f_canon'] = r['f_venta'] * r['canon'] + e['canon_fijo'] if feria else 0
    r['f_result'] = r['f_venta'] - r['f_canon'] - r['c_total'] if feria else 0
    den = e['tkt'] * (1 - r['canon']) - r['c_var']
    r['f_eq'] = 0 if (not feria or den <= 0) else int(_ceil((r['c_staff'] + r['c_gen'] + r['c_rent'] + r['c_desp_f'] + e['canon_fijo']) / den))
    return r


def etiquetas(d1, d2, d3):
    """Texto de los cuatro tramos de cancelación (espejo de las fórmulas de la tabla)."""
    f = lambda x: ('%g' % x)
    return ['%s días o más' % f(d1), 'De %s a menos de %s días' % (f(d2), f(d1)), 'De %s a menos de %s días' % (f(d3), f(d2)),
            'Menos de %s días' % f(d3)]


# ---------------------------------------------------------------------------------------------------------------------
# Fórmulas
# ---------------------------------------------------------------------------------------------------------------------
def _rng(col, f1, f2, hoja=H1):
    return "'%s'!$%s$%d:$%s$%d" % (hoja, col, f1, col, f2)


def refs(col):
    """Referencias a celdas de la columna `col` (B en Calculadora; B/C/D en Ejemplos) + búsquedas en las tablas."""
    ref = dict((k, '$%s$%d' % (col, f)) for k, f in K.items())
    ref.update((k, '$%s$%d' % (col, f)) for k, f in S.items())
    ref['t_beb_inv'] = 'INDEX(%s,MATCH(%s,%s,0))' % (_rng('B', F_FORM + 1, F_FORM + len(FORMATOS)), ref['formato'],
                                                     _rng('A', F_FORM + 1, F_FORM + len(FORMATOS)))
    ref['t_ajuste'] = 'INDEX(%s,MATCH(%s,%s,0))' % (_rng('B', F_HOR + 1, F_HOR + len(HORARIOS)), ref['horario'],
                                                    _rng('A', F_HOR + 1, F_HOR + len(HORARIOS)))
    for k, f in RG.items():
        ref['r_' + k] = "'%s'!$B$%d" % (H1, f)
    cab = "'%s'!$B$%d:$D$%d" % (H1, F_CAN, F_CAN)
    for k, f in CT.items():
        ref['t_' + k] = "INDEX('%s'!$B$%d:$D$%d,MATCH(%s,%s,0))" % (H1, f, f, ref['canal'], cab)
    ref['is_feria'] = "%s='%s'!$D$%d" % (ref['canal'], H1, F_CAN)
    ref['is_loza'] = "%s='%s'!$A$%d" % (ref['serv'], H1, F_SERV + 1)
    ref['e1'] = str(F_ELEC + 1)
    ref['e3'] = str(F_ELEC + 3)
    for k, c in (('esc_sin', 'm_prod'), ('esc_con', 'm_tot'), ('esc_cafe', 'm_cafe'), ('esc_leche', 'm_leche')):
        ref[k] = esc_ref(c)
    ref['kw_enchufe'] = '$%s$%d' % (col, S['kw_enchufe'])
    return ref


def a_excel(expr, ref):
    e = re.sub(r'\$A\$\{(e\d)\}', lambda m: "'%s'!$A$%s" % (H1, ref[m.group(1)]), expr)
    return re.sub(r'\{(\w+)\}', lambda m: ref[m.group(1)], e)


def _f(ws, coord, v, b=False, sz=11, i=False, fmt=None, wrap=False, fill=None, locked=True):
    c = ws[coord]
    c.value = v
    c.font = Font(name=FUENTE, size=sz, bold=b, italic=i)
    if fmt:
        c.number_format = fmt
    c.alignment = Alignment(wrap_text=wrap, vertical='top')
    if fill:
        c.fill = fill
    c.protection = Protection(locked=locked)
    return c


def _nota(ws, fila, texto, desde='C', hasta='F', chars=105.0):
    if not texto:
        return
    _f(ws, '%s%d' % (desde, fila), texto, wrap=True)
    ws.merge_cells('%s%d:%s%d' % (desde, fila, hasta, fila))
    ws.row_dimensions[fila].height = max(16, 15 * math.ceil(len(texto) / chars))


def _imprimir(ws, horizontal=False):
    ws.page_setup.paperSize = 9                                                   # A4
    ws.page_setup.orientation = 'landscape' if horizontal else 'portrait'
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.oddFooter.center.text = 'aichef.pro/%s · página &P de &N' % PID
    ws.print_options.horizontalCentered = True
    ws.protection.sheet = True                                                    # sin contraseña
    ws.sheet_view.showGridLines = False


def _dv(ws, tipo, celdas, f1=None, f2=None, op=None, titulo='Valor no válido', msg=''):
    dv = DataValidation(type=tipo, formula1=f1, formula2=f2, operator=op, allow_blank=False, showErrorMessage=True,
                        errorTitle=titulo, error=msg)
    ws.add_data_validation(dv)
    for c in celdas:
        dv.add(c)


def _nom(v, n=11):
    return v if len(v) <= n else v


# ---------------------------------------------------------------------------------------------------------------------
# Hoja Escandallo
# ---------------------------------------------------------------------------------------------------------------------
def hoja_escandallo(wb):
    ws = wb.active
    ws.title = HE
    for col, w in (('A', 44), ('B', 14), ('C', 9), ('D', 12)):
        ws.column_dimensions[col].width = w
    for col in BCOL:
        ws.column_dimensions[col].width = 14
    ws.column_dimensions[OCOL].width = 56
    _f(ws, 'A1', 'ESCANDALLO POR BEBIDA — 16 INSUMOS × 10 BEBIDAS, EN GRAMOS, MILILITROS Y UNIDADES', b=True, sz=14)
    _f(ws, 'A2', 'Escribe solo en las celdas VERDES (precios, mermas, cantidades, mezcla y precios de carta). Importes sin IVA salvo el precio de '
                 'carta. Los precios son estimaciones del kit: pon los de tu proveedor. El coste de una bebida de esta hoja NO es el '
                 '«coste de bebida» del plan financiero: aquel es la media de la mezcla con la merma, no una receta.', wrap=True)
    ws.merge_cells('A2:%s2' % OCOL)
    ws.row_dimensions[2].height = 34
    for col, t in zip('ABE', ('DATOS GENERALES', 'Valor', 'Notas')):
        _f(ws, '%s4' % col, t, b=True, fill=GRIS)
    for k, rot, fmt, val, nota in ESC_IN:
        f = E[k]
        _f(ws, 'A%d' % f, rot)
        _f(ws, 'B%d' % f, val, fmt=fmt, fill=VERDE, locked=False)
        _nota(ws, f, nota, desde='E', hasta=OCOL, chars=150.0)
    for col, t in (('A', 'INSUMO (cantidad · precio)'), ('B', 'Precio sin IVA'), ('C', 'Merma'), ('D', 'Precio neto')):
        _f(ws, '%s%d' % (col, E_CAB), t, b=True, fill=GRIS, wrap=True)
    _f(ws, '%s%d' % (OCOL, E_CAB), 'ORIGEN DEL PRECIO DE EJEMPLO', b=True, fill=GRIS, wrap=True)
    _f(ws, 'A%d' % E_PVP, 'Precio de carta con IVA (€)', b=True)
    _f(ws, 'A%d' % E_MIX, 'Mezcla de ventas (% de las bebidas)', b=True)
    _f(ws, 'A%d' % E_DOB, 'Dobles de espresso por bebida', b=True)
    for j, (nom, (_n, mez, dob, _leche, _oz, pvp)) in enumerate(BEB.items()):
        c = BCOL[j]
        _f(ws, '%s%d' % (c, E_CAB), nom, b=True, fill=VERDE, wrap=True, locked=False)
        _f(ws, '%s%d' % (c, E_PVP), pvp, fmt=EUR, fill=VERDE, locked=False, b=True)
        _f(ws, '%s%d' % (c, E_MIX), mez / 100.0, fmt=PCT, fill=VERDE, locked=False)
        _f(ws, '%s%d' % (c, E_DOB), float(dob), fmt='0.0', fill=VERDE, locked=False)
    ws.row_dimensions[E_CAB].height = 32
    g = grid()
    for i, (nom, p, m, origen, _u) in enumerate(INSUMOS):
        f = E_I0 + i
        _f(ws, 'A%d' % f, nom, fill=VERDE, locked=False)
        _f(ws, 'B%d' % f, p, fmt=EUR, fill=VERDE, locked=False)
        _f(ws, 'C%d' % f, m, fmt='0%', fill=VERDE, locked=False)
        _f(ws, 'D%d' % f, '=B%d/(1-C%d)' % (f, f), fmt=EUR3)
        for j in range(NB):
            c = BCOL[j]
            if i == 0:                                                           # café: dobles × gramos por doble
                _f(ws, '%s%d' % (c, f), '=%s$%d*$B$%d' % (c, E_DOB, E['gdoble']), fmt='#,##0.0;-#,##0.0;"-"')
            else:
                _f(ws, '%s%d' % (c, f), g[i][j], fmt='#,##0.0;-#,##0.0;"-"', fill=VERDE, locked=False)
        _f(ws, '%s%d' % (OCOL, f), origen, i=True)
    _f(ws, 'A%d' % E_R, 'RESULTADO POR BEBIDA', b=True, fill=GRIS)
    for j in range(NB):
        _f(ws, '%s%d' % (BCOL[j], E_R), '=%s%d' % (BCOL[j], E_CAB), b=True, fill=GRIS, wrap=True)
    ws.row_dimensions[E_R].height = 32
    for k, rot, fmt in RES:
        f = RW[k]
        neg = k in ('c_tot', 'fc')
        _f(ws, 'A%d' % f, rot, b=neg)
        for j in range(NB):
            c = BCOL[j]
            col_prod = '%s$%d:%s$%d' % (c, E_I0, c, E_P1)
            col_env = '%s$%d:%s$%d' % (c, E_P1 + 1, c, E_I1)
            ex = {
                'leche': 'SUM(%s%d:%s%d)' % (c, E_I0 + 1, c, E_I0 + 4),
                'c_prod': 'SUMPRODUCT(%s,$D$%d:$D$%d)/1000' % (col_prod, E_I0, E_P1),
                'c_env': 'SUMPRODUCT(%s,$D$%d:$D$%d)' % (col_env, E_P1 + 1, E_I1),
                'c_tot': '%s%d+%s%d' % (c, RW['c_prod'], c, RW['c_env']),
                'pvp_sin': '%s%d/(1+$B$%d)' % (c, E_PVP, E['iva']),
                'fc_sin': '%s%d/%s%d' % (c, RW['c_prod'], c, RW['pvp_sin']),
                'fc': '%s%d/%s%d' % (c, RW['c_tot'], c, RW['pvp_sin']),
                'sem': 'IF(%s%d<=$B$%d,"%s",IF(%s%d<=$B$%d+$B$%d,"%s","%s"))' % (
                    c, RW['fc'], E['obj'], FC_OK, c, RW['fc'], E['obj'], E['tol'], FC_VIG, FC_ALTO),
                'margen': '%s%d-%s%d' % (c, RW['pvp_sin'], c, RW['c_tot']),
                'pvp_obj': '%s%d/$B$%d*(1+$B$%d)' % (c, RW['c_tot'], E['obj'], E['iva']),
            }[k]
            _f(ws, '%s%d' % (c, f), '=' + ex, fmt=fmt, b=neg, wrap=(k == 'sem'))
    ws.row_dimensions[RW['sem']].height = 32
    rng = '%s%d:%s%d' % (BCOL[0], RW['sem'], BCOL[-1], RW['sem'])
    top = '%s%d' % (BCOL[0], RW['sem'])
    for txt, fill in ((FC_OK, OK), (FC_VIG, AMBAR), (FC_ALTO, ROJO)):
        ws.conditional_formatting.add(rng, FormulaRule(formula=['%s="%s"' % (top, txt)], fill=fill))
    # coste de la mezcla
    _f(ws, 'A%d' % E_M0, 'COSTE DE LA MEZCLA (lo lee la hoja «%s»)' % H1, b=True, fill=GRIS)
    _f(ws, 'B%d' % E_M0, 'Valor', b=True, fill=GRIS)
    mix = '$%s$%d:$%s$%d' % (BCOL[0], E_MIX, BCOL[-1], E_MIX)
    fil = lambda k: '$%s$%d:$%s$%d' % (BCOL[0], RW[k], BCOL[-1], RW[k])
    suma = '$B$%d' % MR['suma']
    # VALUE() solo fuerza un número nativo en pycel (SUMPRODUCT devuelve un escalar de numpy que ROUNDUP no acepta); en Excel no cambia nada
    pond = lambda rango: 'IF(%s=0,0,VALUE(SUMPRODUCT(%s,%s))/%s)' % (suma, mix, rango, suma)
    cafe = '$%s$%d:$%s$%d' % (BCOL[0], E_I0, BCOL[-1], E_I0)
    ex = {
        'suma': 'SUM(%s)' % mix,
        'chk': 'IF(ROUND(%s,2)=1,"%s","%s")' % (suma, MZ_OK, MZ_NO),
        'm_prod': pond(fil('c_prod')), 'm_env': pond(fil('c_env')),
        'm_tot': '$B$%d+$B$%d' % (MR['m_prod'], MR['m_env']),
        'm_cafe': pond(cafe), 'm_leche': pond(fil('leche')), 'm_ticket': pond(fil('pvp_sin')),
        'm_fc': 'IF($B$%d=0,0,$B$%d/$B$%d)' % (MR['m_ticket'], MR['m_tot'], MR['m_ticket']),
    }
    for k, rot, fmt in MZ:
        f = MR[k]
        neg = k in ('m_tot', 'chk')
        _f(ws, 'A%d' % f, rot, b=neg)
        _f(ws, 'B%d' % f, '=' + ex[k], fmt=fmt, b=neg, wrap=(k == 'chk'))
    ws.merge_cells('B%d:E%d' % (MR['chk'], MR['chk']))
    ws.conditional_formatting.add('B%d' % MR['chk'], FormulaRule(formula=['$B$%d="%s"' % (MR['chk'], MZ_NO)], fill=ROJO))
    f = E_FIN
    _f(ws, 'A%d' % f, 'El coste con envase es el de la bebida servida en vaso de un solo uso; en loza solo cuenta el coste de producto. '
                      'Los vasos de papel con forro de PE o PLA ("compostables") son plástico a efectos de la Ley 7/2022: se cobran '
                      'aparte en el ticket. El food cost del plan financiero es otra cosa: la media de la mezcla con la merma.',
       i=True, wrap=True)
    ws.merge_cells('A%d:%s%d' % (f, OCOL, f))
    ws.row_dimensions[f].height = 34
    # validaciones
    _dv(ws, 'decimal', ['B%d' % E['iva'], 'B%d' % E['tol']] + ['C%d' % (E_I0 + i) for i in range(NI)],
        f1='0', f2='0.9', op='between', titulo='Porcentaje no válido', msg='Escribe un porcentaje entre 0 y 0,9 (0,1 = 10 %).')
    _dv(ws, 'decimal', ['B%d' % E['obj']], f1='0.01', f2='0.9', op='between', titulo='Objetivo no válido',
        msg='El objetivo no puede ser 0 (se divide entre él): escribe entre 0,01 y 0,9.')
    _dv(ws, 'decimal', ['%s%d' % (c, E_MIX) for c in BCOL], f1='0', f2='1', op='between', titulo='Porcentaje no válido',
        msg='Escribe un porcentaje entre 0 y 1. La mezcla entera tiene que sumar el cien por cien.')
    _dv(ws, 'decimal', ['B%d' % E['gdoble']] + ['B%d' % (E_I0 + i) for i in range(NI)] + ['%s%d' % (c, E_PVP) for c in BCOL]
        + ['%s%d' % (c, E_DOB) for c in BCOL]
        + ['%s%d' % (c, E_I0 + i) for c in BCOL for i in range(1, NI)],
        f1='0', op='greaterThanOrEqual', titulo='Importe no válido', msg='Escribe un número mayor o igual que 0.')
    ws.freeze_panes = 'B%d' % (E_CAB + 1)
    _imprimir(ws, horizontal=True)


# ---------------------------------------------------------------------------------------------------------------------
# Hoja Calculadora
# ---------------------------------------------------------------------------------------------------------------------
def hoja_calculadora(wb):
    ws = wb.create_sheet(H1)
    for col, w in (('A', 66), ('B', 24), ('C', 17), ('D', 17), ('E', 17), ('F', 56)):
        ws.column_dimensions[col].width = w
    _f(ws, 'A1', 'CALCULADORA DE PRECIOS DE CAFETERÍA MÓVIL PARA EVENTOS — DE LA TAZA AL PRESUPUESTO', b=True, sz=14)
    _f(ws, 'A2', 'Escribe sólo en las celdas VERDES: todo lo demás se calcula. Importes sin IVA salvo donde la fila diga lo contrario. '
                 'Los valores por defecto son estimaciones del kit (ratios de EE. UU. en el consumo): cámbialos por los tuyos.', wrap=True)
    ws.merge_cells('A2:F2')
    ws.row_dimensions[2].height = 32
    for col, t in zip('ABC', ('DATOS DEL EVENTO', 'Valor', 'Notas')):
        _f(ws, '%s4' % col, t, b=True, fill=GRIS)
    for k, rot, fmt, val, nota in ENTRADAS:
        f = K[k]
        _f(ws, 'A%d' % f, rot)
        _f(ws, 'B%d' % f, val, fmt=fmt if fmt != '@' else None, fill=VERDE, locked=False, wrap=(fmt == '@'))
        _nota(ws, f, nota)
    for col, t in zip('ABC', ('CÁLCULO', 'Valor', 'Notas')):
        _f(ws, '%s%d' % (col, F_CALC), t, b=True, fill=GRIS)
    ref = refs('B')
    fila = F_CALC
    for k, rot, fmt, expr, nota in SALIDAS:
        fila += 1
        if expr is None:
            _f(ws, 'A%d' % fila, rot, b=True, fill=GRIS)
            continue
        neg = k in ('price', 'price_iva', 'total', 'margin_calc', 'aviso')
        _f(ws, 'A%d' % fila, rot, b=neg)
        _f(ws, 'B%d' % fila, '=' + a_excel(expr, ref), fmt=fmt, b=neg, wrap=(fmt == 'General'))
        if fmt == 'General':
            ws.merge_cells('B%d:F%d' % (fila, fila))
            ws.row_dimensions[fila].height = 32 if k == 'aviso' else 16
            if nota:
                _f(ws, 'A%d' % fila, rot + ' · ' + nota, b=neg, wrap=True)
                ws.row_dimensions[fila].height = 48 if k == 'aviso' else 32
        else:
            _nota(ws, fila, nota)
    # reglas de escalado
    _f(ws, 'A%d' % F_REGLAS, 'REGLAS DE ESCALADO (fuente única: «datos_escalado»; misma tabla que las Instrucciones del plan y el Word)',
       b=True, fill=GRIS)
    _f(ws, 'B%d' % F_REGLAS, 'Valor', b=True, fill=GRIS)
    for k, rot, fm, val, nota in DE.REGLAS:
        fmt = {'ent': ENT, 'dec': '#,##0.00', 'pct': PCT}[fm]
        _f(ws, 'A%d' % RG[k], rot)
        _f(ws, 'B%d' % RG[k], val, fmt=fmt, fill=VERDE, locked=False)
        _nota(ws, RG[k], nota)
    # formato
    _f(ws, 'A%d' % F_FORM, 'FORMATO → BEBIDAS POR INVITADO', b=True, fill=GRIS)
    _f(ws, 'B%d' % F_FORM, 'Bebidas', b=True, fill=GRIS)
    for i, (nombre, hasta, v, rango) in enumerate(DE.BEBIDAS_POR_INVITADO, 1):
        _f(ws, 'A%d' % (F_FORM + i), nombre)
        _f(ws, 'B%d' % (F_FORM + i), v, fmt='0.00', fill=VERDE, locked=False)
        _f(ws, 'C%d' % (F_FORM + i), 'Rango del research: %s' % rango, i=True)
    _f(ws, 'D%d' % (F_FORM + 1), '%s' % DE.ORIGEN, i=True, wrap=True)
    ws.merge_cells('D%d:F%d' % (F_FORM + 1, F_FORM + 2))
    # horario
    _f(ws, 'A%d' % F_HOR, 'HORARIO → AJUSTE DE LAS BEBIDAS POR INVITADO', b=True, fill=GRIS)
    _f(ws, 'B%d' % F_HOR, 'Ajuste', b=True, fill=GRIS)
    for i, (nombre, aj) in enumerate(HORARIOS.items(), 1):
        _f(ws, 'A%d' % (F_HOR + i), nombre)
        _f(ws, 'B%d' % (F_HOR + i), aj, fmt='0%', fill=VERDE, locked=False)
    # opciones de servicio y electricidad
    _f(ws, 'A%d' % F_SERV, 'OPCIONES DE SERVICIO (lista de la entrada «Servicio en»)', b=True, fill=GRIS)
    for i, t in enumerate(SERVICIOS, 1):
        _f(ws, 'A%d' % (F_SERV + i), t)
    _f(ws, 'A%d' % F_ELEC, 'OPCIONES DE ELECTRICIDAD (lista de la entrada «Electricidad en el lugar»)', b=True, fill=GRIS)
    for i, t in enumerate(ELEC, 1):
        _f(ws, 'A%d' % (F_ELEC + i), t)
    # por cliente
    _f(ws, 'A%d' % F_CAN, 'POLÍTICA POR CLIENTE', b=True, fill=GRIS)
    for col, c in zip('BCD', CANALES):
        _f(ws, '%s%d' % (col, F_CAN), c, b=True, fill=GRIS, wrap=True)
    for k, (rot, fmt, vals, nota) in CANAL_TAB.items():
        f = CT[k]
        _f(ws, 'A%d' % f, rot)
        for col, v in zip('BCD', vals):
            _f(ws, '%s%d' % (col, f), v, fmt=fmt, fill=VERDE, locked=False)
        _f(ws, 'E%d' % f, nota, wrap=True)
        ws.merge_cells('E%d:F%d' % (f, f))
        ws.row_dimensions[f].height = max(16, 15 * math.ceil(len(nota) / 62.0))
    for n, (k, rot) in enumerate(LABELS.items(), 1):
        f = CT[k]
        _f(ws, 'A%d' % f, '%s de cancelación (texto, se calcula con los cortes)' % rot)
        for col in 'BCD':
            d = lambda kk: '%s%d' % (col, CT[kk])
            ex = {1: '%s&" días o más"' % d('d1'),
                  2: '"De "&%s&" a menos de "&%s&" días"' % (d('d2'), d('d1')),
                  3: '"De "&%s&" a menos de "&%s&" días"' % (d('d3'), d('d2')),
                  4: '"Menos de "&%s&" días"' % d('d3')}[n]
            _f(ws, '%s%d' % (col, f), '=' + ex, wrap=True)
        ws.row_dimensions[f].height = 32
    # tabla de escalado de referencia
    _f(ws, 'A%d' % F_ESC, 'TABLA DE ESCALADO (evento tipo: barra de dos a cuatro horas, por la tarde, con vaso de un solo uso)', b=True, fill=GRIS)
    for col, n in zip('BCDE', DE.TAM_REF):
        _f(ws, '%s%d' % (col, F_ESC), n, b=True, fill=GRIS, fmt='0" inv."')
    _f(ws, 'A%d' % ESC_HORAS, 'Horas de barra del evento tipo')
    _f(ws, 'B%d' % ESC_HORAS, DE.HORAS_REF, fmt='0', fill=VERDE, locked=False)
    r_ = dict(('r_' + k, "$B$%d" % f) for k, f in RG.items())
    fr = F_FORM + 1 + [n for n, *_x in DE.BEBIDAS_POR_INVITADO].index(DE.FORMATO_REF)
    hr = F_HOR + 1 + list(HORARIOS).index(DE.HORARIO_REF)
    esc_cafe, esc_leche = esc_ref('m_cafe'), esc_ref('m_leche')
    kwm = '$B$%d' % K['kw_maq']
    F = dict((k, ESC_F0 + i) for i, (k, *_r) in enumerate(DE.FILAS_TABLA))
    for k, rot, fm in DE.FILAS_TABLA:
        _f(ws, 'A%d' % F[k], rot)
        for col in 'BCDE':
            n = '%s$%d' % (col, F_ESC)
            c = lambda kk: '%s%d' % (col, F[kk])
            ex = {
                'bebidas': 'ROUNDUP(ROUND(%s*$B$%d*(1+$B$%d),2),0)' % (n, fr, hr),
                'baristas': 'MAX(1,ROUNDUP(ROUND(%s/$B$%d*%s/%s,2),0))' % (c('bebidas'), ESC_HORAS, r_['r_pico'], r_['r_cap_barista']),
                'estaciones': 'ROUNDUP(%s/%s,0)' % (c('baristas'), r_['r_bar_maq']),
                'grupos': '%s*%s' % (c('estaciones'), r_['r_grupos_maq']),
                'molinos': '%s+%s' % (c('estaciones'), r_['r_molinos_extra']),
                'kg_cafe': 'ROUNDUP(%s*%s/1000+%s,1)' % (c('bebidas'), esc_cafe, r_['r_purga']),
                'l_leche': 'ROUNDUP(ROUND(%s*%s/1000,2),0)' % (c('bebidas'), esc_leche),
                'vasos': 'ROUNDUP(ROUND(%s*(1+%s),2),0)' % (c('bebidas'), r_['r_reserva']),
                'kw': '%s*%s' % (c('estaciones'), kwm),
                'toma': 'IF(%s<=$B$%d,$A$%d,"%s")' % (c('kw'), S['kw_enchufe'], F_ELEC + 1, TXT_TOMA_NO),
                'agua': 'ROUNDUP(ROUND(%s*%s+%s,2),0)' % (c('bebidas'), r_['r_agua_beb'], r_['r_agua_base']),
            }[k]
            _f(ws, '%s%d' % (col, F[k]), '=' + ex, fmt={'ent': ENT, 'dec': DEC, 'txt': 'General'}[fm], wrap=(fm == 'txt'))
    ws.row_dimensions[F['toma']].height = 32
    f = F_ULT
    _f(ws, 'A%d' % f, 'Es la misma tabla que las Instrucciones del plan financiero y la sección de logística del plan de negocio. '
                      'Una cafetera de dos grupos saca unas 55 bebidas por hora con un barista y de 100 a 120 con dos; la segunda '
                      'estación entra cuando el pico no cabe. Un enchufe de 16 A da unos 3,7 kW: con una cafetera de 3,5 kW o menos '
                      'cabe; con dos estaciones hace falta toma dedicada o generador. Estimación del kit con ratios de EE. UU.',
       i=True, wrap=True)
    ws.merge_cells('A%d:F%d' % (f, f))
    ws.row_dimensions[f].height = 48
    # validaciones
    rf = refs('B')
    _dv(ws, 'list', [rf['canal'].replace('$', '')], f1='"%s"' % ','.join(CANALES), titulo='Cliente no válido',
        msg='Elige Particular, Empresa o Feria.')
    for k, f0, n, t in (('formato', F_FORM, len(FORMATOS), 'Formato'), ('horario', F_HOR, len(HORARIOS), 'Horario'),
                        ('serv', F_SERV, len(SERVICIOS), 'Servicio'), ('elec', F_ELEC, len(ELEC), 'Electricidad')):
        _dv(ws, 'list', [rf[k].replace('$', '')], f1='=$A$%d:$A$%d' % (f0 + 1, f0 + n), titulo='%s no válido' % t,
            msg='Elige una opción de la lista.')
    _dv(ws, 'whole', ['B%d' % K['guests']], f1='1', f2='100000', op='between', titulo='Número no válido',
        msg='Escribe un número entero de 1 o más.')
    _dv(ws, 'whole', ['B%d' % K['km'], 'B%d' % K['dias']] + ['%s%d' % (c, CT[k]) for k in ('d1', 'd2', 'd3') for c in 'BCD']
        + ['B%d' % RG[k] for k in ('cap_barista', 'bar_maq', 'grupos_maq', 'molinos_extra', 'agua_base', 'tension', 'amp_enchufe')],
        f1='0', f2='100000', op='between', titulo='Número no válido', msg='Escribe un número entero de 0 o más.')
    _dv(ws, 'decimal', ['B%d' % K['hours'], 'B%d' % ESC_HORAS], f1='0.5', f2='24', op='between', titulo='Horas no válidas',
        msg='Escribe entre 0,5 y 24 horas (no puede ser 0: se divide entre ellas).')
    _dv(ws, 'decimal', ['B%d' % K[k] for k in ('h_extra', 'dulces', 'rentals', 'gen_cost', 'kw_maq', 'wage', 'per_km', 'tkt', 'canon_fijo')]
        + ['B%d' % RG[k] for k in ('pico', 'purga', 'loza_inv', 'agua_beb', 'factor_kva')]
        + ['B%d' % (F_FORM + i) for i in range(1, len(FORMATOS) + 1)],
        f1='0', op='greaterThanOrEqual', titulo='Importe no válido', msg='Escribe un número mayor o igual que 0.')
    _dv(ws, 'decimal', ['B%d' % K[k] for k in ('ss', 'iva')] + ['B%d' % RG['reserva']]
        + ['%s%d' % (c, CT[k]) for k in CANAL_TAB if k not in ('margen', 'd1', 'd2', 'd3') for c in 'BCD'],
        f1='0', f2='1', op='between', titulo='Porcentaje no válido', msg='Escribe un porcentaje entre 0 y 1 (0,10 = 10 %).')
    _dv(ws, 'decimal', ['%s%d' % (c, CT['margen']) for c in 'BCD'], f1='0', f2='0.8', op='between',
        titulo='Porcentaje no válido', msg='Escribe un margen objetivo entre 0 y 80 % (0,50 = 50 %): se divide entre 1 − margen − canon.')
    _dv(ws, 'decimal', ['B%d' % (F_HOR + i) for i in range(1, len(HORARIOS) + 1)], f1='-0.5', f2='1', op='between',
        titulo='Ajuste no válido', msg='Escribe un ajuste entre −50 % y 100 %.')
    ws.freeze_panes = 'A5'
    _imprimir(ws)


# ---------------------------------------------------------------------------------------------------------------------
# Hoja Ejemplos
# ---------------------------------------------------------------------------------------------------------------------
def hoja_ejemplos(wb):
    ws = wb.create_sheet(H2)
    ws.column_dimensions['A'].width = 66
    for col in 'BCD':
        ws.column_dimensions[col].width = 30
    _f(ws, 'A1', '3 PRESUPUESTOS DE EJEMPLO — con las mismas fórmulas de la hoja «%s»' % H1, b=True, sz=14)
    _f(ws, 'A2', 'Estimaciones del kit para ilustrar el cálculo, no precios de mercado: cambia los datos en «%s» para presupuestar tus '
                 'eventos. Las tablas (margen y cobro por cliente, formatos, escalado) están al final de esa hoja y la mezcla de '
                 'bebidas, en «%s»; también mueven estos ejemplos.' % (H1, HE), wrap=True)
    ws.merge_cells('A2:D2')
    ws.row_dimensions[2].height = 32
    _f(ws, 'A4', 'DATOS DEL EVENTO', b=True, fill=GRIS)
    for j, nombre in enumerate(EJEMPLOS):
        _f(ws, '%s4' % 'BCD'[j], nombre, b=True, fill=GRIS, wrap=True)
    ws.row_dimensions[4].height = 48
    for k, rot, fmt, val, nota in ENTRADAS:
        _f(ws, 'A%d' % K[k], rot)
        for j, e in enumerate(EJEMPLOS.values()):
            _f(ws, '%s%d' % ('BCD'[j], K[k]), e[k], fmt=fmt if fmt != '@' else None, wrap=(fmt == '@'))
    _f(ws, 'A%d' % F_CALC, 'RESULTADO', b=True, fill=GRIS)
    for j in range(3):
        _f(ws, '%s%d' % ('BCD'[j], F_CALC), list(EJEMPLOS)[j], b=True, fill=GRIS, wrap=True)
    ws.row_dimensions[F_CALC].height = 48
    fila = F_CALC
    for k, rot, fmt, expr, nota in SALIDAS:
        fila += 1
        if expr is None:
            _f(ws, 'A%d' % fila, rot, b=True, fill=GRIS)
            continue
        neg = k in ('price', 'price_iva', 'total', 'margin_calc', 'aviso')
        _f(ws, 'A%d' % fila, rot, b=neg)
        for j in range(3):
            col = 'BCD'[j]
            _f(ws, '%s%d' % (col, fila), '=' + a_excel(expr, refs(col)), fmt=fmt, b=neg, wrap=(fmt == 'General'))
        if fmt == 'General':
            ws.row_dimensions[fila].height = 64 if k in ('aviso', 'tramo') else 32
    f = fila + 2
    _f(ws, 'A%d' % f, 'QUÉ ENSEÑA CADA EJEMPLO', b=True, fill=GRIS)
    for j, (nombre, nota) in enumerate(EJ_NOTAS.items()):
        rr = calcular(EJEMPLOS[nombre])
        nota = nota.replace('{res}', '{:,.0f}'.format(rr['f_result']).replace(',', '.')).replace('{eq}', str(rr['f_eq']))
        _f(ws, 'A%d' % (f + 1 + j), nombre, b=True, wrap=True)
        _f(ws, 'B%d' % (f + 1 + j), nota, wrap=True)
        ws.merge_cells('B%d:D%d' % (f + 1 + j, f + 1 + j))
        ws.row_dimensions[f + 1 + j].height = 15 * max(3, math.ceil(len(nota) / 85.0))
    ws.freeze_panes = 'B5'
    _imprimir(ws, horizontal=True)


# ---------------------------------------------------------------------------------------------------------------------
# Hoja Instrucciones
# ---------------------------------------------------------------------------------------------------------------------
INSTRUCCIONES = [
    ('INSTRUCCIONES DE USO — Calculadora de escandallo y presupuesto de cafetería móvil para eventos', True),
    ('Convierte el coste de tus bebidas en un precio por invitado y en un presupuesto completo: baristas, cafeteras, molinos, kilos de '
     'café, litros de leche, vasos, potencia eléctrica y agua, subtotal, IVA, total, cobro por pagos y lo que retienes si el cliente '
     'cancela. Sólo se escribe en las celdas VERDES; el margen se calcula.', False),
    ('HOJA «ESCANDALLO»', True),
    ('1. Escribe el precio sin IVA y la merma de cada insumo (café, leches, cacao, chai, sirope, té, azúcar, vasos, tapa, removedor y '
     'servilleta) y los gramos, mililitros o unidades de cada bebida. El café se calcula con los dobles por bebida y los gramos por doble.', False),
    ('2. Para cada bebida ves el coste de producto, el coste con envase, el precio sin IVA, el food cost con semáforo, el margen y el '
     'precio de carta que necesitarías para llegar a tu objetivo. La mezcla de ventas tiene que sumar el cien por cien: la hoja lo avisa.', False),
    ('3. El coste de UNA bebida de esta hoja no es el «coste de bebida» del plan financiero: aquel es la media de la mezcla con la merma '
     '(purga, calibrado y leche sobrante), no una receta. No copies uno en el otro.', False),
    ('HOJA «CALCULADORA»', True),
    ('4. Elige el cliente (Particular, Empresa o Feria), los invitados, el formato (bebidas por invitado según las horas), el horario y '
     'el servicio en loza o en vaso de un solo uso. En Feria, los invitados son las tazas que esperas vender.', False),
    ('5. La tabla de escalado del final da baristas, cafeteras de dos grupos, molinos, kilos de café, litros de leche, vasos o tazas, '
     'potencia, toma eléctrica y agua. Es la misma que figura en las Instrucciones del plan financiero y en el plan de negocio.', False),
    ('6. Escribe las horas de servicio y las horas fuera del servicio (carga, viaje, montaje y limpieza), el coste bruto por hora y la '
     'Seguridad Social. Si cobras tú de barista, cuéntate a precio de hora: es tu coste de oportunidad.', False),
    ('7. El precio por invitado es el coste directo dividido entre (1 − margen − canon), redondeado a los 0,50 € de arriba. Verás también '
     'su equivalente por hora de barra y por bebida, para comparar con las tarifas por hora o por consumición que te pidan.', False),
    ('8. A una empresa se le presupuesta el precio SIN IVA («+ IVA»); a un particular, el precio CON IVA, porque en una oferta a '
     'consumidores el precio va con los impuestos incluidos. El desplazamiento va en línea aparte, ida y vuelta y sin margen.', False),
    ('ELECTRICIDAD', True),
    ('Una cafetera de dos grupos gasta de 2,4 a 4,5 kW. Un enchufe de 16 A a 230 V da unos 3,7 kW: con una máquina de 3,5 kW o menos cabe; '
     'si no, hace falta toma dedicada o un generador inverter (o baterías de litio con inversor). Los molinos, la nevera y la iluminación '
     'van aparte: déjales margen. La hoja te avisa cuando el enchufe no basta, y el contrato del kit pide la toma por escrito.', False),
    ('IVA, VASOS Y COBROS', True),
    ('La bebida para consumir en el acto o para llevar va al 10 % de IVA (Ley 37/1992, art. 91). Los extras con precio propio (personalización '
     'de máquina o stand, vasos con logo, talleres) van al 21 %. En loza no hay vaso de plástico; el vaso de papel con forro de PE o PLA '
     '(«compostable») es plástico a efectos de la Ley 7/2022 (arts. 2 y 55) y se cobra aparte en el ticket. Pajitas y agitadores de plástico, '
     'prohibidos. En ferias y festivales, el organizador puede imponer su sistema de vaso reutilizable (RD 1055/2022, art. 7).', False),
    ('La propina voluntaria es del equipo: no entra en el precio, en la base imponible ni en el total. Los pagos en efectivo con particulares '
     'solo valen por debajo de 1.000 €: la ley prohíbe pagar en efectivo 1.000 € o más (art. 7 de la Ley 7/2012).', False),
    ('COBRO Y CANCELACIÓN', True),
    ('Particular: 30 % de señal al reservar (a cuenta del precio) y 70 % siete días antes del evento. Empresa: 30 % de señal y 70 % a 30 días '
     'de la factura. Feria: cobro en el acto. Emite factura de cada pago, también de la señal.', False),
    ('Cancelación, sobre el total, por tramos «de X a menos de Y» sin huecos. Particular: con 60 días o más retienes el 10 %; de 30 a '
     'menos de 60 días, el 30 %; de 7 a menos de 30 días, el 60 %; con menos de 7 días, el 100 % menos los costes que te ahorras (consumibles, café y leche sin gastar, refuerzo y desplazamiento). Empresa: con 30 días o más, el 10 %; de 15 a '
     'menos de 30 días, el 30 %; de 7 a menos de 15 días, el 60 %; con menos de 7 días, igual que Particular. Es recíproco: si cancela la cafetería, devuelve lo cobrado y paga lo del mismo tramo. Si cambias un corte en la tabla, los tramos '
     'se reescriben solos. En un servicio con fecha no hay derecho de desistimiento en la contratación a distancia (art. 103.l del TRLGDCU): '
     'por eso la política tiene que estar firmada.', False),
    ('FERIA', True),
    ('La venta directa en mercados y ferias depende de la autorización municipal y del canon del organizador. La hoja calcula la venta '
     '(tazas × ticket), el canon (porcentaje más cuota fija), el resultado de la jornada y las tazas que necesitas para cubrir los costes. '
     'El «precio por invitado» de esa columna es el ticket mínimo por taza que cubre coste, canon y margen.', False),
    ('ESTIMACIONES DEL KIT', True),
    ('Los valores por defecto y los tres ejemplos son estimaciones del kit para ilustrar el cálculo, no precios de mercado. El consumo de '
     'bebidas por invitado, la capacidad por barista y el agua usan ratios de EE. UU. y no tienen fuente española: sustitúyelos por tus '
     'mediciones. Cambia los precios por los de tu tostador y tus proveedores, los salarios por tu convenio y los kilómetros por los tuyos '
     'antes de presupuestar.', False),
    ('Fuentes: research del producto (octubre 2026); Ley 37/1992 del IVA, art. 91; Ley 7/2022, arts. 2, 55 y 56; RD 1055/2022, art. 7; '
     'TRLGDCU, arts. 85, 87 y 103.', False),
]


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H3)
    ws.column_dimensions['A'].width = 110
    f = 1
    for t, b in INSTRUCCIONES:
        _f(ws, 'A%d' % f, t, b=b, sz=13 if f == 1 else 11, wrap=True)
        if not b:
            ws.row_dimensions[f].height = max(16, 15 * math.ceil(len(t) / 120.0))
        f += 2 if b and f > 1 else 1
    f += 1
    for t in ('Para editar una celda que no esté en verde: Revisar → Desproteger hoja (no tiene contraseña).',
              'Más plantillas y kits del catálogo en aichef.pro/productos-digitales', motor.BIO_LINE,
              motor.VERSION_FMT.format(pid=PID)):
        _f(ws, 'A%d' % f, t, wrap=True)
        f += 1
    _imprimir(ws)


def generar(destino):
    wb = openpyxl.Workbook()
    hoja_escandallo(wb)
    hoja_calculadora(wb)
    hoja_ejemplos(wb)
    hoja_instrucciones(wb)
    pr = wb.properties
    pr.title = '%s · v%s' % (TITULO, motor.VERSION)
    pr.subject = 'Plan de Negocio: Cafetería Móvil para Eventos'
    pr.description = 'aichef.pro/%s' % PID
    pr.keywords = 'plan negocio cafetería móvil eventos, AI Chef Pro'
    pr.creator = pr.lastModifiedBy = motor.CREATOR
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    wb.save(destino)
    sys.path.insert(0, PD)
    import inject_cache as IC                                                      # noqa: E402
    nf, inj, fail = IC.inject(destino)
    print('%s: formulas=%d cache_inyectado=%d fallos_pycel=%d' % (os.path.basename(destino), nf, inj, fail))
    return fail


# ---------------------------------------------------------------------------------------------------------------------
# Autotest
# ---------------------------------------------------------------------------------------------------------------------
#: SPEC D12 (research §8 + brief de la pizzería) y restos que no pueden estar en una calculadora de café
PROHIBIDOS = [r'\bfreelance', r'carn[eé]t?\b', r'de 22 %', r'Comunitat', r'\b15 a[ñn]os', r'sin licencias', r'sin registro sanitario',
              r'demanda creciente', r'comida testigo', r'sin pl[aá]stico', r'exent[oa]s? de la Ley', r'desde 3\.000', r'garantizad',
              r'recuperas la inversi', r'torrefacto', r'carajillo|martini|alcohol', r'food ?truck', r'validad[oa]s?',
              r'Espa[ñn]a,? 2026', r'a toda Espa[ñn]a', r'enchufa en cualquier', r'service charge|sales tax']
RANGOS_EJEMPLO = {'Boda con barra tras la cena': (7.0, 10.0), 'Congreso con dos pausas de café': (3.5, 5.5)}


def _distinto(x, v):
    if isinstance(v, str):
        return x != v
    return not isinstance(x, (int, float)) or abs(float(x) - v) > 0.005


def celdas_escandallo(esc=None):
    """(celda, valor esperado, etiqueta) de todas las salidas del Escandallo."""
    esc = esc or ESC
    out = []
    for i in range(NI):
        out.append(('D%d' % (E_I0 + i), esc['neto'][i], 'neto%d' % i))
    for j in range(NB):
        for k in RW:
            out.append(('%s%d' % (BCOL[j], RW[k]), esc['bebidas'][j][k], '%s[%d]' % (k, j)))
    for k in MR:
        out.append(('B%d' % MR[k], esc['mz'][k], k))
    return out


def autotest(destino):
    from pycel import ExcelCompiler
    err, n = [], 0
    xl = ExcelCompiler(filename=destino)
    wv = openpyxl.load_workbook(destino, data_only=True)
    wf = openpyxl.load_workbook(destino)
    # Escandallo contra pycel y caché
    for c, v, lab in celdas_escandallo():
        n += 1
        for et, x in (('pycel', xl.evaluate("'%s'!%s" % (HE, c))), ('caché', wv[HE][c].value)):
            if _distinto(x, v):
                err.append('Escandallo %s (%s): %s %r ≠ esperado %r' % (c, lab, et, x, v))
    # Calculadora y Ejemplos
    casos = [(H2, 'BCD'[j], e, nombre) for j, (nombre, e) in enumerate(EJEMPLOS.items())]
    casos.append((H1, 'B', OrderedDict((k, v) for k, _r, _f2, v, _n in ENTRADAS), 'hoja principal'))
    for hoja, col, e, nombre in casos:
        esperado = calcular(e)
        for k, v in esperado.items():
            c = '%s%d' % (col, S[k])
            n += 1
            for lab, x in (('pycel', xl.evaluate("'%s'!%s" % (hoja, c))), ('caché', wv[hoja][c].value)):
                if _distinto(x, v):
                    err.append('%s · %s %s (%s): %s %r ≠ esperado %r' % (nombre, hoja, c, k, lab, x, v))
        if esperado['margin_calc'] + 1e-9 < esperado['margen']:
            err.append('%s: margen calculado %.4f < objetivo %.4f' % (nombre, esperado['margin_calc'], esperado['margen']))
        if nombre in RANGOS_EJEMPLO:
            lo, hi = RANGOS_EJEMPLO[nombre]
            if not lo <= esperado['price'] <= hi:
                err.append('%s: %.2f €/inv fuera del rango del research %s-%s' % (nombre, esperado['price'], lo, hi))
    # tabla de escalado de referencia (la de datos_escalado, la del plan y el Word) contra pycel
    F = dict((k, ESC_F0 + i) for i, (k, *_r) in enumerate(DE.FILAS_TABLA))
    for j, col in enumerate('BCDE'):
        d = DE.tabla_escalado()[j][1]
        for k, _rot, _fm in DE.FILAS_TABLA:
            n += 1
            x = xl.evaluate("'%s'!%s%d" % (H1, col, F[k]))
            v = d[k]
            if _distinto(x, v):
                err.append('escalado %s %s: %r ≠ %r' % (col, k, x, v))
    # casos propios: cambian celdas de la hoja principal y se recalculan con pycel
    base = OrderedDict((k, v) for k, _r, _f2, v, _n in ENTRADAS)
    propios = [('propio 1: Empresa, 40 invitados, hasta 2 h, mañana, vaso', dict(
        base, canal='Empresa', guests=40, formato='Hasta 2 horas', horario='Mañana (desayuno y café de media mañana)',
        serv='Vaso de un solo uso', hours=2, h_extra=4, dulces=0.0, km=0)),
        ('propio 2: Particular, 260 invitados, jornada, sin toma', dict(
            base, canal='Particular', guests=260, formato='Más de 6 horas (jornada)', horario='Tarde o jornada mixta',
            hours=9, elec='Sin toma (generador o baterías)', km=60, dias=10, rentals=150.0)),
        ('propio 3: Feria, 400 tazas, canon fijo', dict(
            base, canal='Feria', guests=400, hours=11, serv='Vaso de un solo uso', elec='Enchufe de 16 A', km=20, canon_fijo=120.0,
            tkt=3.2, dias=3, dulces=0.2))]
    for nombre, e in propios:
        esperado = calcular(e)
        xl2 = ExcelCompiler(filename=destino)
        for k in S:
            xl2.evaluate("'%s'!B%d" % (H1, S[k]))
        for k, v in e.items():
            xl2.set_value("'%s'!B%d" % (H1, K[k]), v)
        for k, v in esperado.items():
            n += 1
            x = xl2.evaluate("'%s'!B%d" % (H1, S[k]))
            if _distinto(x, v):
                err.append('%s: %s pycel %r ≠ esperado %r' % (nombre, k, x, v))
    # el selector de cliente cambia cobro, canon y cancelación
    e = dict(EJEMPLOS['Boda con barra tras la cena'])
    cs = [calcular(dict(e, canal=c)) for c in CANALES]
    if cs[0]['cb2'] == 0 or cs[1]['cb2'] != 0 or cs[1]['cb3'] == 0 or cs[2]['cb4'] == 0 or cs[0]['cb4'] != 0:
        err.append('el selector de cliente no cambia el cobro')
    # cobro: cada cliente suma el cien por cien y la señal coincide con el primer tramo del Particular
    for ic in range(3):
        s = sum(CANAL_TAB[k][2][ic] for k in ('pc_senal', 'pc_antes', 'pc_30d', 'pc_acto'))
        if abs(s - 1.0) > 1e-9:
            err.append('cobro %s suma %.2f ≠ 100 %%' % (CANALES[ic], s))
    # tramos de cancelación SIN huecos: cortes descendentes y porcentajes crecientes; cada día cae en un solo tramo
    for ic in (0, 1):
        d = [CANAL_TAB[k][2][ic] for k in ('d1', 'd2', 'd3')]
        v = [CANAL_TAB['cn%d' % i][2][ic] for i in (1, 2, 3, 4)]
        if not (d[0] > d[1] > d[2] > 0):
            err.append('cancelación %s: cortes no descendentes %r' % (CANALES[ic], d))
        if v != sorted(v) or v[-1] != 1.0:
            err.append('cancelación %s: tramos no crecientes %r' % (CANALES[ic], v))
        for dia in range(0, 400):
            tr = calcular(dict(base, canal=CANALES[ic], dias=dia))['tramo']
            esp = etiquetas(*d)[0 if dia >= d[0] else (1 if dia >= d[1] else (2 if dia >= d[2] else 3))]
            if tr != esp:
                err.append('cancelación %s: el día %d cae en %r, no en %r' % (CANALES[ic], dia, tr, esp))
                break
    if [CANAL_TAB['cn%d' % i][2][ic] for i in (1, 2, 3, 4) for ic in (0, 1)] != [0.10, 0.10, 0.30, 0.30, 0.60, 0.60, 1.0, 1.0]:
        err.append('cancelación: los porcentajes no son 10 / 30 / 60 / 100 (SPEC D16)')
    # Σ de la mezcla = 100 % (datos, Escandallo y fila de la hoja)
    if sum(b[1] for b in DE.BEBIDAS) != 100 or round(ESC['mz']['suma'], 9) != 1.0:
        err.append('la mezcla de bebidas no suma el cien por cien: %r' % ESC['mz']['suma'])
    if abs(sum(s for _n, s in DE.LECHES) - 1.0) > 1e-9:
        err.append('el reparto de leches no suma 1')
    for j, (nom, b) in enumerate(BEB.items()):
        if abs(sum(grid()[i][j] for i in range(1, 5)) - b[3]) > 1e-9:
            err.append('la leche de %s no suma %s ml' % (nom, b[3]))
    if abs(ESC['mz']['m_cafe'] - DE.cafe_g_medio()) > 1e-9 or abs(ESC['mz']['m_leche'] - DE.leche_ml_medio()) > 1e-9:
        err.append('café/leche medios del Escandallo ≠ datos_escalado')
    # coste medio de la bebida dentro del orden de magnitud del research (≈ 0,60 € de producto + ≈ 0,13 € de envase)
    if not 0.50 <= ESC['mz']['m_prod'] <= 0.75 or not 0.08 <= ESC['mz']['m_env'] <= 0.20:
        err.append('coste medio por bebida fuera del research: %.3f + %.3f' % (ESC['mz']['m_prod'], ESC['mz']['m_env']))
    if not 0.2 <= ESC['mz']['m_ticket'] <= 4:
        err.append('ticket medio fuera de rango')
    # semáforo: rojo con un food cost alto
    alto = calcular_escandallo(pvp=[0.5] * NB)
    if any(b['sem'] != FC_ALTO for b in alto['bebidas']) or any(b['sem'] != FC_OK for b in calcular_escandallo(pvp=[20.0] * NB)['bebidas']):
        err.append('el semáforo no distingue los tres estados')
    if motor.detectar(wf, FICHERO)['molde'] != 'calc-beta':
        err.append('motor.detectar no la reconoce como calc-beta')
    gf = motor.gate_formatos(wf, FICHERO)
    if gf:
        err.append('gate_formatos: %d celdas, p. ej. %r' % (len(gf), gf[:3]))
    # validaciones de datos
    ws = wf[H1]
    dvs = dict((str(rng), dv) for dv in ws.data_validations.dataValidation for rng in dv.sqref.ranges)
    c = 'B%d' % K['canal']
    if dvs.get(c) is None or dvs[c].type != 'list' or 'Particular,Empresa,Feria' not in (dvs[c].formula1 or ''):
        err.append('DV de lista incorrecta en %s' % c)
    for k in ('formato', 'horario', 'serv', 'elec'):
        c = 'B%d' % K[k]
        dv = dvs.get(c)
        if dv is None or dv.type != 'list' or not (dv.formula1 or '').startswith('=$A$'):
            err.append('DV de lista del rango incorrecta en %s' % c)
    dv = dvs.get('B%d' % CT['margen'])
    if dv is None or dv.formula2 != '0.8':
        err.append('DV del margen (máx. 80 %)')
    for k in ('guests', 'km', 'dias'):
        dv = dvs.get('B%d' % K[k])
        if dv is None or dv.type != 'whole':
            err.append('DV entera ausente en %s' % k)
    dve = dict((str(rng), dv) for dv in wf[HE].data_validations.dataValidation for rng in dv.sqref.ranges)
    for c in ('B%d' % E['obj'], '%s%d' % (BCOL[0], E_MIX), '%s%d' % (BCOL[0], E_I0 + 1)):
        if dve.get(c) is None:
            err.append('Escandallo: falta DV en %s' % c)
    # textos, protección, caché y verdes desbloqueadas
    textos = []
    for w in wf.worksheets:
        if w.page_setup.paperSize != 9 or not w.protection.sheet:
            err.append('%s: A4 y protección' % w.title)
        if w.protection.password:
            err.append('%s: protegida con contraseña' % w.title)
        for row in w.iter_rows():
            for c in row:
                v = c.value
                if isinstance(v, str) and c.data_type != 'f':
                    textos.append((w.title, c.coordinate, v))
                if c.data_type == 'f' and wv[w.title][c.coordinate].value is None:
                    err.append('%s!%s: fórmula sin caché' % (w.title, c.coordinate))
                if c.fill.fgColor.rgb in ('00E8F5E9', 'FFE8F5E9') and c.protection.locked:
                    err.append('%s!%s: verde bloqueada' % (w.title, c.coordinate))
    # ninguna tasa tecleada dentro de una fórmula: sólo constantes estructurales (0, 1, 2, 1000); los textos entre comillas no cuentan
    for w in wf.worksheets:
        for row in w.iter_rows():
            for c in row:
                if c.data_type == 'f':
                    sin = re.sub(r'"[^"]*"', '', str(c.value))
                    sin = re.sub(r"'[^']+'!|\$?[A-Z]{1,2}\$?\d+", '', sin)
                    for num in re.findall(r'(?<![A-Za-z])\d+\.?\d*', sin):
                        if num not in ('0', '1', '2', '1000'):
                            err.append('%s!%s: número tecleado %s en la fórmula %s' % (w.title, c.coordinate, num, c.value))
    todo = '\n'.join(t for _h, _c, t in textos)
    for rx in PROHIBIDOS:
        if re.search(rx, todo, re.I):
            err.append('prohibido /%s/' % rx)
    if re.search(r'[぀-ヿ㐀-䶿一-鿿가-힯Ѐ-ӿ؀-ۿ֐-׿฀-๿]', todo):
        err.append('caracteres no latinos')
    if re.search(r'\$|\bUSD\b', todo):
        err.append('restos del EN ($)')
    if motor.VERSION_FMT.format(pid=PID) not in todo or motor.BIO_LINE not in todo:
        err.append('falta la línea de versión o la bio')
    if 'Versión 1.0 · octubre 2026' not in todo:
        err.append('la versión no es «1.0 · octubre 2026»')
    if '16 A' not in todo or '3,7 kW' not in todo:
        err.append('falta el aviso de electricidad (16 A ≈ 3,7 kW)')
    if wf.sheetnames != [HE, H1, H2, H3]:
        err.append('pestañas %r' % wf.sheetnames)
    p = wf.properties
    if p.creator != 'AI Chef Pro' or p.lastModifiedBy != 'AI Chef Pro' or p.description != 'aichef.pro/%s' % PID or \
            p.keywords != 'plan negocio cafetería móvil eventos, AI Chef Pro':
        err.append('docProps: creator=%r description=%r keywords=%r' % (p.creator, p.description, p.keywords))
    for x in err:
        print('ERROR', x)
    print('autotest calculadora cafetería móvil ES: %d comprobaciones (pycel + caché en Escandallo, ejemplos y hoja principal; pycel en '
          '3 casos propios y en la tabla de escalado) · %s' % (n * 2, 'VERDE' if not err else 'ROJO (%d errores)' % len(err)))
    print('  Escandallo: coste medio %.3f € producto + %.3f € envase = %.3f € por bebida · ticket medio %.2f € · food cost %.1f %% · '
          'café %.2f g · leche %.1f ml' % (ESC['mz']['m_prod'], ESC['mz']['m_env'], ESC['mz']['m_tot'], ESC['mz']['m_ticket'],
                                           ESC['mz']['m_fc'] * 100, ESC['mz']['m_cafe'], ESC['mz']['m_leche']))
    for nombre, e in EJEMPLOS.items():
        r = calcular(e)
        print('  %-36s %4d beb · %d bar · %d caf · %6.2f €/inv sin IVA · %6.2f con IVA · %6.2f €/h · %5.2f €/bebida · total %9.2f · '
              'margen %.1f %%' % (nombre, r['bebidas'], r['baristas'], r['estaciones'], r['price'], r['price_iva'], r['price_h'],
                                  r['price_taza'], r['total'], r['margin_calc'] * 100))
        if e['canal'] == 'Feria':
            print('     feria: venta %.2f · canon %.2f · coste %.2f · resultado %.2f · equilibrio %d tazas' % (
                r['f_venta'], r['f_canon'], r['c_total'], r['f_result'], r['f_eq']))
    return 1 if err else 0


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--salida', required=True, help='carpeta de salida')
    ap.add_argument('--autotest', action='store_true')
    a = ap.parse_args()
    destino = os.path.join(a.salida, FICHERO)
    if not a.autotest and generar(destino):
        sys.exit('ERROR: fallos de pycel en inject_cache')
    sys.exit(autotest(destino))
