# Recipe Costing Kit Pro — SPEC (F1 · 24-sep-2026 · sesión Claude Code)

> Primer producto de la **Tienda internacional en inglés**. Es la versión inglesa del **Kit de Escandallos Pro**
> (`kit-escandallos`, 12 €, contenido v2.0). Doc canónico: `scripts/productos-digitales/TIENDA-INTERNACIONAL.md`.
>
> Base:
> - `F1-inventario-es.md`: qué entrega hoy el ES, con fichero:línea.
> - `F1-research-us-uk.md`: mercado, con la fuente de cada dato.
> - `F1-research-8-bloques-en.md`: los 8 bloques del método, en curso.
> - `SPEC-R1.json`: revisión adversarial ronda 1, 37 hallazgos, todos incorporados aquí (IDs T# y M# entre corchetes).
>
> Esta SPEC **decide**. Lo que no está aquí no se hace.
>
> Estado: research de 8 bloques hecho (`F1-research-8-bloques-en.md`) y **OK de John recibido el 24-sep** con dos
> decisiones que amplían el alcance: **dos plantillas nuevas en ES y EN a la vez** (D17) y **licencia de un negocio
> por compra** (D18). Próximo paso: revisión R2 de esta SPEC → F2.

## 0. Reglas que mandan

### 0.1 Duplicar y adaptar (John, 24-sep)

Otro idioma = **DUPLICAR lo español y traducirlo, adaptando las variables del mercado**. No se crean plantillas,
diseños, componentes ni páginas nuevas. **Las hojas de trabajo conservan sus hojas, columnas, filas y fórmulas.** Lo
que cambia es el contenido: textos, unidades, precios, impuesto, benchmarks y formatos.

Excepciones declaradas (dato de mercado, no diseño; el gate 1 las reconoce una a una):
- **E1.** La tabla auxiliar `Conversions` crece y se regenera (D7).
- **E2.** Los rangos de VLOOKUP y el área de impresión de `Conversions` se amplían (D7) [T3].
- **E3.** La fórmula de `Bottle Sizes` del 04 pasa de centilitros a mililitros (§2.5) [T2, M1].
- **E4.** El formato de fecha pasa a fecha corta del sistema (D13) [M17].

John, 24-sep: «los archivos se tienen que adaptar a inglés y a métricas de uso común en US/UK».

### 0.2 Producto INDEPENDIENTE del español (John, 24-sep)

John, 24-sep: «el producto en inglés tiene que ser independiente al español al igual que los otros idiomas, con su
propio dashboard, sus propios archivos… su propio producto en Stripe y var env en Netlify».

| Pieza | Recipe Costing Kit Pro (EN) | Kit de Escandallos Pro (ES) |
|---|---|---|
| productId | `recipe-costing-kit` | `kit-escandallos` |
| Landing | `/en/digital-products/recipe-costing-kit` | `/kit-escandallos` |
| Acceso y dashboard | `…/recipe-costing-kit/access` y `…/library`; `RecipeCostingKitDashboard.tsx`; JWT `recipe-costing-kit-jwt` | `/kit-escandallos-access` y `-library` |
| Ficheros | `astro-site/public/dl/recipe-costing-kit/` (12 xlsx + PDF, 100 % en inglés) | `…/dl/kit-escandallos/` (no se tocan) |
| Stripe | **producto y Payment Link propios, en USD** (los crea John) | los suyos, en EUR |
| Netlify | **env var propia** `VITE_STRIPE_PAYMENT_LINK_RECIPE_COSTING_KIT`, scope Builds, **todos los contextos** [T15]; la da de alta Claude con el link de John | `VITE_STRIPE_PAYMENT_LINK_ESCANDALLOS` |
| Backend | entradas propias con `lang: 'en'` (verify, resend, downloads, admin y su desplegable, precios, links); email de acceso en inglés | las suyas |
| Compra | cada producto tiene su propio acceso. ⚠️ Que una sesión pagada de uno **no** abra el otro solo se garantiza con `PURCHASE_VALIDATION=strict`; hoy está en `soft`, que es decisión aparcada por John (§5) [T8] | — |

Lo único compartido es el **diseño**: la plantilla `KitExcelLandingPage` y los componentes del dashboard, los dos con
`lang`.

### 0.3 Research como en español y OK de John antes de construir (John, 24-sep)

John, 24-sep: «aprovechando de los archivos en español lo que se pueda aprovechar, pero se debe hacer un research
adaptado a su mercado en inglés como se hace en español».

Método de la memoria `feedback_research-previo-producto-nuevo`: 8 bloques adaptados a US/UK.
1. Tipos de comprador.
2. Normativa.
3. Herramientas y software del sector.
4. Proveedores y formatos de compra.
5. Modelo de negocio.
6. Referentes.
7. Necesidades de documentación propias del mercado EN.
8. Precio y comparables.

Se entregan a John y **se espera su OK antes de la F2**. Lo que el research pida y el kit ES no traiga (un formato de
compra nuevo, una hoja nueva) **se propone a John antes de hacerlo**.

**OK de John (24-sep):**
- OK al research y a la adaptación que sale de él.
- «Yield Test» e «Ingredient Price List»: **sí, en español e inglés a la vez** (D17).
- Licencia: **un negocio por compra** (D18).

## 1. Decisiones

| # | Tema | Decisión |
|---|---|---|
| D1 | Slug | `recipe-costing-kit` → `/en/digital-products/recipe-costing-kit` (+ `/access`, `/library`) [research §6.4] |
| D2 | Nombre | **Recipe Costing Kit Pro**, gemelo de «Kit de Escandallos Pro». Ya lo llevan la tarjeta del hub EN, el catálogo, los 26 banners y los spokes EN. Se propaga igual a H1, `<title>`, dashboard, email, changelog, metadatos de los xlsx y productLabel [T13, M15]. Title SEO: `Recipe Costing Kit Pro: 11 Food Cost Templates for Excel` (+ «& Google Sheets» solo si pasa el test, D16) |
| D3 | Precio | **$19**, pago único, acceso de por vida [research §5.2] |
| D4 | Anclas comerciales | **Igual que en español** (John, 24-sep): precio tachado, % de descuento, nota de lanzamiento, «#1», valor de los bonos, badge «Best Seller». Solo se convierten y suben al escalón $…9 los importes **base**: el `priceOld` y el valor de cada bono. Todo lo demás se **deriva**: valor de bonos = suma de bonos; total = priceOld + bonos; ahorro = priceOld − 19; % = 1 − 19/priceOld. Gate con esas 4 identidades, y `cta.items` repite los valores de `bonus.items` [M3]. **Sin** testimonios, reseñas, rating ni `aggregateRating` (decisión del 23-sep, TIENDA §3.5) |
| D5 | Moneda en los xlsx | Formato numérico **sin símbolo** (`#,##0.00`; el 11 `#,##0`). Rótulos sin «(€)». Instrucciones: «amounts are in your currency». Cero `€` y cero `$` en valores **y** en `number_format` [T9] |
| D6 | Impuesto | Misma celda y mismas filas que el ES, con otro rótulo: `Tax rate (%)` (sales tax / VAT / GST), **0 % por defecto**; `Suggested menu price (pre-tax)`; `Menu price incl. tax`; `Current menu price (pre-tax / ex VAT)`. No hay conmutador: sería una fila y una fórmula nuevas en 71 hojas. Instrucciones con la tabla por mercado: US 0 % o su tipo local (la carta va sin impuestos); UK 20 % VAT (se imprime el precio «incl. tax»; el precio actual se teclea sin VAT = carta ÷ 1,2); CA, carta sin impuestos; AU 10 % GST incluido |
| D7 | Unidades y `Conversions` [T1, M4, research 8b-B §1.6] | Ejemplos en **US customary**. **Desplegable EN** (una lista literal por hoja, como el ES; 33 unidades, 241 caracteres ≤ 255): `lb,oz,kg,g,gal,qt,pt,imp pt,cup,fl oz,tbsp,tsp,L,ml,cl,each,dozen,bunch,can,bottle,15 dz case,30 dz case,50 lb bag,40 lb case,36x1 lb case,16 kg sack,40x250 g case,4x1 gal case,12x750 ml case,24x12 fl oz case,1/2 bbl keg,1/6 bbl keg,50 L keg`. **Sin `case` genérico**: ningún factor único vale para 4 gal, 36 lb o 180 huevos. `Conversions` **generada por regla** en `mapas.py`: una clave `compra→uso` por cada pareja de la **misma dimensión**, con factor = tamaño(compra) ÷ tamaño(uso) y factores NIST. Los packs solo como unidad de compra, con su identidad y subunidades (`→each`, `→bottle`, `→can`). `can`/`bottle` solo a volumen, `each` y sí mismas. `bunch` sin peso. Unas **224 claves**, cero duplicados, cero peso↔volumen. `bottle` = 750 ml y `can` = 12 fl oz, editables, con aviso UK (70 cl / 330 ml). Tamaños de pack con fuente (USDA, TTB 27 CFR 5.203 y 25.11, distribuidores: 8b-B §1.4). Columna C generada («1 × 50 lb bag = 800 oz»). Rangos VLOOKUP `$A$5:$B$260` (tabla + ~30 filas vacías) y área de impresión hasta la última fila [T3]. Avisos: oz ≠ fl oz; US ≠ imperial; nunca peso↔volumen («pro kitchens weigh: weigh one cup once») |
| D8 | Terminología [M7, M21] | Glosario del research §1.1: recipe cost card; **Trim loss %** para la merma (cabecera «Yield % = 100 % − trim loss %»); «waste» **solo** para el desperdicio (09 y BONUS); AP/EP; **Q-factor (%)** = «seasonings, oil, garnish, packaging and small prep losses you don't cost line by line» (sin energía, también en el 05); target/actual food cost %. Filas 36-37: **Gross profit per portion (at suggested price)** y **Target GP % (at suggested price)**. Fila 40: **Actual food cost % (actual GP % = 100 % − this)**. Pour cost en el bar. **Nunca «entrée».** Ortografía estadounidense; vocabulario UK solo en Instrucciones |
| D9 | Ficheros y hojas | Nombres del research §1.2-1.3, salvo `Waste Factors`, que pasa a **`Yield Factors`** [M21]. El renombrado se hace **en el motor** y reescribe todas las referencias (§2.2) |
| D10 | Recetas de ejemplo | **Las mismas del ES** (regla de copia), traducidas. Se permite sustituir un **ingrediente** sin fuente de precio ni disponibilidad en EE. UU. por otro medible (p. ej. Serrano por Ibérico), manteniendo el plato, la hoja y la estructura [M9]. 01 «Beef Tenderloin with PX Sherry Reduction & Asparagus» |
| D11 | Precios de ejemplo [M9] | `mercado_en.json` lleva **una fila por ingrediente**: los 126 de las recetas, 15 del BONUS y 7 de `Bottle Sizes`. Cada fila tiene fuente (BLS, USDA, distribuidor…) o `[estimado]`. Gate: falla si falta alguna. **Nunca** se fabrica un precio de ingrediente para que cuadre un porcentaje. En el xlsx no se fecha ningún precio: una línea en Instrucciones, «Sample prices are illustrative U.S. references — replace them with your own supplier invoices». Nunca se convierten los € del ES |
| D12 | Benchmarks, **fuente única** [M6] | Fine dining 30-35 % · casual 28-32 · fast casual 27-32 · café 25-30 · catering 28-35 · food truck 28-35 · hotel F&B 30-35 (sin fuente, se mantiene) · pastry & bakery 25-35 · bar **18-24 %** (pour cost) · delivery 28-32 % sobre neto con **comisión 25 %** por defecto (nota «UK ≈ 30 %»). Alimenta la calculadora 10, las Instrucciones del 04 al 08, la landing (grid y FAQ) y la sección de benchmarks del bono. Gate de texto: todo rango «NN-NN %» en xlsx, .md y data file coincide con D12 |
| D13 | Fechas y papel | Las **93 celdas** de fecha (06 ×2, 09 ×1, BONUS ×90) pasan a fecha corta del sistema (`numFmtId 14`), no a un `mm/dd` fijo [M17]. Meses en inglés. **US Letter** (`paperSize 1`), mismo ajuste a una página de ancho. Pie «AI Chef Pro · aichef.pro · Page &P of &N» |
| D14 | Versión y actualizaciones | «Version 2.0 · September 2026 · aichef.pro/en/digital-products/recipe-costing-kit · info@aichef.pro». Changelog EN con una entrada (primera edición en inglés del contenido 2.0). **Regla:** cada versión nueva del ES se porta al EN en la siguiente sesión EN de la rotación, con su changelog y su broadcast EN [M22] |
| D15 | «Menu engineering» [M14] | Las plantillas no hacen análisis de menú; el bono sí trae una **introducción** (paso 5, matriz Kasavana & Smith). La landing puede decir «includes a basic menu-engineering step in the 30-day guide» y nada más. Se corrige TIENDA §2 con este matiz |
| D16 | Google Sheets | Hasta que pase el test real, **solo «Microsoft Excel»** en `compatApps`, `compatPills`, FAQ, title y dashboard [M8]. Consentimiento de John para usar su Drive: **pendiente**; se pregunta cuando existan los ficheros |
| D17 | **Dos plantillas nuevas, ES y EN a la vez** (John, 24-sep) | Ficheros **independientes**; no son hojas dentro de 01-08. Así no se reescribe la columna de precio de 71 hojas ni se enlazan libros separados, algo que no funciona bien entre ficheros ni en Google Sheets. **Primero en español** (Kit de Escandallos Pro **v2.1**, §2.0) y el EN los recibe por el mismo pipeline de duplicado. `12-test-de-rendimiento.xlsx` → `12-yield-test.xlsx` · `13-lista-precios-ingredientes.xlsx` → `13-ingredient-price-list.xlsx`. El kit pasa de 11 a **13 plantillas** + 2 bonus (landing, hub, dashboard y SEO: «13 Food Cost Templates»). Precio **sin cambio**: 12 € y $19. La subida a $24 del research queda para cuando haya reseñas EN |
| D18 | Licencia (John, 24-sep) | **Un negocio por compra.** Se puede usar en tu negocio o con tus clientes, pero **sin entregarles copias**: cada negocio compra la suya. Escuelas: licencia de aula en info@aichef.pro. Va en una FAQ de la landing EN y en una línea de Instrucciones de los xlsx EN. En ES no se añade: no se ha pedido |
| D19 | Ventas netas [research 8b-A C1] | «Net sales» = **sin impuesto y sin service charge ni propinas** en los textos del 10, el 11, el BONUS, el PDF e Instrucciones. UK: Employment (Allocation of Tips) Act 2023 y VAT Notice 709/1. US: DOL Fact Sheet #15 |
| D20 | De la factura al precio por unidad [8b-B §1.6] | Bloque de Instrucciones en 01-08, «From invoice to price per unit»: catch weight → `lb`/`kg`; caja de la lista → precio de la caja tal cual; caja fuera de la lista → `lb`/`each` con precio ÷ contenido (*pack/size*); lata #10 por peso neto; aceite de freidora al Q-factor; precios sin impuesto recuperable. Más textos breves: yield propio, cooking loss, escalado, subrecetas y pesar los secos. En `Yield Factors`, A2 remite al **12 Yield Test** y al USDA Food Buying Guide |

## 2. Entregables (F2)

### 2.0 Primero el español: Kit de Escandallos Pro v2.1 (D17)

Dos libros nuevos con las convenciones del kit v2.0:
- celdas de entrada en verde `E8F5E9` y calculadas sin relleno;
- todas las divisiones con `IFERROR`;
- protección de hoja sin contraseña, con las entradas desbloqueadas;
- A4, pie y metadatos;
- línea «Versión 2.1 · <mes> 2026 · aichef.pro/kit-escandallos»;
- `inject_cache.py` al final;
- verificación con pycel.

Los textos los escriben subagentes Anthropic (regla 1bis). El generador vive en
`scripts/productos-digitales/kit-escandallos-v2_1/`.

**`12-test-de-rendimiento.xlsx`**
- `Instrucciones`.
- **`Test de despiece`** (*butcher's yield test*):
  - Cabecera (entradas): producto, proveedor, fecha, peso de compra (AP), precio por kg AP y coste AP.
  - Tabla de hasta 12 componentes: pieza; tipo con DV `Útil / Subproducto / Desecho`; peso; valor de mercado por kg (solo subproductos); valor; % del AP.
  - Resultado: peso útil, valor de subproductos, coste neto útil = coste AP − subproductos, **rendimiento %**, **coste por kg útil**, **factor de coste** = coste por kg útil ÷ precio AP, **merma % para el escandallo** = 1 − rendimiento, porción estándar y coste por porción.
- **`Test de cocción`** (*cooking loss test*):
  - Entradas: peso crudo útil, coste crudo (a mano o el coste por kg útil del despiece) y peso cocinado.
  - Resultado: **pérdida por cocción %**, coste por kg cocinado, porción cocinada, coste por porción y **rendimiento combinado** = despiece × cocción.
- Ejemplos: el del despiece es una pieza del kit (solomillo o lomo entero); el de cocción, una elaboración del kit (hamburguesa o asado). Rendimientos típicos con fuente o `[estimado]`. «Duplica la pestaña para otro test.»

**`13-lista-precios-ingredientes.xlsx`**
- `Instrucciones`.
- **`Lista de precios`**: un bloque de resumen arriba (nº de ingredientes, nº de alertas y mayor subida) y una tabla de ~120 filas.
  - Columnas: ingrediente · categoría · proveedor · formato de compra (texto de la factura) · contenido del formato · unidad base (DV) · **precio del formato** · **precio por unidad base** · precio anterior · **variación %** · estado OK/ALERTA (CF) · fecha de la última factura · notas.
  - Umbral de alerta en celda verde (5 %).
  - Precargada con los ingredientes de ejemplo de las plantillas.
- **Honestidad:** las fichas **no se alimentan solas** de la lista, porque cada plantilla es un libro independiente. Las Instrucciones y la landing lo dicen: «copia el precio por unidad base a la ficha, con esa unidad como unidad de compra».
- Sin comparador de proveedores: es del Kit de Inventario.

**Publicación del ES v2.1**, en un PR propio antes de la F3 EN:
- los ficheros en `dl/kit-escandallos/`;
- claves en `get-download-urls.ts`;
- 2 tarjetas en el dashboard ES;
- grid de la landing ES, y «11» → «13» en landing, hub ES, catálogo y FAQ;
- `productos-changelog.ts` 2.1;
- broadcast ES en la cola de 5 días (regla del 5-sep).

**Gates:** `censo-entregables.py --only kit-escandallos --fail`, `gate-flujo-postpago.py`, pycel y `tienda-gate --es-identico` (solo cambian las landings esperadas).

### 2.1 Fuente y método

- **Fuente = los xlsx publicados** en `astro-site/public/dl/kit-escandallos/`: los 12 de la v2.0 (`ed45f35`) **+ los
  2 nuevos de la v2.1** (§2.0), y el `bono-guia-food-cost-30-dias.md`. **No** se usa `scripts/generate-escandallos.py`: es la v1.0 (inventario §2).
- Salida: `astro-site/public/dl/recipe-costing-kit/` (14 xlsx + PDF). **Los ficheros ES no se tocan.**
- Código en `scripts/productos-digitales/recipe-costing-kit/`:
  - `extraer_textos.py` → `textos_es.json` (832 cadenas con contexto).
  - `mapas.py`: hojas, claves-dato, literales y la `Conversions` generada (D7).
  - `textos_en.json`: traducción cadena a cadena por subagentes Anthropic; nada de `bridge.py` (regla 1bis).
  - `mercado_en.json`: sobrescrituras de celda con fuente o `[estimado]`, más **la lista cerrada de «textos con cifra derivada»** [M5]. Son las celdas de Instrucciones y notas que citan cifras que la versión EN cambia: comisión, tamaños de botella y lata, IVA, precios, ratio de camareros, «~21 %», «unos 3 puntos». Se **reescriben** con la cifra recalculada sobre la hoja EN final; no se traducen literalmente.
  - `aplicar_en.py`: copia → hojas → claves → `Conversions` → textos → literales → formatos → mercado → metadatos (los 6 campos de docProps, incluido `category` «AI Chef Pro · Digital products» [T9]), pie y papel → `inject_cache.py` **al final**. Idempotente y con `--dry-run` sobre el scratchpad.
- En el mismo commit que publica `dl/recipe-costing-kit/`, `recipe-costing-kit` entra en `EXCLUIDOS` de
  `postprocess-transversal.py`. Si no, un `all` le forzaría A4 y metadatos en español [T12].
- Ejecución en el **Mac, en serie, con el vigilante**: openpyxl no calienta (decisión del 20-sep). El venv del VPS no
  tiene openpyxl.

### 2.2 Renombrado de hojas

Con el mapa se reescribe, en el mismo paso:
- las 849 fórmulas `Hoja!` / `'Hoja'!`;
- las 29 DV `Mermas!…`;
- la CF de 03 `Rotación Semanal`;
- el XML de los 2 gráficos;
- las áreas de impresión de las 71 hojas;
- **todos los textos que citan pestañas**: Instrucciones, notas A2/A18 del 04, `Presupuesto!B3/B6` del 06, `Evolución!A2/A6` del 09 y mensajes de error de las DV [T14].

Nombres ≤ 31 caracteres, sin `[]:*?/\`.

**Gate:**
- ninguna fórmula, DV, CF, gráfico ni área de impresión cita una hoja inexistente;
- todo nombre entre «» o '' de cualquier texto o mensaje de DV existe en `wb.sheetnames` del libro, salvo una lista blanca de conceptos que no son pestañas.

### 2.3 Claves-dato

El mismo mapa se aplica **a la vez** en la tabla (`Yield Factors`, `Conversions`), en las listas de las DV y en las
filas de ejemplo.
- Categorías: research §1.4.
- Unidades: D7 (`ud` → each, `docena` → dozen, `manojo` → bunch, `sobre` → packet, `lata` → can, `botella` → bottle).
- Motivos del BONUS: traducidos.

**Gate:**
1. Cero claves duplicadas en `Conversions`.
2. Las dos unidades de cada clave están en la lista de la DV.
3. Toda pareja de la misma magnitud entre unidades del desplegable resuelve.
4. Cada envase es coherente con su tamaño único.
5. Toda fila de ejemplo resuelve su factor (≠ «?») y su categoría (≠ «»).
6. Escribir una pareja nueva en la primera fila libre de `Conversions` la resuelve [T3].

### 2.4 Literales de fórmula

- `"revisa merma"` → `"check trim loss"` (453 celdas).
- `"revisa unidades"` → `"check units"` (453).
- `"ALERTA"` → `"ALERT"`: 29 celdas **y** las 2 reglas CF que colorean por esa cadena.
- Sin cambios: `"OK"`, `"?"`, `"→"`, `"✓"`, `"?*"`, `">0"`.

### 2.5 Adaptación de mercado por fichero

| Fichero EN | Qué se adapta además del texto |
|---|---|
| 01 standard recipe cost card | Ingredientes en lb/oz/fl oz con precio por unidad de compra US (el solomillo en **catch weight**, `lb`); filas de impuesto (D6), GP (D8) y Q-factor 10 %. Instrucciones con el bloque D20 (común a 01-08) |
| 02 tasting menu | Igual que 01 en los 9 pases; el food cost objetivo único de `Summary` se mantiene |
| 03 prix fixe lunch menu | Extras [M19]: «Bread & butter» con valor, «Drink (if included)» y «Coffee (if included)» **a 0** por defecto, con nota. Food cost objetivo 33 %: se revisa contra D12 (casual 28-32 %) y se justifica en `mercado_en.json` |
| 04 cocktails & drinks | **E3:** `Bottle Sizes!B` en **ml** (750 / 1000 / 1750; en EE. UU. el formato legal de destilado es métrico) y `D5:D16 = IFERROR(ROUND(C*1000/B,4),"")` = «Price per liter». Las recetas compran en `L` y usan `fl oz` (clave `L→fl oz` = 33,814), con pour estándar US de **1.5 fl oz** (NIAAA). Vino 750 ml; la lata va por `can` en `Conversions`, no en esta hoja. Nota UK: 25/35 ml y 70 cl. «Spillage & ice allowance» 5 % [T2, M1]. En las filas vacías de `Bottle Sizes` se precargan **un vino de 750 ml y un barril de 1/6 bbl**. Instrucciones con la tabla de medidas (US 1.5 / 5 / 12 fl oz; UK 25/35 ml, 125/175 ml y ⅓, ½ y ⅔ de pinta), el pour cost por categoría (destilados 18-20 %, barril ≈ 20 %, botella ≈ 25 %, vino más alto) y el impuesto de bebidas que paga el bar (p. ej. Texas 6,7 %) antes del pour cost [8b-A C5, 8b-B §2.4] |
| 05 pastry & bakery | Rendimiento en unidades (se mantiene). **La pastelería de EE. UU. formula en gramos**: compra en formato de caja o `lb` y uso en `g` [8b-A C4]. Ejemplos con el precio de la factura tal cual: harina `50 lb bag`, mantequilla `36x1 lb case`, leche `4x1 gal case`, huevos `15 dz case` [8b-B §1.7]. Mermas de obrador del ES; Q-factor sin «energía del horno» |
| 06 catering & events | Recepción por invitado. En `Event Quote` [8b-A C2, M20]: **1 camarero cada 25 invitados** en recepción (tabla de ratios en Instrucciones: emplatado 1:10-12, buffet 1:20); **camarero $25/h y jefe de sala $35/h** (OEWS $17 + 7,65 % FICA, o tarifa de agencia; `[estimado]` con el ancla); **rentals $3,50/invitado**; **mínimo $1.000**; el «margen sobre servicios» pasa a **«Service charge (%)» 20 %**. En `Event Checklist`: food handler cards / food manager certification, seguro, permisos y «Allergen matrix (US: 9 major · UK/EU: 14)». **`Client Proposal`** [M11]: «Price per guest», «TOTAL», A15 «Quote valid for 30 days. Applicable sales tax is added to the final invoice…», e Instrucciones UK/AU para cambiar a «Prices include VAT/GST». «…the service charge is not a gratuity» (D19) |
| 07 café & brunch | Mismas 4 recetas en unidades US, con alguna fila en formato de caja [8b-B §1.7] |
| 08 food truck | `Break-Even` con costes diarios US: **$45 + $25 + $30 + $300 + $50 + $15 = $465/día** (commissary/parking, permisos y seguro, propano/generador, 2 personas con cargas [M20], amortización, limpieza), con la cuenta de cada línea `[estimado]` [8b-A §4.3] |
| 09 food waste tracker | 16 familias con objetivos, compras de ejemplo en USD, fecha D13, «Week 2…12», objetivo global 4 %. Aviso: «trim loss goes in the recipe cost card, not in the waste log» |
| 10 menu price calculator | Filas D12; ventas netas D19; «DoorDash, Uber Eats or Grubhub (UK: Deliveroo, Just Eat)»; impuesto D6. El «~21 %» se recalcula con la comisión del 25 % (≈ 22,5 %) [M5] |
| 11 monthly food cost dashboard | Meses en inglés (son las categorías del gráfico), año como celda editable, cabecera «Period (month or week)» con el método semanal en Instrucciones, «Net purchases (excl. recoverable tax)», ventas netas D19 y «unos 3 puntos» recalculado [M5, 8b-B §2.6] |
| BONUS inventory & waste control | 15 productos: stock (C:E), precio (I) **y** matriz por ración (C5:Q14) convertidos con el **mismo factor**, con cantidades por ración iguales a la AP qty de las recetas EN. Gate: la desviación relativa H/F de cada producto es la misma que en el ES [M10]. 7 motivos (DV) y platos traducidos. «Net purchases (excl. recoverable tax)». Instrucción para pegar plato + unidades vendidas desde el *product mix* del TPV (Toast, Square, Clover, Lightspeed, Epos Now) en `Sales for the Period` A-B [8b-A C6] |
| **12 yield test** | Duplicado del ES v2.1 (§2.0): lb/oz, USD, ejemplo con una pieza US (p. ej. *whole beef tenderloin, PSMO*), rendimiento típico con fuente o `[estimado]`, y remisión a *Trim loss %* de las fichas |
| **13 ingredient price list** | Duplicado del ES v2.1: unidades base US (`lb, oz, kg, g, gal, fl oz, L, ml, each`), formatos de compra de D7 como texto de factura, distribuidores US genéricos (sin marcas), USD, umbral 5 % |

Transversal:
- Metadatos (§2.1) y línea de versión D14. «© 2026 AI Chef Pro · All rights reserved».
- Rótulos de la foto con la ruta de Excel **y** de Google Sheets.
- Protección: «Review → Unprotect Sheet» / «Data → Protect sheets and ranges».
- `errorTitle` de las 58 DV: «Invalid value» [T9].

### 2.6 El bono PDF

`bonus-guide-food-cost-30-days.md` = el `.md` ES traducido y adaptado por subagentes Anthropic:
- IVA → sales tax/VAT, sin el art. 91 LIVA.
- Benchmarks de D12 en lugar de «España 2026».
- Proveedores y platos genéricos o de EE. UU.; importes en USD.
- Paso 5 (menu engineering básico) sin la venta cruzada a la Guía ES; enlaza al hub EN [M14].
- Nombres de fichero y pestaña EN exactos.
- **Mismo caso práctico: 32 % declarado → 35,36 % real → 31,8 % en 30 días**, con los mismos porcentajes e importes en USD [M13].
- Bio anclada.
- Añadidos del research [8b-A C7/C9, 8b-B §2.6]:
  - semana 1: cómo leer una factura (caja, catch weight, *pack/size*);
  - semana 4: prime cost < 60-65 % (NRA);
  - tabla de economía: márgenes NRA, food cost de cadenas cotizadas (las de Darden y Texas Roadhouse se confirman antes de publicar), inflación USDA ERS/ONS y la regla 30/30/30/10 con su matiz;
  - «Further reading»: *Culinary Math*, *Math for the Professional Kitchen*, *Food and Beverage Cost Control*, sin afiliación;
  - ventas netas D19;
  - las plantillas 12 y 13 donde encajen (yield test en la semana 2, lista de precios en la semana 3).

Maquetador: copia parametrizada de `bono_guia.py` (cabecera, «Page {n}», título, marcador de metadatos, Letter). Gate
de glifos: cero caracteres fuera de WinAnsi y cero restos de español. El nº de páginas se comprueba contra la landing,
porque `paginas-gate.py` solo lee `productos/**` [T9].

## 3. Landing, dashboard y backend (F3)

**Orden [T5]:**
1. El Payment Link se pide a John **al cerrar la F2**.
2. La F3 va en **un solo PR** que lleva a la vez:
   - la env var ya dada de alta;
   - `payment-links.ts` y `product-prices.ts` regenerados;
   - el productId en verify, resend, downloads, admin y `zona-app`;
   - las páginas;
   - `FAMILIAS.en.vivo = true` [T4].
3. Antes de fusionar: gates contra el deploy preview.
4. Nada de producto EN en `main` sin link: `sync-payment-links.py` y `gate-flujo-postpago.py` se pondrían rojos para **todo** el catálogo.
5. Tras el merge: compra de prueba en producción.

**Landing:** `astro-site/src/data/productos-en/kits/recipe-costing-kit.ts` (tipo `KitExcelData`).
- Sin `testimonials`, `reviews` ni `aggregateRating`.
- Anclas D4 y nombre D2.
- FAQ con el PAA (research §6.3) más la de moneda: «amounts have no currency symbol; checkout shows your local currency» [M22].
- Columnas del kit listadas en claro (AI Overview).
- D16 en `compatApps`, `compatPills` y la FAQ.
- `footerLinks` a la tienda y las herramientas EN. `alreadyBought.product = 'recipe-costing-kit'`.
- OG image nueva sin texto español (`generate-images`).
- `src/lib/sitemap-lastmod.json` con la fecha de publicación [T4].
- **13 plantillas** + 2 bonus (D17) en el grid, la lista de columnas y el title.
- FAQ adicionales [8b-A C8, 8b-B §4]:
  - «Does it handle case prices and catch weight?»: sí.
  - «What's not included?»: par levels, menu engineering (solo la introducción del PDF) y auto-feed de precios.
  - Licencia D18.
  - Private chef, meal prep, ghost kitchen y estudiantes.
- **Comparativa honesta kit vs SaaS**: meez $19/mes, Jelly £129/mes, MarginEdge $350/mes, R365 $469-749/mes. El kit no los sustituye; es el pago único para quien aún no los necesita.

**Páginas:**
- `pages/en/digital-products/recipe-costing-kit.astro`: `lang="en"`, `basePath` **sin** `/en`, `alternatesFamilia`, `whatsapp={false}`, `omitGlobalApp`, `miselup={false}`.
- `…/access.astro`: `ProductAccessGate lang="en"`.
- `…/library.astro` + island + `src/pages/RecipeCostingKitDashboard.tsx`, copia traducida de `KitEscandallosDashboard.tsx`:
  - sin Sheets (D16);
  - sin la venta cruzada «Pro Prompts eBook — €9»: se quita o apunta al hub EN [M8].
- `pages/kit-escandallos.astro` → `alternatesFamilia('kit-escandallos')`.

**Componentes compartidos** (`SaasDiscoveryBanner`, `ProductChangelog`, `LogoBadge`, `WhatsAppProductSupport`,
`CryptoPayButton`): prop `lang` con el ES por defecto **byte a byte idéntico**, demostrado [T11]:
- `--es-identico` sobre una muestra de cada plantilla que monta `CryptoPayButton`: KitExcel, Guía, KitTareas, Plan, `pro-prompts-ebook` y `mega-pack-tareas`;
- diff del render ES con `react-dom/server` antes y después, para los React;
- grep estático de «€», restos de español y rutas ES en `RecipeCostingKitDashboard.tsx`, su island y los wrappers EN (son `client:only`: `tienda-gate` no los ve).

**Backend:**
- `zona-app.ts`, `verify-purchase.ts`, `resend-access.ts`, `get-download-urls.ts` y `admin-generate-access.ts` (con email EN).
- **El desplegable de `src/pages/AdminGenerateAccess.tsx`** y su espejo `src/data/productos-digitales-config.ts` [T7]. `gate-flujo-postpago` (sección A) cruza los ids del desplegable con PRODUCTS.

**Cripto:**
- `CryptoPayButton.astro` con `lang`: copy, países, enlace a las condiciones EN (§5.4) y la renuncia «where it applies (EU/UK)».
- `pages/en/crypto-payment.astro` = copia traducida de `pago-cripto.astro`, fuera del sitemap.
- Si no llega a tiempo, el producto va a `CRYPTO_PRODUCTS_EXCLUDE`.

**Gates que hay que ajustar antes:**
- `miselup-gate.py`: en EN, cero tarjetas.
- `whatsapp-gate.py`: exentos anidados.
- `robots-gate.py`: rutas anidadas.
- `censo-entregables.py`: Letter en carpetas EN.
- `tienda-gate.py`: hreflang que apunte a un 404 en páginas EN aún no vivas.
- `nombre-gate.py`: `productos-en/**` con `name.en` [T13].

**Hub EN:** tarjeta con «10 venue types», precio vivo y badge D4.

**Catálogo y blog EN [T6, M2]:**
- `products-catalog.ts` gana `urlByLang.en` **y precio por idioma**: `priceByLang` después de `description`, o el `usd` de `product-prices.ts`.
- Los consumidores usan URL y precio por idioma: `localize()`, las tarjetas de `/en/use-cases/*`, `catalogo_productos()` / `banner()` del ensamblador y `fase8e-banners-corpus.py`.
- Parche quirúrgico de los 26 banners, a URL EN + $19.
- Gate: ningún banner ni página EN apunta a `/kit-escandallos` ni contiene «€12».

**Spokes EN de casos de uso [M16]:** pasada de copy sobre `use-cases-content.en.ts`.
- Se quitan las funciones que el kit no tiene: importar CSV, coste laboral, «load your recipe book», y el «€12».
- Se describe como plantillas donde se teclean o pegan ingredientes y precios.

**Enlazado:** enlaces contextuales desde los posts EN del tema y las herramientas gratuitas. Cero huérfanas.

**Broadcast EN [M18]:** segmento EN de Resend, «Hi everyone,», hueco = último `scheduled_at` + 5 días, 08:00 UTC.

## 4. Gates

**F2**
1. **Paridad estructural EN↔ES.** Mismas hojas vía el mapa. Misma fórmula celda a celda, salvo los mapas de hoja y de literales y las excepciones E1-E4 de §0.1. Mismas DV, CF, merges, protección, paneles, áreas de impresión (salvo E2) y series de gráfico.
2. **Restos y caracteres.** Cero `€` / `$`, cero restos de español y cero caracteres no latinos. Se buscan en: valores, `number_format`, nombres de hoja, mensajes y títulos de DV, títulos de gráfico, cabeceras y pies, y los 6 campos de docProps. Lista blanca: açaí, jalapeño, Ibérico, Manchego, PX… [T9].
3. **Cálculo.** Caché con `data_only`; pycel sin `#REF!` ni `#VALUE!`; los 6 checks de §2.3; sensibilidad (cambiar un precio o el impuesto mueve lo que debe).
4. **Ejemplos creíbles [T10, M9].** Por receta, un **precio de carta US de referencia** con fuente o `[estimado]` en `mercado_en.json`. El food cost implícito (coste por ración ÷ ese precio) cae en el rango D12 de su tipo de local; el pour cost de las 4 recetas del 04, entre 18 y 24 %. Si una receta cae fuera, se corrige la **cantidad** o el precio de carta de referencia, **nunca** un precio de ingrediente con fuente. Además, `mercado_en.json` completo (D11).
5. **Formato.** Letter; cero formatos con `€` o `dd/mm`; las 93 fechas con `numFmtId 14`; línea de versión D14 en todos.
6. **Coherencia de texto.** Rangos de D12 [M6]; cifras derivadas recalculadas [M5]; nombres de pestaña en textos (§2.2).
7. `censo-entregables.py --only recipe-costing-kit --fail` en 0, con Letter admitido.
7bis. **Libros 12 y 13** (ES v2.1 y EN): pycel sin errores; el ejemplo da un rendimiento entre 0 y 1, un factor de coste ≥ 1 y un coste por porción coherente; la alerta de precio salta cuando la variación supera el umbral y no salta cuando no; la lista de unidades base casa con D7.
8. **Revisión adversarial** con tope de 2 rondas: lente de chef o manager de EE. UU. y del Reino Unido, y lente técnica.
9. **Test de Google Sheets**, si John da el consentimiento (D16).

**F3**
- Gates: `tienda-gate.py` (estático y `--base`), `gate-flujo-postpago.py` LIVE, `robots-gate`, `whatsapp-gate`, `miselup-gate`, `datafast-gate`, `nombre-gate`, y los de T11.
- **`audit-payment-links.py`**, más una consulta a Stripe del Price: currency usd, unit_amount 1900 = `product-prices.ts` [T15].
- Gate de anclas D4 y gate de banners y spokes (§3).
- Compra de prueba: email EN, dashboard, 13 descargas y log `[purchase-validation]` con match en `recipe-costing-kit` [T8].
- `fase8c-libreria-en-gate.py --todos`.

## 5. Pendiente de John

1. **Payment Link USD $19**, al cerrar la F2. Claude le entrega en un bloque:
   - nombre;
   - descripción en prosa de ~260 caracteres;
   - imagen;
   - `success_url` = `https://aichef.pro/en/digital-products/recipe-costing-kit/access?session_id={CHECKOUT_SESSION_ID}`;
   - `currency_options` GBP, CAD y AUD calculados ese día a escalón psicológico [M18].

   Antes de crearlo, John comprueba en Stripe que **USD es moneda de liquidación** (si no, Adaptive Pricing no convierte) y fija `tax_behavior` [T15].
2. **Fiscalidad de la venta**: registro de VAT del Reino Unido desde la primera venta a consumidores (servicios digitales, sin umbral), más CA, AU y EE. UU. Con el asesor, antes de la F3 (research §3.4).
3. **Consentimiento para el test de Sheets** en su Drive (D16).
4. **Condiciones de compra EN** para productos digitales: pago único, acceso de por vida, garantía de 30 días y renuncia al desistimiento donde aplique (EU/UK). `/en/terminos` solo trata la suscripción del SaaS, y es el destino del enlace del diálogo cripto y de los términos del Payment Link. Decisión legal suya antes de la F3 [M12]. El ES tiene el mismo hueco.
5. `PURCHASE_VALIDATION=strict`: sin él, una sesión pagada de un producto abre otro [T8]. Aparcado por él.
6. ~~OK del research de 8 bloques~~ ✅ recibido el 24-sep (§0.3).

## 6. Presupuesto y fases

Tamaño **M** (≤ 5 M tokens de subagentes). F1 lleva ≈ 2,1 M: inventario y research, 0,72 M; revisión R1, 0,70 M;
8 bloques, 0,67 M. Falta la ronda R2.

⚠️ D17 amplía el alcance con el ES v2.1: dos libros nuevos y su publicación. Si el total pasa de 6,5 M (techo + 30 %),
se para y se reporta a John (política del 20-sep).

- **F2-ES (v2.1):** generador de los 2 libros nuevos (opus) + textos (subagentes) → gates → PR de publicación ES.
- **F2-EN:** `extraer_textos.py` + `mapas.py` (opus) → traducción por grupos (sonnet, 2 a la vez, glosario común primero) → `mercado_en.json` (opus) → `aplicar_en.py` (opus) → gates → revisión.
- **F3:** capa de producto en un PR → Payment Link (John) → merge → compra de prueba → broadcast.

Cada fase cierra con su gate, `commit` + `push` y una línea en el handoff.
