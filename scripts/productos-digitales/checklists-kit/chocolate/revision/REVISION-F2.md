# Chocolate Shop Checklists Kit Pro — revisión adversarial de F2 (24-oct-2026 · sesión Claude Code)

Revisor único. Fuentes:
- `chocolate/revision/dump_en.txt` / `dump_es.txt`, 2.669 líneas cada uno, alineados por línea; «L» = línea del volcado
  (la misma en EN y ES);
- `chocolate/SPEC.md`, `chocolate/F2-NOTAS.md`, `chocolate/mapas_chocolate.py` (`ADAPTAR`, `CALENDARIO`, `REGLAS_US`,
  `GRADOS_F_SPEC`) y `../mapas.py` (`REGLAS_US` del base);
- el formato y las lecciones de `icecream/revision/REVISION-F2.md`, y `grep` de los volcados de los hermanos.

Solo lectura y `grep` de los volcados; sin openpyxl. Comprobaciones en la web:
- FDA Food Code 2022: resumen de cambios de la FDA (3-602.12(C), aviso escrito de alérgenos de lo no envasado;
  2-103.11(O), conocimiento de alérgenos del personal); 3-501.19 (time as a public health control: 4 h, o 6 h sin pasar
  de 70 °F, con procedimiento escrito), en las guías de Florida (FDACS), Tennessee y Bethlehem (PA);
- ganache y TCS: la ganache sencilla de nata suele dar aw ≈ 0,86-0,90, por encima de los umbrales habituales (0,85
  cottage food; < 0,88 en la tabla B de 1-201.10). Los inspectores piden análisis de laboratorio (foros de chocolateros
  y guías de cottage food);
- FDA, «Survey of Milk in Dark Chocolate Products» (2015): 94 tabletas; leche detectada en 55 de las 93 sin leche
  declarada, y en 2 de 17 «dairy free»;
- alcohol en confitería: 21 U.S.C. 342(d) (FD&C Act §402(d)). Por encima del 0,5 % que aportan los extractos, la
  confitería está adulterada salvo que la ley del estado donde se vende la permita. NY Agriculture & Markets Law §200: del
  0,5 % al 5 %, sin venta a menores de 21 y con advertencias. NC G.S. 106-129: hasta el 5 % con etiqueta;
- Mothering Sunday = 3 semanas antes de Pascua: del 1 de marzo al 4 de abril. Pascua de 2027: 28 de marzo;
- Reglamento (UE) 1169/2011 arts. 9, 24 y 44, y RD 126/2015 (para las erratas del ES).

## Veredicto

**Hay 1 BLOQUEANTE y 3 MAYORES; además, 21 menores.** Fuera de la EN hay **3 ERRATAS ES**, una de ellas de seguridad
(alérgenos).

**El BLOQUEANTE (B1)** es una contradicción sanitaria que la EN hace explícita. El kit declara TCS la ganache de nata
fresca: 41 °F o menos, 7 días, FDA. A la vez, manda exponer los bombones y las trufas en la vitrina a 60–64 °F todo el
día y guardarlos de noche en la cool room a 59–64 °F. Y las trufas «con nata o mantequilla» cuentan como ganache
fresca. Un inspector que aplique la propia clasificación del kit pone una infracción de mantenimiento en frío
(priority item).

**Lo que se pedía mirar y está bien:**
- **Curvas de templado.** Las conversiones son exactas:
  - dark: 50-55 → 27-28 → 31-32 °C = 122–131 → 81–82 → 88–90 °F;
  - milk: 113–122 → 79–81 → 84–86 °F;
  - white: 104–113 → 77–79 → 82–84 °F.

  Están dentro de lo que publican los fabricantes; el negro coincide con la tabla de Valrhona. El test a 64–68 °F es
  correcto. Lo que falta es presentarlas como típicas en las celdas (m1).
- **Date marking.** «7-day date mark at 41 °F or below, production day = day 1 (FDA 3-501.17)» es correcto (02 B31,
  03 «Weekly» B14). Es correcto también que no haya enfriado, recalentado ni mantenimiento en caliente.
- **Mano desnuda y muestras.** §3-301.11 en las muestras (01 B29, 04 B8), en las cajas (04 B15) y en el lavado de
  manos (01 B8).
- **Etiqueta y aviso de alérgenos.** La etiqueta de lo envasado (02 B25, 04 B12, 06 «Easter» B17) trae los elementos
  de §3-602.11(B). Lote y best-by quedan fuera de la cita, como criterio del kit. No hay obligaciones federales
  inventadas, que era la lección de la heladería. El aviso escrito de la vitrina va como §3-602.12(C) «where adopted».
- **c0204 (03 «Daily» B25, «2 years»): NO es un error.** Son las tarjetas de fichaje, y 29 CFR 516.6 pide 2 años. Las
  nóminas a 3 años ya están en el 03 «Monthly» B16, con NY 6.
