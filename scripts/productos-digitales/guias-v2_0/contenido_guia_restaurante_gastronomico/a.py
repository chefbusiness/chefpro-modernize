# -*- coding: utf-8 -*-
"""
contenido_guia_restaurante_gastronomico/a.py — el CONTENIDO del grupo A para
la guía «Cómo Montar un Restaurante Gastronómico» (85 €, el representante).

`grupo_a.py` pone la lógica de familia (detección de variante y localización de
filas por etiqueta); aquí van las filas, los textos, los importes y los
parámetros **propios de esta guía**. Las claves de los diccionarios de escenario
son **expresiones regulares** que se buscan contra la etiqueta de la columna A
ya normalizada (minúsculas, sin acentos): así siguen valiendo si el rótulo se
reordena, y no hay ni una coordenada fija en este fichero.

FUENTE DE CADA CIFRA — las tres etiquetas que se usan abajo:
  · «docx §N»  → medido en `astro-site/public/dl/guia-restaurante-gastronomico/
                 guia-restaurante-gastronomico.docx`, con el párrafo o la tabla
                 citados. Es el propio producto defendiendo su cifra.
  · «SPEC»     → `guias-v2-SPEC.md` (incluidas las decisiones de §7-bis).
  · «parametrizado» → NO está en la SPEC ni en ningún fichero de la familia.
                 Va en **celda verde con nota** y se declara como ejemplo
                 editable; no se teclea como si fuera un dato del sector
                 (regla capital: cifras del sector, sólo con fuente).

Comprobaciones aritméticas hechas al escribir este módulo (2026-08-29):
  · P&L: pesimista 116.270 €/mes y **−5.936 € de EBITDA (−5,1 %)** — malo pero
    NO inviable (§7-bis.14, frente a los −12.055 €/mes tecleados del japonés);
    realista 169.950 € y +27.965 € (16,5 %); optimista 203.280 € y +39.362 €
    (19,4 %). En euros anuales: 1,40 / 2,04 / 2,44 M€, contra la «facturación
    anual típica: 1,5-3 millones EUR para un gastronómico de 65 plazas» del
    docx §2 — el pesimista queda justo por debajo, que es lo que significa.
  · Ticket medio: los tres escenarios suman **exactamente 100 %** de comensales
    (0,30+0,25+0,45 · 0,40+0,20+0,40 · 0,65+0,20+0,15) y dan 91,95 / 123,20 /
    169,45 € de ticket ponderado.
  · Break-even: 91.000 € de fijos / 0,70 de margen de contribución = **130.000 €
    de umbral**, o **54 cubiertos/día** con ticket 110 € y 22 días. Caben en las
    65 plazas del propio libro (docx §5).
  · Préstamo de ejemplo: 300.000 € a 10 años al 5,5 % → **3.255,79 €/mes**.
"""

# ==========================================================================
# §2.1 · calculadora-ticket-medio.xlsx
# ==========================================================================
#: Tramos que se REPARTEN el 100 % de los comensales. El maridaje y la copa NO
#: entran: son consumo ADICIONAL sobre el mismo comensal, y por eso pueden
#: sumar más de 100 % sin que nada esté mal (SPEC §2.1).
TICKET = {
    'filas_mix': (r'^% comensales menu degustacion largo',
                  r'^% comensales menu degustacion corto',
                  r'^% comensales carta'),
    'escenarios': {
        # B · Escenario 1 — «carta con menú», el modelo 2 del docx §3
        'B': {
            r'^% comensales menu degustacion largo': 0.30,   # parametrizado
            r'^precio menu largo': 100,        # docx §15: menú largo 90-180 €
            r'^% comensales menu degustacion corto': 0.25,   # parametrizado
            r'^precio menu corto': 65,         # docx §15: menú corto 55-90 €
            r'^% comensales carta': 0.45,                    # parametrizado
            r'^ticket medio carta': 70,        # docx §15: 18-28 + 32-48 + 14-22
            r'^% comensales con maridaje': 0.20,             # parametrizado
            r'^precio maridaje': 50,           # docx §15: maridaje 45-90 €
            r'^% comensales con copa': 0.35,                 # parametrizado
            r'^precio copa media': 12,                       # parametrizado
            r'^cubiertos/dia': 55,                           # parametrizado
            r'^dias abierto': 22,                            # parametrizado
        },
        # C · Escenario 2 — el equilibrado; su ticket (123,20 €) es el que
        #     sostiene el «80-120 € por comensal» del docx §1 más el maridaje
        'C': {
            r'^% comensales menu degustacion largo': 0.40,
            r'^precio menu largo': 130,        # docx §15 (punto medio 90-180)
            r'^% comensales menu degustacion corto': 0.20,
            r'^precio menu corto': 75,         # docx §15 (punto medio 55-90)
            r'^% comensales carta': 0.40,
            r'^ticket medio carta': 85,        # docx §15
            r'^% comensales con maridaje': 0.30,
            r'^precio maridaje': 60,           # docx §15 (punto medio 45-90)
            r'^% comensales con copa': 0.30,
            r'^precio copa media': 14,                       # parametrizado
            r'^cubiertos/dia': 70,                           # parametrizado
            r'^dias abierto': 22,                            # parametrizado
        },
        # D · Escenario 3 — «sólo menú degustación», el modelo 1 del docx §3
        'D': {
            r'^% comensales menu degustacion largo': 0.65,
            r'^precio menu largo': 150,        # docx §15 (alto de 90-180)
            r'^% comensales menu degustacion corto': 0.20,
            r'^precio menu corto': 85,         # docx §15 (alto de 55-90)
            r'^% comensales carta': 0.15,
            r'^ticket medio carta': 95,        # docx §15 (alto del sumatorio)
            r'^% comensales con maridaje': 0.50,
            r'^precio maridaje': 75,           # docx §15 (alto de 45-90)
            r'^% comensales con copa': 0.20,
            r'^precio copa media': 16,                       # parametrizado
            r'^cubiertos/dia': 62,                           # parametrizado
            r'^dias abierto': 22,                            # parametrizado
        },
    },
}

