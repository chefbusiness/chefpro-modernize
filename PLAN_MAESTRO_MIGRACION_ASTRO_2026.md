# PLAN MAESTRO — Migración de aichef.pro (parte pública) a Astro

> **Estado: APROBADO — EJECUCIÓN AL 100%** (decisión de John, 2026-07-03)
> Documento canónico del proyecto. Se actualiza al cierre de cada sesión con el log de ejecución (§8).

---

## 1. Por qué (evidencia, auditoría 2026-07-03)

La parte pública actual es una SPA React 18 + Vite con client-side rendering puro. Auditoría con GSC + curl UA Googlebot:

- **La edge function `og-meta` solo cubre ~63 de las 658 URLs del sitemap.** El resto (`/usos`, `/precios`, `/en`, todos los spokes probados…) sirve el `<title>`/meta de la HOME en el HTML crudo → cientos de páginas parecen duplicados de la home en la primera ola de indexación.
- **hreflang: 0 etiquetas server-side** con 7 idiomas + redirect 302 automático por idioma. Señal internacional rota.
- **HTML crudo ≈ 2,7 KB de texto visible** (shell SPA). Todo depende del render JS (segunda ola, tardía y no garantizada).
- **Hub Consultoría Gastro Pro: "Discovered — currently not indexed, Last Crawl: NEVER"** 5 semanas tras el lanzamiento. El cluster consultor (11 págs × 7 idiomas) probablemente invisible entero.
- **~90% de los clicks son de marca** (GSC 28d: 1.384 clicks / 53,8k impr / pos 17,2). Los 102 spokes ES+EN + 75 pSEO + consultor apenas generan clicks no-marca. El techo es estructural, no de contenido.

## 2. Decisiones registradas

| # | Decisión | Motivo |
|---|---|---|
| D1 | Migrar TODA la parte pública a Astro (stack estándar del grupo) | Evidencia §1; paridad con resto de webs del grupo |
| D2 | **NO aplicar quick wins (og-meta completo, prerender, hreflang edge) a la SPA actual** | Decisión de John 2026-07-03: no invertir en algo que vamos a matar; esas mejoras nacen nativas en Astro |
| D3 | Monorepo: el proyecto Astro vive en `astro-site/` dentro de este repo | Historia única, assets compartidos, un solo lugar que proteger |
| D4 | Netlify functions y flujos de pago/acceso se migran TAL CUAL (son framework-agnósticas) | Riesgo dinero = 0 cambios de lógica |
| D5 | Partes "app" (gates post-pago, dashboards descargas, biblioteca Pro Prompts, admin) = **islands React** reutilizando componentes actuales | No reescribir lo que funciona y toca dinero |
| D6 | **Paridad de URLs 1:1** en el cutover: los 658 slugs idénticos, sitemap idéntico. Rediseño/copy "2026" DESPUÉS de estabilizar, nunca mezclado con el cambio de stack | Riesgo SEO del cutover al mínimo |
| D7 | Staging con `X-Robots-Tag: noindex` hasta el cutover | Evitar contenido duplicado durante la migración |
| D8 | Builds y verificación **SOLO en nube** (Netlify deploy previews). NUNCA `npm install`/`astro build`/Playwright en local | REGLA TÉRMICA (CPU ≤65 °C) |
| D9 | Contenido nuevo que se redacte durante la mejora "2026" → `bridge.py`; imágenes → skill `generate-images` | REGLA CAPITAL de contenidos |
| D10 | Carpintería → subagentes `sonnet`/`opus` con `model` explícito; Fable orquesta y verifica lo crítico | REGLA DE DELEGACIÓN |

## 3. Arquitectura objetivo

- **Astro 5 + @astrojs/react** (islands) + Tailwind 3 (config portada verbatim del actual para paridad visual) + @astrojs/sitemap.
- **i18n nativo de Astro**: `es` default sin prefijo + `en/fr/de/it/pt/nl` con prefijo — mismo esquema de rutas actual. hreflang generado en el layout base para TODAS las páginas desde el día 0.
- **Contenido**: los datos existentes (`use-cases-content.*.ts`, `pseo-cities.ts`, `productos-digitales-config.ts`, locales JSON) se transforman con scripts a content collections / data files de Astro. No se reescribe contenido, se vierte.
- **Meta por página nativo en build** → la edge function `og-meta` MUERE con el cutover. `lang-redirect` (302 auto-idioma) se revisa en Fase 6 (con hreflang nativo probablemente sobra o se restringe).
- **Netlify**: site nuevo de staging apuntando a este repo con `base = astro-site`. El site actual no se toca hasta el cutover.

## 4. Fases, entregables y criterios de aceptación