- **Normativa de mantenimiento y licencias:**
  - extintores: OSHA 1910.157(e)(2) mensual y (f) hidrostática;
  - EPA 608 y NFPA 96 solo con grasa;
  - CFPM 2-102.12;
  - candy y sales tax;
  - licencia estatal de fabricación «if your state requires one».
- **Gas (D10).** El protocolo por olor a gas (01 B12) y «the main valve is for emergencies only» (01 «Closing» B25)
  son correctos.
- **08 «Shop Closing» reordenado.** Clientes → música → patio → señalización → vitrinas con el género ya guardado y
  temperatura del obrador → POS → papeleras → seguridad → ventanas → HVAC → luces → alarma → persiana → llave.
- **Calendario B02.** Las fechas son correctas:
  - Valentine's, con fecha límite el 10;
  - Mother's Day, el 2.º domingo, y Teacher Appreciation Week;
  - Father's Day, el 3.er domingo; Labor Day; Thanksgiving, el 4.º jueves;
  - National Chocolate Day, el 28 de octubre;
  - chocolate turkeys, Small Business Saturday y Hanukkah gelt;
  - Hot Chocolate en enero;
  - el shipping cutoff en febrero, julio, agosto y diciembre.

  No quedan restos de España: sin Reyes, turrón, monas, comuniones, panellets, IVA, kg, € ni °C (grep).
- **c0477 (06 «Easter» B15) no repite B9.** B9 planifica y B15 produce, como en el ES. Lo que falla es el contenido
  frente al ADAPTAR (m10).
- **Horas +2 h (D9).** 9:00-9:30 en el 08 y 9:15-9:45 en el 09, con la tienda abierta a las 10 AM: es realista.

**Los 3 MAYORES:**
- **M1.** Ni una tarea de **contacto cruzado de alérgenos**: inclusiones de frutos secos y cacahuete, praliné y
  gianduja, la temperadora compartida entre leche y negro, y las pinzas de la zona de muestras. En una chocolatería es
  el riesgo número uno.
- **M2.** «Does NOT handle food: tell the shift lead and **reassign the task**». Con vómitos, diarrea o ictericia, el
  Food Code pide **exclusión**, no reasignar a la caja o al envasado.
- **M3.** c0442: «Make artisan bark and toffee: praline, nut brittle, truffle» no tiene sentido. Es el calco de
  «turrones: praliné, guirlache, trufa».

**Cómo se corrige.** Todo con texto por celda (`POR_CELDA` / G1), sin filas nuevas. Hacen falta tres cambios en
`REGLAS_US`:
- `tcs_ganache`: «y pH» (tablas A y B) y «no en la vitrina de 60–64 °F»;
- `enfermos`: + §2-201.12 (exclusión);
- `licor`: 21 U.S.C. 342(d), si se adopta m7.

`GRADOS_F_SPEC` no cambia: las correcciones solo usan 41, 59, 60, 64 y 68.

