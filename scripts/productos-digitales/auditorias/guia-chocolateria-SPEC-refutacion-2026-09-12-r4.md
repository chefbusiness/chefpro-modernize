# Re-verificación de la SPEC de «Cómo Montar una Chocolatería» — RONDA 4 (2026-09-12)

Objeto: `scripts/productos-digitales/guia-chocolateria-SPEC.md` (**916 líneas**, §0-§10 + Cierre).
Método: verificación contra los ficheros, nunca contra la memoria. En esta pasada se han abierto y leído
`auditorias/guias-v2-research-sector.json` (**635 entradas**, censadas con Python id a id),
`auditorias/guia-chocolateria-verificacion-legal-2026-09-12.json` (**109 fichas**) y su `-EXCLUIDOS.json` (10),
`guia-pasteleria/gen_calculadora-capex-pasteleria.py` y `guia-pasteleria/gen_plan-financiero-3-anos-pasteleria.py`
(los dos moldes que tocan el cruce nuevo), `src/data/products-catalog.ts`, `astro-site/src/lib/zona-app.ts` y
`astro-site/src/data/productos/guias/`. CPU 42,5-47,1 °C, un fichero cada vez, sin builds ni navegador.

## Veredicto: **CORREGIR ANTES**

**5 hallazgos: 1 ALTA · 1 MEDIA · 3 BAJAS.**
Los **11 hallazgos de la ronda 3 están aplicados**, sin excepción y sin abrir contradicciones nuevas, y la
política del orquestador sobre **D53 está aplicada de forma coherente en los seis sitios** que la ronda pedía.
La única alta es, otra vez, **una costura del mismo cruce**: el octavo cruce (**2 ← 7**) transporta los
**gastos fijos**, pero **«meses de colchón» sigue siendo entrada editable EN LOS DOS LIBROS**, así que el fondo de
maniobra se calcula dos veces y los dos libros pueden volver a publicar **dos inversiones totales distintas** —el
defecto que R3-A2 vino a cerrar— y la fila de CUADRE que §2.3 promete («compara el fondo de maniobra de los dos
libros») **no es construible** con lo único que viaja.

---

### Los 11 hallazgos de la ronda 3: aplicados, uno a uno (con línea)

| Id | Estado | Dónde se comprueba |
|---|---|---|
| **R3-A1** | ✅ aplicado | `SPEC:358` (C1) y `SPEC:360` (C3) dicen «**los OCHO de §2.3**» y declaran qué origina y qué recibe cada constructor; `SPEC:361` (C4) añade el reparto del libro 7. `grep -n "CINCO"` devuelve **cinco ocurrencias y ninguna es de cruces** (134 y 260 = temperaturas · 352 = constructores · 460 = canales · 896 = fila histórica de la ronda 3) |
| **R3-A2** | ✅ aplicado (con residuo, ver **R4-A1**) | `SPEC:328` viaja «**CAPEX SIN el fondo de maniobra**» · `SPEC:330` = octava fila **2 ← 7** · `SPEC:296` = dos líneas separadas en el «Resumen» del libro 2 y la entrada de fijos · `SPEC:261` (D32), `SPEC:319`, `SPEC:332` y `SPEC:699` (§8.2) dicen **OCHO** |
| **R3-M1** | ✅ aplicado | `SPEC:249` (D20) firma **12,05 / 14,15 M** con el «sin el kit, 11,90 / 14,00» dentro; `SPEC:866` y `SPEC:870` anotan las filas de la ronda 2 como superadas |
| **R3-M2** | ✅ aplicado | `SPEC:138-145` retira la nota de la discrepancia y deja «**objetivo 18-20 °C y 50-60 % de HR**, `08!Apertura del Negocio`» y nada más; `SPEC:260` (D31) lo repite; `SPEC:692` adelanta el kit 2.1 a antes de `datos_ejemplo.py` |
| **R3-M3** | ✅ aplicado | `SPEC:273` (D44) lista las **once** familias con `CHS-25a…d`, `CHS-27a/b` y `CHS-28a…d` dentro y marca `CHS-41` como excepción prohibida; `SPEC:580` la baja a la lista negra de §5.2 |
| **R3-M4** | ✅ aplicado | `SPEC:687` (§8.1 filas 23-25) nombra **las CUATRO** páginas por línea, con la de heladería a elegir entre `es.ts:1924` y `:3138` |
| **R3-B1** | ✅ aplicado | `SPEC:40`: «24-oct **CONDICIONADO** —y 29-oct si John aprueba el kit 2.1, que va delante—: ver §7.3» |
| **R3-B2** | ✅ aplicado | `SPEC:690` (fila 30) lleva la humedad dentro del changelog, con el «antes “menos del 60 %” en el `02` y en el `BONUS-01`» |
| **R3-B3** | ✅ aplicado, y mejor de lo pedido | `SPEC:302` publica **los tres requisitos** del art. 13.9 con la `cita_literal` de `PA-29c` **verificada palabra a palabra contra el JSON** hoy, y añade la condición de que el semáforo sólo se active si la CCAA ha ampliado por la letra e) |
| **R3-B4** | ✅ aplicado | `SPEC:408`: las dos denominaciones de surtido **sin comillas de cita**; entrecomillada sólo la `cita_literal` de `CHN-13`, comprobada contra el JSON |
| **R3-B5** | ✅ aplicado | `SPEC:497` (cap. 04): quinto epígrafe del plástico, `3·3·3·2 → 3·3·3·3·2 = 14`, ids `CHN-62`/`62b`/`62c` y las dos prohibiciones |

