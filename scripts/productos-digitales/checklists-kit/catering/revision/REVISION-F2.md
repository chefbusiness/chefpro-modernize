# Catering Checklists Kit Pro — Revisión adversarial F2 (18-oct-2026 · sesión Claude Code)

> Revisor único. Leídos enteros `dump_en.txt` (2.695 líneas), el delta `SPEC.md`, `F2-NOTAS.md` y `POR_CELDA` /
> `REGLAS_US` de `mapas_catering.py`. Contraste con `dump_es.txt` celda a celda donde había duda. Comprobación ligera
> con openpyxl (CPU < 52 °C) de los 11 xlsx de `astro-site/public/dl/catering-checklist-templates/`: bloqueo, formato y
> relleno de las celdas del 09 y relleno de la CF del 01. Sin builds ni Playwright.
> Las líneas `L` son de `dump_en.txt`.

## Veredicto

**NO está listo para vender todavía: 1 BLOQUEANTE + 11 MAYOR + 15 MENOR.** Todo se arregla con texto por celda
(`POR_CELDA` / `G1.json`). Solo M5 toca una regla de la CF, y M6 y M7 cambian filas de sitio sin tocar los contadores.
Fórmulas, DV, bloqueo y formatos del 09 están bien. Lo que falla es lo que un gate no puede leer: el sentido de la
norma, el orden de las operaciones y la coherencia entre libros.

| ID | Sev. | Libro · hoja · celda | Tema |
|---|---|---|---|
| B1 | BLOQUEANTE | 06 · Outdoor Events · B16 (L1475) + `REGLAS_US['tphc']` | «4 h max … **then serve** or discard» |
| M1 | MAYOR | 02 · Transport & Delivery · B26 (L304) | El reloj del 3-501.19 no empieza en la salida ni acaba en el trayecto |
| M2 | MAYOR | 04 · Event Chef · B25 (L723) (+ 05 B18, L1185) | Sobrantes: falta la regla de descarte |
| M3 | MAYOR | 01 · Production · B32 (L116) | No se dice cómo enfriar lo que se produce la víspera |
| M4 | MAYOR | 06 · Cocktail Reception · B9 (L1390) | Ceviche y tartar sin consumer advisory (3-603.11) |
| M5 | MAYOR | 01-06 + B01 · 15 hojas · 32 filas de cabecera | La CF pinta de verde claro las cabeceras: texto blanco ilegible |
| M6 | MAYOR | 08 · Commissary Opening · B9 / B20 (L1774, L1828) | Se carga la comida antes de revisar y preenfriar el vehículo |
| M7 | MAYOR | 08 · Commissary Closing · B5:D19 (L1866-1938) | El orden del cierre sigue sin sentido |
| M8 | MAYOR | 08 Opening B13 (L1794) · 09 Before B6 (L2007) · 06 Weddings B6 | El guaranteed count se cierra en tres momentos distintos |
| M9 | MAYOR | 09 · Event Settlement A15/D15/A16/D16 · Billing Log A3/D3 | La línea del tax «on the non-taxable (0)» y el tipo a 0 sin aviso |
| M10 | MAYOR | B02 · Events Calendar · filas 3-5 (L2597-2609) | El calendario pone abril antes que el 17 de marzo |
| M11 | MAYOR | B02 · Events Calendar · D8 (L2604) | «or with licensed bartenders» como alternativa a la licencia |
| m1-m15 | MENOR | ver abajo | |

---

## BLOQUEANTE

### B1 · 06 «Outdoor Events» B16 (L1475) · y la fuente `mapas_catering.REGLAS_US['tphc']` (≈ L543)
- **Qué falla.** «4 h max from when it comes out (mark the time), **then serve or discard**». Leído al pie de la letra,
  dice que a las 4 h se puede servir o tirar, cuando lo que queda a las 4 h se tira. La fuente del kit trae el mismo
  error: `REGLAS_US['tphc']` = «4 h como máximo **y después servir o descartar**». Para el frío a 6 h faltan dos
  cosas: vigilar que no pase de 70 °F y tirarlo en cuanto pase. Es el único punto del kit donde un empleado al pie de
  la letra pondría comida en riesgo: un buffet al aire libre y en verano.
- **Norma.** FDA Food Code 2022 §3-501.19:
  - (B)(3)-(4): «cooked and served, served at any temperature if ready-to-eat, or discarded, **within 4 hours**»; lo
    que no esté marcado o pase de 4 h se descarta.
  - (C)(2)-(4): vigilar que la parte más caliente no pase de 70 °F; descartar si la pasa, o en todo caso a las 6 h.
