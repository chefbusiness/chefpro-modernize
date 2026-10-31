# Seafood Restaurant Checklists Kit Pro — SPEC DELTA (F1 · 31-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas Recurrentes: Marisquería con Vivero y APPCC** (`kit-tareas-marisqueria`,
> 11 xlsx **v1.1**, origen ChefBusiness, 12 €). Decimocuarto hermano y el tercero y último en el **molde PLANO**: lo que
> no está aquí es `../foodtruck/SPEC.md` (§0 molde, §0.1 ganchos) y la SPEC base. Mapas: `mapas_seafood.py`.

## 0. El ES (medido en el censo)

Molde plano como el food truck y la panadería: una hoja por libro, A1 marca, A2 título, cabecera en la fila 3, sin
«Instrucciones», fórmulas ni protección, A4. Como la panadería: **30 horas** de 24 h en el 01 (07:00-23:45) y el 02 con 7
columnas (E «Valor», DV y CF en F); **14 celdas con °C**. Es el kit más español de los tres: vivero, **lonja y subasta**,
especies gallegas, zona FAO y Reglamento UE 1379/2013, anisakis por RD 1021/2022, alérgenos «2 y 14» de la UE, vedas por
comunidad autónoma, mariscada. Tareas (`filas_tarea`): 01 30 · 02 21 · 03 17 · 04 19 · 05 18 · 06 25 · 07 17 · 08 18 =
**165** + 13 campos del B01 + 12 meses = 190 en el censo. Código común: sin tocar.

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `seafood-restaurant-checklist-templates` (libre) → `/en/digital-products/seafood-restaurant-checklist-templates`; JWT `seafood-restaurant-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_SEAFOOD_RESTAURANT_CHECKLISTS_KIT`; familia `kit-tareas-marisqueria` |
| D2 | Nombre y title | **Seafood Restaurant Checklists Kit Pro**; title SEO = H1: «Seafood Restaurant Checklists Kit Pro: **Raw Bar, Receiving & Opening** Checklist Templates for Excel». DataForSEO US (31-oct): seafood restaurant **301.000**, fish market 165.000, seafood market 90.500, oyster bar **74.000**, raw bar **9.900** (intención local: el oficio), restaurant opening checklist 260, raw bar setup 30; seafood restaurant checklist / opening checklist / shellfish tag log / seafood receiving log sin volumen. «Seafood restaurant» (el comprador) en el nombre; raw bar, receiving y opening, lo que el kit tiene y la SERP busca |
| D3-D4 | Precio | **$15 USD** (molde plano), pago único, sin anclas |
| D6 | Pestañas | Opening & Closing · Live Tank & Receiving · HACCP & Traceability · Raw Bar & Display · Manager Tasks · Duties by Role · Weekly & Monthly · Seasons & Events · Blank Template · Pre-Shift Meeting · Annual Calendar |
| D8 | Glosario | base + **107** (1 sobrescribe: Barra → **Raw bar**): vivero → **live tank**, cámaras → **walk-ins**, lonja → **Buying** / proveedor → **Receiving** (columna A del 02), partidas → **Fish station / Shellfish station / Sauce station / Stock station**, maître → **FOH manager**, jefe cocina → **Head chef**, plancha (puesto) → Griddle cook, PCC → **CCP**, frecuencias y antelaciones |
| D9 | Horas | 30 horas → `hora_us`; la del 01 B36 («antes de 23:30») la escribe el traductor (11:30 PM) |
| D10 | Seguridad (FDA Food Code 2022) | Recepción: fresco 41 °F, congelado 0 °F y duro; **shellstock según NSSP** (en hielo o transporte a 45 °F de aire / 50 °F interna) y luego 41 °F (**3-202.11**). Moluscos de la **ICSSL / NSSP** (**3-201.15**) con su etiqueta **90 días** (**3-203.12**). Expositor sobre **hielo escurrido** (3-303.12), el hielo no es ingrediente (3-303.11), 41 °F (3-501.16). Cocción **145 °F 15 s** (3-401.11; el ES dice 63 °C). Crudo: **parásitos 3-402.11 + registro 3-402.12 + aviso al consumidor 3-603.11** (sustituye al RD 1021/2022). Descongelación 3-501.13 (ROP fuera de la bolsa). **Histamina**: siempre frío, rechazar lo que llegue caliente, la cocción no la destruye (FDA Hazards Guide cap. 7; **sin cifra**). Date marking 7 días para lo cocinado; las «48 h» del ES = estándar de la casa |
| D10b | Vivero | Temperatura del agua **sin las cifras del ES** (8-12 °C bogavante europeo, 14-18 °C langosta: no valen para las especies US): «per your supplier and the tank maker's spec» + lectura en °F; oxígeno, salinidad y pH del ES se quedan (no son °C). Tanque de exposición de **moluscos solo con variance y HACCP plan** del health department (sin número de sección: no verificado) |
| D11 | Alérgenos | **Pescado y crustáceos** son de los 9 US; **los moluscos NO** (se dice si preguntan); UK: los 14 incluyen moluscos; fuera la numeración UE «2 / 14» y los símbolos UE; aviso escrito 3-602.12(C) |
| D12 | Compras | **Lonja → seafood distributor / dock-to-door supplier** (nunca «auction»); producto de lonja → **market price (MP)**; zona FAO → harvest area / origin; Reglamento UE → **FDA Seafood List** (nombre de mercado); origen en la carta = estándar de la casa (no es obligatorio a un restaurante salvo ley estatal); pesca ilegal → **IUU seafood**; vedas por comunidad → seasons and closures de tu estado (agencia estatal, NOAA Fisheries); talla mínima, la del estado |
| D13 | Caja y alcohol | Sin caja (`HOJA_CAJA = None`): 01 B37 (cash count, over/short, tip pool sin managers, 29 U.S.C. 203(m)(2)(B)). Vinos (Albarino sin eñe, Godello, Txakoli) con licencia del local, 21+ con ID (23 U.S.C. 158) |
| D14 | Calendarios | **08**: temporadas de España (centollo gallego, percebe, cigalas de Huelva…) → temporadas US **orientativas** («dates vary by state»: crawfish, soft-shell crab, wild salmon, lobster, stone y king crab, bay scallops, oysters, shrimp); Navidad → **Christmas Eve (Feast of the Seven Fishes)**, Nochevieja → NYE (seafood towers), Semana Santa → **Lent Fridays**, fiestas locales → oyster & seafood festivals, verano → patio + raw bar. **B02**: A, B (producto de temporada US) y C (eventos US) fijados; D y E traductor |
| D15 | Marca y versión | A1 → «AI Chef Pro»; línea «AI Chef Pro · aichef.pro · Seafood Restaurant Checklists Kit Pro»; docProps «· v1.1»; US Letter |
| D-LEX | Prohibidos | plancha, **mariscada** (→ seafood tower / platter / feast), **lonja**, **vivero**, **auction**, workshop, obrador, food truck, window staff, butane, «allergen 2 / 14», MOD. «Restaurant» sí (es un restaurante) |
| D-UK | UK | Solo en la FAQ de la landing: 14 alérgenos (moluscos incluidos), 8 °C / 63 °C |

