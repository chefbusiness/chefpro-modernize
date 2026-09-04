# REFUTACIÓN — «Manual del Manager de Restaurante»

**Fecha:** 2026-09-04 · **Objeto:** `manual-manager-RESEARCH-2026-09-04.md` y las cinco lentes (L1-L5, L3 leída íntegra).
**Método:** lectura completa de los seis documentos + verificación **contra fuente primaria** —textos consolidados del BOE, **el PDF de la modificación del ALEH publicada hoy descargado y extraído con PyMuPDF**, un barrido de los **247 sumarios del BOE del 1-ene al 4-sep-2026** vía la API de datos abiertos, la API Tempus del INE y `last.app/precios`— y **contra el repo**: `openpyxl` sobre los xlsx vivos (censo de nombres de hoja sobre los **432** libros publicados en `astro-site/public/dl/`), PyMuPDF sobre los PDF de la Guía Food Cost, ejecución real de `robots-gate.py`, de `catalogo_productos()` y del clasificador de `fase8d-faq-duplicadas.py`, y lectura de `documentos.py`, `guion_guia_food_cost_ingenieria_menu.py`, `guia-food-cost-SPEC.md`, `use-cases.ts`, `GuiaLandingPage.astro`, `fase8f-guia-food-cost-blog.py` y `astro-site/src/data/productos/guias/*.ts`.
**Encargo:** tumbar la propuesta, no confirmarla. Lo que sigue son los puntos donde **no aguanta tal como está escrita**.

---

## VEREDICTO: **CORREGIR ANTES**

Es el research más sólido de los tres que lleva la familia. L3 es un trabajo legal de nivel profesional, la lista negra existe **antes** de escribir una línea, y **el hallazgo del ALEH es real: lo he verificado con el texto del BOE en la mano, artículo por artículo**. De las **20 afirmaciones normativas** que mandé verificar contra fuente primaria, **13 salen confirmadas al pie de la letra** y la ausencia de las dos normas que se dan por no vigentes está probada con un barrido de los 247 sumarios del BOE de 2026.

Pero hay **10 defectos de gravedad ALTA**, y están repartidos exactamente donde más caro sale:

- **tres en el contenido que es el argumento de venta** — una cotización de Seguridad Social 9 puntos por debajo de la real cableada en la herramienta estrella (A1); un permiso parental que el research da por no retribuido cuando desde el 31-07-2025 hay **dos semanas que sí lo están** (A2); y un ALEH que no resuelve lo que se dice que resuelve, justo en el capítulo que fija la autoridad del producto (A3);
- **dos en el precio** — 65 € contradice una decisión firmada **ayer** para un paquete idéntico (B1), y el ancla externa que lo sostiene contiene una frase comprobablemente falsa (B2);
- **dos en el paquete** — tres de los ocho libros repiten material que el comprador objetivo ya tiene (B3), y tres capítulos del eje «personas» no traen ninguna herramienta del manual (B4);
- **tres en la ejecución** — un enlace de la landing que sería un **404** (C1), seis reglas legales que llegarán al redactor con la orden de **no citar su artículo** (C2), y un plan de banners que, ejecutado con el script existente, **borraría del blog los propios cross-sell del manual** (C3).

Y de las 22 cifras del §5 verificadas contra la fuente, **once no dicen exactamente lo que se les atribuye** (A11) — entre ellas la que justifica la herramienta nº 1.

Ninguno obliga a rehacer el research. Los diez se arreglan **antes** de escribir la SPEC, y cinco son una decisión, no un trabajo.

---

## A. RIGOR

### A1 · ALTA — La Seguridad Social del cuadro de mando (23,60 %) está 9 puntos por debajo de la real y de la que usan los dos productos que dice reutilizar; convierte el semáforo de prime cost en un falso negativo

> **Afirmación literal** (§3.3, herramienta 1): «objetivos de food cost %, labor cost % y prime cost %, **SS a cargo de la empresa 23,60 %** (MM-17, celda con nota)»
> Y §8, cap. 04: «del salario bruto al coste-empresa (**SS 23,60 %**, tope de base)»

El 23,60 % es **sólo el tipo de contingencias comunes a cargo de la empresa**. La propia entrada `MM-17` lo dice sin querer: «Tipo de cotización **por contingencias comunes** del 28,30 %, del que la empresa paga el 23,60 %». La `cifra` del id es correcta; **el rótulo con que se propone usarla, no**.

El total real a cargo de la empresa en hostelería para 2026, verificado contra la Orden PJC/297/2026 y la DA 61.ª del TRLGSS, es **32,15 %** con contrato indefinido y **33,35 %** con temporal: contingencias comunes 23,60 + desempleo 5,50/6,70 + AT/EP 1,50 + FOGASA 0,20 + FP 0,60 + MEI (cuota empresarial) 0,75. Triangulado además con la propia EACL del INE, donde el cociente cotizaciones/salarios en hostelería da **34,92 %**.

Y no hace falta discutirlo en abstracto, porque **el catálogo ya usa el 33 % en los dos ficheros que la propuesta dice reutilizar**, verificado abriendo los xlsx publicados:

| Fichero publicado | Celda / texto | Valor |
|---|---|---|
| `astro-site/public/dl/kit-gestion-personal/03-coste-laboral-mensual.xlsx` | `Nóminas!A2` «Tipo de SS a cargo de la empresa (%)» → `Nóminas!C2` | **0,33** |
| `astro-site/public/dl/guia-food-cost-ingenieria-menu/cuadro-de-mando-prime-cost.xlsx` | `Parámetros!B20`, que es la celda que lee `Mensual!L` (`=$J5*(1+Parámetros!$B$20)`) | **0,33** |
| Ídem | `Instrucciones!A9`, literal: «un salario de 15.400 € cuesta 20.482 € **con un 33 % de cotización**. Contar sólo los brutos…» | **33 %** |

La herramienta 1 declara reutilizar **esa misma fórmula** «cambiando el periodo». Con el 23,60 % sembrado, el mismo restaurante da dos prime cost distintos según qué fichero del mismo catálogo abra.

**Cuánto se equivoca, con números:** si al 33 % el coste de personal con SS es el 33 % de la venta, los brutos son el 24,8 % de la venta; bajar la cotización al 23,60 % resta `0,094 × 24,8 %` = **2,3 puntos de venta**. Un local con un prime cost real del **67 %** leería **64,7 %** y el semáforo diría **«En objetivo»** contra el umbral de 65 %. Es el falso negativo que la decisión D5 de la familia se escribió para evitar, servido esta vez por la casilla de cotización en vez de por el umbral. Y no es una cita que el lector pueda desmentir sin consecuencias: **es una fórmula que va a aplicar a su nómina.**

**Fix:** desglosar la casilla en las cinco cotizaciones reales (contingencias comunes, desempleo **según tipo de contrato**, AT/EP, FOGASA + FP, MEI), cada una en celda editable con su nota y su fuente, y **dejar el total calculado** —que es exactamente el tipo de criterio que el manual dice vender— sembrado en **32,15 %** para indefinido. Como mínimo, sembrar **33 %** por coherencia con los dos productos vivos. Y **`MM-17` no puede entrar en el guion rotulado «SS a cargo de la empresa»**: hay que corregir el id o crear uno nuevo con el total. El capítulo 04 debe explicar la diferencia entre las dos cifras, porque confundirlas es uno de los errores más caros del sector.

---

### A2 · ALTA — El permiso parental: el research se quedó a medio camino, y tal como está haría que un manager denegara mal una solicitud

> **Afirmación literal** (§1, concepto 13, y §11.2): «El **permiso parental de 8 semanas NO es retribuido**: el art. 45.1.o) ET lo tipifica como **suspensión** y el 45.2 «exonera de las obligaciones recíprocas de trabajar y remunerar». **Tampoco hay prestación de la Seguridad Social que lo cubra**»

Lo afirmado es **cierto** — verificado literalmente en el art. 45.1.o), el 45.2 y el 48 bis del ET, que sigue en su única redacción de 2023. El problema es lo que falta, y es lo que un manager necesita justo el día que le llega la solicitud.

El **RDL 9/2025, de 29 de julio** (en vigor **31-07-2025**) reformó el art. 48.4 ET: el permiso por nacimiento y cuidado de menor pasa a **19 semanas** (32 en monoparentalidad) y su reparto incluye ahora:

> «c) **Dos semanas, cuatro en el caso de monoparentalidad, para el cuidado del menor**, que podrán distribuirse a voluntad de la persona trabajadora… **hasta que el hijo o la hija cumpla los ocho años**. Este derecho es individual de la persona trabajadora sin que pueda transferirse su ejercicio.»

Y el art. 177 LGSS declara situación protegida los descansos «de acuerdo con lo previsto en los **apartados 4**, 5 y 6 del artículo 48» → **esas dos semanas SÍ están retribuidas**, con cargo al subsidio por nacimiento y cuidado de menor.

Es decir: hay **dos figuras que se solapan casi punto por punto** —las dos hasta los 8 años, las dos individuales e intransferibles, las dos «para cuidado del menor»— y **una se paga y la otra no**. Un capítulo 12 escrito sobre el research actual dice sólo «el permiso parental no se paga». Un manager que lea eso y reciba una petición de las dos semanas del art. 48.4.c) la denegará o la descontará mal. Y el research lo pone además en la **lista negra** (§11.2: «"El permiso parental de 8 semanas es retribuido" — **es una suspensión** del contrato»), con lo que el gate de coherencia **impediría activamente** escribir la parte correcta.

Duele especialmente porque es el capítulo 12, cuyo argumento es que los blogs se equivocan aquí. El manual se equivocaría **por el otro lado**, que es peor: negar un derecho retribuido.

**Fix:** el capítulo 12 y MM-26 tienen que distinguir las dos figuras en una tabla de dos columnas (art. 48 bis, 8 semanas, **no retribuidas** · art. 48.4.c), 2 semanas —4 en monoparentalidad—, **retribuidas por la Seguridad Social**), y actualizar el permiso de nacimiento a **19 semanas**, no 16. La entrada de la lista negra hay que reescribirla: lo prohibido es decir que **las ocho** semanas son retribuidas, no decir que hay semanas retribuidas.

---

### A3 · ALTA — El ALEH VI no resuelve «gerente vs encargado vs director vs jefe de sala vs administrador»: resuelve dos de los cinco, y el «gerente» que sí trae es de restauración moderna

> **Afirmación literal** (§1, concepto 1): «**El ALEH VI lo resuelve**: 6 áreas funcionales y 3 grupos profesionales; «gerente de centro» y «jefe/a de restaurante o sala» están en el grupo 1.º del área 3.ª (art. 16)»
> Y §8, cap. 01: «Gerente / encargado / director / jefe de sala / administrador **con el organigrama real del ALEH VI**»
> Y §10.2, FAQ 2: «¿Cuáles son los rangos en un restaurante? — **se responde con el organigrama del ALEH VI, que nadie usa**»

