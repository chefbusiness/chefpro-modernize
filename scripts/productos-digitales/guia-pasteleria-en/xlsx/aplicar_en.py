#!/usr/bin/env python3
"""Capa EN sobre los 8 xlsx ES publicados de la guía Food Cost (SPEC §2, D6-D8, D12).

Trabaja sobre el XML del paquete, no con openpyxl: así se conservan byte a byte estilos, anchos, paneles,
impresión, validaciones, formato condicional, protección, nombres definidos y el GRÁFICO del cuadro de mando
(openpyxl los pierde al guardar). Cambia solo:
  - nombres de pestaña (workbook.xml, fórmulas, nombres definidos, referencias de gráfico) — SPEC §2;
  - textos de celda, literales de fórmula y de formato condicional, validaciones, pies, gráfico y docProps,
    desde textos_en/<libro>.json (índice estable de textos_es.json) + textos de celda puntuales (config);
  - entradas numéricas: conversión exacta de unidades (D8) e impuestos a 0 % (D7) — config_en.py;
  - formatos: sin «€», fechas mm/dd/yyyy; papel US Letter.
Las celdas de fórmula salen sin valor cacheado: inject_cache.py los rellena al final (el gate lo comprueba).

    python3 aplicar_en.py <dir_es> <dir_en> [libro.xlsx ...]
"""
import html
import json
import os
import re
import sys
import zipfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import config_en as C  # noqa: E402

RX_LETRA = re.compile(r'[A-Za-zÀ-ÿ]')


# --------------------------------------------------------------------------- textos
def cargar_mapas():
    es = json.load(open(os.path.join(AQUI, 'textos_es.json')))
    mapas, global_ = {}, {}
    faltan = []
    for libro, cadenas in es.items():
        base = libro[:-5]
        ruta = os.path.join(AQUI, 'textos_en', base + '.json')
        en = json.load(open(ruta)) if os.path.exists(ruta) else {}
        m = {}
        for i, s in enumerate(cadenas.keys(), 1):
            if str(i) in en:
                m[s] = en[str(i)]
        mapas[libro] = m
        for s, t in m.items():
            global_.setdefault(s, t)
    # respaldo: cadena ya traducida en otro libro (nombres de plato, rótulos comunes)
    for libro, cadenas in es.items():
        for s, lugares in cadenas.items():
            if s in mapas[libro]:
                continue
            if all(l.startswith('chart-ref') or l == 'sheetname' for l in lugares):
                continue
            if s in global_:
                mapas[libro][s] = global_[s]
            elif RX_LETRA.search(s):
                faltan.append((libro, s, lugares[0]))
    return mapas, faltan


def esc_text(s):
    s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return s.encode('ascii', 'xmlcharrefreplace').decode('ascii')


def esc_attr(s):
    return esc_text(s).replace('"', '&quot;')


# --------------------------------------------------------------------------- referencias de celda
def col2n(c):
    n = 0
    for ch in c:
        n = n * 26 + ord(ch) - 64
    return n


def n2col(n):
    s = ''
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def expandir(rango):
    if ':' not in rango:
        return [rango]
    a, b = rango.split(':')
    ca, ra = re.match(r'([A-Z]+)(\d+)', a).groups()
    cb, rb = re.match(r'([A-Z]+)(\d+)', b).groups()
    return ['%s%d' % (n2col(c), r) for c in range(col2n(ca), col2n(cb) + 1)
            for r in range(int(ra), int(rb) + 1)]


# --------------------------------------------------------------------------- fórmulas
RX_HOJA = re.compile(r"('(?:[^']|'')+'|[A-Za-z_À-ÿ][\wÀ-ÿ.]*)!")
RX_NOMBRE_SIMPLE = re.compile(r'^[A-Za-z_][A-Za-z0-9_.]*$')


class Traductor:
    def __init__(self, libro, mapa, hojas, textos_celda):
        self.libro, self.mapa, self.hojas = libro, mapa, hojas
        self.textos_celda = textos_celda
        self.faltan = []
        self.usadas = set()

    def texto(self, s, donde):
        if s in self.mapa:
            self.usadas.add(s)
            return self.mapa[s]
        if not RX_LETRA.search(s):
            return s
        self.faltan.append((donde, s))
        return s

    def hoja_ref(self, m):
        tok = m.group(1)
        citado = tok.startswith("'")
        nombre = tok[1:-1].replace("''", "'") if citado else tok
        if nombre not in self.hojas:
            return m.group(0)
        en = self.hojas[nombre]
        if citado or not RX_NOMBRE_SIMPLE.match(en):
            return "'" + en.replace("'", "''") + "'!"
        return en + '!'

    def formula(self, f, donde):
        """Reescribe referencias a hojas fuera de los literales y traduce los literales con letras."""
        out, i = [], 0
        partes = re.split(r'("(?:[^"]|"")*")', f)
        for p in partes:
            if p.startswith('"') and p.endswith('"') and len(p) >= 2:
                lit = p[1:-1].replace('""', '"')
                t = self.texto(lit, donde + ' [literal]')
                out.append('"' + t.replace('"', '""') + '"')
            else:
                out.append(RX_HOJA.sub(self.hoja_ref, p))
        return ''.join(out)


