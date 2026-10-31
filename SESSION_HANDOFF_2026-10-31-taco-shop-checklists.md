# Handoff 31-oct-2026 · sesión Claude Code (Mac + VPS) — Taco Shop Checklists Kit Pro LIVE + caché de 4 kits ES

Continúa `SESSION_HANDOFF_2026-10-30-tanda-arreglos.md` (tanda de arreglos, #186).

## 1. Qué salió

- **Taco Shop Checklists Kit Pro** (EN, $19) — https://aichef.pro/en/digital-products/taco-shop-checklist-templates · PR **#188 →
  `8c753f0d`**. Edición EN del Kit de Tareas Taquería: 11 xlsx, 36 hojas, 298 tareas, sin libro de caja (FAQ que remite al Restaurant
  Checklists Kit Pro). Docs: `scripts/productos-digitales/checklists-kit/taco/` (SPEC, F2-NOTAS, F3-NOTAS, `revision/dump_*.txt`).
  - F1: vertical `taco` en `kit.py`, `mapas_taco.py`, memoria de traducción (32 heredadas del base, 458 nuevas).
  - F2: un traductor sonnet; `aplicar_en` en el VPS; gates 8/8, autotest 16/16, censo 0, no latinos 0, LIT255 verde. Código común:
    ganchos de `gates_en.py` (kit sin caja, `FRASES_OK_EXTRA` para «al pastor», G1 con literales fundidos), regresión idéntica en los
    10 kits EN publicados + base.
  - F3: landing duplicada (hotel/pizza), hub EN en la posición 1, enlaces con el Taco Shop Business Plan Kit y 16 pies EN, `llms.txt`
    (34), correo EN. Avatar nuevo `avatars-nicho/avatar-tortillera.jpg` (generate-images).
  - Revisión final (sonnet, 3 lentes): 0 B · 2 M corregidos (horario del trompo alineado en 01/02/06: cono 9:30, montaje 9:45, primera
    sonda 10:20 AM; hoja de alérgenos con los 9 de EE. UU.) + 8 menores. Queda el orden Grito / chiles en nogada del calendario 08
    (mover filas fijas; cosmético).
- **Kits de Tareas ES — caché del 05** (PR **#187 → `666c117e`**): los 33 contadores del libro 05 de cafetería, dark kitchen,
  hamburguesería y pizzería estaban sin valor (el arreglo `adf52a52` se guardó sin `inject_cache`; móvil y Vista Rápida los enseñaban
  vacíos). `inject_cache.py`: 0 celdas cambiadas. Censo de `dl/`: ningún otro contador o suma sin caché.

## 2. Verificación LIVE

Postpago 0 fallos y 0 avisos (92 productos, 1.146 entregables) · robots verde · landing 200 con el link en las 4 posiciones · sitemap +
`llms.txt` con la URL y sitemap reenviado a GSC · checkout cripto 200 (`qa-tacochecklists@aichef.pro`) · tienda-gate verde contra el
preview (53/54 ES idénticas + la Taquería esperada por el hreflang). Link de Stripe `plink_1UWQA54CcdRGidmEOVg6j434`: activo, 19 USD
one-time, redirección a `/access?session_id={CHECKOUT_SESSION_ID}` (CLI con `--live`; sin `--live` la CLI lista el modo test vacío).

## 3. Correo

EN **25-mar-2027 14:00Z** — borrador Resend `879dace8-0772-4952-a0f4-2ee8aa1e4124` («Launch Taco Shop Checklists Kit Pro (EN)», segmento
AI Chef Pro EN, from `hello@news.aichef.pro`), routine `trig_016VjznzFMEiBM2vXBAkDsAw` (24-feb-2027 15:07Z). Prueba a John enviada.
**Siguiente hueco: ES 28-dic · EN 30-mar-2027.**

## 4. Pendientes y deuda

- **John**: purgar pedidos cripto QA sin pagar — `qa-heladeria`, `qa-finca`, `qa-pizzeria`, `qa-pizzashop`, `qa-taqueria`, `qa-tacoshop`,
  `qa-polleria`, `qa-rotisserie`, `qa-tacochecklists` (+ los del 27/28-oct: `qa-hotel-en`, `qa-icecream-en`, `qa-wedding-en`, `qa-ctrl`,
  `qa-cafemovil`, `qa-coffeecart`). Comando en el handoff del 30-oct §4.
- **Gates EN de pizza, burger, cafe y ghost en rojo ANTES de esta sesión** (deriva, no defecto del EN LIVE): G4 porque los mínimos del
  inventario ES pasaron a número (`adf52a52`) y G6 por las cachés vacías del ES (esta última arreglada en #187). Rehacer su G4 cuando se
  actualicen esos kits.
- Erratas ES de la Taquería para su próxima v2.x: `taco/SPEC.md` §5.
- Catálogo JSON EN de los banners del blog: le faltan el Taco Shop Business Plan Kit y el Rotisserie (carril Cursor).
- Blog EN (posts de comida mexicana / tacos → banners del kit): carril Cursor.

## 5. Siguiente

Cola: Plan Sushi Bar ES + EN → Hamburguesería Smash → Kit de Tareas Pollería («Próximos»). Alternativa: traducciones al inglés de los 22
productos ES sin gemelo EN (8 kits de tareas 12-18 €, mega-pack, 10 guías, 2 manuales, plan chef privado); los kits de tareas son los más
rápidos (este circuito: ~1,3 M tokens de subagentes y una sesión cada uno).
