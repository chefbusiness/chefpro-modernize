# LENTE 4 — Sector, modelo de negocio, equipamiento, proveedores y casos de éxito
## Research para el producto «Cómo Montar una Pastelería» (AI Chef Pro)

| | |
|---|---|
| **Producto** | «Cómo Montar una Pastelería» — guía premium «Cómo Montar», producto nº 48 del catálogo (hermana de `guia-panaderia-obrador`, 65 €) |
| **Lente** | L4 — Sector, modelo de negocio, equipamiento, proveedores, casos de éxito, salarios |
| **Fecha del research** | 2026-09-09 / 2026-09-10 (la sesión cruzó la medianoche; **todas las consultas web se hicieron entre el 9 y el 10 de septiembre de 2026** y esa es la fecha de consulta de cada URL salvo que se indique otra) |
| **Prefijo de ids** | `PS-` (PS = Pastelería Sector) |
| **Autor** | Subagente de research (Claude Opus 5), repo `chefpro-modernize` |
| **Naturaleza** | Research y propuesta. **No contiene contenido de producto**: ni capítulos, ni prosa vendible, ni copy de landing |

---

## 0. Método y limitaciones declaradas

### 0.1 Método

1. **Datos oficiales primero.** Se intentó siempre la fuente primaria (INE/DIRCE, MAPA, asociaciones patronales: CEOPPAN, ASEMAC, Asempas) antes de recurrir a prensa, consultoras o portales de franquicia.
2. **Descarga directa del DIRCE.** Se descargaron los CSV públicos del INE (`https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/<id>.csv`) para las tablas 298, 299 y 4721 y se filtraron por CNAE con `grep`/`awk`, en vez de fiarse de resúmenes de terceros.
3. **Precios de equipamiento con precio VISIBLE.** Solo se anotan precios que se leyeron en la ficha o el listado de un distribuidor español, con su URL. Donde el distribuidor trabaja «a presupuesto», se marca **«sin fuente (precio)»**.
4. **Evidencia de mercado por traspasos.** Se leyeron listados reales de traspaso (Milanuncios Barcelona, negociosenventa.es) porque son la mejor prueba disponible de precios de mercado, m² y rentas reales.
5. **Fiabilidad declarada por cifra.** Cada dato lleva etiqueta ALTA / MEDIA / BAJA según sea fuente primaria leída en su página, fuente secundaria leída en su página, o dato leído solo en un resumen de buscador.

### 0.2 Lo que NO se pudo verificar (y por qué)

| # | Limitación | Motivo |
|---|---|---|
| L-1 | **No hay serie DIRCE actual (2025/2026) del grupo CNAE 107 ni de la clase 1071.** La tabla `t=298` del INE, la única pública con desglose por grupos CNAE, es **histórica y se detiene en 2020** (el propio INE lo advierte). | El DIRCE público solo desglosa por divisiones/agrupaciones en las tablas vivas; el detalle por grupo dejó de publicarse en esa tabla |
| L-2 | **No se pudo usar la API JSON del INE** (`servicioswcf.ine.es`). | `curl: (6) Could not resolve host` — el DNS del sandbox no resuelve ese host. Sí resuelve `www.ine.es`, por eso se trabajó con los CSV |
| L-3 | **No hay dato oficial separado de «pastelerías»** frente a «panaderías». El CNAE mezcla las dos en 1071 (fabricación) y en 4724 (comercio minorista). | Limitación de la propia clasificación estadística. Toda cifra de «nº de pastelerías» que circule por internet es una estimación, no un dato del INE |
| L-4 | **No se obtuvo el nº de empresas de la clase CNAE 4724 desde el INE.** El dato de 12.751 empresas y 1.789 M€ de facturación procede de eInforma (Registro Mercantil), que solo cubre sociedades que depositan cuentas — deja fuera a los autónomos, que son mayoría en este sector | Fuente secundaria; se anota con fiabilidad MEDIA y advertencia |
| L-5 | **Iberinform / eInforma / Axesor devuelven ficha de pago o 403.** No se leyó la facturación exacta de Hofmann, Pastelería Mallorca ni La Duquesita | Muros de pago / bloqueo de bots |
| L-6 | **No se encontró un reparto de ventas por día de la semana** publicado y citable para pastelería en España | No existe estudio público localizable; queda como **«sin fuente»** y se propone resolverlo con un supuesto explícito y editable en el xlsx |
| L-7 | **`pasteleros.org` devolvió 403** al PDF de la escala salarial de marzo/abril 2026 | Bloqueo de bots. El dato de convenio queda para la lente normativa; aquí solo se aportan salarios de mercado |
| L-8 | **No se leyó el PDF del informe MAPA 2025 completo** (28,7 MB) | Peso del fichero y restricción térmica del Mac. Se usan las cifras que la prensa especializada atribuye explícitamente al MAPA, más la URL del PDF oficial para que el redactor las verifique en la fase de escritura |
| L-9 | **Los precios de traspaso son precio PEDIDO, no precio pagado** | Los portales publican la oferta; el cierre real suele estar por debajo. Se advierte en la tabla |
| L-10 | **Muchos «precios de referencia» de maquinaria del sector se publican sin IVA** y con descuentos de campaña que caducan | Se anota literalmente si el precio lleva IVA o no, y la fecha de consulta |

### 0.3 Regla que se aplicó a rajatabla

> **Ninguna cifra procede de la memoria del modelo.** Toda cifra de este informe tiene URL. Donde no hay URL, la fila dice **«sin fuente»** y va a la lista negra del §8.2, no a la guía.

---

## 1. Tipos y sub-conceptos del negocio (PS-01 … PS-11)

La decisión más cara que toma el lector es **qué tipo de pastelería monta**, y es la que casi ningún contenido de la SERP le plantea de forma comparada. Esta es la matriz que propongo como capítulo 1 y como primera hoja del xlsx.

### 1.1 Matriz comparada

| id | Sub-concepto | Inversión de referencia | m² | Personal de arranque | Qué cambia estructuralmente |
|---|---|---|---|---|---|
| **PS-01** | **Obrador en casa / venta directa** | **3.000–5.000 €** (mínimo viable) · **5.000–8.000 €** arranque económico; **30.000 €+** equipamiento profesional completo | Cocina separada del uso doméstico | 1 (el propio titular) | Solo **venta directa al consumidor final** (mercados, ferias, entrega a domicilio dentro de la misma unidad sanitaria); **comunicación/notificación al Departamento de Sanidad autonómico, NO RGSEAA**; alta en modelo 036/037 epígrafe **419.1** y RETA; **IVA reducido 10 %** en pastelería artesanal |
| **PS-02** | **Obrador solo producción (sin venta al público)** | **8.000–12.000 €** mínimo viable · **15.000–20.000 €** completo | — | 1–2 | Sin escaparate ni licencia de comercio; el cliente es B2B o pedido |
| **PS-03** | **Local con venta / despacho** | **15.000–25.000 €** mínimo viable · **30.000–50.000 €+** completo | — | 2–3 | Aparece la licencia de actividad comercial y el mobiliario de venta |
| **PS-04** | **Cafetería-pastelería con obrador** | **60.000–80.000 €** mínimo viable · **100.000 €+** completo | — | 3–5 | Añade barra, cafetera, aseos de público, y sube mucho el ticket medio |
| **PS-05** | **Pastelería mediana (obrador + tienda), escenario de consultoría** | **100.000–150.000 €** | ~90 m² en el escenario de La Hostelera | 2–5 | Es el escenario «tipo» de la mayoría de las fuentes publicadas |
| **PS-06** | **Punto caliente pequeño** | **60.000–100.000 €** | — | 1–2 | Regenera producto congelado; no fabrica |
| **PS-07** | **Local céntrico / grande** | **150.000–250.000 €** | — | 3–6 | El alquiler y la obra dominan la inversión |
| **PS-08** | **Franquicia** | **80.000–180.000 €** (rango genérico) · Granier **desde 180.000 €** (local ≥100 m²) o **10.000 €** en modelo autoempleo · Levaduramadre **99.000 €** canon incluido | Granier: **mínimo 100 m²** | — | Canon + royalty + obligación de compra a central; a cambio, obrador central y marca |
| **PS-09** | **Obrador B2B para hostelería** | «sin fuente» específica de inversión; en el caso Cientotreinta grados el 30 % de las ventas es canal restauración | 320 m² entre dos locales (caso real) | — | Producción a volumen, ventas a crédito, menos escaparate |
| **PS-10** | **Pastelería sin gluten / sin alérgenos** | «sin fuente» (inversión) | — | — | Exige **obrador separado o protocolo de línea sin gluten**; nicho en crecimiento |
| **PS-11** | **Pastelería sin salida de humos** | Ahorra el conducto de acero inoxidable, que **«puede superar los 6.000 €»** | — | — | Solo hornos **100 % eléctricos** + **campana de condensación**; obliga a desagüe en el punto del horno y a un surtido sin alimentos grasos |

**Fuentes:**
- PS-01…PS-04 y PS-11(coste evitado): Tamara Viñas, «Cómo montar un negocio de pastelería: guía 2026», **Pastelería Para Todos**, publicado **12-jul-2026** — https://pasteleriaparatodos.com/guia-montar-negocio-pasteleria/ (consultado 2026-09-10). Fiabilidad **MEDIA-ALTA** (profesional del sector con obrador propio, cifras coherentes y desglosadas).
- PS-01 (obrador en casa, requisitos y 5.000–8.000 € / 30.000 €+): Pastelería Para Todos, «Cómo Montar un Obrador de Pastelería en Casa», publicado **18-jun-2025** — https://pasteleriaparatodos.com/montar-obrador-pasteleria-casa/ (consultado 2026-09-10). Fiabilidad **MEDIA**.
- PS-05: La Hostelera, «Cuánto dinero necesito para montar un negocio de repostería o pastelería» — https://www.lahostelera.com/blog/cuanto-dinero-necesito-para-montar-un-negocio-de-reposteria-o-pasteleria/ (consultado 2026-09-10). **La página no publica fecha**; el comentario más reciente es de **22-ago-2025**. Fiabilidad **MEDIA**.
- PS-06, PS-07, PS-08(rango): Stefano Ventura, «Inversión necesaria para abrir una pastelería en España», **plandenegocio.es**, publicado **13-abr-2026** — https://plandenegocio.es/cuanto-cuesta-abrir-pasteleria/ (consultado 2026-09-10). Fiabilidad **MEDIA**.
- PS-08 (Granier): ficha oficial de la franquicia en Franquicias Hoy — https://www.franquiciashoy.es/franquicias/franquicias-de-panaderias-y-pastelerias/panaderias-pastelerias/granier (consultado 2026-09-10). Fiabilidad **MEDIA-ALTA** (datos declarados por la enseña).
- PS-08 (Levaduramadre): Emprendedores / Food Retail — https://www.foodretail.es/retailers/levaduramadre-rozo-los-50-millones-de-facturacion-en-2025-el-16-mas-y-abrio-31-locales.html (consultado 2026-09-10). Fiabilidad **MEDIA**.
- PS-09: Guía Repsol, «Cientotreinta grados», publicado **25-ene-2024** — https://www.guiarepsol.com/es/comer/en-el-mercado/nuevo-obrador-pan-pasteleria-cientotreinta-grados-madrid/ (consultado 2026-09-10). Fiabilidad **MEDIA-ALTA** (reportaje con datos de los propietarios).
- PS-11: Salva Industrial, «Montar una panadería y pastelería sin salida de humos» — https://www.salva.es/es/blog/montar-una-panaderia-y-pasteleria-sin-salida-de-humos (consultado 2026-09-10; **la página no lleva fecha**). Fiabilidad **MEDIA** (fabricante, con interés comercial en la respuesta).

