#!/usr/bin/env python3
"""PDF real para las 6 guías ES v1 que entregaban una portada de 1 página (25-oct-2026, sesión Claude Code).

Las guías panadería-obrador, casual, japonés, mexicano, nikkei y peruano salieron de los generadores
v1 (`scripts/generate-guia-restaurante-*.py`; la panadería vino de ChefBusiness), cuyo `gen_guide_pdf()`
dibujaba con reportlab una portada con «60+ páginas» y nada más. Este script, en el VPS (LibreOffice +
Carlito: `apt-get install libreoffice-writer-nogui fonts-crosextra-carlito`):

  1. Parchea el XML del docx, sin tocar el resto del zip:
     - página Letter → A4;
     - el párrafo vacío con salto de página antes de cada capítulo pasa a `pageBreakBefore` del
       Heading1 (si el capítulo anterior llenaba la página, el salto dejaba una página en blanco);
     - las listas numeradas (estilo ListNumber, un único numId) reinician en 1 bajo cada encabezado
       (antes seguían la cuenta de la lista anterior: «12. Instagram…»).
  2. Exporta el PDF con LibreOffice y lo mide (páginas, A4, páginas vacías).

Idempotente. Uso (VPS, worktree de la rama):
    ssh vps 'HOME=/tmp/lo-home /root/venv-guias/bin/python - /root/<worktree>' < pdf_guias_v1.py

OJO: si alguien vuelve a correr un generador v1, pisa estos parches; correr este script después.
Las páginas anunciadas en las landings las vigila `paginas-gate.py`.
"""
import os, re, shutil, subprocess, sys, tempfile, zipfile

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
os.chdir(ROOT)
GUIAS = ['panaderia-obrador', 'restaurante-casual', 'restaurante-japones',
         'restaurante-mexicano', 'restaurante-nikkei', 'restaurante-peruano',
         # Su PDF era real pero maquetado aparte (reportlab, 10 págs.) y la landing anunciaba 119: PDF = Word
         # como las otras 6 (25-oct-2026, PR aparte).
         'restaurante-gastronomico']
LETTER = '<w:pgSz w:w="12240" w:h="15840"/>'
A4 = '<w:pgSz w:w="11906" w:h="16838"/>'
SALTO = '<w:p><w:r><w:br w:type="page"/></w:r></w:p><w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr>'
SALTO_OK = '<w:p><w:pPr><w:pStyle w:val="Heading1"/><w:pageBreakBefore/></w:pPr>'
LN = '<w:pPr><w:pStyle w:val="ListNumber"/></w:pPr>'
PARRAFO = re.compile(r'<w:p(?: [^>]*)?>.*?</w:p>', re.S)


def reiniciar_listas(doc, styles, numbering):
    """Un w:num nuevo (startOverride 1) por cada grupo de ListNumber a partir del segundo."""
    m = re.search(r'w:styleId="ListNumber".*?<w:numId w:val="(\d+)"/>', styles, re.S)
    if not m or LN not in doc:
        return doc, numbering, 0
    abstracto = re.search(r'<w:num w:numId="%s"><w:abstractNumId w:val="(\d+)"/>' % m.group(1), numbering).group(1)
    siguiente = max(int(n) for n in re.findall(r'<w:num w:numId="(\d+)"', numbering)) + 1
    trozos, ultimo, grupo, visto, nuevos = [], 0, -1, False, []
    for p in PARRAFO.finditer(doc):
        x = p.group(0)
        if 'w:val="Heading' in x:
            visto = False
        elif LN in x:
            if not visto:
                grupo += 1
                visto = True
                if grupo >= 1:
                    nuevos.append(siguiente)
                    siguiente += 1
            if grupo >= 1:
                numpr = '<w:pPr><w:pStyle w:val="ListNumber"/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="%d"/></w:numPr></w:pPr>' % nuevos[-1]
                trozos.append(doc[ultimo:p.start()])
                trozos.append(x.replace(LN, numpr, 1))
                ultimo = p.end()
    trozos.append(doc[ultimo:])
    nums = ''.join('<w:num w:numId="%d"><w:abstractNumId w:val="%s"/><w:lvlOverride w:ilvl="0">'
                   '<w:startOverride w:val="1"/></w:lvlOverride></w:num>' % (n, abstracto) for n in nuevos)
    return ''.join(trozos), numbering.replace('</w:numbering>', nums + '</w:numbering>'), len(nuevos)


def parchear(docx):
    with zipfile.ZipFile(docx) as z:
        partes = {i.filename: z.read(i.filename) for i in z.infolist()}
        infos = z.infolist()
    doc = partes['word/document.xml'].decode('utf-8')
    numbering = partes.get('word/numbering.xml', b'').decode('utf-8')
    antes = (doc, numbering)
    doc = doc.replace(LETTER, A4)
    n_saltos = doc.count(SALTO)
    doc = doc.replace(SALTO, SALTO_OK)
    doc, numbering, n_listas = reiniciar_listas(doc, partes['word/styles.xml'].decode('utf-8'), numbering)
    if (doc, numbering) == antes:
        return 'sin cambios'
    partes['word/document.xml'] = doc.encode('utf-8')
    if numbering:
        partes['word/numbering.xml'] = numbering.encode('utf-8')
    tmp = docx + '.tmp'
    with zipfile.ZipFile(tmp, 'w') as zout:
        for i in infos:
            zout.writestr(i, partes[i.filename])
    with zipfile.ZipFile(tmp) as z:
        assert z.testzip() is None
    os.replace(tmp, docx)
    return 'A4 · %d saltos → pageBreakBefore · %d listas reiniciadas' % (n_saltos, n_listas)


def main():
    import fitz
    import docx as pydocx
    out = tempfile.mkdtemp(prefix='pdfguias-')
    fallos = 0
    for g in GUIAS:
        d = 'astro-site/public/dl/guia-%s' % g
        docx, pdf = '%s/guia-%s.docx' % (d, g), '%s/guia-%s.pdf' % (d, g)
        cambio = parchear(docx)
        pydocx.Document(docx)  # que abra
        r = subprocess.run(['soffice', '--headless', '--norestore', '--convert-to', 'pdf', '--outdir', out, docx],
                           capture_output=True, text=True, timeout=300)
        gen = os.path.join(out, 'guia-%s.pdf' % g)
        if not os.path.exists(gen):
            print('❌ %s: LibreOffice no generó el PDF: %s' % (g, r.stderr[-300:]))
            fallos += 1
            continue
        shutil.copyfile(gen, pdf)
        doc = fitz.open(pdf)
        a4 = all(abs(p.rect.width - 595) < 2 and abs(p.rect.height - 842) < 2 for p in doc)
        vacias = [i + 1 for i, p in enumerate(doc) if len(p.get_text().strip()) < 40]
        ok = a4 and not vacias and doc.page_count > 5
        fallos += not ok
        print('%s %s: %d páginas · A4 %s · vacías %s · %s' % ('✅' if ok else '❌', g, doc.page_count, a4, vacias, cambio))
    shutil.rmtree(out)
    sys.exit(1 if fallos else 0)


if __name__ == '__main__':
    main()
