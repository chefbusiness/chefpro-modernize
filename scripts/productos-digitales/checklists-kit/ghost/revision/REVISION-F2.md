# Ghost Kitchen Checklists Kit Pro — revisión adversarial de F2 (18-oct-2026 · sesión Claude Code)

Revisor único. Fuentes:
- `ghost/revision/dump_en.txt` / `dump_es.txt`, 3.387 líneas cada uno, alineados por línea; «L» = línea del volcado EN;
- `ghost/SPEC.md`, `ghost/F2-NOTAS.md`, `ghost/mapas_ghost.py` (`REGLAS_US`, `GRADOS_F_SPEC`) y `mapas.py`;
- las revisiones del base, el bar, la cafetería, el catering, la pizzería y la hamburguesería, y el volcado final de la
  hamburguesería para ver cómo quedaron sus correcciones.

Solo lectura y `grep` de los volcados, más un `openpyxl` corto sobre el 05 y el 02 con la CPU a 49 °C:
- la tabla de congelación B27:D34 está desbloqueada;
- los mínimos del inventario son números;
- el 02 «Cold Station» B8 tiene ajuste de texto.

Dos comprobaciones en la web:
- AB 3336: la guía del condado de Ventura y el resumen de Inline Plastics;
- la estacionalidad del delivery: el 10-K FY2025 de DoorDash.

## Veredicto

**No hay nada BLOQUEANTE.** Lo que se pedía mirar está bien:
- **Precintos (AB 3336, 2020, en vigor el 1-ene-2021).** Es la cocina la que cierra con un método a prueba de
  manipulación las bolsas y los envases de la comida lista para consumir, antes de que el repartidor de la app se los
  lleve. El resto de lugares lleva «check local rules» y no se inventan normas de NYC.
- **Alérgenos.** Los 9 de EE. UU. y, en el UK, los 14. Sin norma federal para la ficha de la app. En el UK, en la venta
  a distancia, antes de la compra y en la entrega. Natasha's Law, fuera.
- **Arroz de sushi.** §3-502.11(D) es la cita correcta; si no, 41 °F o TPHC con descarte a las 4 h (§3-501.19).
- **El pase.** Caliente a 135 °F o más y frío a 41 °F o menos, en bolsas separadas hasta la recogida.
- **La cocina.** La cocción, el enfriado en dos fases, el recalentado a 165 °F en 2 h, el date marking, el aviso al
  consumidor y las tiras de sanitizante.
- **El negocio.** Comisiones sin cifras inventadas (topes en NYC y SF sin número), permisos y DBA, sales tax como
  marketplace facilitator, FLSA 2 / 3 años (NY 6) y OSHA 1910.157(e)(2).
- **Las erratas ES de la SPEC §5.** El orden del 08 (apertura y cierre) y el 07 sin sala ni barra.
- **El calendario.** Cronológico y con fechas US correctas.
- **La parte técnica.** Sin español, €, °C, horas de 24 h ni términos prohibidos; las fórmulas, la DV y la CF casan con
  su texto.

**Hay 4 MAYORES:**
- **M1.** Vuelve el «Full fryer oil change» MENSUAL de la hamburguesería, y el kit no menciona el TPM en ningún sitio.
- **M2.** La destrucción de parásitos del pescado crudo (poke, sushi) no tiene las tres opciones de §3-402.11. Además,
  «−31 °F until solid plus 15 h» se puede leer como «15 h a −4 °F».
- **M3.** El calendario US pone un «Summer peak season» con más personal, cuando el delivery baja en verano. El propio
  calendario y el 10-K de DoorDash dicen lo contrario.
- **M4.** En el 01 y en el 04 se encienden las marcas ANTES de comprobar la impresora, las cartas y los 86. Es la
  misma errata de orden que la SPEC D10 corrigió en el 08.

**Además, 18 MENORES.** Varios son lecciones de los hermanos que reaparecen: «15 days out», los utensilios cada 4 h,
la calibración anual, la supresión semestral bajo «Annual», el aceite usado y la trampa de grasa, el «0.5 qt» y la
estantería del crudo.

**Cómo se corrige.** Todo con texto por celda (`POR_CELDA` / G1) o `VALORES_EN`, sin filas nuevas: G1 y G6 siguen en
paridad, y ningún °F sale de `GRADOS_F_SPEC`. Hacen falta dos citas nuevas en `REGLAS_US`, §4-602.11(C) (m4) y el TPM
en `aceite` (M1), que ya existen en `mapas_burger.py`. Tras corregir, hay que repasar `ancho_texto` / `n_lineas` en
las celdas que se alargan: 02 «Cold Station» B8 y 05 «Weekly FIFO Check» D29, que ya tiene `ALTOS_FILA` en la 34.

