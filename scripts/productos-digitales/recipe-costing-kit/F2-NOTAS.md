# Food Cost Kit Pro — F2-EN · notas de trabajo

> ⚠️ El producto se llamaba «Recipe Costing Kit Pro» hasta el 24-sep por la noche. Las secciones anteriores a
> «Renombrado» conservan los nombres de entonces (ficheros, pestañas 10 y 13, `dl/recipe-costing-kit/`,
> `RECIPE_COSTING_KIT_APPLY`): son historia. Lo vigente está en «Renombrado», al final.

> Sesión Claude Code, 24-sep-2026. SPEC que manda: `SPEC.md` (D1-D20, §2.1-§2.6, §4). Fuente: los 14 xlsx del
> Kit de Escandallos Pro **v2.1 publicados** en `astro-site/public/dl/kit-escandallos/` (HEAD `770aaf1`; última edición de esa carpeta en `960b959`), que
> **no se han tocado**. Todo en serie en el Mac, con `istats` antes de cada script (43,8-52 °C). Sin builds ni
> navegador. Intérprete: `python3` = `/usr/local/bin/python3` 3.7.2 con openpyxl 3.1.3 (el `/usr/bin/python3` 3.9
> no tiene openpyxl).

## Cimientos

### Qué se ha hecho

| Fichero | Qué es | Cómo se regenera |
|---|---|---|
| `mapas.py` | Mapas ES→EN y tabla `Conversions` generada por la regla cerrada de D7. Importable sin efectos. | `python3 mapas.py` (autotest; `--json` vuelca la tabla) |
| `extraer_textos.py` | Lee los 14 xlsx ES (solo lectura) y escribe `textos_es.json` y `censo_es.json`. Importa `mapas`. | `python3 extraer_textos.py [--origen DIR] [--salida DIR]` |
| `textos_es.json` | Todas las cadenas únicas con contexto, tratamiento, grupo y pistas de la SPEC. | generado |
| `censo_es.json` | Censo §2.1 por libro y hoja: lo que contarán los gates. | generado |
| `<scratchpad>/rck-dryrun/conversions_en.json` | Vista previa de la tabla `Conversions` EN (252 filas, fórmulas incluidas). No va al repo. | `mapas.conversions()` |

Orden: `extraer_textos.py` → `mapas.py` (el autotest cruza con `censo_es.json` si existe). Nada traducido: los
textos EN los escriben después subagentes Anthropic por grupos (regla 1bis; nunca `bridge.py`).

### `censo_es.json` (ES v2.1 publicado)

| Medida | Kit | Nota |
|---|---|---|
| Libros · pestañas | 14 · 76 | |
| Celdas de texto · fórmulas | 3.893 · 2.800 | |
| Fórmulas que citan una hoja | **850** | la SPEC §2.2 dice 849 (v2.0); +1 = `03!Rotación Semanal!K3` de la v2.1. Los gates cuentan contra el censo |
| DV | **60** (32 de lista literal, 28 que leen `Mermas!$A$5:$A$25`) | 58 de la v2.0 + la DV «Tipo» del 12 + la de unidades del 13 (`F10:F154`) |
| CF | **69** (ninguna cita otra hoja) | 66 + 1 del 12 + 2 del 13 |
| Gráficos | 2 (09 `Evolución` LineChart, 11 `Dashboard` BarChart), leídos del ZIP con su hoja ancla | openpyxl los borra al guardar |
| Merges · hojas protegidas · áreas de impresión | 631 · 46 · 62 | |
| Celdas de fecha | **240** = 93 `dd/mm/yyyy` (06 `B45:C45`, 09 `B2`, BONUS `A4:A93`) + 147 `numFmtId 14` (12: 2; 13: 145) | cuadra con D13 |
| Celdas con `€` en el formato | 1.811 (todas, también las vacías) | el inventario contaba 1.027 solo con valor; gate 5 = cero en todas |
| Papel | A4 (`paperSize 9`) en todas | |
| VLOOKUP a `Conversiones` | 453, todas sobre `$A$5:$B$67` | |
| Literales de fórmula | `revisa merma` 453 · `revisa unidades` 453 · `ALERTA` 175 · `Subproducto` 12 · `Útil` 1; sin cambio: `?` 906, `→` 453, `OK` 174, `?*` 2, `>0` 2, `✓` 1 | `Desecho` no aparece en fórmulas (sí en la DV y en `B26` del 12) |
| Literales de CF | `?` 28 · `ALERTA` 3 · `OK` 3 · `✓` 1 | |

Por hoja guarda además: dimensión, fórmulas y su huella sha1, refs a hojas, literales con sus celdas, DV y CF
completas (sqref, tipo, `errorStyle`, `showDropDown`, mensajes), merges, paneles, protección, autofiltro, área y
títulos de impresión, papel y ajuste, cabeceras y pies, formatos, celdas verdes y desbloqueadas, fechas con su
`numFmtId`; por libro, docProps, `sha256`, categorías de `Mermas` y las 33 parejas ES de `Conversiones`.

### `textos_es.json`

- **1.118 cadenas únicas · 4.565 apariciones.** Excluidas, con su recuento en `meta.excluidas`: 3 sin letras (`#`,
  `✓`, `—`) y las invariables `AI Chef Pro` (28) y `N/A` (1). Total contrastado: 4.597 apariciones.
- Por aparición: libro, hoja, celda (o sqref de la DV, campo de cabecera/pie, parte del gráfico, campo de
  docProps) y tipo de lugar (`celda`, `hoja`, `dv-error`, `dv-error-titulo`, `dv-item`, `grafico-titulo`,
  `cabecera-pie`, `docprops`).
- **Tratamiento** (la cadena toma el más fuerte de sus apariciones):

  | Tratamiento | Cadenas | Qué es |
  |---|---|---|
  | `traducir` | **861** (8.799 palabras) | texto libre → subagentes |
  | `regenerar` | 171 | tabla `Conversiones` (E1), lista de la DV de unidades (E5), filas de datos del 13 (R2-10), línea de versión y subject/URL de docProps (D14) |
  | `mapa-hoja` | 49 | 49 nombres de pestaña; 19 de ellos también son celdas que citan la pestaña (02 `Resumen!B5:B13`, 03 `Resumen Menú!B5:B7` y `Rotación Semanal!F4`, 04 `Formatos de Compra!E5:E10`, 08 `Punto de Equilibrio!A16:A18` y los A1 de las pestañas de cóctel y del pulled pork) |
  | `mapa-clave` | 37 | 21 categorías, 6 unidades de celda, 7 motivos y 3 tipos del 12 |

- Campos de ayuda: `en_mapa` (valor EN obligatorio de las cadenas de `mapa-hoja`/`mapa-clave`), `tratamientos` (129
  cadenas mixtas: nombres de ingrediente que se traducen en las fichas y se regeneran en el 13; ninguna cadena a
  traducir coincide con una clave), `cita_hojas` (94 cadenas
  que citan una pestaña entre comillas, con su nombre EN), `categorias_citadas` (14), `con_cifra` (144 de las que se
  traducen: la cifra se reescribe si cambia en EN, M5) y `pistas` (299 cadenas con el recordatorio de la SPEC que les
  aplica: D5, D6, D8, D9, D13, D14, D19, T9, E2…).

### Grupos de traducción

| Grupo | Cadenas | Palabras | Contenido |
|---|---|---|---|
| `G0-comun` | 105 | 974 | en ≥ 3 libros, rejilla de 01-08, Instrucciones comunes (2 libros de 01-08), pie, copyright, keywords y category. **Primero: fija el glosario** |
| `G01` | 98 | 671 | 01 + 02 + 03 |
| `G02` | 86 | 1.060 | 04 + 05 |
| `G03` | 135 | 949 | 06 |
| `G04` | 132 | 1.134 | 07 + 08 + 09 |
| `G05` | 85 | 919 | 10 + 11 |
| `G06` | 106 | 1.513 | 12 |
| `G07` | 114 | 1.579 | 13 (cabeceras e Instrucciones) + BONUS |
| `GM-mapas` | 257 | 1.035 | **no se traduce**: pestañas y claves (`mapas.py`) y lo regenerado |

