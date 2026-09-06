# Refutación de los DOCUMENTOS — «Manual del Chef Ejecutivo» (2026-09-06)

**Veredicto: CORREGIR.** 24 hallazgos confirmados: **11 altos, 11 medios, 2 bajos**.
Lente A (rigor): 14 · Lente B (producto): 10.

**Qué se ha leído entero:** `manual-chef-ejecutivo.md` (1.732 líneas, 54.208 palabras, 20 capítulos) y
`BONUS-12-situaciones-resueltas-cocina.md` (668 líneas, 12 situaciones), los 46 ficheros de la caché
`docs/txt/`, los prompts de `docs/prompts/`, `guion_manual_chef_ejecutivo.py`, el guion del hermano, la
tabla de frontera, la verificación legal contra fuentes primarias, los 225 ids del JSON de research y las
**celdas** de los 7 xlsx (openpyxl `data_only=True`, uno cada vez).

> **No se ha encontrado**: ninguna cifra de la lista negra §8 (`55 €`, `110 €`, `+49,9 %`, `−20 °C 7 días`,
> «ultraactividad», «carné» como algo vigente, «RD 1420/2006» o «RD 3484/2000» como vigentes, «capítulo de
> alérgenos» afirmado, benchmarks de merma/pase/formación, «14-25 °C es la temperatura legal»), ningún
> carácter no latino, ninguna cifra sin origen en celda o en id (las 11 salariales, los 20,14/76,49 €, las
> 50.837/2.731,1/2.646,5 y las 340 raciones están todas verificadas contra el JSON o contra el xlsx), y
> ningún año sin cita a menos de 250 caracteres. La lista negra se cumple. **Lo que falla es otra cosa:
> las TABLAS no dicen lo que dicen los párrafos que las anuncian, y los bloques de un mismo capítulo se
> repiten entre sí.**

---

## 0. La causa raíz de la mitad de los hallazgos de la lente B

`documentos.py:1012-1014` (`prompt_bloque`) entrega a **cada** bloque la lista **completa** de `puntos`
del capítulo, mientras que `bloque_epigrafes` sólo recibe su tercio. Verificado abriendo
`docs/prompts/guia_cap01_b1.txt` y `guia_cap01_b2.txt`: los seis puntos obligatorios son **idénticos**
en los dos. Resultado: los 20 capítulos tienen prosa duplicada entre bloques.

Medido con comparación de frases normalizadas (Jaccard sobre tokens, umbral 0,55) dentro de cada capítulo:

| Capítulo | Frases con solape ≥ 0,55 | Peor caso |
|---|---|---|
| 20 | 12 de 37 | «El plan de 90 días con veinte decisiones, responsable y semana se monta con el libro de reuniones y plan del M…» — **idéntica** |
| 9 | 11 de 36 | «los números del dinero —food cost, labor cost, prime cost, ticket medio— son del Manual del Manager, caps.» — **idéntica** |
| 14 | 11 de 25 | «la declaración de alérgenos plato a plato de toda la carta, con sus catorce columnas, vive en el Pack APPCC» — **idéntica** |
| 1 | 10 de 33 | «el Manual del Manager lleva el negocio, la sala y la ley;» — **idéntica** |
| 11 | 10 de 45 | «El precio es la última línea de una compra, no la primera.» — **idéntica** |
| 5, 7, 10 | 8 de ~33 cada uno | coste 5,67 €, 45/9/58 min, la frase fija de la merma |
| 3, 4, 19 | 3-8 | cap. 4 repite **literal** la frase fija de la conversación de corrección |

**Fix del generador (fuera del alcance de la corrección de texto, pero es lo que impide que vuelva):**
que el guion admita `puntos` por bloque (o que `prompt_bloque` los reparta) y que cada prompt diga qué
epígrafes escribe **otro** tramo, con la instrucción «no los desarrolles, ya están escritos».

---

## 1. Lente A — RIGOR

### A1 · ALTA · manual, cap. 6 · guion
> «en el caso de La Encina hay 14 platos registrados en el índice, de los que sólo 3 tienen la ficha cerrada, un 21,4 % del total»

La tabla que ese párrafo anuncia («El índice de fichas de la carta, plato a plato») imprime **12 filas** y
**una sola** ficha cerrada (P1). El lector cuenta 12 y 1, no 14 y 3. Causa: el guion recorta
`'filas': (10, 21)` y la hoja tiene datos hasta la fila **23** (N1 «Alcachofas confitadas…» y N2 «Guiso de
carrilleras…», las **dos otras fichas cerradas**, quedan fuera).

