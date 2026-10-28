"""
escalado_cof.py — FUENTE ÚNICA (EN) de la tabla de escalado del coffee cart (SPEC D227) y de las bebidas por invitado:
gemelo US de `../plan-cafeteria-movil/datos_escalado.py` (ES final, `d3174a8d`), con unidades US (lb, fl oz, gallons),
electricidad US (salida estándar de 110-120 V y 20 A ≈ 2.4 kW; máquina de 2 grupos a 220 V / 3,400 W, NEMA 6-20) y la carta
de una barra de café de eventos en EE. UU. (cold brew en lugar del café con leche; vasos de 8 / 12 / 16 oz).

Quien necesite esta tabla la IMPORTA de aquí: `calculadora_cof.py` (hojas «Cost per Drink», «Pricing Calculator») y las
pistas del Word §6 (`datos_cof.py`). Sin dependencias. Si cambia un valor, se cambia AQUÍ y se regeneran calculadora y Word.

Procedencia: research US §4.2, §5.1 y §5.2 (Flashquotes, grindkit.app, Coffee Cart Boys, Prima, BLS) y el ES; lo que no
tiene fuente es «Kit estimate (US ratios)». Sesión Claude Code, 28-oct-2026 (paso 1b).
"""
import math

ORIGEN = 'Kit estimate (US ratios): replace with your own measurements'

# 1. Bebidas por invitado según la duración (grindkit.app: ≤ 2 h 1.0 · 2-4 h 1.3-1.5 · 4-6 h 1.5-1.8 · 6+ h 2.0-2.5; la
#    conferencia con pausas = 1.6, mezcla del ES). (nombre, horas hasta inclusive o None, valor, rango)
BEBIDAS_POR_INVITADO = [
    ('Up to 2 hours', 2, 1.0, '1.0'),
    ('Over 2 and up to 4 hours', 4, 1.4, '1.3-1.5'),
    ('Over 4 and up to 6 hours', 6, 1.65, '1.5-1.8'),
    ('Over 6 hours (full day)', None, 2.25, '2.0-2.5'),
    ('Conference with coffee breaks', None, 1.6, 'blend of the breaks'),
]
FORMATO_REF = 'Up to 2 hours'           # el evento tipo US: 2 h de servicio (55.3 % de las reservas, Flashquotes)
#: (nombre, ajuste): mañana +20-30 % (grindkit.app), noche tras la cena −10 % (Kit estimate)
AJUSTE_HORARIO = [
    ('Morning (breakfast and mid-morning coffee)', 0.25),
    ('Afternoon or mixed day', 0.0),
    ('Evening (after dinner)', -0.10),
]
HORARIO_REF = 'Afternoon or mixed day'


def bebidas_por_invitado(horas):
    for nombre, hasta, valor, _r in BEBIDAS_POR_INVITADO:
        if hasta is not None and horas <= hasta:
            return valor
    return [v for n, h, v, _r in BEBIDAS_POR_INVITADO if h is None and n.startswith('Over 6')][0]


# 2. Capacidad y reglas. clave → (rótulo, formato 'ent' | 'dec' | 'pct', valor, nota)
REGLAS = [
    ('cap_barista', 'Drinks per hour one barista makes on a 2-group machine', 'ent', 55,
     'One cart and one barista make 50-65 drinks an hour (flashquotes.com; "50 cups per hour" at coffeecartboys.com). '
     'The kit uses 55.'),
    ('pico', 'Peak factor over the hourly average (the line builds after dinner or at the breaks)', 'dec', 1.3,
     'Kit estimate: the peak hour runs about 30% above the average.'),
    ('bar_maq', 'Baristas working one 2-group machine', 'ent', 2,
     'Kit estimate: one pulls shots while the other steams milk; above that, add a second station.'),
    ('grupos_maq', 'Groups on one machine', 'ent', 2, 'The example machines are 2-group machines.'),
    ('molinos_extra', 'Spare grinders (decaf or batch brew) on top of one per station', 'ent', 1,
     'Kit estimate: one espresso grinder per station plus one for decaf.'),
    ('purga', 'Coffee for purging and dialing in per event (lb)', 'dec', 0.33,
     'Kit estimate: about 150 g (0.33 lb) per event.'),
    ('reserva', 'Spare single-use cups on top of the drinks', 'pct', 0.10, 'Kit estimate: spills, remakes and courtesy drinks.'),
    ('loza_inv', 'Reusable cups per guest (with spares while they are washed)', 'dec', 1.25,
     'Kit estimate: china for about 160 at a wedding of 130 guests.'),
    ('agua_beb', 'Fresh water per drink (gallons: shots, steam and rinsing pitchers)', 'dec', 0.07,
     'Kit estimate: about 9 fl oz per drink.'),
    ('agua_base', 'Fixed fresh water per event (gallons: hand sink, cleaning and reserve)', 'ent', 5,
     'Kit estimate. Your county sets the size of the hand-sink tanks.'),
    ('v_maquina', 'Voltage of the machine circuit (V)', 'ent', 220, 'A 2-group machine runs on a 220-240V circuit.'),
    ('v_enchufe', 'Voltage of a standard outlet (V)', 'ent', 120, 'A standard US outlet gives 110-120V.'),
    ('amp_enchufe', 'Amps of a standard outlet circuit (A)', 'ent', 20,
     'A 20-amp circuit at 120V gives about 2.4 kW; many outlets are only 15 amps (1.8 kW).'),
    ('factor_kw', 'Generator sizing factor (kW of generator per kW of machines)', 'dec', 1.6,
     'Kit estimate for starting load and the grinders: one 3.4 kW machine needs a 5.5 kW (5,500 W running) inverter '
     'generator.'),
]
R = dict((k, v) for k, _r, _f, v, _n in REGLAS)
#: conversiones fijas (celdas grises; nada tecleado en las fórmulas)
CONVERSIONES = [('g_lb', 'Grams in one pound', 453.6), ('oz_gal', 'Fluid ounces in one US gallon', 128.0)]
C = dict((k, v) for k, _r, v in CONVERSIONES)
KW_MAQUINA = 3.4                # kW de la máquina de 2 grupos del caso (220 V, 3,400 W, NEMA 6-20; research §4.1)
KW_ENCHUFE = R['amp_enchufe'] * R['v_enchufe'] / 1000.0        # 2.4 kW

