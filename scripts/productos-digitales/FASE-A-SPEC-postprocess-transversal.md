# Fase A — Especificación del saneamiento determinista transversal (2026-08-22)

Objetivo: dejar los 443 xlsx de los 42 productos (todos menos `kit-tareas-pasteleria`, ya v2.0,
y los 39 huérfanos de la raíz de `/dl/`) sin los defectos MEDIBLES del censo del 22-ago, con dos
scripts versionados e idempotentes. No se cambia contenido de negocio (tareas, cifras, textos):
eso es la Fase B (auditoría opus por representante).

Referencias de código que ya funcionan (copiar el patrón, no reinventar):
- `scripts/productos-digitales/kit-pasteleria-v1_1-postprocess.py` — metadata, `print_setup`,
  `fix_checkbox_family` (☐ en col. A → Nº), `add_line_instructions`, `verify`.
- `scripts/productos-digitales/kit-pasteleria-v2_0-postprocess.py` líneas 80-116 (constantes),
  755-800 (`print_setup`, `fila_cabecera`), 840-960 (`_limpiar_cf`, `analizar_checklist`,
  `normalizar_checklist`), 1631-1700 (`set_metadata`, `linea_instrucciones`, `finalizar`).
- `scripts/productos-digitales/inject_cache.py` — cache de valores (idempotente; se ejecuta AL FINAL,
  cualquier `wb.save()` posterior borra el cache). Gotchas pycel: `COUNTIF` solo 1-D, `COUNTA` no
  existe, `IF(x="","",…)` devuelve cadena vacía por diseño y queda sin `<v>` (NO es fallo).
- Regla térmica (Mac, verano): python EN SERIE, `istats cpu temp` entre tandas, parar si > 60 °C.

## 1. `censo-entregables.py` (gate, versionado)

`python3 scripts/productos-digitales/censo-entregables.py [--only <prod>] [--json out.json] [--fail] [--quiet]`

Recorre `astro-site/public/dl/**` (xlsx, docx, pdf). Producto = carpeta; los ficheros sueltos de
la raíz se etiquetan `prod='dl'` (huérfanos, se listan pero no cuentan para `--fail`).
Por xlsx: `creator`, `title`, `hojas`, `form` (nº fórmulas), `nocache_total` (data_only None),
`nocache_vacio` (la fórmula contiene `""` → vacía por diseño), `nocache_real` (= total − vacío),
`nonlat` (celdas con CJK/cirílico/hangul/árabe/hebreo/tailandés), `bio_vieja` (regex
`29 a[ñn]os|15 a[ñn]os|a[ñn]os de experiencia|15\+ a[ñn]os|29\+ a[ñn]os`, y NO debe casar la bio
nueva «desde los 17 años»), `box_colA` (nº celdas `☐` en la columna A), `noprint` (hojas con
`paperSize != 9`), `version_line` (alguna celda que empiece por `Versión ` o `Version `), `cb_brand`
(celdas con «ChefBusiness»: informativo), `empty_str` (celdas con valor `''`). Por docx
(python-docx): `parrafos`, `bio_vieja`, `nonlat`. Por pdf: `pdftotext` si existe, si no `skip`.
Salida: tabla por producto (n, form, f_sincache_real, box, bio, noA4, creator≠AICP) + totales;
`--json` vuelca la lista completa (misma forma que `censo-entregables-2026-08-22.json` más los
campos nuevos). `--fail`: exit 1 si algún xlsx de producto tiene `nocache_real>0`, `box_colA>0`
(salvo excepción de §2.4 P3a: ahí la ☐ es la marca y NO cuenta como defecto → el censo distingue
«☐ con desplegable» de «☐ muerta» mirando si la celda tiene DV de lista), `bio_vieja`, `noprint>0`,
`creator != 'AI Chef Pro'`, `nonlat>0`, `empty_str>0`. Carga normal de openpyxl (read_only no
expone page_setup). Tiempo de referencia: ~2 min para 645 ficheros.

## 2. `postprocess-transversal.py` (saneamiento)

`python3 scripts/productos-digitales/postprocess-transversal.py <productId>|all [--dry-run] [--json informe.json] [--skip-cache]`

- `all` = todas las carpetas de `astro-site/public/dl/` menos `kit-tareas-pasteleria`.
- `--dry-run`: copia la carpeta a `$SCRATCH/dryrun/<pid>/`, procesa ALLÍ y escribe el informe; no
  toca `/dl/`. Sin `--dry-run` procesa in place.
- Informe por fichero: lista de cambios (qué, hoja, celdas) + métricas de verificación final.
  Exit 1 si alguna verificación falla. Segunda ejecución sobre lo ya procesado: 0 cambios
  (idempotente; el informe lo demuestra).

