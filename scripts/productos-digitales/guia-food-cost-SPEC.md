# «Guía Food Cost + Ingeniería de Menú» — SPEC v1.0 (2026-09-03)

> Producto NUEVO de la línea «Guías técnicas Premium» de aichef.pro. Primer producto nuevo del ciclo de
> sesiones alternadas (decisión de John, 2026-08-31). John dio **luz verde total el 2026-09-03**
> («directamente a producción, a desarrollo, adelante») y delegó las decisiones abiertas del research.
> Fuentes de esta SPEC: `auditorias/guia-food-cost-RESEARCH-2026-09-03.md` (síntesis), las cinco lentes
> `guia-food-cost-research-L1..L5`, y la refutación `guia-food-cost-research-REFUTACION-2026-09-03.md`
> (veredicto «CORREGIR ANTES»: sus 21 puntos están resueltos uno a uno en §1).
>
> Fuente de verdad del CONTENIDO: esta SPEC + `guias-v2_0/guion_guia_food_cost_ingenieria_menu.py`.
> Fuente de verdad de las CIFRAS del texto: los xlsx de `astro-site/public/dl/guia-food-cost-ingenieria-menu/`
> (§7-bis.7 de la SPEC de guías: una sola fuente; el PDF cita celdas, no inventa).

## 0. Ficha del producto

| Campo | Valor |
|---|---|
| Nombre | **Guía Food Cost + Ingeniería de Menú** |
| Subtítulo (hero/SEO) | Escandallo, precios y rentabilidad de tu carta — con el IVA bien puesto y el delivery dentro de la cuenta |
| `productId` / slug | **`guia-food-cost-ingenieria-menu`** (prefijo `guia-` → cae en las reglas existentes de `robots.txt`, sin tocarlas) |
| Landing · access · library | `/guia-food-cost-ingenieria-menu` · `-access` · `-library` |
| Env var Stripe | `VITE_STRIPE_PAYMENT_LINK_GUIA_FOOD_COST` |
| Precio | **55 €** (IVA incluido para consumidor UE; Stripe con `automatic_tax`, `tax_behavior: exclusive` como la familia) |
| Ancla | **Sin `priceOld` ni `discountBadge`** (decisión D2). La caja de bonus enseña el desglose de lo que incluye, no un precio tachado |
| Entregables | 1 guía (PDF + DOCX) · 1 bonus de ejercicios (PDF + DOCX) · **8 libros de Excel** con fórmulas vivas |
| Público | Quien **ya opera** (chef, jefe de cocina, gerente, dueño, director de A&B, obrador, bar, consultor) y necesita decidir precios y carta. NO es una guía de apertura |
| Idioma/mercado | Español. **Fiscalidad española** (IVA); todas las casillas de IVA, comisiones y objetivos son **editables** para LATAM. Cifras en euros. Vocabulario neutro (§6) |
| Canal | Blog ES (enlaces contextuales + banner fijado en los 6 posts del tema), hub `/productos-digitales`, lista de compradores del Kit de Escandallos, plataforma. **No se promete tráfico SEO** |

## 1. Decisiones firmadas (resuelven la refutación; no se reabren al construir)

