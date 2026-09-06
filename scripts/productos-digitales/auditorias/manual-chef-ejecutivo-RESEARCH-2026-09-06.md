# RESEARCH CONSOLIDADO — «Manual del Chef Ejecutivo»
## Producto digital NUEVO nº 3 · AI Chef Pro · línea «Manuales operativos» (hermano del Manual del Manager)

**Fecha:** 2026-09-06 · **Estado:** research cerrado, PENDIENTE DEL OK DE JOHN antes de escribir una sola línea de producto.
**Fuentes:** las seis lentes de este mismo directorio (`manual-chef-ejecutivo-research-L1-competencia.md`, `-L2-serp.md`, `-L3-normativa.md`, `-L4-laboral-datos.md`, `-L5-cliente.md`, `-L6-assets.md`), leídas enteras, más verificación directa contra el repo y contra los PDF publicados (`src/data/products-catalog.ts`, `src/data/use-cases-content.es.ts`, `astro-site/public/robots.txt`, `astro-site/public/dl/**`, `scripts/productos-digitales/manual-manager-SPEC.md`, `guion_manual_manager_restaurante.py`, `auditorias/guias-v2-research-sector.json`, `CALENDARIO-V2-SEMANAL.md`) y una consulta **en vivo a GSC** (`sc-domain:aichef.pro`, 2026-06-08 → 2026-09-05).
**Regla aplicada:** cada cifra lleva fuente y fecha, o va marcada **«sin fuente»**. Nada inventado. Este documento es research y propuesta: **no contiene contenido de producto**.

> ### Nueve verificaciones propias — dos de ellas corrigen a las lentes (detalle en §16)
>
> 1. ❌ **CORRECCIÓN A L6: las cuatro páginas de rol NO tienen `productIds` vacío.** L6 §(e) afirma que `chef-ejecutivo`, `chef-cocina`, `chef-catering` y `fb-manager-hotel` están a cero. Medido con regex sobre `src/data/use-cases-content.es.ts`: **las cuatro traen 6 productos cada una** (líneas 377, 491, 712 y 1484). **El hueco real es otro y es más grande:** de las 20 páginas de rol, **ninguna enlaza a un producto de más de 45 €** — `manual-manager-restaurante` aparece **0 veces** y `guia-food-cost-ingenieria-menu` **0 veces** en todo el fichero. Las páginas de rol venden kits de 9-18 € y nada más.
> 2. ✅ **Calibración de páginas MEDIDA con PyMuPDF sobre los PDF que hoy se venden** (no estimada): manual del Manager **77 págs / 41.235 palabras = 536 pal/pág** · Guía Food Cost **95 págs / 50.265 palabras = 529 pal/pág** · bonus del Manager **28 págs / 11.530 palabras = 412 pal/pág** · bonus de la Guía **32 págs / 12.986 palabras = 406 pal/pág**. **El cuerpo calibra a ~530 y el BONUS a ~410**, no a 530: el §8.1 de la síntesis del Manager presupuestó el bonus en 7.500 palabras y salieron 11.530. Es el dato que dimensiona la promesa de este manual (§8).
> 3. 🔴 **Colisión de identificadores entre L3 y L4.** Las dos lentes usan el prefijo **`CE-`** con numeración solapada: L3 emite `CE-01..CE-40` (normativa) y L4 emite `CE-01..CE-23` (datos del sector). `CE-01` es «alérgenos, Rgto. 852/2004 Anexo II Cap. IX» en una y «índice de incidencia INSST CNAE 56» en la otra. Verificado que `guias-v2-research-sector.json` tiene **162 entradas** y **ningún** `CE-*` (prefijos vivos: MICH, REPS, TURG, SECT, TICK, SMI, CONV, TRAM, ANIS, JORN, FC 36, MM 59), así que el prefijo está libre — **pero hay que renombrar uno de los dos bloques antes de fusionar o se pisan 23 ids.** Propuesta en §15.
> 4. 🔴 **Censo NUEVO que cierra un hueco declarado por L6: 438 xlsx del catálogo escaneados** (`sharedStrings.xml` + hojas, un zip cada uno). Hay **11 menciones a normas derogadas en 8 ficheros**. **Ocho son correctas** (dicen literalmente «que derogó el RD…»). **Tres son defectos reales**, y sólo uno lo había visto L6 (§14.4).
> 5. ✅ **`robots.txt` no necesita nada.** `Disallow: /manual-*-access` y `/manual-*-library` están en los **5 bloques de user-agent** (líneas 39-40, 57-58, 75-76, 93-94, 111-112), con el comentario de cabecera que documenta el prefijo. Confirmo a L6.
> 6. ✅ **Catálogo: 46 productos** (`products-catalog.ts`), `zona-app.ts` con 47 entradas. Éste sería el **47** del catálogo. Escalera medida y contada en §10.1.
> 7. ✅ **El `comingSoon` existe en los DOS ficheros del hub** con `phase: 'Junio 2026'` — `ProductosDigitales.tsx:927` y `ProductosDigitalesHubPage.astro:942`, con la descripción literal «Responsabilidades, KPIs, protocolos, checklists y evaluación de equipo de cocina». **Está vencido tres meses.**
> 8. ✅ **GSC en vivo (90 días) confirma el brief y añade algo que no estaba:** cero consultas de puesto; **todas las consultas con «chef» son de marca** (`ai chef pro` 555 impr./pos. 1,0 · `ai chef` 3.249/5,3 · `chef gpt` 3.210/6,4). Pero el **glosario técnico de cocina sí posiciona**: `5 salsas madre de la cocina` pos. **5,0** · `que es un fondo blanco en cocina` **7,0** · `tipos de mermas en cocina` **7,0** · `mise en place cocina` **9,7** · `que es un roux en cocina` **10,9**. Y `cocina molecular` acumula **339 impresiones** en posición 49,8. Es la puerta de entrada real (§13).
> 9. ✅ **Los 13 posts del contexto existen y los 13 llevan sus 3 banners.** Extraídos los productos de cada banner, lo que da la lista exacta de candidatos a sustitución quirúrgica (§13.2). Y el agente **«Chef Ejecutivo Pro»** existe en el catálogo de la plataforma en ES y como **«Executive Chef Pro»** en EN.

---

## 0. Lo primero: qué demanda hay de verdad y por dónde entra el dinero

**Hay más volumen que en los dos productos anteriores, y sigue estando donde no se puede vender.** Volúmenes de DataForSEO (Google Ads, búsquedas/mes, medidos el 2026-09-06 y entregados en el encargo):

| Keyword | ES | MX | CO | AR | CL | PE |
|---|---|---|---|---|---|---|
| **sous chef** | **1.000** | **2.900** | 720 | 720 | 720 | 480 |
| **jefe de cocina** | 320 | 320 | 140 | 110 | 110 | 170 |
| **brigada de cocina** | 320 | **880** | 260 | 260 | 140 | 210 |
| **chef ejecutivo** | 260 | **1.300** | 170 | 110 | 260 | 170 |
| funciones del jefe de cocina | 110 | 70 | 70 | 20 | 10 | 40 |
| ficha técnica de cocina | 90 | 30 | 20 | 10 | 50 | 30 |
| head chef | 90 | — | — | — | — | — |
| **organigrama de cocina** | 50 | **590** | 40 | 30 | 40 | 50 |
| receta estándar | sin dato | 140 | 30 | 10 | 10 | 10 |
| funciones del chef ejecutivo | 10-20 | 10-20 | 10-20 | 10-20 | 10-20 | 10-20 |
| manual de cocina profesional · manual de procedimientos de cocina · manual del chef · estandarización de recetas · control de calidad en cocina · checklist cocina restaurante | **0-10** | — | — | — | — | — |
| **manual del chef ejecutivo** · gestión de cocina · kpi cocina · evaluación de desempeño cocina · manual de operaciones de cocina · protocolos de cocina restaurante · planificación de producción en cocina | **SIN DATO** | — | — | — | — | — |

Competencia **LOW en todo**. Cinco lecturas, y ninguna es cómoda:

1. **La keyword con más volumen del bloque (`sous chef`, 1.000/mes en España) no es de este producto.** Es intención de **empleo y de carrera**. L2 midió la SERP: InfoJobs con secciones dedicadas por ciudad, LinkedIn, Hosco, Turijobs, Indeed. Igual que «gerente de restaurante» era 89 % empleo para el hermano, aquí el patrón se repite y además está **partido en dos**: lo que no captura el empleo lo captura la **formación reglada de pago** (CIB, CETT, Cámara de Madrid, ESAH, Gasma, Barcelona Culinary Hub).
2. **El nº 1 de la SERP española de «chef ejecutivo» es un competidor con el mismo nombre que nuestro slug.** `chefejecutivo.com` (Jorge Blasco, consultoría + curso de 40 módulos con «acceso de por vida»). No publica precio. No es un impedimento técnico —el slug es nuestro dominio— pero hay que saberlo antes de escribir copy que compita en esa cadena.
3. **La intención de GESTIÓN vale literalmente cero.** «manual de operaciones de cocina», «kpi cocina», «evaluación de desempeño cocina», «planificación de producción en cocina», «gestión de cocina»: **sin dato**. Y las que sí se miden («manual de cocina profesional», «estandarización de recetas», «control de calidad en cocina») están en **0-10**. Esto es peor que en el Manual del Manager, donde al menos «manual de operaciones de un restaurante» daba 10/mes con SERP 100 % limpia.
4. **El volumen real de la familia está en LATAM y es de definición, no de compra.** «chef ejecutivo» 1.300 en México frente a 260 en España; «organigrama de cocina» 590 frente a 50; «brigada de cocina» 880 frente a 320. Son consultas de *qué es / quién manda*, servibles con contenido, no con una landing de 55 €.
5. **Y la trampa del sufijo, otra vez.** «ficha técnica de cocina» = 90; «receta estándar» en España = sin dato (140 en México). La gente busca el concepto y filtra sola. Señal de contenido, no de landing. Mismo patrón que «chile crisp» (2026-08-02) y que «cuadrante de turnos restaurante» (2026-09-04).

**Lo que sí prueba que existe comprador:** el mercado paga **695 € a 9.075 €** por exactamente este temario (§6). El Diploma Chef Ejecutivo del CIB cuesta **7.714-9.075 €**, el DSU del CETT **5.152,50-6.222,50 €**, el Curso Superior de la Cámara de Madrid **4.300 €** — y la propia Cámara **subió el precio** de 3.950 € (edición anterior) a 4.300 € (2026-2027). Nadie sube el precio de un curso que no se llena. La demanda existe; lo que no existe es la búsqueda de un documento.

### Por dónde entra el dinero: seis canales, todos nuestros

| Canal | Estado real hoy (verificado por mí) | Qué hay que hacer |
|---|---|---|
| **El producto está ANUNCIADO en el hub desde mayo, y vencido** | `ProductosDigitales.tsx:927` y `ProductosDigitalesHubPage.astro:942`, `phase: 'Junio 2026'`, descripción «Responsabilidades, KPIs, protocolos, checklists y evaluación de equipo de cocina» | Retirar la entrada de `comingSoon` **en los dos ficheros** al publicar (D18 del Manager) y poner la tarjeta real con badge «Nuevo» |
| **Banners en el blog ES** | 325/325 posts con 3 banners y 46 productos en rotación (`fase8e-banners-corpus.py`, 2026-08-31) | Producto **47** al catálogo → entra en la rotación. Además, **sustitución quirúrgica** en 5 posts de cocina (§13.2) |
| **13 posts propios de cocina, todos vivos y con sus 3 banners** | Verificado fichero a fichero. El más on-topic: `libreria-de-prompts-para-chef-ejecutivo-pro-ai` (hoy con banners de escandallos, gestión de personal e inventario) | Banner fijado en 5 + enlace contextual en el resto |
| **5 páginas `/usos/rol/…` del público exacto** | `chef-ejecutivo-corporativo` (89 impresiones, todas de marca), `chef-jefe-cocina` ⚠️ (el slug real, **no** `chef-cocina`), `sous-chef`, `chef-catering`, `fb-manager-hotel`. **Las 5 tienen 6 productos… y ninguno cuesta más de 45 €** | Enlace **bidireccional** + añadir el manual (y de paso el del Manager y la Guía Food Cost) a sus `productIds` |
| **Lista de compradores (Resend)** | Pack APPCC (14 €), Kit de Escandallos (12 €), Kit de Tareas (12 €), Kit de Inventario (14 €), Guía Food Cost (55 €), Manual del Manager (55 €, LIVE desde el 5-sep) | Es el público exacto: ya pagó por las plantillas de cocina y este manual es el criterio que falta. Broadcast propio (regla de John del 5-sep, cola de 5 días) |
| **Plataforma (Pickaxe)** | Agente **«Chef Ejecutivo Pro»** vivo en ES (y «Executive Chef Pro» en EN), con su librería de prompts publicada en el blog | Mención desde el agente y desde la librería |

**Conclusión del bloque, sin adornos:** este producto **no se lanza por volumen de búsqueda**. La keyword del nombre no tiene ni dato, la del puesto es empleo y la de gestión vale cero. Se lanza porque (a) el hueco de pago está medido producto a producto y es un desierto (§6), (b) el temario se vende hoy a 695-9.075 € en formato que caduca, (c) tenemos seis canales propios y una base de compradores de cocina, y (d) **lleva anunciado desde mayo con fecha de junio**. **La landing no va a captar por búsqueda y no se debe prometer que lo haga.**

---

## 1. Los conceptos que el manual DEBE fijar (y que la SERP mezcla)

Es el equivalente a las 18 distinciones del Manual del Manager. Aquí son **16**, y el reparto es peor para lo gratuito: **13 no las cubre bien nadie en español** y en **6** lo gratuito afirma algo **falso**.

| # | Concepto | Qué es exactamente | Con qué se confunde | ¿Lo cubre bien la SERP gratuita? |
|---|---|---|---|---|
| 1 | **Chef ejecutivo vs jefe de cocina vs chef corporativo vs sous chef vs jefe de partida** | El ALEH VI lo resuelve por escrito: área funcional **2.ª (Cocina y Economato)**, con Jefe/a de cocina, 2.º jefe/a y Jefe/a de catering en el **grupo 1.º**; jefe/a de partida, cocinero/a, repostero/a, encargado/a y ayudantes en el **2.º**; auxiliar en el **3.º** (arts. 15-16) | Se usan como sinónimos, y «chef corporativo» no está en el convenio: es una denominación de uso del multi-outlet | **NO, y es el hueco más limpio del research.** L2 comparó las **6 de 20 fuentes** que sí distinguen roles: **ninguna traza la frontera igual que otra**. El PAA pregunta literalmente «¿Cuál es el rango más alto en una cocina?» y «¿Qué orden jerárquico hay en la cocina?» |
| 2 | **Ficha técnica (receta estándar) vs escandallo** | Dos documentos distintos del mismo plato: el escandallo dice **cuánto cuesta**; la ficha técnica dice **cómo se hace** (pasos, técnica, tiempos, punto, montaje, alérgenos, conservación) | Se llaman igual y se venden como lo mismo | **NO.** La única ficha técnica completa de la SERP española es **de pago (15 €, ingenieriademenu.com) y es de costeo**. Y **tampoco lo cubre nuestro propio catálogo**: `ficha-escandallo-base.xlsx` es 100 % coste, sin un solo campo de proceso (L6, verificado celda a celda) |
| 3 | **Receta estándar de verdad vs la plantilla de 5 campos** | Una receta estándar operativa lleva rendimiento, alérgenos, temperatura de servicio, tolerancias y fecha de revisión | Se confunde con una tarjeta de receta doméstica | **NO.** La plantilla gratuita más descargada de la SERP (crehana.com) tiene **5 campos**: número, nombre, ingredientes, instrucciones y notas. Sin alérgenos, sin rendimiento, sin temperatura |
| 4 | **Mise en place vs planificación de producción** | El *mise en place* es la preparación del puesto; la planificación de producción es **cuánto hay que producir hoy** contra la previsión de cubiertos y el stock ya elaborado | Se cree que tener el puesto montado es planificar | **NO, y el vacío es total en español.** La única herramienta completa con forecast y escalado de recetas es **Apicbase, un SaaS internacional en inglés/neerlandés/francés/alemán**, sin una palabra en español (L2 §3.4) |
| 5 | **Protocolo de pase vs «cultura del pase»** | Un procedimiento escrito: quién canta, quién marcha, quién despacha, cómo se gestiona un **86**, qué tiempo objetivo tiene cada familia de plato | Se trata como carácter y actitud del chef | **NO.** La única pieza en español sobre el pase (ingenieriademenu.com) son **10 reglas de comportamiento** tipo «no digas "ya casi"» — no un procedimiento con roles y secuencia |
| 6 | **KPI de cocina vs KPI del restaurante** | De cocina son: **% de merma por partida, tiempo de pase, incidencias de alérgenos, horas de cocina por cubierto, cumplimiento de ficha técnica, retrabajos/devoluciones, rotación de la brigada** | Se venden como «KPIs de cocina» el ticket medio, el RevPASH, la rotación de mesas y las reseñas | **NO, y con etiqueta engañosa.** De los **~30 KPIs** que enumeran las dos fuentes más completas (Barcelona Culinary Hub 10, ingenieriademenu 20), **sólo food cost y margen bruto por plato son de cocina**; el resto son de sala, marketing o finanzas |
| 7 | **Cobertura de estación vs competencia técnica** | Cobertura = «¿puede sostener la partida en un servicio lleno?» (niveles 0-3, sin prueba). Competencia = «¿lo hace bien?», medida con prueba práctica puntuada | Se cree que quien cubre, sabe | **NO fuera, y tampoco dentro.** Nuestra `matriz-formacion-polivalencia.xlsx` mide cobertura y nuestra `06-evaluacion-desempeno.xlsx` mide 10 competencias **genéricas** (puntualidad, higiene personal, trabajo en equipo…): ninguna evalúa cortes, cocciones, salsas ni emplatado |
| 8 | **Merma de proceso vs desperdicio alimentario** | La merma es pérdida de **rendimiento** (limpieza, cocción, evaporación); el desperdicio es comida **servible que se tira** y tiene su propia jerarquía legal (Ley 1/2025, art. 5) | Se mezclan, y se gestionan con la misma hoja | **NO.** Y ojo: nuestro `05-control-mermas.xlsx` mide merma **por producto y categoría de compra**, nunca por partida ni contra la producción del día |
| 9 | **Comidas testigo: no es sólo de hospitales y colegios** 🔴 | Art. 30.8-10 del RD 1086/2020: obliga también a **comedores de empresa con menú común**, a **eventos cuando esa sea la actividad principal** y a **cualquier encargo para grupos o eventos de MÁS DE 40 PERSONAS**. Ración ≥**100 g**, identificada y fechada, **7 días** a ≤4 °C o ≤−18 °C | Se cree que es cosa de colectividades sanitarias y escolares | **NO. Es el hallazgo del research** (CE-11). Cualquier chef ejecutivo de hotel, catering o banquetes que sirva un evento mediano está obligado, y casi ninguno lo sabe |
| 10 | **«Elaboración propia» es voluntaria y tiene exclusiones expresas** 🔴 | Art. 11 del RD 1021/2022: la mención es **voluntaria**, y **no es elaboración** fraccionar o envasar un producto ya elaborado por otro, ni cortar o deshuesar carne fresca, ni limpiar o cortar pescado | Se pone en la carta como reclamo sin comprobar si aplica | **NO** (CE-12). Es un mito extendido y trivialmente convertible en una tabla de decisión: «¿esto que hago cuenta como elaboración?» |
| 11 | **Alérgenos: el Rgto. 852/2004 NO tiene un capítulo de alérgenos** | La obligación de no cruzar alérgenos es el **Anexo II, Capítulo IX, punto 9**, insertado por el Rgto. (UE) 2021/382. Lo que sí es un capítulo nuevo es el **XI bis, «cultura de seguridad alimentaria»**, que es obligación **de la dirección** | Se cita un «capítulo de alérgenos» inexistente; y el «Cap. V bis» que muchos suponen de alérgenos es de **donación** | **NO** (CE-01, CE-02, CE-03). Y corrige una suposición del propio encargo |
| 12 | **Vida útil: no existe una cifra legal de días** | No hay tabla legal de «esta salsa dura X días». Sólo hay obligación de **estudio de vida útil** cuando el producto listo para consumo favorece a *Listeria monocytogenes* (Rgto. 2073/2005, Anexo II), y reglas propias para lo **congelado** (RD 1021/2022, art. 5) | Circulan tablas de días presentadas como normativa | **NO** (CE-08, CE-37). Quien publica una tabla de días como ley está inventando el dato |
| 13 | **Acrilamida: nivel de referencia ≠ límite sancionable** | El Rgto. (UE) 2017/2158 fija **niveles de referencia** (café tostado 400 μg/kg, instantáneo 850 μg/kg) que **disparan la revisión de medidas**, no un límite. Y **no menciona a los restaurantes** como sujeto obligado: aplica a fabricantes y, con requisitos extra, a franquicias con suministro centralizado | Se vende como si multaran al restaurante por freír oscuro | **NO** (CE-19, CE-20). Fritura de patata por debajo de 175 °C sigue siendo buena práctica: eso es lo que hay que decir |
| 14 | **El mito de los 25 kg** | El RD 487/1997 **no contiene ninguna cifra en kilos** ni en su articulado ni en su Anexo: exige evaluar carga, esfuerzo, suelo, temperatura, agarre y factores individuales. El «25 kg» es una **guía técnica orientativa del INSST**, no vinculante | Se enseña como límite legal en todos los cursos del sector | **NO** (CE-24). Verificado por lectura íntegra del Anexo |
| 15 | **El uniforme y el calzado: no hay «ley del uniforme», hay dos marcos que se suman** | Higiene alimentaria (852/2004, Anexo II, Cap. VIII: «vestimenta adecuada, limpia y, en su caso, protectora») **+** PRL: el Anexo III del RD 773/1997 lista literalmente **«utilización regular de cuchillos de mano en la producción»** y **«trabajos en ambientes húmedos»** como generadores de EPI obligatorio y **gratuito** | Se trata como imagen de marca o como un plus de calidad | **NO** (CE-05, CE-22, CE-23). Una cocina activa los dos supuestos casi por definición |
| 16 | **«Carné de manipulador»** | No existe desde el **RD 109/2010**, que derogó el RD 202/2000. La formación es del titular, por puesto, y puede impartirla la propia empresa (Rgto. 852/2004, Anexo II, Cap. XII) | Se pide en ofertas de trabajo y se vende como «carné oficial homologado» | **NO, y lo repiten portales serios:** **randstad.es, con fecha 18-may-2026**, lo menciona como certificación valorable. 16 años después de su derogación (MM-30, CE-04) |

