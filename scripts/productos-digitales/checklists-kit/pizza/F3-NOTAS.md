# Pizza Shop Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 18-oct-2026. Implementador único de F3 en la rama `feat/pizza-shop-checklists-en` (worktree,
> apilada sobre catering → cafetería → bar). Molde: la F3 del Catering (`../catering/F3-NOTAS.md`, commit `0e76f679`)
> replicada punto por punto. Contrato: `SPEC.md` (delta) + la SPEC base. Sin build, sin Playwright, sin navegador
> (regla térmica): verificación = lectura + scripts ligeros (CPU 47-49 °C toda la sesión).

## 1. Puntos de registro (los 25 del catering, para `pizza-shop-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla con `lang` | `KitTareasLandingPage.astro` | sin cambios |
| 2 | Ficha EN (réplica de TODAS las secciones de `kit-tareas-pizzeria.ts`) | `astro-site/src/data/productos-en/tareas/pizza-shop-checklist-templates.ts` | ✅ |
| 3 | Landing `/en/digital-products/pizza-shop-checklist-templates` | `…/pizza-shop-checklist-templates.astro` | ✅ `omitGlobalApp`, `miselup={false}`, `whatsapp={false}`, env `VITE_STRIPE_PAYMENT_LINK_PIZZA_SHOP_CHECKLISTS_KIT` → `#comprar` sin link |
| 4 | Gate `/access` (ProductAccessGate `lang="en"`) | `…/pizza-shop-checklist-templates/access.astro` | ✅ |
| 5 | Dashboard `/library` + island | `…/library.astro`, `islands/library/PizzaShopChecklistsKitLibraryIsland.tsx`, `src/pages/PizzaShopChecklistsKitDashboard.tsx` | ✅ 12 tarjetas (11 xlsx + Equivalents Guide); claves del ES (02 = `horno`); cruza a Restaurant, Coffee Shop Checklists y Food Cost Kit Pro (el ES: Kit Tareas, Kit Tareas Cafetería, Escandallos) |
| 6 | Gemelo ES con hreflang recíproco | `astro-site/src/pages/kit-tareas-pizzeria.astro` → `alternatesFamilia('kit-tareas-pizzeria')` | ✅ (cambia solo el `<head>`) |
| 7 | Familia `kit-tareas-pizzeria` → `en: pizza-shop-checklist-templates, vivo: true` | `astro-site/src/lib/tienda.ts` | ✅ (fusionar con el link) |
| 8 | Zona app con `lang: 'en'` | `astro-site/src/lib/zona-app.ts` | ✅ |
| 9 | Backend: PRODUCTS con `lang: 'en'` | `verify-purchase.ts`, `resend-access.ts` | ✅ |
| 10 | Descargas: claves de `kit-tareas-pizzeria` → 11 xlsx EN + `equivalents-guide` | `get-download-urls.ts` | ✅ nombres de `SPEC.md` §2 (= los de `dl/` de la F2) |
| 11 | Precio `{ usd: 19 }` | `product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (71 productos, 20 priceByLang) |
| 12 | Payment Link | `payment-links.ts` vía `sync-payment-links.py` | ⏳ John (§4) |
| 13 | Admin de accesos | `admin-generate-access.ts`, `AdminGenerateAccess.tsx` | ✅ |
| 14 | Config SPA y changelog EN | `productos-digitales-config.ts`, `productos-changelog.ts` | ✅ v2.0 «First English edition» |
| 15 | Catálogo `kit-tareas-pizzeria`: `name.en`, `description.en`, `urlByLang.en`, `priceByLang.en` | `src/data/products-catalog.ts` | ✅ |
| 16 | Alias de enlace | `linkify-use-case.ts` (astro) y `.tsx` (SPA) | ✅ |
| 17 | Hub EN: «Recurring Tasks: Pizzeria» sube a la 1 con copy EN | `DigitalProductsHubPage.astro` | ✅ (decía «330 tasks + inventory», «assembly line»; imagen = la misma, sin texto ES) |
| 18 | `footerLinks`: 5 kits + Restaurant, Bar, Coffee Shop y Catering Checklists | `kits/*-templates.ts` ×5, `tareas/{restaurant,bar,coffee-shop,catering}-checklist-templates.ts` | ✅ +1 línea cada uno |
| 19 | GEO: `llms.txt` y `llms-full.txt` («currently 20 products») | `astro-site/public/` | ✅ + fila «Daily operating checklists» |
| 20 | Sitemap: lastmod de la landing | `sitemap-lastmod.json` | ✅ |
| 21 | Blog EN: 2 banners sustituidos + párrafo contextual | `fase8x-config/kit-tareas-pizzeria-en.json` + `--aplicar` + `fase8b-regen-lastmod.py` | ✅ reversibilidad OK ×2; `fase8c-libreria-en-gate --todos` 0 errores |
| 22 | Temas para futuros rebalanceos | `fase8e-banners-en-reapuntar.py` (`TEMAS`) | ✅ |
| 23 | `tienda-gate.py`: testimonios exentos + `/kit-tareas-pizzeria` en `--esperadas` (comentario) | `tienda-gate.py` | ✅ estático verde (20 vivos fuera de ES) |
| 24 | Correo de lanzamiento EN | `emails/broadcast-pizza-shop-checklists-lanzamiento-en.{html,subject.txt}` | ✅ sin programar |
| 25 | Tres puertas cripto + nota de devoluciones | vienen con la plantilla | ✅ |

Blog EN: `prompt-library-pizza-consulting` (218 menciones; víctima Staff Scheduling Kit; párrafo antes de «Tips for
getting more out of Pizza Consultant Pro», ancla 10) y `robotic-restaurants-robot-chefs-servers` (15, su sección
«Pazzi»; víctima Inventory Kit; párrafo al final de «Robot Chefs», antes de «Robot Servers and Delivery», ancla 3).
No hay posts EN de restaurante italiano; los de delivery no nombran la pizza y el de cloud kitchens ya lleva el Catering.

## 2. Las 20 landings ES siguen byte a byte iguales

Comparador sin build (`es-identico-local/comparar.mjs`, `ASTRO_NM` = `johnguerrero-es-astro/node_modules`,
`--ref main`): **ES idénticas 40 · distintas 0**. Render EN (245.856 bytes): `revisar_texto` de `tienda-gate` sin
fallos en las 5 fichas EN, 0 `aggregateRating`, `priceCurrency` USD, H1 = title SEO; «€» y «Google Sheets» solo en las
constantes de la plantilla (las mismas 9 / 8 apariciones que el catering). Hermanos: +1 línea cada uno (su pie).
Sintaxis de los TS/TSX y del frontmatter de los .astro tocados: esbuild sin errores.

## 3. Decisiones de contenido

- Traducción propia desde el ES (regla 1bis, sin bridge); cifras comprobadas contra los 11 xlsx EN de la F2
  (`b4e89b17`, llegaron a mitad de la F3): **373 tareas** (30+14+18+14 = 76 en el 01; 31 en el 08 con responsable y
  hora), 5 filas verdes libres en cada checklist, inventario diario de 32 productos con Par y «⚠️ REORDER», 22 fechas +
  5 huecos y nota UK; 750–840 / 570 °F, 60–90 s / 3–5 min, precalentado «per manufacturer (45–60 min)», make line y
  masa en frío ≤ 41 °F, bolsa caliente ≥ 135 °F y fría aparte, < 30 min, ceniza en frío a metálico con tapa, NFPA 96
  mensual con combustible sólido, food cost 28–32 %, rollos de monedas y propinas de tarjeta fuera de ventas.
- **Lo que el ES afirma y el kit no trae, fuera:** «Trail €60-75/mes» y «sin internet», «fermentación lenta 24-72 h»,
  «temperatura de masa madre», «banco de masas», «etiquetado» del delivery, «amasadora y cámara de fermentación», el
  «foco por día» del semanal (todo va el lunes), «DDD / BIE / Verifactu»; en el dashboard ES, «6 checklists» del 01
  (son 4) y «17 fechas» (son 22). «Precio especial de lanzamiento / -69 %» → fórmula de la tienda EN.
- FAQ obligatoria UK/CA/AU (8 °C / 63 °C, 14 alérgenos ya anotados en las tareas, hoja de caja sin contraseña, nota UK
  del calendario, edad del alcohol como el catering). La intención «restaurant opening / closing checklist» va en las
  keywords y en las dos primeras FAQ («The same as a restaurant opening checklist…»), no en los xlsx.
- Testimonios: los 10 traducidos tal cual con el subtítulo de la edición española; UNA frase cambiada (Carmen Ruiz:
  «etiquetado para repartidores» → «every order checked against the ticket», que el kit sí trae).
- **Imágenes:** fuera `tareas-pizzeria-delivery.jpg` («A DOMICILIO», «HORNO DE LEÑA», Glovo, bandera) y la OG ES →
  OG = `tareas-pizzeria-hero.jpg`; entran `use-case-pizzeria-toppings.jpg` y `use-case-pizzero-team.jpg` (casos de uso
  EN, sin texto). `-equipo.jpg` se queda (pizarra en inglés con precios en £). Falta una OG EN propia si John la quiere.

## 4. Pendiente para el cierre

1. **John:** Payment Link USD $19 con redirección a
   `/en/digital-products/pizza-shop-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` y env
   `VITE_STRIPE_PAYMENT_LINK_PIZZA_SHOP_CHECKLISTS_KIT` en Netlify (scope builds); luego `sync-payment-links.py`.
   Hoy `gate-flujo-postpago --offline --only pizza-shop-checklist-templates`: 12 entregables, **1 fallo esperado**
   («SIN Payment Link», que lista también bar, cafetería y catering por la rama apilada).
2. `vivo: true` ya está en la rama: fusionar SOLO con el link creado (o `vivo: false` si hubiera que fusionar antes).
3. Preview: `tienda-gate --base` y `--es-identico --esperadas /kit-tareas-pizzeria` (+ `/kit-tareas-bar`,
   `/kit-tareas-cafeteria`, `/kit-tareas-catering` si van en el mismo PR), `whatsapp-gate`, `robots-gate`; render
   visual de landing, hub y dashboard.
4. LIVE: acceso por admin + `gate-flujo-postpago.py --only pizza-shop-checklist-templates`; sitemap en GSC; correo a la
   cola de 5 días (`CALENDARIO-V2-SEMANAL.md`, siguiente hueco EN) y programarlo con su routine.
5. Testimonio de Roberto Sánchez: su negocio de origen es «PizzaExpress», nombre de una cadena real del Reino Unido.
   Traducido tal cual por la regla; decidir si se cambia el nombre del negocio en la EN.
6. Test real en Google Sheets (común a la línea) → pastilla, `compatSubtitle`, FAQ y aviso del dashboard.
