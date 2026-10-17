# Restaurant Checklists Kit Pro — revisión adversarial de F2 (entregables)

> Sesión Claude Code, 17-oct-2026. Revisor único y solo lectura. Entradas: `revision/dump_en.txt` y `dump_es.txt`
> leídos en paralelo (4.227 líneas, alineados línea a línea), `SPEC.md`, `mapas.py`, `F1-inventario-es.md`,
> `F2-NOTAS.md`, `textos_en/G1.json` y `G2.json`. Además, comprobaciones cortas con openpyxl sobre los 11 xlsx EN
> (anchos, merges, bloqueo, relleno de CF, XML crudo y docProps), con la CPU a menos de 52 °C.
> «L» = línea de `dump_en.txt` (es la misma línea en `dump_es.txt`). «c0xxx» = id de `textos_en`.

## Veredicto

**No hay nada BLOQUEANTE**: ninguna fórmula rota, ninguna cifra FDA, OSHA o NFPA falsa, ningún resto de español y
ninguna cita a una pestaña o fichero que no exista. Aun así, **no lo daría por listo para vender** sin las 4 MAYORES.
Las cuatro se arreglan cambiando textos (`textos_en` o `mapas.POR_CELDA`) y relanzando `aplicar_en.py` y los gates;
la estructura no se toca. Sin ellas, un kitchen manager de EE. UU. vería cuatro cosas:
- el cuadre de caja en ámbar todos los días;
- la nómina en la lista mensual;
- un turno «Overnight» en 17 cabeceras;
- un kit que presume de FDA Food Code y no trae ni enfriamiento ni recalentado.

| Severidad | Nº |
|---|---|
| BLOQUEANTE | 0 |
| MAYOR | 4 |
| MENOR | 16 |
| DUDA | 6 |

---

## MAYORES

### M1 · 09: la cifra de la «Z» no está definida para EE. UU. (impuesto y propinas), así que el OVER / SHORT sale ámbar a diario

**Dónde:**
- 09 «Cash Drawer Closing» `A53` (L3718).
- «Monthly Cash Log» `G4` (L3740).
- «Instructions» `B15` (L3489) y `B17` (L3491).
- «Monthly Cash Log» `A37` (L4032).

**Qué falla.** En España el precio lleva el IVA dentro y no hay propinas en tarjeta, así que «Z del TPV» no tiene
ambigüedad. En EE. UU. el cierre del POS separa net sales, sales tax, tips y un «total», y en muchos POS ese total
**incluye las propinas** (en Square, por ejemplo, «Total collected»; casualmente es el mismo rótulo que nuestro
`A52`). El TOTAL COLLECTED del kit sí incluye el impuesto, porque el efectivo y la tarjeta lo llevan dentro, pero
**excluye** las propinas (D12: C50 sin propinas y C51 las devuelve). Así que:
- quien teclee **net sales** queda «short» por todo el sales tax del día;
- quien teclee el **total del POS** queda «short» por todas las propinas de tarjeta.

En los dos casos la celda C54 / H5:H35 se pone ámbar todos los días, y B17 dice «the drawer doesn't balance». La
lógica de D12 es correcta; lo que falta es decir qué número de la Z se escribe.

**Corrección exacta:**
- `mapas.POR_CELDA` («Cierre de Caja», `A53`): `POS Z report: sales + tax, excl. tips`. A53:B53 está combinada y
  mide 60, así que cabe.
- `mapas.POR_CELDA` («Registro Mensual», `G4`): `POS Z (+ tax, no tips)`. Ancho 14 con ajuste y alto 36: cabe en
  2 líneas.
- 09 «Instructions» `B15` (ADAPTAR): `▸ In the "Closing Summary" you only type three figures: "Card sales, excl. tips", "Other tenders + card tips paid in cash" and "POS Z report: sales + tax, excl. tips" (net sales plus sales tax, without tips or gratuities; many POS "total" lines include tips). Everything else is a formula.`
- 09 «Instructions» `B17`: `▸ OVER / SHORT = TOTAL COLLECTED − POS Z report (sales + tax, excl. tips). If the cell turns AMBER, the drawer doesn't balance: check it BEFORE signing.`
- 09 «Monthly Cash Log» `A37`: añadir al final `"POS Z" = net sales + sales tax, without tips.`
- G4 compara las citas de rótulos: B15 tiene que citar el A53 nuevo literal.

