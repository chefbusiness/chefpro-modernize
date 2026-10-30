#!/usr/bin/env python3
"""parche_xml_xlsx.py — arreglos en los xlsx publicados tocando SOLO el XML de lo que cambia.

Por qué XML y no openpyxl: openpyxl reescribe el libro entero, tira las cachés <v> de las fórmulas (hay que pasar
después `inject_cache.py`) y, al reaplicarse, duplica desplegables (RD-17). Aquí se reescribe únicamente el contenido de
los elementos que cambian; el resto del zip viaja byte a byte con el mismo orden y la misma compresión.

1. LIT255 — Excel limita a 255 caracteres CADA literal de texto de una fórmula (el token ptgStr guarda la longitud en
   un byte; al teclearlo avisa «Text values in formulas are limited to 255 characters»): un literal más largo en un
   fichero obliga a Excel a reparar el libro al abrirlo. Se trocea en «"…"&"…"»: mismo valor, misma caché.
2. TEXTOS — sustituciones exactas de la tabla ARREGLOS en <t>, <f>, <v>, <formula1> y en los atributos prompt/error
   de las <dataValidation>; cada una limitada a los ficheros que casan con su patrón.

Uso (raíz del repo):
  python parche_xml_xlsx.py [--apply] [--check] [ficheros…]   (sin ficheros: astro-site/public/dl/**/*.xlsx)
  sin --apply = simulación (informa y no escribe) · --check = exit 1 si queda algún literal > 255 (gate de producto)
Importable: `partir_literales(formula)` y `parchear(ruta, apply=True)` para los generadores.
Sesión Claude Code, 30-oct-2026 (tanda de arreglos sin correo).
"""
import fnmatch
import glob
import html
import os
import re
import sys
import zipfile

MAX_LIT = 255
TROZO = 240          # margen bajo el límite: cada trozo mide como mucho esto (en caracteres del VALOR)

# (patrón de ruta, texto viejo, texto nuevo). Patrón fnmatch sobre la ruta relativa a dl/.
CHECKLISTS_ES_22 = ('plan-catering-tematico-eventos/checklist-*', 'plan-negocio-finca-eventos-bodas/checklist-*',
                    'plan-negocio-heladeria/checklist-*', 'plan-negocio-paellero-eventos/checklist-*',
                    'plan-negocio-parrillero-asador-eventos/checklist-*', 'plan-negocio-pizzeria/checklist-*',
                    'plan-negocio-polleria/checklist-*', 'plan-negocio-taqueria/checklist-*')
ARREGLOS = []
for _p in CHECKLISTS_ES_22:
    # Desplegable «✓,—,N/A» sobre celdas «☐» con leyenda «☐ (pendiente)»: la lista pasa a ✓,☐,N/A (como en los EN).
    ARREGLOS += [(_p, '"✓,—,N/A"', '"✓,☐,N/A"'),
                 (_p, 'Usa el desplegable: ✓, —, N/A.', 'Usa el desplegable: ✓, ☐, N/A.')]
