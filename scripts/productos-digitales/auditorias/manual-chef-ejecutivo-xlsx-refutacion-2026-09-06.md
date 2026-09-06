# Refutación de los 7 libros de Excel — «Manual del Chef Ejecutivo» (2026-09-06)

> Refutador adversarial de los xlsx de `scripts/productos-digitales/manual-chef-ejecutivo/build/`, dos lentes en un
> solo pase: **(A) fórmulas y convenciones** y **(B) dominio y legal**. El encargo era TUMBAR los libros, no
> confirmarlos. Contrastado contra `manual-chef-ejecutivo-SPEC.md` (D1-D30, §2.2, §3, §8), `datos_ejemplo.py`,
> `auditorias/guias-v2-research-sector.json`, el informe y el JSON de correcciones del verificador legal
> (`manual-chef-ejecutivo-verificacion-legal-2026-09-06.{md,json}`), `manual-manager-SPEC.md` y el molde de
> `manual-manager/`.
>
> **Veredicto: CORREGIR.** 17 hallazgos: **3 altos, 6 medios, 8 bajos**. Ninguno afecta al motor de cálculo, que
> está limpio; los tres altos son (1) una validación de datos que impide al comprador usar sus propias partidas en
> dos libros, (2) 43 celdas con faltas de ortografía —varias dentro de texto que el producto declara *literal* del
> convenio— y (3) una fecha de entrada en vigor imposible en la hoja «Estado Normativo».

## 0. Lo que NO se pudo tumbar (verificado, no asumido)

Se comprobó celda a celda con `openpyxl` (formulas y `data_only`) y con `pycel`, un libro cada vez:

| Comprobación | Resultado |
|---|---|
| Fórmulas totales | 2.564 en los 7 libros |
| Fórmulas sin caché | 899, y **las 899 evalúan a `""`** (comprobado con `pycel` una a una: 0 fallos, 0 que debieran tener valor). Es la convención «sin dato» = `""`, no un fallo de caché |
| Errores `#REF!` / `#DIV/0!` / `#VALUE!` en `data_only` | **0** |
| Funciones prohibidas (`INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA`, `RANK`, `NETWORKDAYS`) | **0** |
| Referencias externas entre ficheros (`[`) | **0** — D4 se cumple en todo el pack |
| Divisiones sin `IFERROR` | **0** |
| Constantes numéricas dentro de fórmula | **0** distintas de 0/1/100 y de los índices de `INDEX`/`MATCH` (posición de ranura de partida), que la SPEC permite |
| Semáforos numéricos sin `ISNUMBER` | **0** (28+30+19+15+12+16+9 = 129 reglas, todas con `dxf` y con prioridad ordenada; la regla crítica va siempre antes que la ámbar) |
| `print_setup` A4 + `fitToPage` | **28/28 hojas** |
| Protección de hoja sin contraseña | **28/28 hojas** |
| Celdas verdes (`E8F5E9`) bloqueadas | **0 de 4.679**; y 0 celdas no verdes desbloqueadas con valor |
| Metadata `author` / `lastModifiedBy` | `AI Chef Pro` en los 7 |
| Caracteres fuera de cp1252 (WinAnsi) | **0** |
| Hoja «Instrucciones» la primera, línea de versión, bio y nota de desproteger | 7/7 |
| Celdas del `mapa-*.json` que no existen | **0** de 724 mapeadas |
| Formatos numéricos | `#,##0.00 €`, `0.0%`, `dd/mm/yyyy`, `#,##0(.0/.00/.000)`; **0 anomalías** (ningún % con valor >1,5; ningún texto en celda con formato €) |
| Lista negra §8 de la SPEC | 0 apariciones de «+49,9 %», «la temperatura legal de la cocina es 14-25 °C», «20 fuentes», «45-55 €», «−20 °C durante 7 días», «110 €», «55 €». `RD 1420/2006` sale **una** vez y es correcta: «está DEROGADO con efectos del 22-12-2022» |
| Notas legales | 66 notas «Verificado el 06-09-2026», **todas con norma y URL**, 0 sin enlace, 0 con otra fecha |
| Correcciones del verificador legal comprobadas una a una | 63 °C (art. 30.2) ✔ · temperatura PRL por categoría con «sin rango para el pesado» y el condicionante del local ✔ · «el RD 487/1997 no contiene ninguna cifra en kilos» ✔ · microempresas excluidas del art. 6 pero obligadas por el art. 8 ✔ · anisakis −20 °C/24 h y −35 °C/15 h ✔ · umbral «más de 40» con comparación estricta (`$D$22>$D$7`) ✔ · el Anexo III del RD 773/1997 nunca «exige» un EPI ✔ |
| Coherencia con `datos_ejemplo.py` y con el Manager | `python3 datos_ejemplo.py` sale **TODAS LAS COMPROBACIONES EN VERDE**: 12 personas, 6 partidas, 52 semanas ISO y 46.737 cubiertos idénticos a los del Manager; la fila de referencia de la comparativa (3.320 cub · 4,63 % · 19,2 min · 0,269 h/cub · 6,63/1.000) la recalcula el libro desde la hoja «Semana» y coincide |
| Reglas de no-solape | Libro 1 sin una sola columna de dinero ✔ · merma agregada por partida, nunca por producto ✔ · ficha con **alérgenos de proceso** y remisión expresa a `pack-appcc/08` para la declaración de carta (D5) ✔ · libro 7 excluye limpieza, plagas y temperaturas de cámara ✔ · libro 4 no pregunta «¿puede cubrir?» y remite a la matriz del Manager ✔ · coste por ración **copiado** en celda verde, no calculado (D4) ✔ |
| Utilidad | Las 28 hojas responden a una decisión concreta y las cadencias declaradas son realistas. La `Matriz RACI` valida las 15 decisiones con una sola «A» y al menos una «R» (15/15 «Correcta»); la auditoría demuestra el caso que justifica el libro (la nota global sube de 3,09 a 3,54 y el área de mermas cae de 3,67 a 2,58) |

