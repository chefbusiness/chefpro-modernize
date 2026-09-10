# Refutación de los 8 libros de Excel — «Cómo Montar una Pastelería» (2026-09-10)

> Refutador adversarial de los xlsx de `scripts/productos-digitales/guia-pasteleria/build/`, dos lentes en un
> solo pase: **(A) fórmulas y convenciones** y **(B) dominio, coherencia y legal**. El encargo era TUMBARLOS, no
> confirmarlos. Cada libro se abrió **dos veces** (fórmulas y `data_only`), uno cada vez, y las cadenas clave se
> recalcularon con **pycel** evaluando la salida ANTES de tocar la entrada. Contrastado contra
> `guia-pasteleria-SPEC.md` (D1-D36, §2.2, §2.3, §3, §5), `guia-pasteleria/datos_ejemplo.py`,
> `auditorias/guia-pasteleria-verificacion-legal-2026-09-10.json` (63 entradas), los ficheros vivos de
> `kit-tareas-pasteleria/` y `kit-escandallos/05-pasteleria.xlsx`, y los 8 `mapa-*.json`.
>
> **Veredicto: CORREGIR ANTES.** 23 hallazgos: **3 altos · 9 medios · 11 bajos**. El motor de cálculo está
> esencialmente limpio (0 funciones prohibidas, 0 referencias externas, 0 divisiones sin `IFERROR`, 0 DV con
> lista de comas, 0 celdas verdes vacías en 2.222 verdes). Los tres altos son (1) **tres celdas que publican `0`
> donde hay 100 h, 40 h y 22 líneas** —el bug de `=SUM(rango de SUMPRODUCT)` que el constructor 3-4 cazó y gateó
> en sus libros y que nadie corrió en los libros 7 y 8—, dos de ellas **dentro del mapa que el guion va a citar**;
> (2) el libro 7 compara **dos ámbitos distintos** y sale de fábrica con un veredicto rojo falso que manda al
> comprador a rehacer su plan financiero; y (3) el libro 4 construye toda su hoja del huevo **sin la nota legal
> de PA-14**, el id que contiene las tres vías del art. 9 que su propio desplegable ofrece.

## 0. Lo que NO se pudo tumbar (verificado, no asumido)

| Comprobación | Resultado |
|---|---|
| Fórmulas totales | **4.515** en los 8 libros (152 · 313 · 292 · 1.899 · 1.021 · 299 · 351 · 188) |
| Errores `#REF!` / `#DIV/0!` / `#VALUE!` en `data_only` | **0** |
| Fórmulas sin caché | 95, y **son la convención «sin dato» = `""`** (31+1+47+3+0+0+3+10, coincide al dígito con lo declarado por los cuatro constructores) |
| Funciones prohibidas (`INDIRECT` · `COUNTA` · `PMT` · `OFFSET` · `XLOOKUP` · `LET` · `LAMBDA` · `RANK` · `NETWORKDAYS` · `IRR`) | **0** en los 8 libros |
| Referencias externas entre libros (`[`, `.xlsx!`) | **0** — la regla transversal de §2.3 se cumple en todo el pack |
| Divisiones sin `IFERROR` | **0** de 4.515 |
| Constantes tecleadas dentro de fórmula | **1 sola de verdad** (hallazgo A6); el resto son conversiones de unidad (60 min/h, 12 meses, 365 días, 7 días, 1.000 g/kg) e índices de mes |
| DV de tipo lista contra rango | **26 de 26**, todas al rango de su propia hoja, todas con `showErrorMessage=True`, **0 listas con comas**, 0 rangos vacíos, 0 mal formadas |
| Celdas verdes | **2.222**; **0 vacías**, **0 bloqueadas**, **0 con fórmula dentro**, **0 celdas no verdes desbloqueadas con valor** → D21 se cumple, verificado sobre el fichero (no sobre el mapa) |
| Semáforos | 106 reglas de formato condicional; **1 sola** hace comparación numérica sin `ISNUMBER` (hallazgo A8). Las 85 restantes de tipo `cellIs equal` comparan **texto**, donde `ISNUMBER` no aplica. Los semáforos de fórmula del libro 4 (`Decisión de Surtido!H6:I35`) sí llevan `IF(NOT(ISNUMBER(...)),"",...)` |
| `print_setup` A4 + `fitToPage` | **51/51 hojas** (paperSize 9, `fitToWidth=1`, orientación elegida hoja a hoja) |
| Protección de hoja sin contraseña | **51/51** |
| Metadata | `creator` y `lastModifiedBy` = `AI Chef Pro` en los 8; `title` y `subject` presentes en los 8 |
| Hoja «Instrucciones» la primera · «Celdas verdes = campos editables» · línea de versión `Versión 1.0 · septiembre 2026 · aichef.pro/guia-pasteleria-obrador · info@aichef.pro` · bio · nota de desproteger · cadencia de uso · frontera con el kit | **8/8 en cada uno de los siete puntos** (la línea de versión es idéntica carácter a carácter en los 8) |
| Mapas | 78 · 73 · 220 · 49 · 118 · 108 · 93 · 50 etiquetas → **todos ≥ 25**. **0 celdas inexistentes**, **0 desajustes de valor** salvo una fecha, **0 valores vacíos** |
| Gate de `SUM(rango)` recalculado a mano contra el caché | 105 sumas analizadas, **3 descuadres** (hallazgos A1 y B1); los otros 102 cuadran |
| Gate de agregados (`SUMPRODUCT(--(x=y),z)`, `SUMIF`, `COUNTIF`) recalculado a mano | 95 analizados, **0 descuadres reales** (los 5 que saltaron eran falsos positivos de mi propio gate, que normaliza espacios dentro de literales) |
| Notas legales | **217 notas** «Verificado el 10-09-2026 · norma y artículo · URL»; **0 con otra fecha**, **0 sin URL**. `gate_legal()` en verde en los ocho generadores |
| Formatos numéricos | `#,##0.00 €` · `0.0%` · `dd/mm/yyyy` · `#,##0(.0/.00/.000)`; **0 celdas de texto con formato €**, **0 fechas como número**, 2 porcentajes >150 % que son reales (hallazgo B8) |
| Coherencia con `kit-escandallos/05-pasteleria.xlsx` (SPEC §3) | **Idéntica**. Croissant: los 7 ingredientes, las 7 cantidades, los 7 precios, las 7 mermas y la misma fórmula (`E/(1−merma)` y `bruta×precio/factor`) → materia de tanda 4,716701 € en los dos ficheros. Igual en Tarta de Chocolate 70 % y Macarons |
| Coherencia con el kit, lo que la SPEC mandaba **abrir para comprobar** | **Comprobado abriendo los dos ficheros**: `Croissant de mantequilla`, `Pain au chocolat` y `Napolitana de crema` están literalmente precargadas en `10-plan-produccion-semanal.xlsx` (Plan Semanal y Producido vs Vendido) y en `12-control-alergenos-vitrina.xlsx` (Matriz y Carta) |
| R4 y D12: ¿está corregido el `13-registro-temperaturas-recepcion.xlsx`? | **SÍ, hoy**: su hoja «Vidas Útiles» dice «Con huevo: 24 h de tope (art. 9.3)» y «Producto relleno: vitrina a 4 °C o menos (art. 4.1, fila 9)», y sus vitrinas están a 0-4 °C. **La cautela del constructor 5-6 era innecesaria** y la cita del libro 4 es legítima |
| Juego de datos «La Clara» | 90 m² repartidos 45+22+(5+4+3)+(8+3) = **exactamente** los 45/22/12/11 de D22 · **30 referencias** en 6+6+6+4+8 familias · **mix suma 100,0 %** · 5 personas / **3,5 jornadas** con los 4 nombres literales del kit y dos Dependientes Vitrina · 6 grupos de convenio con los 6 brutos de D22 y 15 pagas · 6 picos con los nombres del `BONUS-02` |
| Capacidad, libro 1 ↔ libro 3 | **480** piezas/día, **476** de crucero, **4** de excedente y **6** campañas que no se aguantan: coinciden al dígito en los dos libros |
| Personal, libro 5 ↔ libro 8 | 92.776,0785 € de coste anual y 3,5 jornadas: **idénticos** y ambos iguales a `datos_ejemplo.coste_personal_anual()` |
| Ruta crítica, libro 6 ↔ `datos_ejemplo.ruta_critica()` | 8,50 meses, apertura en **septiembre**, holgura hito a hito idéntica y **11 hitos con holgura cero** (el camino más largo son 9; las dos ramas paralelas empatadas tampoco tienen holgura). La fila está bien rotulada «Hitos SIN holgura (ruta crítica)» |
| Lista negra §5 de la SPEC | **0 apariciones** de «11.729 pastelerías», «1,08 M€», «84.000-180.000 €», PS-60, «110 m²» como caso, «dulcería», «artesana», «plan gratuito», «100 % legal», «TRLGDCU», «exenta del art. 6», «los 500 kg incluyen el mostrador», RD 3484/2000, RD 1420/2006, RD 2207/1995. Las 5 menciones a `RD 1254/1991` y al «carnet de manipulador» son **las refutaciones**, escritas como tales |
| D8 (art. 3 como árbol) | Cumplido: puerta de entrada delante, tres condiciones **ACUMULATIVAS**, y dentro de «marginal» **dos vías ALTERNATIVAS** con la cita literal del 25 % y de los 500 kg, más el aviso expreso de que la lectura del mostrador no existe |
| D7 (art. 13.8 con **cinco** letras) · D13 (tres límites del 13.9) · D10/D11 (dos techos, no un conflicto; plazo del 9.3 separado de la vida útil) | Cumplidos y bien escritos. La vida útil sale como texto «Por declarar en tu APPCC» en las 30 referencias, nunca calculada |
| Pruebas de comportamiento con pycel (evaluando la salida antes de tocar la entrada) | Libro 1: bajar el obrador de 45 a 20 m² mueve total, descuadre, % y veredicto («Reparto suficiente» → «El obrador se queda corto»). Libro 2: escenario Medio→Alto mueve obra, CAPEX, desembolso, aportación propia y el coste de la obra nueva a 5 años. Libro 4: doblar el PVP del croissant mueve food cost, margen y aporte al ticket; la matriz de huevo devuelve 4 °C+8 °C→manda 4 y 24 h en la vía 1.a) no estable, y **excluye correctamente la vía 1.b)** del art. 9.3, que es lo que dice PA-15. Libro 5: subir tickets/día mueve ingresos; subir un bruto mueve coste de personal, fijos y punto de equilibrio |