### 1.2 Sub-conceptos que la SERP pide y las fuentes NO cubren

Estos **no tienen cifra publicada** y deben ir a la guía como marco de decisión, **no como número**:

- **Cake design / tartas por encargo**: hay decenas de negocios activos (cakedesigns.es, bettyscakesmadrid.com, teresamuntane.com, auxaitartas.com, cakeryrocks.com, saltincake.es), pero **ninguna cifra de inversión, ticket ni facturación publicada** → **«sin fuente»**.
- **Heladería-pastelería**: no se localizó ningún dato de inversión o margen específico del formato mixto → **«sin fuente»**.
- **Pastelería-panadería** (formato combinado): se cubre indirectamente vía Granier y Levaduramadre.
- **Online / delivery puro**: la SERP lo pide («vender repostería desde casa España», «ayudatpymes.com online desde casa») pero **no hay cifras** → **«sin fuente»**.

> **Propuesta de entregable:** hoja `01_Modelo` del xlsx con estas 11 filas, columnas *Inversión mín / Inversión máx / m² / Personal / Requisito diferencial*, y **celda verde de parámetro** para que el lector elija su modelo y arrastre el resto del libro.

---

## 2. El sector (PS-12 … PS-27)

### 2.1 Cuántos hay: el dato que nadie tiene limpio

