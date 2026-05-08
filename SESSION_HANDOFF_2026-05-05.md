# Session Handoff — 2026-05-05 → 2026-05-06

## Estado del proyecto al cerrar el día

**Sprint en curso**: Paridad bidireccional de productos digitales entre `chefbusiness.co` y `aichef.pro`. Mi rol (Claude Code en `/Users/johnguerrero/chefpro-modernize`) es portar **16 productos CB-only a aichef.pro**. El otro terminal (Claude Code en `/Users/johnguerrero/chefbusiness-astro`) porta los 11 AICP-only a CB.

**Modo de trabajo acordado**:
- Un producto a la vez, end-to-end, sin testing manual con tarjetas Stripe de prueba.
- Yo escribo código + assets + commit + push. John crea Stripe Payment Link + carga la env var Netlify en paralelo.
- Cuando John pega el `https://buy.stripe.com/...`, basta con que Netlify rebuilde (las vars `VITE_*` se inyectan en build-time). No hay edición manual del código adicional.
- Si la variable se carga DESPUÉS del primer deploy del producto, hace falta forzar rebuild (commit vacío sirve).

---

## ✅ Producto cerrado hoy: Kit Tareas Sushi Bar (€14)

- **Slug**: `/kit-tareas-sushi-bar`
- **Stripe Payment Link**: `https://buy.stripe.com/14AfZa94w2S20IL1wV6oo0X` ← creado por John
- **Netlify env var**: `VITE_STRIPE_PAYMENT_LINK_TAREAS_SUSHI_BAR` ← cargada por John
- **Commit del código**: `45e065a` — "feat(productos): port Kit Tareas Sushi Bar (€14) from chefbusiness.co"
- **Commit trigger rebuild**: `da8baae` — empty commit para forzar inyección de la env var en el bundle
- **Status producto**: LIVE en producción tras Netlify deploy del commit `da8baae` (en construcción al cerrar la sesión).

### Verificar mañana al arrancar
1. Visitar https://aichef.pro/kit-tareas-sushi-bar
2. View source → buscar `buy.stripe.com/14AfZa94w2S20IL1wV6oo0X` en el HTML/JS — si aparece, botón conectado.
3. Si NO aparece, hacer otro `git commit --allow-empty -m "trigger" && git push` o usar "Trigger deploy → Clear cache and deploy site" en Netlify.

### Lista completa de archivos creados (31 files / 1860 insertions)
- `public/dl/kit-tareas-sushi-bar/` — 11 .xlsx (copiados desde CB)
- `public/og-kit-tareas-sushi-bar.jpg` — placeholder reusando OG de Chef Privado (PENDIENTE generar imagen real con Nano Banana 2)
- `src/pages/KitTareasSushiBar.tsx` (landing)
- `src/pages/KitTareasSushiBarAccessGate.tsx`
- `src/pages/KitTareasSushiBarDashboard.tsx`
- `src/components/kit-tareas-sushi-bar/` — 11 componentes (HeroSection, ContentGrid, WhySection, AuthorSection, BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar, FadeIn)
- `src/data/testimonials-sushi-bar.ts` — 8 testimonios
- Editado: `src/data/productos-digitales-config.ts` (+ entrada `kit-tareas-sushi-bar`)
- Editado: `src/App.tsx` (+ 3 imports + 3 rutas)
- Editado: `netlify/edge-functions/og-meta.ts` (+ entrada SEO)
- Editado: `src/pages/ProductosDigitales.tsx` (+ tarjeta hub con icono `Fish`)

---

## 🚧 Pendientes para mañana 2026-05-06 — 15 productos CB-only restantes

### Lista en orden recomendado de ejecución

#### Bloque A — Resto de Kits Tareas (réplicas mecánicas tras Sushi Bar)
| # | Slug AICP a crear | Producto | Precio | Stripe env var name | Material en CB |
|---|---|---|---|---|---|
| 1 | `/kit-tareas-asador` | Kit Tareas Asador / Parrilla y Josper | €14 | `VITE_STRIPE_PAYMENT_LINK_TAREAS_ASADOR` | `chefbusiness-astro/public/dl/kit-tareas-asador/` (11 xlsx) + `kit-tareas-asador.astro` (1230 líneas) |
| 2 | `/kit-tareas-marisqueria` | Kit Tareas Marisquería | €14 | `VITE_STRIPE_PAYMENT_LINK_TAREAS_MARISQUERIA` | `chefbusiness-astro/public/dl/kit-tareas-marisqueria/` |
| 3 | `/kit-tareas-tapas-bar` | Kit Tareas Tapas Bar / Gastrobar | €14 | `VITE_STRIPE_PAYMENT_LINK_TAREAS_TAPAS_BAR` | `chefbusiness-astro/public/dl/kit-tareas-tapas-bar/` |
| 4 | `/kit-tareas-food-truck` | Kit Tareas Food Truck | €12 | `VITE_STRIPE_PAYMENT_LINK_TAREAS_FOOD_TRUCK` | `chefbusiness-astro/public/dl/kit-tareas-food-truck/` |
| 5 | `/kit-tareas-panaderia` | Kit Tareas Panadería / Obrador | €12 | `VITE_STRIPE_PAYMENT_LINK_TAREAS_PANADERIA` | `chefbusiness-astro/public/dl/kit-tareas-panaderia/` |