| # | Sev. | Dónde | Qué |
|---|---|---|---|
| M1 | MAYOR | 05 «Monthly Maintenance» B7 (L1784) · 05 «Weekly Deep Clean» B10 (L1642) · 01 «Kitchen Closing» B13 (L255) · 03 «Shift Handover» B12 (L1023) · 05 «Weekly FIFO Check» B14 (L1725) | Cambio de aceite mensual, boil-out semanal Y mensual, y sin TPM |
| M2 | MAYOR | 02 «Cold Station» B8 (L489) · 05 «Weekly FIFO Check» D29 (L1746) | §3-402.11 incompleta y ambigua |
| M3 | MAYOR | BONUS-02 «Holiday Calendar» B18/C18 (L3332-3333) · C14 (L3317) | «Summer peak season» en un negocio de delivery |
| M4 | MAYOR | 01 «Kitchen Opening» B31-B37 / E31-E37 (L152-185) · 04 «App Manager» B7-B10 (L1278-1296) | Marcas encendidas antes de impresora, cartas y 86 |
| m1 | MENOR | 06 «Holiday Season» E7 (L2155) · E8 (L2160) | «15 days out» reaparece |
| m2 | MENOR | 02 «Cold Station» B18 (L531) vs 05 «Weekly FIFO Check» B8 (L1699) | Vegetales cortados: 24 h frente a 2 días |
| m3 | MENOR | 01 «Kitchen Closing» B6 (L224) · 02 «Hot Station» B18 (L448) · 02 «Cold Station» B17 (L526) | «Keeps 7 days» frente a los plazos más cortos del kit |
| m4 | MENOR | 02 «Hot Station» B11 (L417) · 02 «Cold Station» B15 (L520) · 05 «Weekly Deep Clean» B9 (L1637) | Sin utensilios cada 4 h; tablas de corte «semanales» |
| m5 | MENOR | 05 «Quarterly & Annual» B15 (L1890) · 02 «Hot Station» B6 (L396) | La sonda solo se calibra una vez al año |
| m6 | MENOR | 05 «Quarterly & Annual» B8/E8 (L1865/L1867) | Supresión cada 6 meses bajo «Annual» |
| m7 | MENOR | 05 «Quarterly & Annual» B13/E13 (L1881/L1884) | Retirada del aceite usado «Quarterly» |
| m8 | MENOR | 05 «Quarterly & Annual» B14/E14 (L1886/L1888) · 05 «Instructions» B6 (L1438) | Cartón «Quarterly» y sin trampa de grasa (FOG) |
| m9 | MENOR | 05 «Quarterly & Annual» B7 (L1861) | NFPA 96 no dice «cooking all day» |
| m10 | MENOR | 02 «Hot Station» B7 (L401) | Crudo «bottom shelf» con pollo, ternera y pescado |
| m11 | MENOR | 05 «Daily Inventory» C/D24, C/D25, C/D27 (L1537-1550) | «0.5 qt» (×3) |
| m12 | MENOR | 08 «Site Opening» E5 (L2445) vs 04 «Operations Manager» E6 (L1364) | Alarma a las 9:00 AM frente a las 8:45 AM |
| m13 | MENOR | 04 «Multi-Brand Cook» B13 (L1123) vs 02 «Hot Station» B13 (L427) | Objetivo de 10 min frente a 8-12 min |
| m14 | MENOR | 01 «Kitchen Opening» B18 (L95) vs B40 (L193) | La mise en place va antes que el sanitizado de superficies |
| m15 | MENOR | 03 «Manager Monthly» B21 (L966) vs 05 «Weekly Deep Clean» B7 (L1627) | Filtros de campana: técnico mensual frente a equipo semanal |
| m16 | MENOR | 09 «Instructions» B6 (L2644) | La caja de un restaurante en una cocina solo delivery |
| m17 | MENOR | 08 «Instructions» B11 (L2403) | Nada para la cocina compartida (cloud kitchen park, commissary) |
| m18 | MENOR | 02 «Cold Station» B7 (L484) | «a HACCP plan from the health department» |

---

## MAYORES

### M1 · «Full fryer oil change» MENSUAL, boil-out semanal y mensual, y ningún TPM en el kit

**Dónde:**
- 05 «Monthly Maintenance» B7 (L1784), D7 «Manager» y E7 «Monthly» (L1786-1787): `Full fryer oil change and deep
  clean (boil-out) per the fryer manufacturer's instructions (…)`;
- 05 «Weekly Deep Clean» B10 (L1642): `Deep-clean the fryer (boil-out) per the manufacturer's instructions`, «Monday»;
- el aceite sin TPM: 01 «Kitchen Closing» B13 (L255), 03 «Shift Handover» B12 (L1023) y 05 «Weekly FIFO Check» B14
  (L1725, «color, smell, smoke»).

**Qué falla.**
- **Es la M1 de la hamburguesería, que reaparece.** Allí se corrigió así: «the oil itself is changed whenever the TPM
  tester says, not once a month». En una ghost kitchen que fríe todo el día para varias marcas (alitas, tenders,
  patatas), el aceite dura días, y una fila mensual de «Full fryer oil change» se lee como «el aceite se cambia cada
  mes».
- **El boil-out aparece dos veces, con frecuencias distintas:** semanal en el 05 «Weekly Deep Clean» y mensual en el 05
  «Monthly Maintenance».
- **Ninguna celda del kit nombra el TPM** (`grep -i "TPM\|polar\|tester"` = 0). El criterio que queda, «color, smell,
  smoke», es el que la lección de los hermanos («aceite según TPM») sustituyó.

**Norma o fuente:**
- `mapas_burger.REGLAS_US['aceite']`: filtrado según el fabricante y cambio cuando lo diga el medidor de TPM, sin límite
  federal;
- `mapas_ghost.REGLAS_US['aceite']` solo dice «según el fabricante».

