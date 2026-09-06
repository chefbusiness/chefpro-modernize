# REFUTACIÓN — «Manual del Chef Ejecutivo»

**Fecha:** 2026-09-06 · **Objeto:** `manual-chef-ejecutivo-RESEARCH-2026-09-06.md` (944 líneas) y las seis lentes `L1`…`L6` del mismo directorio.
**Método:** tres lentes en un pase (rigor · negocio · producto), con verificación directa contra fuentes primarias (BOE consolidado en PDF, extraído con PyMuPDF), contra el repositorio y contra los 438 xlsx del catálogo. **Se ha intentado TUMBAR la propuesta, no confirmarla.**

**Veredicto: CORREGIR ANTES.** 28 refutaciones: **6 altas · 14 medias · 8 bajas**. La propuesta es sólida en su núcleo —el hueco de mercado existe, la frontera con el hermano está pensada y el bloque normativo de cocina es real y verificable—, pero **no se puede firmar la SPEC tal cual**: hay una cifra de portada que se cae al recomputarla, tres duplicaciones con el hermano que la tabla de frontera no ve, una promesa de compatibilidad que el propio diseño de los libros contradice, y un presupuesto cuya mitigación no cierra por un factor de 2,5.

**Lo que SÍ he confirmado letra a letra** (para que no se re-verifique): CE-11 (comidas testigo, art. 30.8-10 del RD 1086/2020: umbral de **más de 40 personas**, ≥100 g, ≥7 días, ≤4 °C o ≤−18 °C) es **exacto**; CE-10 (4/8/−18 °C, 60→10 °C en <2 h, recalentado ≥74 °C ≥15 s) es **exacto**; CE-33 (exención de 1.300 m² de la Ley 1/2025) es **exacto**, incluida la trampa del mismo CIF; CE-21 y CE-22 existen en el Anexo III y el Anexo I del RD 486/1997; los tres defectos de §14.4 **existen los tres** en producto vendido; `robots.txt` cubre `manual-*` en los 5 bloques; `products-catalog.ts` tiene **46** entradas; el `comingSoon` está en `ProductosDigitales.tsx:927` y en `astro-site/src/components/pages/ProductosDigitalesHubPage.astro:942`; las 20 páginas de rol tienen `productIds` poblados y **`manual-manager-restaurante` y `guia-food-cost-ingenieria-menu` aparecen 0 veces** en `src/data/use-cases-content.es.ts`.

---

## A — RIGOR

### A1 · ALTA — El «+49,9 %» de la portada del capítulo 3 se cae al sumar el Plus Convenio

**Afirmación literal (§3.4):** «**El mismo puesto, dos provincias** (clase/grupo A, 2026) — Jefe/a de Cocina Madrid **1.415,47 €**, Barcelona **2.121,29 €**, **+49,9 %**» … «Es la mejor prueba de por qué este manual NO puede dar una cifra única de nómina.»

**Problema.** Dos defectos sumados, los dos verificables por el lector en un minuto:

1. **Se comparan magnitudes distintas.** La propia tabla de Madrid dice tres líneas más arriba: «**Se suma siempre** Plus Convenio 191,22 €/mes en 11 pagas». El Plus Convenio no está en la cifra comparada; el salario catalán no tiene contrapartida equivalente declarada (L4 §7.2 sólo añade manutención, alojamiento y transporte, y manutención también existe en Madrid). Recomputado a **bruto anual de convenio** (base × 14 + plus × 11):

   | Puesto | Madrid anual | Barcelona anual | Diferencia real | Publicado |
   |---|---|---|---|---|
   | Jefe/a de Cocina | 21.920,00 € | 29.698,06 € | **+35,5 %** | +49,9 % |
   | Segundo/a Jefe/a | 20.537,50 € | 26.103,14 € | **+27,1 %** | +41,6 % |
   | Cocinero/a | 20.077,04 € | 25.242,70 € | **+25,7 %** | +40,4 % |
   | Ayudante | 19.155,28 € | 22.501,50 € | **+17,5 %** | +32,0 % |
   | Auxiliar | 18.233,52 € | 22.078,70 € | **+21,1 %** | +36,9 % |

   **Las cinco filas están infladas entre 12 y 15 puntos.**
2. **La etiqueta del año es falsa.** El encabezado dice «(clase/grupo A, **2026**)», pero la tabla de Madrid es la **de 2025 congelada por ultraactividad** (el propio §3.4 lo dice al presentarla) y la catalana es la tabla **Any 2026**. Comparar una tabla congelada contra una actualizada ensancha el hueco otra vez.

Además, «Clase A» (Madrid: 4-5 tenedores y salones de banquetes) y «Grup A» (Cataluña) son clasificaciones de establecimiento distintas; equipararlas es una decisión metodológica que hay que declarar, no dar por hecha.

**Gravedad: alta.** Es la cifra estrella del §3.4, entra en el capítulo 03 y es exactamente el tipo de dato que el manual promete que el lector puede comprobar. Un comprador de Madrid con su nómina delante la desmonta.

**Fix.** Publicar **bruto anual de convenio** (base × pagas + plus convenio + complementos citados), recalcular las cinco filas con los porcentajes reales, etiquetar Madrid como «tabla 2025 en ultraactividad» y añadir una línea diciendo que las clases de establecimiento no son homologables entre convenios. El argumento («no hay cifra única de nómina») sobrevive intacto con +35,5 %: no hace falta el 49,9.

---

### A2 · MEDIA — «La temperatura legal de la cocina es 14-25 °C»: la síntesis borró el matiz que L3 sí puso

**Afirmación literal (§2.4 nº 3, §1 nº 15, cap. 17):** «la **temperatura legal de 14-25 °C** que casi ninguna cocina cumple en verano» · «**PRL — temperatura del local**: Trabajos ligeros: 14-25 °C».

**Problema.** Verificado hoy en el BOE (RD 486/1997, Anexo III, punto 3): el rango existe y **no hay exclusión expresa para cocinas** — hasta aquí, correcto. Pero el Real Decreto sólo fija rango para **dos** categorías: trabajos sedentarios (17-27 °C) y **trabajos ligeros** (14-25 °C). No fija ninguno para el trabajo pesado. **L3 escribió «trabajos ligeros (la clasificación que *suele* aplicarse a cocina)»; la síntesis eliminó el "suele" y lo convirtió en "la temperatura legal"** de una cocina. Clasificar el trabajo de una partida de calientes en plena carga como «ligero» es una conclusión de la evaluación de riesgos, no un dato de la norma; y el punto 4 del mismo Anexo III admite expresamente «las limitaciones o condicionantes que puedan imponer las características particulares del lugar de trabajo».