#### Bloque B — Planes Negocio Línea A (5 productos €29-35)
| # | Slug AICP | Producto | Precio | Stripe env var |
|---|---|---|---|---|
| 6 | `/plan-negocio-bar-restaurante` | Plan Negocio Bar-Restaurante | €35 | `VITE_STRIPE_PAYMENT_LINK_PLAN_BAR_RESTAURANTE` |
| 7 | `/plan-negocio-tapas-bar` | Plan Negocio Tapas Bar / Gastrobar | €35 | `VITE_STRIPE_PAYMENT_LINK_PLAN_TAPAS_BAR` |
| 8 | `/plan-negocio-cafeteria` | Plan Negocio Cafetería / Brunch | €29 | `VITE_STRIPE_PAYMENT_LINK_PLAN_CAFETERIA` |
| 9 | `/plan-negocio-panaderia` | Plan Negocio Panadería / Obrador | €35 | `VITE_STRIPE_PAYMENT_LINK_PLAN_PANADERIA` |
| 10 | `/plan-negocio-food-truck` | Plan Negocio Food Truck | €29 | `VITE_STRIPE_PAYMENT_LINK_PLAN_FOOD_TRUCK` |

> **Aviso**: AICP no tiene NINGÚN Plan de Negocio Línea A LIVE actualmente. El primero (Bar-Restaurante) será template canónico para los otros 4. Patrón base distinto al de los Kits Tareas — usar template T1 del Excel `Mapa_Contenidos_00_Doctrina_y_Templates.xlsx`.

#### Bloque C — Planes Línea B Gastro Móvil (5 productos €45-55)
| # | Slug AICP | Producto | Precio | Stripe env var |
|---|---|---|---|---|
| 11 | `/plan-negocio-cocteleria-eventos` | Plan & Kit Coctelería de Eventos / Barra Móvil | €55 | `VITE_STRIPE_PAYMENT_LINK_PLAN_COCTELERIA` |
| 12 | `/plan-negocio-parrillero-asador-eventos` | Plan & Kit Parrillero / Asador Eventos | €45 | `VITE_STRIPE_PAYMENT_LINK_PLAN_PARRILLERO` |
| 13 | `/plan-negocio-paellero-eventos` | Plan & Kit Paellero / Paella Eventos | €45 | `VITE_STRIPE_PAYMENT_LINK_PLAN_PAELLERO` |
| 14 | `/plan-chef-privado-showcooking` | Plan & Kit Chef Privado / Showcooking | €45 | `VITE_STRIPE_PAYMENT_LINK_PLAN_CHEF_PRIVADO` |
| 15 | `/plan-catering-tematico-eventos` | Plan Catering & Kit Temático Eventos | €45 | `VITE_STRIPE_PAYMENT_LINK_PLAN_CATERING_TEMATICO` |

> AICP tampoco tiene planes Línea B Gastro Móvil. Coctelería €55 es el más completo (9 entregables + 4 bonus); usarlo como template canónico Línea B.

---

## 📋 Patrón mecánico validado (Sushi Bar como plantilla canónica)

Para **cada Kit Tareas** (Bloque A) — pasos exactos:

1. `mkdir -p public/dl/kit-tareas-<slug> src/components/kit-tareas-<slug>`
2. `cp /Users/johnguerrero/chefbusiness-astro/public/dl/kit-tareas-<slug>/*.xlsx public/dl/kit-tareas-<slug>/`
3. Leer `chefbusiness-astro/src/pages/productos-digitales/kit-tareas-<slug>.astro` (1200+ líneas) → extraer: title, description, checkItems, categories (11), foodGallery, testimonials (8), ctaItems, faqs (6), schema price.
4. Crear 14 archivos React replicando estructura `src/components/kit-tareas-sushi-bar/` y `src/pages/KitTareasSushiBar*.tsx`.
5. Editar:
   - `src/data/productos-digitales-config.ts` (+ entrada con files)
   - `src/App.tsx` (+ import + 3 rutas)
   - `netlify/edge-functions/og-meta.ts` (+ entrada `/kit-tareas-<slug>`)
   - `src/pages/ProductosDigitales.tsx` (+ tarjeta hub, importar icono lucide adecuado)
