# REFUTACIÓN DE LA SPEC — «Cómo Montar una Chocolatería» (ronda 1)

**Fecha:** 2026-09-12 · **Objeto:** `scripts/productos-digitales/guia-chocolateria-SPEC.md` (738 líneas, §0-§10 + Cierre)
**Método:** verificación directa contra los ficheros, no contra la SPEC. Se han abierto con `openpyxl read_only` los
xlsx del kit (`01-apertura-cierre`, `02-partidas-produccion`, `06-eventos-temporada`, `BONUS-02`, más un barrido de los
11), se ha cruzado **cada id `CHN-*`/`CHS-*` citado** contra las 635 entradas de
`auditorias/guias-v2-research-sector.json` con un script, se han leído las 109 fichas legales y los 10 EXCLUIDOS, el
resultado estructurado del workflow legal (`resultados-wf_7fcee771.json`: 29 prohibiciones + 13 avisos), los 28
hallazgos de la refutación del research, las 18 decisiones firmadas, la SPEC de Pastelería y su juego de generadores,
y se han comprobado contra el repo y contra producción las 20 referencias `fichero:línea` de §7 y §8
(`curl -sI https://aichef.pro/guia-chocolateria-obrador` → **404**, `robots.txt` con `/guia-*` en los **5** bloques,
`products-catalog.ts` **48**, `zona-app.ts` **49**, `guias/` **10 fichas + types.ts**, **326** posts ES).
**Se ha intentado TUMBARLA, no confirmarla.**

## Veredicto: **CORREGIR ANTES**

**23 hallazgos: 5 altas · 9 medias · 9 bajas.**

Lo que aguanta —y no hay que re-verificar— es mucho y es lo más caro:

- **Los 28 hallazgos de la refutación están resueltos uno a uno** (D19-D40 + D5, D17, D9→D43), con el fix pedido o con
  una alternativa mejor argumentada. Tres de las respuestas **mejoran** el hallazgo: §1.B.3 corrige a C6 (son **siete**
  meses «Alta», no cinco — medido hoy en `BONUS-02!Calendario`), D30 sustituye el titular «factor 5» por «factor de 3
  a 5» con la aritmética del kit, y D38 desmonta C9 por hoja y no por fichero.
- **Los literales legales casan con el JSON palabra por palabra.** Comprobados uno a uno: EUDR 2.15 ↔ 38.3 ↔ 5.3.a/b
  (`CHN-21/22/23/24`), 644.5 con su nota y la Regla 4.ª (`CHN-72/94/95/96`), ausencia de «fino/superior/extra»
  (`CHN-08`), el bombón fuera de la nota (14) (`CHN-16b` + `CHN-84`), los ocho alérgenos (`CHN-34b`), el lote fuera del
  1169/2011 (`CHN-35/36`), el art. 6.6 y el art. 8 (`CHN-64`/`CHN-92`), la libertad horaria por el 5.2 (`CHN-77`), el
  plástico (`CHN-62b/62c`) y el convenio (`CHN-66`/`CHN-93`). **Ninguna prohibición del resultado legal aparece como
  afirmación en la SPEC.**
- **Cero ids inventados.** De los 160 ids citados, los 17 que no están en el JSON común son: los 11 «bare» que sólo
  aparecen en la propia advertencia de D44 (línea 211) y 6 que se citan **como EXCLUIDOS** (`CHN-49d`, `CHN-50`,
  `CHN-70`, `CHN-79`, `CHN-80`, `CHN-98`) y están, los seis, en `-EXCLUIDOS.json`. **Uso correcto en los 17 casos.**
- **La reconciliación con el kit es real donde dice serlo.** Las diez vidas útiles de §1.B.1 son literalmente las de
  `02-partidas-produccion.xlsx!Moldeado`; las siete temperaturas de §1.B.2 son literalmente las de `01!Apertura`,
  `01!Cierre`, `01!Instrucciones`, `02!Templado` y `02!Moldeado`; las 12 filas y el 7/4/1 de §1.B.3 y §3.4 son los del
  `BONUS-02`; `06-eventos-temporada` tiene las tres hojas que dice; la regla de merma de D40 es literal; los tres
  perfiles y las tres coberturas (55-70 / 35-40 / 28-33 %) también.
- **§9 suma** (A4 cerrado): 0,55+0,50+0,30+3,15+0,60+0,65 = **5,75**; 4,50+0,40+0,60+0,75+0,25 = **6,50**; total
  **12,25**; +2,10 de research = **14,35**; y 14,35 − 13,44 = **0,91**, como dice el texto. La referencia 13,44 M es la
  recomposición que pedía A4 (12,84 de la columna del research + 0,60 del guion), y sus 8 sumandos suman 13,44.
- **La aritmética del índice es correcta en las 21 entradas:** los 21 productos `a·b·c… = N` suman lo que declaran, los
  21 tienen entre 4 y 6 epígrafes (umbral de `verificar_guion.py`), el presupuesto de palabras da 37.900 (16×1.750 +
  4×2.100 + 1.500), dentro del ±3 % de `palabras_objetivo: 37000`, y los bloques de D50 suman 40 (6×2 + 14 + 1 + 12 + 1),
  que a 0,1125 M dan los 4,50 M de §9.
- **Los dos «PENDIENTE PARA LA SPEC» del resultado legal están recogidos**, y bien: D47 (etiquetado vs granel) y D48
  (árbol operador/comerciante + tabla de clientes del art. 5.3.b). **La FAQ del research es de compra**, las dos
  definicionales del PAA quedan fuera (D39) y el slug está libre.
- **Los nueve libros están repartidos sin huérfanos** (C1 1+2 · C2 3+5 · C3 4+6 · C4 7 · C5 8+9), las 14 claves de
  `PRODUCT_FILES` cuadran con 5 documentos + 9 libros y con el `SECTIONS[]` del dashboard (2+9+3), y la regla de orden
  del índice se cumple en los cuatro pares que declara (10→14, 11→13, 12→16, 09→19).

Lo que **no** se puede firmar: la FAQ pública se manda copiar del research **sin las correcciones que la refutación
ordenó para ella**; el precio único de la cobertura —la celda que la propia SPEC llama «la más crítica del paquete»—
entra **con IVA declarado** en un escandallo, y la regla de IVA sólo cubre el equipamiento; el paso lógico de `CHN-22`
se publica como literalidad cuando el propio verificador lo declara inferencia; los cruces entre libros son **cinco y
no tres**, y los dos que faltan son justo los del precio de cobertura; la reconciliación con el kit **se dejó fuera los
alérgenos**, donde el kit publica cinco y seis y la guía prohíbe decir cinco. Y §2.4 reparte siete recuentos de líneas
a los generadores equivocados, que es la A11 reintroducida donde dimensiona a cinco agentes opus.

---

## A — ALTAS

### A-1 · ALTA — La FAQ pública se manda copiar del research «tal cual», y esas 12 preguntas contienen literalmente A1, A2, A5, A7, A8 y la causalidad falsa de la FAQ 11

**Afirmación literal (SPEC:598, §8.1 fila 1):** «`faqs` (**las 12 de §4 del research**, pasadas por `clasifica()`)».

**Problema.** Dos cosas, y la segunda cuesta dinero.

