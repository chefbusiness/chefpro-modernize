# RESEARCH CONSOLIDADO — «Guía Food Cost + Ingeniería de Menú»
## Producto digital NUEVO · AI Chef Pro · línea «Guías técnicas Premium»

**Fecha:** 2026-09-03 · **Estado:** research cerrado, PENDIENTE DEL OK DE JOHN antes de escribir una sola línea de producto.
**Fuentes:** las cinco lentes de research de este mismo directorio (`guia-food-cost-research-L1-competencia.md`, `-L2-serp.md`, `-L3-datos.md`, `-L4-cliente.md`, `-L5-assets.md`), leídas enteras, más verificación directa contra el repo (`astro-site/public/dl/`, `astro-site/src/data/productos/`, `scripts/productos-digitales/guias-v2-SPEC.md`, `CALENDARIO-V2-SEMANAL.md`).
**Regla aplicada:** cada cifra lleva fuente y fecha, o va marcada **«sin fuente»**. Nada inventado. Este documento es research y propuesta: **no contiene contenido de producto** (eso lo produce `bridge.py` después, según la regla capital).

---

## 0. Lo primero, porque cambia cómo se vende esto

**La demanda SEO de este producto es PEQUEÑA, y hay que decirlo antes de decidir nada.** Los volúmenes medidos con DataForSEO (España, Google Ads, búsquedas/mes, medidos 2026-09-03 en el contexto del encargo):

| Keyword | España | México | Argentina | Colombia |
|---|---|---|---|---|
| escandallo | **5.400** (competencia LOW) | 210 | 140 | 90 |
| menu engineering | 320 | 50 | — | — |
| como hacer un escandallo | 170 | — | — | — |
| food cost | 90 | 70 | 40 | 50 |
| escandallo de un plato | 70 | — | — | — |
| ingeniería de menú | 40 | 90 | — | 20 |
| que es el food cost | 20 | — | — | — |
| costeo de recetas | 10 | **390** | — | — |
| «guia food cost» · «curso food cost» · «libro food cost» | **sin volumen** | | | |

Tres lecturas incómodas y necesarias:

1. **El único head term con volumen real en España es «escandallo» (5.400/mes)… y ya lo tenemos ocupado.** GSC (90 días) muestra que «plantilla escandallo…» lleva a `/kit-escandallos` en **posiciones 8-15**. Una landing nueva con «escandallo» en el slug competiría contra nuestro propio activo que ya rankea. **Argumento duro para NO meter «escandallo» en el slug** (§10).
2. **La intención comercial de este producto no se busca.** «guia food cost», «curso food cost» y «libro food cost» tienen volumen cero. Nadie teclea el nombre del producto. La landing **no va a captar por búsqueda**, igual que ya pasa con las librerías de prompts (criterio de John, 2026-07-31: no se miden por tráfico SEO).
3. **La SERP de «escandallo» está cerrada.** AI Overview presente, y el top lo copan RAE, Wikipedia, una app (escandallos.es), escuelas (ESAH, CESAE) y SaaS (Cegid, ComboHR). No es una SERP donde una landing de producto entre por la puerta.

**Entonces, ¿por dónde entra el dinero? Por cuatro canales que ya existen y son nuestros:**

| Canal | Estado real hoy | Qué hay que hacer |
|---|---|---|
| **Banners en el blog ES** | 325/325 posts con 3 banners, 44/44 productos en rotación (`fase8e-banners-corpus.py`, 2026-08-31) | Añadir el producto 45 al catálogo y **reejecutar la rotación**; los 6 posts de food cost/escandallo/mermas que ya existen son colocación de máxima relevancia temática (§14) |
| **Los 6 posts propios ya publicados** que tratan exactamente esto | `8-errores-que-destruyen-el-food-cost-en-tu-restaurante`, `food-cost-ia-escenarios-inflacionarios-2026`, `mejores-calculadoras-food-cost-ia-comparativa`, `escandallos-ia-cocina-profesional`, `carta-restaurante-rentable-ingenieria-menu-ia`, `que-son-las-mermas-en-cocina` | Enlace contextual + banner fijado por relevancia (no rotado) hacia la landing nueva |
| **Lista de clientes** (compradores del Kit de Escandallos 12 €) | Es el público perfectamente cualificado: ya pagaron por escandallar | Campaña Resend al segmento que compró kit-escandallos (skill `resend-operaciones-grupo`) |
| **Hub `/productos-digitales` + plataforma** | Hub vivo; la plataforma (Pickaxe) tiene agentes de escandallo/carta | Tarjeta en el hub + mención desde los agentes relacionados |

**Conclusión del bloque:** este producto se lanza porque **hay demanda de problema** (medida en la voz del cliente, §6) y porque **tenemos el canal**, no porque haya demanda de búsqueda. Si el criterio de decisión fuera el volumen SEO, no se lanzaría. Es exactamente el mismo criterio con el que John aprobó las librerías de prompts.

---

## 1. Tipos y sub-conceptos que la guía DEBE distinguir

Esto es el equivalente, en una guía técnica, a «los tipos de negocio» de una guía de «Cómo Montar». Son los conceptos que la SERP española mezcla o directamente no distingue, y donde está la autoridad del producto.

| # | Concepto | Qué es exactamente | Con qué se confunde | ¿Lo cubre la SERP gratuita? |
|---|---|---|---|---|
| 1 | **Food cost teórico** | Coste que sale de la receta escandallada × unidades vendidas | Con el real; casi nadie los nombra por separado | Solo Purohospitality lo nombra; **ninguna fuente enseña a medir la diferencia** (L2 §2.15) |
| 2 | **Food cost real** | (Stock inicial + compras − stock final) / ventas del periodo | Ídem | Presente, pero sin cruzarlo con el teórico |
| 3 | **Desviación teórico-real** | La diferencia, y sus causas: merma no registrada, raciones descontroladas, robo, error de inventario | Se llama «merma» a todo | **No** |
| 4 | **Merma de despiece / rendimiento** | Pérdida de peso del producto al limpiar/despiezar (bruto→neto) | Con el desperdicio | Sí, básico (4/18 fuentes) |
| 5 | **Merma de cocción** | Pérdida por técnica (plancha, horno, fritura, sous-vide) | Con la anterior | **No: ninguna fuente da tabla por técnica** (L2 §2.8) |
| 6 | **Desperdicio (waste)** | Producto tirado: caducado, mal conservado, error de servicio | Con la merma | Parcial |
| 7 | **Margen de contribución (€)** | PVP neto − coste de materia prima, **en euros** | Con el food cost % | Sí en menu engineering |
| 8 | **Food cost %** | Coste / venta **neta** × 100 | Con el margen; y con el PVP **con IVA** (error de raíz, §2) | Sí, pero mal (§2) |
| 9 | **Prime cost** | Food cost + coste de personal (con SS) sobre venta | No se menciona | **No: 0/18 fuentes lo calculan** (L2 §2.7) |
| 10 | **Beverage cost / pour cost** | Coste de bebida sobre venta de bebida, como cuenta propia | Se mete dentro del food cost global | Mención de pasada en 4/18, **sin rangos** (L2 §2.3) |
| 11 | **Coste por lote (obrador)** | Coste de una tanda repartido entre el rendimiento en unidades, + mano de obra por hora + packaging | Con el escandallo por ración | **No, con ejemplo numérico completo** (L2 §2.4) |
| 12 | **Food cost efectivo por canal** | El que queda tras comisión de plataforma y packaging en delivery/take away | Se usa el mismo número para sala y delivery | **No: 0/18 fuentes lo calculan** (L2 §2.2) |
| 13 | **Escandallo de menú de precio fijo** | El margen lo decide el **mix** de elecciones, no el plato | Con el escandallo plato a plato | **No** (L2 §2.12) |
| 14 | **Popularidad (mix %)** | Cuota de ventas del plato **dentro de su familia**, no sobre la carta entera | Se calcula sobre el total y descoloca la matriz | Se cita el 70 %/N en 7/18, casi siempre sin la corrección por familia |
| 15 | **Precio objetivo vs precio de mercado vs precio de valor** | Tres formas distintas de llegar al PVP; la del factor no vale para todo | Se enseña solo la del factor (coste/FC) | **No** |