## 2. Ficheros (D5)

| # | Fichero ES | Fichero EN |
|---|---|---|
| 01 | `01-apertura-cierre-marisqueria.xlsx` | `01-seafood-restaurant-opening-closing-checklist.xlsx` |
| 02 | `02-vivero-lonjas-pescado.xlsx` | `02-live-tank-seafood-receiving-checklist.xlsx` |
| 03 | `03-trazabilidad-appcc-marisco.xlsx` | `03-seafood-haccp-traceability-shellfish-tags.xlsx` |
| 04 | `04-expositor-barra-mariscos.xlsx` | `04-raw-bar-seafood-display-checklist.xlsx` |
| 05 | `05-tareas-manager.xlsx` | `05-seafood-restaurant-manager-checklist.xlsx` |
| 06 | `06-tareas-perfiles.xlsx` | `06-seafood-restaurant-duties-by-role.xlsx` |
| 07 | `07-semanales-mensuales.xlsx` | `07-seafood-restaurant-weekly-monthly-checklist.xlsx` |
| 08 | `08-eventos-estacionales.xlsx` | `08-seafood-seasons-events-checklist.xlsx` |
| 09 | `09-plantilla-personalizable.xlsx` | `09-blank-seafood-restaurant-checklist-template.xlsx` |
| B01 | `BONUS-01-briefing-servicio.xlsx` | `BONUS-01-seafood-pre-shift-meeting-template.xlsx` |
| B02 | `BONUS-02-calendario-anual.xlsx` | `BONUS-02-seafood-restaurant-annual-calendar.xlsx` |

