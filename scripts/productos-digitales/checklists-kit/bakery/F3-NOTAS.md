# Bakery Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 31-oct-2026. Segundo de los tres kits de MOLDE PLANO de la F3 conjunta (`../foodtruck/F3-NOTAS.md`
> tiene el contexto y el método). Rama `feat/checklists-en-lote-4`. Molde: la F3 del Taco Shop (#188) punto por punto.
> Sin build, Playwright ni navegador (CPU 42-46 °C).

## 0. Para John: el Payment Link (punto 12)

| Campo | Valor |
|---|---|
| Producto Stripe | **Bakery Checklists Kit Pro** |
| Precio | **$15 USD**, pago único |
| Redirección tras el pago | `https://aichef.pro/en/digital-products/bakery-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` |
| Env (scope builds, todos los contextos) | `VITE_STRIPE_PAYMENT_LINK_BAKERY_CHECKLISTS_KIT` |
| Después | `python3 scripts/productos-digitales/sync-payment-links.py` y `--check` |

Descripción para Stripe (prosa): «Excel checklists for bread bakeries with 135 tasks already written: opening and closing
on the overnight bake shift, the sourdough starter and fermentation, deck and rack ovens with a bake table in °F, the
display case and labels, the manager, duties by role, weekly and monthly upkeep, a daily production sheet and a 12-month
US calendar. Lifetime access to the dashboard.»

## 1. Puntos de registro (los 25 del Taco Shop, para `bakery-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla | `KitTareasLandingPage.astro` | sin cambios (no afirma nada del molde: todo sale de `data`); sin flag |
| 2 | Ficha EN | `astro-site/src/data/productos-en/tareas/bakery-checklist-templates.ts` | ✅ $15, sin anclas ni rating; 9 plantillas + 3 bonus, 22 FAQ on-page + 6 en el JSON-LD, 8 testimonios sin marcas |
| 3-5 | Landing, `/access`, `/library`, island, dashboard | `pages/en/digital-products/bakery-checklist-templates{.astro,/access.astro,/library.astro}`, `islands/library/BakeryChecklistsKitLibraryIsland.tsx`, `src/pages/BakeryChecklistsKitDashboard.tsx` | ✅ copias del Taco Shop; 12 tarjetas con las claves e iconos del ES; cruza a Bakery Business Plan Kit, **Pastry Shop Checklists Kit Pro** y HACCP Food Safety Kit Pro (el ES: Kit Tareas Restaurante, Pastelería y Pack APPCC) |
| 6 | Gemelo ES | `pages/kit-tareas-panaderia.astro` → `alternatesFamilia('kit-tareas-panaderia')` | ✅ (solo el `<head>`: `--esperadas /kit-tareas-panaderia`) |
| 7 | Familia `kit-tareas-panaderia` → `en: …, vivo: true` | `lib/tienda.ts` | ✅ (fusionar con el link) |
| 8-10 | Zona app, verify/resend, descargas + config | `zona-app.ts`, `verify-purchase.ts`, `resend-access.ts`, `get-download-urls.ts`, `productos-digitales-config.ts` | ✅ 11 xlsx de SPEC §2 + `equivalents-guide`; `gate-flujo-postpago --offline`: 12 = 12 |
| 11 | Precio `{ usd: 15 }` | `product-prices.ts` | ✅ `--check` verde (94) |
| 12 | Payment Link | — | ⏳ John (§0) |
| 13-16 | Admin, changelog v1.1, catálogos, alias | `admin-generate-access.ts`, `AdminGenerateAccess.tsx`, `productos-changelog.ts`, `products-catalog.ts`, `digital-products-catalogue.json`, `linkify-use-case.ts/.tsx` | ✅ |
| 17 | Hub EN | `DigitalProductsHubPage.astro` | ✅ «Recurring Tasks: Bakery / Production Kitchen» sube a la 1 con copy EN (decía «steam convection ovens» y «Christmas, Epiphany»); Mega Pack el último |
| 18 | `footerLinks` | 13 fichas de checklists (11 + Taco Shop + Food Truck), 5 kits y el Bakery Business Plan Kit | ✅ (el Pastry Shop incluido: cruce pan ↔ pastelería) |
| 19 | GEO | `llms.txt` y `llms-full.txt` («36 products») | ✅ |
| 20 | Sitemap | `sitemap-lastmod.json` | ✅ 2026-10-31 |
| 21-22 | Blog EN | — | ❌ otra sesión |
| 23 | `tienda-gate.py` | comentario de `--esperadas` + exento «Kit de Tareas Recurrentes: Panadería / Obrador» | ✅ estático verde (37 vivos fuera de ES) |
| 24 | Correo EN | `emails/broadcast-bakery-checklists-lanzamiento-en.{html,subject.txt}` | ✅ SIN PROGRAMAR; «Hi everyone,», #111 + #FFD700, $15 |
| 25 | Cripto + devoluciones | plantilla | ✅ estático (`CRYPTO_PRODUCTS=all`, fuera de `EXCLUDE`, `{ usd: 15 }`) |

## 2. Verificación (ligera, sin build)

- Cifras contra `revision/dump_en.txt` y los xlsx (openpyxl): 11 libros de una hoja, **135 tareas** (01 25 = 7 + 7 + 5 + 6,
  de 3:00 AM a 2:30 PM · 02 16 con columna «Reading» · 03 18 = 6 + 5 + 7 de la tabla de horneado · 04 14 · 05 13 · 06 18 =
  5 + 5 + 4 + 4 · 07 16 = 8 + 8 · 08 15), B01 de 13 campos en 4 bloques, B02 de 12 meses (panes, eventos y pedidos,
  mantenimiento, formación), Letter, sin proteger, desplegable en 01-04 y 06-08. Los °F de la ficha ⊂ los de los xlsx
  (rangos incluidos: 72–79, 75–82, 75–79, 37–41, 36–39, 430–500, 465–480, 445–465, 445, 430–445, 375–390, 355–375, 41, 135).
- Contraste frase a frase: ajustado tras él «all sanitized» (los hornos se limpian, no se desinfectan con tira) y «ancient
  grains» (→ «specialty grains»: el 08 dice spelt, kamut, buckwheat, whole rye).
- `tienda-gate.py` estático verde; `sync-product-prices --check` verde; `gate-flujo-postpago --offline --only
  bakery-checklist-templates`: 12 = 12, falla SOLO «SIN Payment Link»; esbuild 0 errores (TS/TSX y frontmatter).
- Cierre conjunto (ver `../foodtruck/F3-NOTAS.md` §2): ES idénticas 40/40, render EN sin fallos de `revisar_texto`. **Auditoría adversarial:** arreglados «sourdough starter log» (el 02 es un checklist con una fila de registro y una columna «Reading», no una hoja de registro: ficha, keywords, hub, correo), «a column for each reading» (es una), el testimonio de María López («poolish y biga registrados con temperaturas y horas» → la fila no las pide; frase cambiada), «the damper … for each oven» (solo el de solera), «11 Excel checklists» → «11 Excel files» y «Manager checklists».

## 3. Decisiones de contenido

- **Molde plano:** fuera contador, N/A que descuenta, celdas verdes, filas libres, protección, iniciales, firma y versión
  dentro del fichero; sí la HORA de cada tarea del 01 (turno de madrugada) y la columna «Reading» del 02.
- **Fuera lo que el ES promete y el kit no trae** (SPEC §5): horno de convección (la FAQ dice que se añade en la plantilla
  en blanco), «protocolos para recuperar masas», esponja, «gestión de cola», «reporting con KPIs», calibración de
  termómetros, San Juan, Reyes, ensaimadas, «marketing por estación» (la columna E del calendario es Training), «cada
  categoría con sus tiempos» (la tabla trae 7 panes), «Imprimible A4», guía ES↔LatAm, FAQ de Google Sheets.
- **SEO (SPEC D2):** title «Bakery Checklists Kit Pro: Bread Bakery Opening, Production & Closing Checklist Templates for
  Excel»; FAQ arriba: opening (30/mes), closing, cleaning schedule, production schedule, starter log. FAQ nuevas: cottage
  food (no aplica: panadería con permiso) y pan frente a pastelería (→ Pastry Shop Checklists Kit Pro).
- **Testimonios:** los 8 del ES con el subtítulo de la edición española. **Una frase cambiada** (Fernando Delgado: «Navidad,
  Reyes, Semana Santa» → «the holiday season, Easter»). **Avatares:** el maestro panadero pasa del chaleco de bar
  (avatar-1) al chef con gorro (chef-avatar-3); la oficial de obrador, del vestido negro (avatar-6) a la panadera de
  `avatars-nicho/avatar-panadera-celiaca.jpg` (reutilizada de la Guía Panadería). Sin imagen nueva.
- **Imágenes:** las 6 del ES (`use-case-panadero-*`), abiertas: solo rótulos en inglés en los tarros → se quedan. OG = hero.
- **UK** solo en la FAQ: 8 / 63 °C, 14 alérgenos, pan y bollería fría para llevar a tipo cero de IVA (lo caliente no).

## 4. Pendiente

1. **John:** Payment Link (§0); luego `sync-payment-links.py`. Fusionar SOLO con el link.
2. Preview: `tienda-gate --base` y `--es-identico --esperadas /kit-tareas-panaderia`, `whatsapp-gate`, `robots-gate`, render.
3. LIVE: acceso por admin + `gate-flujo-postpago --only bakery-checklist-templates`; sitemap en GSC; correo a la cola EN.
