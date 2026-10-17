# Bar Checklists Kit Pro — revisión adversarial de F2 (entregables)

> Sesión Claude Code, 18-oct-2026. Revisor único, solo lectura.
>
> **Entradas:**
> - `bar/revision/dump_en.txt` y `dump_es.txt`, leídos en paralelo (3.352 líneas, alineados línea a línea);
> - `bar/SPEC.md`, `../SPEC.md`, `bar/mapas_bar.py`, `../mapas.py` y `bar/textos_es.json` (para los ids);
> - `../revision/REVISION-F2.md` (lo corregido en el kit base no se repite);
> - una comprobación corta con openpyxl sobre `05-…xlsx`, con la CPU a 48 °C;
> - búsquedas web para verificar normas: 204 CMR 4.03, 26 U.S.C. 5301(c) y TTB, FDA Food Code 2022 §3-602.12(C) y
>   la vida de un barril con *party pump*.
>
> **Notación.** «L» = línea de `dump_en.txt`, que es la misma línea en `dump_es.txt`. «c0xxx» = id de `bar/textos_es.json`.
> Las correcciones solo cambian textos (`textos_en/G1.json` o `heredado.json`, `mapas_bar.POR_CELDA`, `CALENDARIO`,
> `ADAPTAR` y `GLOSARIO`). No se añade ninguna fila ni cambia la estructura, así que G1 y G6 siguen en paridad. Ninguna
> corrección mete un °F nuevo ni una cita fuera de `REGLAS_US`, así que G7 sigue igual.

## Veredicto

**No hay nada BLOQUEANTE.** Las fórmulas, la caja, los °F, las citas del delta y la paridad están bien.

Aun así, **no lo daría por listo para vender** sin las 6 MAYORES. Cuatro de ellas son del tipo que pide la lente 1:
- prácticas que son **ilegales en algunos estados y aparecen como práctica general**:
  - el «2-for-1»;
  - la «open bar» de Nochevieja;
  - guardar batches en una «capped bottle», es decir, rellenar botellas de licor;
- **el carding no aparece en los puestos que sirven.**

Las otras dos:
- **ninguna tira de sanitizante en el lavavajillas de vasos**;
- **la tabla de vida útil se titula «Freezer time».**

| Severidad | Nº |
|---|---|
| BLOQUEANTE | 0 |
| MAYOR | 6 |
| MENOR | 16 |
| DUDA | 6 |

---

## MAYORES

### M1 · BONUS-01: «2-for-1» como promoción de ejemplo

**Dónde:** «Pre-Shift Meeting» `B9` (L3134, c0745): `Active promotions (happy hour, 2-for-1, etc.)`.

**Qué falla.** Es el «2x1» del ES, traducido tal cual. En EE. UU. el 2-for-1 está prohibido en varios estados:
- Massachusetts, 204 CMR 4.03(1):
  - (b) prohíbe entregar más de dos bebidas a una persona a la vez;
  - (c) prohíbe vender por debajo del precio habitual de esa misma semana;
  - 4.03(2) prohíbe además anunciarlo.
- Illinois, 235 ILCS 5/6-28: prohíbe servir varias bebidas a la vez a una persona.

Es justo lo que el delta (D-BAR) quería evitar, y la plantilla lo leería en voz alta el equipo cada día. El resto del
kit sí remite al estado: L1939, L3325 y L3337.

**Corrección exacta (c0745):** `Active promotions (happy hour, drink of the day, food specials), only as your state allows: some ban 2-for-1s and drink discounts`

En `ADAPTAR` de esa celda: «sin 2x1 como ejemplo; promociones según el estado (REGLAS_US.happy_hour)».

### M2 · 06 «New Year's Eve»: «dinner + open bar» para una noche abierta al público

**Dónde:** «New Year's Eve» `B6` (L1866, c0503): `Define the concept for the night (party, dinner + open bar, ticket price)`.

