# Coffee Shop Checklists Kit Pro — revisión adversarial de F2 (entregables)

> Sesión Claude Code, 18-oct-2026. Revisor único, solo lectura.
>
> **Entradas:**
> - `cafe/revision/dump_en.txt` y `dump_es.txt`, leídos en paralelo (4.515 líneas, alineados línea a línea);
> - `cafe/SPEC.md`, `../SPEC.md`, `cafe/mapas_cafe.py`, `../mapas.py`, `cafe/textos_en/G1.json` y `heredado.json`
>   (para los ids);
> - `../revision/REVISION-F2.md` y `../bar/revision/REVISION-F2.md` (lo ya corregido no se repite);
> - una comprobación corta con openpyxl sobre `05-…xlsx`, `07`, `08` y `09`, con la CPU a 48 °C: los mínimos del
>   inventario son número (`int` / `float`), la tabla de congelación está desbloqueada y los formatos de la caja son
>   `#,##0.00`, sin €;
> - una búsqueda web sobre el date marking de los envases abiertos (FDA Food Code §3-501.17).
>
> **Notación.** «L» = línea de `dump_en.txt`, que es la misma línea en `dump_es.txt`; se cita la línea de la celda B
> (o de la celda indicada). «c0xxx» = id de `cafe/textos_en/G1.json` o de `heredado.json`.
> Las correcciones solo cambian textos (`G1.json`, `heredado.json`, `mapas_cafe.POR_CELDA`, `GLOSARIO`, `ADAPTAR`,
> `VALORES_EN` y `REGLAS_US`). No se añade ninguna fila ni cambia la estructura, así que G1 y G6 siguen en paridad.
> Las cifras nuevas son todas °F de `GRADOS_F_SPEC` (41, 135). Las citas nuevas (§3-501.17(B), §3-501.19) hay que
> darlas de alta en `REGLAS_US` antes de pasar G7; se indica en cada caso.

## Veredicto

**No hay nada BLOQUEANTE.** Las fórmulas, el semáforo del inventario, la caja, los °F, las 10 celdas con °C, las
alertas de alcohol, los alérgenos y el calendario están bien.

**No lo daría por listo para vender sin las 5 MAYORES.** Las cuatro primeras son de seguridad alimentaria: el
inspector de EE. UU. las mira en una coffee shop con brunch, y el manager las echaría en falta.

1. La leche abierta se rige por «la fecha de la etiqueta». Falta el tope de 7 días desde la apertura.
2. Ninguna tarea diaria mide el sanitizante con tiras.
3. El cold brew, que es la bebida número uno del verano, no tiene ninguna tarea de preparación.
4. La hollandaise y los huevos poco hechos no tienen ningún control.
5. **Sistémica:** quedan roles y zonas de restaurante en la salida, que entran por el glosario del base y se saltan
   `RX_CONTEXTO_PENDIENTE`: «Head chef», «FOH manager», «GM», «Host stand», «Cashier / MOD» y «DINING ROOM».

Los gates no ven ninguna de las cinco: el texto está en inglés, no lleva € y cita bien.

## MAYORES

### M1 · La leche abierta: «the date on the label rules» deja pasar leche con más de 7 días abierta

- **Dónde:**
  - 01 «Espresso Bar Closing» B20, L776 (c0207): `… covered and dated; the date on the label rules`;
  - 05 «Weekly FIFO Check» B11, L2649 (c0626): `the manufacturer's label date and the date you wrote when you opened
    it rule`.
- **Origen:** la regla `REGLAS_US['leche']` de `mapas_cafe.py`, que dice «manda la fecha de la etiqueta», y sus dos
  `ADAPTAR`.
- **Qué falla:** FDA Food Code 2022 §3-501.17(B).
  - Un alimento listo para consumir y TCS, envasado por un procesador, se marca al abrir el envase si se guarda más de
    24 h: 7 días como máximo a 41 °F, y **el día de apertura cuenta como día 1**.
  - La fecha que se marca **no puede pasar del use-by del fabricante**: manda la que llegue antes.
  - La leche líquida no está en las exenciones de §3-501.17(G), que son quesos duros, yogur y similares.
  - Con el texto actual, un galón con el sell-by a 14 días se usa 14 días después de abierto. «Opened milk not date
    marked» es una de las infracciones típicas en una coffee shop.
