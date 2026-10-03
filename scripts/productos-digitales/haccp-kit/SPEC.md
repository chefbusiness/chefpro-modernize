# HACCP Food Safety Kit Pro — SPEC (F1 · 3-oct-2026 · sesión Claude Code)

> Cuarto producto de la **Tienda internacional en inglés** (ola 1): la edición EN del **Pack Plantillas APPCC**
> (`pack-appcc`, 14 €, contenido v2.0, 19 plantillas + 2 bonus). Doc canónico: `TIENDA-INTERNACIONAL.md`. Plantilla de
> método: `restaurant-inventory-kit/`. Base: `F1-inventario-es.md`, `censo_es.json`, `textos_es.json` (de
> `extraer_textos.py`) y `mapas.py` (autotest + cruce con el censo, 0 errores). Esta SPEC **decide**; lo que no está
> aquí no se hace. Tamaño **S** por precio ($19): techo 2,5 M tokens el producto entero.

## 0. Reglas que mandan (John)

- **Duplicar el ES y adaptar, nunca reconstruir.** Mismos 21 libros, 48 hojas, rangos, merges, áreas, paneles y
  semáforos. Solo 3 excepciones estructurales, declaradas (D13, D14, D15-D16) y admitidas por nombre en el gate.
- Nombres por intención de búsqueda; textos de producto con **subagentes Anthropic** (regla 1bis), nunca bridge.py.
- Sin fiscalidad añadida (las plantillas no llevan importes). Landing = la ES replicada, testimonios traducidos tal
  cual con subtítulo de edición española, **sin** `aggregateRating` ni `review` (TIENDA §3.5).
- Proporcionalidad: una pasada de research, un implementador por fase, gates de script, una revisión final.

## 1. Decisiones

