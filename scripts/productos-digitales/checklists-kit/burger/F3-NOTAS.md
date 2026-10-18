# Burger Joint Checklists Kit Pro — F3 (producto y lanzamiento) · notas

> Sesión Claude Code, 18-oct-2026. Implementador único de F3 en la rama `feat/burger-joint-checklists-en` (worktree,
> apilada sobre pizza → catering → cafetería → bar). Molde: la F3 de la pizzería (`../pizza/F3-NOTAS.md`, commits
> `51c11cf2` y `855b5c3f`) replicada punto por punto. Contrato: `SPEC.md` (delta) + la SPEC base. Sin build, sin
> Playwright, sin navegador (regla térmica): verificación = lectura + scripts ligeros (CPU 47-51 °C toda la sesión).

## 1. Puntos de registro (los 25 de la pizzería, para `burger-joint-checklist-templates`)

| # | Punto | Fichero | Estado |
|---|---|---|---|
| 1 | Plantilla con `lang` | `KitTareasLandingPage.astro` | sin cambios |
| 2 | Ficha EN (réplica de TODAS las secciones de `kit-tareas-hamburgueseria.ts`) | `astro-site/src/data/productos-en/tareas/burger-joint-checklist-templates.ts` | ✅ |
| 3 | Landing `/en/digital-products/burger-joint-checklist-templates` | `…/burger-joint-checklist-templates.astro` | ✅ `omitGlobalApp`, `miselup={false}`, `whatsapp={false}`, env `VITE_STRIPE_PAYMENT_LINK_BURGER_JOINT_CHECKLISTS_KIT` → `#comprar` sin link |
| 4 | Gate `/access` (ProductAccessGate `lang="en"`) | `…/burger-joint-checklist-templates/access.astro` | ✅ |
| 5 | Dashboard `/library` + island | `…/library.astro`, `islands/library/BurgerJointChecklistsKitLibraryIsland.tsx`, `src/pages/BurgerJointChecklistsKitDashboard.tsx` | ✅ 12 tarjetas (11 xlsx + Equivalents Guide); claves del ES (02 = `plancha-grill`); cruza a Restaurant, Pizza Shop Checklists y Food Cost Kit Pro (el ES: Kit Tareas, Kit Tareas Pizzería, Escandallos) |
| 6 | Gemelo ES con hreflang recíproco | `astro-site/src/pages/kit-tareas-hamburgueseria.astro` → `alternatesFamilia('kit-tareas-hamburgueseria')` | ✅ (cambia solo el `<head>`) |
| 7 | Familia `kit-tareas-hamburgueseria` → `en: burger-joint-checklist-templates, vivo: true` | `astro-site/src/lib/tienda.ts` | ✅ (fusionar con el link) |
| 8 | Zona app con `lang: 'en'` | `astro-site/src/lib/zona-app.ts` | ✅ |
| 9 | Backend: PRODUCTS con `lang: 'en'` | `verify-purchase.ts`, `resend-access.ts` | ✅ |
| 10 | Descargas: claves de `kit-tareas-hamburgueseria` → 11 xlsx EN + `equivalents-guide` | `get-download-urls.ts` | ✅ nombres de `SPEC.md` §2 (= los de `dl/` de la F2) |
| 11 | Precio `{ usd: 19 }` | `product-prices.ts` vía `sync-product-prices.py` | ✅ `--check` verde (72 productos, 21 priceByLang) |
| 12 | Payment Link | `payment-links.ts` vía `sync-payment-links.py` | ⏳ John (§4) |
| 13 | Admin de accesos | `admin-generate-access.ts`, `AdminGenerateAccess.tsx` | ✅ |
| 14 | Config SPA y changelog EN | `productos-digitales-config.ts`, `productos-changelog.ts` | ✅ v2.0 «First English edition» |
| 15 | Catálogo `kit-tareas-hamburgueseria`: `name.en`, `description.en`, `urlByLang.en`, `priceByLang.en` | `src/data/products-catalog.ts` | ✅ |
| 16 | Alias de enlace | `linkify-use-case.ts` (astro) y `.tsx` (SPA) | ✅ |
| 17 | Hub EN: «Recurring Tasks: Burger Joint» sube a la 1 con copy EN | `DigitalProductsHubPage.astro` | ✅ (decía «302 pre-filled tasks», «assembly line», «polar compounds test»; imagen = la misma, sin texto ES) |
| 18 | `footerLinks`: 5 kits + Restaurant, Bar, Coffee Shop, Catering y Pizza Shop Checklists | `kits/*-templates.ts` ×5, `tareas/{restaurant,bar,coffee-shop,catering,pizza-shop}-checklist-templates.ts` | ✅ +1 línea cada uno |
| 19 | GEO: `llms.txt` y `llms-full.txt` («currently 21 products») | `astro-site/public/` | ✅ + fila «Daily operating checklists» |
| 20 | Sitemap: lastmod de la landing | `sitemap-lastmod.json` | ✅ |
| 21 | Blog EN: 2 banners sustituidos + párrafo contextual | `fase8x-config/kit-tareas-hamburgueseria-en.json` + `--aplicar` + `fase8b-regen-lastmod.py` | ✅ reversibilidad OK ×2; `fase8c-libreria-en-gate --todos` 0 errores |
| 22 | Temas para futuros rebalanceos | `fase8e-banners-en-reapuntar.py` (`TEMAS`) | ✅ |
| 23 | `tienda-gate.py`: testimonios exentos + `/kit-tareas-hamburgueseria` en `--esperadas` (comentario) | `tienda-gate.py` | ✅ estático verde (21 vivos fuera de ES) |
| 24 | Correo de lanzamiento EN | `emails/broadcast-burger-joint-checklists-lanzamiento-en.{html,subject.txt}` | ✅ sin programar |
| 25 | Tres puertas cripto + nota de devoluciones | vienen con la plantilla | ✅ |

