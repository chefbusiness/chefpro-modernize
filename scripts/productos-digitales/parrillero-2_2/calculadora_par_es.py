#!/usr/bin/env python3
"""
calculadora_par_es.py — Plan de Negocio Parrillero-Asador para Eventos ES 2.2 (SPEC D12): `calculadora-pricing-eventos-parrillero.xlsx`,
del coste de la carne y la brasa al precio por invitado y al presupuesto completo. Fork de `paellero-2_2/calculadora_pae_es.py`:
  · canal Particular / Empresa / Ayuntamiento (desplegable); el margen objetivo, el cobro y la cancelación de cada canal
    están en una tabla VISIBLE (nada de puntos tecleados dentro de una fórmula);
  · formato → gramos de carne cruda por invitado; experiencia (las 10 del kit + la chuletada de fiesta) → materia prima por
    invitado; estilo de servicio → invitados por parrillero y por ayudante;
  · logística por la TABLA DE ESCALADO (F1-research §2): kg de carne cruda y servida, parrillas, parrilleros, ayudantes y
    kg de carbón. La misma tabla va en el manual técnico (sección 8, `arreglos_d9.py` la importa de aquí);
  · personal a €/h × (1 + SS); IVA 10 %; desplazamiento ida y vuelta a 0,95 €/km en línea aparte SIN margen; suplemento de show de fuego en €/invitado;
  · cobro por canal (Particular 30/40/30, Empresa 30 + 70 a 30 días, Ayuntamiento 0 % de anticipo y pago a 30 días: LCSP art. 198);
  · cancelación por tramos SIN huecos (Particular 60/30-59/7-29/<7 · Empresa 30/15-29/7-14/<7);
  · margen bruto CALCULADO sobre el subtotal; 3 ejemplos por las mismas fórmulas; autotest pycel ± 0,01 €.
Hojas `Calculadora` · `Ejemplos` · `Instrucciones` (firma `calc-beta` de `motor.detectar`). A4, protegida sin contraseña,
verdes desbloqueadas. Corre en el VPS (openpyxl + pycel).

    /root/venv-guias/bin/python calculadora_par_es.py --salida <dir>      # genera + inject_cache + autotest
    /root/venv-guias/bin/python calculadora_par_es.py --salida <dir> --autotest

Sesión Claude Code, 12-oct-2026.
"""
import argparse
import math
import os
import re
import sys
from collections import OrderedDict

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill, Protection
from openpyxl.worksheet.datavalidation import DataValidation

AQUI = os.path.dirname(os.path.abspath(__file__))
PD = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(PD, 'planes-v2_0'))
import motor                                                                       # noqa: E402
import par_version                                                                 # noqa: E402,F401  (mes de versión: octubre 2026)

PID = 'plan-negocio-parrillero-asador-eventos'
FICHERO = 'calculadora-pricing-eventos-parrillero.xlsx'
TITULO = 'Calculadora de precios de parrillada y asado para eventos (de la carne al presupuesto)'
H1, H2, H3 = 'Calculadora', 'Ejemplos', 'Instrucciones'
VERDE = PatternFill('solid', fgColor='E8F5E9')
GRIS = PatternFill('solid', fgColor='F2F2F2')
FUENTE = 'Calibri'
CANALES = ['Particular', 'Empresa', 'Ayuntamiento']
EUR, ENT, PCT, DEC = '#,##0.00 €', '#,##0', '0%', '#,##0.0'

# ---------------------------------------------------------------------------------------------------------------------
# Tablas de datos (F1-research §2). Son la FUENTE ÚNICA: la calculadora las escribe en celdas verdes y el manual técnico
# (arreglos_d9.py) las importa para que su tabla de la sección 8 sea la misma.
# ---------------------------------------------------------------------------------------------------------------------
#: formato → gramos de carne cruda por invitado (con entrantes 350-450 g · sin entrantes 500-600 g · chuletada 300 g)
FORMATOS = OrderedDict([('Asado completo', 500), ('Plato principal', 400), ('Brunch', 200), ('Chuletada de fiesta', 300)])
#: experiencia → materia prima por invitado, sin IVA (research §2; la 11 sale del escandallo del caso de fiestas)
EXPERIENCIAS = OrderedDict([
    ('01 Asado argentino', 9.5), ('02 Asador a la cruz', 11.0), ('03 Parrilla uruguaya', 8.5), ('04 BBQ texano', 8.0),
    ('05 Rodizio brasileño', 8.5), ('06 Asador criollo-castellano', 11.0), ('07 Parrilla mediterránea', 9.0),
    ('08 Asador llanero', 6.5), ('09 Show de fuego (corte premium)', 14.0), ('10 Brunch parrillero corporativo', 5.5),
    ('11 Chuletada o costillada de fiesta', 2.5)])
#: estilo de servicio → (invitados por parrillero, invitados por ayudante)
SERVICIOS = OrderedDict([('Buffet', (70, 60)), ('Cortes en mesa', (45, 50)), ('Fiesta de volumen', (150, 100))])
#: reglas de escalado
REGLAS = OrderedDict([
    ('kg_parr', ('Carne cruda que asa una parrilla de 120 × 60 cm en un servicio (kg)', DEC, 32.0,
                 '12-15 kg por tanda y 2-3 tandas: se toma 13 kg × 2,5 tandas, que son 60-80 invitados con 400 g.')),
    ('carb_kg', ('Carbón por kg de carne cruda (kg)', DEC, 0.8,
                 'Entre 0,7 y 1 kg de carbón por kg de carne cruda: unos 0,3-0,45 kg por invitado. Para el asado a la '
                 'cruz suma 2-3 kg de leña por kg de carne.')),
    ('carb_p', ('Precio del carbón (€ por kg)', EUR, 1.5,
                'Tarifa profesional de 1,3 a 2,0 € por kg (encina, marabú o quebracho; saco de 15 kg).')),
    ('merma', ('Merma de cocción (de crudo a servido)', PCT, 0.30,
               'Vacuno y cerdo a la brasa pierden el 25-35 %; el brisket ahumado, el 40-50 %.')),
    ('ayud_desde', ('Ayudante desde (invitados)', ENT, 40,
                    'Por debajo de este número de invitados el parrillero trabaja sin ayudante.')),
])
#: política por canal: Particular · Empresa · Ayuntamiento
CANAL_TAB = OrderedDict([
    ('margen', ('Margen bruto objetivo sobre el subtotal', (0.42, 0.40, 0.40),
                'Parte del subtotal que queda tras los costes directos. Estimación del kit: la boda particular lleva más '
                'margen que la empresa; el ayuntamiento paga por volumen.')),
    ('pc_senal', ('Cobro: señal al firmar (% del total)', (0.30, 0.30, 0.0),
                  'Particular y Empresa, el 30 % al firmar. Un ayuntamiento no anticipa: compra por contrato menor.')),
    ('pc_d7', ('Cobro: pago a siete días del evento (% del total)', (0.40, 0.0, 0.0), 'Sólo el contrato Particular.')),
    ('pc_48h', ('Cobro: pago a las 48 horas del evento (% del total)', (0.30, 0.0, 0.0), 'Sólo el contrato Particular.')),
    ('pc_30d', ('Cobro: pago a 30 días de la factura (% del total)', (0.0, 0.70, 1.0),
                'Empresa, el 70 % restante; Ayuntamiento, el 100 % desde la conformidad (art. 198.4 de la Ley 9/2017).')),
    ('cn1', ('Cancelación tramo 1 (% del total que retienes)', (0.30, 0.20, 0.0),
             'Particular: 60 días o más, retienes la señal (el 30 %). Empresa: 30 días o más, el 20 % del pedido.')),
    ('cn2', ('Cancelación tramo 2 (% del total que retienes)', (0.50, 0.50, 0.0),
             'Particular: de 30 a 59 días. Empresa: de 15 a 29 días.')),
    ('cn3', ('Cancelación tramo 3 (% del total que retienes)', (0.75, 0.75, 0.0),
             'Particular: de 7 a 29 días. Empresa: de 7 a 14 días.')),
    ('cn4', ('Cancelación tramo 4 (% del total que retienes)', (1.0, 1.0, 0.0),
             'Particular y Empresa: con menos de 7 días o no presentación, el 100 %. A un ayuntamiento no se le aplican '
             'estos tramos: se rige por su pliego o su contrato menor.')),
])