**Corrección EN.** Las cuatro celdas son `CELSIUS_SIN_F` y siguen sin cifra °F.
- 05 «Monthly Maintenance» B7 (D7 «Manager» y E7 «Monthly» se quedan):
  `Fryer check per the manufacturer: thermostat and high-limit, drain valve, baskets and the built-in filtration or filter machine; the oil itself is changed whenever the TPM tester says (no federal limit), not once a month — the boil-out is weekly ("Weekly Deep Clean" tab)`
- 05 «Weekly FIFO Check» B14:
  `Check the fryer oil with a TPM tester or test strips (color, smell and smoke only as a backup) and log the date of the last change; no federal limit: change it when the tester says and per the fryer manufacturer`
- 01 «Kitchen Closing» B13:
  `Filter the fryer oil per the fryer manufacturer (many have built-in filtration designed for hot oil; others need it cooled) and change it when the TPM tester says, with heat-resistant gloves, apron and goggles; used oil goes to the used cooking oil recycler's container`
- 03 «Shift Handover» B12:
  `Fryer oil condition (last TPM reading) and date of the last change (changed when the TPM tester says, per the fryer manufacturer)`
- `REGLAS_US['aceite']`, como en la hamburguesería: `filtrado según el fabricante de la freidora; cambio cuando lo diga
  el medidor de TPM (sin límite federal)`.

**Errata para el ES v2.x:** «Cambio completo del aceite» mensual (05 «Mantenimiento Mensual» B7).

### M2 · Pescado crudo: §3-402.11 con dos de sus tres opciones y una redacción ambigua

**Dónde:**
- 02 «Cold Station» B8 (L489): `…use only fish frozen at −4 °F or below for 7 days, or at −31 °F or below until solid plus 15 h (FDA 3-402.11)…`;
- 05 «Weekly FIFO Check» D29 (L1746): `…at −4 °F or below for 7 days (or −31 °F or below until solid plus 15 h), with a record (FDA 3-402.11)…`.

**Qué falla.** En esta ghost kitchen, el poke y el sushi son el corazón de la estación fría.
- **§3-402.11(A) tiene TRES opciones:**
  1. congelado y almacenado a −4 °F o menos durante 7 días (168 h);
  2. congelado a −31 °F o menos hasta solidificar y **almacenado a −31 °F** o menos 15 h;
  3. congelado a −31 °F o menos hasta solidificar y almacenado a −4 °F o menos **24 h**.
- **El kit omite la tercera.**
- **«Until solid plus 15 h» no dice a qué temperatura van esas 15 h.** Quien congele en un abatidor a −31 °F y pase el
  pescado a un congelador de −4 °F lo dará por tratado a las 15 h, y la norma pide 24 h a −4 °F. Es un fallo de
  destrucción de parásitos.
- **La propia fuente del kit las tiene completas:** `mapas.REGLAS_US['parasitos']` (L532) dice «−4 °F 168 h · −31 °F
  hasta sólido + 15 h · −31 °F sólido + −4 °F 24 h; registro 90 días».
- **En D29, el registro se atribuye a 3-402.11;** es §3-402.12.

No lo marco BLOQUEANTE porque la lectura natural es la correcta, el congelador de 0 °F queda bien excluido y casi
siempre manda la declaración del proveedor (que el kit sí nombra).

**Norma o fuente:** FDA Food Code 2022 §3-402.11(A)(1)-(3) y §3-402.12.

**Corrección EN:**
- 02 «Cold Station» B8:
  `Fish served RAW, marinated or partly raw (poke, sushi, tartare, ceviche) — parasite destruction (FDA 3-402.11): frozen and stored at −4 °F or below for 7 days; or frozen at −31 °F or below until solid and stored at −31 °F or below for 15 h; or frozen at −31 °F or below until solid and stored at −4 °F or below for 24 h. Keep the freezing record, or the supplier's written statement, for 90 days (FDA 3-402.12); consumer advisory on each app listing (FDA 3-603.11). A regular 0 °F freezer does not count`
- 05 «Weekly FIFO Check» D29:
  `Fat goes rancid even frozen; freezing only counts as parasite destruction at −4 °F or below for 7 days, or at −31 °F until solid and then 15 h at −31 °F or 24 h at −4 °F (FDA 3-402.11), with a record or the supplier's statement (FDA 3-402.12): a regular 0 °F freezer does not get there`
- Después: `ancho_texto` / `n_lineas` en las dos. La fila 29 del FIFO puede necesitar `ALTOS_FILA`, como la 34.

### M3 · «Summer peak season» en el calendario de una cocina solo delivery

**Dónde:** BONUS-02 «Holiday Calendar»:
- fila 18 (L3331-3334): A18 `July–August`, B18 `Summer peak season`, C18 `Extra staff, extended hours and a summer menu by brand`;
- fila 14, el Memorial Day, C14 (L3317): `Summer kicks off: extra staff and summer stock…`.

**Qué falla.**
- **El kit se contradice.** El mismo calendario dice en la fila 11 (L3304) `Warm weather: lunch orders drop` y en la
  fila 22 (L3348) `Cold, rainy days: orders go up`.
- **Las apps dicen lo mismo que esas dos filas.** El 10-K FY2025 de DoorDash: la demanda sube con frío o mal tiempo y
  baja con tiempo cálido y soleado, y cae en las vacaciones escolares de verano.
- **De dónde viene.** Es la «temporada alta» del ES (L3317/L3332: «Inicio temporada alta», «Temporada alta»), que es
  turística española. Para un restaurante con terraza vale; para un delivery-only de EE. UU., no.
