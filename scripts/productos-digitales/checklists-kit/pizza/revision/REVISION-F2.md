# Pizza Shop Checklists Kit Pro — revisión adversarial de F2 (18-oct-2026 · sesión Claude Code)

Revisor único. Fuentes: `pizza/revision/dump_en.txt` / `dump_es.txt` (3.666 líneas; «L» = línea del volcado EN),
`pizza/SPEC.md`, `pizza/F2-NOTAS.md`, `pizza/mapas_pizza.py` (`REGLAS_US`, `GRADOS_F_SPEC`) y las cuatro revisiones de
los hermanos. Solo lectura de volcados y un `openpyxl` corto sobre los xlsx (CPU 48-50 °C).

## Veredicto

**No hay nada BLOQUEANTE.** Lo que está, está bien:
- las fórmulas, la DV y la CF (`$F5`, y `$E5` en el 09);
- la caja;
- los °F y las citas FDA, NFPA, OSHA y FLSA;
- los alérgenos y el alcohol en las celdas donde aparece;
- las lecciones de los hermanos: sanitizante, 3-501.19, enfriamiento en dos fases, 165 °F en 2 h, aviso al consumidor,
  date marking y orden de los cierres 01 y 08.

**Hay 2 MAYORES** que un dueño de pizza shop de EE. UU. vería el primer día:
- el calendario de una pizzería no trae National Pizza Day ni National Pizza Month;
- el horno solo tiene objetivos de napolitana y romana, así que una pizza shop de horno de piso de gas o de cinta falla
  la lectura cada mañana.

**Además, 21 MENORES**, cuatro de ellos lecciones de los hermanos que reaparecen: «15 days out», el brindis gratis de
Nochevieja, la cronología del calendario y restos de bar o restaurante.

Todo se corrige con texto por celda (`POR_CELDA` / `ADAPTAR`). No hay filas nuevas, así que G1 y G6 siguen en paridad,
y ninguna corrección introduce °F fuera de `GRADOS_F_SPEC`.

| # | Sev. | Dónde | Qué |
|---|---|---|---|
| M1 | MAYOR | B02 Holiday Calendar B6/C6, B9/C9, B20/C20 | Faltan National Pizza Day (9-feb), National Pizza Month (oct.) y Pi Day |
| M2 | MAYOR | 01 B16 · 02 B6/B13/B15 · harina 00 en 01 B31, 03 B11, 05 A7 | Solo hay objetivos de napolitana / romana; ni horno de piso de gas, ni de cinta, ni harina high-gluten |
| m1 | MENOR | 01 Kitchen Closing B13/E13 · 04 Pizza Maker B21/E21 | La ceniza «en frío» a las 11:00 PM |
| m2 | MENOR | 08 Pizza Shop Opening B20/E20 | Horno a las 9:30 sin campana; en el 01, campana 9:45 y horno 10:00 |
| m3 | MENOR | 08 Pizza Shop Opening B21 | 3-501.19 sin procedimiento escrito |
| m4 | MENOR | B02 C26 | Brindis de Nochevieja sin «regalar alcohol, según el estado» |
| m5 | MENOR | 04 Server B13 | Falta «no servir a visiblemente ebrios» |
| m6 | MENOR | 06 Holiday Season E12 | «15 days out» (ya corregido en la cafetería) |
| m7 | MENOR | B02 C20 | «(no cocktails)» |
| m8 | MENOR | B02 C18 | «Holiday service» = «servicio de festivo» (calco) |
| m9 | MENOR | B02 C19 | «back-to-routine crowd» (calco de «vuelta a la rutina») |
| m10 | MENOR | B02 A10, A13 (+ orden) | Cuaresma «March–April» y playoffs «May» |
| m11 | MENOR | 06 Game Night B14/E14 | «Turn on the delivery apps early» a las 5:00 PM, cuando ya están encendidas desde las 11:30 AM |
| m12 | MENOR | 04 Shift Manager B20, E6 | «alarm, lights, gas», al revés que el 08; apertura a las 10:00 frente a las 9:00 del 08 |
| m13 | MENOR | 01 Kitchen Opening D10 | El control de salud lo hace el pizza maker y no el responsable del turno |
| m14 | MENOR | 01 Kitchen Closing B10 | «Date-mark everything… keeps 7 days» |
| m15 | MENOR | 01 Kitchen Closing B15 | «follow the manufacturers» (incompleto) |
| m16 | MENOR | 02 Make Line B6 | La make line no anota la temperatura |
| m17 | MENOR | 04 Delivery Driver B18 | Falta el reembolso de kilometraje (FLSA) |
| m18 | MENOR | 05 Daily Inventory A42 | «Delivery bags» ×30: ¿bolsa térmica o desechable? |
| m19 | MENOR | 03 B14 · 05 Monthly B11, B12 | «softener salt» y «replace filters» cada mes |
| m20 | MENOR | 05 Instructions B8 · Weekly D8 | Lo que promete la instrucción no casa con «Technician» en la hoja |
| m21 | MENOR | BONUS-01 B6, B26 · 07 By Area A19/C20:C24 | «Bar staff» sin repartidores; sección «BAR» en una pizza shop |

