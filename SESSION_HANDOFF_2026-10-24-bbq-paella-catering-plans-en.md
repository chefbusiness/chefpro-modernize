# Handoff — 24-oct-2026 (sesión Claude Code, Mac + VPS) — BBQ Catering + Paella Catering Business Plan Kit (EN, $39)

## ▶️ Para retomar

- **Estado:** los dos productos LISTOS a falta del Payment Link. Cierran el **lote EN de 5** que John pidió el 24-oct antes de salir
  («cuando tengas cinco productos terminados… hacemos la configuración en Stripe»): #156 Ice Cream Shop Checklists · #157 Chocolate +
  Pastry Shop Checklists · **#158 BBQ Catering Business Plan** · **#159 Paella Catering Business Plan**. PR **apilados** (cada rama sale
  de la anterior, todos contra main para que Netlify haga preview): se fusionan en orden 156 → 157 → 158 → 159, o el #159 con merge
  commit, que incluye los cuatro de abajo.
- Lista para John con nombre, precio, redirección y descripción de Stripe de los 5: `PAYMENT_LINKS_PENDIENTES_JOHN.md` (raíz, en main).
- Worktrees del Mac (scratchpad de la sesión `7b1225aa…`): `wt-bbq`, `wt-paella` (+ `-f3`); VPS: `/root/wt-bbq`, `/root/wt-paella`.
  Limpiarlos tras fusionar.
- Detalle técnico: `scripts/productos-digitales/business-plans-en-6/` (BBQ) y `business-plans-en-7/` (Paella): `F1-research-us-delta.md`,
  `F1-inventario-delta.md`, `SPEC-delta.md` (D96-D113 y D114-D132), `F2-NOTAS.md` (§8 cierre con sha256), `F3-NOTAS.md`, `REVISION-FINAL.md`.

## 1. Cierre (con los links)

Para cada producto del lote: CLI de Stripe `--live` (USD, one_time, exclusive, redirección a su `/access`) → `netlify api createEnvVars`
(scope builds, context all) → `sync-payment-links.py` → sacar de draft y fusionar en orden (**el modo automático bloquea `gh pr merge`:
Shift+Tab**) → LIVE: `gate-flujo-postpago --only <slug>` ×5, `tienda-gate --base https://aichef.pro`, `robots-gate --live`, gate completo
en el VPS, sitemap en GSC. Envs del lote: `VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_CHECKLISTS_KIT`, `…_CHOCOLATE_SHOP_CHECKLISTS_KIT`,
`…_PASTRY_SHOP_CHECKLISTS_KIT`, `…_BBQ_CATERING_BUSINESS_PLAN`, `…_PAELLA_CATERING_BUSINESS_PLAN`.

**Correos EN** (plantillas ya escritas en `scripts/productos-digitales/emails/broadcast-<slug>-lanzamiento-en.*`, cola de 5 días a las
14:00Z; Resend no programa a > 30 días → borrador + routine 30 días antes; confirmar huecos con `GET /broadcasts` antes):
24-ene Ice Cream · 29-ene Chocolate · 3-feb Pastry · 8-feb BBQ · 13-feb Paella. (Las notas de las SPEC del BBQ y la paella proponen
29-ene y 3-feb porque no sabían del lote: manda esta lista.)

## 2. Hecho

| | BBQ Catering | Paella Catering |
|---|---|---|
| Gemelo ES | `plan-negocio-parrillero-asador-eventos` 2.2 | `plan-negocio-paellero-eventos` 2.2 |
| Concepto US | off-site BBQ caterer: ahúma en commissary, smoker trailer al evento en bodas/premium, drop-off, live-fire premium | paella cocinada en vivo en el evento, prep en commissary, drop-off menor, premium de marisco, tapas |
| Caso | 150 × 75 × $38 = $427,500 · CAPEX $83,300 · préstamo $101,000 · DSCR 2.43× · equilibrio 128 · pesimista sin caja | 135 × 58 × $40 = $313,200 · CAPEX $49,480 · préstamo $64,000 · DSCR 2.47× · equilibrio 116 · pesimista sin caja |
| Calculadora extra | Meat Yield & Smoke Schedule · Shopping List by Guest Count · live pit $650 | Paella Yield & Pan Sizing · Shopping List by Guest Count · Tapas hour? |
| Código | conjunto `bbq` (diccionario catering EN, código del mobile bar) | conjunto `pael` clonado del `bbq` (propuestas = EN del BBQ, 16 sha256 fijados, `bp7.py verificar`) |
| Gates | G1-G9 verde · autotest 20/20 · docx 8/8 · calc 581 · barrido 0 · regresión 5 planes | G1-G9 verde · 20/20 · 8/8 · calc 509 · barrido 0 · regresión 7 planes |
| Revisión final | 0 B · 6 M · 18 m → ronda, todo aplicado | 0 B · 3 M · 19 m → ronda |
| Imágenes | 3 generadas (smoker trailer en boda, carving station, drop-off) + og | 3 generadas (paella en boda, paella party con tapas, van) + og |
| Tokens | ≈ 2,8 M | ≈ 2,4 M |

## 3. Para la sesión del blog (Cursor)

Posts EN candidatos para banners: ver `business-plans-en-6/F3-NOTAS.md` §5 y `business-plans-en-7/F3-NOTAS.md` §5.

## 4. Deuda anotada

- ES paellero: «Paella valenciana DO» / «Paella vegetal DO» en carta, manual, calculadora y landing (la DO ampara el arroz, no el plato).
- ES parrillero: merma del brisket 35-40 % y 40-50 %; «18 cortes» / «12 cortes» incluyen queso y embutidos.
- `check_textos` (común a los planes EN) rechaza tildes y eñes: «quinceaneras», «fideua»; aceptable, pero un día convendría una lista blanca.
