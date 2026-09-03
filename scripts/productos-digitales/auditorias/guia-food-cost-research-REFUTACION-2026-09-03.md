# REFUTACIÓN — «Guía Food Cost + Ingeniería de Menú»

**Fecha:** 2026-09-03 · **Objeto:** `guia-food-cost-RESEARCH-2026-09-03.md` y las cinco lentes (L1-L5).
**Método:** lectura íntegra de los seis documentos + verificación contra el repo (`openpyxl` sobre los xlsx vivos, lectura de `robots.txt`, `astro.config.mjs`, `products-catalog.ts`, las 8 fichas de `src/data/productos/guias/`, `fase8e-banners-corpus.py`, `guias-v2-SPEC.md`) y contra fuente externa donde el dato era fiscal o académico.
**Encargo:** tumbar la propuesta, no confirmarla. Lo que sigue son los puntos donde la propuesta **no aguanta** tal y como está escrita.

**Veredicto: CORREGIR ANTES.** El research es serio y la mayoría de sus cautelas están bien puestas, pero hay **seis defectos de gravedad alta**, y tres de ellos están justo en lo que se vende como la ventaja competitiva del producto (el IVA español), en el canal por el que se dice que entrará el dinero (los banners) y en el argumento que fija el precio. Publicar sin corregirlos significaría vender una guía fiscal con un tipo de IVA equivocado, por un canal que hoy no se puede ejecutar, a un precio decidido con una comparable falsa.

---

## A. RIGOR

### A1 · ALTA — El aceite NO va al 10 %: va al 4 % desde el 1-ene-2025, y el capítulo 04 se construye sobre eso

> **Afirmación literal** (§2.1, fila «IVA **soportado** en compras»): «**10 %** (resto de alimentos: carnes, pescados, conservas, **aceite**…)»

El **RDL 4/2024, de 26 de junio**, modificó el **art. 91.Dos.1.1.º de la Ley 37/1992** para incluir **los aceites de oliva** entre los alimentos de primera necesidad **con efectos desde el 1 de enero de 2025**, y con carácter **permanente** (no fue una rebaja temporal como las de 2022-2024, que sí caducaron). Cualquier aceite de oliva —virgen extra, virgen, refinado u orujo— tributa hoy al **4 %**.

El daño no es cosmético, es estructural:

- El **capítulo 04** propuesto se titula literalmente «El coste real de compra: 4 %, 10 % y 21 % en el mismo albarán». Su única razón de ser es enseñar a clasificar cada línea del albarán por tipo. Con el aceite en el cubo equivocado, el capítulo enseña a hacerlo mal.
- El aceite es, además, **el ejemplo estrella de volatilidad de todo el research** (L3 §4.5: 3,91 €/L → 3,22 €/L, dato de 28-ago-2026 marcado «Alta»). Va a aparecer en varios capítulos.
- Es exactamente el tipo de error del que el producto presume estar libre: §2 abre diciendo que el IVA «es **la mayor ventaja competitiva del producto**» porque «de 18 fuentes… **NINGUNA** explica…». Un competidor con un asesor fiscal delante tarda un minuto en desmontarlo.

L3 lo arrastra desde su origen: las filas 3.3 y 3.4 copian un listado de fuentes fiscales secundarias y **no incluyen el aceite en el 4 %**. La propia nota metodológica de L3 avisa de que el PDF de la AEAT no se pudo leer y de que el listado se sostiene «en tres fuentes fiscales independientes». Tres fuentes coincidentes en un listado desactualizado siguen estando desactualizadas.

**Fix:** reescribir la fila con el listado del art. 91.Dos.1.1.º **vigente**, con el aceite de oliva en el 4 % y citando el RDL 4/2024 junto al texto consolidado del BOE. Y añadir al `guion_<pid>.py` un gate que aborte si el string «aceite» aparece a menos de N caracteres de «10 %» en los capítulos 03-04.

---

### A2 · ALTA — El IVA por canal está mal: en delivery, la bebida alcohólica **y el refresco** van al 21 %

> **Afirmación literal** (§2.1, fila 1): «IVA repercutido en servicio de hostelería (comida y bebida servidas para consumo en el acto, **incluida la bebida alcohólica en sala**, y también **take away y delivery**) → **10 %**»
> **Y la única excepción declarada** (§2.1, fila 2): «IVA al **21 %** — **única excepción relevante**: venta de producto cerrado **sin servicio** (la botella sin abrir que el cliente se lleva)»
> **Y en FAQ nº6:** «¿Las bebidas alcohólicas llevan el 21 % en un restaurante? *(no: el 10 % también en sala, art. 91.Uno.2.2…)*»

Lo verificado: cuando no hay servicio auxiliar —que es exactamente el caso del reparto a domicilio y de la venta para llevar— la operación es **entrega de bienes**, y entonces manda el tipo del producto, no el 10 % del servicio. La comida elaborada va al 10 %, pero **las bebidas alcohólicas y las bebidas refrescantes / azucaradas van al 21 %**, se lleven o se repartan.

La afirmación tiene por tanto dos defectos, no uno:

1. Presenta el 10 % como aplicable a *«comida y bebida»* en take away y delivery, cuando la bebida es la excepción.
2. Reduce el 21 % a «la botella sin abrir que el cliente se lleva», cuando también alcanza **la caña, la copa y el refresco pedidos por Glovo**.

Y el error no se queda en el texto: **L5 lo cablea en la herramienta**. §3.2.2 propone `=IF(canal="alcohol para llevar",0.21,0.10)` — con esa fórmula, un refresco vendido por delivery sale al 10 %. Es el capítulo 15 («Multicanal») y la herramienta nº 2 del producto, es decir, uno de los tres diferenciadores.

Ojo también con la instrucción de L5 §3.2.7 de «**reproducir LITERALMENTE** la nota de `escandallo-maestro.xlsx!I31`». Verifiqué esa celda: dice *«10 % en restauración, INCLUIDA la bebida alcohólica servida **en sala**…»*. Es correcta **porque está acotada a la sala**. Copiarla tal cual a una carta de bodega que incluye venta para llevar, o a un simulador multicanal, es sacarla de su ámbito.

**Fix:** la regla no son dos casillas, son seis — {sala, take away, delivery} × {comida, refresco/azucarada, alcohol}. Escribirla como matriz en el capítulo 03, y en los xlvs sustituir el `IF` binario por un `VLOOKUP` sobre esa matriz de 6 celdas editables. Antes de escribir, contrastar con una consulta vinculante de la DGT sobre plataformas de reparto (existe, la cita e-consulting), no con blogs sectoriales.

---

### A3 · MEDIA — El umbral de prime cost del 60 % es de EE. UU. y lo desmiente la propia fuente española del research

> **Afirmación literal** (§9, cap. 08): «**Prime cost: la métrica que de verdad mide la salud del negocio** — Food cost + personal, **el umbral del 60 %**…»
> Y §5: «Prime cost (food + personal) ≤ **60 %** de la venta; > 65 % hace muy difícil ser rentable… **Toast (EEUU…)**»

El research lo marca como EE. UU. y dice que se citará como «convención de sector, no como dato español». Pero el capítulo lo enuncia sin matiz («el umbral del 60 %») y, sobre todo, **choca con la única fuente española de fiabilidad Alta que tiene el propio research**: CaixaBankLab × elBulliFoundation da **producto 30 % + personal 30-35 %** para servicio en mesa, con **EBITDA sano del 10-13 %**. Es decir: un restaurante español de servicio completo, sano y rentable, tiene un prime cost de **60-65 %** por construcción.

Enseñado como está, el capítulo le dice al lector español típico que está por encima del umbral cuando está exactamente donde debe estar. Es un falso positivo aplicado al 100 % del público objetivo principal.

**Fix:** en el capítulo, derivar el umbral de la estructura española (30 % + 30-35 % → **65 % para servicio en mesa**, **~55 % para barra/autoservicio** con el 15-25 % de personal de la misma fuente) y usar el 60 % de Toast solo como contraste declarado de EE. UU. El semáforo de `cuadro-de-mando-prime-cost.xlsx` debe llevar el objetivo **en celda editable y sembrado con el valor español**, no con el americano.

---

### A4 · MEDIA — Los «3 métodos» de la herramienta estrella no son tres votos independientes, y la fórmula de Pavesic propuesta no es la de Pavesic

> **Afirmación literal** (§7.2, herramienta 1): «Cuando los 3 métodos **coinciden** en marcar un plato, es señal de **alta confianza** para reformular/retirar sin más análisis»

Hay tres variables en juego —popularidad, margen de contribución y food cost %— y cada método toma **dos de las tres**: Kasavana & Smith = popularidad × MC; Miller = food cost % × popularidad; Pavesic = food cost % × MC ponderado. No son tres mediciones independientes: son las tres parejas posibles del mismo trío. Un plato con popularidad alta, MC alto y FC % bajo sale «bien» en los tres **por aritmética**, no por triangulación. Y la discrepancia que se vende como hallazgo («típico del marisco: margen absoluto alto, food cost % pobre») no es una señal emergente: es la diferencia determinista y conocida entre el eje MC y el eje FC %, que se puede explicar en un párrafo sin construir tres hojas.

Peor: **la fórmula de Pavesic que especifica L5 no es la de Pavesic.** §3.2.1 escribe «Pavesic (índices **ponderados** MCI/CMI)» pero luego define `CMI = CM_plato/CM_medio`, que es el margen **sin ponderar**. Pavesic (1983) usa el **margen de contribución ponderado** (MC × unidades vendidas). Con la fórmula tal como está escrita, el eje de Pavesic pasa a ser idéntico al de Kasavana & Smith y el «tercer método» se convierte en «K&S con FC % en el otro eje». La herramienta diferenciadora nº 1 quedaría con dos métodos y medio.

Y la definición que va al texto también se queda coja: §9 cap. 12 resume Pavesic como «(margen ponderado)» y **omite su eje característico, el food cost %**, que es justo lo que Kasavana & Smith decidieron ignorar y lo que hace de Pavesic un «tercer enfoque».

