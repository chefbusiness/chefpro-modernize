# LENTE 5 — Activos propios, frontera, canales y entregables · «Cómo Montar una Churrería-Chocolatería»

- **Producto:** guía «Cómo Montar» nº 51 (tamaño L, 65 € orientativo) · **Fecha:** 2026-10-03 · **Sesión:** Claude Code en el Mac.
- **Método:** 100 % local, sin web. Lectura del repo en `main` (`f23fca98`): SPEC, guion, `datos_ejemplo.py`, landing y refutación de documentos de la hermana; los 9 xlsx de la hermana y los de los productos frontera (openpyxl `read_only`, uno cada vez, o `unzip -p` de las hojas); capa de producto (catálogo, hub ×2, robots, zona-app, functions, buscador, blog, casos de uso). `istats cpu temp` entre lecturas: 48,8-62,2 °C; una pausa de enfriado a < 58 °C al tocar 62,2 °C. Sin navegador ni Playwright.
- **Ids:** solo se REUTILIZAN `CHN-*` / `CHS-*` (verificados el 12-09-2026, ficheros `auditorias/guia-chocolateria-verificacion-legal-2026-09-12.json|.md` e `auditorias/guia-chocolateria-ids-CHS.json`) y `CUS-M*` de la L1 de este producto (`auditorias/guia-churreria-research-L1-mercado-cliente.md`). Esta lente **no crea ids nuevos**: no consultó ninguna fuente externa. Lo que pide fuente nueva va marcado **«sin fuente»** y asignado a la lente que debe cerrarlo.
- **Referencias `fichero:línea`** = estado del repo el 2026-10-03.

## 0. Limitaciones declaradas

| # | Limitación | Efecto |
|---|---|---|
| L-1 | Sin web: ninguna norma ni precio nuevo verificado aquí | Todo lo nuevo de churrería (fritura, aceite, acrilamida, venta ambulante, convenio de hostelería, precios de churrera/freidora) queda **«sin fuente»** → lente normativa (CUN) y lente de sector (CUS) |
| L-2 | `buscador-report.py` exige `ADMIN_PASSWORD` y lee Netlify Blobs (`scripts/productos-digitales/buscador-report.py:28-30`) | **No sé si alguien buscó «churr» en el hub.** Hay que correrlo en F3 con la credencial |
| L-3 | Cola de Resend leída del calendario, no por `GET /broadcasts` | El hueco del 13-nov es **del documento** (`CALENDARIO-V2-SEMANAL.md:223`), no confirmado por API |
| L-4 | De los xlsx frontera leí hojas, cabeceras y celdas clave, no cada fórmula | Las reglas de no-solape citan hoja; la celda solo donde la abrí |
| L-5 | Costes de tokens de la hermana: los del calendario (`CALENDARIO-V2-SEMANAL.md:397-398`), no un recuento de transcripts | Estimaciones de §5 con esa base; ±15 % |

---

## 1. La hermana, por el molde

### 1.1 Las 53 decisiones de la SPEC: qué se hereda como decisión de FAMILIA

| Decisión hermana (`guia-chocolateria-SPEC.md`) | ¿Familia? | Para la churrería |
|---|---|---|
| D1 alcance con variantes como columna de escenario | **Sí (patrón)** | Se repite el patrón: caso central + columnas de variante (§4.4) |
| D2 variante «sin cifras de maquinaria» si no hay precio público | **Sí** | Aplica a churrera/freidora/extracción hasta que CUS los cierre (hoy `CHS-49`: sin precio) |
| D3, D4, D15, D18, D35, D37-D41, D47-D48, D52-D53 | No (chocolate/cacao/EUDR/kit) | Se deciden de nuevo o no aplican |
| D5 norma viva con fecha de revisión DENTRO | **Sí** | Para la norma del aceite y la de acrilamida, si la lente normativa las confirma vivas |
| D6 `comingSoon` con guarda server-side | **Hecha** | La guarda ya existe: `ProductosDigitalesHubPage.astro:1511` `{comingSoon.length > 0 && (` |
| D7 / D32 cero salidas entre libros: celda verde «cópialo del libro N» + fila de cuadre con semáforo | **Sí** | Obligatoria (§4.2) |
| D8 / D28 hueco de Resend condicionado y confirmado por API | **Sí** | §3.4 |
| D9 / D43 convenio: REGCON + una tabla de ejemplo + método | **Sí (método)** | Convenio a decidir de nuevo (hostelería ≠ confiterías de `CHN-65`) |
| D10, D21, D22, D24, D41, D42 | Parcial | Reutilizables por id donde la norma es la misma (Ley 12/2012, IAE, Ley 1/2025, IVA) |
| D11 franquicia como «orden de magnitud publicado», nunca dato auditado | **Sí** | Con la tabla `CUS-M13…M24` de L1 |
| D12 / D27 FAQ de consultoría con inversiones inventadas | **Sí (vigilar)** | No hay FAQ de churrería en `use-cases-content.es.consultor.ts` (grep «churr» solo da chimichurri/churrasco) |
| D13 voz de John no bloquea | **Sí** | Igual |
| D14 / D20 / D29 / D50 presupuesto que SUMA, palanca de bloques | **Sí** | §5 |
| D16 nace con cripto | **Sí** | Hoy `CRYPTO_PRODUCTS=all`: nada que tocar en la env (`CLAUDE.md`, sección NOWPayments) |
| D17 un solo nombre visible | **Sí** | «Cómo Montar una Churrería-Chocolatería» (el de la tarjeta, `…HubPage.astro:1015`) |
| D19 argumento legal publicado con su límite dentro | **Sí** | Para el 644.6 (§1.4) |
| D23 ningún sumando sin fuente como número cerrado; «desde» = suelo | **Sí** | Crítico en maquinaria de churrería |
| D25, D39 FAQ sin preguntas de consumidor | **Sí** | «churreria» 110.000/mes es intención de consumidor (dato del encargo) |
| D26 recuento de líneas de generadores para dimensionar | **Sí** | §5 |
| D30 / D31 la guía CITA lo que ya publica la casa; un concepto = una fuente | **Sí** | Aceite: citar `pack-appcc/09` (§2, R4) |
| D33 no calcular lo que no tiene coeficiente con fuente | **Sí** | Extracción de humos: semáforo + preguntas al instalador, no cálculo de caudal sin fuente |
| D34 árbol en vez de umbrales sueltos | **Sí** | Árbol IAE/CNAE por modelo (§4.2 libro 8) |
| D36 el valle se modela con lo que para y lo que sigue | **Sí** | Verano: cierre / carta de verano / ferias (libro 5) |
| D44 fusión de ids con gate de recuento | **Sí** | `CUN-*` y `CUS-*` al JSON común con `guia-chocolateria-json-merge.py` como molde |
| D45 `puntos_por_epigrafe` | **Sí** | Obligatorio (en Chef Ejecutivo, sin él: ≈2,2 M de desduplicación, SPEC hermana §9) |
| D46 banners con `fase8x-sustituir-banner.py --producto` | **Sí** | Existe: `scripts/astro-migration/fase8x-sustituir-banner.py` |
| D49 nombres de fichero firmados antes del guion | **Sí** | §4.2 |
| D51 nombre del caso comprobado en la OEPM | **Sí** | §4.5 |