**Ese es el índice de criterio del manual: 16 distinciones, 13 sin cobertura gratuita decente y 6 donde lo gratuito afirma algo falso** (nº 9, 10, 11, 12, 13, 14, 16 — siete si se cuenta el carné aparte). Todas comprobables por el lector en un minuto abriendo el BOE o EUR-Lex: es la mejor prueba de criterio que puede dar un producto de pago.

### 1.1 Los cuatro errores repetidos que el manual puede corregir con autoridad (L2 §4)

| Error | Dónde se midió | Qué escribe el manual |
|---|---|---|
| **Cifras con apariencia de estudio y sin fuente** | `qamarero.com/blog/organigrama-de-un-restaurante-estructura` publica «30 % menos rotación», «25 % de aumento de eficiencia», «40 % de reducción de conflictos laborales», «30 % de incremento de productividad» **sin citar nada**. El mismo dominio ya salió con el mismo patrón en el research del Manual del Manager | Cifra con URL y fecha, o «sin fuente verificada». Nunca una cifra suelta con aire de dato duro |
| **Normativa de otro país sin avisar** | `germandebonis.com` mezcla **SENASA** (organismo argentino) dentro de un «manual de procedimientos de cocina» sin decir en ningún momento cuál es su marco legal | El manual dice en la primera página que su marco es **español** y qué hacer si el lector está fuera |
| **La brigada de Escoffier presentada como universal** | 4 fuentes (loomispay, monouso, qamarero, BCH) describen organigramas de 8-24 puestos con nombres franceses como si fueran el estándar. **Sólo loomispay** reconoce un modelo moderno reducido | El manual da el organigrama del ALEH VI (10 puestos reales) y **dice cuándo NO aplica el modelo clásico**: una cocina de 6 personas no está «mal» comparada con un hotel de lujo |
| **KPIs de sala vendidos como KPIs de cocina** | BCH y ingenieriademenu venden listas de 10 y 20 KPIs con SEO de «cocina» cuando la mayoría son de sala/marketing/finanzas | Concepto nº 6 de la tabla anterior, con la línea trazada explícitamente |

---

## 2. Normativa de COCINA, España 2026: lo verificado hoy y lo que se reutiliza por id

L3 leyó **texto consolidado** en `boe.es` y `eur-lex.europa.eu` con `curl` (no fichas ni blogs) y extrajo **dos PDF oficiales íntegros con PyMuPDF** (la guía de la Comunidad de Madrid, 53 págs, y el avance de siniestralidad del MITES, 24 págs). Lo ya verificado el 4-sep para el Manual del Manager **no se re-verifica**: se cita por su id `MM-*` y sólo se confirma que sigue vigente.

### 2.1 Lo nuevo, verificado hoy (ids `CE-*`, fiabilidad Alta salvo lo marcado)

| id | Tema | Qué dice la norma | Norma y artículo | Fiabilidad |
|---|---|---|---|---|
| **CE-11** 🔴 | **Comidas testigo** | Obligatorias para residencias, centros de día, comedores escolares e infantiles, hospitales y campamentos; **comedores colectivos con menú común (institucionales y de empresa)**; medios de transporte; **eventos cuando sea la actividad principal**; y **cualquier encargo para grupos o eventos de más de 40 personas**. Ración **≥100 g**, identificada y fechada, recogida en el momento del servicio, conservada **≥7 días** a **≤4 °C** o **≤−18 °C** | RD 1086/2020, **art. 30.8, 30.9 y 30.10** | **Alta** (texto leído letra a letra) |
| **CE-12** 🔴 | **«Elaboración propia»** | Mención **voluntaria**. No es elaboración: fraccionar o envasar un producto ya elaborado por otro fabricante, cortar o deshuesar carne fresca, limpiar o cortar pescado | RD 1021/2022, **art. 11** | Alta |
| **CE-01** | **Alérgenos / contaminación cruzada** | El equipo, transporte o recipientes usados con un alérgeno del Anexo II del Rgto. 1169/2011 no pueden reutilizarse sin limpiar y comprobar ausencia de restos visibles. **No es un capítulo dedicado**: es el **punto 9 del Cap. IX** del Anexo II, insertado por el Rgto. (UE) 2021/382 | Rgto. (CE) 852/2004 | Alta |
| **CE-02** | **Cultura de seguridad alimentaria** | Obligación **de la dirección**: compromiso, liderazgo, conocimiento de peligros por todo el personal, comunicación abierta entre turnos y recursos suficientes; adaptada a la naturaleza y tamaño de la empresa | Rgto. 852/2004, Anexo II, **Cap. XI bis** | Alta |
| **CE-03** | Donación de alimentos | El «Cap. V bis» que el encargo suponía de alérgenos es en realidad de **redistribución/donación** (aptitud, fechas, envase, temperatura, trazabilidad) | Rgto. 852/2004, Anexo II, Cap. V bis | Alta |
| CE-04 | Formación de manipuladores | «…de acuerdo con **su actividad laboral**»: por puesto, no genérica | Rgto. 852/2004, Anexo II, Cap. XII, punto 1 | Alta |
| CE-05 | Indumentaria | «Vestimenta adecuada, limpia y, en su caso, protectora»; prohibido manipular con enfermedad transmisible, herida infectada o diarrea sin avisar al operador | Rgto. 852/2004, Anexo II, Cap. VIII | Alta |
| CE-07 | «Sin gluten» | **≤20 mg/kg** «sin gluten» · **≤100 mg/kg** «muy bajo en gluten». Vigente desde el 20-07-2016 | Rgto. (UE) 828/2014, arts. 1-3 y 5 | Alta (límites) / **Media** (el texto **no menciona expresamente a la restauración**) |
| CE-08 | Vida útil y *Listeria* | El Rgto. 2073/2005 aplica a toda la cadena **incluida la venta al por menor**; para alimentos listos para consumo que favorezcan el crecimiento de *L. monocytogenes* exige **estudio de vida útil** documentado (pH, aw, sal, conservantes, envase, literatura, modelos predictivos) | Rgto. (CE) 2073/2005, art. 1 y Anexo II | **Media** (verificado por intermediario sobre el HTML, no letra a letra) |
| CE-09 | Trazabilidad | Un paso atrás (art. 18.2) y un paso adelante (18.3). **El paso adelante no alcanza al consumidor final**: sólo importa si se suministra a otro establecimiento | Rgto. (CE) 178/2002 | Alta |
| CE-10 | Temperaturas | Refrigeradas **≤4 °C** si vida útil >24 h y **≤8 °C** si <24 h; congeladas **≤−18 °C**; enfriar de 60 a 10 °C en **<2 h**; recalentar a **≥74 °C ≥15 s** en el centro | RD 1086/2020, art. 30.1-30.7 (redacción del RD 1021/2022) | Alta (confirmado por dos vías: BOE + guía CAM 2024) |
| CE-13 | Congelación y etiqueta | Producto elaborado en el propio establecimiento y luego congelado: **tres fechas** en la etiqueta (elaboración/transformación + congelación + caducidad o consumo preferente del congelado) más registro de descripción y cantidad | RD 1021/2022, art. 5 | Alta |
| CE-14 | **Anisakis** | **−20 °C ≥24 h** o **−35 °C ≥15 h** en la totalidad del producto; informar por cartel o carta-menú (art. 8.2); excepción si se aplica ≥60 °C ≥1 min | RD 1021/2022, art. 8.1-8.3 (reutiliza y confirma **MM-33**) | Alta |
| CE-16 | Trazabilidad en la inspección | Qué comprueba el inspector: albaranes con lote y caducidad → envases originales conservados y fechas de elaboración → destinatarios y comidas servidas. **La «trazabilidad de proceso» interna no la exige la norma**, pero sin ella una retirada es mucho más lenta y cara | Guía CAM 2024 sobre Rgto. 178/2002 | Alta (PDF oficial de 53 págs extraído íntegro) |
| CE-17 | Aceites de fritura | Componentes polares **<25 %**. Vigente pese a que el RD 176/2013 derogó otros artículos de la misma Orden | Orden 26-01-1989, art. 6.3 (reutiliza MM) | Alta |
| CE-18 | Contaminantes en materia prima | El **Rgto. (UE) 2023/915 derogó al Rgto. 1881/2006** (~25-05-2023) y fija máximos de dioxinas, PCB, mercurio, cadmio, plomo, estaño y micotoxinas. **Vincula al COMPRAR**, no al elaborar | Rgto. (UE) 2023/915, arts. 9 y 11 | Alta (derogación) / Media (detalle de anexos) |
| CE-19 / CE-20 | Acrilamida | Obliga a **fabricantes**, con régimen simplificado para pequeños operadores y extra para franquicias con suministro centralizado; **no nombra a los restaurantes**. Fritura de patata **<175 °C**; niveles de referencia café tostado **400** e instantáneo **850 μg/kg** = disparador de revisión, no límite sancionable. Aplicable desde el 11-04-2018 | Rgto. (UE) 2017/2158 | Alta (ámbito) / Media (anexos) |
| **CE-21** | **PRL — temperatura del local** | Trabajos ligeros: **14-25 °C**; humedad 30-70 %; ventilación mínima 50 m³/h por trabajador en ambientes calurosos | RD 486/1997, Anexo III, punto 3 | Alta (texto íntegro) |
| **CE-22** | **PRL — suelos** | «Fijos, estables y **no resbaladizos**, sin irregularidades ni pendientes peligrosas» | RD 486/1997, Anexo I, punto 3.1º | Alta |
| **CE-23** | **PRL — EPI de cocina** | El Anexo III lista literalmente **«utilización regular de cuchillos de mano en la producción»** → guantes de protección mecánica, delantal/polainas/pantalón resistentes al corte, calzado resistente a perforaciones; y **«trabajos en ambientes húmedos»** → calzado antideslizante. El empresario lo proporciona **gratis** y lo repone | RD 773/1997, art. 3.c) y Anexo III | Alta (texto íntegro) |
| **CE-24** | **PRL — el mito de los 25 kg** | El RD **no fija ninguna cifra en kilos**: sólo exige evaluar factores cualitativos. El 25 kg es una guía técnica orientativa del INSST, no vinculante | RD 487/1997, Anexo, puntos 1-5 | Alta (ausencia confirmada por lectura íntegra) |
| CE-25 / CE-26 | PRL — máquinas | Elementos móviles con riesgo de contacto mecánico → **resguardos** (picadoras, cortadoras de fiambre, batidoras, amasadoras). Equipos con desgaste → **comprobaciones periódicas documentadas** por personal competente, conservadas toda la vida útil del equipo | RD 1215/1997, Anexo I punto 1.8 y art. 4 | Alta |
| CE-27 / CE-28 | PRL — formación y EPI | Formación teórica y práctica adecuada al puesto, dentro de jornada y **cuyo coste no recae en el trabajador**; EPI cuando el riesgo no se pueda evitar por medios colectivos | Ley 31/1995, arts. 19 y 17.2 | Alta |
| CE-29 | Guía oficial de riesgos en cocina | INSHT, «Restaurantes, Bares y Cafeterías» (Serie Microempresas): suelo antideslizante, limpiar grasa **en frío**, cuchillos con mango antideslizante, resguardos, **cambiar el aceite en frío**, mangos de sartén hacia dentro, comprobar el termostato de la freidora | INSHT | **Media** — el PDF **no lleva año de edición** (sólo se acota «anterior a 2018» por el nombre del organismo) y se leyó de un espejo sectorial: `insst.es` dio 404 |
| **CE-30** | **Siniestralidad 2025** | Hostelería: **50.837** accidentes de trabajo en jornada con baja, **19 mortales**. Es el **5.º sector** (detrás de manufacturera 96.068, construcción 79.845, comercio 69.968 y actividades administrativas 57.030) — **no el 4.º**, como dice parte de la prensa. Índice de incidencia **2.731,1/100.000** frente a 2.547,5 de media; índice **mortal 1,02** frente a 2,81: muchos accidentes, pocos mortales | MITES, Estadística de AT, avance ene-dic 2025 | **Alta** (PDF oficial extraído y contado: págs. 4, 9 y 17) |
| CE-31 | Desperdicio — jerarquía | Orden legal exacto ante un excedente: **1º prevención · 2º donación para consumo humano · 3º alimentación animal · 4º subproductos industriales · 5º reciclado/compost · 6º valorización energética**. Se puede adaptar por viabilidad técnica, seguridad alimentaria o eficiencia, **documentándolo** | Ley 1/2025, art. 5.1-5.2 | Alta |
| CE-32 | Desperdicio — hostelería | *Doggy bag* universal con envases aptos, reutilizables o reciclables; plástico de un solo uso remite al art. 55.1 de la Ley 7/2022 y su cobro obligatorio | Ley 1/2025, art. 8 | Alta |
| CE-33 | Desperdicio — exención | Exentos del **plan** los establecimientos de hasta **1.300 m²** de superficie útil, y las **microempresas quedan excluidas por completo** (art. 6.6). ⚠️ **Con el mismo CIF, si el conjunto de locales supera 1.300 m², sí obliga** | Ley 1/2025, art. 6.4.c) y 6.6 | Alta |
| CE-34 | Convenios de donación | Deben fijar recogida, transporte y almacenamiento; **selecciona el donante**, no el receptor; el receptor puede rechazar de forma justificada | Ley 1/2025, art. 7 | Alta |
| CE-35 | Botulismo en V gama | El Comité Científico de la AESAN evaluó en 2024 el riesgo en alimentos de V gama tras casos en España en 2023; recomienda conservar **<4 °C, idealmente <3,3 °C**. Aprobado el **12-12-2024**, Revista del Comité Científico vol. 40 (2024), pp. 33-69 | AESAN | **Media** — ⚠️ `aesan.gob.es` **devuelve 404 en todas sus rutas** (mismo patrón del 4-sep). Contenido y fecha confirmados por ACSA/Generalitat, **no se leyó el PDF original** |
| CE-36 | Cocina al vacío | Existe una «Guía de prácticas correctas de higiene específica para la cocina al vacío» de la Agència de Salut Pública de Catalunya; se apoya en el APPCC y **no fija días de vida útil** | ASPCAT | **Media-baja** — URL exacta no localizada |
| **CE-37** | **No hay cifra legal de días de vida útil** | Síntesis de CE-08 + CE-13 + CE-35: no existe tabla legal. Cada establecimiento lo fija y lo justifica en su APPCC, salvo el caso ya regulado de la congelación | — | **Alta** (la ausencia de norma es en sí el dato verificado) |
| CE-38 / CE-39 / CE-40 | Inspección por comunidad | **Madrid**: «Guía de requisitos de seguridad alimentaria para establecimientos de restauración», 1.ª ed., **febrero 2024**, 53 págs, leída íntegra. **Cataluña**: registro **RSIPAC** + **GPCH** reconocidas por la ACSA. **Andalucía**: **PGH + APPCC** con documento orientativo de la Junta. **Ninguna impone requisitos más estrictos que la norma estatal**: cambia el nombre del sistema documental y el grado de detalle de la guía | — | Madrid **Alta** · Cataluña y Andalucía **Media** (estructura confirmada, contenido no leído íntegro) |

### 2.2 Lo que se reutiliza sin re-verificar (ids `MM-*`, verificados el 2026-09-04)

| id | Qué aporta a este manual |
|---|---|
| **MM-29** | APPCC obligatorio (simplificado si procede) **con una persona responsable designada de su aplicación** — la base del capítulo 13 |
| **MM-30** | **El carné de manipulador no existe desde 2010** (RD 202/2000 derogado por el RD 109/2010) |
| **MM-31** | 14 alérgenos, obligatorios en no envasados (art. 44.1); **el cartel «consulte al personal» no basta** sin soporte escrito o electrónico accesible (RD 126/2015, art. 6.5) |
| **MM-32 / MM-33** | **RD 3484/2000 y RD 1420/2006 DEROGADOS** con efectos del 22-12-2022 |
| MM-35 | Sanciones de seguridad alimentaria (Ley 17/2011, art. 52): leves ≤5.000 € · graves 5.001-20.000 € · muy graves 20.001-**600.000 €** + cierre de hasta 5 años |
| MM-36 | *Doggy bag* obligatorio desde el **22-12-2022** (RD 1021/2022, art. 18.5), con la excepción del bufé libre y la obligación de informar |
| MM-01 a MM-13 | Jornada, descansos, horas extra, vacaciones, contratación y despido — aplican a la brigada igual que al resto de la plantilla; **este manual los cita, no los reescribe** (viven en el Manual del Manager, caps. 9-14) |
| MM-14 / MM-15 | ALEH VI, 6 áreas funcionales y 3 grupos; diferencia salarial entre provincias |
| MM-41 / MM-42 / MM-43 | Estructura de costes (producto 30 %, personal 30-35 %); coste laboral de hostelería, el más bajo de las 19 secciones; **inversión en formación 20,14 €/trabajador/año frente a 76,49 € de media nacional** |
| MM-53 / MM-56 / MM-57 | Cotización empresarial, absentismo (ETCL) y salarios del sector |

### 2.3 Estado de vigencia a 2026-09-06

| Norma | Estado |
|---|---|
| Rgto. 852/2004 (con la modificación 2021/382) · 1169/2011 + RD 126/2015 · 828/2014 · 2073/2005 · 178/2002 · 2017/2158 · 2023/915 | **VIGENTES** |
| RD 1086/2020 (redacción RD 1021/2022) · RD 1021/2022 · Orden 26-01-1989 art. 6.3 · Ley 1/2025 (art. 6 exigible desde 02-04-2026) | **VIGENTES** |
| Ley 31/1995 (act. 09-04-2026) · RD 486/1997 · RD 773/1997 (mod. RD 1076/2021) · RD 1215/1997 · RD 487/1997 | **VIGENTES** |
| **RD 3484/2000** · **RD 1420/2006** | **DEROGADOS** desde el 22-12-2022 |
| **Rgto. (CE) 1881/2006** | **DEROGADO** desde ~25-05-2023 por el Rgto. 2023/915 |
| **RD 202/2000** (carné de manipulador) | **DEROGADO** desde el 20-02-2010 por el RD 109/2010 |

### 2.4 Qué de esto es argumento de venta (y qué NO se puede decir en el copy)

1. **Nadie del censo de pago demuestra estar actualizado.** L1 lo dice con nombres: los libros de FP y el manual de higiene de 109,25 € **no tienen fecha de revisión visible** frente al RD 1021/2022; ninguna ficha consultada lo menciona. Un manual que dice «el RD 3484/2000 está derogado desde 2022, aquí tienes la ficha del BOE» se separa solo.
2. **CE-11 es la mejor prueba de criterio del producto entero.** Una obligación real, con umbral concreto (**40 personas**), que afecta a banquetes, catering y hoteles, y que no aparece en ninguna de las 20 fuentes que leyó L2 ni en ningún producto del censo de L1.
3. **El bloque de PRL de cocina no existía en el research del hermano** y es donde más se puede corregir al sector: los 25 kg que no están en la norma, el EPI de corte que sí es obligatorio y gratuito, la temperatura legal de 14-25 °C que casi ninguna cocina cumple en verano.
4. **Y hay criterio que sólo se da diciendo que la ley NO obliga:** no hay cifra legal de días de vida útil (CE-37), no hay periodicidad legal de formación en alérgenos, la acrilamida no nombra a los restaurantes y el «carné» no existe. Decirlo así es un diferenciador que ningún blog del sector puede permitirse, porque casi todos venden el curso o el servicio.
5. ⚠️ **Límite del copy comercial** (regla de John del 5-sep, `feedback_copy-comercial-sin-argumento-boe`): en Stripe y en los titulares lideran los **entregables y el beneficio práctico**. «Verificado contra el BOE» se mantiene **dentro** del producto, en la landing larga y en el email — como rigor, nunca como gancho.

### 2.5 Riesgo de caducidad de este bloque (menor que el del hermano)

| Qué puede cambiar | Probabilidad |
|---|---|
| Informe AESAN de botulismo / guías autonómicas: que vuelvan a estar accesibles y haya que citar el PDF original | Alta (es un arreglo, no un riesgo) |
| Nuevo reglamento europeo de contaminantes o de acrilamida | Baja a corto plazo |
| Convenio provincial (Madrid expiró el 31-12-2025, se aplica por ultraactividad; Cataluña vigente 2025-2028) | **Alta**, y afecta a §3 |
| ALEH VI | **Bajo hasta el 31-12-2030** (vigencia de la modificación del 04-09-2026) |
| SMI y cotización | Certeza anual |

