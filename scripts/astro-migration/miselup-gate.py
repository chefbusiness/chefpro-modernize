#!/usr/bin/env python3
"""miselup-gate.py — la tarjeta lateral de Miselup está EXACTAMENTE UNA VEZ en la landing pública y
en el dashboard privado de cada producto digital, y en NINGUNA otra página (John, 19-sep-2026).

Lee el registro astro-site/src/lib/zona-app.ts (landingPath + libraryPath de los 48 productos), pide
cada página al sitio (--base; default producción) y exige:
  · landing y library: 1 `id="miselup-card"`, 1 bloque <style> con `#miselup-card`, 1 <script> con
    `miselupCardDismissed`, y el CTA a app.miselup.pro con sus UTM.
  · muestra de páginas AJENAS (home, hub, blog, precios, un -access, EN, términos): CERO rastros.
NO construye nada en local (regla térmica): mide lo servido.

Uso:
  python3 scripts/astro-migration/miselup-gate.py                       # producción
  python3 scripts/astro-migration/miselup-gate.py --base https://deploy-preview-N--aichefpro.netlify.app
Exit 1 si hay fallos.
"""
import argparse, concurrent.futures as cf, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ZONA = os.path.join(ROOT, 'astro-site/src/lib/zona-app.ts')
AJENAS = ['/', '/productos-digitales', '/blog', '/precios', '/kit-escandallos-access', '/en/', '/terminos',
          '/integraciones', '/pago-cripto', '/manual-chef-ejecutivo-access', '/libreria-de-prompts',
          '/en/prompt-libraries',
          # post con el bloque congelado «CHEFBUSINESS GROUP», que enlaza a miselup.pro: la palabra
          # «miselup» NO es rastro de la tarjeta; por eso el gate mide la firma del componente.
          '/blog/libreria-de-prompts-para-fermentus-ai']
CTA = 'https://app.miselup.pro/signup?utm_source=aichef&utm_medium=sidecard&utm_campaign=miselup-recetario&utm_content='


def registro():
    s = open(ZONA, encoding='utf-8').read()
    out = []
    for m in re.finditer(r"productId:\s*'([^']+)'(.*?)\}", s, re.S):
        pid, cuerpo = m.group(1), m.group(2)
        lp = re.search(r"landingPath:\s*'([^']+)'", cuerpo)
        lb = re.search(r"libraryPath:\s*'([^']+)'", cuerpo)
        if lp and lb:
            out.append((pid, lp.group(1), lb.group(1)))
    return out


def http(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'miselup-gate/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode('utf-8', 'ignore')
    except urllib.error.HTTPError as e:
        return e.code, ''
    except Exception as e:  # noqa
        return 0, str(e)


def medir(html, placement=''):
    return {
        'card': len(re.findall(r'id="miselup-card"', html)),
        'style': len(re.findall(r'<style[^>]*>[^<]*#miselup-card', html)),
        # bloques <script> que contienen el JS del snippet (la cadena aparece 2 veces dentro: leer y escribir)
        'script': len(re.findall(r'<script[^>]*>(?:(?!</script>).)*?miselupCardDismissed', html, re.S)),
        'cta': html.count(CTA + placement) if placement else html.count(CTA),
        # firma del COMPONENTE, no de la marca (25 posts del blog llevan «miselup» en un enlace)
        'rastro': html.count('id="miselup-card"') + html.count('miselupCardDismissed') + html.count(CTA),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default=os.environ.get('AICP_BASE_URL', 'https://aichef.pro'))
    args = ap.parse_args()
    base = args.base.rstrip('/')
    reg = registro()
    if len(reg) < 40:
        print(f'✗ el registro zona-app.ts devuelve {len(reg)} productos: el parser ha perdido entradas')
        sys.exit(1)
    objetivos = [(pid, 'landing', lp) for pid, lp, _ in reg] + [(pid, 'library', lb) for pid, _, lb in reg]
    fallos = []
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        res = list(ex.map(lambda t: (t, http(base + t[2])), objetivos))
        aj = list(ex.map(lambda p: (p, http(base + p)), AJENAS))
    ok = 0
    for (pid, tipo, path), (st, html) in res:
        if st != 200:
            fallos.append(f'{pid} {tipo} {path} → HTTP {st}'); continue
        m = medir(html, 'landing' if tipo == 'landing' else 'dashboard')
        if m['card'] == 1 and m['style'] == 1 and m['script'] == 1 and m['cta'] == 1:
            ok += 1
        else:
            fallos.append(f'{pid} {tipo} {path}: card={m["card"]} style={m["style"]} script={m["script"]} cta={m["cta"]} (esperado 1/1/1/1; el CTA debe llevar utm_content={tipo if tipo == "landing" else "dashboard"})')
    for path, (st, html) in aj:
        if st != 200:
            print(f'  ⚠ ajena {path} → HTTP {st} (sin comprobar)'); continue
        if medir(html)['rastro']:
            fallos.append(f'ajena {path}: {medir(html)["rastro"]} rastros de la tarjeta Miselup y no debería haber ninguno')
    print(f'Miselup side-card en {base}: {ok}/{len(objetivos)} páginas de producto correctas '
          f'({len(reg)} productos × landing + library) · {len(AJENAS)} páginas ajenas comprobadas')
    for f in fallos:
        print('  ✗', f)
    sys.exit(1 if fallos else 0)


if __name__ == '__main__':
    main()