**Gravedad: media.** El bloque de PRL se vende como «donde más se puede corregir al sector» (§2.4 nº 3). Sostenerlo sobre una clasificación que el propio research califica de habitual, no de normativa, invita a la refutación del primer técnico de PRL que lo lea.

**Fix.** Escribir la frase como está en la norma: «el RD fija 17-27 °C para trabajo sedentario y 14-25 °C para trabajo ligero, y no fija rango para el trabajo pesado; en qué categoría cae tu cocina lo determina tu evaluación de riesgos, y el Anexo III admite condicionantes del propio local». Es más útil y es inatacable.

---

### A3 · MEDIA — Al bloque de temperaturas le falta el número que más se usa en una cocina (63 °C) y las dos cláusulas de flexibilidad

**Afirmación literal (CE-10, §2.1 y cap. 13):** «Refrigeradas ≤4 °C si vida útil >24 h y ≤8 °C si <24 h; congeladas ≤−18 °C; enfriar de 60 a 10 °C en <2 h; recalentar a **≥74 °C ≥15 s** en el centro».

**Problema.** He extraído el artículo 30 completo del texto consolidado (`boe.es/buscar/pdf/2020/BOE-A-2020-15872-consolidado.pdf`). Todo lo citado es literal y correcto. Pero **faltan tres cosas del mismo artículo**, y las tres son criterio, que es lo que el producto vende:

- **Art. 30.2:** las comidas preparadas se sirven cuanto antes «a menos que se refrigeren, congelen o **se mantengan a una temperatura superior o igual a 63 °C**». El **mantenimiento en caliente a 63 °C** es el número que un jefe de cocina mira varias veces por servicio (baño maría, vitrina, buffet, delivery) y **no aparece en ninguna parte del research**: ni en CE-10, ni en el capítulo 13, ni en la lista de temperaturas del §1.
- **Art. 30.5:** el operador **puede fijar temperaturas de conservación distintas** de las del apartado 3 si lo demuestra con evidencias científicas ante la autoridad competente.
- **Art. 30.7:** **pueden aplicarse temperaturas de recalentamiento más bajas** si la combinación tiempo/temperatura es equivalente a efectos de destrucción microbiana.

**Gravedad: media.** Publicar «74 °C o nada» es el mismo rigidez-sin-matiz que el manual reprocha a los blogs del sector, y omitir el 63 °C deja fuera el parámetro operativo más frecuente. Además, el 63 °C es imprescindible para el capítulo de delivery que hoy no existe (ver C3).

**Fix.** Añadir a CE-10 los apartados 30.2, 30.5 y 30.7 con su texto; el capítulo 13 lista **cinco** temperaturas (63 / 4 / 8 / −18 / 74-15 s) más el binomio 60→10 °C en 2 h, y dice en una frase que la norma admite equivalencias documentadas.

---

### A4 · MEDIA — «El mercado paga más por dirigir cocina que por dirigir sala» compara diplomas universitarios con cursos de 49 €

**Afirmación literal (§6.2 nº 1, repetida en §10.3):** «El mercado paga **sistemáticamente MÁS** por dirigir cocina que por dirigir sala. En ningún punto de comparación resultó más barata la formación de cocina: Cámara de Madrid 4.300 €, CETT 5.152,50-6.222,50 €, CIB 7.714-9.075 € — y en el censo del Manual del Manager los cursos generalistas de gestión estaban en **49-260 €**.»

**Problema.** El «49-260 €» del censo del hermano son, verificado en `manual-manager-RESEARCH-2026-09-04.md:175`, **Aprendum (150 €, normal 260) y estudioformacion (49 €, normal 159), cursos online con acceso limitado a 6 meses**. Se están comparando **diplomas y posgrados universitarios presenciales** contra **dos cursos online de tarifa promocional**. El censo del Manager **no incluyó ningún posgrado de dirección de restauración o de F&B** —que existen y cuestan miles de euros—, así que la ausencia de equivalente de sala mide el alcance de aquel censo, no el mercado. **La propia L1 lo dice** (`L1:122`): el precio del equivalente generalista de Cámara es «**sin cifra confirmada**» y el argumento es «de **POSICIONAMIENTO**, no de coste de producción».

**Gravedad: media.** Es el pilar del escenario de 65-69 € del §10.3 y el hallazgo nº 1 del §6.2. Sostener una decisión de precio sobre una comparación no homologable es exactamente el error que el research denuncia en `qamarero.com`.

**Fix.** O se retira la afirmación, o se censan 3-4 posgrados españoles de dirección de restauración/F&B y se compara con los de cocina. Mientras tanto, la frase honesta es: «el censo no encontró en formación de cocina ningún producto por debajo de 695 €», que es un hecho verificado y ya sirve de ancla.

---

### A5 · MEDIA — «Nadie sube el precio de un curso que no se llena» es una inferencia vendida como evidencia de demanda

**Afirmación literal (§0 y §6.2 nº 2):** «la propia Cámara **subió el precio** de 3.950 € a 4.300 €. **Nadie sube el precio de un curso que no se llena.** La demanda existe.»

**Problema.** Un cambio de precio entre dos ediciones no demuestra ocupación: puede responder a coste, a horas, a cambio de temario, a IPC o a reposicionamiento. Es el único dato que la síntesis aporta para afirmar que **existe demanda de pago solvente** —el resto del §0 demuestra lo contrario (la keyword del nombre no tiene ni dato)—, y aparece **dos veces** como argumento estructural.

**Gravedad: media.** El research prohíbe explícitamente «cifras con apariencia de estudio» de terceros (§1.1); esta es una inferencia propia con apariencia de prueba. Si entra al copy, es refutable.

**Fix.** Dejar el dato («3.950 € → 4.300 € entre ediciones, fuente oficial, consultado el 06-09-2026») y borrar la conclusión causal. Sustituirla por la evidencia que sí se tiene: seis canales propios y una lista de compradores que ya pagó por plantillas de cocina.

---

