# Handoff — 16/17-oct-2026 (sesión Claude Code) — How to Open a Pastry Shop (EN, $69), producto 15 de la tienda EN

## 0. Estado: LISTO a falta del Payment Link · PR #132 (draft) · rama `feat/bakery-guide-en`
- **Tarea de John**: Payment Link en **USD $69** (¡moneda USD, no EUR!), nombre «How to Open a Pastry Shop», redirección tras
  pago `https://aichef.pro/en/digital-products/how-to-open-a-pastry-shop/access?session_id={CHECKOUT_SESSION_ID}`,
  impuesto automático como los demás EN.
- Al recibirlo: CLI de Stripe, env `VITE_STRIPE_PAYMENT_LINK_HOW_TO_OPEN_A_PASTRY_SHOP` (builds), `sync-payment-links.py`,
  PR fuera de draft, merge, gates LIVE (`gate-flujo-postpago --only how-to-open-a-pastry-shop`, completo, `tienda-gate`,
  `robots-gate`), sitemap en GSC, correo EN 4-dic 14:00Z (borrador + routine).

## 1. Qué hay
| Pieza | Estado |
|---|---|
| Guía EN | 20 caps. + anexo normativo US (79 fuentes) · PDF 113 págs. + DOCX · 61.188 palabras |
| Bonus | «12 Opening Decisions, Solved» · PDF 39 págs. + DOCX |
| Plan | «Sample Business Plan for a Pastry Shop» · DOCX (9.003 palabras) |
| 8 xlsx EN | `aplicar_en.py` (XML directo) + `inject_cache.py` + `cache_manual.py`; gate de invariantes 6/8 OK + 3 diferencias aceptadas (`xlsx/GATE-XLSX.md`) |
| Landing/app | ficha EN, landing/access/library, dashboard, registro 5 fuentes + admin, $69, familia en tienda.ts, hub vivo, enlaces cruzados, llms.txt, 4 banners blog EN |
| Correo | `emails/broadcast-how-to-open-a-pastry-shop-lanzamiento-en.html` (sin programar) |

## 2. Decisiones clave (SPEC D1-D20)
- Caso «La Clara» 1:1 en Texas; pagas 15 → 12 (×15/12, anual igual); 33 % = payroll taxes, workers' comp and benefits;
  mínimo $15,080; impuestos a 0 % (precio pre-tax); sq ft/°F/CFM; gramos y $/kg en recetas; picos US-Texas (Mother's Day en mayo).
- Los 15 traspasos reales de España → plantilla de anuncios de tu zona (filas vaciadas, op `vaciar` nueva en aplicar_en).

## 3. Pendientes (no bloquean)
- **Erratas de la guía ES** (≈ 15, en `guia-pasteleria-en/ERRATAS-ES.md`), la más seria: el «colchón del 22,9 %» sobre el
  equilibrio se lee como caída de ventas admisible (es 18,6 %). Parche puntual del ES: proponer a John.
- Florida: mínimo $15.00 desde el 30-sep-2026 sin confirmar en FloridaCommerce (el texto dice $14.00 + «check»).
- Siguiente EN por demanda: «How to Open a Restaurant» (1.760/mes) tras subir la guía Casual ES a v2.

## 4. Lecciones
- Un «how to open» es 90 % readaptación legal/laboral/fiscal: research US en una pasada + tandas opus + mapa de cifras
  recalculadas (`xlsx/diff_valores.py`) antes de traducir lo que depende de la caja.
- Las decisiones compartidas (`DECISIONES-TANDAS.md`) con §9 por tanda evitaron incoherencias entre 17 agentes; aun así hubo que
  unificar a mano áreas, columnas y unidades (batidora 20 L).
- BizBuySell bloquea fetch (403): sin datos US de traspasos, plantilla vacía antes que datos de otro país.

Consumo ≈ 8,7 M tokens de subagentes (L, techo 10 M). CPU del Mac 45-63 °C (vigilante activo, tope 2 agentes; xlsx, render y
gates en el VPS).
