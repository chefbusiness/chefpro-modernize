# Handoff — 24-oct-2026 (sesión Claude Code, Mac + VPS) — Chocolate Shop + Pastry Shop Checklists Kit Pro (EN, $19)

## ▶️ Para retomar

- **Estado:** los dos productos LISTOS a falta del Payment Link. PR **#157** (draft), rama `feat/chocolate-pastry-checklists-en`,
  **apilada sobre #156** (Ice Cream Shop Checklists). Worktree del Mac `scratchpad/wt-chocopastry`; VPS `/root/wt-chocopastry`.
  Preview: https://deploy-preview-157--aichefpro.netlify.app/en/digital-products/pastry-shop-checklist-templates
- Lote EN de 5 (John, 24-oct): los Payment Links se crean juntos al volver John. Lista con nombre, precio, redirección y
  descripción de Stripe: `PAYMENT_LINKS_PENDIENTES_JOHN.md` (raíz, en main).
- Detalle técnico: `scripts/productos-digitales/checklists-kit/{chocolate,pastry}/{SPEC,F2-NOTAS,F3-NOTAS}.md` y `revision/REVISION-F2.md`.

## 1. Cierre (con los links)

El mismo que el #156 (§2 de su handoff), para las env `VITE_STRIPE_PAYMENT_LINK_CHOCOLATE_SHOP_CHECKLISTS_KIT` y
`VITE_STRIPE_PAYMENT_LINK_PASTRY_SHOP_CHECKLISTS_KIT`: CLI de Stripe (USD 1900, exclusive, redirección) → `netlify api createEnvVars`
(builds, all) → `sync-payment-links.py` → fusionar en orden #156 → #157 (o #157 con merge commit, que incluye #156) → LIVE:
`gate-flujo-postpago --only <slug>` ×3, `tienda-gate --base https://aichef.pro`, `robots-gate --live`, gate completo en el VPS, sitemap
en GSC. **Correos EN** (ya escritos en `scripts/productos-digitales/emails/broadcast-{chocolate,pastry}-shop-checklists-lanzamiento-en.*`):
huecos de la cola EN tras el icecream (24-ene) → **29-ene** chocolate y **3-feb** pastry, 14:00Z (borrador + routine 30 días antes).

## 2. Hecho

| | Chocolate Shop | Pastry Shop |
|---|---|---|
| Ficheros | 11 xlsx (9 + 2 bonus) + guía de equivalencias | 15 xlsx (9 + 4 libros propios + 2 bonus) + guía |
| Tareas | 338 en 37 hojas | 413 + 17 eventos, 62 hojas |
| Gates EN | VERDE 8/0 · autotest 19/19 · 0 cortadas nuevas | VERDE 8/0 · autotest 20/20 · 0 cortadas nuevas |
| Revisión adversarial | 1 B · 3 M · 21 m → una ronda, aplicados | 1 B · 8 M · 22 m → una ronda, 20/22 menores |
| Parche ES LIVE (sin cambio de versión) | 🔴 7 celdas de seguridad: ganache de nata fresca en frío y con fecha de caducidad, etiqueta con ingredientes/alérgenos, síntomas = no entra en obrador | maquetación del 09 (áreas de impresión, anchos) + 02 C8 merengue suizo |
| Tokens (subagentes) | ≈ 1,2 M | ≈ 1,75 M |

F3 conjunta (≈ 0,65 M): fichas, landing/access/library, hreflang gemelo ES, registro, hub EN (Pastry 1 · Chocolate 2 · Ice Cream 3),
pies cruzados con la guía How to Open a Pastry Shop, `llms*.txt` (25 productos), sitemap, correos. Preview: `gate-flujo-postpago --base`
12/12 y 16/16 entregables 200 (fallos solo de Payment Link), `tienda-gate --es-identico` 46/49 + 3 esperadas, verde.

Código común del circuito (pastry): `aplicar_en.objetivo_ajuste` mide texto girado, `_bloquear_verde` invertido para kits sin
protección, `G6_ESPERADO` para valores fijados; los 9 hermanos salen idénticos (los 4 rojos previos de `adf52a52` siguen igual).
`postprocess-transversal.py`: los dos slugs en `EXCLUIDOS`.

## 3. Para la sesión del blog (Cursor)

- Chocolate: `prompt-library-creative-chocolate`, `prompt-library-chocolate-consulting` (y `prompt-library-creative-pastry`).
- Pastry: `prompt-library-pastry-consulting`, `prompt-library-creative-pastry`, `prompt-library-creative-bakery`; en
  `prompt-library-bakery-consulting` cambiar uno de sus dos banners del Coffee Shop Checklists por el Pastry Shop.

## 4. Pendiente menor

- Pastry m21 («day-old» en el desplegable del 10) no aplicado: la DV del ES está cerca del límite de 255 caracteres.
- Fotos `tareas-pasteleria-masas` y `-decoracion` (ES y EN) muestran reloj y alianza cuando el kit pide trabajar sin joyas (opcional).