ENTRADAS = [
    ('canal', 'Cliente', '@', 'Particular',
     'Particular, Empresa o Ayuntamiento: cambian el margen objetivo, el cobro y los tramos de cancelación (tabla del '
     'final). Las comisiones de fiestas y las peñas cuentan como Empresa.'),
    ('guests', 'Invitados previstos', ENT, 100, 'Número entero de invitados a los que sirves.'),
    ('formato', 'Formato del servicio', '@', 'Asado completo',
     'Fija los gramos de carne cruda por invitado con la tabla del final. No cambia el precio: la materia prima de la '
     'experiencia ya trae su carta habitual.'),
    ('exper', 'Experiencia', '@', '01 Asado argentino',
     'Las 10 experiencias del kit y la chuletada de fiesta: fijan la materia prima por invitado con la tabla del final.'),
    ('servicio', 'Estilo de servicio', '@', 'Cortes en mesa',
     'Buffet: un parrillero por cada 60-80 invitados. Cortes en mesa: uno por cada 40-50.'),
    ('beb', 'Bebida por invitado (coste)', EUR, 4.0,
     'Cerveza, refrescos y vino que pones tú. 0 si la bebida la pone el cliente.'),
    ('menaje', 'Coste de menaje, desechables y consumibles por invitado', EUR, 0.60,
     'Estimación del kit: platos y cubiertos compostables, aluminio, pan y hielo. Pon 0 si el cliente pone el menaje.'),
    ('hours', 'Horas por persona (carga, viaje, montaje, brasa, servicio y recogida)', DEC, 9,
     'Estimación del kit: pon las horas reales de tu equipo.'),
    ('wage', 'Coste bruto por hora del personal', EUR, 13.0,
     'Estimación del kit. Copia tu convenio provincial de hostelería.'),
    ('ss', 'Seguridad Social a cargo de la empresa', PCT, 0.33,
     '30,65 % de contingencias, desempleo, FOGASA, formación y MEI, más AT/EP (fijos discontinuos, art. 16 ET).'),
    ('rentals', 'Importe de alquileres repercutidos (carpa, mesas, sillas, parrilla extra)', EUR, 400.0,
     'Lo que te cobra el alquilador para este evento. Si lo facturas aparte sin ser accesorio, ese importe va al 21 % '
     'de IVA.'),
    ('km', 'Kilómetros de ida (cocina de apoyo → espacio)', ENT, 35, 'Se cobran ida y vuelta, en una línea aparte.'),
    ('per_km', 'Tarifa por kilómetro de desplazamiento', EUR, 0.95,
     'La del contrato del kit: se cobra ida y vuelta y va sin margen.'),
    ('show', 'Importe del suplemento de show de fuego por invitado', EUR, 0.0,
     'De 8 a 15 € por invitado si abres con provoletas y chorizos flambeados a la vista (experiencia 09). 0 si no hay show. '
     'Se suma al precio sin margen objetivo: cubre su materia prima extra y el tiempo del parrillero.'),
    ('iva', 'IVA del servicio de comidas', PCT, 0.10,
     'Ley 37/1992, art. 91.Uno.2.2.º: comida y bebida para consumir en el acto, alcohol incluido. Lo que facturas '
     'aparte sin ser accesorio (carpa, mobiliario) va al 21 %.'),
]
K = OrderedDict((k, 5 + i) for i, (k, *_r) in enumerate(ENTRADAS))
F_CALC = 5 + len(ENTRADAS) + 1

# nombre, rótulo, formato, expresión, nota. {x}: celda de la entrada/salida; {g_tab} etc.: búsquedas en las tablas
SALIDAS = [
    ('gramos', 'Carne cruda por invitado (g, de la tabla)', ENT, '{t_gramos}', 'Busca el formato en la tabla del final.'),
    ('mp', 'Coste de materia prima por invitado de la experiencia (tabla)', EUR, '{t_mp}',
     'Busca la experiencia en la tabla del final. Cámbiala si tu escandallo es otro.'),
    ('ipp', 'Invitados por parrillero (del estilo de servicio)', ENT, '{t_ipp}', ''),
    ('ipa', 'Invitados por ayudante (del estilo de servicio)', ENT, '{t_ipa}', ''),
    ('margen', 'Margen objetivo del cliente elegido', PCT, '{t_margen}', 'De la tabla por cliente del final.'),
    ('kg_crudo', 'Carne cruda total (kg)', DEC, '{guests}*{gramos}/1000', 'Invitados × gramos por invitado.'),
    ('kg_servida', 'Carne servida total (kg)', DEC, '{kg_crudo}*(1-{r_merma})', 'Carne cruda menos la merma de cocción.'),
    ('parrillas', 'Parrillas necesarias', ENT, 'MAX(1,ROUNDUP({kg_crudo}/{r_kg_parr},0))',
     'Carne cruda entre lo que asa una parrilla de 120 × 60 cm, hacia arriba. Si no las tienes, alquílalas.'),
    ('parrilleros', 'Parrilleros necesarios', ENT, 'MAX(1,ROUNDUP({guests}/{ipp},0))',
     'Invitados entre invitados por parrillero, hacia arriba.'),
    ('ayudantes', 'Ayudantes necesarios', ENT, 'IF({guests}<{r_ayud_desde},0,ROUNDUP({guests}/{ipa},0))',
     'Desde el mínimo de invitados de la tabla; el resto, invitados entre invitados por ayudante, hacia arriba.'),
    ('kg_carbon', 'Carbón total (kg)', DEC, '{kg_crudo}*{r_carb_kg}', 'Kg de carne cruda × kg de carbón por kg de carne.'),
    ('c_mp', 'Coste de materia prima', EUR, '{mp}*{guests}', ''),
    ('c_beb', 'Coste de bebida', EUR, '{beb}*{guests}', ''),
    ('c_menaje', 'Coste de menaje, desechables y consumibles', EUR, '{menaje}*{guests}', ''),
    ('c_carbon', 'Coste del carbón', EUR, '{kg_carbon}*{r_carb_p}', ''),
    ('c_staff', 'Coste de personal (salario + Seguridad Social)', EUR,
     '({parrilleros}+{ayudantes})*{hours}*{wage}*(1+{ss})',
     'Parrilleros y ayudantes. Si el dueño cocina, se cuenta a precio de hora: es su coste de oportunidad.'),
    ('c_rent', 'Importe de alquileres', EUR, '{rentals}', ''),
    ('c_total', 'Coste directo total', EUR, '{c_mp}+{c_beb}+{c_menaje}+{c_carbon}+{c_staff}+{c_rent}', ''),
    ('c_guest', 'Coste directo por invitado', EUR, '{c_total}/{guests}', ''),
    ('price', 'PRECIO POR INVITADO SIN IVA', EUR, 'ROUNDUP({c_total}/(1-{margen})/{guests}*2,0)/2+{show}',
     'Coste ÷ (1 − margen) ÷ invitados, redondeado a los 0,50 € de arriba, más el suplemento de show. Es el precio de '
     'las empresas («+ IVA»).'),
    ('price_iva', 'PRECIO POR INVITADO CON IVA', EUR, '{price}*(1+{iva})',
     'Es el que ve un particular: en una oferta a consumidores el precio va con impuestos incluidos.'),
    ('subtotal', 'Subtotal de comida sin IVA', EUR, '{price}*{guests}', 'Precio por invitado × invitados.'),
    ('desp', 'Desplazamiento (ida y vuelta, sin margen)', EUR, '{km}*2*{per_km}', 'Línea aparte del presupuesto.'),
    ('base', 'Base imponible', EUR, '{subtotal}+{desp}', ''),
    ('iva_amt', 'IVA', EUR, '{base}*{iva}', ''),
    ('total', 'TOTAL DEL PRESUPUESTO (con IVA)', EUR, '{base}+{iva_amt}', ''),
    ('cb1', 'Importe del cobro 1: señal al firmar', EUR, '{total}*{t_pc_senal}', 'Con la firma del contrato; en un ayuntamiento, nada.'),
    ('cb2', 'Importe del cobro 2: a siete días del evento', EUR, '{total}*{t_pc_d7}', 'Sólo el contrato Particular.'),
    ('cb3', 'Importe del cobro 3: a las 48 horas del evento', EUR, '{total}*{t_pc_48h}', 'Sólo el contrato Particular.'),
    ('cb4', 'Importe del cobro 4: a 30 días de la factura', EUR, '{total}*{t_pc_30d}',
     'Empresa: el resto. Ayuntamiento: todo, desde la conformidad. Factura de cada pago, también de la señal.'),
    ('profit', 'Margen bruto en euros', EUR, '{subtotal}-{c_total}', 'Sobre el subtotal de comida, sin el desplazamiento.'),
    ('margin_calc', 'Margen bruto (calculado)', '0.0%', 'IF({subtotal}=0,0,{profit}/{subtotal})',
     'Sale de los costes, nunca se teclea. Queda igual o por encima del objetivo por el redondeo del precio y el show.'),
    ('can1', 'Importe retenido si cancela: tramo 1', EUR, '{total}*{t_cn1}',
     'Particular: 60 días o más. Empresa: 30 días o más.'),
    ('can2', 'Importe retenido si cancela: tramo 2', EUR, '{total}*{t_cn2}',
     'Particular: de 30 a 59 días. Empresa: de 15 a 29 días.'),
    ('can3', 'Importe retenido si cancela: tramo 3', EUR, '{total}*{t_cn3}',
     'Particular: de 7 a 29 días. Empresa: de 7 a 14 días.'),
    ('can4', 'Importe retenido si cancela: tramo 4', EUR, '{total}*{t_cn4}',
     'Particular y Empresa: menos de 7 días o no presentación.'),
]
S = OrderedDict((k, F_CALC + 1 + i) for i, (k, *_r) in enumerate(SALIDAS))

