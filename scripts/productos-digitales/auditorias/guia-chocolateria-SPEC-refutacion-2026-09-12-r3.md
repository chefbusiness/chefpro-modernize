# Refutación de la SPEC de «Cómo Montar una Chocolatería» — RONDA 3 (2026-09-12)

Objeto: `scripts/productos-digitales/guia-chocolateria-SPEC.md` (**849 líneas**, §0-§10 + Cierre).
Método: verificación contra los ficheros, nunca contra la memoria. En esta pasada se han abierto con
`openpyxl` (uno cada vez, CPU 54,0-55,4 °C) `02-partidas-produccion.xlsx`, `01-apertura-cierre.xlsx`,
`03-tareas-manager.xlsx`, `04-tareas-perfiles.xlsx`, `05-tareas-semanales-mensuales.xlsx`,
`06-eventos-temporada.xlsx`, `08-apertura-cierre-negocio.xlsx`, `BONUS-01` y `BONUS-02` del kit; se han
leído las **109 fichas** de la verificación legal y su `-EXCLUIDOS.json`, el **JSON común de 635 ids**, el
`resultados-wf_7fcee771.json` (29 prohibiciones + 13 avisos), los `gen_*.py` de Pastelería
(`wc -l` fichero a fichero), `productos-changelog.ts`, `GuiaLandingPage.astro`,
`ProductosDigitalesHubPage.astro`, `ProductosDigitales.tsx`, `use-cases-content.*`, `robots.txt` y
`curl` a producción.

## Veredicto: **CORREGIR ANTES**

**11 hallazgos: 2 ALTAS · 4 MEDIAS · 5 BAJAS.**
Las dos altas son **costuras entre las dos mitades** de la SPEC y **las dos las abrió la propia ronda 2**:
al subir la lista de cruces de CINCO a SIETE se quedaron dos frases en §2.5 diciendo «los cruces
declarados son los CINCO», y el cruce nuevo **7 ← 2** está redactado de una forma que **vuelve a producir
dos inversiones totales distintas** —el defecto exacto que venía a cerrar—, porque el CAPEX del libro 2
**incluye el fondo de maniobra** y el libro 7 lo vuelve a pedir.

### Lo que SÍ está verificado en esta ronda y no hay que volver a mirar

