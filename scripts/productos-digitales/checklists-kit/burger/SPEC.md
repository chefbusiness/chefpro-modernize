# Burger Joint Checklists Kit Pro — SPEC DELTA (F1 · 18-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas para Hamburguesería** (`kit-tareas-hamburgueseria`, 11 xlsx v2.0).
> Quinto hermano vertical del Restaurant Checklists Kit Pro, hecho como el bar, la cafetería, el catering y la pizzería:
> **lo que no está aquí es la SPEC base** (`../SPEC.md` §0-§9). Mapas: `mapas_burger.py` (importa `../mapas.py`). Tamaño
> S. 46 hojas, misma estructura que la pizzería.

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `burger-joint-checklist-templates` → `/en/digital-products/burger-joint-checklist-templates` (+ `/access`, `/library`); productId = slug; JWT `burger-joint-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_BURGER_JOINT_CHECKLISTS_KIT`; ficheros en `dl/burger-joint-checklist-templates/` |
| D2 | Nombre | **Burger Joint Checklists Kit Pro**; title SEO = H1: «Burger Joint Checklists Kit Pro: Burger Restaurant Opening & Closing Checklist Templates for Excel». Sin el sufijo «— Hamburguesería» |
| D3-D4 | Precio | **$19 USD**, pago único; sin `priceOld`, «% off» ni anclas |
| D5 | Ficheros | §2. Demanda US: «burger joint» 60.500/mes (intención local), «burger shop» 14.800, las variantes de checklist sin volumen: los ficheros combinan burger joint / burger shop / burger restaurant. «restaurant» SÍ vale en este kit |
| D6 | Pestañas | Como la pizzería: **Grill Station** · **Make Line** · **Fry Station** · Grill Cook · Line Cook · Fry Cook · Shift Manager · Daily Inventory · Game Night · **Burger Week** · Holiday Season. El resto, del base (08: Restaurant Opening / Closing) |
| D8 | Glosario | base + 24 celdas (4 sobrescriben el base: Auxiliar → **Dishwasher / prep**, Jefe de Cocina → Kitchen manager, Recepción → Front counter, Responsable de caja → Cashier / shift manager): Parrillero / Cocinero plancha → **Grill cook**, Freidurista / Cocinero freidora → **Fry cook**, Cocinero línea → Line cook, Encargado/a → **Shift manager** (nunca «shift lead»); kg / g / L / uds → lb / oz / qt / ea |
| D9 | Horas | 169 horas de 24 h → `hora_us` (7 fijadas en `POR_CELDA` por el orden de la apertura de cocina del 01) |
| D10 | Orden | **Erratas ES corregidas**: 01 «Kitchen Opening» filas 12-18 (comprobar que la campana tira iba DESPUÉS de encender plancha y freidora): campana → que tire → gas → plancha → freidoras → tostador → temperatura del aceite; el °C de B14 y B16 viaja con su tarea a B15 y B18 (`CELSIUS_SIN_F`, lo vigila el autotest). 08 «Restaurant Closing»: limpiar planchas y filtrar el aceite iba DESPUÉS de la alarma y la llave: 14 filas reordenadas, plancha y freidoras primero (con la campana en marcha), alarma → puertas → llave al final. 03 «Manager Daily» B21 «alarma, luces, gas» → gas, luces, alarma (ADAPTAR) |
| D11 | 05 «Quarterly & Annual» | plagas (heredada), campana + conductos NFPA 96 (**trimestral** si alto volumen o charbroil, semestral si moderado), extintores OSHA 1910.157 + extinción, prueba hidrostática (Class K y CO2 cada 5 años), gas, frío EPA 608 (con la make line), aceite usado (recycler), residuos y envases, legionela, agua (Consumer Confidence Report o pozo), seguros (+ liquor liability), POS / sales tax + apps, calibración (32 °F). 03 `B9` = fichajes FLSA (B16 del base) |
| D12 | Caja | 09 igual que el base (`POR_CELDA` y `ADAPTAR` del 09 heredados tras `cruzar_base`) |
| D14 | Calendario | Estructura del base (filas 5-26), días fuertes de un burger joint US y orden cronológico: Reyes → **Super Bowl** · Día del Padre → St. Patrick's + **March Madness** · Semana Santa → **Lent Fridays** (veggie / fish) + Easter · 1 de mayo → **National Burger Month** (28 de mayo: National Hamburger Day) · San Juan → Father's Day con las tareas del ES · vuelta al cole → + football season + **18 sept: National Cheeseburger Day** · Halloween sin cócteles · Todos los Santos → Thanksgiving + Black Friday · cenas de empresa → office orders · NYE sin uvas ni cava |
| D-BUR | Carne picada | **155 °F durante 17 s** en el centro con sonda (3-401.11(A)(2); tabla 145 °F 3 min · 150 °F 1 min · 158 °F al instante); poco hecha solo a petición y con **aviso al consumidor** (3-603.11), nunca del menú infantil (3-401.11(D)); sin los 75 °C del ES. Cruda = TCS: a 41 °F hasta la plancha, sin «temperar» (o TPHC: 4 h y se tira, 3-501.19); separada de lo listo para consumir (3-302.11); manos y guantes al pasar de crudo a listo (2-301.14, 3-304.15); descongelar en cámara (3-501.13) |
| D-BUR | Plancha · freidora | 200-230 °C ≈ **400–450 °F**; 175-180 °C ≈ **350–355 °F**. Aceite: filtrado y cambio **según el fabricante** (sin cifra: los «40 °C» del ES fuera, `CELSIUS_SIN_F`); test polares → medidor de TPM, sin límite federal. Pollo a **165 °F** (3-401.11(A)(3)) |
| D-BUR | Make line · frío | inserts, toppings cortados y coleslaw a **41 °F** con date marking 7 días (3-501.16, 3-501.17); salsas caseras 5 días (criterio del kit); bacon precocinado: enfriar 135 → 70 °F en 2 h y → 41 °F en 4 h más, o recalentar a 165 °F en 2 h para mantener en caliente; huevo frito con yema líquida / mayonesa casera: aviso al consumidor o huevo pasteurizado |
| D-BUR | Lecciones de los hermanos | tiras de sanitizante en 5 tareas diarias (superficies, mesas, make line ×2, prensa y espátulas) · 3-501.19 bien dicho · enfriamiento en dos fases y recalentado · aviso al consumidor · date marking · `TERMINOS_PROHIBIDOS` (pizza, dough, barista, tip jar, commissary, venue, BEO, shift lead, busser, cocktails, MOD…; «restaurant» permitido) · CF `$F5="✓"` sin cabeceras internas (no aplica la de catering) · `AJUSTE_MAQUETA_ES` (el ES no ajusta el texto) · orden de apertura y cierre · calendario cronológico |
| D-BUR | Delivery · alérgenos · alcohol | apps US (DoorDash, Uber Eats, Grubhub); sin repartidor propio en el ES. Los 9 de EE. UU.: el bun suele llevar **trigo, leche, huevo, soja y sésamo**; el gluten en sí no, la mostaza tampoco (UK sí); UK: 14. Cross-contact en plancha, línea y aceite compartido. Cerveza / brindis solo con licencia, 21+ con ID, sin 2x1 de bebida. Foie gras solo donde sea legal (California lo prohíbe) |
| D-BUR | Fuera | Shakes, soft-serve, drive-thru y holding cabinet: el ES no los trae → no se añaden |
| D-UK | UK | 14 alérgenos en las celdas de alérgenos; nota UK del B02 heredada; 8 °C / 63 °C en la FAQ de la landing |

