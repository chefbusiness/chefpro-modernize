#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Censo de vocabulario y terminos de los productos digitales ES (docx/xlsx). Python 3.7, solo stdlib."""
import argparse, collections, glob, html, json, os, re, sys, time, zipfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
PUBLIC = os.path.join(ROOT, 'astro-site', 'public')
TS = os.path.join(ROOT, 'netlify', 'functions', 'get-download-urls.ts')
ZONA = os.path.join(ROOT, 'astro-site', 'src', 'lib', 'zona-app.ts')

STOP = set("""
que los las del con por para una uno unos unas como más mas pero sus este esta esto estos estas ese esa eso esos esas
también tambien muy sin sobre entre cuando donde desde hasta hay son ser fue era han has hemos has está están estan estar
cada todo toda todos todas otro otra otros otras mismo misma así asi aquí aqui allí ahí ahi cual cuál cuales quien
quién qué cómo cuándo dónde porque porqué pues sea sean será serán puede pueden puedes podemos debe deben debes
tiene tienen tienes tengo tener hacer hace hacen haces según segun tras ante bajo contra durante mediante
nos les mis tus nuestro nuestra nuestros nuestras vuestro suyo suya suyos suyas aun aún ya sí si no ni nada algo
alguna alguno algunos algunas ninguna ninguno solo sólo sola solos tan tanto tanta tantos tantas mucho mucha muchos muchas
poco poca pocos pocas demás demas cuyo cuya dicho dicha siempre nunca jamás casi otra vez veces luego antes después despues
ahora entonces además ademas incluso unos esto eso aquello aquel aquella aquellos aquellas lo la el le se me te al de en un y o u a e
sido siendo sido haber habrá había habia hubo han fueron seria sería vez parte forma tipo caso etc num
""".split())
STOP = set(w for w in STOP if len(w) >= 3) | set(["que", "los", "las"])
TOKRE = re.compile(r'[a-záéíóúüñ]+')


def read_registry():
    txt = open(TS, encoding='utf-8').read()
    prods = collections.OrderedDict()
    cur = None
    for line in txt.split('\n'):
        m = re.match(r"^  '([^']+)':\s*\{\s*$", line)
        if m:
            cur = m.group(1)
            prods[cur] = []
            continue
        if re.match(r"^  \},?\s*$", line):
            cur = None
            continue
        if cur:
            m = re.match(r"^\s{4}'[^']+':\s*'(/dl/[^']+)'", line)
            if m:
                prods[cur].append(m.group(1))
    zona = open(ZONA, encoding='utf-8').read()
    en = set(re.findall(r"productId:\s*'([^']+)'[^\n]*?lang:\s*'en'", zona))
    es = collections.OrderedDict((k, v) for k, v in prods.items() if k not in en)
    pp = sorted(glob.glob(os.path.join(PUBLIC, 'dl', 'b1-*.docx')) + glob.glob(os.path.join(PUBLIC, 'dl', 'b23-*.xlsx')))
    es['pro-prompts-ebook'] = ['/dl/' + os.path.basename(p) for p in pp]
    return es, en


def xml_text(raw):
    return raw.decode('utf-8', 'replace')


def extract_docx(z):
    out = []
    names = z.namelist()
    sel = [n for n in names if n == 'word/document.xml' or re.match(r'word/(header|footer)\d*\.xml$', n) or n == 'word/footnotes.xml']
    for n in sel:
        x = xml_text(z.read(n))
        x = x.replace('</w:p>', '\n</w:p>')
        parts = []
        for m in re.finditer(r'<w:t(?:\s[^>]*)?>([^<]*)</w:t>|\n', x):
            parts.append('\n' if m.group(0) == '\n' else m.group(1))
        out.append(html.unescape(''.join(parts)))
    return '\n'.join(out)


