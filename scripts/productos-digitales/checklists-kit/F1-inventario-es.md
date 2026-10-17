# Kit de Tareas Recurrentes v2.0 (ES) — inventario de F1 para Restaurant Checklists Kit Pro (EN)

> Sesión Claude Code, 17-oct-2026. Fuente = los **11 xlsx PUBLICADOS** de `astro-site/public/dl/kit-tareas/`
> (sha256 de cada uno en `censo_es.json`), nunca el generador (`kit-tareas-v2_0/`). El docx
> `guia-equivalencias-kit-tareas.docx` (ES↔LatAm) NO se replica: su papel lo hace el bonus común EN
> «US · UK · Canada · Australia Hospitality Equivalents Guide» (`dl/en-shared/`). Todos los recuentos salen de
> `extraer_textos.py` (`censo_es.json` + `textos_es.json`); `gate_f1.py` comprueba que las tablas §0 y §1 son las
> que genera el censo. Celdas citadas como `libro:Hoja!celda`. Los defectos heredados (§3) NO se corrigen aquí.

## 0. Totales del kit (censo)

| Libro | Hojas | Texto | Tareas | Fórmulas | Fx→hoja | DV | CF | Merges | Protegidas | Horas 24 h | °C | Fmt € | Textos € | Verdes | Desbloq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01-apertura-cierre | 7 | 581 | 111 | 12 | 0 | 6 | 6 | 53 | 6 | 64 | 6 | 0 | 0 | 777 | 1141 |
| 02-partidas-cocina | 4 | 306 | 57 | 6 | 0 | 3 | 3 | 25 | 3 | 35 | 6 | 0 | 0 | 396 | 569 |
| 03-tareas-manager | 5 | 427 | 81 | 8 | 0 | 4 | 4 | 38 | 4 | 15 | 0 | 0 | 0 | 560 | 831 |
| 04-tareas-perfiles | 6 | 382 | 68 | 10 | 0 | 5 | 5 | 40 | 5 | 28 | 0 | 0 | 0 | 525 | 746 |
| 05-tareas-semanales-mensuales | 5 | 366 | 63 | 8 | 0 | 4 | 4 | 44 | 4 | 0 | 1 | 0 | 0 | 490 | 692 |
| 06-eventos-festivos | 5 | 333 | 60 | 8 | 0 | 4 | 4 | 32 | 4 | 4 | 0 | 0 | 0 | 448 | 636 |
| 07-plantilla-personalizable | 4 | 130 | 0 | 6 | 0 | 3 | 3 | 24 | 3 | 0 | 0 | 0 | 0 | 381 | 477 |
| 08-apertura-cierre-negocio | 3 | 171 | 28 | 4 | 0 | 2 | 2 | 12 | 2 | 15 | 0 | 0 | 0 | 248 | 304 |
| 09-apertura-cierre-caja | 4 | 183 | 23 | 95 | 1 | 3 | 4 | 32 | 3 | 11 | 0 | 282 | 20 | 421 | 467 |
| BONUS-01-briefing-servicio | 2 | 45 | 0 | 0 | 0 | 0 | 0 | 6 | 1 | 0 | 0 | 0 | 0 | 20 | 20 |
| BONUS-02-calendario-anual-tareas | 2 | 130 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 20 | 112 |
| **Total** | **47** | **3054** | **491** | **157** | **1** | **34** | **35** | **308** | **36** | **172** | **13** | **282** | **20** | **4286** | **5995** |

Columnas: «Tareas» = filas con número en A y texto en B (las 491 que anuncia la landing ES); «Horas 24 h» = celdas
de TEXTO «07:00» (no son horas de Excel); «°C» y «Textos €» = celdas de texto que los citan; «Fmt €» = celdas con
formato `#,##0.00 €`; «Protegidas» = hojas protegidas sin contraseña.

Transversal (los 11 libros):
- **Libro de texto, no de cálculo.** 3.054 celdas de texto frente a 157 fórmulas. En 01-08 las únicas fórmulas
  son el contador de cada checklist (`=COUNTIFS(B5:Bn,"?*",F5:Fn,"✓")` de `=COUNTIF(B5:Bn,"?*")-COUNTIF(F5:Fn,"N/A")`)
  y la única CF pinta la fila al marcar ✓ (`$F5="✓"`). El 09 lleva el recuento por denominaciones
  (`=B27*500`… 15 multiplicadores), el resumen de cierre y el registro mensual (fórmula con hoja:
  `'Apertura de Caja'!C23`, la única de todo el kit) y 2 CF `cellIs` (descuadre ≠ 0 en ámbar). B01 y B02 no tienen
  fórmulas.
