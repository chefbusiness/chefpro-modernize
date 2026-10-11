#!/usr/bin/env python3
"""
arreglos_d9.py — Catering ES 2.0 (SPEC D9): arreglos SÓLO de texto en los otros 7 ficheros del producto (F1-camino §5):
fuera «validado(s) España 2026» y «research», «freelance» → personal fijo discontinuo, inversión alineada con el plan,
RGSEAA → registro autonómico, IVA de los servicios asociados aclarado, columna «Estado» de proveedores → «Por
verificar». Cada sustitución exige encontrar EXACTAMENTE su texto en su párrafo/celda (si no, aborta sin escribir).
Corre en el VPS (python-docx + openpyxl).

    /root/venv-guias/bin/python arreglos_d9.py --salida /root/tmp-cates-f2/d9     # ensayo: copias corregidas
    /root/venv-guias/bin/python arreglos_d9.py --aplicar                          # escribe en dl/ (paso 3)

Sesión Claude Code, 11-oct-2026.
"""
import argparse
import os
import shutil
import sys

import docx
import openpyxl

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
DL = os.path.join(REPO, 'astro-site', 'public', 'dl', 'plan-catering-tematico-eventos')

#: fichero → [(('p', i) | ('t', tabla, fila, col), texto viejo, texto nuevo)]
DOCX = {
    '12-conceptos-tematicos-pre-empaquetados.docx': [
        (('p', 2), 'Conceptos validados España 2026 con menú, escandallo, ambientación y pricing',
         'Edición 2026 · conceptos con menú, escandallo, ambientación y precio orientativo'),
    ],
    'carta-12-menus-tematicos-cocinas-mundo.docx': [
        (('p', 2), 'Recetario operativo premium validado España 2026', 'Recetario operativo premium · edición 2026'),
    ],
    'catalogo-equipamiento-multi-cocina-catering-tematico.docx': [
        (('p', 2), 'Marcas y modelos validados España 2026', 'Marcas y modelos de referencia · edición 2026'),
        (('p', 6), 'aquí necesitas equipamiento especializado por cada cocina del mundo que ofrezcas',
         'aquí necesitas equipamiento especializado para cada estación temática que vendas (empieza por dos o tres, '
         'no por todas)'),
        (('t', 10, 1, 2), '16.000 € usado / 380 €/mes',
         '18.000-22.000 € usada con equipo de frío y certificado ATP (el plan financiero presupuesta 22.000 €)'),
    ],
    'guia-especializacion-catering-tematico-multi-concepto.docx': [
        (('p', 14), 'Inversión inicial moderada (5.500-8.500 €)',
         'La inversión inicial del plan financiero (furgoneta, estaciones, menaje y fondo de maniobra)'),
        (('p', 18), 'busca un freelance especializado de confianza',
         'busca un cocinero especialista de confianza para tu bolsa de fijos discontinuos'),
        (('p', 38), 'Según el research del mercado España 2026, los 5 conceptos con mejor relación demanda / '
                    'complejidad / margen son:',
         'Por demanda, complejidad de arranque y margen orientativo, estos 5 conceptos son los más recomendables para '
         'empezar:'),
        (('p', 40), 'El research detectó conceptos con demanda creciente y oferta escasa:',
         'Conceptos con demanda creciente y poca oferta (criterio del autor):'),
        (('p', 47), 'Subcontratar freelance que no conoces antes de un evento grande.',
         'Llamar para un evento grande a un especialista con el que nunca has trabajado.'),
        (('p', 50), 'el equipo freelance no replica calidad', 'el equipo de eventos no replica la calidad'),
        (('t', 0, 0, 4), 'Margen', 'Margen bruto orientativo'),
    ],
    'manual-tecnico-multi-cocina-appcc-catering.docx': [
        (('p', 2), 'Protocolos profesionales validados España 2026', 'Protocolos profesionales · edición 2026'),
        (('p', 55), 'Coordinación equipo freelance multi-concepto', 'Coordinación del equipo de eventos multi-concepto'),
        (('p', 56), 'requiere equipo freelance especializado por concepto',
         'requiere personal especializado por concepto, contratado como fijo discontinuo o a través de una ETT'),
        (('p', 57), 'Bolsa de freelance fiables', 'Bolsa de fijos discontinuos fiables'),
        (('p', 59), 'que el freelance lee D-1', 'que el equipo lee el día antes'),
        (('p', 62), 'el freelance estrella', 'el especialista estrella'),
        (('p', 69), 'Inscripción RGSEAA si transportas alimentos elaborados.',
         'Inscripción en el registro sanitario autonómico previa declaración responsable (RD 1021/2022); el RGSEAA '
         'sólo si suministras a otros establecimientos.'),
        (('t', 1, 9, 1), 'briefing equipo freelance', 'briefing del equipo de eventos'),
    ],
    'modelos-contrato-catering-tematico-b2c-b2b.docx': [
        (('p', 2), 'Plantillas legales adaptadas España 2026', 'Plantillas de contrato B2C y B2B · edición 2026'),
        (('p', 76), '(10 % catering / 21 % servicios asociados)',
         '(10 % el catering y los servicios accesorios que se facturen con él; 21 % los servicios que se facturen '
         'aparte, como mobiliario, carpas o decoración)'),
    ],
}
PROVEEDORES = 'plantilla-proveedores-catering-tematico-eventos.xlsx'