### 2.1 Metadata (todos los xlsx)
`creator`/`lastModifiedBy` = `AI Chef Pro`; `title` = `<Título legible> · <Nombre corto del producto>`;
`subject` = `<Nombre corto> · v1.1`; `keywords` = `<pid con los guiones convertidos en espacios>, AI Chef Pro`
(p. ej. `kit-escandallos` → `kit escandallos, AI Chef Pro`);
`description` = `aichef.pro/<pid>`; `category` = `AI Chef Pro · Productos digitales`.

**Título legible** (decisión INT-08): primera celda de texto de la hoja
`Instrucciones`/`Índice`/`Indice` si existe → si no, la A1 de la primera hoja **de datos** (y si
esa A1 no sirve, su primera celda de texto) → si no, el nombre del fichero sin número ni
extensión, con guiones → espacios y mayúscula inicial. **Se descarta** toda cadena que empiece
(sin distinguir mayúsculas ni tildes) por `INSTRUCCIONES`, `ÍNDICE`/`INDICE`, `CÓMO USAR`/`COMO
USAR`, `AI CHEF PRO —` o `CHEFBUSINESS`: son rótulos y membretes, no títulos. Al resultado se le
quitan emojis (📋, ✅…), símbolos iniciales y espacios sobrantes.

**Nombre corto del producto** (decisiones INT-07 y SPC-01): campo `productName:` de
`astro-site/src/data/productos/**/<pid>.ts` (los 42 productos lo tienen), cortado en el primer
` — ` — **nunca por `: `**, que parte nombres donde los dos puntos son parte de la marca
(`Kit de Tareas Recurrentes: Tapas Bar / Gastrobar`). Si el prefijo resultante lo comparten dos o
más productos (`Kit de Tareas Recurrentes`, `Plan de Negocio`…), esos productos usan el
`productName` **completo**: un `title` que no identifica el producto no vale para nada. La
decisión es GLOBAL, hay que ver los 42 a la vez. Comprobación:
`postprocess-transversal.py --nombres-cortos` (exit 1 si dos colisionan).

### 2.2 Bio anclada (sustituciones 1:1 exactas, misma celda)
| Vieja | Nueva |
|---|---|
| `29 años de experiencia en alta hostelería · 15 años de consultoría gastronómica` | `Diseñado por John Guerrero — chef y consultor gastronómico desde 2010, en cocina desde los 17 años · johnguerrero.es` |
| `▸ Basada en la experiencia de 15 años de consultoría gastronómica` | `▸ Basada en la experiencia de John Guerrero: consultor gastronómico desde 2010, en cocina desde los 17 años` |
| `29+ anos de experiencia en hosteleria y 15+ anos en consultoria.` | `En cocina desde los 17 años · consultor gastronómico desde 2010.` |
| `Esta plantilla es el resultado de mas de 29 anos de experiencia en hosteleria, filtrada` (prefijo; conservar el resto de la frase) | `Esta plantilla es el resultado de la experiencia de John Guerrero (en cocina desde los 17 años, consultor gastronómico desde 2010), filtrada` |
Después, la regex de bio vieja del censo NO debe casar ninguna celda; si casa → se informa como
`bio_sin_patron` y NO se inventa sustitución (falla la verificación).

### 2.3 Impresión A4 (hojas sin setup COMPLETO: se respeta solo el que trae A4 + ajuste al ancho + pie)

> Corrección del 2026-08-22 (hallazgo H3 del refutador del changelog): la regla original «si ya
> vale 9 no se toca» dejó 147 hojas de 11 kits con el A4 «mínimo» del generador (vertical, sin
> ajuste al ancho, sin pie ni cabecera repetida). Ahora se considera configurada solo la hoja con
> las tres cosas; en las demás se aplica el setup respetando orientación, títulos de impresión y
> freeze que ya existan. El censo mide `noprint` con el mismo criterio.
`paperSize=9`, `fitToWidth=1`, `fitToHeight=0`, `fitToPage=True`, márgenes 0.59/0.3, pie
`AI Chef Pro · aichef.pro · Página &P de &N` (tamaño 8). Hojas de texto (`Instrucciones`,
`Índice`, `Indice`, o `max_column ≤ 3` sin fila de cabecera) → `portrait`, sin títulos de
impresión. Hojas de tabla → `landscape` si `max_column ≥ 6`, si no `portrait`; si se detecta fila
de cabecera (§2.4) → `print_title_rows` = esa fila y `freeze_panes` = A{hr+1} **solo si** la hoja
no tenía freeze ya.

