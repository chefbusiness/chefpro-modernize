# Coffee Shop Checklists Kit Pro — SPEC DELTA (F1 · 18-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas para Cafetería** (`kit-tareas-cafeteria`, 11 xlsx v2.0). Segundo
> hermano vertical del Restaurant Checklists Kit Pro, hecho como el bar (`../bar/SPEC.md`): **lo que no está aquí es
> la SPEC base** (`../SPEC.md` §0-§9). Mapas: `mapas_cafe.py` (importa `../mapas.py`). Tamaño S.

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `coffee-shop-checklist-templates` → `/en/digital-products/coffee-shop-checklist-templates` (+ `/access`, `/library`); productId = slug; JWT `coffee-shop-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_COFFEE_SHOP_CHECKLISTS_KIT`; ficheros en `dl/coffee-shop-checklist-templates/` |
| D2 | Nombre | **Coffee Shop Checklists Kit Pro**; title SEO = H1: «Coffee Shop Checklists Kit Pro: Coffee Shop Opening & Closing Checklist Templates for Excel». Sin el sufijo «— Cafetería / Brunch». «cafe» SIN tilde (US y UK), nunca «café» |
| D3-D4 | Precio | **$19 USD**, pago único; sin `priceOld`, «% off» ni anclas |
| D5 | Ficheros | §2 (US: coffee shop/cafe checklist 140 · coffee shop opening checklist 90 · closing 20 · barista checklist 10; UK: cafe cleaning checklist 20). Orden 01-09 + BONUS-01/02 |
| D6 | Pestañas | 49 hojas. Nuevas: Espresso Bar Opening / Closing · Pastry Case · Shift Lead · Barista · Baker · Busser & Runner · Daily / Weekly Inventory · Sunday Brunch · **Holiday Season** (Navidad + invierno) · **Cafe Opening / Cafe Closing** (08). El resto, del base |
| D8 | Glosario | base + 33 celdas (7 sobrescriben el base; ronda 1 M5: Jefe de Cocina → Kitchen lead, Jefe de Sala → Shift lead, Gerente → Manager, Recepción → Front counter, Responsable de caja → Cashier / shift lead): Encargado(/a) → **Shift lead** (no «shift manager»), Pastelero/a → Baker, Auxiliar → Busser / runner, Cocinero calientes / fríos → Hot line / Cold station cook, Técnico SAT → Espresso tech, Office, Storage, Walk-in, Spring / Fall, fechas de Navidad; unidades kg / g / L / uds / doc → lb / oz / qt / ea / doz |
| D9 | Horas | 274 horas de 24 h → `hora_us` |
| D11 | 05 «Quarterly & Annual» | plagas (heredada), campana NFPA 96 si se cocina bajo campana (semestral; anual solo si bajo volumen) + extinción cada 6 meses, extintores OSHA 1910.157, legionela (programa de agua), gas, frío EPA 608 (con la vitrina), aceite usado si hay freidora, seguros (liquor liability solo si sirves alcohol), POS / sales tax. Agua y café (filtro, GH/KH, SAT, muelas en lb, termómetros a 32 °F) = traductor. 03 `B15` = fichajes FLSA (B16 del base) |
| D12 | Caja | 09 igual que el base (53 `POR_CELDA` y 6 `ADAPTAR` heredados tras `cruzar_base`) |
| D14 | Calendario | Misma estructura que el base (filas 5-26); cambian: Reyes → **King cake season** (Jan 6) · Día del Padre → St. Patrick's (sin alcohol) y Father's Day en junio con las tareas del ES · Semana Santa → Easter (hot cross buns) · 1 de mayo → **Teacher Appreciation Week** · vuelta al cole → + **National Coffee Day (Sep 29)** · Todos los Santos → Thanksgiving (pumpkin / pecan pie) · cenas de empresa → **holiday catering** · NYE sin uvas ni cava, brindis sin alcohol salvo licencia |
| D-CAFE | Espresso | jerga barista US (espresso machine, group head, portafilter, steam wand purge, dial in, shots, grinder burrs, hopper, knock box, milk pitchers, drip / batch brew, airpot, pastry case, POS, tip jar); **backflush diario con detergente y descale según el fabricante**, sin cifras propias; «25–30 s / 25–30 ml (about 1 fl oz)» y «9 bar» se quedan |
| D-CAFE | Leche · cold brew | abierta a **41 °F o menos** con date marking: **7 días contando el de apertura, sin pasar del use-by** (3-501.17(B); ronda 1 M1); cold brew (ronda 1 M3): filtrar, tapar, 41 °F y 7 días contando el de preparación, el reposo en frío salvo que lo permita el departamento de salud; jarras frías y separadas por tipo; **milk, soy y tree nuts** entre los 9 (la avena no) |
| D-CAFE | Vitrina | refrigerada a 41 °F para lo TCS; date marking 7 días (3-501.17); pinzas / bakery tissue / guantes, sin mano desnuda (3-301.11); etiqueta con los 9 alérgenos (UK: 14) |
| D-CAFE | Hielo · alcohol | hielo = alimento (pala, nunca el vaso); mimosa / bellini / champán solo con licencia, 21+ con ID; regalar alcohol, según el estado |
| D-CAFE | Inventario | unidades US y los mínimos como **número** (`VALORES_EN`, 34 celdas): kg → lb (×2,2) y g → oz (÷28,35) redondeados; L → qt y uds sin cambiar la cifra; «⚠️ PEDIR» → «⚠️ REORDER» (`CLAVES`) |
| D-UK | UK | 14 alérgenos en las celdas de alérgenos; nota UK del B02 heredada; 8 °C / 63 °C y el resto, en la FAQ de la landing. **Sin Natasha's Law**: el kit no habla de envasado para venta directa (solo vasos y bolsas take-away) |

