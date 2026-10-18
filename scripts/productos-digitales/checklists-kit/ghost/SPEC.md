# Ghost Kitchen Checklists Kit Pro — SPEC DELTA (F1 · 18-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas para Dark Kitchen** (`kit-tareas-dark-kitchen`, 11 xlsx v2.0).
> Sexto hermano vertical (como el bar, la cafetería, el catering, la pizzería y la hamburguesería): **lo que no está aquí
> es la SPEC base** (`../SPEC.md` §0-§9). Mapas: `mapas_ghost.py` (importa `../mapas.py`). Tamaño S. 43 hojas.

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `ghost-kitchen-checklist-templates` → `/en/digital-products/ghost-kitchen-checklist-templates` (+ `/access`, `/library`); productId = slug; JWT `ghost-kitchen-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_GHOST_KITCHEN_CHECKLISTS_KIT`; ficheros en `dl/ghost-kitchen-checklist-templates/` |
| D2 | Nombre | **Ghost Kitchen Checklists Kit Pro**; title SEO = H1: «Ghost Kitchen Checklists Kit Pro: Cloud Kitchen Opening & Closing Templates» (75; el del brief tenía 113). Sin el sufijo «— Dark Kitchen»; «dark kitchen» nunca en EN (ghost kitchen 33.100/mes, `GLOSARIO-JERGA-ES-EN.md`) |
| D3-D4 | Precio | **$19 USD**, pago único; sin `priceOld`, «% off» ni anclas |
| D5 | Ficheros | §2. Demanda US: cloud kitchen 8.100/mes, virtual kitchen 590, virtual restaurant 390, delivery only restaurant 170; las variantes de checklist sin volumen: los ficheros combinan ghost / cloud / virtual / delivery-only kitchen |
| D6 | Pestañas | **Hot Station** · **Cold Station** · **Packing Station** · Multi-Brand Cook · Packer · **App Manager** · Operations Manager · Daily Inventory · **Friday Night Rush** · Game Night · **Brand Launch** · Holiday Season; 08: **Site Opening / Site Closing** (no hay restaurante abierto al público). El resto, del base |
| D8 | Glosario | base + 36 celdas (3 sobrescriben el base: Auxiliar → **Dishwasher / prep**, Jefe de Cocina → Kitchen manager, Responsable de caja → Cashier / shift manager): Packaging → **Packing**, Operaciones → Operations, Recogida riders → **Driver pickup**, Cocinero caliente / frío → **Hot / Cold station cook**, Empaquetador → **Packer**, Gestor → **App manager**, Encargado/a → Shift manager; cuándo: «2 sem antes» → **2 weeks out**, «Viernes 17:00» → Friday 5:00 PM; kg / L / uds → lb / qt / ea |
| D9 | Horas | 148 horas de 24 h → `hora_us` (12 de la apertura del 08 fijadas en `POR_CELDA`, D10) |
| D10 | Orden | **Erratas ES corregidas** (el 01 ya va campana → gas → equipos; la campana suma «que tire»). 08 «Site Opening» filas 11-22: las impresoras de cada app, el timbre de riders y los tiempos de preparación se comprobaban ANTES de encender las tablets (fila 20), y las marcas se activaban a las 09:30, una hora antes que en el 01 y el 04: local → recogida y empaquetado → tablets (10:00 AM) → impresoras, timbre y tiempos → marcas (10:30 AM). 08 «Site Closing», 15 filas: desactivar las marcas y apagar las tablets iba DESPUÉS de la alarma y la llave, y las persianas se cerraban antes de recoger la señalización: pedidos y riders → marcas y tablets → empaquetado y caja → el local → alarma → puertas → llave. 01 «Kitchen Closing» B14: la campana, la última, con los equipos ya fríos |
| D11 | 05 «Quarterly & Annual» | plagas (heredada), campana + conductos NFPA 96 (**trimestral**: se cocina todo el día), extintores OSHA 1910.157 + extinción + hidrostática, gas, legionela, frío EPA 608, aceite usado (recycler), **cartón y plástico** (hauler), calibración (32 °F), seguros (**products coverage**: se come fuera), contratos y comisiones de las apps + sales tax (marketplace facilitator, según el estado). Sin Verifactu. 03 `B11` = fichajes FLSA (B16 del base) |
| D12 | Caja | 09 igual que el base (`POR_CELDA` y `ADAPTAR` del 09 heredados tras `cruzar_base`) |
| D14 | Calendario | Estructura del base (filas 5-26), días fuertes del delivery US y orden cronológico: Reyes → **Super Bowl** · Carnaval → Mardi Gras · Día del Padre → **Lent Fridays + Easter** · Semana Santa → St. Patrick's + **March Madness** · comuniones → Cinco de Mayo · 1 de mayo → Mother's Day · Día de la Madre → Memorial Day · temporada alta → graduaciones · San Juan → Father's Day · Asunción → **Summer slowdown** (el delivery BAJA en verano: ronda 1 M3) · vuelta al cole → Labor Day + **football season** · Todos los Santos → Thanksgiving + Black Friday · puente → Holiday shopping weekends. Sin alcohol |
| D-GHO | Pase · empaquetado | caliente a **135 °F** o más hasta el empaquetado; frío a **41 °F** o menos; caliente y frío en bolsas separadas hasta la recogida (3-501.16; [criterio del kit]); baño maría → steam table / hot well |
| D-GHO | Cocina | pollo 165 °F · picada 155 °F 17 s · pescado 145 °F 15 s (3-401.11); crudo separado (3-302.11); enfriado en dos fases (3-501.14) y recalentado a 165 °F en 2 h (3-403.11); date marking (3-501.17); salsas caseras 5 días, proteínas 3, vegetales cortados 2 ([criterio del kit]); mayonesa casera: huevo pasteurizado o aviso al consumidor |
| D-GHO | Frío crudo | **pescado crudo (poke, sushi)**: las TRES opciones de 3-402.11 (−4 °F 7 días · −31 °F hasta sólido + 15 h a −31 °F · o + 24 h a −4 °F; ronda 1 M2), registro o declaración del proveedor 90 días (3-402.11/12) y aviso al consumidor en la ficha de la app (3-603.11); el congelador a 0 °F NO cuenta (05 D29); **arroz de sushi**: acidificado solo con varianza + HACCP (3-502.11(D)), o a 41 °F, o TPHC 4 h (3-501.19); lavado de vegetales sin «70 ppm» (3-302.15) |
| D-GHO | Precintos | tamper-evident seals: **California los exige** a la comida lista para consumir que recoge un repartidor de app (AB 3336, desde 2021); el resto, «check local rules» (NYC solo tuvo proyectos de ley) |
| D-GHO | Apps · alérgenos | DoorDash, Uber Eats, Grubhub; comisiones según el plan (≈ 15-30 %), topes en NYC y San Francisco, sin cifras por app. Alérgenos: los 9 de EE. UU. en la ficha de cada app (sin norma federal para restaurantes; check local rules); UK: 14, antes de comprar y al entregar (FSA, venta a distancia). Natasha's Law fuera: el delivery no es PPDS |
| D-GHO | Permisos | un health permit por cocina; las marcas virtuales suelen ir con el de la cocina, según la ciudad; DBA de cada marca si el estado lo pide (06 «Brand Launch» B8) |
| D-GHO | 07 | errata ES: los bloques de SALA y BARRA → **PACKING & PICKUP** y **OFFICE & APPS**; «Por Perfil»: jefe de sala → Packer |
| D-GHO | Lecciones de los hermanos | tiras de sanitizante en 4 tareas (superficies al abrir y al cerrar, estación del cocinero, tablas) · 3-501.19 bien dicho · enfriado en dos fases y recalentado · aviso al consumidor · date marking · aceite: filtrado según el fabricante y cambio según el medidor de TPM, boil-out semanal (ronda 1 M1; `CELSIUS_SIN_F` ×4) · `TERMINOS_PROHIBIDOS` (dining room, dine-in, host stand, server, waitstaff, table service, patio, bar, bartender, cocktails, beer, liquor, barista, cafe, tip jar, busser, head / sous chef, shift lead, MOD, FOH, venue, BEO, line-up, pizzeria, dough; «restaurant», «commissary» y «delivery drivers» permitidos) · CF `$F5="✓"` sin cabeceras internas · `AJUSTE_MAQUETA_ES` · `ALTOS_FILA` (05 FIFO, fila 34) y `AJUSTE_FORZADO` (01 B9), F2 · calendario cronológico · «2 weeks out» · mínimos del inventario en formatos de compra US (5 / 10 lb) |
| D-UK | UK | 14 alérgenos en las celdas de alérgenos; nota UK del B02 heredada; 8 °C / 63 °C en la FAQ de la landing |

