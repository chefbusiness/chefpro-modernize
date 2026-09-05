<!-- Copia del plan aprobado por John el 2026-09-05 (sesión Claude Code). Fuente viva durante la ejecución: este fichero. -->

# Plan — «Pagar con cripto» (NOWPayments) como segunda puerta en los 46 productos digitales

Sesión Claude Code · 2026-09-05 · plan técnico, sin ejecutar nada todavía.

## Contexto

Clientes reales de Latinoamérica (GT, PA, MX, AR, UY, VE…) sin acceso a pagos internacionales piden pagar los productos digitales de aichef.pro en cripto (USDT/USDC/BTC/ETH…). John tiene cuenta en NOWPayments con custodia habilitada, API key y servidor MCP (`https://mcp.nowpayments.io/mcp`).

**Lo que se quiere:** Stripe sigue siendo el método principal; al lado, un botón **«Pagar con cripto»** en la landing de cada uno de los **46 productos** (pago único, acceso vitalicio), válido para cualquier país (LATAM, España, EE. UU., Europa), **100 % automatizado**: clic → paga en NOWPayments → recibe por email el mismo enlace de acceso que un comprador de Stripe.

**Decisiones de John fijadas hoy (mandan sobre cualquier idea previa):**
1. **No se mezclan sistemas.** Lo de Stripe vive entero en Stripe; lo de NOWPayments vive entero en NOWPayments (sus facturas, su historial de pagos, sus clientes). Nada de crear facturas en Stripe por ventas cripto. Nuestro código solo abre la puerta (crea la factura por API), recibe la confirmación (IPN) y entrega.
2. **Mismo precio, equivalente en euros, para todos.** La cripto es solo el raíl: la factura de NOWPayments se crea por el precio anunciado en la landing (p. ej. 55 EUR) y el comprador paga su equivalente en la moneda que elija. **Sin lógica de IVA ni de país en el botón.** Retención/conversión/fiscalidad de lo cobrado las gestiona John en el panel de NOWPayments.
3. **Foco:** metodología de implementación y que el botón funcione de punta a punta.

**Doctrina de diseño (ya acordada el 31-ago, sigue vigente):** «crypto es una segunda puerta a la misma habitación — no se duplica la entrega».

## Hechos verificados hoy (solo lectura)

**Repo**
- 46 productos: `PRODUCTS` en `netlify/functions/verify-purchase.ts:13`, 46 URLs en `netlify/shared/payment-links.ts`, 46 páginas `-access`, registro `astro-site/src/lib/zona-app.ts` (46).
- Entrega reutilizable tal cual: `jwt.sign({email, product}, JWT_SECRET, {expiresIn:'365d'})` + `sendAccessEmail(email, token, productId)` (`verify-purchase.ts:426`; Resend, magic link `https://aichef.pro<accessPath>?jwt=…`). Ya lo reutiliza `stripe-webhook.ts:34`.
- Patrón a espejar: `netlify/functions/stripe-webhook.ts` (firma sobre el cuerpo crudo → producto → JWT → email; 200 `ignored` si no hay producto; 500 si falla Resend para que el proveedor reintente; 501 si falta el secreto; el redeploy tras `netlify env:set` **es obligatorio**, build en la nube con `netlify api createSiteBuild`).
- `src/components/shared/ProductAccessGate.tsx:28` acepta `?jwt=` (magic link) → la ruta cripto entra por ahí sin tocar los 46 gates.
- `resend-access.ts:380` busca compras **solo en Stripe** → hay que extenderla para que un comprador cripto pueda autorrecuperar su enlace. `admin/generar-acceso` y `scripts/generate-access-link.mjs` ya sirven para cualquier pasarela.
- **Precio numérico ya existe en las 46 páginas**: `schema.price` (`'55.00'`, `'12.00'`, `'9.00'`, `'89.00'`) en `astro-site/src/data/productos/**/*.ts` (44 fichas) + `pages/mega-pack-tareas.astro:78` + `components/pages/ProPromptsEbookPage.astro:39`. No hay mapa de precios en runtime: hay que generarlo (patrón `sync-payment-links.py`).
- El CTA de Stripe llega como prop `stripeLink` a **5 plantillas** (`GuiaLandingPage.astro` ×10 landings, `KitExcelLandingPage.astro` ×5, `KitTareasLandingPage.astro` ×19, `PlanNegocioLandingPage.astro` ×10, `ProPromptsEbookPage.astro` ×1) + 1 página one-off (`mega-pack-tareas.astro`). Puntos de CTA por plantilla: Hero, BuyBox, CtaFinal y barra sticky.
- Netlify Blobs ya en uso (`log-search.ts`, store `search-queries`, `connectLambda(event)` antes de `getStore`, solo funciona desplegado). `@netlify/blobs ^10.7.13` ya es dependencia.
- No existe política de reembolsos escrita: las 46 landings prometen «30 días · 100 % reembolso · 0 preguntas» (`GuiaLandingPage.astro:546-563` y equivalentes); `faq.astro:84-86` dice que no hay política publicada. El hub `/productos-digitales` es el único sitio que menciona métodos de pago («Pago seguro con Stripe», `ProductosDigitalesHubPage.astro:1000,1507,1610`).
- Línea de productos 100 % en español (sin landings ni emails EN).

