# Bakery Checklists Kit Pro — SPEC DELTA (F1 · 31-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas Recurrentes: Panadería / Obrador** (`kit-tareas-panaderia`, 11 xlsx
> **v1.1**, origen ChefBusiness, 12 €). Decimotercer hermano y el segundo en el **molde PLANO**: lo que no está aquí es
> `../foodtruck/SPEC.md` (§0 molde, §0.1 ganchos ya hechos) y la SPEC base. Mapas: `mapas_bakery.py`. Hermanos LIVE que
> fijan la jerga y el terreno: **Bakery Business Plan Kit** (`bakery-business-plan`, research en
> `../../business-plans-en-2/F1-research-us-delta.md`) y **Pastry Shop Checklists Kit Pro** (`pastry`, v2.0: tartas y
> pastelería; este kit es de **pan**).

## 0. El ES (medido en el censo) — molde plano con tres diferencias frente al food truck

Una hoja por libro, A1 marca, A2 título, cabecera en la fila 3, sin «Instrucciones», sin fórmulas ni protección, A4.
Diferencias: **01 trae 25 horas de 24 h** en D (turno de madrugada 03:00-14:30 → `hora_us`); **02 tiene 7 columnas**
(E «Valor» a rellenar, DV y CF en F); **14 celdas con °C de proceso** (sala, agua, masa, masa madre, levadura, hornos).
Tareas (`filas_tarea`): 01 25 · 02 16 · 03 18 · 04 14 · 05 13 · 06 18 · 07 16 · 08 15 = **135** + 13 campos del B01 + 12
meses del B02 = 160 en el censo. Código común tocado: ninguno (los ganchos del food truck sirven tal cual; las mutaciones
de horas del autotest vuelven porque el censo trae horas).

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `bakery-checklist-templates` (libre: ni `dl/` ni referencias en el repo) → `/en/digital-products/bakery-checklist-templates`; JWT `bakery-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_BAKERY_CHECKLISTS_KIT`; familia `kit-tareas-panaderia` |
| D2 | Nombre y title | **Bakery Checklists Kit Pro** (como el **Bakery** Business Plan Kit); title SEO = H1: «Bakery Checklists Kit Pro: **Bread Bakery** Opening, Production & Closing Checklist Templates for Excel». DataForSEO US (31-oct): bakery opening checklist **30** (la cola con más volumen), bakery checklist / cleaning checklist / cleaning schedule / production schedule / opening and closing checklist 10, closing / daily / template / sourdough starter log sin volumen; **bread bakery 12.100** y **sourdough bakery 6.600** (intención local, pero es el nombre US del oficio). «Bread» y la masa madre en title y ficheros: no pisa al «Pastry Shop Checklists Kit Pro: Opening, Closing & Cake Order Templates» |
| D3-D4 | Precio | **$15 USD** (molde plano, decisión del orquestador), pago único, sin anclas |
| D5 | Ficheros | §2 (opening & closing · sourdough starter · oven · display & counter · manager · roles · cleaning & maintenance · seasonal · blank · daily production sheet · annual calendar) |
| D6 | Pestañas | Opening & Closing · Starter & Fermentation · Ovens & Baking · Display & Counter · Manager Tasks · Duties by Role · Weekly & Monthly · Seasons & Holidays · Blank Template · Daily Production Sheet · Annual Calendar |
| D8 | Glosario | base + **99** (1 sobrescribe: Encargado → Manager). Jerga del Bakery Business Plan Kit: **head baker** (maestro), **baker** (oficial y panadero), **bakery assistant**, **counter staff**, **deck / rack oven**, **proofer** (cámara de fermentación), **retard** / retarder, **sourdough starter**, bulk / final proof, poolish, biga; obrador → **Production** / bakehouse (nunca «workshop»); tienda → Shop |
| D9 | Horas | 25 horas de celda → `hora_us`; las de los títulos de sección (03:00-05:00…) las escribe el traductor (3:00–5:00 AM) |
| D10 | °C de proceso | Las cifras del ES (no son normas) en °F por `POR_CELDA`: sala, agua, masa, masa madre, retardo y levadura al °F entero (72–79, 39–46 / 64–72, 75–79, 75–82, 37–41, 36–39); hornos redondeados de 5 en 5 (430–500 solera; 465–480 barra; 445–465 hogaza y masa madre; 445 chapata; 430–445 integral; 375–390 croissant; 355–375 brioche). Seguridad: TCS 41 / 135 °F en empanadas de carne y rellenos de crema (3-501.16) |
| D11 | Etiquetas y alérgenos | Lo embolsado o encajado en tienda: nombre, ingredientes, peso neto y alérgenos principales (**3-602.11**); lo que va sin envasar: aviso escrito donde se adoptó el Food Code 2022 (**3-602.12(C)**); los 9 US con el **trigo** (no «gluten») y el **sésamo** (semillas); «gluten-free» solo < 20 ppm (21 CFR 101.91) y con separación; «organic» con USDA Organic (7 CFR Part 205); báscula de venta al peso legal-for-trade (NTEP) e inspección de weights & measures [local] |
| D12 | Sin caja | `HOJA_CAJA = None`: la caja del día son 01 B24 / B31, 04 B20, 06 B25 (POS, starting bank, cash count, over/short) |
| D14 | Calendarios | **08**: Navidad (roscón, turrones) → **Holiday season** (stollen, panettone, dinner rolls), Semana Santa → **Easter** (hot cross buns), Día del Pan → **World Bread Day** (16-oct, el mismo día), Comuniones → **Thanksgiving** (el gran día de pedidos de pan US), San Valentín y Halloween se quedan (`POR_CELDA`). **B02** (A mes · B panes · C eventos · D mantenimiento · E formación): A y C fijados (Super Bowl, Mardi Gras king cakes, St. Patrick's soda bread, Easter / Passover, Mother's Day, Jul 4 buns, Rosh Hashanah round challah, World Bread Day, Thanksgiving, holidays); B / D / E traductor, sin roscón, turrones, pan gazpacho ni coca |
| D15 | Marca y versión | A1 → «AI Chef Pro»; línea de marca «AI Chef Pro · aichef.pro · Bakery Checklists Kit Pro» (sin «—»); docProps «· v1.1»; US Letter |
| D-PAN | Gestión | Mermas «< 8 %» = objetivo del kit (se dice así); food cost «about 30%; US bakeries run 28–35%» (research §4); ficha de harina US (proteína, ash, falling number; W y P/L solo si el molino los da); gas de hornos por técnico con licencia [local]; plagas por licensed PCO; cottage food **no aplica** (panadería con tienda = food establishment con permiso; research §9) |
| D-LEX | Términos prohibidos | restaurant (salvo consultant), host stand, head / sous chef, line cook, busser, barback, bartender, server, dining room, **workshop**, **obrador**, plancha, food truck, window staff, MOD, FOH |
| D-UK | UK | Solo en la FAQ de la landing: 14 alérgenos, 8 °C / 63 °C; para llevar, pan y bollería fría zero-rated (research §9) |

