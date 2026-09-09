#!/usr/bin/env python3
"""Gates del reparto de «puntos» por tramo (2026-09-10).

Contexto: `documentos.prompt_bloque()` entregaba a CADA uno de los 2-3 bloques de
un capítulo la lista COMPLETA de `cap['puntos']` mientras los `epigrafes` sí se
repartían, así que los redactores desarrollaban lo mismo (41 pares de frases con
Jaccard ≥ 0,55 en 15 de los 20 capítulos del Manual del Chef Ejecutivo).

Uso: /usr/local/bin/python3 scripts/productos-digitales/tests/test_reparto_puntos.py
Sin pytest a propósito (el pipeline de productos no lo tiene): exit 0 = todo verde,
exit 1 = algún gate rojo.

Gates:
  a  regresión byte a byte: un capítulo SIN «puntos» produce el MISMO prompt que
     antes del cambio (referencia `ref_prompts_pre_reparto.json`, generada con la
     copia intacta de documentos.py), salvo la sección nueva «LO QUE ESCRIBEN LOS
     OTROS TRAMOS», que se quita y se compara el resto carácter a carácter.
     DECISIÓN: esa sección aparece SIEMPRE que el capítulo tenga más de un bloque,
     tenga puntos o no. El reparto de puntos por sí solo no evita que dos
     redactores desarrollen el mismo material —los epígrafes de los otros tramos
     son la señal que lo evita—, y un capítulo sin puntos es justo el que más la
     necesita, porque no tiene ninguna otra frontera escrita.
  b  lista plana de 7 puntos y 3 bloques: repartos disjuntos, en orden, sin perder
     ni duplicar; cada prompt lleva sólo los suyos.
  c  `puntos_por_epigrafe`: cada bloque recibe los de sus epígrafes y ninguno de
     los otros; una clave que no es un epígrafe ABORTA con SystemExit.
  d  `puntos_globales` aparece en TODOS los bloques.
  e  `dump_prompts.py` y `documentos.py` emiten el MISMO prompt para el mismo
     bloque (capítulo 5 real del Manual del Chef Ejecutivo, comparado contra el
     .txt que vuelca el script de verdad, ejecutado en un directorio temporal).
  f  regresión sobre el corpus real: el `solape.py` nuevo da el mismo TOTAL que el
     original clavado en `manual-chef-ejecutivo/build/docs/`.

Los xlsx de `astro-site/public/dl/` sólo se leen (`data_only=True`, vía
documentos.py); este test no escribe NADA dentro del repo salvo su propio informe
en stdout.
"""
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

REPO = '/Users/johnguerrero/chefpro-modernize'
PD = os.path.join(REPO, 'scripts', 'productos-digitales')
AQUI = os.path.dirname(os.path.abspath(__file__))
MARCA_OTROS = 'LO QUE ESCRIBEN LOS OTROS TRAMOS DE ESTE CAPÍTULO'


def cargar(nombre, ruta):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


d = cargar('d', os.path.join(PD, 'guias-v2_0', 'documentos.py'))
FIXTURES = json.load(open(os.path.join(AQUI, 'fixtures_reparto.json'),
                          encoding='utf-8'))
GUIA = FIXTURES['guia']
CASOS = {c['nombre']: c for c in FIXTURES['casos']}

FALLOS = []


def check(gate, cond, detalle=''):
    estado = 'OK  ' if cond else 'FALLO'
    print(f'  [{estado}] {gate}' + (f' — {detalle}' if detalle else ''))
    if not cond:
        FALLOS.append(f'{gate}: {detalle}')
    return cond


def sin_seccion_otros(prompt):
    """Quita la sección «LO QUE ESCRIBEN LOS OTROS TRAMOS» entera.

    Es un elemento propio de `partes` y sus líneas nunca llevan una línea en
    blanco, así que acaba en el primer «\\n\\n» posterior a la marca."""
    i = prompt.find(MARCA_OTROS)
    if i < 0:
        return prompt, False
    fin = prompt.find('\n\n', i)
    fin = len(prompt) if fin < 0 else fin + 2
    return prompt[:i] + prompt[fin:], True


def prompts_del_caso(nombre):
    caso = CASOS[nombre]
    return caso, d.prompts_de_capitulo(caso['cap'], GUIA, caso['ctx_cifras'],
                                       caso['ctx_sector'])


