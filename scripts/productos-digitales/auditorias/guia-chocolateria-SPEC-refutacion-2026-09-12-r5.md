# Re-verificación de la SPEC de «Cómo Montar una Chocolatería» — RONDA 5 (2026-09-12)

Objeto: `scripts/productos-digitales/guia-chocolateria-SPEC.md` (**934 líneas**, §0-§10 + Cierre).
Método: verificación contra los ficheros, nunca contra la memoria. En esta pasada se han abierto y censado con
Python `auditorias/guias-v2-research-sector.json` (**635 entradas**, id a id),
`auditorias/guia-chocolateria-verificacion-legal-2026-09-12.json` (**109 fichas**, campo a campo) y su
`-EXCLUIDOS.json` (**10 ids**), más los baselines del repo (`src/data/products-catalog.ts`,
`astro-site/src/lib/zona-app.ts`, `astro-site/src/data/productos/guias/`,
`astro-site/public/dl/kit-tareas-chocolateria/`). CPU 46,7-49,2 °C, un fichero cada vez, sin builds ni navegador.

## Veredicto: **LISTO**

**3 hallazgos: 0 ALTAS · 0 MEDIAS · 3 BAJAS.**
Los **5 hallazgos de la ronda 4 están aplicados**, sin excepción y **sin abrir contradicciones nuevas**; la
política del orquestador sobre **D53 sigue aplicada de forma coherente en sus seis sitios**; y **la costura del
cruce del fondo de maniobra —que abrió la ronda 2, estrechó la 3 y cerró la 4— queda cerrada por construcción**:
el fondo se calcula **una sola vez**, en el libro 7, y viaja **ya calculado** al libro 2. Las tres bajas son
cinco líneas de redacción; **ninguna bloquea la construcción**.

---

### Los 5 hallazgos de la ronda 4: aplicados, uno a uno (con línea)

| Id | Estado | Dónde se comprueba |
|---|---|---|
| **R4-A1** (ALTA) | ✅ aplicado, **variante (a)** | `SPEC:330` = octava fila «**Fondo de maniobra** \| **2 ← 7**» contra `plan-financiero-3-anos-chocolateria.xlsx!Inversión Inicial`, con el CUADRE contra la línea «fondo de maniobra» del bloque de CAPEX del propio libro 2 · `SPEC:296` retira «meses de colchón» de las entradas del libro 2 («**NO es entrada de este libro**, se decide en el 7») · `SPEC:301` añade a las salidas del libro 7 **las dos celdas citables** de `build/mapa-7.json` («gastos fijos mensuales del año de crucero» y «fondo de maniobra») · `SPEC:261` (D32) y `SPEC:332` reescritos · `SPEC:358` (C1) y `SPEC:361` (C4) alineados. **El contador NO sube: siguen siendo OCHO** (`SPEC:261`, `:319`, `:332`, `:358`, `:360`, `:699`, `:932`) |
| **R4-M1** (MEDIA) | ✅ aplicado | `SPEC:438` publica **NUEVE bloques** con «fondo de maniobra» **en fila propia**, cita los ocho del molde **como son** (`gen_calculadora-capex-pasteleria.py:98-101`, con «Marketing de apertura» dentro), explica que de esa fila sale «Del cual, fondo de maniobra» (`:1083-1086`) y de dónde se deriva el «CAPEX sin el fondo» que viaja al 7, y cierra `BLOQUES_COMPARABLES` (`:106-108`) con **SEIS comparables** y los tres excluidos **enteros**. «Ocho partidas» → «**nueve partidas**» en `SPEC:301` y `SPEC:328`; «nueve bloques» también en `:296` y `:330`. `grep` de recuentos: **cero ocurrencias de «ocho bloques/partidas» fuera de la fila histórica `:922`** |
| **R4-B1** (BAJA) | ✅ aplicado | `SPEC:900` escribe **CHS-25a…d**, **CHS-27a/b** y **CHS-28a…d** con sufijo y sin backticks; `SPEC:932` lleva **CHS-41** sin backticks como nombre de excepción. Censo propio: los **once ids bare de D44 aparecen SÓLO en `SPEC:273`** |
| **R4-B2** (BAJA) | ✅ aplicado | `SPEC:359` (C2) = «**ORIGEN de dos** (4 ← 3 y 7 ← 3) **y no recibe ninguno**», con el precio de cobertura **en base imponible** en `build/mapa-3.json` · `SPEC:362` (C5) = «**RECIBE dos** (9 ← 2 y 8 ← 9) **y ORIGINA uno** (9 → 8)», con el plazo crítico en `build/mapa-9.json` |
| **R4-B3** (BAJA) | ✅ aplicado | `SPEC:70` (D8) y `SPEC:257` (D28) cierran las dos con «**una tercera rama desde D53:** si John aprueba el kit 2.1, el kit ocupa el 24-oct y la guía va al 29-oct (§7.3). **Los tres huecos se recalculan juntos con `GET /broadcasts`**» |

