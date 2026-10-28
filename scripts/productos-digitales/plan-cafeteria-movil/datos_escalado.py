"""
datos_escalado.py — FUENTE ÚNICA de la tabla de escalado de la barra de café móvil para eventos (SPEC D13) y de las
bebidas por invitado según las horas.

Quien necesite esta tabla la IMPORTA de aquí, no la copia:
  · `calculadora_caf_es.py` (hoja Calculadora, bloque «Tabla de escalado» y fórmulas de logística),
  · la hoja `Instrucciones` del plan financiero y el Word §6 (invitados → baristas, grupos o máquinas, molinos, kg de café,
    l de leche, vasos, potencia, toma eléctrica o generador, agua).

Sin dependencias: solo listas, tuplas y dicts de Python, más dos funciones puras (`escalar`, `tabla_escalado`).
Si cambia un valor, se cambia AQUÍ y se regeneran el Excel, la calculadora y el Word.

Procedencia de cada cifra (F1-research §0, §1 y §3.b):
  «research» = rango leído en el research (ratios de EE. UU.: grindkit, beanandbrewtech, ficha de fabricante);
  «estimación del kit (ratios de EE. UU.)» = punto medio o supuesto del kit, SIN fuente española: cámbialo por tu medición.

Sesión Claude Code, 28-oct-2026.
"""
import math

ORIGEN = 'estimación del kit (ratios de EE. UU.)'

# ---------------------------------------------------------------------------------------------------------------------
# 1. Bebidas por invitado según el formato / las horas  (research §1: ≤ 2 h 1,0 · 2-4 h 1,3-1,5 · 4-6 h 1,5-1,8 · jornada 2,0-2,5;
#    congreso con pausas 1,6 = mezcla del caso §4). Valor = punto medio del rango. (nombre, horas hasta inclusive o None, valor, rango)
# ---------------------------------------------------------------------------------------------------------------------
BEBIDAS_POR_INVITADO = [
    ('Hasta 2 horas', 2, 1.0, '1,0'),
    ('Más de 2 y hasta 4 horas', 4, 1.4, '1,3-1,5'),
    ('Más de 4 y hasta 6 horas', 6, 1.65, '1,5-1,8'),
    ('Más de 6 horas (jornada)', None, 2.25, '2,0-2,5'),
    ('Congreso con pausas de café', None, 1.6, 'mezcla del caso'),
]
FORMATO_REF = 'Más de 2 y hasta 4 horas'
#: (nombre, ajuste sobre las bebidas por invitado): mañana +20-30 %, boda de noche −10 % (research §1)
AJUSTE_HORARIO = [
    ('Mañana (desayuno y café de media mañana)', 0.25),
    ('Tarde o jornada mixta', 0.0),
    ('Noche (después de la cena)', -0.10),
]
HORARIO_REF = 'Tarde o jornada mixta'


def bebidas_por_invitado(horas):
    """Bebidas por invitado de una barra abierta de `horas` horas (la fila 'Congreso con pausas' no depende de las horas)."""
    for nombre, hasta, valor, _r in BEBIDAS_POR_INVITADO:
        if hasta is not None and horas <= hasta:
            return valor
    return [v for n, h, v, _r in BEBIDAS_POR_INVITADO if h is None and n.startswith('Más de 6')][0]


