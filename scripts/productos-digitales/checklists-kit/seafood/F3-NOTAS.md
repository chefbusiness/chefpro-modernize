# Seafood Restaurant Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 31-oct-2026. Tercero y último de los kits de MOLDE PLANO de la F3 conjunta (`../foodtruck/F3-NOTAS.md`
> tiene el contexto y el método). Rama `feat/checklists-en-lote-4`. Molde: la F3 del Taco Shop (#188) punto por punto.
> Sin build, Playwright ni navegador (CPU 42-46 °C).

## 0. Para John: el Payment Link (punto 12)

| Campo | Valor |
|---|---|
| Producto Stripe | **Seafood Restaurant Checklists Kit Pro** |
| Precio | **$15 USD**, pago único |
| Redirección tras el pago | `https://aichef.pro/en/digital-products/seafood-restaurant-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` |
| Env (scope builds, todos los contextos) | `VITE_STRIPE_PAYMENT_LINK_SEAFOOD_RESTAURANT_CHECKLISTS_KIT` |
| Después | `python3 scripts/productos-digitales/sync-payment-links.py` y `--check` |

Descripción para Stripe (prosa): «Excel checklists for seafood restaurants with 165 tasks already written: opening and
closing, the live tank and seafood receiving, HACCP and traceability with shellfish tags, the raw bar and ice display, the
manager, duties by role, weekly and monthly upkeep, US seafood seasons, a pre-shift meeting template and a 12-month US
calendar. Lifetime access to the dashboard.»

## 1. Puntos de registro (los 25 del Taco Shop, para `seafood-restaurant-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla | `KitTareasLandingPage.astro` | sin cambios; sin flag |
| 2 | Ficha EN | `astro-site/src/data/productos-en/tareas/seafood-restaurant-checklist-templates.ts` | ✅ $15, sin anclas ni rating; 9 plantillas + 3 bonus, 22 FAQ on-page + 6 en el JSON-LD, 8 testimonios sin marcas |
| 3-5 | Landing, `/access`, `/library`, island, dashboard | `pages/en/digital-products/seafood-restaurant-checklist-templates{.astro,/access.astro,/library.astro}`, `islands/library/SeafoodRestaurantChecklistsKitLibraryIsland.tsx`, `src/pages/SeafoodRestaurantChecklistsKitDashboard.tsx` | ✅ copias del Taco Shop; 12 tarjetas con las claves e iconos del ES (02 = `vivero-lonjas`); cruza a Restaurant Checklists Kit Pro, HACCP Food Safety Kit Pro y Food Cost Kit Pro (el ES: Kit Tareas Restaurante, Chef Privado y Pack APPCC) |
| 6 | Gemelo ES | `pages/kit-tareas-marisqueria.astro` → `alternatesFamilia('kit-tareas-marisqueria')` | ✅ (solo el `<head>`: `--esperadas /kit-tareas-marisqueria`) |
| 7 | Familia `kit-tareas-marisqueria` → `en: …, vivo: true` | `lib/tienda.ts` | ✅ (fusionar con el link) |
| 8-10 | Zona app, verify/resend, descargas + config | `zona-app.ts`, `verify-purchase.ts`, `resend-access.ts`, `get-download-urls.ts`, `productos-digitales-config.ts` | ✅ 11 xlsx de SPEC §2 + `equivalents-guide`; `gate-flujo-postpago --offline`: 12 = 12 |
| 11 | Precio `{ usd: 15 }` | `product-prices.ts` | ✅ `--check` verde (95) |
| 12 | Payment Link | — | ⏳ John (§0) |
| 13-16 | Admin, changelog v1.1, catálogos, alias | `admin-generate-access.ts`, `AdminGenerateAccess.tsx`, `productos-changelog.ts`, `products-catalog.ts`, `digital-products-catalogue.json`, `linkify-use-case.ts/.tsx` | ✅ |
| 17 | Hub EN | `DigitalProductsHubPage.astro` | ✅ «Recurring Tasks: Seafood Restaurant with Live Tanks & HACCP» sube a la 1 con copy EN (decía «EU allergen rules», «fish markets» y «Official Spanish fishing seasons»); orden final arriba: Seafood, Bakery, Food Truck, Taco Shop…; Mega Pack el último |
| 18 | `footerLinks` | 14 fichas de checklists (11 + Taco Shop, Food Truck, Bakery) y 5 kits (HACCP y Restaurant Checklists incluidos) | ✅ sin plan hermano EN (no hay plan de marisquería); la ficha enlaza el Restaurant Business Plan Kit |
| 19 | GEO | `llms.txt` y `llms-full.txt` («37 products») | ✅ |
| 20 | Sitemap | `sitemap-lastmod.json` | ✅ 2026-10-31 |
| 21-22 | Blog EN | — | ❌ otra sesión |
| 23 | `tienda-gate.py` | comentario de `--esperadas` + exento «Kit de Tareas Recurrentes: Marisquería con Vivero y APPCC» | ✅ estático verde (38 vivos fuera de ES) |
| 24 | Correo EN | `emails/broadcast-seafood-restaurant-checklists-lanzamiento-en.{html,subject.txt}` | ✅ SIN PROGRAMAR; «Hi everyone,», #111 + #FFD700, $15; imagen = la nueva del vivero |
| 25 | Cripto + devoluciones | plantilla | ✅ estático (`CRYPTO_PRODUCTS=all`, fuera de `EXCLUDE`, `{ usd: 15 }`) |

## 2. Verificación (ligera, sin build)

- Cifras contra `revision/dump_en.txt` y los xlsx (openpyxl): 11 libros de una hoja, **165 tareas** (01 30 = 21 de apertura
  + 9 de cierre, de 7:00 AM a 11:45 PM · 02 21 = 7 + 7 + 7 con columna «Reading» · 03 17 = 6 + 5 + 6 con 5 CCP · 04 19 = 7 +
  7 + 5 · 05 18 · 06 25 = 5 × 5 · 07 17 = 9 + 8 · 08 18 = 8 + 6 + 4), B01 de 13 campos, B02 de 12 meses, Letter, sin
  proteger, desplegable en 01-04 y 06-08. °F de la ficha (−31, −4, 0, 41, 45, 50, 70, 145) ⊂ los de los xlsx; cifras
  (6 mg/L, 30–35 ppt, pH 7.5–8.5, 90 min, 2 h, 48 h, < 32 %, 15 h / 24 h / 7 days, EPA 608) presentes en el volcado.
- `tienda-gate.py` estático verde; `sync-product-prices --check` verde; `gate-flujo-postpago --offline --only
  seafood-restaurant-checklist-templates`: 12 = 12, falla SOLO «SIN Payment Link»; esbuild 0 errores.
- Cierre conjunto (ver `../foodtruck/F3-NOTAS.md` §2): ES idénticas 40/40, render EN sin fallos de `revisar_texto`. **Auditoría adversarial:** arreglados el testimonio de Ana García (las vedas están en el 08, no en el calendario, y la gamba del kit EN es de todo el año → «frozen lobster tails … fresh lobster season»), «a column for each reading», «lot log» / «parasite-destruction record» como si fueran hojas (son filas que mandan llevarlos: → «lot traceability», «record kept 90 days»; keywords sin «receiving log» ni «tag log»), la repetición del testimonio de Carlos Méndez, «the tank checked overnight» (al cierre), el walk-in de vivos «a 0 °F», «receiving … twice a day» (en cada entrega), la destrucción de parásitos bajo la barra de crudos (es el PCC 5 del 03), «11 Excel checklists» y «Manager checklists».

## 3. Decisiones de contenido

- **Molde plano:** fuera contador, N/A que descuenta, celdas verdes, filas libres, protección, iniciales, firma y versión
  dentro; sí la HORA de cada tarea del 01 y la columna «Reading» del 02.
- **Fuera lo que el ES promete y el kit no trae:** cifras del vivero por especie (8-12 / 14-18 °C: la FAQ explica por qué
  el kit deja el hueco), «densidad de carga», lonja y subasta, UE 1379/2013, zona FAO, RD 1021/2022, «alérgenos 2 y 14»,
  temporadas y vedas de España, percebe y gamba roja, «origen obligatorio por ley» (→ house standard), arqueo como hoja,
  «cierres por vacaciones», «por menos de una mariscada», «€40/mes», «Imprimible A4», guía ES↔LatAm, FAQ de Google Sheets.
- **SEO (SPEC D2):** title «…: Raw Bar, Receiving & Opening Checklist Templates for Excel»; FAQ arriba: opening (intención
  «restaurant opening checklist», 260/mes), closing, raw bar setup, shellfish tags (90 días), receiving; luego vivero,
  HACCP, crudo, histamina, alérgenos (moluscos no son de los 9), temporadas US orientativas.
- **Testimonios:** los 8 del ES con el subtítulo de la edición española. **Frases cambiadas** (regla de John, 11-oct):
  Alejandro Ruiz («densidad de carga» → pH), María López («zona FAO» → harvest area; «reglamento UE» → «stay compliant»),
  David Torres («lonjas, temporadas de pesca» → «receiving, the seasons»), Ana García (temporadas y vedas de España, lonja
  y gamba roja → «seafood seasons and closures», «orders», «the fresh season»). **Avatares:** jefe de cocina → chef-avatar-1
  (chaquetilla; no el chaleco de bar), jefa de sala → avatar-6 (sala), encargada → avatar-4.
- **Imágenes:** de las 6 del ES, la del vivero («VIVERO CENTOLLOS Y BOGAVANTES») y la del expositor («OSTRAS / PERCEBES /
  NAVAJAS…») llevan texto en español y la del equipo el bordado «MADRID» → fuera. Se quedan hero, mariscos y emplatado;
  entran `guia-peruano-plato.jpg` (ceviche) y `tareas-sushi-bar-corte.jpg` (corte de pescado), reutilizadas, y **una
  nueva** sin texto: `ai-gallery/tareas-seafood-en-live-tank.jpg` (Nano Banana 2, 1376 × 768, 315 KB, ≈ $0,07: langostas
  americanas y Dungeness en el vivero, la barra de crudos detrás, cocinero de espaldas). OG = el hero.
- **UK** solo en la FAQ: 8 / 63 °C, 14 alérgenos con moluscos, etiquetas del centro de expedición en lugar de las NSSP,
  edad legal para el vino (18 UK y Australia, 19 en casi todo Canadá).

## 4. Pendiente

1. **John:** Payment Link (§0); luego `sync-payment-links.py`. Fusionar SOLO con el link.
2. Preview: `tienda-gate --base` y `--es-identico --esperadas /kit-tareas-food-truck,/kit-tareas-panaderia,/kit-tareas-marisqueria`,
   `whatsapp-gate`, `robots-gate`, render visual de las tres landings, el hub y los dashboards.
3. LIVE: acceso por admin + `gate-flujo-postpago --only seafood-restaurant-checklist-templates`; sitemap en GSC; correo a la
   cola EN.
