"""sha256 canónico de un xlsx/docx: miembros del zip ordenados, sin las fechas created/modified de docProps/core.xml.
Copia de /tmp/canon_piz.py (regresión de la pizza, 25-oct-2026), versionada para el paso 4 de la heladería.

    python3 canon.py <generado> <publicado>      # IGUAL / DISTINTO + 16 primeros del sha canónico; rc 0 si IGUAL
"""
import hashlib
import re
import sys
import zipfile


def canon(p):
    h = hashlib.sha256()
    with zipfile.ZipFile(p) as z:
        for n in sorted(z.namelist()):
            b = z.read(n)
            if n == 'docProps/core.xml':
                b = re.sub(rb'<dcterms:(created|modified)[^>]*>[^<]*</dcterms:\1>', b'', b)
            h.update(n.encode() + b'\0' + b + b'\0')
    return h.hexdigest()


if __name__ == '__main__':
    a, b = sys.argv[1], sys.argv[2]
    ca, cb = canon(a), canon(b)
    print('%s %s %s' % ('IGUAL' if ca == cb else 'DISTINTO', ca[:16], b))
    sys.exit(0 if ca == cb else 1)