### La política del orquestador sobre D53: aplicada en los seis sitios

| Punto de la política | Dónde | Verificado |
|---|---|---|
| (a) la guía publica los **ocho alérgenos** y **50-60 %**, sin discusión | `SPEC:214-217` · `SPEC:412` · D31 (`SPEC:260`) | ✓ y los ocho coinciden con `CHN-34b` letra a letra (gluten, huevo, cacahuete, soja, leche, frutos de cáscara, sésamo, sulfitos) |
| (b) el kit 2.1 pasa a **PROPUESTA** con su coste y su efecto en Resend | `SPEC:219-224` · `SPEC:772` (§10 p.6) · `SPEC:738` (0,15 M) | ✓ |
| (c) **no bloquea el cap. 12**, con nota-puente | `SPEC:226-229` · `SPEC:505` (cap. 12) | ✓ la nota-puente está literal en el capítulo |
| (d) fila 30 de §8.1 y los gates de §8.2 marcados «**SI John aprueba D53**» | `SPEC:690` · `SPEC:715`, `SPEC:716`, `SPEC:717` | ✓ los tres gates del kit llevan el marcado y el de alérgenos dice explícitamente que no bloquea el capítulo |
| (e) §7.3 con los **dos escenarios** (24-oct / kit 24-oct + guía 29-oct) y `GET /broadcasts` | `SPEC:659-666` | ✓ (matiz en **R4-B3**) |
| D53 reformulada, no sustituida | `SPEC:821` · recuento `SPEC:914` | ✓ siguen siendo **53** decisiones |

### Lo transversal que sí cuadra (comprobado en esta ronda, no hay que volver a mirarlo)

