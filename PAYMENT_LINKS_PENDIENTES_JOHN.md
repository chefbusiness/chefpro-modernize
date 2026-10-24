# Payment Links pendientes — tareas de John (Stripe)

> Sesión Claude Code (Mac), abierto el **24-oct-2026**. John (24-oct): «cuando tengas cinco productos terminados y yo
> esté de vuelta en el ordenador, hacemos la configuración en Stripe para crear los payment links. De momento apárcalos
> como tareas para mí y continúa tú con los siguientes productos».
>
> Cada producto de esta lista está **terminado y en un PR en borrador**: solo le falta su Payment Link. Los PR van
> **apilados** (cada rama sale de la anterior), así que se fusionan en orden, de arriba abajo.

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
| 2 | Chocolate Shop Checklists Kit Pro | $19 | (en curso) | 🔨 F1 |
| 3 | Pastry Shop Checklists Kit Pro | $19 | (en curso) | 🔨 F1 |
| 4 | BBQ Catering Business Plan Kit | $39 | — | ⏳ en cola |
| 5 | Paella Catering Business Plan Kit | $39 | — | ⏳ en cola |

### 1. Ice Cream Shop Checklists Kit Pro — $19.00 USD (PR #156)

- Nombre en Stripe: **Ice Cream Shop Checklists Kit Pro**
- Redirección: `https://aichef.pro/en/digital-products/ice-cream-shop-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}`
- Descripción: Nine Excel checklist templates and three bonuses for ice cream shops: opening and closing, pasteurizing and batch freezing, manager and role duties, cleaning and maintenance, peak season and ice cream catering, cash drawer. One-time payment, lifetime access.
- Env que crearé: `VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_CHECKLISTS_KIT`
- Ojo: este PR lleva también el parche de seguridad del kit ES de heladería (grasas y yemas antes de pasteurizar).