| D | Tema | Decisión | Estado |
|---|---|---|---|
| D1 | Slug | `haccp-templates` → `/en/digital-products/haccp-templates` (+ `/access`, `/library`). productId = slug; JWT `haccp-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_HACCP_KIT`; ficheros en `dl/haccp-templates/` | DECIDIDA |
| D2 | Nombre | **HACCP Food Safety Kit Pro** en landing, schema, dashboard, email, docProps, pies y versión. Title SEO = H1 (Forma B): «HACCP Food Safety Kit Pro: HACCP Plan Template, Food Safety Logs & Checklists for Excel» (sin cifra: no todo son registros) | DECIDIDA |
| D3 | Precio | **$19 USD**, pago único, acceso de por vida. Familia `pack-appcc` en `tienda.ts` (F3) | DECIDIDA |
| D4 | Anclas | Regla del inventario: solo importes base al escalón $…9. `priceOld` 29 € → **$39**; bonus 9 € → **$19** y 7 € → **$9** (bonos $28; valor total $67); ahorro $20; descuento 1 − 19/39 = 51,3 % → «-51%» | DECIDIDA |
| D5 | Ficheros y títulos | Tabla §2.1 (intención US/UK). Título interior (`Instructions!B2`, A1 de la hoja de trabajo) y docProps `title` = título de la tabla | DECIDIDA |
| D6 | Pestañas | Tabla §2.2. En los textos EN, pestañas y valores entre comillas dobles rectas ("Weekly Log") | DECIDIDA |
| D7 | Claves | Un solo diccionario `mapas.CLAVES` (132): ítems de DV, literales de fórmula, tokens de CF y celdas iguales a un ítem de su hoja. Semáforo universal (20 tokens) traducido 1:1; S→Y, SÍ/NO→YES/NO; turnos M/T del 04 → AM/PM | DECIDIDA |
| D8 | Marco normativo | Base **US: FDA Food Code 2022** («as adopted by your state or local health department») + notas **UK** (FSA, Safer Food Better Business, 14 alérgenos). Toda cita ES se sustituye según §3; autoridad = «your local or state health department» (UK: «your local authority»); 112 → 911 (UK 999). Alérgenos: la matriz (08) y el cartel (14) conservan las **14 columnas/filas** (UK 14 ⊇ US 9) y marcan las 9 US «(US 9)» en la cabecera; la fórmula del 08 exige la especie también en pescado (G) y crustáceos (E), como pide FALCPA | DECIDIDA |
| D9 | Temperatura | **°F** en celdas numéricas, DV y fórmulas; en texto «41 °F (5 °C)». Ejemplos convertidos half-up (`mapas.c_a_f`; el 19 con 1 decimal) salvo los overrides de D20. DV en °C → °F (`mapas.DV_NUM`, mismo sqref) | DECIDIDA |
| D10 | Límites (01, 02) | Fórmulas del 01 según §3 (32-41 °F frío y vitrina, ≤ 0 °F congelado, ≥ 135 °F caliente). `Limits!A5:C14` del 02 = `mapas.LIMITES_02` (10 familias del Food Code §3-202.11, máx. °F); filas libres A15:C20 intactas; la lista de `Instructions!B13:B22` se regenera de la misma tabla | DECIDIDA |
| D11 | Aceite (09) | No hay límite federal US de compuestos polares (TPM): 20 % «WATCH» y 25 % «CHANGE» se presentan como **punto de cambio del kit** (varios países de la UE fijan 24-27 % por ley). Máx. de fritura **375 °F** [estimado: rango comercial 350-375 °F]. Retirada: recogedor/reciclador de aceite usado con justificante; UK: waste transfer notes 2 años | DECIDIDA |
| D12 | Inspección (15) | Gravedad Ley 17/2011 → categorías Food Code **Priority / Priority foundation / Core** por punto (`mapas.SEVERIDAD_15`, con su §; las marcas P/Pf/C se comprueban una vez en F2). Resumen: «Priority violations» (cierre si hay imminent health hazard, §8-404.11). Nota UK: Food Hygiene Rating Scheme 0-5 | DECIDIDA |
| D13 | Cocción (16) | DV `C5:C44` pasa de 2 procesos a **5** (`mapas.PROCESOS_16`, límite °F en el propio rótulo: 165/155/145/135 y recalentado 165). La fórmula lee la cifra del rótulo (165 si está vacío) y el recalentado exige ≤ 120 min (§3-403.11(E)). Excepción declarada: ítems de la DV | DECIDIDA |
| D14 | Enfriamiento (17) | **Dos tramos** (§3-501.14): 135 → 70 °F en ≤ 2 h y → 41 °F en ≤ 6 h en total. La columna I («Destino») pasa a «Temp at 6 h (°F)» con DV decimal (+1 DV); el destino de los ejemplos va a «Notes» (K). INCOMPLETE mientras falte la lectura de 6 h. UK: < 8 °C en 90 min (FSA SFBB) en Instructions | DECIDIDA |
| D15 | Parásitos (18) | «Anisakis» → **parasite destruction** (§3-402.11): −4 °F durante `B3` horas (168 por defecto) o −31 °F durante 15 h. Fila 3 nueva copiando el patrón de `19!A3:C3` (etiqueta · celda verde · nota «UK: type 24»). Exenciones de §3-402.11(B) y registros 90 días (§3-402.12) en Instructions; aviso al consumidor §3-603.11 | DECIDIDA |
| D16 | Descongelación (17) | Cámara ≤ 41 °F (§3-501.13(A)) y tiempo máx. = `B3` (24 h por defecto, criterio del kit) en una fila 3 nueva como D15; nota USDA FSIS «24 h por cada 4-5 lb» | DECIDIDA |
| D17 | Termómetros (19) | Hielo **32 °F**; ebullición **212 − pies/550** (≡ 1 °C cada 300 m del ES); altitud en pies (`A3`, `C3`); tolerancia **±2 °F** (§4-203.11(A)); ejemplo Denver (5,280 ft ≈ 202 °F) | DECIDIDA |
| D18 | Personal (13, B01) | Sin «carné»: **CFPM** (§2-102.12) + food handler card donde el estado la exija; UK sin certificado legal (Level 2 habitual). Exclusión hasta **24 h** sin síntomas (§2-201.13) · UK **48 h** (FSA); enfermedades declarables «Big 6» (§2-201.11); sin contacto con la mano desnuda en RTE (§3-301.11); anillo liso permitido (§2-303.11); lavado 20 s (§2-301.12). Lista de formación = `mapas.CLAVES` (8 ítems, incluye CFPM) | DECIDIDA |
| D19 | Conservación | La línea común de los 21 libros = `mapas.CONSERVAR_EN` (2 años como regla del kit + mínimos de 90 días de §3-203.12 y §3-402.12); las 2 variantes con prefijo se traducen | DECIDIDA |
| D20 | Datos de ejemplo | §5: mismas filas, mismos platos e incidencias; nombres, proveedores y unidades US. Cifras: conversión D9 + `mapas.EJEMPLOS_NUM` (12 overrides donde la regla US cambiaría el veredicto). Las **62 fechas de texto** pasan a fechas reales (I1) | DECIDIDA |
| D21 | Formato | Fechas → `numFmtId 14`; fecha-hora → 22; horas → `h:mm AM/PM` (18); horas de texto a 12 h (`mapas.SIN_LETRAS`). **US Letter** (`paperSize 1`) en las 48 hojas con la misma orientación y ajuste; pie `mapas.FOOTER_EN`; firma `mapas.PIE_EN`; versión «Version 2.0 · <mes> 2026 · aichef.pro/en/digital-products/haccp-templates · info@aichef.pro»; docProps: `subject` «HACCP Food Safety Kit Pro · v2.0», `keywords` «haccp plan template, food safety logs, AI Chef Pro», `description` = URL, `category` «AI Chef Pro · Digital products». Papel A4 citado en texto → US Letter | DECIDIDA |
| D22 | Agua (10) | Se mantiene como «Water Quality Log»: cloro libre **0,2-4,0 mg/L** (40 CFR 141.72 y 141.65); red pública vs. pozo (muestreo anual de sistemas no públicos, §5-102.13); máquina de hielo como punto de muestreo de ejemplo; UK: Private Water Supplies Regulations 2016 | DECIDIDA |
| D23 | Trazabilidad y alertas (06, B02) | US: FSMA 204 (registros al FDA en 24 h, obligatorio desde el 20-jul-2028 para la Food Traceability List) y etiquetas de marisco 90 días (§3-203.12); avisar al health department y seguir los recall notices de FDA/USDA; Poison Control 1-800-222-1222. UK: «one step back, one step forward», avisar a la local authority y a la FSA; NHS 111 | DECIDIDA |
| D24 | Plagas y químicos (03, 07) | ROESB → «licensed pest control operator» (licencia estatal de aplicador); nº de biocida y de desinfectante → «EPA Reg. No.»; FDS → SDS (OSHA HazCom, 29 CFR 1910.1200); plazo de seguridad → «re-entry interval (label)»; UK: BPCA/NPTA y COSHH. Campana: NFPA 96 (US) / TR19 Grease (UK). Lavavajillas: aclarado final 180 °F (165 °F en máquina de rack fijo y una temperatura, §4-501.112); superficies en uso cada 4 h (§4-602.11(D)) | DECIDIDA |
| D25 | Plan HACCP (12) | Mismos 21 peligros en 7 fases; límites críticos reescritos con §3; marco: Food Code §8-201.13 (cuándo se exige plan escrito), FDA «Managing Food Safety» (retail) y Codex CXC 1-1969 (rev. 2020); UK: Reg. 852/2004 art. 5 (retenido) y SFBB. PCC/PPRo/NO → **CCP/OPRP/NO**; B/Q/F → B/C/P | DECIDIDA |
| D26 | Defectos heredados | EN nace corregido de I1 (fechas reales). En el ES, I1 se corrige en su próxima v2.x | PROPUESTA (ES) |
| D27 | Máquina | F2 en el **VPS** (`ssh vps`, `/root/chefpro-modernize`, venv `/root/venv-guias`, `git worktree` de la rama; su `/dev/null` está roto → redirigir a ficheros de `/tmp`); `scp` de vuelta y commit desde el Mac. Si el VPS no responde: Mac en serie con `istats` < 62 °C | DECIDIDA |