---

## Lente A — Fórmulas y convenciones

### A1 · ALTA · Validación con lista separada por comas en 3 libros, con las partidas del ejemplo cableadas y con rechazo activo
**Libros:** `desarrollo-carta-control-calidad`, `banquetes-comidas-testigo`, `auditoria-interna-cocina`.
**Celdas:**
- `desarrollo-carta-control-calidad`: `Calendario de Temporada!C13:C24` y `Registro de Pruebas de Plato!E6:E45` → `"Pase y caliente,Fríos y entrantes,Postres y panadería,Barra y bebidas,Sala y servicio,Caja y cierre"`; además `Calendario de Temporada!I13:I24`, `J13:J24` y `Control de Calidad del Pase!B6,D6,G6,H6`.
- `banquetes-comidas-testigo`: `Producción y Ficha de Banquete!D13:D24` (la misma lista de seis partidas), `Registro de Comidas Testigo!D30:D34` (`"Sí,No"`) y `J39:J50` (`"Refrigeración,Congelación"`).
- `auditoria-interna-cocina`: `Estado Normativo!H13:H26` (`"Sin comprobar,Sigue igual,Ha cambiado"`).

**Problema.** La convención de familia de la SPEC §2.2 dice literalmente «**DV contra rango (nunca lista con comas)**», y los libros 1, 2, 3 y 4 la cumplen (apuntan a `Parámetros!$A$44:$A$48`, `$A$12:$A$19`, `'Ficha (plantilla)'!$A$74:$A$77`…). Estos tres no. Y no es formalismo: las dos listas de partidas llevan **cableados los seis nombres de «La Encina»** y las validaciones tienen `showErrorMessage=True`, así que **el comprador que renombre sus partidas en los libros 1, 2 y 4 —que es exactamente lo que D7 y D9 le mandan hacer— no puede escribirlas en los libros 5 y 6**: Excel se las rechaza. Para arreglarlo tiene que desproteger la hoja y editar la validación a mano, que es justo lo que la nota de desproteger dice que no hace falta. Media docena de hojas del pack se quedan atadas al restaurante de ejemplo.

**Fix.** Añadir al final de cada una de las tres hojas un bloque de listas (como `planificacion-produccion-semanal!Producción por Partida!$A$12:$A$19` o `cuadro-de-mando-cocina!Parámetros!$A$51:$A$52`) y apuntar **todas** las DV a ese rango. En los libros 5 y 6 el bloque de partidas debe ser de celdas verdes, con su nota «cópialas del libro 1» (copia declarada, D4). Añadir al gate una comprobación de que ninguna `dataValidation` de tipo `list` tiene una `formula1` que empiece por `"`.

### A2 · MEDIA · El nombre de la unidad de referencia está cableado y contradice lo que promete la hoja «Parámetros»
**Libros:** `cuadro-de-mando-cocina`, `auditoria-interna-cocina`.
**Celdas:** `Comparativa entre Unidades!A17` y `Histórico por Unidad!A6`.

