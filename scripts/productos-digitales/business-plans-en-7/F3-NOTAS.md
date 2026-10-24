# Paella Catering Business Plan Kit (EN, $39) — F3-NOTAS (24-oct-2026 · sesión Claude Code)

> F3 = producto y lanzamiento (SPEC-delta §8, D130), duplicado del BBQ Catering Business Plan Kit (F3 en `527c35eb` +
> `35e7389b` + `7adc0353`). Rama `feat/paella-catering-business-plan-en-f3` (sale de `a967cb4a`); la F2 va después en
> `feat/paella-catering-business-plan-en`. Sin builds ni navegador (Mac, regla térmica; CPU 45-49 °C): verificado con
> esbuild, grep, node y gates estáticos. Sin subagentes.

## 1. Puntos y estado

| Punto | Estado | Dónde |
|---|---|---|
| Ficha EN (PlanNegocioLandingPage, carrusel y 3 puertas cripto heredados, $39 sin anclas, sin rating) | ✅ | `astro-site/src/data/productos-en/planes/paella-catering-business-plan.ts` |
| Landing + `/access` + `/library`, island y dashboard (claves = ES y BBQ + `equivalents-guide`) | ✅ | `pages/en/digital-products/paella-catering-business-plan{.astro,/access.astro,/library.astro}` · `islands/library/PaellaCateringBusinessPlanLibraryIsland.tsx` · `src/pages/PaellaCateringBusinessPlanDashboard.tsx` |
| `tienda.ts` FAMILIAS (`vivo: true`) · `zona-app.ts` · linkify (Astro y SPA) · `sitemap-lastmod.json` | ✅ | — |
| `get-download-urls` (4 + guía de equivalencias) · `verify-purchase` · `resend-access` · `admin-generate-access` (+ SPA) | ✅ | los 4 ficheros de `dl/` los trae la F2 |
| SPA: `productos-digitales-config.ts`, changelog 2.2 «First English edition», catálogo (`name.en`, `urlByLang`, `priceByLang`) | ✅ | — |
| `product-prices.ts` ($39) con `sync-product-prices.py` | ✅ `--check` verde (78 productos, 27 EN) | — |
| `payment-links.ts` | ⏳ John crea el Payment Link → env `VITE_STRIPE_PAYMENT_LINK_PAELLA_CATERING_BUSINESS_PLAN` → `sync-payment-links.py` | — |
| Hub EN: tarjeta viva en la 1 (el BBQ pasa a la 2 y el resto baja); fuera la vieja «Business Plan: Paella Catering for Events» (kit español: 11 entregables, 88 proveedores, DO, Garcima/Vaello) | ✅ | `DigitalProductsHubPage.astro` |
| `footerLinks` hacia la paella: 8 planes EN (incl. BBQ) + Food Cost + HACCP + Catering Checklists | ✅ | — |
| FAQ cruzada «Is there a plan for a paella caterer?» en Catering, Food Truck y BBQ EN (entra también en su FAQPage) | ✅ | — |
| hreflang recíproco en `/plan-negocio-paellero-eventos` (solo el `<head>`; código idéntico al del parrillero) | ✅ | — |
| `llms.txt` / `llms-full.txt` (26 → 27 productos EN + entrada) | ✅ | — |
| `tienda-gate.py`: EXENTOS (`Joan Beltrán`, `Laura Martín`, `Castellón`) y comentario de `--esperadas` | ✅ | — |
| OG `og-paella-catering-business-plan.jpg` | ⚠️ provisional (recorte 1200×630 de `plan-paellero-eventos-hero`) | §4 |
| 3 imágenes nuevas | ❌ las genera el orquestador **antes del merge** | §4 |
| Correo EN de lanzamiento (`.html` + `.subject.txt`), sin programar | ✅ | `emails/broadcast-paella-catering-business-plan-lanzamiento-en.*` |
| `CALENDARIO-V2-SEMANAL.md` (hueco 3-feb 14:00Z, borrador + routine el 4-ene) | ⏳ orquestador | — |
| Altas de la F2 en `censo-entregables.py` (`PRODUCTOS_LETTER`) y `postprocess-transversal.py` (`EXCLUIDOS`) | ⏳ F2 (D127, antes de G9; el BBQ las hizo en su F2, `66253c22`) | — |

