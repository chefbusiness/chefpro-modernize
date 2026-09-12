# Refutación de los 9 libros de Excel — «Cómo Montar una Chocolatería» (2026-09-12)

> Refutador adversarial de los xlsx de `scripts/productos-digitales/guia-chocolateria/build/`, dos lentes en un
> solo pase: **(A) fórmulas y convenciones** y **(B) dominio, coherencia y legal**. El encargo era TUMBARLOS, no
> confirmarlos. Cada libro se abrió **dos veces** (fórmulas y `data_only`), uno cada vez, y las cadenas clave se
> recalcularon con **pycel** evaluando la salida ANTES de tocar la entrada. Contrastado contra
> `guia-chocolateria-SPEC.md` (§2.2, §2.3, §2.4, §2.6, §3, D19-D53), `guia-chocolateria/datos_ejemplo.py`
> (importado, 4.850 líneas), `auditorias/guia-chocolateria-verificacion-legal-2026-09-12.json` (109 fichas
> `CHN-*`) y los nueve `mapa-*.json`. Térmica: `istats cpu temp` entre ejecuciones, un python cada vez,
> máximo registrado **41,4 °C**.
>
> **Veredicto: CORREGIR ANTES.** 24 hallazgos: **4 altos · 10 medios · 10 bajos**. El motor de cálculo está
> limpio de verdad —0 funciones prohibidas, 0 referencias externas, 0 divisiones sin `IFERROR`, 0 celdas verdes
> vacías en 2.317 verdes, 0 errores `#` en 6.360 fórmulas— y las cuatro filas de CUADRE que se probaron
> disparan bien. Lo que no aguanta la refutación es la **coherencia entre libros**: el pack publica hoy
> **dos demandas de campaña**, **dos food cost por referencia**, **dos veredictos opuestos del art. 3** y una
> **columna de vida útil congelada** que el lector no puede arreglar. Y el libro 9 sale de fábrica
> **clasificando a seis empresas reales en la cadena EUDR**, que es justo lo que `datos_ejemplo` dejó en blanco
> a propósito.

## 0. Lo que NO se pudo tumbar (verificado, no asumido)

