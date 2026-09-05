# Handoff — Pasarela cripto NOWPayments (sesión Claude Code, 5→6 sep 2026)

**Qué hay:** el piloto «Pagar con cripto» está implementado en la rama `feat/pago-cripto-piloto` (PR #78) y verificado en su deploy preview hasta la creación de una factura real. Diseño, decisiones de John, especificación v1 y registro de medidas: `PAGOS_CRYPTO_NOWPAYMENTS.md` (leerlo entero antes de tocar nada). Memoria: `project_nowpayments-pasarela-cripto-plan-2026-09-05`.

**Decisiones de John que mandan:** sistemas separados (nada de facturas en Stripe por ventas cripto); mismo precio en EUR para todos los países (sin lógica de IVA en el botón); piloto en un producto → pulir → replicar a 46 → nativo (Stripe prioritario, NOWPayments secundario); el MCP oficial no se usa con la clave de producción (exige `api_key` como argumento).

**Bloqueado por John:** clave IPN (`~/.config/nowpayments/ipn-secret`) y decisión sobre el eBook de 9 € (por debajo del mínimo de NOWPayments) y la moneda de liquidación.

**Cómo se verifica (nunca en local):** `python3 scripts/productos-digitales/gate-flujo-postpago.py` (sección E), `node --experimental-strip-types scripts/productos-digitales/tests/nowpayments-sig.test.ts` (42/42), curl contra el preview (contratos en el doc), logs con `netlify logs --url https://<deploy_id>--aichefpro.netlify.app --source functions --function <nombre> --since 30m`.

Sesión Claude Code · firma de commits `Via: Claude Code`.
