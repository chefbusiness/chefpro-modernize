# RESEARCH CONSOLIDADO — «Manual del Manager de Restaurante»
## Producto digital NUEVO · AI Chef Pro · categoría NUEVA «Manuales operativos»

**Fecha:** 2026-09-04 · **Estado:** research cerrado, PENDIENTE DEL OK DE JOHN antes de escribir una sola línea de producto.
**Fuentes:** las cinco lentes de este mismo directorio (`manual-manager-research-L1-competencia.md`, `-L2-serp.md`, `-L3-datos.md` —158 KB, leído entero—, `-L4-cliente.md`, `-L5-assets.md`), leídas completas, más verificación directa contra el repo (`astro-site/public/robots.txt`, `src/data/products-catalog.ts`, `src/data/use-cases.ts`, `astro-site/src/content/blog/`, `guias-v2_0/documentos.py`, `auditorias/guias-v2-research-sector.json`, `guia-food-cost-SPEC.md`, `CALENDARIO-V2-SEMANAL.md`).
**Regla aplicada:** cada cifra lleva fuente y fecha, o va marcada **«sin fuente»**. Nada inventado. Este documento es research y propuesta: **no contiene contenido de producto**.

> **Cinco verificaciones propias que corrigen o cierran hallazgos de las lentes** (detalle en §13):
> 1. ✅ **`robots.txt` YA cubre `manual-*-access` y `manual-*-library` en los 5 bloques de user-agent.** L5 §4.3 daba por hecho que faltaban 10 líneas: están puestas (sin commitear todavía), con el comentario «manual- desde el 2026-09-04, Manual del Manager». **Cae la única objeción técnica al prefijo `manual-`.**
> 2. ✅ **Los tres fixes de parametrización que L5 pedía ya están aplicados** en el árbol de trabajo, sin commitear: `documentos.py` acepta `tipo_doc` y `categoria_doc`; `types.ts` acepta `why.titlePre` y `why.titleGold`.
> 3. ✅ **Los 52 ids `MM-*` de L3 ya están fusionados** en `auditorias/guias-v2-research-sector.json` (155 entradas totales, prefijos ANIS/CONV/FC/JORN/MICH/**MM**/REPS/SECT/SMI/TICK/TRAM/TURG).
> 4. ✅ **Existen 5 páginas de rol relevantes**, no una: `gerente-restaurante`, `propietario-restaurante`, `director-operaciones-grupo`, `fb-manager-hotel`, `maitre-jefe-sala` (`src/data/use-cases.ts`). Cierra el hueco declarado en L2 §6.
> 5. ✅ **Calibración de páginas medida, no estimada:** la Guía Food Cost prometía 60 páginas con 30.000 palabras y **midió 95** (más 32 del bonus). Es el dato que dimensiona la promesa de este manual (§8).

---

## 0. Lo primero: qué demanda hay de verdad y por dónde entra el dinero

**Hay más demanda que en el producto de ayer, pero está donde no se puede vender, y la keyword obvia es una trampa.** Volúmenes de DataForSEO (Google Ads, búsquedas/mes, medidos por L2 el 2026-09-04):

| Keyword | ES | MX | CO | CL | PE | AR |
|---|---|---|---|---|---|---|
| **gerente de restaurante** | 50 | **720** | 20 | 20 | 30 | 10 |
| **administrador de restaurante** | 10 | 70 | **140** | **260** | **170** | 10 |
| gestión de restaurantes | **110** | 50 | 20 | 10 | **210** | 20 |
| curso gestión de restaurantes | 70 | — | — | — | — | — |
| funciones encargado de restaurante | 50 | — | — | — | — | — |
| encargado de restaurante | 40 | 50 | 10 | 10 | 10 | 30 |
| jefe de sala funciones | 30 | — | — | — | — | — |
| administración de restaurantes | 10 | 140 | 50 | 40 | 140 | 20 |
| **manual de operaciones de un restaurante** | 10 | — | — | — | — | — |
| **manual del gerente de restaurante** | **sin dato** | sin dato | sin dato | sin dato | sin dato | sin dato |
| kpi restaurante · checklist restaurante · briefing restaurante | 20 · 10 · 10 | — | — | — | — | — |

Cuatro lecturas incómodas y necesarias:

1. **«Gerente de restaurante» es 89 % ofertas de empleo.** L2 midió el top 19 de la SERP española: **17 de 19 resultados son InfoJobs, LinkedIn, Turijobs, Glassdoor, Indeed, Jooble o descripciones de puesto para reclutadores**. En «encargado de restaurante», 13 de 19. Una landing con esa cadena como cabecera compite contra InfoJobs, no contra contenido. **Es exactamente la trampa que el encargo sospechaba, confirmada con datos.**
2. **La intención más limpia de todo el research vale 10 búsquedas/mes.** «Manual de operaciones de un restaurante» es **100 % intención de problema, cero contaminación de empleo**, y de sus 18 resultados **ninguno es un producto de pago**: blogs (Purohospitality, Mapal, ComboHR, Monouso, tspoonlab), PDFs académicos y el manual gratuito de elBullifoundation. Es el hueco de cobertura más nítido que se ha medido en las dos sesiones de research… con volumen residual.
3. **El volumen alto está en lo legal y es horizontal.** «Verifactu» **74.000**, «convenio hostelería» **1.600**, «hojas de reclamaciones» **1.300**, «ley de desperdicio alimentario» **390** (todas competencia LOW o MEDIUM). No son puerta de entrada de este producto —aplican a cualquier negocio y exigen mantenimiento normativo— pero son **piezas de captación de blog con dueño evidente** (§10.4).
4. **La trampa del sufijo, otra vez.** «Cuadrante de turnos» = 50/mes; «cuadrante de turnos restaurante» = sin dato. «Rotación de personal» = 70; «rotación de personal hostelería» = sin dato. **La gente busca el concepto genérico y filtra ella misma.** Mismo patrón que «chile crisp» vs «chili crisp» (2026-08-02). Señal de contenido, no de landing.

**Y hay una prueba de que existe comprador aunque no exista keyword:** la SERP de «manual del gerente de restaurante» (volumen no medible) devuelve en los puestos 2 y 14 el ebook *Gerente de Restaurantes: Manual de cabecera del líder de un negocio de restauración*, y en el 13 el clásico *Restaurant Manager's Handbook*. **Hay libros vivos vendiéndose para una búsqueda sin volumen.** Es la misma lógica que sostuvo la Guía Food Cost («guia food cost» = 0 y vendió por canales propios).

### Por dónde entra el dinero: seis canales que ya son nuestros

| Canal | Estado real hoy (verificado) | Qué hay que hacer |
|---|---|---|
| **El producto ya está ANUNCIADO en el hub desde mayo** | `src/pages/ProductosDigitales.tsx:911` y `ProductosDigitalesHubPage.astro:921`: «Manual del Manager de Restaurante — Guía completa del gerente: operaciones, personas, finanzas, servicio y liderazgo», `phase: 'Julio 2026'` | **Está vencido dos meses.** Al publicar hay que **quitar la entrada de `comingSoon` en LOS DOS ficheros** y poner la tarjeta real |
| **Banners en el blog ES** | 325/325 posts con 3 banners, 45 productos en rotación (`fase8e-banners-corpus.py`, 2026-08-31; `products-catalog.ts` tiene **45** entradas) | Producto **46** al catálogo; inserción quirúrgica (patrón D11) en los 5 posts afines, no rotación |
| **Los 9 posts propios ya publicados** (verificado: los 10 ficheros existen) | Máxima: `gerente-de-restaurante-20-areas-clave-donde-la-ia-te-puede-ayudar`, `libreria-de-prompts-para-gerente-de-restaurante-pro-ai` · Alta: `gestion-personal-hosteleria-ia-reducir-rotacion`, `rentabilidad-restaurante-kpis-metricas-2026`, `ia-en-la-gestion-de-criticas-y-reputacion-de-restaurantes` · Media: `30-hacks-…`, `inteligencia-artificial-rentabilidad-…`, `timlup-checklist-digital-tareas-recurrentes`, `libreria-de-prompts-para-comida-de-personal` | Banner fijado en los 5 primeros + enlace contextual en los 4 restantes |
| **5 páginas `/usos/rol/…`** (corrección a L2 §6) | `gerente-restaurante` (73 impresiones / 1 clic en GSC), `propietario-restaurante`, `director-operaciones-grupo`, `fb-manager-hotel`, `maitre-jefe-sala` | Enlace **bidireccional**: el rol como entrada temática, el manual como profundización de pago. Cierra el círculo agente gratuito → contenido → producto |
| **Lista de compradores** | Kit Gestión de Personal (14 €), Kit de Tareas (14 €), Pack APPCC (14 €), Kit Plan Financiero (39 €), Guía Food Cost (55 €) | Campaña Resend segmentada: es el público exacto, ya pagó por las plantillas y este producto es el criterio que falta |
| **Plataforma (Pickaxe)** | Existe el agente **«Gerente de Restaurante Pro AI»**, con su librería de prompts publicada en el blog | Mención desde el agente y desde la librería |

**Conclusión del bloque:** este producto **no se lanza por volumen de búsqueda** —«manual del gerente de restaurante» no tiene ni dato— sino porque (a) hay demanda de problema medida en la voz del cliente y en las ofertas de empleo (§6), (b) **la cobertura de pago en español es un desierto verificado producto a producto** (§7), (c) tenemos el canal, y (d) **el producto lleva anunciado desde mayo y hay que cumplirlo**. Igual que con las librerías de prompts y con la Guía Food Cost: **la landing no va a captar por búsqueda y no se debe prometer que lo haga.**

---

## 1. Los conceptos que el manual DEBE fijar (y que la SERP mezcla)

Esto es el equivalente a los 15 conceptos de la Guía Food Cost. Son las distinciones donde la SERP española confunde, no llega o directamente miente — y donde está la autoridad del producto. **De las 18, hay 12 que nadie cubre bien gratis en español**, y en 5 de ellas lo gratuito dice algo **falso**.

| # | Concepto | Qué es exactamente | Con qué se confunde | ¿Lo cubre bien la SERP gratuita? |
|---|---|---|---|---|
| 1 | **Gerente vs encargado vs director vs jefe de sala vs administrador** | El ALEH VI lo resuelve: 6 áreas funcionales y 3 grupos profesionales; «gerente de centro» y «jefe/a de restaurante o sala» están en el **grupo 1.º del área 3.ª** (art. 16). «Administrador» es el término dominante en Colombia, Chile y Perú | Se usan como sinónimos, y el propio buscador no lo tiene claro | **NO.** El PAA pregunta literalmente «¿Cuáles son los rangos en un restaurante?» y «¿Cómo se llama el encargado del restaurante?» y **ninguno de los 19 resultados dibuja un organigrama** |
| 2 | **Registro de jornada** vs **«fichaje digital obligatorio»** | Obligación desde 2019 (art. 34.9 ET): hora concreta de inicio y fin, conservación **4 años**. **Admite papel o Excel.** El RD del registro digital **sigue en tramitación**, con dictamen desfavorable del Consejo de Estado (23-03-2026) | Se vende como si el digital ya obligara | **NO, y además dicen lo contrario.** L4-K2 recogió un blog afirmando «desde enero 2026 operar sin sistema digital homologado es sancionable», con multas de 1.000-10.000 €/trabajador. **Es falso, y quien lo escribe vende software** |
| 3 | **Cuadrante vs registro vs calendario laboral** | Tres documentos distintos: cuadrante = planificación (art. 34.2, preaviso de **5 días** para la distribución irregular del 10 %) · registro = lo que pasó (art. 34.9) · calendario laboral anual = art. 34.6, **expuesto en lugar visible de cada centro** | Todo se llama «el horario» | **NO.** La SERP de «cuadrante de turnos» es 100 % software de RRHH horizontal, sin ángulo hostelería |
| 4 | **P&L mensual vs cuadro semanal del manager** | El mes es contabilidad; la semana es alerta temprana. Sólo el **39 %** de los profesionales revisa su rentabilidad semanalmente, frente al 50 % que lo hace mensual (TheFork, 615 encuestados, 18-03-2026) | Se cree que el cierre mensual basta | **NO.** Y tampoco lo cubre nuestro propio catálogo: `kit-plan-financiero/05` es mensual |
| 5 | **Prime cost** | Coste de producto + coste de personal **con Seguridad Social** sobre venta neta. Con la estructura española (producto 30 % + personal 30-35 %) el umbral es **≤ 65 % con servicio en mesa** y **≤ 55 % en barra/autoservicio** | Se mira sólo el food cost | **NO.** 0/18 fuentes lo calculaban en el research de ayer; aquí el único sitio donde aparece la cifra es **nuestro propio `kit-plan-financiero/06!Benchmarks`… y ahí va SIN fuente** (L5 §1.3) |
| 6 | **Ticket medio vs gasto medio por cubierto vs ventas por hora** | El ticket medio de la restauración española es **21 €** (CaixaBank Research, pagos con tarjeta, 1S 2025) — pero es **por ticket**, y una mesa de cuatro es un ticket. El gasto por cubierto y las ventas por hora de apertura son otras dos cosas | Se toman decisiones de carta con el número equivocado | **NO.** Ninguna fuente los separa |
| 7 | **Rotación vs absentismo vs temporalidad** | Tres indicadores distintos. Lo verificable: temporalidad en hostelería **12,6 %** frente al 15,5 % nacional y **87 %** de indefinidos (Randstad, 1T 2026). El absentismo **no está desglosado para hostelería** (sólo «servicios», 7,1 %). La rotación del 63,8 % **no tiene fuente primaria** | Se mezclan y se cita el 63,8 % como si fuera oficial | **NO, y con una cifra rota circulando.** En este mismo research aparece atribuida a **Synergie** (L4-A3) y a **Randstad** (L4-H1): dos padres distintos para el mismo dato |
| 8 | **Queja vs reclamación formal (hoja oficial)** | La hoja es competencia **autonómica**: Cataluña obliga a responder en **1 mes**; Andalucía **10 días hábiles** y cartel de mínimo DIN-A4 con letra ≥ 0,7 cm; Madrid, cartel con leyenda literal; C. Valenciana, letra ≥ 1 cm y en las dos lenguas oficiales | Se tratan como lo mismo | **NO.** La SERP de «hojas de reclamaciones» (1.300/mes) es 100 % institucional y **sin una sola pieza específica de restaurantes** |
| 9 | **Briefing vs reunión periódica vs handover** | El briefing es pre-servicio y diario; la reunión es semanal/mensual y deja **acta con responsable y fecha**; el handover es el traspaso entre turnos | Se llaman todos «la reunión» | Parcial (los briefings diarios ya los cubrimos nosotros en dos kits) |
| 10 | **Onboarding vs formación obligatoria** | Cuatro cosas distintas: acogida · formación en PRL (art. 19 Ley 31/1995: **en el momento de la contratación**, dentro de jornada y **cuyo coste no recae en ningún caso sobre el trabajador**) · formación de manipuladores (Reg. 852/2004, Anexo II, Cap. XII: obligación **del titular**, por puesto) · formación específica en APPCC | Se cree que el «carné» lo resuelve todo | **NO, y hay un mito con mercado detrás:** el «carné de manipulador oficial» **no existe desde 2010** (RD 202/2000 derogado por el RD 109/2010). Quien vende un «carné oficial homologado» vende humo |
| 11 | **Auditoría interna de servicio vs inspección de Sanidad vs autoevaluación APPCC** | La primera puntúa experiencia de cliente y estándares de marca; la segunda es control oficial; la tercera es cumplimiento alimentario | Se hace una y se cree cubierta la otra | Parcial: la tercera ya la cubrimos (`pack-appcc/15`); de la primera no hay nada |
| 12 | **Reconocimiento médico: voluntario, no obligatorio** | Art. 22.1 Ley 31/1995: «**sólo podrá llevarse a cabo cuando el trabajador preste su consentimiento**». La empresa **ofrece**; el trabajador puede rehusar. Y la empresa **nunca recibe el informe médico**, sólo las conclusiones de aptitud (art. 22.4) | Se imponen como obligatorios | **NO.** L3 lo marca como «el error más frecuente» del bloque de PRL |
| 13 | **Permiso retribuido vs suspensión del contrato** | El **permiso parental de 8 semanas NO es retribuido**: el art. 45.1.o) ET lo tipifica como **suspensión** y el 45.2 «exonera de las obligaciones recíprocas de trabajar y remunerar». Tampoco hay prestación de la Seguridad Social que lo cubra | Se lista entre los permisos retribuidos | **NO.** Y va acompañado de otro error: el permiso por **fallecimiento son 2 días (+2 por desplazamiento), no 5** — el RDL 5/2023 los separó del accidente/enfermedad grave |
| 14 | **Propina en mano vs bote repartido por la empresa** | Siempre son rendimiento del trabajo en IRPF (DGT V2236-13). La **retención sólo nace si la empresa las reparte** (art. 76.1.3.º RIRPF, que nombra literalmente la propina). Sobre **cotización no hay norma expresa**: ni la LGSS ni el RD 2064/1995 mencionan la palabra | Se dice «el tronco cotiza» como si fuera ley | **NO, y con la fuente equivocada:** la consulta **V3095-17** que citan casi todos los blogs es del **tratamiento fiscal de las propinas en casinos y juegos de azar**, no de hostelería |
| 15 | **Corte vs arqueo vs cierre de caja** | Tres pasos: corte = cambio de turno sin verificación · arqueo = foto puntual del efectivo · cierre = contabilidad completa del día. En México «corte de caja» es el paso intermedio, no el cierre | Se usan como sinónimos y se hace uno solo | **NO.** Y quien sólo hace uno queda ciego ante fugas que aparecen en otro |
| 16 | **Terraza «al aire libre» a efectos de tabaco** | Ley 28/2005, art. 2.2: espacio no cubierto, o cubierto rodeado lateralmente por un **máximo de DOS** paredes, muros o paramentos | Circula «menos de tres paredes» | **NO.** Y ojo: hay un **proyecto de ley aprobado el 21-07-2026** que prohibiría fumar en todas las terrazas — **todavía no está en vigor** |
| 17 | **Efectivo: no se puede ser «cashless»** | Rango legal de cobro en efectivo de un restaurante: **0 a 999,99 €** (Ley 7/2012, art. 7). Y **negarse a aceptar efectivo es infracción de consumo** desde el 28-05-2022 (TRLGDCU art. 47.ñ) | Se cree que se puede rechazar el efectivo | **NO.** Además, la Ley 18/2022 «Crea y Crece» **no regula la aceptación de efectivo**: cero apariciones de «curso legal» y «aceptar» en su texto |
| 18 | **Música ambiental: dos pagos, y un cambio de clasificación del local** | Son **dos derechos distintos**: autor (SGAE o SEDA) + conexos (AGEDI-AIE, facturando juntos como «Somos Música»). Y **poner altavoces reclasifica el local** de tipo 3.1 (TV/hilo musical, máx. 80 dBA) a **tipo 3.2**, que obliga a **limitador-registrador precintado** con 15 días de almacenaje de niveles | Se cree que es un solo recibo y que la música no cambia nada | **NO.** L3 lo marca como «el hallazgo que nadie cuenta» |