| # | Decisión | Resuelve |
|---|---|---|
| D1 | **Precio 55 €.** Escalera real: Kit Escandallos 12 € · Kit Plan Financiero 39 € (7 xlsx) · planes 29-55 € · guías «Cómo Montar» 65 € (20 caps + 8-9 xlsx + 6 checklists + 2 docx) · gastronómico 85 € · mega pack 89 €. Este paquete (guía 20 caps + 8 xlsx densos + bonus) queda **por debajo de las guías de 65 €** y **por encima del plan financiero de 39 €**. No es 49 € porque **49 € es el precio tachado del Kit** y chocarían en el hub | B3, B5 |
| D2 | **Sin precio tachado.** Un producto nuevo no tiene «precio anterior de 30 días» (art. 20 TRLGDCU / RDL 24/2021, ficha COM-13 de la familia). `pricing.priceOld` y `discountBadge` se omiten; `heroNote` = «Pago único · acceso vitalicio · actualizaciones incluidas». `bonusTotalLabel` describe el paquete sin inventar un valor | B4 |
| D3 | **Sin `aggregateRating`, sin reseñas JSON-LD y sin testimonios inventados.** El producto no ha vendido una unidad. La sección de testimonios de la landing se **oculta** cuando `testimonials.items` está vacío (cambio mínimo en `GuiaLandingPage.astro`, sin efecto en las 8 guías). Cuando haya compradores reales, se añaden | B10 |
| D4 | **Bloque fiscal corregido y verificado contra el BOE** (§3): aceite de oliva al **4 %** (RDL 4/2024, art. 91.Dos.1.1.º.g, desde 1-ene-2025; verificado 2026-09-03, `auditorias/guia-food-cost-verificacion-fiscal-2026-09-03.md` — no es la letra f, que es frutas/verduras/hortalizas/legumbres/tubérculos/cereales); matriz de IVA repercutido **3×3** {sala · take away · delivery} × {comida · refresco/azucarada · alcohol}: en sala todo al 10 % (art. 91.Uno.2.2.º); sin servicio (take away/delivery) es entrega de bienes → comida 10 %, bebida alcohólica 21 %, refresco/bebida con azúcares o edulcorantes añadidos 21 % (art. 91.Uno.1.1.º, redacción desde 1-ene-2021). En los xlsx la matriz vive en **celdas editables** y las fórmulas la leen por INDEX/MATCH; nunca un `IF` binario. La nota de `escandallo-maestro!I31` NO se copia fuera de su ámbito (sala) | A1, A2 |
| D5 | **Prime cost con umbral español**: personal 30-35 % + producto 30 % (CaixaBankLab × elBulliFoundation) → objetivo **≤ 65 % con servicio en mesa**, **≤ 55 % barra/autoservicio**. El 60 % de Toast se cita como referencia de EE. UU. El semáforo del cuadro de mando lleva el objetivo en celda editable sembrada con el valor español | A3 |
| D6 | **Matriz multi-método honesta**: Kasavana & Smith (popularidad × MC), Miller (popularidad × FC %), Pavesic (FC % × **MC ponderado por unidades**), **Goal Value de Hayes & Huffman** (hoja propia, no matricial), LeBruto como lectura. La hoja `Comparativa` NO vende «coincidencia = alta confianza»: enseña **dónde discrepan** y por qué (cada método mide dos de tres variables). La hoja Kasavana-Smith se **reconstruye** con fórmulas propias y otros datos de ejemplo; no se copia el fichero de la guía de 85 € | A4, A5, B2 |
| D7 | **Ficha de escandallo base incluida**, mínima (una hoja de ficha + instrucciones, sin el bloque `Resumen`/`INDIRECT` de la maestra). Hace el producto autosuficiente sin reempaquetar el activo de la guía de 85 € | B2, §17.2 |
| D8 | **Psicología de precios**: protagonista el efecto señuelo con estudio revisado por pares; Wansink 2001 se cita con la salvedad de la sanción posterior a su autor y la falta de replicación; Yang/Kimes/Sessarego 2009 se presenta como estudio en dólares con comensales de EE. UU. | A6 |
| D9 | **Bonus = 12 ejercicios resueltos** de 550-700 palabras con tabla (≈ 7.500 palabras → ~17 páginas medidas), no 20 de 300 | A7 |
| D10 | **Ninguna cifra de inflación** en el texto: el cap. 18 enseña a leer la nota mensual del INE y el Observatorio del MAPA. Lista negra del guion: marisquería 40-42 %, IPC de agosto 2026, «67 % no conoce su food cost», «2 % aplica escandallos», anclaje «+8,2 %», caso Gregg Rapp, tabla de mermas con autoría, tarifario «oficial» de delivery | A8, A9 |
| D11 | **Distribución en el blog: inserción quirúrgica**, no rotación. En los 6 posts del tema (`8-errores-que-destruyen-el-food-cost-en-tu-restaurante`, `food-cost-ia-escenarios-inflacionarios-2026`, `mejores-calculadoras-food-cost-ia-comparativa`, `escandallos-ia-cocina-profesional`, `carta-restaurante-rentable-ingenieria-menu-ia`, `que-son-las-mermas-en-cocina`) se **sustituye el banner menos afín** por el del producto nuevo (mismo `banner()` y UTM del ensamblador) y se añade un enlace contextual en el cuerpo. El producto entra además en `products-catalog.ts` para las rotaciones futuras. Un modo `--rebalancear` de `fase8e` queda como tarea futura, fuera de esta sesión | B1 |
| D12 | **Moneda y vocabulario**: cifras en euros (como todo el catálogo); «coste» con la aclaración «(costo)» en la primera mención del glosario; «escandallo (costeo de recetas)», «precio de venta», «plato», «carta (menú)». Mercados citados en ejemplos: España y, en delivery, Rappi/DiDi (MX) y PedidosYa (AR/UY/PA). La landing dice explícitamente: «fiscalidad española; casillas editables para otros países» | B6 |
| D13 | **FAQ de compra**, no definicional: compatibilidad (Excel, Google Sheets, Numbers — sin `INDIRECT` en los libros nuevos), actualizaciones («si cambia el IVA te llega la versión nueva, acceso vitalicio»), garantía 30 días, «¿necesito el Kit?», «¿sirve fuera de España?», y las de hueco temático (IVA en el food cost, delivery, beverage cost, re-escandallado, alternativas a K&S, prime cost) | B7 |
| D14 | **Hotel, buffet, banquete y catering** entran en el cap. 14 con epígrafe y ejemplo propios (menú de precio fijo: el margen lo decide el mix) | B8 |
| D15 | **Simulador multicanal con dirección explícita**: entradas = coste/ración, PVP sala actual sin IVA, tipo (comida/refresco/alcohol), comisión por canal, packaging €/pedido, platos por pedido, precio techo en la app; salidas = FC % efectivo por canal, PVP necesario para el FC objetivo, «¿viable?» comparando con el techo | B9 |
| D16 | **Cap. 20 reconciliado con la landing**: «esta guía te da el criterio; el software te da la automatización; el SaaS cuesta más de 1.100 € al año, IVA aparte, por local». No se vende la guía como sustituto funcional del software | B11 |
| D17 | **La landing publica la cifra de páginas MEDIDA** con PyMuPDF tras construir; la promesa interna del gate es 60 y el texto se dimensiona a ~30.000 palabras (20 caps × 1.400-1.600, con más margen para el 19) | B12, falta 9 |
| D18 | **Corrección del bono del Kit** (`bono-guia-food-cost-30-dias.md:630`: «alcohol 21 %»): se corrige con la matriz de D4 y se le añade la nota de cross-sell hacia esta guía, regenerando PDF con `bono_guia.py`. Se hace **al final de la sesión**, como pasada pequeña sobre otro producto, con censo y gate | §2.3, falta 12 |
| D19 | **Inglés**: no se arranca (decisión del 31-ago). Ninguna pieza EN | §17.10 |
| D20 | **Fiscalidad de la venta del producto** (OSS/IVA electrónico): Stripe ya cobra con `automatic_tax` en toda la familia; no es materia de esta SPEC | falta 11 |

