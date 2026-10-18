# Burger Joint Checklists Kit Pro — revisión adversarial de F2 (18-oct-2026 · sesión Claude Code)

Revisor único. Fuentes:
- `burger/revision/dump_en.txt` / `dump_es.txt`, 3.512 líneas; «L» = línea del volcado EN;
- `burger/SPEC.md`, `burger/F2-NOTAS.md`, `burger/mapas_burger.py` (`REGLAS_US`, `GRADOS_F_SPEC`, `TERMINOS_PROHIBIDOS`) y
  `mapas.py` (`REGLAS_US` del base);
- las revisiones del base y de la pizzería.

Solo lectura de los volcados y un `openpyxl` corto sobre el 05 «Daily Inventory», con la CPU a 52-54 °C. Dos
comprobaciones en la web: §3-401.11(D)(2) y el National Burger Day del Reino Unido.

## Veredicto

**No hay nada BLOQUEANTE.** Lo que está, está bien:
- la carne picada: 155 °F / 17 s y su tabla 145 / 150 / 158;
- poco hecha solo a petición y con aviso al consumidor, y nunca en el menú infantil: la cita de la SPEC, 3-401.11(D), es
  la correcta, porque el (D)(2) es el del menú infantil y el (C) es el del filete entero;
- el pollo a 165 °F, el bacon (enfriamiento en dos fases y recalentado a 165 °F en 2 h) y el TPHC con procedimiento
  escrito;
- los alérgenos del bun, el alcohol y las lecciones de los hermanos (con una excepción, m1);
- el orden de la apertura del 01 y del cierre del 08;
- las fórmulas, la DV, la CF y la caja.

**Hay 2 MAYORES** que un kitchen manager de EE. UU. vería el primer día:
- el «Full fryer oil change» MENSUAL, que contradice el TPM del propio kit;
- un burger joint estadounidense sin queso americano.

**Además, 12 MENORES.** Uno es una lección de los hermanos que reaparece: «15 days out». Otro es una incoherencia que
nació al quitar los «40 °C» del ES: se dice «let it cool» antes de filtrar en caliente.

Todo se corrige con texto por celda (`POR_CELDA` / G1). No hay filas nuevas, así que G1 y G6 siguen en paridad, y
ningún °F queda fuera de `GRADOS_F_SPEC`. Solo m6 pide una cita nueva en `REGLAS_US` (§4-602.11(C)).

| # | Sev. | Dónde | Qué |
|---|---|---|---|
| M1 | MAYOR | 03 «Manager Monthly» B13 (L1033) · 05 «Monthly Maintenance» B7 (L1892) | «Full fryer oil change» cada mes |
| M2 | MAYOR | 01 «Kitchen Opening» B26 (L135) · 05 «Daily Inventory» A15 (L1625) | No hay queso americano |
| m1 | MENOR | 06 «Holiday Season» E13 (L2223) | «15 days out» reaparece |
| m2 | MENOR | 01 «Kitchen Closing» B13/B14 · 02 «Fry Station» B18/B19 · 04 «Fry Cook» B14/B15 | «let it cool» y luego «filter hot» |
| m3 | MENOR | 01 «Kitchen Closing» B6 (L311) · 04 «Grill Cook» B18 (L1242) | Picada «bottom shelf» con pollo crudo en el kit |
| m4 | MENOR | 02 «Make Line» B6 (L618) | La make line no anota su temperatura (lección m16 de la pizzería) |
| m5 | MENOR | 02 «Grill Station» B10 (L545) · 05 «Quarterly & Annual» B20 (L1999) | La sonda se calibra 1 vez al año; «griddle probe» |
| m6 | MENOR | 02 «Grill Station» B17 (L576) | Espátulas y prensa de crudo solo se lavan al cierre (4-602.11, cada 4 h) |
| m7 | MENOR | 05 «Quarterly & Annual» B14 (L1978) · 05 «Instructions» B6 (L1559) | Falta la trampa de grasa (FOG) |
| m8 | MENOR | 05 «Quarterly & Annual» B13/E13 (L1974/L1976) | Retirada de aceite usado «Quarterly» |
| m9 | MENOR | 05 «Quarterly & Annual» E8 (L1959) | La supresión semestral, bajo «Annual» |
| m10 | MENOR | 05 «Weekly Deep Clean» B6 (L1727) · 03 «Manager Monthly» B12 (L1028) | «Take apart» la plancha (flat-top) |
| m11 | MENOR | 04 «Grill Cook» E9 (L1208) | Bacon precocinado a las 10:45 y plancha a las 11:00 |
| m12 | MENOR | BONUS-02 «Instructions» B8 (L3384) | La nota UK no trae el National Burger Day del Reino Unido |