**Fix:** en `guion_manual_chef_ejecutivo.py`, tabla «El índice de fichas de la carta, plato a plato»:
`'filas': (10, 23)`. *Ojo al reejecutar*: N1 y N2 traen `Antigüedad de la ficha (días)` en **−16** y **−18**
(fecha de revisión 22 y 24-09-2026 contra una fecha de control del 06-09-2026); esa columna no se imprime,
pero si alguien la añade, hay que arreglar antes las fechas del xlsx.

### A2 · ALTA · manual, cap. 6 · guion
> «En el periodo se hicieron 30 muestreos del pase, de los que 4 resultaron no conformes con la ficha, y de esos, 1 plato acabó devuelto por el cliente»

La tabla que sigue («El muestreo del pase, plato a plato») imprime **15 de las 30 filas** —`'filas': (6, 20)`
sobre datos que llegan a la fila 35— y en esas 15 hay **1 no conforme y 0 devueltos**: 93,3 %, no el 86,7 %
del texto. El pie lo tapa («Quince muestreos de un mismo periodo») pero contradice al párrafo, que dice que
«el cuadro siguiente recoge el detalle plato a plato **de ese** muestreo». Además se pierden las dos columnas
con la pedagogía —«Devuelto por el cliente» y «Observación» («Sale por debajo de 63 °C: se rehace»,
«Ración de 5 croquetas en vez de 6»)— y los tiempos se redondean a entero (7,5 → 8; 8,5 → 8; 12,5 → 12).

**Fix:** `'filas': (6, 35)`, añadir las columnas `H` (Devuelto por el cliente) e `I` (Observación), y nota:
«Los treinta muestreos del periodo. Los cuatro no conformes y el único devuelto están en las columnas de la
derecha: sin la observación, un “No” no enseña nada.»

### A3 · ALTA · manual, cap. 8 + bonus, situación 5 · `cap08_b1.txt`, `BONUS…/cap05_b1.txt`
> «el muestreo de la hoja «Semana» de cuadro-de-mando-cocina.xlsx dio un tiempo medio de pase de 8,6 minutos en entrantes, 16,5 en principales y 6,7 en postres […] El cuadro siguiente cruza estos números servicio a servicio.»

El cuadro siguiente dice **8,8 / 17,2 / 7,1** (son los de `desarrollo-carta-control-calidad!Control de
Calidad del Pase`, D35:D37; los 8,6/16,5/6,7 son la media anual de `cuadro-de-mando-cocina!Semana`,
AG57:AI57). Tres indicadores con dos valores cada uno, en la misma página, sin decir que son periodos
distintos. En el bonus es peor: la situación 5 atribuye **explícitamente** «el 16,5 de los principales con el
8,6 de los entrantes» a la hoja «Control de Calidad del Pase», que contiene 17,2 y 8,8, y la tabla con los
valores buenos va tres párrafos más abajo.

**Fix (cap. 8):** «…el año cerró con una media de 8,6 minutos en entrantes, 16,5 en principales y 6,7 en
postres. El muestreo del periodo que recoge el cuadro siguiente, con treinta mediciones, da cifras algo más
altas —8,8, 17,2 y 7,1—: es normal, porque mide un periodo corto y no las cincuenta y dos semanas.»
**Fix (bonus 5):** sustituir «Esa hoja compara el 16,5 de los principales con el 8,6 de los entrantes y con el
objetivo de 18» por «Esa hoja da 17,2 minutos de media en principales y 8,8 en entrantes, contra objetivos de
18 y 10».

### A4 · ALTA · manual, cap. 7 · guion
> «Las dos últimas partidas no producen raciones, por eso van a cero: en esta cocina son unidades de servicio, no de producción.»

En la tabla que ese pie acompaña hay **tres** filas a cero: «Barra y bebidas», «Sala y servicio» y «Caja y
cierre». Y «Barra y bebidas» **sí produce**: el organigrama la marca «¿Produce raciones? Sí» con Elena T.
(P09) de responsable, la tabla del cap. 10 de este mismo manual le pone 0,09 kg de materia prima por ración
y un objetivo de merma del 4,5 %, y `cuadro-de-mando-cocina!Semana` le imputa **17.132 raciones y 45,5 kg de
merma** en el año del caso (el 22,7 % de las 75.500 raciones). El cero de la planificación es sólo que la
carta del ejemplo no tiene platos de barra.

**Fix:** «Barra y bebidas aparece a cero porque la carta de esta semana no lleva ninguna elaboración suya, no
porque no produzca: en el cuadro de mando sí tiene producción y merma propias. Sala y servicio y Caja y
cierre van a cero siempre: en esta cocina son unidades de servicio, no de producción.»

### A5 · ALTA · manual, cap. 15 · guion (fila de tabla) contra `cap15_b1.txt`
> Tabla: «Quinta gama por debajo de 4 °C | **Recomendación de una agencia autonómica, no norma estatal**; fiabilidad media declarada»

