# Restaurant Checklists Kit Pro — SPEC (F1 · 17-oct-2026 · sesión Claude Code)

> Producto de la **Tienda internacional en inglés** (ola 2, el primero de la línea Tareas): la edición EN del **Kit de
> Tareas Recurrentes** (`kit-tareas`, 14 €, contenido v2.0, 9 plantillas + 2 bonus xlsx). Doc canónico:
> `TIENDA-INTERNACIONAL.md`. Molde: `staff-kit/` (circuito completo) y `haccp-kit/` (FDA, °F). Base:
> `F1-inventario-es.md`, `censo_es.json`, `textos_es.json` (de `extraer_textos.py`) y `mapas.py` (autotest + cruce con
> el censo, 0 errores). Esta SPEC **decide**; lo que no está aquí no se hace. Tamaño **S** ($19): techo 2,5 M tokens.

## 0. Reglas que mandan (John)

- **Duplicar el ES y adaptar, nunca reconstruir.** Mismos 11 libros, 47 hojas, rangos, merges, áreas, paneles,
  protección (sin contraseña), DV, CF y las 491 tareas en sus filas. Lo que el mercado US exige DENTRO de un
  entregable (°F, FDA, caja en dólares, festivos US, servicios contratados US) se aplica y se declara aquí (D9-D15).
- **Mercado: base US con notas UK** (TIENDA §1). Moneda sin símbolo salvo la tabla de billetes (D12), US Letter,
  reloj de 12 h. Sin fiscalidad añadida.
- Textos de producto con **subagentes Anthropic** (regla 1bis), nunca bridge.py. Landing = la ES replicada, testimonios
  traducidos tal cual con subtítulo de edición española, **sin** `aggregateRating` ni `review` (TIENDA §3.5).