# --- bloques del pie (tablas) ---------------------------------------------------------------------------------------
F_REGLAS = F_CALC + 1 + len(SALIDAS) + 1                       # cabecera del bloque de reglas
R = OrderedDict((k, F_REGLAS + 1 + i) for i, k in enumerate(REGLAS))
F_SERV = F_REGLAS + 1 + len(REGLAS) + 1
F_FORM = F_SERV + 1 + len(SERVICIOS) + 1
F_EXP = F_FORM + 1 + len(FORMATOS) + 1
F_CAN = F_EXP + 1 + len(EXPERIENCIAS) + 1
CT = OrderedDict((k, F_CAN + 1 + i) for i, k in enumerate(CANAL_TAB))
F_ESC = F_CAN + 1 + len(CANAL_TAB) + 1
#: tamaños de la tabla de escalado de referencia (la del manual): 4 columnas
TAM_REF = (40, 80, 150, 300)
#: referencia de la tabla de escalado: plato principal, estilo Buffet
REF_FORMATO, REF_SERVICIO = 'Plato principal', 'Buffet'
ESC_FILAS = ['Carne cruda (kg)', 'Carne servida (kg)', 'Parrillas', 'Parrilleros', 'Ayudantes', 'Carbón (kg)']

EJEMPLOS = OrderedDict([
    ('Boda particular con cortes en mesa', dict(
        canal='Particular', guests=110, formato='Asado completo', exper='01 Asado argentino', servicio='Cortes en mesa',
        beb=5.0, menaje=0.60, hours=9, wage=13.0, ss=0.33, rentals=0.0, km=35, per_km=0.95, show=0.0, iva=0.10)),
    ('Team building de empresa con BBQ texano', dict(
        canal='Empresa', guests=70, formato='Plato principal', exper='04 BBQ texano', servicio='Buffet',
        beb=3.0, menaje=0.60, hours=8, wage=13.0, ss=0.33, rentals=0.0, km=25, per_km=0.95, show=0.0, iva=0.10)),
    ('Fiesta o feria municipal de volumen', dict(
        canal='Ayuntamiento', guests=300, formato='Chuletada de fiesta', exper='11 Chuletada o costillada de fiesta',
        servicio='Fiesta de volumen', beb=0.0, menaje=0.40, hours=9, wage=13.0, ss=0.33, rentals=0.0, km=30,
        per_km=0.95, show=0.0, iva=0.10)),
])
EJ_NOTAS = OrderedDict([
    ('Boda particular con cortes en mesa', 'Particular, 110 invitados (la boda del caso del plan financiero), asado argentino de 500 g de carne cruda por '
     'invitado con cortes en mesa, bebida con vino incluida (5 €). Sin show: con él, súmale de 8 a 15 € por invitado. El precio con IVA es el que ve el particular; cobro en tres '
     'pagos (30 % al firmar, 40 % a siete días, 30 % a las 48 horas).'),
    ('Team building de empresa con BBQ texano', 'Empresa, 70 invitados, BBQ texano en buffet con 400 g de carne cruda, '
     'refrescos y cerveza incluidos y presupuesto «+ IVA». Cobro del 30 % al firmar y el 70 % a 30 días de la factura; '
     'los tramos de cancelación son los del contrato B2B.'),
    ('Fiesta o feria municipal de volumen', '300 invitados en una chuletada de 300 g por persona con servicio de '
     'volumen: el precio queda cerca de los 10 € por invitado. Sin anticipo: el ayuntamiento paga a 30 días desde la '
     'conformidad (art. 198.4 de la Ley 9/2017) y los tramos de cancelación de los contratos del kit no se le aplican '
     '(contrata con su pliego o su contrato menor). Tres parrillas: las dos del kit y el remolque.'),
])


# ---------------------------------------------------------------------------------------------------------------------
# Cálculo en Python (espejo de las fórmulas) — la fuente del autotest y de la tabla del manual
# ---------------------------------------------------------------------------------------------------------------------
def _ceil(x):
    return math.ceil(round(x, 9))


def escalar(guests, gramos, servicio, reglas=None):
    """Tabla de escalado: (kg crudo, kg servida, parrillas, parrilleros, ayudantes, kg carbón)."""
    r = dict((k, v[2]) for k, v in REGLAS.items())
    if reglas:
        r.update(reglas)
    ipp, ipa = SERVICIOS[servicio]
    kg = guests * gramos / 1000.0
    return (kg, kg * (1 - r['merma']), max(1, _ceil(kg / r['kg_parr'])), max(1, _ceil(guests / ipp)),
            0 if guests < r['ayud_desde'] else _ceil(guests / ipa), kg * r['carb_kg'])


