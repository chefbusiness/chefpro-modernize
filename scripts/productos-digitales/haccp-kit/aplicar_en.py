#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
aplicar_en.py — HACCP Food Safety Kit Pro (EN) · montaje de los 21 xlsx desde el Pack Plantillas APPCC v2.0 publicado.

SPEC que manda: `SPEC.md` (§2 mapas, §3 límites, §4-§5, §7 pasos 3-5, D1-D27). Sesión Claude Code, 3-oct-2026.
Copia adaptada de `restaurant-inventory-kit/aplicar_en.py`: misma maquinaria (renombrado de hojas con reescritura de
referencias, literales en fórmulas/CF/DV, traducción por celda, fechas, US Letter + pie, docProps, apóstrofos rectos,
huella de idempotencia, `inject_cache` AL FINAL, `--dry-run`, `--idempotencia`) y las capas PROPIAS del HACCP. Aquí
no se redacta nada: los textos salen de `textos_en/G*.json` (subagentes Anthropic, regla 1bis) y de `mapas.py`.

    python3 aplicar_en.py                      # escribe en astro-site/public/dl/haccp-templates/
    python3 aplicar_en.py --dry-run [--salida <carpeta>] [--mes October] [--idempotencia] [--json informe.json]
    python3 aplicar_en.py --dry-run --parcial  # deja en español lo que aún no tenga traducción (solo ensayo)

Los ficheros ES de `dl/pack-appcc/` se abren en SOLO LECTURA y nunca se escriben.

Orden por libro, siempre desde una copia limpia del ES publicado (→ idempotente):
   1. carga del xlsx ES y renombrado de hojas (mapas.HOJAS) reescribiendo las referencias de las fórmulas y DV;
   2. fórmulas: los 17 patrones de mapas.FORMULAS_EN celda a celda (D10-D17); el resto, literales por mapas.CLAVES
      (estricto: un literal sin clave aborta);
   3. textos POR APARICIÓN (textos_es.json `donde`): traducir/localizar → textos_en, mapa-clave → CLAVES, mapa-hoja →
      HOJAS; línea de versión, firma, línea de conservación (D19, D21) y pie de página (D21);
   4. DV: listas por CLAVES, D13 (lista especial del 16), DV numéricas en °C → °F (DV_NUM), referencias de hoja,
      mensajes por aparición; D14 (+1 DV decimal en 17 Cooling I5:I44);
   5. CF: literales por CLAVES (estricto);
   6. capas regeneradas: LIMITES_02 (+ lista de Instructions B13:B22), SEVERIDAD_15, POR_CELDA, EJEMPLOS_NUM,
      TEMP_COLUMNAS (°C→°F half-up), PARAMETROS (fila 3 nueva de 17 Thawing y 18, D15-D16), ALTITUD_19, SIN_LETRAS;
   7. fechas de texto → fechas reales (I1, 62 celdas); formatos: fecha 14, fecha-hora 22, hora 18 (D21); papel
      US Letter en las 48 hojas;
   8. docProps D21, título interior (Instructions!B2) comprobado, apóstrofos y comillas rectas;
   9. cobertura: toda aparición «regenerar» del ES tiene que haberla escrito una capa;
  10. guardado con el nombre EN (mapas.FICHEROS) e inject_cache.py AL FINAL sobre los 21.