**Ese es el índice de criterio del manual: 18 distinciones, 12 sin cobertura gratuita decente y 5 donde lo gratuito afirma algo falso** (nº 2, 10, 12, 13, 16 — más la fuente equivocada del nº 14). Es exactamente el tipo de material que un lector puede comprobar en un minuto, y por tanto la mejor prueba de criterio que puede dar un producto de pago.

---

## 2. Regulación y obligaciones España 2026: la ventaja competitiva, y su fecha de caducidad

### 2.1 Los 8 estados verificados a hoy (L3 §1, cinco de ellos con el texto del BOE leído)

| # | Norma / medida | Estado real a 2026-09-04 | Fuente | Fiabilidad |
|---|---|---|---|---|
| V1 | **Reducción de jornada a 37,5 h** | **RECHAZADA, NO vigente.** El Congreso aprobó el 10-09-2025 las enmiendas a la totalidad (178 votos frente a 170) y devolvió el proyecto al Gobierno. Sigue el máximo de **40 h semanales de promedio en cómputo anual** | Art. 34.1 ET; Congreso, iniciativa 121/000058 | **Alta** |
| V2 | **Registro horario digital** | **EN TRAMITACIÓN, NO publicado en el BOE.** Dictamen desfavorable del Consejo de Estado el 23-03-2026; aprobación aplazada a septiembre de 2026. Lo exigible sigue siendo el registro diario del art. 34.9 desde 2019, que **admite papel o Excel** | Art. 34.9 ET | Alta (que no hay RD) / **Media** (el estado de la tramitación viene de secundarias coincidentes) |
| V3 | **Verifactu** | **APLAZADO a 2027**, por segunda vez. El **RDL 15/2025, de 2 de diciembre** (BOE 03-12-2025), art. 3: **1-01-2027** para contribuyentes del Impuesto sobre Sociedades y **1-07-2027** para el resto | BOE-A-2025-24446 | **Alta** (texto leído) |
| V4 | **Factura electrónica B2B** | **Reglamento aprobado, obligación NO exigible aún.** RD 238/2026 (BOE 31-03-2026); aplicación diferida a 12 meses (>8 M€) y 24 meses (resto) desde la orden ministerial. **Su art. 4 excluye expresamente las facturas simplificadas** → el tique del restaurante queda fuera | BOE-A-2026-7295 | **Alta** (texto leído) |
| V5 | **Ley 1/2025 de desperdicio alimentario** | **VIGENTE** desde el 02-01-2025; las medidas del art. 6 (plan de prevención) exigibles desde el **02-04-2026**. Pero **el «doggy bag» no nació aquí**: ya obligaba desde el **15-12-2022** por el art. 18.5 del RD 1021/2022. Y del plan **quedan exentos los establecimientos de hasta 1.300 m² y las microempresas** | BOE-A-2025-6597 · RD 1021/2022 | **Alta** (texto leído) |
| V6 | **SMI 2026** | **VIGENTE: 1.221 €/mes** en 14 pagas (**40,70 €/día**, **17.094 €/año**), +3,1 %, con efectos desde el 1-01-2026 | RD 126/2026 (BOE 19-02-2026) | **Alta** |
| V7 | **Antitabaco en terrazas** | **PROYECTO DE LEY, NO vigente.** Aprobado por el Consejo de Ministros el 21-07-2026 y remitido a las Cortes. Hoy rige la Ley 28/2005 en su redacción actual (máximo dos paredes) | Ministerio de Sanidad | Alta |
| V8 | **RD 3484/2000 (temperaturas)** | **DEROGADO** con efectos de 22-12-2022 por el RD 1021/2022. Citarlo hoy es **la cita legal caducada más repetida del sector**. Lo vigente es el art. 30 del RD 1086/2020 en la redacción del RD 1021/2022 | Ficha del BOE | **Alta** (ficha leída) |

### 2.2 Las cinco autocorrecciones de L3 al propio encargo (y tres derogaciones más)

| Lo que se suponía | Lo verificado |
|---|---|
| «RD 830/2022 sobre biocidas / ROESB» | **No existe ningún RD 830/2022 de biocidas.** Son el **RD 830/2010** (capacitación) y la **Orden SCO/3269/2006** (ROESB), las dos vigentes |
| «Los aceites de fritura ya no tienen límite legal» | El **art. 6.3 de la Orden de 26-01-1989** (componentes polares **< 25 %**) **NO fue derogado**: el RD 176/2013 derogó los arts. 7, 8, 10, 11 y 12. Sigue exigible |
| «Las cuantías del art. 40 LISOS las actualizó el RDL 5/2023» | **No.** La última modificación es la **disposición final 1.2 de la Ley 10/2021** (más el RDL 32/2021, que añadió la letra c bis) |
| «La consulta de las propinas es la V3095-17» | Es de **casinos y juegos de azar**. De las 8 consultas vinculantes de la DGT con la palabra «propinas», **la única de hostelería es la V2236-13** |
| «Los perros guía se rigen por el RD 3250/1983» | **DEROGADO** desde el 17-06-2025 por el RD 409/2025 |
| + | **RD 1420/2006 (anisakis) DEROGADO** el 22-12-2022 → art. 8.1 del RD 1021/2022 |
| + | **Se aplica el ALEH VI**, no el V (que es de 2015). Y **ningún ALEH fija tablas salariales**: las remite al convenio provincial (art. 12.5) |
| + | **Orden de 17-03-1965** (Ordenación Turística de Restaurantes) **DEROGADA** por el RD 39/2010. No confundirla con el **RD 2199/1976**, de hojas de reclamaciones, que sigue formalmente vigente |

### 2.3 🔴 El hallazgo del día: el ALEH VI se modificó y se publicó HOY

**Resolución de la DGT de 25-08-2026, BOE núm. 219 del 2026-09-04, pp. 119174-119189 ([BOE-A-2026-18630](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-18630)).** Firmada el 11-06-2026 por CEHE y CEHAT con FeSMC-UGT y CC.OO.-Servicios. Modifica el preámbulo y los **arts. 6, 9, 10, 15, 16, 17, 38, 39, 40 y 41** y las tablas del anexo I, y **añade los capítulos XIII (arts. 67-74, LGTBI) y XIV (arts. 75-80, catástrofes)**.

Lo que cambia para un manager, y que **ningún manual del mercado recoge todavía**:

| Novedad | Contenido |
|---|---|
| **Art. 41.3 — audiencia previa en despido disciplinario** | Antes de la carta hay que **informar de los hechos imputados y su calificación jurídica** y dar **2 días para contestar**. Si se aparta a la persona del servicio, esos 2 días son **permiso retribuido**. Incorpora la STS 1250/2024, de 18-11-2024 (art. 7 del Convenio 158 OIT). **Saltárselo abre la puerta a la improcedencia** |
| **Arts. 38.10, 39.21 y 40.14 — régimen disciplinario del registro de jornada** | **2 incumplimientos = falta LEVE · 3-4 = GRAVE · 5 o más = MUY GRAVE.** El registro deja de ser sólo un riesgo de sanción administrativa y pasa a ser materia disciplinaria interna |
| **Art. 38.12** | **Falta leve**: uso del móvil o de redes sociales en jornada sin autorización |
| **Art. 39.20** | **Falta grave**: incumplir la prohibición de fumar |
| **Cap. XIV (arts. 75-80) — catástrofes y meteorología adversa** | Ligado al art. 37.3.g) ET: se atiende a la **última alerta de AEMET antes del inicio del turno**; si llega con el turno empezado se ofrece permanecer en el centro con refugio, y **ese exceso no es tiempo de trabajo salvo fuerza mayor** |
| **Cap. XIII (arts. 67-74) — LGTBI** | El sector ya tiene su conjunto planificado de referencia para empresas de más de 50 personas; voluntario en las demás |

### 2.4 Qué de esto es ARGUMENTO DE VENTA

1. **«Actualizado al BOE del día del lanzamiento», y es literal.** El ALEH VI se modificó el mismo día del research. Ningún competidor del censo lo recoge.
2. **Es el hueco medido, no una impresión.** De los 36 productos censados por L1, **sólo 2 tratan el cumplimiento legal español con profundidad**, y los dos lo hacen como **trámite de apertura**, no como rutina del día a día. El recurso gratuito más prestigioso y extenso del mercado —557 páginas de elBullifoundation × CaixaBank— tiene **cero apariciones** de «registro horario», «KPI», «prime cost», «briefing», «reseñas», «onboarding» y «evaluación del desempeño» (búsqueda con PyMuPDF sobre el PDF completo, L1 §3.3).
3. **Los 12 errores del §0 de L3 son comprobables por el lector en un minuto.** Un manual que dice «el RD 3484/2000 está derogado desde 2022 y aquí tienes la ficha del BOE» se separa solo de los que lo siguen citando.
4. **Hay criterio que sólo se puede dar diciendo que la ley NO obliga.** De los ~14 puntos del calendario de mantenimiento, **sólo 4 tienen periodicidad fijada por norma estatal**: registro de jornada (diario), inspección de ascensor (2 años), inspección de gas (5 años) y extintores (trimestral por el titular / anual por mantenedora / retimbrado a los 5 años / retirada a los 20). **Campana, plagas, termómetros y formación se venden como «obligación legal cada X meses» y no lo son**: la ley exige el resultado, no el calendario. Decirlo así es un diferenciador que ningún blog del sector puede permitirse, porque casi todos venden el servicio.

### 2.5 Y qué riesgo de caducidad tiene (con nombre y fecha)

| Qué va a cambiar | Cuándo | Probabilidad |
|---|---|---|
| **Verifactu** | 1-01-2027 (sociedades) y 1-07-2027 (resto) | **Certeza de fecha** |
| **Registro horario digital** | Aprobación aplazada «a septiembre de 2026» → puede publicarse en semanas | **Alta e inminente** |
| **Factura electrónica B2B** | 12/24 meses desde una orden ministerial aún no dictada | Alta |
| **Antitabaco en terrazas** | En tramitación parlamentaria desde el 21-07-2026 | Media-alta |
| **SMI** | Revisión anual, típicamente enero | **Certeza anual** |
| **Convenio provincial** | El de Madrid expiró el 31-12-2025 y se aplica por ultraactividad | Alta |
| **Reducción de jornada** | Rechazada, pero el Gobierno puede volver a presentarla | Media |

**Cómo lo gestiona el producto (esto va en la SPEC, no es retórica):**

1. **Ninguna cifra normativa dentro de una fórmula.** Convención de familia (`motor.py`: `escribir_parametro`, `PARAMETROS`): SMI, tipo de cotización, umbrales, plazos y periodicidades viven en **celda verde editable con su nota y su fecha**. Cuando cambie el SMI, el comprador cambia una celda.
2. **Una hoja `Estado Normativo`** en `calendario-cumplimiento-legal.xlsx` (§3), con una fila por norma en movimiento, su estado, **su fecha de corte y su URL**, todo editable. El documento envejece; la herramienta, no.
3. **Un bloque de «estado a la fecha de esta edición» al principio del capítulo legal**, con la fecha de corte visible. La honestidad de fechar es lo que convierte el riesgo en argumento.
4. **Cada afirmación normativa lleva norma + artículo + enlace.** Nunca «es obligatorio» a secas. Así el lector puede verificar y, cuando cambie, sabe dónde mirar.
5. **Un capítulo enseña a verificar el estado**: la **ficha de vigencia del BOE** (que es lo que distingue una norma viva de una derogada), el **REGCON** para el convenio de tu provincia, y el boletín autonómico. El lector se autoactualiza.
6. **«Actualizaciones incluidas» del pago único + `productos-changelog.ts`**: cuando cambie algo relevante, se regenera y el comprador lo recibe. Es el argumento de la familia, y aquí por fin es literal en vez de decorativo.

---

## 3. Herramientas: qué usa el sector y qué damos nosotros

### 3.1 Qué usa el sector (medido en L1, con URL y fecha)

| Categoría | Producto | Precio confirmado | Nota |
|---|---|---|---|
| **SaaS de gestión integral** | **Last.app** | **Starter 50 · Growth 95 · Unlimited 175 €/mes** (+IVA, por local, facturación anual) **+ instalación única de 500 € +IVA** | Precio **oficial** en `last.app/precios`. **Growth = 1.140 €/año; Unlimited = 2.100 €/año** |
| SaaS de reservas | Cover Manager | **99-349 €/mes + 1,50 €/reserva** procesada | Fuente tercera; su página oficial de precios da 404 |
| SaaS de turnos/fichaje | Combo · Skello | 2-5 €/empleado/mes (estimación) · 59-109 €/mes **o** ~5,40 €/empleado/mes (**dos fuentes contradictorias**) | Ninguno publica precio oficial accesible |
| SaaS enterprise | Mapal OS · Nory · Zenchef | Bajo consulta · bajo consulta · 150-400 €/mes (estimación) | Venta consultiva |
| **Plantillas Excel de pago** | IngenieriadeMenu.com: 30 plantillas + 10 de bonus | **39,70 €** (oferta 50 %; normal 79,40 €) | **Sólo Excel de escritorio: no funcionan en Sheets ni Numbers**, y lo dicen en la ficha |
| **Bundle curso+manual+Excel** | «Administración Pro para Restaurantes» (Hotmart) | **89,54 €** (IVA incluido) | 10 módulos + **8 manuales de operaciones en Excel**. **Es LATAM: cero terminología o normativa española** |
| Manual de un solo tema | Formahostel (sala / barra / compras) | **6,75 €** cada uno | Suelo del mercado |
| Libros | 11 censados | **7,59 € – 23,95 €** en euros confirmados (hasta ≈31 € en Amazon.com.mx, conversión aproximada) | Ninguno trae Excel operativo |
| Cursos online | Aprendum · estudioformacion | **150 €** (normal 260) · **49 €** (normal 159) | **Acceso limitado a 6 meses** |
| Cursos institucionales | BCC/Mondragon | **2.310 €** (edición oct-26/mar-27) | 8 ECTS, con fecha de inicio y fin |
| Másteres | BCC F&B · Barcelona Culinary Hub | **12.275 €** · 8.200-11.800 € | Mismo temario, 9-24 meses |
| **Gratuito de referencia** | ManualDelRestaurante.com | **0 €** | 20 manuales (663 págs) + 7 calculadoras Excel. Los add-ons de pago son consultoría (49-99 USD), no documentos |
| **Gratuito más completo** | elBullifoundation × CaixaBank | **0 €** | **557 páginas… pero de APERTURA.** Ver §2.4 punto 2 |