- **Corrección EN:**
  - c0207: `Put opened milk (and cold brew, if you serve it) in the cooler at 41 °F or below, covered and date-marked: 7
    days max counting the day it was opened, never past the use-by date on the label`.
  - c0626: `Check dates on opened milk: toss it at 7 days counting the day it was opened or at the label's use-by date,
    whichever comes first; keep it at 41 °F or below`.
  - `REGLAS_US['leche']` → `('leche y alternativas abiertas a 41 °F o menos; 7 días desde la apertura (día 1), sin
    pasar el use-by del fabricante', 'FDA Food Code 2022 §3-501.16 y §3-501.17(B)')`. Ajustar también los dos
    `ADAPTAR` (01 Cierre Barra Café B20 y 05 FIFO Semanal B11).

### M2 · Ninguna tarea diaria mide el sanitizante con tiras

- **Dónde:**
  - la única tira del kit es la de las tablas de corte, y es semanal: 05 «Weekly Deep Clean» B10, L2540;
  - las tareas diarias de desinfección no la llevan:
    - 01 «Kitchen Opening» B35, L172 (c0073 `Sanitize work surfaces`);
    - 01 «Kitchen Closing» B14, L512 (c0154 `Clean work surfaces and cutting boards`);
    - 01 «Espresso Bar Closing» B24, L792 (c0211 `Clean and sanitize the bar top`);
  - el friegue final tampoco: 04 «Busser & Runner» B17, L2143 (c0482 `Final dish area: wash all remaining dishes`).
- **Qué falla:**
  - FDA Food Code 2022 §4-302.14: tiene que haber un test kit que mida la concentración.
  - §4-501.114 y §4-501.116: la concentración se mide, no se pone a ojo.
  - Es lo mismo que M3 del base y M4 del bar, y aquí no se aplicó: el texto ES de la cafetería es otro, así que la
    memoria no lo heredó. La regla `REGLAS_US['sanitizante']` ya existe.
- **Corrección EN:**
  - c0073: `Sanitize work surfaces with an approved sanitizer at the label concentration: check it with a test strip`.
  - c0154: `Clean and sanitize work surfaces and cutting boards; check the sanitizer with a test strip (range on its
    label)`.
  - c0211, solo en el `heredado.json` de la cafetería: `Clean and sanitize the bar top; check the sanitizer with a test
    strip (range on its label)`.
  - c0482: `Final dish area: wash all remaining dishes and check the dish machine's sanitizer with a test strip (or the
    final-rinse temperature on its data plate)`.

### M3 · El cold brew no tiene ninguna tarea de preparación

- **Dónde:** solo aparece en 01 «Espresso Bar Closing» B20, L776, que trata de guardarlo, y en el calendario, L4449.
  No sale en la apertura del espresso bar (L414), ni en el cierre (L760), ni en la ficha del barista (04 «Barista»
  B11, L1812).
- **Qué falla:**
  - en una coffee shop de EE. UU., el cold brew se hace a diario: se filtra el lote, se pone la fecha, se guarda en
    frío y se arranca el de mañana;
  - es lo primero que busca el comprador en un «barista checklist»;
  - además, el cold brew hecho en casa y guardado más de 24 h lleva date marking (FDA Food Code §3-501.17(A)), y muchos
    departamentos de salud lo tratan como TCS.
- **Corrección EN** (textos de filas que ya existen):
  - c0133 (L414): `Brew the day's drip / batch brew; if you serve cold brew, filter the batch that finished steeping and
    store it covered at 41 °F or below, date-marked (7 days max counting the brew day)`.
  - c0203 (L760): `Empty and clean the drip coffee airpots; if you serve cold brew, start tomorrow's batch in a clean,
    covered container, steeped in the cooler unless your health department allows room-temperature steeping`.
  - 04 «Barista» B11 (L1812): `Brew the drip / batch brew (and filter the cold brew, if you serve it)`.
  - `REGLAS_US` + `('cold_brew', ('a 41 °F o menos, tapado y con fecha, 7 días; el reposo, donde lo permita el
    departamento de salud', 'FDA Food Code 2022 §3-501.16 y §3-501.17; [local] departamento de salud'))`.

### M4 · Hollandaise y huevos poco hechos sin ningún control (brunch)

