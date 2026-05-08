# Session Handoff — 2026-05-08 → 2026-05-09

## Estado del proyecto al cerrar el día

Sprint paridad bidireccional CB↔AICP. **Bloque A (Kits Tareas) cerrado al 100%** con los 6 productos LIVE. Quedan los Bloques B y C (10 Planes de Negocio) por arrancar.

---

## Productos cerrados hoy (2026-05-08)

### #5 Kit Tareas Food Truck (€12) — LIVE

- **Slug**: `/kit-tareas-food-truck`
- **Stripe Payment Link**: `https://buy.stripe.com/6oU8wIbcE0JU4Z16Rf6oo12`
- **Env var Netlify**: `VITE_STRIPE_PAYMENT_LINK_TAREAS_FOOD_TRUCK`
- **Commits hoy**:
  - `d2a52e5` rebuild trigger para inyectar env var
  - `d377e66` fix imágenes (8 refs `tareas-bar-*` → 6 imgs `use-case-food-truck-*` reusadas, coste $0)
- Anoche durante el apagón ya se había commiteado el código en `f4c3e4c`. Hoy se cerró con Stripe + rebuild + fix de placeholders Bar.

### #6 Kit Tareas Panadería / Obrador (€12) — LIVE

- **Slug**: `/kit-tareas-panaderia`
- **Stripe Payment Link**: `https://buy.stripe.com/6oUbIUdkM9gqajldfD6oo13`
- **Env var Netlify**: `VITE_STRIPE_PAYMENT_LINK_TAREAS_PANADERIA`
- **Commits hoy**:
  - `c3aaf0a` código completo end-to-end (31 files, 935 insertions)
  - `da8f004` rebuild trigger para inyectar env var
- Reusa las 6 imgs `use-case-panadero-*` ya producidas (coste imágenes: $0).
- Cierra Bloque A del sprint paridad (los 6 Kits Tareas portados de CB).
- Bug fix incluido en el commit del producto: el card de Food Truck en el hub `/productos-digitales` seguía apuntando a `tareas-bar-hero.jpg` → corregido a `use-case-food-truck-hero.jpg`.

---

## Sprint paridad CB→AICP — Estado completo

| # | Producto | Precio | Status |
|---|---|---|---|
| 1 | Sushi Bar | €14 | LIVE (sesión 2026-05-05) |
| 2 | Asador / Parrilla y Josper | €14 | LIVE (sesión 2026-05-06) |
| 3 | Marisquería | €14 | LIVE (sesión 2026-05-07) |
| 4 | Tapas Bar / Gastrobar | €14 | LIVE (sesión 2026-05-07) |
| 5 | Food Truck | €12 | **LIVE (cerrado hoy)** |
| 6 | Panadería / Obrador | €12 | **LIVE (cerrado hoy)** |

**Bloque A: 6/6 ✅ COMPLETO**

---

## Stash pendiente — refactor Netlify functions

Existe un refactor sin commitear desde antes del apagón del 2026-05-07. Está guardado en `git stash@{0}` con mensaje descriptivo. **No se ha mergeado a main porque toca las 4 funciones de cobro/acceso y el incidente Alfonso del 2026-04-29 sigue fresco** — necesita verificación runtime manual antes de tocar producción.

### Qué hace el refactor

Centraliza metadata por producto en `src/data/productos-digitales-config.ts` (que ya estaba en HEAD con todos los campos: `priceLabel`, `accessPath`, `emailSubject`, `emailTitle`, `emailBodyPostPurchase`, `emailCta`, `emailTitleResend`, `emailBodyResend`, `files`, plus `PRODUCTS_CONFIG`, `PRODUCT_IDS`, `DEFAULT_PRODUCT_ID`, `SPECIAL_DOWNLOAD_PRODUCTS`).

Los 5 archivos consumidores se simplifican drásticamente al consumir todo desde el config en lugar de tener `if/else` por producto:

| Archivo | HEAD líneas | Refactor líneas | Reducción |
|---|---|---|---|
| `netlify/functions/get-download-urls.ts` | 612 | 67 | -545 |
| `netlify/functions/verify-purchase.ts` | 324 | 124 | -200 |
| `netlify/functions/admin-generate-access.ts` | 120 | 89 | -31 |
| `netlify/functions/resend-access.ts` | 138 | 99 | -39 |
| `src/pages/AdminGenerateAccess.tsx` | 217 | 191 | -26 |

**Total**: 5 archivos, -841 / +35 líneas.

### Estado de validación
- `npx tsc --noEmit`: pasa sin errores ✅
- `npm run build`: pasa (28s) ✅
- **Runtime**: NO probado en producción.

### Cómo retomar mañana

```bash
git stash apply stash@{0}        # No usar `pop` hasta validar
npm run build                    # Re-verificar build
# QA manual antes de commit:
#  1. /admin/generar-acceso aún funciona (probar con un producto activo)
#  2. Magic link de email aún se envía con HTML correcto
#  3. /<producto>-access?session_id=cs_test_... verifica pago y crea JWT
#  4. Dashboard descarga el .xlsx correcto desde el JWT
git diff                         # Auditar cambios antes de commitear
git stash drop                   # Solo cuando todo OK
```

Si tras la validación falla algo o decidimos descartar el refactor: `git stash drop stash@{0}` y se acabó.

---

## Pendientes para mañana 2026-05-09

### 9 productos CB-only restantes en aichef.pro

