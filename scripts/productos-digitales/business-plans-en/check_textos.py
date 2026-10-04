#!/usr/bin/env python3
"""
check_textos.py — validador de la salida de los traductores (BRIEF-TRADUCTORES.md). Solo lee JSON: no necesita
openpyxl ni python-docx (corre en el Mac sin carga).

    python3 check_textos.py --tanda GM        # textos_en/GM.json   contra textos_es.json (grupo GM)
    python3 check_textos.py --tanda GFT       # textos_en/GFT.json
    python3 check_textos.py --tanda GCAF      # textos_en/GCAF.json
    python3 check_textos.py --tanda ft_a      # docx_en_ft_a.json   contra docx_es_ft.json (tanda ft_a)
    python3 check_textos.py --tanda ft_b | caf_a | caf_b
    python3 check_textos.py --todas           # las 7 que existan (las que falten se informan, no fallan)
    [--fichero RUTA]  valida otro fichero con el formato de la tanda

Sale con código 1 si hay ERRORES (los AVISOS no bloquean, pero hay que mirarlos). Comprueba:
  · ids/párrafos EXACTOS de la tanda (ni faltan ni sobran) y valores de texto no vacíos;
  · límites de Excel (max_len 32 / 255) en los xlsx;
  · cero español (tildes fuera de la lista blanca, palabras funcionales y de oficio, siglas y normativa ES, coma
    decimal, «€», «EUR», «euros», « », ¿ ¡), cero caracteres no latinos, cero «ChefBusiness» / «chefbusiness.co»,
    cero IDs internos (SPEC, D9, [kit estimate]…), nunca «SBA minimum» ni «approval guaranteed» / «verified»;
  · xlsx: pestañas citadas con su nombre EN; prefijos «▸» y numeración «N.» conservados; sin tokens {{…}};
  · docx: tokens {{nombre}} válidos para el plan (mapas.tokens_de) y bien formados; importes «$» y porcentajes
    FUERA de tokens solo si están en F1-research-us.md o SPEC.md (datos de mercado con fuente); subtítulos de una
    línea sin punto final; nota UK en el último párrafo de §9; CAF 134 con ≥ 3 tokens; sin ciudades españolas.
"""
import argparse
import json
import os
import re
import sys
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import mapas                                                     # noqa: E402

XLSX = ('GM', 'GFT', 'GCAF')
DOCX = tuple(mapas.DOCX_TANDAS)
CIUDADES_ES = re.compile(r'\b(?:Madrid|Barcelona|Valencia|Bilbao|Sevilla|Seville|M[aá]laga|Zaragoza|Spain|Spanish '
                         r'market|España)\b')
PROHIBIDO = re.compile(r'SBA minimum|minimum required by the SBA|approval (?:is )?guaranteed|guaranteed approval|'
                       r'\bverified against\b', re.I)
RX_DOLAR = re.compile(r'\$\s?(\d[\d,]*(?:\.\d+)?)\s?(K|M|million|thousand)?(?:\s?[-–]\s?\$?\s?(\d[\d,]*(?:\.\d+)?)\s?'
                      r'(K|M|million|thousand)?)?', re.I)
RX_PCT = re.compile(r'(\d+(?:\.\d+)?)(?:\s?%?\s?[-–]\s?(\d+(?:\.\d+)?))?\s?%')


def _mult(suf):
    s = (suf or '').lower()
    return 1e3 if s in ('k', 'thousand') else (1e6 if s in ('m', 'million') else 1)


def _num_us(s):
    return float(s.replace(',', ''))


def _candidatos(s):
    """Número de un texto de la SPEC/research (formato ES o US): devuelve las lecturas posibles."""
    out = set()
    s = s.strip().rstrip('.,')
    if not s:
        return out
    if ',' in s and '.' in s:
        if s.rfind(',') > s.rfind('.'):
            out.add(float(s.replace('.', '').replace(',', '.')))
        else:
            out.add(float(s.replace(',', '')))
    elif ',' in s:
        a, b = s.rsplit(',', 1)
        out.add(float(s.replace(',', '')))                   # 26,001 (US miles)
        if len(b) <= 2:
            out.add(float(a.replace(',', '') + '.' + b))     # 7,25 (ES decimal)
    elif '.' in s:
        a, b = s.rsplit('.', 1)
        out.add(float(s))                                    # 7.25 (US decimal)
        if len(b) == 3:
            out.add(float(s.replace('.', '')))               # 30.000 (ES miles)
    else:
        out.add(float(s))
    return out