6. `cp public/og-kit-tareas-chef-privado.jpg public/og-kit-tareas-<slug>.jpg` (placeholder; regenerar después con Nano Banana 2)
7. `npx tsc --noEmit && npm run build` para validar
8. Commit + push con mensaje canónico:
   ```
   feat(productos): port Kit Tareas <Producto> (€<precio>) from chefbusiness.co
   
   <breve resumen del nicho específico>
   
   Pending: Stripe Payment Link + Netlify env <VAR_NAME>.
   ```
9. Entregar a John:
   - **Stripe descripción** (markdown listo para copy/paste, ver más abajo template).
   - **Confirmation URL**: `https://aichef.pro/kit-tareas-<slug>-access?session_id={CHECKOUT_SESSION_ID}`
   - **Env var name**.

10. Cuando John confirme `https://buy.stripe.com/...` y env var cargada → si Netlify no rebuildea solo, hacer commit vacío para forzar.

### Template canónico para Stripe descripción (Kit Tareas)
```
Nombre: Kit de Tareas Recurrentes: <Producto> — Checklists Operativos
Precio: <X>,00 EUR (pago único)

Descripción:
11 checklists operativos pre-rellenados para <nicho>.
Incluye:
- <Categoría 1>
- <Categoría 2>
- ...
- BONUS: Briefing de Servicio + Calendario Anual

Compatible con Excel, Google Sheets, LibreOffice, Apple Numbers e imprimible A4.
Pago único, acceso de por vida, garantía 30 días.

Confirmation URL custom: https://aichef.pro/kit-tareas-<slug>-access?session_id={CHECKOUT_SESSION_ID}
```

---

## ⚠️ No-negociables anti-bugs (incidente Alfonso 2026-04-29)

Antes de hacer commit de cualquier producto:
1. **Paths reales**: cada path en `productos-digitales-config.ts > files` debe existir físicamente en `public/dl/<slug>/`. Verificar con `ls public/dl/<slug>/`. El SPA fallback de Netlify oculta los 404 (devuelve `index.html` con HTTP 200).
2. **Access gate compartido**: usar `<ProductAccessGate>` de `@/components/shared/`, nunca rehacer la lógica.
3. **storageKey único**: en AccessGate y ProtectedRoute (formato `<slug>-jwt`).
4. **Acceso manual disponible**: el admin tool en `/admin/generar-acceso` se autopopula del config — ya cubierto al añadir entrada al config.

Ver memoria: `feedback_digital-products-non-negotiables.md` y `session-2026-04-29-access-gates-fix.md`.

---

## 📁 Archivos de referencia clave

- **Catálogo Excel maestro**: `/Users/johnguerrero/productos-digitales/Catalogo_Productos_Digitales_ChefBusiness_AIChefPro_RoadmapExpansion.xlsx`
- **Doctrina + 7 templates de cluster**: `/Users/johnguerrero/productos-digitales/Mapa_Contenidos_00_Doctrina_y_Templates.xlsx`
- **Mapa Fase 1 (176 artículos planificados)**: `/Users/johnguerrero/productos-digitales/Mapa_Contenidos_01_Fase1_Productos_LIVE.xlsx`
- **Repo CB (Astro)**: `/Users/johnguerrero/chefbusiness-astro/`
- **Repo AICP (este, React+Vite)**: `/Users/johnguerrero/chefpro-modernize/`
- **Plantilla canónica AICP de Kit Tareas**: `KitTareasChefPrivado*.tsx` + `src/components/kit-tareas-chef-privado/` + `src/data/testimonials-chef-privado.ts`
- **Producto LIVE recién portado (referencia exacta)**: `KitTareasSushiBar*.tsx` + `src/components/kit-tareas-sushi-bar/` + `src/data/testimonials-sushi-bar.ts`

---

## 🎯 Mensaje exacto para arrancar mañana

> "Continuamos con la paridad CB→AICP. Ya quedó cerrado **Kit Tareas Sushi Bar** (LIVE en aichef.pro tras commit `da8baae`). Hoy arrancamos con **Kit Tareas Asador / Parrilla y Josper €14** siguiendo el patrón mecánico de Sushi Bar. Lee `SESSION_HANDOFF_2026-05-05.md` para todo el contexto: lista completa de los 15 productos pendientes, patrón a aplicar y no-negociables anti-bugs. Adelante."