---

## MAYORES

### M1 · BONUS-02 «Holiday Calendar»: faltan National Pizza Day, National Pizza Month y Pi Day

**Dónde:** B6 (L3563), C6 (L3564), B9 (L3575), C9 (L3576), B20 (L3619) y C20 (L3620). De paso, `REGLAS_US['dias_fuertes']`.

**Qué falla.** El bonus se vende como «Pizza Shop Holiday & Busy Days Calendar (US)». Sin embargo:
- no trae ni el **National Pizza Day (9 de febrero)** ni el **National Pizza Month (octubre)**, los dos días de
  marketing que cualquier pizza shop de EE. UU. tiene en su calendario;
- tampoco el **Pi Day (14 de marzo)**, con sus ofertas a $3.14.

El encargo lo pedía expresamente. Sobran filas libres, pero un comprador lo vería como olvido: la estructura fija
(filas 5-26) se mantiene metiendo cada fecha en la fila de su mes.

**Corrección EN** (A se queda igual):
- **B6:** `Feb 9 — National Pizza Day + Super Bowl Sunday (2nd Sunday in Feb)`
- **C6:** `National Pizza Day: a one-day deal and a social post. Super Bowl: pre-orders and big party orders, dough balls cold-fermenting ahead, extra drivers and boxes, a short menu to push more orders per hour`
- **B9:** `Mar 14 — Pi Day + Mar 17 — St. Patrick's Day + March Madness`
- **C9:** `Pi Day: a $3.14 deal or a pie special. St. Patrick's: themed specials. March Madness games (mid-March to early April) lift delivery: extra drivers; beer only with a license, 21+ with ID`
- **B20:** `National Pizza Month + Oct 31 — Halloween`
- **C20:** `National Pizza Month: a pizza of the week or a loyalty push all month. Halloween: big delivery night: extra dough, boxes and drivers; themed decor and special pizzas` (también arregla m7)
- **`REGLAS_US['dias_fuertes']`:** añadir «National Pizza Day (9 feb), Pi Day (14 mar), National Pizza Month (octubre)», todo como `[criterio del kit] calendario comercial US`.

### M2 · El horno solo tiene objetivos de napolitana y romana; la pizza shop estándar de EE. UU. no aparece

**Dónde:**
- 01 «Kitchen Opening» B16 (L89): `Check oven temp: 750–840 °F (Neapolitan)`;
- 02 «Pizza Oven Station» B6 (L546) `750–840 °F Neapolitan / 570 °F Roman`, B13 (L577) `60–90 sec Neapolitan / 3–5 min Roman` y B15 (L587) `leopard spotting`;
- harina «00» como única harina de trabajo: 01 B31 (L156), 03 «Manager Weekly» B11 (L961) y 05 «Daily Inventory» A7 (L1696).

**Qué falla.** El ES es de una pizzería napolitana española, con horno de leña o de piedra. El kit EN se vende como
«Pizza Shop», y el título SEO y el H1 dicen «Pizzeria Opening & Closing». Pero la pizza shop independiente típica de
EE. UU. es NY-style o de barrio:
- horno de piso de gas a unos 500-550 °F, o de cinta (conveyor) a unos 450-500 °F;
- harina high-gluten o bread flour.

Con la celda actual, esa tienda anota cada mañana 550 °F frente a un objetivo de «750–840 °F», es decir, la checklist
le dice a diario que su horno está fuera de rango. La SPEC (D-PIZ) dice «wood-fired / deck», pero el texto solo da los
números de la napolitana.

**Norma o fuente:** `REGLAS_US['horno_temp']` y `['horno_fabricante']`: el objetivo es el de la receta y el fabricante.