**Cómo lo gestiona el producto** (idéntico al hermano, no es retórica): ninguna cifra normativa dentro de una fórmula —todas en celda verde con nota y fecha—; hoja `Estado Normativo` con fecha de corte y URL editables; bloque de «estado a la fecha de esta edición» al principio de cada capítulo legal; cada afirmación con norma + artículo + enlace; un apartado que enseña a **abrir la ficha de vigencia del BOE** y a mirar si dice «Norma derogada»; y actualizaciones incluidas con `productos-changelog.ts`.

---

## 3. El puesto: lo que dice el convenio y lo que pide el mercado

### 3.1 El ALEH VI define por escrito las funciones de los 10 puestos de cocina — y casi nadie lo cita

Área funcional **2.ª (Cocina y Economato)**, arts. 15-17 del ALEH VI (BOE-A-2023-6344, texto leído íntegro del PDF oficial). **La modificación del 04-09-2026 (BOE-A-2026-18630) NO toca estas funciones**: sólo normaliza el lenguaje de género («sistema de cremallera»: Jefa/e, Cocinera/o, Ayudanta/e) y el propio texto dice que ese cambio «no supone alteración alguna en la descripción de la prestación laboral». Lo sustantivo de esa reforma (audiencia previa en despido, régimen disciplinario del fichaje, caps. XIII LGTBI y XIV catástrofes) ya está en el Manual del Manager (MM-13, MM-14) y **este manual lo cita, no lo reescribe**.

| Grupo | Puestos | Función literal (art. 17.B, resumida donde se indica) |
|---|---|---|
| **1.º** | **Jefe/a de cocina** | «Planificación, organización y control de todas las tareas propias del departamento de cocina y repostería. Organizar, dirigir y coordinar el trabajo del personal a su cargo… Realizar inventarios y controles de materiales… **Diseñar platos y participar en su elaboración**. Realizar propuestas de pedidos… y gestionar su conservación, almacenamiento y **rendimiento**. Supervisar el mantenimiento y uso de maquinaria… **Colaborar en la instrucción del personal a su cargo**» |
| 1.º | **2.º jefe/a de cocina** | Las mismas funciones de planificación, organización y control, **«colaborar y sustituir al jefe/a de cocina»** |
| 1.º | **Jefe/a de catering** | «Dirección, control y seguimiento del proceso de elaboración y **distribución** de comidas… Cuidar de que la producción reúna las condiciones exigidas, tanto **higiénicas** como de montaje. **Organizar, instruir y evaluar** al personal a su cargo» |
| **2.º** | **Jefe/a de partida** | «Control y supervisión **de la partida** y/o servicio asignado bajo la dirección del jefe/a de cocina… Participar en el control de aprovisionamientos, conservación y almacenamiento. **Elaborar informes sobre la gestión de los recursos y procesos de su partida**» |
| 2.º | **Cocinero/a** | «Preparación, aderezo y presentación de platos… **Colaborar en la planificación de menús y cartas. Colaborar en la gestión de costes e inventarios, así como en las compras**» |
| 2.º | **Repostero/a** | Postres, dulces, bollería y masas; **«realizar el cálculo de costes relacionados con sus cometidos»**; organizar y controlar al personal a su cargo |
| 2.º | **Encargado/a de economato** | «Dirección, control y supervisión… Establecer las necesidades de mercancías y material… **Elaborar las peticiones de ofertas, evaluación y recomendación de las adjudicaciones**. Controlar y planificar las existencias» |
| 2.º | Ayudante/a de cocina | «Participar **con alguna autonomía y responsabilidad** en las elaboraciones **bajo supervisión**» |
| 2.º | Ayudante/a de economato | Compra y gestión de mercancías; recibir pedidos y **controlar las fechas de caducidad**; vigilar existencias |
| **3.º** | Auxiliar de cocina/economato | «Realizar **sin cualificación** las tareas de limpieza de útiles, maquinaria y menaje… **bajo supervisión**. Preparar e higienizar los alimentos» |

> **La lectura que vale por todo el bloque:** el convenio ya separa **tres niveles reales de delegación** —«cualificado, autónomo y responsable» (cocinero, repostero, jefe de partida, encargado) · «con alguna autonomía **bajo supervisión**» (ayudantes) · «**sin cualificación** bajo supervisión» (auxiliar)—. No es una escala inventada por el chef: está en el BOE. Y **ninguno de los 31 productos del censo de L1 la usa.**

### 3.2 Movilidad funcional: la base legal de mover gente entre partidas (art. 19 ALEH VI)

| Supuesto | Qué exige |
|---|---|
| **Dentro del mismo grupo profesional** | **Sin más límite que el grupo o la titulación.** Mover a un cocinero a hacer de jefe de partida, o a un ayudante de repostería a línea caliente, **no necesita pacto ni causa**. Los convenios provinciales pueden regular la **retribución** de la polivalencia, pero no la propia movilidad |
| **A funciones de otro grupo profesional** | Causa económica, técnica, organizativa o de producción (art. 41.1 ET), informar «con la máxima celeridad» a la RLT, y tope de **6 meses en 1 año u 8 meses en 2 años**. Nivel superior → se paga el superior; nivel inferior → se mantiene el salario de origen |
| **A otra área funcional de forma continuada** | Misma causa, **como medida de garantía de estabilidad del empleo**, y obliga a **garantizar formación adecuada** sin menoscabar la formación profesional de la persona |
| **Trabajos de categoría superior** (art. 22 Madrid) | Se cobra la superior **desde el primer día**; a los **4 meses seguidos o 6 alternos en 12 meses** entra el art. 39 ET (consolidación/ascenso) |
| **Trabajos de categoría inferior** (art. 23 Madrid) | Sólo por necesidades perentorias o imprevisibles, avisando al Comité, **cobrando siempre la categoría propia**, tope de **12 días seguidos o 20 alternos al año** |

⚠️ **El art. 21 del convenio de Madrid remite expresamente al ALEH estatal** para clasificación y movilidad funcional: es **materia reservada**, ningún convenio provincial puede endurecerla ni suavizarla.

### 3.3 Lo que tu convenio dice de la COCINA y no del resto del restaurante

Éste es el bloque que **no se solapa** con el Manual del Manager (que cubre el marco general: 40 h, 12 h entre jornadas, registro de jornada, permisos):

| Materia | Madrid | Cataluña / Barcelona |
|---|---|---|
| **Jornada partida** | Es la que tiene una interrupción de **≥1,5 h**; descanso de 30 min en continuada >6 h, divisible en dos de 15 si es partida | **Turnos de máximo 5 h y mínimo 3** para cocina y sala, con **≥1,5 h** entre turno y turno; 20 min computados como trabajo en cualquier jornada >5 h |
| **Descanso entre jornadas** 🔴 | 12 h (art. 34.3 ET) | En **Pirineo y Pre-Pirineo, Costa Daurada, Maresme y provincia de Girona** se puede **bajar a 10 h** para las áreas funcionales **2.ª (Cocina) y 3.ª (Sala)**, con **14 días de preaviso** y razones organizativas. **Excluidos siempre**: menores de 18, personas con discapacidad, trabajadores nocturnos, embarazadas, contratos formativos y reducción por guarda legal (art. 28.c) |
| **Manutención (comida de personal)** | **57,82 €/mes** (tabla 2025, vigente en 2026 **por ultraactividad**); derecho de quien trabaje donde se elaboren comidas/cenas; sustituible por metálico; se abona también en vacaciones y fiestas (art. 28) | **59,21 €/mes** en 2026 (56,93 € en 2025), art. 38. Más alojamiento 55,53 €/mes si aplica y plus de transporte 14,42 €/mes |
| **Formación** | **Plus Compensatorio de Formación: 20 €/mes (240 €/año)** para quien **no** acredite formación específica del sector; el tiempo de formación **es tiempo efectivo de trabajo** (art. 31) | — |
| **Ropa de trabajo** | Si la empresa exige una modalidad concreta, **la facilita a su cargo**; puede sustituirse por metálico pactado con la RLT, con carácter de **suplido** (art. 26.2 ET: no cotiza ni tributa como salario). No exigir modalidad **no exime** de las normas de higiene (art. 36) | ⚠️ **No se localizó artículo equivalente** en el tiempo de este research |

### 3.4 Las tablas salariales de los 5 niveles de cocina (PDF oficiales, leídos)

**Madrid** — salario base mensual, 14 pagas, por clase de establecimiento (BOCM núm. 82, 06-04-2024; tabla 2025 **vigente en 2026 por ultraactividad**):

| Nivel | Puesto | Clase A | Clase B | Clase C |
|---|---|---|---|---|
| I | Jefe/a de Cocina | **1.415,47 €** | 1.366,11 € | 1.250,91 € |
| II-A | Segundo/a Jefe/a de Cocina | 1.316,72 € | 1.292,05 € | 1.217,99 € |
| II-B | Jefe/a de Partida | 1.300,28 € | 1.267,33 € | 1.201,51 € |
| III | Cocinero/a · Repostero/a · Encargado/a de Economato | 1.283,83 € | 1.250,91 € | 1.160,37 € |
| IV | Ayudante de Cocina · Ayudante de Economato | 1.217,99 € | 1.185,05 € | 1.127,42 € |
| V | Auxiliar (marmitón, pinche, fregador/a) | 1.152,15 € | 1.119,22 € | 1.086,31 € |

*(Clase A = restaurantes 4-5 tenedores, bar-restaurante 4-5T y salones de banquetes; B = 3 tenedores y autoservicio; C = 1-2 tenedores, cafés-bares y bares. **Se suma siempre** Plus Convenio 191,22 €/mes en 11 pagas + manutención si aplica.)*

**Barcelona / Cataluña** — salario mensual, 14 pagas, tabla **Any 2026** (DOGC núm. 9630, 23-03-2026), grupo A:

| Nivell | Puesto | Grupo A |
|---|---|---|
| I | *Cap de cuina* | **2.121,29 €** |
| II | *Segon/a cap · Cap de partida · Reboster/a* | 1.864,51 € |
| III | *Cuiner/a · Reboster/a oficial · Encarregat/a d'economats* | 1.803,05 € |
| IV | *Ajudant/a cuiner/a · Ajudant/a d'economat* | 1.607,25 € |
| V | *Marmitons* | 1.577,05 € |

**El mismo puesto, dos provincias** (clase/grupo A, 2026):

| Puesto | Madrid | Barcelona | Diferencia |
|---|---|---|---|
| **Jefe/a de Cocina** | 1.415,47 € | 2.121,29 € | **+49,9 %** |
| Segundo/a Jefe/a | 1.316,72 € | 1.864,51 € | +41,6 % |
| Cocinero/a | 1.283,83 € | 1.803,05 € | +40,4 % |
| Ayudante de Cocina | 1.217,99 € | 1.607,25 € | +32,0 % |
| Auxiliar de Cocina | 1.152,15 € | 1.577,05 € | +36,9 % |

> **Es la mejor prueba de por qué este manual NO puede dar una cifra única de nómina.** Y es un capítulo entero: el chef ejecutivo de un grupo con centros en dos comunidades opera con dos convenios distintos, dos importes de manutención y —en Cataluña— con una cláusula de descanso reducido que en Madrid no existe.

### 3.5 Lo que pide el mercado: 17 ofertas reales (2026)

L4 leyó ofertas activas en InfoJobs, Turijobs, Hosco, LinkedIn/JobLeads, Indeed y agregadores sectoriales. **14 con datos verificables** (título, empresa, ubicación y responsabilidades citables) más 3 síntesis de portal. ⚠️ **De 5 de ellas sólo se pudo leer el snippet** (bloqueo HTTP 456/410 del portal tras varias peticiones).

| Bloque de responsabilidad | Aparece en | Exigencia concreta citada |
|---|---|---|
| **Dirección y coordinación del equipo de cocina** | **11/17** | Bar Bistec es la única que cuantifica la brigada: «dirige 1-5 personas» |
| Control de costes / food cost / escandallos | 5/17 | Grupo Arzábal: «recetas y escandallos»; Turijobs: «control de inventarios, costes y **rentabilidad**» |
| Seguridad alimentaria / APPCC / alérgenos | 4/17 | Hosco (Valencia): «vigilar cumplimiento **APPCC** y política de prevención de incendios» |
| Formación y evaluación del equipo | 5/17 | Hosco: «arrange staff training and development»; Turijobs: «selección, formación, motivación» |
| Desarrollo de carta / menús estacionales | 3/17 | Hotel Samba: menús «adaptados a perfiles de cliente y **temporada**» |
| Gestión de proveedores / compras | 3/17 | Grupo Arzábal: «búsqueda de materia prima y/o productos»; Hosco: «purchasing supplies and ingredients» |
| **Control de raciones y mermas** | **1/17** | Hosco: «**portion and waste control**» — es la **única** oferta que lo nombra con esas palabras |
| **Multi-outlet / corporativo** | **7/17** | Spring Hoteles: jefe de cocina «**bajo la dirección del Chef Ejecutivo**»; Fuerte Group (varios hoteles), Grupo San Eloy (16 establecimientos), Tapeoteca (cadena/franquicia), SH Hotels, Meliá |
| Experiencia mínima | 2 citadas | **3 años** (Grupo Arzábal) a **5 años** (Turijobs) como Jefe de Cocina o Sous Chef |
| Formación exigida | 1 citada | **FP Grado Superior en Dirección de Servicios de Cocina** |

**Salarios reales de las ofertas** (no de agregadores): Chef Ejecutivo Grupo Arzábal (Madrid) **40.000-45.000 €/año**; Jefe de Cocina hotel 4-5★ Valladolid **32.000-36.000 €**; agregado Turijobs de chef ejecutivo **36.000-50.000 €**. Y en Hosteleo, ofertas reales de Jefe de Cocina: Restaurante Ninot (Madrid) 36.000-38.000 € · Ristorante Magia (Alicante) y Marisa Fernández Catering (Madrid) 24.000-30.000 € · Mako Sushi (Badajoz) 23.000-28.000 € · Bar Bistec (Sevilla) y Signatura (Murcia) **18.000-24.000 €**.

> **La lectura que vale por todo el bloque, y es distinta a la del hermano:** al manager de restaurante independiente sólo las cadenas hoteleras le pedían KPIs por nombre. Aquí pasa algo peor: **de 17 ofertas, sólo UNA nombra explícitamente el control de mermas, y ninguna nombra un tiempo de pase, un cumplimiento de ficha técnica ni una evaluación técnica de la brigada.** Se pide «supervisar», «coordinar» y «garantizar calidad». **Ese vacío entre lo que se le pide y lo que necesita medir es exactamente el producto.**

**Salario de mercado (agregadores) — se presenta como RANGO con su fuente, nunca como «el salario»:**

| Puesto | Fuente | Cifra | Fiabilidad |
|---|---|---|---|
| Chef Ejecutivo (España) | Glassdoor (29 salarios, feb-2026) | Media **54.000 €/año**; P25-P75 de 38.250 a **168.125 €** | Media (acceso directo dio 403; vía snippet indexado) |
| Chef Ejecutivo | Jobted · Jooble · Turijobs | 58.420 € · 45.408 € · media ≈44.750 € (rango 36.000-50.000) | Media |
| Sous Chef (España) | Talent.com (946 registros) | Media **28.000 €/año** | Media |
| Jefe de Cocina | Randstad (perfil profesional) | **25.000-40.000 €/año** (rango cualitativo, sin muestra) | Alta en la descripción funcional · Media en la cifra |
| ⛔ Jefe de Cocina | **Talent.com: 13.700 €/año** | **BAJA — cifra anómala.** Muy por debajo de las ofertas reales verificadas (18.000-45.000 €). Probable mezcla con «cocinero» genérico o jornadas parciales. **No se cita** | — |
| ⛔ Sous Chef | **Glassdoor: «entre 1.500 y 2.500 €/año»** | **BAJA — anomalía evidente de datos. No se cita** | — |

**Rango defendible con lo verificado:** jefe de cocina **25.000-45.000 €/año** · chef ejecutivo/corporativo **40.000-60.000 €/año**, con outliers hasta 168.125 € en hoteles de lujo y grupos grandes. **Ninguna fuente explica la varianza**, y el manual tiene que decirlo así.

---

## 4. Datos del sector: los que ENTRAN, con su etiqueta exacta, y los que NO

⚠️ **Antes de la tabla, una advertencia de ingeniería:** L3 y L4 emiten **ids `CE-*` solapados** (§ verificación propia nº 3). Para poder fusionarlos en `guias-v2-research-sector.json` sin pisarse, en este documento y de aquí en adelante se usa:

- **`CE-*`** → normativa de cocina (los 40 de L3). Se conserva la numeración original.
- **`CS-*`** → datos del sector de cocina (los 23 de L4). **`CS-01` es el antiguo `CE-01` de L4**, y así sucesivamente.

### 4.1 Los que entran (fiabilidad Alta o Media declarada)

| id | Dato | Valor | Fuente exacta | Etiqueta obligatoria en el manual | Fiab. |
|---|---|---|---|---|---|
| **CS-01** | Índice de incidencia de accidentes con baja, **CNAE 56 «Servicios de comidas y bebidas»**, 2024 | **2.646,5** por 100.000 (hombres 2.824,1 · mujeres 2.481,8) | INSST, *Informe anual de accidentes de trabajo en España. Datos 2024* (PDF leído) | «CNAE 56, dato 2024» — **no decir "hostelería"**: hostelería incluye alojamiento | **Alta** |
| **CE-30** | Siniestralidad de **hostelería (sección I)**, 2025 | **50.837** accidentes en jornada con baja · **19 mortales** · incidencia **2.731,1**/100.000 (media 2.547,5) · incidencia **mortal 1,02** (media 2,81) | MITES, avance ene-dic 2025 (PDF leído, págs. 4, 9 y 17) | «hostelería, avance 2025; **5.º sector** por volumen, no el 4.º». Los dos índices se citan **juntos**: muchos accidentes, pocos mortales | **Alta** |
| CS-02 | Accidentes de trabajo totales en España, 2024 | 647.200 con baja (556.385 en jornada, 90.815 in itínere) | INSST, informe 2024 | Contexto, no protagonista | Alta |
| CS-07 | Absentismo en hostelería | 7,9 h/mes por IT sobre 132,9 h pactadas → **5,9 %** | INE, ETCL (reutiliza **MM-56**) | «INE, ETCL» — nunca atribuir a Randstad | Alta |
| **MM-43** | **Inversión en formación por trabajador/año** | Hostelería **20,14 €** frente a **76,49 €** de media nacional (**el 26 %**) | INE, EACL 2025 | El dato duro del eje de personas: **la hostelería invierte en formar una cuarta parte de lo que invierte la economía española** | **Alta** |
| MM-41 | Estructura de costes de referencia | Producto **30 %** · personal **30-35 %** en servicio en mesa | CaixaBankLab × elBullifoundation (2017, rev. 2022) | ⚠️ **CS-19: es el coste del EQUIPO COMPLETO, no sólo cocina.** No existe desagregación oficial «sólo cocina» | Alta, con el matiz |
| MM-35 | Sanciones de seguridad alimentaria | Leves ≤5.000 € · graves 5.001-20.000 € · muy graves 20.001-**600.000 €** + cierre de hasta 5 años | Ley 17/2011, art. 52 | Rango legal, no coste real de un brote (ver CS-21) | Alta |
| CS-08 | Abandono de la hostelería por jóvenes en los 2 primeros años | 38 % | Eurostat, vía prensa sectorial | **«dato europeo, no español»** | Media |
| CS-13 | Consumo energético de cocina | El manual MITECO/Gas Natural Fenosa para PYMEs de hostelería (CNAE 55.1 y 56.1) confirma **cualitativamente** que cocina, cuartos fríos y comedor son los mayores consumidores | MITECO (PDF, sin fecha visible) | Se cita **cualitativo**, nunca con porcentaje: el estudio IDAE con la cifra exacta **no se localizó** | Alta (existencia y contenido cualitativo) |
| CS-17 | Pérdida mensual por mermas en un restaurante | 400-600 €/mes | Encuesta 2025 a >250 profesionales en España; **el medio no identifica el instituto** | Sólo si se cita así, con la salvedad. Preferible: **que el lector calcule la suya** | Media/Baja |
| CS-20 | Sanciones por brote | Coherente con MM-35; las cifras extremas que circulan (300 € de mínimo, 5 años de cierre) **no se cotejaron letra a letra** | Fuentes legales sectoriales | Se usa **MM-35**, que sí es Alta | Media |

### 4.2 Los que NO entran (lista negra de cifras, §14.1)