## 2. Decisiones de contenido

- **SEO (D114b, research §9):** title `Paella Catering Business Plan Kit: Word Template + Excel Financial Projections + Pricing
  Calculator | AI Chef Pro` (113 car.; nombre del producto primero, patrón BBQ, en vez del «…Business Plan Template: …» de
  research) · H1 Forma B `Paella Catering ` + oro `Business Plan` + «Template to Start a Live Paella & Spanish Catering
  Company: Word Plan + Excel Financial Projections + Pricing Calculator + Startup Checklist» · meta de research tal cual (145
  car.) «Paella catering business plan template for a live-cooking Spanish caterer: Word plan, 3-year Excel projections,
  pricing calculator and checklist.» · keywords de research + «paella caterer». Los 6 H2 de research no caben como H2
  (constantes de `UI_PLAN`, como en el BBQ): van en el subtítulo del grid («What's inside your Paella Catering Business Plan
  Kit»), tarjetas 2/4/5 («Is a paella catering business profitable?», «Paella for a crowd: pan sizes, rice per guest and staff
  for 50, 100 or 200 guests», «How much does it cost to start a paella catering business?»), razones 2/3 («Cooking Paella at
  Events: Commissary, Propane and Food Safety Rules», «Paella Catering Prices: What to Charge per Person») y FAQ.
- **FAQ (22):** las 9 de research §9 en la redacción del comprador + qué incluye, ¿genérico?, seguridad alimentaria de la
  paella en eventos (arroz TCS, *B. cereus*, 135 °F o TPHC 4 h, 165 / 145 / 155 °F, shellstock tags 90 días), equipo,
  seguros (GL sin exclusión de llama abierta), **«Should I buy this or the Catering Business Plan Kit?»** (canibalización con
  Catering y BBQ), lender, Excel, **UK/Canada/Australia** (moluscos, apio y sulfitos entre los 14 alérgenos UK; en EE. UU. los
  moluscos no son alérgeno mayor), moneda, suscripción, clientes, garantía. `schema.faqs` = el mismo array.
- **Legal sin inventar (research §6):** sin cocina de casa (3-201.11; el cottage food no cubre alimentos TCS), commissary con
  acuerdo escrito, cocinar en el evento → limited food preparation de San Diego County como ejemplo y «ask your county»,
  propano → estación al aire libre o bajo su toldo, cilindros fuera de las carpas, extintor, burn bans, «check with your fire
  marshal»: **los 20 ft de Virginia no salen en la landing** (un solo estado). Evento público = temporary food establishment.
  Sangría sin alcohol o con el vino del cliente, sin venderlo; el corkage fee no se modela. Nada de «DO» aplicado al plato.
- **Jerga y vocabulario:** paella chef / paella caterer / paella pan / 3-ring propane burner / live paella / backyard paella
  party / commissary / insulated food carriers / W-2; «fideua» y «Spanish chorizo» sin tildes. Barrido node de los 282 textos
  de la ficha: 0 restos de español (fuera EXENTOS), 0 no latinos, 0 vocabulario vetado (smoker, pitmaster, brisket, pulled
  pork, ribs, bark, smoke ring, live pit, plated, stations, refrigerated van, induction, pasta, bartender, cocktails,
  freelance, DO, Garcima, paellero/a, €…), «chef» solo como «paella chef» / «second paella chef». Los únicos avisos son
  falsos positivos: «food hygiene rating» (FHRS), «EUR» en la FAQ de moneda (igual que el BBQ), rutas de imagen `plan-paellero-*`
  y el href del Food Truck en el pie. «BBQ Catering Business Plan Kit» solo como producto hermano (FAQ de canibalización y pie).
