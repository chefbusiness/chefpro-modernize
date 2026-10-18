# Catering Checklists Kit Pro — SPEC DELTA (F1 · 18-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas para Catering** (`kit-tareas-catering`, 11 xlsx v2.0). Tercer
> hermano vertical del Restaurant Checklists Kit Pro, hecho como el bar y la cafetería: **lo que no está aquí es la
> SPEC base** (`../SPEC.md` §0-§9). Mapas: `mapas_catering.py` (importa `../mapas.py`). Tamaño S. 36 hojas.

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `catering-checklist-templates` → `/en/digital-products/catering-checklist-templates` (+ `/access`, `/library`); productId = slug; JWT `catering-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_CATERING_CHECKLISTS_KIT`; ficheros en `dl/catering-checklist-templates/` |
| D2 | Nombre | **Catering Checklists Kit Pro**; title SEO = H1: «Catering Checklists Kit Pro: Catering Event Checklist Templates for Excel». Sin el sufijo «— Catering / Eventos». El subtítulo A2 de las checklists («Kit de Tareas: Catering / Eventos») va por `GLOSARIO` con el nombre EN |
| D3-D4 | Precio | **$19 USD**, pago único; sin `priceOld`, «% off» ni anclas |
| D5 | Ficheros | §2 (US: catering checklist 90 · catering event checklist 50 · catering checklist template 50, subiendo) |
| D6 | Pestañas | Production · Transport & Delivery · Event Manager · Quarterly & Annual · Event Chef · **Banquet Captain** (maître) · Server · Bartender · Setup & Load-In · Breakdown & Load-Out · Weddings · Corporate · Cocktail Reception · Outdoor Events · By Event Phase / Area / Role · **Commissary Opening / Closing** (el «local» de un catering es su commissary; «venue» es el recinto del cliente) · Before / After the Event · Event Settlement · Event Billing Log · Pre-Event Briefing · Events Calendar |
| D8 | Glosario | base + 45 celdas (4 sobrescriben el base: Encargado → Ops manager, Recepción → Front desk, Caja → POS, Pre-servicio → Before service): subtítulo A2, zonas (Production, Transport, Setup, Breakdown, Logistics, Office, Storage, Front desk, POS), roles (Ops manager, Sales, Accounting, Event manager, Owner / GM), secciones Before / During / After service, «D-15 … D+30» → «By 15 days out … 30 days after» (los D- son plazos, ronda 1 M8), vida útil y antelaciones |
| D9 | Horas | 18 horas de 24 h (08) → `hora_us` |
| D11 | 03 «Quarterly & Annual» | plagas del commissary, campana NFPA 96, vehículo (registro, commercial auto, permiso del condado si lo pide; sin ATP ni ITV), frío EPA 608, gas, extintores OSHA 1910.157 + extinción, aceite usado, permiso sanitario del commissary, food handler cards + CFPM (2-102.12), seguros + COI, I-9 / W-4, facturación / sales tax |
| D12 | 09 = libro propio | Cobros por evento, no caja. Mismas celdas, fórmulas, DV, CF y protección que el ES; por celda: billetes y monedas US en la tabla opcional de la barra (A30:C45, 15 `FORMULAS_POR_CELDA` como el base); **IVA → sales tax**: «Taxable / Non-taxable subtotal» (deben sumar quote + extras), **C15 = base gravable × `'Event Billing Log'!$C$3`** (tipo estatal + local, `VALORES_EN` = 0, formato 0.00%), C16 = ×0 («Non-taxable subtotal: no sales tax», «Always $0»; la línea del 21 % se queda para no tocar la estructura); el tipo a 0 avisa en A3 «— set it first», D3 y D15; estados Paid / Pending / OVERDUE (`CLAVES`); fechas MM/DD/YYYY |
| D-CF | CF (desviación declarada) | Ronda 1 M5: en 15 hojas (01-06 y B01) la CF de «hecho» pasa de `$E6="✓"` a `AND($E6="✓",$B6<>"Task")`: no pinta las cabeceras internas (con «✓» en E). Mismo rango y relleno; `mapas_catering.CF_POR_CELDA`, que `aplicar_en` aplica y G1 admite por nombre (como `FORMULAS_POR_CELDA`); el autotest caza la excepción revertida y otra CF alterada |
| D14 | Calendario | Otra estructura (A nº · B fecha/evento · C tipo · D tareas · E antelación · F notas; filas 5-26): B y C fijados, E por glosario, D = traductor con ADAPTAR. Reyes → Super Bowl · Día del Padre → St. Patrick's · Comuniones → abril (+ quinceaneras y bar/bat mitzvahs), en orden cronológico tras Easter (ronda 1 M10: D y E de 7-9 por `POR_CELDA`) · Semana Santa → Easter & Passover · + Mother's Day · July 4 cookouts · Black Friday → Thanksgiving · puente → holiday party weekends · Navidad → Hanukkah / Christmas · NYE sin uvas |
| D-CAT | Comida fuera | 135 °F / 41 °F al cargar, en el trayecto, en el buffet y al descargar (3-501.16); **time as a public health control** (3-501.19: servir DENTRO de las 4 h y descartar lo que quede, sin volver al control de temperatura; frío hasta 6 h si sale ≤ 41 °F, vigilando los 70 °F y descartando si los pasa; las 4 h incluyen trayecto + servicio; procedimiento escrito); enfriar lo hecho la víspera (3-501.14); consumer advisory en ceviche / tartar (3-603.11); chafing mantiene, no recalienta (165 °F antes, 3-403.11); sobrantes: enfriar (3-501.14) o descartar lo expuesto; date marking 7 días (3-501.17); parásitos 3-402.11 |
| D-CAT | Equipo y permisos | hotel pans + insulated food carriers («cambros»); chafing fuel: no recargar ni mover encendido, extintor, normas de llama abierta del venue / fire marshal; temporary food establishment permit si se cocina en un evento público; handwashing station portátil + agua potable; carpas grandes: fire marshal |
| D-CAT | Alérgenos y alcohol | etiqueta de buffet con los 9 (UK: 14); open bar con la licencia que pida el estado (la del catering o la del venue), 21+ con ID, servicio responsable (TIPS / ServSafe Alcohol) donde lo exija el estado; alcohol del cliente solo si el estado y el venue lo permiten; nunca rellenar botellas |
| D-CAT | Jerga | BEO, guaranteed / actual count, load-in / load-out, staging area, run sheet, COI + additional insured, deposit (retainer), balance, invoice |
| D-CAT | Cobros | service charge obligatorio ≠ gratuity: es ingreso del negocio y lo pagado al personal es salario (IRS Rev. Rul. 2012-18); NY / MA presumen del personal el no anunciado (política en el contrato); managers y supervisores no se quedan propinas (FLSA); sales tax sobre el service charge y qué está gravado, según el estado (aviso + parámetro); cliente exento con certificado; cheque / ACH / tarjeta |
| D-UK | UK | 14 alérgenos en la etiqueta del buffet; nota UK en el B02 (bank holidays, Boxing Day); 8 °C / 63 °C y «event catering», en la FAQ de la landing (G2: «°C» solo tras su °F) |

