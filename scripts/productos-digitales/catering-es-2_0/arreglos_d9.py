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
import copy
import datetime
import os
import subprocess
import sys
import tempfile

import docx
import docx.text.paragraph
import openpyxl
from docx.shared import Mm

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
DL = os.path.join(REPO, 'astro-site', 'public', 'dl', 'plan-catering-tematico-eventos')

#: fichero → [(('p', i) | ('t', tabla, fila, col), texto viejo, texto nuevo)]
DOCX = {
    '12-conceptos-tematicos-pre-empaquetados.docx': [
        (('p', 2), 'Conceptos validados España 2026 con menú, escandallo, ambientación y pricing',
         'Edición 2026 · conceptos con menú, ambientación, equipamiento, operativa y precio orientativo'),
    ],
    'carta-12-menus-tematicos-cocinas-mundo.docx': [
        (('p', 2), 'Recetario operativo premium validado España 2026', 'Recetario operativo premium · edición 2026'),
        (('p', 5), 'Menú Boda Multicultural Premium 7 estaciones',
         'Menú Boda Multicultural Premium 6 estaciones + activación previa'),
    ],
    'catalogo-equipamiento-multi-cocina-catering-tematico.docx': [
        (('p', 2), 'Marcas y modelos validados España 2026', 'Marcas y modelos de referencia · edición 2026'),
        (('p', 6), 'aquí necesitas equipamiento especializado por cada cocina del mundo que ofrezcas',
         'aquí necesitas equipamiento especializado para cada estación temática que vendas (empieza por dos o tres, '
         'no por todas)'),
        (('p', 6), 'empezar con 1-2 conceptos dominados', 'empezar con dos o tres conceptos dominados'),
        (('t', 10, 1, 2), '16.000 € usado / 380 €/mes',
         '18.000-22.000 € usada con equipo de frío y certificado ATP (el plan financiero presupuesta 22.000 €)'),
    ],
    'guia-especializacion-catering-tematico-multi-concepto.docx': [
        (('p', 14), 'Inversión inicial moderada (5.500-8.500 €), branding básico, captación B2C focalizada en tu zona, '
                    'consolidación operativa, primeras 30-50 reseñas Google.',
         'La etapa 1 incluye la inversión inicial del plan financiero (furgoneta, estaciones, menaje y fondo de '
         'maniobra), una marca básica, captación de particulares en tu zona y las primeras 30-50 reseñas en Google.'),
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
        (('p', 60), 'Pago mismo día post-evento + bonus por evento bien resuelto.',
         'Nómina mensual con las horas de cada llamamiento + plus por evento pactado por escrito.'),
        (('p', 62), 'el freelance estrella', 'el especialista estrella'),
        (('p', 65), 'Carnet manipulador alimentos (vigente) + carnet específico si aplica (japonés/marisquería).',
         'Formación en higiene alimentaria acreditada por la empresa (Reglamento (CE) 852/2004, anexo II, cap. XII), '
         'con un módulo de pescado crudo y anisakis si sirves sushi o ceviche.'),
        (('p', 68), 'Alta autónomo + IAE 677.9.', 'Alta de la empresa (SL o autónomo) en el IAE 677.9.'),
        (('p', 69), 'Inscripción RGSEAA si transportas alimentos elaborados.',
         'Inscripción en el registro sanitario autonómico previa declaración responsable (RD 1021/2022); el RGSEAA '
         'sólo si suministras a otros establecimientos.'),
        (('t', 1, 9, 1), 'briefing equipo freelance', 'briefing del equipo de eventos'),
    ],
    'modelos-contrato-catering-tematico-b2c-b2b.docx': [
        (('p', 2), 'Plantillas legales adaptadas España 2026', 'Plantillas de contrato B2C y B2B · edición 2026'),
        (('p', 13), 'formación (manipulador vigente, APPCC móvil)', 'formación en higiene alimentaria y APPCC móvil'),
        (('p', 27), 'Resto del 60 % en las 24-48 horas posteriores al evento', 'Resto del 60 % siete días antes del evento'),
        (('p', 41), 'entregar la cocina y el espacio del evento', 'entregar el espacio del evento'),
        (('p', 43), ' El CLIENTE garantiza tener seguro hogar con cobertura ampliada para incidentes producidos por '
                    'terceros profesionales en su domicilio.', ''),
        (('p', 47), 'sus derechos ARSULPO',
         'sus derechos de acceso, rectificación, supresión, limitación, portabilidad y oposición'),
        (('p', 76), '(10 % catering / 21 % servicios asociados)',
         '(10 % el catering y los servicios accesorios que se facturen con él; 21 % los servicios que se facturen '
         'aparte, como mobiliario, carpas o decoración)'),
    ],
}
PROVEEDORES = 'plantilla-proveedores-catering-tematico-eventos.xlsx'
#: Ronda de arreglos (REVISION-FINAL m10): párrafo NUEVO tras la última línea de cancelación del contrato B2C (p33),
#: con el formato de esa línea. Va DESPUÉS de las sustituciones por índice.
INSERTAR = {'modelos-contrato-catering-tematico-b2c-b2b.docx': (
    33, 'Al tratarse de un servicio de comida con fecha determinada, el CLIENTE no dispone del derecho de '
        'desistimiento (art. 103.l del TRLGDCU).')}