- 🔴 **Sin precio tachado ni anclas** (John, 11-oct, FTC 16 CFR 233.1, PR #117): ni `priceOld`, ni «% off», ni «worth $X»,
  ni «launch price». Fórmula: «One-time payment · lifetime access · updates included» (como `restaurant-schedule-templates`).
- Proporcionalidad: research en una pasada (inventario §5), un implementador por fase, gates de script, una revisión
  final. Esta F1 ≈ 0,4 M tokens.

## 1. Decisiones

| D | Tema | Decisión | Estado |
|---|---|---|---|
| D1 | Slug | `restaurant-checklist-templates` → `/en/digital-products/restaurant-checklist-templates` (+ `/access`, `/library`). productId = slug; JWT `restaurant-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_RESTAURANT_CHECKLISTS_KIT`; ficheros en `dl/restaurant-checklist-templates/` | DECIDIDA |
| D2 | Nombre | **Restaurant Checklists Kit Pro** en landing, schema, dashboard, email, docProps, marca y versión. Title SEO = H1 (Forma B): «Restaurant Checklists Kit Pro: Opening, Closing & Cleaning Checklist Templates for Excel» («Cleaning» es legítimo: 05 trae la limpieza profunda semanal y el mantenimiento, y los cierres del 01 la diaria). La EN no lleva el sufijo de variante «— Restaurante Casual» (60 apariciones) | DECIDIDA |
| D3 | Precio | **$19 USD**, pago único, acceso de por vida; familia `kit-tareas` en `tienda.ts` con `en: {slug: 'restaurant-checklist-templates'}` (F3) | DECIDIDA |
| D4 | Sin anclas | `pricing` = `price: '$19'`, `heroNote` y `buyBoxNote` «One-time payment · lifetime access · updates included»; sin `priceOld`, `discountBadge` ni `bonusSaveLine`; `bonusTotalLabel` (obligatorio en `KitTareasPricing`) = «Everything included: 9 templates + 3 bonuses» | DECIDIDA |
| D5 | Ficheros y títulos | Tabla §2.1 (intención US). `Instructions!B2` = «NN · título» (`mapas.titulo_interior`); docProps `title` = título; cada cita de fichero en un texto = nombre EN (48 citas, `mapas.FICHEROS`) | DECIDIDA |
| D6 | Pestañas | Tabla §2.2. Pestañas y rótulos citados en los textos, entre comillas dobles rectas ("Kitchen Opening") | DECIDIDA |
| D7 | Fórmulas y CF | Contadores, CF `$F5="✓"`, DV `"✓,—,N/A"` y resumen de caja **idénticos** (`mapas.CLAVES` = {N/A}): nada cambia de color. Solo cambian las **15 fórmulas por celda** de la tabla de billetes (D12) y la referencia `'Apertura de Caja'!C23` por el renombrado | DECIDIDA |
| D8 | Glosario de celdas | `mapas.GLOSARIO` (123): cabeceras (Task · Area · Assigned to · Due by · When · ✓ Done · **Initials** · Frequency · Lead time), zonas (Kitchen, FOH, Bar, Patio, Office…), puestos US (line cook, lead line cook, prep cook, server, bartender, porter, shift manager, Cashier / MOD…) y cuándo (Close, Service, Shift change, días). 972 celdas de puesto/zona | DECIDIDA |
| D9 | Horas | Las **172 horas de 24 h** son TEXTO: `mapas.hora_us` («07:00» → «7:00 AM», «10:00-11:30» → «10:00–11:30 AM», «00:00» → «12:00 AM»). La única hora dentro de una frase (06 `Navidad!B20`) la escribe el traductor. Horarios iguales (encajan con el almuerzo US) | DECIDIDA |
| D10 | Seguridad alimentaria | °F + FDA Food Code 2022 (§3): 41 °F frío / 0 °F congelador / 135 °F caliente; **parásitos 3-402.11** (−4 °F 7 días o −31 °F + 15 h, registro 90 días; ostras: etiquetas 90 días) en `POR_CELDA`; joyas 2-303.11, enfermos 2-201.11, lavamanos 100 °F, date marking 7 días, lavado de vegetales 3-302.15, 9 alérgenos (UK 14) en `ADAPTAR`. «Pack APPCC» → **HACCP Food Safety Kit Pro** (enlace de venta cruzada). 13 celdas con °C | DECIDIDA |
| D11 | Mantenimiento y registros | 05 «Quarterly & Annual»: las 15 filas se quedan; 12 cambian de contenido (`POR_CELDA` B/D/E): pest control (PCO), campana NFPA 96, extintores OSHA 1910.157(e)(3), sistema de extinción de campana cada 6 meses, gas según código local, frío EPA 608, backflow, separador de grasas (FOG), reciclador de aceite, residuos, seguros US, POS + sales tax. 03 `B16`: fichajes 2 años / nóminas 3 (29 CFR 516). Extintores mensuales: OSHA (e)(2) | DECIDIDA |
| D12 | Caja US | Tabla `Cierre de Caja!A27:C42` en dólares (`mapas.DENOMINACIONES`): $100, $50, $20, $10, $5, $2, $1; $1 coin, 50¢, 25¢, 10¢, 5¢, 1¢ (sigue siendo de curso legal), «25¢ roll» ($10) y «10¢ roll» ($5), rótulos de ≤ 10 caracteres (ancho de la columna A); `$`/`¢` solo en esos rótulos (excepción declarada). **Propinas fuera de ventas**: «Card sales, excl. tips» y «Other tenders + card tips paid in cash» (si las propinas de tarjeta se pagan del cajón, el descuadre no las confunde con faltante). TPV → POS, datáfono → card terminal, Z/X del TPV → Z/X report, descuadre → OVER / SHORT, fondo → starting bank. Ronda 1: la Z que se teclea es «POS Z report: sales + tax, excl. tips» (ventas netas + sales tax, sin propinas) y «Net cash (counted − starting bank)» | DECIDIDA |
| D13 | Moneda | Los **282 formatos con €** → `#,##0.00`; los 20 textos con € → rótulos fijados o traductor («in your currency») | DECIDIDA |
| D14 | Festivos | BONUS-02: **22 fechas US** de `mapas.CALENDARIO` en las mismas 22 filas y orden por meses (Super Bowl, Valentine's, Mardi Gras, St. Patrick's, Easter, patio, graduaciones, Cinco de Mayo, Mother's Day 2.º domingo, Memorial Day, Father's Day, 4 de julio, verano, Labor Day, Halloween, Thanksgiving, gift cards, holiday parties, Navidad, NYE); A/B/D fijados, C con `ADAPTAR`. 06: «Valentine's Day» se queda; «Christmas & NYE» sin uvas, cava ni turrón (brindis 21+) | DECIDIDA |
| D15 | Terraza | terraza → **patio**; licencia → outdoor dining / sidewalk café permit; temporada alta → summer peak (Memorial Day–Labor Day); ceniceros solo donde se permita fumar | DECIDIDA |
| D16 | Plataformas | Google, **Yelp** y TripAdvisor; Google Maps → Google Business Profile | DECIDIDA |
| D17 | Papel | **US Letter** (`paperSize 1`) en las 47 hojas, misma orientación y ajuste; «Imprime en A4» → US Letter | DECIDIDA |
| D18 | UK · CA · AU | Sin entregables nuevos: FAQ de la landing, nota UK del B02 (Mothering Sunday, bank holidays, Boxing Day), nota del 09 (para libras, CAD o AUD se desprotege la hoja, sin contraseña, y se cambian rótulo y valor) y el bonus «US · UK · Canada · Australia Hospitality Equivalents Guide» (`dl/en-shared/`) | DECIDIDA |
| D19 | Marca y metadatos | Marca `mapas.MARCA_EN`; pie `mapas.FOOTER_EN`; versión «Version 2.0 · <mes> 2026 · aichef.pro/en/digital-products/restaurant-checklist-templates · info@aichef.pro»; docProps de `mapas.DOCPROPS_EN` | DECIDIDA |
| D20 | Landing | §6 (todas las secciones del ES, plantilla `KitTareasLandingPage` con `lang`) | DECIDIDA |
| D21 | Zona app | `…/access` con `ProductAccessGate`; `…/library` = copia traducida de `KitTareasDashboard.tsx` (11 descargas + bonus común); email EN | DECIDIDA |
| D22 | Máquina | VPS caído hoy: F2 en el **Mac en serie** (python de uno en uno, `istats cpu temp` < 62 °C antes de cada ejecución, esperar a < 60 °C); si vuelve el VPS, F2 allí (`staff-kit/F2-NOTAS.md` §2) | DECIDIDA |
| D23 | Defectos heredados | I1 («Fecha» con días) e I2 («click») de inventario §3: la EN nace corregida; en el ES se proponen para su próxima v2.x | PROPUESTA (ES) |

## 2. Mapas

### 2.1 Ficheros (D5)

| # | Fichero ES | Fichero EN | Título EN (landing, dashboard, B2, docProps) | Intención (US/mes) |
|---|---|---|---|---|
| 01 | `01-apertura-cierre.xlsx` | `01-opening-closing-checklists-kitchen-foh-bar.xlsx` | Opening & Closing Checklists: Kitchen, FOH & Bar | opening checklist 260 · closing 90 |
| 02 | `02-partidas-cocina.xlsx` | `02-kitchen-station-checklists.xlsx` | Kitchen Checklists by Station (Hot Line, Cold Station, Mise en Place) | kitchen checklist 210 |
| 03 | `03-tareas-manager.xlsx` | `03-restaurant-manager-checklist.xlsx` | Restaurant Manager Checklist: Daily, Weekly, Monthly & Shift Handover | daily checklist 40 |
| 04 | `04-tareas-perfiles.xlsx` | `04-daily-duties-side-work-by-role.xlsx` | Daily Duties & Side Work Checklists by Role | side work 590 · bartender 20 |
| 05 | `05-tareas-semanales-mensuales.xlsx` | `05-restaurant-cleaning-schedule.xlsx` | Restaurant Cleaning Schedule & Maintenance Checklists | cleaning checklist 260 · schedule 70 |
| 06 | `06-eventos-festivos.xlsx` | `06-event-holiday-checklists.xlsx` | Event & Holiday Checklists | |
| 07 | `07-plantilla-personalizable.xlsx` | `07-blank-checklist-template.xlsx` | Blank Restaurant Checklist Template (Editable) | checklist template |
| 08 | `08-apertura-cierre-negocio.xlsx` | `08-restaurant-opening-closing-checklist.xlsx` | Restaurant Opening & Closing Checklist (Whole Building) | opening and closing 50 |
| 09 | `09-apertura-cierre-caja.xlsx` | `09-cash-drawer-opening-closing.xlsx` | Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log | |
| B01 | `BONUS-01-briefing-servicio.xlsx` | `BONUS-01-pre-shift-meeting-template.xlsx` | BONUS: Pre-Shift Meeting Template (Line-Up Notes) | |
| B02 | `BONUS-02-calendario-anual-tareas.xlsx` | `BONUS-02-restaurant-holiday-calendar.xlsx` | BONUS: Restaurant Holiday & Events Calendar (US) | |

### 2.2 Pestañas (D6) — 47 hojas, 37 nombres

| Libro | Pestaña ES | Pestaña EN | Libro | Pestaña ES | Pestaña EN |
|---|---|---|---|---|---|
| todos | `Instrucciones` | `Instructions` | 05 | `Limpieza Semanal` | `Weekly Deep Clean` |
| 01 | `Apertura Cocina` | `Kitchen Opening` | 05 | `FIFO Semanal` | `Weekly FIFO Check` |
| 01 | `Apertura Sala` | `FOH Opening` | 05 | `Mantenimiento Mensual` | `Monthly Maintenance` |
| 01 | `Apertura Barra` | `Bar Opening` | 05 | `Trimestral y Anual` | `Quarterly & Annual` |
| 01 | `Cierre Cocina` | `Kitchen Closing` | 06 | `Pre-Evento` | `Pre-Event` |
| 01 | `Cierre Sala` | `FOH Closing` | 06 | `San Valentín` | `Valentine's Day` |
| 01 | `Cierre Barra` | `Bar Closing` | 06 | `Navidad` | `Christmas & NYE` |
| 02 | `Calientes` | `Hot Line` | 06 | `Temporada Terraza` | `Patio Season` |
| 02 | `Fríos` | `Cold Station` | 07 | `Por Franja Horaria` | `By Time of Day` |
| 02 | `Mise en Place` | `Mise en Place` | 07 | `Por Área` | `By Area` |
| 03 | `Diario Manager` | `Manager Daily` | 07 | `Por Perfil` | `By Role` |
| 03 | `Semanal Manager` | `Manager Weekly` | 08 | `Apertura del Negocio` | `Restaurant Opening` |
| 03 | `Mensual Manager` | `Manager Monthly` | 08 | `Cierre del Negocio` | `Restaurant Closing` |
| 03 | `Handover Turno` | `Shift Handover` | 09 | `Apertura de Caja` | `Cash Drawer Opening` |
| 04 | `Jefe de Cocina` | `Head Chef` | 09 | `Cierre de Caja` | `Cash Drawer Closing` |
| 04 | `Sous Chef` | `Sous Chef` | 09 | `Registro Mensual` | `Monthly Cash Log` |
| 04 | `Jefe de Sala` | `FOH Manager` | B01 | `Briefing` | `Pre-Shift Meeting` |
| 04 | `Camarero` | `Server` | B02 | `Calendario Anual` | `Holiday Calendar` |
| 04 | `Barman` | `Bartender` | | | |

El renombrado reescribe en el mismo paso la única fórmula con hoja (1 con referencia a hoja), las 47 áreas y los
35 títulos de impresión y todo texto que cite una pestaña. «Valentine's Day» lleva apóstrofo: openpyxl 3.1 lo escapa
(`'Valentine''s Day'!`); G1 comprueba su área de impresión.

## 3. Reglas US/UK (fuente única de las cifras; `mapas.REGLAS_US`)

| Concepto | ES (publicado) | EN | Fuente |
|---|---|---|---|
| Frío / congelador | 0-4 °C / ≤ −18 °C | 41 °F o menos / 0 °F o menos | FDA Food Code 2022 §3-501.16(A)(2); 0 °F = USDA |
| Caliente | ≥ 65 °C | 135 °F o más | FDA Food Code 2022 §3-501.16(A)(1) |
| Vitrina fría | ≤ 4 °C pescado; < 8 °C vegetales | 41 °F todo TCS (hojas, tomate y melón cortados) | FDA Food Code 2022 §3-501.16 |
| Pescado crudo | anisakis −20 °C 24 h (UE) | −4 °F 7 días o −31 °F hasta sólido + 15 h; registro 90 días | FDA Food Code 2022 §3-402.11, §3-402.12 |
| Ostras y almejas | — | etiquetas shellstock 90 días | FDA Food Code 2022 §3-203.12 |
| Etiquetado | etiquetar y fechar | date marking 7 días a 41 °F (día 1 = preparación) | FDA Food Code 2022 §3-501.17 |
| Enfriamiento (ronda 1) | — | 135 → 70 °F en 2 h y 70 → 41 °F en 4 h más (02 «Hot Line» B23, sobras) | FDA Food Code 2022 §3-501.14 |
| Recalentado (ronda 1) | — | 165 °F 15 s en ≤ 2 h para mantener en caliente (en `REGLAS_US`; sin fila ES del tema → v2.1) | FDA Food Code 2022 §3-403.11(A) |
| Sanitizante (ronda 1) | — | concentración con tiras (test kit), ppm de la etiqueta (01 «Kitchen Closing» B15, lavavajillas B17) | FDA Food Code 2022 §4-302.14; §4-501.114 |
| Aviso al consumidor (ronda 1) | — | crudo o poco hecho: aviso en la carta (02 «Cold Station» B11) | FDA Food Code 2022 §3-603.11 |
| Higiene personal | sin anillos | solo anillo liso; enfermos lo comunican; lavamanos 100 °F | FDA Food Code 2022 §2-303.11, §2-201.11, §5-202.12 |
| Lavado de vegetales | lejía 70 ppm 5 min | agua potable; producto apto a dosis de etiqueta | FDA Food Code 2022 §3-302.15 |
| Alérgenos | 14 (UE) | 9 principales; UK 14 | FALCPA + FASTER Act 2021; Food Information Regulations 2014 |
| Extintores | retimbrado 5 años; BIE | inspección visual mensual; mantenimiento anual; hidrostática según etiqueta | 29 CFR 1910.157(e)(2)-(3), (f); NFPA 10 |
| Campana | limpieza anual homologada | trimestral (alto volumen) · semestral (moderado) · mensual (sólido) | NFPA 96, tabla 11.4 |
| Extinción de campana | — | cada 6 meses | NFPA 96 §11.2; NFPA 17A |
| Frío industrial | frigorista | técnico certificado EPA 608 | 40 CFR Part 82, Subpart F |
| Fichajes | registro de jornada 4 años | fichajes 2 años; nóminas 3 (mínimo federal; NY 6) | 29 CFR 516.5-516.6; NY Labor Law §195(4) |
| Frecuencia de nómina (ronda 1) | mensual | por horas: semanal o quincenal según el estado; en la lista mensual solo se concilia | CA Labor Code §204; NY Labor Law §191; TX Labor Code §61.011 |
| Centavo | 0,01 € | 1¢: no se acuña desde 12-nov-2025, curso legal | U.S. Mint (Coin World, 12-nov-2025) |
| Backflow · grasas | legionela · analítica | test anual habitual · bombeo según ordenanza FOG | [local] compañía de agua; ordenanza municipal |
| Festivos | 22 fechas ES | Memorial Day, Labor Day, Thanksgiving; Mother's / Father's Day | 5 U.S.C. 6103; 36 U.S.C. 117 y 109 |
| UK (notas) | — | 8 °C / 63 °C; 14 alérgenos | Food Safety and Hygiene (England) Regulations 2013, sched. 4 |

## 4. Qué cambia en cada libro además de la traducción

Inventario §1 (tabla por libro): celdas exactas en `mapas.POR_CELDA` (143: caja 47, calendario 66, servicios
contratados 27, parásitos 2, fichajes 1) y `mapas.ADAPTAR` (60 instrucciones por celda, 16 de ellas del calendario).

## 5. Datos de ejemplo

- El kit no trae datos de ejemplo: las tareas, zonas, responsables y horas límite son el producto (§1, D8-D9).
- **Caso de prueba de caja** (G5, en una copia): 1 unidad de cada fila → TOTAL CASH **204.91**; cierre con starting bank
  200, cash counted 1,250, card sales 3,000, other 150, Z 4,200 → TOTAL COLLECTED 4,200 y OVER / SHORT 0.

## 6. Landing EN — réplica de `kit-tareas.ts` en `data/productos-en/tareas/restaurant-checklist-templates.ts`

| Sección ES | Tratamiento EN |
|---|---|
| plantilla | `KitTareasLandingPage` gana `lang` + diccionario `i18n/tienda/<lang>.json` y `titlePost` opcional (como `KitExcelLandingPage`); **el HTML de las 21 páginas ES que la usan sale byte a byte igual** (`tienda-gate.py`). Moneda del schema desde `TIENDAS[lang]` |
| `seo` / `schema` | title = H1 de D2; description «11 Excel checklists for restaurants: opening & closing by area, kitchen stations, manager, cleaning schedule, cash drawer count… $19»; `19.00` USD; **sin rating ni reviews**; `schema.faqs` = FAQ EN |
| `hero` | badge sin amenazas («Checklist apps charge every month; this is $19, once»); `Restaurant Checklists ` + gold `Kit Pro` + `: ` + `Opening, Closing & Cleaning Checklist Templates for Excel`; descripción con «491 restaurant tasks already written»; CTA «BUY NOW — $19» |
| `grid` | 9 tarjetas + 2 bonus con los títulos de §2.1 y lo que hace cada una (contador que excluye N/A, °F y FDA, tabla de caja en dólares) |
| `why` · `bonus` · `buyBox` · `cta` · `stickyLabel` | como el ES; bonus 3 = Equivalents Guide; tres puertas cripto (vienen con la plantilla); `#comprar` y anclas iguales; D4 |
| `faqs` | PAA: «What should be on a restaurant opening checklist?» · «What goes on a restaurant closing checklist?» · «How often should a restaurant be deep cleaned?» (05: semanal + NFPA 96) · «What is side work in a restaurant?» · «Is there a free restaurant checklist template in Excel or PDF?» (sí existen; este kit: 491 tareas, contador, °F/FDA, caja; se imprime o se guarda como PDF desde Excel) + las del ES adaptadas + «Does it work in the UK, Canada or Australia?» (patio = terrace/beer garden, 8/63 °C, 14 alérgenos, billetes editables, bonus Equivalents Guide). **Google Sheets solo si el test de F3 lo confirma** |
| `testimonials` | los del ES traducidos tal cual, subtítulo «…with Kit de Tareas Recurrentes, the Spanish edition of this kit» |
| imágenes | las del ES sin texto en español; si alguna lo lleva, Gemini (skill `generate-images`) sin texto |

## 7. Plan de F2 (entregables) y F3

1. `extraer_textos.py` ✅ → 1.064 cadenas: **G1** 429 (comunes + 01-04, 3,0 k palabras) · **G2** 345 (05-B02, 2,7 k;
   ADAPTAR: 25 en G1 y 35 en G2) · GM 290 sin traducir (pestañas, glosario, horas, `POR_CELDA`, versión, marca, pie, docProps).
2. **Traducción: 2 subagentes sonnet.** G1 PRIMERO (fija el glosario de la prosa: escribe `textos_en/glosario.json`);
   G2 después con ese glosario. Cada uno recibe sus cadenas de `textos_es.json` (`donde`, `pistas`, `adaptar`,
   `cita_rotulos`, `cita_ficheros`), §0-§5, `mapas.GLOSARIO`, `HOJAS`, `FICHEROS`, `TITULOS` y `GLOSARIO-JERGA-ES-EN.md`.
   Salida `textos_en/G<n>.json` = `{id: en}`. **Brief**:
   - `adaptar` manda sobre la traducción literal; las cifras y normas, solo las de §3 y `adaptar` (nada inventado).
   - Pestañas, rótulos y ficheros citados: el EN de `cita_rotulos` / `cita_ficheros` exacto; «» → comillas dobles rectas.
   - No tocar: ✓ — N/A ▸ 💰 📊, «86», `___` de los formularios, los 2 espacios iniciales y las MAYÚSCULAS de los
     títulos de sección, AI Chef Pro, HACCP Food Safety Kit Pro, info@aichef.pro, johnguerrero.es.
   - Firma de autor, literal: «Designed by John Guerrero — chef and restaurant consultant since 2010, in professional
     kitchens since age 17 · johnguerrero.es».
   - Inglés US de checklist (imperativo, corto; ≤ 115 % del largo ES en las columnas B de tareas); puestos y zonas
     dentro de las frases con el EN de `mapas.GLOSARIO`; °F primero; reloj de 12 h; sin € ni normas españolas;
     sin «— Restaurante Casual»; DV: título ≤ 32 y mensaje ≤ 255 caracteres.
   - Al recibirlos: barrido de español y de no latinos (`gate-no-latinos.py`).
3. **`aplicar_en.py`** (copia adaptada del staff-kit): copiar los 11 ES → hojas y referencias → `FORMULAS_POR_CELDA` →
   textos por aparición (`donde`) → capas `POR_CELDA`, `GLOSARIO`, `hora_us`, título interior, versión, marca, pie,
   docProps → `FORMATOS_EN` → Letter → protección idéntica → nombre EN → `inject_cache.py` AL FINAL. `--dry-run`,
   `--idempotencia`. Cobertura: toda aparición «regenerar» la escribe una capa o aborta.
4. **`gates_en.py`** (§8) + `--autotest` con defectos inyectados → UNA revisión adversarial (sonnet: lente de un GM US
   + lente técnica). Tope 2 rondas.
5. `restaurant-checklist-templates` en `EXCLUIDOS` de `postprocess-transversal.py` y en `PRODUCTOS_LETTER` de
   `censo-entregables.py`.
6. **F3**: landing §6, `tienda.ts`, 5 fuentes del backend con `lang: 'en'`, access/library/email, `llms.txt`, sitemap,
   enlaces entrantes (hub EN, catálogo, banners del blog EN, `footerLinks` de los kits EN hermanos) y checklist de
   `TIENDA-INTERNACIONAL.md` §6.

Presupuesto: F1 ≈ 0,4 M · F2 ≤ 1,0 M · F3 ≤ 0,9 M. Si el total pasa de 3,25 M (techo + 30 %), se para y se reporta.

## 8. Gates de F2 (contra `censo_es.json`, nunca cifras fijas)

- **G1 Paridad**: 47 hojas vía §2.2; 157 fórmulas idénticas tras el renombrado salvo las 15 fórmulas por celda; 34 DV
  (mismo sqref, tipo e ítems); 35 CF (sqref, tipo, prioridad, fórmula y relleno); 308 merges; 47 áreas, 35 títulos de
  impresión, 35 paneles; 36 hojas protegidas sin contraseña con los mismos flags; 4.286 celdas verdes y el mismo mapa
  de desbloqueadas; 491 tareas en las mismas filas; mismos anchos.
- **G2 Restos**: cero español, `€`, caracteres no latinos y coma decimal en valores, DV, pies y docProps; °C solo entre
  paréntesis tras °F; ninguna celda «HH:MM» de 24 h (172 horas de 24 h reescritas); `$`/`¢` solo en `A27:A42` del 09;
  los 282 formatos con € reescritos.
- **G3 Formato**: `paperSize 1` en 47; pie, marca, versión y docProps D19; `Instructions!B2` = título interior.
- **G4 Mapas**: cada aparición `mapa-glosario`, `mapa-hoja` y `regenerar` = su EN de `mapas.py`; horas = `hora_us`.
- **G5 Caja**: `C27:C42` = `mapas.DENOMINACIONES`; caso de §5 calculado en una copia (204.91; 4,200 y 0).
- **G6 Cálculo**: caché sin `#REF!`/`#VALUE!`/`#N/A`; contadores = los del ES.
- **G7 Reglas**: cada °F de los textos ∈ {−31, −4, 0, 10, 32, 41, 70, 100, 135, 165} (ronda 1: +70 y +165; 104 fuera, el
  filtrado del aceite va según el fabricante, sin cifra: `mapas.CELSIUS_SIN_F`); cada cita normativa EN ∈ §3.
- **G8** `censo-entregables.py --only restaurant-checklist-templates --fail` y `gate-no-latinos.py` en 0.

## 9. F3 y lo que decide John

Test real en Google Sheets antes de afirmarlo. **John**: el Payment Link USD $19 con redirección a
`/en/digital-products/restaurant-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}`. No hay preguntas de
diseño: la estructura no cambia (lo único nuevo en plantillas es el `lang` de `KitTareasLandingPage`, ya previsto en
TIENDA §3.4).

**Hermanos (~20 verticales ES):** este circuito se reutiliza tal cual cambiando el origen y los mapas por vertical:
`extraer_textos.py --origen dl/kit-tareas-<vertical>` + un `mapas_<vertical>.py` que importe este `mapas.py` y solo
añada sus pestañas, puestos, `POR_CELDA` y `ADAPTAR` propios (el glosario, `hora_us`, la caja y el calendario US ya
están), y un solo par de traductores por tanda con el glosario de esta edición.
**Hecho (18-oct, Bar Checklists Kit Pro):** `kit.py` (`--kit <v>`: mapas, origen y datos del vertical; sin él, el
base byte a byte), `<v>/mapas_<v>.py` y `heredar.py` (memoria de traducción → `heredado.json` + `pendientes.json`).
Delta del primer hermano: `bar/SPEC.md`.
