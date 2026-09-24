# Recipe Costing Kit — F1 · Inventario del Kit de Escandallos Pro (ES)

> Tienda internacional en inglés · producto piloto · fase **F1** (fundamentos). Sesión Claude Code, 24-sep-2026.
> Doc canónico: `scripts/productos-digitales/TIENDA-INTERNACIONAL.md` (§1 regla «duplicar y adaptar», §3 arquitectura,
> §4 fases, §6 checklist). Este informe es un **inventario**: dice qué entrega hoy el kit ES y qué pieza hay que
> duplicar y adaptar. No decide precios, slugs ni textos EN; donde hace falta una decisión, lo marca.
>
> Método: lectura del repo en `main` (`f7078d3`) + un script openpyxl de SOLO LECTURA sobre los 12 xlsx publicados,
> uno a uno y en serie (CPU entre 49,9 °C y 56,5 °C con `istats` antes de cada tanda). Sin builds, sin navegador,
> sin ejecutar generadores. Lo que no se ha podido comprobar se dice como tal.

---

## 0. Conclusiones en diez líneas

1. **La fuente de verdad son los xlsx PUBLICADOS** (`astro-site/public/dl/kit-escandallos/*.xlsx`, commit `ed45f35`),
   no `scripts/generate-escandallos.py`. El generador es la v1.0 de marzo: 97 de sus 253 literales de texto ya no
   están en el kit y escribe en una carpeta que no existe (§2).
2. Los xlsx son el resultado de **tres capas encadenadas**: generador v1.0 → Fase A (v1.1, metadatos/A4/cache) →
   post-proceso v2.0 (`kit-escandallos-v2_0/main.py`, que parte de los ficheros publicados, no de cero). Ninguna
   capa por sí sola reproduce el kit. **F2 = duplicar los 12 xlsx publicados y aplicarles una capa de mercado EN.**
3. Tamaño de la traducción de los xlsx: **832 cadenas únicas, 6.698 palabras únicas** (36.848 caracteres), de las
   que 154 se repiten en ≥ 8 ficheros. El PDF bonus: **7.478 palabras**, 17 páginas, 17 tablas.
4. **Riesgo técnico nº 1: los nombres de hoja.** 849 fórmulas, 29 validaciones, 1 formato condicional y los 2
   gráficos citan hojas por su nombre. Traducir un nombre de hoja sin reescribir esas referencias rompe el libro.
5. **Riesgo técnico nº 2: las claves de texto que son datos.** Las categorías de merma (21), las unidades
   (`kg,g,L,ml,cl,ud,docena,manojo,sobre,lata,botella`) y las claves de `Conversiones` (`kg→g`, `docena→ud`…) se
   buscan con `VLOOKUP`: hay que traducirlas con el MISMO mapa en la tabla, en los desplegables y en las filas.
6. 1.392 celdas-fórmula llevan literales de texto; los que están en español son `"revisa merma"` (453),
   `"revisa unidades"` (453) y `"ALERTA"` (29 + 2 reglas de CF). `"OK"`, `"?"`, `"→"`, `"✓"` sirven tal cual.
7. **Variables de mercado en todos los ficheros:** IVA 10 % en celda (+ textos IGIC/ITBIS/IVU), 1.027 celdas con
   formato `€`, unidades métricas y formatos de botella 70/75 cl, precios de ejemplo en €, «menú del día», «carnés
   de manipulador», benchmarks de food cost, A4, fechas `dd/mm/yyyy`, meses en español.
8. **La landing ya es parametrizable** (`KitExcelLandingPage.astro` con `lang` desde la 0.B y
   `i18n/tienda/en.json` completo, 44/44 claves). Falta todo lo demás del lado EN: data file, wrappers anidados,
   dashboard, gate/island, OG image, `/en/crypto-payment`, `CryptoPayButton` con idioma.
9. **Cuatro gates no están listos para un producto EN vivo** (se pondrían rojos o mirarían a otro lado):
   `whatsapp-gate.py`, `miselup-gate.py`, `robots-gate.py` (no ve rutas anidadas) y `censo-entregables.py` (exige
   A4). Y dos scripts del bono tienen el español cableado (`main.py:161-164`, `bono_guia.py:350-351,451,468-470`).
10. Capa comercial honesta: en EN hay que **quitar** `aggregateRating`, `reviews`, `testimonials`; y **decide John**
    sobre el ancla de precio (`€49 / -75 %`), «Sube pronto», «El kit #1…» y el badge «🔥 Best Seller» del hub EN.

---

## 1. Entregables (`astro-site/public/dl/kit-escandallos/`)

13 ficheros: 11 plantillas + `BONUS-mermas-inventario.xlsx` + `BONUS-guia-food-cost-30-dias.pdf`. Mapa de claves de
descarga en `netlify/functions/get-download-urls.ts:5-18` (§5).

### 1.1 Resumen técnico por fichero (medido con openpyxl 3.1.3, `python3` 3.7.2)

| Fichero | Hojas | Texto | Fórmulas | Núm. entrada (verde) | Celdas `€` | Merges | DV (lista literal) | CF | Gráf. | Fx→hoja | Fx con literal | Hojas protegidas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01-escandallo-estandar | 4 | 212 | 79 | 130 (34) | 37 | 19 | 2 (1) | 2 | 0 | 30 | 60 | 1 |
| 02-menu-degustacion | 13 | 507 | 617 | 200 (104) | 235 | 164 | 18 (9) | 18 | 0 | 263 | 405 | 10 |
| 03-menu-del-dia | 8 | 336 | 236 | 164 (68) | 116 | 55 | 6 (3) | 7 | 0 | 97 | 146 | 5 |
| 04-cocktails-bebidas | 8 | 367 | 280 | 186 (90) | 131 | 76 | 8 (4) | 8 | 0 | 108 | 186 | 5 |
| 05-pasteleria | 6 | 317 | 213 | 174 (78) | 95 | 55 | 6 (3) | 6 | 0 | 82 | 156 | 3 |
| 06-catering | 7 | 405 | 103 | 175 (47) | 62 | 31 | 3 (2) | 3 | 0 | 33 | 62 | 4 |
| 07-cafeteria-brunch | 7 | 374 | 274 | 202 (106) | 122 | 73 | 8 (4) | 8 | 0 | 104 | 201 | 4 |
| 08-food-truck | 7 | 333 | 219 | 175 (79) | 109 | 61 | 6 (3) | 6 | 0 | 85 | 147 | 4 |
| 09-control-mermas | 3 | 79 | 77 | 65 (33) | 20 | 6 | 0 | 4 | 1 (Line) | 2 | 16 | 2 |
| 10-calculadora-pvp | 2 | 49 | 50 | 32 (32) | 41 | 5 | 0 | 0 | 0 | 0 | 0 | 1 |
| 11-dashboard-food-cost-mensual | 2 | 49 | 65 | 14 (14) | 27 | 5 | 0 | 4 | 1 (Bar) | 0 | 13 | 1 |
| BONUS-mermas-inventario | 4 | 92 | 108 | 52 (52) | 32 | 12 | 1 (1) | 0 | 0 | 45 | 0 | 3 |
| **TOTAL** | **71** | **3.120** | **2.321** | **1.569 (737)** | **1.027** | **562** | **58 (30)** | **66** | **2** | **849** | **1.392** | **43** |

«Núm. entrada (verde)» = celdas numéricas con relleno `E8F5E9` (la convención de celda editable del kit).

Comunes a los 12 (medido):
- **Nombres definidos: 0.** Hipervínculos: 0. Imágenes: 0. Comentarios: 0. Macros: 0. `calcChain`: no.
- **Protección de hoja sin contraseña** en 43 de 71 hojas (`prot_password=False` en todas). Las hojas
  `Instrucciones`, `Conversiones` y `Mermas` van sin proteger a propósito. Los rangos de los checklists sí están
  desbloqueados aunque vacíos (06 `Checklist Evento!F5:F40` 36/36; BONUS `Checklist Mermas!A4:F93` 540/540).
- **Paneles inmovilizados** en todas las hojas de datos (`A5` en los escandallos, `B9` calculadora, `B7`
  dashboard, `C5` ventas, `A4` checklist…).
- **Formatos numéricos**: `#,##0.00 €` (todos salvo el 11, que usa `#,##0 €`), `0%`, `0.0%`, `0.000`, `0.###`,
  `+0.0%;-0.0%`, `+0.00;-0.00`, `0`, `0.00`. El único formato de fecha es `dd/mm/yyyy` (09 `Mermas Semanal!B2`, vacía).
- **Impresión**: A4 (`paperSize 9`), ajuste a una página de ancho y pie `AI Chef Pro · aichef.pro · Página &P de &N`
  en todas las hojas (Fase A).
- **Metadatos** (`docProps`): creator `AI Chef Pro`; `title` = «<título> · Kit de Escandallos Pro»;
  `subject` = **«Kit de Escandallos Pro · v1.1»** (desfasado: el contenido es v2.0; defecto menor del ES);
  `keywords` `kit escandallos, AI Chef Pro`; `description` `aichef.pro/kit-escandallos`;
  `category` `AI Chef Pro · Productos digitales`.
