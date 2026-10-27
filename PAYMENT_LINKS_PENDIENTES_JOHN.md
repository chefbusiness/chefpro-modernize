# Payment Links pendientes — tareas de John (Stripe)

> Sesión Claude Code (Mac). **TRES pendientes (27-oct-2026): tienda EN — Hotel, Ice Cream Shop y Wedding Venue.**

## ⏳ PENDIENTES (27-oct-2026): tres productos EN listos a falta del link — John: «escoge los tres que siguen… completos me dices y creamos los enlaces de pago en Stripe»

Los tres van en USD, con pago único, impuesto automático con precio *exclusive* (como el resto de la tienda EN), factura
activada y redirección a su `/access`. Orden de fusión: **#170 → #171 → #172** (van apilados). La env de Netlify la pone Claude
(scope builds, all) y regenera `payment-links.ts` con `sync-payment-links.py`.

### 1. ⏳ Hotel Checklists Kit Pro (EN) — PR #170

| Campo | Valor |
|---|---|
| Nombre del producto | Hotel Checklists Kit Pro - AI Chef Pro |
| Precio | **29,00 USD**, pago único, impuesto automático con precio *exclusive* |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/en/digital-products/hotel-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa) | 19 ready-to-use Excel workbooks with 636 pre-written tasks for a full-service hotel: breakfast, buffet, restaurant, bar and banquet F&B, front desk and night audit, guest services, housekeeping, public areas, pool, patio, preventive maintenance, back office, spa and the cash drawer, plus an annual task calendar and a daily F&B briefing template. Adapted to US standards (FDA Food Code 2022 in °F, MAHC pool and spa guidance, OSHA) and printable on US Letter, with a US, UK, Canada and Australia hospitality equivalents guide. Instant download, lifetime access and free updates. |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_HOTEL_CHECKLISTS_KIT` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/tareas-hotel-hero.jpg` |

### 2. ⏳ Ice Cream Shop Business Plan Kit (EN) — PR #171

| Campo | Valor |
|---|---|
| Nombre del producto | Ice Cream Shop Business Plan Kit - AI Chef Pro |
| Precio | **39,00 USD**, pago único, impuesto automático con precio *exclusive* |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/en/digital-products/ice-cream-shop-business-plan/access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa) | Complete business plan kit to open a neighborhood ice cream shop that makes its ice cream on site: a 10-section Word business plan, 3-year Excel financial projections with monthly cash flow, seasonality and SBA loan sizing, and an 80-task startup checklist, all built on a worked US case you can edit with your own numbers. Includes a US, UK, Canada and Australia hospitality equivalents guide. Instant download, lifetime access and free updates. |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_BUSINESS_PLAN` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-heladeria-hero.jpg` |

### 3. ⏳ Wedding Venue Business Plan Kit (EN) — PR #172

| Campo | Valor |
|---|---|
| Nombre del producto | Wedding Venue Business Plan Kit - AI Chef Pro |
| Precio | **49,00 USD**, pago único, impuesto automático con precio *exclusive* (5 ficheros, como el ES a 45 €) |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/en/digital-products/wedding-venue-business-plan/access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa) | Complete business plan kit to open a barn or estate wedding and event venue with an exclusive caterer: a 10-section Word business plan, 3-year Excel financial projections with monthly cash flow and SBA loan sizing, an 84-task startup checklist, a wedding and event pricing calculator and an editable venue rental agreement template (a template, not legal advice: have a local attorney review it), all built on a worked US case you can adapt to your own venue. Includes a US, UK, Canada and Australia hospitality equivalents guide. Instant download, lifetime access and free updates. |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_WEDDING_VENUE_BUSINESS_PLAN` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-finca-hero.jpg` |

## ✅ HECHOS (25-oct-2026, noche): los DOS de la pizzería, ES y EN — John: «dejar la versión en los dos idiomas en producción»

### 1. ✅ Plan de Negocio: Pizzería Napolitana (ES) — PR #165, link creado el 25-oct-2026