- **Corrección EN (B16):**
  `Double the temperature checks: outdoors, food warms up much faster. Hold hot food at 135 °F or above and cold food at 41 °F or below. Food without temperature control falls under time as a public health control (FDA Food Code 3-501.19): mark the time it came out of temperature control and serve it within 4 h; whatever is left at 4 h is discarded, and it can't go back into hot or cold holding to restart the clock. Cold food can go up to 6 h only if it came out at 41 °F or below and you check it never passes 70 °F: discard it as soon as it does, and at 6 h. This needs a written procedure and, depending on your county, notice to the health department. In hot weather, refill more often and in smaller amounts`
- **Fuente:** `REGLAS_US['tphc']` → «servir o descartar DENTRO de las 4 h (lo que quede a las 4 h se descarta); frío
  hasta 6 h si sale a 41 °F o menos, vigilando que no pase de 70 °F (se descarta si pasa); procedimiento escrito y
  hora marcada».

## MAYOR

### M1 · 02 «Transport & Delivery» B26 (L304)
- **Qué falla.** «4 h max from the marked departure time».
  - Las 4 h cuentan desde que el alimento sale de 41 / 135 °F, que puede ser al emplatar en el commissary y no al
    arrancar la furgoneta.
  - Incluyen el servicio en el venue.
  - No se dice que a las 4 h se tira, ni que hace falta procedimiento escrito.
  - Tal como está, un equipo puede gastar 3 h de trayecto y abrir después un buffet de 4 h: 7 h en total.
- **Norma.** FDA Food Code 2022 §3-501.19(A) (procedimiento escrito) y (B)(2)-(4).
- **Corrección EN:**
  `Hold the cold chain the whole trip: cold 41 °F or below, hot 135 °F or above. Anything traveling without temperature control goes under time as a public health control (FDA Food Code 3-501.19, written procedure required): mark the time it left 41 °F / 135 °F; the 4 h include the trip AND the service at the venue, and whatever is left at 4 h is discarded`

### M2 · 04 «Event Chef» B25 (L723); de paso, 05 «Breakdown & Load-Out» B18 (L1185)
- **Qué falla.**
  - «decide what to keep (cool it per 3-501.14) and what to discard» no dice qué se tira. La 05 B18 sí lo dice («what
    sat exposed on the buffet or was held under TPHC gets discarded»), pero la hoja del chef se imprime sola (04 B11,
    «Print only the tab for the role you need»).
  - En la 05 B18, «cool it» se aplica también a lo que ya estaba frío.
- **Norma.** FDA Food Code 2022 §3-501.14 (enfriamiento) y §3-501.19(B)(4) (descarte).
- **Corrección EN, 04 B25:**
  `Inventory leftovers: keep only food that stayed at 135 °F or above / 41 °F or below and never went out to guests (cool hot food from 135 °F to 70 °F within 2 h, then to 41 °F within 4 h more, FDA Food Code 3-501.14); anything that sat on the buffet or was held under time as a public health control (FDA Food Code 3-501.19) gets discarded`
- **Corrección EN, 05 B18 (opcional, misma lógica):** cambiar «cool it (135 °F to 70 °F…)» por
  `cool the hot food (135 °F to 70 °F within 2 h, then to 41 °F within 4 h more, FDA Food Code 3-501.14) and put the cold food straight back at 41 °F or below`
  y dejar igual el resto de la celda.

### M3 · 01 «Production» B32 (L116); afecta también a B29 (L108)
- **Qué falla.** La víspera se hacen fondos, salsas base, braseados y confitados, en las cantidades de un catering, y
  ninguna tarea del 01 dice cómo enfriarlos. Es el mayor riesgo de un catering: el enfriamiento lento de grandes
  lotes es la vía clásica de *C. perfringens* en banquetes. El kit sí lo cita, pero solo para los sobrantes (04 y 05).
- **Norma.** FDA Food Code 2022 §3-501.14 (ya está en `REGLAS_US['enfriamiento']` del base).
- **Corrección EN (B32):**
  `Do the pre-cooking: confit, braises, sous-vide. Cool anything made ahead in shallow pans, an ice bath or the blast chiller: 135 °F to 70 °F within 2 h, then to 41 °F within 4 h more (FDA Food Code 3-501.14), and log it`

