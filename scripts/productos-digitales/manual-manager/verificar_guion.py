#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar_guion.py — gate del GUION del «Manual del Manager de Restaurante»
ANTES de escribir una sola palabra de prosa.

Lo que se comprueba (SPEC §4 y §6, y el encargo de esta sesión):

  1. El guion importa con `documentos.cargar_guion(PID)`.
  2. `resolver_cifras` sobre TODAS las cifras del manual y del bonus:
     cero referencias rotas (celda inexistente, hoja inexistente) y cero
     valores vacíos (`None` → cadena vacía en el prompt = hueco silencioso).
  3. `construir_tabla` sobre TODAS las tablas: todas construyen y todas
     devuelven al menos una fila.
  4. Todo id de `sector` existe en `auditorias/guias-v2-research-sector.json`.
  5. Suma de `palabras` ≈ `palabras_objetivo` (manual y bonus).
  6. Epígrafes únicos dentro de cada capítulo, y `bloques` <= nº de epígrafes.
  7. Títulos sin cifra con separador de miles (la que dispara el gate de
     coherencia de `documentos.py`); se informa además de los títulos con
     dígitos, que sí están permitidos.
  8. Cero caracteres no latinos en el propio fichero del guion.
  9. Recuento total de referencias `C()` y de tablas.

