#!/usr/bin/env python3
"""
semilla_pae.py — Paellero ES 2.2 (SPEC D1/D3/D10): prepara el ORIGEN que `planes-v2_0/main.py` convierte en el plan
financiero y el checklist del paellero. Copia adaptada de `catering-es-2_0/semilla_cat.py`.

Copia los dos xlsx del Food Truck ES v2.2 publicados (`dl/plan-negocio-food-truck/`, SOLO LECTURA) con los nombres de
fichero del paellero y escribe lo que el módulo de contenido no alcanza (F1-camino §1):
  · plan: títulos de hoja heredados del fichero (Inversión A1/A2, PyG A2, Punto Equilibrio A2), las 14 partidas de
    inversión (filas 7-20: rótulo, importe, nota, ¿IVA?) y los costes fijos propios del P&L (filas 26-35);
  · checklist: título, pestañas, cabeceras de fase y las 83 tareas de `datos_checklist.py` (12/16/14/10/16/15) con el
    pie «Tareas completadas:» debajo; DV, formato condicional y contadores los rehace el motor (`checklist_ok_y_contador`).
Corre en el VPS (openpyxl). Después: `main.py --producto plan-negocio-paellero-eventos --dry-run --origen <salida>`.

    /root/venv-guias/bin/python semilla_cat.py --salida /root/tmp-pae-f2/origen

Sesión Claude Code, 11-oct-2026.
"""
import argparse
import copy
import os
import shutil

import importlib
import sys

import openpyxl

import datos_checklist as DC

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
FT = os.path.join(REPO, 'astro-site', 'public', 'dl', 'plan-negocio-food-truck')
PLAN_FT, CHECK_FT = 'plan-financiero-food-truck.xlsx', 'checklist-apertura-food-truck.xlsx'
PLAN, CHECK = 'plan-financiero-paellero-eventos.xlsx', 'checklist-apertura-paellero-eventos.xlsx'
PID = 'plan-negocio-paellero-eventos'

TITULOS_PLAN = {
    ('Inversión Inicial', 'A1'): 'PLAN DE NEGOCIO: PAELLERO / PAELLA PARA EVENTOS',
    ('Inversión Inicial', 'A2'): 'Inversión inicial estimada — paella y arroces en directo para eventos',
    ('PyG 3 Años', 'A2'): 'Escenario realista — paellero para eventos',
    ('Punto Equilibrio', 'A2'): 'Punto de equilibrio — paellero para eventos',
}

