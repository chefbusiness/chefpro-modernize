#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
aplicar_en.py — Recipe Costing Kit Pro (EN) · montaje de los 14 xlsx desde el ES v2.1 publicado.

SPEC que manda: `SPEC.md` (§2.1 orden, §2.2 hojas, §2.3 claves, §2.4 literales, §2.5 mercado,
D5-D14, excepciones E1-E5). Sesión Claude Code, 24-sep-2026. El texto de producto sale de
`textos_en/` (subagentes Anthropic, regla 1bis): aquí no se redacta nada ni se llama a bridge.py.

    python3 aplicar_en.py --salida <scratchpad>/rck-dryrun           # DRY-RUN (por defecto)
    RECIPE_COSTING_KIT_APPLY=1 python3 aplicar_en.py --real --pdf <ruta del PDF EN>

Dry-run: escribe los 14 xlsx EN en `--salida` (por defecto `$CLAUDE_SCRATCHPAD/rck-dryrun`, o
`.work/recipe-costing-kit/rck-dryrun` del repo). `--real` escribe en
`astro-site/public/dl/recipe-costing-kit/` y exige RECIPE_COSTING_KIT_APPLY=1 (lo lanza el
orquestador tras la revisión). Los ficheros ES de `dl/kit-escandallos/` NUNCA se escriben.

Orden (SPEC §2.1), por libro, siempre desde una copia limpia del ES publicado (→ idempotente):
   1. copia del xlsx ES v2.1;
   2. renombrado de hojas (mapas.HOJAS) reescribiendo TODAS las referencias: fórmulas, DV, CF,
      XML de los gráficos (a nivel de ZIP, paso 12), áreas y títulos de impresión (por título);
   3. literales de fórmula (§2.4: «revisa merma», «ALERTA», «Útil»…), en celdas y en CF;
   4. claves-dato (§2.3) y DV de listas literales: unidades (E5, lista D7), tipos del 12, motivos;
   5. `Conversions` regenerada por mapas.conversions() (E1) y rango $A$5:$B${4+n+30} en los
      VLOOKUP y en el área de impresión (E2);
   6. textos (textos_en/ + textos con cifra derivada de mercado_en.json + notas existentes de
      instrucciones_extra_en.json + textos_en_por_celda.json), cabeceras/pies, mensajes de DV y
      títulos;
   7. formatos: sin símbolo de moneda (D5), fechas a numFmtId 14 (D13, E4), US Letter;
   8. mercado (mercado_en.json): fichas, precios de carta, Bottle Sizes en ml (E3), 06, 08, 09,
      10, 11, 12, 13 y BONUS;
   9. bloques extra de Instructions (instrucciones_extra_en.json) antes del pie de marca;
  10. metadatos (docProps EN) y línea de versión D14 con el mes de publicación;
  11. guardado con el nombre de fichero EN (mapas.FICHEROS);
  12. gráficos de 09 y 11: el XML original del ES con referencias y título EN (openpyxl pierde
      su <c:style>);
  13. PDF del bono (copia) e `inject_cache.py` AL FINAL sobre los 14.
Después, comprobación de idempotencia: 2.ª construcción en un clon y 0 diferencias.