### 3.2 Qué damos nosotros: lo que NO se construye, verificado celda a celda

L5 abrió con `openpyxl` los xlsx vivos de `kit-tareas`, `kit-gestion-personal`, `kit-plan-financiero`, `guia-food-cost-ingenieria-menu` y `pack-appcc`. **Confirmo los tres descartes de L5 §2.1 y añado seis más:**

| Idea | Ya existe en | Decisión |
|---|---|---|
| Arqueo y cuadre de caja | `kit-tareas/09-apertura-cierre-caja.xlsx` (fondo, recuento por denominaciones, Z del TPV, descuadre `=IFERROR(F5-G5,0)`, registro mensual de 31 días) | ❌ **No se construye.** El manual explica cómo **leer un descuadre recurrente**, no recalcula el arqueo |
| Planificador de personal por cubiertos | `kit-gestion-personal/03!Previsión por Servicio` **y** `BONUS-02-calculadora-plantilla-optima.xlsx` (**dos veces**, unificado a propósito por su SPEC, DOM-9) | ❌ **No se construye un tercero** |
| Control de horas y coste por servicio | `kit-gestion-personal/02` + `03!Nóminas` (cruce de medianoche, recargo en celda, SS al 33 %, límite anual de 80 h con semáforo) | ❌ **No se construye** |
| Checklist diario/semanal/mensual del manager | `kit-tareas/03-tareas-manager.xlsx` (**110 tareas** en 4 hojas) | ❌ **Se cita.** El manual aporta el **criterio** detrás de las tareas de más peso |
| Cuadrante de turnos con alertas legales | `kit-gestion-personal/01` (4 alertas: descanso entre jornadas, descanso semanal, jornada semanal, jornada de menor) | ❌ **Se cita** |
| Registro de jornada | `kit-gestion-personal/02` (entrada/salida con cruce de medianoche) | ❌ **Se cita**; el manual explica los 4 años de conservación y el nuevo régimen disciplinario del ALEH |
| Onboarding, vacaciones, evaluación, directorio | `kit-gestion-personal/04, 05, 06, 07` | ❌ **Se citan**; el manual encadena selección → onboarding → evaluación |
| Escandallo, food cost, ingeniería de menú | Kit de Escandallos (12 €) + Guía Food Cost (55 €) | ❌ **Cross-sell explícito** |
| Registros APPCC, inspección de Sanidad, formación alimentaria | `pack-appcc` (21 xlsx, incluido `15-guia-inspeccion-sanidad.xlsx` y `BONUS-01-registro-formacion.xlsx`) | ❌ **Se citan**; la auditoría interna nueva **excluye a propósito** los puntos de APPCC |
| P&L mensual y ratios financieros | `kit-plan-financiero/05` y `06` | ❌ **Se citan**; se construye sólo la variante **semanal** |

**Nota importante que cambia una decisión:** `kit-plan-financiero/06!Benchmarks!C6:G6` ya trae el prime cost «óptimo <60 %, aceptable 60-65 %, peligro >65 %» — **pero sin cita ni URL**. No es una fuente: es una cifra que ya circula en nuestro catálogo. **En el manual el umbral se presenta como DERIVADO de la estructura española** (producto 30 % + personal 30-35 % de CaixaBankLab × elBulliFoundation → ≤ 65 % en sala, ≤ 55 % en barra), citando el 60 % de Toast/restaurantowner **como referencia de EE. UU.** Es la misma decisión D5 que ya se firmó en la Guía Food Cost.

### 3.3 Los 8 libros de Excel — evaluación de las 7 propuestas de L5 y propuesta final

**Confirmo las 7 y las corrijo en tres puntos:** (a) **parto en dos** la nº 6 de L5, que fusionaba cumplimiento legal con reuniones —dos usuarios, dos cadencias y, sobre todo, el calendario de cumplimiento es la pieza que carga toda la ventaja normativa del §2; meterlo en la misma hoja que las actas lo diluye—; (b) **amplío** el registro de quejas para que separe queja de reclamación formal con el plazo legal por comunidad, que es lo que lo hace único; (c) **absorbo** dentro de libros existentes las dos piezas que el encargo preguntaba si faltaban (cuadro de KPI con definiciones → hoja del nº 1; guion de reuniones → hojas del nº 7).

| # | Fichero | Hojas | Entradas (celda verde) | Salidas / fórmulas | Decisión que permite | Motor de origen |
|---|---|---|---|---|---|---|
| 1 | **`cuadro-de-mando-semanal-manager.xlsx`** ⭐ | Instrucciones · Parámetros · Semana (52 filas ISO) · **KPI y definiciones** | tipo de negocio (lista sala / barra-autoservicio), objetivos de food cost %, labor cost % y prime cost %, **SS a cargo de la empresa 23,60 %** (MM-17, celda con nota); por semana: ventas netas de comida y de bebida, stock inicial, compras, stock final, salarios brutos, otros costes de personal, cubiertos, nº de tickets, horas de apertura, horas trabajadas | consumo, food cost %, coste de personal con SS, labor cost %, **prime cost %**, semáforo `ISNUMBER` vs objetivo, **ticket medio** (ventas/tickets), **gasto medio por cubierto** (ventas/cubiertos), cubiertos por hora de apertura, ventas por hora trabajada, margen tras prime cost. La hoja `KPI y definiciones` da la fórmula, la unidad y **el error típico** de cada indicador | Detectar una semana mala **antes** de que se diluya en el promedio del mes (sólo el 39 % revisa semanalmente, TheFork) y dejar de decidir carta con el número equivocado (§1.6) | `guia-food-cost/cuadro-de-mando-prime-cost.xlsx!Mensual` (prime cost y semáforo, cambiando el periodo) + `kit-plan-financiero/05!Resumen Anual` (semáforo con signo) + `kit-gestion-personal/03!Nóminas` (SS en celda) |
| 2 | **`matriz-formacion-polivalencia.xlsx`** | Instrucciones · Matriz · Plan de Cross-Training · Cobertura por Estación · **Coste de una Baja** | 30 empleados × 12 estaciones, nivel **0-3** (0 sin formar / 1 supervisado / 2 autónomo / 3 puede formar); plan: empleado, estación objetivo, responsable, fecha, estado; coste de una baja: horas de selección y su coste/hora, horas de formación y coste/hora del formador y del formado, días de menor rendimiento y % estimado | polivalentes por estación (`COUNTIFS`), **alerta de punto único de fallo** (`=IF(cobertura<=1;"⚠ RIESGO: sólo 1 persona sabe esta estación";"")`), % de cobertura, y **coste estimado de reemplazo calculado con SUS datos** — cero cifras nuestras | Quién cubre una baja sin recurrir a un extra, dónde hay una sola persona que sabe hacer algo, y cuánto cuesta de verdad perderla | `kit-gestion-personal/07!Plantilla` (cabecera y 30 empleados) + `07!Vencimientos!C7` (semáforo) + `06!Ficha Evaluación!C22` (media condicional) |
| 3 | **`quejas-reclamaciones-resenas.xlsx`** | Instrucciones · Parámetros · Registro de Quejas · **Reclamaciones Formales** · Reseñas · Resumen | SLA propio en horas por gravedad; **plazo legal de respuesta por comunidad en celda editable**, sembrado con lo verificado (Cataluña 1 mes · Andalucía 10 días hábiles) y su nota de fuente; quejas: fecha, canal, motivo (lista), gravedad, responsable, acción, cierre; reclamaciones: fecha de entrega de la hoja, nº, comunidad, fecha de respuesta; reseñas: plataforma, fecha, estrellas, tema, respondida S/N | SLA cumplido (`IF(cierre−apertura<=sla/24)`), tiempo medio de cierre (`AVERAGEIFS`), motivo y gravedad más repetidos (`COUNTIFS`), **plazo legal cumplido**, media de estrellas por mes, % de reseñas respondidas | Si las quejas se repiten por el **mismo motivo** —y entonces es un problema de proceso, no de persona— y si la reclamación formal se contestó dentro del plazo de **tu** comunidad | Patrón `✓/—/N/A` de `kit-tareas` + escala de gravedad de `pack-appcc/15!25 Puntos Inspección!D`. **Hueco declarado: no existe nada equivalente en el catálogo** |
| 4 | **`seleccion-scorecard-entrevista.xlsx`** | Instrucciones · Scorecard · Comparativa de Candidatos · Preguntas por Competencia | puesto, candidato, **8 competencias con peso**, puntuación 1-5 o N/A, observaciones; banco de preguntas estructuradas por competencia | media ponderada **sólo de lo valorado** (`=IF(COUNT(rango)=0;"";ROUND(AVERAGE(rango);2))`), ranking de candidatos, recomendación por umbral en celda | Comparar candidatos con el mismo criterio en vez de con la impresión del día, y dejar rastro de **por qué** se contrató a alguien | `kit-gestion-personal/06!Ficha Evaluación!C22`, literal. **Nota legal obligatoria en la hoja de preguntas: art. 9.5 de la Ley 15/2022 — «el empleador no podrá preguntar sobre las condiciones de salud del aspirante al puesto»**. Cierra el ciclo con `04-onboarding-nuevo-empleado.xlsx` |
| 5 | **`plan-90-dias-operativo.xlsx`** | Instrucciones · Decisiones · Calendario 90 Días · KPI de Seguimiento | 20 decisiones: área (lista: personas / servicio / operaciones / cumplimiento / finanzas), **herramienta de origen** (lista de los 8 libros), decisión, responsable, semana, impacto estimado, estado; fecha de inicio en celda; KPI mes 0 vs mes 3 | fecha objetivo `=IFERROR(IF(OR($F5="";$D$36="");"";$D$36+7*($F5−1));"")`, % de decisiones cerradas, avance del calendario, lectura automática **Mejora/Empeora** según si «bajar es bueno» | Dar **orden, fecha y responsable** a las salidas de los otros 7 libros | `guia-food-cost/plan-accion-90-dias.xlsx`, letra por letra. **Declara en Instrucciones que NO es el plan de 90 días de la Guía Food Cost**: áreas distintas, se usan en paralelo |
| 6 | **`calendario-cumplimiento-legal.xlsx`** ⭐ el diferenciador | Instrucciones · **Estado Normativo** · Calendario y Vencimientos · Documentación Obligatoria | fecha de la última actuación de ~14 puntos (ascensor, extintores por titular / por mantenedora / retimbrado / retirada a los 20 años, gas, plagas-DDD, campana y conductos, calibración de termómetros, analítica de agua, formación de manipuladores, formación de PRL, evaluación de riesgos, registro retributivo, plan de desperdicio si aplica, seguro, TPV) + **periodicidad en celda editable** + columna **«¿lo fija una norma estatal? Sí/No»** sembrada con lo verificado; hoja `Estado Normativo`: una fila por norma en movimiento (registro horario digital, Verifactu, factura-e B2B, antitabaco, SMI, convenio provincial) con estado, **fecha de corte** y URL, todo editable | próxima fecha = última + periodicidad; semáforo **❌ VENCIDO / 🔴 <30 d / 🟡 <60 d / 🟢 OK**; contador de vencidos y % en verde | No llegar a una inspección con el extintor caducado — y **saber cuáles de esas fechas son obligación legal y cuáles son práctica del sector** (§2.4 punto 4) | `kit-gestion-personal/07!Vencimientos!C7` (alerta por fecha, literal) + el contenido de `kit-tareas/05!Trimestral y Anual`, al que **se remite sin copiarlo**: aquel es un checklist sin fechas; este es el calendario con alerta |
| 7 | **`reuniones-briefings-actas.xlsx`** | Instrucciones · Calendario de Reuniones · **Guion de Briefing** · **Guion de Reunión Semanal** · Actas y Acuerdos | tipo (briefing de servicio / reunión semanal de equipo / mensual de resultados / uno-a-uno), fecha, asistentes, puntos de agenda; acta: punto, decisión, responsable, fecha de seguimiento, estado | acuerdos abiertos, % cerrados en plazo, acuerdos que vencen esta semana; columna de traspaso a `plan-90-dias-operativo` | Que una reunión deje **decisiones con fecha** en vez de una conversación que nadie recuerda al mes siguiente | **No duplica** los briefings **diarios** de `kit-tareas/BONUS-01` ni de `kit-gestion-personal/BONUS-01` (otra cadencia y otro propósito): se citan |
| 8 | **`auditoria-interna-servicio.xlsx`** (mystery audit) | Instrucciones · Auditoría · Resumen por Área · Histórico | ~60 puntos de control en 6 áreas (llegada y reserva · sala y ambiente · servicio y tiempos · producto y presentación · aseos y limpieza no-APPCC · marca y digital), peso por punto, puntuación 0-5, observación, fecha y auditor | puntuación ponderada `=SUMPRODUCT(peso;puntuación)/SUM(peso)`, % de cumplimiento por área, semáforo, tendencia entre visitas | Puntuar la experiencia de cliente y los estándares de marca de forma **repetible y comparable en el tiempo** | `pack-appcc/15!25 Puntos Inspección` (patrón de puntuación y %). **EXCLUYE a propósito APPCC y sanidad** → remite al Pack APPCC |

**Convenciones obligatorias de familia** (idénticas a la SPEC de la Guía Food Cost §2.2, no negociables): helpers de `guias-v2_0/motor.py`; hoja «Instrucciones» primero con «Celdas verdes = campos editables», línea de versión, bio anclada y nota de desproteger; **cero constantes tecleadas dentro de una fórmula** (SMI, SS, plazos, umbrales: siempre celda); `IFERROR(...;"")` y `ISNUMBER` en semáforos; «sin dato» = `""`, nunca `0`; **prohibido `INDIRECT`, `COUNTA`, `PMT` y `OFFSET`** (compatibilidad con Sheets y Numbers, y con pycel); formatos `#,##0.00 €` y `0.0%`; A4 con `print_setup`; datos de ejemplo **coherentes entre libros** (la misma plantilla de 12 personas y las mismas 6 estaciones en la matriz, el scorecard y el plan de 90 días); metadata `author='AI Chef Pro'`. Después de generar: `inject_cache.py` y verificación `data_only` de cada fórmula registrada.

**Detalle competitivo que sale gratis:** IngenieriadeMenu.com **advierte en su ficha** que sus 40 plantillas no funcionan en Sheets ni Numbers. Nuestras convenciones prohíben justo las funciones que rompen esa compatibilidad. **Es un argumento de landing verificable frente al competidor de plantillas más directo.**

---

## 4. De dónde saca el LECTOR sus propios datos (un capítulo entero del manual)