Cada cadena va a su grupo por el primer libro en que aparece; las que salen en varios llevan todas sus apariciones.

### `mapas.py`

- **Hojas** (D9 + research §1.3): 49 nombres ES → EN, validados por libro (76 pestañas): ≤ 31 caracteres, sin
  `[]:*?/\`, sin apóstrofos, sin repetidos por libro. `Mermas` → `Trim Loss Factors`; 12 → `Butcher Yield Test` y
  `Cooking Loss Test`; 13 → `Price List`. Helpers `hoja_en()` y `ref_hoja()` (comillas cuando hacen falta).
- **Ficheros**: research §1.2 + D17 (`12-yield-test.xlsx`, `13-ingredient-price-list.xlsx`); PDF
  `BONUS-30-day-food-cost-guide.pdf` (research §1.2).
- **Claves-dato** (§2.3): 21 categorías (research §1.4; 270 caracteres en línea, por eso la DV sigue leyendo la
  hoja), 11 unidades (`ud→each`, `docena→dozen`, `manojo→bunch`, `sobre→packet`, `lata→can`, `botella→bottle`),
  7 motivos y los 3 tipos del 12. **Literales** (§2.4) y conjunto sin cambio.
- **Lista D7**: 34 unidades, **248 caracteres** (250 con las comillas) ≤ 255.
- **`Conversions`**: **n = 252 claves** = 141 base↔base (masa 16, volumen 121, recuento 4) + 95 de los 13 formatos
  + 12 de `bottle`/`can` + 4 de `bunch`/`packet`. **Rango VLOOKUP `$A$5:$B$286`** (4 + 252 + 30) y área de
  impresión `$A$1:$J$286`. Factores exactos (NIST HB44 App. C) con `Fraction`; columna C en inglés generada
  («1 × 50 lb bag = 800 oz»).
- **Autotest** (`python3 mapas.py`): lista ≤ 255 y sin `case`; cero claves duplicadas (sin distinguir mayúsculas,
  como VLOOKUP); cero peso↔volumen; toda unidad de clave está en la lista y toda unidad de la lista tiene identidad;
  base↔base completo; cada pack con identidad, subunidades y destinos base, sin cup/tbsp/tsp en barriles y cajas de
  bebida y sin claves de más; ningún pack como destino salvo la identidad; `can`/`bottle` con sus 6 destinos y
  fórmulas sobre su única celda de tamaño (gate 4); valor evaluado = factor en las 252 filas; 25 factores de
  control. Con `censo_es.json` cruza: pestañas por libro, literales de fórmula y de CF, listas de DV, hojas citadas
  y categorías. **Probado en negativo**: 17 defectos inyectados (duplicado, duplicado por mayúsculas, peso↔volumen,
  unidad fuera de lista, pack como destino, cup en barril, bottle→cup, base↔base que falta, envase que no sale de su
  celda, valor ≠ factor, hoja sin mapa, > 31 caracteres, apóstrofo, repetida en un libro, lista > 255, literal nuevo
  y pestaña nueva en el censo): **17/17 detectados**. Un fallo: el autotest se caía con `KeyError` ante una unidad
  desconocida en vez de reportarla; arreglado.

### Decisiones tomadas aquí (para revisar en la ronda de la F2)

1. **`50 L keg` = 11 galones imperiales = 50,00699 L**, como 8b-B §1.4/§1.6: da **88 imp pt exactas**. El nombre dice
   50 L; la diferencia es del 0,014 %.
2. **`can→ml` = 355** (D7), así que `can→fl oz` = 12,004 y no 12; `24x12 fl oz case` usa 288 fl oz exactas. Diferencia
   del 0,03 %.
3. Las filas de envase son `=IFERROR(B<tamaño>/k,"?")`: si alguien escribe texto en la celda de tamaño, la ficha
   dice «check units» en lugar de `#VALUE!`. Celdas de tamaño con `fila0 = 5`: **`B147` (bottle, 750)** y **`B153`
   (can, 355)**. Sugerencia para `aplicar_en.py`: pintarlas en verde; son lo único que un británico tiene que editar.
4. `4x1 gal case` (leche) **sí** lleva cup/tbsp/tsp: D7 solo las excluye de barriles y cajas de bebida.
5. Subunidades: `36x1 lb case→each` 36, `40x250 g case→each` 40, `4x1 gal case→each` 4, `12x750 ml case→bottle/each`
   12, `24x12 fl oz case→can/each` 24. Sin subunidad: `50 lb bag`, `40 lb case`, `16 kg sack` y los barriles.
6. Orden de la tabla: masa, volumen y recuento base; `bottle`, `can`; `bunch`, `packet`; los 13 formatos.
7. El formato `0.###` de `Conversiones!B` del ES enseña «0.001» para `tsp→gal` (el valor es exacto). Lo decide
   `aplicar_en.py` al escribir la tabla (E1).
8. Las filas de datos del 13 (`A10:M154`) son `regenerar` (R2-10): no se traducen. Los nombres de ingrediente se
   traducen desde las fichas; 108 cadenas que solo viven en el 13 van a `GM-mapas`.
9. docProps: `subject` y `description` se regeneran (D14); `title`, `keywords` y `category` se traducen.
10. `Gin Tonic Premium` → `Gin & Tonic` (research §1.3): la pestaña y el A1 pierden «Premium».

### Pendiente (fuera de estos cimientos)

`textos_en.json` (traducción por grupos, `G0-comun` primero), `mercado_en.json`, `aplicar_en.py` (incluida la E3
de `Bottle Sizes` en ml) y los gates de §4.

## PDF (bono, SPEC §2.6)

### Qué se ha hecho

| Fichero | Qué es | Cómo se regenera |
|---|---|---|
| `bonus-guide-food-cost-30-days.md` | La guía EN, **adaptada** (no traducida) desde `kit-escandallos-v2_0/bono-guia-food-cost-30-dias.md`. Redactada por subagente Anthropic, sin `bridge.py`. ≈ 8.300 palabras, 11 secciones, 21 tablas | a mano |
| `bono_guide_en.py` | Copia parametrizada de `bono_guia.py` (el ES no se toca): `PARAMS` con cabecera «AI Chef Pro · Recipe Costing Kit Pro», pie «Page {n}», título «Control Your Food Cost in 30 Days», marcador «A bonus guide from Recipe Costing Kit Pro», **US Letter** y metadatos EN (autor, asunto, creador, keywords). El .docx solo con `--docx` (no es entregable, COM-B18) | `/usr/local/bin/python3 bono_guide_en.py bonus-guide-food-cost-30-days.md <scratchpad>/rck-dryrun/BONUS-30-day-food-cost-guide` |
| `<scratchpad>/rck-dryrun/BONUS-30-day-food-cost-guide.pdf` | Dry-run: **23 páginas Letter** (el ES A4 tiene 17), 70 KB. No va al repo hasta `aplicar_en.py` / F3 | ídem |

Gates del maquetador (abortan con código 3): (1) cero caracteres fuera de WinAnsi tras el mapa (60 emojis/casillas
saneados: ✅ ❌ ⭐ ☐ 🐴 🧩 🐶, − y ─), también en los textos fijos; (2) cero restos de español: signos `¿¡«»€ºª`,
palabras con tilde/eñe fuera de la lista blanca (café, purée, açaí…), funcionales ES y léxico de oficio (IVA,
escandallo, merma, albarán…) y la prohibida «entrée» (D8); (3) tras maquetar se relee el PDF con pypdf: páginas, pie
«Page n» en todas, papel 612×792 pt, título de metadatos y el gate 2 sobre el texto extraído. **`--autotest`:
14/14 defectos inyectados detectados** (€, «», ¿, tilde, eñe, «de», «que», IVA, escandallo, merma, entrée, ≈, CJK,
⅓) y base limpia sin falsos positivos. Aritmética de la guía: **63 comprobaciones, 0 fallos** (script en la sesión).

### Qué se adaptó (SPEC §2.6)

- **Impuesto:** fuera el IVA y el art. 91 LIVA. Semana 1: EE. UU. carta sin impuesto; UK ÷ 1,20 con el aviso «restar
  el 20 % ≠ dividir entre 1,20» (£120 → £100, no £96; £14.520 → £12.100). Compras sin impuesto recuperable.