- **Dónde:**
  - 01 «Kitchen Opening» B24, L125 (c0062): `Prep sauces: hollandaise, pesto, hummus`, a las 7:45 AM, para un servicio
    hasta las 3:00 PM;
  - 02 «Hot Line» B16, L911 (c0240): `Check egg doneness: poached, scrambled, fried`.
- **Qué falla:**
  - la hollandaise lleva yema poco cocinada y se mantiene templada: es el ejemplo de manual de Salmonella y de
    temperatura de riesgo en un brunch;
  - si no está a 135 °F o más (§3-501.16), solo puede estar 4 h sin control, con la hora marcada, y después se tira
    (time as a public health control, §3-501.19(B)). Montada a las 7:45 AM y usada hasta las 3:00 PM, pasa de ese
    límite;
  - el huevo poscocido o con la yema líquida es «raw or undercooked»: pide el aviso al consumidor en la carta
    (§3-603.11), salvo que se use huevo pasteurizado.
  - El kit afirma 135 °F (Kitchen Opening B16), pero no lo aplica donde más falta.
- **Corrección EN:**
  - c0062: `Prep sauces: hollandaise (use pasteurized eggs; hold it at 135 °F or above, or time-mark it and toss it after
    4 hours), pesto, hummus`.
  - c0240: `Check egg doneness: poached, scrambled, fried (runny yolks need the consumer advisory on the menu unless the
    eggs are pasteurized, FDA 3-603.11)`.
  - `REGLAS_US` + `('tphc', ('4 h sin control de temperatura con la hora marcada; después, a la basura', 'FDA Food Code
    2022 §3-501.19(B)'))`. `aviso_consumidor` ya está en el base.

### M5 · Roles y zonas de restaurante que entran por el glosario del base (sistémico)

- **Dónde:**
  - 07 «By Role»: D6:D10 `Head chef` (L3487), D13:D17 `FOH manager` (L3499) y D20:D24 `GM` (L3511). Son los únicos
    roles precargados de la plantilla, y ninguno existe en el resto del kit: el 04 se titula «Shift Lead, Barista,
    Baker, Server, Busser»;
  - 08 «Cafe Opening» C11 y C13, L3611 y L3621: `Host stand`. Una coffee shop no tiene puesto de host: son tareas de
    la tablet de pedidos y de las reservas del brunch;
  - 09 «Cash Drawer Opening» y «Cash Drawer Closing» C5:C16, L3820 y L3888: `Cashier / MOD` (23 celdas). MOD es jerga
    de restaurante; el kit ha elegido «Shift lead» (D8);
  - 09 «Monthly Cash Log» F2, L4021 (c0985): `General manager:`;
  - 01 «FOH Opening» A5 (L196, c0080) y «FOH Closing» A5 (L593, c0169): `DINING ROOM`.
- **Por qué pasa:**
  - `mapas.GLOSARIO` mapea Jefe de Cocina → Head chef, Jefe de Sala → FOH manager, Gerente → GM, Recepción → Host
    stand y Responsable de caja → Cashier / MOD (`mapas.py:156-171`);
  - `_GLOSARIO_CAFE` solo sobrescribe «Encargado»;
  - `RX_CONTEXTO_PENDIENTE`, que ya incluye `head chef`, `host stand`, `FOH managers` y `dining room`, solo se aplica a
    la memoria de traducción de `heredar.py`. No se aplica a las celdas del glosario ni al G1 del traductor;
  - **ningún gate pasa ese RX por la salida**.
- **Corrección EN:**
  - `_GLOSARIO_CAFE` + `('Jefe de Cocina', 'Kitchen lead')`, `('Jefe de Sala', 'Shift lead')`, `('Gerente',
    'Manager')`, `('Recepción', 'Front counter')` y `('Responsable de caja', 'Cashier / shift lead')`. En el ES de la
    cafetería cada uno solo aparece en estas celdas: 5, 5, 5, 2 y 23;
  - c0985: `Manager: _________________________`;
  - c0080: `  SEATING AREA`. c0169: `  SEATING AREA & FURNITURE`;
  - **Gate:** en `gates_en.py` (G2 o G4), pasar `RX_CONTEXTO_PENDIENTE` por todas las celdas EN, salvo la firma de autor
    («restaurant consultant»), cuando el kit lo define. Habría cazado las 6 de golpe y las cazará en el siguiente
    hermano.

