# Payment Links pendientes — tareas de John (Stripe)

> Sesión Claude Code (Mac).

## ⏳ PENDIENTE (31-oct-2026): Plan de Negocio: Hamburguesería Smash (ES) — rama `feat/plan-negocio-hamburgueseria`

Producto nº 59, 35 €. La landing (`/plan-negocio-hamburgueseria`) deja el botón en `#comprar` hasta que exista el link. Cuando lo crees,
Claude pone la env de Netlify, regenera `payment-links.ts`, comprueba el link con la CLI y fusiona.

| Campo | Valor |
|---|---|
| Nombre del producto | Plan de Negocio: Hamburguesería Smash - AI Chef Pro |
| Precio | **35,00 EUR**, pago único, impuesto automático con precio *exclusive* (como pizzería, taquería, pollería y sushi bar) |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/plan-negocio-hamburgueseria-access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa, 259 caracteres) | Plan de negocio para montar una hamburguesería smash con sala, para llevar y a domicilio: plan en Word de 10 secciones, plan financiero en Excel a 3 años, checklist de 80 tareas, calculadora de la carne, las patatas y el escandallo, y guía para Latinoamérica. |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_PLAN_HAMBURGUESERIA` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-hamburgueseria-hero.jpg` |

## ✅ HECHO (31-oct-2026): Lote de 4 checklists EN — PR #189

Links de John comprobados con la CLI (`--live`): pago único, *exclusive*, impuesto automático, factura y redirección a
`/en/digital-products/<slug>/access?session_id={CHECKOUT_SESSION_ID}`. Envs de Netlify creadas (builds) y `payment-links.ts` regenerado.

| Producto Stripe | Precio | Link | Env |
|---|---|---|---|
| Food Truck Checklists Kit Pro | 15 USD | https://buy.stripe.com/9B6bIUdkMdwGfDF6Rf6oo2h (`plink_1UWXsu4CcdRGidmElGA8qDvw`) | `VITE_STRIPE_PAYMENT_LINK_FOOD_TRUCK_CHECKLISTS_KIT` |
| Bakery Checklists Kit Pro | 15 USD | https://buy.stripe.com/dRmfZadkMboyfDFcbz6oo2i (`plink_1UWXx04CcdRGidmEmuFhlUp2`) | `VITE_STRIPE_PAYMENT_LINK_BAKERY_CHECKLISTS_KIT` |
| Seafood Restaurant Checklists Kit Pro | 15 USD | https://buy.stripe.com/5kQ28k3Kcboy1MP2AZ6oo2j (`plink_1UWY134CcdRGidmES3rTqNn5`) | `VITE_STRIPE_PAYMENT_LINK_SEAFOOD_RESTAURANT_CHECKLISTS_KIT` |
| Fine Dining Checklists Kit Pro | 19 USD | https://buy.stripe.com/5kQ6oAcgI8cmajlfnL6oo2k (`plink_1UWY3e4CcdRGidmEnz6cQgL7`) | `VITE_STRIPE_PAYMENT_LINK_FINE_DINING_CHECKLISTS_KIT` |

## ✅ HECHO (31-oct-2026): Plan de Negocio: Sushi Bar (ES) — PR #190

Link de John: https://buy.stripe.com/00w6oA0y0boy6357Vj6oo2f (`plink_1UWXiC4CcdRGidmEKmziMiYi`). Comprobado con la CLI (`--live`): 35 EUR,
pago único, *exclusive*, impuesto automático, factura y redirección a `/plan-negocio-sushi-bar-access`. Env de Netlify creada (builds) y
`payment-links.ts` regenerado.

| Campo | Valor |
|---|---|
| Nombre del producto | Plan de Negocio Sushi Bar - AI Chef Pro |
| Precio | **35,00 EUR**, pago único, impuesto automático con precio *exclusive* (como pizzería, taquería y pollería) |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/plan-negocio-sushi-bar-access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa, 249 caracteres) | Plan de negocio para montar un sushi bar o restaurante de sushi: plan en Word de 10 secciones, plan financiero en Excel a 3 años, checklist de 80 tareas, calculadora del pescado, el arroz y el escandallo por pieza y canal, y guía para Latinoamérica. |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_PLAN_SUSHI_BAR` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-sushi-bar-hero.jpg` |

