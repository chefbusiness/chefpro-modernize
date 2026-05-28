# SESSION HANDOFF — 2026-05-28

**Tarea**: Posicionar el módulo Consultoría Gastro Pro para "ia para consultores/asesores gastronómicos" + variantes por perfil. Auditar por intención de búsqueda real, validar e implementar mejores prácticas (hub + 10 spokes).

**Estado**: ✅ CERRADO. 3 commits en `origin/main`, todo LIVE y verificado por curl.

**HEAD**: `c46d5e1`

---

## TL;DR

El user no posicionaba para consultor/asesor gastronómico y propuso variantes por perfil. Auditoría con **datos reales** (GSC + Google Autocomplete por mercado/idioma) reveló que los combos por perfil ("ia para pasteleros/pizzeros/heladeros consultores") tienen **cero volumen** (emergentes), y que la demanda real está en los **head terms** (`consultor/asesor gastronómico`, `consultoría/asesoría gastronómica`) + el **ángulo IA** (`ia para restaurantes/hostelería`). Se optimizó el hub con esos términos (H1 nuevo + sección SEO + FAQ + schema, 7 idiomas) y se reforzó el **enlazado interno spokes→hub** (el contenido de los spokes ya estaba optimizado y NO se reescribió).

---

## Los 3 commits

| # | Hash | Concepto | Cambios |
|---|------|----------|---------|
| 1 | `9c91a40` | **Hub optimizado 7 idiomas** | `ConsultoriaGastroProHub.tsx` (+152/-35): H1 "IA para Consultores y Asesores Gastronómicos" (+ keyword validada por mercado), subtítulo, sección intro SEO (H2+prosa), bloque FAQ + `FAQPage` schema (5 FAQs), meta/keywords. ES/EN directo; FR/DE/IT/PT/NL vía bridge.py. + sitemap 7 hub URLs. |
| 2 | `43ea648` | **Enlazado interno spokes→hub** | `UseCasePage.tsx` (+39/-6), scoped a `type==='consultor'`: mapa `CONSULTOR_HUB`, breadcrumb gana nivel sub-hub, CTA enlaza al hub con anchor keyword (`consultorHubCta` ×7). 51 spokes role/concept/task intactos. |
| 3 | `c46d5e1` | **Sitemap lastmod 70 spokes** → 2026-05-28 | Parser DOTALL block-safe; 658 URLs intactas; 77 lastmod totales (7 hub + 70 spokes). |

---

## Auditoría — hallazgos validados (lo que el user pidió validar)

- **GSC** `sc-domain:aichef.pro`: ~0 visibilidad consultor/asesor (módulo nuevo, greenfield).
- **Google Autocomplete** (curl, por mercado/idioma):
  - ✅ Head terms fuertes y pan-hispanos: `consultor/asesor gastronómico`, `consultoría/asesoría gastronómica`.
  - ✅ Ángulo IA comercial: `ia para restaurantes` (gratis, agente ia, mejor ia) en todos los mercados; `ia para hostelería/chefs`.
  - ✅ Lexicón MX: `consultoría restaurantera`.
  - ❌ Combos por perfil propuestos = **cero autocompletado** (emergentes). Capturados como long-tail (H1 de spokes ya los llevan + FAQ del hub), no como eje.
  - Head terms por idioma: EN `ai for chefs`+`restaurant/F&B/hospitality consultant` · FR `consultant/conseil en restauration` · DE `Gastronomieberatung`+`KI für Gastronomie` · IT `consulente ristorazione` · PT `ia para restaurantes` (BR) · NL `horeca adviseur/consultant`.

---

## Verificación deploy (live)

- Sitemap live: `lastmod 2026-05-28` en hub + spokes (77 URLs).
- Bundles nuevos desplegados (`index-BLcTgfJY.js`, `index-6DtHeIH-.js`) contienen H1/FAQ/CTA nuevos.
- HTTP 200 en hub + spoke. GSC resubmit ×2 (11:06 + 11:26, Pending).

---

## Notas operativas

- **bridge.py** (`/Users/johnguerrero/chefbusiness-ai/`) usado para FR/DE/IT/PT/NL. Gotcha: deepseek-v4-pro razona → `--max-tokens` ≥8000 o devuelve vacío (3500 falló 3/5, 16000 OK).
- **Térmico**: verano Madrid, CPU rozó 69°C; el calor era de Chrome de fondo, no del trabajo. Builds a 54-56°C. Sin Playwright.
- **Regla aprendida**: H1 de hub descriptivo SÍ se optimiza; solo H1 de spoke (marca agente) es inmutable.

---

## Seguimiento (no bloqueante)

1. **Revisar GSC en ~2-3 semanas** (junio 2026): qué queries empieza a captar el hub tras indexación.
2. **Vigilar canibalización** con la propiedad hermana `sc-domain:consultoresgastronomicos.pro` (mismo nicho).
3. (Opcional) Replicar el patrón intro-SEO + FAQ + FAQPage en otros hubs de uso si rinde.