# --------------------------------------------------------------------------
# a — regresión byte a byte contra el código anterior al reparto
# --------------------------------------------------------------------------
def gate_a():
    print('\nGATE a — regresión byte a byte (capítulos SIN puntos)')
    ref = json.load(open(os.path.join(AQUI, 'ref_prompts_pre_reparto.json'),
                         encoding='utf-8'))
    for nombre, esperado in ref.items():
        caso, nuevos = prompts_del_caso(nombre)
        if not check(f'{nombre}: mismo nº de bloques',
                     len(nuevos) == len(esperado['bloques']),
                     f'{len(nuevos)} vs {len(esperado["bloques"])}'):
            continue
        check(f'{nombre}: mismas palabras por bloque',
              all(b['palabras'] == esperado['palabras'] for b in nuevos),
              f'{[b["palabras"] for b in nuevos]} vs {esperado["palabras"]}')
        for i, (nuevo, viejo) in enumerate(zip(nuevos, esperado['bloques']), 1):
            limpio, tenia = sin_seccion_otros(nuevo['prompt'])
            check(f'{nombre} b{i}: idéntico al prompt viejo',
                  limpio == viejo,
                  'difiere' if limpio != viejo else
                  ('sección «otros tramos» retirada' if tenia else 'sin sección'))
            check(f'{nombre} b{i}: la sección «otros tramos» está presente',
                  tenia, 'el capítulo tiene más de un bloque')
            check(f'{nombre} b{i}: sin sección de PUNTOS OBLIGATORIOS',
                  'PUNTOS OBLIGATORIOS' not in nuevo['prompt'])


# --------------------------------------------------------------------------
# b — lista plana repartida posicionalmente
# --------------------------------------------------------------------------
def gate_b():
    print('\nGATE b — lista plana de 7 puntos entre 3 bloques')
    caso, bloques = prompts_del_caso('plana_7puntos_3bloques')
    planos = caso['cap']['puntos']
    repartos = [b['puntos'] for b in bloques]
    print(f'    reparto: {[len(r) for r in repartos]} de {len(planos)}')
    check('b: 3 bloques', len(bloques) == 3, str(len(bloques)))
    check('b: la concatenación es la lista original (ni pierde ni duplica)',
          [p for r in repartos for p in r] == planos)
    check('b: repartos disjuntos',
          len({id(p) for r in repartos for p in r}) == len(planos))
    check('b: ningún bloque vacío', all(repartos))
    for i, b in enumerate(bloques):
        mios = repartos[i]
        ajenos = [p for j, r in enumerate(repartos) if j != i for p in r]
        cuerpo = b['prompt'].split(MARCA_OTROS)[0]
        check(f'b{i + 1}: están sus {len(mios)} puntos',
              all(p in cuerpo for p in mios))
        check(f'b{i + 1}: ninguno de los {len(ajenos)} ajenos en su sección',
              not any(p in cuerpo for p in ajenos))
        etiquetas = re.findall(r'PUNTO-[A-G]', cuerpo)
        check(f'b{i + 1}: sólo sus etiquetas ({etiquetas})',
              etiquetas == [re.search(r'PUNTO-[A-G]', p).group(0) for p in mios])
        # y en la sección de «otros tramos» sí tienen que aparecer los ajenos
        otros = b['prompt'][b['prompt'].find(MARCA_OTROS):]
        check(f'b{i + 1}: los ajenos se anuncian en «otros tramos»',
              all(p in otros for p in ajenos))


# --------------------------------------------------------------------------
# c — puntos_por_epigrafe (y la clave inexistente que tiene que abortar)
# --------------------------------------------------------------------------
def gate_c():
    print('\nGATE c — puntos_por_epigrafe')
    caso, bloques = prompts_del_caso('por_epigrafe_2bloques')
    por_epi = caso['cap']['puntos_por_epigrafe']
    for i, b in enumerate(bloques):
        esperados = [p for e in b['epigrafes'] for p in por_epi.get(e, [])]
        ajenos = [p for e, ps in por_epi.items() if e not in b['epigrafes']
                  for p in ps]
        cuerpo = b['prompt'].split(MARCA_OTROS)[0]
        check(f'c b{i + 1}: lleva los puntos de sus epígrafes {esperados}',
              b['puntos'] == esperados and all(p in cuerpo for p in esperados))
        check(f'c b{i + 1}: no lleva ninguno de los otros ({len(ajenos)})',
              not any(p in cuerpo for p in ajenos))
    check('c: el epígrafe sin entrada no aporta puntos',
          sum(len(b['puntos']) for b in bloques) ==
          sum(len(v) for v in por_epi.values()))

    caso_malo = CASOS['clave_inexistente']
    try:
        d.prompts_de_capitulo(caso_malo['cap'], GUIA, '', '')
        check('c: una clave inexistente ABORTA', False, 'no abortó')
    except SystemExit as e:
        msg = str(e)
        check('c: una clave inexistente ABORTA', True, msg.split('):')[0][:60])
        check('c: el aborto NOMBRA la clave mal escrita',
              'Beta bien escritó' in msg)