**Corrección EN.** Sin cifras nuevas: G7 no cambia y `GRADOS_F_SPEC` vale tal cual.
- **01 B16:** `Check oven temp against your oven's target (wood-fired Neapolitan 750–840 °F; gas deck, conveyor or electric: per your recipe and manufacturer) — target: ____ °F · reading: ____ °F`
- **02 B6:** `Check oven temp: 750–840 °F Neapolitan / 570 °F Roman; gas deck or conveyor: your recipe's target — log reading: ____ °F`
- **02 B13:** `Watch bake time: 60–90 sec Neapolitan / 3–5 min Roman; deck or conveyor: your recipe's time`
- **02 B15:** `Check doneness: browned rim and crisp bottom (leopard spotting on Neapolitan), not burnt`
- **01 B31:** `Check flour stock (00, high-gluten or bread flour, whole wheat)`
- **03 B11:** `Weekly flour order (00 or high-gluten, semolina)`
- **05 A7:** `00 or high-gluten flour` (por `POR_CELDA`, ya que A7 está en el glosario o en `VALORES_EN`)

Si se quiere dar cifras de deck o conveyor, por ejemplo 500-550 °F, antes hay que añadirlas a `GRADOS_F_SPEC` y a
`REGLAS_US['horno_temp']` como `[fabricante]`.

---

## MENORES

### m1 · La ceniza «en frío» a la hora del cierre: la errata ES del SPEC §5 solo está medio corregida

**Dónde:**
- 01 «Kitchen Closing» B13 (L342) `Remove ash only when cold (at close, or first thing next morning)…` con E13 (L345) `11:00 PM`;
- 04 «Pizza Maker» B21 (L1299) `Remove oven ash when cold…` con E21 (L1302) `11:00 PM`.

**Qué falla.** Un horno de leña que se deja enfriar a las 10:30 PM no está frío a las 11:00 PM. La 04 ni siquiera
ofrece lo de «next morning».

**Norma.** NFPA 96, cap. 14 (solid fuel). En la edición 2017:
- §14.9.3.8: contenedor metálico cerrado, a 3 ft o más de cualquier aparato de cocción;
- §14.9.3.8.1: chapa de calibre 16 o más, con tapa.

La numeración cambia de una edición a otra, así que conviene mantener la cita **general «(NFPA 96)»**, como ya está.

**Corrección EN** (en las dos celdas):
- **01 B13 y 04 B21:** `Ash: never take it out hot at close; remove it cold, usually first thing next morning before lighting, into a closed METAL container kept at least 3 ft from the oven, never trash or plastic (NFPA 96)`
- **E13 y E21:** `Next AM`

### m2 · 08 «Pizza Shop Opening» B20 (L2806) / E20 (L2809): horno a las 9:30 AM y sin campana

**Qué falla.** El 01 «Kitchen Opening» enciende la campana a las 9:45 (B12), revisa el gas a las 9:50 y enciende el
horno a las 10:00 (B15), y dice «exhaust hood BEFORE lighting the oven». El 08, que se presenta como «backbone of the
day», enciende el horno de leña a las 9:30 sin nombrar la campana. Quien use solo el 08 enciende con la extracción
apagada.

**Norma.** NFPA 96, cap. 14: la extracción de combustible sólido debe funcionar mientras haya fuego.

**Corrección EN:**
- **B20:** `Exhaust hood on, then light the oven (preheat per manufacturer; 1 h as a guide; detail in 01, Kitchen Opening)`
- **E20:** `10:00 AM`

### m3 · 08 «Pizza Shop Opening» B21 (L2811): pizza por porciones sin procedimiento escrito

**Qué falla.** La regla de las 4 h y el descarte está bien. Lo que falta es que §3-501.19(A) exige un procedimiento
escrito, preparado de antemano y a disposición del inspector. Además, «Set up the pizza counter if visible» es la
traducción literal de «barra de pizza si es visible».

**Corrección EN:** `Set up the slice counter if you sell by the slice: hot case at 135 °F or above, or time-marked and tossed at 4 h with a written procedure on file (FDA 3-501.19)`

### m4 · BONUS-02 C26 (L3644): el brindis de medianoche sin la regla de regalar alcohol

**Qué falla.** San Valentín (06 B14) sí dice «only where your license and state allow giving alcohol away». Nochevieja
ofrece «a midnight toast», que se lee como gratis, solo con «if your license allows». Algunos estados prohíben las
bebidas gratis; por ejemplo, Massachusetts (204 CMR 4.03). Es la misma lección del bar y de la cafetería.