# --------------------------------------------------------------------------- hojas
RX_CELDA = re.compile(r'<c r="([A-Z]+[0-9]+)"([^>]*?)(?:/>|>(.*?)</c>)', re.S)
RX_IS = re.compile(r'^<is><t(?: xml:space="preserve")?>(.*?)</t></is>$', re.S)
RX_F = re.compile(r'^<f>(.*?)</f>(?:<v>[^<]*</v>|<v\s*/>)?$', re.S)
RX_V = re.compile(r'^<v>([^<]*)</v>$')


def fmt_num(v):
    if isinstance(v, int) or (isinstance(v, float) and v.is_integer() and abs(v) < 1e15):
        return str(int(v))
    return repr(float(v))


def procesar_hoja(xml, hoja_es, T, cfg, informe):
    num = {}
    for h, rango, op in cfg.get('num', []):
        if h == hoja_es:
            for ref in expandir(rango):
                num[ref] = op
    estilo = {}
    for h, rango, ref_estilo in cfg.get('estilo', []):
        if h == hoja_es:
            m = re.search(r'<c r="%s"[^>]*?\ss="(\d+)"' % ref_estilo, xml)
            for ref in expandir(rango):
                estilo[ref] = m.group(1)
    textos = {ref: t for (h, ref), t in cfg.get('texto', {}).items() if h == hoja_es}
    hechos_num = set()

    def celda(m):
        ref, attrs, body = m.group(1), m.group(2), m.group(3)
        if ref in estilo:
            attrs = re.sub(r'\ss="\d+"', ' s="%s"' % estilo[ref], attrs)
        if body is None:
            if ref in num:
                informe['avisos'].append('%s!%s: celda vacía con conversión' % (hoja_es, ref))
            return '<c r="%s"%s/>' % (ref, attrs)
        mi, mf, mv = RX_IS.match(body), RX_F.match(body), RX_V.match(body)
        if mi:
            s = html.unescape(mi.group(1))
            t = textos[ref] if ref in textos else T.texto(s, '%s!%s' % (hoja_es, ref))
            pres = ' xml:space="preserve"' if (t != t.strip() or '\n' in t) else ''
            body = '<is><t%s>%s</t></is>' % (pres, esc_text(t))
        elif mf:
            f = html.unescape(mf.group(1))
            f2 = T.formula(f, '%s!%s' % (hoja_es, ref))
            attrs = re.sub(r'\st="[^"]*"', '', attrs)
            body = '<f>%s</f>' % esc_text(f2)
            if ref in num:
                raise SystemExit('conversión sobre una fórmula: %s!%s' % (hoja_es, ref))
        elif mv:
            if ref in num:
                op, k = num[ref]
                v = float(mv.group(1))
                nuevo = v * k if op == 'mul' else k
                body = '<v>%s</v>' % fmt_num(nuevo)
                hechos_num.add(ref)
        elif body.strip() == '':
            pass
        else:
            raise SystemExit('celda no reconocida %s!%s: %s' % (hoja_es, ref, body[:120]))
        return '<c r="%s"%s>%s</c>' % (ref, attrs, body)

    xml = RX_CELDA.sub(celda, xml)
    sin_hacer = sorted(r for r in num if r not in hechos_num)
    if sin_hacer:
        raise SystemExit('conversión no aplicada (celda vacía o inexistente) en %s: %s' % (hoja_es, sin_hacer))
    informe['num'] += len(hechos_num)

    # validaciones
    dv_cfg = {ref: v for (h, ref), v in cfg.get('dv', {}).items() if h == hoja_es}

    def dv(m):
        attrs_txt, inner = m.group(1), m.group(2)
        attrs = dict(re.findall(r'(\w+)="([^"]*)"', attrs_txt))
        orden = re.findall(r'(\w+)="[^"]*"', attrs_txt)
        primera = attrs['sqref'].split()[0].split(':')[0]
        f1 = re.search(r'<formula1>(.*?)</formula1>', inner, re.S)
        f2 = re.search(r'<formula2>(.*?)</formula2>', inner, re.S)
        f1 = html.unescape(f1.group(1)) if f1 else None
        f2 = html.unescape(f2.group(1)) if f2 else None
        donde = '%s DV %s' % (hoja_es, primera)
        if primera in dv_cfg:
            o = dv_cfg[primera]
            if o is None:
                informe['dv_cambios'].append(donde + ': eliminada')
                return ''
            for k in ('type', 'operator'):
                if k in o:
                    if k not in attrs:
                        orden.append(k)
                    attrs[k] = o[k]
            if 'formula1' in o:
                f1 = o['formula1']
            if 'formula2' in o:
                f2 = o['formula2']
            informe['dv_cambios'].append('%s: %s' % (donde, o))
        elif f1 and f1.startswith('"'):
            items = f1.strip('"').split(',')
            f1 = '"' + ','.join(T.texto(x, donde + ' lista') for x in items) + '"'
        elif f1:
            f1 = T.formula(f1, donde)
        for k in ('error', 'errorTitle', 'prompt', 'promptTitle'):
            if k in attrs:
                attrs[k] = T.texto(html.unescape(attrs[k]), '%s %s' % (donde, k))
                lim = 32 if k.endswith('Title') else 255
                if len(attrs[k]) > lim:
                    raise SystemExit('%s %s > %d caracteres: %r' % (donde, k, lim, attrs[k]))
            else:
                attrs.pop(k, None)
        if f1 and f1.startswith('"') and len(f1) > 257:
            raise SystemExit('%s: lista > 255 caracteres' % donde)
        out = '<dataValidation ' + ' '.join('%s="%s"' % (k, esc_attr(attrs[k]) if k in
                                             ('error', 'errorTitle', 'prompt', 'promptTitle') else attrs[k])
                                             for k in orden) + '>'
        if f1 is not None:
            out += '<formula1>%s</formula1>' % esc_text(f1)
        if f2 is not None:
            out += '<formula2>%s</formula2>' % esc_text(f2)
        return out + '</dataValidation>'

    xml = re.sub(r'<dataValidation ([^>]*)>(.*?)</dataValidation>', dv, xml, flags=re.S)
    m = re.search(r'<dataValidations count="(\d+)">(.*?)</dataValidations>', xml, re.S)
    if m:
        n = len(re.findall(r'<dataValidation ', m.group(2)))
        xml = xml.replace(m.group(0), '<dataValidations count="%d">%s</dataValidations>' % (n, m.group(2))
                          if n else '')

    # formato condicional
    xml = re.sub(r'<formula>(.*?)</formula>',
                 lambda mm: '<formula>%s</formula>' % esc_text(T.formula(html.unescape(mm.group(1)),
                                                                          hoja_es + ' CF')), xml, flags=re.S)

    # cabeceras y pies
    def hf(mm):
        t = html.unescape(mm.group(2))
        for a, b in C.HF:
            t = t.replace(a, b)
        return '<%s>%s</%s>' % (mm.group(1), esc_text(t), mm.group(1))
    xml = re.sub(r'<(oddHeader|oddFooter|evenHeader|evenFooter|firstHeader|firstFooter)>(.*?)</\1>', hf, xml,
                 flags=re.S)
    # papel US Letter
    xml = re.sub(r'(<pageSetup[^>]*?)paperSize="\d+"', r'\1paperSize="%s"' % C.PAPEL_LETTER, xml)
    return xml