---

## Lente A — Fórmulas y convenciones

### A1 · ALTA · Dos celdas del libro 8 publican `0` donde hay 100 h y 40 h — y las dos están en el mapa que va a citar el guion
**Libro:** `plantilla-turnos-y-coste-personal.xlsx`.
**Celdas:** `Turnos Semanales!E24` («Horas de obrador a la semana») y `Turnos Semanales!E25` («Horas de despacho a la semana»).

**Problema.** Las dos fórmulas son `=SUM($E$17:$K$17)` y `=SUM($E$18:$K$18)` sobre filas que a su vez son
`SUMPRODUCT`. Recalculando el rango a mano contra el caché: `E24` vale **0,0** y la suma real es **100**;
`E25` vale **0,0** y la suma real es **40**. Es exactamente el modo de fallo que el constructor 3-4 midió en su
`Escandallo por Tanda!E266` y para el que escribió un gate en `_comun_libros_3_4.cerrar()`: `pycel` evalúa bien
cada `SUMPRODUCT` pero devuelve `0` para el `SUM` que los agrega, `inject_cache.py` escribe ese `0`, y ni
`fallos_pycel` ni «ninguna fórmula `None`» lo ven, porque `0` **es** un valor.

Lo que lo convierte en alto y no en cosmético: **las dos etiquetas están en `mapa-plantilla-turnos-y-coste-personal.json`** con `"valor": 0.0`, y `documentos.py` resuelve las referencias del guion con `openpyxl` en `data_only=True` (D35). Un capítulo que cite «Horas de obrador a la semana» imprimirá **0**. El propio constructor 7-8 declara en su nota que el reparto da «40 h de despacho»: el número que sabe que es correcto no es el que publica su fichero. `fullCalcOnLoad="1"` salva al humano que abre Excel, no al pipeline ni a Google Sheets/Numbers/previsualizador antes de recalcular.

**Fix (en el generador).** `gen_plantilla-turnos-y-coste-personal.py:700-709`: sustituir los dos `=SUM(E17:K17)` / `=SUM(E18:K18)` por el agregado directo sobre la tabla, del mismo modo que el constructor 3-4 resolvió el suyo — p. ej. `=SUMPRODUCT(--($C$11:$C$15="OBRADOR"),$E$11:$K$15)` y `=SUMPRODUCT(--($C$11:$C$15="COMERCIO"),$E$11:$K$15)`, que no dependen de la fila intermedia. Y **portar a los ocho generadores el gate genérico de `_comun_libros_3_4.cerrar()`** que recalcula todo `SUM(rango)` contra la suma de su rango: con él, estas dos y la del hallazgo B1 saltan solas.

