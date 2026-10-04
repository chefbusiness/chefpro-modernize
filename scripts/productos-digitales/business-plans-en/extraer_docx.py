#!/usr/bin/env python3
"""
extraer_docx.py — Food Truck + Coffee Shop Business Plan Kit (EN) · censo y textos ES de los 2 docx (SPEC D22-D23).

Lee los docx PUBLICADOS (SOLO LECTURA) y escribe, junto a este script (o en --salida), `docx_es_ft.json` y
`docx_es_caf.json`:

  {"meta": {...recuentos, estilos, runs, página, tandas, tokens...},
   "parrafos": {"<índice>": {"estilo", "texto", "n_runs", "fmt", "rol", "seccion", "traducir", "tanda", "nota"?}}}

rol: vacio · separador (━━━) · encabezado (Heading 1, D22) · indice · fijo (lo escribe ensamblar_docx.py desde
mapas.DOCX_FIJOS: portada, aviso, cierre — D23) · cuerpo (lo traducen los subagentes) · subtitulo (cuerpo de una
línea sin punto final). Solo `traducir: true` va a los subagentes, en la tanda que diga `tanda` (mapas.DOCX_TANDAS).

Comprueba (sale ≠ 0 si falla): nº de párrafos = SPEC (131 / 167); TODO párrafo con texto tiene UN run (si alguno
tuviera varios, lo lista en meta.multi_run con sus formatos: el ensamblador solo los acepta si todos los runs
comparten formato); encabezados D22 en mapas.DOCX_ENCABEZADOS con estilo Heading 1; índice; cada fijo de mapas tiene
texto en el ES; los índices de DOCX_MOVER / DOCX_RPR_DE / DOCX_NOTAS existen; página US Letter.

    python3 extraer_docx.py [--origen-repo DIR] [--salida DIR]
"""
import argparse
import datetime
import hashlib
import json
import os
import sys
from collections import OrderedDict, Counter

import docx

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
sys.path.insert(0, AQUI)
import mapas                                                     # noqa: E402

N_PARRAFOS_SPEC = {'ft': 131, 'caf': 167}
LETTER = (7772400, 10058400)


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        h.update(fh.read())
    return h.hexdigest()


def fmt_run(r):
    col = r.font.color.rgb if r.font.color is not None and r.font.color.type is not None else None
    return OrderedDict([('bold', r.bold), ('italic', r.italic),
                        ('size_pt', r.font.size.pt if r.font.size is not None else None),
                        ('font', r.font.name), ('color', str(col) if col is not None else None)])


def rpr_xml(r):
    rp = r._r.rPr
    return rp.xml if rp is not None else ''