## ✅ HECHO (31-oct-2026): Sushi Restaurant Business Plan Kit (EN) — PR #192 (apilado, fusionado DESPUÉS del Sushi Bar ES)

Link de John: https://buy.stripe.com/5kQfZabcEeAKfDFcbz6oo2g (`plink_1UWXmt4CcdRGidmEyUH8Az1d`). Comprobado con la CLI (`--live`): 39 USD,
pago único, *exclusive*, impuesto automático, factura y redirección a `/access`. Env de Netlify creada (builds) y `payment-links.ts` regenerado.

| Campo | Valor |
|---|---|
| Nombre del producto | Sushi Restaurant Business Plan Kit - AI Chef Pro |
| Precio | **39,00 USD**, pago único, impuesto automático con precio *exclusive* (como Taco Shop y Rotisserie) |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/en/digital-products/sushi-restaurant-business-plan/access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa, 244 caracteres) | Business plan kit to open a neighborhood sushi restaurant with a sushi bar, take-out and delivery: 10-section Word plan, 3-year Excel financial projections with SBA loan, 80-task startup checklist, and a fish, sushi rice and costing calculator. |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_SUSHI_RESTAURANT_BUSINESS_PLAN` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-sushi-bar-hero.jpg` |

## ✅ HECHO (29-oct-2026): Plan de Negocio: Taquería (ES) — PR #181

Link de John: https://buy.stripe.com/fZu5kwbcEcsCcrt1wV6oo2a (`plink_1UVou74CcdRGidmEufF1axkD`). Comprobado con la CLI: 3500 EUR, pago único,
*exclusive*, impuesto automático, factura y redirección a `/plan-negocio-taqueria-access`. Env de Netlify creada (builds) y `payment-links.ts` regenerado.

| Campo | Valor |
|---|---|
| Nombre del producto | Plan de Negocio Taquería - AI Chef Pro |
| Precio | **35,00 EUR**, pago único, impuesto automático con precio *exclusive* (como pizzería y cafetería móvil) |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/plan-negocio-taqueria-access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa, 245 caracteres) | Plan de negocio para montar una taquería con trompo, barra de salsas y para llevar: plan en Word de 10 secciones, plan financiero en Excel a 3 años, checklist de 80 tareas, calculadora del trompo y escandallo por taco, y guía para Latinoamérica. |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_PLAN_TAQUERIA` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-taqueria-hero.jpg` |

## ✅ HECHO (29-oct-2026): Plan de Negocio: Pollería y Asador de Pollos (ES) — PR #183

Link de John: https://buy.stripe.com/fZu28k3KcgISgHJ5Nb6oo2c (`plink_1UVyTF4CcdRGidmEg0Uy9RG7`). Comprobado con la CLI: 3500 EUR, pago único,
*exclusive*, impuesto automático, factura y redirección a `/plan-negocio-polleria-access`. Env de Netlify creada (builds) y `payment-links.ts` regenerado.

| Campo | Valor |
|---|---|
| Nombre del producto | Plan de Negocio Pollería y Asador de Pollos - AI Chef Pro |
| Precio | **35,00 EUR**, pago único, impuesto automático con precio *exclusive* (como pizzería y taquería) |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/plan-negocio-polleria-access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa, 267 caracteres) | Plan de negocio para montar una pollería o asador de pollos: plan en Word de 10 secciones con las cinco corrientes del pollo asado, plan financiero en Excel a 3 años, checklist de 80 tareas, calculadora del pollo, el asador y el escandallo, y guía para Latinoamérica. |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_PLAN_POLLERIA` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-polleria-hero.jpg` |

## ✅ HECHO (29-oct-2026): Rotisserie Chicken Restaurant Business Plan Kit (EN) — PR #184 (apilado, se fusiona DESPUÉS de la Pollería ES)