| Comprobación | Resultado |
|---|---|
| Fórmulas totales | **6.360** en los 9 libros (197 · 250 · 1.254 · 1.694 · 859 · 440 · 1.071 · 357 · 238) |
| Errores `#REF!` / `#DIV/0!` / `#VALUE!` en `data_only` | **0** |
| Fórmulas sin caché | 102, y **todas** son la convención «sin dato» = `""` (1 · 16 · 0 · 0 · 56 · 2 · 3 · 6 · 18); comprobadas una a una: todas nacen de un `IF(...="","",…)` o de una división por cero declarada |
| Funciones prohibidas (`INDIRECT` · `COUNTA` · `PMT` · `OFFSET` · `XLOOKUP` · `LET` · `LAMBDA` · `RANK` · `NETWORKDAYS` · `IRR`) | **0** en los 9 libros. La cuota del préstamo del libro 7 va como anualidad algebraica (`Financiación!B22`) y la ruta crítica del 8 con aritmética de índices de mes |
| Referencias externas entre libros (`[`, `.xlsx!` dentro de fórmula) | **0** de 6.360. La regla transversal de §2.3 se cumple en todo el pack |
| Divisiones sin `IFERROR` | **0** (las 28 que saltaron en el primer barrido del libro 5 eran barras dentro de literales de texto) |
| Constantes tecleadas dentro de fórmula | **0 de verdad**. Las que saltan son conversiones (`/60`, `*12`, `/7`), índices de mes, y banderas `1/0` de columnas auxiliares. El `0,01` de `CAPEX por Bloque!L54` es tolerancia de redondeo del cuadre, no un parámetro de negocio |
| DV de tipo lista contra rango | **56 de 56**, todas al rango de su propia hoja, **0 listas con comas**, **0 sin `showErrorMessage`** |
| Celdas verdes | **2.317**; **0 vacías**, **0 bloqueadas**, **0 con fórmula dentro**, **0 celdas no verdes desbloqueadas con valor** → la regla 2 de §2.3 se cumple sobre el fichero, no sobre el mapa |
| Semáforos | 158 reglas de formato condicional; **0** comparaciones numéricas sin `ISNUMBER`. Las 5 que saltaron en el libro 8 son `=$B$26="No"`, comparación de TEXTO, donde `ISNUMBER` no aplica |
| WinAnsi (cp1252, tolerando el espacio fino U+202F) | **0 caracteres fuera** en los 9 libros. Ni `≤`, ni `≈`, ni `→`, ni guion no separable, ni CJK |
| `print_setup` A4 (`paperSize 9`) | **69/69 hojas** |
| Protección de hoja **sin contraseña** | **69/69** |
| Metadata | `creator` y `lastModifiedBy` = `AI Chef Pro` en los 9; `title` y `subject` presentes y coherentes en los 9 |
| «Instrucciones» la primera · «celdas verdes = campos editables» · línea de versión exacta · bio anclada · nota de desproteger · cadencia de uso | **9/9 en los seis puntos**. La línea `Versión 1.0 · septiembre 2026 · aichef.pro/guia-chocolateria-obrador · info@aichef.pro` es idéntica carácter a carácter en los nueve |
| Mapas | 103 · 76 · 60 · 129 · 41 · 93 · 87 · 76 · 61 etiquetas → **todos ≥ 25**. **0 refs a celda inexistente**, **0 refs a hoja inexistente**, **0 refs a otro fichero**. Los únicos desajustes de valor son fechas serializadas como `"YYYY-MM-DD"` (correcto) y la entrada `_notas` (hallazgo B2) |
| Formatos numéricos | **0** celdas de texto con formato `€`, **0** fechas sin formato de fecha, **0** números de cuatro cifras en `General`. Los 30 porcentajes >150 % son la columna «Subida máxima que aguanta» del libro 3, y son reales |
| Notas legales | **201** con la cabecera «Verificado el 12-09-2026 · … · URL»; **0 sin URL**; la única con otra fecha es `Ruta Doméstica!B20` (10-09-2026), que es el origen (d) de §3 (`PA-29c` reutilizada de Pastelería) y está bien |
| Ids `CHN-*` citados | **0 inexistentes** contra las 109 fichas de la verificación legal |
| Juego de datos «La Almendra» | **75 m²** repartidos 26+6+8+5+22+8 exactos · **45/22/8** por bloque · **28 referencias** en 10+6+3+5+4 familias · plantilla **3 personas / 2,5 jornadas** con los tres nombres literales del kit (Encargado · Chocolatero · Dependiente) · **15 pagas** · coste hora de obrador **18,4917 €** idéntico en `datos_ejemplo` y en el libro 4 |
| Cadena de dinero libro 2 ↔ libro 7 | **Idéntica por construcción y verificada al céntimo**: CAPEX sin fondo 89.219,35 · fondo 61.425,95 · inversión total **150.645,30 en los dos libros** · IVA soportado 17.912,86 · desembolso 168.558,16 · aportación propia 78.158,16 (libro 2 `IVA y Tesorería!B27`) = `0. Supuestos!B40` del libro 7. **El fondo de maniobra se calcula UNA sola vez, en el libro 7** |
| Ventas del año de crucero | **199.087,94 €** en `datos_ejemplo.cuenta_resultados_crucero()`, en `PyG 3 Años!C11`, en `Canales y Punto Muerto!I11` y en `Peso sobre el Año!E19` del libro 6. Coeficientes de estacionalidad suman **12,0** y los días de apertura **304** |
| Gastos fijos y fondo | `PyG 3 Años!C31`/12 = **10.237,658341** = `Inversión Inicial!B14` = `datos_ejemplo.gastos_fijos_mensuales()`; × 6 meses = **61.425,950047** = `datos_ejemplo.fondo_maniobra()` |
| Precio de cobertura (la celda más crítica) | Vive **sólo** en `sensibilidad-al-precio-del-cacao.xlsx!Coste de Cobertura!G7`; 25,02 €/kg CON IVA → **22,745454 € base imponible**; el libro 4 (`Parámetros!B27`) y el libro 7 (`PyG 3 Años!B71`) copian **22,7455** y sus dos filas de CUADRE dan «CUADRA». Probado con pycel: teclear los 25,02 CON IVA enciende los dos cuadres |
| Plazo crítico 9 → 8 | `Equipamiento!I53` = **10 semanas** = valor por defecto de `Cronograma y Ruta Crítica!C48`; el cuadre dispara a 45 semanas |
| Desviación CAPEX 2 → 9 | `CAPEX por Bloque!L33` = **21.060,00 €** = `Equipamiento!I46` = `datos_ejemplo.equipamiento_bloque_sin_iva('Equipo de templado y moldeado')` |
| D21 (ruta doméstica) | **Cumplido y bien escrito.** Los tres requisitos del art. 13.9 sólo se activan si la letra e) está en «Sí»; el requisito 2 NO tiene semáforo a propósito («inventarse un umbral de kg/m² sería publicar criterio como norma») y la cita de `PA-29c` es literal |
| D34 (art. 3 como árbol) | **Cumplido**: puerta de entrada delante, tres condiciones ACUMULATIVAS, dos vías ALTERNATIVAS dentro de «marginal», y el aviso expreso «LOS 500 KILOS NO INCLUYEN TU MOSTRADOR» |
| D37 (dos capas) | **Cumplido y con las dos bases en el sentido correcto**: el 25 % se calcula sobre el PESO TOTAL con el relleno dentro en bombón y chocolate relleno; en 1.6-1.9 se declara el descuento de los añadidos. Bajar BC1 a 2 g de chocolate enciende «NO CUMPLE» |
| D47 (etiquetado o granel) | **Cumplido**: la celda de dos valores cambia la columna de salida y la referencia normativa; el art. 4.2 sólo se invoca en la vía «envasado con etiqueta» |
| D48, mitad b) | **Cumplida**: la tabla de CLIENTES existe, cuenta minoristas por TIPO y publica la conservación a cinco años |
| D31 (vitrina) | **Cumplido**: el objetivo 16-18 °C no sale nunca en rojo; la única alarma es >20 °C, y con 24 °C se enciende |
| D33 (clima) | **Cumplido**: cero coeficientes de carga térmica, semáforo de coherencia de tres cifras tecleadas y ficha de diez preguntas al instalador |
| D19 (644.5) | **Cumplido**: los cinco canales con «sí / no / no lo sé», la nota literal del epígrafe delante y la pregunta redactada para el asesor |
| Cadmio | **Cumplido**: el bombón **no** tiene límite propio, se declara la regla de alimentos compuestos y **no se publica ninguna cifra del Anexo I** |
| EUDR | Fechas correctas contra `CHN-21` y `CHN-22`: 30-12-2026 general, 30-06-2027 sólo si eres **operador** micro/pequeño; el paso «operador posterior» va marcado como **INFERENCIA declarada**; el nº de DDS sólo se pide en la rama «operador» |
| Pruebas de comportamiento con pycel (salida evaluada ANTES de tocar la entrada) | **21 cadenas en los 9 libros, todas mueven.** Libro 1: bajar el puesto de envasado 512→160 cambia veredicto, campañas y peor déficit; subir agosto a 44 °C enciende «INCOHERENTE». Libro 2: subir la atemperadora mueve bloque, total, CAPEX depurado, Resumen y aportación propia; marcar «lleva IVA» reparte base e IVA; pisar la fila del fondo enciende «NO CUADRA» en dos hojas. Libro 3: cambiar la base declarada mueve la base imponible y los cinco escenarios. Libro 4: doblar el PVP mueve food cost, margen y ticket; subir la merma mueve coste y margen. Libro 5: 24 °C enciende la alarma; 60 días enciende «Por encima del plazo del kit». Libro 6: teclear otra capacidad enciende «REVISA». Libro 7: subir clientes mueve P&L; subir meses de colchón mueve fondo e inversión total; CAPEX distinto enciende «REVISA». Libro 8: los cuatro árboles legales responden y el cuadre del plazo vuelca la fecha. Libro 9: el cuadre del CAPEX y el del plazo disparan |

---

## Lente A — Fórmulas, convenciones y estructura

### A1 · ALTA · Los libros 1 y 6 publican DOS demandas y DOS déficits de campaña distintos para el mismo caso
**Libros:** `capacidad-obrador-y-clima.xlsx` y `campanas-y-valle-del-ano.xlsx`.
**Celdas:** libro 1 `Cuello de Botella!D18:F29`, `B31`, `B32`, `B34`; libro 6 `Capacidad vs Demanda del Pico!F12:H23`, `B26`, `B27`.

**Problema.** Los dos libros calculan, cada uno por su cuenta y con modelos distintos, la demanda diaria y el
déficit de las doce campañas, y publican cifras que no coinciden:

| Campaña | Libro 1 (`D`) | Libro 6 (`F`) | Déficit libro 1 (`F`) | Déficit libro 6 (`H`) |
|---|---|---|---|---|
| Diciembre — Navidad | **1.339,95** | **1.399,68** | −827,95 | 887,68 |
| Febrero — San Valentín | 1.212,56 | 1.139,64 | −700,56 | 627,64 |
| Enero — Reyes | 934,19 | 474,24 | −422,19 | 0,00 |
| Abril — Pascua | 797,37 | 537,76 | −285,37 | 25,76 |
| Agosto | 476,53 | 287,20 | +35,47 | 0,00 |
| **Campañas que no aguantas** | **10** (`B31`) | **7** (`B26`) | | |