**Fix:** (a) corregir `CMI` a `(CM_plato × uds) / media ponderada`; (b) sustituir el marco de «alta confianza por coincidencia» por lo que sí es cierto y vendible: «cada método pregunta algo distinto, y el mapa de **dónde discrepan** es el diagnóstico»; (c) si se quiere un tercer voto realmente independiente, el candidato es **Goal Value (Hayes & Huffman)**, que no es matricial y no usa promedios; (d) escribir la definición completa de Pavesic (food cost % × MC ponderado) en el capítulo 12.

---

### A5 · MEDIA — El capítulo 12 promete cuatro métodos y el Excel implementa dos

> **Afirmación literal** (§9, cap. 12): «**Miller, Pavesic** (margen ponderado), **Hayes & Huffman** (Goal Value) y **LeBruto** (con mano de obra): qué añade cada uno»
> Frente a §7.2 herramienta 1, hojas: «`Datos` · `Kasavana-Smith` · `Miller` · `Pavesic` · `Comparativa`»

El lector lee sobre Goal Value y sobre el modelo con mano de obra, va al libro de Excel y no los encuentra. En un producto cuyo argumento es «documento + herramienta viva», ese desajuste es la reseña de 3★ escrita sola («explica cosas que luego no puedes aplicar»).

**Fix:** o se añade la hoja `Goal-Value` (es una fórmula algebraica de una columna: barata) y se cita LeBruto como lectura, o el capítulo 12 se reordena para dejar claro qué está implementado y qué es contexto histórico. Decidirlo **antes** de escribir el guion, no después.

---

### A6 · MEDIA — Wansink como «lo demostrado» en el capítulo que separa lo demostrado de la leyenda

> **Afirmación literal** (§9, cap. 10): «**Psicología de precios: lo demostrado y lo que es leyenda** — Nombres descriptivos (**+27 %, Wansink 2001**), símbolo de moneda (Cornell 2009), efecto señuelo; y lo que circula sin estudio detrás.»

El paper (Wansink, Painter & van Ittersum, 2001, *Cornell HRAQ*) **no consta retractado** — eso hay que decirlo. Pero su primer autor fue objeto de una investigación de Cornell que en 2018 concluyó que había incurrido en mala conducta académica, dimitió, y acumula del orden de 18 retractaciones, varias de ellas de estudios de campo con la misma metodología (restaurante, muestra pequeña, resultados redondos). Poner una cifra suya como el ejemplo canónico de «lo demostrado», en el único capítulo cuyo propósito declarado es distinguir la evidencia del mito, es exactamente el sitio donde no conviene tener ese flanco abierto.

Añado un matiz que el research no recoge: **Yang, Kimes & Sessarego (2009) mide el efecto de omitir el símbolo `$`**, en dólares y con comensales estadounidenses. Trasladarlo al `€` español sin decirlo es el mismo pecado que §2.2 denuncia («no trasladan limpio»).

**Fix:** o se cita Wansink con la salvedad explícita («publicado en 2001; su autor fue después sancionado por mala conducta científica y el hallazgo no ha sido replicado de forma independiente»), o se sustituye por evidencia posterior. El efecto señuelo (Emerald 2024, con DOI, revisado por pares) es la pieza sólida del capítulo y debería ser la protagonista, no la tercera de la lista.

---

### A7 · MEDIA — El bonus de 20 ejercicios no cabe: salen a 300-350 palabras por ejercicio, y la cuenta de páginas no da

> **Afirmación literal** (§7.1): «`BONUS-20-ejercicios-resueltos` — 20 ejercicios resueltos paso a paso (escandallo con merma, PVP por 4 métodos, clasificación de una carta con los 3 modelos, repricing de delivery, coste por lote, prime cost) — **~6.000-7.000 palabras → ~16-18 páginas**»

Dos problemas, uno aritmético y otro de fondo:

- **Aritmético:** con la calibración que el propio documento usa (410 palabras/página con `PageBreak`), 6.000 palabras son **14,6 páginas**, no 16. Con la referencia del bono del kit (6.848 → 17 pp = 403 p/p), 6.000 son 14,9. El «16-18» solo se cumple a partir de ~6.500 palabras. Es un «+» que el gate de PyMuPDF va a tumbar en el extremo bajo del rango.
- **De fondo, que es el grave:** 20 ejercicios en 6.500 palabras son **325 palabras cada uno**, enunciado incluido. «Clasificación de una carta con los 3 modelos» y «repricing de delivery» no son ejercicios de 325 palabras: son tablas. La demanda existe («menú engineering ejercicios resueltos» aparece como búsqueda relacionada), y precisamente por eso entregar veinte resúmenes en vez de ejercicios resueltos es la peor forma de atenderla.

**Fix:** **10-12 ejercicios de 550-700 palabras** con su tabla, o mantener 20 y subir el bonus a ~11.000-12.000 palabras asumiendo el coste de tokens. La decisión es de John (afecta al presupuesto de la semana B), pero «20 × 300 palabras» no es una opción defendible.

---