## 2. Mapas

### 2.1 Ficheros (D5)

| # | Fichero ES | Fichero EN | Título EN (landing, dashboard, A1, docProps) | Intención (DataForSEO, US/UK) |
|---|---|---|---|---|
| 01 | `01-registro-temperaturas-diario.xlsx` | `01-food-temperature-log.xlsx` | Food Temperature Log: Coolers, Freezers & Hot Holding | food temperature log template 140 |
| 02 | `02-registro-temperaturas-recepcion.xlsx` | `02-receiving-temperature-log.xlsx` | Receiving Temperature Log | variante de la anterior |
| 03 | `03-plan-limpieza-desinfeccion.xlsx` | `03-cleaning-sanitizing-schedule.xlsx` | Master Cleaning & Sanitizing Schedule | «cleaning schedule» (UK) |
| 04 | `04-registro-limpieza-diaria.xlsx` | `04-daily-cleaning-checklist.xlsx` | Daily Cleaning Checklist (AM/PM) | |
| 05 | `05-checklist-recepcion-mercancias.xlsx` | `05-receiving-checklist.xlsx` | Receiving Checklist for Deliveries | |
| 06 | `06-registro-trazabilidad.xlsx` | `06-traceability-log.xlsx` | Food Traceability Log (Lots In & Out) | FSMA 204 |
| 07 | `07-control-plagas-ddd.xlsx` | `07-pest-control-log.xlsx` | Pest Control Log & Bait Station Map | |
| 08 | `08-matriz-alergenos.xlsx` | `08-allergen-matrix.xlsx` | Menu Allergen Matrix (US Big 9 & UK 14) | |
| 09 | `09-control-aceite-fritura.xlsx` | `09-fryer-oil-log.xlsx` | Fryer Oil Log (TPM Tests & Disposal) | |
| 10 | `10-control-agua-potable.xlsx` | `10-water-quality-log.xlsx` | Water Quality Log (Chlorine & Private Supply) | |
| 11 | `11-registro-acciones-correctivas.xlsx` | `11-corrective-action-log.xlsx` | Corrective Action Log | |
| 12 | `12-analisis-peligros-haccp.xlsx` | `12-haccp-plan-hazard-analysis.xlsx` | HACCP Plan Template: Hazard Analysis & CCPs | haccp plan template 390 / 110 · haccp template 110 / 140 |
| 13 | `13-checklist-higiene-personal.xlsx` | `13-employee-hygiene-health-checklist.xlsx` | Employee Hygiene & Health Checklist | |
| 14 | `14-fichas-14-alergenos.xlsx` | `14-allergen-chart-reaction-protocol.xlsx` | Allergen Chart & Allergic Reaction Protocol | |
| 15 | `15-guia-inspeccion-sanidad.xlsx` | `15-health-inspection-checklist.xlsx` | Health Inspection Self-Checklist | |
| 16 | `16-registro-coccion-regeneracion.xlsx` | `16-cooking-reheating-log.xlsx` | Cooking & Reheating Temperature Log | |
| 17 | `17-registro-enfriamiento-descongelacion.xlsx` | `17-cooling-thawing-log.xlsx` | Cooling & Thawing Log (2-Stage Cooling) | |
| 18 | `18-registro-congelacion-anisakis.xlsx` | `18-parasite-destruction-log.xlsx` | Parasite Destruction Log (Fish Served Raw) | |
| 19 | `19-verificacion-termometros.xlsx` | `19-thermometer-calibration-log.xlsx` | Thermometer Calibration Log | |
| B01 | `BONUS-01-registro-formacion.xlsx` | `BONUS-01-food-safety-training-log.xlsx` | BONUS: Food Safety Training Log | |
| B02 | `BONUS-02-protocolo-alerta-alimentaria.xlsx` | `BONUS-02-food-recall-response-plan.xlsx` | BONUS: Food Recall & Foodborne Illness Response Plan | |