El texto del mismo epígrafe dice lo contrario y dice lo correcto: «sale de un informe del Comité Científico de
una agencia sanitaria **estatal** […] (informe del Comité Científico de la **AESAN** sobre botulismo en
envasados al vacío, 2024)». **CE-35** del JSON confirma AESAN, informe aprobado en sesión plenaria del
12-12-2024. La fila de la tabla es falsa y desautoriza al párrafo que la precede.

**Fix:** «Recomendación del Comité Científico de la AESAN (2024), no norma con sanción; fiabilidad media
declarada».

### A6 · ALTA · manual, cap. 14 + bonus, situación 9 · `cap14_b3.txt`, `BONUS…/cap09_b1.txt`
> «Esa área pesa un **26 %** sobre el total de la auditoría, y su cumplimiento se queda en un 73,1 %.» · «El área de prevención de riesgos laborales reúne diez puntos de control, con un peso del **26 %** sobre el total»

26 es el **peso** del área, no un porcentaje: `auditoria-interna-cocina!Resumen por Área` da 26 sobre un
total ponderado de **123**, es decir el **21,1 %**. Las dos áreas (alérgenos y PRL) pesan 26 cada una, así que
el error se repite dos veces con dos áreas distintas. El propio cap. 17 lo escribe bien («un peso de 26 sobre
el total de 123»), lo que deja tres formulaciones distintas del mismo dato en el mismo pack.

**Fix (cap. 14):** «Esa área pesa 26 sobre los 123 puntos ponderados de la auditoría —algo más de la quinta
parte— y su cumplimiento se queda en un 73,1 %.» **Fix (bonus 9):** «reúne diez puntos de control con un peso
de 26 sobre el total ponderado de 123».

### A7 · ALTA · bonus, situación 3 · `BONUS…/cap03_b1.txt`
> «la auditoría interna de cocina de esta casa, con sus **50 puntos de control por área**» · «con los mismos **50 puntos de control por área** que recorrería quien inspecciona»

Son **50 en total, 10 por área** (cinco áreas: orden y mise en place, aplicación de fichas, mermas por
partida, prevención de riesgos, alérgenos en el pase). «50 por área» serían 250. Lo dice bien el manual en el
cap. 17 («diez puntos de control […] de los 50») y en el cap. 20 («las mismas cinco áreas, los mismos
cincuenta puntos»).

**Fix:** «con sus 50 puntos de control repartidos en cinco áreas» (las dos veces).

### A8 · ALTA · bonus, situación 5 · `BONUS…/cap05_b1.txt`
> Título e índice: «El Pase se Descontrola un Viernes: Cuarenta Comandas y **Veinticinco Minutos**» · Texto: «el tiempo se ha ido a **más del doble de esos 18 minutos**» · «Esta noche se llevó **más del doble del objetivo**»

Más del doble de 18 son más de 36 minutos, no 25. El título y el cuerpo de la misma situación dan dos
magnitudes incompatibles del suceso que da nombre a la situación.

**Fix (dos frases del cuerpo):** «el tiempo se ha ido a veinticinco minutos, siete por encima del objetivo de
dieciocho» y «Esta noche se fue a veinticinco minutos contra un objetivo de dieciocho».

### A9 · ALTA · bonus, situación 1 · `BONUS…/cap01_b1.txt`
> «el plan de desarrollo individual —**2 abiertos ahora mismo**— fija qué le falta a quien sube» · «Esos **dos** candidatos son, además, quienes ya tienen abierto un plan de desarrollo individual: el cuadro siguiente recoge qué partida aprende cada uno.»

La hoja «Plan de Desarrollo Individual» tiene **cuatro** planes (2 «En curso» + 2 «Planificado») y la tabla que
sigue **imprime los cuatro**: P06 Omar B., P12 Andrés P., P05 Laura S. y P04 Diego M. El cap. 4 del manual lo
dice bien («2 planes de desarrollo individual planificados y 2 en curso»).

**Fix:** «el plan de desarrollo individual —cuatro abiertos ahora mismo, dos en curso y dos planificados—
fija qué le falta a quien sube» y «Dos de los cuatro planes abiertos son justamente los de los candidatos; el
cuadro siguiente los recoge todos, con la próxima partida que aprende cada uno.»

### A10 · MEDIA · manual, cap. 13 · `cap13_b2.txt`
> «Las cinco temperaturas y el binomio están en el **art. 30.2** del RD 1086/2020, en la redacción que le dio el RD 1021/2022»

El 30.2 es **sólo** el mantenimiento en caliente. La refrigeración es el 30.3, la congelación el 30.4, el
binomio 60→10 °C el 30.6 y el recalentado el 30.7 — así lo dice, correctamente, la tabla que va cuatro
párrafos más abajo en el mismo capítulo. Es exactamente el tipo de cita que un inspector desmonta en un
minuto.