| Comprobación pedida | Resultado |
|---|---|
| **Los 15 hallazgos de la ronda 2** | **13 aplicados limpiamente** (R2-A1 D37 con el literal de `CHN-10` ✓ · R2-A4 acotado a tres celdas ✓ · R2-A5 cuatro filas nuevas en §1.B.2 y D31 a cinco valores ✓ · R2-A6 fila 30 de §8.1, dos gates, 0,15 M en §9, broadcast del kit, punto 6 de §10 ✓ · R2-B1 `CHN-65c` ✓ · R2-B2 `PA-29c` + cuarta procedencia ✓ · R2-B3 🔴 fuera del 15 y puesto al 16 ✓ · R2-B4 anexo con 4-10 `C()` y cuatro hojas de origen ✓ · R2-B5 D5 parafraseando el punto 15 ✓ · R2-C1 `:44`/`:27` ✓ en las dos apariciones · R2-C2 §7.1 alineado con §7.2 ✓ · R2-C3 §2.7 con la baja del libro de turnos ✓ · R2-C4 `CHN-13` completo ✓). **R2-A2 y R2-A3 se aplicaron a medias**: ver **R3-A1** y **R3-A2** |
| **Los 28 hallazgos del research** | 28/28 con su decisión en el Cierre; remuestreados A7/A8/A11/B5/C1/C2/C6/C9/C11 contra ficheros: correctos |
| **Ids** | **CERO ids inexistentes.** 162 ids distintos citados; los 11 «bare» (`CHS-24/25/27/28/37/38/42/45/46/47/69`) aparecen **sólo en la línea 244**, que es donde D44 los prohíbe; los 6 `CHN-*` que no están en el JSON común (`49d, 50, 70, 79, 80, 98`) están **los seis en `-EXCLUIDOS.json`** y la SPEC los cita como excluidos. (Matiz en **R3-M3**) |
| **Reconciliación con el kit — cada celda citada, abierta** | `02!Moldeado` **B21/B43/B46** ✓ · `01!Apertura` **B26** ✓ · `04!Dependiente` **B7** ✓ · `06!Pascua` **B17** ✓ · `03!Mensual` **B6** ✓ · `05!Semanal` **B23** ✓ · `05!Mensual` **B15** ✓ · `BONUS-02!Calendario` **C13** ✓. Las **10 filas de vida útil** (B39-B48/C39-C48) son literales ✓. `08!Apertura del Negocio` **t.16 = fila 20** («16-18 °C y menos del 55 % de humedad») y **t.17 = fila 21** («18-20 °C y 50-60 %») ✓; `08!Cierre` fila 19 ✓; `BONUS-01!Briefing` **B11** ✓. `BONUS-02`: **7 Alta · 4 Media · 1 Baja (agosto)** ✓. `06` tiene **tres** hojas de campaña ✓. **El gate de alérgenos de §8.2 es construible tal como está escrito** |
| **Aritmética del índice** | Las **21 sumas** de `puntos_por_epigrafe` cuadran una a una y el nº de factores coincide con el nº de epígrafes en las 21 filas; todas dentro de 4-6 epígrafes y 2-5 puntos. Palabras 16×1.750 + 4×2.100 + 1.500 = **37.900** (+2,43 % sobre 37.000, el gate falla a >3 %) ✓. Bloques 6×2 + 14 + 1 + 12 + 1 = **40** ✓ |
| **Presupuesto §9** | **Suma**: 0,55+0,50+0,30+2,80+0,60+0,65+0,15 = **5,55** ✓ · 4,50+0,40+0,60+0,75+0,25 = **6,50** ✓ · 5,55+6,50 = **12,05** ✓ · +2,10 = **14,15** ✓ · 14,15−13,44 = **0,71** ✓ · 7×0,30+2×0,35 = 2,80 ✓ · 40×0,1125 = 4,50 ✓. (La cifra **de D20** no: **R3-M1**) |
| **Escenarios de dotación** | `CHS-47b` = 5.740,29 → con el rango de moldes de D23a (12 × 24,20-42,83 = 290,40-513,96, menos los 360 € de «12 × 30») da **5.670,69-5.894,25** ✓ = «≈5.700-5.900». `CHS-47a` = 24.104,99 → **24.035-24.259** ✓ = «≈24.000-24.300». `CHS-29`: 20/12 = 1,67 y 45/35 = 1,29, caída del **23 %** ✓ |
| **Recuentos de `gen_*.py`** | Remedidos con `wc -l`: 1.142 · 1.453 · 1.457 · 1.515 · 1.589 · 1.610 · 1.710 · 2.720 = **13.196** ✓; los siete paréntesis de §2.4 correctos ✓ |
| **Literales legales** | `CHN-10` (dos bases, 1.10 y 1.13 sobre el peso total) ✓ · `CHN-22` (sólo el 38.3 es cita) y `CHN-23` (15 ter) ✓ · `CHN-13` ✓ · `CHN-16b` (puntos 2, 3 y 4) ✓ · `CHN-34b` (ocho) ✓ · `CHN-65/65b/65c` ✓ · `CHN-82` ✓ · `PA-29c` ✓. Las **29 prohibiciones** del resultado legal están en §5.1 y **ninguna aparece afirmada**; los **dos PENDIENTES** están en D47 y D48 ✓ |
| **Líneas de código citadas** | `GuiaLandingPage.astro` `:27` import / `:44` evaluación ✓ · `…HubPage.astro` `:973-975`, `:1143`, `:1447` comentario, `:1448` `<section>`, `:1464` `.map()` ✓ · `ProductosDigitales.tsx` `:958-960`, `:1080`, `:1227` ✓ · `use-cases-content.es.ts:1264/3248/1924/3138` y `…consultor.ts:386/393/505/1070` ✓ · `productos-changelog.ts:651` clave, `:652` `version: '2.0'`, `:660` la frase de las vitrinas ✓ |
| **Slug, robots y FAQ** | `curl -sI https://aichef.pro/guia-chocolateria-obrador` → **404** ✓ · `robots.txt` cubre `/guia-*-access` y `/guia-*-library` en los 5 bloques ✓ · la §14 del research abre en la **línea 922** y son **12 FAQ de compra**, con las de oficio y consumidor excluidas de oficio ✓ (D39) |
| **Libros** | Los 9 se reparten en C1-C5 sin huérfanos; ningún nombre de fichero repite uno de Pastelería; ninguna salida exige otro libro en tiempo de ejecución; el paquete no rehace ninguna tabla del kit |

---

## A — ALTAS

### R3-A1 · ALTA — §2.5 sigue diciendo **dos veces** «los cruces declarados son los CINCO de §2.3, y no hay más», después de que la ronda 2 los subiera a SIETE — y es la sección que reparte el trabajo a los constructores

