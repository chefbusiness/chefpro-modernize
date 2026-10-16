#!/usr/bin/env python3
"""Gate de una tanda traducida de la guía «How to Open a Pastry Shop» EN (SPEC §4-§5).

Copia del gate de la guía Food Cost EN (`guia-food-cost-en/gate_md_en.py`) con el plan de tandas
de `split_md.py`; las tandas de readaptación US (ADAPT) tratan las cifras ausentes como aviso.

Compara `tandas/es/<T>.md` con `tandas/en/<T>.md`:
  ERRORES  a. encabezados (nº, nivel y orden) y separadores `---` (saltos de página)
           b. tablas (nº, filas y columnas por fila; `\\|` rompe la tabla en el render)
           c. ítems de lista por sección (viñeta y numerada por separado, tolerancia 0)
           d. residuo de español: ¿ ¡ « » º ª, letras acentuadas fuera de la lista blanca,
              términos prohibidos (IVA, €, euros, albarán, escandallo, TPV…), palabras
              centinela y densidad de palabras funcionales por párrafo
           e. caracteres de escrituras no latinas
           f. caracteres que Helvetica/WinAnsi no pinta (documentos.parsear + sanear_bloques
              + restos_no_winansi): lo que `sanear` borra o degrada sin estar en MAPA_WINANSI
           g. nombres de fichero ES; todo `.xlsx` citado debe estar en la columna EN de SPEC §2
           h. marcas ⟦ADAPT…⟧ (aviso; error con --final)
           i. ratio de palabras EN/ES < 0,6 (truncado)
           j. cifras de dinero (€) y % del ES que no aparecen en el EN (aviso en las tandas
              fiscales T02/T08/B02, con --fiscal o junto a un contexto de IVA: D7)
  AVISOS   ratio fuera de 0,8-1,3 · pestañas entre comillas que no están en SPEC §2 · «entrée»
           · Spain/Spanish · nombres de producto españoles (jamón, ibérico) · otras cifras ausentes.

    python3 gate_md_en.py --tanda T02 [--final] [--fiscal] [--en otro.md] [--avisos]
    python3 gate_md_en.py --todas [--final]
    python3 gate_md_en.py --autotest     # se valida a sí mismo: ES como EN + corpus EN del blog

Sale con 0 si no hay errores y 1 si los hay. Sólo lee texto: < 1 s por tanda.
"""
import argparse
import collections
import re
import sys
import time
import unicodedata
from decimal import Decimal, InvalidOperation
from pathlib import Path

AQUI = Path(__file__).resolve().parent
TANDAS_ES = AQUI / 'tandas' / 'es'
TANDAS_EN = AQUI / 'tandas' / 'en'
SPEC = AQUI / 'SPEC.md'
REPO = AQUI.parents[2]
sys.path.insert(0, str(AQUI.parent / 'guias-v2_0'))
import documentos as D  # noqa: E402  — importarlo sólo define funciones y constantes

from split_md import TANDAS as _PLAN, ADAPT, ORFANOS  # noqa: E402
TANDAS = [t for plan in _PLAN.values() for t, _ in plan]
TANDAS_FISCALES = set(ADAPT)       # SPEC §4: tandas que se readaptan a EE. UU. (cifras ausentes = aviso)
ORFANOS_ES = set(ORFANOS)          # ficheros ES citados que no tienen EN (SPEC §2)

# --------------------------------------------------------------------------
# Listas del residuo de español (ampliables)
# --------------------------------------------------------------------------
CHARS_ES = '¿¡«»ºª'
# Préstamos que el inglés escribe con tilde (en minúsculas)
PRESTAMOS = {
    'café', 'cafés', 'sauté', 'sautés', 'sautéed', 'sautéing', 'entrée', 'entrées', 'purée',
    'purées', 'puréed', 'jalapeño', 'jalapeños', 'crème', 'brûlée', 'brûlées', 'consommé',
    'flambé', 'flambéed', 'soufflé', 'soufflés', 'rosé', 'rosés', 'frappé', 'canapé',
    'canapés', 'pâté', 'glacé', 'piña', 'añejo', 'añejos', 'albariño', 'albariños', 'ximénez',
    'résumé', 'décor', 'cliché', 'protégé', 'rémy', 'nestlé', 'crémant', 'béarnaise',
    'béchamel', 'velouté', 'rémoulade', 'frisée', 'mâché', 'émincé', 'gratiné', 'éclair',
    'fumé', 'tourné', 'macédoine', 'sémillon', 'pétrus', 'gruyère', 'communiqué', 'praliné',
    'génoise', 'sablé', 'brisée', 'sucrée', 'feuilleté', 'crémeux', 'détrempe',
    'bacardí', 'kahlúa', 'pâtisserie', 'pâtisseries', 'pâte', 'pâtissier', 'pâtissiers', 'crêpe',
    'crêpes', 'éclairs', 'glaçage', 'ensaïmada', 'ensaïmadas', 'quinceañera', 'quinceañeras', 'piñata',
    'piñatas', 'crème', 'brûlée', 'opéra', 'chantilly', 'pâtes', 'choux', 'financier', 'dacquoise',
    'día', 'turrón', 'turrones', 'buñuelo', 'buñuelos'}   # nombres fijados en DECISIONES §4 y §6