**Fix:** «Las cinco temperaturas y el binomio están en el art. 30 del RD 1086/2020 —apartados 2, 3, 4, 6 y
7—, en la redacción que le dio el RD 1021/2022».

### A11 · MEDIA · manual, cap. 7 · `cap07_b2.txt`
> «mantenimiento en caliente a 63 °C o más (art. 30.2), conservación refrigerada a 4 °C […] congelada a -18 °C o menos, enfriamiento […] y recalentamiento […]. **El art. 30.5 permite apartarse de esas temperaturas de conservación** si el operador demuestra ante la autoridad competente que se basan en evidencia científica»

Tras enumerar las cinco, «esas temperaturas de conservación» se lee como todas ellas. La verificación legal
(§3, N5) es tajante: **el 30.5 se refiere sólo al apartado 3 (refrigeración)** y no autoriza bajar de 63 °C ni
subir de −18 °C. El cap. 13 y la situación 8 del bonus lo escriben bien; este párrafo es el único que se sale.

**Fix:** «El art. 30.5 permite apartarse de las temperaturas de **refrigeración** del apartado 3 —nunca de los
63 °C en caliente ni de los −18 °C en congelación— si el operador demuestra ante la autoridad competente que
se basan en evidencia científica».

### A12 · MEDIA · manual, cap. 17 + bonus, situación 9 · `cap17_b2.txt` y guion (2 tablas)
> «(RD 486/1997, Anexo I, **punto 3.1**; comprobado el 6 de septiembre de 2026)» · fila 32 de las dos tablas de auditoría: «RD 486/1997, Anexo I, **punto 3.1**»

La verificación legal (CE-22) lo corrige expresamente: es el **punto 3, apartado 1.º** del Anexo I, «no
“punto 3.1”». Y el propio prompt del capítulo prohíbe esa notación («los apartados se escriben “apartado 2”,
nunca “2)”»). Aparece tres veces (prosa + las dos tablas gemelas del manual y del bonus).

**Fix:** «RD 486/1997, Anexo I, punto 3, apartado 1.º» en los tres sitios.

### A13 · MEDIA · manual, cap. 4 · `cap04_b1.txt` y `cap04_b2.txt`
> «la de fríos y entrantes, Laura S. (P05), **con 1 persona a su cargo**» · «Laura S., responsable de la partida de fríos y entrantes **con una persona más**»

La columna del organigrama es «Personas asignadas», y para fríos y entrantes vale **1**: esa persona **es
Laura S.**, que trabaja sola en su partida. Igual con Iván R.: «4 personas asignadas» le incluye a él, así que
tiene 3 a su cargo. La lectura equivocada convierte una partida de un solo cocinero —el punto único de fallo
que la situación 1 del bonus usa como ejemplo— en una partida con mando sobre alguien.

**Fix:** «la de fríos y entrantes, Laura S. (P05), que la lleva sola» y «Laura S., responsable de la partida
de fríos y entrantes, que la sostiene ella sola».

### A14 · MEDIA · manual, cap. 1 (×2) + bonus, situación 1 · `cap01_b1.txt`, `cap01_b2.txt`, `BONUS…/cap01_b1.txt`
> «se escribe partida (estación): en el resto de los capítulos, la palabra es partida a secas» · «La unidad de trabajo […] la llamamos partida (estación) —**única vez que se escribe así en todo el manual**—» · «se lleva con él el dominio único de la partida (estación) de pescados»

La glosa se escribe **tres** veces, y una de ellas mientras afirma ser la única. La regla D9 pide una sola
mención, en el cap. 1.

**Fix:** dejar la glosa sólo en el párrafo del glosario del cap. 1 (`cap01_b2.txt`), quitar «partida
(estación)» → «partida» en `cap01_b1.txt` («…se escribe partida a secas en todo el manual») y en la situación
1 del bonus.

---

## 2. Lente B — PRODUCTO

### B1 · ALTA · manual, cap. 20 (y los otros 19) · `cap20_b1.txt` + `cap20_b2.txt`
> b1: «Y con esto cerramos el manual. Hay tres cifras que merece la pena anotar el primer día […] Queda la advertencia de siempre. La ley cambia, y por eso cada afirmación de este libro lleva su norma y su fecha de corte»
> b2, 25 líneas después: «Hay tres cifras que se anotan el primer día en cada cocina del grupo […] Queda una advertencia, y es la única con la que se cierra este manual: la ley cambia, y por eso cada afirmación de este libro lleva su norma y su fecha de corte»