**Afirmación literal (SPEC:328, constructor C1):** «⚠️ **No es un cruce: cada libro pide su dato al lector**
(los cruces declarados son **los CINCO de §2.3**, y no hay más)».
**Y (SPEC:330, constructor C3):** «⚠️ **No es un cruce: el 6 no trae ninguna celda del 4** (los cruces
declarados son **los CINCO de §2.3**)».

**Problema.** La ronda 2 subió la lista a **siete** y la SPEC la subió en todas partes menos aquí:
**D32 (SPEC:232)** dice «Los **SIETE** cruces», la tabla de **§2.3 (SPEC:292-300)** tiene **siete filas**,
el gate de **§2.3 (SPEC:302)** y el de **§8.2 (SPEC:662)** exigen que salgan «**SIETE**» filas de CUADRE.
Las dos frases que quedan en CINCO están **justo en las filas de C1 y de C3**, que son **los dos
constructores afectados por los cruces nuevos**: C1 construye el libro 2, que es el ORIGEN del cruce
7 ← 2, y C3 construye el 4 y el 6, que reciben del 3 y del 1. Un constructor que lea su propia fila
—que es lo que lee un agente al que se le asigna C1— cierra su libro con la lista de cinco, y después el
gate cuenta siete y falla; o peor, alguien «arregla» el gate bajándolo a cinco y vuelven a colarse los
dos cruces que la ronda 2 cazó. Es exactamente la mecánica con la que la ronda 1 documentó A-4.

**Evidencia.** `SPEC:328` y `SPEC:330` (CINCO) frente a `SPEC:232`, `SPEC:290`, `SPEC:292-300` (siete
filas), `SPEC:302` y `SPEC:662` (SIETE). Y `SPEC:791`, que ya lo dice: «la lista definitiva es de SIETE».

**FIX.** SPEC:328 → «⚠️ **No es un cruce entre estos dos libros: cada uno pide su dato al lector.** Los
cruces declarados son **los SIETE de §2.3**, y de ellos **C1 es el ORIGEN de dos** —el CAPEX del libro 2
que recibe el 7, y nada del 1 hacia el 2—: C1 **publica en `build/mapa-2.json` la celda del CAPEX** que el
libro 7 citará». SPEC:330 → «⚠️ **No es un cruce: el 6 no trae ninguna celda del 4.** Los cruces
declarados son los **SIETE** de §2.3; de ellos C3 **recibe dos** (el 4 ← 3 y el 6 ← 1) y **no origina
ninguno**». Barrido obligatorio antes de firmar: `grep -n "CINCO" guia-chocolateria-SPEC.md` debe
devolver **cero** ocurrencias referidas a cruces.

---

### R3-A2 · ALTA — El cruce nuevo **7 ← 2** trae **el CAPEX total, que INCLUYE el fondo de maniobra**, y el libro 7 vuelve a pedir el fondo: la corrección de R2-A2 **reproduce el defecto que venía a cerrar** (dos inversiones totales distintas). Además el libro 2 **no tiene entrada para los gastos fijos** con los que ese fondo se calcula

**Afirmación literal (SPEC:299, §2.3, fila del cruce 7 ← 2):** «Celda verde «trae aquí la cifra de
`calculadora-capex-chocolateria.xlsx!Resumen!<Celda>`»… ⚠️ **La hoja «Inversión Inicial» que se hereda del
molde NO vuelve a pedir las ocho partidas** …: pide **el total y el fondo de maniobra**, y el 40/60 de
§3.4 se dimensiona sobre esa cifra cuadrada».
Y **(SPEC:408, §3.3):** los ocho bloques de CAPEX del libro 2 son «obra y adecuación · climatización… ·
**fianza, licencias y fondo de maniobra**».
Y **(SPEC:267, entradas del libro 2):** «importe por partida (mín/máx/tuyo); variante; «¿lleva IVA?» y
tipo por línea; precio de traspaso; renta; horizonte en años; **meses de colchón**; kg/mes de plástico».

**Problema.** Tres defectos encadenados, y el tercero es el que publica dos cifras:

1. **El «total» del libro 2 lleva el fondo de maniobra dentro.** El fondo es **uno de los ocho bloques**
   (SPEC:408), así que el «CAPEX total» que el libro 2 publica en su `Resumen` (SPEC:267, columna de
   salidas) **ya lo contiene**. Si el libro 7 importa ese total **y además** pide el fondo de maniobra,
   el fondo se cuenta **dos veces** y la inversión total del business plan (bonus 1, «todas coherentes con
   el libro 7, celda a celda», SPEC:494) sale inflada en un colchón entero —**seis meses de fijos**,
   SPEC:432—. Y si no se cuenta dos veces, entonces «el total» del libro 2 y «la inversión inicial» del
   libro 7 son **dos magnitudes distintas con el mismo nombre**, que es la otra mitad del mismo defecto.
2. **El molde publica la cifra desagregada, y la SPEC pide la agregada.** En
   `gen_plan-financiero-3-anos-pasteleria.py` la hoja «Inversión Inicial» imprime **tres** renglones —
   `TOTAL`, `FONDO DE MANIOBRA` (línea 814-815) y **`CAPEX (inversión sin el fondo de maniobra)`**
   (línea 825)— y el libro de CAPEX hermano publica en su `Resumen` «**Del cual, fondo de maniobra (es
   caja, no inversión)**» (`gen_calculadora-capex-pasteleria.py:1083-1086`) y titula su variante
   «**“Inversión de apertura” es el CAPEX sin el fondo de maniobra, que es como publica sus cifras el
   sector**» (`:749`). La cifra que hay que traer es **ésa**, no «el total».
3. **El fondo de maniobra es un cruce OCULTO en sentido contrario (2 ← 7), y la lista cerrada de siete no
   lo tiene.** El fondo se calcula «**meses de colchón × gastos fijos mensuales**»
   (`gen_calculadora-capex-pasteleria.py:163, 188-191`), y **los gastos fijos mensuales del año de crucero
   los produce el libro 7**, no el 2 — el propio molde lo escribe en la nota de la celda: «*Es el mismo
   gasto fijo mensual que calcula, mes a mes, el libro 5 …, así que los dos libros publican el mismo
   fondo de maniobra y la misma inversión total. **Si cambias este valor, cámbialo también allí**.*»
   Esa nota es **la definición literal del defecto que Pastelería pagó**: un acoplamiento mantenido a mano.
   Y las entradas del libro 2 de esta SPEC (SPEC:267) **no incluyen los gastos fijos mensuales**, así que
   hoy el libro 2 **no puede calcular su propio fondo de maniobra con ninguna celda declarada**.

**Evidencia.** `SPEC:299`, `SPEC:267`, `SPEC:408`, `SPEC:432` (colchón de 6 meses), `SPEC:417` (40/60),
`SPEC:494` (bonus 1 celda a celda) · `gen_plan-financiero-3-anos-pasteleria.py:133, 743-825` (`I_FONDO`,
`I_FDM`, `I_CAPEX`) · `gen_calculadora-capex-pasteleria.py:101, 163, 183-191, 749, 1083-1086`.

**FIX.** (a) SPEC:299 → «Celda verde «trae aquí **el CAPEX SIN el fondo de maniobra** de
`calculadora-capex-chocolateria.xlsx!Resumen!<Celda>`», con valor por defecto declarado, + **fila de
CUADRE con semáforo**. ⚠️ **El «CAPEX total» del libro 2 INCLUYE el bloque «fianza, licencias y fondo de
maniobra»: lo que viaja es la línea «CAPEX sin el fondo de maniobra», y el fondo lo sigue calculando el
libro 7 con su propio «meses de colchón» × sus fijos. La hoja «Inversión Inicial» no vuelve a pedir las
ocho partidas: pide esa única cifra.**»
(b) Añadir a las salidas del libro 2 en SPEC:267: «**dos líneas separadas en «Resumen»: “CAPEX sin el
fondo de maniobra” y “Del cual, fondo de maniobra (es caja, no inversión)”**».
(c) **Octava fila en la tabla de §2.3**: «**Gastos fijos mensuales del año de crucero** | **2** ← 7 |
Celda verde «trae aquí los fijos mensuales de
`plan-financiero-3-anos-chocolateria.xlsx!PyG 3 Años!<Celda>`», con valor por defecto declarado, +
**fila de CUADRE** que compara el fondo de maniobra de los dos libros». Y subir a **OCHO** el contador de
D32 (SPEC:232), del gate de §2.3 (SPEC:302) y del de §8.2 (SPEC:662). *(Alternativa admisible, pero hay
que escribirla: que el fondo de maniobra **no sea bloque del libro 2** y viva sólo en el 7; entonces el
CAPEX del 2 ya es «sin fondo» por construcción y el cruce 2 ← 7 no hace falta. Lo que no puede quedarse
es el estado actual, donde la misma cifra se calcula en dos sitios sin fila de cuadre.)*
(d) Añadir a las entradas del libro 2 (SPEC:267) la celda de **gastos fijos mensuales**, o la nota que
diga de dónde vienen.

