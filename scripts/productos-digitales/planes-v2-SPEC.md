# Familia «Planes de Negocio» — v2.0 (SPEC, 2026-08-29)

Origen: rondas 1 adversariales de los **DOS representantes** —`auditorias/plan-negocio-bar-restaurante-R1.json` (línea A, **93 hallazgos**: TEC 27 · DOM 36 · COM 30,
«no listo» ×3) y `auditorias/plan-negocio-cocteleria-eventos-R1.json` (línea B, **98 hallazgos**: TEC 26 · DOM 37 · COM 35, «no listo» ×3)— más un **censo propio
de los 10 productos** hecho para esta SPEC (openpyxl + python-docx, 2026-08-29). Lo que sigue es lo que SE HACE; lo demás se descarta en §6 o se pregunta en §7;
la evidencia vive en los dos R1 y se cita aquí por id. El **hotfix de no latinos del 29-ago** (`auditorias/hotfix-no-latinos-docx-2026-08-29.json`) ya limpió 7
docx y **no se revierte**: sus **17 erratas anotadas y NO tocadas** («horno de convención», «mudança», restos en inglés, comas sin espacio) las absorbe §4.

Método y código de referencia: `guias-v2-SPEC.md` (plantilla de formato y **mismo pipeline de documentos**), `kit-plan-financiero-v2-SPEC.md` §7-bis (decisiones
1-14, **se heredan tal cual**) con `kit-plan-financiero-v2_0/` (`motor.py`, `grupo_b.py` tesorería e IVA, `grupo_c.py` informe bancario: cuadro francés con
carencia y vencimiento, TIR/VAN/payback del proyecto, DSCR **antes** de deuda, semáforos con `ISNUMBER`, «sin dato» = `""`), `kit-tareas-v2_0/motor.py` (motor de
familia + módulo de contenido por producto) y `kit-escandallos-v2_0/bono_guia.py` (texto con `bridge.py` → Markdown → docx + PDF con saneado WinAnsi).

Paquete nuevo: `scripts/productos-digitales/planes-v2_0/` — `motor.py`, `grupo_a.py` (línea A), `grupo_b.py` (línea B), `documentos.py`,
`contenido_<pid>.py` (uno por plan), `guion_<pid>.py` (guion de secciones por plan), `main.py`. Ejecución real **sólo** con `PLANES_APPLY=1`; `--dry-run` por
defecto escribiendo a scratchpad. Nada de builds locales ni navegador; `istats cpu temp` antes de cada python y **un proceso cada vez**.

---

## Alcance medido (censo propio, 2026-08-29)

**76 ficheros en 10 productos**: 30 `.xlsx` + 46 `.docx`. **0 caracteres no latinos** tras el hotfix del 29-ago (barrido rehecho hoy: 0 en xlsx y 0 en docx).

⚠️ **Dos de los diez NO siguen el patrón `plan-negocio-*`**: sus carpetas y sus claves en `netlify/functions/get-download-urls.ts` son
`plan-catering-tematico-eventos` y `plan-chef-privado-showcooking-eventos`. Los ids exactos son los que manda `get-download-urls.ts:673-760`.

| pid | € | línea | ficheros | xlsx | **xlsx con 0 fórmulas** | fórmulas | docx plan (palabras) | docx totales (palabras) | checklist (ítems / DV / CF) | Fase A: ver · bio |
|---|---|---|---|---|---|---|---|---|---|---|
| **plan-negocio-bar-restaurante** (rep. A) | 35 | **A-α** | 3 | 2 | **2** | 2 | 6.971 | 6.971 | 51 · 1 · 1 | 1/2 · **1/2** |
| plan-negocio-tapas-bar | 35 | A-β | 3 | 2 | **1** | 12 | 6.873 | 6.873 | 68 · 6 · 6 | 1/2 · 0/2 |
| plan-negocio-cafeteria | 29 | A-β | 3 | 2 | **1** | 12 | 6.508 | 6.508 | 69 · 6 · 6 | 1/2 · 0/2 |
| plan-negocio-panaderia | 35 | A-β | 3 | 2 | **1** | 12 | 6.924 | 6.924 | 62 · 6 · 6 | 1/2 · 0/2 |
| plan-negocio-food-truck | 29 | A-β | 3 | 2 | **1** | 12 | 6.948 | 6.948 | 63 · 6 · 6 | 1/2 · 0/2 |
| **plan-negocio-cocteleria-eventos** (rep. B) | 55 | **B-γ** | 9 | 4 | **2** | 25 | 6.962 | 17.154 | 76 · 6 · 6 | 2/4 · **1/4** |
| plan-negocio-parrillero-asador-eventos | 45 | B-γ | 11 | 4 | **2** | 45 | 2.447 | 11.300 | 93 · **0** · **0** | 2/4 · 0/4 |
| plan-negocio-paellero-eventos | 45 | **B-δ** | 11 | 4 | **2** | 143 | 2.440 | 7.639 | 110 · **0** · **0** | **0/4** · 0/4 |
| plan-catering-tematico-eventos | 45 | B-δ | 11 | 4 | **2** | 150 | 2.841 | 10.312 | 113 · **0** · **0** | **0/4** · 0/4 |
| plan-chef-privado-showcooking-eventos | 45 | B-δ | 11 | 4 | **2** | 145 | 2.604 | 9.788 | 110 · **0** · **0** | **0/4** · 0/4 |

**Lo que el censo cambia respecto de la lectura de los dos R1** — y que obliga a que esta SPEC sea de FAMILIA, no de los representantes ampliados:

1. **La familia tiene CUATRO moldes de plan financiero, no dos.** **A-α** (bar-restaurante): ingresos derivados de `cubiertos × ticket × días` en filas de input,
   hojas numeradas `'1. Inversion Inicial'`…`'5. Personal'`. **A-β** (los otros 4): ingresos como **4 líneas tecleadas por familia de producto**, sin ningún
   input de ticket ni de cubiertos en el P&L, hojas sin numerar `'Inversion Inicial'`, `'PyG 3 Anos'`, `'Punto Equilibrio'`, `'Escenarios'`, `'Personal'`,
   `'Instrucciones'`. **B-γ** (coctelería, parrillero): las mismas 6 hojas de A-β adaptadas a eventos, con `'Personal Freelance'`. **B-δ** (paellero, catering,
   chef-privado): hojas completamente distintas —`'Resumen'`, `'P&L Año 1'` (12 meses), `'Proyección 3 años'`, `'Break-even'`, `'Mix B2C-B2B'`, `'KPIs'`—,
   **con fórmulas** pero con **todas las tasas escritas dentro de la fórmula** (`=B7*0.28`, `=1-0.28-0.05-0.12`, `=850*0.35+1850*0.65`, `=B31*0.4`) y **sin hoja
   de Instrucciones**. Un motor que dé por hecho el molde del representante destroza los otros tres.
2. **El defecto que hunde la línea A no es de bar-restaurante: es de los cinco, y crece.** El P&L imputa un coste de personal que **no es el de su propia hoja
   `Personal`**, medido hoy: bar 115.200 € frente a 209.171 € (**−93.971**), tapas-bar 96.000 frente a **209.174** (−113.174), cafetería 72.000 frente a
   **137.270** (−65.270), food-truck 42.000 frente a **76.566** (−34.566), panadería 72.000 frente a su total de hoja. Con el dato de su propia hoja, el coste
   laboral real es el **66,3 %** de las ventas en bar, el **77,5 %** en tapas-bar (`Instrucciones!A9` fija el techo en 32-38 %), el **72,2 %** en cafetería
   —donde la propia `Personal!F10` lo escribe: «~72% sobre ventas previstas» mientras el P&L imprime 37,9 %— y el **56,7 %** en food-truck (techo declarado
   25-32 %). **Los cinco planes son inviables con sus propios datos** y ninguno lo dice. (TEC-01, DOM-01, COM-03 → FAMILIA 5/5.)
3. **La promesa de fórmulas es falsa en 6 de los 10 y la de «plan de financiación» en los 10.** «fórmula(s)» aparece en las 10 landings (1-5 veces por producto)
   y los 5 planes financieros de línea A + el de coctelería tienen **0 celdas de fórmula**. «financiación» aparece en las 10 landings y en 16 componentes SPA
   (`WhySection`, `FaqAccordion`, `CtaFinal`) y **ninguno de los 30 xlsx tiene una hoja, un bloque ni una fila de origen de fondos, cuota o cuadro de
   amortización**. (TEC-03/TEC-08/DOM-10/COM-04/COM-09 del rep. A + TEC-02/TEC-21/DOM-19/COM-05 del rep. B → FAMILIA 10/10.)
4. **El changelog miente en los diez.** `productos-changelog.ts` dice «Revisión completa de los **2** ficheros» en los 5 de línea A (que entregan **3**) y «de los
   **4** ficheros» en los 5 de línea B (que entregan **9** u **11**). Peor: **paellero, catering y chef-privado no tienen la línea «Versión 1.1» en ninguno de
   sus 4 xlsx** —la Fase A no llegó a ellos—, así que su entrada v1.1 del changelog documenta una revisión que no ocurrió. Medido: la **bio anclada** está en
   **2 de los 30 xlsx** y la línea de versión en **8 de 30**. (DOM-27, COM-18, COM-16 → FAMILIA 10/10, con agravante en 3.)
5. **Los 46 docx están en tamaño CARTA (US Letter) con `author='python-docx'` y `title=''`.** Los 46, sin excepción. DOM-28 era un hallazgo del representante y
   es un defecto de los 46 ficheros de la familia. La Fase A sólo tocó xlsx.
6. **La línea B-δ vende un plan de negocio de 2.440-2.841 palabras**, frente a las ~6.900 de la línea A y del representante B. Además **0 estilos `Heading`** en
   sus 21 docx (no hay panel de navegación ni índice en Word), frente a los 10 `Heading` de los planes de línea A. Y sus tres «plan-de-negocio» llevan sólo 2, 6
   y 7 tablas para todo el documento.
7. **Los cuatro «break-even» de la línea B-δ son 3-30 veces menores que los que anuncia su propia landing.** Medido con las fórmulas del fichero: paellero
   `Break-even!B9 = 8.400 / (1.500 × 0,55) = 10,2 eventos/año` frente a «Break-even 18-22 eventos año 1» de la landing; catering `10.560 / (3.695 × 0,52) =
   5,5 eventos/año`, es decir `B10 = 0,46 eventos/mes`, frente a «**break-even 14 eventos/mes** año 1» de la landing —**factor 30×**—; chef-privado
   `7.800 / (1.102 × 0,62) = 11,4/año`. La causa es la misma que en coctelería (DOM-05): los «costes fijos» son sólo cuota + seguro + marketing + furgo, sin
   amortización, sin retribución del fundador y sin impuesto.
8. **Defectos que ningún R1 podía ver porque sólo existen en los hermanos** — nueve, todos medidos hoy, detallados en §2.12 y §3.10: `NUEVO-01` a `NUEVO-09`.

---

## Decisión: post-proceso de familia para los xlsx, PRODUCCIÓN NUEVA para los docx

**No hay ningún generador que reejecutar.** `scripts/` contiene `generate-plan-financiero.py`, pero es el generador del **producto `kit-plan-financiero`**
(`OUTPUT_DIR = .../public/dl/kit-plan-financiero`, líneas 14-19), no de esta familia. Comprobado: `git log --diff-filter=A` sobre los directorios de los tres
productos devuelve un único commit, `7e050c5` («los 524 entregables daban 404 desde el 19-jul»), que sólo los MOVIÓ; y `git log --diff-filter=D` sobre
`scripts/*plan-negocio*` no devuelve nada. **Los 76 ficheros de esta familia se produjeron con agentes ad-hoc y nunca se commiteó el código.** Consecuencias:

0. **No hay «reejecutar el generador» como opción**: no existe. La alternativa a un post-proceso sería escribir 10 generadores desde cero y **reproducir a mano
   los 76 ficheros**, incluidas las 88-96 filas de proveedores reales y las 110 de checklist que hoy son correctas.
1. **Reescribir desde cero REVIERTE la Fase A** donde sí llegó: A4 (`paperSize=9` + `fitToWidth=1`), `creator='AI Chef Pro'`, casilla unificada y la caché de
   valores de `inject_cache.py` en los 18 xlsx que la recibieron. Es el patrón que ya costó dinero con los ensambladores del blog (`CLAUDE.md`: «RECONSTRUYEN el
   cuerpo entero… pisan las ediciones manuales posteriores»).
2. **El defecto es el mismo en varios productos a la vez** (personal desacoplado en 5, break-even sin amortización en 4, ejemplos tecleados en 4, changelog mal
   contado en 10, docx en Carta en 46): se escribe una vez en el motor y se aplica por familia, y el módulo por plan sólo lleva **lo que de verdad cambia**
   (nombres de hoja, filas, cifras del concepto).
3. **La infraestructura ya existe.** `postprocess-transversal.py` declara aplicar a los 42 productos de `astro-site/public/dl/` y ya lleva parches por (fichero,
   hoja, celda). `planes-v2_0/` extiende ese patrón; no lo inventa.
4. **Es idempotente y auditable**: `--dry-run` a scratchpad, respaldo previo, segunda pasada = 0 cambios, verificación `data_only`, y `censo-entregables.py` /
   `gate-flujo-postpago.py` como red.
5. **Excepción: los 46 docx no se post-procesan del todo.** Los **10 «plan-de-negocio-*.docx»** se **regeneran enteros** con `bridge.py` desde un guion que cita
   las celdas del xlsx (§4.2-§4.3) — ahí no hay nada que parchear: el texto entero contradice al Excel. Los **36 docx restantes de línea B** (cartas, catálogos,
   contratos, manuales, experiencias, guías) se **corrigen quirúrgicamente** salvo los que el R1 declara rotos de raíz —la `carta-15-cocktails-tematicos.docx`,
   cuyos 45 bloques de escalado están al 50 % (DOM-01/COM-01), y sus tres gemelas de carta— que se **recalculan y regeneran**. **Los nombres de fichero no
   cambian** en ninguno de los dos casos (§7-bis.1).

---

## Convenciones de familia (heredadas y verificadas)

Editables **verdes `E8F5E9`** y desbloqueadas, calculadas sin relleno; **parámetros en celda, nunca literales dentro de la fórmula**; `IFERROR` en toda
división; «sin dato» se escribe `""`, **nunca `0`**; semáforo por formato condicional (verde `C6EFCE`, ámbar `FFEB9C`, rojo `FFC7CE`) y **con `ISNUMBER`** en la
guarda; DV con `showErrorMessage=True`; protección de hoja **sin contraseña**; bio anclada («En cocina desde los 17 años · consultor gastronómico desde 2010»);
«Versión 2.0 · agosto 2026 · aichef.pro/<pid> · info@aichef.pro»; metadata `title`/`subject` → `… · v2.0`; `inject_cache.py` al final; A4 donde ya está, y
**A4 nuevo en los 46 docx**.

**pycel 1.0b30** (medido en este Mac el 2026-08-29 para la familia de guías): evalúan `SUM`, `SUMPRODUCT`, `SUMIF`, `COUNTIF`, `IFERROR`, `IF`/`AND` anidados,
`TEXT`, `NPV`, `ROUND`, `MATCH`+`INDEX`. **NO implementa `IRR`, `PMT` ni `COUNTA`**: `COUNTA(r)` → `COUNTIF(r,"<>")`; la cuota del préstamo va como **anualidad
algebraica** `importe*i/(1-(1+i)^-n)`, nunca `PMT`; la TIR se cachea por Newton (precedente: `kit-plan-financiero-v2_0/grupo_c.py`).

---

## 1. Motor común (`motor.py`) — lo que se aplica a los **30 xlsx** de los 10 planes

### 1.1 Detección de molde y aborto si no lo reconoce

El motor **mide antes de escribir**. Firma de cada molde, por nombres de hoja exactos:

| molde | productos | firma (nombres de hoja) |
|---|---|---|
| **A-α** | bar-restaurante | `'1. Inversion Inicial'`, `'2. P&L 3 Anos'`, `'3. Punto Equilibrio'`, `'4. Escenarios'`, `'5. Personal'`, `'Instrucciones'` |
| **A-β** | cafeteria, food-truck, panaderia, tapas-bar | `'Inversion Inicial'`, `'PyG 3 Anos'`, `'Punto Equilibrio'`, `'Escenarios'`, `'Personal'`, `'Instrucciones'` |
| **B-γ** | cocteleria, parrillero | idem A-β con `'Personal Freelance'` (coctelería) o `'Estacionalidad'` + `'Pricing Modelo'` (parrillero) |
| **B-δ** | paellero, catering, chef-privado | `'Resumen'`, `'P&L Año 1'`, `'Proyección 3 años'`, `'Break-even'`, `'Mix B2C-B2B'`, `'KPIs'` |