### La política del orquestador sobre D53: sigue aplicada en los seis sitios

| Punto | Dónde | Verificado |
|---|---|---|
| (a) la guía publica los **ocho alérgenos** y **50-60 %**, sin discusión | `SPEC:214-217` · `:412` · D31 (`:260`) | ✓ los ocho coinciden letra a letra con el `dato` de `CHN-34b` (gluten, huevo, cacahuete, soja, leche, frutos de cáscara, sésamo, sulfitos), leído hoy del JSON legal |
| (b) el kit 2.1 pasa a **PROPUESTA**, con coste y efecto en Resend | `SPEC:219-224` · `:738` (0,15 M) · `:772` (§10 p.6) | ✓ |
| (c) **no bloquea el cap. 12**, con nota-puente | `SPEC:226-229` · `:505` | ✓ la nota-puente está literal en el capítulo |
| (d) fila 30 de §8.1 y los gates del kit marcados «**SI John aprueba D53**» | `SPEC:690` · `:715`, `:716`, `:717` | ✓ y `:715` dice explícitamente que el gate «no bloquea el cap. 12» |
| (e) §7.3 con los **dos escenarios** y `GET /broadcasts` | `SPEC:659-666`, con eco en `:40`, `:70`, `:257` y `:772` | ✓ (matiz de forma en **R5-B1**) |
| D53 reformulada, no sustituida | `SPEC:821` · recuento `:932` | ✓ siguen siendo **53** decisiones (18 + 28 + 7) |

### Lo transversal, comprobado en esta ronda