## 2. Ficheros (D5)

| # | Fichero EN | Título EN |
|---|---|---|
| 01 | `01-burger-joint-opening-closing-checklists.xlsx` | Burger Joint Opening & Closing Checklists: Kitchen, FOH & Takeout |
| 02 | `02-burger-kitchen-station-checklists.xlsx` | Burger Kitchen Station Checklists: Grill, Make Line & Fry Station |
| 03 | `03-burger-restaurant-manager-checklist.xlsx` | Burger Restaurant Manager Checklist: Daily, Weekly, Monthly & Shift Handover |
| 04 | `04-burger-shop-duties-by-role.xlsx` | Burger Shop Duties by Role: Grill Cook, Line Cook, Fry Cook, Shift Manager & Server |
| 05 | `05-burger-restaurant-cleaning-checklist-inventory-maintenance.xlsx` | Burger Restaurant Cleaning Checklist, Inventory & Maintenance Schedule |
| 06 | `06-burger-joint-event-checklists.xlsx` | Burger Joint Event Checklists: Game Night, Burger Week, Holidays & Patio |
| 07 | `07-blank-burger-shop-checklist-template.xlsx` | Blank Burger Shop Checklist Template (Editable) |
| 08 | `08-burger-restaurant-opening-closing-checklist.xlsx` | Burger Restaurant Opening & Closing Checklist (Whole Building) |
| 09 | `09-cash-drawer-opening-closing.xlsx` | Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log |
| B01 | `BONUS-01-burger-joint-pre-shift-meeting-template.xlsx` | BONUS: Burger Joint Pre-Shift Meeting Template (Huddle Notes) |
| B02 | `BONUS-02-burger-joint-holiday-calendar.xlsx` | BONUS: Burger Joint Holiday & Busy Days Calendar (US) |