1. **La sección está mal:** la FAQ del research es **§14** («## 14. FAQ de COMPRA — 12 preguntas», línea 922);
   el §4 es «Bloques obligatorios 3 y 4 — Equipamiento crítico y proveedores reales».
2. **Y sobre todo: esas 12 preguntas son el texto SIN corregir.** Leídas hoy en el research:
   - **FAQ 6:** «*Desde diciembre de 2025 eres «operador posterior»: no haces declaración de diligencia debida, pero sí
     tienes que guardar…*» — la fórmula que A1 y A2 tumbaron (fecha y número de DDS sin condición).
   - **FAQ 4:** «*de ~5.700 € … a ~24.100 €*» — los dos totales **como número cerrado**, que es exactamente lo que
     D23c prohíbe y lo que A7/A8 marcaron («los dos entran en la cifra que **la FAQ 4 publica al cliente**»).
   - **FAQ 3:** «*el chocolate no está en la lista estatal del art. 13.8*» sin la salvedad de la letra e) (A5/D21).
   - **FAQ 11:** «*nuestras convenciones prohíben INDIRECT… **justamente por eso** [para que funcione en Sheets]*» —
     la causalidad falsa que la propia SPEC corrige en §2.3 («*la razón es interna… y así se dice en la FAQ 11, sin la
     causalidad falsa*»). La SPEC se contradice a sí misma en dos secciones.

   La SPEC no da **ninguna** instrucción de reescribir la FAQ con D5, D19, D21, D23 y D48, y **ningún gate la cubre**:
   el único gate de FAQ de §8.2 es `clasifica()` (duplicados), que no mira contenido.

**Evidencia.** `guia-chocolateria-SPEC.md:598` · `auditorias/guia-chocolateria-RESEARCH-2026-09-12.md:922-944`
(FAQ 3, 4, 6 y 11 literales) · `guia-chocolateria-research-REFUTACION-2026-09-12.md` A1 («está en la FAQ pública»),
A2 («va a la FAQ 6»), A7 («la cifra que la FAQ 4 publica al cliente»), A8 («la FAQ 4») · `SPEC:249` (§2.3, FAQ 11).

**Gravedad: alta.** Es copy público, va al `FAQPage` del JSON-LD y al email de lanzamiento, y reintroduce cuatro
hallazgos ya pagados.

**FIX.** Sustituir SPEC:598 por: «`faqs`: las **12 de §14 del research**, **reescritas antes de copiarlas** — FAQ 3 con
la salvedad de la letra e) (D21) · FAQ 4 **sin totales cerrados**, con los dos escenarios como rango y su etiqueta de
base mixta (D23c) · FAQ 6 con la puerta «operador ≠ operador posterior», fecha **30-12-2026** y el nº de DDS
**sólo si el proveedor es operador** (D5, D48) · FAQ 7 con el límite del 644.5 (D19) · FAQ 11 **sin** «para que funcione
en Sheets» (§2.3) — y después pasadas por `clasifica()`». Y añadir una fila a §8.2: «**FAQ vs lista negra** — ninguna de
las 12 respuestas contiene una cadena de §5.1, §5.2 o §5.3 (grep automático sobre la ficha `.ts`)».

---

### A-2 · ALTA — El precio único de la cobertura entra CON IVA en el escandallo, y la Regla de IVA sólo alcanza al equipamiento: el food cost del libro 4 sale inflado

**Afirmación literal (SPEC:349 y :353):** «**Un concepto, UNA fuente, y el precio de la cobertura es la celda más
crítica del paquete:** vive **sólo** en el libro 3 y los libros 4 y 7 la copian…» · tabla: «Precio de cobertura negra
(celda única) | **25,02 €/kg** | **CON IVA, declarada por la fuente** | `CHS-28a`».
Y (SPEC:255, §2.3, regla dura 3): «**Regla de IVA (D23).** Toda línea de precio **de equipamiento** lleva columna
«¿lleva IVA?» y tipo».

**Problema.** El escandallo de un obrador se calcula con precios **sin IVA** (el soportado es deducible). `CHS-28a` es,
verificado en el JSON, «Callebaut 811 … bloque 5 kg: 125,08 € … **Base CON IVA declarada explícitamente por la ficha**»
→ 25,02 €/kg. Esa celda alimenta, por diseño, el «coste materia por pieza» y el «food cost %» del libro 4 y el margen
por canal del libro 7. Con el 10 % de los productos de confitería, **todo el food cost del pack sale ~9 % alto**; si
alguna referencia fuera al 21 %, más. Y la regla que tenía que atraparlo está escrita sólo para «líneas de precio **de
equipamiento**», así que no llega ni al libro 3 ni al 4: las entradas del libro 4 en SPEC:236 son «precios de compra;
gramaje; piezas por molde…», sin una sola mención de base de IVA.

El mismo defecto por el otro lado del cociente: el PVP de la caja (`CHS-29`, SPEC:355) se publica **sin declarar base**
—20,00 / 28,00 / 45,00 € son precios de mostrador, es decir **con IVA**— mientras el libro 7 pide expresamente «ticket
medio **sin IVA**» (SPEC:239). El food cost % del libro 4 y el del libro 7 no van a dar lo mismo.

Es, con otra materia prima, el defecto que D23 nació para cerrar: «*sin ella el CAPEX sale un 21 % desviado*».

**Evidencia.** `guias-v2-research-sector.json` → `CHS-28a` («Base CON IVA declarada explícitamente»), `CHS-29`
(precios de caja sin base), `CHS-28c` («Declarada en la fuente») · `SPEC:236` (entradas del libro 4), `:239` («ticket
medio sin IVA»), `:255` (regla 3), `:349`, `:353`, `:355`.

**Gravedad: alta.** Es la celda de la que beben tres libros, sostiene el argumento de venta del producto (libro 3) y el
error va en la dirección que hace al lector creerse menos rentable de lo que es.

**FIX.** (1) Reescribir SPEC:255 como: «**Regla de IVA (D23), ampliada.** Toda línea de precio —**de equipamiento y de
materia prima**— lleva columna «¿lleva IVA?» y tipo, **y el libro 3 publica el precio de cobertura en las dos bases:
“como lo trae la fuente” (25,02 €/kg, CON IVA, `CHS-28a`) y “base imponible”, que es la que copian el 4 y el 7**. El
PVP de la carta lleva la misma pareja, y el food cost se calcula **siempre sobre base imponible en los dos lados**.»
(2) Añadir a las entradas del libro 3 (SPEC:235) la celda verde «**tipo de IVA de tu cobertura**» y a las del libro 4
(SPEC:236) «**PVP con IVA / tipo aplicado**», con la salida «PVP base» por fórmula. (3) Fila nueva en `gate_libros.py`:
ninguna hoja de escandallo referencia una celda cuya nota diga «CON IVA».

---

### A-3 · ALTA — `CHN-22` se publica como «CONFIRMADA letra a letra» y con un «SIEMPRE», cuando el propio verificador legal declara que el paso operativo es una INFERENCIA y avisa del art. 2.15 ter