### 2.2 Pestañas (D6) — 48 hojas, 28 nombres

| Libro | Pestaña ES | Pestaña EN | Libro | Pestaña ES | Pestaña EN |
|---|---|---|---|---|---|
| todos | `Instrucciones` | `Instructions` | 09 | `Control Aceite` | `Oil Tests` |
| 01 | `Registro Semanal` | `Weekly Log` | 09 | `Retirada de aceite usado` | `Used Oil Pickups` |
| 02 | `Recepción Temperaturas` | `Receiving Temps` | 10 | `Control Agua` | `Water Checks` |
| 02 | `Límites` | `Limits` | 11 | `Acciones Correctivas` | `Corrective Actions` |
| 03 | `Plan Maestro L+D` | `Master Cleaning Plan` | 12 | `Análisis Peligros` | `Hazard Analysis` |
| 03 | `Productos químicos` | `Chemicals` | 13 | `Higiene Personal` | `Hygiene Checklist` |
| 04 | `Limpieza Diaria` | `Daily Cleaning` | 14 | `14 Alérgenos` | `Allergen Chart` |
| 05 | `Recepción Mercancías` | `Receiving Checklist` | 15 | `25 Puntos Inspección` | `25-Point Self-Inspection` |
| 06 | `Trazabilidad` | `Traceability In` | 16 | `Cocción y Regeneración` | `Cooking & Reheating` |
| 06 | `Salida y uso interno` | `Traceability Out` | 17 | `Enfriamiento` | `Cooling` |
| 07 | `Control Plagas DDD` | `Pest Control Log` | 17 | `Descongelación` | `Thawing` |
| 07 | `Plano de cebos` | `Bait Station Map` | 18 | `Congelación Anisakis` | `Parasite Destruction` |
| 08 | `Matriz Alérgenos` | `Allergen Matrix` | 19 | `Verificación Termómetros` | `Calibration Log` |
| B01 | `Formación Personal` | `Training Log` | B02 | `Protocolo Alerta` | `Response Plan` |