- **Ventas netas D19** en la introducción (sin impuesto, propinas ni service charge; DOL FS#15, Tips Act 2023 en vigor
  desde el 1-oct-2024, VAT Notice 709/1: service charge obligatorio al tipo general) y en el checklist.
- **Benchmarks D12** exactos, con las etiquetas de la calculadora 10 («Fine Dining»…«Delivery»), en lugar de «España 2026».
- **Semana 1: cómo leer una factura** (pack/size, catch weight, caja de la lista D7 vs. precio ÷ contenido, lata #10
  por peso neto, aceite de freidora al Q-factor, split-case fee) con una factura de ejemplo de 5 líneas.
- **Semana 2:** ficha del tataki en oz/fl oz/each con precio por unidad de compra (suma $6,52 = 28,68 %); tabla de trim
  loss = valores de `Trim Loss Factors` (típica y rango del ES) en lugar de los 8-15 % del .md ES, que contradecían la
  hoja; **plantilla 12** con un test ilustrativo de *strip loin* (22,6 %, factor 1,29) y la pérdida por cocción del
  USDA FBG (0,74); «waste» solo para el desperdicio (09). **Paso 5** con Kasavana & Smith bien aplicado (margen medio
  ponderado $12,90, umbral de popularidad 70 % = 28 uds); el pulpo sale *Star* con 38 % de food cost y la guía lo usa
  para enseñar por qué se miran las dos cifras. Enlace al hub EN, sin venta cruzada a la guía ES.
- **Semana 3: plantilla 13** (precio por unidad base, ALERT > 5 %, Pegado especial → Valores, solo Excel por D16) +
  USDA ERS ago-2026 (vacuno +9,8 %, huevos −30,8 %); «2/10, net 30»; formatos de caja US; el ahorro de comprar pieza
  entera lo decide el yield test.
- **Semana 4:** credit memo en recepción, waste log en el 09, **prime cost < 60-65 %** (NRA: 65 ¢ en limited-service;
  full-service ≈ 65-70 %, cuenta propia declarada como tal).
- **Caso práctico:** mismas cifras en USD (32 % → 35,36 % → 31,8 %; $91.620, $3.141/mes, $470, $37.692/año). Precios
  de plato como **precio neto medio del product mix** (así $20,91 es natural en una carta US). Etiquetas K&S del caso
  cambiadas por el diagnóstico de food cost (el ES llamaba «Caballo» al pulpo sin cumplir el método). El 30,7 % del
  ES es 30,8 % (7,20/23,41 = 30,76 %). La explicación de la semana 1 se corrigió: el stock BAJÓ (6.200 → 5.900).
- **Tabla de economía (§8)** con fuente: NRA (beneficio 2,8/4,0 %, personal 36,5/31,7 %, prime cost LSR 65 ¢),
  **Chipotle 29,6 %, Shake Shack 28,5 %, Darden 30,6 % y Texas Roadhouse 36,4 % (4T-2025) / 35,1 % (año)**, ERS y ONS
  ago-2026, y la regla 30/30/30/10 con su matiz.
- **Further reading** (3 manuales, «no affiliation»), cierre con los 7 ficheros y pestañas EN exactos de `mapas.py`
  (01, 12, 13, 09, 11, 10, BONUS), y la bio anclada traducida sin sumar cifras.

### Verificación de las cadenas cotizadas (fuente primaria, SEC EDGAR, 24-sep)

| Cadena | Dato | Documento |
|---|---|---|
| Chipotle | «Food, beverage and packaging costs for 2025 were 29.6% of total revenue» | 8-K 3-feb-2026, `cmg-20260203xex991.htm` |
| Shake Shack | Food and paper 396.714 = **28,5 %** de Shack sales FY2025 (impreso) | exhibit 99.1 `shak-20260226_exhibit991.htm` |
| Darden | Food and beverage 4.038,8 / Sales 13.210,9 M$ = **30,57 %** FY2026 (calculado; FY2025 30,28 %) | 8-K 25-jun-2026, `exhibit991-q4fy26.htm` |
| Texas Roadhouse | **36,4 %** en el 4T-2025 (33,5 % el 4T-2024), impreso; año 2.049.687 / 5.847.234 = **35,05 %** (calculado); «commodity inflation of 9.5%» | 8-K 19-feb-2026, `txrh-20260218xex99d1.htm` |

Las tres confirman el research (8b-A §4.1). Prime cost que sale de esas cifras (no se publica en la guía): Chipotle
54,7 %, Shake Shack 54,4 %, Darden 62,2 %, Texas Roadhouse 68,3 %.

### Pendiente / [estimado]

- Precios del ejemplo del PDF (factura, inventarios, ficha del tataki, test del *strip loin*): **ilustrativos**,
  plausibles contra BLS/USDA pero sin fuente fila a fila; el PDF no los presenta como referencia de mercado. No
  entran en `mercado_en.json` (D11 es de los xlsx).
- La tabla de trim loss del PDF copia la típica y el rango de `Mermas` ES; si `mercado_en.json` cambia algún valor
  de `Trim Loss Factors`, hay que regenerar el PDF.
- «Food bought for resale usually carries no sales tax» y el ahorro de 2-3 % por pago al contado: criterio de
  oficio [estimado], redactados como orientación.
- Nº de páginas contra la landing EN (SPEC §2.6): la landing aún no existe (F3). Hoy: **23**.
- Copia a `astro-site/public/dl/recipe-costing-kit/` y clave en `get-download-urls.ts`: con `aplicar_en.py` / F3.

## Mercado (SPEC D5-D7, D10-D12, D19-D20, §2.1, §2.5)

### Qué se ha hecho

| Fichero | Qué es | Cómo se regenera |
|---|---|---|
| `generar_mercado.py` | Datos de mercado EN con sus fuentes y todas las cifras derivadas **calculadas** (nada a mano). Importa `mapas` | `python3 generar_mercado.py` (`--stdout`: solo el resumen) |
| `mercado_en.json` | La salida: catálogo, 156 filas de ficha, precios de carta, Bottle Sizes, 03/06/08/09/10/11, BONUS, libros 12 y 13, 37 textos con cifra derivada, lista blanca de rangos | generado; no se edita |
| `mercado_fuentes_web.json` | Evidencia: 91 listados de WebstaurantStore (título, precio del formato, URL), leídos con curl el 24-sep desde su buscador | a mano (curl) |
| `validar_mercado.py` | Gate: lee los xlsx ES **solo para leer** y lo recalcula todo con `mapas.conversions()` | `python3 validar_mercado.py [--verbose] [--json RUTA]` |

Resultado: **0 fallos** (informe en `<scratchpad>/rck-dryrun/validar_mercado.txt`). Probado en negativo con 10
defectos inyectados (fuente sin razonamiento, fila que falta, precio de carta fuera de D12, merma del 12 ≠ 01, clave
sin Conversions, BONUS descuadrado, rango D12 mal en un texto, precio de catálogo ≠ listado, 13 ≠ ficha, valor del
06): **10/10 detectados**. Un fallo del propio gate: con una fila de la 01 borrada se caía con `KeyError` en vez
de informar; arreglado.

### Fuentes (catálogo de 115 ingredientes, precio por unidad de compra de la ficha)

| Tipo | Nº | Qué |
|---|---|---|
| Distribuidor (WebstaurantStore, URL + fecha) | 80 | precio del formato ÷ contenido; el gate lo recalcula contra el listado |
| BLS Average Price Data (api.bls.gov, ago-2026) | 7 | leche, tomate, lechuga iceberg, plátano, vino de mesa ×2, contramuslo (proxy «chicken legs, bone-in») |
| USDA AMS LM_XB459 (18-sep-2026, texto del PDF) | 2 | solomillo 189A (17,21 $/lb) y picada 81 % (3,33 $/lb); el 184 top butt valora las puntas del 12 |
| Resumen de buscador (fuente secundaria, URL) | 11 | destilados y prosecco, PX, branzino, carrillera, trufa, Serrano (pata Costco) |
| `[derivado]` (fuentes + un parámetro [estimado]) | 11 | huevos en caja de 15 dz, manojos de hierbas, tomate cherry, pepinillos, fruta variada, salsa especial, semillas… |
| `[estimado]` con razonamiento | 4 | vieiras U10, pimiento rojo, fondo de ternera, hielo |

