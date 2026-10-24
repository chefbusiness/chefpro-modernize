# Ice Cream Shop Checklists Kit Pro — SPEC DELTA (F1 · 24-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas Heladería** (`kit-tareas-heladeria`, 11 xlsx v2.0, 298 tareas).
> Séptimo hermano vertical (tras el bar, la cafetería, el catering, la pizzería, la hamburguesería y la ghost kitchen):
> **lo que no está aquí es la SPEC base** (`../SPEC.md` §0-§9). Mapas: `mapas_icecream.py` (importa `../mapas.py`).
> Tamaño S. 38 hojas. **Molde híbrido** (censo): el 01-07, el B01 y el B02 van en el molde ligero del catering
> (# · Tarea · Zona · Responsable · ✓ · Hora · Notas, cabeceras internas por sección, sin protección, sin horas ni
> responsables precargados, subtítulo A2); el 08 y el 09, en el del kit base (el 09, idéntico al base salvo la variante).

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `ice-cream-shop-checklist-templates` → `/en/digital-products/ice-cream-shop-checklist-templates` (+ `/access`, `/library`); productId = slug; JWT `ice-cream-shop-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_CHECKLISTS_KIT`; ficheros en `dl/ice-cream-shop-checklist-templates/` |
| D2 | Nombre | **Ice Cream Shop Checklists Kit Pro**; title SEO = H1: «Ice Cream Shop Checklists Kit Pro: Opening, Closing & Production Templates» (74). Sin el sufijo «— Heladería Artesanal». El subtítulo A2 del molde ligero («Kit de Tareas: Heladería Artesanal») va por `GLOSARIO` con el nombre EN, como el catering |
| D3-D4 | Precio | **$19 USD**, pago único; sin `priceOld`, «% off» ni anclas («One-time payment · lifetime access · updates included») |
| D5 | Ficheros | §2. Demanda US (§R): ice cream shop 246.000/mes · ice cream parlor 27.100 · gelato shop 27.100 · scoop shop 4.400 · ice cream catering 1.600; las variantes con «checklist» sin volumen, como en los hermanos: los títulos combinan ice cream shop / parlor / gelato / scoop shop |
| D6 | Pestañas | Opening · Closing · **Pasteurizing** · **Batch Freezing** · Daily / Weekly / Monthly Tasks · **Ice Cream Maker** · **Scooper & Counter** · **Shift Lead** · Weekly Deep Clean · **Weekly Upkeep & Stock** · Quarterly & Annual · **Peak Season** · **Off-Season** · **Ice Cream Catering** · By Area / By Shift / By Role · **Shop Opening / Shop Closing** · cash del base · **Pre-Shift Huddle** · **Seasonal Calendar**. «Tareas Mensuales» sale en el 03 y el 05: «Monthly Tasks» en los dos (únicas por libro) |
| D7 | CF | Desviación declarada (la del catering, ronda 1 M5): en 18 hojas del molde ligero la CF de «hecho» pasa de `$E6="✓"` a `AND($E6="✓",$B6<>"Task")` (las cabeceras internas llevan «✓» en E y se pintaban). `CF_POR_CELDA`; el 07 no (su cabecera queda fuera del rango). `CLAVES` + «Tarea» → «Task» (los contadores restan las cabeceras) |
| D8 | Glosario | base + 23 celdas (5 sobrescriben el base: Sala → **Seating area**, Recepción → **Front counter**, Encargado → **Shift lead**, Responsable de caja → **Cashier / shift lead**, Vida útil → **Shelf life**): Obrador → **Production** · Pasteurizador → Pasteurizer · Mantecadora → **Batch freezer** · Maduración → **Aging** · Abatidor → **Hardening** · Cámara → Freezer · Vitrina → **Dipping cabinet** · Mostrador → Counter · Equipo → Team · Tienda → Shop · Hora → Time · Semestral → Semiannual |
| D9 | Horas | Las 29 horas de 24 h (08 E5-E22, 09 D5-D15) **+3 h** (07:00 → 10:00 AM; puerta a las 11:00 AM): una scoop shop US abre a media mañana [criterio del kit]; mismo orden e intervalos (`HORAS_ES`, `POR_CELDA`; el autotest comprueba +3 h y orden). El 01-07 no trae horas |
| D10 | Orden y erratas | **Erratas ES corregidas** (§5): 08 «Shop Closing», 15 filas reordenadas: clientes y música → patio y señalización → **vitrinas tapadas (siguen encendidas) y temperaturas de cierre** → caja → papeleras y seguridad («never the freezers or dipping cabinets») → el local → alarma, puertas y llave (en el ES, vitrinas y temperaturas iban DESPUÉS de la alarma y la llave, y las persianas antes que la señalización). 08 «Shop Opening» B20: sin «mantecadoras encendidas». 05 «Weekly Upkeep & Stock» B7: el personal no toca el refrigerante (EPA 608) |
| D11 | 05 «Quarterly & Annual» | plagas (mensual, licensed operator), campana y conductos NFPA 96 **solo si se cocina con grasa** (gofres, crepes; la de vapor del pasteurizador, según su fabricante), frío EPA 608 (vitrinas, mantecadora, abatidor), calibración de termómetros (registrador del pasteurizador si tu estado lo licencia), extintores OSHA 1910.157 + hidrostática, gas y eléctrica, **backflow** (dipper wells, máquina de hielo), **health permit + licencia estatal de frozen dessert**, food handler cards + CFPM (2-102.12), seguros con **equipment breakdown + food spoilage**, POS + sales tax, archivo y plan de seguridad alimentaria. Sin DDD, BIE, gases fluorados, legionela ni Verifactu. 03 `B15` = fichajes FLSA (B16 del base) |
| D12 | Caja | 09 igual que el base: su `POR_CELDA` y su `ADAPTAR` heredados tal cual (`cruzar_base`: mismo texto ES) |
| D13 | Moneda | 282 formatos con € → `#,##0.00` (base) |
| D14 | Calendario | Otra estructura (12 meses, filas 5-16: A mes · B acciones · C sabores · D temporada): A, C y D fijados; B = traductor con ADAPTAR por mes, en orden. Temporada US: **Peak** junio-agosto (Memorial Day → Labor Day), **Shoulder** marzo-mayo y septiembre (el ES pone mayo en alta: en EE. UU. el pico empieza el último lunes de mayo), **Low** octubre-febrero. Valentine's · St. Patrick's (mint chip) + Opening Day de las de temporada · Easter · Mother's Day + graduaciones + Memorial Day · Father's Day + Juneteenth · **National Ice Cream Month y National Ice Cream Day (3.er domingo de julio)** + 4 de julio · county fairs y vuelta al cole · Labor Day · Halloween · Thanksgiving (pie à la mode) · holidays (peppermint, eggnog sin alcohol). Sin turrón, roscón, torrija ni alcohol |
| D-ICE | Temperaturas | conservación **0 °F** o menos · vitrina (dipping cabinet) **6–10 °F** [fabricante] · maduración (aging) **36–39 °F**, nunca por encima de 41 °F (3-501.16) · extracción de la mantecadora helado 16–19 °F / sorbete 10–14 °F [fabricante] · cubetas a −4 °F · catering a la llegada ≤ 10 °F; tabla de vida útil del 02 en °F (`POR_CELDA`) |
| D-ICE | Mezcla y licencia | pasteurización **185 °F 15 s** (cifra del kit = 85 °C) y «manda el programa validado del pasteurizador y el mínimo de tu licencia»; enfriado de la mezcla 135 → 70 °F en 2 h y → 41 °F en 4 h (3-501.14); mezcla madurada 3-5 días (dentro de los 7 del date marking). **[estatal]** pasteurizar la mezcla propia suele exigir licencia de fabricante de frozen dessert / dairy (Vermont, Georgia, Arizona con exención de 2019); algunos estados licencian también mantecar mezcla comprada o el soft serve (Vermont, Massachusetts); con mezcla ya pasteurizada suele bastar el health permit. Nota en 02 «Instructions» B6, sin cifras de otros estados |
| D-ICE | Scoop y alérgenos | scoop en el **dipper well de agua corriente** (3-304.12(D)) o uno por sabor; el agua no quita alérgenos: para alergias, manos, guantes, scoop limpio y sanitizado y cubeta sin tocar [criterio del kit]; los 9 de EE. UU. (sésamo y cacahuete incluidos; sulfitos fuera; «wheat», no «gluten»); sin mano desnuda en cucuruchos y toppings (3-301.11); muestras con cucharilla de un solo uso; catar con cuchara limpia (3-301.12) |
| D-ICE | Pack-out y báscula | pints y quarts; los **pints preenvasados** del autoservicio llevan etiqueta con alérgenos (3-602.11; lo llenado a petición no es «packaged», 1-201.10); venta al peso solo con báscula **legal-for-trade** (pesas y medidas estatal); el helado pesa ≥ 4,5 lb/galón (21 CFR 135.110: el overrun tiene techo) |
| D-ICE | Personal de temporada | equipo de verano con menores: 14-15 años con horario de la FLSA (29 CFR 570.35) y equipos de 570.34; work permit según el estado (06 «Peak Season» B7) |
| D-ICE | Lecciones de los hermanos | tiras de sanitizante en 7 tareas (vitrinas, scoops y dipper well, mostrador y báscula, pasteurizador, superficies del obrador, dispensadores; 4-501.114) · enfriado 3-501.14 (la mezcla; sin recalentado: no aplica) · date marking · CF sin cabeceras internas · `AJUSTE_MAQUETA_ES` · calendario cronológico · «2 weeks out» · `TERMINOS_PROHIBIDOS` (bartender, cocktails, beer, liquor, barista, cafe, dining room, host stand, waitstaff, head / sous chef, line / prep cook, MOD, FOH, BEO, banquet, line-up, pizza, burger, ghost kitchen, packer, app manager, «restaurant» salvo consultant / supply; permitidos: server, patio, tip jar, toppings bar, cookie dough, venue del catering). **Sin inventario con mínimos** en este ES: la lección de los mínimos numéricos no aplica |
| D-UK | UK | nota UK en el B02 (Mothering Sunday, bank holidays, Boxing Day); 14 alérgenos en las celdas de alérgenos; −18 °C de conservación y 8 °C de frío en la FAQ de la landing (F3) |