- **Testimonios:** los 8 del ES traducidos con «…with the Spanish edition of this plan»; cambiada solo la frase que no es
  verdad en el EN: fiestas del pueblo y modelo de contrato B2B → la calculadora; manual técnico y 12 paellas → la tabla de
  pan sizing; contratos B2B → sección de marketing; 95.000 EUR y 88 proveedores DO → checklist; catálogo con SKU de Garcima
  (marca) → startup costs; anexo CCAA y contrato → legal section + permits checklist; 10 experiencias + 12 paellas y «40 %» →
  menu styles y 3 paquetes, sin cifra; contratos B2C/B2B → calculadora. «Don» fuera; «Levante» → «eastern Spain».
- **Imagen del hub:** `plan-paellero-eventos-hero` (paella en vivo en una boda al aire libre, sin texto).

## 3. Cifras «a confirmar con F2-NOTAS»

Todas viven en **un solo bloque `CASO`** al principio de la ficha (comentario `// a confirmar con F2-NOTAS` en cada línea);
la ficha las interpola en FAQ, razones y tarjetas. Hub, `llms*`, changelog, dashboard y correo **no** llevan cifras del caso.
Las cifras fijas que sí salen en texto (líneas de Startup Costs $2,500 / $1,800 / $900 / $18,000 / $3,000 / $3,000, lean
$12-20K, mercado $12-31 / $45 / $44-65, 36 in = 40, 32 = 30, 26 = 18, 3-3,5 oz, 1 paella chef por 3 paelleras) salen de la
SPEC D120/D123 y research §5: cotejarlas también.

| Clave `CASO` | Valor puesto (research §8 / SPEC D118-D120) | Fuente F2 esperada |
|---|---|---|
| `eventos` · `invitados` · `precio` | 135 · 58 · $40.00 | `B4` · `B6` · `B5` (D15 puede subir B4 de 5 en 5 hasta 150) |
| `ventas` | $313,200 | `ventas_a1` |
| `inversion` · `circulante` · `necesidad` | $49,480 · $37,920 · $87,400 | Startup Costs total, circulante, total cash needed |
| `propios` · `prestamo` · `dscr` | $25,000 · $62,400 · 3.1× | `B30` · `B31` calibrado (SBA 7(a)) · DSCR mínimo |
| `neto` · `netoPct` · `equilibrio` | $21,000 · 6.7% · 115 | neto año 1 (research con D&A $5,200; SPEC ≈ $5,700) · % · eventos de equilibrio |
| `marketing` · `seguros` | $8,000 · $5,500 | fijo de marketing · `B27` |
| `pesEventos` · `pesPrecio` · `pesInvitados` | 101 · $36.00 · 52 | Scenarios pesimista (y que la caja se agote de verdad en el año 1) |
| `ejDropoff` · `ejFiesta` · `ejBoda` | $22 · $34 · $52 | «3 Example Quotes» (30 / 45 / 110 invitados; precio por invitado de cada uno) |
| `arrozOz` · `menuStyles` · `formulas` | 3.25 · 8 · 700 | calculadora D123 · docx §2 (inv. §2) · fórmulas del libro |