### 2.4 Casilla unificada (vocabulario de pastelería v2.0: `✓ Completada`, DV `"✓,—,N/A"`, fila verde `C8E6C9` al marcar ✓, contador numerador + denominador calculados)
Fila de cabecera `hr` = primera fila 1..8 con ≥ 3 celdas de texto y fila siguiente con contenido.
Patrones (detectar por la cabecera; si no encaja en ninguno → no tocar y anotar `checklist: no`):

- **P1 «▸» con contador** (kit-tareas base, cafetería, pizzería, hamburguesería, dark-kitchen,
  bar: 01-07 y BONUS-01): A=`☐`, B=`Tarea`, existe col. `Hecha` (F) con DV `"✓,—"` y una celda
  `=COUNTIF(F…,"✓")` en la hoja. → A(hr)=`Nº`; cada `☐` de col. A → entero correlativo (Calibri 10,
  gris `666666`, centrado); `Hecha` → `✓ Completada`; DV de lista de esa columna sustituida por
  `"✓,—,N/A"` sobre las filas de tarea + las filas vacías existentes entre la última tarea y el
  contador (no insertar filas); CF fila verde `$F{hr+1}="✓"` sobre `A{hr+1}:<última col>{fin}`
  (eliminar antes cualquier CF cuya fórmula contenga `"✓"`); contador: numerador
  `=COUNTIF(F{hr+1}:F{fin},"✓")`, celda tras `de` → `=COUNTIF(B{hr+1}:B{fin},"?*")` (en estas hojas
  las secciones van en col. A combinada, B vacía, así que el denominador no las cuenta).
  `fin` = fila del contador − 2 (las filas de holgura ya existen: p. ej. COUNTIF(F5:F39) con
  contador en 41).
- **P2 «▸» sin contador** (asador 01-09, sushi-bar 01-09): misma cabecera, sin DV ni fórmulas.
  → Igual que P1 y, además, DV + CF, y un contador NUEVO en la fila `última tarea + 2` **solo si**
  esa fila y la anterior están vacías y no combinadas: A=`Tareas completadas:` (negrita),
  D=`=COUNTIF(F{hr+1}:F{fin},"✓")`, E=`de`, F=`=COUNTIF(B{hr+1}:B{fin},"?*")`, con `fin` = última
  tarea. Si no hay sitio → sin contador y anotado en el informe (no desplazar nada).
- **P3a «columna OK en A»** (guía panadería-obrador 6 checklists: A=`☐`, B=`Trámite`; planes
  cafetería/food-truck/panadería/tapas-bar/coctelería `checklist-apertura-*`: A=`OK`,
  B=`TRAMITE / ACCION`; coctelería `plantilla-proveedores`: A=None con ☐ debajo, B=`PRODUCTO / SERVICIO`):
  la ☐ de A ES la marca. → cabecera A: `☐`→`✓` (si era `OK` se deja); cada celda `☐` conserva el
  valor `☐` y recibe DV de lista `"✓,☐,N/A"` (así imprime con casilla y en pantalla se elige ✓);
  CF fila verde `$A{r}="✓"`; contador nuevo en `última fila + 2` si hay sitio: B=`Tareas
  completadas:` C=`=COUNTIF(A{hr+1}:A{fin},"✓")` D=`de` E=`=COUNTIF(B{hr+1}:B{fin},"?*")`.
  (En `plantilla-proveedores` NO poner contador: no son tareas.)
- **P3b «columna OK fuera de A», estilo CB** (kits marisquería/food-truck/panadería/tapas-bar y
  `plan-negocio-bar-restaurante/checklist-apertura`: cabecera `Area|Fase | Tarea… | Responsable |
  Hora|Plazo | OK | Observaciones|Notas`, A1 = «ChefBusiness Consultoria Gastronomica», sin DV):
  → DV `"✓,—,N/A"` en la col. OK de las filas con B no vacía; CF fila verde; contador nuevo como
  en P3a (numerador en la col. OK). **No tocar la marca ChefBusiness** (decisión de John pendiente).
- **P4 «# | Tarea | … | ✓ / ✓ Completada | …» con DV `"✓,✗,—"`** (catering, hotel, chef-privado,
  chocolatería, heladería, restaurante-creativo, y los 08/09 de todos los kits): ya tienen Nº y
  desplegable. → Solo CF fila verde sobre la col. de la marca y contador nuevo (B/C/D/E como P3a)
  si hay sitio. NO cambiar su DV.
- **P5 otros** (`Estado` Pendiente/En curso/Completado, registros APPCC, escandallos, financieros,
  cuadrantes): no tocar la lógica de casilla.