---

## B — MEDIAS

### R3-M1 · MEDIA — **D20 sigue firmando 11,90 / 14,00 M** cuando §9 suma 12,05 / 14,15: la decisión que dice «esta tabla SUMA» es la única que no está actualizada

**Afirmación literal (SPEC:220, D20):** «§9 de esta SPEC se recompone fila a fila: **construcción 11,90 M
en dos sesiones · ciclo completo con research 14,00 M**… **Gate de la SPEC: la fila TOTAL es la suma de su
columna** — se comprueba antes de firmar».

**Problema.** §9 fue recompuesta en la ronda 2 con la fila del kit 2.1 (0,15 M) y hoy suma
**5,55 + 6,50 = 12,05** y **12,05 + 2,10 = 14,15** (comprobado fila a fila arriba). §10 punto 5 lo dice
bien y explica los dos recálculos; la fila **R2-A6** del Cierre también. **La decisión firmada, no.** Y es
la decisión, no la tabla, lo que §1 declara «no se reabre al construir»: quien vaya a §1 a buscar el
presupuesto aprobado encuentra **14,00**, que es la cifra que John no tiene que aprobar. Encima la
propia D20 lleva dentro el gate «la fila TOTAL es la suma de su columna», así que se desmiente sola.

**Evidencia.** `SPEC:220` (11,90 / 14,00) · `SPEC:702, 709, 710` (5,55 / 12,05 / 14,15) · `SPEC:712`
(«14,15 frente a 13,44») · `SPEC:730` (§10 p.5) · `SPEC:829` (fila R2-A6).

**FIX.** SPEC:220 → «…se recompone fila a fila: **construcción 12,05 M en dos sesiones · ciclo completo
con research 14,15 M** (11,90 / 14,00 antes de bajar D53 a la capa de ejecución: la regeneración del kit
de 12 € a 2.1 son 0,15 M que no estaban presupuestados)…». Y anotar en `SPEC:794` (fila B-2 del Cierre)
que aquel «11,90 / 14,00» es el estado **de la ronda 1**, superado por R2-A6.

---

### R3-M2 · MEDIA — D31 obliga a publicar una nota que **D53 borra en el mismo commit**: tras regenerar el kit a 2.1, «el 02 y el BONUS-01 lo escriben como “menos del 60 %”» deja de ser cierto

**Afirmación literal (SPEC:231, D31):** «Obrador al templar **18-20 °C y 50-60 % HR** (`08!Apertura` t.17,
el más restrictivo; **el 02 y el BONUS-01 lo escriben “menos del 60 %”**)», con la nota obligatoria de
SPEC:134-137: «*el 02 y el BONUS-01 lo escriben como “menos del 60 %”: la banda 50-60 % es la misma
ventana leída por abajo*».
Y **(SPEC:210, D53):** «**Y en la misma regeneración 2.1 se corrige la incoherencia interna de las
temperaturas**… se unifica en **50-60 %**».

**Problema.** Las dos cosas no pueden ser verdad a la vez en el producto entregado. Si la 2.1 unifica
`02!Templado`, `02!Instrucciones` y `BONUS-01!Briefing` en «50-60 %» —y §8.1 fila 30 lo manda—, entonces
la nota que D31 obliga a escribir **dentro de la guía** describe una discrepancia que **ya no existe** en
el kit, y el comprador que abra los dos productos verá una guía explicando una contradicción que no
encuentra. Es el mismo error de método que §5.3 persigue («reescribir/citar mal lo que el kit de 12 €
publica»), sólo que en el tiempo: la SPEC cita **la 2.0** y entrega **la 2.1**. Verificado hoy que el
literal actual es el de la 2.0 (`02` y `BONUS-01!Briefing` B11 dicen «menos del 60 %»,
`08!Apertura` fila 21 dice «50-60 %»).

**Evidencia.** `SPEC:122, 129, 132, 134-137, 210, 231, 653` · barrido propio: `BONUS-01!Briefing` **B11**
= «objetivo 18-20 °C y menos del 60 %»; `08!Apertura del Negocio` **fila 21 (t.17)** = «18-20 °C y 50-60 %».