**Stripe (leído con el CLI, cuenta `aichefpro`)**: los 46 Payment Links van con Stripe Tax automático, registro fiscal solo ES (régimen pequeño vendedor) y factura automática. 31 precios son `exclusive`, 14 `unspecified` (→ incluido por moneda EUR) y 1 `inclusive`. **Queda fuera de este plan** (decisión 2): se anota como hallazgo aparte por si John quiere armonizarlo en Stripe algún día (`tax_behavior` no se puede cambiar en un precio existente: habría que crear precios y Payment Links nuevos).

**NOWPayments (documentación oficial, SDKs en GitHub, help center)**
- `POST /v1/invoice` (cabecera `x-api-key`): `price_amount`, `price_currency` (EUR admitido), `pay_currency` (opcional: si se omite, el comprador elige en la página alojada), `order_id`, `order_description`, `ipn_callback_url`, `success_url`, `cancel_url`; en ejemplos del help center también `is_fixed_rate`, `is_fee_paid_by_user`, `partially_paid_url`. Devuelve `id` e `invoice_url` (página alojada, con selector de idioma ES/PT). Las invoices **no caducan y no se pueden borrar**; cada pago dentro de una invoice deja de rastrearse a los 7 días.
- IPN: cabecera `x-nowpayments-sig` = **HMAC-SHA512** del JSON con **claves ordenadas recursivamente**, secreto = *IPN secret* del panel. Payload: `payment_id`, `payment_status`, `order_id`, `invoice_id`, `price_amount`, `price_currency`, `pay_currency`, `pay_amount`, `actually_paid`, `outcome_amount`, `outcome_currency`… Si no respondemos 200, reintentan. Pueden llegar **duplicados** (recomiendan idempotencia por `payment_id`) y recomiendan guardar cuerpo + cabeceras 30 días. Reenvío manual desde el panel («Send ipn»).
- Estados: `waiting` → `confirming` → `confirmed` → `sending` → **`finished`** (único que garantiza cobro íntegro) · `partially_paid` (infrapago; no se devuelve) · `failed` · `refunded` · `expired`. Umbral de infrapago configurable en el panel.
- `GET /v1/payment/{id}` solo necesita la API key (el listado `GET /v1/payment` exige además JWT de `/v1/auth`). `GET /v1/min-amount` y `GET /v1/estimate` para mínimos por moneda (dinámicos; un ticket de 9 € puede quedar por debajo del mínimo en BTC on-chain con red cara; USDT-TRC20/BSC confirman en <1 min).
- Sandbox: `https://api-sandbox.nowpayments.io/v1` con cuenta aparte (`account-sandbox.nowpayments.io`), API key e IPN secret propios; simula los estados de un pago.
- MCP oficial (`NowPaymentsIO/nowpayments-mcp`, MIT): `get_full_currencies`, `get_min_amount`, `create_invoice`, `create_payment`, `get_payment_status`. Es herramienta del comerciante/agente; **no sustituye al IPN ni al checkout**.
- No hay motor de IVA ni facturas fiscales con impuestos en NOWPayments: emite su factura/recibo de pago y guarda el historial (con exportación desde el panel). Encaja con la decisión 2.

## Diseño

