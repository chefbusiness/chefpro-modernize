# Handoff 25-sep-2026 (sesión Claude Code) — Food Cost Kit Pro LIVE, primer producto de la tienda EN

## Estado: EN PRODUCCIÓN (PR #100, merge `bc7e3fc2`, 25-sep ~02:00)
- Landing: https://aichef.pro/en/digital-products/food-cost-templates · acceso `/access` · dashboard `/library`
- Hub EN con la tarjeta enlazada a $19: https://aichef.pro/en/digital-products
- $19 USD · Payment Link en `VITE_STRIPE_PAYMENT_LINK_FOOD_COST_KIT` · NOWPayments con `/en/crypto-payment`
- Réplica del Kit de Escandallos Pro v2.1: 14 xlsx + PDF en `astro-site/public/dl/food-cost-templates/`
- Gates LIVE: `gate-flujo-postpago.py --only food-cost-templates` → 15/15/15, 200/200/200, 0 fallos;
  `tienda-gate.py --base https://aichef.pro` verde; `--es-identico` (preview): 4 landings ES idénticas
  byte a byte, `/kit-escandallos` solo cambia en el hreflang.

## Qué pasó en la sesión
- El Mac se apagó por batería (24-sep 23:25) a mitad de la F3. El worktree de `/private/tmp` se perdió;
  se reconstruyó reproduciendo las operaciones de los agentes desde sus transcripts y se verificó contra
  lo que otro agente había leído antes del apagón (15/15 ficheros idénticos). Método en la memoria
  `feedback_commitear-wip-de-subagentes-y-recuperar-desde-transcripts`.
- John paró el gasto: «te estás consumiendo toda la suscripción en un producto de 19 USD». Workflow de
  auditoría cortado; el resto se cerró con gates de script y arreglos pequeños en el hilo principal.
  Regla guardada en `feedback_politica-3-fases-y-presupuesto-proporcional`.
- Decisiones de John (25-sep): la landing EN replica TODAS las secciones del ES — la de compatibilidad
  (Excel, Google Sheets, LibreOffice Calc, Apple Numbers, WPS Office; también en FAQ y dashboard) y los
  10 testimonios traducidos tal cual (subtítulo: son de la edición española). La tienda es UNA, en España.
  `TIENDA-INTERNACIONAL.md` §3.5 revisado.

## Pendiente (próxima sesión)
1. **Correo de lanzamiento del Food Cost Kit Pro** en Resend (regla: un broadcast por producto nuevo,
   cola de 5 días; segmento EN). Plantilla de lanzamiento + `resend-broadcast.py --test` a John antes.
2. GSC: pedir indexación de la landing EN (y comprobar que no cae en ningún Disallow: `robots-gate.py`).
3. Siguiente producto de la ola EN según `TIENDA-INTERNACIONAL.md` (inventario), con presupuesto S:
   un implementador + gates de script, sin fan-out de auditoría.

## Sesión Claude Code (25-sep, tarde) — correo de lanzamiento EN programado + GSC
- **Broadcast programado:** `d3bd1f9c-3bb5-44ad-9d1b-5e8a165a24a9` · «Lanzamiento Food Cost Kit Pro + tienda EN (EN)» ·
  asunto «Our digital store is now in English — first up: Food Cost Kit Pro» · segmento «AI Chef Pro EN» (`d06ed053-…`) ·
  from `hello@news.aichef.pro` · **lunes 28-sep-2026 14:00 UTC** (10:00 NY, 15:00 Londres). Prueba a John: `01a0d866-…`.
  HTML: `scripts/productos-digitales/emails/broadcast-food-cost-templates-lanzamiento-en.html`.
- **Decisión (delegada por John): un solo correo** = presentación de la tienda EN + primer producto. Con 1 de 50 productos
  comprables en inglés, un correo previo de «tienda» llevaba a un escaparate casi entero en «Coming soon». Cierra con los tres
  siguientes de la ola 1 (Inventory, Pro Prompts, HACCP) y pide respuesta: «¿cuál necesitas primero?» (Reply-To info@aichef.pro)
  → las respuestas sirven para ordenar la ola.
- **Cola EN independiente de la ES** (decisión de esta sesión): el segmento EN no recibe los correos ES, así que su hueco se mide
  contra el último envío AL SEGMENTO EN (+5 días) y sin coincidir el mismo día con un correo de producto ES. Hora EN 14:00 UTC.
  Los «Growth» los manda Grokbot (agente independiente de John): no cuentan ni se coordinan.
- Revisión adversarial (2 sonnet, 269 k tokens): 1 hallazgo real (el hub NO distingue qué productos vienen primero: todos
  llevan el mismo «Coming soon in English») → frase quitada. Copy/reglas/render: sin hallazgos.
- **Gotcha:** `resend-broadcast.py` abortó dos veces con «no vivo» en URLs que dan 200: son las ráfagas de la IP del Mac
  contra Netlify (URL con UTM nueva = miss de caché de 3-5 s + 5xx intermitentes). Arreglado ese mismo día: `vivo()` reintenta 3 veces con 8 s de espera (un 404 es definitivo).
- **GSC:** hub `/en/digital-products` indexado (rastreado 24-sep). Landing `/en/digital-products/food-cost-templates`
  «URL is unknown to Google»; en `sitemap-0.xml` y rastreable (robots OK; `/access` y `/library` bloqueados, correcto).
  Sitemap reenviado por API. **Pedir indexación = clic de John en el panel** (la API no lo permite).
- Pendiente de John: **D53** (¿Kit Chocolatería 2.1 delante? → Chocolatería 24-oct o 29-oct); el correo de la Chocolatería
  está escrito y en ventana desde el 24-sep. Taquería 29-oct programable desde el 29-sep; Escandallos 2.1 3-nov desde el 4-oct.