# ==========================================================================
# §2.2 · pl-mensual-escenarios.xlsx  (§7-bis.7 y §7-bis.14)
# ==========================================================================
PL = {
    'escenarios': {
        'B': {                                   # Pesimista: malo, NO inviable
            r'^cubiertos/dia comida': 18,                    # parametrizado
            r'^cubiertos/dia cena': 35,                      # parametrizado
            r'^ticket medio comida': 70,       # docx §15 (menú corto 55-90 €)
            r'^ticket medio cena': 115,        # docx §15 (menú largo 90-180 €)
            r'^dias abierto': 22,                            # parametrizado
            r'^food cost': 0.32,               # docx §3: modelo 2, 28-32 %
            r'^coste personal': 46000,         # docx §13: 450-800 k€/año → mín.
            r'^alquiler': 17000,               # docx §8: 8-12 % de facturación
            r'^otros costes fijos': 22000,                   # parametrizado
        },
        'C': {                                                    # Realista
            r'^cubiertos/dia comida': 25,
            r'^cubiertos/dia cena': 45,
            r'^ticket medio comida': 75,       # docx §15 (medio de 55-90 €)
            r'^ticket medio cena': 130,        # docx §15 (medio de 90-180 €)
            r'^dias abierto': 22,
            r'^food cost': 0.30,               # docx §3: modelo 2, 28-32 %
            r'^coste personal': 52000,         # docx §13: 624 k€/año, el medio
            r'^alquiler': 17000,               # = 10 % de 169.950 €/mes
            r'^otros costes fijos': 22000,
        },
        'D': {                                                    # Optimista
            r'^cubiertos/dia comida': 28,
            r'^cubiertos/dia cena': 50,
            r'^ticket medio comida': 80,       # docx §15
            r'^ticket medio cena': 140,        # docx §15
            r'^dias abierto': 22,
            r'^food cost': 0.28,               # docx §3: modelo 1, 25-28 %
            r'^coste personal': 64000,         # docx §13: 768 k€/año, el alto
            r'^alquiler': 17000,
            r'^otros costes fijos': 26000,
        },
    },
    'notas': {
        r'^alquiler': ('El alquiler es FIJO: no baja porque vendas menos. En el '
                       'escenario realista son el 10 % de la facturación, '
                       'dentro del 8-12 % de zona premium del capítulo 8; en el '
                       'pesimista pesan el 14,6 %, y eso es exactamente lo que '
                       'significa un escenario malo.'),
        r'^coste personal': ('Capítulo 13: cocina 250.000-450.000 €/año y sala '
                             '200.000-350.000 €/año con la SS de la empresa, '
                             'para una plantilla de 22-30 personas. Los tres '
                             'escenarios caben en ese rango (552 / 624 / '
                             '768 k€ al año).'),
        r'^otros costes fijos': ('Suministros, seguros, marketing, tecnología, '
                                 'mantenimiento, limpieza, gestoría y '
                                 'amortización. Parametrizado: sustitúyelo por '
                                 'tu presupuesto real.'),
        r'^food cost': ('Capítulo 3: 25-28 % en el modelo de sólo menú '
                        'degustación y 28-32 % en el de carta + menú.'),
    },
}

