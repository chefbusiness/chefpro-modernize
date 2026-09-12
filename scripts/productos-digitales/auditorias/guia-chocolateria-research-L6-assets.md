# LENTE 6 — Activos propios, frontera, canales y propuesta de entregables
## «Cómo Montar una Chocolatería» (producto nuevo nº 5, sería el **49** del catálogo)

| Campo | Valor |
|---|---|
| Producto en diseño | «Cómo Montar una Chocolatería» — línea «Cómo Montar», hermana de `guia-pasteleria-obrador` y `guia-panaderia-obrador` |
| Fecha del informe | **2026-09-12** |
| Lente | L6 — auditoría de lo que ya vendemos, frontera, canales y propuesta de entregables |
| Autor | Subagente de research (Claude Code) · orquestado por Fable |

### Método

1. **Lectura directa de ficheros del repo**, no de documentación: `openpyxl` con `read_only=True, data_only=True`
   (un libro cada vez), `PyMuPDF` para los PDF, `zipfile`+regex sobre `word/document.xml` para los DOCX, y
   `grep`/`sed` para el código.
2. **Todo lo medido lleva el método al lado.** Cuando digo «medido hoy» significa que lo he contado yo en esta
   sesión sobre el fichero en disco, y doy la ruta.
3. **Las cifras de demanda** (volúmenes, SERP) **no las he medido yo**: vienen del briefing del orquestador
   (DataForSEO, España, consulta del 2026-09-12) y se citan como tales. No he hecho ni una llamada de red.
4. Térmica: `istats cpu temp` antes y después de cada tanda. Registro real de la sesión: **54,9 → 57,8 → 59,1 →
   59,3 → 58,8 → 60,2 → 59,6 → 61,0 → 67,4 (pico, tras PyMuPDF) → 66,4 → 63,4 °C**. Se paró la lectura pesada al
   superar los 65 °C y el resto del trabajo se hizo con `grep`.

### Limitaciones declaradas (lo que NO he podido verificar, y por qué)

| # | No verificado | Por qué | Consecuencia |
|---|---|---|---|
| L-1 | **Registro de búsquedas del hub** (¿alguien buscó «chocolatería»?) | `buscador-report.py` habla con Netlify Blobs vía `curl` y **exige `ADMIN_PASSWORD`**, que está marcada como secreta en Netlify (`scripts/productos-digitales/buscador-report.py:30-34`). El encargo es 100 % local, sin red | **Dato pendiente, y es barato**: una sola ejecución con la clave de John dice si la demanda está registrada. Hasta entonces, «sin fuente» |
| L-2 | **Posiciones y clics en GSC** de la línea `guia-*` y de las URLs de chocolate | Requiere red (MCP `gscServer`) | Se hereda el dato de Pastelería citado en su SPEC (7 clics / 386 impresiones en 90 días) **como referencia de la línea, no como medición de hoy** |
| L-3 | **Nombres reales de los agentes de chocolate en Pickaxe** | La fuente autorizada es la plataforma, no el repo (`CLAUDE.md`) | «Chocolatero Consultor Pro» y «Chocolatería Creativa» se citan **como nombres del repo**, a confirmar contra `fase8c-agentes/catalogo-hub.json` antes de escribir copy |
| L-4 | **Todo lo normativo del chocolate** (RD 1055/2003, cadmio, EUDR, ICCO) | Es la lente L3 (verificación legal), no ésta. Aquí sólo se dice **qué entregable lo necesitaría** | Ningún literal legal de este informe es citable: **todos van marcados «pendiente de L3»** |
| L-5 | **Precios de maquinaria de chocolate** (atemperadora, melanger, túnel) | Requiere red | Los entregables se proponen con **celda verde vacía y su columna de IVA**, nunca con precio inventado |

---

## 1. Inventario exacto de los activos hermanos

### 1.1 `kit-tareas-chocolateria` — 12 €, 11 xlsx (el hub anuncia «9 checklists»)

Medido hoy con `openpyxl` sobre `astro-site/public/dl/kit-tareas-chocolateria/`.

| Fichero | Hojas (filas×cols) | Qué cubre | Fórmulas |
|---|---|---|---|
| `01-apertura-cierre.xlsx` | Instrucciones · Apertura 41×7 · Cierre 30×7 | Uniforme, lavado de manos, **encendido de extracción**, temperaturas de arranque; cierre de vitrina («cubrir bombones expuestos»), arqueo, **limpieza y secado de temperadora** | 4 |
| `02-partidas-produccion.xlsx` ⭐ | Instrucciones · **Templado 36×7** · **Moldeado 49×7** | Stock de cobertura negra/leche/blanca, **T y HR del obrador**, pesado, curva de templado; moldeado (verter, vaciar, invertir, **enfriar a 12-14 °C 10-15 min**, rellenar al 80 %, sellar) | 4 |
| `03-tareas-manager.xlsx` | Instr. · Diario 29×7 · Semanal 43×7 · Mensual 26×7 | Agenda de encargos, briefing, **temperaturas de obrador/cámara/vitrina**, pedidos online overnight; food cost mensual, análisis de ventas por categoría (bombones…) | 6 |
| `04-tareas-perfiles.xlsx` | Instr. · **Chocolatero** 30×7 · **Dependiente** 33×7 · **Encargado** 26×7 | **Los 3 perfiles del kit.** Ojo: chocolatería tiene **3**, pastelería **4** | 6 |
| `05-tareas-semanales-mensuales.xlsx` | Instr. · Semanal 37×7 · Mensual 28×7 · Trimestral y Anual 28×7 | Cadencias largas | 6 |
| `06-eventos-temporada.xlsx` ⭐ | Instr. · **Navidad** 29×7 · **San Valentín** 26×7 · **Pascua** 27×7 | Preparación (catálogo, moldes, packaging, preventa, **fecha límite de encargos**) + producción, por campaña | 6 |
| `07-plantilla-personalizable.xlsx` | Instr. · Por Zona · Por Turno · Por Perfil (31×7 cada una) | Plantilla en blanco | 6 |
| `08-apertura-cierre-negocio.xlsx` | Instr. 45×2 · Apertura 30×8 · Cierre 28×8 | Apertura/cierre **del negocio** (con firma) | 4 |
| `09-apertura-cierre-caja.xlsx` | Instr. 56×2 · Apertura 28×7 · Cierre 59×7 · **Registro Mensual 38×10** | Arqueo, Z del TPV, descuadre, depósito | **95** |
| `BONUS-01-briefing-servicio.xlsx` | Instr. · Briefing 35×7 | Briefing de servicio | 2 |
| `BONUS-02-calendario-anual-tareas.xlsx` ⭐ | Instr. · **Calendario 18×6** | **Los 12 meses con acciones clave, productos destacados y temporada (Alta/Media/Baja)**. Alta: feb, mar, abr, may, oct, nov, dic. **Baja: agosto**. Media: ene, jun, jul, sep | **0** |

**Total medido: 11 ficheros · 139 fórmulas en todo el kit** (95 de ellas en el libro 9, el del arqueo).
Fuera de ese libro, **44 fórmulas en 10 ficheros**: el kit es papel, no calculadora.

**Qué le falta desde la óptica de quien ABRE:** todo. No hay un solo euro, ni un m², ni una decisión de compra,
ni un trámite. El kit es **operación diaria de un negocio que ya existe**.

**Dato de oro que hay que reutilizar (no rehacer):** el `BONUS-02` ya fija el **calendario del chocolate español**
—y con él el **valle de verano**, que es lo que separa a la chocolatería de la pastelería—: julio «temporada
turística, packs souvenir» (Media), **agosto «producción reducida, planificación Q4» (Baja)**, junio «adaptar
catálogo (calor)» (Media). La guía pone los **euros** de ese calendario; el kit pone las **fechas**.

> ⚠️ **La descripción del hub miente por defecto**: `ProductosDigitalesHubPage.astro:806` dice «**9 checklists**»
> y hay **11 ficheros**. Es el mismo defecto que D31 corrigió sólo en pastelería (allí eran 15 anunciados como 9).
> **Corregirlo en la misma pasada de esta guía**, en los dos ficheros del hub.

### 1.2 `guia-pasteleria-obrador` — 65 €, el MOLDE (8 xlsx + 3 documentos)

Medido hoy sobre `astro-site/public/dl/guia-pasteleria-obrador/`.