| Cifra | Por qué no entra |
|---|---|
| **«283 accidentes en cocineros y ayudantes» con desglose** (107 cortes, 42 caídas, 35 sobreesfuerzos, 27 contacto con llamas, 18 golpes) | **CS-04. Circula en prensa sectorial sin atribución rastreable a ningún informe primario.** Candidatos no confirmados: Fremap, UGT-FeSMC, ASEPAL. **Se sustituye por CS-01 y CE-30**, que sí son PDF oficiales |
| **Rango de merma «sano» 4-6 %** | **CS-16. Lo publican proveedores de software de gestión de cocina sin un solo estudio citado.** Se sustituye por el cálculo propio del lector |
| **255 M€/año de pérdida sectorial por mermas** (≈63.000 t) | **CS-15. Cifra zombi.** Repetida en decenas de blogs; el único origen parcial identificado es un estudio de la UAB de **2013** sobre coste del desperdicio (3,10 €/kg), sin confirmación directa |
| **«Hasta el 15 % de la comida cocinada acaba en la basura»** | CS-14. Fuentes sectoriales sin estudio primario |
| **Tasa de rotación en hostelería del 63,8 %** | **CS-06. Ya estaba en la lista negra del hermano** y aquí se agrava: la prensa (Revista Hostelería, 30-04-2026) se la atribuye difusamente a «Linkers», y **L4 verificó directamente que NO aparece en Randstad Research**, a quien se la atribuye habitualmente. Dos padres, ningún informe publicado |
| **«1 cocinero cada 20-25 comensales»** (alta cocina 10-20, bufé 40-50) | **CS-18. Regla empírica de blogs de gestión, sin estudio académico ni patronal.** Si el manual la usa, va como **«regla de partida orientativa que cada casa calibra con su producción»**, jamás como estándar |
| **«El 87 % de los restaurantes no tiene fichas técnicas estandarizadas y pierde 2.400 €/año»** | Aparece repetida en agregadores SEO sin encuesta ni informe localizable. **Descartada por L5 y confirmada aquí** |
| **«Del pulpo se obtiene ~50 % de merma»** | Mismo caso: sin atribución primaria verificable |
| **Consumo energético: «la cocina es más del 50 % del gasto del establecimiento»** · «30.000 kWh/año» · «11.000 kWh/año una freidora» · «el sector es el 7 % del consumo de España» | CS-09 a CS-12. Todas citan a IDAE **sin enlazar el documento primario**. Se usa CS-13 en cualitativo |
| **Talent.com 13.700 €/año para jefe de cocina** y **Glassdoor «1.500-2.500 €/año» para sous chef** | Anomalías evidentes contra las ofertas reales verificadas |
| **Tiempo medio de pase** · **coste directo de un brote** · **horas de formación por trabajador de cocina** | **CS-22, CS-21, CS-23: SIN FUENTE, confirmado.** No existe benchmark español publicado de ninguno de los tres. Van como **métrica que el lector mide con su propia herramienta**, nunca como dato de mercado |

> **La regla de método que sale de aquí, y es la más importante del bloque:** el eje de mermas —que es central al producto— **es el peor documentado de todo el research**. Ninguna cifra de merma tiene estudio primario. La consecuencia de diseño es directa: el manual **no cita benchmarks de merma**, da la **fórmula y la herramienta** (§8, libro 1) para que el lector calcule la suya por partida. Es más honesto y, además, es más útil.

---

## 5. Voz del cliente: dolores, vocabulario, personas y objeciones

### 5.1 Aviso de honestidad que hay que leer antes que la tabla

L5 documentó el bloqueo con tres métodos distintos: **Reddit devuelve 403 por WebFetch, por `curl` y por el proxy `r.jina.ai`**; los comentarios de Facebook y de YouTube se cargan por JavaScript/API y no son accesibles; Quora da 403 desde 2026; Amazon y Udemy no ofrecieron para este nicho un título con reseñas extraíbles (a diferencia del research del hermano, donde sí salieron 7).

**Consecuencia medida:** hay **21 personas identificables y 34 citas o paráfrasis de 11 fuentes**, pero concentradas en 4-5 de los 12 dolores. **Cinco dolores centrales del producto se quedaron con CERO cita primaria**: la ficha técnica que el equipo ignora, las mermas, la producción desordenada, el pase caótico y el miedo a la inspección de Sanidad. **No es que el dolor no exista** —está documentado indirectamente y el propio encargo lo da por conocido—: es que las vías que lo contienen en primera persona están cerradas desde este entorno.

> **Recomendación operativa de L5, que suscribo:** para esas cinco citas, la fuente primaria más accesible y más autorizada que existe **es John**. 29 años en alta hostelería como chef ejecutivo. 5-10 minutos de voz sobre esos cinco puntos concretos valen más que cualquier cita de blog, y la bio ya está anclada en todo el catálogo. **Es una petición concreta, no una idea vaga (§15).**

### 5.2 Los dolores con evidencia, y dónde los resuelve el producto

| Dolor | La evidencia más fuerte | Cap. | Herramienta |
|---|---|---|---|
| **A. Rotación / «no encuentro cocineros»** — 9 citas de 8 personas | **[PRIMARIA]** Ricard Camarena (5 restaurantes, 140-150 empleados): «**Ahora se abren más restaurantes en Valencia que equipos hay disponibles**». Eduard Xatruch (3 establecimientos, ~130 personas): «Lo difícil es conseguir un equipo sólido, comprometido y estable». Juanjo Martínez, **chef ejecutivo del Hyatt Regency Barcelona Tower**: «No hay una combinación perfecta para controlar la rotación de personal» | 3, 18 | 4, 5 |
| **B. Dirigir varias cocinas (hotel / grupo / corporativo)** — 6 citas, 4 fuentes, **3 mercados** | **[PRIMARIA]** César Castañeda, chef corporativo de **Minor Hotels México y Cuba desde 2013, 15 hoteles**: «Mi trabajo consiste en ver una **panorámica completa** de cada hotel y de la marca» · «Es como dirigir una obra de teatro donde el gran reto es que **cada cocinero luzca**». **[PRIMARIA]** Abel Ferrándiz, chef corporativo en Canarias: «En un restaurante independiente puedes trabajar con unas **diez personas** de media, mientras que en un hotel pasas a coordinar equipos de **más de 140 profesionales**» · «El papel de un chef ejecutivo ha evolucionado mucho y hoy implica una importante **carga de gestión administrativa y de control**». **[PRIMARIA]** Juan Sánchez López, chef ejecutivo del Hotel Bonalba 4★: «**Lo mejor, la plantilla. Lo peor, también la plantilla**» · «Hay que hacer una **jerarquía piramidal**, para que funcione el equipo y para que ellos se motiven» | 20, 2 | 4, 1, 8 |
| **C. La transición de escala («yo cocinaba y ahora dirijo»)** | **[PRIMARIA]** Ferrándiz otra vez: «Las decisiones se toman a gran escala, lo que implica una **planificación más estratégica de los pedidos**, una gestión más compleja de los tiempos y una mayor coordinación de los equipos» · «Lo más desafiante ha sido, sin duda, **la gestión de las personas**». ⚠️ **Hueco:** cero citas de un propietario-chef en solitario describiendo el agotamiento de cocinar y dirigir a la vez | 1, 4 | — |
| **D. «Me piden números que no sé dar»** | **[PRIMARIA]** Castañeda, desde el lado del formador: «Queremos que conserves esa pasión… pero **también tenemos que enseñarte números**» · «Tienes que hacerlo entendiendo todas sus implicaciones, incluida la parte de negocio». ⚠️ **Hueco:** no se encontró la cita simétrica de un jefe de cocina admitiendo que no sabe leer su food cost | 9, 10 | 1 |
| **E. Trato al equipo / mandar sin gritar** | **[PRIMARIA]** Castañeda: «**Si les das voz, los equipos se apasionan**» · «los mismos cocineros te dicen: esto lo hacía mi abuelita, o ¿te puedo proponer una receta?» · «**no tienes que aguantar que te griten, no tienes que aguantar trabajar 15 horas**» · «tratar mal al personal es hacer una mala gestión» | 4 | 5 |
| **F. Alérgenos (frustración operativa)** | **[PRIMARIA, Vice España, 11-08-2024]** Mitchell, cocinero: «[Lo peor es] **cuando no te dicen que tienen una alergia hasta el último momento**». Stijn: «Las alergias inventadas son mi mayor problema». ⚠️ **Es frustración operativa, NO el miedo legal** que pedía el encargo: esa cita no existe | 14 | 3, 8 |
| **G. Formación** | Indirecta: Castañeda dedica tiempo deliberado a enseñar números; Tommaso Dainotti (Hosco) sobre por qué se va el talento joven: «**el equilibrio entre horas de trabajo y sueldo se ha convertido en un imprescindible, especialmente para los jóvenes**» (traducido). Y el dato duro: **20,14 € frente a 76,49 €** (MM-43) | 18 | 5 |
| **H-L. Ficha ignorada · mermas · producción desordenada · pase caótico · miedo a Sanidad** | ⛔ **CERO cita primaria**, con búsqueda dirigida y repetida. L5 señala que al leer varios artículos completos (buengusto.co, ingenieriademenu.com) **ninguno contiene un testimonio real**: son piezas prescriptivas que dan el problema por sentado. Es el hueco más llamativo del research porque son los dolores centrales del producto | 5, 6, 7, 8, 10, 13 | 1, 2, 3, 6, 8 |

### 5.3 Vocabulario: español de España con equivalencia LATAM en la primera mención (NO se hacen versiones por país)

| Concepto | Término principal | Equivalencia en la primera mención | Nota |
|---|---|---|---|
| El puesto | **Chef ejecutivo** | **(chef corporativo, cuando dirige varias cocinas)** | **Es el único término del glosario que NO varía en los 6 mercados** — confirmado en ofertas de MX/CO/PE y en 3 entrevistas reales de España, México y Colombia |
| Responsable del día a día | **Jefe de cocina** | (chef de cocina) | Funciona igual en los 6 mercados. **Explicar UNA vez la diferencia con chef ejecutivo**: genera confusión real (2 preguntas de Quora dedicadas sólo a eso) |
| Segundo | **Segundo de cocina (sous chef)** | — | Galicismo asentado en los 6 mercados; aparece en ofertas de Colombia |
| Responsable de sección | **Jefe de partida** | (chef de partie) | Sin variación (Cambridge, Proz, Linguee) |
| La sección | **Partida** | **(estación)** | «Estación» se entiende en toda Hispanoamérica y es más frecuente en literatura técnica reciente |
| El equipo | **Brigada** | — | Universal (Escoffier) |
| Ayudante | **Ayudante/auxiliar de cocina** | — | **«Auxiliar» es el término dominante en México y Colombia**; ES/AR usan «ayudante». Se dicen los dos |
| Friegaplatos | **Steward (friegaplatos / plonge)** | — | «Plonge» es galicismo asentado en España; **«steward» es el término comercial dominante en LATAM** (Winterhalter CO/CL/MX) |
| La fórmula del plato | **Ficha técnica (receta estándar)** | — | **Son sinónimos reales en México, no dos cosas distintas.** Decir los dos o se pierde al lector mexicano |
| El coste del plato | **Escandallo (costeo)** | — | «Costeo» es dominante en México y en el vocabulario de costes de toda Hispanoamérica. **Ya resuelto así en la Guía Food Cost: se mantiene la consistencia** |
| Pérdida de rendimiento | **Merma** | (desperdicio, cuando es comida tirada) | Sin variación. El matiz proceso/residuo se explica una vez |
| Punto de entrega a sala | **Pase** | (despacho / ventana) | «Pase» funciona en los 6 mercados; «despacho» es sinónimo ocasional |
| Preparación previa | **Mise en place** | — | Universal, ni siquiera se traduce |
| Pedido de mesa a cocina | **Comanda** | (orden, en habla coloquial mexicana) | Jerga de oficio asentada en los 6 mercados |
| La lista de platos | **Carta (menú)** | (platillo, para un plato suelto en México) | ⚠️ En España «menú» es más estrecho (menú del día); en México «menú» = la carta completa |

**Y lo que SÍ viaja sin cambios** —el núcleo defendible fuera de España—: la dirección de brigada, la ficha técnica de proceso, la planificación de producción, el protocolo de pase, los KPIs de cocina, la evaluación técnica, el APPCC como sistema, el desarrollo de carta con método y la relación cocina-sala-dirección. **Lo que NO viaja: el convenio, las tablas salariales, la PRL y el detalle normativo español.** La landing lo dice en la primera pantalla.

### 5.4 Las cinco buyer personas

1. **El recién ascendido — de segundo a jefe de cocina, restaurante independiente.** Objetivo: no fallar el primer año y ganar autoridad sobre quien ayer era compañero, sin volverse «el que grita». Llega con dominio técnico y **cero formación en gestión** — el hueco exacto que describe Castañeda. Capítulos que le convierten: **1, 2, 4, 9**.
2. **El chef ejecutivo de restaurante o pequeño grupo (2-5 locales).** Objetivo: retener equipo en un mercado sin gente (Xatruch/Camarena) y dejar de hacerlo todo él. Capítulos: **3, 7, 12, 18**.
3. **El chef corporativo / de hotel o cadena multi-outlet.** Objetivo: que cada cocina rinda igual sin estar él físicamente. Brigadas de 100-140 personas, con bufé, room service, banquetes y carta a la vez. Capítulos: **2, 5, 16, 20**. **Es el persona con más evidencia primaria del research y el único documentado en tres mercados.**
4. **El jefe de cocina de colectividades / catering / comedor de empresa.** Volumen alto y constante, margen y normativa ajustados. **Es el que activa CE-11 (comidas testigo) casi a diario.** Capítulos: **7, 13, 16**.
5. **El segundo de cocina con ambición — compra el manual ANTES del ascenso.** Capítulos: **1, 2, 4**.

### 5.5 Las seis objeciones, con respuesta honesta

| # | Objeción | Cómo se desmonta (sin marketing) |
|---|---|---|
| 1 | **«Ya hay plantillas de ficha técnica y escandallo gratis»** | **Es cierto y no se debe negar**: L5 localizó plantillas gratuitas activas en México, Colombia, Chile y España, y **nuestro propio Kit de Escandallos cuesta 12 €**. El manual **no puede vender «una ficha técnica»**. Vende el criterio: cuándo y cómo estandarizar, **cómo conseguir que el equipo SIGA la ficha** (no sólo que exista), el organigrama, los KPIs y la relación cocina-sala. Y remite explícitamente al kit para la herramienta suelta |
| 2 | **«Esto es para hoteles grandes, mi cocina es de 4 personas»** | ⚠️ **Menos refutada que en el hermano**: allí había una fuente explícita («pequeños y grandes comparten los mismos 7 problemas»); **aquí no se encontró testimonio de una cocina de 4-6 personas**. Se responde con honestidad estructural: **un ejemplo por escala en cada capítulo** (cocina de 4-6 / restaurante de 15-25 / hotel-grupo de 100+), sin fingir que todo aplica igual. Y el cap. 2 dice literalmente que **una brigada de 6 no está «mal» comparada con Escoffier** |
| 3 | **«Llevo años cocinando, ¿qué me va a enseñar un manual?»** | El manual **no compite en técnica culinaria** —eso lo cubren la plataforma y los recetarios— y hay que decirlo así de explícito en el copy. Compite en lo que la formación culinaria no da: números, personas, protocolos, normativa. Evidencia: Castañeda, que dirige 15 hoteles, tiene que **enseñar números** a cocineros técnicamente competentes |
| 4 | **«Es caro para lo que es»** | ⚠️ **Sin cita verificada para este producto** (a diferencia del hermano, donde había una reseña de Amazon con esa queja literal). Se contextualiza con precios oficiales: **tSpoonLab 95 €/mes = 1.140 €/año** · Gstock **desde 249 €/mes = 2.988 €/año** · el curso más barato del censo, **695 €** y caduca a los 3 meses · el Diploma del CIB, **7.714-9.075 €** |
| 5 | **«Mi gerente / el dueño no me va a dejar aplicar nada»** | El manual **no puede prometer autoridad que el lector no tiene**. Ofrece el cap. 19: **cómo llevar una propuesta al gerente o al propietario con la cifra de la semana**, que es lo único que un chef sin autoridad formal sí controla |
| 6 | 🔴 **«Yo no gestiono el negocio, sólo la cocina — esto es para el gerente»** | **Objeción específica de este producto y la más peligrosa**: el riesgo real es que el comprador **confunda este manual con su hermano**, que comparte línea, precio y formato. Se responde **desde el titular**, no desde la FAQ: «el Manager lleva el negocio, la sala y la ley; el Chef Ejecutivo lleva la cocina — la brigada, la producción, los estándares y la seguridad alimentaria». Y se aprovecha la pregunta recurrente de Quora («¿en qué se diferencian un jefe de cocina y un chef ejecutivo?») como gancho de FAQ |

### 5.6 Qué formato pide (y contra qué compite de verdad)

- **Excel es el estándar de facto** en los 4 mercados revisados. El producto **no compite contra software**: compite contra **Excel + WhatsApp + pizarra**. L5 no encontró **ninguna** fuente que sitúe un KDS o un ERP de F&B como herramienta instalada por defecto en el segmento objetivo (negocio independiente o mediano): sólo aparece en cadenas grandes.
- **WhatsApp con un riesgo documentado**: «cuando una reclamación se hace por WhatsApp y no queda registrada, el proveedor sabe que el restaurante **no tiene memoria sistematizada**».
- **Pizarra y bloc físico** son práctica confirmada para el *mise en place*, y forman parte del propio método: «los jefes de partida revisan junto al jefe de cocina las tareas del día siguiente» al cierre del servicio (elBulli Foundation).
- **Conclusión de formato:** capítulos **autoconclusivos por eje**, que se lean sueltos, cada uno con al menos un caso resuelto y una herramienta aplicable. El mismo patrón validado en la Guía Food Cost y en el Manual del Manager.

---

## 6. Competencia de pago: el hueco, confirmado producto a producto

### 6.1 El censo: 31 productos, ninguno completo

L1 censó **31 productos** (6 libros, 9 manuales/plantillas de pago único, 9 cursos y diplomas, 6 SaaS + 1 referencia cruzada), **20 con precio confirmado por URL y fecha**, y marcó «sin fuente (precio)» en el resto sin estimar ninguno. Puntuó **14** sobre 10 ejes.

> **Ningún producto del censo —ni siquiera el más caro, el Diploma del CIB a 9.075 €— tiene «Sí» simultáneo en Brigada + Estandarización + Compras + Carta con coste + Seguridad alimentaria + PRL + Normativa española actualizada + KPIs de cocina + Excel vivo + Pago único.**

**El mercado está partido en dos extremos sin solape:**

| Familia | Precio confirmado | Qué tiene | Qué le falta |
|---|---|---|---|
| **Libros de FP reglada** — *Gestión de la producción en cocina* (Altamar, **33,25 €**), *MF1065_3 Organización de procesos de cocina* (IC Editorial, **26,42 €**), *Cocina profesional* (Paraninfo, **16,62 €**) | 16,62-33,25 € | Proceso y APPCC con profundidad real | **Cero Excel. Cero liderazgo. Cero KPIs.** Escritos para un temario de certificado de profesionalidad, no para la mesa de un chef en ejercicio. **Ninguno demuestra estar actualizado al RD 1021/2022** |
| **Libros de puesto / soft skills** — *Jefe de cocina* (CEAC, **19,00 €**), *Competencias de un Chef* (sin fuente de precio: Amazon bloqueó la ficha) | 19,00 € | Perfil del puesto, liderazgo, gestión de presión | Cortos, sin normativa española, sin Excel |
| **El libro más caro del censo** — *Diseño y gestión de cocinas* (3.ª ed.) | **109,25 €** | Tratado técnico-normativo de instalaciones con apoyo gráfico | **Es de diseño de cocinas, no de dirección del día a día** |
| **Plantillas sueltas** — IngenieriadeMenu.com: fichas técnicas Excel **15,00 €** · Manual de Procedimientos Ayudante de Cocina **17,50 €** (29 págs Word, 5/5 con 2 reseñas) · hoja de producción diaria **2,95 €** · hoja de inventario **4,95 €** | 2,95-17,50 € | Excel real y usable; **es el único vendedor especializado real en español** | **Son átomos.** Una hoja, un manual de **un solo puesto** (y el más bajo de la brigada). Nunca un manual integral que los hile |
| **Cursos y diplomas** — Gastrouni **695 €** · BCC «Gestión desde la Cocina» **895 €** (⚠️ edición feb-2024, vigencia 2026 sin confirmar) · Cámara de Madrid **4.300 €** · Gasma **4.900 €** · CETT **5.152,50-6.222,50 €** · CIB **7.714-9.075 €** | **695 - 9.075 €** | Temario completo; el de Cámara de Madrid toca casi todo el mapa en 9 módulos | **Caducan.** Fecha de inicio y fin, presencial o semipresencial, y **ni un Excel que el alumno se lleve** (excepción parcial: Gastrouni, «20+ plantillas editables», pero 3 meses de acceso y su bloque de cocina es 1 de 4 áreas genéricas) |
| **SaaS** — tSpoonLab **95-110 €/mes** · MyChefTool **desde 99 €/mes** · Gstock **desde 249 €/mes** · Fichatec, Yurest, Haddock (bajo consulta) | **95-249 €/mes** = 1.140-2.988 €/año | Fichas técnicas, escandallos, APPCC, inventario, trazabilidad | **Cero brigada, cero personas, cero PRL, cero KPIs más allá del coste.** Su terreno es el dato transaccional, no la dirección. Y es **100 % recurrente sin fin** |

### 6.2 Los cinco hallazgos que valen por todo el análisis