### M4 · 06 «Cocktail Reception» B9 (L1390)
- **Qué falla.** Hay estaciones de ceviche y tartar (B8, L1387) y no hay consumer advisory. En el base se corrigió
  esto mismo («carpaccio, ceviche, tartare… consumer advisory, FDA 3-603.11», `revision/REVISION-F2.md` L175), y la
  regla ya existe en `REGLAS_US['aviso_consumidor']`.
- **Norma.** FDA Food Code 2022 §3-603.11 (disclosure + reminder para animal crudo o poco hecho).
- **Corrección EN:**
  `Ceviche, tartare and any fish served raw or undercooked — parasite destruction: use only fish with documented freezing (−4 °F or below for 7 days, or −31 °F or below until solid + 15 h; FDA Food Code 3-402.11), keep the record 90 days and note the lot; put the raw/undercooked consumer advisory on the station sign or menu (FDA Food Code 3-603.11)`

### M5 · CF en las cabeceras internas: 01-06 y B01 (15 hojas, 32 filas)
- **Qué falla.**
  - Cada hoja de tareas lleva la CF `$E6="✓"` (relleno sólido `C8E6C9`) sobre `A6:G<fin>`.
  - Las cabeceras de sección que caen dentro de ese rango tienen escrito «✓» en la columna E, como rótulo. Ejemplo:
    01 «Production» E16, L65, con fondo `2D2D2D` y letra blanca en negrita.
  - La CF las da por hechas desde que se abre el libro: el fondo pasa a verde claro y el texto blanco apenas se lee.
- **Filas afectadas** (volcado por hoja):

  | Libro | Hoja | Filas |
  |---|---|---|
  | 01 | Production | 16, 26, 40 |
  | 02 | Transport & Delivery | 14, 24, 31 |
  | 03 | Event Manager | 16, 28, 39 |
  | 03 | Quarterly & Annual | 14, 22, 29 |
  | 04 | Event Chef, Banquet Captain, Server, Bartender | 14 y 23 en cada una |
  | 05 | Setup & Load-In | 16, 27, 36 |
  | 05 | Breakdown & Load-Out | 14, 23 |
  | 06 | Weddings | 15 |
  | 06 | Corporate | 13 |
  | 06 | Cocktail Reception | 15 |
  | 06 | Outdoor Events | 14 |
  | B01 | Pre-Event Briefing | 13, 21, 30 |

- **Por qué no lo vio nadie.** Solo este kit tiene varias tablas por hoja: el base, el bar y la cafetería dan 0
  cabeceras «✓» fuera de la fila 4/5. Además, G1 exige que la CF sea idéntica a la del ES, así que también es una
  errata del ES (`kit-tareas-catering`) y va a la §6 de la SPEC.
- **Corrección (recomendada).** Cambiar la fórmula de cada una de esas 15 CF a `AND($E6="✓",$B6<>"Task")`; en las
  hojas cuyo rango empieza en la fila 6, misma fila de anclaje. Los contadores no cambian, porque ya restan las filas
  «Task». Hay que añadir la excepción en G1, igual que con `FORMULAS_POR_CELDA`.
- **Alternativa.** Poner `Done` en lugar de «✓» en la columna E de las 32 cabeceras internas. Antes, comprobar que
  cabe en el ancho de E. La fórmula `COUNTIFS(...,"Task",E,"✓")` daría entonces 0, que también es correcto.

### M6 · 08 «Commissary Opening»: orden de la carga (B9 L1774 frente a B20 L1828)
- **Qué falla.** En la fila 9, a las 7:00, se cargan los isotermos y se registra la temperatura de salida. Eso es
  antes de imprimir los BEO (fila 12), de las hojas de ruta (fila 11), del briefing (fila 19) y, sobre todo, de
  «Check the transport vehicles» (fila 20, 7:30). El propio 02 B8 manda preenfriar el vehículo ANTES de cargar.
  Contradice el 02 y cualquier ops manager lo ve.
- **Corrección EN.** Rotar B y C de las filas 9, 20, 21 y 22. Las columnas D y E se quedan con su fila, así que la
  carga pasa a las 7:30 AM, después del briefing.

  | Fila | B | C |
  |---|---|---|
  | 9 | `Check the transport vehicles: clean, fueled and the refrigeration on, pre-chilled to 41 °F or below before anything is loaded` | `Logistics` |
  | 20 | `Check the portable equipment` | `Storage` |
  | 21 | `Review the day's order of events` | `Office` |
  | 22 | el texto actual de B9 («Load the insulated carriers… 02-catering-transport-delivery-checklist.xlsx») | `Outside` |