| Comprobación | Resultado |
|---|---|
| **Una sola lista de cruces, con la misma cifra en los cuatro sitios** | **OCHO** en D32 (`SPEC:261`), §2.3 (`SPEC:319` + **8 filas**, 323-330, y `SPEC:332`), §2.5 (`SPEC:358`, `:360`) y §8.2 (`SPEC:699`). Reparto cuadrado: receptores C1 1 · C3 2 · C4 3 · C5 2 = **8**; orígenes libro 1 → 2, libro 2 → 2, libro 3 → 2, libro 7 → 1, libro 9 → 1 = **8**. Las 8 filas de CUADRE caen en 6 libros distintos (7 lleva tres) |
| **El fondo de maniobra no se SUMA dos veces** | ✓ lo que viaja en 7 ← 2 es «CAPEX sin el fondo», y el libro 7 lo dota una vez: **no hay inflación de la inversión total**. *Lo que sí queda abierto es que se CALCULE dos veces: **R4-A1*** |
| **Presupuesto D20 = §9 = §10, fila a fila** | 0,55+0,50+0,30+2,80+0,60+0,65+0,15 = **5,55** ✓ · 4,50+0,40+0,60+0,75+0,25 = **6,50** ✓ · 5,55+6,50 = **12,05** ✓ · +2,10 = **14,15** ✓ · 14,15−13,44 = **0,71** ✓ · 7×0,30+2×0,35 = **2,80** ✓ · 40×0,1125 = **4,50** ✓ · Pastelería 2,06+0,50+0,38+0,60+2,79+4,90+0,71+1,50 = **13,44** ✓. D20 (`SPEC:249`), §9 (`SPEC:746-751`) y §10 p.5 (`SPEC:771`) publican **12,05 / 14,15** y **11,90 / 14,00 sin el kit**: las tres iguales |
| **§0 ↔ §7 ↔ §8** | 4 páginas `/usos/` en `SPEC:40`, `:627` y `:687` ✓ · 4 banners en 8 posts (`:40` ↔ §7.2, `:651` «ganancia neta 4») ✓ · fecha de Resend condicionada en `:40` ↔ §7.3 ✓ · **49 en catálogo** en `:44`, `:672`, `:681`, `:687`, `:743` ✓ · **14 claves de `PRODUCT_FILES`** (`:683`) = 5 documentos + los **9 nombres de fichero de D49** (`:295-303`), 1:1 con `capacidad-clima`…`checklist-equipamiento`, y las mismas 14 en `:688` («14 entregables») y `:721` («14 descargas binarias») ✓ |
| **Baselines contra el repo, medidos hoy** | `products-catalog.ts` = **48** entradas ✓ · `zona-app.ts` `grep -c productId:` = **49** ✓ · `astro-site/src/data/productos/guias/` = 11 ficheros = **10 fichas + `types.ts`** ✓ |
| **Ids** | **Cero ids inexistentes.** 165 ids distintos citados; los 6 `CHN-*` fuera del JSON común (`49d, 50, 70, 79, 80, 98`) están **los seis en `-EXCLUIDOS.json`** y la SPEC los cita **como excluidos** (`SPEC:271`, `:272`, `:563`, `:569`); los 11 bare de D44 sólo aparecen en `SPEC:273` **y en la fila histórica `SPEC:900`** (ver **R4-B1**); `CHS-41` bare sólo en contextos de prohibición (`:273`, `:580`, `:900`, `:914`) |
| **Literales legales contra la verificación del 12-sep** | `CHN-22` (art. 38.3, «operadores… establecidos como tales a 31 de diciembre de 2024») ✓ y la exclusión del punto 15 sigue **parafraseada**, en `nota`, no entrecomillada ✓ · `CHN-23` (art. 2.15 ter) ✓ · `CHN-10` (1.10 y 1.13 **sobre el peso total**) ✓ en D37 y en `SPEC:404-405` · `CHN-34b` (los ocho) ✓ · `CHN-65c` (código **28001025011981**, «CONFITERIAS PASTELERIAS Y REPOSTERIA (COMERCIO E INDUSTRIA)», 01/01/2024-31/12/2026, revisión 28/02/2026) ✓ en `SPEC:394` · `CHN-30` y `CHN-87` (D47) ✓ · `CHN-24` (art. 5.3.a), «únicamente en el caso de que su proveedor sea un operador») ✓ en D48 · `CHN-13` ✓ · `PA-29c` **palabra por palabra** ✓. **Ningún literal contradice el JSON legal** |
| **Aritmética del índice** | Las **21 sumas** de `puntos_por_epigrafe` cuadran de nuevo tras tocar el cap. 04 (14 con 5 epígrafes), todas dentro de 4-6 epígrafes y 2-5 puntos ✓ · palabras 16×1.750 + 4×2.100 + 1.500 = **37.900** (+2,43 % sobre 37.000) ✓ · bloques 6×2 + 14 + 1 + 12 + 1 = **40** ✓ · familias de la carta 10+6+3+5+4 = **28** ✓ · zonas 26+6+8+5+22+8 = **75 m²** ✓ |

---

## A — ALTAS