ARREGLOS += [
    ('pizza-shop-business-plan/pizza-shop-startup-checklist.xlsx',
     'Use the dropdown: ✓, —, N/A. ✓ = done, — = pending,', 'Use the dropdown: ✓, ☐, N/A. ✓ = done, ☐ = pending,'),
    # Holgura = previstos/equilibrio − 1: mide cuánto estás POR ENCIMA del equilibrio; la caída que aguantas es h/(1+h).
    ('*', 'Cuánto puedes caer sobre lo previsto antes de entrar en pérdidas',
     'Cuánto deben superar las ventas previstas a las del punto de equilibrio. La caída que aguantas antes de entrar '
     'en pérdidas es algo menor: con un 15 % de holgura, un 13 % de lo previsto'),
    ('*', 'Cuánto puedes caer antes de no poder pagar los costes fijos y la cuota.',
     'Cuánto superan tus ventas previstas a las del equilibrio de caja. La caída que aguantas antes de no poder pagar '
     'los costes fijos y la cuota es algo menor: con un 25 % de holgura, un 20 %.'),
    ('*', 'Cuánto puedes caer sobre lo previsto antes de no poder pagar los fijos y la cuota.',
     'Cuánto superan tus ventas previstas a las del equilibrio de caja. La caída que aguantas antes de no poder pagar '
     'los fijos y la cuota es algo menor: con un 25 % de holgura, un 20 %.'),
    ('plan-negocio-taqueria/checklist-apertura-taqueria.xlsx',
     '(RD 919/2006, ITC-ICG 08). Apunta la', '(RD 919/2006, ITC-ICG 07 e ITC-ICG 08). Apunta la'),
    # Ronda 2 (revisión adversarial 30-oct): la holgura mínima de B67 se compara con la holgura de CAJA (costes fijos y
    # cuota), no con las pérdidas contables; y el mismo defecto en los planes EN.
    ('*', 'Cuánto deben superar las ventas previstas a las del punto de equilibrio. La caída que aguantas antes de entrar '
          'en pérdidas es algo menor: con un 15 % de holgura, un 13 % de lo previsto',
     'Cuánto deben superar las ventas previstas a las del equilibrio de caja (costes fijos y cuota del préstamo). La '
     'caída que aguantas es algo menor: con un 15 % de holgura, un 13 % de lo previsto'),
    ('*', 'How far you can fall below plan before you start losing money',
     'How far planned sales must sit above cash break-even (fixed costs and the loan payment). The drop you can absorb '
     'is somewhat smaller: with a 15% cushion, about 13% of plan'),
    ('*', 'How far you can fall before you cannot pay the fixed costs and the loan payment.',
     'How far planned sales sit above cash break-even. The drop you can absorb before you cannot pay the fixed costs '
     'and the loan payment is somewhat smaller: with a 25% cushion, 20%.'),
    ('*', 'Fourth-quarter sales tax is settled in January of the following year, so it does not appear in this table.',
     'Fourth-quarter sales tax is settled in Month 13 (January of the following year when Month 1 is January), so it '
     'does not appear in this table.'),
    # Planes EN anteriores al Ice Cream: los meses sólo eran exactos con el Mes 1 en enero.
    ('*', 'The model settles quarterly (April, July, October, January):',
     'The model settles quarterly, in the month after each plan quarter (Months 4, 7 and 10, and the fourth quarter '
     'in Month 13: April, July, October and January when Month 1 is January):'),
]


# --------------------------------------------------------------------------- literales
def _segmentos(formula):
    """[(es_literal, texto_crudo)] — los literales sin las comillas exteriores, con sus «""» internos tal cual."""
    out, i, n, buf = [], 0, len(formula), ''
    while i < n:
        ch = formula[i]
        if ch == '"':
            if buf:
                out.append((False, buf))
                buf = ''
            j, lit = i + 1, ''
            while j < n:
                if formula[j] == '"':
                    if j + 1 < n and formula[j + 1] == '"':
                        lit += '""'
                        j += 2
                        continue
                    break
                lit += formula[j]
                j += 1
            if j >= n:                       # comilla sin cerrar: no es una fórmula que sepamos tocar
                raise ValueError('literal sin cerrar')
            out.append((True, lit))
            i = j + 1
        elif ch == "'":                      # nombre de hoja entre comillas simples ('' = comilla escapada)
            j = i + 1
            while j < n:
                if formula[j] == "'":
                    if j + 1 < n and formula[j + 1] == "'":
                        j += 2
                        continue
                    break
                j += 1
            buf += formula[i:j + 1]
            i = j + 1
        else:
            buf += ch
            i += 1
    if buf:
        out.append((False, buf))
    return out


def _valor(lit):
    return lit.replace('""', '"')


def _largo(lit):
    """Longitud en unidades UTF-16, como la cuenta Excel (un emoji fuera del BMP son 2)."""
    return len(_valor(lit).encode('utf-16-le')) // 2