# (el plural en -s de cualquiera de ellas también vale: «canapés», «pâtés», «éclairs»)
# Nombres de producto españoles que un menú de EE. UU. puede conservar: aviso, no error
NOMBRES_PRODUCTO = {'jamón', 'ibérico', 'ibérica', 'ibéricos', 'ibéricas', 'manchego'}
RX_ACENTO = re.compile(r'\w*[áéíóúñÁÉÍÓÚÑ]\w*')
RX_PROHIBIDAS = re.compile(
    r'(?<!\w)(IVA|BOE|euros?|EUR|albar[aá]n(?:es)?|escandall\w*|Hacienda|Seguridad Social|'
    r'aut[oó]nom[oa]s?|convenios?|ticket medio|TPV|Espa[ñn]a|ayuntamientos?|BOCM|RGSEAA|APPCC|'
    r'CCAA|Registro Sanitario|comunidad(?:es)? aut[oó]nomas?|pasteler[ií]as?|roscones|rosc[oó]n)(?!\w)', re.I)
# Palabras que el inglés no usa nunca sueltas (las ambiguas —de, la, en, con, sin, son— no)
CENTINELAS = set("""
    que los las del una unos unas para según también cómo qué cuál cuánto receta recetas cocina
    plato platos carta hostelería cada desde entre sobre cliente clientes negocio precio precios
    coste costes merma mermas obrador comensal comensales venta ventas compra compras bebida
    bebidas ración raciones hoja hojas bruto bruta neto neta margen porque cuando pero este esta
    estos estas tiene tienen puede pueden mismo misma donde meses año años día días semana
    proveedor proveedores ingrediente ingredientes ejemplo tipo tipos cerveza refresco refrescos
    cubierto cubiertos nuestro nuestra aquí siempre nunca sólo muy menos mejor hacer hace está
    están porcentaje cifra cifras dato datos celda celdas fórmula columna columnas fila filas
    libro libros sala mes producto productos tal""".split())
RX_CENTINELA = re.compile(r'\b(%s)\b' % '|'.join(sorted(CENTINELAS)), re.I)
FUNCIONALES = {'de', 'la', 'el', 'los', 'las', 'que', 'para', 'con', 'del', 'por', 'una', 'un',
               'y', 'en', 'es', 'se', 'al', 'lo', 'como', 'más'}
# Expresiones que el inglés usa tal cual y llevan palabras «españolas»: se quitan antes de medir
RX_PERMITIDAS = re.compile(
    r"(à la carte|a la carte|à la|mise en place|de minimis|ribera del duero|los angeles|"
    r"las vegas|el paso|santa fe|pedro ximénez|chili con carne|pico de gallo|dulce de leche|"
    r"tres leches|crème de la crème|crème de|fleur de sel|en route|en papillote|sous vide|"
    r"al dente|al pastor|al fresco|chef de partie|chef de cuisine|garde manger|pan de|"
    r"pâte de|vin de|eau de|del monte|y-axis|x-axis|\bx and y\b|día de los muertos|día de reyes|"
    r"día de las madres|rosca de reyes|huesos de santo|mona de pascua|buñuelos de viento|pan de muerto)", re.I)
RX_LETRAS = re.compile(r'[^\W\d_]+')
RX_MARCA = re.compile(r'⟦[^⟧\n]*⟧?')

# --------------------------------------------------------------------------
# Cifras (D6: € → $ 1:1, % intacto; D8: magnitudes con unidad se convierten)
# --------------------------------------------------------------------------
RX_NUM_ES = re.compile(r'(?<![\w.,/])(\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+(?:,\d+)?)(?!\w|[.,]\d)')
RX_NUM_EN = re.compile(r'(?<![\w.,/])(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)(?!\w|[.,]\d)')
RX_TRAS_PCT = re.compile(r'\s?%')
RX_TRAS_EUR = re.compile(r'\s?(€|euros?(?!\w)|EUR(?!\w))')
RX_TRAS_UNIDAD = re.compile(
    r'\s?(?:(?:kg|g|gr|mg|ml|cl|dl|l|L|litros?|kilos?|kilogramos?|gramos?|cm|mm|m²|m2|m³/h|m3/h|metros?(?: cuadrados)?)(?!\w)|[°º]\s?C?)')
RX_POR_UNIDAD = re.compile(r'\s?/\s?(kg|g|l|L|litros?|kilos?|ml|cl)(?!\w)')
RX_RANGO = re.compile(r'\s?[-–‑]\s?(\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+(?:,\d+)?)')
RX_CTX_UNIDAD = re.compile(r'\b(kilos?|kg|litros?|gramos?|kilogramos?)\b|/\s?(kg|l)\b', re.I)
# En la etiqueta de una fila sólo cuenta si es «por unidad» («Precio por kg (€)»), no «(1,2 kg)»
RX_CTX_UNIDAD_FILA = re.compile(r'/\s?(kg|g|l|litros?|kilos?)\b|\bpor (kilo|kg|litro)|'
                                r'\((kg|g|ml|cl|l)\)', re.I)
RX_SIN_IVA = re.compile(r'(sin|antes de|neto de|excluido el|excl\.?)\s+(el\s+)?IVA|IVA excluido|'
                        r'sin impuestos', re.I)
RX_CTX_FISCAL = re.compile(r'\bIVA\b|impuest|recargo|tribut|Hacienda|'
                           r'\btipos? (general|reducido|superreducido)', re.I)