Y cuatro moldes de checklist: **C1** monolítico con DV+CF (bar-restaurante, 51 ítems) · **C2** `F1..F6` con 2 `COUNTIF` por hoja + DV + CF (cafetería,
food-truck, panadería, tapas-bar, coctelería) · **C3** `F1..F6` **sin fórmulas, sin DV y sin CF**, con una instrucción («Marca [X] cuando completes el item»)
que apunta a **una columna que no existe** (parrillero: `#` · `Tarea` · `Tiempo estimado` · `Responsable` · `Notas`) · **C4** monolítico `'Checklist 6 fases'`
con columna `OK` **vacía, sin DV, sin CF y sin contador** (paellero, catering, chef-privado). Dos moldes de calculadora (§3.1, §3.2) y dos de proveedores
(§3.7). **Si la firma no coincide con ninguna, el motor aborta con el nombre del fichero**; no adivina.

### 1.2 Hoja/bloque de parámetros — todo número que hoy vive dentro de una fórmula o de un rótulo sale a una celda

Línea A: hoja nueva **`Supuestos`** (§2.1). Línea B: bloque **`PARÁMETROS`** dentro de `Instrucciones` (B-γ) o de `Resumen` (B-δ, que hoy no tiene
`Instrucciones`). Ningún literal sobrevive dentro de una fórmula: hoy `'P&L Año 1'!B9='=B7*0.28'` obliga a editar **26 fórmulas** para cambiar el food cost, y
`'Break-even'!B7='=1-0.28-0.05-0.12'` lo obliga otra vez en un tercer sitio con **el mismo número escrito dos veces**. (TEC-19 rep. B, `NUEVO-04`.)

### 1.3 Constantes tecleadas → fórmulas, **conservando el número como dato de ejemplo**

Los 6 xlsx con 0 fórmulas (5 planes financieros de línea A + el de coctelería) y las columnas constantes de B-γ/B-δ se cablean. **No se borra ningún número que
el cliente pueda estar usando**: se convierte en el valor de la celda de input, y la diferencia entre el valor viejo y el nuevo calculado queda anotada por
fichero en el informe de la tanda. Decisión heredada de `guias-v2-SPEC.md` §7-bis.12.

### 1.4 Formatos por tipo de dato, no por bloque

Censo de defectos de formato encontrados hoy, todos corregibles por tabla en el motor:

- **Recuentos con formato de euro**: `Escenarios!B5:D5` «Clientes/día» → «45 €» (cafetería, tapas-bar, food-truck, panadería); `Escenarios!B7:D7` «Días
  apertura/año» → «300 €»; `'Punto Equilibrio'!B10:B11` «Clientes/día» → «53 €»; `'Proyección 3 años'!B5:D6` «Eventos B2C/B2B totales» → «57 €» (paellero,
  catering, chef-privado); `'5. Personal'!B6:B13` «Personas» → «7 €» (bar). (TEC-16, TEC-08, COM-17.)
- **Importes en euros con formato de porcentaje** — `NUEVO-05`, no visto por ningún R1 y presente en **las tres calculadoras de B-δ**:
  `'Calculadora pricing'!B31='=B29*0.3'` con `number_format='0.0%'` (paellero), `B33='=B31*0.4'` (catering), `B32='=B30*0.4'` (chef-privado). Un anticipo de
  483,48 € se imprime como **«48348,0 %»** en la celda que el cliente copia al contrato. Y en parrillero, `'Estacionalidad'!B17='=SUM(B5:B16)'` con `0.0%`.
- **Decimales significativos ocultos**: `'2. P&L 3 Anos'!B8:D8` ticket 18,5 con `'#,##0 €'` → «19 €», mientras `'3. Punto Equilibrio'!B9` usa `'#,##0.00 €'`
  para el mismo dato (TEC-09). Igual en `Escenarios!B6:D6` de cafetería (9,5 → «10 €») y de panadería (4,5 → «5 €»).
- **Formato `'#,##0 €/h'`** con la `h` sin entrecomillar: openpyxl devuelve `datetime(1900,1,22)` (TEC-07, DOM-16, COM-18). Pasa a `'#,##0" €/h"'`.
- **Magnitudes guardadas como texto** con punto decimal anglosajón: `'Punto Equilibrio'!B6='66.1%'` (los 4 de A-β), `B13='5.8%'`, `'PyG 3 Anos'!E13:E40`,
  `'Personal Freelance'!F13:F16='350 EUR'`, `'Mix B2C-B2B'!F5:F14='55%'`, `KPIs!B6='1.200 €'`. Pasan a número con formato (TEC-22).
- **`General` en las dos cifras estrella**: `'3. Punto Equilibrio'!B14=17950` y `B15=57.9` (TEC-21).

Regla del motor, aplicable sin lista: **si el rótulo de la fila contiene «Eventos», «Clientes», «Cubiertos», «Personas», «Días», «Meses» o «Unidades», la celda
no lleva formato de euro; si contiene «Anticipo», «Precio», «Coste», «Ingresos» o «Margen (€)», no lleva formato de porcentaje.**

### 1.5 Validación de datos y guardas en las fórmulas

Medido: **0 `dataValidation` y 0 reglas de formato condicional en los 10 planes financieros y en las 4 calculadoras**. Se añaden: decimal `>0` en todo input de
precio y volumen, entero `1-365` en días, lista cerrada en todo campo que hoy es texto libre y que una fórmula compara por igualdad —`'Calculadora'!C8` (nivel
de bebida), `C12` (`S`/`N`), `'Calculadora pricing'!B5` (`B2C`/`B2B`), `B9`/`B11`/`B12`/`B13` (`sí`/`no`), `B8` (tipo de paella), `B10` (nivel de calidad)—.
Motivo medido: `'Calculadora'!F16='=C5*C6*IF(C8=1,F5,IF(C8=2,F6,F7))'` cae en la rama **premium** ante cualquier valor distinto de 1 o 2, y
`=IF(B9="sí",1.18,1.00)` cae en la rama barata si el usuario teclea «si» sin tilde. **Ninguna de las dos avisa** (TEC-10, DOM-37, COM-19). Toda división lleva
`IFERROR(...;"")`, empezando por `F30='=F27/C5'`, que hoy devuelve `#¡DIV/0!` con el campo de invitados vacío.

### 1.6 Semáforo con `ISNUMBER`

Formato condicional sobre los ratios de §2.9 y §3.4.11 y sobre toda fila de resultado que pueda quedar negativa, con la guarda `ISNUMBER` porque esas celdas
pueden traer `""` (§7-bis heredado, decisión 13 del kit plan financiero).

### 1.7 Ortografía: acentos, eñes y erratas

Medido: **9-11 familias de palabra sin tilde por fichero** en los 10 planes financieros y en 7 checklists («Ano», «Espana», «Analisis», «Constitucion»,
«Tramite», «Diseno», «Nominas», «Amortizacion», «Comision», «Gestoria», «Bolleria», «Cumpleanos», «danos», «Cataluna»), conviviendo con las **únicas** celdas
acentuadas del libro, que son las dos que inyectó la Fase A. Se corrigen los textos **y los nombres de hoja** (`'2. P&L 3 Anos'` → `'2. P&L 3 Años'`,
`'PyG 3 Anos'` → `'PyG 3 Años'`; ojo: renombrar una hoja obliga a reescribir las referencias entre hojas que el motor acaba de crear, así que el renombrado va
**después** del cableado y con re-verificación). Gate: falla si aparece `Ano `, `Espana`, `Diseno`, `resenas`, `desempeno`, `alergenos`, `danos`, `Cataluna`,
`Cumpleanos` fuera de URL o correo, con la excepción legítima **«campana extractora»** (que convive en el mismo libro con «Campana lanzamiento RRSS», que sí es
errata). Erratas puntuales cazadas: `'Checklist Apertura'!F36='Priorizarcexperiencia hosteleria'` (TEC-26) y `Indice!B15='6. Frutas, herbas y garnish'`
(TEC-23). (TEC-15, TEC-13 rep. B, COM-23.)

### 1.8 Anchos, altos y celdas combinadas con `wrapText`

32 celdas del pack del representante A con `wrap_text` sobre alto fijo de 22 pt que sólo da para una línea (TEC-14), y 5 bloques combinados **sin alto fijado**
en el representante B, entre ellos la `CONCLUSION` de `'Punto Equilibrio'!A18:C18` (313 caracteres, se ve 1 línea de 4) y la nota de autoría de
`Indice!B4:D7` (606 caracteres en 4 filas que necesitan 9) (TEC-09 rep. B). Norma del motor: **toda celda combinada con `wrapText` lleva
`height = ceil(len/ancho) × 15 pt` repartido entre sus filas**, y toda fila de datos con `wrap` pierde el alto fijo o sube a 34 pt.

### 1.9 Instrucciones, versión, bio, metadata y cross-sell

- **Hoja `Instrucciones` en los 12 xlsx que no la tienen** (las 4 calculadoras, los 4 checklists de C3/C4, los 3 planes financieros B-δ, la plantilla de
  proveedores de B-δ), con la leyenda de la casilla que hoy falta (§3.8) y el aviso de qué celdas son editables.
- **Línea de versión en 22 xlsx y bio anclada en 28** (medido: hoy 8/30 y 2/30).
- **Metadata** `creator`/`lastModifiedBy`/`title`/`subject` = `AI Chef Pro` · `<nombre del producto> · v2.0` en los 12 xlsx que la Fase A no alcanzó.
- **Cross-sell sin precios**: el cierre del docx del representante A lista cuatro productos con importe escrito a mano dentro de un fichero ya descargado
  (DOM-35, COM-30, y «300+ prompts» donde el catálogo dice 200+). Se sustituyen por nombre + una única URL a `aichef.pro/productos-digitales`. La marca
  ChefBusiness **se mantiene** (`feedback_marca-chefbusiness-en-productos-aicp-es-deliberada.md`); lo que se quita es el importe.

### 1.10 Hipervínculos y coherencia de nombres

`ws._hyperlinks` está vacío en las 11 hojas de la plantilla de proveedores del representante B: el índice no enlaza a las pestañas y las URLs de la hoja
`'10. Hosply.pro'` son texto plano (TEC-23). Se añaden hipervínculos internos (`celda.hyperlink = "#'6. Frutas y garnish'!A1"`) y externos, y se igualan los
rótulos del índice a los nombres exactos de las pestañas.

---

## 2. Línea A — el plan financiero pasa a ser un MODELO (`grupo_a.py`)

Aplica a los 5 productos de línea A. Las referencias de celda son las de **A-α** (bar-restaurante, el representante); el módulo `contenido_<pid>.py` traduce el
mapa a **A-β** (donde las hojas no van numeradas y los ingresos son 4 líneas por familia de producto en vez de `cubiertos × ticket × días`).

### 2.1 Hoja nueva `0. Supuestos` — la única entrada de datos del libro

Se inserta **la primera**, con las celdas de input en verde `E8F5E9` y DV. Bloques y celdas (A-α; A-β usa las mismas etiquetas con su propio desglose de
ingresos):

| bloque | celdas | contenido |
|---|---|---|
| ACTIVIDAD | `B4` cubiertos/día año 1 · `B5` ticket medio **sin IVA** · `B6` días de apertura/año · `B7:B8` crecimiento año 2 y año 3 | hoy tecleados en `'2. P&L 3 Anos'!B7:D9` |
| MIX Y COSTE DE MERCANCÍA | `B11` % de ventas de **comida** · `B12` % de ventas de **bebida** (`=1-B11`, calculada) · `B13` food cost sobre comida · `B14` coste de bebida sobre bebida · `B15` consumibles % · `B16` **% de ventas por delivery (0 por defecto)** · `B17` comisión de la plataforma | resuelve TEC-04/DOM-04 (doble conteo) y TEC-23/DOM-34 (delivery al 100 %) |
| PERSONAL | `B20` tipo de SS a cargo de la empresa (**33 %**, en celda, heredado de `kit-gestion-personal-v2-SPEC.md`) · `B21` nº de pagas (14) | hoy `33.4%` escrito en el rótulo de `'5. Personal'!D5` |
| LOCAL Y FIJOS | `B24` alquiler mensual · `B25` fianza en meses · `B26` suministros/mes · `B27` seguros/año · … | |
| FINANCIACIÓN | `B30` recursos propios · `B31` importe del préstamo · `B32` tipo nominal · `B33` plazo (años) · `B34` carencia (años) | alimenta §2.8 |
| FISCAL | `B37` tipo IS entidad de nueva creación (**15 %**) · `B38` tipo IS general (25 %) · `B39` IVA repercutido comida (10 %) · `B40` IVA repercutido bebida alcohólica (21 %) · `B41` IVA soportado (21 %) | resuelve TEC-06/DOM-15/COM-13 y TEC-11/DOM-30 |
| AMORTIZACIÓN | `B44` vida útil de obra e instalaciones · `B45` vida útil de maquinaria y mobiliario | resuelve TEC-20/DOM-34 |

**Todas las demás hojas del libro se derivan de aquí por fórmula.** Nada se teclea dos veces.

### 2.2 `1. Inversión Inicial` — subtotales por bloque y fondo de maniobra calculado

- **Subtotal en la celda B de cada encabezado de bloque** (`A6`, `A13`, `A24`, `A34`, `A38`, `A43`) con `=SUMA(...)`, y `%` sobre el total en la columna C
  (TEC-22). Hoy sólo existe el total general `B46`.
- **`B44` (fondo de maniobra) = `=3*'2. P&L 3 Anos'!$B$30/12`**, con el rótulo generado por fórmula desde los meses de `Supuestos`, no escrito a mano. Hoy la
  etiqueta dice «3 meses de costes fijos» y cubre **1,87 meses** en bar-restaurante y **0,91** en cafetería (9.000 € frente a 9.892 €/mes), mientras
  `Instrucciones!A15` exige el mínimo de 3 meses. (TEC-07, DOM-12, COM-06 → FAMILIA 5/5, `NUEVO-01`.)
- **Fila nueva `IVA soportado sobre la inversión (21 %, recuperable)`** que suma a la caja necesaria aunque se marque como recuperable (TEC-11).
- **Tres partidas que sólo existen en el Word** (terraza, stock inicial, imprevistos) se incorporan al Excel, que pasa a ser la fuente única (DOM-19).
- `B46 = suma de los seis subtotales`. El rango publicitado de `Instrucciones` y de la landing se **recalcula después**, no antes (§5.2).

### 2.3 `2. P&L 3 Años` — la cadena completa

1. **Personal desde su propia hoja**: `B20 = ='5. Personal'!$F$13`, `C20`/`D20` con el crecimiento de `Supuestos`. Es el fix de TEC-01/DOM-01/COM-03 y de sus
   cuatro gemelos. **Con la cifra correcta los cinco planes dan pérdidas**, así que el módulo de contenido tiene que **redimensionar la plantilla** de
   `5. Personal` hasta que `B39` («Coste personal / Ingresos») quede por debajo del techo que declara `Instrucciones` (35 % en bar, 32-38 % en tapas-bar,
   35-40 % en cafetería, 25-32 % en food-truck, 35-42 % en panadería) — o subir cubiertos/ticket. **Un plan cuyo caso base suspende su propio semáforo no se
   publica** (DOM-13).
2. **Sin doble conteo de bebida**: `B10` se parte en `Ingresos comida =B10*Supuestos!$B$11` e `Ingresos bebida =B10*Supuestos!$B$12`; `B12 = comida × food cost`
   y `B13 = bebida × coste de bebida`. Hoy el 30 % se aplica al 100 % de los ingresos y encima se cobra el 22 % de la bebida: **33.119,63 € cobrados dos veces**
   en el año 1, que es lo que convierte +10.950 € en −22.170 € (TEC-04, DOM-04, COM-14).
3. **Delivery con interruptor**: `B15 = B10 * Supuestos!$B$16 * Supuestos!$B$17`, con `B16` a 0 por defecto (TEC-23, DOM-34).
4. **Impuesto de Sociedades correcto**: fila nueva `BIN acumulada pendiente`; `C33 = MAX(0;(C32-BIN_pendiente))*Supuestos!$B$37` con el **15 % de entidad de
   nueva creación aplicado a los dos primeros ejercicios con base positiva** y compensación de bases negativas (art. 26 y 29.1 LIS). Medido en el representante:
   corrige 8.905,55 € de sobre-impuesto en tres años. El **mismo defecto está en los 5**: cafetería aplica el 25 % al año 2 sin compensar los −2.590 € del año 1;
   tapas-bar, food-truck y panadería, igual. (TEC-06, DOM-15, COM-13 → FAMILIA 5/5.)
