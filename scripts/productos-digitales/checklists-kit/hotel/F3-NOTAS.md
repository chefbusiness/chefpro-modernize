# Hotel Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 27-oct-2026. Implementador único de la F3 en `feat/hotel-checklists-en` (F1 y F2 ya hechas: 19 xlsx
> EN en `astro-site/public/dl/hotel-checklist-templates/`). Molde: la F3 del Ice Cream Shop Checklists Kit Pro
> (`../icecream/F3-NOTAS.md`, commits `06942e8a`, `516052bc`, `c6d2b251`, `d76fdec5`) replicada punto por punto. Sin
> build, Playwright ni navegador (regla térmica; CPU 46-48 °C toda la sesión). Además, parche de seguridad del ES LIVE
> en commit aparte (§5).

## 1. Puntos de registro (los 25 de la heladería, para `hotel-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla con `lang` | `KitTareasLandingPage.astro` | sin cambios |
| 2 | Ficha EN (todas las secciones de `kit-tareas-hotel.ts`) | `astro-site/src/data/productos-en/tareas/hotel-checklist-templates.ts` | ✅ $29, sin `priceOld`/`discountBadge`/`value`/`aggregateRating`/`review`; 19 plantillas, 20 FAQ on-page + 6 en el JSON-LD, 10 testimonios sin marcas |
| 3 | Landing | `pages/en/digital-products/hotel-checklist-templates.astro` | ✅ `omitGlobalApp`, `miselup={false}`, `whatsapp={false}`, env `VITE_STRIPE_PAYMENT_LINK_HOTEL_CHECKLISTS_KIT` → `#comprar` sin link |
| 4 | Gate `/access` | `…/hotel-checklist-templates/access.astro` | ✅ |
| 5 | Dashboard `/library` + island | `…/library.astro`, `islands/library/HotelChecklistsKitLibraryIsland.tsx`, `src/pages/HotelChecklistsKitDashboard.tsx` | ✅ 20 tarjetas (19 xlsx + `equivalents-guide`), claves e iconos del ES; cruza a Catering Checklists, Restaurant Checklists y Food Cost Kit Pro |
| 6 | Gemelo ES con hreflang recíproco | `pages/kit-tareas-hotel.astro` → `alternatesFamilia('kit-tareas-hotel')` | ✅ (solo el `<head>`: va en `--esperadas /kit-tareas-hotel`) |
| 7 | Familia `kit-tareas-hotel` → `en: …, vivo: true` | `lib/tienda.ts` | ✅ (fusionar con el link) |
| 8 | Zona app `lang: 'en'` | `lib/zona-app.ts` | ✅ |
| 9 | PRODUCTS `lang: 'en'` | `verify-purchase.ts`, `resend-access.ts` | ✅ |
| 10 | Descargas: claves del ES → 19 xlsx EN + `equivalents-guide` | `get-download-urls.ts` | ✅ nombres = `SPEC.md` §2, cruzados por script: 0 de más, 0 de menos (también contra `dl/` en disco, el dashboard y `productos-digitales-config.ts`) |
| 11 | Precio `{ usd: 29 }` | `product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (83 productos) |
| 12 | Payment Link | `payment-links.ts` vía `sync-payment-links.py` | ⏳ John |
| 13 | Admin de accesos | `admin-generate-access.ts`, `AdminGenerateAccess.tsx` | ✅ |
| 14 | Config SPA y changelog | `productos-digitales-config.ts`, `productos-changelog.ts` | ✅ v2.0 «First English edition» (la versión de los xlsx es 2.0 · October 2026) |
| 15 | Catálogo: `name.en`, `description.en`, `urlByLang.en`, `priceByLang.en` | `src/data/products-catalog.ts` | ✅ `$29`; + `digital-products-catalogue.json` (entrada EN, como las hermanas) |
| 16 | Alias de enlace | `linkify-use-case.ts` / `.tsx` | ✅ «Hotel Checklists Kit Pro» (no había alias viejo «Tasks: Full Hotel») |
| 17 | Hub EN: «Recurring Tasks: Full Hotel» sube a la 1 con copy EN | `DigitalProductsHubPage.astro` | ✅ una sola tarjeta (la vieja apuntaba al ES y decía «46 checklists, 15 templates, 11 departments»); imagen = hero EN |
| 18 | `footerLinks`: 10 fichas de checklists (+ Restaurant) y 5 kits | 15 fichas EN | ✅ +1 línea cada una (tras Pastry Shop) |
| 19 | GEO: `llms.txt` y `llms-full.txt` («29 products») | `astro-site/public/` | ✅ + fila del kit y mención en la tabla de checklists (29 USD) |
| 20 | Sitemap lastmod | `sitemap-lastmod.json` | ✅ 2026-10-27 |
| 21 | Blog EN: banners + párrafo | — | ❌ NO (carril de otra sesión) |
| 22 | TEMAS para rebalanceos | — | ❌ NO (ídem) |
| 23 | `tienda-gate.py`: exentos (3 nombres con tilde + el subtítulo de la edición ES) y `/kit-tareas-hotel` en el comentario de `--esperadas` | `tienda-gate.py` | ✅ estático verde: «29 producto(s) vivos fuera de ES con data, páginas y zona-app» |
| 24 | Correo EN | `emails/broadcast-hotel-checklists-lanzamiento-en.{html,subject.txt}` | ✅ SIN PROGRAMAR (va el 5-mar-2027 14:00Z); «Hi everyone,», negro #111 + dorado #FFD700, sin precio tachado |
| 25 | Cripto + devoluciones | plantilla | ✅ |

## 2. Verificación (ligera, sin build)

- `gate-flujo-postpago.py --offline --only hotel-checklist-templates`: 20 ficheros = 20 tarjetas; falla SOLO «SIN Payment
  Link» (esperado).
- `sync-product-prices.py --check` verde; `tienda-gate.py` (estático, python 3.11) en verde.
- esbuild (stdin) sobre los TS/TSX tocados y el frontmatter de los 2 `.astro` tocados: 0 errores (cazó una comilla sin escapar
  en el changelog, corregida).
- Barrido tipo `revisar_texto` de `tienda-gate` sobre todos los literales de la ficha y del dashboard: 0 «€», 0 restos de
  español (` para `, ` con `, tildes…), 0 no latinos; 0 `aggregateRating`/`review`/`priceOld`/«% off»/«worth».
- °F de la ficha (41, 135, 140, 104) dentro de `GRADOS_F_SPEC`; °C solo en la FAQ UK (8 °C, 60/50 °C de la HSE L8).
- Cifras contra `revision/dump_en.txt`: 636 tareas (64 · 35 · 28 · 39 · 38 · 34 · 48 · 23 · 52 · 28 · 28 · 17 · 69 · 28 · 28 ·
  33 · 23 + 21 del briefing), 74 hojas, 24 fechas, 7 listas técnicas en el 13, 5 de housekeeping, 4 de recepción.
- **No hecho (necesita build/preview):** `es-identico-local/comparar.mjs`, render EN, `tienda-gate --base`,
  `whatsapp-gate`, `robots-gate`, render visual de landing, hub y dashboard.

## 3. Decisiones de contenido

- **Cifras** (SPEC, censo y dump EN): 19 ficheros, 74 hojas, 636 tareas, 24 fechas. Fuera «53 hojas / 11 departamentos» del
  ES (no cuadran con los 19 libros ni con el recuento de hojas EN) y «20 fechas» del dashboard ES (son 24).
- **Fuera lo que el ES afirma y el kit no trae:** Trail «€60-75/mes», -81 %, «ahorra €76,50», «valorados en €33»,
  rating 4,9 de 8 reseñas, «Imprimible A4», «sin internet», DDD / BIE / OCA / RD 487/2022 (→ FDA Food Code, OSHA, NFPA,
  ASHRAE 188, MAHC 2024), anisakis (→ 3-402.11), Día del Padre / comuniones / puentes (→ calendario US) y las «tareas por
  perfil» de dos testimonios (el hotel no trae libro de perfiles).
- **Testimonios (los 10, sin marcas ni hoteles reales, D-HOT):** rol + tipo de hotel (+ ciudad cuando el ES la daba:
  «luxury city hotel, Madrid», «lifestyle hotel, Barcelona», «beach resort, Costa del Sol»; Ritz-Carlton, Four Seasons y NH
  no daban ciudad y no se ha inventado). Palace, Meliá, W, Ritz-Carlton, Four Seasons, NH, «Hoteles Ibéricos» y
  «Hospitality Experts» fuera. **Tres frases cambiadas** (regla de John, 11-oct): Miguel Ángel Torres («tareas por perfil
  para camarero», «descorche» → los checklists de restaurante, banquetes y room service, «room charges», briefing),
  Carlos Navarro («las tareas de F&B manager y los perfiles» → «F&B, housekeeping and front desk checklists») y el rol de
  Daniela Hernández (el ES decía Revenue Manager y hablaba como F&B manager de grupo → «Group F&B Manager, hotel chain»).
  Subtítulo con «Kit de Tareas Recurrentes: Hotel Completo, the Spanish edition of this kit».
- **Imágenes:** abiertas una a una las 6 del ES (`tareas-hotel-hero`, `-buffet`, `-roomservice`, `-cocina`, `-banquete`,
  `-equipo`): ninguna lleva texto en español, logos ni marcas (los rótulos del buffet están en inglés) → se quedan las 6.
  **Descartada:** `og-kit-tareas-hotel.jpg` (el OG del ES: «Kit de Tareas Recurrentes», «Hotel Completo — 46 Checklists»,
  «€18,50», «Imprimible A4») → `ogImage` = el hero de la landing, como los hermanos EN. Bonus: equipo, banquete y la
  guía común `en-equivalents-guide.jpg`. Correo y tarjeta del hub: el hero EN.
- **FAQ:** 20 on-page (housekeeping, limpieza de una habitación, frecuencia, chinches, night audit, mantenimiento
  preventivo, plantilla gratis, F&B y seguridad alimentaria, piscina y spa, caja, hotel pequeño a resort, ya rellenas,
  firma, apps tipo Trail, varios hoteles, UK/CA/AU con PWTAG / HSE L8 / Fire Safety Order 2005 / FIR 2014, moneda,
  suscripción, garantía) y 6 en el JSON-LD. Chinches: la FAQ dice que el kit comprueba costuras y somier y lista el control
  de plagas, y que NO es un programa de gestión de plagas.
- **Pie:** los 9 hermanos EN de checklists, los 5 kits y el eBook; sin saliente extra (no hay caso de uso EN de hotel).
- **Cruces del dashboard:** Catering Checklists (banquetes y eventos), Restaurant Checklists (el kit base) y Food Cost Kit
  Pro (el ES cruza a Escandallos).

## 4. Pendiente

1. **John:** Payment Link USD $29 con redirección a
   `/en/digital-products/hotel-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` y env
   `VITE_STRIPE_PAYMENT_LINK_HOTEL_CHECKLISTS_KIT` (scope builds); luego `sync-payment-links.py`.
2. `vivo: true` ya en la rama: fusionar SOLO con el link (los 19 xlsx ya están en `dl/`).
3. Preview: `tienda-gate --base` y `--es-identico --esperadas /kit-tareas-hotel`, `whatsapp-gate`, `robots-gate`, render
   visual de landing, hub y dashboard.
4. LIVE: acceso por admin + `gate-flujo-postpago --only hotel-checklist-templates`; sitemap en GSC; correo a la cola
   (5-mar-2027 14:00Z) con su routine.
5. Blog EN (puntos 21-22, otra sesión): posts EN de hotel F&B / room service / banquetes (agentes «Hotel …») para banners.
6. Menor: `textos_es.json`, `censo_es.json` y `textos_en/pendientes.json` conservan el texto ES de las 3 celdas parcheadas
   (clave de la traducción); no se regeneran para no romper el mapeo. Si algún día se re-ejecuta `extraer_textos`, esas 3
   cadenas ES cambian y hay que remapear su EN (el EN ya está correcto).

## 5. Parche de seguridad del ES LIVE (commit aparte `33096bc6`, sin cambio de versión, sin correo)

Método del commit `938e15e3` (Chocolatería): parche en el XML de las celdas `inlineStr` (VPS, `/tmp/hotelpatch/patch_es.py`),
estilos, DV, CF y caché intactos (solo cambian `sheet2`/`sheet3` del 15 y `sheet5` del 09; los otros 17 libros, mismo
sha256), mismo texto en `scripts/generate-tareas-hotel.py` (el contenido v2.0 de la familia no guarda estos textos).

| Celda | Antes | Después |
|---|---|---|
| 15 «Cierre Spa» B7 | Apagar saunas, baño de vapor y jacuzzi | Apagar saunas y baño de vapor; en el jacuzzi apagar solo chorros y soplante: la filtración, la recirculación y la desinfección siguen en marcha toda la noche |
| 15 «Apertura Spa» B6 | Verificar temperatura de piscina/jacuzzi (35-38 °C) y ajustar | Verificar temperatura del jacuzzi (35-38 °C) y ajustar |
| 09 «Deep Cleaning» B13 | Pulir suelos (parqué, mármol, moqueta según material) | Pulir suelos duros (parqué, mármol) y lavar la moqueta con inyección-extracción, según material |

`censo-entregables` y `gate-no-latinos` del ES en 0; `openpyxl` abre los dos libros; `dump_es.txt` regenerado: solo esas 3 celdas.