| # | Sev. | Dónde | Qué |
|---|---|---|---|
| B1 | BLOQUEANTE | 02 «Molding & Bars» C41/D41 (L462-463), D44 (L472), B12-B13 (L383-386) · 01 «Opening» B25 (L95) · 01 «Closing» B6 (L157) · 01 «Instructions» B16 (L19) · 04 «Sales Associate» B29 (L965) | Ganache fresca declarada TCS (41 °F) pero expuesta y guardada a 59–64 °F |
| M1 | MAYOR | 02 «Molding & Bars» B21 (L409) · 04 «Chocolatier» B24 (L866) · 01 «Opening» B29 (L107) · 04 «Sales Associate» B8 (L905) | Sin control del contacto cruzado de alérgenos |
| M2 | MAYOR | 01 «Opening» B10 (L49), c0033 | «Reassign the task» con vómitos, diarrea o ictericia (debe ser exclusión) |
| M3 | MAYOR | 06 «Holiday Season» B15 (L1406), c0442 | «Bark and toffee: praline, nut brittle, truffle» |
| m1 | menor | 02 «Tempering» A13/A21/A28 (L280, L303, L323) · 01 «Opening» B15 (L66) | Curvas y precalentado sin «typical / per the manufacturer» en las celdas |
| m2 | menor | 02 «Tempering» B7 (L266) | Cobertura con leche «35–40% cocoa» deja fuera la más común (33,6 %) |
| m3 | menor | 02 «Molding & Bars» B6/B19 (L365, L403), C10/C23 (L378, L416) | Moldes «a temperatura ambiente 68–72 °F» con el obrador a 64–68; enfriar a 54–57 °F «en la Cool room» (59–64) |
| m4 | menor | 01 «Instructions» B17 (L20) · 01 «Opening» B20 (L81) · 08 «Shop Closing» B15 (L1875) | «Above 68 °F cocoa butter starts to melt» con la tienda a 68–72 °F; «Turn off HVAC» de noche |
| m5 | menor | 02 «Molding & Bars» B12-B13 (L383-386) | Rellenar y tapar seguido: la ganache no cristaliza antes del capping |
| m6 | menor | 01 «Opening» B19 (L78) vs 08 «Shop Opening» B11/B20 (L1748, L1793) | La vitrina «holds» la temperatura (01) y se enciende al llegar (08) |
| m7 | menor | 02 «Molding & Bars» D45 (L475), c0185 | Licor: «check your state rules» sin el 0,5 %, sin el 21+ y sin el estado de destino de los envíos |
| m8 | menor | 02 D41/D42 (L463, L466), c0176 · 05 «Quarterly & Annual» B8/F8 (L1276-1278) | TCS «por aw» sin pH; análisis de las recetas nuevas «Semiannual» |
| m9 | menor | 06 «Holiday Season» B9 (L1389) | Personal de temporada sin nota de menores (FLSA) |
| m10 | menor | 06 «Easter» B15 (L1561), c0477 · B9 (L1544) | «Chocolate Easter baskets» frente al ADAPTAR (huevos grandes rellenos, centros de mesa) |
| m11 | menor | 01 «Opening» A23 (L86) | «Service setup» (jerga de restaurante) |
| m12 | menor | 06 «Instructions» B6 (L1356) | Promete «Mother's Day and more» y el fichero no tiene esa hoja |
| m13 | menor | 05 «Quarterly & Annual» B9 (L1280) | «Food handler cards for all staff»: solo en algunos estados |
| m14 | menor | 05 «Instructions» B14 (L1066) · 05 «Quarterly & Annual» B14 (L1296) | Bombo (panning machine) y «auger» dados por hecho |
| m15 | menor | 05 «Weekly Tasks» B34 (L1165) | Báscula «sealed by your state weights and measures office»: a menudo es la oficina del condado o de la ciudad |
| m16 | menor | 01 «Closing» B25 (L212) · 08 «Shop Closing» B13 (L1865) | «Water off» (patrón de los hermanos; m9 de la heladería) |
| m17 | menor | BONUS-02 marzo B7 (L2629) · abril B8 (L2633) | Pascua de 2027 = 28 de marzo; «graduation season starts» en abril |
| m18 | menor | BONUS-02 mayo B9 (L2637), c0729 | «Pre-orders closed 2 weeks out» para Mother's Day |
| m19 | menor | BONUS-02 «Instructions» B7 (L2606), c0708 | Mothering Sunday «(March)» |
| m20 | menor | BONUS-02 octubre B14 (L2657) | Sweetest Day sin fecha ni región; orden no cronológico |
| m21 | menor | 08 «Shop Closing» B13 (L1865) · 01 «Closing» B14 (L180) | «Small appliances unplugged» sin excluir la temperadora o el melter si se deja encendido |

---

## BLOQUEANTE

### B1 · La ganache de nata fresca es TCS para el kit, pero sus bombones y trufas viven a 59–64 °F

**Dónde:**
- 02 «Molding & Bars», tabla de vida útil:
  - B41/C41/D41 (L461-463): `Fresh-cream ganache bonbons` · `7 days at 41 °F` · `Treat it as TCS: 41 °F or below, 7 days max (FDA date marking)… Longer only with a lab water-activity test`;
  - D44 (L472): `Truffles and coated clusters… If they contain cream or butter, count them as fresh ganache`;
- 02 B31 (L438), c0159, y 03 «Weekly» B14 (L626), c0239: TCS con 7 días a 41 °F;
- frente a esto, la operativa:
  - 01 «Instructions» B16 (L19): `fillings and ganaches 41 °F or below, bonbon display case 60–64 °F`;
  - 01 «Opening» B25 (L95): `Set up the display case: bonbons, bars, molded figures, truffles` (a 60–64 °F, B19);
  - 01 «Closing» B6 (L157) y 04 «Sales Associate» B29 (L965): el género sale de la vitrina a la **cool room** (59–64 °F);
  - 02 B33 (L444): `Store finished product at 59–64 °F`;
  - 02 B12-B13 (L383-386): se rellena y se tapa sin paso de frío (véase m5: la cristalización de la ganache se hace a
    temperatura de obrador).

**Qué falla.**
- **Mantenimiento en frío.** El kit clasifica como TCS (FDA Food Code 1-201.10) los bombones de ganache de nata fresca
  y las trufas de nata, que en EE. UU. son casi todas las trufas. Lo TCS en frío se mantiene a **41 °F o menos**
  (§3-501.16(A)(2)). Ningún flujo del kit les da ese frío:
  - de día, vitrina a 60–64 °F;
  - de noche, cool room a 59–64 °F;
  - durante la producción, obrador a 64–68 °F.
- **El inspector usará las palabras del propio kit.** Si el negocio declara TCS su ganache, como pide el kit, tenerla
  en una vitrina a 62 °F es una infracción prioritaria, y el 7-day date mark no la arregla.
