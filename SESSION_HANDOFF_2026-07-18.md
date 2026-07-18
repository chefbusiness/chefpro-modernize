# SESSION HANDOFF — 2026-07-18 (fin de día)

**Día de 3 sesiones y 2 apagones térmicos. Resultado: Fase 1 COMPLETA + Fase 2 use cases COMPLETA (441/441 gates verdes). HEAD = `515fe09` + commit de docs.**

---

## 1. Qué se cerró hoy ✅

1. **Slice 3 — home ×7 idiomas** (`272db46` + `3abfbca`): 6 index por idioma, auditoría i18n de 23 componentes, gotcha `build format 'file'`.
2. **Slice 4 — /mentoria-online ×7 + /formacion-presencial** (`f8ab209` + `63e4ed6`): con esto **FASE 1 COMPLETA** (recordar: /precios, /sobre y /servicios NO existen en la SPA — error del plan original).
3. **FASE 2 COMPLETA — cluster use cases 441 URLs ×7 idiomas** (`515fe09`, 451 files):
   - `astro-site/src/lib/use-cases.ts` — SEGMENTS/CONSULTOR_HUB verbatim, `spokeStaticPaths` (62 paths/idioma), helpers de rutas y alternates.
   - `UseCasePageContent.astro` (port 1:1 de `UseCasePage.tsx`, 835 líneas) + `UseCasesHubPage.astro` + `ConsultoriaGastroProHubPage.astro` + `Icon.astro` (50 lucide SVG inline).
   - 7 wrappers hub + 7 catch-alls `[...rest].astro` — **páginas dinámicas** vía getStaticPaths, no 441 ficheros.
   - 430 assets copiados y verificados con `diff -rq`.

## 2. Gates Fase 2 verificados (curl UA Googlebot, staging)

**441/441 en 200** · title + meta description + **canonical exacto a producción** + H1 + **hreflang×8** en las 441 · **FAQPage en 434/434** spokes+consultor (los 7 hubs principales sin FAQ = paridad exacta, `UseCasesHub.tsx` no tiene FAQ) · muestra profunda por idioma (spoke + consultor de cada lang) OK.

## 3. Los 2 apagones térmicos y cómo se recuperó TODO

- **~13:18** — murió al lanzar los gates del slice 4 → recuperado de transcript JSONL, gates relanzados verdes, Fase 2 relanzada.
- **~14:21** — murió el workflow de Fase 2 tras escribir los hubs (CPU 65 °C por renderers de Chrome, no por nuestro trabajo).
- **Método (persistido en memoria `reference_recuperacion-apagon-termico-workflows.md`)**: `/private/tmp` se BORRA al reiniciar, pero en `~/.claude/projects/<proj>/` sobreviven los transcripts, y en `<sesión>/workflows/wf_*.json` está el **script completo** del workflow + en `subagents/workflows/<wf>/journal.jsonl` el **resultado real de cada agente**. Con eso se escribe un script de continuación (el `resumeFromRunId` es solo intra-sesión).

## 4. Hallazgos BAJA pendientes (no bloquean)

1. **`finalBody` DE del hub consultor** dice "5 Anwendungen pro Monat" **en la SPA** (`ConsultoriaGastroProHub.tsx:202`, resto pre-créditos). Fix en la SPA y re-mirror al `.astro` — NUNCA editar solo la copia de Astro (rompería paridad).
2. **51 ogImages ES** de role/concept/task apuntan a `og/use-cases/{slug}.jpg` que tampoco existen en la SPA (solo hay 51 EN + 11 consultor/hub). Generar con `generate-images` en Fase 6/8.
3. Titles/contenido de spokes role/concept/task en FR/DE/IT/PT/NL salen en ES (fallback `content.es` — igual que la SPA; traducirlos = Fase 8, no es regresión).

## 5. Método vigente + térmica

Workflows secuenciales con **modelos explícitos** (porters/revisores/fixers = Opus, mecánica = Sonnet; Fable solo orquesta) + revisor adversarial con schema antes de cerrar cada pieza + gates curl (nunca builds locales ni Playwright). Vigilante istats en background, umbral 63 °C. El causante real del calor de hoy: **pestañas de Chrome** (renderer al 78% CPU).

## 6. Próxima sesión — arranque directo

**Fase 3 — pSEO 75 ciudades** (est. 1 sesión): 1 template data-driven. Referencia del cluster actual: `project_pseo-cities-restaurants.md` (75 ciudades LIVE en la SPA, cluster conectado con 5 puntos de entrada — replicar interenlazado). Mismo método que Fase 2: lib/getStaticPaths + template + revisor adversarial + gates contra el sitemap (76 URLs routables según memoria — verificar conteo exacto en sitemap antes de empezar).

Después: Fase 4 (productos digitales, 33 landings) — **parar y avisar a John antes** (toca dinero).

**Directiva vigente**: ejecución AUTÓNOMA slice a slice (la SPA es la spec); parar solo en producto/copy nuevo, dinero (Fases 4-5) y cutover (Fase 7).

## Mensaje para retomar

> Claude, retomamos la migración Astro de aichef.pro. Lee `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` (§8) y `SESSION_HANDOFF_2026-07-18.md`. Fases 1 y 2 cerradas con gates verdes; arranca directo con la Fase 3 (pSEO 75 ciudades) en staging (site `dc777725-7e95-4336-876e-a5a9b568fe75`).