1. **El mercado paga sistemáticamente MÁS por dirigir cocina que por dirigir sala.** En ningún punto de comparación resultó más barata la formación de cocina: Cámara de Madrid **4.300 €**, CETT **5.152,50-6.222,50 €**, CIB **7.714-9.075 €** — y en el censo del Manual del Manager los cursos generalistas de gestión estaban en **49-260 €**. Es un dato de posicionamiento, no de coste de producción (§10).
2. **Y sube.** La Cámara de Madrid pasó de **3.950 €** (edición anterior, vía Docenzia) a **4.300 €** (edición 2026-2027, fuente oficial). Nadie sube el precio de un curso que no se llena.
3. **Montarse el equivalente comprando átomos ya cuesta lo mismo que el manual entero.** Fichas técnicas 15 € + manual de un puesto 17,50 € + 2-3 hojas sueltas a 3-5 € = **45-55 €**… y no cubre ni una fracción de brigada, PRL, KPIs, comidas testigo ni normativa. **Es el argumento comercial más limpio del research.**
4. **Gumroad y Etsy están vacíos.** Gumroad **no devolvió ningún producto real en español** en 4 variantes de búsqueda (ficha técnica, manual de cocina, gestión de cocina, organigrama), con y sin comillas y con sinónimos LATAM; Etsy sólo tiene *printables* genéricos en inglés. **No es que la competencia barata sea dura: es que casi no existe.** El hueco de 9-30 € para un documento integral está completamente descubierto.
5. **El chef ejecutivo corporativo / multi-outlet no tiene NINGÚN producto dedicado.** Todo el censo —libros, cursos y SaaS— está escrito desde la cocina única: ni CIB ni CETT ni Cámara de Madrid mencionan gestión multi-establecimiento en su temario público. Y es el buyer persona con más evidencia primaria del research (§5.4, nº 3).

### 6.3 Qué hace bien la competencia y copiamos

1. **Basque Culinary Center dirige su curso explícitamente a «chef ejecutivo, director/a culinario de hoteles, chef de eventos, F&B Manager»** — valida por escrito el segmento hotelero/corporativo que nuestro producto cubre. *(Precio 895 €, ⚠️ de una edición fechada feb-2024: **no citar en copy sin reverificar**.)*
2. **Gastrouni incluye «20+ plantillas editables» dentro del curso** (695 €). Es la prueba de que el mercado valora el entregable, no sólo la clase.
3. **IngenieriadeMenu.com avisa en su ficha de que sus plantillas no funcionan en Sheets ni Numbers.** Nuestras convenciones de familia **prohíben `INDIRECT`, `COUNTA`, `PMT` y `OFFSET`** justamente para que sí funcionen: **es un argumento de landing verificable frente al competidor de plantillas más directo.**
4. **El CIB vende «pasar de cocinero a chef ejecutivo con visión de negocio»** — es la promesa exacta de nuestro producto, a 165× el precio.

### 6.4 Limitaciones del censo (declaradas)

**Amazon.es y Amazon.com.mx bloquearon TODO acceso hoy** (500 en WebFetch, reto Akamai `bm-verify` en curl) — más agresivo que el 4-sep, cuando Amazon.com.mx sí respondía. Los libros se verificaron en Casa del Libro, Paraninfo e IC Editorial. **No hay conteo propio de reseñas de ningún libro del censo.** Sin precio: *Competencias de un Chef*, 3 cursos de Hotmart, ESAH, Aprendum, ChefEjecutivo.com y 3 SaaS (Fichatec, Yurest, Haddock). El precio del CETT salió por la **URL en inglés** (la española y `programas.cett.es` devolvieron 404). Y **no se investigó el mercado angloparlante**: se buscó traducción al español de Le Cordon Bleu / CIA y sólo aparecieron recetarios, así que se documenta la ausencia, no una investigación completa.

---

## 7. Lo que ya vendemos y la FRONTERA: qué se cita y qué se construye

L6 abrió con `openpyxl` (`read_only`, un fichero cada vez, pico 63,6 °C) los xlsx vivos de `manual-manager-restaurante`, `kit-tareas`, `pack-appcc`, `kit-gestion-personal`, `kit-inventario`, `guia-food-cost` y `kit-escandallos`.

> **La conclusión del inventario, en una frase:** el catálogo resuelve muy bien **coste** (escandallo, rendimiento, food cost), **cumplimiento de local** (APPCC, alérgenos por plato, recepción) y **personas a nivel de negocio** (evaluación genérica, cobertura de turnos, legal laboral). **El eje que NINGUNA herramienta cubre es el criterio técnico de cocina**: cómo se hace un plato con estándar repetible, cuánto hay que producir hoy, cómo se evalúa la destreza real de la brigada, cómo se desarrolla la carta con método y cómo se documenta el organigrama de cocina.

### 7.1 La frontera con el Manual del Manager (55 €), que es la que decide si el producto existe

| Eje | **Manual del Manager** (negocio / sala / ley) | **Manual del Chef Ejecutivo** (cocina) |
|---|---|---|
| Organigrama | Las **6 áreas funcionales** del ALEH VI y los 3 grupos, para el negocio entero (cap. 01) | El **área 2.ª**: los **10 puestos de cocina** con sus funciones literales del art. 17, y la ficha de puesto descargable |
| Jornada y convenio | Marco general: 40 h, 12 h entre jornadas, registro de jornada, permisos, régimen disciplinario | **Sólo lo que el convenio dice de COCINA**: turnos partidos de 3-5 h, el descanso de 10 h en zona turística de Cataluña, manutención, plus de formación, ropa de trabajo, las 5 escalas salariales |
| Números | Cuadro de mando **financiero semanal**: ventas, food cost %, labor cost %, prime cost, ticket medio | Cuadro de mando **operativo de cocina**: merma por partida, tiempo de pase, incidencias de alérgenos, horas de cocina por cubierto. **Cero columnas financieras** |
| Personas | Selección, onboarding, evaluación **genérica**, quejas del cliente | **Evaluación técnica con prueba práctica** por competencia culinaria y por partida |
| Cumplimiento | Legal **transversal**: laboral, consumo, fiscal, ruido, música, terraza | **De cocina**: seguridad alimentaria desde la responsabilidad del chef, alérgenos en el pase, comidas testigo, vida útil, **PRL de cocina** |
| Servicio | Estándares de sala, reseñas, no-shows, hojas de reclamaciones | **El pase**, el control de calidad de lo que sale, y el cruce cocina↔sala↔dirección |

**Los dos comparten** el mismo caso modelado («La Encina», 12 personas, 6 estaciones) y el mismo marco laboral base, que este manual **cita por capítulo y no reescribe**. **La frase para la landing:** *«El Manager lleva el negocio. El Chef Ejecutivo lleva la cocina. Si diriges las dos cosas, necesitas los dos.»*

### 7.2 Los seis riesgos de canibalización, y la regla de no-solape de cada uno

| Par en riesgo | Por qué NO son lo mismo (verificado celda a celda) | Regla |
|---|---|---|
| `matriz-formacion-polivalencia.xlsx` (Manager) ↔ **evaluación técnica** | La matriz mide **cobertura**: «¿puede SOSTENER la estación en un servicio lleno?», niveles 0-3 **sin prueba**. Es la herramienta de planificación de turnos del manager | La nueva **no vuelve a preguntar «¿puede cubrir?»**. Su salida (plan de desarrollo individual) **remite por referencia** a la hoja `Plan de Cross-Training` de la matriz |
| `BONUS-01-registro-formacion.xlsx` (APPCC) ↔ plan de formación técnica | El registro APPCC es **cumplimiento** con caducidad vía `TODAY()`: certificado, entidad, estado VIGENTE/RENOVAR/CADUCADO | **No se construye un tercer libro de formación** (precedente D3 del Manager: «la hoja de briefing desaparece, existe 20 veces en el catálogo»). Vive como **hoja** dentro de la evaluación técnica |
| `05-control-mermas.xlsx` (Inventario) ↔ mermas por partida | Mide merma por **producto/categoría de compra** (10 categorías fijas) sobre el total de **compras del mes**. Sin partida, sin producción diaria, sin responsable | El cuadro de cocina **no reconstruye el registro**: toma un **total agregado que el usuario copia** desde su propio registro, y lo divide por la **producción de esa partida**. Nunca vuelve a pedir fecha/producto/motivo línea a línea |
| `ficha-escandallo-base.xlsx` (Guía Food Cost) ↔ **ficha técnica de proceso** | El escandallo es 100 % coste (ingrediente, cantidad neta/bruta, merma, precio, IVA, PVP, food cost). **Cero celdas de pasos, técnica, alérgenos, temperatura de servicio o conservación** | La ficha de proceso **no recalcula coste**: enlaza por fórmula externa a la celda ya calculada, con `IFERROR(…,"completa con tu escandallo")` si el comprador no tiene la Guía. **Se venden como PAREJA**: «el escandallo dice cuánto cuesta, la ficha dice cómo se hace» |
| `auditoria-interna-servicio.xlsx` (Manager) ↔ auditoría de cocina | La del manager dice **literalmente** en sus Instrucciones que «excluye APPCC/sanidad a propósito (remite al Pack APPCC)» y puntúa 6 áreas de **sala** | La de cocina puntúa áreas distintas (orden y mise en place, aplicación de fichas, mermas por partida, PRL, alérgenos en el pase) y **remite igualmente al Pack APPCC** para lo sanitario |
| `BONUS-01-briefing-servicio.xlsx` (Kit de Tareas) ↔ handover de cocina | El briefing pre-servicio ya cubre reservas, 86s, alérgenos y especiales, con responsable «jefe de sala o manager» | **Se descarta como libro.** Si hace falta el matiz de cocina (estado del *mise en place*, incidencias de producción), es **una fila más** en la lista de producción diaria |

### 7.3 Lo que se CITA (cross-sell) y no se construye

| Ya existe en | Decisión |
|---|---|
| **Manual del Manager (55 €)** — negocio, sala, jornada, contratación, quejas, cumplimiento transversal | ❌ **Se cita.** Frase del cap. 01: «quien dirige el negocio completo, no sólo la cocina, necesita los dos» |
| **Pack APPCC (14 €)** — 21 xlsx de registros diarios (temperaturas, limpieza, plagas, trazabilidad, matriz de alérgenos por plato, `15-guia-inspeccion-sanidad`) | ❌ **Se cita.** El manual da el **criterio**; el pack da el **papel que hay que rellenar cada día**. La auditoría de cocina excluye lo sanitario a propósito |
| **Kit de Escandallos (12 €)** y **Guía Food Cost (55 €)** — escandallo, rendimiento, mermas por ingrediente, ingeniería de menú | ❌ **Cross-sell explícito.** La ficha de proceso enlaza el coste, no lo recalcula |
| **Kit de Tareas (12 €)** — `02-partidas-cocina.xlsx` (checklists por partida, con alérgenos y anisakis ya integrados) | ❌ **Se cita.** Es un checklist de tareas del día (¿se hizo o no?); la planificación de producción es una **proyección cuantitativa** (cuánto producir). Se imprimen juntos sin repetir una columna |
| **Kit de Inventario (14 €)** — recepción con trazabilidad, mermas por producto, punto de pedido | ❌ **Se cita** |
| **Kit de Gestión de Personal (14 €)** — cuadrante, registro, coste laboral, onboarding, evaluación genérica | ❌ **Se cita.** El manual explica **cuándo usar cada evaluación**: comportamiento → el kit; oficio → el libro nuevo |

### 7.4 El pipeline se reutiliza al 100 %, sin tocar una línea de código

- **`motor.py`** — los libros usan `f()`, `val()`, `verde()`, `dv_lista()`, `semaforo_isnumber()`, `version_line()`, `hoja_instrucciones()` y `PARAMETROS` tal cual. **Cero helpers nuevos.**
- **`documentos.py`** — `tipo_doc`, `tipo_doc_art`, `tipo_doc_dem` y `categoria_doc` **ya están parametrizados** desde la D19 del Manager (líneas 1003, 1039, 1943). Basta con que el guion nuevo rellene esas claves. **Cero cambios de código.**
- **`dump_prompts.py`** y **`check_bloque.py`** — genéricos por `--producto <pid>`.
- **`fase8g-manual-manager-blog.py`** — es la plantilla a clonar, con `PRODUCTO`/`HOY`/`PRIORIDAD_SUSTITUIR`/`NUNCA` propios.
- **`robots.txt`** — nada que tocar: el comodín `manual-*` ya cubre el slug (verificado en los 5 bloques).
- **A crear:** la SPEC, `guion_manual_chef_ejecutivo.py` con su `NO_COMUN` propio, y `manual-chef-ejecutivo/datos_ejemplo.py` que **debe IMPORTAR** —no reinventar— `RESTAURANTE`, `ESTACIONES`, `POLIVALENCIA` y `PLANTILLA` de `manual-manager/datos_ejemplo.py` (que a su vez importa de la Guía Food Cost), para que los tres productos cuadren sin inventar una sola cifra de «La Encina».

---

## 8. La lista DEFINITIVA de entregables

### 8.1 Dimensionado del manual, con calibración MEDIDA (no estimada)

Medido hoy con PyMuPDF sobre los PDF que se venden ahora mismo:

| Producto vivo | Páginas | Palabras | Palabras/página |
|---|---|---|---|
| Guía Food Cost | 95 | 50.265 | **529** |
| Manual del Manager | 77 | 41.235 | **536** |
| Bonus del Manager | 28 | 11.530 | **412** |
| Bonus de la Guía | 32 | 12.986 | **406** |

**Dos lecciones para dimensionar:**

1. **El cuerpo calibra a ~530 palabras/página; el bonus a ~410** (más tablas, menos texto corrido). La síntesis del Manager presupuestó el bonus en 7.500 palabras y salieron **11.530**: usar 530 para el bonus subestima un 30 %.
2. **El guion se sobrepasa siempre.** El Manager presupuestó 1.400-1.600 palabras/capítulo (≈30.000 en total) y entregó **41.235**, es decir **~2.060/capítulo, un +30 %**. Presupuestar con eso a la vista.

| Entregable | Presupuesto de guion | Salida realista (con el +30 % medido) | Gate interno | Qué publica la landing |
|---|---|---|---|---|
| **Manual, 20 capítulos** | 1.600-1.800 palabras/cap. (los 4 legales —13, 14, 16, 17— a 2.000) ≈ **34.000 palabras** | **40.000-44.000 palabras → 75-83 páginas** | `paginas_prometidas: 75` · `min_palabras_cap: 1.300` | **La cifra MEDIDA tras construir** (decisión D17 de la familia). Nunca la prometida |
| **Bonus, 12 situaciones resueltas** | 700-850 palabras/situación + 1 tabla ≈ **9.500 palabras** | **11.000-12.500 palabras → 27-30 páginas** | `paginas_prometidas: 25` · `min_palabras_cap: 550` | Ídem |

### 8.2 El bonus: **«12 situaciones resueltas en cocina»** — elegido y argumentado

| Opción | Veredicto |
|---|---|
| **Recetario o fichas técnicas de ejemplo** | ❌ **Descartada.** Canibaliza los recetarios de la plataforma y el Kit de Escandallos, y **contradice la propia promesa del manual**, que dice explícitamente que no compite en técnica culinaria (objeción 3). Sería la pieza más fácil de criticar |
| **Cuaderno de guiones de conversación** | ⚠️ **No como bonus suelto.** Mismo riesgo que en el hermano: un cuaderno de guiones aislado se lee como relleno. Se **absorbe**: las situaciones que necesitan una conversación traen el guion literal dentro |
| **12 situaciones resueltas en cocina** | ✅ **Elegida** |

**Por qué:** reutiliza el molde exacto ya validado dos veces (mismo `BONUS` del guion, mismos gates, coste conocido); es la respuesta directa a la objeción medida en el hermano («temas tratados demasiado básicos, parece un conjunto de entradas de blog»); y **es lo que las ofertas describen como el trabajo real** — 11 de 17 piden «supervisar y coordinar la operación diaria», que es exactamente resolver situaciones.

**Las 12** (cada una: situación con datos del pack · qué NO hacer · protocolo paso a paso · la norma que aplica con su id y su fecha de verificación · la herramienta del pack que se usa · y el guion literal de la conversación cuando la hay):

1. Un jefe de partida se va a mitad de temporada y sólo él sabe la partida de pescados.
2. Un comensal declara una alergia cuando el plato ya está montado.
3. Sanidad se presenta sin avisar en mitad del servicio.
4. Un banquete de 120 personas: qué hay que guardar, cómo y durante cuánto (CE-11).
5. El pase se descontrola un viernes: 40 comandas y 25 minutos de espera.
6. El plato estrella sale distinto según quién esté de turno.
7. La merma de la partida de fríos se dispara tres semanas seguidas.
8. El proveedor cambia el calibre del producto sin avisar y el escandallo se rompe.
9. Un cocinero se corta con la cortadora de fiambre: qué obliga la ley antes y después (CE-23, CE-25, CE-26).
10. Hay que renovar la carta de temporada en tres semanas.
11. El propietario quiere quitar de la carta un plato que a ti te da margen.
12. Un segundo de cocina asciende a jefe: los primeros 30 días.

### 8.3 Los 8 libros de Excel — evaluación de la propuesta de L6 y propuesta final

**Confirmo los 8 de L6 y los corrijo en tres puntos**, todos con la misma lógica: (a) el libro más flojo se recarga con el hallazgo más diferencial del research; (b) el más decorativo se convierte en herramienta; (c) el bloque legal más nuevo consigue soporte sin añadir un noveno libro.

| # | Fichero | Hojas | Entradas (celda verde) | Salidas / fórmulas | Qué decisión permite | Origen en el motor |
|---|---|---|---|---|---|---|
| **1** | **`cuadro-de-mando-cocina.xlsx`** ⭐ | Instrucciones · Parámetros · Semana (52 filas ISO) · **KPI y Definiciones** | Objetivos de KPI de cocina por tipo de carta; por semana: mermas por cada una de las 6 partidas, producción estimada por partida, tiempos de pase medidos por muestreo, incidencias de alérgenos y gravedad, horas de cocina trabajadas, cubiertos servidos, platos devueltos/retrabajados | % de merma **por partida** (merma ÷ producción de esa partida), horas de cocina por cubierto, tendencia de tiempos de pase con semáforo `ISNUMBER` contra el objetivo de la casa, incidencias por 1.000 cubiertos. La hoja `KPI y Definiciones` da fórmula, unidad y **el error típico** de cada indicador | **Qué partida se come el margen**, y si el problema es de producto (food cost, que vive en el Manager) o de eficiencia de cocina | `cuadro-de-mando-semanal-manager!Semana` (52 filas ISO y semáforo). ⚠️ **NO repite ni una columna financiera**: ventas, food cost %, labor cost % y prime cost se **citan por referencia** en Instrucciones |
| **2** | **`planificacion-produccion-semanal.xlsx`** ⭐ | Instrucciones · Previsión de Cubiertos · Producción por Partida (6 tablas) · **Lista de Producción Diaria** (imprimible) · Ajuste por Desviación | Cubiertos previstos por servicio, % de mix de venta por plato, producción unitaria por ración (de la ficha técnica), stock ya elaborado | Cantidad a producir = cubiertos × % mix − stock; materia prima total = cantidad × cantidad bruta por ración (enlazada al escandallo, no recalculada); **alerta de sobreproducción** si la lista del día anterior quedó con sobrante | Cuánto producir HOY en cada partida en vez de producir «por costumbre» — que es **la causa raíz nº 1 del propio `Plan de Acción` de `05-control-mermas.xlsx`** | `PARAMETROS` + `dv_lista`. **Cierra el hueco de L2 §3.4**: la única herramienta equivalente del mundo es un SaaS en inglés |
| **3** | **`ficha-tecnica-proceso.xlsx`** ⭐ | Instrucciones · Ficha (plantilla a duplicar) · Ficha (ejemplo relleno) · Índice de Fichas | Plato, familia, **pasos numerados**, técnica, tiempos, punto de cocción, temperatura de servicio, montaje con hueco de foto, 14 columnas de alérgenos S/T/N, conservación y **vida útil en cámara y congelador** | **Ninguna de coste**: «coste por ración» y «food cost real» se enlazan por fórmula externa a `ficha-escandallo-base.xlsx`, con `IFERROR(…,"completa con tu escandallo")` | **Que el plato salga igual lo haga quien lo haga.** Es el estándar de proceso que **no existe en ningún fichero del catálogo ni en la SERP española** | `verde()` + `dv_lista()`. Cero superposición con el escandallo |
| **4** | **`organigrama-fichas-puesto-cocina.xlsx`** ✏️ *ampliado* | Instrucciones · Organigrama de Cocina · **Fichas de Puesto (JD)** · Matriz RACI Cocina↔Sala↔Dirección | Nombres y puestos de la plantilla; lista editable de decisiones tipo | Sin cálculo: validación `dv_lista` para R/A/C/I y formato condicional por rol. **Las Fichas de Puesto vienen sembradas con las funciones LITERALES del art. 17 del ALEH VI** (los 10 puestos) más una columna verde para las funciones propias de la casa | Quién decide qué cuando cocina, sala y dirección no coinciden (autorizar un 86, aprobar una ficha nueva antes de subirla a carta, una incidencia de alérgeno) — **y darle a cada persona su descripción de puesto por escrito** | ✏️ **Mi corrección a L6:** como matriz RACI a secas era la pieza más decorativa de las 8. Con las fichas de puesto pasa a **cerrar el hueco nº 12 de L2** («JD descargable por rol de cocina: **0 de 20 fuentes**») y a ser el único sitio del mercado donde esas funciones están en una plantilla editable |
| **5** | **`evaluacion-tecnica-brigada.xlsx`** ⭐ | Instrucciones · **Rúbrica de Competencias Técnicas** · Prueba Práctica · Plan de Desarrollo Individual · Histórico | Puntuación 1-5 **por prueba práctica** (no autoevaluación) en: cortes y manejo de cuchillo, cocciones, fondos y salsas, emplatado y montaje, higiene de manipulación, conocimiento de la ficha técnica, gestión de la merma de su partida. Pesos editables por puesto | Media ponderada que ignora N/A, semáforo de nivel, histórico con tendencia, columna «próxima estación a aprender» que **remite** (no repite) a `matriz-formacion-polivalencia!Plan de Cross-Training` | A quién promocionar, a quién formar en qué y quién no supera el periodo de prueba en su partida — **con una prueba puntuada, no con una opinión** | `06-evaluacion-desempeno!Ficha Evaluación` (media condicional e histórico). Cierra el hueco nº 6 de L2 |
| **6** | **`desarrollo-carta-control-calidad.xlsx`** | Instrucciones · Calendario de Temporada · Registro de Pruebas de Plato · **Control de Calidad del Pase** | Hitos por plato nuevo con fecha objetivo (prueba → coste → ficha → formación → lanzamiento); resultado y coste de cada prueba; muestreo del pase: temperatura de emplatado, tiempo de espera, conformidad con la ficha, devoluciones | Días hasta el próximo hito, % de conformidad del pase, **alerta si un plato lleva más de N días «en prueba» sin ficha técnica cerrada** | Que la carta se renueve con **método** en vez de «porque lo dice el chef», y que lo que sale del pase sea lo que dice la ficha | Patrón de fechas de `Plan de Cross-Training` y `Calendario y Vencimientos`. **Alimenta la columna de tiempos de pase del libro 1** |
| **7** | **`banquetes-eventos-y-desperdicio.xlsx`** 🔴 ✏️ *recargado* | Instrucciones · **Registro de Comidas Testigo** · Jerarquía de Prevención · Registro de Donaciones y Doggy Bag · Panel de Cumplimiento | Nº de comensales del encargo (dispara la obligación), plato y lote de la muestra, fecha y hora de recogida, ubicación y temperatura, fecha de destrucción; cantidad donada/mes, doggy bags entregados, m² del local y forma jurídica | **Alerta automática «COMIDA TESTIGO OBLIGATORIA» si el encargo supera 40 comensales** (CE-11); cuenta atrás de los 7 días de conservación; semáforo de cumplimiento por apartado del art. 6 de la Ley 1/2025 con la exención bien acotada (CE-33); cada fila con norma, URL y fecha de verificación | **Si este encargo dispara la obligación de comidas testigo, y qué se hace legalmente con el excedente** | ✏️ **Mi corrección a L6:** su libro 7 era sólo el plan de desperdicio, la pieza más floja de las 8 (el Manager ya explica la Ley 1/2025 en texto y la mayoría de compradores están **exentos** del plan). Al meter dentro **CE-11**, el hallazgo más diferencial del research, la pieza más débil pasa a ser la que sirve a las buyer personas 3 y 4 |
| **8** | **`auditoria-interna-cocina.xlsx`** ✏️ *sembrado* | Instrucciones · Auditoría · Resumen por Área · Histórico | ~50 puntos en 5 áreas: orden y *mise en place* · aplicación de fichas técnicas · mermas por partida · **PRL de cocina** · alérgenos en el pase. Peso por punto, puntuación 0-5, observación, fecha y auditor | `SUMPRODUCT(peso;puntuación)/SUM(peso)`, % por área, semáforo, tendencia entre visitas | Puntuar la disciplina de cocina de forma **repetible y comparable**, y verla junto a la auditoría de servicio del Manager para tener las dos caras | ✏️ **Mi corrección a L6:** el área de PRL se **siembra con los cinco puntos legales verificados** —temperatura 14-25 °C (CE-21), suelo antideslizante (CE-22), EPI de corte gratuito (CE-23), resguardos de máquinas (CE-25), revisión documentada de equipos (CE-26)—, cada fila con su norma y su URL. **Así el bloque de PRL tiene herramienta sin añadir un noveno libro.** EXCLUYE limpieza, plagas y temperaturas: remite al Pack APPCC, igual que hace su hermano de servicio |