5. **Intereses, no cuota**: `A28` pasa a `Gastos financieros (intereses)` = `='7. Financiacion'!$D$<año>`; la devolución de principal sale del P&L y va a la
   tesorería (§2.7). Hoy la cuota completa de 7.200 € está dentro de «TOTAL COSTES FIJOS» y se resta del «RESULTADO ANTES DE IMPUESTOS», que así no es un P&L
   sino un flujo de caja (TEC-10, DOM-15, COM-12).
6. **Amortización sobre la base real**: `B26 = SUMA(<partidas amortizables de la hoja 1>)/Supuestos!$B$44` separando obra e instalaciones de maquinaria y
   mobiliario. Hoy 5.000 €/año implican una base de 50.000 € cuando el inmovilizado del propio libro suma 76.260 € (TEC-20, DOM-34). En cafetería es al revés:
   9.490 €/año implican 94.900 € de base sobre una inversión de 96.400 € que **incluye 9.000 € de fondo de maniobra, 7.000 € de imprevistos y 2.000 € de stock**,
   que no se amortizan (`NUEVO-02`).
7. **Ratios calculados, no tecleados**: `B38 = (B12+B13)/B10` (hoy es la constante `0,3` mientras el COGS real es 37,7 %), fila nueva `Alquiler / Ingresos` y
   fila nueva `Punto de equilibrio alcanzado (S/N)` (TEC-12).

### 2.4 `3. Punto de Equilibrio` — uno solo, derivado, y con sensibilidad

`B8 = ='2. P&L 3 Anos'!$B$30` · `B7 = B8/12` · `B9 = ='2. P&L 3 Anos'!$B$8` · `B10 = ='2. P&L 3 Anos'!$B$16/('2. P&L 3 Anos'!$B$7*'2. P&L 3 Anos'!$B$9)` ·
`B11 = B9-B10` · `B14 = SI(B11<=0;"MC negativo";B8/B11)` · `B15 = B14/'2. P&L 3 Anos'!$B$9` · `B16 = B14*B9`. Hoy la hoja usa **192.600 € de costes fijos** donde
el P&L dice **198.108,5 €** —diferencia sin origen posible— y un coste variable por cubierto 0,41 € menor, y publica 57,9 cubiertos/día donde salen 61,9
(TEC-05, DOM-11, COM-25). El **párrafo de interpretación `A19` se genera con `TEXTO()`** desde las celdas, para que no quede desfasado al recalcular (hoy además
mezcla «57.9» con punto y «10,73» con coma en la misma frase, TEC-21).

**Tabla de sensibilidad `A22:F30`** con el ticket en columnas (16,50 / 18,50 / 20,50 / 22,50 €) y el coste variable unitario en filas — la landing la promete
(«sensibilidad a ticket medio») y la hoja tiene un único escenario puntual (TEC-19, COM-25).

**Coherencia de días**: hoy `'Punto Equilibrio'` de los cuatro A-β trabaja sobre **30 días/mes** («asumiendo 30 días de apertura») mientras `Escenarios` usa
**300-320 días/año** (= 25-27/mes) y el P&L no declara días. Todos pasan a leer `Supuestos!$B$6` (`NUEVO-03`).

### 2.5 `4. Escenarios` — el mismo motor que el P&L

Fila 9 = `B6*B7*B8`; filas nuevas explícitas de food cost, bebida, consumibles y delivery calculadas sobre la fila 9 **con las mismas tasas de `Supuestos`**;
fila 11 = `='2. P&L 3 Anos'!$B$30`; fila 12 = fila9 − variables − fila11. **El escenario «Realista» debe reproducir al céntimo `'2. P&L 3 Anos'!B32`; si no
coincide, el gate falla.** Hoy da −50.658,75 € donde el P&L da −22.169,98 € **con los cinco inputs idénticos**, porque la hoja aplica en silencio un coste
variable del 55 %/55 %/50 % que no coincide con ningún dato mostrado y la fila «Food cost %» es decorativa (TEC-02, DOM-05, COM-08). En A-β el mismo defecto es
menor pero está: cafetería `Escenarios!C8=190.950` frente a `PyG!B10=190.000`, y tapas-bar `C8=279.000` frente a `B10=270.000`.

**Estructura homogénea**: cafetería tiene fila de amortización en `Escenarios` y tapas-bar no, y ninguno de los dos declara el impuesto que sin embargo aplica
(tapas-bar pasa de 45.501 € de EBITDA a 25.451 € de «RESULTADO NETO» sin una sola fila que lo explique). Las tres columnas llevan las mismas filas
(`NUEVO-06`).

### 2.6 `5. Personal` — SS en celda y fila TOTAL cerrada

`D<fila> = C<fila>*Supuestos!$B$20` (hoy el 33,4 % está escrito en el rótulo `D5`); `F<fila> = E<fila>*Supuestos!$B$21`; la fila del puesto con 2 personas
(`B11=2` en bar) homogeneiza C y D como totales de fila, que hoy son por persona mientras E y F son del total y **la fila no cuadra a la vista** (TEC-16);
`C13`/`D13` se rellenan con sus sumatorios (hoy vacías). Formato `'#,##0'` en la columna «Personas». Ningún salario por debajo del SMI vigente, y el rótulo del
convenio pasa a **provincial**, que es lo que dice el propio checklist (`F37: «Convenio hosteleria de tu provincia»`) y contradice al docx (DOM-24, COM-22).

### 2.7 Hoja nueva `6. Tesorería 12 meses`

12 columnas: cobros (con el desfase de cobro que corresponda), pagos por partida, **IVA repercutido y soportado con liquidación trimestral** (10 % comida /
21 % bebida alcohólica, tipos en `Supuestos`), **devolución de principal del préstamo** (que sale del P&L, §2.3.5), y saldo acumulado arrancando en el fondo de
maniobra. Fila de **payback sobre el flujo de caja libre acumulado**, que es la cifra que el Word repite cinco veces con cinco valores distintos (DOM-17). Es la
hoja que responde la única pregunta que decide una operación bancaria: **en qué mes se agota la caja** (DOM-14, DOM-30, TEC-11).

### 2.8 Hoja nueva `7. Financiación` — usos y orígenes + cuadro francés

Origen de fondos (recursos propios / préstamo bancario / ICO / ENISA / business angels / subvenciones autonómicas) cuadrando con `'1. Inversion Inicial'!B46`, y
**cuadro de amortización francés** con las tres decisiones ya firmadas del kit plan financiero (§7-bis heredado): **carencia anulada en origen si iguala o
supera el plazo** (decisión 12), **cuadro apagado pasado el vencimiento** (decisión 14) y **DSCR con el numerador ANTES de la deuda** (decisión 11). La cuota va
como anualidad algebraica, no `PMT`. Esto cierra la promesa que las **10 landings** hacen y que **ningún fichero cumple** (TEC-08, DOM-10, COM-04 en A;
TEC-21, DOM-19, COM-05 en B). §7-bis.1 lo permite explícitamente: es una hoja dentro de un libro existente, no un fichero nuevo.

### 2.9 `Instrucciones` — ratios que auditan y texto que dice la verdad

Los umbrales de `Instrucciones!A12:A16` pasan a **celdas** y alimentan el formato condicional de los ratios de §2.3.7. Los textos `A6` y `A7` («se calcula
automáticamente») quedan **ciertos** al cablear el libro; hoy describen un comportamiento que el fichero no tiene y llevan al cliente a imprimir cifras
obsoletas tras editar (TEC-17). Se añade la nota de IVA («todas las cifras son SIN IVA») y la conversión PVP/1,10 y PVP/1,21 (TEC-11, DOM-30).

### 2.10 Checklist de apertura — legal vigente y sin inventos

Moldes **C1** y **C2**. Contenido, con las decisiones legales ya firmadas (§7-bis.5):

- **Fuera el «carnet de manipulador obligatorio»**: derogado por el RD 109/2010. Pasa a «Formación en higiene alimentaria de todo el equipo (responsabilidad de
  la empresa; acreditar en el plan APPCC)», responsable = titular, no empleado. Y fuera del docx la «normativa de 2024» con «certificado oficial de al menos
  veinte horas», que no existe. (DOM-08, COM-11 → FAMILIA.)
- **RGSEAA sólo cuando corresponda**: el RD 191/2011 art. 2.2 excluye al minorista que sirve al consumidor final. Las dos filas duplicadas se funden en
  «Inscripción en el Registro Sanitario de la Comunidad Autónoma (declaración responsable de inicio de actividad alimentaria)» con la nota de por qué el estatal
  no aplica. (DOM-09 → FAMILIA.)
- **Cuota de autónomo parametrizada**: hoy el checklist dice «Tarifa plana 80 EUR/mes» y el docx «unos 300 euros» — casi 4× de diferencia, y ninguna de las dos
  es defendible sin fecha. Pasa a «cuota según base mínima del tramo; consulta el importe del ejercicio en curso y verifica con tu gestoría si procede la tarifa
  plana», **con nota de año**. (DOM-25, DOM-13/COM-08 del rep. B.)
- **PRL**: «Obligatorio contratar servicio externo» es falso — el art. 30.5 de la Ley 31/1995 y el art. 11 del RD 39/1997 permiten al empresario asumir la
  actividad preventiva hasta 25 trabajadores con un único centro. Se reescribe: obligatorio es el **plan**, no el proveedor. (DOM-26.)
- **Crea y Crece sin inventos**: no hay «depósito de 3.000 € a cinco años»; lo que impone la Ley 18/2022 es dotar el 20 % del beneficio a reserva legal hasta
  que capital + reserva alcancen 3.000 € y la responsabilidad solidaria de los socios por la diferencia. Y la factura electrónica B2B **no está en vigor desde
  2024**: calendario escalonado pendiente de reglamento, como ya dice bien la propia plantilla de proveedores del kit («Veri*factu obligatorio 2026-2027»).
  (DOM-13, COM-08, DOM-26 rep. B, COM-33.)
- **IAE por tipo, no por número suelto**: 671.4 es «restaurantes de dos tenedores» y se asigna a un bar-restaurante casual con barra de 5 m y ticket de 18,50 €;
  673.2 es «otros cafés y bares» y se etiqueta como «servicios de bar especiales», que es el 673.1. Se reescriben con el epígrafe **y** la nota de que la
  elección la valida el gestor. (TEC-25, DOM-33, DOM-33 rep. B, COM-34.)
- **Trámites que faltan y cuestan dinero o multa**: seguro de RC (presupuestado en `'1. Inversion Inicial'!A41` y **sin tarea que lo ejecute**), hojas de
  reclamaciones y su cartel, registro horario diario (art. 34.9 ET), contrato con gestor autorizado de residuos y aceite usado, DDD, derechos de autor por
  música ambiental, plan de prevención de desperdicio alimentario (Ley 1/2025), boletines de instalación eléctrica y de gas, comunicación de apertura del centro
  de trabajo. (TEC-18, DOM-32, COM-17.)
- **Cronograma único**: hoy el pack da tres (6 meses en el docx, 5-8 meses en el propio docx dos páginas antes, «Mes 6-8» en el checklist). Se fija el
  conservador y se propaga a las cabeceras de fase y al docx. (DOM-23.)
- **Molde C3 (parrillero)**: la instrucción «Marca [X] cuando completes el item» apunta a una columna que no existe. Se añade la columna `OK` con la DV
  `✓ / ☐ / N/A`, el contador y el formato condicional del molde C2 (`NUEVO-07`).
- **Recuento**: el número de la landing se escribe **después** de contar las filas, no antes (§5.2).

### 2.11 Demostraciones exigidas (pycel, bloqueantes)

Ninguna de estas fórmulas se da por buena sin evaluarla con inputs cambiados:

1. Cambiar `Supuestos!B4` (cubiertos) de 55 a 80 → `'2. P&L 3 Anos'!B10`, `B32`, `'3. Punto Equilibrio'!B15` y `'4. Escenarios'!C12` **se mueven los cuatro**.
2. `'4. Escenarios'` columna «Realista» == `'2. P&L 3 Anos'!B32` **al céntimo**.
3. `'2. P&L 3 Anos'!B20` == `'5. Personal'!F13`, y `B39` <= el umbral de `Instrucciones`.
4. Con `Supuestos!B16` (delivery) = 0, `B15` = 0 y todos los totales bajan en consecuencia.
5. Año 1 con pérdida → `B33` = 0; año 2 con base positiva menor que la BIN → `C33` = 0; año 3 → tipo 15 %.
6. `'6. Tesorería'` saldo mínimo acumulado >= 0 con el fondo de maniobra de `'1. Inversion Inicial'!B44`; si es negativo, el módulo de contenido sube el fondo.
7. `'7. Financiacion'` con plazo 3 y carencia 3 → años 4-5 a 0 y capital pendiente final 0 (regresión de la decisión 12/14 heredada).
8. Ninguna celda con `#¡DIV/0!`, `#¡VALOR!` ni `#¿NOMBRE?` tras `inject_cache.py`; `fallos_pycel = 0`.

### 2.12 Defectos que los R1 no podían ver (línea A) — medidos el 2026-08-29

- **`NUEVO-01`** · alta · El fondo de maniobra de **cafetería** cubre **0,91 meses** (9.000 € frente a 9.892 €/mes de costes fijos) con la etiqueta «(3 meses)»
  — la mitad de mal que el representante. Food-truck: 6.000 € frente a 5.275 €/mes = 1,14 meses. Panadería: 8.000 € frente a 10.042 €/mes = **0,80 meses**.
  Tapas-bar: 12.000 € frente a 12.925 €/mes = 0,93 meses. **Los cinco incumplen su propia regla**; cuatro de ellos por un factor de 3.
- **`NUEVO-02`** · media · La base de amortización de **cafetería** (94.900 € implícitos en 9.490 €/año) incluye fondo de maniobra, imprevistos, stock inicial y
  marketing, que no son inmovilizado. Panadería igual (10.450 sobre 105.000). Es el defecto de TEC-20 con el signo contrario: allí infradota, aquí sobredota.
- **`NUEVO-03`** · media · **Dos calendarios dentro del mismo libro** en los cuatro A-β: `'Punto Equilibrio'` calcula sobre 30 días/mes y `Escenarios` sobre
  300-320 días/año. El break-even diario publicado está por tanto un 17-20 % por debajo del que corresponde a los días que el propio libro declara.
- **`NUEVO-06`** · media · `Escenarios` no tiene la misma estructura de filas entre productos ni dentro del mismo producto: cafetería lleva amortización y
  tapas-bar no, y tapas-bar aplica un impuesto de 20.050 € sin una fila que lo declare.
- **`NUEVO-07`** · media · El checklist de **parrillero** (molde C3) manda marcar una columna que no existe, y no tiene DV, contador ni formato condicional,
  a diferencia de sus cinco hermanos de molde C2.

---

## 3. Línea B — calculadora, plan financiero de eventos, proveedores y checklist (`grupo_b.py`)

Aplica a los 5 productos de línea B. Dos submoldes con código común y tablas distintas: **B-γ** (coctelería, parrillero) y **B-δ** (paellero, catering,
chef-privado).

### 3.1 Calculadora, molde β (coctelería, parrillero) — coste **por invitado**, no × horas

Decisión firmada §7-bis.3. `F16 = '=C5*IF(C8=1,F5,IF(C8=2,F6,F7))'` y los rótulos `E5:E7` pasan a «Coste de bebida básica/media/premium **por invitado (evento
completo)**». Alternativa equivalente y preferida por el propio kit: sustituir los tres parámetros por **coste medio por cóctel** (2,20 / 3,53 / 4,80 €, tomados
del escandallo de la carta) más un input nuevo **«cócteles por invitado» (2 por defecto)**, que es como razona el resto del kit. Hoy `F6 = 4,00 €/invitado/hora`
× 5 h = **20 € de coste de bebida por invitado**, por encima del **precio de venta** por invitado de las 10 filas de Ejemplos (14,50-23,00 €): la hoja vendería
por debajo de coste, y con los inputs por defecto escupe **51,65 €/pax** contra los «12-18 EUR» que fija `Instrucciones!B21` del fichero hermano. (TEC-01,
DOM-04, COM-03.)

Además: **`F26` (PRECIO MÍNIMO) recibe la rama `IF(C12="S";…)`** que sí tienen `F27` y `F28`, porque hoy el «suelo del 35 %» deja un **23 % real** cuando hay
wedding planner, que es el canal del 60 % de la facturación (TEC-18, DOM-23); **los tres márgenes objetivo (0,35 / 0,45 / 0,55) salen a celdas** editables con
relleno de input, porque hoy son el único parámetro que el usuario no puede tocar sin editar fórmulas en una hoja rotulada «PARÁMETROS DE COSTE (editables)»
(TEC-19); **`C7` («Tipo de evento») o se conecta a un coeficiente por tipo o se etiqueta como informativo** y se retira «tipo + complejidad» de la landing y del
dashboard (TEC-11, DOM-37); y **la comisión del wedding planner se unifica** — hoy vale 12 % en la calculadora, 10 % en `PyG!A17` y «10-15 %» en
`Instrucciones!B16`, y peor: la calculadora la **repercute** al cliente mientras el P&L la **absorbe** como coste variable. **No pueden ser ciertas las dos
cosas**: se elige repercutir y se eliminan `B17:D17` del bloque de costes variables, recalculando `B18:E20` (DOM-22, COM-31).

