# Kit de Inventario v2.0 (ES) — inventario de F1 para Restaurant Inventory Kit Pro (EN)

> Sesión Claude Code, 25-sep-2026. Fuente = los **9 xlsx PUBLICADOS** de `astro-site/public/dl/kit-inventario/`
> (sha256 de cada uno en `censo_es.json`), nunca un generador. Recuentos sacados por `extraer_textos.py`
> (`censo_es.json` + `textos_es.json`); celdas citadas como `libro:Hoja!celda`. Los defectos heredados se
> señalan (§3) y NO se corrigen en el ES desde esta carpeta.

## 0. Totales del kit (censo)

| Libro | Hojas | Texto | Fórmulas | Fx→otra hoja | DV | CF | Merges | Fechas | Fmt € | Verdes | Áreas impr. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 01-inventario-stock-diario | 5 | 252 | 333 | 19 | 6 | 9 | 9 | 0 | 228 | 900 | 4 |
| 02-fichas-proveedores | 5 | 219 | 175 | 65 | 3 | 3 | 4 | 60 | 150 | 570 | 4 |
| 03-pedidos-compra | 5 | 158 | 116 | 39 | 6 | 2 | 23 | 42 | 247 | 699 | 4 |
| 04-recepcion-mercancias | 4 | 198 | 247 | 120 | 5 | 4 | 11 | 100 | 124 | 860 | 3 |
| 05-control-mermas | 5 | 136 | 167 | 34 | 5 | 3 | 7 | 120 | 247 | 1103 | 4 |
| 06-fifo-caducidades | 4 | 185 | 264 | 12 | 4 | 5 | 1 | 200 | 107 | 744 | 3 |
| 07-analisis-costes-compras | 5 | 155 | 153 | 16 | 3 | 4 | 3 | 0 | 262 | 270 | 4 |
| BONUS-08-inventario-rapido-mensual | 2 | 180 | 321 | 0 | 2 | 1 | 1 | 0 | 161 | 560 | 1 |
| BONUS-09-calculadora-punto-pedido | 3 | 98 | 150 | 60 | 1 | 0 | 1 | 0 | 31 | 273 | 2 |
| **Total** | **38** | **1.581** | **1.926** | **365** | **35** | **31** | **60** | **522** | **1.557** | **5.979** | **29** |

Transversal (los 9 libros):
- **Sin gráficos, sin imágenes, sin nombres definidos, sin sharedStrings** (cadenas inline). 29 hojas protegidas **sin
  contraseña**; las 9 `Instrucciones` sin proteger y sin área de impresión. 1 autofiltro (06 `Control FIFO`).
- **Todas** las celdas desbloqueadas son verdes (`E8F5E9`): 5.979 = 5.979. Es la convención del kit («verde = lo que
  escribes tú») y la EN la conserva.
- Papel **A4 (`paperSize 9`) en las 38 hojas**; pie `AI Chef Pro · aichef.pro · Página &P de &N` en todas.
- Fechas: 522 celdas con formato `dd/mm/yyyy` (ninguna con `numFmtId 14`). Formato con `€`: 1.557 celdas
  (`#,##0.00 €`).
- docProps iguales en los 9 salvo el título: `title` «<título> · Kit Control de Inventario y Compras», `subject`
  «Kit Control de Inventario y Compras · v2.0», `keywords` «kit inventario, AI Chef Pro», `description`
  «aichef.pro/kit-inventario», `category` «AI Chef Pro · Productos digitales».
- Línea de versión en Instrucciones: «Versión 2.0 · agosto 2026 · aichef.pro/kit-inventario · info@aichef.pro».
- Columnas ocultas: 02 `Comparativa Precios` P:T (precio normalizado por unidad) y 04 `Control Recepción` P (Tª mín.).
- **Taxonomía única** (pieza de diseño que la EN debe preservar byte a byte entre libros): las mismas 10 categorías
  en las 9 plantillas (DV literal) y la misma lista de 10 unidades en las 7 que llevan producto. `Resumen Dashboard`
  (01), `Análisis por Categoría` (05) y `Coste por Categoría` (07) agregan con `SUMIF/COUNTIF` **por el texto** de la
  categoría: una traducción distinta en un solo sitio rompe los totales sin error visible.