### A8 · BAJA — El dato de inflación que se va a citar nace caducado

> **Afirmación literal** (§5): «Inflación de alimentos — **+3,2 % interanual en febrero 2026** (último dato exacto disponible)»

Es honesto sobre su hueco (el interanual de agosto no está publicado en la nota consultada), pero el producto se publicará en otoño de 2026 citando un dato de **febrero**, cuando el propio L3 §4.1 registra que el IPC general ha pasado de 2,3 % (feb) a 3,6 % (jul) y 4,3 % (adelantado de agosto). Un lector que abra el INE el día que compra la guía verá otra película. Además, la propia batería de `documentos.py` tiene gates de **fechas caducas**.

**Fix:** aplicar aquí la regla que el research defiende en §4 y no cumple en §5: **no citar la cifra**. El capítulo 18 enseña a leer la nota mensual del INE y el Observatorio del MAPA; el número concreto sobra y es pasivo puro.

---

### A9 · BAJA — Cifras marcadas «no publicar» que siguen impresas en la tabla, y un fichero que no existe

- §5 imprime «**Marisquería 40-42 %**» en la tabla de benchmarks con la nota «Baja — **NO publicar sin segunda fuente**». En la lista negra del §15 vuelve a aparecer. Que esté en dos sitios como «no publicable» y en un tercero como fila de tabla es exactamente cómo un dato sin fuente sobrevive a la siguiente capa. **Fix:** sacarlo de la tabla y dejarlo solo en la lista negra del `guion_<pid>.py`.
- §2.3 dice «y **sus PDF/DOCX publicados**» del bono del kit. En `astro-site/public/dl/kit-escandallos/` solo existe **`BONUS-guia-food-cost-30-dias.pdf`** — no hay `.docx`. Trivial, pero es una instrucción operativa que mandaría a alguien a corregir un fichero inexistente.

---

## B. NEGOCIO

### B1 · ALTA — El canal nº 1 por el que se dice que entra el dinero es hoy un *no-op*

> **Afirmación literal** (§0, tabla de canales): «Banners en el blog ES — **Añadir el producto 45 al catálogo y reejecutar la rotación**»

Verificado en el código: `scripts/astro-migration/fase8e-banners-corpus.py`, línea 234:

```python
if 'utm_medium=banner' in cuerpo:
    return None, 'ya tiene banners'
```

El script **salta cualquier post que ya tenga banners**, y desde el 2026-08-31 los tienen **los 325 posts ES**. Reejecutarlo tras añadir el producto 45 no insertará absolutamente nada: el nuevo producto no aparecerá en ningún banner del blog. Y el otro script, `fase8c-libreria-assemble.py`, tampoco sirve: reconstruye el cuerpo desde el `.txt` de bridge y pisaría lo publicado (gotcha documentado en CLAUDE.md, con `cocina-molecular` como precedente).

Esto no es un detalle de implementación: §0 concluye que «este producto se lanza… porque **tenemos el canal**», y el primer canal de los cuatro es este. Si el plan de distribución falla, el argumento de lanzamiento se queda con la lista de clientes y el hub.

**Fix:** decidir en la semana A —no en la C— cuál de las tres vías se ejecuta: (a) un modo `--rebalancear` en `fase8e` que **sustituya** uno de los tres banners existentes por el nuevo producto en los posts donde toque, con el mismo gate byte a byte que ya tiene; (b) inserción manual quirúrgica en los 6 posts temáticamente relevantes (mínimo viable, ~1 hora); (c) asumir que el blog no distribuye este producto y rehacer §0 sin ese canal. Nótese que (a) es trabajo de script nuevo con su propio gate, y eso **entra en el presupuesto de tokens de la semana**.

---

### B2 · ALTA — La canibalización va del producto barato al caro, y esa dirección no se analiza

> **Afirmación literal** (§12.2): «**Quien tenga las dos no compra nada repetido**: la matriz de la guía gastronómica entra aquí como **una hoja de cinco** dentro de la herramienta multi-método.»
> Y §7.2, herramienta 1: «La hoja `Menu Engineering` completa de `menu-engineering-matrix.xlsx`… entra **tal cual** como hoja «Kasavana-Smith»»
> Y §17 nº2, sobre `ficha-escandallo-base.xlsx`: «Coste: le quita **un poco de exclusividad al Kit de 12 €**.»

El análisis está hecho en un solo sentido (quien compró la de 85 € no repite) y el problema real está en el otro: **la Guía Restaurante Gastronómico (85 €) entrega diez plantillas Excel, y la propuesta reempaqueta dos de ellas dentro de un producto de 49 €** —`menu-engineering-matrix.xlsx` «tal cual» y `escandallo-maestro.xlsx!Ficha (plantilla)` como `ficha-escandallo-base.xlsx`—. Verifiqué que son ficheros vivos de `dl/guia-restaurante-gastronomico/`.

Consecuencias que la síntesis no recoge:

- Un comprador que dude entre las dos y compare los dos listados de entregables ve la misma matriz en las dos. Con IVA correcto y con food cost, lo racional es comprar la de 49 €.
- La ficha de escandallo maestro es, según el propio L5, «**exactamente el motor** que alimenta el escandallo por plato»: es el corazón del producto de 85 €.
- El coste de §17 nº2 está mal contabilizado: no es «un poco de exclusividad al Kit de 12 €», es **el activo diferencial del producto más caro del catálogo**.

**Fix:** o la herramienta 1 **reconstruye** la hoja Kasavana-Smith (mismas fórmulas, otros datos de ejemplo, sin ser el mismo fichero) y `ficha-escandallo-base.xlsx` se recorta a una ficha mínima de una hoja sin el bloque `Resumen`/`INDIRECT` de la maestra, o se sube el precio y se asume la solapa. Es decisión de John, pero tiene que tomarla con esta dirección de la canibalización sobre la mesa, no con la contraria.

---

### B3 · ALTA — La comparable que fija el precio está mal contada

> **Afirmación literal** (§8.1): «**Guías «Cómo Montar»** · 65 € · 20 capítulos, 60+ páginas, **10 plantillas + 8 checklists**»
> Y §8.3 arg. 3: «por debajo de las guías «Cómo Montar» (65 €), que traen **10 plantillas + 8 checklists** + business plan»
> Y §8.3 alternativa 65 €: «**Solo defendible si el paquete iguala su recuento**»
> Y §7.2: «Comparable en volumen al paquete de las guías de 65 € (**20 capítulos + 10 plantillas + 8 checklists**)»

Verificado fichero a fichero en `astro-site/src/data/productos/guias/`:

| Producto | Precio | Capítulos | Plantillas Excel | Checklists |
|---|---|---|---|---|
| `guia-restaurante-casual` | 65 € | 20 | **8** | **6** |
| `guia-restaurante-japones` | 65 € | 20 | **8** | **6** |
| `guia-restaurante-mexicano` | 65 € | 20 | **8** | **6** |
| `guia-restaurante-peruano` | 65 € | 20 | **8** | **6** |
| `guia-panaderia-obrador` | 65 € | 20 | **9** | **6** |
| `guia-restaurante-nikkei` | 65 € | 20 | **9** | **6** |
| `guia-restaurante-gastronomico` | **85 €** | 22 | **10** | **8** |

El «10 plantillas + 8 checklists» es **la de 85 €**, no las de 65 €. El error se repite tres veces y **es el argumento que descarta el precio de 65 €**: la síntesis dice que igualar a las «Cómo Montar» obligaría a subir a 80+ páginas y añadir checklists — con los números reales, la barra a igualar es **20 capítulos + 8-9 plantillas + 6 checklists**, y la propuesta ya lleva **20 capítulos + 7-8 libros de Excel** con densidad muy superior por fichero. La diferencia real entre el paquete propuesto y una guía de 65 € son **6 checklists y dos documentos bonus** (business plan modelo y manual), no un abismo.

También se cuela un dato menor en la misma tabla: «Guía Dark Kitchen · 24 € · **13 capítulos**». Son **12** (`guia-dark-kitchen.ts:20` y `:34`).

**Fix:** rehacer §8.1 con los recuentos reales y **volver a decidir el precio con ellos**. No estoy diciendo que 49 € esté mal; estoy diciendo que la razón por la que se descartó 65 € no era cierta, y que la banda 55-65 € vuelve a estar sobre la mesa.

---

### B4 · ALTA — El `priceOld` de 140 € es el riesgo legal que la SPEC de la familia ya tiene escalado a John como «alta»

> **Afirmación literal** (§8.3): «**49 €** · precio de lanzamiento · ancla `priceOld` **140 €** (−65 %)… **El `priceOld` de 140 €** mantiene la profundidad de descuento de la familia».

El art. 20 del TRLGDCU tras el RDL 24/2021 (Directiva Ómnibus) exige que el precio anterior anunciado sea **el más bajo aplicado en los 30 días previos**. Un producto **nuevo** no ha tenido ningún precio en los 30 días previos, así que un tachado de 140 € no es un descuento: es un precio de referencia inventado.

Y esto no es una objeción teórica de un refutador: **está escrito en el repo**. `guias-v2-SPEC.md` §7.3, ficha **COM-13**, gravedad **alta**, «para John»: describe literalmente el ancla de 220/180/90 €, cita el art. 20 y el RDL 24/2021 y remata «el "HOY" y el "lanzamiento" perpetuos son el agravante clásico». La síntesis propone replicar ese patrón en un producto nuevo **sin mencionar que el problema está abierto**.

**Fix:** (a) no proponer `priceOld` en el research y dejarlo como decisión explícita de John junto a COM-13; o (b) si se quiere el ancla, que sea un **«valor del paquete si se comprara suelto: 140 €»** con el desglose que lo sostiene (que además la casa ya sabe construir: `kit-escandallos.ts:288` lo hace), no un precio tachado; o (c) lanzar realmente a 140 € y bajar después de 30 días. Cualquiera de las tres es defendible; la actual no.

---

### B5 · MEDIA — La escalera de precios omite el vecino más parecido, y 49 € es el número tachado del Kit

