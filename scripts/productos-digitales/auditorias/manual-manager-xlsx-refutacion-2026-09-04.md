# Refutación de los 7 libros de Excel — «Manual del Manager de Restaurante» v1.0

> Fecha: 2026-09-04 · Ámbito: `scripts/productos-digitales/manual-manager/build/*.xlsx` (7 libros, 36 hojas,
> 1.884 fórmulas) + sus 7 `mapa-*.json` · Método: dos lentes en un pase (TÉCNICA y DOMINIO/LEGAL), openpyxl
> (fórmulas y `data_only`), XML crudo de `xl/worksheets/*` para el caché y las `dataValidation`, `curl` a las
> 17 URLs y lectura del texto consolidado del BOE para las normas citadas, y contraste contra
> `manual-manager-SPEC.md`, `auditorias/manual-manager-RESEARCH-2026-09-04.md` §3.3,
> `auditorias/guias-v2-research-sector.json` (MM-01…MM-57) y `guia-food-cost/build/cuadro-de-mando-prime-cost.xlsx`.
>
> **VEREDICTO GLOBAL: CORREGIR.** 5 hallazgos ALTA, 8 MEDIA, 6 BAJA.
> La capa técnica es la más limpia que ha pasado por esta serie: **cero funciones prohibidas, cero constantes
> dentro de fórmulas, cero divisiones sin `IFERROR`, cero celdas verdes con fórmula, cero fórmulas
> desbloqueadas, cero formato condicional cross-hoja, cero caracteres fuera de cp1252 y caché completo**.
> Lo que falla es de DOMINIO: **dos artículos mal citados en notas que llevan el sello «Verificado el
> 04-09-2026»**, los seis puntos legalmente obligatorios del calendario sin norma ni URL, una `dataValidation`
> duplicada sobre la misma celda, y una hoja cuyo número insignia está inflado ~2,7× por un error de unidades.

---

## Veredicto por libro

| # | Libro | Veredicto | Hallazgos |
|---|---|---|---|
| 1 | `cuadro-de-mando-semanal-manager.xlsx` ⭐ | **CORREGIR** | M1, M2, M3 |
| 2 | `matriz-formacion-polivalencia.xlsx` | **CORREGIR** | A4, A5 |
| 3 | `quejas-reclamaciones-resenas.xlsx` | **CORREGIR** | A2, M4, M5 |
| 4 | `seleccion-scorecard-entrevista.xlsx` | **PUBLICABLE** | B2, B3, B5 |
| 5 | `calendario-cumplimiento-legal.xlsx` ⭐ | **CORREGIR** | A1, A3, M7 |
| 6 | `reuniones-acuerdos-plan-90-dias.xlsx` | **CORREGIR** | M6, B1 |
| 7 | `auditoria-interna-servicio.xlsx` | **PUBLICABLE** | B4 |
| — | Transversal (los 7) | **CORREGIR** | M8 |

---

## Resumen ejecutivo

| # | Grav. | Libro | Celda | Qué se rompe |
|---|---|---|---|---|
| A1 | **alta** | calendario | `Estado Normativo!F9` | El RDL 15/2025 aplaza Verifactu por su **disposición final primera**, no por el «art. 3»; y es una de las dos filas sin URL |
| A2 | **alta** | quejas | `Parámetros!F15` | El plazo de 1 mes de Cataluña **no está en el art. 126-9**, está en el **art. 211-4.c)** de la Ley 22/2010 |
| A3 | **alta** | calendario | `Calendario y Vencimientos!I11:L16` | Los 6 puntos marcados «norma estatal = Sí» son los **únicos sin norma, sin URL y sin «Verificado el»** |
| A4 | **alta** | matriz | `Matriz!B14` | **Dos `dataValidation` solapadas** sobre la misma celda (viola ECMA-376; riesgo de diálogo de reparación de Excel) |
| A5 | **alta** | matriz | `Coste de una Baja!B22`, `B28` | 35.385 € de «venta que no se hace» por una baja: el % de caída del TURNO se aplica a la venta del RESTAURANTE, y el total suma ventas con gastos |
| M1 | media | cuadro semanal | `Parámetros!A16-A18` | Se atribuye a CaixaBankLab el tramo «barra o autoservicio», que la D10 de la SPEC prohíbe expresamente |
| M2 | media | cuadro semanal | `Instrucciones!A19` | La tesis «el mes se come la semana mala» sólo se sostiene en 1 de las 4 semanas malas de su propio ejemplo |
| M3 | media | cuadro semanal | `Parámetros!B29`, `B31` | El desglose visible suma 30,65 % contra el 33 % que se usa; falta el AT/EP y el TOTAL no tiene valor |
| M4 | media | quejas | `Parámetros!C15` | «1 mes» de Cataluña modelado como 30 días fijos: en febrero diría «dentro de plazo» dos días después de vencido |
| M5 | media | quejas | `Registro de Quejas!B`,`H` | El SLA se mide en horas con columnas de fecha sin hora: cuantizado a múltiplos de 24 h |
| M6 | media | reuniones | `Actas y Acuerdos!H9:H43` | 15 acuerdos «Cerrado» sin fecha de cierre: «% cerrados en plazo» sale vacío y la lectura nunca se ve |
| M7 | media | calendario | `Estado Normativo!E15:E18` | Las 4 filas libres muestran la fecha de corte con la norma vacía |
| M8 | media | los 7 | — | Las 5 equivalencias LATAM que exige la SPEC §0 no aparecen ni una vez |
| B1 | baja | reuniones | `Plan 90 Días!C10` | Herramienta de origen mal atribuida (calendario en lugar de quejas) |
| B2 | baja | scorecard | `Preguntas…!B31`,`B32` | 2 de las 3 preguntas de «Disponibilidad» no miden disponibilidad |
| B3 | baja | matriz / varios | hoja `Plan de Cross-Training` | Anglicismo con término español ya usado en el mismo libro; «checklist» ×2 |
| B4 | baja | auditoría | `Auditoría!E6`,`G6`,`I6` | Cabecera de 26 ch en columna de 12 con 40 pt de alto: justo 3 líneas, margen cero |
| B5 | baja | scorecard / calendario | `Scorecard!I5` vs `…!I15` | Dos formas de URL distintas para la misma norma (BOE-A-2023-6344) |
| B6 | baja | mapa JSON | `mapa-calendario…json` | Cabecera de la columna F del régimen disciplinario truncada respecto del libro |

