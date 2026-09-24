#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_gm_mapas.py — Recipe Costing Kit Pro (EN) · traducción del grupo GM-mapas.

Produce `textos_en/GM-mapas.json` a partir de `textos_es.json` (solo grupo GM-mapas),
usando `mapas.py` y `glosario_en.json` como fuente de verdad, SIN desviarse de ellos.

Reglas aplicadas (ver SPEC.md D7-D9, §2.2-§2.4, y el encargo de la tarea):
  - mapa-hoja / mapa-clave / regenerar-con-en_mapa -> el valor lo dicta mapas.py (en_mapa).
  - Grupo E1 (tabla Conversions): 56 cadenas. La tabla ES no es un subconjunto de la EN
    (D7 cambia unidades, ancla de tamaño de botella/lata de cl a ml, y quita el peso por
    defecto de bunch/packet). Se traduce cada cadena a lo que representa en la lógica de
    mapas.conversions(), y se marca cifra_derivada=true donde el número es de mercado
    (tamaños de botella/lata) o donde la fila no existe ya en el EN (bunch/packet -> g).
  - Grupo D14 (versión/subject/URL): 3 cadenas, valores ya decididos en la SPEC (D14),
    salvo el mes de publicación (queda como plantilla, cifra_derivada=true).
  - Grupo R2-10 (13-lista-precios-ingredientes.xlsx): 107 cadenas. Todo el libro 13 EN se
    REGENERA desde las recetas EN (mercado_en.json), así que aquí solo se deja una
    traducción de referencia (cifra_derivada=true en formatos de compra y precios; false
    en nombres de ingrediente e instrucciones, que sí se reutilizan).

Ejecutar:
    python3 generar_gm_mapas.py            # escribe textos_en/GM-mapas.json
    python3 generar_gm_mapas.py --check    # solo valida, no escribe
