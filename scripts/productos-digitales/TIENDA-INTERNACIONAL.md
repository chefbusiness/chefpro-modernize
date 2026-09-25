# Tienda internacional de productos digitales — doc canónico

> Frente abierto por John el **2026-09-23** (sesión Claude Code). Primero inglés (`/en/digital-products`) y después, de
> forma progresiva, fr/de/it/pt/nl: los idiomas en los que ya viven la plataforma y las landings principales.
> Leer este documento ENTERO antes de tocar cualquier pieza de la tienda en otro idioma.

## 0. Nomenclatura (John, 24-sep-2026)

«**Tienda internacional**» es el conjunto; cada idioma es **su propia tienda internacional**, y se nombra así en docs,
handoffs, memorias, commits y PR:

| Tienda | Hub | Estado |
|---|---|---|
| Tienda internacional en inglés | `/en/digital-products` | hub LIVE (PR #95) |
| Tienda internacional en francés | `/fr/produits-numeriques` | hub LIVE (PR #96) |
| Tienda internacional en alemán | `/de/digitale-produkte` | hub LIVE (PR #96) |
| Tienda internacional en italiano | `/it/prodotti-digitali` | hub LIVE (PR #96) |
| Tienda internacional en portugués | `/pt/produtos-digitais` | hub LIVE (PR #96) |
| Tienda internacional en neerlandés | `/nl/digitale-producten` | hub LIVE (PR #96) |

Bélgica no tiene idioma propio: la cubren la tienda en neerlandés (Flandes) y la tienda en francés (Valonia y Bruselas).
Todas nacen igual: **duplicando lo español y traduciéndolo** (§1).

## 1. Decisiones de John (23-sep-2026)

| Tema | Decisión |
|---|---|
| Cuándo | **Ya**, sin esperar a cerrar el catálogo ES (deroga §0-bis.3 del calendario del 31-ago) |
| Cadencia | **Rotación de 3 sesiones:** v2.0 ES → producto nuevo ES → producto EN → … (mismo techo de tokens) |
| Mercado | Inglés **US como base internacional**. Impuesto (sales tax/VAT) y moneda son **parámetros** del Excel: celda de tipo de impuesto e importes sin símbolo. Las unidades van en **US customary** en los ejemplos, con una tabla de conversiones que cubre métrico e imperial y avisos UK (decidido en el piloto, `recipe-costing-kit/SPEC.md` D5-D7). Lo normativo: núcleo HACCP/Codex + **anexo US** (FDA Food Code) + **anexo UK** (FSA, 14 alérgenos). Un SKU sirve a US/UK/CA/AU |
| Moneda | Payment Links en **USD**, precio psicológico ($19/$29/$49…), con **Adaptive Pricing** de Stripe activado (UK ve £, CA ve CAD). NOWPayments factura en USD |
| Piloto | **Recipe Costing Kit** (= `kit-escandallos`) |
| 🔴 **Duplicar el ES y adaptar, NUNCA reconstruir** (John, 24-sep) | El español lleva SIEMPRE la delantera: cada producto se construye desde cero SOLO en español. Para inglés (y cada idioma futuro) se **duplican** la landing, el dashboard y los ficheros (xlsx, pdf, docx, md…) del producto ES y se **traducen**, adaptando las variables del mercado nativo (terminología, moneda, impuestos, unidades, normativa/anexos, benchmarks, ejemplos). **Diseño, estructura, componentes y maquetación son los mismos**: no se crea ninguna plantilla ni página nueva. Lo mismo para los hubs. «Nativo» = **traducido al idioma de destino**, no rehecho |

Lo no delegable sigue siendo lo mismo: **el Payment Link de Stripe lo crea John** (en USD, con Adaptive Pricing).

## 2. Datos que sostienen las decisiones

**GSC, `/en/` en los últimos 90 días (medido el 23-sep):**

| País | Impresiones | Clics |
|---|---|---|
| EE. UU. | 2.890 | 9 |
| Reino Unido | 2.063 | 5 |
| Canadá | 312 | 1 |
| India | 217 | 9 |

**Keywords (DataForSEO, 23-sep; US = 2840/en · UK = 2826/en):**

| Keyword | US | UK | Lectura |
|---|---|---|---|
| food cost calculator | 1.900 | 260 | La herramienta gratuita del sitio ya compite aquí; puerta natural hacia el kit |
| restaurant templates | 480 | 140 | ⚠️ **Intención = plantillas de WEB** (ThemeForest, Wix, Canva). No es la keyword del hub |
| food cost template / menu costing template | 170 | 30 | Keyword principal del piloto |
| recipe costing template | 140 | 10 | Secundaria del piloto (con AI Overview) |
| food cost spreadsheet | 110 | 20 | Secundaria |
| recipe costing | 110 | 10 | Informativa |
| food cost calculator excel | 90 | 10 | Secundaria |
| restaurant forms / checklist templates | 70 / 40 | 10 / 10 | Kits de tareas (ola 2) |
| restaurant excel/spreadsheet/management templates | 10-20 | ≤ 10 | Sin demanda: el hub **no** es una pieza SEO de cabeza |

**Lecciones de la SERP:**
- En «food cost template» compiten plantillas **gratuitas** (Airtable, RestaurantOwner, spreadsheet123, chefs-resources) y
  **Etsy**. El comprador espera **Excel Y Google Sheets**: los entregables EN tienen que funcionar en Google Sheets
  (fórmulas compatibles, sin macros) y la landing debe decirlo **solo cuando un test real lo compruebe**. Diferencial
  frente a lo gratis: sistema completo (13 plantillas + 2 bonus tras la v2.1), unidades y formatos de compra US/UK,
  impuesto y moneda configurables, y soporte. **No** «ingeniería de menú»: las plantillas no la hacen; solo el bono PDF
  trae una introducción (corregido el 24-sep, SPEC D15).
- PAA de «food cost template»: *Is 30% a typical food cost?* · *How to make food costing in Excel?* · *How to calculate
  food cost for a recipe formula?* → guion de la FAQ del piloto.
- El hub se posiciona por **marca y enlazado interno** (header, footer, portada EN, blog EN, herramientas gratuitas),
  no por una keyword de cabeza.

## 3. Arquitectura (preparada para 7 idiomas)

1. **Registro `astro-site/src/lib/tienda.ts`**, única fuente de verdad:
   - `TIENDAS: Record<Locale, {hubPath, segmento, moneda, activa}>`. `en → /en/digital-products, USD`. Segmentos reservados:
     `fr produits-numeriques · de digitale-produkte · it prodotti-digitali · pt produtos-digitais · nl digitale-producten`.
   - `tiendaHref(lang)` → `null` si la tienda de ese idioma no está activa (fr nunca enlaza a la tienda ES).
   - **Familias:** `kit-escandallos → {es: 'kit-escandallos', en: 'recipe-costing-kit'}`. De ahí salen los hreflang
     recíprocos ES↔EN y los enlaces cruzados.
2. **URLs anidadas bajo el hub de cada idioma:** landing `/en/digital-products/<slug>`, gate `/en/digital-products/<slug>/access`,
   dashboard `/en/digital-products/<slug>/library`.
   - ⚠️ El filtro del sitemap (`astro.config.mjs`, `/^\/[^/]+-(access|library)$/`) y `robots.txt` (anclado a `/kit-*`…)
     **solo protegen la raíz**. Por idioma: `Disallow: /en/digital-products/*/access` y `.../library`, y un filtro del
     sitemap que acepte el patrón anidado. Correr `robots-gate.py`.
   - El slug EN nativo se decide en la F1 de cada producto por volumen US/UK. **Nunca** empezar un slug de otro idioma por
     `kit- guia- mega- pack- plan- pro- manual-` en la raíz.
3. **`productId` EN propio** (= slug EN), con `lang: 'en'` en las 5 fuentes: `zona-app.ts`, PRODUCTS de
   `verify-purchase.ts` y `resend-access.ts`, `get-download-urls.ts`, `payment-links.ts`/`product-prices.ts`. Compras y
   accesos separados de los ES; el Payment Link lleva metadata `lang`.
4. **Plantillas parametrizadas, no bifurcadas.** `KitExcelLandingPage`, `GuiaLandingPage`, `KitTareasLandingPage`,
   `PlanNegocioLandingPage` y `ProPromptsEbookPage` ganan `lang` + diccionario de interfaz `astro-site/src/i18n/tienda/<lang>.json`.
   Datos EN en `astro-site/src/data/productos-en/<linea>/<slug>.ts` con **el mismo tipo** que los ES.
   **Condición dura: el HTML de las landings ES sale byte a byte idéntico** tras el cambio.
5. **Testimonios y reseñas (REVISADO por John, 25-sep-2026):** la landing de otro idioma replica la del ES también
   en la sección de testimonios: se TRADUCEN los del ES tal cual (nombres, negocios y cifras de origen), con el
   subtítulo diciendo que son de la edición española. Sin `aggregateRating` ni `review` en el JSON-LD. La tienda es
   UNA, en España: quien compra desde EE. UU. o Reino Unido le compra a aichef.pro en España («no estoy montando una
   tienda en Estados Unidos»).
6. **Backend con idioma:** asunto/cuerpo del email y el envoltorio fijo de `sendAccessEmail()` por idioma;
   `ProductAccessGate.tsx` y los dashboards con `copy`/`lang`; `product-prices.ts` → `{eur?, usd?}` y
   `crypto-checkout.ts` con la moneda del producto (regenerar con `sync-product-prices.py` / `sync-payment-links.py`).
7. **Navegación:** enlace a la tienda en **4 ficheros** (`Header.astro`, `Footer.astro`, `ModernHeader.tsx`,
   `ModernFooter.tsx`) vía `tiendaHref(lang)`, solo donde haya tienda activa, con `target="_blank"` y midiendo el ancho
   del menú EN.
8. ~~**Hub EN = componente nuevo `TiendaHubPage.astro`**~~ **REVOCADO por John el 24-sep (ver 0.C bis)**, dirigido por copy JSON y con tarjetas leídas del registro
   (patrón `IntegracionesPage.astro`). El monolito ES (`ProductosDigitalesHubPage.astro`) **no se toca**; solo gana
   `alternates` recíprocos. Secciones: productos EN vivos · «Coming in English» (hoja de ruta) · «¿Hablas español?»
   hacia los 50 productos ES (mercado hispano de EE. UU.) · FAQ + schema · buscador (`normalizar-busqueda.ts` +
   `log-search` con `lang`).
9. **Miselup:** su tarjeta lateral queda **fuera de EN** hasta que Miselup tenga EN (`miselup-gate.py` exige cero en `/en/`).
10. **Blog EN:** `products-catalog.ts` pasa de `url` a `urlByLang` (fallback ES). Cuando un producto tiene versión EN,
    sus banners del blog EN apuntan a ella y el `VETADO` de `fase8c-libreria-en-gate.py` se actualiza.

## 4. Fases

### Fase 0 — Estructura del hub (tamaño M: 2 sesiones, ≤ 5 M tokens)

- **0.A Fundamentos** ✅ 23-sep: research del hub y del piloto (§2), este documento, calendario y memorias.
- **0.B Infraestructura** ✅ 23-sep (PR #93, `42a6878`): `tienda.ts`, sitemap/robots, `lang` en plantillas y backend, `urlByLang`, gate
  `tienda-gate.py`, `gate-flujo-postpago.py` con rutas anidadas y moneda. Verificación en **deploy preview**.
- **0.C Hub EN** ✅ 24-sep (PR #94, `1161e6e`): `TiendaHubPage.astro` + `pages/en/digital-products.astro`, copy
  (bridge.py revisado → `data/tienda-hub/en.json`), imágenes (Nano Banana 2), `TIENDAS.en.activa`, enlace «Digital
  Products» en los 4 ficheros de navegación y `TiendaStrip.astro` en la portada EN. **Buscador del hub aplazado** hasta
  que haya ≥ 6 productos EN (con 0-1 no aporta).
- **0.C bis — hub EN = COPIA del hub ES** (24-sep, orden de John): `components/pages/DigitalProductsHubPage.astro` es
  el gemelo traducido de `ProductosDigitalesHubPage.astro` (mismas secciones, clases, imágenes y JS de filtros,
  «Load more» y buscador; **cualquier cambio de diseño se replica en los dos**). Las 50 tarjetas salen «Coming soon
  in English», sin precio ni enlace, hasta que su familia tenga `en.vivo: true` en `FAMILIAS` (entonces: enlace a la
  landing EN + precio USD de `product-prices.ts`). Borrados `TiendaHubPage.astro`, `data/tienda-hub/en.ts` y
  `public/tienda-en/recipe-costing-kit-card.jpg`. **`TiendaStrip.astro` (franja de la portada EN) también se borró** (John, 24-sep: la portada ES no la tiene), con `data/tienda-hub/en.json` y `public/tienda-en/tienda-en-hero.jpg`, que solo la alimentaban: las 7 portadas montan hoy los mismos componentes en el mismo orden.

### Por producto — política de 3 fases (F1 fundamentos · F2 entregables · F3 lanzamiento)

- **F1:** research US/UK (terminología, benchmarks etiquetados [medido]/[fuente]/[estimado]), SPEC de las diferencias
  con el ES, slug y precio USD.
- **F2** — ⚠️ método CORREGIDO por el piloto (24-sep, `recipe-costing-kit/SPEC.md` §2.1): no hay «motor» que regenerar,
  porque los xlsx publicados salen de capas encadenadas (generador v1.0 + Fase A + post-proceso v2.0). Se **copian
  los xlsx ES publicados** y se les aplica una capa EN (`aplicar_en.py`: hojas, claves-dato, textos, mercado,
  formatos, `inject_cache` al final). El gate es de **paridad estructural EN↔ES**, con excepciones declaradas. Texto
  original de este punto, superado: el motor v2.0 gana un parámetro `mercado` con tablas de textos (`textos_es.py`/`textos_en.py`). **Gate:**
  regenerar los xlsx ES y compararlos celda a celda con los publicados (tienen que salir idénticos). Textos EN con
  **subagentes Anthropic** (regla 1bis: nada de bridge en productos). Gates: sin español, sin no latinos, fórmulas
  intactas, **compatibles con Google Sheets**.
- **F3:** datos de landing EN, `access`/`library`, dashboard, `public/dl/<slug-en>/`, las tres puertas cripto. John crea
  el Payment Link USD. Gates LIVE, compra de prueba, banners del blog EN re-apuntados y broadcast EN en la cola de 5 días.

## 5. Olas (de menos a más dependencia del mercado español)

| Ola | Productos | Tamaño |
|---|---|---|
| 1 | **Recipe Costing Kit** (piloto) → Inventory Kit → Pro Prompts eBook (nombres EN de agentes desde `agentes-en.json`) → Food Safety / HACCP Pack (Codex + anexos FDA/FSA) | M · M · S · M |
| 2 | Motor de Kit de Tareas bilingüe (una vez) → 20 verticales | S cada uno, varios por sesión |
| 3 | Staff Management (FLSA / UK Working Time) · Financial Plan | M, duplicados del ES + anexos FLSA/UK |
| 4-5 | Manuales · guías «How to Open…» · planes de negocio | L, duplicados del ES + research de las variables del mercado |
| — | **Mega Pack: no se replica** (congelado; no vende) | — |

Precio de referencia: el ES en € redondeado a un escalón psicológico en USD por encima (12 € → **$19**). Se confirma en
la F1 de cada producto frente a Etsy/Gumroad.

## 6. Checklist de cierre de un producto EN

- [ ] En `tienda.ts` (familia) y en las 5 fuentes del backend con `lang: 'en'`.
- [ ] Landing, `access` y `library` bajo `/en/digital-products/<slug>`; hreflang recíproco con su gemelo ES.
- [ ] `robots-gate.py`, `tienda-gate.py`, `gate-flujo-postpago.py` LIVE, `whatsapp-gate.py` en verde.
- [ ] Cero español, cero `€` y cero caracteres no latinos en el HTML y en los entregables.
- [ ] Sin reseñas ni ratings inventados.
- [ ] Payment Link USD (John). **Sin compra de prueba** (John, 25-sep): acceso generado por admin + `gate-flujo-postpago.py --only <pid>` LIVE.
- [ ] Tarjeta viva en el hub EN; banners del blog EN re-apuntados; broadcast EN programado.
- [ ] **Antes de que el producto entre en `PRODUCTS`:** existe `/en/crypto-payment` (lee `?o=` y `&estado=parcial` como
      `/pago-cripto`) o el producto va en `CRYPTO_PRODUCTS_EXCLUDE`; con `CRYPTO_PRODUCTS=all` el botón cripto aparece
      solo y sus URLs de vuelta darían 404. `CryptoPayButton.astro` necesita `lang` (hoy tiene copy ES).
- [ ] Coherencia moneda ↔ idioma: precio `usd` en `product-prices.ts` ⇔ `lang: 'en'` en PRODUCTS (si no, factura en
      USD con correo y página de estado en español). Entrada también en `admin-generate-access.ts`.
- [ ] Handoff + memoria + commit con `Via: Claude Code` + push.

## 7. Log

- **2026-09-23 (sesión Claude Code):** frente abierto; plan aprobado; 0.A cerrada (research §2 + este doc).
- **2026-09-23/24 (sesión Claude Code):** 0.B LIVE (PR #93). Preview: 5/5 landings KitExcel ES byte a byte idénticas
  a producción (`tienda-gate --es-identico`), `robots-gate` verde. Dos lecciones:
  - **El compilador de Astro se rompe con template literals o backslashes DENTRO de las expresiones del template**
    (`{`\n${x}\n`}`, un `alt={`${a} ${i}`}` dentro de map + condicional) → build roto con «Expected ";" but found "$"».
    Se detecta sin build del sitio: `npm i @astrojs/compiler esbuild` en el scratchpad + `transform()` + `esbuild`
    sobre el `.astro` (script `astroc/c.mjs` de la sesión). Hacerlo SIEMPRE antes de subir una plantilla tocada.
  - **Los 500 intermitentes («Error - Request ID …», 46 bytes) eran de la IP del Mac, no del sitio:** fallaban igual el
    deploy anterior y `favicon.ico`, mientras el Chrome de Windows daba 40/40 en 200 y otros sites de Netlify 0 fallos.
    Tras ráfagas de gates, Netlify estrangula esa IP: repetir los gates LIVE más tarde o desde otra red antes de
    dar un fallo por bueno.
- **2026-09-24 (sesión Claude Code):** 0.C LIVE (PR #94). El hub enseña el Recipe Costing Kit como «First release» sin
  enlace ni precio: la tarjeta pasa sola a la rejilla cuando `FAMILIAS` lo marque `vivo: true` (y su precio `usd` exista
  en `product-prices.ts`, o saldrá sin precio). Lecciones:
  - **`BaseLayout` emite por defecto un `SoftwareApplication` con ofertas en EUR y `aggregateRating` 4,8.** Toda página
    de la Tienda internacional en inglés necesita `omitGlobalApp`, o viola la capa comercial honesta (§3.5) y `tienda-gate --base` cae por «EUR».
  - **El item de la tienda en el menú es lo que empuja a un idioma por encima de `xl`.** Header.astro y ModernHeader.tsx
    muestran el menú completo desde 1.360 px en todo idioma con tienda activa (antes solo ES).
  - **La SPA no importa de `astro-site/`:** el mapa de la tienda va duplicado en `ModernHeader/ModernFooter.tsx`
    (`TIENDA_PATHS`/`TIENDA_NOMBRE`) y `tienda-gate.py` lo cruza con `tienda.ts`. Al activar otra tienda, tocar los tres.
  - Los 500 de la IP del Mac volvieron (hasta `favicon.ico`). Los gates de red se reprodujeron desde el Chrome de Windows
    con `fetch()` + `DOMParser`: hreflang recíproco, canonical, JSON-LD sin EUR, 0 € fuera del bloque ES, 1 WhatsApp,
    DataFast 1, Miselup 0, sitemap con el hub y sin dashboards.
  - Medir el menú a un ancho concreto exige que el viewport CSS lo sea: con `documentElement.style.width` las media
    queries siguen en escritorio (en ese Chrome, 1.653 px CSS con la ventana a 1.375).
- **2026-09-24 (sesión Claude Code) — hubs de las 7 tiendas LIVE.** El hub EN hecho desde cero (`TiendaHubPage.astro`) se
  tiró: John exige DUPLICAR lo español (§1). `DigitalProductsHubPage.astro` = copia traducida de `ProductosDigitalesHubPage.astro`
  (PR #95) y `DigitalProductsHubPage{Fr,De,It,Pt,Nl}.astro` = copias traducidas de esa (PR #96, traducción con bridge.py y Sonnet
  de respaldo). Tarjetas sin precio ni enlace («Coming soon in <idioma>») hasta que `FAMILIAS` marque `vivo` en ese idioma.
  Sin estrellas ni 4,9/5 fuera de ES. `hubLocales()`/`hubAlternates()` en `tienda.ts` → hreflang recíproco de los 7 hubs;
  enlace en menú y pie de cada portada (4 ficheros de navegación); menú completo desde 1.360 px en los 7 idiomas (medido en el
  Chrome de Windows a 1.362 px: una fila, sin solapes) y 0 desbordes a 360 px en los 6 hubs. `tienda-gate.py --base` cubre ya
  todas las tiendas activas. Lecciones:
  - **Los traductores arrastran «ediciones en inglés» del hub EN** a la FAQ de disponibilidad: pasó en IT, PT y NL. Al traducir
    desde la copia EN, grep del nombre del idioma de origen.
  - **Una copia por idioma = un cambio de diseño se replica en 7 ficheros.** Es el precio de la regla de John; está anotado en
    la cabecera de cada componente.
- **2026-09-24 (tarde, sesión Claude Code):** John decide (1) quitar `TiendaStrip` de la portada EN — las 7 portadas quedan con los mismos componentes que la ES— y (2) que el aviso cripto EN diga que se renuncia al derecho de cancelación de 14 días «where it applies (EU/UK)» (`netlify/shared/email-i18n.ts`): correcto en EU y UK, neutro en EE. UU. El diálogo cripto EN (F3 del piloto) tiene que pedir la misma renuncia con esa redacción.
- **2026-09-24 (noche, sesión Claude Code) — piloto Recipe Costing Kit Pro, F1 cerrada.**
  - Inventario, research US/UK y research de 8 bloques con OK de John.
  - SPEC con 2 rondas adversariales (37 + 46 hallazgos incorporados).
  - Decisiones de John: producto EN independiente; anclas como en ES; Yield Test e Ingredient Price List en ES v2.1 y EN a la vez; licencia de un negocio (todos sus locales) por compra.
  - Lecciones:
    - la fuente de un duplicado son **los ficheros publicados**, nunca el generador original;
    - una tabla de conversiones «editable» tiene que tener filas libres dentro del rango del VLOOKUP (defecto heredado del ES);
    - un «service charge» no se puede usar como nombre de un margen interno;
    - las FAQ de licencia de los kits hermanos («todos tus locales», «ideal para consultores») se revisan contra la licencia D18 al duplicarlos.
- **2026-09-25 (tarde, sesión Claude Code) — broadcast EN del Food Cost Kit Pro programado** (lunes 28-sep 14:00 UTC,
  segmento «AI Chef Pro EN», from `hello@`). Un solo correo: tienda EN + primer producto + los tres siguientes de la ola 1 +
  «responde con el que necesitas primero». Reglas para los siguientes lanzamientos EN:
  - **Cola EN propia**: +5 días sobre el último envío al segmento EN, nunca el mismo día que un correo de producto ES, 14:00 UTC.
  - **No decir que el hub «muestra cuáles vienen»**: todas las tarjetas pendientes llevan el mismo «Coming soon in English».
  - Cuando haya 4-5 productos EN vivos, tiene sentido un correo-resumen de la tienda; antes, cada lanzamiento presenta la tienda.
- **2026-09-25 (tarde, sesión Claude Code) — ola 1, producto 2: «Restaurant Inventory Kit Pro», F1 CERRADA** (duplicado del Kit de
  Inventario ES, 9 xlsx, 14 € → **$19**; slug `restaurant-inventory-templates`). Tamaño **S** (techo 2,5 M): F1 = un solo
  implementador opus, **0,37 M**, sin fan-out. Nombre por datos DataForSEO US (familia «restaurant inventory»: management 720 ·
  spreadsheet/sheet 320 · template 210; «food/kitchen inventory template» 480 pero la SERP mezcla despensa doméstica). Docs en
  `scripts/productos-digitales/restaurant-inventory-kit/` (`SPEC.md` D1-D26, `F1-inventario-es.md`, `censo_es.json`, `mapas.py`,
  `gate_f1.py` verde). Nace corregido de 4 defectos heredados del ES (D23: el ES los corrige en su próxima v2.x).
  **Retomar F2:** `cd scripts/productos-digitales/restaurant-inventory-kit && python3 gate_f1.py` y seguir `SPEC.md` §7 (pipeline del
  piloto: textos EN por subagentes sonnet por grupos → `aplicar_en` adaptado → gates §8 contra el censo). Máquina: Mac en serie con vigilante (S).
- **2026-09-25 (noche, sesión Claude Code) — «Restaurant Inventory Kit Pro», F3 (capa de producto) en la rama
  `feat/restaurant-inventory-kit-en`.** Réplica del piloto pieza a pieza: ficha EN `productos-en/kits/restaurant-inventory-templates.ts`
  (copia de `kit-inventario.ts`, H1 = title D2 en Forma B, testimonios del ES traducidos, sin rating), 3 páginas anidadas,
  dashboard + island, familia `kit-inventario` viva en `tienda.ts`, `zona-app.ts`, 4 functions con `lang: 'en'`, hreflang
  recíproco en `/kit-inventario` (el HTML ES solo cambia en esas líneas: `tienda-gate --es-identico --esperadas /kit-inventario`),
  `VITE_STRIPE_PAYMENT_LINK_RESTAURANT_INVENTORY_KIT` en Netlify (scope builds, contexto all, igual que el piloto),
  `payment-links.ts`/`product-prices.ts` regenerados ($19), Payment Link verificado con la CLI de Stripe (USD 19,00,
  redirección a `…/restaurant-inventory-templates/access?session_id={CHECKOUT_SESSION_ID}`), catálogo con `urlByLang`/`priceByLang`,
  4 banners del blog EN re-apuntados, 7 menciones de `/en/usos/` renombradas (enlazan vía alias), tarjeta del hub EN viva y
  primera (los productos vivos EN van arriba, el más nuevo en 1, con badge «New»).
- **2026-09-25 (noche, sesión Claude Code) — Restaurant Inventory Kit Pro LIVE** (PR #103, `2b6afb33`): F2 (9 xlsx, gates G1-G8,
  autotest 9/9) + F3 (landing, acceso, dashboard, 4 functions, Payment Link `plink_1UJf3q…` verificado con la CLI de Stripe, tarjeta
  viva en el hub EN, 4 banners del blog EN, usos EN). Gates contra preview y LIVE en verde (`/kit-inventario` solo cambia en el
  hreflang). Coste del producto: **1,90 M** de 2,5 M. Correo propio: **5-oct 14:00Z** (`5dd96142-…`); el del 28-sep ya lo nombra
  como «already out». Pendientes: acceso admin (la contraseña que da la CLI de Netlify viene enmascarada → John genera el
  enlace desde `/admin/generar-acceso`) y **galería de capturas** (piloto en este producto; ver memoria del proyecto).