- Funciones usadas (todas compatibles con Google Sheets): `IFERROR` 2.095 · `IF` 1.595 · `VLOOKUP` 750 · `SUM` 69 ·
  `NA` 48 · `SUMPRODUCT` 17 · `ROUND` 12 · `AVERAGE` 10 · `COUNTIF` 4 · `ROUNDUP` 2 · `MAX` 1.

### 1.2 Hojas por fichero

| Fichero | Hojas (nombre · rango usado) |
|---|---|
| 01 | `Instrucciones` B2:B63 · `Escandallo` A1:M40 · `Conversiones` A1:C37 · `Mermas` A1:D25 |
| 02 | `Instrucciones` · `1. Aperitivo` · `2. Entrante` · `3. Pescado` · `4. Carne` · `5. Postre` · `6. Pase` · `7. Pase` · `8. Pase` · `9. Pase` (A1:M35 c/u) · `Resumen` B2:C21 · `Conversiones` · `Mermas` |
| 03 | `Instrucciones` · `Primer Plato` A1:M37 · `Segundo Plato` A1:M36 · `Postre` A1:M35 · `Resumen Menú` B2:C16 · `Rotación Semanal` A1:K11 · `Conversiones` · `Mermas` |
| 04 | `Instrucciones` · `Formatos de Compra` A1:E18 · `Gin Tonic Premium` · `Mojito Clásico` · `Margarita` · `Aperol Spritz` · `Conversiones` · `Mermas` |
| 05 | `Instrucciones` · `Tarta Chocolate` A1:M38 · `Croissants` · `Macarons` · `Conversiones` · `Mermas` |
| 06 | `Instrucciones` · `Cocktail (por persona)` A1:M42 · `Presupuesto` B2:C37 · `Checklist Evento` A1:F45 · `Presupuesto Cliente` A2:E17 · `Conversiones` · `Mermas` |
| 07 | `Instrucciones` · `Tostada Aguacate` · `Açaí Bowl` · `Eggs Benedict` · `Carrot Cake` · `Conversiones` · `Mermas` |
| 08 | `Instrucciones` · `Smash Burger` · `Loaded Fries` · `Pulled Pork Sándwich` · `Punto de Equilibrio` A1:E28 · `Conversiones` · `Mermas` |
| 09 | `Instrucciones` B2:B43 · `Mermas Semanal` A1:J24 · `Evolución` A1:E18 |
| 10 | `Instrucciones` B2:B37 · `Calculadora PVP` A1:J21 |
| 11 | `Instrucciones` B2:B35 · `Dashboard` A1:K20 |
| BONUS | `Instrucciones` B2:B40 · `Inventario` A1:J23 · `Ventas del periodo` A1:Q18 · `Checklist Mermas` A1:F96 |

`Conversiones` (A1:C37, 33 parejas) y `Mermas` (A1:D25, 21 categorías × típica/mín/máx) están **duplicadas
idénticas** en los 8 escandallos (01-08).

### 1.3 Validaciones de datos (58 reglas)

| Regla | Dónde | Valores / fórmula | Mensaje de error |
|---|---|---|---|
| Categoría | columna B de cada escandallo (29 reglas en 01-08) | `Mermas!$A$5:$A$25` (**referencia a hoja**) | «Elige una categoría de la lista (hoja «Mermas»).» |
| Unidades | columnas C y F de cada escandallo (29 reglas) | `"kg,g,L,ml,cl,ud,docena,manojo,sobre,lata,botella"` | «Elige una unidad de la lista.» |
| Checklist | 06 `Checklist Evento!F5:F40` | `"✓,—,N/A"` | «Elige ✓, — o N/A.» |
| Motivo | BONUS `Checklist Mermas!D4:D93` | `"Caducidad,Mal estado,Sobreproducción,Error de preparación,Almacenaje incorrecto,Porcionado excesivo,Otro"` | «Elige un motivo de la lista.» |

Ninguna regla usa `prompt`. Español a traducir: 6 unidades (`ud, docena, manojo, sobre, lata, botella`), 7 motivos,
2 mensajes de error y los 21 nombres de categoría de `Mermas` (que viven en celdas, no en la regla).

### 1.4 Formato condicional (66 reglas)

| Regla | Dónde | Fórmula |
|---|---|---|
| Factor desconocido | `G5:G<n>` de cada escandallo (28) | `cellIs equal "?"` |
| Food cost real > objetivo | celda FOOD COST REAL de cada escandallo (28), p. ej. 01 `Escandallo!J40` | `AND(ISNUMBER($J$40),$J$40>$I$32)` |
| Día sobre objetivo | 03 `Rotación Semanal!K5:K11` | `AND(ISNUMBER(K5),K5>'Resumen Menú'!$C$13)` ← **referencia a otra hoja** |
| Tarea hecha | 06 `Checklist Evento!A5:F40` | `$F5="✓"` |
| Semáforo | 09 `Mermas Semanal!I5:I20` (2) · 11 `Dashboard!K7:K19` (2) | `cellIs equal "ALERTA"` / `"OK"` |
| Escala | 09 `Mermas Semanal!G5:G20` | colorScale |
| Huecos de gráfico | 09 `Evolución!D6:E17` · 11 `Dashboard!H7:I18` | `ISNA(D6)` / `ISNA(H7)` |
| FC mensual > objetivo | 11 `Dashboard!H7:H19` | `AND(ISNUMBER(H7),H7>$D$4)` |

⚠️ **Google Sheets** (conocimiento general, **no verificado aquí**): un formato condicional de Sheets no admite
referencias directas a otra hoja (hay que envolverlas en `INDIRECT`). La regla de 03 `Rotación Semanal!K5:K11`
probablemente se pierde o falla al importar. La FAQ de la landing promete «todas las fórmulas se mantienen» en
Sheets y la SERP EN pide Sheets (TIENDA §2): hace falta una prueba real (Chrome de Windows) en el gate de F2.

### 1.5 Gráficos (2)

| Fichero | Tipo | Título | Referencias (XML del gráfico) |
|---|---|---|---|
| 09 | LineChart | «Desperdicio semanal vs objetivo» | `'Evolución'!$A$6:$A$17`, `$D$6:$D$17`, `$E$6:$E$17`, `'Evolución'!D5`, `E5` |
| 11 | BarChart | «Food Cost mensual vs objetivo» | `'Dashboard'!$B$7:$B$18`, `$H$7:$H$18`, `$I$7:$I$18`, `'Dashboard'!H6`, `I6` |

Los dos gráficos citan **su hoja por nombre** y toman los nombres de serie de celdas de cabecera en español. Las
categorías del 11 son los meses **en texto** (`Dashboard!B7:B18` = «Enero»…«Diciembre»).

### 1.6 Fórmulas que citan NOMBRES de hoja (849 celdas)

Patrones (normalizados; `#` = número de fila):

| Fichero | Hoja | Celdas | Patrón | Hojas citadas |
|---|---|---|---|---|
| 01-08 | cada escandallo | `G5:G<n>` (453 en total) | `=IF(C#&F#="","",IFERROR(VLOOKUP(C#&"→"&F#,Conversiones!$A#:$B#,2,FALSE),"?"))` | `Conversiones` |
| 01-08 | cada escandallo | `H<filas vacías>` (297) | `=IFERROR(VLOOKUP(B#,Mermas!$A#:$C#,2,FALSE),"")` | `Mermas` |
| 02 | `1. Aperitivo`…`9. Pase` | `I27` ×9 | `=Resumen!$C#` | `Resumen` |
| 02 | `Resumen` | `C5:C13` | `=IF('1. Aperitivo'!$J#=0,"",'1. Aperitivo'!$J#)` … `'9. Pase'` | las 9 de pase |
| 03 | `Primer Plato` I29 · `Segundo Plato` I28 · `Postre` I27 | 3 | `='Resumen Menú'!$C#` | `Resumen Menú` |
| 03 | `Resumen Menú` | `C5:C7` | `='Primer Plato'!$J#` · `='Segundo Plato'!$J#` · `='Postre'!$J#` | 3 |
| 03 | `Rotación Semanal` | `C5`,`E5`,`G5`, `H5:H9`, `J5:J9` | `='Primer Plato'!$J#`… `='Resumen Menú'!$C#+…` | 4 |
| 04 | 4 pestañas de cóctel | `D5`/`D6` (6) | `=IFERROR('Formatos de Compra'!$D#,"")` | `Formatos de Compra` |
| 06 | `Presupuesto` C6 · `Presupuesto Cliente` C8:D8 | 3 | `='Cocktail (por persona)'!$J#` · `=IFERROR('Presupuesto'!C#,"")` | 2 |
| 08 | `Punto de Equilibrio` | `B16:C18` (6) | `=IF('Smash Burger'!$I#="",'Smash Burger'!$J#,'Smash Burger'!$I#)`… | `Smash Burger`, `Loaded Fries`, `Pulled Pork Sándwich` |
| 09 | `Evolución` | `B6`, `C6` | `='Mermas Semanal'!E#` / `F#` | `Mermas Semanal` |
| BONUS | `Inventario` | `G5:G19` (15) | `=IFERROR(IF('Ventas del periodo'!C#=0,"",'Ventas del periodo'!C#),"")` | `Ventas del periodo` |
| BONUS | `Ventas del periodo` | `C3:Q4` (30) | `=Inventario!B#` / `=Inventario!A#` | `Inventario` |