### 3.2 Calculadora, molde γ (paellero, catering, chef-privado) — margen de verdad

Estas tres construyen el **precio** por multiplicadores y no calculan **ningún coste**: `B32/B34` («Margen estimado bruto (€)») es `=PVP*0.55` y `B33/B35` es la
constante `0,55`. El «margen» no depende de nada. Se reconstruye la hoja con un bloque `COSTE DEL EVENTO` en celdas —materia prima por pax (desde la carta),
logística por km (hoy `0,95 €/km` dentro de la fórmula `=B7*0.95*2`), ayudantes (`=B10*120`, con la tarifa en celda), consumibles y menaje— y
`Margen (€) = PVP − Coste total`, `Margen (%) = Margen/PVP`, con semáforo contra el objetivo. Y `Anticipo` con formato de euro (`NUEVO-05`, §1.4).

### 3.3 Hoja `Ejemplos` / `10 ejemplos validados` — generada por el motor, no tecleada

**Decisión firmada §7-bis.3: los ejemplos SALEN del motor.** El motor añade a la tabla las columnas de input que hoy faltan (premium sí/no, showcooking sí/no,
nº de ayudantes, nivel de calidad) y **calcula `PVP` y `€/pax` con las fórmulas de la hoja `Calculadora`**, referenciando sus parámetros. Medido hoy en los dos
submoldes:

- **B-γ (coctelería)**: las 10 filas están 1,78×-4,26× **por debajo** de lo que da su propia calculadora, y 2 de las 10 ni siquiera respetan el 45 % que declara
  su columna (`F5=870` donde `410/(1-0,45)=745`; `F7=3.450` donde `(1.530/0,55)/0,88=3.160`). (TEC-06, DOM-04, COM-03.)
- **B-δ (paellero, catering)**: reproducibles en los casos simples (ejemplo #4 del paellero: la fórmula da 1.611,60 € y la tabla publica 1.620 €, 0,5 % de
  diferencia) y **desviados en los premium**: paellero #3 da 3.179 € frente a 3.850 publicados (+17 %) y #9 da 4.277 € frente a 5.850 (+27 %); catering #7 da
  **≥2.700 €** frente a **1.950 publicados**, es decir la tabla enseña a cobrar un **38 % por debajo** de lo que dice la propia calculadora. (`NUEVO-08`.)

**Gate**: cada fila de ejemplo debe reproducirse con sus propios inputs; si difiere más de un 1 %, falla.

### 3.4 Plan financiero de eventos

1. **Inversión sin dobles ni excluyentes** (B-γ): fuera del sumatorio las partidas **recurrentes** que el P&L ya carga en el año 1 —`B6` alta de autónomo y
   gestoría 600 €, `B10` seguro RC 600 €, `B11` multirriesgo 350 €, contra `PyG!B23`=3.960 € y `PyG!B26`=1.100 €: **1.550 € contados dos veces** (TEC-12)— y
   fuera la **SL** (`B7`=800 €), que es alternativa excluyente del alta de autónomo según el propio fichero y el propio checklist (COM-26). «Imprevistos (8 %)»
   pasa a `=REDONDEAR(SUMA(B6:B28)*Supuestos_imprevistos;0)`; hoy 2.200 € sobre 37.830 € es el **5,82 %** (TEC-20, COM-23). Y en B-δ, `Resumen!B/C/D21` ya suman,
   pero **ninguna de las tres cifras (8.520 / 21.410 / 54.440 en catering; 3.790 / 9.670 / 23.110 en paellero) coincide con las que dicen su docx ni su landing**
   (§5.2, `NUEVO-09`).
2. **El supuesto de consumo, explícito** (B-γ): el P&L descansa en **0,93 copas por invitado** en una barra libre de 5 h (14.000 € ÷ 50 eventos = 280 €/evento
   ÷ 3,53 €/cóctel = 79 copas para ~85 invitados). Con 4-5 copas la materia prima pasa del 20 % a más del 50 % de la facturación y el ticket de 1.400 € queda
   **por debajo del coste**. Se fija «copas por invitado y hora» en celda y se recalcula en cascada `B13:D13`, `E13`, `E20`, el break-even y el ticket medio de
   referencia. (DOM-02.)
3. **La columna `% s/VENTAS` sobre el año que dice el rótulo** (B-γ): hoy `E13:E20` son del año 1 y `E34`, `E36`, `E40` del año 3 —`E34='11,6 %'` sale de
   18.220/157.500 cuando sobre el año 1 es el **26,0 %**—. Pasa a `='B34/$B$10'` (TEC-03).
4. **Fiscalidad coherente con la forma jurídica**: `PyG!A39` aplica un IS del 25 % a un modelo que todo el resto del kit define como **autónomo en IRPF**
   (`Inversion Inicial!A6` da de alta un autónomo, `A7` marca la SL como opcional, `Personal Freelance!F5` dice que el fundador «ya cobra como autónomo»). Se
   sustituye por dos filas alternativas —«si autónomo/IRPF (por tramos)» y «si SL/IS»— y se documenta a partir de qué facturación conviene el salto (DOM-21).
   La cuota de autónomo del año 1 baja de 3.960 € a los **1.920 €** que implican las notas del propio kit (80 €/mes + gestoría 80 €/mes), con recálculo en
   cascada de `B34`, `B36`, `B38`, `B39`, `B40` y del break-even (TEC-14). En B-δ, los 80 €/mes de tarifa plana están aplicados **también en los años 2 y 3**
   (`'Proyección 3 años'!C15`, `D15`), donde ya no procede.
5. **Personal freelance con una sola tarifa y con el encuadramiento decidido**: `C6:D9` («EVENTO 4H» y «EVENTO 6H») son en realidad **5 h y 7,5 h** —factor 1,25
   exacto en las 8 celdas— y se corrigen o se renombran con el montaje declarado (TEC-05); `F13` y `F16` («coste por evento tipo») no cuadran con la tabla que
   tienen tres filas más arriba y pasan a fórmula (TEC-16); el DOCX da **tres rangos incompatibles** para el mismo puesto (22 €/h en el Excel, «150-250 € por
   servicio» en el par. 102, «80-120 € por evento de 5 h» en el par. 96) y se unifican citando la celda (DOM-15). Si los runners van por cuenta ajena, entra una
   línea de **SS a cargo de la empresa (33 %)** y otra de PRL en costes fijos (DOM-25).
6. **Ratios de referencia con la unidad correcta**: `Instrucciones!B22 = «169-220 EUR/h»` para un bartender cuyo coste el mismo libro fija en 22 €/h — un error
   de escala de 8-10× en la tabla que el comprador usa para tarificar, propagado además al par. 53 del DOCX. Pasa a «169-220 EUR por servicio (4-6 h)» y se
   revisan de paso `B14:B32` (TEC-15, DOM-11, COM-10).
7. **Amortización sobre el inmovilizado real**: `A37 = «Amortizacion (5 anos sobre 25K)»` cuando el activo amortizable del propio libro suma **21.880 €** y los
   «25K» vienen del total de arranque del catálogo, que incluye stock de bebidas y trámites (TEC-25, DOM-28). En B-δ **no hay ninguna fila de amortización**
   pese a haber 3.790-54.440 € de inversión: se añade.
8. **Hoja nueva `Financiación`** en los 5 (§2.8): origen de fondos, cuadro francés con carencia y vencimiento, y su impacto en el P&L, que hoy no tiene ninguna
   línea de gastos financieros (TEC-21, DOM-19, COM-05).
9. **Hoja nueva `Tesorería Mensual`** en B-γ (B-δ ya tiene `'P&L Año 1'` mensualizado, al que se le añaden cobros con desfase, IVA y saldo acumulado): es el
   negocio **más estacional posible** —el propio fichero documenta «alta: 5-8 eventos mayo-sep + dic» y «baja: 1-3 eventos enero-abril + oct-nov»— y se entrega
   sin previsión mensual, con un fondo de maniobra de 4.000 € que no cubre los 6.073 € de cuatro meses de costes fijos, y con la compra de 4.000 € de stock de
   licor planificada en el mes 2, **antes de tener un solo evento cerrado** (DOM-18).
10. **IVA declarado**: `A3` de la hoja de inversión dice que las cifras son netas; `B12` se ajusta al escenario elegido (2.420 € netos con inversión del sujeto
    pasivo si la empresa está en el ROI, o 2.928 € con el 21 % español — hoy pone 2.880 €, que es el **19 % alemán** y no es ninguno de los dos, y esa cifra se
    propaga al checklist y a la landing); las liquidaciones trimestrales van a la hoja de tesorería (DOM-20, COM-32).
11. **Ratios y semáforo** contra la hoja `KPIs` (B-δ), que hoy es una tabla muerta de texto.

### 3.5 Break-even triple

Tres filas, no una: **(a) cobertura de costes fijos** (el número que hoy se publica), **(b) break-even después de amortización** y **(c) break-even incluyendo
una retribución objetivo del fundador**. Medido: coctelería publica 31 eventos y con la amortización de 5.000 €/año del propio P&L son **40**; y su «RESULTADO
NETO» del año 1 (4.635 €) **no es beneficio: es la retribución íntegra del fundador por 50 eventos**, por debajo del SMI, sin que ninguna hoja lo advierta
(DOM-05, DOM-06, TEC-17, COM-06). En B-δ el problema es peor y **contradice a la landing por factores de 2 a 30**: paellero 10,2 eventos/año en el fichero
frente a «18-22 eventos año 1» en la landing; catering **0,46 eventos/mes** en el fichero frente a «**14 eventos/mes** año 1» en la landing; chef-privado
11,4/año. La fila 40 se renombra **«Resultado antes de retribuir al fundador»** (§7-bis.12) y se añade la fila de retribución.

### 3.6 `Mix B2C-B2B` como fuente única del ticket medio

En B-δ la hoja `Mix B2C-B2B` tiene tipologías, ticket y eventos/año, y **nadie la lee**: `'Proyección 3 años'!B7:B8` y `'Break-even'!B6` traen sus propios
tickets tecleados. Medido en paellero: el mix da un ticket B2C ponderado de **921 €** y B2B de **2.408 €**, frente a los **850 €** y **1.850 €** que usa la
proyección (+8 % y +30 %), y unos ingresos de **269.200 €** frente a los 215.050 € del P&L (**+25 %**). Y la hoja no tiene ni una fila de total. Se cablea:
`Ticket B2C = SUMAPRODUCTO(C,D)/SUMA(D)` sobre las filas B2C, ídem B2B, y `'Break-even'!B6` los lee. En B-γ, el mismo defecto medido por el R1: «50 eventos =
70K» no se sostiene con el propio mix, que da **42,8 eventos**, y una de las cuatro líneas de ingreso («catering y extras») no es un evento pero se divide entre
50 (DOM-24). Y las cuatro escalas de precio incompatibles del DOCX (par. 52, 53, 88, 131) pasan a citar esta tabla (DOM-10, COM-28).

### 3.7 Plantilla de proveedores

- **Los que no son proveedores, fuera del recuento**: 11 de las 96 filas del representante B son categorías genéricas sin contacto («Distribuidores HORECA»,
  «Carrocero local especializado», «Fotógrafo bodas local»), 52 no traen precio y 13 no traen web utilizable, mientras la FAQ —**indexada en el `FAQPage`**—
  afirma que «cada proveedor lleva web/contacto, cobertura, precio orientativo, plazo y notas». Se completan o se mueven a un bloque «categorías a resolver en
  tu zona» y **se ajusta el número**. Deduplicar «Bodeboca», que aparece en dos hojas (DOM-29, COM-09).
- **El nombre de la hoja miente en paellero**: la pestaña se llama `'96 proveedores'` y contiene **88** (la landing sí dice 88, ocho veces). Catering y
  chef-privado sí tienen 96. El motor **renombra la pestaña con el número medido** (`NUEVO-09`).
- Hipervínculos e índice (§1.10).

### 3.8 Checklist de línea B

Moldes **C2** (coctelería), **C3** (parrillero) y **C4** (paellero, catering, chef-privado).

- **El contador nunca cuenta** (C2): las 71 casillas vienen con `☐` (U+2610) y las 6 fórmulas buscan `✓` (U+2713), y el libro no tiene hoja de instrucciones ni
  leyenda. Se añade la leyenda bajo el título de cada hoja y el denominador pasa a `=COUNTIF(rango;"✓")+COUNTIF(rango;"☐")`, que **excluye los `N/A`** y permite
  llegar al 100 % (DOM-17, TEC-24, COM-25). Bloque de **resumen global** en la primera hoja con la suma de los 6 contadores.
- **C3 y C4 no tienen nada**: 0 fórmulas, 0 DV, 0 formato condicional. En C4 la columna `OK` existe y está vacía; en C3 ni existe. Reciben el mismo tratamiento
  que C2 (`NUEVO-07`).
- **El subtítulo de catering dice «110 hitos» y la hoja tiene 113** (copiado del de paellero, que sí tiene 110). Se genera desde el recuento (`NUEVO-09`).
- Contenido legal: mismas correcciones de §2.10 (IAE itinerante 677.9, factura electrónica sin fecha inventada, permiso autonómico de alcohol —hoy 400 € y un
  trámite de 1-2 semanas para algo que el §9 del propio plan dice que **no hace falta** en espacio privado, que es el 100 % del modelo—). (DOM-27, DOM-33,
  COM-33, COM-34.)

### 3.9 Demostraciones exigidas (pycel, bloqueantes)

1. Los 10 ejemplos de cada calculadora se reproducen con sus inputs (tolerancia 1 %).
2. Con `C12="Sí"` (con tilde) y con `C12="SI"`, la calculadora devuelve el **mismo** precio que con `"S"` — o la DV lo impide.
3. `Break-even` con y sin amortización difiere, y la fila (c) incluye la retribución.
4. `'Proyección 3 años'` y `'P&L Año 1'` dan el **mismo** total de ingresos del año 1 (hoy difieren en 100 € en paellero).
5. `'Break-even'!B6` == ticket ponderado calculado desde `'Mix B2C-B2B'`.
6. `Financiación` con carencia >= plazo → aviso, no cuota negativa.
7. Ninguna celda con formato de porcentaje contiene un importe en euros, ni al revés.

### 3.10 Defectos que los R1 no podían ver (línea B) — medidos el 2026-08-29

- **`NUEVO-04`** · alta · **En B-δ todas las tasas viven dentro de la fórmula**: `=B7*0.28` ×26, `=B11*0.12`, `=1-0.28-0.05-0.12`, `=850*0.35+1850*0.65`,
  `=B31*0.4`, `=B7*0.95*2`, `=B10*120`, `=B31*0.55`. El food cost está escrito **dos veces en dos hojas distintas** (P&L y Break-even) y el ticket medio del mix
  **tres veces**. Cambiar un supuesto obliga a editar ~30 fórmulas y a acertar en todas.
- **`NUEVO-05`** · alta · **Importes en euros con formato de porcentaje** en las tres calculadoras B-δ: el anticipo se imprime como «48348,0 %». Es la celda que
  el vendedor copia al contrato.
- **`NUEVO-08`** · alta · Los ejemplos de B-δ se desvían de su propia calculadora hasta un **38 % a la baja** (catering #7: 1.950 € publicados frente a ≥2.700 €
  calculados). Mismo daño que el hallazgo estrella de coctelería, en tres productos más.
- **`NUEVO-09`** · media · Recuentos que se desmienten solos: pestaña `'96 proveedores'` con 88 filas (paellero); subtítulo «110 hitos» con 113 filas
  (catering); «**11 entregables**» y «**9 entregables**» en el mismo fichero de landing (paellero 5+1, catering 6+1).
- **`NUEVO-10`** · alta · **El P&L de catering proyecta 603.700 € de facturación en el año 1** (167.200 B2C + 436.500 B2B) con 10.560 € de costes fijos, sin
  plantilla, sin obrador y con una inversión que el propio libro cifra entre 8.520 € y 54.440 €. Además declara «mix B2C 35 % + B2B 65 %» cuando el reparto real
  de sus propias filas es **27,7 % / 72,3 %**. El paellero, con la misma estructura de costes, proyecta 215.050 €. **Una de las dos escalas está mal**; se
  recalibra en el módulo de contenido y se etiqueta como valor de ejemplo (§7-bis.14 heredado).

