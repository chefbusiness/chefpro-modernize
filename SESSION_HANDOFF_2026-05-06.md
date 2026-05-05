# Session Handoff — 2026-05-06 → próxima sesión

## TL;DR

Sprint paridad CB→AICP, día 2 cerrado. **Producto #2 (Kit Tareas Asador €14) tiene el código 100% LIVE en `origin/main`** esperando que John cree el Stripe Payment Link y cargue la env var en Netlify. También se arregló un bug crítico que detectó John en el producto #1 (Sushi Bar usaba imágenes de Chef Privado en lugar de imágenes propias).

**HEAD**: `090fa0c`
**Tag GitHub respaldo**: `sprint-paridad-2026-05-06-asador-codigo-listo`

---

## ✅ Trabajo cerrado hoy

### 1. Fix bug Sushi Bar (commit `9ed2ad7`)
La galería del Kit Tareas Sushi Bar usaba 8 referencias a imágenes de Chef Privado en HeroSection (×6), ContentGrid (×6), WhySection, BonusSection (×2), BuyBox y CtaFinal. John lo detectó visualmente.

Solución:
- 6 imágenes Nano Banana 2 generadas: `tareas-sushi-bar-{hero,barra,arroz,corte,equipo,emplatado}.jpg`
- Paths actualizados en los 6 componentes
- OG image `og-kit-tareas-sushi-bar.jpg` regenerada con hero real
- Memoria actualizada con **Bug #4** en `feedback_digital-products-non-negotiables.md`
- Coste: 6 × $0.0672 = $0.40
- LIVE en producción tras Netlify deploy

### 2. Kit Tareas Asador / Parrilla y Josper €14 (commit `090fa0c`)
Producto #2 del sprint, end-to-end:

**Slug**: `/kit-tareas-asador`
**Stripe env var**: `VITE_STRIPE_PAYMENT_LINK_TAREAS_ASADOR`
**Confirmation URL custom**: `https://aichef.pro/kit-tareas-asador-access?session_id={CHECKOUT_SESSION_ID}`

**Archivos creados (37 files / 933 insertions)**:
- 11 .xlsx en `public/dl/kit-tareas-asador/` (copiados desde `chefbusiness-astro`)
- 6 imágenes Nano Banana 2 en `public/lovable-uploads/ai-gallery/`: `tareas-asador-{hero,parrilla,josper,maduracion,equipo,emplatado}.jpg`
- `public/og-kit-tareas-asador.jpg` (copia de hero)
- 11 componentes en `src/components/kit-tareas-asador/`
- 3 pages: `KitTareasAsador.tsx`, `KitTareasAsadorAccessGate.tsx`, `KitTareasAsadorDashboard.tsx`
- `src/data/testimonials-asador.ts` (8 testimonios del nicho)
- Entry en `src/data/productos-digitales-config.ts` con 11 paths verificados (script no-negociable: 0 missing)
- 3 imports + 3 rutas en `src/App.tsx`
- Entry en `netlify/edge-functions/og-meta.ts`
- Tarjeta hub en `src/pages/ProductosDigitales.tsx` con icono `Beef`

**Validación**: type-check OK + production build OK (23.36s)

---

## 🚧 Acción pendiente de John (Asador)

### Stripe Payment Link
Texto canónico para copy/paste en el Payment Link Stripe:

```
Nombre: Kit de Tareas Recurrentes: Asador / Parrilla y Horno Josper — Checklists Operativos
Precio: 14,00 EUR (pago único)

Descripción:
11 checklists operativos pre-rellenados para asador, steakhouse y parrilla con horno Josper.
Incluye:
- Apertura y Cierre del Asador
- Protocolo del Horno Josper y Brasas
- Maduración Dry-age y Despiece de Carne
- Parrilla de Pescados y Verduras
- Tareas del Manager
- Perfiles: Parrillero y Equipo
- Semanales y Mensuales
- Eventos y Temporadas (calçotada, caza, Nochevieja)
- Plantilla Personalizable
- BONUS 1: Briefing de Servicio
- BONUS 2: Calendario Anual de Tareas

Compatible con Excel, Google Sheets, LibreOffice, Apple Numbers e imprimible A4.
Pago único, acceso de por vida, garantía 30 días.
```

**Confirmation URL custom (Stripe → Payment links → Confirmation page → Custom URL)**:
```
https://aichef.pro/kit-tareas-asador-access?session_id={CHECKOUT_SESSION_ID}
```

### Netlify env var
```
VITE_STRIPE_PAYMENT_LINK_TAREAS_ASADOR=https://buy.stripe.com/...
```