Más: **29 DV** (`Mermas!$A$5:$A$25`), **1 CF** (03 `Rotación Semanal`), **2 gráficos**, las **áreas de impresión**
(`'Escandallo'!$A$1:$J$40`… en las 71 hojas, con el nombre entre comillas) y **textos de instrucciones** que citan
pestañas por su nombre («Ve a la pestaña 'Escandallo'», «en «Presupuesto»!C5», «pestaña «Ventas del periodo»»…).
Nombres de hoja referenciados que habría que traducir de forma consistente: `Conversiones`, `Mermas`, `Resumen`,
`1. Aperitivo`…`9. Pase`, `Resumen Menú`, `Primer Plato`, `Segundo Plato`, `Postre`, `Formatos de Compra`,
`Cocktail (por persona)`, `Presupuesto`, `Smash Burger`, `Loaded Fries`, `Pulled Pork Sándwich`, `Mermas Semanal`,
`Evolución`, `Dashboard`, `Ventas del periodo`, `Inventario`.

### 1.7 Fórmulas con literales de texto (1.392 celdas)

| Literal | Celdas | Dónde | ¿Traducir? |
|---|---|---|---|
| `"?"` | 906 (+28 reglas CF) | escandallos 01-08, `G` y `J` | No (universal) |
| `"→"` | 453 | escandallos 01-08, `G` (clave de `Conversiones`) | No (U+2192; mantener idéntico en claves) |
| `"revisa merma"` | 453 | escandallos 01-08, `I5:I<n>`: `=IFERROR(IF(E#="","",E#/(1-H#)),"revisa merma")` | **Sí** |
| `"revisa unidades"` | 453 | escandallos 01-08, `J5:J<n>`: `=IF(G#="?","revisa unidades",IFERROR(I#*D#/G#,""))` | **Sí** |
| `"OK"` / `"ALERTA"` | 29 + 2 reglas CF | 09 `Mermas Semanal!I5:I20`: `=IFERROR(IF(G#="","",IF(G#<=C#,"OK","ALERTA")),"")` · 11 `Dashboard!K7:K19` | **`ALERTA` sí** (y la CF que lo compara) |
| `"✓"` | 1 + 1 CF | 06 `Checklist Evento!D42`: `=COUNTIF(F5:F40,"✓")` | No |
| `"?*"` | 1 | 06 `Checklist Evento!F42`: `=COUNTIF(B5:B40,"?*")` | No (comodín) |
| `">0"` | 2 | 03 `Rotación Semanal!I11:J11`: `=IFERROR(SUM(I5:I9)/COUNTIF(I5:I9,">0"),"")` | No |

⚠️ Si se traduce `ALERTA`, hay que cambiar a la vez la fórmula de 29 celdas **y** las 2 reglas CF que colorean por
igualdad de cadena; si no, el semáforo deja de pintarse sin dar error.

### 1.8 Variables de mercado por fichero (muestras reales)

**Comunes a los escandallos 01-08** (misma rejilla del motor v2.0):
- IVA en celda editable `Tipo de IVA (%)` = **0,10** (01 `Escandallo!I34`; en cada hoja de escandallo, fila «Tipo de
  IVA (%)») y texto de `Instrucciones` (01 `B33`): «10 % en hostelería en España; cámbialo si te aplica otro tipo
  (IGIC en Canarias, o el IVA/ITBIS/IVU de tu país en Latinoamérica)». Filas «PVP SUGERIDO (sin IVA)», «PVP CON IVA».
- `Coste elaboración (%)` = 0,10 (01 `I27`), `Food Cost objetivo (%)` = 0,30 (01 `I32`), `Nº de raciones` = 1 (`I29`).
- Unidades: métricas + `ud, docena, manojo, sobre, lata, botella`; formatos por defecto **botella 70 cl** (vino 75) y
  **lata 33 cl**, manojo ≈ 30 g, sobre ≈ 10 g (`Conversiones!A5:C37`).
- `Mermas` (21 categorías): Carne roja 20 %, Aves 25 %, Pescado 35 %, Marisco 45 %, Verdura hoja 25 %, raíz 12 %,
  fruto 10 %, Fruta 15 %, Lácteos 3 %, Secos/granos 2 %, Congelados 7 %, Pan/bollería 5 %, Huevos 11 %,
  Aceites/grasas 3 %, Especias/hierbas 20 %, Chocolate/cacao 5 %, Bebidas/licores 2 %, Setas/hongos 20 %,
  Conservas/encurtidos 8 %, Salsas/condimentos 5 %, Pasta/arroz 2 % (+ mín/máx; 01 `Instrucciones!B51:B56`).
- Línea de versión: «Versión 2.0 · agosto 2026 · aichef.pro/kit-escandallos · info@aichef.pro»; «© 2026 AI Chef Pro ·
  Todos los derechos reservados»; «Kit de Escandallos Pro — AI Chef Pro»; `www.aichef.pro`.
- Rótulos de la zona de foto: «📷 Foto del Plato», «Revisar → Desproteger hoja, luego Insertar → Imagen» (rutas de
  menú de **Excel en español**).