---

## 4. Documentos — 46 docx (`documentos.py` + `guion_<pid>.py`)

### 4.1 Alcance y punto de partida medido

10 «plan-de-negocio-*.docx» (6.508-6.971 palabras en línea A y en coctelería; **2.440-2.841** en B-δ) + 36 docx de línea B (cartas, catálogos, contratos,
manuales, experiencias, guías; 639-3.955 palabras). **Los 46 en tamaño Carta, con `author='python-docx'` y `title=''`** (DOM-28 → 46 ficheros). **0 caracteres
no latinos** tras el hotfix del 29-ago; el gate permanente es `scripts/productos-digitales/gate-no-latinos.py`, que se corre **antes** de ensamblar y **después**
de maquetar.

### 4.2 El guion, antes del texto: el docx CITA el xlsx, no lo recalcula

**Decisión firmada §7-bis.4: una sola fuente de cifras por producto, el xlsx de supuestos.** `guion_<pid>.py` se escribe **leyendo las celdas del xlsx ya
corregido** (por eso los documentos van después de los xlsx, §9) y produce, por sección, un guion cerrado: título · 4-6 epígrafes · **las cifras exactas que la
sección debe citar, con su celda de origen** · las tablas exigidas con sus columnas · las trampas a evitar.

**Guion por sección del plan de negocio** (las 10 secciones del molde de línea A, que se conservan; en B-δ se amplían de 8 a 10 para igualar la estructura):

| § | sección | cifras que cita (celda) | tablas exigidas | trampas a evitar (id) |
|---|---|---|---|---|
| 1 | Resumen ejecutivo | inversión `1!B46` · facturación `2!B10:D10` · resultado `2!B34:D34` y margen `2!B40` · break-even `3!B15` · payback `6!<fila>` | 1: cifras clave a 3 años | **Prohibido afirmar un resultado positivo si `2!B34` es negativo** (DOM-02: hoy promete 8-12 % donde el Excel da −7,03 %); una sola facturación (COM-02: hoy 350K, 520-620K, 480K y 450-550K en el mismo documento) |
| 2 | Concepto y propuesta de valor | plazas y rotación coherentes con `2!B7` | — | superficie por comensal >= 1,5 m² (DOM-16: hoy 1,0 m², licencia denegable) |
| 3 | Análisis de mercado | — | 1: ticket medio por CCAA · 1: supervivencia a 1/3/5 años | **toda cifra con entidad emisora y año, o fuera** (DOM-22: «145.000 M€ = 6,5 % del PIB» es imposible; DOM-21: la landing promete tres datos que no existen; COM-07: 81K en la web contra 210K en el fichero; COM-29: 1.650 € y 1.800 € de gasto per cápita en el mismo documento) |
| 4 | Análisis competitivo | — | 1: competidores | porcentajes sin fuente (DOM-36) |
| 5 | Plan de marketing y captación | presupuesto `1!B35:B37` | 1: canales y coste | una sola escala de precios (COM-28, DOM-10) |
| 6 | Plan de operaciones | equipamiento `1!B14:B33` | 1: equipamiento con importe | el Word no puede describir un equipamiento 2-3× más caro que el presupuestado (DOM-20) |
| 7 | Estructura organizativa y RRHH | plantilla `5!B13` · coste `5!F13` · ratio `2!B39` | 1: puestos, bruto, SS 33 %, coste año | **convenio PROVINCIAL, nunca estatal** (DOM-24, COM-22); ratio bien calculado (DOM-18, COM-19: hoy dice 35-45 % donde son 49-60 %); una sola plantilla (DOM-31, COM-28: hoy cinco) |
| 8 | Plan financiero | **todas** las de `Supuestos`, `2`, `3`, `4`, `6`, `7` | 3: inversión por bloque · P&L 3 años · escenarios | **el break-even se CITA, no se recalcula** (DOM-07, COM-20, COM-21: hoy tres valores y uno calculado a 365 días); alquiler = 8-10 % de la facturación bien dividido (DOM-06, COM-05: hoy 800-1.000 €/mes donde son 2.333-2.917); fondo de maniobra con los meses reales (DOM-12) |
| 9 | Aspectos legales y licencias | — | 1: trámites, plazo y coste | manipulador, RGSEAA, Crea y Crece, cuota de autónomo, factura electrónica: §2.10 (DOM-08, DOM-09, DOM-13, DOM-25, COM-08, COM-11) |
| 10 | Conclusiones y plan de acción | payback `6!<fila>` · cronograma | 1: hitos por mes | un solo cronograma (DOM-23) y un solo payback (DOM-17: hoy cinco horizontes, el mejor 4× optimista) |

**Presupuesto de palabras**: 6.500-7.000 por plan de negocio en los 10 (los B-δ suben ×2,5-2,8 desde sus 2.440-2.841 actuales), **con `Heading 1` en las 10
secciones** —hoy los 21 docx de B-δ tienen **0 estilos de encabezado**— y **>= 8 tablas**, donde hoy los planes de línea A tienen **0 tablas** y los de B-δ entre
2 y 7.

### 4.3 Pipeline `bridge.py` → Markdown → DOCX

1. **Texto, sección a sección, con `bridge.py`. Nunca redactado por Claude** (regla capital). En este Mac el routing está desactualizado, así que la invocación
   es **siempre**:
   `python3 /Users/johnguerrero/chefbusiness-ai/bridge.py --task content --domain aichef --lang es --model ~deepseek/deepseek-v4-flash-latest --max-tokens 8192
   --prompt "<guion de la sección>" --output <sec_NN.txt>`
   El `--model` y el `--max-tokens` **no son opcionales**: el bridge del Mac enruta `content` a `deepseek-v4-pro` (el snapshot que causó las inyecciones CJK) y
   trae `--max-tokens` por defecto en 4096.
2. **Ensamblado a un `.md` por documento**: portada · índice · secciones con `##`, epígrafes con `###`, **tablas Markdown reales**, y `---` antes de cada
   sección.
3. **Gate de idioma ANTES de maquetar**: `gate-no-latinos.py` sobre el `.md`. Aborta con el fragmento de contexto.
4. **Gate de erratas del ensamblador**, que es donde se absorben las **17 erratas anotadas y no tocadas** por el hotfix del 29-ago y las del R1: coma sin
   espacio (`re.sub(r',(?=[A-Za-zÁÉÍÓÚÑáéíóúñ])', ', ')`, 29 casos sólo en la §7 del representante A, DOM-29/COM-27), **palabras fundidas** (minúscula seguida
   de mayúscula intrapalabra o tokens de más de 18 caracteres: «ubicacionesprime», «captandoclientela», «productosno», «equipmentaje», «gestoríasupone»,
   «enlacesmatrimoniales»), **lista negra de restos de otros idiomas** («attentive», «average», «affecting», «survive», «investimento», «practise», «soften
   opening», «compared to», «complemented by», «erforderida», «lokasi», «differentiates», «Nutrition» por Nutrición, «horno de convención» por convección,
   «mudança»), y **años caducos** a menos de 90 caracteres de lenguaje de precios (el gate `valida()` de `fase8c-libreria-assemble.py`, con su ventana, para no
   tumbar un año legítimo). (DOM-36, COM-26.)
5. **Maquetado** con el patrón de `kit-escandallos-v2_0/bono_guia.py`: `parsear()` → `sanear_bloques()` → `restos_no_winansi()` → `construir_docx()`
   (python-docx, con `add_table` de verdad y `Heading 1/2`), **en A4**, con pie «Versión 2.0 · agosto 2026 · aichef.pro/<pid>», bio anclada y
   `core_properties.author='AI Chef Pro'` + `title` poblado.

### 4.4 Los 36 docx de línea B

1. **`carta-15-cocktails-tematicos.docx` y sus tres gemelas** (12 cortes de carne, 12 paellas, 12 menús) — **el fallo más caro del catálogo**. Los 45 bloques de
   «ESCALADO POR INVITADOS» entregan **exactamente el 50 %** de lo que exige la receta de la propia carta: se multiplicó por invitados en vez de por cócteles,
   pese a que la cabecera dice «asumiendo 2 cocktails/persona» y la fila rotula «(100 cocktails)». El propio French 75 se autorrefuta: su consejo dice «una
   botella de 75 cl rinde 12 cocktails» (100 → 8,3 botellas) y su escalado dice «Cava: 4 botellas». **Quien compre según la tabla se planta en una boda de 100
   invitados con la mitad del alcohol.** Se recalcula `cantidad = ml_receta × invitados × cócteles_por_persona` **desde la tabla de ingredientes del mismo
   documento** y se añade un gate que compruebe cada línea contra su receta antes de publicar. **Verificar el mismo cálculo en las cartas de parrillero,
   paellero, catering y chef-privado**, que comparten generador. (DOM-01, COM-01.)
2. **Catálogos de equipamiento** — precios coherentes con la inversión del plan (§7-bis.3): la máquina de hielo está presupuestada en 800 € en el Excel para una
   capacidad que el catálogo tarifa en 1.800-4.500 €, y el equipo que el propio catálogo recomienda (24 kg/día) **incumple el mínimo de 40-60 kg/día que él
   mismo fija dos páginas antes** (DOM-14); el hielo tiene tres costes distintos en el kit y la promesa de «amortiza en 6-12 meses» sale a **36-50 meses** con
   las cifras del propio plan (DOM-32); la portada promete «12 productos reales con SKU» y hay 13 fichas (18 productos contando variantes), **ninguna con SKU**,
   4 sin precio, y el resumen económico tarifa 4 partidas que el catálogo nunca investiga (DOM-30, COM-11); el enlace de la ficha de Riedel apunta a Schott
   Zwiesel (COM-12); y el precio «bruto» aplica el **IVA alemán del 19 %** a una compra que hará una empresa española (COM-32). **Los enlaces se verifican
   buscando el nombre de la marca dentro del HTML, no por código de estado** (`CLAUDE.md`, gate de CTA a Pickaxe).
3. **Contratos** — cláusulas válidas frente a consumidor (§7-bis.3): la cláusula de cancelación cobra el **100 %** al cliente que cancela a 29 días mientras el
   prestador que cancela sin causa paga el **20 %**, con el 60 % de la facturación en bodas de particulares (arts. 85-87 TRLGDCU); la sumisión expresa de fuero
   es **nula** frente a consumidor (art. 90.2 TRLGDCU y art. 54.2 LEC). Se escalona (30 % >60 días, 50 % 30-60, 75 % <30, 100 % en 72 h), se simetriza con una
   indemnización cuantificada y se sustituye el fuero por un doble régimen (domicilio del consumidor en B2C, sumisión pactada sólo en B2B). Se alinea el
   calendario de cobro con el que recomienda el resto del kit (30-50 % en firma + resto 7 días antes; hoy el contrato deja un 20 % **después** del evento) y el
   exceso de invitados se factura a **precio**, no «al coste». (DOM-12, DOM-31, COM-14, COM-35.)
4. **Catálogos de experiencias** — el «pricing sugerido» de las 10 experiencias es «+X % sobre paquete estándar» y **el paquete estándar no está definido en
   ningún sitio del kit**, con cuatro bases candidatas que difieren hasta 8× (COM-24). Se fija la base citando la celda del Excel y se traduce cada +X % a un
   euro concreto. Se aplican `Heading 1` a los 10 títulos (el documento usa `Normal` en sus 156 párrafos, DOM-35) y se sustituyen las «pajitas plástico
   colores», prohibidas en España y contradictorias con el posicionamiento eco del propio kit.
5. **Manuales técnicos y guías de sistemas** (B-δ) — 884-1.502 palabras para un «manual técnico». Presupuesto mínimo **2.500 palabras y >= 3 tablas**, con el
   guion de §4.2 adaptado.

### 4.5 Gates de los documentos (bloqueantes)

1. **No latinos**: `gate-no-latinos.py` = 0 en el `.md` y en los 46 `.docx`.
2. **Erratas**: 0 comas sin espacio, 0 palabras fundidas, 0 términos de la lista negra, 0 años caducos en ventana de precios.
3. **Cifras**: **toda cifra de facturación, inversión, break-even, plantilla, ticket, payback y fondo de maniobra que aparezca en el docx coincide con la celda
   del xlsx** — comparadas por extracción, no a ojo. Es el gate que cierra COM-02, DOM-07, DOM-19, DOM-31, COM-21 y DOM-07/COM-06/COM-30 del rep. B.
4. **Estructura**: >= 10 `Heading 1` y >= 8 tablas en los 10 planes de negocio; >= 2.500 palabras y >= 3 tablas en los manuales.
5. **Referencias cruzadas**: **todo nombre de fichero citado dentro de un entregable existe en `astro-site/public/dl/<pid>/`** — hoy el ANEXO I del contrato
   remite a `carta-15-cocktails-tematicos-cocteleria-eventos.docx`, que no existe, y la lista de anexos anuncia dos **PDF** que se entregan en DOCX y olvida la
   plantilla de 96 proveedores (DOM-36, COM-15, COM-22).
6. **Metadata y formato**: `author='AI Chef Pro'`, `title` no vacío y **A4** en los 46.
7. **Enlaces externos**: 200 **y** el nombre de la marca presente en el HTML (COM-12).

---

## 5. Integración — landing, dashboard, changelog, emails, FAQ y JSON-LD (`integracion`, sonnet)

### 5.1 Superficies por producto (censadas 2026-08-29)

`astro-site/src/data/productos/planes/<pid>.ts` (292-314 líneas, la que sirve producción) · `src/components/<pid>/` (10 carpetas: `HeroSection`, `WhySection`,
`ContentGrid`, `BonusSection`, `FaqAccordion`, `BuyBox`, `CtaFinal`, `TestimonialsSection`) · `src/pages/<Pascal>.tsx`, `<Pascal>AccessGate.tsx`,
`<Pascal>Dashboard.tsx` · `src/data/productos-changelog.ts:932-1096` · `src/data/productos-digitales-config.ts` (`emailBody`) ·
`netlify/functions/{verify-purchase,resend-access,get-download-urls}.ts`. **Los nombres de fichero y las claves de descarga NO cambian** (§7-bis.1): viajan en
emails ya enviados.

### 5.2 Las cifras se escriben DESPUÉS de medirlas

Tabla de promesas cuantitativas que el gate cruza contra el fichero, con lo medido hoy:

| promesa | dónde | medido | acción |
|---|---|---|---|
| «fórmulas», «se recalcula automáticamente» | las 10 landings (1-5 veces), dashboards, FAQ, y un **testimonio firmado** | falso en 6 de 10 | queda **cierto** al cablear (§1.3); si un producto se quedara sin cablear, se retira la frase |
| «plan de financiación / formato ICO» | las 10 landings + 16 componentes SPA | **0 hojas de financiación** en 30 xlsx | queda cierto con §2.8 / §3.4.8 |
| «50+ trámites» | rep. A, 9 sitios | **exactamente 50** (51 filas contando el encabezado) | se amplía el checklist con los trámites de §2.10 y **el número se escribe tras contar** |
| «65+ / 63 / 60+ / 59 trámites» | cafetería, tapas-bar, panadería, food-truck | 69 / 68 / 62 / 63 | se recuentan y se escriben |
| «80-120 ítems» | parrillero | 93 | **correcto**; no se toca (un censo es una hipótesis: comprobado antes de reportar) |
| «96 proveedores» | pestaña de paellero | **88** | se renombra la pestaña; la landing ya dice 88 |
| «110 hitos» | subtítulo de catering | 113 | se genera desde el recuento |
| «11 entregables» y «9 entregables» | **el mismo** fichero de landing (paellero, catering) | 11 ficheros | una sola cifra |
| «Inversión 18-35K EUR» | rep. B, 6 sitios | **40.030 €** en el Excel y **25.580 €** en el catálogo | se elige la del Excel y se propaga a landing, dashboard, schema y docx |
| inversión de B-δ | landing, docx y `Resumen!B/C/D` | paellero 3.500-25.000 (landing) vs **3.790 / 9.670 / 23.110** (xlsx) vs «8.500-12.000 recomendada» (docx); catering 5.500-35.000 (landing) vs **8.520 / 21.410 / 54.440** (xlsx) vs «11.500-16.000» (docx) | una sola cifra, la del xlsx |
| «break-even 18-22 eventos» / «14 eventos/mes» | paellero, catering | **10,2/año** y **0,46/mes** | se publica el break-even **después de amortización y retribución** (§3.5) |
| «81K+ restaurantes activos» | rep. A, 4 sitios | el propio docx dice 355.000 / 210.000 | una sola fuente (Hostelería de España / INE) con año |
| «SKU reales» | rep. B, landing y dashboard | **0 SKU** | se añaden las referencias o se cambia el claim |
| «Bourbon Tasting» | rep. B, landing y dashboard | el fichero la llama «Vintage Bourbon Bar» | los 10 nombres, fuente única |

