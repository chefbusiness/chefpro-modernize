# LENTE 6 — Activos propios, frontera, canales y propuesta de entregables

**Producto en diseño:** «Cómo Montar una Pastelería» — guía premium «Cómo Montar», producto nuevo nº 4 del ciclo de
sesiones alternadas. Sería el **producto 48** del catálogo.
**Slug propuesto:** `guia-pasteleria-obrador` (paralelo a `guia-panaderia-obrador`; el prefijo `/guia-` ya está cubierto
por `robots.txt` en los 5 bloques de user-agent → **no hace falta tocar `robots.txt`**, verificado abajo).
**Fecha del informe:** 2026-09-10 (el encargo se redactó el 2026-09-09; todas mis lecturas y mediciones son del 10-sep).
**Autor:** lente 6 (auditoría de activos). Trabajo 100 % local, sin acceso a web.

## Método

- **Lectura de ficheros del repo** con `grep`/`sed`/`cat` (fichero:línea citado en cada afirmación).
- **Lectura de xlsx** con `openpyxl 3.1.3` en `read_only=True`, un fichero cada vez, cerrando y liberando cada libro
  (`wb.close()` + `gc.collect()`) entre iteraciones. Dos pasadas: `data_only=True` (valores) y `data_only=False`
  (recuento de fórmulas).
- **Medición de PDF** con **PyMuPDF 1.22.5** (disponible en el Mac): `page_count`, palabras por `get_text()`, metadata.
- **Medición de DOCX** descomprimiendo `word/document.xml` y contando tokens y `<w:tbl>`.
- **Térmica:** `istats cpu temp` antes y después de cada tanda. Registro real de la sesión: 64,13 → 64,19 → 61,94 →
  60,81 → 60,63 → 61,06 → 60,25 → 59,25 → 58,25 → 56,56 → 55,75 → 56,00 °C. **Nunca se superaron los 65 °C** y las
  tandas de openpyxl se lanzaron en la ventana descendente (< 61 °C). Sin builds, sin Playwright, sin navegador.

## Limitaciones declaradas (qué NO pude verificar y por qué)

1. **Nada de mercado.** El encargo es 100 % local. Los volúmenes de DataForSEO, la SERP, los precios de
   `lahostelera.com` y el competidor `pasteleriaparatodos.com` que aparecen en el brief **no los he verificado**: los
   trato como dato heredado y los marco como tales cada vez que los uso. No he ejecutado `scripts/dataforseo.py`.
2. **No he abierto producción.** Todo lo que digo de la web sale del repo (`astro-site/src/`, `src/`) y de
   `astro-site/public/dl/`, no de `aichef.pro`. No corrí ningún gate LIVE ni `fase8c-enlaces-vivos.py`.
3. **No he abierto el panel de Resend.** La cola de correos sale de `CALENDARIO-V2-SEMANAL.md` §0-ter, que es el
   registro escrito, no el estado real de la API.
4. **No hay `dist/`** que auditar en esta sesión (no se construye en local por la regla térmica), así que las
   afirmaciones sobre robots.txt y sitemap son **por lectura de la regla**, no por simulación con `robots-gate.py`.
5. **Precios, IVA y epígrafes de IAE de pastelería: no verificados.** Aparecen abajo como *preguntas*, nunca como dato.
   El epígrafe de IAE que cita el checklist de panadería (`644.1` / `419.1`) es de ese producto y **no lo he
   contrastado** con fuente primaria.
6. **⚠️ `documentos.py` se estaba EDITANDO mientras yo lo leía.** Primera lectura: 2.051 líneas. Última: **2.189**
   (`mtime` 2026-09-10 00:05:48, mi sesión empezó antes). Hay otra sesión trabajando en ese fichero **ahora mismo**, y
   está **sin commitear**. Todas las líneas que cito de `documentos.py` son las del estado de las 00:12 del 10-sep y
   **pueden haberse movido otra vez**; los nombres de función (`repartir_puntos`, `prompt_bloque`, `cargar_guion`) sí
   son estables. Antes de tocar nada, `git status` y releer.
7. La cifra de tokens de los tres productos anteriores (9,7 M / ~10,5 M / ~17 M) viene del encargo y de
   `CALENDARIO-V2-SEMANAL.md`; **no he medido consumo yo**.

---

# 1. Inventario de los activos hermanos

## 1.1 `kit-tareas-pasteleria` — 12 €, v2.0 (2026-08-21), **15 xlsx**

Ruta: `astro-site/public/dl/kit-tareas-pasteleria/`. Leídos los 15, uno a uno.

| Fichero | Hojas (filas×cols) | Qué cubre | Qué le falta para QUIEN ABRE | Decisión |
|---|---|---|---|---|
| `01-apertura-cierre.xlsx` | Instrucciones · Apertura Obrador 41×7 · Cierre Obrador 39×7 | Rutina diaria del obrador con hora límite, responsable y firma | Es rutina de régimen, no de arranque | **CITAR** |
| `02-partidas-cocina.xlsx` | Masas y Fermentación 45×8 · Cremas y Rellenos 37×8 · Decoración y Acabado 30×8 | Tareas por partida con parámetro/objetivo (refresco 1:1:1, enfriado 65→10 °C, glaseado 32-35 °C) | No dice **cuánta** capacidad hace falta ni qué equipo la da | **CITAR** |
| `03-tareas-manager.xlsx` | Diario 35×7 · Semanal 41×7 · Mensual 33×7 · Handover 21×7 | Gestión diaria del responsable | No cubre las decisiones de apertura | **CITAR** |
| `04-tareas-perfiles.xlsx` | Jefe Pastelero 33×7 · Pastelero 32×7 · Ayudante 28×7 · Dependiente Vitrina 29×7 | Onboarding por puesto | No dimensiona la plantilla ni su coste | **CITAR** (y construir el dimensionado) |
| `05-tareas-semanales-mensuales.xlsx` | Limpieza Semanal 37×7 · Mantenimiento Mensual 32×7 · Inventario 30×7 | Limpieza, mantenimiento, FIFO | — | **CITAR** |
| `06-eventos-festivos.xlsx` | Navidad 49×7 · San Valentín 30×7 · Semana Santa 34×7 · Día Madre-Padre 28×7 · Comuniones 40×7 · Todos los Santos 35×7 | **Los 6 picos del año, tarea a tarea** | Dice *qué hacer* en el pico; no dice *cuánto factura*, *cuánta tesorería* ni *si el obrador aguanta* | **CITAR + CONSTRUIR distinto** (ver libro 3 del §5) |
| `07-plantilla-personalizable.xlsx` | Por Franja · Por Zona · Por Perfil (en blanco) | Moldes vacíos | — | **CITAR** |
| `08-apertura-cierre-negocio.xlsx` | Apertura 35×8 · Cierre 34×8 | Local, tienda, vitrina, alarma, climatización | — | **CITAR** |
| `09-apertura-cierre-caja.xlsx` | Apertura Caja 20×6 · Cierre Caja 50×6 · Registro Mensual 38×10 | Arqueo y Z del TPV | — | **CITAR** |
| `10-plan-produccion-semanal.xlsx` | Plan Semanal 56×11 · Producido vs Vendido **261×12** · Resumen por Partida 19×7 (Merma %, Coste merma €) | **Planificación de producción y merma ya resueltas** | Nada: está hecho | **CITAR — prohibido rehacer** |
| `11-control-encargos.xlsx` | Ficha 51×4 · Registro 48×15 · Agenda Entregas 19×8 · Encargos de Hoy 24×7 | **Encargos ya resueltos** | Nada | **CITAR — prohibido rehacer** |
| `12-control-alergenos-vitrina.xlsx` | Matriz **57×22** · Carta 59×15 · Cartel 30×4 · Etiquetas 31×6 | **Alérgenos de vitrina (14 UE) ya resueltos**, con cartel y etiquetas | Nada | **CITAR — prohibido rehacer** |
| `13-registro-temperaturas-recepcion.xlsx` | Temperaturas 45×15 · Recepción 44×11 · Etiquetas Elaborado 50×6 · **Vidas Útiles 28×4** | Temperaturas, recepción y vidas útiles (crema pastelera 48-72 h, nata montada 24 h, ganache 5-7 días) | Nada | **CITAR — prohibido rehacer** |
| `BONUS-01-briefing-servicio.xlsx` | Briefing Diario 35×7 | Reunión de 5 min | — | **CITAR** |
| `BONUS-02-calendario-anual-tareas.xlsx` | Calendario Anual 22×7 | Fechas clave con producción y antelación | Fechas, no dinero | **CITAR + CONSTRUIR distinto** |

**Hallazgo colateral (defecto vivo, no bloqueante):** el kit entrega **15 xlsx** pero el hub lo vende como **«9
checklists»** — `src/pages/ProductosDigitales.tsx:678` y `astro-site/src/components/pages/ProductosDigitalesHubPage.astro:694`
—, y `src/data/products-catalog.ts:141-143` lo resume en cinco palabras («Producción, conservación, vitrina,
exposición»). La v2.0 es del 2026-08-21 (`src/data/productos-changelog.ts:25-27`) y la descripción no se actualizó.
**Es un producto que se infravende a sí mismo**; al tocar el hub para el producto 48 se arregla de paso.