def tabla_escalado():
    """Filas de la tabla de referencia (plato principal, buffet): [(invitados, kg crudo, kg servida, parrillas,
    parrilleros, ayudantes, kg carbón)]."""
    return [(n,) + escalar(n, FORMATOS[REF_FORMATO], REF_SERVICIO) for n in TAM_REF]


def calcular(e):
    r = OrderedDict()
    ic = CANALES.index(e['canal'])
    t = lambda k: CANAL_TAB[k][1][ic]
    reg = dict((k, v[2]) for k, v in REGLAS.items())
    r['gramos'] = FORMATOS[e['formato']]
    r['mp'] = EXPERIENCIAS[e['exper']]
    r['ipp'], r['ipa'] = SERVICIOS[e['servicio']]
    r['margen'] = t('margen')
    r['kg_crudo'] = e['guests'] * r['gramos'] / 1000.0
    r['kg_servida'] = r['kg_crudo'] * (1 - reg['merma'])
    r['parrillas'] = max(1, _ceil(r['kg_crudo'] / reg['kg_parr']))
    r['parrilleros'] = max(1, _ceil(e['guests'] / r['ipp']))
    r['ayudantes'] = 0 if e['guests'] < reg['ayud_desde'] else _ceil(e['guests'] / r['ipa'])
    r['kg_carbon'] = r['kg_crudo'] * reg['carb_kg']
    r['c_mp'] = r['mp'] * e['guests']
    r['c_beb'] = e['beb'] * e['guests']
    r['c_menaje'] = e['menaje'] * e['guests']
    r['c_carbon'] = r['kg_carbon'] * reg['carb_p']
    r['c_staff'] = (r['parrilleros'] + r['ayudantes']) * e['hours'] * e['wage'] * (1 + e['ss'])
    r['c_rent'] = e['rentals']
    r['c_total'] = r['c_mp'] + r['c_beb'] + r['c_menaje'] + r['c_carbon'] + r['c_staff'] + r['c_rent']
    r['c_guest'] = r['c_total'] / e['guests']
    r['price'] = _ceil(r['c_total'] / (1 - r['margen']) / e['guests'] * 2) / 2 + e['show']
    r['price_iva'] = r['price'] * (1 + e['iva'])
    r['subtotal'] = r['price'] * e['guests']
    r['desp'] = e['km'] * 2 * e['per_km']
    r['base'] = r['subtotal'] + r['desp']
    r['iva_amt'] = r['base'] * e['iva']
    r['total'] = r['base'] + r['iva_amt']
    r['cb1'] = r['total'] * t('pc_senal')
    r['cb2'] = r['total'] * t('pc_d7')
    r['cb3'] = r['total'] * t('pc_48h')
    r['cb4'] = r['total'] * t('pc_30d')
    r['profit'] = r['subtotal'] - r['c_total']
    r['margin_calc'] = 0 if r['subtotal'] == 0 else r['profit'] / r['subtotal']
    for i in (1, 2, 3, 4):
        r['can%d' % i] = r['total'] * t('cn%d' % i)
    return r


# ---------------------------------------------------------------------------------------------------------------------
# Fórmulas
# ---------------------------------------------------------------------------------------------------------------------
def _rng(col, f1, f2):
    return "'%s'!$%s$%d:$%s$%d" % (H1, col, f1, col, f2)


def refs(col):
    """Referencias a celdas de la columna `col` (B en Calculadora; B/C/D en Ejemplos) + búsquedas en las tablas."""
    ref = dict((k, '$%s$%d' % (col, f)) for k, f in K.items())
    ref.update((k, '$%s$%d' % (col, f)) for k, f in S.items())
    ref['t_gramos'] = 'INDEX(%s,MATCH(%s,%s,0))' % (_rng('B', F_FORM + 1, F_FORM + len(FORMATOS)), ref['formato'],
                                                    _rng('A', F_FORM + 1, F_FORM + len(FORMATOS)))
    ref['t_mp'] = 'INDEX(%s,MATCH(%s,%s,0))' % (_rng('B', F_EXP + 1, F_EXP + len(EXPERIENCIAS)), ref['exper'],
                                                _rng('A', F_EXP + 1, F_EXP + len(EXPERIENCIAS)))
    for k, c in (('t_ipp', 'B'), ('t_ipa', 'C')):
        ref[k] = 'INDEX(%s,MATCH(%s,%s,0))' % (_rng(c, F_SERV + 1, F_SERV + len(SERVICIOS)), ref['servicio'],
                                               _rng('A', F_SERV + 1, F_SERV + len(SERVICIOS)))
    for k, f in R.items():
        ref['r_' + k] = "'%s'!$B$%d" % (H1, f)
    cab = "'%s'!$B$%d:$D$%d" % (H1, F_CAN, F_CAN)
    for k, f in CT.items():
        ref['t_' + k] = "INDEX('%s'!$B$%d:$D$%d,MATCH(%s,%s,0))" % (H1, f, f, ref['canal'], cab)
    return ref


def a_excel(expr, ref):
    return re.sub(r'\{(\w+)\}', lambda m: ref[m.group(1)], expr)


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


def _nota(ws, fila, texto):
    """Nota combinada en C:F (ancho útil ≈ 110 caracteres)."""
    if not texto:
        return
    _f(ws, 'C%d' % fila, texto, wrap=True)
    ws.merge_cells('C%d:F%d' % (fila, fila))
    ws.row_dimensions[fila].height = max(16, 15 * math.ceil(len(texto) / 105.0))


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