Uso:  python3 verificar_guion.py
Requiere que los xlsx estén copiados en astro-site/public/dl/<pid>/.
Via: Claude Code
"""
import datetime as dt
import importlib.util
import json
import os
import re
import sys

REPO = '/Users/johnguerrero/chefpro-modernize'
PID = 'manual-manager-restaurante'
GUIAS = os.path.join(REPO, 'scripts', 'productos-digitales', 'guias-v2_0')
GUION_PY = os.path.join(GUIAS, f'guion_{PID.replace("-", "_")}.py')
RESEARCH = os.path.join(REPO, 'scripts', 'productos-digitales', 'auditorias',
                        'guias-v2-research-sector.json')

sp = importlib.util.spec_from_file_location('d', os.path.join(GUIAS, 'documentos.py'))
d = importlib.util.module_from_spec(sp)
sp.loader.exec_module(d)

XLSX_DIR = os.path.join(d.DL, PID)
fallos, avisos = [], []


def falla(msg):
    fallos.append(msg)


def avisa(msg):
    avisos.append(msg)


# ---------------------------------------------------------------- 1. importa
guion = d.cargar_guion(PID)
GUIA, CAPITULOS, BONUS = guion.GUIA, guion.CAPITULOS, guion.BONUS
print(f'guion cargado: {GUIA["titulo"]} · {len(CAPITULOS)} capítulos · '
      f'{len(BONUS)} documento(s) de bonus')

if not os.path.isdir(XLSX_DIR):
    falla(f'no existe {XLSX_DIR}: copia los xlsx de manual-manager/build/ ahí')
    print('\n'.join(fallos))
    sys.exit(1)

idx = d.indexar_research(json.load(open(RESEARCH, encoding='utf-8')))

RX_MILES = re.compile(r'\b\d{1,3}(?:\.\d{3})+(?:,\d+)?\b')
RX_DIGITO = re.compile(r'\d')
RX_FECHA_CRUDA = re.compile(r'\d{4}-\d{2}-\d{2}|\d{2}:\d{2}:\d{2}')

n_cifras = n_tablas = n_filas = 0


def revisa(caps, etiqueta, gates):
    """Recorre una lista de capítulos y valida todo lo validable."""
    global n_cifras, n_tablas, n_filas
    suma = 0
    for cap in caps:
        cid = f'{etiqueta} cap {cap["n"]:02d} «{cap["titulo"][:48]}»'
        suma += cap['palabras']

        # --- epígrafes y troceo
        epis = cap['epigrafes']
        if len(epis) != len(set(epis)):
            falla(f'{cid}: epígrafes repetidos dentro del capítulo')
        if not 4 <= len(epis) <= 6 and etiqueta == 'MANUAL':
            falla(f'{cid}: {len(epis)} epígrafes (se exigen 4-6)')
        if cap.get('bloques', 2) > len(epis):
            falla(f'{cid}: {cap["bloques"]} bloques para {len(epis)} epígrafes')
        bloques = d.trocear(epis, cap.get('bloques', 2))
        if len(bloques) != cap.get('bloques', 2):
            avisa(f'{cid}: trocear devuelve {len(bloques)} bloques, '
                  f'no {cap.get("bloques", 2)}')

        # --- título sin cifra con separador de miles
        if RX_MILES.search(cap['titulo']):
            falla(f'{cid}: el título lleva una cifra con separador de miles')
        if RX_DIGITO.search(cap['titulo']):
            avisa(f'{cid}: el título lleva dígitos (permitido, pero revísalo)')

        # --- cifras
        cifras = cap.get('cifras', [])
        if etiqueta == 'MANUAL' and not 4 <= len(cifras) <= 10:
            falla(f'{cid}: {len(cifras)} cifras (se exigen 4-10)')
        for etq, ref, fmt in cifras:
            n_cifras += 1
            if fmt not in d.FORMATOS:
                falla(f'{cid}: formato desconocido «{fmt}» en «{etq}»')
            try:
                v = d.celda(XLSX_DIR, ref)
            except Exception as e:                       # hoja/celda/fichero
                falla(f'{cid}: REFERENCIA ROTA {ref} → {type(e).__name__}: {e}')
                continue
            if v is None:
                falla(f'{cid}: CELDA VACÍA {ref} («{etq}»)')
                continue
            if isinstance(v, dt.datetime) or isinstance(v, dt.date):
                falla(f'{cid}: {ref} devuelve una FECHA y `formatear` no tiene '
                      f'formato de fecha: se imprimiría «{v}»')
                continue
            txt = d.formatear(v, fmt)
            if not str(txt).strip():
                falla(f'{cid}: valor formateado VACÍO en {ref} («{etq}»)')
            if RX_FECHA_CRUDA.search(str(txt)):
                falla(f'{cid}: {ref} imprime una fecha en crudo: «{txt}»')

        # --- sector
        for sid in cap.get('sector', []):
            if sid not in idx:
                falla(f'{cid}: id de sector inexistente «{sid}»')

        # --- tablas
        tabs = cap.get('tablas', [])
        if not 1 <= len(tabs) <= 3:
            falla(f'{cid}: {len(tabs)} tablas (se exigen 1-3)')
        for t in tabs:
            n_tablas += 1
            try:
                md, nf = d.construir_tabla(XLSX_DIR, t)
            except Exception as e:
                falla(f'{cid}: TABLA ROTA «{t.get("titulo", "")[:40]}» → '
                      f'{type(e).__name__}: {e}')
                continue
            n_filas += nf
            if RX_FECHA_CRUDA.search(md):
                falla(f'{cid}: la tabla «' + t.get('titulo','')[:40] + '» imprime una fecha en crudo')
            if nf < 1:
                falla(f'{cid}: tabla «{t.get("titulo", "")[:40]}» con 0 filas')
            if 'src' in t and not t.get('nota') and 'legal' in str(t.get('src')):
                avisa(f'{cid}: tabla legal sin nota de verificación')

        # --- prohibiciones
        if not cap.get('prohibido'):
            falla(f'{cid}: sin lista de prohibiciones')

    obj = gates['palabras_objetivo']
    dif = abs(suma - obj) / obj
    print(f'  {etiqueta}: {len(caps)} capítulos · {suma} palabras declaradas '
          f'(objetivo {obj}, desvío {dif * 100:.1f} %)')
    if dif > 0.03:
        falla(f'{etiqueta}: la suma de palabras ({suma}) se desvía más del 3 % '
              f'del objetivo ({obj})')
    return suma


print('\n--- validando el manual ---')
revisa(CAPITULOS, 'MANUAL', GUIA['gates'])
for b in BONUS:
    print(f'--- validando {b["nombre"]} ---')
    revisa(b['capitulos'], 'BONUS', b['gates'])

# ------------------------------------------------- 8. no latinos en el guion
crudo = open(GUION_PY, encoding='utf-8').read()
nl = d.guard_no_latinos(crudo, 'guion')
if nl:
    falla(f'{len(nl)} caracteres no latinos en el propio guion')

# ------------------------------------------------- gates declarados
g = GUIA['gates']
for k in ('paginas_prometidas', 'palabras_objetivo', 'min_palabras_cap',
          'cifras_extra', 'cifras_ignorar', 'erratas_permitidas',
          'mortalidad_permitida'):
    if k not in g:
        falla(f'GUIA.gates: falta la clave «{k}»')
for b in BONUS:
    for k in ('paginas_prometidas', 'palabras_objetivo', 'min_palabras_cap', 'meta'):
        if k not in b['gates']:
            falla(f'{b["nombre"]}.gates: falta la clave «{k}»')

# el mínimo por capítulo tiene que ser alcanzable con lo declarado
minimo = g['min_palabras_cap']
cortos = [c['n'] for c in CAPITULOS if c['palabras'] < minimo]
if cortos:
    falla(f'capítulos con menos palabras declaradas que min_palabras_cap '
          f'({minimo}): {cortos}')
for b in BONUS:
    mb = b['gates']['min_palabras_cap']
    c2 = [c['n'] for c in b['capitulos'] if c['palabras'] < mb]
    if c2:
        falla(f'{b["nombre"]}: situaciones por debajo de {mb} palabras: {c2}')

# ------------------------------------------------------------------ informe
print(f'\nreferencias C() totales: {n_cifras}')
print(f'tablas totales: {n_tablas} · filas construidas: {n_filas}')
print(f'bloques que producirá el pipeline: '
      f'{sum(len(d.trocear(c["epigrafes"], c.get("bloques", 2))) for c in CAPITULOS)} '
      f'(manual) + '
      f'{sum(len(d.trocear(c["epigrafes"], c.get("bloques", 2))) for b in BONUS for c in b["capitulos"])} '
      f'(bonus)')

if avisos:
    print(f'\nAVISOS ({len(avisos)}):')
    for a in avisos:
        print('  ·', a)

if fallos:
    print(f'\nFALLOS ({len(fallos)}):')
    for f in fallos:
        print('  ✗', f)
    sys.exit(1)

print('\nOK: 0 referencias rotas, 0 tablas rotas, 0 ids de sector inexistentes.')