### A2 · ALTA · El libro 7 compara dos ámbitos distintos y sale de fábrica con un veredicto rojo falso que manda a rehacer el plan financiero
**Libro:** `checklist-equipamiento-y-proveedores.xlsx`.
**Celdas:** `Equipamiento!I49`, `I50` y `I51`; entrada `Equipamiento!C9`.

**Problema.** `C9` es la celda verde «Total de CAPEX de equipamiento del libro 2 (€, sin IVA)» y su nota `D9`
dice literalmente «**CÓPIALO DE `calculadora-capex-pasteleria.xlsx` (libro 2), bloques "Equipamiento de obrador"
y "Tienda y vitrina"**». Esos dos bloques del libro 2 valen 54.296,24 + 12.684,10 = **66.980,34 €** y **excluyen
las tres líneas opcionales** (atemperadora 7.400 €, horno de pisos 12.000 €, puertas correderas 120,40 €:
verificado contra `datos_ejemplo.equipamiento_bloque_sin_iva()`).

Pero `I49` y `I50` restan y dividen contra `I44` = «Total real negociado sin IVA, **todas** las líneas» =
**86.500,74 €**, que sí las incluye. Resultado publicado: desviación **+19.520,40 €** y **+29,1 %**, con
`I51` = «**Fuera del umbral: rehaz el CAPEX del libro 2 con estos precios**» y la nota `K51` insistiendo en que
«el plan financiero del libro 5 se calcula sobre el CAPEX del libro 2: si esto se sale, hay que rehacerlo».

Los 19.520,40 € **son exactamente los tres opcionales**, no una desviación de negociación. La comparación correcta
ya existe en la misma hoja: `I43` («Total real negociado sin IVA, sólo líneas críticas») vale **66.980,34 €**,
idéntico a `C9` al céntimo → desviación 0,0 %. El ejemplo publicado, que es el que verá el comprador y el que
citará el capítulo 04, acusa un descuadre que no existe y le pide rehacer el plan de 3 años.

**Fix (en el generador).** `gen_checklist-equipamiento-y-proveedores.py:668-676`: cambiar el operando
`a=R_REAL_TODO` por `a=R_REAL_CRIT` en `R_DESV_EUR` y `R_DESV_PCT` (o, si se quiere mantener el total, cambiar la
semántica de `C9` y su nota `D9` para que el lector copie del libro 2 **incluyendo** los opcionales, que hoy no
están ahí). Añadir además una fila explícita «Diferencia por líneas opcionales (€)» = `I44 − I43`, que es el
número que el lector quiere ver y que hoy está disfrazado de error.

### A3 · MEDIA · `Contador!B27` del libro 7 publica `0` donde son 22 líneas, junto a un 17 y un 5 correctos
**Libro:** `checklist-equipamiento-y-proveedores.xlsx`. **Celda:** `Contador!B27`.

**Problema.** Mismo modo de fallo que A1: `=SUM($B$25:$B$26)` sobre dos `SUMPRODUCT` que valen 17 y 5. El caché
dice **0,0**; la suma real es **22**. La fila se rotula «TOTAL» y queda debajo de sus dos sumandos correctos, así
que en cualquier vista que no recalcule se lee «17 + 5 = 0». No está mapeada, y por eso es media y no alta.

**Fix (en el generador).** `gen_checklist-equipamiento-y-proveedores.py:1216`: emitir la celda como
`=SUMPRODUCT(--('Equipamiento'!$G$16:$G$37<>""))` (o como suma de los dos `SUMPRODUCT` escritos en línea) en vez
de `=SUM($B$25:$B$26)`. Cubierto también por el gate genérico de `SUM(rango)` que pide A1.

### A4 · MEDIA · La bio del autor se publica con DOS literales distintos, cuatro libros cada uno, y dos libros llevan la nota de desproteger duplicada
**Libros:** los ocho.
**Celdas:** `Instrucciones!A34` (libro 1) · `A35` (libro 2) · `A29` (libro 3) · `A29` (libro 4) · `A40` (libro 5) · `A36` (libro 6) · `A30` (libro 7) · `A29` (libro 8).

**Problema.** Cuatro libros escriben la bio **con** sufijo —«… en cocina desde los 17 años **· johnguerrero.es**»
(libros 1 `capacidad`, 2 `calculadora-capex`, 5 `plan-financiero`, 6 `checklist-legal`)— y cuatro **sin** él, con
punto final, que es el literal de la SPEC («… en cocina desde los 17 años.»: libros 3 `estacionalidad`,
4 `carta`, 7 `checklist-equipamiento`, 8 `plantilla-turnos`). La causa está localizada: `_comun_pasteleria.py:49`
y `_comun_libros_5_6.py:63` hacen `BIO = motor.BIO_LINE`, que trae el sufijo; `_comun_libros_3_4.py:48`,
`gen_checklist-equipamiento-y-proveedores.py:90` y `gen_plantilla-turnos-y-coste-personal.py:89` lo declaran a
mano sin él. El riesgo que el constructor 1-2 anticipó se ha materializado.

Añadido: los libros **5 y 6** publican **dos** notas de desproteger seguidas —`plan-financiero!Instrucciones!A37`
+`A38` y `checklist-legal!Instrucciones!A33`+`A34`— porque toman la de `motor` y encima escriben la suya.

**Fix (en el generador).** Subir `VERSION_LINE`, `BIO` y `NOTA_DESPROTEGER` a `guia-pasteleria/datos_ejemplo.py`
(como hace `manual-chef-ejecutivo/datos_ejemplo.py`) con el literal exacto de la SPEC, y que los tres módulos
`_comun_*.py` y los dos generadores sueltos los importen de ahí. En `_comun_libros_5_6.py` quitar la segunda
línea de desproteger.