def _sustituir_parrafo(p, viejo, nuevo):
    for r in p.runs:
        if viejo in r.text:
            r.text = r.text.replace(viejo, nuevo, 1)
            return True
    return False


def docx_(origen, destino, reglas, log):
    d = docx.Document(origen)
    for donde, viejo, nuevo in reglas:
        if donde[0] == 'p':
            p = d.paragraphs[donde[1]]
            sitio = 'p%d' % donde[1]
        else:
            p = d.tables[donde[1]].rows[donde[2]].cells[donde[3]].paragraphs[0]
            sitio = 't%d.r%d.c%d' % donde[1:]
        if viejo not in p.text or not _sustituir_parrafo(p, viejo, nuevo):
            raise SystemExit('ABORTADO: %s %s no contiene «%s» (texto: «%s»)' % (os.path.basename(origen), sitio,
                                                                             viejo, p.text[:120]))
        log.append('%s %s: «%s» → «%s»' % (os.path.basename(origen)[:28], sitio, viejo[:50], nuevo[:60]))
    d.save(destino)


def proveedores(origen, destino, log):
    wb = openpyxl.load_workbook(origen)
    ws = wb.worksheets[0]
    assert ws['G4'].value == 'Estado', ws['G4'].value
    viejo = 'Validados España 2026 · '
    assert str(ws['A2'].value).startswith(viejo), ws['A2'].value
    ws['A2'] = ws['A2'].value[len(viejo):] + ' · comprueba disponibilidad y condiciones antes de pedir'
    n = 0
    for r in range(5, ws.max_row + 1):
        if ws.cell(r, 7).value == 'Validado':
            ws.cell(r, 7).value = 'Por verificar'
            n += 1
    assert n >= 90, n
    wb.save(destino)
    log.append('%s: A2 sin «Validados España 2026» · G «Validado» → «Por verificar» en %d filas' % (PROVEEDORES[:28], n))


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--salida')
    g.add_argument('--aplicar', action='store_true')
    a = ap.parse_args()
    dest = DL if a.aplicar else a.salida
    os.makedirs(dest, exist_ok=True)
    log = []
    for f, reglas in DOCX.items():
        docx_(os.path.join(DL, f), os.path.join(dest, f), reglas, log)
    proveedores(os.path.join(DL, PROVEEDORES), os.path.join(dest, PROVEEDORES), log)
    if not a.aplicar:
        for f in sorted(os.listdir(DL)):
            if f not in DOCX and f != PROVEEDORES:
                pass
    print('\n'.join(log))
    print('D9: %d sustituciones en %d ficheros → %s' % (len(log), len(DOCX) + 1, dest))


if __name__ == '__main__':
    sys.exit(main())
