# Coffee Shop Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 18-oct-2026. Implementador único de F3 en la rama `feat/coffee-shop-checklists-en` (worktree,
> apilada sobre la del bar). Molde: la F3 del Bar Checklists Kit Pro (`../bar/F3-NOTAS.md`, commit `79d328a8`),
> replicada punto por punto. Contrato: `SPEC.md` (delta) + la SPEC base. Sin build, sin Playwright, sin navegador
> (regla térmica): verificación = lectura + scripts ligeros (CPU 47-50 °C toda la sesión).

## 1. Puntos de registro (los 25 del bar, replicados para `coffee-shop-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla con `lang` | `KitTareasLandingPage.astro` | sin cambios |
| 2 | Ficha EN (réplica de TODAS las secciones de `kit-tareas-cafeteria.ts`) | `astro-site/src/data/productos-en/tareas/coffee-shop-checklist-templates.ts` | ✅ |
| 3 | Landing `/en/digital-products/coffee-shop-checklist-templates` | `…/coffee-shop-checklist-templates.astro` | ✅ `omitGlobalApp`, `miselup={false}`, `whatsapp={false}`, env `VITE_STRIPE_PAYMENT_LINK_COFFEE_SHOP_CHECKLISTS_KIT` → `#comprar` sin link |
| 4 | Gate `/access` (ProductAccessGate `lang="en"`) | `…/coffee-shop-checklist-templates/access.astro` | ✅ |
| 5 | Dashboard `/library` + island | `…/library.astro`, `islands/library/CoffeeShopChecklistsKitLibraryIsland.tsx`, `src/pages/CoffeeShopChecklistsKitDashboard.tsx` | ✅ 12 tarjetas (11 xlsx + Equivalents Guide); claves del ES (la 02 es `barista`); cruza a Restaurant Checklists, HACCP y Food Cost Kit Pro (el ES: Kit Tareas, Pack APPCC, Escandallos) |
| 6 | Gemelo ES con hreflang recíproco | `astro-site/src/pages/kit-tareas-cafeteria.astro` → `alternatesFamilia('kit-tareas-cafeteria')` | ✅ (cambia solo el `<head>`) |
| 7 | Familia `kit-tareas-cafeteria` → `en: coffee-shop-checklist-templates, vivo: true` | `astro-site/src/lib/tienda.ts` | ✅ (fusionar con el link) |
| 8 | Zona app con `lang: 'en'` | `astro-site/src/lib/zona-app.ts` | ✅ |
| 9 | Backend: PRODUCTS con `lang: 'en'` | `verify-purchase.ts`, `resend-access.ts` | ✅ |
| 10 | Descargas: claves de `kit-tareas-cafeteria` → 11 xlsx EN + `equivalents-guide` | `get-download-urls.ts` | ✅ nombres de `SPEC.md` §2 (xlsx del commit F2 `72244658`) |
| 11 | Precio `{ usd: 19 }` | `product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (69 productos) |
| 12 | Payment Link | `payment-links.ts` vía `sync-payment-links.py` | ⏳ John (§4) |
| 13 | Admin de accesos | `admin-generate-access.ts`, `AdminGenerateAccess.tsx` | ✅ |
| 14 | Config SPA y changelog EN | `productos-digitales-config.ts`, `productos-changelog.ts` | ✅ v2.0 «First English edition» |
| 15 | Catálogo `kit-tareas-cafeteria`: `name.en`, `description.en`, `urlByLang.en`, `priceByLang.en` | `src/data/products-catalog.ts` | ✅ |
| 16 | Alias de enlace | `linkify-use-case.ts` (astro) y `.tsx` (SPA) | ✅ |
| 17 | Hub EN: «Recurring Tasks: Cafe / Brunch» sube a la 1 con copy EN | `DigitalProductsHubPage.astro` | ✅ (decía «463 tasks», «terrace»; imagen = hero EN) |
| 18 | `footerLinks`: 5 kits + Restaurant y Bar Checklists + Coffee Shop Business Plan Kit | `kits/*-templates.ts` ×5, `tareas/{restaurant,bar}-checklist-templates.ts`, `planes/coffee-shop-business-plan.ts` | ✅ |
| 19 | GEO: `llms.txt` y `llms-full.txt` («currently 18 products») | `astro-site/public/` | ✅ |
| 20 | Sitemap: lastmod de la landing | `sitemap-lastmod.json` | ✅ |
| 21 | Blog EN: 2 banners sustituidos + párrafo contextual | `fase8x-config/kit-tareas-cafeteria-en.json` + `--aplicar` + `fase8b-regen-lastmod.py` | ✅ reversibilidad OK ×2; `fase8c-libreria-en-gate --todos` 0 errores |
| 22 | Temas para futuros rebalanceos | `fase8e-banners-en-reapuntar.py` (`TEMAS`) | ✅ |
| 23 | `tienda-gate.py`: testimonios exentos + `/kit-tareas-cafeteria` en `--esperadas` (comentario) | `tienda-gate.py` | ✅ estático verde (18 vivos fuera de ES) |
| 24 | Correo de lanzamiento EN | `emails/broadcast-coffee-shop-checklists-lanzamiento-en.{html,subject.txt}` | ✅ sin programar |
| 25 | Tres puertas cripto + nota de devoluciones | vienen con la plantilla | ✅ |

Blog EN: solo hay UN post de café (`prompt-library-barista-consulting`, 302 menciones; el siguiente, el del bartender,
15 y ya lleva Bar y Restaurant Checklists). Por eso son 2 y no 3: barista (víctima Restaurant Financial Plan 30 → 29;
párrafo antes de «Professional Coffee Equipment», ancla 8) y `prompt-library-bakery-consulting` (víctima HACCP 29 →
28; párrafo antes de «Why prompts matter», lejos del enlace de How to Open a Pastry Shop): obrador con mostrador =
hoja «Pastry Case» y perfil «Baker».

## 2. Las 20 landings ES siguen byte a byte iguales

Comparador sin build (`es-identico-local/comparar.mjs`, `ASTRO_NM` = `johnguerrero-es-astro/node_modules`,
`--ref main`): **ES idénticas 40 · distintas 0**. Render EN (244.719 bytes): `revisar_texto` de `tienda-gate` sin
fallos, 0 «€», 0 `ratingValue`, `priceCurrency` USD; «Google Sheets» solo en el carrusel de apps (constante de la
tienda). El bar re-renderiza con +264 bytes = la tarjeta nueva de su pie; nada más del bar cambia.

## 3. Decisiones de contenido

- Traducción propia desde el ES (regla 1bis, sin bridge); cada cifra comprobada contra los xlsx EN del commit F2
  (500 tareas, 130 en el 01, 31 en el 08, 22 fechas + 5 filas «(Your date)», «25–30 s, 25–30 ml (about 1 fl oz)»,
  9 bar, 41 °F, 7 días, «tongs/bakery tissue/gloves», «9 major allergens; UK: 14», «⚠️ REORDER», semanal del manager
  «(Monday)», GH/KH, muelas 880–1,320 / 1,760–2,650 lb, mimosa solo con licencia y 21+).
- **Lo que el ES afirma y el kit no trae, fuera:** «latte art del día» y «temperatura de tazas» en el barista,
  «barista jefe» y «responsable de cocina» (perfiles reales: Shift Lead, Barista, Baker, Server, Busser & Runner), el
  semanal «lun-vie con foco por día» (es de lunes, por bloques), «pre-evento 48 h» y «pop-ups» (el 06 son Sunday
  Brunch, Valentine's Day, Holiday Season y Patio Season), las «17 fechas» del dashboard ES. La 02 del ES se vendía
  como «Tareas del Barista»: en EN lleva su título real (cocina + vitrina).
- Testimonios: los 10 traducidos tal cual con el subtítulo de la edición española; dos frases que el kit contradice,
  cambiadas (Andrés Gallego: «48 h antes, día anterior, mañana» → sábado / domingo / servicio; Diego Navarro:
  «rotación de vitrinas… organizado por día» → lo que trae el semanal, por bloques); «A4» → «one sheet».
- Sin anclas (FTC); fórmula «One-time payment · lifetime access · updates included»; sin rating ni reviews.
  FAQ UK/CA/AU: 8 °C / 63 °C, 14 alérgenos (ya anotados en las celdas), «cafe», nota UK del calendario; Canadá y
  Australia con sus temperaturas y alérgenos en las celdas verdes; mimosas con licencia (18 UK/AU + RSA, 19 en
  Canadá salvo AB, MB, QC); caja editable sin contraseña; Equivalents Guide. Sin Natasha's Law (SPEC D-UK).
- **Imágenes:** fuera las del ES con texto en español: hero («TOMA CAFÉ» en las bolsas), vitrina (etiquetas y
  precios en español y en €), inventario («LECHE ENTERA», «ALMENDRA») y la OG («Kit de Tareas», «€12»). Las
  sustituyen fotos EN ya publicadas de la familia coffee shop: `use-case-coffee-shop-hero` (también OG y tarjeta
  del hub y correo), `use-case-coffee-shop-pastries`, `use-case-coffee-shop-bar`. Se quedan barista, brunch, terraza
  (rótulo italiano) y equipo. Los 3 fondos ajenos del ES (cochinillo, gambas, risotto) → fotos de cafetería.
  Falta una OG EN propia si John la quiere.

## 4. Pendiente para el cierre

1. **John:** Payment Link USD $19 con redirección a
   `/en/digital-products/coffee-shop-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` y env
   `VITE_STRIPE_PAYMENT_LINK_COFFEE_SHOP_CHECKLISTS_KIT` en Netlify (scope builds); luego `sync-payment-links.py`.
   Hoy `gate-flujo-postpago --offline --only coffee-shop-checklist-templates`: 12 entregables, **1 fallo esperado**
   («SIN Payment Link», que lista también el del bar porque la rama está apilada).
2. `vivo: true` ya está en la rama: fusionar SOLO con el link creado (o `vivo: false` si hubiera que fusionar antes).
3. Preview: `tienda-gate --base` y `--es-identico --esperadas /kit-tareas-cafeteria` (y `/kit-tareas-bar` si va en
   el mismo PR), `whatsapp-gate`, `robots-gate`; render visual de landing y dashboard.
4. LIVE: acceso por admin + `gate-flujo-postpago.py --only coffee-shop-checklist-templates`; sitemap en GSC; correo
   a la cola de 5 días (`CALENDARIO-V2-SEMANAL.md`, siguiente hueco EN) y programarlo con su routine.
5. Test real en Google Sheets (común a la línea) → pastilla, `compatSubtitle`, FAQ y aviso del dashboard.
