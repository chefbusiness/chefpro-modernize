# Pastry Shop Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 24-oct-2026. Implementador único de la F3 de los DOS hermanos en
> `feat/chocolate-pastry-checklists-en-f3` (sale de `28efc8d3`). La F2 de la pastelería va en la rama hermana
> `feat/chocolate-pastry-checklists-en`: sus 15 xlsx y los volcados entraron allí en `7fd4a21b` mientras esta F3 estaba
> en marcha; las cifras de abajo salen de ese `revision/dump_en.txt` (leído con `git show`, sin traerlo a esta rama) y
> quedan **a confirmar tras la ronda de revisión de la pastelería**. Molde: la F3 del Ice Cream Shop
> (`../icecream/F3-NOTAS.md`) punto por punto; notas del chocolate y lo común (verificación, render, pendientes de
> preview) en `../chocolate/F3-NOTAS.md`. Sin build, Playwright ni navegador (regla térmica; CPU 42-51 °C). No toca
> `checklists-kit/` (salvo este fichero y el del chocolate) ni `astro-site/public/dl/`.

## 1. Puntos de registro (los 25 del icecream, para `pastry-shop-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla con `lang` | `KitTareasLandingPage.astro` | sin cambios |
| 2 | Ficha EN (todas las secciones de `kit-tareas-pasteleria.ts`; como el ES, 13 tarjetas en el grid, bonus solo en su sección y `gridGallery` propio) | `astro-site/src/data/productos-en/tareas/pastry-shop-checklist-templates.ts` | ✅ |
| 3 | Landing | `pages/en/digital-products/pastry-shop-checklist-templates.astro` | ✅ `omitGlobalApp`, `miselup={false}`, `whatsapp={false}`, env `VITE_STRIPE_PAYMENT_LINK_PASTRY_SHOP_CHECKLISTS_KIT` → `#comprar` sin link |
| 4 | Gate `/access` | `…/pastry-shop-checklist-templates/access.astro` | ✅ |
| 5 | Dashboard `/library` + island | `…/library.astro`, `islands/library/PastryShopChecklistsKitLibraryIsland.tsx`, `src/pages/PastryShopChecklistsKitDashboard.tsx` | ✅ 16 tarjetas, claves e iconos del ES (02 = `partidas`; 10-13 = `plan-produccion`, `encargos`, `alergenos`, `temperaturas`), sin la marca «NUEVO v2.0»; cruza a Chocolate Shop, How to Open a Pastry Shop y Food Cost Kit Pro (§3) |
| 6 | Gemelo ES con hreflang recíproco | `pages/kit-tareas-pasteleria.astro` → `alternatesFamilia('kit-tareas-pasteleria')` | ✅ (solo el `<head>`) |
| 7 | Familia `kit-tareas-pasteleria` → `en: …, vivo: true` | `lib/tienda.ts` | ✅ (fusionar con el link Y con los 15 xlsx en `dl/`) |
| 8 | Zona app `lang: 'en'` | `lib/zona-app.ts` | ✅ |
| 9 | PRODUCTS `lang: 'en'` | `verify-purchase.ts`, `resend-access.ts` | ✅ (correo: «the 13 Excel templates, the 2 bonus templates and the Equivalents Guide») |
| 10 | Descargas: claves del ES → 15 xlsx EN + `equivalents-guide` | `get-download-urls.ts` | ✅ nombres = `SPEC.md` §2 = los 15 de `dl/` en la rama hermana (`git ls-tree` contra el mapa: 0 de más, 0 de menos; también con `productos-digitales-config.ts`) |
| 11 | Precio `{ usd: 19 }` | `product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (76 productos) |
| 12 | Payment Link | `payment-links.ts` vía `sync-payment-links.py` | ⏳ John |
| 13 | Admin de accesos | `admin-generate-access.ts`, `AdminGenerateAccess.tsx` | ✅ |
| 14 | Config SPA y changelog | `productos-digitales-config.ts`, `productos-changelog.ts` | ✅ **v2.0** «First English edition»: los 15 xlsx EN dicen «Version 2.0 · October 2026» (la SPEC no fija otra; el ES mezcla 2.0 y 2.1 y su ficha dice 2.1) |
| 15 | Catálogo | `src/data/products-catalog.ts` | ✅ (los casos de uso EN que listan el kit —concept/bakery-pastry-shop, role/pastry-chef, consultancy/pastry-consultant— pasan a enlazar la landing EN) |
| 16 | Alias de enlace | `linkify-use-case.ts` / `.tsx` | ✅ nombre nuevo + el viejo «Tasks: Pastry Shop / Bakery» |
| 17 | Hub EN: la tarjeta sube a la 1 (Chocolate Shop 2, Ice Cream Shop 3) con copy EN | `DigitalProductsHubPage.astro` | ✅ (decía «journeyman», «Epiphany» y «15 templates»; imagen del ES sin texto, se queda) |
| 18 | `footerLinks` cruzados | 13 fichas EN + How to Open a Pastry Shop | ✅ (+2 líneas en cada ficha EN; +1 en la guía: la operación diaria de la pastelería que enseña a abrir) |
| 19 | GEO: `llms.txt` y `llms-full.txt` («25 products») | `astro-site/public/` | ✅ |
| 20 | Sitemap lastmod | `sitemap-lastmod.json` | ✅ |
| 21-22 | Blog EN y TEMAS | — | ❌ NO (sesión Cursor) → §5 |
| 23 | `tienda-gate.py`: exentos (5 nombres nuevos; Laura Fernández, Ana Belén Torres, Isabel García y Fernando López ya estaban) + el subtítulo de la edición ES, y `/kit-tareas-pasteleria` en el comentario de `--esperadas` | `tienda-gate.py` | ✅ estático VERDE |
| 24 | Correo EN | `emails/broadcast-pastry-shop-checklists-lanzamiento-en.{html,subject.txt}` | ✅ sin programar; «Hi everyone,» |
| 25 | Cripto + devoluciones | plantilla | ✅ |

## 2. Verificación

- ES idénticas 40/0 (`comparar.mjs`, ver las notas del chocolate). Render EN (263.481 bytes): `revisar_texto` **0 fallos**
  (antes, «sablée / brisée» habrían saltado por la «é»: reescrito como «sweet and savory tart bases»), 0 rating/review,
  USD, H1 = title SEO (71 car.; description 148), 6 `Question`. «Pastelería» / «Obrador» solo en el subtítulo de la
  edición española y en los negocios de los testimonios.
- °F dentro de `GRADOS_F_SPEC` (0, 32, 36, 41, 45, 68, 70, 72, 75, 82, 135, 350, 375, 400); °C solo en la FAQ UK (8 °C, −18 °C).
- `gate-flujo-postpago.py --offline --only pastry-shop-checklist-templates`: 16/16 ficheros = tarjetas; fallan los 15 xlsx
  «NO en disco» (están en la rama hermana, no en esta) y «SIN Payment Link». Tras fusionar las dos ramas debe quedar
  solo el del link.

## 3. Cifras (A CONFIRMAR tras la ronda de la pastelería) y decisiones de contenido

- **Tareas: 413** en los 9 checklists y el briefing, con el método de los hermanos (filas con número en A y texto en B;
  da 298 en la heladería y 338 en el chocolate): 01 = 22 + 20 = **42** (6 bloques, igual que el ES) · 02 = 26 + 18 + 13 =
  57 · 03 = 16 + 18 + 14 + 6 = 54 · 04 = 14 + 13 + 11 + 12 = 50 · 05 = 18 + 13 + 13 = 44 · 06 = 26 + 11 + 13 + 9 + 17 + 14 =
  90 · 08 = 20 + 19 = 39 · 09 = 11 + 12 = 23 · B01 = 14. El censo ES dice **429** porque suma también las 16 filas del
  calendario (el volcado tiene 17 fechas): no son tareas y la landing no las cuenta como tales. El volcado ES da los mismos
  413 con el mismo método.
- Otras cifras de la landing: 13 plantillas + 2 bonus + guía = **16 ficheros**; **17 fechas** en el B02; **32 productos en
  5 categorías** con filas libres en el plan del 10; objetivo de merma editable al **5 %** y pauta del kit 3–8 %; **43
  productos de partida** en la matriz del 12 (el ES decía «más de 30») y 4 filas libres; registro de temperaturas con 2
  tomas al día y 6 equipos (cámara 32–41 °F, cámara de masas 36–41 °F, congelador 0 °F, 2 vitrinas 32–41 °F, abatidor
  135 → 70 °F en 2 h y 41 °F en 4 h más); recepción: TCS > 41 °F, huevos con aire > 45 °F, leche y nata > 45 °F (solo
  donde la ley láctea lo permite), congelado con señales de descongelación; obrador desde las 5:00 AM, vitrinas a las
  6:45 AM, tienda de 8:00 AM a 8:00 PM (puerta a las 7:50 PM); food cost 28–35 % y merma < 5 % en el mensual del manager;
  depósito 30–50 % como práctica habitual, no ley; masa a 72–75 °F, fermentación ≤ 82 °F, horno 375–400 °F, base en
  blanco a 350 °F; date marking 7 días con 24 h como objetivo del kit en lo que lleva huevo; > 2 h por encima de 41 °F o
  tiempo desconocido → a la basura (regla del kit). El contador del 01-07 cuenta los ✓ sobre todas las tareas (no
  descuenta N/A, a diferencia del molde ligero del chocolate y el icecream): la landing no promete que salte N/A.
- **Fuera lo que el ES afirma y el kit no trae:** «Trail cobra €60-75 al mes» y «sin internet» (→ fórmula de los
  hermanos, Trail sin cifra), «merma en euros» (→ «in your currency»), «14 UE» (→ 9 de EE. UU. + sulfitos + los 14 del
  Reino Unido), «Imprimible A4» (→ US Letter), la FAQ «¿Qué incluye la versión 2.0?» (primera edición inglesa → FAQ de los
  registros: cake order form, allergen chart, temperature/receiving log, plan y mermas), las fechas españolas (→ Holiday
  Season con Three Kings Day y King cake, Easter con hot cross buns, Celebration Cakes, Thanksgiving pies, D14) y el
  precio «valorado en €31».
- **Testimonios: los 10 tal cual, ninguna frase cambiada.** Las marcas reales que señalaba la SPEC §R (Hotel Meliá
  Valencia, Grupo Europastry, Escuela Hofmann) están **solo** en el marquee de la SPA (`src/data/testimonials-pasteleria.ts`,
  que la tienda EN no usa); la ficha ES de Astro ya los trae neutralizados («hotel boutique en Valencia», «obrador
  industrial en Barcelona», «escuela de pastelería en Barcelona») y así se traducen. Isabel García cita «Reyes»: el B02 EN
  trae Three Kings Day. Roles traducidos; negocios conservados («Pastelería La Miga de Oro», «Obrador Sant Jordi»…).
- **Imágenes (todas miradas):** fuera `tareas-pasteleria-horno` (marca **MIWE** en el horno), `tareas-pasteleria-vitrina`
  (cartel «PATISSERIE ATELIER» con «RAZPBERRY ENTREMET» mal escrito), `tareas-pasteleria-equipo` (logos inventados en las
  chaquetillas y un saco de harina con texto) y la OG ES (texto español y «€12»). Se quedan `tareas-pasteleria-hero`
  (hero, OG, cta, bonus 1, hub y correo), `-masas` (why), `-decoracion` y `-produccion` (placa «ELIZA»). Entran
  `guia-pasteleria-1` (vitrina con etiquetas en blanco; bonus 2) y `guia-pasteleria-hero` (obrador con laminadora;
  buyBox y 6.ª del strip), ya publicadas en How to Open a Pastry Shop, y `csbp-en-pastry-case` (vitrina de bollería del
  Coffee Shop Business Plan Kit). Descartadas también `use-case-pasteleria-display` y `-team` (español, €, «MADRID»)
  y `-cakes` (delantal con texto). **No hace falta generar ninguna.** Para John, menor: en `-masas` y `-decoracion` se
  ven un reloj y una alianza mientras se trabaja la masa y se manga la tarta, y el kit pide «sin joyas ni reloj»; el ES
  LIVE usa las mismas fotos. Si se quiere afinar, una foto nueva de decoración sin joyas con la skill de imágenes.
- **Cruces del dashboard:** Chocolate Shop Checklists (el hermano de postre más cercano: muchas pastelerías hacen
  bombones), How to Open a Pastry Shop (la guía EN de la misma familia) y Food Cost Kit Pro (el ES cruza a Escandallos).
  El ES cruza además a Kit Tareas Restaurante y Cafetería: en EN, Coffee Shop, Ice Cream Shop y Restaurant quedan en el pie.
- **Pie:** How to Open a Pastry Shop, los 9 hermanos de checklists, los 5 kits EN, el eBook y el caso de uso EN
  (`/en/use-cases/concept/bakery-pastry-shop`). Y la guía enlaza de vuelta a este kit desde su pie.
- **FAQ:** 20 on-page (apertura, cierre, cake order form, allergen chart, temperature/receiving log, temperaturas,
  producción, plan y mermas, festivos y menores, limpieza, plantilla gratis, ya rellenas, tamaños, firma, Trail, varias
  tiendas, UK/CA/AU con FIR 2014, moneda, suscripción, garantía) y 6 en el JSON-LD (las de mayor demanda: opening
  checklist, cake order form, allergen chart, food temperature log, UK/CA/AU, garantía).

## 4. Pendiente

1. **John:** Payment Link USD $19 con redirección a
   `/en/digital-products/pastry-shop-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` y env
   `VITE_STRIPE_PAYMENT_LINK_PASTRY_SHOP_CHECKLISTS_KIT` (scope builds); luego `sync-payment-links.py`.
2. `vivo: true` en la rama: fusionar con el link **y** con los 15 xlsx de la F2 en `dl/` (o `vivo: false`).
3. **Ronda de la pastelería (F2):** confirmar las cifras del §3 contra el volcado final y repasar la ficha si cambian
   textos que la landing cita (contadores, 43 productos, 32 productos, horas 5:00 / 6:45 / 8:00 AM, 30–50 %, 28–35 %,
   < 5 %, rechazo en recepción, menores). Si la ronda decide que el contador descuente N/A, se puede añadir a la FAQ de
   firma.
4. **Fuera de mi carril:** `postprocess-transversal.py` `EXCLUIDOS` sin `pastry-shop-checklist-templates` (ver las notas
   del chocolate, §4.3).
5. Preview: `tienda-gate --es-identico --esperadas /kit-tareas-pasteleria` y el resto de gates de red; LIVE: acceso por
   admin + `gate-flujo-postpago --only pastry-shop-checklist-templates`; sitemap en GSC; correo a la cola EN.

## 5. Blog EN (para la sesión Cursor)

Posts EN que encajan para banner + párrafo hacia esta landing (menciones de pastry / bakery / croissant):
- `prompt-library-pastry-consulting` (225) y `prompt-library-creative-pastry` (125): los mejores; hoy llevan How to Open a
  Pastry Shop ×2 y Food Cost (más Financial Plan / HACCP).
- `prompt-library-bakery-consulting` (142): hoy lleva **dos banners del Coffee Shop Checklists**; víctima sugerida: uno de
  ellos → Pastry Shop Checklists (encaja mejor con una panadería-pastelería).
- `prompt-library-creative-bakery` (122).
- Por intención de búsqueda: `prompt-library-allergen-identification` (allergen chart) y
  `haccp-plan-template-restaurant-guide` (food temperature log / receiving log).