**El manual se despide dos veces seguidas**, con las mismas tres cifras y la misma advertencia final. Y el
epígrafe «Formación en cascada» del b2 vuelve a abrir con el posicionamiento del primer epígrafe («Este pack
está pensado para una cocina. Si diriges cuatro, no necesitas cuatro packs») y a dar los mismos números de la
comparativa (4,0 %, 4,6 %, 3,8 %, 5,4 %, 4.180 cubiertos, 1 y 5 indicadores, posición 2) que ya estaban 25
líneas antes. Es el caso extremo del problema descrito en §0, que afecta a los 20 capítulos.

**Fix del texto (cap. 20):** borrar del b1 el cierre anticipado (los dos últimos párrafos, «Y con esto
cerramos el manual…» y «Queda la advertencia de siempre…») y, del b2, el primer párrafo de «Formación en
cascada» y el párrafo que repite la comparativa; el epígrafe empieza en «Ninguna de las dos hojas la rellena
solo el chef corporativo». Y aplicar la misma poda, por capítulo, a los casos de la tabla del §0.
**Fix del generador:** repartir `puntos` por bloque en `documentos.py:1012-1014`.

### B2 · ALTA · manual, cap. 19 · `cap19_b1.txt` (y `cap19_b2.txt`)
> «Autorizar un 86 en servicio: **responde el jefe de partida**, o el jefe de cocina si toca a varias partidas» · «Aprobar una ficha técnica nueva […] **se consulta a sala**» · «Comprar fuera de escandallo un producto de temporada: **responde el jefe de cocina**»

El capítulo cuya tesis es «sólo una A por decisión» contradice su propia matriz en tres de las diez decisiones
que narra. En la tabla (hoja «Matriz RACI»): el 86 lleva **Chef ejecutivo = A** y Jefe de partida = **C**; la
ficha nueva lleva Jefe de sala = **I**, no C; la compra fuera de escandallo lleva **Gerencia = A** y Chef = R.
Y los dos bloques se contradicen entre sí: el encargo de grupo es «se consulta a cocina» en el b1 e
«informando a cocina en cuanto se confirma» en el b2 (la tabla dice **C**).

**Fix:** alinear las tres frases con la matriz. «Autorizar un 86 en servicio: responde el chef ejecutivo; lo
ejecuta el segundo, se consulta al jefe de partida afectado y se informa a sala y a dirección.» · «Aprobar una
ficha técnica nueva antes de subir a carta: responde el chef ejecutivo; se consulta al jefe de partida que va
a ejecutarla y se informa a sala y a dirección.» · «Comprar fuera de escandallo un producto de temporada: lo
ejecuta el jefe de cocina, pero **responde dirección**, porque mueve el coste; se consulta al jefe de partida.»
Y en el b2, «lo acepta dirección, **consultando a cocina** por la capacidad antes de firmar».

### B3 · ALTA · manual, cap. 5 (y bonus, situación 6) · guion (tabla) + `cap05_b1.txt`
> «Pasos numerados, cada uno con su punto de control: no basta con describir la acción, hay que dejar escrito qué se comprueba al terminarla.» · pie de la tabla: «La columna de la derecha es la que convierte una receta en una ficha: sin punto de control, un paso es una descripción»

**La columna «Punto de control» de la ficha de ejemplo está vacía en los ocho pasos** (`ficha-tecnica-proceso!
Ficha (ejemplo)`, columna F, filas 21-28: ni un valor). El manual apoya en esa columna la tesis central del
capítulo, la repite en el epígrafe «Temperatura de servicio…» y el bonus la vuelve a imprimir diciendo «con
sus puntos de control marcados uno a uno». El comprador abre la ficha «ejemplo relleno» y ve la columna que
más se le ha vendido en blanco.

**Fix:** rellenar los ocho puntos de control en el xlsx antes de reensamblar (p. ej. paso 5, «marca dorada
uniforme en las dos caras, sin jugo en la plancha»; paso 6, «sonda al centro: 58 °C antes del reposo»; paso 2,
«el puré pasa por el colador sin grumos y sale a 63 °C o más»; paso 8, «peso de la ración y foto de
referencia»). Si por calendario no se rellenan, hay que quitar la columna de la tabla y reescribir el pie.

### B4 · ALTA · manual, cap. 18 · `cap18_b1.txt`
> «la rúbrica se aplicó a **8 personas de la brigada**, con una media ponderada del conjunto de 3,53» · «**la primera persona evaluada** obtuvo una media ponderada de 2,67 y un nivel técnico de 1, combinación que la rúbrica marca como el perfil que necesita formación dirigida antes que confianza sobre el papel»

La brigada **de cocina** son 6 personas. Las 8 evaluadas incluyen a **P01 Marta L., gerente/encargada general
(Área 1.ª)** y a **P03 Nuria C., jefa de sala (Área 3.ª)**, las dos puntuadas como «Ayudante/a de cocina» en
cortes de cuchillo y cocciones. Y «la primera persona evaluada» —el ejemplo estrella del capítulo, el perfil
que «necesita formación dirigida»— **es la gerente del restaurante**. Un comprador que abra el xlsx lo ve en
diez segundos, y desmonta el capítulo entero.