# Citas legales y fechas del ES (D10: se quitan o generalizan): no son «otras cifras» que buscar
RX_LEGAL_ANTES = re.compile(r'(arts?\.|artículos?|apartado|número|Ley|RDL?|Real Decreto|consulta|'
                            r'modelo)\s*(\d+\s*(y|,)\s*)?$', re.I)
RX_FECHA_TRAS = re.compile(r'^\s+de\s+(enero|febrero|marzo|abril|mayo|junio|julio|agosto|'
                           r'septiembre|octubre|noviembre|diciembre)', re.I)
RX_FUERA_CIFRAS = re.compile(r'[\w./-]+\.(?:xlsx|docx|pdf)\b|https?://\S+|aichef\.pro/\S*')


def dec(s, idioma):
    """Cadena numérica → Decimal (ES 1.234,56 · EN 1,234.56)."""
    try:
        if idioma == 'es':
            return Decimal(s.replace('.', '').replace(',', '.'))
        return Decimal(s.replace(',', ''))
    except InvalidOperation:
        return None


def fmt(v):
    t = format(v.normalize(), 'f') if v is not None else '?'
    return t


# --------------------------------------------------------------------------
# Lectura: réplica de documentos.parsear() con número de línea por bloque
# --------------------------------------------------------------------------
RX_UL = re.compile(r'^\s*[-*]\s+')
RX_OL = re.compile(r'^\s*\d+\.\s+')
RX_SEP = re.compile(r'^\s*\|?[\s:|-]+\|?\s*$')


def parsear_con_lineas(md):
    """Mismos bloques que documentos.parsear() (el autotest lo comprueba) + línea 1-based.
    Las tablas guardan además las filas crudas para contar celdas con `\\|` escapado."""
    lineas = md.split('\n')
    out = []
    i, n = 0, len(lineas)
    while i < n:
        linea = lineas[i].rstrip()
        ini = i + 1
        if not linea.strip():
            i += 1
            continue
        if linea.strip() == '---':
            out.append(('hr', None, ini)); i += 1; continue
        m = re.match(r'^(#{1,4}) ', linea)
        if m:
            out.append(('h%d' % len(m.group(1)), linea[len(m.group(1)) + 1:].strip(), ini))
            i += 1
            continue
        if linea.strip().startswith('```'):
            codigo = []
            i += 1
            while i < n and not lineas[i].strip().startswith('```'):
                codigo.append(lineas[i]); i += 1
            i += 1
            out.append(('code', '\n'.join(codigo), ini))
            continue
        if linea.strip().startswith('|') and i + 1 < n and RX_SEP.match(lineas[i + 1]) \
                and '-' in lineas[i + 1]:
            filas = [linea]
            i += 2
            while i < n and lineas[i].strip().startswith('|'):
                filas.append(lineas[i]); i += 1
            tabla = [[c.strip() for c in f.strip().strip('|').split('|')] for f in filas]
            out.append(('table', tabla, ini, filas))
            continue
        if RX_UL.match(linea):
            items = []
            while i < n and RX_UL.match(lineas[i]):
                items.append(RX_UL.sub('', lineas[i].rstrip())); i += 1
            out.append(('ul', items, ini))
            continue
        if RX_OL.match(linea):
            items = []
            while i < n and RX_OL.match(lineas[i]):
                items.append(RX_OL.sub('', lineas[i].rstrip())); i += 1
            out.append(('ol', items, ini))
            continue
        parrafo = [linea]
        i += 1
        while i < n and lineas[i].strip() and not lineas[i].startswith('#') and \
                lineas[i].strip() != '---' and not lineas[i].strip().startswith('```') and \
                not lineas[i].strip().startswith('|') and not RX_UL.match(lineas[i]) and \
                not RX_OL.match(lineas[i]):
            parrafo.append(lineas[i].rstrip()); i += 1
        out.append(('p', ' '.join(parrafo), ini))
    return out


def celdas_robustas(fila):
    s = fila.strip()
    if s.startswith('|'):
        s = s[1:]
    if s.endswith('|') and not s.endswith('\\|'):
        s = s[:-1]
    return [c.strip() for c in re.split(r'(?<!\\)\|', s)]


def fila_linea(ini, k):
    """Línea de la fila k de una tabla que empieza en `ini` (la 1 es el separador)."""
    return ini if k == 0 else ini + 1 + k


def unidades(bloques):
    """(texto, línea, tipo) por párrafo, ítem, fila de tabla, título y bloque de código."""
    for b in bloques:
        tipo, cont, ini = b[0], b[1], b[2]
        if tipo == 'hr':
            continue
        if tipo in ('ul', 'ol'):
            for k, it in enumerate(cont):
                yield it, ini + k, 'item'
        elif tipo == 'table':
            for k, fila in enumerate(cont):
                yield ' | '.join(fila), fila_linea(ini, k), 'fila'
        else:
            yield cont, ini, tipo