def hoja_calculadora(wb):
    ws = wb.active
    ws.title = H1
    for col, w in (('A', 66), ('B', 20), ('C', 17), ('D', 17), ('E', 17), ('F', 56)):
        ws.column_dimensions[col].width = w
    _f(ws, 'A1', 'CALCULADORA DE PRECIOS DE PARRILLADA Y ASADO PARA EVENTOS — DE LA CARNE AL PRESUPUESTO', b=True, sz=14)
    _f(ws, 'A2', 'Escribe sólo en las celdas VERDES: todo lo demás se calcula. Importes sin IVA salvo donde la fila '
                 'diga lo contrario. Los valores por defecto son estimaciones del kit: cámbialos por los tuyos.',
       wrap=True)
    ws.merge_cells('A2:F2')
    ws.row_dimensions[2].height = 32
    for col, t in zip('ABC', ('DATOS DEL EVENTO', 'Valor', 'Notas')):
        _f(ws, '%s4' % col, t, b=True, fill=GRIS)
    for k, rot, fmt, val, nota in ENTRADAS:
        f = K[k]
        _f(ws, 'A%d' % f, rot)
        _f(ws, 'B%d' % f, val, fmt=fmt if fmt != '@' else None, fill=VERDE, locked=False)
        _nota(ws, f, nota)
    for col, t in zip('ABC', ('CÁLCULO', 'Valor', 'Notas')):
        _f(ws, '%s%d' % (col, F_CALC), t, b=True, fill=GRIS)
    ref = refs('B')
    for k, rot, fmt, expr, nota in SALIDAS:
        f = S[k]
        neg = k in ('price', 'price_iva', 'total', 'margin_calc')
        _f(ws, 'A%d' % f, rot, b=neg)
        _f(ws, 'B%d' % f, '=' + a_excel(expr, ref), fmt=fmt, b=neg)
        _nota(ws, f, nota)
    # reglas de escalado
    _f(ws, 'A%d' % F_REGLAS, 'REGLAS DE ESCALADO (tabla de la sección 8 del manual técnico del kit)', b=True, fill=GRIS)
    _f(ws, 'B%d' % F_REGLAS, 'Valor', b=True, fill=GRIS)
    for k, (rot, fmt, val, nota) in REGLAS.items():
        _f(ws, 'A%d' % R[k], rot)
        _f(ws, 'B%d' % R[k], val, fmt=fmt, fill=VERDE, locked=False)
        _nota(ws, R[k], nota)
    # estilo de servicio
    _f(ws, 'A%d' % F_SERV, 'ESTILO DE SERVICIO → PERSONAL', b=True, fill=GRIS)
    _f(ws, 'B%d' % F_SERV, 'Invitados por parrillero', b=True, fill=GRIS, wrap=True)
    _f(ws, 'C%d' % F_SERV, 'Invitados por ayudante', b=True, fill=GRIS, wrap=True)
    ws.row_dimensions[F_SERV].height = 32
    for i, (nombre, (ipp, ipa)) in enumerate(SERVICIOS.items(), 1):
        _f(ws, 'A%d' % (F_SERV + i), nombre)
        _f(ws, 'B%d' % (F_SERV + i), ipp, fmt=ENT, fill=VERDE, locked=False)
        _f(ws, 'C%d' % (F_SERV + i), ipa, fmt=ENT, fill=VERDE, locked=False)
    _f(ws, 'D%d' % (F_SERV + 1), 'Buffet: 60-80 invitados por parrillero. Cortes en mesa: 40-50. Fiesta de volumen: '
                                 'estimación del kit.', i=True, wrap=True)
    ws.merge_cells('D%d:F%d' % (F_SERV + 1, F_SERV + 2))
    # formato
    _f(ws, 'A%d' % F_FORM, 'FORMATO → CARNE CRUDA POR INVITADO', b=True, fill=GRIS)
    _f(ws, 'B%d' % F_FORM, 'Gramos', b=True, fill=GRIS)
    for i, (nombre, g) in enumerate(FORMATOS.items(), 1):
        _f(ws, 'A%d' % (F_FORM + i), nombre)
        _f(ws, 'B%d' % (F_FORM + i), g, fmt=ENT, fill=VERDE, locked=False)
    _f(ws, 'C%d' % (F_FORM + 1), 'Asado sin entrantes: 500-600 g. Con entrantes: 350-450 g. Chuletada de fiesta: 300 g. '
                                 'Brunch: estimación del kit. Sin hueso, un 20 % menos; los niños, la mitad.', i=True,
       wrap=True)
    ws.merge_cells('C%d:F%d' % (F_FORM + 1, F_FORM + 3))
    # experiencia
    _f(ws, 'A%d' % F_EXP, 'EXPERIENCIA → MATERIA PRIMA POR INVITADO (sin IVA, sin bebida)', b=True, fill=GRIS)
    _f(ws, 'B%d' % F_EXP, 'Euros', b=True, fill=GRIS)
    for i, (nombre, mp) in enumerate(EXPERIENCIAS.items(), 1):
        _f(ws, 'A%d' % (F_EXP + i), nombre)
        _f(ws, 'B%d' % (F_EXP + i), mp, fmt=EUR, fill=VERDE, locked=False)
    _f(ws, 'C%d' % (F_EXP + 1), 'Estimación del kit con precios de mayorista de 2025-2026 (lomo bajo de vaca, '
                                'entraña, picanha, costilla, ibérico). La 11 no es de las 10 experiencias: sale del '
                                'escandallo del caso de fiestas. Cambia la cifra por tu escandallo.', i=True, wrap=True)
    ws.merge_cells('C%d:F%d' % (F_EXP + 1, F_EXP + 4))
    # por cliente
    _f(ws, 'A%d' % F_CAN, 'POLÍTICA POR CLIENTE', b=True, fill=GRIS)
    for col, c in zip('BCD', CANALES):
        _f(ws, '%s%d' % (col, F_CAN), c, b=True, fill=GRIS, wrap=True)
    for k, (rot, vals, nota) in CANAL_TAB.items():
        f = CT[k]
        _f(ws, 'A%d' % f, rot)
        for col, v in zip('BCD', vals):
            _f(ws, '%s%d' % (col, f), v, fmt=PCT, fill=VERDE, locked=False)
        _f(ws, 'E%d' % f, nota, wrap=True)
        ws.merge_cells('E%d:F%d' % (f, f))
        ws.row_dimensions[f].height = max(16, 15 * math.ceil(len(nota) / 62.0))
    # tabla de escalado de referencia
    _f(ws, 'A%d' % F_ESC, 'TABLA DE ESCALADO (plato principal de %d g, estilo Buffet)' % FORMATOS[REF_FORMATO],
       b=True, fill=GRIS)
    for col, n in zip('BCDE', TAM_REF):
        _f(ws, '%s%d' % (col, F_ESC), n, b=True, fill=GRIS, fmt='0" inv."')
    refd = dict(('r_' + k, "$B$%d" % f) for k, f in R.items())
    g = '$B$%d' % (F_FORM + 1 + list(FORMATOS).index(REF_FORMATO))
    ipp = '$B$%d' % (F_SERV + 1 + list(SERVICIOS).index(REF_SERVICIO))
    ipa = '$C$%d' % (F_SERV + 1 + list(SERVICIOS).index(REF_SERVICIO))
    for j, rot in enumerate(ESC_FILAS):
        f = F_ESC + 1 + j
        _f(ws, 'A%d' % f, rot)
        for col in 'BCDE':
            n = '%s$%d' % (col, F_ESC)
            kg = '%s*%s/1000' % (n, g)
            expr = [kg, '%s*(1-%s)' % (kg, refd['r_merma']), 'MAX(1,ROUNDUP(%s/%s,0))' % (kg, refd['r_kg_parr']),
                    'MAX(1,ROUNDUP(%s/%s,0))' % (n, ipp),
                    'IF(%s<%s,0,ROUNDUP(%s/%s,0))' % (n, refd['r_ayud_desde'], n, ipa),
                    '%s*%s' % (kg, refd['r_carb_kg'])][j]
            _f(ws, '%s%d' % (col, f), '=' + expr, fmt=DEC if j in (0, 1, 5) else ENT)
    f = F_ESC + 1 + len(ESC_FILAS)
    _f(ws, 'A%d' % f, 'Es la misma tabla que la sección 8 del manual técnico. Una parrilla de 120 × 60 cm asa 12-15 kg por '
                      'tanda; un parrillero atiende 60-80 invitados en buffet y 40-50 con cortes en mesa; el ayudante '
                      'entra desde 40 invitados.', i=True, wrap=True)
    ws.merge_cells('A%d:F%d' % (f, f))
    ws.row_dimensions[f].height = 32
    # validaciones
    ref = refs('B')
    _dv(ws, 'list', [ref['canal'].replace('$', '')], f1='"%s"' % ','.join(CANALES), titulo='Cliente no válido',
        msg='Elige Particular, Empresa o Ayuntamiento.')
    _dv(ws, 'list', [ref['formato'].replace('$', '')], f1='=$A$%d:$A$%d' % (F_FORM + 1, F_FORM + len(FORMATOS)),
        titulo='Formato no válido', msg='Elige un formato de la lista.')
    _dv(ws, 'list', [ref['exper'].replace('$', '')], f1='=$A$%d:$A$%d' % (F_EXP + 1, F_EXP + len(EXPERIENCIAS)),
        titulo='Experiencia no válida', msg='Elige una experiencia de la lista.')
    _dv(ws, 'list', [ref['servicio'].replace('$', '')], f1='=$A$%d:$A$%d' % (F_SERV + 1, F_SERV + len(SERVICIOS)),
        titulo='Estilo no válido', msg='Elige un estilo de servicio de la lista.')
    _dv(ws, 'whole', ['B%d' % K['guests']], f1='1', f2='100000', op='between', titulo='Número no válido',
        msg='Escribe un número entero de 1 o más.')
    _dv(ws, 'whole', ['B%d' % K['km'], 'B%d' % R['ayud_desde']] + ['B%d' % (F_SERV + i) for i in range(1, 4)]
        + ['C%d' % (F_SERV + i) for i in range(1, 4)] + ['B%d' % (F_FORM + i) for i in range(1, 5)],
        f1='0', f2='100000', op='between', titulo='Número no válido', msg='Escribe un número entero de 0 o más.')
    _dv(ws, 'decimal', ['B%d' % K[k] for k in ('beb', 'menaje', 'hours', 'wage', 'rentals', 'per_km', 'show')]
        + ['B%d' % R['kg_parr'], 'B%d' % R['carb_kg'], 'B%d' % R['carb_p']]
        + ['B%d' % (F_EXP + i) for i in range(1, len(EXPERIENCIAS) + 1)],
        f1='0', op='greaterThanOrEqual', titulo='Importe no válido', msg='Escribe un número mayor o igual que 0.')
    _dv(ws, 'decimal', ['B%d' % K[k] for k in ('ss', 'iva')] + ['B%d' % R['merma']]
        + ['%s%d' % (c, CT[k]) for k in CANAL_TAB if k != 'margen' for c in 'BCD'],
        f1='0', f2='1', op='between', titulo='Porcentaje no válido', msg='Escribe un porcentaje entre 0 y 1 (0,10 = 10 %).')
    _dv(ws, 'decimal', ['%s%d' % (c, CT['margen']) for c in 'BCD'], f1='0', f2='0.95', op='between',
        titulo='Porcentaje no válido', msg='Escribe un margen objetivo entre 0 y 95 % (0,40 = 40 %).')
    ws.freeze_panes = 'A5'
    _imprimir(ws)


