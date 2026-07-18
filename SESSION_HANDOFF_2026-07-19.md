# SESSION HANDOFF — 2026-07-19 (madrugada)

**Fase 4 productos digitales COMPLETA: 44 landings + hub con gate de aceptación verde (44/44 checkouts con payment link byte-exacto + QA enlaces hub 44/44). HEAD = `9a24af7` + docs.**

---

## 1. Estado de la migración Astro

| Fase | Estado |
|---|---|
| 0 Scaffolding · 1 Núcleo marketing · 2 Use cases (441) · 3 pSEO ciudades (76) | ✅ cerradas con gates |
| **4 Productos digitales (44 landings + hub)** | ✅ **CERRADA 2026-07-19** — detalle en plan maestro §8 |
| 5 Zona app (gates + dashboards post-pago) | ⏸️ **ESPERA OK DE JOHN — dinero** |
| 6 SEO nativo (sitemap build) · 7 Cutover | Pendientes |

## 2. Claves técnicas de la Fase 4 (para Fase 5 y mantenimiento)

- **4 templates** en `astro-site/src/components/pages/`: KitTareas/KitExcel/Guia/PlanNegocio`LandingPage.astro` + datos en `astro-site/src/data/productos/{tareas,kits,guias,planes}/` + 2 one-offs (eBook, Mega Pack) + `ProductosDigitalesHubPage.astro`.
- **44 env vars `VITE_STRIPE_PAYMENT_LINK_*` replicadas al site de staging** (scope builds, vía API). Al crear producto 45: añadir la var TAMBIÉN en staging.
- **Gates reutilizables PERSISTIDOS EN EL REPO**: `scripts/astro-migration/` (README + `prepare-inputs.sh` que regenera listas de URLs y payment links + gates de Fases 2/3/4 + smoke del hotfix). Probados end-to-end el 2026-07-19. `/private/tmp` se borra en cada reinicio — todo lo valioso vive ya en el repo.
- Divergencias DOM por línea cubiertas con props opcionales (ver §8). El orden de tarjetas del hub es decisión de negocio — NO reordenar.

## 3. Hotfix de producción del 2026-07-18 (contexto)

17 productos entregaban el eBook post-pago (mapas de las 4 netlify functions desincronizados) → `7ab25b7` LIVE, smoke verde, **cero compras afectadas (confirmado por John)**. Bug #5 en la doctrina. Pendiente opcional de John: compra test o magic link admin para validar end-to-end (también servirá como test de Fase 5).

## 4. Próxima sesión — Fase 5 (SOLO con OK explícito de John)

Alcance: 44 access-gates + 44 dashboards como islands (D5: reutilizar componentes React), funciones netlify intactas (0 diff), `/admin/generar-acceso`, y **compra de prueba real end-to-end** como gate final. Antes de codificar: releer `feedback_digital-products-non-negotiables.md` (Bugs #1-#5). Quirks de naming: `/pro-prompts-library-access`, `/kit-tareas-hotel-completo-access`. Añadir noindex server-side + `Disallow` robots.txt para `/*-access` y `/*-library` (hoy depende de JS). Decidir config de functions del site Astro para el cutover (el site staging base=astro-site no las sirve — las llamadas van al dominio de producción hasta el swap).

Pendientes menores acumulados: finalBody DE hub consultor (SPA) · `/saas-trial` (datos pSEO) · 51 ogImages ES use cases · schemas globales BaseLayout · meta robots en cutover · sitemap Fase 6 debe AÑADIR las 45 URLs de productos (hoy 0/44 en sitemap, gap del generador de la SPA).

## Mensaje para retomar

> Claude, retomamos la migración Astro de aichef.pro. Lee `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` (§8) y `SESSION_HANDOFF_2026-07-19.md`. Fases 0-4 cerradas con gates verdes. Lo siguiente es la Fase 5 (zona app post-pago — dinero): preséntame el plan detallado y espera mi OK antes de tocar nada.
