# Refutación de la SPEC de «Cómo Montar una Chocolatería» — RONDA 2 (2026-09-12)

Objeto: `scripts/productos-digitales/guia-chocolateria-SPEC.md` (798 líneas, §0-§10 + Cierre).
Método: verificación contra los ficheros, nunca contra la memoria — 635 ids del JSON común leídos con
`json`, 109 fichas de la verificación legal leídas una a una, los **11 xlsx del kit** abiertos con
`openpyxl read_only` (uno cada vez; CPU 52,2-52,9 °C en toda la pasada), `documentos.py`,
`verificar_guion.py`, `gen_*.py` de Pastelería, los 8 posts del blog, el hub ×2, `use-cases-content.*`,
`robots.txt`, `sinonimos-buscador.json` y `curl` a producción.

## Veredicto: **CORREGIR ANTES**

**15 hallazgos: 6 ALTAS · 5 MEDIAS · 4 BAJAS.**
Ninguno tumba el producto; **cuatro de las seis altas tumbarían un libro o un capítulo si se construye
tal cual**, y dos de ellas son la reaparición exacta de defectos que esta misma familia ya pagó
(el cruce entre libros que publicó dos inversiones distintas en Pastelería, y el gate que no puede
pasar el caso conocido-bueno).

### Lo que SÍ está verificado y no hay que volver a mirar