### 1.2 Libro a libro: qué se reutiliza, qué no aplica, qué falta

| Libro hermana (`public/dl/guia-chocolateria-obrador/`) | Hojas (leídas) | REUTILIZABLE como estructura | NO aplica a churrería | Lo que la churrería necesita y no está |
|---|---|---|---|---|
| 1 `capacidad-obrador-y-clima` | Parámetros · Zonas y m2 · Clima del Obrador · Capacidad por Equipo · Cuello de Botella · Ficha de Visita a Local | Capacidad por Equipo → Cuello de Botella → Ficha de Visita (eliminatorios) | Clima 16-18 °C/HR, cámara de chocolate | Churros/hora por churrera + freidora, demanda por franja, **cola del domingo**, ítems eliminatorios de humos a cubierta, gas y ruido |
| 2 `calculadora-capex-chocolateria` | Parámetros · CAPEX por Bloque · **Variante del Formato** · Traspaso vs Obra Nueva · IVA y Tesorería · Resumen | Todo el esqueleto (bloques, base de IVA por línea, traspaso a 5 años, fondo de maniobra traído del plan) | Bloques «Climatización y deshumidificación», «Equipo de templado», «Packaging y moldes» | Bloques de extracción/filtros/conducto, freidoras y churreras, sala y terraza; columnas despacho · feria · franquicia |
| 3 `sensibilidad-al-precio-del-cacao` | Coste de Cobertura · Escenarios de Precio · Repercusión al PVP · Stock | Escenarios de subida → repercusión (4 salidas) | Cacao como insumo crítico | Sensibilidad al precio del **aceite y la harina** (cabe como hoja del libro de aceite) |
| 4 `carta-de-apertura-y-escandallo-chocolate` | Denominaciones y Mínimos · Escandallo por Molde y Tanda · Merma de Templado · Coste Hora · Unidad vs Caja · Mix y Ticket Medio · Decisión de Surtido | Coste Hora · Mix con dos temporadas · Decisión de Surtido (margen € × rotación) · «Unidad vs Caja» → «Ración vs docena/kg» | Denominaciones del RD 1055/2003 por bombón; tanda por molde | Escandallo **por kg de masa**: rendimiento masa→piezas, **absorción de aceite**, porra vs churro, taza |
| 5 `vida-util-rellenos-y-rotacion` | Tipo de Relleno y aw · Vida Útil Declarada · Etiquetado o Granel · Temperatura y Vitrina · Lote y Merma | Patrón «la declaras TÚ; la hoja la recoge» | Todo (aw de ganache, vitrina) | Vida en exposición del churro frito y de la masa (sin fuente) → cabe en el libro 3, no libro propio |
| 6 `campanas-y-valle-del-ano` | Calendario de Campañas · Peso sobre el Año · Capacidad vs Demanda del Pico · Refuerzo y Tesorería · El Valle de Agosto | Peso sobre el Año (12 coeficientes supuestos) · Capacidad vs Pico · Refuerzo · Valle | Campañas de bombonería (San Valentín, Pascua, comuniones…) | Pico oct-mar, domingos, Reyes; **franjas** (desayuno/merienda/madrugada); valle de verano con tres salidas |
| 7 `plan-financiero-3-anos-chocolateria` | 0. Supuestos · Inversión · PyG 3 Años · Punto de Equilibrio · Escenarios · Personal · Tesorería · Financiación · Canales y Punto Muerto · Talleres | Motor `planes-v2_0` 2.2 entero; «Canales y Punto Muerto» | Talleres y Regalo Corporativo | Canales sala / para llevar / ferias; personal con madrugada |
| 8 `checklist-legal-licencias-y-cacao` | Checklist Legal (F1-F6) · Árbol de Registro Sanitario · Suministro a Otros Minoristas · Ruta Doméstica · Cadmio · EUDR · Registro de Formación · Cronograma y Ruta Crítica | F1-F6 · Árbol de Registro · Registro de Formación (`CHN-69`) · Cronograma por índices | Cadmio, EUDR, Ruta Doméstica | Árbol IAE/CNAE por modelo, humos/actividad, aceite y gestor, venta ambulante, terraza y horario, PRL fuego de aceite |
| 9 `checklist-equipamiento-y-proveedores-cacao` | Equipamiento · Variante del Formato · Proveedores y EUDR · Clientes a los que Suministras · Contador | Equipamiento línea a línea (base de IVA, plazo) · Contador | EUDR, clientes | Proveedores de harina, aceite, chocolate a la taza, envase |

### 1.3 Cifras que la hermana YA publica sobre «taza y churros» — esta guía no puede contradecirlas

