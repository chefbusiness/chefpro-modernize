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

──────────────────────────────────────────────────────────────────────────
UNA SOLA FUENTE POR MAGNITUD (§7-bis.7) — cómo encajan los cuatro libros
──────────────────────────────────────────────────────────────────────────
La ronda 2 midió TRES tickets medios y DOS facturaciones distintas para el
mismo restaurante (RD-09, RT-11, RC-02). Aquí se cierra la cadena: los tres
escenarios son los MISMOS en los cuatro libros y cada cifra se deriva de la
anterior, no se teclea dos veces.

  calculadora-ticket-medio  → mix de comensales y precios (docx §15)
        ↓ ticket ponderado T y cubiertos/día N
  pl-mensual-escenarios     → tickets de comida y cena calibrados para que
                              (Nc·tk_comida + Nn·tk_cena) = T·N EXACTAMENTE
        ↓ facturación mensual F = T·N·días
  plan-financiero 'P&L Mensual' → el escenario REALISTA desglosado por línea
  cash-flow-break-even      → break-even con esos mismos fijos y ese ticket

Comprobación aritmética (hecha al escribir este módulo, 2026-08-29):

  Escenario     T (€)    N     días   F (€/mes)     F (€/año)   EBITDA
  Pesimista     99,80    60     22    131.736,00    1,58 M€     +3.580,48 (2,7 %)
  Realista     123,20    70     22    189.728,00    2,28 M€    +34.007,92 (17,9 %)
  Optimista    136,00    78     22    233.376,00    2,80 M€    +47.030,72 (20,2 %)

  · Los tres caben en la «facturación anual típica 1,5-3 M€ para un
    gastronómico de 65 plazas» del docx §2.
  · El PESIMISTA es malo pero NO inviable (§7-bis.14, RT-13): +2,7 % de EBITDA
    con el alquiler pesando el 12,9 % de la facturación (docx §8 da 8-12 % en
    zona premium: pasarse es exactamente lo que significa un escenario malo).
  · Coste de personal: 564 / 718 / 936 k€ al año, dentro del rango CORREGIDO de
    §5.4 (556 k€ - 1,0 M€ con la SS de la empresa), no del rango viejo que
    DOM-02/COM-10 declaran falso.
  · Préstamo de ejemplo: 300.000 € a 10 años al 5,5 % con 1 año de carencia →
    1.375,00 €/mes el primer año (sólo intereses) y 3.528,00 €/mes después.
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
    # RC-02: las columnas se llamaban «Escenario 1/2/3» y no se podían cruzar
    # con el «Pesimista/Realista/Optimista» del P&L. Son el mismo restaurante.
    'cabeceras': {'B': 'Pesimista', 'C': 'Realista', 'D': 'Optimista'},
    'escenarios': {
        # B · PESIMISTA — «carta con menú», el modelo 2 del docx §3
        'B': {
            r'^% comensales menu degustacion largo': 0.30,   # parametrizado
            r'^precio menu largo': 110,        # docx §15: menú largo 90-180 €
            r'^% comensales menu degustacion corto': 0.25,   # parametrizado
            r'^precio menu corto': 70,         # docx §15: menú corto 55-90 €
            r'^% comensales carta': 0.45,                    # parametrizado
            r'^ticket medio carta': 75,        # docx §15: 18-28 + 32-48 + 14-22
            r'^% comensales con maridaje': 0.20,             # parametrizado
            r'^precio maridaje': 55,           # docx §15: maridaje 45-90 €
            r'^% comensales con copa': 0.35,                 # parametrizado
            r'^precio copa media': 13,                       # parametrizado
            r'^cubiertos/dia': 60,             # = 22 comida + 38 cena del P&L
            r'^dias abierto': 22,                            # parametrizado
        },
        # C · REALISTA — el equilibrado; su ticket (123,20 €) sostiene el
        #     «80-120 € por comensal» del docx §1 más el maridaje
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
            r'^cubiertos/dia': 70,             # = 25 comida + 45 cena del P&L
            r'^dias abierto': 22,                            # parametrizado
        },
        # D · OPTIMISTA — más cubiertos Y mejor mix (65 % de menú largo).
        #     RD-09: antes tenía MENOS cubiertos que el realista, que es lo
        #     contrario de un escenario optimista.
        'D': {
            r'^% comensales menu degustacion largo': 0.65,
            r'^precio menu largo': 120,        # docx §15 (dentro de 90-180)
            r'^% comensales menu degustacion corto': 0.20,
            r'^precio menu corto': 72,         # docx §15 (dentro de 55-90)
            r'^% comensales carta': 0.15,
            r'^ticket medio carta': 82,        # docx §15
            r'^% comensales con maridaje': 0.50,
            r'^precio maridaje': 57,           # docx §15 (dentro de 45-90)
            r'^% comensales con copa': 0.20,
            r'^precio copa media': 14,                       # parametrizado
            r'^cubiertos/dia': 78,             # = 28 comida + 50 cena del P&L
            r'^dias abierto': 22,                            # parametrizado
        },
    },
    # RD-23 · §1.5(a): esta hoja FIJA precios y en España el precio de carta se
    # anuncia CON IVA. Sin decirlo, un menú de 150 € se lee como 150 € netos y
    # la facturación sale un 10 % alta.
    'iva': {'etiqueta': 'Tipo de IVA de los precios de esta hoja (%)',
            'valor': 0.10,
            'nota': ('Los precios de arriba se escriben SIN IVA, igual que el '
                     'P&L. Esta celda sólo sirve para la fila «Ticket medio '
                     'CON IVA», que es el precio que el comensal ve en la '
                     'carta: 10 % general de restauración y 21 % en la parte '
                     'de bebida alcohólica.')},
    # RC-02 · el simulador se compara con el P&L, que es la fuente (§7-bis.7)
    'reconciliacion': {
        'B': 131736.00, 'C': 189728.00, 'D': 233376.00,
    },
}