Leí el art. 15 del ALEH VI en el texto del BOE ([BOE-A-2023-6344](https://www.boe.es/buscar/act.php?id=BOE-A-2023-6344), consultado 2026-09-04). La lista literal del **área funcional tercera** es:

> «Restaurante y bar: Jefe/a restaurante o sala. 2.º Jefe/a restaurante o sala. Jefe/a sector. Camarero/a. Barman/Barwoman. Sumiller/a. Escanciador/a. Ayudante/a camarero. Repartidor/a de comidas y bebidas. **Restauración moderna: Gerente de centro.** Supervisor/a restauración moderna. Preparador/a restauración moderna. Asistente/a restauración moderna. Colectividades: … Catering: …»

De donde:

- **«Encargado» NO existe en el área tercera.** El ALEH sólo tiene «Encargado/a economato» (área 2.ª) y «Gobernante/a o Encargado/a general» (área 4.ª, pisos y limpieza). El puesto que en España se llama «encargado de restaurante» —40 búsquedas/mes, el segundo término más buscado del research y la primera pregunta de la FAQ— **no está en el convenio**.
- **«Director» y «Administrador» no aparecen en ninguna área funcional.** «Administrador de restaurante» es justamente el término dominante en Colombia (140/mes), Chile (260) y Perú (170), y es la FAQ nº 4.
- **«Gerente de centro» sí existe**, pero dentro del bloque **«Restauración moderna»** —comida rápida y cadenas—, no del bloque «Restaurante y bar». Equipararlo con el manager de un restaurante independiente de servicio en mesa, que es el público declarado, es forzar la fuente.

El daño no es de matiz: el capítulo 01 fija la autoridad del producto y la FAQ 2 promete «el organigrama del ALEH VI, **que nadie usa**». Nadie lo usa, entre otras cosas, porque **no responde la pregunta**.

**Fix:** reescribir el concepto 1 y el capítulo 01 con lo que el ALEH **sí** hace (clasificar en 6 áreas y 3 grupos; «jefe/a de restaurante o sala» en el grupo 1.º del área 3.ª; «gerente de centro» en el bloque de restauración moderna; y que **el grupo profesional que consta en contrato y nómina es lo que manda**, art. 11.2 ALEH) y **lo que no** (no tipifica «encargado de restaurante», ni «director», ni «administrador»: son denominaciones de uso). Esa distinción es *más* vendible que la falsa: explica por qué en el sector nadie se aclara. Y ojo con la trampa de fuente: **la modificación de hoy sólo publica las filas que cambian**, así que el organigrama completo hay que componerlo con `BOE-A-2023-6344` **+** `BOE-A-2026-18630` — un convenio no tiene texto consolidado en el BOE.

---

### A4 · MEDIA — La fecha del *doggy bag* es falsa, y el research usa la fecha correcta de la misma norma dos filas más abajo

> **Afirmación literal** (§2.1, V5): «el «doggy bag» **no nació aquí**: ya obligaba desde el **15-12-2022** por el art. 18.5 del RD 1021/2022»
> Y §11.2: «"El doggy bag es obligatorio desde la Ley 1/2025" — **desde el 15-12-2022** (RD 1021/2022, art. 18.5)»

La ficha oficial del BOE del RD 1021/2022 dice: «Fecha de publicación: **21/12/2022** — Fecha de entrada en vigor: **22/12/2022**». **No hay ningún 15 de diciembre.** Y el propio documento usa la fecha correcta para **esa misma norma** en la fila V8 de la tabla de al lado: «RD 3484/2000 — DEROGADO con efectos de **22-12-2022** por el RD 1021/2022».

Es un error de dos dígitos, sí. Pero está en **uno de los 12 «errores comprobables» que son el argumento de venta nº 3** («un manual que dice "el RD 3484/2000 está derogado desde 2022 y aquí tienes la ficha del BOE" se separa solo de los que lo siguen citando»). Equivocar la fecha justo en la pieza que se usa para demostrar que uno es más riguroso que la competencia es el peor sitio posible para tenerla mal.

Y falta lo que más le importa al lector: la obligación **excluye el bufé libre** («salvo en los formatos de servicio de bufé libre o similares donde la disponibilidad de comida no está limitada») y **obliga a informar de la posibilidad de forma clara y visible en el propio establecimiento** — una obligación de cartelería sancionable que no aparece en la síntesis.

**Fix:** 22-12-2022 en los dos sitios, más la excepción del bufé y la obligación de informar.

---

### A5 · MEDIA — La exclusión de las facturas simplificadas NO es absoluta, y la excepción es justamente la que emite un restaurante

> **Afirmación literal** (§2.1, V4): «Su art. 4 **excluye expresamente las facturas simplificadas** → el tique del restaurante queda fuera»
> Y §11.2: «"Habrá que emitir factura electrónica de cada mesa" — **el art. 4 del RD 238/2026 excluye las facturas simplificadas**»

El art. 4.1 del RD 238/2026 dice, literal: «Se exceptúan… las operaciones que se documenten a través de facturas simplificadas… **a menos que se trate de facturas simplificadas cualificadas a las que se refiere el artículo 7.2** de ese mismo Reglamento».

La **factura simplificada cualificada** del art. 7.2 del RD 1619/2012 es la que lleva NIF y domicilio del destinatario y la cuota repercutida por separado — es decir, **exactamente el tique que un restaurante emite cuando un cliente de empresa pide «pónmelo con mis datos» para deducírselo**. Esas sí entran en la factura electrónica obligatoria cuando llegue el plazo. Y son, además, las que más se emiten en el segmento de comidas de trabajo, que es un negocio central para el público del manual.

Decirlo sin el matiz da al lector la falsa sensación de que el RD 238/2026 no le afecta en absoluto. Es el mismo tipo de simplificación que el producto denuncia en los demás.

**Fix:** en el capítulo 06, la regla es de tres casillas, no de dos: tique normal → fuera; **tique con los datos fiscales del cliente (simplificada cualificada) → dentro**; factura completa B2B → dentro. Con la remisión al art. 7.2 del RD 1619/2012 para que el lector sepa cuál es cuál.

---

### A6 · MEDIA — La exención de los 1.300 m² es mucho más estrecha de lo que la síntesis sugiere

> **Afirmación literal** (§2.1, V5): «Y del plan **quedan exentos los establecimientos de hasta 1.300 m² y las microempresas**»
> Y §11.2: «"Todo restaurante necesita plan de prevención del desperdicio" — **exentos los de hasta 1.300 m² y las microempresas**»

El art. 6.4.c) de la Ley 1/2025 exime sólo de «**las obligaciones del presente apartado cuatro**» — el plan de prevención y los convenios de donación. **Siguen obligando a todo restaurante que no sea microempresa, sea cual sea su superficie**: el art. 6.1 (aplicar la jerarquía de prioridades del art. 5), el 6.2 (medidas del art. 19 de la Ley 7/2022), el 6.3 (nulidad de las cláusulas que impidan donar) y el 6.5 (no dejar alimentos no aptos). Sólo las **microempresas** quedan fuera del artículo entero (art. 6.6).

Como prácticamente ningún restaurante llega a 1.300 m², la redacción actual lleva a concluir que la Ley 1/2025 no le aplica en absoluto — y es falso. Además, es un flanco de credibilidad: el research vende como diferenciador saber distinguir lo que obliga de lo que no, y aquí se pasa de largo.

**Fix:** en el capítulo 19 (o el 20), «de lo que estás exento» y «de lo que no» en dos columnas, con la frase clave: **la exención de superficie sólo alcanza al plan de prevención y a los convenios de donación; el resto del art. 6 obliga a cualquier restaurante que no sea microempresa**.

---

### A7 · MEDIA — Las propinas son uno de los 18 conceptos obligatorios, no están en ningún capítulo, y los dos números de consulta que sostienen el argumento no se pudieron verificar

Dos problemas encadenados en el mismo punto.

**Primero, no hay capítulo.** El concepto 14 del §1 es uno de los cinco donde «lo gratuito afirma algo falso», es el error nº 12 del argumento de venta, está en la lista negra y tiene dos entradas de datos propias, **MM-24 y MM-25**. Y sin embargo: **ningún capítulo del índice del §8 lo cubre** —el 06 es caja, tique, efectivo y Verifactu— y **MM-24 y MM-25 no están asignados a ninguno**. Verificado contra el JSON: son, junto con MM-48, los únicos tres ids `MM-*` de los 52 que el §8 no cita. Los datos de TheFork Lab sobre propinas del §5.6 tampoco tienen destino. Un guion escrito sobre este índice no producirá el contenido, y **no hay gate que compruebe que los 18 conceptos del §1 tienen capítulo**.

**Segundo, la fuente del argumento no está acreditada.** El art. 76.1.3.º del RIRPF **sí** está confirmado al pie de la letra («Cuando satisfagan a su personal cantidades desembolsadas por terceros en concepto de **propina**…»). Pero **ni la V3095-17 ni la V2236-13 se pudieron verificar**: el buscador oficial de la DGT (`petete.tributos.hacienda.gob.es`) devuelve «la consulta realizada no devuelve resultados» **incluso para consultas de control y para búsqueda libre**, así que no confirma ni refuta ninguna de las dos. Y el research construye sobre esa distinción un argumento de autoridad de primer orden: «la consulta que citan casi todos los blogs es la equivocada». Es la afirmación del research **con peor relación entre rotundidad y respaldo**.

**Fix:** (a) bloque de propinas al **capítulo 06** con sus dos epígrafes (fiscalidad y retención según quién reparte; que la **cotización no tiene norma expresa** y depende del convenio), asignándole MM-24 y MM-25; (b) **verificar a mano las dos consultas** antes de imprimir sus números, o reformular el argumento apoyándose sólo en el RIRPF, que sí está acreditado; (c) añadir al research una **tabla de trazabilidad concepto → capítulo** para los 18: es un chequeo de cinco minutos que cierra la clase entera de fallo.

---

### A8 · MEDIA — La lista negra veta DOS datos que el INE sí publica, y la fila de supervivencia está mal etiquetada

> **Afirmación literal** (§5.7): «Supervivencia empresarial (todos los sectores) — **76,9 %** a 1 año · **63,5 %** a 3 · **41,9 %** a 5 — INE, Demografía Armonizada de Empresas — **Alta**»
> Y §11.1: «**No existe fuente oficial de mortalidad de restaurantes en España.**» · «**Absentismo específico de hostelería** — Randstad sólo desglosa hasta «sector servicios» (7,1 %). **No atribuir esa cifra a la hostelería**»

Tres cosas, y las dos últimas son oportunidades perdidas por prudencia mal dirigida:

1. **El 63,5 % es la tasa a DOS años, no a tres.** La serie nacional es 76,9 % (1 año) → 63,5 % (**2** años) → 41,9 % (5 años). Está mal etiquetada en una fila marcada «Alta».
2. **Sí hay serie de supervivencia de hostelería.** En la Demografía Armonizada de Empresas por sección de actividad (base: 34.933 empresas), hostelería da **75,6 % a 1 año · 53,5 % a 3 · 38,8 % a 5**. La premisa de la lista negra es cierta para *restaurantes* como subclase, pero **falsa para hostelería como sección** — y es un dato mejor: más específico, más bajo que la media nacional y con fuente primaria. (Aviso de honestidad que sí hay que dar: esa cohorte está contaminada por la pandemia.)
3. **Sí hay absentismo de hostelería.** No lo publica Randstad, que se queda en «sector servicios», pero **lo publica el INE en la ETCL, tabla 6043** (horas no trabajadas por IT, sección I). La entrada de la lista negra dice que el dato no existe; existe, sólo que en otra fuente. Y de paso: el 7,1 % / 5,5 % que se cita es del **4T 2025**, cuando ya hay **1T 2026 (7,2 % y 5,6 %)**.

Es el reverso exacto del problema de A10: allí se cita lo que no se puede, aquí se renuncia a lo que sí se puede. Las dos cosas nacen de no volver a la fuente primaria cuando la secundaria no da.

**Fix:** corregir la etiqueta del 63,5 % a «2 años»; usar la serie de **hostelería** (75,6 / 53,5 / 38,8) con el aviso de la cohorte; y reescribir las dos entradas de la lista negra — lo que no existe es la tasa de *restaurantes* y el absentismo *de Randstad*, no los datos.

---

### A9 · MEDIA — Los reconocimientos médicos: faltan las tres excepciones del art. 22.1, y la segunda es justamente la de los manipuladores

> **Afirmación literal** (§1, concepto 12): «Art. 22.1 Ley 31/1995: «**sólo podrá llevarse a cabo cuando el trabajador preste su consentimiento**». La empresa **ofrece**; el trabajador puede rehusar»

Correcto, y verificado literal. Pero el mismo art. 22.1 continúa: «De este carácter voluntario **sólo se exceptuarán, previo informe de los representantes de los trabajadores**, los supuestos en los que la realización de los reconocimientos sea **imprescindible para evaluar los efectos de las condiciones de trabajo sobre la salud**… o para **verificar si el estado de salud del trabajador puede constituir un peligro para el mismo, para los demás trabajadores o para otras personas relacionadas con la empresa**… o cuando así esté establecido en **una disposición legal**».

La segunda excepción —«peligro… para otras personas relacionadas con la empresa»— es exactamente la que se invoca en hostelería para los manipuladores de alimentos. Presentar el reconocimiento como puramente voluntario, sin decir que la excepción existe y que **requiere informe previo de la representación de los trabajadores**, es la clase de simplificación que produce un conflicto laboral en un local con delegados. L3 lo marca como «el error más frecuente» del bloque de PRL, y la corrección se queda a medias.

**Fix:** al capítulo 15 y a MM-21, la regla completa: voluntario **por defecto**, con tres excepciones tasadas, y en las tres **informe previo de la RLT**. Y el matiz operativo que hace falta: aun en el caso excepcional, la empresa sigue recibiendo sólo las **conclusiones de aptitud** (art. 22.4).

---

### A10 · MEDIA — El 63,8 % va a la lista negra por su fuente, pero el resto del MISMO informe se queda en la tabla; y hay un dato del §5.4 que ya se ha dado la vuelta

> **Afirmación literal** (§11.1): «**Rotación en hostelería del 63,8 %** — … aparece con **dos padres distintos**: Synergie (L4-A3) y Randstad (L4-H1). **No se cita**»
> Y **§5.3**, dos filas más abajo: «Salario medio en hostelería vs media nacional — **1.512 € vs 2.345 €/mes (−35 %)** — **Synergie España 2026, vía InfoHoreca** — Media»

Las dos cifras salen del **mismo informe, el mismo día y la misma URL** (L4-A3 y L4-A4: `infohoreca.com/noticias/20260626/…`, 26-06-2026). Si ese informe no es citable porque no está publicado y su atribución baila, no lo es para la rotación **ni para el salario**. La verificación independiente cerró además la cadena: Synergie → FOS → Linkers, y **Linkers nunca publicó el informe**. La decisión D4 (lista negra) es la correcta; hay que aplicarla **al informe entero**, no a la fila que incomoda.

Y hay un segundo problema en el mismo bloque, de caducidad: la **temporalidad del 12,6 % frente al 15,5 % nacional** (§5.4) está confirmada para el 1T 2026, pero **en el 2T 2026 la ventaja se invierte** y la hostelería adelanta a la media nacional. Un manual publicado en otoño de 2026 que diga «la hostelería tiene menos temporalidad que la media» estará diciendo algo que ya dejó de ser cierto cuando se imprima.

**Fix:** sacar el 1.512 €/2.345 € de la tabla y sustituirlo por el dato **primario del INE que el research ya tiene**: sueldos y salarios por trabajador/año, **17.190,75 € en hostelería frente a 28.410,78 € nacional** (EACL 2025). Dice lo mismo, con fuente primaria, sin intermediarios y sin cadena circular. Y la temporalidad: o se cita con el trimestre pegado a la cifra («12,6 % en el 1T 2026»), o se sustituye por el **87 % de indefinidos sobre asalariados**, que es la misma idea y aguanta mejor el trimestre siguiente.

---

### A11 · MEDIA — Once citas del §5 no dicen exactamente lo que se les atribuye — incluida la que justifica la herramienta estrella

Fui a la fuente primaria de las 22 cifras del §5. **Seis salen confirmadas al pie de la letra** (ver «Lo que SÍ aguanta»). Once dicen algo distinto de lo que se les hace decir, en grados que van de la errata de fecha a un cambio de significado:

| Cita del §5 | Lo que dice de verdad la fuente |
|---|---|
| **«Sólo el 39 % revisa su rentabilidad cada semana» (TheFork, 615 profesionales)** | Las tres cifras son correctas, pero **la ficha del estudio acota la muestra a restaurantes con ticket medio superior a 25 € y a perfiles directivos**: deja fuera bares, cafeterías y menú del día. Y la fecha es **17**-03-2026, no 18 |
| **«Prime cost 60-65 % — Toast / restaurantowner»** | El 60-65 % es de **Jim Laube (RestaurantOwner, 2017)**, no de Toast. **Toast fija el objetivo en «60 % or lower»** (30 % COGS + 30 % personal) y la excelencia en 55 %; el ~65 % es su *media* del full-service, no su objetivo |
| **CaixaBankLab × elBullifoundation, «metodología Sapiens»** | La palabra **«Sapiens» no aparece** en el artículo. Dice «servicio **integrado / parcial**», **nunca «barra» ni «autoservicio»** — la traducción que sostiene el umbral del ≤55 % es glosa del research, no de la fuente. **Sí tiene fecha**, en los metadatos: publicado 2017, revisado 2022 (la instrucción «citar sin fecha» se puede mejorar). Y su propia aritmética no cierra: 30 + 32,5 + 5 + 17 deja **15,5 %**, no el «EBITDA sano del 10-13 %» |
| **«Ticket medio 21 € — CaixaBank Research, 1S 2025»** | Las cuatro cifras son exactas y la fuente **sí blinda el «por transacción»**, pero son datos de **2024** (media de enero a septiembre), de un artículo del **16-01-2025**. No es «1S 2025». Excluyen efectivo y reflejan la cuota de una sola entidad |
| **«38 h semanales en administración, supervisión y formación» (Square + AmEx)** | Son 38 h de gestión **del personal** (14 administrativas + 24 de supervisión y formación) |
| **«77 % considera la gestión de personal *muy estresante*»** | Dice «**son de los más estresantes**» |
| **«La gestión de datos es su reto principal: 37 %»** | Dice «**uno de** sus retos», y la formulación es «generación y gestión de **insights** del negocio» |
| **«+19 puntos porcentuales (+49 %)» (Anderson & Magruder)** | La referencia y la cita son exactas, pero el 19 pp es **sólo la franja de las 19:00 h** (18 h = 11 pp, 20 h = 15 pp) y el propio paper dice «**only the 7:00 pm result is significant**». Mide disponibilidad para mesa de cuatro, 36 h antes, San Francisco 2010 |
| **«SMS: no-show del 1,92 % al 1,52 %» (CoverManager)** | Es **un solo día** (Día del Padre de 2025) y **sólo el subgrupo sin protección**; la propia nota avisa de que no es trasladable al resto del año. **No es comparable** con el 3,3 % de TheFork, que es media anual de todas sus reservas |
| **«SMI 2026: 17.094 €/año» (RD 126/2026)** | Los 40,70 €/día y los 1.221 €/mes están en el art. 1. **Los 17.094 € no figuran en el RD**: son 1.221 × 14 |
| **«Beneficios sociales 211,42 €» (INE, EACL)** | Los importes son exactos pero **no existe una variable «beneficios sociales» en la EACL**: son la suma de cotizaciones voluntarias + prestaciones sociales directas + gastos de carácter social. Va marcado «Alta» y es un derivado propio. (Igual, «1.748.137 ocupados» es **media anual**, no plantilla a fecha fija) |

La primera fila es la que más importa y merece decirse aparte. **El 39 % de TheFork es el dato que justifica el cuadro de mando semanal**, que es la herramienta nº 1 y el capítulo 03 entero («El cuadro de mando semanal: por qué la semana y no el mes»). Que su muestra excluya a los bares, a las cafeterías y a los restaurantes de menú del día **no invalida el dato**, pero sí obliga a citarlo con su ámbito — porque el público que el research define en §6 (independientes de 8-15 personas, con el 73 % del sector en microempresas) está en buena parte **fuera de esa muestra**. Escribir «sólo el 39 % de los restaurantes revisa sus números cada semana» sin decirlo es atribuir a todo el sector una encuesta de restaurantes de ticket alto.

La segunda importa por otra razón: el §11 pone en la lista negra «prime cost 60-65 % presentado como dato español» y lo manda citar «como convención de EE. UU. (**Toast** / restaurantowner)». **Toast dice otra cosa** — su objetivo publicado es 60 % o menos—, así que el contraste que se quiere hacer con el umbral español derivado del ≤65 % queda mal montado en su propia referencia.

**Fix:** corregir las once en la SPEC antes de que pasen al guion, y añadir a las tres primeras su ámbito en la propia frase («entre restaurantes de ticket medio superior a 25 €…», «según RestaurantOwner…», «datos de 2024 sobre pagos con tarjeta…»). Ninguna obliga a renunciar al dato; todas obligan a acotarlo.

---

### A12 · MEDIA — La lista negra está incompleta, y la cifra que encabeza la lista **sigue publicada** en el sitio

El §11 es bueno, pero se ha construido mirando las cifras que dieron problemas, no barriendo las tablas. Repasando §5 y las lentes, **falta**:

| Qué falta | Por qué debe entrar |
|---|---|
| **«Coste laboral/año de Servicios de comidas y bebidas: 20.658 €»** (§5.2) | Fiabilidad **Media** por confesión propia: el desglose por división **no está en la nota de prensa del INE**, viene de `brainsre` citándola. Está en la misma tabla que cinco cifras «Alta» del INE y se leerá como si fuera INE primario |
| **El bloque Ivie/Cajamar entero** (§5.7): 46.932 €/empleado · **+44,3 %** de productividad sobre la UE-27 · coste laboral **−30 %** · **1 bar por cada 281 habitantes** | La nota original **no abre** (error TLS); son réplicas del emisor. Son las cifras más «citables» del research y las más fáciles de escribir como si fueran oficiales |
| **«Facturación +3,1 % y rentabilidad −0,9 %»** (§5.7) | El research lo llama «**el dato que justifica el manual entero**», y su fuente es prensa que reproduce un anuario **de pago (1.800 €/año)** que nadie ha leído. Un argumento que carga todo el producto no puede descansar en fiabilidad Media sin decirlo en la propia frase |
| **«Prime cost 60-70 %»** de restaurantowner (L4-J3) | La lista negra veta el 60-65 % «como dato español», pero en L4 circula un **tercer número, 60-70 %**, de la misma casa. Un redactor que lea L4 lo copiará |
| **«Beneficios sociales por trabajador/año: 211,42 €»** (§5.2) | **No es una variable de la EACL**: es la suma de tres conceptos distintos. Marcado «Alta» en la tabla, cuando es un derivado propio |
| **Tarifas SGAE 2026 en €/mes** (20,67 / 22,53 / 28,67…) | Son correctas hoy, pero **caducan cada año**. En prosa envejecen mal: deben ir en celda del calendario legal con su fecha, nunca impresas en el capítulo 19 |
| **«Ley 10/2025 de servicios de atención a la clientela»** | L3 §4.11 verifica que un restaurante independiente **queda FUERA** (umbral de 250 trabajadores / 50 M€ / 43 M€). No está en §11.2 y es el tipo de norma nueva que un redactor aplica de más: los plazos de 15 y 5 días hábiles no son suyos |
| **El propio 23,60 %** (A1) | «No usar como coste de SS a cargo de la empresa». No es un dato mal copiado: es una **fórmula errónea** |
| **El EBITDA sano del 10-13 %** presentado como resultado de la estructura de costes | La suma de la propia fuente (30 + 32,5 + 5 + 17) deja **15,5 %**. O se cita como afirmación de la fuente, o se deriva — las dos cosas a la vez, no |
| **«El 8,6 % del empleo nacional»** (§5.7, patronal) | Circula en prensa atribuido también a Randstad; **el correcto es 7,9 %**, que el propio §5.4 trae tres filas más arriba. Dos cifras del mismo concepto en el mismo apartado |
| **«Temporalidad nacional 15,5 %»** si se atribuye al INE | De la EPA sale **14,77 %**. Sólo es citable «según Randstad» |
| **«Coste de reemplazo 2.800-5.000 €»** | Ya está vetado, pero conviene añadir el porqué exacto: **no aparece ni en el informe de Synergie**, sólo en prensa. Y hay una alternativa trazable en la misma página para el eje de rotación: **24,1 % (Nailted)** |

Y una advertencia que vale por todas: **la lista negra sólo apunta al producto nuevo, y el problema ya está publicado**. La entrada nº 1 —«El 60 % de los restaurantes cierra en los primeros años», correctamente vetada— está **viva hoy** en tres sitios del repo:

- `astro-site/src/data/productos/guias/guia-restaurante-casual.ts:21` (badge del hero de una landing de **65 €**)
- `src/components/guia-restaurante-casual/HeroSection.tsx:71` (el gemelo de la SPA)
- `src/data/pseo-cities-content.es.ts:60` (la plantilla que alimenta las páginas pSEO de ciudades)

Y `astro-site/src/data/productos/kits/kit-plan-financiero.ts:15` documenta que **ya se quitó de un producto** («OJO: el badge YA NO cita "El 60% de los restaurantes…"»), lo que confirma que la casa sabe que no se sostiene y que la limpieza se quedó a medias.

**Fix:** ampliar el §11 con las once filas de arriba **y** abrir una tarea separada —no bloqueante de este producto, pero sí de la próxima sesión— para retirar el 60 % de las tres ubicaciones vivas. Vetar una cifra en el producto nuevo mientras se vende en el de al lado es la peor de las dos posiciones.

---

### A13 · MEDIA — El art. 41.3 del ALEH trae una excepción y una remisión que se omiten, y no consta desde cuándo se aplica

Descargué y extraje el PDF de [BOE-A-2026-18630](https://www.boe.es/boe/dias/2026/09/04/pdfs/BOE-A-2026-18630.pdf) (16 páginas). **Todo lo sustancial que dice la síntesis es correcto** (ver «Lo que SÍ aguanta»). Faltan tres cosas, y la primera importa:

1. **La excepción.** El texto literal es: «…para darle la oportunidad de contestar a las imputaciones; **a menos que no pueda pedirse razonablemente a la empresa que le conceda esta posibilidad**». Un manual que enuncie «hay que dar 2 días **siempre**» está incompleto justo donde el manager puede necesitar saber que hay salida.
2. **La remisión.** El artículo abre «…**sin perjuicio del cumplimiento del resto de obligaciones establecidas en el artículo 55.1 del Estatuto de los Trabajadores** cuando se refiere a los colectivos concretos regulados»: la audiencia previa **se suma** al expediente contradictorio de representantes y afiliados, no lo sustituye.
3. **Desde cuándo aplica.** No está en la síntesis ni en MM-13. Lo dice el propio acuerdo: «las partes… han acordado un nuevo periodo de vigencia, **desde el momento de la publicación del presente texto en el BOE hasta el 31 de diciembre del año 2030**». Es decir, **desde el 04-09-2026**. Es el dato que convierte la novedad en instrucción operativa —«si despides mañana, esto ya te aplica»— y no está escrito en ningún sitio.

**Fix:** las tres al capítulo 14 y a MM-13, con la cita literal de la excepción. Y actualizar el §13: ya no hace falta esperar al verificador legal para este documento, está verificado.

---

### A14 · MEDIA — «Actualizado al BOE del día del lanzamiento» caduca entre el research y la publicación, y hay un RD anunciado para este mismo mes

> **Afirmación literal** (§2.4.1): «**«Actualizado al BOE del día del lanzamiento», y es literal.**»
> Y **§2.5**: «**Registro horario digital** — Aprobación aplazada «a septiembre de 2026» → puede publicarse en semanas — **Alta e inminente**»

Las dos frases están en la misma sección y se contradicen en la práctica. El research es de hoy; el §12.3 dice que la fase B **no cabe en una semana**. Entre el research y la publicación pasarán semanas, y en esas semanas:

- el **RD del registro horario digital** está anunciado para **septiembre de 2026** — este mes. El capítulo 11 vende como diferenciador que «el fichaje digital todavía no obliga» y el §11.2 lo mete en la lista negra al revés. Si el RD sale antes que el producto, **el capítulo 11 nace equivocado y el gate de coherencia obliga a escribir lo contrario de lo que dirá el BOE**;
- el **convenio de hostelería de Madrid** está en ultraactividad desde el 31-12-2025: se puede firmar cualquier día, y con él caen las tablas del §5.3 y el ejemplo del capítulo 08.

Añado un dato de la verificación que **refuerza** el research y a la vez acota lo que puede decir: barrí los **247 sumarios del BOE del 1-ene al 4-sep-2026** por la API de datos abiertos. **No hay ningún RD de registro horario ni ninguna ley antitabaco.** El «hoy no te obliga» está sólidamente probado. Lo que **no** se pudo acreditar en fuente primaria son los **detalles de tramitación**: el dictamen del Consejo de Estado de 23-03-2026, el aplazamiento a septiembre y el Consejo de Ministros de 21-07-2026. Son precisamente las frases que caducan antes y las únicas que no tienen respaldo primario.

**Fix:** (a) un **re-chequeo obligatorio de las 7 normas en movimiento del §2.5 en las 48 h previas a publicar**, como gate de lanzamiento con su salida escrita —igual que `robots-gate.py` es obligatorio aunque «ya esté puesto»—; (b) bajar los detalles de tramitación a «según el Ministerio» o quitarlos: el mensaje útil no depende de ellos; (c) reescribir el claim como «**verificado contra el BOE el <fecha> — y cuando cambia, te llega la versión nueva**», que es verdad siempre y además vende el pago único.

---

### A15 · BAJA — Cuatro recuentos que no cuadran

- **«7 guías «Cómo Montar»» a 65 €** (§9.1) y «la franja de 65 € ya está establecida con **7 productos**» (§9.2 arg. 4): son **seis** (`guia-restaurante-casual`, `guia-panaderia-obrador`, `guia-restaurante-japones`, `guia-restaurante-mexicano`, `guia-restaurante-nikkei`, `guia-restaurante-peruano`), y **la propia tabla enumera los seis**. Es un número que sostiene un argumento de precio y se repite dos veces.
- **«el más bajo de las 19 secciones de actividad»** (§5.2): la EACL publica **18** secciones. El hecho —que hostelería es el mínimo— es correcto; el denominador, no.
- **«los 9 posts propios ya publicados (verificado: los 10 ficheros existen)»** (§0) y «los **10** posts de blog de L2 §5 existen en disco» (§13): son **nueve**. El «décimo» sale de que el patrón `30-hacks-…` casa con **dos** ficheros del blog y L2 sólo nombra uno.
- **«los 3 fixes de parametrización… están aplicados sin commitear»** (§0 nota 2, §12.2 nº 6, §13): están **commiteados** en `68eb353`, con el árbol de trabajo limpio. No cambia nada del plan, pero sí una consecuencia: los cambios ya están en `main` y **la prueba de no-regresión que pide el riesgo 10 del §12.1 (regenerar la Guía Food Cost) sigue sin hacerse** sobre código que ya está en producción.

---

## B. NEGOCIO

### B1 · ALTA — 65 € contradice una decisión firmada ayer, para un paquete idéntico en todo lo contable

> **Afirmación literal** (§9.2, arg. 1): «**Amplitud, no capricho.** La Guía Food Cost (55 €) es **un producto vertical**… Este manual cubre **5 ejes + cumplimiento legal transversal**, 20 capítulos, **8 libros de Excel** y un bonus de 12 casos»

`guia-food-cost-SPEC.md:34`, **decisión D1, firmada el 2026-09-03**, dice literalmente:

> «**Precio 55 €.** Escalera real: … guías «Cómo Montar» 65 € (**20 caps + 8-9 xlsx + 6 checklists + 2 docx**) · gastronómico 85 € · mega pack 89 €. **Este paquete (guía 20 caps + 8 xlsx densos + bonus) queda por debajo de las guías de 65 €**…»

El paquete que la SPEC describe —«20 caps + 8 xlsx densos + bonus»— **es exactamente, término a término, el que el manual propone**. Ayer eso valía 55 € *precisamente porque* la franja de 65 € trae dos bloques de entregables más. Hoy se propone 65 € para el mismo recuento sin refutar D1 ni mencionarla.

Y no es un tecnicismo de SPEC: es lo que ve el comprador. Los `checkItems` reales de las landings vivas:

| Producto | Precio | Lo que enumera la landing |
|---|---|---|
| `guia-restaurante-casual` | **65 €** | 20 capítulos, 60+ páginas · **8 plantillas Excel** · **6 checklists** · **Business Plan modelo** · **Manual de operaciones** |
| `guia-panaderia-obrador` | **65 €** | 20 capítulos, 70+ páginas · **9 plantillas Excel** · **6 checklists** · **Business Plan modelo** · **Manual del obrador** |
| `guia-food-cost-ingenieria-menu` | **55 €** | 20 capítulos, 95 páginas · **8 herramientas Excel** · (+ bonus) |
| **Manual del Manager (propuesto)** | **65 €** | 20 capítulos, ~95 páginas · **8 libros Excel** · (+ bonus de 12 casos) |

En el hub, a 65 €, el manual queda **con dos bloques de entregables menos que sus seis vecinos de precio**, y con el mismo recuento exacto que el vecino de 55 €. La «amplitud temática» no es un entregable: no se puede contar en una tarjeta y no la puede comprobar quien está decidiendo.

**Fix — y es una decisión, no trabajo:** o **55 €**, que es el precio que la casa ya decidió ayer para este recuento; o 65 € **añadiendo lo que la franja de 65 € tiene** (6 checklists y un segundo documento). Ojo: la opción B choca de frente con la decisión D2 del orquestador, que descartó el kit de checklists por duplicar `kit-tareas/03`. Es decir: **con el bonus elegido, 65 € no tiene cómo justificarse por recuento.**

---

### B2 · ALTA — El ancla externa que sostiene el precio está mal contada: 65 € es MÁS que un mes del plan Starter

> **Afirmación literal** (§9.2, arg. 2): «**65 € es el 5,7 % de un año de Last.app Growth** (95 €/mes +IVA = 1.140 €/año, precio publicado en su web, más 500 € de instalación única) **y menos de lo que cuesta un mes de cualquiera de sus tres planes**»

Verificado hoy en `last.app/precios`, texto literal: **Starter «50€/mes+IVA por local»**, Growth «95€/mes+IVA», Unlimited «175€/mes+IVA», instalación «500€ + IVA» en los tres.

- Un mes de **Starter** con IVA = **60,50 €**. El manual son 65 €. **65 > 60,50**: la afirmación es falsa para uno de los tres planes, y precisamente para el más comparable — el plan de entrada de un local independiente, que es el público del manual.
- Sin IVA tampoco se salva: 65 € IVA incluido son **53,72 €** de base, frente a los 50 € de Starter.
- Y el «5,7 %» compara un precio **con IVA** contra un anual **sin IVA**. Con IVA, 1.140 € son 1.379,40 €, y la cifra correcta es **4,7 %**.

El ancla sigue siendo buena —nadie discute que un pago único de 65 € es otra cosa que 1.379 €/año por local—, pero **está escrita con una frase comprobablemente falsa** en el mismo párrafo que fija el precio. Es el flanco que un comprador con la web de Last.app abierta cierra en diez segundos.

**Fix:** «65 € es **menos de un 5 %** de lo que cuesta un año del plan Growth de Last.app (1.140 € + IVA por local, más 500 € + IVA de instalación), y **es tuyo para siempre**». Cifra correcta, comparable homogénea, y no se apoya en el plan donde el argumento se rompe.

---

### B3 · ALTA — Tres de los ocho libros repiten material que el comprador objetivo ya tiene, y uno de ellos sería el tercer plan de 90 días del catálogo

> **Afirmación literal** (§3.3, herramienta 1): «Motor de origen: `guia-food-cost/cuadro-de-mando-prime-cost.xlsx!Mensual` (prime cost y semáforo, **cambiando el periodo**)»
> Y herramienta 5: «`guia-food-cost/plan-accion-90-dias.xlsx`, **letra por letra**»

El público prioritario del lanzamiento (§0, «Lista de compradores») incluye a los compradores de la **Guía Food Cost (55 €)**, que es además el cross-sell explícito del §3.2. Abrí con `openpyxl` los 17 libros implicados y los crucé con un censo de nombres de hoja sobre **los 432 xlsx publicados**. El solape real, medido:

| Libro propuesto | Solape | Evidencia |
|---|---|---|
| **1 · `cuadro-de-mando-semanal-manager`** | **~70 %** | `cuadro-de-mando-prime-cost.xlsx!Mensual` tiene **18 columnas** y **16 de las propuestas ya están, con la fórmula**: consumo (`$E5+$F5-$G5`), coste de personal con SS (`$J5*(1+Parámetros!$B$20)`), food cost %, labor cost %, **prime cost %** (`($H5+$L5)/$D5`), objetivo y semáforo. Y `kit-plan-financiero/06!Ratios` **ya publica** 11 ratios con benchmark, objetivo y semáforo, **incluidos ticket medio y coste por cubierto** — que es casi la hoja «KPI y definiciones» propuesta. **Nuevo de verdad:** las 52 filas ISO, cubiertos/hora de apertura, ventas/hora trabajada y la columna «error típico» |
| **5 · `plan-90-dias-operativo`** | **DUPLICADO ESTRUCTURAL** | Las cuatro hojas propuestas —Instrucciones · Decisiones · Calendario 90 Días · KPI de Seguimiento— son los **nombres exactos** de `guia-food-cost/plan-accion-90-dias.xlsx`, y las cabeceras coinciden casi al carácter (`Calendario 90 Días` y `KPI de Seguimiento`, **idénticas**). Y ese fichero **ya lleva su propio disclaimer**: `Instrucciones` f16 dice literal «ESTE PLAN NO ES EL PLAN DE 4 SEMANAS DEL BONO DEL KIT DE ESCANDALLOS…». Sería el **tercer** plan de 90 días del catálogo, con el **tercer** aviso |
| **7 · `reuniones-briefings-actas`** | **~40 %** | Hay **20 hojas «Briefing»** en el catálogo, y las dos que el research cita para descartarlas son más completas de lo que sugiere: `kit-gestion-personal/BONUS-01!Briefing` ocupa **A1:F72** e incluye arqueo con tolerancia de descuadre y temperaturas APPCC del cambio de turno. La hoja «Guion de Briefing» propuesta **es eso, por tercera vez**. Genuinamente nuevo: reuniones periódicas y actas (`acta` y `reunión` = **0 hojas en 432 libros**) |
| 4 · `seleccion-scorecard-entrevista` | ~35 % en mecánica | `kit-gestion-personal/06!Ficha Evaluación` es el mismo artefacto (10 competencias 1-5 con N/A, media condicional, nivel por umbral). Nuevo: candidato en vez de empleado, **pesos**, ranking y banco de preguntas |
| 6 · `calendario-cumplimiento-legal` | ~45 % en contenido | `kit-tareas/05!Trimestral y Anual` ya lista **15 obligaciones** con responsable y cadencia ≈ 11 de los ~14 puntos. Pero **sin ninguna columna de fecha** (`Nº, Tarea, Nº de parte, Responsable, Cadencia, ✓, Firma`). El mecanismo —última + periodicidad → próxima + semáforo, la columna «¿lo fija una norma estatal?» y la hoja `Estado Normativo`— **no existe en el catálogo** |
| **2 · `matriz-formacion-polivalencia`** | **~10 % — NUEVO REAL** | `polivalenc` = **0 hojas y 0 celdas** en los 432 libros |
| **3 · `quejas-reclamaciones-resenas`** | **NUEVO REAL** | `queja`, `reclamac`, `reseñ`, `review` = **0 hojas** en 432 libros. El «hueco declarado» se sostiene entero |
| **8 · `auditoria-interna-servicio`** | **~15 % — NUEVO REAL** | `pack-appcc/15!25 Puntos Inspección` es higiene y legalidad sanitaria; se comparte el patrón de puntuación y poco más |

Para el segmento al que primero se le va a vender: **un libro es re-compra estructural (el 5), otro repite el 70 % de un libro que ya tiene (el 1) y un tercero repite por tercera vez un formulario que existe 20 veces (la hoja de briefing del 7)**. La mitigación propuesta es una frase en Instrucciones. Una frase no es una mitigación: es un aviso de que se lo está vendiendo dos veces — y en el plan de 90 días, **la frase ya existe y ya iba dirigida al mismo problema**.

El research analiza la canibalización en un solo sentido —§12.1 riesgo 4, «los kits ejecutan, el manual decide», de barato a caro— y **no analiza ésta**, que va de caro a caro.

**Fix, a elegir antes de construir:**
- **El libro 5 deja de ser un libro:** son 20 filas y una lista de valores en la columna «área» del `plan-accion-90-dias.xlsx` que ya existe, o una hoja dentro de otro libro del manual.
- **El libro 1 no repite el prime cost:** se queda con lo que no existe (semana ISO, cubiertos/hora de apertura, ventas/hora trabajada, ticket medio y gasto por cubierto **separados**, la columna del error típico) y **remite** al cuadro de mando de la Guía Food Cost y al dashboard del Kit Plan Financiero.
- **El libro 7 pierde la hoja «Guion de Briefing»** y remite a las dos que existen.
- Quedan **7 libros densos y sin repeticiones**, que se defienden mejor en la landing que 8 con tres solapes — y encajan con el precio de B1.

---

### B4 · ALTA — Tres capítulos del eje «personas» no traen ninguna herramienta del manual: su única herramienta es un producto de 14 € que no va incluido

Leyendo la columna «Herramienta» del índice del §8:

| Capítulo | Herramienta declarada | ¿Va incluida? |
|---|---|---|
| **11 · Jornada, cuadrante y registro de jornada** | `(kit-gestion-personal/01-02)` | **No.** Kit de Gestión de Personal, 14 € aparte |
| **12 · Permisos, vacaciones y conciliación** | `(kit-gestion-personal/05)` | **No** |
| **14 · Evaluar, corregir y, si toca, despedir** | `(kit-gestion-personal/06)` | **No** |
| 05 · El día del manager | `(kit-tareas) + 7` | Parcial |
| 06 · La caja y el tique | `(kit-tareas/09) + 6` | Parcial |
| 10 · Selección y primeros 30 días | `4 (+ kit-gestion-personal/04)` | Parcial |
| 19 · Seguridad alimentaria y el local | `6, 8 (+ pack-appcc)` | Parcial |
| 01 · Qué es un manager | `—` | Ninguna |

Son **tres capítulos sin herramienta propia y siete de veinte que remiten a producto de pago aparte**. Y los tres sin herramienta están en el eje «personas», que es el que más capítulos tiene (8 de 20) y el dolor nº 1 del research.

Dos consecuencias que la síntesis no recoge:

1. **Alimenta la objeción que ella misma documenta.** La objeción 4 —«es caro para lo que es», confirmada con una reseña real— se responde peor cuando el lector descubre en el capítulo 11 que para aplicar lo que acaba de leer necesita comprar otra cosa. En un producto de 65 € comprado por un **empleado con sueldo de 24.000-36.000 €** (L4 §2), eso duele.
2. **Rompe la jerarquía que el propio producto vende.** La frase de la landing es «los kits te dicen qué hacer cada día; **el manual te dice por qué, con qué criterio y qué pasa si no lo haces**». En los capítulos 11, 12 y 14 el manual **no tiene con qué**: el criterio se queda sin herramienta donde aterrizar.

**Fix:** no hacen falta tres libros más. Basta con que el **calendario de cumplimiento legal (herramienta 6)** —que ya es el diferenciador— incorpore dos hojas que hoy no existen y que no duplican nada: un cuadro de **plazos y topes de jornada** (12 h, 9 h, 80 h/año, preaviso de 5 días, 4 años de conservación, 2 días de audiencia previa) y un **cuadro de permisos con su cómputo** (2+2, 5, 15, 4 días medidos en horas, 8 semanas no retribuidas **y las 2 retribuidas de A2**), los dos en celdas editables con su artículo. Son tablas de referencia, no calculadoras: no pisan al Kit de Gestión de Personal y dan herramienta a los tres capítulos huérfanos. Y el capítulo 01 debe **decir en su primera página** qué se incluye y qué no, en vez de dejar que el lector lo descubra en el 11.

---

### B5 · MEDIA — La FAQ mete por la puerta de atrás la intención de empleo que el slug excluye a propósito, y dos pares los marca el detector de la propia casa

> **Afirmación literal** (§10.1): «**Por qué no «gerente» en el slug ni en el title:** «gerente de restaurante» es **89 % ofertas de empleo** … donde sólo traería competencia contra InfoJobs»
> Y §10.2: las preguntas 1 a 4 son «¿Qué hace el encargado de un restaurante?» · «¿Cuáles son los rangos en un restaurante?» · «¿Cómo se llama el encargado del restaurante?» · «¿Qué es lo que hace un administrador en un restaurante?»

Las cuatro son PAA literal, sí — **de las dos SERP que el propio research mide como 89 % y 68 % de empleo** (L2 §2.1 y §2.2). Emitirlas en el `FAQPage` de la landing es pedirle a Google que muestre la página de producto para la intención que el §10.1 decidió evitar, con un visitante que busca trabajo o el nombre del puesto, no criterio de gestión por 65 €. La decisión del slug y la de la FAQ apuntan en direcciones opuestas.

Y hay un segundo problema, medible. Pasé las nueve preguntas del PAA por el clasificador de la propia casa (`scripts/astro-migration/fase8d-faq-duplicadas.py`, función `clasifica()`):

```
PARECIDA   0,79   Q1 «¿Qué hace el encargado de un restaurante?»  ||  Q3 «¿Cómo se llama el encargado del restaurante?»
PARECIDA   0,79   Q1 «¿Qué hace el encargado de un restaurante?»  ||  Q4 «¿Qué es lo que hace un administrador en un restaurante?»
```

**PARECIDA** es, según la cabecera del propio script, el nivel «revisar a mano». Dos pares sobre nueve, y a ojo hay un tercero que el clasificador no alcanza: Q5 «¿Qué debe contener un manual de operaciones?» y Q6 «¿Cómo hacer un manual de procedimientos para un restaurante?». En un rich result **cada `Question` aparece sola**, así que tres formulaciones de «qué hace / cómo se llama el encargado» se reparten una sola respuesta.

**Fix:** (a) fundir Q1+Q3+Q4 en una sola pregunta de jerarquía y vocabulario («¿Gerente, encargado, jefe de sala o administrador? ¿Es lo mismo?»), que además es la que A3 obliga a responder bien; (b) fundir Q5+Q6; (c) usar los tres huecos liberados para preguntas de **compra** —qué incluye y qué no (B4), compatibilidad, qué pasa cuando cambia la normativa—, que es lo que la decisión D13 de la familia ya estableció para la Guía Food Cost.

---

### B6 · MEDIA — Los «seis canales que ya son nuestros» no traen ni una cifra de conversión, y el único número medido son 73 impresiones

> **Afirmación literal** (§0): «este producto **no se lanza por volumen de búsqueda** … sino porque … **(c) tenemos el canal**»

La tabla de canales es honesta en lo que enumera, pero no hay **ni una estimación de unidades**. El único dato de tráfico medido en todo el bloque es «`gerente-restaurante` (**73 impresiones / 1 clic en GSC**)». El research no dice cuántas visitas traen los cinco posts afines, ni cuántos contactos tienen los cinco segmentos de Resend, ni qué convirtió el lanzamiento de ayer.

No pido inventar una previsión. Pido que **el precio no se decida sólo con anclas**: a 65 € con un canal cuyo tamaño no se ha medido, la elasticidad es exactamente el riesgo que no se está evaluando. Y el propio research reconoce (§13, L2) que **la canibalización en GSC no se ha comprobado** y lo llama «un chequeo de 5 minutos».

**Fix:** antes de firmar el precio, dos consultas de cinco minutos: (a) GSC `page × query` de los cinco posts afines y de las cinco páginas `/usos/rol/` a 90 días; (b) el recuento de contactos de los cinco segmentos de Resend. Con eso, «tenemos el canal» pasa de afirmación a número.

---

### B7 · MEDIA — Los argumentos 4 y 5 del precio se contradicen entre sí

> **Arg. 4:** «Respeta la escalera sin colisiones… Y la franja de 65 € **ya está establecida** con 7 productos»
> **Arg. 5:** «Deja sitio para la categoría… a 65 € la línea «Manuales operativos» **nace con precio propio**»

O la franja está ocupada —por **seis** productos, ver A14— y entonces la categoría nueva **no** nace con precio propio, nace encima del punto de precio más poblado del catálogo; o nace con precio propio y entonces la franja no estaba establecida. Las dos cosas no pueden ser a la vez, y el argumento 5 es el que justifica no bajar a 55 €.

Si de verdad se quiere escalón propio para la línea, en la escalera hay un hueco real: **no existe ningún producto entre 55 € y 65 €**. Un **59-60 €** sería «precio propio» de verdad, no compartido con seis vecinos.

---

### B8 · MEDIA — El presupuesto ya no cabe, y hay dos trabajos que no están contados

> **Afirmación literal** (§12.3): «La fase B de este producto **no cabe en una semana**… Recomendación: B1 y B2 en dos sesiones pares distintas»

El aviso está bien puesto. Lo que falta es que **dos partidas reales no aparecen en ninguna fase**:

1. **El script de banners.** §0 y §10.3 dan por hecho «inserción quirúrgica (patrón D11)». El patrón existe, pero está implementado en `fase8f-guia-food-cost-blog.py`, que **es específico de la Guía Food Cost**: `PRODUCTO`, `HOY` y la lista `PRIORIDAD_SUSTITUIR` están a fuego. Hay que escribir uno nuevo con su gate byte a byte — y además rehacerle la lista de prioridad, o hará lo contrario de lo que se quiere (C3).
2. **El verificador legal por bloque.** El riesgo 2 del §12.1 lo declara **obligatorio** («antes de escribir los capítulos 8-15 y 19, contra las fuentes primarias, no contra L3») — son **nueve capítulos** de verificación contra BOE. En §12.3 sólo aparece «1 verificador legal sonnet» dentro de B1, cuyo objeto declarado es el bloque normativo de las herramientas.

**Fix:** itemizarlos y decidir con John **antes de arrancar** —como el propio §12.3 pide— si el producto ocupa dos ciclos. Si los ocupa, el calendario de «1 producto/semana» se ajusta explícitamente, no a mitad.

---

### B9 · MEDIA — El mecanismo anticaducidad cubre los Excel y deja fuera la prosa, que es donde está el 70 % de lo que caduca

> **Afirmación literal** (§2.5): «3. Un bloque de «estado a la fecha de esta edición» **al principio del capítulo legal**»

Los puntos 1 y 2 (parámetros en celda, hoja `Estado Normativo`) son buenos y resuelven los xlsx. El 3 no resuelve el documento: **no hay «el capítulo legal»**. Hay contenido normativo en los capítulos 6, 8, 9, 11, 12, 14, 15, 19 y 20 — **nueve de veinte**. Un bloque de fecha al principio de uno deja sin fechar los otros ocho, y son los que llevan las cifras que caducan antes: SMI y cotización en el 04, Verifactu en el 06, tablas de convenio en el 08, registro digital en el 11, permisos en el 12, terrazas en el 19.

**Fix:** «**Verificado el <fecha> · <norma, artículo> · <URL>**» **al pie de cada tabla legal**, no una vez por capítulo. Es una línea por tabla, la genera el guion, y convierte el envejecimiento en una propiedad visible del documento en vez de en una errata. Es además la única forma de que el punto 6 («actualizaciones incluidas») se pueda ejecutar: sin fecha por tabla, quien regenere dentro de seis meses no sabrá qué revisar.

---

### B10 · BAJA — Entre el 60 y el 70 % del volumen de búsqueda medido está en mercados que el producto declara no cubrir

Los volúmenes del §0: «gerente de restaurante» 720 en México frente a 50 en España; «administrador de restaurante» 140 en Colombia, 260 en Chile, 170 en Perú frente a 10 en España. El research lo gestiona bien (vocabulario neutro, casillas editables, FAQ 10 explícita, sin versiones por país). Pero conviene tenerlo escrito en la SPEC como lo que es: **el producto se posiciona sobre la demanda española, que es la minoritaria**, y su diferenciador declarado —la normativa— es el único que no viaja. No cambia la decisión; cambia lo que se puede prometer en el copy y lo que se puede esperar de LATAM.

---

## C. TÉCNICO

### C1 · ALTA — `/usos/rol/director-operaciones-grupo` sería un 404 enlazado desde una landing de pago

> **Afirmación literal** (§0 nota 4, §0 tabla, §10.3 y §13): «`director-operaciones-grupo`», cuatro veces, presentado como una de las cinco páginas `/usos/rol/` a enlazar de forma bidireccional.

Ese es el **`id`** de la entrada en `src/data/use-cases.ts:182`, no su slug público. La URL la compone `ucSlug()` (`astro-site/src/lib/use-cases.ts:74-76`) a partir de **`uc.slug.es`**, y en este rol —y sólo en éste de los cinco— **no coinciden**:

| Rol | `id` | `slug.es` | URL pública real |
|---|---|---|---|
| propietario | `propietario-restaurante` | `propietario-restaurante` | `/usos/rol/propietario-restaurante` ✅ |
| gerente | `gerente-restaurante` | `gerente-restaurante` | `/usos/rol/gerente-restaurante` ✅ |
| **director ops** | `director-operaciones-grupo` | **`director-operaciones-grupo-restauracion`** (`use-cases.ts:187`) | **`/usos/rol/director-operaciones-grupo-restauracion`** |
| F&B hotel | `fb-manager-hotel` | `fb-manager-hotel` | `/usos/rol/fb-manager-hotel` ✅ |
| maître | `maitre-jefe-sala` | `maitre-jefe-sala` | `/usos/rol/maitre-jefe-sala` ✅ |

Quien construya el interenlazado copiando la cadena del research publicará un **301 a un 404 desde una landing de 65 €**. Y no lo cazaría ningún gate: `fase8c-enlaces-vivos.py` mira el blog, no las landings de producto.

**Fix:** corregir el slug en el research **y** ampliar el gate de enlaces vivos a `astro-site/src/data/productos/**` — que es donde vive el `footerLinks` de las 45 landings.

---

### C2 · ALTA — Seis reglas legales con artículo del BOE llegarán al redactor rotuladas «HUECO SIN FUENTE» y con la orden de no citarlas

Éste no está en el research y es el más silencioso de todos. `bloque_research()` (`documentos.py:760-785`) mete en la misma bolsa **todo id cuya `cifra` sea nula** y le manda al redactor esta línea literal:

```
- [MM-21] HUECO SIN FUENTE — «…»: NO escribas ninguna cifra sobre esto; formúlalo en cualitativo.
```

De los 52 ids `MM-*`, **seis tienen `cifra` vacía**, y **ninguno es un hueco**: son reglas **cualitativas con norma citada**.

| id | Contenido | Fuente que SÍ tiene | Capítulo |
|---|---|---|---|
| `MM-10` | Fijo-discontinuo: llamamiento por escrito, antigüedad por toda la relación | Art. 16 ET (RDL 32/2021) + URL | **cap. 09** |
| `MM-21` | Reconocimientos médicos voluntarios, requieren consentimiento | Art. 22.1 y 22.4 Ley 31/1995 + URL | **cap. 15** |
| `MM-24` | Propinas: rendimientos del trabajo sujetos a IRPF | DGT + URL | *(sin capítulo, ver A7)* |
| `MM-25` | Si la empresa reparte el bote, obligada a retener | Art. 76.1.3.º RIRPF + URL | *(sin capítulo)* |
| `MM-28` | Política escrita de desconexión digital, previa audiencia | Art. 88.3 LO 3/2018 + URL | **cap. 15** |
| `MM-38` | Agua no envasada gratuita: hay que **ofrecerla** | Ley 7/2022 art. 18.3 + URL | **cap. 19** |

El `f-string` que compone la fuente vive en la rama `else` de esa función (`documentos.py:774-780`), así que a estos seis **nunca se les pasa `fuente_titulo`**: el redactor escribirá el contenido legal **sin poder citar el artículo**. Y ocurre justo en los tres capítulos que el research vende como «la ventaja normativa» del producto — en el capítulo 15 son **2 de sus 5 ids**.

Es exactamente el patrón que la memoria del proyecto ya tiene documentado: **no falla, no avisa y ningún gate lo ve**. El documento saldría en verde diciendo «los reconocimientos médicos son voluntarios» sin poder añadir «art. 22.1 de la Ley 31/1995», que es **la mitad del valor de la frase**.

**Fix (una línea):** distinguir en `bloque_research()` «cifra ausente **con** fuente» —regla cualitativa citable, se le pasa la fuente y se le pide que cite el artículo— de «sin fuente» —el hueco de verdad—. Y, ya que se toca, verificar los otros productos de la familia: el mismo defecto afecta a cualquier guion con reglas cualitativas.

---

### C3 · ALTA — Los cinco posts ya tienen sus tres banners, y reutilizar el patrón existente borraría precisamente los cross-sell del manual

> **Afirmación literal** (§0 y §10.3): «inserción quirúrgica (**patrón D11**) en los 5 posts afines» · «**Banner fijado** (sustitución quirúrgica del menos afín)»

**Dato que el research no dice en ningún punto: los diez posts candidatos ya tienen exactamente 3 banners**, que es el máximo de la política vigente desde el 31-08-2026. «Fijar» el del manual en los cinco primeros significa **retirar un producto de cada uno de los cinco** — cinco productos que dejan de venderse desde ahí, en contra de la regla de cobertura de agosto (44/44, máximo 7,1 %). Eso hay que decirlo y decidirlo, no descubrirlo al ejecutar.

Y el patrón que se pretende reutilizar haría lo contrario de lo que se busca. `fase8f-guia-food-cost-blog.py` sustituye por esta lista de prioridad:

```python
PRIORIDAD_SUSTITUIR = ['kit-tareas-', 'plan-negocio-', 'guia-panaderia', 'guia-restaurante',
                       'guia-dark-kitchen', 'mega-pack', 'pro-prompts', 'pack-appcc',
                       'kit-gestion-personal', 'kit-plan-financiero']
NUNCA = ('kit-escandallos', 'kit-inventario', PRODUCTO)
```

Esa lista está escrita **para un producto de food cost**: quita primero los kits de tareas y protege escandallos e inventario. Para el Manual del Manager es exactamente al revés — sus vecinos afines son **kit-tareas, kit-gestion-personal y pack-appcc**, que están en la lista de sacrificio, y `kit-escandallos`/`kit-inventario`, que están protegidos, son los menos afines de todos. Ejecutarlo así **retiraría de los cinco posts los banners de los productos que la propia landing pone como cross-sell** (§10.3, «Salientes») y dejaría los de escandallos. El script no fallaría, el gate byte a byte pasaría, y el resultado sería un blog que empuja al manual desde posts donde acaba de borrar a sus complementos.

Un caso concreto que lo ilustra: en `libreria-de-prompts-para-gerente-de-restaurante-pro-ai` los tres banners actuales son `kit-plan-financiero`, `kit-gestion-personal` y `kit-inventario` — **los tres afines al manual**. Ahí no hay un «menos afín» obvio y hay que decidirlo a mano.

**Fix:** el script nuevo (`fase8g`) necesita **su propia `PRIORIDAD_SUSTITUIR` y su propio `NUNCA`**, con `kit-gestion-personal`, `kit-tareas` y `pack-appcc` protegidos, y `kit-escandallos`, `plan-negocio-*` y las guías de apertura como candidatos. Y parametrizar `PRODUCTO`/`HOY` para que el próximo producto no necesite un tercer fichero.

---

### C4 · MEDIA — El gate de páginas está calibrado tan bajo que no puede detectar nada

> **Afirmación literal** (§8): «la promesa interna del gate va en **60** y la landing publica la cifra MEDIDA tras construir (decisión D17)»

Medí los PDF publicados de la Guía Food Cost con PyMuPDF y los crucé con las palabras declaradas en su guion:

| Documento | Palabras del guion (`'palabras'` sumadas) | Páginas medidas | Palabras redactadas / página |
|---|---|---|---|
| `guia-food-cost-ingenieria-menu.pdf` | **31.300** | **95** | **330** |
| `BONUS-ejercicios-resueltos.pdf` | **7.610** | **32** | **238** |

La calibración de la síntesis es **correcta** (28.000-32.000 palabras → 85-97 páginas; 7.500 → ~31). Lo que no aguanta es el gate: el documento saldrá en torno a **90 páginas** y `paginas_prometidas: 60` deja **30 puntos de holgura**. Un manual un tercio más corto **pasaría en verde**. Lo mismo con `min_palabras_cap: 900` frente a un objetivo de 1.400-1.600: un capítulo un 40 % corto pasa.

Un gate que no puede fallar no es un gate — y esta familia ya tiene documentado el patrón «sospechar del gate antes que del dato».

**Fix:** `paginas_prometidas` a **85** y `min_palabras_cap` a **1.200**, manteniendo D17 (la landing publica lo medido). Si el documento sale por debajo de 85, eso es justo lo que hay que saber antes de publicar.

---

### C5 · MEDIA — El `comingSoon` del hub lleva dos meses caducado y además llama «Guía» al manual

Verificado en los dos ficheros, con la misma redacción:

- `src/pages/ProductosDigitales.tsx:911`
- `astro-site/src/components/pages/ProductosDigitalesHubPage.astro:921`

```
name: 'Manual del Manager de Restaurante',
desc: 'Guía completa del gerente: operaciones, personas, finanzas, servicio y liderazgo.',
phase: 'Julio 2026'
```

El research señala que hay que quitar la entrada al publicar (§12.1 riesgo 9), pero no dice dos cosas: (a) **`phase: 'Julio 2026'` está caducado desde hace dos meses y está vivo en producción** — un «próximamente» con fecha pasada es peor que no anunciar nada; (b) la `desc` publicada empieza por «**Guía** completa del gerente», que contradice el reposicionamiento como línea de **manuales** y como categoría nueva.

**Fix:** si el producto no sale esta semana, **corregir `phase` hoy** (es un cambio de una cadena en dos ficheros) y alinear la `desc` con el nombre de la categoría. Al lanzar, quitar la entrada de los dos.

---

### C6 · MEDIA — La FAQ de las 45 landings de producto no la barre ningún gate

Detallado en B5: `fase8d-faq-duplicadas.py` sólo recorre `astro-site/src/content/blog/`. Las 45 landings emiten `FAQPage` desde `GuiaData.faqs` y **ninguna pasa por el detector**. Extenderlo son veinte líneas y protege 45 páginas, no una.

---

### C7 · BAJA — Queda un literal «esta guía» en el prompt que lee el redactor

`documentos.py:1027`, cabecera del bloque `prohibido`: `'anterior de esta guía y no se pueden repetir):\n'`. **No se imprime en el documento**, pero es lo último que el redactor lee antes de escribir, y el `SYSTEM` le pide primera persona del plural: un modelo al que se le dice «esta guía» tres párrafos antes tiene probabilidad no despreciable de escribir «esta guía» en el cuerpo de un **manual**. Es otro `guia.get('tipo_doc','guía')` de una línea. (Aparte: si el manual reutiliza el motor de xlsx, `grupo_c.py:175` define `NOTA_SIN_DATO = ('Sin dato en la guía: escríbelo tú…')`, que **sí es texto de celda**, y `grupo_c.py:1134,1559,1761,1882` construyen notas con la palabra «guía».)

---

## Tabla resumen de hallazgos

| id | Gravedad | Qué | Fix |
|---|---|---|---|
| **A1** | **ALTA** | La herramienta 1 siembra la SS a cargo de la empresa al **23,60 %** (sólo contingencias comunes) cuando lo real es **32,15 %** y los dos productos que dice reutilizar usan **33 %**; infravalora el prime cost en **2,3 puntos de venta** y da falsos «En objetivo» | Desglosar las 5 cotizaciones en celda (total 32,15 % indefinido) o sembrar 33 %; sacar MM-17 del rol de «coste-empresa» |
| **A2** | **ALTA** | El permiso parental: desde el **RDL 9/2025** hay **2 semanas SÍ retribuidas** hasta los 8 años (art. 48.4.c ET, protegidas por el art. 177 LGSS) junto a las 8 no retribuidas. La lista negra **impediría escribir la parte correcta** | Tabla de dos figuras en el cap. 12 y en MM-26; nacimiento a **19 semanas**; reescribir la entrada de la lista negra |
| **A3** | **ALTA** | El ALEH VI **no** tipifica «encargado de restaurante», «director» ni «administrador»; el «gerente de centro» que sí trae es de **restauración moderna** | Reescribir concepto 1 y cap. 01; componer el organigrama con BOE-A-2023-6344 **+** BOE-A-2026-18630 |
| **A4** | MEDIA | El *doggy bag* obliga desde el **22-12-2022**, no desde el 15-12-2022 — y el research usa la fecha correcta de la misma norma dos filas más abajo. Faltan la excepción del bufé y la obligación de informar | Corregir en los dos sitios y añadir excepción + cartelería |
| **A5** | MEDIA | La exclusión de las simplificadas del RD 238/2026 **no es absoluta**: las **cualificadas** (tique con NIF del cliente) sí entran | Regla de tres casillas en el cap. 06, con remisión al art. 7.2 RD 1619/2012 |
| **A6** | MEDIA | La exención de 1.300 m² de la Ley 1/2025 alcanza **sólo al apartado 4**; los arts. 6.1, 6.2, 6.3 y 6.5 obligan a todo restaurante que no sea microempresa | «De qué estás exento / de qué no», en dos columnas |
| **A7** | MEDIA | Las **propinas** son uno de los 18 conceptos obligatorios y no están en ningún capítulo (MM-24 y MM-25 huérfanos); y **ni la V3095-17 ni la V2236-13 se pudieron verificar** en el buscador de la DGT | Bloque al cap. 06; verificar a mano las dos consultas o apoyarse sólo en el RIRPF; tabla de trazabilidad concepto→capítulo |
| **A8** | MEDIA | La lista negra veta **dos** datos que el INE sí publica: supervivencia de **hostelería** (75,6 / 53,5 / 38,8) y **absentismo de hostelería** (ETCL tabla 6043). Y el 63,5 % es la tasa a **2 años**, no a 3 | Corregir la etiqueta, usar las dos series del INE y reescribir las dos entradas de la lista negra |
| **A9** | MEDIA | Reconocimientos médicos: faltan las **tres excepciones** del art. 22.1, y la segunda es la que se invoca para manipuladores | Regla completa + informe previo de la RLT, al cap. 15 y a MM-21 |
| **A10** | MEDIA | El 63,8 % va a lista negra pero el **1.512 €/2.345 € del mismo informe** se queda en la tabla; y la temporalidad del 12,6 % **se invierte en el 2T 2026** | Sustituir por el dato primario del INE (17.190,75 € vs 28.410,78 €); fechar o sustituir la temporalidad |
| **A11** | MEDIA | **Once citas del §5 no dicen lo que se les atribuye**: el 39 % de TheFork es de una muestra **de ticket medio > 25 € y perfiles directivos**; el prime cost 60-65 % es de **Laube/RestaurantOwner, no de Toast** (Toast dice 60 % o menos); CaixaBankLab no dice «Sapiens» ni «barra/autoservicio» y **sí tiene fecha** (2017, rev. 2022); el ticket medio de 21 € es de **2024**, no del 1S 2025; el +19 pp es **sólo la franja de las 19:00**; el 1,92 % de CoverManager es **un solo día**; los 17.094 € no están en el RD del SMI; «beneficios sociales» no es variable de la EACL; y tres matices en Square+AmEx | Acotar cada una en la propia frase antes de que pase al guion; ninguna obliga a renunciar al dato |
| **A12** | MEDIA | Lista negra incompleta (**11** entradas); y el «60 % de los restaurantes cierra», vetado aquí, **sigue publicado** en 3 sitios del repo | Ampliar §11; tarea separada para `guia-restaurante-casual.ts:21`, `HeroSection.tsx:71` y `pseo-cities-content.es.ts:60` |
| **A13** | MEDIA | El art. 41.3 tiene una **excepción** y una remisión al art. 55.1 ET que se omiten, y no consta que aplica **desde el 04-09-2026** (vigencia hasta 31-12-2030) | Las tres al cap. 14 y a MM-13, con cita literal |
| **A14** | MEDIA | «Actualizado al BOE del día del lanzamiento» caduca entre research y publicación, y el **RD del registro horario está anunciado para este mes**. Los detalles de tramitación no tienen respaldo primario | Gate de re-chequeo de las 7 normas 48 h antes de publicar; bajar los detalles a «según el Ministerio»; reformular el claim |
| **A15** | BAJA | Cuatro recuentos: **6** productos a 65 € (no 7) · **18** secciones del INE (no 19) · **9** posts (no 10) · los 3 fixes **están commiteados** (`68eb353`), y la prueba de no-regresión sigue pendiente sobre código ya en `main` | Corregirlos antes de que sostengan argumentos |
| **B1** | **ALTA** | 65 € contradice la decisión **D1 firmada ayer** para el mismo recuento (20 caps + 8 xlsx + bonus = 55 €); a 65 € tiene **2 bloques de entregables menos** que sus seis vecinos de precio | 55 €, o 65 € añadiendo checklists + 2.º documento (lo que D2 descartó) |
| **B2** | **ALTA** | «menos de lo que cuesta un mes de cualquiera de sus tres planes» es **falso**: Starter = 60,50 € con IVA < 65 €. Y el «5,7 %» mezcla precio con IVA y anual sin IVA (real: **4,7 %**) | Reescribir el ancla con cifras homogéneas y sin el plan Starter |
| **B3** | **ALTA** | 3 de los 8 libros repiten material del comprador objetivo: el **5 es duplicado estructural** (mismas 4 hojas), el **1 solapa ~70 %** y la hoja de briefing del **7** existe ya 20 veces | El 5 no es un libro; el 1 renuncia al prime cost; el 7 pierde el briefing → **7 libros densos** |
| **B4** | **ALTA** | Los caps. **11, 12 y 14** no tienen ninguna herramienta del manual: su única herramienta es el Kit de Gestión de Personal (14 €, no incluido). 7 de 20 caps remiten a producto aparte | Dos hojas de referencia (topes de jornada, cómputo de permisos) en la herramienta 6; y decir en el cap. 01 qué se incluye y qué no |
| **B5** | MEDIA | La FAQ reintroduce la intención de **empleo** que el slug evita; `clasifica()` marca 2 pares **PARECIDA 0,79** | Fundir Q1+Q3+Q4 y Q5+Q6; liberar 3 huecos para preguntas de compra |
| **B6** | MEDIA | «Tenemos el canal» sin una cifra de conversión; el único número medido son **73 impresiones / 1 clic** | GSC `page × query` de los 5 posts y las 5 páginas de rol + recuento de segmentos Resend, antes de firmar el precio |
| **B7** | MEDIA | Arg. 4 y arg. 5 del precio se contradicen (franja «ya establecida» vs «precio propio») | Si se quiere escalón propio, el hueco real está en **59-60 €** |
| **B8** | MEDIA | El presupuesto no cuenta el **script de banners nuevo** ni la verificación legal de **9 capítulos** | Itemizarlos y decidir con John si ocupa dos ciclos, antes de arrancar |
| **B9** | MEDIA | El bloque de fecha va «al principio del capítulo legal» y lo legal está en **9 capítulos** | «Verificado el <fecha> · norma · URL» **al pie de cada tabla legal** |
| **B10** | BAJA | El 60-70 % del volumen medido está en mercados cuya normativa no se cubre | Escribirlo en la SPEC como límite del copy y de la expectativa |
| **C1** | **ALTA** | `/usos/rol/director-operaciones-grupo` es un **404**: el slug público es `director-operaciones-grupo-restauracion` (`use-cases.ts:187`). El research usa el `id` como URL 4 veces | Corregir el slug y ampliar `fase8c-enlaces-vivos.py` a las landings de producto |
| **C2** | **ALTA** | **6 reglas legales con artículo del BOE** (`MM-10, 21, 24, 25, 28, 38`) llegarán al redactor como «HUECO SIN FUENTE» con la orden de no citar (`documentos.py:760-785`), en los caps. 09, 15 y 19 | Distinguir «cifra ausente **con** fuente» de «sin fuente» — una línea |
| **C3** | **ALTA** | Los 5 posts **ya tienen 3 banners** (el research no lo dice) y reutilizar `fase8f` borraría los banners de **kit-gestion-personal, kit-tareas y pack-appcc** —los propios cross-sell— dejando los de escandallos | `fase8g` con su propia `PRIORIDAD_SUSTITUIR`/`NUNCA` y `PRODUCTO`/`HOY` parametrizados |
| **C4** | MEDIA | `paginas_prometidas: 60` con salida esperada de ~90 (calibración medida: **330 palabras/página**); `min_palabras_cap` 900 sobre objetivo 1.400 | Gate a **85** páginas y **1.200** palabras/capítulo |
| **C5** | MEDIA | El `comingSoon` lleva **dos meses caducado** (`phase: 'Julio 2026'`) y su `desc` llama «**Guía**» al manual, en los dos ficheros del hub | Corregir hoy si no sale esta semana; quitar las dos entradas al lanzar |
| **C6** | MEDIA | Ningún gate barre la FAQ de las 45 landings de producto | Extender `fase8d-faq-duplicadas.py` a `astro-site/src/data/productos/**` |
| **C7** | BAJA | Residuo «esta guía» en el prompt del redactor (`documentos.py:1027`) y en las notas de celda de `grupo_c.py` | Un `tipo_doc` más |

---

## Lo que SÍ aguanta

Y aguanta bien, porque lo he comprobado, no porque lo diga el documento:

1. **El hallazgo del día es real, y es exactamente lo que dice.** Descargué el PDF de [BOE-A-2026-18630](https://www.boe.es/boe/dias/2026/09/04/pdfs/BOE-A-2026-18630.pdf) (BOE núm. 219 de 04-09-2026, pp. 119174-119189) y lo leí entero. Existe, es la Resolución de 25-08-2026 de la DGT, está suscrito el **11-06-2026** por CEHE y CEHAT con FeSMC-UGT y CC.OO.-Servicios, modifica el preámbulo y los arts. **6, 9, 10, 15, 16, 17, 38, 39, 40 y 41** y las tablas del anexo I, y añade el **cap. XIII (arts. 67-74, LGTBI)** y el **cap. XIV (arts. 75-80, catástrofes)** — los rangos de artículos son correctos uno a uno. El art. **41.3** dice literalmente lo que la síntesis afirma, incluidos los **«dos días»** para contestar y que «estos dos días **se consideran como de permiso retribuido**» si se aparta a la persona del servicio, citando la **STS 1250/2024 de 18-11-2024 (rcud 4735/2023)** y el art. 7 del Convenio 158 de la OIT. Y los tres apartados disciplinarios son literales: **38.10** «dos incumplimientos» (leve), **39.21** «de tres a cuatro» (grave), **40.14** «cinco o más» (muy grave); más el **38.12** del móvil y el **39.20** de fumar. Añado el dato que faltaba: **aplica desde la publicación en el BOE, 04-09-2026, y hasta el 31-12-2030**. **El argumento de venta nº 1 se sostiene entero.**
2. **De las 20 afirmaciones normativas verificadas contra fuente primaria, 13 salen confirmadas al pie de la letra**: las 37,5 h rechazadas (con el escrutinio de la votación), Verifactu 1-01-2027 / 1-07-2027 por el art. 3 del RDL 15/2025, el SMI de **1.221 €/mes y 40,70 €/día** del RD 126/2026, la terraza de «un **máximo de dos** paredes», el RD 3484/2000 derogado y el art. 30 del RD 1086/2020 con sus temperaturas, el carné de manipulador derogado por el RD 109/2010, el fallecimiento de 2+2 días separado por el RDL 5/2023, el registro retributivo **sin umbral**, el LGTBI a «**más de** cincuenta», **todas** las cuantías del art. 40 LISOS y su atribución a la Ley 10/2021, el efectivo hasta 999,99 € y el art. 47.ñ) desde el 28-05-2022, la factura simplificada de 3.000 € en hostelería, y el preaviso de 5 días con el calendario laboral visible. **Es un porcentaje de acierto muy alto para un bloque legal de este tamaño.**
3. **Y la ausencia también está probada.** Un barrido de los **247 sumarios del BOE del 1-ene al 4-sep-2026** por la API de datos abiertos confirma que **no existe ningún RD de registro horario digital ni ninguna ley antitabaco**. El «hoy no te obliga nada de esto» —que es el mensaje útil para el manager— está sólidamente respaldado.
4. **El dato estrella del eje de personas resiste al céntimo.** El gasto en formación profesional de la EACL 2025: **20,14 €** en hostelería frente a **76,49 €** de media nacional (26,3 %). La variable existe **con ese nombre exacto** («Gastos en formación profesional», tabla 9125 de la API Tempus del INE), la EACL 2025 está publicada (23-07-2026), hostelería es el mínimo de las 18 secciones y —dato extra que **refuerza** el argumento y que el research no tiene— en 2024 era 22,87 €, así que **cae un 11,9 % interanual frente al 2,4 % nacional**: la hostelería no sólo invierte una cuarta parte, es que está reduciendo la inversión cuatro veces más rápido que el resto de la economía.
5. **Y con ella, otras cinco cifras del §5 salen confirmadas al pie de la letra**: el coste laboral de hostelería (**23.690,02 €**, el más bajo) y los sueldos (**17.190,75 €**, también el más bajo) de la EACL; el DIRCE (**266.476** empresas, 63.063 sin asalariados, 6.736 con ≥20, y cuadra: CNAE 55 + 56); el **75 %** de ManpowerGroup con su desglose 69/6 y sus comparaciones global 74 % y Europa 76 %; y las dos citas académicas de reseñas, **literales** en el PDF original («a one-star increase in Yelp rating leads to a 5-9 percent increase in revenue», «driven by independent restaurants»; y la referencia exacta de *The Economic Journal* 122(563):957-989). También queda confirmado el matiz contraintuitivo que el research quiere explicar: **la bebida sí tiene peor food cost porcentual (34,5 %) que la comida (28 %)**, y la ponderación 70/30 cierra en el 30 % declarado.
6. **La lectura de la demanda es honesta y va contra el propio interés del producto.** Decir que la keyword obvia es 89 % empleo, que la intención más limpia vale 10 búsquedas/mes y que «la landing no va a captar por búsqueda y no se debe prometer que lo haga» es lo contrario de lo que haría un research que quiere que le aprueben el producto.
7. **La disciplina de fuentes de L3 es de nivel profesional.** Cinco autocorrecciones al propio encargo (el RD 830/2022 que no existe, el art. 6.3 de la Orden de 1989 que no se derogó, la Ley 10/2021 en vez del RDL 5/2023, la V2236-13 en vez de la V3095-17, el RD 3250/1983 derogado), y una separación explícita entre lo que la norma exige y lo que el sector vende como obligación —las **cuatro** periodicidades fijadas por norma estatal frente a las que no lo están— que es, de todo el research, el material más difícil de copiar y el mejor argumento de criterio del producto.
8. **Tres de los ocho libros son huecos de mercado reales**, medidos sobre los 432 xlsx publicados: `polivalenc`, `queja`, `reclamac`, `reseñ`, `review`, `acta`, `reunión` y `auditoría` dan **cero hojas** en todo el catálogo. Los libros 2, 3 y 8 no duplican nada.
9. **La capa técnica está más limpia de lo que el propio research cree.** `robots.txt` cubre `manual-*-access` y `manual-*-library` en los **5** bloques de user-agent, sin colisión posible con ninguna URL pública (el único slug del repo que empieza por `manual-` es un post del blog, servido bajo `/blog/`), y `robots-gate.py --live` sale verde sobre 1.188 URLs. `products-catalog.ts` tiene **45** entradas por los tres métodos de recuento, incluido el parser de `fase8c-libreria-assemble.py` —el bug silencioso de agosto **no se reproduce**—. `tipo_doc`, `categoria_doc`, `why.titlePre` y `why.titleGold` están correctamente parametrizados y consumidos (`GuiaLandingPage.astro:360`). Los **52 ids `MM-*`** son correlativos, sin lagunas, y **ningún id citado en el §8 falta del JSON**. Y **no hay un solo glob sobre `productos/guias/`**: las 10 referencias son imports estáticos, así que **crear `manuales/` es seguro** (decisión D7) — el único coste es duplicar o importar cruzado el `types.ts`.
10. **La calibración de páginas es correcta**, medida contra el PDF real: 330 palabras redactadas por página en el documento principal y 238 en el bonus. 20 capítulos de 1.400-1.600 dan ~90 páginas y 7.500 palabras de bonus dan ~31. Lo único que falla ahí es el gate (C4), no la previsión.
11. **Las decisiones D2, D3, D11 y D12 son correctas** — bonus de casos resueltos en vez de otro paquete de checklists, ocho libros como marco de trabajo (aunque salgan siete tras B3), sin `aggregateRating` ni testimonios, y reutilizar el restaurante modelo de la Guía Food Cost para que los ejemplos crucen entre productos.

---

## Recomendación de precio

**55 €.** Es el precio que la casa firmó ayer, con argumentos escritos, para un paquete idéntico en todo lo que un comprador puede contar: 20 capítulos, 8 libros de Excel y un bonus de 12 piezas. A 65 € el manual se sienta en el hub al lado de seis productos del mismo precio que traen **6 checklists y un segundo documento más**, y al lado de uno de 55 € que trae exactamente lo mismo que él. La «amplitud temática» es real, pero no aparece en ninguna tarjeta y no la puede comprobar quien está decidiendo. Y el argumento que sostenía el 65 € —el ancla del SaaS— tiene una frase falsa dentro (B2).

Si John quiere que la línea «Manuales operativos» nazca con escalón propio —el único argumento del §9.2 que no se cae—, el hueco real de la escalera está en **59-60 €**: ahí no colisiona con nadie, mantiene la distancia con la Guía Food Cost y sigue por debajo del bundle de Hotmart. **65 € sólo es defendible si el paquete gana lo que la franja de 65 € tiene**, y eso choca con la decisión D2 del propio orquestador.

---

**Via: Claude Code**
