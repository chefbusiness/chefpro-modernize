# Pastry Shop Checklists Kit Pro — SPEC DELTA (F1 · 24-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas Pastelería** (`kit-tareas-pasteleria`, 15 xlsx v2.0/2.1, 429 tareas).
> Noveno hermano vertical: **lo que no está aquí es la SPEC base** (`../SPEC.md` §0-§9). Mapas: `mapas_pastry.py`
> (importa `../mapas.py`). Tamaño S con 4 libros más. 62 hojas. **Molde base sin protección** (censo): el 01-07 y el B01
> con las columnas del base (Nº · Tarea · Zona · Responsable · Hora Límite · ✓ Completada · Firma; el 02 añade
> «Parámetro / Objetivo»), horas precargadas, CF `$F5="✓"` / `$G5="✓"` sin cabeceras internas y línea de marca; **0 hojas
> protegidas** en los 15 libros. El 09 es **propio** (otra maqueta, §1 D12). Los libros 10-13 no existen en ningún
> hermano. Dominio de referencia: la guía EN `../../guia-pasteleria-en/` (F1-research-us.md §3, §7, §8, §13).

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `pastry-shop-checklist-templates` → `/en/digital-products/pastry-shop-checklist-templates` (+ `/access`, `/library`); productId = slug; JWT `pastry-shop-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_PASTRY_SHOP_CHECKLISTS_KIT`; ficheros en `dl/pastry-shop-checklist-templates/` |
| D2 | Nombre | **Pastry Shop Checklists Kit Pro**; title SEO = H1: «Pastry Shop Checklists Kit Pro: Opening, Closing & Cake Order Templates» (72). Sin «— Pastelería / Obrador» (60 apariciones) ni «Pastelería con Tienda» |
| D3-D4 | Precio | **$19 USD**, pago único; sin `priceOld`, «% off» ni anclas («One-time payment · lifetime access · updates included») |
| D5 | Ficheros | §2. Demanda US (§R): pastry shop 40.500 · cake order form 480 · allergen chart 320 · food temperature log 320 · bakery order form 260 · temperature log sheet 210 · receiving log 140 · pastry chef duties 110; «bakery/pastry shop checklist» 0-30 (como los hermanos). Los libros 10-13 llevan su intención propia en el nombre |
| D6 | Pestañas | Kitchen Opening / Closing · **Doughs & Fermentation · Creams & Fillings · Decorating & Finishing** · Manager Daily / Weekly / Monthly · Shift Handover · **Head Pastry Chef · Pastry Cook · Pastry Assistant · Counter Associate** · Weekly Deep Clean · Monthly Maintenance · **Weekly Inventory** · **Holiday Season · Valentine's Day · Easter · Mother's & Father's Day · Celebration Cakes (Apr-Jun) · Thanksgiving (Nov)** · By Time of Day / By Area / By Role · Shop Opening / Closing · caja · **Weekly Plan · Made vs Sold · Summary by Category · Order Form · Order Log · Pickup Schedule · Today's Orders · Allergen Matrix · Allergen Chart · Case Sign · Case Labels · Temperature Log · Receiving Log · Prep Labels · Shelf Life** · Pre-Shift Huddle · Holiday Calendar. Los textos citan libros como «→ 13 Registro de Temperaturas · hoja X»: `CITAS_LIBRO` + `HOJAS_CITADAS` (pista al traductor) |
| D7 | CF | Sin cambios en el 01-09 (CF `$F5="✓"` sin cabeceras internas: no hace falta `CF_POR_CELDA` de «hecho»). **Desviación declarada:** 7 reglas del 13 con el umbral en °F (`CF_POR_CELDA`: cámara 32-41 °F, cámara de masas 36-41 °F, congelador > 0 °F, vitrinas 32-41 °F, abatidor > 70 °F a las 2 h, recepción > 41 °F). Fechas `dd/mm/yyyy` → `mm/dd/yyyy` (394 celdas, `FORMATOS_EN`) |
| D8 | Glosario | base + 140 celdas: zonas (Obrador → **Kitchen**, Vitrina → **Bakery case**, Despacho → Counter, Tienda → Shop, Horno → Ovens), puestos (Jefe Pastelero → **Head pastry chef**, Pastelero → Pastry cook, Ayudante → **Pastry assistant**, Dependiente → **Counter associate**, Encargado → **Shift lead**), cuándo (Continuo → Ongoing, Recepción → On delivery, «N sem antes» → «N weeks out»), fechas del 06, categorías y **referencias del 10 y el 12** (mismo texto en las dos hojas; en `CLAVES` también, para el desplegable, el SUMIF y el G6 de la carta), los 14 alérgenos, las etiquetas del 13 |
| D9 | Horas | Las 220 horas de 24 h → `hora_us` sin desplazar (obrador desde las 5:00 AM, tienda de 8:00 AM a 8:00 PM: horario normal de una bakery US); las 7 horas dentro de frase (07 cabeceras, 08 B7-B8), el traductor |
| D10 | Orden y erratas | El 01 y el 08 ya vienen en el orden real (v2.1: alarma y llave al final; vitrinas 45 min antes de montar). Erratas ES corregidas en la EN (§5): zonas mal puestas en el 06 (`POR_CELDA`), «más de dos horas, valóralo» (13), mousses con merengue crudo (02, ADAPTAR) |
| D11 | 05 | El ES no trae «Trimestral y Anual» ni servicios contratados: sin `POR_CELDA` de NFPA/OSHA/EPA. Solo ADAPTAR: filtros de campana (conductos por empresa certificada si se cocina con grasa, NFPA 96), báscula legal para el comercio, termostato del horno sin cifras, sonda contra display (41 °F) |
| D12 | Caja | **09 propio**: billetes en A21:C27, monedas A29:C36, total C37, resumen A39:B47, fondo en «Apertura de Caja»!C17; «Registro Mensual» C = **ventas en efectivo netas** (ya sin el fondo). Mismas 15 denominaciones US que el base en sus filas (`DENOMINACIONES`, `FORMULAS_POR_CELDA`), rótulos y resumen del base adaptados a estas celdas (`POR_CELDA`), `CASOS_G5` (204.91; 200 / 1,250 / 3,000 / 150 / Z 4,200 → 4,200 y 0), `CELDA_CACHE_MAL = 'B43'`, `LIBROS_SIN_MARCA = ('09',)` (el ES no trae la línea de marca) |
| D13 | Moneda | 945 formatos con € → `#,##0.00`; textos con € → rótulos fijados (09, 10 «Unit cost», 11 importes) o «in your currency» |
| D14 | Calendario y 06 | B02 (filas 4-20, cronológico; las variables al final como el ES): Three Kings Day & King cake (Jan 6 → Mardi Gras) · Valentine's · **Pi Day & St. Patrick's** (sustituye al Día del Padre) · Easter · **Mother's Day (2.º domingo de mayo, pico)** · First Communions & graduations (May–Jun) · Summer + July 4 · Halloween · **Day of the Dead & Thanksgiving (pies: pico)** · Black Friday & Small Business Saturday · **Christmas (pico)** · New Year's Eve · local · **Wedding season (May–Oct)** · corporate · birthdays · showers. B, D y F fijados; E y G, ADAPTAR. 06: Navidad → «Holiday Season» con la sección de Reyes → **Three Kings Day (rosca de Reyes / King cake; el muñequito aparte)**; Semana Santa → **Easter** (hot cross buns, Easter breads, carrot cake); Día Madre-Padre → Mother's & Father's Day (fechas US); Comuniones → **Celebration Cakes** (First Communion, graduaciones, showers: el flujo de tarta de pisos, prueba, depósito y montaje, como la guía EN ch. 16); Todos los Santos → **Thanksgiving (pies; plazos relativos al 4.º jueves, `POR_CELDA`)** |
| D-PAS | Cifras de proceso | °C → °F redondeado al grado; hornos a los escalones US (350, 375-400, 450-480 °F); pesos oz (g); espesores in (mm); harina W → bread flour (12,5-13,5 % proteína), mantequilla 82 % de grasa [criterio del kit]. Columna «Target / Spec» del 02 fijada en `POR_CELDA` (31 celdas) |
| D-PAS | Seguridad alimentaria | Vitrina refrigerada **41 °F o menos** para lo TCS (3-501.16; sustituye al RD 1021/2022 art. 4.1); enfriado de cremas **135 → 70 °F en 2 h y → 41 °F en 4 h más** (3-501.14); date marking **7 días** máximo legal y **24 h como objetivo del kit** en lo elaborado con huevo (3-501.17; sustituye al «tope legal» del art. 9.3); merengue cocido o claras pasteurizadas en lo que no se hornea (3-302.13); recepción 41 °F, **huevos con cáscara en aire a 45 °F**, leche hasta 45 °F si la ley lo permite y enfriada a 41 °F en 4 h, congelado sin descongelar (3-202.11, 3-501.14); más de 2 h por encima de 41 °F o tiempo desconocido → a la basura [criterio del kit], 4 h solo con procedimiento escrito (3-501.19); sanitizante con tira (4-501.114); calibración por punto de hielo (32 °F) |
| D-PAS | 10 Plan de producción | Referencias de ejemplo → pastry shop US (Butter croissant, Custard danish, Concha, Pain aux raisins, Palmier, Cheesecake, Apple pie, Napoleon, Eclair, Carrot cake, Sourdough boule, Baguette, Muffin, Pound cake…); categorías Viennoiserie · Cakes & pastries · Bread · Savory · Cookies & small cakes (= `CLAVES`). Desplegable «Action» con su condición en °F; nota: lo expuesto no se congela, «dilo si estuvo congelado» [criterio del kit: sin obligación federal para lo sin envasar] y donación con la **Bill Emerson Good Samaritan Food Donation Act** (42 U.S.C. 1791) |
| D-PAS | 11 Encargos | Depósito 30-50 % y política de cancelación = **práctica habitual, no ley** (guía EN §8); tamaño en pulgadas; forma de pago Cash · Card · Zelle / Venmo · Bank transfer · Not paid yet; canal In store · Phone · Text / WhatsApp · Website · Other; alérgenos del cliente: los 9 de EE. UU. + gluten (celíacos) + sulfitos + celery / mustard / lupin-mollusks (UK). **Sin RGPD**: aviso de privacidad US [criterio del kit] (solo lo necesario, consentimiento de alergias aparte del de marketing, ninguno premarcado, destruir al mes); marketing por SMS con consentimiento escrito (TCPA, 47 CFR 64.1200) y email con baja (CAN-SPAM) |
| D-PAS | 12 Alérgenos | Las 14 columnas se quedan con sus símbolos: los 9 de EE. UU. en sus mismas columnas (Gluten → **Wheat (gluten)**, Crustáceos → **Shellfish**…), sulfitos (se declaran desde 10 ppm, 21 CFR 101.100(a)(4)) y Celery / Mustard / Lupin / Mollusks **(UK)**; cada referencia EN tiene el **mismo perfil de alérgenos** que la ES (Ensaimada → Concha; Roscón → Three Kings bread; Torrijas → Hot cross buns; Huesos de santo → Amaretti; Panellets → Pignoli; Turrón → torrone; Polvorón → Polvorones con nota de la leche). Base legal: **FALCPA + FASTER Act** y **FDA Food Code 2022 §3-602.12(C)** (aviso escrito en lo sin envasar, donde el estado lo adopte; guía EN §3.1 [OF]); UK FIR 2014. Cabeceras giradas 90° en 95 pt: ≤ 15 caracteres |
| D-PAS | 13 Registros | Cabeceras y CF en °F (D7); albarán → invoice / packing slip; etiquetas «Made (date & time) · Use by (date & time) · Batch # · Made by»; vidas útiles con su conservación en °F y las notas legales US |
| D-PAS | Personal de temporada | 06 «Holiday Season» B9: menores de 18 sin amasadoras, batidoras industriales, laminadoras ni divisoras, ni limpiarlas (**29 CFR 570.62, HO 11**; salvo batidoras de sobremesa ≤ 5 quarts); 14-15 años, **nada de hornear** (29 CFR 570.33(h); DOL Fact Sheet #58) |
| D-PAS | Lecciones de los hermanos | tiras de sanitizante (01) · enfriado 3-501.14 solo donde aplica (cremas, abatidor) · 3-501.19 bien citado · date marking · CF sin cabeceras internas (no aplica: molde base) · `AJUSTE_MAQUETA_ES` · calendario cronológico · «N weeks out» · `TERMINOS_PROHIBIDOS` (dining room, host stand, server, bartender, cocktails, beer, liquor, barista, coffee shop, busser, head / sous chef, line / prep cook, banquet, BEO, line-up, pizza, burger, ghost kitchen, packer, app manager, ice cream shop, dipping cabinet, batch freezer, scooper, MOD, FOH, GM, «restaurant» salvo consultant / supply; permitidos: venue, cookie scoop, coffee machine) · inventario: **sin mínimos numéricos** en el ES (la deuda `adf52a52` del G4 no aplica, `VALORES_EN` vacío) |
| D-UK | UK | nota UK en el B02 (Mothering Sunday, bank holidays, Boxing Day); 14 alérgenos en el 11 y el 12; 8 °C / −18 °C y FIR 2014 en la FAQ de la landing (F3) |

## 2. Ficheros (D5)

| # | Fichero ES | Fichero EN | Título EN |
|---|---|---|---|
| 01 | `01-apertura-cierre.xlsx` | `01-pastry-kitchen-bakery-case-opening-closing-checklists.xlsx` | Pastry Kitchen & Bakery Case Opening and Closing Checklists |
| 02 | `02-partidas-cocina.xlsx` | `02-pastry-kitchen-production-checklists.xlsx` | Pastry Kitchen Production Checklists: Doughs, Creams & Fillings, Decorating |
| 03 | `03-tareas-manager.xlsx` | `03-pastry-shop-manager-checklist.xlsx` | Pastry Shop Manager Checklist: Daily, Weekly, Monthly & Shift Handover |
| 04 | `04-tareas-perfiles.xlsx` | `04-pastry-chef-duties-by-role.xlsx` | Pastry Chef Duties by Role: Head Pastry Chef, Pastry Cook, Assistant & Counter |
| 05 | `05-tareas-semanales-mensuales.xlsx` | `05-bakery-cleaning-schedule-maintenance-inventory.xlsx` | Bakery Cleaning Schedule, Equipment Maintenance & Weekly Inventory |
| 06 | `06-eventos-festivos.xlsx` | `06-pastry-shop-holiday-event-checklists.xlsx` | Pastry Shop Holiday & Event Checklists: Holidays, Valentine's, Easter, Mother's Day, Celebration Cakes & Thanksgiving |
| 07 | `07-plantilla-personalizable.xlsx` | `07-blank-pastry-shop-checklist-template.xlsx` | Blank Pastry Shop Checklist Template (Editable) |
| 08 | `08-apertura-cierre-negocio.xlsx` | `08-pastry-shop-opening-closing-checklist.xlsx` | Pastry Shop Opening & Closing Checklist (Whole Shop) |
| 09 | `09-apertura-cierre-caja.xlsx` | `09-cash-drawer-opening-closing.xlsx` | Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log |
| 10 | `10-plan-produccion-semanal.xlsx` | `10-bakery-production-schedule-waste-log.xlsx` | Bakery Production Schedule & Waste Log: Weekly Plan, Made vs. Sold & Summary |
| 11 | `11-control-encargos.xlsx` | `11-cake-order-form-order-log.xlsx` | Cake Order Form & Custom Order Log: Order Form, Log, Pickups & Today's Orders |
| 12 | `12-control-alergenos-vitrina.xlsx` | `12-bakery-allergen-chart.xlsx` | Bakery Allergen Chart (9 Major Allergens, UK 14): Matrix, Chart, Case Sign & Labels |
| 13 | `13-registro-temperaturas-recepcion.xlsx` | `13-food-temperature-log-receiving-log.xlsx` | Food Temperature Log, Receiving Log, Prep Labels & Shelf Life Chart |
| B01 | `BONUS-01-briefing-servicio.xlsx` | `BONUS-01-pastry-shop-pre-shift-meeting-template.xlsx` | BONUS: Pastry Shop Pre-Shift Meeting Template (Huddle Notes) |
| B02 | `BONUS-02-calendario-anual-tareas.xlsx` | `BONUS-02-pastry-shop-holiday-calendar.xlsx` | BONUS: Pastry Shop Holiday & Events Calendar (US) |

## 3. Reglas del delta (`mapas_pastry.REGLAS_US` = las del base que aplican + estas)

Fuera del base (no aplican a este ES): parásitos, moluscos, recalentado, aviso al consumidor, campana NFPA 96 / extinción,
EPA 608, fichajes y frecuencia de nómina, backflow, grasas, extintores, lavado de vegetales, joyas, enfermos, lavamanos.

| Concepto | Fuente |
|---|---|
| Vitrina 41 °F (TCS: cremas, nata, cheesecake, pies de crema) · enfriado 135 → 70 °F / 2 h → 41 °F / 4 h | FDA Food Code 2022 §3-501.16(A)(2), §1-201.10; §3-501.14 |
| Date marking 7 días (24 h = objetivo del kit con huevo) · huevo pasteurizado o merengue cocido | §3-501.17; [criterio del kit]; §3-302.13 |
| Recepción 41 °F · huevos 45 °F de aire · leche 45 °F y a 41 °F en 4 h · congelado, congelado | §3-202.11(A), (B), (C), (E); §3-501.14 |
| Tiempo como control (4 h con procedimiento escrito) · regla de 2 h del kit | §3-501.19; [criterio del kit] |
| Aviso escrito de alérgenos en lo sin envasar · formación en alergias | §3-602.12(C) (donde el estado lo adopte); §2-103.11(O) |
| 9 alérgenos · sulfitos ≥ 10 ppm · «may contain» voluntario y veraz | FALCPA + FASTER Act; 21 CFR 101.100(a)(4); FDA (advisory labeling) |
| Donación de buena fe | 42 U.S.C. 1791 (Bill Emerson Good Samaritan Food Donation Act) |
| Menores: máquinas de panadería (HO 11) · 14-15 años sin hornear | 29 CFR 570.62; 29 CFR 570.33(h); DOL Fact Sheet #58 |
| Marketing por SMS / email | 47 CFR 64.1200 (TCPA); 15 U.S.C. 7704 (CAN-SPAM) |
| Báscula legal · conductos de campana si hay grasa | [estatal] pesas y medidas, NIST Handbook 44; NFPA 96, [local] |
| Fechas US | 36 U.S.C. 117 y 109; 5 U.S.C. 6103; guía EN §7 (King cake / rosca, Pi Day, Day of the Dead) |
| Depósito 30-50 %, food cost 28-35 %, merma 3-8 % · conversión de cifras · muñequito aparte | [criterio del kit]; guía EN §8 |

°F que el kit puede afirmar (G7, `GRADOS_F_SPEC` = las cifras °F de los textos de mapas, comprobado con `gates_en.permitidas`):
0, 32, 36, 37, 39, 41, 43, 45, 54, 57, 64, 68, 70, 72, 75, 77, 79, 82, 84, 86, 88, 90, 95, 99, 113, 122, 135, 175, 180,
183, 185, 244, 250, 320, 325, 340, 350, 375, 400, 450, 480. `CELSIUS_SIN_F` vacío: los 72 textos con °C llevan su °F.

## 4. Memoria de traducción (`../heredar.py --kit pastry`, `MEMORIA`: cafetería, base, heladería, catering, pizzería, hamburguesería, ghost kitchen y bar)

1.361 cadenas; **GM 478** (1.689 palabras: pestañas, glosario, claves, 203 `POR_CELDA`, 220 horas, marca, versión). De
las 883 a traducir: **63 heredadas** (58 exactas + 5 por sufijo; 32 de la cafetería, 28 del bar, 2 de la heladería y 1
del base; 329 palabras) y **820 pendientes** (813 nuevas, 3 «contexto», 4 con otro ADAPTAR; **8.184 palabras**; 197
con ADAPTAR): **G1 457 cadenas / 3.653 palabras** (comunes + 01-07) y **G2 363 / 4.531** (08-13 y bonus). El orden de la
memoria apenas cambia nada (63-64): el ES pastelería está reescrito y casi todo es nuevo. **Propuesta: DOS traductores
sonnet**, G1 primero (fija la prosa) → `textos_en/G1.json`; G2 después con el glosario del G1 → `textos_en/G2.json`
(`aplicar_en` lee todos los `G<n>.json`). Cada uno: sus ids de `pendientes.json` (campo `grupo`), esta SPEC, `GLOSARIO`,
`HOJAS`, `CITAS_LIBRO`, `REGLAS_US` y `heredado.json`.

    python3 extraer_textos.py --kit pastry && python3 pastry/mapas_pastry.py && python3 heredar.py --kit pastry
    python3 aplicar_en.py --kit pastry --dry-run [--parcial] --idempotencia --mes October; python3 gates_en.py --kit pastry [--parcial] --dir <carpeta> [--autotest]

**Prueba de humo F1** (dry-run `--parcial` en el VPS): `aplicar_en` monta los 15 libros (12 s, `inject_cache` sin
fallos); gates G1, G2, G4, G5 (2 casos, 9 comprobaciones), G6, G7 y G8 en verde; **G3 rojo por 2 celdas**: «Celery (UK)»
en el 12 (K4 de la matriz, J5 de la carta). Es un falso positivo: las cabeceras de alérgenos van **giradas 90°** en una
fila de 95 pt y `objetivo_ajuste` mide el ancho (5) sin mirar `textRotation` (el ES «Apio» cabía en horizontal; el resto
ya desbordaba en el ES y se trata como maqueta heredada). El `--autotest` no corre hasta que la carpeta base esté limpia.
**Para la F2** (código común, cambio mínimo y comprobado con el dry-run de los hermanos): en `objetivo_ajuste`, las celdas
con `textRotation` se miden contra el alto de la fila o se saltan; y `_bloquear_verde` (mutación G1 del autotest) necesita
una celda verde desbloqueada y **este ES no tiene ninguna** (0 hojas protegidas, 0 desbloqueadas): o la mutación se salta
cuando el censo trae 0 desbloqueadas, o se declara otra.

## 5. Erratas del ES (para su próxima v2.x; la EN nace corregida)

- 06 «Semana Santa» C8: «Producción de figuras de chocolate» con zona **Admin** (es obrador); 06 «San Valentín» C17 y
  «Día Madre-Padre» C14: «Reforzar despacho» con zona **Obrador** (es vitrina). La EN los corrige por celda.
- 13 «Registro de Temperaturas» A40: «más de dos horas fuera de rango, valóralo antes de venderlo» es vago; la EN:
  más de 2 h por encima de 41 °F o tiempo desconocido → se tira.
- 10 desplegable «Acción»: «abatido antes de −18 °C» (se entiende «abatido a −18 °C»).
- 02 «Cremas y Rellenos» B15-B16: mousses con «merengue» sin decir que sea cocido o de claras pasteurizadas.
- 03 «Semanal Manager» E25 y 04 «Jefe Pastelero» E9: «Recepción» en la columna de hora (se lee «a la recepción»).
- Versiones mezcladas (2.0 agosto / 2.1 septiembre) entre libros del mismo kit.
- 06 «Instrucciones» B5: «hasta el 40 % de su año» sin fuente (la EN no da la cifra).
- **RESUELTAS en el ES LIVE (ronda 1 de la F2, 24-oct-2026, parche XML sin cambio de versión; la EN las hereda):**
  - 09 «Instrucciones»: área de impresión `A1:A20` (el texto va en la B) → `A1:B30`.
  - 09 «Registro Mensual»: área `A1:I38`, sin la J «Responsable» → `A1:J38`.
  - 09 «Cierre de Caja»: los rótulos del Resumen de Cierre (A41-A46) no cabían en la columna A de 5 → A = 24 y
    B = 31 (el ancho impreso no cambia).
  - 02 «Cremas y Rellenos» C8: almíbar a 118-121 °C también para el merengue suizo → «Italiano: almíbar a
    118-121 °C · suizo: claras y azúcar a 71 °C · mantequilla a 18-20 °C».
  - Las mismas correcciones, en `scripts/productos-digitales/kit-pasteleria-v2_0-postprocess.py`.

## R. Research (una pasada, 24-oct-2026)

**Demanda (DataForSEO, US, 2840/en):** pastry shop 40.500 · bakery case 590 · cake order form 480 · allergen chart 320 ·
food temperature log 320 · bakery order form 260 · temperature log sheet 210 · receiving log 140 · pastry chef duties 110
· food prep labels 70 · custom cake order form 50 · cake order template 40 · bakery opening checklist 30 · shelf life
chart 20 · bakery manager duties 20; bakery checklist / cleaning checklist / cleaning schedule / production schedule /
production plan / inventory sheet / allergen chart template 10; bakery closing checklist y bakery waste log sin dato. De
la orquestación: pastry shop business plan 1.600 · how to open a bakery 720 · how to start a bakery business 480.
**Jerga US** (alta en `../../GLOSARIO-JERGA-ES-EN.md`, sección Pastelería; base: guía EN §13.1): pastry kitchen · bakery
case · counter associate · head pastry chef · pastry cook · shift lead · viennoiserie · retarder / retarder-proofer ·
blast chiller · dough sheeter · spiral / planetary mixer · deck / convection oven · sheet pan · piping bag · bench prep ·
custom order · pre-order · deposit · balance due · pickup slot · cake message · day-old · waste log · recipe costing ·
spec sheet · invoice · date marking · cross-contact. **Delicado, comprobado:** 3-602.12(C) y 2-103.11(O) (guía EN §3.1,
PDF leído); 3-202.11 (A)-(E) (`restaurant-inventory-kit/mapas.py`); HO 11 = 29 CFR 570.62 (texto en eCFR / FindLaw) y
14-15 años sin hornear = 29 CFR 570.33(h) (Cornell LII) + DOL Fact Sheet #58; 3-302.13 (texto reproducido por la regla
de Minnesota 4626.0245). **Testimonios y marcas reales** (para la F3; no se tocan en F1): `kit-tareas-pasteleria.ts`
(testimonios de la landing) y `src/data/testimonials-pasteleria.ts` (10, marquee) citan marcas reales: **Hotel Meliá
Valencia, Grupo Europastry, Escuela Hofmann**; el resto son obradores genéricos. Decidir en F3 como en los hermanos.