Blog EN: `prompt-library-burger-restaurant` (162 menciones; víctima Financial Plan Kit; párrafo al cierre de la sección
del Kitchen Manager, antes de «Prompts for Burger Cook Specialist», ancla 6) y `restaurant-profit-margin-calculator`
(«Case Study 2: The Burger Joint», fast casual de 3 locales; víctima Staff Scheduling Kit; párrafo antes de «Before and
After», ancla 4). Descartados: Robotic Restaurants (ya lleva el Pizza Shop), Ghost Kitchens y Plant-Based Menus.

## 2. Las 20 landings ES siguen byte a byte iguales

Comparador sin build (`es-identico-local/comparar.mjs`, `ASTRO_NM` = `johnguerrero-es-astro/node_modules`,
`--ref main`): **ES idénticas 40 · distintas 0**. Render EN (247.532 bytes): `revisar_texto` de `tienda-gate` sin
fallos, 0 `aggregateRating` ni `review`, `priceCurrency` USD, H1 = title SEO, 6 `Question` en el FAQPage; «€» y
«Google Sheets» solo en las constantes de la plantilla (las mismas 9 / 8 apariciones que los 5 hermanos). Hermanos: +1
línea cada uno (su pie). Sintaxis de los 31 TS/TSX y frontmatter .astro tocados: esbuild sin errores.

## 3. Decisiones de contenido

- Traducción propia desde el ES (regla 1bis, sin bridge); cifras comprobadas contra los 11 xlsx EN de la F2 (llegaron a
  mitad de la F3; volcado propio de tareas): **346 tareas** (30+14+18+10 = 72 en el 01; 31 en el 08 con responsable y
  hora), 5 filas verdes libres, inventario diario de 28 productos con Par y «⚠️ REORDER», 22 fechas + 5 huecos y nota
  UK; plancha 400–450 °F, aceite 350–355 °F, carne picada 155 °F / 17 s con sonda (menos hecha solo a petición con el
  aviso al consumidor, nunca el menú infantil), pollo 165 °F, bola de smash 3–3.5 oz prensada 30–45 s, campana 30 s,
  pan cara abajo, patatas 3–4 min y aros 2–3 min, test TPM, make line y toppings a 41 °F con date marking de 7 días,
  salsas 5 días, carne fresca 3 días, ticket times < 12 min, food cost 28–32 %, NFPA 96 trimestral / semestral, aceite
  usado a un recycler, propinas de tarjeta fuera de ventas y rollos de monedas.