| Qué necesita | Fuente pública real | URL | Fiabilidad / aviso |
|---|---|---|---|
| **Si una norma sigue viva** | **Ficha de vigencia del BOE** (el aviso «Norma derogada, con efectos de…») y el texto **consolidado** | `boe.es/buscar/act.php?id=…` y ELI (`boe.es/eli/es/rd/2022/12/13/1021/con`) | **Alta.** Es la comprobación que separa este manual de los que citan el RD 3484/2000 |
| **Qué convenio le aplica** | **REGCON** — Registro y Depósito de Convenios Colectivos del Ministerio de Trabajo; se filtra por provincia + sector | `expinterweb.mites.gob.es/regcon/` | **Alta** (comprobado en vivo por L3) |
| Marco estatal del sector | **ALEH VI** y su modificación | BOE-A-2023-6344 · **BOE-A-2026-18630** | Alta |
| Coste laboral, empresas, facturación, supervivencia, IPC | **INE**: EACL, DIRCE, EEE Servicios, DAE, IPC | `ine.es/dyngs/Prensa/EACL2025.pdf`, `…/DIRCE2025.pdf`, `…/EEESS2024.pdf`, `…/DAE2023.htm` | Alta (PDF oficiales) |
| Normativa alimentaria europea consolidada | **EUR-Lex** (Reg. 852/2004, 178/2002, 1169/2011) | `eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02004R0852-20210324` | Alta |
| Sanciones laborales | **LISOS** (RDLeg 5/2000), art. 40 | `boe.es/buscar/act.php?id=BOE-A-2000-15060` | Alta |
| Sanciones alimentarias | **Ley 17/2011**, arts. 51-53 | `boe.es/buscar/act.php?id=BOE-A-2011-11604` | Alta |
| Sanciones de consumo | **TRLGDCU** (RDLeg 1/2007), arts. 47-50 | `boe.es/buscar/act.php?id=BOE-A-2007-20555` | Alta |
| Hojas de reclamaciones, precios visibles, horarios, ruido | **Boletines y portales autonómicos** (BOJA, DOGC, BOCM, DOGV, BOPA) + portales de consumo de cada comunidad; **ordenanza acústica y de horarios del ayuntamiento** | Varias | Alta cuando el boletín abre. ⚠️ **El DOGC es una SPA en JavaScript, el BOCM de 2010 devuelve 404 y el BOPA no fue accesible**: L3 tuvo que reconstruir varios por espejo |
| Videovigilancia y datos de clientes | **AEPD**, Guía de videovigilancia | `aepd.es/guias/guia-videovigilancia.pdf` | Alta |
| Trazabilidad | Guía AESAN/MAPA | ⚠️ **El PDF de `aesan.gob.es` devuelve 404 hoy**; se lee la edición publicada por el Gobierno de Aragón, que es el mismo documento | Media |
| Derechos de música | **SGAE**, Libro de Tarifas Generales · **Somos Música** (AGEDI + AIE) | `sgae.es/clientes-usuarios/` | SGAE **Alta** · ⚠️ **AGEDI-AIE sin fuente vigente: su enlace de tarifas da 404** |
| Estructura de costes de referencia | **CaixaBankLab × elBullifoundation**, metodología Sapiens | `caixabanklab.com/elbullifoundation/es/consumos-beneficios-restaurante/` | Alta, ⚠️ **la página no lleva fecha visible: citar «sin fecha», nunca inventar el año** |
| Mercado de trabajo y absentismo | **Randstad Research** | `randstadresearch.es` | Media |
| Tamaño y coyuntura del sector | **Hostelería de España**, Anuario | ⚠️ **De pago (1.800 €/año)**: las cifras vienen de prensa que las reproduce | Media |
| **Sus propios números** | Su **convenio provincial**, su **TPV**, sus **nóminas** y su **hoja de reclamaciones autonómica** | — | El manual tiene que insistir: **el dato bueno es el suyo** |

**Regla de redacción derivada (§7-bis.21 de la SPEC de familia, «sin fuente, no entra»):** el manual **enseña a consultar** estas fuentes, no las sustituye con una tabla que caduca. Y añade la comprobación que nadie enseña: **abrir la ficha del BOE y mirar si dice «Norma derogada»**.

---

## 5. KPI y benchmarks CON fuente (lo demás, a la lista negra del §11)

### 5.1 Estructura de costes y prime cost

| Dato | Valor | Fuente | Fiabilidad |
|---|---|---|---|
| Coste de producto sobre venta | **30 %** (comida 28 %, bebida **34,5 %**; mix de ingresos 70/30) | CaixaBankLab × elBullifoundation, metodología Sapiens | **Alta** ⚠️ sin fecha visible |
| Coste de personal, **servicio en mesa** | **30-35 %** de la venta neta | Ídem | **Alta** |
| Coste de personal, **barra/autoservicio** | **15-25 %** | Ídem | **Alta** |
| Alquiler · generales · EBITDA sano | ≤ **5 %** (hasta 10 % en algunos modelos) · **17 %** ideal (13-20 %) · **10-13 %**, por debajo del 10 % toca reestructurar | Ídem | **Alta** |
| **Prime cost objetivo** | **≤ 65 %** con servicio en mesa · **≤ 55 %** en barra/autoservicio | **Derivado** de las dos filas anteriores (misma decisión D5 de la Guía Food Cost) | **Derivado — se marca como tal** |
| Prime cost 60-65 % | Referencia de **EE. UU.** | Toast / restaurantowner.com | Media — **se cita como convención americana, nunca como dato español** |

> **El matiz contraintuitivo que hay que explicar, no simplificar:** según la fuente española más sólida, **la bebida tiene PEOR food cost (34,5 %) que la comida (28 %)** sobre sus respectivos ingresos. El margen **absoluto** por unidad sí suele ser mayor; el porcentual, no.

### 5.2 Coste laboral y formación (INE, fuente primaria — el bloque más fuerte del research)

| Dato | Hostelería | Media nacional | Fuente | Fiabilidad |
|---|---|---|---|---|
| Coste laboral bruto por trabajador/año (2025) | **23.690,02 €** — **el más bajo de las 19 secciones de actividad** | 38.748,94 € (+3,3 %) | INE, EACL 2025 (publ. 23-07-2026) | **Alta** |
| Sueldos y salarios por trabajador/año (2025) | **17.190,75 €** — **el más bajo de todas las secciones** | 28.410,78 € (+3,1 %) | Ídem | **Alta** |
| **Gasto en formación profesional** por trabajador/año | **20,14 €** | **76,49 €** (la hostelería invierte el **26 %** de la media) | Ídem | **Alta** |
| Beneficios sociales por trabajador/año | 211,42 € | 531,46 € | Ídem | **Alta** |
| Coste laboral de hostelería sobre la media | **61,1 %** | — | Cálculo propio sobre el INE | Alta (derivado) |
| Coste laboral/año, «Servicios de comidas y bebidas» | 20.658 € (+0,8 %) | — | brainsre citando la EACL | Media (el desglose por división no está en la nota de prensa) |

> **El dato del 20,14 € es la mina del manual**: la hostelería invierte en formar a su gente **una cuarta parte** de lo que invierte la media de la economía española. Es el argumento numérico —con fuente primaria— de todo el eje de personas.

### 5.3 Salario, cotización y convenio

| Dato | Valor | Fuente | Fiabilidad |
|---|---|---|---|
| **SMI 2026** | **1.221 €/mes** en 14 pagas · **40,70 €/día** · **17.094 €/año** (+3,1 %, efectos desde el 1-01-2026) | RD 126/2026 (BOE 19-02-2026) | **Alta** |
| Cotización por contingencias comunes | **28,30 %**, de los que la **empresa paga el 23,60 %** y el trabajador el 4,70 %; tope de base **5.101,20 €/mes** desde el 1-01-2026 | Orden PJC/297/2026 | **Alta** |
| Convenio de **Madrid**: cocinero/a nivel III · jefe/a de cocina | **1.160,37-1.283,83 €/mes** · 1.250,91-1.415,47 € — convenio **expirado el 31-12-2025, aplicándose por ultraactividad** | BOCM 06-04-2024 (research interno, ids CONV-02..07) | **Alta** |
| Convenio de **Cataluña**: *cuiner/a* Barcelona · *cap de cuina* | **1.607,25-1.803,05 €/mes** · hasta 2.121,29 € — vigente 2025-2028 | DOGC 23-03-2026 | **Alta** |
| **Diferencia entre provincias, mismo puesto** | **40-50 %** | Derivado de las dos filas anteriores | **Alta (derivado)** — es la mejor prueba de por qué el manual **no puede dar una cifra única de nómina** |
| Salario medio en hostelería vs media nacional | 1.512 € vs 2.345 €/mes (**−35 %**) | Synergie España 2026, vía InfoHoreca | Media (secundaria) |
| Salario de un gerente de restaurante en España | **18.000 € – 95.200 €/año según la fuente** (Wageindicator 1.593-2.383 €/mes · Glassdoor 30.330 € media, p90 95.200 · InfoJobs 20.500 € + variable · HuffPost 2.500-3.800 €/mes · Barcelona Culinary Hub 25.000-33.000 · Ostelea 18.000-24.000) | L2 §2.11 | **Ninguna explica la varianza.** El manual lo presenta como **rango con sus fuentes**, nunca como «el salario» |
| Fuera de España (referencia, no cita de oferta) | MX **15.000-18.000 MXN netos**/mes · CO **2-6 M COP**/mes · GT **Q3.000-11.000**/mes · AR $59.641/mes media · PE **S/ 1.994-6.221**/mes al empezar · CL $717.794-1.804.491/mes | L4 §2 (Computrabajo, OCC, elempleo, Wageindicator) | Media |

### 5.4 Personal: rotación, absentismo y temporalidad

| Dato | Valor | Fuente | Fiabilidad |
|---|---|---|---|
| **Temporalidad en hostelería** | **12,6 %** (media nacional 15,5 %); indefinidos sobre asalariados **87 %** | Randstad Research, 1T 2026 | Media |
| Ocupados en hostelería (EPA) | **1,77 M** (7,9 % del empleo); comidas y bebidas **1,3 M (76 %)** | Ídem | Media |
| Absentismo **general** y **del sector servicios** | **7,1 %** de las horas pactadas (IT: 5,5 %) | Randstad Research, 4T 2025 | Media ⚠️ **NO existe desglose de hostelería: no atribuirle esta cifra** |
| Empresas de hostelería con dificultades para encontrar personal | **75 %** (69 % «algunas» + 6 % «muchas»); global 74 %, Europa 76 % | **ManpowerGroup**, *Talent Mismatch 2026*, nota de prensa propia (06-05-2026) | **Alta (primaria)** |
| Tasa de rotación 63,8 % · coste de reemplazo 2.800-5.000 € | — | Linkers / Synergie / Randstad — **tres atribuciones distintas, informe original no publicado** | **LISTA NEGRA (§11)** |

### 5.5 Gestión, tiempo y control de los números

| Dato | Valor | Fuente | Fiabilidad |
|---|---|---|---|
| **Sólo el 39 % revisa su rentabilidad cada semana** (50 % mensual), pese a que el **70 %** dice tener una situación económica sólida | — | **TheFork**, *Retos y Desafíos de la Restauración en España*, 615 profesionales (18-03-2026) | **Alta (primaria)** — es el dato que justifica el cuadro de mando semanal |
| Horas semanales que un hostelero dedica a administración, supervisión y formación | **38 h** | **Square + American Express**, *Recupera tu Tiempo*, 152 propietarios + 6 entrevistas (mar-may 2024) | **Alta (primaria)** |
| Considera la gestión de personal «muy estresante» | **77 %** | Ídem | **Alta (primaria)** |
| La generación y gestión de datos del negocio es su reto principal | **37 %** | Ídem | **Alta (primaria)** |
| Ahorro al automatizar inventarios | **4 h/semana** | Ídem (declaración de Gonzalo Saenz, Square España) | Media (declaración, no medición publicada) |

### 5.6 Cliente: reseñas, esperas y no-shows

| Dato | Valor | Fuente | Fiabilidad |
|---|---|---|---|
| **Una estrella más en Yelp → ingresos** | **+5 a 9 %** | Luca, M., **HBS Working Paper 12-016** (2011, rev. 2016), PDF leído | **Alta** |
| El efecto lo mueven **los independientes**; las cadenas no se ven afectadas por su rating | — | Ídem | **Alta** |
| **Media estrella más → agotar mesas en hora punta** | **+19 puntos porcentuales (+49 %)** | Anderson & Magruder, *The Economic Journal* **122(563): 957-989** (2012), PDF leído | **Alta** |
| Reputación online en hoteles: +1 % de índice | ADR **+0,89 %** · ocupación **+0,54 %** · **RevPAR +1,42 %**; +1 punto en escala de 5 permite subir precio **+11,2 %** | Cornell (C. K. Anderson, 2012) | Media ⚠️ **el PDF original está caído (eCommons devuelve 405)**: cifras del comunicado oficial |
| Eliminar la espera → ingresos | **+15 %** (simulación; muestra de **94.404 clientes**, 12 meses) | De Vries, Roy & De Koster, *Journal of Operations Management* **63(1)** (2018) | **Alta** ⚠️ **trabajo de campo en un restaurante de India: evidencia internacional, no benchmark español** |
| **Tasa de no-show en España** | **3,3 %** (3,6 % en 2024); Sevilla 3,7 %, Barcelona 3,5 %, Madrid/Málaga 3,3 %, Valencia 3,2 %, Alicante 3,1 % | TheFork, 2025 | Media |
| Reconfirmación por **SMS** | no-show del **1,92 % al 1,52 %** (**−21 %**) | CoverManager, muestra de 9.500 restaurantes | Media |
| Reserva **garantizada con tarjeta** | no-show al **0,66 %** (**−66 %**) | Ídem | Media |
| Restaurantes que ya piden garantía bancaria · prepago | **21 %** (el doble que en 2023) · **7 %** (el triple) | TheFork, 2025 | Media |
| **Propinas**: quién la deja | **25 % siempre · 15 % nunca · 58 % según la experiencia** | TheFork Lab, +4.500 usuarios (2026) | Media |
| **Propinas**: cuánto | **63 % deja menos del 5 %** · 35 % entre el 5 y el 10 % · **sólo el 2 % supera el 10 %**; el **77 %** la eliminaría | Ídem | Media |

### 5.7 Sector: tamaño, ticket y coyuntura

| Dato | Valor | Fuente | Fiabilidad |
|---|---|---|---|
| Empresas de hostelería (DIRCE, 1-01-2025) | **266.476**; sin asalariados **63.063 (23,7 %)**; con 20 o más **6.736 (2,5 %)** | INE | **Alta** |
| Cifra de negocios de Hostelería (2024) | **117.440 M€** (+12,4 %); personal ocupado **1.748.137** | INE, EEE Servicios | **Alta** |
| Ventas por ocupado | **67.180 €/año** | Cálculo propio sobre el INE | Alta (derivado) |
| Facturación del sector según la **patronal** (2024) | **166.211 M€**, de los que restauración **116.193 M€**; empleo 1,85 M; **más de 300.000 locales** | Hostelería de España, Anuario 2025 | Media |
| **Facturación +3,1 % y rentabilidad −0,9 %** en 2025 | — | Ídem | Media — **es el dato que justifica el manual entero: más ventas con menos margen** |
| Restauración: VAB, empleo, productividad | **66.961 M€ (4,9 % del VAB)** · 1.377.235 empleos · **46.932 €/empleado** · **+44,3 %** de productividad sobre la UE-27 · coste laboral **−30 %** sobre la UE-27 · 73 % microempresas · parcial 23,3 % · **1 bar por cada 281 habitantes** | Informe Ivie/Cajamar (19-11-2025) | Media ⚠️ la nota de `ivie.es` no abre (error TLS); verificada por dos réplicas del emisor |
| **Ticket medio de la restauración española** | **21 €** (Baleares 35 € máx., Álava 16,5 € mín.; turista extranjero 31,2 €) | CaixaBank Research, 1S 2025 | Media ⚠️ **es por TICKET, no por cubierto; y no existe cifra pública del segmento de alta cocina** |
| Ticket medio **+2,5 %** frente a inflación del sector **+4,6 %** | → **contracción del gasto real**; satisfacción del consumidor −1,1 % | Delectatech, 2025 | Media |
| Gasto total en restauración | **43.500 M€** (+2,4 %); ≈7.200 M visitas; cadenas **+5 %** vs independientes **+0,8 %** | Circana, 2025 | Media |
| Cierres de establecimientos | **31,1 al día** (≈11.183 en el año), frente a 37,5/día en 2024 | Delectatech, 2025 | Media — **es un recuento absoluto, NO una tasa de fracaso** |
| Supervivencia empresarial (todos los sectores) | **76,9 %** a 1 año · **63,5 %** a 3 · **41,9 %** a 5 | INE, Demografía Armonizada de Empresas | **Alta** |

> ⚠️ **No mezclar INE con Hostelería de España en la misma tabla:** 117.440 M€ frente a 166.211 M€ son metodologías distintas, y **266.476 son EMPRESAS (DIRCE) mientras que «más de 300.000» son LOCALES** (patronal). Elegir una fuente y ser coherente en todo el manual.

### 5.8 Los KPI de riesgo: cuánto cuesta equivocarse (todo Alta, todo BOE)

