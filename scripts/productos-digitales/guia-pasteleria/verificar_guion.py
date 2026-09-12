#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar_guion.py — gate del GUION de «Cómo Montar una Pastelería»
ANTES de escribir una sola palabra de prosa.

Clon parametrizado del gate del hermano (`manual-chef-ejecutivo/verificar_guion.py`),
con las rutas de este producto y con TRES comprobaciones nuevas que exige la
D36 de `guia-pasteleria-SPEC.md`:

  · títulos sin raya larga (la sanitización WinAnsi la convierte en «-» y el
    gate `tablas_ancladas` de `documentos.py` deja de encontrar el título);
  · `puntos_por_epigrafe` presente en TODOS los capítulos, con todas sus claves
    siendo epígrafes literales del capítulo, sin epígrafes huérfanos y con 2-5
    puntos cada uno (D33: es el primer guion de la familia que lo usa);
  · `puntos_globales` presente, con 2-3 criterios que van enteros a todos los
    tramos.

Lo que se comprueba (SPEC §4 y D36):

  1. El guion importa con `documentos.cargar_guion(PID)`.
  2. `resolver_cifras` sobre TODAS las cifras de la guía y de los dos bonus:
     cero referencias rotas (fichero, hoja o celda inexistentes) y cero valores
     vacíos (`None` → cadena vacía en el prompt = hueco silencioso).
  3. `construir_tabla` sobre TODAS las tablas: todas construyen y todas
     devuelven al menos una fila; ninguna imprime una fecha en crudo.
  4. Todo id de `sector` existe en `auditorias/guias-v2-research-sector.json`.
  5. Suma de `palabras` dentro del ±3 % de `palabras_objetivo` (guía y bonus).
  6. Epígrafes únicos dentro de cada capítulo, 4-6 en la guía, y
     `bloques` <= nº de epígrafes.
  7. Títulos sin cifra con separador de miles y sin raya larga; se informa
     además de los títulos con dígitos, que sí están permitidos.
  8. `puntos_por_epigrafe` y `puntos_globales`, según lo de arriba.
  9. Cero caracteres no latinos en el propio fichero del guion.
 10. Claves obligatorias de `gates` presentes, y `min_palabras_cap` alcanzable.
 11. Recuento total de referencias `C()`, de tablas y de bloques.