**Descartes confirmados** (para no pasar de 8 y no duplicar): *handover / briefing de cocina* (redundante con `BONUS-01-briefing-servicio.xlsx`; precedente D3) y *plan de formación técnica independiente* (redundante con el `Plan de Cross-Training` ya existente; absorbido como hoja del libro 5). *Calendario de cartas* + *registro de pruebas* + *control de calidad del pase* se fusionan en el libro 6.

**Convenciones obligatorias de familia** (idénticas a la SPEC del Manager §2.2, no negociables): helpers de `motor.py`; hoja «Instrucciones» primero con «celdas verdes = editables», línea de versión, bio anclada y nota de desproteger; **cero constantes tecleadas dentro de una fórmula**; `IFERROR(...;"")` y `ISNUMBER` en semáforos; «sin dato» = `""`, nunca `0`; **prohibido `INDIRECT`, `COUNTA`, `PMT` y `OFFSET`**; formatos `#,##0.00 €` / `0.0 %` / `dd/mm/yyyy`; A4 con `print_setup`; metadata `author='AI Chef Pro'`; datos de ejemplo desde un `datos_ejemplo.py` que **importa** los del Manager. Cada celda con dato legal lleva nota **«Verificado el 06-09-2026 · norma · URL»**. Tras generar: `inject_cache.py` + verificación `data_only` de cada fórmula registrada + `mapa-<libro>.json`.

### 8.4 Resumen del paquete

**1 manual (PDF + DOCX) de 20 capítulos · 1 bonus (PDF + DOCX) de 12 situaciones · 8 libros de Excel con fórmulas vivas.** Pago único, acceso vitalicio al dashboard, actualizaciones incluidas.

---

## 9. Índice propuesto: 20 capítulos

Cada capítulo irá con guion cerrado en `guion_manual_chef_ejecutivo.py` (epígrafes, cifras referenciadas a celda de xlsx o a ids `CE-*` / `CS-*` / `MM-*`, tablas exigidas y prohibiciones). **Ninguna cifra entra si no sale de una celda o de un id.**

| # | Título | Contenido obligatorio (2-3 líneas) | Tabla desde | ids |
|---|---|---|---|---|
| **01** | **Qué es exactamente un chef ejecutivo (y para quién es este manual)** | La taxonomía que la SERP no fija: chef ejecutivo / jefe de cocina / chef corporativo / sous chef / jefe de partida, con el área 2.ª del ALEH VI. **La frontera con el Manual del Manager en la primera página.** Mapa «problema → capítulo → herramienta» con los 8 libros; tabla «qué incluye este pack / qué es cross-sell»; y qué **NO** vas a encontrar aquí (no es un recetario, no es un curso de técnicas, no es una guía de apertura) | `organigrama-fichas-puesto-cocina!Organigrama` | MM-14 |
| **02** | **La brigada real: los 10 puestos del convenio y el organigrama que sí tienes** | Las funciones **literales** del art. 17 para los 10 puestos; los **tres niveles de delegación** que el propio convenio distingue (cualificado autónomo / con supervisión / sin cualificación); **por qué la brigada de Escoffier de 15 puestos no aplica a una cocina de 6** y cómo se colapsa sin perder responsabilidades; el nivel del chef corporativo, que **no está en el convenio** | `…!Fichas de Puesto (JD)` | MM-14 |
| **03** | **Lo que tu convenio dice de la COCINA (y no del resto del restaurante)** | Movilidad funcional del art. 19: libre dentro del grupo, con causa y tope de 6/8 meses fuera de él, con formación garantizada al cambiar de área; categoría superior (4 meses seguidos / 6 alternos) e inferior (12 días / 20 alternos); **turnos partidos de cocina de 3-5 h y el descanso reducido a 10 h en zona turística de Cataluña**, con sus 6 exclusiones; manutención (57,82 € Madrid / 59,21 € Cataluña); plus de formación; ropa de trabajo como suplido; **la escalera de 5 niveles y el +49,9 % Barcelona-Madrid** | Tablas §3.4 + `…!Fichas de Puesto` | MM-14, MM-15 |
| **04** | **Mandar en una cocina sin gritar** | Autoridad formal vs real; delegar por nivel del convenio, no por confianza; **«si les das voz, los equipos se apasionan»** y «tratar mal al personal es hacer una mala gestión» (Castañeda); la jerarquía piramidal que motiva (Sánchez López); señales tempranas de quemado; la conversación difícil; el ascenso de compañero a jefe | — | — |
| **05** | **La ficha técnica de proceso: que el plato salga igual lo haga quien lo haga** | Qué lleva y qué NO (**el coste vive en el escandallo**); pasos, técnica, tiempos, punto, montaje con foto, alérgenos, temperatura de servicio, conservación; **versión y fecha de revisión** como campos obligatorios; por qué la plantilla de 5 campos que circula gratis no sirve | `ficha-tecnica-proceso!Ficha` | CE-06, CE-13 |
| **06** | **Estandarizar de verdad: por qué la ficha existe y nadie la sigue** | El problema no es escribir la ficha, es **hacerla vinculante**: quién la aprueba, dónde vive, cómo se forma en ella, cómo se audita en el pase y qué pasa cuando el proveedor cambia el producto; el control de versiones que evita que convivan tres versiones del mismo plato | `desarrollo-carta-control-calidad!Control de Calidad del Pase` | — |
| **07** | **Mise en place y planificación de producción** | La diferencia entre tener el puesto montado y **saber cuánto hay que producir**; previsión de cubiertos desde reservas e histórico; cantidad a producir = cubiertos × mix − stock elaborado; la lista de producción diaria imprimible; el ajuste por desviación; **producir «por costumbre» es la causa raíz nº 1 de merma de nuestro propio kit** | `planificacion-produccion-semanal!Producción por Partida` | — |
| **08** | **El pase: protocolo, no cultura** | Roles (quién canta, quién marcha, quién despacha), secuencia de comandas, **gestión del 86** y quién lo autoriza, tiempos objetivo por familia de plato, cómo se mide sin cronómetro (muestreo); por qué **10 reglas de actitud no son un procedimiento** | `cuadro-de-mando-cocina!Semana` (tiempos) | CS-22 (sin fuente: se mide, no se cita) |
| **09** | **Los KPI que son de cocina (y los que no)** | Los siete que sí: merma por partida, tiempo de pase, incidencias de alérgenos, horas de cocina por cubierto, cumplimiento de ficha, retrabajos/devoluciones, rotación de brigada. **Los que son de sala, marketing o finanzas y no le tocan al chef**; dónde acaba este manual y empieza la Guía Food Cost (food cost e ingeniería de menú) | `cuadro-de-mando-cocina!KPI y Definiciones` | MM-41 + CS-19 |
| **10** | **Mermas y rendimiento: tu cifra, no la de un blog** | Merma de proceso vs desperdicio; merma por **partida** (contra la producción) frente a merma por producto (contra las compras, que ya cubre el Kit de Inventario); **por qué en este manual no hay ningún benchmark de merma** y cómo se calcula el propio en cuatro semanas | `cuadro-de-mando-cocina!Semana` | ⛔ CS-15, CS-16, CS-17 en lista negra |
| **11** | **Compras y especificaciones desde la cocina** | La especificación técnica que el chef le da al proveedor (calibre, corte, grado de maduración, formato de envío, tolerancias), no sólo el precio; el papel del **encargado de economato** según el art. 17 («elaborar peticiones de ofertas, evaluación y recomendación de adjudicaciones»); **los contaminantes vinculan al COMPRAR** (Rgto. 2023/915), no al elaborar; qué guardar del albarán para la trazabilidad | (cross-sell `kit-inventario/04`) | CE-18, CE-09, CE-16 |
| **12** | **Desarrollo de carta y menús de temporada con criterio de coste** | El método: probar → costear → documentar → formar → lanzar, con fecha por hito; qué se prueba y cómo se registra; qué decisión es del chef y cuál es de dirección; **frontera explícita: la ingeniería de menú vive en la Guía Food Cost**, aquí está el proceso de desarrollo | `desarrollo-carta-control-calidad!Calendario de Temporada` | — |
| **13** | **Seguridad alimentaria: de lo que respondes tú, no el propietario** | **Cultura de seguridad alimentaria como obligación de la DIRECCIÓN** (Cap. XI bis) y qué significa demostrarla; APPCC con **responsable designado**; temperaturas vigentes (4/8/−18/74 °C y 60→10 en 2 h); **anisakis −20 °C/24 h o −35 °C/15 h** y el justificante del proveedor; trazabilidad un paso atrás y adelante; las **tres fechas** de la etiqueta al congelar; **qué NO cuenta como «elaboración propia»** | (cross-sell `pack-appcc`) | CE-02, CE-10, CE-12, CE-13, CE-14, CE-09, MM-29 |
| **14** | **Alérgenos desde dentro de la cocina** | **No hay un «capítulo de alérgenos» en el 852/2004**: es el punto 9 del Cap. IX; los 14 de declaración obligatoria; **el cartel «consulte al personal» no basta** sin soporte escrito accesible; contaminación cruzada de equipo y recipientes; «sin gluten» ≤20 mg/kg y «muy bajo» ≤100; el alérgeno que llega al pase con el plato montado; protocolo ante una reacción | `ficha-tecnica-proceso!Ficha` (14 columnas) + `pack-appcc/08` | CE-01, CE-06, CE-07, MM-31 |
| **15** | **Vida útil, envasado al vacío y lo que la ley NO dice** | **No existe cifra legal de días** para una elaboración propia no congelada; cuándo obliga el **estudio de vida útil** (RTE que favorece *Listeria*); V gama y la recomendación de <4 °C, idealmente <3,3 °C (⚠️ fiabilidad media, fuente secundaria); **acrilamida: nivel de referencia ≠ límite sancionable**, y el reglamento no nombra a los restaurantes; fritura por debajo de 175 °C y aceite con <25 % de polares | `ficha-tecnica-proceso!Ficha` (conservación) | CE-08, CE-37, CE-35, CE-19, CE-20, CE-17 |
| **16** | **Comidas testigo, banquetes y qué se hace con el excedente** 🔴 | **La obligación que casi nadie conoce**: quién está obligado, el umbral de **más de 40 personas**, los **100 g**, los **7 días** y las temperaturas; cómo se recoge cuando elaboración y servicio están en sitios distintos; y después, la **jerarquía legal de 6 niveles** del excedente, el doggy bag universal desde 2022, el convenio de donación y **de qué está exento tu local de verdad** (1.300 m² sólo del apartado 4; microempresas fuera; ojo al conjunto con el mismo CIF) | `banquetes-eventos-y-desperdicio!Registro de Comidas Testigo` | **CE-11**, CE-31, CE-32, CE-33, CE-34, MM-36 |
| **17** | **PRL en la cocina: lo que la evaluación de riesgos convierte en obligación** | **No existe una «ley del uniforme»**: existe la suma de higiene alimentaria (vestimenta adecuada, limpia y protectora) **y** PRL (EPI **gratuito** por uso regular de cuchillos y por suelo húmedo); temperatura legal **14-25 °C**; suelos antideslizantes; resguardos en picadoras y cortadoras; comprobaciones periódicas documentadas de los equipos; **el mito de los 25 kg**; y la siniestralidad real: muchos accidentes, pocos mortales | `auditoria-interna-cocina!Auditoría` (área PRL) | CE-05, CE-21 a CE-30, CS-01 |
| **18** | **Formar y evaluar a la brigada: cobertura no es competencia** | La diferencia entre «¿puede cubrir la estación?» (matriz del Manager) y «¿lo hace bien?» (rúbrica con prueba práctica); las 7 competencias técnicas y sus pesos por puesto; el plan de desarrollo individual que alimenta el cross-training; la formación de manipuladores **por puesto y sin carné**; el plus de formación del convenio; **y el 20,14 € frente a 76,49 € del INE** | `evaluacion-tecnica-brigada!Rúbrica` | MM-43, MM-30, CE-04 |
| **19** | **Cocina, sala y dirección: quién decide qué** | La matriz RACI de las decisiones que cruzan: cambio de carta, 86 de un plato, incidencia de alérgeno, compra fuera de escandallo, ficha técnica nueva; la comanda mal cantada y la alergia que no llega a cocina como **problema de sistema, no de personas**; **cómo llevar una propuesta al gerente o al propietario con la cifra de la semana** (responde a la objeción 5) | `organigrama-fichas-puesto-cocina!Matriz RACI` | — |
| **20** | **Varias cocinas a la vez — y los 90 días siguientes** | El chef ejecutivo corporativo: estandarizar entre unidades, formación en cascada (él forma a los jefes de cocina, no a los cocineros), **KPIs comparables** entre outlets, y bufé + room service + banquetes + carta a la vez; **dos convenios distintos si hay centros en dos comunidades**; y el cierre: qué se mide en el mes 0 y en el mes 3, con responsable y fecha | `cuadro-de-mando-cocina!Semana` + `auditoria-interna-cocina!Histórico` | MM-15 |

**Cobertura de los ejes anunciados en el hub desde mayo** («Responsabilidades, KPIs, protocolos, checklists y evaluación de equipo de cocina»): responsabilidades (1, 2, 3, 13, 17, 19) · KPIs (9, 10, 20) · protocolos (5, 6, 7, 8, 13, 14, 16) · checklists (8, 12, 17 + el libro 8) · evaluación de equipo (18, 4).

---

## 10. Precio y ancla

### 10.1 La escalera real del catálogo (46 productos, contados hoy en `products-catalog.ts`)

| Franja | Nº | Productos |
|---|---|---|
| 9 € | 1 | eBook Pro Prompts |
| **12 €** | 13 | Kit de Escandallos + 12 kits de tareas por concepto |
| **14 €** | 8 | Kit de Tareas, Pack APPCC, Kit de Inventario, Kit de Gestión de Personal + 4 kits de tareas |
| 18 / 18,50 € | 2 | kit-tareas-chef-privado · kit-tareas-hotel |
| 24 € | 1 | Guía Dark Kitchen |
| 29 / 35 € | 5 | 5 planes de negocio |
| **39 €** | 1 | Kit Plan Financiero |
| 45 € | 4 | 4 planes de eventos |
| **55 €** | **3** | **Guía Food Cost + Ingeniería de Menú · Manual del Manager de Restaurante · Plan Coctelería** |
| **65 €** | **6** | 6 guías «Cómo Montar» (casual, panadería-obrador, japonés, mexicano, nikkei, peruano) |
| 85 € | 1 | Guía Restaurante Gastronómico (22 caps, 119 págs, 18 xlsx) |
| 89 € | 1 | Mega Pack de Tareas |

### 10.2 Recomendación: **55 €**

**Cinco argumentos, uno por línea:**

1. **John ya decidió el escalón de esta línea, hace dos días.** La síntesis del Manual del Manager recomendó **65 €** y la SPEC lo firmó en **55 €** (decisión D1). La línea «Manuales operativos» **nació a 55 €**. Poner el segundo manual a 65 € dice que el primero vale menos, y el hub los enseña uno al lado del otro.
2. **El bundle sólo funciona con paridad, y es el argumento comercial más fuerte que sale del research.** «Los dos lados de la dirección —el negocio y la cocina— por 110 €: **menos del 16 % del curso más barato del censo** (Gastrouni, 695 €, y caduca a los 3 meses).» Con precios asimétricos ese mensaje se cae.
3. **El ancla externa aguanta igual de bien:** **tSpoonLab 95 €/mes = 1.140 €/año** (precio oficial, `tspoonlab.com/restauracion`, 2026-09-06) · **Gstock desde 249 €/mes = 2.988 €/año** · **MyChefTool desde 99 €/mes**. 55 € es **pago único** frente a un gasto recurrente sin fin, y **menos de lo que cuesta un mes** de cualquiera de los tres.
4. **La franja de 65 € ya tiene dueño y otra lectura.** Son **6 guías «Cómo Montar»**, y el hub las lee como «abrir un formato concreto». Meter ahí un manual de dirección ensucia esa franja y no gana nada.
5. **Y montarse el equivalente por piezas ya cuesta 45-55 €** (fichas técnicas 15 € + manual de un puesto 17,50 € + 3 hojas sueltas), sin brigada, sin PRL, sin KPIs, sin comidas testigo y sin normativa. **55 € por el conjunto completo es defendible sin retórica.**

**Sin `priceOld` ni `discountBadge`** (decisión D2 de la familia: producto nuevo, sin «precio anterior de 30 días» que sostenga un tachado — art. 20 TRLGDCU / RDL 24/2021). **Sin `aggregateRating`, sin `review` en el JSON-LD y sin testimonios inventados** (D3): la sección de testimonios se oculta con `items: []`, como ya hacen la Guía Food Cost y el Manual del Manager. El `bonusTotalLabel` describe el paquete; no inventa un valor.

### 10.3 Las alternativas, con su coste honesto

- **65-69 €** — defendible **con datos**: L1 documenta que el mercado paga sistemáticamente más por dirigir cocina que por dirigir sala (4.300-9.075 € los diplomas de chef ejecutivo, frente a 49-260 € de los cursos generalistas del censo del Manager), y este manual trae **8 libros frente a 7** y un bloque normativo con 40 ids nuevos. **Su coste:** rompe la paridad de línea a los dos días de fijarla, obliga a explicar en el copy por qué cocina cuesta más que negocio, y choca con la lectura de la franja de las 6 guías «Cómo Montar».
- **79-89 €** — es la opción (c) de L1, apoyada en el mismo dato de mercado. **Su coste:** colisiona con la Guía Restaurante Gastronómico (85 €, 119 páginas y 18 xlsx) y con el Mega Pack (89 €), y es el que más se aleja de la paridad. Necesitaría un recuento de entregables que hoy no tiene.
- **45 €** — captaría volumen. **Su coste:** desperdicia el ancla del SaaS, deja el manual por debajo del Kit Plan Financiero (39 €) + un kit de 14 €, y daría el precio por entregable más bajo del catálogo.
- **49 € — VETADO**: es el precio tachado del Kit de Escandallos y chocarían en el hub (misma razón que en los dos productos anteriores).