## 2. Entregables (ruta `astro-site/public/dl/guia-food-cost-ingenieria-menu/`)

### 2.1 Documentos (pipeline `guias-v2_0/documentos.py` sin cambios de código)

| Fichero | Contenido | Objetivo |
|---|---|---|
| `guia-food-cost-ingenieria-menu.pdf` + `.docx` | 20 capítulos (§4) | ~30.000 palabras; ≥ 60 páginas medidas; gates §5.6 de la familia en verde |
| `BONUS-ejercicios-resueltos.pdf` + `.docx` | 12 ejercicios resueltos con tabla (§4.2) | ~7.500 palabras; ~17 páginas |

### 2.2 Los 8 libros de Excel

Convenciones de familia (obligatorias): helpers de `guias-v2_0/motor.py` (`f`, `val`, `verde`, `dv_lista`, `dv_porcentaje`, `semaforo_isnumber`, `escribir_parametro`, `PARAMETROS`, `version_line`); hoja «Instrucciones» primero (con «Celdas verdes = campos editables», la línea de versión `Versión 1.0 · septiembre 2026 · aichef.pro/guia-food-cost-ingenieria-menu · info@aichef.pro`, la bio anclada y la nota de desproteger); celdas verdes = entrada; parámetros normativos en celda verde con nota; **cero constantes tecleadas dentro de una fórmula** (IVA, comisiones, objetivos: siempre celda); `IFERROR(...,"")` y `ISNUMBER` en semáforos; «sin dato» = `""` nunca `0`; **prohibido `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`** (compatibilidad Sheets/Numbers y pycel); formato `#,##0.00 €`, `0.0%`; A4 apaisado con `print_setup`; datos de ejemplo coherentes entre libros (**la misma carta de 12 platos de ejemplo** aparece en la ficha, la matriz, el simulador y el caso integral del cap. 19); metadata `author='AI Chef Pro'`. Después de generar: `inject_cache.py` y verificación `data_only` de cada fórmula registrada.