# --------------------------------------------------------------------------
# d. Residuo de español (se reutiliza en render_en.py sobre el texto del docx/pdf)
# --------------------------------------------------------------------------
def residuo(texto, densidad=True):
    """Devuelve (errores, avisos) de español en un trozo (párrafo, ítem, fila o título)."""
    errs, avisos = [], []
    t = RX_MARCA.sub(' ', texto)
    chars = sorted(set(c for c in t if c in CHARS_ES))
    if chars:
        errs.append('signos españoles %s' % ' '.join(chars))
    malas, producto = set(), set()
    for w in RX_ACENTO.findall(t):
        wl = w.lower()
        if wl in PRESTAMOS or (wl.endswith('s') and wl[:-1] in PRESTAMOS):
            continue
        (producto if wl in NOMBRES_PRODUCTO else malas).add(w)
    if malas:
        errs.append('palabras con tilde/ñ: %s' % ', '.join(sorted(malas)[:8]))
    if producto:
        avisos.append('nombre de producto español (¿coherente con el xlsx?): %s'
                      % ', '.join(sorted(producto)))
    if '€' in t:
        errs.append('símbolo €')
    prohib = sorted(set(m.group(1) for m in RX_PROHIBIDAS.finditer(t)))
    if prohib:
        errs.append('términos prohibidos: %s' % ', '.join(prohib))
    limpio = RX_PERMITIDAS.sub(' ', t)
    cent = sorted(set(m.group(1).lower() for m in RX_CENTINELA.finditer(limpio)))
    if cent:
        errs.append('palabras españolas: %s' % ', '.join(cent[:10]))
    if densidad:
        toks = RX_LETRAS.findall(limpio)
        k = sum(1 for w in toks if w.lower() in FUNCIONALES)
        if k >= 3 and toks and k / len(toks) >= 0.15:
            errs.append('densidad de palabras funcionales españolas %d/%d' % (k, len(toks)))
        else:
            # frase a medio traducir dentro de un párrafo inglés: 3 marcas en 6 palabras
            marca = [w.lower() in FUNCIONALES or w.lower() in CENTINELAS for w in toks]
            for i in range(len(toks)):
                if sum(marca[i:i + 6]) >= 3:
                    errs.append('tramo en español «%s»' % ' '.join(toks[i:i + 6]))
                    break
    if re.search(r'\bSpain\b|\bSpanish\b', t):
        avisos.append('menciona Spain/Spanish (solo para contrastar mercados)')
    if re.search(r'\bentr[ée]es?\b', t, re.I):
        avisos.append('«entrée» (D9: main / main course)')
    return errs, avisos


def no_latinos(texto):
    """e. Letras de otras escrituras (CJK, cirílico, griego, hangul, árabe, hebreo, tailandés…)."""
    malos = []
    for ch in texto:
        o = ord(ch)
        if o < 0x250:
            continue
        if 0x3000 <= o <= 0x303F or 0xFF00 <= o <= 0xFFEF:
            malos.append(ch)
            continue
        if unicodedata.category(ch).startswith('L') and \
                not unicodedata.name(ch, '').startswith('LATIN'):
            malos.append(ch)
    malos += D.RX_NO_LATINOS.findall(texto)
    return sorted(set(malos))


def winansi(texto):
    """f. Lo que el PDF (Helvetica Type-1) no pinta: restos antes de sanear que no están en
    MAPA_WINANSI (sanear los degrada o los borra en silencio) + lo que quede tras sanear."""
    bloques = D.parsear(RX_MARCA.sub('', texto))
    antes = D.restos_no_winansi(bloques)
    quedan = D.restos_no_winansi(D.sanear_bloques(bloques))
    malos = {c for c in antes if c not in D.MAPA_WINANSI}
    malos |= set(quedan)
    return sorted(malos)


# --------------------------------------------------------------------------
# g. Mapa de ficheros y pestañas (SPEC §2, fuente única)
# --------------------------------------------------------------------------
_MAPA = None


def mapa_spec():
    """(raíces ES prohibidas, ficheros EN válidos, pestañas EN) leídos de la tabla §2."""
    global _MAPA
    if _MAPA:
        return _MAPA
    texto = SPEC.read_text(encoding='utf-8')
    m = re.search(r'^## 2\..*?$(.*?)^## 3\.', texto, re.S | re.M)
    if not m:
        sys.exit('ABORTADO: no encuentro la tabla §2 en SPEC.md')
    raices_es, ficheros_en, pestanas = set(ORFANOS_ES), set(), set()
    for linea in m.group(1).splitlines():
        c = [x.strip().replace('**', '') for x in linea.strip().strip('|').split('|')]
        if len(c) != 3 or not re.search(r'\.(xlsx|docx)', c[0]):
            continue
        raices_es.add(re.sub(r'\.(xlsx|docx).*$', '', c[0]))
        base = re.sub(r'\.(xlsx|docx).*$', '', c[1])
        for ext in re.findall(r'\.(xlsx|docx|pdf)', c[1]):
            ficheros_en.add('%s.%s' % (base, ext))
        pestanas |= {p.strip() for p in c[2].split('·') if p.strip() not in ('', '—')}
    if len(raices_es) < 10 or len(ficheros_en) < 10:
        sys.exit('ABORTADO: la tabla §2 de SPEC.md no se ha leído bien')
    _MAPA = (raices_es, ficheros_en, pestanas)
    return _MAPA


RX_XLSX = re.compile(r'[\w.-]+\.xlsx\b')
RX_PESTANA = re.compile(r'(?:sheets?|tabs?)\s+(["“])([^"”\n]{1,40})["”]|'
                        r'(["“])([^"”\n]{1,40})["”]\s+(?:sheets?|tabs?)\b', re.I)