---

## MAYORES

### M1 · «Full fryer oil change» con frecuencia MENSUAL

**Dónde:**
- 03 «Manager Monthly»: B13 (L1033), D13 «Manager» y E13 «Monthly» (L1036);
- 05 «Monthly Maintenance»: B7 (L1892), D7 «Manager» y E7 «Monthly».

**Qué falla.** En un burger joint que fríe patatas todo el día, el aceite dura días y no un mes. El propio kit lo dice en
cuatro sitios:
- 02 «Fry Station» B6 (L706): «change per the tester and fryer manufacturer»;
- 03 «Manager Weekly» B19 (L971);
- 05 «Weekly FIFO Check» B15 (L1830);
- `REGLAS_US['aceite']`.

Una fila mensual de «Full fryer oil change» se lee como «el aceite se cambia una vez al mes»: es un error de calidad y
choca con el TPM del kit. Viene del ES («Cambiar aceite de freidora completo», Mensual), pero en el ES lo tapaba el test
de polares; aquí la contradicción se ve.

**Norma o fuente:** `REGLAS_US['aceite']` (fabricante + TPM). El «boil-out» mensual (o semanal) es la tarea que sí
lleva fecha fija.

**Corrección EN** (en B13 del 03 y en B7 del 05; D y E se quedan igual):
- `Fryer boil-out: drain, clean with fryer cleaner and refill with fresh oil, per the manufacturer (the oil itself is changed whenever the TPM tester says, not once a month)`

**Errata para el ES v2.x:** la misma.

### M2 · Un burger joint de EE. UU. sin queso americano

**Dónde:** 01 «Kitchen Opening» B26 (L135), `Slice cheese: cheddar, gouda, blue cheese, Swiss`, y 05 «Daily Inventory»
A15 (L1625), `Cheddar slices`, con mínimo de 50 «ea».

**Qué falla.** El queso americano es el queso por defecto de la hamburguesa en EE. UU.: el cheeseburger clásico, el
smash y lo que piden In-N-Out, Shake Shack o Five Guys. Que no aparezca ni en el mise en place ni en el inventario es
la señal más clara de que el kit viene de fuera. Es el equivalente al «National Pizza Day» que faltaba en la pizzería
(M1 allí). El ES traía «cheddar, gouda, blue cheese, emmental». Swiss por emmental está bien.

**Corrección EN:**
- **01 B26:** `Slice cheese: American, cheddar, gouda, blue cheese, Swiss`
- **05 A15** (por `POR_CELDA` si está en glosario o en `VALORES_EN`): `American / cheddar slices`

D15 se queda en 50.

---

## MENORES

### m1 · 06 «Holiday Season» E13 (L2223): «15 days out»

**Qué falla.** Es la lección m15 de la cafetería y m6 de la pizzería, y F2-NOTAS la da por aprobada («2 weeks out»). En
este mismo kit, «Burger Week» E6 (L2130) ya dice `2 weeks out`.

**Corrección EN (E13):** `2 weeks out`

### m2 · «Let it cool» y luego «many filter hot»: la freidora se contradice

**Dónde:**
- 01 «Kitchen Closing» B13 (L342) y B14 (L347);
- 02 «Fry Station» B18 (L758) y B19 (L763);
- 04 «Fry Cook» B14 (L1373) y B15 (L1378).

**Qué falla.**
- En el ES, «apagar y dejar enfriar» precedía a «filtrar SOLO por debajo de 40 °C». La EN quitó los 40 °C
  (`CELSIUS_SIN_F`, bien) y dice «many filter hot by design», pero dejó la fila anterior: «Turn off the fryer and let it
  cool». Quien tenga filtrado integrado (lo normal en EE. UU.: Frymaster, Pitco) lee que primero enfríe y después filtre
  en caliente.
