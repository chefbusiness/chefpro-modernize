# Bakery Checklists Kit Pro — F2: traducción y montaje (31-oct-2026 · sesión Claude Code)

Todo el python con xlsx en el VPS (`/root/wt-kits`, venv `/root/venv-guias`). Textos: `textos_en/heredado.json` (7) +
`textos_en/G1.json` (217, traducidas en esta sesión, `724a88b8`) + GM 201 por `mapas_bakery.py`. Mes de los
docProps: **October**. Precio **$15**. Slug en `PRODUCTOS_LETTER` (`censo-entregables.py`) y `EXCLUIDOS`
(`postprocess-transversal.py`). **Código común: sin tocar** (los ganchos del molde plano del food truck, `f35b7355`,
sirven tal cual; sin regresión que repetir).

## Comandos (en `scripts/productos-digitales/checklists-kit/`)

    python3 extraer_textos.py --kit bakery && python3 bakery/mapas_bakery.py && python3 heredar.py --kit bakery
    python3 aplicar_en.py --kit bakery --dry-run --salida /tmp/pan-en --idempotencia --mes October
    python3 gates_en.py --kit bakery --dir /tmp/pan-en --mes October [--autotest]
    cp /tmp/pan-en/*.xlsx ../../../astro-site/public/dl/bakery-checklist-templates/ && python3 gates_en.py --kit bakery --mes October
    python3 ../censo-entregables.py --only bakery-checklist-templates --fail
    python3 ../gate-no-latinos.py --only bakery-checklist-templates
    python3 ../parche_xml_xlsx.py --check ../../../astro-site/public/dl/bakery-checklist-templates/*.xlsx

## Resultados

| Paso | Resultado |
|---|---|
| Montaje | 11 xlsx (SPEC §2), 80.446 bytes; idempotencia 0 diferencias; 0 fórmulas; 0 desbordes; 25 horas a reloj de 12 h |
| Gates | **VERDE 8/0** (dry-run y publicado): G1 11 hojas · 7 DV (122 celdas) · 7 CF · 64 merges · 11 paneles · 11 títulos de impresión · 160 tareas; G2 900 piezas contra términos prohibidos; G3 54 altos de fila, 11 títulos interiores; G4 456 glosario · 72 regeneradas · 227 traducidas · 25 horas; **G5 y G6 N/A**; G7 33 °F y 10 citas, todas permitidas, 14 celdas ES con °C |
| Autotest | **16/16 CAZADOS** (las 14 del food truck + las dos de horas, porque el 01 trae horas) |
| censo-entregables · no-latinos · LIT255 | 0 defectos (`--fail`) · 11 ficheros, 0 no latinos · VERDE |
| Publicado | `astro-site/public/dl/bakery-checklist-templates/` (`eaad4777`); volcados `revision/dump_en.txt` y `dump_es.txt` (861 líneas cada uno) |

Arreglo de la F2: G7 leía «5 °F» en la fuente de la regla de proceso («redondeados a 5 °F») como cifra permitida; la fuente
se reescribe sin la cifra. Ninguna traducción tocada tras el primer montaje.

## Lo que la F3 tiene que saber (landing, dashboard, email)

- **No prometer** (molde plano o la ES lo promete y no está): contador de tareas, N/A que no cuenta, hoja de
  instrucciones, protección (van **sin proteger**), horno de convección, protocolos para recuperar masas, gestión de colas,
  reporting / KPIs, calibración de termómetros, hoja de caja, firma o bio dentro del fichero, «marketing» en el calendario
  (su columna E es **Training**), San Juan ni fiestas españolas.
- Sí: **135 tareas** en 8 checklists con **horas del turno de madrugada** (3:00 AM-2:30 PM) en el 01 + plantilla en blanco +
  hoja de producción diaria (13 campos) + calendario de 12 meses (panes de temporada, pedidos US, mantenimiento,
  formación); tabla de horneado en °F por tipo de pan; masa madre (refresco 1:1:1, pH 3.8–4.2, float test, backup),
  poolish y biga; desplegable ✓ / — / N/A con fila en verde en 7 hojas (01-04, 06-08; el 05 y el 09 no lo llevan);
  etiquetas y alérgenos FDA (3-602.11 / 3-602.12(C), trigo y sésamo), gluten-free y organic con sus normas; US Letter.
- Pan, no pastelería: title «Bakery Checklists Kit Pro: Bread Bakery Opening, Production & Closing Checklist Templates for
  Excel»; enlazar al Bakery Business Plan Kit y, como hermano, al Pastry Shop Checklists Kit Pro (tartas y pastelería).
- `$15`, env `VITE_STRIPE_PAYMENT_LINK_BAKERY_CHECKLISTS_KIT`, JWT `bakery-checklist-templates-jwt`; UK solo en la FAQ;
  Google Sheets solo si el test lo confirma; cottage food: la FAQ puede decir que este kit es para una panadería con
  permiso (food establishment), no para la venta casera.

Erratas del ES: `SPEC.md` §5.

## Ronda de revisión de contenido (31-oct · sesión Claude Code; 0 bloqueantes)

Aplicado (`68694d7d` textos y mapas, `e6778f5c` remontaje y republicación): 01 B5 «Turn on the ovens and the proofer: deck /
rack oven»; 07 B6 «(carbon, grease)». **Orden por horas del 01**: en la apertura, el control de la sala del obrador (ES B10,
03:00) quedaba tras las 03:30; mover la fila arrastraría la nota F7 («Calibrated scale»), así que **se ajusta la hora a 3:30
AM** (la del amasado y el agua) sin mover filas. En el cierre, las tareas de las 2:00 PM antes que las de las 2:30 PM
(`_MOVIDAS_01`: filas 29-32 con su zona, responsable y hora; sin notas en F). Resultado: **VERDE 8/0** (G5 y G6 N/A),
autotest 16/16, idempotencia 0, censo-entregables / no-latinos / LIT255 en 0; 213 pendientes (4 cadenas movidas a GM).