## 1.2 `kit-tareas-chocolateria` — 12 €, 11 xlsx

Sólo aporta lo que la pastelería no tiene: `02-partidas-produccion.xlsx` con hojas **Templado** y **Moldeado**. Si la
guía cubre la variante «pastelería con línea de bombonería», el templado se **cita** ahí. El resto (01, 03-09, bonus) es
el mismo molde que el kit de pastelería. **Nada que construir.**

## 1.3 `guia-panaderia-obrador` — 65 €, **la hermana directa**. 15 xlsx + 3 docx + 1 pdf

### 1.3.1 🔴 El PDF que se vende no existe

Medido hoy con PyMuPDF sobre `astro-site/public/dl/guia-panaderia-obrador/`:

| Fichero | Medido | Prometido en la landing |
|---|---|---|
| `guia-panaderia-obrador.pdf` | **1 página · 55 palabras** · metadata `author='anonymous'`, `title='untitled'` | «20 capítulos, 70+ páginas» |
| `guia-panaderia-obrador.docx` | **4.699 palabras · 0 tablas** (≈ 9 páginas a la densidad medida) | idem |
| `business-plan-modelo.docx` | **796 palabras · 0 tablas** | «resumen ejecutivo, proyecciones financieras a 3 años y análisis de mercado» |
| `manual-operaciones.docx` | **944 palabras · 0 tablas** | «manual del obrador» |

El PDF es literalmente una portada que dice *«Para la guía completa en formato editable, descarga el archivo DOCX»* y
debajo *«20 capítulos · 70+ páginas»*. La promesa está en
`astro-site/src/data/productos/guias/guia-panaderia-obrador.ts:20`, `:30`, `:32`, `:158` y `:187`.

**Por qué importa para este producto, y mucho:** la pastelería es la hermana natural de la panadería. Todo el copy, el
cross-sell y el email post-compra van a apuntar de una a otra. **Vender la 48 apoyándose en una hermana que entrega
un 13 % de lo que promete es el mayor riesgo comercial del lanzamiento.** Esto es el estado v1.0 que la
`guias-v2-SPEC.md` §5 describe («en 6 de las 8 guías el PDF es una portada de una página»): la v2.0 de los documentos
**nunca se aplicó a panadería** — su changelog (`src/data/productos-changelog.ts:84-94`) va por **v1.1 (2026-08-22)** y
sólo cubre «revisión completa de las 15 plantillas».

### 1.3.2 Los 15 xlsx: cuáles son molde de familia y cuáles son de panadería

Recuento de fórmulas con `data_only=False` (segunda pasada):

| Fichero | Hojas | Fórmulas | Molde reutilizable | Contenido |
|---|---|---|---|---|
| `calculadora-capex.xlsx` | CAPEX Panadería 31×5 | 3 | ✅ **molde** (partida / mín / máx / tu importe / notas) | panadería (horno de piso, salida de humos) |
| `plan-financiero-3-anos.xlsx` | P&L 3 años 25×5 | 21 | ⚠️ molde **débil** | panadería (mostrador, B2B, suscripción) |
| `pl-mensual-escenarios.xlsx` | P&L 3 escenarios 19×5 | 18 | ✅ molde | panadería |
| `cash-flow-break-even.xlsx` | Cash Flow 24m 13×15 | 42 | ✅ molde | panadería |
| `calculadora-ticket-medio.xlsx` | Ticket Medio 17×5 | 14 | ✅ molde (PVP × mix % → aporte) | panadería |
| `plantilla-turnos-brigada.xlsx` | Turnos obrador 17×11 | **0** | ⚠️ molde **inservible** (no calcula ni horas ni coste) | panadería (turnos 03-11) |
| `cronograma-apertura-gantt.xlsx` | Gantt 19×9 | **0** | ✅ molde (hitos × meses con ■) | panadería |
| `escandallo-maestro-panaderia.xlsx` | Escandallos 28×8 | 75 | ✅ molde | **panadería pura** (T55/T65/T80, masa madre) |
| `plan-fermentacion-y-produccion.xlsx` | 18×9 | **0** | ❌ | **panadería pura** (hidratación %, bulk, bloque frío) |
| `checklist-legal.xlsx` | 36×5 | 2 (COUNTIF) | ✅ **molde B** | panadería (IAE 644.1 / 419.1) |
| `checklist-equipamiento.xlsx` | 39×6 | 2 | ✅ **molde B** con precio mín/máx y prioridad | panadería |
| `checklist-appcc.xlsx` | 43×5 | 2 | ✅ **molde B** | panadería (silos, harinas) |
| `checklist-contratacion.xlsx` | 28×5 | 2 | ✅ **molde B** | panadería |
| `checklist-marketing-preapertura.xlsx` | 30×5 | 2 | ✅ **molde B** | panadería |
| `checklist-salida-humos.xlsx` | 28×5 | 2 | ✅ **molde B** — el mejor de todos (bloque «PRE-ALQUILER: NO FIRMAR HASTA VERIFICAR», con un ítem marcado *KILLER*) | mixto |

**Conclusión del 1.3:** de los 15, **11 sirven de molde estructural** y **2 son de panadería pura**
(`plan-fermentacion-y-produccion`, `escandallo-maestro-panaderia`). Pero el nivel de fórmula es **v1.0**: tres libros
tienen **cero** fórmulas y el `cash-flow` lleva los costes tecleados como constantes con el porcentaje en el rótulo
(«Coste materias primas (20%)» = `-2800` a mano). **Copiar el molde sí; copiar la implementación, no.**

## 1.4 `plan-negocio-panaderia` — 35 €. **Aquí está el motor financiero bueno**

`astro-site/public/dl/plan-negocio-panaderia/plan-financiero-panaderia.xlsx` (66.513 bytes) tiene 9 hojas:

`0. Supuestos` 68×3 (celdas verdes: transacciones/día 180, ticket medio sin IVA 5,5 €, días de apertura 310) ·
`Inversión Inicial` 38×5 (con columna **«¿Lleva IVA?»**) · `PyG 3 Años` 59×8 (con columna **«Tipo de IVA de la línea (%)»**) ·
`Punto Equilibrio` 36×6 · `Escenarios` 28×6 · `Personal` 29×10 (bruto, **SS a cargo de la empresa**, coste mes, coste año;
convenio de hostelería, 14 pagas) · `Instrucciones` 72×5 · **`Tesorería 12 meses` 70×15** (con estacionalidad mensual que
suma 100 % y **rampa de arranque** 0,55 → 1,00) · `Financiación` 80×8.

Esto es el **motor 2.2 de la familia PLANES**, y es cualitativamente superior al `plan-financiero-3-anos.xlsx` de la
guía de panadería (25×5, 21 fórmulas, sin tesorería, sin IVA, sin financiación).

> **Decisión que propongo y que hay que firmar en la SPEC:** el bloque financiero de la Guía de Pastelería se construye
> con el **molde de `planes-v2_0` (motor 2.2)**, no con el de `guias-v2_0/grupo_a.py` v1.0. Si no, la guía de 65 €
> entregaría un plan financiero peor que el del plan de negocio de 35 €.

`checklist-apertura-panaderia.xlsx`: 6 fases (F1 Constitución, F2 Local y licencias, F3 Equipamiento, F4 Personal,
F5 Marketing, F6 90 días) + Instrucciones. Molde de fases reutilizable.

**No existe `plan-negocio-pasteleria`** en el catálogo (verificado: los 10 planes son cafetería, food-truck,
bar-restaurante, panadería, tapas-bar, catering temático, chef privado, paellero, parrillero y coctelería,
`src/data/products-catalog.ts:328-428`). **No hay competidor interno directo por el lado del plan de negocio.**

## 1.5 `kit-escandallos` hoja 05 — 12 €

`05-pasteleria.xlsx` (26.011 bytes): `Instrucciones` 66×2 · **`Tarta Chocolate` 38×13** · **`Croissants` 37×13** ·
**`Macarons` 37×13** · `Conversiones` 37×3 · `Mermas` 25×4.

Cubre: escandallo **de la tanda completa** con `Ud. Compra / Precio/Ud / Cantidad / Ud. Uso / Factor / Merma (%)`, tabla
de conversión y mermas de referencia por categoría (Lácteos 3 %, Secos/granos 2 %, Chocolate/cacao 12 %).

**Le falta, desde la óptica de quien abre:** son **3 elaboraciones**, no una carta; **no incorpora coste hora de
obrador** (el coste es sólo de ingrediente); y no ayuda a **decidir el surtido** de apertura. **Decisión: CITAR** para el
escandallo unitario y **CONSTRUIR** la capa que falta (carta completa + mano de obra + decisión de surtido).

## 1.6 `pack-appcc` — 14 €, 21 xlsx