- **Qué vería el comprador.** Un operations manager lo ve en cuanto lo lee: le dice que refuerce turnos en sus semanas
  más flojas.

**Fuente:** DoorDash, Form 10-K FY2025, «Seasonality».

**Corrección EN** (texto por celda en `CALENDARIO` / `POR_CELDA`; las filas no cambian):
- B18: `Summer slowdown (warm weather, vacations, school break)`
- C18: `Delivery usually dips: trim prep and shifts, keep the hours steady, push lunch combos and hot-weather items (bowls, salads, cold drinks) and plan the fall menu; near beaches, tourist areas or summer events it can run the other way`
- D18: `Ongoing` (se queda).
- C14: `Summer kicks off: decide the holiday hours and post them in each app, set up the summer menu and plan staffing for the slower summer weeks`
- `REGLAS_US['dias_fuertes']` no cambia; puede sumar «el verano baja».

### M4 · Las marcas se encienden ANTES de comprobar la impresora, las cartas y los 86 (01 y 04)

**Dónde:**
- 01 «Kitchen Opening», bloque «ORDER TABLETS & DELIVERY APPS» (L150-185), todo a las 10:30 AM, en este orden:
  1. B31: tablets;
  2. B32: wifi;
  3. **B33: `Turn on all brands in DoorDash, Uber Eats and Grubhub`**;
  4. B34: cartas;
  5. B35: alérgenos;
  6. B36: impresora;
  7. B37: 86.
- 04 «App Manager» (L1272-1296):
  1. B6: tablets, 10:00 AM;
  2. **B7: marcas ON**, 10:30;
  3. B8: cartas;
  4. B9: promos;
  5. B10: 86.

**Qué falla.**
- **Es la errata de orden que la SPEC D10 corrigió en el 08.** El 08 ya va bien: tablets (10:00), impresoras y KDS,
  timbre, tiempos y, la última, las marcas (10:30).
- **El 01 y el 04 son las listas que siguen el shift manager y el app manager**, y encienden las marcas antes de saber
  si la impresora imprime («no printed ticket, the order never goes out», 08 B19) y antes de pausar lo agotado. Entran
  pedidos de platos que no hay y llegan las cancelaciones y las malas notas.
- **El 01 enciende las tablets a las 10:30 AM**, y el 08 B18 y el 04 B6, a las 10:00 AM.

**Corrección EN** (texto por celda; mismas filas):
- 01 «Kitchen Opening»:

  | Celda | Texto | Hora (E) |
  |---|---|---|
  | B31 | `Turn on all order tablets` | `10:00 AM` |
  | B32 | `Check the wifi / data connection on every tablet` | `10:00 AM` |
  | B33 | `Check the ticket printer works` | `10:15 AM` |
  | B34 | `Check that menus are up to date (prices, availability)` | `10:15 AM` |
  | B35 | el texto de alérgenos actual | `10:15 AM` |
  | B36 | `86 anything out of stock: pause that dish or brand in each app` | `10:30 AM` |
  | B37 | `Turn on all brands in DoorDash, Uber Eats and Grubhub — last, once the tablets, printer, menus and 86s are checked` | `10:30 AM` |

- 04 «App Manager»:

  | Celda | Texto |
  |---|---|
  | B7 | `Check that menus are up to date` |
  | B8 | `86 the dishes that are out of stock` |
  | B9 | `Turn on today's promos if applicable` |
  | B10 | `Turn on all brands in DoorDash, Uber Eats and Grubhub` |

  Las horas E7-E10 se quedan a las 10:30 AM.

**Errata para el ES v2.x:** la misma en el 01 «Apertura Cocina» y en el 04 «Gestor de Plataformas».

---

## MENORES

### m1 · 06 «Holiday Season» E7 (L2155) y E8 (L2160): «15 days out»

**Qué falla.** Es la lección m15 de la cafetería, m6 de la pizzería y m1 de la hamburguesería. El glosario traduce
«15 días antes» literalmente.

**Corrección EN (E7 y E8):** `2 weeks out`. Para que no vuelva, en el glosario: «15 días antes» → «2 weeks out».

### m2 · Vegetales cortados: «24 h» en la estación fría, «2 days» en el FIFO

**Dónde:**
- 02 «Cold Station» B18 (L531): `Discard cut fruit/vegetables older than 24 h (kit standard)`;
- 05 «Weekly FIFO Check» B8 (L1699): `Check cut vegetables (2 days max)`.

**Qué falla.** Hay dos plazos de descarte para lo mismo. `REGLAS_US['plazos_kit']` los separa bien: fruta cortada
24 h, vegetales cortados 2 días.

**Corrección EN (02 B18):**
`Discard cut fruit older than 24 h and cut vegetables older than 2 days (kit standard, same as the "Weekly FIFO Check" tab in 05); cut leafy greens, tomatoes and melon are TCS: 41 °F or below and date marked (FDA 3-501.16, 3-501.17)`

**Errata para el ES:** «+24h» (B18) frente a «max 2 días» (FIFO B8).

### m3 · «Ready-to-eat keeps 7 days» frente a los plazos más cortos del propio kit

**Dónde:** 01 «Kitchen Closing» B6 (L224), 02 «Hot Station» B18 (L448) y 02 «Cold Station» B17 (L526).

**Qué falla.**
- Son 7 días: el máximo de §3-501.17.
- Pero el 05 «Weekly FIFO Check» fija 5 días para las salsas caseras, 3 para las proteínas frescas y 2 para los
  vegetales cortados. Quien etiquete a 7 días todo lo preparado se salta el criterio del kit.