### A5 · BAJA · 55 caracteres fuera de WinAnsi (cp1252) en cuatro libros
**Libros y celdas:**
- **U+202F** (espacio fino), 21 apariciones: `estacionalidad-y-picos` ×6 (`Instrucciones!A19`, `Parámetros!E25`, `E26`, `Capacidad vs Demanda del Pico!A17`, `Refuerzo y Tesorería!R6`, `R11`) y `carta-de-apertura-y-escandallo` ×15 (`Instrucciones!A10`, `A16`, `A17`, `A19`, `A21`, `Parámetros!G19`, `G20`, `G24`, `G31`, `G34`, `G35`, `A91`, `Decisión de Huevo y Temperatura!A61`, `Mix y Ticket Medio!I43`, `I46`).
- **U+2192** (flecha), 2: `plan-financiero-3-anos-pasteleria!Instrucciones!A37` y `checklist-legal-y-licencias!Instrucciones!A33`, los dos por usar `motor.NOTA_DESPROTEGER` tal cual (`_comun_libros_5_6.py:64`).
- **U+2610 ☐** y **U+2713 ✓**, 32: `checklist-legal-y-licencias!Checklist Legal (F1-F6)!A7:A51` y sus listas de validación.

**Problema.** La convención de §2.2 dice «textos WinAnsi». Los tres casos son distintos y no merecen la misma
respuesta: la flecha es un descuido puro y ya está resuelta en `_comun_pasteleria.py:53`; el espacio fino es
deliberado (`motor.NARROW`) y tiene precedente en el `guia-food-cost` ya publicado; las casillas ☐/✓ calcan el
molde B de `checklist-legal` de panadería y el libro 7 resolvió lo mismo **sin símbolos**, con el vocabulario
Pendiente/Presupuestado/Pedido/Recibido/Instalado/N-A. Los tres libros no pueden decidirlo cada uno por su cuenta.

**Fix (en el generador).** (a) `_comun_libros_5_6.py:64` → usar la nota parcheada de `_comun_pasteleria.py`
(inmediato, sin discusión). (b) Decidir de una vez si el gate WinAnsi se aplica a los xlsx o sólo a los
documentos, y escribirlo en la SPEC; si se aplica, sustituir `NARROW` por espacio normal en los libros 3 y 4 **y
en el `guia-food-cost` publicado**, y las casillas del libro 6 por el vocabulario del libro 7. (c) En cualquier
caso, añadir el barrido cp1252 al cierre de los ocho generadores, que hoy sólo lo hace `_comun_pasteleria.py`.

### A6 · BAJA · Un umbral de negocio cableado dentro de una fórmula teniendo su parámetro al lado
**Libro:** `calculadora-capex-pasteleria.xlsx`. **Celda:** `IVA y Tesorería!B28` (`gen_calculadora-capex-pasteleria.py:1073`).

**Problema.** `=IF(B26="","",IF(B26<=0,"…",IF(B27<3,"Te falta colchón: revisa el fondo de maniobra","Necesitas
aportación propia")))`. El **3** es un umbral de criterio, no una conversión de unidad, y la hoja ya tiene
`Parámetros!B16` = «Meses de colchón de tesorería» = 4 en celda verde. Con B16 = 4 el veredicto nunca puede decir
«te falta colchón», porque `B27` = `B24/B17` = 4 por construcción: el aviso está muerto salvo que el lector baje
B16 por debajo de 3. Es el **único** hardcode real de los 4.515 formulas del pack.

**Fix (en el generador).** Añadir un parámetro verde «Colchón mínimo aceptable (meses)» (valor por defecto 3,
declarado supuesto) y referenciarlo: `IF(B27<'Parámetros'!$B$xx, …)`.

### A7 · BAJA · Centinela `999` en 144 celdas, y vive en una celda VERDE que el lector puede tocar
**Libro:** `checklist-legal-y-licencias.xlsx`. **Celdas:** `Cronograma y Ruta Crítica!C6` (verde, valor 999) y la matriz `C24:N35`.

**Problema.** La matriz de dependencias usa 999 como «no aplica», oculto con el formato `[=999]"";0.0`, y las
holguras se calculan con `MIN(MIN(C24:C35), MAX($H$9:$H$20)) − H9`. Está **honestamente declarado** en `O6`
(«Truco de cálculo, no un dato») —por eso es bajo y no medio—, pero (a) es una celda verde sin guarda: si el
lector escribe ahí un 3, las once holguras y la ruta crítica cambian sin un solo aviso, y (b) los 999 se leen tal
cual con `data_only`, así que cualquier volcado a CSV o cualquier script que recorra la hoja los verá.

**Fix (en el generador).** Dejar `C6` **bloqueado y sin relleno verde** (es una constante de implementación, no
una entrada), o mantenerlo verde con un semáforo que avise si `C6 <= MAX(C9:C20)`.

### A8 · BAJA · El único semáforo numérico sin `ISNUMBER` del pack
**Libro:** `checklist-legal-y-licencias.xlsx`. **Regla:** formato condicional de tipo `expression` sobre `Ruta Doméstica!B14`, fórmula `=$B$7>$B$13`.

**Problema.** `B7` («Kilos de producto que elaboras a la semana») es verde y numérica. En Excel, cualquier texto
es mayor que cualquier número: si el lector escribe «unos 60» o «60 kg», la regla se enciende en rojo y la hoja
avisa de que se pasa del tope legal de 100 kg cuando no lo sabe. La fórmula de la celda (`B14`) sí está bien
protegida por `IFERROR`, pero pinta el resultado con esta regla. Es 1 de 106 reglas: las otras 105 están bien.

**Fix (en el generador).** `=AND(ISNUMBER($B$7),ISNUMBER($B$13),$B$7>$B$13)`.

### A9 · BAJA · Cuatro de los ocho mapas llevan una clave cuyo `ref` no es `libro!Hoja!Celda`
**Ficheros:** `mapa-carta-de-apertura-y-escandallo.json` y `mapa-estacionalidad-y-picos.json` (clave `_notas`), `mapa-checklist-legal-y-licencias.json` y `mapa-plan-financiero-3-anos-pasteleria.json` (clave `_meta`).

**Problema.** Esas cuatro entradas respetan el esquema `{ref, valor, tipo}` (con `tipo: "nota"`) pero su `ref` es
sólo el nombre del fichero, sin `!Hoja!Celda`. Cualquier consumidor que haga `ref.split('!')` para resolver la
celda —que es exactamente lo que hace `documentos.py` con las referencias del guion— revienta o resuelve mal en
la mitad de los mapas del producto. Los otros cuatro mapas no llevan ninguna clave así.

Segundo detalle del mismo sitio: `mapa-checklist-legal-y-licencias.json` guarda «Caducidad de la formación del
Jefe Pastelero» como la **cadena** `"2028-09-09"` mientras la celda `Registro de Formación!F6` devuelve un
`datetime`. Es la única de 789 etiquetas que no coincide en tipo con su celda.