### Flujo de punta a punta
1. **Landing** (las 46): junto al CTA de Stripe, botón secundario «Pagar con cripto» (USDT · USDC · BTC · ETH…). Al pulsarlo se abre un mini-diálogo con **un solo campo: email** (es lo que necesitamos para entregar) y una casilla de aceptación («pago irreversible; devoluciones se gestionan manualmente»). Sin país, sin importe editable.
2. **`POST /.netlify/functions/crypto-checkout`** `{product, email}` → valida producto contra `PRODUCTS` y contra el mapa de precios generado → crea `orderToken` aleatorio (≥ 16 bytes hex) → guarda el pedido en Blobs (`crypto-orders/<token>`: producto, email normalizado, precio EUR, país por cabecera geo de Netlify solo como dato de soporte, `status: created`, timestamps) → llama a `POST /v1/invoice` con `price_amount` (del mapa, **nunca del cliente**), `price_currency: 'eur'`, `order_id: <token>`, `order_description: <nombre del producto>`, `ipn_callback_url: https://aichef.pro/.netlify/functions/nowpayments-ipn`, `success_url: https://aichef.pro/pago-cripto?o=<token>`, `cancel_url: <landing>#comprar`, `is_fixed_rate`/`is_fee_paid_by_user` desde env → guarda `invoice_id`/`invoice_url` en el pedido → responde `{url}` y el navegador redirige.
3. **Página alojada de NOWPayments**: el comprador elige moneda y paga. NOWPayments registra el pago, su factura y su historial.
4. **`POST /.netlify/functions/nowpayments-ipn`** (espejo de `stripe-webhook.ts`): 501 si falta `NOWPAYMENTS_IPN_SECRET`; 400 sin firma o firma inválida (HMAC-SHA512 sobre el JSON con claves ordenadas recursivamente); guarda SIEMPRE el IPN crudo (`crypto-ipn/<fecha>/<payment_id>-<status>`); carga el pedido por `order_id`; comprueba `price_amount`/`price_currency` contra el pedido; actualiza `status` y `payment_id`. Solo con **`payment_status === 'finished'`** y pedido no entregado → `jwt.sign` + `sendAccessEmail(email, token, productId)` → marca `delivered` (escritura condicional de Blobs para que un IPN duplicado no envíe dos emails; si la condicional no está disponible, se acepta el segundo email idéntico como hace hoy el webhook de Stripe). 200 en todo lo procesado/ignorado; 500 solo si falla Resend (NOWPayments reintenta). `partially_paid`/`expired`/`failed` → solo se anotan.
5. **Página de éxito `/pago-cripto?o=<token>`** (Astro, `noindex`): consulta `GET /.netlify/functions/crypto-order-status?o=<token>` cada pocos segundos. Estados: «esperando confirmaciones de la red — te enviamos el enlace por email en cuanto se confirme» · «pago confirmado: revisa tu email» + botón «Abrir mi acceso» (`<accessPath>?jwt=…`, el token de pedido es secreto del comprador, igual que hoy el `session_id`) · «pago incompleto / caducado: escríbenos» con el email de soporte y el nº de pedido.
6. **Autorrecuperación**: `resend-access.ts` busca primero en Stripe (como hoy) y, si no hay sesión, en el índice de pedidos cripto por email (`crypto-orders-by-email/<email>/<token>`); si hay pedido `delivered` de ese producto → reenvía el magic link. `admin/generar-acceso` y el CLI siguen valiendo tal cual.

### Componentes (nuevo o tocado)
| Pieza | Tipo | Ruta | Reutiliza |
|---|---|---|---|
| Mapa de precios | shared GENERADO | `netlify/shared/product-prices.ts` (`PRODUCT_PRICES: Record<productId, {eur: number}>`) | patrón `payment-links.ts` |
| Generador + gate | script | `scripts/productos-digitales/sync-product-prices.py` (lee `schema.price` de las 44 fichas + los 2 one-off; `--check` = drift y 46 = `PRODUCTS`) | patrón `sync-payment-links.py` |
| Cliente NOWPayments + firma | shared | `netlify/shared/nowpayments.ts` (`createInvoice`, `getPayment`, `verifyIpnSignature(rawBody, sig, secret)`, `sortKeysDeep`) | — (fuera de `functions/` para que el bundler no lo tome por function) |
| Libro de pedidos | shared | `netlify/shared/crypto-orders.ts` (Blobs: `getOrder`, `createOrder`, `markDelivered`, índice por email) | `log-search.ts` (`connectLambda` + `getStore`) |
| Checkout | function | `netlify/functions/crypto-checkout.ts` | `PRODUCTS` de `verify-purchase.ts`, cupo por minuto como `log-search.ts` |
| IPN | function | `netlify/functions/nowpayments-ipn.ts` | `sendAccessEmail`, `PRODUCTS`, contrato de códigos de `stripe-webhook.ts` |
| Estado del pedido | function | `netlify/functions/crypto-order-status.ts` | libro de pedidos |
| Informe admin | function + script | `netlify/functions/crypto-report.ts` (`x-admin-password`, JSON/CSV por mes) + `scripts/productos-digitales/crypto-report.py` | patrón `search-report.ts` / `buscador-report.py` |
| Reenvío | function (edición) | `netlify/functions/resend-access.ts` | libro de pedidos |
| Botón + diálogo | componente Astro | `astro-site/src/components/CryptoPayButton.astro` (`productId`, `landingPath`; JS vanilla, sin island) | estilos de los CTA existentes |
| Inserción en landings | edición | las 5 plantillas de `astro-site/src/components/pages/` + `pages/mega-pack-tareas.astro`, en **BuyBox y CtaFinal** (y Hero si cabe; no en la barra sticky) | prop nueva `cryptoEnabled` |
| Página de éxito | página Astro | `astro-site/src/pages/pago-cripto.astro` (`noindex`, ES) | `BaseLayout` |
| Copy | edición | hub `ProductosDigitalesHubPage.astro` (FAQ métodos de pago + «Pago seguro con Stripe o cripto con NOWPayments»), `terminos.astro` (cláusula pagos cripto), FAQ de garantía | — |
| Gate | script (edición) | `scripts/productos-digitales/gate-flujo-postpago.py` sección E (cripto) | secciones A-D |
| Robots/sitemap | comprobación | `/pago-cripto` no debe caer en ningún patrón de `robots.txt` (gate `robots-gate.py`); `noindex` en la página | — |
| Docs | docs | `PAGOS_CRYPTO_PENDIENTE.md` → `PAGOS_CRYPTO_NOWPAYMENTS.md` (diseño + runbook), `CLAUDE.md` (sección nueva), memoria, checklist de la skill `digital-product-launch` | — |