| Comprobación | Resultado |
|---|---|
| **Una sola lista de cruces, con la misma cifra en los cuatro sitios** | **OCHO** en D32 (`:261`), §2.3 (`:319` + 8 filas `:323-330` + `:332`), §2.5 (`:358`, `:360`) y §8.2 (`:699`). `grep -n "CINCO\|SIETE"`: **ninguna ocurrencia referida a cruces** fuera de las filas históricas `:866` y `:896`. Reparto cuadrado por las dos caras: **orígenes** libro 1 → 2 · libro 2 → 2 · libro 3 → 2 · libro 7 → 1 · libro 9 → 1 = **8**; **receptores** C1 1 · C2 0 · C3 2 · C4 3 · C5 2 = **8** |
| **El fondo de maniobra se cuenta UNA vez y se calcula UNA vez** | ✓ Cerrado por construcción: los **dos factores** («meses de colchón» y «fijos mensuales») viven sólo en el libro 7 (`:301`, `:330`); lo que viaja en **7 ← 2** es «CAPEX **sin** el fondo» y lo que vuelve en **2 ← 7** es **la magnitud ya calculada** (`:328`, `:330`). El libro 2 publica «inversión total = CAPEX sin fondo + fondo importado» (`:296`) y el libro 7 «Inversión Inicial = CAPEX sin fondo + fondo dotado» (`:301`): **la misma cifra por construcción**, no por coincidencia. `grep` de «meses de colchón»: **16 ocurrencias, todas coherentes**, ninguna lo pone como entrada del libro 2 |
| **La fila de CUADRE del 2 ← 7 ya es construible** | ✓ Con la magnitud viajando, el libro 2 tiene las dos cifras que comparar (celda verde importada ↔ fila del bloque «fondo de maniobra» de su CAPEX, `:296` + `:330`). Era lo que R4-A1 declaraba imposible con sólo los fijos |
| **Presupuesto D20 = §9 = §10, sumado fila a fila** | 0,55+0,50+0,30+2,80+0,60+0,65+0,15 = **5,55** ✓ · 4,50+0,40+0,60+0,75+0,25 = **6,50** ✓ · 5,55+6,50 = **12,05** ✓ · +2,10 = **14,15** ✓ · 7×0,30+2×0,35 = **2,80** ✓ · 40×0,1125 = **4,50** ✓ · Pastelería 2,06+0,50+0,38+0,60+2,79+4,90+0,71+1,50 = **13,44** ✓ · 14,15−13,44 = **0,71** ✓. **D20 (`:249`), §9 (`:746-751`) y §10 p.5 (`:771`) publican las mismas cuatro cifras**: 12,05 / 14,15 con el kit, 11,90 / 14,00 sin él |
| **§0 ↔ §7 ↔ §8** | **4 páginas `/usos/`** en `:40`, `:627` y `:687` ✓ · **4 banners en 8 posts** (`:40` ↔ tabla de §7.2, que suma 8 posts, y `:651` «ganancia neta 4») ✓ · **fecha de Resend condicionada con sus tres ramas** en `:40`, `:70`, `:257`, `:659-666`, `:772` ✓ · **49 en catálogo** en `:44`, `:672`, `:681`, `:687`, `:743` y el badge de D6 ✓ · **14 claves de `PRODUCT_FILES`** (`:683`) = 5 documentos + los **9 nombres de fichero de D49** (`:295-303`), 1:1 con `capacidad-clima`…`checklist-equipamiento`; y las mismas 14 en `:688` («14 entregables»), `:721` («14 descargas binarias») y en el `SECTIONS[]` del dashboard (`:680`, «Guía 2 · Herramientas 9 · Bonus 3») ✓ |
| **Baselines contra el repo, medidos hoy** | `products-catalog.ts` = **48** entradas ✓ · `zona-app.ts` `grep -c productId:` = **49** ✓ · `productos/guias/` = **11** ficheros ✓ · `dl/kit-tareas-chocolateria/` = **11** xlsx ✓ |
| **Ids** | **164 ids distintos citados; cero inexistentes no declarados.** Los 6 `CHN-*` fuera del JSON común (`49d, 50, 70, 79, 80, 98`) están **los seis en `-EXCLUIDOS.json`** y la SPEC los cita **como excluidos** (`:271`, `:272`, `:563`, `:569`). **Los once bare de D44 aparecen sólo en `:273`** (R4-B1 cerrado). `CHS-41` bare —la excepción que sí existe— sólo en contextos de prohibición (`:273`, `:580`, `:900`, `:923`, `:932`) |
| **Literales legales contra la verificación del 12-sep** | Leídos del JSON campo a campo: `CHN-10` (1.6-1.9/1.11/1.12 descontando · **1.10 y 1.13 sobre el peso total**) ✓ en D37 (`:266`) y `:404-405` · `CHN-34b` (los ocho, `cifra: 8`) ✓ en `:215`, `:412` · `CHN-22` (art. 38.3 literal, «establecidos como tales a 31 de diciembre de 2024») ✓ en D5 · `CHN-23` (art. 2.15 ter) ✓ · `CHN-24` («**únicamente en el caso de que su proveedor sea un operador**») ✓ en D48 · `CHN-30` + `CHN-87` ✓ en D47 · `CHN-13` (la única frase entrecomillada es la del BOE; las dos denominaciones de surtido viven en `dato`) ✓ · `CHN-65c` (código **28001025011981**, «CONFITERIAS PASTELERIAS Y REPOSTERIA (COMERCIO E INDUSTRIA)», 01/01/2024-31/12/2026, revisión 28/02/2026) ✓ en `:394` · `CHN-08`, `CHN-47b`, `CHN-49`, `CHN-49b` ✓. **Ningún literal contradice el JSON legal** (matiz de atribución de campo en **R5-B3**) |
| **Aritmética del índice** | Las **21 sumas** de `puntos_por_epigrafe` cuadran (script propio), todas con **4-6 epígrafes** y **2-5 puntos** ✓ · palabras 16×1.750 + 4×2.100 + 1.500 = **37.900** (+2,43 % sobre 37.000, dentro del ±3 %) ✓ · bloques 6×2 + 14 + 1 + 12 + 1 = **40** ✓ · balance 9 + 6 + 5 = **20** capítulos ✓ · familias de la carta 10+6+3+5+4 = **28** ✓ · zonas 26+6+8+5+22+8 = **75 m²** ✓ · §5.1 = **29** prohibiciones + **4** de la SPEC ✓ · §5.2 = **N-1…N-20** ✓ |

