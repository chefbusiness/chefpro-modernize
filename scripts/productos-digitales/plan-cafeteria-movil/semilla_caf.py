#!/usr/bin/env python3
"""
semilla_caf.py — Cafetería Móvil para Eventos ES 1.0 (SPEC D2, D5-D8): prepara el ORIGEN que `planes-v2_0/main.py`
convierte en el plan financiero y el checklist de la cafetería móvil. Copia adaptada de `parrillero-2_2/semilla_par.py`.

Copia los dos xlsx del Food Truck ES v2.2 publicados (`dl/plan-negocio-food-truck/`, SOLO LECTURA) con los nombres de
fichero de la cafetería móvil y escribe lo que el módulo de contenido no alcanza (F1-camino §1 y §3):
  · plan: valores de `0. Supuestos` (grupo_a conserva lo verde que trae el libro), títulos de hoja (Inversión A1/A2,
    PyG A2, Punto Equilibrio A2), las 14 partidas de inversión (filas 7-20: rótulo, importe, nota, ¿IVA?; 42.000 €,
    SPEC D8) y los 10 costes fijos propios del P&L (filas 26-35; 7.700 €/año, SPEC D8), y docProps;
  · checklist: título, pestañas, cabeceras de fase y las 80 tareas de `datos_checklist.py` (12/16/14/10/14/14) con el
    pie «Tareas completadas:» debajo; `Instrucciones!A3` con el NOMBRE del producto (m13 de la pizzería); DV, formato
    condicional y contadores los rehace el motor (`checklist_ok_y_contador`).
Corre en el VPS (openpyxl). Después: `main_caf.py --producto plan-negocio-cafeteria-movil-eventos --dry-run --origen <salida>`
(lo hace `ciclo.sh`).

    /root/venv-guias/bin/python semilla_caf.py --salida /root/tmp-caf-f2/motor/origen

Sesión Claude Code, 28-oct-2026.
"""
import argparse
import copy
import importlib
import os
import shutil
import sys

import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation

import datos_checklist as DC

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
FT = os.path.join(REPO, 'astro-site', 'public', 'dl', 'plan-negocio-food-truck')
PLAN_FT, CHECK_FT = 'plan-financiero-food-truck.xlsx', 'checklist-apertura-food-truck.xlsx'
PLAN, CHECK = 'plan-financiero-cafeteria-movil-eventos.xlsx', 'checklist-apertura-cafeteria-movil-eventos.xlsx'
PID = 'plan-negocio-cafeteria-movil-eventos'
NOMBRE = 'Plan de Negocio: Cafetería Móvil para Eventos'

TITULOS_PLAN = {
    ('Inversión Inicial', 'A1'): 'PLAN DE NEGOCIO: CAFETERÍA MÓVIL PARA EVENTOS',
    ('Inversión Inicial', 'A2'): 'Inversión inicial estimada — barra de café de especialidad para bodas, empresas y ferias',
    ('PyG 3 Años', 'A2'): 'Escenario realista — cafetería móvil para eventos',
    ('Punto Equilibrio', 'A2'): 'Punto de equilibrio — cafetería móvil para eventos',
}