def hoja_ejemplos(wb):
    ws = wb.create_sheet(H2)
    ws.column_dimensions['A'].width = 66
    for col in 'BCD':
        ws.column_dimensions[col].width = 28
    _f(ws, 'A1', '3 PRESUPUESTOS DE EJEMPLO — con las mismas fórmulas de la hoja «%s»' % H1, b=True, sz=14)
    _f(ws, 'A2', 'Estimaciones del kit para ilustrar el cálculo, no precios de mercado: cambia los datos en «%s» '
                 'para presupuestar tus eventos. Las tablas (margen y cobro por cliente, materia prima, escalado) están '
                 'al final de esa hoja y también mueven estos ejemplos.' % H1, wrap=True)
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
    for k, rot, fmt, expr, nota in SALIDAS:
        neg = k in ('price', 'price_iva', 'total', 'margin_calc')
        _f(ws, 'A%d' % S[k], rot, b=neg)
        for j in range(3):
            col = 'BCD'[j]
            _f(ws, '%s%d' % (col, S[k]), '=' + a_excel(expr, refs(col)), fmt=fmt, b=neg)
    f = S[SALIDAS[-1][0]] + 2
    _f(ws, 'A%d' % f, 'QUÉ ENSEÑA CADA EJEMPLO', b=True, fill=GRIS)
    for j, (nombre, nota) in enumerate(EJ_NOTAS.items()):
        _f(ws, 'A%d' % (f + 1 + j), nombre, b=True, wrap=True)
        _f(ws, 'B%d' % (f + 1 + j), nota, wrap=True)
        ws.merge_cells('B%d:D%d' % (f + 1 + j, f + 1 + j))
        ws.row_dimensions[f + 1 + j].height = 15 * max(3, math.ceil(len(nota) / 80.0))
    ws.freeze_panes = 'B5'
    _imprimir(ws, horizontal=True)