**Fix (en el generador).** Sacar la nota de cabecera del diccionario de etiquetas a una clave hermana
(`{"celdas": {...}, "notas": "..."}`) o darle un `ref` completo; y serializar las fechas con un criterio único en
los cuatro módulos comunes (`_comun_libros_5_6.cerrar()` ya lo hace, los otros no).

### A10 · BAJA · Los títulos `A1` van en oración en seis libros y en Title Case en dos, con las pestañas siempre en Title Case
**Libros:** los ocho. **Ejemplos:** `capacidad-obrador-y-local`: pestaña «Cuello de Botella» / `A1` «Cuello de botella». `plan-financiero`: pestaña «Punto de Equilibrio» / `A1` «Punto de equilibrio: cuántos tickets al día». Total: 37 títulos en oración.

**Problema.** La convención pide «Title Case español en encabezados». Los libros 3 (`estacionalidad-y-picos`) y 4
(`carta-de-apertura-y-escandallo`) lo cumplen en `A1`; los otros seis usan mayúscula de oración, y en los seis la
pestaña **sí** está en Title Case, así que el mismo libro escribe el mismo título de dos formas.

**Fix (en el generador).** Una función `titulo_hoja(nombre)` en el módulo común compartido (el mismo que se cree
para A4) que aplique Title Case español y se use tanto para `ws.title` como para `A1`.

### A11 · BAJA · Tres detalles de acabado
**(a)** El `subject` de la metadata usa **tres** formatos distintos: «Cómo Montar una Pastelería · libro 1 · v1.0» (libros 1-2), «… · v1.0» (libros 7-8) y «… · Versión 1.0 · septiembre 2026» (libros 3-6). **Fix:** un solo literal en el módulo común.
**(b)** `estacionalidad-y-picos!Instrucciones!A` y `carta-de-apertura-y-escandallo!Instrucciones!A` tienen **118 de ancho**; con `fitToWidth=1` esa hoja se imprime a una escala que deja el texto ilegible. Los otros seis libros no pasan de 84. **Fix:** tope de 90 en el módulo común y `wrap_text`.
**(c)** `calculadora-capex-pasteleria!Parámetros!B11` = `=IF(B10="Bajo",B7,IF(B10="Alto",B9,B8))`: con `B10` vacío o mal escrito cae **silenciosamente en «Medio»** en vez de devolver `""`. La DV lo impide mientras la hoja esté protegida, pero la convención de la casa es que un «sin dato» no se resuelva solo. **Fix:** `IF(B10="","",IF(...))`.

---

## Lente B — Dominio, coherencia entre libros y legal

### B1 · ALTA · El libro 4 construye toda la hoja del huevo sin la nota legal de PA-14, que es el id que contiene las tres vías del art. 9
**Libro:** `carta-de-apertura-y-escandallo.xlsx`. **Celdas:** `Decisión de Huevo y Temperatura!D6:D35` y su bloque de listas `A50:B54`.

**Problema.** `IDS_LEGALES_REQUERIDOS` de `datos_ejemplo.py` asigna **diez** ids al libro 4. Barriendo las 131
notas del fichero sólo aparecen **seis**: PA-12, PA-15, PA-23, PA-33, PA-36 y PA-36b. Faltan **PA-13**
(congelación, art. 5), **PA-21** (alérgenos), **PA-24** (RD 496/2010), **PA-25** (RD 308/2019) y —la que importa—
**PA-14, «Huevo crudo: las tres vías legales del art. 9»**.

Las cuatro primeras son discutibles y el constructor 3-4 las declaró con argumento (los alérgenos están prohibidos
aquí por R3; el art. 5 y la norma de calidad son prosa de capítulo). **PA-14 no lo es.** La columna `D` ofrece un
desplegable cuyos valores son literalmente las vías del art. 9 —`70/2`, `63/20`, `ovoproducto`— y el bloque
`B50:B52` parafrasea sus condiciones («70 °C durante 2 s en el centro», «63 °C durante 20 s **y servido para
consumo inmediato**»). Eso es la cita literal de PA-14, y va **sin una sola nota** «Verificado el 10-09-2026 · RD
1021/2022, art. 9.1 · URL». Las únicas notas legales de la hoja apuntan al art. 9.3 y al art. 4.1, es decir a las
**consecuencias**, no al artículo que **crea** las tres vías. En el libro que la SPEC declara «la hoja que no
existe en ningún producto del catálogo ni de la competencia», y en un producto cuya promesa es «la norma, el
artículo y el enlace», es el hueco más caro del pack.

**Fix (en el generador).** `gen_carta-de-apertura-y-escandallo.py`: poner `nota_legal('PA-14')` en `A50`, `A51` y
`A52` (las tres etiquetas de vía) y en la cabecera `D5`; y decidir explícitamente PA-13/PA-21/PA-24/PA-25 —o se
les da celda, o se les quita del reparto de `IDS_LEGALES_REQUERIDOS` con una línea de justificación, para que el
gate deje de mentir. Hoy `gate_legal()` pasa porque sólo comprueba que los ids **existan** en el JSON, no que
estén **usados**: **añadirle la comprobación de cobertura por libro**.

### B2 · MEDIA · Una nota «Verificado» respalda con el CTE DB-HS 3 justo lo que la verificación legal dice que el DB-HS 3 NO regula
**Libros:** `capacidad-obrador-y-local.xlsx` y `checklist-legal-y-licencias.xlsx`.
**Celdas:** `Ficha de Visita a Local!D6` (con `B6` «El local puede tener salida de humos propia hasta cubierta» y `J6`) y `Checklist Legal (F1-F6)!C8` («Confirmar que existe salida de humos hasta cubierta y quién la autoriza»).

**Problema.** Las dos celdas llevan la nota «Verificado el 10-09-2026 · **CTE, Documento Básico HS Salubridad,
Sección HS 3, apartado 1.1** · https://www.codigotecnico.org/pdf/Documentos/HS/DBHS.pdf». Pero el hallazgo de la
verificación legal que hay detrás de ese título es **PA-07**, y su `dato` dice lo contrario de lo que la nota
sugiere: «*El ámbito de aplicación de la Sección HS 3 son las viviendas y, en edificios de otro uso, solo
aparcamientos y garajes. Para locales de cualquier otro tipo (una pastelería) el propio DB-HS 3 remite al RITE.
Las reglas de "boca de expulsión en cubierta separada 3 m" son las de las viviendas*», y su `nota` remata: «*La
altura real de la chimenea la fija la ORDENANZA MUNICIPAL*».