**Problema.** `cuadro-de-mando-cocina!Parámetros!A11` dice «El nombre de la cocina es el que aparece como unidad de referencia en la hoja *Comparativa entre Unidades*», y `Parámetros!B5` vale `Restaurante de ejemplo «La Encina»`. Pero `Comparativa entre Unidades!A17` es un **texto literal**, `La Encina (unidad de referencia)`: ni es una fórmula ni coincide con B5, lo que prueba que no hay vínculo. El comprador cambia el nombre de su cocina en Parámetros y la comparativa sigue diciendo «La Encina» para siempre. Mismo patrón en el libro 7: `Histórico por Unidad!B6` **sí** lee `'Auditoría'!$D$7` (la fecha), pero `A6` es literal mientras `Auditoría!D9` es la celda verde donde el usuario escribe qué cocina audita.

**Fix.** `Comparativa entre Unidades!A17` → `=IF(Parámetros!$B$5="","",Parámetros!$B$5&" (unidad de referencia)")`. `Histórico por Unidad!A6` → `=IF('Auditoría'!$D$9="","",'Auditoría'!$D$9)`.

### A3 · MEDIA · La alerta de sobreproducción corta la comprobación de caducidad justo en el caso en que hay merma segura
**Libro:** `planificacion-produccion-semanal`.
**Celdas:** `Producción por Partida!N24:N45` (y su efecto en `M24` y en `Lista de Producción Diaria!D14`).

**Problema.** La fórmula es
`=IFERROR(IF($G24="","",IF(AND(ISNUMBER($H24),$H24>$G24),"Sobreproducción: el stock ya cubre toda la semana, no produzcas",IF(AND(...),IF($L24<'Previsión de Cubiertos'!$B$7+$H24*'Previsión de Cubiertos'!$B$8/$G24,"El stock caduca antes de consumirse al ritmo previsto: ...",""),""))),"")`
La comprobación de caducidad va **anidada en el ELSE** de la rama de sobreproducción, así que cuando hay más stock que previsión nunca se evalúa. En el propio ejemplo publicado pasa: E1 (masa de croqueta) tiene `H24 = 140` raciones en cámara con `L24 = 08-09-2026` de consumo preferente, contra `G24 = 104` previstas para la semana del 07 al 13. El libro dice «el stock ya cubre toda la semana, no produzcas», `M24` sale 0 y la `Lista de Producción Diaria` imprime **0 raciones los seis días** — y no avisa de que ese stock caduca el segundo día de la semana. El aviso que el pack vende como su alerta de sobreproducción está dando, en su propio caso de demostración, un consejo que garantiza la merma que el libro 1 mide.

**Fix.** Separar las dos comprobaciones y concatenarlas, p. ej. `=IFERROR(IF($G24="","",TRIM(IF(AND(ISNUMBER($H24),$H24>$G24),"Sobreproducción: el stock ya cubre toda la semana, no produzcas. ","")&IF(AND(ISNUMBER($L24),ISNUMBER($H24),$H24>0,...,$L24<...),"El stock caduca antes de consumirse al ritmo previsto: prográmalo en los primeros días","")))," ")`.

### A4 · BAJA · Seis celdas del `mapa-*.json` resuelven a «sin dato» y el guion puede citarlas como si tuvieran valor
**Libros:** `banquetes-comidas-testigo`, `desarrollo-carta-control-calidad`, `auditoria-interna-cocina`, `ficha-tecnica-proceso`.
**Celdas:** `Producción y Ficha de Banquete!C32,D32,E32` (partida «Barra y bebidas», que no interviene en el menú del banquete); `Calendario de Temporada!O16,P16,O17,P17` (N4 y N5 todavía sin pruebas); `Histórico por Unidad!C14` («Tu estándar de grupo»); `Índice de Fichas!C6` («Avisar si la ficha supera (días)»).

**Problema.** Las dos últimas están vacías **a propósito** y así lo explican sus notas (`Índice de Fichas!D6`: «Vacía a propósito: el plazo de revisión lo pones tú»), pero el mapa no distingue una celda vacía a propósito de una que debería tener valor, y los redactores del guion citan por mapa. Además, dejar `C14` vacía hace que las columnas `K` y `L` de `Histórico por Unidad` («Desviación contra tu estándar» y «Lectura») salgan en blanco en las tres unidades del ejemplo: el comprador no llega a ver para qué sirven.

**Fix.** Marcar esas celdas en el `mapa-*.json` con `"vacia_a_proposito": true` y añadir al gate un aviso si el guion cita una celda del mapa sin valor. En `Histórico por Unidad!C14`, rellenar con el estándar del grupo del caso (el mismo 3,54 o el valor que fije el constructor) para que las dos columnas se demuestren.

