# SESSION HANDOFF — 2026-07-03

**Sesión triple: pricing free tier + auditoría SEO + arranque PLAN MAESTRO migración Astro.**

---

## 1. Pricing — CERRADO ✅ (LIVE verificado)

**Diagnóstico**: 0 suscripciones nuevas ~3 semanas. Checkout descartado como causa (John lo probó en incógnito, Stripe OK). Causa real: **arbitraje** — el free de 10.000 créditos/mes + bonus de 10€ = 30-35.000 créditos (mismo precio por crédito que Pro) hacía irracional suscribirse; usuarios de Pro 25€ se bajaban a free+bonus.

**Aplicado**:
- **Pickaxe (John)**: rate €1 = 3.000 → **1.000 créditos** (bonus 10€ pasa a 10.000, prima 3,4× vs Pro) + free 10.000 → **3.000 créditos/mes**. ⚠️ Verificar hecho en LOS 5 WORKSPACES (ES/EN/IT/FR/DE — rate y límite van por workspace).
- **Web (commit `93d73fb`, LIVE verificado en bundle)**: 30 archivos / 362 reemplazos — free a 3.000 en 7 idiomas + rename **"Premium Plus Anual" → "Premium Max Anual"** (era Max ilimitado mal etiquetado: parecía +58% vs Plus mensual).
- **Mecánica clave descubierta**: el rate NO cambia consumo por run (~1.428 créditos/run constante) ni asignaciones de planes (van por Access group). Solo precia los créditos comprados. Los Access groups de pago tienen checkbox **"Free Trial Period"** → palanca futura si el free sigue sin convertir.
- **Vigilar (finales julio)**: menos bonus sueltos, altas Pro, frees chocando límite. Detalle completo: memoria `project_pricing-arbitraje-bonus-vs-suscripcion.md`.

## 2. Auditoría SEO — ENTREGADA (inventario, nada aplicado sobre la SPA)

Hallazgos críticos: og-meta solo cubre ~63/658 URLs (el resto sirve title de HOME a los bots) · hreflang 0 · HTML crudo 2,7 KB · hub consultor "Discovered, Last Crawl NEVER" tras 5 semanas · ~90% clicks = marca · striking distance y limpieza documentados en `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` §1 y §5.

## 3. PLAN MAESTRO migración Astro — APROBADO, EJECUCIÓN ARRANCADA

- **Decisión John**: ejecución al 100%. Los quick wins NO se aplican a la SPA (nos la vamos a cargar); nacen nativos en Astro (D2 del plan).
- **Documento canónico**: `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` (raíz del repo) — 8 fases, decisiones D1-D10, gates de aceptación, riesgos, log de ejecución vivo.
- **Fase 0 arrancada hoy**: scaffold `astro-site/` creado A MANO (sin npm install local — regla térmica): package.json, astro.config.mjs (i18n 7 idiomas, es sin prefijo), tailwind.config portado del actual, tokens CSS portados, BaseLayout.astro con canonical+hreflang nativos, netlify.toml de staging con **X-Robots-Tag: noindex**, README.
- **Staging creado VÍA CLI (sin pasos manuales de John)**: site `aichef-astro-staging` (id `dc777725-7e95-4336-876e-a5a9b568fe75`) → **https://aichef-astro-staging.netlify.app** — repo conectado (base `astro-site`, branch `main`, publish `astro-site/dist`). Gotcha CLI: `netlify api createSite/updateSite` exigen los campos dentro de `"body": {…}`.
- **✅ GATE FASE 0 SUPERADO (2026-07-03)**: primer build verde + HTTP 200 + `x-robots-tag: noindex` + title/meta server-side + canonical + **hreflang ×8** (7 idiomas + x-default) verificados con curl. **FASE 0 CERRADA.**
- **Próxima sesión**: directo a **Fase 1** (home ×7 idiomas, /precios, header/footer/nav con paridad visual).

## 3-bis. "Replicar y Sustituir Pickaxe" — visión registrada (Fase 9)

John decidió registrar la sustitución de Pickaxe por una app propia (`app.aichef.pro`, chat estilo ChatGPT + 55 agentes + créditos + MCP/actions/webhooks, posiblemente en Vercel) como **fase final post-Astro**. Documento canónico: `REPLICAR_Y_SUSTITUIR_PICKAXE.md` (raíz) — catálogo de limitaciones vividas, activos (¡el Stripe con las suscripciones ya es nuestro!), decisiones abiertas a iterar y fases 9.0-9.5. NO se ejecuta nada hasta cerrar la migración Astro; primero se madura la idea.

## 4. Reglas reforzadas hoy

- **REGLA TÉRMICA reforzada por John** (CPU llegó a 63,6 °C en sesión): istats siempre, ralentizar cerca de 65 °C, cero builds locales/Playwright. Memoria: `feedback_regla-termica-cpu-65-grados.md`.

## Mensaje para retomar

> Claude, retomamos la migración Astro de aichef.pro. Lee `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` (raíz) y `SESSION_HANDOFF_2026-07-03.md`. El staging de Netlify [ya está creado / hay que crearlo]. Verifica el gate de Fase 0 y sigue con Fase 1.