El libro 1 multiplica un objetivo diario (471,814) por un «factor de campaña» que su propio constructor
declara derivado (`C18:C29`, celda verde); el libro 6 reparte una base de 472 por el coeficiente mensual de
`Peso sobre el Año` y le suma las unidades incrementales del producto estrella. Son dos modelos legítimos,
pero **§2.2 asigna el déficit de capacidad al libro 6** y al libro 1 sólo «bombones/día por equipo» y «el
equipo que limita». Las dos versiones están en sus `mapa-*.json`, así que `documentos.py` puede citar
cualquiera de las dos y el capítulo 18 puede decir 1.340 mientras el xlsx que el comprador abre dice 1.400.

Peor: el **cruce 6 ← 1 de D32 es «déficit de capacidad del pico»** y lo que de verdad viaja es la
**capacidad** (`Cuello de Botella!B7` → `Capacidad vs Demanda del Pico!B6`). El déficit que el libro 1 publica
en `B32` lleva la nota «ES LA CIFRA QUE VIAJA AL LIBRO 6» (`J33`) y **no la trae nadie**.

**Fix (en el generador).** `gen_capacidad-obrador-y-clima.py`: eliminar el bloque `Cuello de Botella!A16:J34`
(las doce filas de campaña, el recuento `B31`, el peor déficit `B32:B33` y el veredicto `B34`) y sus etiquetas
del mapa, dejando en el libro 1 sólo capacidad por equipo, cuello de botella y veredicto del día normal, que
es lo que §2.2 le asigna. Corregir la nota `J33` para que apunte a lo que sí viaja (`B7`). Si en cambio se
decide que el bloque de campañas es del libro 1, hay que regenerar el 6 sin sus filas 11-27 y rehacer el cruce
para que viaje el déficit, no la capacidad — pero entonces hay que tocar `datos_ejemplo.CRUCES[0]`.

### A2 · ALTA · La columna de vida útil que sostiene el veredicto de los surtidos está congelada y bloqueada
**Libro:** `vida-util-rellenos-y-rotacion.xlsx`.
**Celdas:** `Vida Útil Declarada!L40:L43` («Pieza más corta del surtido (días)»), y los veredictos `M40:M43`.

**Problema.** Las cuatro celdas son **constantes tecleadas = 10**, sin fórmula, **bloqueadas** y **sin relleno
verde**. No son entrada (el lector no puede tocarlas) ni salida (no se recalculan). Probado con pycel:
bajando la vida útil declarada de BC1 (`G16`) de 10 a 3 días, `G44` («la más corta de la carta») baja a 3,
pero `L40:L43` siguen diciendo **10** y los cuatro veredictos `M40:M43` no se mueven. La caja de 12 bombones
sigue publicando que su pieza más corta dura 10 días cuando dentro lleva una de 3.

Y el veredicto que emiten de fábrica ya es engañoso: `M40` dice «**Por debajo del plazo del kit: conservador,
y es decisión tuya**» comparando contra la familia `C40` = «Bombones de ganache con **nata UHT**, sorbato o
alcohol» (4-8 semanas), cuando la pieza que manda en esa caja es BC1, **ganache de nata fresca** (10-15 días).
Los 10 días no son conservadores: son el máximo posible.

Es la columna que sostiene la promesa del libro («cuánto dura cada bombón») y la única de las tres reglas de
surtido que no se propaga: la aw sí se hereda (`Tipo de Relleno y aw` da 0,88 a las cuatro cajas, que es la de
BC1) y la vida útil sembrada también, pero la comparación se hace contra un número muerto.

**Fix (en el generador).** `gen_vida-util-rellenos-y-rotacion.py`: convertir `L40:L43` en fórmula sobre las
piezas que componen cada caja —el libro 4 ya publica la composición en `Unidad vs Caja!C7:F16`, así que el 5
puede replicar la tabla de composición como columnas auxiliares y resolverlo con `MIN` sobre las filas cuya
cantidad en esa caja sea >0—, o, si se prefiere no duplicar la composición, dejarla como **celda verde** con
su valor por defecto declarado y la nota «cópialo de la pieza más corta que metes dentro». Y corregir `C40:C43`
para que la familia del kit sea la de la pieza más restrictiva, no la de nata UHT.

### A3 · MEDIA · Tres de las ocho celdas de cruce no citan la CELDA de origen que exige D32
**Libros:** 2, 4 y 9.
**Celdas:** `calculadora-capex-chocolateria.xlsx!CAPEX por Bloque!C51`,
`carta-de-apertura-y-escandallo-chocolate.xlsx!Parámetros!A25`,
`checklist-equipamiento-y-proveedores-cacao.xlsx!Equipamiento!A46`.

**Problema.** §2.3 fija la redacción: «trae aquí la cifra de `<fichero>.xlsx!<Hoja>!<Celda>`». Cinco de las
ocho la cumplen (`…!Cuello de Botella!B7` ×2, `…!Coste de Cobertura!G7`, `…!CAPEX por Bloque!L44`,
`…!Equipamiento!I53`). Las otras tres se quedan en la hoja:

- `C51`: «Trae aquí el fondo de maniobra de `plan-financiero-3-anos-chocolateria.xlsx!Inversión Inicial`» — sin celda (es `B16`).
- `A25`: «…de `sensibilidad-al-precio-del-cacao.xlsx!Coste de Cobertura` (columna de base imponible…)» — sin celda; la celda sí aparece, pero escondida en la columna `F27:F30` de la tabla de abajo.
- `A46`: «…de `calculadora-capex-chocolateria.xlsx!CAPEX por Bloque`» — sin celda (es `L33`).

En una hoja de 69 filas con columnas auxiliares, «búscalo en esa hoja» no es lo mismo que «cópialo de esa
celda», y el gate que §2.3 encarga a `gate_libros.py` cuenta exactamente esa cadena.

**Fix (en el generador).** Añadir la referencia completa en los tres rótulos:
`gen_calculadora-capex-chocolateria.py` → `!Inversión Inicial!B16`;
`gen_carta-de-apertura-y-escandallo-chocolate.py` → `!Coste de Cobertura!G7` (y G8/G9/G10 en la tabla);
`gen_checklist-equipamiento-y-proveedores-cacao.py` → `!CAPEX por Bloque!L33`.

### A4 · MEDIA · El cruce 7 ← 2 apunta a una celda de trabajo en vez de a la línea publicada del «Resumen»
**Libro:** `plan-financiero-3-anos-chocolateria.xlsx`.
**Celda:** `Inversión Inicial!A6` (rótulo) y `B6` (verde).

**Problema.** El rótulo dice «trae aquí la cifra de `calculadora-capex-chocolateria.xlsx!CAPEX por Bloque!L44`».
La SPEC §2.3 y `datos_ejemplo.CRUCES[5]['hoja_origen']` dicen **`Resumen`**, y esa hoja **existe** en el libro 2
y publica exactamente esa línea en `Resumen!A7`/`B7` («CAPEX SIN el fondo de maniobra» = 89.219,35, fórmula
`='CAPEX por Bloque'!L44`). El valor es el mismo, así que el cuadre no se entera; lo que falla es que se manda
al comprador a una fila intermedia de una hoja de cálculo de 69 filas en lugar de a la hoja «Resumen», que es
la que la propia SPEC define como «las cifras que hay que llevar al banco».