### Configuración y secretos (repo PÚBLICO: nada en git)
- Env vars en el site **`aichefpro` (`ee5802cf-34bb-4354-90d9-aa9f628b4038`)**, scope `functions`, contexto `production`, marcadas como secreto: `NOWPAYMENTS_API_KEY`, `NOWPAYMENTS_IPN_SECRET`. No secretas: `NOWPAYMENTS_API_BASE` (`https://api.nowpayments.io/v1`; sandbox en contexto `deploy-preview`/`branch-deploy`), `CRYPTO_PRODUCTS` (allowlist del piloto → `all` al replicar; scope `functions` **y** `builds`, porque el checkout la aplica en runtime y las plantillas en build), `CRYPTO_FIXED_RATE` (`0` por defecto: +1 % de coste), `CRYPTO_FEE_PAID_BY_USER` (`0` por defecto: el comprador paga el equivalente exacto en euros). Vacía o ausente = botón apagado en todo el sitio (interruptor de emergencia).
- Las claves van del panel a un fichero `600` y de ahí a `netlify env:set --secret --context production`; **nunca por chat ni logs**. Redeploy en la nube después.
- **MCP en Claude Code**: `.mcp.json` en el repo con `"headers": {"x-api-key": "${NOWPAYMENTS_API_KEY}"}` (sin secreto; expansión de variables verificada en la doc oficial) y la variable exportada en el shell de John; o ámbito `user` (`~/.claude.json`, fuera del repo). Herramientas como `mcp__nowpayments__*`. Ojo: `create_invoice` por MCP con la clave de producción crea facturas reales que **no se pueden borrar** → experimentar con la clave de **sandbox**.
- Panel de NOWPayments (John): generar la **clave IPN** («Genera una clave IPN para notificaciones de pago»), fijar saldo principal / lista blanca cuando quiera (no bloquean el botón), umbral de infrapago, y crear la cuenta **sandbox**.

### Seguridad y casos límite (dentro del diseño, no como aviso)
- Precio solo del mapa generado en servidor; el cliente no manda importe. `order_id` aleatorio, ligado al producto en el libro; el IPN se cruza con el pedido (producto + importe + moneda).
- Entrega solo con `finished`; idempotencia por pedido (+ `payment_id` guardado). IPN crudos guardados ≥ 30 días. Sin firma o firma mala → 400 y nada más.
- Infrapago/expirado: no se entrega; el comprador lo ve en la página de éxito y tiene email de soporte + nº de pedido; John lo resuelve en el panel (reenvío de IPN o entrega manual con `admin/generar-acceso`).
- Mínimos por moneda: en Fase 0 se mide `min-amount` para 9 € y 12 € (USDT-TRC20, USDC, BTC, ETH, LTC, TRX, SOL). Si BTC on-chain queda por encima, se documenta y la página alojada ya se lo dice al comprador.
- Cupo por minuto en `crypto-checkout` (como `log-search`) para que un bucle no cree miles de facturas (no se borran).
- Caída de NOWPayments: el botón responde con «pasarela no disponible, usa tarjeta»; Stripe no se ve afectado.

## Método (John, 2026-09-05): piloto en UN producto → pulir → replicar → nativo

1. Implementar en **un producto** y ver cómo queda.
2. Ver qué mejoras hacen falta (UX del botón y del diálogo, página de éxito, email, panel de NOWPayments).
3. **Pagos de prueba reales** (John y Claude) en ese producto.
4. Cuando esté pulido, **replicar a los 45 restantes**.
5. Dejarlo **nativo**: todo producto nuevo nace con dos botones — **Stripe prioritario, NOWPayments secundario** — sin trabajo extra por producto.

**Cómo se acota el piloto sin código desechable:** el backend es genérico desde el día 1 (functions y mapa de precios cubren los 46). Lo que limita el piloto es un **allowlist** `CRYPTO_PRODUCTS` (env, scope functions y builds): `crypto-checkout` solo acepta los productos listados y las plantillas solo pintan el botón para ellos. Replicar = poner `CRYPTO_PRODUCTS=all` y redeploy. Para lo nativo: el botón vive en las 5 plantillas + mega-pack y el precio sale de `schema.price`, así que un producto nuevo hereda las dos puertas al crear su ficha; el gate (sección E) y el checklist de lanzamiento lo comprueban.