#: REVISION-FINAL m13: A4 y docProps de los 7 (estaban en US Letter y «python-docx / 2013»).
TITULOS = {
    '12-conceptos-tematicos-pre-empaquetados.docx': '12 Conceptos Temáticos Pre-empaquetados',
    'carta-12-menus-tematicos-cocinas-mundo.docx': 'Carta de 12 Menús Temáticos de Cocinas del Mundo',
    'catalogo-equipamiento-multi-cocina-catering-tematico.docx': 'Catálogo de Equipamiento Multi-cocina',
    'guia-especializacion-catering-tematico-multi-concepto.docx': 'Guía de Especialización Progresiva',
    'manual-tecnico-multi-cocina-appcc-catering.docx': 'Manual Técnico Multi-cocina y APPCC',
    'modelos-contrato-catering-tematico-b2c-b2b.docx': 'Modelos de Contrato B2C y B2B',
}
VERSION = '2.2'
#: Los arreglos parten SIEMPRE de los ficheros 1.1 (último commit de main antes de la 2.x): así el script es
#: idempotente y se puede volver a correr después de aplicarlo.
REV_ORIGEN = 'ee9c03b1'


def _sustituir_parrafo(p, viejo, nuevo):
    for r in p.runs:
        if viejo in r.text:
            r.text = r.text.replace(viejo, nuevo, 1)
            return True
    return False


def docx_(origen, destino, reglas, log):
    d = docx.Document(origen)
    f = os.path.basename(destino)
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
    if f in INSERTAR:
        i, texto = INSERTAR[f]
        base = d.paragraphs[i]
        nuevo_p = copy.deepcopy(base._p)
        base._p.addnext(nuevo_p)
        p = docx.text.paragraph.Paragraph(nuevo_p, base._parent)
        for r in p.runs[1:]:
            r._r.getparent().remove(r._r)
        p.runs[0].text = texto
        log.append('%s p%d+: párrafo nuevo «%s»' % (f[:28], i, texto[:60]))
    for s in d.sections:
        s.page_width, s.page_height = Mm(210), Mm(297)
    cp = d.core_properties
    cp.title = '%s — Catering Temático de Eventos · v%s' % (TITULOS[f], VERSION)
    cp.subject = 'Plan de Negocio: Catering Temático de Eventos'
    cp.author = cp.last_modified_by = 'AI Chef Pro'
    cp.comments = 'aichef.pro/plan-catering-tematico-eventos'
    cp.created = cp.modified = datetime.datetime.now().replace(microsecond=0)
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
    pr = wb.properties
    for campo in ('title', 'subject'):
        v = getattr(pr, campo) or ''
        if 'v1.1' in v:
            setattr(pr, campo, v.replace('v1.1', 'v' + VERSION))
    pr.creator = pr.lastModifiedBy = 'AI Chef Pro'
    pr.description = 'aichef.pro/plan-catering-tematico-eventos'
    wb.save(destino)
    log.append('%s: A2 sin «Validados España 2026» · G «Validado» → «Por verificar» en %d filas · docProps v%s' % (
        PROVEEDORES[:28], n, VERSION))


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--salida')
    g.add_argument('--aplicar', action='store_true')
    a = ap.parse_args()
    dest = DL if a.aplicar else a.salida
    os.makedirs(dest, exist_ok=True)
    log = []
    tmp = tempfile.mkdtemp(prefix='d9-origen-')
    for f in list(DOCX) + [PROVEEDORES]:
        rel = os.path.relpath(os.path.join(DL, f), REPO)
        with open(os.path.join(tmp, f), 'wb') as fh:
            fh.write(subprocess.check_output(['git', '-C', REPO, 'show', '%s:%s' % (REV_ORIGEN, rel)]))
    for f, reglas in DOCX.items():
        docx_(os.path.join(tmp, f), os.path.join(dest, f), reglas, log)
    proveedores(os.path.join(tmp, PROVEEDORES), os.path.join(dest, PROVEEDORES), log)
    print('\n'.join(log))
    print('D9: %d sustituciones en %d ficheros → %s' % (len(log), len(DOCX) + 1, dest))


if __name__ == '__main__':
    sys.exit(main())