---

## ALTA

### A1 · El RDL 15/2025 aplaza Verifactu por su disposición final primera, no por el «art. 3»

- **Libro:** `calendario-cumplimiento-legal.xlsx` · **Hoja:** `Estado Normativo` · **Celdas:** `F9` (y su reflejo `I9`)

**Problema.** `F9` dice «RDL 15/2025, art. 3 (aplazamiento del Reglamento Verifactu)» y `I9` estampa
«Verificado el 04-09-2026 · RDL 15/2025, art. 3…». Es una de las **dos únicas filas del libro sin URL**
(`G9` vacía), así que nada aguas abajo puede desmentirlo.

**Prueba.** Texto consolidado del RD 1007/2023 en el BOE (`BOE-A-2023-24840`, leído el 04-09-2026):

> «Se modifica por la **disposición final 1** del Real Decreto-ley 15/2025, de 2 de diciembre. Ref. BOE-A-2025-24446»

Y el propio RDL (`BOE-A-2025-24446`, título verificado: «…y por el que se modifica el Real Decreto 1007/2023,
de 5 de diciembre») abre así:

> «**Disposición final primera.** Modificación del Real Decreto 1007/2023, de 5 de diciembre. La disposición
> final cuarta queda redactada en los siguientes términos: […] los obligados tributarios a que se refiere el
> **artículo 3.1.a)** deberán tener adaptados los sistemas […] antes del **1 de enero de 2027**. El resto de
> obligados tributarios mencionados en el artículo 3.1 deberán tener operativos los citados sistemas
> informáticos antes del **1 de julio de 2027**.»

Las dos fechas del libro son correctas. Lo que está mal es el precepto: el «art. 3» que aparece en el texto es
el **artículo 3.1.a) del Reglamento** (quién está obligado), no un artículo del RDL. La SPEC §3 arrastra el
mismo error («Verifactu · Aplazado a 2027 (RDL 15/2025, **art. 3**)»), así que el guion lo copiará al manual.

**Fix concreto.**

```
F9 = "RDL 15/2025, de 2 de diciembre, disposición final primera (da nueva redacción a la DF 4.ª del RD 1007/2023)"
G9 = "https://www.boe.es/buscar/act.php?id=BOE-A-2025-24446"
```

`I9` se recompone solo. Añadir la entrada **MM-58** (§ final de este informe) y corregir la fila «Verifactu»
de la tabla del §3 de `manual-manager-SPEC.md`.

---

### A2 · El plazo de un mes de Cataluña no está en el art. 126-9

- **Libro:** `quejas-reclamaciones-resenas.xlsx` · **Hoja:** `Parámetros` · **Celda:** `F15` (nota de la fila que alimenta `C15 = 30`)

**Problema.** `F15` dice: «Verificado el 04-09-2026 · Decret 121/2013 y Codi de consum de Cataluña
(Llei 22/2010), **art. 126-9**: hay que contestar en el plazo máximo de 1 mes desde la presentación de la
hoja · https://www.boe.es/buscar/act.php?id=BOE-A-2010-13115».

**Prueba.** Leído el texto consolidado de `BOE-A-2010-13115` (verificado: «Ley 22/2010, de 20 de julio, del
Código de consumo de Cataluña») el 04-09-2026:

- **Art. 126-9** se titula «**Información sobre los sistemas de reclamación**» y dice: «1. Las personas
  consumidoras tienen derecho a la entrega, cuando lo pidan, de una hoja oficial de reclamación o denuncia…».
  **No contiene ningún plazo de respuesta.**
- El plazo está en el **art. 211-4 «Atención a las personas consumidoras», letra c)**: «…y dar respuesta a las
  quejas y reclamaciones recibidas lo antes posible, en cualquier caso **en el plazo de un mes desde que son
  presentadas**».

El dato (1 mes) es correcto; el artículo, no. Y es precisamente la nota que legitima la única cifra
autonómica que el libro usa en una fórmula (`Reclamaciones Formales!G5` lee `C15`). Un libro cuyo argumento
de venta es «el dato, el artículo, la fuente y el enlace al BOE para que puedas comprobarlo tú» no puede
fallar el artículo.

**Fix concreto.**

```
F15 = "Verificado el 04-09-2026 · Código de consumo de Cataluña (Ley 22/2010), art. 211-4.c): hay que dar
       respuesta a las quejas y reclamaciones en el plazo de un mes desde que son presentadas; el derecho a
       la entrega de la hoja oficial está en el art. 126-9, y el modelo lo regula el Decret 121/2013 ·
       https://www.boe.es/buscar/act.php?id=BOE-A-2010-13115"
```

Revisar también que el cap. 17 del guion no repita «art. 126-9» con el plazo.

---

### A3 · Los seis puntos que SÍ obliga una norma estatal son los únicos sin norma, sin URL y sin verificación

- **Libro:** `calendario-cumplimiento-legal.xlsx` · **Hoja:** `Calendario y Vencimientos`
- **Celdas:** `I11:L11` (ascensor), `I12:L15` (los cuatro de extintores), `I16:L16` (gas) — **vacías las cuatro columnas**

**Problema.** El diferenciador declarado del libro es la columna `E` «¿Lo fija una norma estatal? Sí/No», y la
D12 de la SPEC obliga a que «cada tabla o celda que fije un dato legal lleve nota "Verificado el 04-09-2026 ·
norma · URL"». Medido sobre las 18 filas:

| Columna E | Filas | Con norma + URL + «Verificado el» |
|---|---|---|
| **«Sí»** (7 filas) | 10 registro de jornada · 11 ascensor · 12-15 extintores · 16 gas | **1 de 7** (sólo el registro de jornada) |
| «No» (11 filas) | plagas, campana, termómetros, agua, manipuladores, PRL, ERL, registro retributivo, desperdicio, seguro, TPV | 6 de 11 |

Es decir: **de los seis puntos por los que el lector va a firmar un contrato de mantenimiento, ninguno dice de
qué norma sale la periodicidad**, mientras que los que el libro se esfuerza en marcar como «no obligatorios»
sí traen su cita. Justo al revés de lo que prometen las Instrucciones (`A19`: «CADA FILA LEGAL TRAE SU FUENTE
Y SU ENLACE») y de lo que sostiene el argumento comercial del §2.4 del research.