**Ese es el índice de conceptos del producto**: 15 distinciones, de las cuales **7 no las cubre bien nadie en español gratis** (3, 5, 9, 10, 11, 12, 13) y **2 más se cubren mal** (8 y 14).

---

## 2. Regulación y fiscalidad España 2026 que afecta al cálculo

Esta es **la mayor ventaja competitiva del producto** y no es una opinión: L2 midió que **de 18 fuentes con contenido recuperable, solo 3 mencionan el IVA y NINGUNA explica si el % de food cost se calcula sobre PVP con IVA o sobre base imponible**. Y nosotros ya tenemos el criterio verificado y aplicado en el código vivo (commit `379fe79`, 2026-08-31).

### 2.1 Lo que SÍ aplica

| Regla | Valor | Fuente | Fiabilidad |
|---|---|---|---|
| IVA repercutido en servicio de hostelería (comida y bebida servidas para consumo en el acto, **incluida la bebida alcohólica en sala**, y también take away y delivery) | **10 %** | Ley 37/1992, art. 91.Uno.2.2º — texto consolidado en `boe.es/buscar/act.php?id=BOE-A-1992-28740` (consultado 2026-09-03) | **Alta** (BOE, fuente primaria) |
| IVA al **21 %** — única excepción relevante | Venta de producto cerrado **sin servicio** (la botella sin abrir que el cliente se lleva) | Misma Ley, art. 91.Uno.2.2º | Alta |
| IVA **soportado** en compras: tres tipos distintos en el mismo albarán | **4 %** (pan común, harinas panificables, leche, huevos, quesos, frutas, verduras, hortalizas, legumbres, tubérculos, cereales) · **10 %** (resto de alimentos: carnes, pescados, conservas, aceite…) · **21 %** (bebidas alcohólicas y azucaradas/refrescos) | Ley 37/1992 art. 91.Dos y art. 91.Uno; listado contrastado en tres fuentes fiscales independientes (Rankia, Calders Economistes) | Media-Alta — **no se pudo leer el PDF oficial de la AEAT** (venía en binario comprimido), así que la guía debe citar el BOE, no el PDF |
| Consecuencia para el escandallo | El restaurante paga IVA distinto por línea de compra pero **siempre repercute el 10 % en sala** → el escandallo debe registrar el IVA soportado **por partida** si quiere el coste neto real; y el food cost % se calcula **sobre venta neta (base imponible), no sobre el precio de carta** | Deducción de lo anterior (L3 §3.6) | — (razonamiento, se marca como tal) |

### 2.2 Lo que NO aplica (y hay que decirlo para que nadie lo copie de un blog americano)

- **No hay «tip credit» ni estructura de propinas americana**: los rangos de food cost «ideales» de la National Restaurant Association (28-35 %, citados por Purohospitality) vienen de un mercado con otra estructura de costes. **No trasladan limpio** (L2 §3).
- **No hay impuesto especial de bebida azucarada que altere el escandallo** más allá del tipo de IVA de compra (21 %).
- **No aplica el «IEPS» mexicano ni figuras equivalentes** en España: si algún día se hace el anexo LATAM, es research aparte (§17, decisión de John).
- **La casilla de IVA de las herramientas va EDITABLE**, nunca fija: un comprador de México/Argentina/Colombia debe poder poner su tipo (L4, glosario).

### 2.3 ⚠️ Hallazgo con dinero detrás: tenemos ese error VIVO en producción hoy

`scripts/productos-digitales/kit-escandallos-v2_0/bono-guia-food-cost-30-dias.md:630` dice:

> «En hostelería en España, las bebidas alcohólicas de alta graduación llevan IVA del 21 %, así que conviene separarlas para no distorsionar los cálculos.»

Es **exactamente** el error que John mandó corregir el 2026-08-31 y que ya está corregido —con la cita legal literal— en `astro-site/public/dl/guia-restaurante-gastronomico/escandallo-maestro.xlsx`, celda `Ficha (plantilla)!I31`. **El bono del kit no formaba parte de aquel commit y sigue publicado con el error** (`/dl/kit-escandallos/BONUS-guia-food-cost-30-dias.pdf`).

**Implicación directa para este lanzamiento:** si la guía nueva enseña el 10 % (que es lo correcto) y el bono del kit sigue diciendo 21 %, **el mismo cliente lee dos cosas contradictorias firmadas por nosotros**, y en el producto barato está la equivocada. **Es una decisión para John (§17, nº3): la corrección del bono debería ir ANTES o EN el mismo sprint que este lanzamiento.**

---

## 3. Herramientas críticas: qué usa el sector y qué damos nosotros

### 3.1 Qué usa el sector (medido en L1)

| Categoría | Qué es | Precio confirmado | Fuente |
|---|---|---|---|
| **SaaS de food cost** | tSpoonLab (escandallos + food cost paramétrico); Haddock (OCR de facturas + food cost dinámico) | **95 €/mes** (tSpoonLab, desde) · **95 €/mes Standard, 120 €/mes Premium anual, IVA aparte** (Haddock) → **1.140-1.440 €/año** | `tspoonlab.com/restauracion/` · `haddock.app/precios-de-haddock` (2026-09-03) |
| SaaS/TPV con menu engineering incrustado | Gstock, PLEKO, Ágora POS, Mapal OS | Bajo demanda / no publicado — **sin fuente (precio)** | L1 §1.4 |
| **Plantillas Excel sueltas de pago** | ingenieriademenu.com (matriz BCG automática); Germán De Bonis (hasta 200 platos) | **15,75 €** · **9 USD** (oferta, normal 19 USD) | L1 §1.2 |
| **Excel gratuitos** | Decenas de plantillas de escandallo publicadas por blogs del sector | 0 € | L4 §4, objeción 1 (con URLs) |
| Cursos | Aprendum 29 € (acceso **3 meses**), La Fábrica 100 € (presencial 6 h), Scoolinary (suscripción **79,90 €/año**, 4,4/5 con 808 valoraciones) | Confirmados | L1 §1.3 |
| Formación superior | Máster F&B Barcelona Culinary Hub | **8.200 € online / 11.800 € presencial** | `barcelonaculinaryhub.com` (2026-09-03) |

**El hueco, verificado producto a producto (L1 §3): ningún producto en español integra, en un solo pago único vitalicio, documento técnico largo + Excel de escandallo con fórmulas vivas + Excel de ingeniería de menú con fórmulas vivas.** Los libros son texto; las plantillas son solo Excel; los cursos caducan; el SaaS es una suscripción.

### 3.2 Qué damos nosotros, y de dónde sale cada motor

L5 auditó, celda a celda y con `openpyxl`, los 13 xlsx del kit y los 2 de la guía gastronómica. **Tres cosas cambiaron la propuesta:**

1. **El «análisis de carta por familias con umbral 70 %/N» que parecía la joya de la corona YA EXISTE**, con fórmulas correctas, en `menu-engineering-matrix.xlsx` (columnas H/K/L, `L5 = $I$32/SUMPRODUCT(--($C$5:$C$29=$C5),--($D$5:$D$29>0))` con `I32=0,7`). **No se construye otra vez.**
2. **`10-calculadora-pvp.xlsx!G18 = $C$4*E18/(1-F18)`** ya descuenta la comisión de plataforma antes del PVP — pero **solo en una fila por tipo de negocio**, no por plato. Esa fórmula es la base del simulador multicanal nuevo.
3. **`escandallo-maestro.xlsx` v2.0 ya tiene todos los fixes** que la SPEC daba por pendientes (`G7=D7/(1-F7)` cantidad bruta, `H29=H28/$F$4` coste por ración, `H30=H29/H4` PVP sin IVA, `H31` IVA en celda, `H34` food cost real). Es el motor de coste por ración de todo lo nuevo.

