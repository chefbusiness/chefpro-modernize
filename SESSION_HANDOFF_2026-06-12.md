# SESSION HANDOFF — 2026-06-12 — Migración usos→créditos en planes de precios (CERRADO)

## Qué se hizo

Migración completa de la palabra **"usos" → "créditos"** y de las cantidades en **todos los planes, todos los idiomas (7) y todas las páginas** con réplica de planes. Commit único: **`94c6a88`** (LIVE en main, deploy automático Netlify).

### Conversión aplicada (confirmada por John con captura de app.aichef.pro)

| Plan | Antes | Ahora |
|---|---|---|
| AI Chef Miembro (Gratis) | 20 usos/mes | **10.000 créditos/mes** |
| AI Chef Premium Pro (25€/mes) | 150 usos/mes | **85.000 créditos/mes** |
| AI Chef Premium Plus (50€/mes) | 350 usos/mes | **175.000 créditos/mes** |
| AI Chef Premium Max (95€/mes) | Uso ilimitado | **Créditos ilimitados** |
| AI Chef Premium Plus Anual (950€/año) | Uso ilimitado | **Créditos ilimitados** |

CTAs gratuitos de casos de uso: "5 usos al mes" → "10.000 créditos al mes".

### Alcance — 531 reemplazos en 30 archivos

1. **7 locales JSON** (`src/i18n/locales/{es,en,fr,de,it,pt,nl}.json`): bloque principal de pricing (`uses_label` USOS→CRÉDITOS, `unlimited_badge`, claves `uses` ×37 por archivo, bullets "X usos mensuales", descripciones del plan Max/Anual, subtítulos "hasta el uso ilimitado") + 7 réplicas por landing temática + variante "X menús/mes" (landing carta) + prosa de FAQs con cifras.
2. **SEOHead.tsx**: JSON-LD `SoftwareApplication > offers` (4 descripciones).
3. **Use-cases content**: `use-cases-content.es.ts`, `.en.ts` y los 7 `.{lang}.consultor.ts`.
4. **UI use-cases**: `UseCasePage.tsx` (ctaFreeUses ×7 idiomas), `UseCasesHub.tsx` (es/en), `ConsultoriaGastroProHub.tsx` (7 idiomas: ctaNote, finalBody, FAQs, seoIntroBody DE, seoDescription NL), `PSeoCityPage.tsx` (CTA hardcoded).
5. **8 páginas pSEO** con arrays de planes hardcoded: EscandallosRestaurante, HerramientasIARestaurantes, RecetasIARestaurantes, ReducirCostesRestaurante, MenuRestaurante, ChatGPTRestaurantes, SoftwareGestionCocina, MarketingRestaurante.
6. **pseo-cities-content.es.ts**: "uso ilimitado" → "créditos ilimitados".

### Decisiones de wording

- Formato numérico localizado: ES/DE/IT/PT/NL `10.000` · EN `10,000` · FR `10 000`.
- Terminología tomada del FAQ canónico `/sistema-creditos`: créditos (ES/PT), credits (EN/NL), crédits (FR), Credits (DE), crediti (IT).
- **NO tocado a propósito**: `src/data/sistema-creditos-faq.ts` (explica la migración y menciona "usos" intencionalmente).
- La variante "20 menús/mes" pasó a créditos (la cifra en menús ya no existe en la plataforma).

### Verificación

- 7 JSON parsean OK (`python3 -m json.tool`), `tsc --noEmit` limpio.
- Auditoría grep final: **0 residuales** de wording de planes con "usos" en los 7 idiomas (los únicos hits son el verbo neerlandés "gebruiken" en prosa normal, falsos positivos).
- Scripts reproducibles con conteo por patrón: `scripts/migrate_usos_creditos.py` + `scripts/migrate_usos_creditos_fase2.py`.
- Restricción térmica respetada: máx 54°C (istats), sin Playwright, build en Netlify (nube).

## Estado

- **HEAD main = `94c6a88`** · Tag de respaldo: `migracion-usos-creditos-2026-06-12`.
- Memoria actualizada: `project_migracion-usos-a-creditos.md` (migración COMPLETA) + índice MEMORY.md.

## Pendiente / próxima sesión

- **Verificar en producción** (cuando Netlify termine el deploy): aichef.pro sección Precios debe mostrar "CRÉDITOS: 10.000/mes" etc. en los 7 idiomas. Sin Playwright basta `curl -s https://aichef.pro/assets/*.js | grep -c "10.000 créditos"` sobre el bundle o revisión visual de John.
- Opcional SEO: bump `lastmod` en sitemap de las páginas con planes (no se hizo — cambio de wording menor, no solicitado). Recordar: sitemap multi-formato → editar con parser DOTALL, nunca awk línea a línea.
- Hilos abiertos previos (sin cambios hoy): seguimiento GSC Consultoría Gastro Pro (~2-3 sem desde 2026-05-28), AICP→CB 11 productos, Fase 3 i18n FR/IT/PT/DE/NL de use cases, refactor netlify functions en branch `origin/refactor/netlify-functions-config-2026-05-08`, monitor pasivo Pickaxe (curl HEAD weekly) pendiente de añadir.