## 2. Ficheros (D5)

| # | Fichero EN | Título EN |
|---|---|---|
| 01 | `01-coffee-shop-opening-closing-checklists.xlsx` | Coffee Shop Opening & Closing Checklists: Espresso Bar, Kitchen & FOH |
| 02 | `02-cafe-kitchen-pastry-case-checklists.xlsx` | Cafe Kitchen Checklists: Hot Line, Cold Station & Pastry Case |
| 03 | `03-coffee-shop-manager-checklist.xlsx` | Coffee Shop Manager Checklist: Daily, Weekly, Monthly & Shift Handover |
| 04 | `04-barista-checklist-duties-by-role.xlsx` | Barista Checklist & Daily Duties by Role (Shift Lead, Barista, Baker, Server, Busser) |
| 05 | `05-cafe-cleaning-checklist-inventory-maintenance.xlsx` | Cafe Cleaning Checklist, Inventory & Maintenance Schedule |
| 06 | `06-coffee-shop-event-checklists.xlsx` | Coffee Shop Event Checklists: Sunday Brunch, Valentine's Day, Holiday Season & Patio |
| 07 | `07-blank-coffee-shop-checklist-template.xlsx` | Blank Coffee Shop Checklist Template (Editable) |
| 08 | `08-cafe-opening-closing-checklist.xlsx` | Cafe Opening & Closing Checklist (Whole Shop) |
| 09 | `09-cash-drawer-opening-closing.xlsx` | Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log |
| B01 | `BONUS-01-coffee-shop-pre-shift-meeting-template.xlsx` | BONUS: Coffee Shop Pre-Shift Meeting Template (Huddle Notes) |
| B02 | `BONUS-02-coffee-shop-holiday-calendar.xlsx` | BONUS: Coffee Shop Holiday & Events Calendar (US) |

## 3. Reglas del delta (`mapas_cafe.REGLAS_US` = las del base + estas)