| Ámbito | Leve | Grave | Muy grave |
|---|---|---|---|
| **Relaciones laborales** (art. 40.1 LISOS) | 70-750 € | **751-7.500 €** | 7.501-**225.018 €** |
| **Prevención de riesgos** (art. 40.2 LISOS) | 45-2.450 € | 2.451-**49.180 €** | 49.181-**983.736 €** |
| **Fraude en temporales** (40.1.c bis) | 1.000-2.000 € | 2.001-5.000 € | 5.001-**10.000 € ⚠️ por cada trabajador** |
| **Falta de alta en la Seguridad Social** (40.1.e) | 3.750-7.500 € | 7.501-9.600 € | 9.601-**12.000 € ⚠️ una infracción por cada trabajador**, +20 % con 2 afectados y hasta +50 % con 5 o más |
| **Seguridad alimentaria** (Ley 17/2011, art. 52) | ≤ 5.000 € | 5.001-20.000 € | 20.001-**600.000 €** + **cierre de hasta 5 años** |
| **Consumo** (TRLGDCU, arts. 48-50) | 150-10.000 € | 10.001-100.000 € | 100.001-**1.000.000 €** ⚠️ y **pueden sobrepasarse hasta entre 2 y 8 veces el beneficio ilícito**: la multa no tiene techo nominal |
| **Ruido** (Ley 37/2003, art. 29) | ≤ 600 € | 601-12.000 € | 12.001-**300.000 €** + clausura de 2 a 5 años |
| **Desperdicio alimentario** (Ley 1/2025, art. 21) | ≤ 2.000 € | 2.001-60.000 € | 60.001-**500.000 €** |
| **RGPD** (arts. 83.4 y 83.5) | — | 10 M€ o el **2 %** del volumen global | 20 M€ o el **4 %** — la mayor de las dos |

Prescripción (art. 4 LISOS): 3 años en el orden social, 4 en Seguridad Social; en PRL, 1 año las leves, 3 las graves y 5 las muy graves.

---

## 6. Voz del cliente (L4): dolores, exigencias reales, vocabulario y objeciones

### 6.1 Los 11 dolores → qué capítulo y qué herramienta los resuelven

| Dolor | Evidencia (la más fuerte de cada grupo) | Capítulo | Herramienta |
|---|---|---|---|
| **A. Rotación y falta de personal** | **[PRIMARIA]** Chema Fernández (ManpowerGroup España, 06-05-2026): «La hostelería se enfrenta a un reto de talento que va más allá de la escasez de candidatos. Las empresas necesitan profesionales con actitud, competencias y orientación al cliente» — con el **75 %** de las empresas del sector reconociendo dificultades. **[PRIMARIA]** Paco Quirós, propietario de 8 restaurantes (El Español, 03-09-2026): «**Tengo un 60 % de rotación, he tenido que aprender a convivir con ello**» | 10, 13 | 2, 4 |
| **B. Cuadrantes y bajas de última hora** | **[PRIMARIA]** Juanjo Gondar, gerente del Asador Lapamán (Cuatro.com, 29-04-2026), sobre pasar del turno partido al continuo: «**Trabajan mejor, mucho más motivados**». Juan Pablo Domínguez, encargado de Hakuna, describiendo el partido: «Vienen a las 11:00, se van a las 16 y vuelven las 19» | 11 | (kit-gestion-personal/01) + 2 |
| **C. Presión del propietario y falta de autonomía** | **[PRIMARIA]** Dueño de un bar de Sant Feliu de Llobregat (Infobae, 09-09-2025): «**He dejado a mi familia de lado. Mis hijos me han perdido toda su infancia**» — y a la pregunta de si repetiría: «**No**». **[indicio]** ILO Restaurante anuncia «**gestionar con autonomía real**» como reclamo del puesto: se vende como diferencial porque no es lo normal | 7 | 1, 5 |
| **D. Falta de procedimientos escritos** | Barra de Ideas (06-06-2026): «**Si se marcha, el local tiembla**» · la diferencia entre «gestionamos por personas» y «gestionamos por sistema» | 1, 5, 20 | 6, 7, 8 |
| **E. Reseñas negativas y quejas** | **[PRIMARIA]** Mismo dueño de Sant Feliu: «**Los clientes son lo más difícil de gestionar**… tienes un 10, un 15 % que…» | 17 | 3 |
| **F. Control de caja y mermas** | Diferencia entre **corte** (cambio de turno), **arqueo** (foto del efectivo) y **cierre** (contabilidad del día): quien sólo hace uno se queda ciego ante fugas que aparecen en otro | 6 | (kit-tareas/09) + 1 |
| **G. Conflictos y burnout** | **[PRIMARIA]** Diego Coquillat: «Priorizar la salud y bienestar del trabajador es el principal aspecto a la hora de reducir el impacto del burnout»; señales de alerta = «cambios inexplicables en su rendimiento físico, capacidad de trabajo y humor» | 7, 14 | 7 |
| **H. Formación de nuevos** | Objetivo del primer día: «pasos que debe seguir, cuáles serán sus funciones, el horario, quién será la persona de contacto, las expectativas, la formación de inducción» (Mapal). **Y el dato duro del INE: 20,14 € frente a 76,49 €** | 10 | 4, 2 |
| **I. Comunicación cocina-sala** | Barra de Ideas (27-02-2026): «Un plato que sale tarde. Una comanda mal cantada. Una alergia que no llegó a cocina. Y entonces, miradas. Suspiros. Fricción.» · «**La comunicación interna en restauración no es un concepto bonito para colgar en la pared. Es un sistema operativo. Sin él, el servicio chirría**» | 16 | 7 |
| **J. No entender los números** | **[PRIMARIA]** Jay Kim (TheFork Iberia, 18-03-2026): «el contexto actual exige dar un paso más en términos de gestión operativa y eficiencia» — con **sólo el 39 % revisando su rentabilidad semanalmente**. **[PRIMARIA]** Square+AmEx: **38 h/semana** en administración y **77 %** que vive la gestión de personal como «muy estresante» | 2, 3, 4 | 1 |
| **K. Cumplimiento legal e inspecciones** | Es el dolor peor servido del mercado (§7) y el que más caro sale (§5.8). ⚠️ Las cifras concretas que circulan sobre la ITSS **no se pudieron verificar** y van a la lista negra | 6, 8, 9, 11, 12, 15, 19, 20 | 6 |

### 6.2 Qué exigen las ofertas de empleo reales → el índice

15 ofertas/fuentes analizadas (9 España, 4 Colombia, 1 México, 1 Guatemala) más benchmarks agregados de AR/PE/CL/PA.

| Función | Aparece en | Dónde va en el manual |
|---|---|---|
| Supervisión y coordinación del equipo / operación diaria | **15/15** | Caps. 5, 7, 16 |
| Control de costes / gestión de inventario | **12/15** | Caps. 2, 3, 4 (+ cross-sell a Kit de Inventario y Guía Food Cost) |
| Cumplimiento normativo (seguridad alimentaria, APPCC, sanitario) | **8/15** | Caps. 15, 19 |
| Formación y desarrollo de personal | 7/15 | Caps. 10, 13 |
| Gestión de caja / procesos financieros | 6/15 | Cap. 6 |
| Gestión de eventos / banquetes | 3/15 | Se menciona, no es eje (lo cubre el Kit de Catering) |
| **KPIs explícitos (Food Cost, Payroll, GOP, ticket medio)** | **2/15 — y las dos son cadenas hoteleras** (Minor Hotels y Grupo Quispe) | Caps. 2, 3, 4 |
| Marketing / redes locales | 2/15 | Cap. 17 (reseñas y reputación) |

> **La lectura que vale por todo el bloque:** al manager de un negocio **independiente** se le pide «gestión integral» y «supervisar» —descripción operativa y difusa—, mientras que **sólo las cadenas hoteleras le piden explícitamente saber leer KPIs concretos**. Es decir: la mayoría de los managers de restaurante independiente **no tiene ni en su propia oferta de trabajo la lista de qué números debe controlar**. Encaja exactamente con el 39 % de TheFork. **Ese es el producto.**

### 6.3 Vocabulario por mercado (decisión ya tomada por el research: NO se hacen versiones por país)

| Concepto | Término principal | Equivalencia en la primera mención |
|---|---|---|
| El puesto | **Manager** (anglicismo asentado: aparece literalmente en **4 de las 9 ofertas españolas** revisadas) | **(gerente / encargado)**, y **«administrador»** al citar Colombia, Chile o Perú, donde es el término dominante |
| Documento de turnos | **Cuadrante de turnos** | **(horario del personal / rol de turnos)** — «rol» es el término argentino |
| Verificación de caja | **Arqueo / cierre de caja** | **(corte de caja)** — en México el corte es el paso de cambio de turno, **no** el cierre: hay que decirlo, no traducirlo |
| Personal de sala | **Camarero/a** | **(mesero/a · mozo/a · garzón)** |
| Espacio de servicio | **Sala** | **(salón)** — «salón» se entiende en los 6 mercados; «sala» está marcado como España |
| Ticket a cocina | **Comanda** | universal en los 6 mercados como jerga de oficio: no se adapta |
| Verbo | **Pedir** | nunca «ordenar» como verbo principal: sólo funciona en México |
| Pago de personal | **Nómina** | **(planilla)** en Perú · «recibo de sueldo» en Argentina. ⚠️ **El recargo sobre el salario bruto varía muchísimo por país** (≈45 % en Perú, ~152 % del salario base en Colombia con todas las prestaciones): el manual **no puede dar una fórmula única de coste del empleado**; el % va en celda |
| Control horario | **Registro de jornada** | **(control de asistencia / control horario)**. El marco legal es **español**: la sección de cumplimiento dice explícitamente «consulta tu normativa local» |

**Y todo lo que SÍ viaja sin cambios** —y por tanto es el núcleo defendible fuera de España—: la gestión de turnos y cuadrantes, los KPI de sala y cocina, la lectura de la cuenta de resultados, el control de caja como método, el APPCC como sistema, la gestión de reseñas, los rituales de liderazgo y el pre-shift, y la selección con scorecard.

### 6.4 Las 6 objeciones y cómo se desmontan

| # | Objeción | Cómo se desmonta (sin marketing) |
|---|---|---|
| 1 | **«Ya hay plantillas y checklists gratis»** | Es cierto y no se debe negar (ManualDelRestaurante.com regala 20 manuales y 7 calculadoras; hay paquetes de 30-40 plantillas). El valor no es tener una plantilla: es el **criterio que conecta las plantillas sueltas** —cuándo usar cada una y qué hacer con lo que sale— más los 5 ejes integrados **y el bloque normativo verificado**, que ninguna plantilla gratuita trae |
| 2 | **«Esto es para cadenas, mi negocio es pequeño»** | **Refutada por una fuente identificada**: Barra de Ideas (06-06-2026) sostiene que pequeños y grandes comparten los **mismos 7 problemas estructurales** y sólo cambia la escala. El manual lo hace explícito con **un ejemplo por escala** (independiente de 8-15 personas vs grupo de varios locales) — sin fingir que un solo local necesita la misma profundidad de sistemas. Y hay un dato objetivo: el **73 % de las empresas de restauración son microempresas** y el 23,7 % de las de hostelería **no tienen ni un asalariado** |
| 3 | **«Llevo años en esto, ¿qué me va a enseñar un libro?»** | Confirmada **literalmente** en dos reseñas de Amazon: Juan Manuel Vera (2★): «Hay algunos temas interesantes pero tratados demasiado básicos. **Parece más bien un conjunto de entradas de blog**». Se desmonta empezando donde termina lo gratuito: los **18 conceptos del §1**, los **12 errores comprobables del §2**, y **casos resueltos con cifras**, no teoría |
| 4 | **«Es caro para lo que es»** | Confirmada: Jorge H. (3★, desde México, 02-12-2025), título de la reseña: «**Costoso**». Se desmonta **sin ocultar el precio**: al lado de lo que cuesta un año de SaaS de gestión (**1.140-2.100 €/año** en Last.app, precio oficial) y de lo que cuesta **una** sanción grave (751-7.500 € en laboral, 5.001-20.000 € en alimentaria) |
| 5 | **«Mi jefe no me va a dejar aplicar nada»** | ⚠️ **Sin cita textual verificada** (el intento falló por certificado SSL); la evidencia indirecta sí se sostiene. El manual **no puede prometer autonomía**: ofrece el **cap. 7**, «cómo defender un cambio ante el propietario con números», que es lo único que un manager sin autoridad formal sí controla |
| 6 | **«No me fío de comprar un documento sin verlo»** | Objeción estándar de infoproducto, sin fuente específica en este research. Se resuelve como en el resto del catálogo: índice completo en la landing, capturas reales de los Excel y garantía de 30 días |

### 6.5 Qué formato pide el comprador

- **Penaliza el relleno, no la extensión.** Las dos quejas más duras de las 7 reseñas analizadas van en la misma dirección: «un tercio del libro dedicado a explicar matrices básicas» y «**interlineados y márgenes grandes para que ocupen más páginas**» (oriol, 3★). **Ninguna de las 7 critica que un libro sea demasiado corto.**
- **Premia la aplicabilidad inmediata.** Jules (5★, 08-03-2026): «Un manual de gestión sencillo y práctico que podrás **ejecutar en tu negocio desde el minuto 1**».
- **No tiene tiempo:** 38 h semanales en administración y 77 % de estrés en gestión de personal (Square+AmEx).
- **Conclusión de formato:** **capítulos autoconclusivos por eje**, que se lean sueltos, cada uno con al menos un caso resuelto con cifras y una herramienta aplicable. Es el mismo patrón validado en la Guía Food Cost.

---

## 7. Competencia: el hueco, confirmado producto a producto

### 7.1 El censo: 36 productos de pago, ninguno completo

L1 censó **36 productos** en 4 familias (11 libros, 8 manuales/plantillas de pago único, 10 cursos y másteres, 7 SaaS) con precio verificado por URL, marcando «sin fuente (precio)» en 9 de ellos. Y puntuó 13 con detalle suficiente sobre 10 ejes.

> **Ningún producto del censo, ni de pago ni gratuito, tiene «Sí» simultáneo en Operaciones + Personas + Finanzas + Servicio + Liderazgo + Legal España + Excel con fórmulas vivas + Pago único.**

Los cuatro motivos, uno por familia:

1. **Los libros son texto puro.** Ninguno de los 11 trae Excel operativo.
2. **Las plantillas Excel son sólo Excel.** Las 40 de IngenieriadeMenu.com (39,70 €) no llevan detrás un documento largo, sino una guía de uso corta.
3. **Los cursos caducan.** Aprendum da 6 meses de acceso; BCC/Mondragon es una edición con fechas fijas. No son documento de consulta permanente.
4. **El SaaS no es un documento y es 100 % recurrente.** Exige alimentar datos cada día y cuesta 50-349 €/mes por local.

### 7.2 Los dos hallazgos que valen por todo el análisis

**(a) El competidor de formato más parecido existe… y es LATAM.** «Administración Pro para Restaurantes» (Hotmart, **89,54 €**) junta curso + manual + **8 manuales de operaciones en Excel**. Es la **prueba de concepto** de que el mercado compra este formato. Y su punto ciego es exactamente nuestro punto fuerte: **no menciona en ningún punto verificable terminología ni normativa española** (IVA de hostelería, registro de jornada, APPCC, hojas de reclamaciones, convenio colectivo).

**(b) El recurso gratuito más prestigioso del mercado NO es un manual de gestión: es una guía de apertura.** El manual de **elBullifoundation × CaixaBank** son **557 páginas** — y una búsqueda de términos sobre el PDF completo con PyMuPDF devuelve:

| Término | Páginas en que aparece |
|---|---|
| registro horario · KPI · prime cost · briefing · reseñas · onboarding · evaluación del desempeño | **0** |
| APPCC | 1 |
| convenio colectivo · reclamaciones | 2 · 3 |
| alérgenos | 4 |
| turnos | 9 |
| nómina | 11 |

Su índice confirma que el 100 % del contenido indexado es «cómo abrirlo»: empresa, papeleo, conceptualización, oferta, local, plan económico y financiación. **Ni el recurso gratuito más extenso y prestigioso del mercado en español cubre la operación diaria de un restaurante ya abierto.**

### 7.3 Precios del mercado (comparables para el §9)

| Formato | Rango confirmado |
|---|---|
| Manual de un solo tema (Formahostel) | **6,75 €** |
| Libros en euros confirmados | **7,59 – 23,95 €** |
| 40 plantillas Excel (IngenieriadeMenu) | **39,70 €** (normal 79,40 €) |
| Cursos online con descuento agresivo | **49 – 150 €** — **acceso caducable a 6 meses** |
| **Bundle curso + manual + Excel (Hotmart, LATAM)** | **89,54 €** |
| Curso institucional (BCC/Mondragon, 8 ECTS) | **2.200 – 2.310 €** |
| Másteres (BCC F&B, Barcelona Culinary Hub) | **8.200 – 12.275 €** |
| **SaaS de gestión por local** | **50 – 349 €/mes** → Last.app Growth **1.140 €/año**, Unlimited **2.100 €/año**, **+500 € de instalación** |

### 7.4 Qué hace bien la competencia y copiamos

