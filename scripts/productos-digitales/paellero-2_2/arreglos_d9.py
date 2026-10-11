#!/usr/bin/env python3
"""
arreglos_d9.py — Paellero para Eventos 2.2 (SPEC D13, D5, D8, D9): arreglos SÓLO de texto en los 7 ficheros NO
rehechos del producto (6 docx + plantilla de proveedores). Cada sustitución exige encontrar EXACTAMENTE su texto en
su párrafo/celda (si no, aborta sin escribir). Parte SIEMPRE de los ficheros publicados de la 1.2 (git show), así que
es repetible. Corre en el VPS (python-docx + openpyxl).

    /root/venv-guias/bin/python arreglos_d9.py --salida /root/tmp-pae-f2/d9     # ensayo: copias corregidas
    /root/venv-guias/bin/python arreglos_d9.py --aplicar                        # escribe en dl/ (paso 3)

Sesión Claude Code, 11-oct-2026.
"""
import argparse
import copy
import datetime
import os
import re
import subprocess
import sys
import tempfile

import docx
import docx.text.paragraph
import openpyxl
from docx.shared import Mm
from openpyxl.worksheet.datavalidation import DataValidation

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
DL = os.path.join(REPO, 'astro-site', 'public', 'dl', 'plan-negocio-paellero-eventos')
#: Ficheros publicados de la 1.2 (último commit de main antes de la 2.2): el script es idempotente.
REV_ORIGEN = '2d6cac44'
VERSION = '2.2'
FECHA = datetime.datetime(2026, 10, 11)

CONTRATO = 'modelos-contrato-paellero-eventos.docx'
CARTA = 'carta-12-paellas-arroces.docx'
PROVEEDORES = 'plantilla-proveedores-paellero-eventos.xlsx'

#: fichero → [(('p', i) | ('t', tabla, fila, col), texto viejo, texto nuevo)]
DOCX = {
    '10-experiencias-tematicas-paellero.docx': [
        (('p', 6), 'Cada una tiene su propio dossier visual, ticket recomendado y storytelling diferenciado.',
         'Cada una tiene su ticket recomendado y su storytelling, y puedes preparar su dossier visual para '
         'presentarla.'),
    ],
    CARTA: [
        (('p', 1), 'Recetas profesionales · Escandallo · Maridaje',
         'Recetas profesionales · Food cost por ración · Maridaje'),
    ],
    'catalogo-equipamiento-utensilios-menaje-paellero.docx': [
        (('p', 1), 'SKU, URL y precio actualizado', 'SKU, URL y precio orientativo'),
        (('p', 2), 'España 2026 · Garcima', 'Edición 2026 · Garcima'),
        (('p', 6), 'precio actualizado a abril 2026', 'precio orientativo de abril 2026 (confírmalo con el proveedor)'),
    ],
    'guia-tipos-paellero-roadmap-food-truck.docx': [],
    'manual-tecnico-paellero-profesional.docx': [],
    CONTRATO: [
        (('p', 2), 'Plantillas validadas con asesor legal — adapta nombre, fecha, importe y demás datos',
         'Plantillas orientativas: revísalas con tu asesor antes de usarlas y adapta nombre, fecha, importe y demás '
         'datos'),
        (('p', 23), 'o efectivo el día del evento.',
         'o en efectivo el día del evento, solo hasta 1.000 € (límite de pagos en efectivo entre un empresario y un '
         'consumidor, art. 7 de la Ley 7/2012).'),
        (('p', 31), 'intervención de la autoridad sanitaria)',
         'intervención de la autoridad sanitaria, la prohibición del uso del fuego o del gas por la época o el nivel '
         'de peligro de incendios)'),
        (('p', 31), 'sin coste adicional. Si la reprogramación',
         'sin coste adicional. Antes de reprogramar, las partes intentarán el plan B pactado en el briefing (cocina '
         'del recinto o equipos sin llama). Si la reprogramación'),
    ],
}

#: Párrafos NUEVOS: fichero → [(índice del párrafo de referencia (del original), 'despues'|'antes', índice del párrafo
#: cuyo formato se copia, texto)]. Los índices son los del original 1.2 (se resuelven antes de insertar nada).
INSERTAR = {
    CONTRATO: [(29, 'despues', 31,
                'Al tratarse de un servicio de comida con fecha determinada, el Cliente no dispone del derecho de '
                'desistimiento (art. 103.l del Texto Refundido de la Ley General para la Defensa de los Consumidores '
                'y Usuarios).')],
    CARTA: [(5, 'antes', 7,
             'Fiestas populares por volumen: una paella grande para un ayuntamiento o una comisión de fiestas, de '
             '300-400 raciones o más, se cobra a 3-6 € por ración sin IVA, con una sola variedad y servicio en plato '
             'desechable. Referencias: contratos menores publicados en la Plataforma de Contratación del Sector '
             'Público (Sayalonga, 2025: 400 raciones de paella mixta con menaje y servicio por 1.480 €) y fichas de '
             'proveedores de paella gigante en Bodas.net (3-10 € por invitado). En las fiestas privadas (cumpleaños, '
             'comuniones, peñas) con una paella y un entrante, el plan financiero usa 18 € por ración; una paella sola '
             'para grupos se cobra a 11-14 € por persona (tarifa publicada de un proveedor de Cataluña, 2026).')],
}