> **Lo que se deja sobre la mesa, dicho en voz alta:** con 55 € renunciamos al margen que el mercado de formación de cocina justificaría. Se hace **a cambio de coherencia de línea y de un bundle vendible**. Si John prefiere el margen, la opción sólida es **65 €** — pero entonces hay que decidir si el Manual del Manager sube también, o la línea nace con dos precios.

**Idea aparte, para decisión de John (§15):** un **bundle «Dirección completa: Manager + Chef Ejecutivo»**. Los dos productos comparten caso modelado, motor y formato, y las objeciones 6 de los dos research apuntan a lo mismo: el comprador duda de cuál necesita. Un bundle convierte esa duda en una venta doble en vez de en un carrito abandonado.

---

## 11. Nombre, slug, subtítulo, promesa y vocabulario

### 11.1 Nombre y slug

**Nombre: «Manual del Chef Ejecutivo».** No es una preferencia: **es el nombre con el que el producto lleva anunciado en el hub desde mayo**, en los dos ficheros, con su descripción publicada. Cambiarlo rompe una promesa que ya está en producción. Además, «chef ejecutivo» es **el único término del glosario que no varía en ninguno de los 6 mercados** (L5), confirmado en ofertas de MX/CO/PE y en tres entrevistas reales de España, México y Colombia.

**Slug recomendado: `manual-chef-ejecutivo`** → `https://aichef.pro/manual-chef-ejecutivo`, `-access`, `-library`.

| Alternativa evaluada | Veredicto |
|---|---|
| **`manual-chef-ejecutivo`** | ✅ **Recomendado.** Misma convención que `manual-manager-restaurante` (nombre del puesto, sin artículos); prefijo `manual-` **ya cubierto por `robots.txt` en los 5 bloques**; corto; el término no varía por mercado |
| `manual-del-chef-ejecutivo` | ❌ Ningún slug del catálogo lleva artículo. Rompe la convención por un carácter de más |
| `manual-jefe-de-cocina` | ❌ Deja fuera al chef ejecutivo y al corporativo, que son **2 de las 5 buyer personas** y el segmento con más evidencia primaria. Además «jefe de cocina» tiene menos volumen (320 vs 260 en ES, pero 320 vs **1.300** en MX) |
| `manual-direccion-cocina` / `manual-gestion-de-cocina` | ❌ **Sin dato** de volumen en las dos, y no coincide con el nombre publicado desde mayo |
| `manual-chef-ejecutivo-cocina` | ❌ Redundante: un chef ejecutivo es de cocina por definición |

> ⚠️ **Contexto que hay que conocer antes de escribir copy:** `chefejecutivo.com` es el **nº 1 de la SERP española de «chef ejecutivo»** (consultoría y curso de 40 módulos de Jorge Blasco, sin precio publicado). No es un impedimento —el slug es nuestro dominio— pero sí explica por qué **no se debe pelear esa cadena en el `<title>`** ni prometer tráfico por ella.

### 11.2 Copy

| Elemento | Propuesta | Nota |
|---|---|---|
| **H1** | **«El Manual del Chef Ejecutivo»** | Nombre de producto (regla de H1 spoke del proyecto: marca, no keyword-stuffing) |
| **Title** (≤60) | **«Manual del Chef Ejecutivo \| Brigada, Producción y Carta»** (53) | Alternativa: «Manual del Chef Ejecutivo \| Dirigir la Cocina 2026» (50) |
| **Subtítulo del hero** | **«Brigada, producción, estándares y seguridad alimentaria: el criterio de quien dirige la cocina — no de quien la cocina.»** | Marca la frontera con el hermano **y** con los recetarios en una sola línea |
| **Promesa honesta** | **«No te enseña a cocinar. Te da el sistema para que tu cocina funcione igual estés tú o no: quién hace qué, cuánto se produce cada día, cómo se estandariza un plato y de qué respondes tú ante una inspección.»** | Responde de frente a la objeción 3 («llevo años cocinando») |
| **Description** (~155) | **«Para quien ya dirige una cocina: brigada y partidas, planificación de producción, fichas técnicas de proceso, KPIs de cocina, alérgenos y PRL. 20 capítulos y 8 Excel.»** (159 → recortar a «…alérgenos y PRL. 20 capítulos y 8 Excel.») | — |
| **Keywords** (para el cuerpo y los H2, **no para el slug ni el title**) | chef ejecutivo · jefe de cocina · brigada de cocina · organigrama de cocina · ficha técnica de cocina · receta estándar · sous chef · funciones del jefe de cocina · planificación de producción en cocina · KPI de cocina | «sous chef» (1.000/mes ES) y «brigada de cocina» sólo en el cuerpo: su intención es **empleo y definición** |
| **Frase de frontera para la landing** | *«El Manager lleva el negocio. El Chef Ejecutivo lleva la cocina. Si diriges las dos cosas, necesitas los dos.»* | Va **arriba**, no en la FAQ (objeción 6) |

### 11.3 Límite del copy, escrito en la primera pantalla

**El marco legal explicado es el ESPAÑOL.** Las herramientas tienen todas las casillas editables, el vocabulario lleva su equivalencia LATAM en la primera mención y el método viaja entero — pero **no se promete cobertura normativa de ningún otro país**. Se dice en el hero, en la FAQ y en el email. Y, según la regla de John del 5-sep, la FAQ **ofrece la adaptación como servicio** para quien esté fuera de España, en vez de fingir que el producto ya la trae.

---

## 12. FAQ de COMPRA — 12 preguntas

Las de **empleo** («¿cuánto cobra un chef ejecutivo?», «¿cómo se asciende de jefe de partida a sous chef?», «¿dónde hay ofertas?») **quedan fuera**: son la intención que captura InfoJobs y no son nuestras. Estas 12 son de compra.

| # | Pregunta | Cómo se responde |
|---|---|---|
| 1 | **¿En qué se diferencia del Manual del Manager de Restaurante? ¿Necesito los dos?** | **La primera, por la objeción 6.** El Manager lleva negocio, sala, personas y ley transversal; éste lleva cocina: brigada, producción, estándares, seguridad alimentaria, PRL de cocina y carta. Se responde con la tabla de frontera del §7.1, sin marketing: **si sólo diriges la cocina, con éste basta** |
| 2 | **¿Qué diferencia hay entre chef ejecutivo y jefe de cocina, y cuál soy yo?** | Pregunta recurrente y real (dos preguntas de Quora dedicadas sólo a eso, y **6 de 20 fuentes de la SERP la contestan distinto entre sí**). Se responde con el área 2.ª del ALEH VI y se dice que **el manual sirve a los dos**, con ejemplos por escala |
| 3 | **¿Sirve si mi cocina es de 4 o 5 personas?** | Sí, **con un matiz que se dice**: cada capítulo trae un ejemplo por escala (4-6 / 15-25 / 100+). Y el cap. 2 dice literalmente que una brigada de 6 **no está «mal»** comparada con la de Escoffier: lo que cambia es quién acumula funciones |
| 4 | **¿Sirve para hotel, colectividades o un grupo con varias cocinas?** | Sí, y es donde más aporta: el cap. 20 es multi-outlet, el 16 cubre **comidas testigo** (obligatorias para catering, comedores de empresa y encargos de más de 40 personas) y el 3 explica qué pasa cuando tienes centros en dos comunidades con convenios distintos |
| 5 | **¿Y si sólo soy jefe de cocina, no chef ejecutivo?** | El manual está escrito para quien **ya dirige una cocina**, se llame como se llame el puesto en su nómina. Los capítulos 1, 2 y 20 explican qué cambia al subir de escalón, para quien vaya a subir |
| 6 | **¿Y si soy propietario-chef y lo llevo todo yo?** | Entonces te tocan las dos caras: éste te da el sistema de cocina y el Manual del Manager el del negocio. Se dice claro que **son dos productos**, no se disfraza |
| 7 | **¿Sirve si mi restaurante está fuera de España?** | **El marco legal explicado es el español.** Las herramientas son editables y el método viaja entero (brigada, producción, ficha técnica, pase, KPIs, evaluación). **No se promete normativa LATAM**, y se ofrece la adaptación como servicio |
| 8 | **¿Necesito el Pack APPCC si compro este manual?** | Son cosas distintas y hay que decirlo: el manual da el **criterio** (de qué respondes, qué mira el inspector, cómo se dirige la seguridad alimentaria); el Pack da **los 21 registros diarios** que hay que rellenar y firmar. La auditoría de cocina de este manual **excluye a propósito** lo sanitario y remite al Pack |
| 9 | **¿Y el Kit de Escandallos o la Guía Food Cost?** | La ficha técnica de proceso **no recalcula coste**: lo enlaza. Escandallo = cuánto cuesta; ficha técnica = cómo se hace. Se venden como pareja, y el manual funciona sin ellos (con la celda de coste en blanco) |
| 10 | **¿Los Excel funcionan en Google Sheets y en Numbers?** | Sí: nuestras convenciones **prohíben `INDIRECT`, `COUNTA`, `PMT` y `OFFSET`** justamente por eso. Es un argumento verificable frente al competidor de plantillas más directo, que **avisa en su propia ficha** de que las suyas no funcionan |
| 11 | **¿Qué pasa cuando cambie la normativa?** | Pago único con **actualizaciones incluidas**: los parámetros legales viven en celda editable con su nota y su fecha, hay una hoja `Estado Normativo` con fecha de corte y URL, y un apartado enseña a comprobar la vigencia en el BOE. Cuando cambie algo relevante se regenera y el comprador lo recibe |
| 12 | **¿Puedo verlo antes de comprar? ¿Y si no me sirve?** | Índice completo en la landing, capturas reales de los 8 Excel y garantía de 30 días. Objeción estándar de infoproducto, se resuelve como en el resto del catálogo |

**JSON-LD:** `Product` (con `offers`, `priceValidUntil`, `availability`, `seller`) **sin `aggregateRating` ni `review`** + `FAQPage` con las 12 + `BreadcrumbList`. Se pasa `clasifica()` de `fase8d-faq-duplicadas.py` sobre la FAQ final: **cero pares PARECIDA/DEFINICION** (D14 del hermano). Ojo con las preguntas 8 y 9, que son las que más se parecen entre sí.

---

## 13. Canales, interenlazado y piezas de captación

### 13.1 Entrantes (regla capital: cero páginas huérfanas)

| Origen | Acción |
|---|---|
| **Hub `/productos-digitales`** (Astro **y** SPA) | Tarjeta real con badge «Nuevo» + **retirar la entrada de `comingSoon` en LOS DOS ficheros** (`ProductosDigitales.tsx:927` y `ProductosDigitalesHubPage.astro:942`), o quedarán la tarjeta real y la de «Próximamente · Junio 2026» a la vez |
| **5 posts del blog con banner FIJADO** (sustitución quirúrgica, patrón D16) | Ver §13.2 |
| **8 posts más con enlace contextual** | `mise-en-place`, `alergenos`, `gestion-de-alergenos-con-ia-en-restaurantes`, `ia-gestion-alergenos-hosteleria`, `appcc-seguridad-alimentaria-ia-hosteleria`, `12-innovaciones-ia-cocinas-profesionales`, `como-la-ia-transformara-el-rol-de-los-chefs`, `de-chef-tradicional-a-chef-ia` |
| **5 páginas `/usos/rol/`** — `chef-ejecutivo-corporativo`, **`chef-jefe-cocina`** ⚠️ (el slug real; el `id` es `chef-cocina`), `sous-chef`, `chef-catering`, `fb-manager-hotel` | Enlace **bidireccional** + añadir `'manual-chef-ejecutivo'` a sus `productIds`. **Y de paso cerrar el hueco medido: hoy ninguna de las 20 páginas de rol enlaza a un producto de más de 45 €** (`manual-manager-restaurante` y `guia-food-cost-ingenieria-menu` aparecen **0 veces** en todo el fichero) |
| **`footerLinks` cruzados** | Desde `manual-manager-restaurante.ts`, `kit-gestion-personal.ts`, `kit-tareas.ts`, `guia-food-cost-ingenieria-menu.ts` y **`pack-appcc.ts`** — que hoy **no enlaza ni siquiera al Manual del Manager**: sus `footerLinks` sólo tienen aichef.pro, Kit de Escandallos, Pro Prompts eBook y contacto |
| **Rotación general de banners** | Entrada **47** en `products-catalog.ts` → `fase8e-banners-corpus.py` lo reparte por los 325 posts |
| **Lista de compradores (Resend)** | Segmentos de Pack APPCC, Kit de Escandallos, Kit de Inventario, Kit de Tareas, Guía Food Cost y Manual del Manager. **Broadcast propio** (regla de John del 5-sep): el hueco es el `scheduled_at` más tardío que haya en Resend **+ 5 días**, a las 08:00 UTC. ⚠️ La cola documentada llega hoy al **2-oct** (hermanos de línea A), así que el slot previsible es el **7-oct** — a confirmar contra Resend en el momento del lanzamiento, no ahora |
| **Plataforma** | Agente **«Chef Ejecutivo Pro»** (ES) y su librería de prompts |

**Salientes de la landing:** Manual del Manager (55 €), Pack APPCC (14 €), Kit de Escandallos (12 €), Guía Food Cost (55 €), Kit de Tareas (12 €), Kit de Inventario (14 €), la plataforma y el blog — con `utm_source=landing&utm_medium=cross-sell` para poder medir quién compra dos.

### 13.2 Los 5 posts con banner fijado, y qué banner sustituye a cuál

Medido hoy: los 13 posts tienen exactamente 3 banners. Éstos son los candidatos, con el banner **menos afín** marcado para sustituir:

| Post | Banners hoy | Sustituir |
|---|---|---|
| `libreria-de-prompts-para-chef-ejecutivo-pro-ai` | kit-escandallos · kit-gestion-personal · kit-inventario | **kit-inventario** (el menos ligado al criterio del chef) |
| `escandallos-ia-cocina-profesional` | kit-escandallos · guia-food-cost · plan-negocio-bar-restaurante | **plan-negocio-bar-restaurante** (es de apertura, no de cocina) |
| `que-son-las-mermas-en-cocina` | kit-inventario · plan-negocio-cocteleria-eventos · guia-food-cost | **plan-negocio-cocteleria-eventos** |
| `mise-en-place` | kit-tareas · kit-escandallos · pack-appcc | **kit-escandallos** (el post no habla de coste) |
| `tipos-de-cortes-en-la-cocina-profesional` | guia-restaurante-gastronomico · kit-tareas-chef-privado · mega-pack-tareas | **guia-restaurante-gastronomico** |

⚠️ **Los banners de `kit-tareas*`, `pack-appcc`, `kit-escandallos` y `guia-food-cost` van a la lista `NUNCA` del script**, porque son cross-sell del manual: sustituirlos sería quitarse ventas propias. Regla heredada de la D16 del hermano. **Y gate de reversibilidad byte a byte**: el script quita exactamente lo insertado y compara con el original.

### 13.3 Las piezas de captación de blog que salen de este research

**No son este producto y no bloquean el lanzamiento**, pero salen gratis, tienen volumen real, competencia LOW y cero producto de pago en la SERP. Se escriben con `bridge.py` (regla capital: los productos no, el blog sí) y van a la cola de contenidos.

| Keyword | Vol/mes ES · MX | Ángulo | Riesgo |
|---|---|---|---|
| **brigada de cocina** + **organigrama de cocina** | 320 · 880 / 50 · **590** | «El organigrama de cocina que sí existe: los 10 puestos del convenio (y por qué la brigada de Escoffier no aplica a tu cocina de 6)» — con las funciones literales del art. 17 | Bajo. **Es el hueco más limpio: 6 fuentes distinguen roles y las 6 lo hacen distinto** |
| **funciones del jefe de cocina** | 110 · 70 | «Funciones del jefe de cocina según el convenio (no según un blog)» | Bajo. Compite con ESAH, Northbridge y escuelas: nuestro diferencial es citar el BOE |
| **ficha técnica de cocina** + **receta estándar** | 90 · 30 / sin dato · 140 | «Qué debe llevar una ficha técnica de cocina para que sirva de verdad (y por qué no es un escandallo)» | Bajo. ⚠️ **Comprobar canibalización con `escandallos-ia-cocina-profesional` antes de escribirla** |
| **sous chef** | **1.000** · 2.900 | ⚠️ **Volumen alto, intención de EMPLEO.** Si se escribe, es pieza de definición de carrera que enlaza al manual, **no** una landing. Se decide con GSC en la mano | **Medio**: es la trampa de InfoJobs. No prometer conversión |

**Y la puerta de entrada real, medida en GSC:** el glosario técnico de cocina ya posiciona (`5 salsas madre` pos. 5,0 · `fondo blanco` 7,0 · `tipos de mermas en cocina` 7,0 · `mise en place cocina` 9,7 · `roux` 10,9). **Un cocinero que busca «mise en place» no busca «gestión de cocina» — pero es exactamente el público que necesita estandarizar.** Es el mismo patrón de «glosario corto que rankea, manual largo que no» ya documentado en `CLAUDE.md`. El interenlazado desde esas piezas vale más que cualquier landing nueva.

---

## 14. LISTA NEGRA — lo que NO puede aparecer en el producto

Va literalmente al `NO_COMUN` de `guion_manual_chef_ejecutivo.py` como `cifras_ignorar` + `prohibido`, y el gate de coherencia de cifras de `documentos.py` la hace cumplir.

### 14.1 Cifras sin fuente primaria

| Cifra | Por qué no entra |
|---|---|
| **«283 accidentes en cocineros y ayudantes de cocina»** con su desglose (107 cortes, 42 caídas, 35 sobreesfuerzos, 27 llamas, 18 golpes) | Circula en prensa sectorial **sin atribución rastreable a ningún informe primario**. Se sustituye por **CS-01** (INSST, CNAE 56, 2.646,5/100.000 en 2024) y **CE-30** (MITES 2025), que son PDF oficiales leídos |
| **Rango de merma «sano» del 4-6 %** | Lo publican **proveedores de software de cocina** sin un solo estudio citado |
| **255 M€/año de pérdida del sector por mermas** (≈63.000 t) | **Cifra zombi.** El único origen parcial identificado es un estudio de la UAB de **2013** (3,10 €/kg), sin confirmación directa |
| **«Hasta el 15 % de lo cocinado acaba en la basura»** | Fuentes sectoriales sin estudio primario |
| **Rotación en hostelería del 63,8 %** | **Ya estaba prohibida en el hermano, y aquí empeora**: la prensa se la atribuye a «Linkers» y **L4 verificó que NO aparece en Randstad Research**, a quien se le atribuye habitualmente |
| **«1 cocinero cada 20-25 comensales»** (alta cocina 10-20, bufé 40-50) | Regla empírica de blogs. Si se usa, va como **«regla de partida orientativa que cada casa calibra con su producción»**, nunca como estándar |
| **«El 87 % de los restaurantes no tiene fichas técnicas y pierde 2.400 €/año»** | Repetida en agregadores SEO sin encuesta ni informe localizable |
| **«Del pulpo se obtiene ~50 % de merma»** | Sin atribución primaria |
| **«La cocina es más del 50 % del consumo energético»** · «30.000 kWh/año» · «11.000 kWh/año una freidora» · «el sector es el 7 % del consumo de España» | Todas citan a IDAE **sin enlazar el documento primario**. Sólo se puede usar el dato cualitativo del manual MITECO |
| **Talent.com 13.700 €/año para jefe de cocina** · **Glassdoor «1.500-2.500 €/año» para sous chef** | Anomalías evidentes contra las ofertas reales verificadas |
| **Cualquier «salario del chef ejecutivo» como cifra única** | El rango real según fuente va de 44.750 a 58.420 € de media, con P75 en **168.125 €**, y ninguna fuente explica la varianza. **Va como rango con su fuente** |
| **Tiempo medio de pase · coste directo de un brote · horas de formación por trabajador de cocina** | **Confirmado que no existe benchmark español publicado de ninguno.** Van como métrica que el lector mide con su herramienta |
| **Los porcentajes de qamarero.com** (30 % menos rotación, 25 % más eficiencia, 40 % menos conflictos, 30 % más productividad) | Publicados **sin citar ningún estudio**, con apariencia de dato duro. Mismo patrón ya detectado en el research del Manager |
| **BCC «Gestión desde la Cocina» a 895 €** en copy comercial | El precio es de una edición fechada en **feb-2024**; la vigencia 2026 no se pudo confirmar. **No citarlo sin reverificar** |

### 14.2 Afirmaciones normativas falsas o caducas