def extract_xlsx(z):
    out = []
    names = z.namelist()
    if 'xl/sharedStrings.xml' in names:
        x = xml_text(z.read('xl/sharedStrings.xml'))
        for si in re.findall(r'<si>(.*?)</si>', x, re.S):
            t = ''.join(re.findall(r'<t(?:\s[^>]*)?>([^<]*)</t>', si))
            out.append(html.unescape(t))
    for n in names:
        if re.match(r'xl/worksheets/sheet\d+\.xml$', n):
            x = xml_text(z.read(n))
            for is_ in re.findall(r'<is>(.*?)</is>', x, re.S):
                out.append(html.unescape(''.join(re.findall(r'<t(?:\s[^>]*)?>([^<]*)</t>', is_))))
    if 'xl/workbook.xml' in names:
        x = xml_text(z.read('xl/workbook.xml'))
        for s in re.findall(r'<sheet\s[^>]*?name="([^"]*)"', x):
            out.append(html.unescape(s))
    return '\n'.join(out)


def load_all():
    es, en = read_registry()
    filetext = {}
    stats = {'leidos': 0, 'saltados': 0, 'ausentes': [], 'errores': []}
    prodtext = {}
    prodfiles = {}
    for slug, paths in es.items():
        chunks = []
        nf = 0
        for p in paths:
            fp = PUBLIC + p
            ext = os.path.splitext(p)[1].lower()
            # La guía de equivalencias es la SALIDA de este censo, no texto del producto: leerla
            # (existe desde el 13-oct) metía sus 200 términos en la cuenta de cada producto (25-oct).
            if os.path.basename(p).startswith('guia-equivalencias'):
                continue
            if ext not in ('.docx', '.xlsx'):
                if p not in filetext:
                    stats['saltados'] += 1
                    filetext[p] = None
                continue
            if p not in filetext:
                if not os.path.exists(fp):
                    stats['ausentes'].append(p)
                    filetext[p] = None
                else:
                    try:
                        z = zipfile.ZipFile(fp)
                        filetext[p] = extract_docx(z) if ext == '.docx' else extract_xlsx(z)
                        z.close()
                        stats['leidos'] += 1
                    except Exception as e:
                        stats['errores'].append((p, str(e)))
                        filetext[p] = None
            if filetext[p] is not None:
                chunks.append(filetext[p])
                nf += 1
        prodtext[slug] = '\n'.join(chunks)
        prodfiles[slug] = nf
    return es, en, prodtext, prodfiles, stats


def do_vocab(outdir, es, prodtext, prodfiles):
    os.makedirs(outdir, exist_ok=True)
    uni = collections.defaultdict(collections.Counter)
    bi = collections.defaultdict(collections.Counter)
    for slug, text in prodtext.items():
        for line in text.casefold().split('\n'):
            toks = [t if (len(t) >= 3 and t not in STOP) else None for t in TOKRE.findall(line)]
            for i, t in enumerate(toks):
                if t is None:
                    continue
                uni[t][slug] += 1
                if i + 1 < len(toks) and toks[i + 1] is not None:
                    bi[t + ' ' + toks[i + 1]][slug] += 1

    def dump(d, path, top):
        rows = []
        for tok, c in d.items():
            rows.append((tok, len(c), sum(c.values()), c.most_common(3)))
        rows.sort(key=lambda r: (-r[1], -r[2], r[0]))
        with open(path, 'w', encoding='utf-8') as f:
            f.write('token\tn_productos\ttotal\ttop_productos\n')
            for tok, n, tot, tp in rows[:top]:
                f.write('%s\t%d\t%d\t%s\n' % (tok, n, tot, '; '.join('%s:%d' % x for x in tp)))
        return rows[:top]

    ru = dump(uni, os.path.join(outdir, 'vocab-unigramas.tsv'), 4000)
    rb = dump(bi, os.path.join(outdir, 'vocab-bigramas.tsv'), 3000)
    with open(os.path.join(outdir, 'productos.json'), 'w', encoding='utf-8') as f:
        json.dump({s: {'archivos': prodfiles[s], 'caracteres': len(prodtext[s])} for s in es}, f, ensure_ascii=False, indent=1)
    return ru, rb


def compile_pat(p):
    return re.compile(r'(?<![a-záéíóúüñ])(?:' + p + r')(?![a-záéíóúüñ])', re.I)