# 3. Carta: (nombre, mezcla %, dobles de espresso, leche total fl oz, vaso oz, precio de carta sin sales tax)
G_POR_DOBLE = 18                # g por doble: 18 g (0.63 oz) in, 36 g out (research §4.2)
BEBIDAS = [
    ('Espresso', 6, 1, 0, 8, 3.50),
    ('Americano', 12, 1, 0, 12, 4.50),
    ('Cortado', 6, 1, 2, 8, 4.75),
    ('Latte', 24, 1, 10, 12, 6.50),
    ('Cappuccino', 14, 1, 5, 8, 6.00),
    ('Flat white', 6, 1, 5, 8, 6.00),
    ('Mocha', 8, 1, 8, 12, 7.00),
    ('Chai latte', 8, 0, 6, 12, 6.50),
    ('Hot chocolate', 4, 0, 8, 12, 5.50),
    ('Cold brew', 12, 1.5, 1, 16, 6.50),
]
#: reparto de las fl oz de leche de cada bebida (suma 1): research §4.2, avena en el 25 % de las bebidas con leche
LECHES = [('Whole milk', 0.65), ('Lactose-free milk', 0.05), ('Oat milk', 0.25), ('Almond milk', 0.05)]


def cafe_g_medio():
    return sum(b[1] * b[2] for b in BEBIDAS) * G_POR_DOBLE / float(sum(b[1] for b in BEBIDAS))


def leche_oz_medio():
    return sum(b[1] * b[3] for b in BEBIDAS) / float(sum(b[1] for b in BEBIDAS))


# 4. Escalado
def _ceil(x, dec=0):
    f = 10 ** dec
    return math.ceil(round(x * f, 9)) / float(f)


def _cu(x, dec=0):
    """ROUNDUP(ROUND(x;2);dec): el ROUND interior evita que el ruido binario suba una unidad."""
    return _ceil(round(x, 2), dec) if dec else int(math.ceil(round(x, 2)))


def escalar(invitados, horas, bebidas_inv, ajuste=0.0, desechable=True, kw_maquina=KW_MAQUINA, cafe_g=None, leche_oz=None,
            reglas=None):
    r = dict(R)
    if reglas:
        r.update(reglas)
    cafe_g = cafe_g_medio() if cafe_g is None else cafe_g
    leche_oz = leche_oz_medio() if leche_oz is None else leche_oz
    bebidas = _cu(invitados * bebidas_inv * (1 + ajuste))
    por_hora = bebidas / float(horas)
    baristas = max(1, _cu(por_hora * r['pico'] / r['cap_barista']))
    estaciones = int(_ceil(baristas / float(r['bar_maq'])))
    kw = estaciones * kw_maquina
    kw_enchufe = r['amp_enchufe'] * r['v_enchufe'] / 1000.0
    return dict(
        bebidas=bebidas, por_hora=por_hora, baristas=baristas, estaciones=estaciones, grupos=estaciones * r['grupos_maq'],
        molinos=estaciones + r['molinos_extra'], lb_cafe=_ceil(bebidas * cafe_g / C['g_lb'] + r['purga'], 1),
        gal_leche=_cu(bebidas * leche_oz / C['oz_gal']),
        vasos=_cu(invitados * r['loza_inv']) if not desechable else _cu(bebidas * (1 + r['reserva'])),
        kw=kw, amperios=kw * 1000.0 / r['v_maquina'], gen_kw=_cu(kw * r['factor_kw'], 1),
        toma=TOMA_OK if kw <= kw_enchufe else TOMA_NO,
        agua=_cu(bebidas * r['agua_beb'] + r['agua_base']))


TOMA_OK = 'Standard 110V outlet'
TOMA_NO = 'Dedicated 220V circuit or generator'
TAM_REF = (50, 100, 200, 300)
HORAS_REF = 2
FILAS_TABLA = [
    ('bebidas', 'Drinks served', 'ent'),
    ('baristas', 'Baristas', 'ent'),
    ('estaciones', '2-group machines (stations)', 'ent'),
    ('grupos', 'Groups in total', 'ent'),
    ('molinos', 'Grinders', 'ent'),
    ('lb_cafe', 'Coffee beans (lb)', 'dec'),
    ('gal_leche', 'Milk and plant-based milks (gal)', 'ent'),
    ('vasos', 'Single-use cups', 'ent'),
    ('kw', 'Power draw of the machines (kW)', 'dec'),
    ('toma', 'Power needed', 'txt'),
    ('agua', 'Fresh water (gal)', 'ent'),
]


def tabla_escalado():
    """[(invitados, dict)] del evento tipo US: 2 horas, por la tarde, 1.0 bebidas por invitado, vaso de un solo uso."""
    return [(n, escalar(n, HORAS_REF, bebidas_por_invitado(HORAS_REF), 0.0, True)) for n in TAM_REF]


if __name__ == '__main__':
    print('café medio %.2f g · leche media %.2f fl oz · salida estándar %.2f kW' % (cafe_g_medio(), leche_oz_medio(),
                                                                                   KW_ENCHUFE))
    for n, d in tabla_escalado():
        print(n, d)