| Fase | Alcance | Criterio de aceptación (gate UltraCode) | Est. |
|---|---|---|---|
| **0** | Scaffolding `astro-site/`: config Astro+i18n, Tailwind portado, tokens/CSS vars, BaseLayout con canonical+hreflang, netlify.toml staging (noindex), README | Deploy staging VERDE en Netlify; curl del staging muestra HTML con title/meta/hreflang correctos | 1-2 ses. |
| **1** | Núcleo marketing: home ×7 idiomas, /precios, servicios, sobre, header/footer/nav completos | Paridad visual y de copy con producción (verificación por WebFetch/screenshot en nube); HTML crudo completo por idioma | 2-3 ses. |
| **2** | Use cases: script TS→content collections + 102 spokes + hubs (usos, consultor) | 100% spokes con title/meta/H1/FAQ schema propios en HTML crudo; diff de contenido byte-a-byte vs datos origen | 2-3 ses. |
| **3** | pSEO 75 ciudades (1 template data-driven) | 75 URLs con paridad de slug y contenido completo server-side | 1 ses. |
| **4** | Productos digitales: 33 landings consolidadas (460 componentes clónicos → 1-2 templates + 33 entradas) + páginas de compra | Los 33 checkouts Stripe apuntando a los MISMOS payment links (env vars); QA de enlaces 33/33 | 3-4 ses. |
| **5** | Zona app como islands: gates acceso, dashboards descarga, biblioteca Pro Prompts (JWT), /admin | **Compra de prueba real end-to-end** + acceso + descarga verificados; funciones netlify intactas (0 diff) | 2-3 ses. |
| **6** | SEO nativo: sitemap en build (diff exacto vs sitemap.xml actual), OG images, redirects, revisión lang-redirect, llms.txt | Diff sitemap = 0 URLs perdidas; rich results válidos (FAQ/Product/Breadcrumb) en muestras | 1-2 ses. |
| **7** | **Cutover**: quitar noindex, swap del site en Netlify (o cambio de publish dir), monitoreo GSC diario | 2-4 semanas de vigilancia: cobertura de indexación ≥ baseline, 0 errores 404/soft-404 nuevos | 1-2 ses. |
| **8** (post) | Mejora "2026": rediseño/copy/contenido enriquecido, quick wins CTR (titles striking distance §5), más free tools | Cada mejora con research+SERP previo (REGLA CAPITAL) | abierta |
| **9** (siguiente nivel) | **Replicar y Sustituir Pickaxe**: app propia `app.aichef.pro` (chat + agentes + créditos + MCP/actions/webhooks). Visión completa en [`REPLICAR_Y_SUSTITUIR_PICKAXE.md`](REPLICAR_Y_SUSTITUIR_PICKAXE.md) | Se itera la idea al cerrar Fase 7; no se ejecuta hasta madurar stack y spec | post-Astro |

**Total estimado (Fases 0-7): 12-18 sesiones.**

## 5. Backlog SEO que nace DENTRO de Astro (ex-quick wins, por D2)

- hreflang 7 idiomas en todas las páginas (Fase 0, layout base).
- Meta únicos por URL para las 658 (Fases 1-4, nativo).
- Titles/CTR de striking distance: `/herramientas-gratuitas` (pos 3,8 / 468 impr), `/en/kitchen-management-software-ai` (7,9 / 462), `/en/reduce-restaurant-costs-ai` (8,2 / 378), `/kit-escandallos` (14,7 / 236) → Fase 8.
- Más free tools (mejor performer no-marca) → Fase 8 con `free-tool-strategy`.
- Poda blog posts fa/uz/ka/ko (skill `prune-posts`) → independiente de la migración, cualquier momento.
- Housekeeping GSC: retirar sitemap www duplicado + sitemap tienda stale → en Fase 7.

## 6. Riesgos y mitigaciones

1. **Romper pagos/accesos** → D4+D5 (cero cambios de lógica) + compra test real en Fase 5 + los 2 bugs históricos (access gates 2026-04-29, paths descarga) como checklist explícito.
2. **Regresión SEO en cutover** → D6 paridad 1:1 + D7 noindex staging + diff sitemap Fase 6 + vigilancia GSC Fase 7. Rollback = revertir swap en Netlify (la SPA queda intacta en el repo).
3. **Térmica** → D8. Si una sesión exige iterar mucho: mover dev a Abacus (skill `migrar-a-abacus`).
4. **Doble mantenimiento durante la migración** → congelar productos nuevos y cambios de copy en la SPA salvo urgencias (pricing, bugs); si algo cambia en la SPA, anotarlo en §8 para replicar en Astro.

## 7. Toolkit de verificación (cada fase)

```bash
# Qué ve un bot (staging o prod)
curl -s -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" URL | grep -o "<title>[^<]*</title>\|hreflang"
# Estado deploy Netlify staging → panel o API; GSC vía MCP gscServer; temperatura → istats cpu temp
```

## 8. Log de ejecución (actualizar cada sesión)

- **2026-07-03** — Plan aprobado. Fase 0 arrancada: scaffold `astro-site/` creado a mano (sin npm install local, D8), pendiente crear site de staging en Netlify (JOHN: New site from Git → este repo → base `astro-site`, build `npm run build`, publish `astro-site/dist`).