La causa es de diseño, no de descuido: `nota_legal()` (`datos_ejemplo.py:2250`) compone la nota con
`fuente_titulo` + URL y **nunca con el `dato`**, así que un hallazgo NEGATIVO se publica exactamente igual que uno
positivo y el lector lee «esto está verificado contra el CTE». Encima, en el libro 1 la nota va pegada a un ítem
cuya regla operativa la pone `J6`: «La salida debe llegar a cubierta y **rebasar la cumbrera en 1 m** (PS-86c)»,
y PS-86c es un id de **sector**, no una norma verificada —el propio constructor 1-2 lo declaró—. El resultado es
un requisito de sector con sello de norma.

El acierto está al lado y demuestra que se sabía hacer: `Ficha de Visita a Local!J7` sí cita **PA-07b** (aire AE4
del RITE, sin conducto común con despacho ni aseos) y ésa sí es la base primaria correcta.

**Fix (en el generador).** (a) En los dos sitios, sustituir la nota de PA-07 por la de **PA-07b** (RITE, IT
1.1.4.2.5) y añadir en el texto visible «la altura de la chimenea la fija la ordenanza municipal, no el CTE».
(b) En `J6`, dejar el «1 m sobre la cumbrera» marcado como referencia de sector (PS-86c) y no como obligación.
(c) De fondo: hacer que `nota_legal()` acepte un prefijo («NO aplica: …») o que los ids con hallazgo negativo se
publiquen con su `dato` delante, porque este patrón se repetirá.

### B3 · MEDIA · Dos CAPEX totales y dos fondos de maniobra en el mismo pack, con la causa localizada
**Libros:** `calculadora-capex-pasteleria.xlsx` y `plan-financiero-3-anos-pasteleria.xlsx`.
**Celdas:** libro 2 `Parámetros!B17` (15.562,21), `Parámetros!B18` (62.248,84), `CAPEX por Bloque!K47` (228.049,18), `IVA y Tesorería!B26` (201.960,05); libro 5 `Inversión Inicial!B18` (62.115,26), `B19` (227.915,60), `0. Supuestos!B36` (201.826,48).

**Problema.** Medido: **Δ CAPEX = 133,58 €** y **Δ fondo = 133,58 €** y **Δ aportación propia = 133,57 €**. La
causa se aísla del todo: el libro 2 siembra sus gastos fijos mensuales con
`datos_ejemplo.gastos_fijos_mensuales()` = 15.562,21 €, y esa función mete **siempre** `intereses_anio_1()`
(3.660,38 €) aunque la foto sea la del año de crucero; el libro 5 calcula sus fijos de crucero con **sus**
intereses del año 2 (3.259,67 €, cuadro francés con carencia de 6 meses), 186.345,79/12 = 15.528,82 €/mes. Los
dos × 4 meses de colchón dan los dos fondos.

No es un fallo de fórmula de ningún libro —los dos son internamente correctos— pero el pack publica **dos
inversiones totales** para la misma pastelería, y la SPEC §2.2 nombra al libro 5 «la fuente única de cifras del
texto financiero» mientras el libro 2 es el que se titula «Calculadora de inversión inicial». El capítulo 04
citará uno y el 18 el otro.

**Fix (en el generador).** Lo limpio es corregir `datos_ejemplo.gastos_fijos_mensuales()` para que acepte el año
(o no incluya intereses y los sume quien los necesite) y resembrar `Parámetros!B17` del libro 2 con la cifra del
libro 5. Si no se puede tocar `datos_ejemplo` en esta sesión, la alternativa mínima es que la nota `E17` del
libro 2 diga qué año de intereses lleva y que el guion cite **siempre** el libro 5 para la inversión total.

### B4 · MEDIA · «Beneficio neto del año de crucero»: 32.348,05 € en `datos_ejemplo` contra 27.836,45 € en el libro 5
**Libro:** `plan-financiero-3-anos-pasteleria.xlsx`. **Celdas:** `PyG 3 Años` (resultado neto de crucero, mapeado como 27.836,45) y `datos_ejemplo.cuenta_resultados_crucero()`.

**Problema.** `cuenta_resultados_crucero()` devuelve `{'beneficio_neto': 32348.05, 'margen_neto': 0.10}`, pero ese
número es **margen bruto − gastos fijos**, es decir el resultado **antes de impuestos**; el libro lo llama por su
nombre (RAI 32.748,77 €, que difiere de los 32.348,05 por lo dicho en B3) y publica además el **neto después de
impuestos**: **27.836,45 €**, con margen **8,6 %** y su semáforo «dentro de la banda 8-12 %: Sí».

Hay por tanto **dos «beneficio neto» y dos «margen neto» del mismo año** en el mismo producto, y se llevan
4.511,60 € y 1,4 puntos. El nombre de la clave de `datos_ejemplo` invita justo al error: un redactor que escriba
«La Clara gana 32.348 € al año, un 10 % de margen neto» estará citando un RAI llamado neto, y el gate de
coherencia de `documentos.py` verá dos cifras.

**Fix (en el generador).** Renombrar la clave a `resultado_antes_impuestos` en `datos_ejemplo.py` (y `margen_rai`),
y que el guion tome el beneficio **sólo** del mapa del libro 5. Mientras tanto, no exponer
`cuenta_resultados_crucero()` a los redactores.

### B5 · MEDIA · La hoja del huevo resuelve en silencio —y en la dirección permisiva— una entrada contradictoria que ella misma permite
**Libro:** `carta-de-apertura-y-escandallo.xlsx`. **Celdas:** `Decisión de Huevo y Temperatura!D6:D35` (vía legal) y `F6:F35` (¿estable a temperatura ambiente?), con efecto en `H`, `I` y `K`.

**Problema.** El desplegable de `D` tiene cinco valores, y el quinto —**«estable a ambiente»**, definido en `B54`
como «Vía 1.a) y el producto terminado **ES** estable a temperatura ambiente»— **duplica la pregunta de la
columna F**, que es la que pregunta exactamente eso. Nada impide contestar las dos cosas de forma incoherente, y
la hoja no avisa. Comprobado con pycel sobre la fila 6:

| D6 | E6 (relleno) | F6 (estable) | `I6` temperatura | `K6` plazo |
|---|---|---|---|---|
| `70/2` | Sí | No | **4 °C** | **24** |
| **`estable a ambiente`** | **Sí** | **No** | 4 °C | **«No aplica»** |
| `ovoproducto` | No | No | 8 °C | 24 |