Link de John: https://buy.stripe.com/3cI6oA6Wo1NYezBejH6oo23 (`plink_1UUXG84CcdRGidmEsDF3iCG4`). Comprobado con la CLI de
Stripe: 3500 EUR, pago único, *exclusive*, impuesto automático, factura y redirección a `/plan-negocio-pizzeria-access`.
Env de Netlify creada (builds, all) y `payment-links.ts` regenerado.

Mismo patrón que la heladería (`plink_1UUSdP4CcdRGidmEm3lXcQyH`, 35 EUR):

| Campo | Valor |
|---|---|
| Nombre del producto | Plan de Negocio Pizzería Napolitana - AI Chef Pro |
| Precio | **35,00 EUR**, pago único, impuesto automático con precio *exclusive* |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/plan-negocio-pizzeria-access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa) | Plan de negocio completo para abrir una pizzería con horno de leña y sala: plan en Word de 10 secciones, plan financiero en Excel de 9 hojas con tesorería mes a mes, checklist de apertura de 80 tareas, calculadora de masa y escandallo por pizza y guía de equivalencias para Latinoamérica |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_PLAN_PIZZERIA` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-pizzeria-hero.jpg` |

### 2. ✅ Pizza Shop Business Plan Kit (EN) — PR #166, link creado el 25-oct-2026

Link de John: https://buy.stripe.com/3cI28k4Og9gq0IL4J76oo24 (`plink_1UUXZ54CcdRGidmEovs56WB3`; nombre en Stripe «Neapolitan-style
Pizza Shop Business Plan Kit - AI Chef Pro»). Comprobado con la CLI: 3900 USD, pago único, *exclusive*, impuesto automático, factura y
redirección a `/en/digital-products/pizza-shop-business-plan/access`. Env de Netlify creada (builds, all) y `payment-links.ts` regenerado.

| Campo | Valor |
|---|---|
| Nombre del producto | Pizza Shop Business Plan Kit - AI Chef Pro |
| Precio | **39,00 USD**, pago único, impuesto automático con precio *exclusive* (como el BBQ y la Paella) |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/en/digital-products/pizza-shop-business-plan/access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa) | Complete business plan kit to open a Neapolitan-style pizza shop with a wood-fired oven: a 10-section Word business plan, 3-year Excel financial projections with monthly cash flow, an opening checklist, a pizza dough and food cost calculator, and a hospitality equivalents guide for the US, UK, Canada and Australia |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_PIZZA_SHOP_BUSINESS_PLAN` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-pizzeria-hero.jpg` |

## ✅ Plan de Negocio: Finca de Eventos y Bodas (ES) — PR #164, link creado el 25-oct-2026

Link de John: https://buy.stripe.com/14A7sE4Og9gqajla3r6oo22 (`plink_1UUVHD4CcdRGidmEy72mv0Yh`). Comprobado con la CLI de
Stripe: 4500 EUR, pago único, *exclusive*, impuesto automático, factura y redirección a `/plan-negocio-finca-eventos-bodas-access`.
Env de Netlify creada (builds, all) y `payment-links.ts` regenerado.

Mismo patrón que el de la heladería (`plink_1UUSdP4CcdRGidmEm3lXcQyH`) y los planes de eventos a 45 €:

| Campo | Valor |
|---|---|
| Nombre del producto | Plan de Negocio Finca de Eventos y Bodas - AI Chef Pro |
| Precio | **45,00 EUR**, pago único, impuesto automático con precio *exclusive* |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/plan-negocio-finca-eventos-bodas-access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa) | Plan de negocio completo para montar una finca de eventos y bodas arrendada, con catering exclusivo concesionado: plan en Word de 10 secciones, plan financiero en Excel de 9 hojas con tesorería mes a mes, checklist de apertura de 84 tareas, calculadora de presupuesto del espacio, modelos de contrato y guía de equivalencias para Latinoamérica |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_PLAN_FINCA_EVENTOS` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-finca-hero.jpg` |