| id | Cifra | Fuente | Fecha del dato | Fiabilidad |
|---|---|---|---|---|
| **PS-12** | **11.778 empresas** en el grupo CNAE **107** (Fabricación de productos de panadería y pastas alimenticias), a 1-ene-**2020**. Serie: 2013 = 10.549 · 2014 = 10.247 · 2015 = 10.117 · 2016 = 10.009 · 2017 = 10.539 · 2018 = 11.788 · 2019 = 11.745 · **2020 = 11.778** | INE, DIRCE, tabla **298** «Empresas por CCAA, actividad principal (grupos CNAE 2009) y estrato de asalariados (antigua estratificación)», CSV descargado de https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/298.csv (tabla en https://www.ine.es/jaxiT3/Tabla.htm?t=298) | 1-ene-2020 | **ALTA** (dato oficial) pero **CADUCA**: la tabla es histórica |
| **PS-13** | **91.188 empresas** en el grupo CNAE **472** (Comercio al por menor de productos alimenticios, bebidas y tabaco en establecimientos especializados), 2020; serie descendente desde 104.262 en 2013 | Misma tabla INE 298 | 1-ene-2020 | **ALTA** pero el grupo 472 es **demasiado ancho** (incluye carnicerías, fruterías, pescaderías…) — **no sirve para dimensionar pastelerías** |
| **PS-14** | **3.310.824 empresas activas** en España a 1-ene-**2025** (total nacional) | INE, DIRCE, tabla **4721** (CSV) — https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/4721.csv · nota de prensa https://www.ine.es/dyngs/Prensa/DIRCE2025.htm | 1-ene-2025 | **ALTA** (contexto, no sectorial) |
| **PS-15** | **12.751 empresas** y **1.789.002.394 €** de facturación en la clase CNAE **4724** (comercio al por menor de pan, panadería, confitería y pastelería en establecimientos especializados) | eInforma — https://www.einforma.com/informes-sectoriales/cnae-4724-empresas-comercio-al-por-menor-de-pan-y-productos-de-panaderia-confiteria-y-pasteleria-en-establecimientos-especializados (consultado 2026-09-10) | Sin año declarado en el snippet | **MEDIA-BAJA**. Es Registro Mercantil: **solo sociedades que depositan cuentas**. Los autónomos, que son la mayoría del sector, no cuentan. **Usar solo como orden de magnitud, nunca como censo** |
| **PS-16** | **11.000–11.500 panaderías artesanas con obrador propio** en España | CEOPPAN citado por Qué Franquicia, «Situación del sector de las panaderías en España en 2026» — https://quefranquicia.com/situacion-del-sector-de-las-panaderias-en-2026/ y L'Express Franchise — https://lexpress-franchise.com/es/articulos/situacion-sector-panaderias-espana/ (consultados 2026-09-10) | 2026 (publicación) | **MEDIA** (secundaria; cita a CEOPPAN pero no enlaza al informe) |
| **PS-17** | **600–700 hornos rurales cierran cada año** por falta de relevo generacional | Mismas fuentes que PS-16, atribuido a estimaciones de 2023 | 2023 | **MEDIA-BAJA** |

> ⚠️ **Aviso de censo.** No existe un dato oficial de «cuántas pastelerías hay en España». El CNAE mezcla panadería y pastelería en los dos códigos relevantes. **La guía debe decirlo explícitamente** en vez de repetir una cifra redonda. Ver lista negra §8.2.

### 2.2 CEOPPAN — la foto del oficio (datos 2020)

| id | Cifra | Valor |
|---|---|---|
| **PS-18** | Trabajadores del sector | **336.000** |
| **PS-19** | Fabricantes | **15.000** |
| **PS-20** | Puntos de venta | **45.000** |
| **PS-21** | Consumo de pan | **35,64 kg/persona/año** (32,78 en hogar + 2,86 fuera) |
| **PS-22** | Facturación | **3.614 M€** doméstica + **400 M€** extradoméstica = **4.014 M€** |
| **PS-23** | Precio medio del pan | **2,43 €/kg** |
| **PS-24** | Reparto producción | Tradicional **50 %** · Industrial **40 %** |
| **PS-25** | Canal | Super/autoservicio **39,7 %** · Tienda tradicional **34,8 %** · Hiper **7 %** · Online **0,5 %** |

**Fuente:** CEOPPAN, «Informe 2021: la panadería tradicional y artesana española» (datos referidos a **2020**) — https://www.ceoppan.es/datosdelsectordelpan/la-panaderia-tradicional-y-artesana-espanola (consultado 2026-09-10). Fiabilidad **ALTA** para 2020 (patronal), pero **son datos de PAN, no de pastelería**, y tienen **6 años**. En la guía deben ir etiquetados como tales.

### 2.3 ASEMAC — la industria de masas congeladas (competencia directa del obrador)

| id | Magnitud 2025 | Valor | Variación |
|---|---|---|---|
| **PS-26a** | Producción total de masas congeladas | **980.876 t** | **−0,65 %** |
| **PS-26b** | Pan | **747.153 t** | **−0,89 %** |
| **PS-26c** | **Bollería y pastelería** | **233.856 t** | **+0,17 %** |
| **PS-26d** | Facturación del sector | **2.001,63 M€** | **+3,20 %** (primera vez por encima de 2.000 M€) |
| **PS-26e** | Facturación pan | — | **+2,30 %** |
| **PS-26f** | **Facturación bollería y pastelería** | — | **+4,43 %** |
| **PS-26g** | Serie 2018-2025: producción | — | **+1,17 %** |
| **PS-26h** | Serie 2018-2025: facturación | — | **+47,46 %** |
| **PS-26i** | Serie 2018-2025: producción de pastelería | — | **+31,10 %** |
| **PS-26j** | Consumo de pan en hogares 2025 | Penetración **~97 %** | Volumen **+1,4 %**, valor **+3,2 %** |

**Fuente:** ASEMAC, «La industria de panadería y bollería supera los 2.000 millones de euros y consolida su estabilidad en 2025», publicado **28-abr-2026** — https://www.asemac.es/noticias-asemac/52-la-industria-de-panaderia-y-bolleria-supera-los-2-000-millones-de-euros-y-consolida-su-estabilidad-en-2025 (consultado 2026-09-10). Fiabilidad **ALTA** (nota de la propia patronal). Réplica en prensa: https://www.retailactual.com/noticias/20260428/industria-panaderia-bolleria-datos-produccion-asemac y https://www.revistaaral.com/texto-diario/mostrar/5861136/industria-panaderia-bolleria-supera-2000-millones-euros-2025-32

| id | Cifra | Valor | Fuente | Fiabilidad |
|---|---|---|---|---|
| **PS-27** | ASEMAC agrupa al **80 % de las empresas** y **~90 % de las ventas** del sector de masas congeladas; **~5.000 empleos directos** | — | Leído en resumen de búsqueda sobre asemac.es y prensa sectorial; **no verificado en la página** | **BAJA** — verificar antes de publicar |

> **Lectura para la guía (no es contenido, es el ángulo):** la bollería y pastelería **congelada** creció un **31,1 % en producción entre 2018 y 2025** y su facturación sube más rápido que la del pan. Ese es el competidor real del obrador de barrio, y explica por qué el punto caliente (PS-06) existe como modelo de negocio.

### 2.4 Consumo en hogares — Panel del MAPA 2025

| id | Categoría | Volumen | Gasto | kg/persona/año | Precio medio | Variación |
|---|---|---|---|---|---|---|
| **PS-28** | **Bollería y pastelería** | **274,2 millones de kg** | **1.917,6 M€** | **5,85 kg** | «sin fuente» (no publicado en las fuentes leídas) | Volumen **+5,3 %** · Valor **+5,6 %** |
| **PS-29** | Bollería y pastelería por renta | — | — | Renta **baja 8,26 kg** vs renta **alta 4,39 kg** (casi el doble) | — | — |
| **PS-30** | **Galletas** | — | — | «sin fuente» | **4,95 €/kg** | Volumen **−3,5 %** · Valor **−0,5 %** |
| **PS-31** | **Chocolates, cacaos y derivados** | — | — | **2,84 kg** (**33,88 €/persona**) | **11,93 €/kg** | Volumen **−6,5 %** · Valor **+10,4 %** |
| **PS-32** | **Productos navideños** | — | — | «sin fuente» | **12,62 €/kg** | Volumen **+1,1 %** · Valor **+6,9 %** |

**Fuentes:**
- Informe oficial: MAPA, **Informe del Consumo Alimentario en España 2025**, publicado **30-jul-2026** — PDF en línea: https://www.mapa.gob.es/es/dam/jcr:021c103a-f584-4d44-bebf-e1b44344ab11/Informe%20comsumo%202025_en%20l%C3%ADnea_.2026-07-30-11-08-13.pdf · índice: https://www.mapa.gob.es/es/alimentacion/temas/consumo-tendencias/panel-de-consumo-alimentario/ultimos-datos (consultado 2026-09-10). **No se abrió el PDF (28,7 MB, restricción térmica).**
- PS-28 y PS-29 leídos en: El Independiente, **17-ago-2026** — https://www.elindependiente.com/sociedad/consumo/2026/08/17/los-hogares-de-rentas-bajas-comen-el-doble-de-bolleria-industrial-que-las-familias-con-mayor-poder-adquisitivo/ (consultado 2026-09-10, página leída). Fiabilidad **ALTA-MEDIA**.
- PS-28 (variaciones), PS-30, PS-31, PS-32 leídos en: Sweetpress, «El consumo alimentario frena su descenso en 2025 y el gasto se eleva un 3,4 %», **30-jul-2026** — https://www.sweetpress.com/actualidad/el-consumo-alimentario-frena-su-descenso-en-2025-y-el-gasto-se-eleva-un-34-MC20554338 (consultado 2026-09-10, página leída). Fiabilidad **ALTA-MEDIA**.

> ⚠️ **Contradicción menor a resolver antes de publicar:** El Independiente dice **274,2** millones de kg; el resumen del buscador sobre la misma noticia daba **274,3**. Diferencia irrelevante para el negocio, pero **la guía debe citar una sola cifra** — usar **274,2**, que es la que se leyó en la página.

### 2.5 Canal de venta

| id | Cifra | Valor | Fuente | Fiabilidad |
|---|---|---|---|---|
| **PS-33** | ~**74 %** de las ventas de bollería, pastelería, galletas y cereales en España se hicieron en **supermercado** (2023); hiper **15,2 %**; otras formas **5,4 %**; **comercio especializado 5,4 %** | Statista — https://es.statista.com/estadisticas/501706/cuota-de-mercado-en-la-comercializacion-de-bolleria-y-pasteleria-en-espana (leído en resumen de búsqueda, **muro de pago**) | 2023 | **BAJA-MEDIA** |
| **PS-34** | **68,2 %** super · **12,5 %** hiper · **10,6 %** tienda tradicional | Reparto del **total de la compra alimentaria** en 2025, **NO de bollería** | 2025 | ⚠️ **NO USAR como dato de pastelería** — riesgo de error de atribución. Ver lista negra |

> **Lectura:** solo ~**1 de cada 20 euros** de bollería y pastelería pasa por el comercio especializado. El obrador **no compite en volumen con el supermercado y no debe intentarlo**: compite en producto fresco, encargo y temporada. Es la tesis de negocio de la guía.

### 2.6 Estacionalidad — la única palanca de caja que sí tiene cifras

| id | Campaña | Cifra | Fuente | Fiabilidad |
|---|---|---|---|---|
| **PS-35** | **Roscón de Reyes**: ~**30 millones de unidades** en la campaña de Navidad 2025/26, en línea con la anterior | Estimación de **ASEMAC**, vía Infobae/EFE, **2-ene-2026** — https://www.infobae.com/america/agencias/2026/01/02/los-espanoles-consumiran-alrededor-de-30-millones-de-roscones-de-reyes-esta-navidad/ | 2026 | **MEDIA-ALTA** |
| **PS-36** | **Comunidad de Madrid**: más de **2,9 millones** de roscones | **Asempas** (Asociación Empresarial de Pasteleros y Panaderos de Madrid), vía Libertad Digital, **2-ene-2026** — https://www.libertaddigital.com/madrid/2026-01-02/fiebre-por-el-roscon-en-madrid-casi-3-millones-de-ventas-y-preferencia-por-el-relleno-7339233/ | 2026 | **MEDIA-ALTA** |
| **PS-37** | **57 %** de los consumidores elige **roscón relleno** (nata o trufa) | Asempas, misma fuente que PS-36 | 2026 | **MEDIA** |
| **PS-38** | **El Corte Inglés**: **850.000** roscones · **Viena Capellanes**: **72.000** roscones | Infobae/EFE, 2-ene-2026 (misma URL que PS-35) | 2026 | **MEDIA** |
| **PS-39** | **Todos los Santos**: los pasteleros esperaban vender **+4 %** a un precio hasta un **3 %** mayor | Vivir Ediciones — https://vivirediciones.es/los-pasteleros-esperan-vender-un-4-mas-por-todos-los-santos-a-un-precio-hasta-un-3-mayor/ y Andalucía Información — https://andaluciainformacion.es/andalucia/1797111/los-pasteleros-esperan-vender-un-4-mas-por-todos-los-santos/ (**la página devolvió 403**, leído en resumen) | Año no confirmado | **BAJA** — verificar el año antes de usar |
| **PS-40** | **Huesos de santo 50–60 €/kg** · **Panellets 70–90 €/kg** | 7 Televalencia — https://7televalencia.com/dulces-todos-santos-valencia/ (leído en resumen de búsqueda) | Atribuido a **2024** | **BAJA-MEDIA** — precio de venta al público, útil como referencia de posicionamiento |
| **PS-41** | **Ensaimadas** (caso Pomar): 25-30/día normal → **150-200/día** en temporada alta; individuales 50-60 → **500-600**. **Turrón: 7.000-8.000 barras** en Navidad | El Español/Cocinillas, **21-nov-2025** — https://www.elespanol.com/cocinillas/reportajes-gastronomicos/20251113/matias-dueno-pasteleria-espana-montar-obrador-cuesta-eur-rentabilidad-kw/1003744012399_0.html | 2025 | **ALTA** (declaración directa del gerente) |

> **Lo que enseña PS-41 y que ninguna fuente de la SERP explica:** el pico de temporada alta multiplica la producción **por 5-10×**, no por 1,5×. Eso condiciona **el dimensionado del horno, del abatidor y de la plantilla eventual** — y es exactamente el tipo de dato que justifica un xlsx de plan de producción estacional.

### 2.7 Tendencias con evidencia

| id | Tendencia | Evidencia | Fuente |
|---|---|---|---|
| **PS-42** | **Artesano vs industrial**: la producción industrial congelada de bollería/pastelería creció **+31,1 % (2018-2025)** mientras el nº de obradores artesanos se estanca | PS-26i, PS-16, PS-17 | ASEMAC + CEOPPAN vía prensa |
| **PS-43** | **Croissant de mantequilla / bollería de autor como producto estrella**: en Hofmann, **un solo producto** (croissant de mascarpone, ~3.000 uds/semana) representa **cerca del 30 % de la facturación global** de la pastelería | The New Barcelona Post, **12-feb-2026** — https://www.thenewbarcelonapost.com/hofmann-badalona-centro-id-expansion-internacional/ | **ALTA** |
| **PS-44** | **Desestacionalización**: el roscón se empieza a vender fuera de Navidad; piezas más pequeñas; opciones sin gluten y sin lactosa | Libertad Digital, 2-ene-2026 (URL de PS-36) | **MEDIA** |
| **PS-45** | **Pastelería sin gluten**: mercado de productos sin gluten en España **+18 % entre 2022 y 2025**, previsiones positivas 2026-2028 | Eurobakeries — https://www.eurobakeries.com/el-pan-sin-gluten-en-la-hosteleria-guia-practica-para-atender-a-los-clientes-celiacos-y-sensibles-al-gluten-en-2026/ (leído en resumen; **fuente con interés comercial**) | **BAJA** |
| **PS-46** | **Supermercado como competidor de temporada**: hay roscones de supermercado premiados a **9 €** | La Ciutat — https://laciutat.cat/es/cataluna/este-es-mejor-roscon-reyes-2026-supermercado-por-solo-9-euros_881457_102.html · Directo al Paladar — https://www.directoalpaladar.com/consumidores/estos-siete-mejores-roscones-supermercado-2026-mercadona-a-lidl-corte-ingles-a-aldi | **MEDIA** |
| **PS-47** | **Obradores de barrio con crecimiento real**: Cientotreinta grados pasó de un local (2017) a obrador de **320 m²** produciendo **~600 kg/día** con capacidad para **1.200 kg** | Guía Repsol, 25-ene-2024 (URL de PS-09) | **MEDIA-ALTA** |

---

## 3. Modelo de negocio (PS-48 … PS-66)

### 3.1 Rentabilidad y márgenes — el bloque más valioso del research

| id | Métrica | Valor | Fuente | Fiabilidad |
|---|---|---|---|---|
| **PS-48** | **Rentabilidad neta de una pastelería «yendo bien»** | **8-12 %** | Matías Pomar Oliver, gerente de **Pastelerías Pomar** (4.ª generación, fundada en 1902), El Español/Cocinillas **21-nov-2025** — https://www.elespanol.com/cocinillas/reportajes-gastronomicos/20251113/matias-dueno-pasteleria-espana-montar-obrador-cuesta-eur-rentabilidad-kw/1003744012399_0.html | **ALTA** (declaración con nombre y empresa) |
| **PS-49** | **Coste de montar un obrador** | **«200.000, 300.000 y más» €** | Misma fuente | **ALTA** |
| **PS-50** | **Coste de abrir una tienda** | **100.000 €** | Misma fuente | **ALTA** |
| **PS-51** | **Margen del turrón** | **~40 %** | Misma fuente | **ALTA** |
| **PS-52** | **Punto de equilibrio por producto** | «vender **8 unidades** para empatar; la **novena** empieza a ganar» | Misma fuente | **ALTA** (ilustrativo, no extrapolable) |
| **PS-53** | **Estructura de venta** | **95 %** venta directa al cliente · **5 %** venta a crédito a 30-60 días | Misma fuente | **ALTA** |
| **PS-54** | **Plantilla** | **47 personas**, de las cuales **10 familiares** | Misma fuente | **ALTA** |
| **PS-55** | **Margen bruto objetivo en pastelería artesana** | **65-70 % sobre coste** | Tamara Viñas, Pastelería Para Todos, 12-jul-2026 (URL de PS-01) | **MEDIA-ALTA** |
| **PS-56** | **Food cost objetivo (regla de oro)** | coste de ingredientes **por debajo del 30-35 %** del PVP | Misma fuente | **MEDIA-ALTA** |
| **PS-57** | **Beneficio neto mensual de un obrador artesano unipersonal bien tarificado** | **1.200-2.500 €/mes** | Misma fuente | **MEDIA** |
| **PS-58** | **Ejemplo de break-even** | costes fijos de **5.000 €/mes** ⇒ facturación de **~7.200 €/mes** | Misma fuente | **MEDIA** |
| **PS-59** | **Packaging** | entre **5 % y 15 %** del coste total del producto en pastelería | Pleko — https://pleko.app/escandallo-pasteleria (leído en resumen de búsqueda) | **BAJA-MEDIA** |

> ⚠️ **PS-55 y PS-56 no dicen lo mismo y hay que redactarlo con cuidado.** «Margen del 65-70 %» y «food cost por debajo del 30-35 %» son **la misma restricción expresada dos veces** (65 % de margen ⇔ 35 % de food cost). Escribirlas como dos reglas distintas sería un error de contenido. **La guía debe presentarlas como una sola regla con dos lecturas**, y el xlsx debe calcular una desde la otra, nunca pedir las dos.

### 3.2 Break-even y gastos fijos (escenarios publicados)

| id | Escenario | Gastos fijos/mes | Facturación mínima/mes |
|---|---|---|---|
| **PS-60a** | Pastelería pequeña | **5.000 €** | **7.000 €** |
| **PS-60b** | Mediana | **8.000 €** | **10.000 €** |
| **PS-60c** | Grande / céntrica | **12.000 €** | **15.000 €** |

**Desglose de gastos fijos mensuales (PS-61):** alquiler **1.200-3.000 €** · suministros **600-1.200 €** · personal (2-5 empleados) **2.000-6.000 €** · seguros y gestoría **300-700 €** · marketing **200-500 €** · reposición de stock **1.000-2.000 €** → **total 5.000-12.000 €/mes**.
**ROI declarado (PS-62):** **18-36 meses**.

**Fuente PS-60/61/62:** plandenegocio.es, 13-abr-2026 (URL de PS-06). Fiabilidad **MEDIA**. ⚠️ **El propio artículo no cita fuente primaria** para estos rangos; cita a 6 blogs del sector. **Tratar como escenario editable, nunca como benchmark.**

### 3.3 Ticket medio

| id | Cifra | Valor | Fuente | Fiabilidad |
|---|---|---|---|---|
| **PS-63** | **Ticket medio de restauración en España** | **~21 €** por transacción (2024). Baleares **35 €**, Álava **16,5 €**. Turista extranjero **31,2 €** | CaixaBank Research (1S 2025, Informe Sectorial Turismo) vía Campus CaixaBankLab — https://caixabanklab-campus.com/cual-es-el-ticket-medio-restauracion-espana/ | **MEDIA-ALTA** — pero es **restauración**, no pastelería |
| **PS-64** | **Ticket medio de pastelería** | **«sin fuente»** — no existe dato público localizable | — | — |
| **PS-65** | Ejemplo de cafetería (referencia de orden de magnitud) | cafetería de **60 m²** con **10.000 €/mes** de gastos y ticket **4,50 €** necesita **80-100 clientes/día** | Qué Café — https://quecafe.info/calculadora-de-costes-cafeteria-especialidad/ (leído en resumen) | **BAJA** |

> **Decisión propuesta:** el ticket medio de pastelería va al xlsx como **parámetro en celda verde con valor por defecto declarado como supuesto**, nunca como «dato del sector». Y en la guía se explica cómo medirlo con el TPV en dos semanas. Es más honesto y más útil que un número inventado.

### 3.4 Materias primas: los dos riesgos que hay que modelar

**PS-66 — Mantequilla.**

| Dato | Valor | Fecha | Fuente |
|---|---|---|---|
| Cotización UE, 4.ª semana de junio 2026 | **386 €/100 kg** (−2,8 % en 4 semanas) | jun-2026 | Observatorio del Mercado Lácteo de la Comisión Europea, vía Campo Galego — https://www.campogalego.es/ultimas-cotizaciones-de-la-leche-y-de-los-productos-lacteos-en-los-mercados-internacionales-5/ |
| Cotización UE, 2.ª semana de junio 2026 | **405 €/100 kg** (+2,3 % en 4 semanas) | jun-2026 | Revista Vaca Pinta — https://vacapinta.com/es/mercados/nuevo-maximo-historico-de-la-mantequilla-en-europa.html |
| Máximo histórico previo | La mantequilla llegó a **duplicarse de ~4.000 a ~8.000 €/t** antes de 2026 | 2024-2025 | El Economista — https://www.eleconomista.es/mercados-cotizaciones/noticias/13215097/02/25/la-crisis-de-la-mantequilla-escasez-y-precios-disparados-en-europa-pero-espana-ni-se-inmuta.html |
| Precio de la leche en España | **52,23 €/100 kg** en feb-2026, **+10,5 %** interanual (España sube mientras la UE corrige) | feb-2026 | Agronews CyL — https://www.agronewscastillayleon.com/precio-leche-vaca-ue-feb-26/ |

Fiabilidad **MEDIA-ALTA** (fuente primaria: Milk Market Observatory de la Comisión Europea, leída a través de prensa especializada). ⚠️ **Es cotización de commodity a granel**, no el precio que paga un obrador por mantequilla de hoja 82-84 % — que es sensiblemente superior. **No mezclar los dos en la misma tabla.**

**PS-67 — Cacao.**

| Dato | Valor | Fecha | Fuente |
|---|---|---|---|
| Precio ICCO a inicios de 2026 | **~5.000 USD/t** | ene-2026 | Gestión (Perú) — https://gestion.pe/economia/cacao-precios-se-amargan-en-arranque-del-2026-y-hunden-exportaciones-que-podria-cambiar-noticia/ |
| Precio ICCO en abril 2026 | **~3.300 USD/t** | abr-2026 | Misma fuente |
| Futuros Londres/Nueva York | **~4.000 USD/t**, tendencia bajista | 2026 | Investing/EFE — https://es.investing.com/news/stock-market-news/el-precio-del-cacao-se-desploma-en-2026-por-la-menor-demanda-y-el-alza-de-las-existencias-3508623 |
| Cierre de agosto 2026 | **6.204,94 USD** (≈ 5.325,70 €/t) | ago-2026 | Leído solo en resumen de búsqueda — **CONTRADICE** a las anteriores |
| Caída desde máximos | **−54 %** en 12 meses (cacao) y **−21 %** (azúcar); los precios minoristas bajan mucho más lento | mar-2026 | Infobae, **15-mar-2026** — https://www.infobae.com/espana/2026/03/15/los-pasteleros-hacen-el-agosto-en-semana-santa-el-precio-del-cacao-y-del-azucar-se-desploma-pero-las-torrijas-y-los-huevos-de-pascua-cuestan-mas/ |

> 🚨 **CONTRADICCIÓN NO RESUELTA.** Las fuentes dan **3.300 / 4.000 / 5.000 / 6.205 USD/t** para 2026 según el mes y el mercado. **Ninguna cifra puntual de cacao debe entrar en la guía.** Lo que sí entra es el **patrón**, que está triplemente confirmado: (a) máximos históricos en 2024-2025, (b) caída fuerte en 2026, (c) **el precio minorista no baja al ritmo del commodity**. La guía debe enseñar a **modelar la volatilidad** (celda de precio de cobertura + análisis de sensibilidad), no a fijar un precio.

**PS-68 — Precios de materia prima que circulan sin fuente primaria.** Chocolate cobertura premium 18-22 €/kg · vainilla en rama 600-800 €/kg · frutos secos 15-35 €/kg · mantequilla de calidad 9-12 €/kg. Aparecen en un resumen de búsqueda atribuible a Pleko (https://pleko.app/escandallo-pasteleria). **Fiabilidad BAJA → lista negra.** Van al §8.2.

### 3.5 Evidencia de mercado: traspasos reales

Es la mejor prueba de precio de mercado disponible, y **ninguna guía de la SERP la usa**. Todos consultados el **2026-09-10**.

**PS-69 — Milanuncios, traspasos de obrador/pastelería en Barcelona** (https://www.milanuncios.com/traspasos-en-barcelona/obrador-pasteleria.htm):

| Negocio | m² | Traspaso | Renta/mes | Nota |
|---|---|---|---|---|
| Pastelería-repostería, Gràcia | **85** | **43.000 €** | **1.250 €** | Zona de paso, licencia nueva |
| Pastelería take away, Poblenou | **69** | **80.000 €** | **850 €** | Obrador abierto al público |
| Obrador Sant Antoni | **80** | **25.000 €** | **1.050 €** | Sin venta al público (catering/helados) |
| Panadería-pastelería, Pg. Maragall | **63** | **18.000 €** | **1.300 €** | Solo venta, sin degustación |
| Pastelería artesanal, Sant Andreu | **63** | **19.000 €** | **1.300 €** | Totalmente equipado |

Varios listados advierten de **2.000-3.000 € adicionales** de honorarios de gestión inmobiliaria, y citan la licencia de actividad **4724B6a**.

**PS-70 — negociosenventa.es, pastelerías en traspaso en España** (https://www.negociosenventa.es/traspaso/comercio/pasteleria):

| Negocio | Provincia | Traspaso |
|---|---|---|
| Repostería creativa | Almería | **25.000 €** |
| Pastelería-obrador | Barcelona | **50.000 €** |
| Tienda de pastelería creativa (obrador pequeño) | Madrid | **20.000 €** |
| Pastelería-obrador por jubilación | Barcelona | **75.000 €** |
| Pastelería-cafetería por jubilación (36+ años) | Lleida | **100.000 €** |
| Pastelería-panadería **sin obrador** (25+ años) | Madrid | **19.500 €** |
| Despacho de pan y bollería | Valencia | **15.500 €** |
| Pastelería operativa (Benimaclet) | Valencia | **18.000 €** |
| Pastelería | Sevilla | **6.000 €** |
| Gofres y dulces belgas (7 años) | Gran Canaria | **65.000 €** |

**PS-71 — Traspasos citados en resúmenes de búsqueda (fiabilidad BAJA, verificar):** panadería-cafetería con obrador en San Blas-Canillejas (Madrid): **50.000 €** de traspaso, **1.600 €/mes** de renta, **50 m² de tienda + 70 m² de obrador** · obrador con panadería-pastelería en Campo de las Naciones (Madrid): **95.000 €**, **200 m²** · pastelería con obrador en Barcelona: **200.000 €** incluyendo activos, know-how y cartera digital de clientes.

> **Lecturas que salen solas de PS-69/70 y que valen un capítulo:**
> 1. **Traspasar sale entre 3 y 10 veces más barato que montar de cero.** Frente a los 100.000-250.000 € de obra nueva (PS-05/PS-07/PS-49/PS-50), la mediana de estos traspasos ronda los **25.000-50.000 €** con maquinaria y licencia incluidas.
> 2. **La renta es el dato que mata el negocio, no el traspaso.** Un traspaso de 18.000 € con 1.300 €/mes de renta es peor negocio que uno de 80.000 € con 850 €/mes: en 4 años la diferencia de renta se come el ahorro del traspaso. **Ese cálculo debe ser una hoja del xlsx.**
> 3. **«Por jubilación» es la etiqueta más repetida** — coherente con la falta de relevo generacional de PS-17.
> 4. ⚠️ **Son precios PEDIDOS, no pagados.**

---

## 4. Equipamiento crítico con marcas y precios (PS-72 … PS-86)

### 4.1 Hornos — precios con IVA en un distribuidor español

**PS-72.** La Hostelera, categoría «Hornos profesionales para panadería, repostería y pastelería» — https://www.lahostelera.com/158-hornos-profesionales-para-panaderia-reposteria-y-pasteleria (consultado **2026-09-10**; **precios CON IVA** según la propia página):

| Marca | Modelo | Bandejas | Precio (IVA incl.) |
|---|---|---|---|
| UNOX | Roberta XF003 | 3 | **605,61 €** |
| UNOX | Anna XF023 | 4 | **698,78 €** |
| ROMAGSA | Maxiplus | 4 | **703,01 €** |
| FM Industrial | RXL 304 | 4 | **719,29 €** |
| SMEG | ALFA43X | 4 | **791,95 €** |
| UNOX | Domenica XF043 | 4 | **1.229,84 €** |
| UNOX | XFT183 Elena | 3 | **1.313,70 €** |
| INFRICO | HE604Plus | 4 | **1.593,21 €** |
| UNOX | Rosella XFT193 | 4 | **1.639,79 €** |
| SMEG | ALFA420E1HDS | 4 | **2.513,41 €** |
| Nerone | NEMID-5 | 5 | **2.922,15 €** |
| SMEG | ALFA625E1HDS | 6 | **2.964,50 €** |
| EKA | KF 1001 G (gas) | 4 | **3.210,13 €** |
| UNOX | XB693 Bakerlux | 6 | **3.354,12 €** |
| SMEG | ALFA1035HR-2 | 10 | **3.896,20 €** |
| UNOX | XB893 | 10 | **4.844,84 €** |
| UNOX | XEBC-06EU-E1RM | 6 | **5.450,45 €** |
| UNOX | XB813G (gas) | 10 | **6.288,98 €** |
| UNOX | XEBC-06EU-EPRM | 6 | **7.453,60 €** |
| UNOX | XEBC-10EU-GPRM (gas) | 10 | **11.275,71 €** |

Fiabilidad **ALTA** (precio visible en tienda española, leído en la página).

**PS-73 — Hornos de pisos (deck) y rotativos.** Salva Industrial fabrica hornos de pisos eléctricos modulares de **1 a 5 módulos**, con **1 o 2 puertas**, cámaras de **200 o 300 mm**, para **2, 3, 4 o 6 bandejas** de 60×40 o 76×46 cm, con variación de temperatura **<±5 ºC** — https://salva.es/es/hornos-de-panaderia/hornos-de-pisos-electricos/Horno-de-pisos-electricos-modulares (consultado 2026-09-10). **Precio: «sin fuente (precio)»** — Salva vende por distribuidor y presupuesto. Otras marcas de referencia del segmento: Bongard (https://www.bongard.es/), Wiesheu, Miwe, Sveba Dahlen.

**PS-74 — Referencia de coste de horno declarada por un profesional en activo:** «un horno profesional puede costar **más de 20.000 o 30.000 euros**», igual que un congelador profesional — Matías Pomar, El Español 21-nov-2025 (URL de PS-48). Fiabilidad **ALTA** (declaración), **MEDIA** como precio de mercado (es una horquilla hablada).

**PS-75 — Referencias de escenario de inversión:** horno profesional **15.000-35.000 €**; amasadora industrial **4.000-8.000 €**; vitrinas refrigeradas **7.000-15.000 €** — plandenegocio.es, 13-abr-2026 (URL de PS-06). Fiabilidad **MEDIA**.

### 4.2 Frío, laminación, atemperado y vitrinas

| id | Equipo | Marca/modelo | Precio | IVA | Fuente |
|---|---|---|---|---|---|
| **PS-76** | **Vitrina expositora pastelera refrigerada curva** | **Docriluc VEPD-9-15-C** (1505×900×1305 mm, 452 L, 0,93 m² de exposición, R-290) | **2.284,10 €** (PVP tachado 3.263,00 €, −30 %) | **SIN IVA** (la ficha lo declara) | Gavinox — https://gavinox.es/vitrinas-expositoras/1441-vitrina-expositora-pastelera-refrigerada-curva-vepd-9-15-c-docriluc.html (consultado 2026-09-10) |
| **PS-77** | Accesorio: puertas correderas traseras VEPD-9-15 | Docriluc | **120,40 €** | sin IVA | Misma URL |
| **PS-78** | **Abatidor de temperatura** | **Irinox**, 4 bandejas (gama Multifresh, ciclos de +85 ºC a −40 ºC) | **desde 10.037 € + IVA** | sin IVA | EquipoH — https://www.equipoh.com/blog/55_Abatidor-de-temperatura--Precios-y-opciones-para-cada-necesidad y https://www.equipoh.com/64-fabricante-irinox (leído en resumen de búsqueda) — fiabilidad **MEDIA** |
| **PS-79** | **Laminadora automática de masa** | **Sammic DF-40** (hasta 40 cm) | **1.215,00 € sin IVA / 1.470,15 € con IVA** | ambos | Alimaq — https://alimaq.com/preparacion/laminadoras/laminadora-automatica-de-masa-hasta-40-cms-df-40 (leído en resumen) — fiabilidad **MEDIA** |
| **PS-80** | **Laminadora profesional de obrador** | **RONDO** (Rondostar 5000 y gama de laminadoras) | **«sin fuente (precio)»** — venta por distribuidor (**Sermont** es distribuidor oficial en España) | — | https://www.rondo-online.com/ · https://sermont.es/productos/laminacion-corte-y-acabado/ |
| **PS-81** | **Batidora planetaria 20 L** | **Sammic BP-20** (20 L, 900 W, 95-392 rpm, temporizador 0-99 min) | **desde 595,04 €** (HostelShopping) | no declarado | https://www.hostelshopping.com/producto/batidora-amasadora-planetaria-be-20-sammic/ · Makro (403 al bot): https://www.makro.es/marketplace/product/90b8aa82-a0c4-4f39-8233-42b50e07f259 — fiabilidad **MEDIA** |
| **PS-82** | **Atemperadora de chocolate** | **Selmi One 12 kg** | **7.400,00 € + IVA** | sin IVA | Chocosolutions — https://chocosolutions.com/products/temperadora-selmi-one-12-kg (leído en resumen) · fabricante: https://www.selmi-group.com/ — fiabilidad **MEDIA** |
| **PS-83** | **Cámara de fermentación controlada / roll-in** | — | **hasta 19.438 €+** el rango alto de la categoría de La Hostelera; artículos de gama media **60-700 €+** | con IVA | https://www.lahostelera.com/325-maquinaria-y-suministros-para-panaderia-y-pasteleria (consultado 2026-09-10) — fiabilidad **MEDIA** (rango de categoría, no ficha de producto) |
| **PS-84** | Conducto de extracción de humos de acero inoxidable | — | **puede superar los 6.000 €** | no declarado | Salva (URL de PS-11) — fiabilidad **MEDIA** |

**Marcas de referencia sin precio publicado localizable (todas → «sin fuente (precio)»):** hornos Wiesheu, Miwe, Sveba Dahlen · batidoras Bear Varimixer, Sinmag, KitchenAid Pro · laminadoras Fritsch · abatidores Coldline, Infrico · armarios y cámaras Infrico, Salva · vitrinas Tecnodom, Bakermac · atemperadoras Chocovision, ICB · inyectoras y dosificadoras · mesas de acero y de mármol · envasadora · lavavajillas de obrador.

### 4.3 Obra e instalaciones

| id | Concepto | Cifra | Fuente |
|---|---|---|---|
| **PS-85a** | Obra civil, nivel bajo | **54.000 €** (**600 €/m²**, local de referencia de **90 m²**) | La Hostelera (URL de PS-05) |
| **PS-85b** | Obra civil, nivel medio | **81.000 €** (**900 €/m²**) | Misma |
| **PS-85c** | Obra civil, nivel alto | **108.000 €** (**1.200 €/m²**) | Misma |
| **PS-85d** | Equipamiento, tres niveles | **15.000 € / 29.000 € / 46.000 €** | Misma |
| **PS-85e** | Proyecto técnico | **5.000 €** | Misma |
| **PS-85f** | Asesoramiento profesional | **1.000 €** | Misma |
| **PS-85g** | Marketing | **5.000 €** | Misma |
| **PS-85h** | **Total del escenario recomendado por la fuente** | **137.000 €** = proyecto 5.000 + obra media 81.000 + equipamiento alto 46.000 + marketing 5.000 | Misma |
| **PS-86a** | **Potencia eléctrica solo para los hornos** | **20-80 kW** | Estudio LBA, «Licencia para panadería u obrador en Madrid», actualizado **abr-2026** — https://www.estudio-l.es/licencia-obrador-panaderia-madrid/ |
| **PS-86b** | Caudal de extracción | **50 m³/h por kW** instalado en equipos de gas · **40 m³/h por kW** en eléctricos | Hostelmarkt — https://hostelmarkt.com/actualidad-hosteleria/equipamiento-cocina-industrial-restaurante-guia-tecnica/ (leído en resumen) — fiabilidad **BAJA-MEDIA** |
| **PS-86c** | Salida de humos | conducto **hasta cubierta, 1 m por encima de la cumbrera** | Estudio LBA (URL de PS-86a) |
| **PS-86d** | Zonas obligatorias del local | venta, obrador, almacén de materia prima, cámara frigorífica, almacén de producto terminado, vestuarios/aseos de personal, almacén de residuos; **principio de «marcha adelante»** | Estudio LBA |
| **PS-86e** | Superficies | lisas, lavables e impermeables; **encuentros pared-suelo redondeados**; lavamanos no manual por zona | Estudio LBA |

⚠️ **La lente normativa manda sobre este bloque.** Aquí se recoge lo técnico-económico; los requisitos legales exactos (RD 109/2010, Reglamento CE 852/2004, APPCC, registro sanitario) los fija la lente de normativa. **No duplicar ni contradecir.**

### 4.4 Dotación tipo propuesta — obrador 40-60 m² + tienda 30-50 m²

**Con precios reales de este research.** Todos los importes **sin IVA salvo indicación**, y cada línea con su id.

| Línea | Referencia | Importe | Fuente (id) |
|---|---|---|---|
| Horno de convección con vapor, 6 bandejas | UNOX XB693 Bakerlux (IVA incl.) | **3.354,12 €** | PS-72 |
| Segundo horno / apoyo, 4 bandejas | SMEG ALFA420E1HDS (IVA incl.) | **2.513,41 €** | PS-72 |
| Batidora planetaria 20 L | Sammic BP-20 | **595,04 €** | PS-81 |
| Laminadora automática 40 cm | Sammic DF-40 | **1.215,00 €** | PS-79 |
| Abatidor de temperatura 4 bandejas | Irinox (entrada de gama) | **10.037,00 €** | PS-78 |
| Vitrina expositora refrigerada curva 1,5 m | Docriluc VEPD-9-15-C | **2.284,10 €** | PS-76 |
| Segunda vitrina (mismo modelo) | Docriluc | **2.284,10 €** | PS-76 |
| Atemperadora de chocolate 12 kg *(opcional según concepto)* | Selmi One | **7.400,00 €** | PS-82 |
| **Subtotal de maquinaria con precio verificado** | | **≈ 29.682,77 €** | |
| Cámara/armario de fermentación controlada | rango de categoría | **«sin fuente (precio)» — usar 3.000-19.438 €** | PS-83 |
| Cámara frigorífica, mesas frías, mesa de mármol, congelador, envasadora, lavavajillas de obrador, básculas, pequeño material, TPV, packaging inicial | | **«sin fuente (precio)»** | — |
| **Obra civil, 90 m² a nivel medio** | 900 €/m² | **81.000 €** | PS-85b |
| **Proyecto técnico** | | **5.000 €** | PS-85e |
| **Conducto de extracción** *(evitable con horno eléctrico + campana de condensación)* | | **> 6.000 €** | PS-84 |

> **Cómo debe leerse esta tabla en el producto:** el subtotal de **≈29.700 €** de maquinaria con precio verificado **encaja casi exactamente** con el nivel «equipamiento medio, 29.000 €» de La Hostelera (PS-85d). Es una **validación cruzada entre dos fuentes independientes**, y es el mejor argumento de credibilidad que tiene este research. Con la obra media (81.000 €) y el proyecto (5.000 €), el total ronda los **116.000 €** — dentro del rango de PS-05 (100.000-150.000 €) y por debajo de los 137.000 € del escenario de equipamiento alto.
>
> **Lo que falta para cerrar el CAPEX** (fermentación, frío de conservación, mobiliario, TPV, packaging, fianza y fondo de maniobra) **no tiene precio verificado** y debe ir al xlsx como **líneas en blanco con celda verde**, no rellenadas a ojo.

---

## 5. Proveedores reales del sector (PS-87 … PS-95)

**Todos verificados con URL. Ninguno inventado.** Consultados 2026-09-09/10.

| id | Categoría | Proveedor | Qué vende | Web | Verificación |
|---|---|---|---|---|---|
| **PS-87** | **Ingredientes premium / técnicos** | **Sosa Ingredients** | Ingredientes premium para pastelería y gastronomía moderna. Fundada en Cataluña en **1967**, presente en **más de 80 países** | https://www.sosa.cat/ | **ALTA** (web propia + ficha de marca socia en Valrhona: https://www.valrhona.us/partner-brands/sosa-ingredients) |
| **PS-88** | **Ingredientes de panadería/pastelería/chocolate** | **Puratos** | Masas madre, mejorantes, mixes, rellenos, chocolate | https://www.puratos.com/products | **ALTA** |
| **PS-89** | **Chocolate y coberturas** | **Barry Callebaut** (marcas **Callebaut**, **Cacao Barry**, **Chocovic**) | Coberturas y servicios técnicos para profesionales. **Chocovic es marca de Barry Callebaut** | https://www.barry-callebaut.com/ · https://www.callebaut.com/ · https://www.cacao-barry.com/ | **MEDIA-ALTA** (relación Chocovic↔Barry Callebaut confirmada en resultados; **verificar la web ES antes de publicar**) |
| **PS-90** | **Chocolate premium** | **Valrhona** | Coberturas y formación profesional; distribuye la gama **Sosa** como marca socia | https://www.valrhona.com/ | **ALTA** |
| **PS-91** | **Mantequilla y nata profesional** | **Debic** (FrieslandCampina) | Mantequillas de punto de fusión fijo para hojaldre y bollería, natas profesionales | https://www.debic.com/ | **ALTA** |
| **PS-92** | **Mantequilla profesional** | **Elle & Vire Professionnel** | Mantequillas de laminado; **mantequilla seca 84 % MG** para hojaldre | https://www.elle-et-vire.com/int/es/pro/ (raíz verificada: https://www.elle-et-vire.com/) | **ALTA** |
| **PS-93** | **Harinas** | **Ylla 1878** | Harinas profesionales para panadería, **pastelería**, bollería, churrería y pizzería; integrales, centeno, malta, arroz, maíz, soja, de fuerza | https://www.ylla1878.com/es/harinas-profesionales/ | **ALTA** |
| **PS-94** | **Harinas** | **Farinera Coromina** | Fundada en **1897** en Girona. Harinas especiales, a la piedra, ecológicas, integrales, de centeno, «a la carta», de fuerza y media fuerza. Distribución en península, Baleares, Canarias y sur de Francia | https://www.farineracoromina.com/ (ficha: https://www.proveedores.com/proveedores/farinera-coromina/) | **MEDIA-ALTA** (**verificar el dominio propio antes de publicar**) |
| **PS-95** | **Distribución de materias primas** | **Cospan** | Distribuidor de materias primas de panadería y pastelería | https://cospan.es/ | **MEDIA** |

**Proveedores citados en el encargo que NO se pudieron verificar en este research** → **«sin fuente»**, no publicar sin comprobar: Harinas Polo · Molí de Picó · Harinera Vilafranquina · Dawn Foods · Zeelandia · Bakels · Ravifruit · Boiron · Ovopack · Pascual Ovoproductos · García de Pou · Selfpackaging · Makro (como distribuidor Horeca sí existe, pero no se verificó su catálogo de pastelería) · Sanilus · Cadibe · Silikomart · Matfer · De Buyer · Martellato · Pavoni · Chocolates Torras.

> **Aviso de marca propia:** el directorio **Hosply.pro** (https://www.hosply.pro/, «Directorio de Proveedores HORECA») apareció en los resultados de búsqueda de proveedores. **Es una marca del grupo ChefBusiness** (aparece en el bloque «CHEFBUSINESS GROUP» congelado en 62 posts del blog, según `CLAUDE.md`). Es una oportunidad de enlace interno legítima desde el capítulo de proveedores — **decisión de John**.

---

## 6. Casos de éxito de referencia (PS-96 … PS-103)

| id | Marca | Modelo | Dato público con fuente | Lección para la guía |
|---|---|---|---|---|
| **PS-96** | **Hofmann** (Barcelona) | Escuela + pastelería de autor + obrador central | Fundada **1983**. **Más de 150 profesionales** en el grupo; **una treintena** en el nuevo obrador. Nuevo centro de I+D y producción en **Badalona: 1.200 m²**, inversión **>700.000 €**, operativo desde mediados de enero de 2026; **duplica la capacidad productiva** y prevé **+40 % de producción en 2026**. **Más de 200.000 alumnos** formados en su escuela. **2 tiendas** en Barcelona (Born y Turó Park); expansión a **Dubái**. Croissant de mascarpone: **~3.000 uds/semana ≈ 30 % de la facturación** de la pastelería; pastel de pistacho hasta **1.800 uds/mes**. Turnos de **5:00 a 18:00, de lunes a domingo** — The New Barcelona Post, **12-feb-2026**: https://www.thenewbarcelonapost.com/hofmann-badalona-centro-id-expansion-internacional/ | **Un solo producto puede ser el 30 % de la caja.** El obrador centralizado es lo que permite escalar sin multiplicar tiendas. Fiabilidad **ALTA** |
| **PS-97** | **Pastelerías Pomar** (Mallorca) | Obrador familiar + tiendas, 4.ª generación (1902) | **47 empleados** (10 familiares) · rentabilidad **8-12 %** · obrador **200.000-300.000 €+** · tienda **100.000 €** · **95 %** venta directa / **5 %** a crédito · margen turrón **~40 %** · picos de temporada ×5-10 — El Español/Cocinillas, **21-nov-2025**: https://www.elespanol.com/cocinillas/reportajes-gastronomicos/20251113/matias-dueno-pasteleria-espana-montar-obrador-cuesta-eur-rentabilidad-kw/1003744012399_0.html | **Es el caso más útil de todo el research**: un profesional en activo dando la rentabilidad real y la inversión real. Fiabilidad **ALTA** |
| **PS-98** | **Cientotreinta grados** (Madrid) | Obrador de barrio + café de especialidad + B2B | Fundada por los hermanos **Alberto y Guido Miragoli**, abrió en **Chamberí en 2017**; **ganó el concurso del mejor pan de Madrid en 2020**; nuevo obrador en Prosperidad en **octubre de 2023**. **320 m²** entre los dos locales; **~600 kg/día** de producción con capacidad para **1.200 kg**. **~70 % de las ventas** a clientes particulares fieles, **~30 %** a restauración — Guía Repsol, **25-ene-2024**: https://www.guiarepsol.com/es/comer/en-el-mercado/nuevo-obrador-pan-pasteleria-cientotreinta-grados-madrid/ | **El obrador de barrio moderno crece por producción, no por m² de tienda.** Fiabilidad **MEDIA-ALTA** |
| **PS-99** | **Manolo Bakes** (Madrid) | Cadena propia (**abandonó la franquicia**) | **33,5 M€** de facturación en 2024 (**+40 %** sobre 2023) y **1 M€** de beneficio neto (**+26,5 %**); en 2023 facturó **32 M€** con **42 tiendas**. **Más de 50 locales**; objetivo de **100**. **>25 millones de «manolitos»/año**. Compró los derechos de la marca «Los Manolitos» por **2,5 M€** (jul-2025). Filiales en EE. UU. — El Español/Invertia: https://www.elespanol.com/invertia/empresas/distribucion/20240115/manolitos-manolo-bakes-toman-impulso-elevan-ventas-preparan-internacionalizacion/825167838_0.html · Libre Mercado, **3-jul-2025**: https://www.libertaddigital.com/libremercado/2025-07-03/jue-manolo-bakes-se-hace-con-los-derechos-de-los-manolitos-por-2-5-millones-de-euros-7272362/ | **Un producto icónico monoproducto puede sostener una cadena entera** — y la franquicia no siempre es el final del camino: **recompró sus franquicias**. Fiabilidad **MEDIA-ALTA** |
| **PS-100** | **Levaduramadre** (Comess Group) | Franquicia de panadería-cafetería con obrador propio | **49,3 M€** facturados en 2025 (**+16 %**); **31 aperturas** en el año (**+18 % de red**), cierre en **167 tiendas**; objetivo 2026: **60 M€** y **60 tiendas**. **Inversión de 99.000 €** canon incluido (**canon 12.000 €**); **no requiere salida de humos** — Food Retail: https://www.foodretail.es/retailers/levaduramadre-rozo-los-50-millones-de-facturacion-en-2025-el-16-mas-y-abrio-31-locales.html · Emprendedores: https://emprendedores.es/franquicias/franquicias-actualidad/levaduramadre-roza-los-50-millones-de-facturacion-y-crece-al-16/ | **«Sin salida de humos» es una ventaja de negocio, no un detalle técnico**: reduce el coste del alquiler porque amplía los locales candidatos. Conecta con PS-11 y PS-84. Fiabilidad **MEDIA-ALTA** |
| **PS-101** | **Granier** (Consupan SL) | Franquicia panadería-cafetería | Constituida **2010**. **318 establecimientos** en la ficha oficial (la enseña declara **>350** en España e internacional). **Inversión desde 180.000 €**, **canon 8.000 €**, **royalty 500 €/mes**, **sin canon de publicidad**, contrato **10 años**, local **mínimo 100 m²**. Modelo **autoempleo** desde **10.000 €** con cesión de **1.000 €/mes** y royalty del **2 %** — Franquicias Hoy: https://www.franquiciashoy.es/franquicias/franquicias-de-panaderias-y-pastelerias/panaderias-pastelerias/granier | **Dos modelos de entrada con un orden de magnitud de diferencia** en la misma enseña. Fiabilidad **MEDIA-ALTA** (datos declarados por la franquiciadora) |
| **PS-102** | **Viena Capellanes** (Madrid) | Pastelería + catering + corners de empresa | **276 empleados** (dato 2026) y facturación **+12,33 %** interanual; **22 establecimientos** en Madrid, tienda online y **más de 70 «Viena Corner»** en empresas. **72.000 roscones** en la campaña 2025/26 — eInforma: https://www.einforma.com/informacion-empresa/viena-reposteria-capellanes (**ficha de pago, leída en resumen**) · Infobae/EFE 2-ene-2026 (URL de PS-35) · asociado de Marcas de Restauración: https://marcasderestauracion.es/asociados/viena-capellanes/ | **El canal B2B (corners de empresa, catering) desestacionaliza la caja.** Fiabilidad **MEDIA** (empleados/facturación no verificados en la página) |
| **PS-103** | **Sector franquiciado de panadería-pastelería** | — | **>1.738 establecimientos franquiciados** y **>641 M€** de facturación conjunta anual — Informe de Hostelería y Restauración 2026 de **Tormo Franquicias Consulting**, citado por Franquicia Insider: https://franquiciainsider.com/analisis/analisis-granier-franquicia-2026-05 (leído en resumen) | Contexto de tamaño del canal franquicia. Fiabilidad **BAJA-MEDIA** — **verificar contra el informe original de Tormo antes de publicar** |

**Casos citados en el encargo que NO se pudieron documentar con cifras públicas** → mencionables como referencia de oficio pero **sin ninguna cifra**: Escribà · Bubó · Oriol Balaguer · La Pastisseria (Josep Maria Rodríguez) · Moulin Chocolat (Ricardo Vélez) · Pastelería Mallorca · La Duquesita · Totel (Paco Torreblanca) · Nunos · Cristina Torrent · Santagloria.

> 🚨 **Refutación de un dato del propio encargo.** El encargo sugería que **«Cientotreinta grados»** podía ser una franquicia de **Oriol Balaguer** con «250 k€ + 30 k€ de canon». **Es falso**: Cientotreinta grados es de los hermanos **Alberto y Guido Miragoli** y **no consta como franquicia** (Guía Repsol, PS-98). Esa cifra apareció en un resumen de buscador y **no tiene respaldo**. Va a la lista negra.

---

## 7. Salarios y personal (PS-104 … PS-108)

**Aquí solo va el dato de MERCADO. El convenio lo fija la lente normativa.**

| id | Puesto | Salario | Fuente | Fiabilidad |
|---|---|---|---|---|
| **PS-104** | **Media nacional de pastelero** | **1.791-1.966 €/mes** brutos (Indeed/Jooble); **14,04 €/hora** brutos (Jooble); **14.000-25.200 €/año** brutos | Insertia, «¿Cuánto cobra un pastelero en España? Sueldo y convenio 2026» — https://www.insertia.net/blog/cuanto-cobra-un-pastelero-en-espana-sueldo-por-hora-dia-y-mes-segun-convenio-de-pasteleria (consultado 2026-09-10; **la página no publica fecha**). Cita a Gasma, Jooble, Indeed, Tusalario y CEAC | **MEDIA** |
| **PS-105** | **Por categoría (€/mes brutos)** | Aprendiz **1.000-1.200** · Auxiliar **1.300-1.550** · Oficial de 2.ª **1.400-1.700** · Oficial de 1.ª **1.500-1.900** · **Maestro pastelero 2.000-2.800** · Chef pastelero de hotel 5\* **2.500-3.000** | Misma fuente | **MEDIA** |
| **PS-106** | **Por hora (€ brutos)** | Aprendiz **6,80-8** · Oficial de 1.ª **11-13** · Maestro **15-20** · Chef pastelero premium **18-25** | Misma fuente | **MEDIA** |
| **PS-107** | **Convenio de Barcelona (referencia)** | Dependiente rama mercantil: **988,57 €** de salario base + **545,39 €** de plus de convenio = **1.533,98 €/mes** (tabla 2025) | Cartas Laborales — https://cartaslaborales.app/novedades-convenios/confiteria-pasteleria-barcelona-convenio-2023-2025 (leído en resumen) · CCOO: https://ccoo.app/convenio/convenio-colectivo-confiteria-pasteleria-y-bolleria-de-barcelona/ | **MEDIA** — **la lente normativa debe confirmarlo** |
| **PS-108** | **Convenio de Sevilla** | Subida del **9,95 %** repartida hasta 2026 | El Español, 8-may-2024 — https://www.elespanol.com/sevilla/20240508/convenio-dulce-pasteleros-sevilla-suben-sueldo-ciento-trabajaran-horas/853664800_0.html | **MEDIA** |

**Escala oficial no accesible:** la escala de salarios básicos de la rama de pastelería de marzo y abril de 2026 está publicada en `pasteleros.org` (https://pasteleros.org/wp-content/uploads/2026/04/escala_2026_272-96_pasteleria_abril-octubre.pdf) pero **devolvió HTTP 403**. **Es la fuente que debe usar la lente normativa.**

**Plantillas por modelo (referencias):** 2-5 empleados con un coste de **2.000-6.000 €/mes** en el escenario de plandenegocio.es (PS-61) · **47 personas** en Pomar (PS-54) · **~30** en el obrador nuevo de Hofmann y **>150** en todo el grupo (PS-96) · **276** en Viena Capellanes (PS-102).

---

## 8. Cierre

### 8.1 Tabla PS-* de las cifras que ENTRAN en el producto

Solo las de fiabilidad **ALTA** o **MEDIA-ALTA**, con la etiqueta que debe llevar la cifra en la guía.

| id | Cifra | Valor | Fiabilidad | Etiqueta obligatoria en el texto |
|---|---|---|---|---|
| PS-01 | Inversión obrador en casa | 3.000-5.000 € (mín.) / 5.000-8.000 € (arranque) | MEDIA-ALTA | «según Pastelería Para Todos, jul-2026» |
| PS-02 | Inversión obrador solo producción | 8.000-20.000 € | MEDIA-ALTA | ídem |
| PS-03 | Inversión local con venta | 15.000-50.000 € | MEDIA-ALTA | ídem |
| PS-04 | Inversión cafetería-pastelería | 60.000-100.000 €+ | MEDIA-ALTA | ídem |
| PS-05 | Escenario pastelería 90 m² | 137.000 € (5.000 + 81.000 + 46.000 + 5.000) | MEDIA | «escenario de La Hostelera, sin fecha de publicación» |
| PS-08 | Franquicia Granier | desde 180.000 € · autoempleo desde 10.000 € | MEDIA-ALTA | «datos declarados por la enseña» |
| PS-11 | Ahorro por evitar conducto de humos | >6.000 € | MEDIA | «según Salva Industrial» |
| PS-12 | Empresas CNAE 107 | 11.778 (1-ene-2020) | ALTA | **«dato del INE de 2020; no hay serie posterior pública»** |
| PS-18-25 | Foto CEOPPAN del oficio | 336.000 trabajadores, 15.000 fabricantes, 45.000 puntos de venta | ALTA | **«datos de 2020 y referidos al PAN, no a la pastelería»** |
| PS-26c | Producción congelada de bollería y pastelería 2025 | 233.856 t (+0,17 %) | ALTA | «ASEMAC, abr-2026» |
| PS-26d | Facturación masas congeladas 2025 | 2.001,63 M€ (+3,20 %) | ALTA | ídem |
| PS-26i | Crecimiento producción pastelería 2018-2025 | +31,10 % | ALTA | ídem |
| PS-28 | Consumo en hogar de bollería y pastelería 2025 | 274,2 M kg · 1.917,6 M€ · 5,85 kg/persona | ALTA-MEDIA | «Panel de Consumo del MAPA 2025» |
| PS-29 | Brecha por renta | 8,26 kg (renta baja) vs 4,39 kg (renta alta) | ALTA-MEDIA | ídem |
| PS-31 | Chocolate y derivados 2025 | 2,84 kg · 33,88 €/persona · 11,93 €/kg | ALTA-MEDIA | ídem |
| PS-35 | Roscones campaña 2025/26 | ~30 millones de unidades | MEDIA-ALTA | «estimación de ASEMAC, ene-2026» |
| PS-36 | Roscones en Madrid | >2,9 millones | MEDIA-ALTA | «estimación de Asempas, ene-2026» |
| PS-41 | Multiplicador de temporada alta | ×5 a ×10 sobre día normal | ALTA | «caso Pastelerías Pomar» |
| PS-43 | Concentración de facturación en un producto | ~30 % en un solo croissant | ALTA | «caso Hofmann, feb-2026» |
| PS-48 | **Rentabilidad neta** | **8-12 %** | ALTA | «declaración de Matías Pomar, nov-2025» |
| PS-49 | **Coste de montar un obrador** | **200.000-300.000 €+** | ALTA | ídem |
| PS-50 | **Coste de abrir una tienda** | **100.000 €** | ALTA | ídem |
| PS-53 | Reparto de cobro | 95 % directa / 5 % a crédito 30-60 días | ALTA | ídem |
| PS-55/56 | **Regla de margen** | margen bruto 65-70 % ⇔ food cost <30-35 % | MEDIA-ALTA | «una sola regla, dos lecturas» |
| PS-58 | Break-even ilustrativo | 5.000 € de fijos ⇒ ~7.200 €/mes | MEDIA | «ejemplo, no benchmark» |
| PS-60 | Escenarios de break-even | 5.000→7.000 · 8.000→10.000 · 12.000→15.000 € | MEDIA | «escenario de plandenegocio.es, abr-2026» |
| PS-63 | Ticket medio de restauración | ~21 € (2024) | MEDIA-ALTA | **«es restauración, NO pastelería»** |
| PS-66 | Mantequilla, cotización UE | 386-405 €/100 kg (jun-2026) | MEDIA-ALTA | **«commodity a granel, no mantequilla de hoja»** |
| PS-69/70 | **Traspasos reales** | 6.000-100.000 € · 63-85 m² · rentas 850-1.600 €/mes | ALTA (son anuncios leídos) | **«precio PEDIDO, no pagado»** |
| PS-72 | Hornos de convección | 605-11.276 € con IVA (20 modelos) | ALTA | «La Hostelera, sep-2026, IVA incl.» |
| PS-76 | Vitrina Docriluc VEPD-9-15-C | 2.284,10 € sin IVA | ALTA | «Gavinox, sep-2026, sin IVA» |
| PS-78 | Abatidor Irinox 4 bandejas | desde 10.037 € + IVA | MEDIA | «EquipoH» |
| PS-79 | Laminadora Sammic DF-40 | 1.215 € sin IVA / 1.470,15 € con IVA | MEDIA | «Alimaq» |
| PS-81 | Batidora Sammic BP-20 | desde 595,04 € | MEDIA | «HostelShopping» |
| PS-82 | Atemperadora Selmi One 12 kg | 7.400 € + IVA | MEDIA | «Chocosolutions» |
| PS-85 | Obra civil | 600 / 900 / 1.200 €/m² | MEDIA | «La Hostelera» |
| PS-86a | Potencia eléctrica solo hornos | 20-80 kW | MEDIA-ALTA | «Estudio LBA, abr-2026» |
| PS-87-95 | Proveedores verificados | 9 con URL | ALTA/MEDIA-ALTA | — |
| PS-96 | Hofmann | 1.200 m², >700.000 €, >150 empleados, +40 % previsto | ALTA | «feb-2026» |
| PS-97 | Pomar | 47 empleados, 8-12 % de rentabilidad | ALTA | «nov-2025» |
| PS-98 | Cientotreinta grados | 320 m², ~600 kg/día (cap. 1.200), 70/30 B2C-B2B | MEDIA-ALTA | «ene-2024» |
| PS-99 | Manolo Bakes | 33,5 M€ (2024, +40 %), >50 locales, >25 M manolitos/año | MEDIA-ALTA | «datos de 2024» |
| PS-100 | Levaduramadre | 49,3 M€ (2025), 167 tiendas, inversión 99.000 € | MEDIA-ALTA | — |
| PS-101 | Granier | 318 establecimientos, canon 8.000 €, royalty 500 €/mes | MEDIA-ALTA | «declarado por la enseña» |
| PS-104-106 | Salarios de mercado | 1.300-2.800 €/mes según categoría | MEDIA | **«mercado, no convenio»** |

**Recuento: 47 filas con fuente.**

### 8.2 🚫 LISTA NEGRA — cifras que circulan sin fuente primaria y NO deben entrar

| # | Cifra prohibida | Dónde circula | Por qué se rechaza |
|---|---|---|---|
| **N-1** | **«11.729 pastelerías y panaderías en España en 2025, +2,11 % sobre 2023»** | recipok.com — https://recipok.com/asi-esta-realmente-el-sector-de-la-pasteleria-en-espana-en-2025-aperturas-cierres-y-el-dato-que-nadie-te-cuenta/ | Blog sin fuente primaria; el INE **no publica** ese desglose (L-1/L-3). Precisión falsa: dar cuatro dígitos a un censo que no existe |
| **N-2** | 🚨 **«Facturación media anual por pastelería: 1,08 millones de euros»** | modelosdeplandenegocios.com — https://modelosdeplandenegocios.com/blogs/news/analisis-mercado-pastelerias-espana | **Absurdo y peligroso.** Contradice frontalmente a PS-48/PS-57/PS-60 (un obrador artesano factura 7.000-15.000 €/mes ⇒ 84.000-180.000 €/año). Un lector que planifique sobre 1,08 M€ **quiebra**. Contenido de granja de IA |
| **N-3** | **«Cientotreinta grados, franquicia de Oriol Balaguer, 250 k€ + 30 k€ de canon, 5 % royalty + 2 % marketing»** | Resumen de buscador, sin página que lo respalde | **Refutado por PS-98**: la marca es de los hermanos Miragoli y no consta como franquicia |
| **N-4** | **«Franquicia Manolo Bakes: ~300.000 € de inversión»** | asest.es, enriquearanzubia.es | **Manolo Bakes recompró sus franquicias y ya no franquicia en España** (franquiciainsider.com, PS-99). Vender una inversión en una franquicia que no existe |
| **N-5** | **«Chocolate cobertura 18-22 €/kg · vainilla 600-800 €/kg · frutos secos 15-35 €/kg · mantequilla 9-12 €/kg»** | Resumen atribuible a pleko.app | Sin fecha, sin formato (granel/minorista), sin proveedor. Los precios de commodity de 2026 se mueven ±50 % (PS-67) |
| **N-6** | **«68,2 % super / 12,5 % hiper / 10,6 % tienda tradicional» presentado como reparto de la BOLLERÍA** | Varias webs | Es el reparto del **total de la compra alimentaria** en 2025, no de bollería (PS-34). Error de atribución que exagera el peso del comercio especializado |
| **N-7** | **«El cacao cotiza a X USD/t»** (cualquier valor puntual) | Todas las fuentes de PS-67 | Cuatro cifras distintas para 2026 (3.300 / 4.000 / 5.000 / 6.205). **Sin consenso ⇒ sin cifra** |
| **N-8** | **«Horno modular Salva, 1.499 € sin impuestos»** | confiyepes.com | Precio de un listado antiguo para un equipo cuyo fabricante vende a presupuesto (PS-73). Induciría a presupuestar un horno de pisos por el precio de uno de convección |
| **N-9** | **«Mercado sin gluten +18 % entre 2022 y 2025»** | eurobakeries.com (PS-45) | Proveedor de pan sin gluten dando el tamaño de su propio mercado, sin citar estudio |
| **N-10** | **«Los pasteleros esperan vender un 4 % más por Todos los Santos»** sin decir el año | vivirediciones.es / andaluciainformacion.es (PS-39) | La página devolvió **403** y no se pudo fechar. Una cifra de campaña sin año no vale nada |
| **N-11** | **Cualquier «ticket medio de pastelería»** | — | **No existe dato público** (PS-64). Va como parámetro editable, no como dato |
| **N-12** | **Cualquier «reparto de ventas por día de la semana»** | — | **No se encontró fuente** (L-6). Va como supuesto declarado |
| **N-13** | **«12.751 empresas y 1.789 M€ en el CNAE 4724»** presentado como censo | eInforma (PS-15) | Solo cubre sociedades que depositan cuentas; **excluye a los autónomos**, que son la mayoría del sector. Vale como orden de magnitud, **nunca como censo** |

### 8.3 Las 5 cifras clave para la portada del producto

Elegidas por tener **la fuente más fuerte y más reciente**, no por ser las más llamativas.

| # | Cifra de portada | Valor | Fuente | id |
|---|---|---|---|---|
| **1** | **Inversión tipo** | **entre 3.000 € (obrador en casa) y 200.000-300.000 € (obrador completo)** — la guía cubre los **11 modelos**, con el escenario medio de pastelería con obrador en **~137.000 €** | Matías Pomar (El Español, **21-nov-2025**) para el extremo alto; Pastelería Para Todos (**12-jul-2026**) para el bajo; La Hostelera para el escenario medio | PS-49, PS-01, PS-05 |
| **2** | **m²** | **90 m²** en el escenario de referencia · los traspasos reales de Barcelona van de **63 a 85 m²** · obrador de barrio de referencia: **320 m²** entre dos locales | La Hostelera; Milanuncios (consultado **2026-09-10**); Guía Repsol (**25-ene-2024**) | PS-05, PS-69, PS-98 |
| **3** | **Personal** | **de 1 a 5 personas** según modelo, con un coste de **2.000-6.000 €/mes**; salarios de mercado **1.300-2.800 €/mes** por categoría | plandenegocio.es (**13-abr-2026**); Insertia | PS-61, PS-105 |
| **4** | **Ticket / margen** | **margen bruto 65-70 %** ⇔ **food cost por debajo del 30-35 %**, y **rentabilidad neta real del 8-12 %** | Pastelería Para Todos (**12-jul-2026**) y Matías Pomar (**21-nov-2025**) | PS-55, PS-56, PS-48 |
| **5** | **Break-even** | **5.000 € de costes fijos ⇒ ~7.200 €/mes de facturación**; escenarios de **7.000 / 10.000 / 15.000 €/mes**; **ROI de 18-36 meses** | Pastelería Para Todos; plandenegocio.es (**13-abr-2026**) | PS-58, PS-60, PS-62 |

> ⚠️ **Aviso para el copy de portada (regla de John del 5-sep sobre copy comercial):** la cifra **8-12 % de rentabilidad** es honesta y **poco vendible**. Es exactamente por eso por lo que debe ir: ninguna guía de la SERP la dice. El gancho es **«te decimos lo que gana de verdad una pastelería»**, no «monta tu pastelería y hazte rico». Y **el precio del producto (65 €) frente a los 700-800 € que cuesta un plan APPCC externo** (PS-01, Pastelería Para Todos) es el argumento de valor más limpio que hay en todo este research.

---

## 9. Propuesta de entregables (para el guion, no es contenido)

Derivada de lo que **sí tiene datos** en este informe:

1. **`01_Modelo`** — matriz de los 11 sub-conceptos (§1.1) con celda verde de selección.
2. **`02_CAPEX`** — dotación tipo del §4.4 con las líneas verificadas prerrellenadas y las no verificadas **en blanco con celda verde**. Nunca rellenar a ojo lo que no tiene fuente.
3. **`03_Traspaso_vs_Obra`** — comparador que enfrenta traspaso + renta contra obra nueva a 5 años (la lectura 2 de §3.5). **No existe en ninguna guía de la competencia.**
4. **`04_Escandallo`** — food cost por lote con la regla única de §3.1 (margen ⇔ food cost, calculada una desde la otra) y línea de packaging al 5-15 %.
5. **`05_Estacionalidad`** — plan de producción con multiplicador de campaña ×5-10 (PS-41) y las 6 campañas (Reyes, San Valentín, Semana Santa, comuniones, Todos los Santos, Navidad).
6. **`06_PyG_y_BreakEven`** — 3 escenarios de §3.2 con rentabilidad objetivo anclada al 8-12 % real.
7. **`07_Sensibilidad_MP`** — mantequilla y cacao como **parámetros con rango**, nunca como constante (§3.4 y N-7).
8. **`08_Personal`** — plantilla por modelo con salarios de mercado y coste empresa.
9. **`09_Proveedores`** — los 9 verificados de §5, con columna vacía para los que el lector añada.

---

*Fin del informe L4. Research y propuesta; sin contenido de producto.*
