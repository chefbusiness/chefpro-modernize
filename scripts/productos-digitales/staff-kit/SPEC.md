# Restaurant Staff Scheduling Kit Pro — SPEC (F1 · 3-oct-2026 · sesión Claude Code)

> Quinto producto de la **Tienda internacional en inglés** (ola 1): la edición EN del **Kit Gestión de Personal y
> Turnos** (`kit-gestion-personal`, 14 €, contenido v2.0, 7 plantillas + 2 bonus). Doc canónico: `TIENDA-INTERNACIONAL.md`.
> Plantillas de método: `restaurant-inventory-kit/` (hojas protegidas, moneda) y `haccp-kit/` (normativa US/UK). Base:
> `F1-inventario-es.md`, `censo_es.json`, `textos_es.json` (de `extraer_textos.py`) y `mapas.py` (autotest + cruce con
> el censo, 0 errores). Esta SPEC **decide**; lo que no está aquí no se hace. Tamaño **S** ($19): techo 2,5 M tokens.

## 0. Reglas que mandan (John)

- **Duplicar el ES y adaptar, nunca reconstruir.** Mismos 9 libros, 30 hojas, rangos, merges, áreas, paneles,
  protección (sin contraseña) y semáforos. Lo que la norma US exige DENTRO de un entregable (una columna, un
  desplegable, una celda-parámetro) se aplica, se declara aquí (D8, D10, D11) y el gate lo admite por nombre.
- **Mercado: base US con notas UK** (TIENDA §1). Sin fiscalidad añadida: los impuestos y cargas de las plantillas son
  **parámetros editables** marcados como estimación. Moneda sin símbolo, US Letter, reloj de 12 h, fecha US.
- Nombres por intención de búsqueda; textos de producto con **subagentes Anthropic** (regla 1bis), nunca bridge.py.
  Landing = la ES replicada, testimonios traducidos tal cual con subtítulo de edición española, **sin**
  `aggregateRating` ni `review` (TIENDA §3.5).
- Proporcionalidad: una pasada de research (orquestador: DataForSEO + PAA), un implementador por fase, gates de
  script, una revisión final. Esta F1 ≈ 0,3 M tokens.

## 1. Decisiones