- **Tabla maestra de 50 productos** repetida: 01 (Cocina 20 + Barra 15 + Almacén 15) = BONUS-08 (mismos 50, mismo
  orden, mismo precio); subconjuntos con el MISMO precio en 02, 03, 04, 05, 06, 07 y BONUS-09. BONUS-09 está
  calibrado para que `consumo diario × (lead time + cobertura)` = par level del 01 y `stock máximo` = par max del 01
  (comprobado en las 8 filas de ejemplo: pollo 4×(1+1)=8, solomillo 1×(2+1)=3, salmón 2×(1+1)=4, leche 8×(2+1)=24,
  patata 6,25×(2+2)=25…).

## 1. Por libro

### 01 · Inventario de Stock Diario
- Pestañas: `Instrucciones` · `Cocina` (A1:M47, datos 5-44) · `Barra` (datos 5-34) · `Almacén` (datos 5-34) ·
  `Resumen Dashboard` (totales por zona y por categoría, 33 fórmulas `COUNTIF/SUMIF` sobre las tres zonas).
- Columnas: # · Producto · Categoría (DV) · Unidad (DV) · Par Level · Par Max · Stock Real · Estado · A Pedir ·
  Precio/ud (€) · Valor (€) · Proveedor · Notas.
- Literales: `"🔴 PEDIR"`, `"🟡 BAJO"`, `"🟢 OK"` (100/100/100 en las 3 zonas); `Resumen` cuenta `"*BAJO*"`, `"*PEDIR*"`.
  CF `containsText` con tokens PEDIR / BAJO / OK en H.
- Variables de mercado: 50 productos españoles con precio en € (`Cocina!B5:J24`, `Barra`, `Almacén`); unidades `kg`,
  `L`, `ud`, `docena`, `barril`, `saco`, `caja`, `rollo`, `paquete`; «Cerveza de grifo (barril 30 L)», «Vino tinto
  (botella 75 cl)», «Aceite de girasol (garrafa 5 L)», «Nata 35 % M.G.», «Huevos M», «Cubetas GN 1/1», «Lejía
  alimentaria»; «precio de compra SIN IVA» (`Instrucciones!A10`, `Cocina!A3`…); `Fecha: ___/___/______` (orden d/m/a,
  `Cocina!A2`); A4.

### 02 · Fichas de Proveedores
- Pestañas: `Directorio Proveedores` (A1:S23; 6 fichas de ejemplo) · `Comparativa Precios` (hasta 5 proveedores, precio
  normalizado en P:T ocultas, estado de la cotización con `TODAY()`) · `Evaluación Proveedores` (5 criterios 1-5, nota
  A/B/C/D, coherencia con «Homologado») · `Condiciones Comerciales` (trae plazo de pago, mínimo y días del directorio).
- Literales: `"Prov. 1…5"`, `"⚠ falta contenido"`, `"⛔ COTIZACIÓN VENCIDA"`, `"🟡 vence esta semana"`, `"🟢 vigente"`,
  notas `"A — Preferente"… "D — Sustituir"`, `"S"` (comparado con la DV `S,N,Pendiente`), `LEFT(…,1)="D"/"C"`.
- Variables de mercado: **CIF/NIF** (`Directorio!D3`, datos D4:D9), **Nº RGSEAA** (E3, E4:E9), homologación como
  «prerrequisito de tu plan APPCC» (`Instrucciones!A14`, DV P4:P23, `Evaluación!A2`); direcciones, teléfonos y correos
  `.es` españoles (Pamplona, Vigo, Mercavalencia, Alcalá de Guadaíra, Alicante, Alcobendas); «30 días fecha factura»,
  «Contado»; formatos de venta «Caja 5 kg», «Garrafa 5 L», «Saco 20 kg», «Caja 12 briks de 1 L»; rappel en €
  («a partir de 2.000 € al mes»); fechas dd/mm.

### 03 · Pedidos de Compra
- Pestañas: `Pedido Actual` (cabecera con VLOOKUP a `Proveedores`, 30 líneas, totales F40:H43, desglose por tipo de
  IVA A45:D48, aviso de pedido mínimo A43) · `Proveedores` (copia operativa del directorio) · `Historial Pedidos`
  (fila 4 enlazada al pedido en curso) · `Listas` (IVA por categoría A2:B11 + excepciones por producto E2:F10).