⚠️ La duda que declaró el constructor del libro 7 —«NO hay hoja «Resumen» en su libro»— **es falsa**:
`calculadora-capex-chocolateria.xlsx` tiene siete hojas y la séptima se llama `Resumen`.

**Fix (en el generador).** `gen_plan-financiero-3-anos-chocolateria.py`: cambiar el rótulo a
`calculadora-capex-chocolateria.xlsx!Resumen!B7` y ajustar la nota `D6`. El valor por defecto no cambia.

### A5 · MEDIA · `datos_ejemplo.CRUCES` nombra cuatro hojas que no existen en los ficheros construidos
**Fichero:** `guia-chocolateria/datos_ejemplo.py`, lista `CRUCES`.

**Problema.** El gate que §2.3 encarga («cada celda verde “trae aquí la cifra de X” tiene su fila de CUADRE en
la misma hoja: deben salir OCHO, contadas contra esta tabla») no puede construirse contra `CRUCES` tal y como
está, porque cuatro de las ocho entradas nombran hojas inexistentes:

| Cruce | `CRUCES` dice | La hoja real es | Por qué |
|---|---|---|---|
| 4 ← 3 y 7 ← 3 | `hoja_origen = 'Coste de Cobertura por Referencia'` | **`Coste de Cobertura`** | 33 caracteres, y Excel corta en 31 |
| 4 ← 3 | `hoja_receptor = 'Escandallo por Molde/Tanda'` | **`Parámetros`** | La barra está prohibida en un nombre de hoja, y además la celda verde vive en «Parámetros», que es donde está la tabla de precios de la que bebe el libro |
| 7 ← 1 | `hoja_receptor = 'Tesoreria 12 meses'` | **`Tesorería 12 meses`** | Sin tilde |
| 7 ← 3 | `hoja_receptor = 'PyG 3 Anos'` | **`PyG 3 Años`** | Sin tilde |

**Fix (en el generador).** Corregir las cuatro entradas de `CRUCES` en `datos_ejemplo.py` con los nombres
reales (los `mapa-*.json` ya los llevan bien) **antes** de escribir `gate_libros.py`, y que el gate resuelva la
hoja por el nombre real, no por el literal de la SPEC. La SPEC §2.2/§2.3 hay que actualizarla en los mismos
cuatro sitios.

### A6 · MEDIA · El libro 2 teclea el fondo de maniobra DOS veces y su rótulo de partida habla de meses
**Libro:** `calculadora-capex-chocolateria.xlsx`.
**Celdas:** `CAPEX por Bloque!I28`, `J28`, `K28` (verdes, 61.425,95) y `CAPEX por Bloque!L51` (verde,
61.425,95); rótulo `C28`.

**Problema.** El fondo de maniobra entra en el libro por dos puertas verdes distintas: la fila del bloque
(`K28`, que es la que suma al CAPEX) y la celda del cruce (`L51`, que es la que lleva el rótulo «trae aquí…»).
La fila de CUADRE compara **la una contra la otra**, es decir, **el libro contra sí mismo**, no contra el libro
7. Funciona como red (probado: pisar `K28` enciende «NO CUADRA» en `L54` y en `Resumen!B16`), pero obliga al
comprador a teclear el mismo número dos veces y deja abierta la vía de teclearlo mal en las dos.

Y el rótulo de la partida, `C28`, dice «**Colchon de tesoreria (meses de gastos fijos)**» en una línea cuyo
importe está en euros, justo donde R4-A1 prohíbe que el libro 2 pida «meses de colchón».

Detalle menor del mismo bloque: la nota `Resumen!D8` dice «No es prudencia: **es inversión**, y por eso está
dentro del total» pegada a un rótulo que dice «Del cual, fondo de maniobra (**es caja, no inversión**)».

**Fix (en el generador).** `gen_calculadora-capex-chocolateria.py`: hacer que `I28`, `J28` y `K28` sean
fórmulas `=L51` (dejando el cruce como única celda verde del concepto), o al revés; renombrar `C28` a
«Fondo de maniobra traído del libro 7 (€)»; y reescribir `D8` para que no contradiga a `A8`.

### A7 · BAJA · Un mapa publica una etiqueta cuyo valor es cadena vacía
**Libro:** `calculadora-capex-chocolateria.xlsx` · **mapa:** `mapa-calculadora-capex-chocolateria.json`.
**Celda:** `IVA y Tesorería!B36`, etiqueta «Coste anual del impuesto al plástico», `"valor": ""`.

**Problema.** La fórmula devuelve `""` a propósito (no hay plástico importado), `inject_cache` la deja en
`None` y el mapa la publica con valor vacío. `documentos.py` resuelve las referencias del guion con
`data_only=True`: un capítulo que cite esa etiqueta imprimirá nada, sin aviso.

**Fix (en el generador).** O se saca del mapa, o se publica en su lugar la celda del veredicto
(`IVA y Tesorería!B37` = «Sin alerta»), que sí tiene contenido en los dos estados.

### A8 · BAJA · Los nueve mapas llevan una entrada `_notas` con tipo inválido y valor que no casa
**Mapas:** los nueve.
**Entrada:** `"_notas": {"ref": "<libro>.xlsx!Instrucciones!A1", "valor": "<texto de la nota>", "tipo": "nota"}`.

**Problema.** `tipo` sólo admite `entrada|salida|parametro` según el encargo; `"nota"` no está. Y el `valor`
declarado no es el de la celda (`Instrucciones!A1` contiene el título de la hoja), así que cualquier gate que
compare mapa contra fichero marca nueve desajustes falsos. Además infla el recuento de etiquetas en uno.

**Fix (en el generador).** Mover el texto a una clave hermana fuera del diccionario de etiquetas
(p. ej. `{"_meta": {...}, "etiquetas": {...}}`) o quitar la entrada; y que el gate de recuento cuente sólo las
entradas con `tipo` válido.

### A9 · BAJA · Once títulos de hoja con Title Case mal aplicado
**Libros:** los 9 menos el 8 (que tiene el suyo).
**Celdas:** la `A1` de cada hoja.

**Problema.** Las **pestañas** están bien (`CAPEX por Bloque`, `Capacidad vs Demanda del Pico`, `Escandallo por
Molde y Tanda`…), pero el título que se imprime en `A1` pasa por un `title()` ingenuo y sube preposiciones y
pronombres:

| Libro | `A1` publicado | Debería |
|---|---|---|
| 2 | `CAPEX Por Bloque` | `CAPEX por Bloque` |
| 6 | `Capacidad Vs Demanda del Pico` | `Capacidad vs Demanda del Pico` |
| 1 | `Capacidad Por Equipo` | `Capacidad por Equipo` |
| 4 | `Escandallo Por Molde y Tanda` · `Unidad Vs Caja` | `…por…` · `…vs…` |
| 3 | `Coste de Cobertura Por Referencia` | `…por Referencia` |
| 5 | `Lote y Merma Por Caducidad` | `…por Caducidad` |
| 9 | `Clientes a los Que Suministras: el Registro del Art. 5.3.b)` | `…a los que Suministras: El Registro…` |
| 7 | `Inversión Inicial: la Cifra Que Viene y la Que Se Dota Aquí` · `…: las Dos Líneas Que No Dependen del Cacao` | `…: La Cifra que Viene y la que se Dota Aquí` · `…: Las Dos Líneas que No Dependen…` |
| 8 | `EUDR: Tu Papel en la Cadena y Qué Fecha Te Corre` | `…y Qué Fecha te Corre` |

Es la regla de Title Case español del proyecto (significativas en mayúscula; `de/por/y/para/que/se/vs` en
minúscula) y, además, tras dos puntos la palabra siguiente sí va en mayúscula, que es justo lo contrario de lo
que hacen los dos títulos del libro 7.

**Fix (en el generador).** El helper de título de `_comun_chocolateria.py` (o el que use cada `gen_*`) tiene
que respetar una lista de palabras funcionales y capitalizar después de `:`. Un solo arreglo en el helper
corrige los once.

### A10 · BAJA · Congelado de paneles y pie de versión inconsistentes entre libros
**Libros:** los 9.

**Problema.** Dos detalles de acabado que delatan cinco manos distintas: (a) **`freeze_panes`**: los libros 1,
2, 3, 4 y 6 no lo llevan en **ninguna** hoja, el 7 en 7 de 11, el 5 y el 8 en todas menos una y el 9 en todas
menos dos; en tablas de 28 a 44 filas con cabecera, sin congelar se pierde el encabezado al primer scroll.
(b) **Pie de versión**: los libros 4, 6 y 9 repiten la línea `Versión 1.0 · …` al pie de todas sus hojas; los
otros seis sólo en «Instrucciones». La convención sólo exige la de «Instrucciones», así que ninguna está mal,
pero el pack se lee como tres productos distintos.

**Fix (en el generador).** Bajar las dos decisiones a `_comun_chocolateria.py` (un `cerrar_hoja()` que aplique
`freeze_panes` en la fila de cabecera y escriba el pie) y llamarlo desde los nueve generadores.

---

## Lente B — Dominio, coherencia entre libros y legal

### B1 · ALTA · El libro 9 clasifica de fábrica a seis empresas reales en la cadena EUDR, y `datos_ejemplo` lo dejó en blanco a propósito
**Libro:** `checklist-equipamiento-y-proveedores-cacao.xlsx`.
**Celdas:** `Proveedores y EUDR!G7:G12`, y sus salidas `N7:N12` y `O7:O12`.

**Problema.** `datos_ejemplo.PROVEEDORES` define la tupla como
`(nombre, categoria, url, fuente, papel_eudr (vacio: lo rellena el lector), nota)` y los **seis** proveedores
llevan `papel_eudr = ''`. D48 dice lo mismo: «`PROVEEDORES` lleva la columna «operador / operador posterior /
comerciante» **VACÍA para que la rellene el lector**». El libro publicado siembra las seis con
«**operador posterior**», y de ahí salen dos columnas calculadas que dicen, con nombre y apellidos:

- `N7` (Callebaut / Barry Callebaut Ibérica): «Sus datos, su dirección y el producto: **el nº de DDS NO se le pide** por el art. 5.3.a)».
- `N8` (Asociación Chocolate Bean to Bar España, cuya categoría en la propia hoja es «**Grano de cacao** para bean-to-bar»): lo mismo.
- `O7:O12`: «**Completa** para su papel en la cadena» para los seis.

Dos problemas encadenados, y los dos son legales:

1. **Es exactamente la rama equivocada.** `CHN-23` define operador como quien hace la primera comercialización
   en el mercado de la Unión. Un grupo que importa grano de cacao y una asociación que canaliza **grano** son
   el caso de OPERADOR, no de operador posterior; y `CHN-24`, art. 5.3.a), obliga a guardar el nº de referencia
   de la DDS **precisamente** cuando el proveedor es operador. El libro sale de fábrica diciéndole al comprador
   que **no se lo pida**, que es el error que D48 vino a cerrar por el lado contrario («prohibido “pide a todos
   tus proveedores el número de su DDS”») y que aquí se ha cometido por el otro extremo.
2. **Tres de los seis no están en la cadena EUDR en absoluto.** Utilcentre vende maquinaria, SelfPackaging
   cajas y Gift Campaign regalo corporativo: ninguno comercializa producto pertinente del Anexo I. Asignarles
   un papel EUDR y un semáforo «Completa» es aplicar el reglamento fuera de su ámbito.

**Fix (en el generador).** `gen_checklist-equipamiento-y-proveedores-cacao.py`: sembrar `G7:G12` con
«**No lo sé**» (valor que el desplegable de la hoja ya ofrece y que respeta la regla 2 de celda verde no vacía
sin inventar la calificación de un tercero), y que `N` y `O` devuelvan «Pregúntaselo por escrito antes de
comprar» mientras el papel no esté resuelto. Para las tres líneas que no venden producto pertinente, sacarlas
del árbol EUDR con una columna «¿te vende producto del Anexo I?» o dejar su fila de papel en blanco declarado.

### B2 · ALTA · Los libros 8 y 9 publican veredictos OPUESTOS del art. 3 con el mismo juego de datos
**Libros:** `checklist-legal-licencias-y-cacao.xlsx` y `checklist-equipamiento-y-proveedores-cacao.xlsx`.
**Celdas:** libro 8 `Suministro a Otros Minoristas!B6` (verde, «No»), `B7`, `B41`, `B42`; libro 9
`Clientes a los que Suministras!E23` y `E27`.

**Problema.** El libro 9 cuenta por TIPO de cliente y publica:

> `E23` = **1** minorista de distinta titularidad · `E27` = «**Suministras a otros minoristas: resuelve los TRES semáforos del art. 3 en el libro 8**».

El libro 8, abierto en el libro 8, responde:

> `B41` = «**El art. 3 no te aplica: no suministras a otros minoristas de distinta titularidad**» · `B42` = «Nada de esto te aplica».

La causa es la celda verde `B6` («¿Suministras bombones de producción propia a establecimientos MINORISTAS de
distinta titularidad?»), sembrada con **«No»**, cuando `datos_ejemplo.CLIENTES_B2B` incluye
`('Tienda gourmet La Despensa', 'Minorista de distinta titularidad', …)` y **la propia hoja del libro 8** la
lista en su tabla de destinatarios (`A13`, 9 kg/semana, 3 % del volumen, 12 km). El libro contradice su propia
tabla de ejemplo tres filas más abajo.