## 2. Ficheros (D5) — títulos en `mapas_bakery.TITULOS`

| # | Fichero ES | Fichero EN |
|---|---|---|
| 01 | `01-apertura-cierre-panaderia.xlsx` | `01-bakery-opening-closing-checklist.xlsx` |
| 02 | `02-masas-madre-fermentacion.xlsx` | `02-sourdough-starter-fermentation-checklist.xlsx` |
| 03 | `03-hornos-coccion.xlsx` | `03-bakery-oven-baking-checklist.xlsx` |
| 04 | `04-expositor-venta.xlsx` | `04-bakery-display-counter-checklist.xlsx` |
| 05 | `05-tareas-manager.xlsx` | `05-bakery-manager-checklist.xlsx` |
| 06 | `06-tareas-perfiles.xlsx` | `06-bakery-duties-by-role.xlsx` |
| 07 | `07-semanales-mensuales.xlsx` | `07-bakery-cleaning-maintenance-schedule.xlsx` |
| 08 | `08-eventos-estacionales.xlsx` | `08-bakery-seasonal-holiday-checklist.xlsx` |
| 09 | `09-plantilla-personalizable.xlsx` | `09-blank-bakery-checklist-template.xlsx` |
| B01 | `BONUS-01-briefing-produccion.xlsx` | `BONUS-01-bakery-daily-production-sheet.xlsx` |
| B02 | `BONUS-02-calendario-anual.xlsx` | `BONUS-02-bakery-annual-calendar.xlsx` |

## 3. Reglas del delta (`REGLAS_US` = base + 11; 41 en total)

| Concepto | Fuente |
|---|---|
| Temperaturas de proceso convertidas (sala, agua, masa, masa madre, retardo, levadura, hornos) | [criterio del kit]: las cifras del ES en °F |
| TCS en panadería (empanadas de carne, rellenos de crema) | FDA Food Code 2022 §1-201.10, §3-501.16 |
| Etiqueta de lo envasado en tienda · aviso escrito de lo no envasado | §3-602.11(B)(5), §3-602.12(C) (FDACS Florida; Illinois DPH, allergen FAQ) |
| «Gluten-free» < 20 ppm · «organic» | 21 CFR 101.91 · 7 CFR Part 205 |
| Báscula legal-for-trade · gas por técnico con licencia · plagas por PCO | [local] NIST Handbook 44 / NTEP; código de gas (base); [estatal] licencia de PCO |
| Food cost 28-35 % · cottage food no aplica · calendario US | research US del Bakery Business Plan Kit §4 y §9; [criterio del kit] + 5 U.S.C. 6103 |

°F permitidos (G7): −31, −4, 0, 36, 37, 39, 41, 46, 64, 70, 72, 75, 79, 82, 100, 135, 165, 355, 375, 390, 430, 445, 465,
480, 500. 14 celdas ES con °C, todas por `POR_CELDA`.

## 4. Memoria de traducción (`MEMORIA`: food truck, base, pastry)

**425 cadenas** (832 apariciones); **GM 201** (604 palabras: 11 pestañas, glosario, 61 `POR_CELDA`, 25 horas, marca, pie,
docProps). De las **224 a traducir: 7 heredadas** (exactas; 6 del food truck, 1 de la pastelería; 16 palabras) y **217
pendientes** (todas nuevas; **1.107 palabras**; 35 ADAPTAR): **G1 91 / 539** (01-04) y **G2 126 / 568** (05-B02).
Traducidas en esta sesión (`textos_en/G1.json`).

## 5. Erratas del ES (para su v2.0; la EN las deja o nace corregida)

- Tildes quitadas en todo el kit (77 celdas; pestañas «Hornos y Coccion», «Briefing Produccion»).
- La landing ES promete lo que los ficheros no traen: horno de **convección**, «protocolos para recuperar masas que pierden
  fuerza», «gestión de cola en horas punta y reposición», «reporting con KPIs», «calibración de termómetros» (solo
  básculas), **San Juan** en el 08 y «acciones de marketing por estación» en el B02 (la columna E es **Formación**).
- 01 B22 «alérgenos (gluten, leche, huevo, soja)»: faltan el sésamo y los frutos secos de los panes con semillas y nueces.
- 05 y 09 sin el desplegable ✓ / — / N/A que anuncia el changelog 1.1.