### M2 · 03: «Process payroll» va en la lista MENSUAL y con frecuencia «Monthly»

**Dónde:** 03 «Manager Monthly» `B18` (L1535, c0406) y `E18` = «Monthly».

**Qué falla.** En España la nómina es mensual; en EE. UU., para el personal por horas, pagar una vez al mes es
**ilegal en la mayoría de los estados**:
- CA Labor Code §204: dos veces al mes;
- NY Labor Law §191: semanal para los *manual workers* (cocineros, friegaplatos);
- TX Labor Code §61.011: dos veces al mes para los non-exempt.

La FLSA, además, exige pagar las horas extra en el payday ordinario. Leído en una lista mensual, «Process payroll»
se entiende como nómina mensual. ADAPTAR tradujo la tarea, pero no cambió su cadencia.

**Corrección exacta (c0406):** `Reconcile the month's payroll runs (weekly or biweekly, per your state's pay-frequency law): tips, overtime, bonuses`. `E18` se queda en «Monthly», porque la conciliación sí es mensual.

### M3 · El kit vende «°F y FDA Food Code», pero le faltan los controles TCS que más mira un inspector de EE. UU.

**Dónde:**
- 02 «Hot Line» `B23` (L855, c0248) y `B20` (L849, c0246);
- 01 «Kitchen Closing» `B15` (L484, c0164);
- 01 «Kitchen Opening» `B44` (L197, c0091).

**Qué falla.** En los 11 libros no aparecen:
- el **enfriamiento en dos fases**: 135 → 70 °F en 2 h y 70 → 41 °F en otras 4 h (FDA Food Code 2022 §3-501.14);
- el **recalentado para mantener en caliente**: 165 °F durante 15 s, en 2 h como máximo (§3-403.11(A));
- la **concentración del sanitizante** medida con tiras: §4-302.14, test kit, y §4-501.114, ppm según etiqueta.

El ES no los tiene, así que no es una regresión de la traducción. Pero la SPEC §3, que es la «fuente única», tampoco,
y G7 los impediría hoy (70 y 165 no están en el conjunto de °F). Las tareas de sobras («Store leftover proteins:
label and date») y de limpieza («Clean and sanitize») son justo donde un GM o un inspector de EE. UU. espera verlos.

**Corrección exacta.** Se reescriben filas existentes; ninguna fila nueva, así que G1 y G6 siguen en paridad:
- c0248 (02 «Hot Line» `B23`): `Cool leftover proteins fast (135 → 70 °F within 2 h, then to 41 °F within 4 more h, FDA Food Code 3-501.14), then label and date`
- c0246 (02 «Hot Line» `B20`): `Hot-holding check (135 °F or above; leftovers reheated to 165 °F within 2 h first, FDA Food Code 3-403.11) — log reading: ____ °F`
- c0164 (01 «Kitchen Closing» `B15`): `Clean and sanitize work surfaces; test the sanitizer with test strips (ppm on the label)`
- c0091 (01 «Kitchen Opening» `B44`): `Set up sanitizer buckets for wiping cloths and test them with strips (ppm on the label)`
- `mapas.REGLAS_US` y SPEC §3: añadir `enfriamiento` (135→70 °F 2 h; 70→41 °F 4 h; §3-501.14),
  `recalentado` (165 °F 15 s en ≤ 2 h; §3-403.11) y `sanitizante` (test kit §4-302.14; §4-501.114).
- G7: añadir 70 y 165 al conjunto de °F.

### M4 · «Shift: ☐ AM ☐ PM ☐ Overnight» en 17 cabeceras

**Dónde:** c0040, 17 apariciones; `A2` en L42, 219, 334, 438, 588, 663, 778, 907, 1016, 1171, 1594, 1709, 1808,
1887, 1981, 2085 y 3099.

