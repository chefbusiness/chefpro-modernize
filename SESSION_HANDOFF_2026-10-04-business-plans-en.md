# Handoff 4-oct-2026 — Tienda EN: 4 business plans (Food Truck + Coffee Shop listos; Restaurant + Bakery en F2)

> Sesión Claude Code. Mismo día: los 4 EN del 3-oct (#106-#109) quedaron LIVE (merge `1411b467`) con correos EN programados
> 10/15/20/25-oct. Después, con DataForSEO US, se eligieron 4 planes de negocio (John aprobó y delegó la elección).

## 🔴 TAREA DE JOHN — Payment Links (USD, pago único, Adaptive Pricing, impuesto automático, «redirigir a tu web»)

| Producto | Precio | Redirección tras el pago | Env var (la pone Claude, scope builds) |
|---|---|---|---|
| **Food Truck Business Plan Kit** | **$39** | `https://aichef.pro/en/digital-products/food-truck-business-plan/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_FOOD_TRUCK_BUSINESS_PLAN` |
| **Coffee Shop Business Plan Kit** | **$39** | `https://aichef.pro/en/digital-products/coffee-shop-business-plan/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_COFFEE_SHOP_BUSINESS_PLAN` |
| Restaurant Business Plan Kit (cuando esté) | $39 | `https://aichef.pro/en/digital-products/restaurant-business-plan/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_RESTAURANT_BUSINESS_PLAN` |
| Bakery Business Plan Kit (cuando esté) | $39 | `https://aichef.pro/en/digital-products/bakery-business-plan/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_BAKERY_BUSINESS_PLAN` |

Descripciones (prosa):
- **Food Truck Business Plan Kit** — «A ready-to-edit food truck business plan in Word (10 sections, written for a US truck)
  with Excel financial projections: startup costs, 3-year P&L, 12-month cash flow, break-even, staffing, scenarios and a
  financing sheet with loan schedule and DSCR. Plus a 68-task startup checklist and a benchmarks bonus. One-time payment,
  lifetime access.»
- **Coffee Shop Business Plan Kit** — «A ready-to-edit coffee shop business plan in Word (10 sections, coffee shop with
  brunch) with Excel financial projections: startup costs, 3-year P&L, 12-month cash flow, break-even, staffing, scenarios
  and a financing sheet with loan schedule and DSCR. Plus a 75-task opening checklist and a benchmarks bonus. One-time
  payment, lifetime access.»

## 1. Food Truck + Coffee Shop Business Plan Kit — PR #110, listos a falta del Payment Link

- Rama `feat/business-plans-en`. Todo en `scripts/productos-digitales/business-plans-en/` (SPEC D1-D29, F1, F2-NOTAS §1-§8,
  F3-NOTAS, REVISION-FINAL.md). Plantilla `PlanNegocioLandingPage.astro` con `lang` (las 15 landings ES byte a byte iguales).
- Circuito: F1 Opus · plantilla Opus · F3 Opus · F2-t1 Opus (extracción) · 7 tandas Sonnet (GM, GFT, GCAF, ft_a, ft_b,
  caf_a, caf_b) · F2-t2 Opus en el VPS (aplicar_en + gates + calibración + docx) · 1 revisión Opus que RECALCULA · 1 ronda
  de arreglos. ≈ 4,3 M tokens de subagentes (techo 5,9 M).
- Caso base final (tras M1, tarjeta 3,5 %): FT 80 clientes/día, ventas $291,200, neto 6,7 %, DSCR mín. 1,96×, caja mín.
  $24,330, holgura 20,3 % · CAF 145 clientes/día, $542,300, neto 7,3 %, DSCR 2,42×, caja $64,487, holgura 20,6 %.
- Gates: G1-G9 + autotest 20/20 + idempotencia 0 (VPS); preview #110: `tienda-gate` verde, `--es-identico` 13/15 + las 2
  esperadas solo hreflang, `gate-flujo-postpago --only` ×2 fallan SOLO por el Payment Link (3/3 descargas OK).
- Correos EN listos (sin programar): food truck **30-oct 14:00Z**, coffee shop **4-nov 14:00Z** (programable desde el 5-oct).

## 2. Restaurant + Bakery Business Plan Kit — PR #111 (borrador, base `feat/business-plans-en`)

- Rama `feat/business-plans-en-2`. Docs en `scripts/productos-digitales/business-plans-en-2/` (SPEC-delta D30-D47).
- Hecho: F1 delta, F3 completa (fichas con `TODO_CIFRA` que la F2 rellena; el `tienda-gate` da rojo si quedan). En curso:
  F2 tanda 1 (generalizar el código común a 4 libros más, con FT/CAF regenerados idénticos como condición dura).
- Sin deploy preview: Netlify solo construye PR contra `main`. Se tendrá al fusionar el #110 (el #111 se reapunta a `main`).
- Correos EN: restaurant **9-nov**, bakery **14-nov** 14:00Z.

## 3. Pasos para publicar (cuando John pase los links)

1. Comprobar cada link con la CLI de Stripe (`stripe payment_links list --live` + `list_line_items`): USD 39, redirección.
2. `netlify env:set <VAR> <url> --scope builds` (las de la tabla).
3. En el worktree de la rama: `python3 scripts/productos-digitales/sync-payment-links.py` → commit + push → preview →
   `gate-flujo-postpago.py --base https://deploy-preview-<n>--aichefpro.netlify.app --crypto-products all --crypto-exclude
   pro-prompts-ebook --only <slug>` sin fallos.
4. `gh pr ready <n>` y merge con MERGE COMMIT. Gates LIVE: `gate-flujo-postpago --only` ×N, `tienda-gate --base
   https://aichef.pro`, `robots-gate --live`, `miselup-gate`, `datafast-gate`; tarjetas vivas en `/en/digital-products`.
5. Correos: `resend-broadcast.py --html <fichero> --subject "<ASUNTO del comentario>" --segment
   d06ed053-4327-4bec-9e3b-25a9ee9f6704 --from "AI Chef Pro <hello@news.aichef.pro>" --test john@chefbusiness.co` y luego
   `--scheduled-at` en las fechas de arriba.

## 4. Pendientes para John (no bloquean)

- **Precio tachado ($129) en las landings EN**: la revisión marcó que en EE. UU. un «precio anterior» al que nunca se ha
  vendido es el ejemplo de manual de la FTC (16 CFR 233.1). Se quitó «regular price» de los correos de estos planes; los
  correos de HACCP, eBook y Food Cost también lo dicen (no tocados). Decidir la política de anclas de la tienda EN.
- El carrusel de logos de las landings EN de KITS (KitExcelLandingPage) muestra Google Sheets/PDF; en los planes EN ya solo
  Excel y Word.
- Verificación humana recomendada: abrir 2-3 xlsx/docx por producto en Excel/Word y repasar las landings a 360 px.

Sesión Claude Code · `Via: Claude Code`.