**Y `documentos.py` se reutiliza al 100 % sin tocar una línea de código** (L5 §4.1): solo hay que escribir un `guion_<pid>.py` nuevo con `GUIA` + `CAPITULOS` + `BONUS` y poblar `astro-site/public/dl/<pid>/` con los xlsx. Eso incluye la batería completa de gates (páginas medidas con PyMuPDF, palabras, paridad PDF↔DOCX, tablas ancladas, no-latinos, WinAnsi, fechas caducas, coherencia de cifras, metadata). **Es la pieza de más apalancamiento de todo el research.**

---

## 4. Fuentes y proveedores de datos reales (de dónde saca el LECTOR sus números)

Un capítulo entero de la guía debe enseñar al lector a alimentar sus propias tablas. Esto es lo que hay, verificado:

| Qué dato | Fuente pública real | URL | Fiabilidad |
|---|---|---|---|
| Precios en origen y mayorista de 34 productos frescos | **Observatorio de Precios y Mercados del MAPA** (sistema origen-mayorista vía Mercasa) | `mapa.gob.es/es/alimentacion/temas/observatorio-cadena/cadenas-valor/sistema-de-precios-om` | Alta (institucional) |
| Inflación de alimentos | **INE**, notas de prensa mensuales del IPC | `ine.es/dyngs/Prensa/IPC0226.htm` y siguientes | Alta (oficial) |
| Tipos de IVA | **BOE**, Ley 37/1992 texto consolidado, art. 91 | `boe.es/buscar/act.php?id=BOE-A-1992-28740` | Alta (primaria) |
| Estructura de costes de un restaurante español | **CaixaBankLab × Fundación elBulli** | `caixabanklab.com/elbullifoundation/es/consumos-beneficios-restaurante/` | Alta |
| Ejemplo real y fechado de volatilidad | Aceite de oliva en origen: **3,91 €/L → 3,22 €/L** en la campaña 2025/26, mínimo de 4 campañas; AOVE estabilizado en 3,40-3,50 €/kg | Libre Mercado, publicado 2026-08-28 | Alta |
| Comisiones de delivery | Glovo 15-35 % + IVA (+cuota ~39 €/mes) · Uber Eats 30/25/15-20 % + IVA por escalón · Just Eat **13 % + IVA solo marketing** o 25-35 % servicio completo (+0,30 €/pedido) · Deliveroo 30 %/25 % + fee 50 €/mes · packaging 1,35-2,15 €/pedido | qamarero.com (2026-09-03) | **Media — fuente ÚNICA especializada. Las plataformas NO publican tarifario. La guía debe decir «orden de magnitud de mercado 2025-2026», nunca «tarifa oficial»** |
| Precio de proveedor propio | El albarán del lector | — | La guía tiene que insistir: **el dato bueno es el suyo**, no el de una tabla |

**Regla de redacción derivada (§7-bis.21 de `guias-v2-SPEC.md`, «sin fuente, no entra»): la guía enseña a CONSULTAR estas fuentes, no las sustituye con una tabla de precios que caducaría en tres meses.** Esto además protege el producto: una guía con precios de ingredientes dentro envejece; una guía que enseña a leer el Observatorio del MAPA, no.

---

## 5. Modelo de negocio del lector: rangos de food cost y margen, con fuente

| Segmento | Food cost objetivo | Fuente | Fiabilidad |
|---|---|---|---|
| **Media del sector, España** | **~30 %**; rango sano 25-35 % | CaixaBankLab × elBulliFoundation | **Alta** |
| **Desglose comida/bebida, España** | **Comida 28 %** sobre ingresos de comida · **Bebida 34,5 %** sobre ingresos de bebida · mix de ingresos 70/30 | Misma fuente | **Alta** |
| Gastronómico / fine dining, España | 20-25 % | qamarero.com | Media |
| Restauración tradicional de carta | 28-32 % (otra fuente: 30-35 %) | qamarero.com | Media |
| Bar de tapas | 28-35 % | qamarero.com | Media |
| Pizzería | 25-30 % | qamarero.com | Media |
| Cafetería | 20-28 % | qamarero.com | Media |
| Dark kitchen / delivery | 28-32 % objetivo, hasta 30-38 % típico, **incluyendo packaging dentro del food cost** | agregado (foodshot.ai, kitchennmbrs.app) — mayormente LATAM/EEUU | Media |
| Pastelería/obrador artesanal | 28-34 % (industrial B2B 32-38 %) | agregado LATAM (GASDA, Roomlab, bcnsoft) — **no es fuente española** | Media |
| Hotel F&B / buffet | 28-40 % | Cucinovo (**EEUU**) | Media — **usar con reserva explícita** |
| Marisquería | 40-42 % | **sin fuente trazable** — cifra plausible, repetida en agregados, sin URL única | **Baja — NO publicar sin segunda fuente** |
| **Beverage cost** | Espirituosos/cócteles 15-22 % · barril 20-26 % · botella/lata 24-28 % · pour cost objetivo 18-24 % | getbackbar/purimax (**EEUU**) | Media |
| Beverage cost, referencia española | 15-25 % en bebidas estándar | qamarero.com | Media |
| **Prime cost (food + personal)** | ≤ **60 %** de la venta; > 65 % hace muy difícil ser rentable salvo alto volumen. Full service 60-65 %, QSR 55-60 % | Toast (**EEUU**, pero es la referencia más citada del sector) | Media — **es el hueco que L5 marcó como «research pendiente»; queda resuelto con esta fuente, citada como EEUU y como convención de sector, no como dato español** |
| Coste de personal, España | **30-35 %** con servicio en mesa · **15-25 %** autoservicio/barra | CaixaBankLab × elBulliFoundation | **Alta** |
| Estructura completa, España | Producto 30 % + Personal 30-35 % + Alquiler ≤5-10 % + Generales 13-20 % (ideal 17 %) → **EBITDA sano 10-13 %**; por debajo del 10 % toca reestructurar | Misma fuente | **Alta** |
| SMI y coste laboral | SMI 1.184 €/mes en 2025; coste empresa por trabajador ~1.500 €/mes | Diario de Gastronomía citando informe de Hostelería de España | Media |
| Inflación de alimentos | **+3,2 % interanual en febrero 2026** (último dato exacto disponible) · julio 2026 **−0,7 % intermensual** · agosto 2026: solo tendencia confirmada («bajaron menos que hace un año»), **cifra interanual exacta NO disponible** | INE | Alta / **el dato de agosto es un hueco declarado: no se inventa** |

**El matiz de autoridad que casi nadie cuenta:** la fuente española más sólida dice que la **bebida tiene PEOR food cost (34,5 %) que la comida (28 %)** sobre sus respectivos ingresos. Contradice el tópico de «la bebida siempre da más margen». La guía debe explicarlo, no simplificarlo — y es justo el tipo de matiz que separa un documento técnico de un post de blog.

---

## 6. Casos y voz real del sector (solo lo que tiene fuente)

L4 se topó con un bloqueo importante y hay que decirlo: **Reddit, Quora, Udemy y los comentarios de YouTube estaban bloqueados a nivel de herramienta** (HTTP 403 / fetch denegado, con intentos repetidos). No hay voz cruda de foro en este research. Lo que sí hay, con nombre y fecha:

| Uso en la guía | Cita / caso | Fuente |
|---|---|---|
| **Apertura del capítulo de proveedores** | Agus (@Eldel_Bar, hostelero, España): «Hace cinco años cobraba la caña a 1,60 euros, ahora a 2 euros, **pero el barril me cuesta el doble**.» | El Español, 26-10-2025 |
| **Capítulo de inflación / re-escandallado** | Tres dueños de restaurante en Palermo (Buenos Aires): «La papelería subió un 27 %; el pollo, 18 %; la carne, 38 %; las hamburguesas, 50 %; las aceitunas… ¡un 100 %!» · «Me parece una locura subir un 100 % la carta» · un CEO de cafeterías: «nos llegan **dos listas de precios de proveedores** en el mismo día» | El Cronista, 16-08-2023 |
| **Voz LATAM femenina / bar-cafetería** | Luz Stella García (Barranquilla): «Subió el salario de los trabajadores, las verduras y, en general, todos los insumos están demasiado caros» · Diana Marcela Vélez (Bogotá): «Todo está muy caro y tengo que sostener el negocio sin echar a ningún empleado» | warocol.com |
| **Capítulo de carta corta** | Restaurante criollo en Miraflores (Lima): recortó la carta de **48 a 28 platos** → ticket medio S/ 38 → S/ 44 (**+16 %**) y food cost del **34 % al 29 %** | panca.pe (caso publicado, sin nombre del local) |
| **Capítulo de delivery** | Lomo saltado a S/ 38: **62 % de margen en sala → 19 % en la app**; ajustando a S/ 45 en la app, sube a 38 % | gestionrestoba.com (patrón repetido en olaclick.com, México) |
| **Capítulo de obrador** | Ana Aboli, repostera (España): «Aún no puedo vivir de Confeti» · «Valórate más y valora tu trabajo. Si regalas tu trabajo, ni te valoras a ti, ni valoras lo que haces» | yoemprendedora.es |
| **Perfil de comprador avanzado** | Angelo Vassallo, Director de A&B del Fairmont Rey Juan Carlos I: «Un restaurante es una empresa, es un negocio. **El propietario no sólo es un cocinero**» | LinkedIn Pulse — ⚠️ menciona «el virus», así que es de 2020-2021: **se cita como voz profesional, no como dato de mercado actual** |
| **La objeción a batir, literal** | Reseña **1★**, España, 15-03-2024, sobre un libro del nicho: «casi un tercio del total de páginas dedicadas a explicar **matrices básicas**» y cuestiona «el precio que es significativamente más alto» | amazon.es/dp/B0CSYX51GG |

**Dos ausencias declaradas:** no se encontró **ninguna cita textual de un restaurantero mexicano con nombre** pese a búsquedas dirigidas, y **4 de los 5 libros del nicho en Amazon.es tienen 0 reseñas** (la muestra de voz de comprador es de una sola obra). Además, **dos estadísticas que circulan («67 % no conoce su food cost real», «solo el 2 % aplica escandallos») se descartaron** al no poder verificarlas: **no deben aparecer en el producto**.

**La reseña 1★ es el brief del producto en una frase:** si esta guía dedica un tercio a explicar qué es un escandallo y qué es la matriz 2×2, ya está escrita la reseña que nos van a poner.

---

## 7. Entregables — la lista DEFINITIVA

**Ruta de entrega:** `astro-site/public/dl/guia-food-cost-ingenieria-menu/`
**Motor de documentos:** `scripts/productos-digitales/guias-v2_0/documentos.py` + `guion_guia_food_cost_ingenieria_menu.py` nuevo (cero cambios de código, L5 §4.1).
**Motor de texto:** `bridge.py` con `--model ~deepseek/deepseek-v4-flash-latest --max-tokens 8192` (regla capital + gotcha del Mac). **Ninguna línea de contenido la escribe Claude.**

### 7.1 Documentos

| Fichero | Qué es | Objetivo medido |
|---|---|---|
| `guia-food-cost-ingenieria-menu.pdf` + `.docx` | La guía, **20 capítulos** | **~28.000 palabras → 60+ páginas**, ver calibración abajo |
| `BONUS-20-ejercicios-resueltos.pdf` + `.docx` | 20 ejercicios resueltos paso a paso (escandallo con merma, PVP por 4 métodos, clasificación de una carta con los 3 modelos, repricing de delivery, coste por lote, prime cost) | ~6.000-7.000 palabras → **~16-18 páginas** (referencia medida: el bono del kit son 6.848 palabras → 17 páginas) |

**Calibración de páginas (medida el 2026-08-29 con la maqueta real, `guias-v2-SPEC.md` §5.1, NO estimada):** un Markdown de 37.295 palabras con 33 tablas produce **73 páginas** sin saltos (499 palabras/página) y **90 páginas** con `PageBreak` por capítulo + portada + índice (**410 palabras/página**). Con nuestro pipeline (que sí usa `PageBreak`), la aritmética honesta es:

- 20 capítulos × 1.400-1.500 palabras = **28.000-30.000 palabras**
- 28.000 / 410 = **68 páginas** · 30.000 / 410 = **73 páginas**
- **Promesa de landing: «60+ páginas»** — se cumple con margen y **el gate lo MIDE con PyMuPDF**, no se estima. (Para prometer «80+» habría que subir a ~33.000 palabras: es una decisión de John, §17 nº6, con coste de tokens.)

Comparativa interna para calibrar la promesa: `guia-restaurante-gastronomico` promete 80+ (22 capítulos, ~37.000 palabras) y las guías de 65 € prometen 60+ (20 capítulos, ~28.000). **Esta guía se sitúa exactamente en el molde de las de 60+.**

### 7.2 Herramientas Excel

De los 10 ejemplos que se plantearon, **L5 descartó 3 por duplicación verificada** (análisis por familias — ya existe idéntico; food cost teórico vs real semanal — ya está en 3 ficheros del kit; pastelería por lote — duplica `05-pasteleria.xlsx`). Quedan **7 nuevas + 1 de decisión**:

| # | Fichero | Hojas | Qué DECISIÓN permite tomar | Qué reutiliza (motor existente) |
|---|---|---|---|---|
| 1 | **`matriz-multimetodo-carta.xlsx`** ⭐ el diferenciador | `Datos` · `Kasavana-Smith` · `Miller` · `Pavesic` · `Comparativa` | Cuando los 3 métodos coinciden en marcar un plato, es señal de alta confianza para reformular/retirar sin más análisis; cuando **discrepan** (típico del marisco: margen absoluto alto, food cost % pobre), la señal es que hace falta juicio, no otra fórmula | La hoja `Menu Engineering` completa de `menu-engineering-matrix.xlsx` (columnas A-M, umbral 70 %/N por familia) entra **tal cual** como hoja «Kasavana-Smith» |
| 2 | **`simulador-repricing-multicanal.xlsx`** | `Carta` · `Multicanal` · `Resumen` | Cuánto subir el precio en cada canal sin perder margen tras comisión, y **qué platos excluir del delivery** porque no aguantan la comisión | `PVP = coste/(FC_obj × (1−comisión))` de `10-calculadora-pvp.xlsx!G18`, **escalada de una fila a toda la carta** |
| 3 | **`precio-objetivo-multi-metodo.xlsx`** | `Por plato` con 4 columnas de PVP: Factor · Margen objetivo en € · Mercado · Valor percibido | Qué método usar según el plato: factor para volumen, **margen en € para proteger el beneficio absoluto** en platos caros, mercado para anclar a la zona, valor para producto con historia | El panel «Factor» es literalmente `escandallo-maestro!H30` y `10-calculadora-pvp` |
| 4 | **`rendimiento-mermas-producto.xlsx`** | `Test de Rendimiento` · `Mi Tabla de Mermas` | Sustituir la merma **genérica de tabla** («pescado 35 %») por la **medida con tu proveedor y tu cuchillo**, y decidir si compensa aprovechar subproductos (`Coste neto/kg = (Precio×Bruto − Valor subproductos)/Limpio`) | La convención `D/(1−F)` de `escandallo-maestro` en sentido inverso, y el **formato exacto** de la hoja `Mermas` del kit para poder pegarlo ahí |
| 5 | **`cuadro-de-mando-prime-cost.xlsx`** | `Mensual` (12 filas: food cost %, labor cost %, prime cost %, semáforo) | Ver food cost y personal **juntos**: hoy **ningún fichero del catálogo cruza los dos**, y un food cost «bueno» puede esconder un labor cost descontrolado | `11-dashboard-food-cost-mensual.xlsx!H7` + convención de SS al 33 % en celda de `plantilla-turnos-brigada` |
| 6 | **`carta-de-bebidas-beverage-cost.xlsx`** | `Vinos` · `Cervezas y NA` · `Destilados y Cócteles` · `Resumen Bodega` | Gestionar la bodega como **cuenta de resultados propia** (hoy solo hay 4 cócteles sueltos en el kit) y aplicar **el IVA correcto por canal** | Patrón «Formatos de Compra» (botella→€/L) de `04-cocktails-bebidas.xlsx`; **reproduce literalmente la nota legal de `escandallo-maestro!I31`** (§2.3) |
| 7 | **`plan-accion-90-dias.xlsx`** | `Decisiones` · `Calendario 90 días` · `KPI de seguimiento` | Da **orden de ejecución** a las salidas de las otras 6: convierte el análisis en algo con fecha y responsable | Patrón ✓/—/N/A de `06-catering.xlsx!Checklist Evento` + Gantt de `cronograma-apertura-gantt.xlsx`. **Declara en su primera hoja que NO es el plan de 4 semanas del bono del kit** (trimestral y de carta, no diario y de disciplina) |
| 8 | **`ficha-escandallo-base.xlsx`** ⚠️ **decisión de John** | `Ficha (plantilla)` para duplicar + `Resumen` | Que la guía sea **autosuficiente**: sin coste por ración, las 7 herramientas de arriba no tienen input | Sería la hoja `Ficha (plantilla)` de `escandallo-maestro.xlsx` v2.0 **sin las 11 plantillas por formato del kit**. Ver §17 nº2 |