#: Sustituciones por patrón en TODOS los párrafos de un fichero (se exige el nº exacto).
REGEX = {
    CARTA: [
        (re.compile(r'PVP recomendado al cliente: (\d+-\d+) € / pax'),
         r'PVP orientativo por ración (bodas y empresas, con entrantes y show cooking, sin IVA): \1 €', 12),
        (re.compile(r'Food cost estimado: ([\d,]+) € / pax'), r'Food cost estimado: \1 € por ración', 12),
    ],
}

TITULOS = {
    '10-experiencias-tematicas-paellero.docx': '10 Experiencias Temáticas Paellero',
    CARTA: 'Carta 12 Paellas y Arroces',
    'catalogo-equipamiento-utensilios-menaje-paellero.docx': 'Catálogo Equipamiento, Utensilios y Menaje Paellero',
    'guia-tipos-paellero-roadmap-food-truck.docx': 'Guía 8 Sistemas de Cocción + Roadmap Food Truck',
    'manual-tecnico-paellero-profesional.docx': 'Manual Técnico Paellero Profesional',
    CONTRATO: 'Modelos de Contrato Paellero / Paella para Eventos',
}

PROHIBIDAS = ['validad', 'freelance', 'carnet de manipulador', 'manipulador', 'España 2026', 'tarifa plana', 'RGSEAA',
              'PATRICOVA', 'INFOCYL', 'PIDOM', 'sin licencia']


def _sustituir_parrafo(p, viejo, nuevo):
    """Sustituye la 1.ª aparición de `viejo` conservando el formato: dentro de un run, o fusionando sólo los runs
    afectados (el texto fusionado toma el formato del primero)."""
    for r in p.runs:
        if viejo in r.text:
            r.text = r.text.replace(viejo, nuevo, 1)
            return True
    runs = p.runs
    texto = ''.join(r.text for r in runs)
    i = texto.find(viejo)
    if i < 0:
        return False
    j = i + len(viejo)
    pos = 0
    primero = None
    for r in runs:
        ini, fin = pos, pos + len(r.text)
        pos = fin
        if fin <= i or ini >= j:
            continue
        if primero is None:
            primero = r
            r.text = r.text[:i - ini] + nuevo + (r.text[j - ini:] if fin >= j else '')
        else:
            r.text = r.text[j - ini:] if fin > j else ''
    return primero is not None


def _clonar(base, texto):
    nuevo = copy.deepcopy(base._p)
    p = docx.text.paragraph.Paragraph(nuevo, base._parent)
    for r in p.runs[1:]:
        r._r.getparent().remove(r._r)
    p.runs[0].text = texto
    return nuevo


def _textos(d):
    for p in d.paragraphs:
        yield p.text
    for t in d.tables:
        for row in t.rows:
            for c in row.cells:
                yield c.text
    for s in d.sections:
        for p in list(s.header.paragraphs) + list(s.footer.paragraphs):
            yield p.text


def docx_(origen, destino, reglas, log):
    d = docx.Document(origen)
    f = os.path.basename(destino)
    corto = f[:28]
    # (1) sustituciones por índice (los índices son los del original)
    for donde, viejo, nuevo in reglas:
        if donde[0] == 'p':
            p = d.paragraphs[donde[1]]
            sitio = 'p%d' % donde[1]
        else:
            p = d.tables[donde[1]].rows[donde[2]].cells[donde[3]].paragraphs[0]
            sitio = 't%d.r%d.c%d' % donde[1:]
        if viejo not in p.text or not _sustituir_parrafo(p, viejo, nuevo):
            raise SystemExit('ABORTADO: %s %s no contiene «%s» (texto: «%s»)' % (f, sitio, viejo, p.text[:120]))
        log.append((f, '%s %s: «%s» → «%s»' % (corto, sitio, viejo[:50], nuevo[:60])))
    # (2) sustituciones por patrón
    for rx, repl, esperado in REGEX.get(f, []):
        n = 0
        for p in d.paragraphs:
            m = rx.search(p.text)
            if m:
                if not _sustituir_parrafo(p, m.group(0), m.expand(repl)):
                    raise SystemExit('ABORTADO: %s no pude sustituir «%s»' % (f, m.group(0)))
                n += 1
        if n != esperado:
            raise SystemExit('ABORTADO: %s patrón %s: %d coincidencias (esperadas %d)' % (f, rx.pattern, n, esperado))
        log.append((f, '%s: patrón «%s» ×%d' % (corto, rx.pattern[:40], n)))
    # (3) párrafos nuevos (referencias resueltas ANTES de insertar)
    for ref, modo, molde, texto in INSERTAR.get(f, []):
        ps = d.paragraphs
        base, mold = ps[ref], ps[molde]
        nuevo = _clonar(mold, texto)
        if modo == 'despues':
            base._p.addnext(nuevo)
        else:
            base._p.addprevious(nuevo)
        log.append((f, '%s p%d %s: párrafo nuevo «%s»' % (corto, ref, modo, texto[:60])))
    for s in d.sections:
        s.page_width, s.page_height = Mm(210), Mm(297)
    cp = d.core_properties
    base_t = re.sub(r'\s*·\s*v\d+(\.\d+)*\s*$', '', cp.title or TITULOS[f]) or TITULOS[f]
    cp.title = '%s · v%s' % (base_t, VERSION)
    cp.author = cp.last_modified_by = 'AI Chef Pro'
    cp.comments = 'aichef.pro/plan-negocio-paellero-eventos'
    cp.created = cp.modified = FECHA
    d.save(destino)
    log.append((f, '%s: A4 + docProps (autor, fechas, comments, title v%s)' % (corto, VERSION)))