**Norma:** `REGLAS_US['alcohol_gratis']`.

**Corrección EN:** `Big delivery night: extra dough and drivers, closing hours; if the dining room is open, party favors and a midnight toast (alcohol only if your license allows and, if it's free, only where your state allows giving alcohol away; 21+ with ID); night shifts`

### m5 · 04 «Server» B13 (L1527): servir cerveza o vino sin el corte de servicio

**Qué falla.** El bar (M6) lo añadió a las fichas de quien sirve. Aquí hay ID y 21+, pero falta no servir a quien
está visiblemente ebrio. Esa es la base de la responsabilidad civil del local (dram shop), y la ley estatal de
alcoholes la prohíbe.

**Norma:** [estatal] ABC.

**Corrección EN:** `Serve pizzas and drinks (beer and wine only if your license allows; 21+ with ID; never serve anyone visibly intoxicated)`

### m6 · 06 «Holiday Season» E12 (L2372): `15 days out`

**Qué falla.** En la cafetería ya se corrigió (m15 → «2 weeks out») y aquí reaparece.

**Corrección EN:** `2 weeks out`

### m7 · BONUS-02 C20 (L3620): «themed decor and special pizzas (no cocktails)»

**Qué falla.** Es el resto del ES «menú/cocktails especiales» después de quitar el alcohol. En inglés, ese
«(no cocktails)» es incomprensible.

**Corrección EN:** el C20 de M1; si M1 no se aplica, `Big delivery night: extra dough, boxes and drivers; themed decor and special pizzas`

### m8 · BONUS-02 C18 (L3612): «Holiday service»

**Qué falla.** Viene de «Servicio de festivo», y la fila ES era el 15 de agosto. En inglés de EE. UU., «holiday» es un
festivo; con el sentido de «vacaciones» es británico.

**Corrección EN:** `Summer hours and menu, staff vacations; extra staff and drivers where summer is busy (beach and tourist areas); patio at full capacity`

### m9 · BONUS-02 C19 (L3616): «back-to-routine crowd»

**Qué falla.** Es un calco de «vuelta a la rutina». Además, el fútbol americano no se juega solo domingo y lunes.

**Corrección EN:** `Fall menu, back-to-school lunch specials and game-day deals for football: Thursday, Sunday and Monday night games and college Saturdays lift delivery`

### m10 · BONUS-02: las etiquetas de mes de Cuaresma y de los playoffs, y la cronología

**Dónde:** A10 (L3578) y A13 (L3590).

**Qué falla.**
- La Cuaresma empieza el Miércoles de Ceniza, entre el 4 de febrero y el 10 de marzo: en 2026 fue el 18 de febrero y en
  2027 es el 10 de febrero. Los «Lent Fridays» empiezan, pues, casi siempre en **febrero**, y A10 dice «March–April».
- Los playoffs de la NBA y de la NHL empiezan a mediados de **abril**, y A13 dice «May».

Con las etiquetas bien, el orden cronológico (la lección M10 del catering) pide dos intercambios.

**Corrección EN:**
- **A10:** `February–April`; después, intercambiar el contenido completo (A:D) de las filas 9 y 10: Cuaresma va justo detrás de Mardi Gras y antes que el 17 de marzo.
- **A13:** `April–June`; después, intercambiar A:D de las filas 12 y 13: los playoffs antes que «May–June Graduation season».

El B02 no tiene fórmulas ni DV: el intercambio es seguro.

### m11 · 06 «Game Night» B14 (L2245) / E14 (L2248): «Turn on the delivery apps early» a las 5:00 PM

**Qué falla.** El ES «activar apps con tiempo, 17:00» tenía sentido con un partido a las 21:00. En el kit EN las tablets
ya se encienden a diario a las 11:30 AM (01 «FOH Opening» B18, 04 «Shift Manager» B9), así que la tarea no significa
nada.

**Corrección EN:**
- **B14:** `Check every delivery app is live and set longer prep times for the rush`
- **E14:** `2 h before kickoff`

### m12 · 04 «Shift Manager»: el cierre en orden inverso y la apertura una hora después que el 08

**Dónde:** B20 (L1470) y E6 (L1411).

**Qué falla.**
- B20 dice «Close the shop: alarm, lights, gas». Es el orden que la SPEC D10 corrigió en el 01 y en el 08: alarma al
  final.