Los dos primeros casos describen **el mismo producto** —vía 1.a), relleno, no estable— y sólo el primero devuelve
las 24 horas. La segunda lectura es la incorrecta: PA-15 dice literalmente «los alimentos elaborados conforme a
lo establecido en los apartados 1.a), **que no sean estables a temperatura ambiente**, […] se consumirán en un
máximo de veinticuatro horas», y aquí el propio libro ha aceptado «no estable» en `F`. Es decir: el pack se
equivoca **por defecto**, quitando una obligación legal, en la hoja que vende como su diferencial.

Que conste lo que **sí** está bien y me sorprendió: excluir la vía **`63/20`** del art. 9.3 es correcto (el 9.3
nombra sólo el 1.a) y el apartado 2), y la hoja documenta en `B51` que esa vía exige «servido para consumo
inmediato». Ahí no hay nada que tumbar.

**Fix (en el generador).** Quitar `estable a ambiente` del desplegable de `D` —la información ya la da `F`— y
dejar cuatro vías (`70/2`, `63/20`, `ovoproducto`, `sin huevo`); el texto de `N` se construye entonces con `D`+`F`.
Si se quiere conservar por pedagogía, añadir una columna de coherencia:
`=IF(AND($D6="estable a ambiente",$F6="No"),"Incoherente: has elegido la vía de producto estable y luego has dicho que no lo es","")`
con su semáforo.

### B6 · MEDIA · El ejemplo publicado dice que «La Clara» no aguanta ninguna de las seis campañas y que el refuerzo no cubre en ninguna
**Libros:** `capacidad-obrador-y-local.xlsx` y `estacionalidad-y-picos.xlsx`.
**Celdas:** `Cuello de Botella!B12` («AJUSTADO»), `B28` («Varios picos se te van del obrador»), `G18:G23` (seis «NO»); `Capacidad vs Demanda del Pico!N6:N11`; `Refuerzo y Tesorería!H6:H11` (seis «No»).

**Problema.** Con 480 piezas/día de capacidad y 476 de crucero quedan **4 piezas de holgura (0,8 %)**, así que
cualquier factor de campaña se sale: Reyes pide 2.856 piezas/día (déficit −2.376) y hasta Comuniones, el pico más
suave, pide 762 (déficit −282). Y en la hoja de refuerzo, «¿Cubre el refuerzo?» sale **«No» en las seis**,
incluida San Valentín, donde `datos_ejemplo` da 0 personas y 0 horas de refuerzo contra 1 persona necesaria.

Los números son internamente correctos y coherentes entre los dos libros (comprobado al dígito), y el mensaje
—«el abatidor es tu cuello de botella»— es el que justifica la decisión 2 del bonus 2. Pero es una **decisión de
producto, no un hallazgo de cálculo**, y el guion la va a citar: el caso de demostración de una guía de 65 € que
enseña a montar una pastelería dice que la pastelería del ejemplo no puede servir Reyes, ni San Valentín, ni
Semana Santa, ni las comuniones, ni Todos los Santos, ni el Día del Padre. **Tiene que confirmarlo el
orquestador antes de que se escriba un capítulo encima**, porque revertirlo después obliga a regenerar los libros
1, 3 y 8 y a reescribir los capítulos que los citen.

**Fix (en el generador).** Ninguno automático: es una firma. Si se confirma, dejarlo y que el capítulo lo explote
como lección. Si no, subir la dotación de frío negativo en `datos_ejemplo.EQUIPAMIENTO` (el abatidor de 4
bandejas es quien limita) y dar a San Valentín un refuerzo distinto de cero; después regenerar 1, 2, 3, 7 y 8.

### B7 · MEDIA · El pack publica tres costes por hora distintos para la misma plantilla
**Libros:** `carta-de-apertura-y-escandallo.xlsx` (`Parámetros`, «Coste hora de obrador» = **17,94 €**), `plantilla-turnos-y-coste-personal.xlsx` (`Horas y Coste!L7:L11` = 16,00 / 15,43 / 13,36 / … y «Coste medio por hora de la plantilla» = **14,89 €**) y `estacionalidad-y-picos.xlsx` (`Parámetros!B21`, «Coste hora de empresa del refuerzo» = **13,36 €**).

**Problema.** Los tres están bien calculados y cada uno mide una cosa distinta —hora **productiva** de obrador
con el factor 0,85, hora **pagada** media de toda la plantilla, y hora pagada del grupo 5 que se usa para el
refuerzo—, y dos de ellos llevan nota. Pero un lector que salte del libro 3 al 4 ve 13,36 y 17,94 para «la hora
de la misma gente», y un redactor que cite los dos en el mismo capítulo escribirá una incoherencia. El constructor
3-4 lo anticipó; el tercer número (14,89) no estaba en su aviso.

**Fix (en el generador).** Rotular las tres celdas con el denominador dentro del propio título («Coste por hora
**productiva** de obrador», «Coste medio por hora **pagada** de la plantilla», «Coste por hora **pagada** del
refuerzo, grupo 5») y que cada nota remita a las otras dos por `libro!Hoja!Celda`. Añadir las tres al `prohibido`
del guion como trío que no se mezcla.

### B8 · MEDIA · Coeficientes inventados que devuelven +404 % y +151 % contra el rango publicado, sin semáforo por fila
**Libro:** `calculadora-capex-pasteleria.xlsx`. **Celdas:** `Variante del Formato!M15:M24` (y los coeficientes `D15:H24`).

**Problema.** Medido fila a fila, la desviación de la inversión modelada contra el punto medio del rango publicado:
PS-02 «obrador a puerta cerrada» **+404,2 %** (70.585 € modelados contra 8.000-20.000 publicados), PS-04
«cafetería-pastelería» **+150,9 %** (200.732 contra 60.000-100.000), PS-03 +78,3 %, PS-08 +34,9 %, PS-05 +32,6 %,
PS-07 +32,6 %, PS-06 +7,5 %, PS-01 −9,3 %.

La hoja es honesta: `A3` y `B29` declaran que los 50 coeficientes son supuestos editables, que las dos columnas
de la derecha sí son dato publicado con su id, y hasta anticipan el caso —«si tu cuenta y el rango publicado se
van a más del doble, uno de los dos está mal, y suele ser el rango». Por eso es media y no alta. Pero **no hay
ninguna marca en las dos filas donde eso pasa**: el lector ve un 404,2 % en una columna con formato de porcentaje
y sin nada que le diga que ése es precisamente el caso del que habla el párrafo de abajo. Y D17 obliga a la
lectura «dos fuentes independientes en el mismo orden de magnitud», que en esas dos filas no se sostiene.

