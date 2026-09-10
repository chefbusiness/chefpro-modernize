# Handoff — Guía «Cómo Montar una Pastelería» (producto nuevo nº 4) · sesión Claude Code 2026-09-09/10 (Mac)

> ⏳ EN CONSTRUCCIÓN (se completa al cerrar la sesión). John se fue a dormir a las 02:35 con la orden «avanza con todo
> hasta completar el producto y déjame los datos de Stripe»; vuelve a las 6:45-7:00.

## 0. Lo que John tiene que hacer por la mañana (5 minutos)

1. **Crear el producto y el Payment Link en Stripe** con estos datos:

| Campo | Valor |
|---|---|
| Nombre del producto | **Cómo Montar una Pastelería** |
| Precio | **65,00 €** · pago único · `tax_behavior: exclusive` · `automatic_tax: on` · `tax_code: txcd_10000000` (Digital products / general) · `invoice_creation: on` |
| Descripción (prosa, ~260 caracteres, sin viñetas, sin «BOE») | Para quien va a abrir una pastelería en España: 20 capítulos en PDF y DOCX editable, 8 herramientas Excel con fórmulas vivas —capacidad de obrador, CAPEX, campañas, escandallo, licencias y personal—, un business plan modelo relleno y 12 decisiones de apertura resueltas. Pago único, acceso de por vida. |
| Imagen del producto (opcional) | `https://aichef.pro/og-guia-pasteleria-obrador.jpg` (estará en producción tras el push) |
| Redirección tras el pago | `https://aichef.pro/guia-pasteleria-obrador-access?session_id={CHECKOUT_SESSION_ID}` |
| Recoger email | sí (lo usa `verify-purchase` para el magic link) |

2. Pegar la URL `https://buy.stripe.com/…` aquí en el chat. Claude hace el resto: env var `VITE_STRIPE_PAYMENT_LINK_GUIA_PASTELERIA_OBRADOR` en Netlify (scope builds, todos los contextos), `sync-payment-links.py`, push, deploy, gates LIVE, cripto (`CRYPTO_PRODUCTS`), y el borrador del correo de lanzamiento (slot 14-oct).
3. **Compra de prueba real** cuando esté LIVE (o `aichef.pro/admin/generar-acceso`).

*(El resto del handoff se escribe al cerrar la sesión.)*

Via: Claude Code
