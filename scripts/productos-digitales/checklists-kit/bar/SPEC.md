# Bar Checklists Kit Pro — SPEC DELTA (F1 · 18-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas para Bar** (`kit-tareas-bar`, 11 xlsx v2.0). Primer hermano
> vertical del Restaurant Checklists Kit Pro: **lo que no está aquí es la SPEC base** (`../SPEC.md` §0-§9: reglas,
> D7-D13, D16-D23, caja, horas, °F, Letter, gates). Mapas: `mapas_bar.py` (importa `../mapas.py`). Tamaño S.

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `bar-checklist-templates` → `/en/digital-products/bar-checklist-templates` (+ `/access`, `/library`); productId = slug; JWT `bar-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_BAR_CHECKLISTS_KIT`; ficheros en `dl/bar-checklist-templates/` |
| D2 | Nombre | **Bar Checklists Kit Pro**; title SEO = H1: «Bar Checklists Kit Pro: Bar Opening & Closing Checklist Templates for Excel». Sin el sufijo «— Bar / Cocktails» (`VARIANTES_ES`) |
| D3-D4 | Precio | **$19 USD**, pago único; sin `priceOld`, «% off» ni anclas (FTC; regla de la tienda EN) |
| D5 | Ficheros | §2 (intención US: bar opening checklist 110 · bar closing 90 · bar checklist 50 · bartender checklist 30; UK bar cleaning checklist 50 · bar closing 30). Mismo orden 01-09 + BONUS-01/02 |
| D6 | Pestañas | 41 hojas. Heredadas: Instructions, Bar Opening/Closing, Manager Daily/Weekly/Monthly, Weekly Deep Clean, Monthly Maintenance, Quarterly & Annual, By Time of Day, By Role, cash (09), Holiday Calendar. Nuevas: Cocktail Station · Draft Beer Station · Wine & Cellar · Head Bartender · Bartender · Barback · Cocktail Server · Weekly Inventory · Cocktail Night · **New Year's Eve** (apóstrofo: G1 comprueba su definedName) · Happy Hour · Pairings & Tastings · By Area · Pre-Shift Meeting. **Cambian**: «Apertura/Cierre del Negocio» → Venue Opening / Venue Closing (en el bar, «Bar Opening» es la barra del 01) |
| D8 | Glosario | base + 28 celdas del bar: Cocktails, Coffee, Stockroom (bodega), Head bartender, Bartender, Barback, Maintenance, Ongoing, Pre-open, Week 1-4, «N weeks out», lead times del B02, Date |
| D9 | Horas | 152 horas de 24 h → `hora_us`; las de las frases (07, «18:00-20:00» del happy hour) las escribe el traductor |
| D11 | 05 «Quarterly & Annual» | 12 filas: plagas (heredada), extintores OSHA 1910.157, campana NFPA 96 + extinción cada 6 meses (si hay cocina), gas + calefactores de patio (propano, fire code local), **servicio del draft** (ácido cada 3 meses), frío EPA 608 (cámaras, botellero, máquina de hielo), filtros (traductor), legionela (programa de agua si hay misters o torre), **música y ruido** (ordenanza y permiso), **licencia de alcohol** + permiso de patio, seguros + licencias de música (ASCAP, BMI, SESAC, GMR), POS. 03 `B10` = fichajes FLSA (la fila B16 del base) |
| D12 | Caja | 09 igual que el base: las 53 celdas `POR_CELDA` y los 6 `ADAPTAR` se heredan tras comprobar el texto ES (`cruzar_base`) |
| D14 | Calendario | Otra estructura (A nº · B fecha · C evento · D tareas · E antelación · F notas; filas 4-26). B y C fijados (§3); D y F con ADAPTAR donde el evento cambia: Carnaval → Mardi Gras · Semana Santa → Spring break · 1 de mayo → Cinco de Mayo (fila 9) y Memorial Day weekend (fila 10, D y F por `POR_CELDA`) · Asunción → Jul 4 · eventos deportivos → **Super Bowl** (2.º domingo de febrero) & big games · puente de diciembre → **Thanksgiving Eve** · Nochebuena → Christmas Eve; NYE sin uvas ni cava |
| D-BAR | Alcohol | 21+ e ID; no servir a visiblemente ebrios; last call y cierre «check your state's ABC/liquor authority»; servicio responsable (TIPS / ServSafe Alcohol) donde el estado lo exija; happy hour y bebidas gratis restringidas en algunos estados (World Cocktail Day sin «cóctel gratis»); aforo = cartel del fire marshal |
| D-BAR | Draft | 38 °F; PSI del técnico o del distribuidor (sin los «2,5-3 bar» del ES); líneas cada 2 semanas y ácido cada 3 meses (Brewers Association) |
| D-BAR | Hielo | el hielo es alimento: pala o pinzas, nunca el vaso; sin mano desnuda en garnish ni hielo (FDA 3-301.11) |
| D-UK | UK | Challenge 25 (03 Daily), nota del B02 (bank holidays, Boxing Day, Temporary Event Notice); resto en la FAQ de la landing (licensing hours, personal licence) |