---

## C — BAJAS (ninguna bloquea; las tres son redacción)

### R5-B1 · BAJA — D53 anuncia «**cinco puntos**» y publica **cuatro**: falta como punto propio el efecto en la cola de Resend, que es justo la rama que John tiene que decidir

**Afirmación literal (`SPEC:212`):** «…y la regla de la casa es “**un dictado de John = sólo ese cambio**”. **Queda
así, en cinco puntos:**» — y a continuación sólo hay **(a)** (`:214`), **(b)** (`:219`), **(c)** (`:226`) y
**(d)** (`:231`), más dos ⚠️ de acotación (`:235`, `:237`).

**Problema.** La política del orquestador enumera cinco puntos y el quinto es el del calendario: «*§7.3: el hueco
de la guía es el 24-oct salvo que John apruebe el kit 2.1 (entonces kit 24-oct y guía 29-oct), siempre confirmado
con `GET /broadcasts`*». Ese contenido **existe y es correcto** —está en §7.3 (`:659-666`), en §10 punto 6
(`:772`), en D8 (`:70`), en D28 (`:257`) y en §0 (`:40`)—, pero **no como punto de D53**, que es la decisión que
§1 declara «no se reabre al construir». Quien vaya a D53 a ver qué se le pregunta a John cuenta cuatro y busca un
quinto que no está. No hay pérdida de información; hay un recuento que no casa con su propia lista.

**Evidencia.** `SPEC:212` frente a `SPEC:214`, `:219`, `:226`, `:231`; el contenido ausente, en `SPEC:659-666` y
`SPEC:772`.

**FIX.** Añadir tras `SPEC:233` el punto **(e)**: «**(e) El hueco de Resend depende de esta respuesta, y son dos
escenarios, no uno:** si **no** se aprueba, la guía ocupa el **24-oct**; si **sí**, el kit lleva su propio
broadcast y **va delante** (una actualización sale antes que un lanzamiento) → **kit 24-oct y guía 29-oct**. En
los dos casos el hueco se confirma con **`GET /broadcasts`** antes de escribirlo (§7.3, D8, D28).» Alternativa de
una línea: cambiar «en cinco puntos» por «en cuatro puntos» — **pero es peor**, porque deja la consecuencia de
calendario fuera de la decisión que se firma.

---

### R5-B2 · BAJA — Retirado «meses de colchón» del libro 2, el supuesto de **6 meses** de §3.4 se queda **sin libro asignado** en la única lista que lee el constructor

**Afirmación literal (`SPEC:462`, §3.4):** «**Financiación, tesorería y calendario — todo supuesto declarado**…
estructura **40 % recursos propios / 60 % préstamo a 7 años**, **colchón de tesorería de 6 meses de fijos**, y
**apertura el 1 de junio**… **Los tres van en celda verde** con el supuesto escrito al lado.»
**Frente a las entradas del libro 7 (`SPEC:301`)**, donde «meses de colchón» **no figura en la enumeración**: sólo
aparece **dentro del paréntesis** del cruce 7 ← 2 («*el fondo de maniobra lo dota AQUÍ, con los meses de colchón
de este libro y sus propios fijos*»).

**Problema.** Antes de R4-A1 el parámetro estaba enumerado como entrada del libro 2 (`SPEC:296`). El fix lo
retiró de allí —correctamente— pero **no lo enumeró en el libro 7**, que es donde ahora vive en exclusiva. Queda
declarado sólo en prosa incidental, y §3.4 —que es donde el constructor busca el **valor por defecto**— no dice a
qué libro pertenece. Dos riesgos pequeños y concretos: (1) la **regla 2 de §2.3** exige que *ninguna celda verde
quede vacía* y se verifica **sobre los `mapa-*.json`**, así que un parámetro que no está en la lista de entradas
de ningún libro puede no acabar en ningún mapa; (2) un constructor que lea §3.4 sin el paréntesis de `:301`
podría devolverlo al libro 2, que es exactamente lo que R4-A1 prohíbe.

**Evidencia.** `SPEC:462` · `SPEC:301` (entradas del libro 7, sin el parámetro enumerado) · `SPEC:296` (retirado
del libro 2) · `SPEC:316` (regla de celdas verdes) · molde: `gen_plan-financiero-3-anos-pasteleria.py:651-652`,
donde `colchon` **es una entrada** («Fondo de maniobra (meses de costes fijos)»).