## 2. Ficheros (D5)

| # | Fichero ES | Fichero EN | Título EN |
|---|---|---|---|
| 01 | `01-apertura-cierre.xlsx` | `01-ice-cream-shop-opening-closing-checklists.xlsx` | Ice Cream Shop Opening & Closing Checklists: Dipping Cabinets, Toppings & Counter |
| 02 | `02-partidas-produccion.xlsx` | `02-ice-cream-production-checklists.xlsx` | Ice Cream & Gelato Production Checklists: Pasteurizing, Aging & Batch Freezing |
| 03 | `03-tareas-manager.xlsx` | `03-ice-cream-shop-manager-checklist.xlsx` | Ice Cream Shop Manager Checklist: Daily, Weekly & Monthly |
| 04 | `04-tareas-perfiles.xlsx` | `04-ice-cream-shop-duties-by-role.xlsx` | Ice Cream Shop Duties by Role: Ice Cream Maker, Scooper & Shift Lead |
| 05 | `05-tareas-semanales-mensuales.xlsx` | `05-ice-cream-shop-cleaning-checklist-maintenance.xlsx` | Ice Cream Shop Cleaning Checklist & Maintenance Schedule |
| 06 | `06-eventos-temporada.xlsx` | `06-ice-cream-shop-seasonal-catering-checklists.xlsx` | Ice Cream Shop Seasonal Checklists: Peak Season, Off-Season & Ice Cream Catering |
| 07 | `07-plantilla-personalizable.xlsx` | `07-blank-ice-cream-shop-checklist-template.xlsx` | Blank Ice Cream Shop Checklist Template (Editable) |
| 08 | `08-apertura-cierre-negocio.xlsx` | `08-ice-cream-parlor-opening-closing-checklist.xlsx` | Ice Cream Parlor Opening & Closing Checklist (Whole Shop) |
| 09 | `09-apertura-cierre-caja.xlsx` | `09-cash-drawer-opening-closing.xlsx` | Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log |
| B01 | `BONUS-01-briefing-servicio.xlsx` | `BONUS-01-ice-cream-shop-pre-shift-meeting-template.xlsx` | BONUS: Ice Cream Shop Pre-Shift Meeting Template (Huddle Notes) |
| B02 | `BONUS-02-calendario-anual-tareas.xlsx` | `BONUS-02-ice-cream-shop-seasonal-calendar.xlsx` | BONUS: Ice Cream Shop Seasonal Calendar & Flavor Planner (US) |