**Afirmación literal (SPEC:67, D5):** «**Para el operador posterior —lo que es una chocolatería que compra cobertura—
la fecha es el 30-12-2026, SIEMPRE** | **CONFIRMADA letra a letra** por la verificación legal (`CHN-22`)… **la exclusión
es deliberada. Resuelve A1**». Repetido en el cap. 11 (SPEC:435) y en el prohibido «*el EUDR te llega en junio de 2027
si eres pequeño*».

**Problema.** Los **literales** están confirmados —los he cruzado uno a uno con el JSON y son exactos—, pero el paso que
va del literal a la frase publicada **no lo está**, y el verificador lo dice él mismo. Aviso 3 del resultado legal:

> «CHN-22 tiene un salto que **NO es cita** y va declarado como tal: los literales de los arts. 2.15 y 38.3 son nivel A,
> pero el paso «una chocolatería que compra cobertura es operador posterior → el 38.3 no le alcanza» es **INFERENCIA**.
> […] Aviso adicional que la lente no daba: **el art. 2.15 ter exige que TODOS los insumos estén amparados por una DDS;
> con cobertura anterior al EUDR o no amparada, la calificación deja de ser automática**.»

Es decir: el «SIEMPRE» es falso en un caso real y frecuente —cobertura comprada antes del EUDR o sin DDS aguas
arriba—, y el propio A1 pedía explícitamente lo contrario de lo que la SPEC escribe: «*si se opta por la lectura
contraria…, hay que decir que es **interpretación**, no nivel A*». La SPEC convierte la salvedad en una afirmación
categórica justo en la frase que va a la FAQ, al capítulo 11, a la hoja «EUDR: ¿te aplica?» del libro 8 y al correo de
lanzamiento dirigido a P5.

**Evidencia.** `resultados-wf_7fcee771.json` → `legal.avisos[2]` · `guias-v2-research-sector.json` → `CHN-22.nota`
(«Lectura literal: si compras cobertura ya comercializada en la UE eres operador posterior…») y `CHN-23.nota`
(art. 2.15 ter) · `REFUTACION` A1, párrafo de fix · `SPEC:67`, `:435`, `:38`.

**Gravedad: alta.** Es la afirmación estrella del producto y la que decide una obligación con sanción.

**FIX.** Reescribir la segunda mitad de SPEC:67: «**Los dos literales (arts. 2.15 y 38.3) son nivel A y están
confirmados letra a letra; el paso «una chocolatería que compra cobertura es operador posterior» es INFERENCIA
DECLARADA, y así se escribe en la guía, en el libro 8 y en la FAQ.** Redacción obligatoria: «*si tu cobertura llega ya
comercializada en la UE y amparada por una declaración de diligencia debida, eres operador posterior (art. 2.15 ter) y
el aplazamiento del art. 38.3 —que es para operadores— no te alcanza: tu fecha es el 30 de diciembre de 2026. Si tu
cobertura NO está amparada (compra anterior al EUDR, proveedor que no lo acredita), la calificación deja de ser
automática y hay que revisarla*».» Y añadir a la lista negra §5.1 una entrada 30: ❌ «*siempre eres operador posterior*»
/ ❌ «*tu fecha es el 30-12-2026 pase lo que pase*».

---

### A-4 · ALTA — Los cruces entre libros son CINCO, no tres: D32, §2.3 y el gate sólo cubren tres, y los dos que faltan son los del precio de cobertura

**Afirmación literal (SPEC:199, D32):** «**Los TRES cruces entre libros** se materializan como celda verde + fila de
cuadre, y el gate lo comprueba. Son: libro 6 «déficit de capacidad contra el libro 1» · libro 7 «fecha límite…» · libro
9 «desviación contra el CAPEX del libro 2»». Y la tabla de §2.3 (SPEC:261-263) tiene exactamente esas tres filas, bajo
el rótulo «**los tres cruces reales del paquete**».

**Problema.** La propia SPEC declara otros dos en dos sitios distintos, y son sobre la cifra más importante del pack:

- **SPEC:349 (§3.3):** «el precio de la cobertura … vive **sólo** en el libro 3 y **los libros 4 y 7 la copian por celda
  verde con fila de cuadre (D32)**».
- **SPEC:235 (§2.2, libro 3, columna «Frontera»):** «Un solo precio de cobertura en todo el paquete…; **el 4 y el 7 lo
  copian por celda verde con fila de cuadre (D32)**, nunca por fórmula entre libros».

Son **cruces 4←3 y 7←3** que no están en D32 ni en la tabla de §2.3. Y §2.5 insinúa dos más al justificar los pares:
«*el semáforo de clima del 1 usa la **partida de climatización del 2***» (1←2) y «*el escandallo del 4 alimenta el peso
de campaña del 6*» (6←4).

El daño es concreto: un constructor que trabaje desde §2.3 —que es la sección de convenciones, la que se lee para
construir— hará tres filas de cuadre y **no las dos del precio de cobertura**. El resultado es el mismo concepto
tecleado en tres libros sin control de coherencia, que es **literalmente** el defecto ALTO de Pastelería que D32 cita
como razón de existir («el fondo de maniobra calculado dos veces publicó dos inversiones totales distintas»). El gate
nuevo («ninguna fórmula menciona otro fichero») **no lo detecta**: comprueba fórmulas, no filas de cuadre ausentes.

**Evidencia.** `SPEC:199` (D32), `:235`, `:261-263` (tabla de tres), `:265` (gate), `:288-292` (§2.5, pares C1 y C3),
`:349` (§3.3).

**Gravedad: alta.** Reabre el defecto ALTO de la hermana sobre la cifra que sostiene el argumento de venta del libro 3.

**FIX.** (1) Reescribir la cabecera de D32 (SPEC:199) como «**Los CINCO cruces entre libros**» y añadir a su lista:
«libro 4 ← 3 «precio de cobertura por referencia»» y «libro 7 ← 3 «precio de cobertura»». (2) Añadir esas dos filas a la
tabla de §2.3 (tras SPEC:263) con el mismo patrón: celda verde «trae aquí la cifra de
`sensibilidad-al-precio-del-cacao.xlsx!Coste de Cobertura por Referencia!<Celda>`» + fila de CUADRE con semáforo.
(3) Corregir §2.5 para que los pares se justifiquen **sin** describir cruces no declarados, o declararlos: si el
semáforo del libro 1 usa la partida de climatización del 2 y el peso de campaña del 6 usa el escandallo del 4, son dos
cruces más y necesitan su celda verde y su cuadre. (4) Ampliar el gate de `gate_libros.py`: además de «ninguna fórmula
menciona otro fichero», **«cada celda verde etiquetada “trae aquí la cifra de X” tiene su fila de CUADRE en la misma
hoja”, contadas contra la lista de la SPEC (deben ser 5, o las que queden tras (3))**.

---

### A-5 · ALTA — La reconciliación con el kit se dejó fuera los ALÉRGENOS, y ahí el kit publica cinco y seis donde la guía prohíbe decir cinco

**Afirmación literal (SPEC:82-87, §1.B):** «Reconciliación con `kit-tareas-chocolateria` — **hecha ABRIENDO los
ficheros, antes de fijar un solo dato**… **la guía CITA el kit, no lo reescribe, y donde la guía necesita un número que
el kit ya publica, usa EL DEL KIT**». Y (SPEC:343, §3.2 y D41): «**Los alérgenos de una bombonería son OCHO, no cinco**
(`CHN-34b`)… ❌ Prohibido «los cinco alérgenos de una bombonería»».

