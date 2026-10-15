"""Volcado legible de los 8 xlsx ES: textos, entradas numéricas y fórmulas (solo lectura)."""
import sys, os, glob, re, openpyxl
ES = sys.argv[1]; OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)
for f in sorted(glob.glob(os.path.join(ES, '*.xlsx'))):
    wb = openpyxl.load_workbook(f)
    lines = []
    for ws in wb.worksheets:
        lines.append(f'##### SHEET {ws.title}  dims={ws.dimensions} freeze={ws.freeze_panes} prot={ws.protection.sheet}')
        for row in ws.iter_rows():
            parts = []
            for c in row:
                v = c.value
                if v is None: continue
                if c.data_type == 'f':
                    parts.append(f'{c.coordinate}={v}  [{c.number_format}]')
                elif isinstance(v, str):
                    parts.append(f'{c.coordinate}:"{v}"')
                else:
                    parts.append(f'{c.coordinate}#{v!r} [{c.number_format}]')
            if parts: lines.append(' | '.join(parts))
        for dv in ws.data_validations.dataValidation:
            lines.append(f'  DV {dv.sqref} type={dv.type} f1={dv.formula1} f2={dv.formula2} errT={dv.errorTitle!r} err={dv.error!r} pT={dv.promptTitle!r} p={dv.prompt!r}')
        for cf in ws.conditional_formatting:
            for r in cf.rules:
                lines.append(f'  CF {cf.sqref} {r.type} {r.formula} {r.operator}')
        lines.append(f'  HF footer={ws.oddFooter.center.text!r} header={ws.oddHeader.center.text!r} L={ws.oddFooter.left.text!r} R={ws.oddFooter.right.text!r}')
    open(os.path.join(OUT, os.path.basename(f) + '.txt'), 'w').write('\n'.join(lines))
    print(os.path.basename(f), len(lines))