# --------------------------------------------------------------------------
# j. Cifras
# --------------------------------------------------------------------------
def cifras_es(bloques, fiscal_tanda):
    """Ocurrencias del ES: (valor, clase, línea, contexto). Clases: 'err' (dinero o % que
    tiene que estar en el EN), 'aviso' (dinero/% fiscal), 'otra', 'exenta' (unidad, D8)."""
    occ = []

    def tag_de(txt, a, b):
        resto = txt[b:]
        m = RX_RANGO.match(resto)
        tras = resto[m.end():] if m else resto     # rango «28-32 %» → hereda la etiqueta
        if RX_TRAS_PCT.match(tras):
            return 'pct'
        mm = RX_TRAS_EUR.match(tras)
        if mm:
            return 'eur_ud' if RX_POR_UNIDAD.match(tras[mm.end():]) else 'eur'
        if RX_TRAS_UNIDAD.match(tras):
            return 'ud'
        return 'otra'

    def analizar(txt, linea, ctx_ud, ctx_fiscal, celda):
        # ctx_ud = (cabecera de la columna, etiqueta de la fila) en las tablas
        limpio = RX_FUERA_CIFRAS.sub(lambda m: ' ' * len(m.group(0)), txt)
        for m in RX_NUM_ES.finditer(limpio):
            a, b = m.span(1)
            v = dec(m.group(1), 'es')
            if v is None:
                continue
            antes, despues = limpio[:a], limpio[b:]
            if re.match(r'^\s*(#+\s*)?$', antes) and despues.startswith('.'):
                continue                                  # ordinal «3.» de título o lista
            tag = tag_de(limpio, a, b)
            if tag == 'otra' and '.' not in m.group(1) and ',' not in m.group(1) \
                    and 1900 <= v <= 2099:
                continue                                  # año
            ctx = txt[max(0, a - 45):b + 25].replace('\n', ' ')
            if tag == 'ud' or tag == 'eur_ud':
                occ.append((v, 'exenta', linea, ctx)); continue
            # €/kg, kg… en la cabecera o la etiqueta de la fila, o «el kilo» al lado: D8 lo
            # convierte a $/lb, oz… (el % nunca: el rendimiento no cambia con la unidad)
            if tag in ('eur', 'otra') and (
                    (celda and (RX_CTX_UNIDAD.search(ctx_ud[0]) or
                                RX_CTX_UNIDAD_FILA.search(ctx_ud[1]))) or
                    (not celda and RX_CTX_UNIDAD.search(txt[max(0, a - 120):b + 60]))):  # la frase: «el kilo limpio … es de 28,84 €»
                occ.append((v, 'exenta', linea, ctx)); continue
            if tag == 'otra':
                if v == v.to_integral_value() and v <= 12:
                    continue                              # el inglés las escribe en letra
                if despues[:2].startswith('/') or RX_LEGAL_ANTES.search(antes[-30:]) or \
                        RX_FECHA_TRAS.match(despues):
                    continue                              # «Ley 37/1992», «art. 91», «22 de…»
                occ.append((v, 'otra', linea, ctx)); continue
            ventana = txt if celda else txt[max(0, a - 60):b + 40]
            fisc = fiscal_tanda or RX_CTX_FISCAL.search(
                RX_SIN_IVA.sub(' ', ventana + ' ' + (ctx_fiscal or '')))
            occ.append((v, 'aviso' if fisc else 'err', linea, ctx))

    for b in bloques:
        tipo, cont, ini = b[0], b[1], b[2]
        if tipo == 'hr' or tipo == 'code':
            continue
        if tipo == 'table':
            cab = cont[0]
            for k, fila in enumerate(cont):
                if k == 0:
                    continue
                for ci, c in enumerate(fila):
                    h = cab[ci] if ci < len(cab) else ''
                    analizar(c, fila_linea(ini, k), (h, fila[0] if ci else ''),
                             ' '.join(fila) + ' ' + h, True)
        elif tipo in ('ul', 'ol'):
            for k, it in enumerate(cont):
                analizar(it, ini + k, ('', ''), '', False)
        else:
            analizar(cont, ini, ('', ''), '', False)
    return occ


def cifras_en(texto):
    limpio = RX_FUERA_CIFRAS.sub(' ', RX_MARCA.sub(' ', texto))
    c = collections.Counter()
    for m in RX_NUM_EN.finditer(limpio):
        v = dec(m.group(1), 'en')
        if v is not None:
            c[v] += 1
    return c


# --------------------------------------------------------------------------
# Gate de una tanda
# --------------------------------------------------------------------------
def palabras(t):
    return len([w for w in t.split() if re.search(r'\w', w)])


def estructura(bloques):
    """Encabezados [(nivel, línea)], tablas, separadores y listas por sección."""
    heads, tablas, hrs, listas = [], [], [], [collections.Counter()]
    for b in bloques:
        tipo, ini = b[0], b[2]
        if tipo in ('h1', 'h2', 'h3', 'h4'):
            heads.append((int(tipo[1]), ini, b[1]))
            listas.append(collections.Counter())
        elif tipo == 'table':
            tablas.append((ini, [len(celdas_robustas(f)) for f in b[3]], b[3]))
        elif tipo == 'hr':
            hrs.append(ini)
        elif tipo in ('ul', 'ol'):
            listas[-1][tipo] += len(b[1])
            listas[-1]['_l' + tipo] = listas[-1]['_l' + tipo] or ini
    return heads, tablas, hrs, listas


