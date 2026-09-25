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