def cifras_permitidas():
    """Importes y porcentajes citables sin token: los de F1-research-us.md y SPEC.md (más las reglas de mapas)."""
    dol, pct = set(), set()
    textos = []
    for f in ('F1-research-us.md', 'SPEC.md'):
        p = os.path.join(AQUI, f)
        if os.path.exists(p):
            textos.append(open(p, encoding='utf-8').read())
    textos += [v for v, _f in mapas.REGLAS_US.values()]
    rx_d = re.compile(r'\$\s?(\d[\d.,]*)\s?(K|M)?(?:\s?[-–]\s?\$?\s?(\d[\d.,]*)\s?(K|M)?)?')
    rx_p = re.compile(r'(\d[\d.,]*)(?:\s?%?\s?[-–]\s?(\d[\d.,]*))?\s?%')
    for t in textos:
        for m in rx_d.finditer(t):
            for g, suf in ((m.group(1), m.group(2) or m.group(4)), (m.group(3), m.group(4))):
                if g:
                    for v in _candidatos(g):
                        dol.add(round(v * _mult(suf), 2))
        for m in rx_p.finditer(t):
            for g in (m.group(1), m.group(2)):
                if g:
                    pct |= {round(v, 2) for v in _candidatos(g)}
    return dol, pct


def cifras_texto(t):
    """Importes ($) y porcentajes de un texto EN (formato US) fuera de tokens."""
    t = mapas.RX_TOKEN.sub(' ', t)
    dol, pct = [], []
    for m in RX_DOLAR.finditer(t):
        a, sa, b, sb = m.groups()
        sa = sa or sb
        dol.append((round(_num_us(a) * _mult(sa), 2), m.group(0)))
        if b:
            dol.append((round(_num_us(b) * _mult(sb), 2), m.group(0)))
    for m in RX_PCT.finditer(t):
        for g in (m.group(1), m.group(2)):
            if g:
                pct.append((round(float(g), 2), m.group(0)))
    return dol, pct


def comunes(t, donde, err, avi):
    # Los NOMBRES de token ({{mes_saldo_minimo}}, {{fondos_propios}}…) son identificadores internos en español: se
    # quitan antes de buscar restos de español, que si no cuentan «mes», «saldo»… como texto (falso positivo).
    t_sin_tokens = mapas.RX_TOKEN.sub(' ', t)
    for motivo, ctx in mapas.restos_espanol(t_sin_tokens):
        (avi if motivo.startswith('oficio') else err).append('%s: %s · «%s»' % (donde, motivo, ctx.strip()[:70]))
    nl = mapas.no_latinos(t)
    if nl:
        err.append('%s: caracteres no latinos %s' % (donde, nl))
    if mapas.RX_ID_INTERNO.search(t):
        err.append('%s: ID interno «%s»' % (donde, mapas.RX_ID_INTERNO.search(t).group(0)))
    if PROHIBIDO.search(t):
        err.append('%s: afirmación prohibida «%s»' % (donde, PROHIBIDO.search(t).group(0)))
    if CIUDADES_ES.search(t):
        err.append('%s: referencia española «%s»' % (donde, CIUDADES_ES.search(t).group(0)))
    if '  ' in t.strip('\n'):
        avi.append('%s: doble espacio' % donde)


def check_xlsx(tanda, fichero, err, avi):
    te = json.load(open(os.path.join(AQUI, 'textos_es.json'), encoding='utf-8'))
    esperadas = OrderedDict((e['id'], e) for e in te['cadenas'] if e['grupo'] == tanda)
    en = json.load(open(fichero, encoding='utf-8'))
    if not isinstance(en, dict):
        err.append('%s: el fichero debe ser un objeto {id: texto}' % fichero)
        return
    falta = [k for k in esperadas if k not in en]
    sobra = [k for k in en if k not in esperadas]
    if falta:
        err.append('faltan %d ids: %s' % (len(falta), ', '.join(falta[:15])))
    if sobra:
        err.append('sobran %d ids (no son de %s): %s' % (len(sobra), tanda, ', '.join(sobra[:15])))
    for k, v in en.items():
        if k not in esperadas:
            continue
        e = esperadas[k]
        donde = '%s (%s)' % (k, e['donde'][0].get('h', '') + '!' + str(e['donde'][0].get('c', '')))
        if not isinstance(v, str) or not v.strip():
            if e['es'].strip():
                err.append('%s: texto vacío' % donde)
            continue
        if 'max_len' in e and len(v) > e['max_len']:
            err.append('%s: %d caracteres > %d (límite de Excel)' % (donde, len(v), e['max_len']))
        if mapas.RX_TOKEN.search(v) or '{{' in v:
            err.append('%s: los xlsx no llevan tokens {{…}}' % donde)
        comunes(v, donde, err, avi)
        for ch in e.get('cita_hojas', []):
            ens = [x.strip() for x in ch['en'].split('/')] if ch['en'] else []
            if ens and not any(x in v for x in ens):
                err.append('%s: cita la pestaña «%s» y el EN no nombra "%s"' % (donde, ch['es'], ch['en']))
        if e['es'].startswith('▸') and not v.startswith('▸'):
            err.append('%s: el ES empieza por «▸» y el EN no' % donde)
        m = re.match(r'^(\d+)\. ', e['es'])
        if m and not v.startswith(m.group(1) + '. '):
            err.append('%s: el ES va numerado «%s.» y el EN no' % (donde, m.group(1)))
        if not e.get('por_celda'):
            r = len(v) / max(1, len(e['es']))
            if len(e['es']) > 40 and (r < 0.4 or r > 2.2):
                avi.append('%s: longitud EN/ES = %.1f' % (donde, r))
    print('  %s: %d ids esperados · %d recibidos' % (tanda, len(esperadas), len(en)))