# ==========================================================================
# §2.2 · pl-mensual-escenarios.xlsx  (§7-bis.7 y §7-bis.14)
# ==========================================================================
#: Los tickets de comida y cena NO son cifras sueltas: se han calibrado para
#: que la facturación de esta hoja sea EXACTAMENTE la del simulador de ticket
#: medio (T × cubiertos × días), con la cena a ~1,6 × la comida (el menú largo
#: se sirve de noche). Comprobado: 22·72,25 + 38·115,75 = 5.988,00 = 99,80·60.
PL = {
    'escenarios': {
        'B': {                                   # Pesimista: malo, NO inviable
            r'^cubiertos/dia comida': 22,                    # parametrizado
            r'^cubiertos/dia cena': 38,                      # parametrizado
            r'^ticket medio comida': 72.25,    # calibrado contra T = 99,80 €
            r'^ticket medio cena': 115.75,     # docx §15 (menú largo 90-180 €)
            r'^dias abierto': 22,                            # parametrizado
            r'^food cost': 0.32,               # docx §3: modelo 2, 28-32 %
            r'^coste personal': 47000,         # docx §13+§14 → 564 k€/año
            r'^alquiler': 17000,               # docx §8: 8-12 % de facturación
            r'^otros costes fijos': 22000,                   # parametrizado
            r'^amortizacion': 6000,                          # parametrizado
        },
        'C': {                                                    # Realista
            r'^cubiertos/dia comida': 25,
            r'^cubiertos/dia cena': 45,
            r'^ticket medio comida': 88.91,    # calibrado contra T = 123,20 €
            r'^ticket medio cena': 142.25,     # docx §15 (medio de 90-180 €)
            r'^dias abierto': 22,
            r'^food cost': 0.30,               # docx §3: modelo 2, 28-32 %
            r'^coste personal': 59801.68,      # = plantilla-turnos-brigada
            r'^alquiler': 17000,               # = 9,0 % de 189.728 €/mes
            r'^otros costes fijos': 22000,
            r'^amortizacion': 6000,
        },
        'D': {                                                    # Optimista
            r'^cubiertos/dia comida': 28,
            r'^cubiertos/dia cena': 50,
            r'^ticket medio comida': 98.25,    # calibrado contra T = 136,00 €
            r'^ticket medio cena': 157.14,     # docx §15 (dentro de 90-180 €)
            r'^dias abierto': 22,
            r'^food cost': 0.28,               # docx §3: modelo 1, 25-28 %
            r'^coste personal': 78000,         # docx §13+§14 → 936 k€/año
            r'^alquiler': 17000,
            r'^otros costes fijos': 26000,
            r'^amortizacion': 6000,
        },
    },
    'notas': {
        r'^alquiler': ('El alquiler es FIJO: no baja porque vendas menos. En el '
                       'escenario realista son el 9,0 % de la facturación, '
                       'dentro del 8-12 % de zona premium del capítulo 8; en el '
                       'pesimista pesan el 12,9 %, y eso es exactamente lo que '
                       'significa un escenario malo.'),
        # DOM-02/COM-10/§5.4 · el rango del capítulo 13 es el BRUTO, SIN la
        # Seguridad Social de la empresa. Con el 33 % de
        # plantilla-turnos-brigada!C41 las cifras correctas son éstas.
        r'^coste personal': ('Coste con la SS de la empresa YA incluida (33 %, '
                             'la celda C41 de plantilla-turnos-brigada.xlsx). '
                             'Los rangos del capítulo 13 —cocina '
                             '250.000-450.000 €/año y sala 200.000-350.000 €— '
                             'son BRUTOS, sin SS: con el 33 % son cocina '
                             '322.400-601.900 € y sala 234.000-403.000 €, o '
                             '556 k€-1,0 M€ en total. Los tres escenarios '
                             '(564 / 718 / 936 k€ al año) caben ahí. El '
                             'realista NO se teclea: es el coste de la brigada '
                             'de plantilla-turnos-brigada.xlsx.'),
        r'^otros costes fijos': ('Suministros, seguros, marketing, tecnología, '
                                 'mantenimiento, limpieza y gestoría. La '
                                 'amortización va en su PROPIA fila, debajo: '
                                 'si entrase aquí, el «EBITDA» sería un EBIT. '
                                 'Parametrizado: sustitúyelo por tu '
                                 'presupuesto real.'),
        r'^food cost': ('Capítulo 3: 25-28 % en el modelo de solo menú '
                        'degustación y 28-32 % en el de carta + menú.'),
        r'^amortizacion': ('Amortización mensual del equipamiento y la obra. '
                           'NO resta del EBITDA (por eso está debajo): resta '
                           'del EBIT, que es la fila siguiente. Parametrizado: '
                           'divide tu CAPEX amortizable entre los años de vida '
                           'útil y entre 12.'),
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
        # parametrizado: préstamo de EJEMPLO. Con 1 año de carencia da
        # 3.208,33 €/mes el primer año (sólo intereses) y 8.232,00 €/mes los
        # nueve siguientes. El importe se ha subido de los 300.000 € de la v1.1
        # a 700.000 € porque con la NECESIDAD que este mismo libro calcula
        # ahora (1.889.944,24 €) los 300.000 € dejaban el plan sin cuadrar.
        'importe': 700000,
        'plazo': 10,
        'tipo': 0.055,
        'carencia': 1,
        # RD-20 · un analista de riesgos cuadra necesidad = fondos propios +
        # préstamo + otras fuentes antes de mirar nada más. Con el préstamo de
        # ejemplo, los fondos propios que hacen cuadrar el plan son
        # 1.889.944,24 − 700.000 = 1.189.944,24 €.
        'fondos_propios': 1189944.24,
        'otras_fuentes': 0,
    },
    # SPEC §2.3.5 y §7-bis.3: mínimo 6 meses de costes fijos + personal.
    'fondo_maniobra': {'meses': 6},
    # RD-08 · el Gantt firma el arrendamiento en el mes 3 y contrata la brigada
    # en el 12 para abrir en el 18: hay renta y hay nóminas ANTES de facturar
    # un euro, y no había ninguna partida que lo recogiera. Los meses van en
    # celda verde; el importe lo pone el P&L de este mismo libro.
    'preapertura': {'meses_renta': 6, 'meses_nomina': 2},
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
    # RD-01/RT-02/RC-01 · el libro que §7-bis.7 declara FUENTE ÚNICA se
    # entregaba con las 22 partidas vacías: «TOTAL inversión 0,00 €». Estos
    # importes van en VERDE y son de EJEMPLO (§1.2), y CUADRAN con lo que los
    # checklists de este mismo pack ya tasan, que es lo que exige RC-05:
    #   equipamiento (8 conceptos)  = 161.430,40 € = checklist-equipamiento!G98
    #   sala (2 conceptos)          = 108.200,00 € = checklist-diseno-sala
    #   vajilla + textil            =  30.230,00 € = checklist-vajilla
    #   web + marketing lanzamiento =  23.800,00 € = checklist-marketing
    #   proyecto técnico y licencias=  23.960,00 € = checklist-legal SIN el
    #                                 bloque «Local» (su TOTAL es 57.960 €,
    #                                 de los que 34.000 € son la fianza:
    #                                 un depósito recuperable, no CAPEX;
    #                                 va con la preapertura, no aquí)
    'inversion': {
        r'^obra civil y reforma integral': 250000,  # capex, rango medio
        r'^instalaciones \(electricidad': 60000,    # parametrizado
        r'^equipamiento cocina caliente': 78000,    # checklist-equipamiento
        r'^equipamiento cocina fria': 42000,        # checklist-equipamiento
        r'^pasteleria y obrador': 14000,            # checklist-equipamiento
        r'^zona de pase': 8000,                     # checklist-equipamiento
        r'^plonge y lavado': 6430.40,               # checklist-equipamiento
        r'^almacenamiento y camaras': 13000,        # checklist-equipamiento
        r'^mobiliario sala': 62000,                 # checklist-diseno-sala
        r'^iluminacion y decoracion': 46200,        # checklist-diseno-sala
        r'^vajilla, cristaleria': 26000,            # checklist-vajilla
        r'^manteleria y textil': 4230,              # checklist-vajilla
        r'^bodega inicial': 40000,                  # capex, rango medio
        r'^vitrina climatizada': 6500,              # parametrizado
        r'^tpv, software': 9900,                    # checklist-equipamiento
        r'^web, branding': 8800,                    # checklist-marketing
        r'^marketing de lanzamiento': 15000,        # checklist-marketing
        r'^proyecto tecnico y licencias': 23960,    # checklist-legal
        r'^seguros \(primer ano\)': 4500,           # parametrizado
        r'^stock inicial materias primas': 12000,   # capex, rango medio
        r'^uniformes equipo': 3500,                 # parametrizado
        # `fondo de maniobra` NO va aquí: lo CALCULA el bloque de §2.3.5.
    },
    # RD-01/RT-02/RC-01/RC-09 · el 'P&L Mensual' precargado con el escenario
    # REALISTA, línea a línea. Cuadra al céntimo con pl-mensual-escenarios:
    #   ingresos   40.106,00 + 115.434,00 + 34.188,00 = 189.728,00
    #   variables  45.636,36 + 11.282,04 =  56.918,40 = 30 % de la facturación
    #   fijos      SUM(B20:B29) + B31     =  98.801,68 (sin la amortización)
    #   EBITDA     132.809,60 - 98.801,68 =  34.007,92 = pl-mensual!C21
    'pl_mensual': {
        r'^comidas \(cubiertos': 40106.00,
        r'^cenas \(cubiertos': 115434.00,
        r'^vinos y bebidas': 34188.00,
        r'^eventos privados': 0,
        r'^materia prima': 45636.36,
        r'^bebidas \(coste bodega\)': 11282.04,
        r'^personal cocina': 38390.01,
        r'^personal sala': 21411.67,
        r'^alquiler': 17000,
        r'^suministros': 6000,
        r'^seguros': 900,
        r'^marketing': 3500,
        r'^tecnologia y software': 1200,
        r'^mantenimiento y reparaciones': 2400,
        r'^limpieza externa': 2800,
        r'^asesoria y gestoria': 1200,
        r'^amortizacion equipamiento': 6000,
        r'^otros gastos fijos': 4000,
    },
    'pl_notas': {
        r'^comidas \(cubiertos': ('Escenario REALISTA de '
                                  'pl-mensual-escenarios.xlsx: 25 cubiertos de '
                                  'comida × 72,92 € × 22 días. Valor de '
                                  'ejemplo: cámbialo por el tuyo y el libro '
                                  'entero se recalcula.'),
        r'^cenas \(cubiertos': ('45 cubiertos de cena × 116,60 € × 22 días '
                                '(escenario realista).'),
        r'^vinos y bebidas': ('Maridaje y copa del simulador de ticket medio: '
                              '(18,00 + 4,20) € × 70 cubiertos × 22 días.'),
        r'^personal cocina': ('Coste CON la Seguridad Social de la empresa. '
                              'La fuente del coste de personal es '
                              'plantilla-turnos-brigada.xlsx (§7-bis.7): '
                              '59.801,68 €/mes = 717.620,12 €/año para las 24 '
                              'personas del cuadrante, con el 33 % de SS.'),
        r'^amortizacion equipamiento': ('Queda FUERA del EBITDA (fila 32) y '
                                        'resta en el EBIT (fila 37): un EBITDA '
                                        'con la amortización dentro es un '
                                        'EBIT con otro nombre.'),
    },
}