### M7 · 08 «Commissary Closing» B5:D19 (L1866-1938): orden del cierre
- **Qué falla.** El POR_CELDA solo arregló las filas 16-19. Lo demás sigue en el orden heredado del ES:
  - fila 6: «no queda nadie»;
  - fila 9: se cierran persiana y puertas;
  - fila 10: se apagan las luces;
  - después: baldear el muelle (12), vaciar papeleras (14) y descargar furgonetas (16), con la gente ya encerrada y a
    oscuras.

  Además, «Last one out» descarga las furgonetas y el commissary no dice qué hacer con la comida que vuelve.
- **Corrección EN** (B / C / D; E = `Close` en todas; 15 tareas, contadores iguales):

  | Fila | B | C | D |
  |---|---|---|---|
  | 5 | `Unload and clean the delivery vehicles: returned food that still qualifies goes straight to the blast chiller or walk-in to finish cooling (FDA Food Code 3-501.14); the rest is discarded` | Logistics | Ops manager |
  | 6 | `Check in the portable equipment that came back` | Storage | Ops manager |
  | 7 | `Collect and store the outdoor equipment that came back (tents, umbrellas and patio heaters)` | Outside | Ops manager |
  | 8 | `Clear and hose down the loading dock: no carts, no pallets and no trash` | Outside | Ops manager |
  | 9 | `Empty trash cans in common areas and restrooms` | Restrooms | Ops manager |
  | 10 | `Turn off the commissary equipment that shouldn't run overnight (ovens, fryer, hood) and leave the walk-ins and blast chiller on` | General | Ops manager |
  | 11 | `Turn off the card terminal (or leave it on standby)` | POS | Ops manager |
  | 12 | `Final safety check (gas, water, outlets)` | General | Ops manager |
  | 13 | `Check that windows are closed` | General | Ops manager |
  | 14 | `Turn off HVAC` | General | Ops manager |
  | 15 | `Check that no staff or visitors are left in the commissary before closing` | General | Ops manager |
  | 16 | `Turn off lights (leave security lighting)` | General | Ops manager |
  | 17 | `Set the alarm` | Entrance | Ops manager |
  | 18 | `Close security gate and doors` | Entrance | Last one out |
  | 19 | `Lock up and verify it is locked` | Entrance | Last one out |

  Para el ES (§6): es errata de toda la secuencia, no solo de las filas 16-19.

### M8 · El guaranteed count, incoherente entre libros
- **Qué falla.**
  - 09 «Before the Event» B6 (L2007): «confirmed» a 15 días.
  - 06 «Weddings» B6 (L1254): «final guaranteed count» la semana antes.
  - 08 «Commissary Opening» B13 (L1794): «Confirm the guaranteed count… with each client» el mismo día, a las 7:15 AM,
    con C13 = «Front desk».
  - En EE. UU. el guarantee se cierra en una fecha límite anterior al evento y se factura el mayor entre guarantee y
    actual (`REGLAS_US['guaranteed_count']`). Confirmarlo la mañana del evento contradice el concepto y el After B5.
- **Corrección EN:**
  - 08 B13: `Call each client's day-of contact: confirm arrival time, site contact and any last-minute changes (the guaranteed count is already locked; extra guests are billed per the contract)`
  - 08 C13: `Office`
  - 09 Before B6: `Deadline for the guaranteed count (final headcount) sent to the client in writing; the count locks on that date, per your contract`. D6 sigue en «15 days out»: es cuando se envía.

### M9 · 09: la línea del tax a 0 y el tipo a 0 sin aviso
- **Qué falla.**
  - A16, «Tax on the non-taxable subtotal (0)» (L2163), es un oxímoron que el comprador va a preguntar.
  - Con C3 = 0 (L2259) la hoja de liquidación enseña «Sales tax 0.00» sin avisar de nada. D15 solo dice «Formula.»
    (L2162).
  - El que no lea la B19 de instrucciones factura sin sales tax, y el sales tax no cobrado lo debe el vendedor.
- **Norma.** [estatal] department of revenue (`REGLAS_US['sales_tax']`).
- **Corrección EN** (todo por `POR_CELDA`, mismas celdas):
  - Billing Log A3: `Sales tax rate (state + local) — set it first`
  - Billing Log D3: `0 = no sales tax until you enter your combined rate (state + local), e.g. 0.0825 for 8.25%. "Event Settlement" applies it to the taxable subtotal; here it is applied to the whole base, so "Invoice total" is an estimate if part of the event is exempt: the exact figure is in "Event Settlement".`
  - Settlement A15: `Sales tax (rate set in Event Billing Log C3)`
  - Settlement D15: `Formula: taxable subtotal × the rate in "Event Billing Log" C3. It stays at $0 until you enter your rate there.`
  - Settlement A16: `Non-taxable subtotal: no sales tax`
  - Settlement D16: `Always $0: exempt items and tax-exempt clients carry no sales tax. Nothing to enter.`