- E6 abre y desarma la alarma a las 10:00 AM. El 08 «Pizza Shop Opening» E5 lo hace a las 9:00 AM, con el mismo rol, y
  la higiene del equipo del 01 es a las 9:00.

**Corrección EN:**
- **B20:** `Close the shop: gas off, lights off, then set the alarm`
- **E6:** `9:00 AM`

### m13 · 01 «Kitchen Opening» D10 (L65): el control de salud del equipo lo hace el «Pizza maker»

**Qué falla.** Según FDA 2-201.11, quien recibe los avisos de síntomas y excluye o restringe es el person in charge, no
un compañero. En el ES era el «Pizzero».

**Corrección EN (D10):** `Shift manager`

### m14 · 01 «Kitchen Closing» B10 (L331): «Date-mark everything: ready-to-eat food keeps 7 days at 41 °F»

**Qué falla.** §3-501.17 pide marcar fecha a la comida RTE y TCS que se guarda más de 24 h, con 7 días **como
máximo**. «Keeps 7 days» suena a que todo dura 7 días.

**Corrección EN:** `Date-mark ready-to-eat TCS food kept over 24 h: 7 days max at 41 °F or below, prep day = day 1 (FDA 3-501.17)`

### m15 · 01 «Kitchen Closing» B15 (L352): «follow the manufacturers»

**Qué falla.** La frase queda incompleta.

**Corrección EN:** `Turn off the exhaust hood (wood-fired oven: not while fire or embers remain; follow the oven and hood manufacturers' instructions)`

### m16 · 02 «Make Line» B6 (L644): la make line no registra la lectura

**Qué falla.** La make line abierta es el punto que más mira el inspector de una pizza shop, y en todo el kit no hay
ninguna lectura de su temperatura, mientras que el horno y la cámara sí tienen «log reading».

**Corrección EN:** `Set up make line inserts: tomato sauce, mozzarella, toppings — all at 41 °F or below (FDA 3-501.16); don't fill above the cold line and keep the lid closed between orders — log reading: ____ °F`

### m17 · 04 «Delivery Driver» B18 (L1636): falta el reembolso de kilometraje

**Qué falla.** Es el riesgo laboral número uno del reparto de pizza en EE. UU., con demandas colectivas contra las
grandes cadenas. Con coche propio, los costes del vehículo no pueden dejar el salario por debajo del mínimo.

**Norma:** 29 CFR 531.35 («free and clear») y DOL Field Operations Handbook 30c15.

**Corrección EN:** `Report delivery issues and log your miles: drivers using their own car get reimbursed so vehicle costs never push pay below minimum wage (FLSA)`

Hay que añadir `REGLAS_US['kilometraje']` con la fuente 29 CFR 531.35. La celda solo cita «FLSA», que ya está en
`REGLAS_US`.

### m18 · 05 «Daily Inventory» A42 (L1821): «Delivery bags», mínimo 30 «ea»

**Qué falla.** El resto del kit llama «delivery bag» a la bolsa térmica (04 «Delivery Driver» B7: «hot bag (insulated
delivery bag)»). Treinta bolsas térmicas como mínimo diario es absurdo; lo que se quiere decir es la bolsa desechable.

**Corrección EN (A42):** `To-go bags (paper / plastic)`

### m19 · «softener salt» y «replace filters» cada mes (restos europeos)

**Dónde:** 03 «Manager Monthly» B14 (L1075) y 05 «Monthly Maintenance» B11 (L2053) para la sal; 05 B12 (L2058) para los
filtros.

**Qué falla.**
- Los lavavajillas comerciales de EE. UU. no llevan descalcificador de sal integrado; el ablandador, si lo hay, va aparte.
- Los filtros de lamas (baffle) de la campana se desengrasan, no se sustituyen cada mes. Además, ya se desengrasan cada
  semana (05 «Weekly Deep Clean» B12).

**Corrección EN:**
- **03 B14 y 05 B11:** `Dish machine: filters, rinse aid and chemical levels (water softener salt only if you have a softener)`
- **05 B12:** `Exhaust hood: degrease the hood and check the filters (replace only bent or damaged ones); the contractor cleans the DUCTS (see "Quarterly & Annual")`

### m20 · Lo que promete 05 «Instructions» B8 frente a «Technician» en las hojas

**Dónde:** 05 «Instructions» B8 (L1658) y 05 «Weekly Deep Clean» D8 (L1853).