### A6 · ALTA — El «−20 °C / 7 días» vive en DOS productos vendidos, no en uno, y §14.4 sólo reporta uno

**Afirmación literal (§14.4):** tres defectos, y la cifra errónea de anisakis se atribuye **sólo** a `kit-tareas-marisqueria/03`: «Doble defecto: la norma derogada, **y la cifra**».

**Problema.** He re-escaneado los 438 xlsx. `kit-tareas-sushi-bar/03-seguridad-anisakis-appcc.xlsx` **también** publica el criterio estadounidense, y de forma más explícita y más operativa que marisquería:

> «El pescado debe congelarse a **-20 °C durante mínimo 7 días** o -35 °C durante 15 horas»
> «IMPORTANTE: Si la temperatura sube por encima de -18 °C durante la congelación, **reiniciar el conteo de 7 días**»

Lo verificado (CE-14 / MM-33, RD 1021/2022 art. 8.1 y Rgto. 853/2004 Anexo III Secc. VIII Cap. III.D) son **24 horas** a −20 °C. Un local que siga esa hoja inmoviliza el pescado **siete veces más tiempo del que la ley exige**, con el coste de cámara y de rotación que eso supone — y lo hace creyendo que cumple una norma que ni siquiera es la vigente («Normativa: RD 1420/2006»).

Además, en `kit-inventario/04-recepcion-mercancias.xlsx` la norma derogada **no está sólo en una nota**: aparece como **columna de fuente legal por familia de producto** («0 a 4 °C · **RD 3484/2000, art. 6**»), lo que la convierte en el respaldo aparente de cada umbral de la hoja.

**Gravedad: alta.** Es seguridad alimentaria en producto vendido, y el research lo reporta a la baja justo en la sección que existe para no heredarlo.

**Fix.** Corregir §14.4: **dos** productos con el parámetro de anisakis erróneo (sushi-bar y marisquería) y uno con el respaldo legal derogado por fila (inventario). Subir la pregunta 5 del §15.2 de «¿se corrigen?» a «se corrigen esta semana, aunque sea en sesión aparte»: es el único defecto del catálogo que puede acabar en una inspección.

---

### A7 · BAJA — «11 menciones en 8 ficheros» son 11 menciones en **10** ficheros

**Afirmación literal (§14.4 y verificación propia nº 4):** «Hay **11 menciones a normas derogadas en 8 ficheros**.»

**Problema.** Re-censado: 11 menciones, sí, pero repartidas en **10** ficheros (`pack-appcc/12`, `/13`, `/16`, `/17`, `/18`, `guia-restaurante-gastronomico/checklist-appcc`, `manual-manager-restaurante/calendario-cumplimiento-legal`, `kit-inventario/04`, `kit-tareas-sushi-bar/03`, `kit-tareas-marisqueria/03`). El 8 sale de contar 7 ficheros correctos + 3 defectuosos y olvidar que `pack-appcc/12` aporta dos menciones.

**Gravedad: baja**, pero es un recuento propio presentado como censo cerrado en un documento cuyo argumento central es que los demás no cuentan bien.

**Fix.** 11 menciones · 10 ficheros · 8 correctas · 3 defectos.

---

### A8 · BAJA — «20 fuentes» son 25 filas censadas

**Afirmación literal (§1 nº 1, §1.1, cap. 01):** «L2 comparó las **6 de 20 fuentes** que sí distinguen roles» · «JD descargable por rol de cocina: **0 de 20 fuentes**» · «ninguna de las **20 fuentes** que leyó L2».

**Problema.** El censo de L2 tiene **25 filas numeradas** (más 2 entradas sin numerar), de las que 2 fallaron por certificado caducado (`titulae.es`, `bartalentlab.com`). El denominador «20» es de L2 y la síntesis lo copia sin recontarlo — y va camino de la landing como prueba de exhaustividad.

**Gravedad: baja.**

**Fix.** «25 fuentes censadas, 23 legibles» y recalcular los ratios (6/23, 0/23, 2/23).

---

### A9 · BAJA — «Montarse el equivalente cuesta 45-55 €»: con los precios citados, el techo es 47,35 €

**Afirmación literal (§6.2 nº 3 y §10.2 nº 5):** «fichas técnicas 15 € + manual de un puesto 17,50 € + 2-3 hojas sueltas a 3-5 € = **45-55 €**… **Es el argumento comercial más limpio del research.**»

**Problema.** Con las piezas y precios que el propio censo verifica (15,00 + 17,50 + hojas de 2,95 y 4,95 €), el máximo alcanzable con tres hojas es **47,35 €**. El «55 €» —que es justo el número que hace que el argumento cierre «cuesta lo mismo que el manual entero»— no está soportado por ninguna cifra del censo.

**Gravedad: baja**, pero el argumento se va a copiar literalmente a la landing.

**Fix.** «45-47 €», o añadir al carrito las piezas que faltan y citarlas con su precio.

---

### A10 · BAJA — El recuento de la tabla de 16 conceptos no cuadra consigo mismo

**Afirmación literal (§1, cierre):** «13 sin cobertura gratuita decente y **en 6** lo gratuito afirma algo falso (nº **9, 10, 11, 12, 13, 14, 16** — siete si se cuenta el carné aparte)».

**Problema.** La lista entre paréntesis tiene **siete** elementos y el nº 16 **es** el carné, así que «siete si se cuenta el carné aparte» no significa nada: o son 6 (9-14) o son 7 (9-14 + 16). Esta tabla es el índice de criterio del manual y va al guion.

**Gravedad: baja.**

**Fix.** «13 sin cobertura decente y 7 donde lo gratuito afirma algo falso (9, 10, 11, 12, 13, 14 y 16)».

---

### A11 · BAJA — «Las microempresas quedan excluidas por completo» se lee como excluidas de la Ley, y es de un artículo

**Afirmación literal (CE-33, §2.1 y §1 nº ­—):** «Exentos del **plan** los establecimientos de hasta 1.300 m²… y las **microempresas quedan excluidas por completo** (art. 6.6).»