### R4-A1 · ALTA — El octavo cruce trae los **gastos fijos**, pero «**meses de colchón**» sigue siendo entrada editable **en los dos libros**: el fondo de maniobra se calcula **dos veces** y los dos libros pueden volver a publicar **dos inversiones totales distintas**. Además, la fila de CUADRE que §2.3 promete **no es construible** con lo único que viaja

**Afirmación literal (SPEC:330, §2.3, octava fila):** «**Gastos fijos mensuales del año de crucero** | **2** ← 7 |
Celda verde «trae aquí los fijos mensuales de `plan-financiero-3-anos-chocolateria.xlsx!PyG 3 Años!<Celda>`»…
+ **fila de CUADRE** que **compara el fondo de maniobra de los dos libros**».
**Y (SPEC:296, entradas del libro 2):** «…precio de traspaso; renta; horizonte en años; **meses de colchón**;
**gastos fijos mensuales del año de crucero traídos del libro 7**…».
**Y (SPEC:301, libro 7):** «**el fondo de maniobra lo dota AQUÍ, con los meses de colchón de ESTE LIBRO y sus
propios fijos**, y por eso el libro 2 los recibe de vuelta por celda verde en lugar de calcularlos».

**Problema.** El fondo de maniobra es `meses de colchón × gastos fijos mensuales`. La ronda 3 cerró la mitad del
acoplamiento —los **fijos** ya viajan— pero dejó **el otro factor duplicado**: «meses de colchón» es entrada
editable del libro 2 (`SPEC:296`) **y** del libro 7 (`SPEC:301`). Consecuencias, las tres verificadas contra el
molde:

1. **El fondo sigue calculándose en dos sitios.** En el molde los dos libros tienen su propio parámetro de
   colchón sembrado del mismo dato —`gen_calculadora-capex-pasteleria.py:163-167` («Meses de colchón de
   tesorería», `D.P('meses_colchon_fondo_maniobra')`) y `gen_plan-financiero-3-anos-pasteleria.py:651-652`
   (`ent('colchon', 'Fondo de maniobra (meses de costes fijos)', D.P('meses_colchon_fondo_maniobra'), C.ENT)`,
   una **entrada**, con el cálculo en `:778`)—. Si el lector cambia uno y no el otro, el libro 2 publica
   «inversión total = CAPEX sin fondo + fondo₂» (`SPEC:296`) y el libro 7 publica «Inversión Inicial = CAPEX sin
   fondo + fondo₇» (`SPEC:301`): **dos inversiones totales distintas con el mismo nombre**, que es literalmente la
   segunda mitad del defecto que R3-A2 describía y que §2.3 dice haber cerrado (`SPEC:332`: «el fondo de maniobra
   calculado dos veces publicó dos inversiones totales distintas en el mismo pack»).
2. **La fila de CUADRE prometida no se puede construir.** Para «comparar el fondo de maniobra de los dos libros»
   el libro 2 necesitaría **el fondo del 7** (o sus meses de colchón), y **lo único que trae es los fijos**. Con
   los fijos, lo máximo que puede hacer el cuadre es lo que hacen los otros siete: avisar si lo tecleado se aleja
   del origen. Un constructor que lea `SPEC:330` tiene dos salidas y las dos son malas: inventarse una celda que
   nadie declaró, o escribir un cuadre más débil que el que el gate cuenta — el patrón «gate que no falla pero
   deja pasar el error» que la casa ya tiene documentado.
3. **El molde avisaba de esto con todas las letras y la nota sigue viva.** `gen_calculadora-capex-pasteleria.py:183-191`:
   «*Es el mismo gasto fijo mensual que calcula, mes a mes, el libro 5 …, así que los dos libros publican el mismo
   fondo de maniobra y la misma inversión total. **Si cambias este valor, cámbialo también allí**.*» La SPEC cita
   esa nota como «la definición del defecto» (`SPEC:330`) y **la reproduce a medias**: quita el acoplamiento manual
   de los fijos y deja el de los meses.

**Evidencia.** `SPEC:296`, `SPEC:301`, `SPEC:330`, `SPEC:332` · `gen_calculadora-capex-pasteleria.py:163-167,
183-191, 1083-1086` · `gen_plan-financiero-3-anos-pasteleria.py:651-652, 778, 805, 814-815, 825`.