def _trocear(lit):
    """Trozos crudos de `lit` con un valor ≤ TROZO cada uno; corta tras un espacio si lo hay cerca; nunca parte «""»."""
    trozos, actual, i = [], '', 0
    while i < len(lit):
        tok = '""' if lit.startswith('""', i) else lit[i]
        if _largo(actual) + 2 > TROZO:
            k = actual.rfind(' ')
            if k >= TROZO // 2:
                trozos.append(actual[:k + 1])
                actual = actual[k + 1:]
            else:
                trozos.append(actual)
                actual = ''
        actual += tok
        i += len(tok)
    trozos.append(actual)
    return trozos


def partir_literales(formula):
    """Devuelve la fórmula (sin escapar XML) con los literales > 255 troceados, o la misma si no hace falta."""
    segs = _segmentos(formula)
    if not any(es and _largo(t) > MAX_LIT for es, t in segs):
        return formula
    if any(not es and '{' in t for es, t in segs):
        raise ValueError('constante de matriz: un literal no se puede trocear con &')
    out = []
    for es, t in segs:
        if es and _largo(t) > MAX_LIT:
            out.append('&'.join('"' + p + '"' for p in _trocear(t)))
        elif es:
            out.append('"' + t + '"')
        else:
            out.append(t)
    nueva = ''.join(out)
    assert _sin_trocear(nueva) == _sin_trocear(formula)
    return nueva


def _sin_trocear(formula):
    """Forma normal: los «"a"&"b"» se funden en un literal. Dos fórmulas que sólo difieren en el troceo dan lo mismo."""
    out = []
    for es, t in _segmentos(formula):
        if es and len(out) >= 2 and out[-1] == (False, '&') and out[-2][0]:
            out.pop()
            out[-1] = (True, out[-1][1] + _valor(t))
        else:
            out.append((es, _valor(t) if es else t))
    return out


def fundir_literales(formula):
    """Inverso del troceo: «"a"&"b"» → «"ab"» (mismo valor). Para los circuitos que buscan cada literal ES por su clave
    o comparan fórmulas con un registro escrito sin trocear (business-plans-en: aplicar_en, gates_en, extraer_textos)."""
    try:
        segs = _segmentos(formula)
    except ValueError:
        return formula
    out = []
    for es, t in segs:
        if es and len(out) >= 2 and out[-1] == (False, '&') and out[-2][0]:
            out.pop()
            out[-1] = (True, out[-1][1] + t)
        else:
            out.append((es, t))
    return ''.join('"' + t + '"' if es else t for es, t in out)


def literales_largos(formula):
    try:
        return [_largo(t) for es, t in _segmentos(formula) if es and _largo(t) > MAX_LIT]
    except ValueError:
        return []


# --------------------------------------------------------------------------- XML
def _escapar(texto, original, atributo=False):
    s = texto.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    if atributo:
        s = s.replace('"', '&quot;').replace('\n', '&#10;').replace('\r', '&#13;').replace('\t', '&#9;')
    if '&#' in original:                     # respetar el estilo del fichero (referencias numéricas para lo no ASCII)
        s = ''.join(c if ord(c) < 128 else '&#%d;' % ord(c) for c in s)
    return s


def _sustituir(texto, reglas):
    usadas = []
    for k, viejo, nuevo in reglas:
        if viejo in texto:
            texto = texto.replace(viejo, nuevo)
            usadas.append(k)
    return texto, usadas


RX_ELEM = re.compile(r'(<(f|t|v|formula1)(?:\s[^>]*?)?(?<!/)>)(.*?)(</\2>)', re.S)   # nunca <f …/> (compartida)
RX_DV_TAG = re.compile(r'<dataValidation\b[^>]*>')
RX_DV_ATTR = re.compile(r'(\s(?:prompt|error)=")([^"]*)(")')


