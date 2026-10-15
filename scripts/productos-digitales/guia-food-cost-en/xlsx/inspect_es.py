"""Inspección del paquete de los 8 xlsx ES (solo lectura)."""
import zipfile, re, sys, glob, os
ES = sys.argv[1]
for f in sorted(glob.glob(os.path.join(ES, '*.xlsx'))):
    z = zipfile.ZipFile(f)
    names = z.namelist()
    print('==', os.path.basename(f), len(names), 'parts')
    print('  ', ' '.join(n for n in names if not n.startswith('xl/worksheets/sheet')))
    wb = z.read('xl/workbook.xml').decode()
    print('   sheets:', re.findall(r'<sheet [^>]*name="([^"]+)"', wb))
    dn = re.findall(r'<definedName[^>]*>.*?</definedName>', wb)
    print('   definedNames:', dn[:20])
    for n in names:
        if n.startswith('xl/worksheets/sheet'):
            x = z.read(n).decode()
            feats = {k: len(re.findall(p, x)) for k, p in [('dv', r'<dataValidation '), ('cf', r'<conditionalFormatting'), ('hf', r'<headerFooter'), ('prot', r'<sheetProtection'), ('drawing', r'<drawing '), ('merge', r'<mergeCell '), ('f', r'<f>|<f '), ('pane', r'<pane '), ('print', r'<pageSetup'), ('inlineStr', r't="inlineStr"'), ('str', r't="str"')]}
            print('  ', n, feats)
    st = z.read('xl/styles.xml').decode()
    print('   numFmts:', re.findall(r'formatCode="([^"]+)"', st))
