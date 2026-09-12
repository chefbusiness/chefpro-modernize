# LENTE 4 — Sector, modelo de negocio, equipamiento, proveedores y casos de éxito
## Research para el producto «Cómo Montar una Chocolatería» (AI Chef Pro)

| | |
|---|---|
| **Producto** | «Cómo Montar una Chocolatería» — guía premium «Cómo Montar», sería el **producto 49** del catálogo (hermana de `guia-pasteleria-obrador` y `guia-panaderia-obrador`, 65 €) |
| **Lente** | L4 — Sector, modelo de negocio, equipamiento, proveedores, casos de éxito, salarios |
| **Prefijo de ids** | `CHS-` (CHS = **CH**ocolatería **S**ector) |
| **Fecha del research** | **2026-09-12**. Todas las consultas web se hicieron ese día; ésa es la fecha de consulta de cada URL salvo que se indique otra |
| **Autor** | Subagente de research (Claude Opus 5), repo `chefpro-modernize` |
| **Naturaleza** | **Research y propuesta.** No contiene contenido de producto: ni capítulos, ni prosa vendible, ni copy de landing |

---

## 0. Método y limitaciones declaradas

### 0.1 Método

1. **Fuente primaria primero.** Se intentó siempre el dato oficial (INE/DIRCE por descarga directa de CSV, MAPA, Produlce, BOE/EUR-Lex, ICCO) antes de recurrir a prensa sectorial, consultoras o portales de franquicia.
2. **Descarga directa del DIRCE.** Se descargaron los CSV públicos del INE (`https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/<id>.csv`, tablas 298, 299 y 4721) y se filtraron por CNAE con `grep`/`awk`, en vez de fiarse de resúmenes de terceros. Resultado: **el DIRCE público no aísla el chocolate** (§2.1).
3. **Precios de equipamiento solo con precio VISIBLE** en la ficha o el listado de un distribuidor, con URL, **y con la base de IVA declarada tal como la declara la web**. Donde la web no dice si el precio lleva IVA, se anota **«base NO declarada»** — no se supone. Ésta es la corrección directa del defecto que la refutación tumbó en la lente L4 de Pastelería (mezclar bases).
4. **Evidencia de mercado por traspasos reales.** Se leyeron listados vivos de Milanuncios porque son la mejor prueba disponible de m², rentas y precios pedidos.
5. **Aritmética explícita.** Cualquier suma o división de este informe se muestra con sus sumandos, para que sea refutable.
6. **Fiabilidad declarada por cifra**: **ALTA** (fuente primaria leída en su página) · **MEDIA** (secundaria leída en su página) · **BAJA** (solo leída en un resumen de buscador, no en la página).

### 0.2 Lo que NO se pudo verificar, y por qué

| # | Limitación | Motivo |
|---|---|---|
| **L-1** | **No existe dato DIRCE del chocolate.** La tabla `t=298` (la única pública con desglose por **grupos** CNAE) llega al grupo **108** «Fabricación de otros productos alimenticios», que mezcla cacao/chocolate con café, té, especias, platos preparados y alimentación infantil. La clase **1082** es de 4 dígitos y el DIRCE público no la publica. Además la tabla **se detiene en 2020** | Limitación de la propia estadística pública |
| **L-2** | **La tabla `t=4721` (DIRCE vivo, hasta 2025) trae una columna «Grupos CNAE» pero vacía en las filas nacionales.** Solo se pudo extraer el total nacional | Estructura del fichero; se abandonó el fichero de 112 MB por la restricción térmica (§0.4) |
| **L-3** | **No se leyó la serie oficial de precios del cacao de la ICCO.** Su página `icco.org/statistics/` muestra como «último» un ICCO daily price de **07/10/2024** (6.094,13 US$/t) y remite a una **suscripción anual de pago** para la serie | Muro de pago; la página pública está desactualizada. Se trabaja con prensa que **cita expresamente a la ICCO** |
| **L-4** | **No se leyeron los valores numéricos del RD 1055/2003** (porcentajes mínimos, grasas vegetales ≤5 %, definición legal de «chocolate a la taza») ni **los límites de cadmio del Rgto. (UE) 2023/915** | Se verificó la **existencia, ámbito y vigencia** de ambas normas, pero los valores exactos son competencia de la **lente normativa (L3)**, que debe leerlos en el BOE/EUR-Lex. Aquí van marcados **«sin fuente (valores)»** |
| **L-5** | **InfoJobs devuelve HTTP 456** (anti-bot) y Glassdoor no se pudo leer | No hay ofertas reales de chocolatero con salario transcrito. Los salarios de §7 salen de un **agregador**, no de ofertas, y bajan a fiabilidad MEDIA-BAJA |
| **L-6** | **Selfpackaging devuelve HTTP 403** | Sin precios de packaging de bombones. Queda **«sin fuente (precio)»** |
| **L-7** | **No hay precio publicado de equipamiento bean-to-bar** (tostador, descascarilladora, melanger, refinadora, concha, prensa). CocoaTown y Premier/DCM publican catálogo pero no precio accesible | Venta a presupuesto / tienda fuera de la UE. **«sin fuente (precio)»** |
| **L-8** | **No hay precio publicado de la cámara climatizada del obrador de chocolate** (16-18 °C, HR 50-60 %) ni del deshumidificador profesional dimensionado | Solución a medida por instalador. **«sin fuente (precio)»** |
| **L-9** | **Los precios de traspaso son precio PEDIDO, no precio pagado**, y ninguno de los anuncios leídos es una chocolatería artesana pura: son churrería-chocolatería o pastelería-bombonería | Naturaleza del portal. Se advierte en la tabla |
| **L-10** | **No se pudo verificar la facturación de Cacao Sampaka, Casa Cacao, Bombonería Pons ni Chocolatería San Ginés** | eInforma/Axesor/Iberinform devuelven ficha de pago o 404; ninguna publica cuentas accesibles |
| **L-11** | **No se leyó el informe Produlce 2025 completo ni el informe Alimarket 2025**, solo la prensa que los cita y el resumen público | Informes de pago / acceso restringido |

### 0.3 Regla que se aplicó a rajatabla

> **Ninguna cifra de este informe procede de la memoria del modelo.** Toda cifra lleva URL. Donde no la hay, la fila dice **«sin fuente»** y va a la **lista negra del §9.2**, no a la guía.

### 0.4 Nota térmica

Se respetó la restricción del Mac. La descarga y el `grep` de los dos CSV de 112 MB llevaron la CPU a **67,0 °C**; se interrumpió el trabajo local, se borraron los ficheros grandes y **el resto del research se hizo solo por red** (sin carga local), volviendo a **53,5 °C**. Por eso la limitación **L-2** no se reintentó: no compensaba el riesgo por un dato que la tabla probablemente no contiene.

---

## 1. Tipos y sub-conceptos del negocio (CHS-01 … CHS-12)

La decisión más cara que toma el lector es **qué chocolatería monta**, y en este sector la palabra significa **dos negocios distintos** que no comparten ni licencia ni maquinaria ni ticket. Ésta es la matriz que propongo como capítulo 1 y como primera hoja del xlsx.

### 1.1 Matriz comparada

| id | Sub-concepto | Inversión de referencia | m² | Personal | Qué cambia estructuralmente |
|---|---|---|---|---|---|
| **CHS-01** | **Obrador en casa / venta directa** | «sin fuente» (no hay cifra publicada para chocolate) | Zona separada del uso doméstico | 1 | Sin horno ni freidora: es el sub-concepto **más barato de toda la familia «Cómo Montar»**, porque el chocolate no genera humos. Venta directa, ferias, mercados |
| **CHS-02** | **Obrador de bombonería sin venta al público (B2B)** | Núcleo de máquina verificado: **≈ 24.105 €** (§4.6, base mixta) · versión mínima **≈ 5.740 €** | «sin fuente» | 1-2 | Cliente = hostelería, regalo corporativo, tiendas. Sin escaparate ni licencia comercial. Venta a crédito y estacionalidad de pedidos, no de paso |
| **CHS-03** | **Bombonería / chocolatería artesana con obrador + tienda** ⭐ | **20.000-30.000 €**, «hasta 80.000 € según el proyecto» | **60-100 m²** | **1-2** | **Es el molde principal propuesto.** Aparece la vitrina refrigerada de chocolate (+14/+17 °C), el TPV y el packaging de regalo |
| **CHS-04** | **Tienda de chocolate SIN obrador** | «sin fuente» | «sin fuente» | 1-2 | Compra producto acabado a fabricantes. No necesita RGSEAA de fabricación (a confirmar por L3), pero **pierde el margen de transformación** y queda a merced del precio de la cobertura |
| **CHS-05** | **Bean-to-bar** (del grano a la tableta) | «sin fuente (precio)» — no hay precio público del tren de máquinas (L-7) | «sin fuente» | «sin fuente» | Es el único sub-concepto que **importa grano** → entra de lleno en el **EUDR** (§2.6) y en el control de **cadmio**. Hay **asociación sectorial propia** con ~41-45 miembros (§6.4) |
| **CHS-06** | **Chocolatería-cafetería** (obrador + consumo en local) | «sin fuente» | «sin fuente» | 3-5 (por analogía con Pastelería, «sin fuente» para chocolate) | Añade barra, aseos de público y sube el ticket; **cambia la licencia** (pasa a actividad de hostelería) |
| **CHS-07** | **Chocolatería de taza y churros** ⚠️ | «sin fuente» (inversión). Traspasos reales: **58.000-95.000 €** (§3.6) | **74-118 m²** (traspasos reales) | «sin fuente» | **Es otro negocio.** Freidora + **extracción de humos** + chocolatera. Es hostelería, no obrador de chocolate. Margen bruto del churro **85-90 %** (§3.4). Ver la decisión del §1.3 |
| **CHS-08** | **Chocolatería-pastelería** | Traspasos reales de pastelería-bombonería: **26.000-210.000 €** (§3.6) | **90-400 m²** | «sin fuente» | Horno → vuelve la salida de humos y la licencia cara que CHS-03 se ahorra |
| **CHS-09** | **Chocolatería-heladería** | «sin fuente» | «sin fuente» | «sin fuente» | **Contraestacional perfecta**: el valle de verano del chocolate (§3.5) es el pico del helado. Es la respuesta natural a la peor debilidad del modelo |
| **CHS-10** | **Venta online con envío** | «sin fuente» | — | — | El chocolate **no viaja en verano** sin embalaje isotérmico. Caso Bombonería Pons: crece «por venta online, más tiendas físicas, venta al por mayor e incluso exportación» |
| **CHS-11** | **Talleres y catas como línea de ingresos** | «sin fuente» (inversión) | — | 1 | **25-45 €/persona**, mínimo típico 6 pax (§3.3). Ingreso de margen altísimo que **no consume cobertura** y **rellena el valle de verano** |
| **CHS-12** | **Franquicia** | **Valor desde 125.000 €** (canon 24.040 €, royalty 5 %) · **Chök desde 100.000 €** (canon 30.000 €, contrato 5 años, local mín. 55 m²) · **Cacao Sampaka: 100-250 m², población ≥500.000 hab** | Ver columna anterior | — | Canon + royalty + compra obligada a central. Es **4-5 veces** la inversión de CHS-03 |

**Fuentes de la matriz:**
- CHS-03 (20.000-30.000 € / hasta 80.000 €, 60-100 m², 1-2 empleados): Stefano Ventura, «Cómo hacer el plan de negocio de una chocolatería paso a paso», **plandenegocio.es**, publicado **17-dic-2025** — https://plandenegocio.es/como-hacer-un-plan-de-negocio-para-chocolateria/ · Fiabilidad **MEDIA**. ⚠️ Es el **mismo dominio** cuyo artículo de requisitos comete el error del «carnet de manipulador» (§9.2, nº 15): usar sus cifras con distancia.
- CHS-07 y CHS-08 (traspasos): Milanuncios, §3.6.
- CHS-10 (Pons): https://bomboneriapons.com/en/pages/history-bomboneria-pons · **MEDIA**.
- CHS-11: §3.3.
- CHS-12 (Valor): https://lexpress-franchise.com/es/articulos/chocolateria-valor-franquicia-cifras-fechas/ · **MEDIA**. (Chök): https://www.franquiciashoy.es/franquicias/franquicias-de-panaderias-y-pastelerias/panaderias-pastelerias/chok · **MEDIA-ALTA** (datos declarados por la enseña). (Cacao Sampaka): https://www.mundofranquicia.com/franquicia/alimentacion-y-supermercados/delicatessen/cacao-sampaka/ · **MEDIA**.

### 1.2 El hallazgo estructural: **el chocolate no hace humo, y eso es dinero**