- **Sin gráficos, imágenes, comentarios ni nombres definidos.** 36 hojas protegidas SIN contraseña (todas las de
  trabajo); las 11 `Instrucciones`, no. 47 áreas de impresión, 35 títulos de impresión (fila 4) y 35 paneles (`A5`).
  Papel **A4 (`paperSize 9`) en las 47** (41 verticales y 6 apaisadas, todas ajustadas a 1 página de ancho); pie `AI Chef Pro · aichef.pro ·
  Página &P de &N`; línea de marca `— Kit de Tareas Recurrentes · Restaurante Casual · AI Chef Pro · aichef.pro` al
  pie de cada hoja e Instrucciones.
- **DV**: 33 listas `"✓,—,N/A"` (una por checklist; ✓ y — sin letras, N/A igual en inglés) + 1 de número entero
  (09 recuento, `B27:B42`). Mensajes: «Marca no válida» (33) y «Cantidad no válida». Literales de fórmula: `?*`,
  `✓`, `N/A`, `>0`, `<0` → `mapas.CLAVES` = {N/A}: **ningún literal cambia y ninguna CF cambia de color**.
- **Verdes = editables**: 4.286 celdas verdes (`E8F5E9`), todas desbloqueadas; hay además 1.709 desbloqueadas sin
  verde: las columnas A (nº) y B (tarea) de las filas de tareas, las filas separadoras y la tabla del B02 (el
  cliente puede reescribir sus tareas). La F2 conserva el mismo mapa celda a celda.
- docProps iguales en los 11 salvo el título («título — Restaurante Casual · Kit de Tareas Recurrentes Pro»):
  `subject` «Kit de Tareas Recurrentes Pro · v2.0», `keywords` «kit tareas, AI Chef Pro», `description`
  «aichef.pro/kit-tareas», `category` «AI Chef Pro · Productos digitales». Versión en las 11 Instrucciones:
  «Versión 2.0 · agosto 2026 · aichef.pro/kit-tareas · info@aichef.pro»; firma de autor «Diseñado por John
  Guerrero — chef y consultor gastronómico desde 2010, en cocina desde los 17 años · johnguerrero.es».
- **Bloque «Se conecta con»** repetido en los 11 (cita 08, 01 y 09 por nombre de fichero, «Orden de uso: local →
  áreas → caja») + una línea «Estás en NN-…xlsx» propia de cada libro: 48 citas a ficheros, 18 cadenas.
- **Datos de ejemplo: ninguno.** Las tareas, zonas, responsables y horas límite son el contenido del producto.

## 1. Lo que depende de España (censo) y su destino

| Dependencia de España | Apariciones | Cadenas | Destino |
|---|---|---|---|
| Temperaturas en °C | 13 | 13 | D10: °F + FDA Food Code (ADAPTAR o POR_CELDA) |
| Horas de 24 h como celda («07:00») | 172 | 22 | D9: `mapas.hora_us` (regenerar) |
| Horas de 24 h dentro de una frase | 1 | 1 | D9: el traductor, reloj de 12 h |
| Euros (€) en textos | 20 | 20 | D12-D13: dólares en la tabla de caja; sin símbolo en el resto |
| Caja española: TPV, datáfono, Bizum, arqueo, descuadre | 45 | 34 | D12: POS, card terminal, Z/X report, starting bank, over/short, propinas fuera |
| APPCC y «Pack APPCC» | 3 | 3 | D10: HACCP · «HACCP Food Safety Kit Pro» |
| Normativa y administración española | 27 | 26 | D10-D11: FDA Food Code, OSHA, NFPA 96, EPA 608, FLSA, normas locales (POR_CELDA / ADAPTAR) |
| Festivos y costumbres españolas | 27 | 27 | D14: calendario US (`mapas.CALENDARIO`) y ADAPTAR en 06 «Christmas & NYE» |
| Terraza y temporada alta | 46 | 25 | D15: patio / patio season (Memorial Day–Labor Day) |
| Puestos y zonas de la hostelería española (celda entera) | 972 | 51 | D8: `mapas.GLOSARIO` (line cook, prep cook, server, porter, MOD…) |
| Plataformas españolas | 2 | 2 | D16: Google, Yelp, TripAdvisor; Google Business Profile |
| Alérgenos (UE 14) | 8 | 8 | D10: 9 alérgenos US; nota UK 14 |
| Papel A4 citado | 1 | 1 | D17: US Letter |
| Sufijo de variante «Restaurante Casual» | 60 | 14 | D2: la EN no lleva sufijo |
| Citas a ficheros ES (.xlsx) | 48 | 18 | D5: nombre de fichero EN (`mapas.FICHEROS`) |
| Menús de Excel en español | 19 | 3 | Excel EN: «Review → Unprotect Sheet», «right-click → Insert», «Move or Copy» |
| Formatos de número con € | 282 | — | D13: `#,##0.00` |
| Hojas en A4 (paperSize 9) | 47 | — | D17: US Letter (paperSize 1) |