| # | Libro | Hojas | Fórmulas (medidas) | **¿De FAMILIA o de PASTELERÍA?** |
|---|---|---|---|---|
| 1 | `capacidad-obrador-y-local.xlsx` | Instrucciones · Parámetros · **Zonas y m2** 37×7 · **Capacidad por Equipo** 26×16 · **Cuello de Botella** 32×10 · **Ficha de Visita a Local** 40×10 | **152** | **FAMILIA en la ESTRUCTURA, contenido nuevo entero.** Las 7 zonas de pastelería (fermentación, horno) no son las del chocolate; el «cuello de botella» pasa de horno/abatidor a **atemperadora/túnel de frío**; y la ficha de visita **cambia de signo**: la «prueba de humos» y la salida a cubierta son el criterio eliminatorio de pastelería y **un obrador de chocolate no tiene hornos ni fritura**. En su lugar entran **cámara a 16-18 °C, humedad relativa y estabilidad térmica**, que pastelería no mide |
| 2 | `calculadora-capex-pasteleria.xlsx` | Instr. · Parámetros · **CAPEX por Bloque** 61×15 · **Variante del Formato** 31×15 · **Traspaso vs Obra Nueva** 49×10 · **IVA y Tesorería** 30×5 · Resumen | **323** | **FAMILIA casi tal cual.** La mecánica (mín/máx/tuyo, «¿lleva IVA?» + tipo por línea, traspaso vs obra a 5 años, IVA soportado y cuándo vuelve) es transversal. **Cambian las partidas y las variantes**: bean-to-bar mete tostadora, descascarilladora, melanger/refinadora y conchadora, que no existen en pastelería |
| 3 | `estacionalidad-y-picos.xlsx` | Instr. · Parámetros · **Calendario de 6 Picos** 17×18 · **Peso sobre el Año** 34×9 · **Capacidad vs Demanda del Pico** 19×17 · **Refuerzo y Tesorería** 20×18 | **292** | **FAMILIA en la estructura; el contenido es OTRO.** Los picos de pastelería son Reyes, San Valentín, Padre/Madre, Semana Santa, comuniones y Todos los Santos. Los del chocolate son **Navidad+Reyes, San Valentín, Pascua (monas y huevos), Día de la Madre, Halloween** y, sobre todo, **el VALLE de julio-agosto**, que en pastelería no es un capítulo y aquí lo es: calor, envíos imposibles y cierre. **La hoja que falta es «valle», no otro pico** |
| 4 | `carta-de-apertura-y-escandallo.xlsx` | Instr. · Parámetros 93×7 · **Escandallo por Tanda** 266×13 · **Coste Hora y Mano de Obra** 43×19 · **Decisión de Huevo y Temperatura** 64×15 · **Mix y Ticket Medio** 53×13 · **Decisión de Surtido** 50×11 | **1.929** (el libro más denso del pack) | **FAMILIA en el motor de escandallo; la hoja estrella NO aplica.** «Decisión de Huevo y Temperatura» es el diferencial de pastelería (art. 9 del RD 1021/2022) y **en chocolate no pinta nada**: el bombón no lleva huevo crudo. Su **hueco funcional** en chocolate es otro y es igual de propio: **aw / vida útil del relleno y temperatura de conservación**. El motor (coste por tanda, merma, coste hora de obrador imputado por unidad, mix, food cost, veredicto de surtido) se hereda entero |
| 5 | `plan-financiero-3-anos-pasteleria.xlsx` | Instr. · 0. Supuestos 65×3 · Inversión Inicial · PyG 3 Años · Punto de Equilibrio · Escenarios · Personal 32×11 · **Tesorería 12 meses** 34×15 · Financiación 126×8 · **Canales y Punto Muerto** 31×10 | **1.022** | **FAMILIA tal cual** (molde `planes-v2_0` motor 2.2 + hoja propia). Cambian los **canales**: pastelería tiene 4 (mostrador, encargos, B2B, envío); chocolate tiene **5** y dos son suyos —**regalo corporativo** y **talleres/catas**— con estacionalidad y días de cobro radicalmente distintos |
| 6 | `checklist-legal-y-licencias.xlsx` | Instr. · Checklist Legal (F1-F6) 75×11 · **Árbol de Registro Sanitario** · **Suministro a Otros Minoristas** 49×6 · **Ruta Doméstica** 57×3 · Registro de Formación 21×8 · **Cronograma y Ruta Crítica** 84×15 | **299** | **FAMILIA en 5 de 6 hojas.** El árbol de registro sanitario, el árbol del art. 3 (suministro a otros minoristas), la ruta doméstica, el registro de formación y el Gantt con ruta crítica valen igual. **Lo que cambia el producto entero**: el obrador de chocolate **no tiene salida de humos ni hornos**, así que la licencia de actividad es otra conversación; y aparecen **tres frentes que pastelería no tiene** — denominaciones legales del cacao, cadmio y EUDR (§5.8) |
| 7 | `checklist-equipamiento-y-proveedores.xlsx` | Instr. · Equipamiento 74×23 · Variante del Formato 56×13 · Proveedores 31×12 · Contador 51×6 | **352** | **FAMILIA en el molde B.** Cambian los **9 proveedores sembrados** (Sosa, Puratos, Barry Callebaut, Valrhona, Debic, Elle & Vire, Ylla 1878, Farinera Coromina, Cospan → aquí manda el eje **cobertura/cacao**) y hay que **añadir dos columnas que pastelería no necesita**: declaración EUDR del proveedor y analítica de cadmio |
| 8 | `plantilla-turnos-y-coste-personal.xlsx` | Instr. · Parámetros 32×7 · Turnos Semanales 38×15 · Horas y Coste 36×14 · Plan de Contratación 46×11 | **188** | **FAMILIA tal cual.** Cambian los **perfiles** (el kit de chocolatería tiene **3**: Chocolatero, Dependiente, Encargado — no los 4 de pastelería) y **desaparece el turno de madrugada**, que en pastelería es un capítulo entero (cap. 14) y en chocolate no existe |

**Total medido: 8 libros · 4.557 fórmulas** (el handoff de Pastelería registra 4.556; la diferencia de 1 es de
método de conteo, no de contenido — cuento cualquier cadena que empiece por `=` en cualquier hoja).

**Documentos, medidos hoy con PyMuPDF y `zipfile`:**

| Fichero | Páginas | Palabras | **Palabras/página** | Tablas |
|---|---|---|---|---|
| `guia-pasteleria-obrador.pdf` | **103** | 56.168 | **545,3** | — |
| `guia-pasteleria-obrador.docx` | — | 53.790 | — | **44** |
| `BONUS-12-decisiones-de-apertura.pdf` | **37** | 16.842 | **455,2** | — |
| `BONUS-12-decisiones-de-apertura.docx` | — | 16.053 | — | **12** |
| `business-plan-modelo-pasteleria.docx` | — | **7.415** | — | **9** |

> **Calibración para presupuestar la guía de chocolatería:** cuerpo **545 pal/pág**, bonus **455 pal/pág**. Encaja
> con la banda que la SPEC de Pastelería midió sobre los productos ya publicados (529-544 cuerpo, 406-464 bonus,
> `guia-pasteleria-SPEC.md:83`). Y confirma la lección: **el guion presupuestó 37.500 palabras y salieron 56.168
> — un +49 %**, todavía peor que el +30 % que la SPEC daba por hecho.

> ⚠️ **Aviso de estado, no de diseño:** los 13 entregables y la ficha `guia-pasteleria-obrador.ts` están
> **modificados y SIN COMMITEAR** en el árbol de trabajo (`git status --porcelain` los marca ` M`), y el
> `CALENDARIO-V2-SEMANAL.md:141-143` dice que el producto está **en `main` LOCAL, sin push, esperando el Payment
> Link de John**. La ficha ya publica **103 y 37 páginas**, que coincide con lo que acabo de medir: el fixer de la
> refutación **ya corrió**. Pero mientras no se commitee, esto es trabajo que un apagón se lleva
> (`feedback_commitear-wip-de-subagentes-…`).

### 1.3 `kit-escandallos` (12 €) — **confirmado: NO tiene hoja de chocolatería**

Contenido real de `astro-site/public/dl/kit-escandallos/` (13 ficheros): `01-escandallo-estandar`,
`02-menu-degustacion`, `03-menu-del-dia`, `04-cocktails-bebidas`, **`05-pasteleria`**, `06-catering`,
`07-cafeteria-brunch`, `08-food-truck`, `09-control-mermas`, `10-calculadora-pvp`,
`11-dashboard-food-cost-mensual`, `BONUS-guia-food-cost-30-dias.pdf`, `BONUS-mermas-inventario`.

**No hay `chocolateria.xlsx` ni nada equivalente.** El escandallo de chocolate —con merma de templado, recortes
recuperables, coste por molde y precio por caja frente a por unidad— **no existe hoy en el catálogo**. Es hueco
libre, y es exactamente el hueco que llena el libro 4 de la guía.

### 1.4 `pack-appcc` (14 €) — qué cubre del obrador de chocolate

21 ficheros. Reparto desde la óptica de un obrador de chocolate:

- **Aplica y hay que CITAR, no rehacer:** `01-registro-temperaturas-diario`, `02-registro-temperaturas-recepcion`,
  `03-plan-limpieza-desinfeccion`, `04-registro-limpieza-diaria`, `05-checklist-recepcion-mercancias`,
  `06-registro-trazabilidad`, `07-control-plagas-ddd`, `08-matriz-alergenos`, `10-control-agua-potable`,
  `11-registro-acciones-correctivas`, `12-analisis-peligros-haccp`, `13-checklist-higiene-personal`,
  `14-fichas-14-alergenos`, `15-guia-inspeccion-sanidad`, `17-registro-enfriamiento-descongelacion`,
  `19-verificacion-termometros`, `BONUS-01-registro-formacion`, `BONUS-02-protocolo-alerta-alimentaria`.
- **NO aplica a chocolatería:** `09-control-aceite-fritura` (salvo variante churrería), `16-registro-coccion-regeneracion`,
  `18-registro-congelacion-anisakis`.
- **Lo que el pack NO cubre y el chocolate necesita:** trazabilidad de **lote de cobertura**, control de **cadmio**
  por proveedor, **aw de rellenos**, y la temperatura de la **cámara de chocolate a 16-18 °C**, que no es frío de
  conservación (los registros del pack están pensados para 0-8 °C y congelación).

> 🔴 **Deuda que toca de refilón**: el `CALENDARIO-V2-SEMANAL.md` (punto 0 de «Deuda nueva») registra que
> `kit-inventario/04-recepcion-mercancias.xlsx` cita el **RD 3484/2000 derogado**. Si esta guía va a citar el pack
> APPCC como cross-sell, conviene que ese punto 0 esté cerrado antes.

### 1.5 Tabla de decisión: qué se CITA y qué se CONSTRUYE

| Activo | Qué cubre | Qué le falta a quien ABRE | **Decisión** |
|---|---|---|---|
| `kit-tareas-chocolateria` (12 €) | Templado, moldeado, vitrina, perfiles, 3 campañas, calendario anual, arqueo | Todo lo económico, lo legal y lo de compra | **CITAR** (cross-sell explícito) + corregir «9 checklists» → 11 |
| `guia-pasteleria-obrador` (65 €) | El molde entero de la familia | Es otro oficio: huevo, hornos, humos, madrugada, fermentación | **CONSTRUIR distinto** reutilizando estructura. **Prohibido copiar prosa** |
| `guia-panaderia-obrador` (65 €) | Ídem, más flojo | — | **NI CITAR** mientras no entregue lo que promete (D19 de Pastelería) |
| `kit-escandallos` (12 €) | 8 verticales de escandallo, **ninguna de chocolate** | El escandallo por molde con merma de templado | **CITAR** como cross-sell; el escandallo de chocolate se **CONSTRUYE** en el libro 4 |
| `pack-appcc` (14 €) | 18 de 21 registros valen | Lote de cobertura, cadmio, aw, cámara 16-18 °C | **CITAR** (18 registros) + **CONSTRUIR** lo que falta dentro del libro de vida útil |
| Guía Food Cost (55 €) cap. 17 | Costeo por lote en obrador | Nada específico de chocolate | **CITAR** |
| `kit-plan-financiero` (39 €) | Plan financiero genérico | — | **NO citar como cross-sell de la landing**: el plan financiero va **dentro** de la guía (mismo criterio que D-§7.1 de Pastelería, que lo sustituyó como banner) |

### 1.6 Lo que la refutación de documentos de Pastelería cambia en el diseño del siguiente producto

`auditorias/guia-pasteleria-docs-refutacion-2026-09-10.md` — **46 hallazgos: 11 altos, 25 medios, 10 bajos**
(Lente A 19 · B 14 · C 13). Seis lecciones que **modifican la SPEC del producto 49 antes de escribirla**:

1. **Un nombre de producto acabado en `%` rompe el formateador de tablas.** `documentos.py:722` mira las **dos
   primeras celdas** de la fila con `RX_ETIQUETA_PCT = r'\(\s*%\s*\)|\ben\s*%|\(porcentaje\)|%\s*$'`; «Tarta de
   chocolate 70 %» casó y tres tablas del pack imprimieron **«4,0 %» donde iba 4 °C y «24,0 %» donde iban 24
   horas**. 🔴 **En chocolatería esto es un riesgo ESTRUCTURAL, no una anécdota**: la carta entera son nombres con
   porcentaje («Tableta 70 %», «Cobertura 55 %», «Bombón de origen 64 %»). **O se arregla `es_fila_porcentual()`
   en el generador antes de construir, o los nombres de la carta no llevan `%` — y arreglar el generador es lo
   correcto porque el `%` es vocabulario del oficio.**