def parchear_xml(xml, reglas, informe, nombre):
    def elem(m):
        abre, tag, crudo, cierra = m.group(1), m.group(2), m.group(3), m.group(4)
        texto = html.unescape(crudo)
        nuevo, usadas = _sustituir(texto, reglas)
        for k in usadas:
            informe.append('%s <%s> regla %d' % (nombre, tag, k))
        if tag == 'f':
            try:
                partido = partir_literales(nuevo)
            except ValueError as e:
                informe.append('%s AVISO %s: %s' % (nombre, e, nuevo[:60]))
                partido = nuevo
            if partido != nuevo:
                informe.append('%s LIT255 %s' % (nombre, literales_largos(nuevo)))
            nuevo = partido
        if nuevo == texto:
            return m.group(0)
        return abre + _escapar(nuevo, crudo) + cierra

    def attr(m):
        texto = html.unescape(m.group(2))
        nuevo, usadas = _sustituir(texto, reglas)
        for k in usadas:
            informe.append('%s <dv@> regla %d' % (nombre, k))
        return m.group(0) if nuevo == texto else m.group(1) + _escapar(nuevo, m.group(2), True) + m.group(3)

    xml = RX_ELEM.sub(elem, xml)
    return RX_DV_TAG.sub(lambda m: RX_DV_ATTR.sub(attr, m.group(0)), xml)


def parchear(ruta, apply=False, rel=None):
    rel = rel or os.path.basename(ruta)
    reglas = [(k, v, n) for k, (pat, v, n) in enumerate(ARREGLOS) if fnmatch.fnmatch(rel, pat)]
    informe = []
    with zipfile.ZipFile(ruta) as zin:
        entradas = [(i, zin.read(i.filename)) for i in zin.infolist()]
    cambios = {}
    for info, data in entradas:
        if not re.match(r'xl/(worksheets/sheet\d+|sharedStrings)\.xml$', info.filename):
            continue
        xml = data.decode('utf-8')
        nuevo = parchear_xml(xml, reglas, informe, info.filename.rsplit('/', 1)[1])
        if nuevo != xml:
            cambios[info.filename] = nuevo.encode('utf-8')
    if cambios and apply:
        tmp = ruta + '.tmp'
        with zipfile.ZipFile(tmp, 'w') as zout:
            for info, data in entradas:
                zout.writestr(info, cambios.get(info.filename, data), compress_type=info.compress_type)
        os.replace(tmp, ruta)
    return informe, sorted(cambios)


def quedan_largos(ruta):
    largos = []
    with zipfile.ZipFile(ruta) as z:
        for n in z.namelist():
            if re.match(r'xl/worksheets/sheet\d+\.xml$', n):
                for m in re.finditer(r'<f(?:\s[^>]*)?>(.*?)</f>', z.read(n).decode('utf-8'), re.S):
                    for L in literales_largos(html.unescape(m.group(1))):
                        largos.append('%s(%d)' % (n.rsplit('/', 1)[1], L))
    return largos


def main(argv):
    apply, check = '--apply' in argv, '--check' in argv
    rutas = [a for a in argv if not a.startswith('--')]
    base = 'astro-site/public/dl/'
    if not rutas:
        rutas = sorted(glob.glob(base + '**/*.xlsx', recursive=True))
    total, fallos, usos = 0, [], dict.fromkeys(range(len(ARREGLOS)), 0)
    for r in rutas:
        rel = r.split(base, 1)[1] if base in r else os.path.basename(r)
        if apply or not check:
            informe, partes = parchear(r, apply=apply, rel=rel)
            for linea in informe:
                m = re.search(r' regla (\d+)$', linea)
                if m:
                    usos[int(m.group(1))] += 1
            if partes:
                total += 1
                print('%s %s: %d cambios en %s' % ('APLICADO' if apply else 'SIMULADO', rel, len(informe),
                                                  ','.join(p.rsplit('/', 1)[1] for p in partes)))
                for linea in informe:
                    print('    ' + linea)
        if check:
            largos = quedan_largos(r)
            if largos:
                fallos.append('%s: %s' % (rel, ', '.join(largos[:6])))
    print('ficheros con cambios: %d de %d' % (total, len(rutas)))
    if apply or not check:
        for k, (pat, viejo, _) in enumerate(ARREGLOS):
            print('  regla %2d [%s] «%s…»: %d' % (k, pat[:28], viejo[:34], usos[k]))
    if check:
        for f in fallos:
            print('ROJO literal > 255: ' + f)
        print('gate LIT255: %s (%d ficheros con literales > 255)' % ('VERDE' if not fallos else 'ROJO', len(fallos)))
        return 1 if fallos else 0
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