### Si Netlify no rebuildea solo
Avísame y hago `git commit --allow-empty -m "trigger Netlify rebuild"` para forzar la inyección de la env var en el bundle.

### Verificación
1. Visitar https://aichef.pro/kit-tareas-asador
2. Click en "COMPRAR AHORA — €14"
3. Debe abrir Stripe Checkout con el producto a €14. Si abre `#comprar` → la env var no se inyectó, forzar rebuild.

---

## 📋 Productos restantes del sprint (14 después de Asador)

### Bloque A — Kits Tareas restantes (mecánicas tras Asador)
| # | Slug AICP | Producto | Precio | Stripe env var |
|---|---|---|---|---|
| 3 | `/kit-tareas-marisqueria` | Kit Tareas Marisquería | €14 | `VITE_STRIPE_PAYMENT_LINK_TAREAS_MARISQUERIA` |
| 4 | `/kit-tareas-tapas-bar` | Kit Tareas Tapas Bar / Gastrobar | €14 | `VITE_STRIPE_PAYMENT_LINK_TAREAS_TAPAS_BAR` |
| 5 | `/kit-tareas-food-truck` | Kit Tareas Food Truck | €12 | `VITE_STRIPE_PAYMENT_LINK_TAREAS_FOOD_TRUCK` |
| 6 | `/kit-tareas-panaderia` | Kit Tareas Panadería / Obrador | €12 | `VITE_STRIPE_PAYMENT_LINK_TAREAS_PANADERIA` |

### Bloque B — Planes Negocio Línea A (5 productos)
| # | Slug | Producto | Precio | Env var |
|---|---|---|---|---|
| 7 | `/plan-negocio-bar-restaurante` | Plan Negocio Bar-Restaurante | €35 | `VITE_STRIPE_PAYMENT_LINK_PLAN_BAR_RESTAURANTE` |
| 8 | `/plan-negocio-tapas-bar` | Plan Negocio Tapas Bar / Gastrobar | €35 | `VITE_STRIPE_PAYMENT_LINK_PLAN_TAPAS_BAR` |
| 9 | `/plan-negocio-cafeteria` | Plan Negocio Cafetería / Brunch | €29 | `VITE_STRIPE_PAYMENT_LINK_PLAN_CAFETERIA` |
| 10 | `/plan-negocio-panaderia` | Plan Negocio Panadería / Obrador | €35 | `VITE_STRIPE_PAYMENT_LINK_PLAN_PANADERIA` |
| 11 | `/plan-negocio-food-truck` | Plan Negocio Food Truck | €29 | `VITE_STRIPE_PAYMENT_LINK_PLAN_FOOD_TRUCK` |

> Línea A NO tiene template canónico LIVE en AICP. El primer producto (Bar-Restaurante) será el template T1 — patrón distinto a los Kits Tareas.

### Bloque C — Planes Línea B Gastro Móvil (5 productos)
| # | Slug | Producto | Precio | Env var |
|---|---|---|---|---|
| 12 | `/plan-negocio-cocteleria-eventos` | Plan & Kit Coctelería de Eventos | €55 | `VITE_STRIPE_PAYMENT_LINK_PLAN_COCTELERIA` |
| 13 | `/plan-negocio-parrillero-asador-eventos` | Plan & Kit Parrillero / Asador Eventos | €45 | `VITE_STRIPE_PAYMENT_LINK_PLAN_PARRILLERO` |
| 14 | `/plan-negocio-paellero-eventos` | Plan & Kit Paellero / Paella Eventos | €45 | `VITE_STRIPE_PAYMENT_LINK_PLAN_PAELLERO` |
| 15 | `/plan-chef-privado-showcooking` | Plan & Kit Chef Privado / Showcooking | €45 | `VITE_STRIPE_PAYMENT_LINK_PLAN_CHEF_PRIVADO` |
| 16 | `/plan-catering-tematico-eventos` | Plan Catering & Kit Temático Eventos | €45 | `VITE_STRIPE_PAYMENT_LINK_PLAN_CATERING_TEMATICO` |

> Línea B usar Coctelería €55 como template canónico (9 entregables + 4 bonus, el más completo).

---

## 📋 Patrón mecánico actualizado (Asador como segunda referencia)

Para **cada Kit Tareas** del Bloque A, los pasos son los del SESSION_HANDOFF_2026-05-05.md + las 2 lecciones aprendidas hoy:

### Lección #1 — Bug del sed en clonación
Al clonar archivos React con sed, el reemplazo genérico `sushi-bar→<slug>` se ejecuta antes que los específicos `tareas-sushi-bar-<X>→tareas-<slug>-<Y>`. Resultado: las galerías quedan con nombres mal mapeados.