| Comprobación pedida | Resultado |
|---|---|
| Los **28 hallazgos** de la refutación del research | resueltos uno a uno en §1.C y en el Cierre; muestreados A1/A3/A5/A6/A7/A9/A11/B1/B5/C1/C2/C5/C9 contra ficheros: correctos |
| Los **23 hallazgos de la ronda 1** | **23/23 aplicados**. Verificados los 23; `documentos.py` **1126/1131/1145/1150** ✓, `…HubPage.astro` **1447 comentario / 1448 `<section>` / 1464 `.map()`** ✓, `postprocess-transversal.py` fuera de `auditorias/` ✓, solape **≤1** ✓, escenario B **≈5.700-5.900 €** (5.670,69-5.894,25 recalculado a mano sobre `CHS-47b` = 5.740,29) ✓, los **siete** recuentos de `gen_*.py` remedidos con `wc -l` (13.196, más largo 2.720, más corto 1.142) ✓, cinco vitrinas de las FAQ censadas ✓ |
| **Ids inexistentes** (D44) | **cero**. 161 ids distintos citados; los 11 «bare» (`CHS-24/25/27/28/37/38/42/45/46/47/69`) aparecen **sólo en la línea 233**, que es donde D44 los prohíbe; los 6 `CHN-*` que faltan del JSON común (`49d, 50, 70, 79, 80, 98`) están **los seis en `-EXCLUIDOS.json`** y la SPEC los cita como excluidos |
| **Presupuesto §9** | **suma**: 5,40 + 6,50 = 11,90 · 11,90 + 2,10 = 14,00 · los 9 libros 7×0,30 + 2×0,35 = 2,80 · 40 bloques × 0,1125 = 4,50 · Pastelería 2,06+0,50+0,38+0,60+2,79+4,90+0,71+1,50 = 13,44 ✓ |
| **Aritmética del índice** | las **21 sumas** de `puntos_por_epigrafe` cuadran, los epígrafes listados coinciden con los factores en las 21 filas, todos dentro de `EPI_MIN/MAX 4-6` y `PUNTOS_POR_EPI 2-5` ✓. Palabras: 16×1.750 + 4×2.100 + 1.500 = **37.900**, +2,43 % sobre `palabras_objetivo 37000` (el gate falla a >3 %) ✓. Bloques: 6×2 + 14 + 1 + 12 + 1 = **40** ✓ |
| **Reconciliación con el kit** | **real**: las 10 vidas útiles de `02!Moldeado`, la regla de merma, las temperaturas de `01`, los 3 hojas de campaña de `06`, las 12 filas del `BONUS-02` (**7 Alta · 4 Media · 1 Baja**, agosto único «Baja») y las tres listas de alérgenos (6/6/**5**) son **literalmente** lo que dice §1.B. *Salvo el punto **R2-A5**.* |
| Cruces, huérfanos y moldes | los 9 libros se reparten en C1-C5 sin dejar ninguno huérfano; ningún nombre de fichero repite uno de Pastelería; `kit-escandallos/05-pasteleria.xlsx` = `Instrucciones · Tarta Chocolate · Croissants · Macarons · Conversiones · Mermas` (D38 correcta); `pack-appcc` 21 xlsx ✓ |
| Slug y rutas | `curl -sI https://aichef.pro/guia-chocolateria-obrador` → **404** ✓; `robots.txt` cubre `/guia-*-access` y `/guia-*-library` en las líneas **35-36 · 53-54 · 71-72 · 89-90 · 107-108** ✓; `sinonimos-buscador.json` tiene **8 grupos** y ninguno menciona chocolate, cacao, bombón ni templado ✓ |
| Baselines de §0 | catálogo **48**, `payment-links` **48**, `product-prices` **48**, `zona-app grep -c productId:` **49**, fichas de guías **10** ✓ |
| Blog | los **8 posts** existen y tienen **exactamente 3 `<aside>`** cada uno; los cuatro banners a sustituir (`kit-plan-financiero`, `pro-prompts-ebook`, `kit-tareas-sushi-bar`, `kit-tareas-asador`) están donde dice §7.2 ✓; `fase8i` existe y `fase8j` está libre ✓ |
| Prohibiciones | las **29** del resultado legal están en §5.1 una a una y **ninguna aparece afirmada** en ningún punto de la SPEC ✓ |
| Los dos PENDIENTES legales | recogidos: **D47** (etiqueta vs granel) y **D48** (árbol operador/comerciante + tabla de clientes del art. 5.3.b) ✓ |

---

## A — ALTAS

### R2-A1 · ALTA — D37 **invierte las dos bases de cálculo** del RD 1055/2003, y la que invierte es la del bombón: choca con `CHN-10` y con la propia §3.2

**Afirmación literal (SPEC:226, D37):** «…y con **dos bases de cálculo** (ap. 4: **para el 1.10 y el 1.13 el
mínimo se calcula deduciendo el relleno**; el 25 % del bombón, **sobre el peso total, relleno incluido**)».

**Problema.** Las dos mitades del paréntesis se contradicen entre sí y la primera es **falsa**. `CHN-10`
(nivel A, cita literal) dice exactamente lo contrario: *«En el caso de los productos definidos en los
apartados **1.10 y 1.13**, los contenidos del chocolate **se calcularán en relación con el peso total del
producto acabado, incluido el relleno**»*, y la deducción es la de **1.6-1.9, 1.11 y 1.12** («se calculan
descontando los ingredientes del apartado 3»). Es decir: **la base que la SPEC atribuye al bombón es
justo la del producto que no es el bombón.** La §3.2 lo dice bien tres párrafos después («Bombones…
**≥25 % de chocolate sobre el peso TOTAL, relleno incluido**» y «Tabletas… en 1.6-1.9 / 1.11 / 1.12
**descontando los ingredientes añadidos**»), así que la SPEC lleva las dos versiones y **la mala es la que
manda**: D37 es la decisión que construye la hoja «Denominaciones y Mínimos Legales» del libro 4 y
alimenta el epígrafe «La tabla de mínimos y **las dos bases de cálculo**» del cap. 10. Con la base
invertida, la capa (a) («el 25 % … que sale solo de los gramajes que el lector ya mete») **se calcula sobre
el peso del bombón sin relleno** y da un resultado más favorable que el legal: una referencia que no
cumple el 25 % pasaría el semáforo.

**Evidencia.** `SPEC:226` · `SPEC:360` (tabletas, correcto) y `SPEC:359` (bombones, correcto) ·
`guia-chocolateria-verificacion-legal-2026-09-12.json` → `CHN-10`, `cita_literal` y `dato` · `CHN-03`
(25 % del peso total) · `CHN-82` (praliné, mismo 25 %).

**FIX.** SPEC:226, sustituir el paréntesis por: «(**ap. 4, y son dos bases opuestas**: en **1.6-1.9, 1.11 y
1.12** los mínimos se calculan **descontando los ingredientes añadidos del ap. 3**; en **1.10 (chocolate
relleno) y 1.13 (bombón)** el contenido de chocolate se calcula **sobre el peso total del producto acabado,
relleno incluido** — `CHN-10`)». Y añadir a la lista negra del §5.1: «❌ “el 25 % del bombón se calcula
descontando el relleno”».

---

### R2-A2 · ALTA — Falta el cruce **7 ← 2**: el libro 7 trae la hoja «Inversión Inicial» del molde y nadie le pasa el CAPEX del libro 2 → **dos inversiones totales distintas en el mismo pack**, que es el defecto ALTO que Pastelería ya pagó

**Afirmación literal (SPEC:261, libro 7):** hojas «0. Supuestos · **Inversión Inicial** · PyG 3 Años · … ·
**Financiación** …», y su columna de entradas: «tickets/día; ticket medio sin IVA; días de apertura;
estacionalidad…; rampa de arranque; brutos de convenio; % de SS; **condiciones de deuda**; por canal…;
**capacidad diaria traída del libro 1**…; **precio de cobertura … traído del libro 3**…; escenario de
formato». **No hay ninguna entrada de CAPEX ni de inversión.**

**Problema.** El molde heredado **sí** construye esa hoja con sus propias celdas verdes:
`gen_plan-financiero-3-anos-pasteleria.py:743-825` define `H_INV = 'Inversión Inicial'`, un
`DEFECTO_CAPEX` con un valor por defecto **por partida**, `_FILA_CAPEX` para las ocho partidas y la fila
`'CAPEX (inversión sin el fondo de maniobra)'`. O sea: el libro 7 **vuelve a pedir el CAPEX entero**, y el
libro 2 lo calcula por su cuenta. §2.3 declara **CINCO** cruces y el gate nuevo de `gate_libros.py` exige
que salgan **exactamente cinco filas de CUADRE**, así que el constructor C4 no tiene ni permiso ni sitio
para cuadrar su inversión con la del libro 2 — y la §3.4 le pide además «**40 % recursos propios / 60 %
préstamo**», que se dimensiona sobre esa cifra. Es literalmente lo que §2.3 dice que no puede volver a
pasar: «*el fondo de maniobra calculado dos veces publicó **dos inversiones totales distintas en el mismo
pack***». El libro **9** sí tiene su cuadre contra el CAPEX del 2; el **7**, que es el que publica la
inversión en el business plan del bonus 1, no.

**Evidencia.** `SPEC:261` (entradas y hojas del libro 7) · `SPEC:279-289` (la tabla de los cinco cruces y
el gate «deben salir CINCO») · `gen_plan-financiero-3-anos-pasteleria.py:75, 129-147, 743-825` ·
`SPEC:417` (40/60) · `SPEC:479` (bonus 1 «todas coherentes con el **libro 7**, celda a celda»).

**FIX.** (a) §2.3, añadir la **sexta** fila a la tabla de cruces: «**CAPEX total (Inversión Inicial)** |
**7** ← 2 | Celda verde «trae aquí la cifra de `calculadora-capex-chocolateria.xlsx!Resumen!<Celda>`»,
**con valor por defecto declarado**, + **fila de CUADRE con semáforo**; la hoja «Inversión Inicial» del
molde **no vuelve a pedir las ocho partidas**: pide el total y el fondo de maniobra». (b) Cambiar en
SPEC:221 (D32), SPEC:289 y SPEC:644 «**CINCO**» → «**SEIS**» (y ver R2-A3, que puede dejarlo en SIETE).
(c) Añadir esa entrada a la columna de entradas del libro 7 en SPEC:261.

---

### R2-A3 · ALTA — El libro 8 calcula la **fecha de apertura** y el libro 9 calcula el «**plazo crítico que mueve la fecha de apertura**»: sexto cruce no declarado, sin celda verde y sin cuadre

**Afirmación literal.** SPEC:262 (libro 8, salidas): «…**mes de cada hito, ruta crítica y fecha de
apertura**» · SPEC:263 (libro 9, salidas): «…**plazo crítico** que mueve la fecha de apertura» ·
SPEC:425 (§3.5): «Las duraciones son **supuesto declarado**; lo que no lo es son los **plazos de entrega de
maquinaria**, que **el lector teclea en el libro 9** y **son los que de verdad mueven la fecha**».

**Problema.** La SPEC dice a la vez (i) que la fecha de apertura la calcula el 8 con duraciones
supuestas y (ii) que lo que de verdad la mueve vive en el 9. Las dos salidas son la misma magnitud
calculada en dos libros con datos distintos: el comprador verá una fecha de apertura en el cronograma y
un «plazo crítico» incompatible en el checklist de equipamiento, sin una sola fila que le avise. Es el
mismo patrón de A-4 de la ronda 1 (los dos cruces del precio de cobertura que se quedaron fuera de la
lista) y el mismo de R2-A2. Y el gate de D32, que cuenta las filas de cuadre **contra la lista**, impide
resolverlo por iniciativa del constructor C5.

**Evidencia.** `SPEC:262`, `SPEC:263`, `SPEC:425`, `SPEC:283-289` (la lista cerrada de cruces).

**FIX.** §2.3, séptima fila: «**Plazo de entrega crítico de maquinaria** | **8** ← 9 | Celda verde «trae
aquí el plazo en semanas de
`checklist-equipamiento-y-proveedores-cacao.xlsx!Equipamiento!<Celda>`», con valor por defecto declarado,
+ **fila de CUADRE** que avisa si la ruta crítica del cronograma es más corta que ese plazo». Y en
SPEC:425 cerrar la frase: «…y por eso el cronograma **trae ese plazo por celda verde y lo cuadra**, en
lugar de suponerlo».

---

### R2-A4 · ALTA — El gate de alérgenos («`grep` de “frutos secos” en los 11 xlsx = **0**») **no puede pasar nunca**, y si se fuerza rompe la tabla de vidas útiles que §1.B.1 cita literalmente — y de él cuelga que el cap. 12 se escriba

**Afirmación literal (SPEC:660, §8.2):** «**Alérgenos kit↔guía** (A-5, D53) | `grep` de «frutos secos» en
los 11 xlsx de `kit-tareas-chocolateria` | **0 ocurrencias**… **Hasta que el kit esté regenerado, el
cap. 12 no se escribe**».

**Problema.** «Frutos secos» aparece hoy en **10 celdas** del kit y **sólo 3 son declaraciones de
alérgenos**. Las otras 7 son usos correctos e intocables del castellano: `02!Moldeado` t.3 «Añadir
inclusiones si aplica: **frutos secos**, frutas, sal», `02!Moldeado` fila 43 «**Bombones de praliné,
gianduja y frutos secos** | 2-4 meses» y fila 46 «**Frutos secos** garrapiñados…», `03!Mensual`
«Inventario completo: coberturas, **frutos secos**, licores, packaging», `05!Semanal` «Contar stock de
**frutos secos** y frutas deshidratadas», `05!Mensual` «Inventario: **frutos secos**, pralinés…» y
`BONUS-02!Calendario` septiembre «Bombones de **frutos secos**, praliné, especiados». El gate, tal como
está escrito, **falla siempre**: o se desactiva a la primera (y se pierde la señal, que es el
razonamiento con el que la ronda 1 corrigió el gate de solape), o alguien renombra esas celdas y
entonces **la fila «Bombones de praliné, gianduja y frutos secos» deja de existir** — la misma fila que
§1.B.1 publica como literal del kit y que D30 obliga a **citar sin reescribir**. Con la guía bloqueada
detrás («el cap. 12 no se escribe»), el gate roto para la sesión B2.

**Evidencia.** Barrido propio de los 11 xlsx con `openpyxl read_only` (10 aciertos, listados arriba) ·
`SPEC:660` · `SPEC:97-106` (la tabla de vidas útiles con la familia «…y frutos secos») · `SPEC:219`
(D30: la guía **cita** esa tabla) · precedente `C-6` de la ronda 1.

**FIX.** SPEC:660 → «**Alérgenos kit↔guía** (A-5, D53) | `grep` de «frutos secos» **en las tres celdas de
declaración de alérgenos** (`01!Apertura` t.2, `04!Dependiente` t.2, `06!Pascua` t.5) | **0 ocurrencias en
esas tres**; el gate **no mira el resto del kit**, donde «frutos secos» es el nombre correcto de un
ingrediente y de una familia de producto (7 celdas legítimas, incluida la fila de vida útil que la guía
cita)». Y añadir a D53 (SPEC:194-199) la misma acotación, para que el generador del kit no toque las 7.

---

### R2-A5 · ALTA — La reconciliación de temperaturas (§1.B.2 → D31) **se dejó fuera `08-apertura-cierre-negocio.xlsx` y `BONUS-01`**: el kit publica la humedad del obrador de **dos formas** y una humedad de **vitrina** que la SPEC no recoge

**Afirmación literal (SPEC:130, D31):** «**cuatro valores únicos en `datos_ejemplo.py`, y son los del
kit** — obrador al templar **18-20 °C / <60 % HR**, cámara **15-18 °C / 50-60 % HR**, nevera de rellenos
**0-4 °C**, sala de tienda **20-22 °C**», sobre una tabla (SPEC:120-128) que sólo cita `01` y `02`.

**Problema.** Barridos hoy los 11 ficheros, el kit publica dos objetivos más y uno de ellos **contradice
al que D31 fija como único**:

| Fichero · hoja · fila | Literal del kit | Choca con |
|---|---|---|
| `08-apertura-cierre-negocio.xlsx!Apertura del Negocio` f.21 (t.17) | «Verificar la temperatura y la humedad del obrador: objetivo **18-20 °C y 50-60 %**» | D31 fija «**menos del 60 %**» |
| `08-apertura-cierre-negocio.xlsx!Apertura del Negocio` f.20 (t.16) | «las vitrinas temperadas han alcanzado **16-18 °C y menos del 55 % de humedad**» | §1.B.2 no tiene HR de vitrina, y el libro 5 construye la hoja «Temperatura y Vitrina» |
| `BONUS-01-briefing-servicio.xlsx!Briefing` f.11 | «objetivo **18-20 °C y menos del 60 %**» | confirma la otra versión |
| `08!Cierre del Negocio` f.19 | «temperatura de cierre del obrador: objetivo **18-20 °C**» | — |

Son **cinco** magnitudes, no cuatro, y la humedad del obrador está publicada de dos maneras en un
producto vendido. El «<60 %» de D31 **contradice al `08`**, que además es la hoja que el changelog 2.0
del kit anuncia en la ficha pública («vitrinas temperadas (16-18 °C, menos del 55 % de humedad)»,
`src/data/productos-changelog.ts:651`). Y D30 había ordenado justo esto: «*las seis reglas K1-K6 se
vuelven a pasar **abriendo TODAS las hojas** de los 11 ficheros, no las primeras filas*» — para los
alérgenos se hizo (§1.B.6), para las temperaturas no.

**Evidencia.** Barrido propio de los 11 xlsx (líneas citadas arriba) · `SPEC:116-139` · `SPEC:219` (D30) ·
`src/data/productos-changelog.ts:651` y ss.

**FIX.** (a) Añadir a la tabla de §1.B.2 las dos filas del `08` y la del `BONUS-01`, con su fichero y
hoja. (b) SPEC:130 (D31) → «**cinco** valores únicos… obrador al templar **18-20 °C y 50-60 % HR**
—`08!Apertura del Negocio` t.17 es el más restrictivo y es el que manda, con la nota «*el 02 y el
BONUS-01 dicen “menos del 60 %”: la banda 50-60 % es la misma ventana leída por abajo*»—, cámara
**15-18 °C / 50-60 %**, nevera **0-4 °C**, sala **20-22 °C** y **vitrina 16-18 °C con menos del 55 % de
HR** (`08` t.16)». (c) Llevar la HR de vitrina a las entradas de la hoja «Temperatura y Vitrina» del
libro 5 (SPEC:259). (d) Anotar la incoherencia interna del kit en D53, para corregirla en la misma
regeneración 2.1.

---

### R2-A6 · ALTA — **D53 no baja a la capa de ejecución**: corregir el kit a 2.1 bloquea el cap. 12 y no está ni en §8.1, ni en §9, ni en §7.3 — y la regla de John obliga además a un correo propio

**Afirmación literal (SPEC:194-199, D53):** «…se regeneran por
`kit-tareas-v2_0/contenido_kit_tareas_chocolateria.py`, con changelog **2.1**… **Hasta que eso esté hecho,
el cap. 12 no se escribe**».

**Problema.** Es una decisión que toca **otro producto vivo** (`kit-tareas-chocolateria`, 12 €, hoy
**2.0** en `productos-changelog.ts:652`) y que **bloquea un capítulo de éste**, y no tiene dueño en
ninguna de las tres capas donde el trabajo se planifica:

- **§8.1 «Ficheros a tocar»** (29 filas) no incluye `kit-tareas-v2_0/contenido_kit_tareas_chocolateria.py`,
  ni los 11 xlsx regenerados de `public/dl/kit-tareas-chocolateria/`, ni la entrada **2.1** del changelog
  del kit (la fila 17-18 sólo habla del changelog **v1.0** de la guía).
- **§9** no tiene fila para ese trabajo (la fila «C · Capa de producto» enumera landing, zona app,
  dashboard, functions, catálogo, hub, changelog, imágenes, cripto, alias, `fase8x`, FAQ y email: el kit
  no aparece), así que los 14,00 M no lo cubren.
- **§8.2** sólo trae el `grep` (y ver R2-A4); no hay `censo-entregables.py --only kit-tareas-chocolateria`,
  ni verificación de descargas LIVE del kit tras regenerarlo.
- **§7.3** programa un único broadcast, el de la guía. La regla vigente de John (2026-09-05, `CLAUDE.md`)
  es «**cada vez que un producto digital se actualiza de versión (2.0, 2.1…) se programa un broadcast
  individual**, cola de 5 días»: el kit 2.1 necesita el suyo, y eso **desplaza el hueco** que §7.3 calcula.

**Evidencia.** `SPEC:194-199`, `SPEC:618-636` (§8.1), `SPEC:639-666` (§8.2), `SPEC:672-689` (§9),
`SPEC:606-612` (§7.3) · `src/data/productos-changelog.ts:651-653` (`version: '2.0'`) · `CLAUDE.md`,
regla de correos de producto.

**FIX.** (a) §8.1, fila nueva **30**: «`scripts/productos-digitales/kit-tareas-v2_0/contenido_kit_tareas_chocolateria.py`
+ los 11 xlsx de `astro-site/public/dl/kit-tareas-chocolateria/` + `productos-changelog.ts`
(`kit-tareas-chocolateria` **2.0 → 2.1**, entrada «Los ocho alérgenos del Anexo II en las tres celdas de
declaración») — **regenerar por el generador, nunca a mano**; prerrequisito del cap. 12». (b) §9, fila
nueva en la sesión B1: «**Kit de Chocolatería 2.1** (D53) | sonnet | **0,15 M**», y subir el total a
**12,05 / 14,15 M** (banda alta 14,50-14,70). (c) §8.2, añadir `censo-entregables.py --only
kit-tareas-chocolateria --fail` y la verificación LIVE de sus 11 descargas. (d) §7.3, añadir: «**el kit
2.1 lleva su propio broadcast** (regla del 5-sep): se programa **antes** que el de la guía y el hueco de
ésta pasa a ser el siguiente +5 días».

---

## B — MEDIAS

### R2-B1 · MEDIA — El convenio de Madrid se cita con una denominación que **no es la oficial** y que no está en ninguna ficha

**Afirmación literal (SPEC:349):** «**Convenio de Madrid, código 28001025011981**, «**CONFITERIAS
PASTELERIAS Y BOLLERIAS**», tablas 2026 a **15 pagas**…».

**Problema.** `CHN-65c` (nueva, consultada en REGCON el 12-09-2026, con la fila literal como
`cita_literal`) dice: «Código 28001025011981, denominación oficial «**CONFITERIAS PASTELERIAS Y
REPOSTERIA (COMERCIO E INDUSTRIA)**»». Barridas las 109 fichas, **la cadena «BOLLERIAS» no aparece en
ninguna**. Es una tabla salarial que va al producto marcada como ejemplo **y con su código delante**:
quien la busque en REGCON por ese nombre no la encuentra, y el método que el cap. 17 enseña
(«identificar tu convenio por denominación y ámbito») queda desmentido por el propio ejemplo. La regla de
la casa para lo legal es entrecomillar sólo lo que está en la fuente.

**Evidencia.** `SPEC:349` · `CHN-65c` (`dato` y `cita_literal`) · `CHN-65` (lo que sí es literal del art. 2
del convenio: «Confitería, Pastelería, Bollería y Repostería» — **texto del articulado**, no denominación
del registro).

**FIX.** SPEC:349 → «**Convenio de Madrid, código 28001025011981**, denominación oficial en REGCON
«**CONFITERIAS PASTELERIAS Y REPOSTERIA (COMERCIO E INDUSTRIA)**» (`CHN-65c`), vigencia 01/01/2024-31/12/2026
con revisión salarial de 28/02/2026; su art. 2 incluye «la fabricación y venta de bombones… cuando la
actividad principal… sea la de Confitería, Pastelería, Bollería y Repostería» (`CHN-65`)».

---

### R2-B2 · MEDIA — El «semáforo de los 100 kg» del libro 8 **no tiene id**: sale de `PA-29c` (Pastelería), no de ninguna ficha `CHN-*`

**Afirmación literal (SPEC:262, salidas del libro 8):** «…**semáforo de los 100 kg y aviso de «demostrable
documentalmente»**…».

**Problema.** Ninguna de las 109 fichas `CHN-*` menciona los 100 kg ni el art. 13.9: la única cifra de
kilos verificada para el chocolate es `CHN-41` («≤500 kg/semana», art. 3, suministro a otros minoristas).
Los 100 kg y el «demostrarlo documentalmente» son **`PA-29c`**, de la verificación legal de **Pastelería**
del 10-sep («*no puede superar en ningún caso los 100 kg semanales, y hay que DEMOSTRARLO
DOCUMENTALMENTE*»). La SPEC no cita un solo id `PA-*` (0 ocurrencias) y su §3 declara que **sólo hay tres
orígenes válidos**, uno de ellos «un id `CHN-*` / `CHS-*` del JSON común». Además, la hoja donde vive es la
**Ruta Doméstica**, y D21 establece que para el bombón esa ruta **no está abierta por defecto** (letra b
no encaja; depende de la letra e de cada CCAA): un semáforo de 100 kg sin esa condición delante sugiere
que la ruta existe. Es exactamente el error de método que la propia SPEC prohíbe en §5.3: «copiar
redacciones legales de otros kits sin verificar».

**Evidencia.** `SPEC:262` · barrido de `CHN-*` (0 coincidencias con «13.9», «100 kg», «demostrable
documentalmente») · `guia-pasteleria-verificacion-legal-2026-09-10.json` → `PA-29c` · `PA-29c` **sí está**
en el JSON común (635) · `SPEC:338` (los tres orígenes) · `SPEC:210` (D21).

**FIX.** SPEC:262 → «…**semáforo del tope de 100 kg/semana del art. 13.9 y aviso de “demostrable
documentalmente” (`PA-29c`, reutilizada de Pastelería y verificada el 10-09-2026), que sólo se activa si
la celda «¿tu CCAA ha ampliado la lista por la letra e)?» está en “sí”**…». Y añadir a §3 la cuarta
procedencia legítima: «(d) un id **`PA-*`** del JSON común, **citado como reutilización con su fecha**».

---

### R2-B3 · MEDIA — Tres listas distintas de «capítulos que firma el verificador legal»: §4 marca 🔴 el **15** y no el **16**; §9 y D50 dicen lo contrario

**Afirmación literal.** SPEC:445 (leyenda): «🔴 = **lo firma el verificador legal antes de escribirse**»;
llevan 🔴 los capítulos **09, 10, 11, 12, 15 y 19** (SPEC:457-467) · SPEC:683 (§9): «Verificador legal de
los caps. **09, 10, 11, 12, 16 y 19**» · SPEC:437 (D50): «`bloques: 2` en los **seis** capítulos legales y
densos —**09, 10, 11, 12, 16 y 19**—».

**Problema.** El capítulo **15** («El precio del cacao») **no cita un solo id `CHN-*`** (sus ids son
`CHS-23`, `CHS-24a/b/d`) y es un capítulo de mercado; el **16** («Vida útil del relleno») lleva
`CHN-30`, `CHN-30b`, `CHN-31`, `CHN-38`, `CHN-88` **y es donde vive D47**, la decisión legal más reciente
del producto (art. 4.2 del RD 1021/2022 frente al autocontrol para el granel). Con las tablas como están,
el capítulo con la decisión legal nueva **no pasa por el verificador** y el de precios sí — y el
presupuesto de §9 paga la verificación del 16, que la tabla no pide.

**Evidencia.** `SPEC:445`, `SPEC:463` (cap. 15 🔴, ids sólo `CHS-*`), `SPEC:464` (cap. 16 sin 🔴, cinco
ids `CHN-*` y D47), `SPEC:683`, `SPEC:437`.

**FIX.** SPEC:463 → quitar el 🔴 del cap. 15; SPEC:464 → «**16** 🔴». Queda un único conjunto en los tres
sitios: **09, 10, 11, 12, 16 y 19**.

---

### R2-B4 · MEDIA — El anexo va como capítulo principal **sin ninguna cifra de xlsx**, y `verificar_guion.py` aborta

**Afirmación literal (SPEC:469, fila A):** «Va como **entrada 21 de `CAPITULOS`** para que el pipeline lo
escriba… | **Hojas de origen: —** | ids: Todos los `CHN-*` | Prohibido: **Cifras de sector: aquí sólo
normas**».

**Problema.** `verificar_guion.py` corre `revisa(CAPITULOS, 'GUIA', …, principal=True)` sobre **toda** la
lista, anexo incluido, y tiene dos comprobaciones que el anexo no puede pasar sin celdas:
`if principal and not CIFRAS_MIN <= len(cifras) <= CIFRAS_MAX: falla` (4-10) y, sin condición ninguna,
`if not cifras: falla(f'{cid}: sin ninguna cifra del producto')`. No hay excepción por `sin_numerar`
(esa clave sólo la usa `documentos.py` para no numerarlo). Pastelería lo resolvió dándole al anexo
**ocho `C()` de umbrales normativos** tomados de celdas `Parámetros` (art. 4.1, art. 9.3, sin gluten,
art. 13.9, los dos umbrales del art. 3, SMI). Tal como está la fila A, el gate que §8.2 manda dejar en
verde «antes de gastar un token de redacción» **aborta**.

**Evidencia.** `verificar_guion.py:60-62, 119-121, 179-185` · `guion_guia_pasteleria_obrador.py`, entrada
`'n': 21` (ocho `C()`) · `SPEC:469` · `SPEC:649` (el gate del guion).

**FIX.** SPEC:469, columna «Hojas de origen» → «`checklist-legal!Suministro a Otros Minoristas` ·
`checklist-legal!Ruta Doméstica` · `carta!Denominaciones y Mínimos Legales` · `plan-financiero!Personal`»,
y añadir a la fila: «**4-10 `C()` de UMBRALES NORMATIVOS** (25 % del bombón · 35/18/14 del chocolate a la
taza · 500 kg/semana y 25 % del art. 3 · 750 m² de la Ley 12/2012 · 5 kg/mes del art. 75.f) · referencia
anual del SMI), **nunca cifras de sector**: es lo que exige `verificar_guion.py` a todo capítulo
principal».

---

### R2-B5 · MEDIA — D5 dice que «los DOS literales» del EUDR están «confirmados letra a letra» por `CHN-22`, y el del art. 2.15 no es la cita literal de ninguna ficha

**Afirmación literal (SPEC:67, D5):** «**Los DOS LITERALES están confirmados letra a letra** por la
verificación legal (`CHN-22`): art. 38.3 «…» + art. 2.15 «“operador”, toda persona física o jurídica que
[…] introduce los productos pertinentes en el mercado o los exporta, **excluidos los operadores
posteriores**», los dos marcados **▼M2**».

**Problema.** `CHN-22` tiene **una sola** `cita_literal`, la del art. 38.3. El texto del art. 2.15 vive
sólo en su campo `nota` («el art. 2.15 excluye de la palabra “operador” a los operadores posteriores») y
la única cita literal de la familia 2.15 que existe es la de **`CHN-23`**, que es la del punto **15 ter**
(«operador posterior»). El gate de literalidad cubre **81 citas comprobables**, y esa frase entrecomillada
no es una de ellas. Es el mismo hueco que la ronda 1 abrió con A-3: el argumento más sensible del
producto (la fecha del EUDR) apoyado en una atribución más fuerte de lo que la verificación sostiene.

**Evidencia.** `CHN-22` (`cita_literal` = sólo 38.3) · `CHN-23` (`cita_literal` = art. 2, punto 15 ter) ·
resultado legal, aviso «CHN-22 tiene un salto que NO es cita» · `SPEC:67`.

**FIX.** SPEC:67 → «El literal del **art. 38.3** está confirmado letra a letra (`CHN-22`) y el de
«**operador posterior**» (art. 2, punto **15 ter**) también (`CHN-23`); **la exclusión “excluidos los
operadores posteriores” del punto 15 consta en la `nota` de `CHN-22`, no como cita del gate de
literalidad: se parafrasea, no se entrecomilla**, hasta que se abra el consolidado y entre como cita
propia».

---

## C — BAJAS

### R2-C1 · BAJA — `GuiaLandingPage.astro:22` es un comentario; `cryptoEnabledFor()` se evalúa en la **44**

**Afirmación literal (SPEC:78 en D16 y SPEC:635 en §8.1):** «**No hay nada que tocar en la plantilla**:
`GuiaLandingPage.astro:22` evalúa `cryptoEnabledFor(data.slug)` en build-time».

**Problema.** La línea 22 es prosa de un comentario de bloque; el `import` está en la **27** y la
evaluación, `const cryptoEnabled = cryptoEnabledFor(data.slug);`, en la **44**. La conclusión («no hay
nada que tocar») es correcta; la referencia, no. Es la misma clase de C-1/C-2 de la ronda 1 y aparece
**dos veces**.

**Evidencia.** `astro-site/src/components/pages/GuiaLandingPage.astro:27` y `:44`.

**FIX.** SPEC:78 y SPEC:635 → «`GuiaLandingPage.astro:44` (`import` en la `:27`)».

---

### R2-C2 · BAJA — §7.1 promete arreglar el banner de `guia-restaurante-peruano` «en la misma pasada» y §7.2 lo aplaza

**Afirmación literal.** SPEC:585 (§7.1, colaterales de D15): «(c) **Los dos posts de chocolate que venden
sushi, cocina peruana y asador se arreglan en la misma pasada de banners**» · SPEC:598 (§7.2): «…
`guia-restaurante-peruano` **queda anotado como segundo arreglo**».

**Problema.** Verificado en el corpus: `chocolateria-artesanal-e-ia-una-combinacion-innovadora.md`
tiene exactamente tres banners —`guia-restaurante-peruano`, `kit-tareas-chocolateria` y
`kit-tareas-sushi-bar`— y la guía sólo puede ocupar **uno**, así que §7.2 tiene razón y §7.1 promete algo
imposible en esta pasada. El que se quede sin arreglar es un post de chocolatería vendiendo cocina
peruana.

**Evidencia.** `astro-site/src/content/blog/es/chocolateria-artesanal-e-ia-una-combinacion-innovadora.md`
(3 `<aside>`, los tres destinos listados) · `SPEC:585` · `SPEC:598`.

**FIX.** SPEC:585 (c) → «Los dos posts de chocolate que venden sushi y asador se arreglan en esta pasada;
**`guia-restaurante-peruano` en el mismo post de chocolatería artesanal no cabe —sólo hay un hueco— y
queda anotado como segundo arreglo para la siguiente pasada de banners**».

---

### R2-C3 · BAJA — El paquete **pierde** el libro de turnos y coste de personal de la hermana y no lo declara en ninguna parte

**Afirmación literal (SPEC:265):** «**Los seis sustantivos quedan cubiertos con 9 libros**, que son el
paquete más grande de los cinco productos del ciclo (D29b)».

**Problema.** Los ocho libros de Pastelería incluyen `gen_plantilla-turnos-y-coste-personal.py` (**1.457
líneas**, el octavo de la suma de 13.196) y su cap. 14 «Turnos de Madrugada y Jornada Legal». En
Chocolatería no hay libro de turnos: el personal vive en **una hoja** del libro 7 y el cap. 17 se apoya
en `plan-financiero!Personal`. La decisión es defendible (aquí no hay madrugada ni jornada nocturna),
pero **no está escrita**: §2.2, §2.4 y §2.7 no la mencionan, así que un constructor que compare los dos
paquetes creerá que falta un libro, y el argumento «9 frente a 8» compara paquetes que no cubren lo
mismo.

**Evidencia.** `wc -l gen_plantilla-turnos-y-coste-personal.py` = 1.457 · `guion_guia_pasteleria_obrador.py`
cap. 14 · `SPEC:255-265`, `SPEC:295-307`, `SPEC:332`.

**FIX.** Añadir a §2.7 («Lo que NO se construye»): «**Plantilla de turnos y coste de personal**: en
Pastelería es un libro propio por la jornada de madrugada; aquí el obrador de chocolate no la tiene, así
que el personal se resuelve **en la hoja «Personal» del libro 7** y el cap. 17 lo explica. **No es un
olvido: es la única baja respecto al molde de la hermana.**»

---

### R2-C4 · BAJA — «Caja surtida: la denominación va **por pieza**» se queda con la mitad de `CHN-13`, y la caja es la unidad de venta del producto

**Afirmación literal (SPEC:363):** «**Caja surtida**: la denominación va **por pieza**, con la regla de
surtidos del ap. 1».

**Problema.** `CHN-13` dice que las denominaciones del ap. 1 son obligatorias **pero** que «en surtidos de
1.6-1.10 y 1.13 **pueden sustituirse por “chocolates surtidos” o “chocolates rellenos surtidos”**, con
**una única lista de ingredientes**». La formulación de la SPEC empuja a lo contrario de lo que la norma
permite justo en el formato que §3.2 declara «la unidad de venta real» (y que el bonus 2 convierte en la
decisión nº 4). Un redactor puede escribir que cada bombón de la caja necesita su denominación.

**Evidencia.** `CHN-13` (`dato` y `cita_literal`) · `SPEC:363` · `SPEC:365` (la caja como unidad de venta).

**FIX.** SPEC:363 → «**Caja surtida**: la denominación va por pieza **o, si el surtido es de 1.6-1.10 y
1.13, se sustituye por «chocolates surtidos» / «chocolates rellenos surtidos» con una única lista de
ingredientes** (`CHN-13`) — y ésa es una decisión de etiquetado, no una obligación».

---

## Qué hacer con esto

1. **R2-A1** se arregla en una línea y no puede esperar: alimenta el libro 4 y el cap. 10.
2. **R2-A2** y **R2-A3** son la misma familia que la A-4 de la ronda 1: la lista de cruces pasa de cinco
   a **siete**, y con ella el gate de `gate_libros.py`. Hacerlo **antes** de escribir los constructores,
   porque después el gate obliga a mentir o a desactivarse.
3. **R2-A4** y **R2-A5** obligan a volver al kit con los 11 ficheros abiertos —esta vez todas las hojas—
   antes de cerrar `datos_ejemplo.py`.
4. **R2-A6** es calendario y dinero: decide John si el kit 2.1 entra en esta sesión (y entonces el cap. 12
   se desbloquea) o si el cap. 12 se escribe con los ocho alérgenos y el kit se corrige después, con su
   correo propio.

Via: Claude Code