El renombrado reescribe en el mismo paso las 40 fórmulas con referencia a hoja (02 F5:F44), la DV que cita hoja
(02 E5:E44), las 48 áreas y 25 títulos de impresión y todo texto que cite una pestaña.

## 3. Límites US/UK (fuente única de las cifras; `mapas.LIMITES_F`, `LIMITES_02`, `FORMULAS_EN`)

| Concepto | ES (publicado) | EN (fórmula / texto) | Fuente |
|---|---|---|---|
| Frío (cámaras y vitrina) | 0-4 °C / 0-8 °C | 32-41 °F | FDA Food Code 2022 §3-501.16(A)(2) (≤ 41 °F); suelo 32 °F [estimado, calidad] |
| Congelado | ≤ −18 °C | ≤ 0 °F | [estimado: práctica; el Food Code no fija cifra de almacén] |
| Caliente | ≥ 65 °C | ≥ 135 °F (UK ≥ 63 °C en nota) | §3-501.16(A)(1); UK Food Hygiene Regs 2013 Sch. 4 |
| Recepción | 10 familias UE | 41 °F · 45 °F (shellstock, shucked, leche, huevo) · congelado «received frozen» (0 °F) · ambiente N/A | §3-202.11(A)-(E), §3-202.15, NSSP, PMO |
| Cocción | ≥ 75 °C | 165 °F aves/rellenos · 155 °F picados · 145 °F piezas/pescado · 135 °F vegetal para mantener | §3-401.11(A)(1)-(3), §3-401.13 |
| Recalentado | 75 °C en < 60 min | 165 °F en ≤ 2 h | §3-403.11(A),(E) |
| Enfriamiento | 60 → 10 °C en 2 h | 135 → 70 °F en 2 h y → 41 °F en 6 h (UK < 8 °C en 90 min) | §3-501.14(A); FSA SFBB «Chilling» |
| Descongelación | cámara ≤ 4 °C, ≤ 24 h | cámara ≤ 41 °F, ≤ B3 h (24) | §3-501.13(A); USDA FSIS (24 h por 4-5 lb) |
| Parásitos | −20 °C 24 h / −35 °C 15 h | −4 °F 168 h / −31 °F 15 h (UK/UE 24 h) | §3-402.11(A); registros §3-402.12 |
| Termómetro | ±1 °C; 0 / 100 °C | ±2 °F; 32 / 212 °F − ft/550 | §4-203.11(A) |
| Cloro libre | 0,2-1,0 mg/L | 0,2-4,0 mg/L | 40 CFR 141.72 y 141.65 (MRDL) |
| Aceite | 25 % CP · 180 °C | 25 % TPM (kit) · 375 °F | sin norma federal US [estimado]; D11 |
| Salud del personal | 48 h | 24 h (UK 48 h) | §2-201.13; FSA «Fitness to work» |
| Alérgenos | 14 (UE) | 9 US (FALCPA + FASTER Act; aviso escrito §3-602.12) · 14 UK | FDA; UK FIR 2014 |