Además `[estimado]`: el barril de 1/6 bbl (110 $), los **precios de carta** de referencia (18: 16 recetas + 2 menús),
06 (camarero 25 $/h, jefe de sala 35 $/h), 08 (465 $/día desglosado), 09 y 11 (compras y ventas USD = ES × 4, mismos %).
Ningún € del ES se ha convertido y ningún precio con fuente se ha tocado para cuadrar un porcentaje (D11).

### Food cost implícito contra D12 (todos dentro)

01 33,1 % (fine dining 30-35) · menú 02 32,5 % (115 $) · menú 03 28,9 % (24 $, casual 28-32) · 04 pour cost 21,9 /
20,2 / 22,4 / 23,8 % · 05 27,6 / 26,7 / 26,1 % · 06 31,1 % · 07 28,4 / 29,0 / 29,5 / 25,9 % · 08 29,7 / 32,3 / 33,9 %.

### Decisiones (para la ronda de revisión)

1. **Correcciones para caer en D12** (cantidad o precio de carta, nunca precio con fuente; cada una documentada en su
   fila con `cambio_cantidad`): G&T ½ botella de tónica; Aperol 1,5 fl oz (pour estándar US); **croissants ×2** (el ES
   hace piezas de ~50 g de masa) con **placas de mantequilla de hojaldrar 82 %** (el mismo producto que la «mantequilla
   seca 82 % MG» del ES); avocado toast 2 rebanadas + ¾ aguacate + 2 huevos (título → «with Poached Eggs»); açaí bowl
   2 packs; eggs Benedict 1 muffin abierto (el ES contaba 2).
2. ⚠️ **Macarons: precio de referencia MAYORISTA (0,95 $/pieza)**. En vitrina (2,50-3 $) el food cost cae al ~9 %: el
   rango 25-35 % de D12 no le sirve a una pieza de mano de obra. Es la única receta con referencia mayorista.
3. Elección de producto en el bar: ron **Flor de Caña 4** (18,99 $) y **Zonin** (11,99 $); con Bacardi el mojito quedaba
   en el 12 % y con La Marca el spritz por encima del 24 %.
4. **Solomillo EN = test US de `datos_ejemplos.json`** (5 lb 9 oz, For Love of the Table) a 17,21 $/lb: merma para la
   ficha **37,4 %** (39,3 % bruta menos puntas y cordón); 7 porciones de 7 oz. La fila 5 de la 01 lleva 0,3739 y cuadra
   con el 12 (12,03 $ la porción). Queda fuera de la tabla «Beef & red meat» (15-25 %): el texto c0022 lo explica.
5. Cocción: 10 smash burgers × 6 oz = 3,75 lb → 2,775 lb (USDA 0,74); porción cocinada **4,44 oz** (2 decimales) para
   que test y ficha 08 den el mismo coste exacto.
6. Sustituciones D10: ahi en porciones (bluefin sin precio), branzino (la lubina salvaje no se encuentra), carrillera
   de cerdo (título del pase → «Pork Cheek Braised in Red Wine»), gamba blanca 16/20 (el «langostino» de EE. UU. es
   otro animal), Serrano en pata (el ejemplo de la SPEC), Manchego-style, puré de maracuyá, patata blanca (Agria).
   Donde cambia el formato de compra cambia la merma, con nota (atún 10 %, vieira 5 %, coliflor 5 %, spring mix 5 %,
   ajo pelado 3 %, gamba 35 %, Serrano en pata 50 %).
7. Menús 02 y 03: los pases no se venden sueltos. «Current menu price» de cada pase = **reparto del precio del menú en
   proporción a su coste** (cada pase enseña el food cost del menú). Objetivo único: 02 **30 %** (ES 25 %, por debajo
   de D12) y 03 **32 %** (ES 33 %). 03: bread & butter 0,33 $, bebida y café a 0 (M19).
8. Un precio por ingrediente: desaparecen las notas «la plantilla 07 lo usa a … (otro proveedor)» del 13. El 13 EN
   tiene **113** ingredientes (ES 115), unidades base lb/L/each (bunch en hierbas), 2 filas de demostración (aceite
   ALERT +10,3 %, solomillo OK +1,8 %) y proveedores genéricos. La bebida compuesta del 06 no entra, como en el ES.
9. BONUS: un factor por producto para stock y ración (6 decimales), así que H/F = ES exacto; solomillo, patata y
   mantequilla del plato 1 = AP qty de la 01 EN (por eso el stock de solomillo sale en 25,4 lb).
10. Pastelería en gramos y ml (también el aceite del carrot cake, 220 g, y el postre del 02); cocina salada en oz,
    fl oz, tsp/tbsp y each. Formatos de caja de D7 usados: 50 lb bag, 36x1 lb case, 15 dz case, 4x1 gal case, 40 lb case.

### Para `aplicar_en.py`

- Las filas de ficha (A-F y H), los títulos sustituidos (`titulo_en`) y los precios de carta mandan sobre `textos_en`
  (los nombres de ingrediente de los grupos G01-G07 quedan como referencia).
- Los 37 textos de `textos_cifra_derivada` sustituyen a su traducción (clave = cadena ES exacta).
- Bottle Sizes: B en ml, D = `IFERROR(ROUND(C*1000/B,4),"")` (E3); la fila 12 lleva el barril.
- 02/03: el objetivo va en la celda del Summary; 03 rellena las tres filas de extras con sus rótulos.

## Montaje y gates (sesión Claude Code, 24-sep)

### Qué se ha hecho

| Fichero | Qué es | Cómo se corre |
|---|---|---|
| `aplicar_en.py` | Monta los 14 xlsx EN desde el ES v2.1 publicado, en el orden de §2.1. Dry-run por defecto; `--real` escribe en `dl/recipe-costing-kit/` y exige `RECIPE_COSTING_KIT_APPLY=1` (**no se ha ejecutado**) | `python3 aplicar_en.py --salida <scratchpad>/rck-dryrun [--mes September] [--json …]` |
| `gates_en.py` | Gates F2 de §4 (1, 2, 3, 4, 5, 6, 7, 7bis) y `--autotest` con 14 defectos inyectados | `python3 gates_en.py --dir <scratchpad>/rck-dryrun [--solo 1,5] [--autotest]` |
| `textos_en_por_celda.json` | Traducción por celda para una cadena ES con dos sentidos («Compras»: Purchasing en 06, Purchases en el BONUS) | la lee `aplicar_en.py` |
| `censo-entregables.py` (cambio) | `PRODUCTOS_LETTER = {'recipe-costing-kit'}` y `--letter` para una ruta de carpeta: en productos EN se exige US Letter (paperSize 1) y «Instructions» cuenta como hoja de texto. El ES sigue exigiendo A4 (regresión: `--only kit-escandallos --fail` → 0 defectos) | `--only <carpeta>/ --letter --fail` |

Sin `--dir`/`--salida`, las dos herramientas usan `$CLAUDE_SCRATCHPAD/rck-dryrun` o `.work/recipe-costing-kit/rck-dryrun` (ninguna ruta de sesión en el código: el repo es público). `istats` antes de cada libro, cada `inject_cache` y cada gate. Los ES de `dl/kit-escandallos/` no se han tocado (`git status` limpio en `astro-site/`).

### Montaje (dry-run, 46 s)

- **14 xlsx + PDF**. Conversions **n = 252** → VLOOKUP y área `$A$5:$B$286` (E1/E2); celdas de tamaño **B147** (bottle, 750) y **B153** (can, 355) en verde.
- 1.940 fórmulas reescritas: **918 referencias de hoja** (fórmulas, DV y CF) y **1.097 literales** (453 «check trim loss», 453 «check units», 175 + 3 CF «ALERT», 12 «By-product», 1 «Usable»); 29 DV de unidades sustituidas por la lista D7 (E5) y 30 DV más (categorías, tipos del 12, motivos).
- 2.400 textos traducidos, 4.206 celdas de mercado, 512 filas de Instructions extra, **240 fechas** a numFmtId 14, 76 hojas en Letter con pie EN, docProps EN y línea «Version 2.1 · September 2026 · …».
- Gráficos de 09 y 11: openpyxl 3.1.3 **sí los conserva** pero pierde su `<c:style>`; se reponen desde el XML del ES con las referencias y el título en inglés (drawings idénticos al ES).
- **Idempotencia: 0 diferencias** entre dos construcciones. `inject_cache`: 2.848 fórmulas, `fallos_pycel=0` en los 14.

