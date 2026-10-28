#!/usr/bin/env python3
"""
fuente_cof.py — material de CONTENIDO para los redactores, desde el gemelo ES «Plan de Negocio: Cafetería Móvil para
Eventos» 1.0 (en F2 el 28-oct-2026): el checklist ES (`datos_checklist.py`, sin abrir el xlsx), los párrafos ES del plan
en las 61 ranuras del docx (`textos/caf_es_{a,b}.json`, con sus {TOKENS}), el contrato ES (`textos/contrato_es.json`), la
tabla de escalado (`datos_escalado.py`) y, si ya existe, la calculadora ES (`calculadora-escandallo-presupuesto-cafe-
eventos.xlsx`: hojas, rótulos y fórmulas) → `fuente_es_cof.json`. El circuito de texto corre sobre el FOOD TRUCK ES (las
ranuras); el contenido de café sale de aquí y de research (D221, D228, D229). Sus CIFRAS no se usan (D231).

Lo que falta se lista en `pendientes` (paso 1c: re-extraer cuando el ES pase su revisión y vuelva a correr). Orígenes:
  COF_FUENTE_ES = carpeta de los scripts ES (por defecto `../plan-cafeteria-movil/`; en el VPS, durante la F2 del ES,
                  `/root/wt-cafemovil/scripts/productos-digitales/plan-cafeteria-movil`, SOLO LECTURA)
  COF_DL_ES     = carpeta de los entregables ES (por defecto `astro-site/public/dl/plan-negocio-cafeteria-movil-eventos/`;
                  durante la F2 del ES, su salida en `/root/tmp-caf-f2/…`, SOLO LECTURA)
Corre en el VPS (openpyxl solo si hay calculadora). Clon de `../business-plans-en-7/fuente_pael.py`. Sesión Claude Code,
28-oct-2026 (paso 1a).

    COF_FUENTE_ES=… COF_DL_ES=… python3 bp11.py fuente
"""
import datetime
import glob
import hashlib
import importlib.util
import json
import os
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
CAF = os.environ.get('COF_FUENTE_ES') or os.path.join(os.path.dirname(AQUI), 'plan-cafeteria-movil')
DL = os.environ.get('COF_DL_ES') or os.path.join(REPO, 'astro-site', 'public', 'dl', 'plan-negocio-cafeteria-movil-eventos')
CALC = 'calculadora-escandallo-presupuesto-cafe-eventos.xlsx'
# fases ES (SPEC ES §4) → fase EN sugerida (rejilla de 68 de la paella, D228)
FASE_EN = OrderedDict([
    (1, 'P1 Business Setup (constitución → LLC, EIN, sales tax permit, business license, préstamo, contrato con '
        'abogado, plan de seguridad alimentaria, CFPM)'),
    (2, 'P2 Permits & Commissary (vehículo y sanidad → commissary + agreement, mobile food unit permit + plan review, '
        'temporary event permits, fire marshal y generador, comprar el carro, el remolque en el DMV, GL + COI, alcohol '
        'fuera, aguas grises)'),
    (3, 'P3 Equipment (equipo y proveedores → máquinas y molinos, cadena de frío de la leche, tostador y leches, '
        'smallwares, siropes y alt milks, segunda estación, agua, vasos compostables, evento de prueba)'),
    (4, 'P4 Staff (personal y formación → baristas por evento, W-2, I-9 / W-4, propinas, food handler cards, seguridad '
        'del barista, OSHA, protocolo de servicio y alérgenos)'),
    (5, 'P5 Marketing (marca y captación → carta, web, Google, The Knot / Zola, GigSalad / Thumbtack / The Bash, '
        'presupuestos con la calculadora, prospección B2B, open house y bridal show)'),
    (6, 'P6 First 90 Days (primer evento → llamada final, comprobación de la sala, pedidos, carga, montaje y servicio, '
        'recogida, reseña, revisión frente a la calculadora)'),
])
USO = ('CONTENIDO de coffee catering para los redactores (D221, D228, D229). NO se traduce tal cual: se condensa y se '
       'adapta a EE. UU. con research (F1-research-us-delta.md §1-§9, glosario §9 obligatorio). Las CIFRAS del ES NO se '
       'usan (D231: 107.055 €, 130 eventos, 135 invitados, 6,10 €…): las del caso salen del libro EN (tokens). Fuera: '
       'IVA, autónomo, fijo discontinuo, convenio, SMI, RD / Ley / Reglamento, registro sanitario autonómico, comida '
       'testigo, ITV, Piaggio / Ape, furgoneta (aquí: remolque cerrado), «feria» (aquí: festival / farmers market), '
       'Bizum, «cafetería» (falso amigo: coffee cart / mobile espresso bar), litros, kg y °C como unidad principal, '
       '«ChefBusiness»')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def _modulo(nombre):
    p = os.path.join(CAF, nombre)
    if not os.path.exists(p):
        return p, None
    spec = importlib.util.spec_from_file_location(nombre[:-3] + '_caf', p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return p, m


def checklist():
    p, m = _modulo('datos_checklist.py')
    if m is None or not hasattr(m, 'FASES'):
        return p, None, None
    fases = OrderedDict()
    for k, fase in enumerate(m.FASES, 1):
        hoja, titulo, tareas = fase[0], fase[1], fase[2]
        lista = []
        for j, t in enumerate(tareas, 1):
            t = list(t) + [''] * 4
            lista.append(OrderedDict([('n', j), ('tarea', t[0]), ('responsable', t[1]), ('plazo', t[2]), ('nota', t[3])]))
        fases[hoja] = OrderedDict([('titulo', titulo), ('fase_en_sugerida', FASE_EN.get(k, '')), ('tareas', lista)])
    return p, getattr(m, 'TITULO', ''), fases


def ranuras():
    out, fuentes = OrderedDict(), []
    for f in ('a', 'b'):
        p = os.path.join(CAF, 'textos', 'caf_es_%s.json' % f)
        if os.path.exists(p):
            fuentes.append(p)
            out.update(json.load(open(p, encoding='utf-8')))
    return fuentes, OrderedDict(sorted(out.items(), key=lambda kv: int(kv[0])))


def escalado():
    p, m = _modulo('datos_escalado.py')
    if m is None:
        return p, None
    out = OrderedDict()
    for k in dir(m):
        if k.isupper():
            v = getattr(m, k)
            try:
                json.dumps(v)
                out[k] = v
            except (TypeError, ValueError):
                out[k] = repr(v)[:2000]
    return p, out


def calculadora():
    cands = [os.path.join(DL, CALC)] + sorted(glob.glob(os.path.join(DL, '**', CALC), recursive=True))
    p = next((x for x in cands if os.path.exists(x)), None)
    if not p:
        return os.path.join(DL, CALC), None
    import openpyxl
    wb = openpyxl.load_workbook(p)
    hojas = OrderedDict()
    for ws in wb.worksheets:
        celdas = []
        for row in ws.iter_rows():
            for c in row:
                if c.value is None:
                    continue
                v = c.value if isinstance(c.value, (int, float, str)) else str(c.value)
                celdas.append([c.coordinate, v])
        hojas[ws.title] = OrderedDict([('dim', ws.dimensions), ('celdas', celdas)])
    return p, hojas


def main():
    fuentes, pendientes = [], []
    pc, titulo, fases = checklist()
    (fuentes.append(pc) if fases else pendientes.append('checklist ES (%s)' % os.path.relpath(pc, REPO)))
    pr, docx_es = ranuras()
    fuentes += pr
    if len(docx_es) < 61:
        pendientes.append('docx ES por ranura: %d/61 (textos/caf_es_{a,b}.json)' % len(docx_es))
    pctr = os.path.join(CAF, 'textos', 'contrato_es.json')
    contrato = json.load(open(pctr, encoding='utf-8')) if os.path.exists(pctr) else None
    (fuentes.append(pctr) if contrato else pendientes.append('contrato ES (textos/contrato_es.json)'))
    pe, esc = escalado()
    (fuentes.append(pe) if esc else pendientes.append('tabla de escalado ES (datos_escalado.py)'))
    pk, calc = calculadora()
    (fuentes.append(pk) if calc else pendientes.append('calculadora ES (%s)' % CALC))
    out = OrderedDict([
        ('meta', OrderedDict([
            ('generado', datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')),
            ('script', 'scripts/productos-digitales/business-plans-en-11/fuente_cof.py'),
            ('origen_es', CAF), ('dl_es', DL),
            ('uso', USO),
            ('fuentes', OrderedDict((x if not x.startswith(REPO) else os.path.relpath(x, REPO), sha(x)) for x in fuentes)),
            ('pendientes', pendientes),
        ])),
        ('checklist_es', OrderedDict([('titulo', titulo), ('fases', fases)]) if fases else None),
        ('docx_es_por_ranura', docx_es),
        ('contrato_es', contrato),
        ('escalado_es', esc),
        ('calculadora_es', calc),
    ])
    dest = os.path.join(AQUI, 'fuente_es_cof.json')
    with open(dest, 'w', encoding='utf-8') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    n = sum(len(f['tareas']) for f in fases.values()) if fases else 0
    print('fuente_es_cof.json: checklist %d tareas · docx %d/61 ranuras · contrato %s párrafos · escalado %s · '
          'calculadora %s · pendientes: %s' % (n, len(docx_es), len(contrato) if contrato else 0,
                                               'sí' if esc else 'no', 'sí' if calc else 'no', pendientes or 'ninguno'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