Térmica: todo en SERIE; `istats` antes de cada libro y de cada inject_cache (espera ≥ 62 °C).
"""
import argparse
import copy
import datetime
import glob
import html
import json
import logging
import os
import re
import shutil
import subprocess
import sys
import time
import zipfile
from collections import OrderedDict
from xml.sax.saxutils import escape as xml_escape

AQUI = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(AQUI)
REPO = os.path.dirname(os.path.dirname(SCRIPTS))
sys.path.insert(0, AQUI)

import openpyxl                                              # noqa: E402
from openpyxl.styles import Font, PatternFill, Protection   # noqa: E402

import mapas                                                 # noqa: E402
import extraer_textos                                        # noqa: E402

logging.disable(logging.CRITICAL)

ORIGEN = os.path.join(REPO, 'astro-site', 'public', 'dl', 'kit-escandallos')
DESTINO_REAL = os.path.join(REPO, 'astro-site', 'public', 'dl', 'recipe-costing-kit')
INJECT = os.path.join(SCRIPTS, 'inject_cache.py')

VERSION = '2.1'
SUBJECT = 'Recipe Costing Kit Pro · v2.1'
DESCRIPTION = 'aichef.pro/en/digital-products/recipe-costing-kit'
CREATOR = 'AI Chef Pro'
MESES = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
         'September', 'October', 'November', 'December']
VERDE = 'E8F5E9'
FMT_FECHA = 'mm-dd-yy'                     # numFmtId 14 = fecha corta del sistema (D13)
FMT_CONV_B = 'General'                     # Conversions!B: factores exactos sin «0.001» engañoso
PDF_EN = mapas.FICHEROS['BONUS-guia-food-cost-30-dias.pdf']
INVARIABLES = {'OK', 'N/A', 'AI Chef Pro'}
RX_VERSION_ES = re.compile(r'^Versi[óo]n \d+\.\d+ · ')
RX_VERSION_EN = re.compile(r'^Version \d+\.\d+ · ')

UNIDADES_ES_DV = mapas.dv_lista(mapas.UNIDADES.keys())       # "kg,g,L,ml,cl,ud,docena,…"
DV12_ES = mapas.dv_lista(mapas.DV12.keys())
MOTIVOS_ES = mapas.dv_lista(mapas.MOTIVOS.keys())
DV_CHECKLIST = mapas.dv_lista(mapas.DV_CHECKLIST_06.split(','))

HOJA_INSTR_ES = 'Instrucciones'
HOJA_INSTR_EN = mapas.hoja_en(HOJA_INSTR_ES)


class Aborta(Exception):
    pass


# ==========================================================================
# Térmica
# ==========================================================================
def termica(umbral=62, reanuda=60):
    """Espera mientras la CPU esté a ≥ umbral °C (regla térmica del Mac). Sin istats, no hace nada."""
    def leer():
        try:
            out = subprocess.run(['istats', 'cpu', 'temp', '--value-only'], capture_output=True,
                                 text=True, timeout=20).stdout
            return float(re.findall(r'[\d.]+', out)[0])
        except Exception:
            return None
    t = leer()
    if t is None or t < umbral:
        return t
    while t is not None and t >= reanuda:
        print('  [térmica] CPU %.1f °C: espero 60 s' % t, flush=True)
        time.sleep(60)
        t = leer()
    return t


# ==========================================================================
# Datos
# ==========================================================================
def cargar_datos():
    te = json.load(open(os.path.join(AQUI, 'textos_es.json'), encoding='utf-8'))
    tr = OrderedDict()
    for p in sorted(glob.glob(os.path.join(AQUI, 'textos_en', '*.json'))):
        for x in json.load(open(p, encoding='utf-8')):
            if x['es'] in tr and tr[x['es']] != x['en']:
                raise Aborta('traducción contradictoria para %r (%s)' % (x['es'][:60], p))
            tr[x['es']] = x['en']
    mercado = json.load(open(os.path.join(AQUI, 'mercado_en.json'), encoding='utf-8'))
    for x in mercado['textos_cifra_derivada']:          # M5: mandan sobre la traducción
        tr[x['es']] = x['en']
    extra = json.load(open(os.path.join(AQUI, 'instrucciones_extra_en.json'), encoding='utf-8'))
    notas = {}
    for n in extra['notas_existentes']:
        for f in n['ficheros']:
            notas[(f, n['hoja_en'], n['celda'])] = (n['es'], n['en'])
    # Cadenas ES con dos sentidos según la celda (textos_en_por_celda.json): mandan en su celda.
    for n in json.load(open(os.path.join(AQUI, 'textos_en_por_celda.json'), encoding='utf-8')):
        notas[(n['fichero_en'], n['hoja_en'], n['celda'])] = (n['es'], n['en'])
    faltan = [c['es'] for c in te['cadenas'] if c['es'] not in tr]
    if faltan:
        raise Aborta('%d cadenas de textos_es.json sin traducción: %r' % (len(faltan), faltan[:5]))
    for c in te['cadenas']:
        if c.get('en_mapa') and tr[c['es']] != c['en_mapa']:
            raise Aborta('mapa ≠ traducción para %r' % c['es'])
    conv = mapas.conversions()
    return {'te': te, 'tr': tr, 'mercado': mercado, 'extra': extra, 'notas': notas,
            'conv': conv, 'n': len(conv), 'fin_conv': mapas.ultima_fila_rango(len(conv))}


def mes_por_defecto():
    return MESES[datetime.date.today().month - 1]


def linea_version(mes):
    return 'Version %s · %s %d · %s · info@aichef.pro' % (VERSION, mes, datetime.date.today().year,
                                                          DESCRIPTION)


# ==========================================================================
# Fórmulas: hojas, literales y rango de Conversions
# ==========================================================================
RX_STR = re.compile(r'"(?:[^"]|"")*"')
RX_REF = re.compile(r"(?:'((?:[^']|'')+)'|([^\W\d][\w.]*))!")
RX_CONV_EN = re.compile(r'(Conversions!\$A\$5:\$B\$)(\d+)')


class Transformador:
    """Reescribe una fórmula ES a EN: referencias de hoja (fuera de literales), literales
    de §2.4 (dentro de literales) y el final del rango de Conversions (E2)."""

    def __init__(self, mapa_hojas, fin_conv):
        self.mapa = mapa_hojas
        self.en = set(mapa_hojas.values())
        self.fin = fin_conv
        self.hojas_citadas = 0
        self.literales = 0

    def refs(self, s):
        def rep(m):
            nombre = (m.group(1) if m.group(1) is not None else m.group(2)).replace("''", "'")
            if nombre in self.mapa:
                self.hojas_citadas += 1
                return mapas.ref_hoja(self.mapa[nombre]) + '!'
            if nombre in self.en:
                return m.group(0)
            raise Aborta('hoja desconocida en fórmula: %r en %r' % (nombre, s[:80]))
        s = RX_REF.sub(rep, s)
        return RX_CONV_EN.sub(lambda m: m.group(1) + str(self.fin), s)

    def formula(self, f):
        out, pos = [], 0
        for m in RX_STR.finditer(f):
            out.append(self.refs(f[pos:m.start()]))
            lit = m.group(0)[1:-1].replace('""', '"')
            if lit in mapas.LITERALES:
                lit = mapas.LITERALES[lit]
                self.literales += 1
            out.append('"' + lit.replace('"', '""') + '"')
            pos = m.end()
        out.append(self.refs(f[pos:]))
        return ''.join(out)


def formato_en(fmt):
    """number_format EN: sin «€» (D5) y fechas a la corta del sistema (D13)."""
    if not isinstance(fmt, str):
        return fmt
    if fmt.lower() in ('dd/mm/yyyy', 'dd/mm/yy', 'd/m/yyyy'):
        return FMT_FECHA
    if '€' in fmt:
        f = re.sub(r'\[\$€[^\]]*\]', '', fmt)
        f = f.replace('"€"', '').replace('€', '')
        return re.sub(r'\s+', ' ', f).strip()
    return fmt


# ==========================================================================
# Estructura ES (antes de tocar nada)
# ==========================================================================
def detectar_fichas(wb):
    """Hojas con rejilla de escandallo: filas de datos (DV de unidades en C) y filas de resultado."""
    fichas = OrderedDict()
    for ws in wb.worksheets:
        d = None
        for dv in ws.data_validations.dataValidation:
            if dv.formula1 == UNIDADES_ES_DV:
                for rng in dv.sqref.ranges:
                    if rng.min_col == 3:
                        d = (rng.min_row, rng.max_row)
        if not d:
            continue
        pos = {}
        for r in range(d[1] + 1, ws.max_row + 1):
            a = ws.cell(r, 1).value
            if not isinstance(a, str):
                continue
            if a == 'COSTE TOTAL INGREDIENTES':
                pos['tot'] = r
            elif a in ('Coste elaboración (%)', 'Merma y hielo (%)'):
                pos['q'] = r
            elif a.startswith('Nº de raciones') or a.startswith('Rendimiento'):
                pos['rac'] = r
            elif a.startswith('Food Cost objetivo (%)'):
                pos['fc'] = r
            elif a == 'Tipo de IVA (%)':
                pos['iva'] = r
            elif a == 'PVP actual en carta (sin IVA)':
                pos['pvp'] = r
        falta = {'tot', 'q', 'rac', 'fc', 'iva', 'pvp'} - set(pos)
        if falta:
            raise Aborta('%s: no encuentro las filas %s de la ficha' % (ws.title, sorted(falta)))
        pos.update(d0=d[0], d1=d[1])
        fichas[ws.title] = pos
    return fichas


def fila_por_rotulo(ws, col, prefijo, obligatoria=True):
    for r in range(1, ws.max_row + 1):
        v = ws.cell(r, col).value
        if isinstance(v, str) and v.startswith(prefijo):
            return r
    if obligatoria:
        raise Aborta('%s: no encuentro el rótulo «%s»' % (ws.title, prefijo))
    return None


def posiciones_es(wb, corto):
    """Filas de resumen que hay que localizar por su rótulo ES antes de traducir."""
    p = {}
    if corto == '02':
        ws = wb['Resumen']
        p['02'] = {'fc': fila_por_rotulo(ws, 2, 'Food Cost objetivo (%)'),
                   'iva': fila_por_rotulo(ws, 2, 'Tipo de IVA (%)')}
    if corto == '03':
        ws = wb['Resumen Menú']
        p['03'] = {'pan': fila_por_rotulo(ws, 2, 'Pan (por comensal)'),
                   'bebida': fila_por_rotulo(ws, 2, 'Bebida ('),
                   'cafe': fila_por_rotulo(ws, 2, 'Café'),
                   'fc': fila_por_rotulo(ws, 2, 'Food Cost objetivo (%)'),
                   'iva': fila_por_rotulo(ws, 2, 'Tipo de IVA (%)')}
    return p


# ==========================================================================
# Escritura protegida (nunca se pisa una fórmula)
# ==========================================================================
CONTADOR = {'mercado': 0}


def escribir(ws, coord, valor):
    c = ws[coord]
    if c.data_type == 'f' or (isinstance(c.value, str) and c.value.startswith('=')):
        raise Aborta('%s!%s es una fórmula (%r): el mercado no la pisa' % (ws.title, coord, c.value))
    c.value = valor
    CONTADOR['mercado'] += 1


# ==========================================================================
# Pasos
# ==========================================================================
def renombrar(wb):
    mapa = OrderedDict((ws.title, mapas.hoja_en(ws.title)) for ws in wb.worksheets)
    for ws in wb.worksheets:
        ws.title = mapa[ws.title]
    if wb.sheetnames != list(mapa.values()):
        raise Aborta('renombrado: %r ≠ %r' % (wb.sheetnames, list(mapa.values())))
    return mapa


def reescribir_formulas(wb, T, rep):
    n = 0
    for ws in wb.worksheets:
        for c in list(ws._cells.values()):
            if c.data_type == 'f' and isinstance(c.value, str):
                nuevo = '=' + T.formula(c.value[1:]) if c.value.startswith('=') else T.formula(c.value)
                if nuevo != c.value:
                    c.value = nuevo
                    n += 1
    rep['formulas_reescritas'] = n


def reescribir_dv_cf(wb, T, traducir, rep):
    dv_uni = dv_otras = cf_n = 0
    for ws in wb.worksheets:
        for dv in ws.data_validations.dataValidation:
            f1 = dv.formula1
            if f1 == UNIDADES_ES_DV:
                dv.formula1 = mapas.DV_UNIDADES_EN          # E5: se sustituye, no se mapea
                dv_uni += 1
            elif f1 == DV12_ES:
                dv.formula1 = mapas.DV12_EN
                dv_otras += 1
            elif f1 == MOTIVOS_ES:
                dv.formula1 = mapas.DV_MOTIVOS_EN
                dv_otras += 1
            elif f1 == DV_CHECKLIST:
                pass
            elif f1 and not f1.startswith('"'):
                dv.formula1 = T.refs(f1)
                dv_otras += 1
            else:
                raise Aborta('%s: DV de lista literal desconocida %r' % (ws.title, f1))
            if dv.formula2:
                dv.formula2 = T.refs(dv.formula2)
            for attr in ('error', 'errorTitle', 'prompt', 'promptTitle'):
                v = getattr(dv, attr)
                if v:
                    setattr(dv, attr, traducir(v, '%s DV %s %s' % (ws.title, dv.sqref, attr)))
        for cf in ws.conditional_formatting:
            for regla in cf.rules:
                if regla.formula:
                    regla.formula = [T.formula(x) for x in regla.formula]
                    cf_n += 1
    rep.update(dv_unidades=dv_uni, dv_otras=dv_otras, cf_reglas=cf_n)


def regenerar_conversions(ws, datos, rep):
    """E1: tabla generada por mapas.conversions(); E2: área de impresión con 30 filas libres."""
    filas, n, fin = datos['conv'], datos['n'], datos['fin_conv']
    estilos = [copy.copy(ws.cell(mapas.FILA0, c)._style) for c in (1, 2, 3)]
    for r in range(mapas.FILA0, max(ws.max_row, fin) + 1):
        for c in (1, 2, 3):
            ws.cell(r, c).value = None
    ancho = 46
    for f in filas:
        r = f['fila']
        celdas = (ws.cell(r, 1), ws.cell(r, 2), ws.cell(r, 3))
        for cel, st in zip(celdas, estilos):
            cel._style = copy.copy(st)
        celdas[0].value = f['clave']
        celdas[1].value = f['valor']
        celdas[2].value = f['nota']
        celdas[1].number_format = FMT_CONV_B
        if f['tamano']:
            celdas[1].fill = PatternFill('solid', fgColor=VERDE)
            celdas[1].protection = Protection(locked=False)
        ancho = max(ancho, min(90, len(f['nota']) + 2))
    ws.column_dimensions['C'].width = ancho
    ws.print_area = 'A1:J%d' % fin
    tam = {f['origen']: 'B%d' % f['fila'] for f in filas if f['tamano']}
    rep.update(conversions_n=n, conversions_fin=fin, celdas_tamano=tam)
    return tam


def traducir_libro(wb, fname_en, mapa, datos, mes, rep):
    """Textos de celda (no fórmula), cabeceras/pies y línea de versión."""
    tr, notas = datos['tr'], datos['notas']
    inv = {v: k for k, v in mapa.items()}
    faltan = rep.setdefault('faltan', [])
    n = 0

    def traducir(v, lugar):
        if v in tr:
            return tr[v]
        if v in INVARIABLES or not any(ch.isalpha() for ch in v):
            return v
        faltan.append('%s: %r' % (lugar, v[:90]))
        return v

    for ws in wb.worksheets:
        hoja_es = inv[ws.title]
        for c in list(ws._cells.values()):
            v = c.value
            if not isinstance(v, str) or c.data_type == 'f':
                continue
            col = c.column_letter
            if hoja_es == 'Conversiones' and c.row >= mapas.FILA0 and col in 'ABC':
                continue                                   # E1: regenerada aparte
            if hoja_es == 'Lista de precios' and c.row >= 10:
                continue                                   # R2-10: el 13 EN se genera
            if RX_VERSION_ES.match(v):
                c.value = linea_version(mes)
                n += 1
                continue
            nota = notas.get((fname_en, ws.title, c.coordinate))
            if nota and v == nota[0]:
                c.value = nota[1]
                n += 1
                continue
            nuevo = traducir(v, '%s!%s' % (ws.title, c.coordinate))
            if nuevo != v:
                c.value = nuevo
                n += 1
        for parte in ('oddHeader', 'oddFooter', 'evenHeader', 'evenFooter', 'firstHeader',
                      'firstFooter'):
            hf = getattr(ws, parte)
            for pos in ('left', 'center', 'right'):
                t = getattr(hf, pos).text
                if t:
                    getattr(hf, pos).text = traducir(t, '%s %s.%s' % (ws.title, parte, pos))
    rep['textos_traducidos'] = n
    return traducir


def formatos_y_papel(wb, rep):
    """D5 (sin moneda), D13 (numFmtId 14) y US Letter."""
    # 1) Las entradas propias con «€» se corrigen en su sitio: ninguna celda (tampoco las vacías
    #    con estilo) conserva el símbolo y styles.xml sale limpio.
    nf = wb._number_formats
    for i, f in enumerate(list(nf)):
        if '€' in f:
            list.__setitem__(nf, i, formato_en(f))
    _indice_formatos(nf)
    # 2) Toda celda de fecha (dd/mm/yyyy o un «mm-dd-yy» propio) pasa a la builtin 14.
    fechas = cambiados = 0
    for ws in wb.worksheets:
        for c in list(ws._cells.values()):
            f = c.number_format
            if isinstance(f, str) and (f == FMT_FECHA or f.lower() in ('dd/mm/yyyy', 'dd/mm/yy')):
                c.number_format = FMT_FECHA            # builtin 14
                fechas += 1
            else:
                g = formato_en(f)
                if g != f:
                    c.number_format = g
                    cambiados += 1
        ws.page_setup.paperSize = ws.PAPERSIZE_LETTER
    # 3) Las entradas dd/mm que ya no usa ninguna celda se neutralizan (fecha corta US), para
    #    que styles.xml no lleve formatos del ES.
    for i, f in enumerate(list(nf)):
        if f.lower() in ('dd/mm/yyyy', 'dd/mm/yy'):
            libre = 'm/d/yyyy'
            while libre in list(nf):
                libre += ';@'
            list.__setitem__(nf, i, libre)
    _indice_formatos(nf)
    rep.update(celdas_fecha=fechas, formatos_cambiados=cambiados)


def _indice_formatos(nf):
    if len(set(nf)) != len(nf):
        # IndexedList reconstruye su índice sin contar repetidos: con dos entradas iguales los
        # numFmtId de las celdas quedarían desplazados.
        raise Aborta('formatos propios repetidos: %r' % list(nf))
    nf._dict = {v: i for i, v in enumerate(nf)}
    nf.clean = True


# ---------------------------------------------------------------- mercado
def mercado_fichas(wb, corto, fichas_es, mapa, M, rep):
    hechas = 0
    for rec in [r for r in M['recetas'] if r['libro'] == corto]:
        ws = wb[rec['hoja_en']]
        lay = fichas_es[rec['hoja_es']]
        filas = {f['fila']: f for f in rec['filas']}
        for r in range(lay['d0'], lay['d1'] + 1):
            a = ws.cell(r, 1).value
            if a not in (None, '') and r not in filas:
                raise Aborta('%s fila %d («%s»): fila de ejemplo sin fila EN en mercado_en.json'
                             % (rec['hoja_en'], r, a))
        vinculadas = []
        for r, f in filas.items():
            if not (lay['d0'] <= r <= lay['d1']):
                raise Aborta('%s fila %d fuera de la rejilla' % (rec['hoja_en'], r))
            escribir(ws, 'A%d' % r, f['nombre_en'])
            escribir(ws, 'B%d' % r, f['categoria_en'])
            escribir(ws, 'C%d' % r, f['ud_compra'])
            d = ws['D%d' % r]
            if d.data_type == 'f':
                vinculadas.append((r, d.value, f['precio']))      # 04: enlazada a Bottle Sizes
            else:
                escribir(ws, 'D%d' % r, f['precio'])
            escribir(ws, 'E%d' % r, f['cantidad'])
            escribir(ws, 'F%d' % r, f['ud_uso'])
            escribir(ws, 'H%d' % r, f['merma'])
        escribir(ws, 'I%d' % lay['q'], rec['q_factor'])
        escribir(ws, 'I%d' % lay['rac'], rec['raciones'])
        if ws['I%d' % lay['fc']].data_type != 'f':
            escribir(ws, 'I%d' % lay['fc'], rec['target_fc'])
        escribir(ws, 'I%d' % lay['iva'], 0)                        # D6: 0 % por defecto
        escribir(ws, 'I%d' % lay['pvp'], rec['precio_carta_ref'])  # D10 / R2T-22
        if rec.get('titulo_en'):
            escribir(ws, 'A1', rec['titulo_en'])
        hechas += 1
        if vinculadas:
            rep.setdefault('precios_vinculados', []).extend(
                '%s!D%d = %s' % (rec['hoja_en'], r, v) for r, v, _ in vinculadas)
    rep['fichas_mercado'] = hechas
    # D6: «Tax rate (%)» a 0 en TODAS las fichas del libro, también en las pestañas sin receta de ejemplo (02:
    # «6. Course»…«9. Course» conservaban el 10 % del ES). Revisión R1 EN, CHEF-01.
    for hoja_es, lay in fichas_es.items():
        ws = wb[mapa[hoja_es]]
        if ws['I%d' % lay['iva']].data_type != 'f' and ws['I%d' % lay['iva']].value != 0:
            escribir(ws, 'I%d' % lay['iva'], 0)
            rep['impuesto_a_0_sin_receta'] = rep.get('impuesto_a_0_sin_receta', 0) + 1


def nota_resumen(ws, nota, estilo_de=None):
    """CHEF-03: nota del Summary con el precio del menú (celda vacía en el ES)."""
    c = ws[nota['celda']]
    if c.value not in (None, ''):
        raise Aborta('%s!%s no está vacía: %r' % (ws.title, nota['celda'], c.value))
    escribir(ws, nota['celda'], nota['texto'])
    if estilo_de:
        c._style = copy.copy(ws[estilo_de]._style)
    else:
        c.font = Font(italic=True, size=10, color='FF555555')


def mercado_resumenes(wb, corto, pos, M, rep):
    if corto == '02':
        ws, p, m = wb['Summary'], pos['02'], M['menu_02']
        escribir(ws, 'C%d' % p['fc'], m['target_fc'])
        escribir(ws, 'C%d' % p['iva'], 0)
        nota_resumen(ws, m['nota_resumen'], 'B21')
    if corto == '03':
        ws, p, m = wb['Menu Summary'], pos['03'], M['menu_03']
        ex = m['extras']
        for clave, fila in (('bread_and_butter', p['pan']), ('drink', p['bebida']),
                            ('coffee', p['cafe'])):
            escribir(ws, 'B%d' % fila, ex[clave]['rotulo'])
            escribir(ws, 'C%d' % fila, ex[clave]['valor'])
        escribir(ws, 'C%d' % p['fc'], m['target_fc'])
        escribir(ws, 'C%d' % p['iva'], 0)
        nota_resumen(ws, m['nota_resumen'])


RX_COORD_CLAVE = re.compile(r'^([A-Z]{1,2}\d+)_')


def mercado_04(wb, M, rep):
    ws = wb['Bottle Sizes']
    for r in range(5, 17):                                     # E3: ×1000 sobre ml
        ws['D%d' % r].value = '=IFERROR(ROUND(C%d*1000/B%d,4),"")' % (r, r)
        for col in 'ABCE':
            escribir(ws, '%s%d' % (col, r), None)
    for b in M['bottle_sizes']:
        r = b['fila']
        escribir(ws, 'A%d' % r, b['producto'])
        escribir(ws, 'B%d' % r, b['ml'])
        escribir(ws, 'C%d' % r, b['precio_botella'])
        escribir(ws, 'E%d' % r, b['donde'])
    rep['bottle_sizes'] = len(M['bottle_sizes'])


def mercado_06(wb, M, rep):
    ws = wb['Event Quote']
    c6 = M['catering_06']
    for k, v in c6.items():
        m = RX_COORD_CLAVE.match(k)
        if not m or isinstance(v, (dict, str)):
            continue
        escribir(ws, m.group(1), v)
    escribir(ws, 'B25', c6['C25_rotulo'])


def mercado_08(wb, M, rep):
    ws = wb['Break-Even']
    be = M['break_even_08']
    for l in be['lineas']:
        escribir(ws, 'A%d' % l['fila'], l['rotulo'])
        escribir(ws, 'B%d' % l['fila'], l['valor'])
    for i, x in enumerate(be['mix']):
        escribir(ws, 'E%d' % (16 + i), x)
    escribir(ws, 'B25', be['B25_impuesto'])


def mercado_09(wb, M, rep):
    ws = wb['Weekly Waste Log']
    w = M['waste_09']
    for r in range(5, 21):
        escribir(ws, 'E%d' % r, None)
        escribir(ws, 'F%d' % r, None)
    for f in w['familias_con_ejemplo']:
        if ws['A%d' % f['fila']].value != f['familia']:
            raise Aborta('09 fila %d: %r ≠ %r' % (f['fila'], ws['A%d' % f['fila']].value, f['familia']))
        escribir(ws, 'E%d' % f['fila'], f['compra'])
        escribir(ws, 'F%d' % f['fila'], f['desperdicio'])
    ev = wb['Trend']
    escribir(ev, 'B3', w['objetivo_global'])
    for r in range(7, 18):
        escribir(ev, 'B%d' % r, None)
        escribir(ev, 'C%d' % r, None)
    for s in w['semanas']:
        escribir(ev, 'B%d' % s['fila'], s['compra'])
        escribir(ev, 'C%d' % s['fila'], s['desperdicio'])


def mercado_10(wb, M, rep):
    ws = wb['Menu Price Calculator']
    c = M['calculadora_10']
    escribir(ws, 'C4', c['C4_coste_racion'])
    escribir(ws, 'C5', c['C5_impuesto'])
    for f in c['filas']:
        r = f['fila']
        escribir(ws, 'B%d' % r, f['rotulo'])
        escribir(ws, 'C%d' % r, f['fc_min'])
        escribir(ws, 'D%d' % r, f['fc_max'])
        escribir(ws, 'F%d' % r, f['comision'])


def mercado_11(wb, M, rep):
    ws = wb['Dashboard']
    d = M['dashboard_11']
    escribir(ws, 'D3', d['D3_anio'])
    escribir(ws, 'D4', d['D4_objetivo'])
    for r in range(7, 19):
        for col in 'CDEG':
            escribir(ws, '%s%d' % (col, r), None)
    for m in d['meses']:
        r = m['fila']
        escribir(ws, 'C%d' % r, m['stock_ini'])
        escribir(ws, 'D%d' % r, m['compras'])
        escribir(ws, 'E%d' % r, m['stock_fin'])
        escribir(ws, 'G%d' % r, m['ventas'])


def mercado_12(wb, M, rep):
    d = M['libro12']['despiece']
    ws = wb['Butcher Yield Test']
    escribir(ws, 'A1', d['titulo'])
    escribir(ws, 'C5', d['C5_producto'])
    escribir(ws, 'C8', d['C8_peso_ap_lb'])
    escribir(ws, 'C9', d['C9_precio_lb'])
    escribir(ws, 'C11', d['C11_unidades_porcion'])
    for r in range(14, 26):
        for col in 'ABCD':
            escribir(ws, '%s%d' % (col, r), None)
    for comp in d['componentes']:
        r = comp['fila']
        escribir(ws, 'A%d' % r, comp['pieza'])
        escribir(ws, 'B%d' % r, comp['tipo'])
        escribir(ws, 'C%d' % r, comp['peso_lb'])
        escribir(ws, 'D%d' % r, comp['valor_lb'])
    escribir(ws, 'C36', d['C36_porcion_oz'])
    ws['C36'].number_format = '#,##0.00'          # 5.5 oz no se ve «6» (revisión R1 EN, CHEF-14)
    c = M['libro12']['coccion']
    ws = wb['Cooking Loss Test']
    escribir(ws, 'A1', c['titulo'])
    escribir(ws, 'C5', c['C5_elaboracion'])
    escribir(ws, 'C7', c['C7_peso_crudo_lb'])
    escribir(ws, 'C8', c['C8_precio_lb'])
    escribir(ws, 'C9', c['C9_peso_cocinado_lb'])
    escribir(ws, 'C10', c['C10_merma_despiece'])
    escribir(ws, 'C11', c['C11_unidades_porcion'])
    escribir(ws, 'C12', c['C12_porcion_cocinada_oz'])
    # La porción cocinada en oz lleva 2 decimales (4.44 oz): el «#,##0» de los gramos la
    # enseñaría como «4». Solo formato de una celda de entrada, no estructura.
    ws['C12'].number_format = '#,##0.00'


def mercado_13(wb, M, rep):
    ws = wb['Price List']
    l13 = M['libro13']
    escribir(ws, 'B5', l13['umbral_alerta'])
    filas = l13['filas']
    ultima = 154
    if 10 + len(filas) + l13['filas_vacias'] - 1 > ultima:
        raise Aborta('13: %d ingredientes + %d vacías no caben en A10:M%d'
                     % (len(filas), l13['filas_vacias'], ultima))
    entradas = 'ABCDEFGILM'
    for r in range(10, ultima + 1):
        for col in entradas:
            escribir(ws, '%s%d' % (col, r), None)
    for i, f in enumerate(filas):
        r = 10 + i
        escribir(ws, 'A%d' % r, f['ingrediente'])
        escribir(ws, 'B%d' % r, f['categoria'])
        escribir(ws, 'C%d' % r, f['proveedor'])
        escribir(ws, 'D%d' % r, f['formato'])
        escribir(ws, 'E%d' % r, f['contenido'])
        escribir(ws, 'F%d' % r, f['unidad_base'])
        escribir(ws, 'G%d' % r, f['precio_formato'])
        if f.get('precio_anterior') is not None:
            escribir(ws, 'I%d' % r, f['precio_anterior'])
        escribir(ws, 'M%d' % r, f['notas'])
    rep['ingredientes_13'] = len(filas)
    rep['filas_libres_13'] = ultima - 9 - len(filas)


def mercado_bonus(wb, M, rep):
    b = M['bonus']
    inv = wb['Inventory']
    col_de = {}
    for p in b['productos']:
        r = p['fila']
        escribir(inv, 'A%d' % r, p['producto_en'])
        escribir(inv, 'B%d' % r, p['ud_en'])
        for col, k in (('C', 'stock_ini'), ('D', 'compras'), ('E', 'stock_fin')):
            escribir(inv, '%s%d' % (col, r), p.get(k))
        escribir(inv, 'I%d' % r, p['precio_unitario'])
        col_de[p['producto_es']] = openpyxl.utils.get_column_letter(3 + r - 5)
    vs = wb['Sales for the Period']
    for r in range(5, 15):
        for c in range(1, 18):
            escribir(vs, '%s%d' % (openpyxl.utils.get_column_letter(c), r), None)
    for i, pl in enumerate(b['platos']):
        r = 5 + i
        escribir(vs, 'A%d' % r, pl['plato_en'])
        escribir(vs, 'B%d' % r, pl['raciones'])
        for prod_es, q in pl['por_racion'].items():
            escribir(vs, '%s%d' % (col_de[prod_es], r), q)


def aplicar_mercado(wb, corto, fichas_es, pos, mapa, M, rep):
    if corto in ('01', '02', '03', '04', '05', '06', '07', '08'):
        mercado_fichas(wb, corto, fichas_es, mapa, M, rep)
    mercado_resumenes(wb, corto, pos, M, rep)
    extra = {'04': mercado_04, '06': mercado_06, '08': mercado_08, '09': mercado_09,
             '10': mercado_10, '11': mercado_11, '12': mercado_12, '13': mercado_13,
             'BONUS': mercado_bonus}.get(corto)
    if extra:
        extra(wb, M, rep)


# ---------------------------------------------------------------- Instructions extra
def insertar_extra(wb, fname_en, datos, rep):
    ex = datos['extra']
    bloque = ex['ficheros'].get(fname_en)
    if not bloque:
        raise Aborta('%s sin bloque en instrucciones_extra_en.json' % fname_en)
    ws = wb[HOJA_INSTR_EN]
    ancla_txt = ex['insercion']['ancla_en']
    ancla = None
    for r in range(1, ws.max_row + 1):
        if ws.cell(r, 2).value == ancla_txt:
            ancla = r
            break
    if ancla is None:
        raise Aborta('%s: no encuentro el ancla «%s» en Instructions' % (fname_en, ancla_txt))
    if ws.cell(ancla - 1, 2).value not in (None, ''):
        raise Aborta('%s: la fila anterior al ancla no está vacía' % fname_en)
    for m in ws.merged_cells.ranges:
        if m.max_row >= ancla:
            raise Aborta('%s: combinación %s por debajo del ancla' % (fname_en, m))
    est_titulo = est_vineta = est_vacia = None
    for r in range(1, ancla):
        c = ws.cell(r, 2)
        v = c.value
        if est_titulo is None and isinstance(v, str) and c.font.b and (c.font.sz or 11) == 12:
            est_titulo = copy.copy(c._style)
        if est_vineta is None and isinstance(v, str) and v.startswith('▸'):
            est_vineta = copy.copy(c._style)
    est_vacia = copy.copy(ws.cell(ancla - 1, 2)._style)
    if est_titulo is None or est_vineta is None:
        raise Aborta('%s: sin estilo de título o de viñeta en Instructions' % fname_en)
    filas = bloque['filas']
    n = len(filas)
    ultima_col = max(ws.max_column, 2)
    for r in range(ws.max_row, ancla - 1, -1):
        for c in range(1, ultima_col + 1):
            src, dst = ws.cell(r, c), ws.cell(r + n, c)
            dst.value = src.value
            dst._style = copy.copy(src._style)
        ws.row_dimensions[r + n].height = ws.row_dimensions[r].height
    for i, f in enumerate(filas):
        r = ancla + i
        for c in range(1, ultima_col + 1):
            ws.cell(r, c).value = None
            ws.cell(r, c)._style = copy.copy(ws.cell(ancla - 1, c)._style)
        ws.row_dimensions[r].height = None
        cel = ws.cell(r, 2)
        if f['tipo'] == 'vacia':
            cel._style = copy.copy(est_vacia)
        else:
            cel._style = copy.copy(est_titulo if f['tipo'] == 'titulo' else est_vineta)
            cel.value = f['texto']
    rep['instructions_extra'] = n


def notas_nuevas(wb, fname_en, datos, rep):
    """Celdas de texto nuevas (vacías en el ES), de instrucciones_extra_en.json «notas_nuevas»."""
    n = 0
    for nota in datos['extra'].get('notas_nuevas', []):
        if fname_en not in nota['ficheros']:
            continue
        ws = wb[nota['hoja_en']]
        c = ws[nota['celda']]
        if c.value not in (None, ''):
            raise Aborta('%s!%s no está vacía: %r' % (ws.title, nota['celda'], c.value))
        c.value = nota['en']
        if nota.get('estilo_de'):
            c._style = copy.copy(ws[nota['estilo_de']]._style)
        if nota.get('ancho_columna'):
            ws.column_dimensions[c.column_letter].width = nota['ancho_columna']
        n += 1
    rep['notas_nuevas'] = n


# Anchos de columna (solo formato): cabeceras D9 de «Trim Loss Factors» que se cortaban (T10) y la columna
# «When» del checklist del 06, con plazos en palabras (CHEF-07).
ANCHOS = {'Trim Loss Factors': {'B': 20, 'C': 17, 'D': 17}, 'Event Checklist': {'E': 20}}


def anchos(wb):
    for hoja, cols in ANCHOS.items():
        if hoja in wb.sheetnames:
            for col, w in cols.items():
                wb[hoja].column_dimensions[col].width = w


# Una sola forma de apóstrofo en los 14 libros: la recta (revisión R1 EN, CHEF-19).
APOSTROFOS = {'\u2019': "'", '\u2018': "'"}


def normalizar_apostrofos(wb, rep):
    n = 0
    for ws in wb.worksheets:
        for c in list(ws._cells.values()):
            if isinstance(c.value, str) and c.data_type != 'f' and any(a in c.value for a in APOSTROFOS):
                v = c.value
                for a, b in APOSTROFOS.items():
                    v = v.replace(a, b)
                c.value = v
                n += 1
        for dv in ws.data_validations.dataValidation:
            for attr in ('error', 'errorTitle', 'prompt', 'promptTitle'):
                v = getattr(dv, attr)
                if v and any(a in v for a in APOSTROFOS):
                    for a, b in APOSTROFOS.items():
                        v = v.replace(a, b)
                    setattr(dv, attr, v)
                    n += 1
    rep['apostrofos_normalizados'] = n


# ---------------------------------------------------------------- metadatos
def metadatos(wb, traducir, rep):
    p = wb.properties
    p.title = traducir(p.title, 'docProps title')
    p.keywords = traducir(p.keywords, 'docProps keywords')
    p.category = traducir(p.category, 'docProps category')
    p.subject = SUBJECT
    p.description = DESCRIPTION
    p.creator = CREATOR
    p.lastModifiedBy = CREATOR
    rep['docprops'] = OrderedDict((k, getattr(p, k)) for k in
                                  ('title', 'subject', 'creator', 'keywords', 'description',
                                   'category', 'lastModifiedBy'))


# ---------------------------------------------------------------- gráficos (ZIP)
RX_F = re.compile(r'(<(?:c:)?f>)([^<]*)(</(?:c:)?f>)')
RX_AT = re.compile(r'(<a:t>)([^<]*)(</a:t>)')


def restaurar_graficos(path_es, path_en, mapa, T, traducir, rep):
    """openpyxl reescribe el gráfico sin su <c:style>: se vuelve al XML original del ES con las
    referencias de hoja y el título en inglés. El ancla (drawing) la conserva openpyxl."""
    g_es = extraer_textos.graficos(path_es)
    if not g_es:
        return
    g_en = extraer_textos.graficos(path_en)
    if len(g_en) != len(g_es):
        raise Aborta('%s: %d gráficos en EN y %d en ES' % (path_en, len(g_en), len(g_es)))
    parte_en = {g['hoja']: g['parte'] for g in g_en}
    with zipfile.ZipFile(path_es) as z:
        nuevos = {}
        for g in g_es:
            x = z.read(g['parte']).decode('utf-8')
            x = RX_F.sub(lambda m: m.group(1) + xml_escape(T.formula(html.unescape(m.group(2))))
                         + m.group(3), x)
            x = RX_AT.sub(lambda m: m.group(1) + xml_escape(traducir(html.unescape(m.group(2)),
                                                                     'gráfico ' + g['parte']))
                          + m.group(3), x)
            destino = parte_en.get(mapa[g['hoja']])
            if not destino:
                raise Aborta('gráfico de «%s» sin parte EN' % g['hoja'])
            nuevos[destino] = x.encode('utf-8')
    with zipfile.ZipFile(path_en) as z:
        infos = z.infolist()
        partes = {i.filename: z.read(i.filename) for i in infos}
    partes.update(nuevos)
    tmp = path_en + '.tmp'
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for i in infos:
            zout.writestr(i, partes[i.filename])
    os.replace(tmp, path_en)
    rep['graficos'] = sorted(nuevos)


# ==========================================================================
# Un libro
# ==========================================================================
def construir_libro(fname_es, carpeta, datos, mes):
    fname_en = mapas.FICHEROS[fname_es]
    corto = extraer_textos.corto(fname_es)
    src = os.path.join(ORIGEN, fname_es)
    dst = os.path.join(carpeta, fname_en)
    rep = OrderedDict([('es', fname_es), ('en', fname_en)])
    wb = openpyxl.load_workbook(src)

    fichas_es = detectar_fichas(wb)
    pos = posiciones_es(wb, corto)
    mapa = renombrar(wb)                                                 # 2
    T = Transformador(mapa, datos['fin_conv'])
    reescribir_formulas(wb, T, rep)                                      # 2-3
    traducir = traducir_libro(wb, fname_en, mapa, datos, mes, rep)       # 6 (textos antes que DV)
    reescribir_dv_cf(wb, T, traducir, rep)                               # 2-4
    rep['refs_hoja'] = T.hojas_citadas
    rep['literales'] = T.literales
    if 'Conversions' in wb.sheetnames:
        regenerar_conversions(wb['Conversions'], datos, rep)             # 5
    formatos_y_papel(wb, rep)                                            # 7
    CONTADOR['mercado'] = 0
    aplicar_mercado(wb, corto, fichas_es, pos, mapa, datos['mercado'], rep)   # 8
    rep['celdas_mercado'] = CONTADOR['mercado']
    insertar_extra(wb, fname_en, datos, rep)                             # 9
    notas_nuevas(wb, fname_en, datos, rep)                               # 9 (celdas nuevas)
    anchos(wb)
    metadatos(wb, traducir, rep)                                         # 10
    normalizar_apostrofos(wb, rep)
    if rep['faltan']:
        raise Aborta('%s: %d textos sin traducción:\n  %s'
                     % (fname_es, len(rep['faltan']), '\n  '.join(rep['faltan'][:20])))
    wb.save(dst)                                                         # 11
    restaurar_graficos(src, dst, mapa, T, traducir, rep)                 # 12
    if rep['faltan']:
        raise Aborta('%s: gráfico sin traducción: %r' % (fname_es, rep['faltan']))
    rep['fichas'] = list(fichas_es)
    return rep


def construir(carpeta, datos, mes, log=print):
    os.makedirs(carpeta, exist_ok=True)
    informe = []
    for fname_es in mapas.LIBROS_ES:
        termica()
        rep = construir_libro(fname_es, carpeta, datos, mes)
        informe.append(rep)
        log('  %-38s fórmulas %4d · refs %4d · literales %4d · DV unid. %2d · textos %4d · '
            'mercado %4d' % (rep['en'], rep['formulas_reescritas'], rep['refs_hoja'],
                             rep['literales'], rep['dv_unidades'], rep['textos_traducidos'],
                             rep.get('celdas_mercado', 0)))
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
            if c.value is None:
                continue
            relleno = str(c.fill.fgColor.rgb) if c.fill is not None and c.fill.fill_type == 'solid' else None
            celdas[c.coordinate] = (repr(c.value), c.number_format, relleno, bool(c.protection.locked))
        fuera[ws.title] = {
            'celdas': celdas,
            'merges': sorted(str(m) for m in ws.merged_cells.ranges),
            'dv': sorted('%s:%s:%s' % (dv.type, dv.formula1, dv.sqref) for dv in ws.data_validations.dataValidation),
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
# inject_cache y main
# ==========================================================================
def inject_cache(carpeta, log=print):
    fuera = []
    for fname_es in mapas.LIBROS_ES:
        termica()
        p = os.path.join(carpeta, mapas.FICHEROS[fname_es])
        r = subprocess.run([sys.executable, '-W', 'ignore', INJECT, p], capture_output=True, text=True)
        linea = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ''
        log('    ' + linea)
        fuera.append({'fichero': mapas.FICHEROS[fname_es], 'salida': linea, 'exit': r.returncode,
                      'stderr': r.stderr[-400:] if r.returncode else ''})
    return fuera


def carpeta_dryrun(arg):
    if arg:
        return os.path.abspath(arg)
    s = os.environ.get('CLAUDE_SCRATCHPAD')
    if s:
        return os.path.join(os.path.abspath(s), 'rck-dryrun')
    return os.path.join(REPO, '.work', 'recipe-costing-kit', 'rck-dryrun')


def main():
    ap = argparse.ArgumentParser(description='Recipe Costing Kit Pro (EN): montaje de los 14 xlsx')
    ap.add_argument('--salida', default=None, help='carpeta del dry-run (por defecto '
                    '$CLAUDE_SCRATCHPAD/rck-dryrun o .work/recipe-costing-kit/rck-dryrun)')
    ap.add_argument('--real', action='store_true', help='escribe en astro-site/public/dl/'
                    'recipe-costing-kit/ (exige RECIPE_COSTING_KIT_APPLY=1)')
    ap.add_argument('--pdf', default=None, help='PDF EN del bono (por defecto, el del dry-run)')
    ap.add_argument('--mes', default=None, help='mes de la línea de versión D14 (por defecto, el actual)')
    ap.add_argument('--json', default=None, help='informe JSON')
    ap.add_argument('--sin-idempotencia', action='store_true')
    ap.add_argument('--sin-cache', action='store_true', help='(depuración) no corre inject_cache')
    args = ap.parse_args()

    if args.real and os.environ.get('RECIPE_COSTING_KIT_APPLY') != '1':
        raise SystemExit('ABORTADO: --real escribe en dl/recipe-costing-kit/. Hace falta también '
                         'RECIPE_COSTING_KIT_APPLY=1 (orquestador, tras la revisión).')
    mes = args.mes or mes_por_defecto()
    if mes not in MESES:
        raise SystemExit('--mes debe ser un mes en inglés: %s' % ', '.join(MESES))
    dry = carpeta_dryrun(args.salida)
    carpeta = DESTINO_REAL if args.real else dry
    pdf = args.pdf or os.path.join(dry, PDF_EN)

    t0 = time.time()
    try:
        datos = cargar_datos()
        print('== 1/4 · montaje de los 14 libros → %s (n Conversions = %d, rango $A$5:$B$%d, mes %s)'
              % (carpeta, datos['n'], datos['fin_conv'], mes), flush=True)
        informe = construir(carpeta, datos, mes)
    except Aborta as e:
        raise SystemExit('ABORTADO: %s' % e)

    print('== 2/4 · PDF del bono', flush=True)
    destino_pdf = os.path.join(carpeta, PDF_EN)
    if not os.path.isfile(pdf):
        raise SystemExit('ABORTADO: no encuentro el PDF EN en %s' % pdf)
    if os.path.abspath(pdf) != os.path.abspath(destino_pdf):
        shutil.copy2(pdf, destino_pdf)
    print('  %s (%d KB)' % (destino_pdf, os.path.getsize(destino_pdf) // 1024), flush=True)

    idem = {'ejecutada': False}
    if not args.sin_idempotencia:
        print('== 3/4 · idempotencia: 2.ª construcción en un clon', flush=True)
        clon = os.path.join(os.path.dirname(dry), 'rck-idem')
        if os.path.isdir(clon):
            shutil.rmtree(clon)
        construir(clon, datos, mes, log=lambda *_: None)
        difs = []
        for fname_es in mapas.LIBROS_ES:
            n = mapas.FICHEROS[fname_es]
            difs += diferencias(digest(os.path.join(carpeta, n)), digest(os.path.join(clon, n)), n)
        shutil.rmtree(clon)
        idem = {'ejecutada': True, 'diferencias': len(difs), 'detalle': difs[:30]}
        print('  diferencias 1.ª vs 2.ª construcción: %d' % len(difs), flush=True)
        for d in difs[:10]:
            print('    ' + d)

    print('== 4/4 · inject_cache (AL FINAL, sobre los 14)', flush=True)
    cache = [] if args.sin_cache else inject_cache(carpeta)

    fallos = []
    if idem.get('diferencias'):
        fallos.append('idempotencia: %d diferencias' % idem['diferencias'])
    fallos += ['inject_cache %s: exit %s' % (c['fichero'], c['exit']) for c in cache if c['exit']]
    fallos += ['inject_cache %s: %s' % (c['fichero'], c['salida']) for c in cache
               if 'fallos_pycel=0' not in c['salida']]
    salida = OrderedDict([('producto', 'recipe-costing-kit'), ('version', VERSION),
                          ('fecha', datetime.datetime.now().isoformat(timespec='seconds')),
                          ('modo', 'real' if args.real else 'dry-run'), ('carpeta', carpeta),
                          ('mes', mes), ('conversions_n', datos['n']),
                          ('rango_vlookup', mapas.rango_vlookup(datos['n'])),
                          ('libros', informe), ('pdf', destino_pdf), ('idempotencia', idem),
                          ('inject_cache', cache), ('fallos', fallos),
                          ('segundos', round(time.time() - t0, 1))])
    if args.json:
        with open(args.json, 'w', encoding='utf-8') as fh:
            json.dump(salida, fh, ensure_ascii=False, indent=1, default=str)
        print('informe → %s' % args.json)
    if fallos:
        print('\nFALLOS:\n  ' + '\n  '.join(fallos))
        sys.exit(1)
    print('\nOK: 14 xlsx + PDF en %s (%.0f s)' % (carpeta, time.time() - t0))


if __name__ == '__main__':
    main()