### 2.5 Línea de versión y de marca en `Instrucciones`/`Índice`
Si existe esa hoja: `Versión 1.1 · agosto 2026 · aichef.pro/<pid> · info@aichef.pro` (sustituye
una línea previa que empiece por `Versión `/`Version `; si no, se añade 2 filas bajo la última de
texto, copiando su estilo; nunca duplica). En ficheros P1/P2 añadir además (si no está):
`Marca con ✓ en la columna «✓ Completada» (desplegable): es la que cuenta el total de tareas
completadas.` Si el fichero no tiene hoja de instrucciones: nada.

### 2.6 Limpieza y cierre

**Reparación de fórmulas inválidas con patrón inequívoco** (excepción documentada de la Fase A,
decisión INT-01). Regla general: la Fase A no toca el contenido. Única excepción: una fórmula que
Excel no puede evaluar y cuya avería tiene una firma que no admite interpretación — un `=` de más
pegado al nombre de una función justo detrás de un operador. Se sustituye el patrón `/=` seguido
de nombre de función por `/`, y **sólo** si la celda empieza por `=`. Caso medido:
`kit-escandallos/10-calculadora-pvp.xlsx` → hoja `Calculadora PVP`, celdas **E7:E15**,
`=$C$4/=AVERAGE(C7,D7)` → `=$C$4/AVERAGE(C7,D7)` (antes, las nueve celdas abrían con `#¿NOMBRE?`).
Cada reparación se anota en el informe como `formula_reparada` con hoja, celda, `antes` y
`despues`. No se generaliza a otros operadores ni a otras anomalías: lo demás se informa
(`pseudo_formulas`) y espera a la Fase B.

**Segunda vía: `REPARACIONES_EXACTAS`** (decisión del orquestador tras el dry-run `all`, 2026-08-22).
Seis productos no pasaban la verificación por **referencias circulares preexistentes** del
generador (Excel abre con el aviso «referencia circular»; pycel no puede cachear): la tabla del
script lista, por (fichero, hoja, celda), la fórmula rota y la correcta, deducida sin ambigüedad
de las etiquetas de la propia hoja. Se aplica **solo si la celda contiene exactamente la fórmula
rota** (idempotente; si el cliente la editó, no se toca). Casos: `guia-dark-kitchen/
calculadora-viabilidad-dark-kitchen.xlsx` → `Punto de Equilibrio` B/C/D 24 (food cost sobre la
facturación, no sobre las comisiones: con la vieja salía positivo), 26 (`SUM` de las cuatro filas
superiores, no de sí misma), 28 (margen bruto + costes fijos) y 29 (EBITDA / facturación); y
`cash-flow-break-even.xlsx` → `Break-Even` B12 (`=B11*(1-B8)`) en las guías casual, japonés,
mexicano, nikkei y peruano. La celda B13 «Break-Even (meses)» de esas 5 guías está **vacía**:
es contenido, queda anotado para la Fase B.

**Pseudo-fórmulas → texto.** Seis etiquetas escritas como «= Margen bruto (€)», «= Ingresos
netos», «= CF anuales / MC unitario» (guía dark-kitchen y plan bar-restaurante) las guardó el
generador como FÓRMULA: Excel las abre con `#¿NOMBRE?`. Se conservan con el mismo texto visible
pero con tipo texto (`pseudo_formula_a_texto`). Desde aquí, los tres scripts (`postprocess`,
`censo`, `inject_cache`) cuentan fórmulas por **tipo de celda `f`**, no por «cadena que empieza
por `=`».

**Funciones que pycel no implementa** (`IRR`, `XIRR`, `PMT`, `COUNTA`): la celda queda sin cache
por el evaluador, no por el fichero (Excel calcula al abrir). Se cuenta como `nocache_pycel`
en el post-proceso **y en el censo** (mismo literal en los dos, regla de sincronización) y no es
defecto. Caso: `kit-plan-financiero/07-informe-viabilidad-bancos.xlsx:Proyecciones:B21`.

Celdas con valor `''` → `None`. Guardar. Al FINAL de cada producto: `inject_cache.py` sobre sus
xlsx, y verificación por fichero con `data_only`: `nocache_real == 0`, `nonlat == 0`, `bio_vieja
== False`, `creator == 'AI Chef Pro'`, `noprint == 0`, `empty_str == 0`, el fichero vuelve a abrir
con openpyxl (XML válido) y **las fórmulas del contador evalúan** (pycel) a entero ≥ 0.

## 3. Qué NO hace la Fase A
Cambiar tareas/cifras/textos de negocio · insertar filas o columnas · renombrar ficheros
(`PRODUCT_FILES` de `get-download-urls.ts` los referencia por ruta) · tocar docx/pdf · tocar la
marca ChefBusiness de los 7 productos de origen CB · tocar `kit-tareas-pasteleria` ni los 39
huérfanos de la raíz.
