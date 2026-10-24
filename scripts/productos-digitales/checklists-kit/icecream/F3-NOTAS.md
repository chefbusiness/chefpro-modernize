# Ice Cream Shop Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 24-oct-2026. Implementador único de la F3 en `feat/ice-cream-shop-checklists-en-f3` (sale de la
> F1 `8c761db8`; la F2 —traducción y xlsx— va en paralelo en `feat/ice-cream-shop-checklists-en`). Molde: la F3 de la
> ghost kitchen (`../ghost/F3-NOTAS.md`, commits `d3628c76` y `27a6284f`) replicada punto por punto. Sin build,
> Playwright ni navegador (regla térmica; CPU 39-47 °C toda la sesión). No toca `checklists-kit/` (salvo este fichero)
> ni `astro-site/public/dl/`.

## 1. Puntos de registro (los 25 de la ghost kitchen, para `ice-cream-shop-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla con `lang` | `KitTareasLandingPage.astro` | sin cambios |
| 2 | Ficha EN (todas las secciones de `kit-tareas-heladeria.ts`) | `astro-site/src/data/productos-en/tareas/ice-cream-shop-checklist-templates.ts` | ✅ |
| 3 | Landing | `pages/en/digital-products/ice-cream-shop-checklist-templates.astro` | ✅ `omitGlobalApp`, `miselup={false}`, `whatsapp={false}`, env `VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_CHECKLISTS_KIT` → `#comprar` sin link |
| 4 | Gate `/access` | `…/ice-cream-shop-checklist-templates/access.astro` | ✅ |
| 5 | Dashboard `/library` + island | `…/library.astro`, `islands/library/IceCreamShopChecklistsKitLibraryIsland.tsx`, `src/pages/IceCreamShopChecklistsKitDashboard.tsx` | ✅ 12 tarjetas, claves e iconos del ES (02 = `partidas`); cruza a Coffee Shop, Restaurant Checklists y Food Cost Kit Pro (ver §3) |
| 6 | Gemelo ES con hreflang recíproco | `pages/kit-tareas-heladeria.astro` → `alternatesFamilia('kit-tareas-heladeria')` | ✅ (solo el `<head>`) |
| 7 | Familia `kit-tareas-heladeria` → `en: …, vivo: true` | `lib/tienda.ts` | ✅ (fusionar con el link) |
| 8 | Zona app `lang: 'en'` | `lib/zona-app.ts` | ✅ |
| 9 | PRODUCTS `lang: 'en'` | `verify-purchase.ts`, `resend-access.ts` | ✅ |
| 10 | Descargas: claves del ES → 11 xlsx EN + `equivalents-guide` | `get-download-urls.ts` | ✅ nombres = `SPEC.md` §2 = `censo_es.json` `nombre_en` (cruzado por script: 0 de más, 0 de menos) |
| 11 | Precio `{ usd: 19 }` | `product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (74 productos, 22 priceByLang + el nuevo) |
| 12 | Payment Link | `payment-links.ts` vía `sync-payment-links.py` | ⏳ John |
| 13 | Admin de accesos | `admin-generate-access.ts`, `AdminGenerateAccess.tsx` | ✅ |
| 14 | Config SPA y changelog | `productos-digitales-config.ts`, `productos-changelog.ts` | ✅ v2.0 «First English edition» |
| 15 | Catálogo: `name.en`, `description.en`, `urlByLang.en`, `priceByLang.en` | `src/data/products-catalog.ts` | ✅ (los 3 casos de uso EN que listan el kit —concept/artisan-ice-cream-shop, role/master-gelato-maker, consultancy/gelato-consultant— pasan a enlazar la landing EN) |
| 16 | Alias de enlace | `linkify-use-case.ts` / `.tsx` | ✅ + el alias viejo «Tasks: Ice Cream Shop» repuntado a la landing EN y la mención de texto del caso de uso EN del consultor heladero cambiada al nombre nuevo (`use-cases-content.en.consultor.ts`, 1 frase) |
| 17 | Hub EN: «Recurring Tasks: Artisan Ice Cream Shop» sube a la 1 con copy EN | `DigitalProductsHubPage.astro` | ✅ (decía «9 pre-filled operational checklists», «churning», «High/low season»; imagen del ES con texto español → el hero EN) |
| 18 | `footerLinks`: 6 hermanos verticales + Restaurant + 5 kits | 12 fichas EN | ✅ +1 línea cada una (la del Ghost Kitchen, tras el Burger Joint) |
| 19 | GEO: `llms.txt` y `llms-full.txt` («23 products») | `astro-site/public/` | ✅ + fila «Daily operating checklists» |
| 20 | Sitemap lastmod | `sitemap-lastmod.json` | ✅ |
| 21 | Blog EN: banners + párrafo | — | ❌ NO (orden del orquestador: el blog es de la sesión Cursor) → §5 |
| 22 | TEMAS para rebalanceos | — | ❌ NO (ídem) |
| 23 | `tienda-gate.py`: exentos (8 nombres + el subtítulo de la edición ES) y `/kit-tareas-heladeria` en el comentario de `--esperadas` | `tienda-gate.py` | ✅ familias verdes (23 vivos fuera de ES); el estático sale ROJO por robots.txt, PREEXISTENTE (§4.4) |
| 24 | Correo EN | `emails/broadcast-ice-cream-shop-checklists-lanzamiento-en.{html,subject.txt}` | ✅ sin programar; «Hi everyone,» |
| 25 | Cripto + devoluciones | plantilla | ✅ |

## 2. Verificación (ligera, sin build)

- `es-identico-local/comparar.mjs --ref main` (`ASTRO_NM=/Users/johnguerrero/johnguerrero-es-astro/node_modules`):
  **ES idénticas 40 · distintas 0**. Render EN (250.175 bytes): `revisar_texto` de `tienda-gate` 0 fallos (mutación
  comprobada: «Cierre de la heladería» → ❌ «í»), 0 `aggregateRating`/`review`, `priceCurrency` USD, 0 EUR, H1 = title
  SEO (74 car.; description 159), 6 `Question`; «€» 9 y «Google Sheets» 8 = las constantes de la plantilla (igual
  que la ghost). «Heladería» solo en el subtítulo de la edición española y en 3 negocios de testimonio. «Madrid» 0.
- °F de la ficha: todos dentro de `GRADOS_F_SPEC` (−4, 0, 6–10, 10, 10–14, 16–19, 32, 36–39, 41, 70, 104–122, 135,
  185); °C solo en la FAQ UK (−18 °C y 8 °C, D-UK).
- esbuild (stdin, `johnguerrero-es-astro/node_modules/.bin/esbuild`): 34 TS/TSX y frontmatter .astro tocados, 0 errores.
- `sync-product-prices.py --check` verde. `gate-flujo-postpago.py --offline --only ice-cream-shop-checklist-templates`:
  12/12 ficheros = tarjetas; fallan SOLO los 11 xlsx «NO en disco» (F2 en la rama hermana) y «SIN Payment Link».

## 3. Decisiones de contenido

- **Cifras** — del censo (paridad estructural; **a confirmar contra los xlsx EN de la F2**): 298 tareas; 43 en el 01
  (26 + 17), 27 en el 02, 38 en el 03, 41 en el 04, 44 en el 05, 36 en el 06, 33 en el 08 con responsable y hora, 23
  en el 09, 13 en el briefing; 3 plantillas en blanco de 25 filas; 12 meses con 4 sabores; 5 filas libres solo en el 08
  y el 09 (molde base: el molde ligero no las trae). De la SPEC y `mapas_icecream.py` (fijadas en POR_CELDA/ADAPTAR):
  0 °F, 6–10 °F, 36–39 °F y nunca > 41 °F, 16–19 / 10–14 °F, −4 °F, 10 °F a la llegada, 185 °F 15 s con el programa
  validado y la licencia por delante, 104–122 °F, 135 → 70 °F en 2 h y → 41 °F en 4 h, vida útil 2–3 meses a 0 °F y
  3–5 días a 36–39 °F, 32 °F (agua con hielo), Memorial Day–Labor Day, horas del 08 desde las 10:00 AM («mid-morning»).
  Del ES traducido tal cual (**a confirmar en los xlsx EN**): 18–24 sabores (06 «Peak Season» B6), 10–14 (06
  «Off-Season» B6, ADAPTAR), 2–3 tandas al día, 2 scoopers, 24–48 h, maduración mínimo 4 h / 8–12 h. Food cost: sin
  cifra en la landing (el ES dice < 28-32 %; no se afirma hasta ver el xlsx EN).
- **Fuera lo que el ES afirma y el kit no trae:** «software de gestión €40/mes» y «sin internet» (→ fórmula de los
  hermanos), el «inventario semanal por categoría» (son comprobaciones de stock en el 03 y el 05; SPEC D-ICE: sin
  inventario con mínimos), el «foco por día» del semanal del manager, las «fechas clave» en el 06 (están en el
  BONUS-02), las mermas «en el checklist del manager» (van al cierre del 01 y al mensual del 05), DDD / gases fluorados /
  legionela / BIE / registro sanitario (→ D11), «Imprimible A4», «stock de cucuruchos» del briefing (no está) y, en el
  dashboard ES, «15 fechas clave» (son 12 meses). Precio de lanzamiento / −69 % / «valorados en €33» → fórmula EN.
- **Testimonios: los 8 tal cual** (ninguno cita marca o persona real, SPEC §R). **Una frase cambiada** (regla de John,
  11-oct, como Laura Serrano en la ghost): Ana Belén Ruiz decía que el control de «food cost y mermas» lo incluye el
  checklist del manager → «the food cost control in the manager checklist, with the waste log at closing». Comentado
  en la ficha. Roles traducidos; nombres de negocio conservados («Heladería La Cremería», «Gelateria Valentini»…);
  «Consultora gastronómica, Heladerías & Obradores» → «Hospitality Consultant, ice cream shops and production kitchens»
  (no es un negocio); «Cadena Heladerías Frozen Art» → «Frozen Art ice cream shop chain».
- **Imágenes:** las 6 del ES llevan texto en español o la marca «Madrid» a la vista (hero «HELADOS ARTESANALES MADRID
  2026» y «PRECIOS»; vitrina con etiquetas en español; obrador y equipo con pizarras «SABORES DEL DÍA» y «TAREAS
  DIARIAS»; producción con «LA CREMÉ MADRID» y la marca Carpigiani). Se queda solo `tareas-heladeria-servicio`
  (etiquetas en inglés; un «GELATO MADRE · MADRID» pequeño en el delantal: **decide John**). El resto, fotos YA
  publicadas en los casos de uso EN de heladería y gelato, sin español: `use-case-heladeria-conos` (hero y OG;
  «GELATERIA»), `use-case-heladeria-flavors` (vitrina cenital, etiquetas en italiano; una dice «Amarena Fabbri», marca
  real de un ingrediente), `use-case-heladeria-team` (mezcla, sin texto), `use-case-maestro-heladero-mantecadora`
  (mantecadora; «ARTIGIANALE» al fondo) y `consultor-heladero-equipo` (reunión, «ARTISANAL GELATO»; bonus 1). Correo y
  tarjeta del hub: el hero EN. **No hace falta generar ninguna**; opcional, una OG EN propia.
- **Cruces del dashboard:** Coffee Shop Checklists (el hermano más cercano: mostrador, vitrina y café; muchas
  heladerías venden café), Restaurant Checklists (el kit base) y Food Cost Kit Pro (el ES cruza a Escandallos). El ES
  cruza al Kit Tareas Bar; en EN el Bar no casa con una heladería (sin alcohol).
- **Pie:** los 7 hermanos de checklists, los 5 kits EN, el eBook y el caso de uso EN de heladería artesana
  (`/en/use-cases/concept/artisan-ice-cream-shop`, saliente extra como el de la ghost).
- **FAQ:** 19 on-page (opening, closing, producción, licencia estatal de frozen dessert, scoop / dipper well /
  alérgenos, temperaturas, temporada + catering + calendario, limpieza, plantilla gratis, ya rellenas, gelato / scoop
  shop / cadena, firma, Trail, varias tiendas, UK/CA/AU, moneda, suscripción, garantía) y 6 en el JSON-LD.

## 4. Pendiente

1. **John:** Payment Link USD $19 con redirección a
   `/en/digital-products/ice-cream-shop-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` y env
   `VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_CHECKLISTS_KIT` (scope builds); luego `sync-payment-links.py`.
2. `vivo: true` ya en la rama: fusionar SOLO con el link y con los 11 xlsx de la F2 en `dl/` (o `vivo: false`).
3. **Orquestador, tras la F2:** confirmar contra los xlsx EN las cifras de §3 (sobre todo 18–24 / 10–14 sabores,
  2–3 tandas, 24–48 h, 4 h / 8–12 h, el orden del «Shop Closing» y que el texto de las tareas de alérgenos y scoop
  dice lo que la FAQ resume), y que los títulos de las hojas casan con la ficha. Re-ejecutar
  `gate-flujo-postpago --offline --only ice-cream-shop-checklist-templates` (debe quedar solo «SIN Payment Link»).
4. **Preexistente, fuera de esta F3:** `tienda-gate.py` estático sale rojo por robots.txt («tienda en/fr/de/it/pt/nl
  ACTIVA sin sus 6 Disallow en 10 de 16 bloques»); robots.txt no se ha tocado aquí (último cambio, #143). Lo mismo
  pasará en `main`: avisar a quien lleve el SEO.
5. Preview: `tienda-gate --base` y `--es-identico --esperadas /kit-tareas-heladeria`, `whatsapp-gate`, `robots-gate`;
   render visual de landing, hub y dashboard.
6. LIVE: acceso por admin + `gate-flujo-postpago --only …`; sitemap en GSC; correo a la cola (siguiente hueco EN) con
   su routine.
7. Menor, de los hermanos: el alias `'Tasks: Pizzeria'` de `linkify-use-case` sigue apuntando a la landing ES aunque el
   Pizza Shop Checklists Kit Pro está vivo (aquí se ha repuntado el de heladería).

## 5. Blog EN (para la sesión Cursor; puntos 21-22 no hechos)

Posts EN que encajan para banners + párrafo hacia esta landing:
- `prompt-library-creative-ice-cream` (191 menciones de ice cream / gelato): el mejor; banner tras la sección de
  producción o de vitrina.
- `prompt-library-gelato-consulting` (167): para el consultor que entrega checklists al cliente (cuadra con el
  testimonio de Sofía Delgado).
- Secundario: `prompt-library-creative-pastry` (27 menciones).
Víctima sugerida en el rebalanceo de TEMAS: el banner genérico de Restaurant Checklists en esos posts, si lo hay.