- Literales: `"⚠ falta coste"`, `"✓ El pedido supera el mínimo…"`, `"⚠ POR DEBAJO DEL PEDIDO MÍNIMO…"`, `" líneas"`,
  `"<>"`; CF tokens «POR DEBAJO» / «supera».
- **Variable fiscal (la más profunda del kit):** DV `H9:H38` = lista literal `"4,10,21"` (tipos de IVA españoles);
  `Listas` con el tipo por categoría (4/10/21) y 9 excepciones (arroz, harina, huevos, legumbres, pasta al 4 %;
  mantequilla y nata al 10 %; refresco y tónica al 21 %); desglose fijo por **4 / 10 / 21** en `Pedido Actual!A46:A48`
  (números bloqueados); rótulos BASE IMPONIBLE / CUOTA DE IVA; `Historial` con cuotas del 10, 21 y 4 %.
  Emisor «CIF / NIF» (`Pedido Actual!F4`). «Archivo → Imprimir → PDF … A4 apaisado» (`Instrucciones!A13`).

### 04 · Recepción de Mercancías
- Pestañas: `Control Recepción` (A1:V45; 40 líneas; familia sugerida por VLOOKUP a `Verificación Temperaturas!G4:H13`,
  límites por VLOOKUP a `A4:E18`, conformidad en R) · `Registro Incidencias` (importe reclamado − abonos) ·
  `Verificación Temperaturas` (15 familias con Tª mín./máx. numéricas + puente categoría→familia).
- Literales: `"N/A"`, `"⚠ FAMILIA SIN LÍMITE"`, `"✗ RECHAZAR (frío)"`, `"✗ RECHAZAR (calor)"`, `"✓ CONFORME"`,
  `"*RECHAZAR*"`; CF tokens RECHAZAR / SIN LÍMITE / CONFORME + expresión `SEARCH("RECHAZAR",$R4)` sobre O.
- **Variables normativas:** 15 familias de la UE con límites en **°C** (7 / 3 / 4 / 4 / 2 / 2 °C; congelados −15 °C al
  recibir; comidas preparadas 4 y 8 °C; lácteos 8; frutas 12; huevos «no refrigerar» con N/A), base normativa
  **Reg. (CE) 853/2004, 852/2004, 589/2008 y RD 3484/2000** (`Verificación!E4:E18`, `Instrucciones!A11`); 38 textos
  con °C/Tª (`O3:R3`, `B3:D3`, `B4:B17`, `G15`, `A20`, `Instrucciones!A7-A8`); «APPCC» (A6, A11, A20).
- Ejemplo (A4:U7) = una sola historia con `Registro Incidencias` A4:K6: entrega corta (solomillo 12→10 kg), rechazo
  por temperatura (merluza a 5 °C con límite 2 °C), mal estado (tomate con moho) y una línea sin control de
  temperatura (huevos, familia N/A). Importes 64 / 112 / 39 € coherentes con precio × cantidad.

### 05 · Control de Mermas
- Pestañas: `Registro Diario Mermas` (100 líneas, total G105) · `Análisis por Categoría` (10 categorías + 10 motivos,
  COUNTIF/SUMIF) · `Dashboard Mermas` (coste, % sobre compras, nº, categoría y motivo top; objetivo 3 %) ·
  `Plan de Acción` (5 causas típicas escritas).
- Literales: `"⚠ falta coste"`, `"🔴 ALERTA"`, `"🟡 REVISAR"`, `"🟢 OK"`, `"— sin mermas registradas —"`, `" veces"`,
  `" · "`, `"<>"`. CF tokens ALERTA / REVISAR / OK.
- Variables: «compras del mes SIN IVA» (`Dashboard!A10`, `A13`, `Instrucciones!A8`); «500 € de merma son mucho en un
  bar…» (`Instrucciones!A10`, `Dashboard!A13`); «Responsable del plan APPCC» (`Plan!F6`); «etiquetado FEFO».