- **El riesgo es real.** Una ganache sencilla de nata da aw ≈ 0,86-0,90: TCS según la tabla B (< 0,88 no lo es).
  Pasar 7 días a 62 °F no es lo mismo que pasarlos a 41 °F.
- **Lo que hace el chocolatero US:** formular la ganache, más azúcar, glucosa, sorbitol o alcohol, y demostrar en
  laboratorio que **no** es TCS. Solo así puede exponerla a 60–64 °F. Si no, la tiene en una vitrina refrigerada a
  41 °F o la vende con *time as a public health control* (§3-501.19: 6 h sin pasar de 70 °F y descartar, con
  procedimiento escrito).
- **El kit menciona el análisis solo para alargar la vida útil.** En D41 dice «Longer only with a lab water-activity
  test», pero no dice que **sin** ese análisis el producto no puede ir a la vitrina templada.

**Norma o fuente:** FDA Food Code 2022 §1-201.10 (TCS food, tablas A y B), §3-501.16(A)(2) y §3-501.19.

**Corrección EN.** Solo texto, y sin °F nuevos.
- 02 D41:
  `Treat it as TCS until a lab test (water activity and pH; FDA 1-201.10) shows it is not: 41 °F or below, 7 days max (date marking), so NOT in the 60–64 °F display case or the cool room — use a refrigerated case or the fridge. Let the box warm up CLOSED before opening, or it sweats`
- 02 D44:
  `Fresh-cream truffles follow the fresh-cream row (TCS unless lab-tested); butter-only or nut centers, this row`
- 01 «Opening» B25:
  `Set up the display case: bonbons, bars, molded figures, truffles — fresh-cream (TCS) items only if lab-tested as non-TCS; otherwise in a refrigerated case at 41 °F or below (table in file 02)`
- 01 «Closing» B6:
  `Take product out of the display case: bonbons and bars to the cool room; any TCS fresh-cream item to the fridge (41 °F or below)`
- 01 «Instructions» B16, al final:
  `Fresh-cream ganache is TCS unless a lab test says otherwise: it does not go in the 60–64 °F case.`
- `REGLAS_US['tcs_ganache']`: «aw y pH»; «sin el análisis, nunca en la vitrina ni en la cool room».
- Si se quiere ofrecer TPHC: añadir §3-501.19 a `REGLAS_US`. Exige el 70 °F en `GRADOS_F_SPEC`, así que **no lo
  recomiendo**: basta con la vitrina refrigerada o el análisis.

**ERRATA ES** con la misma raíz: véase ERRATA ES 1.

---

## MAYORES

### M1 · Ni una tarea de contacto cruzado de alérgenos

**Dónde:** el kit solo dice «may contain» en el cartel:
- 01 B26 (L98) y 04 B7 (L902);
- `_VITRINA`: «“Trazas” → “may contain” (contacto cruzado en líneas compartidas)».

Las tareas donde se crea el contacto cruzado no dicen nada:
- 02 «Molding & Bars» B21 (L409): `Add inclusions if needed: nuts, dried fruit, salt`;
- 04 «Chocolatier» B8 / B24 (L820, L866): `Temper couverture by type (dark/milk/white)` y `Clean the tempering machine after every use`;
- 01 «Opening» B29 (L107) y 04 «Sales Associate» B8 (L905): zona de muestras con pinzas;
- 04 B15 (L925): cajas surtidas montadas a mano;
- 06 «Holiday Season» B15: praliné y brittle.

**Qué falla.**
- **El riesgo número uno de una chocolatería es el alérgeno que no se ve.** Por ejemplo:
  - leche en el chocolate negro, cuando la temperadora o los moldes vienen de la leche. En la encuesta de la FDA de
    2015 se detectó leche en 55 de 93 tabletas negras sin leche declarada, y en 2 de 17 «dairy free»;
  - frutos secos y cacahuete del praliné y de las inclusiones, que pasan a las tabletas lisas;
  - las mismas pinzas para la muestra de gianduja y para la de trufa negra.
- **El kit pide un «may contain» veraz sin dar el control que lo hace veraz.** Tampoco pide formar al personal en
  alérgenos (Food Code 2022, 2-103.11(O)).
- **Es justo la lección de la heladería** (M3, el cacahuete y el scoop). Aquí ni siquiera hay una tarea.

**Corrección EN.** Solo texto en celdas existentes:
- 02 B21:
  `Add inclusions if needed: nuts, dried fruit, salt — run nut and peanut bars LAST, then clean molds, tools and the tempering machine before plain bars (allergen cross-contact)`
- 04 «Chocolatier» B24:
  `Clean the tempering machine after every use, and always before switching from milk to dark or white: milk carried over into dark chocolate is an undeclared allergen`
- 01 «Opening» B29 / 04 «Sales Associate» B8, añadir:
  `…one set of tongs per tray (nut and peanut items never share tongs)`.
- 04 «Sales Associate» B15, añadir:
  `…with gloves or tongs; for an allergy request, fresh gloves and pieces from untouched trays`.