### A5 · BAJA · Las instrucciones del libro 1 prometen que las columnas de partidas desactivadas «el libro las ignora», y los totales no las ignoran
**Libro:** `cuadro-de-mando-cocina`. **Celdas:** `Instrucciones!A6` frente a `Semana!M5:M56` y `Semana!AE5:AE56`.

**Problema.** `Instrucciones!A6` dice «si pones 4, las columnas 5 a 8 se quedan sin encabezado y el libro las ignora». Lo que ignoran las ranuras desactivadas son los **semáforos** y el recuento `AR` (por `ISNUMBER` del objetivo, que sale vacío). Pero `M5` (`=IF(COUNT($E5:$L5)=0,"",SUM($E5:$L5))`) y `AE5` (`SUMPRODUCT($E5:$L5,$E$62:$L$62)`) siguen sumando lo que quede escrito en esas columnas. El libro 4 lo dice bien en `Organigrama!D5` («se marcan *Fuera del alcance* y **dejan de avisarte**»); el libro 1 promete de más.

**Fix.** Igualar el texto del libro 1 al del libro 4 («dejan de avisarte»), o enmascarar las ranuras inactivas en `M` y `AE`.

### A6 · BAJA · El horizonte de consumo del aviso de caducidad usa 7 días en una semana con el lunes cerrado
**Libro:** `planificacion-produccion-semanal`. **Celdas:** `Previsión de Cubiertos!B8` (= 7) usada en `Producción por Partida!N24:N45` como `$H24*'Previsión de Cubiertos'!$B$8/$G24`.

**Problema.** El caso modelado cierra los lunes (las filas 15 y 16 de la previsión van vacías a propósito) y sirve en 6 días. Al repartir el consumo entre 7 días, el aviso estima que el stock dura un día más de lo que dura, y por tanto se enciende menos de lo que debería.

**Fix.** Calcular el horizonte con los días con previsión (`COUNT` de días con cubiertos > 0) o dejar B8 pero documentar en la nota que son días naturales, no días de servicio.

### A7 · BAJA · Dos patrones distintos para comparar contra el valor de una lista
**Libros:** `banquetes-comidas-testigo`, `desarrollo-carta-control-calidad` frente a `ficha-tecnica-proceso`.
**Celdas:** `Registro de Comidas Testigo!O39:O50` compara con los literales `"Refrigeración"`/`"Congelación"`; `Control de Calidad del Pase!J6:J45` y `K6:K45` con `"Sí"`; `Calendario de Temporada!M13:M24` con `"No"`. En cambio `Índice de Fichas!J10:J39` compara contra las celdas de su propia lista (`$A$42`, `$A$43`, `$A$44`, `$A$45`, `$A$49`).

**Problema.** El segundo patrón sobrevive a que alguien renombre un valor de la lista; el primero deja de funcionar **en silencio** (devuelve `""` o el estado equivocado sin ningún error). Conviviendo los dos en el mismo pack, el comprador no puede saber cuál es seguro tocar.

**Fix.** Unificar en el patrón del libro 3: la lista en celdas, la DV apuntando al rango (ver A1) y las fórmulas comparando contra esas celdas.

---

## Lente B — Dominio y legal

### B1 · ALTA · 43 celdas con faltas de ortografía, varias dentro de texto que el libro declara LITERAL del convenio
**Libros:** 6 de los 7 (todos menos `cuadro-de-mando-cocina`).

| Libro | Palabra | Debe decir | Celdas |
|---|---|---|---|
| brigada-puestos-y-evaluacion | autonomo | autónomo | `Organigrama!G24,G26,G27`, `Fichas de Puesto!E6,E7,E8` … (11) |
| brigada-puestos-y-evaluacion | autonoma | autónoma | `Fichas de Puesto!C10,C11,C14` |
| brigada-puestos-y-evaluacion | mercancias | mercancías | `Fichas de Puesto!C6,C9,C12,C14` |
| brigada-puestos-y-evaluacion | idoneas | idóneas | `Fichas de Puesto!C10` |
| brigada-puestos-y-evaluacion | Direccion | Dirección | `Rúbrica de Competencias!E35`, `Histórico!G7` |
| brigada-puestos-y-evaluacion | bascula | báscula | `Prueba Práctica!D11` |
| brigada-puestos-y-evaluacion | otono / sabados / reunion | otoño / sábados / reunión | `Plan de Desarrollo Individual!E12` |
| auditoria-interna-cocina | microbiologicos / derogo / garantia / entro / freir / humedos | microbiológicos / derogó / garantía / entró / freír / húmedos | `Estado Normativo!A16,B22,C22,C13,C23,C25` |
| auditoria-interna-cocina | estanterias / periodicas / vacian | estanterías / periódicas / vacían | `Auditoría!C26,C53,C54` |
| banquetes-comidas-testigo | jamon | jamón | `Registro de Comidas Testigo!C39,C41`, `Producción y Ficha de Banquete!C13,C14` |
| ficha-tecnica-proceso | anadir / rucula / cascara | añadir / rúcula / cáscara | `Ficha (ejemplo)!B27,B31,A64` |
| desarrollo-carta-control-calidad | castanas | castañas | `Calendario de Temporada!B16` |
| planificacion-produccion-semanal | chuleton | chuletón | `Producción por Partida!E32` |