## ✅ Plan de Negocio: Heladería Artesanal (ES) — PR #161, link creado el 25-oct-2026

Link de John: https://buy.stripe.com/5kQ28k94w78i2QT8Zn6oo21 (`plink_1UUSdP4CcdRGidmEm3lXcQyH`). Comprobado con la CLI de
Stripe: 3500 EUR, pago único, *exclusive*, impuesto automático, factura y redirección a `/plan-negocio-heladeria-access`.
Env de Netlify creada (builds, all) y `payment-links.ts` regenerado.

Mismo patrón que el de la panadería (`plink_1TVHkk4CcdRGidmE0rdXrGbn`, comprobado con la CLI el 25-oct):

| Campo | Valor |
|---|---|
| Nombre del producto | Plan de Negocio Heladería Artesanal - AI Chef Pro |
| Precio | **35,00 EUR**, pago único, impuesto automático con precio *exclusive* (como la panadería) |
| Factura | activada (como la panadería) |
| Después del pago | redirigir a `https://aichef.pro/plan-negocio-heladeria-access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa) | Plan de negocio completo para abrir una heladería artesanal con obrador propio: plan en Word de 10 secciones, plan financiero en Excel con fórmulas vivas y tesorería mes a mes, checklist de apertura con 80 tareas y guía de equivalencias para Latinoamérica |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_PLAN_HELADERIA` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-heladeria-hero.jpg` |

## ✅ Lote EN de 5 — cerrado y LIVE el 25-oct-2026

John (24-oct): «cuando tengas cinco productos terminados y yo esté de vuelta en el ordenador, hacemos la configuración en
Stripe para crear los payment links». Los cinco se crearon el 25-oct y se comprobaron con la CLI de Stripe (USD, pago único,
impuesto automático *exclusive*, redirección a `/access`).

| Producto | Precio | Payment Link | Env de Netlify |
|---|---|---|---|
| Ice Cream Shop Checklists Kit Pro | $19 | https://buy.stripe.com/28E3co5Sk64eezB3F36oo1W | `VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_CHECKLISTS_KIT` |
| Chocolate Shop Checklists Kit Pro | $19 | https://buy.stripe.com/eVqdR2dkM78iajl0sR6oo1X | `VITE_STRIPE_PAYMENT_LINK_CHOCOLATE_SHOP_CHECKLISTS_KIT` |
| Pastry Shop Checklists Kit Pro | $19 | https://buy.stripe.com/00w4gs5Sk64eajlgrP6oo1Y | `VITE_STRIPE_PAYMENT_LINK_PASTRY_SHOP_CHECKLISTS_KIT` |
| BBQ Catering Business Plan Kit | $39 | https://buy.stripe.com/fZufZafsUdwG4Z1fnL6oo1Z | `VITE_STRIPE_PAYMENT_LINK_BBQ_CATERING_BUSINESS_PLAN` |
| Paella Catering Business Plan Kit | $39 | https://buy.stripe.com/14AdR294wgISajl5Nb6oo20 | `VITE_STRIPE_PAYMENT_LINK_PAELLA_CATERING_BUSINESS_PLAN` |

PR #156 → #159 fusionados (merge `7e7afc6e`). Gates LIVE, correos y routine: `scripts/productos-digitales/CALENDARIO-V2-SEMANAL.md`
(entrada del 25-oct).

## Cómo se crea un link (para el próximo lote)

- Stripe → Payment Links → producto nuevo, **USD**, pago único, **impuesto automático con precio *exclusive***.
- «Después del pago» → redirigir a `https://aichef.pro/en/digital-products/<slug>/access?session_id={CHECKOUT_SESSION_ID}`
  (con `{CHECKOUT_SESSION_ID}` literal).
- Descripción en prosa, sin viñetas ni comillas al final.
- Claude lo comprueba con la CLI y hace el resto: env en Netlify, `sync-payment-links.py`, fusión, gates en vivo, sitemap en GSC
  y correo en la cola EN.