"""
import json
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import mapas  # noqa: E402

ES_PATH = os.path.join(AQUI, 'textos_es.json')
OUT_DIR = os.path.join(AQUI, 'textos_en')
OUT_PATH = os.path.join(OUT_DIR, 'GM-mapas.json')

HOJAS = mapas.HOJAS  # ES -> EN, exacto (D9)

# ==========================================================================
# 1. Grupo E1 — tabla `Conversions` (56 cadenas), hardcodeado 1:1 (ver docstring).
# ==========================================================================
NOTA_ANCLA_ML = ('D7/E3: en EN el ancla de tamaño pasa de cl (ES) a ml — ver la fila '
                 '→ml de {u} en mapas.ENVASES. La cifra la fija mapas.py, no se traduce a mano.')
NOTA_DERIVADA_ML = ('D7/E3: fila derivada de la celda de tamaño en ml (mapas.conversions() '
                     'la calcula con una fórmula); en ES esta fila salía del ancla en cl.')
NOTA_SIN_PESO = ('D7(4): en EN, bunch/packet no llevan peso por defecto — esta fila no '
                  'existe en la Conversions EN (mapas.SUELTAS). Traducción solo de referencia.')

E1 = {
    # --- masa: kg, g ---
    'kg→kg': ('kg→kg', False, None),
    'misma unidad': ('same unit', False, None),
    'kg→g': ('kg→g', False, None),
    '1 kg = 1.000 g': ('1 kg = 1,000 g', False, None),
    'g→g': ('g→g', False, None),
    'g→kg': ('g→kg', False, None),
    '1 g = 0,001 kg': ('1 g = 0.001 kg', False, None),
    # --- volumen: L, ml, cl ---
    'L→L': ('L→L', False, None),
    'L→ml': ('L→ml', False, None),
    '1 L = 1.000 ml': ('1 L = 1,000 ml', False, None),
    'L→cl': ('L→cl', False, None),
    '1 L = 100 cl': ('1 L = 100 cl', False, None),
    'ml→ml': ('ml→ml', False, None),
    'ml→L': ('ml→L', False, None),
    '1 ml = 0,001 L': ('1 ml = 0.001 L', False, None),
    'ml→cl': ('ml→cl', False, None),
    '1 ml = 0,1 cl': ('1 ml = 0.1 cl', False, None),
    'cl→cl': ('cl→cl', False, None),
    'cl→ml': ('cl→ml', False, None),
    '1 cl = 10 ml': ('1 cl = 10 ml', False, None),
    'cl→L': ('cl→L', False, None),
    '1 cl = 0,01 L': ('1 cl = 0.01 L', False, None),
    # --- recuento: each, dozen (D7 §2.3: ud->each, docena->dozen) ---
    'ud→ud': ('each→each', False, None),
    'docena→ud': ('dozen→each', False, None),
    '1 docena = 12 ud': ('1 dozen = 12 each', False, None),
    'docena→docena': ('dozen→dozen', False, None),
    'ud→docena': ('each→dozen', False, None),
    '1 ud = 1/12 docena': ('1 each = 1/12 dozen', False, None),
    # --- sueltas: bunch, packet (identidad + ->each; D7(4)) ---
    'manojo→manojo': ('bunch→bunch', False, None),
    'manojo→ud': ('bunch→each', False, None),
    'el manojo se compra y se usa como unidad':
        ('same unit (bought and used as one bunch)', False,
         'mapas.SUELTAS: texto exacto de mapas.conversions() para la identidad de bunch.'),
    'sobre→sobre': ('packet→packet', False, None),
    'sobre→ud': ('packet→each', False, None),
    'el sobre se compra y se usa como unidad':
        ('same unit (bought and used as one packet)', False,
         'mapas.SUELTAS: texto exacto de mapas.conversions() para la identidad de packet.'),
    # --- envases: can (lata), bottle (botella) — identidad y ->each ---
    'lata→lata': ('can→can', False, None),
    'lata→ud': ('can→each', False,
                'mapas.ENVASES: nota exacta "one can counted as one unit".'),
    'la lata se compra y se usa como unidad':
        ('same unit (bought and used as one can)', False,
         'mapas.ENVASES: texto exacto de mapas.conversions() para la identidad de can.'),
    'botella→botella': ('bottle→bottle', False, None),
    'botella→ud': ('bottle→each', False,
                   'mapas.ENVASES: nota exacta "one bottle counted as one unit".'),
    'la botella se compra y se usa como unidad':
        ('same unit (bought and used as one bottle)', False,
         'mapas.ENVASES: texto exacto de mapas.conversions() para la identidad de bottle.'),
    # --- botella: en ES el ancla es cl (70/75); en EN el ancla pasa a ml (D7/E3) ---
    'botella→cl': ('bottle→cl', True, NOTA_DERIVADA_ML.format(u='bottle')),
    'botella de 70 cl (destilados). Vino: cambia el 70 por 75':
        ('From the bottle size cell (in ml) — edit the size there, not here.', True,
         NOTA_DERIVADA_ML.format(u='bottle') +
         ' ES: ancla 70 cl (destilados) / 75 cl (vino).'),
    'botella→ml': ('bottle→ml', True, NOTA_ANCLA_ML.format(u='bottle')),
    'botella de 70 cl = 700 ml':
        ('bottle size in ml: 750 (US wine & spirits). UK spirits: type 700 here — '
         'edit only this cell', True,
         'Texto EXACTO de mapas.ENVASES["bottle"]["nota_tam"] (D7/E3: 750 ml US, no 700).'),
    'botella→L': ('bottle→L', True, NOTA_DERIVADA_ML.format(u='bottle')),
    'botella de 70 cl = 0,7 L':
        ('From the bottle size cell (in ml) — edit the size there, not here.', True,
         NOTA_DERIVADA_ML.format(u='bottle')),
    # --- lata: en ES el ancla es cl (33); en EN el ancla pasa a ml (D7/E3) ---
    'lata→cl': ('can→cl', True, NOTA_DERIVADA_ML.format(u='can')),
    'lata de 33 cl':
        ('From the can size cell (in ml) — edit the size there, not here.', True,
         NOTA_DERIVADA_ML.format(u='can') + ' ES: ancla 33 cl.'),
    'lata→ml': ('can→ml', True, NOTA_ANCLA_ML.format(u='can')),
    'lata de 33 cl = 330 ml':
        ('beverage can 12 fl oz = 355 ml (UK: 330). Edit only this cell. '
         'For #10 food cans buy in oz', True,
         'Texto EXACTO de mapas.ENVASES["can"]["nota_tam"] (D7/E3: 355 ml US; '
         'el 330 ml de la ES es justo la cifra UK que cita la nota).'),
    'lata→L': ('can→L', True, NOTA_DERIVADA_ML.format(u='can')),
    'lata de 33 cl = 0,33 L':
        ('From the can size cell (in ml) — edit the size there, not here.', True,
         NOTA_DERIVADA_ML.format(u='can')),
    # --- manojo/sobre -> peso: D7(4) los quita en EN ---
    'manojo→g': ('bunch→g', False, NOTA_SIN_PESO),
    'manojo de hierbas ≈ 30 g': ('herb bunch ≈ 30 g', False, NOTA_SIN_PESO),
    'sobre→g': ('packet→g', False, NOTA_SIN_PESO),
    'sobre ≈ 10 g': ('packet ≈ 10 g', False, NOTA_SIN_PESO),
}

# ==========================================================================
# 2. Grupo D14 — versión / subject / URL (3 cadenas). Valores ya en la SPEC.
# ==========================================================================
D14 = {
    'Versión 2.1 · septiembre 2026 · aichef.pro/kit-escandallos · info@aichef.pro':
        ('Version 2.1 · [MONTH] 2026 · aichef.pro/en/digital-products/recipe-costing-kit · '
         'info@aichef.pro', True,
         'D14: aplicar_en.py resuelve [MONTH] al publicar (mes de publicación del EN, no '
         'tiene por qué coincidir con el de la v2.1 ES).'),
    'Kit de Escandallos Pro · v2.1':
        ('Recipe Costing Kit Pro · v2.1', False,
         'D14/D2: subject de docProps, nombre ya decidido, no lo toca el agente de mercado.'),
    'aichef.pro/kit-escandallos':
        ('aichef.pro/en/digital-products/recipe-costing-kit', False,
         'D14/D1: slug ya decidido en la SPEC, no depende del mercado.'),
}

# ==========================================================================
# 3. Grupo R2-10 — 13-lista-precios-ingredientes.xlsx (107 cadenas).
#    Todo el libro se regenera desde mercado_en.json (D11): esto es SOLO referencia.
# ==========================================================================
NOTA_R210_FORMATO = ('R2-10: el 13 EN se genera desde las recetas EN (mercado_en.json), no '
                      'traduciendo el ES — cambian ingredientes, formatos de compra (D7) y '
                      'precios. Traducción de referencia.')
NOTA_R210_PRECIO = NOTA_R210_FORMATO + ' Precio ES de referencia: {precio}.'

# 3.1 Ingredientes y descriptores sueltos (sin "Se usa en:").
R2_STANDALONE = {
    'Bandeja 5 kg': ('Tray, 5 kg', True, NOTA_R210_FORMATO),
    'Al peso (precio por kg)': ('By weight (price per kg)', False, None),
    'Sobre 100 g': ('Packet, 100 g', True, NOTA_R210_FORMATO),
    'Caja 5 kg': ('Case, 5 kg', True, NOTA_R210_FORMATO),
    'Caja 2 kg': ('Case, 2 kg', True, NOTA_R210_FORMATO),
    'Microgreens': ('Microgreens', False, None),
    'Bandeja 50 g': ('Tray, 50 g', True, NOTA_R210_FORMATO),
    'Saco 10 kg': ('Sack, 10 kg', True, NOTA_R210_FORMATO),
    'Malla 5 kg': ('Mesh bag, 5 kg', True, NOTA_R210_FORMATO),
    'Saco 25 kg': ('Sack, 25 kg', True, NOTA_R210_FORMATO),
    'Caja 6 kg': ('Case, 6 kg', True, NOTA_R210_FORMATO),
    'Caja 12 tarrinas de 250 g': ('Case of 12 tubs, 250 g', True, NOTA_R210_FORMATO),
    'Caja 20 piezas': ('Case, 20 pieces', True, NOTA_R210_FORMATO),
    'Caja 12 tarrinas de 125 g': ('Case of 12 tubs, 125 g', True, NOTA_R210_FORMATO),
    'Caja 4 kg': ('Case, 4 kg', True, NOTA_R210_FORMATO),
    'Naranja': ('Orange', False, None),
    'Caja 10 kg': ('Case, 10 kg', True, NOTA_R210_FORMATO),
    'Caja 6 briks de 1 L': ('Case of 6 cartons, 1 L', True, NOTA_R210_FORMATO),
    'Placa 2 kg': ('Slab, 2 kg', True, NOTA_R210_FORMATO),
    'Brik 1 L': ('Carton, 1 L', True, NOTA_R210_FORMATO),
    'Paquete 84 lonchas': ('Pack, 84 slices', True, NOTA_R210_FORMATO),
    'Bolsa 2 kg': ('Bag, 2 kg', True, NOTA_R210_FORMATO),
    'Tarrina 2 kg': ('Tub, 2 kg', True, NOTA_R210_FORMATO),
    'Fardo 10 paquetes de 1 kg': ('Bundle of 10 packs, 1 kg', True, NOTA_R210_FORMATO),
    'Colorante rojo': ('Red food coloring', False, None),
    'Bote 50 g': ('Jar, 50 g', True, NOTA_R210_FORMATO),
    'Bote 250 g': ('Jar, 250 g', True, NOTA_R210_FORMATO),
    'Paquete 500 g': ('Pack, 500 g', True, NOTA_R210_FORMATO),
    'Caja 250 g': ('Case, 250 g', True, NOTA_R210_FORMATO),
    'Croquetas': ('Croquettes', False, None),
    'Caja 60 ud': ('Case, 60 each', True, NOTA_R210_FORMATO),
    'Mini quiche': ('Mini quiche', False, None),
    'Caja 40 ud': ('Case, 40 each', True, NOTA_R210_FORMATO),
    'Bolsa 6 ud': ('Bag, 6 each', True, NOTA_R210_FORMATO),
    'Por rebanada': ('Per slice', False, None),
    'Pan mini': ('Mini bread rolls', False, None),
    'Caja 100 ud': ('Case, 100 each', True, NOTA_R210_FORMATO),
    'Brik 1 kg (pasteurizadas)': ('Carton, 1 kg (pasteurized)', True, NOTA_R210_FORMATO),
    'Estuche 30 huevos': ('Carton of 30 eggs', True, NOTA_R210_FORMATO),
    'Garrafa 5 L': ('Jug, 5 L', True, NOTA_R210_FORMATO),
    'Bidón 25 L': ('Drum, 25 L', True, NOTA_R210_FORMATO),
    'Aceite de oliva virgen extra (AOVE)': ('Extra virgin olive oil (EVOO)', False, None),
    'Botella 500 ml': ('Bottle, 500 ml', True, NOTA_R210_FORMATO),
    'Botella 100 ml': ('Bottle, 100 ml', True, NOTA_R210_FORMATO),
    'Malla 1 kg': ('Mesh bag, 1 kg', True, NOTA_R210_FORMATO),
    'Bote 500 g': ('Jar, 500 g', True, NOTA_R210_FORMATO),
    'Cebollino': ('Chives', False, None),
    'Manojo': ('Bunch', False, None),
    'Hierbabuena': ('Spearmint', False, None),
    'Romero fresco': ('Fresh rosemary', False, None),
    'Saco 5 kg (gotas)': ('Sack, 5 kg (chips)', True, NOTA_R210_FORMATO),
    'Botella 70 cl': ('Bottle, 70 cl', True, NOTA_R210_FORMATO),
    'Por servicio (dosis)': ('Per serving (dose)', False, None),
    'Botella 75 cl': ('Bottle, 75 cl', True, NOTA_R210_FORMATO),
    'Soda / agua con gas': ('Soda / sparkling water', False, None),
    'Pack 6 botellas de 1 L': ('Pack of 6 x 1 L bottles', True, NOTA_R210_FORMATO),
    'Caja 24 botellines de 20 cl': ('Case of 24 x 20 cl bottles', True, NOTA_R210_FORMATO),
    'Por litro': ('Per liter', False, None),
    'Botella 2 L': ('Bottle, 2 L', True, NOTA_R210_FORMATO),
}

RE_PRECIO = re.compile(r'La plantilla (\d+) lo usa a ([\d,]+)\s*€/(\w+) \(otro proveedor\)\.')
RE_ILUSTRATIVO = re.compile(
    r'Ilustrativo: el precio anterior es de ejemplo, para que veas cómo funciona la alerta\. '
    r'Bórralo\.')


def hoja_en_o_falla(nombre_es):
    if nombre_es not in HOJAS:
        raise KeyError('hoja sin mapa en HOJAS: ' + nombre_es)
    return HOJAS[nombre_es]


def traducir_refs(refs_txt):
    """'02 «4. Carne» · 07 «Carrot Cake»' -> '02 "4. Meat" · 07 "Carrot Cake"'."""
    def repl(m):
        return '"' + hoja_en_o_falla(m.group(1)) + '"'
    return re.sub(r'«([^»]+)»', repl, refs_txt)


def traducir_se_usa_en(es):
    """Traduce una cadena 'Se usa en: ...' completa (con posible cola de frase)."""
    assert es.startswith('Se usa en: ')
    idx = es.rfind('».')
    assert idx != -1, 'sin cierre de refs: ' + es
    refs_part = es[len('Se usa en: '):idx + 2]   # hasta el '».' incluido
    rest = es[idx + 2:]                          # cola, puede ser ''

    refs_en = traducir_refs(refs_part)
    en = 'Used in: ' + refs_en
    cifra = False
    notas = []

    rest = rest.strip()
    while rest:
        m_precio = RE_PRECIO.match(rest)
        m_ilust = RE_ILUSTRATIVO.match(rest)
        if m_precio:
            plantilla, precio, unidad_es = m_precio.groups()
            unidad_en = mapas.UNIDADES.get(unidad_es, unidad_es)
            en += (' Template {} uses a different supplier ([$ price TBD for the US '
                   'market]/{}).').format(plantilla, unidad_en)
            cifra = True
            notas.append('ES: {} €/{} (plantilla {}, otro proveedor).'.format(
                precio, unidad_es, plantilla))
            rest = rest[m_precio.end():].strip()
        elif m_ilust:
            en += (' Sample data: the previous price is just an example, so you can see '
                   'how the alert works. Delete it.')
            rest = rest[m_ilust.end():].strip()
        else:
            raise ValueError('cola de frase sin patrón conocido: {!r} (de {!r})'.format(rest, es))
    return en, cifra, ('; '.join(notas) if notas else None)


# ==========================================================================
# 4. Autocomprobación de una cadena EN.
# ==========================================================================
def solo_latin1_ampliado(s):
    """Cero CJK/cirílico/hangul/árabe/hebreo/tailandés (glosario_en / bridge guard_idioma)."""
    for ch in s:
        if ch in '€':
            return False
        cat = unicodedata.category(ch)
        try:
            name = unicodedata.name(ch)
        except ValueError:
            name = ''
        bloques_prohibidos = ('CJK', 'HIRAGANA', 'KATAKANA', 'HANGUL', 'CYRILLIC', 'ARABIC',
                               'HEBREW', 'THAI', 'DEVANAGARI')
        if any(b in name for b in bloques_prohibidos):
            return False
    return True


PALABRAS_ES_RESIDUALES = [
    r'\bde la\b', r'\bpara\b', r'\bcon\b', r'\by\b', r'\bpor\b', r'\bsin\b',
    r'\bcómo\b', r'\bqué\b', r'á', r'é', r'í', r'ó', r'ú', r'ñ', r'¿', r'¡',
]

# Excepciones ya decididas en la SPEC (gate 2, §4): nombres propios / términos que se
# quedan en su grafía original aunque lleven tilde o diéresis.
LISTA_BLANCA_ACENTOS = ['açaí', 'jalapeño', 'ibérico', 'manchego']


def restos_espanol(s):
    low = s.lower()
    for w in LISTA_BLANCA_ACENTOS:
        low = low.replace(w, '')
    for pat in PALABRAS_ES_RESIDUALES:
        if re.search(pat, low):
            return pat
    return None


# ==========================================================================
# 5. Construcción del resultado
# ==========================================================================
def construir():
    with open(ES_PATH, encoding='utf-8') as fh:
        data = json.load(fh)
    cadenas = [c for c in data['cadenas'] if c.get('grupo') == 'GM-mapas']

    salida = []
    vistos = set()
    fallos = []

    for c in cadenas:
        es = c['es']
        if es in vistos:
            fallos.append('cadena repetida en textos_es.json: ' + es)
            continue
        vistos.add(es)

        obj = {'es': es}
        try:
            if 'en_mapa' in c:
                obj['en'] = c['en_mapa']
            elif es in E1:
                en, cifra, nota = E1[es]
                obj['en'] = en
                if cifra:
                    obj['cifra_derivada'] = True
                if nota:
                    obj['nota'] = nota
            elif es in D14:
                en, cifra, nota = D14[es]
                obj['en'] = en
                if cifra:
                    obj['cifra_derivada'] = True
                if nota:
                    obj['nota'] = nota
            elif es in R2_STANDALONE:
                en, cifra, nota = R2_STANDALONE[es]
                obj['en'] = en
                if cifra:
                    obj['cifra_derivada'] = True
                if nota:
                    obj['nota'] = nota
            elif es.startswith('Se usa en: '):
                en, cifra, nota = traducir_se_usa_en(es)
                obj['en'] = en
                if cifra:
                    obj['cifra_derivada'] = True
                if nota:
                    obj['nota'] = nota
            else:
                fallos.append('cadena de GM-mapas sin regla de traducción: ' + repr(es))
                continue
        except Exception as e:
            fallos.append('error traduciendo {!r}: {}'.format(es, e))
            continue

        # Autocomprobaciones
        en = obj['en']
        if not solo_latin1_ampliado(en):
            fallos.append('carácter no latino / € en EN: ' + repr(en))
        resto = restos_espanol(en)
        if resto:
            fallos.append('resto de español ({}) en EN: {!r}'.format(resto, en))
        if es in HOJAS.values() or (obj['en'] in mapas.HOJAS.values()):
            pass
        # nombres de pestaña (mapa-hoja): longitud <= 31
        for d in c['donde']:
            if d.get('t') == 'hoja':
                if len(obj['en']) > 31:
                    fallos.append('nombre de pestaña EN > 31: {!r}'.format(obj['en']))
                break

        salida.append(obj)

    return salida, fallos, len(cadenas)


def main():
    check_only = '--check' in sys.argv
    salida, fallos, n_es = construir()

    n_cifra = sum(1 for o in salida if o.get('cifra_derivada'))
    print('GM-mapas: {} cadenas ES, {} traducidas, {} marcadas cifra_derivada, {} fallos'.format(
        n_es, len(salida), n_cifra, len(fallos)))
    if fallos:
        for f in fallos:
            print('  FALLO:', f)

    if len(salida) != n_es:
        print('ABORTA: faltan cadenas sin traducir ({} de {})'.format(
            n_es - len(salida), n_es))
        sys.exit(2)
    if fallos:
        sys.exit(2)

    if not check_only:
        os.makedirs(OUT_DIR, exist_ok=True)
        with open(OUT_PATH, 'w', encoding='utf-8') as fh:
            json.dump(salida, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
        print('Escrito:', OUT_PATH)


if __name__ == '__main__':
    main()