- 02 B19 conserva además «if dark or smelly» como criterio, cuando el kit usa el medidor de TPM.
- En la 04 se limpia la freidora (B14) antes de filtrar (B15).

**Norma o fuente:** `REGLAS_US['aceite']` ([fabricante]).

**Corrección EN** (sin °F nuevos; el autotest de `CELSIUS_SIN_F` sigue valiendo):
- **01 B13:** `Turn the fryer off after service; the hood stays on until the fryer and griddle have cooled`
- **01 B14 y 02 B19:** `Filter the oil every night as the fryer manufacturer says (built-in filtration usually runs with the oil still hot, right after service; a portable filter only once it has cooled to what the manual allows) and change it when the TPM tester says; heat-resistant gloves, apron and goggles`
- **02 B18:** `Turn off the fryer at the end of service`
- **04 B14:** `Turn off the fryer; clean the outside once the oil is filtered`
- **04 B15:** `Filter the oil as the fryer manufacturer says (built-in filtration: with the oil still hot; portable filter: once it has cooled to what the manual allows); heat-resistant gloves, apron and goggles`

### m3 · Picada cruda en la «bottom shelf» cuando el kit también guarda pollo crudo

**Dónde:** 01 «Kitchen Closing» B6 (L311) y 04 «Grill Cook» B18 (L1242): `…41 °F or below, bottom shelf below ready-to-eat food (FDA 3-302.11)`.

**Qué falla.** §3-302.11(A)(2) también separa los crudos entre sí: el orden de estantes que enseña cualquier inspector
va por temperatura final de cocción, y el pollo (165 °F) va siempre el más bajo. El kit trae pollo crudo en varios
sitios:
- 05 «Daily Inventory» A9 «Breaded / crispy chicken»;
- la tabla del congelador B30, «Raw chicken (crispy, tenders, nuggets)»;
- los tenders de 02 B10.

Con «bottom shelf», la picada acaba debajo del pollo solo si este va arriba. Es la falta de cross-contamination que más
se ve en la walk-in de una hamburguesería.

**Corrección EN** (en las dos celdas; en la 04, «Store leftover beef labeled:» se mantiene):
- `Store leftover beef in the walk-in: raw ground beef covered, date-marked, 41 °F or below, below ready-to-eat food and above any raw chicken (FDA 3-302.11)`

### m4 · 02 «Make Line» B6 (L618): la make line no registra la lectura

**Qué falla.** Es la lección m16 de la pizzería, que no pasó a esta F2. La mesa refrigerada abierta es el punto que más
mira el inspector, y en todo el kit solo la walk-in tiene «log reading».

**Corrección EN:** el texto actual + ` — log reading: ____ °F`, es decir:
- `Set up inserts: lettuce, tomato, onion and pickles — raw-eaten produce washed under running potable water (FDA 3-302.15); if using a produce wash, only one approved for fruits and vegetables, at label dose, then RINSE. Inserts in the make-line cooler at 41 °F or below (FDA 3-501.16) — log reading: ____ °F`

### m5 · La sonda que decide los 155 °F se calibra una vez al año; «griddle probe»

**Dónde:** 05 «Quarterly & Annual» B20 (L1999), con D20 «Technician» y E20 «Annual», y 02 «Grill Station» B10 (L545),
`Check spatulas, presses, thermometer`.

**Qué falla.**
- El kit dice, con razón, que «the core temp of ground beef depends on that probe». Sin embargo, la única calibración es
  anual y la hace un técnico. La práctica US (ServSafe y los inspectores) es el ice-point a diario o cada semana, y
  siempre después de un golpe.
- «Griddle probe» no existe: la plancha tiene termostato, y el núcleo se mide con el termómetro de sonda del cocinero.

**Norma o fuente:** §4-502.11(B) pide calibrar «as necessary to ensure their accuracy», sin plazo. La corrección no
cita nada nuevo.