## 4. Qué cambia en cada libro además de la traducción

| # | Cambio |
|---|---|
| 01 | 8 patrones de fórmula (D10); DV −40…266 °F; lecturas en °F; horas a 12 h; Hora/Firma/Nº inc. M·T → AM·PM |
| 02 | `Limits` y su lista (D10); DV −40…140 °F; ejemplos §5 |
| 03 | D24 (EPA Reg. No., SDS, NFPA 96, lavavajillas, 4 h); frecuencias por CLAVES |
| 04, 05, 06 | AM/PM (04); YES/NO y «2/3 de vida útil» como criterio del kit (05); D23 (06); fechas reales (I1) |
| 07 | D24; DV 0-168 h se conserva como «re-entry interval (h)» |
| 08 | D8: cabeceras «(US 9)», fórmula S con E y G, categorías de carta US, especificación con especie |
| 09 | D11 (fórmula 375 °F; DV 32…482 °F) |
| 10 | D22 (fórmula 0,2-4,0) |
| 11 | Ejemplos §5 con cifras EN; listas por CLAVES |
| 12 | D25; límites críticos de la columna I reescritos con §3 |
| 13, B01 | D18 |
| 14 | D8 (marca US 9; 911/999; EpiPen = «epinephrine auto-injector») |
| 15 | D12; firma del autor traducida (John Guerrero, consultor desde 2010) |
| 16 | D13 |
| 17 | D14, D16 |
| 18 | D15 |
| 19 | D17 |
| B02 | D23; tabla de contactos US/UK |

## 5. Datos de ejemplo (D20) — los traductores los usan tal cual

- **Proveedores**: Pescados de la Ría S.L. → Harbor Fresh Seafood · Cárnicas del Norte → Prime Cut Meats · Congelados del
  Sur → Polar Frozen Foods · Lácteos Vega → Valley Dairy Co. · Control de Plagas del Norte S.L. → Northside Pest Control ·
  Recogidas Oleo S.L. → GreenLoop Oil Recycling · Formación Hostelera Norte S.L. → Northside Food Safety Training · Aula
  Gastro Formación → Kitchen Skills Academy · catering Nordel → Nordel Inc. (corporate catering). Todos ficticios.
- **Personas**: Ana Ruiz → Anna Ross (A.R.) · Marcos Sáez → Mark Shaw (M.S.) · Lucía Prat → Lucy Pratt (L.P.) · J.M. igual.
- **Productos**: merluza fresca → fresh cod · canal de ternera → beef chuck (subprimal) · guisantes → frozen peas · nata →
  heavy cream · harina saco 25 kg → all-purpose flour, 50 lb bag · boquerón → anchovy (Engraulis encrasicolus) para
  boquerones · salmón igual · gambas → shrimp. Unidades US: 8,4 kg → 18.5 lb · 22 kg → 48 lb · 6 L → 1.5 gal · 4,2 kg →
  9.3 lb · 9 kg → 20 lb · 40 L → 10 gal · olla de 20 L → 5-gallon stockpot · bandejas < 5 cm → pans under 2 in deep ·
  15 cm → 6 in. Códigos: ALB- → INV- (invoice); ES/BIO y «Registro HA» → «EPA Reg. No. 00000-000 (sample)».