**Corrección EN:**
- 01 «Kitchen Closing» B6:
  `Date-mark all prepped food: prep day = day 1, 7 days max at 41 °F (FDA 3-501.17), or less where the "Weekly FIFO Check" tab in 05 sets a shorter limit`
- En 02 B18 y B17, sustituir `date marking: ready-to-eat food keeps 7 days at 41 °F, prep day = day 1 (FDA 3-501.17)`
  por:
  `date marking: 7 days max at 41 °F, prep day = day 1 (FDA 3-501.17), or the kit's shorter limit (05 "Weekly FIFO Check")`

### m4 · Ni un utensilio cada 4 h, y las tablas de corte se sanitizan «cada semana»

**Dónde:**
- 05 «Weekly Deep Clean» B9 (L1637): `Cutting boards: wash, rinse and sanitize (…)`, «Monday»;
- en servicio no hay nada: ni en 02 «Hot Station», ni en 02 «Cold Station», ni en 04 «Multi-Brand Cook».

**Qué falla.**
- Es la lección «utensilios cada 4 h» (m6 de la hamburguesería; su volcado final, L576, cita §4-602.11). Aquí no
  aparece en ninguna celda.
- La única fila de tablas es SEMANAL: se lee como «las tablas se sanitizan una vez a la semana».

**Norma o fuente:** FDA Food Code §4-602.11(A)(C): al menos cada 4 h con alimentos TCS, y entre crudo y listo para
consumir.

**Corrección EN:**
- 05 «Weekly Deep Clean» B9:
  `Cutting boards: deep clean and inspect — scrub, sanitize (approved sanitizer at label strength, test strip; FDA 4-501.114) and resurface or replace any with deep cuts or stains (in use they are washed, rinsed and sanitized at least every 4 h, FDA 4-602.11)`
- 02 «Hot Station» B11:
  `Cook to each brand's tickets; wash, rinse and sanitize tongs, spatulas and cutting boards at least every 4 h during service, or swap in clean ones (FDA 4-602.11)`
- 02 «Cold Station» B15:
  `Keep inserts restocked; swap serving spoons, tongs and cutting boards for clean, sanitized ones at least every 4 h (FDA 4-602.11)`
- `REGLAS_US`: + §4-602.11(C), como en `mapas_burger.py` (L589).

### m5 · 05 «Quarterly & Annual» B15 (L1890): la sonda solo se calibra una vez al año

**Qué falla.**
- Es la m5 de la hamburguesería. Es la única calibración del kit, con E15 «Annual».
- De esa sonda dependen los 165 / 155 / 145 °F, el enfriado y el pase.

**Corrección EN:**
- 05 B15:
  `Once a year, have the oven and griddle thermostats and any built-in probes checked against a known standard; the probe thermometers get an ice-point check (32 °F) at opening ("Hot Station" tab in 02, row 1) and after any drop`
  D15 y E15 se quedan.
- 02 «Hot Station» B6 (L396):
  `Preheat griddle, oven and burners for today's menus; ice-point check the probe thermometer (32 °F) and recalibrate it if it's off`

### m6 · 05 «Quarterly & Annual» B8 / E8 (L1865 / L1867): la supresión semestral bajo «Annual»

**Qué falla.** Es la m9 de la hamburguesería. Quien programe por la columna «Frequency» se salta la inspección de los
6 meses.

**Corrección EN:**
- B8:
  `Hood fire suppression inspected every 6 months (NFPA 96) and annual extinguisher maintenance by a licensed fire protection company: new tag and record (OSHA 1910.157); hydrostatic tests as the label says (OSHA 1910.157(f))`
- E8: `Semiannual`

### m7 · 05 «Quarterly & Annual» B13 / E13 (L1881 / L1884): el aceite usado se retira «Quarterly»

**Qué falla.** Es la m8 de la hamburguesería. Con freidoras todo el día, la retirada va según el volumen, no cada
trimestre.

**Corrección EN (B13; E13 «Quarterly» se queda):**
`Used fryer oil: pickups by a licensed recycler as often as your volume needs; every quarter, check the receipts are on file and the outdoor container is closed and not leaking`

### m8 · 05 «Quarterly & Annual» B14 (L1886): el cartón se retira «Quarterly» y no hay trampa de grasa

**Qué falla.**
- Se lee como «la recogida de cartón es trimestral», y en una ghost kitchen es semanal o más frecuente.
- Falta el separador de grasas (FOG), que casi todos los municipios exigen a una cocina con freidora y plancha. Es la
  m7 de la hamburguesería.

**Corrección EN:**
- B14 (E14 «Quarterly» se queda; es la revisión):
  `Review the cardboard and plastic recycling contract with your hauler (pickups usually run weekly or more: a ghost kitchen goes through far more packaging than a regular restaurant) and keep the grease trap pumping manifests, as often as your local FOG rules require`
- 05 «Instructions» B6 (L1438), en la lista: `… used cooking oil, cardboard and plastic packaging pickup, grease trap, thermometer calibration, …`

### m9 · 05 «Quarterly & Annual» B7 (L1861): NFPA 96 no dice «cooking all day»

**Qué falla.** La tabla de NFPA 96 llama «high volume» a la cocina de 24 horas, la parrilla de carbón (charbroiling) y
el wok. Una cocina de 9:00 AM a 10:30 PM es «moderate» si no hace ninguna de esas. El E7 «Quarterly» vale, pero el
texto atribuye a NFPA un criterio que no es suyo.