**Corrección EN:**
- **02 B10:** `Check spatulas, presses and the probe thermometer: ice-point check (32 °F), recalibrate if it's off`
- **05 B20:** `Once a year, have the griddle thermostats and any built-in probes checked against a known standard; the probe thermometers get a daily ice-point check (32 °F) at the grill station — the core temp of ground beef depends on them`

D20 y E20 se quedan igual.

### m6 · 02 «Grill Station» B17 (L576): espátulas, prensa y pinzas de crudo solo se lavan al cierre

**Qué falla.** §4-602.11(C) pide limpiar cada 4 h, como mínimo, los utensilios en uso con comida TCS. La espátula y la
prensa tocan la picada cruda en cada pedido. El kit las lava y desinfecta solo a las 10:30 PM (02 B21). Es una cita
frecuente de los inspectores en hamburgueserías.

**Corrección EN:**
- **B17:** `Keep the griddle clean between batches (scraper); wash, rinse and sanitize spatulas, press and tongs at least every 4 h during service, or swap in clean ones (FDA 4-602.11)`
- **Añadir a `REGLAS_US`:** `('utensilios_4h', ('utensilios en uso con TCS: lavar, enjuagar y desinfectar cada 4 h como mínimo', 'FDA Food Code 2022 §4-602.11(C)'))`

G7 lo exige para la cita nueva.

### m7 · Falta la trampa de grasa (grease trap / interceptor)

**Dónde:** 05 «Quarterly & Annual» B14 (L1978) y la lista de 05 «Instructions» B6 (L1559).

**Qué falla.** Plancha y freidoras hacen del burger joint el generador de FOG por excelencia. El vaciado de la trampa,
con su manifiesto, es lo que pide la ordenanza municipal. El base EN lo trae («Grease trap pumped by a licensed hauler»),
y `REGLAS_US['grasas']` existe. Aquí no aparece, porque la fila ES no estaba.

**Corrección EN** (sin fila nueva):
- **B14:** `Review the waste and recycling hauler contract and local recycling rules (takeout and delivery multiply the cardboard and packaging), and keep the grease trap pumping manifests, as often as your local FOG rules require`
- **Instructions B6:** cambiar «…used-oil pickup, waste and containers, Legionella…» por «…used-oil pickup, waste, containers and grease trap, Legionella…».

### m8 · 05 «Quarterly & Annual» B13 / E13 (L1974 / L1976): retirada del aceite usado «Quarterly»

**Qué falla.** Con la frecuencia «Quarterly», la fila se lee como «el recycler pasa cada trimestre». En una
hamburguesería pasa cada pocas semanas, y lo que se hace por trimestre es revisar los recibos.

**Corrección EN (B13; E13 se queda en Quarterly):**
- `Used fryer oil: pickups by a licensed recycler as often as your volume needs; every quarter, check the receipts are on file and the outdoor container is closed and not leaking (with fryers running all day, it is one of the biggest waste streams in a burger joint)`

### m9 · 05 «Quarterly & Annual» E8 (L1959): la inspección semestral de la supresión, bajo «Annual»

**Qué falla.** B8 junta el mantenimiento anual del extintor con la supresión de la campana «every 6 months (NFPA 96)»,
pero la columna de frecuencia dice «Annual». En un local de plancha y freidora, el sistema de supresión es la revisión
de incendio que más importa. El base EN la tiene en su propia fila «Semiannual»; la pizzería quedó igual que aquí.

**Corrección EN:**
- **E8:** `Semiannual`
- **B8**, opcional y con la supresión delante: `Hood fire suppression inspected every 6 months (NFPA 96) and annual extinguisher maintenance by a licensed fire protection company: new tag and record (OSHA 1910.157)`

### m10 · «Take apart» la flat-top

**Dónde:**
- 05 «Weekly Deep Clean» B6 (L1727): `Take apart and deep-clean the flat-top griddle`, a cargo de Dishwasher / prep;
- 03 «Manager Monthly» B12 (L1028): `Deep-clean the griddle (take apart if possible)`, a cargo de Technician.

**Qué falla.** Una plancha flat-top no se desmonta. Es un calco de «desmontar plancha», que en el ES valía para la
parrilla de rejillas.