## MENORES

- **m1 · Horas: la pastelera hornea antes de que se abra el local.**
  - Dónde:
    - 02 «Pastry Case» B6, L1081, y 04 «Baker» B6, L1905: `6:30 AM`;
    - 08 «Cafe Opening» B5 `Disarm the alarm`, L3580, y B8 `Raise security gate…`, L3595: `6:45 AM`;
    - 04 «Shift Lead» B6 `Open the shop and disarm the alarm`, L1694: `7:00 AM`.
  - Qué falla: tres horas distintas para el mismo hito, y la primera tarea del día va antes de la apertura. Viene del ES.
  - Corrección (`POR_CELDA`): 08 «Cafe Opening» E5:E8 → `6:30 AM`; 04 «Shift Lead» E6 → `6:30 AM`. Anotar en la
    `SPEC.md` §6 como errata del ES.
- **m2 · «Walk-in» por defecto y una sola lectura para dos equipos.**
  - Dónde: L94 (c0055), L543 (c0161) y L2643 (c0624).
  - Qué falla:
    - muchas coffee shops independientes trabajan solo con neveras de puerta (reach-in) o bajo mostrador, y el
      glosario mapea «Cámara» → «Walk-in»;
    - además, se piden cooler y freezer y solo hay un hueco: `log reading: ____ °F`.
  - Corrección:
    - c0055: `Check that the coolers (walk-in or reach-in) and the freezer ran all night and log the temperatures
      (cooler 41 °F or below, freezer 0 °F or below) — log reading: cooler ____ °F · freezer ____ °F. If out of range,
      don't use the product until it's been assessed`;
    - c0161: `Check that the coolers and freezer are closed and at temperature (cooler 41 °F or below, freezer 0 °F or
      below) — log reading: cooler ____ °F · freezer ____ °F`;
    - c0624: igual, con `Check the temperatures of all coolers and freezers (…)`.
- **m3 · Cierre de la vitrina incoherente entre libros.**
  - Dónde: 02 «Pastry Case» B23, L1154 (c0285 `Clear the case; store everything in the walk-in`) y 04 «Baker» B17,
    L1952 (c0452).
  - Qué falla: contradicen a 01 «Espresso Bar Closing» B18, L766, que dice que la bollería seca se guarda con la fecha
    del día y no en frío.
  - Corrección:
    - c0285: `Clear the case: TCS items (custards, cheesecake, dairy fillings) to the cooler at 41 °F or below; dry
      baked goods covered and dated`;
    - c0452: `Pull product from the case: TCS items to the cooler, dry baked goods covered and dated`.
- **m4 · Hielo: el cubo se vacía pero no se limpia, y la máquina de hielo no aparece en ninguna hoja.**
  - Dónde: L807 (c0214) y L2566 (c0608).
  - Qué falla: el moho en la máquina de hielo es una infracción habitual. El hielo es alimento (lo dice el propio kit,
    L404).
  - Corrección:
    - c0214: `Empty, clean and sanitize the ice bin`;
    - c0608: `Clean inside the bar fridge; check the ice machine bin and chute for mold or slime (full clean and
      sanitize per the manufacturer)`.
- **m5 · Campana: el auxiliar «desmonta» la campana cada semana.**
  - Dónde: 05 «Weekly Deep Clean» B7, L2525 (c0599 `Take apart and clean the exhaust hood`).
  - Qué falla: el personal saca y desengrasa los filtros. La campana, el conducto y las boquillas de extinción son del
    contratista (NFPA 96; lo dice la Quarterly B7, L2858).
  - Corrección: `Remove and degrease the hood filters (hood and duct cleaning is the contractor's job: see Quarterly &
    Annual)`.
- **m6 · El filtro de agua: «se limpia» cada mes y «se cambia» cada trimestre.**
  - Dónde: 05 «Monthly Maintenance» B9, L2770 (c0668 `Clean the water filter`), frente a la Quarterly B15, L2884.
  - Qué falla: el cartucho del filtro no se limpia, se sustituye.
  - Corrección: `Check the water filter: pressure/flow and capacity used (change it on the Quarterly & Annual schedule)`.