**Producto piloto propuesto:** `kit-tareas-cafeteria` (12 EUR): plantilla mayoritaria (`KitTareasLandingPage.astro`, 19 landings), gate compartido `ProductAccessGate`, ticket bajo para los pagos de prueba. Alternativa aún más barata: `pro-prompts-ebook` (9 EUR), pero usa plantilla y gate propios, así que enseñaría menos sobre la réplica.

## Fases y criterio de cierre

**Fase 0 — Conectar y mirar por dentro (sin código de producción)**
- Conectar el MCP (`.mcp.json` + variable) y, con la cuenta **sandbox**, listar monedas, mínimos para 9/12/55 €, crear una invoice de prueba y ver la página alojada (¿pide email por sí misma? ¿qué campos?), lanzar el flujo simulado y **capturar un IPN real** (payload completo y firma) contra un endpoint de prueba (branch deploy en la nube). Confirmar longitud máxima de `order_id`, `partially_paid_url`, `is_fee_paid_by_user`.
- Cierre: tabla de hechos LIVE (mínimos, campos del IPN, comportamiento de la página) anotada en `PAGOS_CRYPTO_NOWPAYMENTS.md`. Si la página alojada recoge el email de forma fiable y llega en el IPN, se simplifica el diálogo de la landing (queda solo la casilla de aceptación).

**Fase 1 — Backend genérico + piloto en sandbox (branch deploy en la nube)**
- `sync-product-prices.py` + `product-prices.ts` (46/46, `--check` verde) · `nowpayments.ts` (firma probada con el IPN capturado en Fase 0 y con un test local tipo `pv-test.cjs`: esbuild + node, 0 builds de Astro) · `crypto-orders.ts` · `crypto-checkout.ts` (respeta `CRYPTO_PRODUCTS`) · `nowpayments-ipn.ts` · `crypto-order-status.ts` · `crypto-report.ts` · extensión de `resend-access.ts` · sección E del gate.
- Frontend del piloto: `CryptoPayButton.astro` insertado en `KitTareasLandingPage.astro` (BuyBox y CtaFinal) y `pago-cripto.astro`; `CRYPTO_PRODUCTS=kit-tareas-cafeteria`.
- Cierre: en el branch deploy con claves sandbox: la landing del piloto pinta el botón y las otras 45 no; checkout crea invoice → IPN sandbox `finished` → email de acceso recibido → magic link abre el dashboard; IPN sin firma → 400; producto fuera del allowlist → 403; duplicado → un solo email; `gate-flujo-postpago.py` verde (A-E).

**Fase 2 — Piloto en producción: ver cómo queda, pulir, pagos reales**
- Claves reales en `production` (secretas) + `CRYPTO_PRODUCTS=kit-tareas-cafeteria` → deploy en la nube → gate LIVE → **pagos de prueba reales** (John con su wallet; Claude verifica el rastro: pedido en Blobs, IPN, email, panel de NOWPayments) en USDT-TRC20 y en una segunda moneda (BTC o ETH) para ver tiempos de confirmación y la página de éxito en cada estado.
- Revisión conjunta: botón y diálogo en móvil y escritorio (WhatsApp flotante y banner de cookies no lo tapan), textos, email, factura/historial en el panel de NOWPayments, runbook de soporte («no me llegó el enlace»: nº de pedido → panel → «Send ipn» o `admin/generar-acceso`). Lista de mejoras → se aplican → segunda ronda de pagos si hace falta.
- Cierre: John da el «pulido» al piloto por escrito (handoff) y auditoría adversarial (opus) del diff antes de replicar.

**Fase 3 — Réplica a los 46 y nativo para los nuevos**
- Botón en las otras 4 plantillas + `mega-pack-tareas.astro`; copy del hub (FAQ métodos de pago, «Pago seguro con Stripe o cripto con NOWPayments»), `terminos.astro` (cláusula pagos cripto), garantía; `CRYPTO_PRODUCTS=all`.
- Nativo: `schema.price` como fuente del precio queda documentado como campo obligatorio de toda ficha; sección E del gate exige 46/46 (y N/N al crecer) en el mapa y el botón en cada landing del `dist`; checklist de la skill `digital-product-launch` y `CLAUDE.md` con la regla «todo producto nace con dos botones: Stripe prioritario, NOWPayments secundario».
- Cierre: en el `dist` de producción 46/46 landings con el botón (grep), 0 en la zona app, `whatsapp-gate.py`, `robots-gate.py` y `gate-flujo-postpago.py` verdes; `crypto-report.py --days 7` con los pagos del piloto; docs (`PAGOS_CRYPTO_NOWPAYMENTS.md`), memoria y handoff; commit + push con firma `Via: Claude Code`.

## Verificación (además de los cierres de fase)
- Test unitario de la firma IPN con el payload capturado (positivo, negativo, claves anidadas desordenadas).
- `curl` contra las 4 functions en el branch deploy (contratos 400/405/501/200), como hoy con el webhook de Stripe.
- Auditoría adversarial (opus) del diff antes de pasar a producción: manipulación de precio, replay de IPN, `order_id` forjado, entrega antes de `finished`, secretos en el repo, builds locales (prohibidos).
- Vigilancia la primera semana: informe `crypto-report.py --days 7` y logs de Netlify `[nowpayments-ipn]`.