**Daño.** La afirmación «Sí, lo fija una norma estatal» sin precepto es exactamente el tipo de dato que este
manual dice combatir; y el cap. 11 del guion no tiene celda que citar para los cuatro vencimientos de
extintores, que son los que aparecen en rojo en el ejemplo.

**Fix concreto.** Rellenar las cuatro columnas con las normas que sostienen esas periodicidades (todas
verificables en el BOE y coherentes con los meses ya sembrados en `D11:D16`):

```
fila 11 (ascensor, D=24)        I: "RD 88/2013, ITC AEM-1 (inspecciones periódicas de ascensores)"
fila 12 (titular, D=3)          I: "RD 513/2017, Reglamento de instalaciones de protección contra incendios,
fila 13 (mantenedora, D=12)         Anexo II, tablas I y II"
fila 14 (retimbrado, D=60)      I: "RD 513/2017, Anexo II, tabla II (prueba de presión cada 5 años)"
fila 15 (retirada, D=240)       I: "RD 513/2017, Anexo I, art. 21 (vida útil máxima de 20 años)"
fila 16 (gas, D=60)             I: "RD 919/2006, ITC-ICG 07 (revisión periódica de instalaciones receptoras)"
```

y componer `J` (URL del BOE de cada una), `K` (id `MM-*` si se abre) y `L` con el patrón
«Verificado el 04-09-2026 · <I> · <J>». **Antes de escribirlas, leer el texto consolidado de cada una y
confirmar que la periodicidad es la sembrada** — este informe señala el hueco, no da las periodicidades por
verificadas.

---

### A4 · Dos `dataValidation` solapadas sobre `Matriz!B14`

- **Libro:** `matriz-formacion-polivalencia.xlsx` · **Hoja:** `Matriz` · **Celda:** `B14`

**Problema.** En `xl/worksheets/sheet2.xml` conviven:

```xml
<dataValidation sqref="B12 B13 B14" type="list" errorTitle="Nivel de 0 a 3"
                error="Elige un valor de la lista: 0, 1, 2, 3" …>
<dataValidation sqref="B14"        type="decimal" operator="between" errorTitle="Personas"
                error="Escribe un valor entre 0 y 30." …>
```

`B14` es «Punto único de fallo: personas o menos por estación» = 1, un **recuento de personas**, no un nivel
0-3: se coló en el `sqref` de la lista de niveles que corresponde a `B12` y `B13`.

**Daño.** Dos cosas, y la primera es la grave:

1. ECMA-376 §18.3.1.32 no admite `sqref` solapados entre `dataValidation` de la misma hoja. Excel trata la
   colisión como fichero inconsistente: en el mejor caso aplica una y descarta la otra en silencio; en el
   peor abre el diálogo de «hemos encontrado un problema con parte del contenido… ¿quiere que intentemos
   recuperarlo?» **en un entregable de 55 €**.
2. Aunque Excel la tolere, la lista `0,1,2,3` bloquea el umbral por encima de 3, cuando la propia
   `Instrucciones!A19` invita a subirlo («si en tu casa una estación no está cubierta hasta que hay dos
   personas, sube el umbral de riesgo») y su DV propia declara el rango 0-30.

**Fix concreto.** En el generador, cambiar el `sqref` de la lista de niveles a `"B12 B13"` y dejar `B14` sólo
con su DV decimal. Regenerar y comprobar en el XML que ningún `sqref` de la hoja se solapa. Conviene añadir
al gate de familia una comprobación de solapamiento de `sqref` entre las `dataValidation` de cada hoja: es
barata y aquí ha pasado desapercibida a todos los gates existentes.

---

### A5 · «Perder a una persona cuesta 36.579 €»: el porcentaje del turno aplicado a la venta del restaurante, y ventas sumadas con gastos

- **Libro:** `matriz-formacion-polivalencia.xlsx` · **Hoja:** `Coste de una Baja` · **Celdas:** `B19`, `B20`, `B21`, `B22`, `B28`

**Problema.** El bloque B calcula

```
B22 = B19 * B20 * B21  =  30 días × 0,35 × 3.370 €/día  =  35.385 €
B28 = B15 + B22        =  1.194 € + 35.385 €            =  36.579 €
```

Dos errores encadenados:

1. **La base no es la del porcentaje.** La nota `C20` define `B20` como «Cuánto rinde de menos **el conjunto
   del turno** durante esos días», pero `B21` es «Venta media de un día» del **restaurante entero** —
   `C21` lo dice: «la venta anual dividida entre los 364 días de las 52 semanas» (1.226.661 / 364 = 3.370 ✓,
   coherente con el libro 1). Multiplicando una cosa por la otra, perder a **1 de las 12 personas** de la
   plantilla se lleva por delante el **35 % de toda la facturación durante un mes**: 35.385 € = el **2,9 % de
   la venta anual** del negocio. Ningún manager reconocerá ese orden de magnitud, y el ejemplo es lo primero
   que mira antes de decidir si se fía del libro.
2. **Se suman euros que no son la misma clase de euro.** `A30` lo reconoce («B es venta que no entra, y por
   eso no se apunta como coste») y aun así `B28` los suma y lo llama «IMPACTO ESTIMADO TOTAL». Lo comparable
   es el **margen** que esa venta habría dejado: el propio pack lo calcula en el libro 1
   (`Semana!Q57` → margen tras prime cost 37,2 %), lo que daría ≈ 13.170 € y un total ≈ 14.364 €, **2,5 veces
   menos** que lo que hoy imprime la hoja.

**Fix concreto.** Escalar y convertir, dejando las dos celdas nuevas en verde:

```
B20bis (nueva) "Peso de esa persona en la venta del turno (%)"        → celda verde, ej. 0,10
B20            "Caída del rendimiento del turno mientras no se cubre" → se mantiene
B22 = IFERROR(IF(OR($B$19="",$B$20="",$B$20bis="",$B$21=""),"",$B$19*$B$20*$B$20bis*$B$21),"")
B23 (nueva) "Margen tras prime cost (%)"                              → celda verde, ej. 0,37
B24 (nueva) "MARGEN QUE NO SE GANA (B)" = IFERROR(IF(OR($B$22="",$B$23=""),"",$B$22*$B$23),"")
B28 = IF(COUNT($B$26,$B$27)=0,"",SUM($B$26,$B$27))   con B27 apuntando ya al MARGEN, no a la venta
```