# ---------------------------------------------------------------------------------------------------------------------
# 2. Capacidad y reglas de escalado
# ---------------------------------------------------------------------------------------------------------------------
#: clave → (rótulo, formato, valor, nota). `formato`: 'ent' | 'dec' | 'pct'
REGLAS = [
    ('cap_barista', 'Bebidas por hora que saca un barista con una cafetera de dos grupos', 'ent', 55,
     'Ratios de EE. UU. (grindkit y beanandbrewtech): 50-60 bebidas por hora con un barista en dos grupos; con dos baristas, 100-120. Se toma 55.'),
    ('pico', 'Factor de pico sobre la media (la cola se concentra tras la cena o en las pausas)', 'dec', 1.3,
     'Estimación del kit (ratios de EE. UU.): el pico es un 30 % más alto que la media por hora.'),
    ('bar_maq', 'Baristas que trabajan en una misma cafetera', 'ent', 2,
     'Ratios de EE. UU.: con dos baristas en una cafetera se llega a 100-120 bebidas por hora; una segunda estación entra por encima de eso.'),
    ('grupos_maq', 'Grupos de una cafetera', 'ent', 2, 'La cafetera del caso es de dos grupos (2,4-4,5 kW; la del caso, hasta 3,5 kW).'),
    ('molinos_extra', 'Molinos de reserva (descafeinado o filtro) además de uno por estación', 'ent', 1,
     'Estimación del kit: un molino de espresso por estación más uno de descafeinado o filtro.'),
    ('purga', 'Café de purga y calibrado por evento (kg)', 'dec', 0.15, 'Estimación del kit: 100-200 g por evento. Se toma 150 g.'),
    ('reserva', 'Reserva de vasos desechables sobre las bebidas', 'pct', 0.10, 'Estimación del kit: derrames, repeticiones y cortesías.'),
    ('loza_inv', 'Tazas de loza por invitado (con reposición durante el lavado)', 'dec', 1.25,
     'Del caso: loza para 150 en una boda de 120 invitados (plan financiero).'),
    ('agua_beb', 'Agua limpia por bebida (litros: grupo, vapor y aclarado de jarras)', 'dec', 0.25, 'Estimación del kit (ratios de EE. UU.).'),
    ('agua_base', 'Agua limpia fija por evento (litros: manos, limpieza y reserva)', 'ent', 20, 'Estimación del kit (ratios de EE. UU.).'),
    ('tension', 'Tensión de la red (V)', 'ent', 230, 'Red monofásica española.'),
    ('amp_enchufe', 'Intensidad de un enchufe doméstico o de finca (A)', 'ent', 16,
     'Un enchufe de 16 A a 230 V da unos 3,7 kW (3,68 kW).'),
    ('factor_kva', 'Factor para dimensionar el generador (kVA por kW de cafetera)', 'dec', 1.4,
     'Margen de arranque: una cafetera de 3,5 kW pide un generador inverter de 5 kVA (fichas de distribuidor).'),
]
R = dict((k, v) for k, _r, _f, v, _n in REGLAS)
KW_MAQUINA = 3.5                 # kW de la cafetera de dos grupos del caso (≤ 3,5 kW: cabe en un enchufe de 16 A)
KW_ENCHUFE = R['amp_enchufe'] * R['tension'] / 1000.0          # 3,68 kW

# ---------------------------------------------------------------------------------------------------------------------
# 3. Bebidas de la carta: mezcla de ventas, dobles de espresso, leche total (ml) y vaso (oz).  La calculadora reparte la leche
#    entre las cuatro leches con LECHES; el café sale de dobles × G_POR_DOBLE.
# ---------------------------------------------------------------------------------------------------------------------
G_POR_DOBLE = 16                 # g por doble (research: 16-18 g; con 22 €/kg → 0,35 € de café por bebida)
#: (nombre, mezcla %, dobles de espresso, leche total ml, vaso oz, PVP de carta con IVA)
BEBIDAS = [
    ('Espresso', 14, 1, 0, 4, 2.20),
    ('Americano', 14, 1, 0, 8, 2.70),
    ('Cortado', 10, 1, 80, 4, 2.40),
    ('Café con leche', 16, 1, 180, 8, 3.30),
    ('Flat white', 8, 1, 150, 8, 3.80),
    ('Capuchino', 14, 1, 160, 8, 3.80),
    ('Latte', 12, 1, 240, 12, 4.20),
    ('Mocha', 4, 1, 200, 12, 4.60),
    ('Chai latte', 4, 0, 220, 12, 4.40),
    ('Chocolate a la taza', 4, 0, 200, 8, 3.80),
]
#: reparto de los ml de leche de cada bebida entre las cuatro leches del Escandallo (suma 100 %)
LECHES = [('Leche entera', 0.70), ('Leche sin lactosa', 0.10), ('Bebida de avena barista', 0.15), ('Bebida de soja barista', 0.05)]


def cafe_g_medio():
    """Gramos de café por bebida de la mezcla estándar."""
    return sum(b[1] * b[2] for b in BEBIDAS) * G_POR_DOBLE / float(sum(b[1] for b in BEBIDAS))


def leche_ml_medio():
    """Mililitros de leche por bebida de la mezcla estándar."""
    return sum(b[1] * b[3] for b in BEBIDAS) / float(sum(b[1] for b in BEBIDAS))