Consecuencia medida: con `B6` = «No», **las tres condiciones del art. 3 quedan decorativas** (`B26`, `B33`,
`B37` calculan «Sí» pero `B41` las ignora) y el veredicto que el guion puede citar del mapa es el equivocado
para «La Almendra». Probado con pycel: poniendo `B6` = «Sí», el veredicto pasa a «Cumples las tres: sigues
FUERA del RGSEAA, con la declaración responsable y el registro del art. 3.5», que es la lectura correcta del
caso, y `B42` pasa a pedir la declaración responsable y el registro.

**Fix (en el generador).** `gen_checklist-legal-licencias-y-cacao.py`: sembrar `B6` = «Sí» (es lo que dice el
juego de datos) y, para que no vuelva a divergir, derivar el valor por defecto de
`len([c for c in D.CLIENTES_B2B if c[1] == 'Minorista de distinta titularidad']) > 0` en vez de escribirlo a
mano. Añadir al gate del pack la comprobación cruzada `libro 9!E23 > 0 ⟺ libro 8!B6 = "Sí"`.

### B3 · MEDIA · Los libros 3 y 4 publican DOS food cost por referencia, y discrepan sobre si TB4 está rota
**Libros:** `sensibilidad-al-precio-del-cacao.xlsx` y `carta-de-apertura-y-escandallo-chocolate.xlsx`.
**Celdas:** libro 3 `Escenarios de Precio!G16:G43` y el contador `G44`; libro 4
`Coste Hora y Mano de Obra!Q7:Q34`.

**Problema.** Las dos columnas se llaman «Food cost» y se calculan sobre bases distintas: el libro 3 divide el
coste de materia **sin merma** (`F16 = D16 + C16*D$7`) entre el PVP sin IVA; el libro 4 divide el coste de
materia **con la merma no recuperable** (`L7 = Escandallo!O70`) entre el mismo PVP. Las 28 referencias salen
sistemáticamente más bajas en el libro 3, entre 6 y 116 puntos básicos, y en una la diferencia cruza el umbral
de la casa:

| Id | Food cost libro 3 | Food cost libro 4 | Techo (`B41`/`B10`) | |
|---|---|---|---|---|
| TB1 tableta de origen | 48,50 % | 48,99 % | 35 % | rota en los dos |
| **TB4 tableta con almendra marcona** | **34,64 %** | **35,35 %** | 35 % | **el 3 dice que aguanta, el 4 dice que no** |
| TB5 | 31,10 % | 31,74 % | 35 % | aguanta en los dos |

Por eso el contador `Escenarios de Precio!G44` publica **6 referencias rotas hoy** donde con la base del libro
4 son **7**. Y el libro 3 es justamente el que decide «la referencia que primero se rompe» y «la subida máxima
que aguanta»: con la base sin merma, todas las subidas máximas salen optimistas.

**Fix (en el generador).** `gen_sensibilidad-al-precio-del-cacao.py`: aplicar en la columna de coste de
materia la misma merma no recuperable que usa el libro 4 (`datos_ejemplo.coste_materia_con_merma`), o —si se
prefiere mantener el escenario «limpio»— renombrar las columnas a «Coste de MATERIA sobre PVP (sin merma)» y
publicar al lado la equivalencia, para que nadie compare dos números que se llaman igual. La primera opción es
la que respeta «un concepto, una fuente».

### B4 · MEDIA · La base de amortización del libro 7 no coincide con la nota que la explica
**Libro:** `plan-financiero-3-anos-chocolateria.xlsx`.
**Celdas:** `Inversión Inicial!B11` (verde, 86.619,35), nota `D11`, y la cadena `B26` → `B27` → `PyG 3 Años!C29`.

**Problema.** `D11` dice: «El CAPEX menos la FIANZA (que es un depósito y se recupera) **y menos el primer
pedido de packaging y moldes de consumo** (que son existencias, no inmovilizado)». La cifra sembrada es
89.219,35 − 2.600 = **86.619,35**, es decir, **sólo la fianza**. El bloque «Packaging y moldes» del libro 2
vale **3.004,36 €** (`CAPEX por Bloque!L36` = moldes 804,36 + primer pedido de packaging 2.200) y no se resta.

Efecto medido: la amortización anual (`B27 = B26/10`) sale **8.661,94 €** en vez de **8.361,50 €**, o sea
**300,44 €/año de más** que entran en `PyG 3 Años!C29` → costes fijos `C31` → punto de equilibrio, margen neto,
fondo de maniobra (`= C31/12 × 6`) y, por el cruce 2 ← 7, la inversión total de los dos libros. No cambia el
veredicto (el margen neto sigue en banda), pero es una cifra que el bonus 1 «business plan modelo» copia celda
a celda.

Y hay un segundo problema en la misma celda: el rótulo dice «Inmovilizado amortizable, **traído del libro 2**»
y **el libro 2 no publica esa cifra en ninguna celda** —ni en `Resumen`, ni en `CAPEX por Bloque`—, así que el
comprador no puede ir a buscarla. Lo mismo, en menor grado, con `B10` («IVA soportado total»), que sí existe
(`CAPEX por Bloque!M40` = 17.912,86) y esa está bien citada.

**Fix (en el generador).** O se corrige el número —`B11 = 89.219,35 − 2.600 − 3.004,36 = 83.614,99`— o se
corrige la nota para que diga que sólo se descuenta la fianza. La primera es la coherente con la nota y con
`D26` («Ni la fianza ni el fondo de maniobra se amortizan»). En los dos casos,
`gen_calculadora-capex-chocolateria.py` debería publicar la línea «Inmovilizado amortizable» en su hoja
`Resumen` para que la etiqueta «traído del libro 2» sea cierta.

### B5 · MEDIA · Los libros 7 y 8 resuelven la vía a) del art. 3 con bases distintas y números distintos
**Libros:** `plan-financiero-3-anos-chocolateria.xlsx` y `checklist-legal-licencias-y-cacao.xlsx`.
**Celdas:** libro 7 `Canales y Punto Muerto!B30`, `B31`, `B32`; libro 8
`Suministro a Otros Minoristas!B20`, `B21`, `B22`.

**Problema.** El libro 7 toma «Peso del B2B sobre las ventas (%)» = `B8` = **11 %** —el porcentaje de las
ventas **en euros** del canal «B2B a hostelería»— y lo compara con el 25 % del art. 3.2, publicando
«Marginal por la vía a)». El libro 8 toma «% de tu volumen anual» por destinatario y suma **14 %**, y sólo
cuenta a los minoristas de distinta titularidad.

Tres discrepancias en el mismo test legal: (a) **euros contra volumen** —el art. 3 habla de volumen de
alimentos comercializados, no de facturación—; (b) **todo el B2B contra sólo los minoristas** —hostelería y
regalo corporativo no son «establecimientos minoristas de distinta titularidad», como el propio libro 8
explica en `A3` y `F17`—; (c) **dos números publicados, 11 % y 14 %**, para la misma condición.

