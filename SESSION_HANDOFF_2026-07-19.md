# SESSION HANDOFF — 2026-07-19

## Sesión 3 (mediodía) — ✅ FASE 6 COMPLETA: SEO nativo + 155 URLs rescatadas, gate 2.278 checks verde

**Fases 0-6 ✅ — solo queda Fase 7 (cutover, decisión de John) y las post-cutover.** El censo destapó 126 URLs de free tools/landings/hub jamás asignadas a fase + 5 legales en 404 → portadas 155 URLs como islands (22 head-modules con doble verificación adversarial). Sitemap nativo 696 URLs (= prod − /services×7 + 45 productos), lastmod portado, llms.txt, lang-redirect ACTIVO en staging (se mantiene tras cutover), 3 JSON-LD globales en BaseLayout, 51 OG cards ES (QA visual, 3 regeneradas) LIVE también en prod. Detalle completo en plan maestro §8 (entrada 2026-07-19 Fase 6).

Claves para la próxima sesión: 2 gotchas nuevos en §8 (aliases de paquetes bare cross-root + plugin `cross-root-assets-as-url` para imágenes) · gate reutilizable `scripts/astro-migration/fase6-gate.py` (2.278 checks; correr tras cualquier cambio en astro-site) · **Fase 7 = cutover: quitar FunctionsOriginPatch.astro + bloque noindex del netlify.toml de astro-site + añadir meta robots index en BaseLayout + swap de site + GSC** — NO ejecutar sin OK explícito de John. Ideas nuevas registradas: Fase 8B (blog.aichef.pro → /blog con 301 por post) y 8C (~70 páginas de agentes IA).

---

## Sesión 2 (mañana) — ✅ FASE 5 COMPLETA: gate 767/767 + happy-path E2E real CERRADO

Las 89 rutas de la zona app post-pago (44 access + 44 library + admin) LIVE en staging como islands `client:only` reutilizando los componentes de la SPA cross-root TAL CUAL. **Gate de aceptación cerrado con magic link real de John**: generado desde el admin de Astro en staging (S3 e2e) → gate vanilla Pro Prompts en staging → library compuesta → 3/3 descargas binarias reales. Detalle completo en plan maestro §8 (entrada 2026-07-19 Fase 5). **Próximo: Fase 6.**

Claves rápidas para la próxima sesión: gotcha Netlify `/.netlify/*` no redirigible → `FunctionsOriginPatch.astro` (QUITAR en cutover, igual que el bloque noindex del toml) · generador+gate en `scripts/astro-migration/fase5-*.py` · fix admin select 27→44 YA EN PRODUCCIÓN · próximo: Fase 6 (sitemap build con +45 URLs de productos, diff vs sitemap.xml actual, og images, revisión lang-redirect, llms.txt).

---

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