**Corrección EN (B7):**
`Hood and duct cleaning by a certified contractor (NFPA 96): quarterly if high volume (24-hour cooking, charbroiling or wok), semiannual if moderate — a multi-brand kitchen cooking from morning to night often goes quarterly: your hood contractor and fire marshal decide`

### m10 · 02 «Hot Station» B7 (L401): «keep raw on the bottom shelf» con pollo, ternera y pescado

**Qué falla.** Es la m3 de la hamburguesería; su volcado final dice «below ready-to-eat food and above any raw
chicken». Aquí conviven pollo, picada y pescado crudos: el pollo, abajo del todo.

**Corrección EN.** Sustituir el final por:
`…; store raw below ready-to-eat, with raw chicken on the very bottom, under beef and fish (FDA 3-302.11)`

### m11 · 05 «Daily Inventory»: «0.5 qt» ×3 (L1537-1550)

**Qué falla.** D24 Teriyaki, D25 Sriracha y D27 BBQ sauce = 0.5 «qt». Es la conversión directa de 0,5 L. La
hamburguesería lo pasó a «1 pt» (su REVISION D2).

**Corrección:**
- C24, C25 y C27 → `pt`;
- `VALORES_EN` D24, D25 y D27 → `1`, como número;
- `REGLAS_US['inventario']`: «0,5 L → 1 pt».

### m12 · 08 «Site Opening» E5 (L2445) 9:00 AM frente a 04 «Operations Manager» E6 (L1364) 8:45 AM

**Qué falla.**
- El mismo hito tiene dos horas: el 04 abre y desarma la alarma a las 8:45, y el 08, la columna vertebral del día, a
  las 9:00.
- Además, a las 9:00 AM el 01 ya enciende campana y gas.

**Corrección EN (08 E5):** `8:45 AM`. Errata también en el ES (09:00 frente a 08:45).

### m13 · 04 «Multi-Brand Cook» B13 (L1123): «under 10 min»

**Qué falla.** El 02 «Hot Station» B13 (L427) y `REGLAS_US['plazos_kit']` dicen 8-12 min, y el 03 «Manager Weekly» B8,
«under 12».

**Corrección EN:** `Watch ticket times: orders ready in 8-12 min`

### m14 · 01 «Kitchen Opening»: la mise en place (filas 11-15) va antes que el sanitizado de superficies (fila 30)

**Qué falla.**
- Las horas están bien: el sanitizado, a las 9:00, y la mise en place, a las 9:15.
- Pero quien sigue la hoja de arriba abajo prepara sobre superficies sin sanitizar.

**Corrección EN (B18, L95; sin mover filas):**
`Set up mise en place for all brands/concepts, on surfaces already cleaned and sanitized (row 30)`

### m15 · 03 «Manager Monthly» B21 (L966): los filtros de campana, del técnico y mensuales

**Qué falla.**
- El 03 dice `the team cleans the filters` con D21 «Technician» y E21 «Monthly».
- El 05 «Weekly Deep Clean» B7 (L1627) los desengrasa el equipo cada semana.
- El 05 «Monthly Maintenance» B9 se los da al técnico.

**Corrección EN (03 B21):**
`Hood: the team degreases the filters every week ("Weekly Deep Clean" tab in 05); the technician checks the fan, belts and filters monthly; the contractor cleans the ductwork ("Quarterly & Annual" tab, NFPA 96)`

### m16 · 09: una caja de restaurante (propinas, house accounts) en una cocina solo delivery

**Dónde:** 09 entero; «Works with» B24 en todos los libros.

**Qué falla.**
- En una ghost kitchen, los pedidos de las apps vienen pagados y cada app los liquida en su payout.
- No hay propinas de mesa, y el 09 habla de «card tips paid in cash» y de «house accounts».
- La SPEC D12 decide mantenerlo igual que el base (G5). Pero a un comprador le falta una línea que le diga para qué le
  sirve.

**Corrección EN.** Añadir al final de 09 «Instructions» B6 (L2644):
` In a delivery-only kitchen the app orders are prepaid and paid out by each app (reconcile them against each app's payout report, 01 "Kitchen Closing", row 18): use this file for what is paid at your own counter — walk-in pickup, phone or own-website orders paid on pickup.`

### m17 · 08: nada para la cocina compartida

**Qué falla.**
- En EE. UU., buena parte de las ghost kitchens son una unidad dentro de un cloud kitchen park o una commissary. El
  operador del edificio lleva la alarma, la climatización, los baños, las zonas comunes y el lobby de repartidores.
- El 08 da por hecho que el comprador controla el edificio. La jerga «commissary / shared kitchen» no aparece en el
  kit.

**Corrección EN.** Añadir al final de 08 «Instructions» B11 (L2403):
` In a shared kitchen facility (a unit in a cloud kitchen park or a commissary), mark N/A what the facility operator handles — alarm, HVAC, restrooms, common areas, driver lobby — and keep your own unit's tasks.`

### m18 · 02 «Cold Station» B7 (L484): «a variance and a HACCP plan from the health department»

**Qué falla.** Se lee como si el departamento de salud escribiera el plan HACCP. La varianza la concede el departamento
y el plan lo hace el operador y lo aprueba el departamento (§3-502.11(D), §8-201.13).