**Por qué es alto y no cosmético.** Tres razones concretas:
1. **La columna del convenio se vende como literal.** `Fichas de Puesto!A3` dice «La columna de funciones del convenio es LITERAL: es lo que pone el ALEH VI», e `Instrucciones!A7` remata «Esa columna no se toca: es lo que pone el ALEH VI, y es lo que un inspector o un abogado va a leer». El art. 17.B escribe «autónoma», «mercancías», «idóneas»; el libro escribe «autonoma», «mercancias», «idoneas». Una cita literal con faltas deja de ser una cita literal.
2. **«Frutos de cascara»** (`Ficha (ejemplo)!A64`) es el nombre de un alérgeno del Anexo II del Rgto. (UE) 1169/2011, que se escribe «Frutos de **cáscara**». Es la tabla de alérgenos del producto.
3. **Incoherencia entre libros del mismo pack:** el mismo plato es «Croquetas de **jamón** ibérico (6 ud)» en `ficha-tecnica-proceso!Índice de Fichas!B10` y `planificacion-produccion-semanal!Producción por Partida!B24`, y «Croquetas de **jamon** ibérico» en `banquetes-comidas-testigo`. Además «otono» y «castanas» pierden la eñe, que en «castanas» cambia la palabra.

**Fix.** Corregir en la fuente (`manual-chef-ejecutivo/datos_ejemplo.py`: `PUESTOS_ALEH`, `NIVELES_DELEGACION`, `EVALUACIONES`, `PRUEBA_PRACTICA`, `PDI`, `COMIDAS_TESTIGO`, `BANQUETE_MENU`, `AUDITORIA_COCINA`, `ESTADO_NORMATIVO`, `CALENDARIO_TEMPORADA`, `FICHA_TECNICA_EJEMPLO`, `MIX_VENTA_PARTIDA`), regenerar los 7 libros, volver a pasar `inject_cache.py` y verificar `data_only`. Y añadir el barrido de estas ~25 palabras al gate: `checks()` ya comprueba cp1252, que no detecta nada de esto porque las formas sin tilde son WinAnsi perfectamente válidas.

### B2 · ALTA · La hoja «Estado Normativo» da una fecha de entrada en vigor de la Ley 1/2025 anterior a su publicación
**Libro:** `auditoria-interna-cocina`. **Celda:** `Estado Normativo!B26`.
**Dice:** «Vigente desde el **02-01-2025**; el art. 6 es exigible desde el 02-04-2026».

**Problema.** La Ley 1/2025 es **de 1 de abril de 2025** y se publicó en el BOE el **02-04-2025** — así lo fija el informe del verificador legal en la corrección de CE-33, que cita la Disposición final vigésima («las medidas obligatorias del artículo 6 serán aplicadas transcurrido el plazo de un año desde la publicación en el BOE», *publicada el 02-04-2025*, exigible el 02-04-2026). Una norma no puede estar vigente tres meses antes de publicarse. La segunda mitad de la frase es correcta y procede del verificador; la primera **no está ni en `guias-v2-research-sector.json` (CE-31..CE-34, MM-36) ni en el informe del verificador**: es un dato añadido en `datos_ejemplo.py` (`ESTADO_NORMATIVO`) sin fuente, en la única hoja del pack cuya promesa explícita es «esta hoja existe para que no tengas que creerte nada».

**Fix.** `B26` → «Publicada en el BOE el 02-04-2025; las obligaciones del art. 6 son exigibles desde el 02-04-2026 (DF vigésima)». Y añadir al gate: ninguna fecha de la hoja «Estado Normativo» puede ser anterior a la de publicación de la norma que describe.

### B3 · MEDIA · El libro de banquetes cita el art. 30.9 y no lo implementa: falta la doble toma del catering
**Libro:** `banquetes-comidas-testigo`. **Celdas:** tabla `Registro de Comidas Testigo!A38:P50` y notas `E7`, `E9`, `E35`, `Instrucciones!A19`.

