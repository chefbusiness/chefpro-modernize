#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gates_en.py — Gates F2 del HACCP Food Safety Kit Pro (EN), SPEC §8 (G1-G8), sobre la salida de aplicar_en.py.
Copia adaptada de `restaurant-inventory-kit/gates_en.py`. Solo LEE: los 21 xlsx EN, los 21 xlsx ES publicados
(dl/pack-appcc, solo lectura), censo_es.json y mapas.py. Ningún recuento está escrito a mano: todo sale de
censo_es.json, de los xlsx ES o de mapas.py; las únicas cifras propias son las de la historia de SPEC §5 (G6).

    python3 gates_en.py                               # contra astro-site/public/dl/haccp-templates/
    python3 gates_en.py --dir /tmp/haccp-dry          # contra un dry-run
    python3 gates_en.py --solo G1,G2 [--mes October] [--json informe.json]
    python3 gates_en.py --autotest [--dir …]          # inyecta defectos en una COPIA y exige que se detecten

Gates (SPEC §8):
  G1 paridad: 48 hojas por §2.2; fórmula a fórmula = ES tras HOJAS + CLAVES salvo los 17 patrones de FORMULAS_EN;
     fórmulas con hoja; DV (mismo sqref y nº de celdas; tipo igual; listas por CLAVES salvo D13; °C→°F por
     DV_NUM; +1 de D14); CF (sqref, tipo, prioridad, fórmulas); merges; áreas y títulos de impresión; paneles;
     verdes y desbloqueadas (+2 de D15-D16); sin protección; 0 gráficos e imágenes;
  G2 restos: cero español, «€», caracteres no latinos o fuera de la lista blanca, coma decimal, horas de 24 h,
     normativa ES (RX_NORMA, salvo la cita UK «retained»), IDs internos, en valores, literales, DV, CF, formatos,
     pies y docProps; todo «°C» de texto va entre paréntesis tras su °F;
  G3 formato: paperSize 1 en las 48; fechas del censo con 14/22/18 según su tipo; las 62 de texto convertidas
     (fecha real, 14); pie D21 en las 48; firma PIE_EN; versión D21; docProps; Instructions!B2 = título D5;
  G4 claves: cada ítem de DV ∈ CLAVES (o D13); cada celda escrita en un rango con DV de lista es un ítem;
     cada número de ejemplo en una DV numérica, dentro de sus límites;
  G5 CF: tokens EN inyectivos por rango (dos tokens ES distintos nunca dan el mismo EN) y todos ∈ CLAVES;
  G6 cálculo e historia: <v> en toda <f>, cero errores; cada veredicto EN = CLAVES[veredicto ES] (caché del ES);
     08 = Complete ×8; recuentos iguales donde no hay °F; cifras de ejemplo e incidencias de SPEC §5;
  G7 límites: cada cifra de FORMULAS_EN, LIMITES_02, PARAMETROS, DV_NUM y PROCESOS_16 = SPEC §3 (mapas.LIMITES_F);
     los mensajes de las DV de °F citan sus límites EN;
  G8 censo-entregables.py --fail (Letter) y gate-no-latinos.py en 0.