**Total propuesto: 2 documentos (guía + bonus) × 2 formatos + 7 u 8 xlsx.** Comparable en volumen al paquete de las guías de 65 € (20 capítulos + 10 plantillas + 8 checklists), pero **con densidad técnica mucho mayor por fichero**: aquí no hay checklists de relleno, son 7-8 libros con fórmulas.

### 7.3 Lo que se reutiliza y lo que NO se construye (para que nadie lo pida dos veces)

- ✅ **Se reutiliza el motor**, no el fichero: `menu-engineering-matrix.xlsx` entra como una hoja dentro de la herramienta 1; `escandallo-maestro.xlsx` aporta la fórmula de coste por ración; `10-calculadora-pvp.xlsx` aporta la del PVP con comisión; `11-dashboard-food-cost-mensual.xlsx` la del food cost real.
- ❌ **NO se construye**: análisis de carta por familias (ya existe idéntico), food cost teórico vs real semanal (ya está en 3 ficheros), pastelería por lote (duplica `05-pasteleria.xlsx`; lo único que le falta —escalado de tanda— es una mejora del fichero existente, tarea del kit).
- ❌ **NO se repite en el texto**: la negociación con proveedores. El bono del kit ya trae **7 tácticas completas + guion de llamada línea a línea**. Si la guía toca compras, tiene que ir a otro nivel (contratos indexados, gestión del riesgo de volatilidad, condiciones de pago a escala de grupo), no repetir las mismas 7.

---

## 8. Precio sugerido y comparables

### 8.1 La escalera propia

| Producto | Precio | Qué es |
|---|---|---|
| eBook Pro Prompts | 9 € | 200+ prompts |
| **Kit de Escandallos Pro** | **12 €** | 11 plantillas + bono de 17 páginas |
| Kits de tareas | 12-18 € | Checklists operativos |
| Planes de negocio | 29-55 € | Plan + financiero por formato |
| Guía Dark Kitchen | 24 € | 13 capítulos, +40 páginas |
| **Guías «Cómo Montar»** | **65 €** | 20 capítulos, 60+ páginas, 10 plantillas + 8 checklists |
| **Guía Restaurante Gastronómico** | **85 €** | 22 capítulos, 119 páginas, 10 plantillas |

Ancla interna útil: **nuestra propia landing del kit valora su bono de food cost de 17 páginas en 27 €** (`kit-escandallos.ts:257`; la tarjeta de ChefBusiness dice 29 €). Es una cifra de marketing, no de mercado, pero fija el lenguaje de valor de la casa: 17 páginas de food cost = 27 €.

### 8.2 Los comparables externos medidos (L1)

| Ancla | Cifra | Por qué importa |
|---|---|---|
| **SaaS de food cost** | **95 €/mes + IVA** (tSpoonLab, Haddock) = **1.140 €/año** | Es el ancla más fuerte y **está confirmada en dos fuentes independientes** |
| Plantilla Excel suelta de ingeniería de menú | 15,75 € · 9 USD | Techo de lo que hoy se paga por «solo el Excel» |
| Manual corto | 6,75 € (Formahostel) | Suelo del mercado |
| Curso grabado con descuento | 29 € (Aprendum, **acceso solo 3 meses**) / 100 € (taller presencial 6 h) | Precio psicológico de la categoría |
| Libro de gestión del nicho | 38,60 € tapa blanda / 65,50 € tapa dura (*Cocinando Rentabilidad*) | Techo del formato «texto sin herramienta» |
| Máster F&B | 8.200-11.800 € | El mismo temario, empaquetado como título |

### 8.3 La propuesta

> ### **49 €** · precio de lanzamiento · ancla `priceOld` **140 €** (−65 %)

**Por qué 49 € y no otra cosa, en una frase por argumento:**

1. **Es la franja que L1 recomienda (39-49 €) por ser la que explota los 6 huecos sin canibalizar** ni al Kit de 12 € ni a la Guía de 85 €.
2. **El argumento de venta es aritmético y verificable, no marketing:** 49 € es el **4,3 % de lo que cuesta un año** de la función equivalente en Haddock o tSpoonLab (1.140 €/año, confirmado con URL), **y es tuyo para siempre**.
3. **Respeta la escalera:** queda 4× por encima del Kit (12 €) —lo bastante para que se note que es otra cosa— y por debajo de las guías «Cómo Montar» (65 €), que traen 10 plantillas + 8 checklists + business plan. Poner esta al mismo precio que aquellas obligaría a igualar el recuento de entregables, no la densidad.
4. **Es coherente con nuestro propio lenguaje de valor:** si 17 páginas de food cost las valoramos en 27 €, 60+ páginas con 7-8 libros de Excel a 49 € es una progresión que el cliente que ya compró el kit entiende sin explicación.
5. **La franja 39-49 € no tiene comparables directos en el censo** — es zona sin anclas de mercado visibles, así que **la landing tiene que construir la comparación** (kit barato ↔ SaaS caro) en lugar de apoyarse en «así lo vende la competencia».

**Alternativas, con su coste honesto:**

- **55 €** — lo pone en el techo de la banda de planes de negocio. Defendible, pero pierde el redondeo psicológico y el argumento «menos de la mitad de lo que pagas cada mes por el software» se vuelve más discutible (55/95 = 58 %).
- **65 €** — paridad con las guías «Cómo Montar». **Solo defendible si el paquete iguala su recuento** (habría que subir a 80+ páginas y añadir checklists), lo que sube el presupuesto de tokens de la semana B.
- **35 €** — capta más volumen y compite de frente con el curso de 29 €, pero **estrecha demasiado el hueco contra el Kit de 12 €** y desperdicia el ancla del SaaS.

**El `priceOld` de 140 €** mantiene la profundidad de descuento de la familia (dark-kitchen 24/90 = −73 %; guías 65/180 = −64 %; gastronómico 85/220 = −61 %) sin exagerar.

---

## 9. Índice de capítulos propuesto (20 capítulos)

Cada capítulo va con guion cerrado en `guion_<pid>.py` (epígrafes + cifras que debe citar del propio producto + tablas exigidas), según §5.2 de la SPEC. Presupuesto: **1.400-1.500 palabras/capítulo**.