De los 21, cubren obrador de pastelería sin cambios: `01` temperaturas diario · `02` recepción · `03` plan L+D ·
`04` limpieza diaria · `05` checklist recepción · `06` trazabilidad · `07` plagas DDD · **`08` matriz alérgenos (214×19)** ·
`10` agua · `11` acciones correctivas · **`12` análisis de peligros HACCP (51×15)** · `13` higiene personal ·
`14` fichas 14 alérgenos · **`15` guía inspección (96×7, 25 puntos)** · `17` enfriamiento/descongelación ·
`19` termómetros · BONUS formación · BONUS alerta alimentaria.
**No aplican a pastelería:** `09` aceite de fritura (salvo buñuelos/torrijas), `16` cocción-regeneración, `18` anisakis.

**Decisión: CITAR el pack entero.** La guía **no** construye ni un registro APPCC; construye el **checklist de puesta
en marcha del sistema** (qué hay que tener el día de la inspección), que es otra cosa.

> ⚠️ **Deuda heredada que NO debe entrar aquí:** `CALENDARIO-V2-SEMANAL.md` §0-ter punto 0 documenta que
> `kit-tareas-sushi-bar/03` y `kit-tareas-marisqueria/03` citan el **RD 1420/2006, derogado**. La guía de pastelería no
> toca anisakis, así que **no hereda el defecto** — pero conviene no copiar redacciones legales de otros kits sin
> verificar.

## 1.7 Guía Food Cost — cap. 17 «Costeo por Lote en Obrador y Pastelería»

Leído en `scripts/productos-digitales/guias-v2_0/guion_guia_food_cost_ingenieria_menu.py`. **1.400 palabras, 2 bloques,
4 epígrafes:** «La unidad de costeo es la tanda, no la pieza» · «Mano de obra por hora dentro del coste del lote» ·
«Packaging y etiquetado» · «Escalar una fórmula sin escalar el error».

Y trae esta instrucción literal en sus `puntos`:

> «Para el negocio que quiera la plantilla de costeo por lote lista, está en el Kit de Escandallos; aquí se da el
> método y se usa el método del margen objetivo.»

**Es el capítulo de método, y ya remite a otro producto por la herramienta.** La guía de pastelería **cita el cap. 17
para el método** y construye la herramienta de **carta de apertura** (que ninguno de los dos tiene). Sin solape.

---

# 2. Frontera y reglas de no-solape

## 2.1 Frontera con `kit-tareas-pasteleria` (12 €) — la más peligrosa

El kit resuelve **operar**; la guía resuelve **abrir**. La línea es limpia porque el kit es exhaustivo en lo suyo.

| Riesgo | Por qué es real | **Regla** |
|---|---|---|
| **R1 · Plan de producción** | El libro `10` ya trae Plan Semanal + Producido vs Vendido (261 filas) + merma por partida con coste € | La guía **no** emite ninguna hoja de plan de producción semanal. El capítulo de producción **cita** el libro 10 por su nombre de fichero. Lo que sí construye es **capacidad de obrador** (cuántas piezas/día permite el equipo que estás comprando), que es una decisión de compra, no de operación |
| **R2 · Encargos** | El libro `11` trae ficha, registro, agenda y encargos del día | Prohibido rehacer. La guía cubre **el modelo de negocio de encargos** (comuniones: captación, anticipo, calendario de entrega) y remite al libro 11 para la herramienta |
| **R3 · Alérgenos de vitrina** | El libro `12` trae matriz 57×22, carta, cartel y etiquetas de los 14 UE | Prohibido rehacer, y prohibido también duplicar con `pack-appcc/08`. La guía lleva **una fila de checklist legal** («matriz de alérgenos publicada antes de abrir») y nada más. *(Es la misma regla D5 del Manual del Chef Ejecutivo: nunca dos declaraciones completas de alérgenos en el mismo catálogo.)* |
| **R4 · Temperaturas y vidas útiles** | El libro `13` trae registro, recepción, etiquetas y vidas útiles orientativas | Prohibido rehacer. La guía cita el libro 13 y el `pack-appcc` |
| **R5 · Calendario de picos** | El `BONUS-02` ya lista las fechas con producción y antelación | La guía **no** repite el calendario. Construye la **economía** del pico: % de facturación anual, capacidad necesaria, refuerzo de plantilla y tesorería. El bonus dice *cuándo y qué*; la guía dice *cuánto y si aguantas* |
| **R6 · Perfiles de puesto** | El libro `04` trae 4 perfiles con sus tareas | La guía **no** rehace las fichas de tarea. Construye el **dimensionado** (cuántas personas de cada perfil, con coste y SS) y el **plan de contratación** con plazos |

**Regla transversal que propongo escribir en la SPEC (equivalente a la D4/D5 del Manual del Chef):** *cero fórmulas
entre libros y cero duplicación de tabla operativa; cuando la guía necesita un dato que vive en el kit, lleva una
**celda verde** con la nota «cópialo de tu `10-plan-produccion-semanal.xlsx`» y un enlace de texto.*

**Y esto es también el argumento de venta cruzada más honesto que tenemos:** la guía de 65 € puede decir, con verdad,
«la operativa del día 1 ya está resuelta en el Kit de Tareas Pastelería de 12 €; esta guía es lo que hay que decidir
antes». Son productos complementarios de verdad, no solapados.

## 2.2 Frontera con `guia-panaderia-obrador` (65 €) — mismo molde, contenido propio

**Se comparte (estructura):** las 6 familias de checklist (legal, equipamiento, APPCC, contratación, marketing
preapertura, salida de humos) · el gantt de apertura · la calculadora de CAPEX · el ticket medio · el P&L de 3
escenarios · el cash-flow / break-even · la estructura de 20 capítulos · los dos bonus (business plan + manual).

**Es contenido propio de pastelería (no se hereda):**

1. **Frío, no calor.** La panadería gira sobre horno, fermentación y masa madre. La pastelería gira sobre **frío
   negativo y abatimiento**: abatidor, cámara de fermentación controlada, congelación de entremets a −18 °C, glaseado
   sobre pieza congelada. El CAPEX y la capacidad cambian por completo.
2. **Estacionalidad extrema.** La panadería vende pan todos los días; la pastelería concentra en 6 picos
   (Reyes, San Valentín, Padre/Madre, Semana Santa, Comuniones, Todos los Santos). El calendario del propio kit lo dice:
   *«Roscón de Reyes — pico máximo del año para pastelerías»*. La panadería no tiene ese problema y su guía no lo
   modela.
3. **Encargos y comuniones** como línea de negocio con anticipo, calendario y riesgo de anulación. En panadería es
   marginal.
4. **Vitrina y merma de exposición.** El producto de pastelería caduca en 24-72 h (las vidas útiles del libro 13:
   nata montada 24 h) y se vende a la vista. La merma de vitrina es una partida propia.
5. **Las variantes del formato**, que la panadería no tiene: pastelería-cafetería · sin obrador (producto de terceros) ·
   obrador B2B/online · boutique de autor · cake design/encargos · obrador en casa. **La SERP heredada del brief
   apunta fuerte a «desde casa»** («montar una pastelería en casa», «requisitos para montar un obrador en casa»,
   «vender repostería desde casa España»), así que esa variante **no es un apéndice: es un capítulo**.

**🔴 Riesgo mayor y su regla:** *no se puede lanzar la Guía de Pastelería enlazando a la de Panadería como hermana
mientras la de Panadería entregue un PDF de 1 página.* Dos salidas, y hay que elegir antes de escribir el copy:

- **(a)** Se arregla panadería primero (es una sesión impar completa: aplicar §5 de `guias-v2-SPEC.md`), o
- **(b)** El copy y el `emailBody` de pastelería **no mencionan la guía de panadería** hasta que esté arreglada. Se
  cruza sólo con `kit-tareas-pasteleria`, `kit-escandallos`, `pack-appcc` y la Guía Food Cost.

Mi recomendación: **(b) para no bloquear el lanzamiento**, con (a) anotado como deuda inmediata. Decisión de John.

## 2.3 Frontera con `plan-negocio-panaderia` (35 €) y con la Guía Food Cost (55 €)

- **Plan de negocio (35 €) vs Guía Cómo Montar (65 €):** el plan responde *«¿sale la cuenta y qué le enseño al banco?»*;
  la guía responde *«¿qué hago, en qué orden, con qué proveedor y qué me juego si me equivoco?»*. La guía **contiene**
  un plan financiero, y por eso la escalera de precios es coherente (35 → 65). **No hay `plan-negocio-pasteleria`, así
  que no hay canibalización real hoy**; sí la habría si algún día se crea. Regla: si nace, nace **con la guía como
  upsell explícito**, no como sustituto.
- **Guía Food Cost (55 €):** frontera ya escrita por el propio cap. 17. La de pastelería **cita** el método de costeo
  por lote y **no** explica ingeniería de menú (eso es Food Cost, caps. 1-16).

---

# 3. Pipeline y molde: ¿se puede construir sin tocar el pipeline?

**Sí.** El producto encaja como caso nativo de la familia, sin modificar `documentos.py`.

## 3.1 Lo que ya está resuelto