- `REGLAS_US`: basta con `precautorio`. Si se cita la formación, añadir 2-103.11(O).

### M2 · «Reassign the task» en lugar de excluir

**Dónde:** 01 «Opening» B10 (L49), c0033:
`Anyone with vomiting, diarrhea, jaundice, sore throat with fever or an infected wound does NOT handle food: tell the shift lead and reassign the task (FDA 2-201.11)`.

**Qué falla.**
- **Viene del ES, y la EN lo deja más lejos del Food Code que los hermanos.** El ES dice «reasignar tarea»; los ocho
  hermanos dicen solo «no food handling».
- **Con vómitos o diarrea**, §2-201.12(A) pide **excluir**: la persona no trabaja ni entra en el establecimiento como
  empleado. Reasignarla a la caja, al envasado de cajas o a montar regalos la deja en contacto con producto y clientes.
  El norovirus es la primera causa de brotes en retail.
- **La ictericia** exige exclusión y aviso a la autoridad sanitaria (§2-201.11(B) / 2-201.12(B)).
- **Restringir** (reasignar) solo vale para el dolor de garganta con fiebre y para la herida infectada sin cubrir. B9
  ya lo cubre con apósito y guante.
- **Es la primera hoja del kit**, y la usará cada mañana quien abre.

**Corrección EN:**
`Vomiting, diarrhea or jaundice: that person does NOT work today — send them home (exclusion) and the person in charge reports jaundice or a diagnosed illness to the health department; sore throat with fever or an uncovered infected wound: no work with unwrapped food (FDA 2-201.11, 2-201.12)`
- `REGLAS_US['enfermos']`: añadir §2-201.12.

**ERRATA ES:** véase ERRATA ES 3.

### M3 · c0442, la línea de turrones mal calcada

**Dónde:** 06 «Holiday Season» B15 (L1406): `Make artisan bark and toffee: praline, nut brittle, truffle`.
ES: `Producir turrones artesanales: praliné, guirlache, trufa` (tres variedades de turrón).

**Qué falla.**
- **Se leen como tipos de bark y toffee cosas que no lo son.** «Truffle» no es un bark ni un toffee, el «nut brittle»
  no es un toffee y «praline» en EE. UU. es otra cosa.
- **Un chocolatero lo ve a la primera.** Está en la hoja de la campaña que más factura.
- **Falta el producto estrella de la temporada.** El ADAPTAR pedía «bark, toffee, brittle (el guirlache) y trufas», y
  el C16 del B02 ya trae el peppermint bark.

**Corrección EN:**
`Make holiday bark, toffee and brittle: peppermint bark, chocolate-dipped English toffee, nut brittle`

---

## Menores

- **m1 · Curvas presentadas como órdenes (02 «Tempering» A13/A21/A28, L280/L303/L323; 01 «Opening» B15, L66).**
  - **Qué falla:** «per the manufacturer's curve» solo está en «Instructions» B11 (L241). Las celdas dicen «Melt to
    122–131 °F», sin matiz. El `_CURVA` del ADAPTAR (cifras del kit; manda la curva del fabricante) se perdió en las
    celdas.
  - **Por qué importa:** quien trabaja con Callebaut lee 45-50 °C (113–122 °F) para fundir el negro, y con Guittard
    lee «no pasar de 120 °F». El 01 B15 pone «preheat to 113 °F» sin «per the manufacturer», y el ADAPTAR sí lo pedía.
  - **Corrección:**
    - cabeceras: `Tempering Process — Dark Chocolate (typical curve; your couverture's chart rules)` (ídem Milk y White);
    - 01 B15: `Turn on the tempering machine and preheat per the manufacturer (typically 113 °F)`.
- **m2 · 02 «Tempering» B7 (L266).**
  - **Qué falla:** `milk couverture stock (35–40% cocoa)`. La cobertura con leche más usada en EE. UU. (Callebaut 823)
    tiene 33,6 %, y muchas están entre el 30 y el 34 %.
  - **Corrección:** `(30–40% cocoa)`.
  - **ES:** igual (35-40 %).
- **m3 · 02 «Molding & Bars» B6 / B19 (L365, L403) y C10 / C23 (L378, L416).**
  - **Qué falla (temperatura de los moldes):** «at room temperature (68–72 °F)» con el obrador a 64–68 °F (B9 del
    «Tempering»): a temperatura ambiente, los moldes estarán a 64–68 °F.
  - **Qué falla (zona del enfriado):** «Chill at 54–57 °F» con zona «Cool room», que el kit mantiene a 59–64 °F. Ahí
    no se puede enfriar a 54–57 °F.
  - **Corrección:**
    - B6: `Prep clean molds, slightly warmer than the room (68–72 °F)`;
    - C10, C14 y C23: `Fridge`, o el texto `in a cooling cabinet or fridge set to 54–57 °F`.
  - **ES:** la misma incoherencia (moldes a 20-22 °C con el obrador a 18-20 °C; 12-14 °C «en cámara de conservación»
    a 15-18 °C).