**Qué falla.**
- B8 dice que la pestaña mensual recoge «the checks your own team does». Pero «Monthly Maintenance» asigna 6 de sus 9
  tareas a «Technician» (L2034, L2039, L2044, L2049, L2060, L2065).
- «Weekly Deep Clean» B8 dice «Team cleans the oven mouth…», y su D8 es «Technician» cada lunes.

**Corrección EN:**
- **05 «Instructions» B8:** `▸ The monthly tab mixes your team's own checks (hood filters, a look at the extinguisher, first-aid kit) with the monthly ones for a technician or qualified person (oven, wood-fired exhaust, gas valves): they don't replace the contracted services in "Quarterly & Annual", they prepare for them.`
- **05 «Weekly Deep Clean» D8:** `Pizza maker`

### m21 · Restos de bar y de restaurante en el BONUS-01 y en el 07

**Dónde:** BONUS-01 B26 (L3520) y B6 (L3502); 07 «By Area» A19 (L2602) y C20:C24 (L2604-L2612).

**Qué falla.**
- El huddle de una pizza shop tiene «Bar staff» pero no tiene **repartidores**.
- «Expected covers» solo cuenta comensales en sala.
- En el 07, «BAR» viene del ES «BARRA», que en una pizzería española es el mostrador.

**Corrección EN:**
- **B01 B26:** `Drivers on shift (and bar staff, if any):`
- **B01 B6:** `Expected covers + delivery / carryout orders:`
- **07 A19:** `  COUNTER / BAR — type your counter or bar tasks below`
- **07 C20:C24:** `Counter / bar`

---

## DUDAS (no demostradas, fuera de la ronda salvo que el orquestador decida)

- **D1 · Precalentado de 45-60 min (01 B15, L84; 08 B20, «1 h»).** Con gas es razonable. Un horno de leña en frío suele
  necesitar 1½-2 h según los fabricantes, y menos con el calor del día anterior. La celda ya remite al fabricante.
- **D2 · Mínimos del inventario (05 D6:D42).** Son enteros (comprobado con `openpyxl`: 32 int) y las conversiones son
  exactas (×2,2; ÷28,35). Son coherentes con una tienda pequeña de unas 30 bolas al día. Las cifras raras (22 lb,
  11 lb, 7 lb, 7 oz y 10 oz) delatan la conversión de 10 kg, 5 kg, 3 kg, 200 g y 300 g. Los envases de EE. UU. son el
  saco de harina de 50 lb y los bloques o bolsas de mozzarella de 5-6 lb. Redondear (25 / 10 / 10 lb, 8 / 12 oz) sería
  más creíble. No es un error.
- **D3 · Super Bowl LXI = 14 de febrero de 2027 = San Valentín** (confirmado: SoFi, segundo domingo). Quien compre ahora
  y planifique febrero agradecería una nota, pero el calendario es atemporal («Year: ______»). «2nd Sunday in Feb» es
  correcto para la temporada actual de 17 partidos.
