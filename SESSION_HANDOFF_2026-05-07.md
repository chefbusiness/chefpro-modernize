# Session Handoff — 2026-05-07 → próxima sesión

## TL;DR

Sprint paridad CB→AICP, día 3 cerrado. **Marisquería €14 LIVE en producción** (verificado con tarjeta — botón COMPRAR abre Stripe Checkout). Implementado **estándar llms.txt site-wide** para GEO (descubrimiento por LLMs).

**HEAD**: `cda5b51`
**Tag GitHub respaldo**: `sprint-paridad-2026-05-06-marisqueria-live-llms-txt`

---

## Estado actual del sprint paridad CB→AICP

### LIVE (3 de 16)
| # | Producto | Slug | Stripe | Status |
|---|---|---|---|---|
| 1 | Kit Tareas Sushi Bar €14 | `/kit-tareas-sushi-bar` | `https://buy.stripe.com/14AfZa94w2S20IL1wV6oo0X` | LIVE |
| 2 | Kit Tareas Asador €14 | `/kit-tareas-asador` | `https://buy.stripe.com/fZu6oA5Sk1NY9fh3F36oo0Y` | LIVE |
| 3 | Kit Tareas Marisquería €14 | `/kit-tareas-marisqueria` | `https://buy.stripe.com/aFa8wI1C450a2QT2AZ6oo0Z` | LIVE |

### Pendientes (13 productos)

**Bloque A — Kits Tareas restantes (4 productos, mecánica idéntica a Marisquería)**
- #4 `/kit-tareas-tapas-bar` — Tapas Bar / Gastrobar — €14 — env `VITE_STRIPE_PAYMENT_LINK_TAREAS_TAPAS_BAR`
- #5 `/kit-tareas-food-truck` — Food Truck — €12 — env `VITE_STRIPE_PAYMENT_LINK_TAREAS_FOOD_TRUCK`
- #6 `/kit-tareas-panaderia` — Panadería / Obrador — €12 — env `VITE_STRIPE_PAYMENT_LINK_TAREAS_PANADERIA`

**Bloque B — Planes Negocio Línea A (5 productos, plantilla NUEVA, distinta a Kits Tareas)**
- #7 `/plan-negocio-bar-restaurante` — €35 — primer producto = template canónico T1
- #8 `/plan-negocio-tapas-bar` — €35
- #9 `/plan-negocio-cafeteria` — €29
- #10 `/plan-negocio-panaderia` — €35
- #11 `/plan-negocio-food-truck` — €29

**Bloque C — Planes Línea B Gastro Móvil (5 productos, template Coctelería €55)**
- #12 `/plan-negocio-cocteleria-eventos` — €55 (template canónico, 9 entregables + 4 bonus)
- #13 `/plan-negocio-parrillero-asador-eventos` — €45
- #14 `/plan-negocio-paellero-eventos` — €45
- #15 `/plan-chef-privado-showcooking` — €45
- #16 `/plan-catering-tematico-eventos` — €45

---

## Mensaje exacto para arrancar mañana

> "Continuamos sprint paridad CB→AICP. Cerrado ayer 2026-05-06: Marisquería €14 LIVE en producción (`a322319`+`11bc897`) y `/llms.txt` + `/llms-full.txt` site-wide para GEO (`cda5b51`). HEAD `cda5b51`. Arrancamos producto #4: **Kit Tareas Tapas Bar / Gastrobar €14**, slug `/kit-tareas-tapas-bar`, env `VITE_STRIPE_PAYMENT_LINK_TAREAS_TAPAS_BAR`. Lee `SESSION_HANDOFF_2026-05-07.md` para el patrón mecánico (idéntico a Marisquería + actualizar `/public/llms.txt` con la nueva línea del producto). Adelante."

---

## Patrón mecánico canónico para Kit Tareas (mismo que usé para Marisquería)

1. Verificar archivos en `chefbusiness-astro`:
   ```bash
   ls /Users/johnguerrero/chefbusiness-astro/public/dl/kit-tareas-<slug>/
   ls /Users/johnguerrero/chefbusiness-astro/src/pages/productos-digitales/kit-tareas-<slug>.astro
   ```

2. Crear directorios + copiar .xlsx:
   ```bash
   mkdir -p public/dl/kit-tareas-<slug> src/components/kit-tareas-<slug>
   cp /Users/johnguerrero/chefbusiness-astro/public/dl/kit-tareas-<slug>/*.xlsx public/dl/kit-tareas-<slug>/
   ```

3. Generar 6 imágenes Nano Banana 2 (NUNCA reusar de otro producto):
   - `tareas-<slug>-{hero,img2,img3,img4,equipo,emplatado}.jpg`
   - Usar API key del maestro: `/Users/johnguerrero/chefbusiness-astro/IMAGENES_MAESTRO_CHEFBUSINESS.md` línea 23
   - Coste: 6 × $0.0672 = $0.40