- «Las temperaturas las fija el **RD 3484/2000**» — **derogado** el 22-12-2022.
- «El anisakis se regula por el **RD 1420/2006**» — **derogado** el 22-12-2022. Lo vigente es el art. 8.1 del RD 1021/2022.
- «Existe el **carné de manipulador de alimentos**» — **no existe desde el 20-02-2010** (RD 109/2010, que derogó el RD 202/2000).
- «El Reglamento 852/2004 tiene un **capítulo de gestión de alérgenos**» — no lo tiene: es el **punto 9 del Cap. IX** del Anexo II. Y el «Cap. V bis» es de **donación**, no de alérgenos.
- «Las **comidas testigo** sólo las guardan hospitales y colegios» — también comedores de empresa con menú común, eventos como actividad principal y **cualquier encargo de más de 40 personas**.
- «Poner **"elaboración propia"** es obligatorio» / «puedo ponerlo si fracciono, envaso, deshueso carne fresca o limpio pescado» — **es voluntario** y esos supuestos están **expresamente excluidos**.
- «Hay una norma que fija **cuántos días dura** una elaboración propia en cámara» — **no existe esa cifra legal**.
- «Si mi café o mis patatas superan el **nivel de referencia de acrilamida** es ilegal» — son **disparadores de revisión**, no límites sancionables, y el reglamento **no nombra a los restaurantes**.
- «El **RD 487/1997** fija en **25 kg** el peso máximo» — **la norma no contiene ninguna cifra en kilos**; el 25 kg es una guía orientativa del INSST.
- «El **uniforme** de cocina es sólo imagen» — el EPI de corte y el calzado antideslizante **son obligatorios y gratuitos** una vez la evaluación de riesgos detecta cuchillos y suelo húmedo.
- «Los **aceites de fritura** ya no tienen límite legal» — el art. 6.3 de la Orden de 26-01-1989 (**<25 % de polares**) sigue vigente.
- «El **Rgto. 1881/2006** fija los contaminantes» — **derogado** por el Rgto. (UE) 2023/915 desde ~25-05-2023.
- «El **doggy bag** obliga desde la Ley 1/2025» — **desde el 22-12-2022** (RD 1021/2022, art. 18.5), con la excepción del bufé libre.
- «Un restaurante de menos de **1.300 m²** está exento de la Ley 1/2025» — **sólo del apartado 4** del art. 6; y ojo al conjunto de locales con el mismo CIF.
- «Se aplica el **ALEH V**» — el vigente es el **VI**, modificado el 04-09-2026 y con vigencia hasta el 31-12-2030.
- «El **ALEH** tipifica al chef corporativo» — **no existe en el convenio**: es una denominación de uso del multi-outlet.
- «La **jornada máxima** es de 37,5 h» / «el registro de jornada tiene que ser digital» / «Verifactu obliga en 2026» — todo lo del bloque transversal del Manual del Manager sigue prohibido aquí.
- «El Reglamento **828/2014** dice literalmente "restaurantes"» — **no los menciona**; se argumenta por analogía con «información alimentaria al consumidor final» y se dice que se argumenta.
- «El informe de la **AESAN** sobre botulismo dice…» citado como leído — **el PDF da 404**; el contenido viene de ACSA/Generalitat y va marcado como fiabilidad media.
- «La guía del **INSHT** "Restaurantes, Bares y Cafeterías" es de [año]» — **el PDF no lleva año**; sólo se puede acotar «anterior a 2018».

### 14.3 Errores de método

- **Confundir «hostelería» con «CNAE 56»** al citar siniestralidad: CE-30 es hostelería (incluye alojamiento) y CS-01 es sólo servicios de comidas y bebidas. Son años distintos (2025 y 2024) y ámbitos distintos.
- **Decir que hostelería es «el 4.º sector» en accidentes**: es el **5.º**. La prensa que dice 4.º omite «actividades administrativas» (57.030).
- **Citar el 30-35 % de coste de personal como si fuera sólo cocina**: es el **equipo completo** (CS-19). No existe desagregación oficial.
- **Presentar la brigada de Escoffier como el estándar** sin advertir cuándo no aplica.
- **Mezclar normativa de otro país sin decirlo** (el error de `germandebonis.com` con SENASA).
- **Dar una cifra única de nómina de cocina**: el mismo jefe de cocina cobra **+49,9 %** en Barcelona que en Madrid.
- **Repetir el bloque laboral general del Manual del Manager**: jornada, permisos, contratación y despido se **citan por capítulo**, no se reescriben.

### 14.4 🔴 Y lo que hay que corregir en lo que YA vendemos (censo propio, hoy)

Escaneados los **438 xlsx** del catálogo: **11 menciones a normas derogadas en 8 ficheros**. **Ocho son correctas** (dicen literalmente «que derogó el RD…»: `pack-appcc/12`, `/13`, `/16`, `/17`, `/18`, `guia-restaurante-gastronomico/checklist-appcc` y `manual-manager-restaurante/calendario-cumplimiento-legal`). **Tres son defectos reales:**

| Fichero | Texto real | Por qué es defecto |
|---|---|---|
| `kit-inventario/04-recepcion-mercancias.xlsx` | «Umbrales tomados del Reglamento (CE) 853/2004 (Anexo III), **el RD 3484/2000** y el Reglamento (CE) 589/2008» | Cita el RD **derogado desde el 22-12-2022 como fuente vigente de los umbrales de temperatura**. Es el que ya había visto L6 |
| `kit-tareas-sushi-bar/03-seguridad-anisakis-appcc.xlsx` | «REGISTRO OBLIGATORIO — Congelación Preventiva Anisakis. **Normativa: RD 1420/2006** y Reglamento CE 853/2004 — Obligatorio para todo establecimiento que sirva pescado crudo» | Cita la norma **derogada como la vigente**. **NO lo había detectado ninguna lente** |
| `kit-tareas-marisqueria/03-trazabilidad-appcc-marisco.xlsx` | «PCC5 Anisakis: congelación previa **−20 °C/7d** para consumo crudo/marinado … **Obligatorio RD 1420/2006**» | **Doble defecto**: la norma derogada, **y la cifra**. Lo verificado (MM-33 / CE-14, RD 1021/2022 art. 8.1) es **−20 °C durante 24 h** o −35 °C durante 15 h. Los 7 días son el criterio de la FDA estadounidense, no el español. **NO lo había detectado ninguna lente** |

**Estos tres son producto vendido, no borrador.** No entran en el alcance de este research (que es sólo investigación), pero **el guion del nuevo manual no puede heredar ninguna de las tres**, y hay que decidir si se corrigen (§15, pregunta 5).

---

## 15. Riesgos, decisiones abiertas y presupuesto

### 15.1 Riesgos

| # | Riesgo | Evidencia | Mitigación |
|---|---|---|---|
| 1 | 🔴 **Confusión con el Manual del Manager** — es el riesgo nº 1 y es comercial, no técnico | Misma línea, mismo precio propuesto, mismo formato, mismo caso modelado, y **L5 lo señala como objeción específica sin precedente en el hermano** | Frontera **en el titular y en la primera pregunta de la FAQ**, no enterrada; tabla comparativa en la landing; cap. 01 con el mapa completo; y considerar el bundle (§10.2) |
| 2 | **Canibalización con cinco productos propios** | Kit de Escandallos (12 €), Pack APPCC (14 €), Kit de Tareas (12 €), Kit de Inventario (14 €), Guía Food Cost (55 €) | Las **6 reglas de no-solape del §7.2**, verificadas celda a celda, y el cap. 01 con la tabla «qué incluye el pack / qué es cross-sell». La frase: *«Los kits te dicen qué hacer cada día. El manual te dice por qué, con qué criterio y de qué respondes»* |
| 3 | **Un error en el bloque legal cuesta más que un error de food cost** | Un chef que aplique mal una regla de alérgenos o de temperaturas puede acabar en una sanción de **20.001-600.000 €** con cierre de hasta 5 años (MM-35) | **Verificador legal independiente obligatorio** (agente sonnet, patrón del verificador fiscal de la Guía Food Cost) **antes** de escribir los caps. 13-17, **contra las fuentes primarias, no contra L3** |
| 4 | **Dos bloques del research se apoyan en fuente secundaria** | CE-35 (botulismo AESAN: `aesan.gob.es` da **404 en todas sus rutas**, mismo patrón del 4-sep) y CE-36 (guía de cocina al vacío de Cataluña: URL no localizada) | Se citan **marcados como fiabilidad media** y con la fuente que sí respondió (ACSA/Generalitat). **No se dice «según el informe de la AESAN» como si se hubiera leído** |
| 5 | **El eje de mermas —central al producto— no tiene una sola cifra fiable** | Las cuatro cifras que circulan (4-6 %, 255 M€, 15 %, 400-600 €/mes) están en la lista negra | **El manual no cita benchmarks de merma**: da la fórmula y la herramienta para que el lector calcule la suya por partida. Es más honesto **y más útil** |
| 6 | **Cinco dolores centrales sin voz del cliente** | Ficha ignorada, mermas, producción desordenada, pase caótico y miedo a Sanidad: **cero citas primarias** por bloqueo de Reddit, Facebook y YouTube | **Pedirle a John 5-10 minutos de voz** sobre esos cinco puntos (§15.2, pregunta 7). Es la fuente más autorizada que existe para este producto |
| 7 | **Vender profundidad LATAM que no tenemos** | El bloque legal es **exclusivamente español**; el 60-70 % del volumen medido está en LATAM | Casillas editables + vocabulario neutro + **la landing lo dice en la primera pantalla** + la FAQ ofrece la adaptación como servicio |
| 8 | **Ámbito autonómico y provincial imposible de cubrir** | 17 convenios de hostelería, 17 sistemas de inspección (Madrid GRSA, Cataluña GPCH/RSIPAC, Andalucía PGH) | Marco estatal + cómo buscar el propio (REGCON, boletín autonómico). Madrid y Cataluña **como ejemplos declarados**, nunca como regla nacional |
| 9 | **Colisión de ids `CE-*` entre L3 y L4** | 23 ids solapados con contenidos distintos | Renombrar el bloque de L4 a **`CS-*`** antes de fusionar en `guias-v2-research-sector.json` (162 entradas, ningún `CE-*` todavía) |
| 10 | **Tres citas legales caducadas vivas en productos vendidos** | §14.4: `kit-inventario/04`, `kit-tareas-sushi-bar/03`, `kit-tareas-marisqueria/03` (esta última, además, con **−20 °C/7 días**) | No heredarlas en el guion nuevo. Corregirlas es decisión de John (§15.2, pregunta 5) |
| 11 | **La reseña de 2★ ya está escrita si repetimos lo básico** | Del research del hermano: «temas tratados demasiado básicos, parece un conjunto de entradas de blog»; y **ninguna de las 7 reseñas analizadas criticaba que un libro fuera corto** | El cap. 01 declara el nivel; lo gratuito se cita y se salta; los **16 conceptos del §1** y el bonus de casos son lo contrario del relleno |
| 12 | **Presupuesto** | El Manual del Manager costó **≈10,5 M tokens** de subagentes, y la redacción de una guía de 95 páginas con subagentes Anthropic ≈**5,5 M**. El techo de John es **~15 % de la cuota semanal** y una semana normal debe quedarse por debajo de **1,5 M** | **La fase B no cabe en una semana.** Partirla en dos sesiones pares, decidido **antes** de arrancar (§15.3) |
| 13 | **Regenerar pisa ediciones manuales** | Gotcha conocido de los ensambladores | Diff de enlaces antes de regenerar nada publicado |
| 14 | **`robots.txt` y sitemap** | El comodín borró 26 posts en agosto | El prefijo `manual-` ya está cubierto en los 5 bloques, pero **correr `robots-gate.py --live`** tras el deploy igualmente |

### 15.2 Decisiones que sólo puede tomar John

1. **Precio: 55 € (recomendado, paridad de línea)** o 65 € (el margen que el mercado justificaría, rompiendo la paridad a los dos días de fijarla). **49 € vetado.**
2. **¿Se crea un bundle «Manager + Chef Ejecutivo»?** Los dos comparten motor, caso modelado y formato, y la objeción 6 de los dos research apunta a la misma duda del comprador.
3. **¿8 libros, con el nº 7 recargado con las comidas testigo (CE-11) y el nº 4 ampliado con las fichas de puesto del ALEH?** Es mi corrección a L6 y es lo que convierte las dos piezas más flojas en las dos más diferenciales.
4. **Bonus: «12 situaciones resueltas en cocina»** (recomendado, ~11.500 palabras → ~28 páginas medidas).
5. **¿Se corrigen las tres citas caducadas del catálogo** (`kit-inventario/04`, `kit-tareas-sushi-bar/03`, `kit-tareas-marisqueria/03`) **y el «−20 °C/7 días» de marisquería** en esta sesión, o van a una sesión impar? Son producto vendido y el error de temperatura es de seguridad alimentaria.
6. **¿Se añaden `manual-manager-restaurante`, `guia-food-cost-ingenieria-menu` y el nuevo manual a los `productIds` de las páginas de rol?** Hoy **ninguna de las 20 enlaza a un producto de más de 45 €**: son 20 páginas construidas para este público vendiendo sólo kits de 9-18 €.
7. **¿Nos das 5-10 minutos de voz sobre los cinco dolores sin cita** (ficha ignorada, mermas, producción desordenada, pase caótico, miedo a Sanidad)? Es el hueco declarado de L5 y tu experiencia es la fuente más autorizada que existe para llenarlo.
8. **¿Banner fijado por sustitución quirúrgica en los 5 posts del §13.2, o sólo rotación general?**
9. **¿Se parte la fase B en dos sesiones?** El presupuesto no cabe en una semana.
10. **Prefijo de ids: `CE-*` para normativa y `CS-*` para datos del sector** — hay que decidirlo antes de fusionar el JSON.
11. **¿Se mantiene «Manual del Chef Ejecutivo» y `manual-chef-ejecutivo`?** Es el nombre anunciado desde mayo; cambiarlo rompe una promesa publicada.
12. **Inglés: ¿sigue vetado?** El agente **«Executive Chef Pro»** ya existe en EN. La decisión del 31-ago dice que no se arranca hasta cerrar el ES.
13. **Slot del broadcast:** el último programado + 5 días. La cola documentada llega al **2-oct**, así que el hueco previsible es el **7-oct** — a confirmar contra Resend en el lanzamiento.

### 15.3 Presupuesto estimado por fase

| Fase | Trabajo | Estimación |
|---|---|---|
| **A — research + SPEC** (esta sesión) | 6 lentes + esta síntesis + SPEC con decisiones firmadas | **Cerrada.** ~2,0-2,4 M tokens de subagentes |
| **B1 — herramientas** | 1 opus `datos_ejemplo.py` (que **importa** los del Manager) → 3 constructores opus (libros 1-2 · 3-4 · 5-6-7-8) → 1 refutador opus de los xlsx (dos lentes en un prompt) → fixer sonnet → `inject_cache` y verificación `data_only` | **1,5-2 M** |
| **B2 — documentos** | 1 opus para el guion → `dump_prompts.py` → ~45 redactores sonnet por bloque con `check_bloque.py` → **1 verificador legal sonnet contra fuentes primarias** (caps. 13-17) → `documentos.py` ensambla → 1 refutador opus → fixer → gates (páginas con PyMuPDF, no latinos, coherencia de cifras, paridad PDF↔DOCX, metadata) | **5-6 M** |
| **C — capa de producto y lanzamiento** | Landing sobre `GuiaData`, dashboard (Manual 2 · Herramientas 8 · Bonus 2), 4 functions + config, Payment Link (John), catálogo 47, hub ×2 con el `comingSoon` retirado, changelog, imágenes, `fase8g` del blog, `robots-gate.py --live`, `fase5-generate-zona-app.py --check`, `whatsapp-gate.py`, gate offline y gate LIVE, broadcast en Resend | **0,8-1 M** |

⚠️ **Aviso explícito:** el techo de John es **~15 % de la cuota semanal** y una semana normal debe quedarse **por debajo de 1,5 M**. **La fase B no cabe en una semana.** O se hacen B1 y B2 en dos sesiones pares distintas, o este manual ocupa dos ciclos de producto nuevo. **Decidirlo antes de arrancar, no a mitad.**

---

## 16. Lo que este research NO pudo verificar

**L1 — competencia**
- **Amazon.es y Amazon.com.mx bloquearon TODO acceso hoy** (500 en WebFetch, reto Akamai `bm-verify` en curl) — más agresivo que el 4-sep. **Cero conteo propio de reseñas** de ningún libro del censo.
- Sin precio: *Competencias de un Chef*, 3 cursos de Hotmart (Agustín Naab, Gerardo Maldonado, Chef Campus), ESAH (625 h), Aprendum, ChefEjecutivo.com y 3 SaaS (Fichatec, Yurest, Haddock).
- **Vigencia 2026 del precio de BCC (895 €)** no confirmada: la fuente indexada es de una edición de feb-2024.
- El precio del **CETT** salió por la URL **en inglés**; la española y `programas.cett.es` dieron 404.
- **No se investigó el mercado angloparlante**: se buscó y no apareció ningún título de gestión traducido (sólo recetarios). Se documenta la ausencia, no una investigación completa.

**L2 — SERP**
- **titulae.es** y **bartalentlab.com**: certificado SSL caducado. **guiaturistica.org**: `ECONNRESET`. **Academia.edu**: 403 en los dos PDF.
- **CIB (posgrado) y CETT/Cámara de Madrid**: sólo verificados por snippet, sin WebFetch a la página primaria.
- **No se corrió SERP en Chile, Perú, Colombia ni Argentina**: el análisis es de España.

**L3 — normativa**
- **PDF original del informe AESAN de botulismo**: `aesan.gob.es` da **404 en todas las rutas**. Contenido vía ACSA/Generalitat, **fiabilidad media**.
- **Guía de cocina al vacío de Cataluña**: URL exacta no localizada, fiabilidad media-baja.
- **Año de edición de la guía INSHT**: el PDF no lo indica.
- **Guías de Cataluña (GPCH) y Andalucía (PGH)**: estructura confirmada, contenido **no leído íntegro** (sí la de Madrid, 53 págs).
- **Aplicabilidad expresa del Rgto. 828/2014 a restaurantes**: el texto no los menciona literalmente.
- Detalle numérico de los anexos de los Rgtos. 2017/2158 y 2023/915: verificado por intermediario sobre el HTML, no cotejado carácter a carácter.

**L4 — convenio y datos**
- **5 de las 17 ofertas** (chef ejecutivo en Boadilla del Monte y Granada, jefe de cocina en un centro sanitario de Girona, Grupo San Eloy en Sevilla, icsa grupo en Burgos) **no se pudieron leer completas** (HTTP 456/410 tras varias peticiones).
- **Sin guía salarial estructurada** de Michael Page, Hays o Adecco específica de cocina 2026.
- **Sin artículo equivalente al art. 36 de Madrid** (ropa de trabajo) en el convenio de Cataluña.
- **Sin desglose oficial de accidentes por tipo** para la ocupación cocinero/ayudante.
- **Sin estudio IDAE primario** con el % de consumo energético de la cocina.
- **Sin ratio oficial** de cocineros por comensal, **sin coste medio de un brote**, **sin benchmark de tiempo de pase** y **sin horas de formación** por trabajador de cocina.

**L5 — voz del cliente**
- **Reddit bloqueado por completo** (403 por WebFetch, por curl y por el proxy `r.jina.ai`); **comentarios de Facebook y YouTube inaccesibles**; Quora 403; foros no útiles.
- **Cero citas primarias** para cinco dolores: ficha ignorada, mermas, producción desordenada, pase caótico y miedo a Sanidad.
- **Cero voz directa de Argentina y Uruguay** — mismo hueco geográfico que en los dos research anteriores.
- **Sin reseñas extraíbles** de Amazon ni Udemy para este nicho.
- Sin testimonio de un **propietario-chef en solitario** ni de la transición de segundo a jefe **en primera persona**.

**L6 — assets**
- ❌ **Corregido por mí:** su §(e) daba por **vacíos** los `productIds` de las 4 páginas de rol. **Los cuatro tienen 6 productos.** El hueco real es que ninguna de las 20 enlaza a un producto de más de 45 €.
- ✅ **Cerrado por mí:** su hueco «no se censó cuántas veces aparece la cita caducada en el resto del catálogo». **Censados los 438 xlsx: 11 menciones, 8 correctas y 3 defectos** (§14.4).
- **Ninguna fórmula de los 8 libros se verificó con pycel**: son diseño, no ficheros.
- No se auditaron los otros ~39 xlsx fuera de los 15 señalados como frontera.
- No se comprobó si `use-cases-content.{en,fr,de,it,pt,nl}.ts` replican el patrón.

**Verificaciones propias de esta síntesis (lo que SÍ comprobé)**
- ✅ `robots.txt` con `manual-*` en los 5 bloques · ✅ **46** productos en `products-catalog.ts` y **47** entradas en `zona-app.ts` · ✅ `comingSoon` del Chef Ejecutivo en los dos ficheros del hub con `phase: 'Junio 2026'` · ✅ los 13 posts existen y los 13 tienen **3 banners**, con sus productos extraídos · ✅ los 5 slugs de rol, incluido `chef-jefe-cocina` (el `id` es `chef-cocina`) · ✅ **calibración medida con PyMuPDF** de los 4 PDF publicados · ✅ **438 xlsx escaneados** en busca de normas derogadas · ✅ **GSC en vivo** (90 días) para consultas de cocina, chef, merma y alérgenos · ✅ agente «Chef Ejecutivo Pro» (ES) y «Executive Chef Pro» (EN) en el catálogo de la plataforma · ✅ `guias-v2-research-sector.json` con 162 entradas y ningún `CE-*`.
- ❌ **No verifiqué el BOE-A-2026-18630 ni el BOE-A-2023-6344 con mis propias manos**: me apoyo en L4, que leyó los dos PDF oficiales íntegros. **Antes de escribir los capítulos 2 y 3, el verificador legal debe abrirlos.**
- ❌ **No repetí los fetches de precios de L1**: las cifras de SaaS, cursos y libros se toman de esa lente.
- ❌ **No consulté Resend** para saber cuál es hoy el `scheduled_at` más tardío: la fecha del 7-oct es una previsión sobre lo documentado en el calendario, **no un hueco confirmado**.

---

**Via: Claude Code**