| Dato publicado | Dónde (leído hoy) | Id |
|---|---|---|
| Chocolatera Ugolini Delice 3 (3 L) **527 € sin IVA**; es la **única** línea con precio | `calculadora-capex-chocolateria.xlsx!Variante del Formato` y `checklist-equipamiento-y-proveedores-cacao.xlsx!Variante del Formato` | `CHS-46a` (https://www.equipoh.com/chocolateras-196, 2026-09-12) |
| Churrera, freidora, extracción y campana-conducto: «SIN PRECIO VERIFICADO» | mismas hojas | `CHS-49` |
| Ración de 4 uds ~2,50 €; con chocolate 3,50-4 € (+40-60 %); pieza 0,30-0,70 € | `datos_ejemplo.py:2299-2300` · `plan-financiero…!PyG 3 Años` | `CHS-32` (https://es.loomispay.com/blog/rentabilidad-churreria-2025, 2026-09-12) |
| Margen bruto del churro 85-90 % frente a «un poco más del 50 %» de un maestro churrero: **se publican los dos** | `datos_ejemplo.py:2301-2304`; el P&L de la hermana usa **50 %** | `CHS-31` |
| Traspasos churrería-chocolatería: Elche 75 m² (sin precio) · Vallecas 74 m², 82.000-95.000 €, renta 910 €/mes · Mataró 118 m², 58.000 € — precios PEDIDOS | `datos_ejemplo.py:2309-2315` | `CHS-37a/b/c` (https://www.milanuncios.com/traspasos/chocolateria.htm, 2026-09-12) |
| Escenario P&L año 2: +35 clientes/día (supuesto), PVP 3,50 €, margen línea 50 %, personal +12.462,96 €/año, otros fijos +1.200 €/año → ventas 199.088 → 232.942 €; resultado neto 17.269 → 20.044 €; margen neto 8,67 % → 8,60 % | `plan-financiero-3-anos-chocolateria.xlsx!PyG 3 Años` A54:C68 | supuestos + `CHS-31/32` |
| Punto muerto mensual 14.231 € (bombonería) frente a 16.547 € (con taza y churros) | `…!Punto de Equilibrio` | derivado |
| Legal: el Anexo de la Ley 12/2012 incluye el 644.5 y **ningún grupo de la agrupación 67**; el grupo 676 queda fuera de la inexigibilidad de licencia | landing `guia-chocolateria-obrador.ts:286` y `:349`, CAPEX, P&L, guion `:653-672` | `CHN-49`, `CHN-49b`, `CHN-49c` (https://www.boe.es/buscar/act.php?id=BOE-A-2012-15595) |
| Gas: inspección de la instalación receptora cada 5 años si hay freidora de gas | `datos_ejemplo.py:2286-2290` | `CHN-48` (BOE-A-2006-15345) |
| Taza servida en sala = hostelería, IVA 10 % | `datos_ejemplo.py:1420-1430` | `CHN-71c` (BOE-A-1992-28740) |
| Con mesas, el art. 8 de la Ley 1/2025 obliga aunque seas microempresa | `datos_ejemplo.py:1424-1427` | `CHN-92` (BOE-A-2025-6597) |
| «Chocolate a la taza» ≠ «chocolate caliente» (lleva almidón); denominación ≥35 % cacao total, ≥18 % manteca, ≥14 % desgrasada, ≤8 % harina/almidón; familiar 30/18/12 y ≤18 % | SPEC hermana `:409`, `:610` | `CHN-05` (BOE-A-2003-15599) |
| Franquicia Maestro Churrero: **fila sin cifras** («hueco declarado») | `calculadora-capex…!Variante del Formato`; `datos_ejemplo.py:2335-2346` | sin id en la hermana |

### 1.4 Hallazgos sobre la hermana que tocan a este producto

1. **Veredicto del P&L por ratio, no por euros.** `PyG 3 Años!B68` compara `C67>B67` (margen neto en %): con los supuestos publicados dice «La taza y los churros **restan**: te ocupan sala y personal para nada», mientras el resultado neto **sube** de 17.269 a 20.044 €/año (+2.775 €). Riesgo: si esta guía dice que una churrería-chocolatería es viable, el comprador de las dos lee una contradicción aparente. No es contradicción de dato, pero sí de mensaje. → Decisión abierta 4.
2. **El 644.6 está DENTRO del Anexo de la Ley 12/2012, y la hermana no lo dice.** `CHN-49b` verifica que el Anexo incluye «el grupo 644 completo —644.1 … 644.6—»; `CHN-72` (verificación `.md:231`) cita que el 644.6 «faculta la elaboración de los productos de churrería»; el literal del epígrafe («Comercio al por menor de masas fritas, con o sin coberturas o rellenos, … preparados de chocolate y bebidas refrescantes») está en `auditorias/guia-chocolateria-research-L3-normativa.md`, **no** en una ficha `CHN` propia. **Hipótesis para la lente normativa:** la churrería de DESPACHO sin consumo en el local (variante b) podría quedar en la inexigibilidad de licencia previa hasta 750 m² y la de consumo en sala (676 u otro grupo de la 67) no. No contradice a la hermana (habla de la «chocolatería de taza»), pero **convierte la frontera (a)/(b) en frontera legal**. Verificar: literal del 644.6 en BOE-A-1990-23930, alcance real del art. 2 de la Ley 12/2012 y si la fritura arrastra calificación ambiental autonómica pese a la inexigibilidad. Si se confirma → `CUN-*` nuevo con el límite dentro (patrón D19).
3. **Convenio con «masas fritas» en el nombre:** `CHN-93` (REGCON, 2026-09-12) recoge el de Toledo, código 45000145011981, «MAZAPÁN, MASAS FRITAS, CONFITERÍAS Y CHOCOLATES», vigencia 01/01/2025-31/12/2026 (verificación `.md`, fila de `CHN-93`). Es la única prueba en casa de un convenio que nombra la churrería. Con sala, el candidato natural es el de hostelería provincial → **sin fuente**, lente normativa.
4. **El P&L de la hermana usa el 50 % de margen** (el bajo de `CHS-31`). Si esta guía modela el churro con 85-90 %, tiene que explicar en la misma hoja por qué difieren (bruto sobre materia prima frente a margen tras aceite, mermas y mano de obra), o el comprador de las dos ve dos márgenes para el mismo churro.
5. **Trampas ya cazadas en los documentos de la hermana** (`auditorias/guia-chocolateria-docs-refutacion-2026-09-19.md`: 63 hallazgos únicos, 26 altos) que este molde arrastraría si no se blindan: constantes de Python impresas literales (`F_KIT_08_APERTURA`, A13/C9); celdas con salto de línea que rompen la tabla Markdown (C1, precisamente en la tabla de variantes de taza y churros); bases de IVA mezcladas en una comparación (C10, B18, B24); precios «desde» publicados como cerrados (A14, B7); porcentajes mal calculados (A1, A2); la misma frase repetida seis veces (C17); tablas de datos sin tildes (C16); punto decimal inglés (A24); dos cifras distintas del mismo canal entre guía y bonus (B22/C20); promesas de recuento que la tabla desmiente (C14, C24, A25).

---

## 2. Frontera y reglas de no-solape

### 2.1 Qué cubre ya cada producto vecino (abierto hoy)

| Producto (precio, `products-catalog.ts`) | Qué cubre que roce a la churrería | Evidencia |
|---|---|---|
| `guia-chocolateria-obrador` (65 €) | Taza y churros como epígrafe del cap. 01 + columnas de escenario (§1.3) | ver §1.3 |
| `kit-tareas-chocolateria` (12 €) | Bombonería en marcha; «chocolate caliente» solo como producto de invierno en el calendario | `BONUS-02-calendario-anual-tareas.xlsx` (única mención; cero «churro», cero «a la taza», cero «freidora» en los 11 ficheros) |
| `plan-negocio-food-truck` (29 €) | Vehículo 25.000 €, adaptación 8.000 €, cocina móvil 10.000 € (con freidora), generador; ticket 12 € sin IVA, 45 clientes/día, 250 días; gestor de aceite (400 €); SGAE en ferias (200 €); convenio «hostelería o comercio según clasificación de la venta ambulante» | `plan-financiero-food-truck.xlsx!Inversión Inicial`, `!0. Supuestos`, `!Personal`; checklist F1-F6 con «Acuerdos con mercados y eventos» (F5) |
| `kit-tareas-food-truck` (12 €) | Licencia de venta ambulante (2-3 meses de antelación), seguro RC, IAE, temporadas de ferias y festivales, briefing pre-evento | `04-permisos-eventos-localizaciones.xlsx!Permisos y Eventos`, `08-eventos-estacionales.xlsx`, `BONUS-01-briefing-pre-evento.xlsx` |
| `plan-negocio-cafeteria` (29 €) / `kit-tareas-cafeteria` (12 €) | Plan financiero genérico de cafetería-brunch; en el kit: vaciado de freidora «solo por debajo de 40 °C», retirada de aceite por gestor, «chocolate caliente especial» en Navidad | `kit-tareas-cafeteria/01-apertura-cierre.xlsx`, `05-tareas-semanales-mensuales.xlsx`, `06-eventos-festivos.xlsx`; el plan no menciona churros |
| `pack-appcc` (14 €) | **Sí cubre el control del aceite de fritura**: `09-control-aceite-fritura.xlsx`, hojas «Instrucciones», «Control Aceite» (Fecha · Freidora · Tipo de test · % CP · Tª máx. · Estado · Acción) y «Retirada de aceite usado» (litros, gestor, nº documento). Estado en `Control Aceite!F5:F44`: `CAMBIAR` si Tª > 180 °C o CP ≥ 25 %, `VIGILAR` ≥ 20 % | `Instrucciones!B13` («Máximo 25 % de compuestos polares — Orden de 26 de enero de 1989»), `!B14` (180 °C), `!B16` (LER 20 01 25), `!B20` (un test por freidora y semana); también `12-analisis-peligros-haccp.xlsx` menciona fritura |
| `kit-escandallos` (12 €) | Sin churro. `08-food-truck.xlsx` trae «Costes fijos del día» con «Alquiler de plaza / canon del mercado 60 €/día» y una hoja «Punto de Equilibrio» diario | hojas Smash Burger · Loaded Fries · Pulled Pork · Punto de Equilibrio · Conversiones · Mermas |
| Guía Food Cost + Ingeniería de Menú (55 €) | Método genérico: ficha de escandallo, rendimiento y mermas, multimétodo de precio, prime cost, repricing | `ficha-escandallo-base.xlsx`, `rendimiento-mermas-producto.xlsx`, `precio-objetivo-multi-metodo.xlsx`… |
| `kit-inventario` (14 €) | Inventario genérico | (no abierto: sin rastro de fritura en el barrido de hojas) |

### 2.2 Reglas numeradas

| # | Riesgo | Regla |
|---|---|---|
| R1 | Contradecir a la hermana en legal | La frase del 676/agrupación 67 se reutiliza **literal** (`CHN-49c`). Lo nuevo del 644.6 entra solo con `CUN-*` verificado y con su límite dentro (D19) |
| R2 | Contradecir a la hermana en cifras | Ticket 2,50 → 3,50-4 € y margen 85-90 % / ~50 % se publican con `CHS-31/32`, **los dos márgenes juntos** y el porqué de la diferencia; si esta guía usa otro margen en su P&L, lo dice y lo justifica |
| R3 | Pisar la bombonería | Ni plantillas de bombón ni templado. Epígrafe espejo en el cap. 01 («la bombonería es OTRO negocio») que remite a la hermana con enlace; la hermana añade el enlace inverso en su FAQ (`guia-chocolateria-obrador.ts:286`) |
| R4 | Duplicar el registro de aceite del Pack APPCC | Esta guía **no** trae registro diario de % CP: **calcula coste, consumo y punto económico de cambio** y cita `pack-appcc/09-control-aceite-fritura.xlsx!Control Aceite` como el registro. Los umbrales (25 % CP, 180 °C) se citan de ahí, y si la lente normativa los corrige, **se corrige el Pack primero** (un concepto = una fuente) |
| R5 | ⚠️ 180 °C del Pack frente a la temperatura real de fritura del churro | **Sin fuente** la temperatura de fritura del churro. Si el sector fríe por encima de 180 °C, el Pack marcaría «CAMBIAR» en cada fritura: conflicto con un producto vivo. Lente normativa: verificar si la Orden de 26-01-1989 fija tope de temperatura y su vigencia |
| R6 | Copiar el food truck en la variante feria | La variante (c) es **caseta/remolque de churros en ferias**, no un vehículo-cocina: sin vehículo ni ITV ni generador como eje. Lo que el food truck no tiene y esta guía sí: **punto muerto por EVENTO** (canon/tasa por m² y día, montaje, desplazamiento, producción por evento) y la **estacionalidad invertida** (L1 B2-4). Se enlaza a `plan-negocio-food-truck` y `kit-tareas-food-truck` para quien va a vehículo |
| R7 | Copiar el «canon del mercado» del Kit Escandallos | El libro de ferias calcula por evento de varios días; si cita un coste diario de plaza, **no reutiliza los 60 €/día** del kit (supuesto, sin id) |
| R8 | Pisar la cafetería | Variante (e) = epígrafe + remisión a `plan-negocio-cafeteria`/`kit-tareas-cafeteria`; aquí solo «qué cambia al meter freidora» (humos, licencia, aceite, PRL) |
| R9 | Pisar el Kit Escandallos y la Guía Food Cost | Escandallo propio **solo** de lo que ninguno tiene (masa por kg → piezas, absorción de aceite, porra, taza); el método genérico se cita y se vende cruzado |
| R10 | Registro sanitario contradictorio entre productos | `kit-tareas-food-truck/04-permisos-eventos-localizaciones.xlsx` dice «Registro sanitario del vehículo (RGSEAA)»; la hermana publica un árbol que saca del registro estatal al minorista (`checklist-legal…!Árbol de Registro Sanitario`). La lente normativa decide para la caseta de feria y, si el kit está mal, se anota como deuda del kit (no se arregla aquí) |
| R11 | Obrador B2B (masa, churro congelado/prefrito) | **Fuera**: una línea de «qué cambia» (RGSEAA, suministro a otros minoristas; la hermana ya tiene el árbol del art. 3 del RD 1021/2022, `CHN-*` de su libro 8). L1 no encontró demanda (A5-f) |
| R12 | Contradecir al post del blog que vende el producto | Ver §3.3: el post publica cifras sin fuente que la guía no podrá sostener |

---

## 3. Capa de producto y canales

### 3.1 Estado medido

| Superficie | Hoy | Al publicar | Cita |
|---|---|---|---|
| `src/data/products-catalog.ts` | **50** ids | 51 (`guia-churreria-chocolateria`, `€65`) | `grep "id: '"` = 50; sin comentarios entre `description: {` y `es:` (parser del ensamblador) |
| `netlify/shared/payment-links.ts` · `product-prices.ts` | **52** cada uno (50 ES + `food-cost-templates` + `restaurant-inventory-templates`) | 53 · 53 (generados: `sync-payment-links.py`, `sync-product-prices.py`) | hermana en `:6` y `:7` |
| `astro-site/src/lib/zona-app.ts` | **52** `productId:` en el registro | 53 | hermana en `:100` |
| 4 functions | `verify-purchase.ts:210` · `resend-access.ts:205` · `admin-generate-access.ts:36` · `get-download-urls.ts:376-390` | 1 entrada en cada una; `get-download-urls` con 14-15 claves | |
| Hub Astro `comingSoon` | **21** tarjetas (`…HubPage.astro:1014-1036`), la nuestra en **:1015** | Se retira; quedan 20 (la guarda de `:1511` ya existe) | el encargo decía 22: son 21 |
| Hub SPA `comingSoon` | **21** (`src/pages/ProductosDigitales.tsx:997-1019`), la nuestra en **:998** | Se retira en el gemelo | |
| Hub `products` | Orden «novedades primero, ✨ solo las 5 últimas, Mega Pack último» (`…HubPage.astro:63-66`) | Tarjeta real en posición 1 en los dos gemelos; la 5.ª novedad actual pierde el «✨»; ItemList JSON-LD (`…HubPage.astro:1125`, `ProductosDigitales.tsx:1097`) | |
| `astro-site/public/robots.txt` | `/guia-*-access` y `/guia-*-library` en los 5 bloques de user-agent (`:44-45`, `:98-99`, `:152-153`, `:206-207`, `:260-261`) | **Nada que tocar.** `/guia-churreria-chocolateria` no contiene `-access` ni `-library` → rastreable; `-access`/`-library` → bloqueadas. Verificar con `robots-gate.py`, no suponerlo | |
| Slug | `guia-churreria-chocolateria` libre: cero coincidencias en `src`, `astro-site/src`, `netlify`, `_redirects` | | grep 2026-10-03 |
| Plantilla | `GuiaLandingPage.astro`: `cryptoEnabledFor(data.slug)` en `:44`, tres `CryptoPayButton` en `:265`, `:567`, `:662` | Nada que tocar; wrapper con `whatsapp={false}` y env literal (`guia-chocolateria-obrador.astro`) | |
| Changelog | hermana en `src/data/productos-changelog.ts:146` (v1.0 «Lanzamiento») | v1.0 | |
| Buscador | `sinonimos-buscador.json`: 11 grupos, 4 frases, 8 alias; **cero** grupos con churro/porra/chocolate; alias de la hermana en `:111` | Alias nuevo (`churreria churros porras tejeringos chocolate a la taza freidora feria caseta franquicia…`). No crear grupo de sinónimos que no exista en ninguna card | |
| Búsquedas reales de «churr» | **no medido** (L-2) | `buscador-report.py --days 90` en F3 | |
| Pickaxe | Sin agente de churrería; afines: «Chocolatería Creativa», «Chocolatero Consultor Pro», «Food Truck AI+» | Nombrarlos solo tras cotejar `fase8c-agentes/catalogo-hub.json` | |

### 3.2 Casos de uso que deberían enlazar (`productIds`, primera posición o segunda)

| Página de rol | Fichero:línea | Hoy | Propuesta |
|---|---|---|---|
| `chocolateria` | `src/data/use-cases-content.es.ts:3248` | hermana 1.ª | añadir en 2.ª |
| `chocolatero` | `:1264` | hermana 1.ª | no (es bombonero) |
| `cafeteria-brunch` | `:2255` | pastelería 1.ª | añadir (variante e) |
| `food-truck` | `:4532` (bloque) | `kit-tareas` genérico, **sin** los dos productos de food truck | añadir aquí la churrería es dudoso; anotar como deuda que esta página no vende sus propios productos |
| `coffee-shop-specialty` | `:4240` | kit cafetería | no |
| `chocolatero-consultor` | `use-cases-content.es.consultor.ts:386` | hermana 1.ª | no |

`PRODUCT_ALIASES` en `src/lib/linkify-use-case.tsx:29` y `astro-site/src/lib/linkify-use-case.ts:33`; desplegable de `src/pages/AdminGenerateAccess.tsx:61`; `src/data/productos-digitales-config.ts` (mapa de ficheros, la hermana aparece 17 veces).

### 3.3 El post `ia-churrerias-guia-completa.md` (el único del tema)

- **3 banners**, todos ajenos: `/guia-dark-kitchen`, `/kit-tareas-bar`, `/kit-tareas-restaurante-creativo` (UTM `utm_content=ia-churrerias-guia-completa`). La hermana lo dejó «No tocar» por D1 (SPEC `:652`); ahora es **el** post del producto.
- **Sustitución quirúrgica** con `fase8x-sustituir-banner.py --producto guia-churreria-chocolateria`: banner 1 → esta guía; banner 2 → `guia-chocolateria-obrador`; banner 3 → `pack-appcc`. Lista `NUNCA` del script: `pack-appcc`, `kit-escandallos`, `guia-chocolateria-obrador`.
- 🔴 **El post publica cifras sin fuente que la guía no podrá sostener** (frontmatter `faq` y tablas, `:52-60`, `:90-95`, `:105-113`): inversión total «12.000-50.000 €», maquinaria «5.000-17.000 €», margen bruto «60 %», «40.000 a 60.000 €» de beneficio anual (eco de `CHS-33`, fiabilidad **baja**: solo resumen de buscador), 88 raciones/día de punto de equilibrio. Y una contradicción interna: la tabla de inversión suma como mínimo 26.000 € con sus propios suelos (5.000 + 2.000 + 2.000 + 3.000 + 500 + 13.500) y publica «12.000» como total mínimo. Enlazar desde ahí a una guía con cifras con fuente expone la discrepancia. → Decisión abierta 5. Al tocar el `faq:` del frontmatter: `rm -rf astro-site/.astro astro-site/dist` antes del build y `fase8b-regen-lastmod.py` después (CLAUDE.md, gotchas del blog).
- Enlaces internos actuales del post: solo `8-errores-que-destruyen-el-food-cost…` (×2), `/productos-digitales` (×2), `como-abrir-restaurante-ia-guia-completa`. No hay otro post de churrería: grep «churr» en el blog da chimichurri/churrasco y menciones sueltas.

### 3.4 Resend

Cola ES según `CALENDARIO-V2-SEMANAL.md:217` y `:221-223`: … Taquería 29-oct ✅ · Escandallos 2.1 3-nov · Kit Chocolatería 2.1 **8-nov (solo si está LIVE)** → hueco **13-nov 08:00 UTC**; si el kit 2.1 no sale, **8-nov**. Programable a ≤30 días: el 13-nov desde el **14-oct**. Confirmar con `GET /broadcasts` antes de escribirlo en el handoff (D28 de la hermana). Saludo «Hola, colegas» (regla del 21-sep).

### 3.5 Lista completa de lo que se toca para publicar el producto 51

| # | Fichero | Qué |
|---|---|---|
| 1 | `astro-site/src/data/productos/guias/guia-churreria-chocolateria.ts` | Ficha `GuiaData` calcada de la hermana: sin `priceOld`, sin `discountBadge`, sin `aggregateRating`, `testimonials.items: []`; FAQ con «¿sirve fuera de España?» y «¿cubre la bombonería?» |
| 2 | `astro-site/src/pages/guia-churreria-chocolateria.astro` | Wrapper; `VITE_STRIPE_PAYMENT_LINK_GUIA_CHURRERIA_CHOCOLATERIA` literal; `whatsapp={false}`; `locales={['es']}` |
| 3-5 | `…-access.astro`, `…-library.astro`, `islands/library/GuiaChurreriaLibraryIsland.tsx` | Generados con `fase5-generate-zona-app.py` |
| 6 | `astro-site/src/lib/zona-app.ts` | Entrada (52 → 53) — también dispara la tarjeta Miselup (`miselup-gate.py`) |
| 7-9 | `src/App.tsx`, `src/pages/GuiaChurreriaAccessGate.tsx`, `src/pages/GuiaChurreriaDashboard.tsx` | Rutas y dashboard |
| 10 | `src/data/products-catalog.ts` | 50 → 51 |
| 11-12 | `netlify/shared/payment-links.ts`, `product-prices.ts` | Regenerar (52 → 53) |
| 13-16 | 4 functions | `PRODUCTS` + `PRODUCT_FILES` |
| 17-18 | `src/data/productos-digitales-config.ts`, `src/data/productos-changelog.ts` | Espejo + v1.0 |
| 19-20 | `…HubPage.astro` y `src/pages/ProductosDigitales.tsx` | Quitar `comingSoon` `:1015`/`:998`; tarjeta en posición 1; ItemList; rotar «✨» |
| 21 | `astro-site/src/lib/sinonimos-buscador.json` | Alias |
| 22-23 | `src/lib/linkify-use-case.tsx`, `astro-site/src/lib/linkify-use-case.ts` | `PRODUCT_ALIASES` |
| 24 | `src/pages/AdminGenerateAccess.tsx` | Desplegable |
| 25 | `src/data/use-cases-content.es.ts` | `productIds` de `chocolateria` y `cafeteria-brunch` |
| 26 | `footerLinks` cruzados | Desde `guia-chocolateria-obrador.ts`, `pack-appcc.ts`, `kit-escandallos.ts`, `plan-negocio-food-truck.ts` (hoy `:279-285`), `plan-negocio-cafeteria.ts`; y la FAQ `:286`/`:349` de la hermana con enlace |
| 27 | Imágenes | 6 de galería + OG + fondos, skill `generate-images` |
| 28 | `astro-site/public/dl/guia-churreria-chocolateria/**` | Guía PDF+DOCX, bonus, business plan, 9 xlsx |
| 29 | Blog | `fase8x-sustituir-banner.py` + corrección de cifras del post (decisión 5) |
| 30 | Resend | Borrador con sufijo «— PROGRAMAR 13-nov» |
| Gates | `nombre-gate.py`, `paginas-gate.py --only …`, `gate-no-latinos.py`, `censo-entregables.py --fail`, `robots-gate.py`, `whatsapp-gate.py`, `miselup-gate.py`, `hub-gate.py`, `gate-flujo-postpago.py` (E-f cripto), `datafast-gate.py`, `fase8d-faq-duplicadas.py` sobre el post | |

---

## 4. Propuesta de entregables

### 4.1 Paquete y caso central

- **Caso central (a):** churrería-chocolatería de local fijo con obrador de masa y consumo en sala/terraza. **Columnas de escenario:** (b) despacho/para llevar, (c) caseta de feria, (d) franquicia. **Epígrafe + remisión:** (e) churros dentro de una cafetería. **Fuera:** (f) obrador B2B. Coincide con L1 Parte C-1.
- **Paquete de familia:** guía PDF+DOCX (20 capítulos + anexo) · bonus 1 business plan modelo relleno (DOCX) · bonus 2 «12 decisiones de apertura» (PDF+DOCX) · **9 libros de Excel**. Mismo formato que Pastelería y Chocolatería; la plantilla de dashboard se calca.

### 4.2 Los 9 libros (nombres propuestos para firmar antes del guion, D49)

Convención: **E** = entradas verdes · **S** = salidas por fórmula · **C** = cruce con otro libro (celda verde «cópialo del libro N» + fila de cuadre) · **H/N** = hereda estructura de la hermana / nuevo.

| # | Fichero | Hojas | E (verde) | S (fórmula) | Decisión que permite tomar | Dolor o norma · frontera |
|---|---|---|---|---|---|---|
| 1 | `produccion-hora-punta-y-local.xlsx` (H: libro 1) | Instrucciones · Parámetros · Equipos y Capacidad · Demanda por Franja · Cuello de Botella · **Cola del Domingo** · Ficha de Visita a Local | kg de masa/h de la churrera o dosificadora, litros y carga por tanda de la freidora, minutos por tanda, piezas por kg de masa (C ← 3), raciones/hora por franja, personas en línea | raciones/hora que aguanta el conjunto; equipo que manda; tiempo de espera y longitud de cola en la hora pico (aritmética simple de llegadas menos servicio, sin funciones prohibidas); veredicto de la ficha (eliminatorios: humos a cubierta, gas, potencia, ruido) | ¿Una churrera o dos? ¿Ese local sirve? | Producción en pico y cola (encargo); sin fuente las capacidades de equipo → CUS. Frontera: no hay capacidad de fritura en ningún producto vivo |
| 2 | `calculadora-capex-churreria.xlsx` (H: libro 2 + hoja de equipamiento del libro 9) | Instrucciones · Parámetros · CAPEX por Bloque · **Equipamiento Línea a Línea** · Variante del Formato · Franquicia frente a Independiente · Traspaso vs Obra Nueva · IVA y Tesorería · Resumen | importe mín/máx/tuyo y base de IVA por línea; variante elegida; traspaso pedido y renta; fondo de maniobra (C ← 7) | CAPEX por bloque y total; extra por variante; comparación traspaso/obra a 5 años; IVA soportado a adelantar | ¿Cuánto necesito y en qué formato? | Bloques nuevos: extracción, filtros y conducto; freidoras/churreras; sala y terraza. Chocolatera 527 € (`CHS-46a`) reutilizada; traspasos `CHS-37a/b/c` como comparables directos; franquicias `CUS-M13…M24` (L1) con etiqueta D11. Frontera: el food truck cifra vehículo, aquí caseta |
| 3 | `carta-de-apertura-y-escandallo-churro.xlsx` (H: libro 4, N: masa) | Instrucciones · Parámetros · **Escandallo por kg de Masa** (churro y porra) · **Absorción de Aceite y Merma** · Chocolate a la Taza · Coste Hora · Ración vs Docena o Kilo · Mix y Ticket por Franja y Temporada · Decisión de Surtido | receta por kg de masa y precios de compra; g por pieza; % de absorción de aceite (verde, **sin fuente**); merma de rotos/sobrantes; precio del aceite (C ← 4); receta de la taza; PVP con IVA; mix de invierno y de verano | coste por pieza, ración, docena y kg; coste por taza; **margen bruto y margen tras aceite y mano de obra** en la misma hoja (resuelve `CHS-31`); ticket medio por franja; margen € × rotación | ¿A cuánto vendo la ración, la docena y la taza? | Margen bruto vs neto (L1 B2-3); denominación del chocolate a la taza si se vende envasado (`CHN-05`). Frontera: ni Kit Escandallos ni Food Cost costean masa frita |
| 4 | `aceite-de-fritura-coste-y-cambio.xlsx` (N; reusa «Escenarios de Precio» del libro 3 hermana) | Instrucciones · Parámetros · Consumo y Reposición · Punto Económico de Cambio · Comparativa de Aceites · Escenarios de Precio del Aceite y la Harina · Gestor de Aceite Usado | capacidad de cuba (L), reposición diaria (L), kg de masa frita/día (C ← 1), días entre cambios **según tu registro** (C ← Pack APPCC), precio por litro de cada aceite, % de subida a simular | € de aceite por ración y por mes; litros a gestor al mes; coste anual por tipo de aceite; impacto de la subida en el margen | ¿Qué aceite compro y cuánto me cuesta cambiarlo? | Calidad del aceite y gestor (encargo); umbrales citados de `pack-appcc/09` (R4/R5). **No es registro APPCC** |
| 5 | `franjas-y-temporada-del-ano.xlsx` (H: libro 6) | Instrucciones · Parámetros · Peso sobre el Año · Franjas del Día · Capacidad contra el Pico (C ← 1) · Refuerzo y Tesorería · **El Verano: Cerrar, Carta de Verano o Ferias** | 12 coeficientes (supuestos declarados: no hay reparto mensual publicado), % de venta por franja, días de apertura, refuerzos | ventas por mes y por día de apertura; déficit de capacidad en domingos y Navidad-Reyes; resultado de julio-agosto en las tres salidas | ¿Cierro en verano? ¿Cuánta gente meto el domingo? | Estacionalidad oct-mar e invertida en feria (L1 B2-4); sin fuente la curva → supuesto |
| 6 | `ferias-y-venta-ambulante.xlsx` (N) | Instrucciones · Parámetros · Calendario de Ferias · **Punto Muerto por Evento** · Producción por Evento (C ← 1, ← 3) · Autorizaciones por Evento · Resumen de Temporada | por evento: días, horas, tasa o canon (€/m²·día o fijo), m² de caseta, desplazamiento, montaje, personal, afluencia estimada, ticket | raciones para cubrir el evento; resultado por evento; ranking de eventos; resultado de la temporada | ¿A qué ferias voy y a cuáles no? | Ferias y vía pública (L1 B2-7: tasas por m²/día, sin municipio identificado) → normativa de venta no sedentaria **sin fuente** (CUN). Frontera R6/R7 |
| 7 | `plan-financiero-3-anos-churreria.xlsx` (H: libro 7, motor `planes-v2_0` 2.2) | 0. Supuestos · Inversión Inicial (C ← 2) · PyG 3 Años · Punto de Equilibrio · Escenarios · Personal (C ← 9) · Tesorería 12 meses (C ← 5) · Financiación · **Canales y Punto Muerto** (sala · para llevar · ferias C ← 6) · Instrucciones | clientes/día, ticket sin IVA, días, rampa, IVA por canal (10 % en sala `CHN-71c`; para llevar **sin fuente**) | P&L, punto muerto mensual y diario, tesorería con valle de verano, DSCR | ¿Aguanta el banco? ¿Qué canal paga los fijos? | Veredictos por **euros, no por ratio** (§1.4-1); con columna de escenario «local fijo / despacho» como la hermana hizo con «taza y churros» |
| 8 | `checklist-legal-fritura-y-licencias.xlsx` (H: libro 8, N: fritura) | Instrucciones · Checklist Legal (F1-F6) · **Árbol IAE y CNAE por Modelo** · Licencia y Humos · Árbol de Registro Sanitario · Venta Ambulante y Ferias · Terraza y Horario · Alérgenos y Aceite Compartido · PRL de la Fritura · Registro de Formación · Cronograma y Ruta Crítica | estado, coste previsto/real, fechas; respuestas del árbol (¿consumo en local? ¿para llevar? ¿ferias? ¿suministras a otros?) | contador por fase; veredicto de epígrafe (644.6 / grupo de la 67 / ambos); ruta crítica en meses | ¿Qué papel me toca y en qué orden? | 644.6 y 676 (`CHN-49b/49c/72`), gas (`CHN-48`), formación (`CHN-69`), Ley 1/2025 con mesas (`CHN-92`), alérgenos (`CHN-33`, `CHN-34b`). **Sin fuente:** humos/actividad calificada, norma del aceite, acrilamida (Rgto. (UE) 2017/2158), venta no sedentaria, terrazas, extintor clase F → CUN |
| 9 | `turnos-plantilla-y-madrugada.xlsx` (N) | Instrucciones · Parámetros · Cuadrante por Franja · Horas y Nocturnidad · Coste de Plantilla · Convenio: Cómo Identificar el Tuyo · Riesgos del Puesto | grupo y salario del convenio del lector, horas por franja, plus de nocturnidad (**sin fuente**), jornadas | coste anual por puesto y total (→ libro 7); horas del titular; huecos de cobertura | ¿Cuánta gente necesito y cuánto me cuesta abrir de madrugada? | Dolores 1-2 de L1 (madrugón, personal); convenio (`CHN-66/93` como método; hostelería **sin fuente**). **Palanca:** se puede absorber en `7!Personal` (§5) |

**Reglas de construcción heredadas que aplican a los nueve:** prohibidas INDIRECT, COUNTA, PMT, OFFSET, XLOOKUP, LET, LAMBDA y referencias entre libros; cero constantes en fórmulas (el 180 °C y el 25 % de `pack-appcc/09` **sí** están dentro de su fórmula `F5` — no copiar ese patrón); parámetros en verde con nota y fecha; listas de validación contra rango (`_comun_chocolateria.py:dv_rango`); `barrer_cp1252` y `gate_sum_rango`; tildes en las tablas que salen de los datos (C16); coma decimal; ninguna celda con salto de línea si viaja a una tabla del PDF (C1).

### 4.3 Índice propuesto (20 capítulos + anexo)

| Cap | Tema | H/N | Libro que lo sostiene |
|---|---|---|---|
| 01 | Qué negocio estás montando: las seis variantes y cuál te toca (con «la bombonería es OTRO negocio», espejo de D1) | H | 2 |
| 02 | El cliente, las franjas y la plaza | H | 5 |
| 03 | La carta de apertura: churro, porra, chocolate a la taza y para llevar | H | 3 |
| 04 | Cuánto cuesta abrir, partida a partida | H | 2 |
| 05 | El local: metros, zonas y la ficha de visita | H | 1 |
| 06 | Antes de firmar: la freidora cambia la conversación de la licencia (inverso del cap. 06 hermano) | N | 8 |
| 07 | Humos, extracción, filtros y ruido: qué preguntar al instalador | N | 1, 8 |
| 08 | Maquinaria: churrera, dosificadora, freidora y chocolatera | H | 2 |
| 09 | Producción en hora punta: la cola del domingo | N | 1 |
| 10 | Licencias, sanidad y registro, con el epígrafe de cada modelo | H | 8 |
| 11 | Aceite de fritura: calidad, cambio, coste y gestor | N | 4 |
| 12 | Acrilamida, alérgenos y el aceite compartido | N | 8 |
| 13 | Autocontrol, formación y el día de la inspección | H | 8 |
| 14 | Escandallo del churro y de la porra: rendimiento, absorción y los dos márgenes | H+N | 3 |
| 15 | Proveedores: harina, aceite, chocolate y envase | H | 2 |
| 16 | El equipo, los turnos y la madrugada | H+N | 9 |
| 17 | La temporada: de octubre a marzo, y qué haces en verano | H | 5 |
| 18 | Ferias, casetas y venta ambulante | N | 6 |
| 19 | Franquicia o independiente | N | 2 |
| 20 | El plan financiero, el punto de equilibrio y los primeros noventa días | H | 7 |
| A | Anexo normativo con fecha de revisión | H | — |

**11 H/H+N · 8 N** (+ anexo). Las H reutilizan guion, `puntos_por_epigrafe` y tablas de la hermana cambiando datos; las N necesitan guion desde cero.

**Bonus:** se mantiene el par de familia (business plan modelo + «12 decisiones de apertura»): mismo pipeline, cero desarrollo nuevo, y la refutación de la hermana ya dejó las trampas del bonus a la vista (B8/B9/B22/B23/C20/C30). Alternativa descartada: un «plan de ferias de la primera temporada» como bonus — duplicaría el libro 6.

### 4.4 Juego de datos único (para `datos_ejemplo.py`)

| Campo | Propuesta | Fuente |
|---|---|---|
| Nombre | «Churrería-Chocolatería La Rueda» (paralelo a La Encina / La Clara / La Almendra). **Comprobar en la OEPM antes de cerrar** (D51); evitar marcas de L1: Valor, Maestro Churrero, Churros Factory, Madrid1883, Pinocho, Tejeringo's, Kukuchurro, ChurroFácil, Porfirio, San Ginés | supuesto |
| Ciudad | Ciudad media española sin nombre (el lector pone la suya) | patrón de familia |
| Superficie | **75 m²** | convergencia con `CHS-37a` (75 m²) y `CHS-37b` (74 m²), los comparables directos que la hermana usó como «otro formato» |
| Renta | 910 €/mes como referencia observada | `CHS-37b` |
| Formato | obrador de masa a la vista + barra + sala + terraza; despacho a calle | supuesto |
| Horario | mañana y tarde a diario; madrugada de viernes a domingo y festivos | supuesto (L1 B2-1 da el patrón, no la cifra) |
| Plantilla | titular + churreros/as + sala, con refuerzo en domingos y Navidad-Reyes | supuesto; coste del convenio que decida la lente normativa |
| Carta | **22 referencias en 5 familias**: churros y porras (ración, docena, kilo) · rellenos · chocolate a la taza (taza, para llevar) · bebidas calientes y frías · para llevar y encargos | PVP de referencia `CHS-32` donde exista; el resto supuesto |
| Variante feria | una caseta, temporada de verano y fiestas locales, nº de eventos supuesto | supuesto |
| Margen del churro | los dos de `CHS-31`, con la explicación | `CHS-31` |

---

## 5. Presupuesto y riesgos de pipeline

### 5.1 Base de cálculo

- Coste real de la hermana: **≈16 M solo en F2+F3** (redactores 7,3 · capa de producto 1,6 · refutación r1 2,3 · r2 2,9 · fixer final) más una F1 de 5 rondas de SPEC (`CALENDARIO-V2-SEMANAL.md:397-398`). Redactores 7,3 M / 40 bloques (D50) = **≈0,18 M por bloque real**, frente a 0,1125 M estimados (SPEC hermana §9).
- Generadores de la hermana: **9 `gen_*.py` = 18.424 líneas** + 5 `_comun_*.py` = 1.773 + `gate_libros.py` 369 + `verificar_guion.py` 406 (`wc -l`, 2026-10-03). Guion: 5.629 líneas.
- Techo L: **≤10 M** (F1 2 · F2 6 · F3 2) y parada si se pasa un 30 % (`CALENDARIO-V2-SEMANAL.md:390-398`).

### 5.2 Estimación por fase (M de tokens de subagentes)

| Fase | Partida | Hipótesis | M |
|---|---|---|---|
| F1 | 5 lentes de research | en curso | 1,10-1,30 |
| F1 | Verificación legal del delta `CUN-*` | solo lo nuevo (fritura, aceite, acrilamida, 644.6, venta no sedentaria, terrazas, PRL, convenio); lo demás por id `CHN-*` | 0,30 |
| F1 | SPEC + refutación (≤2 rondas) | molde de la hermana | 0,35 |
| F1 | `datos_ejemplo.py` + guion | 11 caps H reusando el guion de la hermana; 8 N desde cero | 0,55 |
| | **Subtotal F1** | | **2,30-2,50** ⚠️ +15-25 % sobre 2 M |
| F2 | 9 libros | 6 heredan molde a ≈0,20; 3 nuevos (4, 6, 9) a ≈0,28 | 2,05 |
| F2 | Refutación de xlsx | gates de script primero, 1 refutador opus + verificador sonnet | 0,45 |
| F2 | Redactores | **30 bloques** frente a los 40 de la hermana (D50: 6 caps a 2, 14 a 1, anexo 1, bonus 2 = 12, bonus 1 = 1): aquí 09 y 14 a 2, los otros 18 a 1, anexo 1, **bonus 2 en 6 bloques (dos decisiones por bloque)**, bonus 1 en 1 → 30 × 0,12-0,15 | 3,60-4,50 |
| F2 | Refutación de documentos (r1 + r2 verificadores) | sin fixer final aparte | 1,00 |
| | **Subtotal F2** | | **7,10-8,00** ⚠️ +18-33 % |
| F3 | Capa de producto calcada por Sonnet + gates + Resend + banners | lista §3.5 | 1,10-1,40 |
| | **TOTAL** | | **10,5-11,9** (dentro del +30 % = 13 M; fuera del techo nominal de 10 M) |

**Palancas, con su coste honesto:**
1. **Absorber el libro 9 en `7!Personal`** (−0,25 M entre libro, refutación y bloque): el cuadrante de madrugada vive como hoja del plan. Coste: pierde el libro más pegado al dolor nº 1 de L1.
2. **Anexo normativo heredado**: las normas comunes (Ley 12/2012, IAE, IVA, Ley 1/2025, 852/2004, 1169/2011, CNAE-2025, gas) ya están redactadas y verificadas en la hermana; reescribir solo el delta (−0,15 M).
3. **Bloques de redacción con puntos de la hermana**: en los 11 capítulos H, `puntos_por_epigrafe` se calca y se cambian datos (es lo que baja el 0,18 M/bloque real hacia 0,12).
4. **No** se recomienda bajar de 20 capítulos ni de 12 decisiones: es lo que sostiene el precio de familia de 65 €.

### 5.3 Reutilización concreta que baja el coste

| Pieza | Cómo |
|---|---|
| `_comun_chocolateria.py` | Copiar a `_comun_churreria.py`: `VERSION_LINE` propio, `dv_rango`, `barrer_cp1252`, `gate_sum_rango`, `cabecera/seccion/nota/pie` sin cambios |
| `_comun_libro_7.py` + `gen_plan-financiero-3-anos-chocolateria.py` (3.899 líneas) | Molde del libro 7 con el motor 2.2; cambiar canales y escenario de formato |
| `gen_calculadora-capex-chocolateria.py` (2.059) | Molde del libro 2, incluida la hoja «Variante del Formato» y la de franquicia |
| `gen_capacidad-obrador-y-clima.py` (2.102) | Molde del libro 1 sin la hoja de clima |
| `gen_campanas-y-valle-del-ano.py` (1.387) | Molde del libro 5 |
| `gen_checklist-legal-licencias-y-cacao.py` (2.568) | F1-F6, Árbol, Registro de Formación, Cronograma; fuera Cadmio, EUDR y Ruta Doméstica |
| `gen_carta-de-apertura-y-escandallo-chocolate.py` (1.868) | Coste Hora, Mix, Decisión de Surtido |
| `gate_libros.py`, `verificar_guion.py`, `dump_prompts.py`, `check_bloque.py`, `documentos.py` | Tal cual |
| `guia-chocolateria-json-merge.py` | Fusión `CUN-*`/`CUS-*` al JSON común con gate de recuento |

### 5.4 Trampas ya documentadas que hay que blindar con gate, no con atención

1. Constantes de Python impresas literales en el PDF (A13/C9 de la refutación de documentos de la hermana) → grep de `F_[A-Z_]+` en `txt/` antes de ensamblar.
2. Saltos de línea dentro de celdas que viajan a tabla Markdown (C1).
3. Bases de IVA mezcladas en una misma comparación (C10, B18, B24); precios «desde» publicados como cerrados (A14, B7).
4. Veredictos que comparan ratios cuando la pregunta es en euros (§1.4-1, nuevo).
5. Dos cifras para el mismo concepto entre guía y bonus (B22/C20) → «un concepto = una fuente».
6. Parser del catálogo que pierde entradas si hay comentarios entre `description: {` y `es:` (CLAUDE.md, catálogo del 30-ago).
7. Purga de `astro-site/.astro` al tocar frontmatter (FAQ del post).
8. `html_tabla` escapa enlaces dentro de celdas; espacio fino U+202F y guion U+2011 en los `.md` ensamblados (CLAUDE.md).
9. Los gates LIVE leen el registro del árbol LOCAL: `git pull` antes de fiarse (CLAUDE.md, 3 fases).
10. Térmica: F2 de tamaño L **en el VPS**, no en el Mac (política de 3 fases, `CALENDARIO-V2-SEMANAL.md:381`).