## 2. Ficheros (D5)

| # | Fichero EN | Título EN |
|---|---|---|
| 01 | `01-bar-opening-closing-checklists.xlsx` | Bar Opening & Closing Checklists: Bar Station, Coffee & Patio |
| 02 | `02-bar-station-checklists-cocktails-beer-wine.xlsx` | Bar Station Checklists: Cocktails, Draft Beer & Wine |
| 03 | `03-bar-manager-checklist.xlsx` | Bar Manager Checklist: Daily, Weekly & Monthly |
| 04 | `04-bartender-checklist-duties-by-role.xlsx` | Bartender Checklist & Daily Duties by Role (Head Bartender, Bartender, Barback, Server) |
| 05 | `05-bar-cleaning-checklist-inventory-maintenance.xlsx` | Bar Cleaning Checklist, Inventory & Maintenance Schedule |
| 06 | `06-bar-event-checklists.xlsx` | Bar Event Checklists: Cocktail Night, New Year's Eve, Happy Hour & Tastings |
| 07 | `07-blank-bar-checklist-template.xlsx` | Blank Bar Checklist Template (Editable) |
| 08 | `08-venue-opening-closing-checklist.xlsx` | Bar Opening & Closing Checklist (Whole Venue) |
| 09 | `09-cash-drawer-opening-closing.xlsx` | Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log |
| B01 | `BONUS-01-bar-pre-shift-meeting-template.xlsx` | BONUS: Bar Pre-Shift Meeting Template (Line-Up Notes) |
| B02 | `BONUS-02-bar-events-calendar.xlsx` | BONUS: Bar Holiday & Events Calendar (US) |

## 3. Reglas del delta (`mapas_bar.REGLAS_US` = las del base + estas)