**Problema.** Abiertos hoy los 11 ficheros del kit con `openpyxl read_only` y barridos por «alérgen», el kit publica
**tres listas distintas y ninguna es de ocho**:

| Fichero · hoja | Lo que publica el kit, literal | Cuántos |
|---|---|---|
| `01-apertura-cierre.xlsx!Apertura`, tarea 2 | «los alérgenos declarados — **leche, frutos secos, soja, gluten, huevo y sésamo**— más las trazas» | **6** |
| `04-tareas-perfiles.xlsx!Dependiente`, tarea 2 | «los alérgenos declarados (**leche, frutos secos, soja, gluten y sésamo**… )» [misma redacción, con huevo] | **6** |
| `06-eventos-temporada.xlsx!Pascua`, tarea 5 | «alérgenos declarados (**leche, frutos secos, soja, gluten y huevo**)» | **5** |

La tercera es, palabra por palabra, la frase que la prohibición nº 11 del resultado legal y D41 prohíben escribir
(«*Los cinco alérgenos de una bombonería son leche, frutos secos, soja, gluten y huevo*»), **ya publicada por la casa en
un producto vendido a 12 €**. Y las tres funden «frutos secos» en una entrada, cuando `CHN-34b` demuestra que
cacahuetes (punto 5), frutos de cáscara (punto 8) y sésamo (punto 11) son **entradas independientes** del Anexo II —el
hallazgo se llevó una corrección de ficha entera—. Falta además el **sulfito** en las tres.

Es el patrón exacto de C1 y C2 (los dos ALTAS del bloque de producto), y §1.B no tiene su regla K: hay K1 (templado),
K2 (campañas), K3 (perfiles), K5 (escandallo), K7 (vida útil) y la de temperaturas, pero **ninguna de alérgenos**,
aunque D30 dejó dicho que «*las seis reglas K1-K6 se vuelven a pasar abriendo TODAS las hojas de los 11 ficheros*» —
resultado que la SPEC no registra.

**Evidencia.** `astro-site/public/dl/kit-tareas-chocolateria/01-apertura-cierre.xlsx!Apertura` ·
`04-tareas-perfiles.xlsx!Dependiente` · `06-eventos-temporada.xlsx!Pascua` (los tres leídos con openpyxl hoy) ·
`resultados-wf_7fcee771.json` → `legal.prohibiciones[10]` · `guias-v2-research-sector.json` → `CHN-34b` ·
`SPEC:82-87`, `:208` (D41), `:343`, `:438` (cap. 12).

**Gravedad: alta.** Un comprador de los dos productos lee cinco en el checklist con el que etiqueta la vitrina y ocho
en la guía; y el que está mal es el que se usa a diario para etiquetar, con el cacahuete y el sésamo escondidos dentro
de «frutos secos».

**FIX.** Añadir a §1.B, tras B.5 (SPEC:177), un bloque **B.6 — Alérgenos (regla K8)** con la tabla de arriba y esta
decisión: «**D53 — Los ocho alérgenos son los de `CHN-34b` y el kit se corrige en el MISMO commit.** Las tres celdas de
texto del kit (`01!Apertura` t.2, `04!Dependiente` t.2, `06!Pascua` t.5) pasan a «*los alérgenos declarados —leche,
huevo, cereales con gluten, soja, **cacahuetes**, **frutos de cáscara**, **granos de sésamo** y **sulfitos**— más las
trazas*», con entrada en el changelog del kit (2.1) y regeneración por su generador
(`kit-tareas-v2_0/contenido_kit_tareas_chocolateria.py`), **nunca a mano**. Hasta que eso esté hecho, el cap. 12 no se
escribe.» Y anotar en §8.2 la fila «**Alérgenos kit↔guía** — `grep` de «frutos secos» en los 11 xlsx del kit = 0».

---

## B — MEDIAS

### B-1 · MEDIA — §2.4 asigna SIETE de los ocho recuentos de líneas al generador equivocado, y los dos superlativos son falsos: es la A11 reintroducida donde dimensiona a cinco agentes opus

**Afirmación literal (SPEC:273-281):** «1 | capacidad y clima | `gen_capacidad-obrador-y-local.py` (**1.515** líneas)»
· «2 | CAPEX | `gen_calculadora-capex-pasteleria.py` (**1.453**)» · «4 | carta y escandallo |
`gen_carta-de-apertura-y-escandallo.py` (**1.589, el más denso**)» · «6 | campañas | `gen_estacionalidad-y-picos.py`
(**1.610**)» · «7 | plan financiero | `gen_plan-financiero-3-anos-pasteleria.py` (**1.710**)» · «8 | checklist legal |
`gen_checklist-legal-y-licencias.py` (**2.720, el más largo**)» · «9 | equipamiento |
`gen_checklist-equipamiento-y-proveedores.py` (**1.457**)».

**Problema.** `wc -l scripts/productos-digitales/guia-pasteleria/gen_*.py`, hoy:

| Generador | SPEC dice | Real |
|---|---|---|
| `gen_capacidad-obrador-y-local.py` | 1.515 | **1.453** |
| `gen_calculadora-capex-pasteleria.py` | 1.453 | **1.515** |
| `gen_carta-de-apertura-y-escandallo.py` | 1.589 | **1.610** |
| `gen_estacionalidad-y-picos.py` | 1.610 | **1.142** |
| `gen_plan-financiero-3-anos-pasteleria.py` | 1.710 | **2.720** |
| `gen_checklist-legal-y-licencias.py` | 2.720 | **1.710** |
| `gen_checklist-equipamiento-y-proveedores.py` | 1.457 | **1.589** |

La causa es identificable y vale para el fix: **la suma de D26a está en orden alfabético de fichero**
(`1.515 + 1.453 + 1.610 + 1.589 + 1.710 + 1.142 + 2.720 + 1.457` = capex, capacidad, carta, checklist-equip,
checklist-legal, estacionalidad, plan-financiero, plantilla-turnos) y §2.4 repartió esos ocho números **en el orden de
los libros de chocolate**. El total (13.196) y la media (1.650) son correctos; los siete repartos, no. Y de ahí salen
los dos superlativos invertidos: **el más largo de los ocho es el plan financiero (2.720)**, no el checklist legal, y
el «más denso» que se le atribuye a la carta (1.610) es en realidad el tercero.

Importa porque §2.4 es la columna «qué se calca» que leen los cinco constructores opus, y porque es exactamente el
defecto que A11 ya corrigió una vez en este mismo producto.

**Evidencia.** `wc -l scripts/productos-digitales/guia-pasteleria/gen_*.py` · `SPEC:273-281`, `:283`.

**FIX.** Corregir los siete paréntesis de SPEC:273-281 con los valores reales de la tabla; cambiar «(1.589, **el más
denso**)» por «(1.610)» en la fila 4 y «(2.720, **el más largo**)» por «(1.710)» en la fila 8; y añadir tras SPEC:283:
«**El más largo de los ocho es `gen_plan-financiero-3-anos-pasteleria.py` (2.720), que es el molde del libro 7**».

---

### B-2 · MEDIA — «Tres libros sin molde previo» sostiene el +0,91 M del presupuesto, y §2.4 sólo marca DOS