**Qué falla.** La barra libre a precio fijo, es decir, «unlimited drinks for a fixed price», está prohibida en
Massachusetts (204 CMR 4.03(1)(d)) y en Illinois (235 ILCS 5/6-28), salvo en eventos privados no abiertos al
público. Una fiesta de Nochevieja con entrada no es un evento privado. B02 `D17` («open bar packages» para cenas
de empresa) **sí** se sostiene, porque son eventos privados.

**Corrección exacta (c0503):** `Define the concept for the night (party or dinner, ticket price and what it includes); open bars and all-you-can-drink packages are banned in some states (e.g. Massachusetts): check your state's ABC/liquor authority`

### M3 · 05 «Weekly Inventory»: la tabla de vida útil refrigerada se titula «Freezer time»

**Dónde:** «Weekly Inventory» `C36` (L1644, c0410, `mapa-glosario`).

**Qué falla.** Viene del glosario del base: `mapas.py:192`, `('Vida útil', 'Freezer time')`, que en el restaurante
encabezaba la tabla del congelador. En el bar, la columna dice «24 h refrigerated», «3–4 weeks refrigerated» o
«Keg date», y ningún producto va al congelador. Es la cabecera de la tabla que anuncia «Instructions» `B14` (L1347).

**Corrección exacta:** en `mapas_bar.py`, `GLOSARIO['Vida útil'] = 'Shelf life'`. En el bar solo aparece en esa celda.
El ancho de C es 12, así que cabe. El base no se toca.

### M4 · Ni tiras de sanitizante en el lavavajillas de vasos ni en la barra

**Dónde:**
- 04 «Barback» `B9` (L1222, c0313): «Wash glassware in the glass washer»;
- 01 «Bar Closing» `B15` (L262, c0100): «Sanitize the bar top»;
- también L287 y L1392.

**Qué falla.** En un bar, lo primero que mide un inspector de EE. UU. es la concentración del sanitizante del glass
washer, que es de baja temperatura y desinfecta con química. En los 11 libros no aparecen ni «sanitizer», ni
«strips», ni «ppm». La regla ya está en `REGLAS_US.sanitizante`, heredada del base (FDA Food Code 2022 §4-302.14 y
§4-501.114; ronda 1 del base, M3). La lente pedía expresamente «lavavajillas de vasos con tiras».

**Corrección exacta:**
- c0313: `Wash glassware in the glass washer; test the sanitizer with strips at the start of the shift (ppm on the label)`
- c0100: `Sanitize the bar top; test the sanitizer with strips (ppm on the label)`
- `ADAPTAR` de las dos celdas → `REGLAS_US.sanitizante`.

### M5 · Batches en una «capped bottle»: rellenar una botella de licor es ilegal a nivel federal

**Dónde:**
- 05 «Weekly Inventory» `D40` (L1657, c0423): `Spirits and fortified wines only: capped bottle, refrigerated, away from light`;
- relacionado: 02 «Cocktail Station» `B9` (L417, c0142), «Prep the day's infusions».

**Qué falla.** En una barra, «capped bottle» se lee como «la botella vacía de licor, tapada». Pero 26 U.S.C. 5301(c) y
27 CFR 31.201 prohíben al minorista meter en una botella de licor algo distinto de lo que tenía al cerrarse, y
alterar su contenido. La pena es una multa de hasta 1.000 $ o hasta 1 año de prisión. Desde 2012, la TTB no persigue
las infusiones para consumo en el local, pero **sigue persiguiendo el rellenado de botellas por parte de los
minoristas**. Hay que decirlo donde el kit habla de guardar batches e infusiones.

**Corrección exacta:**
- c0423: `Spirits and fortified wines only: sealed, labeled container (never back into an empty liquor bottle), refrigerated, away from light`
- c0142: `Prep the day's infusions (if applicable: infused gin, spiced vodka) in labeled jars, never in a liquor bottle`
- Opcional, como fuente del dato sin citarlo en el texto: en `REGLAS_US`,
  `('rellenado', ('no rellenar botellas de licor; batches e infusiones en recipientes propios etiquetados', '26 U.S.C. 5301(c); 27 CFR 31.201'))`
  y la misma fila en `bar/SPEC.md` §3.