**Fix (en el generador).** `gen_plan-financiero-3-anos-chocolateria.py`: quitar el cálculo del art. 3 de la
hoja de canales y dejar sólo el puntero («la vía a) se resuelve en `checklist-legal-licencias-y-cacao.xlsx`,
hoja “Suministro a Otros Minoristas”, y se mide en VOLUMEN, no en euros»), que es lo que ya hace bien la nota
`A33`. Si se quiere conservar un aviso numérico, que compare el peso en euros del canal contra un umbral
propio y declarado, y que no lo llame «vía a) del art. 3.2».

### B6 · MEDIA · Las cajas surtidas heredan la aw y la vida útil de su pieza más delicada, pero no su temperatura
**Libro:** `vida-util-rellenos-y-rotacion.xlsx`.
**Celdas:** `Temperatura y Vitrina!D22` (BC1 = 4 °C), `D46:D49` (CJ1-CJ4 = 18 °C), `F22`, `F46:F49`, `F50`.

**Problema.** El criterio del libro para un surtido —declarado por su constructor y visible en los datos— es
«se comporta como su pieza más delicada»: las cuatro cajas toman la aw de BC1 (**0,88**) y su vida útil
(**10 días**). Pero la temperatura no sigue el mismo criterio: BC1 se declara a **4 °C** y el libro responde
«Nevera de rellenos, no vitrina» y «**No con esta vitrina**»; las cuatro cajas que lo llevan dentro se declaran
a **18 °C** y el libro responde «**Sí, está dentro del rango de tu vitrina**». El recuento `F50` («Referencias
que van a nevera») da **2** cuando por el mismo criterio deberían ser 6.

No es sólo formal: la caja es la unidad de venta real del negocio (familia propia en §3.2) y la que se regala;
publicar que una caja con ganache de nata fresca dentro va a la vitrina a 18 °C contradice la línea del kit que
el propio libro cita en `Tipo de Relleno y aw!J16` («*en refrigeracion a 0-4 grados C y atemperar CERRADOS
antes de abrir*»).

**Fix (en el generador).** `gen_vida-util-rellenos-y-rotacion.py`: sembrar la temperatura declarada de las
cuatro cajas con la **mínima** de las piezas que componen cada una (el mismo criterio que ya se aplica a la aw
y a la vida útil), o —si se decide que un surtido se despacha atemperado— decirlo explícitamente en la nota y
excluir a BC1 de las cajas. Lo que no puede quedar es el mismo criterio aplicado a dos de tres columnas.

### B7 · MEDIA · El producto estrella de Reyes y de Halloween es un huevo de Pascua
**Libros:** `campanas-y-valle-del-ano.xlsx` y `capacidad-obrador-y-clima.xlsx`.
**Celdas:** `Calendario de Campañas!E7` (Enero — Reyes) y `E16` (Octubre — Halloween);
`Cuello de Botella!H18` y `H27` (los mismos meses, con el id `TF1`).

**Problema.** Las dos filas publican como producto estrella «**TF1 - Huevo de Pascua de chocolate con leche,
250 g**». Es el producto que manda el pico de esas campañas, el que fija las unidades incrementales y el que
aparece en el mapa. Un huevo de Pascua en Reyes y en Halloween no es un supuesto discutible: es un error
visible para cualquier chocolatero que abra el fichero, y está en un libro cuyo argumento de venta es
«el calendario de campañas con los euros dentro».

La causa está aguas arriba: la familia «Turrones, figuras y temporada» de `datos_ejemplo.CARTA` tiene cinco
referencias (huevo, mona, hueso de santo, turrón, almendras bañadas) y **ninguna figura de Reyes**, pese a que
§3.2 de la SPEC define la familia como «(huevos de Pascua, monas, **figuras de Reyes**, turrón de chocolate)».
El generador eligió la referencia de temporada más parecida y le tocó el huevo.

**Fix (en el generador).** Lo limpio es en `datos_ejemplo.py`: sustituir una de las cinco por una **figura de
Reyes** (o añadirla y llevar la familia a 6, ajustando el recuento de 28) y, para Halloween, apuntar a una
referencia que exista (BC5 trufa, o TF3). Mientras eso no pase, `gen_campanas-y-valle-del-ano.py` y
`gen_capacidad-obrador-y-clima.py` no deberían publicar un producto estrella cuyo nombre contradice al mes.

### B8 · MEDIA · 170 de 201 notas legales citan la norma pero no el artículo
**Libros:** los 9.

**Problema.** La regla 1 de §2.3 fija la nota: «Verificado el 12-09-2026 · **norma y artículo** · URL». El
recuento por libro de notas que nombran artículo, apartado, anexo o epígrafe:

| Libro | Notas legales | Con artículo | |
|---|---|---|---|
| 4 · carta y escandallo | 38 | **0** | toda la capa de denominaciones del RD 1055/2003 |
| 3 · sensibilidad al cacao | 7 | **0** | incluye el tipo de IVA del 10 % |
| 6 · campañas | 3 | **0** | |
| 9 · equipamiento | 14 | 1 | |
| 1 · capacidad y clima | 12 | 3 | |
| 2 · CAPEX | 14 | 3 | |
| 7 · plan financiero | 24 | 3 | |
| 5 · vida útil | 14 | 2 | |
| 8 · checklist legal | 75 | 19 | el mejor del pack |
| **Total** | **201** | **31** | **170 sin artículo** |

Ejemplo del caso peor: `Denominaciones y Mínimos!E7` sostiene el mínimo del 25 % del bombón con
«Verificado el 12-09-2026 · Real Decreto 1055/2003 … texto consolidado · URL», sin decir que es el ap. 1.13 y
el ap. 4 —que es exactamente la pareja que D37 declara «prohibido invertir»—. Y las siete notas del IVA citan
la Ley 37/1992 entera sin el art. 91.Uno.1.1.º.

**Fix (en el generador).** El helper `nota_legal(id)` debe componer la nota con el campo de artículo de la
ficha (`CHN-*` ya trae `dato` con el artículo dentro en la mayoría de los casos) y **abortar** si el texto
resultante no contiene `art.`, `ap.`, `Anexo` o `Epígrafe`. Es un gate de una línea que arregla los nueve
libros a la vez.

### B9 · BAJA · El libro 4 nombra el tope del 40 % de materias añadidas y no lo calcula, teniendo los gramos
**Libro:** `carta-de-apertura-y-escandallo-chocolate.xlsx`.
**Celdas:** `Denominaciones y Mínimos!F20`, `F21`, `F27`, `F29` (dicen «…con materias comestibles añadidas del
ap. 3 (tope 40 %)»), contra `J20`, `K20` (22 g sobre 100 g), etc.