## Fuera de alcance (explícito)
- Retención/conversión/retiradas de la cripto cobrada, fiscalidad de las tenencias, modelo 721, off-ramp: John, en el panel de NOWPayments y con su gestor.
- Cualquier cambio en Stripe (precios, `tax_behavior`, Payment Links): hallazgo anotado, no tarea.
- Versión EN de landings/emails (la línea es ES; cuando llegue el inglés nativo el botón hereda).
- Suscripciones del SaaS (Pickaxe/Stripe) y consultoría: siguen como están.

## Nota de método
Hay un workflow de diseño + refutación adversarial (2 diseños opus, 3 refutadores) todavía en curso sobre esta misma base de hechos; sus objeciones se incorporan **antes de escribir la primera línea de la Fase 1** (los hallazgos bloqueantes se revisan con John).

## Pendiente de confirmar en Fase 0 (no bloquea el plan)
- Si la página alojada de las invoices creadas por API puede exigir el email y si ese email viaja en el IPN.
- Longitud máxima de `order_id`; soporte real de `partially_paid_url`, `is_fee_paid_by_user`, `is_fixed_rate` en `/v1/invoice`.
- Que el sandbox envía IPN (indicios de terceros, sin confirmación oficial).
- Escritura condicional en `@netlify/blobs` v10 (`onlyIfNew`/`onlyIfMatch`) para la idempotencia estricta.
- Política de devoluciones cripto (John): mantener la garantía de 30 días con devolución manual desde Custody a la wallet del cliente, o excluir cripto de la garantía. El copy de la casilla de aceptación depende de esto.

## Anexo — Mejoras incorporadas tras el workflow de diseño (2 diseños opus, 2026-09-05)
- **`order_id` firmado**: `<productId>.<aleatorio>.<hmac-sha256 truncado>` con `NOWPAYMENTS_ORDER_SECRET` (distinto de `JWT_SECRET`). Un IPN con `order_id` que no lleve nuestra firma (p. ej. una factura creada a mano en el panel) → `200 {ignored:'foreign_order'}` + log. Longitud a confirmar contra el límite de NOWPayments en Fase 0.
- **Reconfirmación fuera de banda**: antes de entregar, `GET /v1/payment/{payment_id}` con la API key debe devolver también `finished` y el mismo `price_amount`/`price_currency`. Defensa en profundidad frente a un IPN firmado con un secreto filtrado.
- **Orden de puertas del IPN**: 405 → 501 (sin secreto) → 400 (sin firma / firma inválida, `timingSafeEqual`) → idempotencia (`delivered`) → firma del `order_id` → pedido en el libro → estado → importe → reconfirmación → entrega → marcar `delivered` (escritura condicional `onlyIfMatch` de Blobs, verificada en la doc de Netlify).
- **Textos legales**: `terminos.astro` y `legales.astro` son wrappers GENERADOS (`fase6-generate-marketing.py`) sobre islands de la SPA; el copy vive en `src/i18n/locales/es.json` (`pages.terms.content_paragraphs`). La cláusula de pagos cripto se añade ahí (ES; decidir si se replica en los otros 6 locales).
- **Firma IPN (SDK oficial `nowpayments-sdk-nodejs/src/ipn.js`)**: `createHmac('sha512', secret.trim()).update(JSON.stringify(sortObjectDeep(payload))).digest('hex')`, comparación `timingSafeEqual` sobre buffers hex de igual longitud. `sortObjectDeep` ordena claves recursivamente y respeta arrays.
- **Cuerpo de `POST /v1/invoice` (SDK oficial `client.js`)**: `price_amount, price_currency, pay_currency, payout_currency, ipn_callback_url, order_id, order_description, success_url, cancel_url, partially_paid_url, is_fixed_rate, is_fee_paid_by_user`. **No hay `customer_email` en la invoice** (solo en `/v1/invoice-payment`): el email lo captura nuestro diálogo.
- Descartado: leer el precio en vivo del Payment Link de Stripe (un diseño lo proponía) — viola «sistemas separados»; el precio sale de `schema.price`.
- Descartado por ahora: unificar el acuñado de JWT de las 4 functions en un `access-grant.ts` compartido — toca la ruta de Stripe que hoy funciona; se valora después del piloto.

---

# Especificación de implementación v1 (piloto) — consolidada tras 3 refutaciones adversariales (2026-09-05)

Fuente de contrato de la API: colección Postman oficial (JSON accesible en
`https://documenter.gw.postman.com/api/collections/7907941/2s93JusNJt?segregateAuth=true&versionTag=latest`).
Copia local de la sesión en el scratchpad (`nowpayments-postman.json`, `nowpayments-endpoints.json`).

