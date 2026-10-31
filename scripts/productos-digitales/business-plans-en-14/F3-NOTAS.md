# Sushi Restaurant Business Plan Kit (EN, $39) — F3 (producto y lanzamiento) · notas
> Sesión Claude Code, 31-oct-2026 (F3, decisiones delegadas). Rama `feat/sushi-restaurant-business-plan-en` (apilada sobre la ES
> `feat/plan-negocio-sushi`, PR #190). Mac en ligero: sin build, npm, Playwright ni navegador.

## 1. Qué se hizo (réplica de la F3 del Rotisserie, `26e618f8`)
- Ficha `astro-site/src/data/productos-en/planes/sushi-restaurant-business-plan.ts` (25 FAQ = FAQPage) + wrappers
  `/en/digital-products/sushi-restaurant-business-plan{,/access,/library}.astro`, isla y `src/pages/SushiRestaurantBusinessPlanDashboard.tsx`
  (claves = ES `plan-negocio`, `plan-financiero`, `checklist-apertura`, `calculadora-sushi` + `equivalents-guide` común).
- Registro: `tienda.ts` (`plan-negocio-sushi-bar` → `en: vivo: true`), `zona-app.ts`, `verify-purchase`, `resend-access`,
  `get-download-urls`, `admin-generate-access`, `AdminGenerateAccess.tsx`, `product-prices.ts` (sync), `productos-changelog.ts` (2.2),
  `productos-digitales-config.ts`, `products-catalog.ts` (`urlByLang`/`priceByLang`), linkify ×2, `sitemap-lastmod.json`, `llms*.txt` 34 → 35.
- Hub EN: la tarjeta EN SUSTITUYE en el puesto 1 a la provisional «Business Plan: Sushi Bar» de la F3 ES; Mega Pack sigue el último.
- Enlaces cruzados: footers de Restaurant, Taco Shop, Pizza Shop y Rotisserie → sushi; el sushi enlaza a 13 hermanos. No hay
  checklists de sushi EN (los checklists EN no enlazan planes salvo su gemelo).
- Correo EN `emails/broadcast-sushi-restaurant-business-plan-lanzamiento-en.{html,subject.txt}`: «Hi everyone,», #111 + #FFD700,
  $39, imágenes `plan-sushi-bar-hero.jpg` y `-barra.jpg`, **SIN PROGRAMAR**.
- Imágenes: las 7 `plan-sushi-bar-*.jpg` del ES (sin texto), mismos huecos que la landing ES; ninguna generada. Sin testimonios (como el Rotisserie).
- Cripto: la plantilla monta las 3 puertas + nota de devoluciones con `cryptoEnabledFor(slug)` (`CRYPTO_PRODUCTS=all`); precio en `product-prices.ts`.
- `#comprar` sin link; entrada EN en `PAYMENT_LINKS_PENDIENTES_JOHN.md` (descripción de 244 car., contada con python).
- De paso (bug de main): la entrada del Rotisserie en `productos-digitales-config.ts` estaba ANIDADA dentro del objeto del Taco Shop
  (un `lang`/`}` mal colocado en #184); ahora es de primer nivel. Solo lo leen 4 dashboards de guías y `paginas-gate.py`.

## 2. Contraste landing ↔ entregables
Volcado de los 4 ficheros (`python-docx`/`openpyxl`, caché) en el scratch y `contraste.py`: toda cifra de la ficha con eco literal en
docx/xlsx/`cifras_caso.json`/`cifras_calculadora.md` (solo quedan «10 sections», «9 sheets» —el Word dice «ten-section», «nine-sheet»—,
el $39 y el «$20,000» de la pregunta del PAA). Recortes propios frente al molde del Rotisserie: sin «lb with kg» (el plan no da kg),
sin nota de Australia (el Word solo trae la UK), sin «flags any pay below the minimum wage» (la hoja da el suelo, no avisa), sin
detalle de tiers de DoorDash/Uber/Grubhub (el plan solo da 15-30 % y «Grubhub has its own tiers»), sin ventless, «Operations
Plan» sin take-out (eso va en Marketing). M1 y M2 de la REVISION-FINAL repetidos (FAQ del marketplace y de la congelación).

## 3. Gates (Mac, ligeros)
esbuild de los 20 .ts/.tsx tocados + frontmatter de los 4 .astro: OK · `sitemap-lastmod.json` JSON válido · `sync-product-prices.py
--check`: VERDE (94) · `tienda-gate.py` (estático): VERDE (36 vivos fuera de ES) · `hub-gate.py`: PASS · `nombre-gate.py --only`: ✅
(4 enlaces cruzados) · `gate-flujo-postpago.py --offline`: 5 ficheros = 5 tarjetas; único ✗ = «sin Payment Link» (este y el ES, esperado)
· no latinos en ficha, dashboard y correo: 0. **Pendiente con preview** (no hay PR de la rama EN): `tienda-gate.py --es-identico --base
… --esperadas /plan-negocio-sushi-bar` (el ES solo cambia en el hreflang), `gate-flujo-postpago.py --base … --crypto-products all
--crypto-exclude pro-prompts-ebook`, JSON-LD en el `dist`.

## 4. Revisión adversarial (Opus, una pasada) · 0 B · 1 M · 13 m, todo arreglado en fuente
Cifras del caso y de la calculadora, M1/M2, reglas duras (sin «sushi-grade», pH legal, licencia, «gluten-free», anclas ni cifras
movibles), 80 tareas, hojas y enlaces: correctos. Arreglado: **M** unidades (el Word solo da °C/sq m en la superficie y la congelación;
la calculadora también usa fl oz) · m: hood cleaning va dentro de Maintenance · el Costing admite precios con impuesto · en el Costing
tecleas precios de carta además de ingredientes · «raw-fish permit» no existe (health permit + reglas) · 51 nigiri por lb de arroz
CRUDO (ficha, hub, dashboard) · atún = las especies que lista el Code · histamina «si se calientan» · el hueco 24 % → 32 % no es la
merma que la calculadora ya cuenta · coma · calco «filter for the space» · correo «12-month cash flow» · llms: registros = 3-402.12 ·
«every piece» → «each piece» / «14 products». Meta description a 154 car.
**Deuda en el entregable (no se toca en F3)**: el desplegable `Fish Yield!B18` de la calculadora trae por defecto «I freeze in-house»
y el procedimiento del plan (¶104) es comprar el pescado ya tratado; no mueve ninguna cifra → próxima tanda de arreglos (VPS +
gates), cambiar el defecto a «Arrives frozen with a supplier letter».