Es la ventaja competitiva del sub-concepto CHS-03 frente a toda la familia «Cómo Montar», y **ninguna fuente de la SERP la enuncia como decisión de negocio**:

> «Si los hornos instalados son eléctricos, equipados con recogida de vapores por condensación, y su potencia total conjunta es inferior a 10 kW, no será necesaria la instalación de salida de humos» — y se evita «el coste de instalar conductos de acero inoxidable por toda la fachada (que **puede superar los 6.000 €**)».
> — Salva Industrial, «¿Montar una panadería y pastelería sin salida de humos? Guía técnica» — https://www.salva.es/es/blog/montar-una-panaderia-y-pasteleria-sin-salida-de-humos (consultado 2026-09-12; **la página no lleva fecha**). Fiabilidad **MEDIA** (fabricante, con interés comercial en la respuesta).

**Un obrador de chocolate puro no tiene horno ni freidora en absoluto.** Es decir: la excepción que la panadería tiene que pelear técnicamente, la chocolatería la tiene **de serie**. Eso abre locales que a una pastelería le están vedados y, según la misma fuente, evita la licencia compleja de cocina caliente. **Lo tiene que confirmar la lente normativa (L3)** antes de escribirlo como afirmación: aquí queda como hipótesis bien fundada, marcada, no como dato.

La contrapartida es la simétrica y **también hay que enseñarla**: lo que la chocolatería se ahorra en extracción **se lo gasta en clima**. El chocolate exige un obrador estable (§4.4) y ése es un coste que la pastelería no tiene.

### 1.3 ⚠️ DECISIÓN PARA JOHN: qué se hace con la «chocolatería de taza y churros»

**El problema.** «Chocolatería» significa dos cosas en España. La descripción ya anunciada en el hub —«Temperado, obrador, vitrina, proveedores de cacao, licencias y modelo de negocio»— apunta inequívocamente a **(a) la bombonería artesana**. Pero el volumen de búsqueda está en la otra: «chocolateria» 9.900/mes, «chocolate a la taza» 4.400/mes, «chocolateria churreria» 1.000/mes, frente a «bomboneria» 880 y «chocolate artesanal» 390.

**Los tres argumentos, con dato:**

1. **El volumen de (b) es de CONSUMIDOR, no de emprendedor.** Las keywords de intención de apertura del lado de los churros son residuales: «montar una churreria» **50/mes**, frente a «como montar una chocolateria» 10 y «montar una chocolateria» 10. Nadie está buscando abrir una churrería en volumen suficiente para sostener un producto de 65 €. Y el PAA de la SERP («¿Cuánto vale 1 kg de cacao?», «¿Cuál es el chocolate que más se vende?») es de consumidor puro.
2. **(b) es un negocio de HOSTELERÍA, no un obrador.** Freidora, extracción de humos, barra, servicio en sala. Comparte con (a) el escandallo y el CAPEX, pero **no comparte la columna vertebral**: el capítulo de temperado, moldes, cámara de chocolate y vida útil de rellenos no le sirve de nada. Si (b) fuera el eje, la guía sería «Cómo Montar una Churrería» — otro producto.
3. **Pero dejarlo FUERA deja un agujero visible.** El lector que teclea «chocolatería» y llega a la landing tiene, en España, una probabilidad alta de estar pensando en San Ginés o en una franquicia Valor. Si el producto no nombra ese modelo **ni para descartarlo**, parece incompleto.

**Propuesta (a decisión de John):** **capítulo de variante, no producto aparte y no fuera.**

- **Un capítulo** de la guía (propuesta: el que cierre el bloque de sub-conceptos) dedicado a CHS-07, con lo que sí está medido: margen bruto del churro **85-90 %**, ración de 4 uds **~2,50 €** que sube a **3,50-4 €** al añadir chocolate, ingredientes+aceite **~20 % de la facturación**, y los traspasos reales de §3.6 como referencia de m² e inversión.
- **Una columna de escenario** en el xlsx de CAPEX y en el de P&L, para que el lector pueda correr los números de (b) con el mismo motor.
- **Un párrafo explícito en la landing y en la FAQ** que diga cuál de las dos chocolaterías cubre la guía a fondo y cuál cubre como variante. Es el antídoto contra la devolución por expectativa.
- **No** un producto aparte: con «montar una churreria» a 50/mes y sin canal propio, no se sostiene.

---

## 2. El sector en España (CHS-13 … CHS-26)

### 2.1 Empresas y establecimientos — el dato oficial NO existe con el detalle que se querría

