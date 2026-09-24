# Recipe Costing Kit Pro — SPEC (F1 · 24-sep-2026 · sesión Claude Code)

> Primer producto de la **Tienda internacional en inglés**. Es la versión inglesa del **Kit de Escandallos Pro**
> (`kit-escandallos`, 12 €, contenido v2.0). Doc canónico: `scripts/productos-digitales/TIENDA-INTERNACIONAL.md`.
>
> Base:
> - `F1-inventario-es.md`: qué entrega hoy el ES, con fichero:línea.
> - `F1-research-us-uk.md`: mercado, con la fuente de cada dato.
> - `F1-research-8-bloques-en.md`: los 8 bloques del método, en curso.
> - `SPEC-R1.json`: revisión adversarial ronda 1, 37 hallazgos, todos incorporados aquí (IDs T# y M# entre corchetes).
> - `SPEC-R2.json`: ronda 2 (la última; tope de 2), 46 hallazgos incorporados (IDs R2T-# y R2-#). Lo que quede lo
>   cazan los gates de script.
>
> Esta SPEC **decide**. Lo que no está aquí no se hace.
>
> Estado: research de 8 bloques hecho (`F1-research-8-bloques-en.md`) y **OK de John recibido el 24-sep** con dos
> decisiones que amplían el alcance: **dos plantillas nuevas en ES y EN a la vez** (D17) y **licencia de un negocio
> por compra** (D18). R2 incorporada. **Próximo paso: F2-ES (v2.1).**

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
- **E5.** La lista literal de la DV de unidades se **sustituye** por la de D7; no se mapea. El gate comprueba que el `sqref`, el tipo y el `errorStyle` no cambian y que la lista es exactamente la de D7 [R2T-03].

John, 24-sep: «los archivos se tienen que adaptar a inglés y a métricas de uso común en US/UK».

### 0.2 Producto INDEPENDIENTE del español (John, 24-sep)

John, 24-sep: «el producto en inglés tiene que ser independiente al español al igual que los otros idiomas, con su
propio dashboard, sus propios archivos… su propio producto en Stripe y var env en Netlify».

| Pieza | Recipe Costing Kit Pro (EN) | Kit de Escandallos Pro (ES) |
|---|---|---|
| productId | `recipe-costing-kit` | `kit-escandallos` |
| Landing | `/en/digital-products/recipe-costing-kit` | `/kit-escandallos` |
| Acceso y dashboard | `…/recipe-costing-kit/access` y `…/library`; `RecipeCostingKitDashboard.tsx`; JWT `recipe-costing-kit-jwt` | `/kit-escandallos-access` y `-library` |
| Ficheros | `astro-site/public/dl/recipe-costing-kit/` (14 xlsx + PDF = 13 plantillas + 2 bonus, 100 % en inglés) | `…/dl/kit-escandallos/` (no se tocan) |
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
| D2 | Nombre [T13, M15, R2T-21] | **Recipe Costing Kit Pro**, gemelo de «Kit de Escandallos Pro». Ya lo llevan la tarjeta del hub EN, el catálogo, los 26 banners y los spokes EN. `titlePre + titleGold` y `schema.productName` = «Recipe Costing Kit Pro» **exactos**; la cifra va en `titlePost` o en la descripción. Se propaga a `<title>`, dashboard, email, changelog, metadatos de los xlsx y productLabel. Title SEO: `Recipe Costing Kit Pro: 13 Food Cost Templates for Excel` (+ «& Google Sheets» solo si pasa el test, D16). Gate: `nombre-gate.py --only recipe-costing-kit` |
| D3 | Precio | **$19**, pago único, acceso de por vida [research §5.2] |
| D4 | Anclas comerciales | **Igual que en español** (John, 24-sep): precio tachado, % de descuento, nota de lanzamiento, «#1», valor de los bonos, badge «Best Seller». Solo se convierten y suben al escalón $…9 los importes **base**: el `priceOld` y el valor de cada bono. Todo lo demás se **deriva**: valor de bonos = suma de bonos; total = priceOld + bonos; ahorro = priceOld − 19; % = 1 − 19/priceOld. Gate con esas 4 identidades, y `cta.items` repite los valores de `bonus.items` [M3]. **Sin** testimonios, reseñas, rating ni `aggregateRating` (decisión del 23-sep, TIENDA §3.5) |
| D5 | Moneda en los xlsx | Formato numérico **sin símbolo** (`#,##0.00`; el 11 `#,##0`; precio por unidad base del 13, 4 decimales). Rótulos sin «(€)». Instrucciones: «amounts are in your currency». Cero `€` en todo el libro. **`$` solo** dentro de celdas de TEXTO de Instrucciones y notas, en ejemplos US («a $29.99 bag of flour»); nunca en `number_format` ni en celdas numéricas [T9, R2T-14] |
| D6 | Impuesto | Misma celda y mismas filas que el ES, con otro rótulo: `Tax rate (%)` (sales tax / VAT / GST), **0 % por defecto**; `Suggested menu price (pre-tax)`; `Menu price incl. tax`; `Current menu price (pre-tax / ex VAT)`. No hay conmutador: sería una fila y una fórmula nuevas en 71 hojas. Instrucciones con la tabla por mercado: US 0 % o su tipo local (la carta va sin impuestos); UK 20 % VAT (se imprime el precio «incl. tax»; el precio actual se teclea sin VAT = carta ÷ 1,2); CA, carta sin impuestos; AU 10 % GST incluido |
| D7 | Unidades y `Conversions` [T1, M4, 8b-B §1.6, R2T-01/02, R2-06/07/14] | Ejemplos en **US customary**. **Desplegable EN** (una lista literal por hoja, como el ES; 34 unidades, 248 caracteres ≤ 255): `lb,oz,kg,g,gal,qt,pt,imp pt,cup,fl oz,tbsp,tsp,L,ml,cl,each,dozen,bunch,packet,can,bottle,15 dz case,30 dz case,50 lb bag,40 lb case,36x1 lb case,16 kg sack,40x250 g case,4x1 gal case,12x750 ml case,24x12 fl oz case,1/2 bbl keg,1/6 bbl keg,50 L keg`. **Sin `case` genérico.** **Regla cerrada de `Conversions`**, generada por `mapas.py`, que se versiona en el repo: (1) **base↔base**: toda pareja de unidades base de la misma dimensión (masa `lb,oz,kg,g`; volumen `gal,qt,pt,imp pt,cup,fl oz,tbsp,tsp,L,ml,cl`; recuento `each,dozen`), identidades incluidas; (2) **packs** (los 13 formatos): solo como origen; identidad, subunidad (`→each`, `→bottle`, `→can`) y destinos base de su dimensión. **Excluidos** `cup,tbsp,tsp` como destino de barriles y cajas de bebida; (3) **`can` y `bottle`**: solo origen, con destinos `fl oz, ml, cl, L, each` y sí mismos. **Nunca** `cup/tbsp/tsp/qt/gal/pt`: en una factura de cocina la lata es la #10 y se compra en oz. Sus filas son **fórmulas sobre una única celda de tamaño** (`bottle→ml` = 750; `can→ml` = 355): el UK edita un valor [R2T-20]; (4) `bunch` y `packet`: identidad y `→each` = 1, sin peso. Cero duplicados, cero peso↔volumen. **n** lo calcula el script: rango VLOOKUP de las 453 fórmulas = `$A$5:$B${4+n+30}` y área de impresión igual. Nada de cifras fijas en la SPEC. Columna C generada («1 × 50 lb bag = 800 oz»; `can`: «beverage can 12 fl oz — for #10 food cans buy in oz»). Tamaños con fuente (8b-B §1.4). Avisos: oz ≠ fl oz; US ≠ imperial; nunca peso↔volumen («pro kitchens weigh: weigh one cup once») |
| D8 | Terminología [M7, M21] | Glosario del research §1.1: recipe cost card; **Trim loss %** para la merma (cabecera «Yield % = 100 % − trim loss %»); «waste» **solo** para el desperdicio (09 y BONUS); AP/EP; **Q-factor (%)** = «seasonings, oil, garnish, packaging and small prep losses you don't cost line by line» (sin energía, también en el 05); target/actual food cost %. Filas 36-37: **Gross profit per portion (at suggested price)** y **Target GP % (at suggested price)**. Fila 40: **Actual food cost % (actual GP % = 100 % − this)**. Pour cost en el bar. **Nunca «entrée».** Ortografía estadounidense; vocabulario UK solo en Instrucciones |
| D9 | Ficheros y hojas | Nombres del research §1.2-1.3, salvo `Waste Factors`, que pasa a **`Trim Loss Factors`** (cabeceras «Typical / Min / Max trim loss %» y nota «yield = 100 % − trim loss») [M21, R2T-23, R2-20]. Libros nuevos: 12 `Butcher Yield Test`, `Cooking Loss Test`; 13 `Price List`, sin apóstrofos [R2T-07]. En los textos EN, las pestañas se citan **solo entre comillas dobles rectas** ("Recipe Cost Card") [R2T-18]. El renombrado se hace **en el motor** y reescribe todas las referencias (§2.2) |
| D10 | Recetas de ejemplo | **Las mismas del ES** (regla de copia), traducidas. Se permite sustituir un **ingrediente** sin fuente de precio ni disponibilidad en EE. UU. por otro medible (p. ej. Serrano por Ibérico), manteniendo el plato, la hoja y la estructura [M9]. 01 «Beef Tenderloin with PX Sherry Reduction & Asparagus». En EN, la celda «Current menu price» de cada receta **se precarga** con el precio de carta de referencia de `mercado_en.json`, para que el ejemplo enseñe el food cost real y la CF. Es contenido, no estructura [R2T-22] |
| D11 | Precios de ejemplo [M9] | `mercado_en.json` lleva **una fila por ingrediente**: los 126 de las recetas, 15 del BONUS, 8 de `Bottle Sizes` y los ejemplos de los libros 12 (pieza y subproductos) y 13 [R2T-08, R2-10, R2-18]. Cada fila tiene fuente (BLS, USDA, distribuidor…) o `[estimado]`. Gate: falla si falta alguna. **Nunca** se fabrica un precio de ingrediente para que cuadre un porcentaje. En el xlsx no se fecha ningún precio: una línea en Instrucciones, «Sample prices are illustrative U.S. references — replace them with your own supplier invoices». Nunca se convierten los € del ES |
| D12 | Benchmarks, **fuente única** [M6] | Fine dining 30-35 % · casual 28-32 · fast casual 27-32 · café 25-30 · catering 28-35 · food truck 28-35 · hotel F&B 30-35 (sin fuente, se mantiene) · pastry & bakery 25-35 · bar **18-24 %** (pour cost) · delivery 28-32 % sobre neto con **comisión 25 %** por defecto (nota «UK ≈ 30 %»). Alimenta la calculadora 10, las Instrucciones del 04 al 08, la landing (grid y FAQ) y la sección de benchmarks del bono. Gate de texto **acotado** [R2T-13, R2-08]: solo compara los rangos que van junto a una etiqueta de tipo de local de D12, los de las filas de la calculadora y los del grid y la FAQ de la landing. Lista blanca en `mercado_en.json` para pour cost por categoría, prime cost, comisión, service charge, objetivos de desperdicio del 09, rendimientos del 12 y cadenas cotizadas |
| D13 | Fechas y papel | **Toda** celda de fecha pasa a fecha corta del sistema (`numFmtId 14`), no a un `mm/dd` fijo [M17]: 93 en 06, 09 y BONUS, más las de 12 y 13. Los libros 12 y 13 ES **nacen** con `numFmtId 14`. Los gates cuentan por regla, no por número [R2-11]. Meses en inglés. **US Letter** (`paperSize 1`), mismo ajuste a una página de ancho. Pie «AI Chef Pro · aichef.pro · Page &P of &N» |
| D14 | Versión y actualizaciones [R2T-16, R2-05] | El EN nace del ES **v2.1**: «Version 2.1 · <mes de publicación> 2026 · aichef.pro/en/digital-products/recipe-costing-kit · info@aichef.pro». `aplicar_en.py` resuelve el mes al publicar. Changelog EN: «first English edition of content 2.1». **Regla:** cada versión nueva del ES se porta al EN en la siguiente sesión EN de la rotación, con su changelog y su broadcast EN [M22] |
| D15 | «Menu engineering» [M14] | Las plantillas no hacen análisis de menú; el bono sí trae una **introducción** (paso 5, matriz Kasavana & Smith). La landing puede decir «includes a basic menu-engineering step in the 30-day guide» y nada más. Se corrige TIENDA §2 con este matiz |
| D16 | Google Sheets | Hasta que pase el test real, **solo «Microsoft Excel»** en `compatApps`, `compatPills`, FAQ, title y dashboard [M8]. Consentimiento de John para usar su Drive: **pendiente**; se pregunta cuando existan los ficheros |
| D17 | **Dos plantillas nuevas, ES y EN a la vez** (John, 24-sep) | Ficheros **independientes**; no son hojas dentro de 01-08. Así no se reescribe la columna de precio de 71 hojas ni se enlazan libros separados, algo que no funciona bien entre ficheros ni en Google Sheets. **Primero en español** (Kit de Escandallos Pro **v2.1**, §2.0) y el EN los recibe por el mismo pipeline de duplicado. `12-test-de-rendimiento.xlsx` → `12-yield-test.xlsx` · `13-lista-precios-ingredientes.xlsx` → `13-ingredient-price-list.xlsx`. El kit pasa de 11 a **13 plantillas** + 2 bonus (landing, hub, dashboard y SEO: «13 Food Cost Templates»). Precio **sin cambio**: 12 € y $19. La subida a $24 del research queda para cuando haya reseñas EN |
| D18 | Licencia (John, 24-sep; precisada por R2-17) | **Un negocio (con todos sus locales) por compra.** Se puede usar con tus clientes, pero **sin entregarles copias**: cada negocio compra la suya. Escuelas: licencia de aula en info@aichef.pro. Va en una FAQ de la landing EN, en una línea de Instrucciones de los xlsx EN y en las **condiciones de compra EN** (§5.4). En ES no se añade (no se ha pedido). Aviso en TIENDA: las FAQ de licencia de los kits hermanos («todos tus locales», «ideal para consultores») se revisan contra D18 al duplicarlos |
| D19 | Ventas netas [research 8b-A C1] | «Net sales» = **sin impuesto y sin service charge ni propinas** en los textos del 10, el 11, el BONUS, el PDF e Instrucciones. UK: Employment (Allocation of Tips) Act 2023 y VAT Notice 709/1. US: DOL Fact Sheet #15 |
| D20 | De la factura al precio por unidad [8b-B §1.6] | Bloque de Instrucciones en 01-08, «From invoice to price per unit»: catch weight → `lb`/`kg`; caja de la lista → precio de la caja tal cual; caja fuera de la lista → `lb`/`each` con precio ÷ contenido (*pack/size*); lata #10 por peso neto; aceite de freidora al Q-factor; precios sin impuesto recuperable. Más textos breves: yield propio, cooking loss, escalado, subrecetas y pesar los secos. En `Trim Loss Factors`, A2 remite al **12 Yield Test** y al USDA Food Buying Guide |

## 2. Entregables (F2)

### 2.0 Primero el español: Kit de Escandallos Pro v2.1 (D17)

Dos libros nuevos con las convenciones del kit v2.0:
- el generador **importa los helpers** de `kit-escandallos-v2_0/motor.py`;
- celdas de entrada en verde `E8F5E9` y calculadas sin relleno;
- todas las divisiones con `IFERROR`, y solo funciones que pycel evalúa (nada de `COUNTA`: se usa `COUNTIF(rango,"?*")`) [R2-09];
- protección de hoja sin contraseña, con las entradas desbloqueadas;
- A4, pie, metadatos y fechas `numFmtId 14`;
- `inject_cache.py` al final;
- verificación con pycel.

Los textos los escriben subagentes Anthropic (regla 1bis). El generador vive en
`scripts/productos-digitales/kit-escandallos-v2_1/`.

**`12-test-de-rendimiento.xlsx`** (pestañas `Instrucciones`, `Test de despiece`, `Test de cocción`)

*`Test de despiece`* (*butcher's yield test*):
- **Cabecera** (entradas): producto, proveedor, fecha, peso de compra (AP), precio por kg AP, coste AP y una celda verde **«unidades de porción por unidad de peso»** (ES 1000 g/kg; EN 16 oz/lb). Ninguna fórmula lleva constantes de unidad [R2T-07].
- **Tabla** de hasta 12 componentes: pieza; tipo con DV `Útil,Subproducto,Desecho` (EN `Usable,By-product,Trim (no value)`); peso; valor de mercado por kg (solo subproductos); valor; % del AP. Más una fila calculada **«pérdida de corte» = AP − Σ componentes** [R2T-06].
- **Resultado:**
  - peso útil;
  - valor de subproductos;
  - coste neto útil = coste AP − valor de subproductos;
  - rendimiento bruto %, informativo;
  - **coste por kg útil**;
  - **factor de coste** = coste por kg útil ÷ precio AP;
  - **la ÚNICA cifra que se lleva a la ficha**: «**Merma % para tu escandallo**» = 1 − precio AP ÷ coste por kg útil (= 1 − 1/factor). Incluye el crédito de los subproductos, así que la ficha, con el precio AP, da el mismo coste que el test [R2T-06, R2-02];
  - porción estándar y coste por porción.

*`Test de cocción`* (*cooking loss test*):
- Entradas: peso crudo útil, coste crudo (a mano o el coste por kg útil del despiece) y peso cocinado.
- Resultado: pérdida por cocción %, coste por kg cocinado, porción cocinada y coste por porción. La merma combinada para la ficha es 1 − (1 − merma de despiece) × (1 − pérdida por cocción).

*Ejemplo* [R2-13]:
- El despiece usa **la misma pieza que compra la 01**: el solomillo entero.
- La merma del solomillo en la fila 5 de la 01 **pasa a ser la del test**, en ES v2.1 y en EN, con nota en el changelog.
- Rendimientos típicos con fuente o `[estimado]` (medir en F2).
- La cocción usa una elaboración del kit, la hamburguesa del 08.
- «Duplica la pestaña para otro test.»

**`13-lista-precios-ingredientes.xlsx`** (pestañas `Instrucciones`, `Lista de precios`)

- **Resumen arriba:** nº de ingredientes (con `COUNTIF "?*"`), nº de alertas y mayor subida.
- **Tabla:** tantas filas como ingredientes distintos de las recetas del kit, más 30 vacías [R2-10].
- **Columnas:** ingrediente · categoría · proveedor · formato de compra (texto de la factura) · contenido del formato · unidad base (DV; se recomiendan kg/L/ud, y en EN lb/L/each) · **precio del formato** · **precio por unidad base** (4 decimales) · **precio anterior por unidad base** · **variación %** sobre el precio por unidad base · estado OK/ALERTA (CF) · fecha de la última factura · notas [R2T-08, R2-09].
- **Umbral de alerta** en celda verde, 5 %.
- **Precarga:** los ingredientes de ejemplo con su precio, las **fechas vacías** y el precio anterior vacío, salvo 1-2 filas de demostración marcadas «ilustrativo» en la propia fila (`[estimado]` en los datos) [R2-10].
- **Protección** con ordenar y autofiltro permitidos, y autofiltro definido [R2T-08].
- **Honestidad:** las fichas **no se alimentan solas** de la lista, porque cada plantilla es un libro independiente. Instrucciones y landing: «copia el precio por unidad base a la ficha, con esa unidad como unidad de compra, usando **Pegado especial → Valores**» (Excel Ctrl+Alt+V → V; Sheets Ctrl+Shift+V). Un pegado normal arrastra la fórmula [R2-09].
- Sin comparador de proveedores: es del Kit de Inventario.
- En EN, el 13 se **genera desde las recetas EN finales** (`mercado_en.json`), no traduciendo el ES, porque cambian ingredientes, unidades y precios [R2-10].

**Arreglos del ES que la v2.1 incluye:**
- **Rango de `Conversiones` con filas libres** en las 453 fórmulas de 01-08 (`$A$5:$B${4+n+30}`), más el área de impresión ampliada: hoy lo que se escribe debajo de la tabla no se encuentra [R2T-15].
- **Línea «Versión 2.1»** y `subject` «Kit de Escandallos Pro · v2.1» en los **14** libros; hoy dicen «v1.1» [R2T-16, R2-05].
- `kit-escandallos` entra en `EXCLUIDOS` de `postprocess-transversal.py` en el mismo PR, para que un `all` no la devuelva a v1.1.

**Revisión:** una ronda adversarial de los libros 12 y 13 ES, con lente de chef o gerente español y lente técnica, antes
del PR. Cuenta dentro del tope de 2 rondas por artefacto [R2-16].

**Publicación del ES v2.1**, en un PR propio **fusionado ANTES de la F2-EN**, porque el EN parte de esos ficheros
[R2T-24]. La lista sale de un grep [R2T-10, R2-04]:
- los ficheros en `dl/kit-escandallos/`;
- claves en `get-download-urls.ts`;
- 2 tarjetas y la cabecera del dashboard ES («Tus 13 plantillas + 2 bonus»);
- grid, FAQ y textos «11» → «13» de la landing ES;
- tarjeta del kit en los **7 hubs** (ES y las 6 copias internacionales, que enlazan a la landing ES);
- `emailBody` de `verify-purchase.ts` y `resend-access.ts`;
- la FAQ de venta cruzada de la Guía Food Cost;
- `productos-changelog.ts` 2.1;
- broadcast ES en la cola de 5 días.

**Gates del ES v2.1:**
- `censo-entregables.py --only kit-escandallos --fail`;
- `gate-flujo-postpago.py --base <preview>` (su sección B comprueba los `/dl/` en vivo);
- pycel;
- **grep a cero** de «11 (plantillas|templates|modèles|Vorlagen|template|modelos|sjablonen)» ligado al kit en `src`, `astro-site/src` y `netlify`;
- `tienda-gate --es-identico` con una opción nueva **`--esperadas /kit-escandallos`**, que para esa ruta imprime el diff de texto en vez de fallar [R2T-11, R2-16];
- test del rango libre de `Conversiones` en ES.

### 2.1 Fuente y método

- **Fuente = los xlsx publicados** en `astro-site/public/dl/kit-escandallos/`: los 12 de la v2.0 (`ed45f35`) **+ los
  2 nuevos de la v2.1** (§2.0), y el `bono-guia-food-cost-30-dias.md`. **No** se usa `scripts/generate-escandallos.py`: es la v1.0 (inventario §2).
- Salida: `astro-site/public/dl/recipe-costing-kit/` (14 xlsx + PDF). **Los ficheros ES no se tocan.**
- Código en `scripts/productos-digitales/recipe-costing-kit/`:
  - `extraer_textos.py` → `textos_es.json` (cadenas con contexto) **y `censo_es.json`**: fechas, literales, DV, CF, hojas y áreas de impresión por libro, generado del ES v2.1 publicado. Los gates comparan contra ese censo, no contra recuentos fijos de la v2.0 [R2T-17, R2-11].
  - `mapas.py`: hojas, claves-dato, literales y la `Conversions` generada (D7).
  - `textos_en.json`: traducción cadena a cadena por subagentes Anthropic; nada de `bridge.py` (regla 1bis).
  - `mercado_en.json`: sobrescrituras de celda con fuente o `[estimado]`, más **la lista cerrada de «textos con cifra derivada»** [M5]. Son las celdas de Instrucciones y notas que citan cifras que la versión EN cambia: comisión, tamaños de botella y lata, IVA, precios, ratio de camareros, «~21 %», «unos 3 puntos». Se **reescriben** con la cifra recalculada sobre la hoja EN final; no se traducen literalmente.
  - `aplicar_en.py`: copia → hojas → claves → `Conversions` → textos → literales → formatos → mercado → metadatos (los 6 campos de docProps, incluido `category` «AI Chef Pro · Digital products» [T9]), pie y papel → `inject_cache.py` **al final**. Idempotente y con `--dry-run` sobre el scratchpad.
- En el mismo commit que publica `dl/recipe-costing-kit/`, `recipe-costing-kit` entra en `EXCLUIDOS` de
  `postprocess-transversal.py`. Si no, un `all` le forzaría A4 y metadatos en español [T12].
- Ejecución en el **Mac, en serie, con el vigilante**. **Excepción registrada** a la política de 3 fases (F2 de un M al
  VPS): es trabajo de kit xlsx, el mismo caso que la decisión del 20-sep para los kits réplica (openpyxl no calienta y
  el ping-pong git con el VPS cuesta más). Además, el venv del VPS no tiene openpyxl (medido el 24-sep) [R2T-24].
- **Antes del gate 7 de la F2**, `censo-entregables.py` acepta Letter (`paperSize 1`) en las carpetas de
  `productos-en/**` [R2T-24, R2-15].

### 2.2 Renombrado de hojas

Con el mapa se reescribe, en el mismo paso:
- las 849 fórmulas `Hoja!` / `'Hoja'!`;
- las 28 DV `Mermas!…`;
- la CF de 03 `Rotación Semanal`;
- el XML de los 2 gráficos;
- las áreas de impresión (59 hojas; las de Instrucciones no tienen);
- **todos los textos que citan pestañas**: Instrucciones, notas A2/A18 del 04, `Presupuesto!B3/B6` del 06, `Evolución!A2/A6` del 09 y mensajes de error de las DV [T14].

Nombres ≤ 31 caracteres, sin `[]:*?/\`.

**Gate:**
- ninguna fórmula, DV, CF, gráfico ni área de impresión cita una hoja inexistente;
- todo nombre entre comillas dobles rectas (la forma única EN, D9) en cualquier texto o mensaje de DV existe en `wb.sheetnames` del libro, salvo una lista blanca. Un tramo entre comillas simples solo cuenta si coincide con una pestaña, por los apóstrofos del inglés [R2T-18].

### 2.3 Claves-dato

El mismo mapa se aplica **a la vez** en la tabla (`Trim Loss Factors`, `Conversions`), en las listas de las DV y en las
filas de ejemplo.
- Categorías: research §1.4.
- Unidades: D7 (`ud` → each, `docena` → dozen, `manojo` → bunch, `sobre` → packet, `lata` → can, `botella` → bottle).
- Motivos del BONUS: traducidos.

**Gate:**
1. Cero claves duplicadas en `Conversions`.
2. Las dos unidades de cada clave están en la lista de la DV.
3. Resuelven [R2T-02, R2-06]:
   - toda pareja base↔base de la misma dimensión;
   - cada pack a su identidad, sus subunidades y las unidades base de su dimensión (salvo las excluidas);
   - `can`/`bottle` a sus 6 destinos.

   Ninguna clave tiene un pack como destino, salvo la identidad.
4. Todas las claves de un envase salen de su única celda de tamaño.
5. Toda fila de ejemplo resuelve su factor (≠ «?») y su categoría (≠ «»).
6. Escribir una pareja nueva en la primera fila libre de `Conversions` la resuelve [T3].

### 2.4 Literales de fórmula

- `"revisa merma"` → `"check trim loss"` (453 celdas).
- `"revisa unidades"` → `"check units"` (453).
- `"ALERTA"` → `"ALERT"`: 29 celdas **y** las 2 reglas CF que colorean por esa cadena, más la columna de estado, el `COUNTIF` y la CF del 13.
- Libro 12: los literales de `SUMIF` y de la DV `"Útil"`, `"Subproducto"`, `"Desecho"` → `"Usable"`, `"By-product"`, `"Trim (no value)"` [R2T-17].
- Sin cambios: `"OK"`, `"?"`, `"→"`, `"✓"`, `"?*"`, `">0"`.

### 2.5 Adaptación de mercado por fichero

| Fichero EN | Qué se adapta además del texto |
|---|---|
| 01 standard recipe cost card | Ingredientes en lb/oz/fl oz con precio por unidad de compra US (el solomillo en **catch weight**, `lb`); filas de impuesto (D6), GP (D8) y Q-factor 10 %. Instrucciones con el bloque D20 (común a 01-08) |
| 02 tasting menu | Igual que 01 en los 9 pases; el food cost objetivo único de `Summary` se mantiene |
| 03 prix fixe lunch menu | Extras [M19]: «Bread & butter» con valor, «Drink (if included)» y «Coffee (if included)» **a 0** por defecto, con nota. Food cost objetivo 33 %: se revisa contra D12 (casual 28-32 %) y se justifica en `mercado_en.json` |
| 04 cocktails & drinks | **E3:** `Bottle Sizes!B` en **ml** (750 / 1000 / 1750; en EE. UU. el formato legal de destilado es métrico) y `D5:D16 = IFERROR(ROUND(C*1000/B,4),"")` = «Price per liter». Las recetas compran en `L` y usan `fl oz` (clave `L→fl oz` = 33,814), con pour estándar US de **1.5 fl oz** (NIAAA). Vino 750 ml; la lata va por `can` en `Conversions`, no en esta hoja. Nota UK: 25/35 ml y 70 cl. «Spillage & ice allowance» 5 % [T2, M1]. El vino de copeo de la fila 11 pasa a 750 ml y en las filas vacías **solo se precarga el barril de 1/6 bbl** [R2T-19, R2-18]. Instrucciones con la tabla de medidas (US 1.5 / 5 / 12 fl oz; UK 25/35 ml, 125/175 ml y ⅓, ½ y ⅔ de pinta), el pour cost por categoría (destilados 18-20 %, barril ≈ 20 %, botella ≈ 25 %, vino más alto) y el impuesto de bebidas que paga el bar (p. ej. Texas 6,7 %) antes del pour cost [8b-A C5, 8b-B §2.4] |
| 05 pastry & bakery | Rendimiento en unidades (se mantiene). **La pastelería de EE. UU. formula en gramos** [8b-A C4]: los secos y las grasas, en `g`; la leche, en `ml` o `fl oz`; los huevos, en `each` [R2T-19, R2-18]. Ejemplos con el precio de la factura tal cual: harina `50 lb bag`, mantequilla `36x1 lb case`, leche `4x1 gal case`, huevos `15 dz case` [8b-B §1.7]. Mermas de obrador del ES; Q-factor sin «energía del horno» |
| 06 catering & events | Recepción por invitado. En `Event Quote` [8b-A C2, M20]: **1 camarero cada 25 invitados** en recepción (tabla de ratios en Instrucciones: emplatado 1:10-12, buffet 1:20); **camarero $25/h** (punto medio entre el coste W-2, OEWS $17 + 7,65 % FICA = $18,30, y la tarifa de agencia de $30; `[estimado]`) y **jefe de sala $35/h** (proporción del ES 22/16), con «replace with your own rates» [R2-21]; **rentals $3,50/invitado**; **mínimo $1.000**. `Presupuesto!C25` se rotula **«Markup on services (%)»**, uso interno, 20 %, con la fórmula intacta: **no es un service charge** [R2T-04, R2-01]. En `Event Checklist`: food handler cards / food manager certification, seguro, permisos y «Allergen matrix (US: 9 major · UK/EU: 14)». **`Client Proposal`** [M11]: «Price per guest», «TOTAL», A15 «Quote valid for 30 days. Applicable sales tax is added to the final invoice…», e Instrucciones UK/AU para cambiar a «Prices include VAT/GST». **Service charge opcional:** el usuario lo escribe en la fila libre B9 (concepto, comensales, importe). Instrucciones: en US, si es obligatorio es ingreso del negocio y puede tributar (DOL FS#15); en UK va íntegro al personal (Tips Act 2023); A15 solo lo menciona si esa línea existe. `C35` = food cost sobre el total facturado **sin** service charge (D19) |
| 07 café & brunch | Mismas 4 recetas en unidades US, con alguna fila en formato de caja [8b-B §1.7] |
| 08 food truck | `Break-Even` con costes diarios US: **$45 + $25 + $30 + $300 + $50 + $15 = $465/día** (commissary/parking, permisos y seguro, propano/generador, 2 personas con cargas [M20], amortización, limpieza), con la cuenta de cada línea `[estimado]` [8b-A §4.3] |
| 09 food waste tracker | 16 familias con objetivos, compras de ejemplo en USD, fecha D13, «Week 2…12», objetivo global 4 %. Aviso: «trim loss goes in the recipe cost card, not in the waste log» |
| 10 menu price calculator | Filas D12; ventas netas D19; «DoorDash, Uber Eats or Grubhub (UK: Deliveroo, Just Eat)»; impuesto D6. El «~21 %» se recalcula con la comisión del 25 % (≈ 22,5 %) [M5] |
| 11 monthly food cost dashboard | Meses en inglés (son las categorías del gráfico), año como celda editable, cabecera «Period (month or week)», `B19` «TOTAL (12 periods)» y el método semanal en Instrucciones («weekly: use one copy per quarter») [R2-19], «Net purchases (excl. recoverable tax)», ventas netas D19 y «unos 3 puntos» recalculado [M5, 8b-B §2.6] |
| BONUS inventory & waste control | 15 productos: stock (C:E), precio (I) **y** matriz por ración (C5:Q14) convertidos con el **mismo factor**, con cantidades por ración iguales a la AP qty de las recetas EN. Gate: la desviación relativa H/F de cada producto es la misma que en el ES [M10]. 7 motivos (DV) y platos traducidos. «Net purchases (excl. recoverable tax)». Instrucción para el *product mix* del TPV (Toast, Square, Clover, Lightspeed, Epos Now): los platos se escriben **una vez**, cada uno con su receta por ración, y en cada periodo se copian **solo las unidades vendidas en la columna B**, en la fila de su plato. **Nunca** se pega sobre la columna A [8b-A C6, R2T-05] |
| **12 yield test** | Duplicado del ES v2.1 (§2.0): lb/oz (celda de porción = 16), USD, la misma pieza que la 01 EN (*whole beef tenderloin, PSMO*), rendimiento con fuente o `[estimado]`, y «Trim loss % for your cost card» = la merma de la fila 5 de la 01 EN |
| **13 ingredient price list** | Estructura del ES v2.1, **datos generados desde las recetas EN**: unidades base US (recomendadas lb/L/each), formatos de compra de D7 como texto de factura, distribuidores genéricos (sin marcas), USD sin símbolo, umbral 5 % |

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
- `CryptoPayButton.astro` con `lang`: copy, países, enlace a las condiciones EN (§5.4) y la renuncia «where it applies (EU/UK)». El `<script is:inline>` lleva **una rama EN aparte** (8 errores, «Continue to payment»…) y el bloque ES queda **intacto** (las 48 landings ES byte a byte). Además, un grep sobre los `<script>` del HTML EN: cero «Continuar», «inténtalo», «escríbenos», «pasarela» [R2T-12].
- `pages/en/crypto-payment.astro` = copia traducida de `pago-cripto.astro`, fuera del sitemap.
- Si no llega a tiempo, el producto va a `CRYPTO_PRODUCTS_EXCLUDE`.

**Gates que hay que ajustar antes:**
- `miselup-gate.py`: en EN, cero tarjetas.
- `whatsapp-gate.py`: exentos anidados.
- `robots-gate.py`: rutas anidadas.
- `tienda-gate.py`: hreflang que apunte a un 404 en páginas EN aún no vivas, y `--esperadas <ruta>` (§2.0).
- `nombre-gate.py`: `productos-en/**` con `name.en`, y corrido con `--only recipe-costing-kit` (hoy está rojo en 44 productos ES) [T13, R2T-21].

**Hub EN** [R2T-09, R2-04]: la tarjeta pasa a «13 Excel templates», «Preloaded trim-loss (yield) rates», «10 venue types», con el slug de la landing EN, precio vivo y badge D4. Gate: el nº de claves de `get-download-urls` de cada producto casa con el grid de su landing.

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
3. **Cálculo.** Caché con `data_only`; pycel sin `#REF!` ni `#VALUE!` y sin funciones que no evalúe; los 6 checks de §2.3; sensibilidad (cambiar un precio o el impuesto mueve lo que debe).
4. **Ejemplos creíbles [T10, M9].** Por receta, un **precio de carta US de referencia** con fuente o `[estimado]` en `mercado_en.json`. El food cost implícito (coste por ración ÷ ese precio) cae en el rango D12 de su tipo de local; el pour cost de las 4 recetas del 04, entre 18 y 24 %. Si una receta cae fuera, se corrige la **cantidad** o el precio de carta de referencia, **nunca** un precio de ingrediente con fuente. Además, `mercado_en.json` completo (D11).
5. **Formato.** Letter; cero formatos con `€` o `dd/mm`; **toda** celda de fecha con `numFmtId 14` (contada contra `censo_es.json`); línea de versión D14 en todos; `$` solo en texto de Instrucciones y notas (D5).
6. **Coherencia de texto.** Rangos de D12 [M6]; cifras derivadas recalculadas [M5]; nombres de pestaña en textos (§2.2).
7. `censo-entregables.py --only recipe-costing-kit --fail` en 0, con Letter admitido.
7bis. **Libros 12 y 13** (ES v2.1 y EN):
   - pycel sin errores.
   - 12: rendimiento entre 0 y 1 y factor de coste ≥ 1. El coste por ración del 12 = el de la fila 5 de la 01 alimentada con «Merma % para tu escandallo» (tolerancia 0,5 %) [R2-02, R2-13].
   - 13: la alerta salta cuando la variación supera el umbral y no salta cuando no. Para cada ingrediente que está a la vez en el 13 y en una ficha, precio del formato ÷ contenido = precio de la ficha ÷ factor [R2T-08].
   - Unidades base casan con D7.
8. **Revisión adversarial** con tope de 2 rondas: lente de chef o manager de EE. UU. y del Reino Unido, y lente técnica.
9. **Test de Google Sheets**, si John da el consentimiento (D16).

**F3**
- Gates: `tienda-gate.py` (estático y `--base`), `gate-flujo-postpago.py` LIVE, `robots-gate`, `whatsapp-gate`, `miselup-gate`, `datafast-gate`, `nombre-gate`, y los de T11.
- **`audit-payment-links.py`**, más una consulta a Stripe del Price: currency usd, unit_amount 1900 = `product-prices.ts` [T15].
- Gate de anclas D4 y gate de banners y spokes (§3).
- Compra de prueba: email EN, dashboard, **15 descargas** (13 plantillas + BONUS xlsx + PDF) y log `[purchase-validation]` con match en `recipe-costing-kit` [T8, R2T-09].
- `fase8c-libreria-en-gate.py --todos`.

## 5. Pendiente de John (simplificado por John el 24-sep)

John, 24-sep: «vendo desde España; Stripe cobra IVA a quien aplica… no me busques las cinco patas del gato».
Memoria: `feedback_tienda-en-sin-complicar-fiscalidad`.

**Fuera de esta SPEC por decisión de John:**
- registro de VAT del Reino Unido;
- `currency_options` GBP/CAD/AUD;
- comprobación de la moneda de liquidación y `tax_behavior`.

**Stripe:**
- Claude entregó el paquete el 24-sep: nombre «Recipe Costing Kit Pro», descripción en prosa de 254 caracteres, **$19** (si Stripe no deja USD, **17 €**) y redirección a `https://aichef.pro/en/digital-products/recipe-costing-kit/access?session_id={CHECKOUT_SESSION_ID}`.
- John crea el producto y el Payment Link y devuelve el enlace `buy.stripe.com`.
- Claude da de alta `VITE_STRIPE_PAYMENT_LINK_RECIPE_COSTING_KIT` en Netlify y regenera `payment-links.ts` / `product-prices.ts`.
- ⚠️ Si el link sale en EUR: `product-prices.ts` con `eur`, y la landing y el hub EN muestran «€» en lugar de «$» (hay que parametrizarlo en la F3).

**Tareas pendientes que no bloquean el lanzamiento:**
- condiciones de compra EN (`/en/terminos` solo cubre el SaaS);
- `PURCHASE_VALIDATION=strict`;
- test de Google Sheets (necesita su Drive);
- pesar un solomillo real para el ejemplo ES.

## 6. Presupuesto y fases [R2-12, R2T-24]

Gasto medido hasta el cierre de la F1: **≈ 2,8 M** tokens de subagentes (inventario y research 0,72; R1 0,70;
8 bloques 0,67; R2 0,67).

El alcance ya no es el de un M normal:
- es el **primer producto** de la tienda EN, y le toca construir infraestructura que heredarán los siguientes: cripto EN, componentes con `lang`, 6 gates;
- se le suma el **ES v2.1** (D17).

**Decisión (delegada, se informa a John):**
- el **ES v2.1 ocupa la casilla «v2.x ES» de la rotación**, con presupuesto propio de S (≤ 2,5 M);
- el piloto EN sigue en M (≤ 5 M), con un aviso al pasar cada subpresupuesto:

| Fase | Tope |
|---|---|
| F1 (hecha) | 2,8 M |
| F2-ES v2.1 (libros 12 y 13 + revisión + publicación) | 1,2 M (cuenta en la casilla ES) |
| F2-EN (14 xlsx + PDF + gates + 1 ronda) | 1,8 M |
| F3 (capa de producto + infraestructura EN) | 1,2 M |

Si el total del piloto EN, sin el ES v2.1, pasa de 6,5 M (techo + 30 %), se para y se reporta.

- **F2-ES (v2.1):** generador de los 2 libros (opus) + textos (subagentes) → gates → 1 ronda de revisión → PR ES → merge.
- **F2-EN:** `extraer_textos.py` + `mapas.py` (opus) → traducción por grupos (sonnet, 2 a la vez, glosario común primero) → `mercado_en.json` (opus) → `aplicar_en.py` (opus) → gates → revisión.
- **F3:** capa de producto en un PR → Payment Link (John) → merge → compra de prueba → broadcast.

Cada fase cierra con su gate, `commit` + `push` y una línea en el handoff.