**Fix (texto):** «la rúbrica se aplicó a las 6 personas de cocina y, en esta casa, también a las dos personas
de sala y dirección que entran en cocina a cubrir: 8 evaluaciones en total, con una media ponderada de 3,53»;
y cambiar el ejemplo individual a **P06 Omar B.** («media ponderada de 3,31 y nivel técnico 2»), que es un
ayudante de cocina real y además tiene plan de desarrollo abierto. **Fix alternativo (mejor):** sacar a P01 y
P03 de la hoja de rúbrica y dejar las 6 de cocina.

### B5 · MEDIA · manual, cap. 8 (2 párrafos + fila de tabla) y bonus, situación 10 · `cap08_b1.txt`, `cap08_b2.txt`
> «Y la Ley 7/2022, en su art. 18.3, exige ofrecer siempre agua no envasada gratis y complementaria a la carta, y obliga a aceptar el recipiente reutilizable que traiga el cliente»

Es **MM-38**, material del hermano, y la tabla de frontera asigna «Agua, envases, comida sobrante y perros de
asistencia» al **Manual del Manager, cap. 19**. Además no es de cocina —el agua la sirve sala— ni tiene que
ver con el epígrafe donde está («El plato que sale por la puerta»). Ocupa dos párrafos del cap. 8, una fila de
su tabla y un tercio del bloque «La norma que aplica» de la situación 10 del bonus.

**Fix:** dejar sólo lo que sí es de cocina y citar. En el cap. 8: «El envase de plástico de un solo uso se
puede cobrar aparte, por el título V de la Ley 7/2022; la comida, no. Lo demás que la ley obliga a ofrecer en
sala —el agua no envasada gratuita y la aceptación del recipiente que trae el cliente— está en el Manual del
Manager, cap. 19.» Y borrar la fila «Recipiente del cliente» de la tabla del cap. 8, que no decide nada de
cocina.

### B6 · MEDIA · bonus, situación 1 · `BONUS…/cap01_b1.txt`
> «Un jefe de partida (chef de partie) entrega el preaviso […] y se lleva con él el dominio único de la **partida de pescados** de “La Encina” […] El patrón no es exclusivo de pescados: en el organigrama […] la partida de fríos y entrantes tiene **también** 1 sola persona asignada»

En La Encina **no existe la partida de pescados** (las seis son pase y caliente, fríos y entrantes, postres y
panadería, barra y bebidas, sala y servicio, caja y cierre) **ni existe el puesto de jefe/a de partida** (el
manual repite en los caps. 2, 4 y 12 que está a cero). El propio párrafo se delata con ese «también». Es la
primera página del bonus y el primer choque del lector con los datos del pack.

**Fix:** reencuadrar la situación sobre la partida que sí es punto único de fallo: «Laura S. (P05), la única
persona de la partida de fríos y entrantes —la partida de la que salen los entrantes de toda la carta—,
entrega el preaviso con dos semanas de margen en mitad de temporada.» Cambiar el título de la situación 1 en
el guion y en el índice: «La Única Persona de una Partida se Va a Mitad de Temporada».

### B7 · MEDIA · manual, cap. 19 (×2) y bonus, situación 11 · `cap19_b2.txt`, `BONUS…/cap11_b1.txt`
> «La fila de esta decisión en la matriz **está comprobada como correcta**, y conviene que lo siga estando cada vez que cambie la brigada.» · «te dice de quién es la decisión —la fila del precio de venta de este plato **ya está marcada como Correcta**—»

«Correcta» es el valor de la columna de **gate** del xlsx, que sólo comprueba que la fila tenga exactamente
una A. No dice que el reparto sea el bueno para el restaurante del lector, que es como se lee. Es un mecanismo
interno del taller asomando al documento, y encima induce a no revisar la fila.

**Fix:** sustituir por «La matriz comprueba sola que esa fila tenga un único responsable, que es lo mínimo;
que el responsable sea el que tu casa quiere es la conversación que hay que tener una vez y firmar.»

### B8 · MEDIA · manual (14 veces) y bonus (3) · varios bloques
> «la hoja «Semana» de cuadro-de-mando-cocina.xlsx» · «la hoja «Control de Calidad del Pase» de desarrollo-carta-control-calidad.xlsx» · «la hoja «Parámetros» de cuadro-de-mando-cocina.xlsx»

Diecisiete nombres de fichero **con extensión** dentro de la prosa. El prompt prohíbe la sintaxis de celda
(«Parámetros!B7») por la misma razón que aplica aquí: el lector compra un libro, no un manual de rutas. Los
títulos de las tablas sí llevan el nombre del fichero, y ahí está bien; en mitad de una frase, no.