**Corrección EN:**
- **05 B6:** `Deep-clean the flat-top griddle: grease trough and drawer, splash guards, front and sides (griddle brick or screen + griddle cleaner), then re-season`
- **03 B12:** `Griddle: check the surface and thermostat with a surface thermometer, and deep-clean the grease trough`

### m11 · 04 «Grill Cook» E9 (L1208): bacon precocinado a las 10:45 AM

**Qué falla.** La plancha se enciende a las 11:00 AM (E6, L1193; 01 B15), y el horno de los panes también (01 B17).
«Precook bacon» a las 10:45 no tiene equipo encendido. El 01 B27, también a las 10:45, dice «precooked or ready for the
griddle» y vale.

**Corrección EN (E9):** `11:15 AM`

### m12 · BONUS-02 «Instructions» B8 (L3384): la nota UK sin el National Burger Day británico

**Qué falla.** El kit se vende «US con notas UK». En el Reino Unido, el National Burger Day es el **último jueves de
agosto**, el jueves antes del bank holiday; en 2026, el 27 de agosto. Es la fecha de marketing de cualquier hamburguesería
británica. La nota trae Mothering Sunday, los bank holidays y Boxing Day.

**Corrección EN:** `▸ Add the dates that matter in your area (local holidays, fairs). UK note: Mothering Sunday (March), National Burger Day (last Thursday in August), bank holidays and Boxing Day, in the free rows`

Conviene añadirlo a `REGLAS_US['dias_fuertes']` como `[criterio del kit]`.

---

## DUDAS (no demostradas; fuera de la ronda salvo que el orquestador decida)

- **D1 · Foie gras (06 «Burger Week» B7, L2132): «wagyu, truffle, foie gras where legal».**
  - La cita de `REGLAS_US`, Cal. Health & Safety Code §25982, es correcta: prohíbe vender productos de aves
    sobrealimentadas.
  - En Nueva York, la Local Law 202 (2019) sigue en litigio.
  - Con «where legal» la celda no es ilegal en ningún sitio, pero el foie gras en un burger joint independiente de
    EE. UU. es raro. Si se quiere quitar: `(wagyu, truffle, aged or specialty cheeses)`.
- **D2 · Mínimos del inventario (05 D6:D38).**
  - Son números (`openpyxl`: 25 int + 3 float), así que la errata ES de «mínimos como TEXTO» nace corregida en la EN.
    Las conversiones son exactas.
  - Las cifras raras delatan la conversión: 11 oz (300 g), 22 lb (10 kg) y 0,5 qt.
  - En EE. UU. se compran cajas de patatas de 30 lb, bolsas de blue cheese de 5 lb y medidas en pint.
  - Redondear (12 oz, 20 lb, «1 pt») sería más creíble. Los pickles a 1 lb van justos para unas 90 burgers al día, pero
    es un mínimo y no un consumo.
- **D3 · «cut tomato, lettuce and onion are TCS» (01 «Kitchen Closing» B7, L316).** La definición TCS del Food Code
  nombra la hoja verde, el tomate y el melón cortados. La cebolla cortada no está en la lista: depende de la valoración
  del producto y del regulador local. Es conservador y no daña. Si se quiere precisión: `cut tomato and lettuce are TCS
  (keep cut onion with them)`.
- **D4 · 06 «Game Night» E9 (L2073): «Add staff» 3 days out.** El calendario pone 2 semanas para la Super Bowl (D6,
  L3411). Las leyes de predictive scheduling (NYC, Chicago, Seattle, Oregon…) obligan a avisar con 14 días, pero solo
  alcanzan a las cadenas grandes, no al independiente. Para una noche de partido normal, 3 días valen.
- **D5 · Menores en la plantilla.** El trabajo infantil (FLSA) es el foco de inspección número uno del DOL en
  hamburgueserías:
  - de 14 a 15 años, solo freidoras con cestas automáticas (29 CFR 570.34);
  - de 16 a 17 años, ni cortadoras eléctricas ni compactadoras (HO 10 y HO 12).

  El kit asigna por rol y no afirma nada ilegal. Es idea para una v2.1, no un error.
- **D6 · Sonda en el centro de una smash de 3 oz (02 B14).** En un patty de ¼ in es poco práctico: las cadenas validan
  por tiempo y lo comprueban con la sonda al principio del turno. La regla es correcta y está bien escrita.