def check_docx(tanda, fichero, err, avi):
    plan, secs = mapas.DOCX_TANDAS[tanda]
    de = json.load(open(os.path.join(AQUI, 'docx_es_%s.json' % plan), encoding='utf-8'))
    esperadas = OrderedDict((k, e) for k, e in de['parrafos'].items() if e.get('traducir') and e.get('tanda') == tanda)
    en = json.load(open(fichero, encoding='utf-8'))
    if not isinstance(en, dict):
        err.append('%s: el fichero debe ser un objeto {"índice": "texto"}' % fichero)
        return
    falta = [k for k in esperadas if k not in en]
    sobra = [k for k in en if k not in esperadas]
    if falta:
        err.append('faltan %d párrafos: %s' % (len(falta), ', '.join(falta)))
    if sobra:
        err.append('sobran %d párrafos (no son de %s o son fijos): %s' % (len(sobra), tanda, ', '.join(sobra[:20])))
    validos = set(mapas.tokens_de(plan))
    dol_ok, pct_ok = cifras_permitidas()
    n_tok = 0
    for k, v in en.items():
        if k not in esperadas:
            continue
        e = esperadas[k]
        donde = '%s[%s]' % (plan, k)
        if not isinstance(v, str) or not v.strip():
            err.append('%s: texto vacío' % donde)
            continue
        comunes(v, donde, err, avi)
        toks = mapas.RX_TOKEN.findall(v)
        n_tok += len(toks)
        for t in toks:
            if t not in validos:
                err.append('%s: token desconocido para %s: {{%s}}' % (donde, plan, t))
        resto = mapas.RX_TOKEN.sub('', v)
        if '{' in resto or '}' in resto:
            err.append('%s: llaves sueltas (token mal escrito)' % donde)
        dol, pct = cifras_texto(v)
        for val, txt in dol:
            if val not in dol_ok:
                err.append('%s: importe «%s» sin token ni fuente en research/SPEC (usa un token o redacta sin cifra)'
                           % (donde, txt))
        for val, txt in pct:
            if val not in pct_ok:
                err.append('%s: porcentaje «%s» sin token ni fuente en research/SPEC' % (donde, txt))
        if e['rol'] == 'subtitulo':
            if '\n' in v or len(v) > 80 or v.rstrip().endswith('.'):
                err.append('%s: subtítulo: una línea, < 80 caracteres, sin punto final' % donde)
        else:
            if '\n' in v:
                err.append('%s: un párrafo de cuerpo no lleva saltos de línea' % donde)
            r = len(v.split()) / max(1, e['palabras'])
            if r < 0.5 or r > 1.8:
                avi.append('%s: palabras EN/ES = %.2f' % (donde, r))
    # reglas por párrafo
    ult9 = {'ft': '108', 'caf': '142'}[plan]
    if ult9 in en and not re.search(r'\bUK\b|United Kingdom', en[ult9]):
        err.append('%s[%s]: el último párrafo de §9 debe cerrar con la nota UK (D22)' % (plan, ult9))
    if plan == 'caf' and '134' in en and len(mapas.RX_TOKEN.findall(en['134'])) < 3:
        err.append('caf[134]: el resumen de §8 debe citar sus cifras con tokens (≥ 3)')
    print('  %s: %d párrafos esperados · %d recibidos · %d tokens' % (tanda, len(esperadas), len(en), n_tok))


def fichero_de(tanda):
    if tanda in XLSX:
        return os.path.join(AQUI, 'textos_en', '%s.json' % tanda)
    return os.path.join(AQUI, 'docx_en_%s.json' % tanda)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('--tanda', choices=XLSX + DOCX)
    ap.add_argument('--todas', action='store_true')
    ap.add_argument('--fichero')
    args = ap.parse_args()
    if not args.tanda and not args.todas:
        ap.error('--tanda X o --todas')
    tandas = list(XLSX + DOCX) if args.todas else [args.tanda]
    total_err = 0
    for t in tandas:
        f = args.fichero if (args.fichero and not args.todas) else fichero_de(t)
        if not os.path.exists(f):
            print('%s: falta %s' % (t, os.path.relpath(f, AQUI)))
            if not args.todas:
                total_err += 1
            continue
        err, avi = [], []
        try:
            (check_xlsx if t in XLSX else check_docx)(t, f, err, avi)
        except json.JSONDecodeError as ex:
            err.append('JSON inválido: %s' % ex)
        for x in err:
            print('ERROR', t, x)
        for x in avi:
            print('AVISO', t, x)
        print('%s: %s (%d errores, %d avisos)' % (t, 'OK' if not err else 'ROJO', len(err), len(avi)))
        total_err += len(err)
    return 1 if total_err else 0


if __name__ == '__main__':
    sys.exit(main())