Detalle por libro (lo que la EN cambia además de traducir; celdas exactas en `mapas.POR_CELDA` y `mapas.ADAPTAR`):

| Libro | Mercado español → destino EN |
|---|---|
| 01 | Cámaras 0-4 °C / ≤ −18 °C (`Apertura Cocina!B18,B21:B23`, `Cierre Cocina!B12`) → 41 °F / 0 °F; «Pack APPCC» (`B24`) → HACCP Food Safety Kit Pro; joyas «sin anillos» (`B7`) → FDA 2-303.11 (anillo liso sí); síntomas (`B10`) → FDA 2-201.11; olor a gas (`B14`) → salir y llamar a la compañía o al 911; etiquetar y fechar (`Cierre Cocina!B6`) → date marking 7 días; carta de alérgenos (`Apertura Sala!B12`) → 9 alérgenos US; ceniceros de terraza (`B19`) → solo si la ciudad lo permite; TPV/datáfono → POS / card terminal; 64 horas de 24 h |
| 02 | Caliente ≥ 65 °C (`Calientes!B20`) → 135 °F; aceite < 40 °C y «gestor autorizado» (`B27`) → 104 °F y reciclador; lejía 70 ppm (`Fríos!B6`) → FDA 3-302.15; anisakis −20 °C 24 h (`Fríos!B10`, `Mise en Place!B10`, norma UE) → **FDA 3-402.11: −4 °F 7 días** o −31 °F + 15 h, registro 90 días; ostras: etiquetas 90 días; vitrina ≤ 4 / < 8 °C (`Fríos!B17`, RD 3484/2000) → 41 °F para todo TCS; helado −18 → −12 °C (`Mise en Place!B28`) → 0 °F → 10 °F |
| 03 | Registro diario de jornada (`Diario Manager!B35`) → fichajes en POS/app; «conservarlos 4 años» (`Mensual Manager!B16`, art. 34.9 ET) → FLSA 2 años fichajes / 3 nóminas; nóminas y variables (`B18`) → payroll con propinas; extintores (`B23`) → OSHA mensual; Google/TripAdvisor (`Diario!B29`) → + Yelp; Google Maps (`Mensual!B30`) → Google Business Profile; «Pack APPCC» (`Semanal!B26`) |
| 04 | Puestos ES (pestañas y columna D) → server, bartender, head chef, FOH manager; «cuenta nunca antes» (`Camarero!B20`) → costumbre US; barman → bartender |
| 05 | **«Trimestral y Anual» entera** (`B6:B24`, `D`, `E`): DDD, campana por empresa homologada, extintores y BIE, retimbrado 5 años, gas cada 5 años, frigorista, legionela, analítica de agua, gestor de aceite, punto limpio, póliza, Verifactu → plagas (PCO), NFPA 96 (campana y sistema de extinción cada 6 meses), OSHA 1910.157, gas según código local, EPA 608, backflow, separador de grasas (FOG), reciclador de aceite, residuos, seguros US, POS + sales tax; tabla de congelación a −18 °C (`FIFO Semanal!A37`) → 0 °F (USDA: seguro indefinidamente, tiempos de calidad); TPV y datáfono (`Mantenimiento!B18`); «Pack APPCC» (`Instrucciones!B8`) |
| 06 | Navidad y Nochevieja (`Navidad!B8,B17,B21:B23`: turrón, cordero, cava, uvas, campanadas, cotillón) → prime rib, champán, party favors, brindis a medianoche solo 21+; licencia de terraza al Ayuntamiento (`Temporada Terraza!B6`) → outdoor dining permit; horas «18:00 … 00:00» |
| 07 | «Imprime en A4» (`Instrucciones!B21`); «click derecho → 'Mover o copiar'»; puestos de las plantillas en blanco |
| 08 | Persianas (`Apertura del Negocio!B8`) → security gate; TPV / POS / datáfono; 15 horas de 24 h |
| 09 | **Caja en euros**: 15 denominaciones (`Cierre de Caja!A27:A42` + fórmulas `C27:C42`) → billetes y monedas de EE. UU. con cartuchos; rótulos «(€)»; Visa/MC, Bizum, vales, invitaciones → card sales sin propinas, other tenders + propinas pagadas en efectivo; Z del TPV, X de apertura, descuadre → POS Z report, X report, over/short; «Fecha» con días 1-31 (`Registro Mensual!A4`) → Day; nota de `A37` con «100 €» |
| B01 | «☐ Comida ☐ Cena» → Lunch / Dinner; briefing → pre-shift meeting (line-up); celíaco → gluten-free / celiac |
| B02 | **22 fechas españolas** (`Calendario Anual!A5:D26`: Reyes, Carnaval, 19-mar Día del Padre, Semana Santa, comuniones, 1-may, 1.er domingo Día de la Madre, San Juan, 15-ago, Todos los Santos, puente de diciembre, Nochevieja con uvas) → calendario US de `mapas.CALENDARIO` (Super Bowl, St. Patrick's, Easter, Cinco de Mayo, Mother's Day 2.º domingo, Memorial Day, Father's Day, 4 de julio, Labor Day, Thanksgiving, gift cards, NYE); nota UK (Mothering Sunday, bank holidays, Boxing Day) |

## 2. Lo que la EN hereda tal cual

- Toda la estructura: 47 hojas, rangos, 308 merges, áreas e impresión, paneles, anchos, colores, verdes,
  desbloqueadas, protección sin contraseña, las 34 DV y las 35 CF, los contadores y las 491 tareas en el mismo orden
  y en las mismas filas (las de festivos y servicios contratados cambian de contenido, no de sitio).
- Las 15 filas del recuento de caja, el resumen de cierre y el registro mensual con sus fórmulas (solo cambian los 15
  multiplicadores de `C27:C42`); la lógica «el fondo es un saldo» (media, no suma) y el descuadre acumulado en valor
  absoluto.
- La tabla de vida útil en congelación (mismas cifras: son de calidad y quedan por debajo o en línea con la USDA
  FoodKeeper), el briefing, las tres plantillas en blanco y el calendario como herramienta.

## 3. Defectos heredados (no se tocan aquí)

- **I1 · «Fecha» con días 1-31** (09 `Registro Mensual!A4`, `A5:A35`): la cabecera dice «Fecha» y la columna lleva el
  número de día. EN: «Day» (`POR_CELDA`). ES: proponer «Día» en su próxima v2.x.
- **I2 · «click derecho» frente a «clic derecho»** (07 `Instrucciones!B13`; el resto del kit dice «clic»). Cosmético.
- Observación (no es defecto): el anisakis a −20 °C 24 h es la regla de la UE (Reglamento 853/2004) y es correcta en
  el ES; en EE. UU. la regla es otra (FDA 3-402.11) y la EN la cambia (D10).

## 4. Jerga profesional (US, notas UK) — fuente

Fijada en `mapas.GLOSARIO` (celdas cortas) y añadida a `GLOSARIO-JERGA-ES-EN.md` (sección «Checklists de cocina, sala
y caja»). US por defecto; UK solo en notas (B02, 09, FAQ de la landing).

| ES | US | UK (nota) | Fuente |
|---|---|---|---|
| sala / comedor · terraza | front of house (FOH) / dining room · patio | — · terrace / beer garden | uso común (por verificar) |
| camarero · ayudante · barman · encargado | server · busser · bartender · shift manager / MOD | waiter · — · bartender · duty manager | uso común |
| chef de partida · cocinero · auxiliar · limpieza | lead line cook · line cook · prep cook · porter | chef de partie · commis · kitchen porter (KP) | uso común |
| partida · comanda · pase · «86» | station · ticket · the pass / expo · 86 | section · check · pass · 86 | uso común |
| cámara · baño maría · plancha · campana | walk-in cooler/freezer · steam table · flat-top · hood | walk-in · bain-marie · plancha · canopy | uso común |
| tareas de apoyo del camarero | side work (590/mes) | side duties | DataForSEO US, 17-oct |
| briefing | pre-shift meeting / line-up | briefing | uso común |
| fondo de caja · cajón · arqueo | starting bank · cash drawer · cash count / cash-out | float · till · cashing up | uso común |
| TPV · datáfono · lectura Z · descuadre | POS · card terminal · Z report · over/short | EPOS · card machine · Z read · over/under | uso común |
| firma de cada tarea | initials | initials | uso común |
| etiquetar y fechar | date marking (7 días, 41 °F) | use-by labelling | FDA Food Code 2022 §3-501.17 |
| frío / caliente | 41 °F / 135 °F | 8 °C / 63 °C | FDA Food Code §3-501.16; Food Safety and Hygiene (England) Regs 2013 |
| alérgenos | 9 major allergens | 14 allergens | FALCPA + FASTER Act; Food Information Regs 2014 |
| registro de jornada | time-clock punches / records | working time records | 29 CFR 516.6 |

## 5. Research (una pasada, 17-oct-2026) — solo lo que el producto afirma

- **Demanda** (DataForSEO, dada por el orquestador): US restaurant opening checklist 260 (MEDIUM) · restaurant cleaning
  checklist 260 (HIGH) · kitchen checklist 210 · restaurant checklist(s) 140 · restaurant closing checklist 90 ·
  restaurant/commercial kitchen cleaning checklist 90+90 · restaurant cleaning schedule 70 · opening and closing 50 ·
  daily checklist 40 · side work 590 · side work checklist 30 · bartender opening checklist 20. UK: kitchen cleaning
  checklist 260 (intención doméstica, regla 4 del glosario) · kitchen cleaning schedule 140 · kitchen checklist 110.
  SERP de «restaurant opening checklist»: AI Overview e intención mixta (abrir un restaurante vs. apertura diaria);
  relacionadas «pdf», «template», «printable», «Excel free download».
- **FDA Food Code 3-402.11** (parásitos): −20 °C/−4 °F 168 h, −35 °C/−31 °F hasta sólido + 15 h, o −35 °C sólido +
  −20 °C 24 h; exentos moluscos, ciertos atunes y acuicultura con pienso; registros 90 días (3-402.12). Fuentes:
  law.cornell.edu (16 Del. Admin. Code § 3-402.11), Maricopa County, Southern Nevada Health District.
- **Centavo**: último penny de circulación acuñado el 12-nov-2025 (Filadelfia); sigue siendo de curso legal. Fuente:
  coinworld.com «Final cent for circulation struck at Philadelphia Mint».
- **NFPA 96, tabla 11.4** (limpieza de campana): mensual combustible sólido · trimestral alto volumen (24 h,
  charbroil, wok) · semestral moderado · anual bajo. Fuentes: Village of New Paltz, CaptiveAire, Marysville FD.
- **OSHA 29 CFR 1910.157(e)**: inspección visual mensual (e)(2), mantenimiento anual registrado (e)(3), mantenimiento
  de 6 años en polvo de 12 años (e)(4); pruebas hidrostáticas en la tabla L-1 (no se publica un intervalo por tipo:
  «on the date on their label»). Fuente: osha.gov/laws-regs/regulations/standardnumber/1910/1910.157.
- Sin verificar cita a cita (proporcionalidad): 41/135 °F, date marking, joyas, enfermos, lavamanos 100 °F, EPA 608,
  FLSA 516.5-516.6 y los festivos (fechas fijadas por ley: 5 U.S.C. 6103; 36 U.S.C. 109 y 117) son reglas estables ya
  usadas en los kits EN hermanos (HACCP, Staff) o de calendario.