**FIX.** SPEC:134-137 y SPEC:231 → sustituir la nota por: «*hasta la versión 2.0 el `02` y el `BONUS-01`
escribían “menos del 60 %”; la **2.1 los unifica en 50-60 %** (D53), que es la misma ventana leída por
abajo. **La guía cita el kit 2.1**, y la nota de la celda verde dice sólo “objetivo 18-20 °C y 50-60 % de
HR (`kit-tareas-chocolateria`, `08-apertura-cierre-negocio.xlsx!Apertura del Negocio`)”*». Y añadir al
orden de dependencia de §8.1: **el kit 2.1 se regenera ANTES de cerrar `datos_ejemplo.py`**, no sólo antes
del cap. 12.

---

### R3-M3 · MEDIA — La lista de familias «que sólo existen con sufijo» de D44 **no casa con sus propios 11 ids bare**: faltan tres y sobra `CHS-41`, que **sí existe bare** en el JSON (agregado de fiabilidad baja)

**Afirmación literal (SPEC:244, D44):** «La síntesis cita `CHS-24`, `CHS-37`, `CHS-38`, `CHS-47`, `CHS-69`,
`CHS-25`, `CHS-27`, `CHS-28`, `CHS-42`, `CHS-45` y `CHS-46`, y en el JSON **sólo existen con sufijo**
(`CHS-24a…d`, `CHS-37a/b/c`, `CHS-38a…e`, `CHS-47a/b`, `CHS-69a…d`, **`CHS-41a…j`**, `CHS-42a…j`,
`CHS-45a/b`, `CHS-46a…f`)».

**Problema.** Censado el JSON común (635 entradas): de los **once** ids bare de la primera lista, el
paréntesis sólo documenta **ocho** —**faltan `CHS-25a…d`, `CHS-27a/b` y `CHS-28a…d`**, y `CHS-28a` es
precisamente la celda más crítica del paquete (el precio de la cobertura, §3.3)—, y a cambio incluye
**`CHS-41`, que NO está en la lista de bare porque en el JSON existe también SIN sufijo**:
`CHS-41` = «Atemperadoras — la escalera completa (síntesis)», cifra «14 (factor entre extremos)»,
**fiabilidad baja**, con la nota «[AGREGADO sin fuente única…]». O sea: el único id de la familia que la
regla debería marcar como **prohibido por otro motivo** (agregado sin fuente, que §4 manda tratar como
«hueco deliberado») está listado como si fuera inexistente, y `verificar_guion.py` —que sólo comprueba
existencia— **lo dejaría pasar**.

**Evidencia.** Censo propio sobre `auditorias/guias-v2-research-sector.json`: `CHS-25` → a,b,c,d ·
`CHS-27` → a,b · `CHS-28` → a,b,c,d · `CHS-41` → **bare + a…j** · el resto, como dice la SPEC.
Ficha `CHS-41`: `fiabilidad: baja`, `nota` «AGREGADO sin fuente única — escalera resumida de las
atemperadoras CHS-41a…j». `SPEC:244`, `SPEC:456` (la regla del hueco deliberado).

**FIX.** SPEC:244 → «…y en el JSON **sólo existen con sufijo** (`CHS-24a…d`, **`CHS-25a…d`**,
**`CHS-27a/b`**, **`CHS-28a…d`**, `CHS-37a/b/c`, `CHS-38a…e`, `CHS-42a…j`, `CHS-45a/b`, `CHS-46a…f`,
`CHS-47a/b`, `CHS-69a…d`). ⚠️ **`CHS-41` es la excepción: existe también SIN sufijo, y su ficha bare es un
AGREGADO sin fuente única con `fiabilidad: baja` («factor 14 entre extremos de la escalera»). Está
PROHIBIDO citarla: las atemperadoras se citan `CHS-41a…j`, una a una.** `verificar_guion.py` no puede
cazar esto —el id existe—, así que va también a la lista negra de §5.2».

---

### R3-M4 · MEDIA — §8.1 manda tocar **3** páginas `/usos/` y §0 y §7.1 prometen **4**: la página de heladería se cae en la capa de ejecución

**Afirmación literal (SPEC:650, §8.1 filas 23-25):** «Cross-sell, desplegable del admin (**49**) y
`productIds` de **las 3 páginas de rol** más las SEIS FAQ de D27 en los 7 idiomas».
Frente a **§0 (SPEC:40):** «**4 páginas `/usos/`**» y **§7.1 (SPEC:595):** «las **4** que anuncia §0 …
las **tres seguras** … **más UNA de heladería** por la variante chocolatería-heladería: se elige entre
`:1924` y `:3138` abriendo las dos… Enlace **bidireccional** en las cuatro».