## Lo que intenté refutar y se sostiene

- **Carne picada:**
  - 155 °F 17 s; 145 °F 3 min, 150 °F 1 min y 158 °F al instante (3-401.11(A)(2));
  - pollo a 165 °F (A)(3);
  - poco hecha solo a petición y con aviso (3-603.11);
  - menú infantil sin picada poco hecha. Es **3-401.11(D)(2)**, confirmado: el (C) es el filete entero intacto. La SPEC y
    `REGLAS_US['poco_hecha']` lo citan bien; las celdas citan «3-401.11» en general, que es correcto.
- **El resto de la carne:**
  - cruda a 41 °F sin temperar (3-501.16), TPHC escrito con 4 h y descarte (3-501.19), descongelar en cámara (3-501.13);
  - manos y guantes de crudo a listo para consumir (2-301.14, 3-304.15);
  - herramientas de crudo separadas (3-302.11);
  - verdura lavada (3-302.15);
  - date marking de 7 días con día 1 = preparación (3-501.17).
- **Bacon y huevo:**
  - bacon enfriado 135 → 70 °F en 2 h y → 41 °F en 4 h más (3-501.14) y recalentado a 165 °F en 2 h (3-403.11);
  - yema líquida y mayonesa casera con aviso o con huevo pasteurizado.
- **°C del ES:**
  - las 10 celdas están convertidas o eliminadas: L79 → B15, L89 → B18, L105, L357, L525, L561, L711, L1839;
  - las 4 de `CELSIUS_SIN_F` sin °F: los 40 °C fuera en 01 «Kitchen Closing» B14 (L347) y 02 «Fry Station» B19
    (L763); en 01 «Kitchen Opening», la cifra del B14 va al B15 y la del B16 al B18.
- **Plancha y freidora:** 400–450 °F, 350–355 °F, TPM sin límite federal y, en el 08 B8, plancha y freidoras antes de
  la campana.
- **Orden del día:**
  - apertura del 01: campana → tiro → gas → plancha → freidoras → tostador → aceite (10:45 → 11:15), coherente con el
    08 B20 (11:00);
  - cierre del 01 y del 08: alarma, puertas y llave al final;
  - 03 B21: gas, luces, alarma;
  - control de salud con el Shift manager.
- **Alérgenos:** los 9 de EE. UU. con sésamo; el bun con trigo, leche, huevo, soja y sésamo; la mostaza fuera de los 9
  y dentro de los 14 del Reino Unido; la lactosa como intolerancia; cross-contact en plancha, línea y aceite compartido
  (L1508, L2189, L2194).
- **Alcohol:** solo en el calendario (C10 y C26) y en la liquor liability, con licencia, 21+ con ID, sin 2x1 y «free
  drinks only where your state allows them».