- **Carga del guion por convención:** `documentos.py:2036-2037` construye la ruta
  `guion_{pid.replace("-","_")}.py` y la importa con `importlib` (`:2040`). Para `guia-pasteleria-obrador` bastará
  crear `guias-v2_0/guion_guia_pasteleria_obrador.py`.
- **Tipo de documento parametrizado:** `documentos.py:2080-2081` ya lee `categoria_doc` y `tipo_doc` del guion (se
  añadió el 2026-09-04 para la línea de Manuales), y `:1032`/`:1081` usan `tipo_doc_art` y `tipo_doc_dem`. Para una
  «Guía Cómo Montar» **son los valores por defecto** («Guía profesional», «de la guía», «esta guía»): **no hay que
  tocar nada**.
- **Gates configurables desde el guion:** `GUIA['gates']` acepta `paginas_prometidas`, `palabras_objetivo`,
  `min_palabras_cap` (`--min-palabras-cap`, default 900 en `:2114`), `cifras_extra`, `erratas_permitidas`,
  `erratas_forzadas`.
- **CLI:** `--producto --salida --json --solo-capitulos --regenerar --sin-bonus --solo-bonus --min-palabras-cap
  --modelo` (argparse desde `:2104`). `--modelo` fuerza `MODELO` y `MODELO_FALLBACK` a la vez.
- **Guardas:** aborta si `--salida` cae dentro de `public/dl/` (cabecera, regla dura 1). Los xlsx se leen en
  `data_only=True` y son la única fuente de cifras.
- **Constructores de xlsx:** el patrón está en `guia-food-cost/gen_*.py` — cabecera con `PID/PRODUCTO/NOMBRE/TITULO`,
  `sys.path` a `guias-v2_0`, `import motor`, `import datos_ejemplo as D`, salida a `build/`, y después
  `python3 ../inject_cache.py build/<fichero>.xlsx`. **Ni un número de negocio dentro del generador**: todos vienen de
  `datos_ejemplo.py`.

## 3.2 🔴 Ordenación crítica: los xlsx van ANTES que el texto

`documentos.py` calcula `xlsx_dir = os.path.join(DL, pid)` (`:2126`) — es decir,
`astro-site/public/dl/guia-pasteleria-obrador/`. **Los 10 libros de Excel tienen que estar ya copiados ahí antes de
lanzar la redacción**, porque el guion cita cifras por `fichero.xlsx!Hoja!Celda` y el pipeline las resuelve con openpyxl
para meter **el número** en el prompt. Invertir el orden hace que el guion no pueda escribirse.

## 3.3 🔴 Hallazgo: la trampa de los `puntos` YA ESTÁ ARREGLADA, pero **sin commitear**

El encargo la lista como riesgo pendiente («`documentos.py` reparte epígrafes pero no `puntos` → duplicación»).
**Corrección:** existe `repartir_puntos()` en `documentos.py:1096-1150`, fechada **2026-09-10**, con dos formas de
declararlos y un aborto explícito si una clave no es un epígrafe del capítulo. `prompt_bloque()` (desde `:1008`) ya recibe
`puntos` por tramo y `otros_tramos`. El docstring cita el defecto medido: *«41 pares de frases con Jaccard…»*.

**Pero:** `git status` devuelve `M scripts/productos-digitales/guias-v2_0/documentos.py` — **el arreglo está sin
commitear**. El último commit que tocó el fichero es `5565082` (Manual del Manager). Esto es exactamente el riesgo de la
memoria `feedback_commitear-wip-de-subagentes-y-recuperar-desde-transcripts`: si el Mac se apaga, se pierde.

**Acción inmediata, antes de nada:** commitear ese arreglo.

Y un matiz: **ningún guion existente usa `puntos_por_epigrafe`** (grep sin resultados en `guion_*.py`), así que todos
caen por la rama posicional. El guion de pastelería debería **nacer con `puntos_por_epigrafe`**, que es la forma
preferida y la que aborta si te equivocas de clave.

## 3.4 Calibración medida hoy con PyMuPDF

| PDF | Páginas | Palabras | **Palabras/página** | Metadata |
|---|---|---|---|---|
| `guia-food-cost-ingenieria-menu.pdf` | 95 | 50.265 | **529** | `AI Chef Pro` ✅ |
| `manual-chef-ejecutivo.pdf` | 96 | 52.203 | **544** | `AI Chef Pro` ✅ |
| `BONUS-ejercicios-resueltos.pdf` (Food Cost) | 32 | 12.986 | **406** | `AI Chef Pro` ✅ |
| `BONUS-12-situaciones-resueltas-cocina.pdf` | 34 | 15.762 | **464** | `AI Chef Pro` ✅ |
| `guia-panaderia-obrador.pdf` | **1** | **55** | — | `anonymous` / `untitled` ❌ |

**Confirma la calibración del encargo: ~530 palabras/página en cuerpo y ~410-465 en bonus.** Presupuesto para 20
capítulos y 70+ páginas prometidas: **~37.000 palabras** (1.700-1.850 por capítulo) para llegar a **~70 páginas
medidas** con `PageBreak`, portada e índice. Bonus de 25-30 páginas ≈ **10.500-12.000 palabras**.

## 3.5 Lo que SÍ habría que añadir

| Qué | Dónde | Por qué |
|---|---|---|
| `guion_guia_pasteleria_obrador.py` | `guias-v2_0/` | Obligatorio, es el contrato del contenido |
| `guia-pasteleria/` con 10 `gen_*.py` + `datos_ejemplo.py` | `scripts/productos-digitales/` | Patrón `guia-food-cost/` |
| `verificar_guion.py` | `guia-pasteleria/` | Copiar de `manual-chef-ejecutivo/`: valida que las N referencias a celda existen antes de gastar tokens de redacción |
| Ids de research `PA-*` en `guias-v2-research-sector.json` | `auditorias/` | Con gate de recuento, como los `CE-*`/`CS-*` (D24 del Manual del Chef) |
| Cifra `paginas_prometidas` en `GUIA['gates']` | el guion | Se **mide** y la landing publica lo medido |
| Nada en `documentos.py` | — | **No hace falta tocar el pipeline** |

---

# 4. Capa de producto y canales — todo lo que hay que tocar para publicar el 48

Verificado fichero a fichero. Estado a 2026-09-10.

## 4.1 Lo que YA está listo y no hay que tocar

| Superficie | Estado | Evidencia |
|---|---|---|
| **`robots.txt`** | ✅ **No tocar** | `astro-site/public/robots.txt` bloquea `/guia-*-access` y `/guia-*-library` en los 5 bloques (Googlebot, Bingbot, Twitterbot, facebookexternalhit, `*`). `guia-pasteleria-obrador-access/-library` cae dentro; la landing `/guia-pasteleria-obrador` no. **Sólo haría falta una línea nueva si el slug estrenara prefijo** — no es el caso |
| **Plantilla de landing** | ✅ Lista | `astro-site/src/components/pages/GuiaLandingPage.astro` ya trae las **3** inserciones de `CryptoPayButton` (`:265`, `:567`, `:662`), `cryptoEnabled = cryptoEnabledFor(data.slug)` (`:44`) y la nota de devoluciones (`:585`) |
| **Testimonios ocultables** | ✅ Listo | `GuiaLandingPage.astro:338-341`: con `testimonials.items` vacío la sección entera no se pinta (decisión D3 del 2026-09-03). Producto nuevo → `items: []`, sin `aggregateRating`, sin `priceOld`. Molde exacto: `astro-site/src/data/productos/manuales/manual-chef-ejecutivo.ts:18-19`, `:120-124` |
| **Buscador — sinónimos** | ✅ Sin cambios necesarios | `astro-site/src/lib/sinonimos-buscador.json`: ningún grupo ni frase menciona pastelería/obrador/montar, así que **no se dispara el gate de grupos huérfanos** (`ProductosDigitalesHubPage.astro:983-993`) |

## 4.2 Lo que hay que tocar, con fichero