| # | Título | En una línea |
|---|---|---|
| 01 | **Para quién es esta guía (y qué NO vas a encontrar aquí)** | Nivel de partida, mapa de decisión por problema, y por qué no volvemos a explicar qué es un escandallo. |
| 02 | **Las cuatro cifras que gobiernan tu carta** | Food cost %, margen de contribución en €, prime cost y ticket medio: qué mide cada una y cuál manda en cada decisión. |
| 03 | **IVA, base imponible y el error que invalida tu food cost** | El 10 % del art. 91.Uno.2.2 (también el alcohol en sala), el 21 % de la venta para llevar, y por qué el % se calcula sobre venta neta. |
| 04 | **El coste real de compra: 4 %, 10 % y 21 % en el mismo albarán** | Cómo registrar el IVA soportado por partida para que el coste neto sea el de verdad. |
| 05 | **Del bruto al neto: merma, rendimiento y el test que sustituye a la tabla** | Merma de despiece, de cocción y desperdicio; por qué la tabla genérica te miente y cómo medir la tuya. |
| 06 | **La ficha de escandallo que aguanta una auditoría** | Cantidad neta → bruta con `D/(1−F)`, raciones, subproductos aprovechables y coste por ración. |
| 07 | **Food cost teórico vs real: dónde se escapa el dinero** | Las cuatro causas de la desviación y el protocolo semanal para localizar cuál es la tuya. |
| 08 | **Prime cost: la métrica que de verdad mide la salud del negocio** | Food cost + personal, el umbral del 60 %, y por qué un food cost «bueno» puede estar tapando el problema. |
| 09 | **Cuatro formas de poner precio a un plato** | Factor, margen objetivo en €, precio de mercado y valor percibido: cuándo usar cada una y cuándo el factor te arruina el marisco. |
| 10 | **Psicología de precios: lo demostrado y lo que es leyenda** | Nombres descriptivos (+27 %, Wansink 2001), símbolo de moneda (Cornell 2009), efecto señuelo; y lo que circula sin estudio detrás. |
| 11 | **Ingeniería de menú I — Kasavana & Smith bien hecho** | La matriz, el umbral 70 %/N y por qué se calcula **por familia** y no sobre la carta entera. |
| 12 | **Ingeniería de menú II — lo que la matriz clásica no ve** | Miller, Pavesic (margen ponderado), Hayes & Huffman (Goal Value) y LeBruto (con mano de obra): qué añade cada uno. |
| 13 | **Cuando los métodos discrepan: el protocolo de decisión** | Reformular, resubir, rediseñar o retirar — plato a plato, con criterio y no con una fórmula más. |
| 14 | **Carta corta y menú de precio fijo** | Cuántos platos aguanta tu cocina, cómo se poda sin perder ventas, y cómo se escandalla un menú donde el margen lo decide el mix. |
| 15 | **Multicanal: sala, take away y delivery** | Comisión de plataforma, packaging y precio diferenciado: cómo evitar vender a pérdida en la app. |
| 16 | **Beverage cost: la bodega como cuenta de resultados propia** | Vinos, cerveza, destilados y cócteles con sus rangos, su IVA correcto y su margen ponderado. |
| 17 | **Costeo por lote en obrador y pastelería** | Rendimiento de la tanda, mano de obra por hora, packaging y escalado de 12 a 200 unidades. |
| 18 | **Cuando sube el proveedor: protocolo de re-escandallado** | Cada cuánto se re-escandalla, qué dispara una revisión inmediata y cómo se sube el precio sin perder al cliente. |
| 19 | **Caso integral: una carta entera, de principio a fin** | Los 12 platos de ejemplo del propio libro, escandallados, clasificados por los 3 métodos y repricing multicanal — con las cifras que salen de nuestros xlsx, no de un cliente inventado. |
| 20 | **Cuándo tu Excel se queda corto** | Hoja de ruta Excel → software de food cost → agentes de IA, con el criterio para decidir el salto (y lo que cuesta cada escalón). |

**Cobertura de los 15 huecos de la SERP:** IVA (03, 04) · delivery (15) · beverage cost (16) · pastelería (17) · inflación y re-escandallado (18) · alternativas a Kasavana & Smith (12) · prime cost (08) · mermas por técnica (05) · escandallo + ingeniería de menú integrados (19) · food cost por canal (15) · menú del día vs carta (14) · psicología con profundidad (10) · reingeniería periódica (18) · casos con cifras (19) · plantilla completa (los entregables).

**Regla de honestidad para el capítulo 19:** el caso se construye **con los datos de ejemplo de nuestros propios xlsx** y se etiqueta como caso modelado. **No se presenta como cliente real.** (El bono del kit ya tiene su caso 35,36 %→31,8 %; este es otro, a 90 días y con las palancas nuevas — no se recicla.)

---

## 10. Nombre, slug y posicionamiento

### 10.1 Nombre comercial

> **«Guía Food Cost + Ingeniería de Menú»**

Se mantiene el nombre que ya está en el calendario (`CALENDARIO-V2-SEMANAL.md` §3 nº1) y en la decisión de John del 31-ago. Razones: los dos términos están **unificados en los cuatro mercados** (España, México, Argentina, Colombia — L4 §2), los dos son los que el comprador reconoce, y juntos declaran exactamente el alcance.

**Subtítulo para hero/SEO:** «Escandallo, precios y rentabilidad de tu carta — con IVA español y delivery» — mete «escandallo» donde sí suma (en el texto, para la SERP y para el lector español) sin meterlo en la URL.

### 10.2 Slug

> **`guia-food-cost-ingenieria-menu`** → `https://aichef.pro/guia-food-cost-ingenieria-menu`

| Candidato | Veredicto |
|---|---|
| **`guia-food-cost-ingenieria-menu`** | ✅ **Recomendado.** Declara el alcance completo, empieza por `guia-` (ver 10.3), no pisa a `kit-escandallos` |
| `guia-escandallos-pro` / `guia-escandallo-food-cost` | ❌ **Descartado.** «escandallo» es el único head term con volumen (5.400/mes) **y ya lo ocupa `/kit-escandallos` en posiciones 8-15 de GSC**. Una segunda landing con ese término compite contra nuestro activo que ya rankea |
| `guia-food-cost` | ⚠️ Más corto y limpio, pero deja fuera la mitad del producto. Segunda opción si John quiere URL corta |
| `guia-ingenieria-de-menu` | ⚠️ Cubre el término mejor posicionado en México (90/mes) pero pierde el food cost. Tercera opción |
| `food-cost-pro`, `menu-engineering-pro` | ❌ **Descartado por infraestructura**, ver 10.3 |

### 10.3 Por qué el prefijo `guia-` no es cosmético (verificado en el repo)

`astro-site/public/robots.txt` protege la zona de pago con reglas **ancladas al prefijo de cada familia de producto** (`/kit-*-library`, `/guia-*-access`…) precisamente porque el 2026-08-27 un comodín mal entendido **bloqueó 26 posts ingleses durante casi un mes sin dar un solo aviso**. Un slug que empiece por `guia-` cae dentro de las reglas existentes: la página de acceso `/guia-food-cost-ingenieria-menu-access` queda bloqueada a robots y excluida del sitemap **sin tocar nada**. Un slug tipo `food-cost-pro` obligaría a **añadir dos líneas nuevas a `robots.txt`** y a correr `robots-gate.py`; si se olvidara, la zona de pago quedaría indexable.

**Aun así, y aunque el prefijo sea el correcto, hay que correr `python3 scripts/astro-migration/robots-gate.py` antes de publicar.** Es un comando y aquí ya ha costado un mes de indexación.

### 10.4 Posicionamiento en una frase

> **El método que convierte tus escandallos en decisiones de carta.** Lo que en un máster de F&B de 8.200 € es un módulo, y lo que un software de 95 €/mes te calcula sin explicarte por qué, aquí es un documento tuyo para siempre, con el IVA español bien puesto y el delivery dentro de la cuenta.

---

## 11. Vocabulario ES / LATAM (decisión ya tomada por el research)

**No se hacen versiones por país** (coherente con la decisión de tienda única de John, 31-ago). Se usa un vocabulario que funcione en los cuatro mercados:

| Concepto | Término principal | Sinónimo entre paréntesis, primera mención |
|---|---|---|
| Cálculo del coste de un plato | **Escandallo** | **(costeo de recetas)** — cubre España sin dejar fuera a LATAM, que reconoce «costeo» de inmediato |
| % de coste sobre venta | **Food cost** | (CMV) una sola vez, para el lector argentino de perfil contable |
| Documento de receta con cantidades y coste | **Ficha técnica** | (receta estándar) |
| Precio final | **Precio de venta** | (PVP) — «PVP» es jerga de España; en LATAM se entiende pero no se usa |
| Un plato del menú | **Plato** | «platillo» **solo** como aclaración regional en el glosario — **no como término por defecto**: suena forzado en España y Argentina |
| La lista de platos | **Carta** | (menú) — en México «menú» es lo cotidiano |
| Análisis de rentabilidad + popularidad | **Ingeniería de Menú** | (menu engineering) en la primera mención |
| Pérdida de producto | **Merma** | universal en los 4 mercados, no hace falta adaptar |
| Comisión de reparto | **Delivery** / comisión de plataformas | mencionar **Rappi y DiDi Food** explícitamente en los ejemplos de México |
| Impuesto | **IVA** | mismo acrónimo en los 4 mercados, **pero el % y las reglas cambian → la casilla va editable, nunca fija** |

---

## 12. Diferenciación explícita (esto va en la landing, no solo aquí)

### 12.1 Frente al **Kit de Escandallos Pro (12 €)** — la frontera es de MÉTODO, no de tamaño

| | Kit de Escandallos Pro · 12 € | Guía Food Cost + Ingeniería de Menú · 49 € |
|---|---|---|
| Qué es | **Plantillas para escandallar** | **Método, análisis y decisión** |
| Metodologías de clasificación de carta | **0** — no clasifica, solo costea | **3** cruzadas (Kasavana-Smith + Miller + Pavesic) con columna de discrepancia |
| Formas de fijar precio | 1 (coste/FC, por tipo de negocio) | **4** (factor, margen en €, mercado, valor), por plato |
| Merma | Tabla de referencia genérica (21 categorías) | **Protocolo de test de rendimiento con TU proveedor**, medido |
| Bebidas | 4 cócteles sueltos | **Carta de bodega completa como P&L**, con el IVA correcto |
| Delivery | Una fila en la calculadora de PVP | **Simulador multicanal por plato**, con packaging y comisión |
| Prime cost | No existe | **Cuadro de mando mensual** food + personal |
| Horizonte | Semanal/mensual (disciplina) | Trimestral (decisiones de carta y contrato) |
| Bono | 30 días, táctico, con negociación de proveedores a fondo | 90 días, estratégico, **ejecuta** las decisiones de la matriz — **no repite** la negociación |

**La frase para la landing:** *«El Kit te dice cuánto te cuesta cada plato. La Guía te dice qué hacer con esa información.»*

### 12.2 Frente a la **Guía Cómo Montar un Restaurante Gastronómico (85 €)**

Son productos de **eje distinto**: aquella es una guía de **apertura de un negocio concreto** (22 capítulos: licencias, obra, brigada de 12-17 personas, Michelin, inversión de 500-900 k€); esta es una guía de **una disciplina, para un negocio que ya está abierto**, sea del formato que sea.

- La de 85 € incluye `escandallo-maestro.xlsx` y `menu-engineering-matrix.xlsx` **como dos de sus diez plantillas**; aquí la ingeniería de menú **es el producto**, y se entrega con tres metodologías, no una.
- El comprador es distinto: allí, quien **va a abrir**; aquí, quien **ya opera** y le está desapareciendo el margen.
- **Quien tenga las dos no compra nada repetido**: la matriz de la guía gastronómica entra aquí como **una hoja de cinco** dentro de la herramienta multi-método.

### 12.3 Frente al contenido gratuito (la objeción honesta)

Hay decenas de plantillas de escandallo gratuitas y la SERP cubre bien «qué es un escandallo» y «qué es la ingeniería de menú». **No se puede negar y no se debe intentar.** El producto empieza **donde termina el contenido gratuito**: los 7 huecos que ninguna de las 18 fuentes cubre (IVA, delivery, beverage cost, re-escandallado, prime cost, alternativas a Kasavana & Smith, escandallo + ingeniería integrados en un mismo caso), más los ejercicios resueltos, más las herramientas con fórmulas vivas.

---

## 13. Cross-sell (en las dos direcciones, y medible)

| Desde | Hacia | Cómo |
|---|---|---|
| **Bono de 30 días del kit** (Semana 2, «ingeniería de menú básica») | Guía nueva | Nota de 2-3 frases: «esta clasificación usa una sola metodología; cruzarla con Miller y Pavesic y ver dónde discrepan es lo que trae la Guía Food Cost + Ingeniería de Menú». Edición pequeña sobre fichero existente ⚠️ **aprovechando la misma pasada que corrige el IVA (§2.3)** |
| **Guía nueva**, capítulo 06 | Kit de Escandallos Pro (12 €) | «Si aún no tienes cada plato escandallado, hazlo primero con el Kit — 11 plantillas por formato, 12 €» |
| **Guía nueva**, capítulo 08 | Kit Gestión de Personal y Turnos (14 €) | El labor cost del prime cost sale de ahí |
| **Guía nueva**, capítulo 20 | Plataforma (agentes de IA) + suscripción | El salto Excel → software → agentes |
| **Guía Restaurante Gastronómico (85 €)**, cap. 15 | Guía nueva | Quien monta un gastronómico querrá la profundidad de carta |
| **Los 6 posts de blog** de food cost/escandallo/mermas | Guía nueva | Banner fijado por relevancia + enlace contextual |
| **Landing nueva** | Kit + Kit Personal | Banner cruzado con `utm_source=landing&utm_medium=cross-sell` para poder medir quién compra los dos |

---

## 14. FAQ del producto (12 preguntas, todas con demanda medida)

Las 4 primeras salen del **People Also Ask real** de Google España; las 8 siguientes, de preguntas repetidas en el corpus de 18 fuentes o de huecos que **nadie responde bien** (por tanto, sin competencia gratuita ya posicionada).

1. **¿Qué es un escandallo en hostelería, y en qué se diferencia de un escandallo de costes o de producto?** *(PAA)*
2. **¿Cómo se calcula el escandallo de un plato, paso a paso?** *(PAA)*
3. **¿Cuál es el food cost ideal?** *(3/18 fuentes, con rangos distintos entre sí → aquí se explica por qué varía y se dan los rangos por formato con su fuente)*
4. **¿Qué diferencia hay entre food cost teórico y food cost real, y cómo mido la desviación?** *(hueco: solo 1/18 lo nombra, ninguna enseña a medirlo)*
5. **¿Cómo afecta el IVA al cálculo del food cost? ¿Se calcula sobre el precio de carta o sobre la base imponible?** *(hueco grave: 0/18 fuentes lo explican)*
6. **¿Las bebidas alcohólicas llevan el 21 % en un restaurante?** *(no: el 10 % también en sala, art. 91.Uno.2.2 — y es la pregunta que corrige nuestro propio bono)*
7. **¿Cómo calculo el food cost real de un plato vendido por delivery, descontando la comisión?** *(hueco: 0/18)*
8. **¿Cuál es el food cost objetivo de las bebidas y por qué es distinto al de la comida?** *(hueco, con el matiz de CaixaBank: la bebida sale al 34,5 % frente al 28 % de la comida)*
9. **¿Con qué frecuencia hay que re-escandallar una receta?** *(hueco: ninguna fuente da protocolo)*
10. **¿El método de Kasavana & Smith es el único válido?** *(hueco: se cita en 7/18 como si lo fuera; solo un paper académico menciona alternativas)*
11. **¿Cómo se calcula el prime cost y por qué importa más que el food cost solo?** *(hueco: 0/18)*
12. **¿Necesito comprar el Kit de Escandallos si compro esta guía?** *(objeción nº5 medida en L4 — se responde con la jerarquía del §12, no con marketing)*

---

## 15. Riesgos

