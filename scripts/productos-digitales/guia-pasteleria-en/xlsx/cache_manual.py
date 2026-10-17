#!/usr/bin/env python3
"""Caché a mano de las fórmulas que pycel no sabe evaluar (inject_cache.py las deja sin <v>).

El ES publicado trae el valor; el EN tiene que traer el mismo (traducido si es texto), o un visor que no recalcula
(Quick Look, móvil) la enseña en blanco. Valor comprobado a mano contra sus entradas (mismas en ES y EN).

    python3 cache_manual.py <dir_en>        # después de inject_cache.py, antes de gate_xlsx_en.py --cache
"""
import html
import os
import re
import sys
import zipfile

# (libro EN, pestaña EN, celda) -> valor. B32: payback = «Más de 3 años» en ES (24,230 + 47,186 + 50,357 < 227,916)
MANUAL = {('3-year-financial-plan.xlsx', '12-Month Cash Flow', 'B32'): 'More than 3 years'}


def parte_de(z, hoja):
    wb = z.read('xl/workbook.xml').decode()
    rels = z.read('xl/_rels/workbook.xml.rels').decode()
    relmap = {re.search(r'Id="([^"]+)"', r).group(1): re.search(r'Target="([^"]+)"', r).group(1)
              for r in re.findall(r'<Relationship [^>]*/>', rels)}
    for mm in re.finditer(r'<sheet [^>]*name="([^"]+)"[^>]*r:id="([^"]+)"', wb):
        if html.unescape(mm.group(1)) == hoja:
            t = relmap[mm.group(2)]
            return t.lstrip('/') if t.startswith('/') else 'xl/' + t
    raise SystemExit('no encuentro la pestaña %s' % hoja)


def main():
    d = sys.argv[1]
    for (libro, hoja, ref), val in MANUAL.items():
        ruta = os.path.join(d, libro)
        z = zipfile.ZipFile(ruta)
        parte = parte_de(z, hoja)
        x = z.read(parte).decode()
        rx = re.compile(r'<c r="%s"([^>]*)>(<f>.*?</f>)(?:<v>[^<]*</v>|<v\s*/>)?</c>' % ref, re.S)
        m = rx.search(x)
        if not m:
            raise SystemExit('%s!%s: no es una celda con fórmula' % (hoja, ref))
        attrs = re.sub(r'\st="[^"]*"', '', m.group(1))
        v = ('<v>%s</v>' % html.escape(val, quote=False)) if isinstance(val, str) else '<v>%r</v>' % val
        t = ' t="str"' if isinstance(val, str) else ''
        x = x[:m.start()] + '<c r="%s"%s%s>%s%s</c>' % (ref, attrs, t, m.group(2), v) + x[m.end():]
        tmp = ruta + '.tmp'
        with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zo:
            for info in z.infolist():
                zo.writestr(info, x.encode() if info.filename == parte else z.read(info.filename))
        z.close()
        os.replace(tmp, ruta)
        print('%s · %s!%s ← %r' % (libro, hoja, ref, val))


if __name__ == '__main__':
    main()