**Problema.** Las cuatro notas legales del libro citan «RD 1086/2020, art. 30, **apartados 8, 9 y 10**», pero el apartado 9 no está implementado. El verificador legal lo marcó expresamente al corregir CE-11: «El art. 30.9 añade el caso del catering: si la elaboración y el servicio se hacen en establecimientos distintos, quien elabora recoge la testigo en el momento más próximo a su salida del establecimiento y quien la sirve la recoge en el momento del servicio, **es decir, dos tomas y no una**», y remata «*Añade el art. 30.9, ausente del research y central para el libro 6 y el cap. 16*». La tabla de muestras tiene una sola «Fecha de recogida» y una sola «Hora» por elaboración y ninguna columna que distinga las dos tomas; el público que declara la SPEC §0 incluye «chef ejecutivo de catering» y «jefe de cocina de colectividades/catering», que es justo a quien le aplica.

**Fix.** Añadir a la tabla una columna **«Momento de la toma»** con DV contra rango (`Salida del obrador` / `En el servicio` / `Toma única`), una celda verde en el bloque del evento **«¿Elaboración y servicio en establecimientos distintos?»**, y una fórmula de aviso que marque las elaboraciones con una sola toma cuando esa celda diga «Sí». Nota con el texto del art. 30.9 y la URL ya usada en el libro.

### B4 · MEDIA · Los diez puestos del convenio están normalizados: no son los del art. 15 de 2023 ni los de la modificación de 2026
**Libro:** `brigada-puestos-y-evaluacion`. **Celdas:** `Fichas de Puesto!A6:A15`, `Organigrama!C48:C57` (lista de la DV) y la nota `Fichas de Puesto!A18`.

**Problema.** El libro escribe una lista homogénea: «Jefe/a de cocina», «Segundo/a jefe/a de cocina», «Jefe/a de catering», «Jefe/a de partida», «Cocinero/a», «Repostero/a», «Encargado/a de economato», «Ayudante/a de cocina», «Ayudante/a de economato», «Auxiliar de cocina y economato». El informe del verificador legal (`SPEC-1-D23-modificacion-aleh-2026`, severidad **alta**) dice que la Resolución de 25-08-2026 (BOE-A-2026-18630) **sí** modifica los arts. 15 a 17, que **solo 5 de los 10 puestos** cambiaron de nombre invirtiendo el orden de género («Jefa/e cocina», «Jefa/e catering», «Cocinera/o», «Ayudanta/e cocina», «Encargada/o economato»), que los otros cuatro «siguen escritos como en 2023 (*2.º Jefe/a cocina*, *Jefe/a partida*, *Repostero/a*, *Auxiliar cocina*)» y que hay una incoherencia del propio BOE con «Ayudante/a economato». Su instrucción es literal: «**El libro 4 debe reproducir la lista mixta o citar solo los nombres del art. 17, sin inventar homogeneidad**». El libro inventa homogeneidad (añade la preposición «de», que el convenio no pone) y presenta el resultado como nombres del convenio en la hoja que declara ser literal.

Añadido: `Fichas de Puesto!A18` cita «BOE-A-2023-6344, **modificado por BOE-A-2026-18630**» y enlaza a `https://www.boe.es/diario_boe/txt.php?id=BOE-A-2023-6344`, mientras `A19` enlaza al `act.php` consolidado del mismo id — y el verificador advierte que **ese consolidado todavía muestra la redacción de 2023**, así que el lector que pulse el enlace no verá la modificación que la nota afirma.

**Fix.** Reproducir los nombres tal como los imprime cada norma (lista mixta), con una nota corta que avise de la incoherencia del BOE en «Ayudante/a economato», o retitular la columna «Puesto (denominación del art. 17.B)» y no presentarla como el listado del art. 15. Añadir la URL de BOE-A-2026-18630 junto a la del consolidado.

### B5 · MEDIA · El punto 21 de la auditoría audita una práctica diaria y señala una hoja semanal
**Libro:** `auditoria-interna-cocina`. **Celda:** `Auditoría!C39`.
**Dice:** «Cada partida anota su merma a diario en la hoja del cuadro de mando».

**Problema.** La hoja «Semana» del `cuadro-de-mando-cocina` es semanal: 52 filas, una por semana ISO, y así lo explica `cuadro-de-mando-cocina!Instrucciones!A9`. En todo el pack no hay ninguna hoja donde anotar la merma diaria. El auditor que use el punto 21 tal como está no puede verificarlo con ninguna herramienta del producto, y el comprador que lo lea buscará una hoja que no existe.