4. Leer `chefbusiness-astro/src/pages/productos-digitales/kit-tareas-<slug>.astro` para extraer copy específico (testimonials, FAQs, ContentGrid templates+icons, HeroSection, WhySection, BonusSection, CtaFinal).

5. Clonar template Marisquería (es el más reciente y limpio):
   ```bash
   cp -r src/components/kit-tareas-marisqueria/. src/components/kit-tareas-<slug>/
   cp src/data/testimonials-marisqueria.ts src/data/testimonials-<slug>.ts
   cp src/pages/KitTareasMarisqueria.tsx src/pages/KitTareas<Slug>.tsx
   cp src/pages/KitTareasMarisqueriaAccessGate.tsx src/pages/KitTareas<Slug>AccessGate.tsx
   cp src/pages/KitTareasMarisqueriaDashboard.tsx src/pages/KitTareas<Slug>Dashboard.tsx
   ```

6. **Two-pass sed** (lección aprendida del bug genérico):
   - Pass 1: renombrar paths de imágenes específicas (`tareas-marisqueria-vivero` → `tareas-<slug>-img2`)
   - Pass 2: renombrar slug genérico + class names (`kit-tareas-marisqueria` → `kit-tareas-<slug>`, `KitTareasMarisqueria` → `KitTareas<Slug>`, `TAREAS_MARISQUERIA` → `TAREAS_<SLUG_UPPER>`, `marisqueriaTestimonials` → `<slug>Testimonials`)

7. Editar copy específico del nicho en cada componente (ContentGrid templates, HeroSection h1+subtitle+checkItems, WhySection reasons, AuthorSection bio, BonusSection desc, FaqAccordion 6 FAQs, CtaFinal items+heading, BuyBox CTA, GuaranteeSection, StickyBar label, KitTareas<Slug>.tsx Helmet+SEO+JSON-LD+breadcrumb, Dashboard TEMPLATES keys+icons+desc + h1 + p).

8. Editar `src/data/productos-digitales-config.ts` (entry con 11 paths verificados — script no-negociable `MISSING:0`).

9. Editar `src/App.tsx` (3 imports + 3 rutas).

10. Editar `netlify/edge-functions/og-meta.ts` (entry SEO).

11. Editar `src/pages/ProductosDigitales.tsx` (tarjeta hub con icono lucide adecuado — `Shell` para mariscos, busca el siguiente del nicho).

12. **NUEVO PASO HOY**: Editar `public/llms.txt` añadiendo UNA línea más en la sección "Recurring-Tasks Kits by Concept" con el formato canónico:
    ```
    - [Kit Tareas <Nombre> (€XX)](https://aichef.pro/kit-tareas-<slug>): operational checklists for <descripción corta del nicho>.
    ```

13. Verificar paths con script no-negociable (`MISSING: 0`).

14. `npx tsc --noEmit && npm run build`.

15. `git add` SOLO los archivos del producto (no el resto de modificaciones que arrastra el repo) + commit + push.

16. Entregar a John: nombre Stripe + descripción ~260 chars en formato párrafo + Confirmation URL + Env var name.

17. Esperar a John → crear Stripe + cargar env Netlify → commit vacío trigger rebuild → verificar.

---

## Files críticos del repo (referencia rápida)

- `src/App.tsx` — registro de rutas (líneas ~570-580 zona de Kits Tareas)
- `src/data/productos-digitales-config.ts` — entry por producto con 11 paths
- `src/pages/ProductosDigitales.tsx` — hub de productos
- `netlify/edge-functions/og-meta.ts` — OG tags por ruta
- `public/llms.txt` — índice maestro para LLMs (mantener actualizado)
- `public/llms-full.txt` — versión extendida del índice
- `IMAGENES_MAESTRO_CHEFBUSINESS.md` (en `chefbusiness-astro`) — API key Nano Banana 2

---

## ⚠️ Recordar

1. **Nunca reusar imágenes de otro producto** (lección Bug #4 documentada). Galería propia siempre.
2. **Two-pass sed obligatorio** (lección sed bug del Sushi Bar).
3. **Verificación de paths antes del commit** — script no-negociable, MISSING:0 obligatorio.
4. **Actualizar `/public/llms.txt`** cada producto nuevo (línea adicional en sección Recurring-Tasks).
5. **No tocar tema CSS / layouts globales** — la home siempre fue dark + gold.

---

## Commits clave de la sesión

- `bbd4a2c` — chore: trigger Netlify rebuild Asador env
- `a322319` — feat(productos): port Kit Tareas Marisquería €14
- `11bc897` — chore: trigger Netlify rebuild Marisquería env
- `cda5b51` — feat(geo): add /llms.txt + /llms-full.txt

## Coste sesión

- Marisquería: 6 imágenes × $0.0672 = $0.40
- **Total: $0.40**