#: Filas 7-20 de 'Inversión Inicial' (molde FT): (rótulo, importe, nota, ¿lleva IVA?). Research §4: 42.000 € en 15
#: partidas; la rotulación (1.200) va fundida con la furgoneta (14.000) para caber en las 14 filas (SPEC D8). Sin
#: palabras de recuento en el rótulo (motor.RX_RECUENTO) ni «registro» fuera de la fila de trámites (AMORTIZABLE).
#: «campana» no aparece (motor.TILDES la acentúa: gotcha de la pizzería).
INVERSION = [
    ('Furgoneta usada con rotulación y anclajes', 15200,
     'Furgoneta de ocasión tipo Kangoo L2 o Trafic (12.000-16.000 € en el mercado; el caso, 14.000 €) con la '
     'rotulación de la marca, estanterías y anclajes para llevar la barra, la cafetera y los depósitos sujetos. Si '
     'fijas en ella fregadero, depósitos o mueble, es una reforma de vehículo: informe de conformidad e ITV. '
     'Estimación del kit. Si la compras a un particular no hay IVA, sino el impuesto de transmisiones; en un '
     'concesionario, en REBU, el IVA no se deduce: pon «No» en la columna de al lado', 'Sí'),
    ('Barra-carro a medida con ruedas y depósitos ocultos, carpa e iluminación', 4400,
     'Barra móvil fabricada a medida, con los depósitos de agua escondidos y ruedas para entrar en salones y '
     'pabellones, más una carpa de 3 × 3 m y la iluminación para los servicios de noche. Una mesa de barista básica '
     'ronda los 1.800 € sin máquina. Estimación del kit', 'Sí'),
    ('Cafetera de dos grupos de gama media (3,5 kW como máximo)', 5500,
     'Máquina de espresso de dos grupos de gama media (3.000-6.000 €). Que no pase de 3,5 kW: así cabe en un enchufe '
     'de 16 A (unos 3,7 kW) y no dependes del generador en cada finca. Estimación del kit', 'Sí'),
    ('Molinos: espresso bajo demanda y descafeinado o filtro', 2100,
     'Un molino de espresso bajo demanda profesional (unos 1.430 € sin IVA) y otro para el descafeinado o el filtro '
     '(unos 620 €): el invitado español pide descafeinado de máquina. Fichas de distribuidor', 'Sí'),
    ('Energía: generador inverter de 5-7 kVA o primera batería, y cuadro con protecciones', 4500,
     'Para las fincas sin toma suficiente: un generador inverter de 5 kVA o más (los de 7 kVA, 4.300-5.350 €) o una '
     'primera batería de litio con inversor, silenciosa para bodas (un sistema completo, 6.000-10.000 €), con un '
     'cuadro con protecciones. Estimación del kit', 'Sí'),
    ('Agua e higiene: depósitos alimentarios, bomba, filtro descalcificador y lavamanos', 1000,
     'Dos depósitos de uso alimentario (agua limpia y gris), bomba, filtro descalcificador para la cafetera y un '
     'lavamanos autónomo. El agua se carga en red pública y el operador responde de ella hasta el punto de uso (RD '
     '3/2023, arts. 65.3 y 66.b)', 'Sí'),
    ('Frío: nevera bajo barra, neveras portátiles, acumuladores y termómetro', 900,
     'Leche y bebidas vegetales a la temperatura de su etiqueta desde la base hasta la barra, y un termómetro para '
     'el registro del APPCC', 'Sí'),
    ('Menaje: jarras por tipo de leche, tampers, básculas, cajón de posos y loza', 1500,
     'Una jarra por cada tipo de leche (alérgenos), tampers, básculas de extracción, cajón de posos, loza para 150 '
     'invitados y cajas para transportarla. En bodas y eventos de empresa se sirve en loza: es la opción segura con '
     'la normativa de envases', 'Sí'),
    ('TPV, datáfono y software', 600, 'Cobro en la venta directa y facturación conforme a Veri*factu', 'Sí'),
    ('Marca, web, fotos y dossier', 2000,
     'Identidad, web con formulario de presupuesto, sesión de fotos de la barra y dossier para novios, empresas, '
     'agencias y planners', 'Sí'),
    ('Constitución SL + notaría + registro', 1000,
     'SL unipersonal. Las tasas y el arancel del Registro no llevan IVA; los honorarios del notario y de la '
     'gestoría sí: cambia la columna de al lado a «Sí» si tu presupuesto es sobre todo de honorarios', 'No'),
    ('Declaración responsable, APPCC, alérgenos y formación de barista', 1000,
     'Redacción del plan APPCC itinerante, fichas de alérgenos de cada bebida y de la bollería, formación en higiene '
     'alimentaria y curso de barista', 'Sí'),
    ('Stock inicial: café, leche UHT y vasos', 800,
     'Primer pedido de café de especialidad, leche UHT o ESL «barista», bebidas vegetales, siropes y vasos', 'Sí'),
    ('Lanzamiento: feria nupcial, escaparate de bodas y catas para agencias', 1500,
     'Stand en una feria nupcial, alta destacada en un portal de bodas y catas para agencias y planners antes del '
     'primer evento', 'Sí'),
]
assert len(INVERSION) == 14 and sum(x[1] for x in INVERSION) == 42000