**Problema.** §8.1 es la lista de la que sale el commit: si dice tres, se hacen tres, y el enlace
entrante de la página de heladería —el único que §7.1 deja sin decidir cuál de las dos es— **no se
ejecuta nunca**. Es la misma clase de B-9 de la ronda 1 (una decisión que no baja a la capa donde el
trabajo se planifica), y choca con la regla capital de interenlazado. Verificado que las dos candidatas
existen y son ambiguas por el `productIds`: `use-cases-content.es.ts:1924` y `:3138` tienen **la misma
lista** (`kit-tareas-heladeria`, `kit-escandallos`, `pack-appcc`…), así que la elección **sólo** puede
hacerse abriendo el cuerpo, como dice §7.1.

**Evidencia.** `SPEC:40`, `SPEC:595`, `SPEC:650` · `use-cases-content.es.ts:1264`, `:3248`, `:1924`,
`:3138` y `…consultor.ts:386` verificados línea a línea.

**FIX.** SPEC:650 → «…`productIds` de **las CUATRO páginas de rol** —`chocolatero` (`es.ts:1264`),
`chocolateria` (`es.ts:3248`), `chocolatero-consultor` (`es.consultor.ts:386`) y **la de heladería que se
elija entre `es.ts:1924` y `es.ts:3138` abriendo las dos** (§7.1)—, con el slug **en primera posición** y
enlace **bidireccional**, más las SEIS FAQ de D27 en los 7 idiomas».

---

## C — BAJAS

### R3-B1 · BAJA — §0 sigue fijando el correo en el **24-oct** después de que §7.3 lo moviera al **29-oct** al meter delante el broadcast del kit

**Afirmación literal (SPEC:40):** «…rotación general, **lista de compradores (Resend, 24-oct)**…».
**Frente a SPEC:627:** «**Se programa ANTES que el de la guía** … **si el kit 2.1 ocupa el 24-oct, la guía
va al 29-oct**».

**Problema.** La ficha del producto —lo que se copia al handoff— publica una fecha que §7.3 ya declara
condicionada y probablemente desplazada. D8 (SPEC:70) al menos va marcada «matizada por D28»; §0 no.

**FIX.** SPEC:40 → «lista de compradores (Resend, **24-oct condicionado y detrás del kit 2.1: ver §7.3**)».

---

### R3-B2 · BAJA — La entrada de changelog del kit 2.1 que dicta §8.1 **sólo menciona los alérgenos**, y la regeneración cambia además la humedad publicada

**Afirmación literal (SPEC:653, §8.1 fila 30):** «…la humedad del obrador unificada en 50-60 % (R2-A5), y
entrada de changelog «**Los ocho alérgenos del Anexo II en las tres celdas de declaración**»».

**Problema.** El changelog es lo que ve el comprador del kit de 12 € cuando le llega el correo de la 2.1
(§7.3), y la 2.1 **cambia un valor operativo que él usa cada mañana** —la humedad objetivo del obrador en
`02!Templado`, `02!Instrucciones` y `BONUS-01!Briefing`—. Anunciar sólo los alérgenos deja el cambio de
humedad sin rastro, que es justo lo que un changelog existe para evitar.

**FIX.** SPEC:653 → entrada de changelog «**Los ocho alérgenos del Anexo II en las tres celdas de
declaración, y la humedad objetivo del obrador unificada en 50-60 % en las cuatro hojas que la publican
(antes “menos del 60 %” en el 02 y en el BONUS-01)**».

---

### R3-B3 · BAJA — El art. 13.9 tiene **tres** obligaciones y el libro 8 publica dos: falta «**proporcional al tamaño de las instalaciones**»

**Afirmación literal (SPEC:273, salidas del libro 8):** «semáforo del **tope de 100 kg/semana del art. 13.9**
y aviso de «**demostrable documentalmente**» (`PA-29c`…)».

**Problema.** El `tema` de `PA-29c` es literalmente «**El art. 13.9 tiene TRES obligaciones, no una**», y
su cita literal empieza por la que falta: «*El volumen total de alimentos preparados deberá ser
**proporcional al tamaño de las instalaciones** de manera que se garanticen unas prácticas correctas de
higiene alimentaria y **en ningún caso** podrán superar los 100 kilogramos semanales, lo cual **se
demostrará documentalmente**…*». Su propia nota avisa de que «el tope de 100 kg casi nunca se alcanza en
una cocina doméstica»: es decir, **la obligación que de verdad muerde es la que se ha quedado fuera**. Es
la misma media ficha que R2-C4 cazó en `CHN-13`.