| # | Fichero | Qué |
|---|---|---|
| 1 | `src/data/products-catalog.ts` | Entrada nº **48** (hoy **47**, contadas de `:20` a `:490`). `name`/`description` ES+EN, `price: '€65'`, `url` |
| 2 | `src/pages/ProductosDigitales.tsx` | Card real en `products` **y quitar la línea `:942`** del array `comingSoon` |
| 3 | `astro-site/src/components/pages/ProductosDigitalesHubPage.astro` | Lo mismo: card real **y quitar `:957`**. Los contadores del hero (`:995-997`, `:1126`) se recalculan solos |
| 4 | `astro-site/src/data/productos/guias/guia-pasteleria-obrador.ts` | El `data` de la landing (tipo `GuiaData`) |
| 5 | `astro-site/src/pages/guia-pasteleria-obrador.astro` | Wrapper de ~32 líneas. Molde: `manual-chef-ejecutivo.astro` (`whatsapp={false}`, `omitGlobalApp`, `locales={['es']}`, `basePath`, env var estática) |
| 6 | `astro-site/src/pages/guia-pasteleria-obrador-access.astro` | **GENERADO** por `scripts/astro-migration/fase5-generate-zona-app.py` — *editar el generador, no el fichero* |
| 7 | `astro-site/src/pages/guia-pasteleria-obrador-library.astro` | Idem. `whatsapp={false}` (el dashboard monta su `WhatsAppProductSupport`) |
| 8 | `src/pages/GuiaPasteleriaAccessGate.tsx` + `GuiaPasteleriaDashboard.tsx` | Islands de la SPA |
| 9 | `astro-site/src/islands/library/GuiaPasteleriaLibraryIsland.tsx` | Island del dashboard |
| 10 | `src/App.tsx` | 2 rutas (`-access`, `-library` con `ProtectedRoute storageKey=…-jwt`). Molde `:881-886` |
| 11 | `src/data/productos-digitales-config.ts` | Bloque completo: `accessPath`, `emailSubject`, `emailTitle`, `emailBodyPostPurchase`, `emailCta`, `emailTitleResend`, `emailBodyResend`, mapa `files` con los 10 xlsx + 4 documentos. Molde `:1000-1024` |
| 12 | `netlify/functions/get-download-urls.ts` | Gemelo del mapa. ⚠️ Regla §7-bis.1: **las claves ya emitidas no se cambian nunca** |
| 13 | `netlify/functions/verify-purchase.ts` | Mapa de producto |
| 14 | `netlify/functions/resend-access.ts` | Mapa de producto |
| 15 | `netlify/functions/admin-generate-access.ts` | Mapa de producto |
| 16 | `netlify/shared/payment-links.ts` | Entrada nº 48 (hoy **47**; `manual-chef-ejecutivo` en `:37`). **Payment Link lo crea John** |
| 17 | `netlify/shared/product-prices.ts` | `'guia-pasteleria-obrador': { eur: 65 }` (molde `:37`) |
| 18 | `src/data/productos-changelog.ts` | Bloque `version: '1.0'` + entrada «Lanzamiento» (molde `:100-108`) |
| 19 | `src/pages/AdminGenerateAccess.tsx` | Selector de producto (el censo de 27→44 ya falló una vez aquí) |
| 20 | **Netlify env** | `VITE_STRIPE_PAYMENT_LINK_GUIA_PASTELERIA_OBRADOR`, **scope `builds`** |
| 21 | **`CRYPTO_PRODUCTS`** | Añadir el id → `kit-tareas-cafeteria,manual-chef-ejecutivo,guia-pasteleria-obrador`. **Scope `builds` Y `functions`** + **redeploy** (media pasarela queda cocida en el HTML). Si para entonces el pago real de prueba de John ha cerrado y se aplicó la réplica, será `CRYPTO_PRODUCTS=all` y no hay que hacer nada |
| 22 | `astro-site/src/lib/sinonimos-buscador.json` | **Un alias nuevo** (ver 4.3) |
| 23 | `src/data/use-cases-content.es.ts` | `productIds` de 3-4 páginas de rol (ver 4.4) |
| 24 | 2-3 posts del blog ES | Sustitución quirúrgica de banner (ver 4.5) |
| 25 | Resend | Broadcast de lanzamiento (ver 4.6) |
| 26 | `scripts/productos-digitales/CALENDARIO-V2-SEMANAL.md` | Anotar el slot |

**Gates a correr antes de dar OK:** `whatsapp-gate.py` (exactamente 1 botón por página; la landing y el dashboard pasan
`whatsapp={false}`) · `robots-gate.py` · `gate-flujo-postpago.py` · `censo-entregables.py --fail` ·
`audit-payment-links.py` / `sync-payment-links.py` · `sync-product-prices.py` · el gate de páginas de `documentos.py`.

## 4.3 Buscador: el alias que hace falta (y una ironía)

**El buscador del hub ya ofrece «montar una pastelería» como ejemplo animado del placeholder**
(`ProductosDigitalesHubPage.astro:2259`, dentro de la lista `ejemplos` de `placeholderAnimado()`). Es decir: **el hub
lleva meses invitando al visitante a teclear la búsqueda de un producto que no existe.** Hoy esa consulta cae en la
tarjeta de `comingSoon` (que sí entra en el índice, `:985`). Al lanzar, cae en el producto real: el ejemplo pasa de
promesa a acierto. Buen argumento para no retrasarlo más.

**Alias que propongo** en `sinonimos-buscador.json` → `alias`:

```
"/guia-pasteleria-obrador": "abrir montar una pasteleria obrador reposteria pasteleria en casa
                             cake design tartas por encargo vitrina licencia maquinaria"
```

Razón: el índice de la card se construye con `indiceBusqueda([name, description, features, tags, tagLabel, slug,
ALIAS_BUSQUEDA[slug]])` (`:977`) y **normaliza sin acentos** (`normalizarBusqueda`, `normalizar-busqueda.ts:36-43`).
Las consultas de la SERP heredada («repostería desde casa», «cake design», «requisitos obrador») no aparecerían
literalmente en el copy. El tag `pasteleria` ya existe (`:50`), y `panaderia` (`:51`) etiqueta «Panadería / Obrador».

## 4.4 🔴 Páginas de rol: dos miswirings vivos

Censo de `src/data/use-cases-content.es.ts` (**51 bloques con `productIds`**):

| Página | Línea de `productIds` | Qué lleva hoy |
|---|---|---|
| `pasteleria-obrador` | **2698** | `kit-tareas-pasteleria`, `kit-escandallos`, `pack-appcc`, `kit-inventario`, `kit-gestion-personal`, `pro-prompts-ebook` |
| `repostero-pastelero` | **2034** | *exactamente los mismos 6* |
| `panadero` | **1153** | *exactamente los mismos 6* |
| `chocolateria` / `chocolatero` | — | los mismos, con `kit-tareas-chocolateria` en lugar del de pastelería |

**Defecto 1 — la página del panadero vende el kit de pastelería.** `panadero` (`:1153`) lleva `kit-tareas-pasteleria`
**y no `kit-tareas-panaderia`**, que existe en el catálogo (`products-catalog.ts:439`). Todo el cuerpo de la página
habla de masa madre, hidrataciones y coste hora de obrador de panadería (`:1115-1219`), y el producto que ofrece es el
de otro oficio.

**Defecto 2 — `guia-panaderia-obrador` está huérfana de las 51 páginas de rol.** De los 51 bloques, **9 citan una guía
«Cómo Montar»** (`:2584` dark-kitchen, `:3469`/`:4893`/`:4999` gastronómico, `:3580` mexicano, `:3690` peruano,
`:3800`/`:4350` japonés, `:3910` nikkei) y **`guia-panaderia-obrador` no aparece en ninguno** — ni siquiera en la del
panadero. Es una guía de 65 € sin una sola entrada desde el clúster de casos de uso.

**Regla para el 48 (regla capital: cero huérfanas):** `guia-pasteleria-obrador` entra en los `productIds` de
**`pasteleria-obrador` (:2698)**, **`repostero-pastelero` (:2034)** y, si la guía cubre la variante pastelería-cafetería,
también en la de cafetería. Y de paso se arreglan los dos defectos de arriba (`panadero` → `kit-tareas-panaderia` +
`guia-panaderia-obrador`), que es un cambio de dos líneas.

*Precedente: la D21 del Manual del Chef Ejecutivo hizo justo esto — entró en `chef-ejecutivo` (:377), `chef-cocina`
(:491), `sous-chef` (:602), `chef-catering` (:712) y `fb-manager-hotel` (:1484). El molde existe y funciona.*

## 4.5 Blog: los 6 posts ya tienen sus 3 banners — hay que sustituir, no añadir

Medido sobre `astro-site/src/content/blog/es/` (hrefs relativos `?utm_source=blog&utm_medium=banner`):

| Post | Banner 1 | Banner 2 | Banner 3 | Sustitución quirúrgica |
|---|---|---|---|---|
| `libreria-de-prompts-para-pastelero-consultor-pro-ai` | `kit-tareas-pasteleria` | `kit-plan-financiero` | `kit-escandallos` | **3 → guía** (plan financiero está dentro de la guía) |
| `libreria-de-prompts-para-pasteleria-creativa-ai` | `kit-tareas-pasteleria` | `kit-escandallos` | `pro-prompts-ebook` | **3 → guía** |
| `ai-chef-pro-un-chatgpt-para-la-pasteleria-profesional-usos-y-aplicaciones` | `kit-tareas-pasteleria` | `kit-tareas-panaderia` | `guia-restaurante-gastronomico` | **3 → guía** (un post de pastelería que vende una guía de restaurante gastronómico es el peor encaje de los seis) |
| `libreria-de-prompts-para-panadero-consultor-pro-ai` | `kit-tareas-pasteleria` | `kit-plan-financiero` | `kit-escandallos` | Post de panadería: el banner 1 debería ser `kit-tareas-panaderia`; el hueco natural es para `guia-panaderia-obrador`, **no** para el 48 |
| `ia-para-panaderias` | `kit-tareas-panaderia` | `kit-plan-financiero` | `plan-catering-tematico-eventos` | **3 → `guia-panaderia-obrador`** (catering temático en un post de panadería no encaja). No es el 48 |
| `libreria-de-prompts-para-chocolateria-creativa-ai` | `kit-tareas-chocolateria` | `kit-escandallos` | `pro-prompts-ebook` | Sólo si la guía cubre bombonería |