| # | Fichero | Hojas | Entradas (verde) | Salidas (fórmula) | Decisión que permite |
|---|---|---|---|---|---|
| 1 | `ficha-escandallo-base.xlsx` | Instrucciones · Ficha | plato, familia, raciones, FC objetivo, IVA sala (param), 20 líneas: ingrediente, unidad, cantidad neta/ración, precio/ud sin IVA, merma % ; PVP actual en carta sin IVA | cantidad bruta `=D/(1-F)`, coste línea, coste total, coste/ración, PVP sin IVA objetivo, PVP con IVA, food cost real, margen € | Coste por ración: el input de todo lo demás |
| 2 | `rendimiento-mermas-producto.xlsx` | Instrucciones · Test de Rendimiento · Merma de Cocción · Mi Tabla de Mermas | 10 tests: producto, peso bruto, precio/kg bruto, peso limpio, kg y valor/kg de subproductos aprovechables · cocción: técnica, peso crudo, peso cocinado · tabla: categoría, merma de referencia (rangos del research con fuente), merma medida | rendimiento %, merma %, factor 1/rend, coste neto/kg `=(precio×bruto − subproductos)/limpio`, pérdida de cocción %, «la que usas» = medida si existe, si no referencia | Sustituir la merma genérica por la tuya; decidir si compensa aprovechar subproductos |
| 3 | `precio-objetivo-multi-metodo.xlsx` | Instrucciones · Por Plato | 15 platos: coste/ración, FC objetivo (param global y por plato opcional), margen objetivo €, precio de mercado de la zona, precio de valor percibido, método elegido (lista A/B/C/D) | PVP por cada método (A factor `=coste/FC`; B `=coste+margen`; C y D dan el FC resultante), PVP elegido (`INDEX` según método), PVP con IVA sala, margen €, FC % final, semáforo vs objetivo | Qué método usar según el plato; el factor arruina los platos de coste alto |
| 4 | `matriz-multimetodo-carta.xlsx` ⭐ | Instrucciones · Datos · Kasavana-Smith · Miller · Pavesic · Goal Value · Comparativa | 25 platos: nombre, familia (lista), uds vendidas, coste/ración, PVP sin IVA; parámetros: umbral de popularidad 70 %, labor % y otros variables % (Goal Value) | por familia con `SUMIF/COUNTIF/SUMPRODUCT`: mix %, umbral `=0,7/N_familia`, MC, MC medio ponderado, FC %, FC medio ponderado de la familia; clasificaciones K&S (Star/Plowhorse/Puzzle/Dog), Miller (Winner/Marginal/Loser), Pavesic (Prime/Standard/Sleeper/Problem), Goal Value vs objetivo; Comparativa: las 4 lecturas lado a lado, «¿discrepan?» y texto de diagnóstico (`IF` encadenados: «MC alto con FC % pobre: revisar precio, no retirar», etc.) | Reformular, resubir, rediseñar o retirar, plato a plato, entendiendo qué mide cada método |
| 5 | `simulador-repricing-multicanal.xlsx` | Instrucciones · Parámetros · Carta · Resumen | matriz IVA 3×3 (D4), comisión take away y delivery, packaging €/pedido, platos por pedido, FC objetivo por canal; 20 platos: coste, PVP sala sin IVA, tipo (comida/refresco/alcohol), precio techo en la app sin IVA | por canal: FC % efectivo `=(coste+pack/platos_pedido)/(PVP×(1−com))`, PVP sin IVA necesario para el FC objetivo, PVP con IVA (INDEX/MATCH sobre la matriz), «¿viable en delivery?» (`IF(necesario<=techo)`), ingreso neto por plato; Resumen: nº viables, nº a excluir, margen total por canal | Cuánto subir en cada canal y qué platos excluir del delivery |
| 6 | `carta-de-bebidas-beverage-cost.xlsx` | Instrucciones · Parámetros · Vinos · Cervezas y Refrescos · Destilados y Cócteles · Resumen Bodega | matriz IVA (D4), objetivos de beverage cost por categoría (editables, sembrados con las referencias del research y su fuente), 30 vinos (compra botella sin IVA, formato cl, PVP botella y copa, copas por botella, uds vendidas), barriles y botellines (litros, precio, cl por servicio, PVP), destilados (70 cl, precio, cl por copa, PVP) y 8 cócteles (4 líneas de ingredientes) | coste por copa/servicio, margen €, beverage cost % por referencia y ponderado por categoría, ventas y coste totales, semáforo vs objetivo; Resumen con PVP con IVA por canal (sala vs para llevar) | Gestionar la bodega como cuenta de resultados propia con el IVA correcto por canal |
| 7 | `cuadro-de-mando-prime-cost.xlsx` | Instrucciones · Parámetros · Mensual | tipo de negocio (lista: sala/barra-autoservicio), objetivo de prime cost por tipo (65 %/55 %, D5), SS empresa 33 % (param familia); 12 meses: ventas netas comida y bebida, stock inicial, compras, stock final, salarios brutos, otros costes de personal | consumo, food cost %, coste de personal con SS, labor cost %, prime cost %, semáforo `ISNUMBER` vs objetivo, margen tras prime cost; gráfico de líneas prime cost vs objetivo (openpyxl) | Ver food cost y personal juntos: un food cost «bueno» que tapa un labor cost roto |
| 8 | `plan-accion-90-dias.xlsx` | Instrucciones · Decisiones · Calendario 90 Días · KPI de Seguimiento | 20 decisiones: plato/área, herramienta de origen (lista), decisión (lista: Reformular/Resubir/Rediseñar/Retirar/Negociar/Mantener), responsable, fecha, impacto estimado €/mes, estado (lista); calendario 13 semanas con hitos y «Hecho» (Sí/No); KPI mes 0-3: food cost %, prime cost %, ticket medio, MC por cubierto, nº de platos | impacto total, % de decisiones cerradas, avance del calendario, variación de cada KPI vs mes 0 con semáforo | Dar fecha y responsable a las salidas de las otras 7. **Declara en Instrucciones que NO es el plan de 4 semanas del bono del Kit** |