**Corrección EN.** Sustituir `needs a variance and a HACCP plan from the health department (FDA 3-502.11(D))` por:
`needs a variance from the health department and a HACCP plan it approves (FDA 3-502.11(D))`

---

## Lo que se intentó refutar y aguanta

**Precintos.** 01 B28, 02 B8 y B15, 04 B15 y el inventario A33 / A38.
- AB 3336, firmada el 18-sep-2020 y en vigor el 1-ene-2021: la cocina cierra con un método a prueba de manipulación
  (pegatina o cinta) las bolsas y los envases de la comida lista para consumir, antes de que el repartidor de la
  plataforma la recoja.
- «Check local rules» fuera de California.

**Pase y empaquetado.** 02 «Packing Station» B11 (L583): bolsas o compartimentos separados, a 135 / 41 °F hasta la
recogida.

**Pescado y arroz** (salvo M2):
- el congelador de 0 °F, excluido;
- el registro o la declaración del proveedor, 90 días;
- el aviso al consumidor en la ficha de la app, en 02 B8 y en 06 B9;
- el ceviche, dentro;
- el arroz: §3-502.11(D), o 41 °F, o TPHC con procedimiento escrito, hora marcada y descarte a las 4 h.

**Lecciones de los hermanos que NO reaparecen:**
- el sanitizante con tira en 01 B40 y B18, 04 B19 y 05 B9;
- §3-501.19 bien dicho;
- el enfriado en dos fases (×4) y el recalentado a 165 °F en 2 h (01 B21, 05 D32);
- el date marking con el día 1;
- sin alcohol;
- sin restos de bar, pizzería ni hamburguesería;
- el orden del 08 (apertura y cierre) y el cierre del 01, con la campana la última y los equipos fríos;
- «let it cool» sin contradicción con el filtrado en caliente (01 B13).

**Normas citadas:**
- 5-202.12 a 100 °F;
- 2-201.11;
- 4-501.114;
- 3-401.11: 165 °F, 155 °F durante 17 s y 145 °F durante 15 s;
- 3-501.13;
- OSHA 1910.157(e)(2) y (f);
- FLSA 2 / 3 años y NY 6;
- EPA 608;
- marketplace facilitator;
- products coverage.

**Alérgenos.** 01 B35, 03 «Manager Weekly» B18 y 06 B9:
- los 9 de EE. UU. y los 14 del UK;
- sin norma federal para la ficha de la app;
- en el UK, en la venta a distancia, antes de la compra y en la entrega.

**Comisiones.** «Roughly 15-30 %», que casa con los planes de 15 / 25 / 30 % de DoorDash y Uber Eats. Topes en NYC y
SF, sin cifra.

**Calendario US.** Cronológico. Las fechas, correctas:
- Super Bowl: el 2.º domingo de febrero desde 2022; LXI cae el 14-feb-2027;
- Mother's Day: el 2.º domingo de mayo;
- Memorial Day: el último lunes de mayo;
- Father's Day: el 3.er domingo de junio;
- Labor Day: el 1.er lunes de septiembre;
- Thanksgiving: el 4.º jueves de noviembre;
- Mardi Gras: febrero-marzo.

Ningún «15 days» en el BONUS-02.

**Técnica:**
- sin €, IVA, APPCC, TPV, Glovo ni Just Eat, °C, «kg», horas de 24 h ni términos prohibidos («restaurant» solo en
  «a regular restaurant» y en la firma);
- los contadores cubren las 5 filas verdes libres;
- la DV es ✓ / — / N/A, igual que las instrucciones;
- la CF ámbar de la caja casa con 09 B17;
- el 05 «Daily Inventory» está sin proteger, como dice B23;
- los mínimos son números (`openpyxl`: int / float);
- la tabla de congelación B27:D34 está desbloqueada, como promete 05 B8;
- las pestañas citadas existen («Weekly FIFO Check», «Quarterly & Annual», «Kitchen Closing», «Cash Drawer Closing»);
- el 07 sale con PACKING & PICKUP / OFFICE & APPS y Packer.

## DUDAS (no son hallazgos)

- **D1 · Exenciones de §3-402.11(B).** Ciertas especies de atún (*Thunnus*) y el pescado de acuicultura alimentado con
  pienso, con la declaración del proveedor (§3-402.12(C)). Una cláusula en 02 B8 ayudaría a quien compra salmón de
  granja para poke, pero alarga una celda ya larga.
- **D2 · La redacción de M2 viene del base.** Está en `mapas.py` L344-350, en 02 «Fríos» B10 y «Mise en Place» B10, y
  en el catering. Si se corrige aquí, conviene alinear los hermanos en su próxima v2.x; no es tarea de esta F2.
- **D3 · El 09 completo en una ghost kitchen** es decisión de producto (SPEC D12). m16 solo explica para qué sirve.
- **D4 · AB 3336 y el contrato con cada app.** Según la guía del condado de Ventura, la cocina debe tener además un
  contrato con cada plataforma. Podría sumarse a 06 «Brand Launch» B8 («keep a signed agreement with each app; required
  in California»). No lo he cotejado con el texto de la ley.
- **D5 · Super Bowl «2nd Sunday in Feb».** Es correcto hoy. Si la NFL pasa a 18 partidos, se mueve. «Early-to-mid
  February (check the NFL date)» resistiría mejor.
- **D6 · Memorial Day (C14 en M3).** Es un fin de semana de barbacoa en casa; el efecto en el delivery es variable. La
  corrección propuesta evita afirmar un pico o un valle.