y reescribir `A30` para que diga que lo que se suma al coste directo es el **margen** no ganado. Alternativa
mínima si no se quiere tocar la estructura: dejar `B22` como está pero **renombrar `B28` a «Coste directo (A)
+ venta no realizada (B) — no se suman en la cuenta de resultados»** y bajar `B20` a un valor defendible
para un solo puesto.

---

## MEDIA

### M1 · Se atribuye a CaixaBankLab el tramo «barra o autoservicio», que la D10 prohíbe

`cuadro-de-mando-semanal-manager.xlsx!Parámetros!A16` y `A18`. `A16` dice: «la estructura de costes de
referencia […] sitúa la materia prima en torno al 30 % y el personal en el 30-35 % con servicio en mesa
(**15-25 % en barra o autoservicio**)» y `A18` cierra: «Fuente de la estructura de referencia: CaixaBankLab
con elBullifoundation». La **D10 de la SPEC** es explícita: «CaixaBankLab (2017, rev. 2022) **sin "Sapiens" ni
"barra/autoservicio"**». `A17` sí acota correctamente el 65/55 como criterio de la casa; lo que no está
acotado es el 15-25 %.
**Fix:** sacar el paréntesis de `A16` de la frase atribuida y, si se quiere conservar el segundo escalón,
decir que la horquilla de barra/autoservicio es criterio de la casa, igual que ya se hace con el 55 %.
**Además:** `https://caixabanklab.com/elbullifoundation/es/consumos-beneficios-restaurante/` fue **la única de
las 17 URLs del pack que no respondió** (timeout de 30 s; las otras 16 dan 200). Comprobarla antes de
publicar: es la única fuente no primaria que sostiene el parámetro central del libro insignia.

### M2 · La tesis que justifica el libro sólo se cumple en 1 de las 4 semanas malas de su propio ejemplo

`cuadro-de-mando-semanal-manager.xlsx!Instrucciones!A19`: «en el restaurante de ejemplo, septiembre cierra el
mes en objetivo y sin embargo la semana 36 cerró en el 66,8 % de prime cost».

Recalculado sobre el propio libro y contra `guia-food-cost/build/cuadro-de-mando-prime-cost.xlsx!Mensual`:

| Semana | Lunes | Prime cost | Mes al que cae | Prime cost del mes |
|---|---|---|---|---|
| 7 | 09/02/2026 | 72,00 % | febrero | **68,04 % — fuera de objetivo** |
| 33 | 10/08/2026 | 70,99 % | agosto | **69,90 % — fuera de objetivo** |
| 35 | 24/08/2026 | 72,20 % | agosto | **69,90 % — fuera de objetivo** |
| 36 | **31/08/2026** | 66,80 % | sept. (6 de 7 días) | 60,40 % — en objetivo |

Dos cosas. Primera: la semana 36 se presenta en la hoja `Semana` con «Lunes de la semana = **31/08/2026**»,
y el libro no tiene columna de mes; agrupando por ese lunes, agosto sale al 67,87 % y la frase se cae sola.
Segunda: en **tres de las cuatro** semanas malas el cuadro mensual **ya marca el mes en rojo**, así que
«el promedio del mes se come la semana mala» describe 1 de 4 casos, no la regla.
**Fix:** decir la fecha completa («la semana 36, del 31 de agosto al 6 de septiembre, seis de cuyos siete
días son de septiembre») y cambiar el argumento por el que sí sostienen los datos, que además es mejor: el
mes te dice *que* algo pasó en agosto; la semana te dice *cuál* (33 y 35, con food cost del 38,6 %) y te lo
dice cuatro semanas antes. Es literalmente lo que ya escribe la decisión nº 8 del plan de 90 días.

### M3 · El desglose de cotización visible suma 30,65 % contra el 33 % que se usa, y el TOTAL está vacío

`cuadro-de-mando-semanal-manager.xlsx!Parámetros`. `B22` (verde, editable) = 0,33 es lo que consume toda la
hoja `Semana`. Debajo, `B25:B30` es una tabla bloqueada de referencia: 23,60 + 5,50 + 0,20 + 0,60 + 0,75 =
**30,65 %**. `B29` (AT/EP) está **vacía** y `B31` («TOTAL a cargo de la empresa en hostelería 2026») **también**,
con la cifra sólo en la nota `C31` («32,15 % con contrato indefinido […] y 33,35 % con contrato de duración
determinada»).

Reconstruido: 30,65 + **1,50** = 32,15 % exacto, y 32,15 − 5,50 + 6,70 = 33,35 % exacto. Es decir, el
constructor **sí usó el 1,50 % de la tarifa de la DA 61.ª TRLGSS para el CNAE 56**, pero no lo escribió. El
lector que sume la columna obtiene 30,65 % y no puede reconciliarlo con el 33 % que tiene arriba.
**Fix:** `B29 = 0,015` con nota «Tarifa de primas de la DA 61.ª TRLGSS, CNAE 56 "Servicios de comidas y
bebidas"; comprueba el epígrafe de tu actividad», y `B31 = IFERROR(SUM($B$25:$B$30),"")` → 0,3215, dejando en
`C31` la explicación de que `B22` redondea al 33 % como convención de la casa (D5). Las partidas siguen
bloqueadas; lo editable sigue siendo `B22`.

### M4 · «1 mes» de Cataluña modelado como 30 días fijos

`quejas-reclamaciones-resenas.xlsx!Parámetros!C15 = 30`, y `Reclamaciones Formales!F` cuenta días naturales.
`Reclamaciones Formales!A27` promete: «te avisa antes, nunca después». Para febrero eso no se cumple: una
hoja entregada el 3 de febrero vence el 3 de marzo (**28 días**), y el libro daría «Dentro de plazo: Sí»
hasta el día 30 — dos días **después** de vencido, en la dirección peligrosa. Lo mismo, con un día, en
cualquier entrega de finales de enero.
**Fix:** añadir a la tabla de `Parámetros` una columna «tipo de plazo» (`Días` / `Meses`) y calcular
`G = IF(tipo="Meses", EDATE($B5,n), $B5+n)` restando después contra `E`. `EDATE` ya se usa en el libro 5, así
que está dentro de la convención de familia. Fix mínimo si no se toca la estructura: `C15 = 28` y decirlo en
la nota.