- **m4 · 01 «Instructions» B17 (L20), 01 «Opening» B20 (L81) y 08 «Shop Closing» B15 (L1875).**
  - **Qué falla (B17):** «Above 68 °F cocoa butter starts to melt». El chocolate templado (forma V) funde hacia
    93 °F; lo que sube por encima de ~68 °F es el riesgo de ablandamiento y de bloom.
  - **Qué falla (tienda):** el propio kit pone la tienda a 68–72 °F. Y el 08 B15 dice «Turn off HVAC or set it to
    night mode», cuando las tabletas envueltas de las estanterías se quedan siempre fuera de la cool room.
  - **Corrección:**
    - B17: `Above 68 °F chocolate softens and bloom risk climbs: …`;
    - 01 B20: `Turn on the A/C — keep the shop at 68–72 °F (unwrapped bonbons stay in the 60–64 °F case)`;
    - 08 B15: `Set HVAC to night mode — never fully off in warm weather: wrapped bars on the shelves need the shop at 68 °F or below overnight`.
- **m5 · 02 «Molding & Bars» B12-B13 (L383-386).**
  - **Qué falla:** `Fill bonbons to 80%…` y, a continuación, `Cap with tempered chocolate`. La ganache tiene que
    cristalizar antes de tapar, normalmente de 12 a 24 h a temperatura de obrador. Si no, la tapa no sella y el
    bombón suda.
  - **Corrección:** B12 `Fill bonbons to 80%, leaving room for the cap; let the filling set before capping (ganache: usually overnight — if it is TCS, in the fridge)`.
  - **Relación con B1:** cuadra con lo propuesto allí.
  - **ES:** igual.
- **m6 · 01 «Opening» B19 (L78) frente a 08 «Shop Opening» B11 / B20 (L1748, L1793).**
  - **Qué falla:** el 01 dice que la vitrina «holds 60–64 °F», como si hubiera estado encendida toda la noche. El 08
    la enciende al llegar (B11, 9:15) y la comprueba a las 9:30. El 08 «Closing» B9 la apaga.
  - **Corrección (01 B19):** `Check the bonbon display case has reached 60–64 °F (switched on at arrival, file 08) and is not fogging up before setting out product…`.
- **m7 · 02 D45 (L475), c0185.**
  - **Qué falla:** «Alcohol-filled candy: check your state rules» va en la buena dirección (21 U.S.C. 342(d) remite a
    la ley del estado), pero no da el dato que necesita el comprador: por encima del 0,5 %, la confitería solo es legal
    donde el estado lo permite. Unos estados exigen además venta a mayores de 21 y advertencias (NY: hasta el 5 %).
    Y la tienda **envía** a otros estados (06, B02).
  - **Corrección:** `Over 0.5% alcohol, candy is legal only where state law allows it (FD&C Act 402(d)): check your state's limit, any 21+ or warning-label rule, and the destination state before shipping`.
  - **Gates:** `REGLAS_US['licor']` + «21 U.S.C. 342(d)».
- **m8 · 02 D41 / D42 (L463, L466), c0176 · 05 «Quarterly & Annual» B8 / F8 (L1276-1278).**
  - **Qué falla (aw sin pH):** «lab water-activity test». La definición TCS (1-201.10, tablas A y B) cruza aw y pH:
    entre 0,88 y 0,92, el pH decide.
  - **Qué falla (frecuencia):** el análisis de las recetas **nuevas** va con «Semiannual», y una receta nueva se analiza
    antes de venderla.
  - **Corrección:**
    - aw: «lab test of water activity and pH»;
    - 05 B8: `…water activity and pH of each new ganache or filling BEFORE it goes on sale, and again if the recipe changes…`;
    - F8: `Per new recipe`.
- **m9 · 06 «Holiday Season» B9 (L1389).**
  - **Qué falla:** `Plan extra production: shifts, seasonal staff`. La campaña de fiestas contrata estudiantes, y el
    kit no dice nada de menores. A los de 14-15 años la FLSA les limita las horas y les prohíbe manejar o limpiar
    máquinas eléctricas que no estén en la lista permitida: temperadora, bombo, enrobadora (29 CFR 570.33(e) y 570.34).
  - **Corrección:** `Plan extra production: shifts and seasonal staff (minors: FLSA hour limits; under 16, no operating or cleaning the tempering or panning machine; check state work permits)`.
  - **Gates:** `REGLAS_US`, regla `menores` (la de la heladería, con 570.33(e)).
- **m10 · 06 «Easter» B15 (L1561), c0477.**
  - **Qué falla:** `Make decorated chocolate Easter baskets`. El ADAPTAR pedía huevos grandes decorados y rellenos o
    centros de mesa. En EE. UU., una «Easter basket» es una cesta rellena de dulces; la cesta hecha de chocolate es un
    nicho. B9 (planificar) y B15 (producir) no se repiten.
  - **Corrección:**
    - B15: `Make large decorated and filled eggs and chocolate centerpieces; assemble filled Easter baskets`;
    - B9: `Plan filled Easter basket orders and showpiece eggs, if you offer them`.
