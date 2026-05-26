# SEO Audit Consultoría Gastro Pro — Session Handoff 2026-05-26

## Contexto

User pidió auditoría SEO completa de las 77 páginas del módulo Consultoría Gastro Pro (1 hub + 10 spokes × 7 idiomas) tras el sprint i18n masivo. **Objetivo: que las páginas posicionen en Google de cada mercado para captar consultores gastronómicos como suscriptores de aichef.pro, no "saludo al viento"**.

## Estado del audit

8 subagentes lanzados en paralelo (background):

| Agent | Topic | Status |
|---|---|---|
| afdd2234eea0455fd | EN keyword research (US/UK/global) | ✅ **VOLVIÓ** — ver `seo_research_en.md` |
| a1a9e02fffab6c2c4 | FR keyword research (FR/BE/CH/QC) | ✅ **VOLVIÓ** — ver `seo_research_fr.md` |
| a128333948fc3edaa | DE keyword research (DE/AT/CH) | ⏳ Pending |
| a5f2e8bf6bcddb175 | IT keyword research (IT) | ⏳ Pending |
| aa87c97c002e4c228 | PT keyword research (PT + BR) | ⏳ Pending |
| a7db0b9e2cf2d0cc9 | NL keyword research (NL + BE-FL) | ⏳ Pending |
| a9394b30e4ad45b60 | ES keyword research (ES + LATAM) | ⏳ Pending |
| aff400f32094746a5 | Auditoría técnica transversal (meta/schemas/OG/hreflang) | ⏳ Pending |

## Bugs CRÍTICOS ya identificados (preliminar, EN + FR)

### EN — Search-volume mismatch en 5 H1
1. **chef-consultor** "Consultant Chef Pro" → debería ser **"Chef Consultant"** (×3 volume)
2. **barista-consultor** "Barista Consultant Pro" → debería ser **"Coffee Shop Consultant"** (×10 volume)
3. **bartender-consultor** "Bartender Consultant Pro" → debería ser **"Bar / Cocktail Consultant"** (×8 volume)
4. **baker-consultor** "Baker Consultant Pro" → debería ser **"Bakery Consultant"** (×5 volume)
5. **pizzero-consultor** "Pizza Chef Consultant Pro" → debería ser **"Pizza / Pizzeria Consultant"** (×6 volume)

### FR — TODAS las H1 con orden invertido al uso nativo
- "Pâtissier Consultant" → **"Consultant Pâtissier"**
- "Boulanger Consultant" → **"Consultant Boulanger"**
- ... mismo patrón en los 10 spokes
- "Bartender" → **"Mixologue/Barman"** (bartender = cero volumen FR)
- "HORECA" → **"CHR"** para FR puro
- "Gastronomy Consultant" → **"Consultant en Restauration"** (×3-4 mejor)

## Gaps de contenido universales (EN findings)

1. **Falta sección "Pricing & Fees"** en todos los spokes. El PAA #1 universal es "how much does X consultant charge". Tenemos ranges en los 10 nichos.
2. **Falta sección "Startup Costs"** en consumer-facing (gelato, pizza, coffee, bakery, chocolate). Esos PAA tienen ×5-20 volumen vs queries de consultor.
3. **Falta posicionamiento competitivo vs Tastewise/Nory/Toast** (SaaS players). Ninguno ranquea por "AI for [consultant role]" — ventaja para nosotros.
4. **FAQs no usan PAA verbatim**. Hay que reemplazar las FAQ actuales por las preguntas exactas del PAA de Google para que aparezcan como rich results.
5. **No hay schema.org Service con priceRange** real.

## Decisión estratégica preliminar (esperando agentes restantes)

Una vez vuelvan los 6 agentes restantes, sintetizar:
1. Tabla unificada de renames H1 por idioma
2. Tabla de keywords a integrar en H2/copy por idioma
3. Plan de implementación: ¿cuántos commits, qué orden?
4. Estimación de impacto: tráfico orgánico potencial post-fix

## Archivos de backup en este directorio

- `SESSION_HANDOFF.md` — este archivo
- `seo_research_en.md` — full EN report (con sources)
- `seo_research_fr.md` — full FR report (con sources)
- (pending) `seo_research_de.md` · `seo_research_it.md` · `seo_research_pt.md` · `seo_research_nl.md` · `seo_research_es.md` · `audit_tecnico.md`

## CPU + temperature

- Pico hoy: 61.44°C (zona de cuidado)
- Límite hard: 65°C → apagón térmico
- Estrategia: NO paralelo + Writes en lugar de Bash pesado + esperar agentes (que viven en cloud, no consumen CPU local)

## Estado de commits anteriores (Consultoría Gastro Pro completo LIVE)

```
f3ecb8d  feat(seo): sitemap +66 URLs i18n (592→658)
93553ca  feat(og-meta): social previews FR/DE/IT/PT/NL (55 entries)
b3128c6  feat(i18n): 6 idiomas adicionales con contenido nativo
553d1e4  feat(seo): sitemap +11 URLs ES
4d4a0f9  fix(security): API key no hardcoded
312e5e6  feat: 8 OG sufijo -consultor
e035e08  feat: 71 imgs Nano Banana 2
755edc0  feat(consultoria): hub + 10 landings ES
```

**HEAD actual: `f3ecb8d`** (a confirmar tras commit de este handoff)