### M5 · El SLA se mide en horas con columnas de fecha sin hora

`quejas-reclamaciones-resenas.xlsx!Registro de Quejas`. `B` y `H` tienen DV `type=date` y formato
`dd/mm/yyyy`; `I5 = ($H5-$B5)*Parámetros!$C$11` multiplica por 24. El resultado sólo puede ser 0, 24, 48, 72…
Con el SLA sembrado para gravedad 3 en **24 h**, una queja grave cerrada a cualquier hora del día siguiente
puntúa exactamente 24 y pasa; y cualquier SLA por debajo de 24 h es directamente inmedible. En los datos
sembrados, `Resumen!E24` y `E26` muestran «0,0 horas medias hasta el cierre», que es cierto pero se lee como
«sin dato».
**Fix:** formato `dd/mm/yyyy hh:mm` en `B` y `H` (la DV `date` acepta el serial con parte decimal), rótulos
«Fecha y hora de la queja» / «Fecha y hora de cierre», y una línea en `Instrucciones` explicándolo. Si se
prefiere no pedir la hora, expresar el SLA en **días** y renombrar `I` a «Días hasta el cierre».

### M6 · El «% cerrados en plazo» del libro de reuniones nunca se enciende

`reuniones-acuerdos-plan-90-dias.xlsx!Actas y Acuerdos`. De 25 acuerdos, 15 están en `G` como «Cerrado» y
**ninguno tiene fecha en `H` («Fecha de cierre real»)**. Consecuencia: `D54` = 0, `D55` («Cerrados EN PLAZO
(%)») sale vacío, y las lecturas «Cerrado en plazo» y «Cerrado fuera de plazo» de la columna `I` —con su
formato condicional ya definido— no aparecen ni una vez en el fichero que compra el cliente. Es una salida
declarada del libro (research §3.3, libro 7: «acuerdos abiertos, **% cerrados en plazo**, acuerdos que vencen
esta semana») y el cap. 20 del guion no tendrá celda que citar.
**Fix:** sembrar `H` en los 15 cerrados, con al menos dos posteriores a `F` para que se vea «Cerrado fuera de
plazo». El resto del libro está bien resuelto — de hecho `D56` ya explica que «"sin dato" no es "cero"», que
es la razón por la que el vacío es correcto; lo que falta es el dato de ejemplo.

### M7 · Las filas libres de `Estado Normativo` muestran la fecha de corte sin norma

`calendario-cumplimiento-legal.xlsx!Estado Normativo!E15:E18`. La fórmula
`=IFERROR(IF($C$5="","",$C$5),"")` no mira si la fila tiene contenido, así que las cuatro filas libres
(numeradas 8-11 en `A`) enseñan **04/09/2026** con `B`, `C`, `D`, `F`, `G`, `H` e `I` vacías. La hoja hermana
del mismo libro no comete el error: `Calendario y Vencimientos!H28:H35` devuelve `""` en sus 8 filas libres.
**Fix:** `E15 = IFERROR(IF(OR($B15="",$C$5=""),"",$C$5),"")`, replicado a `E8:E18`.

### M8 · Las equivalencias LATAM que exige la SPEC no aparecen en ninguno de los 7 libros

La SPEC §0 («Idioma/mercado») obliga a «vocabulario ES con equivalencia LATAM la primera vez
(gerente/encargado ↔ **administrador**; cuadrante ↔ **rol/horario**; arqueo ↔ **corte de caja**; nómina ↔
**planilla**; sala ↔ **salón**)», y la D22 razona por qué: el 60-70 % del volumen medido está en LATAM.
Censado sobre las 36 hojas:

| Término ES | Usos | Equivalencia LATAM | Usos |
|---|---|---|---|
| cuadrante | 4 | rol / horario | **0** |
| arqueo | 2 | corte de caja | **0** |
| nómina | varias | planilla | **0** |
| sala | muchas | salón | **0** |
| gerente / encargado | 2 | administrador | **0** |

Sólo `matriz!Matriz!C18` glosa «Gerente / encargada general (manager)». **Fix:** una glosa entre paréntesis en
la primera aparición de cada término, preferentemente en la hoja `Instrucciones` de cada libro, que es donde
el lector entra. Es una edición de cinco cadenas y no toca ninguna fórmula.

---

## BAJA

- **B1 · `reuniones-acuerdos-plan-90-dias.xlsx!Plan 90 Días!C10`.** La decisión «Contestar por escrito la
  reclamación GI-2026-0463 y revisar por qué se pasó el mes» tiene como herramienta de origen «Calendario de
  cumplimiento legal»; sale del libro de quejas (`Reclamaciones Formales!A6`, 39 días contra 30). El
  «Resumen por herramienta de origen» reparte por eso 4 al calendario y 3 a quejas, cuando es 3 y 4.
  Fix: `C10 = "Quejas, reclamaciones y reseñas"`.
- **B2 · `seleccion-scorecard-entrevista.xlsx!Preguntas por Competencia!B31`, `B32`.** Las preguntas 23
  («¿Qué te hizo dejar el último puesto?») y 24 («¿Qué esperas de este trabajo dentro de un año?») están bajo
  «Disponibilidad para turno partido y fines de semana»: 2 de las 3 preguntas de esa competencia no la miden.
  Fix: reclasificarlas o sustituirlas por dos de disponibilidad real (festivos, temporada alta, cierre de
  noche y apertura del día siguiente).
- **B3 · Anglicismos con término español ya usado en el propio pack.** La hoja `Plan de Cross-Training`
  convive en el mismo libro con «Matriz de formación y polivalencia» (fix: «Plan de formación cruzada» o
  «Plan de polivalencia»); «checklist» ×2 (`auditoria!Instrucciones!A16`,
  `calendario!Instrucciones!A25`). «SLA» (21 usos) y «KPI» (3) quedan justificados: los dos se glosan en su
  primera aparición y son vocabulario del oficio.
- **B4 · `auditoria-interna-servicio.xlsx!Auditoría!E6`, `G6`, `I6`.** «Visita N: puntuación (0-5)», 26
  caracteres en columnas de ancho 12 con `wrap_text` y fila de 40 pt: caben exactamente 3 líneas y no sobra
  nada. Es el único caso del pack sin margen (`Semana!M4`, 42 ch en 17 de ancho, tiene 70 pt). Fix: ancho 14
  o alto 46.