def proveedores(origen, destino, log):
    wb = openpyxl.load_workbook(origen)
    ws = wb.worksheets[0]
    assert ws.title == '88 proveedores', ws.title
    assert ws['G4'].value == 'Estado', ws['G4'].value
    assert ws['A1'].value == '88 Proveedores Reales — Paellero / Paella para Eventos', ws['A1'].value
    ws['A1'] = '88 proveedores — Paellero / Paella para Eventos'
    viejo = 'Validados España 2026 · '
    assert str(ws['A2'].value).startswith(viejo), ws['A2'].value
    ws['A2'] = ws['A2'].value[len(viejo):]
    n = 0
    for r in range(5, 93):
        if ws.cell(r, 7).value == 'Validado':
            ws.cell(r, 7).value = 'Por verificar'
            n += 1
    assert n == 69, n
    assert not any(ws.cell(r, 7).value == 'Validado' for r in range(5, ws.max_row + 1))
    dv = DataValidation(type='list', formula1='"Por verificar,Contactado,Homologado,Investigar"', allow_blank=True)
    dv.add('G5:G92')
    ws.add_data_validation(dv)
    pr = wb.properties
    pr.title = '88 proveedores — Paellero / Paella para Eventos · v%s' % VERSION
    pr.subject = (pr.subject or '').replace('v1.1', 'v' + VERSION).replace('v1.2', 'v' + VERSION)
    pr.creator = pr.lastModifiedBy = 'AI Chef Pro'
    pr.description = 'aichef.pro/plan-negocio-paellero-eventos'
    pr.created = pr.modified = FECHA
    wb.save(destino)
    log.append((PROVEEDORES, '%s: A1/A2 sin «Reales»/«Validados España 2026» · G «Validado» → «Por verificar» en %d '
                             'filas · DV G5:G92 · docProps v%s' % (PROVEEDORES[:28], n, VERSION)))


def barrido(dest):
    hay = []
    for f in list(DOCX):
        d = docx.Document(os.path.join(dest, f))
        for t in _textos(d):
            for pal in PROHIBIDAS:
                if pal.lower() in t.lower():
                    hay.append('%s: «%s» en «%s»' % (f[:30], pal, t[:90]))
        for a in ('title', 'subject', 'comments', 'author'):
            v = getattr(d.core_properties, a) or ''
            if 'python-docx' in v:
                hay.append('%s: docProps %s con python-docx' % (f[:30], a))
    wb = openpyxl.load_workbook(os.path.join(dest, PROVEEDORES))
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str):
                    for pal in PROHIBIDAS:
                        if pal.lower() in c.value.lower():
                            hay.append('%s %s: «%s» en «%s»' % (PROVEEDORES[:20], c.coordinate, pal, c.value[:80]))
    pr = wb.properties
    for pal in ('Reales',):
        for v in (pr.title, pr.subject):
            if v and pal in v:
                hay.append('xlsx docProps «%s»: %s' % (pal, v))
    return hay


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
    print('\n'.join(l for _, l in log))
    por = {}
    for f, _ in log:
        por[f] = por.get(f, 0) + 1
    for f, n in por.items():
        print('  %3d  %s' % (n, f))
    print('D9: %d sustituciones/arreglos en %d ficheros → %s' % (len(log), len(DOCX) + 1, dest))
    hay = barrido(dest)
    if hay:
        print('BARRIDO: %d coincidencias prohibidas' % len(hay))
        print('\n'.join(hay))
        return 1
    print('BARRIDO: 0 coincidencias prohibidas')
    return 0


if __name__ == '__main__':
    sys.exit(main())