**Ganancia neta para el 48: 3 banners** en los tres posts de pastelería. **Herramienta:** `fase8e-banners-corpus.py`
inserta pero **no sustituye**; para cambiar un banner ya publicado hace falta una pasada quirúrgica del estilo `fase8h`
que se usó con el Manual del Chef Ejecutivo. **Prohibido reejecutar `fase8c-libreria-assemble.py`**: reconstruye el
cuerpo desde el `.txt` de bridge y pisa las ediciones manuales.

⚠️ **No prometer tráfico SEO.** Con los datos heredados del brief («como montar una pasteleria» = 10/mes, «montar una
pasteleria» = 20/mes) la conclusión es la misma que en los tres productos anteriores: **el canal es propio** (hub,
buscador del hub, lista de compradores, blog, páginas de rol, plataforma).

## 4.6 Resend: dónde cabe el correo de lanzamiento

Cola escrita en `CALENDARIO-V2-SEMANAL.md` §0-ter (regla: último `scheduled_at` **+ 5 días**, 08:00 UTC / 10:00 Madrid):

| Fecha | Correo | Estado |
|---|---|---|
| 14-sep | Manual del Chef Ejecutivo (lanzamiento) | programado |
| 19-sep | Bar-restaurante 2.1 | programado |
| 24-sep | Cafetería 2.2 | programado |
| 29-sep | Tapas-bar 2.2 | programado |
| 4-oct | Panadería 2.2 | programado |
| 9-oct | Food truck 2.2 | **BORRADOR** (Resend no admite > 30 días vista; programar a partir del 9-sep) |
| **14-oct** | **← hueco para la Guía de Pastelería** | libre |

**⚠️ Trampa:** el 14-oct está a **34 días** del 10-sep, fuera del tope de 30 días de Resend. **No se puede programar
todavía**: queda como borrador y se programa a partir del **14-sep**. Y al recrear cualquier correo: **leer el asunto
ANTES de borrar** y `json.loads(strict=False)` (el HTML trae caracteres de control) — la lección del 6-sep, en la que se
borraron cuatro correos a ciegas.

**Alternativa que merece plantearse a John:** un lanzamiento anunciado desde mayo con **4 meses de retraso visible**
compite mal con un aviso de versión. El precedente existe: la D28 del Manual del Chef Ejecutivo **adelantó el
lanzamiento y desplazó un hueco las cinco actualizaciones de planes**, con este argumento literal: *«un lanzamiento
anunciado desde mayo vende más que un aviso de versión y no debe esperar al 7-oct»*. Si se repite, la pastelería
saldría el **19-sep** o el **24-sep** y todo lo demás corre un hueco.

---

# 5. Propuesta de entregables

## 5.0 El juego de datos único

Patrón obligado (`guia-food-cost/datos_ejemplo.py:1-40`): **un solo `datos_ejemplo.py`** del que beben los 10
generadores, el guion y los bonus. *«Si un número cambia, cambia aquí y se regeneran los libros.»*

Propuesta (a firmar en la SPEC; los importes concretos los fija el research de datos, **no los invento aquí**):

| Campo | Propuesta | Por qué |
|---|---|---|
| Nombre | Pastelería de ejemplo **«La Clara»** | Nombre neutro, femenino, sin marca real. Paralelo a «La Encina» de Food Cost |
| Formato | Pastelería con **obrador propio + despacho a calle**, ciudad media española | Es el caso central del brief; las 5 variantes se tratan como desviaciones sobre él |
| Superficie | **~110 m²**: obrador ~55, despacho/tienda ~25, cámara/almacén ~15, aseos + vestuario ~15 | Coherente con el «mínimo 80 m²: obrador + tienda» del checklist F2 de `plan-negocio-panaderia`, subido por el frío de pastelería. **Cifra a validar en el research** |
| Plantilla | Jefe pastelero · 1 oficial · 1 ayudante · 2 dependientes (1 a tiempo parcial) | **Coincide exactamente con los 4 perfiles del `04-tareas-perfiles.xlsx`** del kit → el cross-sell es literal |
| Carta | **30 referencias** en 5 familias: bollería · pastelería individual · tartas y entremets · panes de acompañamiento · temporada | Las 3 primeras deben incluir croissant, pain au chocolat y napolitana de crema, que son las que el `10-plan-produccion-semanal.xlsx` y el `12-control-alergenos-vitrina.xlsx` ya traen precargadas |
| Coherencia externa | Tarta de chocolate 70 %, croissants y macarons con **el mismo escandallo** que `kit-escandallos/05-pasteleria.xlsx` | Un cliente que tenga los dos productos vería dos costes distintos del mismo croissant. **Copia declarada, no vínculo** (regla D4/D8) |

## 5.1 Los 10 libros de Excel

Restricciones de familia: **prohibidos** `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA` y las
referencias entre libros. **Cero constantes dentro de fórmulas**; parámetros en celda verde. `COUNTIF` sí se usa
(los checklists del molde B lo hacen). Todos con hoja `Instrucciones` y `inject_cache.py` al final.

| # | Libro | Hojas | Entradas (verde) | Salidas por fórmula | **Decisión que permite tomar** | Dolor / norma | Frontera |
|---|---|---|---|---|---|---|---|
| 1 | `capacidad-obrador-y-local.xlsx` | Parámetros · Zonas y m² · Capacidad por Equipo · Cuello de Botella · Ficha de Visita a Local | m² por zona, litros de amasadora, bandejas de horno, m³ de cámara y de abatidor, horas de turno | m² totales y % obrador/venta, piezas/día por equipo, **el equipo que limita**, piezas/día del conjunto, ¿aguanta el pico? | **¿Este local me sirve y qué equipo tengo que comprar sí o sí?** | Se firma un alquiler antes de saber si cabe el obrador. Reserva de vestuarios y aseos (RD 486/1997) | **Nada equivalente en el catálogo.** El kit organiza la producción en el obrador que ya tienes |
| 2 | `calculadora-capex-pasteleria.xlsx` | Parámetros · CAPEX por Bloque · Variante del Formato · IVA y Tesorería · Resumen | importe por partida (mín/máx/tuyo), variante elegida, tipo de IVA por línea | total por bloque, total CAPEX, **IVA soportado y cuándo se recupera**, CAPEX por variante | **¿Cuánto necesito y qué es prescindible?** | Molde `guia-panaderia-obrador/calculadora-capex` (3 fórmulas) **mejorado** con la columna «¿Lleva IVA?» de `plan-negocio-panaderia` | Contenido 100 % pastelería: abatidor, cámara de fermentación controlada, laminadora, atemperadora, vitrina refrigerada, batidora planetaria |
| 3 | `estacionalidad-y-picos.xlsx` | Parámetros · Calendario de 6 Picos · Peso sobre el Año · Capacidad vs Demanda del Pico · Refuerzo y Tesorería | ventas estimadas por pico, precio y unidades, personal de refuerzo, antelación de compra | % de facturación de cada pico sobre el año, **déficit de capacidad en el pico** (contra el libro 1), coste del refuerzo, **tesorería inmovilizada en stock de temporada** | **¿Aguanto Reyes y las comuniones, y con cuánto dinero parado?** | El calendario del kit dice *«Roscón — pico máximo del año»* pero no cuantifica nada. Es **el riesgo nº 1 del formato** | **El libro más propio de todo el producto.** Ni panadería ni ningún restaurante lo tienen. Frontera R5: el `BONUS-02` da fechas; éste da euros |
| 4 | `carta-de-apertura-y-escandallo.xlsx` | Parámetros (coste hora obrador) · Escandallo por Tanda (30 refs) · Coste Hora y Mano de Obra · Mix y Ticket Medio · Decisión de Surtido | precios de compra, gramaje, tanda, minutos de mano de obra, PVP, mix % | coste materia por pieza, **coste de mano de obra por pieza**, coste total, food cost %, margen €, aporte al ticket medio, **semáforo de surtido** | **¿Con qué 30 referencias abro y cuáles sobran?** | El cap. 17 de Food Cost dice *«una pieza de bollería puede llevar más euros de manos que de materia prima»*; el escandallo del kit **no incluye mano de obra** | Frontera con `kit-escandallos/05` (3 refs, sin mano de obra) y con Food Cost (método, sin herramienta de carta). Aquí: **carta completa + coste hora + decisión de surtido** |
| 5 | `plan-financiero-3-anos-pasteleria.xlsx` | 0. Supuestos · Inversión · PyG 3 Años · Punto de Equilibrio · Escenarios · Personal · **Tesorería 12 meses** · Financiación · Instrucciones | tickets/día, ticket medio sin IVA, días de apertura, estacionalidad mensual, rampa | P&L, punto muerto, 3 escenarios, coste de personal con SS, **tesorería mes a mes**, servicio de deuda | **¿Sale la cuenta y cuánto dinero necesito hasta el break-even?** | Es la fuente única de cifras del texto (§7-bis.7) | **Molde de `planes-v2_0` motor 2.2**, no el de la guía de panadería. La estacionalidad mensual del motor 2.2 es justo lo que la pastelería necesita |
| 6 | `mix-de-canales-y-punto-muerto.xlsx` | Parámetros · Mostrador · Encargos · B2B (hoteles/cafeterías) · Online y Envío · Punto Muerto por Canal | ventas y margen por canal, coste de servir cada canal, comisión de plataforma | margen de contribución por canal, **punto muerto con y sin B2B**, canal que sostiene el negocio | **¿Necesito B2B para llegar, o el mostrador basta?** | Las 5 variantes del formato se juegan aquí. El obrador B2B/online es una de ellas | Nada equivalente. `calculadora-ticket-medio` sólo mezcla producto, no canal |
| 7 | `checklist-legal-y-licencias.xlsx` | 6 fases (F1-F6) + contador | ✓/☐/N/A, fecha, responsable, coste | contador por fase y total, % de avance | **¿Qué me falta para poder abrir?** | Molde B + molde de fases de `plan-negocio-panaderia/checklist-apertura-panaderia` | Contenido a **verificar en el research legal**: RGSEAA, licencia de actividad, obrador anexo a despacho, extracción, epígrafe de IAE. **No copiar el 644.1/419.1 de panadería sin contrastar** |
| 8 | `checklist-equipamiento-y-proveedores.xlsx` | Equipamiento (con mín/máx y prioridad) · Variante del Formato · Proveedores (materia prima) · Contador | ✓, precio real negociado, proveedor, plazo de entrega | contador, desviación contra el CAPEX del libro 2, **plazo crítico** | **¿Qué compro, a quién, y qué plazo me retrasa la apertura?** | El brief lo pide literalmente («maquinaria, proveedores») y **es una keyword medida**: «maquinaria pasteleria» 70/mes (heredado) | Molde B de `checklist-equipamiento`. La columna de **plazo** es nueva: una laminadora a 8 semanas mueve la fecha de apertura |
| 9 | `cronograma-apertura-gantt.xlsx` | Gantt (hitos × meses) · Ruta Crítica · Fecha de Apertura | fecha de inicio, duración de cada hito | mes de cada hito, **ruta crítica**, fecha de apertura estimada, **aviso si cae fuera de pico** | **¿Cuándo abro, y estoy abriendo en el peor mes?** | Abrir una pastelería en julio y llegar a Reyes sin rodaje. La estacionalidad hace que la **fecha** sea una decisión de dinero | Molde `cronograma-apertura-gantt` (0 fórmulas hoy) → aquí **con** fórmulas |
| 10 | `plantilla-turnos-y-coste-personal.xlsx` | Parámetros (convenio, SS %) · Turnos Semanales · Horas y Coste · Plan de Contratación | horas por persona y día, bruto de convenio, % de SS, fecha de alta | horas semanales por persona y total, **coste mes y año con SS**, aviso si se pasa de jornada, coste del refuerzo de pico | **¿Cuánta gente, cuándo la contrato y cuánto cuesta de verdad?** | Molde `plantilla-turnos-brigada` **tiene 0 fórmulas**: no calcula ni horas ni coste. La SS se olvida y hunde el P&L (defecto DOM-02 del representante) | La plantilla coincide con los 4 perfiles del `04-tareas-perfiles.xlsx` del kit → frontera R6: el kit dice *qué hace* cada perfil; éste dice *cuántos y cuánto cuestan* |