## 2. Ficheros (D5)

| # | Fichero EN | Título EN |
|---|---|---|
| 01 | `01-catering-prep-production-checklist.xlsx` | Catering Prep & Production Checklist (Off-Site Catering) |
| 02 | `02-catering-transport-delivery-checklist.xlsx` | Catering Transport & Delivery Checklist: Loading, Holding Temps & Load-In |
| 03 | `03-catering-event-manager-checklist.xlsx` | Catering Event Manager Checklist + Quarterly & Annual Compliance |
| 04 | `04-catering-staff-checklists-by-role.xlsx` | Catering Staff Checklists by Role (Event Chef, Banquet Captain, Server, Bartender) |
| 05 | `05-catering-event-setup-breakdown-checklist.xlsx` | Catering Event Setup & Breakdown Checklist (Load-In / Load-Out) |
| 06 | `06-catering-event-checklists-by-type.xlsx` | Catering Event Checklists: Weddings, Corporate, Cocktail Receptions & Outdoor |
| 07 | `07-catering-checklist-template.xlsx` | Catering Checklist Template (Blank & Editable) |
| 08 | `08-catering-commissary-opening-closing-checklist.xlsx` | Catering Commissary Opening & Closing Checklist |
| 09 | `09-catering-deposits-invoicing-payments.xlsx` | Catering Deposits, Invoicing & Payments: Event Settlement & Billing Log |
| B01 | `BONUS-01-catering-pre-event-briefing-template.xlsx` | BONUS: Catering Pre-Event Briefing Template (Team Huddle) |
| B02 | `BONUS-02-catering-events-calendar.xlsx` | BONUS: Catering Busy Season & Events Calendar (US) |