# --------------------------------------------------------------------------
# d — puntos_globales en todos los bloques
# --------------------------------------------------------------------------
def gate_d():
    print('\nGATE d — puntos_globales')
    caso, bloques = prompts_del_caso('por_epigrafe_2bloques')
    globales = caso['cap']['puntos_globales']
    for i, b in enumerate(bloques):
        check(f'd b{i + 1}: sección de criterios de todo el capítulo',
              'CRITERIOS QUE APLICAN A TODO EL CAPÍTULO' in b['prompt'])
        check(f'd b{i + 1}: están los {len(globales)} criterios globales',
              all(g in b['prompt'] for g in globales))
        check(f'd b{i + 1}: los globales NO se cuentan como puntos del tramo',
              not any(g in b['puntos'] for g in globales))


# --------------------------------------------------------------------------
# e — dump_prompts.py == documentos.py sobre un capítulo real
# --------------------------------------------------------------------------
def gate_e():
    print('\nGATE e — dump_prompts.py vs documentos.py (cap. 5 real)')
    pid = 'manual-chef-ejecutivo'
    tmp = tempfile.mkdtemp(prefix='dumpprompts-')
    try:
        r = subprocess.run([sys.executable,
                            os.path.join(PD, 'guias-v2_0', 'dump_prompts.py'),
                            pid, tmp],
                           capture_output=True, text=True)
        if not check('e: dump_prompts.py termina bien', r.returncode == 0,
                     (r.stderr or r.stdout).strip().splitlines()[-1][:160]
                     if (r.stderr or r.stdout).strip() else ''):
            return
        print('    ' + r.stdout.strip().splitlines()[0])

        guion = d.cargar_guion(pid)
        guia = guion.GUIA
        xlsx_dir = os.path.join(d.DL, pid)
        idx = d.indexar_research(d.cargar_research())
        cap = next(c for c in guion.CAPITULOS if c['n'] == 5)
        cap['tablas_anunciadas'] = [t.get('titulo', '')
                                    for t in cap.get('tablas', [])]
        ctx = d.contexto_capitulo(cap, xlsx_dir, idx)
        mios = d.prompts_de_capitulo(cap, guia, ctx['ctx_cifras'],
                                     ctx['ctx_sector'])
        for i, b in enumerate(mios, 1):
            ruta = os.path.join(tmp, 'prompts', f'guia_cap05_b{i}.txt')
            if not check(f'e b{i}: dump_prompts volcó el bloque',
                         os.path.exists(ruta), ruta):
                continue
            volcado = open(ruta, encoding='utf-8').read()
            check(f'e b{i}: prompt idéntico ({len(volcado)} caracteres)',
                  volcado == b['prompt'])
        check('e: el cap. 5 reparte sus puntos entre los tramos',
              [len(b['puntos']) for b in mios] ==
              [len(x) for x in d.repartir_puntos(
                  cap, [b['epigrafes'] for b in mios])],
              f'{[len(b["puntos"]) for b in mios]} de '
              f'{len(cap.get("puntos") or [])}')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# --------------------------------------------------------------------------
# f — el solape.py nuevo da el mismo TOTAL que el original
# --------------------------------------------------------------------------
def gate_f():
    print('\nGATE f — solape.py generalizado vs el original (corpus real)')
    docs = os.path.join(PD, 'manual-chef-ejecutivo', 'build', 'docs')
    viejo = subprocess.run([sys.executable, os.path.join(docs, 'solape.py'),
                            '0.55'], capture_output=True, text=True, cwd=docs)
    nuevo = subprocess.run([sys.executable,
                            os.path.join(PD, 'guias-v2_0', 'solape.py'),
                            os.path.join(docs, 'txt'), '0.55'],
                           capture_output=True, text=True)

    def total(salida):
        m = re.search(r'TOTAL pares solapados:\s*(\d+)', salida)
        return int(m.group(1)) if m else None
    tv, tn = total(viejo.stdout), total(nuevo.stdout)
    print(f'    original: TOTAL {tv} · generalizado: TOTAL {tn}')
    check('f: mismo TOTAL en los dos medidores', tv is not None and tv == tn,
          f'{tv} vs {tn}')
    check('f: mismas líneas por capítulo',
          [l for l in viejo.stdout.splitlines() if l.startswith('cap ')] ==
          [l for l in nuevo.stdout.splitlines() if l.startswith('cap ')])
    check('f: exit 0 cuando no hay pares (sirve de gate)',
          (nuevo.returncode == 0) == (tn == 0),
          f'exit {nuevo.returncode} con TOTAL {tn}')


if __name__ == '__main__':
    for g in (gate_a, gate_b, gate_c, gate_d, gate_e, gate_f):
        g()
    print('\n' + '=' * 70)
    if FALLOS:
        print(f'ROJO — {len(FALLOS)} comprobaciones fallidas:')
        for f in FALLOS:
            print(' -', f)
        sys.exit(1)
    print('VERDE — todos los gates del reparto de puntos pasan.')