- Comprobado: C3 está desbloqueada, en verde y con formato `0.00%`. «0.0825» funciona en Excel y en Sheets.

### M10 · B02 «Events Calendar», filas 3-5 (L2597-2609): orden cronológico
- **Qué falla.** La fila 3, «April — First Communion season (starts)», va antes que la 4, «Mar 17 — St. Patrick's
  Day», y que la 5, «Mar–Apr — Easter & Passover». Viene heredado del ES, donde las Comuniones van antes del Día del
  Padre (19-mar).
- **Corrección EN.** Mover B, C, D y E entre las filas 3, 4 y 5. B y C salen del `CALENDARIO`; D y E necesitan
  `POR_CELDA` (o reordenar el CALENDARIO y sus textos).

  | Fila | B | C | D | E |
  |---|---|---|---|---|
  | 3 | Mar 17 — St. Patrick's Day | Holiday | su D actual, corregido por M11 | 3 weeks |
  | 4 | Mar–Apr — Easter & Passover (dates vary) | Holiday | su D actual | 3 weeks |
  | 5 | April — First Communion season (starts) | Celebration | `Kids' + adult menus, themed decor` | 2–3 months |

### M11 · B02 «Events Calendar» D8 (L2604)
- **Qué falla.** «alcohol only under your license **or with licensed bartenders**» da a entender que unos bartenders
  con permiso sustituyen la licencia del negocio. No es así: la licencia (catering o venue) la pide el estado; el
  permiso del camarero, donde existe, es aparte.
- **Norma.** [estatal] ABC / liquor authority (`REGLAS_US['licencia_eventos']`).
- **Corrección EN:**
  `Corporate parties and family gatherings with a themed menu; alcohol only under the license your state requires (yours or the venue's), 21+ with ID`

## MENOR