| id | Dato | Fuente | Fecha | Fiabilidad |
|---|---|---|---|---|
| **CHS-13** | **3.237 empresas** en el grupo CNAE **108** «Fabricación de otros productos alimenticios» a 1-ene-**2020**. Serie leída: 2008=2.827 · 2011=2.668 · 2013=2.647 · 2015=2.640 · 2016=2.639 · 2017=2.823 · 2018=3.180 · 2019=3.178 · **2020=3.237**. De ellas, **690 sin asalariados** en 2020 | INE, DIRCE, tabla **298**, CSV descargado de https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/298.csv (tabla: https://www.ine.es/jaxiT3/Tabla.htm?t=298) | 1-ene-2020 | **ALTA** (dato oficial) pero **INSERVIBLE COMO «CHOCOLATERÍAS»**: el grupo 108 mezcla cacao/chocolate con café, té, especias y platos preparados. Y **está caduca** |
| **CHS-14** | **91.188 empresas** en el grupo CNAE **472** (comercio minorista de alimentación en establecimientos especializados) a 1-ene-**2020**; **39.508 sin asalariados**. Serie: 2008=109.273 · 2013=104.262 · 2016=99.037 · 2019=92.403 · **2020=91.188** — es decir, **el comercio especializado de alimentación perdió ~18.000 empresas entre 2008 y 2020** | INE, DIRCE, tabla 298 (mismo CSV) | 1-ene-2020 | **ALTA** pero **agregada**: 472 incluye carnicerías, pescaderías, fruterías… |
| **CHS-15** | **3.310.824 empresas activas** en España a 1-ene-**2025** (total nacional, contexto) | INE, DIRCE, tabla **4721**, CSV: https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/4721.csv | 1-ene-2025 | **ALTA** (contexto, no sectorial) |
| **CHS-16** | **976 empresas** con CNAE **1082** «Fabricación de cacao, chocolate y productos de confitería» en España | eInforma (Registro Mercantil) — https://www.einforma.com/informes-sectoriales/cnae-1082-empresas-fabricacion-de-cacao-chocolate-y-productos-de-confiteria | balance **2024** | **MEDIA**. Solo cubre sociedades que **depositan cuentas**: deja fuera a los autónomos, que en chocolatería artesana son mayoría. Un resumen de buscador daba **968** el mismo día → el directorio se mueve |
| **CHS-17** | **13.167 empresas** con CNAE **4724** (comercio minorista de pan, panadería, confitería y pastelería); **facturación media por empresa 830.681 €**; **401 altas y 164 bajas** en 12 meses | eInforma — https://www.einforma.com/informes-sectoriales/cnae-4724-empresas-comercio-al-por-menor-de-pan-y-productos-de-panaderia-confiteria-y-pasteleria-en-establecimientos-especializados | 2024 | **MEDIA**, con la misma advertencia. ⚠️ La cifra de «facturación total del sector» que publica esa ficha es **incoherente** con su propia media → §9.2 nº 3 |

> **Conclusión que hay que escribir en la guía, no esconder:** **no existe un número oficial de chocolaterías en España.** Cualquier cifra que circule por internet es una estimación. Es exactamente la misma limitación que tuvo la guía de Pastelería (allí, 1071 mezclaba panadería y pastelería), y se resuelve igual: **contexto sí, cifra de portada no**.

### 2.2 Tamaño del mercado y consumo (CHS-18 … CHS-22)

| id | Dato | Fuente | Fecha | Fiabilidad |
|---|---|---|---|---|
| **CHS-18** | **Valor de consumo de cacao y chocolate en España: 2.323 M€ en 2025, +10,3 %** · **facturación nacional 2.146 M€, +12,3 %** · **exportaciones 858 M€, +35,7 %** · **importaciones 1.034 M€, +25,6 %**, con **99,4 % de origen UE** · **6.994 empleos directos, +1,2 %** (57 % mujeres; >80 % de los jóvenes con contrato fijo) | Informe Produlce 2025 (Asociación Española del Dulce), vía Revista Aral, publicado **10-sep-2026** — https://www.revistaaral.com/texto-diario/mostrar/6008413/consumo-cacao-chocolate-espana-crece-103-hasta-2323-millones-euros · confirmado en Financial Food, publicado **9-sep-2026** — https://financialfood.es/el-consumo-de-cacao-y-chocolate-crece-un-103-en-espana-hasta-los-2-323-millones/ | 2025 | **ALTA** (dos medios sectoriales independientes citando el mismo informe patronal, con cifras idénticas) |
| **CHS-19** | **Reparto por categorías (% del valor):** tabletas **31,3 %** · cacao soluble y **chocolate a la taza 23,0 %** · snacks **19,0 %** · **bombones 13,6 %** · cremas de untar **13,1 %** | Produlce 2025, vía Aral y Financial Food (mismas URLs) | 2025 | **ALTA** |
| **CHS-20** | **El sector del dulce español facturó 8.110 M€ en 2025, +4,5 %** | Informe Produlce 2025 vía Revista Alimentaria — https://revistaalimentaria.es/industria/elaborados/las-ventas-sector-dulce-espanol-superan-8-100-millones-euros-en-2025-un-45-mas-que-ano-anterior | 2025 | **ALTA** |
| **CHS-21** | **Consumo per cápita en hogares: 2,96 kg** (TAM a marzo 2025), desde **3,19 kg** (mar-2024), **3,21 kg** (mar-2023) y **3,54 kg** (2022). **Precio medio 10,11 €/kg, +11,3 %** interanual. En 12 meses a mar-2025, **el consumo cayó 6,1 % y el gasto subió 7,1 %** | MAPA e INE, vía Xataka Magnet, publicado **18-sep-2025** — https://www.xataka.com/magnet/espana-comer-chocolate-se-esta-convirtiendo-lujo-eso-ha-empezado-a-pasar-factura-a-su-consumo | mar-2025 | **MEDIA-ALTA** (prensa generalista citando MAPA e INE con serie coherente). ⚠️ El 10,11 €/kg es **precio de hogar en tienda**, NO coste de materia prima |
| **CHS-22** | **Gasto per cápita 33,88 €** en 2025, con **volumen −6,4 %** y **precios +18 % de media**. El mercado español de chocolate creció **+0,5 % en valor y cayó −4,6 % en volumen** en 2025; exportaciones **+36 %** | Agencia EFE vía Infobae, publicado **12-sep-2026** (= hoy) — https://www.infobae.com/espana/agencias/2026/09/12/el-mercado-del-chocolate-intenta-remontar-tras-la-caida-del-consumo-por-su-alto-precio/ · cita al Ministerio de Agricultura | 2025 | **MEDIA-ALTA** |

**La lectura de negocio, que es lo que importa para la guía:** el mercado crece **en euros y se encoge en kilos**. Desde 2022 el consumo per cápita ha caído de **3,54 kg a 2,96 kg** (−16,4 % en tres años) mientras el precio subía. Para el que monta una chocolatería artesana eso es, paradójicamente, **una buena noticia**: el consumidor ya ha aceptado pagar más por menos cantidad, que es exactamente el terreno del producto artesano. Es el argumento del presidente de la asociación bean-to-bar, citado por EFE: «el consumidor no busca necesariamente chocolate barato, busca que el precio que paga tenga sentido».

### 2.3 Precio medio de mercado (CHS-23)

| id | Dato | Fuente | Fecha | Fiabilidad |
|---|---|---|---|---|
| **CHS-23** | Mercado español de chocolate y cacao: **2.160 M€ y 161.000 t** (TAM a junio 2024, NielsenIQ). El chocolate es «casi un tercio» de los 7.800 M€ de ventas del perímetro Produlce. **El precio del chocolate subió 17,7 % en 2025, tras un 10 % en 2024: casi 30 % acumulado en dos años** | Informe IPMARK «Chocolates/Cacao 2026», citando NielsenIQ — https://ipmark.com/informes/informe-chocolates-cacao-2026/ | 2026 (datos TAM jun-2024 y 2024-2025) | **MEDIA** |

### 2.4 La crisis del cacao 2023-2026 (CHS-24) — **el dato que decide el escandallo**

| id | Dato | Fuente | Fecha | Fiabilidad |
|---|---|---|---|---|
| **CHS-24a** | **2-ene-2026: 4.956 €/t.** Un año antes, **2-ene-2025: >10.300 €/t**. Máximo de 2025: **>10.800 €/t** (finales de enero). Mínimo de 2025: **~4.400 €/t** (noviembre) | Food Retail & Service, publicado **7-ene-2026**, citando expresamente a la **ICCO** — https://www.foodretail.es/fabricantes/el-cacao-se-estrena-en-2026-a-mitad-de-precio-que-en-2025.html | ene-2026 | **MEDIA-ALTA** (prensa sectorial citando la fuente primaria) |
| **CHS-24b** | **12-sep-2026: 5.938 US$/t**, «aproximadamente un 20 % por debajo de hace un año, aunque aún muy por encima de los niveles previos a 2024» | Agencia EFE vía Infobae, **12-sep-2026** — https://www.infobae.com/espana/agencias/2026/09/12/el-mercado-del-chocolate-intenta-remontar-tras-la-caida-del-consumo-por-su-alto-precio/ | **hoy** | **MEDIA-ALTA** |
| **CHS-24c** | La producción mundial 2024/25 revisada al alza hasta **~4,728 M t, +8,4 %** interanual | ICCO vía Procurement Resource — https://www.procurementresource.com/es/resource-center/cocoa-price-trends | 2025/26 | **BAJA** (no leído en la página de la ICCO; L-3) |
| **CHS-24d** | ⚠️ «Aunque en los últimos meses ha habido una notable bajada del precio del cacao, **esto no se ha trasladado a una bajada del precio del chocolate**» | Demócrata — https://www.democrata.es/economia/consumo-cacao-chocolate-espana-mantiene-fortaleza-pesar-aumento-30-precios/ | 2026 | **BAJA** (resumen de buscador; **verificar antes de publicar**) |

> **La lección que tiene que llevar la guía:** el precio de la cobertura **no baja cuando baja el cacao**, o baja con retraso. Un escandallo de chocolatería montado sobre el precio de la bolsa es un escandallo falso: hay que montarlo sobre la **factura del proveedor**, con el precio en **celda verde editable** y una hoja de sensibilidad. Esto encaja directamente con la doctrina de los xlsx de la casa (cero constantes dentro de fórmulas).

⚠️ **CONTRADICCIÓN DETECTADA Y RESUELTA.** Varios medios latinoamericanos (eldiario.ec, extra.ec, latercera.com) sitúan el cacao en 2026 entre **3.000 y 4.500 US$/t**, incluso «perforando los 3.000». Es **incompatible** con los 4.956 €/t de la ICCO en enero y los 5.938 US$/t de EFE hoy. Probablemente mezclan precio de finca / precio local ecuatoriano con la cotización internacional. **Van a la lista negra (§9.2 nº 1).** La cifra que entra es la de §CHS-24a/b.

### 2.5 Tendencias (CHS-25)

| id | Tendencia | Dato | Fuente | Fiabilidad |
|---|---|---|---|---|
| **CHS-25a** | **Bean-to-bar organizado** | Asociación **Bean to Bar** con **45 miembros** entre chocolateros e importadores de cacao. Su listado web permite identificar **~41** (27 makers, 8 importadores/proveedores, 6 museos y espacios) | EFE/Infobae 12-sep-2026 (los 45) — https://www.infobae.com/espana/agencias/2026/09/12/el-mercado-del-chocolate-intenta-remontar-tras-la-caida-del-consumo-por-su-alto-precio/ · listado: https://www.chocolatebeantobar.com/asociados/ | **MEDIA-ALTA** / **ALTA** (listado propio de la asociación) |
| **CHS-25b** | **«Dubai chocolate»** | Búsquedas globales de «Dubai Chocolate» **+128 % entre enero y marzo de 2025**; **13.800 millones** de visualizaciones de #dubaichocolate en TikTok en ese trimestre | WGSN — https://www.wgsn.com/es/blogs/la-tendencia-del-chocolate-de-dubai-como-wgsn-pronostico | **MEDIA** |
| **CHS-25c** | Chocolate **negro, sin azúcar, vegano y de origen** | Valor «lidera el segmento de chocolate negro, que sigue creciendo por las tendencias de bienestar del consumidor». IPMARK cita bean-to-bar, sin azúcar, vegano y «estilo Dubái» como movimientos del mercado | https://www.sweetpress.com/actualidad/chocolates-y-cacao/chocolates-valor-cierra-2025-con-mas-de-220-millones-de-euros-de-facturacion-MI19330059 · https://ipmark.com/informes/informe-chocolates-cacao-2026/ | **MEDIA** |
| **CHS-25d** | **Regalo y experiencias** | Los bombones son el **13,6 %** del valor de la categoría (CHS-19) y el motor de los picos de regalo (§3.5). Los talleres/catas se venden a **25-45 €/persona** (§3.3) | §3.3 y §3.5 | **MEDIA** |

⚠️ **Aviso sobre «Dubai chocolate» para la guía.** Es una moda con **fecha de caducidad declarada por la propia fuente que la pronosticó**: WGSN sitúa su saturación máxima «a finales de 2024 / principios de 2025». Un producto de 65 € que se vende en 2026-2027 **no puede apoyar su capítulo de carta en una moda que ya está transitando**. Va en la guía como **ejemplo de cómo se explota una moda** (y cómo se sale de ella), nunca como recomendación de surtido.

### 2.6 EUDR: el reglamento de deforestación **sí incluye el cacao** (CHS-26)

| id | Dato | Fuente | Fiabilidad |
|---|---|---|---|
| **CHS-26** | El **Reglamento (UE) 2023/1115** cubre madera, **cacao**, café, soja, caucho y palma. El **Reglamento (UE) 2025/2650, de 19-dic-2025**, lo modifica y **retrasa la aplicación al 30-dic-2026** para medianas y grandes empresas, con **seis meses adicionales para micro y pequeñas empresas y personas físicas: 30-jun-2027**. Es el **tercer** aplazamiento (estaba previsto para dic-2024, se fue a dic-2025 y ahora a dic-2026) | TARIC, «Novedades y nueva prórroga… hasta diciembre de 2026» — https://www.taric.es/noticias/2026-01-02-retraso-en-aplicacion-de-reglamento-eudr-hasta-el-30-12-2026/ · AIDIMME — https://actualidad.aidimme.es/2025/12/18/la-ue-aprueba-un-nuevo-aplazamiento-del-reglamento-eudr-por-un-ano-alivia-la-gestion-y-otorga-a-las-pyme-6-meses-mas-de-gracia/ | **MEDIA-ALTA** (dos consultoras especializadas coincidentes) |

**Lo que la guía debe decir — y lo que NO puede decir todavía.** Está verificado que el cacao está dentro y cuáles son las fechas. **NO está verificado** —y no debe escribirse hasta que lo confirme la lente normativa L3 leyendo el reglamento— qué obliga exactamente a:

- una **chocolatería pequeña que compra cobertura ya fabricada a un proveedor de la UE** (lo normal en CHS-03), que previsiblemente actúa como **comerciante** aguas abajo y no como operador que introduce en el mercado; frente a
- un **bean-to-bar que importa grano de fuera de la UE** (CHS-05), que sí es **operador** y a quien le caería la diligencia debida completa.

Esta distinción es **el punto de mayor valor y mayor riesgo de toda la guía**: ninguna fuente gratuita española la explica para un obrador pequeño, y equivocarla es un problema legal para el lector. **Marcada como pregunta obligatoria para L3 (§10).**

### 2.7 Cadmio y RD 1055/2003 — verificado que existen, sin valores (CHS-27)

| id | Dato | Fuente | Fiabilidad |
|---|---|---|---|
| **CHS-27a** | **RD 1055/2003, de 1 de agosto**, aprueba la Reglamentación técnico-sanitaria sobre los productos de cacao y chocolate destinados a la alimentación humana; transpone la **Directiva 2000/36/CE**; es **obligatorio para fabricantes, elaboradores, envasadores, comerciantes e importadores**. **BOE-A-2003-15599** | https://www.boe.es/buscar/doc.php?id=BOE-A-2003-15599 | **ALTA** (existencia y ámbito) · **«sin fuente (valores)»** para porcentajes mínimos, grasas vegetales ≤5 % y definición legal de «chocolate a la taza» |
| **CHS-27b** | El **Reglamento (UE) 2023/915** fija los contenidos máximos de **cadmio** en cacao y chocolate; **los límites dependen del contenido de sólidos de cacao del producto final**; están en vigor desde 2019 (por la norma precedente) | https://eur-lex.europa.eu/legal-content/ES/TXT/PDF/?uri=CELEX:32023R1510 (reglamento modificativo) · contexto: https://cgspace.cgiar.org/server/api/core/bitstreams/b4f2235f-92ac-4ef6-b46a-50f1f723a2eb/content | **MEDIA** (existencia y criterio) · **«sin fuente (valores)»** |

> El cadmio es **el argumento técnico que separa una guía seria de un blog**: es el único contaminante cuyo límite legal **sube con el % de cacao**, es decir, **castiga precisamente al chocolate negro premium** que es el posicionamiento natural del obrador artesano. Y en bean-to-bar depende del **origen del grano**. La guía debe tratarlo como un **criterio de compra de materia prima**, no como una curiosidad. Valores exactos → L3.

---

## 3. Modelo de negocio (CHS-28 … CHS-40)

### 3.1 Precio de la cobertura: la única materia prima que importa (CHS-28)

| id | Producto | Formato | Precio | Base IVA | €/kg | Fuente |
|---|---|---|---|---|---|---|
| **CHS-28a** | **Callebaut 811** (negro 54,5 %) | **bloque 5 kg** | **125,08 €** (rebajado desde 136,48 €) | **CON IVA** (la ficha muestra «precio con IVA incluido») | **25,02 €/kg** (125,08 ÷ 5) | Planeta Torta — https://www.planeta-torta.es/los-chocolates-reposteria-gotas-fundir/11351-chocolate-negro-de-cobertura-811-de-callebaut-55-en-bloque-5-kg.html |
| **CHS-28b** | Callebaut 811 callets | 1 kg | **24,40 €** | **BAJA** — no leído en la página | 24,40 €/kg | Gadgets & Cuina (vía resumen de buscador) — https://www.gadgetscuina.com/cobertura-chocolate-negro-callebaut-811-54-5-1-kg-16514.1017 |
| **CHS-28c** | **Valrhona pepitas** | 400 g | **14,99 €** | **no declarada** | **37,48 €/kg** (14,99 ÷ 0,4) | Club del Chocolate — https://www.clubdelchocolate.com/en/452-cobertura-valrhona |
| **CHS-28d** | Valrhona **Guanaja 70 %** 35,50 € · **Ivoire 35 %** 39,95 € · **Jivara 40 %** 39,95 € · **Dulcey 32 %** 41,95 € | **⚠️ formato NO indicado en la página** | — | no declarada | **NO CALCULABLE** | misma URL |

> **Conclusión operativa:** la cobertura profesional de referencia está hoy en **~25 €/kg con IVA** (Callebaut, formato bloque de 5 kg, el que compra un obrador) y las coberturas de gama alta tipo Valrhona en **~37 €/kg**. **Un factor 1,5 entre las dos**, que es la decisión de posicionamiento más cara del negocio y debe ser un **parámetro en celda verde**, nunca una constante.
>
> ⚠️ Los cuatro precios de Valrhona de CHS-28d **no se pueden usar**: sin el formato, dividir es inventar. Van a la lista negra (§9.2 nº 13).
>
> ⚠️ **Para el escandallo hay que decidir la base.** El 25,02 €/kg lleva IVA; el tipo aplicable al chocolate en España **no se verificó en esta lente** y es una cuestión fiscal que corresponde a L3. **No se ha calculado aquí el precio sin IVA** precisamente para no introducir el error que hundió la L4 de Pastelería.

### 3.2 Precio de venta al público del bombón artesano (CHS-29)

| id | Producto | Precio | €/unidad | Fuente | Fiabilidad |
|---|---|---|---|---|---|
| **CHS-29** | Bombones artesanos, caja **12 uds** | **20,00 €** | **1,67 €** | Confitería Gascón — https://www.confiteriagascon.com/bombones-artesanos-caja-mediana-20-unidades_pr385952 | **MEDIA** |
| | Caja **20 uds** | **28,00 €** | **1,40 €** | misma URL | **MEDIA** |
| | Caja **35 uds** | **45,00 €** | **1,29 €** | misma URL | **MEDIA** |

⚠️ **La página NO publica el peso**, así que **no hay €/kg** y la comparación directa con el coste de la cobertura **no se puede cerrar aquí**. Lo que sí se ve, y es un hallazgo aprovechable: **el precio por bombón baja un 23 % de la caja de 12 a la de 35** (1,67 → 1,29 €). Esa **escalera de precio por formato** es una decisión de carta que la guía debe enseñar con su propia hoja de cálculo, y es exactamente el tipo de cosa que ninguna fuente gratuita de la SERP explica.

⚠️ **La página tampoco declara si los precios llevan IVA.**

### 3.3 Talleres y catas (CHS-30)

| id | Dato | Fuente | Fiabilidad |
|---|---|---|---|
| **CHS-30** | **25-45 €/persona**, con mínimo habitual de **6 personas** y duración de **90-150 min**. Referencias concretas: Madrid 26 € · Madrid 45 € · Valencia 30 € (mín. 6 pax) · Murcia 25 € (IVA incluido, mín. 6 pax) · Madrid ~30 € (sábados por la mañana) | Agregado de https://www.tallerdechocolate.es/talleres-de-chocolate/talleres-en-madrid/ · https://www.gastronomiaactiva.com/catas-en-barcelona/taller-cata-de-chocolates-premium/ · https://www.clubdelchocolate.com/en/1939-cata-chocolate-presencial-grupo.html · https://helenchocolate.es/producto/cata-de-chocolates-en-madrid/ | **MEDIA** (precios públicos de varios operadores, leídos vía buscador; **verificar 2-3 en página antes de publicar**) |

> **Por qué esta línea merece capítulo propio:** un taller de 8 personas a 30 € son **240 € de ingreso** con un consumo de materia prima marginal y **cero riesgo de merma**. Es la única línea del negocio que **no depende del precio del cacao** y que **funciona en agosto**, que es el valle (§3.5). En la matriz de sub-conceptos es CHS-11 y debería estar en el P&L como línea separada, no como «otros ingresos».

### 3.4 Chocolate a la taza y churros: el margen (CHS-31 … CHS-33)

| id | Dato | Fuente | Fiabilidad |
|---|---|---|---|
| **CHS-31** | **Margen bruto del churro: 85-90 %** («uno de los más altos de la pastelería rápida»). Un maestro churrero citado lo rebaja a «un poco más del 50 %» | Loomis Pay, «Rentabilidad de una churrería: ingresos y costes 2025» — https://es.loomispay.com/blog/rentabilidad-churreria-2025 · contraste: https://www.elespanol.com/sociedad/20251021/dueno-negocio-churros-anos-historia-vendemos-raciones-dia-rentabilidad/1003743974262_0.html (21-oct-2025) | **MEDIA**. ⚠️ **Los dos números difieren en 35 puntos**: probablemente uno es margen bruto sobre materia prima y el otro margen neto. **La guía debe publicar los dos y decir por qué difieren**, no elegir el más bonito |
| **CHS-32** | **Precio por pieza 0,30-0,70 €** · **ración de 4 uds ~2,50 €** · **con chocolate el ticket sube a 3,50-4 €** | Loomis Pay (misma URL) | **MEDIA** |
| **CHS-33** | **Ingredientes y aceite ≈ 20 % de la facturación**. Ingresos mensuales de una churrería **3.000-6.000 €**; un negocio bien gestionado, **40.000-60.000 € de beneficio anual** | Loomis Pay (misma URL) · https://qamarero.com/blog/cuanto-dinero-se-gana-con-una-churreria-es-rentable/ | **MEDIA** / **BAJA** (el beneficio anual, solo en resumen de buscador) |

> **El dato de negocio:** **el chocolate es lo que convierte 2,50 € en 3,50-4 €** — un **+40 % a +60 % de ticket** por añadir la taza. Es el argumento comercial de CHS-07 y, curiosamente, también el argumento para que **una bombonería CHS-03 se plantee servir chocolate a la taza en invierno**: sube el ticket sin tocar el obrador. Es una recomendación cruzada que la guía puede dar y que no está en ninguna fuente.

### 3.5 Estacionalidad (CHS-34 … CHS-36)

| id | Dato | Fuente | Fiabilidad |
|---|---|---|---|
| **CHS-34** | **Tres picos del año: Navidad, San Valentín y Halloween.** «Las ventas de chocolates y dulces **pueden llegar a duplicar el promedio anual** en San Valentín». **Hay compañías que hacen en San Valentín hasta el 10 % de su venta anual** | Produlce vía Financial Food, publicado **10-feb-2025** — https://financialfood.es/las-ventas-de-chocolates-y-dulces-pueden-llegar-a-duplicar-el-promedio-anual-en-san-valentin/ | **MEDIA-ALTA** (prensa sectorial citando a la patronal) |
| **CHS-35** | **Febrero es el 4º mes del año con más ventas de bombones**, con **21,89 M€** | Produlce vía Cantabria Económica — https://www.cantabriaeconomica.com/la-economia-hoy/san-valentin-uno-de-los-tres-momentos-del-ano-que-impulsan-las-ventas-de-bombones-y-caramelos-en-espana/ | **MEDIA**. ⚠️ Dato de **2022** según la propia nota → **envejecido**, usar solo como orden de magnitud |
| **CHS-36** | Los **bombones son el 13,6 % del valor** de la categoría cacao/chocolate (2025); en 2022 Produlce los situaba en el **18,2 %** del total de chocolate y cacao | CHS-19 (2025) · https://www.cantabriaeconomica.com/… (2022) | **ALTA** (2025) / **BAJA** (2022) |

⚠️ **Lo que NO se encontró y hay que declarar: no hay dato público del reparto mensual de ventas de una chocolatería española.** Ni Navidad vs resto, ni monas de Pascua, ni Día de la Madre, ni la profundidad del valle de verano. **Es exactamente la limitación L-6 de la guía de Pastelería** y se resuelve igual: **hoja de estacionalidad con curva editable por el lector y supuesto explícito**, nunca con una curva inventada.

Lo que sí está verificado y sostiene el capítulo:
- Los tres picos existen y están nombrados por la patronal (CHS-34).
- Uno de ellos **puede duplicar la media** (CHS-34).
- Hasta el **10 % de la venta anual** puede concentrarse en un solo evento (CHS-34).
- El verano es un valle **estructural, no comercial**: el chocolate no aguanta ni la vitrina ni el envío sin frío (§4.4 y CHS-10). **De ahí la lógica de CHS-09 (heladería) y CHS-11 (talleres) como contraestacionales.**

### 3.6 Traspasos reales — la mejor prueba de m², rentas y precios (CHS-37 … CHS-39)

**Consultados en Milanuncios el 2026-09-12.** ⚠️ Son **precios PEDIDOS**, no pagados.

| id | Negocio | Provincia | m² | Traspaso | Alquiler/mes | Otros datos |
|---|---|---|---|---|---|---|
| **CHS-37a** | Chocolatería-churrería | **Elche (Alicante)** | **75** | no publicado | no publicado | **Facturación >150.000 € (2023)**; previsión de beneficios >100.000 € (2024) ⚠️ el mismo anuncio aparece duplicado bajo Murcia |
| **CHS-37b** | Churrería-chocolatería | **Madrid (Vallecas)** | **74** | **82.000-95.000 €** (negociables) | **910 €** | «Beneficio neto anual demostrado» (sin cifra) |
| **CHS-37c** | Churrería-chocolatería | **Mataró (Barcelona)** | **118** | **58.000 €** | no publicado | — |
| **CHS-38a** | Pastelería-**bombonería** con obrador (40+ años) | **El Prat de Llobregat (BCN)** | **90** | **26.000 €** | **1.100 €** | Obrador completamente equipado |
| **CHS-38b** | Pastelería-bombonería histórica (34 años) | **Reus (Tarragona)** | **300** | **73.000 €** | no publicado | Dos zonas con salida de humos |
| **CHS-38c** | Pastelería-bombonería, obrador a la vista | **Barcelona (Sagrada Familia)** | **180** | **140.000 €** | **2.200 €** | Diseño moderno |
| **CHS-38d** | Pastelería con obrador profesional | **Valencia (Abastos)** | **100** | **180.000 €** | no publicado | Hornos Salva, fermentadora, abatidor, cámaras |
| **CHS-38e** | Obrador de pastelería y panadería | **Lliçà d'Amunt (BCN)** | **400** | **210.000 €** | no publicado | — |

Fuentes: https://www.milanuncios.com/traspasos/chocolateria.htm y https://www.milanuncios.com/traspasos/bomboneria.htm (consultados 2026-09-12). Fiabilidad **MEDIA-ALTA** como evidencia de mercado, **BAJA** como precio de transacción.

| id | Lectura |
|---|---|
| **CHS-39** | **El rango de traspaso de un negocio de chocolate en marcha va de 26.000 € (90 m², El Prat) a 210.000 € (400 m², obrador)**, y **la renta observada de 910 a 2.200 €/mes**. El caso más informativo es CHS-38a: **26.000 € por 90 m² con obrador equipado y 40 años de clientela** — es decir, **traspasar puede salir más barato que montar de cero** (CHS-03: 20.000-80.000 € **sin** local ni clientela). La guía debe tener **la comparativa traspaso vs obra nueva como decisión explícita**, igual que la tiene la de Pastelería |

⚠️ **Ninguno de los ocho anuncios es una bombonería artesana pura.** Es un dato en sí mismo: **el negocio de chocolate puro se traspasa poco** porque, en su mayoría, es un obrador unipersonal cuyo valor está en las manos del titular. Eso refuerza el sub-concepto CHS-01/CHS-02 como puerta de entrada real.

### 3.7 Punto de equilibrio (CHS-40)

| id | Dato | Fuente | Fiabilidad |
|---|---|---|---|
| **CHS-40** | Con **costes fijos de 4.000 €/mes** y **margen bruto de 1,50 €/unidad**, el equilibrio está en **~2.667 unidades/mes ≈ 89/día**. Escenario de ventas: **80-120 unidades/día a 2,50 € de media → 6.000-9.000 €/mes**. Gastos mensuales: materias primas 1.500-2.500 € · sueldos (1-2 empleados) 2.000-3.000 € · suministros 300-500 € · marketing 300-500 €. Beneficio: **1.500-2.000 €/mes** optimista, **500 € o pérdidas** conservador | plandenegocio.es, **17-dic-2025** — https://plandenegocio.es/como-hacer-un-plan-de-negocio-para-chocolateria/ | **MEDIA-BAJA** |

⚠️ **Tres avisos sobre CHS-40, y son importantes:**
1. La aritmética **cuadra** (4.000 ÷ 1,50 = 2.666,7 ✓; 2.667 ÷ 30 = 88,9 ✓), lo cual es más de lo que se puede decir de la mayoría de fuentes de la SERP.
2. Pero **el ticket de 2,50 €/unidad no casa con el PVP del bombón artesano medido en CHS-29** (1,29-1,67 €/ud) ni con una caja de regalo (20-45 €). El «2,50 €» parece una unidad genérica de pastelería, no un bombón. **Usar el método, no el número.**
3. Es del **mismo dominio** que comete el error del carnet de manipulador (§9.2 nº 15). Entra **solo como escenario editable**, jamás como promesa de rentabilidad.

---

## 4. Equipamiento crítico, con marca, precio y **base de IVA declarada**

> **Regla que se aplicó:** cada línea dice si el precio es **CON IVA**, **SIN IVA** o **base NO declarada**, con la frase literal de la web cuando existe. **No se ha convertido ninguna base.** Ésta es la corrección directa del defecto que la refutación tumbó en la L4 de Pastelería.

### 4.1 Atemperadoras (CHS-41)

| id | Modelo | Capacidad | Precio | Base IVA | Fuente |
|---|---|---|---|---|---|
| **CHS-41a** | **Selmi One** | 12 kg (55 kg/h) | **8.500 €** · **+1.045 €** de embalaje, transporte asegurado y puesta en marcha | ⚠️ **base NO declarada** para el precio principal. La ficha dice literalmente: «A este precio se le debe añadir **1045 €/Neto** por Embalaje, Transporte asegurado y Puesta en Marcha» → el uso de «Neto» apunta a **SIN IVA**, pero **la web no lo afirma** | Utilcentre — https://www.utilcentre.com/temperadora-selmi-one-12kg.html · potencia 1 kW / 16 A · 38×73×H147 cm |
| **CHS-41b** | **Selmi Color EX** | 12 kg | **12.300 €** | base NO declarada | Utilcentre — https://www.utilcentre.com/maquinaria-chocolate.html |
| **CHS-41c** | **Selmi Ghana-Legend** | 24 kg | **12.300 €** | base NO declarada | misma URL |
| **CHS-41d** | **Selmi Plus EX** | 24 kg | **18.500 €** | base NO declarada | misma URL |
| **CHS-41e** | **Selmi Futura EX** | 35 kg | **21.500 €** | base NO declarada | misma URL |
| **CHS-41f** | **Selmi Top EX** | 60 kg | **27.500 €** | base NO declarada | misma URL |
| **CHS-41g** | **Selmi Cento EX** | 100 kg | **45.000 €** | base NO declarada | misma URL |
| **CHS-41h** | **Pavoni MINITEMPER** | 4,5 L (≈3 kg) | **1.960,00 €** · cubeta adicional **165,30 €** | base NO declarada | Utilcentre — https://www.utilcentre.com/maquinaria/chocolate/temperadoras.html |
| **CHS-41i** | Mantenedor 1 cubeta digital | — | **desde 570,00 €** | base NO declarada | misma URL |
| **CHS-41j** | Temperador baño maría digital | 22 L | **2.650,00 €** | base NO declarada | misma URL |

⚠️ **Precio contradictorio detectado.** Chocosolutions publica la misma Selmi One 12 kg a **7.400 € + IVA** (https://chocosolutions.com/products/temperadora-selmi-one-12-kg, «Estos precios son en euros, **Más IVA**, Más gastos de envío e importación»). Pero **es una tienda mexicana** (teléfono +52 81 8363-2182) y el precio lleva costes de importación aparte: **no es precio del mercado español** y va a la lista negra (§9.2 nº 12). El precio de referencia para España es el de Utilcentre.

> **La escalera está limpia y es una tabla de decisión excelente para la guía:** de **1.960 €** (Minitemper, 3 kg — obrador en casa / arranque) a **8.500 €** (Selmi One, 12 kg — el estándar profesional de entrada) a **27.500 €** (Top EX, 60 kg — producción). **Un factor 14 entre los extremos**, y la elección depende de los kilos/semana que salga el lector en la hoja de capacidad de obrador. Ese cruce —kg/semana → máquina— es el corazón del capítulo de equipamiento, y **no existe en ninguna fuente gratuita**.

### 4.2 Enrobadoras, bañadoras y dosificación (CHS-42)

| id | Equipo | Precio | Base IVA | Fuente |
|---|---|---|---|---|
| **CHS-42a** | Enrobadora **Selmi R200 Legend** | **6.800 €** | base NO declarada | https://www.utilcentre.com/maquinaria-chocolate.html |
| **CHS-42b** | Enrobadora **Selmi RS 200** | **8.500 €** | base NO declarada | misma URL |
| **CHS-42c** | Enrobadora **Selmi RS 250** | **9.700 €** | base NO declarada | misma URL |
| **CHS-42d** | **Truffle Dipper** | **8.200 €** | base NO declarada | misma URL |
| **CHS-42e** | **Truffle Dipper automático** | **14.900 €** | base NO declarada | misma URL |
| **CHS-42f** | **Filler Piastra** 6 kg | **9.000 €** | base NO declarada | misma URL |
| **CHS-42g** | **Filler Vasi** 6 kg | **7.400 €** | base NO declarada | misma URL |
| **CHS-42h** | **Filler Vasi automática** 6 kg | **11.300 €** | base NO declarada | misma URL |
| **CHS-42i** | **Placa dosificadora** | **1.495 €** | base NO declarada | misma URL |
| **CHS-42j** | Filtro de papel (pack 4) | **150 €** | base NO declarada | misma URL |

⚠️ **No se encontró precio publicado de guitarra de corte.** «sin fuente (precio)».

### 4.3 Vitrina de tienda (CHS-43) — **la única refrigeración cuyo rango de temperatura es distinto**

| id | Equipo | Precio | Base IVA | Fuente |
|---|---|---|---|---|
| **CHS-43** | **Vitrina refrigerada Docriluc WB-6-6-R / VVB-6-6-R** para chocolates y bombones. **600×730×1380 mm**. **Temperatura de trabajo para chocolates: +14 °C a +17 °C**. Condensación y evaporación **ventiladas** | **2.684,99 €** (oferta; antes **3.487,00 €**) | ✅ **SIN IVA — declarado literalmente**: «2.684,99 € **sin impuestos**» | Equipo H — https://www.equipoh.com/vitrinas-expositoras/vitrina-expositora-refrigerada-para-chocolate-docriluc-wb-6-6-r-2824.html |

> **El dato técnico que justifica el capítulo:** **+14/+17 °C**, no los +2/+4 °C de una vitrina de pastelería. Una vitrina de pastelería **arruina** el bombón (condensación, *sugar bloom*, pérdida de brillo). Es un error caro y frecuentísimo, y la fuente lo hace explícito al llamar a la gama «temperatura de trabajo **para chocolates**». Infrico tiene la gama equivalente (Lyon VLY B, Niza VNZ 12 B, **7-12 °C**) pero **su ficha devolvió 404** y no hay precio verificado → «sin fuente (precio)».

### 4.4 Clima del obrador (CHS-44) — **el coste que nadie presupuesta**

| id | Dato | Fuente | Fiabilidad |
|---|---|---|---|
| **CHS-44** | «El rango óptimo para trabajar con cobertura está **entre 18 y 22 °C**». «El aire acondicionado debería estar funcionando **al menos una hora antes** de empezar a trabajar el chocolate, para que toda la sala —incluidos mármoles, utensilios y moldes— alcance esa temperatura estable». «Un deshumidificador es una inversión que se amortiza rápido en obradores de clima mediterráneo o costero, y **mantener la humedad relativa por debajo del 55 %** reduce significativamente los problemas de agarre y opacidad» | Llevats21, «Cómo trabajar el chocolate en el obrador en verano» — https://llevats21.com/como-trabajar-el-chocolate-en-el-obrador-en-verano/ | **MEDIA** (blog técnico del sector, sin fecha visible) |

⚠️ **«sin fuente (precio)»** para la cámara climatizada de chocolate y el deshumidificador profesional dimensionado (L-8). Lo único con precio que se encontró es de consumo general (climatizador evaporativo industrial **desde 365 €** para 60 m², https://www.enervill.es/climatizadores-evaporativos-portatiles/) y **no sirve** para un obrador de chocolate: un evaporativo **añade humedad**, que es exactamente lo contrario de lo que necesita el chocolate. **No usarlo.**

> ⚠️ **DISCREPANCIA A RESOLVER EN LA GUÍA.** El brief de este encargo habla de «cámara de chocolate 16-18 °C, HR 50-60 %» y la fuente verificada dice **18-22 °C de sala** y **HR <55 %**. **Son dos cosas distintas**: la temperatura de la **sala de trabajo** (18-22 °C) y la de la **cámara de conservación del producto acabado** (más fría). La guía debe separarlas explícitamente. **La cifra de la cámara de conservación queda «sin fuente» y no debe escribirse hasta verificarla.**

### 4.5 Moldes, chocolateras y pequeño material (CHS-45 … CHS-46)

| id | Equipo | Precio | Base IVA | Fuente |
|---|---|---|---|---|
| **CHS-45a** | **Moldes de policarbonato Chocolate World**: rango **24,20 € – 42,83 €**/ud. Ejemplos: CF0246 Rosa Davide Comaschi **24,20 €** · CW12064 Óvalo Facetas **25,17 €** · Molde magnético CW1000L07 Sol **42,83 €** | ver columna | base NO declarada | RestorHome — https://www.restorhome.es/471-moldes-bomboneria-Chocolate-World |
| **CHS-45b** | Moldes **Martellato**: ~**17,85 €**/ud, con ofertas desde 8,93 € | | **BAJA** (solo resumen de buscador) | https://www.marialunarillos.com/martellato.html |
| **CHS-46a** | **Chocolatera Ugolini Delice 3** (3 L) | **527,00 €** | ✅ **SIN IVA — declarado**: «Estos precios se entienden sin IVA» | Equipo H — https://www.equipoh.com/chocolateras-196 |
| **CHS-46b** | **Ugolini Delice 5** (5 L) | **631,55 €** | ✅ SIN IVA | misma URL |
| **CHS-46c** | **Ugolini Delice 5 Gold** (5 L) | **748,00 €** | ✅ SIN IVA | misma URL |
| **CHS-46d** | **Campeona TXM/5-LB** (5 L) | **833,00 €** | ✅ SIN IVA | misma URL |
| **CHS-46e** | **Campeona TXM/14-LC** (14 L) | **1.521,50 €** | ✅ SIN IVA | misma URL |
| **CHS-46f** | **Campeona TXM/40-LC** (40 L) | **2.159,00 €** | ✅ SIN IVA | misma URL |

⚠️ **Anomalía en el listado de chocolateras Campeona, verificar antes de usar:** la **TXM/9-LB (9 L) cuesta 1.015,75 €**, menos que la **TXM/7-LC (7 L) a 1.300,50 €**; y la **TXM/20-LC (20 L) a 1.500,25 €** cuesta menos que la **TXM/14-LC (14 L) a 1.521,50 €**. La serie **no es monótona**, lo que apunta a que las letras finales (LB/LC) designan acabados distintos, o a un error del listado. **Solo se incorporan a la guía las líneas de la serie LB y LC por separado, o ninguna.** Va al §9.2 nº 14.

### 4.6 **Dotación tipo de un obrador de bombonería 30-50 m² + tienda 25-40 m²** (CHS-47)

> ⚠️ **Léase esto antes que la tabla.** Lo que sigue **NO es un presupuesto de apertura**. Es **la suma de las líneas con precio verificado**, y nada más. Las partidas que faltan (obra, instalación eléctrica, frío del obrador, mobiliario de tienda, TPV) **no tienen precio público** y **deliberadamente no se han estimado**: inventarlas sería exactamente lo que la regla de la casa prohíbe. La guía debe resolverlas con **presupuestos reales del lector en celda verde**.

**Escenario A — profesional de entrada** (CHS-47a)

| Línea | id | Importe | Base |
|---|---|---|---|
| Atemperadora Selmi One 12 kg | CHS-41a | 8.500,00 € | no declarada |
| Embalaje + transporte + puesta en marcha | CHS-41a | 1.045,00 € | «Neto» |
| Enrobadora Selmi R200 Legend | CHS-42a | 6.800,00 € | no declarada |
| Placa dosificadora | CHS-42i | 1.495,00 € | no declarada |
| 12 moldes de policarbonato Chocolate World (12 × 30 €, dentro del rango 24,20-42,83 €) | CHS-45a | 360,00 € | no declarada |
| Temperador baño maría digital 22 L | CHS-41j | 2.650,00 € | no declarada |
| Mantenedor 1 cubeta digital | CHS-41i | 570,00 € | no declarada |
| Vitrina Docriluc WB-6-6-R (tienda) | CHS-43 | 2.684,99 € | **SIN IVA** |
| **TOTAL de las líneas verificadas** | **CHS-47a** | **24.104,99 €** | ⚠️ **BASE MIXTA — no sumable como cifra fiscal** |

*Comprobación: 8.500 + 1.045 = 9.545 · +6.800 = 16.345 · +1.495 = 17.840 · +360 = 18.200 · +2.650 = 20.850 · +570 = 21.420 · +2.684,99 = **24.104,99 €**.*

**Escenario B — arranque mínimo viable** (CHS-47b)

| Línea | id | Importe |
|---|---|---|
| Pavoni Minitemper 4,5 L | CHS-41h | 1.960,00 € |
| Cubeta adicional | CHS-41h | 165,30 € |
| Mantenedor 1 cubeta digital | CHS-41i | 570,00 € |
| 12 moldes de policarbonato | CHS-45a | 360,00 € |
| Vitrina Docriluc WB-6-6-R | CHS-43 | 2.684,99 € |
| **TOTAL de las líneas verificadas** | **CHS-47b** | **5.740,29 €** |

*Comprobación: 1.960 + 165,30 = 2.125,30 · +570 = 2.695,30 · +360 = 3.055,30 · +2.684,99 = **5.740,29 €**.*

**Lo que FALTA en ambos escenarios y NO tiene precio verificado** («sin fuente (precio)»): obra y adecuación · instalación eléctrica (trifásica, kW) y de agua · **cámara/armario de conservación de chocolate** · **climatización y deshumidificación del obrador** · mesa de mármol o granito · mesas de trabajo de inox y fregaderos · abatidor · microondas e inducción · balanza · **TPV** · **packaging** · mobiliario y rótulo de tienda · licencias y proyecto técnico · **fondo de maniobra y stock inicial de cobertura**.

> **Dato de contraste útil:** la única fuente publicada que da un número completo (CHS-03) sitúa la apertura de una chocolatería de tamaño medio en **20.000-30.000 €, hasta 80.000 €**. El núcleo de máquina profesional verificado aquí ya son **24.105 €**. **Las dos cifras solo son compatibles si la fuente está pensando en un obrador con Minitemper (escenario B, 5.740 €) y no con Selmi.** Eso es exactamente lo que la guía tiene que hacer explícito, y es un argumento de venta en sí mismo: **el rango publicado de «20.000-30.000 €» esconde dos negocios distintos.**

### 4.7 Bean-to-bar (CHS-48)

| id | Equipo | Precio | Fuente |
|---|---|---|---|
| **CHS-48** | Tostador, bandeja de enfriado, descascarilladora manual de lujo y *winnower* básico (kit de entrada) · melanger Deluxe **ECGC 12SLTA** · molinos/conchas de gran escala | **«sin fuente (precio)»** | CocoaTown España — https://cocoatown.com/es/collections/entry-kit y https://cocoatown.com/es/products/professional-kit · Premier/DCM — https://www.melangers.com/ (envío desde EE. UU.) · maquinaria y líneas bean-to-bar en España: **KM0Chocolate** — https://km0chocolate.es/ |

**Los catálogos existen y están verificados; los precios no son públicos.** Para la guía esto es **un hallazgo, no un fallo**: significa que el lector que quiera ir a bean-to-bar **va a tener que pedir presupuesto sí o sí**, y la guía debe darle la **lista de la compra y las preguntas que hacer**, no un número falso. Es coherente con que el bean-to-bar sea CHS-05, un sub-concepto de segunda fase.

### 4.8 Chocolate a la taza y churros (CHS-49)

- **Chocolatera:** verificada con precio, §4.5 (Ugolini 527-748 €, Campeona 833-2.159 €, todos **SIN IVA declarado**).
- **Churrera, freidora y extracción:** **«sin fuente (precio)»**. Fabricantes y distribuidores verificados: **Inblan** — https://www.inblan.com/maquinaria-para-churreria/ (fabrica churreras y calientachocolates de acero inoxidable) · **HostelShop España** — https://hostelshopespana.com/maquinaria-de-hosteleria-para-churrerias/ · **Churrofácil** — https://www.churrofacil.com/tienda/es/12-maquinarias-y-repuestos.

---

## 5. Proveedores reales, verificados con URL (CHS-50 … CHS-56)

> Solo se listan nombres que se han visto en una URL real. **Ninguno inventado.** Los marcados 🔎 se identificaron en resultados de búsqueda pero **su web no se abrió**: verificar antes de publicar.

### 5.1 Coberturas y chocolate profesional (CHS-50)

| Proveedor | Qué vende | URL | Verificación |
|---|---|---|---|
| **Barry Callebaut Ibérica** (Callebaut, Cacao Barry, Chocovic) | Cobertura profesional. Es el mayor grupo del sector con presencia industrial en España | https://www.callebaut.com/es-ES/ | ✅ citado por Alimarket como inversor activo en España — https://www.alimarket.es/alimentacion/informe/415633/informe-2025-del-sector-de-chocolates-y-cacao-para-uso-industrial |
| **Valrhona** | Cobertura de gama alta (Guanaja, Ivoire, Jivara, Dulcey) | distribución ES: https://www.clubdelchocolate.com/en/452-cobertura-valrhona | ✅ precios vistos |
| **Chocolates Torras** (Girona) | **Línea profesional de coberturas** negro/leche/blanco, «con y sin azúcar», más de un siglo | https://chocolatestorras.com/profesional/ | ✅ página profesional propia verificada |
| **Simón Coll** (Sant Sadurní d'Anoia, 1840) + **Amatller** (1797, adquirida en 1972) | Chocolate **bean-to-bar desde 1840** | https://www.simoncoll.com/es/sobre-simon-coll/historia | ✅ |
| **Sosa Ingredients** | Ingredientes de alta gama para gastronomía y pastelería (pralinés, frutos secos, texturizantes) | https://www.sosa.cat/ | 🔎 nombre verificado en fuente sectorial; web no abierta |
| **Natra** | Derivados del cacao, **>220 M€ de ingresos** por derivados del cacao | https://www.alimarket.es/alimentacion/informe/415633/… | ✅ (cifra vía Alimarket) |
| **Grupo Nederland**, **Norte Eurocao** | Derivados del cacao para uso industrial; citados como inversores activos | misma URL de Alimarket | ✅ (mención) |
| **Blanxart** | Chocolate artesano | 🔎 **no verificado**: la búsqueda no devolvió su web ni datos de empresa. **No publicar sin verificar** |

### 5.2 Grano de cacao para bean-to-bar (CHS-51)

⚠️ **Bloque de riesgo alto.** Ninguna de estas webs se abrió; todas proceden de directorios o del listado de la asociación.

| Proveedor | Origen del dato | Verificación |
|---|---|---|
| **Kahkow Europa** (Valencia) | Listado de asociados de la Asociación Chocolate Bean to Bar España — https://www.chocolatebeantobar.com/asociados/ | ✅ **ALTA** (listado de la propia asociación sectorial) |
| **Essenzo Cacao**, **Intensa Cacao**, **Top Kokoa**, **Orilla Cacao**, **Lopetes Artesanos**, **Chocolates OrigenEcuador**, **Clorawfila** | mismo listado | ✅ **ALTA** como miembros; 🔎 web y condiciones de venta **sin verificar** |
| **Killa Foods** (Barcelona), **Grupo Meza**, **Amari Cacao Import SL** (País Vasco), **Cacao del Norte** | Directorio Proveedores.com — https://www.proveedores.com/importadores_t/cacao-en-grano | 🔎 **BAJA** — solo resumen de buscador |

> **La recomendación para la guía es el propio hallazgo:** la vía fiable para que un obrador pequeño encuentre grano en España **no es un buscador, es la Asociación Chocolate Bean to Bar** (§6.4), que publica su directorio de asociados incluyendo importadores. Eso es un consejo accionable y verificado que ninguna fuente de la SERP da.

### 5.3 Maquinaria (CHS-52)

| Proveedor | Qué vende | URL | Verificación |
|---|---|---|---|
| **Utilcentre, S.L.** | Distribuidor **Selmi** en España + Pavoni. **Precios públicos** | https://www.utilcentre.com/maquinaria-chocolate.html | ✅ precios leídos |
| **Selmi Group** (fabricante) | Atemperadoras, enrobadoras, fillers | https://www.selmi-group.com/ | ✅ |
| **KM0Chocolate** | Maquinaria profesional y **líneas bean-to-bar** en España | https://km0chocolate.es/ | 🔎 título verificado en buscador; web no abierta |
| **CocoaTown** (tienda ES) | Kits bean-to-bar completos | https://cocoatown.com/es/ | ✅ catálogo verificado, sin precio |
| **Equipo H** | Vitrinas, chocolateras. **Precios públicos SIN IVA declarado** | https://www.equipoh.com/ | ✅ |
| **Deldivel**, **Frigeria Hostelería**, **Clifrihos**, **Multiservicios Vallés** | Distribuidores de vitrinas Docriluc / Infrico | https://www.deldivel.es/ · https://frigeriahosteleria.com/ · https://tienda.clifrihos.com/ | 🔎 listados, sin precio verificado |
| **Inblan** | Fabricante de churreras y calientachocolates | https://www.inblan.com/maquinaria-para-churreria/ | ✅ |

### 5.4 Utensilios y moldes (CHS-53)

| Proveedor | URL | Verificación |
|---|---|---|
| **RestorHome** (moldes Chocolate World, Pavoni, Martellato) | https://www.restorhome.es/471-moldes-bomboneria-Chocolate-World | ✅ precios leídos |
| **María Lunarillos** | https://www.marialunarillos.com/martellato.html · https://www.marialunarillos.com/para-bombones-y-piruletas.html | 🔎 precios solo vía buscador |
| **El Món Dolç de Clàudia** | https://www.elmondolcdeclaudia.com/es/moldes-para-bombones-y-chocolate-chocolate-world/ | ✅ existe |
| **Chocolate World** (fabricante, modelos CW####) | referenciado en RestorHome | ✅ |

### 5.5 Packaging (CHS-54)

| Proveedor | Qué vende | URL | Verificación |
|---|---|---|---|
| **SelfPackaging** | Cajas y estuches para bombones; personalización con logo desde pocas unidades | https://selfpackaging.es/90-cajas-para-bombones | ⚠️ **HTTP 403** — **«sin fuente (precio)»** (L-6) |
| **García de Pou** | Envases de cartón personalizados para alimentación | https://www.garciadepou.com/es/envases-de-carton-personalizados | ✅ existe, sin precio |

### 5.6 Regalo corporativo B2B (CHS-55)

| Proveedor | Dato | URL |
|---|---|---|
| **Gift Campaign** | Bombones y chocolates personalizados **«desde 0,30 €»** | https://www.giftcampaign.es/dulces-personalizados/chocolates.html |
| **Regalo Publicidad** | **«desde 0,35 €»** | https://www.regalopublicidad.com/ocio-y-aire-libre/caramelos-personalizados/chocolates |
| **Lindt España** | Canal de venta a empresas propio de la marca | https://www.lindt.es/venta-a-empresas |
| **Cornet 1945** | Línea corporativa para hoteles, eventos, ferias y empresa | https://www.cornetxocolaters.com/categoria-producto/corporativo/ |
| **QuieroChocolate**, **NoSoloDulce**, **Regalo Chocolate** | Cajas de bombones personalizados de empresa | https://quierochocolate.com/regalo-corporativo/ · https://nosolodulce.com/6-bombones-chocolates-personalizados · https://regalochocolate.com/producto/caja-con-36-bombones-personalizados/ |

| id | Lectura para el modelo de negocio |
|---|---|
| **CHS-55** | **El B2B corporativo tiene dos reglas operativas verificadas que cambian la planificación de un obrador:** (1) **plazo de entrega de 14-16 días desde la aprobación de la muestra virtual**; (2) **mínimos de fabricación de 10 a 25 cajas, con plazos de 20-30 días**. Y «la Navidad es la época por excelencia» de este canal. Traducido: **el pedido corporativo de Navidad se cierra en octubre**, no en diciembre. Eso es una línea del calendario operativo de la guía, y es la clase de dato que el que abre no sabe. Fuentes: los proveedores de la tabla, consultados 2026-09-12. Fiabilidad **MEDIA** |

### 5.7 Vida útil de los rellenos (CHS-56)

| id | Dato | Fuente | Fiabilidad |
|---|---|---|---|
| **CHS-56** | «Los bombones rellenos de **ganache** pueden conservarse **5 o 6 semanas si contienen sorbitol**. De lo contrario, habrá que consumirlos en un **máximo de 8 días**». La ganache lleva nata (emulsión de agua y grasa) → más agua disponible → caduca antes. Se puede **controlar la actividad de agua (aw)** para extender la vida útil | Danielle Pacheco Chocolatier — https://daniellepacheco.es/eng/los-bombones-de-chocolate-caducan/ · Scoolinary, curso de formulación de rellenos — https://www.scoolinary.com/courses/chocolate-bonbon-formulation | **MEDIA** (profesional del sector + escuela) |

> **Es el dato de negocio más infravalorado del sector, y merece su propio epígrafe:** **un factor 5 de vida útil (8 días vs 5-6 semanas) según la formulación del relleno.** Eso no es una cuestión técnica: es **la diferencia entre poder vender online, poder hacer regalo corporativo con 14-16 días de plazo (CHS-55), y poder fabricar para Navidad en noviembre** — o no poder hacer nada de eso. **La formulación del relleno es una decisión de MODELO DE NEGOCIO**, y así hay que presentarla. ⚠️ Los valores exactos de aw y el uso de sorbitol deben pasar por la lente normativa/técnica antes de publicarse.

---

## 6. Casos de éxito (CHS-57 … CHS-68)

| id | Marca | Modelo | Dato público verificado | Fuente | Lección para la guía |
|---|---|---|---|---|---|
| **CHS-57** | **Chocolates Valor** (Villajoyosa, 1881) | Industrial + **cadena propia de chocolaterías**, franquicia desde **1984** («la primera franquicia de chocolate de España») | **>220 M€ de facturación en 2025, +34 % en ventas, 8,2 M€ de beneficio neto**. **39 establecimientos**, **5 aperturas en 2025** (Madrid, Cuenca, Elche). **Nº 2 en tabletas** y líder en chocolate negro. Presencia en **>45 países**. Franquicia: **inversión desde 125.000 €, canon 24.040 €, royalty 5 %** | https://www.sweetpress.com/actualidad/chocolates-y-cacao/chocolates-valor-cierra-2025-con-mas-de-220-millones-de-euros-de-facturacion-MI19330059 (**17-dic-2025**) · https://lexpress-franchise.com/es/articulos/chocolateria-valor-franquicia-cifras-fechas/ | **El modelo integrado**: fábrica + chocolaterías de taza propias. Demuestra que (a) y (b) **pueden convivir** en una misma marca. Es el techo del sub-concepto CHS-12 |
| **CHS-58** | **Chök** (Barcelona, 2012, Fernando Madrid; Woxofkok Projects SL) | Híbrido «casual bakery + casual chocolate boutique», franquicia desde 2013 | **42 establecimientos**. **Inversión desde 100.000 €, canon 30.000 €, contrato 5 años, local mínimo 55 m²**. Expansión en Oriente Medio (Riad, Dubái) | https://www.franquiciashoy.es/franquicias/franquicias-de-panaderias-y-pastelerias/panaderias-pastelerias/chok · https://www.profesionalhoreca.com/2023/10/08/la-cadena-de-pasteleria-chok-apuesta-por-su-expansion-via-franquicia/ | **El local más pequeño de todo el research: 55 m².** Prueba que el formato chocolate-boutique cabe donde una pastelería no |
| **CHS-59** | **Cacao Sampaka** | Boutique de chocolate premium + franquicia | Tiendas en **Madrid y Barcelona**, y en **Japón (Tokio, Osaka, Kobe)**; próxima apertura en **Riad**. Franquicia: local **100-250 m²**, **población mínima 500.000 hab** y nivel económico ≥ media nacional | https://cacaosampaka.com/tiendas/ · https://www.mundofranquicia.com/franquicia/alimentacion-y-supermercados/delicatessen/cacao-sampaka/ | **El criterio de ubicación más exigente medido: 500.000 habitantes.** Es el contraargumento a «abro una chocolatería premium en mi pueblo». Facturación **no verificada** (L-10) |
| **CHS-60** | **Casa Cacao** (Girona — Jordi Roca y Anna Payet) | **Bean-to-bar + café + tienda + hotel de 15 habitaciones** | Edificio de **4 plantas de los años 40** (la antigua **La Gerundense**, primera fábrica de papel continuo de Cataluña), **adquirido en 2016**. Obrador **visible desde la calle**. Cacao comprado a pequeñas comunidades de **Perú, Venezuela, Colombia y Ecuador** | https://diariodesign.com/interiorismo/hoteles/jordi-y-la-fabrica-de-chocolate · https://www.theworlds50best.com/stories/News/jordi-roca-chocolate-factory-casa-cacao-girona.html | **El obrador como escaparate**: producción a la vista como activo de marketing. **Inversión no publicada** (§9.2 nº 16) |
| **CHS-61** | **Kaitxo** (**Balmaseda, Bizkaia** — Las Encartaciones) | Bean-to-bar familiar + **café de especialidad** | Fundada en **2017** por **Raquel González** (catadora de chocolate) y **Mikel González** (experto en café). El nombre = **KA**fe + **TXO**colate. **Oro mundial en los International Chocolate Awards** (Florencia) con su tableta de pistacho caramelizado en chocolate blanco aromatizado. Abren el obrador al público | https://kaitxo.com/cronica-de-2023-en-kaitxo-chocolate-y-cafe/ · https://www.actualgastro.com/kaitxo-bean-to-bar-la-suma-de-kafe-y-txocolate/ · https://www.vinosycaminos.com/texto-diario/mostrar/4177933/… | **El modelo café + chocolate** como respuesta a la estacionalidad, y **el premio internacional como palanca de marca** para un obrador pequeño. ⚠️ **CORRECCIÓN AL BRIEF: está en Balmaseda, NO en Karrantza** (§9.2 nº 7) |
| **CHS-62** | **Utopick Chocolates** (Valencia, barrio de Ruzafa) | Bean-to-bar + obrador-tienda | Fundada por **Paco Llopis** (maestro chocolatero) y **Juana Rojas**. Trabaja **directamente con productores de cacao**, de la cosecha al obrador de Valencia. Exporta (presente en catálogos de EE. UU. y Australia) | https://www.visitvalencia.com/que-hacer-valencia/gastronomia/espacios-gastronomicos-valencia/utopick-chocolate-makers · https://cocoarunners.com/maker/utopick/ | **Bean-to-bar urbano exportador**: el obrador pequeño que vende fuera de España. Sin cifras públicas |
| **CHS-63** | **Pancracio** (fundada **2003 en Cádiz** por Pedro Álvarez; **comprada en 2017** por una firma valenciana del sector del lujo) | Marca de chocolate artesano + retail + online | **Facturación >2.500.000 €**, **capital social 3.217.823 €**, **35 empleados** (2026), **+51,42 %** de ingresos en el último ejercicio publicado (cuentas más recientes: 2024) | https://www.einforma.com/informacion-empresa/pancracio-chocolates · https://infonif.economia3.com/ficha-empresa/pancracio-chocolates-sa | **La trayectoria completa**: de obrador andaluz a marca comprada por un grupo de lujo. Fiabilidad **MEDIA** (Registro Mercantil vía agregador) |
| **CHS-64** | **Enric Rovira** (Barcelona / **Castellbell i el Vilar**) | Chocolate de autor con diseño | **Enric Rovira, S.L. fundada en 1993** con Francesc Forrellat. Obrador al pie de Montserrat. Caso estudiado en Harvard | https://www.enricrovira.com/en/history/ · https://www.viaempresa.cat/es/empresa/enric-rovira-el-chocolate-que-se-estudia-en-harvard_10505_102.html | **El diseño como diferencial** (sus «rajolas» inspiradas en el Eixample). Demuestra que el producto puede ser el mismo y el envase, el negocio |
| **CHS-65** | **Simón Coll** (Sant Sadurní d'Anoia, **1840**) + **Amatller** (**1797**) | Fabricante histórico, **bean-to-bar desde 1840** | Simón Coll **adquirió Amatller en 1972** — «la marca de chocolate más antigua de Europa». Tienen espacio visitable (Espai Xocolata) | https://www.simoncoll.com/es/sobre-simon-coll/historia | **El bean-to-bar no es una moda de 2015**: en España lleva desde 1840. Argumento de posicionamiento |
| **CHS-66** | **Bombonería Pons** (Sants, Barcelona, **1960**) | Obrador familiar de barrio, 3 generaciones | **2 tiendas** (Olzinelles 78 y Nau de Santa Maria 3). Crece por **venta online, más tiendas físicas, venta al por mayor y exportación**. Fabrica bombones, turrones y **monas de Pascua** | https://bomboneriapons.com/en/pages/history-bomboneria-pons | **El caso más parecido al lector objetivo**: obrador familiar de barrio que escala por canales, no por franquicia. **Y confirma las monas como pico estacional** |
| **CHS-67** | **Chocolatería San Ginés** (Madrid, **1894**) | Chocolate a la taza y churros (CHS-07) | **Abierta 24 h, 365 días.** **No acepta reservas**: ticket en caja al entrar, se entrega al camarero al sentarse. Ha ido **anexando locales contiguos** para absorber la afluencia | https://chocolateriasangines.com/chocolateria-san-gines/ · https://www.esmadrid.com/en/nightlife/chocolateria-de-san-gines | **La referencia absoluta de CHS-07** y una lección de operaciones: el **prepago en caja** como solución de rotación. Sin cifras públicas (L-10) |
| **CHS-68** | **Oriol Balaguer** / **Moulin Chocolat** | Pastelería-chocolatería de autor → cadena | Proyección de **Balaguer Coffee & Bakery: 1,5 M€ (2026) → 4 M€ (2027) → 8 M€ (2028)**, con **35 tiendas en tres años**. **Moulin Chocolat la fundó Ricardo Vélez en 2006**; **hoy es de Balaguer**, que mantuvo la decoración original y las recetas clásicas | https://www.elcorreogallego.es/economia/2026/06/01/pastelero-oriol-balaguer-abre-madrid-cafeteria-coffe-bakery-cadena-130906172.html (**1-jun-2026**) · https://www.timeout.com/madrid/shopping/moulin-chocolat | **Adquirir un obrador con marca** en vez de crearlo. ⚠️ **CORRECCIÓN AL BRIEF: Moulin Chocolat ya no es «de Ricardo Vélez»** (§9.2 nº 8) |

### 6.4 Un activo que la guía debe nombrar: la Asociación Chocolate Bean to Bar España

**45 miembros** según EFE (12-sep-2026); el listado público permite identificar **~41**: **27 makers**, **8 importadores/proveedores de cacao** y **6 museos y espacios**. Entre los makers, por comunidades: Utopick y Caūma (Valencia), Kaitxo y Lurka (País Vasco), Kina y Chocoacom (Barcelona), Casa Cacao (Girona), Origen (Lleida), Maüa (Mallorca), Relieve (Tenerife), Puchero (Valladolid), Ignacio Guerras (Madrid), Chocolates Artesanos Isabel (Teruel), Maychoco (Málaga), Chocolate Moro (Extremadura), Pangea, Rafa Gorrotxategi.
— https://www.chocolatebeantobar.com/asociados/ (consultado 2026-09-12) · el nº 45: https://www.infobae.com/espana/agencias/2026/09/12/…

⚠️ **Discrepancia declarada:** 45 (EFE) vs ~41 (recuento del listado). Puede deberse a altas recientes o a miembros no listados. **Publicar «más de 40», no una cifra exacta.**

---

## 7. Salarios y personal (CHS-69 … CHS-70)

| id | Puesto | €/hora | €/mes | Fuente | Fiabilidad |
|---|---|---|---|---|---|
| **CHS-69a** | **Chocolatero / bombonero especializado** | **13-16 €** | **105-130 €/día** | Insertia — https://www.insertia.net/blog/cuanto-cobra-un-pastelero-en-espana-sueldo-por-hora-dia-y-mes-segun-convenio-de-pasteleria | **MEDIA-BAJA** |
| **CHS-69b** | Oficial de primera | 11-13 € | 1.500-1.900 € | misma URL | **MEDIA-BAJA** |
| **CHS-69c** | Auxiliar / ayudante | 8-9,50 € | 1.300-1.550 € | misma URL | **MEDIA-BAJA** |
| **CHS-69d** | Encargado / maestro | 15-20 € | 2.000-2.800 € | misma URL | **MEDIA-BAJA** |

⚠️ **Tres avisos serios sobre este bloque:**
1. **No son ofertas reales.** InfoJobs devolvió **HTTP 456** y Glassdoor no se pudo leer (L-5). El encargo pedía ofertas con URL y **no se pudieron obtener**.
2. La fuente es un **agregador que mezcla convenios de distintas provincias y años** (cita el convenio provincial de Sevilla con una subida del 9,95 %, el **ALEH VI de marzo de 2023** y el **IV Convenio de Panadería y Pastelería de la Comunitat Valenciana de 2022**) **con plataformas de salarios** (Jooble, Indeed, Tusalario). **No es una tabla de convenio.**
3. ⚠️ **El chocolatero es la categoría mejor pagada del obrador después del maestro** (13-16 €/h frente a 11-13 € del oficial de primera). Si se confirma, es un dato de negocio de primer orden para el capítulo de personal: **el cuello de botella de una chocolatería no es la máquina, es encontrar a quien la maneje**. Pero **hay que confirmarlo**, porque procede de un agregador.

> **La tabla salarial de convenio la debe dar la lente normativa (L3)**, no ésta. Aquí queda declarado como salario **de mercado orientativo**.

| id | Dato de plantilla | Fuente |
|---|---|---|
| **CHS-70** | **1-2 empleados** en el escenario de chocolatería de tamaño medio (60-100 m²), con **2.000-3.000 €/mes** de coste salarial total | plandenegocio.es (CHS-40) — **MEDIA-BAJA** |

---

## 8. Propuesta de entregables (no es contenido de producto: es el alcance)

Reutilizando el molde de `guia-pasteleria-obrador` (8 libros de Excel + guía + bonus + business plan):

| # | Libro xlsx propuesto | Qué resuelve, con el dato de este research |
|---|---|---|
| 1 | **Capacidad de obrador y ficha de visita al local** | Cruza kg/semana → máquina (§4.1, factor 14 entre Minitemper y Top EX). **Ficha de visita específica de chocolate**: sin salida de humos (§1.2), pero **con** clima y HR (§4.4) y **con** el rango +14/+17 °C de la vitrina (§4.3) |
| 2 | **CAPEX por escenarios: traspaso vs obra nueva** | Escenarios A/B de §4.6 (24.105 € / 5.740 €) como líneas verificadas, más las **12 partidas «sin fuente»** en celda verde. Columna de traspaso alimentada por §3.6 (26.000-210.000 €) |
| 3 | **Estacionalidad, picos y tesorería** | Navidad / San Valentín / Halloween (CHS-34), monas (CHS-66), **valle de verano**, y el **cierre del pedido corporativo en octubre** (CHS-55). Curva **editable**, supuesto explícito — no hay dato público (§3.5) |
| 4 | **Carta de apertura y escandallo** | Cobertura en **celda verde** (§3.1: 25 €/kg vs 37 €/kg, factor 1,5) + **escalera de precio por formato** (§3.2: −23 % del estuche de 12 al de 35) + hoja de sensibilidad al precio del cacao (§2.4) |
| 5 | **Plan financiero a 3 años (P&L + tesorería 12 meses)** | Con **talleres/catas como línea propia** (§3.3) y el **chocolate a la taza como palanca de ticket** (+40/+60 %, §3.4) |
| 6 | **Checklist legal y licencias con Gantt** | Lo llena L3. Este research aporta: **EUDR con dos fechas según tamaño** (§2.6), **cadmio** (§2.7), **RD 1055/2003** (§2.7) |
| 7 | **Checklist de equipamiento y proveedores** | §4 y §5 completos, **con la columna de base de IVA** |
| 8 | **Turnos y coste de personal** | §7, con la advertencia de fiabilidad |

**Bonus propuesto** (equivalente a «12 decisiones de apertura»): las decisiones que este research ha dejado planteadas y cuantificadas — **artesana o de taza** (§1.3) · **traspaso o de cero** (CHS-39) · **Minitemper o Selmi** (§4.6) · **Callebaut o Valrhona** (§3.1) · **bean-to-bar sí o no, con el EUDR delante** (§2.6) · **ganache de 8 días o de 6 semanas** (§5.7) · **cómo se rellena agosto** (CHS-09/CHS-11).

---

## 9. Cierre

### 9.1 Tabla CHS-* — las cifras que ENTRAN

| id | Cifra | Fiabilidad |
|---|---|---|
| CHS-13 / CHS-14 | 3.237 empresas CNAE 108 y 91.188 CNAE 472 (1-ene-2020, INE DIRCE) | **ALTA** (pero agregadas: contexto, no «chocolaterías») |
| CHS-16 / CHS-17 | 976 empresas CNAE 1082 · 13.167 empresas CNAE 4724 (2024, eInforma) | MEDIA |
| CHS-18 | 2.323 M€ de consumo (+10,3 %) · 2.146 M€ de facturación (+12,3 %) · 858 M€ export · 1.034 M€ import · 6.994 empleos (2025, Produlce) | **ALTA** |
| CHS-19 | Tabletas 31,3 % · taza/soluble 23,0 % · snacks 19,0 % · **bombones 13,6 %** · cremas 13,1 % | **ALTA** |
| CHS-20 | Sector del dulce 8.110 M€ (+4,5 %), 2025 | **ALTA** |
| CHS-21 | 2,96 kg/persona (mar-2025), desde 3,54 kg (2022) · 10,11 €/kg (+11,3 %) | MEDIA-ALTA |
| CHS-22 | Gasto per cápita 33,88 € · volumen −6,4 % · precios +18 % (2025, MAPA) | MEDIA-ALTA |
| CHS-23 | +17,7 % de precio en 2025 tras +10 % en 2024 = **~30 % acumulado** | MEDIA |
| CHS-24a/b | Cacao: **>10.800 €/t** (máx. ene-2025) → **4.956 €/t** (2-ene-2026) → **5.938 US$/t** (12-sep-2026) | MEDIA-ALTA |
| CHS-26 | EUDR: **30-dic-2026** medianas y grandes · **30-jun-2027** micro y pequeñas | MEDIA-ALTA |
| CHS-28a | Cobertura Callebaut 811, bloque 5 kg: **125,08 € CON IVA = 25,02 €/kg** | MEDIA |
| CHS-28c | Valrhona pepitas 400 g: 14,99 € = **37,48 €/kg** | MEDIA |
| CHS-29 | Bombón artesano al público: **1,67 € (12 uds) · 1,40 € (20) · 1,29 € (35)** | MEDIA |
| CHS-30 | Talleres y catas: **25-45 €/persona**, mín. 6 pax | MEDIA |
| CHS-31/32/33 | Churro: margen bruto **85-90 %** · ración 2,50 € → **3,50-4 € con chocolate** · MP+aceite ≈ 20 % de ventas | MEDIA |
| CHS-34 | San Valentín **duplica** la media; hasta el **10 % de la venta anual** en un evento | MEDIA-ALTA |
| CHS-37/38 | Traspasos reales: **26.000-210.000 €**, **74-400 m²**, renta **910-2.200 €/mes** | MEDIA-ALTA (como mercado) |
| CHS-41 | Atemperadoras: **1.960 € (Minitemper 3 kg) → 8.500 € (Selmi One 12 kg) → 27.500 € (Top EX 60 kg)** | MEDIA (base de IVA no declarada) |
| CHS-43 | Vitrina de chocolate **+14/+17 °C**: **2.684,99 € SIN IVA** | **ALTA** (base declarada) |
| CHS-44 | Obrador **18-22 °C**, **HR <55 %** | MEDIA |
| CHS-46 | Chocolateras Ugolini **527-748 € SIN IVA**; Campeona **833-2.159 € SIN IVA** | **ALTA** (base declarada) |
| CHS-47a/b | Núcleo de máquina verificado: **24.104,99 €** / **5.740,29 €** | MEDIA (base mixta, declarado) |
| CHS-55 | B2B corporativo: **14-16 días de plazo**, mínimos de **10-25 cajas**, **20-30 días** | MEDIA |
| CHS-56 | Ganache: **8 días** sin sorbitol vs **5-6 semanas** con él | MEDIA |
| CHS-57 | Valor: **>220 M€ (2025), +34 %, 8,2 M€ de BN, 39 establecimientos** | MEDIA-ALTA |
| CHS-58 | Chök: **42 establecimientos, desde 100.000 €, canon 30.000 €, local mín. 55 m²** | MEDIA-ALTA |
| CHS-69 | Chocolatero **13-16 €/h**; encargado **15-20 €/h** | **MEDIA-BAJA** |

### 9.2 🚫 LISTA NEGRA — cifras que circulan y NO deben entrar

| # | Cifra rechazada | Por qué |
|---|---|---|
| 1 | **Cacao a 3.000-4.500 US$/t en 2026** (eldiario.ec, extra.ec, latercera.com) | Contradice a la ICCO vía FoodRetail (**4.956 €/t** el 2-ene-2026) y a EFE (**5.938 US$/t** el 12-sep-2026). Probable confusión con precio de finca latinoamericano |
| 2 | **«Facturación agregada CNAE 1082 = 16.817.176 €»** (eInforma) | Incoherente: con 976 empresas, o es la **media por empresa** (→ 16.400 M€ de sector, absurdo frente a los 2.146 M€ de Produlce) o es un total imposible. **Dato ambiguo: fuera** |
| 3 | **«Facturación total del sector CNAE 4724 = 830,68 M€»** (eInforma) | Incoherente con su propia media: 13.167 × 830.681 € = **10.937 M€**, no 830,68 M€. Solo entra la **media** |
| 4 | **Consumo per cápita «3,03 kg»** | No verificado en página. El dato leído es **2,96 kg** (TAM mar-2025) |
| 5 | **Inversión de la franquicia Valor «desde 150.000 €»** | No verificada en página. La verificada es **125.000 €** |
| 6 | **Valor: «contrato de 10 años», «3 locales propios y 29 franquiciados», «facturación por local 250.000-500.000 €»** | Solo en resumen de buscador. Además, 3+29=32 **no cuadra** con los 39 establecimientos verificados |
| 7 | **Kaitxo «en Karrantza»** (viene del brief) | Las fuentes dicen **Balmaseda, Las Encartaciones (Bizkaia)** |
| 8 | **«Moulin Chocolat, de Ricardo Vélez»** (viene del brief) | Vélez **la fundó en 2006**; **hoy es de Oriol Balaguer** |
| 9 | **«El sector del dulce factura 7.500 M€»** | Es de **2023**. La cifra vigente es **8.110 M€ (2025)** |
| 10 | **Lluc Crusellas: tableta Dubái a «casi 14 €», su más vendida** | Solo en resumen de buscador; no verificado en página |
| 11 | **Interpretar los precios de Utilcentre como «con IVA»** | La web **no lo declara**. Único indicio: «1045 €/**Neto**» en los extras, que apunta a lo contrario |
| 12 | **Selmi One a «7.400 € + IVA»** (Chocosolutions) | Tienda **mexicana** (tel. +52), con importación aparte. No es precio del mercado español |
| 13 | **Valrhona Guanaja 35,50 € · Ivoire 39,95 € · Jivara 39,95 € · Dulcey 41,95 €** como €/kg | **La página no publica el formato.** Dividir sería inventar |
| 14 | **Serie de precios Campeona tal cual** | No es monótona: TXM/9 (1.015,75 €) < TXM/7 (1.300,50 €) y TXM/20 (1.500,25 €) < TXM/14 (1.521,50 €) |
| 15 | **«Carnet de manipulador de alimentos» como requisito de apertura** (plandenegocio.es, 14-abr-2026) | **Error clásico**: el carnet como documento oficial fue derogado. Es formación acreditada por la empresa. **Confirmar con L3** |
| 16 | **Cualquier cifra de inversión de Casa Cacao** | No hay dato publicado |
| 17 | **Climatizador evaporativo «desde 365 €» para el obrador** | Un evaporativo **añade humedad**: es lo contrario de lo que necesita el chocolate |
| 18 | **Valores numéricos del RD 1055/2003 y de los límites de cadmio** | Verificada la existencia de las normas, **no los valores** (L-4) → los da L3 |
| 19 | **Cualquier «número de chocolaterías en España»** | **No existe** dato oficial (§2.1) |

### 9.3 Las 5 cifras para la portada del producto

> ⚠️ **Aviso capital.** Solo **dos** de las cinco tienen respaldo sólido. Las otras tres las publicaría **con el rango completo y la fuente al lado**, nunca como promesa. Y **ninguna** debe escribirse como «rentabilidad esperada».

| # | Cifra | Valor propuesto | Respaldo |
|---|---|---|---|
| **1. Inversión tipo** | **Desde ~5.700 € (arranque mínimo) hasta ~24.100 € solo en maquinaria de chocolate** — y **20.000-80.000 €** de apertura completa según la única fuente publicada | CHS-47a/b (**verificado línea a línea**) + CHS-03 | 🟡 **La parte de maquinaria es sólida y propia; la de apertura completa es de una sola fuente MEDIA.** Publicar **las dos**, y decir que el rango publicado «20.000-30.000 €» esconde dos negocios distintos |
| **2. m²** | **60-100 m²** (fuente publicada) · **74-118 m²** (traspasos reales de chocolatería) · **55 m²** (mínimo de la franquicia Chök) | CHS-03, CHS-37, CHS-58 | 🟢 **Sólida: tres fuentes independientes convergen en 55-120 m²** |
| **3. Personal** | **1-2 personas** para 60-100 m², con **2.000-3.000 €/mes** de coste salarial | CHS-70 + CHS-69 | 🟡 Una sola fuente MEDIA-BAJA para la plantilla |
| **4. Ticket** | **1,29-1,67 € por bombón**, **20-45 € el estuche**, **25-45 € el taller** · en variante de taza, **3,50-4 €** | CHS-29, CHS-30, CHS-32 | 🟢 **Sólida: precios públicos reales de operadores** |
| **5. Break-even** | **~89 unidades/día** con 4.000 €/mes de costes fijos y 1,50 €/ud de margen | CHS-40 | 🔴 **La más débil.** Fuente MEDIA-BAJA, del mismo dominio que comete el error del carnet, y **su ticket de 2,50 € no casa con el PVP real medido**. **Publicar como método editable, nunca como cifra** |

---

## 10. Preguntas que esta lente NO puede responder y traslada

1. **EUDR (la más importante):** ¿qué obliga exactamente a una chocolatería pequeña que compra cobertura a un proveedor de la UE (comerciante aguas abajo) frente a un bean-to-bar que importa grano (operador)? → **L3**
2. **RD 1055/2003:** porcentajes legales mínimos, límite del 5 % de grasas vegetales y **definición legal de «chocolate a la taza»** → **L3**
3. **Cadmio:** valores máximos por contenido de sólidos de cacao del Rgto. (UE) 2023/915 → **L3**
4. **Tipo de IVA aplicable al chocolate** (para convertir el 25,02 €/kg de la cobertura a base imponible) → **L3**
5. **Licencia:** ¿confirma L3 que un obrador de chocolate sin horno ni freidora evita la salida de humos y la licencia de cocina caliente? Es **el mayor argumento económico del producto** (§1.2)
6. **Convenio:** tabla salarial real del chocolatero (§7 solo tiene mercado, no convenio) → **L3**
7. **Registro sanitario:** ¿RGSEAA o comunicación autonómica según sub-concepto (CHS-01 vs CHS-02 vs CHS-03)? → **L3**
8. **Decisión de producto (§1.3):** qué se hace con la chocolatería de taza y churros → **John**
9. **Temperatura de la cámara de conservación** de producto acabado (los 16-18 °C del brief **no se verificaron**; lo verificado son los 18-22 °C de sala) → research técnico adicional
10. **Reparto mensual de ventas** de una chocolatería española: **no existe dato público** (§3.5). Se resuelve con supuesto explícito y editable, como en Pastelería