### 06 · FIFO y Caducidades
- Pestañas: `Control FIFO` (50 lotes, autofiltro, fecha límite efectiva = MIN(caducidad, apertura + vida útil)) ·
  `Alertas Caducidad` (contadores y valor por estado, protocolo) · `Mapa Almacén` (11 zonas = DV R5:R54).
- Literales: `"Consumo preferente"` (comparado con la DV `Caducidad,Consumo preferente`), `"⚠ REVISAR (consumo
  preferente)"`, `"⛔ CADUCADO — RETIRAR"`, `"🔴 URGENTE"`, `"🟡 PRÓXIMO"`, `"🟢 OK"` y sus comodines `"*…*"` en
  `Alertas`; CF tokens CADUCADO / URGENTE / REVISAR / PRÓXIMO / OK.
- Variables: **Reglamento (UE) 1169/2011, art. 24** (caducidad vs consumo preferente, `Instrucciones!A18`); zona
  **«Huevera» a temperatura ambiente, «NO refrigerar antes de la venta»** con Reg. (CE) 589/2008 (`Mapa!A13:E13`,
  `Instrucciones!A9`); químicos con Reg. (CE) 852/2004 (`Mapa!E14`); temperaturas de zona en °C (`Mapa!B4:B14`);
  «5.ª gama»; 200 fechas dd/mm.

### 07 · Análisis de Costes de Compras
- Pestañas: `Coste por Categoría` (10 × 12 meses, fila 14 TOTAL) · `Evolución Mensual` (meses largos) ·
  `Top 20 Productos` (ranking Top 5 con LARGE) · `Dashboard KPIs` (food cost de consumo, coste por cubierto, variación;
  periodo elegible en B10).
- Literales: `"Año completo"` (comparado con la DV `Año completo,Ene…Dic`) y `MATCH($B$10, B3:M3)` sobre las cabeceras
  `Ene…Dic` de `Coste por Categoría`: **cabeceras de mes, ítems de la DV y literal tienen que coincidir**. `">0.05"`,
  estados OK / REVISAR / ALERTA.
- Variables: «TODOS LOS IMPORTES VAN SIN IVA (BASE IMPONIBLE)… entre un 4 % y un 21 % inflado» (`Instrucciones!A6-A7`);
  rango sano 28-32 % (`Dashboard!D4`); ejemplo coherente 10.400 € compras / 34.000 € ventas / 1.450 cubiertos →
  31,0 % (`Dashboard!A19`, comprobado: (4.200 + 10.400 − 4.050) / 34.000 = 31,03 %); meses en español.

### BONUS-08 · Inventario Rápido Mensual
- Pestaña `Conteo Rápido` (80 líneas; valor, consumo = anterior + compras − actual, variación y %; CF ámbar > 20 %).
- Literales: `"⚠ falta coste"`, `"⚠ faltan compras"`. Mismos 50 productos y precios que el 01.
- Variables: € y «SIN IVA» (`A3`), `Mes: ____ Fecha: ___/___/______` (`A2`), «filas libres hasta la 84».

### BONUS-09 · Calculadora Punto de Pedido
- Pestañas: `Calculadora` (30 líneas; ROP = consumo × lead time + stock de seguridad; EOQ de Wilson; cantidad
  sugerida = MIN(EOQ, consumo × vida útil × factor, stock máx.)) · `Parámetros` (coste de pedido 3 €, almacenamiento
  25 % anual, factor de vida útil 0,7: las tres celdas verdes que leen las fórmulas).
- Sin literales traducibles. Variables: «2-5 €» y «3 €» de coste de pedido (`Parámetros!B4`, `Instrucciones!A21`);
  ejemplo de la leche en L (`Instrucciones!A19`: 8 L/día, 12 días, 60 L, EOQ 287, tope 67 — comprobado con los
  parámetros); lead times por familia española (`Parámetros!A6:C9`).

## 2. Literales dentro de fórmulas, CF y DV que son texto español