**FIX (una de las dos, pero escrita).**
**(a) La preferible — que viaje la magnitud, no sus factores.** El octavo cruce pasa a ser
«**Fondo de maniobra**  | **2** ← 7 | Celda verde «trae aquí el fondo de maniobra de
`plan-financiero-3-anos-chocolateria.xlsx!Inversión Inicial!<Celda>`», con valor por defecto declarado, + **fila de
CUADRE** que lo compara con la línea «fondo de maniobra» del bloque de CAPEX del propio libro 2». Se **retira
«meses de colchón» de las entradas del libro 2** (`SPEC:296`) y la nota dice «*los meses de colchón se deciden en
el libro 7, que es donde están los fijos*». Así el fondo se calcula **una vez**, la inversión total sale idéntica
por construcción y el cuadre es construible con lo que viaja.
**(b) La alternativa —** si se quiere que el libro 2 siga dotando: la celda verde trae **los fijos Y los meses de
colchón** (dos celdas, una fila de CUADRE), y se dice explícitamente que «meses de colchón» del libro 2 es un
**espejo**, no una decisión independiente. Sube el contador a **NUEVE** celdas verdes y hay que tocar D32
(`SPEC:261`), §2.3 (`SPEC:319`, `:332`), §2.5 (`SPEC:358`, `:361`) y §8.2 (`SPEC:699`).
**En los dos casos**, añadir a las **salidas del libro 7** (`SPEC:301`, que hoy no la nombra) la celda citable
«**gastos fijos mensuales del año de crucero**» y, en (a), «**fondo de maniobra**», que es lo que C4 tiene que
publicar en `build/mapa-7.json` (`SPEC:361`).

---

## B — MEDIAS

### R4-M1 · MEDIA — Los ocho bloques de CAPEX de §3.3 **no son los ocho del molde** y **funden «fianza, licencias y fondo de maniobra» en UNO**: con el fondo sin fila propia, las dos líneas nuevas del «Resumen» que exige §2.2 **no tienen de dónde salir**

**Afirmación literal (SPEC:438):** «**CAPEX por bloque** (**los ocho bloques del molde de Pastelería**…): obra y
adecuación · climatización y deshumidificación · equipo de templado y moldeado · frío (cámara de chocolate +
vitrina) · mobiliario y tienda · packaging y moldes · TPV, informática y rótulo · **fianza, licencias y fondo de
maniobra**».
**Frente a (SPEC:296, salidas del libro 2):** «**dos líneas separadas en «Resumen»: “CAPEX sin el fondo de
maniobra” y “Del cual, fondo de maniobra (es caja, no inversión)”** —la primera es la que viaja al libro 7—».

**Problema.** Dos cosas, y la segunda es la que rompe el cruce nuevo:

1. **No son los del molde.** Los ocho de `gen_calculadora-capex-pasteleria.py:98-101` son *Obra civil e
   instalaciones · Equipamiento de obrador · Tienda y vitrina · Licencias y proyecto técnico · **Fianza y
   garantías** · Packaging inicial · **Marketing de apertura** · **Fondo de maniobra***. Los de chocolate son otros
   ocho: añaden climatización y TPV/rótulo, **pierden «Marketing de apertura»** y **funden tres bloques del molde
   en uno**. Decir «los ocho del molde» invita a calcarlos y a que el conteo cuadre por casualidad.
2. **Sin bloque propio de «Fondo de maniobra» las dos líneas del Resumen no existen.** El molde publica
   «**Del cual, fondo de maniobra (es caja, no inversión)**» con
   `"='%s'!K%d" % (H_CAP, B_INI + BLOQUES.index('Fondo de maniobra'))`
   (`gen_calculadora-capex-pasteleria.py:1083-1086`): **apunta a la fila del bloque**. Con el bloque fusionado esa
   referencia no tiene destino, y «CAPEX sin el fondo de maniobra» —la cifra que **viaja al libro 7** por el cruce
   7 ← 2— tampoco es derivable (habría que restar una parte de un bloque mixto). Y hay un tercer daño silencioso:
   `BLOQUES_COMPARABLES` (`:106-108`) **excluye a propósito fianza, packaging y fondo** de la comparación con el
   escenario publicado, porque «la fianza es un depósito, el packaging son existencias y el fondo de maniobra es
   caja»; el bloque fusionado es **medio comparable (licencias) y medio no**, así que esa exclusión tampoco se
   puede escribir.