- **m11 · 01 «Opening» A23 (L86).**
  - **Qué falla:** «Service setup» es jerga de restaurante (heredado). El 01 «Instructions» B6 ya dice «shop setup».
  - **Corrección:** `Shop and display setup`.
- **m12 · 06 «Instructions» B6 (L1356).**
  - **Qué falla:** `Holiday Season, Valentine's Day, Easter, Mother's Day and more`. El fichero tiene tres hojas y no hay
    ninguna de Mother's Day.
  - **Corrección:** `Holiday Season, Valentine's Day and Easter (Mother's Day and the rest of the year: BONUS 02 calendar)`.
- **m13 · 05 «Quarterly & Annual» B9 (L1280).**
  - **Qué falla:** `Food handler cards for all staff`. Solo las exigen algunos estados o condados (CA, TX, IL, WA, OR,
    FL, AZ por condado…). El ADAPTAR decía «según el estado».
  - **Corrección:** `Food handler cards where your state or county requires them (renewals on its schedule) and a certified food protection manager on the team (FDA Food Code 2-102.12)`.
- **m14 · 05 «Instructions» B14 (L1066) · 05 «Quarterly & Annual» B14 (L1296).**
  - **Qué falla:** el bombo (panning machine) y el desgaste del «auger» se dan por hecho. Muchas chocolaterías
    pequeñas no tienen bombo, y las temperadoras de sobremesa no tienen tornillo.
  - **Corrección (B14):** `Technician service on the tempering machine (and panning machine, if you have one): probes, heating elements, gaskets and, on continuous machines, auger wear`.
- **m15 · 05 «Weekly Tasks» B34 (L1165).**
  - **Qué falla:** «inspected and sealed by your state weights and measures office». En muchos estados inspecciona y
    precinta el condado o la ciudad (sealers de condado en CA y NY, por ejemplo).
  - **Corrección:** `…by your state or local (county/city) weights and measures office`.
- **m16 · 01 «Closing» B25 (L212) · 08 «Shop Closing» B13 (L1865).**
  - **Qué falla:** «water off» es ambiguo: no se cierra la llave general del agua cada noche. Es el m9 de la heladería.
  - **Corrección:** `no taps left running`.
- **m17 · BONUS-02 marzo B7 (L2629) y abril B8 (L2633).**
  - **Qué falla (marzo):** la primera Pascua que gestionará el comprador (2027) cae el **28 de marzo**, y el kit pone
    en marzo solo «Easter prep».
  - **Qué falla (abril):** «graduation season starts (Apr–Jun)». En EE. UU. las graduaciones son en mayo y junio; en
    abril empiezan los **encargos**. El ADAPTAR proponía bodas y baby showers de primavera.
  - **Corrección:**
    - marzo: `…Easter prep (Easter itself falls in March some years: 2027, March 28)…`;
    - abril: `…graduation and spring wedding orders open (ceremonies May–June): favors and custom boxes`.
- **m18 · BONUS-02 mayo B9 (L2637), c0729.**
  - **Qué falla:** `pre-orders closed 2 weeks out`. Cerrar los encargos de Mother's Day dos semanas antes pierde el
    grueso de la demanda, que llega la última semana. Además choca con el día 10 de Valentine's, a 4 días.
  - **Origen:** viene del ADAPTAR y es el mismo patrón de la heladería.
  - **Corrección:** `pre-orders open 2–3 weeks out, order deadline a few days before`.
- **m19 · BONUS-02 «Instructions» B7 (L2606), c0708.**
  - **Qué falla:** `Mothering Sunday (March)`. Cae del 1 de marzo al 4 de abril; en 2038 es el 4 de abril. Viene del
    ADAPTAR.
  - **Corrección:** `Mothering Sunday (3 weeks before Easter: March or early April)`.
- **m20 · BONUS-02 octubre B14 (L2657).**
  - **Qué falla:** «Sweetest Day» va sin fecha y sin la nota «sobre todo en el Medio Oeste» que traía el CALENDARIO.
    Además, el orden no es cronológico.
  - **Corrección:** `Sweetest Day (3rd Saturday, mainly Midwest) · National Chocolate Day (28) · Halloween (31): seasonal figures and bonbons · holiday production ramps up · publish the holiday catalog`.
- **m21 · 08 «Shop Closing» B13 (L1865) · 01 «Closing» B14 (L180).**
  - **Qué falla:** «small appliances unplugged — never the cool room or the fridges». No excluye los melters o la
    temperadora que algunas tiendas dejan encendidos de noche con chocolate dentro. El 01 B14 los limpia a diario, y es
    coherente si el equipo se vacía; si no, alguien la desenchufa con 10 lb dentro.
  - **Corrección:** `…— never the cool room, the fridges or a melter kept on overnight`.