La tabla §8.1 «La escalera propia» no incluye dos productos vivos de `products-catalog.ts`:

- **`kit-plan-financiero` — 39 €.** Es el comparable interno más cercano en precio **y en forma**: un kit de libros de Excel con fórmulas, relanzado en v2.0 hace cinco días. La pregunta «¿por qué esto vale 49 € si el Kit Plan Financiero vale 39 €?» va a existir y el research no la responde porque no lo menciona.
- **`mega-pack-tareas` — 89 €**, que es en realidad el techo del catálogo, no los 85 € de la guía gastronómica.

Y un detalle de escaparate que no vi en ninguna lente: **`kit-escandallos.ts:283` fija `priceOld: '€49'`**. Es decir, la landing del Kit de Escandallos muestra hoy «~~€49~~ €12». Poner el producto nuevo a **49 €** significa que en el hub, uno al lado del otro, el cliente ve el mismo número como «precio tachado del kit barato» y como «precio del producto nuevo». Es el peor anclaje posible para el producto nuevo.

**Fix:** completar la escalera, responder a la comparación con `kit-plan-financiero` (39 €) y, si se mantiene la franja, elegir **47 € o 52 €** en lugar de 49 € para no chocar con el tachado del Kit.

---

### B6 · MEDIA — El vocabulario LATAM no resuelve las dos cosas que un comprador de LATAM ve primero: la moneda y «costo»

> **Afirmación literal** (§11): «Se usa un vocabulario que funcione en **los cuatro mercados**» + §2.2 «La casilla de IVA de las herramientas va **EDITABLE**, nunca fija».

Tres huecos, por orden de impacto:

1. **La moneda está cableada.** Verifiqué con `openpyxl` `10-calculadora-pvp.xlsx`: los formatos numéricos son `'#,##0.00 €'`, celda a celda. Toda la familia de xlsx está construida así. Un comprador de México, Argentina o Uruguay abrirá **siete u ocho libros con el símbolo € en cada importe**. La casilla de IVA editable no arregla eso, y cambiar el formato en centenares de celdas de ocho ficheros no es algo que se le pueda pedir al cliente.
2. **«Coste» vs «costo».** La tabla de vocabulario resuelve escandallo/costeo, PVP/precio de venta, plato/platillo, carta/menú… y no dice nada de la palabra **más repetida de todo el producto**. En España es «coste»; en los cinco mercados LATAM es «costo». Un documento de 28.000 palabras que diga «coste» 400 veces suena español, no neutro.
3. **Los mercados del research no son los del negocio.** El encargo dice que los clientes reales de LATAM son **GT / PA / MX / AR / UY**. L4 y §11 trabajan **ES / MX / AR / CO** (+ PE en los casos). **Guatemala, Panamá y Uruguay no aparecen en ninguna de las cinco lentes**, y §11 menciona explícitamente «Rappi y DiDi Food» solo para México cuando en Panamá y Uruguay el reparto es otro (PedidosYa domina el Cono Sur).

**Fix:** (a) decidir si los xlsx se entregan con **formato de moneda neutro** (`#,##0.00` + una celda «Moneda» que se pinta en las cabeceras) o con una segunda variante; es una decisión de motor, se toma ahora, no en la semana B; (b) añadir «costo» al glosario con criterio de uso; (c) o se declara que la v1 es **para España** y la landing lo dice, o se cierra el hueco de GT/PA/UY antes de prometer neutralidad.

---

### B7 · MEDIA — La FAQ del producto no responde ninguna objeción de compra, y sus dos primeras preguntas contradicen al capítulo 01

> **Afirmación literal** (§14): «FAQ del producto (12 preguntas, **todas con demanda medida**)», encabezada por «1. ¿Qué es un escandallo en hostelería…? *(PAA)*» y «2. ¿Cómo se calcula el escandallo de un plato, paso a paso? *(PAA)*»

Tres problemas encadenados:

- **Las dos primeras son definicionales**, y §0 ya demostró que **esta landing no va a captar por búsqueda**. Así que no cumplen la función SEO que justificaría tenerlas, y sí contradicen el capítulo 01 («por qué no volvemos a explicar qué es un escandallo») y la lección de la reseña 1★ que el propio research eleva a brief («un tercio de las páginas explicando matrices básicas»). Lo primero que lee un comprador cualificado es exactamente lo que le hizo poner una estrella al competidor.
- **Falta la objeción que la competencia sí declara.** L1 registra que la plantilla de `ingenieriademenu.com` avisa: «**compatible solo con Excel de escritorio (no Sheets/Numbers)**». Nuestros libros usan `SUMPRODUCT`, `INDIRECT` y validaciones; `INDIRECT` con nombres de hoja entre comillas es precisamente lo que se rompe o degrada fuera de Excel. Nadie ha comprobado qué pasa al abrirlos en Google Sheets o Numbers, y la FAQ no dice nada. Es la pregunta nº 1 de un comprador de LATAM con Sheets.
- **Se cae la objeción 7 de L4** («no me fío de comprar un documento digital sin poder probarlo») sin decir por qué, y no hay ninguna pregunta sobre **garantía/devolución**, **actualizaciones** («si cambia el IVA, ¿me llega la versión nueva?» — pregunta obligada en un producto que se vende por su fiscalidad) ni **acceso vitalicio**.