## 3. Reglas del delta (`REGLAS_US` = base + 14; 44 en total)

| Concepto | Fuente |
|---|---|
| Cocción 145 °F 15 s · descongelación · hielo de expositor · aviso escrito de alérgenos | FDA Food Code 2022 §3-401.11(A)(1); §3-501.13; §3-303.11, §3-303.12; §3-602.12(C) |
| Recepción (shellstock NSSP 45 °F aire / 50 °F interna) · moluscos de la ICSSL · etiquetas 90 días | §3-202.11 (B); NSSP Guide (ISSC); S.C. Code Regs. 61-25 §3-202 · §3-201.15 · §3-203.12 (base) |
| Parásitos + registro · aviso al consumidor | §3-402.11, §3-402.12, §3-603.11 (base) |
| Histamina | FDA Fish and Fishery Products Hazards and Controls Guidance, cap. 7 (sin cifra) |
| Tanque de moluscos con variance · moluscos no alérgeno US · nombre de mercado | [local] variance del health department · FALCPA + FASTER Act; Food Information Regulations 2014 (UK) · FDA, The Seafood List |
| Propinas · 21 años · temporadas US · calendario | 29 U.S.C. 203(m)(2)(B) · 23 U.S.C. 158 · [criterio del kit] + agencias estatales / NOAA Fisheries · 5 U.S.C. 6103 (base) |

°F permitidos (G7): −31, −4, 0, 41, 45, 50, 70, 100, 135, 145, 165. 14 celdas ES con °C: por ADAPTAR o POR_CELDA.

## 4. Memoria de traducción (`MEMORIA`: food truck, bakery, base)

**465 cadenas** (944 apariciones); **GM 244** (758 palabras: 11 pestañas, glosario, 89 `POR_CELDA`, 30 horas, marca,
pie, docProps). De las **221 a traducir: 8 heredadas** (exactas; 4 de la panadería y 4 del food truck; 14 palabras) y
**213 pendientes** (todas nuevas; **1.311 palabras**; 57 ADAPTAR): **G1 97 / 665** (01-04) y **G2 116 / 646** (05-B02).
Traducidas en esta sesión (`textos_en/G1.json`, `21c128c3`).

## 5. Erratas del ES (para su v2.0)

- Tildes quitadas en todo el kit (95 celdas, SPEC CB §2.1); el B01 B23 sí lleva «albariño» con eñe.
- 03 B20 y 06 B14: cocción «≥ 63 °C» en pescados y mariscos (el ES no cita fuente; la EN va a 145 °F, 3-401.11).
- 01 B11 y 04 B10 dicen «obligatorio por ley» el origen y el precio por especie sin citar la norma.
- 05 sin el desplegable ✓ / — / N/A; 09 sin desplegable ni CF.
- La landing ES promete «arqueo» y un 01 de cierre completo (SPEC CB §2.2): el cierre de caja es una tarea (01 B37).