- **D7 · El orden de las antelaciones en 06 «Game Night»** (Day before → 2 days → 3 days → Day before) no es
  cronológico. Viene así del ES y es igual en los hermanos ya publicados; lo dejo.

## Fuentes web

- [Ventura County EH — AB 3336 guidance for food facilities and third-party delivery services](https://rmadocs.venturacounty.gov/environmental-health/programs/consumer-food-protection/publications/environmental-health-assembly-bill-3336-guidance-for-food-facilities-and-third-party-delivery-services.pdf)
- [Inline Plastics — What is California's Assembly Bill 3336](https://www.inlineplastics.com/blog/what-is-californias-assembly-bill-3336-and-what-does-it-mean-for-food-businesses/)
- [DoorDash, Inc. — Form 10-K FY2025 (Seasonality)](https://www.sec.gov/Archives/edgar/data/1792789/000179278926000013/dash-20251231.htm)

---

## Ronda 1: aplicado / no aplicado (implementador, 18-oct-2026 · sesión Claude Code)

Todo en la fuente, sin filas nuevas: G1 y G6 siguen en paridad y ningún °F sale de `GRADOS_F_SPEC`. Citas nuevas en
`REGLAS_US`: `aceite` (TPM) y `utensilios_4h` (§4-602.11(C)), las dos copiadas de `mapas_burger.py`, y
`estacionalidad` (10-K de DoorDash).

| # | Estado | Cómo |
|---|---|---|
| M1 aceite | APLICADO | G1 c0443 (05 B7), c0414 (FIFO B14), c0093 (01 B13), c0260 (03 B12): texto EN exacto del informe. `_ACEITE` y los ADAPTAR, con TPM. El boil-out queda semanal (05 «Weekly Deep Clean» B10). Siguen en `CELSIUS_SIN_F`, sin °F |
| M2 parásitos | APLICADO | G1 c0148 (02 B8) y c0426 (FIFO D29), con las 3 opciones y §3-402.12. `_PARASITOS` alineado con `mapas.REGLAS_US['parasitos']`. B8 en fila automática (11 líneas) y D29 subida a 61,25 por `capa_ajuste`: no hace falta `ALTOS_FILA` |
| M3 verano | APLICADO | B18 `Summer slowdown (warm weather, vacations, school break)` (`CALENDARIO`); G1 c0830 (C18) y c0818 (C14): texto EN exacto del informe |
| M4 orden 01 / 04 | APLICADO | `POR_CELDA` (`_TABLETS_01`, `_APPS_04`, con la fila de origen comprobada por `cruzar_censo`). 01: B33 impresora, B36 los 86, B37 las marcas, la última; E31-E37 a las 10:00 / 10:15 / 10:30 AM. 04: B7 cartas, B8 los 86, B10 las marcas; E sin cambios. Salen de G1 c0069, c0072, c0073, c0307, c0308 y c0310 (pasan a GM) |
| m1 | APLICADO | glosario «15 días antes» → `2 weeks out` |
| m2 | APLICADO | G1 c0156 |
| m3 | APLICADO | c0086 (01 B6, heredada del base; pasa a pendientes con `_DATE_KIT`), c0142 y c0155 |
| m4 | APLICADO | G1 c0397, c0135 y c0154 (heredada de la hamburguesería, pasa a pendientes con `_UTENSILIOS`); `REGLAS_US['utensilios_4h']` |
| m5 | APLICADO | `POR_CELDA` 05 B15 (sin comillas rectas: «Hot Station tab in 02, task #1»); G1 c0129 |
| m6 | APLICADO | `POR_CELDA` 05 B8 y E8 `Semiannual` |
| m7 | APLICADO | `POR_CELDA` 05 B13 |
| m8 | APLICADO | `POR_CELDA` 05 B14; G1 c0338 (+ grease trap) |
| m9 | APLICADO | `POR_CELDA` 05 B7 |
| m10 | APLICADO | G1 c0131; `_COCCION` |
| m11 | APLICADO | `POR_CELDA` C24, C25 y C27 = `pt`; `VALORES_EN` D24, D25 y D27 = 1; `cruzar_censo`, factor L → pt; `REGLAS_US['inventario']` |
| m12 | APLICADO | `POR_CELDA` 08 E5 = `8:45 AM` |
| m13 | APLICADO | G1 c0281 |
| m14 | APLICADO | G1 c0052, con «(task #30)» en vez de «(row 30)»: B40 es la tarea nº 30 (columna #), no la fila 30 de Excel |
| m15 | APLICADO | G1 c0249 |
| m16 | APLICADO | c0654 (heredada del base, pasa a pendientes con su ADAPTAR) = EN del base + la frase del informe, con «task #18» (B26 es la tarea nº 18) |
| m17 | APLICADO | c0596 (heredada del base, pasa a pendientes con ADAPTAR) = EN del base + la frase del informe |
| m18 | APLICADO | G1 c0147; `_ARROZ` |
| D1-D7 | NO APLICADO | Son dudas (por instrucción). D2 queda anotada para John en `SPEC.md` §5 |

**Resultado.** Construcción real con `--idempotencia --mes October`: 0 diferencias. Gates VERDE 8/0 y autotest 18/18.
censo-entregables y no-latinos a 0. Celdas cortadas: 0 nuevas. Detalle en `F2-NOTAS.md`.