- **m7 · Jerga de espresso.**
  - L342 (c0117) `Check the machine pressure (9 bar)`: con la máquina parada, el manómetro de caldera marca 1-1,5 bar, y
    el barista creerá que algo falla. Corrección: `Check the brew pressure gauge during the test shot (about 9 bar)`.
  - L719 (c0194) `Clean the portafilters with hot water`: en EE. UU. el cierre es dejarlos en remojo con limpiador.
    Corrección: `Soak the portafilters and baskets in espresso machine cleaner (per its label), then rinse with hot
    water`.
- **m8 · Bebida de Navidad: «pumpkin spice» en diciembre.**
  - Dónde: 06 «Holiday Season» B15, L3198 (c0778).
  - Qué falla: en EE. UU., pumpkin spice es de otoño (de finales de agosto a noviembre; el propio calendario lo pone en
    «Fall drinks menu», L4463). Viene del ES.
  - Corrección: `Special holiday coffee: gingerbread latte, peppermint mocha, eggnog latte`.
- **m9 · «The week with no deliveries».**
  - Dónde: L3224 (c0784).
  - Qué falla: en EE. UU. los distribuidores solo paran el 25-dic y el 1-ene.
  - Corrección: `Check stock for the holiday weeks: confirm your suppliers' delivery days around Dec 25 and Jan 1`.
- **m10 · Ceniceros en el patio como práctica general.**
  - Dónde: L254 (c0096) y L636 (c0179).
  - Qué falla: muchos estados y ciudades prohíben fumar en terrazas de restauración.
  - Corrección:
    - c0096: `Check that ashtrays are clean (only if local law allows smoking on your patio)`;
    - c0179: `Collect and empty the ashtrays (if you have a smoking area)`.
- **m11 · «Tablecloths» en el cierre y «placemats/napkins» en la apertura.**
  - Dónde: L595 (c0170, heredado) frente a L203.
  - Corrección, solo en el heredado de la cafetería: `Break down tables: collect placemats/napkins, silverware, glasses`.
- **m12 · Unidades del inventario: las cifras están bien convertidas, el envase no.**
  - Lo que está bien, comprobado: 2 kg → 4 lb, 1 → 2, 0,5 → 1; 100 g → 4 oz, 300 → 10, 500 → 18, 250 → 8. Todos son
    número y el semáforo funciona.
  - Lo que chirría a un manager de EE. UU.:
    - la leche entera se compra por galones: L2226 (c0513) → `Whole milk (1 gal = 4 qt)`; L2384 (c0566) → `Whole milk
      (1 gal = 4 qt)`;
    - el bacon a 18 oz: L2313, D34 → `1` (`VALORES_EN` fila 34) y C34 → `lb` (`POR_CELDA`);
    - el café de mayorista se vende en bolsas de 5 lb: L2368 (c0560) → `House blend coffee (5 lb or 2 lb bags)`;
    - el sirope, en botella: L2259 y L2263 → `Vanilla syrup (bottles)` y `Caramel syrup (bottles)`, con C19:C20 → `ea`
      y D19:D20 → `1`. Es opcional.
  - Las plantas (oat, soy, almond) en qt están bien: el formato barista es la caja de 32 oz.
- **m13 · Alcohol servido por menores.**
  - Dónde: L3042 (c0739) y L3130.
  - Qué falla: las coffee shops emplean mucho a menores de 18, y casi todos los estados fijan una edad mínima para
    servir alcohol.
  - Corrección:
    - c0739: `Offer mimosas/bellinis as an add-on (only with an alcohol license; guests 21+ with ID, served only by
      staff old enough under your state's law)`;
    - L3130: añadir `, served by staff old enough under your state's law` antes del paréntesis.
  - Es una regla `[estatal]`, sin cita nueva.
- **m14 · 05 «Instructions» promete que las hojas con fórmulas van protegidas.**
  - Dónde: B23, L2189.
  - Qué falla: «Daily Inventory» y «Weekly Inventory» tienen fórmulas y no están protegidas. Viene del ES.
  - Corrección (`POR_CELDA` solo en 05, porque c0017 es común a los 11 libros): `▸ Checklist sheets with formulas are
    protected WITHOUT a password: the input cells (the green ones) are unlocked. The two inventory sheets are left
    unprotected so you can add products: don't type over the Status or Total value columns.`
- **m15 · 06 «Holiday Season»: `15 days out` (E6 y E8, L3164 y L3174) bajo `PREP (2 WEEKS OUT)`.**
  - Corrección: `2 weeks out`.

