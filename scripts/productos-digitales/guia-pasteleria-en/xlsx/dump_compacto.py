"""Volcado compacto: textos + entradas numéricas por fila; fórmulas solo por patrón distinto (por columna)."""
import sys, os, re, openpyxl
f = sys.argv[1]; sheets = sys.argv[2:] or None
wb = openpyxl.load_workbook(f)
def patron(coord, v):
    col, row = re.match(r'([A-Z]+)(\d+)', coord).groups()
    return col + ':' + re.sub(r'(?<![A-Z$])(\$?[A-Z]{1,2})\$?' + row + r'(?!\d)', r'\1#', v)
for ws in wb.worksheets:
    if sheets and ws.title not in sheets: continue
    print(f'##### {ws.title} dims={ws.dimensions} freeze={ws.freeze_panes}')
    seen = set()
    for row in ws.iter_rows():
        parts = []
        for c in row:
            v = c.value
            if v is None: continue
            if c.data_type == 'f':
                p = patron(c.coordinate, v)
                if p not in seen:
                    seen.add(p); parts.append(f'{c.coordinate}={v} [{c.number_format}]')
            elif isinstance(v, str):
                parts.append(f'{c.coordinate}:"{v}"')
            else:
                parts.append(f'{c.coordinate}#{v!r} [{c.number_format}]')
        if parts: print(' | '.join(parts))
    for dv in ws.data_validations.dataValidation:
        print(f'  DV {str(dv.sqref)[:40]} type={dv.type} f1={dv.formula1} f2={dv.formula2}')
    for cf in ws.conditional_formatting:
        for r in cf.rules:
            print(f'  CF {cf.sqref} {r.type} {r.formula} {r.operator}')