### 2.3 Lo que NO se construye
Análisis por familias suelto (ya está dentro de la matriz), food cost teórico vs real semanal (Kit: 09, 11 y bonus mermas), pastelería por lote (Kit: 05), negociación con proveedores (bono del Kit: 7 tácticas). El cap. 17 (obrador) y el 07 (teórico vs real) explican método y remiten al Kit para la plantilla.

## 3. Bloque fiscal (fuente primaria: Ley 37/1992 consolidada, `boe.es/buscar/act.php?id=BOE-A-1992-28740`)

| Operación | Tipo | Base legal |
|---|---|---|
| Servicio de hostelería en sala: comida, bebida, **alcohol incluido** | 10 % | art. 91.Uno.2.2.º («suministro de comidas y bebidas para consumir en el acto») |
| Take away / delivery de comida elaborada (entrega de bienes, sin servicio) | 10 % | art. 91.Uno.1.1.º |
| Take away / delivery de bebida alcohólica | 21 % | art. 91.Uno.1.1.º excluye las bebidas alcohólicas → tipo general art. 90 |
| Take away / delivery de refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos | 21 % | art. 91.Uno.1.1.º, exclusión vigente desde 1-ene-2021 (Ley 11/2020) |
| Compras al 4 %: pan común, harinas panificables, leche, quesos, huevos, frutas, verduras, hortalizas, legumbres, tubérculos, cereales y **aceites de oliva** | 4 % | art. 91.Dos.1.1.º (aceite de oliva por RDL 4/2024, con efectos 1-ene-2025) |
| Compras al 10 %: resto de alimentos (carnes, pescados, conservas, aceites de semillas, agua…) | 10 % | art. 91.Uno.1.1.º |
| Compras al 21 %: bebidas alcohólicas, refrescos azucarados/edulcorados, y todo lo no alimentario (packaging, menaje) | 21 % | art. 90 |