| ID | Celda (línea) | Qué falla y por qué | Corrección EN exacta |
|---|---|---|---|
| m1 | 05 «Setup & Load-In» B29 (L1091) | Al recalentado le falta «within 2 h» (FDA §3-403.11(A); el base ya lo dice así) | Cambiar `reheat cold food to 165 °F first, FDA Food Code 3-403.11` por `reheat cold food to 165 °F within 2 h first, FDA Food Code 3-403.11`; el resto igual |
| m2 | 06 «Cocktail Reception» B10 (L1393) | La FALCPA dice «crustacean shellfish»; los moluscos no son alérgeno mayor en EE. UU. | `…(FALCPA + FASTER Act: milk, egg, fish, crustacean shellfish, tree nuts, peanuts, wheat, soy and sesame); UK: 14` |
| m3 | 09 Instructions B20 (L1963); 04 «Banquet Captain» B26 (L811) | «for the IRS it is wages» es impreciso. El service charge es ingreso del negocio; lo que se reparte al personal es salario no-propina (Rev. Rul. 2012-18). Tal como está, parece que todo el cargo es salario | B20: `▸ What carries sales tax is decided by your state (check with your CPA or the department of revenue): in many states food, drinks, rentals and the mandatory service charge. A mandatory service charge is NOT a tip: it is your revenue, and whatever part of it you pay to staff is wages on payroll for the IRS, not tips (Rev. Rul. 2012-18). The gratuity is the client's choice, goes on a separate line and belongs to the team. A tax-exempt client needs their exemption certificate on file. If the two subtotals don't add up to quote + extras, the sheet warns you.` · B26: `Handle gratuities and feedback for the service team: gratuities per house policy and your state's rules; a mandatory service charge is NOT a gratuity: what you pay out of it to staff is wages for the IRS (Rev. Rul. 2012-18)` |
| m4 | 09 Settlement D10 (L2147) | La hoja no dice dónde va el service charge (lo normal en EE. UU. es 18-22 %). D12 lo da por incluido en lo gravable | `The accepted amount BEFORE sales tax, mandatory service charge included if your quote has one.` |
| m5 | 09 After B8 (L2084) | «not inside the invoice» contradice D11 (L2150) y After B6, que meten las roturas en Extras. Viene del ES | `Breakage or incident charges communicated to the client before the invoice goes out, so they never show up on it as a surprise` |
| m6 | 09 Instructions B35 (L1972) | El 09 va por evento, no por commissary | `▸ "N/A" = not applicable to this event: that task comes OUT of the total (don't delete it, mark it N/A). "—" = not done: it still counts as pending and lowers the percentage, which is the point.` |
| m7 | 09 Instructions B22 (L1965) | El valor de cada billete está dentro de la fórmula de C30:C45; no hay columna de «valor» que cambiar | Última frase: `…in the UK, Canada or Australia, unprotect the sheet (no password) and change each row's label and the multiplier in its Subtotal formula.` |
| m8 | 08 Opening B8 (L1769), B10 (L1779); Closing B8 (L1881) | Restos de restaurante: «front door» y «POS» chocan con 09 B7 («a catering business has no counter or POS shift») | Opening B8: `Raise the security gate and unlock the doors` · Opening B10: `Turn on the card terminal and the invoicing software (deposits and balances paid by card)` · Closing: ya en M7, fila 11 |
| m9 | 03 «Quarterly & Annual» B31 (L615) | El I-9 se hace en los 3 días hábiles del alta, no cada trimestre (8 CFR 274a.2(b)(1)(ii); añadir a `REGLAS_US['i9']`) | `This quarter's new hires: check each new event employee has Form I-9 (completed by their 3rd business day) and W-4 on file, and the time-clock records filed` |
| m10 | 03 «Event Manager» B29 (L450); B01 B14 (L2491) | «starter, mains» es UK; en un banquete de EE. UU. se dice «appetizer, entrée» | B29: `Control service timing: appetizers, entrées, dessert, coffee` · B14: `Review the full menu with the team: appetizers, entrées, desserts` |
| m11 | 03 «Event Manager» A27 (L441), A38 (L473) | Mayúsculas incoherentes con el resto de rótulos, y «After event» sin artículo | A27: `During the Event` · A38: `After the Event` |
| m12 | 01 Instructions B10 (L14); 08 Instructions B12 y B16 (L1717, L1719) | En el 01 la columna se llama «Time», no «Due by». En el cierre del 08 se llama «When» | 01 B10: `▸ Green cells are editable: assigned to, time, notes.` · 08 B16: `▸ Everything filled in daily is GREEN: Assigned to, Due by (When, at closing), ✓ Done, Initials and Notes.` |
| m13 | 06 Instructions B6 (L1233) | Promete «formal banquets» y no hay pestaña de banquetes | `▸ Weddings, corporate events, cocktail receptions and outdoor events.` |
| m14 | B02 B5 (L2587), C14 (L2633), D12 (L2624), D22 (L2674) | El 2.º domingo cae entre el 8 y el 14 de febrero (2027: el 14), así que «Early Feb» no siempre cuadra. El 4 de julio está tipado «Wedding». La fila de graduaciones no dice nada de graduaciones. Hanukkah aparece sin contenido | B5: `Feb — Super Bowl Sunday (2nd Sunday)` · C14: `Mixed` · D12: `Graduation open houses and party trays, outdoor events, rain plan Bs, tents` · D22: `Holiday menus: prime rib, ham, seafood, seasonal desserts; for Hanukkah (dates vary), latkes and brisket` |
| m15 | 04 «Bartender» B11 (L938) | Un gin and tonic premezclado pierde el gas; ningún bartender de EE. UU. lo prepara en batch | `Prep cocktail batches if needed (sangria, punch, batched margaritas) in their own labeled containers; never refill a liquor bottle` |

## Comprobado sin hallazgos

- **Español y España.** Sin €, IVA, APPCC, TPV, ITV, festivos ES ni °C en el EN: las 17 celdas con °C del ES salen
  todas en °F. Sin horas de 24 h; las 18 horas del 08 en `7:00 AM`. Fechas `MM/DD/YYYY`. «restaurant» solo aparece en
  la firma.
- **Correcciones de revisiones anteriores.** No reaparece ninguna:
  - ni tiras de sanitizante;
  - nunca se rellena una botella (04 B11);
  - 21+ con ID (04 B15 y B17, 06 B19, B02);
  - sin hollandaise;
  - el date marking es correcto: 3-501.17, 7 días, día 1 = preparación.
- **Normas de comida fuera del local.** Bien citadas: 41 / 135 °F (3-501.16), parásitos (3-402.11 con sus dos vías y
  los 90 días), lavado de manos a 100 °F (5-202.12), exclusión por síntomas (2-201.11), CFPM (2-102.12), NFPA 96
  (trimestral / semestral, extinción cada 6 meses) y OSHA 1910.157.