Sale con código 1 si algún gate falla.
"""
import argparse
import datetime
import html
import json
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from collections import OrderedDict, Counter

AQUI = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(AQUI)
REPO = os.path.dirname(os.path.dirname(SCRIPTS))
sys.path.insert(0, AQUI)

import openpyxl                                          # noqa: E402

import mapas                                             # noqa: E402
import aplicar_en as A                                   # noqa: E402

logging.disable(logging.CRITICAL)

ORIGEN = A.ORIGEN
CENSO_SCRIPT = os.path.join(SCRIPTS, 'censo-entregables.py')
NO_LATINOS = os.path.join(SCRIPTS, 'gate-no-latinos.py')
TOL = 0.006
ERRORES = ('#REF!', '#VALUE!', '#NAME?', '#DIV/0!', '#N/A', '#NUM!', '#NULL!')
CLAVES = mapas.CLAVES
CLAVES_EN = set(CLAVES.values())

# Lista blanca de caracteres no ASCII: los símbolos del ES publicado que no son letras ni signos españoles
# (▸ → ☐ ✓ ✗ ⚠ 📍 · — … °) + la tipografía del kit EN (§ ≤ ≥ − ±). Todo lo demás falla.
SIMBOLOS_OK = set('▸→☐✓✗⚠·—–…°§≤≥−±×½⛔✅❌⏱') | {'\U0001F4CD', '\U0001F534', '\U0001F7E1', '\U0001F7E2', '️'}
RX_ID_INTERNO = re.compile(r'\[(?:fuente|estimado|derivado)\]|\bSPEC\b|\((?:D|I)\d{1,2}\)|\bD\d{1,2}\b(?=[:,)])')
SIGNOS_ES = set('¿¡«»€ºª')
RX_TILDE = re.compile(r'[áéíóúüñÁÉÍÓÚÜÑ]')
LISTA_BLANCA_TILDE = {'ximénez', 'café', 'purée', 'sauté', 'sautéed', 'jalapeño', 'jalapeños', 'crème', 'brûlée',
                      'béchamel', 'entrée', 'entrées'}
FUNCIONALES_ES = {
    'de', 'del', 'las', 'el', 'los', 'y', 'que', 'con', 'para', 'por', 'una', 'unos', 'unas', 'es', 'al', 'se',
    'su', 'sus', 'como', 'pero', 'muy', 'cuando', 'donde', 'porque', 'este', 'esta', 'esto', 'estos', 'desde',
    'hasta', 'sobre', 'entre', 'tu', 'tus', 'te', 'mis', 'hoja', 'pestaña', 'celda', 'celdas', 'sin', 'ejemplo',
    'cada', 'debe', 'hay', 'puede', 'si', 'lo', 'le', 'les', 'todo', 'toda', 'todos', 'nunca', 'siempre',
}
OFICIO_ES = {
    'temperatura', 'temperaturas', 'camara', 'camaras', 'limpieza', 'plagas', 'alergenos', 'alergeno', 'aceite',
    'agua', 'registro', 'registros', 'fecha', 'firma', 'responsable', 'observaciones', 'incidencia', 'incidencias',
    'proveedor', 'proveedores', 'lote', 'caducidad', 'coccion', 'enfriamiento', 'descongelacion', 'termometro',
    'termometros', 'formacion', 'hielo', 'ebullicion', 'albaran', 'mercancias', 'recepcion', 'trazabilidad',
    'desinfeccion', 'manipulador', 'manipuladores', 'carne', 'pescado', 'merluza', 'ternera', 'guisantes', 'nata',
    'harina', 'gambas', 'boqueron', 'boquerones', 'estofado', 'caldo', 'arroz', 'cocina', 'sala', 'barra',
    'almacen', 'plantilla', 'plantillas', 'instrucciones', 'estado', 'semana', 'mes', 'dia', 'lunes', 'martes',
    'miercoles', 'jueves', 'viernes', 'sabado', 'domingo', 'manana', 'tarde', 'grave', 'leve', 'cumple',
    'vigente', 'caducado', 'renovar', 'rechazar', 'revisar', 'vigilar', 'cambiar', 'alerta', 'repetir', 'apto',
    'desechado', 'devuelto', 'pendiente', 'sonda', 'grifo', 'cebo', 'cebos', 'cebadero', 'sanidad', 'inspeccion',
    'gestor', 'autorizado', 'empresa', 'entrantes', 'primeros', 'segundos', 'postres', 'bebidas', 'otros',
    'completo', 'incompleto', 'turbio', 'consumo', 'captura', 'ausente', 'danado', 'trazas', 'contiene', 'apio',
    'mostaza', 'sesamo', 'soja', 'altramuces', 'moluscos', 'crustaceos', 'cacahuetes', 'lacteos', 'huevos',
}
OFICIO_ES -= {'sala', 'mes', 'completo'}                  # 'sala' (UK) / 'mes' / coincidencias inglesas posibles
OFICIO_ES -= {'boquerones'}            # SPEC §5: «anchovy (Engraulis encrasicolus) para boquerones» = nombre del plato
RX_URL = re.compile(r'https?://\S+|\b[\w-]+(?:\.[\w-]+)*\.(?:es|com|pro|gov|org|uk|co|example|net)\b[/\w.#-]*', re.I)
RX_PALABRA = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+")
RX_STR = A.RX_STR
RX_NORMA = re.compile(A.extraer_textos.RX_NORMA.pattern.replace(r'\b112\b', r'(?<![\d.\-§])112(?![\d])'))
RX_NORMA_UE = re.compile(r'Reg\.|Regulation|1169/2011|178/2002|852/2004|853/2004|2073/2005')
RX_SIGLAS_ES = re.compile(r'\b(?:APPCC|PCC|PPRo|DDD|ROESB|RGSEAA|FDS|CIF|NIF)\b')
RX_HORA_24 = re.compile(r'\b(?:0\d|1[3-9]|2[0-3]):[0-5]\d\b')
RX_COMA_DECIMAL = re.compile(r'(?<![\d,])\d+,\d{1,2}(?![\d])')


def no_permitidos(t):
    return sorted({ch for ch in t if ord(ch) > 127 and ch not in SIMBOLOS_OK
                   and not ('À' <= ch <= 'ÿ' and ch not in '×÷')})


def restos_espanol(t):
    out = []
    limpio = RX_URL.sub(' ', t)
    for ch in limpio:
        if ch in SIGNOS_ES:
            out.append(('signo «%s»' % ch, t[:80]))
    for m in RX_PALABRA.finditer(limpio):
        w = m.group(0)
        wl = w.lower()
        ctx = limpio[max(0, m.start() - 30):m.end() + 30].replace('\n', ' ')
        sin = (wl.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
               .replace('ñ', 'n'))
        if RX_TILDE.search(w) and wl not in LISTA_BLANCA_TILDE:
            out.append(('tilde/eñe «%s»' % w, ctx))
        elif wl in FUNCIONALES_ES and w not in ('Y', 'T', 'N', 'NO', 'SE', 'TE', 'SI'):   # Y/N/T son claves EN
            out.append(('funcional ES «%s»' % w, ctx))
        elif sin in OFICIO_ES and wl not in LISTA_BLANCA_TILDE:
            out.append(('oficio ES «%s»' % w, ctx))
    m = RX_COMA_DECIMAL.search(t)
    if m:
        out.append(('coma decimal «%s»' % m.group(0), t[:80]))
    m = RX_HORA_24.search(t)
    if m and not re.search(re.escape(m.group(0)) + r'\s*(?:AM|PM|a\.m\.|p\.m\.)', t):
        out.append(('hora de 24 h «%s»' % m.group(0), t[:80]))
    m = RX_SIGLAS_ES.search(t)
    if m:
        out.append(('sigla ES «%s»' % m.group(0), t[:80]))
    for m in RX_NORMA.finditer(t.replace('EPA Reg. No.', 'EPA registration no.')):
        if RX_NORMA_UE.fullmatch(m.group(0)) and re.search(r'\bUK\b|retained', t):
            continue                                       # D25/D8: cita UK de la norma UE retenida
        out.append(('normativa ES «%s»' % m.group(0), t[:80]))
        break
    return out


def celsius_sueltos(t):
    """D9: todo «°C» de texto va entre paréntesis justo detrás de su cifra en °F («41 °F (5 °C)»)."""
    malos = []
    for m in re.finditer('°C', t):
        antes = t[:m.start()]
        abre = antes.rfind('(')
        if abre < 0 or ')' in antes[abre:]:
            malos.append(t[max(0, m.start() - 25):m.end() + 5])
            continue
        if '°F' not in antes[abre:] and '°F' not in antes[max(0, abre - 40):abre]:
            malos.append(t[max(0, abre - 25):m.end() + 5])
    return malos


# ==========================================================================
# Utilidades
# ==========================================================================
class Resultado:
    def __init__(self):
        self.gates = OrderedDict()
        self.actual = None

    def gate(self, nombre):
        self.actual = nombre
        self.gates.setdefault(nombre, {'fallos': [], 'datos': OrderedDict()})
        return self

    def fallo(self, msg):
        self.gates[self.actual]['fallos'].append(msg)

    def dato(self, k, v):
        self.gates[self.actual]['datos'][k] = v


_CACHE = {}


def cargar(path, data_only=False):
    k = (path, data_only, os.path.getmtime(path))
    if k not in _CACHE:
        _CACHE[k] = openpyxl.load_workbook(path, data_only=data_only)
    return _CACHE[k]


def libros(carpeta):
    for es in mapas.LIBROS_ES:
        en = mapas.FICHEROS[es]
        yield es, en, A.extraer_textos.corto(es), os.path.join(ORIGEN, es), os.path.join(carpeta, en)


def lits(f):
    return [x[1:-1].replace('""', '"') for x in RX_STR.findall(f or '')]


def celdas(sqref):
    out = []
    for rg in str(sqref).split():
        out.extend(A.rango(rg))
    return out


def es_verde(c):
    return (c.fill is not None and c.fill.fgColor is not None and isinstance(c.fill.fgColor.rgb, str)
            and c.fill.fgColor.rgb.upper().endswith(A.VERDE))


def celdas_reales(ws):
    for row in ws.iter_rows():
        for c in row:
            if c.__class__.__name__ != 'MergedCell':
                yield c


def _pagina(ws):
    ps = ws.page_setup
    fit = ws.sheet_properties.pageSetUpPr.fitToPage if ws.sheet_properties.pageSetUpPr else None
    return (ps.orientation, ps.fitToWidth, ps.fitToHeight, fit, str(ws.print_title_rows), str(ws.print_title_cols))


def _area(ws):
    pa = ws.print_area
    return pa.split('!')[-1] if pa else None


def _cf_firma(cf, regla, trans):
    dxf = regla.dxf
    color = None
    if dxf is not None:
        color = (str(dxf.fill.fgColor.rgb) if dxf.fill is not None and dxf.fill.fgColor is not None else None,
                 str(dxf.font.color.rgb) if dxf.font is not None and dxf.font.color is not None else None)
    return (str(cf.sqref), regla.type, regla.operator, regla.priority, bool(regla.stopIfTrue),
            tuple(trans(x) for x in (regla.formula or [])), regla.text, color)


def parametros_libro(corto):
    return [(h, v) for (c, h), v in mapas.PARAMETROS.items() if c == corto]


def dv_en_esperada(corto, h_es, de, cen, T):
    """(type, operator, formula1, formula2) EN de una DV ES."""
    sq, f1 = str(de.sqref), de.formula1 or ''
    esp = mapas.DV_LISTAS_ESPECIALES.get((corto, h_es, sq))
    if esp:
        return de.type, de.operator, esp[1], de.formula2
    if f1.startswith('"'):
        return de.type, de.operator, mapas.dv_lista(CLAVES[x] for x in f1.strip('"').split(',')), de.formula2
    if de.type in ('decimal', 'whole') and cen['cita_temp']:
        for k, (es, en) in mapas.DV_NUM.items():
            if k[:2] == (corto, h_es) and (len(k) == 2 or sq.startswith(k[2])):
                return de.type, de.operator, en[0], en[1]
        return de.type, de.operator, '<<sin DV_NUM>>', None
    return de.type, de.operator, T.refs(f1) if f1 else f1, T.refs(de.formula2) if de.formula2 else de.formula2


# ==========================================================================
# G1 — paridad estructural
# ==========================================================================
def gateG1(R, carpeta, datos):
    R.gate('G1 paridad')
    censo = datos['censo']
    tot = Counter()
    for es, en, corto, pes, pen in libros(carpeta):
        if not os.path.isfile(pen):
            R.fallo('%s: no existe' % en)
            continue
        ce = censo['libros'][es]
        wes, wen = cargar(pes), cargar(pen)
        esperado = [mapas.HOJAS[h] for h in ce['hojas']]
        if wen.sheetnames != esperado or wes.sheetnames != ce['hojas']:
            R.fallo('%s: hojas %r ≠ %r' % (en, wen.sheetnames, esperado))
            continue
        tot['hojas'] += len(esperado)
        mapa = OrderedDict((h, mapas.HOJAS[h]) for h in wes.sheetnames)
        T = A.Transformador(mapa)
        extra_param = {(mapa[h], 'B3') for h, _ in parametros_libro(corto)}
        for h_es in wes.sheetnames:
            ws_es, ws_en = wes[h_es], wen[mapa[h_es]]
            hd = ce['hojas_detalle'][h_es]
            lugar = '%s:%s' % (en, ws_en.title)
            f_es = {c.coordinate: c.value for c in ws_es._cells.values() if c.data_type == 'f'}
            f_en = {c.coordinate: c.value for c in ws_en._cells.values() if c.data_type == 'f'}
            if len(f_es) != hd['celdas_formula']:
                R.fallo('%s: el ES ya no cuadra con el censo (%d ≠ %d fórmulas)' % (lugar, len(f_es), hd['celdas_formula']))
            if set(f_en) != set(f_es):
                R.fallo('%s: celdas con fórmula distintas: solo ES %s · solo EN %s'
                        % (lugar, sorted(set(f_es) - set(f_en))[:5], sorted(set(f_en) - set(f_es))[:5]))
            con_hoja = 0
            for k, fe in f_es.items():
                fn = f_en.get(k)
                if fn is None:
                    continue
                tot['formulas'] += 1
                try:
                    esperado_f, es_pat = A.formula_en(fe, ws_es[k].row, T)
                except A.Aborta as e:
                    esperado_f, es_pat = '<<%s>>' % e, False
                tot['formulas_patron_en'] += es_pat
                if esperado_f != fn:
                    R.fallo('%s!%s: fórmula EN %r ≠ esperada %r' % (lugar, k, fn[:80], esperado_f[:80]))
                if A.extraer_textos.refs_hoja(fn):
                    con_hoja += 1
                    for h in A.extraer_textos.refs_hoja(fn):
                        if h not in wen.sheetnames:
                            R.fallo('%s!%s cita la hoja inexistente %r' % (lugar, k, h))
            tot['formulas_con_hoja'] += con_hoja
            if con_hoja != hd['formulas_con_hoja']:
                R.fallo('%s: %d fórmulas con referencia a hoja ≠ censo %d' % (lugar, con_hoja, hd['formulas_con_hoja']))
            # DV
            cen_dv = {d['sqref']: d for d in hd['dv']}
            dves = sorted(ws_es.data_validations.dataValidation, key=lambda d: str(d.sqref))
            dven_all = ws_en.data_validations.dataValidation
            d14 = (corto == '17' and h_es == A.D14['hoja'])
            extra = [d for d in dven_all if d14 and str(d.sqref) == A.D14['sqref']]
            dven = sorted([d for d in dven_all if d not in extra], key=lambda d: str(d.sqref))
            if len(dves) != len(dven) or len(dves) != len(hd['dv']) or len(extra) != (1 if d14 else 0):
                R.fallo('%s: DV ES %d, EN %d (+%d D14), censo %d' % (lugar, len(dves), len(dven), len(extra), len(hd['dv'])))
            for de, dn in zip(dves, dven):
                tot['dv'] += 1
                tot['dv_celdas'] += len(celdas(dn.sqref))
                firma = lambda d: (str(d.sqref), bool(d.allow_blank), bool(d.showDropDown),  # noqa: E731
                                   bool(d.showErrorMessage), bool(d.showInputMessage), d.errorStyle)
                if firma(de) != firma(dn):
                    R.fallo('%s: DV %s cambia (%r → %r)' % (lugar, de.sqref, firma(de), firma(dn)))
                cen = cen_dv.get(str(de.sqref))
                if cen is None or len(celdas(dn.sqref)) != cen['n_celdas']:
                    R.fallo('%s: DV %s fuera del censo o con otro nº de celdas' % (lugar, dn.sqref))
                    continue
                for attr in ('error', 'errorTitle', 'prompt', 'promptTitle'):
                    if bool(getattr(de, attr)) != bool(getattr(dn, attr)):
                        R.fallo('%s: DV %s pierde/gana %s' % (lugar, dn.sqref, attr))
                try:
                    esp = dv_en_esperada(corto, h_es, de, cen, T)
                except (KeyError, A.Aborta) as e:
                    esp = ('<<%s>>' % e,)
                got = (dn.type, dn.operator, dn.formula1, dn.formula2)
                if got != esp:
                    R.fallo('%s: DV %s %r ≠ esperada %r' % (lugar, dn.sqref, got, esp))
                if (corto, h_es, str(de.sqref)) in mapas.DV_LISTAS_ESPECIALES:
                    tot['dv_d13'] += 1
            for dn in extra:
                tot['dv_d14'] += 1
                tot['dv_celdas_d14'] += len(celdas(dn.sqref))
                if (dn.type, dn.operator, dn.formula1, dn.formula2) != ('decimal', 'between', A.D14['f1'], A.D14['f2']) \
                        or not dn.error:
                    R.fallo('%s: DV D14 %s = %r' % (lugar, dn.sqref, (dn.type, dn.formula1, dn.formula2)))
            # CF
            cfe = sorted((_cf_firma(cf, r, T.formula) for cf in ws_es.conditional_formatting for r in cf.rules), key=repr)
            cfn = sorted((_cf_firma(cf, r, lambda x: x) for cf in ws_en.conditional_formatting for r in cf.rules), key=repr)
            tot['cf'] += len(cfn)
            if len(cfn) != len(hd['cf']):
                R.fallo('%s: %d CF EN ≠ censo %d' % (lugar, len(cfn), len(hd['cf'])))
            if cfe != cfn:
                dif = [(a, b) for a, b in zip(cfe, cfn) if a != b] or [(cfe[:1], cfn[:1])]
                R.fallo('%s: formato condicional distinto (ES transformado → EN): %r' % (lugar, dif[0]))
            # merges, protección, paneles, impresión, columnas ocultas
            mg = sorted(map(str, ws_en.merged_cells.ranges))
            if mg != sorted(hd['merges']):
                R.fallo('%s: combinaciones distintas' % lugar)
            tot['merges'] += len(mg)
            if bool(ws_en.protection.sheet) != hd['proteccion']['hoja'] or ws_en.protection.password:
                R.fallo('%s: protección distinta del ES' % lugar)
            if ws_en.freeze_panes != hd['paneles']:
                R.fallo('%s: paneles %s ≠ %s' % (lugar, ws_en.freeze_panes, hd['paneles']))
            tot['paneles'] += 1 if ws_en.freeze_panes else 0
            if _pagina(ws_es) != _pagina(ws_en):
                R.fallo('%s: ajuste o títulos de impresión %r ≠ %r' % (lugar, _pagina(ws_es), _pagina(ws_en)))
            tot['titulos_impresion'] += 1 if ws_en.print_title_rows else 0
            ae = hd['area_impresion'].split('!')[-1] if hd['area_impresion'] else None
            if _area(ws_en) != ae:
                R.fallo('%s: área de impresión %s ≠ %s' % (lugar, _area(ws_en), ae))
            tot['areas_impresion'] += 1 if ae else 0
            ocultas = sorted(k for k, d in ws_en.column_dimensions.items() if d.hidden)
            if ocultas != hd['columnas_ocultas']:
                R.fallo('%s: columnas ocultas %s ≠ %s' % (lugar, ocultas, hd['columnas_ocultas']))
            # verdes y desbloqueadas (+B3 de D15-D16)
            extra_c = {c for (h, c) in extra_param if h == ws_en.title}
            ue = {c.coordinate for c in celdas_reales(ws_es) if c.protection.locked is False}
            un = {c.coordinate for c in celdas_reales(ws_en) if c.protection.locked is False}
            ve = {c.coordinate for c in celdas_reales(ws_es) if es_verde(c)}
            vn = {c.coordinate for c in celdas_reales(ws_en) if es_verde(c)}
            if un != ue | extra_c:
                R.fallo('%s: desbloqueadas distintas (solo ES %s, solo EN %s)' % (lugar, sorted(ue - un)[:5],
                                                                                   sorted(un - ue - extra_c)[:5]))
            if vn != ve | extra_c:
                R.fallo('%s: verdes distintas (solo ES %s, solo EN %s)' % (lugar, sorted(ve - vn)[:5], sorted(vn - ve - extra_c)[:5]))
            bloq = sorted(c for c in vn if c not in un)
            if bloq and sorted(c for c in ve if c not in ue) != bloq:
                R.fallo('%s: celdas verdes bloqueadas nuevas %s' % (lugar, bloq[:5]))
            tot['verdes'] += len(vn)
            tot['desbloqueadas'] += len(un)
        with zipfile.ZipFile(pen) as z:
            n = z.namelist()
        g = [x for x in n if x.startswith('xl/charts/') or x.startswith('xl/media/') or x.startswith('xl/drawings/')]
        if g:
            R.fallo('%s: gráficos/imágenes %s' % (en, g[:3]))
    T0 = censo['totales']
    n_pat = sum(p['n'] for info in censo['libros'].values() for hd in info['hojas_detalle'].values()
                for p in hd['patrones_formula'] if p['patron'] in mapas.FORMULAS_EN)
    n_par = len(mapas.PARAMETROS)
    esperados = OrderedDict([
        ('hojas', T0['hojas']), ('formulas', T0['celdas_formula']), ('formulas_patron_en', n_pat),
        ('formulas_con_hoja', T0['formulas_con_hoja']), ('dv', T0['dv']), ('dv_d14', 1), ('dv_d13', 1),
        ('dv_celdas', T0['dv_celdas']), ('cf', T0['cf']), ('merges', T0['merges']),
        ('areas_impresion', T0['areas_impresion']), ('titulos_impresion', T0['titulos_impresion']),
        ('paneles', T0['paneles']), ('verdes', T0['verdes'] + n_par), ('desbloqueadas', T0['desbloqueadas'] + n_par),
    ])
    for k, v in esperados.items():
        if tot[k] != v:
            R.fallo('total %s = %d ≠ esperado %d (censo)' % (k, tot[k], v))
    for k, v in sorted(tot.items()):
        R.dato(k, v)


# ==========================================================================
# G2 — restos y caracteres
# ==========================================================================
def piezas_de_texto(pen):
    wb = cargar(pen)
    for ws in wb.worksheets:
        yield 'hoja', ws.title, ws.title
        for c in ws._cells.values():
            if isinstance(c.value, str) and c.data_type != 'f':
                yield 'valor', '%s!%s' % (ws.title, c.coordinate), c.value
            if c.data_type == 'f':
                for x in lits(c.value):
                    yield 'literal', '%s!%s' % (ws.title, c.coordinate), x
            if isinstance(c.number_format, str) and c.number_format != 'General':
                yield 'formato', '%s!%s' % (ws.title, c.coordinate), c.number_format
        for dv in ws.data_validations.dataValidation:
            for attr in ('error', 'errorTitle', 'prompt', 'promptTitle', 'formula1'):
                v = getattr(dv, attr)
                if v and (attr != 'formula1' or v.startswith('"')):
                    yield 'dv', '%s DV %s %s' % (ws.title, dv.sqref, attr), v
        for cf in ws.conditional_formatting:
            for regla in cf.rules:
                for f in regla.formula or []:
                    for x in lits(f):
                        yield 'literal', '%s CF %s' % (ws.title, cf.sqref), x
        for parte in ('oddHeader', 'oddFooter', 'evenHeader', 'evenFooter', 'firstHeader', 'firstFooter'):
            hf = getattr(ws, parte)
            for pos in ('left', 'center', 'right'):
                t = getattr(hf, pos).text
                if t:
                    yield 'cabecera-pie', '%s %s.%s' % (ws.title, parte, pos), t
    p = wb.properties
    for k in ('title', 'subject', 'creator', 'keywords', 'description', 'category', 'lastModifiedBy'):
        v = getattr(p, k)
        if v:
            yield 'docprops', k, v
    with zipfile.ZipFile(pen) as z:
        estilos = z.read('xl/styles.xml').decode('utf-8')
    for m in re.finditer(r'<numFmt [^>]*formatCode="([^"]*)"', estilos):
        yield 'styles.xml', 'numFmt', html.unescape(m.group(1))


def gateG2(R, carpeta, datos):
    R.gate('G2 restos')
    n = Counter()
    for es, en, corto, pes, pen in libros(carpeta):
        for tipo, lugar, t in piezas_de_texto(pen):
            n[tipo] += 1
            donde = '%s %s' % (en, lugar)
            if '€' in t or re.search(r'\bEUR\b|\beuros?\b', t):
                R.fallo('%s: moneda € en %s: %r' % (donde, tipo, t[:70]))
            malos = no_permitidos(t)
            if malos:
                R.fallo('%s: carácter fuera de la lista blanca %r en %s: %r' % (donde, ''.join(malos), tipo, t[:60]))
            if tipo in ('formato', 'styles.xml'):
                if re.search(r'dd/mm|yyyy-mm-dd|€', t, re.I) or (re.search(r'hh?:mm', t, re.I) and 'AM/PM' not in t.upper()
                                                                  and t != A.FMT_FECHA_HORA):
                    R.fallo('%s: formato %r' % (donde, t))
                continue
            m = RX_ID_INTERNO.search(t)
            if m:
                R.fallo('%s: ID interno %r en %s: …%s…' % (donde, m.group(0), tipo, t[max(0, m.start() - 30):m.end() + 10]))
            for motivo, ctx in restos_espanol(t):
                R.fallo('%s: %s · …%s…' % (donde, motivo, ctx))
            for s in celsius_sueltos(t):
                R.fallo('%s: °C sin su °F delante · …%s…' % (donde, s))
                n['celsius_sueltos'] += 1
            if '°C' in t:
                n['textos_con_celsius_ok'] += 1
    for k, v in sorted(n.items()):
        R.dato(k, v)


# ==========================================================================
# G3 — formato
# ==========================================================================
def gateG3(R, carpeta, datos, mes):
    R.gate('G3 formato')
    censo = datos['censo']
    n = Counter()
    rx_version = re.compile(r'^Version %s · %s \d{4} · %s · info@aichef\.pro$'
                            % (re.escape(A.VERSION), mes, re.escape(A.DESCRIPTION)))
    for es, en, corto, pes, pen in libros(carpeta):
        ce = censo['libros'][es]
        wb = cargar(pen)
        wes = cargar(pes)
        firmas_es = sum(1 for ws in wes.worksheets for c in ws._cells.values() if c.value == mapas.PIE_ES)
        firmas_en = sum(1 for ws in wb.worksheets for c in ws._cells.values() if c.value == mapas.PIE_EN)
        if firmas_en != firmas_es:
            R.fallo('%s: %d firmas PIE_EN ≠ %d del ES' % (en, firmas_en, firmas_es))
        n['firmas'] += firmas_en
        for h_es, hd in ce['hojas_detalle'].items():
            ws = wb[mapas.HOJAS[h_es]]
            n['hojas'] += 1
            if ws.page_setup.paperSize not in (1, '1'):
                R.fallo('%s:%s: paperSize %s ≠ 1 (Letter)' % (en, ws.title, ws.page_setup.paperSize))
            fechas = {}
            for f in hd['fechas']:
                fechas[f['celda']] = A.NUMFMT[A.tipo_fecha(f['formato'])]
            for f in hd['fechas_texto']:
                c = ws[f['celda']]
                n['fechas_texto'] += 1
                esp = datetime.datetime.strptime(f['texto'], '%d/%m/%Y')
                if c.value != esp:
                    R.fallo('%s:%s!%s: fecha de texto %r no convertida (%r)' % (en, ws.title, f['celda'], f['texto'], c.value))
                fechas[f['celda']] = 14
            for coord, fid in fechas.items():
                c = ws[coord]
                n['fechas_%d' % fid] += 1
                if c._style.numFmtId != fid:
                    R.fallo('%s:%s!%s: fecha con numFmtId %s ≠ %s' % (en, ws.title, coord, c._style.numFmtId, fid))
            for c in ws._cells.values():
                if c._style.numFmtId in (14, 18, 22) and c.coordinate not in fechas:
                    R.fallo('%s:%s!%s: numFmtId %s en una celda que no era fecha' % (en, ws.title, c.coordinate, c._style.numFmtId))
            for k in hd['cabeceras_pies']:
                obj, pos = k.split('.')
                v = getattr(getattr(ws, obj), pos).text
                if v != A.PIE_EN:
                    R.fallo('%s:%s: %s = %r ≠ pie D21' % (en, ws.title, k, v))
                else:
                    n['pies'] += 1
        ins = wb[A.HOJA_INSTR_EN]
        vers = [c.value for c in ins._cells.values() if isinstance(c.value, str) and c.value.startswith('Version ')]
        if len(vers) != 1 or not rx_version.match(vers[0]):
            R.fallo('%s: línea de versión D21 %r' % (en, vers))
        else:
            n['versiones'] += 1
        p = wb.properties
        esp = {'title': mapas.TITULOS[en], 'subject': A.SUBJECT, 'keywords': A.KEYWORDS, 'description': A.DESCRIPTION,
               'category': A.CATEGORY, 'creator': A.CREATOR}
        for k, v in esp.items():
            if getattr(p, k) != v:
                R.fallo('%s: docProps %s %r ≠ %r' % (en, k, getattr(p, k), v))
        if ins['B2'].value != mapas.TITULOS[en]:
            R.fallo('%s: Instructions!B2 %r ≠ título D5' % (en, ins['B2'].value))
    T0 = censo['totales']
    if n['hojas'] != T0['hojas'] or n['pies'] != sum(len(hd['cabeceras_pies']) for i in censo['libros'].values()
                                                       for hd in i['hojas_detalle'].values()):
        R.fallo('hojas %d / pies %d ≠ censo' % (n['hojas'], n['pies']))
    if n['fechas_texto'] != T0['fechas_texto']:
        R.fallo('fechas de texto %d ≠ censo %d' % (n['fechas_texto'], T0['fechas_texto']))
    for k, v in sorted(n.items()):
        R.dato(k, v)


# ==========================================================================
# G4 — claves
# ==========================================================================
def gateG4(R, carpeta, datos):
    R.gate('G4 claves')
    n = Counter()
    for es, en, corto, pes, pen in libros(carpeta):
        wb = cargar(pen)
        for ws in wb.worksheets:
            lugar = '%s:%s' % (en, ws.title)
            for dv in ws.data_validations.dataValidation:
                f1 = dv.formula1 or ''
                if dv.type == 'list' and f1.startswith('"'):
                    items = f1.strip('"').split(',')
                    n['dv_listas'] += 1
                    especial = items == mapas.PROCESOS_16
                    for x in items:
                        if x not in CLAVES_EN and not especial:
                            R.fallo('%s: DV %s ítem %r ∉ CLAVES' % (lugar, dv.sqref, x))
                    for coord in celdas(dv.sqref):
                        c = ws[coord]
                        if c.value is None or c.data_type == 'f':
                            continue
                        n['valores_con_dv_lista'] += 1
                        if str(c.value) not in items:
                            R.fallo('%s!%s: %r fuera de su DV %s' % (lugar, coord, c.value, f1[:60]))
                elif dv.type in ('decimal', 'whole') and f1 and dv.formula2:
                    try:
                        lo, hi = float(f1), float(dv.formula2)
                    except ValueError:
                        continue
                    for coord in celdas(dv.sqref):
                        v = ws[coord].value
                        if v is None or ws[coord].data_type == 'f':
                            continue
                        n['valores_con_dv_numerica'] += 1
                        if not isinstance(v, (int, float)) or isinstance(v, bool) or not lo <= v <= hi:
                            R.fallo('%s!%s: %r fuera de su DV %s-%s' % (lugar, coord, v, f1, dv.formula2))
    for k, v in sorted(n.items()):
        R.dato(k, v)


# ==========================================================================
# G5 — CF
# ==========================================================================
def gateG5(R, carpeta, datos):
    R.gate('G5 CF')
    n = Counter()
    for es, en, corto, pes, pen in libros(carpeta):
        wes, wen = cargar(pes), cargar(pen)
        for h_es in wes.sheetnames:
            ws_es, ws_en = wes[h_es], wen[mapas.HOJAS[h_es]]
            tok_es, tok_en = {}, {}
            for cf in ws_es.conditional_formatting:
                for r in cf.rules:
                    for f in r.formula or []:
                        tok_es.setdefault(str(cf.sqref), set()).update(x for x in lits(f) if x)
            for cf in ws_en.conditional_formatting:
                for r in cf.rules:
                    for f in r.formula or []:
                        tok_en.setdefault(str(cf.sqref), set()).update(x for x in lits(f) if x)
            for rg in sorted(set(tok_es) | set(tok_en)):
                e, m = tok_es.get(rg, set()), tok_en.get(rg, set())
                n['rangos'] += 1
                n['tokens'] += len(m)
                if len(e) != len(m):
                    R.fallo('%s:%s CF %s: %d tokens ES → %d EN (colisión) %r' % (en, ws_en.title, rg, len(e), len(m), sorted(m)))
                fuera = sorted(x for x in m if x not in CLAVES_EN)
                if fuera:
                    R.fallo('%s:%s CF %s: tokens ∉ CLAVES %r' % (en, ws_en.title, rg, fuera))
    err = mapas.cruzar_censo(os.path.join(AQUI, 'censo_es.json'))
    for e in err:
        R.fallo('mapas.cruzar_censo: ' + e)
    for k, v in sorted(n.items()):
        R.dato(k, v)


# ==========================================================================
# G6 — cálculo e historia
# ==========================================================================
def celdas_sin_v(path):
    fuera = set()
    with zipfile.ZipFile(path) as z:
        wbx = z.read('xl/workbook.xml').decode('utf-8')
        rels = z.read('xl/_rels/workbook.xml.rels').decode('utf-8')
        destino = {}
        for tag in re.findall(r'<Relationship\b[^>]*>', rels):
            i, t = re.search(r'\bId="([^"]+)"', tag), re.search(r'\bTarget="([^"]+)"', tag)
            if i and t:
                destino[i.group(1)] = t.group(1)
        for tag in re.findall(r'<sheet\b[^>]*>', wbx):
            nombre = html.unescape(re.search(r'\bname="([^"]*)"', tag).group(1))
            rid = re.search(r'\br:id="([^"]+)"', tag).group(1)
            t = destino[rid]
            parte = t.lstrip('/') if t.startswith('/') else 'xl/' + t
            xml = z.read(parte).decode('utf-8')
            for m in re.finditer(r'<c\b([^>]*?)(?:/>|>(.*?)</c>)', xml, re.S):
                dentro = m.group(2) or ''
                if '<f' in dentro and not re.search(r'<v>[^<]', dentro) and '<v></v>' not in dentro \
                        and '<v/>' not in dentro and '<v />' not in dentro:
                    fuera.add((nombre, re.search(r'\br="([A-Z]+\d+)"', m.group(1)).group(1)))
    return fuera


def num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


# Historia de SPEC §5 (D20): cifras de ejemplo EN y veredictos que cuentan las incidencias INC-001…INC-007
HISTORIA = OrderedDict([
    ('01', [('Weekly Log', {'B7': 38, 'G7': 39, 'B8': 37, 'G8': 39, 'B9': 44, 'G9': 38, 'C9': 'ALERT', 'F9': 'INC-001'})]),
    ('02', [('Receiving Temps', {'D5': 35, 'D6': 38, 'D7': 7, 'G5': 'OK', 'G6': 'OK', 'G7': 'REJECT'})]),
    ('05', [('Receiving Checklist', {'D5': 35, 'D6': 38, 'D7': 7})]),
    ('09', [('Oil Tests', {'E5': 347, 'E6': 352, 'E7': 356, 'F5': 'OK', 'F6': 'WATCH', 'F7': 'CHANGE'}),
            ('Used Oil Pickups', {'B5': 10})]),
    ('10', [('Water Checks', {'E5': 'OK', 'E6': 'INVESTIGATE', 'E7': 'INVESTIGATE'})]),
    ('16', [('Cooking & Reheating', {'E5': 180, 'E6': 172, 'E7': 158, 'H5': 'OK', 'H6': 'OK', 'H7': 'REPEAT'})]),
    ('17', [('Cooling', {'D5': 198, 'F5': 43, 'I5': 38, 'D6': 185, 'F6': 46, 'I6': 39, 'D7': 190, 'F7': 78,
                         'H5': 'OK', 'H6': 'OK', 'H7': 'ALERT'}),
            ('Thawing', {'B3': 24, 'H5': 'OK', 'H6': 'OK'})]),
    ('18', [('Parasite Destruction', {'B3': 168, 'F5': -8, 'G5': 169, 'F6': -33, 'G6': 16, 'H5': 'OK', 'H6': 'OK'})]),
    ('19', [('Calibration Log', {'B3': 0, 'E5': 32.5, 'E6': 211.1, 'E7': 28.8, 'D5': 32, 'D6': 212, 'F7': 3.2,
                                 'G5': 'PASS', 'G6': 'PASS', 'G7': 'FAIL'})]),
])
SIN_FAHRENHEIT = {'03', '04', '07', '08', '11', '12', '15'}       # recuentos que no dependen de °F ni de la fecha


def gateG6(R, carpeta, datos):
    R.gate('G6 cálculo')
    n = Counter()
    for es, en, corto, pes, pen in libros(carpeta):
        wf, wv = cargar(pen), cargar(pen, data_only=True)
        wes_v = cargar(pes, data_only=True)
        wes_f = cargar(pes)
        sin_v = celdas_sin_v(pen)
        for h_es in wes_f.sheetnames:
            ws, ws_v, we_v = wf[mapas.HOJAS[h_es]], wv[mapas.HOJAS[h_es]], wes_v[h_es]
            for c in ws._cells.values():
                if c.data_type != 'f':
                    continue
                n['formulas'] += 1
                if (ws.title, c.coordinate) in sin_v:
                    R.fallo('%s:%s!%s sin caché (<f> sin <v>)' % (en, ws.title, c.coordinate))
                    continue
                v = ws_v[c.coordinate].value
                ve = we_v[c.coordinate].value
                if isinstance(v, str) and v in ERRORES:
                    R.fallo('%s:%s!%s = %s' % (en, ws.title, c.coordinate, v))
                    continue
                if v is None:
                    n['vacias_legitimas'] += 1
                else:
                    n['con_valor'] += 1
                if isinstance(ve, str) and ve in CLAVES:
                    n['veredictos'] += 1
                    n['veredictos_' + corto] += 1
                    if v != CLAVES[ve]:
                        R.fallo('%s:%s!%s veredicto %r ≠ CLAVES[%r] = %r' % (en, ws.title, c.coordinate, v, ve, CLAVES[ve]))
                elif (ve is None) != (v is None) and corto not in ('B01',):
                    R.fallo('%s:%s!%s caché %r (ES %r)' % (en, ws.title, c.coordinate, v, ve))
                elif num(ve) and corto in SIN_FAHRENHEIT:
                    n['recuentos'] += 1
                    if not (num(v) and abs(v - ve) < TOL):
                        R.fallo('%s:%s!%s recuento %r ≠ ES %r' % (en, ws.title, c.coordinate, v, ve))
    for corto in ('01', '02', '08', '09', '10', '12', '16', '17', '18', '19', 'B01'):
        if not n['veredictos_' + corto]:
            R.fallo('%s: sin veredictos de ejemplo que comparar' % corto)
    # 08: las 8 filas de ejemplo «Complete»
    w8 = cargar(os.path.join(carpeta, mapas.FICHEROS['08-matriz-alergenos.xlsx']), True)['Allergen Matrix']
    s8 = [w8['S%d' % r].value for r in range(6, 14)]
    if s8 != ['Complete'] * 8:
        R.fallo('08 Allergen Matrix S6:S13 %r ≠ Complete ×8' % s8)
    # historia de SPEC §5 (valores de la caché para las fórmulas)
    for corto, hojas in HISTORIA.items():
        fname = [en for es, en, c, *_ in libros(carpeta) if c == corto][0]
        wv = cargar(os.path.join(carpeta, fname), True)
        for hoja, esperado in hojas:
            for coord, e in esperado.items():
                v = wv[hoja][coord].value
                n['historia'] += 1
                ok = (num(v) and num(e) and abs(v - e) < 0.051) or v == e
                if not ok:
                    R.fallo('%s %s!%s = %r ≠ SPEC §5 %r' % (corto, hoja, coord, v, e))
    # 11 Corrective Actions: las 7 incidencias siguen ahí (A5:A11)
    w11 = cargar(os.path.join(carpeta, mapas.FICHEROS['11-registro-acciones-correctivas.xlsx']))['Corrective Actions']
    incs = [w11['A%d' % r].value for r in range(5, 12)]
    if incs != ['INC-%03d' % i for i in range(1, 8)]:
        R.fallo('11 Corrective Actions A5:A11 %r ≠ INC-001…INC-007' % incs)
    for k, v in sorted(n.items()):
        R.dato(k, v)


# ==========================================================================
# G7 — límites (SPEC §3 = mapas.LIMITES_F)
# ==========================================================================
def _num_txt(x):
    return ('%g' % x)


def gateG7(R, carpeta, datos):
    R.gate('G7 límites')
    L = mapas.LIMITES_F
    n = Counter()
    # Sondas: (libro, hoja EN, columna, fragmentos que TODA fórmula de esa columna tiene que llevar)
    s = _num_txt
    sondas = [
        ('01', 'Weekly Log', 'C', [], None),
        ('09', 'Oil Tests', 'F', ['>%s,"CHANGE"' % s(L['aceite'][0])], 40),
        ('10', 'Water Checks', 'E', ['>=%s' % s(L['cloro'][0]), '<=%s)' % s(L['cloro'][1])], 31),
        ('16', 'Cooking & Reheating', 'H', [',%s),"REPEAT"' % s(L['recalentar'][0]), '>%s),"REPEAT"' % s(L['recalentar'][1])], 40),
        ('17', 'Cooling', 'H', ['>=%s' % s(L['caliente'][0]), '<=%s' % s(L['enfriar_2h'][0]), '<=2)', '<=%s,"OK"' % s(L['enfriar_6h'][0])], 40),
        ('17', 'Thawing', 'H', ['<=%s' % s(L['descongelar'][0]), 'IF($B$3="",%s,$B$3)' % s(L['descongelar'][1])], 40),
        ('18', 'Parasite Destruction', 'H', ['<=%s' % s(L['parasitos'][0]), 'IF($B$3="",%s,$B$3)' % s(L['parasitos'][1]),
                                             '<=%s' % s(L['parasitos_rapido'][0]), '>=%s)' % s(L['parasitos_rapido'][1])], 40),
        ('19', 'Calibration Log', 'D', ['",%s,' % s(L['termometro'][1]), '%s-IF($B$3="",0,$B$3)/%s' % (s(L['ebullicion'][0]), s(L['ebullicion'][1]))], 40),
        ('19', 'Calibration Log', 'G', ['<=%s,"PASS"' % s(L['termometro'][0])], 40),
    ]
    wbs = {}
    for es, en, corto, pes, pen in libros(carpeta):
        wbs[corto] = cargar(pen)
    for corto, hoja, col, frags, total in sondas:
        if not frags:
            continue
        fs = [c.value for c in wbs[corto][hoja]._cells.values() if c.data_type == 'f' and c.column_letter == col]
        if total is not None and len(fs) != total:
            R.fallo('%s %s!%s: %d fórmulas ≠ %d' % (corto, hoja, col, len(fs), total))
        for f in fs:
            for fr in frags:
                if fr not in f:
                    R.fallo('%s %s!%s: falta %r en %r' % (corto, hoja, col, fr, f[:90]))
                    break
            n['formulas_sondeadas'] += 1
    # 01: frío 32-41 °F (cámaras y vitrina), congelado ≤ 0 °F, caliente ≥ 135 °F (por bloque de filas)
    w1 = wbs['01']['Weekly Log']
    cuenta = Counter()
    for c in w1._cells.values():
        if c.data_type != 'f' or c.column_letter not in 'CH' or c.row > 63:
            continue
        f = c.value
        if '>=%s,' % s(L['frio'][0]) in f and '<=%s)' % s(L['frio'][1]) in f:
            cuenta['frio'] += 1
        elif '<=%s,"OK"' % s(L['congelado'][0]) in f:
            cuenta['congelado'] += 1
        elif '>=%s,"OK"' % s(L['caliente'][0]) in f:
            cuenta['caliente'] += 1
        else:
            R.fallo('01 Weekly Log!%s fórmula sin límite US: %r' % (c.coordinate, f))
    if (cuenta['frio'], cuenta['congelado'], cuenta['caliente']) != (42, 28, 14):
        R.fallo('01: frío/congelado/caliente = %r ≠ 42/28/14 (patrones del censo)' % dict(cuenta))
    n.update({'01_' + k: v for k, v in cuenta.items()})
    # LIMITES_02 (§3: 41 °F; 45 °F shellstock, shucked, leche y huevo; congelado 0 °F; ambiente N/A)
    w2 = wbs['02']['Limits']
    permitidos = {L['frio'][1], 45, L['congelado'][0], 'N/A'}
    for i, (fam, mx, base) in enumerate(mapas.LIMITES_02):
        r = 5 + i
        got = (w2['A%d' % r].value, w2['B%d' % r].value)
        if got != (fam, mx) or mx not in permitidos:
            R.fallo('02 Limits fila %d: %r ≠ %r (§3)' % (r, got, (fam, mx)))
        n['limites_02'] += 1
    # PARAMETROS (D15-D16) = LIMITES_F
    for (c, h), (et, valor, nota) in mapas.PARAMETROS.items():
        ws = wbs[c][mapas.HOJAS[h]]
        esp = L['descongelar'][1] if c == '17' else L['parasitos'][1]
        if valor != esp or ws['B3'].value != esp or ws['A3'].value != et or ws['C3'].value != nota:
            R.fallo('%s %s!A3:C3 = %r ≠ PARAMETROS/§3 %r' % (c, ws.title, (ws['A3'].value, ws['B3'].value), (et, esp)))
        n['parametros'] += 1
    # PROCESOS_16: 165/155/145/135 °F (§3-401.11) y recalentado 165 °F (§3-403.11)
    cifras = [int(re.search(r'\((\d{3}) °F\)$', p).group(1)) for p in mapas.PROCESOS_16]
    if cifras != [165, 155, 145, 135, L['recalentar'][0]]:
        R.fallo('PROCESOS_16 %r ≠ §3 (165/155/145/135 + recalentado %s)' % (cifras, L['recalentar'][0]))
    # DV_NUM: límites EN = conversión de los ES; los mensajes citan los límites EN
    for es, en, corto, pes, pen in libros(carpeta):
        for (c, h, *col), (es_b, en_b) in mapas.DV_NUM.items():
            if c != corto:
                continue
            if tuple(str(mapas.c_a_f(float(x))) for x in es_b) != en_b:
                R.fallo('DV_NUM %s %s: %r no es la conversión de %r' % (c, h, en_b, es_b))
            ws = wbs[corto][mapas.HOJAS[h]]
            for dv in ws.data_validations.dataValidation:
                if (dv.formula1, dv.formula2) != en_b or (col and not str(dv.sqref).startswith(col[0])):
                    continue
                n['dv_num'] += 1
                msg = ' '.join(x for x in (dv.error, dv.prompt) if x)
                if en_b[0] not in msg or en_b[1] not in msg or '°F' not in msg:
                    R.fallo('%s %s DV %s: el mensaje no cita %s y %s °F: %r' % (corto, ws.title, dv.sqref, en_b[0], en_b[1], msg[:100]))
    if n['dv_num'] != len(mapas.DV_NUM) + 1:          # + la DV nueva de D14 con los mismos límites
        R.fallo('DV en °F encontradas %d ≠ %d (DV_NUM + D14)' % (n['dv_num'], len(mapas.DV_NUM) + 1))
    for k, v in sorted(n.items()):
        R.dato(k, v)


# ==========================================================================
# G8 — censo-entregables y gate-no-latinos
# ==========================================================================
def gateG8(R, carpeta, datos):
    R.gate('G8 censo + no-latinos')
    real = os.path.abspath(carpeta) == os.path.abspath(A.DESTINO_REAL)
    cmds = [[sys.executable, CENSO_SCRIPT, '--only', mapas.SLUG if real else carpeta, '--fail'] + ([] if real else ['--letter']),
            [sys.executable, NO_LATINOS, '--only', mapas.SLUG if real else carpeta]]
    for cmd in cmds:
        r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, cwd=REPO)
        lineas = [x for x in r.stdout.strip().splitlines() if x.strip()]
        nombre = os.path.basename(cmd[1])
        R.dato(nombre, lineas[-1] if lineas else '')
        if r.returncode:
            R.fallo('%s exit %d: %s' % (nombre, r.returncode, ' | '.join(lineas[-6:])))


# ==========================================================================
# Autotest: cada gate tiene que cazar un defecto inyectado en una COPIA
# ==========================================================================
def _mutar(carpeta, fname, fn):
    p = os.path.join(carpeta, fname)
    wb = openpyxl.load_workbook(p)
    fn(wb)
    wb.save(p)


def _set(ws, coord, v):
    ws[coord].value = v


def _cf_colision(wb):
    ws = wb['Oil Tests']
    for cf in ws.conditional_formatting:
        for r in cf.rules:
            r.formula = [f.replace('"WATCH"', '"ALERT"') for f in r.formula]


def _lock(wb):
    from openpyxl.styles import Protection
    wb['Parasite Destruction']['B3'].protection = Protection(locked=True)


MUTACIONES = [
    ('G1', '01-food-temperature-log.xlsx', lambda wb: _set(wb['Weekly Log'], 'C7', wb['Weekly Log']['C7'].value.replace('ALERT', 'ALERTA')), 'fórmula EN'),
    ('G1', '18-parasite-destruction-log.xlsx', _lock, 'desbloqueadas'),
    ('G2', '05-receiving-checklist.xlsx', lambda wb: _set(wb['Instructions'], 'B3', 'Revisa la temperatura de cada entrega'), 'ES'),
    ('G2', '13-employee-hygiene-health-checklist.xlsx', lambda wb: _set(wb['Instructions'], 'B3', 'Keep it below 5 °C at all times'), '°C sin su °F'),
    ('G3', '06-traceability-log.xlsx', lambda wb: setattr(wb['Traceability In'].page_setup, 'paperSize', 9), 'paperSize'),
    ('G3', '11-corrective-action-log.xlsx', lambda wb: _set(wb['Corrective Actions'], 'B5', '09/07/2026'), 'no convertida'),
    ('G4', '08-allergen-matrix.xlsx', lambda wb: _set(wb['Allergen Matrix'], 'D6', 'S'), 'fuera de su DV'),
    ('G5', '09-fryer-oil-log.xlsx', _cf_colision, 'colisión'),
    ('G6', '01-food-temperature-log.xlsx', lambda wb: _set(wb['Weekly Log'], 'B9', 40), 'veredicto'),
    ('G7', '18-parasite-destruction-log.xlsx', lambda wb: _set(wb['Parasite Destruction'], 'B3', 24), 'PARAMETROS'),
]


def autotest(carpeta, mes, datos):
    ok = True
    base = ejecutar(carpeta, mes, ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'], datos, silencioso=True)
    sucios = [g for g, v in base.gates.items() if v['fallos']]
    if sucios:
        print('AUTOTEST: la carpeta base no está limpia (%s): arregla eso primero' % sucios)
        return False
    for gate, fname, fn, aguja in MUTACIONES:
        tmp = tempfile.mkdtemp(prefix='haccp-autotest-')
        try:
            for f in mapas.FICHEROS.values():
                shutil.copy2(os.path.join(carpeta, f), tmp)
            _mutar(tmp, fname, fn)
            if gate in ('G6',):
                subprocess.run([sys.executable, '-W', 'ignore', A.INJECT, os.path.join(tmp, fname)],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            R = ejecutar(tmp, mes, [gate], datos, silencioso=True)
            fallos = [f for g in R.gates.values() for f in g['fallos']]
            cazado = any(aguja.lower() in f.lower() for f in fallos)
            ok &= cazado
            print('  autotest %s %-44s %s' % (gate, fname, 'CAZADO' if cazado else 'NO CAZADO %r' % fallos[:2]))
        finally:
            shutil.rmtree(tmp)
    return ok


# ==========================================================================
# main
# ==========================================================================
GATES = OrderedDict([('G1', gateG1), ('G2', gateG2), ('G3', gateG3), ('G4', gateG4), ('G5', gateG5),
                     ('G6', gateG6), ('G7', gateG7), ('G8', gateG8)])


def cargar_datos():
    return {'censo': json.load(open(os.path.join(AQUI, 'censo_es.json'), encoding='utf-8'))}


def ejecutar(carpeta, mes, solo, datos, silencioso=False):
    R = Resultado()
    for nombre, fn in GATES.items():
        if solo and nombre not in solo:
            continue
        A.termica()
        if nombre == 'G3':
            fn(R, carpeta, datos, mes)
        else:
            fn(R, carpeta, datos)
        g = R.gates[R.actual]
        if not silencioso:
            estado = 'OK' if not g['fallos'] else 'FALLA (%d)' % len(g['fallos'])
            resumen = ' · '.join('%s=%s' % (k, v) for k, v in list(g['datos'].items())[:10] if not isinstance(v, list))
            print('%-24s %s  %s' % (R.actual, estado, resumen[:240]))
            for f in g['fallos'][:int(os.environ.get('HACCP_MAX_FALLOS', '15'))]:
                print('    - ' + f[:240])
    return R


def main():
    ap = argparse.ArgumentParser(description='Gates F2 del HACCP Food Safety Kit Pro (EN)')
    ap.add_argument('--dir', default=A.DESTINO_REAL, help='carpeta con los 21 xlsx EN (por defecto dl/<slug>)')
    ap.add_argument('--mes', default=None, help='mes de la línea de versión (por defecto, el actual)')
    ap.add_argument('--solo', default=None, help='G1,G2,… (por defecto, todos)')
    ap.add_argument('--json', default=None)
    ap.add_argument('--autotest', action='store_true')
    args = ap.parse_args()
    mes = args.mes or A.mes_por_defecto()
    datos = cargar_datos()
    carpeta = os.path.abspath(args.dir)
    if args.autotest:
        ok = autotest(carpeta, mes, datos)
        print('AUTOTEST: %s' % ('OK' if ok else 'FALLA'))
        sys.exit(0 if ok else 1)
    solo = [s.strip().upper() for s in args.solo.split(',')] if args.solo else None
    R = ejecutar(carpeta, mes, solo, datos)
    fallos = sum(len(g['fallos']) for g in R.gates.values())
    if args.json:
        with open(args.json, 'w', encoding='utf-8') as fh:
            json.dump(R.gates, fh, ensure_ascii=False, indent=1, default=str)
    print('\n%s: %d gates, %d fallos (%s)' % ('VERDE' if not fallos else 'ROJO', len(R.gates), fallos, carpeta))
    sys.exit(1 if fallos else 0)


if __name__ == '__main__':
    main()