INSTRUCCIONES = [
    ('INSTRUCCIONES DE USO — Calculadora de precios de parrillada y asado para eventos', True),
    ('Convierte tu escandallo en un precio por invitado y en un presupuesto completo: kilos de carne, parrillas, '
     'parrilleros, ayudantes y carbón, subtotal, IVA, total, cobro por pagos y lo que retienes si el cliente cancela. '
     'Sólo se escribe en las celdas VERDES; el margen se calcula.', False),
    ('1. Elige el cliente (Particular, Empresa o Ayuntamiento; las comisiones de fiestas y las peñas cuentan como '
     'Empresa), los invitados, el formato del servicio, la experiencia y el estilo de servicio.', False),
    ('2. La tabla de escalado y las demás tablas del final de la primera hoja dan los gramos de carne cruda por invitado, la '
     'materia prima de la experiencia y los invitados por parrillero y por ayudante. Las parrillas salen de dividir los '
     'kilos de carne cruda entre lo que asa una parrilla; los parrilleros, de dividir los invitados entre los que atiende '
     'cada uno.', False),
    ('3. Escribe la bebida que pones tú (0 si la pone el cliente) y el menaje y los consumibles por invitado. El carbón '
     'se calcula con los kilos de carne.', False),
    ('4. Escribe las horas por persona, el coste bruto por hora y la Seguridad Social. Si cocinas tú, cuéntate a precio de '
     'hora: es tu coste de oportunidad.', False),
    ('5. Escribe los alquileres que repercutes y los kilómetros de ida: el desplazamiento se cobra ida y vuelta, en una '
     'línea aparte y sin margen.', False),
    ('6. El margen objetivo de cada cliente está en la tabla «Política por cliente» del final: cámbialo ahí. El precio por '
     'invitado es el coste directo dividido entre (1 − margen), redondeado a los 0,50 € de arriba, más el suplemento de '
     'show de fuego si lo hay: el margen calculado queda igual o por encima del objetivo.', False),
    ('7. A una empresa se le presupuesta el precio SIN IVA («+ IVA»); a un particular, el precio CON IVA, porque en una '
     'oferta a consumidores el precio va con los impuestos incluidos.', False),
    ('IVA, PROPINAS Y COBROS', True),
    ('El servicio de comidas para consumir en el acto va al 10 % de IVA, bebida y alcohol incluidos (Ley 37/1992, art. '
     '91.Uno.2.2.º). Lo que facturas aparte sin ser accesorio, como la carpa o el mobiliario, va al 21 %. En las facturas '
     'a empresas no se practica retención de IRPF por esta actividad.', False),
    ('La propina voluntaria es decisión del cliente y es del equipo: no entra en el precio, en la base imponible ni en el '
     'total.', False),
    ('Los pagos en efectivo con particulares solo valen por debajo de 1.000 €: la ley prohíbe pagar en efectivo 1.000 € o '
     'más (art. 7 de la Ley 7/2012).', False),
    ('COBRO Y CANCELACIÓN', True),
    ('Particular: 30 % al firmar, 40 % a siete días del evento y 30 % a las 48 horas; Empresa: 30 % al firmar y 70 % a 30 días '
     'de la factura; Ayuntamiento: sin anticipo y pago a 30 días desde la conformidad (art. 198.4 de la Ley 9/2017). Emite '
     'factura de cada pago, también de la señal.', False),
    ('Cancelación, sobre el total. Particular: con 60 días o más retienes la señal (el 30 %); de 30 a 59 días, el 50 %; de 7 '
     'a 29 días, el 75 %; con menos de 7 días, el 100 %. Empresa: con 30 días o más, el 20 %; de 15 a 29 días, el 50 %; de 7 a '
     '14 días, el 75 %; con menos de 7 días, el 100 %. En un servicio de comida con fecha no hay derecho de desistimiento '
     '(art. 103.l del TRLGDCU): por eso la política tiene que estar firmada.', False),
    ('FUEGO Y SEGURIDAD', True),
    ('Si hay alerta de incendios o prohibición del fuego en el espacio, el servicio pasa al plan B de gas (plancha o '
     'piedra volcánica, una botella de menos de 15 kg por aparato) o se cambia la fecha, como recoge el contrato del kit. '
     'La licencia de la finca no levanta la restricción en terreno forestal.', False),
    ('ESTIMACIONES DEL KIT', True),
    ('Los valores por defecto y los tres ejemplos son estimaciones para ilustrar el cálculo, no precios de mercado. '
     'Cámbialos por tu escandallo, tus salarios, tus alquileres y tus kilómetros antes de presupuestar.', False),
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
    hoja_calculadora(wb)
    hoja_ejemplos(wb)
    hoja_instrucciones(wb)
    pr = wb.properties
    pr.title = '%s · v%s' % (TITULO, motor.VERSION)
    pr.subject = 'Plan de Negocio Parrillero-Asador para Eventos'
    pr.description = 'aichef.pro/%s' % PID
    pr.keywords = 'plan negocio parrillero asador eventos, AI Chef Pro'
    pr.creator = pr.lastModifiedBy = motor.CREATOR
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    wb.save(destino)
    sys.path.insert(0, PD)
    import inject_cache as IC                                                      # noqa: E402
    nf, inj, fail = IC.inject(destino)
    print('%s: formulas=%d cache_inyectado=%d fallos_pycel=%d' % (os.path.basename(destino), nf, inj, fail))
    return fail


PROHIBIDOS = [r'\bfreelance', r'validad[oa]s?', r'Espa[ñn]a,? 2026', r'food ?truck', r'carnet', r'carné',
              r'tarifa plana', r'cocina central']
#: rangos del research §2 (€/invitado sin IVA) que deben cumplir los ejemplos
RANGOS_EJEMPLO = {'Boda particular con cortes en mesa': (40, 46), 'Team building de empresa con BBQ texano': (25, 40),
                  'Fiesta o feria municipal de volumen': (8, 12)}
#: escenario estándar con el que se rotulan los tickets de las 10 experiencias (arreglos_d9 los importa)
ESCENARIO_TICKET = dict(guests=80, formato='Plato principal', servicio='Cortes en mesa', beb=0.0, menaje=0.60, hours=9,
                        wage=13.0, ss=0.33, rentals=0.0, km=0, per_km=0.95, show=0.0, iva=0.10)


def precio_experiencia(exper, canal, **cambios):
    e = dict(ESCENARIO_TICKET, canal=canal, exper=exper)
    e.update(cambios)
    return calcular(e)['price']


#: Tickets orientativos (€/invitado sin IVA) que los docx del kit rotulan para cada experiencia: (Particular, Empresa) con
#: None si no aplica. El autotest comprueba que el precio de la calculadora, en el escenario estándar, cae dentro.
EXP_TICKETS = OrderedDict([
    ('01', ((30, 55), (28, 45))), ('02', ((33, 58), (32, 50))), ('03', ((28, 50), (26, 42))),
    ('04', (None, (26, 42))), ('05', ((28, 50), (26, 42))), ('06', ((33, 58), (32, 50))),
    ('07', ((29, 52), (28, 45))), ('08', ((24, 40), (24, 38))), ('09', ((35, 55), (35, 55))),
    ('10', (None, (22, 38)))])
#: combinaciones recomendadas: (experiencias del mix, canal, rango del ticket)
COMBOS = OrderedDict([('boda_premium', (('09', '02'), 'Particular', (40, 70))),
                      ('team_building', (('10', '04'), 'Empresa', (45, 65))),
                      ('boda_costa', (('09', '07'), 'Particular', (40, 65)))])


def ticket_texto(codigo):
    """Línea «TICKET DE SERVICIO» de la experiencia `codigo` (sin IVA, orientativo)."""
    p, e = EXP_TICKETS[codigo]
    if codigo == '09':
        return ('Orientativo, sin IVA: suplemento de 8-15 €/inv. sobre cualquier experiencia · como servicio propio, '
                '%d-%d €/inv.' % p)
    partes = []
    if p:
        partes.append('Particular %d-%d €/inv.' % p)
    if e:
        partes.append('Empresa %d-%d €/inv.' % e)
    txt = 'Orientativo, sin IVA: ' + ' · '.join(partes)
    if codigo == '04':
        txt += ' · el show cooking por jornada se presupuesta aparte'
    if codigo == '10':
        txt += ' · la producción se presupuesta aparte'
    return txt


def autotest(destino):
    from pycel import ExcelCompiler
    err, n = [], 0
    xl = ExcelCompiler(filename=destino)
    wv = openpyxl.load_workbook(destino, data_only=True)
    wf = openpyxl.load_workbook(destino)
    casos = [(H2, 'BCD'[j], e, nombre) for j, (nombre, e) in enumerate(EJEMPLOS.items())]
    casos.append((H1, 'B', OrderedDict((k, v) for k, _r, _f2, v, _n in ENTRADAS), 'hoja principal'))
    for hoja, col, e, nombre in casos:
        esperado = calcular(e)
        for k, v in esperado.items():
            c = '%s%d' % (col, S[k])
            n += 1
            for lab, x in (('pycel', xl.evaluate("'%s'!%s" % (hoja, c))), ('caché', wv[hoja][c].value)):
                if not isinstance(x, (int, float)) or abs(float(x) - v) > 0.005:
                    err.append('%s · %s %s (%s): %s %r ≠ esperado %r' % (nombre, hoja, c, k, lab, x, v))
        if esperado['margin_calc'] + 1e-9 < esperado['margen']:
            err.append('%s: margen calculado %.4f < objetivo %.4f' % (nombre, esperado['margin_calc'], esperado['margen']))
        if nombre in RANGOS_EJEMPLO:
            lo, hi = RANGOS_EJEMPLO[nombre]
            if not lo <= esperado['price'] <= hi:
                err.append('%s: %.2f €/inv fuera del rango del research %s-%s' % (nombre, esperado['price'], lo, hi))
    # tabla de escalado de referencia (la del manual) contra pycel
    for j, col in enumerate('BCDE'):
        fila = tabla_escalado()[j]
        for i in range(6):
            n += 1
            x = xl.evaluate("'%s'!%s%d" % (H1, col, F_ESC + 1 + i))
            if not isinstance(x, (int, float)) or abs(float(x) - fila[1 + i]) > 0.005:
                err.append('escalado %s fila %d: %r ≠ %r' % (col, i, x, fila[1 + i]))
    # casos propios: cambian celdas de la hoja principal y se recalculan con pycel
    base = OrderedDict((k, v) for k, _r, _f2, v, _n in ENTRADAS)
    propios = [('propio 1: Empresa, 25 invitados, brunch', dict(base, canal='Empresa', guests=25, formato='Brunch',
                                                               exper='10 Brunch parrillero corporativo',
                                                               servicio='Buffet', hours=6, beb=0.0, rentals=0.0,
                                                               km=0, show=0.0)),
               ('propio 2: Particular, 41 invitados, estilo mesa', dict(base, canal='Particular', guests=41,
                                                                       exper='02 Asador a la cruz', hours=7,
                                                                       rentals=0.0, km=60, show=12.5)),
               ('propio 3: Ayuntamiento, 350 invitados', dict(base, canal='Ayuntamiento', guests=350,
                                                             formato='Chuletada de fiesta', servicio='Fiesta de volumen',
                                                             exper='11 Chuletada o costillada de fiesta',
                                                             beb=0.0, menaje=0.4, rentals=0.0, km=20))]
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
            if not isinstance(x, (int, float)) or abs(float(x) - v) > 0.005:
                err.append('%s: %s pycel %r ≠ esperado %r' % (nombre, k, x, v))
    e = dict(EJEMPLOS['Team building de empresa con BBQ texano'])
    cs = [calcular(dict(e, canal=c)) for c in CANALES]
    if len(set(round(c['can2'], 2) for c in cs)) < 2 or cs[0]['cb2'] == 0 or cs[1]['cb2'] != 0 or cs[2]['cb1'] != 0:
        err.append('el selector de cliente no cambia el cobro o la cancelación')
    # tramos de cancelación SIN huecos: los textos de las celdas cubren 0..∞ y los porcentajes suben
    for ic in (0, 1):
        v = [CANAL_TAB['cn%d' % i][1][ic] for i in (1, 2, 3, 4)]
        if v != sorted(v) or v[-1] != 1.0:
            err.append('cancelación %s: tramos no crecientes %r' % (CANALES[ic], v))
    for ic in range(3):
        s = sum(CANAL_TAB[k][1][ic] for k in ('pc_senal', 'pc_d7', 'pc_48h', 'pc_30d'))
        if abs(s - 1.0) > 1e-9:
            err.append('cobro %s suma %.2f ≠ 100 %%' % (CANALES[ic], s))
    # precios de las 10 experiencias dentro del rango del research
    for nombre in list(EXPERIENCIAS)[:10]:
        for canal in ('Particular', 'Empresa'):
            p = precio_experiencia(nombre, canal)
            if not 15 <= p <= 100:
                err.append('experiencia %s %s: %.2f €/inv fuera de 15-100' % (nombre, canal, p))
    # tickets de las experiencias y de las combinaciones (los que rotulan los docx) dentro de lo que calcula la hoja
    nombres = list(EXPERIENCIAS)
    for cod, (rp, re_) in EXP_TICKETS.items():
        nom = [x for x in nombres if x.startswith(cod)][0]
        for canal, rg in (('Particular', rp), ('Empresa', re_)):
            if rg and not rg[0] <= precio_experiencia(nom, canal) <= rg[1]:
                err.append('ticket %s %s: %.2f fuera de %s' % (cod, canal, precio_experiencia(nom, canal), rg))
    for nombre, (mix, canal, rg) in COMBOS.items():
        # el show de fuego (09) entra como suplemento de 10 €/inv. (el centro de 8-15), no como servicio propio
        tot = sum(10.0 if c == '09' else precio_experiencia([x for x in nombres if x.startswith(c)][0], canal)
                  for c in mix)
        if not rg[0] <= tot <= rg[1]:
            err.append('combinación %s: %.2f fuera de %s' % (nombre, tot, rg))
    if motor.detectar(wf, FICHERO)['molde'] != 'calc-beta':
        err.append('motor.detectar no la reconoce como calc-beta')
    gf = motor.gate_formatos(wf, FICHERO)
    if gf:
        err.append('gate_formatos: %d celdas, p. ej. %r' % (len(gf), gf[:3]))
    # validaciones de datos
    ws = wf[H1]
    dvs = dict((str(rng), dv) for dv in ws.data_validations.dataValidation for rng in dv.sqref.ranges)
    c = 'B%d' % K['canal']
    if dvs.get(c) is None or dvs[c].type != 'list' or 'Particular,Empresa,Ayuntamiento' not in (dvs[c].formula1 or ''):
        err.append('DV de lista incorrecta en %s' % c)
    for k in ('formato', 'exper', 'servicio'):
        c = 'B%d' % K[k]
        dv = dvs.get(c)
        if dv is None or dv.type != 'list' or not (dv.formula1 or '').startswith('=$A$'):
            err.append('DV de lista del rango incorrecta en %s' % c)
    dv = dvs.get('B%d' % CT['margen'])
    if dv is None or dv.formula2 != '0.95':
        err.append('DV del margen (máx. 95 %)')
    for k in ('guests', 'km'):
        dv = dvs.get('B%d' % K[k])
        if dv is None or dv.type != 'whole':
            err.append('DV entera ausente en %s' % k)
    textos = []
    for w in wf.worksheets:
        if w.page_setup.paperSize != 9 or not w.protection.sheet:
            err.append('%s: A4 y protección' % w.title)
        for row in w.iter_rows():
            for c in row:
                v = c.value
                if isinstance(v, str) and c.data_type != 'f':
                    textos.append((w.title, c.coordinate, v))
                if c.data_type == 'f' and wv[w.title][c.coordinate].value is None:
                    err.append('%s!%s: fórmula sin caché' % (w.title, c.coordinate))
                if c.fill.fgColor.rgb in ('00E8F5E9', 'FFE8F5E9') and c.protection.locked:
                    err.append('%s!%s: verde bloqueada' % (w.title, c.coordinate))
    # ninguna tasa tecleada dentro de una fórmula: sólo constantes estructurales (0, 1, 2, 1000)
    for w in wf.worksheets:
        for row in w.iter_rows():
            for c in row:
                if c.data_type == 'f':
                    sin_refs = re.sub(r"'[^']+'!|\$?[A-Z]{1,2}\$?\d+", '', str(c.value))
                    for num in re.findall(r'(?<![A-Za-z])\d+\.?\d*', sin_refs):
                        if num not in ('0', '1', '2', '1000'):
                            err.append('%s!%s: número tecleado %s en la fórmula %s' % (w.title, c.coordinate, num, c.value))
    todo = '\n'.join(t for _h, _c, t in textos)
    for rx in PROHIBIDOS:
        if re.search(rx, todo, re.I):
            err.append('prohibido /%s/' % rx)
    if re.search(r'service charge|sales tax|\$', todo, re.I):
        err.append('restos del EN (service charge / sales tax / $)')
    if motor.VERSION_FMT.format(pid=PID) not in todo or motor.BIO_LINE not in todo:
        err.append('falta la línea de versión o la bio')
    if wf.sheetnames != [H1, H2, H3]:
        err.append('pestañas %r' % wf.sheetnames)
    p = wf.properties
    if p.creator != 'AI Chef Pro' or p.description != 'aichef.pro/%s' % PID or \
            p.keywords != 'plan negocio parrillero asador eventos, AI Chef Pro':
        err.append('docProps: creator=%r description=%r keywords=%r' % (p.creator, p.description, p.keywords))
    for x in err:
        print('ERROR', x)
    print('autotest calculadora parrillero ES: %d comprobaciones (pycel + caché en ejemplos y hoja principal, pycel en '
          '3 casos propios y en la tabla de escalado) · %s' % (n * 2, 'VERDE' if not err else 'ROJO (%d errores)' % len(err)))
    for nombre, e in EJEMPLOS.items():
        r = calcular(e)
        print('  %-42s %d parrillas · %d parrilleros · %d ayud. · %6.2f €/inv sin IVA · %6.2f con IVA · total %9.2f · '
              'margen %.1f %%' % (nombre, r['parrillas'], r['parrilleros'], r['ayudantes'], r['price'], r['price_iva'],
                                  r['total'], r['margin_calc'] * 100))
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