#: Filas 26-35 de 'PyG 3 Años' (costes fijos propios). SPEC D8: los 9 del research §4 + «Licencias y tasas de venta en
#: ferias y mercados» (300 €; `grupo_a.RX_SIN_IVA` sólo actúa en la columna E de Inversión: en el P&L todas las filas
#: propias van al tipo general, grupo_a.py:2544-2547, revisión final M5 y F2-NOTAS §9) = 7.700 €/año, una por
#: fila del molde (no se suprimen filas: desplazaría el P&L). Sin «eventos», «clientes» ni «días» en el rótulo
#: (motor.RX_RECUENTO). Las claves de `contenido….FIJOS` son estos rótulos normalizados.
FIJOS = {
    26: ('Asesoría fiscal y laboral (nóminas de fijos discontinuos)', 1680),   # research 1.500: +180 € por la demo §2.11.5 (F2-NOTAS §3)
    27: ('Furgoneta: mantenimiento, neumáticos e ITV', 800),
    28: ('Marketing: escaparate de bodas, Google Ads local, redes y feria nupcial', 3000),
    29: ('Software de gestión comercial, CRM y teléfono', 500),
    30: ('Mantenimiento de la cafetera y los molinos (técnico, juntas y filtros)', 600),
    31: ('Uniformes y lavandería', 300),
    32: ('Gestión de residuos (posos de café y envases)', 100),
    33: ('Prevención de riesgos laborales y vigilancia de la salud', 300),
    34: ('Catas y degustaciones comerciales', 300),
    35: ('Licencias y tasas de venta en ferias y mercados', 300),
}
FIJOS_TOTAL = 7880   # SPEC D8: 7.700 € + 180 € de calibración (demo §2.11.5 del motor)
assert sum(x[1] for x in FIJOS.values()) == FIJOS_TOTAL


def _supuestos(wb):
    """Los valores de `0. Supuestos` del caso. `grupo_a` CONSERVA lo que el libro ya trae en las celdas verdes (§1.3:
    dato del cliente) y sólo usa el valor del contenido en una celda vacía: partiendo del libro del FT, sin este paso
    el caso seguiría siendo el del food truck."""
    p2 = os.path.join(os.path.dirname(AQUI), 'planes-v2_0')
    sys.path.insert(0, p2)
    import grupo_a
    contenido = importlib.import_module('contenido_plan_negocio_cafeteria_movil_eventos.a')
    coords = dict((t[0], t[1]) for t in grupo_a.SUPUESTOS_BASE)
    ws = wb['0. Supuestos']
    escritas = 0
    for clave, t in contenido.SUPUESTOS.items():
        if t[2] is None:
            continue
        assert clave in coords, clave
        ws[coords[clave]] = t[2]
        escritas += 1
    return escritas


def _docprops(wb):
    """REVISION-FINAL B1 del parrillero: el motor no reescribe `description` ni `keywords` y heredaba los del FT."""
    wb.properties.description = 'aichef.pro/' + PID
    wb.properties.keywords = 'plan de negocio cafetería móvil para eventos, barra de café, AI Chef Pro'


def plan(salida):
    destino = os.path.join(salida, PLAN)
    shutil.copy2(os.path.join(FT, PLAN_FT), destino)
    wb = openpyxl.load_workbook(destino)
    print('  supuestos escritos:', _supuestos(wb))
    _docprops(wb)
    for (hoja, coord), texto in TITULOS_PLAN.items():
        wb[hoja][coord] = texto
    ws = wb['Inversión Inicial']
    for i, (rot, imp, nota, iva) in enumerate(INVERSION):
        r = 7 + i
        assert not str(ws.cell(r, 1).value).lower().startswith(('fianza', 'alquiler', 'imprevistos')), r
        ws.cell(r, 1).value, ws.cell(r, 2).value, ws.cell(r, 4).value, ws.cell(r, 5).value = rot, imp, nota, iva
    ws = wb['PyG 3 Años']
    assert str(ws['A25'].value).startswith('Seguros') and str(ws['A36'].value).startswith('Amortización')
    for r, (rot, imp) in FIJOS.items():
        ws.cell(r, 1).value, ws.cell(r, 2).value = rot, imp
        ws.cell(r, 6).value = None          # la nota la pone el contenido (FIJOS)
    wb.save(destino)
    return destino


def _copiar_estilo(origen, destino):
    destino.font, destino.border = copy.copy(origen.font), copy.copy(origen.border)
    destino.fill, destino.alignment = copy.copy(origen.fill), copy.copy(origen.alignment)
    destino.number_format, destino.protection = origen.number_format, copy.copy(origen.protection)


