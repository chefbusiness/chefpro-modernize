# Chocolate Shop Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 24-oct-2026. Implementador único de la F3 de los DOS hermanos (chocolate y pastelería) en
> `feat/chocolate-pastry-checklists-en-f3` (sale de `28efc8d3`; la F2 de la pastelería sigue en la rama hermana
> `feat/chocolate-pastry-checklists-en`). Molde: la F3 del Ice Cream Shop (`../icecream/F3-NOTAS.md`, commits `9e3918e5`,
> `06942e8a`, `516052bc`, `c6d2b251`, `12592f32`, `d76fdec5`) punto por punto. Sin build, Playwright ni navegador
> (regla térmica; CPU 42-51 °C toda la sesión). No toca `checklists-kit/` (salvo este fichero y el de pastry) ni
> `astro-site/public/dl/`. Notas de la pastelería: `../pastry/F3-NOTAS.md`.

## 1. Puntos de registro (los 25 del icecream, para `chocolate-shop-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla con `lang` | `KitTareasLandingPage.astro` | sin cambios |
| 2 | Ficha EN (todas las secciones de `kit-tareas-chocolateria.ts`) | `astro-site/src/data/productos-en/tareas/chocolate-shop-checklist-templates.ts` | ✅ |
| 3 | Landing | `pages/en/digital-products/chocolate-shop-checklist-templates.astro` | ✅ `omitGlobalApp`, `miselup={false}`, `whatsapp={false}`, env `VITE_STRIPE_PAYMENT_LINK_CHOCOLATE_SHOP_CHECKLISTS_KIT` → `#comprar` sin link |
| 4 | Gate `/access` | `…/chocolate-shop-checklist-templates/access.astro` | ✅ |
| 5 | Dashboard `/library` + island | `…/library.astro`, `islands/library/ChocolateShopChecklistsKitLibraryIsland.tsx`, `src/pages/ChocolateShopChecklistsKitDashboard.tsx` | ✅ 12 tarjetas, claves e iconos del ES (02 = `partidas`); cruza a Pastry Shop, Ice Cream Shop y Food Cost Kit Pro (§3) |
| 6 | Gemelo ES con hreflang recíproco | `pages/kit-tareas-chocolateria.astro` → `alternatesFamilia('kit-tareas-chocolateria')` | ✅ (solo el `<head>`) |
| 7 | Familia `kit-tareas-chocolateria` → `en: …, vivo: true` | `lib/tienda.ts` | ✅ (fusionar con el link) |
| 8 | Zona app `lang: 'en'` | `lib/zona-app.ts` | ✅ |
| 9 | PRODUCTS `lang: 'en'` | `verify-purchase.ts`, `resend-access.ts` | ✅ |
| 10 | Descargas: claves del ES → 11 xlsx EN + `equivalents-guide` | `get-download-urls.ts` | ✅ nombres = `SPEC.md` §2 = los 11 de `dl/` (cruzado por script: 0 de más, 0 de menos; también con `productos-digitales-config.ts`) |
| 11 | Precio `{ usd: 19 }` | `product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (76 productos, 25 priceByLang) |
| 12 | Payment Link | `payment-links.ts` vía `sync-payment-links.py` | ⏳ John |
| 13 | Admin de accesos | `admin-generate-access.ts`, `AdminGenerateAccess.tsx` | ✅ |
| 14 | Config SPA y changelog | `productos-digitales-config.ts`, `productos-changelog.ts` | ✅ v2.1 «First English edition» (D2: 2.1 en los 11 libros) |
| 15 | Catálogo: `name.en`, `description.en`, `urlByLang.en`, `priceByLang.en` | `src/data/products-catalog.ts` | ✅ (los casos de uso EN que listan el kit —concept/chocolate-shop, role/chocolatier, consultancy del chocolatero— pasan a enlazar la landing EN) |
| 16 | Alias de enlace | `linkify-use-case.ts` / `.tsx` | ✅ nombre nuevo + el viejo «Tasks: Chocolate Shop» (no aparece en ningún texto EN hoy; por si vuelve) |
| 17 | Hub EN: la tarjeta sube a la 2 (Pastry Shop 1, Ice Cream Shop 3) con copy EN | `DigitalProductsHubPage.astro` | ✅ (decía «11 templates», «counter staff, manager»; imagen del ES con rótulos en francés → el hero EN) |
| 18 | `footerLinks` cruzados | 13 fichas EN (+ la del icecream) | ✅ +2 líneas cada una (Chocolate y Pastry, tras el Ice Cream Shop) |
| 19 | GEO: `llms.txt` y `llms-full.txt` («25 products») | `astro-site/public/` | ✅ + fila «Daily operating checklists» |
| 20 | Sitemap lastmod | `sitemap-lastmod.json` | ✅ |
| 21 | Blog EN: banners + párrafo | — | ❌ NO (el blog es de la sesión Cursor) → §5 |
| 22 | TEMAS para rebalanceos | — | ❌ NO (ídem) |
| 23 | `tienda-gate.py`: exentos (8 nombres + el subtítulo de la edición ES) y `/kit-tareas-chocolateria` en el comentario de `--esperadas` | `tienda-gate.py` | ✅ estático VERDE (25 vivos fuera de ES) |
| 24 | Correo EN | `emails/broadcast-chocolate-shop-checklists-lanzamiento-en.{html,subject.txt}` | ✅ sin programar; «Hi everyone,» |
| 25 | Cripto + devoluciones | plantilla | ✅ |

## 2. Verificación (ligera, sin build)

- `es-identico-local/comparar.mjs --ref main --en data/productos-en/tareas` (`ASTRO_NM=/Users/johnguerrero/johnguerrero-es-astro/node_modules`):
  **ES idénticas 40 · distintas 0**. El `<head>` de `/kit-tareas-chocolateria` cambia a propósito (hreflang es + en +
  x-default): lo mide `tienda-gate --es-identico --esperadas /kit-tareas-chocolateria` en el preview.
- Render EN (254.672 bytes): `revisar_texto` de `tienda-gate` **0 fallos** (cazó «Obrador Beltrán» → a EXENTOS;
  mutación comprobada con una tilde de más), 0 `aggregateRating`/`review`, `priceCurrency` USD, H1 = title SEO
  (73 car.; description 158), 6 `Question`; «€» 9 y «Google Sheets» 8 = las constantes de la plantilla (igual que el
  icecream); «EUR» 1 = la FAQ de moneda. «Chocolatería» / «Bombonería» / «Obrador» solo en el subtítulo de la edición
  española y en los negocios de los testimonios.
- °F de la ficha: todos dentro de `GRADOS_F_SPEC` (0, 32, 41, 54, 57, 59, 60, 64, 68, 72, 77, 79, 81, 82, 84, 86, 88, 90,
  100, 104, 113, 122, 131); °C solo en la FAQ UK.
- esbuild (stdin) de los TS/TSX y frontmatter .astro tocados: 0 errores. `sync-product-prices.py --check` verde.
  `tienda-gate.py` estático verde.
- `gate-flujo-postpago.py --offline --only chocolate-shop-checklist-templates`: 12/12 ficheros = tarjetas, 0 issues de
  disco; falla SOLO «SIN Payment Link» (y avisa de las secciones D y E, de red).

## 3. Decisiones de contenido

- **Cifras: las de los xlsx EN de la F2 tras la ronda 1** (`F2-NOTAS.md` «Cifras para la landing», contrastadas con
  `revision/dump_en.txt`): 338 tareas en 37 hojas; 41 en el 01 (25 + 16), 32 en el 08 con responsable (horas 9:00-9:30 AM en
  la apertura y «Close» en el cierre; la tienda abre a las 10 AM, D9), 12 meses en el B02. Temperaturas (D-CHOC): obrador
  64–68 °F y 50–60 %, cool room 59–64 °F, vitrina 60–64 °F y < 55 %, tienda 68–72 °F, moldes 68–72 °F, enfriado 54–57 °F,
  nevera 41 °F; curvas «typical curve; your couverture's chart rules»; temperadora «typically 113 °F». Food cost 30–35 %
  (03 «Weekly Tasks», Friday: criterio del kit, sí está en el xlsx). Porcentajes de cacao 55–70 / 30–40 / 28–33 % (ronda 1, m2).
- **Ronda 1 en la landing:** ganache de nata fresca = TCS hasta un análisis de aw y pH (41 °F, nevera o vitrina
  refrigerada, 7 días, nunca la vitrina de 60–64 °F ni la cool room) en la FAQ de apertura, cierre, vida útil y
  temperaturas, en la tarjeta 02 y en el changelog; contacto cruzado (pinzas por bandeja, frutos secos y cacahuete al
  final, temperadora limpia de leche a negro o blanco, guantes nuevos para alérgicos); exclusión por vómitos, diarrea o
  ictericia; licor > 0,5 % solo donde el estado lo permite (y envíos solo a esos estados; 21+ en algunos) en la FAQ de
  licencias; menores de 16 sin temperadora ni bombo.
- **Fuera lo que el ES afirma y el kit no trae:** «software de gestión €40/mes» y «sin internet» (→ fórmula de los
  hermanos), «Imprimible A4» (→ US Letter), DDD / BIE / legionela / «SAT de cámaras» (→ servicios contratados US, D11),
  Reyes, comuniones, 15 de agosto, Todos los Santos y «puente de diciembre» (→ fechas US, D14), «moldes» en el inventario
  semanal (el EN los cuenta en el mensual) y, en el dashboard ES, «15 fechas clave» (son 12 meses). Precio de lanzamiento
  / −69 % / «valorados en €33» / aggregateRating 4,9 con 3 reviews → fórmula EN sin anclas ni rating.
- **Parche ES de hoy (`938e15e3`) frente a la ficha ES:** la ficha ES de chocolatería no da vida útil ni temperatura de
  vitrina para la ganache (solo «vitrina temperada» en la tarjeta 01, genérico), así que **no queda contradicción** en su
  copy. No se ha tocado (gate de ES idénticas).
- **Testimonios: los 8 tal cual** (ninguno cita marca o persona real, SPEC §R) y **ninguna frase cambiada**: Sergio
  Herrera («food cost y mermas de producción en el checklist del manager») casa con el 03 (diario «Track waste and
  discarded chocolate», martes «Review accumulated waste», viernes food cost); Andrés Beltrán cita «ferias» y el B02 trae
  «local food fairs» en septiembre (y el 06 «Add local fairs»). Roles traducidos; negocios conservados («Chocolatería
  Roca», «Bombonería La Trufa Dorada»…); «Cadena Chocolaterías Mendoza» → «Mendoza chocolate shop chain»; «Consultora
  gastronómica, Chocolaterías & Obradores» → «Hospitality Consultant, chocolate shops and production kitchens».
- **Imágenes (todas miradas):** las 6 del ES llevan texto o marcas ajenas: hero y vitrina con «Atelier du Chocolat»
  (nombre de una cadena francesa real) y rótulos en francés mal escritos; obrador con la marca **Selmi** en la temperadora
  y «OBRADOR ARTESÀ»; equipo con el logo «Gami» en la temperadora; servicio con «Couture Chocolats» en cajas y delantal.
  Se queda solo `tareas-chocolateria-produccion` (sin texto). El resto, fotos YA publicadas en los casos de uso EN de
  chocolatería y chocolatero: `use-case-chocolatero-bombones` (hero, OG, cta, tarjeta del hub y correo; sin texto),
  `use-case-chocolateria-display` (rótulos en inglés: «Salted Caramel», «Single Origin Peru»…), `use-case-chocolateria-obrador`
  (mesa de templado, sin texto legible), `use-case-chocolateria-team` (relleno de moldes con guantes, «HANDCRAFTED
  CHOCOLATES»; bonus 1) y `use-case-chocolateria-bonbons` (bandeja; bonus 2). Descartadas también
  `use-case-chocolateria-hero` (rótulos en español y €) y `consultor-chocolatero-equipo` (logo Selmi). **No hace falta
  generar ninguna**; opcional, una OG EN propia.
- **Cruces del dashboard:** Pastry Shop y Ice Cream Shop Checklists (los hermanos de postre: muchas chocolaterías venden
  pastelería o helado) y Food Cost Kit Pro (el ES cruza a Escandallos). El ES cruza además al Kit Tareas Restaurante: en EN
  el Restaurant Checklists queda en el pie. El dashboard del icecream NO se ha tocado (sigue Coffee Shop, Restaurant y Food
  Cost): los tres kits de postre se cruzan entre sí por el pie, y así el icecream no depende de que estos dos se publiquen.
- **Pie:** los 9 hermanos de checklists, los 5 kits EN, el eBook y el caso de uso EN de chocolatería
  (`/en/use-cases/concept/chocolate-shop`, saliente extra como el icecream).
- **FAQ:** 20 on-page (apertura, cierre, templado, ganache y vida útil, temperaturas, alérgenos y etiquetas, licencias
  estatales y licor, temporada, venta al peso y encargos, limpieza, plantilla gratis, ya rellenas, tamaños de negocio,
  firma, Trail, varias tiendas, UK/CA/AU, moneda, suscripción, garantía) y 6 en el JSON-LD. UK: rangos en °C (obrador
  18–20, cool room 15–18, vitrina 16–18, tienda 20–22 °C), ganache fresca a 8 °C o menos, 14 alérgenos; hojas 08-09
  protegidas sin contraseña (como el base).

## 4. Pendiente

1. **John:** Payment Link USD $19 con redirección a
   `/en/digital-products/chocolate-shop-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` y env
   `VITE_STRIPE_PAYMENT_LINK_CHOCOLATE_SHOP_CHECKLISTS_KIT` (scope builds); luego `sync-payment-links.py`.
2. `vivo: true` ya en la rama: fusionar SOLO con el link (los 11 xlsx ya están en `dl/`) o volver a `vivo: false`.
3. **Fuera de mi carril (lo hace quien lleve la F2):** `postprocess-transversal.py` `EXCLUIDOS` no tiene
   `chocolate-shop-checklist-templates` ni `pastry-shop-checklist-templates` (el icecream entró en su F1, `c5f9772c`).
   Recorre las carpetas de `dl/`: un `all` les forzaría A4 y español. Una línea; no lo he tocado para no chocar con la
   rama hermana.
4. Preview: `tienda-gate --base` y `--es-identico --esperadas /kit-tareas-chocolateria` (con los otros gemelos),
   `whatsapp-gate`, `robots-gate`; render visual de landing, hub y dashboard.
5. LIVE: acceso por admin + `gate-flujo-postpago --only chocolate-shop-checklist-templates`; sitemap en GSC; correo a la
   cola EN (siguiente hueco) con su routine.

## 5. Blog EN (para la sesión Cursor; puntos 21-22 no hechos)

Posts EN que encajan para banner + párrafo hacia esta landing (menciones de chocolate / bonbon / truffle / tempering):
- `prompt-library-creative-chocolate` (310): el mejor; banner tras la sección de templado o de bombones. Hoy lleva
  banners de Food Cost, HACCP y el eBook.
- `prompt-library-chocolate-consulting` (291): para el consultor que entrega checklists al cliente (cuadra con el
  testimonio de Patricia Vega). Hoy: Food Cost, HACCP y Financial Plan.
- Secundario: `prompt-library-creative-pastry` (103).
Víctima sugerida en el rebalanceo: uno de los dos banners genéricos (HACCP o Food Cost) de cada post de chocolate.