2. **Una referencia de celda desplazada una fila no la caza ningún gate.** `verificar_guion.py` sólo comprueba que
   la celda exista y no esté vacía; `formatear()` hace `str(v)` si no es número. Resultado: dos etiquetas
   numéricas llegaron al redactor con texto dentro y **uno se inventó «veinte semanas»** donde la celda decía 9
   (A2, la única cifra fabricada de los tres documentos). **Fix obligatorio antes de la sesión B: que
   `verificar_guion.py` aborte cuando una referencia con formato `eur*`/`pct*`/`num*` resuelva a algo no numérico.**
3. **Un concepto, UNA fuente.** El fondo de maniobra se calculaba en `calculadora-capex` y en `plan-financiero`
   con fijos distintos → **dos inversiones totales en el mismo pack** (228.049 € vs 227.916 €, A3). En
   chocolatería el concepto de riesgo equivalente es el **coste de la cobertura**: si aparece en el escandallo, en
   la sensibilidad al cacao y en el CAPEX de stock inicial, tiene que salir **de una sola celda**.
4. **Una decisión que el xlsx aplica hay que enseñarla en la prosa ANTES de la hoja que la usa.** La hoja estrella
   de pastelería (decisión del huevo) se vendió como el diferencial y **«ovoproducto» aparece 0 veces en los 21
   capítulos** (B1). El comprador abrió un Excel que el libro no le enseñó a usar. **Regla nueva: todo libro
   marcado ⭐ en la SPEC tiene que tener un epígrafe propio que lo explique, y el gate lo comprueba buscando su
   vocabulario en el `.md`.**
5. **Dos tablas del mismo capítulo no pueden dar dos números del mismo concepto sin la columna que los reconcilia**
   (B5: refuerzo de campaña, 3 de 6 campañas con dos cifras). En chocolatería pasará igual con **las unidades de
   campaña**, que es exactamente donde A8 detectó que el modelo de Reyes no se sostenía aritméticamente.
6. **Lo que sí funcionó y hay que repetir sin tocarlo:** `puntos_por_epigrafe` (D33). `solape.py` dio **1 par en
   46 bloques**, contra **41 pares en 15 de 20 capítulos** del Manual del Chef Ejecutivo. **Ahorra los ~2,2 M de
   la pasada de desduplicación.** Va en el guion desde el primer día.

---

## 2. Frontera y reglas de no-solape

### 2.1 Contra `kit-tareas-chocolateria` (12 €) — reglas K1-K6

| # | Riesgo de solape | **Regla** |
|---|---|---|
| **K1** | **Templado y moldeado** (`02-partidas-produccion.xlsx`: Templado 36×7 · Moldeado 49×7, con curvas y tiempos) | La guía **no emite ninguna hoja de proceso de templado ni de moldeado** y **no enseña técnica**. Lo que construye es **capacidad**: cuántos bombones/día permite la atemperadora que estás comprando. Decisión de compra, no de ejecución. El cap. correspondiente cita el libro 02 **por su nombre de fichero** |
| **K2** | **Campañas** (`06-eventos-temporada.xlsx`: Navidad, San Valentín, Pascua) y **calendario anual** (`BONUS-02`, 12 meses con temporada Alta/Media/Baja) | La guía **no repite el calendario ni las tareas de campaña**. Construye la **economía de la campaña**: % de facturación sobre el año, déficit de capacidad, coste del refuerzo, **tesorería inmovilizada en moldes y packaging de temporada** y —lo que el kit no tiene— **el coste del valle de verano** |
| **K3** | **Perfiles de puesto** (`04-tareas-perfiles.xlsx`: **Chocolatero · Dependiente · Encargado**, 3 perfiles) | La guía **no rehace las fichas de tarea**. Construye el **dimensionado** (cuántas personas de cada perfil, bruto de convenio, coste de empresa con SS) y el **plan de contratación** con fechas de alta. ⚠️ **Los nombres de perfil del juego de datos tienen que ser LITERALMENTE los 3 del kit** — el precedente es D22 de Pastelería, donde inventarse «Oficial» quedó prohibido |
| **K4** | **Vitrina y mostrador** (`01-apertura-cierre`, «cubrir bombones que queden expuestos») | La guía **no hace checklist de vitrina**. Lo suyo es la **decisión de vitrina**: refrigerada o a temperatura ambiente climatizada, y qué referencia puede estar en cuál. Es una decisión de CAPEX y de vida útil, no de apertura del día |
| **K5** | **Arqueo de caja** (`09-apertura-cierre-caja.xlsx`, 95 fórmulas, Registro Mensual 38×10) | **Prohibido rehacer.** Es el único libro del kit con cálculo de verdad y está resuelto |
| **K6** | **Control de temperaturas de obrador y cámara** (`03-tareas-manager.xlsx`, diario) | La guía **no emite registro de temperaturas** (es del kit y del `pack-appcc/01`). Lo suyo es **dimensionar el clima**: qué cámara necesita ese obrador para sostener 16-18 °C con la carga térmica de la ciudad y del equipo. Es cálculo de compra, no de registro |

**Regla transversal (heredada de Pastelería, §2.3):** *cero fórmulas entre libros y cero duplicación de tabla
operativa; cuando la guía necesita un dato que vive en el kit, la celda verde **trae su propio valor por defecto
declarado como supuesto** y la nota «si ya tienes el Kit de Tareas Chocolatería, sustitúyelo por tu dato real de
`<fichero>.xlsx`».* Es la D21 de Pastelería, y aquí es aún más necesaria: el comprador de esta guía **no ha
abierto**, así que no tiene ni un histórico de producción.

**Frase de frontera, arriba en la landing y no en la FAQ** (calcada del criterio que funcionó en Pastelería):
«*El Kit de Tareas te dice qué hacer cada día cuando ya has abierto. Esta guía es todo lo que hay que decidir
antes.*»

### 2.2 Contra `guia-pasteleria-obrador` (65 €) — el molde de familia

| Se COMPARTE (estructura) | Es CONTENIDO PROPIO (nunca se copia) |
|---|---|
| Los 8 (o 10) libros y su reparto por decisión | Las partidas, los equipos, las zonas y los proveedores |
| El motor de escandallo por tanda con coste hora de obrador imputado | La **merma de templado y los recortes recuperables**, que no tienen equivalente en pastelería |
| La ficha de visita a local con veredicto eliminatorio | Los **criterios**: allí humos y forjado, aquí **clima, estabilidad térmica y ausencia de humos como ventaja** |
| El molde `planes-v2_0` 2.2 del plan financiero | Los **canales** (5, dos propios) y la estacionalidad con valle |
| El árbol de registro sanitario, el árbol del art. 3, la ruta doméstica y el Gantt | **RD 1055/2003, cadmio y EUDR**, que en pastelería no existen |
| `puntos_por_epigrafe`, `NO_COMUN`, la lista negra, el vocabulario ES/LATAM | Cada entrada de esas listas |

🔴 **Prohibición dura, y hay precedente medido:** *está prohibido copiar prosa, tablas o redacciones legales de la
guía de pastelería.* El precedente está en la SPEC de Pastelería §5: «copiar redacciones legales de otros kits sin
verificar» ya produjo que `kit-tareas-sushi-bar/03` y `kit-tareas-marisqueria/03` citen el **RD 1420/2006
derogado**, y eso sigue vivo en producto vendido (punto 0 de la deuda del calendario).

### 2.3 Riesgos de canibalización, uno a uno

| Riesgo | Real? | Regla |
|---|---|---|
| Con el **kit de chocolatería** (12 €) | **No.** Precios 12 vs 65 €, públicos distintos (ya abierto vs aún no) | Cross-sell en los dos sentidos. **Entra en `footerLinks` de la ficha y la ficha del kit enlaza de vuelta** |
| Con la **guía de pastelería** (65 €) | **Bajo, pero existe en un caso**: la **chocolatería-pastelería** es una variante real | La variante se trata como **columna de la hoja «Variante del Formato»**, y el capítulo 01 dice explícitamente cuándo comprar la otra guía. **Pero D19 sigue vigente: no se enlaza a ninguna guía hermana mientras no entreguen lo que prometen** |
| Con `kit-escandallos` (12 €) | **No**: no hay hoja de chocolate | Cross-sell. La guía construye el escandallo de chocolate porque **no existe** |
| Con `pack-appcc` (14 €) | **Sí, si la guía rehace registros** | La guía lleva **una fila de checklist** («plan de autocontrol firmado antes de abrir») y **cero registros**. Lo que construye —aw, lote de cobertura, cámara a 16-18 °C— **no está en el pack** |
| Con la **página de rol** `/usos/rol/chocolatero-bombonero` | **No**: es tráfico, no producto | La página **gana** un `productId` |
| Con **`ia-churrerias-guia-completa`** (post del blog) y la variante chocolatería-churrería | **Sí, y es conceptual**: si la guía abraza el modelo San Ginés, deja de ser una guía de obrador | Ver §5.9: **la churrería NO es este producto** |

---

## 3. Pipeline y molde: ¿se puede construir copiando `guia-pasteleria/`?

### 3.1 Sí, y sin tocar una línea del pipeline común

Verificado en el código:

- **`guias-v2_0/documentos.py` es genérico**: su única entrada de producto es `--producto <pid>`
  (`documentos.py:2162`), lee `xlsx_dir = DL/<pid>/` y resuelve las referencias `fichero.xlsx!Hoja!Celda` del
  guion. **No hay ningún registro de productos que haya que ampliar.** Sus 2.246 líneas se reutilizan tal cual.
- **`guias-v2_0/motor.py`** (2.135 líneas) aporta `f()`, `val()`, `verde()`, `dv_lista()`, `dv_porcentaje()`,
  `semaforo_isnumber()`, `escribir_parametro()`, `PARAMETROS`, `version_line()`, `hoja_instrucciones()`. Sin cambios.
- **`dump_prompts.py` (62 líneas)**, **`check_bloque.py` (32)** y **`solape.py` (82)** son agnósticos del producto.
- **`guia-pasteleria/` se copia entera a `guia-chocolateria/`**: `_comun_pasteleria.py` (280 líneas) pasa a
  `_comun_chocolateria.py` cambiando **sólo el nombre**; su razón de existir —`VERSION_LINE` propio («Versión 1.0
  · septiembre 2026» en vez del «Versión 2.0 · agosto 2026» que devuelve `motor.version_line()`,
  `motor.py:203-215`) y `dv_rango()` para que toda validación vaya contra un rango— **vale igual aquí**.