**Evidencia.** `SPEC:438`, `SPEC:296`, `SPEC:328` · `gen_calculadora-capex-pasteleria.py:98-101, 106-108,
1083-1086`.

**FIX.** SPEC:438 → «**CAPEX por bloque** (**nueve bloques: los ocho del molde de Pastelería con climatización y
TPV/rótulo en lugar de marketing de apertura, y el fondo de maniobra conservando SU FILA PROPIA**, que es de donde
el «Resumen» saca «Del cual, fondo de maniobra» —`gen_calculadora-capex-pasteleria.py:1083-1086`— y de donde se
deriva el «CAPEX sin el fondo» que viaja al libro 7): obra y adecuación · climatización y deshumidificación ·
equipo de templado y moldeado · frío · mobiliario y tienda · packaging y moldes · TPV, informática y rótulo ·
**fianza y licencias** · **fondo de maniobra**. ⚠️ **Fianza, packaging y fondo quedan FUERA de
`BLOQUES_COMPARABLES`** (`:106-108`): un depósito, unas existencias y una caja no se comparan contra un
presupuesto de obra y equipamiento». Y ajustar la mención «los ocho bloques» de `SPEC:296` y del cruce
`SPEC:328` («las ocho partidas» → «las nueve partidas»).

---

## C — BAJAS

### R4-B1 · BAJA — Tres ids **bare** de D44 (`CHS-25`, `CHS-27`, `CHS-28`) viven **fuera de la fila D44**, en la tabla histórica de la ronda 3

**Afirmación literal (SPEC:900):** «…**faltaban `CHS-25`, `CHS-27` y `CHS-28`** —y `CHS-28a` es el precio de la
cobertura— y **sobraba `CHS-41`, que sí existe bare**…».

**Problema.** Censado hoy contra el JSON de 635: los once bare de D44 aparecen **sólo en `SPEC:273`** salvo estos
tres, que reaparecen entrecomillados en el Cierre. No es un error de contenido —la frase describe el hallazgo— pero
el guion se escribe leyendo esta SPEC, y la regla de la casa es que un id citado en la SPEC es un id citable. Un
`grep -o 'CH[NS]-[0-9]*[a-z]*'` sobre la SPEC para sembrar la clave `sector` los arrastra, y `verificar_guion.py`
**sí** los cazaría (no existen), pero después de haber gastado la redacción.

**Evidencia.** Censo propio: `CHS-25` → `SPEC:273, 900` · `CHS-27` → `SPEC:273, 900` · `CHS-28` → `SPEC:273, 900`;
las otras ocho familias, sólo en `:273`.

**FIX.** SPEC:900 → escribirlos **sin backticks y con el sufijo**: «faltaban las familias **CHS-25a…d**,
**CHS-27a/b** y **CHS-28a…d** —y `CHS-28a` es el precio de la cobertura—». Mismo criterio en `SPEC:914` para
`CHS-41`, que ahí va como nombre de excepción, no como cita.

---

### R4-B2 · BAJA — §2.5 declara los cruces de **C1, C3 y C4** y **calla los de C2 y C5**, que también originan y reciben

**Afirmación literal (SPEC:359, C2):** «Los dos son **nuevos** y los dos giran sobre el mismo eje… El 3 fija **la
celda única del precio de cobertura** de la que bebe todo el paquete».
**Y (SPEC:362, C5):** «Los dos son **molde B sembrado**… El árbol de proveedores del 9 y la hoja EUDR del 8
**tienen que decir lo mismo**».

**Problema.** El fix de R3-A1 dio a C1, C3 y C4 la cuenta exacta de qué originan y qué reciben, y dejó a los otros
dos sin ella. Contadas sobre la tabla de §2.3: **C2 ORIGINA dos** (4 ← 3 y 7 ← 3) y por tanto **tiene que publicar
la celda del precio de cobertura en base imponible en `build/mapa-3.json`**, o C3 y C4 no pueden montar sus filas
de CUADRE; **C5 RECIBE dos** (9 ← 2, que viene de C1, y 8 ← 9, que es interno) **y ORIGINA uno** (9 → 8). Es la
misma asimetría que R3-A1 cazó: el constructor lee **su fila**, y en dos de las cinco no está escrito qué le toca
publicar.

