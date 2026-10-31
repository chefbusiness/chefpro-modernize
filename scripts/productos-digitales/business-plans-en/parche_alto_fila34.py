#!/usr/bin/env python3
"""
parche_alto_fila34.py — sube a 149.5 pt el alto de la fila 34 de «12-Month Cash Flow» en los planes EN LIVE (sesión
Claude Code, 31-oct-2026, PR #191). La nota del IVA del 4.º trimestre (A34) creció en #186 por parche XML y la fila se
quedó en 134.75 pt; el circuito (`aplicar_en.capa_altos`) le da 149.5 al regenerar. Parche XML del elemento
`<row r="34" …>` y nada más: el resto del zip viaja byte a byte (mismo método que `../parche_xml_xlsx.py`).

    python3 parche_alto_fila34.py [--apply] <xlsx>…      # sin --apply solo informa
"""
import re
import sys
import zipfile

VIEJO = '<row r="34" ht="134.75" customHeight="1">'
NUEVO = '<row r="34" ht="149.5" customHeight="1">'


def hoja_tesoreria(z):
    wb = z.read('xl/workbook.xml').decode('utf-8')
    rels = z.read('xl/_rels/workbook.xml.rels').decode('utf-8')
    for nombre, rid in re.findall(r'<sheet [^>]*name="([^"]+)"[^>]*r:id="([^"]+)"', wb):
        if nombre.endswith('12-Month Cash Flow'):
            dest = re.search(r'<Relationship [^>]*Id="%s"[^>]*Target="([^"]+)"' % rid, rels) or \
                re.search(r'<Relationship [^>]*Target="([^"]+)"[^>]*Id="%s"' % rid, rels)
            t = dest.group(1).lstrip('/')
            return t if t.startswith('xl/') else 'xl/' + t
    raise SystemExit('sin hoja «12-Month Cash Flow»')


def main(argv):
    apply = '--apply' in argv
    for ruta in [a for a in argv if not a.startswith('--')]:
        with zipfile.ZipFile(ruta) as zin:
            miembro = hoja_tesoreria(zin)
            entradas = [(i, zin.read(i.filename)) for i in zin.infolist()]
        xml = dict((i.filename, d) for i, d in entradas)[miembro].decode('utf-8')
        n = xml.count(VIEJO)
        if n != 1:
            raise SystemExit('%s: %d apariciones de %s (se esperaba 1)' % (ruta, n, VIEJO))
        nuevo = xml.replace(VIEJO, NUEVO).encode('utf-8')
        print('%s %s · %s' % ('PARCHEADO' if apply else 'PENDIENTE', ruta, miembro))
        if apply:
            tmp = ruta + '.tmp'
            with zipfile.ZipFile(tmp, 'w') as zout:
                for info, data in entradas:
                    zout.writestr(info, nuevo if info.filename == miembro else data, compress_type=info.compress_type)
            import os
            os.replace(tmp, ruta)


if __name__ == '__main__':
    main(sys.argv[1:])