- **`gate_libros.py` (269 líneas)** es reutilizable **cambiando dos literales**: la línea de versión y la lista de
  ficheros. Sus 9 comprobaciones (funciones prohibidas, referencias externas, celdas verdes vacías, constantes
  cableadas de IVA/margen, «Instrucciones» primera, versión, `creator`, WinAnsi, ≥25 etiquetas válidas en el
  `mapa-*.json`) son de familia.
- **`verificar_guion.py` (338 líneas)** se copia **y se le añade el gate que faltaba** (§1.6, lección 2).
- **`paginas-gate.py`**, **`nombre-gate.py`**, **`censo-entregables.py`**, **`gate-no-latinos.py`**,
  **`gate-flujo-postpago.py`**, **`inject_cache.py`**, **`postprocess-transversal.py`**,
  **`sync-payment-links.py`**, **`sync-product-prices.py`** ya existen en `scripts/productos-digitales/` y aceptan
  `--only <slug>`. **Nada nuevo que escribir.**

**Lo único NUEVO de código:** un script de banners del blog. La serie va `fase8f` (Food Cost) · `fase8g` (Manager)
· `fase8h` (Chef) · **`fase8i` (Pastelería, ya existe)** → la siguiente libre es **`fase8j`**. 🔴 **Recomendación
firme: NO copiar el script una quinta vez.** Son cinco ficheros casi idénticos; generalizarlo a
`fase8x-sustituir-banner.py --producto <pid>` cuesta lo mismo que la copia y cierra la deuda. (Lo propuso ya D32
de la SPEC de Pastelería y no se hizo.)

### 3.2 Lo que sí hay que construir de cero

| Pieza | Por qué es nueva |
|---|---|
| `datos_ejemplo.py` (≈3.300 líneas en pastelería) | Juego de datos único de la chocolatería modelo: zonas, convenio, plantilla, 25-30 referencias, precios de compra, vías de conservación, campañas |
| 8-10 `gen_*.py` | Media medida en pastelería: **1.142-2.720 líneas por libro**, 12.578 líneas en los 8 |
| `_comun_libros_*.py` | Los dos módulos compartidos de pastelería (322 + 435 líneas) sirven de plantilla; el contenido cambia |
| `guion_guia_chocolateria_obrador.py` | ~4.900 líneas en pastelería, con `puntos_por_epigrafe` desde el día 1 |
| SPEC | ~330 líneas, el formato de `guia-pasteleria-SPEC.md` |

---

## 4. Capa de producto y canales: TODO lo que hay que tocar para publicar el producto 49

**Baseline verificado hoy:** `src/data/products-catalog.ts` tiene **48** entradas (`grep -c "^  '"`),
`netlify/shared/payment-links.ts` **48**, `netlify/shared/product-prices.ts` **48**,
`astro-site/src/lib/zona-app.ts` **49** `productId:` (una más que el catálogo; conviene comprobar cuál antes de
añadir la 50.ª). `astro-site/src/data/productos/guias/` tiene **10 fichas + `types.ts`**.

| # | Fichero (ruta exacta) | Qué se añade / verificado hoy |
|---|---|---|
| 1 | `astro-site/src/data/productos/guias/guia-chocolateria-obrador.ts` | Ficha `GuiaData`. Molde: `guia-pasteleria-obrador.ts` (**320 líneas**, con cabecera de decisiones; la de panadería son 204 y es el molde flojo). **Sin `priceOld`/`discountBadge`/`aggregateRating`/`review`, `testimonials.items: []`** |
| 2 | `astro-site/src/pages/guia-chocolateria-obrador.astro` | Wrapper con env **literal** `VITE_STRIPE_PAYMENT_LINK_GUIA_CHOCOLATERIA_OBRADOR`, `whatsapp={false}`, `locales={['es']}` |
| 3-5 | `…-access.astro` · `…-library.astro` · `islands/library/…LibraryIsland.tsx` | **GENERADOS** por `scripts/astro-migration/fase5-generate-zona-app.py`. No editar a mano |
| 6 | `astro-site/src/lib/zona-app.ts` | Entrada en `PRODUCTOS_ZONA_APP[]` (`storageKey: 'guia-chocolateria-obrador-jwt'`) |
| 7-9 | `src/App.tsx` · `src/pages/GuiaChocolateriaAccessGate.tsx` · `src/pages/GuiaChocolateriaDashboard.tsx` | 2 rutas `ProtectedRoute`; gate ≈13 líneas; dashboard con `SECTIONS[]` y **exactamente 1 `<title>` sin comillas dobles** |
| 10 | `src/data/products-catalog.ts` | Entrada **49**. Es la que alimenta `fase8e-banners-corpus.py` sobre los 325 posts ES |
| 11-12 | `netlify/shared/payment-links.ts` · `netlify/shared/product-prices.ts` | **GENERADOS** por `sync-payment-links.py` / `sync-product-prices.py` (48 → 49) |
| 13-16 | `netlify/functions/{verify-purchase,resend-access,admin-generate-access,get-download-urls}.ts` | Medido hoy para pastelería: **2 · 2 · 1 · 14** menciones. `get-download-urls` lleva **13 claves de fichero + el slug**; aquí serán **las que salgan de §5** |
| 17-18 | `src/data/productos-digitales-config.ts` · `src/data/productos-changelog.ts` | Changelog **v1.0 «Lanzamiento»**; el molde exacto está en `productos-changelog.ts:112-131` |
| 19-20 | `astro-site/src/components/pages/ProductosDigitalesHubPage.astro` · `src/pages/ProductosDigitales.tsx` | Tarjeta nueva + `ListItem` en el JSON-LD + **vaciar `comingSoon`** + corregir «9 checklists» → 11 en la tarjeta del kit de chocolatería (`…HubPage.astro:806`) |
| 21-22 | `astro-site/src/lib/sinonimos-buscador.json` · `src/lib/linkify-use-case.tsx` | Alias nuevo (§4.2) y `PRODUCT_ALIASES['Cómo Montar una Chocolatería']` (`linkify-use-case.tsx:13`) |
| 23 | `src/data/use-cases-content.es.ts` | `productIds` de **4 páginas** (§4.3) |
| 24 | `src/pages/AdminGenerateAccess.tsx` | Desplegable 48 → 49 |
| 25 | `footerLinks` de las fichas afines | `kit-tareas-chocolateria`, `kit-escandallos`, `pack-appcc`, Guía Food Cost. **NO** las guías hermanas (D19) |
| 26-27 | `astro-site/public/lovable-uploads/ai-gallery/guia-chocolateria-{hero,1..5}.jpg` + `public/og-guia-chocolateria-obrador.jpg` · `astro-site/public/dl/guia-chocolateria-obrador/**` | **7 imágenes** (skill `generate-images`; la OG **no se repite** en el cuerpo). Entregables **en disco y trackeados en git** antes de desplegar. ⚠️ `pkill -STOP mediaanalysisd` al añadirlas |
| 28 | `scripts/astro-migration/fase8j-…` **o** el genérico `fase8x-sustituir-banner.py` | §3.1 |
| 29 | env `CRYPTO_PRODUCTS` (Netlify, scope **`builds` Y `functions`**) | §4.5 |

### 4.1 🔴 El `comingSoon` se queda VACÍO, y los dos ficheros del hub NO se comportan igual

Verificado hoy. El array tiene **una sola entrada**, y es ésta:

```
src/pages/ProductosDigitales.tsx:958-960
astro-site/src/components/pages/ProductosDigitalesHubPage.astro:973-975
  { iconName: 'Utensils', name: 'Cómo Montar una Chocolatería',
    desc: 'Temperado, obrador, vitrina, proveedores de cacao, licencias y modelo de negocio.',
    tags: ['pdf','guias','chocolateria'], phase: 'Junio 2026' }
```

**Lo que pasa al publicar el producto y retirar la entrada:**

| Fichero | Guarda | Qué se ve con el array vacío |
|---|---|---|
| `src/pages/ProductosDigitales.tsx:1227` | `{filteredComingSoon.length > 0 && (…)}` | ✅ La sección **desaparece limpiamente** |
| `astro-site/src/components/pages/ProductosDigitalesHubPage.astro:1448-1500` | **NINGUNA.** `<section id="pd-coming-section">` se renderiza siempre y dentro va `{comingSoon.map(…)}` | 🔴 **Queda el rótulo «En Desarrollo / Próximos Productos / Mismo estándar de calidad: acceso inmediato, actualizaciones de por vida y garantía de 30 días» con la rejilla VACÍA** — y el Astro es el que sirve producción desde el cutover de Fase 7 |

Y en los dos, el badge del hero (`ProductosDigitales.tsx:1080` y `…HubPage.astro:1143`) imprime
`{productsCount} productos disponibles · {comingSoonCount} próximamente` → diría **«49 productos disponibles · 0
próximamente»**.

**Acción obligatoria en el mismo commit:**
1. Envolver la sección del Astro en `{comingSoon.length > 0 && (…)}` (paridad con la SPA). El `<script>` del
   cliente ya referencia `pd-coming-section` y `[data-coming]` (`…HubPage.astro:1721-1723`): hay que comprobar que
   tolera `comingSection === null`.
2. Hacer condicional el trozo «· N próximamente» del badge, en los dos ficheros.
3. **O** —decisión de John— sembrar `comingSoon` con el siguiente producto de la cola, que es la vía que mantiene
   viva la señal de «esto se mueve» y además alimenta el registro de demanda del buscador.

> **Esto no rompe el build ni sale en ningún diff visual.** Es exactamente el patrón de
> `feedback_gates-que-no-fallan-pero-dejan-pasar-el-error`.

### 4.2 Buscador del hub

`astro-site/src/lib/sinonimos-buscador.json` (2.817 bytes) tiene **8 grupos**, **4 frases** y **7 alias**. Hoy
**ningún grupo ni alias menciona chocolate, cacao, bombón ni templado**, así que un alias nuevo **no dispara el
gate de grupos huérfanos** del frontmatter.

**Alias propuesto** (el índice normaliza sin acentos; no se ponen tildes ni ñ):

```json
"/guia-chocolateria-obrador": "abrir montar una chocolateria bomboneria obrador de chocolate cacao cobertura bombones tabletas templado atemperadora bean to bar licencia traspaso taller de chocolate"
```

⚠️ **Comprobar antes de cerrar** si el placeholder animado del buscador (`…HubPage.astro`, del que la SPEC de
Pastelería cita la línea 2259 para «montar una pastelería») sugiere alguna consulta de chocolate: si lo hace,
hoy cae en una tarjeta de «Próximamente».

**L-1 sigue abierto:** el cruce de demanda real requiere
`ADMIN_PASSWORD='…' python3 scripts/productos-digitales/buscador-report.py --days 30`. **Es una sola ejecución y
puede cambiar el argumento comercial entero** (si la gente ya busca «chocolatería» en el hub, el producto no nace
a ciegas).