Regla de cálculo: el food cost % se calcula sobre **venta neta (base imponible)** y con **coste neto de IVA soportado** (el IVA de compra se deduce en el 303: es tesorería, no coste). Un agente verificador confirma este bloque contra el BOE antes de que se escriban los capítulos 03-04 y las hojas de parámetros.

## 4. Índice de la guía (guion cerrado en `guion_guia_food_cost_ingenieria_menu.py`)

Presupuesto: 20 capítulos · 1.400-1.600 palabras (el 19, 2.200) · 1-3 tablas por capítulo construidas desde los xlsx · prohibiciones de familia (`NO_COMUN`) + lista negra D10 · cifras SOLO desde celdas de los 8 libros o desde `auditorias/guias-v2-research-sector.json` (ids `FC-*`, añadidos en esta sesión con URL y fecha).

| # | Título | Contenido obligatorio |
|---|---|---|
| 01 | Para quién es esta guía (y qué no vas a encontrar aquí) | nivel de partida; mapa «problema → capítulo → herramienta»; jerarquía con el Kit (plantillas) y con esta guía (método y decisión); glosario ES/LATAM (D12) |
| 02 | Las cuatro cifras que gobiernan tu carta | food cost %, margen de contribución €, prime cost, ticket medio; cuál manda en cada decisión; tabla desde `cuadro-de-mando` y `matriz` |
| 03 | IVA, base imponible y el error que invalida tu food cost | matriz 3×3 (§3) como tabla; cálculo sobre venta neta; ejemplo con un plato de la ficha (con y sin IVA) |
| 04 | El coste real de compra: 4 %, 10 % y 21 % en el mismo albarán | lista del 4 % con el aceite de oliva; IVA soportado por partida; el IVA es tesorería; tabla de un albarán de ejemplo |
| 05 | Del bruto al neto: merma, rendimiento y el test que sustituye a la tabla | despiece, cocción y desperdicio; protocolo del test; coste neto/kg con subproductos; tablas desde `rendimiento-mermas-producto` |
| 06 | La ficha de escandallo que aguanta una auditoría | `D/(1−F)`, raciones, coste/ración, PVP objetivo; tabla desde `ficha-escandallo-base`; cross-sell explícito al Kit para las 11 plantillas por formato |
| 07 | Food cost teórico vs real: dónde se escapa el dinero | fórmula del real (stock inicial + compras − final); cuatro causas de desviación; protocolo semanal; remite al dashboard del Kit |
| 08 | Prime cost: la métrica que mide la salud del negocio | estructura española 30 % + 30-35 % (fuente CaixaBankLab/elBulli); umbral 65 %/55 % (D5); Toast como contraste EE. UU.; tabla desde `cuadro-de-mando-prime-cost`; cross-sell al Kit de Gestión de Personal |
| 09 | Cuatro formas de poner precio a un plato | factor, margen € objetivo, mercado, valor percibido; cuándo cada una; tabla desde `precio-objetivo-multi-metodo` |
| 10 | Psicología de precios: lo demostrado y lo que es leyenda | efecto señuelo (estudio con DOI) primero; Wansink con salvedad (D8); símbolo de moneda (estudio en $); lo que circula sin estudio |
| 11 | Ingeniería de menú I: Kasavana & Smith bien hecho | matriz, umbral 70 %/N, por familia; tabla desde `matriz` hoja K&S |
| 12 | Ingeniería de menú II: lo que la matriz clásica no ve | Miller, Pavesic (FC % × MC ponderado), Goal Value (fórmula completa), LeBruto (lectura); tablas desde las hojas Miller/Pavesic/Goal Value |
| 13 | Cuando los métodos discrepan: el protocolo de decisión | qué mide cada método; lectura de la hoja Comparativa; reformular/resubir/rediseñar/retirar; tabla Comparativa |
| 14 | Carta corta, menú de precio fijo, buffet y banquete | tamaño de carta; poda; el margen lo decide el mix; hotel/buffet/catering/eventos con ejemplo (D14); tabla de un menú de precio fijo desde `matriz` (familia «Menú») |
| 15 | Multicanal: sala, take away y delivery | comisiones como orden de magnitud 2025-2026 (fuente), packaging por pedido, IVA por canal (D4), techo de precio; tabla desde `simulador-repricing-multicanal`; Rappi/DiDi/PedidosYa en la nota LATAM |
| 16 | Beverage cost: la bodega como cuenta de resultados propia | CaixaBank: bebida 34,5 % vs comida 28 %; copa vs botella; barril; cócteles; IVA por canal; tablas desde `carta-de-bebidas` |
| 17 | Costeo por lote en obrador y pastelería | rendimiento de tanda, mano de obra por hora, packaging, escalado; método (la plantilla es la 05 del Kit) |
| 18 | Cuando sube el proveedor: protocolo de re-escandallado | disparadores, calendario, cómo leer INE/MAPA (sin cifra, D10), cómo subir precio sin perder al cliente; NO repite las 7 tácticas del bono del Kit |
| 19 | Caso integral: una carta entera, de principio a fin | los 12 platos de ejemplo del pack: ficha → matriz (4 métodos) → precio objetivo → multicanal → plan 90 días; etiquetado como **caso modelado**, no cliente real; 3-4 tablas |
| 20 | Cuándo tu Excel se queda corto | criterio Excel → software → agentes de IA; frase de D16; CTA honesto a la plataforma |

