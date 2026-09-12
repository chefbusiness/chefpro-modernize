#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar_guion.py — gate del GUION de «Cómo Montar una Chocolatería»
ANTES de escribir una sola palabra de prosa.

Clon parametrizado del gate de la hermana (`guia-pasteleria/verificar_guion.py`,
10-09-2026) con las rutas de este producto, los NUEVE libros de este pack y DOS
comprobaciones nuevas que exige la D44 de `guia-chocolateria-SPEC.md`:

  (a) **Ningún id «bare» de las once familias de D44** —`CHS-24`, `CHS-25`,
      `CHS-27`, `CHS-28`, `CHS-37`, `CHS-38`, `CHS-42`, `CHS-45`, `CHS-46`,
      `CHS-47` y `CHS-69`— ni **`CHS-41`**. Los once primeros NO existen en el
      JSON (sólo existen con sufijo: `CHS-28a`, `CHS-41h`…), así que la
      comprobación 4 ya los cazaría; `CHS-41` es la trampa de verdad, porque
      SÍ existe sin sufijo y es un **agregado sin fuente única** de fiabilidad
      baja (§5.2 de la SPEC): el gate de existencia lo dejaría pasar. Se mira
      tanto en `sector` como en el TEXTO de los puntos y de las prohibiciones,
      que es lo que acaba dentro del prompt del redactor.
  (b) **Ningún id de `fiabilidad: "baja"` citado como cifra** en
      `puntos_por_epigrafe`. Un id de fiabilidad baja es un HUECO DELIBERADO
      (`_meta.como_leer_la_fiabilidad` del propio JSON: «No hay fuente
      utilizable. Estos items NO deben rellenarse ni convertirse en texto de
      la guia»). Si el id baja TIENE `cifra`, es FALLO; si no la tiene, AVISO
      —se puede citar el hecho cualitativo, nunca un número.

Lo que se comprueba (SPEC §4, D45c y D44):

  1. El guion importa con `documentos.cargar_guion(PID)`.
  2. `celda()` sobre TODAS las cifras de la guía y de los dos bonus: cero
     referencias rotas (fichero, hoja o celda inexistentes), cero valores
     vacíos, cero fechas en crudo y cero tipos incompatibles (formato numérico
     sobre celda de texto: A2 del 10-09-2026).
  3. `construir_tabla` sobre TODAS las tablas: todas construyen, todas
     devuelven al menos una fila y ninguna imprime una fecha en crudo.
  4. Todo id de `sector` existe en `auditorias/guias-v2-research-sector.json`
     (635 entradas tras la fusión del 12-09-2026: 115 `CHS-*` + 109 `CHN-*`).
  5. Suma de `palabras` dentro del ±3 % de `palabras_objetivo` (guía y bonus).
  6. Epígrafes únicos dentro de cada capítulo, 4-6 en la guía, y
     `bloques` <= nº de epígrafes.
  7. Títulos sin cifra con separador de miles y sin raya larga.
  8. `puntos_por_epigrafe` (dict epígrafe literal → lista de 2-5 puntos, sin
     claves huérfanas, sin epígrafes sin puntos y sin bloques vacíos tras el
     reparto real de `documentos.repartir_puntos`) y `puntos_globales` (2-3).
  9. Cero caracteres no latinos en el propio fichero del guion.
 10. Claves obligatorias de `gates` presentes, `min_palabras_cap` alcanzable y
     `erratas_permitidas` asignada a GUIA **y a cada bonus**.
 11. Los NUEVE libros del pack están en `astro-site/public/dl/<pid>/`.
 12. Las dos comprobaciones nuevas (a) y (b) de arriba.
 13. Recuento total de referencias `C()`, tablas, filas, puntos y bloques.

Uso:  /usr/local/bin/python3 scripts/productos-digitales/guia-chocolateria/verificar_guion.py
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
PID = 'guia-chocolateria-obrador'
GUIAS = os.path.join(REPO, 'scripts', 'productos-digitales', 'guias-v2_0')
GUION_PY = os.path.join(GUIAS, f'guion_{PID.replace("-", "_")}.py')
RESEARCH = os.path.join(REPO, 'scripts', 'productos-digitales', 'auditorias',
                        'guias-v2-research-sector.json')
N_LIBROS = 9

# Umbrales de la D45c. Sólo se aplican al DOCUMENTO PRINCIPAL los de epígrafes
# y cifras: los bonus tienen su propio molde (5 epígrafes fijos en el de las 12
# decisiones, 4 por sección en el business plan).
EPI_MIN, EPI_MAX = 4, 6
CIFRAS_MIN, CIFRAS_MAX = 4, 10
TABLAS_MIN, TABLAS_MAX = 1, 3
PUNTOS_POR_EPI_MIN, PUNTOS_POR_EPI_MAX = 2, 5
GLOBALES_MIN, GLOBALES_MAX = 2, 3

#: D44 · §5.2. Las once familias que la síntesis cita «bare» y que en el JSON
#: SÓLO existen con sufijo, más `CHS-41`, que existe sin sufijo pero es un
#: agregado de fiabilidad baja y está PROHIBIDO citarlo (las atemperadoras se
#: citan `CHS-41a`…`CHS-41j`, una a una).
IDS_BARE_PROHIBIDOS = ('CHS-24', 'CHS-25', 'CHS-27', 'CHS-28', 'CHS-37',
                       'CHS-38', 'CHS-41', 'CHS-42', 'CHS-45', 'CHS-46',
                       'CHS-47', 'CHS-69')