## 2. Ficheros (D5)

| # | Fichero EN | Título EN |
|---|---|---|
| 01 | `01-ghost-kitchen-opening-closing-checklists.xlsx` | Ghost Kitchen Opening & Closing Checklists: Kitchen, Packing & Delivery Apps |
| 02 | `02-cloud-kitchen-station-checklists.xlsx` | Cloud Kitchen Station Checklists: Hot Station, Cold Station & Packing |
| 03 | `03-ghost-kitchen-manager-checklist.xlsx` | Ghost Kitchen Manager Checklist: Daily, Weekly, Monthly & Shift Handover |
| 04 | `04-virtual-kitchen-duties-by-role.xlsx` | Virtual Kitchen Duties by Role: Cook, Packer, App Manager & Operations Manager |
| 05 | `05-cloud-kitchen-cleaning-checklist-inventory-maintenance.xlsx` | Cloud Kitchen Cleaning Checklist, Inventory & Maintenance Schedule |
| 06 | `06-ghost-kitchen-peak-and-event-checklists.xlsx` | Ghost Kitchen Peak Checklists: Friday Rush, Game Night, Brand Launch & Holidays |
| 07 | `07-blank-ghost-kitchen-checklist-template.xlsx` | Blank Ghost Kitchen Checklist Template (Editable) |
| 08 | `08-delivery-only-kitchen-opening-closing-checklist.xlsx` | Delivery-Only Kitchen Opening & Closing Checklist (Whole Site) |
| 09 | `09-cash-drawer-opening-closing.xlsx` | Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log |
| B01 | `BONUS-01-ghost-kitchen-pre-shift-meeting-template.xlsx` | BONUS: Ghost Kitchen Pre-Shift Meeting Template (Huddle Notes) |
| B02 | `BONUS-02-ghost-kitchen-delivery-calendar.xlsx` | BONUS: Ghost Kitchen Holiday & Peak Delivery Days Calendar (US) |

