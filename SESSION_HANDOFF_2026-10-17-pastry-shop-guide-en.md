# Handoff — 16/17-oct-2026 (sesión Claude Code) — How to Open a Pastry Shop (EN, $69), producto 15 de la tienda EN

## 0. Estado final: LIVE (17-oct, merge `882f6796` del PR #132) · Tienda EN: 15 productos
- Stripe `plink_1URUsY4CcdRGidmEk7sNDFEr` (`buy.stripe.com/4gMbIU0y0eAK9fh6Rf6oo1O`), producto `prod_VSPgxcvDbWWbSn`,
  **$69 USD** (6900, `tax_behavior` exclusive como la Food Cost Guide EN), impuesto automático, redirección a `/access`
  comprobada con la CLI (`--live`). Descripción Stripe (252 caracteres) en el producto. Env
  `VITE_STRIPE_PAYMENT_LINK_HOW_TO_OPEN_A_PASTRY_SHOP` (builds, all) + mapa de 66 links (`dabbf447`).
- Gates: `--only` contra el preview 0 fallos (aviso del webhook = el preview no tiene `STRIPE_WEBHOOK_SECRET`) · LIVE `--only`
  **0 fallos / 0 avisos** (webhook armado) · completo en el VPS **66 productos / 918 entregables / 0 / 0** · `tienda-gate` (15 vivos
  fuera de ES) · `robots-gate` (1.277 URLs públicas, ninguna bloqueada). Landing en `sitemap-0.xml`; sitemap reenviado en GSC.
- **Correo EN 4-dic 14:00Z**: borrador `1e8b7c2f-5430-4ecb-8566-8b53f960fd3e` («Lanzamiento How to Open a Pastry Shop (EN) — 4-dic»,
  asunto «Open your pastry shop with a plan, not a guess», prueba a John enviada) + routine `trig_01LqowZy9azA47FqMag3Ktwn`
  (4-nov 15:07Z) → **al retomar después del 4-nov, mirar su `list_runs`**. Siguiente hueco EN: **9-dic 14:00Z**.
- Sesión del 17-oct (Claude Code): la de la noche anterior SÍ terminó (resumen entregado a las 03:22); John apagó después.
  Worktrees `wt-bakery` (Mac y VPS) eliminados; `main` del VPS al día.

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
- (17-oct, lanzamiento) El paquete del Payment Link debe llevar los 5 campos: nombre, **descripción ≤ 260** (John tuvo que pedirla),
  precio con moneda, impuesto y redirección. El modo automático bloquea `gh pr merge` («Merge Without Review»): avisar a John
  del Shift+Tab al pedir el link. El aviso «stripe-webhook 501» del gate contra un preview es esperado (el preview no tiene
  `STRIPE_WEBHOOK_SECRET`); en LIVE responde 400 sin firma. El gate completo (918 descargas) se pasó en el VPS.

Consumo ≈ 8,7 M tokens de subagentes (L, techo 10 M). CPU del Mac 45-63 °C (vigilante activo, tope 2 agentes; xlsx, render y
gates en el VPS).