## Correcciones que mandan sobre el plan aprobado
1. **Firma IPN = HMAC-SHA512 sobre `JSON.stringify(sortObjectDeep(JSON.parse(body)))`**, secreto `trim()`, comparación `timingSafeEqual` de buffers hex de igual longitud. NO es «sobre el cuerpo crudo» (eso es Stripe). El cuerpo se lee respetando `event.isBase64Encoded`. `sortObjectDeep` = el `sortObject` oficial (recursivo, respeta arrays). La prosa oficial `JSON.stringify(params, Object.keys(params).sort())` es INCORRECTA (replacer): no usarla.
2. **Infrapago**: `price_amount` del IPN es el que pusimos nosotros y no detecta nada. Antes de entregar se **reconfirma con `GET /v1/payment/{payment_id}`** (misma API key que creó la factura) y se exige: `payment_status === 'finished'`, `price_currency === 'eur'`, `Number(price_amount) === order.priceEur`, y `actually_paid / pay_amount >= CRYPTO_MIN_PAID_RATIO` (env, default `0.95`; NOWPayments ya aplica su propio umbral configurable en el panel para marcar `finished`). Si no cuadra → `200 {ignored:'underpaid'}` + marca en el libro + huérfano para John.
3. **`order_id` corto y opaco** (32 hex de `crypto.randomBytes(16)`), sin productId ni HMAC dentro. El libro (Blobs) es la única verdad: producto, importe y email salen del registro. Sin `NOWPAYMENTS_ORDER_SECRET`.
4. **Libro con consistencia fuerte**: `getStore({ name:'crypto-orders', consistency:'strong' })` en TODAS las lecturas (aquí una lectura obsoleta cuesta una venta; en `log-search` no).
5. **Pedido no encontrado**: si el `created_at` del pago tiene menos de 24 h → `500 {error:'order_not_found_retry'}` (NOWPayments reintenta); si es más antiguo → `200 {ignored:'unknown_order'}`. En ambos casos se guarda el huérfano (`orphans/<payment_id>`).
6. **Invoice reutilizable**: si el pedido ya está `delivered` y llega un `finished` con OTRO `payment_id` → `200 {ignored:'order_already_fulfilled'}` + huérfano (alguien pagó dos veces la misma factura: John lo resuelve a mano). Si el pedido NO está entregado y llega otro `payment_id` (el primero expiró) → se actualiza `paymentId` y sigue el flujo normal.
7. **Idempotencia estricta con escritura condicional** (`onlyIfMatch` sobre el etag, verificado en la doc de Netlify Blobs): lock de entrega → email → `delivered:true`. Si el lock no se consigue (concurrente) → `500` para que reintente más tarde. Si el email falla → se libera el lock y `500`.
8. **Guardas de entorno en el IPN** como en `stripe-webhook.ts:56-59`: sin `JWT_SECRET` o `RESEND_API_KEY` → `500 misconfigured` (porque `sendAccessEmail` retorna EN SILENCIO si falta `RESEND_API_KEY`, `verify-purchase.ts:427`).
9. **Sin IPN al expirar** (doc oficial: «no callbacks are sent after a payment expires»): el estado se refresca por consulta (`crypto-order-status` consulta la API si el pedido lleva `paymentId` y >10 min sin IPN; `crypto-report` marca estancados). Un pedido `created` sin `paymentId` es un abandono (el comprador no eligió moneda): no hay nada que consultar.
10. **Timeout** de la llamada a NOWPayments: **5 s**, cero reintentos (crear factura no es idempotente). Presupuesto de la function: 10 s.
11. **Diálogo del botón** pide: email (obligatorio), **país de facturación** (select obligatorio; no cambia el precio: es evidencia para el IVA junto con el país de la cabecera geo de Netlify), y **dos casillas separadas**: (a) «He leído y acepto las condiciones de compra y devoluciones» y (b) «Solicito el acceso inmediato al contenido digital y entiendo que, al recibirlo, pierdo el derecho de desistimiento de 14 días». Los tres timestamps van al libro. El email de acceso lleva una línea recordando (b) para compras cripto (parámetro opcional `extraHtml` de `sendAccessEmail`, sin cambiar el comportamiento de Stripe).
12. **Endpoint de checkout**: cupo global por minuto (patrón `log-search.ts`), comprobación de `Origin` (aichef.pro, www, `*.netlify.app`), y ningún campo de importe aceptado del cliente.
13. **Admin**: `crypto-report` usa el patrón FUERTE de `search-report.ts` (cabecera `x-admin-password`, comparación timing-safe, cupo de intentos), no el de `admin-generate-access`. Purga de pedidos `created`/`expired` con más de 30 días.
14. **`resend-access`**: consulta el índice cripto por email **al principio** (antes de Stripe y sin depender de `PURCHASE_VALIDATION`).
15. **Sitemap**: excluir `/pago-cripto` en el filtro de `astro-site/astro.config.mjs` (además del `noindex`).
16. **Fees vigentes** (help center y pricing oficial): **1 %** sin conversión; **1,5 %** con conversión multi-moneda, con `is_fixed_rate` o con `is_fee_paid_by_user`. Defaults: `CRYPTO_FIXED_RATE=0` (la tasa fija caduca a los 10 min → `expired`, sin callback), `CRYPTO_FEE_PAID_BY_USER=0`.
17. **Sandbox deprecado** (doc oficial: «Since 2025, the Sandbox environment is no longer actively maintained or kept in sync with Production»): se usa solo para ver la FORMA de un IPN y probar la firma; la validación real son pagos reales de importe mínimo en el piloto.
18. **MCP oficial descartado en este proyecto**: sus 5 herramientas exigen `api_key` como ARGUMENTO en cada llamada (comprobado con `tools/list` contra el endpoint), así que la clave acabaría en la conversación y en los logs. La exploración se hace con `curl` leyendo la clave de un fichero `600`; el backend la lee de la env var de Netlify.
19. **Estados oficiales (9)**: `waiting, confirming, confirmed, sending, partially_paid, finished, failed, refunded, expired`. Cualquier otro valor se registra como desconocido (sin romper).
20. **Sin branch deploys** en el site (`allowed_branches: ["main"]`): la prueba en la nube va por **deploy preview de una PR**; las env `NOWPAYMENTS_*` del contexto `deploy-preview` apuntan a la cuenta que John decida (sandbox para forma de IPN; producción para el piloto real desde `main`).