| Concepto | EN | Fuente |
|---|---|---|
| Leche · cold brew · vitrina | 41 °F o menos (TCS); date marking 7 días (leche: desde la apertura, sin pasar el use-by) | FDA Food Code 2022 §3-501.16, §3-501.17(A)-(B) |
| Hollandaise · huevos | 135 °F o más o 4 h con la hora marcada; aviso al consumidor salvo huevo pasteurizado; tiras de sanitizante a diario | FDA Food Code 2022 §3-501.19(B), §3-603.11, §4-302.14 |
| Alérgenos de las leches | milk, soy, tree nuts entre los 9; la avena no | FALCPA 2004 + FASTER Act 2021 |
| Mano desnuda · hielo | pinzas o guantes en lo listo para consumir; el hielo es alimento | FDA Food Code 2022 §3-301.11 y «food» |
| Espresso | backflush diario con detergente; descale según el fabricante | [fabricante] manual de la máquina |
| Alcohol | 21 en todos los estados; regalarlo, restringido en algunos | 23 U.S.C. 158; [estatal] ABC / liquor authority |
| Conversiones · fechas | muelas 400-600 / 800-1.200 kg = 880-1,320 / 1,760-2,650 lb; mínimos kg → lb, g → oz; National Coffee Day 29-sep; Teacher Appreciation Week 1.ª semana completa de mayo | [criterio del kit] |

°F que el kit puede afirmar (G7, `GRADOS_F_SPEC`): −31, −4, 0, 32, 41, 70, 100, 135, 165.

## 4. Memoria de traducción (`../heredar.py --kit cafe`, fuentes `MEMORIA`: base y luego bar)

1.108 cadenas; GM 262 (pestañas, glosario, horas, `POR_CELDA`, `VALORES_EN`, marca, versión). De las 846 a traducir:
**226 heredadas** (223 exactas + 3 por sufijo; 222 del base y 4 del bar) y **620 pendientes** (588 nuevas, 16 «contexto»,
13 con otro ADAPTAR y 3 `NO_HEREDAR` de la ronda 1) → `textos_en/G1.json` (traductor sonnet + ronda 1).

## 5. Circuito (VPS, venv `/root/venv-guias`)

    python3 extraer_textos.py --kit cafe && python3 cafe/mapas_cafe.py && python3 heredar.py --kit cafe
    python3 aplicar_en.py --kit cafe --dry-run [--parcial] --idempotencia --mes October
    python3 gates_en.py --kit cafe [--parcial] --dir <carpeta> [--autotest]     # autotest: 18 (+ VALORES_EN y término prohibido)

Gates: 49 hojas · 235 fórmulas (15 por celda; 77 del inventario dan "" como el ES: G6 «vacías como ES») · 34 DV · 35 CF
· 328 merges · 36 protegidas · 500 tareas · 274 horas · 10 °C · 34 valores fijados · G2 `TERMINOS_PROHIBIDOS` (ronda 1
M5: roles y zonas de restaurante en cualquier pieza EN). En `PRODUCTOS_LETTER` y `EXCLUIDOS`.

## 6. Erratas del ES (para su próxima v2.x; la EN nace corregida)

- 05 «Inventario Diario» D6:D44: los mínimos son TEXTO («2»); `IF(B6<D6, …)` compara un número con un texto y da
  «⚠️ PEDIR» siempre (en Excel un número es menor que cualquier texto). Escribirlos como número.
- 05 «Inventario Diario» A48 / «Inventario Semanal» A58: línea de marca con otro formato («Kit de Tareas Recurrentes:
  … —»), distinta de la del resto del kit. (04 «Auxiliar» B17: «Office» = zona de friegue; en el 03, la oficina.)
- Horas: 08 «Apertura del Negocio» E5:E8 y 04 «Encargado» E6 abren después de que la pastelería hornee (6:30 AM)
  → EN 6:30 AM. 05 «Instrucciones» B23 promete hojas protegidas, y los inventarios no lo están (la EN corrige la promesa).