# ==========================================================================
# §2.4 · cash-flow-break-even.xlsx
# ==========================================================================
CASH = {
    # Se REPITE con nota, no se enlaza: un .xlsx movido de carpeta daría #REF!
    # (§1.13). Son las cuotas que calcula plan-financiero-3-anos!Financiación
    # con el préstamo de ejemplo: 300.000 € a 10 años al 5,5 % con 1 año de
    # carencia. RD-21: estos 12 meses son el AÑO 1, es decir, el año de
    # carencia, en el que se pagan SÓLO intereses.
    'cuota_mensual': 8232.00,
    'cuota_carencia': 3208.33,
    'anio': 1,
    # RD-20/RD-08 · lo que el bloque de «Inversión» calcula como necesidad
    # total, repetido aquí con su nota (§1.13: se repite el dato, no se enlaza).
    'necesidad_total': 1889944.24,
    # RD-14 · la bebida tiene su propia celda de tipo para quien tenga venta
    # PARA LLEVAR (ésa sí va al 21 %).
    # 2026-08-31 (RD-17, decisión del dueño): en SALA es el 10 %, igual que la
    # comida (art. 91.Uno.2.2 de la Ley del IVA).
    'iva_bebida': 0.10,
    # RD-06/RC-08 · las 12 columnas se entregaban vacías y el punto de
    # equilibrio decía «No alcanzado» nada más abrir el fichero. Rampa de
    # apertura sobre el escenario REALISTA (189.728 €/mes): parametrizada, en
    # verde, con la nota de que es un ejemplo.
    'rampa': (0.60, 0.70, 0.80, 0.85, 0.90, 0.95,
              1.00, 1.00, 1.00, 1.00, 1.00, 1.00),
    'mes_tipo': {
        # ingresos (se multiplican por la rampa)
        'ingresos': {r'^facturacion comidas': 40106.00,
                     r'^facturacion cenas': 115434.00,
                     r'^bebidas y vinos': 34188.00,
                     r'^otros ingresos': 0},
        # gastos VARIABLES (se multiplican por la rampa)
        'variables': {r'^materia prima': 56918.40},
        # gastos FIJOS de caja (NO llevan rampa: son fijos). La amortización no
        # entra: no es caja.
        'fijos': {r'^personal': 59801.68,
                  r'^alquiler': 17000,
                  r'^suministros': 6000,
                  r'^marketing': 3500,
                  r'^otros gastos': 12500},
        # IVA soportado: 10 % de la materia prima y 21 % del resto de gastos
        # con IVA (las nóminas y la Seguridad Social no llevan).
        'iva_soportado': {'variables': 0.10, 'fijos_con_iva': 39000,
                          'tipo_fijos': 0.21},
    },
    # RD-07 · un cash flow de APERTURA sin saldo inicial ni salida de caja de
    # la inversión mide «el primer mes con flujo operativo positivo», no el mes
    # en que se recupera lo invertido. Parametrizado y en verde.
    # El saldo inicial de tesorería del mes 1 de EXPLOTACIÓN es, por
    # construcción, el fondo de maniobra que plan-financiero-3-anos.xlsx
    # dimensiona en su hoja «Inversión»: 155.720,08 €/mes de estructura × 6.
    'apertura': {'saldo_inicial': 934320.48, 'desembolso_capex': None,
                 'iva_capex': None},
    'break_even': {
        # = personal 59.801,68 + alquiler 17.000 + otros 22.000 del escenario
        # realista del P&L de esta misma guía (§7-bis.7: una sola fuente).
        # La amortización NO entra: el break-even es de caja.
        'costes_fijos': 98801.68,
        # 1 − food cost 0,30 del escenario realista (docx §3).
        'margen_contribucion': 0.70,
        # Ticket ponderado del escenario realista de
        # calculadora-ticket-medio.xlsx (§7-bis.7).
        'ticket_medio': 123.20,
        'dias_mes': 22,
    },
}