**Fix (en el generador).** Añadir una columna «¿Cuadra con el rango publicado?» con
`=IF(M15="","",IF(ABS(M15)>1,"Se van a más del doble: mira el rango antes que la cuenta","En el mismo orden de magnitud"))`
y su semáforo, y sacar los 50 coeficientes a `datos_ejemplo.py` con procedencia `'supuesto'` explícita, para que
dejen de vivir dentro de un generador.

### B9 · BAJA · El tope legal de 100 kg del art. 13.9 viaja en una celda verde, como si fuera un dato del lector
**Libro:** `checklist-legal-y-licencias.xlsx`. **Celda:** `Ruta Doméstica!B13` (verde, 100).

**Problema.** `B13` es «Tope absoluto de la norma (kg a la semana)», lleva su nota legal correcta y alimenta el
semáforo `B14`. Pero está en verde, es decir: en el vocabulario del propio producto, «campo editable». El lector
puede subirlo a 300 y la hoja le dirá «Dentro del tope». Al lado, `B15` («Criterio propio de proporcionalidad»)
también es verde y **ahí sí corresponde**, porque es criterio de la casa y la hoja lo dice. La diferencia entre
las dos no se ve. La SPEC (D13) lista como entradas verdes de esa hoja «m² útiles · kg/semana · ¿registro
documental? · ¿tu CCAA amplía el 13.8.e)?»: `B13` no está en esa lista.

**Fix (en el generador).** Dejar `B13` bloqueado y sin relleno verde (parámetro normativo), manteniendo su nota
legal. Misma revisión para cualquier otra celda verde cuyo valor lo fije una norma.

### B10 · BAJA · La nota legal del IAE cita cuatro epígrafes y el texto de al lado cita cinco
**Libro:** `checklist-legal-y-licencias.xlsx`. **Celdas:** `Checklist Legal (F1-F6)!C16` (nota) y `K16` (texto).

**Problema.** La nota dice «RDLeg 1175/1990, tarifas del IAE, epígrafes **419.2, 644.1, 644.2 y 644.3**»; el texto
visible de `K16`, que cita PA-38, dice «los epígrafes son **419.1, 419.2, 644.1, 644.2 y 644.3**». Falta el 419.1
en la nota. La afirmación de fondo es correcta y coincide con PA-38 («el epígrafe minorista 644.1 —y el 644.3—
YA facultan para fabricar en el propio establecimiento»), así que es sólo la lista de la nota la que se queda
corta; pero es la nota la que lleva el sello «Verificado».

**Fix (en el generador).** Alinear el literal de la nota con el de PA-38.

### B11 · BAJA · Las «Personas de refuerzo» de San Valentín son 0 y el coste sale 0 €, en una columna donde la casa escribe `""`
**Libro:** `estacionalidad-y-picos.xlsx`. **Celdas:** `Refuerzo y Tesorería!B7`, `C7`, `D7`, `F7`.

**Problema.** `B7` = 0 personas y `C7` = 0 horas vienen de `datos_ejemplo.PICOS`, así que el 0 € de `F7` es un cero
**real**, no un «sin dato» —correcto según la convención—. Lo que chirría es que `F7` está mapeada como «Coste del
refuerzo de San Valentín» con `"valor": 0`, y que `H7` («¿Cubre el refuerzo?») dice «No» porque hacen falta 1
persona y hay 0. Un capítulo que cite la etiqueta imprimirá «el refuerzo de San Valentín cuesta 0,00 €» al lado
de «el refuerzo no cubre», que es verdad y suena a error.

**Fix (en el generador).** Añadir en `R7` la frase que ya tienen Reyes y Todos los Santos, explicando que San
Valentín se resuelve con la plantilla y por eso no hay refuerzo, y que el guion cite `H7` junto con `F7` o
ninguna de las dos.

### B12 · BAJA · Ocho hojas largas sin inmovilizar la fila de cabecera
**Libros y hojas:** `checklist-legal-y-licencias!Suministro a Otros Minoristas` (48 filas) y `Ruta Doméstica` (57) · `plan-financiero!0. Supuestos` (56), `Escenarios`, `Personal` y `Canales y Punto Muerto` · `checklist-equipamiento!Contador` (45) · `estacionalidad!Peso sobre el Año`.

**Problema.** No está en la lista de convenciones de §2.2, así que no es incumplimiento; lo anoto porque el resto
del pack sí lo hace bien (las hojas de verdad largas —`Escandallo por Tanda` con 261 filas, `Financiación` con
118, `Tesorería 12 meses`, `Checklist Legal (F1-F6)`— sí tienen `freeze_panes`), y la diferencia se nota al usarlo.

**Fix (en el generador).** `ws.freeze_panes` en la fila siguiente a la de cabecera en las ocho.

---

## Recomendación

**CORREGIR ANTES de copiar a `astro-site/public/dl/guia-pasteleria-obrador/` y antes de escribir el guion.**

Bloqueantes, por este orden y todos en el generador:

1. **A1** — `Turnos Semanales!E24` y `E25` publican 0 en el xlsx **y en el mapa**; el guion citaría 0 horas de obrador. Con ellas, **A3** (`Contador!B27`).
2. **A2** — la desviación del libro 7 compara ámbitos distintos y publica un veredicto rojo que pide rehacer el plan financiero.
3. **B1** — falta `nota_legal('PA-14')` en la hoja del huevo, y `gate_legal()` no lo ve porque no comprueba cobertura.
4. **B5** — la contradicción D/F de la hoja del huevo quita las 24 h del art. 9.3 por defecto.
5. **B2** — la nota del CTE DB-HS 3 respalda lo contrario de lo que dice PA-07.

Y **dos decisiones que no son de código y las tiene que firmar el orquestador antes de la sesión B**: si el juego
de datos publicado dice que «La Clara» no aguanta ninguna campaña (**B6**), y qué cifra de inversión y de
beneficio es la buena cuando el libro 2, el libro 5 y `datos_ejemplo` dan tres (**B3** y **B4**).

Un solo gate nuevo —recalcular a mano todo `SUM(rango)` contra su rango, que `_comun_libros_3_4.cerrar()` ya
tiene escrito— caza A1 y A3 en los ocho libros. Un segundo gate —cobertura de `IDS_LEGALES_REQUERIDOS` por
libro— caza B1 y los cuatro ids sin celda del libro 4.