**Fix:** «la hoja de la semana del cuadro de mando de cocina», «la hoja de control de calidad del pase del
libro de desarrollo de carta», «la hoja de parámetros del cuadro de mando» — como ya hace, correctamente, el
cap. 9.

### B9 · MEDIA · manual, cap. 19 · `cap19_b2.txt`
> «Parar el pase por una avería de frío lo decide quien manda en cocina en ese turno, informando de inmediato a sala y a dirección; **con el tiempo medio de pase de principales en 16,5, no hay margen para consultar antes de actuar**.»

La media anual de pase de principales no tiene ninguna relación con si hay tiempo de consultar antes de parar
el pase por una avería de frío. Es una cifra metida con calzador para cumplir el cupo de datos del bloque, y
un lector con criterio lo nota.

**Fix:** cortar la subordinada: «…informando de inmediato a sala y a dirección: es la única decisión de la
matriz que cualquiera de la brigada puede activar y sólo el chef puede revertir.»

### B10 · MEDIA · bonus, situación 11 · guion (tabla)
> Tabla «Las decisiones de carta que cruzan, y quién responde de cada una», columnas: Chef ejecutivo · Jefe de sala · Gerencia · Propiedad

La tabla recorta la matriz a cuatro columnas quitando **Segundo/a de cocina** y **Jefe/a de partida**, que son
justo las que llevan la **R** en seis filas. Resultado: «Autorizar un 86», «Aprobar una ficha técnica nueva» y
«Parar el pase por una avería de frío» quedan con una A y **sin ningún R**, y «Gestionar una incidencia de
alérgeno» parece ejecutada sólo por sala. Es la tabla de una situación cuyo argumento es «mira la fila antes
de discutir».

**Fix:** imprimir las seis columnas, como hace el cap. 19 del manual, o —si no caben— reducir la tabla a las
cuatro filas de carta que la situación necesita (PVP, retirar plato, modificar gramaje, aprobar ficha) con
todas sus columnas.

### B11 · MEDIA · bonus, situación 12 · `BONUS…/cap12_b1.txt`
> «el segundo de cocina asciende a jefe de cocina […] una sola ocupa la casilla de jefe o jefa de cocina, y la de segundo o segunda **se queda en cero**»

En La Encina el puesto de segundo de cocina está a cero **en todo el manual**, también antes del ascenso: no
hay ningún segundo que pueda ascender, y el texto describe la foto posterior al ascenso como idéntica a la de
siempre (1 jefe, 0 segundos, 6 personas) sin explicar qué fue del jefe anterior. La situación no encaja con
los datos del caso que ella misma cita.

**Fix:** cambiar el protagonista al que sí existe: «Diego M. (P04), cocinero de la partida de pase y caliente
y el de más recorrido de la brigada, asciende a jefe de cocina.» Su plan de desarrollo individual («Preparar
el paso a jefe de partida de caliente») ya sostiene la escena, y el organigrama queda coherente. Ajustar el
título en el guion y en el índice: «Un Cocinero Asciende a Jefe de Cocina: los Primeros Treinta Días».

### B12 · BAJA · bonus, situación 11 · `BONUS…/cap11_b1.txt`
> «de las etiquetas que chocan en una conversación como esta —gerente, encargado, director, jefe de sala, administrador— el ALEH VI solo tipifica dos: jefe de sala, en el área de restaurante, sala y bar, y gerente, solo dentro del bloque de restauración moderna»

Cinco líneas sobre nomenclatura **de sala** —material del Manual del Manager, caps. 1 y 8— en una situación
sobre retirar un plato de la carta, para concluir algo que se dice en una frase («el convenio no gobierna
quién decide sobre la carta»). Es relleno del cupo de «datos del sector» del bloque.

**Fix:** dejar la conclusión y quitar el desarrollo: «Y no lo resuelve el convenio: el ALEH VI ordena
categorías laborales, no quién decide qué se queda en la carta. Esa frontera te la da tu matriz de
responsabilidades, no el BOE.»

### B13 · BAJA · manual, cap. 15 · guion (tabla)
> Tabla «Qué fija la ley, qué recomienda y qué no dice», tercera columna: «**Cómo se usa en cocina**» → «Reglamento (CE) 2073/2005, art. 3 y Anexo II», «Art. 5.3 del RD 1021/2022», «Reglamento (UE) 2017/2158»…

Ocho de las nueve filas ponen en esa columna la **cita de la norma**, no el uso. Sólo la primera fila cumple
el encabezado («Se decide por escrito, por elaboración, y se anota en la ficha»).

**Fix:** renombrar la columna a «Dónde está» y mover el uso al pie, o rellenar las ocho filas con el uso real
y dejar las citas para el pie de tabla, que ya las lleva todas.