1. **«Manual de trabajo diario»** — así se vende «El Nuevo Gerente de Restaurante» (Hotmart). Enmarca el producto como herramienta de consulta constante, no como lectura de una vez. **Lenguaje directo para el copy.**
2. **La estructura del bloque legal de elBullifoundation**: constitución → trámites administrativos → obligaciones contables → fiscales → laborales → licencia → higiénico-sanitarios, y al final de cada bloque **«¿quién se ocupa de las tareas?»**. Ese patrón de checklist de responsabilidad encaja perfectamente con el eje de operaciones.
3. **La transparencia de compatibilidad de IngenieriadeMenu.com**, que avisa de que sus plantillas no funcionan en Sheets ni Numbers. Nosotros lo decimos **a favor**: nuestras convenciones prohíben `INDIRECT`, `COUNTA`, `PMT` y `OFFSET` justamente para que funcionen.
4. **La autoridad de nicho de *Host*** (Abel Valverde, ex director de sala de Santceloni): se vende por quién lo firma. Aquí, la bio de John (29 años de alta hostelería + 15 de consultoría) hace ese trabajo y ya está anclada en el pipeline.
5. **La certificación por test ≥60 %** de Aprendum y estudioformacion: credencial barata de producir con valor percibido alto. **No es el foco, pero es una idea a valorar** para una versión futura.

### 7.5 Yumminn, fuera del censo

Se investigó por figurar en el encargo: **quebró en 2025** (Juzgado de lo Mercantil nº 11; su dominio ya no resuelve por DNS, verificado). No es competidor vivo.

---

## 8. Propuesta de ÍNDICE: 20 capítulos + bonus

Cada capítulo va con guion cerrado en `guion_manual_manager_restaurante.py` (epígrafes, cifras que debe citar referenciadas a celda de los xlsx o a ids `MM-*`, tablas exigidas y prohibiciones). Presupuesto: **1.400-1.600 palabras/capítulo → ~30.000 palabras**. Con la calibración medida de la Guía Food Cost (30.000 palabras → **95 páginas**), la promesa interna del gate va en **60** y **la landing publica la cifra MEDIDA tras construir** (decisión D17 de la familia).

| # | Título | Eje | Contenido obligatorio | Herramienta | ids `MM-*` |
|---|---|---|---|---|---|
| 01 | **Qué es exactamente un manager de restaurante (y para quién es este manual)** | Liderazgo | Gerente / encargado / director / jefe de sala / administrador con el **organigrama real del ALEH VI** (6 áreas, 3 grupos); mapa «problema → capítulo → herramienta»; jerarquía con el Kit de Tareas, el de Personal, el Pack APPCC y la Guía Food Cost; qué NO vas a encontrar aquí | — | MM-14 |
| 02 | **Los números que gobiernan tu turno: 12 definiciones que casi nadie distingue** | Finanzas | Ticket medio vs gasto por cubierto vs ventas por hora; food cost, labor cost, prime cost, margen tras prime cost; rotación vs absentismo vs temporalidad; qué mide cada uno y cuál manda en cada decisión | 1 (hoja KPI y definiciones) | MM-41, MM-42, MM-47 |
| 03 | **El cuadro de mando semanal: por qué la semana y no el mes** | Finanzas | El 39 % de TheFork; qué se mide cada lunes en 15 minutos; cómo se lee un semáforo; la semana mala que el promedio mensual esconde | **1** | MM-41, MM-44 |
| 04 | **Prime cost y coste de personal: dónde se pierde el margen** | Finanzas | Estructura española 30 % + 30-35 %; umbral **≤65 % en sala / ≤55 % en barra** (derivado, con Toast como contraste EE. UU.); del salario bruto al coste-empresa (SS 23,60 %, tope de base); el coste laboral más bajo de las 19 secciones | 1 | MM-16, MM-17, MM-41, MM-42 |
| 05 | **El día del manager: apertura, servicio, cierre y handover** | Operaciones | El criterio detrás del checklist, no otro checklist: qué decide cada bloque del día, qué se delega, qué firma el manager; **cross-sell explícito a `kit-tareas/03` (110 tareas)** | (kit-tareas) + 7 | — |
| 06 | **La caja y el tique: corte, arqueo, cierre — y lo que viene** | Operaciones | Los tres pasos y por qué no son sinónimos; qué hacer con un descuadre que se repite; factura simplificada **hasta 3.000 €** en hostelería (400 € el límite general) y contenido mínimo del tique; **efectivo de 0 a 999,99 € y por qué no se puede ser cashless**; Verifactu 2027 y factura-e B2B con las simplificadas excluidas | (kit-tareas/09) + 6 | MM-37, MM-39 |
| 07 | **Mandar sin quemar al equipo: autoridad, delegación y cómo defender un cambio con números** | Liderazgo | Autoridad formal vs real; delegar sin perder el control; señales tempranas de burnout; **cómo llevar una propuesta al propietario con la cifra de la semana** (responde a la objeción 5); la conversación difícil | 1, 7 | MM-44 |
| 08 | **El convenio que te aplica: ALEH VI, tu provincia y lo que no se negocia** | Personas | ALEH VI (no el V); las **materias reservadas** que el convenio provincial no puede tocar (clasificación, periodo de prueba, formativos, régimen disciplinario); cómo se busca en **REGCON**; **40-50 % de diferencia salarial Madrid-Barcelona** para el mismo puesto; ultraactividad | 6 | MM-14, MM-15 |
| 09 | **Contratar sin fabricar un indefinido por accidente** | Personas | El contrato se presume indefinido; desapareció el de obra y servicio; circunstancias de la producción (6 meses / 1 año) y sustitución; **encadenamiento: 18 meses en 24 → fija**; fijo-discontinuo y su antigüedad por toda la relación; periodo de prueba del ALEH (90/60/45); formativos; **y que el fraude se sanciona por cada trabajador** | 6 | MM-09, MM-10, MM-11, MM-23 |
| 10 | **Selección con criterio y los primeros 30 días** | Personas | Scorecard y entrevista estructurada; lo que **no se puede preguntar** (art. 9.5 Ley 15/2022); onboarding; y las **cuatro formaciones distintas**: acogida, PRL en el momento de la contratación, manipuladores (sin carné oficial desde 2010) y APPCC específica; el 20,14 € del INE | **4** (+ kit-gestion-personal/04) | MM-30, MM-43 |
| 11 | **Jornada, cuadrante y registro de jornada: tres documentos que no son lo mismo** | Personas | 40 h de promedio (no 37,5); 12 h entre jornadas, 9 h diarias, día y medio acumulable en 14; los 15 minutos **sólo si lo dice el convenio**; 80 horas extra/año; complementarias; **estado REAL del registro digital** y los 4 años de conservación; **el nuevo régimen disciplinario del ALEH: 2 = leve, 3-4 = grave, ≥5 = muy grave**; la presunción de jornada completa en el parcial sin registro | (kit-gestion-personal/01-02) | MM-01 a MM-08 |
| 12 | **Permisos, vacaciones y conciliación sin sustos** | Personas | 30 días naturales y 2 meses de preaviso; **fallecimiento 2+2, no 5**; los 5 días de accidente/enfermedad grave y a quién alcanzan; **el permiso parental de 8 semanas NO es retribuido**; fuerza mayor familiar medida en horas; guarda legal (la concreción horaria **la elige la persona**); **adaptación de jornada: el silencio de la empresa la concede** | (kit-gestion-personal/05) | MM-08, MM-26, MM-27 |
| 13 | **Rotación, absentismo y polivalencia: qué se puede medir de verdad** | Personas | Las tres cosas separadas y la fórmula de cada una; qué dato existe y cuál no (**y por qué el 63,8 % no se cita**); la matriz de polivalencia y el punto único de fallo; el coste real de una baja calculado con **tus** datos | **2** | MM-42, MM-43 |
| 14 | **Evaluar, corregir y, si toca, despedir** | Personas | Evaluación con la ficha del kit; régimen disciplinario del ALEH; **audiencia previa obligatoria: 2 días para contestar, permiso retribuido si se aparta del servicio (novedad del 04-09-2026)**; objetivo 20 días/año (tope 12 mensualidades) puestos a disposición **con la carta**; improcedente 33/24; contratos anteriores a 2012; qué lleva un finiquito | (kit-gestion-personal/06) | MM-12, MM-13 |
| 15 | **Lo que obliga aunque seáis tres: igualdad, acoso, desconexión y PRL** | Personas / legal | **Registro retributivo sin umbral de plantilla** (un bar con 2 empleados lo necesita) y **protocolo de acoso sin umbral**; plan de igualdad desde 50 (con el cómputo real: parciales cuentan como una persona, temporales extinguidos a razón de 1 por cada 100 días); LGTBI a partir de **más** de 50; **política escrita de desconexión digital** (los grupos de WhatsApp de servicio); PRL: plan, evaluación, emergencias, y que **los reconocimientos médicos son voluntarios** | 6 | MM-18, MM-19, MM-20, MM-21, MM-28 |
| 16 | **El servicio: estándares, briefing y la conversación cocina-sala** | Servicio | Briefing vs reunión vs handover; guion de briefing de 7 minutos; estándares escritos; el conflicto cocina-sala como **problema de sistema, no de personas**; cómo se corrige en el momento sin humillar | **7** | — |
| 17 | **Quejas, hojas de reclamaciones y reseñas: tres cosas distintas** | Servicio | Protocolo de queja en sala; **la hoja oficial es competencia autonómica** (cartel obligatorio, plazos de respuesta: Cataluña 1 mes, Andalucía 10 días hábiles, y la hoja electrónica ya obligatoria en Andalucía desde mayo de 2026); quién responde las reseñas, en cuántos días y con qué tono; **+1★ = +5-9 % de ingresos y +½★ = +49 % de agotar mesas, y el efecto es sólo para independientes** | **3** | MM-45 |
| 18 | **Reservas, no-shows y datos del cliente** | Servicio | No-show del 3,3 % y qué lo baja (**SMS −21 %, tarjeta −66 %**); política de garantía y cómo comunicarla; el efecto medido de la espera; **RGPD: la reserva se gestiona por ejecución del contrato, sin consentimiento; el marketing sí lo exige aparte**; y el restaurante **sí** debe llevar registro de actividades de tratamiento | 3 | MM-46 |
| 19 | **Seguridad alimentaria y el local: de lo que responde el manager** | Legal / operaciones | **Cultura de seguridad alimentaria como obligación de la DIRECCIÓN** (Anexo II Cap. XI bis); APPCC simplificado **con responsable designado**; alérgenos y **por qué el cartel «consulte al personal» no basta sin soporte escrito**; temperaturas vigentes (63/4/8/−18 °C, enfriar 60→10 en 2 h, recalentar 74 °C/15 s); anisakis (−20 °C/24 h o −35 °C/15 h) y el justificante del proveedor; trazabilidad de un paso atrás; **registro autonómico, no RGSEAA**; ruido y limitador si hay altavoces; horarios; terraza y las **dos** paredes; SGAE **y** AGEDI-AIE; perros de asistencia; agua gratuita, envases y doggy bag | 6, 8 (+ pack-appcc) | MM-29 a MM-36, MM-38, MM-49 a MM-52 |
| 20 | **El calendario del manager, la auditoría interna y los 90 días siguientes** | Liderazgo / operaciones | Qué es obligación **con fecha fijada por norma** (registro diario, ascensor 2 años, gas 5 años, extintores) y qué se vende como tal sin serlo (campana, termómetros, plagas, formación); la auditoría interna puntuable; cómo se convierte todo lo anterior en 13 semanas con responsable y fecha; qué se mide en el mes 0 y en el mes 3 | **5, 6, 8** | MM-02, MM-22, MM-35, MM-40 |

**Cobertura de los ejes anunciados en el hub desde mayo:** operaciones (5, 6, 19, 20) · personas (8-15) · finanzas (2, 3, 4) · servicio (16, 17, 18) · liderazgo (1, 7, 20) · **cumplimiento legal, transversal y como diferenciador** (6, 8, 9, 11, 12, 14, 15, 19, 20).

### 8.1 El bonus: **«12 situaciones resueltas del manager»** — elegido y argumentado

De las tres opciones planteadas:

| Opción | Veredicto |
|---|---|
| **Kit de checklists imprimibles** | ❌ **Descartada.** Es lo único de las tres que **duplicaría lo que ya vendemos**: `kit-tareas/03-tareas-manager.xlsx` son 110 tareas y hay 11 kits más de checklists. Y es justo el formato que el mercado ya regala en paquetes de 30-40 plantillas (L4, objeción 1). Sería la pieza más fácil de criticar |
| **Guiones de reuniones y conversaciones difíciles** | ⚠️ **No como bonus suelto.** El contenido es valioso —los dolores G (burnout) e I (cocina-sala) lo piden— pero un cuaderno de guiones aislado corre el riesgo de leerse como relleno genérico, que es exactamente lo que penalizan las reseñas |
| **12 situaciones resueltas del manager** | ✅ **Elegida** |

**Por qué, en cuatro razones:**

1. **Es la respuesta directa a la objeción medida.** Las reseñas de 1★ y 2★ del nicho dicen «temas tratados demasiado básicos, parece un conjunto de entradas de blog» y «márgenes grandes para ocupar más páginas». Un caso resuelto con datos, protocolo y norma aplicable es lo contrario de eso.
2. **Reutiliza el molde exacto ya validado ayer.** El bonus de la Guía Food Cost son 12 ejercicios resueltos de 550-700 palabras con tabla (≈7.500 palabras) y **midió 32 páginas**. Mismo `BONUS` del guion, mismos gates, coste conocido.
3. **Absorbe la opción 2 sin sus riesgos:** las situaciones que necesitan una conversación **traen el guion literal dentro** (la conversación difícil, el briefing tras un servicio malo, la reunión con el propietario). Se queda lo bueno de los guiones y se pierde el relleno.
4. **Es lo que las ofertas de empleo describen como el trabajo real**: 15/15 piden «supervisión y coordinación de la operación diaria», que es exactamente resolver situaciones.

**Las 12 situaciones propuestas** (cada una: situación con datos, qué NO hacer, protocolo paso a paso, la norma que aplica, la herramienta del pack que se usa y —cuando la hay— el guion literal de la conversación):

1. Una baja a dos horas del servicio del viernes.
2. La caja descuadra 40 € tres días seguidos.
3. Un cliente pide la hoja de reclamaciones.
4. Una reseña de 1★ acusa al local de una intoxicación.
5. Un camarero lleva 19 meses encadenando contratos temporales.
6. La semana cierra con un prime cost del 71 %.
7. Una persona pide reducción de jornada por guarda legal justo en el turno de viernes noche.
8. Se presenta una inspección de Sanidad sin avisar.
9. Una empleada comunica una situación de acoso.
10. El cocinero clave se va y sólo él sabe hacer la partida fría.
11. El propietario quiere subir la carta un 10 % y tú tienes los números.
12. Hay que despedir por causas disciplinarias.

**Objetivo: ~7.500 palabras → ~30 páginas medidas**, mismo dimensionado que el bonus de food cost.

---

## 9. Precio

### 9.1 La escalera real del catálogo (45 productos, leídos de `src/data/products-catalog.ts`)

| Franja | Productos | Qué son |
|---|---|---|
| **9 €** | eBook Pro Prompts | 200+ prompts |
| **12 – 14 €** | Kit de Escandallos (12) · 12 kits de tareas (12) · Pack APPCC, Kit de Inventario, **Kit de Gestión de Personal**, Kit de Tareas (14) · kits CB (14) | Plantillas Excel operativas |
| **18 – 18,50 €** | kit-tareas-chef-privado · kit-tareas-hotel | Kits ampliados |
| **24 €** | Guía Dark Kitchen | 13 capítulos, +40 páginas |
| **29 – 35 €** | Planes de negocio (cafetería, food truck, bar-restaurante, panadería, tapas-bar) | Plan + financiero por formato |
| **39 €** | Kit Plan Financiero | 7 xlsx con modelo financiero completo |
| **45 €** | 4 planes de eventos (catering, chef privado, paellero, parrillero) | Plan + financiero de un formato de eventos |
| **55 €** | Plan Coctelería · **Guía Food Cost + Ingeniería de Menú** | La guía: **20 capítulos, 95 páginas medidas, 8 Excel y un bonus de 32 páginas — pero de UNA disciplina vertical** |
| **65 €** | **7 guías «Cómo Montar»** (casual, panadería-obrador, japonés, mexicano, nikkei, peruano) | 20 capítulos, 8-9 plantillas Excel, checklists y manual de operaciones |
| **85 €** | Guía Restaurante Gastronómico | 22 capítulos, 119 páginas, 18 xlsx |
| **89 €** | Mega Pack de Tareas | 11 kits juntos |