| Fichero | Platos / ingredientes de ejemplo (precio en €, unidad) | Otras variables de mercado |
|---|---|---|
| 01 | Solomillo con PX y Espárragos: solomillo de ternera 28,5 €/kg, patata agria 1,8, espárrago verde 6,5, mantequilla 9, **vino Pedro Ximénez** 8,5 €/L, fondo oscuro 12 €/L, AOVE 7,5 €/L, flor de sal 15 €/kg, pimienta 25, microgreens 70 €/kg | — |
| 02 | Tartar de atún rojo (42 €/kg), Vieira con coliflor y **trufa negra 800 €/kg**, Lubina con beurre blanc (32), **Carrillera ibérica** al vino tinto (18), Esfera de chocolate 70 % | 9 pases, FC objetivo único en `Resumen!C12` |
| 03 | **Menú del Día**: Ensalada mediterránea (queso feta 12 €/kg, AOVE), Pollo al horno (contramuslo 5,5), **Flan casero** (huevo campero 3,6 €/docena) | `Resumen Menú`: pan 0,15 €/comensal, bebida 0,40, café 0,20, **FC objetivo 33 %** (`C13`), IVA 10 % (`C15`); `Rotación Semanal` L-V |
| 04 | Gin Tonic Premium (5 cl), Mojito (6 cl), Margarita, Aperol Spritz; hielo 0,5 €/kg | `Formatos de Compra`: **botellas 70 cl** (destilados) / **75 cl** (vino, prosecco): ginebra 19,60 €, ron 10,50, tequila 15,40… ; «Merma y hielo» 5 %; FC de bar 20-25 % |
| 05 | Tarta chocolate 70 % (12 raciones), Croissants (20 ud; mantequilla 82 % MG 12 €/kg), Macarons (30 ud; colorante 4 €/bote) | Mermas de obrador 12 % cobertura / 8 % harinas |
| 06 | Cocktail por persona: **jamón ibérico 65 €/kg, queso manchego 16**, salmón, langostino, **croquetas** 0,35 €/ud… | `Presupuesto`: 50 pax, **1 camarero/22 pax**, 5 h × **16 €/h**, jefe de sala 6 h × **22 €/h**, menaje 1,20 €/pax, transporte 150 €, montaje 200 €, FC comida 35 %, margen servicios 20 %, **mínimo 600 €**, IVA 10 %. `Checklist Evento`: 30 tareas, entre ellas «**Registro sanitario y carnés de manipulador al día**», «Seguro de responsabilidad civil», «Autorización del espacio y horario de música», alérgenos (sin cifra de «14»). `Presupuesto Cliente!A15`: «válido 30 días… **Precios con IVA incluido**… confirmación 7 días antes» |
| 07 | Tostada de aguacate (pan masa madre 0,60 €/ud), Açaí bowl (22 €/kg), Eggs Benedict, Carrot cake (tanda de 12, molde 20 cm) | FC cafetería 25-30 % |
| 08 | Smash burger (blend 80/20 9,5 €/kg), Loaded fries, Pulled pork sándwich | `Punto de Equilibrio` €/día: plaza/canon 60, seguros-licencias-tasas 25, combustible/generador 35, personal 140 (2 × jornada), amortización 30, limpieza 10; mix 50/25/25 %; IVA 10 % (`B25`) |
| 09 | 16 familias de desperdicio con objetivo mín/típico/máx (secos 2-3 %, carne/pescado 3-5 %, verdura/fruta 5-8 %, bebidas 1-2 %); compras de ejemplo 1.850 €, 1.240 €… | fecha `dd/mm/yyyy`, «Semana 2…12», objetivo global 4 % (`Evolución!B3`) |
| 10 | coste 5,50 € (`C4`) | IVA 10 % (`C5`); 10 tipos: Fine Dining 25-28 %, Casual 28-32, Fast Casual 30-35, **Cafetería** 25-30, Catering 30-40, Food Truck 28-35, Hotel F&B 30-35, **Pastelería** 20-30, **Bar/Cócteles** 20-25, **Delivery** 28-32 % sobre neto con **comisión 30 %** (`F18`); textos «Glovo o Uber Eats» (`Instrucciones!B21`) |
| 11 | stock/compras/ventas de ejemplo 1.000/5.000/1.200/16.000 € | **Año 2026** fijo (`D3`), FC objetivo 30 % (`D4`), meses en español, «divídelas entre 1,10» (`Instrucciones!B18`) |
| BONUS | 15 productos en kg/L/**docena** (solomillo 26 €, lubina 14 €, huevos 3,60 €/docena…); platos «Solomillo al Pedro Ximénez», «Lubina a la plancha», «Ensalada de la casa» | registro de 90 líneas, 7 motivos (DV) |

**Normativa española citada en los xlsx: ninguna** por número (sin RD, Reglamento ni BOE). Lo más «español» es
fiscal (IVA 10 %, IGIC) y de sector (menú del día, carné de manipulador, Glovo).

### 1.9 Dimensión de la traducción

| Medida | Valor |
|---|---|
| Cadenas únicas del kit (celdas, nombres de hoja, mensajes DV, ítems de lista, títulos de gráfico, pies) | **832** |
| Palabras (sobre cadenas únicas) | **6.698** |
| Caracteres | 36.848 |
| Cadenas presentes en ≥ 8 ficheros (Instrucciones comunes, rejilla, `Conversiones`, `Mermas`) | 154 |
| Por fichero (cadenas / palabras) | 01: 188/1.211 · 02: 225/1.438 · 03: 229/1.485 · 04: 215/1.588 · 05: 204/1.389 · 06: 314/2.118 · 07: 214/1.321 · 08: 226/1.500 · 09: 82/764 · 10: 50/641 · 11: 52/443 · BONUS: 92/703 |
| Metadatos por fichero | `title`, `subject`, `keywords`, `description`, `category` + pie de página |

---

## 2. ¿Fuente de verdad = generador o ficheros publicados?

### 2.1 Historia (git)

| Commit | Fecha | Qué hizo con los xlsx |
|---|---|---|
| `00c7043` | 2026-03-16 | `scripts/generate-escandallos.py` crea los 12 xlsx en `public/dl/kit-escandallos/` (v1.0) |
| `09e386d` | 2026-03-18 | Arreglo de una fórmula de catering y regeneración. **Último cambio del generador.** |
| `7e050c5` | 2026-08-08 | `git mv public/dl → astro-site/public/dl` (rename 100 %, byte a byte) |
| `d42bcf8` | 2026-08-22 11:12 | **Fase A (v1.1)**: `postprocess-transversal.py` + `inject_cache.py` sobre 57 xlsx: cache de valores, A4, metadatos, bio anclada, línea de versión, 9 fórmulas de la calculadora reparadas |
| `ed45f35` | 2026-08-22 17:11 | **v2.0**: `kit-escandallos-v2_0/main.py` (motor + grupo_a/b/c) reescribe los 12 xlsx + crea el bono PDF |
| `ad37925` | 2026-09-03 | Solo el PDF (y su .md): IVA del alcohol en sala 10 % |

`git log` de la carpeta no muestra ninguna otra edición de los xlsx después de `ed45f35`; las fechas de
modificación en disco (22-ago 17:09-17:10) coinciden.

### 2.2 El generador no reproduce el kit publicado

- `scripts/generate-escandallos.py:54-57` escribe en `<repo>/public/dl/kit-escandallos`, que **ya no existe**
  (se movió en `7e050c5`). Ejecutarlo hoy recrearía una carpeta muerta con la v1.0.
- Comparación de textos (literales `ast` del generador y de los 5 scripts de `kit-escandallos-v2_0/` contra las
  832 cadenas de los xlsx):

| Origen de la cadena publicada | Cadenas |
|---|---|
| Solo en el generador v1.0 (nombres de plato, ingredientes, cabeceras de la rejilla…) | 124 |
| En el generador **y** en los scripts v2.0 | 155 |
| Solo en los scripts v2.0 (Instrucciones reescritas, hojas nuevas, bloques de resultado…) | **490** |
| Por fragmento (f-strings/concatenaciones) en v2.0 / en el generador | 14 / 3 |
| Compuestas por f-string (`f"📋 {titulo}"` en `generate-escandallos.py:109`, `f'Semana {i + 1}'` en `grupo_c.py:475`…) | 45 |
| Solo en `postprocess-transversal.py` (Fase A) | 1 (`✓`) |

- Del otro lado: de los **253 literales de texto** (> 12 caracteres) del generador, **97 ya no están** en los xlsx
  (p. ej. «▸ El food cost objetivo en bar suele ser 18-25%», «Selecciona una categoría válida», «Personal de servicio
  (camareros)», «Bar/Cocktails», «Arrastra aquí la foto del plato terminado»): la v2.0 los sustituyó.

### 2.3 Y el pipeline v2.0 tampoco es un generador

`kit-escandallos-v2_0/main.py:1-35` lo dice: es un **post-proceso** que copia `astro-site/public/dl/kit-escandallos`
a una carpeta de trabajo (`ORIGEN`, `main.py:57`) y le aplica `grupo.pre → motor.aplicar → grupo.post →
motor.cerrar` fichero a fichero (`procesar()`, `main.py:227-260`), después `inject_cache.py`. Necesita la estructura v1.1 (o la v2.0,
sobre la que es idempotente según el mensaje de `ed45f35`: «idempotencia 0 diferencias»; no lo he re-ejecutado).
Los nombres de plato, ingredientes y precios que vienen del generador v1.0 **no están en el motor**: están en los
ficheros. Además `main.py:58-61` tiene un `SCRATCH` por defecto apuntando a una sesión antigua (usar
`CLAUDE_SCRATCHPAD` si se reutiliza) y el gate del bono (`main.py:161-164`) **exige tildes, ñ, € y «»** en el PDF.

### 2.4 Conclusión (decide la F2)

**Duplicar los 12 xlsx PUBLICADOS** y aplicarles una **capa de mercado EN** (script nuevo, idempotente, en
`scripts/productos-digitales/recipe-costing-kit/`), en este orden:

1. copia `dl/kit-escandallos/*.xlsx` → carpeta de trabajo;
2. **mapa de nombres de hoja** ES→EN y reescritura de TODAS las referencias: 849 fórmulas, 29 DV, 1 CF, 2 gráficos
   (XML), áreas de impresión y textos que citan pestañas;
3. **mapa de claves-dato** (21 categorías, 11 unidades, 33 claves de `Conversiones`, 7 motivos, `✓,—,N/A`) aplicado a
   la tabla, a los desplegables y a las filas de ejemplo a la vez;
4. traducción de las 832 cadenas por diccionario (celdas, mensajes DV, títulos de gráfico, pies, metadatos) —
   el texto EN lo redactan **subagentes Anthropic** (regla 1bis del CLAUDE.md global: nada de `bridge.py` en productos);
5. literales en fórmulas (`revisa merma`, `revisa unidades`, `ALERTA` + sus 2 CF);
6. variables de mercado (§1.8): moneda, impuesto, unidades/`Conversiones` imperiales, ejemplos, benchmarks, papel,
   formato de fecha, meses, año fijo;
7. `inject_cache.py` **al final** (cualquier `save()` posterior borra el cache);
8. gates.

Por qué no «motor v2.0 + parámetro `mercado` + regenerar ES idéntico» (lo que sugiere TIENDA §4 F2): el motor no
genera, parte de un fichero; sin un v1.1 EN de entrada no hay de dónde partir, y los textos de origen v1.0 (279
cadenas) no están en ningún `textos_es.py`. El gate equivalente, y más útil, es **de paridad estructural EN↔ES**:
mismas hojas (vía el mapa de nombres), misma fórmula celda a celda **salvo** el mapa de hojas y de literales, mismas
DV/CF/merges/protección/paneles/área de impresión, y valores cacheados coherentes (`data_only`). La identidad ES está
garantizada porque los ficheros ES no se tocan.

Decisiones de diseño que hay que cerrar en F1 antes de escribir el script:
- **Moneda como parámetro**: un formato numérico de Excel no puede leer una celda. Opciones: (a) formato neutro
  (`#,##0.00`) + código de moneda en las cabeceras con fórmula (`="Price/Unit ("&Settings!$B$2&")"`); (b) `$`
  fijo. (a) cumple TIENDA §1 («moneda es parámetro del Excel»); (b) es más simple. Las cabeceras hoy son texto.
- **Unidades**: métrico con `$` o imperial (lb/oz/fl oz/qt/gal) como ejemplo principal. Si imperial, `Conversiones`
  gana parejas (`lb→oz`, `lb→kg`, `oz→g`, `gal→fl oz`, `qt→fl oz`, `fl oz→ml`…) y los precios pasan a $/lb.
- **Impuesto**: en EE. UU. el precio de carta va SIN sales tax (lo suma el ticket) y el tipo varía por estado/ciudad;
  en Reino Unido el precio de carta lleva IVA y la restauración va al tipo general. Afecta a filas «PVP CON IVA» y al
  «Presupuesto Cliente» del 06. [conocimiento general — verificar en el research de F1]
- **Papel**: US Letter vs A4 (ver gate `censo-entregables.py:240`, §6).
- **Versión** del kit EN (¿1.0?) y su línea «Version … · aichef.pro/en/digital-products/recipe-costing-kit».

---

## 3. El PDF bonus («Guía: Controla tu Food Cost en 30 Días»)

| Campo | Valor |
|---|---|
| Fuente | `scripts/productos-digitales/kit-escandallos-v2_0/bono-guia-food-cost-30-dias.md` (664 líneas, **7.478 palabras**) |
| Maquetador | `kit-escandallos-v2_0/bono_guia.py` (Markdown → PDF con reportlab A4 + DOCX con python-docx) |
| Cómo se produjo | texto con `bridge.py` (SPEC §5) en `ed45f35`; re-maquetado desde el mismo .md en `ad37925` |
| Salida | `astro-site/public/dl/kit-escandallos/BONUS-guia-food-cost-30-dias.pdf`, **17 páginas** (pypdf), `/Title` «Guía: Controla tu Food Cost en 30 Días», Producer ReportLab. El .docx va fuera de la carpeta de entrega a propósito (`main.py:74-76`) |
| Estructura | 17 tablas Markdown, 7 bloques de código/fórmula |

Esquema (H2): 1. Introducción · 2. Semana 1 — Medir (inventario valorado, registro de compras, cálculo, «¿es bueno o
malo tu food cost?») · 3. Semana 2 — Escandallar (top-10, escandallo, mermas, FC por plato, ingeniería de menú) ·
4. Semana 3 — Negociar (7 tácticas, guion con proveedor, errores) · 5. Semana 4 — Controlar (rutinas diaria/semanal,
alertas) · 6. Checklist semanal de las 4 semanas · 7. Caso práctico (32 % declarado → 35 % real → 32 % en 30 días) ·
8. FAQ (6) · 9. Cierre. Firma: «John Guerrero — chef y consultor gastronómico desde 2010, en cocina desde los 17 años ·
johnguerrero.es» (`.md:664`).

Mercado español dentro del PDF:
- **98 importes en €**; tablas con proveedores y platos españoles (lomo de merluza, **carrillera ibérica**, pulpo a la
  brasa, **tomate raff**, «Carnes del Norte», «Frutas y Verduras SL»); TPV; albarán.
- **IVA**: «en España, la hostelería aplica el 10 % de IVA» (`.md:82`), «divide entre 1,10» (`.md:51`, `.md:110`) y la
  FAQ 4 con **«art. 91.Uno.2.2.º de la Ley del IVA»** (10 % en sala, 21 % para llevar) (`.md:630-632`).
- **Benchmarks** «como referencia para España en 2026» (`.md:134-139`): alta cocina 28-33 %, mediterránea 25-30 %,
  pizzería 22-27 %, fast food 20-25 %.
- **Venta cruzada a un producto solo-ES**: «Guía Food Cost + Ingeniería de Menú … (aichef.pro/guia-food-cost-ingenieria-menu)»
  (`.md:254`) — en EN hay que quitarla o apuntarla a algo que exista en inglés.
- **Nombres de fichero y de pestaña citados** en el cierre (`.md:652-656`: «01-escandallo-estandar.xlsx, pestaña
  «Escandallo»», «09… «Mermas Semanal»… «Evolución»», «11… «Dashboard»», «10… «Calculadora PVP»», «BONUS… «Inventario»»):
  tienen que coincidir con los nombres EN finales.

`bono_guia.py` tiene español cableado que hay que parametrizar al duplicarlo: cabecera «AI Chef Pro · Kit de
Escandallos Pro» y pie «Página {n}» (`bono_guia.py:350-351`), `title='Guía: Controla tu Food Cost en 30 Días'`
(`:451`), y la detección del bloque de metadatos por el literal **«Bono del Kit»** (`:468-470`; un .md inglés no casaría
y el subtítulo saldría duplicado). El saneado WinAnsi (`:36-60`) sirve igual en inglés.

---

## 4. Landing

### 4.1 Piezas

| Fichero | Estado para EN |
|---|---|
| `astro-site/src/pages/kit-escandallos.astro` | Wrapper ES: `lang='es'`, `stripeLink = import.meta.env.VITE_STRIPE_PAYMENT_LINK_ESCANDALLOS` (`:17`), `whatsapp={false}`, `omitGlobalApp` (`:21-22`), **`locales={['es']}`** (`:28`). Cuando EN esté vivo debe pasar a `alternatesFamilia('kit-escandallos')` (`tienda.ts:102-118`) o no habrá hreflang ES→EN (y `tienda-gate --base` lo exige en los dos sentidos) |
| `astro-site/src/components/pages/KitExcelLandingPage.astro` (903 líneas) | **Ya parametrizada** (0.B): prop `lang` (`:41-44`), diccionario `ui` de `i18n/tienda/<lang>.json` (`:46-48`), moneda del JSON-LD desde `TIENDAS[lang].moneda` (`:98`), ruta canónica con `tiendaProductoPath` (`:50-52`), breadcrumb con `ui.homeHref` (`:143`), testimonios opcionales (`:151`, `:255`, `:385`). No queda texto de interfaz en español cableado en el marcado (medido: solo `alt` en inglés y nombres propios) |
| `astro-site/src/i18n/tienda/en.json` | **Existe**, 44/44 claves iguales que `es.json` (`homeHref /en`, `hubBackLabel ← Digital Products`, `authorBadgesDefault`, `cryptoRefundNote`…) |
| `astro-site/src/data/productos/kits/types.ts` | Tipo `KitExcelData`; ya documenta que sirve para `data/productos-en/kits/<slug>.ts` (`:32-36`) y que `testimonials` es opcional (`:258-265`) |
| `astro-site/src/data/productos/kits/kit-escandallos.ts` (312 líneas) | Datos ES a duplicar en `astro-site/src/data/productos-en/kits/recipe-costing-kit.ts` (**la carpeta no existe**) |

### 4.2 Campos de datos (`kit-escandallos.ts`) — qué hacer en EN

| Campo (línea) | Contenido ES | EN |
|---|---|---|
| `slug` (11) | `kit-escandallos` | **Adaptar**: `recipe-costing-kit` (reservado en `tienda.ts:94`) |
| `stripeEnvKey` (12) | `VITE_STRIPE_PAYMENT_LINK_ESCANDALLOS` | **Nuevo** (p. ej. `VITE_STRIPE_PAYMENT_LINK_RECIPE_COSTING_KIT`); John crea el link USD |
| `seo.title/description/keywords` (15-19) | «Kit Escandallos Pro…», «Solo 12 euros» | **Adaptar** con el research US/UK (TIENDA §2: *food cost template*, *recipe costing template*, *food cost spreadsheet*…) |
| `seo.ogImage` (20) | `og-kit-escandallos.jpg` | **Nueva imagen**: la actual lleva texto ES incrustado, «€12», «Imprimible A4» y un «Checklists Operativos Pre-Rellenados» que ni siquiera es de este kit (visto) |
| `schema.productName/Description` (24-26) | ES | Traducir |
| `schema.price` (27) | `'12.00'` | **Adaptar**: USD (TIENDA §5: $19, se confirma en F1). `sync-product-prices.py` lo lee de aquí |
| `schema.priceValidUntil` (28) | `2026-12-31` | Reutilizar/revisar (caduca en 3 meses) |
| `schema.aggregateRating` (29-34) | 4,9 / 10 | **QUITAR** (§3.5) |
| `schema.reviews` (35-51) | 3 reseñas ES | **QUITAR** |
| `schema.faqs` (53-78) | 6 FAQ cortas | Traducir; guion PAA de TIENDA §2 (*Is 30% a typical food cost?*…). Ojo con «todas las fórmulas se mantienen» en Sheets (§1.4) |
| `schema.breadcrumbName` (79) | «Kit de Escandallos Pro» | Traducir |
| `images.*` (82-104) | 6+6 fotos de galería, 3 fondos | **Reutilizar** (van con `alt=""`; son platos, varios españoles: croqueta, cochinillo, gambas al ajillo, torrija — decisión estética, no técnica) |
| `hero.badge` (108) | «El kit #1 de escandallos…» | **Decide John** (claim «#1», COM-28 aparcado en ES) |
| `hero.title*`, `description`, `checkItems` (109-122) | ES | Traducir |
| `hero.ctaLabel` (123) | «COMPRAR AHORA — €12» | Adaptar (precio USD) |
| `compatApps` (126-130) | HTML con `<a href="https://aichef.pro">` | Traducir; enlace a `/en` |
| `grid.*` (132-151) | 11 tarjetas | Traducir y adaptar (menú del día, IVA, cl…) — deben describir los xlsx EN reales |
| `why.*` (153-173) | 4 razones + pills | Traducir |
| `authorBio` (175-176) | «CEO de AI Chef Pro… desde los 17 años… desde 2010…» | Traducir sin sumar cifras (bio anclada) |
| `authorBadges` (177) | ES | Omitir → cae a `ui.authorBadgesDefault` EN |
| `bonus.subtitle` (183) + `items[].value` (189, 197) | «valorados en €46», «€27», «€19» | **Decide John**: ancla de valor en USD o sin valor |
| `bonus.items[].image` (191, 199) | focaccia, hogaza | Reutilizar |
| `buyBox.ctaLabel` (205) | «SÍ, QUIERO EL KIT — €12» | Adaptar |
| `guarantee.text/stats` (210-216) | 30 días / 100 % / «0 Preguntas incómodas» | Traducir (la garantía se mantiene: §3.5) |
| `faqs` on-page (220-245) | 6 | Traducir |
| `cta.*` (247-263) | «…por menos de lo que cuesta un menú del día» | Adaptar (el «menú del día» no existe en US/UK) |
| `testimonials` (265-280) | 10 testimonios ES | **QUITAR** (el campo es opcional; sin él no se pintan marquee ni avatares con estrellas) |
| `pricing.priceOld/discountBadge` (283-285) | «€49», «-75%» | **Decide John** (ancla de precio sin precio anterior real en EN) |
| `pricing.heroNote/buyBoxNote` (286-287) | «Precio especial de lanzamiento. Sube pronto» | **Decide John** (urgencia) |
| `pricing.bonusTotalLabel/bonusSaveLine` (288-289) | «€95…», «¡Ahorra €37 HOY!» | **Decide John** |
| `stickyLabel`, `stickyVariant` (292-293) | «KIT ESCANDALLOS — €12», `v1` | Adaptar / reutilizar |
| `footerLinks` (295-303) | 4 productos **solo ES** | **Adaptar**: `/en`, `/en/digital-products`, herramientas EN (`/en/food-cost-calculator-restaurant`, `/en/ai-food-cost-calculator`), contacto |
| `updateNote` (304) | «Producto actualizado · Versión 2.0 · agosto 2026» | Adaptar a la versión EN |
| `alreadyBought` (306-309) | `product: 'kit-escandallos'` | **Adaptar**: `recipe-costing-kit` + label EN (el form llama a `resend-access` con ese id) |

### 4.3 Tres puertas cripto (`CryptoPayButton.astro`, 937 líneas)

- La plantilla monta `hero` (`KitExcelLandingPage.astro:317-323`), `buybox` (`:576-582`) y `cta` (`:667-673`), con
  `productName` = `productLabel` de `zona-app.ts` (`:61-63`) y `cryptoEnabledFor(data.slug)` (`:65`).
- **El componente no tiene `lang`** (`CryptoPayButton.astro:59-72`): todo el copy es español — «Pago con
  criptomonedas», «Paga con cripto · paso 1 de 2», «Tu email (ahí te enviamos el acceso)», «País de facturación»,
  lista de países con nombres en español (`:85-110`), enlace a **`/terminos`** (ES) (`:498`), «Continuar al pago»,
  8 mensajes de error (`:759-766`). ~189 líneas con caracteres españoles.
- Con `CRYPTO_PRODUCTS=all` las puertas aparecen solas en la landing EN (`crypto-checkout.ts` de `lib`, `:45`).
  TIENDA §6 ya lo avisa: o existe `/en/crypto-payment` y el botón habla inglés, o el producto va a
  `CRYPTO_PRODUCTS_EXCLUDE`.

---

## 5. Access gate + dashboard

| Pieza ES | Qué es | ¿Tiene `lang`? | Español dentro |
|---|---|---|---|
| `src/pages/KitEscandallosAccessGate.tsx` (90 líneas) | Gate **vanilla** (no usa el compartido): `verify-purchase` con `product:'kit-escandallos'`, guarda `kit-escandallos-jwt`, navega a `/kit-escandallos-library` | No | título, «Verificando tu compra…», error, «Volver al Kit de Escandallos» |
| `src/components/shared/ProductAccessGate.tsx` (129) | Gate compartido de 48 productos | **Sí** (0.B): `lang?: 'es'|'en'` y `COPY.en` (`:12-35`) | — |
| `src/components/shared/ProtectedRoute.tsx` (27) | Redirige si no hay JWT (`storageKey`, `redirectTo`) | No hace falta | — |
| `src/pages/KitEscandallosDashboard.tsx` (192) | `TEMPLATES` (13 tarjetas con claves de descarga, `:15-29`), `useAuth('kit-escandallos-jwt')`, `get-download-urls` | No | ~40 cadenas: títulos/descr. de las 13 tarjetas, «Tu Dashboard», «Tus 11 plantillas + 2 bonus…», «Descargar», «Disponible pronto», «Compatibles con Excel, Google Sheets…», venta cruzada «Ver Pro Prompts eBook — €9» (`:170`, producto ES), pie |
| `src/components/shared/SaasDiscoveryBanner.tsx` | banner del SaaS | No | «Estos productos digitales complementan…», «+55 aplicaciones» |
| `src/components/shared/ProductChangelog.tsx` | versión + novedades (`productos-changelog.ts:321`) | No | «Versión», «Actualizado», «Novedades y mejoras», «Tu acceso es de por vida…» |
| `src/components/shared/LogoBadge.tsx` | logo + migas | No | enlace a `/productos-digitales` (`:20`) |
| `src/components/shared/WhatsAppProductSupport.tsx` | botón WhatsApp del dashboard | No | «Hola, necesito ayuda con mi compra…» (`:13`), `aria-label="Soporte por WhatsApp"` (`:22`) |

**Wrappers `.astro`**: los 50 ES los genera `scripts/astro-migration/fase5-generate-zona-app.py` desde `zona-app.ts`
(plantillas `ACCESS_TPL`/`ISLAND_TPL_PROPS`/`LIBRARY_TPL`, `:40-122`). Desde la 0.B **salta** las entradas con
`lang` ≠ `es` (`:176-186`): los wrappers EN se escriben **a mano**. Los ES: `pages/kit-escandallos-access.astro`
(`BaseLayout title={ACCESS_TITLE} noindex` + `FunctionsOriginPatch` + gate `client:only`) y
`pages/kit-escandallos-library.astro` (`noindex whatsapp={false}` + `islands/library/KitEscandallosLibraryIsland.tsx`
= `ProtectedRoute` + dashboard). `ACCESS_TITLE` es español (`zona-app.ts:55`); el shim de Helmet anula el `<title>`
del cliente, así que el título EN tiene que ir en el `BaseLayout` del wrapper. La navegación del gate funciona en
rutas anidadas: el shim `astro-site/src/islands/shims/react-router-dom.tsx:60-61` usa `window.location`.

Cómo quedaría lo anidado (siguiendo `tienda.ts:74-80` y lo que exige `tienda-gate.py:219-230`):
- `astro-site/src/pages/en/digital-products/recipe-costing-kit.astro` (o `…/recipe-costing-kit/index.astro`): landing.
- `astro-site/src/pages/en/digital-products/recipe-costing-kit/access.astro`: `BaseLayout lang="en" title="Verifying
  access... | AI Chef Pro" noindex` + `FunctionsOriginPatch` + `ProductAccessGate client:only="react"` con
  `productId='recipe-costing-kit'`, `storageKey='recipe-costing-kit-jwt'`,
  `dashboardPath='/en/digital-products/recipe-costing-kit/library'`, `landingPath='/en/digital-products/recipe-costing-kit'`,
  `productLabel`, `lang='en'` (reutiliza el gate compartido que ya habla inglés; no hace falta un gate nuevo).
- `…/recipe-costing-kit/library.astro`: `noindex whatsapp={false} miselup={false}` + island nuevo
  (`ProtectedRoute storageKey='recipe-costing-kit-jwt' redirectTo='/en/digital-products/recipe-costing-kit'`) + el
  dashboard EN = **copia traducida** de `KitEscandallosDashboard.tsx`.
- Imports con un nivel más de `../` que los ES.

**Claves de descarga ↔ `netlify/functions/get-download-urls.ts:5-18`**: `estandar, degustacion, menu-dia, cocktails,
pasteleria, catering, cafeteria, food-truck, mermas, calculadora-pvp, dashboard, bonus-mermas, bonus-guia` → rutas
`/dl/kit-escandallos/…`. La function lee `payload.product` del JWT (`:870-872`) y devuelve `PRODUCT_FILES[product]`
(`:889`). Para EN: entrada `'recipe-costing-kit'` con las MISMAS claves (las del `TEMPLATES` del dashboard) y rutas
`/dl/recipe-costing-kit/<nombre-en>.xlsx|pdf`. Los ficheros de `/dl/` son estáticos y públicos (no hay `Disallow`
de `/dl/` en `robots.txt` ni cabeceras en `_headers`): igual que en ES.

---

## 6. Backend

### 6.1 Dónde se registra el productId EN

| # | Fichero | Entrada ES | Qué hace falta en EN | Preparado por la 0.B |
|---|---|---|---|---|
| 1 | `astro-site/src/lib/zona-app.ts:58` | registro de la zona app | entrada `recipe-costing-kit` con rutas anidadas y **`lang: 'en'` al final** (el regex del generador espera los 8 primeros campos en orden) | campo `lang?` (`:44-50`); el generador lo salta |
| 2 | `netlify/functions/verify-purchase.ts:25-31` | `PRODUCTS` (email de acceso) | `accessPath` anidado, asunto/título/cuerpo/CTA en inglés, `lang: 'en'` | `lang?: TiendaLang` (`:9-15`), `emailI18n(config.lang)` en el envoltorio (`:492`) |
| 3 | `netlify/functions/resend-access.ts:26` | `PRODUCTS` («¿Ya compraste?») | ídem | `lang?` (`:15`), `emailI18n` (`:404`) |
| 4 | `netlify/functions/get-download-urls.ts:5-18` | `PRODUCT_FILES` | entrada nueva (§5) | — |
| 5 | `netlify/shared/payment-links.ts:16` | GENERADO por `sync-payment-links.py` | se regenera cuando exista la env var del link USD; lee `productos-en/**` (`sync-payment-links.py:35-38`) y exige que el id esté en `PRODUCTS` | sí |
| 6 | `netlify/shared/product-prices.ts:17` | GENERADO (`{ eur: 12 }`) | `'recipe-costing-kit': { usd: 19 }` al regenerar con `sync-product-prices.py` (lee `productos-<lang>/**` y la moneda de `TIENDAS`) | sí (`sync-product-prices.py:27-35`, tipo `{eur?, usd?}`) |
| 7 | `netlify/functions/admin-generate-access.ts:7` | `{ accessPath, label }` | entrada nueva | **No**: el email manual está **en español cableado** (`:104-117`: asunto «Tu acceso a…», «Acceder a mi producto», «Guarda este email…») y no usa `emailI18n` |
| 8 | `netlify/functions/crypto-checkout.ts` | lee `PRODUCTS` y `PRODUCT_PRICES` | nada propio: moneda `usd` si hay precio `usd` (`:343-345`), página de estado por idioma (`:194-195`, `:387`), `landingPath()` ya entiende `/access` anidado (`:179-186`), `productoLabel()` limpia «Your access to (the)» (`:153-162`) | sí |
| 9 | `netlify/shared/email-i18n.ts` | textos fijos del email | nada: `en` ya existe (`guardaEmail`, `avisoCripto` «where it applies (EU/UK)») | sí |
| 10 | `netlify/functions/stripe-webhook.ts:84-99` | resuelve el producto por payment link y llama a `sendAccessEmail` | nada, **siempre que** `payment-links.ts` tenga la entrada EN (si no: «SIN producto mapeado», `:87-89`) | sí |
| 11 | `netlify/functions/nowpayments-ipn.ts:394` | email tras pago cripto | nada (usa `PRODUCTS[pid].lang`) | sí |
| 12 | `src/data/productos-changelog.ts:321` | changelog del dashboard | entrada `recipe-costing-kit` en inglés (y `ProductChangelog` con idioma) | no |
| 13 | `src/data/products-catalog.ts:47-56` | banners del blog | `urlByLang: { en: '/en/digital-products/recipe-costing-kit' }` **después de `description`** (`:11-19`); el precio es uno solo (`'€12'`) | parcial (`urlByLang` y `productUrl()` existen, `:20-33`; ningún consumidor los usa todavía) |

Coherencia moneda↔idioma (TIENDA §6): precio `usd` en `product-prices.ts` ⇔ `lang: 'en'` en `PRODUCTS`, o la factura
sale en USD con correo y página de estado en español.

### 6.2 Pago cripto: `/pago-cripto` y la falta de `/en/crypto-payment`

- `astro-site/src/pages/pago-cripto.astro` (288 líneas, `noindex`, `title` «Confirmando tu pago cripto…» `:25`) lee
  `?o=` y `&estado=parcial`. **No existe `astro-site/src/pages/en/crypto-payment.astro`**, pero
  `crypto-checkout.ts:194-195` ya manda allí los `success_url` de productos EN → **404** si se enciende cripto antes.
- El filtro del sitemap solo excluye `path === '/pago-cripto'` (`astro.config.mjs`, bloque del filtro): hay que
  añadir `/en/crypto-payment`.

### 6.3 Qué esperan los gates de un producto EN vivo

| Gate | Espera | Estado para EN |
|---|---|---|
| `tienda-gate.py` (estático) | por familia viva: data file `productos-en/**/<slug>.ts`, landing `pages/en/digital-products/<slug>.astro` o `…/<slug>/index.astro`, `access.astro` y `library.astro`, entrada en `zona-app.ts` con `lang: 'en'` (`:206-234`) | listo |
| `tienda-gate.py --base` | 200; hreflang recíproco con el gemelo ES en los dos sentidos; sin `€`, sin restos de español, sin no latinos; gate/dashboard `noindex` | listo — **obliga a tocar `pages/kit-escandallos.astro:28`** |
| `gate-flujo-postpago.py` | `PRODUCTS` verify = resend = download; cada `/dl/` en disco, en git y 200; rutas anidadas; `product-prices` = `PRODUCTS` con `eur` o `usd`; E-f: 3 `data-crypto-open` + 1 `<dialog>` + 3 `aria-controls` por landing encendida | listo (0.B: `:26-35`, `:269-270`) |
| `miselup-gate.py` | lee TODAS las entradas de `zona-app.ts` (`registro()`, `:30-39`) y exige la tarjeta 1 vez en landing y dashboard | **No listo**: con la entrada EN exigirá la tarjeta en EN, y TIENDA §3.9 pide **cero**. Además `BaseLayout.astro:95-100` la monta por `landingPath/libraryPath` → los wrappers EN deben pasar `miselup={false}` y el gate saltar `lang ≠ es` y verificar cero |
| `whatsapp-gate.py` | 1 botón flotante por página del `dist`; exentos = `pages/*-library.astro` **de la raíz** (`:101-102`) | **No listo**: el dashboard anidado `en/digital-products/recipe-costing-kit/library.html` saldrá como «SIN botón» |
| `robots-gate.py` | zona app = `PAGES.glob("*.astro")` terminados en `-access/-library` (`:126-136`) | **Ciego a lo anidado**: no comprueba que `…/access` y `…/library` EN estén bloqueados (lo cubre `tienda-gate.py`); verifica, eso sí, que la landing EN sea rastreable |
| `censo-entregables.py` | recorre todo `dl/**`; `noprint` si `paperSize != 9` (A4) (`:240-241`) | **Choca con US Letter** si se elige Letter; `bio_vieja` busca patrones en español (inofensivo); `version_line` acepta «Version » |
| `kit-escandallos-v2_0/main.py` `_pdf_sin_cuadrados` | exige tildes, ñ, `€` y «» en el PDF (`:161-164`) | **Falla por diseño** con un PDF inglés: hay que parametrizarlo |
| `fase8c-libreria-en-gate.py` | `VETADO` exime el `€` solo dentro de banners (`:38-46`); paridad de banners/UTM EN↔ES | revisar al re-apuntar los 26 banners |

---

## 7. Infraestructura EN que ya existe

- **`astro-site/src/lib/tienda.ts`**: `TIENDAS.en` = `/en/digital-products`, `USD`, `activa: true` (`:30`);
  `tiendaProductoPath()` (`:74-80`) → `/en/digital-products/<slug>[/access|/library]`; **`FAMILIAS`**
  `kit-escandallos → { es: vivo, en: { slug: 'recipe-costing-kit', vivo: false } }` (`:89-97`);
  `alternatesFamilia()` (`:102-118`) — **ningún fichero la usa todavía** (grep), tampoco la landing ES.
- **Sitemap** (`astro-site/astro.config.mjs`, filtro): ya excluye `/^\/(en|…)\/(digital-products|…)\/[^/]+\/(access|library)$/`;
  la landing EN entrará con `lastmod` = `NEW_URLS_LASTMOD` `'2026-07-19'` salvo que se añada al mapa.
- **`robots.txt:58-63`**: `Disallow: /en/digital-products/*/access$`, `/access/`, `/access?` y lo mismo para `library`.
- **Hub EN** (`components/pages/DigitalProductsHubPage.astro`): tarjeta «Recipe Costing Kit Pro» (`:158-171`); pasa a
  viva sola cuando `FAMILIAS.en.vivo === true` (`enVivo()`, `:902-906`) con precio `$<usd>` de `PRODUCT_PRICES`
  (`:907-910`) — si falta `usd` sale sin precio. La tarjeta dice «Menu-price calculator for **9** venue types»
  (`:164`; el xlsx tiene **10** filas y la landing ES dice 10; el hub ES también dice 9) y lleva el badge
  **«🔥 Best Seller»** (`:169`), que en EN no es verdad hasta que venda: decide John (§3.5).
- **Blog EN**: **26 posts** en `astro-site/src/content/blog/en/` llevan un banner «Get Recipe Costing Kit Pro for €12»
  que enlaza a la landing **ES** `/kit-escandallos?utm_…` (p. ej. `prompt-library-food-waste-costing.md`). Son HTML
  fijo dentro del .md: hay que re-apuntarlos (URL + precio) con un parche quirúrgico (no con el ensamblador, que
  reescribe el cuerpo). `fase8c-libreria-assemble.py` solo lee `url` del catálogo.
- **Enlaces entrantes candidatos** (regla de cero huérfanas): hub EN, los 26 banners, y los posts EN del tema —
  `ai-food-cost-calculator-reduce-costs`, `ai-recipe-costing-ingredients-profit`, `recipe-cost-calculator-pricing-guide`,
  `best-recipe-costing-software-compared`, `bar-profit-margins-beverage-costing`, `prompt-library-food-waste-costing` —
  y las herramientas gratuitas `/en/food-cost-calculator-restaurant`, `/en/ai-food-cost-calculator`,
  `/en/food-cost-calculator-restaurant-ai`. ⚠️ `recipe-cost-calculator-pricing-guide` puede competir por *recipe
  costing template*: comprobar canibalización en GSC en el research de F1.
- Doc desfasado: TIENDA §4 0.C cita `TiendaStrip.astro`; se retiró en `8a725e0` y `data/tienda-hub/` ya no existe.

---

## 8. Lista de trabajo F2 / F3

### F2 — entregables

| # | Fichero / acción | Riesgo |
|---|---|---|
| 1 | Research F1 (US/UK) y decisiones: slug, precio USD, moneda como parámetro (§2.4), métrico vs imperial, impuesto, Letter/A4, benchmarks etiquetados, nombres EN de las 12 plantillas y de las 71 hojas | Alto: todo lo demás cuelga de aquí |
| 2 | `scripts/productos-digitales/recipe-costing-kit/mapa_hojas.py` (ES→EN, 1:1, ≤ 31 caracteres, sin `[]:*?/\`) | Alto: una referencia olvidada = `#REF!` silencioso |
| 3 | `…/mapa_claves.py`: 21 categorías, 11 unidades (+ imperiales), 33+ claves de `Conversiones`, 7 motivos, `ALERTA` | Alto: `VLOOKUP` devuelve `?`/`""` sin error si una clave no casa |
| 4 | `…/textos_en.py`: diccionario de las 832 cadenas (subagentes Anthropic, por fichero; gate sin español / sin no latinos) | Medio: volumen (6.698 palabras) y coherencia terminológica |
| 5 | `…/mercado_en.py`: precios de ejemplo en $, `Conversiones` imperial, `Formatos de Compra` (750 ml), impuesto, FC de benchmarks, plataformas de delivery, `Presupuesto` de catering (tarifas/hora, *service charge*), `Punto de Equilibrio` (commissary, permisos), meses, año, fecha | Alto: cifras inventadas = defecto de producto; cada benchmark etiquetado [medido]/[fuente]/[estimado] |
| 6 | `…/aplicar_en.py` (copia → hojas → claves → textos → literales → formatos → metadatos/pie/papel → `inject_cache.py` al final), idempotente, `--dry-run` en el scratchpad | Alto: `inject_cache` debe ser lo último; openpyxl 3.1 y `<v />` (gotcha conocido) |
| 7 | Gate de paridad estructural EN↔ES (fórmulas celda a celda módulo mapas, DV, CF, merges, protección, paneles, áreas de impresión, gráficos) + `data_only` + pycel de sensibilidad | Medio |
| 8 | Prueba real en **Google Sheets** (Chrome de Windows): CF cruzada del 03, protección, DV desde otra hoja, gráficos | Medio: la landing lo promete |
| 9 | `censo-entregables.py`: aceptar Letter en la carpeta EN (si se elige Letter) | Bajo |
| 10 | Bono: `bono-guide-food-cost-30-days.md` (traducción + adaptación: IVA→sales tax/VAT, benchmarks, proveedores, sin art. 91 LIVA, sin venta cruzada a la guía ES, nombres de fichero/pestaña EN) y copia parametrizada de `bono_guia.py` (cabecera, «Page», título, marcador de metadatos) + gate de glifos sin exigir ñ/€/«» | Medio |
| 11 | `astro-site/public/dl/recipe-costing-kit/` (12 xlsx + PDF) + commit que los incluya | Bajo (recordar `git add` de `public/dl`) |