**Afirmación literal:** SPEC:287 (§2.5) «son nueve libros y **tres no tienen molde**» · SPEC:665 (§9) «**tres libros sin
molde previo** (los 0,35 M/libro frente a los 0,30 de la hermana)» · SPEC:652 «0,35 M por libro… porque **tres no tienen
molde previo**».

**Problema.** La tabla de §2.4 (SPEC:273-281) marca `N` exactamente **dos**: el 3 (sensibilidad al cacao) y el 5 (vida
útil y rotación). Los otros siete llevan `H` con su generador de origen nombrado, el 8 y el 9 incluidos. El research
decía **cuatro** («*el libro 5 … es uno de los cuatro «sin molde previo» que sostienen el precio*», citado en C1 y C7).
Tres cifras distintas para el mismo hecho, y la del §9 es la que justifica el sobrecoste de 0,91 M sobre Pastelería,
que es sobre lo que John decide (§10, punto 5).

**Evidencia.** `SPEC:273-281` (dos `N`), `:287`, `:652`, `:665` · `REFUTACION` C1 y C7 (cuatro, en el research).

**FIX.** Decidir el número contra la tabla y propagarlo. Si son dos: SPEC:287 → «son nueve libros y **dos no tienen
molde (3 y 5)**, y el 8 añade dos hojas sin molde (cadmio y EUDR)»; SPEC:652 y :665 → recalcular la fila «Los 9 libros»
con 7 × 0,30 + 2 × 0,35 = **2,80 M** (no 3,15) y rehacer los totales de §9, que bajarían a **11,90 M** de construcción y
**14,00 M** de ciclo. Si se mantienen 3,15 M, decir **qué tercer libro** no tiene molde y marcarlo `N` en §2.4.

---

### B-3 · MEDIA — «"Vitrina refrigerada 4.000-18.000 €" en todas» es falso: la partida aparece UNA vez, vale 6.000-18.000, y la propia frase calcula sobre 6.000

**Afirmación literal (SPEC:194, D27, y repetida en SPEC:557, §7.1):** «el patrón de partidas es **idéntico en las seis**
(«**vitrina refrigerada 4.000-18.000 €**» **en todas**): es **una plantilla, no seis cifras investigadas**, y la vitrina
de chocolate verificada cuesta **2.684,99 €** (`CHS-43`), o sea que publica **de 2,2 a 6,7 veces** el precio real».

**Problema.** Censadas hoy las seis FAQ de `src/data/use-cases-content.es.consultor.ts`:

| Línea | Vertical | Partida de vitrina, literal |
|---|---|---|
| `:279` | heladería | «vitrina expositora (**4.000–15.000 €**)» |
| `:393` | chocolatería | «vitrina refrigerada (**6.000–18.000 €**)» |
| `:505` | pastelería | «vitrinas refrigeradas (**4.000–14.000 €**)» |
| `:618` | pizzería | «vitrinas refrigeradas para ingredientes (**3.000–10.000 €**)» |
| `:731` | cafetería | **ninguna** |
| `:1070` | panadería | «vitrinas y mobiliario de tienda (**5.000–18.000 €**)» |

Ni el nombre, ni el rango, ni el «en todas». `grep -o 'vitrina refrigerada ([0-9]…'` devuelve **una** ocurrencia en todo
el fichero. Y la frase se contradice a sí misma dentro de la misma celda: **2,2 y 6,7 son 6.000/2.685 y 18.000/2.685**,
no 4.000/2.685 (que sería 1,5). §5.2 `N-2` sí escribe el dato bueno («vitrina refrigerada 6.000-18.000 €»), así que la
SPEC dice las dos cosas.

La conclusión de fondo —que las seis son una plantilla— sigue en pie por estructura (mismo esqueleto de seis partidas y
mismos órdenes de magnitud), pero la prueba citada no existe, y es la prueba que un agente `sonnet` va a intentar
verificar antes de tocar 7 ficheros × 6 FAQ.

**Evidencia.** `src/data/use-cases-content.es.consultor.ts:279, 393, 505, 618, 731, 1070` (leídas hoy) ·
`SPEC:194`, `:498` (`N-2`), `:557`.

**FIX.** En SPEC:194 y SPEC:557 sustituir el paréntesis por: «(las seis repiten el mismo esqueleto de 5-6 partidas con
los mismos órdenes de magnitud, **con la vitrina en las cinco que la traen: 3.000-10.000 · 4.000-14.000 · 4.000-15.000 ·
5.000-18.000 y 6.000-18.000 €**): es una plantilla, no seis cifras investigadas. La de chocolatería publica
**6.000-18.000 €** y la vitrina verificada cuesta **2.684,99 €** (`CHS-43`): **de 2,2 a 6,7 veces** el precio real».

---

### B-4 · MEDIA — §7.1 promete que `fase8e-banners-corpus.py` «reparte» el producto 49 por los 326 posts, y `fase8e` sólo INSERTA sobre posts que ya tienen sus 3 banners

**Afirmación literal (SPEC:560, §7.1):** «**Rotación general de banners** | Entrada **49** en `products-catalog.ts` →
`fase8e-banners-corpus.py` **lo reparte solo por los 326 posts ES**».

**Problema.** La propia SPEC lo desmiente dos veces: SPEC:213 (D46) y SPEC:573 (§7.2) dicen «**`fase8e-banners-corpus.py`
sólo INSERTA, no sustituye** (verificado: sus flags son `--lang/--aplicar/--informe/--limite`)». Y el estado medido es
que **los 326 posts ES ya tienen sus 3 banners** (§7.2 lo afirma para los 8 que toca, y el corpus se cerró en 325/325
el 31-ago). Un script que sólo inserta, sobre un corpus saturado, **no reparte nada**: el producto 49 entraría en el
catálogo y seguiría con cero banners salvo por las cuatro sustituciones de §7.2.

El riesgo no es sólo la frase: es que alguien ejecute `fase8e --aplicar` esperando el reparto y se quede con un informe
vacío dando por hecho que la rotación está hecha.

**Evidencia.** `SPEC:213`, `:560`, `:573` · `scripts/astro-migration/fase8e-banners-corpus.py` (flags) · `CLAUDE.md`
(«ES 325/325 posts con 3 banners»).

**FIX.** Sustituir SPEC:560 por: «**Rotación general de banners** | Entrada **49** en `products-catalog.ts`, que la mete
en `rotar_productos()` **para todo lo que se genere a partir de ahora**. ⚠️ **No hay reparto retroactivo**: los 326 posts
ES ya tienen sus 3 banners y `fase8e-banners-corpus.py` **sólo inserta**, así que sobre el corpus actual no haría nada.
Los únicos banners del 49 en el blog son **los 4 de §7.2**, vía `fase8x-sustituir-banner.py`».

---

### B-5 · MEDIA — D1 (firmada) exige columna de escenario de taza y churros «en el libro 2 y en el P&L», y el libro 7 no la tiene

**Afirmación literal:** SPEC:38 (§0, Alcance) y SPEC:63 (D1): «La chocolatería de taza y churros entra como **epígrafe
del cap. 01** + **columna de escenario en el libro 2 y en el P&L** + párrafo en la primera pantalla de la landing y una
FAQ».