| # | Riesgo | Evidencia | Mitigación |
|---|---|---|---|
| 1 | **La demanda SEO es pequeña y la landing no captará por búsqueda** | Volúmenes del §0; «guia food cost» = 0 | Asumido y planificado: el canal son los banners en 325 posts, la lista de clientes, el hub y la plataforma (§0). **No prometer tráfico orgánico a esta landing** |
| 2 | **Canibalización interna** con el Kit (12 €) y la Guía Gastronómico (85 €) | L4 objeción nº5; L5 §6.1 | Jerarquía explícita en la landing y en el capítulo 01 (§12). Sin ella, el catálogo se hace la competencia a sí mismo |
| 3 | ⚠️ **Contradicción viva con nuestro propio producto: el bono del kit dice 21 % de IVA** | `bono-guia-food-cost-30-dias.md:630`, publicado hoy | **Corregirlo antes o durante este lanzamiento** (§17 nº3). Si no, el cliente lee dos verdades opuestas nuestras |
| 4 | **La reseña 1★ ya está escrita si repetimos lo básico** | Reseña real: «un tercio de las páginas explicando matrices básicas» | Capítulo 01 declara el nivel; el contenido gratuito se **cita y se salta**, no se reescribe |
| 5 | **Datos sin fuente sólida colándose en el texto** | L3 declara 9 huecos: marisquería 40-42 %, IPC exacto de agosto 2026, tabla de mermas con autoría, tarifario oficial de delivery, año de Miller, anclaje «+8,2 %», caso Gregg Rapp, desperdicio México | Regla «sin fuente, no entra» (§7-bis.21) + el gate de coherencia de cifras de `documentos.py`. **Los 9 van en una lista negra explícita del `guion_<pid>.py`** |
| 6 | **Regenerar pisa ediciones manuales** | Gotcha conocido: los ensambladores reconstruyen el cuerpo desde el `.txt` de bridge | Diff de enlaces antes de regenerar cualquier cosa ya publicada |
| 7 | **Presupuesto de tokens** | Regla de John: 1 producto/semana, techo ~15 % de la cuota; el método son 3 sesiones (A research / B entregables / C lanzamiento) | Esta sesión cierra la **A**. La B (8 xlsx + 2 documentos + gates) es la cara: no meter nada más en esa semana |
| 8 | **8 libros de Excel sin verificar en pycel** | L5 lo declara: son propuestas de diseño, no ficheros | La verificación de fórmulas es un gate obligatorio de la semana B, no un «ya se verá» |
| 9 | **`robots.txt` / sitemap** | El comodín borró 26 posts en agosto | El prefijo `guia-` ya está cubierto, pero **correr `robots-gate.py`** igualmente |
| 10 | **Promesa de páginas incumplida** | 6 de las 8 guías de la familia llegaron a tener el PDF en una portada | El gate mide con PyMuPDF; **la promesa se pone después de medir**, no antes |
| 11 | **Vender profundidad LATAM que no tenemos** | El research fiscal es **solo español**; no hay research verificado de IVA/IEPS por país | O se hace research aparte (§17 nº5) o **la landing no promete fiscalidad LATAM**: promete casillas editables y vocabulario neutro |

---

## 16. Lo que este research NO pudo medir (para que nadie lo dé por sabido)

- **Reddit, Quora, Udemy y comentarios de YouTube: bloqueados** por la herramienta (403 / fetch denegado). No hay voz cruda de foro. Facebook, solo el título de un post.
- **Sin cita textual de ningún restaurantero mexicano con nombre**, pese a búsquedas dirigidas.
- **Precio exacto de 7 de los 23 productos censados** (Amazon bloqueó el fetch en varios, CESAE y Hotmart ocultan precio, los SaaS enterprise cotizan bajo demanda). Ninguna cifra se estimó.
- **Findus, Truyol y Gosufra** quedaron fuera del mapa de cobertura de la SERP (timeouts / sin contenido en español). **Hosteltáctil** devolvió solo el H1 (render JS).
- **El PDF oficial de tipos de IVA de la AEAT** no se pudo leer (binario comprimido): el listado 4/10/21 se sostiene en el BOE + tres fuentes fiscales coincidentes.
- **La cifra interanual exacta del IPC de alimentos de agosto 2026** no está publicada en la nota consultada. Se usa la de febrero 2026 (3,2 %), que es el último dato exacto.
- **No se ha comprobado en GSC (`page` × `query`) si los 6 posts propios canibalizarían la landing nueva.** Es un chequeo de 5 minutos que conviene hacer antes de la semana C.

---

## 17. Decisiones que solo puede tomar John

1. **Precio final.** Recomendado **49 €** (`priceOld` 140 €). Alternativas: 55 € / 65 € (esta última exige subir a 80+ páginas y añadir checklists) / 35 €.
2. **¿Se incluye `ficha-escandallo-base.xlsx` en el `dl/`?** Con ella la guía es **autosuficiente** (las otras 7 herramientas necesitan un coste por ración como input); sin ella, el comprador que no tenga el Kit ni la Guía Gastronómico se queda a medias y aparece la objeción «encima tengo que comprar otro producto». Coste: le quita un poco de exclusividad al Kit de 12 €.
3. **¿Se corrige el IVA del bono del kit (`bono-guia-food-cost-30-dias.md:630`, y sus PDF/DOCX publicados) antes o durante este lanzamiento?** Hoy hay un dato incorrecto vivo en un producto que vende. Mi recomendación: **sí, en la misma pasada** que añade el cross-sell (§13).
4. **Nombre y slug definitivos**: `guia-food-cost-ingenieria-menu` (recomendado) vs `guia-food-cost` vs `guia-ingenieria-de-menu`. **Si se elige un slug que no empiece por `guia-`, hay que añadir dos líneas a `robots.txt`.**
5. **¿Anexo LATAM en la v1?** Hoy **no tenemos** research fiscal verificado de México/Argentina/Colombia. Opciones: (a) v1 solo España con casillas de IVA editables y vocabulario neutro —lo que este research sí respalda—; (b) research aparte y anexo en una v1.1.
6. **Promesa de páginas: 60+ (recomendado, ~28.000 palabras) o 80+ (~33.000 palabras)** — la segunda sube el gasto de tokens de la semana B.
7. **¿El bonus «20 ejercicios resueltos» va dentro del producto o se usa como lead magnet** para captar lista? Hay demanda medida de «menú engineering ejercicios resueltos» (búsqueda relacionada en la SERP).
8. **Capa comercial:** ¿testimonios y ratings nuevos para esta landing, o se mantiene la política vigente de **no tocar** la capa comercial (orden del 29-ago)? Un producto nuevo no tiene testimonios reales que copiar.
9. **¿Entra en la rotación de banners como producto 45?** Implica reejecutar `fase8e-banners-corpus.py` sobre los 325 posts ES (y decidir si se **fija** en los 6 posts temáticamente relevantes en vez de dejarlo a la rotación).
10. **Inglés nativo:** la decisión del 31-ago dice que **no se arranca hasta cerrar el ES**. ¿Se mantiene, o este producto (con demanda inglesa evidente: el hub `/en/food-cost-calculator-restaurant` ya recibe clics) es la excepción?

---

## 18. Si John da el OK, la siguiente sesión es esta

Según el método de 3 sesiones del calendario (§3), esta cierra la **Semana A**. La **B** sería:

1. `guion_guia_food_cost_ingenieria_menu.py` con los 20 capítulos, las cifras que cada uno debe citar (referenciadas a celda de los xlsx nuevos) y **la lista negra de los 9 datos sin fuente**.
2. Los 7-8 xlsx, reutilizando los motores identificados, verificados con pycel.
3. `documentos.py --producto guia-food-cost-ingenieria-menu` → bridge.py → gates (páginas con PyMuPDF, no-latinos, coherencia de cifras, paridad PDF↔DOCX, metadata).
4. Un refutador (opus, dos lentes en un prompt) + fixes (sonnet). **Nada de tres lentes opus: eso es lo que disparó el gasto en agosto.**

Y la **C**: landing sobre la plantilla existente, dashboard, function de descargas, Payment Link (lo crea John), entrada en `products-catalog.ts`, hub, banners, `robots-gate.py`, gate de flujo post-pago y gate LIVE.