# --------------------------------------------------------------------------- libro
def procesar_libro(ruta_es, ruta_en, mapas):
    libro = os.path.basename(ruta_es)
    cfg = C.LIBROS[libro]
    hojas = cfg['hojas']
    T = Traductor(libro, mapas[libro], hojas, cfg.get('texto', {}))
    informe = {'libro': libro, 'num': 0, 'dv_cambios': [], 'avisos': []}
    z = zipfile.ZipFile(ruta_es)
    partes = [(i, z.read(i.filename)) for i in z.infolist()]
    datos = {i.filename: d for i, d in partes}

    wb = datos['xl/workbook.xml'].decode('utf-8')
    rels = datos['xl/_rels/workbook.xml.rels'].decode('utf-8')
    relmap = {re.search(r'Id="([^"]+)"', r).group(1): re.search(r'Target="([^"]+)"', r).group(1)
              for r in re.findall(r'<Relationship [^>]*/>', rels)}
    hoja_parte = {}
    for mm in re.finditer(r'<sheet [^>]*name="([^"]+)"[^>]*r:id="([^"]+)"', wb):
        nombre = html.unescape(mm.group(1))
        tgt = relmap[mm.group(2)]
        hoja_parte[nombre] = tgt.lstrip('/') if tgt.startswith('/') else 'xl/' + tgt
    if set(hoja_parte) != set(hojas):
        raise SystemExit('%s: pestañas %s ≠ mapa %s' % (libro, list(hoja_parte), list(hojas)))

    nuevos = {}
    for nombre, parte in hoja_parte.items():
        nuevos[parte] = procesar_hoja(datos[parte].decode('utf-8'), nombre, T, cfg, informe)

    def renombrar(mm):
        return '<sheet %sname="%s"' % (mm.group(1), esc_attr(hojas[html.unescape(mm.group(2))]))
    wb = re.sub(r'<sheet ([^>]*?)name="([^"]+)"', renombrar, wb)
    wb = re.sub(r'(<definedName [^>]*>)(.*?)(</definedName>)',
                lambda mm: mm.group(1) + esc_text(T.formula(html.unescape(mm.group(2)), 'definedName'))
                + mm.group(3), wb, flags=re.S)
    nuevos['xl/workbook.xml'] = wb

    st = datos['xl/styles.xml'].decode('utf-8')
    def formato(mm):
        code = html.unescape(mm.group(1))
        nuevo = C.FORMATOS.get(code, code)
        nuevo = re.sub(r'[\s\u00a0\u202f]*(€|\[\$€[^\]]*\]|"€")[\s\u00a0\u202f]*', '', nuevo)
        if nuevo != code:
            informe['formatos'] = informe.get('formatos', []) + ['%s -> %s' % (code, nuevo)]
        return 'formatCode="%s"' % esc_attr(nuevo)
    st = re.sub(r'formatCode="([^"]*)"', formato, st)
    nuevos['xl/styles.xml'] = st

    for parte in datos:
        if parte.startswith('xl/charts/') and parte.endswith('.xml'):
            x = datos[parte].decode('utf-8')
            x = re.sub(r'<a:t>(.*?)</a:t>', lambda mm: '<a:t>%s</a:t>' % esc_text(
                T.texto(html.unescape(mm.group(1)), parte)), x, flags=re.S)
            for tag in ('f', 'c:f'):
                x = re.sub(r'<%s>(.*?)</%s>' % (tag, tag), lambda mm, tag=tag: '<%s>%s</%s>' % (
                    tag, esc_text(T.formula(html.unescape(mm.group(1)), parte)), tag), x, flags=re.S)
            nuevos[parte] = x

    core = datos['docProps/core.xml'].decode('utf-8')
    for tag, val in (('dc:title', cfg['titulo']), ('dc:subject', C.ASUNTO), ('dc:creator', C.AUTOR),
                     ('cp:lastModifiedBy', C.AUTOR)):
        core = re.sub(r'(<%s[^>]*>)(.*?)(</%s>)' % (tag, tag), lambda mm: mm.group(1) + esc_text(val)
                      + mm.group(3), core, flags=re.S)
    core = re.sub(r'(<dcterms:modified[^>]*>)(.*?)(</dcterms:modified>)', r'\g<1>%s\3' % C.FECHA_MOD, core)
    nuevos['docProps/core.xml'] = core

    os.makedirs(os.path.dirname(ruta_en), exist_ok=True)
    tmp = ruta_en + '.tmp'
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zo:
        for info, d in partes:
            d2 = nuevos.get(info.filename)
            zo.writestr(info, d2.encode('utf-8') if isinstance(d2, str) else d)
    os.replace(tmp, ruta_en)
    informe['faltan'] = T.faltan
    return informe


def main():
    dir_es, dir_en = sys.argv[1], sys.argv[2]
    libros = sys.argv[3:] or list(C.LIBROS)
    mapas, faltan = cargar_mapas()
    errores = 0
    for libro, s, donde in faltan:
        print('SIN TRADUCCIÓN (censo) %s · %s · %r' % (libro, donde, s[:90]))
        errores += 1
    for libro in libros:
        inf = procesar_libro(os.path.join(dir_es, libro), os.path.join(dir_en, C.LIBROS[libro]['out']), mapas)
        print('%s -> %s: %d entradas numéricas cambiadas; DV cambiadas: %d' % (
            libro, C.LIBROS[libro]['out'], inf['num'], len(inf['dv_cambios'])))
        for d in inf['dv_cambios']:
            print('   DV', d)
        for a in inf.get('formatos', []):
            print('   FORMATO', a)
        for a in inf['avisos']:
            print('   AVISO', a)
        for donde, s in inf['faltan']:
            print('   SIN TRADUCCIÓN %s: %r' % (donde, s[:90]))
            errores += 1
    print('ERRORES: %d' % errores)
    sys.exit(1 if errores else 0)


if __name__ == '__main__':
    main()