## 3. Reglas del delta (`mapas_icecream.REGLAS_US` = las del base + estas)

| Concepto | Fuente |
|---|---|
| Congelado 0 °F; frío 41 °F; maduración 36–39 °F; vitrina 6–10 °F; extracción 16–19 / 10–14 °F | FDA Food Code 2022 §3-501.11, §3-501.16(A)(2); [fabricante] dipping cabinet y batch freezer; [criterio del kit] |
| Pasteurización 185 °F 15 s · licencia de frozen dessert / dairy | [criterio del kit]; [estatal] Vermont Agency of Agriculture (Frozen Dessert / Milk Handlers License), Massachusetts DPH, Arizona Dept. of Agriculture (exención 2019), Ga. Comp. R. & Regs. 40-2-8-.01 |
| Enfriado de la mezcla 135 → 70 °F en 2 h, → 41 °F en 4 h · date marking 7 días | §3-501.14; §3-501.17 |
| Dipper well (agua corriente) o agua a 135 °F · sin mano desnuda · catar con cuchara limpia | §3-304.12(D) y (F); §3-301.11; §3-301.12 |
| Etiqueta de lo envasado en el local (alérgenos) · «packaged» | §3-602.11; §1-201.10 |
| Ice cream ≥ 4,5 lb/galón y 10 % de grasa láctea | 21 CFR 135.110 |
| Menores de 14-15 años: horario y equipos | 29 CFR 570.35 y 570.34; [estatal] work permits |
| Báscula legal para el comercio · CFPM y food handler cards | [estatal] pesas y medidas, NIST Handbook 44 (NTEP); §2-102.12 y [estatal] |
| Temporada y fechas US | Proclamation 5219 (1984: National Ice Cream Month y Day); 5 U.S.C. 6103 (Memorial, Juneteenth, Labor, Thanksgiving); 36 U.S.C. 117 y 109 |
| Seguro con food spoilage · hielo seco · plazos y sabores | [criterio del kit] |