def revisar(tanda, final=False, fiscal=False, ruta_en=None, ruta_es=None):
    """Lee la pareja de ficheros y devuelve (errores, avisos, info)."""
    es_p = Path(ruta_es) if ruta_es else TANDAS_ES / ('%s.md' % tanda)
    en_p = Path(ruta_en) if ruta_en else TANDAS_EN / ('%s.md' % tanda)
    for p in (es_p, en_p):
        if not p.exists():
            return [(0, 'io', 'no existe %s' % p)], [], {}
    return revisar_textos(tanda, es_p.read_text(encoding='utf-8'),
                          en_p.read_text(encoding='utf-8'), final, fiscal)


def revisar_textos(tanda, es, en, final=False, fiscal=False):
    """Devuelve (errores, avisos, info); cada error/aviso es (línea_en, código, mensaje)."""
    E, A = [], []
    if not en.strip():
        return [(0, 'io', 'el EN está vacío')], [], {}
    if en == es:
        E.append((0, 'io', 'el EN es idéntico al ES'))
    bes, ben = parsear_con_lineas(es), parsear_con_lineas(en)

    # a. encabezados y separadores
    h_es, t_es, hr_es, l_es = estructura(bes)
    h_en, t_en, hr_en, l_en = estructura(ben)
    if len(h_es) != len(h_en):
        E.append((0, 'a-titulos', 'encabezados: ES %d · EN %d' % (len(h_es), len(h_en))))
    for (nv_es, li_es, tx_es), (nv_en, li_en, tx_en) in zip(h_es, h_en):
        if nv_es != nv_en:
            E.append((li_en, 'a-titulos', 'nivel %s en EN y %s en ES (ES l.%d «%s»)'
                      % ('#' * nv_en, '#' * nv_es, li_es, tx_es[:50])))
            break                                       # el resto sale desplazado
    if len(hr_es) != len(hr_en):
        E.append((hr_en[0] if hr_en else 0, 'a-separadores',
                  'separadores `---` (saltos de página): ES %d · EN %d' % (len(hr_es), len(hr_en))))

    # b. tablas
    if len(t_es) != len(t_en):
        E.append((0, 'b-tablas', 'tablas: ES %d · EN %d' % (len(t_es), len(t_en))))
    for k, ((li_es, c_es, _), (li_en, c_en, filas_en)) in enumerate(zip(t_es, t_en), 1):
        if len(c_es) != len(c_en):
            E.append((li_en, 'b-tablas', 'tabla %d: %d filas en EN y %d en ES (ES l.%d)'
                      % (k, len(c_en), len(c_es), li_es)))
        else:
            for j, (a, b) in enumerate(zip(c_es, c_en)):
                if a != b:
                    E.append((fila_linea(li_en, j), 'b-tablas', 'tabla %d fila %d: %d columnas '
                              'en EN y %d en ES' % (k, j + 1, b, a)))
        for j, f in enumerate(filas_en):
            if '\\|' in f:
                E.append((fila_linea(li_en, j), 'b-tablas', 'barra escapada `\\|`: el render '
                          '(documentos.parsear) la parte como columna; usa «/»'))

    # c. listas por sección
    if len(h_es) == len(h_en):
        for s, (a, b) in enumerate(zip(l_es, l_en)):
            for tipo, nombre in (('ul', 'viñetas'), ('ol', 'numerados')):
                if a[tipo] != b[tipo]:
                    li = b['_l' + tipo] or (h_en[s - 1][1] if s else 1)
                    sec = h_en[s - 1][2][:40] if s else 'portada'
                    E.append((li, 'c-listas', 'sección «%s»: %d ítems %s en EN y %d en ES'
                              % (sec, b[tipo], nombre, a[tipo])))
    else:
        for tipo in ('ul', 'ol'):
            ta, tb = sum(x[tipo] for x in l_es), sum(x[tipo] for x in l_en)
            if ta != tb:
                E.append((0, 'c-listas', 'ítems %s: ES %d · EN %d' % (tipo, ta, tb)))

    # d. residuo de español · e. no latinos
    for txt, li, tipo in unidades(ben):
        errs, avs = residuo(txt)
        for e in errs:
            E.append((li, 'd-espanol', '%s · «%s»' % (e, RX_MARCA.sub('', txt)[:70])))
        for a in avs:
            A.append((li, 'd-aviso', a))
        nl = no_latinos(txt)
        if nl:
            E.append((li, 'e-no-latinos', ' '.join('%s U+%04X' % (c, ord(c)) for c in nl)))

    # f. WinAnsi (lo que el PDF no pinta)
    lineas_en = en.split('\n')
    for ch in winansi(en):
        li = next((i + 1 for i, l in enumerate(lineas_en) if ch in l), 0)
        E.append((li, 'f-winansi', '%r U+%04X: Helvetica no lo pinta (sanear lo borra o '
                  'degrada); usa un carácter WinAnsi' % (ch, ord(ch))))

    # g. ficheros
    raices_es, ficheros_en, pestanas = mapa_spec()
    for i, l in enumerate(lineas_en, 1):
        for r in raices_es:
            if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(r), l):
                E.append((i, 'g-ficheros', 'nombre de fichero ES «%s»' % r))
        for x in RX_XLSX.findall(l):
            if x not in ficheros_en:
                E.append((i, 'g-ficheros', '«%s» no está en la columna EN de SPEC §2' % x))
        for m in RX_PESTANA.finditer(l):
            q, nombre = (m.group(1), m.group(2)) if m.group(2) else (m.group(3), m.group(4))
            if nombre not in pestanas:
                A.append((i, 'g-pestana', 'pestaña «%s» no está en SPEC §2' % nombre))
            if q == '“':
                A.append((i, 'g-pestana', 'pestaña con comillas curvas: D11 pide rectas'))

    # h. marcas ⟦ADAPT⟧
    marcas = [(i, m.group(0)) for i, l in enumerate(lineas_en, 1) for m in RX_MARCA.finditer(l)]
    for i, mk in marcas:
        (E if final else A).append((i, 'h-adapt', mk[:90]))

    # i. ratio de palabras
    pes, pen = palabras(es), palabras(en)
    ratio = pen / pes if pes else 0
    if ratio < 0.6:
        E.append((0, 'i-ratio', 'ratio de palabras EN/ES %.2f (< 0,6: ¿truncado?)' % ratio))
    elif not 0.8 <= ratio <= 1.3:
        A.append((0, 'i-ratio', 'ratio de palabras EN/ES %.2f (fuera de 0,8-1,3)' % ratio))

    # j. cifras
    fiscal_tanda = fiscal or tanda in TANDAS_FISCALES
    occ = cifras_es(bes, fiscal_tanda)
    hay_en = cifras_en(en)
    por_valor = collections.OrderedDict()
    for v, clase, li, ctx in occ:
        por_valor.setdefault(v, []).append((clase, li, ctx))
    exentas = 0
    for v, lista in por_valor.items():
        clases = collections.Counter(c for c, _, _ in lista)
        exentas += clases['exenta']
        if v in hay_en:
            if clases['err'] > hay_en[v]:
                A.append((0, 'j-cifras', '%s: %d veces como dinero/%% en ES y %d en EN'
                          % (fmt(v), clases['err'], hay_en[v])))
            continue
        for clase, codigo, dest in (('err', 'j-cifras', E), ('aviso', 'j-cifras-fiscal', A),
                                    ('otra', 'j-cifras-otras', A)):
            if clases[clase]:
                _, li, ctx = next(x for x in lista if x[0] == clase)
                dest.append((0, codigo, '%s (x%d) no aparece en EN · ES l.%d «…%s…»'
                             % (fmt(v), clases[clase], li, ctx.strip())))
                break
    info = {'palabras_es': pes, 'palabras_en': pen, 'ratio': ratio, 'marcas': len(marcas),
            'cifras_exentas': exentas, 'titulos': len(h_en), 'tablas': len(t_en)}
    return E, A, info