#: Un id sólo es «bare» si detrás no viene ni una letra de sufijo ni otro
#: dígito: `CHS-28a` y `CHS-280` no son `CHS-28`.
RX_BARE = {i: re.compile(r'\b' + re.escape(i) + r'(?![0-9A-Za-z-])')
           for i in IDS_BARE_PROHIBIDOS}
#: Cualquier id del research citado dentro del texto de un punto.
RX_ID = re.compile(r'\b(?:CHN|CHS|PA|PS)-[0-9]+[a-z]*(?:-int)?\b')

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
    falla(f'no existe {XLSX_DIR}: copia ahí los xlsx de guia-chocolateria/build/')
    print('\n'.join(fallos))
    sys.exit(1)

RES = json.load(open(RESEARCH, encoding='utf-8'))
idx = d.indexar_research(RES)

RX_MILES = re.compile(r'\b\d{1,3}(?:\.\d{3})+(?:,\d+)?\b')
RX_DIGITO = re.compile(r'\d')
RX_FECHA_CRUDA = re.compile(r'\d{4}-\d{2}-\d{2}|\d{2}:\d{2}:\d{2}')
RAYA = '—'     # por escape: en un heredoc degeneraría en «-»

#: Formatos de `documentos.FORMATOS` que EXIGEN un número en la celda. `txt`
#: queda fuera a propósito: es el único que declara que va a imprimir texto.
FMT_NUMERICOS = tuple(k for k in d.FORMATOS if k != 'txt')

n_cifras = n_tablas = n_filas = n_puntos = 0


def revisa_ids_del_texto(cid, textos):
    """(a) y (b) de la D44, sobre el TEXTO que viaja al prompt del redactor."""
    for t in textos:
        if not isinstance(t, str):
            continue
        for bare, rx in RX_BARE.items():
            if rx.search(t):
                falla(f'{cid}: cita el id «{bare}» SIN SUFIJO (D44 · §5.2). '
                      'Las once familias sólo existen con sufijo y `CHS-41` es '
                      'un agregado de fiabilidad baja: cítalos uno a uno '
                      f'(«{bare}a», «{bare}b»…).')
        for sid in RX_ID.findall(t):
            ficha = idx.get(sid)
            if ficha is None:
                falla(f'{cid}: el texto cita un id que no existe en el '
                      f'research: «{sid}»')
                continue
            if ficha.get('fiabilidad') == 'baja':
                if ficha.get('cifra') not in (None, ''):
                    falla(f'{cid}: cita como CIFRA el id «{sid}», que es de '
                          'fiabilidad BAJA (hueco deliberado del research: no '
                          'se rellena ni se convierte en texto de la guía)')
                else:
                    avisa(f'{cid}: menciona el id «{sid}», de fiabilidad baja '
                          '(sin cifra: sólo puede usarse como hecho '
                          'cualitativo, nunca como número)')


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

        # --- puntos_por_epigrafe (D45a) y puntos_globales
        ppe = cap.get('puntos_por_epigrafe')
        if not ppe:
            falla(f'{cid}: sin «puntos_por_epigrafe» (D45: es obligatorio en '
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
                revisa_ids_del_texto(cid, ps)
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
        revisa_ids_del_texto(cid, globales)
        revisa_ids_del_texto(cid, cap.get('prohibido') or [])

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
            # A2 (2026-09-10): un formato NUMÉRICO sobre una celda de TEXTO no
            # rompía nada -`formatear` cae en `str(v)`- y el redactor recibía
            # una etiqueta numérica con un veredicto de texto detrás. De ahí
            # salió la única cifra inventada del pack de Pastelería.
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
            for bare, rx in RX_BARE.items():
                if rx.fullmatch(sid):
                    falla(f'{cid}: «sector» trae el id «{bare}» SIN SUFIJO '
                          '(D44 · §5.2): cítalo con su sufijo, uno a uno')

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

# los nueve libros del pack tienen que estar todos en dl/
libros = sorted(f for f in os.listdir(XLSX_DIR) if f.endswith('.xlsx'))
print(f'\nlibros en {XLSX_DIR}: {len(libros)}')
if len(libros) != N_LIBROS:
    falla(f'se esperaban {N_LIBROS} libros en dl/ y hay {len(libros)}: {libros}')

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
bajas = [i for i in ids if (idx.get(i) or {}).get('fiabilidad') == 'baja']
print(f'ids de sector distintos usados: {len(ids)} '
      f'(CHN {len([i for i in ids if i.startswith("CHN-")])} · '
      f'CHS {len([i for i in ids if i.startswith("CHS-")])} · '
      f'PA {len([i for i in ids if i.startswith("PA-")])})')
print(f'de ellos, de fiabilidad baja (huecos declarados, nunca cifra): '
      f'{len(bajas)}')
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
      '0 ids de sector inexistentes, 0 ids «bare» de D44, '
      '0 cifras de fiabilidad baja, 0 caracteres no latinos.')