- **Platos del 08** (mismas marcas S/T/N → Y/T/N): Caesar salad · Ham croquettes · Seafood soup · Seafood & chicken paella ·
  Beef tenderloin with Pedro Ximénez sherry sauce · Basque-style hake with clams · Cheesecake · Vanilla ice cream. La
  especificación nombra cereal, fruto de cáscara, **especie de pescado** (p. ej. anchovy en la César) y **de crustáceo**:
  las 8 filas tienen que salir «Complete».
- **Historia de incidencias** (mismo veredicto que el ES): INC-001 walk-in 1 a 44 °F (6,5 °C) el miércoles AM, producto a
  39 °F → released · INC-002 frozen peas a 7 °F con envase roto → returned · INC-003 agua turbia → follow-up · INC-004 saco
  de harina roído → discarded · INC-005 beef stew a 78 °F a las 2 h (límite 70 °F) → discarded · INC-006 termómetro del
  walk-in 2 desviado 3.2 °F en hielo (tolerancia ±2 °F) → replaced · INC-007 stew recalentado a 158 °F (límite 165 °F) →
  reheated a 174 °F. Ejemplos numéricos: 01 = 38/39/37/39/**44**/38 °F; 02 = 35/38/7 °F; 09 = 347/352/356 °F; 16 =
  180/172/158 °F; 17 = 198→43→38, 185→46→39, 190→**78** °F; 18 = −8 °F 169 h y −33 °F 16 h; 19 = 32.5/211.1/**28.8** °F.

## 6. Landing EN — réplica de `pack-appcc.ts` en `data/productos-en/kits/haccp-templates.ts`

| Sección ES | Tratamiento EN |
|---|---|
| `seo` / `schema` | title = H1 de D2; description «21 HACCP & food safety templates for Excel… FDA Food Code limits in °F… $19»; productName D2; `19.00` USD; **sin rating ni reviews**; `schema.faqs` = FAQ EN |
| `hero` | badge sin multas españolas: «FDA Food Code 2022 limits in °F, ready for your next health inspection»; título `HACCP Food Safety ` + gold `Kit Pro`; CTA «BUY NOW — $19» |
| `grid` | **19** tarjetas + 2 bonus con los títulos de §2.1 (12 primero: es la intención principal) |
| `why` | «Not a free template, a system»: 21 plantillas enlazadas (incidencias → 11, límites → 12), semáforos automáticos, °F; sin «obligatorio por ley» español |
| `bonus`, `buyBox`, `cta`, `pricing`, `stickyLabel` | D3-D4 |
| `faqs` | las 6 del ES adaptadas + PAA: «Can I write my own HACCP plan?» (sí; §8-201.13 dice cuándo se exige por escrito) · «What is the format for a HACCP plan?» · «What are the 7 steps of a HACCP plan?» (los 7 principios del 12) · «What are the 5 documents that go in the HACCP manual?» (plan, análisis de peligros, prerrequisitos, registros de vigilancia y correctivas, verificación) · «Does it work in the UK?» (SFBB, 14 alérgenos) · «Does it work in Google Sheets?» (solo si un test real lo confirma) |
| `testimonials` | los del ES traducidos tal cual, subtítulo «…with Pack Plantillas APPCC, the Spanish edition of this kit» |

Dashboard (F3): `…/library` con la isla del ES copiada y traducida (21 descargas, títulos §2.1); `…/access` con
`ProductAccessGate`; email EN; tres puertas cripto; ficheros en `astro-site/public/dl/haccp-templates/`.

## 7. Plan de F2 (entregables, en el VPS — D27)

1. `extraer_textos.py` ✅ → 1.573 cadenas: **G1** 560 (comunes + 01-08, 5,3 k palabras) · **G2** 471 (09-14, 5,7 k) ·
   **G3** 361 (15-B02, 5,3 k) · GM 181 sin traducir. 176 son «localizar» (datos de ejemplo, §5).
2. **Traducción**: 3 subagentes sonnet. G1 PRIMERO (fija glosario y la línea común); después G2 y G3 en paralelo con el
   glosario de G1. Cada uno recibe sus cadenas (`donde`, `pistas`, `cita_hojas`, `en_mapa`), §1-§5 y los mapas.
   Salida `textos_en/G<n>.json` = `{id: en}`. Barrido de no latinos y de español al recibirlos.
3. **`aplicar_en.py`** (copia adaptada del inventario): copiar los 21 ES → hojas y referencias → CLAVES (fórmulas, CF,
   DV, celdas) → `FORMULAS_EN` → textos → regenerados (versión, pie, firma, docProps, CONSERVAR, LIMITES_02,
   SEVERIDAD_15, DV especial, PARAMETROS, ALTITUD_19, POR_CELDA) → °C→°F (TEMP_COLUMNAS, DV_NUM, EJEMPLOS_NUM)
   → fechas de texto a fechas → SIN_LETRAS → formatos → Letter y pie → guardar con nombre EN → `inject_cache.py` AL FINAL.
   `--dry-run`, `--idempotencia`.
4. **`gates_en.py`** (§8) + `--autotest` con defectos inyectados → UNA revisión adversarial (sonnet, lente inspector
   US + lente técnica; incluye las marcas P/Pf/C de D12). Tope 2 rondas.
5. `haccp-templates` en `EXCLUIDOS` de `postprocess-transversal.py` y en `PRODUCTOS_LETTER` de `censo-entregables.py`.

Presupuesto: F1 ≈ 0,35 M · F2 ≤ 1,2 M · F3 ≤ 0,7 M. Si el total pasa de 3,25 M (techo + 30 %), se para y se reporta.

## 8. Gates de F2 (contra `censo_es.json`, nunca cifras fijas)

- **G1 Paridad**: 48 hojas vía §2.2; 1.141 fórmulas idénticas tras HOJAS + CLAVES salvo los 17 patrones de
  `FORMULAS_EN` (celda a celda); 40 fórmulas con hoja; 57 DV (+1 de D14; mismo sqref y `n_celdas`; tipo igual salvo D13);
  195 CF (mismo sqref, tipo y prioridad); 294 merges; 48 áreas y 25 títulos de impresión; 25 paneles; 10.854 verdes
  (+2 de D15-D16); 0 gráficos e imágenes; sin protección, como el ES.
- **G2 Restos**: cero español, `€`, caracteres no latinos, coma decimal, horas de 24 h y normativa ES (`RX_NORMA`) en
  valores, DV, CF, pies y docProps; todo «°C» de texto va entre paréntesis tras su °F.
- **G3 Formato**: `paperSize 1` en 48; las 722 fechas con 14/22/18 y las 62 de texto convertidas; pie y versión D21.
- **G4 Claves**: cada ítem de DV ∈ `CLAVES` (o D13); celdas de ejemplo iguales a un ítem de su DV.
- **G5 CF**: tokens EN inyectivos por rango (`mapas.cruzar_censo`).
- **G6 Cálculo e historia**: caché sin `#REF!`/`#VALUE!`/`#N/A`; cada veredicto de ejemplo EN = `CLAVES[veredicto ES]`
  (01, 02, 08 = Complete ×8, 09, 10, 12, 16, 17 ×2, 18, 19, B01).
- **G7 Límites**: cada cifra de `FORMULAS_EN`, `LIMITES_02` y `PARAMETROS` coincide con §3 (`mapas.LIMITES_F`).
- **G8** `censo-entregables.py --only haccp-templates --fail` y `gate-no-latinos.py --only haccp-templates` en 0.

## 9. F3 y lo que decide John

Checklist de `TIENDA-INTERNACIONAL.md` §6 completo (familia `pack-appcc` con `en: {slug: 'haccp-templates', vivo: true}`,
5 fuentes del backend con `lang: 'en'`, gates LIVE, broadcast EN en la cola de 5 días). **John**: el Payment Link USD $19
con redirección a `/en/digital-products/haccp-templates/access?session_id={CHECKOUT_SESSION_ID}`.
