# Pendientes — parches preparados y NO aplicados

## `replica-cripto-46-productos.patch` (6-sep-2026, 04:0x, sesión Claude Code)
Diff preparado por un agente opus sobre `e2b9cae` (rama `feat/cripto-ux-recuadro`) para montar la segunda puerta
«Pagar con cripto» en TODAS las landings: plantillas `GuiaLandingPage`, `KitExcelLandingPage`,
`PlanNegocioLandingPage` (3 inserciones cada una, calcadas de `KitTareasLandingPage`), página propia
`mega-pack-tareas.astro`, variable `CRYPTO_PRODUCTS_EXCLUDE` (helper de build + backend, normalización igual en
los dos), gate `gate-flujo-postpago.py` ampliado a las 46 landings, y la sección «Env vars» del doc.

**Estado:** el agente se paró antes de entregar su informe de verificación (John quiso apagar el Mac), así que
el parche está **sin revisar** y puede estar incompleto en su último paso (el gate). Decisión de John: la réplica
se aplica **después** del pago real de prueba (~8-sep-2026).

**Cómo aplicarlo:** `git apply --check scripts/productos-digitales/pendientes/replica-cripto-46-productos.patch`
sobre `main`. ⚠️ El parche nació sobre `e2b9cae`, donde el hero de Kit de Tareas llevaba la tarjeta cripto como
HERMANA del recuadro dorado; en `main` (`ad5bce5`) el hero volvió al bloque INTEGRADO por decisión de John. El
parche NO toca `KitTareasLandingPage.astro`, pero en las tres plantillas nuevas coloca el `variant="hero"` como
hermano: **al aplicarlo hay que mover esas tres inserciones del hero DENTRO del recuadro dorado**, tras el sello
de Stripe, como está hoy en Kit de Tareas. Después: revisión adversarial del diff, preview con
`CRYPTO_PRODUCTS=all` + `CRYPTO_PRODUCTS_EXCLUDE=pro-prompts-ebook` en `deploy-preview`, curl a las 46 landings.
Detalle en `PAGOS_CRYPTO_NOWPAYMENTS.md` → «Siguiente sesión».