#: Filas 7-20 de 'Inversión Inicial' (molde FT): (rótulo, importe, nota, ¿lleva IVA?). Research §3: 38.450 € en 15
#: partidas; «web, fotos, marca y dossier» (2.500) y «lanzamiento» (2.000) van juntas para caber en las 14 filas.
#: Sin palabras de recuento en el rótulo (motor.RX_RECUENTO).
INVERSION = [
    ('Furgoneta isoterma usada con certificado ATP', 18000,
     'Furgoneta usada con caja isoterma y equipo de frío, con el certificado ATP vigente (RD 237/2000) para llevar '
     'carne y marisco. Estimación del kit', 'Sí'),
    ('Rotulación, estanterías y anclajes de botellas', 1200,
     'Rotulación con la marca, estanterías con amarres y anclajes para llevar las botellas de gas en pie y sujetas',
     'Sí'),
    ('Paelleras de 60 a 150 cm', 2400,
     'Diez paelleras de 60 a 120 cm y una de 150 cm para fiestas populares (90-120 raciones). Una de 90 cm ronda '
     'los 61 € (ManoMano, octubre de 2026)', 'Sí'),
    ('Quemadores de anillos, patas y trípodes de leña', 2100,
     'Quemadores de 2 a 5 anillos con sus patas y dos trípodes para cocinar con leña donde esté permitido', 'Sí'),
    ('Gas y seguridad: reguladores, flexibles, extintores y manta ignífuga', 950,
     'Reguladores, tubos flexibles en fecha, tres extintores de polvo ABC, manta ignífuga, cortavientos y el '
     'depósito de los envases de propano', 'Sí'),
    ('Neveras, isotermos GN, sondas y acumuladores', 1500,
     'Cadena de frío del marisco y la carne desde la cocina de apoyo hasta el evento, y sondas para el registro '
     'del APPCC', 'Sí'),
    ('Carpa, mesas plegables, lavamanos portátil y protector de suelo', 1800,
     'Zona de cocción bajo carpa, mesa de show cooking, lavamanos para el personal y protector del césped o del '
     'pavimento', 'Sí'),
    ('Utensilios, ollas de caldo, cuchillería y básculas', 1600,
     'Paletas, cucharas, ollas de caldo de 50 litros, cuchillería, tablas de colores y básculas', 'Sí'),
    ('Uniformes y EPI térmicos', 400, 'Chaquetas, delantales y guantes resistentes al calor', 'Sí'),
    ('Marca, web, fotos, dossier y lanzamiento', 4500,
     'Identidad, web con formulario de presupuesto, sesión de fotos y vídeo, dossier para bodas, empresas y '
     'ayuntamientos, y degustaciones de lanzamiento', 'Sí'),
    ('Software, tablet y datáfono', 800, 'Presupuestos, agenda y facturación conforme a Veri*factu', 'Sí'),
    ('Constitución SL + notaría + registro', 1000,
     'SL unipersonal. Las tasas y el arancel del Registro no llevan IVA; los honorarios del notario y de la '
     'gestoría sí: cambia la columna de al lado a «Sí» si tu presupuesto es sobre todo de honorarios', 'No'),
    ('Declaración responsable, plan APPCC, alérgenos y formación', 1200,
     'Redacción del plan APPCC, fichas de alérgenos de cada arroz, formación en higiene alimentaria del equipo y '
     'trámites sanitarios', 'Sí'),
    ('Stock inicial de producto', 1000, 'Arroz, especias, aceite, desechables y la primera carga de gas', 'Sí'),
]
assert len(INVERSION) == 14 and sum(x[1] for x in INVERSION) == 38450

#: Filas 26-35 de 'PyG 3 Años' (costes fijos propios). Research §3: 9.900 €/año en 9 partidas; la fila restante del
#: molde se llena con un coste real [estimado] (permisos municipales, 200 €) en vez de suprimirla: suprimir filas
#: desplaza el P&L y el motor lo cuenta como fórmulas perdidas (catering, F2-NOTAS §3.4). Sin «eventos»,
#: «clientes» ni «días» en el rótulo (motor.RX_RECUENTO).
FIJOS = {
    26: ('Asesoría fiscal y laboral (nóminas de fijos discontinuos)', 1800),
    27: ('Furgoneta: mantenimiento, ITV e inspección ATP', 1200),
    28: ('Marketing y publicidad', 4000),
    29: ('Software de gestión comercial, CRM y teléfono', 900),
    30: ('Revisión de gas por instaladora y mantenimiento de extintores', 400),
    31: ('Uniformes y lavandería', 400),
    32: ('Gestión de residuos (orgánico y aceite usado)', 200),
    33: ('Prevención de riesgos laborales y vigilancia de la salud', 400),
    34: ('Pruebas de arroz y degustaciones comerciales', 600),
    35: ('Permisos y autorizaciones municipales', 200),
}


def _supuestos(wb):
    """Los valores de `0. Supuestos` del caso paellero. `grupo_a` CONSERVA lo que el libro ya trae en las celdas
    verdes (§1.3: dato del cliente) y sólo usa el valor del contenido en una celda vacía: partiendo del libro del
    FT, sin este paso el caso seguiría siendo el del food truck (45 × 12 € × 250, medido en el primer dry-run)."""
    p2 = os.path.join(os.path.dirname(AQUI), 'planes-v2_0')
    sys.path.insert(0, p2)
    import grupo_a
    contenido = importlib.import_module('contenido_plan_negocio_paellero_eventos.a')
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
    """REVISION-FINAL B1: el motor no reescribe `description` ni `keywords` y heredaba los del FT."""
    wb.properties.description = 'aichef.pro/' + PID
    wb.properties.keywords = 'plan negocio paellero eventos, AI Chef Pro'


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
    ins['A3'] = 'Este fichero forma parte del producto «%s» de AI Chef Pro.' % PID
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