Link de John: https://buy.stripe.com/4gM14g80s8cm7791wV6oo2d (`plink_1UVycF4CcdRGidmEOnjuRLkO`). Comprobado con la CLI: 3900 USD, pago único,
*exclusive*, impuesto automático, factura y redirección a `/access`. Env de Netlify creada (builds) y `payment-links.ts` regenerado.

| Campo | Valor |
|---|---|
| Nombre del producto | Rotisserie Chicken Restaurant Business Plan Kit - AI Chef Pro |
| Precio | **39,00 USD**, pago único, impuesto automático con precio *exclusive* |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/en/digital-products/rotisserie-chicken-restaurant-business-plan/access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa, 260 caracteres) | Business plan kit to open a rotisserie chicken restaurant (Peruvian pollo a la brasa, peri-peri or charcoal chicken): 10-section Word plan, 3-year Excel financial projections with SBA loan, 80-task startup checklist, and a chicken yield and costing calculator. |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_ROTISSERIE_CHICKEN_RESTAURANT_BUSINESS_PLAN` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-polleria-hero.jpg` |

## ✅ HECHO (29-oct-2026): Taco Shop Business Plan Kit (EN) — PR #182 (apilado, se fusiona DESPUÉS del ES)

Link de John: https://buy.stripe.com/dRm7sE5Sk64e0IL0sR6oo2b (`plink_1UVoxK4CcdRGidmEeSCIcHgk`). Comprobado con la CLI: 3900 USD, pago único,
*exclusive*, impuesto automático, factura y redirección a `/access`. Env de Netlify creada (builds) y `payment-links.ts` regenerado.

| Campo | Valor |
|---|---|
| Nombre del producto | Taco Shop Business Plan Kit - AI Chef Pro |
| Precio | **39,00 USD**, pago único, impuesto automático con precio *exclusive* |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/en/digital-products/taco-shop-business-plan/access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa, 216 caracteres) | Business plan kit to open a taco shop or taqueria: 10-section Word plan, 3-year Excel financial projections with monthly cash flow and SBA loan, 80-task startup checklist, and a trompo yield and taco cost calculator. |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_TACO_SHOP_BUSINESS_PLAN` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-taqueria-hero.jpg` |

## ✅ HECHOS (28-oct-2026): los DOS de la cafetería móvil, ES y EN, LIVE (#177 `176b10d0` · #178 `13734218`) — John: «un producto nuevo en español y su versión en inglés en producción, las dos tareas de hoy»

### 1. Plan de Negocio: Cafetería Móvil para Eventos (ES) — PR #177

| Campo | Valor |
|---|---|
| Nombre del producto | Plan de Negocio Cafetería Móvil para Eventos - AI Chef Pro |
| Precio | **45,00 EUR**, pago único, impuesto automático con precio *exclusive* (como pizzería y finca) |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/plan-negocio-cafeteria-movil-eventos-access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa, 257 caracteres) | Plan de negocio para montar una barra de café de especialidad para bodas, empresas y ferias: plan en Word de 10 secciones, plan financiero en Excel, checklist de 80 tareas, calculadora de presupuesto por evento, modelo de contrato y guía para Latinoamérica. |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_PLAN_CAFETERIA_MOVIL` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-cafeteria-movil-hero.jpg` |

### 2. Coffee Cart Business Plan Kit (EN) — rama `feat/coffee-cart-business-plan` (PR apilado, se fusiona después del ES)

| Campo | Valor |
|---|---|
| Nombre del producto | Coffee Cart Business Plan Kit - AI Chef Pro |
| Precio | **39,00 USD**, pago único, impuesto automático con precio *exclusive* |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/en/digital-products/coffee-cart-business-plan/access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa, 247 caracteres) | Business plan kit to start a coffee cart and espresso catering company: 10-section Word plan, 3-year Excel financial projections with monthly cash flow and SBA loan, startup checklist, per-guest pricing calculator and a service agreement template. |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_COFFEE_CART_BUSINESS_PLAN` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-cafeteria-movil-hero.jpg` |