### M6 · 04: en las fichas de quienes sirven no aparece ni el ID ni el corte de servicio

**Dónde:**
- 04 «Bartender» `B13` (L1139, c0298);
- 04 «Cocktail Server» `B7` (L1300, c0328).

**Qué falla.** El «21 + ID + no servir a visiblemente ebrios» solo aparece en 03 «Manager Daily» `B16` (L706) y en
las noches de evento (L1907, L1912 y B02). Las fichas «Bartender» y «Cocktail Server» son las que el libro 04
vende como *Bartender Checklist* («Perfect for onboarding new staff», L984), y no lo mencionan. En EE. UU. quien
sirve responde en persona: la ley penal de venta a menores, la dram shop y los cursos RBS y BASSET que el propio kit
cita (L805). No es una regresión del ES, que tampoco lo tiene, pero un bar manager de EE. UU. no entregaría esa
ficha a un nuevo sin esa línea.

**Corrección exacta:**
- c0298: `Make cocktails from the menu and special orders; card guests per house policy (21+) and never serve anyone visibly intoxicated`
- c0328: `Take orders with knowledge of the cocktail menu; card guests per house policy (21+) and stop serving anyone visibly intoxicated`
- `ADAPTAR` = el de 03 «Diario Manager» `B16`.

---

## MENORES

1. **B02 «Holiday Calendar», fila 21 (L3317-L3321; `CALENDARIO[21]`, F21 = c0837)**
   - Qué falla: el Super Bowl solo sale en una nota, sin fecha. El base lo tiene como fila propia (2.º domingo de
     febrero desde 2022) y en un bar de EE. UU. es de los 5 días más fuertes del año.
   - Corrección:
     - `B21` = `Feb (2nd Sun) · varies`;
     - `C21` = `Super Bowl Sunday & big games`;
     - c0837 = `Super Bowl on the 2nd Sunday in Feb; also March Madness, NBA/NHL playoffs, World Series`.

2. **B02, filas 9 y 10 (L3245-L3255)**
   - Qué falla: «Late May · Memorial Day weekend» va antes que «May 5 · Cinco de Mayo». La fila 9 era el 1 de mayo
     del ES, así que se rompe el orden por meses.
   - Corrección: intercambiar las filas 9 y 10 en `CALENDARIO`, con D y F por `POR_CELDA` (E es «2 weeks» en las dos):
     - fila 9 = `May 5` · `Cinco de Mayo` · D `Margaritas, mezcal, tequila, Mexican decorations` · F `Already one of the biggest bar nights of the year in the US`;
     - fila 10 = `Late May` · `Memorial Day weekend (last Mon of May)` · D `Holiday hours, patio at full capacity and stock for several days in a row` · F `A long weekend moves more than a normal Saturday and is ordered with the same lead time`.

3. **B02 `F18` (L3303, c0827)**
   - Qué falla: «The after-dinner drink with the family is a short, very profitable peak» es la copa de después de
     la cena de Nochebuena española. Además contradice a `D18` («many bars close early on Christmas Eve»).
   - Corrección: `Usually a short night: staff lean and post the hours early`.

4. **05 «Weekly Inventory» `D44` (L1669, c0435) y `bar/SPEC.md` §6**
   - Qué falla: «the old "3–5 days" rule only applies to air pumps (party pumps)» es falso. Una party pump mete aire
     y el barril hay que acabarlo en el día: las fuentes del sector dan entre 8 y 24 h.
   - Corrección: `Keg date rules (Brewers Association: 45–60 days unpasteurized, 90–120 days pasteurized, from packaging) with a balanced CO₂ system and lines cleaned every 2 weeks; on an air pump (party pump), finish the keg the same day`.
   - En SPEC §6, errata ES: «los 3-5 días no valen ni con bomba de aire (se acaba en el día)».