**Solución**: tras la clonación inicial, ejecutar un segundo sed que solo arregle los paths de imágenes específicas. Ejemplo Asador:
```bash
find src/components/kit-tareas-<slug> src/pages -maxdepth 2 -name "*.tsx" | xargs grep -l "tareas-<slug>-" 2>/dev/null | while read f; do
  sed -i '' \
    -e 's|tareas-<slug>-barra|tareas-<slug>-<imagen2>|g' \
    -e 's|tareas-<slug>-arroz|tareas-<slug>-<imagen3>|g' \
    -e 's|tareas-<slug>-corte|tareas-<slug>-<imagen4>|g' \
    "$f"
done
```

### Lección #2 — No-negociable galería propia
Generar SIEMPRE 6 imágenes específicas del nicho con Nano Banana 2 antes del commit. Documentado como **Bug #4** en `feedback_digital-products-non-negotiables.md`.

### Pasos canónicos refinados
1. `mkdir -p public/dl/kit-tareas-<slug> src/components/kit-tareas-<slug>`
2. `cp /Users/johnguerrero/chefbusiness-astro/public/dl/kit-tareas-<slug>/*.xlsx public/dl/kit-tareas-<slug>/`
3. **Generar 6 imágenes Nano Banana 2** del nicho específico (no reusar de otro producto)
4. Leer `chefbusiness-astro/src/pages/productos-digitales/kit-tareas-<slug>.astro` → extraer copy
5. Clonar con sed los 14 archivos del template Sushi Bar (o ahora Asador) sustituyendo slug
6. **Segundo sed para fix de paths de imágenes específicas**
7. Editar copy específico en: testimonials, ContentGrid templates+icons+subtitle, HeroSection (h1+subtitle+checkItems), WhySection (reasons+icons), AuthorSection (bio), BonusSection (BONUS desc), FaqAccordion (6 FAQs), CtaFinal (items+heading+CTA), BuyBox (CTA), GuaranteeSection (paragraph), StickyBar (label), KitTareas<Slug>.tsx (Helmet+SEO+JSON-LD+breadcrumb+TestimonialsMarquee subtitle), KitTareas<Slug>Dashboard.tsx (TEMPLATES keys+icons+desc + h1 + p)
8. Editar `src/data/productos-digitales-config.ts` (entry con 11 files paths)
9. Editar `src/App.tsx` (3 imports + 3 routes)
10. Editar `netlify/edge-functions/og-meta.ts` (entry SEO)
11. Editar `src/pages/ProductosDigitales.tsx` (tarjeta hub con icono lucide adecuado)
12. Verificar paths con script no-negociable (`MISSING: 0`)
13. `npx tsc --noEmit && npm run build`
14. Commit + push con mensaje canónico
15. Entregar a John: Stripe descripción + Confirmation URL + Env var name

---

## ⚠️ Recordar al retomar

1. **Verificar Asador en producción primero**: `https://aichef.pro/kit-tareas-asador` debe abrir Stripe Checkout al pulsar "COMPRAR".
2. **Si Stripe no abre**: revisar si John ya cargó la env var. Si sí, hacer commit vacío para forzar rebuild.
3. **Si John ya configuró todo**: actualizar memoria + tabla de productos LIVE con el Stripe link real, y arrancar Marisquería.

---

## 📋 Mensaje exacto para arrancar próxima sesión

> "Continuamos sprint paridad CB→AICP. Cerrado ayer 2026-05-06: producto #2 Kit Tareas Asador código LIVE (commit `090fa0c`). Antes de arrancar producto #3 (Marisquería €14, slug `/kit-tareas-marisqueria`, env `VITE_STRIPE_PAYMENT_LINK_TAREAS_MARISQUERIA`), comprueba en https://aichef.pro/kit-tareas-asador que el botón "COMPRAR" abre Stripe Checkout — si no, revisa si John ya cargó la env var en Netlify y haz commit vacío si hace falta. Lee `SESSION_HANDOFF_2026-05-06.md` para el patrón mecánico actualizado (incluye lección del sed bug y no-negociable de galería propia). Adelante."

---

## Coste sesión

- Sushi Bar fix: 6 imágenes × $0.0672 = $0.40
- Asador nuevo: 6 imágenes × $0.0672 = $0.40
- **Total: $0.81**

## Tags GitHub de respaldo

- `sprint-paridad-2026-05-06-asador-codigo-listo` (apunta a `090fa0c`)

## Commits clave de la sesión

- `9ed2ad7` — fix(sushi-bar): 6 imágenes propias
- `090fa0c` — feat(productos): port Kit Tareas Asador €14
