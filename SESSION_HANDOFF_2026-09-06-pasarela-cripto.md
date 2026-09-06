# Handoff — Pasarela cripto NOWPayments (sesión Claude Code, 5→6 sep 2026)

**Qué hay:** el piloto «Pagar con cripto» está **EN PRODUCCIÓN** en `https://aichef.pro/kit-tareas-cafeteria` (PR #78 fusionada a la 01:06; claves `NOWPAYMENTS_API_KEY` e `NOWPAYMENTS_IPN_SECRET` en `production`, comprobadas por contrato HTTP). Diseño, decisiones de John, especificación v1, registro de medidas y las **decisiones de UX literales de John** están en `PAGOS_CRYPTO_NOWPAYMENTS.md` (leerlo entero antes de tocar nada). Memoria: `project_nowpayments-pasarela-cripto-plan-2026-09-05`.

**Decisiones de John que mandan:** sistemas separados (nada de facturas en Stripe por ventas cripto); mismo precio en EUR para todos los países (sin lógica de IVA en el botón); piloto en un producto → pulir → replicar a 46 → nativo (Stripe prioritario, NOWPayments secundario); el MCP oficial no se usa con la clave de producción (exige `api_key` como argumento). UX: recuadro cripto **hermano** del de Stripe, azul pastel NOWPayments, botón de pago genuino (no CTA con texto largo), sello con iconos de monedas, y las dos puertas en los tres puntos de compra.

**Rediseño UX EN PRODUCCIÓN desde las 03:12** (PR #79 + `ad5bce5` + `a989f39`): hero integrado, BuyBox con dos tarjetas, botón «PAGAR CON CRIPTO — €12», un diálogo por página, 22 hallazgos de la revisión adversarial aplicados. **Réplica al resto de productos EN ESPERA** por decisión de John («probamos primero el pago»): diff preparado y sin aplicar en el worktree `.claude/worktrees/agent-a0b26e4cbb20410c2` (detalle y trampa del hero en `PAGOS_CRYPTO_NOWPAYMENTS.md` → «Estado 6-sep 03:20»).

**Bloqueado por John:** el pago real de prueba de 12 € (necesita cargar una wallet) y la decisión sobre el eBook de 9 € (por debajo del mínimo de NOWPayments) y la moneda de liquidación.

**Cómo se verifica (nunca en local):** `python3 scripts/productos-digitales/gate-flujo-postpago.py` (sección E), `node --experimental-strip-types scripts/productos-digitales/tests/nowpayments-sig.test.ts` (42/42), curl contra producción o el preview (contratos en el doc), logs con `netlify logs --url https://<deploy_id>--aichefpro.netlify.app --source functions --function <nombre> --since 30m`.

**Térmica:** esta noche el Mac se apagó DOS veces (kernel panics 01:38 y 01:48). Tras un panic, Spotlight reindexa 10-15 min y sube solo la CPU: leer `istats cpu temp` antes de cada paso, arrancar `scripts/termica/watchdog-termico.sh` en background, un solo agente a la vez, cero builds locales, y commit + push de docs pronto.

Sesión Claude Code · firma de commits `Via: Claude Code`.