**Fix.** Reformular el punto: «Cada partida pesa y anota su merma a diario, y el total de la semana se lleva a la hoja *Semana* del cuadro de mando», o añadir un bloque diario opcional al libro 1. La primera opción es la barata y no toca fórmulas.

### B6 · MEDIA · El muestreo del pase no permite contar los platos calientes que salieron por debajo de 63 °C, y el ejemplo trae uno
**Libro:** `desarrollo-carta-control-calidad`. **Celdas:** `Control de Calidad del Pase!E6:E45`, `D56`, `D57`, `D58`.

**Problema.** `D56` y `D57` dan el mínimo y el máximo de **todas** las muestras mezclando frío y caliente, así que el «mínimo del muestreo» es siempre el postre o la ensalada más fríos: sale **6 °C**, que no dice nada. El dato que sí importa —cuántas elaboraciones que se mantienen en caliente salieron por debajo del umbral de `D58` (63 °C, con su nota legal correcta)— no se calcula, y el propio juego de datos contiene una: `10-09-2026, P1, 61 °C`, con la observación «Sale por debajo de 63 °C: se rehace», que queda enterrada en una columna de texto libre. La `Ficha (plantilla)` del libro 3 sí hace esa comprobación (`B50` → «POR DEBAJO DEL MÍNIMO»), plato a plato; el libro que muestrea el servicio, no.

La nota `A61` («el libro NO lo aplica solo a la columna de temperatura… una ensalada se sirve a 9 °C y una torrija templada a 57 °C sin incumplir nada») es un razonamiento **correcto** y no hay que tocarlo: el problema no es que no se puntúe la columna, es que falta el dato que permitiría puntuarla bien.

**Fix.** Añadir la columna «¿Se mantiene en caliente? (Sí/No)» con DV contra rango, y dos filas al resumen: «Muestras de elaboraciones que se mantienen en caliente» y «De ellas, por debajo del mínimo de `D58`», con su semáforo `ISNUMBER`.

### B7 · BAJA · Tres libros no declaran su cadencia de uso, y son los tres cuya cadencia no es evidente
**Libros:** `desarrollo-carta-control-calidad`, `banquetes-comidas-testigo`, `auditoria-interna-cocina`. **Celdas:** hoja `Instrucciones` de cada uno.

**Problema.** La D3 de la SPEC exige que el cap. 01 declare «la **cadencia de uso** de cada libro (semanal / mensual / al abrir temporada / una vez / sólo si haces eventos)». Los libros 1, 2, 3 y 4 la traen escrita en su Instrucciones (`cuadro-de-mando-cocina!A13`, `planificacion-produccion-semanal!A12`, `ficha-tecnica-proceso!A25`, `brigada-puestos-y-evaluacion!A31`). Estos tres no dicen nada, y precisamente su cadencia es la que no se deduce sola: al abrir temporada, sólo si haces eventos, y al cierre de trimestre o de temporada. El guionista del cap. 01 no tiene de dónde sacarla sin inventarla.

**Fix.** Añadir la línea «Cadencia:» a las tres hojas de Instrucciones, con el mismo formato que los otros cuatro.

### B8 · BAJA · La glosa de «estación» se escribe de dos maneras incompatibles y se repite fuera de la primera mención
**Libros:** `cuadro-de-mando-cocina`, `planificacion-produccion-semanal`, `brigada-puestos-y-evaluacion`.
**Celdas:** `cuadro-de-mando-cocina!Instrucciones!A6` y `Parámetros!A24`; `planificacion-produccion-semanal!Instrucciones!A7` y `B20`; `brigada-puestos-y-evaluacion!Instrucciones!A6`, `Rúbrica de Competencias!A50`, `Plan de Desarrollo Individual!A30`.

**Problema.** Los libros 1 y 2 glosan «partidas (**estaciones, en el uso de otros países de habla hispana**)» y el libro 4 glosa «partidas (**estaciones, en el vocabulario de la matriz de polivalencia del Manual del Manager**)». Las dos explicaciones no pueden ser la misma: el Manual del Manager es un producto español y su matriz de polivalencia llama «estación» a esa columna, como dice `NOTA_EQUIVALENCIA_PARTIDA`. El comprador de los dos manuales lee que su otro manual habla «de otros países». Además, D9 pide la glosa **sólo en la primera mención de cada libro** y los tres la repiten en una segunda celda.

**Fix.** Una sola formulación en los tres, la del libro 4 (que es la verificable), y quitar la segunda aparición de cada libro dejando solo «partida».