### 4.3 Páginas de uso (`/usos/`) — **son 4, no 1**

Medido hoy en `src/data/use-cases-content.es.ts`. Hay **dos** páginas de chocolate, no una:

| Clave | Línea del bloque | Línea de `productIds` | `productIds` actuales |
|---|---|---|---|
| `'chocolatero'` (rol · slug `chocolatero-bombonero`) | **1225** | **1264** | `kit-tareas-chocolateria, kit-escandallos, pack-appcc, kit-inventario, kit-gestion-personal, pro-prompts-ebook` |
| `'chocolateria'` (concepto de negocio) | **3210** | **3248** | idénticos |
| `'maestro-heladero'` | 1886 | 1924 | `kit-tareas-heladeria, …` |
| `'heladeria'` | 3100 | 3138 | `kit-tareas-heladeria, …` |
| `'cafeteria-brunch'` | 2217 | 2255 | ya lleva `guia-pasteleria-obrador` |

**Acción:** añadir `'guia-chocolateria-obrador'` **en primera posición** a las líneas **1264** y **3248**
(las dos páginas de chocolate), y **valorarlo** en las dos de heladería (la chocolatería-heladería es variante
real y el helado es la respuesta clásica al valle de verano). Enlace **bidireccional**: la ficha del producto
enlaza de vuelta.

> Precedente: `guia-pasteleria-obrador` está hoy en **3** páginas (líneas 2034, 2255, 2698) y
> `guia-panaderia-obrador` en **1** (1153) — la puso D31 de Pastelería porque no estaba en ninguna.

### 4.4 Blog — banners medidos hoy, post a post

Extraído con `grep -o 'href="/[a-z0-9-]*?utm_source=blog&amp;utm_medium=banner'` sobre
`astro-site/src/content/blog/es/`. **Los tres banners están ya puestos en todos**, así que **hay que SUSTITUIR, no
añadir** (`fase8e-banners-corpus.py` sólo inserta).

| Post (menciones de chocolate según el briefing) | Banner 1 | Banner 2 | Banner 3 | **Sustitución quirúrgica propuesta** |
|---|---|---|---|---|
| `libreria-de-prompts-para-chocolatero-consultor-pro-ai` (370) | `kit-tareas-chocolateria` | `kit-plan-financiero` | `kit-escandallos` | **Sustituir `kit-plan-financiero`** — el plan financiero a 3 años va **dentro** de la guía (mismo criterio que D-§7.1 de Pastelería) |
| `libreria-de-prompts-para-chocolateria-creativa-ai` (353) | `kit-tareas-chocolateria` | `kit-escandallos` | `pro-prompts-ebook` | **Sustituir `pro-prompts-ebook`** — es el más genérico de los tres |
| `chocolateria-artesanal-e-ia-una-combinacion-innovadora` (88) | `kit-tareas-chocolateria` | **`guia-restaurante-peruano`** | **`kit-tareas-sushi-bar`** | 🔴 **El peor encaje del corpus: un post de chocolatería artesanal vendiendo cocina peruana y sushi.** Sustituir **`kit-tareas-sushi-bar`** por la guía; y **`guia-restaurante-peruano`** es candidato a un segundo arreglo (queda a criterio: no es de esta guía) |
| `libreria-de-prompts-para-pasteleria-creativa-ai` (120) | `kit-tareas-pasteleria` | `kit-escandallos` | `guia-pasteleria-obrador` | **No tocar.** Ya vende la guía hermana correcta |
| `libreria-de-prompts-para-pastelero-consultor-pro-ai` (50) | `kit-tareas-pasteleria` | `guia-pasteleria-obrador` | `kit-escandallos` | **No tocar** |
| `libreria-de-prompts-para-heladeria-creativa-ai` (31) | `kit-tareas-heladeria` | `kit-escandallos` | `pro-prompts-ebook` | **Enlace contextual**, no banner (el solape es la chocolatería-heladería, no el producto) |
| `libreria-de-prompts-para-heladero-consultor-pro-ai` (27) | `kit-tareas-heladeria` | `kit-plan-financiero` | `kit-escandallos` | Ídem |
| `ia-churrerias-guia-completa` (18) | `guia-dark-kitchen` | `kit-tareas-bar` | `kit-tareas-restaurante-creativo` | **Sólo si John decide incluir la variante churrería** (§5.9). Si no, **no tocar**: este post es de churrería, no de obrador de chocolate |

**A la lista `NUNCA` del script de banners:** `kit-tareas-chocolateria`, `kit-escandallos`, `pack-appcc` y
`guia-food-cost-ingenieria-menu` — son el cross-sell de la guía; sustituirlos sería quitarse ventas propias.
Después de aplicar: **siempre `fase8b-regen-lastmod.py`**. Y **prohibido** reejecutar
`fase8c-libreria-assemble.py`: reconstruye el cuerpo desde el `.txt` de bridge y pisa lo publicado.

### 4.5 `robots.txt`, cripto, zona app y Resend

- **`robots.txt`: nada que tocar.** `astro-site/public/robots.txt` cubre el prefijo `guia-` en los **5 bloques de
  user-agent** (líneas 35-36, 53-54, 71-72, 89-90, 107-108: `Disallow: /guia-*-access` y `/guia-*-library`), y la
  cabecera (líneas 15-16) declara los prefijos de la zona app. **Correr `robots-gate.py` igualmente**: es el gate
  que cazó las 26 URLs borradas del índice.
- **Cripto: nada que tocar en la plantilla.** `astro-site/src/components/pages/GuiaLandingPage.astro` importa
  `CryptoPayButton` (línea 26), llama `cryptoEnabledFor(data.slug)` (línea 44) y monta **las tres puertas**
  (líneas 265, 567, 662 — hero, buybox, cta). **Lo único que hay que hacer es añadir el slug a la env
  `CRYPTO_PRODUCTS`** en Netlify, con **scope `builds` Y `functions`** (`crypto-checkout.ts:87` la revalida en
  runtime, `astro-site/src/lib/crypto-checkout.ts:37` se evalúa en build-time). **Prerrequisito:** el producto
  debe existir ya en `verify-purchase.ts` y en `product-prices.ts` o `crypto-checkout` lo rechaza.
- **Zona app:** los 3 ficheros los **genera** `fase5-generate-zona-app.py`; verificar con `--check` (byte a byte).
- **Resend — el hueco real.** Regla de John del 5-sep: último `scheduled_at` + 5 días, **08:00 UTC / 10:00
  Madrid**. Estado leído hoy en `CALENDARIO-V2-SEMANAL.md`: Chef **14-sep** · bar **19-sep** · cafetería **24-sep**
  · tapas **29-sep** · panadería **4-oct** · food truck **9-oct (PROGRAMADO el 10-sep)** · **guía de pastelería
  14-oct (BORRADOR, programar desde el 14-sep)** · **kit pastelería 2.1 19-oct (BORRADOR, desde el 19-sep)**.
  → **El primer hueco libre para esta guía es el 24-oct-2026, 08:00 UTC.** Queda como **BORRADOR con el nombre
  «— PROGRAMAR 24-oct»** hasta el **24-sep** (Resend no admite programar a más de 30 días vista). Al reprogramar:
  **un broadcast programado no se edita (403)** — es `GET` (guardar asunto y nombre) → `DELETE` → `POST`, con
  `json.loads(strict=False)`.

---

## 5. Propuesta de entregables

> Nada de lo que sigue es contenido de producto: es **especificación**. Ninguna cifra de ejemplo va aquí; todas
> viven en `datos_ejemplo.py` y se deciden con L3 (normativa) y L4 (sector) delante.

### 5.1 Alcance recomendado: **10 libros**, con plan de absorción a 8

Pastelería bajó de 10 a 8 por decisión de John (D3), absorbiendo dos hojas. Aquí propongo **10**, porque el
chocolate tiene **tres frentes que la pastelería no tiene** (precio del cacao, vida útil del relleno, y
talleres/B2B como líneas de ingreso reales), y marco **cuál se absorbe en cuál** si John quiere 8.

### 5.2 Los libros