- **B5 · Dos formas de URL para la misma norma.** `seleccion-scorecard-entrevista!Scorecard!I5` usa
  `boe.es/buscar/doc.php?id=BOE-A-2023-6344` y `calendario!Régimen Disciplinario ALEH!I15` usa
  `boe.es/diario_boe/txt.php?id=BOE-A-2023-6344`. Las dos devuelven 200; conviene unificar en la forma
  `buscar/act.php` (texto consolidado), que es la que el propio manual enseña a consultar.
- **B6 · `mapa-calendario-cumplimiento-legal.json`.** La columna `F` de la tabla del régimen disciplinario
  figura como «Sanción posible» y la cabecera del libro es «Sanción posible (escala del ALEH VI)». Sin
  consecuencia funcional (el mapa apunta a la columna, no al rótulo), pero el guion cita por rótulo.

---

## Lo que sí aguanta

**Capa técnica — impecable, y verificada con gate propio, no por lectura:**

- **Cero funciones prohibidas** en las 1.884 fórmulas: ni `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`,
  `LET`, `LAMBDA`, `RANK`, `NETWORKDAYS`, ni matrices dinámicas (`FILTER`, `SORT`, `UNIQUE`, `SEQUENCE`,
  `TEXTJOIN`, `IFS`, `SWITCH`, `MAXIFS`, `MINIFS`). `COUNTA` está resuelto con `COUNTIF(rango,"<>")` y `COUNT`.
- **Cero constantes numéricas dentro de fórmulas** fuera de las estructurales (0, 1, 7, 12, 24, 100 y los
  literales de escala 2-5). Las 24 horas del día viven en `quejas!Parámetros!C11`, **fuera del verde y con la
  nota que explica por qué no es un parámetro del negocio**.
- **Cero divisiones sin `IFERROR`**, y además con guarda de divisor cero explícita (`$T5=""` **y** `$T5=0`).
- **Cero celdas verdes con fórmula · cero fórmulas desbloqueadas · cero celdas verdes bloqueadas** (gate sobre
  las 3.978 celdas con relleno `00E8F5E9`).
- **Caché completo:** 0 fórmulas sin `<v>` en el XML de las 36 hojas. Los `None` que devuelve openpyxl son las
  353 que devuelven `""` — el gotcha `<v/>` de openpyxl 3.1.x, no un caché ausente.
- **Cero formato condicional que referencie otra hoja.** Y donde el umbral vivía en otra hoja, se copia con
  una fórmula y se explica: `matriz!Cobertura por Estación!A9` — «Se copian aquí porque el formato condicional
  no puede leer otra hoja». Es la regla de Sheets aprendida y documentada dentro del producto.
- **Las 40 `dataValidation` con `showErrorMessage`**, ninguna `formula1` por encima de 255 caracteres, y la
  única que apunta a un rango lo hace dentro de su propia hoja (`'Plan 90 Días'!$B$64:$B$70`).
- **Cero caracteres fuera de cp1252** en celdas, notas, listas de validación, títulos de error, prompts y
  nombres de hoja. Ni un emoji en los semáforos: «RIESGO: punto único de fallo…», no «⚠».
- **A4 (`paperSize=9`) y `fitToPage` en las 36 hojas**; `author='AI Chef Pro'` y `subject` con producto y
  versión en los 7 ficheros; protección **sin contraseña** en las 36.
- **Las 7 hojas `Instrucciones` van primero** y las 7 llevan línea de versión
  («Versión 1.0 · septiembre 2026 · aichef.pro/manual-manager-restaurante · info@aichef.pro»), bio anclada de
  John Guerrero, «Celdas verdes = campos editables» y nota de desproteger.
- **Los 7 `mapa-*.json`: 1.202 celdas mapeadas y ninguna apunta a celda vacía ni a fórmula con caché vacía.**
  El guion no puede citar un hueco.

**Prueba de estrés — la pasa, y no sólo en filas vacías:**

- Las **353 fórmulas de filas libres** de los 7 libros devuelven `""`. Ni un `#DIV/0!`, `#VALUE!`, `#REF!` o
  `#N/A` en todo el pack.
- **Filas parcialmente rellenas también:** `Semana!E5` admite sólo ventas de comida
  (`IF(AND($C5="",$D5=""),"",IF($C5="",0,$C5)+…)`); `M5` trata «otros costes de personal» vacío como 0 sin
  romper pero exige el bruto; `U/V/X/Z` blindan el divisor contra `""` **y** contra `0`.
- **Ningún parámetro está escondido:** con cero constantes dentro de fórmulas, cambiar `Parámetros!B22`
  (SS 33 %) recorre `Semana!M5:M56` → `N` → `O` → `Q` → `R` → `E66`; cambiar `Matriz!B12` recorre
  `Cobertura!C6` → `B12:B23` → `F12:F23` y el formato condicional; cambiar `Auditoría!D75:D78` recorre
  `Resumen por Área!D4:D7` → `H` → `Histórico!D3:D4`; cambiar `Calendario!C6/C7` reescribe hasta el TEXTO del
  semáforo (`"< "&TEXT($C$6,"0")&" días"`).
- **«Sin dato» ≠ 0 donde de verdad importa:** `Actas y Acuerdos!D55` sale vacío con la nota «Vacío mientras no
  anotes ninguna fecha de cierre real: "sin dato" no es "cero"».
- **Las medias ponderadas descuentan lo no valorado del denominador** (`--ISNUMBER`) tanto en la auditoría
  (`Resumen por Área!D10:F15`) como en el scorecard (`Scorecard!D23`), y las dos hojas lo explican al lector.

**Capa legal — lo verificado contra el BOE hoy, palabra a palabra:**

- **Art. 9.5 de la Ley 15/2022 citado LITERAL.** `scorecard!Preguntas por Competencia!A5` dice «el empleador
  no podrá preguntar sobre las condiciones de salud del aspirante al puesto»; el texto consolidado
  (`BOE-A-2022-11589`) dice exactamente «5. El empleador no podrá preguntar sobre las condiciones de salud del
  aspirante al puesto», **sin excepciones ni salvedades**. No hay caveat omitido ni añadido.
- **Ley 28/2005 art. 2.2 correcto.** «terraza legal = máximo dos paredes» frente al literal del BOE
  (`BOE-A-2005-21261`): «se entiende por espacio al aire libre todo espacio no cubierto o todo espacio que
  estando cubierto esté rodeado lateralmente por un **máximo de dos paredes, muros o paramentos**».