## DUDAS (no demostradas)

- **D1 · Descalcificar cada mes.** Las filas son 03 «Manager Monthly» B17, L1517, y 05 «Monthly Maintenance» B6,
  L2755, asignadas a «Tech / barista». En muchas máquinas comerciales de caldera no se descalcifica de forma rutinaria:
  se previene con el filtro, y si hay que hacerlo, lo hace el técnico. El «per the manufacturer's instructions» lo
  cubre, pero la frecuencia «Monthly» empuja a hacerlo. Si se quiere: `Descale only if and when the manufacturer
  calls for it (most commercial machines rely on the water filter; boiler descaling is a tech job)`.
- **D2 · Dial-in «25–30 ml (about 1 fl oz)»** (L337). Es una dosis sencilla. En EE. UU. se tira doble por defecto y
  se calibra por peso (p. ej., 18 g → 36 g). Lo decidió la SPEC; no está mal, pero un barista US lo notaría.
- **D3 · Tip pool** (L673). Según la FLSA, 29 U.S.C. 203(m)(2)(B), los managers y supervisores no pueden quedarse
  propinas del bote. El texto no dice quién participa, y la SPEC eligió «sin más afirmaciones legales». Se podría
  añadir `(owners and managers can't keep a share)`, con la regla en `REGLAS_US`.
- **D4 · Leche en dispensador.** Algunos estados (p. ej., Minnesota 4626.0400) aprueban un método alternativo al date
  marking para la leche en máquina dispensadora. No cambia M1: es una excepción que aprueba el regulador.