5. **05 «Weekly Inventory» `D39` (L1654, c0420)**
   - Qué falla: «orgeat… must be declared on the menu» es la norma UE (Reglamento 1169/2011). En EE. UU., donde se
     ha adoptado el FDA Food Code 2022, §3-602.12(C) exige un aviso **por escrito**, y el formato es libre: carta,
     tarjeta, cartel o table tent.
   - Corrección: `Label with the prep date; orgeat contains ALMOND (tree nut): list it on the menu or your written allergen sheet`.

6. **02 «Cocktail Station» `B11` (L427, c0144)**
   - Qué falla: «flips MILK». Un flip lleva huevo entero (y a veces nata). Si un camarero solo lee «milk», puede
     decir «no lleva huevo». El error viene del ES («flips LÁCTEOS»).
   - Corrección: `…orgeat has ALMOND (tree nuts), sours EGG WHITE, flips WHOLE EGG and often cream (MILK); sulfites in wine and vermouth…`.
     El resto de la cadena se queda igual.
   - Para la errata del ES: «flips HUEVO y a menudo nata».

7. **02 «Wine & Cellar» `B6` (L563, c0172)**
   - Qué falla: «whites and roses» se lee como «rosas».
   - Corrección: `Check open wines by the glass (whites and rosés in the cooler at 46–50 °F)`. Hay que comprobar que G2
     no tome «rosés» por español.

8. **02 «Wine & Cellar» `E4` (L558, c0170 = «Cadencia», 2 apariciones)**
   - Qué falla: la cabecera dice «Frequency», pero `E6`-`E13` son horas («4:00 PM»). Viene del ES.
   - Corrección: solo en esta celda, por `POR_CELDA`, `When`. La de 05 «Quarterly & Annual» se queda en «Frequency».

9. **02 «Draft Beer Station» `B7` (L495, c0157)**
   - Qué falla: «pour off the first third» es un calco de «tirar el primer tercio»: no dice el tercio de qué.
   - Corrección: `Flush the taps: pour off the first few ounces from each faucet until the beer runs clear and cold`.

10. **06 «New Year's Eve» `B16` (L1907, c0517)**
    - Qué falla: el brindis de medianoche, si es gratis, es un *free drink*, prohibido en Massachusetts por 204 CMR
      4.03(1)(a). El kit ya aplica ese criterio en el World Cocktail Day (L3325).
    - Corrección: `Midnight toast for guests 21+ only (check ID), with a non-alcoholic option; build it into the ticket price where your state bans free drinks`.

11. **06 «Pairings & Tastings» `B7` (L2007, c0536)**
    - Qué falla: «a bottle to take home» supone vender una botella cerrada para llevar, y no todas las licencias
      on-premise lo permiten (off-sale).
    - Corrección: `Settle in writing the price per person and what it includes: number of pours, food pairing, farewell drink and any bottle to take home (check your license: not every on-premise license allows sealed bottles to go)`.

12. **01 «Bar Closing» `B24` (L298, c0109)**
    - Qué falla: el bar vive de tabs, y ninguna lista de cierre dice «cerrar todas las cuentas abiertas antes de la
      Z». Una tab abierta descuadra el OVER / SHORT.
    - Corrección: `Close out every open tab (no open checks before the Z report) and check that the day's cash count is closed and signed: it is not repeated here, it is done on "Cash Drawer Closing" in 09-cash-drawer-opening-closing.xlsx`.
      La cita de rótulo y la de fichero se quedan literales.