°F que el kit puede afirmar (G7, `GRADOS_F_SPEC`): −4, 0, 6, 10, 14, 16, 19, 32, 36, 39, 41, 70, 100, 104, 122, 135, 185.
`CELSIUS_SIN_F` = 08 «Cierre» B19 (sus temperaturas suben a la fila 10 con el reorden; en la 19 queda la llave).

## 4. Memoria de traducción (`../heredar.py --kit icecream`, `MEMORIA`: cafetería, base, catering, pizzería, hamburguesería, ghost kitchen y bar)

705 cadenas; GM 215 (1.011 palabras: pestañas, glosario, 183 `POR_CELDA`, 29 horas, marca, versión). De las 490 a
traducir: **87 heredadas** (84 exactas + 3 por sufijo; 81 de la cafetería y 6 del catering; 891 palabras) y **403
pendientes** (395 nuevas, 4 «contexto», 4 con otro ADAPTAR; **3.862 palabras**; 103 ADAPTAR en total) → UN traductor
sonnet → `textos_en/G1.json` con los 403 ids. La cafetería va delante del base: 87 heredadas frente a 84 (el base
dice «restaurant») y 86 con el catering delante (su molde ligero apenas comparte textos). Lo nuevo es casi todo: las
tareas de una heladería no existen en los hermanos.

    python3 extraer_textos.py --kit icecream && python3 icecream/mapas_icecream.py && python3 heredar.py --kit icecream
    python3 aplicar_en.py --kit icecream --dry-run [--parcial] --idempotencia --mes October; python3 gates_en.py --kit icecream [--parcial] --dir <carpeta> [--autotest]