**Problema.** El libro 2 sí la recoge (SPEC:234 y :274: «Variantes bean-to-bar y taza y churros»). El libro 7
(SPEC:239) tiene once hojas —Supuestos, Inversión Inicial, PyG 3 Años, Punto de Equilibrio, Escenarios, Personal,
Tesorería 12 meses, Financiación, Canales y Punto Muerto, Talleres y Regalo Corporativo, Instrucciones— y **ni una
entrada, ni una salida, ni una columna** de taza y churros; su hoja «Escenarios» es la de optimista/base/pesimista del
molde `planes-v2_0`. §2.4 fila 7 tampoco la lista entre lo nuevo. Una decisión firmada por delegación de John se queda
sin implementar en la mitad de su alcance, y es la mitad que decide si el lector puede modelar su negocio.

**Evidencia.** `SPEC:38`, `:63`, `:234`, `:239`, `:274`, `:279`.

**FIX.** Añadir a las entradas del libro 7 (SPEC:239): «**escenario de formato: bombonería / bombonería + taza y
churros** (celda verde de dos valores, D1) — con su ticket, su margen y su coste de personal propios»; a las salidas:
«**P&L y punto muerto por formato**, en columnas contiguas»; y a §2.4 fila 7, en «qué es nuevo»: «**la columna de
escenario de taza y churros (D1)**».

---

### B-6 · MEDIA — D10 (firmada) queda huérfana: ni un capítulo, ni una hoja, ni un epígrafe entregan la artesanía alimentaria

**Afirmación literal (SPEC:72, D10):** «**Artesanía:** Cataluña con articulado (**Decreto 85/2024**, incluye
«chocolates»); el resto, enlace al registro autonómico | Vigente **y acotada**…».

**Problema.** «Artesanía» aparece en la SPEC exactamente tres veces —en D10, en D21 (donde se **prohíbe** usar el
Decreto como prueba de qué es «repostería») y en el prohibido del cap. 09—, y **ninguna es un entregable**. Ni el
índice de §4 (20 capítulos + anexo) ni ninguna de las hojas de los 9 libros de §2.2 cubren el registro de artesanía
alimentaria, sus requisitos ni el enlace autonómico. Tras D21, la única huella que queda del Decreto 85/2024 es
negativa. Para el lector, «¿puedo llamarme artesano y qué me hace falta?» es una pregunta de apertura con consecuencias
de rotulación y de subvención, y era el sentido de D10.

**Evidencia.** `SPEC:72`, `:188` (D21), `:433` (cap. 09, prohibido) · `grep -n "artesanía\|85/2024"` sobre la SPEC:
sólo esas tres líneas.

**FIX.** Añadir a los epígrafes del cap. 09 (SPEC:433) un quinto: «**Artesanía alimentaria: qué es, qué NO es y dónde se
pide** — repertorio catalán del **Decreto 85/2024**, que incluye «chocolates», como único articulado leído; para el
resto de comunidades, el enlace a su registro y las tres preguntas que hay que hacerle (D10). ⚠️ **No es el RD
1021/2022 y no prueba nada sobre «repostería» (D21).**», ajustar su `puntos_por_epigrafe` a `4·4·2·5·3·2 = 20` (o
recortar otro epígrafe para no pasar de 6) y añadir una fila «¿vas a inscribirte como artesano? (CCAA + enlace)» a la
hoja «Checklist Legal (F1-F6)» del libro 8.

---

### B-7 · MEDIA — La lista de prohibiciones dice ir «literal» y la nº 28 pierde «de CAPEX», que es justo la categoría que §3.3 publica

**Afirmación literal (SPEC:469 y :500, §5.1):** «Son **veintinueve**, y cada una lleva su id. **Van literales**» ·
«28 | Cualquier cifra de ruido, de seguro de RC, de coste de proyecto técnico **o de exposición laboral** presentada
como dato verificado | `CHN-50`, `CHN-70`, `CHN-79`, `CHN-80` (EXCLUIDOS)».

**Problema.** El resultado de la verificación legal, prohibición 28, dice: «*Cualquier cifra de ruido, de seguro de RC,
de coste de proyecto técnico, **de CAPEX** o de exposición laboral presentada como dato verificado*». Las otras 28 las
he cotejado una a una y son literales; ésta pierde una categoría, y no una cualquiera: §3.3 publica dos escenarios de
CAPEX (**≈24.000-24.300 €** y **≈5.500-5.900 €**) y el cap. 04 los explica. La etiqueta de D23c («BASE MIXTA, no es
presupuesto de apertura») es precisamente lo que hace compatible publicarlos con esa prohibición — pero si la
prohibición se cita mutilada, quien la aplique no verá que el CAPEX está dentro de su ámbito.

**Evidencia.** `resultados-wf_7fcee771.json` → `legal.prohibiciones[27]` · `SPEC:469`, `:500`, `:364-365`.

**FIX.** SPEC:500 → «28 | Cualquier cifra de ruido, de seguro de RC, de coste de proyecto técnico, **de CAPEX** o de
exposición laboral **presentada como dato verificado** — los dos escenarios de dotación de §3.3 sólo pueden salir con
su etiqueta de base mixta y como rango (D23c) | `CHN-50`, `CHN-70`, `CHN-79`, `CHN-80` (EXCLUIDOS)».

---

### B-8 · MEDIA — D19 convierte en fila obligatoria del libro 8 un cruce «canal → epígrafe de IAE» que el propio verificador deja como pregunta para el asesor

**Afirmación literal (SPEC:186, D19):** «**Fila nueva obligatoria en la hoja «Checklist Legal» del libro 8: canal →
epígrafe de IAE.**» Y SPEC:240 (libro 8): salida «veredicto…» con la fila; SPEC:443 (cap. 19): «El cruce **canal →
epígrafe de IAE**, y los tres canales que se salen de la nota del 644.5».

**Problema.** Los tres literales nuevos son correctos y los he verificado (`CHN-94`, `CHN-95`, `CHN-96`). Pero la nota
de `CHN-95` dice, literalmente: «*En contra: el 644.5 condiciona la FABRICACIÓN a que «su comercialización se realice
en las propias dependencias de venta», y **eso es lo que hay que preguntar al asesor** para los canales B2B, regalo
corporativo y envío*»; y la de `CHN-96`: «*quien monte los cinco canales y quiera **una sola alta** que lo cubra todo,
la que lo cubre es la industrial (421.1)*» — que la SPEC prohíbe presentar como necesaria (§5.3: ❌ «*necesitas el
epígrafe industrial 421.1 para fabricar bombones*»).

Es decir: **no existe fuente que dé un epígrafe por canal**, y una hoja que emita «canal → epígrafe» tiene que
inventárselo o dejar cinco celdas verdes que el lector no sabe rellenar — exactamente el dilema que C4 tumbó para la
carga térmica y que D33 resolvió cambiando la salida.

**Evidencia.** `guias-v2-research-sector.json` → `CHN-95.nota`, `CHN-96.nota` · `SPEC:186`, `:240`, `:443`, `:503`
(§5.3).