- **Identidad de las normas comprobada en el BOE:** `BOE-A-2026-3815` = RD 126/2026 del SMI 2026 ✓;
  `BOE-A-2026-7296` = Orden PJC/297/2026 de cotización ✓; `BOE-A-2026-18630` = Resolución de 25-08-2026 de la
  DGT que publica la modificación del ALEH VI ✓; `BOE-A-2010-13115` = Ley 22/2010 del Código de consumo de
  Cataluña ✓. **16 de 17 URLs devuelven 200** (la excepción es CaixaBankLab, M1).
- **Topes de jornada, los diez correctos:** 40 h de promedio en cómputo anual (34.1), 9 h diarias salvo
  distribución irregular pactada (34.3), 12 h entre jornadas (34.3), 1,5 días acumulables en 14 (37.1), los 15
  minutos **con la condición del convenio bien puesta** (34.4), 80 h extra al año con la proporción en jornada
  parcial y la exclusión de las compensadas con descanso (35.2), complementarias pactadas 30 % ampliable al
  60 % y voluntarias 15 % con el mínimo de 10 h semanales (12.5), registro diario y 4 años (34.9) y la
  presunción de jornada completa del 12.4.c).
- **Permisos, con la trampa del parental bien resuelta (D6):** las dos figuras van en filas consecutivas,
  la de 8 semanas **no** retribuida razonada por el art. 45.1.o) y 45.2 (suspensión → exoneración recíproca) y
  la ausencia de prestación, y la de 2 semanas **sí** retribuida por el art. 48.4.c) con la situación
  protegida del art. 177 LGSS. Además el error frecuente marcado como tal: «son 2 días, ampliables en 2 más si
  hay desplazamiento, **NO 5**; el RDL 5/2023 separó el fallecimiento del accidente o enfermedad grave».
  Nacimiento 19 semanas descompuestas 6 + 11 + 2, fuerza mayor computada **por horas**, guarda legal
  identificada como reducción con reducción proporcional de salario, y adaptación con silencio positivo.
- **La columna «¿lo fija una norma estatal?» reparte bien:** 7 «Sí» que son **cuatro familias** (registro de
  jornada, ascensor, gas y los cuatro vencimientos de extintores) y 11 «No» — plagas, campana y conductos,
  termómetros, analítica de agua, formación de manipuladores y de PRL, evaluación de riesgos, registro
  retributivo, desperdicio, seguro y TPV — cada uno con la nota que explica que la ley exige el **resultado**,
  no el calendario. `Instrucciones!A15` lo dice entero y sin ambigüedad. Es el mejor contenido del pack.
- **Lista negra §8: cero apariciones.** Las tres coincidencias del barrido son las refutaciones deliberadas:
  `Parámetros!A33` («el 23,60 % es SOLO contingencias comunes y no debe rotularse coste de la Seguridad Social
  a cargo de la empresa»), `Topes de Jornada!I6` («la reducción a 37,5 horas NO está vigente») y
  `Permisos!B12` (el parental retribuido, correctamente distinguido). Ni Toast, ni Sapiens, ni Linkers, ni
  1.512/2.345, ni el 60 % de cierres, ni el 63,5 %, ni Starter, ni el 5,7 %, ni las consultas V3095-17 /
  V2236-13, ni «carné de manipulador», ni los 1.300 m², ni «Verifactu obliga desde 2026».
- **El plazo de Andalucía se compara en días naturales contra 10 hábiles y está dicho**
  (`Reclamaciones Formales!A27`): avisa antes, nunca después. Diseño conservador y documentado.

**Coherencia del caso modelado — verificada celda a celda, y es notable:**

| Lo que dice una herramienta | Lo que dice la otra |
|---|---|
| Retimbrado de extintores vencido el 09/05/2026, −118 días, «VENCIDO» (`calendario!…!H14`) | Decisión nº 4 del plan: «Contratar el retimbrado de los extintores, **vencido desde mayo**» |
| Reclamación GI-2026-0463: 39 días contra un plazo de 30 → «No» (`quejas!…!I6`) | Decisión nº 5: «Contestar por escrito la reclamación **GI-2026-0463**… por qué se pasó el mes» |
| Exactamente **4** semanas por encima del 65 % (7, 33, 35, 36) | Decisión nº 7: «Analizar **las cuatro semanas** fuera de objetivo del año» |
| Las dos peores son la 33 (70,99 %) y la 35 (72,20 %) | Decisión nº 8: «Ajustar el pedido de la **semana 33 y 35** tipo» |
| «Fríos y entrantes» con **1 sola** persona a nivel ≥2 (P05) → punto único de fallo | Decisiones nº 1 y nº 13: llevar a P06 y luego a P04 a nivel 2 en la partida fría |
| «Aseos y limpieza» única área que empeora, −0,82 pts (`auditoría!Histórico!E15/E16`) | Decisión nº 6: «Recuperar el área de aseos y limpieza, **la única que empeora**» |
| **4** acuerdos «VENCIDO» (`Actas y Acuerdos!D50`) | Decisión nº 9: «Cerrar los **cuatro acuerdos vencidos**» |
| Plantilla de **12** y **24** preguntas del guion | Decisiones nº 16 («las doce personas») y nº 11 («las 24 preguntas») |

- **La misma plantilla y las mismas estaciones en los cuatro libros que las usan:** P01-P12 idénticos en las
  listas de validación de matriz, quejas, reuniones y plan de 90 días; 6 estaciones sembradas sobre una
  capacidad de 30 × 12 sin tocar una fórmula, exactamente como pedía la SPEC §2.2.
- **Coherencia con la Guía Food Cost:** 1.226.661 € de venta anual en el cuadro semanal frente a 1.232.200 €
  en el cuadro mensual de aquel producto (**0,45 %** de diferencia), mismo 33 % de SS, mismo objetivo de
  65 %, y septiembre en objetivo en los dos. Los 3.370 €/día de `Coste de una Baja!B21` salen de dividir esa
  misma venta anual entre 364. El restaurante modelado es uno solo.
