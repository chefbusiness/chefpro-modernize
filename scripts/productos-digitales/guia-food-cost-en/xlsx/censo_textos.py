"""Censo de cadenas a traducir en los 8 xlsx ES: celdas de texto, literales de fórmulas, DV, CF, cabeceras/pies,
gráficos y docProps. Salida: textos_es.json {libro: {cadena: [lugares]}} + resumen. Solo lectura."""
import sys, os, glob, re, json, zipfile, html, openpyxl
from collections import OrderedDict
ES = sys.argv[1]; OUT = sys.argv[2]
LIT = re.compile(r'"((?:[^"]|"")*)"')
res = OrderedDict(); tot_words = 0
def add(d, s, where):
    if s is None or s == '' : return
    d.setdefault(s, []).append(where)
for f in sorted(glob.glob(os.path.join(ES, '*.xlsx'))):
    name = os.path.basename(f); d = OrderedDict()
    wb = openpyxl.load_workbook(f)
    for ws in wb.worksheets:
        add(d, ws.title, f'sheetname')
        for row in ws.iter_rows():
            for c in row:
                v = c.value
                if isinstance(v, str):
                    if c.data_type == 'f':
                        for m in LIT.finditer(v):
                            s = m.group(1).replace('""', '"')
                            if re.search(r'[A-Za-zÁÉÍÓÚáéíóúñÑ]', s): add(d, s, f'{ws.title}!{c.coordinate} [formula-lit]')
                    else:
                        add(d, v, f'{ws.title}!{c.coordinate}')
        for dv in ws.data_validations.dataValidation:
            for a in ('errorTitle', 'error', 'promptTitle', 'prompt'):
                add(d, getattr(dv, a), f'{ws.title} DV {a} {str(dv.sqref)[:20]}')
            if dv.type == 'list' and dv.formula1 and dv.formula1.startswith('"'):
                for it in dv.formula1.strip('"').split(','):
                    if re.search(r'[A-Za-zÁÉÍÓÚáéíóúñÑ]', it): add(d, it, f'{ws.title} DVlist {str(dv.sqref)[:20]}')
        for cf in ws.conditional_formatting:
            for r in cf.rules:
                for fx in (r.formula or []):
                    for m in LIT.finditer(fx):
                        add(d, m.group(1), f'{ws.title} CF {cf.sqref}')
        for hf in (ws.oddFooter, ws.oddHeader, ws.evenFooter, ws.firstFooter):
            for part in (hf.left, hf.center, hf.right):
                add(d, part.text, f'{ws.title} HF')
    p = wb.properties
    for a in ('title', 'subject', 'creator', 'description', 'keywords', 'category', 'lastModifiedBy'):
        add(d, getattr(p, a), f'docProps {a}')
    z = zipfile.ZipFile(f)
    for n in z.namelist():
        if n.startswith('xl/charts/'):
            x = z.read(n).decode()
            for t in re.findall(r'<a:t>([^<]*)</a:t>|<c:v>([^<]*)</c:v>', x):
                s = html.unescape(t[0] or t[1])
                if re.search(r'[A-Za-zÁÉÍÓÚáéíóúñÑ]', s): add(d, s, f'chart {n}')
            for t in re.findall(r'<c:f>([^<]*)</c:f>', x): add(d, html.unescape(t), f'chart-ref {n}')
    res[name] = d
    w = sum(len(s.split()) for s in d)
    tot_words += w
    print(f'{name}: {len(d)} unique strings, {w} words')
print('TOTAL words', tot_words)
json.dump(res, open(OUT, 'w'), ensure_ascii=False, indent=1)