- **Calendario:**
  - Super Bowl el segundo domingo; Mardi Gras; Cuaresma de febrero a abril; St. Patrick's y March Madness;
  - National Burger Month en mayo, con el 28 de mayo como National Hamburger Day;
  - Mother's, Memorial, Father's y Labor Day bien;
  - 18 de septiembre: National Cheeseburger Day; Thanksgiving el cuarto jueves;
  - sin Reyes, uvas ni cava;
  - C18, C19, C20 y C26 con las lecciones de la pizzería;
  - el orden de mayo («May–June» antes de Mother's Day) es el mismo que en todos los hermanos.
- **NFPA, OSHA y otras normas:**
  - NFPA 96, tabla 11.4: trimestral si hay charbroil o alto volumen, semestral si es moderado;
  - OSHA 1910.157(e)(2) y (e)(3), y (f) con Class K y CO2 cada 5 años;
  - EPA 608; Consumer Confidence Report; FLSA 2 y 3 años (NY 6).
- **Restos de español:** ni €, ni °C, ni kg, g, L o ml, ni IVA, APPCC, TPV, horas de 24 h o tildes en las 3.512 líneas.
  Tampoco ningún término de `TERMINOS_PROHIBIDOS`, ni pizza, ni barista.
- **Técnica:**
  - la DV salta las filas de sección;
  - la CF es `$F5="✓"` (`$E5` en el 09) y C54 / H5:H35 ≠ 0;
  - los contadores cuentan las filas libres;
  - la Daily Inventory está sin proteger, como promete su B24;
  - las pestañas citadas existen («Kitchen Opening», «Quarterly & Annual», «Weekly FIFO Check» y «Cash Drawer
    Opening»);
  - el papel es Letter (=1).

---

## Ronda 1: aplicado / no aplicado (18-oct-2026 · sesión Claude Code)

Todo con la corrección EN del informe, en la fuente (`mapas_burger.py` y `textos_en/G1.json`). Construcción real en el
VPS: VERDE 8/0, autotest 18/18, censo 0, no-latinos 0, 0 desbordes; `dump_en.txt` regenerado (3.512 líneas).

| # | Estado | Cómo |
|---|---|---|
| M1 boil-out | APLICADO | c0262 (03 B13) y c0461 (05 B7) = «Fryer boil-out…» (D y E igual); `REGLAS_US['aceite']` + boil-out; errata ES en `SPEC.md` §5 |
| M2 queso americano | APLICADO | c0062 (01 B26) y c0380 (05 A15 «American / cheddar slices»; D15 sigue en 50) |
| m1 «15 days out» | APLICADO | `POR_CELDA` 06 E13 = «2 weeks out» (la celda es de glosario) |
| m2 freidora | APLICADO | c0116, c0117 = c0201, c0200, c0322, c0323 con el EN del informe; `_ACEITE` (ADAPTAR) a juego; `CELSIUS_SIN_F` intacto (sin temperatura) |
| m3 picada sobre el pollo | APLICADO | c0109 y c0305 («Store leftover beef labeled:» se mantiene); `_CARNE_GUARDAR` a juego |
| m4 make line con lectura | APLICADO | c0174 + « — log reading: ____ °F»; ADAPTAR a juego |
| m5 sonda | APLICADO | c0161 (02 B10) y c0496 (05 B20); D20 / E20 igual; 32 °F ya estaba en `GRADOS_F_SPEC` |
| m6 utensilios cada 4 h | APLICADO | c0168 (02 B17) + `REGLAS_US['utensilios_4h']` (§4-602.11(C)); G7 la admite |
| m7 trampa de grasa | APLICADO | sin fila nueva: `POR_CELDA` 05 B14 (contrato de residuos + manifiestos de la trampa, FOG) y c0355 (05 Instructions B6) |
| m8 aceite usado | APLICADO | `POR_CELDA` 05 B13 (E13 sigue en Quarterly) |
| m9 supresión semestral | APLICADO | `POR_CELDA` 05 E8 = «Semiannual» y B8 con la supresión delante |
| m10 «take apart» | APLICADO | c0408 (05 B6) y c0260 (03 B12) |
| m11 bacon a las 10:45 | APLICADO | `POR_CELDA` 04 E9 = «11:15 AM» |
| m12 nota UK | APLICADO | `POR_CELDA` B02 B8 (sale de `_HEREDA_ADAPTAR`) + `REGLAS_US['dias_fuertes']` con el National Burger Day UK |
| D2 mínimos | APLICADO (aprobada) | `VALORES_EN` al formato de compra US: bacon 5 lb, blue cheese y jalapeños 12 oz, patatas 20 lb, aros 5 lb, BBQ / mostaza / mayonesa 1 pt (C26:C28 = «pt», factor L → pt en `cruzar_censo`); siguen siendo números; criterio en `SPEC.md` (D-BUR Inventario) |
| D1, D3-D6 | NO APLICADO | decisión del orquestador: el foie gras se queda con «where legal»; lo que pide filas nuevas (menores en plantilla, etc.) va a la v2.1 |

Landing (`astro-site/src/data/productos-en/tareas/burger-joint-checklist-templates.ts`), 4 cambios triviales a juego:
picada «below ready-to-eat food and above any raw chicken»; freidora «filtered every night… changed when the TPM tester
says… monthly boil-out… quarterly sheet checks the used fryer oil pickups»; «flat-top griddle deep cleaned, grease trough
and splash guards included, and re-seasoned»; «a fryer boil-out» en vez de «a full fryer oil change».