- **D5 · UK y PPDS (Natasha's Law).** Si una cafetería del Reino Unido envuelve en el local bollería o sándwiches para
  grab-and-go, necesita la lista completa de ingredientes. La SPEC lo dejó fuera a propósito y el kit no habla de
  envasado; anoto el riesgo para la FAQ de la landing.
- **D6 · «Expected covers»** (BONUS-01 B6). Es término de restaurante, aunque se entiende en un brunch con mesas.

## Lo que intenté refutar y se sostiene

- **Fórmulas y paridad:**
  - contadores `COUNTIFS` / `COUNTIF − N/A` en todas las hojas;
  - en el semáforo del inventario, D6:D44 son `int` / `float` (openpyxl): la errata del ES (mínimo en texto) está
    corregida y `B<D` funciona;
  - la caja: TOTAL COLLECTED, OVER / SHORT y la Z «sales + tax, excl. tips»;
  - rollos de 25¢ = $10 y de 10¢ = $5; el penny, sin acuñar pero de curso legal;
  - la media del fondo de caja y el sobrante o faltante acumulado en valor absoluto.
- **°F:** las 10 celdas con °C del ES están todas convertidas (L94, 445, 522, 543, 880, 1029, 1117, 2643, 2710 y
  2900). 41, 0, 135, 100, −4, −31 y 32 son correctas, y la del aceite sigue al fabricante, sin cifra.
- **Normas citadas:**
  - NFPA 96 tabla 11.4 y NFPA 17A cada 6 meses;
  - OSHA 1910.157(e)(2), (e)(3) y (f);
  - EPA 608;
  - FLSA: fichajes 2 años, nóminas 3, NY 6;
  - FDA 2-201.11, 3-301.11, 3-402.11 y 3-501.17 (7 días, día 1).
- **Calendario:**
  - King cake el 6-ene (Epiphany);
  - Teacher Appreciation Week, la primera semana completa de mayo (National PTA; en 2026, del 4 al 8);
  - Mother's Day el 2.º domingo de mayo y Father's Day el 3.º de junio;
  - Memorial Day el último lunes;
  - National Coffee Day el 29-sep;
  - Thanksgiving el 4.º jueves, con pumpkin y pecan pie;
  - gift cards del Black Friday a Nochebuena;
  - Nochevieja con el alcohol condicionado a la licencia y a 21+.
- **Alcohol:** todas las menciones (L3042, L3089, L3130 y L4493) van con licencia y 21+. Regalar alcohol, «según el
  estado».
- **Alérgenos:** los 9 de EE. UU., y 14 en UK, en vitrina, pastelería y bollería. Milk, soy y almond (tree nut), sin la
  avena. No hay mano desnuda (tongs / bakery tissue / gloves), y el hielo es alimento (L404).
- **Restos de español:** sin €, IVA, APPCC, TPV, «café» con tilde, horas de 24 h, Reyes, cava, turrón ni ml / kg
  sueltos (solo «25–30 ml» con fl oz). «Office» en el 04 B17 ya es «Final dish area»; en el 03 es la oficina, y así se
  queda.
- **Instrucciones contra el libro:**
  - la tabla de congelación del FIFO existe y está desbloqueada (B36:D43, `locked=False`);
  - las celdas verdes del 07 y el 08 son editables;
  - las citas a ficheros y pestañas apuntan a ficheros y pestañas que existen.

## Ronda 1: aplicado / no aplicado (18-oct-2026 · sesión Claude Code)

Construcción real en el VPS: idempotencia 0; G1-G8 VERDE 8/0 (G2 con términos prohibidos); autotest 18/18; censo 0;
no-latinos 0; base y bar idénticos a lo publicado. Ids: `G1.json` salvo que se diga otra cosa.

| # | Estado | Cómo |
|---|---|---|
| M1 leche abierta | APLICADO | c0207 y c0626 con el EN del informe; `ADAPTAR` 01 Cierre Barra Café B20 y 05 FIFO B11; `REGLAS_US['leche']` → §3-501.16 y §3-501.17(B) |
| M2 tiras de sanitizante | APLICADO | c0073, c0154, c0482 + c0211 (sale de la memoria con `NO_HEREDAR` y va a `G1.json`); `ADAPTAR` en las 3 filas de 01 |
| M3 cold brew | APLICADO | c0133, c0203 y c0426 (04 «Barista» B11); `ADAPTAR` y `REGLAS_US['cold_brew']` |
| M4 hollandaise y huevos | APLICADO | c0062 y c0240; `REGLAS_US['tphc']` (§3-501.19(B)); `aviso_consumidor` del base. El autotest G7 elige ahora una cita que el kit no permite (la cafetería ya permite 3-501.19) |
| M5 restos de restaurante | APLICADO | `_GLOSARIO_CAFE`: Kitchen lead, Shift lead, Manager, Front counter, Cashier / shift lead; c0985 (`NO_HEREDAR`), c0080 y c0169. **Gate nuevo**: `mapas.TERMINOS_PROHIBIDOS` (None en base y bar) → G2 lo pasa por toda pieza EN (3.557 en la cafetería, 0 fallos) y el autotest inyecta `TERMINO_PROHIBIDO_EJEMPLO` |
| m1 horas | APLICADO | `POR_CELDA` 08 «Cafe Opening» E5:E8 y 04 «Shift Lead» E6 → 6:30 AM; G4 acepta la hora fijada en `POR_CELDA`; errata en `SPEC.md` §6 |
| m2 walk-in y dos lecturas | APLICADO | c0055, c0161, c0624 |
| m3 cierre de la vitrina | APLICADO | c0285, c0452 |
| m4 hielo | APLICADO | c0214, c0608 |
| m5 campana | APLICADO | c0599 |
| m6 filtro de agua | APLICADO | c0668 |
| m7 jerga de espresso | APLICADO | c0117, c0194 |
| m8 pumpkin spice | APLICADO | c0778 |
| m9 semana sin entregas | APLICADO | c0784 |
| m10 ceniceros | APLICADO | c0096, c0179 |
| m11 manteles | APLICADO | c0170 (`NO_HEREDAR` → `G1.json`) |
| m12 unidades | APLICADO salvo lo opcional | c0513 y c0566 (galón), c0560 (5 lb / 2 lb), bacon `VALORES_EN` D34 = 1 y `POR_CELDA` C34 = lb. **No aplicado**: siropes en botellas (opcional en el informe) → v2.1 |
| m13 menores sirviendo alcohol | APLICADO | c0739 y c0762 («served by staff old enough under your state's law»); sin cita nueva |
| m14 promesa de protección | APLICADO | `POR_CELDA` 05 «Instructions» B23 (solo en el 05; c0017 sigue en los otros 10). La protección no se toca |
| m15 «15 days out» | APLICADO | `POR_CELDA` 06 «Holiday Season» E6 y E8 → 2 weeks out |
| D1-D6 | NO APLICADO | dudas no demostradas: fuera de la ronda por decisión del coordinador |