13. **05 «Quarterly & Annual» `B14` (L1718, c0461)**
    - Qué falla: la limpieza y desinfección de la máquina de hielo (cubeta y evaporador, moho) es un clásico de
      inspección en bares, y no aparece. Solo se cambia el filtro.
    - Corrección: `Ice machine: clean and sanitize the bin and evaporator per the manufacturer (check for mold and slime); replace its water filter and the espresso machine's, and test water hardness to set the descaling frequency`.
      `D14` y `E14` se quedan.

14. **08 «Venue Closing», filas 16-19 (L2489-L2507; c0632, c0633, c0635 y c0636)**
    - Qué falla: el orden es «Set the alarm» → «Lock up» → «Clean the beer faucets» → «Empty and clean the garnish
      station»: se limpia después de cerrar con llave. Viene del ES.
    - Corrección: intercambiar B, C y D de 16-17 con 18-19 por `POR_CELDA`. E es «Close» en las cuatro.
      - 16: `Clean the beer faucets` · `Bar` · `Last one out`
      - 17: `Empty and clean the garnish station` · `Bar` · `Last one out`
      - 18: `Set the alarm` · `Entrance` · `Shift manager`
      - 19: `Lock up and verify it is locked` · `Entrance` · `Last one out`
    - G4 tiene que aceptar `POR_CELDA` sobre celdas `mapa-glosario`.
    - Errata para el ES v2.x.

15. **08 «Venue Opening» `B8` (c0598, el ADAPTAR heredado del base)**
    - Qué falla: el kit insiste en el aforo del fire marshal (L706, L1912 y L3349), pero no pide comprobar las
      salidas de emergencia. Es lo segundo que mira el fire marshal en un bar.
    - Corrección: `Raise security gate and open front door; check every emergency exit is unlocked and clear and the exit signs are lit`.
      Sin cita, para no salir de G7.

16. **Referencias FDA: ninguna en los 11 libros. Cambio opcional, pero aporta.**
    - Qué falla: G7 solo ve OSHA 1910.157, NFPA 96 y EPA 608, más Brewers Association y FLSA. Las dos reglas de
      alimentos del delta (el hielo es alimento y sin mano desnuda) están en `REGLAS_US`, pero los textos no las
      citan. Al bar manager le sirve tener la cita para formar al equipo y ante el inspector.
    - Corrección:
      - c0046: `…no bare-hand contact with ice, citrus or garnish (FDA Food Code 3-301.11): use tongs, picks, a scoop or gloves`;
      - c0150: `…Ice is food (FDA Food Code): keep the scoop out of the ice or with the handle out`.
    - El formato es el mismo que pasa G7 en el base («FDA Food Code 3-402.11»).
    - Las demás referencias que esperaría un comprador ya están en el texto sin número de norma: TIPS / ServSafe,
      ASCAP / BMI / SESAC / GMR, liquor liability, ABC. Añadir más no aporta.

---

## DUDAS (no demostradas)

- **D1 · B02 fila 11 (L3257-L3261).** «Jun 20–21 · First day of summer» con «Open patio season» choca con el Memorial
  Day, que ya pone el patio «at full capacity». Fue una decisión aprobada en F2 y en EE. UU. el solsticio no es noche
  de bar. Alternativa: Pride (junio), si John lo quiere.
- **D2 · 06 «Happy Hour» `B6`.** El ejemplo «6:00–8:00 PM» viene del ES; en EE. UU. lo típico es 4–7 PM. No es un
  error, es un valor editable.
- **D3 · 01 «Bar Opening» `B7`.** «no polish or acrylics» es más estricto que FDA §2-302.11, que lo permite con
  guante. Vale como norma de la casa.
- **D4 · 03 «Manager Monthly» `A2`.** Lleva cabecera de turno («Shift: ☐ AM ☐ Mid ☐ PM») en una lista mensual,
  igual que el ES y el base. Lo lógico sería «Month / Year».
- **D5 · Extintores.** Falta la inspección visual mensual (OSHA 1910.157(e)(2)), que el base sí tiene. El ES del bar
  no tiene fila para eso, así que queda para la v2.1.