Todos están en `censo_es.json` (`literales`, `literales_cf`, `dv`) y tienen EN en `mapas.LITERALES` /
`mapas.TOKENS_CF` / `mapas.DV_LISTAS` (autotest de `mapas.py` contra el censo: 0 errores). Pares que **deben
cambiar a la vez** o se rompe la lógica sin error visible:
1. Estado de 01 (fórmula H) ↔ CF de H ↔ `COUNTIF("*BAJO*"/"*PEDIR*")` de `Resumen Dashboard`.
2. `"S"` de 02 `Evaluación!J` ↔ ítem `S` de la DV `Directorio!P4:P23`.
3. Estados de 04 R ↔ CF de R ↔ CF expresión de O ↔ `COUNTIF("*RECHAZAR*")` de la fila 45.
4. `"Consumo preferente"` de 06 L ↔ ítem de la DV F5:F54; estados de L ↔ CF ↔ comodines de `Alertas Caducidad`.
5. `"Año completo"` de 07 `Dashboard!B6` ↔ ítem de la DV B10; `Ene…Dic` de la DV ↔ `Coste por Categoría!B3:M3`.
6. Las 10 categorías: 7 DV literales + etiquetas `A` de `Resumen Dashboard`, `Análisis por Categoría`, `Coste por
   Categoría`, `Listas`, `Verificación Temperaturas!G4:G13` + todas las celdas de ejemplo.
7. Las 15 familias de 04: `Verificación!A4:A18` (lista de la DV G4:G43 y clave del VLOOKUP) ↔ `H4:H13` ↔ `G4:G7`.
8. Las 11 zonas de 06: `Mapa Almacén!A4:A14` ↔ DV literal R5:R54 ↔ `R5:R10`.
Sin cambio: `""`, `"<>"`, `"—"`, `"D"`, `"C"`, `"N/A"`, `"🟢 OK"`, `"*OK*"`, `">0.05"`, `" · "`.

## 3. Defectos heredados (se señalan; corregir en AMBAS ediciones, el ES en su propia sesión)

| # | Dónde | Defecto | Tratamiento EN |
|---|---|---|---|
| I1 | `B09:Parámetros!C12` | Texto de cliente con un ID interno de auditoría: «RT-08: es una casilla verde de verdad…» | Se elimina el «RT-08:» (D23) |
| I2 | `06:Instrucciones!A17` y landing ES (`checkItems`, «las mismas unidades en las 8 de producto») | La DV de unidades está en **7** libros (01, 02, 03, 05, 06, 07, B08), no en 8 | EN dice 7 (D23) |
| I3 | Landing ES (`compatApps`) | «Compatible con Excel, Google Sheets, LibreOffice y Numbers» sin prueba registrada | EN = pastillas del piloto (D22) |
| I4 | Landing ES FAQ «¿Puedo usarlo en varios restaurantes?» | Licencia «todos tus locales / consultores» contradice la licencia del piloto (D18 del piloto: un negocio por compra, sin copias a clientes) | EN = licencia D18 del piloto (D22) |
| I5 | `07:Top 20 Productos!L27:M31` | Con dos gastos iguales el Top 5 repite el primero (documentado en `A33`, no corregido) | Se mantiene y se traduce el aviso (paridad) |
| I6 | `04:Verificación Temperaturas!B14` vs `C14` | «Tª ideal 4 a 12 °C» con mínimo aceptable 0 °C: ideal ≠ aceptable sin explicarlo | La tabla EN se reescribe (D12) y distingue «ideal» de «accept» |
| I7 | `03:Pedido Actual!A46:A48` | El desglose por tipo está fijado a 4/10/21 en celdas bloqueadas: un tipo distinto no se desglosa | EN: celdas editables (D11) |
| I8 | docProps | El nombre interno «Kit Control de Inventario y Compras» ≠ nombre comercial «Kit de Inventario» | EN usa un único nombre (D2) |
| I9 | 06 `Mapa Almacén` y 04 familia «Huevos» | Correcto en la UE, **peligroso en EE. UU.**: allí el huevo lavado se refrigera por ley | Variable de mercado (D12), no defecto del ES |

## 4. Recuento de cadenas (textos_es.json)

967 cadenas únicas (2.071 apariciones): **542 a traducir** (6.865 palabras) en G0-comun (28) + G01-G05; **246 a
localizar** (GL-mercado: productos, fichas de proveedor, notas «(ejemplo)», zonas y temperaturas de zona); 179 que
no se traducen (GM-mapas: 30 pestañas, 110 claves-dato, 39 regenerar). Excluidas: 21 sin letras, «AI Chef Pro» y «N/A».