### Gates (todos en verde)

| Gate | Resultado |
|---|---|
| 1 paridad | 2.800 fórmulas: 2.788 idénticas salvo mapas + 12 E3 (`*1000/B`); 453 VLOOKUP a `$B$286`; 60 DV (29 E5), 69 CF, 631 merges, 5.936 celdas desbloqueadas, protección, paneles, áreas, títulos y ajuste iguales; 2 gráficos con series y ancla iguales |
| 2 restos | 0 «€», 0 no latinos, 0 español en 7.874 valores, 5.030 formatos, 53 numFmt de styles.xml, 76 hojas, 152 DV, 76 pies, 98 docProps y 2 gráficos. «$» (51) y «£» (9) solo como importe en texto |
| 3 cálculo | 2.848 fórmulas con caché (1.639 vacías legítimas, 34 #N/A buscados de los gráficos), 0 errores; los 6 checks de §2.3 en las 8 Conversions y 156 filas de ejemplo; sensibilidad (precio +10 %, doble cantidad, impuesto 20 %) y pareja nueva en las filas 257 y 286 → resuelve |
| 4 creíbles | `validar_mercado.py` 0 fallos; food cost del xlsx dentro de D12 en las 16 recetas y los 2 menús (8 pases) (01 33,1 · pour cost 20,2-23,8 · 05 26,1-27,6 · 06 31,1 · 07 25,9-29,5 · 08 29,7-33,9 · menú 02 32,5 · menú 03 28,9 %) |
| 5 formato | 76/76 Letter y pie EN; 240/240 fechas del censo con numFmtId 14 (y ninguna otra celda con el 14); versión D14 en los 14; docProps (subject, description, category, creator) |
| 6 texto | 6 rangos D12 junto a su etiqueta correctos + 3 de lista blanca; calculadora 10 = D12; 51 cifras derivadas en su celda; 405 citas entre comillas (110 pestañas, 110 rótulos, 177 de otro libro nombrado, 8 de lista blanca); 16 citas de B147/B153 correctas; cabeceras D9 en las 8 «Trim Loss Factors» |
| 7 censo | `censo-entregables.py --only rck-dryrun/ --letter --fail`: 15 ficheros, 0 defectos |
| 7bis 12/13 | rendimiento 0,6067, factor 1,5973, merma 0,3739 = 01!H5, coste por porción 12,0267 vs 01!J5 12,0258; cocción 1,2488 = 08!J5; 13: 113 ingredientes, 1 ALERT y 1 OK, la alerta salta con +10 % y no con +2 % (pycel), 155 filas de ficha = 13, unidades en D7 |

`--autotest`: **14/14 defectos detectados** (hoja citada inexistente, DV sin E5, español, €, CJK, clave duplicada por mayúsculas, cantidad fuera de D12, A4, fecha con formato propio, sin línea de versión, pestaña entre comillas simples, rango D12 falso, 13 ≠ ficha, porción del 12 ≠ 01).

### Arreglos hechos al iterar (en datos o código, nunca en el xlsx)

1. `generar_mercado.py`: «from the 15 dz case **case**» (texto del 13) → regenerado `mercado_en.json` (único cambio) y `validar_mercado.py` en verde.
2. `textos_en/G07`: el 13 decía que las filas demo llevan «"Illustrative"» en Notes, pero sus notas dicen «Sample data:» → corregido.
3. `textos_en/G03`: «Client Proposal» D7/B13 decían «(tax incl.)» contra A15 («sales tax is added to the final invoice», SPEC §2.5) → «Price per guest» y «TOTAL».
4. `textos_en/G0-comun`: cabeceras de «Trim Loss Factors» a las de D9 («Typical / Min / Max trim loss %»); el gate 6 las vigila.
5. `textos_en/G06`: «Cutting Loss» → «Cutting loss» (mismo estilo que el resto de rótulos).
6. BONUS «Inventory» D4: «Purchasing» → «Purchases» por celda (`textos_en_por_celda.json`).
7. Primeras versiones de los gates que no mordían: el 6 cortaba la frase en «:» y no reconocía ningún rango D12 («for catering: 28-35%»); la lista blanca de rangos venía como cadenas compuestas («2-3% · 3-5%…»). Arreglados y probados con el autotest.

### Decisiones (para la ronda de revisión)

1. `Conversions!B` en formato `General` (el `0.###` del ES enseñaba «0.001» para tsp→gal); columna C ensanchada a la nota más larga. Es la tabla regenerada (E1).
2. 12 «Cooking Loss Test»!C12 a `#,##0.00`: la porción cocinada en oz (4.44) con el `#,##0` de los gramos se vería «4». Solo formato de una celda de entrada.
3. 13: se conserva la tabla del ES (A10:M154, 145 filas) por paridad: 113 ingredientes + **32** filas libres (la SPEC pide ≥ 30).
4. Citas entre comillas de pestañas o rótulos de **otro** libro («Used in: 01 "Recipe Cost Card"», «the "Inventory" tab in the BONUS file»): el gate 6 las admite solo si el texto nombra ese libro (número, «BONUS» o «recipe cost card» = 01-08) y el nombre existe allí; un nombre que no exista en ninguno falla. Lista blanca: solo «purchase→recipe» (la forma de la clave, que es el paréntesis del rótulo A4 de Conversions).
5. Las entradas de formato con «€» se corrigen en su sitio dentro de `wb._number_formats` (styles.xml sale sin «€»); las dd/mm que dejan de usarse pasan a `m/d/yyyy`, y las celdas de fecha apuntan a la builtin 14.

### Pendiente

- `--real` (lo lanza el orquestador tras la revisión) y, en ese mismo commit, `recipe-costing-kit` en `EXCLUIDOS` de `postprocess-transversal.py` (§2.1, T12).
- Gate 8 (revisión adversarial, tope 2 rondas) y 9 (test de Google Sheets, pendiente del consentimiento de John).
- Nº de páginas del PDF (23) contra la landing EN: F3.

## Revisión R1 EN (sesión Claude Code, 24-sep)

Ronda 1 de 2 (gate 8): lente de chef/manager US-UK (CHEF-01…19) y lente técnica (T1…T11). Todo se arregla en
**código o datos** y se regenera; ningún xlsx se toca a mano. Los ES de `dl/kit-escandallos/` siguen intactos
(`git status astro-site/` limpio). Scripts en serie con `istats` (46-55 °C).

### Hallazgo → decisión

| ID | Decisión | Qué se hizo (dónde) |
|---|---|---|
| CHEF-01 | aplicado | `aplicar_en.mercado_fichas`: «Tax rate (%)» a 0 en TODAS las fichas, con o sin receta (02 «6…9. Course» tenían el 10 % del ES). Gate 5: toda fila «Tax rate (%)» de los 14 libros = 0 (33 filas) |
| CHEF-02 | aplicado | PDF: «net food sales» en definición (bebida aparte, remite a la FAQ 4), fórmula, semana 1, checklist, dashboard mensual y caso. 11: G6 «Net food sales» (G05), B5 y B18 (`generar_mercado`), B34 (`generar_instrucciones_extra`) |
| CHEF-03 | aplicado, **opción A** | Pases de 02 y 03 sin «Current menu price», como el ES (`generar_mercado.menu`). Nota calculada en `Summary!B23` (02: 115 $ → 33,2 %) y `Menu Summary!B18` (03: 22 $ → 30,1 %). Gate 4 y `validar_mercado` exigen el pase vacío y la nota con precio y food cost del xlsx. Precio del 03: 24 → **22 $** (extremo bajo de su rango [estimado]): con los precios USDA de CHEF-12 el menú caía al 27,6 %, fuera de casual |
| CHEF-04 | aplicado | 02 «3. Fish»!H5 0,40 → **0,55** (redondo entero → filete, nota en la fila). `Trim Loss Factors!E7` (columna nueva de notas, fuera de la DV y del VLOOKUP): «Gutted, head-on fish cut on the bone. Whole round fish to skin-on fillet loses 50-60%». No se renombra la categoría (es clave de DV, VLOOKUP y 09). PDF: fila «Fish» de la tabla y táctica 3 reescrita (4,50 ÷ 0,45 = 10,00 $ > 8,20 $; «The yield test decides») |
| CHEF-05 | aplicado | = T2 |
| CHEF-06 | aplicado | 06 B8 (G03): «…in "Event Quote"!C5. Don't also enter it on the recipe cost card (keep Number of portions at 1)…» |
| CHEF-07 | aplicado | Checklist B31 «Allergen matrix for every dish (US: 9 major allergens incl. sesame · UK/EU: 14)», B36 con food manager certificado (UK: food hygiene certificates). Opcional también: «Timeline», «7 days out»…«3 h before service»…«After service»; columna E a 20 |
| CHEF-08 | aplicado | = T9: merma 0 en 07 «Avocado Toast» fila 6 y 02 «1. Amuse-Bouche» fila 6 (each→each). Avocado toast 25,3 % (café 25-30) |
| CHEF-09 | aplicado, **alternativa mínima** | Se mantiene 0,95 $ mayorista (así cumple D12 sin lista blanca en el gate 4, que la SPEC no prevé). A1 «Raspberry Macarons — 30 pieces (wholesale to cafés)» y línea en Instructions del 05: a 2,75 $ en vitrina ≈ 9 %, «price retail macarons on labor time» |
| CHEF-10 | aplicado | Caso: 450 cubiertos × 50,90 $ de ticket de COMIDA = 91.620 $ (mismos % e importes); introducción suavizada («percentages and sequence… real; dollar amounts illustrative»). PDF sigue en **23 páginas** |
| CHEF-11 | aplicado | Chocolate fundido, no templado: 5 % en la tarta (H5) y también en el chocolate blanco de la ganache de los macarons (H10, misma razón). 05 B10: «5% on chocolate melted into a batter or ganache (… use 10-12% for couverture you temper) and 8% on flour (dusting, bench flour and sifting)» |
| CHEF-12 | aplicado | Espárrago **3,99 $/lb**, coliflor **entera 2,36 $/lb** (vuelve la merma del 30 % del ES) y pepino persa **2,21 $/lb**: USDA AMS FVWRETAIL, semana del 18-sep-2026 (media ponderada anunciada; techo del precio de distribuidor, como BLS). Microgreens **1,88 $/oz** (30 $/lb de productor local; fuente secundaria). El resto de fruta y verdura de WebstaurantStore se revisó: sin desvíos de ×2. Ningún precio se tocó para cuadrar un % (D11) |
| CHEF-13 | aplicado | BONUS: compras en formatos de EE. UU. (50 lb bag, 25 lb case, 3 × 12 lb, 6 × 1 lb, 2 × 3 L, 8 botellas; catch weight a 2 decimales) y stock a 1-2 decimales; E se calcula para conservar F. `validar_mercado` M10 pasa a ±0,0005 absoluto (antes 1e-3 relativo): 0,05 puntos, invisible |
| CHEF-14 | aplicado | 12 C5 «PSMO (IMPS 189A: peeled, side muscle on)»; B18 «"Cutting loss"» (G06); C36 `#,##0.00` |
| CHEF-15 | aplicado en parte | 06 A1 «Spanish-Style Cocktail Reception — Cost per Guest» y Client Proposal B8 (no «Tapas»: quiche, shrimp cocktail y brioche no lo son). Carrot cake con **canola** (el aceite de la 08; catálogo «Canola oil»; el girasol sale del catálogo y del 13, que queda en **112** ingredientes). PDF: «risotto». Las croquetas del PDF se quedan |
| CHEF-16 | aplicado | G04: «a classic mistake»; gate 2 caza `v1\.\d` |
| CHEF-17 | aplicado | PDF: sin «dry-aged»; aceite de freidora «35 lb jug-in-box… Q-factor, or cost it by weight»; ejemplo UK £18,000 → £15,000 |
| CHEF-18 | (1) y (3) aplicados; **(2) rechazado** | (1) Instructions del 04: el 3-2-1 lleva 2 fl oz y sale a ≈ 28 % a 15 $ (calculado). (3) `Bottle Sizes!A2`: las botellas del ejemplo ya están enlazadas. (2) El mojito a 10 $ está dentro de su rango con fuente (10-14 $) y sale del pour cost objetivo, que es lo que enseña el kit; a 12 $ quedaría en el 16,8 %, fuera de D12 bar (18-24), y el gate 4 lo prohíbe. «Happy-hour price» sería un marco inventado |
| CHEF-19 | aplicado | 13 B9 calcula las filas libres (145 − 112 = **33**); apóstrofo recto en los 14 (fuente G03/G07 + `normalizar_apostrofos` en `aplicar_en` + lista blanca T6 sin ’); categoría sin renombrar, nota en `Trim Loss Factors!E9` («Also stems and flowers, such as asparagus and cauliflower») |
| T1 | aplicado | Gate 1 en sentido directo: `Transformador(ES) == EN` en fórmulas, DV (formula1/2) y CF. Gate 2 pasa restos, € y lista blanca por los literales de fórmula y CF. Check nuevo: el literal de una CF `cellIs` tiene que salir de las fórmulas de su rango |
| T2 | aplicado | Sin «(D19)» en `generar_mercado`; gate 2 con `RX_ID_INTERNO` (`(D|E|M|T n)`, `R2T-`, `[estimado]`, `SPEC`, `v1.x`) en valores, DV, pies, docProps, gráficos, literales y PDF |
| T3 | aplicado | 06 B12 (pre-tax en US/Canadá; incl. VAT/GST en UK/AU) + línea «U.S. and Canada: keep Tax rate (%)… at 0%» en el bloque de impuestos del 06 |
| T4 | aplicado | Gate 6(b): coincidencia exacta con mayúsculas; prefijo solo con «…», « (» o «:»; «X:» como marca literal de nota; también mensajes de DV y cabeceras/pies. Destapó 5 citas flojas, corregidas en textos_en («Sales mix», «Typical target» ×2, «Previous price per base unit», «recipe cost card, in "Trim loss %"») |
| T5 | aplicado | Gate 3 lee el XML: toda `<c>` con `<f>` lleva `<v>` (0 sin caché; 1.648 vacías legítimas `<v></v>`) |
| T6 | aplicado | Lista blanca: ASCII + letras Latin-1 + `→▸×—÷·−…©£≈✓⅓½⅔¾Σ📷📋`; también en literales y PDF |
| T7 | aplicado | `mapas.py`: envases `=IF(AND(ISNUMBER(B),B>0),B/k,"?")`. Gate 3 lo prueba en pycel con 0, "" y texto (pycel no recalcula con `set_value(None)`) |
| T8 | aplicado | `50 L keg` = 50.000 ml exactos → 87,9877 imp pt; nota «UK keg, 50 L ≈ 88 imp pt»; control del autotest de `mapas.py` actualizado |
| T9 | aplicado | = CHEF-08 |
| T10 | aplicado | `Trim Loss Factors` B = 20, C-D = 17 (solo formato) |
| T11 | aplicado | Gate `pdf` (Letter, **23** páginas = `PAGINAS_PDF`, ficheros y pestañas citados, tabla de trim loss = `Trim Loss Factors`, tabla D12 = 10!B9:D18, restos y lista blanca). Autotest: base limpia primero y subcadena esperada por defecto |

### Arrastres de la revisión (datos que cambian)

- Food cost del xlsx: 01 **30,9 %** · menú 02 **33,2 %** · menú 03 **30,1 %** (22 $) · 04 21,6/20,2/22,4/23,8 · 05 26,3/26,7/25,6 · 06 31,1 · 07 25,3/29,0/29,5/25,3 · 08 29,7/32,3/33,9. Todos dentro de D12.
- Catálogo 114 ingredientes (USDA AMS 5, distribuidor 75, BLS 7, secundaria 12, [derivado] 11, [estimado] 4); el 13, 112 + 33 libres.
- Quedan superadas: Cimientos, decisiones 1 (keg de 11 imp gal) y 3 (`IFERROR` en envases); Mercado, decisiones 2 (macarons sin declarar) y 7 (reparto del precio del menú); Montaje, decisión 3 (32 → 33 filas libres).
- Textos nuevos redactados por Claude (regla 1bis), nunca `bridge.py`.

### Resultados

| Comprobación | Resultado |
|---|---|
| `mapas.py` (autotest) | OK: n = 252, rango `$A$5:$B$286`, control `50 L keg→imp pt` = 87,9877 |
| `generar_mercado.py` → `validar_mercado.py` | 0 fallos; 16 recetas y 2 menús dentro de D12 |
| `generar_instrucciones_extra.py` | 515 filas, 0 fallos |
| `bono_guide_en.py` | gates del maquetador OK; **23 páginas** Letter |
| `aplicar_en.py` (dry-run, 46 s) | 14 xlsx + PDF; idempotencia 0 diferencias; `inject_cache` 2.848 fórmulas, `fallos_pycel=0` en los 14 |
| `gates_en.py` | **9/9 en verde** (1, 2, 3, 4, 5, 6, 7, 7bis, pdf): 2.788 fórmulas idénticas por transformación directa + 12 E3; 35 literales de CF; 7.480 literales y 7.897 valores sin restos; 0 fórmulas sin `<v>`; 33 filas «Tax rate (%)» a 0; 437 citas (140 pestañas, 109 rótulos, 180 de otro libro); PDF 23 págs., 8 ficheros y 18 pestañas citados, 8 filas de trim loss = xlsx, 10 filas D12 = calculadora 10 |
| `gates_en.py --autotest` | **25/25** defectos detectados con su mensaje (14 de antes + 11 nuevos: T1 ×3, T2, T5, T6, T7, T4, CHEF-01, CHEF-03, PDF) y base limpia en los 8 gates usados |
| `censo-entregables.py --only rck-dryrun/ --letter --fail` | 15 ficheros, 0 defectos. Regresión ES `--only kit-escandallos --fail`: 0 defectos |

Pendiente (igual que antes): `--real` y `EXCLUIDOS` de `postprocess-transversal.py` (orquestador); ronda 2 (la última) si
el orquestador la lanza; gate 9 (Google Sheets) con el consentimiento de John; la landing EN (F3) tiene que decir
**23 páginas** (`PAGINAS_PDF` en `gates_en.py`).

## Renombrado (D9 bis, sesión Claude Code, 24-sep, noche)

El producto pasa a **Food Cost Kit Pro** (slug `food-cost-templates`, `aichef.pro/en/digital-products/food-cost-templates`)
y los ficheros, títulos y dos pestañas se adaptan a la intención de búsqueda (SPEC, aviso de cabecera y D9 bis). Todo
se cambia en **código y datos** y se regenera; ningún xlsx se toca a mano. Los ES de `dl/kit-escandallos/` siguen
intactos. Scripts en serie con `istats` (48-61 °C). La carpeta de trabajo conserva su ruta
(`scripts/productos-digitales/recipe-costing-kit/`): es lo único que puede llevar el nombre viejo.

### Qué cambia y dónde

| Pieza | Antes | Ahora | Fuente |
|---|---|---|---|
| Producto, `subject`, cabecera B3, ancla del pie de marca | Recipe Costing Kit Pro | **Food Cost Kit Pro** (`subject` «Food Cost Kit Pro · v2.1») | `mapas.PRODUCTO`; `textos_en/G0-comun`, `GM-mapas` |
| URL (`description`, línea de versión D14) | …/recipe-costing-kit | `aichef.pro/en/digital-products/food-cost-templates` | `mapas.URL_PRODUCTO` |
| `keywords` | recipe costing kit, AI Chef Pro | food cost kit, food cost templates, AI Chef Pro | `G0-comun` |
| Ficheros (15) y títulos | research §1.2 | tabla D9 bis, exacta | `mapas.FICHEROS` y `mapas.TITULOS` (nuevo) |
| Título interior | «📋 Standard Recipe Cost Card — A La Carte Dish»; docProps «… · Recipe Costing Kit Pro» | docProps `title` = título D9 bis **exacto**; Instructions B2 = «📋 » + título (el icono es el diseño del ES) | `textos_en/G01-G07`; `aplicar_en.comprobar_titulo()` aborta si no casan |
| Pestaña 10 / 13 | Menu Price Calculator / Price List | **Menu Pricing Calculator** / **Price Tracker** | `mapas.HOJAS` |
| PDF | «Control Your Food Cost in 30 Days», `BONUS-30-day-food-cost-guide.pdf` | **«How to Reduce Food Cost in 30 Days»**, `BONUS-reduce-food-cost-30-days.pdf`; cabecera, subtítulo, asunto y keywords con «Food Cost Kit Pro» | `bono_guide_en.py` (PARAMS), `bonus-guide-food-cost-30-days.md` |
| `--real` | `dl/recipe-costing-kit/`, `RECIPE_COSTING_KIT_APPLY=1` | **`dl/food-cost-templates/`, `FOOD_COST_KIT_APPLY=1`** | `aplicar_en.py` |

Ficheros EN finales (nombre → título interior):

| Fichero | Título |
|---|---|
| `01-recipe-cost-card.xlsx` | Recipe Cost Card & Plate Cost Calculator |
| `02-tasting-menu-costing.xlsx` | Tasting Menu Costing |
| `03-prix-fixe-set-menu-costing.xlsx` | Prix Fixe & Set Menu Costing |
| `04-pour-cost-calculator.xlsx` | Pour Cost Calculator (Cocktails & Drinks) |
| `05-bakery-cake-pricing.xlsx` | Bakery & Cake Pricing Calculator |
| `06-catering-pricing-quote.xlsx` | Catering Pricing Calculator & Quote |
| `07-cafe-brunch-costing.xlsx` | Café & Brunch Menu Costing |
| `08-food-truck-pricing-break-even.xlsx` | Food Truck Menu Pricing & Break-Even |
| `09-food-waste-log.xlsx` | Food Waste Log |
| `10-menu-pricing-calculator.xlsx` | Menu Pricing Calculator |
| `11-food-cost-percentage-tracker.xlsx` | Food Cost Percentage Tracker |
| `12-yield-test.xlsx` | Yield Test (Butcher & Cooking Loss) |
| `13-ingredient-price-tracker.xlsx` | Ingredient Price Tracker |
| `BONUS-actual-vs-theoretical-food-cost.xlsx` | BONUS: Actual vs Theoretical Food Cost (Inventory & Waste) |
| `BONUS-reduce-food-cost-30-days.pdf` | How to Reduce Food Cost in 30 Days (23 páginas Letter) |

### Referencias: qué se reescribe solo y qué no

- **Solas** (`aplicar_en.py`, desde `mapas.HOJAS` / `mapas.FICHEROS`): fórmulas, DV, CF, áreas de impresión, XML de
  los gráficos, nombre de fichero de salida y copia del PDF. Comprobado: 10 y 13 no se citan por nombre en ninguna
  fórmula (refs 0 en los dos libros) y el gate 1 sigue en verde.
- **No solas** (texto traducido), arregladas en datos: dos accesos fijos `wb['Menu Price Calculator']` y
  `wb['Price List']` de `aplicar_en.py` (y siete en `gates_en.py`, más el pycel `'Price List'!K…`) pasan por
  `mapas.hoja_en()`; las citas «template 13 (Ingredient Price List)» → «(Ingredient Price Tracker)» en `G0-comun`, `G02`
  y `generar_instrucciones_extra.py` (12 filas); «Template 01 (Standard Recipe Cost Card)» → «(Recipe Cost Card)»
  en `G06` y `generar_mercado.py`; «template 03 (Prix Fixe Lunch Menu)» y «template 04 (Cocktails & Drinks)» en `G07`;
  en el bono, 13 nombres de fichero, 4 citas de pestaña («Menu Pricing Calculator», «Price Tracker») y «price list» →
  «price tracker» en el titular y el checklist de la semana 3.
- **Decisión (para la ronda 2):** los rótulos de hoja que repetían el nombre viejo del producto siguen al nombre
  nuevo, como en el ES (que repite el suyo): 09 `Weekly Waste Log!A1` «Food Waste Log — Weekly Waste vs. Purchases»,
  10 `B2` «Menu Pricing Calculator — Suggested Menu Price», 11 `Dashboard!B2` «Food Cost Percentage Tracker», 13 `A1`
  «Ingredient Price Tracker» y 03 `Menu Summary` «Summary — Prix Fixe & Set Menu». Las formas cortas «template 12
  (Yield Test)» y «Template 08 (Food Truck)» se quedan: son el arranque del título nuevo.
- Regenerados en cadena (solo cambian los nombres; diffs revisados): `extraer_textos.py` → `textos_es.json` y
  `censo_es.json` (pistas D2/D14, `en_mapa` de 10/13 y `nombre_en`), `generar_gm_mapas.py` → `GM-mapas.json`,
  `generar_mercado.py` → `mercado_en.json` (2 líneas) → `validar_mercado.py` 0 fallos, `generar_instrucciones_extra.py`
  → `instrucciones_extra_en.json` (claves por fichero EN; 0 fallos). A mano: `glosario_en.json` (ficheros, pestañas,
  nombre del producto) y `textos_en_por_celda.json` (fichero del BONUS).

### Gate nuevo `nombre` (`gates_en.py --solo nombre`)

- (a) La carpeta tiene **exactamente** los 15 ficheros de `mapas.FICHEROS`: uno de más (p. ej. un nombre retirado
  que quedó de una construcción vieja) o de menos falla.
- (b) xlsx: **todo su XML** (valores, docProps, pies, fórmulas, DV, gráficos, `workbook.xml`), 196 partes: cero
  «Recipe Costing» (con mayúsculas: en minúscula es término de oficio y se admite), cero `recipe-costing-kit` en
  cualquier caja y cero nombres o ficheros retirados (`mapas.NOMBRES_RETIRADOS` y `FICHEROS_RETIRADOS`); docProps
  `title` = D9 bis; una sola fila «📋 …» en Instructions = D9 bis; cabecera «Food Cost Kit Pro — AI Chef Pro»; las
  pestañas de 10 y 13 existen.
- (c) PDF: texto de las 23 páginas + metadatos, mismo filtro; título de metadatos = D9 bis; portada con título y
  nombre del producto.
- (d) Datos: `textos_en/*.json`, `textos_en_por_celda.json`, `mercado_en.json`, `mercado_fuentes_web.json`,
  `instrucciones_extra_en.json`, `glosario_en.json`, `textos_es.json`, `censo_es.json` y el `.md` del bono (17
  ficheros), con una única excepción: la ruta `scripts/productos-digitales/recipe-costing-kit/`. En los datos no cuenta
  `08-food-truck.xlsx` como retirado, porque es también el nombre del fichero ES.
- También `gate5` exige ahora `title` = D9 bis y «food cost kit» en `keywords`, y `mapas.py` (autotest) comprueba
  15 ficheros canónicos, `TITULOS` alineado con `FICHEROS`, ningún retirado y las pestañas 10/13.
- `PAGINAS_PDF` sigue en **23** (el título nuevo no mueve la paginación).

### Resultados

| Comprobación | Resultado |
|---|---|
| `mapas.py` (autotest) | OK: n = 252, rango `$A$5:$B$286`, 15 ficheros y títulos D9 bis |
| `validar_mercado.py` | 0 fallos |
| `bono_guide_en.py --autotest` y maquetado | 14/14; **23 páginas** Letter, `BONUS-reduce-food-cost-30-days.pdf` |
| `aplicar_en.py` (dry-run, 50 s) | 14 xlsx + PDF; idempotencia 0 diferencias; `inject_cache` 2.848 fórmulas, `fallos_pycel=0` en los 14 |
| `gates_en.py` | **10/10 en verde** (1, 2, 3, 4, 5, 6, 7, 7bis, pdf, **nombre**); PDF: 8 ficheros y 18 pestañas citados, todos existen |
| `gates_en.py --autotest` | **34/34** defectos detectados con su mensaje (25 de antes + 9 del gate `nombre`: title, pie y línea de versión con el nombre/slug viejo, título de Instructions, pestaña 10 retirada, fichero retirado en la carpeta, título del PDF, `textos_en` y `.md` del bono) y base limpia en los 9 gates usados |
| `censo-entregables.py --only rck-dryrun/ --letter --fail` | 15 ficheros, 0 defectos |

Pendiente (orquestador / F3): `--real` con `FOOD_COST_KIT_APPLY=1` → `dl/food-cost-templates/`, `food-cost-templates`
en `EXCLUIDOS` de `postprocess-transversal.py` en ese mismo commit, claves de `get-download-urls.ts` con los 15
nombres nuevos, y la landing/dashboard EN con los títulos de la tabla D9 bis y «23 pages».

## F3-A · capa de producto EN (sesión Claude Code, 24/25-sep)

> El Mac se apagó a mitad de la F3-A (sin batería). Lo hecho antes del apagón se reconstruyó en `bbd4b2a0`
> (ficha, landing, access, library, dashboard, island, 4 componentes con `lang`, CryptoPayButton EN, hreflang
> ES↔EN, `tienda.ts` en.vivo). Esta sesión cerró el resto. Todo en serie, `istats` antes de cada script
> (51-58 °C), sin builds ni navegador.

**Qué se hizo** (commits `c3999f7b`, `656ac9a3`, `067579cb`, `29137850`):
- `/en/crypto-payment` = copia traducida de `/pago-cripto` (mismos 11 estados y mismos `data-*` en el mismo orden;
  enlace «product page» → `/en/digital-products/<productId>`); fuera del sitemap; rastreable (lleva `noindex`).
- Entrada `food-cost-templates` con `lang: 'en'` en `zona-app.ts`, `verify-purchase.ts`, `resend-access.ts`,
  `get-download-urls.ts` (15 claves = las del dashboard), `admin-generate-access.ts` (email manual por idioma),
  `AdminGenerateAccess.tsx` y `productos-digitales-config.ts`. `stripe-webhook`, `nowpayments-ipn`,
  `crypto-checkout` y `crypto-order-status` no tienen mapa propio (leen `PRODUCTS`, `PAYMENT_LINKS`, `PRODUCT_PRICES`).
- `payment-links.ts` y `product-prices.ts` regenerados: una línea añadida en cada uno (`bJecMYa8AgIS9fhcbz6oo1y`, `usd: 19`).
- `miselup-gate.py` (entradas con `lang` ≠ es → cero rastros) y `whatsapp-gate.py` (dashboards anidados exentos).

**Validación estática:** `fase5-generate-zona-app.py --check` verde (150 ficheros; EN omitida) · `tienda-gate.py`
verde · `gate-flujo-postpago.py --offline` 51 productos / 736 entregables / 0 fallos (EN: 15 ficheros = 15 tarjetas) ·
`sync-* --check` verdes · `robots-gate.py` verde · `@astrojs/compiler` sin errores en los 8 `.astro` · esbuild en los
18 `.ts/.tsx` · `tsc` con los mismos 6 errores preexistentes antes y después · emails de los 50 productos ES
(admin + verify) idénticos byte a byte · CryptoPayButton ES idéntico (6/6) · SaasDiscoveryBanner, LogoBadge,
WhatsAppProductSupport y ProductChangelog: 107 renders ES idénticos sin prop y con `lang="es"`, cerrados y abiertos.

**Pendiente (F3-B, con deploy preview):** `tienda-gate.py --base` y `--es-identico --esperadas /kit-escandallos`,
`gate-flujo-postpago.py --base … --crypto-products all --crypto-exclude pro-prompts-ebook`, `miselup-gate`,
`whatsapp-gate` sobre el `dist` del preview, `datafast-gate`, `nombre-gate`; lastmod de la landing EN en el sitemap
(hoy caería en `NEW_URLS_LASTMOD`); enlaces entrantes (§3.7); compra de prueba y broadcast EN.