### 4.2 Bonus «12 ejercicios resueltos» (documento propio del pipeline, `BONUS` del guion)
1 cantidad bruta y coste con merma · 2 test de rendimiento con subproductos · 3 food cost real del mes · 4 PVP por los 4 métodos de un mismo plato · 5 IVA por canal de una bebida · 6 clasificación K&S de una familia de 6 platos · 7 el mismo grupo en Miller y Pavesic (y por qué discrepan) · 8 Goal Value de dos platos · 9 repricing en delivery con packaging y techo · 10 copa vs botella · 11 prime cost de un mes y su semáforo · 12 menú de precio fijo: margen por mix. Cada uno: enunciado con datos, resolución paso a paso, tabla, lectura del resultado. Las cifras salen de los xlsx (mismos platos de ejemplo).

## 5. Capa de producto (zona app + landing + hub + functions)

1. `astro-site/src/lib/zona-app.ts`: nueva entrada `guia-food-cost-ingenieria-menu` (accessPath, libraryPath, landingPath, storageKey `guia-food-cost-ingenieria-menu-jwt`, gate `GuiaFoodCostAccessGate`, dashboard `GuiaFoodCostDashboard`) → `python3 scripts/astro-migration/fase5-generate-zona-app.py` genera `-access.astro`, `-library.astro` y el island.
2. SPA (fuente de los islands): `src/pages/GuiaFoodCostAccessGate.tsx` (wrapper de `ProductAccessGate`, 10 líneas) · `src/pages/GuiaFoodCostDashboard.tsx` (patrón del dashboard gastronómico; secciones: Guía (2) · Herramientas Excel (8) · Bonus (2)) · rutas en `src/App.tsx`.
3. Functions (las 4 + shared): `verify-purchase.ts`, `resend-access.ts`, `admin-generate-access.ts`, `get-download-urls.ts` (claves `guia-pdf`, `guia-docx`, `bonus-pdf`, `bonus-docx`, `ficha-escandallo`, `rendimiento-mermas`, `precio-objetivo`, `matriz-multimetodo`, `simulador-multicanal`, `carta-bebidas`, `cuadro-prime-cost`, `plan-90-dias`) · `src/data/productos-digitales-config.ts` (mapa duplicado) · `netlify/shared/payment-links.ts` (tras crear el Payment Link) · `grep -c "'guia-food-cost-ingenieria-menu'" netlify/functions/*.ts` ≥ 1 en las 4.
4. Landing: `astro-site/src/data/productos/guias/guia-food-cost-ingenieria-menu.ts` (tipo `GuiaData`, `showCompatibleApps: true`, sin `priceOld`/`discountBadge`/`aggregateRating`, `testimonials.items: []`) + `astro-site/src/pages/guia-food-cost-ingenieria-menu.astro` (wrapper; env `VITE_STRIPE_PAYMENT_LINK_GUIA_FOOD_COST`). `GuiaLandingPage.astro`: ocultar testimonios si `items.length === 0`.
5. Catálogo y enlaces: `src/data/products-catalog.ts` (entrada 45, nombre/precio/desc), hub `ProductosDigitalesHubPage.astro` (tarjeta nueva tras el Kit de Escandallos, badge «Nuevo»; **quitar** la entrada «Guía Food Cost + Ingeniería de Menú» de `comingSoon`) y `src/pages/ProductosDigitales.tsx` (paridad), `linkify-use-case.ts`, `productos-changelog.ts` (entrada 1.0), footerLinks cruzados en `kit-escandallos.ts` y `guia-restaurante-gastronomico.ts`, `_redirects` no aplica.
6. Imágenes (skill `generate-images`, Nano Banana 2): 6 de galería `/lovable-uploads/ai-gallery/guia-foodcost-{hero,carta,cocina,bodega,delivery,equipo}.jpg` + `og-guia-food-cost-ingenieria-menu.jpg` (1200×630). Sin texto legible en las imágenes, sin marcas, sin ingredientes con etiqueta.
7. Stripe (con el CLI si la clave lo permite; si no, John): producto «Guía Food Cost + Ingeniería de Menú — AI Chef Pro», `tax_code txcd_10000000`, precio 5500 EUR `tax_behavior exclusive`, Payment Link con `after_completion.redirect` a `https://aichef.pro/guia-food-cost-ingenieria-menu-access?session_id={CHECKOUT_SESSION_ID}`, `automatic_tax` on, `invoice_creation` on, `billing_address_collection auto` (calco del de la guía gastronómica). Env var en Netlify (`aichefpro`, contextos production y deploy-preview; scope builds) y `sync-payment-links.py`.
8. Blog (D11): enlace contextual + banner sustituido en los 6 posts; `fase8b-regen-lastmod.py`.