### 5.3 Dashboards y descripciones

La tarjeta del dashboard del rep. A describe el Word con un índice **que no es el suyo**: inventa «descripción del negocio» y «plan de financiación» y omite
«Análisis Competitivo» y «Aspectos Legales», que son dos de las secciones más vendibles (COM-24). Se reescribe con los 10 títulos reales, y **el gate compara la
descripción de la tarjeta contra los `Heading 1` del docx**. Igual con los puestos de personal que enumera la landing y que no existen en la hoja `Personal`
(«jefe de sala» cuando el puesto se llama «Camarero jefe»; plurales donde hay una sola persona; y el «Gerente/Propietario», la partida más cara, sin mencionar)
(TEC-27).

### 5.4 Bonus que no son bonus

Los «BONUS valorados en €38» del rep. A son **dos de las nueve tarjetas del grid**, con la descripción palabra por palabra; el BONUS 2 no existe como
entregable: son siete líneas de la hoja `Instrucciones` (TEC-24, COM-15). En el rep. B, los «BONUS de €68» son dos de los 9 entregables ya contados, y el
subtítulo dice «además del plan financiero y los 7 entregables principales», que suma 10 sobre 9 (COM-13). Y el BONUS 1 se vende diciendo que «sustituye una
asesoría jurídica de 200-400 EUR» cuando **el propio fichero, en su primera página, dice lo contrario** (COM-07). Se reformulan como «incluido» o se mueven
fuera del grid, y se retira la equivalencia en euros con una asesoría.

### 5.5 Changelog y emails

`productos-changelog.ts` pasa a v2.0 en los 10 con el **recuento correcto** (3 ficheros en línea A; 9 u 11 en línea B) y con el detalle de lo que cambia. El
`emailBody` de `productos-digitales-config.ts` adopta la fórmula del tapas-bar («documento DOCX completo, 10 secciones») en los 10, con las cifras medidas.
(DOM-27, COM-18, COM-16.)

### 5.6 FAQ y JSON-LD

Las FAQ que afirman lo que el fichero no hace («las fórmulas se recalculan automáticamente» ×2 casi idénticas en el rep. A; «cada proveedor lleva… precio») se
reescriben con lo que el fichero hace después de la v2.0. `aggregateRating`, `reviews`, testimonios y anclas de precio **no se tocan** (§7-bis.6, §7.3).

---

## 6. Descartado, con motivo

1. **Reescribir los 76 ficheros desde cero con generadores nuevos.** No hay generador que recuperar (§ Decisión) y reescribir destruiría contenido correcto que
   costó dinero producir: 88-96 filas de proveedores reales con web y cobertura, 110 hitos de checklist, 15 recetas de cóctel con escandallo. El post-proceso
   conserva y corrige.
2. **Fusionar el plan financiero y la calculadora en un solo libro** (línea B). Sus claves de descarga viajan en emails enviados (§7-bis.1).
3. **Crear un fichero nuevo «Plan de Financiación»**. §7-bis.1 lo prohíbe salvo que la landing lo prometa como fichero — y no lo promete como fichero, sino como
   contenido. Va como **hoja** dentro del plan financiero.
4. **Recalcular a mano las cifras del docx.** Prohibido por §7-bis.4: el docx se regenera desde el guion que lee el xlsx. Un parche manual reintroduce el
   problema en la siguiente edición.
5. **Redactar prosa con Claude.** Regla capital: `bridge.py`. Claude escribe el guion, no el texto.
6. **Tocar `aggregateRating`, reseñas, testimonios y anclas de precio.** Decisión de John (§7.3).
7. **Un barrido «automático» de acentos con diccionario genérico.** Cazaría «campana extractora» como errata. Se usa lista cerrada con excepciones (§1.7).
8. **Verificar en navegador o con build local.** Restricción térmica; la verificación es por `curl` y por gate, como en el resto de la familia.

---

## 7. Dudas para el orquestador · para John

### 7.1 Dudas para el orquestador (bloquean tandas concretas, no el arranque)

1. **Cuando el caso base corregido deja de ser viable, ¿se recorta la plantilla o se sube el volumen?** Los cinco planes de línea A pasan a pérdidas al enlazar
   el personal real (§2.3.1). El criterio por defecto de esta SPEC es **recortar la plantilla hasta cumplir el propio semáforo**, porque es lo que hace
   defendible el plan ante un banco; la alternativa (subir cubiertos/ticket) infla la facturación. **Confirmar.**
2. **El P&L de catering (603.700 € en el año 1) y el de paellero (215.050 €) no pueden ser los dos correctos con la misma estructura de costes** (`NUEVO-10`).
   ¿Se recalibra catering a la baja o se le añade la estructura (obrador, plantilla, cámara) que 600 k€ exigen — con el consiguiente cambio de inversión y de
   landing?
3. **Presupuesto de palabras de los planes de negocio de B-δ**: esta SPEC propone subirlos de 2.440-2.841 a 6.500-7.000 para igualar a la línea A. Son ~12.000
   palabras nuevas por `bridge.py` en 3 productos. **Confirmar el gasto** (es barato, pero es una decisión de alcance).
4. **`bridge.py`: Mac o VPS.** El del Mac está desactualizado (`reference_bridge-py-mac-desactualizado.md`): sin `--strict-lang`, `--max-tokens` 4096 por
   defecto y `content` → `deepseek-v4-pro`. Esta SPEC asume Mac con `--model` y `--max-tokens` explícitos y el gate en el ensamblador. Si se ejecuta en el VPS,
   añadir `--strict-lang` y el gate sigue igual.
5. **Los 4 checklists de línea B sin contador (C3, C4)**: ¿se les añade la columna `OK` con DV (cambia la estructura visible del fichero que ya descargaron los
   compradores) o sólo la leyenda? Recomendación: **añadirla** — es una columna vacía que hoy no sirve para nada en C4 y que en C3 ni existe pese a que la
   instrucción la nombra.

### 7.2 Para John (no se toca en la v2.0; queda descrito el riesgo)

1. **`aggregateRating` y `reviews` en el JSON-LD de los 10**: 4,9/5 con 8 reseñas y hasta 3 `Review` con nombre y apellidos, **sin ningún sistema de reseñas
   detrás**. Riesgo doble: prácticas comerciales desleales (Directiva UE 2019/2161, arts. 20-21 TRLGDCU, que exige informar de cómo se verifica que las reseñas
   son de compradores reales) y acción manual de Google por *structured data spam*. (COM-10, COM-20.)
2. **Testimonios que describen funcionalidades inexistentes**: el de «Fernando Delgado» del rep. A dice «solo cambias las cifras del local» sobre un libro con
   **0 fórmulas**. Con la v2.0 la afirmación pasa a ser **cierta**, así que el riesgo desaparece solo — pero el testimonio sigue sin ser de un comprador
   verificable.
3. **Anclas de precio permanentes**: `€120 → €35` (−71 %), `€165 → €55` (−67 %) y `€165 → €45` (−73 %) con «Precio especial de lanzamiento. Sube pronto» en
   productos vivos desde agosto y `priceValidUntil` al 31-12-2026. El art. 20.4 TRLGDCU (Directiva Ómnibus) exige que el precio anterior anunciado sea el más
   bajo aplicado en los 30 días previos. **No hay ningún Payment Link ni env var con esos importes.** (COM-16, COM-21.)
4. **Cross-sell a `chefbusiness.co` dentro de los docx** con cuatro precios escritos a mano. La marca es deliberada
   (`feedback_marca-chefbusiness-en-productos-aicp-es-deliberada.md`); lo que la v2.0 sí quita son los **importes**, que quedan congelados en ficheros ya
   descargados (§1.9).
5. **`ingredientsindex.pro` con el TLS roto** aparece en bloques de marcas hermanas del grupo. No se toca aquí; se recuerda porque cualquier enlace del catálogo
   que apunte ahí lleva a un aviso de seguridad.

---

## 7-bis. Decisiones del orquestador ya tomadas (no se reabren al construir)

**Las 8 firmadas** (literales del encargo, y aplicadas arriba):

1. **Mismos ficheros y nombres.** Se pueden **añadir hojas** dentro de un libro; no se crean ficheros nuevos salvo que la landing ya los prometa como fichero.
   Un «Plan de Financiación» prometido como contenido se construye como **hoja** del plan financiero (§2.8, §3.4.8).
2. **El plan financiero de cada plan pasa a ser un MODELO**: inputs en celdas verdes en **una** hoja de supuestos (inversión, ticket, cubiertos/eventos, mix de
   bebida, food cost, personal con **SS 33 %**, alquiler, IVA) y **todas** las demás hojas derivadas por fórmula; **IS 15 % los dos primeros ejercicios con
   beneficio** para entidad de nueva creación y **compensación de BINs**; **sin doble conteo de bebida**; **break-even ÚNICO** que incluye amortización y cuota;
   **fondo de maniobra >= 3 meses** de costes fijos + personal **calculado, no tecleado**; **escenarios que comparten el mismo motor que el P&L**. §2.1-§2.9.
3. **Línea B**: calculadora con **coste por invitado** (no × horas) y **ejemplos que SALEN del motor**; **escalados de carta = nº de cócteles/raciones** (no
   invitados), verificados contra las recetas; catálogos de equipamiento con precios **coherentes con la inversión del plan**; contrato con cláusulas válidas
   frente a consumidor (**cancelación proporcional, no 100 % a 29 días**) y aviso legal coherente con lo que promete la landing. §3.1-§3.3, §4.4.
4. **UNA sola fuente de cifras por producto: el xlsx.** El docx del plan se regenera con `bridge.py` desde un guion que **CITA** las cifras leídas del xlsx.
   Pipeline: leer xlsx → guion con cifras → `bridge.py` por sección → ensamblado con python-docx → gates (no latinos, cifras del docx = cifras del xlsx,
   párrafos/tablas mínimos). **Nada de cifras tecleadas en prosa.** §4.2-§4.5.
5. **Legal VIGENTE y sin inventos**: nada de carnet de manipulador «obligatorio»; RGSEAA **sólo cuando corresponda**; registro sanitario autonómico; cuota de
   autónomo **por tramos vigente, parametrizada y con nota de año**; obligaciones reales de Crea y Crece (factura electrónica) **sin inventar otras**; licencias
   por tipo genérico + nota autonómica/municipal. §2.10, §3.8, §4.2 §9.
6. **Testimonios, `aggregateRating` y anclas de precio: NO se tocan.** Van a §7.2 con el riesgo descrito.
7. **Método de familia**: motor común + módulo por plan; **DOS representantes** (bar-restaurante para A, coctelería para B) con **3 refutadores + corrector +
   ronda 2 + crítico** cada uno; **hermanos por sonnet verificando cada id**; ejecución real **EN SERIE con canario por línea**; capa de producto **honesta con
   cifras medidas**. §9.
8. **Térmica y seguridad**: dry-run a scratchpad, APPLY con variable de entorno y respaldo, **un python cada vez**.

**Decisiones añadidas al escribir esta SPEC** (argumentadas arriba; el constructor tampoco las reabre):

9. **El motor detecta el molde antes de escribir y aborta si no lo reconoce** (§1.1). La familia tiene **cuatro moldes de plan financiero, cuatro de checklist,
   dos de calculadora y dos de plantilla de proveedores**. Dar por hecho el del representante rompe siete de los diez productos. Es el mismo error que costó
   dinero con los «tres moldes de HTML» del blog.
10. **La línea B no recibe la hoja `Supuestos` de la línea A: recibe un bloque `PARÁMETROS`** en `Instrucciones` (B-γ) o en `Resumen` (B-δ). Su driver es el
    evento y su P&L es mensual por estacionalidad; forzarle el molde A obligaría a renombrar hojas que la propia landing enumera.
11. **Ningún número vive dentro de una fórmula ni dentro de un rótulo.** Los rótulos que hoy llevan el porcentaje escrito («Food cost (30% sobre ingresos)»,
    «Amortizacion (5 anos sobre 25K)», «Imprevistos (8%)», «Colchon operativo (3 meses costes fijos)») se **generan con `TEXTO()`** desde la celda del
    parámetro. Es lo que impide que vuelvan a mentir: hoy los cuatro mienten.
12. **En línea B, «RESULTADO NETO» se renombra «Resultado antes de retribuir al fundador»** y se añade la fila de retribución (§3.5). Presentar como beneficio
    lo que es el sueldo del año es lo que hace parecer viable un ejercicio que no lo es.
13. **Las cifras de la capa de producto se escriben DESPUÉS de medir el fichero** y el gate las cruza (§5.2). Ninguna promesa cuantitativa se copia del texto
    anterior. Y un recuento del R1 **no se cree sin remedirlo**: el «80-120 ítems» de parrillero parecía falso y es correcto.
14. **El hotfix de no latinos del 29-ago no se revierte.** Los 7 docx limpiados son la base de partida; sus **17 erratas anotadas** se absorben en el guion y en
    el gate de erratas del ensamblador (§4.3.4), no con parches manuales sobre el fichero viejo.
15. **Los 46 docx pasan a A4 + metadata + versión + bio**, se regeneren o no. Es post-proceso barato sobre un defecto que afecta a los 46 y que un cliente ve al
    abrir Archivo → Propiedades antes de mandarlo al banco.
16. **`pycel` manda sobre la elegancia**: nada de `IRR`, `PMT` ni `COUNTA`; anualidad algebraica y `COUNTIF(r,"<>")`. Toda fórmula nueva se demuestra evaluada
    (§2.11, §3.9) antes de darla por buena.

---

17. **Línea A, personal real (duda 1): se recalibra el CASO BASE hasta que cumpla su propio semáforo, por los dos lados y dentro de rangos con fuente.**
    Plantilla dimensionada por horas de servicio del formato (turnos del cuadrante, no la actual sobredimensionada), con SMI 2026 = 17.094 €/año
    (RD 126/2026) y SS 33 % como suelo; ticket y cubiertos/eventos dentro de rangos del sector citados en la SPEC o en el propio docx original. El
    labour cost del caso base ≤ el techo que declara la hoja de ratios; si con datos defendibles no se llega, el caso base se entrega EN PÉRDIDAS y lo
    dice (la hoja de escenarios muestra qué hace falta para ser viable). Nunca se «cuadra» tocando un porcentaje escondido.
18. **NUEVO-10 (duda 2): catering se recalibra A LA BAJA**, coherente con su inversión, su estructura de costes y su landing; si la landing cita los
    603.700 €, la capa de producto (T10) publica la cifra medida. No se inventa una estructura de obrador que el producto no vende.
19. **Planes de negocio de B-δ (duda 3): SÍ se suben a 6.500-7.000 palabras** con bridge.py (paridad con la línea A; el gate de §9 lo exige a los 10).
20. **bridge.py (duda 4): en el Mac, SIEMPRE con `--model ~deepseek/deepseek-v4-flash-latest --max-tokens 8192`** y el gate `gate-no-latinos.py`
    (más el barrido sobre el Markdown antes de ensamblar); el VPS no interviene en esta familia.
21. **Checklists sin contador, moldes C3/C4 (duda 5): se añade la columna OK con desplegable y contador** (en C4 la columna existe vacía; en C3 la
    instrucción nombra una columna que no existe). Cambia la estructura visible, pero es lo que el fichero ya promete.

## 8. Mapa id → sección (191/191)

Los **93** hallazgos del R1 de `plan-negocio-bar-restaurante` (línea A) + los **98** de `plan-negocio-cocteleria-eventos` (línea B) = **191**, más los 10
`NUEVO-*` del censo de familia. La columna **ámbito** dice si el defecto es de **FAMILIA** (con el número de productos medido entre paréntesis) o sólo del
**REPRESENTANTE**; ninguno se da por replicado sin medirlo en el hermano (§9, tanda T6).

### 8.1 Representante línea A — `plan-negocio-bar-restaurante` (93)