**FIX.** SPEC:273 → «…**los tres requisitos del art. 13.9**: volumen **proporcional al tamaño de las
instalaciones** (que es el que de verdad limita: el tope casi nunca se alcanza en una cocina doméstica),
tope de **100 kg/semana** y **demostrable documentalmente** (`PA-29c`, reutilizada de Pastelería y
verificada el 10-09-2026)…».

---

### R3-B4 · BAJA — §3.2 entrecomilla «chocolates surtidos» / «chocolates rellenos surtidos», que **no están en la `cita_literal` de `CHN-13`** — la misma regla que D22 impone

**Afirmación literal (SPEC:378):** «…se sustituye por «**chocolates surtidos**» / «**chocolates rellenos
surtidos**» con una ÚNICA lista de ingredientes (`CHN-13`, aps. 6.a) y 6.c))».

**Problema.** La `cita_literal` de `CHN-13` es sólo «*podrá haber una única lista de ingredientes para el
conjunto de productos que compongan el surtido*»; las dos denominaciones viven en su campo `dato`, y por
tanto **no están entre las 81 citas que pasan el gate de literalidad**. La regla de la casa la escribe la
propia SPEC en D22: «**Se entrecomilla únicamente lo que está en el BOE**». Es el mismo hueco que R2-B5
cerró para el art. 2.15 del EUDR, y aquí quedó abierto.

**FIX.** SPEC:378 → dejar las dos denominaciones **sin comillas de cita** («…se sustituyen por las
denominaciones de surtido que prevé el ap. 6.c) —chocolates surtidos y chocolates rellenos surtidos—, con
una única lista de ingredientes, que es lo que sí está entrecomillado: «*podrá haber una única lista de
ingredientes para el conjunto de productos que compongan el surtido*» (`CHN-13`)»), o **ampliar la
`cita_literal` de `CHN-13`** con el texto del ap. 6.c) y volver a pasar el gate de literalidad.

---

### R3-B5 · BAJA — El libro 2 emite la alerta del art. 75.f) del plástico y **su capítulo llega nueve capítulos después** (13), contra la regla de orden de §4

**Afirmación literal (SPEC:458):** «**Regla de orden, y es la que ordena el índice entero: cada decisión
legal que un xlsx aplica tiene su capítulo ANTES.**»
Y **(SPEC:267):** el libro 2 tiene la entrada «kg/mes de plástico no reciclado…» y la salida «**alerta al
superar los 5 kg/mes del art. 75.f) de la Ley 7/2022**».

**Problema.** El libro 2 es el del **capítulo 04**, y el art. 75.f) se explica en el **capítulo 13**
(ids `CHN-62`, `CHN-62b`, `CHN-62c`, SPEC:476). El lector se encuentra el semáforo rojo del impuesto al
plástico dentro de la calculadora de CAPEX nueve capítulos antes de que nadie le diga qué es, qué queda
fuera (los moldes, `CHN-62c`) y qué no (los semielaborados y los cierres). El cap. 04 ni cita esos ids ni
lleva la prohibición correspondiente.

**FIX.** Cualquiera de las dos, pero escrita: (a) añadir a `SPEC:467` (cap. 04) un epígrafe o punto
«**el impuesto al plástico aparece como alerta en la calculadora y se explica entero en el cap. 13**» con
`CHN-62`/`CHN-62b`/`CHN-62c` en su columna de ids; o (b) mover la entrada «kg/mes de plástico» y su
alerta **al libro 9** (packaging y proveedores), que es el del cap. 13.

---

## Qué hacer con esto, por orden

1. **R3-A2 antes de escribir un solo constructor.** Toca la tabla de cruces, las salidas del libro 2, las
   entradas del libro 2 y el contador del gate (siete → ocho, o la variante de sacar el fondo de maniobra
   del libro 2). Después del reparto ya no se puede: el gate obliga a mentir o a desactivarse, que es lo
   que la ronda 2 documentó dos veces.
2. **R3-A1 cuesta dos frases** y evita que C1 y C3 construyan con la lista vieja.
3. **R3-M1, R3-M3, R3-M4 y R3-B1** son cuatro líneas: presupuesto firmado, mapa de ids, páginas `/usos/`
   y fecha de Resend.
4. **R3-M2 y R3-B2** se deciden juntas con el punto 6 de §10 (si el kit 2.1 entra en esta sesión): la
   guía tiene que citar **la versión del kit que se va a entregar**, no la que hay hoy.

Via: Claude Code