- **Lo que el ES afirma y el kit no trae, fuera:** «Trail €60-75/mes» y «sin internet», «gestión de riders» (no hay
  repartidor propio: la FAQ lo dice), «etiquetado» del delivery, «control de tiempos por grosor», la guía «rare a well
  done» (→ 155 °F con sonda), la «presión» del smash, el «foco por día» del semanal (todo va el lunes), «noche de burger
  especial», «festivos con menú limitado», «DDD / BIE / Verifactu»; en el dashboard ES, «6 checklists» del 01 (son 4)
  y «17 fechas» (son 22). «Precio especial de lanzamiento / -69 %» → fórmula de la tienda EN.
- FAQ obligatoria UK/CA/AU (8 °C / 63 °C, 14 alérgenos con la mostaza, que no está en los 9 de EE. UU.; hoja de caja
  sin contraseña, nota UK del calendario, edad del alcohol). La intención «restaurant opening / closing checklist» va
  en las keywords y en las dos primeras FAQ.
- Testimonios: 9 de 10 traducidos tal cual con el subtítulo de la edición española. **Retirado SOLO en EN: Patricia
  Vega, «Grupo Burger Factory»** (Burger Factory es una cadena real canadiense, ~40 locales y alguno en EE. UU.; mismo
  criterio que PizzaExpress). Se quedan «The Burger Lab» (homónimos sueltos) y «BurgerExpress» (cadena británica de los
  80, cerrada en 1993). Dos frases cambiadas: Sergio Ramos (la guía por grosor «rare… well done» → cada patty
  comprobado con sonda) y Diego Castillo («etiquetado» → el palillo con bandera en las burgers altas).
- **Imágenes:** las 7 del ES no llevan texto en español (bolsas «FLAME & GRIND», pizarra «SIZZLE SHACK» con $) y se
  quedan; fuera solo la OG ES (`og-kit-tareas-hamburgueseria`: «Kit de Tareas», «€12», «Google Sheets», «A4») → OG =
  `tareas-burger-hero.jpg`. Falta una OG EN propia si John la quiere.

## 4. Pendiente para el cierre

1. **John:** Payment Link USD $19 con redirección a
   `/en/digital-products/burger-joint-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` y env
   `VITE_STRIPE_PAYMENT_LINK_BURGER_JOINT_CHECKLISTS_KIT` en Netlify (scope builds); luego `sync-payment-links.py`.
   Hoy `gate-flujo-postpago --offline --only burger-joint-checklist-templates`: 12 entregables, fallos esperados «SIN
   Payment Link» (lista también bar, cafetería, catering y pizzería por la rama apilada) y los 11 xlsx «NO trackeado en
   git» hasta el commit.
2. `vivo: true` ya está en la rama: fusionar SOLO con el link creado (o `vivo: false` si hubiera que fusionar antes).
3. Preview: `tienda-gate --base` y `--es-identico --esperadas /kit-tareas-hamburgueseria` (+ los hermanos que vayan en
   el mismo PR), `whatsapp-gate`, `robots-gate`; render visual de landing, hub y dashboard.
4. LIVE: acceso por admin + `gate-flujo-postpago.py --only burger-joint-checklist-templates`; sitemap en GSC; correo a
   la cola de 5 días (`CALENDARIO-V2-SEMANAL.md`, siguiente hueco EN) y programarlo con su routine.
5. Testimonio de «Sergio Ramos»: es también el nombre de un futbolista muy conocido; traducido tal cual por la regla.
   Decidir si se cambia el nombre en la EN.
6. Test real en Google Sheets (común a la línea) → pastilla, `compatSubtitle`, FAQ y aviso del dashboard.