## Libro de pedidos (Netlify Blobs, store `crypto-orders`, consistencia fuerte)
| Clave | Contenido |
|---|---|
| `orders/<orderId>` | `{orderId, productId, email, emailNorm, priceEur, currency:'eur', country, geoCountry, acceptedPolicyAt, waivedWithdrawalAt, createdAt, status, invoiceId, invoiceUrl, paymentId, payCurrency, payAmount, actuallyPaid, outcomeAmount, outcomeCurrency, lastIpnAt, ipnCount, delivered, deliveredAt, deliveryLockAt, flags:[]}` |
| `email/<sha256(emailNorm)>/<orderId>` | índice para `resend-access` y soporte |
| `day/<YYYY-MM-DD>/<orderId>` | índice para el informe |
| `ipn/<YYYY-MM-DD>/<paymentId>-<status>-<ts>` | IPN crudo + cabeceras (≥ 30 días) |
| `orphans/<paymentId>` | pagos sin pedido, infrapagados o segundos pagos de una factura ya servida |
| `rl/<YYYY-MM-DDTHH:mm>` | contador del cupo por minuto del checkout |

## Contratos HTTP
- `POST /.netlify/functions/crypto-checkout` `{product, email, country, acceptPolicy:true, waiveWithdrawal:true}` → `200 {url, orderId}` · `400 invalid_request|unknown_product|invalid_email|invalid_country|consent_required` · `403 origin_not_allowed|product_not_enabled` · `405` · `429 rate_limited` · `501 crypto_not_configured` (sin API key) · `503 crypto_disabled` (`CRYPTO_PRODUCTS` vacío) | `503 gateway_unavailable` (NOWPayments no responde/5xx).
- `POST /.netlify/functions/nowpayments-ipn` → `405` · `501 webhook_not_configured` · `500 misconfigured` · `400 missing_signature|invalid_signature|invalid_json` · `200 {ignored:<motivo>}` · `500 {error:'order_not_found_retry'|'delivery_in_progress'|'email_failed'}` · `200 {sent:true}`.
- `GET /.netlify/functions/crypto-order-status?o=<orderId>` → `200 {orderId, status, productId, productLabel, emailMasked, delivered, accessUrl?}` · `400` · `404` · `405`.
- `GET /.netlify/functions/crypto-report?days=30[&format=csv][&purge_unpaid_before=YYYY-MM-DD]` con `x-admin-password` → JSON/CSV; `401`; `429`.

## Env vars (site `aichefpro`, `ee5802cf-…`)
Secretas, scope `functions`: `NOWPAYMENTS_API_KEY`, `NOWPAYMENTS_IPN_SECRET`. No secretas: `NOWPAYMENTS_API_BASE` (default `https://api.nowpayments.io/v1`), `CRYPTO_PRODUCTS` (scope `functions` **y** `builds`; vacío = apagado; `all` = todos; o CSV de productIds), `CRYPTO_MIN_PAID_RATIO` (`0.95`), `CRYPTO_FIXED_RATE` (`0`), `CRYPTO_FEE_PAID_BY_USER` (`0`), `CRYPTO_SITE_URL` (default `https://aichef.pro`; en deploy preview, la URL del preview para `success_url`/`ipn_callback_url`). Ya existen en todos los contextos: `JWT_SECRET`, `RESEND_API_KEY`, `ADMIN_PASSWORD`.