**Evidencia.** `SPEC:325` (9 ← 2), `SPEC:326` (4 ← 3), `SPEC:327` (7 ← 3), `SPEC:329` (8 ← 9) frente a
`SPEC:359` y `SPEC:362`.

**FIX.** SPEC:359 → añadir «⚠️ **C2 es ORIGEN de dos cruces** (4 ← 3 y 7 ← 3) **y no recibe ninguno**: publica en
`build/mapa-3.json` la celda del **precio de cobertura en BASE IMPONIBLE** —nunca la de base con IVA (A-2)— que
citan el 4 y el 7». SPEC:362 → «⚠️ **C5 RECIBE dos** (9 ← 2, del libro 2 de C1, y 8 ← 9, interno a este
constructor) **y ORIGINA uno** (9 → 8): monta las dos filas de CUADRE y publica el **plazo de entrega crítico** en
`build/mapa-9.json`».

---

### R4-B3 · BAJA — D8 y D28 siguen publicando **un solo escenario** de fecha de Resend; el segundo (29-oct) vive sólo en §7.3

**Afirmación literal (SPEC:70, D8):** «Resend: borrador para el **24-oct-2026**, 08:00 UTC» · estado «**Matizada
por D28**: pasa de “libre” a “**condicionado**”…».
**Y (SPEC:257, D28):** «**24-oct SI Pastelería y el kit se programan a partir del 14-sep y del 19-sep; si no, el
hueco real es el 14-oct**».

**Problema.** La política de D53 abrió un **tercer** escenario —kit de Chocolatería 24-oct y guía **29-oct**— que
§0 (`SPEC:40`) y §7.3 (`SPEC:659-664`) sí recogen, pero **las dos decisiones firmadas, no**. §1 declara que las
decisiones «no se reabren al construir», así que quien vaya a D8/D28 a buscar la fecha aprobada encuentra dos
ramas de tres. Es la misma clase de R3-M1 (la decisión firmada desalineada de la sección que la desarrolla), en
versión menor.

**Evidencia.** `SPEC:70`, `SPEC:257` frente a `SPEC:40`, `SPEC:661-662`.

**FIX.** SPEC:70 y SPEC:257 → cerrar las dos con «**y una tercera rama desde D53: si John aprueba el kit 2.1, el
kit ocupa el 24-oct y la guía va al 29-oct (§7.3)**. Los tres huecos se recalculan juntos con `GET /broadcasts`».

---

## Qué hacer con esto, por orden

1. **R4-A1 antes de escribir C1 y C4.** Toca la octava fila de §2.3, las entradas del libro 2, las salidas del
   libro 7 y —si se elige la variante (b)— el contador de OCHO a NUEVE en D32, §2.3, §2.5 y §8.2. Después del
   reparto ya no se puede: el gate cuenta filas de CUADRE y el constructor tendría que inventarse una celda.
2. **R4-M1 en el mismo commit**, porque es de lo que depende que la línea «CAPEX sin el fondo» exista para
   viajar: es partir un bloque en dos y una frase de `BLOQUES_COMPARABLES`.
3. **R4-B1, R4-B2 y R4-B3** son cinco líneas: tres ids del Cierre, dos filas de §2.5 y dos decisiones de §1.

**Lo que NO hay que volver a mirar:** los 11 hallazgos de la ronda 3 (aplicados, tabla de arriba), la política de
D53 (aplicada en los seis sitios), el presupuesto (sumado fila a fila en las tres publicaciones), los ids (cero
inexistentes; los excluidos, citados como tales), los literales legales de la muestra (D5/EUDR, D37/`CHN-10`, D47,
D48, `CHN-65c`, `CHN-34b`, `CHN-13`, `PA-29c`), la aritmética del índice (21 sumas, 40 bloques, 37.900 palabras) y
los baselines del repo (48 productos, 49 `productId:`, 10 fichas de guía).

Via: Claude Code