| # | Fichero | Hojas | Entradas (celda verde) | Salidas por fórmula | **La decisión que permite tomar** | Frontera / por qué existe |
|---|---|---|---|---|---|---|
| **1** ⭐ | `capacidad-obrador-y-clima.xlsx` | Instrucciones · Parámetros · **Zonas y m²** · **Clima del Obrador** · **Capacidad por Equipo** · **Cuello de Botella** · **Ficha de Visita a Local** | m² por zona; kg/hora de atemperadora; nº de moldes y policarbonatos; m³ de cámara a 16-18 °C; m³ de túnel/abatidor; **T y HR objetivo**; **T exterior de tu ciudad en agosto**; horas de turno; potencia instalada | m² totales y % obrador/venta; **bombones/día por equipo**; **el equipo que limita**; piezas/día del conjunto; **carga térmica de la cámara y si el equipo la sostiene en agosto**; semáforo eliminatorio del local | **Si ese local sirve, y cuántos bombones/día aguanta el equipo que vas a comprar** | **Nada equivalente en el catálogo.** Y la hoja «Clima del Obrador» no existe ni en pastelería ni en la competencia: es **el** criterio del chocolate. **Frontera K1/K6**: el kit ejecuta el templado y registra temperaturas; esto decide el local y el equipo |
| **2** | `calculadora-capex-chocolateria.xlsx` | Instr. · Parámetros · **CAPEX por Bloque** · **Variante del Formato** · **Traspaso vs Obra Nueva** · **IVA y Tesorería** · Resumen | importe por partida (mín/máx/tuyo); variante; **«¿lleva IVA?» y tipo por línea**; precio de traspaso; renta; horizonte; meses de colchón | total por bloque y CAPEX total; **IVA soportado y cuándo vuelve**; CAPEX por variante; **coste a 5 años de traspaso+renta vs obra nueva+renta** | **Cuánto necesitas de verdad, y si sale mejor traspaso u obra** | Molde del libro 2 de pastelería (323 fórmulas) con **partidas propias**. La **«Variante del Formato»** es aquí mucho más cara de fallar: bean-to-bar mete tostadora, descascarilladora, refinadora/melanger y conchadora. **Cero precios inventados: celda verde vacía con su columna de IVA** |
| **3** ⭐ | `sensibilidad-al-precio-del-cacao.xlsx` | Instr. · Parámetros · **Coste de Cobertura por Referencia** · **Escenarios de Precio** · **Repercusión al PVP** · **Stock y Cobertura de Compra** | €/kg de cada cobertura (negra, leche, blanca, origen); % de cobertura en cada referencia; **escenarios de subida en %**; margen objetivo; semanas de stock de seguridad | coste de materia por referencia en cada escenario; **food cost resultante**; **subida de PVP necesaria para mantener margen**; **€ inmovilizados si compras a plazo**; **la referencia que primero se rompe** | **Qué haces cuando el cacao sube un 40 %: subes precio, cambias gramaje, cambias cobertura o aceptas menos margen** | 🔴 **El libro más propio del producto y el que ninguna guía gratuita tiene.** El chocolate es el único oficio de la casa donde **una commodity volátil es el 40-60 % del coste**. Es la respuesta estructurada al dolor nº 1 que la propia página de rol ya declara: «cacao con precio volátil que cambia el coste real cada semana» (`use-cases-content.es.ts:1232`). **Absorbible como hoja del libro 4 si se baja a 8** |
| **4** ⭐ | `carta-de-apertura-y-escandallo-chocolate.xlsx` | Instr. · Parámetros (coste hora de obrador) · **Escandallo por Molde/Tanda** (25-30 refs) · **Merma de Templado y Recortes** · **Coste Hora y Mano de Obra** · **Unidad vs Caja** · **Mix y Ticket Medio** · **Decisión de Surtido** | precios de compra; gramaje por bombón; **piezas por molde**; nº de moldes por tanda; minutos de mano de obra; **% de merma de templado** y **% de recorte recuperable**; PVP por unidad y por caja; mix % | coste materia por pieza; **coste real con merma y recorte recuperado**; coste de mano de obra por pieza; food cost %; margen €; **precio de la caja de 9/16/24 frente a la suma de sus unidades**; aporte al ticket medio; veredicto de surtido | **Qué vendes, a cuánto, y si la caja te gana o te cuesta dinero** | Motor heredado del libro 4 de pastelería (1.929 fórmulas, el más denso). **Lo propio:** la **merma de templado con recorte recuperable** (el chocolate mal templado **se vuelve a fundir**, la masa fallida no) y **la caja como unidad de venta**, que no existe en pastelería. **`kit-escandallos` NO tiene hoja de chocolate** (verificado, §1.3) |
| **5** ⭐ | `vida-util-rellenos-y-rotacion.xlsx` | Instr. · Parámetros · **Tipo de Relleno y aw** · **Vida Útil Declarada** · **Temperatura y Vitrina** · **Lote Económico y Merma por Caducidad** | tipo de relleno por referencia (ganache de nata / de agua / de mantequilla, praliné, gianduja, licor, fruta); **aw medida o estimada por ti**; T de conservación; ventas/semana; tamaño de lote | **plazo orientativo por familia**, **vida útil DECLARADA POR TI (celda verde, nunca calculada)**, temperatura de conservación con su norma, **lote económico**, **merma esperada por caducidad en €/año**, semáforo de vitrina refrigerada vs climatizada | **Cuánto dura cada bombón, en qué vitrina va y de cuánto haces cada lote** | 🔴 **Es el hueco funcional de la «decisión del huevo» de pastelería, y la lección B1 obliga a que la prosa lo explique antes de la hoja.** ⚠️ **Regla dura de diseño:** la vida útil **la declara el fabricante en su APPCC**; el libro **nunca la calcula ni la presenta como norma** — el precedente es D11 de Pastelería, que separó «plazo legal» de «vida útil declarada por ti». **Frontera:** el `pack-appcc` registra temperaturas; esto **decide** cuáles |
| **6** ⭐ | `campanas-y-valle-del-ano.xlsx` | Instr. · Parámetros · **Calendario de Campañas** · **Peso sobre el Año** · **Capacidad vs Demanda del Pico** · **Refuerzo y Tesorería** · **El Valle de Verano** | ventas estimadas por campaña; PVP y unidades/día; personal de refuerzo; antelación de compra de moldes y packaging; **meses de valle y % de caída**; ¿cierras en agosto? | % de facturación de cada campaña sobre el año; **déficit de capacidad** (contra el libro 1); coste del refuerzo; **tesorería inmovilizada en moldes y packaging de temporada**; **coste del valle: fijos que siguen corriendo con la caja parada**; **cuánto tiene que aportar la desestacionalización para taparlo** | **Si aguantas Navidad, y de qué vives en julio y agosto** | **Frontera K2**: el `BONUS-02` del kit da **fechas y qué producto**; esto da **euros y si aguantas**. La hoja «El Valle de Verano» **no tiene equivalente en pastelería**, donde el verano no es un agujero: aquí el propio kit lo declara **Baja** en agosto y **Media** en junio-julio |
| **7** | `plan-financiero-3-anos-chocolateria.xlsx` | 0. Supuestos · Inversión Inicial · PyG 3 Años · Punto de Equilibrio · Escenarios · Personal · **Tesorería 12 meses** · Financiación · **Canales y Punto Muerto** · Instrucciones | tickets/día; ticket medio sin IVA; días de apertura; **estacionalidad mensual con el valle dentro**; rampa; brutos de convenio; % SS; condiciones de deuda; **por canal**: ventas, margen, coste de servir, comisión de plataforma, **coste de envío refrigerado** | P&L; punto muerto; 3 escenarios; coste de personal con SS; tesorería mes a mes; servicio de deuda; **margen de contribución por canal**; **punto muerto con y sin B2B**; **qué canal sostiene el negocio** | **Si el negocio se sostiene, cuándo llega al equilibrio y qué canal lo sostiene** | Molde `planes-v2_0` motor **2.2** (el mismo que el libro 5 de pastelería, 1.022 fórmulas). **Los canales son 5, no 4**: mostrador · online con envío · B2B hostelería · **regalo corporativo** · **talleres y catas**. ⚠️ Libro **híbrido**: manda la línea de versión de la familia de guías, no la del motor 2.2 |
| **8** ⭐ | `checklist-legal-licencias-y-cacao.xlsx` | Instr. · **Checklist Legal (F1-F6)** · **Árbol de Registro Sanitario** · **Suministro a Otros Minoristas** · **Ruta Doméstica** · **Denominaciones Legales del Cacao** · **Cadmio y Analíticas** · **EUDR: ¿te aplica?** · Registro de Formación · **Cronograma y Ruta Crítica** | ✓/☐/N/A, fecha, responsable, coste; CCAA; ¿suministras a otros minoristas?; m² útiles y kg/semana; **% de cacao y de manteca de cada referencia**; **¿grasas vegetales distintas de la manteca?**; **¿importas grano o compras cobertura en la UE?**; **¿quién es tu proveedor y qué te declara?**; fecha de inicio y duración de cada hito | contador y % por fase; veredicto «comunicación autonómica» vs «RGSEAA»; tres semáforos del art. 3; semáforos de la ruta doméstica; **qué puedes LLAMAR legalmente a cada referencia** (y qué no); **si necesitas analítica de cadmio y con qué frecuencia**; **tu papel en la cadena EUDR y qué documentación te toca**; mes de cada hito, ruta crítica, fecha de apertura | **Qué papel te toca, en qué orden, cómo puedes llamar a lo que vendes y qué te obliga la norma del cacao** | 🔴 **El libro más diferencial del bloque legal, y donde está el riesgo.** Las 5 hojas de familia se heredan. **Las tres nuevas dependen ENTERAS de L3**: RD 1055/2003 (definiciones y % mínimos, grasas vegetales ≤5 %, «chocolate a la taza»), Rgto. (UE) 2023/915 (cadmio) y Rgto. (UE) 2023/1115 (EUDR). **Ni un literal se escribe sin la verificación legal contra fuente primaria.** ⚠️ **Y la hoja de EUDR sólo se construye si L3 confirma qué obliga HOY a una chocolatería pequeña**: si la respuesta es «nada directamente, sólo pedirle la declaración a tu proveedor», la hoja se queda en dos preguntas y una carta tipo, no en un módulo |
| **9** | `checklist-equipamiento-y-proveedores-cacao.xlsx` | Instr. · **Equipamiento** (mín/máx, prioridad, **¿lleva IVA?**, **plazo de entrega**) · **Variante del Formato** · **Proveedores de Cobertura y Cacao** · Contador | ✓; precio real negociado; proveedor; plazo en semanas; **¿te declara origen y EUDR?**; **¿te da analítica de cadmio?**; pedido mínimo | contador; **desviación contra el CAPEX del libro 2**; **plazo crítico** que mueve la apertura; **semáforo de documentación del proveedor** | **Qué compras, a quién, a qué precio real, con qué plazo y con qué papeles** | Molde B del libro 7 de pastelería (352 fórmulas). **Dos columnas nuevas** (EUDR, cadmio) que en pastelería no existen. **Los proveedores no verificados no se publican** — regla heredada (allí se dejaron fuera 22 de 31) |
| **10** ⭐ | `talleres-catas-y-regalo-corporativo.xlsx` | Instr. · Parámetros · **Precio del Taller** · **Punto Muerto por Sesión** · **Regalo Corporativo** · **Calendario de Cierre de Pedidos** | precio/persona; aforo mín. y máx.; coste de materia por asistente; horas de docente y su coste; horas de sala perdidas para venta; pedido mínimo B2B; % de personalización; días de cobro | margen por sesión; **asistentes para cubrir el punto muerto**; **€/hora de sala del taller frente a €/hora de la misma sala vendiendo**; margen del pedido corporativo; **fecha límite de cierre de pedidos de Navidad calculada hacia atrás desde la capacidad del libro 1** | **Si el taller y el regalo de empresa te dan dinero o te ocupan el obrador en el peor momento** | 🔴 **No existe nada parecido en el catálogo** y son **las dos líneas que tapan el valle y financian la campaña**. La segunda hoja es la que impide el error clásico: aceptar 400 cajas corporativas para la semana en que ya no cabe un molde más. **Absorbible como dos hojas del libro 7 si se baja a 8** |

**Si John quiere 8 libros** (paridad con Pastelería): se absorbe el **3** en el **4** (hoja «Escenarios de Precio
del Cacao») y el **10** en el **7** (hojas «Talleres» y «Regalo Corporativo» junto a «Canales y Punto Muerto»).
**Recomendación: mantener el 3 como libro propio.** Es el argumento comercial más fuerte del producto y una hoja
enterrada dentro del escandallo no se ve ni se vende.

### 5.3 La guía: 20 capítulos + anexo

`H` = hereda estructura de Pastelería · `N` = nuevo del chocolate · 🔴 = depende de L3 y no se escribe sin ella.