| Concepto | EN | Fuente |
|---|---|---|
| Edad | 21 en todos los estados | National Minimum Drinking Age Act of 1984 (23 U.S.C. 158) |
| Servicio responsable | TIPS, ServSafe Alcohol u otro aprobado, obligatorio en algunos estados | [estatal] p. ej. California RBS (AB 1221), Illinois BASSET |
| Ebrios · last call · licencia | no servir a visiblemente ebrios; horas y renovación según el estado | [estatal] ABC / liquor authority; dram shop |
| Happy hour · gratis | restringidas o prohibidas en algunos estados | [estatal] p. ej. Massachusetts 204 CMR 4.03 |
| Draft | 38 °F; líneas cada 2 semanas; ácido cada 3 meses; frescura 45-60 días (sin pasteurizar) / 90-120 (pasteurizada) | Brewers Association, Draught Beer Quality Manual |
| Hielo · manos | el hielo es alimento; sin mano desnuda en alimentos listos | FDA Food Code 2022 («food» incluye el hielo); §3-301.11 |
| Música · ruido · aforo | ASCAP, BMI, SESAC, GMR; ordenanza de ruido; occupancy limit | 17 U.S.C. 106(4); [local] ordenanza y fire code |
| Vino · hielo (conversiones) | 46-50 / 61-64 / 54-61 °F; 30-50 kg = 65-110 lb | [criterio del kit] cifras del ES convertidas |
| Rellenado (ronda 1) | nunca devolver nada a una botella de licor: batches e infusiones en recipientes propios etiquetados | 26 U.S.C. 5301(c); 27 CFR 31.201 |
| Promociones (ronda 1) | sin 2x1 ni barra libre en noches abiertas al público (solo eventos privados); brindis gratis, en el precio | [estatal] 204 CMR 4.03(1)(a)-(d); 235 ILCS 5/6-28 |
| Sanitizante · alérgenos (ronda 1) | tiras en glass washer y barra (ppm de la etiqueta); aviso de alérgenos por escrito | FDA Food Code 2022 §4-302.14, §4-501.114; §3-602.12(C) |
| UK | Challenge 25, personal licence, premises licence, TEN | Licensing Act 2003; Mandatory Licensing Conditions Order 2010 |

°F que el kit puede afirmar (G7, `GRADOS_F_SPEC`): −31, −4, 0, 32, 38, 41, 46, 50, 54, 61, 64, 70, 100, 135, 165.

## 4. Memoria de traducción (`../heredar.py --kit bar`)

853 cadenas; tras la ronda 1, GM 252 (pestañas, glosario, horas, `POR_CELDA`, marca, versión). De las 601 a traducir:
**118 heredadas** (115 exactas + 3 por sufijo; 1.282 palabras) en `textos_en/heredado.json` y **483 pendientes** (475
nuevas + 7 cuyo EN del base dice «restaurant» + 1 corregida en el bar, `NO_HEREDAR`; 4.015 palabras) en
`textos_en/pendientes.json`. UN traductor sonnet → `textos_en/G1.json` = {id: en} con el brief de la SPEC base §7.2,
`../textos_en/glosario.json` y `heredado.json` como referencia de estilo.

## 5. Circuito (VPS, venv `/root/venv-guias`)

    python3 extraer_textos.py --kit bar && python3 bar/mapas_bar.py && python3 heredar.py --kit bar
    python3 aplicar_en.py --kit bar --dry-run [--parcial] --idempotencia      # real: sin --dry-run → dl/bar-checklist-templates
    python3 gates_en.py --kit bar [--parcial] --dir <carpeta> [--autotest]

Gates contra `censo_es.json` del bar: 41 hojas · 147 fórmulas (15 por celda) · 29 DV · 30 CF · 248 merges · 30
protegidas · 342 tareas · 3.365 verdes · 152 horas · 7 celdas con °C. `bar-checklist-templates` ya está en
`PRODUCTOS_LETTER` (censo-entregables) y `EXCLUIDOS` (postprocess-transversal).

## 6. Erratas del ES (para su próxima v2.x; la EN nace corregida)

- 05 «Inventario» C44: «barril conectado 3-5 días» no vale ni con bomba de aire (con ella se acaba en el día); con
  CO₂ manda la fecha del barril.
- 02 «Coctelería Clásica» B11: los flips llevan HUEVO entero y a menudo nata, no solo «LÁCTEOS».
- 08 «Cierre del Negocio» 16-19: se limpia (grifos, garnish station) DESPUÉS de activar la alarma y cerrar con llave.
- BONUS-01 B9 «2x1» y 06 «Nochevieja» B6 «barra libre»: en la EN, según el estado (ver §3).
- 02 «Cerveza y Grifo» B6: «2,5-3,0 bar» no es una presión general (depende del sistema y del gas).
- 01 «Apertura Barra» B7: «se manipulan hielo, cítricos y garnish sin guante» (en EE. UU., sin mano desnuda).