def extraer(plan, repo):
    f_es, f_en, tit = mapas.DOCX[plan]
    path = os.path.join(repo, mapas.PLANES[plan]['dir_es'], f_es)
    d = docx.Document(path)
    errores = []
    pars = d.paragraphs
    fijos = mapas.textos_fijos_docx(plan)
    enc = mapas.DOCX_ENCABEZADOS[plan]
    ind = mapas.DOCX_INDICE[plan]
    notas = mapas.DOCX_NOTAS.get(plan, {})
    tanda_de_sec = {}
    for tid, (pl, secs) in mapas.DOCX_TANDAS.items():
        if pl == plan:
            for s in secs:
                tanda_de_sec[s] = tid
    out = OrderedDict()
    multi = []
    seccion = 0
    ultimo_enc = enc[-1]
    for i, p in enumerate(pars):
        txt = p.text
        runs = p.runs
        if i in enc:
            seccion = enc.index(i) + 1
        e = OrderedDict()
        e['estilo'] = p.style.name
        e['texto'] = txt
        e['n_runs'] = len(runs)
        if runs:
            e['fmt'] = fmt_run(runs[0])
        con_texto = [r for r in runs if r.text]
        if len(runs) > 1 and txt.strip():
            rprs = {rpr_xml(r) for r in runs}
            multi.append(OrderedDict([('parrafo', i), ('runs', len(runs)), ('formatos_distintos', len(rprs)),
                                      ('textos', [r.text for r in runs])]))
        # rol
        if i in fijos:
            rol = 'encabezado' if i in enc else ('indice' if i in ind else 'fijo')
        elif not txt.strip():
            rol = 'vacio'
        elif set(txt.strip()) <= set('━'):
            rol = 'separador'
        elif seccion == 0:
            rol = 'sin-asignar'
        else:
            una_linea = '\n' not in txt and len(txt) < 80 and not txt.rstrip().endswith('.')
            rol = 'subtitulo' if una_linea else 'cuerpo'
        if i in mapas.DOCX_RPR_DE.get(plan, {}):
            rol = 'cuerpo'                                         # CAF 134: el resumen nuevo de §8
        e['rol'] = rol
        e['seccion'] = seccion
        if rol == 'fijo' and i > ultimo_enc:
            e['seccion'] = 11                                       # cierre
        e['traducir'] = rol in ('cuerpo', 'subtitulo')
        if e['traducir']:
            e['tanda'] = tanda_de_sec[seccion]
            e['palabras'] = len(txt.split())
        if i in fijos:
            e['en_fijo'] = fijos[i]
        if i in notas:
            e['nota'] = notas[i]
        if rol == 'sin-asignar':
            errores.append('%s[%d]: párrafo con texto fuera de las secciones y sin fijo: %r' % (plan, i, txt[:60]))
        if rol == 'encabezado' and p.style.name != 'Heading 1':
            errores.append('%s[%d]: el encabezado no es Heading 1' % (plan, i))
        if i in fijos and not txt.strip():
            errores.append('%s[%d]: fijo sobre un párrafo vacío en el ES' % (plan, i))
        if con_texto and not runs:
            errores.append('%s[%d]: texto sin runs' % (plan, i))
        out[str(i)] = e
    # CAF 134: el placeholder pasa a cuerpo traducible (va a §8 tras el movimiento)
    for i in notas:
        if str(i) not in out:
            errores.append('%s: DOCX_NOTAS cita el párrafo %d, que no existe' % (plan, i))
    mov = mapas.DOCX_MOVER.get(plan)
    if mov:
        for i in [mov['despues_de']] + mov['orden']:
            if str(i) not in out:
                errores.append('%s: DOCX_MOVER cita el párrafo %d, que no existe' % (plan, i))
        for i in mov['orden']:
            if out[str(i)]['estilo'] != 'Normal':
                errores.append('%s: DOCX_MOVER mueve un párrafo que no es Normal (%d)' % (plan, i))
    for i, j in mapas.DOCX_RPR_DE.get(plan, {}).items():
        if out[str(i)]['n_runs'] != 1 or out[str(j)]['n_runs'] != 1:
            errores.append('%s: DOCX_RPR_DE %d ← %d sin run único' % (plan, i, j))
    if len(pars) != N_PARRAFOS_SPEC[plan]:
        errores.append('%s: %d párrafos (SPEC D22: %d)' % (plan, len(pars), N_PARRAFOS_SPEC[plan]))
    if [i for i, p in enumerate(pars) if p.style.name == 'Heading 1'] != enc:
        errores.append('%s: los Heading 1 del ES no son mapas.DOCX_ENCABEZADOS' % plan)
    s = d.sections[0]
    pagina = (s.page_width, s.page_height)
    if pagina != LETTER:
        errores.append('%s: la página no es US Letter (%s)' % (plan, pagina))
    trad = [k for k, e in out.items() if e['traducir']]
    meta = OrderedDict([
        ('generado', datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()),
        ('script', 'scripts/productos-digitales/business-plans-en/extraer_docx.py'),
        ('plan', plan), ('fichero_es', os.path.join(mapas.PLANES[plan]['dir_es'], f_es)), ('sha256', sha256(path)),
        ('fichero_en', os.path.join(mapas.PLANES[plan]['dir_en'], f_en)), ('titulo_en', tit),
        ('n_parrafos', len(pars)), ('n_con_texto', sum(1 for p in pars if p.text.strip())),
        ('n_sin_runs', sum(1 for p in pars if not p.runs)),
        ('n_un_run', sum(1 for p in pars if len(p.runs) == 1)),
        ('multi_run', multi),
        ('estilos', OrderedDict(Counter(p.style.name for p in pars).most_common())),
        ('roles', OrderedDict(Counter(e['rol'] for e in out.values()).most_common())),
        ('n_traducir', len(trad)),
        ('palabras_traducir', sum(out[k]['palabras'] for k in trad)),
        ('tandas', OrderedDict((t, OrderedDict([('parrafos', [int(k) for k in trad if out[k]['tanda'] == t]),
                                                ('palabras', sum(out[k]['palabras'] for k in trad
                                                                 if out[k]['tanda'] == t))]))
                               for t in mapas.DOCX_TANDAS if mapas.DOCX_TANDAS[t][0] == plan)),
        ('pagina_emu', list(pagina)),
        ('mover', mov), ('rpr_de', mapas.DOCX_RPR_DE.get(plan)),
        ('tokens', OrderedDict((t, desc) for t, (fmt, src, desc) in mapas.tokens_de(plan).items())),
        ('regla', 'Un run por párrafo: ensamblar_docx.py sustituye el texto del run y conserva su formato (rPr) y el '
                  'del párrafo (pPr). Los traductores escriben SOLO los párrafos con traducir=true de su tanda.'),
    ])
    return OrderedDict([('meta', meta), ('parrafos', out)]), errores


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('--origen-repo', default=REPO)
    ap.add_argument('--salida', default=AQUI)
    args = ap.parse_args()
    todos = []
    for plan in mapas.PLANES:
        obj, err = extraer(plan, args.origen_repo)
        todos += err
        with open(os.path.join(args.salida, 'docx_es_%s.json' % plan), 'w', encoding='utf-8') as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
        m = obj['meta']
        print('docx_es_%s.json: %d párrafos (%d con texto, %d de un run, %d sin runs, %d multi-run) · estilos %s · '
              'roles %s · traducir %d párrafos / %d palabras · tandas %s' % (
                  plan, m['n_parrafos'], m['n_con_texto'], m['n_un_run'], m['n_sin_runs'], len(m['multi_run']),
                  dict(m['estilos']), dict(m['roles']), m['n_traducir'], m['palabras_traducir'],
                  {k: (len(v['parrafos']), v['palabras']) for k, v in m['tandas'].items()}))
    for e in todos:
        print('ERROR', e)
    print('extraer_docx: %s' % ('VERDE' if not todos else 'ROJO (%d)' % len(todos)))
    return 1 if todos else 0


if __name__ == '__main__':
    sys.exit(main())
