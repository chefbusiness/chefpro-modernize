#!/usr/bin/env python3
"""
Gate del botón flotante de WhatsApp (2026-09-03).

Desde esta fecha lo pinta `BaseLayout.astro` para TODO el sitio (orden de John:
tiene que estar en todas las páginas). Antes lo montaba cada página a mano y sólo
llegaba a 655 de 1.312: faltaba en el blog entero, /precios, /contacto, el hub de
librerías, los legales y los 44 gates de acceso.

Qué verifica sobre el `dist/` (hace falta build reciente):

  1. TODA página HTML tiene EXACTAMENTE UN botón flotante de WhatsApp
     (un `<a href="https://wa.me/34744717942…">` cuya class lleve `fixed bottom`).
     Dos superpuestos es el fallo típico al añadir uno nuevo sin quitar el viejo:
     no rompe el build, no sale en ningún diff y en pantalla es un botón encima
     de otro con doble animación.

  2. EXCEPCIÓN, las 44 páginas `*-library.astro`: el dashboard post-pago monta su
     PROPIO WhatsAppProductSupport en React dentro de un island `client:only`, así
     que su HTML estático lleva CERO a propósito y pasan `whatsapp={false}`.
     El gate exige que sean exactamente esas y que ninguna otra se quede sin botón.

  3. El `aria-label` del botón global está traducido (nada de castellano suelto en
     las ramas /en, /fr, /de, /it, /pt, /nl).

Uso: python3 scripts/astro-migration/whatsapp-gate.py [DIST]
     DIST default: astro-site/dist
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DIST = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'astro-site' / 'dist'

TELEFONO = '34744717942'
# El <a> flotante: href a wa.me + class con `fixed bottom`. Descarta el enlace de
# WhatsApp del footer y los de dentro del cuerpo de los posts, que no son flotantes.
FLOTANTE = re.compile(
    r'<a[^>]*href="https://wa\.me/' + TELEFONO + r'[^"]*"[^>]*class="[^"]*fixed bottom[^"]*"',
    re.S,
)
ARIA = re.compile(
    r'<a[^>]*href="https://wa\.me/' + TELEFONO + r'[^"]*"[^>]*aria-label="([^"]*)"',
    re.S,
)
# aria-label esperado por idioma (whatsapp.tooltip de src/i18n/locales/*.json).
TOOLTIP_ES = 'Contacta con nosotros en WhatsApp'
TOOLTIP = {
    'en': 'Contact us on WhatsApp',
    'fr': 'Contactez-nous sur WhatsApp',
    'de': 'Kontaktieren Sie uns auf WhatsApp',
    'it': 'Contattaci su WhatsApp',
    'pt': 'Contacte-nos no WhatsApp',
    'nl': 'Neem contact met ons op via WhatsApp',
}


def idioma(rel: str) -> str:
    """Prefijo de idioma de la URL ('es' para la rama sin prefijo).

    Ojo: con `build.format: 'file'` la portada de cada idioma es `fr.html`, no
    `fr/index.html` — sin quitarle la extensión, las 6 homes traducidas se leían
    como españolas y su aria-label no se comprobaba (falso verde detectado
    probando el gate contra un defecto inyectado a mano).
    """
    primero = rel.split('/')[0]
    if primero.endswith('.html'):
        primero = primero[:-len('.html')]
    return primero if primero in TOOLTIP else 'es'


def main() -> int:
    if not DIST.is_dir():
        print(f'❌ no existe {DIST} — hace falta `cd astro-site && npm run build`')
        return 1

    fallos: list[str] = []
    sin_boton: list[str] = []
    con_dos: list[tuple[str, int]] = []
    total = 0

    for p in sorted(DIST.rglob('*.html')):
        total += 1
        rel = p.relative_to(DIST).as_posix()
        html = p.read_text(encoding='utf-8', errors='replace')
        n = len(FLOTANTE.findall(html))
        if n == 0:
            sin_boton.append(rel)
        elif n > 1:
            con_dos.append((rel, n))
        else:
            m = ARIA.search(html)
            esperado = TOOLTIP.get(idioma(rel))
            # Las landings de producto usan su propio texto ("Soporte por WhatsApp"):
            # sólo se comprueba el botón GLOBAL, que es el que sale del i18n.
            if esperado and m and m.group(1) == TOOLTIP_ES:
                fallos.append(f'{rel}: aria-label en castellano en la rama /{idioma(rel)}')

    # Las únicas páginas que pueden no traerlo en el HTML son los 44 dashboards.
    esperadas_sin = {p.name.replace('.astro', '.html')
                     for p in (ROOT / 'astro-site' / 'src' / 'pages').glob('*-library.astro')}
    inesperadas = [s for s in sin_boton if s not in esperadas_sin]
    faltan = sorted(esperadas_sin - set(sin_boton))

    print(f'-- {total} páginas HTML en {DIST}')
    print(f'-- con botón flotante: {total - len(sin_boton)}')
    print(f'-- sin botón en el HTML: {len(sin_boton)} '
          f'(esperadas {len(esperadas_sin)} = dashboards -library, lo montan en React)')

    for rel, n in con_dos:
        fallos.append(f'{rel}: {n} botones flotantes superpuestos')
    for rel in inesperadas:
        fallos.append(f'{rel}: SIN botón flotante (¿le falta el BaseLayout o sobra whatsapp={{false}}?)')
    for rel in faltan:
        fallos.append(f'{rel}: es un dashboard -library y trae botón en el HTML '
                      f'(¿se le ha caído el whatsapp={{false}}? saldrían dos al hidratar)')

    if fallos:
        print()
        for f in fallos:
            print(f'  ❌ {f}')
        print(f'\n❌ GATE WHATSAPP: {len(fallos)} fallos')
        return 1
    print('\n✅ GATE WHATSAPP VERDE: 1 botón flotante por página, sin duplicados')
    return 0


if __name__ == '__main__':
    sys.exit(main())