# ---------------------------------------------------------------------------------------------------------------------
# 4. Escalado
# ---------------------------------------------------------------------------------------------------------------------
def _ceil(x, dec=0):
    f = 10 ** dec
    return math.ceil(round(x * f, 9)) / float(f)


def _cu(x):
    """ROUNDUP(ROUND(x;2);0): el ROUND interior evita que el ruido binario (462,00000000000006) suba una unidad."""
    return int(math.ceil(round(x, 2)))


def escalar(invitados, horas, bebidas_inv, ajuste=0.0, desechable=True, kw_maquina=KW_MAQUINA, cafe_g=None, leche_ml=None, reglas=None):
    """Logística de un evento: dict con bebidas, baristas, estaciones (cafeteras), grupos, molinos, kg de café, l de leche,
    vasos (desechables o tazas de loza), kW, A, kVA, toma y litros de agua. Espejo EXACTO de las fórmulas de la calculadora."""
    r = dict(R)
    if reglas:
        r.update(reglas)
    cafe_g = cafe_g_medio() if cafe_g is None else cafe_g
    leche_ml = leche_ml_medio() if leche_ml is None else leche_ml
    bebidas = _cu(invitados * bebidas_inv * (1 + ajuste))
    return escalar_bebidas(bebidas, invitados, horas, desechable, kw_maquina, cafe_g, leche_ml, r)


def escalar_bebidas(bebidas, invitados, horas, desechable, kw_maquina, cafe_g, leche_ml, r):
    por_hora = bebidas / float(horas)
    baristas = max(1, _cu(por_hora * r['pico'] / r['cap_barista']))
    estaciones = int(_ceil(baristas / float(r['bar_maq'])))
    kw = estaciones * kw_maquina
    kw_enchufe = r['amp_enchufe'] * r['tension'] / 1000.0
    return dict(
        bebidas=bebidas, por_hora=por_hora, baristas=baristas, estaciones=estaciones, grupos=estaciones * r['grupos_maq'],
        molinos=estaciones + r['molinos_extra'], kg_cafe=_ceil(bebidas * cafe_g / 1000.0 + r['purga'], 1),
        l_leche=_cu(bebidas * leche_ml / 1000.0),
        vasos=_cu(invitados * r['loza_inv']) if not desechable else _cu(bebidas * (1 + r['reserva'])),
        kw=kw, amperios=kw * 1000.0 / r['tension'], kva=_cu(kw * r['factor_kva']),
        toma='Enchufe de 16 A' if kw <= kw_enchufe else 'Toma dedicada o generador',
        agua=_cu(bebidas * r['agua_beb'] + r['agua_base']))


#: tamaños de la tabla de referencia (invitados) y horas del evento tipo
TAM_REF = (50, 100, 200, 300)
HORAS_REF = 3
#: filas de la tabla (clave de `escalar`, rótulo, formato)
FILAS_TABLA = [
    ('bebidas', 'Bebidas servidas (ud.)', 'ent'),
    ('baristas', 'Baristas', 'ent'),
    ('estaciones', 'Cafeteras de dos grupos (estaciones)', 'ent'),
    ('grupos', 'Grupos en total', 'ent'),
    ('molinos', 'Molinos', 'ent'),
    ('kg_cafe', 'Café en grano (kg)', 'dec'),
    ('l_leche', 'Leche y bebidas vegetales (l)', 'ent'),
    ('vasos', 'Vasos desechables (ud.)', 'ent'),
    ('kw', 'Potencia de las cafeteras (kW)', 'dec'),
    ('toma', 'Toma eléctrica', 'txt'),
    ('agua', 'Agua limpia (l)', 'ent'),
]


def tabla_escalado():
    """[(invitados, dict de `escalar`)] del evento tipo: 3 horas, tarde, de 2 a 4 horas (1,4 bebidas por invitado), vaso desechable."""
    return [(n, escalar(n, HORAS_REF, bebidas_por_invitado(HORAS_REF), 0.0, True)) for n in TAM_REF]


if __name__ == '__main__':
    print('ORIGEN: %s' % ORIGEN)
    print('café medio %.2f g · leche media %.1f ml · enchufe %.2f kW' % (cafe_g_medio(), leche_ml_medio(), KW_ENCHUFE))
    for n, d in tabla_escalado():
        print(n, d)