**Qué falla.** «Mañana / Tarde / Noche» son los turnos de comida y de cena de un restaurante español; «Noche» es la
cena, no un turno de madrugada. «Overnight» es el *graveyard shift* de un diner 24 h y no existe en un casual
restaurant. Es lo primero que se lee en cada hoja. Además choca con BONUS-01 `B2` (L4060: «☐ Lunch ☐ Dinner»). No
está declarado en la SPEC.

**Corrección exacta (c0040):** `Date: ___/___/______    Shift: ☐ AM  ☐ Mid  ☐ PM    Shift manager: _________________________`
(AM / Mid / PM es el reparto de turnos habitual en EE. UU.; «Tarde» = Mid.)

---

## MENORES

1. **B02 «Holiday Calendar» `B6` (L4124, `mapas.CALENDARIO[6]`)**
   - Qué falla: «Super Bowl Sunday (early Feb)» no es exacto. Desde la temporada de 17 partidos (2022), la Super Bowl
     se juega el **2.º domingo de febrero**: 8-feb-2026 y **14-feb-2027, el mismo día que San Valentín**, que es la
     siguiente después de la compra.
   - Corrección: `Super Bowl Sunday (2nd Sunday in Feb)`.
   - Opcional: en C6, añadir `; in 2027 it falls on Feb 14 (Valentine's)`.
2. **B02 `B19` (L4176, `CALENDARIO[19]`)**
   - Qué falla: Memorial Day y Thanksgiving llevan su regla; Labor Day no.
   - Corrección: `Labor Day (1st Monday) + back to school`.
3. **03 «Manager Monthly» `B16` (L1525, POR_CELDA)**
   - Qué falla: el plazo de la FLSA es un mínimo federal; hay estados que piden más (NY Labor Law §195(4): 6 años).
   - Corrección: `File this month's time-clock records (FLSA minimum: time cards 2 years, payroll 3 years; some states require longer, e.g. NY 6)`.
4. **01 «Kitchen Opening» `B10` (L72, c0055)**
   - Qué falla: la tarea está en imperativo para el empleado («Report… to the person in charge»), pero `D10` la asigna
     al Head chef, que es precisamente quien recibe el aviso. Además, §2-201.11 incluye la herida infectada.
   - Corrección: `Check no one has vomiting, diarrhea, jaundice, sore throat with fever or an infected cut; if so, no food handling (FDA 2-201.11)`.
5. **01 «Kitchen Opening» `B17` (L98, c0063)**
   - Qué falla: «dishwasher» en EE. UU. es también el puesto (el friegaplatos), y el resto del kit dice «dish machine»
     (L2254 y L2489).
   - Corrección: `Turn on the dish machine and check chemical levels`.
6. **03 «Manager Weekly» `B16` (L1373, c0361)**
   - Qué falla: es un calco de albarán → factura. En EE. UU. la factura llega con el pedido.
   - Corrección: `Match delivery invoices to vendor statements and chase missing credits`.
7. **Calcos en las instrucciones:**
   - «it is the FRAME of the day» y «the frame of the day»: c0029 en 11 hojas (L29, 765, 1158, 1696, 2191, 2650, 3086,
     3283, 3508, 4047 y 4101), más c0033, c0229, c0313, c0442, c0810, c0817 y c0873. Corrección: `BACKBONE` /
     `backbone`, mismas frases.
   - c0014 (L14), corrección: `▸ File the signed sheets — they prove the work was done, and who did it`.
   - c0769 (06 «Patio Season» `B15`, L3027), «Store furniture in storage», corrección: `Move the furniture into storage`.
8. **05 «Quarterly & Annual» `B23` (L2612, c0661)**
   - Qué falla: el punto de hielo es una comprobación casera y frecuente, no algo que haga un Technician una vez al año.
   - Corrección: `Thermometers: ice-point check (32 °F) weekly and after any drop; send the reference thermometer for certified calibration yearly`.
   - `D23` y `E23` se quedan.