**FIX.** Reformular la fila como pregunta, igual que hizo D33: SPEC:186 → «**Fila nueva obligatoria en la hoja
«Checklist Legal»: canal → ¿te saca de la nota del 644.5?** Por cada uno de los cinco canales, **sí/no/no lo sé** con la
nota literal delante, **más la salida «lleva esta pregunta a tu asesor fiscal, con esta redacción»** y el aviso de
`CHN-96` (la única alta que cubre los cinco es la industrial, y eso te saca del amparo de la Ley 12/2012, `CHN-49b`).
❌ **La hoja NO emite un epígrafe de IAE por canal: ninguna fuente lo da.**»

---

### B-9 · MEDIA — D4 (firmada) no baja a la capa de ejecución: ni §7.1 ni §8.1 instruyen cambiar el texto de la tarjeta

**Afirmación literal (SPEC:66, D4):** «La tarjeta del hub dirá «**proveedores de cobertura y cacao**»; el libro 9 cubre
las dos cosas | Vigente. Es un cambio de tres palabras sobre lo anunciado desde mayo».

**Problema.** La tarjeta de `comingSoon` dice hoy, verificado en el repo, «*Temperado, obrador, vitrina, **proveedores
de cacao**, licencias y modelo de negocio.*» (`ProductosDigitales.tsx:959` y `…HubPage.astro:974`). Al publicar, esa
tarjeta se retira y nace la del producto. Pero la fila «Hub, los DOS ficheros» de §7.1 (SPEC:552) sólo dice «Tarjeta
real con badge «Nuevo» y vaciar `comingSoon`», y §8.1 filas 19-20 (SPEC:607) enumeran seis cambios sin incluir la
redacción. D4 sobrevive sólo como eco en §2.2 («proveedores de cacao **y de cobertura** → 9 (D4)», SPEC:243), que es
prosa de cobertura de promesa, no una instrucción.

**Evidencia.** `src/pages/ProductosDigitales.tsx:959` · `astro-site/src/components/pages/ProductosDigitalesHubPage.astro:974`
· `SPEC:66`, `:243`, `:552`, `:607`.

**FIX.** Añadir a SPEC:552, tras «Tarjeta real con badge «Nuevo»»: «**con la descripción de D4: «Obrador, denominaciones
legales, vitrina, campañas, licencias y proveedores de cobertura y cacao» —«cobertura» entra, que es lo que de verdad
compra una bombonería—**», y repetirlo en la celda de §8.1 filas 19-20.

---

## C — BAJAS

### C-1 · BAJA — `…HubPage.astro:1447` es el comentario; la `<section id="pd-coming-section">` abre en **1448**

**Afirmación literal (SPEC:68 y :553):** «la `<section id="pd-coming-section">` que abre en **`ProductosDigitalesHubPage.astro:1447`**
(el `.map()` está en **:1464**)».

**Problema.** Leídas las líneas: 1447 es `{/* ===== Coming Soon ===== */}` y 1448 es
`<section id="pd-coming-section" class="px-4 pb-16 md:pb-24">`. El `.map()` en 1464 sí es exacto, y la guarda de la SPA
en `ProductosDigitales.tsx:1227` y los badges en `:1080` / `…HubPage.astro:1143` también. La refutación del research ya
daba el número bueno («la SPA sí tiene guarda (:1227) y el Astro no (**:1448**)»): se perdió al escribir la SPEC.

**FIX.** SPEC:68 y SPEC:553 → «…que abre en **`…HubPage.astro:1448`** (el comentario `{/* ===== Coming Soon ===== */}`
va en :1447; el `.map()` está en :1464)».

---

### C-2 · BAJA — D45 sitúa `puntos_por_epigrafe` en `documentos.py:1096`, que es texto de un prompt

**Afirmación literal (SPEC:212, D45a):** «**`puntos_por_epigrafe`** (`documentos.py:1096`) en los 20 capítulos…».

**Problema.** En `guias-v2_0/documentos.py`, la línea 1096 está dentro de la cadena que construye el bloque «DATOS DEL
SECTOR» del prompt. `def repartir_puntos(cap, bloques)` está en la **1126**, el docstring que describe
`cap['puntos_por_epigrafe']` en la **1131**, la lectura `por_epi = cap.get('puntos_por_epigrafe')` en la **1145** y el
`SystemExit` de claves huérfanas en la **1152**. Un agente que abra 1096 no encuentra nada de lo que D45 le promete.

**FIX.** SPEC:212 → «**`puntos_por_epigrafe`** (`documentos.py`: `repartir_puntos()` en la **línea 1126**, contrato en
la 1131, lectura en la 1145 y `SystemExit` de claves huérfanas en la 1152)».

---

### C-3 · BAJA — `postprocess-transversal.py` no está en `auditorias/`

**Afirmación literal (SPEC:622, §8.2):** «Postproceso transversal | `auditorias/postprocess-transversal.py <ruta>
--dry-run`».

**Problema.** El fichero vive en `scripts/productos-digitales/postprocess-transversal.py`; en `auditorias/` no hay
ninguno con ese nombre (`find scripts -name "*postprocess*"`). Los otros 17 comandos de §8.2 y §2 sí resuelven.

**FIX.** SPEC:622 → «`/usr/local/bin/python3 scripts/productos-digitales/postprocess-transversal.py <ruta> --dry-run`».

---

### C-4 · BAJA — Costura entre las dos mitades: un fragmento colgando en el balance del índice

**Afirmación literal (SPEC:448):** «…y 5 son mixtos (03, 08, 14, 18 y 19); el anexo hereda.** **Nueve más veinte** /
**Nueve más seis más cinco son los veinte capítulos**, y el anexo va aparte».

**Problema.** «Nueve más veinte» es un resto de edición sin sentido, pegado justo antes de la frase buena. El recuento
sí es correcto y lo he contado sobre la tabla: H = 01, 02, 04, 05, 09, 12, 13, 17, 20 (**9**) · N = 06, 07, 10, 11, 15,
16 (**6**) · H+N = 03, 08, 14, 18, 19 (**5**).

**FIX.** Borrar «Nueve más veinte» de SPEC:448.

---

### C-5 · BAJA — El suelo del escenario B (≈5.500 €) no lo sostiene ninguna de las dos correcciones de D23

**Afirmación literal (SPEC:365):** «**Escenario B — arranque mínimo** | **≈5.500-5.900 €**».

**Problema.** `CHS-47b` es 5.740,29 € con «12 moldes ~360,00 €» dentro. Aplicando D23a (moldes **290,40-513,96 €**) el
rango real es **5.670,69 - 5.894,25 €**, y D23b («mantenedor **desde** 570 €») sólo puede empujar hacia arriba, nunca
hacia abajo. El suelo publicado, 5.500 €, está **170 € por debajo** de lo que produce el propio método. El escenario A
sí está bien redondeado: 24.104,99 → 24.035-24.259 → «≈24.000-24.300 €».

**FIX.** SPEC:365 → «**≈5.700-5.900 €** (5.670-5.894 con el rango de moldes de D23a; el mantenedor es un «desde», así
que el techo puede subir)».

---

### C-6 · BAJA — El gate de solape exige «0 pares» y el producto de referencia salió con 1

**Afirmación literal (SPEC:626, §8.2):** «Solape | `guias-v2_0/solape.py <dir_txt>` | Que `puntos_por_epigrafe` haya
hecho su trabajo: **0 pares** por encima del umbral».