- **Permisos, chafing y alcohol.** Temporary food establishment permit, estación de lavado de manos, carpas con fire
  marshal y lona ignífuga. Chafing: mantiene, no recalienta, ni se recarga ni se mueve encendido, extintor a mano.
  Licencia del estado o del venue, TIPS / ServSafe Alcohol, alcohol del cliente.
- **Registros laborales.** FLSA: time cards 2 años y payroll 3; NY 6.
- **Jerga de catering.** Presente y bien usada: BEO, guaranteed / actual count, load-in / load-out, staging area, run
  sheet, COI + additional insured, hotel pans, cambros, chafing dishes, commissary frente a venue.
- **09: fórmulas, formatos y bloqueo.**
  - C14 avisa si las bases no cuadran.
  - C15 = C12 × `'Event Billing Log'!$C$3`; C17 sale de las bases.
  - Estados Paid / Pending / OVERDUE en C24 y K6:K30, ámbar en C22 y H6:H30.
  - Monedas US: el rollo de 25¢ son $10 y el de 10¢, $5.
  - Todas las entradas (C5:C13, C19, C21, C23, B30:B45, C47, A6:D30, F:G, I:J) están desbloqueadas y en verde, con
    formatos `#,##0.00`, `MM/DD/YYYY` y `0.00%`.
  - Las 6 hojas protegidas no tienen contraseña y permiten insertar filas, como dice la instrucción.
- **Contadores.** Las cachés casan con las filas de tareas (01 = 38, 02 = 24, 03 = 33 / 20, 08 = 18 / 15, 09 = 12 / 12,
  B01 = 20). Hay 5 filas libres dentro del rango en el 08 y el 09.
- **Citas.** Todas las citas a ficheros y pestañas existen: «Transport & Delivery», «Event Settlement», «Event Billing
  Log» C3, BONUS-01, la tabla al pie de «Production» y la columna «Frequency».

## DUDAS (no son defectos; decide John)

1. **Deposit = retainer** (09 Before B7, L2011; D19, L2172). En EE. UU., «non-refundable retainer» y «deposit»
   (que puede tener que devolverse si se cancela) no son lo mismo en un contrato. ¿Dejamos «Deposit» a secas y la
   política de cancelación en B11?
2. **Service charge en NY y MA.** En NY (12 NYCRR 146-2.19) y MA (M.G.L. c.149 §152A), un service charge que no se
   anuncia claramente como «no es propina» se presume del personal. Se puede añadir a m3: `in some states (e.g., NY, MA) a service charge not clearly disclosed as not a gratuity is presumed to belong to the staff`.
   Requiere `REGLAS_US`.
3. **El banquet captain y las propinas** (04 B26). Si el captain es supervisor según el test de la FLSA, no puede
   quedarse parte del tip pool (29 U.S.C. 203(m)(2)(B)). ¿Se añade «managers and supervisors can't keep any part of
   the tips»?
4. **«15 days out»** para firmar presupuesto y cobrar depósito (09 Before D5:D10). Las bodas en EE. UU. se reservan
   con 6-12 meses. Es editable y funciona como «a más tardar», pero ¿rótulo `By 15 days out`?
5. **Calibración de termómetros trimestral** (03 Q&A F17). FDA §4-502.11(B) dice «as necessary»; para sondas de
   evento lo práctico es semanal o cada vez que se caen. Criterio del kit.
6. **Comuniones en el calendario US** (filas 3 y 7). Están decididas en la SPEC, pero es un nicho (católico /
   hispano). ¿Quinceañeras y Bar / Bat Mitzvahs rendirían más? Si se cambia, es un dato del calendario, no del diseño.
7. **Fix de M5.** La errata está también en el ES `kit-tareas-catering` en producción. ¿Se corrige el ES en su
   próxima v2.x, o ya?

## Para la §6 de la SPEC (erratas del ES detectadas aquí)

- CF sobre las cabeceras internas (M5).
- Orden completo del cierre del 08 (M7) y carga antes de revisar el vehículo en la apertura (M6).
- Calendario: Comuniones antes del Día del Padre (M10).
- 09 «Después» B8, «no dentro de la factura», frente a D11, que mete las roturas en Extras (m5).

## Ronda 1: aplicado / no aplicado (18-oct-2026 · sesión Claude Code)