Uso:  /usr/local/bin/python3 scripts/productos-digitales/guia-pasteleria/verificar_guion.py
Requiere que los ocho xlsx estén copiados en astro-site/public/dl/<pid>/.
En el Mac hay que usar `/usr/local/bin/python3`: el del sistema no trae openpyxl.
Via: Claude Code
"""
import datetime as dt
import importlib.util
import json
import os
import re
import sys

REPO = '/Users/johnguerrero/chefpro-modernize'
PID = 'guia-pasteleria-obrador'
GUIAS = os.path.join(REPO, 'scripts', 'productos-digitales', 'guias-v2_0')
GUION_PY = os.path.join(GUIAS, f'guion_{PID.replace("-", "_")}.py')
RESEARCH = os.path.join(REPO, 'scripts', 'productos-digitales', 'auditorias',
                        'guias-v2-research-sector.json')

# Umbrales de la D36. Sólo se aplican al DOCUMENTO PRINCIPAL los de epígrafes y
# cifras: los bonus tienen su propio molde (5 epígrafes fijos en el de las 12
# decisiones, 4 secciones por capítulo en el business plan).
EPI_MIN, EPI_MAX = 4, 6
CIFRAS_MIN, CIFRAS_MAX = 4, 10
TABLAS_MIN, TABLAS_MAX = 1, 3
PUNTOS_POR_EPI_MIN, PUNTOS_POR_EPI_MAX = 2, 5
GLOBALES_MIN, GLOBALES_MAX = 2, 3

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
    falla(f'no existe {XLSX_DIR}: copia ahí los xlsx de guia-pasteleria/build/')
    print('\n'.join(fallos))
    sys.exit(1)

idx = d.indexar_research(json.load(open(RESEARCH, encoding='utf-8')))

RX_MILES = re.compile(r'\b\d{1,3}(?:\.\d{3})+(?:,\d+)?\b')
RX_DIGITO = re.compile(r'\d')
RX_FECHA_CRUDA = re.compile(r'\d{4}-\d{2}-\d{2}|\d{2}:\d{2}:\d{2}')
RAYA = '—'          # por escape: en un heredoc degeneraría en «-»

#: Formatos de `documentos.FORMATOS` que EXIGEN un número en la celda. `txt`
#: queda fuera a propósito: es el único que declara que va a imprimir texto.
FMT_NUMERICOS = tuple(k for k in d.FORMATOS if k != 'txt')

n_cifras = n_tablas = n_filas = n_puntos = 0


def revisa(caps, etiqueta, gates, principal=False):
    """Recorre una lista de capítulos y valida todo lo validable."""
    global n_cifras, n_tablas, n_filas, n_puntos
    suma = 0
    for cap in caps:
        cid = f'{etiqueta} cap {cap["n"]:02d} «{cap["titulo"][:48]}»'
        suma += cap['palabras']

        # --- epígrafes y troceo
        epis = cap['epigrafes']
        if len(epis) != len(set(epis)):
            falla(f'{cid}: epígrafes repetidos dentro del capítulo')
        if principal and not EPI_MIN <= len(epis) <= EPI_MAX:
            falla(f'{cid}: {len(epis)} epígrafes (se exigen '
                  f'{EPI_MIN}-{EPI_MAX})')
        if cap.get('bloques', 2) > len(epis):
            falla(f'{cid}: {cap["bloques"]} bloques para {len(epis)} epígrafes')
        bloques = d.trocear(epis, cap.get('bloques', 2))
        if len(bloques) != cap.get('bloques', 2):
            avisa(f'{cid}: trocear devuelve {len(bloques)} bloques, '
                  f'no {cap.get("bloques", 2)}')

        # --- puntos_por_epigrafe (D33) y puntos_globales
        ppe = cap.get('puntos_por_epigrafe')
        if not ppe:
            falla(f'{cid}: sin «puntos_por_epigrafe» (D33: es obligatorio en '
                  'los 20 capítulos, en el anexo y en los dos bonus)')
        else:
            conocidos = set(epis)
            huerfanas = [k for k in ppe if k not in conocidos]
            if huerfanas:
                falla(f'{cid}: «puntos_por_epigrafe» tiene {len(huerfanas)} '
                      'clave(s) que no son epígrafes de este capítulo (sus '
                      'puntos se perderían sin avisar): '
                      + '; '.join(f'«{k}»' for k in huerfanas))
            sin_puntos = [e for e in epis if not ppe.get(e)]
            if sin_puntos:
                falla(f'{cid}: {len(sin_puntos)} epígrafe(s) sin ningún punto: '
                      + '; '.join(f'«{e}»' for e in sin_puntos))
            for e in epis:
                ps = ppe.get(e) or []
                n_puntos += len(ps)
                if ps and not PUNTOS_POR_EPI_MIN <= len(ps) <= PUNTOS_POR_EPI_MAX:
                    falla(f'{cid}: el epígrafe «{e[:44]}» tiene {len(ps)} '
                          f'puntos (se exigen {PUNTOS_POR_EPI_MIN}-'
                          f'{PUNTOS_POR_EPI_MAX})')
            # y que el reparto real de documentos.py no aborte
            try:
                repartos = d.repartir_puntos(cap, bloques)
            except SystemExit as e:
                falla(f'{cid}: repartir_puntos aborta → {e}')
            else:
                vacios = [i for i, r in enumerate(repartos, 1) if not r]
                if vacios:
                    falla(f'{cid}: el/los bloque(s) {vacios} se quedan sin '
                          'ningún punto tras el reparto')

        globales = cap.get('puntos_globales') or []
        if not GLOBALES_MIN <= len(globales) <= GLOBALES_MAX:
            falla(f'{cid}: {len(globales)} «puntos_globales» (se exigen '
                  f'{GLOBALES_MIN}-{GLOBALES_MAX})')

        # --- título: sin separador de miles y sin raya larga
        if RX_MILES.search(cap['titulo']):
            falla(f'{cid}: el título lleva una cifra con separador de miles')
        if RAYA in cap['titulo']:
            falla(f'{cid}: el título lleva raya larga (la sanitización WinAnsi '
                  'la convierte en guion y el gate de tablas ancladas deja de '
                  'encontrar el título)')
        if RX_DIGITO.search(cap['titulo']):
            avisa(f'{cid}: el título lleva dígitos (permitido, pero revísalo)')

        # --- cifras
        cifras = cap.get('cifras', [])
        if principal and not CIFRAS_MIN <= len(cifras) <= CIFRAS_MAX:
            falla(f'{cid}: {len(cifras)} cifras (se exigen '
                  f'{CIFRAS_MIN}-{CIFRAS_MAX})')
        if not cifras:
            falla(f'{cid}: sin ninguna cifra del producto')
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
            if isinstance(v, (dt.datetime, dt.date)):
                falla(f'{cid}: {ref} devuelve una FECHA y `formatear` no tiene '
                      f'formato de fecha: se imprimiría «{v}»')
                continue
            # A2 (2026-09-10): un formato NUMÉRICO sobre una celda de TEXTO
            # no rompía nada -`formatear` cae en `str(v)`- y el redactor
            # recibía «Plazo crítico de entrega, en semanas: En línea con el
            # CAPEX del libro 2». De ahí salió la única cifra inventada del
            # pack («veinte semanas»). El tipo se comprueba ahora.
            if fmt in FMT_NUMERICOS and not isinstance(v, (int, float)):
                falla(f'{cid}: TIPO INCOMPATIBLE en {ref} («{etq}»): el '
                      f'formato «{fmt}» es numérico y la celda devuelve '
                      f'{type(v).__name__} → se imprimiría «{v}»')
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
        if not TABLAS_MIN <= len(tabs) <= TABLAS_MAX:
            falla(f'{cid}: {len(tabs)} tablas (se exigen '
                  f'{TABLAS_MIN}-{TABLAS_MAX})')
        for t in tabs:
            n_tablas += 1
            tit = t.get('titulo', '')
            try:
                md, nf = d.construir_tabla(XLSX_DIR, t)
            except Exception as e:
                falla(f'{cid}: TABLA ROTA «{tit[:40]}» → '
                      f'{type(e).__name__}: {e}')
                continue
            n_filas += nf
            if RX_FECHA_CRUDA.search(md):
                falla(f'{cid}: la tabla «{tit[:40]}» imprime una fecha en crudo')
            if nf < 1:
                falla(f'{cid}: tabla «{tit[:40]}» con 0 filas')
            if RAYA in tit:
                falla(f'{cid}: el título de la tabla «{tit[:40]}» lleva raya larga')
            if not tit:
                falla(f'{cid}: tabla sin título')

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


print('\n--- validando la guía ---')
revisa(CAPITULOS, 'GUIA', GUIA['gates'], principal=True)
for b in BONUS:
    print(f'--- validando {b["nombre"]} ---')
    revisa(b['capitulos'], 'BONUS', b['gates'])

# ------------------------------------------------- 9. no latinos en el guion
crudo = open(GUION_PY, encoding='utf-8').read()
nl = d.guard_no_latinos(crudo, 'guion')
if nl:
    falla(f'{len(nl)} caracteres no latinos en el propio guion')

# ------------------------------------------------- 10. gates declarados
g = GUIA['gates']
for k in ('paginas_prometidas', 'palabras_objetivo', 'min_palabras_cap',
          'cifras_extra', 'cifras_ignorar', 'erratas_permitidas',
          'mortalidad_permitida'):
    if k not in g:
        falla(f'GUIA.gates: falta la clave «{k}»')
for b in BONUS:
    for k in ('paginas_prometidas', 'palabras_objetivo', 'min_palabras_cap',
              'meta', 'erratas_permitidas'):
        if k not in b['gates']:
            falla(f'{b["nombre"]}.gates: falta la clave «{k}»')
    if not b['gates'].get('erratas_permitidas'):
        falla(f'{b["nombre"]}: «erratas_permitidas» vacío — hay que asignar '
              '_ERRATAS_OK también a cada bonus, o se queda sin ella')
if not g.get('erratas_permitidas'):
    falla('GUIA.gates: «erratas_permitidas» vacío')

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
        falla(f'{b["nombre"]}: bloques por debajo de {mb} palabras: {c2}')

# los ocho libros del pack tienen que estar todos en dl/
libros = sorted(f for f in os.listdir(XLSX_DIR) if f.endswith('.xlsx'))
print(f'\nlibros en {XLSX_DIR}: {len(libros)}')
if len(libros) != 8:
    falla(f'se esperaban 8 libros en dl/ y hay {len(libros)}: {libros}')

# ------------------------------------------------------------------ informe
bloques_guia = sum(len(d.trocear(c['epigrafes'], c.get('bloques', 2)))
                   for c in CAPITULOS)
bloques_bonus = sum(len(d.trocear(c['epigrafes'], c.get('bloques', 2)))
                    for b in BONUS for c in b['capitulos'])
print(f'referencias C() totales: {n_cifras}')
print(f'tablas totales: {n_tablas} · filas construidas: {n_filas}')
print(f'puntos repartidos por epígrafe: {n_puntos}')
ids = sorted({s for c in CAPITULOS for s in c.get('sector', [])}
             | {s for b in BONUS for c in b['capitulos']
                for s in c.get('sector', [])})
print(f'ids de sector distintos usados: {len(ids)} '
      f'(PA {len([i for i in ids if i.startswith("PA-")])} · '
      f'PS {len([i for i in ids if i.startswith("PS-")])})')
print(f'bloques que producirá el pipeline: {bloques_guia} (guía) + '
      f'{bloques_bonus} (bonus) = {bloques_guia + bloques_bonus}')

if avisos:
    print(f'\nAVISOS ({len(avisos)}):')
    for a in avisos:
        print('  ·', a)

if fallos:
    print(f'\nFALLOS ({len(fallos)}):')
    for f in fallos:
        print('  ✗', f)
    sys.exit(1)

print('\nOK: 0 referencias rotas, 0 celdas vacías, 0 tablas rotas, '
      '0 ids de sector inexistentes, 0 caracteres no latinos.')
