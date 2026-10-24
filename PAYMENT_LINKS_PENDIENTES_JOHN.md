# Payment Links pendientes — tareas de John (Stripe)

> Sesión Claude Code (Mac), abierto el **24-oct-2026**. John (24-oct): «cuando tengas cinco productos terminados y yo
> esté de vuelta en el ordenador, hacemos la configuración en Stripe para crear los payment links. De momento apárcalos
> como tareas para mí y continúa tú con los siguientes productos».
>
> ✅ **LOS 5 ESTÁN LISTOS (24-oct, noche).** Cada uno está terminado y en un PR en borrador; solo le falta su Payment Link.
> Los PR van **apilados** (156 → 157 → 158 → 159: cada rama sale de la anterior), así que se fusionan en orden, de arriba abajo
> (o el #159 con merge commit, que incluye los cuatro de abajo). Preview con los 5: https://deploy-preview-159--aichefpro.netlify.app/en/digital-products

## Cómo crear cada link (igual para todos)

- Stripe → Payment Links → producto nuevo, **USD**, pago único, **impuesto automático con precio *exclusive*** (como el
  resto de la tienda EN). Adaptive Pricing ya está activo en la cuenta.
- «Después del pago» → redirigir a la URL de la tabla (con `{CHECKOUT_SESSION_ID}` literal).
- Descripción: el texto de la tabla, en prosa, tal cual.
- Pásame los links (o solo dime «hechos»: los leo yo con la CLI de Stripe) y hago el resto: env en Netlify,
  `sync-payment-links.py`, fusionar, gates en vivo, sitemap en GSC y correos de lanzamiento en la cola EN.

## Productos

| # | Producto | Precio | PR | Estado |
|---|---|---|---|---|
| 1 | Ice Cream Shop Checklists Kit Pro | $19 | #156 | ✅ listo |
| 2 | Chocolate Shop Checklists Kit Pro | $19 | #157 | ✅ listo |
| 3 | Pastry Shop Checklists Kit Pro | $19 | #157 | ✅ listo |
| 4 | BBQ Catering Business Plan Kit | $39 | #158 | ✅ listo |
| 5 | Paella Catering Business Plan Kit | $39 | #159 | ✅ listo |

### 1. Ice Cream Shop Checklists Kit Pro — $19.00 USD (PR #156)

- Nombre en Stripe: **Ice Cream Shop Checklists Kit Pro**
- Redirección: `https://aichef.pro/en/digital-products/ice-cream-shop-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}`
- Descripción: Nine Excel checklist templates and three bonuses for ice cream shops: opening and closing, pasteurizing and batch freezing, manager and role duties, cleaning and maintenance, peak season and ice cream catering, cash drawer. One-time payment, lifetime access.
- Env que crearé: `VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_CHECKLISTS_KIT`
- Ojo: este PR lleva también el parche de seguridad del kit ES de heladería (grasas y yemas antes de pasteurizar).

### 2. Chocolate Shop Checklists Kit Pro — $19.00 USD (PR #157)

- Nombre en Stripe: **Chocolate Shop Checklists Kit Pro**
- Redirección: `https://aichef.pro/en/digital-products/chocolate-shop-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}`
- Descripción: Nine Excel checklist templates and three bonuses for chocolate shops: opening and closing, tempering and molding, manager and role duties, cleaning and maintenance, holiday season, Valentine's Day and Easter, cash drawer with sales by weight. One-time payment, lifetime access.
- Env que crearé: `VITE_STRIPE_PAYMENT_LINK_CHOCOLATE_SHOP_CHECKLISTS_KIT`
- Ojo: el PR lleva también un parche de seguridad del kit ES de chocolatería (ganache de nata fresca en frío, etiqueta con alérgenos, exclusión por síntomas).

### 3. Pastry Shop Checklists Kit Pro — $19.00 USD (PR #157)

- Nombre en Stripe: **Pastry Shop Checklists Kit Pro**
- Redirección: `https://aichef.pro/en/digital-products/pastry-shop-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}`
- Descripción: Thirteen Excel templates and three bonuses for pastry shops: nine checklists for opening and closing, production stations, manager and role duties, cleaning, holiday campaigns and the cash drawer, plus four logs for weekly production and waste, custom cake orders, the bakery allergen chart and temperatures. One-time payment, lifetime access.
- Env que crearé: `VITE_STRIPE_PAYMENT_LINK_PASTRY_SHOP_CHECKLISTS_KIT`

### 4. BBQ Catering Business Plan Kit — $39.00 USD (PR #158)

- Nombre en Stripe: **BBQ Catering Business Plan Kit**
- Redirección: `https://aichef.pro/en/digital-products/bbq-catering-business-plan/access?session_id={CHECKOUT_SESSION_ID}`
- Descripción: Business plan kit for an off-site BBQ catering company: a 10-section Word business plan, 3-year Excel financial projections, a per-guest pricing calculator with meat yields and shopping lists by guest count, and a 68-task startup checklist. One-time payment, lifetime access.
- Env que crearé: `VITE_STRIPE_PAYMENT_LINK_BBQ_CATERING_BUSINESS_PLAN`

### 5. Paella Catering Business Plan Kit — $39.00 USD (PR #159)

- Nombre en Stripe: **Paella Catering Business Plan Kit**
- Redirección: `https://aichef.pro/en/digital-products/paella-catering-business-plan/access?session_id={CHECKOUT_SESSION_ID}`
- Descripción: Business plan kit for a live paella and Spanish catering company: a 10-section Word business plan, 3-year Excel financial projections, a per-guest pricing calculator with paella pan sizing and shopping lists by guest count, and a 68-task startup checklist. One-time payment, lifetime access.
- Env que crearé: `VITE_STRIPE_PAYMENT_LINK_PAELLA_CATERING_BUSINESS_PLAN`

## Después de los links (Claude)

Correos EN de lanzamiento, ya escritos, en la cola de 5 días a las 14:00Z: 24-ene Ice Cream · 29-ene Chocolate · 3-feb Pastry ·
8-feb BBQ · 13-feb Paella (borrador en Resend + routine 30 días antes de cada uno). Detalle del cierre: `SESSION_HANDOFF_2026-10-24-bbq-paella-catering-plans-en.md` §1 (rama del #159).
