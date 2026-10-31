# Fine Dining Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 31-oct-2026. Implementador único de la F3 en `feat/checklists-en-lote-4`, tras las de los tres kits
> de molde plano (`../foodtruck/F3-NOTAS.md`, mismo método y mismos scripts de registro). Este es **v2.0 completo** (molde
> híbrido como el hotel): la F3 del Taco Shop (#188) y la del hotel punto por punto, sin restricciones de molde plano.
> Sin build, Playwright ni navegador (CPU 45-48 °C).

## 0. Para John: el Payment Link (punto 12)

| Campo | Valor |
|---|---|
| Producto Stripe | **Fine Dining Checklists Kit Pro** |
| Precio | **$19 USD**, pago único |
| Redirección tras el pago | `https://aichef.pro/en/digital-products/fine-dining-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` |
| Env (scope builds, todos los contextos) | `VITE_STRIPE_PAYMENT_LINK_FINE_DINING_CHECKLISTS_KIT` |
| Después | `python3 scripts/productos-digitales/sync-payment-links.py` y `--check` |

Descripción para Stripe (prosa): «Excel checklists for fine dining restaurants with 477 tasks already written: opening and
closing with modernist equipment, tasting menu mise en place and a plating bible, R&D, kitchen brigade duties, sommelier
and wine pairing, chef's table and events, whole-restaurant opening and closing and a cash drawer count in US dollars,
plus a pre-shift meeting template and a 12-month US calendar. Lifetime access to the dashboard.»

## 1. Puntos de registro (los 25 del Taco Shop, para `fine-dining-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla | `KitTareasLandingPage.astro` | sin cambios |
| 2 | Ficha EN | `astro-site/src/data/productos-en/tareas/fine-dining-checklist-templates.ts` | ✅ $19, sin anclas ni rating; 11 plantillas + 3 bonus (14 ficheros), 24 FAQ on-page + 6 en el JSON-LD, 8 testimonios sin marcas |
| 3-5 | Landing, `/access`, `/library`, island, dashboard | `pages/en/digital-products/fine-dining-checklist-templates{.astro,/access.astro,/library.astro}`, `islands/library/FineDiningChecklistsKitLibraryIsland.tsx`, `src/pages/FineDiningChecklistsKitDashboard.tsx` | ✅ copias del Taco Shop; 14 tarjetas con las claves e iconos del ES (`apertura-negocio`, `apertura-caja`…); cruza a Restaurant Checklists Kit Pro, HACCP Food Safety Kit Pro y Food Cost Kit Pro (el ES: Kit Tareas Restaurante, Chef Privado y Escandallos) |
| 6 | Gemelo ES | `pages/kit-tareas-restaurante-creativo.astro` → `alternatesFamilia('kit-tareas-restaurante-creativo')` | ✅ (solo el `<head>`: `--esperadas /kit-tareas-restaurante-creativo`). La «Guía Restaurante Gastronómico» ES no tiene gemelo EN: sin relación que declarar |
| 7 | Familia `kit-tareas-restaurante-creativo` → `en: …, vivo: true` | `lib/tienda.ts` | ✅ (fusionar con el link) |
| 8-10 | Zona app, verify/resend, descargas + config | `zona-app.ts`, `verify-purchase.ts`, `resend-access.ts`, `get-download-urls.ts`, `productos-digitales-config.ts` | ✅ 13 xlsx de SPEC §2 + `equivalents-guide`; `gate-flujo-postpago --offline`: 14 = 14 |
| 11 | Precio `{ usd: 19 }` | `product-prices.ts` | ✅ `--check` verde (96) |
| 12 | Payment Link | — | ⏳ John (§0) |
| 13-16 | Admin, changelog **v2.0**, catálogos, alias | `admin-generate-access.ts`, `AdminGenerateAccess.tsx`, `productos-changelog.ts`, `products-catalog.ts`, `digital-products-catalogue.json`, `linkify-use-case.ts/.tsx` | ✅ (arreglada a mano una comilla de «chef's» en la `description.en` del catálogo que el script dejaba sin escapar) |
| 17 | Hub EN | `DigitalProductsHubPage.astro` | ✅ «Recurring Tasks: Creative / Chef-Driven Restaurant» sube a la 1 con copy EN; Mega Pack el último |
| 18 | `footerLinks` | 15 fichas de checklists (11 + Taco Shop, Food Truck, Bakery, Seafood) y 5 kits | ✅ (sin plan hermano EN; la ficha enlaza el Restaurant Business Plan Kit) |
| 19 | GEO | `llms.txt` y `llms-full.txt` («38 products»; tabla «… Taco Shop and Fine Dining … (19 USD each)») | ✅ |
| 20 | Sitemap | `sitemap-lastmod.json` | ✅ 2026-10-31 |
| 21-22 | Blog EN | — | ❌ otra sesión |
| 23 | `tienda-gate.py` | comentario de `--esperadas` + exentos `consommé` / `Consommé` (préstamo con tilde, como «entrée») | ✅ estático verde |
| 24 | Correo EN | `emails/broadcast-fine-dining-checklists-lanzamiento-en.{html,subject.txt}` | ✅ SIN PROGRAMAR; «Hi everyone,», #111 + #FFD700, $19 |
| 25 | Cripto + devoluciones | plantilla | ✅ render: 3 puertas y la nota de reembolso como los hermanos |

## 2. Verificación (ligera, sin build)

- Cifras contra `revision/dump_en.txt`: 13 libros, 49 hojas (13 «Instructions»), **477 tareas** (01 55 = 33 AM + 22 PM ·
  02 63 · 03 50 · 04 60 en 7 hojas · 05 63 · 06 32 · 07 44 · 08 34 · 10 33 = 18 + 15 · 11 23 = 11 + 12 · B01 20) + las 9
  filas de ejemplo en N/A del 09, que no cuentan (como el ES, 477). Contador «Tasks done: X of Y» que resta las N/A
  (fórmula del 01 leída), firma «Signed off by», 10 y 11 protegidos sin contraseña con responsable, hora límite,
  iniciales y 5 filas verdes libres; caja con billetes y monedas US, Z del TPV, OVER / SHORT y registro mensual. °F de la
  ficha (−31, −4, 0, 32, 41, 70, 100, 135, 145) ⊂ los de los xlsx; °C solo en la FAQ UK. Cada FAQ y cada descripción,
  contra su hoja (los nombres de hoja citados existen).
- `es-identico-local/comparar.mjs --ref main --en …` (CPU 48 °C): **ES idénticas 40 · distintas 0**; render EN 262 KB:
  `revisar_texto` sin fallos, 356 apariciones de la pasarela y la nota de reembolso (= hermanos), 0 `aggregateRating`, USD.
- `tienda-gate.py` estático verde; `sync-product-prices --check` verde (96); `gate-flujo-postpago --offline --only
  fine-dining-checklist-templates`: 14 = 14, falla SOLO «SIN Payment Link»; esbuild 0 errores.
- **No hecho (necesita preview):** `tienda-gate --base`, `--es-identico --esperadas /kit-tareas-restaurante-creativo`, render.

## 3. Decisiones de contenido

- **SEO (SPEC D2):** title «Fine Dining Checklists Kit Pro: Tasting Menu, Brigade & Chef's Table Checklist Templates for
  Excel»; FAQ arriba: opening, closing, **steps of service** (210/mes, desde la hoja «Maître & Dining Room»), mise en place
  del menú degustación, brigada, chef's table (33.100); después I+D, crudo, sous vide, sumiller, foto y guías, servicios
  contratados, caja, service charge ≠ propina, fine dining o bistró.
- **Fuera lo que el ES afirma y el kit EN no trae:** «€40/mes», commis y stagiaire como perfiles, «costes I+D» como tal,
  anisakis UE, BIE / DDD / Verifactu, registro de jornada 4 años, Repsol y fechas españolas, «rangos de sala» en el briefing,
  «Imprimible A4», guía ES↔LatAm, Google Sheets. Las guías: Michelin Guide «in the cities it covers», 50 Best, OAD, James Beard.
- **Testimonios:** los 8 del ES con el subtítulo de la edición española. **Frases cambiadas:** Lucía Navarro («rangos de
  sala» → «the storytelling of each course»), Javier Ortega («guías, premios y jornadas temáticas» → «special menus and food
  festivals»). Roles sin las estrellas Michelin del ES (no verificables fuera de España: «tasting menu / fine dining
  restaurant»). **Avatares** reasignados por oficio y género (chef ejecutivo chef-avatar-1, sous chef 4, jefa de sala 6,
  consultora 2, pastelero chef-avatar-3, chef propietario 8, director 1).
- **Imágenes:** las del ES salvo la de I+D (`-id`: logo legible de una marca real de circuladores); el bordado del hero es
  un nombre inventado. **Una nueva** sin texto: `ai-gallery/tareas-fine-dining-en-pass.jpg` (Nano Banana 2, 1376 × 768,
  266 KB, ≈ $0,07: el pase de un menú degustación con pinzas y lámparas de calor). OG = hero.
- **UK** solo en la FAQ: 8 / 63 °C, 14 alérgenos, denominaciones de la caja, edad legal para el maridaje.

## 4. Pendiente

1. **John:** Payment Link (§0); luego `sync-payment-links.py`. Fusionar SOLO con el link (los 13 xlsx ya están en `dl/`).
2. Preview: `tienda-gate --base`, `--es-identico --esperadas /kit-tareas-food-truck,/kit-tareas-panaderia,/kit-tareas-marisqueria,/kit-tareas-restaurante-creativo`,
   `whatsapp-gate`, `robots-gate`, render visual.
3. LIVE: acceso por admin + `gate-flujo-postpago --only fine-dining-checklist-templates`; sitemap en GSC; correo a la cola EN.