### B9 · BAJA · Dos incoherencias del caso modelado en el flujo de carta nueva
**Libros:** `desarrollo-carta-control-calidad`, `ficha-tecnica-proceso`.
**Celdas:** `Calendario de Temporada!J13`, `J14`, `I15`, `H15`; `Índice de Fichas!A10:A39`.

**Problema.** (a) N1 y N2 figuran con «Ficha técnica cerrada = Sí» en el libro 5 y **no aparecen** en el «Índice de Fichas» del libro 3, que es el registro de fichas del pack y solo lista los 20 platos de la carta vigente: el flujo *documentar la ficha → entra en el índice* no queda demostrado de punta a punta, y es el que justifica tener los dos libros. (b) N3 mantiene estado «En prueba» y fecha de lanzamiento 06-10-2026 aunque su última prueba (24-09) se decidió «Descartar».

**Fix.** Añadir N1 y N2 al «Índice de Fichas» con su versión y fecha (dos filas), y poner N3 en estado «Descartado» sin fecha de lanzamiento — la alerta de días en prueba se sigue disparando igual porque depende de `J15="No"` y de los días desde la primera prueba.

### B10 · BAJA · El resumen del anisakis se queda corto respecto a la corrección del verificador
**Libro:** `auditoria-interna-cocina`. **Celda:** `Estado Normativo!C20`.

**Problema.** Dice «Congelación a -20 °C durante 24 horas, o a -35 °C durante 15 horas. El plazo de siete días que circula por el sector viene de una norma derogada» — correcto y alineado con la lista negra §8. Pero las correcciones CE-14 y MM-33 del verificador añaden tres cosas operativas que faltan: la **excepción del pescado de aguas continentales**, la de la **acuicultura marina con declaración del operador por lote**, y la obligación de **informar al consumidor por cartel o carta-menú**, que es la parte que se inspecciona y se sanciona.

**Fix.** Ampliar `C20` con esas tres frases (caben en la celda; el resto de filas de la hoja son igual de largas).

---

## Resumen

| Id | Libro | Celda/Hoja | Gravedad |
|---|---|---|---|
| A1 | desarrollo-carta · banquetes · auditoría | DV de `Calendario C13:C24`, `Pruebas E6:E45`, `Banquete D13:D24`, `Testigo D30:D34/J39:J50`, `Estado Normativo H13:H26` | alta |
| B1 | 6 de 7 libros | 43 celdas (tabla del hallazgo) | alta |
| B2 | auditoria-interna-cocina | `Estado Normativo!B26` | alta |
| A2 | cuadro-de-mando · auditoría | `Comparativa entre Unidades!A17`, `Histórico por Unidad!A6` | media |
| A3 | planificacion-produccion-semanal | `Producción por Partida!N24:N45` | media |
| B3 | banquetes-comidas-testigo | `Registro de Comidas Testigo!A38:P50` | media |
| B4 | brigada-puestos-y-evaluacion | `Fichas de Puesto!A6:A15`, `A18`, `Organigrama!C48:C57` | media |
| B5 | auditoria-interna-cocina | `Auditoría!C39` | media |
| B6 | desarrollo-carta-control-calidad | `Control de Calidad del Pase!E6:E45`, `D56:D58` | media |
| A4 | 4 libros | 6 celdas del mapa que resuelven a `""` | baja |
| A5 | cuadro-de-mando-cocina | `Instrucciones!A6` vs `Semana!M`/`AE` | baja |
| A6 | planificacion-produccion-semanal | `Previsión de Cubiertos!B8` | baja |
| A7 | banquetes · desarrollo-carta vs ficha | comparaciones contra literal vs contra celda | baja |
| B7 | desarrollo-carta · banquetes · auditoría | hoja `Instrucciones` | baja |
| B8 | cuadro-de-mando · planificación · brigada | glosa de «estación» | baja |
| B9 | desarrollo-carta · ficha-tecnica | `Calendario!J13,J14,I15,H15`; `Índice de Fichas` | baja |
| B10 | auditoria-interna-cocina | `Estado Normativo!C20` | baja |

**Orden de arreglo recomendado:** B1 y B2 primero (tocan `datos_ejemplo.py` y obligan a regenerar los 7 libros de todas formas), luego A1, A3, A2, B3, B4, B5, B6 sobre los generadores, y el resto en la misma pasada. Después: `inject_cache.py` + verificación `data_only` de cada fórmula registrada + `mapa-*.json` + `postprocess-transversal.py --dry-run` + `censo-entregables.py --only manual-chef-ejecutivo --fail`.

Via: Claude Code