- **D6 · Infusiones.** La TTB las tolera desde 2012 para consumo en el local, pero no he encontrado un documento
  vigente que lo confirme, y algún estado puede regularlas. Por eso M5 solo pide «labeled jars, never in a liquor
  bottle».

---

## Lo que intenté refutar y se sostiene

- **Citas del delta (SPEC §3), comprobadas una a una:**
  - 23 U.S.C. 158 (edad de 21);
  - California AB 1221 (RBS obligatorio desde el 1-jul-2022);
  - Illinois BASSET;
  - Massachusetts 204 CMR 4.03: free drinks (a), más de dos bebidas (b), precio por debajo del de la semana (c),
    barra libre a precio fijo (d) y la excepción de eventos privados;
  - 17 U.S.C. 106(4);
  - Licensing Act 2003 y la TEN para abrir más allá del horario de la premises licence.
- **Draft (Brewers Association, *Draught Beer Quality Manual*):**
  - 38 °F;
  - líneas cada 2 semanas y ácido cada 3 meses (L921, L1481 y L1710);
  - frescura de 45–60 días sin pasteurizar y de 90–120 pasteurizada;
  - PSI del técnico, sin los «2,5–3 bar» del ES;
  - Venue Opening `B20` («CO₂ pressure») está bien.
- **Las 7 celdas con °C:**
  - 2–4 y 0–4 °C → «41 °F or below»;
  - 3–5 °C → 38 °F;
  - 8–10 °C → 46–50 °F;
  - 16–18 °C → 61–64 °F;
  - 12–16 °C → 54–61 °F (bien redondeado);
  - no queda ningún «°C» suelto.
- **Hielo y manos:**
  - pala o pinzas, nunca el vaso (y quemar el ice well si se rompe uno);
  - la pala con el mango fuera;
  - sin mano desnuda en hielo, cítricos ni garnish;
  - lavamanos a 100 °F;
  - el hielo seco solo como decoración (L3277).
- **Alcohol:**
  - last call «check your state's ABC/liquor authority» (L226);
  - el happy hour remite al estado en las 3 apariciones;
  - World Cocktail Day sin cóctel gratis;
  - ID 21+ en St. Patrick's, Spring break, Thanksgiving Eve y NYE;
  - Challenge 25 en 03 `B16`;
  - TIPS / ServSafe «where your state requires it»;
  - liquor liability en los seguros;
  - ASCAP, BMI, SESAC y GMR;
  - aforo del fire marshal.
- **Festivos:**
  - Mardi Gras Feb–Mar;
  - Memorial Day el último lunes;
  - Beaujolais Nouveau el 3.er jueves de noviembre;
  - Thanksgiving Eve, el miércoles anterior;
  - NYE con «ticketed entry with a drink included» (es venta, no regalo);
  - en ninguna parte quedan cava, uvas ni Nochebuena.
- **Técnica:**
  - nada de español, €, IVA, APPCC, TPV ni horas de 24 h (grep sobre el dump);
  - las citas entre comillas de pestañas y rótulos existen tal cual;
  - las 11 citas de fichero llevan el nombre EN;
  - 29 DV y 30 CF iguales que en el base;
  - la caja hereda la ronda 1 (Z sin propinas);
  - la tabla de vida útil es editable de verdad: `B37:D46` desbloqueadas y en verde (openpyxl), como promete «Instructions» `B14`.

Fuentes web:
- 204 CMR 4.03 (LII Cornell);
- 26 U.S.C. 5301 (openjurist), 27 CFR 31.201 y la postura de la TTB de 2012 sobre infusiones (Libation Law Blog);
- FDA Food Code 2022 §3-602.12(C) (Perkins Coie y Georgia DPH);
- vida del barril con party pump (KegWorks y Micro Matic).

---

## Ronda 1: aplicado / no aplicado (18-oct-2026 · sesión Claude Code)