# ==========================================================================
# §2.3 · plan-financiero-3-anos.xlsx
# ==========================================================================
PLAN = {
    'proyeccion': {
        # parametrizado: la SPEC no fija un crecimiento y el docx tampoco. Van
        # en celda verde y con nota, como cualquier hipótesis del cliente.
        'crecimiento': {'C': 0.08, 'D': 0.05},
        'inflacion': {'C': 0.03, 'D': 0.03},
        # SPEC §2.3.1: tipo general 25 %, con la nota del 15 % de las entidades
        # de nueva creación (que escribe `grupo_a`).
        'impuesto_sociedades': 0.25,
    },
    'financiacion': {
        # parametrizado: préstamo de EJEMPLO, ~43 % del CAPEX medio que calcula
        # calculadora-capex.xlsx (703.000 €). Con 1 año de carencia da
        # 1.375,00 €/mes el primer año y 3.528,00 €/mes los nueve siguientes.
        'importe': 300000,
        'plazo': 10,
        'tipo': 0.055,
        'carencia': 1,
    },
    # SPEC §2.3.5 y §7-bis.3: mínimo 6 meses de costes fijos + personal.
    'fondo_maniobra': {'meses': 6},
    # §2.3.6 · correspondencia de los 22 conceptos de «Inversión» con las 12
    # categorías de calculadora-capex.xlsx, para que los dos totales sean
    # comparables aunque el cliente rellene uno solo. Sin `externalLink`.
    'capex_map': {
        r'^obra civil y reforma integral': 'Obra civil y reforma integral',
        r'^instalaciones \(electricidad': 'Obra civil y reforma integral',
        r'^equipamiento cocina caliente': 'Equipamiento cocina profesional',
        r'^equipamiento cocina fria': 'Equipamiento cocina profesional',
        r'^pasteleria y obrador': 'Equipamiento cocina profesional',
        r'^zona de pase': 'Equipamiento cocina profesional',
        r'^plonge y lavado': 'Equipamiento cocina profesional',
        r'^almacenamiento y camaras': 'Equipamiento cocina profesional',
        r'^mobiliario sala': 'Mobiliario sala (65 plazas)',
        r'^iluminacion y decoracion': 'Interiorismo y decoración',
        r'^vajilla, cristaleria': 'Vajilla, cristalería, cubertería',
        r'^manteleria y textil': 'Vajilla, cristalería, cubertería',
        r'^bodega inicial': 'Bodega inicial (vinos)',
        r'^vitrina climatizada': 'Bodega inicial (vinos)',
        r'^tpv, software': 'Tecnología (TPV, reservas, software)',
        r'^web, branding': 'Marketing lanzamiento',
        r'^marketing de lanzamiento': 'Marketing lanzamiento',
        r'^proyecto tecnico y licencias': 'Proyecto técnico + licencias',
        r'^seguros \(primer ano\)': 'Seguros y otros',
        r'^stock inicial materias primas': 'Stock inicial materias primas',
        r'^uniformes equipo': 'Seguros y otros',
        r'^fondo de maniobra': 'Fondo de maniobra (6 meses)',
    },
}

# ==========================================================================
# §2.4 · cash-flow-break-even.xlsx
# ==========================================================================
CASH = {
    # Se REPITE con nota, no se enlaza: un .xlsx movido de carpeta daría #REF!
    # (§1.13). Es la cuota que calcula plan-financiero-3-anos!Financiación!B12
    # con el préstamo de ejemplo de arriba: 300.000 € a 10 años al 5,5 % con
    # 1 año de carencia → 108 cuotas de 3.528,00 € (durante la carencia se
    # pagan sólo 1.375,00 €/mes de intereses).
    'cuota_mensual': 3528.00,
    'break_even': {
        # = personal 52.000 + alquiler 17.000 + otros 22.000 del escenario
        # realista del P&L de esta misma guía (§7-bis.7: una sola fuente).
        'costes_fijos': 91000,
        # 1 − food cost 0,30 del escenario realista (docx §3).
        'margen_contribucion': 0.70,
        # Facturación realista 169.950 € / (70 cubiertos × 22 días) = 110,36 €.
        'ticket_medio': 110,
        'dias_mes': 22,
    },
}
