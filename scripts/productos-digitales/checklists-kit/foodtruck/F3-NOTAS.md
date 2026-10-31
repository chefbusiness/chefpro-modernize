# Food Truck Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 31-oct-2026. Implementador único de la F3 de los tres kits de MOLDE PLANO (food truck, panadería,
> marisquería) en `feat/checklists-en-lote-4` (worktree compartido con la F2 del fine dining: no se toca
> `checklists-kit/**` salvo estas notas ni `public/dl/**`). Molde: la F3 del Taco Shop (`../taco/F3-NOTAS.md`, #188)
> replicada punto por punto. Sin build, Playwright ni navegador (regla térmica; CPU 43-47 °C).

## 0. Para John: el Payment Link (punto 12)

| Campo | Valor |
|---|---|
| Producto Stripe | **Food Truck Checklists Kit Pro** |
| Precio | **$15 USD**, pago único |
| Redirección tras el pago | `https://aichef.pro/en/digital-products/food-truck-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` |
| Env (scope builds, todos los contextos) | `VITE_STRIPE_PAYMENT_LINK_FOOD_TRUCK_CHECKLISTS_KIT` |
| Después | `python3 scripts/productos-digitales/sync-payment-links.py` y `--check` |

Descripción para Stripe (prosa): «Excel checklists for food trucks with 141 tasks already written: setup and teardown, the
pre-trip and vehicle check, health inspection prep under the FDA Food Code, permits and events, the manager, duties by
role, weekly and monthly upkeep, a pre-event briefing and a 12-month US calendar. Lifetime access to the dashboard.»

## 1. Puntos de registro (los 25 del Taco Shop, para `food-truck-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla con `lang` | `KitTareasLandingPage.astro` | sin cambios: la plantilla no afirma contador, instrucciones, protección ni versión (todo sale de `data`); **no hace falta flag** |
| 2 | Ficha EN | `astro-site/src/data/productos-en/tareas/food-truck-checklist-templates.ts` | ✅ $15, sin `priceOld`/`discountBadge`/`value`/`aggregateRating`/`review`; 9 plantillas + 3 bonus, 20 FAQ on-page + 6 en el JSON-LD, 8 testimonios sin marcas |
| 3 | Landing | `pages/en/digital-products/food-truck-checklist-templates.astro` | ✅ copia del Taco Shop: `omitGlobalApp`, `miselup={false}`, `whatsapp={false}`, env → `#comprar` sin link |
| 4 | Gate `/access` | `…/food-truck-checklist-templates/access.astro` | ✅ |
| 5 | Dashboard `/library` + island | `…/library.astro`, `islands/library/FoodTruckChecklistsKitLibraryIsland.tsx`, `src/pages/FoodTruckChecklistsKitDashboard.tsx` | ✅ 12 tarjetas (11 xlsx + `equivalents-guide`), claves e iconos del ES; cruza a Food Truck Business Plan Kit, Restaurant Checklists Kit Pro y HACCP Food Safety Kit Pro (el ES: Kit Tareas Restaurante, Bar y Pack APPCC) |
| 6 | Gemelo ES con hreflang recíproco | `pages/kit-tareas-food-truck.astro` → `alternatesFamilia('kit-tareas-food-truck')` | ✅ (solo el `<head>`: va en `--esperadas /kit-tareas-food-truck`) |
| 7 | Familia `kit-tareas-food-truck` → `en: …, vivo: true` | `lib/tienda.ts` | ✅ (fusionar con el link) |
| 8 | Zona app `lang: 'en'` | `lib/zona-app.ts` | ✅ |
| 9 | PRODUCTS `lang: 'en'` | `verify-purchase.ts`, `resend-access.ts` | ✅ |
| 10 | Descargas: claves del ES → 11 xlsx EN + `equivalents-guide` | `get-download-urls.ts` (+ `productos-digitales-config.ts`) | ✅ nombres = SPEC §2 = `dl/` en disco; `gate-flujo-postpago --offline`: 12 = 12 |
| 11 | Precio `{ usd: 15 }` | `product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (93 productos) |
| 12 | Payment Link | — | ⏳ John (§0); `#comprar` sin link como los hermanos antes del suyo |
| 13 | Admin de accesos | `admin-generate-access.ts`, `AdminGenerateAccess.tsx` | ✅ «(EN, $15)» |
| 14 | Changelog | `productos-changelog.ts` | ✅ v1.1 «First English edition» (los xlsx son v1.1 en docProps, como el ES) |
| 15 | Catálogo | `src/data/products-catalog.ts` (`name.en`, `description.en`, `urlByLang.en`, `priceByLang.en`) + `digital-products-catalogue.json` | ✅ `$15` |
| 16 | Alias de enlace | `linkify-use-case.ts` / `.tsx` | ✅ |
| 17 | Hub EN | `DigitalProductsHubPage.astro` | ✅ la tarjeta «Recurring Tasks: Food Truck» sube a la 1 con copy EN (decía «mobile HACCP»); el Mega Pack sigue el último |
| 18 | `footerLinks` | 12 fichas de checklists (11 + Taco Shop), 5 kits y el Food Truck Business Plan Kit | ✅ +1 línea cada una (tras el Taco Shop / el Hotel; en el plan, tras Digital Products) |
| 19 | GEO | `llms.txt` y `llms-full.txt` («35 products») | ✅ + fila del kit y la tabla de checklists (15 USD) |
| 20 | Sitemap lastmod | `sitemap-lastmod.json` | ✅ 2026-10-31 |
| 21-22 | Blog EN | — | ❌ otra sesión |
| 23 | `tienda-gate.py` | comentario de `--esperadas` con `/kit-tareas-food-truck` | ✅ sin exentos nuevos (los 5 nombres con tilde ya estaban; «Kit de Tareas Recurrentes: Food Truck» no dispara RESTOS_ES); estático verde |
| 24 | Correo EN | `emails/broadcast-food-truck-checklists-lanzamiento-en.{html,subject.txt}` | ✅ SIN PROGRAMAR; «Hi everyone,», #111 + #FFD700, sin precio tachado, $15 |
| 25 | Cripto + devoluciones | plantilla | ✅ estático: `CRYPTO_PRODUCTS=all`, fuera de `EXCLUDE`, `{ usd: 15 }` en `product-prices.ts` (≥ los $14 del eBook EN que ya cobra en cripto) → 3 puertas + nota de reembolso, como el Taco Shop |

## 2. Verificación (ligera, sin build)

- Cifras contra `revision/dump_en.txt` y los 11 xlsx (openpyxl): 11 libros de **una hoja**, **141 tareas** (01 23 = 5 + 6 +
  4 + 8 · 02 18 · 03 18 · 04 18 · 05 15 · 06 20 = 4 × 5 · 07 16 = 8 + 8 · 08 13 = 7 + 6), B01 de 15 campos en 4 bloques,
  B02 de 12 meses (eventos, menú sugerido, mantenimiento, marketing), papel Letter, sin proteger, desplegable en 01-04 y
  06-08 (05 y 09 sin él). °F de la ficha (0, 41, 70, 100, 135, 145, 155, 165) ⊂ °F de los xlsx; °C solo en la FAQ UK.
  Las frases de la ficha, el changelog, el hub, `llms` y el correo, una a una contra el volcado (01 B5-B30, 02-08, B01, B02).
- `tienda-gate.py` estático verde (36 vivos fuera de ES); `sync-product-prices.py --check` verde (93);
  `gate-flujo-postpago.py --offline --only food-truck-checklist-templates`: 12 = 12, falla SOLO «SIN Payment Link».
- esbuild (stdin) sobre los TS/TSX tocados y el frontmatter de los `.astro` tocados (landing, access, library, gemelo ES,
  hub): 0 errores. JSON de catálogo y sitemap: válidos.
- **No hecho (necesita preview):** `tienda-gate --base`, `--es-identico --esperadas /kit-tareas-food-truck` (el `<head>`), render visual.
- **Cierre conjunto de los tres (CPU 44-49 °C):** `es-identico-local/comparar.mjs --ref main --en …`: **ES idénticas 40 · distintas 0** (la plantilla no se toca: sin flag de molde plano; las otras 12 fichas EN solo ganan sus líneas de pie, comprobado con `git diff origin/main`); render EN de las tres (≈ 253 KB) con `revisar_texto` de `tienda-gate` sin fallos, las mismas apariciones de la pasarela cripto y la nota de reembolso que el Taco Shop, 0 `aggregateRating`, `priceCurrency` USD. `robots-gate.py` estático verde.
- **Auditoría adversarial (un agente opus, refutador, contra los volcados):** 0 cifras mal (recontó las 141 / 135 / 165 tareas y los campos de los bonus). Arreglado lo que señaló en esta ficha: «18 tasks with lead times» (solo 12 la llevan), «pre-event tasks for each» event type (son 6 genéricas), «a blank for each °F reading» (5), las 18 del 02 como «pre-trip» (11 lo son; el resto semanal, mensual o anual), «the hood … degreased by the crew» (solo los filtros), «11 Excel checklists» → «11 Excel files» (SEO, CTA, llms, correo) y «Manager checklists» → «A manager checklist».

## 3. Decisiones de contenido

- **Molde plano: fuera todo lo que el Taco Shop afirma y estos ficheros no traen** — contador de tareas, N/A que descuenta,
  celdas verdes editables, 5 filas libres, hojas protegidas («no password»), horas límite («due-by»), iniciales y firma
  del encargado, línea de versión dentro. En su lugar: «who does it and how long it takes» (el 01 trae duración), el
  desplegable ✓ / — / N/A con la fila en verde en 7 checklists, «every cell can be edited».
- **Fuera lo que el ES promete y el kit no trae** (SPEC §5): vitrina y arqueo como hoja (la caja es una tarea: FAQ → Restaurant
  Checklists Kit Pro), «potencia» y «protocolo de emergencia» del generador, «reporting con KPIs», «reservas privadas», ITV,
  licencias españolas, «APPCC obligatorio», fiestas patronales, «Imprimible A4», guía ES↔LatAm, FAQ de Google Sheets.
- **SEO (SPEC D2):** title = H1 «…: Inspection, Setup & Teardown Checklist Templates for Excel»; las FAQ de inspección
  sanitaria (110-170/mes), de bomberos (40) y la PAA «pre-trip inspection» van arriba, con la intención «setup / teardown».
- **Testimonios:** los 8 del ES traducidos tal cual con el subtítulo «…with Kit de Tareas Recurrentes: Food Truck, the
  Spanish edition of this kit». Ninguno contradice el kit EN («gas» → propane). Avatares del ES: ya cuadran (2, 4 y 6 son
  mujeres). Sin imagen nueva.
- **Imágenes:** las 6 del ES, abiertas: rótulos en inglés de marcas inventadas, sin texto en español → se quedan. OG = hero.
- **UK** solo en la FAQ (SPEC D-UK): council 28 días antes, street trading licence, rating 0-5 (Inglaterra, Gales e Irlanda
  del Norte), 8 / 63 °C, 14 alérgenos.

## 4. Pendiente

1. **John:** Payment Link (§0); luego `sync-payment-links.py`. `vivo: true` ya en la rama: fusionar SOLO con el link.
2. Preview: `tienda-gate --base` y `--es-identico --esperadas /kit-tareas-food-truck`, `whatsapp-gate`, `robots-gate`, render.
3. LIVE: acceso por admin + `gate-flujo-postpago --only food-truck-checklist-templates`; sitemap en GSC; correo a la cola EN.
4. Blog EN (21-22, otra sesión).