---

## 3. Lo que se comprobó y salió limpio

- **Cifras contra celda:** 46.737 cubiertos, 75.500 raciones, 617 kg / 16.698 kg → 3,7 %, 3,2 / 5,1 / 2,4 /
  4,0 % por partida, 0,32 y 0,50 de alérgenos, 0,25 y 0,26 h/cubierto, 221 devueltos y 516 retrabajados →
  15,8, 587 / 933 / 958 cubiertos, 940 / 734 / 323 / 66 raciones, 14 platos y 3 fichas cerradas (21,4 %),
  30 muestreos / 4 no conformes / 86,7 % / 90,0 %, 8 pruebas / 3,75 / 2,84 € / 5 de 5 platos y 40,0 %,
  120 comensales / 6 elaboraciones / 600 raciones / 56 horas, 6 muestras testigo, 3,54 y 70,9 % de auditoría,
  3,85 y 76,9 % de PRL, 3,65 y 73,1 % de alérgenos, 3,53 de rúbrica, 160 minutos de prueba, 340 raciones y
  1.927,80 €, 5,67 €, 45/9/58 minutos, 58 °C, versión 1.2, 180 días de estado normativo, umbrales ámbar 3 y
  crítico 2, 4,0 / 4,6 / 3,8 / 5,4 % y 4.180 cubiertos de la comparativa. **Todas casan.**
- **Cifras contra id:** 1.415,47 / 1.316,72 / 1.300,28 / 1.283,83 / 1.217,99 / 1.152,15 · 2.121,29 / 1.864,51
  / 1.803,05 / 1.607,25 / 1.577,05 · 1.459,95 · 1.404,89 · 1.232,72 · 1.160,37 · 21.920,00 y 29.698,06 con el
  **+35,5 %** · 57,82 / 59,21 / 15,39 / 20 € · 1.791 y 1.783 h · 20,14 frente a 76,49 € (MM-43/CS-23) ·
  50.837 accidentes, 19 mortales, 2.731,1 / 2.547,5 / 1,02 / 2,81 (CE-30) y 2.646,5 / 2.824,1 / 2.481,8
  (CS-01), con sus dos etiquetas separadas y sin promediarlas. **Todas casan.**
- **Bloque legal:** 63 / 4 / 8 / −18 / 74 °C 15 s y el binomio 60→10 °C en 2 h; «lo recalentado que no se
  consume se descarta» (30.7 in fine) en tres sitios; comidas testigo >40 / ≥100 g / 7 días / 4 °C / −18 °C y
  la **doble toma del 30.9**; anisakis −20 °C 24 h o −35 °C 15 h **con aguas continentales excluidas y la
  excepción de acuicultura con declaración por lote**; elaboración propia voluntaria **con el límite de venta
  de la letra b**; punto 9 del cap. IX del Anexo II y «no hay capítulo de alérgenos»; cultura de seguridad
  alimentaria del cap. XI bis; 20 y 100 mg/kg de gluten con la avena; art. 6 y art. 8 de la Ley 1/2025 con la
  definición de microempresa (menos de 10 personas / 2 M€) y la **DF vigésima (exigible desde el 02-04-2026)**;
  EPI «lista no exhaustiva» + gratuidad incondicional + «la hostelería no aparece por su nombre»; temperatura
  por categoría con «sin rango para el pesado»; **50 m³/h «en los casos restantes»**; el mito de los 25 kg con
  los 80 kg derogados de 1935 y 1961; plus de formación de Madrid **que paga la empresa**, con los 90 días y
  la exclusión de PRL y manipulación; manutención 57,82 € Madrid / 59,21 € **Barcelona**; ropa del art. 41
  catalán con lavado a cargo de la empresa; «tabla de 2025, la última publicada» sin la palabra ultraactividad;
  modificación de 2026 que **sí modifica** los arts. 15-17 y **no altera funciones**, con los 5 de 10 puestos
  renombrados; RD 1021/2022 = BOE-A-2022-21681. **Todo conforme a la verificación legal.**
- **Frontera con el hermano:** las citas «Manual del Manager, cap. N» apuntan al capítulo correcto en los
  ocho casos (cap. 7 conversación de corrección y guion de la propuesta, cap. 8 arquitectura del convenio,
  caps. 2 y 3 cuadro financiero, cap. 13 polivalencia y cross-training, cap. 16 conflicto cocina-sala —**no
  el 18**—, cap. 19 local y excedente, cap. 20 plan de 90 días). Ningún epígrafe repite una tesis del hermano.

---

*Refutación escrita el 2026-09-06 leyendo los dos documentos enteros, la caché por bloques, el guion y las
celdas de los siete xlsx. Temperatura de CPU vigilada antes de cada python (máx. 50,4 °C).*

Via: Claude Code