### 9.2 Recomendación: **65 €**

**Los cinco argumentos, uno por línea:**

1. **Amplitud, no capricho.** La Guía Food Cost (55 €) es **un producto vertical**: una disciplina, escandallo y carta. Este manual cubre **5 ejes + cumplimiento legal transversal**, 20 capítulos, **8 libros de Excel** y un bonus de 12 casos. En amplitud está en la franja de las guías «Cómo Montar» (65 €), no por debajo del producto más estrecho del catálogo.
2. **El ancla externa es oficial y aguanta:** **65 € es el 5,7 % de un año de Last.app Growth** (95 €/mes +IVA = 1.140 €/año, precio publicado en su web, más 500 € de instalación única) y **menos de lo que cuesta un mes** de cualquiera de sus tres planes. Y es **tuyo para siempre**.
3. **Queda por debajo del único competidor de formato equivalente.** El bundle de Hotmart que junta manual + curso + 8 Excel cuesta **89,54 €** y **no cubre España**. 65 € es «lo mismo, más barato, y con la normativa española verificada al BOE del día».
4. **Respeta la escalera sin colisiones.** No choca con 55 (vertical), ni con 85 (apertura de un formato concreto), ni con 89 (mega pack). Y la franja de 65 € **ya está establecida con 7 productos**: el hub la lee como «documento largo + herramientas», que es exactamente lo que es.
5. **Deja sitio para la categoría.** El **Manual del Chef Ejecutivo** es el nº 3 de la cola de productos nuevos. Si el primer manual sale a 55 €, la categoría nace pegada a la Guía Food Cost y no queda escalón; a 65 € la línea «Manuales operativos» nace con precio propio.

**Sin `priceOld` ni `discountBadge`** (decisión D2 de la familia: producto nuevo, sin «precio anterior de 30 días» que sostenga un tachado — art. 20 TRLGDCU / RDL 24/2021). **Sin `aggregateRating`, sin reseñas en el JSON-LD y sin testimonios inventados** (D3): la sección de testimonios se oculta con `items: []`, como ya hace la Guía Food Cost. El `bonusTotalLabel` describe el paquete; no inventa un valor.

### 9.3 Las alternativas, con su coste honesto

- **55 €** — paridad con la Guía Food Cost. Defendible si se quiere abrir barata una categoría nueva, **pero deja el producto MÁS ancho al mismo precio que el más estrecho**, y el hub los enseña uno al lado del otro. Además quema el escalón para el Manual del Chef Ejecutivo.
- **45 €** — capta volumen y es el único que compite de frente con las 40 plantillas de 39,70 €. Pero **desperdicia el ancla del SaaS** (el argumento más fuerte), sitúa el manual por debajo del Kit Plan Financiero (39 €) + un kit de 14 €, que es menos producto, y daría el precio por entregable más bajo de todo el catálogo.
- **49 € — VETADO**: es el precio tachado del Kit de Escandallos y chocarían en el hub (misma razón que en la Guía Food Cost).
- **89 €** — paridad con el bundle de Hotmart, pero **colisiona con el Mega Pack** y se acerca demasiado al gastronómico de 85 €, que tiene 119 páginas y 18 xlsx.

---

## 10. SEO y landing

### 10.1 Slug, title, H1, description

**Slug (ya decidido por el orquestador): `manual-manager-restaurante`** → `https://aichef.pro/manual-manager-restaurante`, `-access`, `-library`.

> ✅ **Corrección a L5 §4.3:** el prefijo `manual-` **ya está declarado** en `astro-site/public/robots.txt`, con sus dos reglas en **los 5 bloques de user-agent** (`Disallow: /manual-*-access` y `/manual-*-library`), y el comentario de cabecera ya lo documenta («manual- desde el 2026-09-04, Manual del Manager»). **No hay 10 líneas pendientes.** Está en el árbol de trabajo sin commitear: entra en el commit del producto. `astro.config.mjs` (filtro del sitemap, `/^\/[^/]+-(access|library)$/`) y `whatsapp-gate.py` son genéricos y no necesitan tocarse. **Aun así hay que correr `robots-gate.py`** tras el build: un comando, y aquí ya costó un mes de indexación de 26 posts.

| Elemento | Propuesta | Alternativas |
|---|---|---|
| **Title** (≤60) | **«Manual del Manager de Restaurante \| Operaciones y Equipo»** (56) | «Manual del Manager de Restaurante \| Guía Operativa 2026» (55) · «Manual de Operaciones para Gerentes de Restaurante» (50) |
| **H1** | **«El Manual del Manager de Restaurante»** (nombre de producto, regla de H1 spoke del proyecto: marca, no keyword-stuffing) | «Manual del Manager de Restaurante: Operaciones, Personas y Números Bajo Control» |
| **Subtítulo del hero** | «Para gerentes, encargados y jefes de sala que ya operan: operaciones, personas, finanzas, servicio y liderazgo — con la normativa española verificada» | Mete «gerente/encargado/jefe de sala» donde suma (texto) **sin arrastrar el ruido de empleo a la URL ni al title** |
| **Description** (~155) | **«Para quien ya gestiona un restaurante: cuadro de mando semanal, cuadrante y registro de jornada, KPIs, quejas y cumplimiento legal 2026. 20 capítulos y 8 Excel.»** (159 → recortar a «…quejas y cumplimiento 2026. 20 capítulos y 8 Excel.») | «El manual operativo que ningún curso te da: turnos, KPIs, quejas, reseñas y equipo en un solo documento. Pago único, acceso vitalicio.» (146) |
| **Keywords** | manual del manager de restaurante · gerente de restaurante · encargado de restaurante · manual de operaciones de un restaurante · gestión de restaurantes · administrador de restaurante · jefe de sala · KPI restaurante · cuadrante de turnos · registro de jornada hostelería | — |

**Por qué no «gerente» en el slug ni en el title:** «gerente de restaurante» es **89 % ofertas de empleo** en la SERP española. Se usa en el H2, en el subtítulo, en la FAQ y en el cuerpo —donde sirve al lector y a la semántica— **pero no en la URL ni en el title**, donde sólo traería competencia contra InfoJobs. Es la misma decisión que se tomó con «escandallo» en la Guía Food Cost, y por el mismo tipo de razón.

### 10.2 FAQ — 12 preguntas, las 9 primeras literales del People Also Ask

| # | Pregunta | Origen |
|---|---|---|
| 1 | ¿Qué hace el encargado de un restaurante? | PAA literal («encargado de restaurante») |
| 2 | ¿Cuáles son los rangos en un restaurante? | PAA literal — **se responde con el organigrama del ALEH VI, que nadie usa** |
| 3 | ¿Cómo se llama el encargado del restaurante? | PAA literal |
| 4 | ¿Qué es lo que hace un administrador en un restaurante? | PAA literal (SERP de México) — **sirve a MX, CO, CL y PE con una sola landing** |
| 5 | ¿Qué debe contener un manual de operaciones? | PAA literal («manual de operaciones de un restaurante») |
| 6 | ¿Cómo hacer un manual de procedimientos para un restaurante? | PAA literal |
| 7 | ¿Cómo hacer un cuadrante de trabajo por turnos? | PAA literal |
| 8 | ¿Cuándo me tienen que entregar el cuadrante de trabajo? | PAA literal — se responde con el **preaviso de 5 días del art. 34.2 ET** y la diferencia entre cuadrante, registro y calendario laboral |
| 9 | ¿Qué establecimientos están obligados a tener hoja de reclamaciones? | PAA literal — se responde advirtiendo de que **es competencia autonómica** |
| 10 | ¿Sirve si mi restaurante está fuera de España? | Objeción de compra: **el marco legal explicado es el español**; las casillas de las herramientas son editables y el vocabulario es neutro. **No se promete cobertura normativa LATAM** |
| 11 | ¿Necesito el Kit de Gestión de Personal o el Kit de Tareas si compro este manual? | Objeción medida (L4 nº 1): se responde con la jerarquía —**los kits son las plantillas de ejecución; el manual es el criterio y la decisión**— no con marketing |
| 12 | ¿Los Excel funcionan en Google Sheets y en Numbers? ¿Y qué pasa cuando cambie la normativa? | Compatibilidad (sin `INDIRECT`/`COUNTA`/`PMT`/`OFFSET`, a diferencia del competidor de plantillas) + **actualizaciones incluidas y celdas editables** (§2.5) |

**JSON-LD:** `Product` (con `offers` a 65 EUR, `priceValidUntil`, `availability`, `seller`) **sin `aggregateRating` ni `review`** + `FAQPage` con las 12 + `BreadcrumbList`. Sin `priceOld` ni badge de descuento.

### 10.3 Interenlazado (regla capital: cero páginas huérfanas)

**Entrantes:**

| Origen | Acción |
|---|---|
| `gerente-de-restaurante-20-areas-clave-donde-la-ia-te-puede-ayudar` · `libreria-de-prompts-para-gerente-de-restaurante-pro-ai` | **Banner fijado** (sustitución quirúrgica del menos afín, patrón D11) + enlace contextual |
| `gestion-personal-hosteleria-ia-reducir-rotacion` · `rentabilidad-restaurante-kpis-metricas-2026` · `ia-en-la-gestion-de-criticas-y-reputacion-de-restaurantes` | **Banner fijado** + enlace contextual |
| `30-hacks-…` · `inteligencia-artificial-rentabilidad-…` · `timlup-checklist-digital-tareas-recurrentes` · `libreria-de-prompts-para-comida-de-personal` | Enlace contextual |
| **5 páginas `/usos/rol/`**: `gerente-restaurante`, `propietario-restaurante`, `director-operaciones-grupo`, `fb-manager-hotel`, `maitre-jefe-sala` | Enlace **bidireccional** |
| Hub `/productos-digitales` (Astro **y** SPA) | Tarjeta real con badge «Nuevo» + **quitar la entrada de `comingSoon`** de los dos ficheros |
| `footerLinks` cruzados | Desde `kit-gestion-personal.ts`, `kit-tareas.ts`, `pack-appcc.ts` y `guia-food-cost-ingenieria-menu.ts` |
| Rotación general | Entrada 46 en `products-catalog.ts` → `fase8e-banners-corpus.py` lo reparte por los 325 posts |
| Lista de compradores | Campaña Resend a los segmentos de kit-gestion-personal, kit-tareas, pack-appcc y guía food cost |

**Salientes de la landing:** Kit de Gestión de Personal (14 €), Kit de Tareas (14 €), Pack APPCC (14 €), Kit Plan Financiero (39 €), Guía Food Cost (55 €), la plataforma (agente «Gerente de Restaurante Pro AI») y el blog. Con `utm_source=landing&utm_medium=cross-sell` para poder medir quién compra dos.

### 10.4 Aparte: cuatro piezas de captación de blog con volumen y sin dueño

**No son este producto y no bloquean el lanzamiento**, pero salen gratis de este research y tienen volumen real, competencia baja y cero producto de pago en la SERP:

| Keyword | Vol/mes ES | Ángulo | Riesgo |
|---|---|---|---|
| **verifactu** | **74.000** (MEDIUM) | «Verifactu en hostelería: por qué NO entra en 2026 y qué hay que hacer antes de enero de 2027» | Alta exigencia de actualización |
| **convenio hostelería** | **1.600** (LOW) | «Cómo saber qué convenio de hostelería te aplica (y por qué el mismo cocinero cobra un 40 % más en Barcelona que en Madrid)» | **No prometer cobertura de los 17 convenios provinciales**: enseñar a usar REGCON |
| **hojas de reclamaciones** | **1.300** (LOW) | «Hojas de reclamaciones en un restaurante: cartel, plazos y qué cambia según tu comunidad» | Competencia autonómica |
| **ley de desperdicio alimentario** | **390** (LOW) | «Ley 1/2025 en restaurantes: qué obliga de verdad (y por qué el doggy bag es de 2022)» | Bajo |

Estas cuatro **sí se miden por tráfico** y se escriben con `bridge.py` (regla capital: los productos no, el blog sí). Van a la cola de contenidos, no a esta sesión.

---

## 11. LISTA NEGRA — lo que NO puede aparecer en el producto

Va literalmente al `guion_manual_manager_restaurante.py` como `cifras_ignorar` + `prohibido`, y el gate de coherencia de cifras de `documentos.py` la hace cumplir.

### 11.1 Cifras sin fuente primaria

| Cifra | Por qué no entra |
|---|---|
| **«El 60 % de los restaurantes cierra en los primeros años»** | **No existe fuente oficial de mortalidad de restaurantes en España.** Sustituir por el **41,9 % de supervivencia a 5 años** del INE (todos los sectores) y los **31,1 cierres diarios** de Delectatech, dejando claro que **son cosas distintas** y que un recuento absoluto no es una tasa de fracaso |
| **Rotación en hostelería del 63,8 %** | El informe original de Linkers no está publicado ni enlazado por nadie. Y en **este mismo research aparece con dos padres distintos**: Synergie (L4-A3) y Randstad (L4-H1). **No se cita** |
| **Coste de reemplazar a un empleado: 2.800-5.000 €** | Misma procedencia y mismo problema. **En su lugar, la herramienta 2 lo calcula con los datos del lector** |
| **«Hostelería concentra el 19,64 % de las infracciones de la ITSS»** | La memoria de la ITSS de 2023 no se pudo abrir para confirmarla |
| **«15.045 puestos irregulares en 2024» y «450.000 trabajadores afectados por horas extra no pagadas»** | Misma fuente secundaria, no verificada en la memoria original |
| **«80 % de los profesionales de hostelería con problemas de salud mental» (The Burnt Chef Project)** | Al leer el artículo completo señalado como fuente, **el dato no está en el texto** |
| **Onboarding: «+82 % de retención y +70 % de productividad»** | Cifra tipo Gallup/BambooHR repetida sin atribución consistente; sin fuente primaria localizable |
| **«58 % de los comensales consulta apps de reservas antes de elegir»** | La página que la citaba devuelve 404 |
| **Absentismo específico de hostelería** | Randstad sólo desglosa hasta «sector servicios» (7,1 %). **No atribuir esa cifra a la hostelería** |
| **Ticket medio de alta cocina · márgenes por segmento · cubiertos por camarero** | Ningún organismo los publica en España. Si el manual los necesita, van como **plantilla de cálculo**, nunca como benchmark citado |
| **Tarifas de AGEDI-AIE en €/mes** (los ≈8,82 € que circulan) | Su enlace oficial de tarifas da 404. Y **las tarifas de SGAE que publican algunos blogs del sector contradicen el documento oficial y son erróneas** |
| **Prime cost 60-65 % presentado como dato español** | Es convención de EE. UU. (Toast / restaurantowner). El umbral español se **deriva** de CaixaBank × elBulli y se marca como derivado |
| **Cualquier «salario del gerente» como cifra única** | El rango real según fuente va de 18.000 a 95.200 €/año, y ninguna explica la varianza |

### 11.2 Afirmaciones normativas falsas o caducas

- «La jornada es de 37,5 horas» — **rechazada** el 10-09-2025.
- «El fichaje digital ya es obligatorio» / «desde enero de 2026 es sancionable operar sin sistema homologado» / cualquier multa citada por ese concepto — **el RD no existe en el BOE**.
- «Verifactu entra en vigor en 2025» o «en 2026» — **1-01-2027 y 1-07-2027**.
- «Habrá que emitir factura electrónica de cada mesa» — **el art. 4 del RD 238/2026 excluye las facturas simplificadas**.
- «Las temperaturas las fija el RD 3484/2000» — **derogado** el 22-12-2022.
- «El anisakis se regula por el RD 1420/2006» — **derogado** el 22-12-2022.
- «Los perros guía se rigen por el RD 3250/1983» — **derogado** el 17-06-2025.
- «Se aplica el ALEH V» — el vigente es el **VI**, modificado el 04-09-2026.
- «Existe el RD 830/2022 de biocidas» — **no existe**.
- «Las cuantías del art. 40 LISOS las actualizó el RDL 5/2023» — **fue la Ley 10/2021**.
- «La consulta V3095-17 regula las propinas en hostelería» — **es de casinos**; la de hostelería es la **V2236-13**.
- «El doggy bag es obligatorio desde la Ley 1/2025» — **desde el 15-12-2022** (RD 1021/2022, art. 18.5).
- «Todo restaurante necesita plan de prevención del desperdicio» — **exentos los de hasta 1.300 m² y las microempresas**.
- «Hay que inscribirse en el RGSEAA» — **registro autonómico**, salvo que se supere el 25 % del volumen anual o 500 kg/semana de suministro a terceros.
- «Se puede fumar en terrazas con menos de tres paredes» — **máximo DOS**; y hay un proyecto de ley en tramitación.
- «Los reconocimientos médicos son obligatorios» — **voluntarios** (art. 22.1 Ley 31/1995).
- «El permiso parental de 8 semanas es retribuido» — **es una suspensión** del contrato.
- «5 días por fallecimiento» — **2 días, ampliables en 2 más** por desplazamiento.
- «Los 15 minutos del bocadillo son tiempo de trabajo» — **sólo si lo establece el convenio o el contrato**.
- «Abrir un restaurante va por declaración responsable desde la Ley 12/2012» — **la hostelería no está en su anexo**.
- «Existe el carné oficial de manipulador de alimentos» — **derogado en 2010**.
- «El cartel de "consulte al personal" basta para los alérgenos» — **hace falta soporte escrito o electrónico accesible**.
- «Se puede ser cashless» — **negarse a aceptar efectivo es infracción de consumo** desde el 28-05-2022.
- «La Ley 18/2022 Crea y Crece regula la aceptación de efectivo» — **no la menciona**.
- Presentar como obligación legal con periodicidad la **limpieza de campana y conductos**, la **calibración de termómetros**, la **frecuencia de formación** o la **medición del aceite de fritura**: **ninguna tiene periodicidad fijada por norma estatal**.