- **D4 · 01 «Kitchen Closing» B17 (L358): «lightly flour» la mesa de amasado al cerrar.** Es heredado. En mesa de madera
  (§4-101.17 la permite como «bakers' table») es práctica habitual. En acero inoxidable deja residuo de comida toda la
  noche (§4-601.11).
- **D5 · Inspección del horno por técnico cada mes (03 B13, L1070; 05 B6, L2032).** Una pizza shop independiente rara
  vez tiene un técnico al mes; en 05 «Quarterly & Annual» B8 ya hay una revisión anual por el fabricante. ¿D = Manager?
- **D6 · Horno de cinta (conveyor).** No hay tareas de limpieza de cinta, dedos y quemadores. Si M2 se aplica, va a
  una v2.1 con filas nuevas.

## Lo que intenté refutar y se sostiene

- **Normas, comprobadas una a una contra la celda:**
  - §2-201.11 (síntomas), §3-302.11 (crudo separado), §3-403.11 (165 °F en 2 h), §3-501.13 (descongelar a 41 °F);
  - §3-501.14 (135 → 70 °F en 2 h y → 41 °F en 4 h más), §3-501.16 (41 / 135 °F), §3-501.17(B) (7 días, día 1 =
    apertura, sin pasar el use-by);
  - pepperoni y prosciutto «per the maker's label», coherente con la exención §3-501.17(G) de los curados estables;
  - §3-501.19 (las porciones se tiran a las 4 h), §3-603.11 (carbonara y tiramisú), §4-501.114 (tiras), §5-202.12
    (agua de manos a 100 °F).
  - NFPA 96: extinción cada 6 meses (§11.2.1); tabla 11.4 con inspección **mensual** si hay combustible sólido
    (correcto) y trimestral o semestral según volumen; limpieza cuando hay depósitos (§11.6).
  - Ceniza en metálico con tapa, nunca a la basura: correcto (2017 §14.9.3.8 y §14.9.3.8.1). La cita general «(NFPA 96)»
    es la adecuada.
  - OSHA 1910.157(e)(2) mensual y (e)(3) anual; (f) hidrostática de 5 años para Clase K y CO2.
  - FLSA 203(m)(2)(B); 29 CFR 516 (2 y 3 años; NY 6); EPA 608; 40 CFR 141 Subpart O.
- **Horno:**
  - 750–840 °F = 400–450 °C y 570 °F = 300 °C: conversiones exactas y realistas para napolitana y romana (AVPN: suelo
    de unos 430 °C); el fallo es de cobertura (M2), no de cifra;
  - cocción de 60–90 s en la napolitana;
  - leña lejos de la boca;
  - nunca apagar con agua;
  - campana antes del fuego en el 01;
  - campana encendida mientras haya brasas.
- **Masa, make line y queso:**
  - cold fermentation a 41 °F o menos, tapada, con fecha y hora;
  - masa cruda no TCS, como criterio del kit;
  - inserts a 41 °F o menos;
  - mozzarella TCS con date marking;
  - salchicha cruda en su propio insert.
- **Delivery:**
  - bolsa caliente a 135 °F o más y frío aparte a 41 °F o menos;
  - propinas del repartidor bien citadas;
  - «hired and non-owned auto» bien descrito, como criterio del kit, y aviso de que la póliza personal puede excluir el
    reparto;
  - apps de EE. UU.
- **Alérgenos:** los 9 de EE. UU. con sésamo; trigo sí y gluten no; lactosa como intolerancia; UK: 14 (L1522, L2343).
- **Alcohol:** cerveza solo con licencia y 21+; prosecco de bienvenida «where your license and state allow»; ningún
  2-for-1 ni barra libre; los «game-day/game-night deals» no mencionan alcohol.
- **Calendario:**
  - Super Bowl en el segundo domingo; March Madness de mediados de marzo a principios de abril;
  - Mother's Day el segundo domingo de mayo, Memorial Day el último lunes, Father's Day el tercer domingo, Labor Day el
    primer lunes, Thanksgiving el cuarto jueves;
  - la víspera de Thanksgiving y Halloween como noches fuertes;
  - sin Reyes, cava ni uvas.
- **Restos de español:** ningún €, °C, kg, ml, IVA, APPCC, TPV ni hora de 24 h en las 3.666 líneas. Las 4 celdas ES con
  °C están convertidas (L89, L110, L546 y L1984).
- **Técnica:**
  - DV: en cada hoja salta las filas de sección;
  - CF: `$F5` (y `$E5` en el 09), sin cabeceras internas con ✓;
  - contadores B5:Bn por hoja;
  - mínimos como número y fórmula de estado correcta;
  - inventario sin proteger, como promete 05 B24, que corrige la errata ES;
  - caja: 25¢ roll = $10 y 10¢ roll = $5; penny fuera de producción desde 2025, pero de curso legal;
  - B02 sin fórmulas, así que se pueden reordenar filas.
- **Orden de los cierres:** el 01 «FOH Closing» deja la alarma al final, en «Lock-Up», y el 08 «Pizza Shop Closing»
  enfría el horno al principio y termina con alarma, puertas y llave. Las 14 tareas del ES están todas en los dos.
- **Textos cortados:** heurística ancho × líneas sobre todas las celdas de más de 60 caracteres, combinadas o sin ajuste.
  Solo salen 2 límites, y los dos caben:
  - 05 FIFO D30, 96 caracteres en 2 líneas a 30 pt;
  - 09 «Monthly Cash Log» A37, 484 caracteres a 9 pt en 3 líneas a 36,75 pt.
  Las filas largas con ajuste y sin alto fijo se autoajustan, como en el base.

## Ronda 1: aplicado / no aplicado (18-oct-2026 · sesión Claude Code)

Todo en la fuente, con el EN exacto del informe: `G1.json` (28 cadenas reescritas; c0858, c0861, c0867 y c0870 salen
porque sus celdas pasan a `POR_CELDA`: 377 ids = `pendientes.json`), `POR_CELDA` (+20), `ADAPTAR`, `REGLAS_US` y
`VALORES_EN`. Sin filas nuevas (G1 y G6 en paridad) y sin °F nuevos (`GRADOS_F_SPEC` igual).

| # | Estado | Dónde |
|---|---|---|
| M1 Pizza Day / Month / Pi Day | APLICADO | `CALENDARIO` B6, B10 (Pi Day tras el cambio de fila), B20; C6 = c0849, C20 = c0890, C10 por `POR_CELDA` (lleva «$3.14»: zona «$» legítima); `REGLAS_US['dias_fuertes']` |
| M2 horno y harina | APLICADO | c0051, c0162, c0170, c0172, c0068, c0245, c0396 (A7, que estaba en `G1.json`, no en el glosario); `_HORNO_F` y `REGLAS_US['horno_temp']` sin cifra nueva |
| m1 ceniza | APLICADO | c0116 y c0317 + `POR_CELDA` E13 / E21 «Next AM»; `REGLAS_US['ceniza']` (3 ft, contenedor cerrado), cita general «(NFPA 96)» |
| m2 campana → horno en el 08 | APLICADO | c0682 + `POR_CELDA` 08 E20 «10:00 AM» |
| m3 procedimiento escrito | APLICADO | c0683; `REGLAS_US['tphc']` |
| m4 brindis gratis | APLICADO | c0904 (`REGLAS_US['alcohol_gratis']`) |
| m5 visiblemente ebrio | APLICADO | c0350; `REGLAS_US['servicio_alcohol']` |
| m6 «15 days out» | APLICADO | `POR_CELDA` 06 «Holiday Season» E12 «2 weeks out» |
| m7 «(no cocktails)» | APLICADO | con M1 (c0890) |
| m8 «Holiday service» | APLICADO | c0884 |
| m9 «back-to-routine crowd» | APLICADO | c0887 |
| m10 cronología | APLICADO | filas 9↔10 y 12↔13: A, B y D por `CALENDARIO`; C por `POR_CELDA` (`_CAL_C`, el EN de la fila de origen); A9 «February–April», A12 «April–June» |
| m11 apps del Game Night | APLICADO | c0559 + `POR_CELDA` 06 «Game Night» E14 «2 h before kickoff» |
| m12 cierre del Shift Manager | APLICADO | c0342 + `POR_CELDA` 04 «Shift Manager» E6 «9:00 AM» |
| m13 control de salud | APLICADO | `POR_CELDA` 01 «Kitchen Opening» D10 «Shift manager» |
| m14 date marking | APLICADO | c0113 |
| m15 «follow the manufacturers» | APLICADO | c0118 |
| m16 lectura de la make line | APLICADO | c0181 (fila existente enriquecida) |
| m17 kilometraje | APLICADO | c0371; `REGLAS_US['kilometraje']` (29 CFR 531.35; DOL FOH 30c15); la celda cita «(FLSA)» |
| m18 «Delivery bags» | APLICADO | c0436 «To-go bags (paper / plastic)» |
| m19 sal y filtros | APLICADO | c0272 (03 B14 y 05 B11) y c0501 |
| m20 promesa del 05 | APLICADO | c0382 + `POR_CELDA` 05 «Weekly Deep Clean» D8 «Pizza maker» |
| m21 bar en B01 y 07 | APLICADO | `POR_CELDA` B01 B26 y B6, 07 «By Area» A19 y C20:C24 «Counter / bar» |
| D2 mínimos del inventario | APLICADO (aprobada) | `VALORES_EN`: harina 25 lb, semolina 10, sal 5, mozzarella 10, pepperoni 5, pesto 12 oz, aceite de trufa 4 fl oz, anchoas 8 oz, rúcula 8 oz; criterio en SPEC D-INV; tolerancia de `cruzar_censo` a ×1,6 |
| D1, D3-D6 | NO APLICADO | dudas no demostradas o que piden filas nuevas (conveyor, técnico mensual): v2.1 |

Resultado: montaje con idempotencia 0; gates VERDE 8/0; autotest 18/18; censo 0; no latinos 0; heurística de textos
cortados 0 avisos en 2.558 celdas; 4 hermanos idénticos (ver `F2-NOTAS.md`).