## 3. Reglas del delta (`mapas_burger.REGLAS_US` = las del base + estas)

| Concepto | Fuente |
|---|---|
| Picada 155 °F / 17 s y tabla · pollo 165 °F · poco hecha y menú infantil | FDA Food Code 2022 §3-401.11(A)(2), (A)(3), (D); §3-603.11 |
| TCS crudo a 41 °F · TPHC 4 h · crudo separado · manos y guantes · descongelar | §3-501.16; §3-501.19(B); §3-302.11; §2-301.14 y §3-304.15; §3-501.13 |
| Make line, toppings y coleslaw a 41 °F con date marking 7 días | §3-501.16(A)(2) y §3-501.17 |
| Agua · alérgenos (mostaza fuera de los 9) · edad 21 · foie gras | 40 CFR Part 141 Subpart O; FALCPA + FASTER Act, FIR 2014 (UK); 23 U.S.C. 158; Cal. Health & Safety Code §25982 |
| 400–450 / 350–355 °F · aceite y TPM · 3 / 5 días · 12 min · días fuertes · kg → lb | [criterio del kit]; [fabricante]; [estatal] ABC |

°F que el kit puede afirmar (G7, `GRADOS_F_SPEC`): −31, −4, 0, 32, 41, 70, 100, 135, 145, 150, 155, 158, 165, 350, 355,
400, 450.

## 4. Memoria de traducción (`../heredar.py --kit burger`, `MEMORIA`: base, bar, cafetería, catering y pizzería)

869 cadenas; GM 271 (pestañas, glosario, horas, `POR_CELDA`, 28 `VALORES_EN`, marca, versión). De las 598 a traducir:
**280 heredadas** (275 exactas + 5 por sufijo; 195 del base, 54 de la pizzería, 28 de la cafetería, 3 del bar; 2.384
palabras) y **318 pendientes** (301 nuevas, 12 con otro ADAPTAR, 2 «contexto», 3 `NO_HEREDAR`; **2.015 palabras**) en
`textos_en/pendientes.json` → UN traductor sonnet → `textos_en/G1.json`.

    python3 extraer_textos.py --kit burger && python3 burger/mapas_burger.py && python3 heredar.py --kit burger
    python3 aplicar_en.py --kit burger --dry-run [--parcial] --idempotencia --mes October
    python3 gates_en.py --kit burger [--parcial] --dir <carpeta> [--autotest]

## 5. Erratas del ES (para su próxima v2.x; la EN nace corregida)

- 01 «Apertura Cocina» B17: comprobar el tiro de la campana DESPUÉS de encender plancha y freidora (B14-B16).
- 08 «Cierre del Negocio» B18: limpiar planchas y filtrar el aceite DESPUÉS de la alarma y la llave. 03 «Diario» B21:
  «alarma, luces, gas» (el gas y las luces, antes que la alarma).
- 05 «Inventario Diario» D6:D38: los mínimos son TEXTO y la fórmula pide siempre (como la cafetería y la pizzería); A40:
  marca con otro formato. 05 «Instrucciones» B24 promete hojas protegidas y el inventario no lo está.
- 01 «Cierre Cocina» B14 y 02 «Freidora» B19: «filtrar SOLO por debajo de 40 °C» choca con las freidoras de filtrado
  en caliente: manda el fabricante. 01 «Cierre Cocina» B15: «apagar la plancha cuando ya esté fría».
- 05 «Instrucciones» B2: el título ya va cortado en el ES (dos líneas en 26 pt): la EN sube la fila (`ALTOS_FILA`).