Térmica: todo en SERIE; `istats` antes de cada libro y de cada inject_cache (espera si ≥ 62 °C hasta < 60 °C). En el
VPS (D27) no hay istats y la guarda no espera.
"""
import argparse
import copy
import datetime
import glob
import json
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(AQUI)
REPO = os.path.dirname(os.path.dirname(SCRIPTS))
sys.path.insert(0, AQUI)

import openpyxl                                              # noqa: E402
from openpyxl.worksheet.datavalidation import DataValidation  # noqa: E402

import mapas                                                 # noqa: E402
import extraer_textos                                        # noqa: E402

logging.disable(logging.CRITICAL)

ORIGEN = os.path.join(REPO, 'astro-site', 'public', 'dl', 'pack-appcc')
DESTINO_REAL = os.path.join(REPO, 'astro-site', 'public', 'dl', mapas.SLUG)   # haccp-templates
INJECT = os.path.join(SCRIPTS, 'inject_cache.py')

VERSION = '2.0'
SUBJECT = mapas.PRODUCTO + ' · v2.0'                                  # D21
DESCRIPTION = mapas.URL_PRODUCTO
KEYWORDS = 'haccp plan template, food safety logs, AI Chef Pro'
CATEGORY = 'AI Chef Pro · Digital products'
CREATOR = 'AI Chef Pro'
PIE_EN = mapas.FOOTER_EN                                              # D21: «AI Chef Pro · aichef.pro · Page &P of &N»
MESES = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
         'September', 'October', 'November', 'December']
VERDE = 'E8F5E9'
FMT_FECHA = 'mm-dd-yy'                     # numFmtId 14 (fecha corta del sistema)
FMT_FECHA_HORA = 'm/d/yy h:mm AM/PM'       # formato propio (revisión final): reloj de 12 h, como las horas sueltas
FMT_HORA = 'h:mm AM/PM'                    # numFmtId 18
NUMFMT = {FMT_FECHA: 14, FMT_FECHA_HORA: None, FMT_HORA: 18}   # None = formato propio: G3 lo compara por cadena
INVARIABLES = set(extraer_textos.INVARIABLES)
RX_VERSION_ES = extraer_textos.RX_VERSION
HOJA_INSTR_EN = mapas.HOJAS['Instrucciones']
CLAVES = mapas.CLAVES
CAMPO_DV = {'dv-error-titulo': 'errorTitle', 'dv-error': 'error', 'dv-prompt-titulo': 'promptTitle', 'dv-prompt': 'prompt'}

# Datos de ejemplo de SPEC §5 que no son temperaturas (mapas.EJEMPLOS_NUM solo cubre °F): 09 «Used Oil Pickups»
# B5 = 40 L → 10 gal (la cabecera EN es «Gallons collected»). Mandan sobre el valor ES, como EJEMPLOS_NUM.
EJEMPLOS_EXTRA = OrderedDict([
    (('09', 'Retirada de aceite usado', 'B5'), 10),
])
# D14 · 17 Cooling: la columna I pasa a lectura de 6 h con DV decimal (+1 DV), mismo rango que D/F
D14 = {'hoja': 'Enfriamiento', 'sqref': 'I5:I44', 'modelo': 'D5:D44', 'f1': '-22', 'f2': '266'}
# D15-D16: la fila 3 nueva copia el estilo de 19!A3:C3 (etiqueta · celda verde · nota)
MODELO_PARAM = ('19-verificacion-termometros.xlsx', 'Verificación Termómetros')


class Aborta(Exception):
    pass


# ==========================================================================
# Térmica (regla del Mac: se apaga por encima de ~65 °C; en el VPS no hay istats)
# ==========================================================================
def termica(umbral=62, reanuda=60):
    def leer():
        try:
            out = subprocess.run(['istats', 'cpu', 'temp', '--value-only'], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, universal_newlines=True, timeout=20).stdout
            return float(re.findall(r'[\d.]+', out)[0])
        except Exception:
            return None
    t = leer()
    if t is None or t < umbral:
        return t
    while t is not None and t >= reanuda:
        print('  [térmica] CPU %.1f °C: espero 30 s' % t, flush=True)
        time.sleep(30)
        t = leer()
    return t


# ==========================================================================
# Datos
# ==========================================================================
def cargar_datos(parcial=False):
    te = json.load(open(os.path.join(AQUI, 'textos_es.json'), encoding='utf-8'))
    censo = json.load(open(os.path.join(AQUI, 'censo_es.json'), encoding='utf-8'))
    tx = OrderedDict()
    for p in sorted(glob.glob(os.path.join(AQUI, 'textos_en', 'G[0-9].json'))):
        for k, v in json.load(open(p, encoding='utf-8')).items():
            if k in tx and tx[k] != v:
                raise Aborta('traducción contradictoria para %s en %s' % (k, os.path.basename(p)))
            tx[k] = v
    ids = {c['id'] for c in te['cadenas']}
    ajenas = sorted(set(tx) - ids)
    if ajenas:
        raise Aborta('textos_en trae ids que no están en textos_es.json: %r' % ajenas[:5])
    faltan = [c['id'] for c in te['cadenas'] if c['grupo'] != 'GM' and c['id'] not in tx]
    if faltan and not parcial:
        raise Aborta('%d cadenas G1-G3 sin traducción (p. ej. %r)' % (len(faltan), faltan[:5]))
    celdas, dvmsg = {}, {}
    for c in te['cadenas']:
        for d in c['donde']:
            if d['t'] == 'celda':
                celdas[(d['f'], d['h'], d['c'])] = (c['id'], d['tr'], c['es'])
            elif d['t'] in CAMPO_DV:
                dvmsg[(d['f'], d['h'], d['c'], CAMPO_DV[d['t']])] = (c['id'], d['tr'], c['es'])
    return {'te': te, 'censo': censo, 'tx': tx, 'celdas': celdas, 'dvmsg': dvmsg, 'faltan': faltan,
            'parcial': parcial}


def mes_por_defecto():
    return MESES[datetime.date.today().month - 1]


def linea_version(mes):
    return 'Version %s · %s %d · %s · info@aichef.pro' % (VERSION, mes, datetime.date.today().year, DESCRIPTION)


def f_a_c(f):
    """°F → °C entero half-up (solo para el «(nn °C)» de los textos regenerados)."""
    c = (f - 32) * 5.0 / 9.0
    return int(__import__('math').floor(c + 0.5))


# ==========================================================================
# Fórmulas: hojas y literales
# ==========================================================================
RX_STR = re.compile(r'"(?:[^"]|"")*"')
RX_REF = re.compile(r"(?:'((?:[^']|'')+)'|([^\W\d][\w.]*))!")


def ref_hoja(nombre):
    """Nombre de hoja tal como va en una fórmula (entre comillas si hace falta)."""
    if re.fullmatch(r'[A-Za-z_][A-Za-z0-9_.]*', nombre):
        return nombre
    return "'" + nombre.replace("'", "''") + "'"


class Transformador:
    """Reescribe una fórmula ES a EN: referencias de hoja (fuera de literales) y literales (dentro, ESTRICTO)."""

    def __init__(self, mapa_hojas, literales=CLAVES):
        self.mapa = mapa_hojas
        self.en = set(mapa_hojas.values())
        self.lit = literales
        self.hojas_citadas = 0
        self.literales = 0

    def refs(self, s):
        def rep(m):
            nombre = (m.group(1) if m.group(1) is not None else m.group(2)).replace("''", "'")
            if nombre in self.mapa:
                self.hojas_citadas += 1
                return ref_hoja(self.mapa[nombre]) + '!'
            if nombre in self.en:
                return m.group(0)
            raise Aborta('hoja desconocida en fórmula: %r en %r' % (nombre, s[:80]))
        return RX_REF.sub(rep, s)

    def formula(self, f):
        out, pos = [], 0
        for m in RX_STR.finditer(f):
            out.append(self.refs(f[pos:m.start()]))
            lit = m.group(0)[1:-1].replace('""', '"')
            if lit:
                if lit not in self.lit:
                    raise Aborta('literal sin clave EN %r en %r' % (lit, f[:90]))
                lit = self.lit[lit]
                self.literales += 1
            out.append('"' + lit.replace('"', '""') + '"')
            pos = m.end()
        out.append(self.refs(f[pos:]))
        return ''.join(out)

    def celda(self, v):
        return '=' + self.formula(v[1:]) if v.startswith('=') else self.formula(v)


def formula_en(v, fila, T):
    """Fórmula EN de una celda: patrón de FORMULAS_EN (D10-D17) o HOJAS + CLAVES. Devuelve (nueva, es_patron)."""
    pat = mapas.patron(v)
    if pat in mapas.FORMULAS_EN:
        if pat.replace('{r}', str(fila)) != v:
            raise Aborta('patrón FORMULAS_EN que no es de una sola fila: %r' % v[:90])
        return mapas.FORMULAS_EN[pat].replace('{r}', str(fila)), True
    return T.celda(v), False


def rango(ref):
    c1, r1, c2, r2 = openpyxl.utils.cell.range_boundaries(ref)
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            yield '%s%d' % (openpyxl.utils.get_column_letter(c), r)


def renombrar(wb):
    mapa = OrderedDict((ws.title, mapas.HOJAS[ws.title]) for ws in wb.worksheets)
    for ws in wb.worksheets:
        ws.title = mapa[ws.title]
    if wb.sheetnames != list(mapa.values()):
        raise Aborta('renombrado: %r ≠ %r' % (wb.sheetnames, list(mapa.values())))
    return mapa


def reescribir_formulas(wb, T, rep):
    n = pat = 0
    for ws in wb.worksheets:
        for c in list(ws._cells.values()):
            if c.data_type == 'f' and isinstance(c.value, str):
                nuevo, es_pat = formula_en(c.value, c.row, T)
                pat += es_pat
                if nuevo != c.value:
                    c.value = nuevo
                    n += 1
    rep['formulas_reescritas'] = n
    rep['formulas_patron_en'] = pat


# ==========================================================================
# Textos por aparición
# ==========================================================================
class Libro:
    """Estado de un libro en construcción: celdas escritas por capas (cobertura de «regenerar»)."""

    def __init__(self, wb, corto, mapa, datos, rep):
        self.wb, self.corto, self.mapa, self.datos, self.rep = wb, corto, mapa, datos, rep
        self.inv = {en: es for es, en in mapa.items()}
        self.escritas = set()                 # (hoja_es, celda)
        self.faltan = rep.setdefault('faltan', [])

    def ws(self, hoja_es):
        return self.wb[self.mapa[hoja_es]]

    def poner(self, hoja_es, coord, valor, es_esperado=None, tipo=None):
        c = self.ws(hoja_es)[coord]
        if c.data_type == 'f' or (isinstance(c.value, str) and c.value.startswith('=')):
            raise Aborta('%s %s!%s es una fórmula (%r): una capa no la pisa' % (self.corto, hoja_es, coord, c.value))
        if es_esperado is not None and not es_esperado(c.value):
            raise Aborta('%s %s!%s: el ES trae %r, no lo esperado' % (self.corto, hoja_es, coord, c.value))
        c.value = valor
        self.escritas.add((hoja_es, coord))
        return c

    def en_de(self, ident, tr, es, lugar):
        if tr in ('traducir', 'localizar'):
            en = self.datos['tx'].get(ident)
            if en is None:
                self.faltan.append('%s %s %r' % (lugar, ident, es[:60]))
                return es
            return en
        if tr == 'mapa-clave':
            return CLAVES[es]
        if tr == 'mapa-hoja':
            return mapas.HOJAS[es]
        return None                                              # regenerar: lo escribe una capa


def traducir_textos(L, mes):
    n = 0
    regenerar = []
    for ws in L.wb.worksheets:
        h_es = L.inv[ws.title]
        for c in list(ws._cells.values()):
            v = c.value
            if not isinstance(v, str) or c.data_type == 'f':
                continue
            if RX_VERSION_ES.match(v):
                L.poner(h_es, c.coordinate, linea_version(mes))
                n += 1
                continue
            if v == mapas.PIE_ES:
                L.poner(h_es, c.coordinate, mapas.PIE_EN)
                n += 1
                continue
            if v.replace('▸ ', '', 1) == mapas.CONSERVAR_ES:
                L.poner(h_es, c.coordinate, v[:len(v) - len(mapas.CONSERVAR_ES)] + mapas.CONSERVAR_EN)
                n += 1
                continue
            k = (L.corto, h_es, c.coordinate)
            if k not in L.datos['celdas']:
                if any(ch.isalpha() for ch in v) and v not in INVARIABLES:
                    raise Aborta('%s %s!%s: texto %r fuera de textos_es.json' % (L.corto, h_es, c.coordinate, v[:60]))
                continue                                         # sin letras / invariable (SIN_LETRAS, fechas, ☐…)
            ident, tr, es = L.datos['celdas'][k]
            if es != v:
                raise Aborta('%s %s!%s: textos_es.json dice %r y el ES trae %r' % (L.corto, h_es, c.coordinate, es[:40], v[:40]))
            en = L.en_de(ident, tr, es, '%s %s!%s' % (L.corto, ws.title, c.coordinate))
            if en is None:
                regenerar.append((h_es, c.coordinate))
                continue
            if en != v:
                c.value = en
                n += 1
        for parte in ('oddHeader', 'oddFooter', 'evenHeader', 'evenFooter', 'firstHeader', 'firstFooter'):
            hf = getattr(ws, parte)
            for pos in ('left', 'center', 'right'):
                t = getattr(hf, pos).text
                if not t:
                    continue
                if 'Página &P' not in t:
                    raise Aborta('%s %s %s.%s inesperado: %r' % (L.corto, ws.title, parte, pos, t))
                getattr(hf, pos).text = PIE_EN
    L.rep['textos_traducidos'] = n
    return regenerar


# ==========================================================================
# DV y CF
# ==========================================================================
def dv_censo(L, h_es, sq):
    for d in L.datos['censo']['libros'][L.rep['es']]['hojas_detalle'][h_es]['dv']:
        if d['sqref'] == sq:
            return d
    raise Aborta('%s %s: DV %s no está en el censo' % (L.corto, h_es, sq))


def dv_num(L, h_es, sq, f1, f2):
    for k, (es, en) in mapas.DV_NUM.items():
        if k[:2] == (L.corto, h_es) and (len(k) == 2 or sq.startswith(k[2])):
            if (f1, f2) != es:
                raise Aborta('%s %s DV %s: ES %r ≠ DV_NUM %r' % (L.corto, h_es, sq, (f1, f2), es))
            return en
    raise Aborta('%s %s DV %s de temperatura sin DV_NUM' % (L.corto, h_es, sq))


def reescribir_dv_cf(L, T):
    n = OrderedDict([('dv_listas', 0), ('dv_especiales', 0), ('dv_num', 0), ('dv_ref', 0), ('dv_mensajes', 0),
                     ('cf_reglas', 0)])
    for ws in L.wb.worksheets:
        h_es = L.inv[ws.title]
        for dv in ws.data_validations.dataValidation:
            sq = str(dv.sqref)
            f1 = dv.formula1 or ''
            cen = dv_censo(L, h_es, sq)
            esp = mapas.DV_LISTAS_ESPECIALES.get((L.corto, h_es, sq))
            if esp:
                if f1 != esp[0]:
                    raise Aborta('%s %s DV %s: lista especial ES cambiada %r' % (L.corto, h_es, sq, f1))
                dv.formula1 = esp[1]
                n['dv_especiales'] += 1
            elif f1.startswith('"'):
                items = f1.strip('"').split(',')
                faltan = [x for x in items if x not in CLAVES]
                if faltan:
                    raise Aborta('%s %s: DV %s con ítems sin clave EN %r' % (L.corto, h_es, sq, faltan))
                dv.formula1 = mapas.dv_lista(CLAVES[x] for x in items)
                if len(dv.formula1) > 257:
                    raise Aborta('%s %s: DV %s > 255 caracteres' % (L.corto, h_es, sq))
                n['dv_listas'] += 1
            elif dv.type in ('decimal', 'whole') and cen['cita_temp']:
                dv.formula1, dv.formula2 = dv_num(L, h_es, sq, dv.formula1, dv.formula2)
                n['dv_num'] += 1
            elif f1:
                dv.formula1 = T.refs(f1)
                if dv.formula2:
                    dv.formula2 = T.refs(dv.formula2)
                n['dv_ref'] += 1
            for attr in ('error', 'errorTitle', 'prompt', 'promptTitle'):
                v = getattr(dv, attr)
                if not v:
                    continue
                k = (L.corto, h_es, sq, attr)
                if k not in L.datos['dvmsg']:
                    raise Aborta('%s %s DV %s %s fuera de textos_es.json: %r' % (L.corto, h_es, sq, attr, v[:50]))
                ident, tr, es = L.datos['dvmsg'][k]
                en = L.en_de(ident, tr, es, '%s DV %s %s' % (ws.title, sq, attr))
                if en is None:
                    raise Aborta('%s %s DV %s %s marcado «regenerar»' % (L.corto, h_es, sq, attr))
                setattr(dv, attr, en)
                n['dv_mensajes'] += 1
        for cf in ws.conditional_formatting:
            for regla in cf.rules:
                if regla.formula:
                    regla.formula = [T.formula(x) for x in regla.formula]
                    n['cf_reglas'] += 1
                if regla.text:
                    raise Aborta('%s %s: CF %s con texto (no previsto en el pack)' % (L.corto, h_es, cf.sqref))
    L.rep.update(n)


def d14_dv(L):
    """D14: +1 DV decimal en 17 Cooling I5:I44 (lectura de 6 h, °F), con flags y mensajes EN de la DV de D/F."""
    ws = L.ws(D14['hoja'])
    modelo = [dv for dv in ws.data_validations.dataValidation if D14['modelo'] in str(dv.sqref).split()]
    if len(modelo) != 1 or (modelo[0].formula1, modelo[0].formula2) != (D14['f1'], D14['f2']):
        raise Aborta('17 D14: DV modelo %s no encontrada o sin °F' % D14['modelo'])
    m = modelo[0]
    nueva = DataValidation(type='decimal', operator='between', formula1=D14['f1'], formula2=D14['f2'],
                           allow_blank=m.allow_blank, showErrorMessage=m.showErrorMessage,
                           showInputMessage=m.showInputMessage, errorStyle=m.errorStyle,
                           errorTitle=m.errorTitle, error=m.error, promptTitle=m.promptTitle, prompt=m.prompt)
    nueva.add(D14['sqref'])
    ws.add_data_validation(nueva)
    fmt = ws['D5'].number_format
    for coord in rango(D14['sqref']):
        ws[coord].number_format = fmt
    L.rep['d14_dv'] = D14['sqref']


# ==========================================================================
# Capas regeneradas (mapas.py)
# ==========================================================================
def comillas_rectas(t):
    return t.replace('«', '"').replace('»', '"')


def capa_02(L):
    ws = L.ws('Límites')
    for i, (fam, mx, base) in enumerate(mapas.LIMITES_02):
        r = 5 + i
        L.poner('Límites', 'A%d' % r, fam, lambda v: isinstance(v, str) and v)
        L.poner('Límites', 'B%d' % r, mx, lambda v: v is not None)
        L.poner('Límites', 'C%d' % r, comillas_rectas(base), lambda v: isinstance(v, str) and v)
    for r in range(15, 21):                          # filas libres A15:C20 intactas (vacías en el ES)
        for col in 'ABC':
            if ws['%s%d' % (col, r)].value is not None:
                raise Aborta('02 Limits %s%d no está vacía' % (col, r))
    for i, (fam, mx, base) in enumerate(mapas.LIMITES_02):
        r = 13 + i
        if mx == 'N/A':
            t = '▸ %s → no temperature limit (N/A)' % fam
        else:
            t = '▸ %s → max. %d °F (%d °C)' % (fam, mx, f_a_c(mx))
        L.poner('Instrucciones', 'B%d' % r, t, lambda v: isinstance(v, str) and v.startswith('▸ '))
    L.rep['limites_02'] = len(mapas.LIMITES_02)


def capa_15(L):
    ws = L.ws('25 Puntos Inspección')
    gravedades = {'Leve', 'Grave', 'Muy grave'}
    filas_es = {c.row for c in ws._cells.values() if c.column == 4 and c.value in gravedades}
    if filas_es != set(mapas.SEVERIDAD_15):
        raise Aborta('15: filas con gravedad %s ≠ SEVERIDAD_15 %s' % (sorted(filas_es), sorted(mapas.SEVERIDAD_15)))
    for r, (cat, _sec) in mapas.SEVERIDAD_15.items():
        L.poner('25 Puntos Inspección', 'D%d' % r, cat, lambda v: v in gravedades)
    L.rep['severidad_15'] = len(mapas.SEVERIDAD_15)


def capa_celdas(L):
    """POR_CELDA, EJEMPLOS_NUM, EJEMPLOS_EXTRA, SIN_LETRAS (mapas) y ALTITUD_19 sobre la fila 3 del 19."""
    n = 0
    for (c, h, coord), v in mapas.POR_CELDA.items():
        if c == L.corto:
            L.poner(h, coord, v, lambda x: isinstance(x, str))
            n += 1
    for (c, h, coord), v in list(mapas.EJEMPLOS_NUM.items()) + list(EJEMPLOS_EXTRA.items()):
        if c != L.corto:
            continue
        if isinstance(v, str) and re.fullmatch(r'\+\d+h', v):
            fila = int(re.search(r'\d+', coord).group(0))
            entrada = L.ws(h)['D%d' % fila].value
            if not isinstance(entrada, datetime.datetime):
                raise Aborta('%s %s!D%d no es fecha-hora (%r): no puedo sumar %s' % (c, h, fila, entrada, v))
            v = entrada + datetime.timedelta(hours=int(v[1:-1]))
        L.poner(h, coord, v)
        n += 1
    for (c, h, coord), v in mapas.SIN_LETRAS.items():
        if c == L.corto:
            L.poner(h, coord, v, lambda x: isinstance(x, str) and not any(ch.isalpha() for ch in x if ch not in 'MT'))
            n += 1
    if L.corto == '19':
        L.poner('Verificación Termómetros', 'A3', mapas.ALTITUD_19[0], lambda x: isinstance(x, str))
        L.poner('Verificación Termómetros', 'C3', mapas.ALTITUD_19[1], lambda x: isinstance(x, str))
        envolver_a3(L.ws('Verificación Termómetros'), '19')
        n += 2
    L.rep['capa_celdas'] = n


def capa_temperaturas(L):
    """°C → °F (half-up, mapas.c_a_f) en las columnas de ejemplo de mapas.TEMP_COLUMNAS (salvo overrides)."""
    n = 0
    fijas = {(h, coord) for (c, h, coord) in list(mapas.EJEMPLOS_NUM) + list(EJEMPLOS_EXTRA) if c == L.corto}
    for (c, h), (cols, dec) in mapas.TEMP_COLUMNAS.items():
        if c != L.corto:
            continue
        ws = L.ws(h)
        for cel in list(ws._cells.values()):
            v = cel.value
            if openpyxl.utils.get_column_letter(cel.column) not in cols or (h, cel.coordinate) in fijas:
                continue
            if isinstance(v, bool) or not isinstance(v, (int, float)):
                continue
            L.poner(h, cel.coordinate, mapas.c_a_f(v, dec))
            n += 1
    L.rep['temperaturas_f'] = n


# Revisión final: la etiqueta de A3 (columna de 14) salía cortada en 17 Thawing, 18 y 19 → ajuste de texto y fila 3
# más alta (2-3 líneas en 17/18; la del 19 ocupa 4).
ALTO_FILA3 = {'17': 45, '18': 45, '19': 60}


def envolver_a3(ws, corto):
    al = copy.copy(ws['A3'].alignment)
    al.wrap_text = True
    al.vertical = al.vertical or 'center'
    ws['A3'].alignment = al
    ws.row_dimensions[3].height = ALTO_FILA3[corto]


def estilo_de(dst, src):
    dst.font = copy.copy(src.font)
    dst.fill = copy.copy(src.fill)
    dst.border = copy.copy(src.border)
    dst.alignment = copy.copy(src.alignment)
    dst.protection = copy.copy(src.protection)
    dst.number_format = src.number_format


def capa_parametros(L, modelo):
    """D15-D16: fila 3 nueva (etiqueta · celda verde · nota) en 17 Thawing y 18 Parasite Destruction."""
    n = 0
    for (c, h), (etiqueta, valor, nota) in mapas.PARAMETROS.items():
        if c != L.corto:
            continue
        ws = L.ws(h)
        for coord in ('A3', 'B3', 'C3'):
            if ws[coord].value is not None:
                raise Aborta('%s %s!%s no está vacía en el ES' % (c, h, coord))
        if any(m.min_row <= 3 <= m.max_row for m in ws.merged_cells.ranges):
            raise Aborta('%s %s: la fila 3 tiene celdas combinadas' % (c, h))
        for coord, v in (('A3', etiqueta), ('B3', valor), ('C3', nota)):
            cel = L.poner(h, coord, v)
            estilo_de(cel, modelo[coord])
            n += 1
        envolver_a3(ws, c)
    L.rep['parametros'] = n


def fechas_texto(L):
    """I1: las fechas de ejemplo escritas como TEXTO dd/mm/aaaa pasan a fechas reales con numFmtId 14."""
    n = 0
    for h, hd in L.datos['censo']['libros'][L.rep['es']]['hojas_detalle'].items():
        for x in hd['fechas_texto']:
            cel = L.ws(h)[x['celda']]
            if cel.value != x['texto']:
                raise Aborta('%s %s!%s: fecha de texto %r ≠ censo %r' % (L.corto, h, x['celda'], cel.value, x['texto']))
            texto = mapas.FECHAS_TEXTO_EN.get((L.corto, h, x['celda']), x['texto'])   # revisión final: INC-001
            cel.value = datetime.datetime.strptime(texto, '%d/%m/%Y')
            cel.number_format = FMT_FECHA
            n += 1
    L.rep['fechas_texto'] = n


def tipo_fecha(fmt):
    f = (fmt or '').lower()
    hora = 'h' in f
    fecha = 'd' in f or 'y' in f
    if hora and fecha:
        return FMT_FECHA_HORA
    if hora:
        return FMT_HORA
    return FMT_FECHA


def formatos_y_papel(L):
    """D21: fechas → 14, fecha-hora → 22, horas → 18 (según el formato ES de cada celda del censo); formatos
    propios dd/mm sin uso → variantes US; US Letter en todas las hojas."""
    wb = L.wb
    n = OrderedDict([('fecha', 0), ('fecha_hora', 0), ('hora', 0)])
    for h, hd in L.datos['censo']['libros'][L.rep['es']]['hojas_detalle'].items():
        ws = L.ws(h)
        for x in hd['fechas']:
            fmt = tipo_fecha(x['formato'])
            ws[x['celda']].number_format = fmt
            n[{FMT_FECHA: 'fecha', FMT_FECHA_HORA: 'fecha_hora', FMT_HORA: 'hora'}[fmt]] += 1
    for ws in wb.worksheets:
        ws.page_setup.paperSize = ws.PAPERSIZE_LETTER
    nf = wb._number_formats
    usados = set(nf)
    for i, f in enumerate(list(nf)):
        fl = f.lower()
        if re.search(r'dd/mm|hh:mm|yyyy-mm-dd', fl) and 'am/pm' not in fl:
            nuevo = {FMT_FECHA: 'm/d/yyyy', FMT_FECHA_HORA: 'm/d/yyyy h:mm AM/PM', FMT_HORA: 'h:mm AM/PM'}[tipo_fecha(f)]
            while nuevo in usados:
                nuevo += ';@'
            usados.add(nuevo)
            list.__setitem__(nf, i, nuevo)
    if len(set(nf)) != len(nf):
        raise Aborta('formatos propios repetidos: %r' % list(nf))
    nf._dict = {v: i for i, v in enumerate(nf)}
    nf.clean = True
    L.rep.update(('celdas_' + k, v) for k, v in n.items())


COMILLAS = {'\u2019': "'", '\u2018': "'", '\u201c': '"', '\u201d': '"'}


def normalizar_comillas(L):
    n = 0

    def norm(v):
        for a, b in COMILLAS.items():
            v = v.replace(a, b)
        return v
    for ws in L.wb.worksheets:
        for c in list(ws._cells.values()):
            if isinstance(c.value, str) and c.data_type != 'f' and any(a in c.value for a in COMILLAS):
                c.value = norm(c.value)
                n += 1
        for dv in ws.data_validations.dataValidation:
            for attr in ('error', 'errorTitle', 'prompt', 'promptTitle'):
                v = getattr(dv, attr)
                if v and any(a in v for a in COMILLAS):
                    setattr(dv, attr, norm(v))
                    n += 1
    L.rep['comillas_normalizadas'] = n


def metadatos(L, fname_en):
    p = L.wb.properties
    p.title = mapas.TITULOS[fname_en]                 # D5
    p.subject = SUBJECT
    p.keywords = KEYWORDS
    p.description = DESCRIPTION
    p.category = CATEGORY
    p.creator = CREATOR
    p.lastModifiedBy = CREATOR
    L.rep['docprops'] = OrderedDict((k, getattr(p, k)) for k in
                                    ('title', 'subject', 'creator', 'keywords', 'description', 'category'))


def comprobar_titulo(L, fname_en):
    """D5: el título interior (Instructions!B2) es EXACTAMENTE el de mapas.TITULOS. Nunca se parchea."""
    esperado = mapas.TITULOS[fname_en]
    v = L.wb[HOJA_INSTR_EN]['B2'].value
    if v != esperado and not L.datos['parcial']:
        raise Aborta('%s: Instructions!B2 %r ≠ D5 %r' % (fname_en, v, esperado))
    L.rep['titulo'] = v


# ==========================================================================
# Un libro
# ==========================================================================
def construir_libro(fname_es, carpeta, datos, mes, modelo_param):
    fname_en = mapas.FICHEROS[fname_es]
    corto = extraer_textos.corto(fname_es)
    rep = OrderedDict([('es', fname_es), ('en', fname_en)])
    wb = openpyxl.load_workbook(os.path.join(ORIGEN, fname_es))
    mapa = renombrar(wb)                                                       # 1
    L = Libro(wb, corto, mapa, datos, rep)
    T = Transformador(mapa)
    reescribir_formulas(wb, T, rep)                                            # 2
    regenerar = traducir_textos(L, mes)                                        # 3
    reescribir_dv_cf(L, T)                                                     # 4-5
    if corto == '17':
        d14_dv(L)
    if corto == '02':                                                          # 6
        capa_02(L)
    if corto == '15':
        capa_15(L)
    capa_celdas(L)
    capa_temperaturas(L)
    capa_parametros(L, modelo_param)
    rep['refs_hoja'] = T.hojas_citadas
    rep['literales'] = T.literales
    fechas_texto(L)                                                            # 7
    formatos_y_papel(L)
    metadatos(L, fname_en)                                                     # 8
    comprobar_titulo(L, fname_en)
    normalizar_comillas(L)
    sin_capa = [x for x in regenerar if x not in L.escritas]                   # 9
    if sin_capa:
        raise Aborta('%s: apariciones «regenerar» que ninguna capa escribió: %r' % (fname_es, sin_capa[:8]))
    rep['regeneradas'] = len(regenerar)
    if rep['faltan'] and not datos['parcial']:
        raise Aborta('%s: %d textos sin traducción:\n  %s' % (fname_es, len(rep['faltan']), '\n  '.join(rep['faltan'][:20])))
    wb.save(os.path.join(carpeta, fname_en))                                  # 10
    return rep


def modelo_parametros():
    wb = openpyxl.load_workbook(os.path.join(ORIGEN, MODELO_PARAM[0]))
    ws = wb[MODELO_PARAM[1]]
    return {k: ws[k] for k in ('A3', 'B3', 'C3')}


def construir(carpeta, datos, mes, log=print):
    os.makedirs(carpeta, exist_ok=True)
    modelo = modelo_parametros()
    informe = []
    for fname_es in mapas.LIBROS_ES:
        termica()
        rep = construir_libro(fname_es, carpeta, datos, mes, modelo)
        informe.append(rep)
        log('  %-44s fórmulas %4d (EN %3d) · refs %3d · lit %4d · textos %4d · regen %3d · °F %2d · faltan %d'
            % (rep['en'], rep['formulas_reescritas'], rep['formulas_patron_en'], rep['refs_hoja'], rep['literales'],
               rep['textos_traducidos'], rep['regeneradas'], rep['temperaturas_f'], len(rep['faltan'])))
    return informe


# ==========================================================================
# Idempotencia (huella comparable, sin fechas de guardado)
# ==========================================================================
def digest(path):
    wb = openpyxl.load_workbook(path)
    p = wb.properties
    fuera = {'_props': (p.title, p.subject, p.keywords, p.description, p.category, p.creator)}
    for ws in wb.worksheets:
        celdas = {}
        for c in ws._cells.values():
            if c.value is None and not (c.fill is not None and c.fill.fill_type == 'solid'):
                continue
            relleno = str(c.fill.fgColor.rgb) if c.fill is not None and c.fill.fill_type == 'solid' else None
            celdas[c.coordinate] = (repr(c.value), c.number_format, relleno, bool(c.protection.locked))
        fuera[ws.title] = {
            'celdas': celdas,
            'merges': sorted(str(m) for m in ws.merged_cells.ranges),
            'dv': sorted('%s:%s:%s:%s:%s:%s' % (dv.type, dv.formula1, dv.formula2, dv.sqref, dv.error, dv.prompt)
                         for dv in ws.data_validations.dataValidation),
            'cf': sorted('%s:%s' % (cf.sqref, [r.formula for r in cf.rules]) for cf in ws.conditional_formatting),
            'prot': bool(ws.protection.sheet), 'area': str(ws.print_area),
            'papel': ws.page_setup.paperSize, 'pie': ws.oddFooter.center.text,
        }
    return fuera


def diferencias(a, b, fichero):
    out = []
    if a['_props'] != b['_props']:
        out.append('%s: propiedades' % fichero)
    for hoja in sorted((set(a) | set(b)) - {'_props'}):
        if hoja not in a or hoja not in b:
            out.append('%s:%s: hoja solo en una pasada' % (fichero, hoja))
            continue
        for k in ('merges', 'dv', 'cf', 'prot', 'area', 'papel', 'pie'):
            if a[hoja][k] != b[hoja][k]:
                out.append('%s:%s: cambia %s' % (fichero, hoja, k))
        ca, cb = a[hoja]['celdas'], b[hoja]['celdas']
        for coord in sorted(set(ca) | set(cb)):
            if ca.get(coord) != cb.get(coord):
                out.append('%s:%s!%s: %s → %s' % (fichero, hoja, coord, ca.get(coord), cb.get(coord)))
    return out


# ==========================================================================
# inject_cache y verificación de la caché
# ==========================================================================
def inject_cache(carpeta, log=print):
    fuera = []
    for fname_es in mapas.LIBROS_ES:
        termica()
        p = os.path.join(carpeta, mapas.FICHEROS[fname_es])
        r = subprocess.run([sys.executable, '-W', 'ignore', INJECT, p], stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, universal_newlines=True)
        linea = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ''
        log('    ' + linea)
        fuera.append({'fichero': mapas.FICHEROS[fname_es], 'salida': linea, 'exit': r.returncode,
                      'stderr': r.stderr[-400:] if r.returncode else ''})
    return fuera


def verificar_cache(carpeta):
    out = OrderedDict()
    for fname_es in mapas.LIBROS_ES:
        p = os.path.join(carpeta, mapas.FICHEROS[fname_es])
        wf, wv = openpyxl.load_workbook(p), openpyxl.load_workbook(p, data_only=True)
        n = con_valor = 0
        for ws in wf.worksheets:
            for c in ws._cells.values():
                if c.data_type == 'f':
                    n += 1
                    if wv[ws.title][c.coordinate].value is not None:
                        con_valor += 1
        out[mapas.FICHEROS[fname_es]] = (n, con_valor)
    return out


def carpeta_dryrun(arg):
    if arg:
        return os.path.abspath(arg)
    s = os.environ.get('CLAUDE_SCRATCHPAD')
    if s:
        return os.path.join(os.path.abspath(s), 'haccp-dryrun')
    return os.path.join(REPO, '.work', mapas.SLUG, 'haccp-dryrun')


def main():
    ap = argparse.ArgumentParser(description='HACCP Food Safety Kit Pro (EN): montaje de los 21 xlsx')
    ap.add_argument('--dry-run', action='store_true', help='escribe en el scratchpad (o --salida), no en dl/')
    ap.add_argument('--salida', default=None, help='carpeta del dry-run')
    ap.add_argument('--mes', default=None, help='mes de la línea de versión D21 (por defecto, el actual)')
    ap.add_argument('--json', default=None, help='informe JSON')
    ap.add_argument('--idempotencia', action='store_true', help='2.ª construcción en un clon y 0 diferencias')
    ap.add_argument('--parcial', action='store_true', help='(solo --dry-run) deja en ES lo que no tenga traducción')
    ap.add_argument('--sin-cache', action='store_true', help='(depuración) no corre inject_cache')
    args = ap.parse_args()
    if args.parcial and not args.dry_run:
        raise SystemExit('--parcial solo vale con --dry-run')

    mes = args.mes or mes_por_defecto()
    if mes not in MESES:
        raise SystemExit('--mes debe ser un mes en inglés: %s' % ', '.join(MESES))
    carpeta = carpeta_dryrun(args.salida) if args.dry_run else DESTINO_REAL
    if os.path.abspath(carpeta) == os.path.abspath(ORIGEN):
        raise SystemExit('ABORTADO: la salida no puede ser la carpeta ES')

    t0 = time.time()
    try:
        datos = cargar_datos(args.parcial)
        print('== 1/3 · montaje de los 21 libros → %s (mes %s)%s' % (
            carpeta, mes, ' · PARCIAL: %d cadenas sin traducción' % len(datos['faltan']) if args.parcial else ''),
            flush=True)
        informe = construir(carpeta, datos, mes)
    except Aborta as e:
        raise SystemExit('ABORTADO: %s' % e)
    sobran = sorted(set(os.listdir(carpeta)) - set(mapas.FICHEROS.values()))
    if sobran:
        print('  aviso: ficheros ajenos en la salida: %s' % sobran)

    idem = {'ejecutada': False}
    if args.idempotencia:
        print('== 2/3 · idempotencia: 2.ª construcción en un clon', flush=True)
        clon = tempfile.mkdtemp(prefix='haccp-idem-')
        construir(clon, datos, mes, log=lambda *_: None)
        difs = []
        for n in mapas.FICHEROS.values():
            difs += diferencias(digest(os.path.join(carpeta, n)), digest(os.path.join(clon, n)), n)
        shutil.rmtree(clon)
        idem = {'ejecutada': True, 'diferencias': len(difs), 'detalle': difs[:30]}
        print('  diferencias 1.ª vs 2.ª construcción: %d' % len(difs), flush=True)
        for d in difs[:10]:
            print('    ' + d)

    print('== 3/3 · inject_cache (AL FINAL, sobre los 21)', flush=True)
    cache = [] if args.sin_cache else inject_cache(carpeta)
    ver = verificar_cache(carpeta) if cache else {}
    for f, (n, v) in ver.items():
        print('    data_only %-44s %4d fórmulas · %4d con valor' % (f, n, v))

    fallos = []
    if idem.get('diferencias'):
        fallos.append('idempotencia: %d diferencias' % idem['diferencias'])
    fallos += ['inject_cache %s: exit %s %s' % (c['fichero'], c['exit'], c['stderr'][-200:]) for c in cache if c['exit']]
    fallos += ['inject_cache %s: %s' % (c['fichero'], c['salida']) for c in cache
               if c['exit'] == 0 and 'fallos_pycel=0' not in c['salida']]
    salida = OrderedDict([('producto', mapas.SLUG), ('version', VERSION),
                          ('fecha', datetime.datetime.now().isoformat(timespec='seconds')),
                          ('modo', 'dry-run' if args.dry_run else 'real'), ('carpeta', carpeta), ('mes', mes),
                          ('libros', informe), ('idempotencia', idem), ('inject_cache', cache),
                          ('cache_data_only', ver), ('fallos', fallos),
                          ('segundos', round(time.time() - t0, 1))])
    if args.json:
        with open(args.json, 'w', encoding='utf-8') as fh:
            json.dump(salida, fh, ensure_ascii=False, indent=1, default=str)
        print('informe → %s' % args.json)
    if fallos:
        print('\nFALLOS:\n  ' + '\n  '.join(fallos))
        sys.exit(1)
    print('\nOK: 21 xlsx en %s (%.0f s)' % (carpeta, time.time() - t0))


if __name__ == '__main__':
    main()