- **Los cuadres internos cuadran:** 18 puntos = 7 «Sí» + 11 «No»; 16 con vencimiento = 12 verdes + 3 rojos +
  0 ámbar + 1 vencido → 75 %; 60 puntos de auditoría en 6 áreas de 10; 20 decisiones = 5 + 4 + 3 + 4 + 4 por
  área y 5 + 2 + 3 + 1 + 4 + 3 + 2 por herramienta; 25 acuerdos = 15 cerrados + 10 abiertos.
- **La auditoría respeta la exclusión de APPCC (SPEC §2.2, libro 7):** los cinco puntos que mencionan
  temperatura o alérgenos son de experiencia de cliente («El plato llega a la temperatura correcta», «El
  personal informa de los alérgenos sin remitir al cartel»), no registros sanitarios.

---

## Entradas propuestas para `auditorias/guias-v2-research-sector.json`

Las dos URLs resolvieron (HTTP 200) y el texto se leyó el 04-09-2026. Formato idéntico al de MM-01…MM-57.

```json
{
  "id": "MM-58",
  "tema": "Verifactu",
  "dato": "El Real Decreto-ley 15/2025, de 2 de diciembre, aplaza Verifactu por su DISPOSICIÓN FINAL PRIMERA, que da nueva redacción a la disposición final cuarta del RD 1007/2023: los obligados tributarios del artículo 3.1.a) del Reglamento (contribuyentes del Impuesto sobre Sociedades) deben tener adaptados sus sistemas antes del 1 de enero de 2027, y el resto de obligados del artículo 3.1 antes del 1 de julio de 2027. OJO al citarlo: el precepto que aplaza es la disposición final primera del RDL, NO un «artículo 3» del RDL; el artículo 3 que aparece en el texto es el del Reglamento del RD 1007/2023 y define QUIÉN está obligado, no CUÁNDO. Lo que hace el manager hoy es pedir por escrito a su proveedor de TPV la fecha de su versión adaptada",
  "cifra": "1 de enero de 2027 (sociedades) y 1 de julio de 2027 (resto)",
  "unidad": "",
  "anio_del_dato": "2026",
  "fuente_titulo": "Real Decreto-ley 15/2025, de 2 de diciembre, disposición final primera (modifica la disposición final cuarta del RD 1007/2023, de 5 de diciembre)",
  "url": "https://www.boe.es/buscar/act.php?id=BOE-A-2025-24446",
  "fecha_publicacion": "2025-12-03",
  "cita_literal": "Disposición final primera. Modificación del Real Decreto 1007/2023, de 5 de diciembre. La disposición final cuarta queda redactada en los siguientes términos: «Disposición final cuarta. Entrada en vigor y efectos. […] No obstante, los obligados tributarios a que se refiere el artículo 3.1.a) deberán tener adaptados los sistemas informáticos a las características y requisitos establecidos en este reglamento y en su normativa de desarrollo antes del 1 de enero de 2027. El resto de obligados tributarios mencionados en el artículo 3.1 deberán tener operativos los citados sistemas informáticos antes del 1 de julio de 2027.»",
  "fiabilidad": "alta",
  "nota": "Verificado el 2026-09-04 leyendo el texto consolidado del RD 1007/2023 (BOE-A-2023-24840), cuya ficha de vigencia remite a «la disposición final 1 del Real Decreto-ley 15/2025, de 2 de diciembre. Ref. BOE-A-2025-24446», y el propio RDL. Corrige la cita «RDL 15/2025, art. 3» que arrastraban manual-manager-SPEC.md §3 y calendario-cumplimiento-legal.xlsx!Estado Normativo!F9."
},
{
  "id": "MM-59",
  "tema": "Fumar en terrazas",
  "dato": "La prohibición de fumar en terrazas de hostelería NO está vigente: el 21 de julio de 2026 el Consejo de Ministros aprobó un proyecto de ley, que es un proyecto. Lo que define hoy una terraza a efectos de la ley antitabaco es el artículo 2.2 de la Ley 28/2005: es espacio al aire libre —y por tanto se puede fumar— todo espacio no cubierto, o todo espacio que, estando cubierto, esté rodeado lateralmente por un máximo de DOS paredes, muros o paramentos. Con tres o más, deja de ser espacio al aire libre y rige la prohibición general",
  "cifra": "máximo 2 paredes, muros o paramentos",
  "unidad": "",
  "anio_del_dato": "2026",
  "fuente_titulo": "Ley 28/2005, de 26 de diciembre, de medidas sanitarias frente al tabaquismo, art. 2.2 (apartado añadido por el RDL 17/2017)",
  "url": "https://www.boe.es/buscar/act.php?id=BOE-A-2005-21261",
  "fecha_publicacion": null,
  "cita_literal": "2. A efectos de esta Ley, en el ámbito de la hostelería, se entiende por espacio al aire libre todo espacio no cubierto o todo espacio que estando cubierto esté rodeado lateralmente por un máximo de dos paredes, muros o paramentos.",
  "fiabilidad": "alta",
  "nota": "Verificado el 2026-09-04 sobre el texto consolidado del BOE. Da URL a la fila «Prohibición de fumar en terrazas» de calendario-cumplimiento-legal.xlsx!Estado Normativo, que hoy es una de las dos filas sin enlace, y respalda la nota de Régimen Disciplinario ALEH!L9 sobre la falta grave de fumar en zonas no permitidas."
}
```

---

## Nota de método

Todo lo cuantificado en este informe sale de scripts sobre los ficheros, no de lectura: gate de funciones
prohibidas y constantes sobre las 1.884 fórmulas, gate de verde/bloqueo sobre las 3.978 celdas con relleno,
lectura del XML crudo para el caché y las `dataValidation`, barrido cp1252 sobre celdas, notas, listas y
nombres de hoja, recálculo de las 52 semanas y de los meses del cuadro contra el cuadro mensual de la Guía
Food Cost, y `curl` a las 17 URLs más lectura del texto consolidado del BOE para las cinco normas que
sostienen los hallazgos A1, A2 y los dos literales verificados. Ningún libro ni generador ha sido modificado.

**Al aplicar los fixes, ojo con la copia publicada:** los 7 `.xlsx` de
`astro-site/public/dl/manual-manager-restaurante/` son **byte a byte idénticos** a los de `build/`
(comprobado con `cmp` el 04-09-2026). Corregir sólo `build/` dejaría el producto entregable sin el
arreglo y el gate de descargas en verde: hay que regenerar y volver a copiar los siete.

Via: Claude Code