## 3. Reglas del delta (`mapas_catering.REGLAS_US` = las del base + estas; §8 G7)

| Concepto | Fuente |
|---|---|
| Time as a public health control (4 h · 6 h frío ≤ 70 °F) | FDA Food Code 2022 §3-501.19 |
| Transporte y buffet 41 / 135 °F; recalentar a 165 °F; enfriar 135→70→41 °F | §3-501.16; §3-403.11; §3-501.14 |
| Certified Food Protection Manager | §2-102.12 |
| Chafing, llama abierta, carpas · permiso temporal · lavamanos portátil · vehículo | [local] fire code / IFC cap. 31; departamento de salud; [estatal] registro |
| Edad 21 · licencia de eventos · servicio responsable · alcohol del cliente · rellenado | 23 U.S.C. 158; [estatal] ABC; CA RBS, IL BASSET; 26 U.S.C. 5301(c) |
| Service charge ≠ propina · sales tax y exención · I-9 | IRS Rev. Rul. 2012-18; [estatal] department of revenue; 8 U.S.C. 1324a |
| COI · guaranteed count · Super Bowl · comuniones · sala 68-72 °F | [criterio del kit] |

°F que el kit puede afirmar (`GRADOS_F_SPEC`): −31, −4, 0, 32, 41, 68, 70, 72, 100, 135, 165.
## 4. Memoria de traducción (`../heredar.py --kit catering`, `MEMORIA`: base, bar y cafetería) y circuito (VPS)

796 cadenas; GM 229. De las 567 a traducir: **41 heredadas** (exactas, todas del base; 406 palabras) y **526
pendientes** (519 nuevas + 7 cuyo EN dice restaurant / shift manager; **5.566 palabras**; 98 con ADAPTAR) en
`textos_en/pendientes.json` → UN traductor sonnet → `textos_en/G1.json`. Venv `/root/venv-guias`:

    python3 extraer_textos.py --kit catering && python3 catering/mapas_catering.py && python3 heredar.py --kit catering
    python3 aplicar_en.py --kit catering --dry-run [--parcial] --idempotencia --mes October
    python3 gates_en.py --kit catering [--parcial] --dir <carpeta> [--autotest]     # autotest: 17 defectos

## 5. Ganchos en el código común (el base, el bar y la cafetería salen idénticos)

`gates_en.py` lee de `mapas`: `HOJA_CAJA`, `CASOS_G5` (G5: 4 casos del 09 en una copia: efectivo 204.91, liquidación
con saldo, cobrada con bases que no cuadran, registro vencido), `FORMULAS_CON_HOJA_EXTRA` (G1), `LIBROS_SIN_MARCA`
(G3: solo el 08 y el 09 traen marca D19), `HOJA_HORAS`, `HOJA_VERDE`, `CELDA_CACHE_MAL`, `CITA_AUTOTEST`; «verdes
bloqueadas» solo en hojas protegidas. `aplicar_en.py` reescribe en styles.xml los formatos del ES que estén en
`FORMATOS_EN` (fechas DD/MM/YYYY), no solo los de €.

## 6. Erratas del ES (para su próxima v2.x; la EN nace corregida)

- CF de «hecho» sobre las cabeceras internas (M5): en el ES también se pintan de verde; arreglo = la fórmula de D-CF.
- 08: carga de isotermos ANTES de revisar y preenfriar el vehículo (M6) y todo el orden del cierre (M7: furgonetas,
  muelle y papeleras con el local ya cerrado y a oscuras; nada sobre la comida que vuelve).
- BONUS-02: Comuniones antes del Día del Padre del 19-mar (M10).
- 09 «Después» B8 «no dentro de la factura» frente a D11, que mete las roturas en Extras (m5).
- 02 «Transporte» B26: «máx. 2 h de transporte refrigerado» no es una norma (con frío controlado no hay tope; sin él,
  manda el tiempo como control).