9. **05 «Quarterly & Annual» `E7` (L2565)**
   - Qué falla: lo normal en un casual de EE. UU. es tener charbroiler (hamburguesas, steaks), y para eso NFPA 96 pide
     limpieza trimestral; B7 ya lo dice.
   - Corrección: valor por defecto `Quarterly`. `E7` es verde y editable.
10. **06 «Patio Season» `B17` (L3037, c0771)**
    - Qué falla: las estufas de patio de EE. UU. son de propano, y el fire code (NFPA 58, cap. 8) prohíbe guardar las
      bombonas dentro del local.
    - Corrección: `Store the patio heaters for winter; propane tanks disconnected and kept outdoors in a locked cage, never inside`.
11. **09 «Cash Drawer Closing» `A49` (L3710, POR_CELDA)**
    - Qué falla: «Cash sales (counted − starting bank)» no son las ventas en efectivo cuando las propinas de tarjeta se
      pagan del cajón; la cuenta es correcta, pero el rótulo engaña a quien lo compare con el «cash sales» de la Z.
    - Corrección: `Net cash (counted − starting bank)`.
12. **09 DV de `B27:B42` (L3725, c0938)**
    - Qué falla: las filas 41-42 son cartuchos, no billetes ni monedas, y «positive» excluye el 0 que la DV sí admite.
    - Corrección: `Enter how many bills, coins or rolls: a whole number (0 or more), no decimals.`
13. **09 «Cash Drawer Opening» `D23` (L3580, c0889)**
    - Qué falla: cita la pestaña sin comillas, contra D6.
    - Corrección: `Deducted from cash on the "Cash Drawer Closing" sheet`. D23:G23 mide 66, así que cabe.
14. **02 «Cold Station» `B10` (L937) y «Mise en Place» `B10` (L1046), POR_CELDA**
    - Qué falla: falta «or below». §3-402.11 dice «−20 °C (−4 °F) **or below**».
    - Corrección: `…confirm it was frozen at −4 °F or below for 7 days (or −31 °F or below until solid + 15 h); keep the record 90 days (FDA Food Code 3-402.11)`.
    - En Mise en Place: `(−4 °F or below 7 days, or −31 °F or below + 15 h, FDA Food Code 3-402.11)`.
15. **02 «Cold Station» `B11` (L942)**
    - Qué falla: el kit cita §3-402.11 para el crudo, pero no el aviso al consumidor que el inspector revisa a la vez
      (§3-603.11).
    - Corrección: `Portion carpaccio, ceviche, tartare (menu carries the raw/undercooked consumer advisory, FDA 3-603.11)`.
16. **05 «Instructions» `B14` (L2179)**
    - Qué falla: dice «by product family», pero la cabecera de la tabla es «Food group» (L2412).
    - Corrección: `…freezer shelf life by food group:…`.

---

## DUDAS (no demostradas)

- **D1 · 02 «Hot Line» `B27` (L875, c0252).** «filter the oil ONLY below 104 °F, never hot» viene del ES y es
  prudente. Pero las freidoras de EE. UU. con filtro incorporado (Frymaster, Pitco) se filtran **en caliente** según
  su manual, y algunas grasas sólidas a 104 °F ya ni fluyen. Propuesta: `Turn off the fryer and filter per the fryer
  manufacturer's procedure (built-in filters run hot: face shield, gloves, apron); by hand, only below 104 °F; used
  oil to the recycler's container`.
- **D2 · 09.** No hay *server checkout* (cada camarero entrega el efectivo que debe y su informe), ni tip-out (busser,
  bar, runner), ni *paid-outs* del cajón. En un casual de EE. UU. con camareros que cobran es lo habitual. Meterlo
  como tarea nueva cambiaría el contador (G6); como texto, cabría en c0938 o en B9.
- **D3 · 06 «Christmas & NYE» `E23` (L2967).** «12:00 AM» para la medianoche es correcto según `hora_us`, pero
  ambiguo (NIST recomienda «12:00 midnight»). Propuesta: `Midnight`, solo en esa celda.
- **D4 · B02.** Faltan los festivos federales que cierran los bancos (MLK, Presidents', Juneteenth, Columbus,
  Veterans), y esos días afectan al «Prepare the bank deposit» del 09. La SPEC no los pide.