**FIX.** Dos líneas. (1) En las **entradas del libro 7** (`SPEC:301`), añadir a la enumeración «**meses de colchón
de tesorería** (por defecto **6**, supuesto declarado, §3.4) — **es el único sitio del paquete donde se decide**».
(2) En `SPEC:462`, cerrar la frase con «…**y los tres viven en el libro 7** (`plan-financiero-3-anos-chocolateria.xlsx`):
el colchón, en su hoja «0. Supuestos», porque es uno de los dos factores del fondo de maniobra y **el libro 2 ya
no lo tiene** (R4-A1)».

---

### R5-B3 · BAJA — D5 atribuye la exclusión «excluidos los operadores posteriores» a la **`nota` de `CHN-22`**, y ese texto vive en el **`dato` de `CHN-22`** y en la **`nota` de `CHN-23`**

**Afirmación literal (`SPEC:67`, D5):** «⚠️ **La exclusión “excluidos los operadores posteriores” del punto 15
consta en la `nota` de `CHN-22`, NO como cita del gate de literalidad (81/81): se PARAFRASEA, no se
entrecomilla**, hasta que se abra el consolidado y entre como cita propia.»

**Problema.** Leídas hoy las dos fichas del JSON legal: la `nota` de **`CHN-22`** habla del marcado ▼M2, de la
lectura literal y de la inferencia declarada, **pero no contiene esa frase**; el texto «*El punto 15 define
«operador» «excluidos los operadores posteriores»*» está en la **`nota` de `CHN-23`**, y el `dato` de `CHN-22`
lo dice con otras palabras («*el art. 2.15 excluye de la palabra “operador” a los operadores posteriores*»).
**La regla operativa de D5 es correcta y no cambia** —esa frase **no** está entre las 81 citas del gate de
literalidad, así que se parafrasea—; lo que falla es el **puntero al campo**, y esta SPEC se construye con la
disciplina de «ficha : campo» (el mismo criterio con el que R3-B4 quitó las comillas a `CHN-13` por vivir en
`dato` y no en `cita_literal`). Quien vaya a verificarlo abre `CHN-22`, no encuentra la frase y no sabe si el
problema es la ficha o la SPEC.

**Evidencia.** `SPEC:67` · `guia-chocolateria-verificacion-legal-2026-09-12.json`, `CHN-22.nota` (sin la frase) y
`CHN-22.dato` («el art. 2.15 excluye…») · `CHN-23.nota` («El punto 15 define «operador» «excluidos los operadores
posteriores»»).

**FIX.** `SPEC:67` → «⚠️ **La exclusión “excluidos los operadores posteriores” del punto 15 consta en el `dato` de
`CHN-22` y en la `nota` de `CHN-23`, en NINGUNA `cita_literal`: no está entre las 81 del gate de literalidad, así
que se PARAFRASEA, no se entrecomilla**, hasta que se abra el consolidado y entre como cita propia.»

---

## Qué hacer con esto

Las tres bajas son **cinco líneas** y van en un solo commit: el punto **(e)** de D53, las dos líneas del colchón
(§2.2 libro 7 y §3.4) y el puntero de campo de D5. **Ninguna condiciona el orden de construcción**, así que
pueden aplicarse antes o después de arrancar los constructores; conviene hacerlo **antes de `datos_ejemplo.py`**
únicamente por R5-B2, que es donde vive el valor por defecto del colchón.

**Lo que NO hay que volver a mirar:** los 5 hallazgos de la ronda 4 (aplicados, tabla de arriba), los 11 de la
ronda 3, los 15 de la ronda 2 y los 23 de la ronda 1 (todos con su fila en el Cierre y verificados en su ronda),
la política de D53 (seis sitios), la lista única de OCHO cruces y su reparto por constructor, el fondo de maniobra
(calculado una vez, contado una vez), el presupuesto (sumado fila a fila en las tres publicaciones), los ids
(cero inexistentes; los excluidos, citados como tales; los once bare, sólo en D44), los literales legales de la
muestra, la aritmética del índice (21 sumas, 40 bloques, 37.900 palabras, 28 referencias, 75 m²) y los baselines
del repo (48 productos, 49 `productId:`, 10 fichas de guía + `types.ts`, 11 xlsx del kit).

**La SPEC queda LISTA para construir.**

Via: Claude Code