**Cobertura de la promesa del hub** («obrador, vitrina, maquinaria, proveedores, licencias y lanzamiento»):
obrador → 1, 3 · vitrina → 4, 6 (+ el libro 12 del kit) · maquinaria → 2, 8 · proveedores → 8 · licencias → 7 ·
lanzamiento → 9. **Los seis sustantivos quedan cubiertos.**

## 5.2 La guía: 20 capítulos

Presupuesto: **~37.000 palabras**, 1.700-1.850 por capítulo, `paginas_prometidas: 70`, `min_palabras_cap: 1.300`.
Cada capítulo con `puntos_por_epigrafe` (§3.3).

| # | Capítulo | Libro que usa |
|---|---|---|
| 1 | Qué negocio estás montando: las 6 variantes y cuál te toca | — |
| 2 | El cliente y la plaza: quién compra pastelería y cuándo | 3 |
| 3 | La carta de apertura: 30 referencias y por qué esas | 4 |
| 4 | Cuánto cuesta abrir: el CAPEX real, partida a partida | 2 |
| 5 | El local: metros, zonas y la ficha de visita | 1 |
| 6 | Antes de firmar el alquiler (el capítulo que ahorra el dinero) | 1, 7 |
| 7 | El obrador por dentro: frío, calor y flujo de trabajo | 1 |
| 8 | Maquinaria: qué compras, qué alquilas y qué esperas a tener | 2, 8 |
| 9 | Licencias, sanidad y registro: el camino completo | 7 |
| 10 | APPCC y alérgenos: qué hay que tener el día de la inspección | 7 *(cita `pack-appcc` y el libro 12 del kit)* |
| 11 | Proveedores: materia prima, packaging y plazos | 8 |
| 12 | Escandallo y precios: por qué la mano de obra manda | 4 *(cita Food Cost cap. 17)* |
| 13 | El equipo: cuántos, qué perfiles y qué cuestan | 10 *(cita el libro 04 del kit)* |
| 14 | Turnos de madrugada y jornada legal | 10 |
| 15 | Los seis picos del año: Reyes, San Valentín, Padre/Madre, Semana Santa, comuniones, Todos los Santos | 3 |
| 16 | Encargos y comuniones como línea de negocio | 3, 6 *(cita el libro 11 del kit)* |
| 17 | Canales: mostrador, B2B, online y envío | 6 |
| 18 | El plan financiero y el dinero hasta el break-even | 5 |
| 19 | Financiación, IVA y tesorería del arranque | 5, 2 |
| 20 | Cronograma, apertura y los primeros 90 días | 9 *(cita todo el kit de tareas)* |

## 5.3 Los dos bonus — y uno que hay que descartar

**BONUS 1 — `business-plan-modelo-pasteleria.docx` (RELLENO).** El caso completo de «La Clara» con cifras: resumen
ejecutivo, mercado, concepto, plan de operaciones, plan financiero, análisis de riesgos con escenarios. Objetivo **≥
3.500 palabras y ≥ 8 tablas**, todas coherentes con el libro 5. Justificación: es el formato que pide un banco o una
línea ENISA, y la versión de panadería son **796 palabras y 0 tablas** (medido). La landing de panadería promete
«resumen ejecutivo, proyecciones financieras a 3 años y análisis de mercado» y no entrega ninguno de los tres.

**BONUS 2 — «12 decisiones de apertura resueltas» (PDF + DOCX).** ~25-30 páginas ≈ **10.500-12.000 palabras**. Molde
probado dos veces (`BONUS-12-situaciones-resueltas-cocina`, 34 págs / 15.762 palabras, medido). Doce decisiones reales,
cada una con contexto, opciones, criterio y la celda del libro que la resuelve. Candidatas:

1. Local con obrador vs obrador aparte · 2. Comprar el abatidor o esperar · 3. Abrir con 20 referencias o con 40 ·
4. Producto de terceros al arrancar: cuándo sí · 5. Cuánto roscón produzco el primer año · 6. Aceptar el primer
encargo de comunión sin histórico · 7. El primer contrato B2B, ¿a qué precio? · 8. Contratar oficial o tirar de
ayudante · 9. Abrir en septiembre o en febrero · 10. Cuándo meto el obrador en casa dentro de la legalidad ·
11. Envío a domicilio: qué producto viaja y cuál no · 12. Qué hago con lo que no se vende hoy.

**BONUS 3 (recetario de escandallos base de 20 referencias) — 🔴 lo descarto como bonus independiente.** Motivo:
un recetario con gramajes y costes que nadie ha cocinado es **exactamente el patrón de cifra inventada** que la casa
prohíbe, y no hay forma de citar fuente para el gramaje de una receta propia. **Alternativa sin riesgo:** las 30
referencias viven **dentro del libro 4** como datos de ejemplo declarados como tales («valores de ejemplo, sustitúyelos
por los tuyos» — la fórmula que ya usa el `LEGAL` del guion del representante), y sus 3 primeras coinciden con
`kit-escandallos/05-pasteleria.xlsx`. Se gana coherencia y se pierde un riesgo.

---

# 6. Presupuesto y riesgos de pipeline

## 6.1 Estimación de tokens

Referencias (del encargo y de `CALENDARIO-V2-SEMANAL.md` §0-ter; **no medidas por mí**): Guía Food Cost **9,7 M** ·
Manual del Manager **~10,5 M** · Manual del Chef Ejecutivo **~17 M**.

