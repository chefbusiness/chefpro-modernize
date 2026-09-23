# Tienda internacional de productos digitales — doc canónico

> Frente abierto por John el **2026-09-23** (sesión Claude Code). Primero inglés (`/en/digital-products`) y después, de
> forma progresiva, fr/de/it/pt/nl: los idiomas en los que ya viven la plataforma y las landings principales.
> Leer este documento ENTERO antes de tocar cualquier pieza de la tienda en otro idioma.

## 1. Decisiones de John (23-sep-2026)

| Tema | Decisión |
|---|---|
| Cuándo | **Ya**, sin esperar a cerrar el catálogo ES (deroga §0-bis.3 del calendario del 31-ago) |
| Cadencia | **Rotación de 3 sesiones:** v2.0 ES → producto nuevo ES → producto EN → … (mismo techo de tokens) |
| Mercado | Inglés **US como base internacional**. Impuesto (sales tax/VAT), moneda ($/£/CAD/AUD) y unidades (oz-lb ↔ g-kg) son **parámetros** del Excel. Lo normativo: núcleo HACCP/Codex + **anexo US** (FDA Food Code) + **anexo UK** (FSA, 14 alérgenos). Un SKU sirve a US/UK/CA/AU |
| Moneda | Payment Links en **USD**, precio psicológico ($19/$29/$49…), con **Adaptive Pricing** de Stripe activado (UK ve £, CA ve CAD). NOWPayments factura en USD |
| Piloto | **Recipe Costing Kit** (= `kit-escandallos`) |
| Nativo, no traducido | Terminología, benchmarks, normativa y ejemplos del mercado anglosajón. Se reutilizan los **motores**, no el contenido regulatorio |

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
  (fórmulas compatibles, sin macros) y la landing debe decirlo. Diferencial frente a lo gratis: sistema completo (12
  plantillas + guía), unidades y moneda configurables, ingeniería de menú y soporte.
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
5. **Capa comercial honesta:** en EN, **sin testimonios, sin ratings y sin `aggregateRating`** hasta que haya compradores
   EN reales. Las reseñas ES no se traducen ni se reutilizan. Garantía y FAQ, sí.
6. **Backend con idioma:** asunto/cuerpo del email y el envoltorio fijo de `sendAccessEmail()` por idioma;
   `ProductAccessGate.tsx` y los dashboards con `copy`/`lang`; `product-prices.ts` → `{eur?, usd?}` y
   `crypto-checkout.ts` con la moneda del producto (regenerar con `sync-product-prices.py` / `sync-payment-links.py`).
7. **Navegación:** enlace a la tienda en **4 ficheros** (`Header.astro`, `Footer.astro`, `ModernHeader.tsx`,
   `ModernFooter.tsx`) vía `tiendaHref(lang)`, solo donde haya tienda activa, con `target="_blank"` y midiendo el ancho
   del menú EN.
8. **Hub EN = componente nuevo `TiendaHubPage.astro`**, dirigido por copy JSON y con tarjetas leídas del registro
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
- **0.C Hub EN:** `TiendaHubPage.astro` + `pages/en/digital-products.astro`, copy (bridge.py, fallback Sonnet),
  imágenes (`generate-images`, mockups en inglés), navegación EN y CTA en la portada EN. PR → gates → merge → LIVE.

### Por producto — política de 3 fases (F1 fundamentos · F2 entregables · F3 lanzamiento)

- **F1:** research US/UK (terminología, benchmarks etiquetados [medido]/[fuente]/[estimado]), SPEC de las diferencias
  con el ES, slug y precio USD.
- **F2:** el motor v2.0 gana un parámetro `mercado` con tablas de textos (`textos_es.py`/`textos_en.py`). **Gate:**
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
| 3 | Staff Management (FLSA / UK Working Time) · Financial Plan | M, rehechos nativos |
| 4-5 | Manuales · guías «How to Open…» · planes de negocio | L, research nativo completo |
| — | **Mega Pack: no se replica** (congelado; no vende) | — |

Precio de referencia: el ES en € redondeado a un escalón psicológico en USD por encima (12 € → **$19**). Se confirma en
la F1 de cada producto frente a Etsy/Gumroad.

## 6. Checklist de cierre de un producto EN

- [ ] En `tienda.ts` (familia) y en las 5 fuentes del backend con `lang: 'en'`.
- [ ] Landing, `access` y `library` bajo `/en/digital-products/<slug>`; hreflang recíproco con su gemelo ES.
- [ ] `robots-gate.py`, `tienda-gate.py`, `gate-flujo-postpago.py` LIVE, `whatsapp-gate.py` en verde.
- [ ] Cero español, cero `€` y cero caracteres no latinos en el HTML y en los entregables.
- [ ] Sin reseñas ni ratings inventados.
- [ ] Payment Link USD con Adaptive Pricing + compra de prueba (email EN, dashboard, descargas).
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

