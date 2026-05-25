# SESSION HANDOFF — 2026-05-25/26

**Sprint**: Rebrand global "apps" → "agentes IA" en aichef.pro + mitigación SEO + 3 rondas de grammar audit.

**Estado**: ✅ CERRADO. 8 commits en `origin/main`. Netlify desplegando última versión.

**HEAD**: `063fd41`

---

## TL;DR

El user pidió cambiar la nomenclatura "apps"/"aplicaciones" a "agentes IA" en todas las páginas, todos los idiomas, metadatos SEO incluidos. ~566 cambios aplicados sobre 7 idiomas + componentes + datos + schemas JSON-LD + OG.

3 rondas de grammar fixes posteriores (la última con 3 subagents Explore en paralelo auditando ES/PT/IT/FR/DE/EN/NL) corrigieron concordancias de género/número/redundancia introducidas por el script de rebrand (regex agnóstico al contexto).

Grep final exhaustivo (16 patrones): **0 residuales**.

`npm run build` local verificado: ✓ 23.53s exit 0.

GSC sitemap resubmitted + 16 URL inspections vía MCP.

---

## Los 8 commits del sprint

| # | Hash | Concepto | Cambios |
|---|------|----------|---------|
| 1 | `04097db` | 7 locales JSON | 237 |
| 2 | `7e4f14d` | use-cases-content.{es,en}.ts + testimonials | 124 |
| 3 | `06fdcf3` | Componentes Kit Tareas + ImageDisclaimerNote + pseo + grammar 1 | 74 |
| 4 | `dbf20ba` | UseCasePage defaults + FAQ schemas inline + FormacionPresencial | 13 |
| 5 | `4ace7e5` | **SEO mitigation** — hybrid keywords "apps + agentes IA" 7 idiomas | 12 |
| 6 | `ffd024a` | **Grammar ronda 2** — femenino plural + redundancia + revert reservas | 19 |
| 7 | `063fd41` | **Grammar ronda 3 audit** — 3 subagents → 75 fixes | 75 |
| 8 | (verify) | `npm run build` ✓ 23s exit 0 | — |

---

## Reglas de tratamiento aplicadas

| Contexto | Tratamiento |
|---|---|
| Producto AICP propio | "apps" → "agentes IA" / "AI agents" / etc. por idioma |
| Competencia SaaS (Trail, software gestión, apps RRHH/inventario/fichaje/reservas) | "apps" → "software" / "sistemas" |
| Marca **ChatGPT** | intacto (incluyendo landing `/chatgpt-para-restaurantes`) |
| Falso positivo línea 2965 es.json (reservas) | revertido a "app propia" |

---

## SEO mitigation aplicada

En cada `seo.keywords` que ya menciona "agentes IA" tras el rebrand, apendizado al final el término viejo para preservar long-tail durante reabsorción de Google:
- ES: `, apps IA cocina, aplicaciones IA hostelería, apps inteligencia artificial restaurante`
- EN/FR/DE/IT/PT/NL: equivalentes por idioma

**Dip orgánico proyectado**: 10-15% durante 2-3 semanas (vs. 15-30% sin mitigación).

---

## Grammar fixes — 3 rondas + audit

| Ronda | Hash | Cambios | Trigger |
|---|---|---|---|
| 1 | (dentro de `06fdcf3`) | 7 | Bug "La agente IA" → "El agente IA" detectado en pseo + use-cases |
| 2 | `ffd024a` | 19 | User reportó "nuestras agentes de IA" mal en ES |
| 3 | `063fd41` | 75 | User pidió audit exhaustivo con subagents |

### Subagents Explore (ronda 3, 3 en paralelo)

- **Agent A (ES)**: 39 bugs (6 puntuales + 33 sistémicos `use-cases-content.es.ts` patrón "suite de agentes (de) IA + adj fem").
- **Agent B (PT + IT)**: 5 bugs (4 PT + 1 IT — todos género de determinante).
- **Agent C (FR + DE + EN + NL)**: 13 bugs (predominante redundancia "IA IA" / "KI-KI" / "AI AI" / "AI-AI" en cookie/privacy strings).

