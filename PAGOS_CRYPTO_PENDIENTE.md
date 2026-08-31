# Pasarela de pago CRYPTO alternativa a Stripe — idea pendiente

> Idea de John, **2026-08-31**. Registrada para no perderla. **No está decidida ni empezada.**

## Por qué

Clientes de **Latinoamérica** piden pagar los productos digitales en **USDC, Bitcoin o SATS**. John: «no es un volumen muy importante, pero sí tengo gente que me lo está pidiendo». Encaja con lo ya medido: hay compras reales desde GT/PA/MX/AR/UY, y en varios de esos países la tarjeta internacional tiene fricción real (bloqueos, control de cambios, recargos).

La idea es **Stripe por defecto + una pasarela crypto ALTERNATIVA**. No sustituir nada.

## Estado de las opciones (mirado el 2026-08-31)

| Opción | Veredicto | Detalle |
|---|---|---|
| **Coinbase** | ❌ descartada | John: «ya no está disponible en España». Es su comprobación; re-confirmar si algún día se retoma |
| **NOWPayments** · `nowpayments.io/es` | ✅ candidata | Custodial. Comisión **desde 1 %** con descuentos por fidelidad. 350+ criptos. **Auto-conversión cripto↔fiat.** API + facturas + plugins. **No exige KYC al comprador** salvo que AML marque la operación |
| **BTCPay Server** · `btcpayserver.org` | ⚠️ no cubre la petición | Self-hosted, open source, **0 % de comisión**, webhooks, enlaces de pago, 30+ plugins. Pero **sólo Bitcoin y Lightning: NO hace USDC** — que es justo lo que piden. Serviría para el subconjunto BTC/SATS a coste cero, a cambio de mantener un servidor |

⚠️ **A verificar antes de comprometerse con NOWPayments:** su web **no confirma** retirada **SEPA en EUR** ni fijar el precio en EUR. Son las dos cosas que hacen falta aquí (44 productos con precio en euros).

## Lo que hace que esto sea barato

**La capa de entrega ya es agnóstica del medio de pago.** `verify-purchase.ts` acuña el JWT de 365 días y `sendAccessEmail()` manda el enlace; el `stripe-webhook.ts` activado el 31-ago no hace nada más que eso.

Una pasarela crypto necesita **sólo tres piezas**:

1. Crear la factura del producto (precio en EUR).
2. Recibir el **IPN** de confirmación (equivalente al webhook de Stripe).
3. Resolver `productId` y llamar **al MISMO `sendAccessEmail`**.

> **Regla de diseño: crypto es una segunda puerta a la misma habitación.** No se duplica la entrega, ni el JWT, ni el email, ni el dashboard. Si se duplican, hay dos cosas que mantener sincronizadas — y ya sabemos lo que cuesta (el mapa de 44 Payment Links).

Necesita además su **mapa factura→producto con gate de drift**, igual que `sync-payment-links.py --check`, o reaparece el `ignored: unknown_product` que deja al comprador sin email.

## Decisiones de John, no técnicas

1. **¿Sólo stablecoin, o también BTC?** Recomendación: **empezar por USDC/USDT solo**. Elimina el riesgo de volatilidad entre factura y liquidación, y es lo que la gente de LATAM tiene de verdad. BTC/SATS después, cuando el flujo esté rodado.
2. **¿Se retiene la cripto o se convierte a EUR?** Es la decisión práctica más gorda: define el off-ramp y dónde aterriza el dinero.
3. **Fiscalidad (España).** Cobro en cripto = ingreso por su valor en EUR el día del cobro; si se retiene y se revaloriza, hay además ganancia patrimonial; y modelo 721 por encima de umbrales. **Esto lo tiene que ver su gestor**, no se decide aquí.
4. **Devoluciones.** Las criptos son irreversibles: hace falta política escrita antes de encender nada.

## A favor, y no es menor

**Cero chargebacks.** Para producto digital eso pesa, sobre todo con la disputa de 650 € abierta.

## Encaje con el ritmo

No es una v2.0 ni un producto nuevo: es **infraestructura**. Hay que decidir si desplaza una sesión de la alternancia o va aparte.

Via: Claude Code