Para la F2: `aplicar_en`/`gates_en` ya traen los ganchos del molde ligero del catering (`CF_POR_CELDA`,
`LIBROS_SIN_MARCA`, `HOJA_HORAS`, `HOJA_VERDE`); no se ha tocado código común. Papel A4 → Letter en las 38 hojas.

## 5. Erratas del ES (para su próxima v2.x; la EN nace corregida)

- 08 «Cierre del Negocio» B18-B19: cubrir las vitrinas y registrar las temperaturas de cierre DESPUÉS de activar la
  alarma (B16) y cerrar con llave (B17); B9 cierra persianas antes de recoger la señalización (B12) y vaciar papeleras
  (B14); B15 «enchufes» sin excluir congeladores y vitrinas.
- 08 «Apertura del Negocio» B20: «mantecadoras encendidas» al abrir (la mantecadora solo se enciende para mantecar).
  Horas de 07:00-07:45 (08 y 09) de cafetería: una heladería abre a media mañana (la EN las sube 3 h).
- 05 «Gestión Semanal» B7: «verificar niveles de refrigerante» lo hace el personal (solo un técnico certificado:
  gases fluorados en España, EPA 608 en EE. UU.).
- 05 «Trimestral y Anual» B9 (semestral) dentro de la sección «Trimestral».
- Molde: las cabeceras internas del 01-06 y el B01 se pintan de verde con la CF de «hecho» (como el catering).

## R. Research (una pasada, 24-oct-2026)

**Demanda (DataForSEO, US, 2840/en):** ice cream shop 246.000 · ice cream cake 135.000 · ice cream scooper 33.100 (el
utensilio) · ice cream parlor 27.100 · gelato shop 27.100 · national ice cream day 27.100 (pico de 246.000 en julio) ·
ice cream social 27.100 · soft serve machine 9.900 · scoop shop 4.400 · ice cream mix 3.600 · how to make gelato 2.900 ·
ice cream catering 1.600 · dipper well 1.000 · ice cream shop equipment 1.000 · dipping cabinet 320 · ice cream shop
business plan 320 · batch freezer 210 · overrun 210 · how to open an ice cream shop 170 · ice cream production 90 ·
soft serve machine cleaning 90; «ice cream shop checklist / opening checklist / cleaning checklist» y «gelato shop
checklist», sin volumen (como en los hermanos). **Jerga US** (alta en `../../GLOSARIO-JERGA-ES-EN.md`, sección
Heladería): scoop shop / ice cream parlor · dipping cabinet (gelato case) · batch freezer · aging the mix · hardening
cabinet / blast freezer · draw temperature · overrun · dipper well · scoop / spade · pan · pint / quart (pack-out) ·
tasting spoon · mix-ins / swirl · waffle cone · ice cream cake · scooper · shift lead · front counter · Opening Day.
**Delicado, comprobado:** 3-304.12(D) (dipper well de agua corriente; la alternativa es agua a 135 °F; hay
citaciones de inspección en Chicago por no tener ninguno); licencias de frozen dessert por estado (Vermont, Massachusetts, Arizona, Georgia,
Nueva Jersey); National Ice Cream Day = 3.er domingo de julio (Proclamation 5219, 1984). Marcas reales en los
testimonios del ES: ninguna (`kit-tareas-heladeria.ts` y `src/data/testimonials-heladeria.ts`, 8 testimonios).