def informe(tanda, E, A, info, ver_avisos=False, limite=25):
    print('== %s · %s palabras EN / %s ES (ratio %.2f) · %s títulos · %s tablas · ⟦ADAPT⟧: %s'
          % (tanda, info.get('palabras_en', '?'), info.get('palabras_es', '?'),
             info.get('ratio', 0), info.get('titulos', '?'), info.get('tablas', '?'),
             info.get('marcas', '?')))
    for li, cod, msg in sorted(E, key=lambda x: x[0]):
        print('  ERROR l.%s [%s] %s' % (li or '-', cod, msg))
    lista = sorted(A, key=lambda x: x[0])
    for li, cod, msg in (lista if ver_avisos else lista[:limite]):
        print('  aviso l.%s [%s] %s' % (li or '-', cod, msg))
    if not ver_avisos and len(lista) > limite:
        print('  … %d avisos más (--avisos para verlos todos)' % (len(lista) - limite))
    if E:
        print('FALLA (%d errores, %d avisos)' % (len(E), len(A)))
    else:
        print('OK (0 errores, %d avisos)' % len(A))


# --------------------------------------------------------------------------
# Autotest: el gate tiene que tumbar el ES y dejar pasar inglés de verdad
# --------------------------------------------------------------------------
def cifras_formato_en(texto):
    """Simula una traducción perfecta de las cifras (D6): 1.234,56 € → $1,234.56 · 32,7 % → 32.7%."""
    def us(m):
        entero, _, decs = m.group(1).replace('.', '').partition(',')
        return '{:,}'.format(int(entero)) + ('.' + decs if decs else '')
    t = RX_NUM_ES.sub(us, texto)
    t = re.sub(r'(\d[\d,.]*)[\s  ]?€', r'$\1', t)
    return re.sub(r'(\d)[\s  ]%', r'\1%', t)