**Problema.** Verificado en el texto consolidado: el art. 6.6 dice «las microempresas quedan excluidas de las obligaciones a las que se refieren **los apartados anteriores del presente artículo**». Es exclusión del **artículo 6**, no de la ley: el **art. 8 (doggy bag universal, con su excepción de bufé y la obligación de informar en la carta) sigue obligando a toda empresa de hostelería, microempresa incluida**. El §14.2 sí acota bien el 1.300 m² («sólo del apartado 4») pero no acota el «por completo» de las microempresas, que es la lectura que el lector-microempresa se llevará.

**Gravedad: baja** (el §14.2 lo compensa parcialmente), pero es precisamente el tipo de matiz que justifica el precio.

**Fix.** «Las microempresas quedan excluidas de las obligaciones del art. 6 (plan y promoción de convenios). **El doggy bag del art. 8 les sigue obligando.**»

---

## B — NEGOCIO

### B1 · ALTA — El presupuesto no cierra, y la mitigación que propone el propio documento se queda en la mitad

**Afirmación literal (§15.3 y riesgo 12):** B1 **1,5-2 M** + B2 **5-6 M** + C **0,8-1 M**. «El techo de John es ~15 % de la cuota semanal y una semana normal debe quedarse **por debajo de 1,5 M**. **La fase B no cabe en una semana.** O se hacen B1 y B2 en **dos sesiones pares** distintas, o este manual ocupa **dos ciclos**.»

**Problema.** La aritmética no sostiene la mitigación. Sólo la fase B necesita **6,5-8 M**; a 1,5 M por sesión son **4,3-5,3 sesiones**, y con la fase C, **5-6**. «Dos sesiones» cubre 3 M: menos de la mitad. Y con la regla de sesiones alternadas (producto nuevo ↔ v2.0 pendiente), 5-6 sesiones de producto son **10-12 semanas naturales** — es decir, lanzamiento a mediados de noviembre, cuando el §13.1 ya está reservando el hueco de Resend para el **7-oct**. Las dos cosas no pueden ser verdad a la vez.

**Gravedad: alta.** Es la decisión que más le cuesta a John si se toma mal: o se rompe el techo de presupuesto que él mismo fijó el 29-ago, o se arranca un producto que se queda a medias en la tercera sesión (precedente ya vivido: la Guía Gastronómica v2.0, «a medio camino», tres documentos sin publicar).

**Fix.** Poner sobre la mesa **tres escenarios con su calendario real** antes de arrancar, no a mitad: (a) alcance completo, 5-6 sesiones, lanzamiento ~mediados de noviembre; (b) **alcance recortado** que sí quepa en 2-3 sesiones — 16 capítulos y 6 libros (fundiendo 4+5 y quitando el 7 al mínimo de comidas testigo, ver B4 y C2), ~4-4,5 M; (c) aplazarlo y ocupar el ciclo con un producto más barato. Y recalcular el slot del broadcast **después** de elegir, no antes.

---

### B2 · ALTA — Las 14 columnas de alérgenos duplican `pack-appcc/08` y ese par NO está en las seis reglas de no-solape

**Afirmación literal (§8.3, libro 3):** «14 columnas de alérgenos S/T/N» dentro de `ficha-tecnica-proceso.xlsx`, y §7.2 lista **seis** pares en riesgo — ninguno es éste.

**Problema.** `pack-appcc/08-matriz-alergenos.xlsx` (14 €) es exactamente «declaración de los 14 alérgenos **por plato** de la carta completa» (L6:38). La ficha de proceso vuelve a pedir los 14 por plato. **L6 sí había visto el problema y lo había resuelto** (`L6:127`): las 14 columnas «idénticas a `08-matriz-alergenos.xlsx`, **enlazadas** a esa matriz cuando el pack APPCC está en la misma carpeta, o repetidas manualmente si no». **La síntesis borró el matiz** y presenta las 14 columnas como contenido propio del libro 3, sin regla de no-solape.

Consecuencia práctica: el comprador que ya tiene el Pack APPCC —que es el segmento diana del broadcast, por definición— declara los alérgenos de cada plato **dos veces en dos ficheros que no se hablan**, y cuando cambia un ingrediente tiene dos sitios donde actualizarlo y uno donde olvidarse. Es el peor tipo de duplicación: la que genera una discrepancia con consecuencias sanitarias.

**Gravedad: alta.**

**Fix.** Séptima regla de no-solape, decidida en la SPEC y no por el constructor: la ficha de proceso lleva alérgenos **de proceso** (contacto y traza **en esta elaboración**, utensilio y superficie, sustitución posible) y **remite** a `08-matriz-alergenos` para la declaración de carta; o al revés. Nunca las dos declaraciones completas. Y en ningún caso enlazadas por fórmula entre ficheros (ver B3).

---

### B3 · ALTA — El enlace por fórmula entre libros rompe la promesa de la FAQ 10 y el propio pipeline