| Fase | Modelo | Estimación | Comparable |
|---|---|---|---|
| Research 6 lentes + refutación | opus (1 refutador, 2 lentes en el mismo prompt) | **1,5-2,0 M** | Ya en curso |
| SPEC + guion de 20 caps + `verificar_guion.py` | opus (SPEC) + sonnet (guion) | **1,5-2,0 M** | El guion del Chef llevó 281 referencias a celda verificadas |
| 10 generadores de xlsx + `datos_ejemplo.py` | sonnet | **2,5-3,0 M** | 7 libros del Chef; aquí son 10 y 3 son nuevos de raíz |
| Redacción: 20 caps × 2 bloques + 2 bonus ≈ **44 agentes** | sonnet, en paralelo | **5,0-6,0 M** | «≈ 5,5 M la redacción de una guía de 95 páginas» |
| Refutación de documentos + fixes | opus (1 pasada) + sonnet (fixes) | **2,0-3,0 M** | El Chef necesitó 27 fixes + desduplicación de 41 pares |
| Integración (26 superficies del §4.2) + gates | sonnet + Fable en lo crítico | **1,0-1,5 M** | — |
| **TOTAL** | | **13,5-17,5 M** | En la banda del Chef Ejecutivo |

**🔴 Aviso de presupuesto:** el techo es **~15 % de la cuota semanal** y «una semana normal debe quedarse por debajo de
1,5 M». Los tres productos nuevos anteriores ya lo rompieron (9,7 / 10,5 / 17 M) y el del Chef fue **una sesión
dedicada que John autorizó expresamente**. Este producto es **más caro que la media**: 10 libros (frente a 7-8) y 3 de
ellos sin molde previo. **Requiere luz verde explícita de John antes de arrancar la construcción, y probablemente dos
sesiones**: (A) research + SPEC + guion + los 10 xlsx; (B) redacción + refutación + integración.

## 6.2 Riesgos y trampas

| # | Riesgo | Estado | Mitigación |
|---|---|---|---|
| 1 | **`documentos.py` duplicaba prosa** (epígrafes repartidos, `puntos` no) | ✅ **ARREGLADO** en `:1096` y ss. (2026-09-10) pero **SIN COMMITEAR** (`git status` = ` M`) y **con otra sesión editándolo en vivo** (creció de 2.051 a 2.189 líneas durante esta auditoría) | **Commitear antes de nada.** Y usar `puntos_por_epigrafe` en el guion nuevo: ningún guion lo usa todavía |
| 2 | **Erratas falsas** («t» caída) | Vivo | `erratas_permitidas` / `erratas_forzadas` en `GUIA['gates']`. La reparación mira si la palabra correcta aparece en el resto del libro |
| 3 | **Títulos sin raya** (U+2011) y espacio fino (U+202F) | Vivo | `NARROW`/`NOBRK` por escape en `documentos.py:85-86`. **Nunca escribir el carácter en un heredoc**: degenera y ninguna sustitución encuentra su patrón |
| 4 | **xlsx a mano: prohibido** | Regla | Los 10 salen de `gen_*.py` + `inject_cache.py`. Gotcha `<v />` de openpyxl 3.1.x documentado |
| 5 | **El orden se invierte** (texto antes que xlsx) | Alto | `documentos.py:1986` lee `DL/<pid>/`. Los 10 libros **en `public/dl/` antes** de redactar |
| 6 | **bridge devuelve vacío** | Medio | `MODELO_FALLBACK = 'anthropic/claude-sonnet-4.6'` ya está en `:97`. Regla: si vuelve vacío dos veces, **cambiar de motor, no duplicar tokens**. *(Nota: la regla de John del 4-sep dice que los productos digitales NO van con bridge sino con subagentes Anthropic — `guias-v2-SPEC.md` §5.3 aún describe bridge y está **desactualizada**; el pipeline real es `dump_prompts.py` → agentes por bloque → `check_bloque.py`.)* |
| 7 | **La hermana rota** (panadería, PDF de 1 pág.) | 🔴 Alto | §2.2: o se arregla antes, o el copy no la menciona |
| 8 | **Duplicar alérgenos** | Medio | Regla R3: la guía sólo lleva una fila de checklist |
| 9 | **Cifras sin fuente** | Alto | Ids `PA-*` en `guias-v2-research-sector.json` con gate de recuento. Un id sin cifra es **hueco deliberado**: el capítulo se reformula sin número |
| 10 | **Precio de plan inventado** | Medio | La lección del post de integraciones: «incluido el plan gratuito» cuando **no hay plan gratuito** (el Miembro son 10 €/mes). Revisar toda mención al SaaS |
| 11 | **Purgar `.astro` al tocar frontmatter** | Bajo | Si se tocan los `.md` del blog: `rm -rf astro-site/.astro astro-site/dist` + `fase8b-regen-lastmod.py` |
| 12 | **`<a>` dentro de celda de tabla** | Bajo | `html_tabla` escapa el HTML. Enlaces en párrafo o viñeta, nunca en celda |

---

# 7. Preguntas para John

1. **La hermana rota.** `guia-panaderia-obrador` se vende a 65 € con «20 capítulos, 70+ páginas» y entrega **un PDF de
   1 página (55 palabras)** más un DOCX de 4.699 palabras. ¿Se arregla **antes** de lanzar pastelería (una sesión impar
   completa), **después**, o el copy de pastelería **no la menciona** hasta que esté? Yo recomendaría lo tercero para no
   bloquear el lanzamiento, con lo primero como deuda inmediata.
2. **Precio.** ¿**65 €**, como el resto de guías «Cómo Montar» y como la de panadería? Con 10 libros de Excel (frente a
   los 7-8 de los productos nuevos anteriores) hay argumento para 65 €, pero es tu decisión.
3. **Slug.** ¿`guia-pasteleria-obrador` (paralelo a panadería, ya cubierto por `robots.txt`) o prefieres otro? Si el
   slug estrenara un prefijo distinto de `guia-`, habría que añadir sus dos líneas al `robots.txt`.
4. **Alcance de las variantes.** El brief lista 6 formatos (obrador propio, pastelería-cafetería, sin obrador,
   B2B/online, boutique de autor, cake design, «obrador en casa»). La SERP heredada apunta fuerte a **«desde casa»**.
   ¿Capítulo propio para la variante doméstica, o sólo un epígrafe? Cambia el alcance legal del producto.
5. **Presupuesto.** Estimo **13,5-17,5 M tokens**, por encima del techo semanal del 15 %. ¿Luz verde para **dos
   sesiones** (A: research + SPEC + guion + 10 xlsx · B: redacción + refutación + integración), como se hizo con el
   Chef Ejecutivo?
6. **Cola de Resend.** El hueco natural es el **14-oct**, pero está a 34 días y Resend no admite programar a más de 30.
   ¿Se deja como borrador, o se **adelanta el lanzamiento** (19-sep o 24-sep) desplazando un hueco las actualizaciones
   de planes, como se decidió el 6-sep con el Chef Ejecutivo?
7. **Cripto.** ¿El 48 nace con NOWPayments activado (regla del 6-sep) aunque el pago real de prueba siga pendiente?
   Si para entonces se aplicó la réplica a los 46, no hay que hacer nada.
8. **Los dos defectos colaterales.** ¿Autorizas arreglarlos en el mismo commit? (a) la página de rol `panadero` vende
   `kit-tareas-pasteleria` en vez de `kit-tareas-panaderia`; (b) `guia-panaderia-obrador` no aparece en ninguna de las
   51 páginas de rol. Son dos líneas.
9. **El kit infravendido.** `kit-tareas-pasteleria` entrega **15 xlsx** y el hub lo anuncia como **«9 checklists»**.
   ¿Actualizo la descripción en los dos ficheros del hub al tocarlos?
10. **`documentos.py` está modificado y sin commitear**, y creció 138 líneas durante esta auditoría. ¿Hay otra sesión
    trabajando en él ahora mismo? Conviene commitear el arreglo de `repartir_puntos()` antes de que se pierda.

# 8. Resumen ejecutivo

1. **El hueco de mercado interno existe y es limpio.** No hay `plan-negocio-pasteleria`, no hay guía de apertura de
   pastelería, y los tres activos cercanos (kit de tareas 12 €, escandallos 12 €, APPCC 14 €) resuelven **operar**, no
   **abrir**. La frontera se puede escribir sin ambigüedad.
2. **El molde está construido y no hay que tocar el pipeline.** `documentos.py` acepta el producto por convención de
   nombre; los gates, el `tipo_doc` y el fallback de motor ya existen.
3. **Hay dos defectos vivos que este lanzamiento debería arreglar de paso**, ambos de dos líneas: la página de rol del
   panadero vende el kit equivocado, y la guía de panadería de 65 € está huérfana de las 51 páginas de rol.
4. **Y uno que no es de dos líneas:** la guía de panadería entrega un PDF de 1 página contra una promesa de «70+
   páginas». Es una decisión de John si se arregla antes, después, o si el copy de pastelería la esquiva.
5. **El coste estimado (13,5-17,5 M tokens) está por encima del techo semanal** y necesita luz verde y, muy
   probablemente, dos sesiones.