---

## ERRATAS ES (kit LIVE `kit-tareas-chocolateria`, para su próxima v2.x)

1. **Seguridad · la ganache fresca, refrigerada en la tabla y expuesta en la operativa.**
   - **La tabla:** 02 «Moldeado» D41 (L463) dice `Actividad de agua alta: en refrigeración a 0-4 °C`, y D44 (L472),
     `Si llevan nata o mantequilla, se cuentan como ganache fresca`.
   - **La operativa:** el 01 «Apertura» B25 monta bombones y trufas en la vitrina a 16-18 °C, y el 01 «Cierre» B6 los
     guarda en conservación a 15-18 °C. Es la misma raíz que B1.
   - **La etiqueta:** con 10-15 días y la necesidad de frío, el 02 B31 (L438) los etiqueta con «consumo preferente».
     Si de verdad son microbiológicamente muy perecederos, el Reglamento (UE) 1169/2011 art. 24 pide «fecha de
     caducidad».
   - **Arreglo:** decir dónde se exponen los de nata fresca (vitrina refrigerada, o formular o analizar la aw) y usar
     «fecha de caducidad» en ese caso.
2. **Seguridad (alérgenos) · tabletas envueltas sin alérgenos.**
   - **Qué dice:** 02 «Moldeado» B25 (L421) `Envolver en papel/aluminio y etiquetar con lote y fecha`, con
     inclusiones de frutos secos dos filas antes (B21).
   - **Qué falla:** lo envasado por el propio comercio lleva siempre los alérgenos destacados (Reglamento (UE)
     1169/2011 arts. 9 y 21; RD 126/2015). El 04 «Chocolatero» B12 se queda en «Envasar y etiquetar». El ES de Pascua
     (06 B17) sí lo hace bien.
   - **Arreglo:** `Envolver y etiquetar: denominación, ingredientes con los alérgenos destacados, peso neto, lote y consumo preferente`.
3. **Higiene · «reasignar tarea» a quien tiene diarrea.**
   - **Qué dice:** 01 «Apertura» B10 (L49) `…NO manipula producto: comunicarlo al encargado y reasignar tarea`.
   - **Qué falla:** el Reglamento (CE) 852/2004, anexo II, cap. VIII.2, prohíbe a quien padece diarrea o tiene heridas
     infectadas manipular alimentos **o entrar en cualquier zona de manipulación** si hay probabilidad de
     contaminación. Reasignarle al mostrador de bombones a granel no lo cumple.
   - **Arreglo:** `…no entra en obrador ni mostrador: comunicarlo al encargado`.

Además, del ES, sin ser de seguridad: m2 (% de la cobertura con leche), m3 (moldes a 20-22 °C con el obrador a
18-20 °C; 12-14 °C «en conservación») y m5 (tapar sin dejar cristalizar).

---

## Dudas (no son errores claros)

1. **Temperadora precalentada a 113 °F con el negro fundido a 122–131 °F (01 B15 frente a 02 B15).** No es
   contradictorio: el precalentado del baño no es la consigna de fusión. Pero quien lea las dos celdas puede dudar, y m1
   lo cubre con «per the manufacturer».
2. **Vitrina encendida a las 9:15 y en rango, humedad incluida, a las 9:30 (08 B11 → B20).** 15 minutos bastan para
   la temperatura en una vitrina pequeña; para la humedad < 55 %, no siempre. Viene del ES (07:15 → 07:30).
3. **Señales de los encargos en efectivo (09 «Cash Drawer Closing» B15).** «Not the day's sales», pero el resumen no
   tiene línea para restarlas. Si entran en el cajón y no se marcan en el POS, el over/short sale en positivo. Habría que
   decir «ring deposits on the POS as a deposit tender» o restarlos. Es el 09 propio del kit (D12).
4. **Longitud del 01 B26 y del 04 B7.** Unos 330 caracteres con la lista de los 9. Caben con alto automático (F2-NOTAS),
   pero se podrían acortar: «the major allergens each item contains (the 9 are listed in "Instructions")». Fish y
   shellfish van solo como parte de la definición, y es correcto.
5. **Catálogo de fiestas.** Se diseña en octubre (06 A4/B6), pero los pedidos corporativos se abren en septiembre
   (B02). Viene así del ES; se puede adelantar el diseño a septiembre.
6. **Etiqueta nutricional.** No la pido: la venta del propio fabricante suele estar exenta (21 CFR 101.9(j)) y el kit no
   afirma nada al respecto.
7. **Food cost 30–35 % (03 «Weekly» B32).** Es plausible si se cuentan materia prima y packaging; está declarado como
   criterio del kit (`plazos_kit`).
8. **08 «Shop Opening» B8 (9:00 AM, «Raise security gate and open front door»).** El público entra a las 10. Es el
   texto del base, aceptado en los hermanos.