**Problema.** La hoja calcula con toda corrección el 25 % del ap. 1.13 (capa (a) de D37) y publica el veredicto,
pero el otro mínimo que nombra —el tope del 40 % de materias añadidas del ap. 3, que afecta a cuatro
referencias— se queda como texto, cuando `J/K` ya traen los gramos para resolverlo (TB4: 22 %, TF4: 32,8 %,
TF2: 5 %, TB5: 20 %). Una hoja que nombra un límite y no lo evalúa invita a suponer que lo ha comprobado.

**Fix (en el generador).** Añadir una columna «Materias añadidas sobre el peso total» = `J/K` y su semáforo
contra un parámetro `0,40` en la zona de mínimos (`A38:B41`), igual que el 25 %.

### B10 · BAJA · El 25 % del bombón se aplica a las CAJAS surtidas, que no son una pieza
**Libro:** `carta-de-apertura-y-escandallo-chocolate.xlsx`.
**Celdas:** `Denominaciones y Mínimos!M31:M34` = «Sí», `N31:N34` = «CUMPLE el 25 % sobre el peso total».

**Problema.** Las cuatro cajas llevan denominación «Chocolates rellenos surtidos» por los aps. 6.a) y 6.c) de
`CHN-13`, que son una regla de **etiquetado de surtidos**, no una categoría con mínimo de composición. El
mínimo del 25 % es por pieza (aps. 1.10 y 1.13). Aplicarlo al agregado de la caja da un resultado que pasa
(42 %) pero enseña una regla que no existe: un surtido podría cumplir en el agregado y llevar dentro una pieza
que no cumple.

**Fix (en el generador).** Poner `M31:M34` = «No» y que `N` diga «La denominación va por pieza: el 25 % lo
comprueba cada bombón en su propia fila», que es lo que el propio `F31` ya explica.

### B11 · BAJA · El libro 2 es el único cuyo «Instrucciones» no cita la frontera con el kit
**Libro:** `calculadora-capex-chocolateria.xlsx`.

**Problema.** Los otros ocho nombran `kit-tareas-chocolateria` y dicen qué hace el kit y qué hace la guía. El 2
no lo menciona en ninguna de sus siete hojas. §2.2 no le asigna frontera explícita, así que no es un
incumplimiento, pero es el único libro del pack sin cross-sell al kit de 12 € y sin la frase que evita que el
comprador crea que la guía repite lo que ya tiene.

**Fix (en el generador).** Añadir el bloque de frontera de `_comun_chocolateria.py` a
`gen_calculadora-capex-chocolateria.py`, aunque sea para decir que el kit no cubre la inversión.

### B12 · BAJA · Las tres celdas citables de la hoja EUDR salen de fábrica en «Sin resolver»
**Libro:** `checklist-legal-licencias-y-cacao.xlsx`.
**Celdas:** `EUDR — Tu Papel en la Cadena!B18`, `B19`, `B20`, las tres en `mapa-checklist-legal-licencias-y-cacao.json`.

**Problema.** Con `B13` («¿tu cobertura llega amparada por una declaración de diligencia debida?») sembrada en
«No lo sé» —que es honesto y coherente con D19—, las tres salidas publican «Sin resolver…». Están en el mapa, y
un capítulo que las cite imprimirá «Sin resolver: primero aclara tu papel» como si fuera el resultado del caso
«La Almendra». Probado con pycel: con «Importo grano» las tres se resuelven bien.

**Fix (en el generador).** Mantener la siembra (es la decisión correcta) pero sacar esas tres etiquetas del
mapa o renombrarlas de forma que un capítulo no las pueda citar como conclusión (p. ej.
«Estado de la hoja EUDR antes de que el lector la rellene»).

### B13 · BAJA · Un cliente marcado «Minorista de distinta titularidad» lleva canal «B2B a hostelería»
**Libro:** `checklist-equipamiento-y-proveedores-cacao.xlsx`.
**Celdas:** `Clientes a los que Suministras!D13` = «Minorista de distinta titularidad», `E13` = «B2B a hostelería».

**Problema.** «Tienda gourmet La Despensa» no es hostelería. Viene tal cual de
`datos_ejemplo.CLIENTES_B2B[3]`, cuyo `canal` es `'B2B hosteleria'`. El contador por TIPO lo resuelve bien
(`E23` = 1) y la nota `G23` lo explica, pero la fila publicada dice dos cosas incompatibles y el desplegable de
canal no ofrece ninguna alternativa para un minorista.

**Fix (en el generador).** Añadir «B2B a minorista» a la lista de canales en `datos_ejemplo.CANALES`/en el
desplegable de la hoja y reasignar ese cliente. Ojo: los **cinco canales del libro 7** son los de §3.4 y no se
tocan; esta lista es la de la tabla de clientes del libro 9, que es otra cosa.

### B14 · BAJA · `Ruta Doméstica!B20` lleva la fecha 10-09-2026 y el resto del pack la del 12-09
**Libro:** `checklist-legal-licencias-y-cacao.xlsx`.

**No es un defecto**, y se anota para que nadie lo «arregle»: es la cita literal del art. 13.9 sostenida por
`PA-29c`, reutilizada de Pastelería, que es el **origen (d)** que §3 declara válido y que exige citarla «con su
fecha de verificación». Ninguna ficha `CHN-*` cubre los 100 kg. Lo que sí hay que hacer es que el futuro
`gate_libros.py` **no** exija una única fecha, o tumbará esta nota.

---

## Resumen de fixes por generador

| Generador | Hallazgos |
|---|---|
| `gen_capacidad-obrador-y-clima.py` | A1 (quitar el bloque de campañas), A9, A10, B7 |
| `gen_calculadora-capex-chocolateria.py` | A3, A6, A9, A10, B4 (publicar «inmovilizado amortizable»), B11 |
| `gen_sensibilidad-al-precio-del-cacao.py` | A9, A10, B3 |
| `gen_carta-de-apertura-y-escandallo-chocolate.py` | A3, A9, A10, B8, B9, B10 |
| `gen_vida-util-rellenos-y-rotacion.py` | **A2**, A9, A10, B6 |
| `gen_campanas-y-valle-del-ano.py` | A1 (o su contrario), A9, A10, B7 |
| `gen_plan-financiero-3-anos-chocolateria.py` | A4, A9, A10, B4, B5 |
| `gen_checklist-legal-licencias-y-cacao.py` | **B2**, A9, A10, B12 |
| `gen_checklist-equipamiento-y-proveedores-cacao.py` | **B1**, A3, A9, A10, B13 |
| `datos_ejemplo.py` | A5 (cuatro nombres de hoja de `CRUCES`), B7 (figura de Reyes), B13 (canal) |
| `_comun_chocolateria.py` | A9 (Title Case), A10 (freeze + pie), B8 (gate de artículo en `nota_legal`) |
| `gate_libros.py` (por escribir) | Contar los OCHO cruces contra `CRUCES` ya corregido; cruzar `libro 9!E23 > 0 ⟺ libro 8!B6="Sí"`; exigir artículo en toda nota legal; tolerar la fecha 10-09-2026 de los ids `PA-*` |