**Frases a cotejar con los ficheros F2** (si alguna no es verdad, se cambia esa frase): calculadora con lb (kg), °F (°C) y
pulgadas (cm) (FAQ UK); nota UK del docx §9 (council 28 días antes, food hygiene rating, 14 alérgenos con moluscos, apio y
sulfitos, VAT 20 %, gas con council y recinto); 3 paquetes con los nombres de D123 e interruptor «Tapas hour?» con coste por
invitado; $/lb de ingredientes en blanco con fila de estado y coste Kit por estilo mientras falten; depósito 50 % («US caterers
ask 25-50 %») y tramos de cancelación; salidas: paelleras por tamaño, personas, arroz (lb), caldo (gal), propano y cilindros de
20 lb; «Paella Yield & Pan Sizing» de 18 a 40 in con invitados, arroz, caldo y aros, 8 estilos con oz por ingrediente, mínimo
del Food Code en su columna y alérgenos con «verify with your recipe and suppliers»; «Shopping List by Guest Count» con
40/80/150/300 (paelleras, quemadores, arroz, caldo, azafrán en g, limones, pan, ensalada, alioli, propano, platos y cubiertos,
hielo, equipo humano); Staffing con los 4 puestos de D121; checklist: contrato con 50 % de depósito, tramos y plan B de viento
y lluvia, plan HACCP con arroz TCS, fase 2 «Propane & Permits» con commissary agreement, condado, fire marshal, cilindros
verticales y sujetos en la van, approved source y shellstock tag log de 90 días; ServSafe Manager, Thumbtack, Google Business
Profile y launch tasting; `B5` «excl. sales tax; staffing and service charge included»; el docx dice que el pesimista agota la
caja y que 135 eventos = dueño a tiempo completo con segundo paella chef en fin de semana; depósito de clientes no modelado.

## 4. Imágenes

Del ES del paellero valen **-hero** (paella en vivo en una boda al aire libre: hero, buyBox, CTA, hub y OG provisional),
**-2** (paella de marisco en un evento de empresa en una azotea: galería, whyBg, bonus 1), **-4** (paelleras, quemador de 3
aros, arroz y azafrán: strip del grid, bonus 2) y **-6** (estilos de paella vistos desde arriba: galería y strip). Fuera **-1**
(cartel «PAELLA VALENCIANA D.O.»: texto y deuda DO), **-3** (restaurante: no es nuestro comprador) y **-5** (food truck
«ARROCERÍA MEDITERRÁNEA» con precios en €). Ninguna de las cuatro útiles enseña EE. UU. ni la carpa de trabajo, la mesa de
tapas o la van: faltan las tres de research §9.

**BLOQUEANTE antes del merge**: la ficha ya referencia estas 3 rutas (galería posiciones 2-4 y strip del grid); hay que
crearlas con `generate-images` en `astro-site/public/lovable-uploads/ai-gallery/` (JPG 1600 px, 200-450 KB). Ningún gate
comprueba que existan: `ls` de las tres antes de fusionar.

| Fichero | Alt (research §9) | Prompt (una línea) |
|---|---|---|
| `paella-catering-seafood-paella-wedding.jpg` | Paella chef stirring a 36-inch seafood paella over a propane burner at an outdoor wedding | Photorealistic golden-hour photo of a paella chef in a dark apron stirring a giant 36-inch seafood paella with shrimp, mussels and lemon wedges over a 3-ring propane paella burner on legs, at an outdoor vineyard wedding in California, string lights and guests at long tables softly blurred behind, no text, no logos, 16:9 |
| `paella-catering-backyard-party-tapas.jpg` | Backyard paella party with tapas | Photorealistic late-afternoon photo of a backyard paella party in an American suburban garden: a large chicken and chorizo paella in a wide pan on a serving table next to small plates of tapas (patatas bravas, Spanish tortilla, cheese and cured ham, olives, aioli and bread), guests holding plates softly blurred behind, no text, no logos, 16:9 |
| `paella-catering-van-pans-burners.jpg` | Paella pans and 3-ring burners loaded in a catering van | Photorealistic daylight photo of the open rear doors of a white cargo van at an event venue, shelving with stacked paella pans of several sizes, 3-ring propane paella burners with folding legs, upright 20-lb propane cylinders strapped in a rack, insulated food carriers and coolers, a caterer in a dark apron unloading, no text, no logos, no brand names, 16:9 |