- **D5 · 05 `E16` (L2593).** La recogida de aceite usado en EE. UU. es a demanda (semanal o quincenal). «Quarterly»
  vale como revisión de los recibos, no como frecuencia de recogida.
- **D6 · Alto de fila.** Las celdas largas con ajuste de texto y sin alto explícito (heredado del ES) se autoajustan
  en Excel de escritorio; está por confirmar en el test de Google Sheets de F3 (SPEC §9).

---

## Lo que intenté refutar y se sostiene

- **Normas:**
  - 41 °F, 0 °F y 135 °F;
  - date marking a 7 días con el día 1 = preparación;
  - parásitos §3-402.11 con registro de 90 días y etiquetas shellstock de 90 días (§3-203.12);
  - anillo liso (§2-303.11), lavamanos a 100 °F (§5-202.12) y lavado de vegetales (§3-302.15);
  - 9 alérgenos;
  - OSHA 1910.157(e)(2) mensual y (e)(3) anual;
  - NFPA 96: campana por volumen y extinción cada 6 meses;
  - EPA 608 y backflow anual;
  - FLSA, 2 y 3 años (§516.5-516.6);
  - punto de hielo a 32 °F;
  - 104 °F = 40 °C, 10 °F ≈ −12 °C;
  - el penny sigue siendo de curso legal.
- **Notas UK:** Mothering Sunday, bank holidays y Boxing Day; desproteger la hoja para libras, CAD o AUD.
- **Festivos:** Mother's Day (2.º domingo de mayo, 36 U.S.C. 117), Father's Day (3.er domingo de junio, 109), Memorial
  Day (último lunes), Thanksgiving (4.º jueves), Mardi Gras y Easter «varies». El orden por meses está bien.
- **Caja:**
  - denominaciones y multiplicadores;
  - cartucho de 25¢ = $10 y de 10¢ = $5;
  - caso de prueba = 204.91 (188 + 1.91 + 15);
  - propinas pagadas del cajón: se suman en C51 y cuadran a 0;
  - el fondo medio y el descuadre en valor absoluto del registro mensual;
  - la CF ámbar (FFF3CD) en C54 y H5:H35, tal como dicen las instrucciones.
- **Técnica:**
  - 157 fórmulas: mismos patrones; ninguna con SEARCH o FIND;
  - DV «✓,—,N/A» y CF `$F5="✓"` / `$E5="✓"`, intactas;
  - `'Cash Drawer Opening'!C23` y `'Valentine''s Day'!` en los definedNames;
  - las 23 citas entre comillas existen tal cual (rótulos, pestañas y ficheros);
  - XML crudo y docProps sin español, sin € y sin °C;
  - summary combinado A:B y cabeceras del registro con ajuste de texto: nada cortado.

---

## Ronda 1: aplicado / no aplicado y por qué

> Sesión Claude Code, 17-oct-2026, con las instrucciones del orquestador. Solo se han cambiado textos:
> `textos_en/G1.json` y `G2.json` (27 cadenas), `mapas.POR_CELDA`, `CALENDARIO`, `ADAPTAR` y `REGLAS_US`. La
> estructura no se ha tocado. Después se regeneró `textos_es.json` con `extraer_textos.py`: los ids y el censo
> salen iguales y solo cambian `adaptar` y `en_por_celda`. Se reconstruyó en el VPS y se pasaron otra vez todos los
> gates (§F2-NOTAS 3).