Solo texto: `textos_en/G1.json`, `mapas_bar.py` (`GLOSARIO`, `CALENDARIO`, `POR_CELDA`, `ADAPTAR`, `REGLAS_US`,
`NO_HEREDAR`) y `heredar.py` (admite `NO_HEREDAR`). Sin filas nuevas ni cambios de estructura: G1/G6 en paridad.

| Hallazgo | Estado | Cómo |
|---|---|---|
| M1 2-for-1 | APLICADO | c0745 con el EN del informe + ADAPTAR B01 `B9` |
| M2 open bar NYE | APLICADO | c0503 + ADAPTAR 06 `B6` (barra libre solo en eventos privados); B02 `D17` se queda |
| M3 «Freezer time» | APLICADO | `GLOSARIO['Vida útil'] = 'Shelf life'` en `mapas_bar.py`. **El base está bien**: su «Vida útil» (05 «FIFO Semanal» `C38`) encabeza la tabla «EN CONGELACIÓN A −18 °C», así que «Freezer time» es correcto y no hace falta una 2.0.1 |
| M4 tiras de sanitizante | APLICADO | c0313 y c0100 + ADAPTAR (`REGLAS_US.sanitizante`) |
| M5 rellenar botellas | APLICADO | c0423 y c0142 + ADAPTAR + `REGLAS_US.rellenado` (26 U.S.C. 5301(c); 27 CFR 31.201) y fila en `bar/SPEC.md` §3 |
| M6 ID y ebrios en 04 | APLICADO | c0298 y c0328 + ADAPTAR = el de 03 «Manager Daily» `B16` |
| m1 Super Bowl | APLICADO | `CALENDARIO[21]`: B «Feb (2nd Sun) · varies», C «Super Bowl Sunday & big games»; c0837 |
| m2 orden Cinco / Memorial | APLICADO | filas 9 y 10 intercambiadas; D y F por `POR_CELDA` (`_CAL_DF`) |
| m3 Christmas Eve | APLICADO | c0827 |
| m4 party pump | APLICADO | c0435 + errata en `bar/SPEC.md` §6 + `REGLAS_US.party_pump` |
| m5 aviso escrito FDA | APLICADO | c0420 + `REGLAS_US.aviso_alergenos` (§3-602.12(C)) |
| m6 flip con huevo | APLICADO | c0144 + errata ES en §6 |
| m7 «rosés» | APLICADO | «white and rosé wines» (sin tocar la lista blanca compartida de G2) |
| m8 «Frequency» con horas | APLICADO | `POR_CELDA` 02 «Wine & Cellar» `E4` = «When» (es un rótulo: ni DV ni CF); la del 05 se queda |
| m9 «first third» | APLICADO | c0157 |
| m10 brindis gratis | APLICADO | c0517 |
| m11 botella para llevar | APLICADO | c0536 |
| m12 tabs antes de la Z | APLICADO | c0109 (cita de rótulo y de fichero literales) |
| m13 máquina de hielo | APLICADO | c0461 (misma fila, D14/E14 iguales) |
| m14 orden del 08 | APLICADO | `POR_CELDA` B/C/D de 08 «Venue Closing» 16-19 (limpiar antes de alarma y llave) + errata en §6 |
| m15 salidas de emergencia | APLICADO | c0598 sale de lo heredado (`NO_HEREDAR`) y va a G1 con el EN del informe |
| m16 citas FDA | APLICADO | c0046 «(FDA Food Code 3-301.11)» y c0150 «Ice is food (FDA Food Code)» |
| D1-D6 | NO | dudas: fuera de la ronda por decisión del orquestador; D5 (inspección mensual de extintores) pide fila → v2.1 |

Resultado: montaje real con idempotencia 0 · gates **VERDE 8/0** · autotest 16/16 · censo 0 defectos · no-latinos 0 ·
el base sale idéntico (0 diferencias, gates idénticos) · sha256 11/11 en el Mac · `dump_en.txt` regenerado.