**Afirmación literal (§7.2 y §8.3, libro 3):** «coste por ración» y «food cost real» se **enlazan por fórmula externa** a `ficha-escandallo-base.xlsx`, con `IFERROR(…,"completa con tu escandallo")». Y **FAQ 10:** «¿Los Excel funcionan en Google Sheets y en Numbers? **Sí:** nuestras convenciones **prohíben `INDIRECT`, `COUNTA`, `PMT` y `OFFSET`** justamente por eso.»

**Problema.** Las referencias **entre libros distintos** no funcionan en Google Sheets (exigen `IMPORTRANGE` con autorización explícita), se rompen en cuanto el usuario mueve o renombra un fichero, y en Excel disparan el aviso de vínculos externos. Es decir: el libro 3 incumple la promesa de la FAQ 10 por una vía que la lista de funciones prohibidas no cubre — y esa promesa se está vendiendo como **argumento verificable frente al competidor directo** (§6.3 nº 3). Además rompe el paso de verificación de la familia: `inject_cache.py` + relectura `data_only` no puede resolver una fórmula que apunta a otro libro, así que el gate daría vacío o fallaría sin decir por qué.

Colateral del mismo diseño: la hoja «Índice de Fichas» del libro 3 pretende indexar hojas duplicadas por el usuario, cosa que **sólo se hace con `INDIRECT`**, que está prohibido. Si no se decide ahora, el constructor lo resolverá con `INDIRECT` o con un índice muerto.

**Gravedad: alta.** Contradice una promesa publicada en la FAQ, choca con la convención de familia y rompe un gate.

**Fix.** **Cero fórmulas entre ficheros en todo el paquete.** La ficha lleva una celda verde «coste por ración (cópialo de tu escandallo)» con nota y enlace de texto al Kit de Escandallos / Guía Food Cost; el `IFERROR` sobra porque no hay fórmula. El «Índice de Fichas» se declara **manual** en Instrucciones. Y se añade a las convenciones de familia: «prohibidas también las referencias externas entre libros».

---

### B4 · ALTA — El capítulo 19 y el 4 repiten, casi con la misma frase, un capítulo del Manual del Manager

**Afirmación literal (§7.1, fila «Servicio»):** el Manager cubre «Estándares de sala, reseñas, no-shows, hojas de reclamaciones» y el nuevo cubre «el cruce cocina↔sala↔dirección». Y **cap. 19:** «la comanda mal cantada y la alergia que no llega a cocina como **problema de sistema, no de personas**».

**Problema.** He abierto el guion del hermano. `guias-v2_0/guion_manual_manager_restaurante.py:1570` es el capítulo **«El Servicio: Estándares, Briefing y la Conversación Cocina-Sala»**, y entre sus epígrafes está literalmente **«Cocina y sala: un problema de sistema, no de personas»** y **«Corregir en el momento sin humillar a nadie»**, con el objetivo declarado de que el lector «deje de tratar el conflicto entre cocina y sala como un problema de caracteres». Es la **misma tesis y casi la misma frase** que el capítulo 19 del manual nuevo — y «corregir sin humillar» solapa además con el capítulo 04 («mandar sin gritar», «la conversación difícil»).

La tabla de frontera del §7.1 **no lo ve**: describe el capítulo de servicio del Manager como si fuera sólo sala, reseñas y no-shows.

**Gravedad: alta.** Es el riesgo nº 1 declarado por el propio research (confusión entre los dos manuales) materializándose en el contenido, no en el marketing. Un comprador de los dos, al mismo precio y a semanas de distancia, se encuentra el mismo capítulo escrito dos veces.

**Fix.** Releer el guion del hermano capítulo a capítulo **antes** de cerrar el índice —no la tabla de frontera de la síntesis, el guion— y reescribir el 19 para que sea lo que el Manager no tiene: **la matriz RACI de decisiones que cruzan** (autorizar un 86, aprobar una ficha nueva, compra fuera de escandallo, incidencia de alérgeno) y **cómo llevar la propuesta al gerente con la cifra de la semana**. El diagnóstico del conflicto cocina-sala se cita: «ya está en el Manual del Manager, cap. 18». Lo mismo con el 04: dejar la delegación por nivel del convenio (que es nuevo) y citar la conversación de corrección.

---

### B5 · MEDIA-ALTA — El capítulo 16 y tres de las cuatro hojas del libro 7 repiten el capítulo 19 del hermano

**Afirmación literal (§8.3, libro 7):** hojas `Registro de Comidas Testigo` · `Jerarquía de Prevención` · `Registro de Donaciones y Doggy Bag` · `Panel de Cumplimiento`. Y §8.3 lo admite: «su libro 7 era sólo el plan de desperdicio, **la pieza más floja de las 8** (el Manager ya explica la Ley 1/2025 en texto y **la mayoría de compradores están exentos** del plan)».

**Problema.** La SPEC del hermano (`manual-manager-SPEC.md`, D8 y §4 cap. 19) ya cubre: jerarquía de la Ley 1/2025, doggy bag desde el 22-12-2022 con la excepción del bufé, exención de 1.300 m² «bien acotada» con tabla «de qué estás exento / de qué no». El capítulo 16 nuevo vuelve a explicar los seis niveles de la jerarquía, el doggy bag, el convenio de donación y la exención — y el libro 7 les pone tres hojas. Lo **genuinamente nuevo y diferencial es CE-11 (comidas testigo)**, que es media hoja de las cuatro. El propio documento diagnostica la debilidad y, en vez de recortar, añade.

**Gravedad: media-alta.** Es duplicación reconocida y mantenida, y consume presupuesto que B1 no tiene.

**Fix.** Libro 7 = **`Registro de Comidas Testigo` + `Producción y Ficha de Banquete`** (que es lo que el chef de eventos sí abre, y hoy no existe en ningún sitio). El desperdicio pasa a **una tabla de una página** en el capítulo 16 que cita el capítulo del Manager y sólo añade lo que es de cocina (qué excedente es donable desde una cocina caliente y qué no). Ahorro estimado: una hoja de libro y ~1.500 palabras.

---

### B6 · MEDIA — Se decide el tercer producto de 55 € sin un solo dato de venta de los dos primeros

**Afirmación literal (§10.2 nº 1):** «John ya decidió el escalón de esta línea, **hace dos días**. La línea "Manuales operativos" **nació a 55 €**.»

**Problema.** El Manual del Manager está LIVE desde el **5-sep** (ayer) y la Guía Food Cost desde el **3-4 sep**. La recomendación de precio, el bundle y el alcance se apoyan en una «paridad de línea» fijada hace 48 horas sobre un producto del que no hay **ninguna** cifra de conversión. El documento tampoco aporta el dato que sí podría tener: cuántos compradores hay en los segmentos de Resend a los que va dirigido el broadcast, ni qué conversión dio el broadcast del Manual del Manager (programado para el 7-sep, según la memoria del proyecto).

**Gravedad: media.** No invalida la propuesta, pero es información barata que cambia dos decisiones (precio y alcance) y que se está omitiendo justo antes de comprometer 7-9 M de tokens.

**Fix.** Antes de la SPEC: ventas de `guia-food-cost-ingenieria-menu` y `manual-manager-restaurante` a 7 días, y tamaño real de los segmentos de compradores de cocina en Resend. Si el escalón de 55 € no convierte, la conversación es otra (45 € y alcance recortado, o pausar la línea).

---

### B7 · MEDIA — El bundle se propone como «el argumento comercial más fuerte» sin una línea de presupuesto

**Afirmación literal (§10.2 nº 2 y §15.2 nº 2):** «El bundle sólo funciona con paridad, y es **el argumento comercial más fuerte** que sale del research» · «¿Se crea un bundle Manager + Chef Ejecutivo?».

**Problema.** En esta arquitectura un bundle **es un producto más**: entrada en `products-catalog.ts`, Payment Link propio y su env var, landing, par `-access`/`-library`, mapeo en `get-download-urls.ts`, validación producto↔sesión, regla de `robots.txt` y su fila en el gate LIVE. Nada de eso está en el §15.3, que sólo presupuesta la capa de producto del manual (0,8-1 M). Se le está pidiendo a John que decida sobre algo cuyo coste nadie ha estimado, en la misma sesión en la que se le dice que el presupuesto no cabe (B1).

**Gravedad: media.**

**Fix.** O se cuantifica (estimo +0,3-0,4 M y una decisión sobre qué pasa con quien ya compró uno de los dos), o se sustituye por la versión sin ingeniería: **cupón de descuento cruzado en el email post-compra y en la landing de cada uno**, que consigue el 80 % del efecto con cero producto nuevo.

---

### B8 · MEDIA — El capítulo 9 comete exactamente el error que el manual denuncia en el capítulo 9

**Afirmación literal (§1 nº 6 y §1.1):** se acusa a Barcelona Culinary Hub y a ingenieriademenu de vender «KPIs de sala como KPIs de cocina» y de publicar «rangos **sin fuente**». Y **cap. 09:** «Los **siete que sí**: merma por partida, tiempo de pase, incidencias de alérgenos, horas de cocina por cubierto, cumplimiento de ficha, retrabajos/devoluciones, rotación de brigada».

**Problema.** Esos siete no tienen **ninguna** fuente. Y el §4.2 lo confirma sin rodeos: **tiempo de pase, coste de un brote y horas de formación de cocina «SIN FUENTE, confirmado»**, ninguna cifra de merma es fiable, y el propio §1 nº 6 dice que de los ~30 KPIs del mercado sólo food cost y margen bruto por plato son de cocina — **los dos únicos que el libro 1 excluye a propósito** («cero columnas financieras»). Resultado: el cuadro de mando estrella tiene siete indicadores sin un solo valor de referencia contra el que compararse, presentados con la autoridad de «los que sí son de cocina».

**Gravedad: media.** No es un error de dato, es un error de encuadre — y es el que un lector escéptico usará para escribir la reseña de 2★ que el riesgo 11 teme.

**Fix.** Encuadrarlos **explícitamente como propuesta de la casa**: «no existe un estándar publicado de KPIs de cocina en español; ésta es nuestra lista, y aquí está por qué cada uno y qué error típico tiene». El libro 1 **exige** que el usuario fije su propio objetivo antes de encender el semáforo (celda verde obligatoria, semáforo en gris mientras esté vacía). Eso convierte la ausencia de benchmark en el argumento, que es lo que el §4.2 ya recomienda para las mermas.

---

### B9 · MEDIA — La hoja `Estado Normativo` que sostiene la promesa de actualizaciones no existe en ninguno de los 8 libros

**Afirmación literal (§2.5):** «hoja **`Estado Normativo`** con fecha de corte y URL editables» como mecanismo de gestión de la caducidad. Y **FAQ 11:** «hay una hoja `Estado Normativo` con fecha de corte y URL».

**Problema.** Ninguno de los 8 libros del §8.3 la incluye. Sus hojas son: Instrucciones/Parámetros/Semana/KPI (1) · Instrucciones/Previsión/Producción/Lista/Ajuste (2) · Instrucciones/Ficha/Ejemplo/Índice (3) · Instrucciones/Organigrama/Fichas de Puesto/RACI (4) · Instrucciones/Rúbrica/Prueba/PDI/Histórico (5) · Instrucciones/Calendario/Pruebas/Pase (6) · Instrucciones/Testigo/Jerarquía/Donaciones/Panel (7) · Instrucciones/Auditoría/Resumen/Histórico (8). En el hermano esa hoja vivía en `calendario-cumplimiento-legal.xlsx`, que aquí **no se construye** (correctamente, es cross-sell). La promesa se quedó sin casa al hacer el trasvase.

**Gravedad: media.** Es una promesa que va a la FAQ pública y al email.

**Fix.** Asignarla explícitamente. Candidato natural: **libro 8 (auditoría)**, que ya es el que concentra la PRL sembrada con norma y URL; o libro 7. Y si se decide no construirla, quitarla del §2.5 y reescribir la FAQ 11.

---

### B10 · MEDIA — El capítulo 10 pisa el eje de rendimiento de la Guía Food Cost, y ese par tampoco está en las seis reglas

**Afirmación literal (§7.2):** las seis reglas nombran `05-control-mermas.xlsx` (Kit de Inventario, 14 €) como el par en riesgo de mermas.

**Problema.** El par caro es otro. `guia-food-cost-ingenieria-menu/rendimiento-mermas-producto.xlsx` (**55 €, el mismo precio**) tiene, según L6:62, «Test de Rendimiento (bruto→limpio, subproductos, coste neto), **Merma de Cocción** (crudo→cocinado, sobrecoste) y **Mi Tabla de Mermas** (mermas de referencia por categoría, editable)». El capítulo 10 se titula «**Mermas y rendimiento**». Se cita la Guía Food Cost como cross-sell en el §7.3, pero **no hay regla de no-solape escrita** para este par, que es el que un comprador de los dos productos de 55 € va a notar.

**Gravedad: media.**

**Fix.** Regla explícita: este manual mide **merma agregada por partida contra la producción del día** y no calcula rendimiento de ingrediente ni merma de cocción — eso se cita («ver Guía Food Cost, `rendimiento-mermas-producto.xlsx`»). El capítulo 10 se retitula para que la frontera esté en el índice: «**La merma de tu partida** (el rendimiento del ingrediente vive en la Guía Food Cost)».

---

### B11 · MEDIA — El vocabulario LATAM se fija y luego se contradice dentro del propio paquete

**Afirmación literal (§5.3):** «La sección: **Partida (estación)**. "Estación" se entiende en toda Hispanoamérica».

**Problema.** El paquete usa los dos términos como si nombraran cosas distintas y sin criterio: el libro 1 mide «merma por cada una de las **6 partidas**», el libro 5 tiene una columna «próxima **estación** a aprender» dentro de un libro que evalúa partidas, y el hermano mide «cobertura por **estación**» sobre **las mismas 6 unidades** de La Encina (`matriz-formacion-polivalencia.xlsx`, 12 × 6). Un comprador de los dos manuales tiene dos nombres para la misma cosa, en dos ficheros que el §7.2 quiere que se remitan el uno al otro.

**Gravedad: media** — es pequeño en apariencia y es exactamente lo que rompe la sensación de sistema, que es lo que se está vendiendo.

**Fix.** Un solo término en herramientas y encabezados: **partida**, con «(estación)» sólo en la primera mención de cada libro y en el glosario. En el libro 5, «próxima **partida** a aprender», con nota: «equivale a la columna "estación" de la matriz de polivalencia del Manual del Manager».

---

### B12 · BAJA — «Checklists», la única promesa del hub que no tiene entregable propio

**Afirmación literal (§9, cobertura):** «checklists (8, 12, 17 **+ el libro 8**)», contra la promesa publicada desde mayo: «Responsabilidades, KPIs, protocolos, **checklists** y evaluación de equipo de cocina».

**Problema.** El libro 8 es una **auditoría puntuada** (`SUMPRODUCT(peso;puntuación)`), no un checklist; los capítulos 8, 12 y 17 son texto. El checklist diario de cocina del catálogo es `kit-tareas/02-partidas-cocina.xlsx`, que se cita como cross-sell. Es decir: de las cinco palabras de la promesa del hub, cuatro tienen entregable y una remite a un producto de 12 €.

**Gravedad: baja**, pero la tarjeta lleva tres meses vencida prometiendo esas cinco cosas.

**Fix.** Elegir una de dos: presentar la **`Lista de Producción Diaria` imprimible** del libro 2 como el checklist del manual (lo es, y además es el único que dice **cuánto**), o reescribir la descripción de la tarjeta al retirar el `comingSoon`, que hay que tocar de todos modos (D18).

---

## C — PRODUCTO

### C1 · ALTA — El índice sirve al jefe de cocina de 8 personas; al chef ejecutivo de 4 outlets le da 1 capítulo de 20 y 0 herramientas de 8

**Afirmación literal (§5.4 nº 3 y §6.2 nº 5):** el chef corporativo/multi-outlet es «**el persona con más evidencia primaria** del research y el único documentado en tres mercados», y «**no tiene NINGÚN producto dedicado**: todo el censo está escrito desde la cocina única».

**Problema.** Ese es el hueco de mercado más limpio que encuentra el research — y el reparto de entregables lo ignora. Le tocan **el capítulo 20** (y media parte del 2 y del 3), y **ninguno de los 8 libros consolida más de una unidad**: el libro 1 son 52 semanas × 6 partidas de **un** local; el 8 es la auditoría de **una** cocina; el 5 evalúa **una** brigada. Un chef de 15 hoteles (Castañeda) o de 4 outlets acaba con cuatro copias del mismo fichero y **sin nada que le diga qué unidad va peor**, que es literalmente su trabajo («ver una panorámica completa de cada hotel y de la marca»). La respuesta de la FAQ 4 —«sí, y es donde más aporta»— no está sostenida por los entregables.

**Gravedad: alta.** Es el argumento de diferenciación más fuerte del research y el que no está en el producto. Y es lo que separa este manual de «el Manual del Manager pero de cocina».

**Fix.** Dos hojas, no un libro nuevo: `Comparativa entre Unidades` en el **libro 1** (los mismos KPIs, 6 columnas de outlet, desviación contra el estándar del grupo y ranking) e `Histórico por Unidad` en el **libro 8** (la misma auditoría puntuada, comparable entre cocinas). Coste marginal bajo, porque el motor y las fórmulas ya están. Y decidir en la SPEC, en una línea, si el manual es «una cocina con un capítulo multi-outlet» o «varias cocinas»: hoy el copy dice lo segundo y el producto es lo primero.

---

### C2 · MEDIA — De los 8 libros, sólo 3 se abren cada semana; cuatro se abren una vez

**Problema.** Cadencia realista de uso, libro a libro:

| Libro | Cuándo se abre de verdad |
|---|---|
| 1 · cuadro de mando de cocina | **Semanal** — es el ancla |
| 2 · planificación de producción | **Diaria/semanal** — es el que justifica el producto |
| 3 · ficha técnica de proceso | Cada vez que nace o cambia un plato (**mensual**) |
| 8 · auditoría interna de cocina | Mensual/trimestral |
| 6 · desarrollo de carta | 2-4 veces al año |
| 5 · evaluación técnica | 1-2 veces al año |
| 4 · organigrama, fichas de puesto y RACI | **Una vez**, y luego cuando entra alguien |
| 7 · banquetes y desperdicio | **Nunca**, en un restaurante de carta sin eventos — que es el comprador mayoritario del hub |

Cuatro de ocho son de consulta única. No es un defecto en sí (una ficha de puesto **debe** rellenarse una vez), pero el paquete se vende como «8 libros con fórmulas vivas» y el §8.3 los presenta todos con el mismo peso.

**Gravedad: media.** Afecta a la percepción de valor y, sobre todo, al presupuesto de B1: fundir dos libros libera ~0,3-0,4 M sin quitar contenido.

**Fix.** (a) El mapa «problema → capítulo → herramienta» del capítulo 01 declara **la cadencia de cada libro** («semanal / al abrir temporada / una vez / sólo si haces eventos»): es honesto y además enseña a usarlos. (b) Evaluar fundir **4 y 5** en un `personas-y-puestos-cocina.xlsx` (organigrama + ficha de puesto + rúbrica + PDI + histórico): giran los dos alrededor de la persona y su puesto, y bajaría el paquete a 7 libros, igual que el hermano.

---

### C3 · MEDIA — Faltan las dos cosas que más se rompen un martes: el frío que se cae y el plato que viaja

**Problema.** Ni los 20 capítulos ni las 12 situaciones cubren:

1. **Se cae el frío.** La cámara sube a 12 °C de madrugada, o el abatidor muere en pleno servicio. Es la incidencia más frecuente y más cara de una cocina, y **tiene norma verificada detrás**: qué se tira y qué no según CE-10, las tres fechas de la etiqueta si se recongela algo (CE-13), qué se apunta para que la inspección no lo lea como un incumplimiento (CE-16), y el aviso al seguro. Hoy el bonus tiene «un cocinero se corta con la cortadora» (situación 9) pero nada de esto.
2. **El plato que viaja.** Delivery y take-away desde la cocina: mantenimiento **≥63 °C** (art. 30.2, que además falta en el research — ver A3), envase apto, tiempo de reparto, qué platos **no** salen y hasta dónde llega tu responsabilidad. Estamos en 2026, el catálogo tiene una **Guía Dark Kitchen (24 €)** y este manual no menciona el canal ni una vez.

**Gravedad: media.** Las dos son diarias, las dos tienen norma española verificable y las dos son justo lo que separa «criterio» de «temario».

**Fix.** Sustituir dos situaciones del bonus por «**se cae la cámara un domingo por la noche**» y «**el plato que sale por la puerta**», o abrir dos epígrafes en los capítulos 13 y 8. Ninguna de las dos añade libro.

---

### C4 · MEDIA — La escala que promete la FAQ no está en las herramientas

**Afirmación literal (FAQ 3, FAQ 5 y objeción 2):** «cada capítulo trae **un ejemplo por escala** (4-6 / 15-25 / 100+)».

**Problema.** Los ocho libros se siembran desde el mismo `datos_ejemplo.py`, que **importa** el de La Encina: 12 personas, 6 partidas (§7.4). La cocina de 4-6 personas —la que más objeciones plantea, la que no tiene ni un testimonio en L5 y a la que la FAQ 3 le dice que sí— abre el libro 1 y ve seis partidas que no tiene, y el libro 5 le pide una rúbrica por partida para una brigada de cuatro. La escala existe en el texto y no en la herramienta, que es donde el comprador la vive.

**Gravedad: media.**

**Fix.** Celda de `Parámetros` «número de partidas activas (3-8)» que gobierne encabezados y filas en los libros 1, 2 y 5 (sin `INDIRECT`: columnas fijas con encabezado enlazado y filas vacías que el semáforo ignora por `ISNUMBER`), más un segundo juego de datos de ejemplo de **5 personas / 3 partidas** en esos tres libros. Es barato y responde a la objeción medida.

---

### C5 · MEDIA — El comprador de los dos manuales teclea los mismos datos dos veces

**Problema.** Las reglas del §7.2 evitan repetir **columnas**; no evitan repetir **trabajo de entrada**. El cuadro semanal del Manager y el cuadro de cocina comparten cadencia (52 filas ISO) y al menos un input (**cubiertos servidos**, que está en los dos). La matriz de polivalencia y la rúbrica técnica comparten **las mismas 12 personas y las mismas 6 unidades**. El bundle de §10.2 se vende como «los dos lados de la dirección»; si al abrirlos el usuario descubre que son dos ficheros paralelos que no se hablan y que le piden dos veces lo mismo, el bundle se convierte en la queja.

**Gravedad: media.** Es la diferencia entre «dos productos» y «un sistema», que es justo lo que justifica comprar los dos.

**Fix.** Una hoja `Parámetros` con **contrato documentado** entre los dos manuales: mismos nombres de persona, mismos nombres de partida/estación, mismo criterio de semana ISO; y en Instrucciones, una tabla de tres filas de «qué se copia de dónde, y qué NO hay que volver a teclear». Sin fórmulas entre ficheros (B3): copia declarada, no vínculo.

---

## LO QUE FALTA para que John pueda decidir con seguridad

1. **Los tres escenarios de presupuesto con su calendario real** (B1): alcance completo 5-6 sesiones, alcance recortado 2-3 sesiones (16 capítulos / 6-7 libros), o aplazar. Hoy se le pide que decida «¿se parte la fase B en dos sesiones?» sobre una aritmética que no cierra.
2. **Las ventas reales de los dos productos de 55 €** a 7 días (Guía Food Cost, Manual del Manager) y **el tamaño de los segmentos de compradores de cocina en Resend** (B6). Es el dato que decide precio y alcance, cuesta dos consultas y no está en el documento.
3. **La tabla de frontera reconstruida leyendo el guion del hermano, capítulo a capítulo** (B4), no la síntesis. Con el resultado, el índice de 20 capítulos revisado: hoy sé de dos solapes (19 y 4) y no puedo garantizar que sean los únicos.
4. **La decisión sobre multi-outlet** (C1): ¿es este manual «una cocina con un capítulo de varias» o «varias cocinas»? De la respuesta dependen dos hojas nuevas, el copy del hero y qué buyer persona lidera la landing.
5. **La corrección de los defectos de seguridad alimentaria del catálogo** (A6): dos productos con «−20 °C / 7 días» y uno con el RD 3484/2000 como respaldo legal por fila. Es lo único de esta lista que ya está cobrando dinero a clientes.
6. **El coste del bundle** (B7), o su sustitución por un cupón cruzado.
7. **La verificación pendiente que la propia síntesis declara** y que sigue abierta: nadie ha abierto con sus manos el **BOE-A-2026-18630** ni el **BOE-A-2023-6344** (§16). Los capítulos 2 y 3 —funciones literales del art. 17 y movilidad funcional del art. 19— se apoyan íntegramente en L4. Con el precedente de A1 (una tabla de L4 mal comparada), el verificador legal debe abrirlos **antes** del guion, no después.
8. **El grupo de ids**: `CE-*` normativa / `CS-*` sector está bien resuelto en §15.2 nº 10, pero conviene fijarlo **antes** de tocar `guias-v2-research-sector.json` — hoy tiene 162 entradas y ningún `CE-*`, así que la ventana está abierta y se cierra en cuanto alguien fusione.
9. **Los 5-10 minutos de voz de John** sobre los cinco dolores sin cita (§15.2 nº 7). Es la única laguna del research que no se puede cerrar con más búsqueda, y afecta a los capítulos 5, 6, 7, 8 y 13 — el corazón del producto.

---

**Nota de método.** Lo que se ha comprobado con fuente primaria en esta refutación: art. 30 completo del RD 1086/2020 y art. 6, 7 y 8 de la Ley 1/2025 (PDF consolidados del BOE, extraídos con PyMuPDF); Anexo III del RD 486/1997 (BOE); las cinco filas salariales recalculadas; los 438 xlsx del catálogo re-escaneados; `products-catalog.ts`, `use-cases-content.es.ts`, `robots.txt`, los dos ficheros del hub y `guion_manual_manager_restaurante.py` leídos en el repositorio. Lo que **no** se ha re-verificado: los precios de cursos y SaaS de L1, los volúmenes de DataForSEO, las 17 ofertas de empleo de L4 y las citas de L5.

**Via: Claude Code**