| id | sev | sección | qué | ámbito |
|---|---|---|---|---|
| TEC-01 | alta | §2.3.1 §2.6 | el P&L lee el coste de personal de su propia hoja | **FAMILIA (5)** |
| TEC-02 | alta | §2.5 | escenarios con el mismo motor que el P&L | **FAMILIA (5)** |
| TEC-03 | alta | §1.3 §2 | libro cableado con fórmulas reales | **FAMILIA (5 + coctelería)** |
| TEC-04 | alta | §2.3.2 | food cost sobre comida y bebida sobre bebida | REPRESENTANTE |
| TEC-05 | alta | §2.4 | break-even derivado del P&L | **FAMILIA (5)** |
| TEC-06 | alta | §2.3.4 | IS 15 % de nueva creación + compensación de BIN | **FAMILIA (5 + coctelería)** |
| TEC-07 | alta | §2.2 | fondo de maniobra = 3 × costes fijos mensuales, por fórmula | **FAMILIA (5)** |
| TEC-08 | alta | §2.8 §5.2 | hoja `7. Financiación` con cuadro de amortización | **FAMILIA (10)** |
| TEC-09 | media | §1.4 | ticket con `'#,##0.00 €'` | **FAMILIA (3)** |
| TEC-10 | media | §2.3.5 §2.8 | intereses en el P&L, principal en tesorería | REPRESENTANTE |
| TEC-11 | media | §2.1 §2.7 | IVA declarado, soportado en la inversión y liquidación trimestral | **FAMILIA (10)** |
| TEC-12 | media | §2.3.7 §2.9 | ratios calculados + semáforo contra los umbrales del propio libro | **FAMILIA (5)** |
| TEC-13 | media | §1.5 §1.6 | validaciones de datos y formato condicional | **FAMILIA (30 xlsx)** |
| TEC-14 | media | §1.8 | alto de fila y `wrapText` | **FAMILIA (5)** |
| TEC-15 | media | §1.7 | tildes y eñes, incluidos nombres de hoja | **FAMILIA (10)** |
| TEC-16 | media | §1.4 §2.6 | «Personas» sin formato de euro; fila de 2 personas cuadrada | **FAMILIA (5)** |
| TEC-17 | media | §2.9 | las Instrucciones dicen la verdad al quedar cableado | **FAMILIA (5)** |
| TEC-18 | media | §2.10 | trámites que faltan (RC, hojas de reclamaciones, registro horario, residuos, DDD, música, Ley 1/2025) | **FAMILIA (5)** |
| TEC-19 | media | §2.4 | tabla de sensibilidad al ticket | **FAMILIA (5)** |
| TEC-20 | media | §2.3.6 | amortización sobre el inmovilizado real | **FAMILIA (5)** |
| TEC-21 | baja | §1.4 §2.4 | formatos `General` y separador decimal español | **FAMILIA (5)** |
| TEC-22 | baja | §2.2 | subtotales por bloque de inversión y % sobre el total | **FAMILIA (5)** |
| TEC-23 | baja | §2.3.3 | delivery con `% de ventas` y `% de comisión` | REPRESENTANTE |
| TEC-24 | baja | §5.4 | los dos «BONUS» ya están contados en el grid | **FAMILIA (10)** |
| TEC-25 | baja | §2.10 | epígrafe de IAE acorde al concepto | REPRESENTANTE |
| TEC-26 | baja | §1.7 | errata `Priorizarcexperiencia` | REPRESENTANTE |
| TEC-27 | baja | §5.3 | los puestos de la landing son los de la hoja `Personal` | **FAMILIA (5)** |
| DOM-01 | alta | §2.3.1 §2.6 | (= TEC-01, desde la lente financiera) | **FAMILIA (5)** |
| DOM-02 | alta | §4.2 §1 | el Resumen Ejecutivo no puede afirmar beneficio si el P&L da pérdidas | **FAMILIA (10)** |
| DOM-03 | alta | §4.3 | inyecciones CJK/cirílicas — **cerrado por el hotfix del 29-ago**; queda el gate permanente | **FAMILIA (7 docx)** |
| DOM-04 | alta | §2.3.2 | doble conteo de bebida (COGS real 37,7 % con ratio impreso 30 %) | REPRESENTANTE |
| DOM-05 | alta | §2.5 | escenarios con coste variable declarado y usado | **FAMILIA (5)** |
| DOM-06 | alta | §4.2 §8 | alquiler = 8-10 % de la facturación bien dividido (2.333-2.917 €/mes) | REPRESENTANTE |
| DOM-07 | alta | §2.4 §4.2 §8 | break-even citado, no recalculado, y con los días reales | **FAMILIA (10)** |
| DOM-08 | alta | §2.10 §4.2 §9 | carnet de manipulador derogado (RD 109/2010) | **FAMILIA (5)** |
| DOM-09 | alta | §2.10 §4.2 §9 | RGSEAA no aplica al minorista (RD 191/2011 art. 2.2) | **FAMILIA (5)** |
| DOM-10 | alta | §2.8 §5.2 | plan de financiación inexistente | **FAMILIA (10)** |
| DOM-11 | alta | §2.4 | dos totales de costes fijos en el mismo libro | **FAMILIA (5)** |
| DOM-12 | alta | §2.2 §4.2 | fondo de maniobra infradotado y con tres cifras | **FAMILIA (5)** |
| DOM-13 | alta | §2.9 §2.3.1 | el caso base debe pasar su propio semáforo antes de publicarse | **FAMILIA (5)** |
| DOM-14 | alta | §2.7 §2.8 | faltan tesorería mensual y cuadro de amortización | **FAMILIA (10)** |
| DOM-15 | media | §2.3.4 §2.3.5 | cuota vs intereses, y IS con BIN | **FAMILIA (5)** |
| DOM-16 | media | §4.2 §2 | 1 m²/comensal es inviable y deniega licencia | REPRESENTANTE |
| DOM-17 | media | §2.7 §4.2 §10 | un solo payback, calculado en tesorería | **FAMILIA (10)** |
| DOM-18 | media | §4.2 §7 | ratio de personal bien dividido (49-60 %, no 35-45 %) | **FAMILIA (10)** |
| DOM-19 | media | §2.2 §4.2 | tres desgloses de inversión → uno, el del Excel | **FAMILIA (10)** |
| DOM-20 | media | §4.2 §6 | el Word no describe equipamiento 2-3× más caro que el presupuestado | REPRESENTANTE |
| DOM-21 | media | §4.2 §3 §5.2 | el «Análisis de Mercado» prometido se escribe con tablas y fuentes | **FAMILIA (10)** |
| DOM-22 | media | §4.2 §3 | 145.000 M€ y 6,5 % del PIB no pueden ser ciertos a la vez; fuente por su nombre actual | REPRESENTANTE |
| DOM-23 | media | §2.10 §4.2 §10 | un solo cronograma, el conservador | **FAMILIA (5)** |
| DOM-24 | media | §4.2 §7 §2.6 | convenio **provincial**, no estatal | **FAMILIA (10)** |
| DOM-25 | media | §2.10 §4.2 | cuota de autónomo parametrizada, con nota de año | **FAMILIA (10)** |
| DOM-26 | media | §2.10 | PRL: obligatorio el plan, no el proveedor externo | **FAMILIA (5)** |
| DOM-27 | media | §5.5 | changelog con el recuento correcto | **FAMILIA (10)** |
| DOM-28 | media | §4.5 §1.9 | docx en A4 con metadata, versión y bio | **FAMILIA (46 docx)** |
| DOM-29 | media | §4.3.4 | comas sin espacio y palabras fundidas | **FAMILIA (10)** |
| DOM-30 | media | §2.1 §2.7 | IVA: rótulo «sin IVA» y liquidación | **FAMILIA (10)** |
| DOM-31 | baja | §4.2 §5.2 | una plantilla y un ticket, no cinco y seis | **FAMILIA (10)** |
| DOM-32 | baja | §5.2 §2.10 | «50+ trámites» son 50 | REPRESENTANTE |
| DOM-33 | baja | §2.10 | IAE con los dos epígrafes y la exención de nueva creación | REPRESENTANTE |
| DOM-34 | baja | §2.3.3 §2.3.6 | delivery al 25-30 % del canal, no al 5 % del total; amortización real | **FAMILIA (5)** |
| DOM-35 | baja | §1.9 §4.2 | cross-sell sin precios congelados | **FAMILIA (10)** |
| DOM-36 | baja | §4.3.4 §4.2 | restos de inglés/italiano y datos sin fuente | **FAMILIA (10)** |
| COM-01 | alta | §4.3 | (= DOM-03) cerrado por el hotfix; gate permanente | **FAMILIA (7 docx)** |
| COM-02 | alta | §4.2 §4.5.3 | cuatro facturaciones dentro del mismo Word | **FAMILIA (10)** |
| COM-03 | alta | §2.3.1 | (= TEC-01/DOM-01) | **FAMILIA (5)** |
| COM-04 | alta | §2.8 §5.2 | (= TEC-08/DOM-10) | **FAMILIA (10)** |
| COM-05 | alta | §4.2 §8 | (= DOM-06) | REPRESENTANTE |
| COM-06 | alta | §2.2 | (= TEC-07/DOM-12) | **FAMILIA (5)** |
| COM-07 | alta | §5.2 §4.2 | 81K en la web contra 210K en el fichero | REPRESENTANTE |
| COM-08 | alta | §2.5 | (= TEC-02/DOM-05) | **FAMILIA (5)** |
| COM-09 | alta | §1.3 §5.2 §7.2 | la promesa de fórmulas queda cierta; el testimonio que la cita, también | **FAMILIA (10)** |
| COM-10 | alta | §7.2 | `aggregateRating` sin sistema de reseñas — **no se toca** (John) | **FAMILIA (10)** |
| COM-11 | alta | §2.10 §4.2 §9 | (= DOM-08) + «Nutrition» → «Nutrición» | **FAMILIA (5)** |
| COM-12 | media | §2.3.5 | (= TEC-10/DOM-15) | REPRESENTANTE |
| COM-13 | media | §2.3.4 | (= TEC-06/DOM-15) | **FAMILIA (5)** |
| COM-14 | media | §2.3.2 §2.3.3 | (= TEC-04/DOM-04) + fila «COGS total %» que el gate compara | REPRESENTANTE |
| COM-15 | media | §5.4 | (= TEC-24) | **FAMILIA (10)** |
| COM-16 | media | §7.2 | ancla de precio permanente — **no se toca** (John) | **FAMILIA (10)** |
| COM-17 | media | §5.2 §2.10 | (= DOM-32) el gate cuenta filas y las compara con la landing | **FAMILIA (10)** |
| COM-18 | media | §5.5 | (= DOM-27) | **FAMILIA (10)** |
| COM-19 | media | §4.2 §7 | (= DOM-18) | **FAMILIA (10)** |
| COM-20 | media | §4.2 §8 | (= DOM-07) días de apertura unificados en `Supuestos!B6` | **FAMILIA (10)** |
| COM-21 | media | §2.4 §4.2 §4.5.3 | tres break-even → uno, y el gate lo verifica en el docx | **FAMILIA (10)** |
| COM-22 | media | §4.2 §7 §2.6 | (= DOM-24) | **FAMILIA (10)** |
| COM-23 | media | §1.7 | (= TEC-15) incluidos portada e índice del docx | **FAMILIA (10)** |
| COM-24 | media | §5.3 | la tarjeta del dashboard lista los 10 títulos reales | **FAMILIA (10)** |
| COM-25 | media | §2.4 | (= TEC-19) | **FAMILIA (5)** |
| COM-26 | baja | §4.3.4 | lista negra de anglicismos y de palabras fundidas | **FAMILIA (10)** |
| COM-27 | baja | §4.3.4 §1.7 | erratas tipográficas y concordancia | **FAMILIA (10)** |
| COM-28 | baja | §4.2 §7 | (= DOM-31) plantilla única | **FAMILIA (10)** |
| COM-29 | baja | §4.2 §3 | gasto per cápita con una sola cifra y fuente | REPRESENTANTE |
| COM-30 | baja | §1.9 §4.2 | (= DOM-35) «300+» → «200+» y precios fuera | **FAMILIA (10)** |

### 8.2 Representante línea B — `plan-negocio-cocteleria-eventos` (98)

