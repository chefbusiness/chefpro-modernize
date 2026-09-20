# Handoff 2026-09-20 — Política de 3 fases + «Tareas Recurrentes: Taquería Mexicana» (sesión Claude Code)

Producción = `main`. Política nueva de John (decisiones delegadas a Claude): `CALENDARIO-V2-SEMANAL.md` §3 y `CLAUDE.md`.

## F1 Fundamentos — CERRADA (gate de script en verde)
- Research `kit-tareas-taqueria/01-research-taqueria-mexicana.md` (601 líneas) · SPEC `02-SPEC-kit-tareas-taqueria.md`
  (862 líneas; refutada en ronda única → 24 correcciones aplicadas → `gate_f1_spec.py` PASS) · contrato del molde v2.0
  `03-contrato-molde-v2.md` + volcados `molde-referencia*.json` (`extraer_molde.py`).
- Decisiones: 14 € / `priceOld '€69'`; BONUS-02 en molde calendario NO-CB; 300 tareas (270-330) en 22 hojas; molde
  canónico = kit base v2.0 (sushi-bar y 5 más siguen en v1.1 CB); Mega Pack fuera; env `VITE_STRIPE_PAYMENT_LINK_TAREAS_TAQUERIA`.
- Consumo F1: research 0,24 M · SPEC 0,21 M · refutación 0,28 M · fixer 0,28 M = **1,0 M** de los 2,5 M del producto.

## F2 Entregables — CERRADA (gates de script en verde)
- `scripts/generate-tareas-taqueria.py` (helpers del molde v2.0 + loader de `contenido/contenido_a.py` (01-04, 173 tareas) y
  `contenido_b.py` (05-08 + 09 + bonus, 125 tareas)) → `astro-site/public/dl/kit-tareas-taqueria/` (11 xlsx, caché inyectada).
- Verificado: generador == post-motor celda a celda (0 diferencias) · `main.py --dry-run --origen` TODO VERDE (11/11 en
  alcance, idempotencia 0) · `comparar_molde.py` 9/9 · `gate_f2_contenido.py` PASS (298 tareas, rango 270-330) ·
  `censo-entregables --only --fail` 0 · `gate-no-latinos` 0. **`postprocess-transversal` NO se corre** (v1.1: degradaría el kit).
- Trampas cazadas: `main.py` tiene el scratchpad de OTRA sesión hardcodeado (`CLAUDE_SCRATCHPAD=$SP` al invocarlo);
  `motor.cadencia` retitula la columna de tiempo por CONTENIDO (07 mensual solo `1º de mes/Quincenal/Mensual/Fin de mes`,
  08 con «antes/víspera/día siguiente/al confirmar»); las colas de «Se conecta con» de 07/08/bonus las escribe el motor
  (`COLA_MOTOR` en el generador, pegadas del dry-run); `texto_appcc` añade la coletilla del Pack a toda celda con APPCC.
- Consumo F2: helpers 0,31 M · redactores 0,24 + 0,22 M = **0,77 M**. Acumulado producto: **1,77 M** de 2,5 M.

## F3 Producto y lanzamiento — EN CURSO (rama `feat/kit-tareas-taqueria`; checklist en SPEC §6)
- Paso 1 (en marcha): 1 Sonnet calca la capa de producto del sushi-bar (ficha, landing, islands, gemelos SPA, App.tsx,
  catálogo, config, changelog, functions ×4, zona-app + `fase5-generate-zona-app.py`, `sync-product-prices.py`, hub ×2 en
  posición 1 sin tarjeta «Próximos», cesta del use-case `restaurante-mexicano`, cross-link desde la guía mexicana) y
  1 Sonnet genera las 7 imágenes con la skill `generate-images`.
- Paso 2: revisión de Fable de lo crítico (payment-links, product-prices, get-download-urls, zona-app, catálogo sin
  comentarios en `description`), gate de multiconjunto del hub (50 productos, 1.ª la taquería, 22 en «Próximos»),
  commit + push + PR → deploy preview de Netlify → `gate-flujo-postpago.py --base <preview> --crypto-products all
  --crypto-exclude pro-prompts-ebook` (el botón de compra caerá a `#comprar` hasta el Payment Link) · `miselup-gate.py
  --base` · curl de `noindex` en `-access`/`-library` y de su ausencia en la landing.
- Paso 3 (**John**): crear el producto en Stripe y su Payment Link → yo lo meto en `netlify/shared/payment-links.ts` y
  John da de alta `VITE_STRIPE_PAYMENT_LINK_TAREAS_TAQUERIA` en Netlify (scope **builds**) → merge → gates LIVE
  (`gate-flujo-postpago.py` sin flags: 50 productos / 722 entregables / 0) · `miselup-gate.py` · sitemap a GSC →
  broadcast de lanzamiento en la cola de Resend (slot = último programado + 5 días: tras el 24-oct de la Chocolatería,
  o el 29-oct si D53).

### Paquete Stripe para John (único paso no delegable)
- **Nombre del producto:** Tareas Recurrentes: Taquería Mexicana
- **Precio:** 14,00 € (pago único) · **moneda:** EUR
- **Descripción (259 caracteres, prosa, sin bullets):** Kit de Tareas de taquería mexicana: 11 Excel con 298 tareas en 22 checklists de apertura, cierre, trompo, tortillería, salsas y alérgenos, manager y perfiles, más briefing pre-servicio y calendario anual. Pago único, acceso vitalicio. Excel, Sheets o Numbers.
- **Confirmation URL (tras el pago):** `https://aichef.pro/kit-tareas-taqueria-access?session_id={CHECKOUT_SESSION_ID}`
- **Env var en Netlify (scope builds):** `VITE_STRIPE_PAYMENT_LINK_TAREAS_TAQUERIA` = URL del Payment Link
- Cripto: nace con NOWPayments (`CRYPTO_PRODUCTS=all`); el importe sale de `product-prices.ts` (regenerado en F3).