def checklist(salida):
    destino = os.path.join(salida, CHECK)
    shutil.copy2(os.path.join(FT, CHECK_FT), destino)
    wb = openpyxl.load_workbook(destino)
    fases = [ws for ws in wb.worksheets if ws.title[:2] in ('F1', 'F2', 'F3', 'F4', 'F5', 'F6')]
    assert len(fases) == 6
    for ws, (titulo, cabecera, tareas) in zip(fases, DC.FASES):
        assert len(titulo) <= 31, titulo
        ws.title = titulo
        ws['A1'], ws['A2'] = DC.TITULO, cabecera
        assert ws['B4'].value and 'TRÁMITE' in ws['B4'].value.upper(), ws['B4'].value
        modelo = [copy.copy(ws.cell(5, c)) for c in range(1, 6)]
        alto = ws.row_dimensions[5].height
        pie = [copy.copy(ws.cell(r, c)) for r in range(5, ws.max_row + 1) for c in range(1, 6)
               if isinstance(ws.cell(r, c).value, str) and 'completad' in ws.cell(r, c).value.lower()]
        assert pie, ws.title
        fila_pie = pie[0].row
        estilo_pie = [copy.copy(ws.cell(fila_pie, c)) for c in range(1, 6)]
        # vaciar la zona de tareas y el pie (valores, DV y formato condicional los rehace el motor)
        for r in range(5, ws.max_row + 1):
            for c in range(1, 6):
                ws.cell(r, c).value = None
            ws.row_dimensions[r].height = None
        ws.data_validations.dataValidation = []
        ws.conditional_formatting = type(ws.conditional_formatting)()
        # revisión final m24: sin desplegable previo, el motor creaba «✓,—,N/A» (motor.VOCAB_MARCA; «✓,☐,N/A» desde el 30-oct-2026) mientras su leyenda
        # de Instrucciones y las casillas dicen «☐»; con este, el motor lo REUTILIZA (`_dv_marca_existente`) y el
        # desplegable, la leyenda y las casillas hablan el mismo idioma («✓,☐,N/A», el de la familia: motor.py:162)
        dv = DataValidation(type='list', formula1='"✓,☐,N/A"', allow_blank=True)
        dv.add('A5:A%d' % (4 + len(tareas)))
        ws.add_data_validation(dv)
        for i, (tarea, resp, plazo, nota) in enumerate(tareas):
            r = 5 + i
            for c, v in enumerate(('☐', tarea, resp, plazo, nota), start=1):
                cel = ws.cell(r, c)
                _copiar_estilo(modelo[c - 1], cel)
                cel.value = v
            ws.row_dimensions[r].height = alto
        r = 5 + len(tareas) + 1
        for c in range(1, 6):
            _copiar_estilo(estilo_pie[c - 1], ws.cell(r, c))
        ws.cell(r, 2).value = 'Tareas completadas:'
        ws.cell(r, 3).value = '=COUNTIF(A5:A%d,"✓")' % (4 + len(tareas))
        ws.cell(r, 4).value = 'de'
        ws.cell(r, 5).value = '=COUNTIF(B5:B%d,"?*")-COUNTIF(A5:A%d,"N/A")' % (4 + len(tareas), 4 + len(tareas))
    # B1: `motor.asegurar_instrucciones` no reescribe la hoja si ya existe: la del FT nombraba su producto
    ins = wb['Instrucciones']
    assert 'plan-negocio-food-truck' in str(ins['A3'].value), ins['A3'].value
    ins['A3'] = 'Este fichero forma parte del «%s» de AI Chef Pro.' % NOMBRE    # m13: el nombre, no el slug
    _docprops(wb)
    wb.save(destino)
    return destino


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--salida', required=True)
    a = ap.parse_args()
    if os.path.isdir(a.salida):
        shutil.rmtree(a.salida)
    os.makedirs(a.salida)
    print('plan      →', plan(a.salida))
    print('checklist →', checklist(a.salida), '(%d tareas: %s)' % (
        sum(len(t) for _, _, t in DC.FASES), '/'.join(str(len(t)) for _, _, t in DC.FASES)))


if __name__ == '__main__':
    main()