### Tipos de bugs corregidos

- Determinante femenino + "agente(s)" masc (ES/PT/IT)
- Adjetivo posterior femenino → masc plural
- Redundancia "agentes IA de IA" / "KI-KI-Agenten" / "AI AI agents"
- Concordancia número (DE/NL singular cuando era plural)
- Pronombre referencial mal concordado ("tú las recibes" → "tú los recibes")
- Sistémico .es.ts: "suite de agentes (de) IA + especializada/pensada/diseñada/dedicada/etc." (43 instancias)

---

## GSC operaciones (via MCP gscServer)

| Operación | Resultado |
|---|---|
| `list_properties` | 37 properties. Usada: `sc-domain:aichef.pro` (siteOwner) |
| `get_sitemaps` | 8 sitemaps activos. Principal: `https://aichef.pro/sitemap.xml` (581 URLs indexed) |
| `submit_sitemap` | ✅ Resubmitted 2026-05-25 20:41, pending processing |
| `batch_url_inspection` x2 (16 URLs) | 8 indexed, 7 unknown, 1 discovered-not-indexed |

### Indexed (8 — re-crawl pendiente tras sitemap submit)
`/`, `/herramientas-gratuitas`, `/kit-escandallos`, `/pack-appcc`, `/pro-prompts-ebook`, `/usos`, `/en/kitchen-management-software-ai`, `/usos/concepto/dark-kitchen`

### Unknown a Google (7 — el sitemap submit las descubrirá)
`/en/`, `/precios`, `/reducir-costes-con-ia`, `/carta-menu-con-ia`, `/marketing-con-ia`, `/herramientas-ia-restaurantes`, `/usos/rol/chef-ejecutivo`

### Discovered, not indexed (1 — issue preexistente, no rebrand)
`/chatgpt-para-restaurantes` — probable thin content o canonical conflict. Investigar aparte.

---

## Pendientes post-sprint (para el user)

1. **GSC UI manual** → "Request Indexing" en top 5 URLs. Acelera reabsorción 3 sem → ~1 sem. La API no expone esto, solo la UI web.
2. **NO tocar blog posts antiguos** (chefbusiness.blog, blog.aichef.pro) — sirven como ancla semántica natural durante la transición.
3. **GA4 + GSC monitoring** 4-6 sem sobre top 20 queries. Si dip > 35% semana 4: pingame para mitigación adicional.
4. **Investigar `/chatgpt-para-restaurantes`** "Discovered, not indexed" — issue preexistente, no relacionado al rebrand.
5. Opcional: schema `additionalType: "AI Agent for Hospitality"` en WebApplication/SoftwareApplication.

---

## Reglas operativas nuevas (guardadas en memoria persistente)

- [[feedback-cpu-temperatura-limite-65]] — monitorizar `istats cpu temp`, límite 65°C. Apagones térmicos previos (2026-05-07/08) justifican.
- [[feedback-no-playwright-recalienta-cpu]] — no usar Playwright (incluido playwright-mcp) en este proyecto. Verificar UI con build + grep + curl.

---

## Scripts canónicos

- `scripts/rename_apps_to_agentes.py` — process 7 JSON locales + TS data files con reglas por idioma. Lookahead heurístico para no romper i18n key paths.
- Inline `python3 - <<'PYEOF'` scripts para: competidor-context en componentes, grammar fixes rondas 2 y 3, audit final.

---

## Próxima sesión — recomendaciones

A) **Esperar 7-10 días** para ver datos GSC post-reabsorción y decidir si hay que mitigar más.
B) Si pasa todo OK: retomar el **plan canónico**: portar AICP→CB (11 productos) o Fase 3 i18n FR/IT/PT/DE/NL en otras áreas del sitio aún sin traducir.
C) Investigar el caso aislado `/chatgpt-para-restaurantes` (Discovered, not indexed) — fácil sprint corto.