| id | sev | sección | qué | ámbito |
|---|---|---|---|---|
| TEC-01 | alta | §3.1 | coste de bebida **por invitado**, no × horas | REPRESENTANTE (molde β) |
| TEC-02 | alta | §3.4 §1.3 | plan financiero cableado | **FAMILIA (2: γ)** |
| TEC-03 | alta | §3.4.3 | `% s/VENTAS` sobre el año que dice el rótulo | **FAMILIA (2: γ)** |
| TEC-04 | alta | §3.4.1 §5.2 | el total de inversión y el rango publicitado dicen lo mismo | **FAMILIA (5)** |
| TEC-05 | alta | §3.4.5 | «EVENTO 4H» son 4 h (hoy 5) | REPRESENTANTE |
| TEC-06 | media | §3.3 | los ejemplos salen del motor | **FAMILIA (5)** |
| TEC-07 | media | §1.4 | `'#,##0" €/h"'` con la unidad entrecomillada | **FAMILIA (2: γ)** |
| TEC-08 | media | §1.4 | eventos sin formato de euro | **FAMILIA (5)** |
| TEC-09 | media | §1.8 | alto de fila en celdas combinadas con `wrap` | **FAMILIA (5)** |
| TEC-10 | media | §1.5 §3.1 | DV en los inputs y guardas en las fórmulas | **FAMILIA (4 calculadoras)** |
| TEC-11 | media | §3.1 §5.2 | «Tipo de evento» se conecta o se retira de la promesa | **FAMILIA (2: γ)** |
| TEC-12 | media | §3.4.1 | partidas recurrentes contadas dos veces (1.550 €) | **FAMILIA (2: γ)** |
| TEC-13 | media | §1.7 | tildes en los 4 libros y en los nombres de hoja | **FAMILIA (10)** |
| TEC-14 | media | §3.4.4 | cuota de autónomo del año 1 reconciliada (1.920 €, no 3.960) | **FAMILIA (5)** |
| TEC-15 | media | §3.4.6 | «169-220 EUR/h» → por servicio | **FAMILIA (2: γ)** |
| TEC-16 | media | §3.4.5 | «coste por evento tipo» por fórmula desde la tabla de tarifas | REPRESENTANTE |
| TEC-17 | media | §3.5 | break-even que incluye amortización | **FAMILIA (5)** |
| TEC-18 | media | §3.1 | `PRECIO MÍNIMO` con la rama del wedding planner | **FAMILIA (2: γ)** |
| TEC-19 | baja | §3.1 §1.2 | los tres márgenes objetivo salen a celdas | **FAMILIA (5)** |
| TEC-20 | baja | §3.4.1 | «Imprevistos (8 %)» calculado (hoy 5,82 %) | **FAMILIA (2: γ)** |
| TEC-21 | baja | §3.4.8 §5.2 | hoja `Financiación` | **FAMILIA (10)** |
| TEC-22 | baja | §1.4 | números guardados como texto | **FAMILIA (5)** |
| TEC-23 | baja | §1.10 §3.7 | hipervínculos del índice y rótulos = pestañas; «herbas» → «hierbas» | **FAMILIA (2)** |
| TEC-24 | baja | §3.8 | contador que excluye los `N/A` + resumen global | **FAMILIA (5)** |
| TEC-25 | baja | §3.4.7 | base de amortización real (21.880 €) | **FAMILIA (5)** |
| TEC-26 | baja | §3.4.3 | coste variable diferenciado por escenario | **FAMILIA (2: γ)** |
| DOM-01 | alta | §4.4.1 | **escalados de carta al 50 %** — se recalculan y se verifican contra la receta | **FAMILIA (4 cartas)** |
| DOM-02 | alta | §3.4.2 | consumo por invitado explícito y en celda | **FAMILIA (2: γ)** |
| DOM-03 | alta | §3.4.1 §5.2 | tres inversiones incompatibles → una | **FAMILIA (5)** |
| DOM-04 | alta | §3.3 §3.1 | los ejemplos no validan nada si no salen del motor | **FAMILIA (5)** |
| DOM-05 | alta | §3.5 | break-even sin amortización | **FAMILIA (5)** |
| DOM-06 | alta | §3.5 §3.4.4 | el «resultado neto» es la retribución del fundador | **FAMILIA (5)** |
| DOM-07 | alta | §4.2 §4.5.3 | los escenarios del docx se leen del Excel | **FAMILIA (5)** |
| DOM-08 | alta | §4.3 | inyecciones CJK/cirílicas/árabes — cerrado por el hotfix; gate permanente | **FAMILIA (7 docx)** |
| DOM-09 | alta | §4.2 §3.5 | cuatro break-even en el mismo docx, uno mezclando unidades | **FAMILIA (5)** |
| DOM-10 | alta | §3.6 §4.2 | cuatro escalas de precio → una tabla única citada | **FAMILIA (5)** |
| DOM-11 | alta | §3.4.6 | (= TEC-15) el ratio de referencia con la unidad correcta | **FAMILIA (2: γ)** |
| DOM-12 | alta | §4.4.3 | cláusulas nulas frente a consumidor (cancelación y fuero) | **FAMILIA (5 contratos)** |
| DOM-13 | alta | §4.2 §9 §2.10 | Crea y Crece sin el «depósito de 3.000 €» inventado | **FAMILIA (10)** |
| DOM-14 | alta | §4.4.2 §3.4.1 | máquina de hielo: precio y capacidad coherentes | REPRESENTANTE |
| DOM-15 | alta | §3.4.5 §4.2 | una sola tarifa de freelance en los tres sitios | **FAMILIA (5)** |
| DOM-16 | media | §1.4 | (= TEC-07) formato de fecha accidental | **FAMILIA (2: γ)** |
| DOM-17 | media | §3.8 | el contador cuenta `☐` y `✓`, con leyenda | **FAMILIA (5)** |
| DOM-18 | media | §3.4.9 | hoja de tesorería mensual y fondo de maniobra dimensionado | **FAMILIA (5)** |
| DOM-19 | media | §3.4.8 §5.2 | (= TEC-21) | **FAMILIA (10)** |
| DOM-20 | media | §3.4.10 §4.4.2 | IVA declarado; el 2.880 € del 19 % alemán se corrige | **FAMILIA (2: γ)** |
| DOM-21 | media | §3.4.4 | IRPF por tramos o IS, según la forma jurídica declarada | **FAMILIA (5)** |
| DOM-22 | media | §3.1 §3.4.2 | la comisión del WP se repercute **o** se absorbe, no las dos | **FAMILIA (2: γ)** |
| DOM-23 | media | §3.1 | (= TEC-18) | **FAMILIA (2: γ)** |
| DOM-24 | media | §3.6 | el ticket medio sale del mix, por fórmula | **FAMILIA (5)** |
| DOM-25 | media | §3.4.5 §4.2 | encuadramiento de los runners y su coste de SS | **FAMILIA (5)** |
| DOM-26 | media | §4.2 §3.8 | factura electrónica con el calendario real | **FAMILIA (10)** |
| DOM-27 | media | §3.4.1 §3.8 | el «permiso de venta de alcohol» sólo donde aplica | **FAMILIA (5)** |
| DOM-28 | media | §3.4.7 | (= TEC-25) | **FAMILIA (5)** |
| DOM-29 | media | §3.7 §5.2 | 52 filas sin precio y 13 sin web: se completan o se matiza la FAQ | **FAMILIA (5)** |
| DOM-30 | media | §4.4.2 | «12 productos» son 13/18, 4 sin precio, y 4 partidas sin investigar | **FAMILIA (5 catálogos)** |
| DOM-31 | media | §4.4.3 | calendario de cobro alineado; exceso de invitados a precio, no a coste | **FAMILIA (5 contratos)** |
| DOM-32 | media | §4.4.2 | un solo coste del hielo y una amortización que salga de él | REPRESENTANTE |
| DOM-33 | baja | §3.8 §4.2 | IAE 677.9 como principal para el itinerante | **FAMILIA (5)** |
| DOM-34 | baja | §4.2 §3.4.1 | el leasing es coste fijo; bloque «compra vs leasing» | **FAMILIA (5)** |
| DOM-35 | baja | §4.4.4 §4.5 | `Heading 1` en las 10 experiencias; fuera las pajitas de plástico | **FAMILIA (21 docx sin Heading)** |
| DOM-36 | baja | §4.5.5 | referencias cruzadas rotas (nombre de fichero y extensiones) | **FAMILIA (5)** |
| DOM-37 | baja | §3.1 §1.5 | `C7` y `C8` validados; nada de caídas silenciosas a «premium» | **FAMILIA (4 calculadoras)** |
| COM-01 | alta | §4.4.1 | (= DOM-01) los 45 bloques de escalado | **FAMILIA (4 cartas)** |
| COM-02 | alta | §4.3 | (= DOM-08) | **FAMILIA (7 docx)** |
| COM-03 | alta | §3.1 §3.3 | parámetros de bebida 2,8× por encima del escandallo del propio kit | REPRESENTANTE |
| COM-04 | alta | §3.4.1 §5.2 | (= TEC-04/DOM-03) | **FAMILIA (5)** |
| COM-05 | alta | §3.4 §5.3 | (= TEC-02) y el dashboard deja de prometer fórmulas que no hay | **FAMILIA (2: γ)** |
| COM-06 | alta | §3.5 §4.2 | (= DOM-09) tres break-even, dos en el mismo documento | **FAMILIA (5)** |
| COM-07 | alta | §5.4 §4.4.3 | el bonus deja de decir que «sustituye una asesoría jurídica» | **FAMILIA (5)** |
| COM-08 | alta | §4.2 §9 | (= DOM-13) + cuota de autónomo con una sola cifra | **FAMILIA (10)** |
| COM-09 | media | §3.7 §5.2 | 11 filas que no son proveedores + Bodeboca duplicado | **FAMILIA (5)** |
| COM-10 | media | §3.4.6 | (= TEC-15/DOM-11) | **FAMILIA (2: γ)** |
| COM-11 | media | §4.4.2 §5.2 | «SKU reales»: se añaden o se cambia el claim; 12 → 18 productos | **FAMILIA (5)** |
| COM-12 | media | §4.4.2 §4.5.7 | enlace de Riedel a Schott Zwiesel; verificación por nombre en el HTML | REPRESENTANTE |
| COM-13 | media | §5.4 | «7 entregables + 2 bonus» suma 9, no 10 | **FAMILIA (5)** |
| COM-14 | media | §4.4.3 | (= DOM-31) dos calendarios de cobro | **FAMILIA (5)** |
| COM-15 | media | §4.5.5 | (= DOM-36) el ANEXO I cita un fichero que no existe | **FAMILIA (5)** |
| COM-16 | media | §5.5 | changelog «4 ficheros» en productos de 9 y 11 | **FAMILIA (5)** |
| COM-17 | media | §1.4 | (= TEC-08) eventos en euros | **FAMILIA (5)** |
| COM-18 | media | §1.4 | (= TEC-07/DOM-16) | **FAMILIA (2: γ)** |
| COM-19 | media | §1.5 §3.1 | (= TEC-10/DOM-37) | **FAMILIA (4 calculadoras)** |
| COM-20 | media | §7.2 | `aggregateRating` — **no se toca** (John) | **FAMILIA (10)** |
| COM-21 | media | §7.2 | ancla de 165 € — **no se toca** (John) | **FAMILIA (10)** |
| COM-22 | media | §4.5.5 | los anexos dicen la extensión real y no olvidan la plantilla | **FAMILIA (5)** |
| COM-23 | media | §3.4.1 | (= TEC-20) imprevistos calculados | **FAMILIA (2: γ)** |
| COM-24 | media | §4.4.4 | el «paquete estándar» se define y cada +X % se traduce a euros | **FAMILIA (5)** |
| COM-25 | media | §3.8 | leyenda de la casilla en cada hoja | **FAMILIA (5)** |
| COM-26 | media | §3.4.1 | autónomo y SL son excluyentes: fuera del sumatorio | **FAMILIA (5)** |
| COM-27 | media | §4.2 §3 | las dos cifras de mercado sin fuente, con fuente o fuera | **FAMILIA (10)** |
| COM-28 | media | §3.6 §4.2 | (= DOM-10) dos precios premium en el mismo docx | **FAMILIA (5)** |
| COM-29 | baja | §5.2 | «Bourbon Tasting» ≠ «Vintage Bourbon Bar» | REPRESENTANTE |
| COM-30 | baja | §4.2 §4.5.3 | las proyecciones del docx = las del PyG | **FAMILIA (5)** |
| COM-31 | baja | §3.1 | comisión del WP con un solo valor | **FAMILIA (2: γ)** |
| COM-32 | baja | §4.4.2 §3.4.10 | IVA alemán del 19 % en una compra española | REPRESENTANTE |
| COM-33 | baja | §3.8 §4.2 | factura electrónica sin fecha inventada | **FAMILIA (10)** |
| COM-34 | baja | §3.8 | (= DOM-33) denominación del epígrafe | **FAMILIA (5)** |
| COM-35 | baja | §4.4.3 | (= DOM-12) asimetría de la cláusula de cancelación | **FAMILIA (5 contratos)** |

### 8.3 Hallazgos del censo de familia (10)

| id | sev | sección | qué | ámbito |
|---|---|---|---|---|
| NUEVO-01 | alta | §2.2 | fondo de maniobra de 0,80-1,14 meses con etiqueta «(3 meses)» | FAMILIA (4 de línea A) |
| NUEVO-02 | media | §2.3.6 | base de amortización que incluye circulante, stock e imprevistos | FAMILIA (2: cafetería, panadería) |
| NUEVO-03 | media | §2.4 §2.1 | dos calendarios en el mismo libro (30 días/mes vs 300-320 días/año) | FAMILIA (4 de A-β) |
| NUEVO-04 | alta | §1.2 §3.4 | todas las tasas dentro de la fórmula, el food cost escrito dos veces | FAMILIA (3 de B-δ) |
| NUEVO-05 | alta | §1.4 §3.2 | importes en euros con formato de porcentaje («48348,0 %») | FAMILIA (3 calculadoras B-δ + parrillero) |
| NUEVO-06 | media | §2.5 | `Escenarios` sin estructura homogénea; impuesto aplicado sin fila | FAMILIA (5 de línea A) |
| NUEVO-07 | media | §2.10 §3.8 | checklists sin casilla, sin contador y sin formato condicional | FAMILIA (4: C3 y C4) |
| NUEVO-08 | alta | §3.3 | ejemplos de B-δ desviados hasta un 38 % **a la baja** de su calculadora | FAMILIA (3 de B-δ) |
| NUEVO-09 | media | §3.7 §3.8 §5.2 | recuentos que se desmienten solos (88 en «96», 113 en «110», 9 y 11) | FAMILIA (3 de B-δ) |
| NUEVO-10 | alta | §3.4 §7.1.2 | el P&L de catering proyecta 603.700 € con la estructura de coste de uno de 215.000 € | catering (decisión de John/orquestador) |

**Recuento: 93 + 98 = 191/191 mapeados**, más 10 `NUEVO-*` del censo.

---

## 9. Plan de ejecución

**Reglas transversales del workflow** (`feedback_workflow-agentes-sin-schema-devuelven-string.md`): `agent()` **siempre con `model` explícito** —heredan Fable
por defecto, que es caro— y **siempre con schema**; sin schema devuelve un *string* y 15 hallazgos se contabilizaron como «0». **Nunca recortar los hallazgos
inline** (un `slice(0, 40000)` costó 32 el mismo día): los hallazgos van **por fichero**, y al cerrar cada tanda se **cruzan los ids de entrada contra los
resueltos**. El paquete se **commitea aunque esté a medias** al final de cada tanda: este Mac se ha apagado a las 03:20 y lo no commiteado se pierde.

| tanda | qué | modelo | entregable |
|---|---|---|---|
| **T0 — preparación** | respaldo de los 76 ficheros; `censo-entregables.py --only <pid> --fail --quiet` y `gate-flujo-postpago.py --offline --only <pid>` en los 10 para congelar la línea base; volcado de estructura (hojas, celdas, moldes, recuentos) a `planes-v2_0/censo-base.json`; `gate-no-latinos.py` sobre los 46 docx para certificar el 0 de partida | orquestador | baseline + censo |
| **T1 — motor y grupo A del representante A** | `motor.py` + `grupo_a.py` + `contenido_plan_negocio_bar_restaurante.py` + `main.py`, `--dry-run` a scratchpad | **opus** | paquete que corre en dry-run |
| **T2 — refutación adversarial del representante A** | 3 lentes que intentan REFUTAR: **(a) técnica Excel** (pycel: cada fórmula nueva evaluada con inputs cambiados + las 8 demostraciones de §2.11), **(b) dominio financiero** (¿lo firma un analista de riesgos?, ¿el caso base pasa su propio semáforo?), **(c) coherencia** (¿lo que dice la landing es cierto abriendo el fichero?) | **opus** ×3 | `auditorias/planes-R2-bar-restaurante.json` |
| **T3 — corrección A** | aplica los hallazgos de T2 uno a uno, citando id | **sonnet** | diff + tabla id→fix |
| **T4 — ronda 2 A** | re-verifica SOLO lo corregido y **los ids que T2 dio por buenos sin demostrarlo**; cruza ids de entrada contra resueltos | **sonnet** | `planes-R3-bar-restaurante.json` |
| **T5 — crítico A** | lee el diff completo y firma o devuelve; busca regresiones, casos límite y referencias colgando | **opus** | veredicto |
| **T6 — grupo B del representante B** | `grupo_b.py` + `contenido_plan_negocio_cocteleria_eventos.py`, `--dry-run`; luego **T2'-T5' completas sobre coctelería** (3 refutadores + corrector + ronda 2 + crítico) | **opus** ×3 + **sonnet** ×2 + **opus** | `auditorias/planes-R2/R3-cocteleria.json` + veredicto |
| **T7 — hermanos línea A** | 4 productos, **en serie**: cada uno verifica **cada id del representante A contra su hermano** (no lo da por replicado) + censo propio + `contenido_<pid>.py`, con atención al molde A-β y a `NUEVO-01/02/03/06` | **sonnet** ×4 | 4 módulos + 4 informes |
| **T8 — hermanos línea B** | 4 productos, **en serie**: parrillero (B-γ, molde C3) y los 3 de B-δ (molde de plan financiero, calculadora γ, checklist C4, `NUEVO-04/05/08/09/10`) | **sonnet** ×4 | 4 módulos + 4 informes |
| **T9 — documentos** | `guion_<pid>.py` (opus, leyendo los xlsx **ya corregidos**) → **el orquestador ejecuta `bridge.py`** sección a sección → ensamblado + gate de idioma y de erratas → `documentos.py` (maquetado A4) → gates de §4.5. Los 10 planes de negocio se regeneran; los 36 docx de línea B se corrigen salvo las 4 cartas, que se recalculan | **opus** (guion) + bridge (texto) + **sonnet** (ensamblado y erratas) | 46 docx |
| **T10 — capa de producto** | landing, dashboard, changelog, `emailBody`, FAQ, JSON-LD y `products-catalog.ts` con las **cifras medidas** en T7-T9 | **sonnet** | diff de integración |
| **T11 — cierre** | `inject_cache.py`, verificación `data_only`, idempotencia, los gates de §9 y el de coherencia de cifras; commit y push | orquestador | gate LIVE verde |

**Orden de ejecución real**

1. **Todo en `--dry-run` sobre copias en scratchpad** hasta que T5 y T5' firmen. `astro-site/public/dl/` no se toca en T1-T6.
2. **Canario por línea**: la primera ejecución real de línea A es **un solo fichero** (`plan-financiero-bar-restaurante.xlsx`), que se abre, se verifica con
   `data_only` y se compara con su respaldo; la de línea B, **la calculadora de coctelería**. Si el canario pasa, el resto del representante; si no, se para.
3. **Los 8 hermanos, uno a uno y en serie**, con `PLANES_APPLY=1` y respaldo previo por producto. Entre productos, `istats cpu temp`.
4. **Los documentos van después de los xlsx**, nunca antes: el texto cita las celdas (§7-bis.4), así que primero tienen que ser correctas.
5. **La capa de producto va la última**, con las cifras ya medidas: el recuento de trámites y el break-even se escriben **después** de contarlos y calcularlos.

**Gates que cierran la meta** (ninguno es opcional): `censo-entregables.py --only <pid> --fail --quiet` = 0 defectos en los 10 · `gate-flujo-postpago.py
--offline --only <pid>` = **76/76 ficheros, 0 fallos** · `gate-no-latinos.py` = 0 en los 46 docx y en los 30 xlsx · `inject_cache.py` con `fallos_pycel` = 0 ·
verificación `data_only` sin resultados en `None` · idempotencia (segunda pasada = 0 cambios) · **0 xlsx con 0 fórmulas** · **0 celdas de euros con formato de
porcentaje y 0 recuentos con formato de euro** · **recuento de ítems del checklist >= el anunciado** en cada tarjeta · **los 10 planes de negocio con >= 10
`Heading 1`, >= 8 tablas y >= 6.500 palabras** · **los 46 docx en A4 con `author='AI Chef Pro'`** · y el **gate de coherencia de cifras** cruzando landing,
dashboard, email, changelog, xlsx y docx.

**Lo que NO se hace en local**: builds de Astro, Playwright, navegador. La verificación de producción es por `curl`/gate, como en el resto de la familia.

---

*SPEC redactada el 2026-08-29. Fuentes: `auditorias/plan-negocio-bar-restaurante-R1.json` (93), `auditorias/plan-negocio-cocteleria-eventos-R1.json` (98),
`auditorias/hotfix-no-latinos-docx-2026-08-29.json`, y censo propio de los 76 ficheros de los 10 productos (openpyxl + python-docx, este Mac, con `istats` entre
ejecuciones y un proceso cada vez). Ningún fichero de `astro-site/public/dl/` fue modificado al escribirla.*