#### Bloque B — Planes Negocio Línea A (5 productos €29-35) — **AICP no tiene NINGUNO LIVE**
| # | Slug AICP | Producto | Precio | Stripe env var name |
|---|---|---|---|---|
| 7 | `/plan-negocio-bar-restaurante` | Plan Negocio Bar-Restaurante | €35 | `VITE_STRIPE_PAYMENT_LINK_PLAN_BAR_RESTAURANTE` |
| 8 | `/plan-negocio-tapas-bar` | Plan Negocio Tapas Bar / Gastrobar | €35 | `VITE_STRIPE_PAYMENT_LINK_PLAN_TAPAS_BAR` |
| 9 | `/plan-negocio-cafeteria` | Plan Negocio Cafetería / Brunch | €29 | `VITE_STRIPE_PAYMENT_LINK_PLAN_CAFETERIA` |
| 10 | `/plan-negocio-panaderia` | Plan Negocio Panadería / Obrador | €35 | `VITE_STRIPE_PAYMENT_LINK_PLAN_PANADERIA` |
| 11 | `/plan-negocio-food-truck` | Plan Negocio Food Truck | €29 | `VITE_STRIPE_PAYMENT_LINK_PLAN_FOOD_TRUCK` |

> El primero (Bar-Restaurante €35) será el **template canónico T1** para los otros 4. Patrón distinto al de los Kits Tareas — usar template T1 del Excel `Mapa_Contenidos_00_Doctrina_y_Templates.xlsx`.

#### Bloque C — Planes Línea B Gastro Móvil (5 productos €45-55) — **AICP no tiene NINGUNO LIVE**
| # | Slug AICP | Producto | Precio | Stripe env var |
|---|---|---|---|---|
| 12 | `/plan-negocio-cocteleria-eventos` | Plan & Kit Coctelería Eventos / Barra Móvil | €55 | `VITE_STRIPE_PAYMENT_LINK_PLAN_COCTELERIA` |
| 13 | `/plan-negocio-parrillero-asador-eventos` | Plan & Kit Parrillero / Asador Eventos | €45 | `VITE_STRIPE_PAYMENT_LINK_PLAN_PARRILLERO` |
| 14 | `/plan-negocio-paellero-eventos` | Plan & Kit Paellero / Paella Eventos | €45 | `VITE_STRIPE_PAYMENT_LINK_PLAN_PAELLERO` |
| 15 | `/plan-chef-privado-showcooking` | Plan & Kit Chef Privado / Showcooking | €45 | `VITE_STRIPE_PAYMENT_LINK_PLAN_CHEF_PRIVADO` |
| 16 | `/plan-catering-tematico-eventos` | Plan Catering & Kit Temático Eventos | €45 | `VITE_STRIPE_PAYMENT_LINK_PLAN_CATERING_TEMATICO` |

> Coctelería €55 es el más completo (9 entregables + 4 bonus); template canónico Línea B.

### Decisión a tomar al arrancar
Tres opciones discutidas hoy al cierre — sin decisión final:
1. **Bloque B primero** (Plan Negocio Bar-Restaurante €35) → estrena Plan Línea A.
2. **Bloque C primero** (Coctelería €55) → mayor ticket, template más completo.
3. **Cerrar el refactor pendiente primero** → validación runtime + commit aislado, después abrir nueva línea.

---

## No-negociables anti-bugs (incidente Alfonso 2026-04-29) — siguen vigentes

Antes de hacer commit de cualquier producto:
1. **Paths reales**: cada path en `productos-digitales-config.ts > files` debe existir físicamente en `public/dl/<slug>/`. Verificar con `ls public/dl/<slug>/`. El SPA fallback de Netlify oculta los 404 (devuelve `index.html` con HTTP 200).
2. **Access gate compartido**: usar `<ProductAccessGate>` de `@/components/shared/`, nunca rehacer la lógica.
3. **storageKey único**: en AccessGate y ProtectedRoute (formato `<slug>-jwt`).
4. **Acceso manual disponible**: el admin tool en `/admin/generar-acceso` se autopopula del config — ya cubierto al añadir entrada al config.
5. **Stripe descripción**: párrafo en prosa de ~260 caracteres, **NUNCA bullet points** (se truncan en dashboard/checkout/recibos). Ver memoria `feedback_stripe-descripcion-formato.md`.

---

## Archivos de referencia clave

- **Catálogo Excel maestro**: `/Users/johnguerrero/productos-digitales/Catalogo_Productos_Digitales_ChefBusiness_AIChefPro_RoadmapExpansion.xlsx`
- **Doctrina + 7 templates de cluster**: `/Users/johnguerrero/productos-digitales/Mapa_Contenidos_00_Doctrina_y_Templates.xlsx`
- **Repo CB (Astro)**: `/Users/johnguerrero/chefbusiness-astro/`
- **Repo AICP (este, React+Vite)**: `/Users/johnguerrero/chefpro-modernize/`
- **Plantilla canónica AICP de Kit Tareas (última validada)**: `KitTareasPanaderia*.tsx` + `src/components/kit-tareas-panaderia/` + `src/data/testimonials-panaderia.ts` (commit `c3aaf0a`)
- **Para Bloque B/C**: NO hay template canónico AICP todavía — el primer Plan Negocio que portemos creará el patrón.

---

## Mensaje exacto para arrancar mañana

> "Continuamos sprint paridad CB→AICP. Cerrado **Bloque A: 6/6 Kits Tareas LIVE** (último commit `da8f004` activando Panadería). Lee `SESSION_HANDOFF_2026-05-08.md` para el contexto completo del día y los pendientes. **Decisión a tomar antes de arrancar**: (1) Bloque B con Plan Negocio Bar-Restaurante €35, (2) Bloque C con Coctelería €55, o (3) cerrar primero el refactor que dejé en `git stash@{0}` con QA runtime antes de mergear. Mi recomendación es opción 3 (refactor) si quieres limpiar deuda técnica ya, o opción 1 (Bloque B Bar-Restaurante) si prefieres seguir abriendo línea de producto. ¿Cuál?"