| D | Tema | Decisión | Estado |
|---|---|---|---|
| D1 | Slug | `restaurant-schedule-templates` → `/en/digital-products/restaurant-schedule-templates` (+ `/access`, `/library`). productId = slug; JWT `restaurant-schedule-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_STAFF_SCHEDULING_KIT`; ficheros en `dl/restaurant-schedule-templates/` | DECIDIDA |
| D2 | Nombre | **Restaurant Staff Scheduling Kit Pro** en landing, schema, dashboard, email, docProps, línea de marca y versión. Title SEO = H1 (Forma B, como los hermanos): «Restaurant Staff Scheduling Kit Pro: Restaurant Schedule Template & Staff Rota for Excel» (US «restaurant schedule template» 170/mes; UK «rota template» 720 y «staff rota template» 320) | DECIDIDA |
| D3 | Precio | **$19 USD**, pago único, acceso de por vida. Familia `kit-gestion-personal` en `tienda.ts` (F3) | DECIDIDA |
| D4 | Anclas | Regla del inventario (mismo `priceOld` 49 € y bonos 9 €): `priceOld` **$59**; bonos **$19** cada uno (bonos $38; valor total $97); ahorro $40; descuento 1 − 19/59 → «-67%» | DECIDIDA |
| D5 | Ficheros y títulos | Tabla §2.1. `Instructions!B2` = «NN · título» (`mapas.titulo_interior`); docProps `title` = título | DECIDIDA |
| D6 | Pestañas | Tabla §2.2. En los textos EN, pestañas y valores entre comillas dobles rectas ("Weekly Schedule"); dentro de un literal de fórmula, sin comillas | DECIDIDA |
| D7 | Claves | Un solo diccionario `mapas.CLAVES` (142): ítems de DV, literales de fórmula, de CF y de DV personalizada, en **un solo paso** (P→SP y T→PM a la vez; nunca encadenado). Los tokens de CF se traducen 1:1 y **ningún mensaje EN cambia de color** (SEARCH casa subcadenas: «cook» contiene «ok»); lo prueba `mapas.cruzar_censo` | DECIDIDA |
| D8 | Turnos (01, 05) | Códigos: M→**AM**, T→**PM**, N→**N**, P→**SP** (split), D→**DBL**, L→**OFF**, V→**V** (vacation/PTO), B→**S** (sick); ausencias del 05 V/S/**H** (holiday)/**L** (other leave), de una letra (columnas de 2,4). `Shifts!C5:D12` pasan a **horas reales** `h:mm AM/PM;;` (mismos horarios: 7 AM-3 PM, 3-11 PM, 11 PM-7 AM, split 10 AM-11 PM con 4 h de pausa, doble 7 AM-11 PM) + DV de hora nueva; 7 patrones de `FORMULAS_EN` (`Shifts!E` ×24 y descanso `AM:AR` con `1-fin+inicio` y `ROUND(…,2)`, I1-I2). Leyendas y tabla: `mapas.LEYENDAS`, `TURNOS_EN` | DECIDIDA |
| D9 | Alertas del cuadrante (01) | `B2` = **10 h** «long-shift alert» (criterio del kit: la FLSA no fija máximo diario); `B3` = **10 h** de descanso entre turnos (*clopening* de las leyes Fair Workweek; UK 11 h); `J` = 40 h/semana (umbral FLSA); 0 días libres = rojo, 1 día = ámbar «6 days on: a 7th day in a row is premium pay in CA»; menores: `O` «Under 18? (Y/N)», `N` «⛔ > 8 h (under-16 cap)», `P` rojo con N/DBL «⛔ UNDER 16: no work after 7 PM (9 PM Jun 1–Labor Day), 29 CFR 570.35; 16-17: state law» y ámbar en el resto «⚠ Minor: under 16, PM/SP end after 7 PM — check 570.35 + state law» (las reglas federales de horario son de MENORES DE 16; 16-17 = ley estatal; revisión final) — fórmulas iguales, solo literales | DECIDIDA |
| D10 | Horas extra FLSA (02) | Fila 3 de `Time Log` (vacía en el ES): `B3` inicio de la semana laboral (**2 = lunes** por defecto, la misma semana que la rejilla lunes-domingo del 01; revisión final, antes 1 = domingo). Cada copia del 02 lleva SEMANAS LABORALES ENTERAS (una semana que cruza meses va entera en una copia: `H` solo suma filas de su copia), `D3` umbral semanal **40 h**, `F3` umbral diario estatal (vacío = federal; CA 8), verdes, desbloqueadas y con DV (+3). `H` = horas extra de la fila: exceso diario + reparto semanal sobre horas **regulares** de la semana hasta ese día (`mapas.H_FLSA`: 6 × 9 h con CA 8 = 14 h, igual que sin regla diaria). Tipos: Pre-approved / Manager request / Emergency / call-in / **Not approved** / Shift cover; `C` = horas no aprobadas (se pagan igual, 29 CFR 785.11); `G` = todas × tarifa × recargo (sin «compensadas»: el *comp time* no existe en empresa privada). En `Monthly OT Summary`: `B3` tarifa de muestra 15, `D3` recargo **1.5**, `F3` **presupuesto anual** de horas extra por persona, 80 (criterio del kit: no hay tope legal). `Time Log!G` = «Scheduled hours» (8) | DECIDIDA |
| D11 | Coste laboral (03, B02) | Pagas/año → **periodos de pago/año**: DV `"52,26,24,12"` (4 ítems; excepción declarada) y **26** por defecto (cada dos semanas, *biweekly*); `C` = bruto por periodo. Coste de empresa `C2` = **10 %** editable [estimado: FICA 7,65 % + FUTA/SUTA + workers' comp; «check with your payroll provider»]; UK: NI 15 % sobre £5.000 + 3 % pensión. Semanas trabajadas **50** [estimado; UK 46,4]. Salario medio 1.400 por periodo; ETT → «agency / temp staff». Los diez tipos (claves de VLOOKUP) y sus umbrales se conservan como reglas del sector | DECIDIDA |
| D12 | Vacaciones → PTO (05) | Sin obligación federal de vacaciones pagadas: «PTO & Vacation Planner» con derecho editable `B2` = **14** días naturales (= dos semanas; UK: 5,6 semanas = 39). Semana 1 = **domingo** 3-ene-2027. «Alta» → **High** season. Finiquito → «final paycheck» (pago del PTO acumulado según el estado; CA lo exige, Labor Code §227.3). Sin «2 meses de preaviso» | DECIDIDA |
| D13 | Menores (01, 07) | Aviso del 07 a < 18 «child labor rules apply (29 CFR 570)»: < 16 límites de horas y de horario; 16-17 sin máquinas peligrosas (cortafiambres, amasadoras: HO 10-11); UK young workers 8 h/día, 40 h/semana, sin noche | DECIDIDA |
| D14 | Onboarding (04) | 17 tareas con plazo legal US fijadas en `mapas.POR_CELDA` (I-9 secciones 1 y 2, W-4, aviso de salario, *new-hire report*, workers' comp, food handler card, alérgenos US 9 / UK 14, OSHA, acoso, alcohol); **cada una respeta el desfase de su fila** (`H = alta + n`, el plazo legal nunca es más corto que el de la fila). El resto se traduce | DECIDIDA |
| D15 | Directorio (07) | Columnas por `POR_CELDA`: Employee ID, FLSA status, pay type, **SSN (solo 4 últimos)**, introductory period, food handler card y **alcohol server cert** como caducidades. Contratos: Permanent / Temporary / Intern / Trainee / Seasonal; Full-time / Part-time. Bloque RGPD → registros US (I-9 aparte, 3 años desde el alta o 1 desde la baja; nóminas 3, fichajes 2; datos médicos aparte) + nota UK GDPR; preaviso del art. 49 fuera | DECIDIDA |
| D16 | Briefing (B01) | Temperaturas en **°F** (`VALORES_EN`: 32-41, −22-0, 32-41, 135-194, 135-194; FDA Food Code §3-501.16); arqueo sin moneda (tolerancia 5); TPV → POS, lectura Z → «Z report»; APPCC → HACCP | DECIDIDA |
| D17 | Moneda | Cero `€`: los 246 formatos con € → `#,##0.00`; rótulos sin «(€)»; literal `" €"` → `""`; «in your currency». Ticket medio «before sales tax» | DECIDIDA |
| D18 | Formato | `dd/mm/yyyy` → `numFmtId 14`; `dd/mm` → `m/d`; `hh:mm` → `h:mm AM/PM`; **US Letter** (`paperSize 1`) en las 30 con la misma orientación y ajuste; pie `mapas.FOOTER_EN`; línea de marca `mapas.MARCA_EN`; versión «Version 2.0 · <mes> 2026 · aichef.pro/en/digital-products/restaurant-schedule-templates · info@aichef.pro»; docProps: `subject` «Restaurant Staff Scheduling Kit Pro · v2.0», `keywords` «restaurant schedule template, staff rota, AI Chef Pro», `description` = URL, `category` «AI Chef Pro · Digital products» | DECIDIDA |
| D19 | Notas de versión | Los bloques «lo que cambia respecto de la 1.1» (03, 05 y menciones sueltas) se traducen como explicación del porqué, sin citar la 1.1: la EN nace en 2.0 | DECIDIDA |
| D20 | Cifras derivadas | Se reescriben con la cifra EN, no se traducen: B02 `Instructions!B16` «$72,800 de ventas, 23,356.67 de coste, 32.1 %» (80 × 35 × 6 × 52/12; 7 FTE × 1.400 × 26/12 × 1,10) y el mismo veredicto que el ES (EXCELLENT, objetivo 33 %); `B11` y 03 `A24` no cambian (5 por servicio, 240 h, 7 FTE) | DECIDIDA |
| D21 | Datos de ejemplo | §5: la ficha del 06 con nombre y puesto US; puestos y glosario US en todos los textos | DECIDIDA |
| D22 | Landing | §6 (todas las secciones del ES) | DECIDIDA |
| D23 | Defectos heredados | EN nace corregido de I1 e I2. En el ES se proponen para su próxima v2.x | PROPUESTA (ES) |
| D24 | Máquina | F2 en el **VPS** (`ssh vps`, `/root/chefpro-modernize`, venv `/root/venv-guias`, `git worktree` de la rama; su `/dev/null` está roto → redirigir a ficheros de `/tmp`); `scp` de vuelta y commit desde el Mac. Si el VPS no responde: Mac en serie con `istats` < 62 °C | DECIDIDA |

## 2. Mapas

### 2.1 Ficheros (D5)

| # | Fichero ES | Fichero EN | Título EN (landing, dashboard, B2, docProps) | Intención |
|---|---|---|---|---|
| 01 | `01-cuadrante-turnos-semanal.xlsx` | `01-restaurant-schedule-template.xlsx` | Restaurant Schedule Template: Weekly & Monthly Staff Rota | US restaurant schedule template 170 · UK rota template 720 |
| 02 | `02-control-horas-extras.xlsx` | `02-overtime-tracker.xlsx` | Overtime Tracker & Time Log (FLSA 40-Hour Week) | |
| 03 | `03-coste-laboral-mensual.xlsx` | `03-labor-cost-calculator.xlsx` | Restaurant Labor Cost Calculator (Payroll & Labor %) | |
| 04 | `04-onboarding-nuevo-empleado.xlsx` | `04-new-hire-onboarding-checklist.xlsx` | New Hire Onboarding Checklist | |
| 05 | `05-planificacion-vacaciones.xlsx` | `05-pto-vacation-planner.xlsx` | PTO & Vacation Planner | |
| 06 | `06-evaluacion-desempeno.xlsx` | `06-employee-performance-review.xlsx` | Employee Performance Review Form | |
| 07 | `07-directorio-plantilla.xlsx` | `07-employee-directory.xlsx` | Employee Directory & Expiry Tracker | |
| B01 | `BONUS-01-briefing-cambio-turno.xlsx` | `BONUS-01-shift-handover-log.xlsx` | BONUS: Shift Handover Log (Manager Log Book) | |
| B02 | `BONUS-02-calculadora-plantilla-optima.xlsx` | `BONUS-02-restaurant-staffing-calculator.xlsx` | BONUS: Restaurant Staffing Calculator | |

### 2.2 Pestañas (D6) — 30 hojas, 22 nombres

| Libro | Pestaña ES | Pestaña EN | Libro | Pestaña ES | Pestaña EN |
|---|---|---|---|---|---|
| todos | `Instrucciones` | `Instructions` | 05 | `Solicitudes` | `PTO Requests` |
| 01 | `Turnos` | `Shifts` | 05 | `Saldo Vacaciones` | `PTO Balance` |
| 01 | `Cuadrante Semanal` | `Weekly Schedule` | 05 | `Cobertura` | `Coverage` |
| 01 | `Cuadrante Mensual` | `Monthly Schedule` | 06 | `Ficha Evaluación` | `Review Form` |
| 02 | `Registro Horas` | `Time Log` | 06 | `Ficha (ejemplo relleno)` | `Review Form (Sample)` |
| 02 | `Resumen Mensual` | `Monthly OT Summary` | 06 | `Histórico` | `Review History` |
| 03 | `Nóminas` | `Payroll` | 07 | `Plantilla` | `Staff Directory` |
| 03 | `Ratio Coste Laboral` | `Labor Cost Ratio` | 07 | `Vencimientos` | `Expiry Alerts` |
| 03 | `Previsión por Servicio` | `Staffing Forecast` | B01 | `Briefing` | `Shift Handover` |
| 04 | `Checklist Onboarding` | `Onboarding Checklist` | B02 | `Calculadora` | `Staffing Calculator` |
| 05 | `Calendario Anual` | `Annual Calendar` | B02 | `Ratios por Tipo` | `Ratios by Concept` |

El renombrado reescribe en el mismo paso las 2.518 con referencia a hoja, las 30 áreas y 14 títulos de impresión y todo
texto que cite una pestaña.

## 3. Reglas US/UK (fuente única de las cifras; `mapas.REGLAS_US`, `VALORES_EN`, `FORMULAS_EN`)

| Concepto | ES (publicado) | EN | Fuente |
|---|---|---|---|
| Horas extra | diarias sobre contrato, 80 h/año, ×1,25 | > 40 h por semana laboral a 1.5×; regla diaria estatal opcional | FLSA 29 U.S.C. 207(a)(1); dol.gov/agencies/whd/overtime |
| Horas extra diarias (CA) | — | 8 h a 1.5× (12 h a 2×, solo en nota) | Cal. Labor Code §510(a) |
| Horas no autorizadas | — | se pagan igual | 29 CFR 785.11-785.13 |
| Compensar con descanso | art. 35.1 ET | no en empresa privada | 29 U.S.C. 207(o) |
| Propinas | — | horas extra sobre el salario mínimo completo, no sobre el cash wage | 29 CFR 531.60; DOL Fact Sheet #15 |
| Descanso entre turnos | 12 h (art. 34.3 ET) | 10 h (NYC fast food 11 h); UK 11 h | ORS 653.442; Seattle SMC 14.22.035; NYC Admin. Code §20-1231; WTR 1998 reg. 10 |
| Jornada diaria | 9 h (art. 34.3 ET) | alerta a 10 h [criterio del kit] | la FLSA no fija máximo diario para adultos (dol.gov/agencies/whd/flsa) |
| Semana | — | 40 h; UK 48 h de media | FLSA §7(a); WTR 1998 reg. 4 |
| Descanso semanal | 1,5 días (art. 37.1 ET) | 1 día de 7 y 7.º día con recargo (CA); UK 24 h | Cal. Labor Code §§551-552, 510(a); WTR reg. 11 |
| Menores | art. 6 ET | < 16: 8 h en día sin colegio, nada tras 7 PM (9 PM jun-Labor Day); < 18: sin máquinas peligrosas | 29 CFR 570.35; 29 CFR 570.50-570.68 |
| Cargas de empresa | 33 % SS | 10 % [estimado] = FICA 7,65 % + FUTA 0,6 % sobre $7.000 + SUTA + workers' comp | IRS Publication 15; IRS Topic 759 |
| Periodos de pago | 12/14/15 pagas | 52/26/24/12 (26 por defecto) | BLS CES «Length of pay periods» |
| Vacaciones | 30 días naturales (art. 38 ET) | sin mínimo federal; 14 [criterio del kit]; UK 5,6 semanas | dol.gov/general/topic/workhours/vacation_leave; gov.uk/holiday-entitlement-rights |
| Alta del trabajador | SS antes de empezar; Contrat@ 10 días | I-9 sección 1 el primer día, sección 2 en 3 días hábiles; *new-hire report* en 20 días | 8 CFR 274a.2(b)(1); 42 U.S.C. 653a(b)(2) |
| Conservación | 4 años (art. 34.9 ET, LISOS) | I-9: 3 años o 1 tras la baja; nóminas 3; fichajes 2 | 8 CFR 274a.2(b)(2)(i)(A); 29 CFR 516.5-516.6 |
| Temperaturas (B01) | 0-4 / −18 / 65 °C | 41 °F frío, 135 °F caliente | FDA Food Code 2022 §3-501.16 |
| UK horas extra / NI | — | sin recargo legal; NI 15 % sobre £5.000 + 3 % pensión | gov.uk/overtime-your-rights; gov.uk «Rates and thresholds for employers 2025 to 2026» |

## 4. Qué cambia en cada libro además de la traducción

| # | Cambio |
|---|---|
| 01 | D8 (códigos, horas reales, DV, 7 patrones), D9 (parámetros y mensajes); `Turnos!A1:D4` por `POR_CELDA`; notas UK (rota, Early/Late, 11 h, 48 h) |
| 02 | D10 (fila 3, `H`, `C`, `G`, tipos, rótulos por `POR_CELDA`); `C:D` en `h:mm AM/PM`; notas: propinas, CA doble tiempo, UK sin recargo |
| 03 | D11 (DV de periodos, parámetros, rótulos por `POR_CELDA`); los diez tipos traducidos (claves); «gestoría» → «payroll provider or accountant» |
| 04 | D14; categorías: Hiring paperwork · Required training · Equipment & access · On-the-job training · Introductory period & reviews |
| 05 | D12, D8 (ausencias); puestos de la DV por CLAVES; «finiquito» fuera |
| 06 | Universal; ficha de ejemplo §5; escala UNSATISFACTORY → EXCELLENT |
| 07 | D13, D15; «Fecha de hoy» y vista previa sin recalcular se mantienen |
| B01 | D16; reservas, incidencias (High/Medium/Low), prioridad (Urgent/High/Normal), stock, personal |
| B02 | D11, D20; «horas complementarias / fijo-discontinuo» → «extra shifts, on-call or seasonal staff» |

## 5. Datos de ejemplo (D20-D21) — los traductores los usan tal cual

- **06 `Review Form (Sample)`**: Marta Ruiz Beltrán → **Jessica Ruiz**; «Jefa de partida — cuarto frío» → «Lead line
  cook — garde manger (cold station)»; «Q3 2026 (julio-septiembre)» → «Q3 2026 (July–September)»; «John Guerrero —
  jefe de cocina» → «John Guerrero — Head chef»; «Jefa de pastelería» → «Pastry chef»; registros APPCC → HACCP logs;
  cubiertos → covers; steak tartar → steak tartare; fechas iguales (formato US).
- **Glosario de puestos**: server, busser, bartender, host, line cook, prep cook, dishwasher, sous chef, head chef,
  FOH manager, shift manager, delivery driver; sala = front of house (FOH), cocina = back of house (BOH).
- **Valores**: `mapas.VALORES_EN` (tarifa 15, recargo 1.5, presupuesto 80 h, 10 %, 50 semanas, 26 periodos, 1.400,
  14 días, 3-ene-2027, °F del B01, ticket 35). B02 de ejemplo: «Casual dining», 80 covers, 2 servicios, 6 días.

## 6. Landing EN — réplica de `kit-gestion-personal.ts` en `data/productos-en/kits/restaurant-schedule-templates.ts`

| Sección ES | Tratamiento EN |
|---|---|
| `seo` / `schema` | title = H1 de D2; description «9 Excel templates to schedule restaurant staff: weekly & monthly schedule with clopening and minor-hour alerts, FLSA overtime tracker, labor cost %… $19»; productName D2; `19.00` USD; **sin rating ni reviews**; `schema.faqs` = FAQ EN |
| `hero` | badge sin amenazas: «FLSA overtime, clopening and minor-hour alerts built in»; título `Restaurant Staff Scheduling ` + gold `Kit Pro`; CTA «BUY NOW — $19» |
| `grid` | 7 tarjetas + 2 bonus con los títulos de §2.1; descripciones con las alertas reales (10 h entre turnos, 40 h FLSA, menores) |
| `why` | «Built for restaurants, not generic HR» (split shifts, doubles, covers per server) · «Real formulas» · «Compliance with the exact citation» (FLSA, 29 CFR 570, Fair Workweek) · «Scheduling apps charge per location every month; this is $19, once» (sin cifra de competidor salvo página de precios pública con fecha) |
| `bonus`, `buyBox`, `cta`, `pricing`, `stickyLabel` | D3-D4; anclas e ids de sección iguales a los del ES (`#comprar` y los que use la plantilla); tres puertas cripto |
| `faqs` | PAA: «Is there a free template for creating a schedule in Google Sheets?» (sí existen; este kit funciona en Sheets **solo si el test de F3 lo confirma**, y añade las alertas) · «How do I create a schedule template?» (códigos y horas una vez en Shifts → códigos en la rejilla) · «How to make a schedule in a spreadsheet?» · + las 6 del ES adaptadas (registro horario digital → «Is it a time clock?», horas extra FLSA/CA, cualquier restaurante, vs software, varios locales, garantía) · «Does it work in the UK?» (rota, 11 h, 48 h, 5,6 semanas: parámetros editables) |
| `testimonials` | los del ES traducidos tal cual, subtítulo «…with Kit Gestión de Personal y Turnos, the Spanish edition of this kit» |

Dashboard (F3): `…/library` con la isla del ES copiada y traducida (9 descargas, títulos §2.1); `…/access` con
`ProductAccessGate`; email EN; ficheros en `astro-site/public/dl/restaurant-schedule-templates/`.

## 7. Plan de F2 (entregables, en el VPS — D24)

1. `extraer_textos.py` ✅ → 872 cadenas: **G1** 384 (comunes + 01-05, 5,3 k palabras) · **G2** 294 (06-B02, 3,9 k;
   25 de ejemplo) · GM 194 sin traducir (claves, pestañas, leyendas, `POR_CELDA`, versión, marca, pie, docProps).
2. **Traducción**: 2 subagentes sonnet. G1 PRIMERO (fija glosario y la línea de firma/desprotección); G2 después con el
   glosario de G1. Cada uno recibe sus cadenas (`donde`, `pistas`, `cita_hojas`, `en_mapa`), §1-§5, `mapas.CLAVES`,
   `POR_CELDA` y `TITULOS`. Salida `textos_en/G<n>.json` = `{id: en}`. Barrido de no latinos y de español al recibirlos.
3. **`aplicar_en.py`** (copia adaptada del HACCP + protección del inventario): copiar los 9 ES → hojas y referencias →
   `FORMULAS_EN` (10 patrones, ya con pestañas EN) → CLAVES en fórmulas, CF (fórmula **y** atributo `text`), DV de lista
   y personalizadas → `DV_LISTAS_ESPECIALES` y `DV_NUEVAS` → textos por aparición → regenerados (título interior,
   versión, marca, pie, docProps, `LEYENDAS`, `TURNOS_EN`, `POR_CELDA`, `PARAMETROS` con relleno verde y desbloqueo) →
   `VALORES_EN` → `FORMATOS_EN` y `FMT_TURNOS` → Letter y pie → protección idéntica (sin contraseña) → guardar con
   nombre EN → `inject_cache.py` AL FINAL. `--dry-run`, `--idempotencia`.
4. **`gates_en.py`** (§8) + `--autotest` con defectos inyectados → UNA revisión adversarial (sonnet: lente de un
   manager US + lente técnica). Tope 2 rondas.
5. `restaurant-schedule-templates` en `EXCLUIDOS` de `postprocess-transversal.py` y en `PRODUCTOS_LETTER` de
   `censo-entregables.py`.

Presupuesto: F1 ≈ 0,3 M · F2 ≤ 1,2 M · F3 ≤ 0,7 M. Si el total pasa de 3,25 M (techo + 30 %), se para y se reporta.

## 8. Gates de F2 (contra `censo_es.json`, nunca cifras fijas)

- **G1 Paridad**: 30 hojas vía §2.2; 4.593 fórmulas idénticas tras HOJAS + CLAVES salvo los 10 patrones de
  `FORMULAS_EN` (celda a celda); 52 DV + 4 nuevas (mismo sqref y `n_celdas`; tipo igual salvo D11); 127 CF (mismo
  sqref, tipo, prioridad y relleno); 165 merges; 30 áreas, 14 títulos de impresión, 17 paneles, 27 columnas ocultas;
  21 hojas protegidas sin contraseña con los mismos flags; 7.500 celdas verdes + 3 (D10), todas desbloqueadas.
- **G2 Restos**: cero español, `€`, caracteres no latinos, coma decimal, `hh:mm` de 24 h y normativa ES (`RX_NORMA`)
  en valores, literales, DV, CF, pies y docProps; los 246 formatos con € reescritos.
- **G3 Formato**: `paperSize 1` en 30; fechas 14 / `m/d`; horas `h:mm AM/PM`; pie, marca, versión y docProps D18;
  `Instructions!B2` = título interior.
- **G4 Claves**: cada ítem de DV ∈ `CLAVES` (o D11); cada celda igual a un ítem de su lista (tipos del B02 incluidos).
- **G5 CF**: tokens EN inyectivos por rango y **cada mensaje EN con el mismo color que su ES** (`mapas.cruzar_censo`).
- **G6 Cálculo**: caché sin `#REF!`/`#VALUE!`/`#N/A`; `Shifts!E5:E12` = 8, 8, 8, 9, 16, 0, 0, 0; B02 = 7 FTE, 72,800,
  23,356.67, 32.1 %, EXCELLENT; 03 `Previsión!B22` = 23,356.67; caso FLSA de prueba en una copia (6 × 9 h, F3 vacío
  y F3 = 8 → 14 h en los dos; 4 × 10 h → 0 y 8).
- **G7 Reglas**: cada cifra de `VALORES_EN`, `DV_NUEVAS` y `FORMULAS_EN` coincide con §3 (`mapas.REGLAS_US`).
- **G8** `censo-entregables.py --only restaurant-schedule-templates --fail` y `gate-no-latinos.py` en 0.

## 9. F3 y lo que decide John

Checklist de `TIENDA-INTERNACIONAL.md` §6 (familia `kit-gestion-personal` con `en: {slug: 'restaurant-schedule-templates',
vivo: true}`, 5 fuentes del backend con `lang: 'en'`, gates LIVE, broadcast EN en la cola de 5 días; enlaces entrantes
desde el hub EN, el catálogo, los banners del blog EN y el Restaurant Inventory Kit Pro; anclas de precio de D4).
Test real en Google Sheets antes de afirmarlo en la FAQ. **John**: el Payment Link USD $19 con redirección a
`/en/digital-products/restaurant-schedule-templates/access?session_id={CHECKOUT_SESSION_ID}`.