### 11.3 Errores de método

- **Mezclar INE con Hostelería de España** en la misma tabla (117.440 M€ vs 166.211 M€; 266.476 **empresas** vs «más de 300.000» **locales**).
- **Fechar CaixaBankLab × elBullifoundation**: la página no lleva fecha visible. Se cita «metodología Sapiens, sin fecha».
- **Presentar el estudio de tiempos de espera como benchmark español**: su trabajo de campo es un restaurante de India.
- **Presentar el ticket medio de 21 € como gasto por cubierto**: es por ticket.
- **Dar una cifra única de coste de personal o de nómina para LATAM**: el recargo va de ~45 % (Perú) a ~152 % del salario base (Colombia).

---

## 12. Riesgos, decisiones abiertas y presupuesto

### 12.1 Riesgos

| # | Riesgo | Evidencia | Mitigación |
|---|---|---|---|
| 1 | **La mayor ventaja del producto es también su mayor riesgo: la normativa caduca** | 7 normas en movimiento con fecha conocida (§2.5) | Parámetros en celda, hoja `Estado Normativo` con fecha de corte, capítulo que enseña a verificar en el BOE, changelog y actualizaciones incluidas |
| 2 | **Un error en el bloque legal cuesta más que un error de food cost** | Un manager que aplique una regla mal puede acabar en una improcedencia o en una sanción de 5 cifras (§5.8) | **Verificador legal independiente obligatorio** (agente sonnet, patrón del verificador fiscal de la Guía Food Cost) **antes** de escribir los capítulos 8-15 y 19, contra las fuentes primarias, no contra L3 |
| 3 | **Ámbito autonómico y provincial imposible de cubrir** | 17 convenios de hostelería y 17 normativas de consumo, hojas, horarios y ruido | El manual da el **marco estatal + cómo buscar el tuyo** (REGCON, boletín autonómico, ordenanza municipal), y usa Madrid, Cataluña, Andalucía y C. Valenciana **como ejemplos declarados**, nunca como regla nacional |
| 4 | **Canibalización con cuatro kits propios** | kit-gestion-personal (14 €), kit-tareas (14 €), pack-appcc (14 €), kit-plan-financiero (39 €) | Jerarquía explícita en el cap. 01 y en la landing: **los kits ejecutan, el manual decide**. La frase para la landing: *«Los kits te dicen qué hacer cada día. El manual te dice por qué, con qué criterio y qué pasa si no lo haces»* |
| 5 | **Vender profundidad LATAM que no tenemos** | El research legal es **exclusivamente español** | Casillas editables + vocabulario neutro + **la landing lo dice explícitamente**. No se promete fiscalidad ni laboral de otros países |
| 6 | **La reseña de 2★ ya está escrita si repetimos lo básico** | «Temas tratados demasiado básicos. Parece más bien un conjunto de entradas de blog» | El cap. 01 declara el nivel; lo gratuito se cita y se salta; el bonus son casos, no teoría |
| 7 | **Presupuesto: este manual es más caro que la Guía Food Cost** | La redacción de la guía de 95 páginas con subagentes Anthropic costó **≈5,5 M tokens** (dato del calendario, 04-09-2026), y aquí cada capítulo legal necesita verificación | §12.3: partir la semana B en dos sesiones |
| 8 | **8 libros sin verificar en pycel** | Son diseño, no ficheros (L5 §5.3) | La verificación de fórmulas es un gate obligatorio de la construcción, no un «ya se verá» |
| 9 | **El hub anuncia el producto desde mayo con `phase: 'Julio 2026'`** | Verificado en los **dos** ficheros (`ProductosDigitales.tsx:911` y `ProductosDigitalesHubPage.astro:921`) | Quitar la entrada de `comingSoon` **en los dos** al publicar, o quedarán la tarjeta real y la de «próximamente» a la vez |
| 10 | **`documentos.py` y `GuiaLandingPage.astro` los comparten las 8 guías** | Los tres fixes de parametrización ya están aplicados sin commitear | **Regenerar al menos un producto ya vendido (food cost) para confirmar que no rompe nada** antes de dar por buenos los cambios |
| 11 | **Regenerar pisa ediciones manuales** | Gotcha conocido de los ensambladores | Diff de enlaces antes de regenerar cualquier cosa publicada |
| 12 | **`robots.txt` y sitemap** | El comodín borró 26 posts en agosto | El prefijo `manual-` ya está cubierto, pero **correr `robots-gate.py`** igual |

### 12.2 Decisiones abiertas para el orquestador / John

1. **Precio final: 65 €** (recomendado). Alternativas: 55 € (paridad con la Guía Food Cost, pero deja el producto más ancho al precio del más estrecho) o 45 €. **49 € vetado.**
2. **Bonus: «12 situaciones resueltas del manager»** (recomendado, ~7.500 palabras → ~30 páginas), con los guiones de conversación incrustados dentro de los casos que los piden. Alternativas descartadas y por qué, en §8.1.
3. **¿8 libros o 7?** Recomiendo **8**, partiendo la propuesta 6 de L5 en `calendario-cumplimiento-legal.xlsx` y `reuniones-briefings-actas.xlsx`: son dos usuarios, dos cadencias, y fusionarlos diluye la pieza que carga toda la ventaja normativa.
4. **¿La rotación del 63,8 % se cita con atribución explícita o va a la lista negra?** Recomiendo **lista negra**: aparece con dos padres distintos en el mismo research y el informe original no está publicado.
5. **¿«Manager» o «Gerente» en el nombre?** Recomiendo **«Manager»** (aparece literalmente en 4 de las 9 ofertas españolas revisadas y se entiende en los 6 mercados LATAM), con «(gerente / encargado)» en la primera mención. Es además el nombre con el que el producto lleva anunciado desde mayo.
6. **Los tres fixes de parametrización del pipeline** (`tipo_doc`/`categoria_doc` en `documentos.py`, `why.titlePre`/`why.titleGold` en `types.ts` y el H2 de `GuiaLandingPage.astro`) **ya están aplicados sin commitear**: ¿se confirman con `tipo_doc='manual'` y `categoria_doc='Manual profesional'`, y se regenera la Guía Food Cost como control de no-regresión?
7. **¿Se crea `astro-site/src/data/productos/manuales/` o se reutiliza `guias/` + `GuiaData`?** L5 recomienda reutilizar (cero tipos nuevos, cero plantilla nueva). **Matiz mío:** hay **dos manuales más en la cola** (Chef Ejecutivo es el nº 3 de productos nuevos), así que la carpeta podría justificarse — pero sólo si aparecen divergencias estructurales reales, no por simetría.
8. **¿Se aprovecha para publicar las 4 piezas de captación del blog** (Verifactu 74.000, convenio 1.600, hojas de reclamaciones 1.300, desperdicio 390)? Son de `bridge.py` y de otra sesión, pero el research ya está hecho y sin dueño en el grupo.
9. **¿Banner fijado en 5 posts (inserción quirúrgica, patrón D11) o se deja a la rotación general?** Recomiendo fijado en los 5 afines + rotación para el resto.
10. **Promesa de páginas:** gate interno en **60** y la landing publica la cifra medida (la Guía Food Cost midió 95 con el mismo dimensionado). ¿Se mantiene o se sube el objetivo de palabras?
11. **Inglés:** sigue vetado hasta cerrar el ES (decisión del 31-ago). Aquí hay un matiz: existe `prompt-library-restaurant-manager.md` en el blog EN y el agente tiene versión inglesa, así que el día que se levante el veto **este producto es candidato natural al primero**.
12. **Certificación tipo test** (lo hacen Aprendum y estudioformacion con ≥60 %): valor percibido alto y coste bajo. **No es el foco**, pero es una idea para v1.1 si John quiere.

### 12.3 Presupuesto estimado por fase

| Fase | Trabajo | Estimación |
|---|---|---|
| **A — research + SPEC** (esta sesión) | 5 lentes + esta síntesis + SPEC con decisiones firmadas | **Cerrada.** ~1,5-1,8 M tokens de subagentes |
| **B1 — herramientas** | 3 constructores opus (2-3 libros cada uno) + 1 verificador **legal** sonnet (bloque normativo contra fuentes primarias) + 1 agente para el guion (opus) + `inject_cache` y verificación `data_only` | **1,5-2 M** |
| **B2 — documentos** | Redacción por bloques con **subagentes Anthropic** (`dump_prompts.py` → agente por bloque → `check_bloque.py`), 20 capítulos + 12 casos + 1 refutador opus (dos lentes en un prompt) + fixer sonnet + gates (páginas con PyMuPDF, no latinos, coherencia de cifras, paridad PDF↔DOCX, metadata) | **5-6 M** (referencia medida: 5,5 M la guía de 95 páginas) |
| **C — capa de producto y lanzamiento** | Landing sobre `GuiaData`, dashboard, 4 functions + config, Payment Link (John), catálogo 46, hub ×2 con el `comingSoon` retirado, changelog, imágenes, banners, `robots-gate.py`, `fase5-generate-zona-app.py --check`, gate offline y gate LIVE | **0,8-1 M** |

⚠️ **Aviso de presupuesto explícito:** el techo de John es **~15 % de la cuota semanal** y una semana «normal» debe quedarse **por debajo de 1,5 M**. La fase B de este producto **no cabe en una semana**. Recomendación: **B1 y B2 en dos sesiones pares distintas**, o asumir que este manual ocupa dos ciclos de producto nuevo. Decidirlo **antes** de arrancar, no a mitad.

---

## 13. Lo que este research NO pudo verificar (consolidado de las cinco lentes)

**L1 — competencia**
- **Precio exacto de 9 de los 36 productos**: 2 manuales de Hotmart, Euroinnova (curso corto), CESAE, Gastrouni (sólo el depósito de 550 €), ESAH, UCM, Combo, Mapal OS y Nory.
- **Amazon.es bloqueó TODO acceso directo hoy** (WebFetch 500 y curl con captcha). Los 11 libros se verificaron vía Amazon.com.mx (en pesos, conversión aproximada marcada) o vía librerías españolas.
- **Le Cordon Bleu Madrid y Crehana**: no se localizó un curso propio de gestión de restaurantes con precio verificable. Se documenta la ausencia, no se afirma que no exista.
- **Gastroeconomy, ThinkFoodGroup y cámaras de comercio**: sin producto de pago propio localizado.
- **Skello y Cover Manager**: sus páginas oficiales de precios devuelven 404; los datos vienen de agregadores con cifras **contradictorias entre sí** (se marca la discrepancia en vez de elegir una).
- Sólo 6 de 36 productos exponían rating con volumen. Reddit, Quora y Udemy no se intentaron (bloqueo conocido).

**L2 — SERP**
- **No se corrió SERP en Chile, Perú, Colombia ni Argentina**: todo el análisis de SERP es de España más una comprobación en México.
- **No se verificó canibalización en GSC (`page` × `query`)** contra el slug definitivo ni sus variantes. **Sigue pendiente y es un chequeo de 5 minutos antes de la fase C.**
- No se probaron sistemáticamente las variantes con y sin tilde.
- ✅ **Cerrado por mí:** el hueco de `use-cases.ts` (hay 5 páginas de rol relevantes, no una).

**L3 — datos y normativa**
- 7 cifras **sin fuente primaria** (§11.1) y 7 **verificadas a medias**: la estructura de costes de CaixaBankLab (sin fecha), el Anuario de Hostelería de España (de pago, 1.800 €/año, leído por prensa), el informe Ivie/Cajamar (nota original con error TLS), el Cornell Hospitality Report (PDF caído), la guía de trazabilidad de AESAN (404, leída en la edición de Aragón), el estudio de esperas (campo en India) y el **estado de la tramitación del registro horario digital** (secundarias coincidentes; lo que sí es primario es que **no hay ningún RD publicado**).
- **11 huecos del bloque de consumidor y local**: tarifas vigentes de AGEDI-AIE (404), texto articulado de dos decretos catalanes (portal en JavaScript), Decreto 1/2010 de Madrid (leído en espejo, BOCM de 2010 en 404), plazo de respuesta al consumidor en Madrid y C. Valenciana, visado del cartel de admisión en Madrid, horarios de cierre de Cataluña, Decreto 32/2003 de Asturias, la inexistencia de una norma con rango legal que use la palabra «terraza» para el suplemento de precio, tres sentencias del bloque de música identificadas pero no leídas íntegras, la tipificación del art. 8 de la Ley 1/2025 y la cuantía aplicable a denegar el acceso a un perro de asistencia.
- **10 temas fuera de alcance**: normativa autonómica de higiene, cuantías del RD 1945/1983 y de la Ley 33/2011, cuantías del TRLGDCU para alérgenos, periodicidad de medición del aceite, documentación tasada de la empresa de DDD, frecuencia de registro de temperaturas, licencia municipal de actividad, **los 15 convenios provinciales distintos de Madrid y Cataluña**, periodicidad de limpieza de campana y calibración de termómetros.

**L4 — voz del cliente**
- **Tres estadísticas descartadas** por no verificarse en su página fuente: Burnt Chef (80 %), onboarding (+82 %/+70 %) y apps de reservas (58 %).
- **Sin ninguna cita textual atribuida a una persona identificable en Argentina, Perú, Chile, Guatemala, Panamá ni Uruguay** — el mismo hueco geográfico que ya se documentó ayer para México.
- **Sin cita textual verificada** del dolor «mi jefe no me deja» (el fetch falló por certificado SSL); se usa evidencia indirecta y se dice.
- **Sin informes localizables de Deloitte, KPMG, Mapal (más allá de su blog) ni Nory**.
- Reddit, Quora, Udemy y comentarios de YouTube: bloqueados.

**L5 — assets**
- **Ninguna fórmula de las herramientas nuevas se verificó con pycel**: son diseño, no ficheros.
- No se auditó el precio ni una entrada real de `products-catalog.ts`.
- `kit-inventario` sólo se nombró, no se abrió.
- ❌ **Corregido por mí:** su §4.3 daba por ausentes las 10 líneas de `manual-` en `robots.txt`. **Ya están.**

**Verificaciones propias de esta síntesis (lo que SÍ comprobé)**
- ✅ `robots.txt` con `manual-*` en los 5 bloques · ✅ los 3 fixes de parametrización aplicados sin commitear · ✅ 52 ids `MM-*` fusionados en `guias-v2-research-sector.json` (155 entradas) · ✅ los 10 posts de blog de L2 §5 existen en disco · ✅ 5 páginas de rol relevantes en `use-cases.ts` · ✅ 45 productos en `products-catalog.ts` (éste sería el 46) · ✅ la entrada `comingSoon` existe en los dos ficheros del hub con `phase: 'Julio 2026'` · ✅ calibración: la Guía Food Cost prometía 60 páginas y **midió 95** con 30.000 palabras y `paginas_prometidas: 60` en su guion.
- ❌ **No comprobé GSC en vivo** (`page` × `query`) para el slug ni sus variantes.
- ❌ **No verifiqué el BOE-A-2026-18630 con mis propias manos**: me apoyo en L3, que sí leyó la resolución. **Antes de escribir el capítulo 14, el verificador legal debe abrirla.**
- ❌ **No repetí los fetches de precios de L1**: las cifras de SaaS, cursos y libros se toman de esa lente.

---

**Via: Claude Code**