### F3 — producto y lanzamiento

| # | Fichero / acción | Riesgo |
|---|---|---|
| 12 | `astro-site/src/data/productos-en/kits/recipe-costing-kit.ts` (tipo `KitExcelData`; sin reviews/rating/testimonials) | Medio: capa comercial (decisiones de John en §4.2) |
| 13 | `astro-site/src/pages/en/digital-products/recipe-costing-kit.astro` (`lang="en"`, `basePath` SIN prefijo, `alternatesFamilia`, `whatsapp={false}`, `omitGlobalApp`, `miselup={false}`) | Medio: `basePath` con `/en` duplica el prefijo (CLAUDE.md del proyecto) |
| 14 | `astro-site/src/pages/kit-escandallos.astro:28` → `alternatesFamilia('kit-escandallos')` | Medio: cambia el HTML ES (solo hreflang); `tienda-gate --es-identico` marcará esa diferencia esperada |
| 15 | `astro-site/src/lib/tienda.ts:94` → `vivo: true` (activa hub, hreflang y tarjeta) — el ÚLTIMO paso | Alto si se adelanta: enlaces a una página sin Payment Link |
| 16 | `…/recipe-costing-kit/access.astro` (`ProductAccessGate lang="en"`) y `…/library.astro` + island + `src/pages/RecipeCostingKitDashboard.tsx` (copia traducida) | Medio |
| 17 | `lang`/copy EN en `SaasDiscoveryBanner`, `ProductChangelog`, `LogoBadge`, `WhatsAppProductSupport` (default `es` byte-idéntico) + entrada EN en `productos-changelog.ts` | Medio: son compartidos por 48 dashboards ES |
| 18 | `astro-site/src/lib/zona-app.ts` (entrada con `lang: 'en'` al final) | Bajo |
| 19 | `verify-purchase.ts`, `resend-access.ts` (`lang: 'en'`), `get-download-urls.ts`, `admin-generate-access.ts` (+ email EN: hoy español cableado) | Alto: dinero y entrega |
| 20 | John: Payment Link USD con Adaptive Pricing, `success_url` = `/en/digital-products/recipe-costing-kit/access?session_id={CHECKOUT_SESSION_ID}`, env `VITE_STRIPE_PAYMENT_LINK_…` | No delegable |
| 21 | `sync-payment-links.py` y `sync-product-prices.py` → `payment-links.ts`, `product-prices.ts` (`usd: 19`) | Medio: el webhook ignora pagos sin mapear |
| 22 | `CryptoPayButton.astro` con `lang` (copy, países, `/en/terminos`) + `astro-site/src/pages/en/crypto-payment.astro` (copia traducida de `pago-cripto.astro`) + exclusión en el sitemap — o `CRYPTO_PRODUCTS_EXCLUDE` hasta tenerlo | Alto: con `CRYPTO_PRODUCTS=all` el botón sale solo y su vuelta daría 404 |
| 23 | OG image EN (`generate-images`), sin `€` ni «A4» | Bajo |
| 24 | Gates: `miselup-gate.py` (saltar EN y exigir cero), `whatsapp-gate.py` (exentos anidados), `robots-gate.py` (ver rutas anidadas); luego `tienda-gate` (estático y `--base`), `gate-flujo-postpago` LIVE, `robots-gate`, `whatsapp-gate`, `miselup-gate`, `datafast-gate` | Medio: tres gates hoy darían falso rojo o miran a otro lado |
| 25 | Hub EN: precio vivo, «9 venue types» → 10, badge «Best Seller» (decide John) | Bajo |
| 26 | `products-catalog.ts` `urlByLang.en` + parche de los 26 banners del blog EN (URL + precio $) + `fase8c-libreria-en-gate.py --todos` | Medio: precio único en el catálogo |
| 27 | Enlazado interno EN (posts del tema, herramientas gratuitas, hub) y comprobación de canibalización | Medio |
| 28 | Compra de prueba (email EN, dashboard, 13 descargas), broadcast EN en la cola de 5 días, handoff + memoria + commit `Via: Claude Code` + push | — |

Defectos del ES vistos de paso (no se tocan aquí): `subject` «Kit de Escandallos Pro · v1.1» en los 12 xlsx v2.0; el
hub ES dice «9 establecimientos» y el xlsx tiene 10.
