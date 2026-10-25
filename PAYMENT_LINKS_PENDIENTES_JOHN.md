# Payment Links pendientes — tareas de John (Stripe)

> Sesión Claude Code (Mac). **No hay ninguno pendiente.**

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