def count_terms(terms, prodtext):
    cps = [(t['id'], [compile_pat(p) for p in t['patrones']]) for t in terms]
    res = {}
    for slug, text in prodtext.items():
        low = text.casefold()
        res[slug] = {}
        for tid, pats in cps:
            res[slug][tid] = sum(len(p.findall(low)) for p in pats)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--vocab')
    ap.add_argument('--terms')
    ap.add_argument('--out')
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--debug', help='id de termino: imprime 5 contextos (60 car. a cada lado)')
    a = ap.parse_args()
    t0 = time.time()
    es, en, prodtext, prodfiles, stats = load_all()
    print('Productos ES: %d (EN excluidos: %d)' % (len(es), len(en)))
    if len(es) != 57:
        print('ERROR: se esperaban 57 productos ES. Lista:')
        for s in es:
            print(' ', s, len(es[s]))
        sys.exit(1)
    print('Archivos leidos: %d, saltados (pdf/otros): %d, ausentes: %d, errores: %d' % (
        stats['leidos'], stats['saltados'], len(stats['ausentes']), len(stats['errores'])))
    for p in stats['ausentes'][:30]:
        print('  AUSENTE', p)
    for p, e in stats['errores'][:10]:
        print('  ERROR', p, e)
    empty = [s for s in es if len(prodtext[s]) == 0]
    if empty:
        print('Productos sin texto:', ', '.join(empty))

    if a.vocab:
        ru, rb = do_vocab(a.vocab, es, prodtext, prodfiles)
        print('TOP 60 unigramas: ' + ', '.join('%s(%d/%d)' % (r[0], r[1], r[2]) for r in ru[:60]))
        print('TOP 40 bigramas: ' + ', '.join('%s(%d/%d)' % (r[0], r[1], r[2]) for r in rb[:40]))
    if a.debug:
        terms = json.load(open(a.terms, encoding='utf-8'))
        t = [x for x in terms if x['id'] == a.debug][0]
        shown = 0
        for slug, text in prodtext.items():
            low = text.casefold()
            for pat in t['patrones']:
                for m in compile_pat(pat).finditer(low):
                    if shown >= 5:
                        break
                    c = low[max(0, m.start() - 60):m.end() + 60].replace('\n', ' / ')
                    print('[%s] ...%s...' % (slug, c))
                    shown += 1
        sys.exit(0)
    if a.terms:
        if not a.out:
            ap.error('--terms requiere --out')
        terms = json.load(open(a.terms, encoding='utf-8'))
        cnt = count_terms(terms, prodtext)
        out = {'productos': {s: {'archivos': prodfiles[s], 'terminos': cnt[s]} for s in es}, 'terminos': {}}
        for t in terms:
            tid = t['id']
            per = sorted(((s, cnt[s][tid]) for s in es if cnt[s][tid] > 0), key=lambda x: -x[1])
            out['terminos'][tid] = {'total': sum(x[1] for x in per), 'productos': len(per), 'top': [list(x) for x in per[:3]]}
        with open(a.out, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, indent=1)
        zero = [k for k, v in out['terminos'].items() if v['total'] == 0]
        print('Terminos: %d; con 0 apariciones: %d %s' % (len(terms), len(zero), zero[:30]))
    if a.check:
        ok = True
        for pat, slug in (('escandallo', 'kit-escandallos'), ('appcc', 'pack-appcc')):
            c = len(compile_pat(pat).findall(prodtext.get(slug, '').casefold()))
            print('control %s en %s: %d -> %s' % (pat, slug, c, 'OK' if c > 0 else 'FAIL'))
            ok = ok and c > 0
        neg = len(compile_pat('escandallo').findall(prodtext.get('kit-tareas-hotel', '').casefold()))
        print('control negativo escandallo en kit-tareas-hotel: %d' % neg)
        print('CHECK ' + ('OK' if ok else 'FAIL'))
        if not ok:
            sys.exit(1)
    print('Tiempo: %.1f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