# ==========================================================================
# §2.3.6 / RC-05 · calculadora-capex.xlsx
# ==========================================================================
#: El checklist de equipamiento de ESTE MISMO pack tasa 164.718,40 € y el
#: «rango alto» de la calculadora decía 150.000 €: el propio producto se
#: desmentía. Se sube el rango a lo que el pack tasa, y el fondo de maniobra
#: deja de ser un rango tecleado que no cubre ni 2,4 meses de los costes fijos
#: que el P&L calcula (RD-03).
#: AVISO DEL CRÍTICO (coherencia CAPEX) — la necesidad total de financiación
#: que publica plan-financiero-3-anos.xlsx es 1.889.944,24 € (CAPEX 734.020,40
#: + preapertura 221.603,36 + fondo de maniobra 934.320,48) y el «Rango Alto»
#: de esta calculadora se quedaba en 1.305.000 €: un 45 % por debajo de lo que
#: el propio pack dice que hace falta, sin que ninguno de los dos libros
#: mencionara al otro. Dos arreglos, ninguno inventado: la calculadora incorpora
#: la PREAPERTURA (que no tenía fila ninguna) y sube el rango del fondo de
#: maniobra hasta cubrir seis meses de una estructura de este tamaño; y las dos
#: filas llegan con el importe del plan como EJEMPLO en la columna verde.
CAPEX = {
    'rangos': {
        r'^equipamiento cocina profesional': (55000, 110000, 180000),
        # 6 meses de estructura: en el extremo bajo, una casa de menú de
        # mercado; en el alto, la de este pack (934.320,48 €).
        r'^fondo de maniobra': (180000, 450000, 950000),
        # Rentas del local antes de abrir (la licencia tarda 4-8 meses) más
        # las nóminas de la brigada durante la formación y las pruebas.
        r'^preapertura': (40000, 110000, 250000),
    },
    #: Filas que esta calculadora NO tenía. Se añaden ANTES de la fila TOTAL,
    #: sin tocar ninguna de las que ya estaban.
    'filas_nuevas': (
        {'patron': r'^preapertura',
         'etiqueta': 'Preapertura (rentas y nóminas antes de abrir)'},
    ),
    #: Valor de EJEMPLO en la columna verde «Tu Presupuesto (€)», tomado del
    #: plan financiero de este mismo kit. No es una estimación nueva: es la
    #: misma cifra, para que los dos libros digan lo mismo.
    'ejemplos': {
        r'^fondo de maniobra': 934320.48,
        r'^preapertura': 221603.36,
    },
    'notas': {
        r'^equipamiento cocina profesional': (
            'El rango alto llega a 180.000 € porque el '
            'checklist-equipamiento-cocina.xlsx de este mismo pack tasa '
            '161.430,40 € para una cocina completa con Josper, horno mixto de '
            '10 GN, abatidor y dos cámaras.'),
        r'^fondo de maniobra': (
            'Estos tres números son un rango de mercado; el TUYO lo calcula '
            'plan-financiero-3-anos.xlsx, hoja «Inversión», con TUS costes '
            'fijos. Seis meses del escenario realista de este pack son '
            '6 × 155.720,08 € = 934.320,48 €, que es la cifra de ejemplo de la '
            'columna verde y la que marca el rango alto. Ajústala a tu caso.'),
        r'^preapertura': (
            'Rentas y suministros del local antes de abrir (la licencia tarda '
            '4-8 meses) más las nóminas de la brigada durante la formación. '
            'La cifra verde, 221.603,36 €, es la de ejemplo del plan '
            'financiero de este kit (6 meses de renta + 2 de nómina); '
            'ajústala a tu caso. Sin esta fila, la calculadora pedía menos '
            'dinero del que el propio plan dice que hace falta.'),
    },
}