Todo en la fuente: `mapas_catering.py` (`REGLAS_US`, `POR_CELDA`, `GLOSARIO`, `CALENDARIO`, `CF_POR_CELDA`, ADAPTAR) y
`textos_en/G1.json` (23 cadenas reescritas, 5 cambios parciales, 11 ids que pasan a `POR_CELDA` retirados). Nada
parcheado en el xlsx. Construcción real VERDE 8/0, autotest 20/20.

| ID | Estado | Cómo |
|---|---|---|
| B1 | Aplicado | B16 (c0439) con la EN del informe; `REGLAS_US['tphc']` y el ADAPTAR `_TPHC` corregidos (servir DENTRO de las 4 h, descartar, sin volver al control; 6 h vigilando 70 °F) |
| M1 | Aplicado | 02 B26 (c0138), EN del informe |
| M2 | Aplicado | 04 B25 (c0261) y 05 B18 (c0366: «cool the hot food … and put the cold food straight back at 41 °F or below») |
| M3 | Aplicado | 01 B32 (c0052), EN del informe |
| M4 | Aplicado | 06 B9 (c0419) + consumer advisory 3-603.11 (ya en `REGLAS_US`) |
| M5 | Aplicado | `CF_POR_CELDA`: `AND($E6="✓",$B6<>"Task")` en las 15 hojas; `aplicar_en` la aplica, G1 la admite por nombre (resto de la CF = ES transformado); autotest: excepción revertida y otra CF alterada, CAZADAS. SPEC §1 D-CF + §6 |
| M6 | Aplicado | 08 Apertura: B/C de 9, 20, 21 y 22 rotados por `POR_CELDA` (D y E con su fila: la carga a las 7:30 AM) |
| M7 | Aplicado | 08 Cierre B5:D19 con la tabla del informe; la fila 5 dice qué hacer con la comida que vuelve (enfriar 3-501.14 o descartar) |
| M8 | Aplicado | 08 B13 (c0509) + C13 «Office»; 09 Before B6 (c0569); 06 Weddings B6 (c0388); `GLOSARIO` D-15 / D-7 / D-3 → «By N days out» (duda 4) y c0552 a juego |
| M9 | Aplicado | A3 «— set it first», A15, D15, A16, D16 por `POR_CELDA` (sin comillas: «Event Billing Log C3»); D3 (c0678) con la EN del informe |
| M10 | Aplicado | Filas 7-9: St. Patrick's · Easter & Passover · Comuniones; D y E por `POR_CELDA` |
| M11 | Aplicado | D7 (antes D8) = EN del informe |
| m1 | Aplicado | c0343 «within 2 h» |
| m2 | Aplicado | c0420 «crustacean shellfish»; ADAPTAR `_ALERGENOS` a juego |
| m3 | Aplicado | c0557 y c0279 con la EN del informe + dudas 2 (NY / MA) y 3 (FLSA: la celda habla de reparto de propinas); `REGLAS_US` nuevas `service_charge_aviso` y `propinas_supervisores` |
| m4 | Aplicado | c0619 |
| m5 | Aplicado | c0591 |
| m6 | Aplicado, adaptado | c0473 es la misma cadena en el 08 y el 09: «doesn't apply (to this event, or to your commissary)» |
| m7 | Aplicado | c0559 «… and the multiplier in its Subtotal formula.» |
| m8 | Aplicado | 08 Apertura B8 y B10 por `POR_CELDA` (eran heredadas del base); el cierre, en M7 |
| m9 | Aplicado | c0229 + `REGLAS_US['i9']` con 8 CFR 274a.2(b)(1)(ii) |
| m10 | Aplicado | c0184, c0710 y, de paso, c0062 («cold appetizers and canapés») |
| m11 | Aplicado | 03 A27 «During the Event», A38 «After the Event» por `POR_CELDA` (el «During the event» del 06 se queda en el glosario) |
| m12 | Aplicado | 01 B10 (c0009); 08 B16 por `POR_CELDA` (era heredada) |
| m13 | Aplicado | c0382 |
| m14 | Aplicado | B5 «Feb — …», C14 «Mixed», D12 (c0763), D22 (c0784) |
| m15 | Aplicado | c0304 |
| Duda 1 | Decidido | «Deposit» se queda |
| Duda 5 | Decidido | Calibración: sin cambios |
| Duda 6 | Aplicado | Filas 9 y 11: «First Communions … quinceaneras & bar/bat mitzvahs» (sin ñ: el gate de restos marca la eñe) |
| Duda 7 | Decidido | El ES no se toca hoy: M5, M6, M7, M10 y m5 en la §6 de la SPEC |