## 6. Gates antes de LIVE
`inject_cache.py` + verificación `data_only` por fórmula registrada · `postprocess-transversal.py <ruta> --dry-run` (A4, metadata, bio, versión) · `censo-entregables.py --only guia-food-cost-ingenieria-menu --fail` = 0 defectos · `gate-no-latinos.py --only <carpeta>` · `documentos.py` con todos los `ok` en verde y páginas medidas · script del Bug #2 (`MISSING: 0`) · `gate-flujo-postpago.py --offline --only guia-food-cost-ingenieria-menu` · `fase5-generate-zona-app.py --check` · `robots-gate.py` (necesita dist: se corre tras el build en la nube con el dist descargado, o por inspección: la landing no casa con `/guia-*-access|library`) · build Netlify verde · `gate-flujo-postpago.py --only …` LIVE (landing con `buy.stripe.com`, access/library 200, descargas binarias con el mismo tamaño que en disco) · compra de prueba real.

## 7. Presupuesto y reparto
Research (cerrado): 1,47 M tokens de subagentes. Construcción: 3 constructores opus (xlsx, 2-3 libros cada uno) + 1 verificador fiscal sonnet + 1 agente sonnet para los ids `FC-*` del research JSON + 1 opus para el guion + 1 refutador opus (dos lentes) + fixer sonnet + 1 opus capa de producto. Texto largo: bridge.py. Fable: SPEC, decisiones, functions/Stripe/env, verificación final y LIVE. Térmica: `istats cpu temp` antes de cada python local; un python cada vez dentro de cada agente.

Via: Claude Code