## ✅ HECHOS (27-oct-2026): tres productos EN — John: «escoge los tres que siguen… completos me dices y creamos los enlaces de pago en Stripe»

Los tres van en USD, con pago único, impuesto automático con precio *exclusive* (como el resto de la tienda EN), factura
activada y redirección a su `/access`. Orden de fusión: **#170 → #171 → #172** (van apilados). La env de Netlify la pone Claude
(scope builds, all) y regenera `payment-links.ts` con `sync-payment-links.py`.

### 1. ✅ Hotel Checklists Kit Pro (EN) — PR #170, link creado el 27-oct-2026

Link de John: https://buy.stripe.com/eVqfZa94w0JU2QT6Rf6oo25 (`plink_1UV6mM4CcdRGidmEPIg3fmmj`). Comprobado con la CLI: 2900 USD, pago único,
*exclusive*, impuesto automático, factura y redirección a `/access`. Env de Netlify creada (builds, all) y `payment-links.ts` regenerado.

| Campo | Valor |
|---|---|
| Nombre del producto | Hotel Checklists Kit Pro - AI Chef Pro |
| Precio | **29,00 USD**, pago único, impuesto automático con precio *exclusive* |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/en/digital-products/hotel-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa, ≤ 260) | 19 Excel workbooks with 636 ready-to-use hotel tasks: F&B, front desk, housekeeping, pool, spa, maintenance and cash drawer. US standards (FDA Food Code, OSHA), US Letter. Works in Excel, Google Sheets and Numbers. Instant download, lifetime access. |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_HOTEL_CHECKLISTS_KIT` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/tareas-hotel-hero.jpg` |

### 2. ✅ Ice Cream Shop Business Plan Kit (EN) — PR #171, link creado el 27-oct-2026

Link de John: https://buy.stripe.com/aFadR2bcEdwGdvx5Nb6oo26 (`plink_1UV6rK4CcdRGidmE9nLDNQrU`). Comprobado con la CLI: 3900 USD, pago único,
*exclusive*, impuesto automático, factura y redirección a `/access`. Env de Netlify creada (builds, all) y `payment-links.ts` regenerado.

| Campo | Valor |
|---|---|
| Nombre del producto | Ice Cream Shop Business Plan Kit - AI Chef Pro |
| Precio | **39,00 USD**, pago único, impuesto automático con precio *exclusive* |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/en/digital-products/ice-cream-shop-business-plan/access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa, ≤ 260) | Business plan kit to open an ice cream shop: 10-section Word plan, 3-year Excel financial projections with monthly cash flow and SBA loan, and an 80-task startup checklist, built on a worked US example. Works in Excel and Google Sheets. Instant download. |
| Env de Netlify (la pone Claude) | `VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_BUSINESS_PLAN` (scope builds) |
| Imagen | `astro-site/public/lovable-uploads/ai-gallery/plan-heladeria-hero.jpg` |

### 3. ✅ Wedding Venue Business Plan Kit (EN) — PR #172, link creado el 27-oct-2026

Link de John: https://buy.stripe.com/9B69AM4Og0JUgHJ5Nb6oo27 (`plink_1UV6uO4CcdRGidmEotbwEDkd`). Comprobado con la CLI: 4900 USD, pago único,
*exclusive*, impuesto automático, factura y redirección a `/access`. Env de Netlify creada (builds, all) y `payment-links.ts` regenerado.

| Campo | Valor |
|---|---|
| Nombre del producto | Wedding Venue Business Plan Kit - AI Chef Pro |
| Precio | **49,00 USD**, pago único, impuesto automático con precio *exclusive* (5 ficheros, como el ES a 45 €) |
| Factura | activada |
| Después del pago | redirigir a `https://aichef.pro/en/digital-products/wedding-venue-business-plan/access?session_id={CHECKOUT_SESSION_ID}` |
| Descripción (prosa, ≤ 260) | Business plan kit to open a wedding and event venue: 10-section Word plan, 3-year Excel projections with SBA loan, 84-task startup checklist, pricing calculator and venue rental agreement template. Works in Excel and Google Sheets. Instant download. |
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