**Fix:** mover 1 y 2 al cuerpo de la guía o al blog; añadir tres preguntas de compra (compatibilidad —tras **probarlo**—, actualizaciones, devolución) y mantener las de hueco temático, que sí son buenas.

---

### B8 · MEDIA — No hay capítulo para dos de los cinco perfiles de comprador que el propio research define

L4 construye cinco personas y §7 del research las hereda. El índice de 20 capítulos cubre a Carlos (restaurante), Marisol (delivery, cap. 15), Ana (obrador, cap. 17) y Diana (bar, cap. 16). **No cubre a Javier, director de A&B de hotel** —persona 3, cuyo referente real (Angelo Vassallo, Fairmont) es además una de las diez citas primarias del research— **ni el catering/eventos**, pese a que el Kit tiene plantilla de catering y el catálogo tiene dos planes de negocio de eventos. L4 objeción 6 pide explícitamente «al menos un ejemplo o mención por formato (sala, delivery, bar, obrador, **hotel**)».

**Fix:** o el capítulo 14 («Carta corta y menú de precio fijo») absorbe buffet/banquete y eventos con su propio epígrafe y su ejemplo, o se retira la persona 3 del material de marketing. Vender a un director de A&B una guía que no menciona el buffet es garantizar la devolución.

---

### B9 · MEDIA — El simulador multicanal, como está especificado, no permite tomar la decisión que promete

> **Afirmación literal** (§7.2, herramienta 2): «Cuánto subir el precio en cada canal sin perder margen tras comisión, y **qué platos excluir del delivery** porque no aguantan la comisión»

Dos defectos de especificación, verificables sobre el motor que dice reutilizar (`10-calculadora-pvp.xlsx!G18 = $C$4*E18/(1-F18)`, con `E18=1/AVERAGE(FCmin,FCmáx)` — confirmado con `openpyxl`; la reformulación de L5 como `coste/(FC×(1−comisión))` es correcta):

1. **La hoja no declara qué es entrada y qué es salida.** El motor heredado **calcula** el PVP a partir del food cost objetivo; la hoja `Multicanal` propuesta lista «PVP sala / PVP take-away / PVP delivery» como si fueran datos del usuario. Con el PVP como salida, la fórmula **siempre** devuelve el FC objetivo y nunca puede señalar un plato inviable; con el PVP como entrada, hace falta la fórmula inversa, que no está escrita. Sin resolver esto, la herramienta o no decide nada o no calcula nada.
2. **El packaging es por PEDIDO y la hoja es por PLATO.** El dato del research (L3 §5.5: 1,35-2,15 €/pedido) no se puede imputar a un plato sin un input de «platos por pedido» / ticket medio de delivery, que no aparece en ninguna hoja. Y es una partida grande: 1,75 € sobre un plato de 12 € son 14 puntos de margen.
3. Falta el input que hace posible la decisión de excluir: **el precio máximo que el mercado acepta en la app** para ese plato. Sin techo, la respuesta a «no aguanta la comisión» siempre es «sube el precio».

**Fix:** especificar la hoja con dirección explícita (`Coste` + `Comisión` + `Packaging/pedido` + `Platos por pedido` + `Precio techo` → `PVP necesario`, `FC % resultante`, `¿viable?`) antes de construirla, y verificarla con pycel como cualquier otra.

---

### B10 · MEDIA — «Capa comercial»: la orden de John era no TOCAR lo existente, no fabricar lo nuevo

> **Afirmación literal** (§17 nº8): «**Capa comercial:** ¿testimonios y ratings nuevos para esta landing, o se mantiene la **política vigente de no tocar** la capa comercial (orden del 29-ago)?»

La pregunta está bien planteada pero le falta el contexto que hace que se pueda responder: `guias-v2-SPEC.md` §7.3 documenta que las ocho landings de guías emiten `aggregateRating 4,9 / 8 reseñas` sobre **ocho testimonios redactados con avatares de stock**, lo llama «**64 reseñas inventadas** publicadas como dato estructurado», y cita el art. 20 y 20 bis del TRLGDCU tras la Ley 4/2022 más las políticas de rich results de Google, con **riesgo de acción manual sobre todo el dominio**. Está fichado como **COM-12, gravedad alta, para John**.

«No tocar lo que ya está publicado» y «crear ocho testimonios nuevos y un `aggregateRating` nuevo para un producto que aún no ha vendido una sola unidad» no son la misma decisión. Presentarlas como las dos caras de la misma pregunta invita a la respuesta equivocada por inercia.

**Fix:** reformular la decisión nº 8 como: «un producto nuevo **no puede** tener `aggregateRating` (no hay compradores). ¿Se lanza sin él —lo correcto— o se replica el patrón de la familia, sabiendo que COM-12 sigue abierto?».

---

### B11 · MEDIA — El capítulo 20 desmonta el argumento de venta principal