## 3. Reglas del delta (`mapas_ghost.REGLAS_US` = las del base + estas)

| Concepto | Fuente |
|---|---|
| Cocción 165 / 155 °F 17 s / 145 °F 15 s · crudo separado · descongelar · TPHC 4 h | FDA Food Code 2022 §3-401.11(A); §3-302.11; §3-501.13; §3-501.19(B) |
| Arroz de sushi acidificado · declaración del proveedor (parásitos) | §3-502.11(D); §3-402.12(B) |
| Pase 135 / 41 °F · mesa fría y date marking | §3-501.16; §3-501.16(A)(2) y §3-501.17 |
| Precintos | California AB 3336 (2020, en vigor el 1-ene-2021); [local] el resto |
| Alérgenos en las apps (US sin norma federal; UK antes de comprar y al entregar) | FALCPA + FASTER Act; Food Information Regulations 2014 (UK) y guía FSA |
| Permisos y DBA · comisiones y topes · sales tax de las apps | [local] / [estatal]; NYC Local Law 2021 y San Francisco; marketplace facilitator laws |
| Plazos 3 / 5 / 2 días, 24 h, 8-12 min, < 30 s · aceite · días fuertes · kg → lb | [criterio del kit]; [fabricante] |

°F que el kit puede afirmar (G7, `GRADOS_F_SPEC`): −31, −4, 0, 32, 41, 70, 100, 135, 145, 155, 165.
## 4. Memoria de traducción (`../heredar.py --kit ghost`, `MEMORIA`: base, bar, cafetería, catering, pizzería y hamburguesería)

855 cadenas; GM 296 (pestañas, glosario, horas, 257 `POR_CELDA`, 32 `VALORES_EN`, marca, versión). De las 559 a
traducir (tras la ronda 1): **199 heredadas** (196 exactas + 3 por sufijo; 1.756 palabras) y **360 pendientes** (335
nuevas, 10 «contexto», 12 con otro ADAPTAR, 3 `NO_HEREDAR`; 2.884 palabras) → UN traductor sonnet → `textos_en/G1.json`.

    python3 extraer_textos.py --kit ghost && python3 ghost/mapas_ghost.py && python3 heredar.py --kit ghost
    python3 aplicar_en.py --kit ghost --dry-run [--parcial] --idempotencia --mes October; python3 gates_en.py --kit ghost [--parcial] --dir <carpeta> [--autotest]

## 5. Erratas del ES (para su próxima v2.x; la EN nace corregida)

- **Para John:** la redacción incompleta de 3-402.11 viene del kit base (LIVE) y del catering → parche puntual en su v2.x:
  base 02 «Cold Station» B10 y «Mise en Place» B10 · cafetería 02 «Hot Line» B9 · catering 01 «Instructions» B16,
  «Production» B34 y 06 «Cocktail Reception» B9. **RESUELTA en esta rama (18-oct-2026):** las 6 celdas, con las 3
  opciones y 3-402.12; cambian 4 xlsx (base 02, cafetería 02, catering 01 y 06), versión 2.0 sin tocar.
- 08 «Apertura del Negocio»: impresoras, timbre y tiempos antes de encender las tablets (B11-B13 vs B20); marcas
  activas a las 09:30 frente a las 10:30 del 01 y del 04. 08 «Cierre del Negocio» B18-B19: marcas y tablets DESPUÉS de
  la alarma y la llave; B9 cierra persianas antes de recoger la señalización (B12) y vaciar papeleras (B14).
- 07 «Por Área» y «Por Perfil»: bloques de SALA y BARRA (y «Jefe de Sala») en una cocina sin público.
- 05 «FIFO Semanal» D29: el congelador normal (−18 °C) no hace la congelación anti-anisakis. Aceite «por debajo de
  40 °C» (01 B13, 03 B12, 05 B14 y B7): manda el fabricante de la freidora.
- 05 «Inventario Diario»: mínimos como TEXTO (la fórmula pide siempre); A45, marca con otro formato; «Instrucciones» B23
  promete hojas protegidas y el inventario no lo está.
- Ronda 1: 01 «Apertura Cocina» B33 y 04 «Gestor» B7 encienden las marcas antes de impresora, cartas y 86; 05
  «Mantenimiento Mensual» B7, cambio de aceite mensual; B02 «Temporada alta» en verano (el delivery baja); 08 alarma a
  las 09:00 frente a las 08:45 del 04; 02 «Estación Fría» B18 (24 h) frente a «FIFO Semanal» B8 (2 días).