| # | Hallazgo | Estado | Qué se hizo / por qué no |
|---|---|---|---|
| M1 | Z del POS sin definir | **Aplicado** | `A53` «POS Z report: sales + tax, excl. tips». `Monthly Cash Log!G4` «POS Z (+ tax, no tips)». B15 (c0867), B17 (c0869) y la nota A37 (c0951) llevan el texto exacto del informe |
| M2 | Nómina mensual | **Aplicado** | c0406 con el texto del informe; E18 se queda en «Monthly». `REGLAS_US.frecuencia_pago` y SPEC §3 |
| M3 | Enfriamiento | **Aplicado** | c0248 (02 «Hot Line» B23). El tema ES ya es «guardar proteínas sobrantes» |
| M3 | Recalentado 165 °F | **No aplicado** | c0246 es «mantenimiento en caliente», no «regenerar o recalentar», y en el ES no hay ninguna fila de ese tema. La regla queda en `REGLAS_US.recalentado`, en SPEC §3 y en G7 (165) para una v2.1 con fila propia |
| M3 | Tiras de sanitizante | **Aplicado en parte** | En c0164 (01 «Kitchen Closing» B15, «limpiar y desinfectar superficies»), y también en c0063 («lavavajillas y nivel de producto», el mismo tema). **c0091 no se toca**: el ES es «trapos limpios disponibles», otro tema. `REGLAS_US.sanitizante` y SPEC §3 |
| M4 | «Overnight» | **Aplicado** | c0040 «☐ AM  ☐ Mid  ☐ PM» en las 17 cabeceras |
| m1 | Super Bowl | **Aplicado** | «Super Bowl Sunday (2nd Sunday in Feb)». La coletilla opcional de 2027 no: es una fecha que caduca |
| m2 | Labor Day | **Aplicado** | «Labor Day (1st Monday) + back to school» |
| m3 | Plazo FLSA | **Aplicado** | POR_CELDA 03 B16 con «FLSA minimum… some states require longer, e.g. NY 6». `REGLAS_US.fichajes` añade NY Labor Law §195(4) |
| m4 | Síntomas | **Aplicado** | c0055, redactado para quien lo comprueba (+ herida infectada). ADAPTAR ajustado |
| m5 | «dish machine» | **Aplicado** | c0063 (va junto con las tiras de M3) |
| m6 | Calco del albarán | **Aplicado** | c0361 «Match delivery invoices and packing slips to vendor statements; chase missing credits» |
| m7 | «frame of the day» y calcos | **Aplicado** | «BACKBONE / backbone of the day» en las 18 apariciones (8 cadenas). c0014 y c0769 con el texto del informe |
| m8 | Calibración de termómetros | **Aplicado** | c0661 con el texto del informe; D23 y E23 se quedan |
| m9 | E7 «Quarterly» | **No aplicado** | Es un valor por defecto que depende del criterio (volumen y tipo de cocina), no algo demostrado. B7 ya dice cuándo toca trimestral y E7 es verde y editable |
| m10 | Propano | **Aplicado** | c0771. Se conserva la condición del ES («If the patio is closed in winter») |
| m11 | «Cash sales» | **Aplicado** | A49 «Net cash (counted − starting bank)» |
| m12 | DV con los cartuchos | **Aplicado** | c0938 con el texto del informe |
| m13 | Pestaña sin comillas | **Aplicado** | c0889 con el texto del informe |
| m14 | «or below» | **Aplicado** | POR_CELDA 02 «Cold Station» B10 y «Mise en Place» B10 |
| m15 | Aviso al consumidor | **Aplicado** | c0262 enriquece la fila de porcionar crudos (mismo tema). `REGLAS_US.aviso_consumidor` y SPEC §3 |
| m16 | «food group» | **Aplicado** | c0533 |
| D1 | Aceite a 104 °F | **Aplicado (regla neutra)** | c0252, según el procedimiento del fabricante (filtros integrados a temperatura de servicio; a mano, que enfríe antes, guantes y recipiente estable). Sin cifra: `mapas.CELSIUS_SIN_F`, 104 fuera de G7 y ADAPTAR ajustado |
| D2 | Server checkout, tip-out, paid-outs | **No (v2.1)** | Son filas nuevas |
| D3-D6 | Medianoche, festivos bancarios, aceite E16, alto en Sheets | **No** | Decisión del orquestador. D6 se verá en el test de Google Sheets de F3 |

**Para una v2.1** (necesitan filas nuevas o cambiar la estructura):
- fila de recalentado a 165 °F (§3-403.11);
- cubos de sanitizante para los trapos (§3-304.14), junto a c0091;
- server checkout, tip-out y paid-outs en el 09;
- festivos federales con bancos cerrados en el B02.