def autotest():
    t0 = time.time()
    fallos = 0
    total_p = cazados_dens = cazados_union = 0
    for t in TANDAS:
        es_p = TANDAS_ES / ('%s.md' % t)
        es = es_p.read_text(encoding='utf-8')
        # 1) la réplica con líneas da los mismos bloques que el render
        mios = [(b[0], b[1]) for b in parsear_con_lineas(es)]
        if mios != D.parsear(es):
            print('  FALLO %s: parsear_con_lineas ≠ documentos.parsear' % t); fallos += 1
        # 2) el ES pasado como EN tiene que fallar por residuo (y sólo por contenido, no por
        #    estructura: contra sí mismo los títulos, tablas y listas cuadran)
        E, _, _ = revisar(t, ruta_en=str(es_p))
        cods = collections.Counter(c for _, c, _ in E)
        print('  %s como EN: %d errores %s' % (t, len(E), dict(cods)))
        if not cods['d-espanol']:
            print('  FALLO %s: el ES pasa como inglés' % t); fallos += 1
        if any(c.startswith(('a-', 'b-', 'c-')) for c in cods):
            print('  FALLO %s: el ES contra sí mismo da errores de estructura' % t); fallos += 1
        # 2b) cifras: con las del ES pasadas a formato US (D6) no falta ninguna; si se
        #     borra un importe que sólo sale una vez, el gate lo caza
        sim = cifras_formato_en(es)
        E2, _, _ = revisar_textos(t, es, sim)
        if any(c == 'j-cifras' for _, c, _ in E2):
            print('  FALLO %s: cifras en formato US dan error %s'
                  % (t, [m for _, c, m in E2 if c == 'j-cifras'][:3])); fallos += 1
        unicas = [v for v, cl, _, _ in cifras_es(parsear_con_lineas(es), t in TANDAS_FISCALES)
                  if cl == 'err']
        cuenta = cifras_en(sim)
        unicas = [v for v in unicas if cuenta[v] == 1]
        if unicas:
            v = unicas[0]
            pat = re.escape(format(v, ',f'))           # Decimal('18.50') → «18.50»
            sim2, n = re.subn(r'(?<![\w.,])%s(?![\w]|[.,]\d)' % pat, 'XX', sim, count=1)
            E3, _, _ = revisar_textos(t, es, sim2)
            if n and not any(c == 'j-cifras' for _, c, _ in E3):
                print('  FALLO %s: borrar %s no da error de cifras' % (t, fmt(v))); fallos += 1
        # 3) cada párrafo ES de verdad (≥ 12 palabras) cae
        for tipo, txt, _ in [(b[0], b[1], b[2]) for b in parsear_con_lineas(es)]:
            if tipo != 'p' or len(txt.split()) < 12:
                continue
            total_p += 1
            errs, _ = residuo(txt)
            if errs:
                cazados_union += 1
            if any(e.startswith('densidad') for e in errs):
                cazados_dens += 1
            else:
                errs_sin, _ = residuo(txt, densidad=False)
                if not errs_sin:
                    print('  ES no cazado: «%s»' % txt[:90])
    print('párrafos ES ≥ 12 palabras: %d · cazados por densidad %d · por el conjunto %d'
          % (total_p, cazados_dens, cazados_union))
    if cazados_union != total_p:
        fallos += 1
    # 4) inglés real (blog EN de aichef.pro): cero falsos positivos de español
    # (los prompt-library-* son volcados de tablas HTML con marcas y residuo propio: fuera)
    blog = sorted(f for f in (REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'en').glob('*.md')
                  if not f.name.startswith('prompt-library-'))
    n_p = fp = 0
    for f in blog:
        txt = re.sub(r'(?s)^---.*?\n---\n', '', f.read_text(encoding='utf-8'), count=1)
        txt = re.sub(r'<[^>]+>', ' ', txt)
        for tipo, cont in D.parsear(txt):
            if tipo not in ('p', 'ul', 'ol', 'h2', 'h3'):
                continue
            for u in (cont if isinstance(cont, list) else [cont]):
                n_p += 1
                errs, _ = residuo(u)
                # el blog EN arrastra «» y € de su origen español: aquí sólo se miden los
                # falsos positivos de tildes, centinelas y densidad
                errs = [e for e in errs if not e.startswith(('términos', 'símbolo', 'signos'))]
                if errs:
                    fp += 1
                    if fp <= 15:
                        print('  FP blog %s: %s · «%s»' % (f.name[:40], errs, u[:80]))
    print('blog EN: %d ficheros, %d unidades, %d falsos positivos' % (len(blog), n_p, fp))
    if not blog or fp > n_p * 0.002:
        fallos += 1
    print('autotest %s en %.2f s' % ('OK' if not fallos else 'FALLA (%d)' % fallos,
                                     time.time() - t0))
    return 0 if not fallos else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--tanda', choices=TANDAS)
    g.add_argument('--todas', action='store_true', help='todas las tandas que tengan EN')
    g.add_argument('--autotest', action='store_true')
    ap.add_argument('--final', action='store_true', help='⟦ADAPT⟧ pasa a ser error')
    ap.add_argument('--fiscal', action='store_true',
                    help='trata la tanda como fiscal (cifras ausentes = aviso)')
    ap.add_argument('--en', default=None, help='otro fichero EN (p. ej. para probar)')
    ap.add_argument('--avisos', action='store_true', help='lista todos los avisos')
    a = ap.parse_args()
    if a.autotest:
        sys.exit(autotest())
    if a.tanda:
        E, A, info = revisar(a.tanda, a.final, a.fiscal, a.en)
        informe(a.tanda, E, A, info, a.avisos)
        sys.exit(1 if E else 0)
    malas, hechas = [], 0
    for t in TANDAS:
        if not (TANDAS_EN / ('%s.md' % t)).exists():
            continue
        hechas += 1
        E, A, info = revisar(t, a.final, a.fiscal)
        informe(t, E, A, info, a.avisos, limite=10)
        if E:
            malas.append(t)
    print('TODAS: %d tandas con EN · %d con errores %s' % (hechas, len(malas), ' '.join(malas)))
    sys.exit(1 if malas or not hechas else 0)


if __name__ == '__main__':
    main()