La plantilla pinta la galería, el strip y los fondos con `alt=""` (decorativas, igual que en el BBQ): los alt de esta tabla
sirven para `generate-images` y para el correo. **OG**: `og-paella-catering-business-plan.jpg` (1200×630) es hoy un recorte del hero ES; rehacerlo desde
`paella-catering-seafood-paella-wedding.jpg` (como el BBQ en `35e7389b`) y, si se rehace, cambiar el alt del correo por el de
la primera fila (nota en la cabecera del `.html`).

## 5. Posts EN candidatos para banners (blog EN = otra sesión, Cursor; no tocados)

`/en/blog/ai-recipe-scaling-guide` (pone de ejemplo «scale this paella recipe to serve 75» ≈ Shopping List by Guest Count) ·
`/en/blog/fish-fumet` (base de la paella de marisco) · `/en/blog/prompt-library-catering` ·
`/en/blog/how-to-start-a-food-truck-business` (quien duda entre paella food truck y catering) ·
`/en/blog/restaurant-profit-margins-explained-benchmarks` (margen neto 7-8 % del catering) ·
`/en/blog/break-even-analysis-restaurants-ai`. No hay post EN de paella: hueco SEO para «how to start a paella catering
business» / «paella for a crowd» (research §2-§3: SERP sin ningún plan ni guía) cuando la sesión del blog lo coja.

## 6. Gates (24-oct, sin build)

- `tienda-gate.py` (estático): ✅ 27 productos vivos fuera de ES con data, páginas y zona-app.
- `sync-product-prices.py --check`: ✅ 78 productos (51 ES + 27 EN); catálogo coincide (27 `priceByLang`).
- `gate-flujo-postpago.py --offline --only paella-catering-business-plan`: 5 ficheros = 5 tarjetas; ❌ esperados: los 4
  ficheros de `dl/paella-catering-business-plan/` (F2) y el Payment Link (John; avisa también del BBQ y de los 3 checklists de
  postre, que lo esperan igual).
- `robots-gate.py`: ✅ (ninguna URL pública bloqueada, zona app bloqueada).
- esbuild: ✅ los 27 TS/TSX tocados o nuevos + los frontmatter de los 5 `.astro` (3 páginas paella, ES paellero, hub EN).
- `sitemap-lastmod.json`: JSON válido.
- Barrido node del texto de la ficha: §2 (0 fallos reales).
- **No ejecutados (necesitan preview o red contra la página nueva):** `tienda-gate.py --base` y `--es-identico --base
  <preview> --esperadas /plan-negocio-paellero-eventos` (la ES solo cambia en el `<head>`: el wrapper queda idéntico línea a
  línea en código al del parrillero y la plantilla no se toca), `carrusel-apps-gate.py --base`, `whatsapp-gate.py`,
  `gate-flujo-postpago.py` LIVE. `nombre-gate.py` no aplica (solo fichas ES).

## 7. Pendientes

1. Orquestador: confirmar el bloque `CASO` con `F2-NOTAS` / `cifras_caso.json` y cotejar las frases de §3.
2. Orquestador: generar las 3 imágenes de §4 y rehacer la OG.
3. F2: altas en `PRODUCTOS_LETTER` (`censo-entregables.py`) y `EXCLUIDOS` (`postprocess-transversal.py`) antes de G9.
4. John: Payment Link USD → env en Netlify → `sync-payment-links.py` → `gate-flujo-postpago.py --only
   paella-catering-business-plan` LIVE (sin compra de prueba: acceso por admin).
5. Tras el deploy: gates con `--base`, sitemap reenviado en GSC (`sc-domain:aichef.pro`), correo (borrador + routine el
   4-ene para el 3-feb 14:00Z; confirmar huecos con `GET /broadcasts`) y entrada en `CALENDARIO-V2-SEMANAL.md`.
6. Blog EN (Cursor): banners de §5 y hueco «how to start a paella catering business».