**Problema.** D45 (SPEC:212) declara, como prueba de que la palanca funciona, que Pastelería dio «**1 par en 46
bloques**». Un gate de 0 pares habría tumbado al producto de referencia, que está LIVE y verificado. Un gate que no
puede pasar el caso conocido-bueno se desactiva a la primera, y con él se pierde la señal.

**FIX.** SPEC:626 → «**≤1 par** por encima del umbral (Pastelería salió con 1 en 46 bloques y es la referencia); con 2
o más, **se regenera en 2 bloques el capítulo implicado**, que es el coste marginal de un bloque».

---

### C-7 · BAJA — §3.1 prohíbe «oficial» y «bombonero» como perfiles y los publica tres filas más abajo

**Afirmación literal (SPEC:325 y :326):** «❌ «maestro chocolatero», «**bombonero**» y «**oficial**» **están
prohibidos**: no existen en el kit» · fila siguiente: «Salario de mercado (sólo orientativo) | Chocolatero `CHS-69a` ·
**oficial de primera** `CHS-69b` · auxiliar `CHS-69c` · encargado `CHS-69d`».

**Problema.** Las tres categorías salariales son correctas y las he verificado en el JSON (11-13 · 8-9,50 · 15-20 €/h),
pero el `tema` de `CHS-69a` es literalmente «Salarios de mercado — **Chocolatero / bombonero especializado**». La SPEC
prohíbe dos palabras y las pone en la tabla contigua sin decir que son etiquetas de la fuente, no perfiles del producto.
Un redactor resolverá la contradicción por su cuenta.

**FIX.** Añadir a la celda de SPEC:326: «⚠️ «oficial de primera», «auxiliar» y «bombonero» son **las etiquetas de la
fuente salarial**, no perfiles de La Almendra: se citan entrecomilladas y **junto a la equivalencia con los tres
perfiles del kit** (Encargado · Chocolatero · Dependiente), nunca como nombre de puesto».

---

### C-8 · BAJA — Los 75 m² se apoyan en dos traspasos de churrería-chocolatería, el negocio que D1 separa, y dejan fuera el único traspaso de bombonería con obrador del censo

**Afirmación literal (SPEC:322):** «Superficie total | **75 m²** | Convergencia de tres fuentes: `CHS-03` (60-100 m²),
traspasos reales de `CHS-37a` (75 m²) y `CHS-37b` (74 m²), y mínimo de franquicia de `CHS-58` (55 m²)».

**Problema.** Leídos en el JSON: `CHS-37a` = «Traspaso real — **chocolatería-churrería**, Elche» y `CHS-37b` = «Traspaso
real — **churrería-chocolatería**, Madrid (Vallecas)». Son el formato que D1 declara «**OTRO negocio**» y que el cap. 01
dedica un epígrafe entero a separar. Mientras tanto, `CHS-38a` —«Traspaso real — **pastelería-bombonería con obrador**
(40+ años), El Prat, **90 m²**, obrador completamente equipado»— es el comparable más cercano que existe en el censo y
no entra en la convergencia. No invalida los 75 m² (el reparto por zona ya es «supuesto declarado»), pero el argumento
de convergencia es más débil de lo que aparenta y `CHS-38a` tira al alza.

**FIX.** SPEC:322 → «Convergencia de cuatro fuentes, **con su formato dicho**: `CHS-03` (bombonería artesana, 60-100 m²),
`CHS-38a` (**pastelería-bombonería con obrador**, 90 m², el comparable más cercano del censo), `CHS-58` (mínimo de
franquicia, 55 m²) y, **como referencia de otro formato** (D1), los traspasos de churrería-chocolatería `CHS-37a`
(75 m²) y `CHS-37b` (74 m²). Se elige **75 m²** por estar dentro de `CHS-03` y por debajo de `CHS-38a`, y es
**supuesto declarado**».

---

### C-9 · BAJA — D35 baja al libro 6 las 12 filas del `BONUS-02` mientras el cap. 18 tiene prohibido «repetir el calendario del kit»

**Afirmación literal:** SPEC:238 (libro 6, hoja) «**Calendario de Campañas** (las 12 filas del kit, D35)» ·
SPEC:442 (cap. 18, prohibido) «**repetir el calendario del kit (K2)**» · SPEC:197 (D30) «la guía **no reescribe** la
tabla: la cita».

**Problema.** Para la vida útil la SPEC decidió citar y no reescribir (D30, C1); para el calendario decidió lo contrario
(D35), y sin decir por qué. Coexisten en el mismo documento con una prohibición explícita que apunta al mismo objeto.
La distinción es defendible —el calendario es el **eje** sobre el que el libro 6 pone los euros, mientras que la tabla
de vidas útiles **es** el entregable del libro 5— pero no está escrita, y quien construya el libro 6 o escriba el cap.
18 se va a topar con las dos instrucciones.

**FIX.** Añadir a D35 (SPEC:202): «**Por qué aquí sí y en el libro 5 no:** en el 5 la tabla del kit **es** el entregable
(por eso se cita, D30); en el 6 las 12 filas son el **eje** sobre el que se calculan los euros, así que bajan como
etiquetas de fila declaradas «copia de `BONUS-02-calendario-anual-tareas.xlsx!Calendario`», **sin reescribir sus
“Acciones clave” ni sus “Productos destacados”**. El cap. 18 sigue sin repetir el calendario: **remite al kit y sólo
narra los euros** (K2).»

---

## Resumen para quien aplique las correcciones

**Antes de escribir `datos_ejemplo.py`** (bloquean el juego de datos): **A-2** (base de IVA del precio de cobertura y del
PVP) y **A-5** (los ocho alérgenos y la corrección del kit en el mismo commit).

**Antes de construir los 9 libros:** **A-4** (los cinco cruces y su gate), **B-8** (canal → epígrafe como pregunta, no
como veredicto), **B-5** (columna de taza y churros en el libro 7) y **B-1** (recuentos de línea de §2.4, que dimensionan
a los cinco constructores).

**Antes de escribir el guion:** **A-3** (`CHN-22` como inferencia declarada + art. 2.15 ter), **B-6** (artesanía, que es
un epígrafe nuevo del cap. 09) y **C-9** (la regla de por qué el 6 copia y el 5 cita).

**Antes de la capa de producto:** **A-1** (las 12 FAQ reescritas antes de copiarlas, más su gate), **B-3** (la prueba de
la plantilla de las seis FAQ de `/usos/`), **B-4** (no hay rotación retroactiva de banners) y **B-9** (texto de la
tarjeta, D4).

**Antes de firmar el presupuesto con John:** **B-2** — si son dos libros sin molde y no tres, la fila «Los 9 libros»
baja de 3,15 a 2,80 M y el ciclo completo de 14,35 a **14,00 M**.

Lo que **no** hace falta re-verificar está en el veredicto: los 28 hallazgos resueltos, los literales legales contra el
JSON, los 160 ids citados, las vidas útiles, las temperaturas, las campañas y el valle contra los xlsx del kit, la suma
de §9, la aritmética de los 21 capítulos, los 40 bloques, el reparto de constructores, las referencias `fichero:línea`
de §7 y §8 (salvo la de C-1), el 404 del slug y la cobertura de `robots.txt`.

**Via: Claude Code**