> **Argumento de venta** (§8.3 nº2): «49 € es el **4,3 %** de lo que cuesta un año de la función equivalente en Haddock o tSpoonLab (1.140 €/año), **y es tuyo para siempre**»
> **Capítulo 20:** «**Cuándo tu Excel se queda corto** — Hoja de ruta Excel → software de food cost → agentes de IA, con el criterio para decidir el salto»

La landing dice «no necesitas pagar 95 €/mes»; el capítulo 20 dice «esto es cuándo tienes que pagar 95 €/mes». Las dos cosas son verdad y el embudo hacia la plataforma tiene sentido, pero **no pueden convivir sin una frase que las reconcilie**, o el lector siente que le han vendido el sustituto de algo y en la página 200 le dicen que compre el original. Añado que la comparación tampoco es limpia: los 1.140 €/año de Haddock son **sin IVA y por establecimiento**, y son un sistema que digitaliza facturas y recalcula solo — no un documento.

**Fix:** una frase de posicionamiento honesta y mejor: «esto te da el **criterio**; el software te da la **automatización**. Con el criterio, el software te sirve; sin él, te da números que no sabes leer». Y citar el SaaS como «más de 1.100 € al año, IVA aparte, por local», no como equivalente funcional.

---

### B12 · BAJA — «60+ páginas» va contra la decisión que la propia familia ya tomó

> **Afirmación literal** (§7.1): «**Promesa de landing: «60+ páginas»** — se cumple con margen»

`guias-v2-SPEC.md` §7.2.3 dice, sobre exactamente esta cuestión: «*Recomiendo la cifra exacta medida*: es mayor que la prometida, **deja de ser un «+» inverificable** y da un dato que el comprador puede comprobar en el primer segundo. **Aplica a las 8**». Proponer un «60+» en un producto nuevo va en dirección contraria a la política que la familia está adoptando, y encima infra-vende (la aritmética del propio §7.1 da 68-73 páginas).

**Fix:** construir primero, medir con PyMuPDF, y poner la cifra medida. En la landing, «**68 páginas**» vende más y es verificable.

---

## Lo que falta para que John pueda decidir con seguridad

1. **Reverificar el bloque fiscal entero antes de escribir los capítulos 03 y 04.** El listado del 4 % con el aceite de oliva (RDL 4/2024), y la matriz de 6 casillas de IVA repercutido {sala, take away, delivery} × {comida, refresco, alcohol}, contra el texto consolidado del BOE y una consulta vinculante de la DGT sobre plataformas de reparto. **Bloqueante**: sin esto, el diferenciador del producto es el defecto del producto.
2. **Cómo se distribuye realmente.** `fase8e` no puede reinsertar. Elegir entre modo `--rebalancear` (script nuevo + gate, con coste de tokens), inserción manual en los 6 posts, o rehacer §0 sin ese canal.
3. **El chequeo de GSC `page × query`** que el propio §16 deja pendiente: si los 6 posts propios canibalizarían la landing. Son cinco minutos y condiciona el §13.
4. **Reabrir el precio con los recuentos reales** (8-9 plantillas + 6 checklists a 65 €; `kit-plan-financiero` a 39 €; el `priceOld €49` del Kit) y decidir aparte el ancla `priceOld` a la luz de COM-13.
5. **Decisión sobre reempaquetar activos de la guía de 85 €** (`menu-engineering-matrix.xlsx` tal cual y la ficha de `escandallo-maestro.xlsx`), con la dirección correcta de la canibalización sobre la mesa.
6. **Verificación en pycel de las 7-8 herramientas.** Hoy son diseño, no ficheros; L5 lo declara. Añadir a esa verificación la **compatibilidad con Google Sheets / Numbers**, que nadie ha probado y que es objeción de compra declarada por la competencia.
7. **Fuente española (o declaración explícita) del umbral de prime cost**, y semáforo del cuadro de mando sembrado con el valor español.
8. **Decisión de moneda** en los xlsx (formato neutro vs €) y de vocabulario («costo»), y qué mercados se declaran: los del research (ES/MX/AR/CO) no son los del negocio (GT/PA/MX/AR/UY).
9. **Presupuesto de palabras no uniforme**: el capítulo 19 (caso integral: 12 platos × 3 métodos + repricing) y el bonus de ejercicios no caben en la asignación plana de 1.400-1.500 palabras. Decidir dónde va el margen antes de arrancar bridge.
10. **`aggregateRating` y testimonios del producto nuevo**: decisión explícita, separada de la orden de «no tocar» del 29-ago.
11. **Fiscalidad de la venta del propio producto** (IVA de servicios prestados por vía electrónica a consumidores UE, ventanilla única OSS, y qué pasa con los clientes de LATAM). No aparece en ninguna de las cinco lentes ni en la síntesis, y es una guía cuyo argumento es que el IVA está bien puesto.
12. **Confirmar que el bono del kit se corrige en la misma pasada** (§17 nº3) — coincido con la recomendación del research, y añado: si se toca ese fichero, corregir también ahí el IVA por canal completo, no solo el «21 % → 10 %».