| # | Capítulo | H/N | Libro que lo sostiene |
|---|---|---|---|
| 01 | Qué negocio estás montando: las variantes del chocolate y cuál te toca | **H** | 2 (Variante del Formato) |
| 02 | El cliente y la plaza: quién compra chocolate, cuándo y a qué precio | **H** | 6 (Peso sobre el Año) |
| 03 | La carta de apertura: las referencias, las familias y la caja como unidad | **H+N** | 4 |
| 04 | Cuánto cuesta abrir: el CAPEX real, partida a partida | **H** | 2 |
| 05 | El local: metros, zonas y la ficha de visita | **H** | 1 |
| 06 | Antes de firmar: **el obrador sin humos cambia la conversación de la licencia** | **N** | 1, 2, 8 |
| 07 | **El clima del obrador: 16-18 °C, humedad y por qué el chocolate manda sobre el local** | **N** | 1 (Clima del Obrador) |
| 08 | Maquinaria: atemperadora, túnel, moldes — qué compras, qué alquilas, qué esperas | **H+N** | 9 |
| 09 🔴 | Licencias, sanidad y registro: el camino completo | **H** | 8 |
| 10 🔴 | **Cómo puedes llamar a lo que vendes: las denominaciones legales del cacao** | **N** | 8 (Denominaciones) |
| 11 🔴 | **Cacao, cadmio y deforestación: qué te pide la norma y qué le pides a tu proveedor** | **N** | 8, 9 |
| 12 | Autocontrol, alérgenos y formación: qué tener el día de la inspección | **H** | 8 (+ cita `pack-appcc`) |
| 13 | Proveedores: cobertura, frutos secos, packaging y plazos | **H** | 9 |
| 14 | **Escandallo del chocolate: la merma de templado, el recorte que vuelve y la caja** | **H+N** | 4 |
| 15 🔴 | **El precio del cacao: qué haces cuando sube y quién paga la subida** | **N** | 3 |
| 16 | **Vida útil del relleno: aw, vitrina y de cuánto haces cada lote** | **N** | 5 |
| 17 | El equipo: cuántos, qué perfiles y qué cuestan | **H** | 7, y los **3 perfiles del kit** |
| 18 | **Las campañas y el valle: de Navidad a agosto** | **H+N** | 6 |
| 19 | **Talleres, catas y regalo corporativo: las dos líneas que tapan el verano** | **N** | 10 |
| 20 | Canales: mostrador, online con envío, B2B y corporativo | **H** | 7 |
| 21 | El plan financiero y el dinero hasta el punto de equilibrio | **H** | 7 |
| 22 | Cronograma, apertura y los primeros noventa días | **H** | 8 (Cronograma) |
| **A** | **Anexo normativo fechado** (vigencias + fechas que se mueven) | **H** | — |

> Son **22 entradas**: hay que podar **dos** para cerrar en 20 + anexo. Candidatos naturales de fusión:
> **10+11** (las dos legales del cacao, en un capítulo 🔴 de 2.100 palabras) y **19 dentro de 20** (talleres y
> corporativo como dos canales más). **Decisión de la SPEC, no de este informe.**
> **Balance: 11 heredan estructura · 7 son nuevos · 4 mixtos.** Es más contenido propio que el que tuvo
> Pastelería respecto a Panadería, y por eso el presupuesto de §6 no baja tanto como cabría esperar.

### 5.4 Bonus — recomendación

| Bonus | Formato | Recomendación |
|---|---|---|
| **1. Business plan modelo relleno** | DOCX | ✅ **SÍ.** El de pastelería mide **7.415 palabras y 9 tablas** (medido hoy), contra las **796 palabras y 0 tablas** de la versión de panadería que la SPEC de Pastelería denunció. Es el bonus con mejor relación valor/coste (**1 redactor**). ⚠️ **Y hereda el defecto B2**: el resumen ejecutivo tiene que **dar** el resultado neto, el margen y el punto de equilibrio, no remitir a otra hoja |
| **2. «12 decisiones de apertura resueltas»** | PDF + DOCX | ✅ **SÍ.** Molde probado tres veces; el de pastelería mide **37 páginas / 16.842 palabras / 12 tablas**. 12 decisiones propias del chocolate: *bombonería o bean-to-bar · comprar atemperadora continua o de sobremesa · abrir con 15 referencias o con 30 · vender la caja o la unidad · cobertura de marca o de origen · abrir vitrina refrigerada o climatizada · aceptar el primer pedido corporativo sin histórico · envío a domicilio en verano: cuándo dices que no · cerrar en agosto o quedarte · el taller: línea de negocio o marketing · empezar en casa dentro de la legalidad · qué haces con el chocolate que no se vende* |
| **3. Calendario de campañas** | — | ❌ **NO.** Es el `BONUS-02` del kit de 12 € (**frontera K2**). Duplicarlo canibaliza y encima quedaría peor |
| **4. Recetario de bombones** | — | ❌ **NO, terminantemente.** Un recetario con gramajes y curvas que nadie ha ejecutado es **el patrón de cifra inventada que la casa prohíbe**, y aquí el riesgo es físico (una curva de templado mal publicada arruina producción). Precedente: Pastelería descartó su BONUS 3 por lo mismo. Las referencias viven **dentro del libro 4** como datos de ejemplo declarados |

### 5.5 Juego de datos único

Un solo `guia-chocolateria/datos_ejemplo.py` del que beben los 10 generadores, el guion y los dos bonus. *Si un
número cambia, cambia ahí y se regeneran los libros.*

| Campo | Propuesta | Por qué |
|---|---|---|
| **Nombre** | Chocolatería **«La Almendra»** (o similar, neutro y sin marca real) | Paralelo a «La Encina» (Food Cost / Manager) y «La Clara» (Pastelería). **Comprobar que no coincide con marca registrada** antes de cerrarlo |
| **Formato** | **Obrador propio + tienda a calle**, ciudad media española **sin nombre propio** | Es el caso central; las demás variantes son **desviaciones tabuladas** sobre él |
| **Superficie** | **Menor que los 90 m² de «La Clara»** — un obrador de chocolate no necesita ni horno ni salida de humos, y **sí una cámara climatizada**. Zonas: obrador de templado · cámara de chocolate · almacén de cobertura · packaging · tienda · aseos y vestuario | ⚠️ **El reparto de m² lo fija L4 (sector), no este informe.** Lo que sí es de diseño: **el reparto no es el de pastelería** y publicarlo copiado sería el error de método que la casa persigue |
| **Plantilla** | **Los 3 perfiles LITERALES del kit**: **Chocolatero · Dependiente · Encargado** | **Regla dura (K3 + precedente D22).** «Maestro chocolatero», «bombonero» u «oficial» **no existen en el kit y quedan prohibidos** si no están en `04-tareas-perfiles.xlsx` |
| **Carta** | **25-30 referencias en 5 familias**: bombones de colección · tabletas · **chocolate a la taza** · turrones y figuras de temporada · **cajas y regalo** | La taza entra como **familia**, no como negocio (§5.9). Las cajas son familia propia porque **la caja es la unidad de venta real** |
| 🔴 **Nombres de las referencias** | **Con `%` en el nombre SÓLO si `documentos.py:722` está arreglado antes** | **§1.6 lección 1.** «Tableta 70 %» rompe el formateador y convierte °C y horas en porcentajes. **Es el riesgo nº 1 de tubería de este producto** |
| **Coherencia con el kit** | Verificar **abriendo los ficheros** qué referencias vienen precargadas en `02-partidas-produccion.xlsx` y `03-tareas-manager.xlsx` y usar **las mismas** donde coincidan | El research de Pastelería lo afirmó sin abrirlos y la SPEC tuvo que ponerlo como tarea (D22/§3). **Aquí se hace antes** |
| **Campañas** | **Navidad+Reyes · San Valentín · Pascua · Día de la Madre · Halloween · Todos los Santos** + **valle de junio-agosto** | **Salen del `BONUS-02` del kit**, que ya declara Alta/Media/Baja mes a mes. Así el lector reconoce el calendario y la guía pone los euros |
| **Convenio** | En celda verde, sustituible, con su código y su publicación | ⚠️ **Cuál es el convenio de una chocolatería** (pastelería, confitería, comercio minorista de alimentación) **es pregunta para L3**: la respuesta cambia los brutos y cambia si el negocio es comercio o industria |

### 5.6 La trampa aritmética que hay que evitar por diseño

El hallazgo **A8** de la refutación de Pastelería: las unidades del pico (420 roscones/día) eran incompatibles con
el mix de la carta (1.714 roscones/año), y **las dos tablas se publicaron declarando el mismo 9,8 % del año**.
Nadie lo vio hasta el refutador.

**En chocolatería es peor**, porque Navidad puede ser un tercio del año. **Regla de diseño para
`datos_ejemplo.py`:** las unidades de campaña **se calculan desde el mix anual**, no se teclean; y el libro 6
lleva una **fila de cuadre explícita** («unidades de campaña / unidades del año de esa referencia») con semáforo.
Y por B5: **si dos tablas del mismo capítulo dan dos números del mismo concepto, va la columna que los reconcilia
o no va la segunda tabla.**

### 5.7 Vocabulario ES / LATAM (equivalencia en la PRIMERA mención, luego España)

| Concepto | España | LATAM (primera mención) | Nota |
|---|---|---|---|
| La tienda | **chocolatería** · **bombonería** | **chocolatería** · **dulcería** ⚠️ | 🚨 **«Dulcería» NO se usa como sinónimo en ninguna parte del producto.** Es el falso amigo más caro del nicho: en México es la tienda de golosinas y el mostrador del cine. Ya está prohibido en la SPEC de Pastelería §6 |
| El espacio de producción | **obrador** | **taller** · **laboratorio** (AR/UY/CL) | Mismo criterio que Pastelería: «obrador» apenas se usa fuera de España |
| Coste unitario | **escandallo** | **costeo** | Heredado |
| Mueble de exposición | **vitrina** · **mostrador** | **exhibidor** · **vitrina exhibidora** | ⚠️ La preposición cambia: «vitrina DE» en España, «vitrina PARA» en LATAM |
| El producto | **bombón** | **bombón** · **chocolate** (unidad) | ⚠️ **«Trufa» y «praliné» NO son sinónimos de bombón**: son tipos. Usarlos como equivalentes es un error técnico que un chocolatero detecta en la primera página |
| Materia prima | **cobertura** · **chocolate de cobertura** | **cobertura** | La forma corta «cobertura» es la del oficio |
| Formato | **tableta** | **barra** (MX/CO) · **barrita** | |
| Bebida | **chocolate a la taza** | **chocolate caliente** ⚠️ | **No son lo mismo**: el español «a la taza» es espeso y lleva almidón. La equivalencia se da, pero se avisa de la diferencia |
| Coste | **coste** | **costo** | Glosario del cap. 01 |

Del vocabulario real de los compradores que sí se usa: «**montar**» (no «abrir») · «**templar**» y «**temperar**»
(las dos vivas; elegir una y declararlo en el glosario) · «**la cámara**» · «**el brillo y el snap**» ·
«**bean-to-bar**» (en inglés, es como se dice) · «**por encargo**» · «**la caja de 9**».

### 5.8 Los tres frentes normativos que sólo tiene este producto

**No se escribe ni una línea de esto sin L3.** Lo que aporta L6 es **dónde vive cada uno en el producto**:

| Frente | Dónde vive | Qué NO puede pasar |
|---|---|---|
| **RD 1055/2003** (denominaciones de cacao y chocolate: % mínimos, grasas vegetales, «chocolate a la taza») | Libro 8, hoja «Denominaciones Legales del Cacao» + capítulo 10 | Que el lector escriba «chocolate negro 70 %» en una etiqueta sin saber qué exige la norma para llamarlo así. **Es una decisión de etiquetado con sanción detrás** |
| **Rgto. (UE) 2023/915** (cadmio) | Libro 8, hoja «Cadmio y Analíticas» + libro 9, columna de proveedor + capítulo 11 | Publicar un límite numérico sin verificarlo contra el texto consolidado. **Los límites de cadmio dependen del producto y del % de cacao**: una cifra suelta sería exactamente el tipo de dato que la lista negra persigue |
| **Rgto. (UE) 2023/1115 — EUDR** (deforestación; el cacao está dentro) | Libro 8, hoja «EUDR: ¿te aplica?» + capítulo 11 | 🔴 **Afirmar que le aplica a una chocolatería pequeña sin haberlo verificado.** La distinción **operador vs comerciante** y la de **pyme vs no pyme** lo cambian todo, y las fechas de aplicación **se han movido**. **Si L3 no puede cerrar esto contra fuente primaria, el capítulo 11 se reduce a «qué le pides por escrito a tu proveedor» y el resto va al ANEXO como fecha que se mueve.** Nunca al revés |

### 5.9 La decisión que hay que llevarle a John: **chocolatería de taza y churros**

Los datos del briefing (DataForSEO, España, 2026-09-12) que la sostienen: «chocolateria» **9.900/mes**,
«chocolate a la taza» **4.400**, «chocolateria churreria» **1.000**, «montar una churreria» **50**; en la SERP de
«como montar una chocolateria» aparecen **maestrochurrero.com** y las relacionadas **«Franquicia Valor»** y
**«Valor chocolate»**.

**Mi recomendación: NO es este producto. Se trata como variante tabulada, no como capítulo.** Tres razones, y las
tres son de producto, no de gusto:

1. **Es otro oficio y otra licencia.** Una churrería **fríe**: tiene salida de humos, campana, control de aceite
   (`pack-appcc/09`) y una licencia de actividad distinta. El argumento estructural de esta guía —**«tu obrador no
   tiene humos y eso te abre locales que a una pastelería le están cerrados»**— se cae en el minuto uno.
2. **El producto entero deja de aplicar.** La cámara a 16-18 °C, el aw de los rellenos, la merma de templado, el
   precio de la cobertura, el EUDR y el cadmio: **nada de eso le sirve a quien monta un San Ginés**.
3. **El volumen es de consumidor, no de emprendedor.** «Chocolate a la taza» (4.400) y «chocolatería» (9.900) los
   teclea quien quiere merendar; la señal de negocio son «como montar una chocolateria» (**10**), «montar una
   chocolateria» (**10**) y «montar una churreria» (**50**). Y la propia SPEC de Pastelería dejó `chocolateria`
   (9.900) marcada «**sin SERP medida**» y **prohibida como sostén de ninguna conclusión de intención** (D25).

**Lo que sí se hace:**
- **«Chocolate a la taza» entra como FAMILIA de la carta** (libro 4) y como línea de desestacionalización en el
  capítulo del valle: es producto de invierno con margen alto y ticket bajo.
- **«Chocolatería-churrería» entra como columna de «Variante del Formato»** (libro 2) con su CAPEX diferencial y
  una nota franca: *esto es un negocio de restauración con freidora y salida de humos; esta guía cubre el
  obrador, no la churrería.*
- **«Chocolatería con degustación / salón» sí entra de verdad** como variante (mesas, IVA de hostelería, convenio
  distinto) — **pero eso lo confirma L3**, porque es el equivalente exacto de la variante «pastelería-cafetería»
  que allí abrió un frente de IVA y convenio (V-02/V-03).
- **Franquicia (Valor y similares) entra como una de las «tres puertas»** del capítulo de antes de firmar —local
  nuevo, traspaso o franquicia—, con la regla heredada: **cifras de franquicia NUNCA como dato auditado**.

---

## 6. Presupuesto y riesgos de pipeline

### 6.1 Estimación por fase, anclada en el coste REAL de Pastelería (≈14,1 M)

| Fase | Trabajo | Modelo | Pastelería (real) | **Chocolatería (estimado)** | Por qué cambia |
|---|---|---|---|---|---|
| Research | 6 lentes + síntesis + refutación | opus/sonnet | 2,06 M | **2,1 M** | Mismo alcance |
| Verificación legal | Contra fuentes primarias + `pypdf` | opus | 0,50 M | **0,75 M** ⬆ | **+50 %: tres frentes nuevos** (RD 1055/2003, cadmio, **EUDR**) y el EUDR obliga a rastrear un reglamento cuyas fechas se han movido |
| SPEC + fusión de ids | SPEC + `PA-*`/`PS-*` al JSON con gate de recuento | Fable + sonnet | 0,38 M | **0,45 M** | Más decisiones (10 libros, la variante churrería, el `%` del formateador) |
| `datos_ejemplo.py` | Juego de datos único | opus | 0,42 M | **0,45 M** | Carta de 25-30 refs con merma de templado y cajas |
| **Libros** | Constructores → refutador → fixer → `inject_cache` → `data_only` → mapas | opus + sonnet | 2,37 M (8 libros) | **2,85 M (10)** ⬆ | 0,30 M/libro medido × 10, + 3 libros sin molde previo (3, 5, 10) |
| Guion | 20 caps + anexo + 2 bonus con `puntos_por_epigrafe` | opus | 0,60 M | **0,70 M** | Más referencias de celda (10 libros) |
| **Redactores** | `dump_prompts.py` → bloques con `check_bloque.py` | sonnet ×N | 4,90 M (47 bloques ⇒ **0,104 M/bloque**) | **4,9-5,2 M** | Mismo nº de bloques si se repite la palanca de `bloques: 1` en los capítulos no legales |
| Capa de producto | Landing, zona app, dashboard, functions, catálogo 49, hub ×2, changelog, cripto, banners, email | opus + sonnet | 0,71 M | **0,75 M** | + el arreglo del `comingSoon` vacío |
| Refutaciones y fixes | Refutación de xlsx + de documentos + fixer | opus + sonnet | ≈1,50 M | **1,6 M** | 46 hallazgos en pastelería; no hay motivo para esperar menos |
| Gates y LIVE | Batería, Stripe, env, Resend, verificación | Fable | (dentro de la capa) | **0,25 M** | |
| | | | **≈14,1 M** | **≈14,8 M** | |

🔴 **Queda por encima del objetivo de 11-13 M de John, igual que le pasó a Pastelería, y hay que decirlo ANTES de
arrancar.** Las palancas, medidas:

1. **Bajar a 8 libros** (absorber el 3 en el 4 y el 10 en el 7): **−0,60 M** → ≈14,2 M. **Coste real:** el
   argumento comercial más fuerte del producto queda enterrado dentro de otro libro.
2. **Repetir la palanca de Pastelería** (`bloques: 1` en los capítulos no legales): ya está dentro de la
   estimación de redactores; **no da margen adicional**.
3. **Reducir el bonus 2 de 12 decisiones a 8**: **−0,4 M**. Coste: es el bonus que más valor percibido da por
   página.
4. **Lo que de verdad puede ahorrar 1,5 M y no cuesta calidad:** **arreglar los dos bugs de tubería antes de
   redactar** (`es_fila_porcentual()` y el gate de tipo en `verificar_guion.py`). En Pastelería esos dos bugs
   generaron 5 de los 11 hallazgos altos y su correspondiente ronda de fixer + regeneración de bloques.

**Estimación honesta: 14-15 M.** Prometer 12 sería repetir el error que la propia SPEC de Pastelería documentó.

### 6.2 Riesgos de pipeline, por orden de probabilidad × daño

| # | Riesgo | Probabilidad | Mitigación |
|---|---|---|---|
| **R-1** 🔴 | **Los `%` en los nombres de la carta rompen las tablas** (`documentos.py:722`) | **Casi segura** — la carta de chocolate está llena de porcentajes | **Arreglar `es_fila_porcentual()` ANTES de construir** (mirar sólo `fila[0]`, o exigir `)` / «en» delante del `%`). Y un gate que busque `%` en columnas de °C, horas o días |
| **R-2** 🔴 | **Una referencia de celda desplazada mete texto donde va una cifra y el redactor se lo inventa** | Alta (pasó con 6 de 315 referencias) | **Añadir a `verificar_guion.py` el aborto por tipo**: formato `eur*`/`pct*`/`num*` ⇒ valor numérico obligatorio |
| **R-3** | **L3 no puede cerrar el EUDR** | Media | Plan B ya escrito (§5.8): capítulo 11 reducido a «qué le pides a tu proveedor» + anexo. **No se inventa** |
| **R-4** | **El mismo concepto calculado en dos libros** (coste de cobertura en escandallo, sensibilidad y stock) | Media-alta | **Una fuente por concepto**, declarada en la SPEC, y gate que compare celda a celda |
| **R-5** | **Las unidades de campaña no cuadran con el mix anual** (A8) | Media-alta | §5.6: se calculan desde el mix, con fila de cuadre y semáforo |
| **R-6** | **El libro estrella se queda sin prosa que lo explique** (B1) | Media | Regla nueva: todo libro ⭐ tiene epígrafe propio, y el gate busca su vocabulario en el `.md` |
| **R-7** | **El `comingSoon` vacío deja un rótulo huérfano en el hub Astro** | **Segura si no se toca** | §4.1, en el mismo commit |
| **R-8** | **La guía de Pastelería sigue sin pushear y sin Payment Link** | Cierta hoy | **No se arranca el producto 49 con el 48 a medias.** Cerrarlo primero |
| **R-9** | **Térmica**: `documentos.py` y los 10 constructores son python local | Alta (hoy se llegó a **67,4 °C** sólo leyendo) | `istats cpu temp` entre fases, **un python cada vez**, `scripts/termica/watchdog-termico.sh` activo, **sin builds locales ni Playwright**; deploy en la nube |
| **R-10** | **Regenerar pisa ediciones manuales** | Media | Prohibido reejecutar `fase8c-libreria-assemble.py`; los xlsx **nunca se tocan a mano, se regeneran**; commitear WIP de subagentes |

---

## 7. Preguntas abiertas para John

Están en el objeto estructurado. La más urgente es la primera: **el producto 48 no está pusheado.**

---

*Informe de research. No contiene contenido de producto. Cada cifra lleva su origen; lo no verificable va marcado
«sin fuente». Método: lectura directa de ficheros del repo (openpyxl `read_only`, PyMuPDF, zipfile, grep), sin red.*

Via: Claude Code
