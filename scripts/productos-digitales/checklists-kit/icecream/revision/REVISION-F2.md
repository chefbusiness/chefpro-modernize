# Ice Cream Shop Checklists Kit Pro — revisión adversarial de F2 (24-oct-2026 · sesión Claude Code)

Revisor único. Fuentes:
- `icecream/revision/dump_en.txt` / `dump_es.txt`, 2.510 líneas cada uno, alineados por línea; «L» = línea del volcado EN;
- `icecream/SPEC.md`, `icecream/F2-NOTAS.md`, `icecream/mapas_icecream.py` (`REGLAS_US`, `GRADOS_F_SPEC`);
- el formato y las lecciones de `ghost/revision/REVISION-F2.md`, y `grep` de los volcados de los hermanos (cafetería,
  catering, pizzería, ghost) para ver qué patrones vienen heredados.

Solo lectura y `grep` de los volcados; sin openpyxl. Comprobaciones en la web:
- pasteurización de mezcla de frozen dessert por estado: Ohio Adm. Code 901:11-3-05 (tabla 155 °F/30 min · 175 °F/25 s ·
  180 °F/15 s…), N.J.A.C. 8:21-7.27 (batch 155/30, HTST 175/25 «u otra equivalente aceptada»), 77 Ill. Adm. Code 785,
  MCL 288.735 (Michigan: batch 155/30, enfriar a 45 °F, registrador con gráficas 180 días);
- Arizona: A.R.S. § 3-607 y HB 2178 (2019);
- FLSA, menores de 14-15 años: 29 CFR 570.33(e) (maquinaria eléctrica) y 570.33(i) (trabajo en congeladores, salvo
  entradas momentáneas para coger algo);
- Food Code 3-602.11(B): elementos de la etiqueta de lo envasado en el local (guías de Pennsylvania y Peoria County);
- batch freezer: el manual de usuario de la GBF 10/20 («Do not run the machine without mixed liquid; otherwise it will
  damage the machine») y el de Stoelting (no funcionar en seco);
- dipping cabinets: no hay documentación de Master-Bilt de un «modo nocturno / conservación» (las vitrinas italianas de
  gelato sí lo traen; las US de tapa corredera, en general no).

## Veredicto

**Hay 1 BLOQUEANTE y 6 MAYORES; además, 14 menores.**

**El BLOQUEANTE (B1)** es una errata del ES que la EN ha traducido tal cual: grasas y emulsionantes (nata, mantequilla,
**yemas**) se añaden **después** de pasteurizar, «cuando la mezcla se enfría a 104–122 °F». Eso mete ingredientes crudos
en una mezcla ya pasteurizada.

**Lo que se pedía mirar y está bien:**
- **Dipper well.** §3-304.12(D) bien citado: agua corriente que arrastre a desagüe, para ice cream. El agua no quita
  alérgenos, y para una alergia hay scoop limpio y sanitizado.
- **Contacto y catas.** Sin contacto a mano desnuda (§3-301.11); se prueba con cuchara limpia cada vez (§3-301.12); las
  muestras van en tasting spoon de un solo uso.
- **La mezcla.** Enfriado 135 → 70 °F en 2 h y → 41 °F en 4 h más (§3-501.14); aging a 36–39 °F con techo de 41 °F;
  mezcla de 3-5 días dentro de los 7 del date marking (§3-501.17).
- **Normas de producto y laborales.** 21 CFR 135.110 (4,5 lb/galón) y «gelato has no federal standard», correctos.
  FLSA 516.2 / 516.5-6 (2 y 3 años, NY 6), correcto.
- **Mantenimiento y permisos.** El personal nunca toca el refrigerante (EPA 608). Extintores con OSHA 1910.157, y
  hidrostática con (f). CFPM con §2-102.12.
- **Calendario B02.** Cronológico y con fechas US correctas:
  - Mother's Day, el 2.º domingo de mayo; Memorial Day, el último lunes de mayo;
  - Father's Day, el 3.er domingo de junio; Juneteenth, el 19 de junio;
  - National Ice Cream Day, el 3.er domingo de julio;
  - Labor Day, el 1.er lunes de septiembre; Thanksgiving, el 4.º jueves de noviembre; Small Business Saturday;
  - temporada: Peak de junio a agosto, mayo en Shoulder con el pico arrancando el Memorial Day, y Low de octubre a
    febrero, coherente con el 06.
- **Horas +3 h.** Llegar a las 10:00 y abrir la puerta a las 11:00 es lo normal en una scoop shop US. El 09 cuadra con
  10:15-10:45.
- **El 08 «Shop Closing» reordenado (D10).** Clientes y música → patio y señalización → vitrinas → caja → papeleras y
  seguridad → local → alarma, persiana y llave.
- **c0332 (backflush).** Condicionado a «If you serve coffee», se puede quedar; véase m6 por la coletilla del
  lavavajillas.
- **185 °F 15 s.** Supera el 180 °F/15 s de la tabla de Ohio y lleva la remisión al programa validado y a la licencia
  (véase m2).
- **Etiquetas de fichero.** El 01 B27 trae los alérgenos US con cacahuete y sésamo.

**Los 6 MAYORES:**
- **M1.** Se da por hecho que toda dipping cabinet tiene un «storage mode» a 0 °F. Además, en el 08 se cambia a servicio
  y se comprueba la temperatura de servicio en el mismo minuto, 30 min antes de abrir.
- **M2.** «Run the batch freezer empty»: los fabricantes prohíben mantecar con el cilindro vacío.
- **M3.** El catering pierde el cacahuete en la lista de alérgenos. El ES dice «frutos secos», que en España incluye el
  cacahuete, y la EN lo traduce por «tree nuts».
- **M4.** Los pints preenvasados solo llevan «allergen label». §3-602.11 pide nombre, ingredientes, contenido neto,
  nombre y lugar del negocio y alérgenos.
- **M5.** A los menores de 14-15 años les falta lo propio de una heladería: no trabajar dentro del congelador
  (§570.33(i)) ni manejar o limpiar la mantecadora o el pasteurizador (§570.33(e)). Y «hire 2 weeks before».
- **M6.** El catering mide la temperatura a la llegada y luego nada: sin frío durante el servicio, sin dipper well in
  situ y sin «lo derretido se tira».

**Cómo se corrige.** Todo con texto por celda (`POR_CELDA` / G1), sin filas nuevas.
- **B1:** se intercambian los textos de B13 y B14 del 02 «Pasteurizing».
- **`REGLAS_US`:** hacen falta tres citas nuevas: 29 CFR 570.33(e)/(i) en `menores`, §3-304.12(A) en `dipper_well` y
  NFPA 96 Tabla 11.4 si se adopta m8.
- **`GRADOS_F_SPEC`:** no cambia, salvo que se acepte m2 (155 y 175 °F).
- **Después de corregir:** `ancho_texto` / `n_lineas` en las celdas que se alargan. Son el 06 B6, B7, B17, B18 y B28, el
  01 «Opening» B16 y B26, el 01 «Closing» B7, el 08 B9, B10 y B20, el 05 «Weekly Upkeep» B6 y el 02 B13-B14.

| # | Sev. | Dónde | Qué |
|---|---|---|---|
| B1 | BLOQUEANTE | 02 «Pasteurizing» B13 (L288) · B14 (L291) | Grasas y emulsionantes (yemas) añadidos DESPUÉS de pasteurizar |
| M1 | MAYOR | 01 «Instructions» B16 (L19) · 01 «Opening» B16 (L66) · 01 «Closing» B7 (L163) · 08 «Shop Opening» B20/E20, B21/E21 (L1660-1668) · 08 «Shop Closing» B9, B10 (L1717, L1722) | «Storage mode (0 °F)» universal; cambio y comprobación a la misma hora |
| M2 | MAYOR | 05 «Weekly Upkeep & Stock» B6 (L1034) | Mantecadora en vacío |
| M3 | MAYOR | 06 «Ice Cream Catering» B6 (L1383) · 01 «Opening» B26 (L95) · 01 «Instructions» B17 (L20) | Sin cacahuete (peanut butter, peanut butter cups) |
| M4 | MAYOR | 06 «Peak Season» B18 (L1300) · 05 «Monthly Tasks» B21 (L1130) | Etiqueta de los pints reducida a alérgenos |
| M5 | MAYOR | 06 «Peak Season» B7 (L1268) · 05 «Weekly Deep Clean» B21 (L1004) · BONUS-02 B8 (L2474) | Menores: congeladores y maquinaria; «2 weeks before» |
| M6 | MAYOR | 06 «Ice Cream Catering» B17 (L1415) · B21 (L1426) · B28 (L1446) | Sin frío ni scoops ni descarte durante el servicio |
| m1 | menor | 02 «Pasteurizing» B15 / C15 (L294-295) | «Blast freezer» y zona «Hardening» para enfriar mezcla líquida |
| m2 | menor | 02 «Pasteurizing» B13 (L288) | 185 °F 15 s sin los mínimos estatales habituales |
| m3 | menor | 02 «Instructions» B6 (L243) · 05 «Quarterly & Annual» B19 (L1204) | Arizona como ejemplo de licencia (exime desde 2019); B19 incoherente con B6 |
| m4 | menor | 02 «Batch Freezing» B24 (L396) · 05 «Weekly Deep Clean» B13 (L981) | «Remove … cylinder»: el cilindro no se desmonta |
| m5 | menor | 04 «Ice Cream Maker» B16 (L736) | Cubetas a la vitrina sin temperar |
| m6 | menor | 05 «Weekly Upkeep & Stock» B10 (L1046) · 05 «Quarterly & Annual» B15 (L1192) | Lavavajillas bajo «if you serve coffee»; espresso sin condición |
| m7 | menor | 05 «Quarterly & Annual» A4 (L1151) vs F6 (L1162) | Sección «quarterly & semiannual» con una tarea «Monthly» |
| m8 | menor | 05 «Quarterly & Annual» B7 / F7 (L1164-1166) | NFPA 96: semestral; una heladería de temporada es «low-volume» (anual) |
| m9 | menor | 08 «Shop Closing» B13 (L1737) · 01 «Opening» B12 (L55) | «Gas off, water off» y «open the main valve» |
| m10 | menor | 01 «Opening» B28 (L101) | «Milk caramel» por «dulce de leche» |
| m11 | menor | 03 «Weekly Tasks» B7 (L544) · 05 «Monthly Tasks» B14 (L1110) | «target <28–32%» |
| m12 | menor | BONUS-02 «Instructions» B16 (L2447) | Mothering Sunday «(March)» |
| m13 | menor | 03 «Weekly Tasks» B22 (L587) | «— log reading: ____ °F» en una revisión de caducidades |
| m14 | menor | 01 «Opening» B18 (L72) | «Above 41 °F the pasteurized mix is no longer safe» (absoluto) |

---

## BLOQUEANTE

### B1 · Grasas y emulsionantes añadidos DESPUÉS de pasteurizar

**Dónde:** 02 «Pasteurizing», sección «Pasteurizing and cooling»:
- B13 (L288): `Pasteurize at 185 °F for 15 seconds (high-temp); … — log reading: ____ °F`;
- B14 (L291): `Add fats and emulsifiers when the mix cools to 104–122 °F — log reading: ____ °F`.

ES B14: `Añadir grasas y emulsionantes al alcanzar 40-50 °C en descenso`.

**Qué falla.**
- **El orden es el contrario al correcto.** La secuencia dice: pasteurizar → enfriar → a 104–122 °F «en descenso»,
  añadir grasas y emulsionantes → seguir enfriando (B15).
- **Lo que entra después de la pasteurización entra crudo.** En una heladería US, «emulsifiers» son también las
  **yemas** de un helado tipo custard / French-style. Echar yemas sin pasteurizar a 104–122 °F a una mezcla que luego
  madura 3-5 días es un riesgo de *Salmonella*. Lo mismo con nata o leche en polvo añadidas tarde.
- **Choca con la licencia estatal.** Las normas estatales de frozen dessert definen la pasteurización como calentar
  **cada partícula de la mezcla** (N.J.A.C. 8:21-7.27; Ohio 901:11-3-05; Nevada NAC 584): lo que se añade después no
  está pasteurizado. El kit le dice al mismo lector, en el 02 «Instructions» B6, que pasteurizar su mezcla requiere esa
  licencia.
- **También falla la técnica.** Los mono y diglicéridos y los estabilizantes necesitan calor para dispersarse.
- **Lo correcto** es que el pasteurizador añada polvos y grasas **mientras sube** la temperatura (40-50 °C ≈ 104–122 °F
  en ascenso) y después mantenga la temperatura de pasteurización. Lo único que entra después son los sabores, los
  swirls y los mix-ins en la mantecadora, y eso el kit ya lo pone en «Batch Freezing» B14.

**Norma o fuente:** definiciones de pasteurización de N.J.A.C. 8:21-7.27 y Ohio Adm. Code 901:11-3-05 (todo el
producto a la temperatura y tiempo listados).

**Corrección EN.** Se intercambian las dos filas, sin filas nuevas, y G1 sigue en paridad.
- B13:
  `Add fats and emulsifiers (cream, butter, egg yolks, stabilizer blend) while the mix HEATS through 104–122 °F, before the pasteurizing hold: anything added after pasteurizing goes in raw — log reading: ____ °F`
- B14 = el texto actual de B13 (con lo que propone m2, si se acepta).

**Errata para el ES v2.x:** B14 «en descenso» → «en ascenso», y la fila va ANTES de «Pasteurizar a 85 °C…».

---

## MAYORES

### M1 · «Storage mode (0 °F)» dado por universal, y el 08 cambia y comprueba la vitrina a la misma hora

**Dónde:**
- 01 «Instructions» B16 (L19): `Dipping cabinets are NOT turned off at night: they go to storage mode.`;
- 01 «Opening» B16 (L66): `Switch the dipping cabinets from overnight storage (0 °F) to service mode (6–10 °F, per the manufacturer)…`;
- 01 «Closing» B7 (L163): `Switch the dipping cabinets to storage mode (0 °F): never turn them off…`;
- 08 «Shop Opening» B20 (L1660, «switched to service mode»), con E20 `10:30 AM`, y B21 (L1665, «at serving temp
  (6–10 °F)»), con E21 `10:30 AM`;
- 08 «Shop Closing» B9 (L1717): `…they stay ON, in storage mode`, y B10 (L1722): `dipping cabinets already in storage mode (0 °F)`.

**Qué falla.**
- **El modo nocturno es de las vitrinas italianas de gelato.** Lo traen las vitrinas con control electrónico y cortina
  (ISA, IFI, Orion…), que es la que tenía en mente el ES. La dipping cabinet típica de una scoop shop US, de tapa
  corredera o vidrio curvo (Master-Bilt, Kelvinator, Excellence), suele tener un solo termostato. Se queda encendida a
  temperatura de servicio, con las cubetas tapadas, o las cubetas pasan al congelador. No he encontrado documentación
  de un «storage mode» en esas marcas.
- **Con esas vitrinas, tres tareas no se pueden hacer.** «Switch to storage mode» al cierre, «switch from storage to
  service» al abrir y «confirm 0 °F».
- **El cierre pide una lectura imposible.** B10 pide anotar 0 °F «already in storage mode» justo después de cambiar el
  modo en B9, y la vitrina no habrá bajado de 6–10 °F a 0 °F en esos minutos.
- **El 08 cambia y comprueba a la vez.** Pasar a servicio (B20) y comprobar que ya está a 6–10 °F (B21) van los dos a
  las 10:30 AM, 30 min antes de abrir la puerta.
  - En el 01, ese paso es la PRIMERA tarea del equipo.
  - Una cubeta a 0 °F necesita tiempo para estar «scoopable».
  - Viene del ES (07:30 + 3 h), pero allí el 08 llevaba además «mantecadoras encendidas» (ya corregido, D10).

**Norma o fuente:** [fabricante]. El propio kit pone «per the manufacturer» en la temperatura de servicio, pero no en la
existencia del modo.

**Corrección EN.** Solo texto. Las horas no se tocan, así que el autotest de +3 h y del orden no cambia.
- 01 «Instructions» B16, última frase:
  `Dipping cabinets are NOT turned off at night: they stay on — on their night/storage setting if your model has one, per the manufacturer.`
- 01 «Opening» B16:
  `First thing: if your dipping cabinets have a night/storage setting, switch them back to service mode (6–10 °F, per the manufacturer), and confirm they held temperature all night — log reading: ____ °F`
- 01 «Closing» B7:
  `Leave the dipping cabinets ON (never turn them off with product inside: an overnight shutdown can ruin the whole batch); use the night/storage setting only if your model has one, per the manufacturer`
- 08 «Shop Opening» B20:
  `Dipping cabinets back in service mode — done FIRST THING on arrival (file 01, Opening tab), so the pans soften to scooping temp before the door opens; they stay on overnight with product inside`
- 08 «Shop Closing» B9:
  `Put the night covers or lids on the dipping cabinets: they stay ON (night/storage setting only if your model has one, per the manufacturer)`
- 08 «Shop Closing» B10:
  `Log the closing temps: dipping cabinets and freezers (0 °F or below) — log reading: ____ °F`

### M2 · «Run the batch freezer empty»

**Dónde:** 05 «Weekly Upkeep & Stock» B6 (L1034): `Run the batch freezer empty: check temperature and cycle — log reading: ____ °F`.
ES: `Test de mantecadora en vacío: verificar temperatura y ciclo`.

**Qué falla.**
- **Los fabricantes lo prohíben.** El manual de la GBF 10/20 dice «Do not run the machine without mixed liquid;
  otherwise it will damage the machine», y el de Stoelting dice que no se ponga a funcionar en seco.
- **El daño.** Con el cilindro vacío, el frío congela la pared en seco y las palas rascan metal contra metal.
- **El dato tampoco sirve.** La «temperatura» de un cilindro vacío no dice nada: la draw temperature se comprueba en la
  primera tanda.
- **La va a hacer quien abre.** Es una tarea semanal que un empleado ejecutará al pie de la letra.

**Corrección EN:**
`Batch freezer check per the manufacturer: scraper blades, beater and door gasket for wear, and the draw temperature on the day's first batch — never run a freezing cycle with the cylinder empty — log reading: ____ °F`

**Errata para el ES v2.x:** «Test de mantecadora en vacío».

### M3 · El catering no nombra el cacahuete

**Dónde:**
- 06 «Ice Cream Catering» B6 (L1383): `…an ice cream menu concentrates MILK, TREE NUTS, EGG, WHEAT (cones, wafers, cookies), SOY and SESAME (9 major allergens; UK: 14)`;
- 01 «Opening» B26 (L95): `…tree nuts (pistachio, hazelnut, almond) travel from pan to pan on the scoop`;
- 01 «Instructions» B17 (L20): `…pistachio, hazelnut and almond are tree nuts`.

**Qué falla.**
- **La traducción se comió el cacahuete.** El ES dice «FRUTOS SECOS», que en el uso español incluye el cacahuete, y la
  EN lo ha traducido por «TREE NUTS». En EE. UU., peanut y tree nuts son dos alérgenos mayores distintos (FALCPA).
- **En una scoop shop US el cacahuete es de lo más habitual:** peanut butter, peanut butter cups, Reese's como mix-in y
  topping, y cacahuete picado en el sundae bar.
- **Falta justo en la hoja donde se recogen las alergias por escrito**, y en la regla de contacto cruzado del scoop.
  El 01 B27 sí lo lista: el kit se contradice.

**Corrección EN:**
- 06 B6:
  `Get guests' allergies and intolerances IN WRITING and confirm which flavors you can serve: an ice cream menu concentrates MILK, TREE NUTS, PEANUTS, EGG, WHEAT (cones, wafers, cookies), SOY and SESAME (US: 9 major allergens; UK: 14)`
- 01 «Opening» B26:
  `Use the dipper well (running water) or one scoop per flavor: tree nuts and peanuts (pistachio, hazelnut, peanut butter) travel from pan to pan on the scoop`
- 01 «Instructions» B17:
  `…pistachio, hazelnut and almond are tree nuts, and peanut butter flavors and toppings carry peanuts (US: 9 major allergens; UK: 14).`

### M4 · Los pints preenvasados, con «allergen label» y nada más

**Dónde:**
- 06 «Peak Season» B18 (L1300): `Prepare to-go packaging: pints and quarts (pre-packed pints get an allergen label; selling by weight needs a legal-for-trade scale)`;
- 05 «Monthly Tasks» B21 (L1130): `Allergen check: verify labeling of pre-packed pints (FDA Food Code 3-602.11)…`.

**Qué falla.**
- **§3-602.11(B) pide más que los alérgenos.** Para lo envasado en el propio local, la etiqueta lleva:
  1. el nombre común;
  2. los ingredientes en orden de peso;
  3. el contenido neto;
  4. el nombre y el lugar del negocio;
  5. la fuente de cada alérgeno mayor.
- **La propia `REGLAS_US['etiqueta_envasado']` lo dice** («nombre, ingredientes y alérgenos»).
- **Una etiqueta solo de alérgenos es una citación segura.** Los pints del congelador de autoservicio son lo primero que
  mira un inspector en una heladería que fabrica.
- **No se inventa nada federal:** el envasado a petición del cliente no es «packaged» (§1-201.10), y eso el kit ya lo
  respeta.

**Norma o fuente:** FDA Food Code 2022 §3-602.11(B); guía de etiquetado en retail del Pennsylvania Dept. of
Agriculture.

**Corrección EN:**
- 06 B18:
  `Prepare to-go packaging: pints and quarts. Pints packed ahead for the freezer case carry a label: flavor name, ingredients, allergens, net weight and your shop's name and city (FDA Food Code 3-602.11); hand-packed to order they are not "packaged". Selling by weight needs a legal-for-trade scale`
- 05 B21:
  `Labeling check: pre-packed pints show name, ingredients, allergens, net weight and shop name and address (FDA Food Code 3-602.11); traceability and an allergen chart matching the recipes`

### M5 · Menores en temporada: faltan los límites propios de una heladería

**Dónde:**
- 06 «Peak Season» B7 (L1268): `Reinforce the team: hire 2 weeks before the season (minors 14–15: FLSA hour and equipment limits; check state work permits)`;
- 05 «Weekly Deep Clean» B21 (L1004): `Clean the inside of the storage freezers`;
- BONUS-02 abril, B8 (L2474): `Hire and train the summer team (many are minors…)`.

**Qué falla.**
- **Lo ya dicho es correcto, pero genérico.** «Hour and equipment limits» no nombra las dos prohibiciones de la FLSA
  que más afectan a una heladería, con un equipo de verano de 14-15 años:
  - **§570.33(i):** no trabajan **en congeladores**; solo pueden entrar un momento a coger algo. Quedan fuera limpiar
    por dentro la walk-in, hacer inventario en ella o trabajar en la hardening room. El kit pone «Clean the inside of
    the storage freezers» como tarea semanal sin advertencia.
  - **§570.33(e):** no manejan, limpian ni montan **maquinaria eléctrica**, y la mantecadora y el pasteurizador no
    están en las excepciones de §570.34 (que sí incluye las «milk shake blenders»).
- **«Hire 2 weeks before the season» se contradice con el propio kit.** La sección se llama «Pre-season prep
  (March–April)» y el B02 contrata y forma en abril. Dos semanas antes del Memorial Day es mediados de mayo, sin tiempo
  para formar. Era la errata «2 weeks» del ES aplicada a la contratación.

**Norma o fuente:** 29 CFR 570.33(e) y (i), y 570.34; guía de la DOL para grocery y restaurantes («may enter freezers
momentarily to retrieve items»).

**Corrección EN:**
- 06 B7:
  `Reinforce the team: hire in March–April so the summer team is trained by Memorial Day. Minors 14–15: FLSA hours, no work inside freezers beyond stepping in to grab an item, and no operating or cleaning the batch freezer, pasteurizer or other power-driven machines (29 CFR 570.33); check state work permits`
- 05 «Weekly Deep Clean» B21:
  `Clean the inside of the storage freezers (not a task for 14–15-year-olds: FLSA)`
- `REGLAS_US['menores']`: se añade 29 CFR 570.33(e)/(i).

### M6 · Catering: se mide a la llegada y después nada

**Dónde:** 06 «Ice Cream Catering»:
- B17 (L1415): `Pack the off-site service kit: pans, spades, gloves, napkins`;
- B21 (L1426): hielo seco;
- B23 (L1432): la llegada a 10 °F o menos;
- B28 (L1446): `Serve ice cream keeping the presentation and flavor rotation`.

**Qué falla.**
- **El transporte está bien:** hielo seco con guantes, sin tocar el helado y con el vehículo ventilado.
- **Pero a partir de ahí la hoja calla.** Es una hoja de un evento al aire libre en julio, y no dice:
  - **cómo se mantiene frío el helado durante el servicio:** carrito o vitrina portátil, o nevera con hielo seco;
  - **dónde van los scoops sin dipper well de agua corriente.** El kit le ha enseñado al lector que la alternativa
    legal es esa, y en un evento no la hay. §3-304.12(A) permite dejarlos en la cubeta con el mango fuera; si no, un
    scoop por sabor;
  - **qué se hace con lo que se derrite:** se tira, no se recongela. Es el criterio de FoodSafety.gov para el helado
    descongelado;
  - **que el hielo seco pone el helado como piedra:** hay que temperarlo antes de servir.
- **Un inspector del temporary food permit** (que el kit cita en B7) mira justo la temperatura y los utensilios en
  servicio.

**Norma o fuente:** FDA Food Code 2022 §3-304.12(A) y (D); [criterio del kit] para el descarte de lo derretido.

**Corrección EN:**
- B17:
  `Pack the off-site service kit: pans, one scoop per flavor (no running-water dipper well on site), spades, gloves, napkins and a probe thermometer`
- B21:
  `Check the cold chain for transport (insulated carriers; dry ice with gloves, never touching the ice cream, vehicle ventilated). Dry ice over-hardens the ice cream: let the pans temper before scooping`
- B28:
  `Serve from a dipping cart or a dry-ice cooler, scoops kept in their pan with the handle up (FDA 3-304.12(A)); check temps during service and throw out any ice cream that melts — never refreeze it — log reading: ____ °F`
- `REGLAS_US['dipper_well']`: se añade §3-304.12(A).

---

## Menores

- **m1 · 02 «Pasteurizing» B15 / C15 (L294-295).**
  - **Qué falla:** `…(pasteurizer cooling cycle or blast freezer)` y la zona C15 «Hardening». La mezcla líquida no se
    enfría en un blast freezer ni en la hardening cabinet: el «abatidor» del ES es aquí un blast chiller. El glosario
    D8 («Abatidor → Hardening») lo arrastra.
  - **Corrección:** `(pasteurizer cooling cycle, a blast chiller or an ice bath)` y C15 = «Pasteurizer».
  - **Nota estatal:** las normas estatales piden enfriar «promptly» a 45 °F (MCL 288.735; N.J.A.C. 8:21-7.27). Las 6 h
    de §3-501.14 son el máximo general, y con el ciclo del pasteurizador sobra. Se puede añadir «or faster if your
    license says so».
- **m2 · 02 «Pasteurizing» B13 (L288).**
  - **Qué falla:** `Pasteurize at 185 °F for 15 seconds (high-temp)` se lee como una orden y no dice que es la cifra
    del kit. No da los mínimos que un fabricante US reconoce: batch 155 °F 30 min y HTST 175 °F 25 s (NJ, IL, MI). En
    Michigan solo se cita el batch.
  - **Corrección:** `Pasteurize to your state license and your pasteurizer's validated program (typical state minimums: 155 °F for 30 min batch, or 175 °F for 25 s HTST); the kit's high-temp target, 185 °F for 15 s, only where your regulator accepts it — log reading: ____ °F, and keep the recording chart if your license requires one`.
  - **Gates:** exige 155 y 175 en `GRADOS_F_SPEC` y la cita estatal en `REGLAS_US['pasteurizacion']`. Si no se quiere
    abrir G7, basta con añadir «(kit target)» tras «15 seconds».
- **m3 · 02 «Instructions» B6 (L243) · 05 «Quarterly & Annual» B19 (L1204).**
  - **Qué falla (B6):** pone Arizona como ejemplo de estado que exige licencia por pasteurizar la mezcla propia. Desde
    HB 2178 (2019), A.R.S. § 3-607 exime a quien la pasteuriza y la vende para consumo en el local, con un plan
    aprobado por el health department. Además, «Check with your state department of agriculture»: en Massachusetts es
    el DPH.
  - **Corrección (B6):** `(e.g. Vermont, Georgia; Arizona exempts on-premises sales with an approved plan)` y `Check with your state department of agriculture or health`.
  - **Qué falla (B19):** `if you make your own ice cream or pasteurize your own mix` contradice al B6, que dice que con
    mezcla comprada suele bastar el health permit.
  - **Corrección (B19):** `if you pasteurize your own mix (or your state also licenses batch-freezing or soft serve)`.
- **m4 · 02 «Batch Freezing» B24 (L396) · 05 «Weekly Deep Clean» B13 (L981).**
  - **Qué falla:** «remove dasher, gasket and cylinder». En una mantecadora el cilindro es fijo: se desmontan el
    batidor (dasher), las palas y la junta de la puerta, y el cilindro se limpia en su sitio.
  - **Corrección:** `remove the dasher, scraper blades and door gasket, clean the cylinder in place, then sanitize`.
  - **Errata ES:** «desmontar… cilindro».
- **m5 · 04 «Ice Cream Maker» B16 (L736).**
  - **Qué falla:** `Refill the dipping cabinet with fresh pans`. Una cubeta recién salida de la hardening a 0 °F o
    menos no se puede servir: en una scoop shop US las cubetas se «temperan» antes.
  - **Corrección:** `Refill the dipping cabinet with tempered pans (moved up from the storage freezer ahead of time so they're scoopable; neat visual finish)`.
- **m6 · 05 «Weekly Upkeep & Stock» B10 (L1046) · 05 «Quarterly & Annual» B15 (L1192).**
  - **Qué falla (B10):** «…and run the dishwasher cleaning cycle» queda dentro de «If you serve coffee or hot drinks»,
    y el lavavajillas (si lo hay) no depende del café.
  - **Corrección (B10):** `If you serve coffee: backflush the group head with detergent and replace the gasket if due. If you have a dishwasher: run its cleaning cycle (filters and wash arms)`.
  - **Qué falla (B15):** da el espresso por presente en todas las tiendas.
  - **Corrección (B15):** `dipper wells, the ice machine and any espresso machine hook up to the water supply`.
- **m7 · 05 «Quarterly & Annual» A4 (L1151) vs F6 (L1162).**
  - **Qué falla:** la cabecera «Contracted services — quarterly & semiannual» incluye el control de plagas con
    frecuencia «Monthly». El ES ponía «Trimestral»; la EN lo pasó a mensual (D11) sin tocar la cabecera.
  - **Corrección:** `Contracted services — monthly, quarterly & semiannual`.
- **m8 · 05 «Quarterly & Annual» B7 / F7 (L1164-1166).**
  - **Qué falla:** la campana NFPA 96 va «Semiannual». En la tabla de NFPA 96, el semestral es para el volumen
    moderado. Unas planchas de gofre o crepe en una heladería, y más si es de temporada, son «low-volume cooking
    operations, such as … seasonal businesses»: anual.
  - **Corrección:** B7 `…cleaning by a certified contractor at the NFPA 96 frequency for your cooking volume (low volume, e.g. waffle cones or a seasonal shop: annually)…` y F7 = «Annual».
- **m9 · 08 «Shop Closing» B13 (L1737) · 01 «Opening» B12 (L55).**
  - **Qué falla (B13):** `gas off, water off`. En una heladería US el gas, si lo hay, alimenta a menudo el calentador
    de agua o la calefacción, y cerrar la llave general cada noche deja sin agua caliente para lavarse las manos a las
    10:00 (100 °F, 5-202.12). «Water off» tampoco dice qué se cierra: en una heladería es el grifo del dipper well.
  - **Corrección (B13):** `Final safety check: gas appliances off (waffle irons, griddles) if any, dipper well tap off, small appliances unplugged — never the freezers or dipping cabinets`.
  - **Patrón heredado (01 B12):** «open the main valve» viene de la cafetería, el catering y la ghost, que ya
    publicaron con él. Se puede dejar o cambiar por `check there is NO gas smell BEFORE lighting anything`.
- **m10 · 01 «Opening» B28 (L101).**
  - **Qué falla:** «milk caramel». El ES dice «dulce de leche», que es el término US (Häagen-Dazs, Talenti).
  - **Corrección:** `chocolate, caramel, berry, dulce de leche`.
- **m11 · 03 «Weekly Tasks» B7 (L544) · 05 «Monthly Tasks» B14 (L1110).**
  - **Qué falla:** «target <28–32%». Un «menos que» delante de un rango no se lee en inglés.
  - **Corrección:** `target 28–32% or lower` (véase la duda sobre el rango).
- **m12 · BONUS-02 «Instructions» B16 (L2447).**
  - **Qué falla:** «Mothering Sunday (March)». Es el 4.º domingo de Cuaresma, tres semanas antes de Pascua, y algunos
    años cae a principios de abril (2030, 2038).
  - **Corrección:** `Mothering Sunday (3 weeks before Easter: March or early April)`.
- **m13 · 03 «Weekly Tasks» B22 (L587).**
  - **Qué falla:** `Check expiry dates in storage and freezers (FIFO) — log reading: ____ °F`. El ES no lleva lectura.
    Es la única celda donde la EN añade «log reading» a una tarea que no mide temperatura.
  - **Corrección:** quitar la coletilla.
- **m14 · 01 «Opening» B18 (L72).**
  - **Qué falla:** `above 41 °F the pasteurized mix is no longer safe`. Es absoluto, y llevará a tirar mezcla que una
    lectura de 43 °F durante 20 min no justifica, o a que el lector deje de fiarse del kit.
  - **Corrección:** `above 41 °F, the person in charge assesses the mix (how warm, for how long) before it is used`.

---

## Dudas (no son errores claros)

1. **Hot fudge sin cifra (01 B28).** Es aceptable para el fudge comercial: suele ser no-TCS por su baja aw, y la
   etiqueta manda. Si la tienda hace un hot fudge propio con nata, podría ser TCS. Entonces sería
   `house-made fudge with cream held at 135 °F or above (FDA 3-501.16)`; el 135 ya está en `GRADOS_F_SPEC`, pero haría
   falta la cita en `REGLAS_US`. No lo marco como error porque no hay un criterio federal claro sobre la aw de una salsa
   casera.
2. **Draw temperature 16–19 °F / 10–14 °F (02 «Batch Freezing» B8).** Viene del ES (−7/−9 y −10/−12 °C) y lleva «per
   the manufacturer». En algunas mantecadoras US (Emery Thompson) el ice cream de alto overrun sale algo más caliente
   (≈ 20–22 °F). No lo he comprobado en un manual concreto.
3. **«Calculate production: 2–3 scoops per guest» (06 B15).** Es generoso para un evento: 1-2 scoops es lo más
   habitual en las tarifas de catering de helado. Es criterio del kit y viene del ES.
4. **Rango de food cost 28–32 %.** En una scoop shop que fabrica, el coste de producto suele estar algo por debajo
   (20-30 %). Está declarado como `plazos_kit` [criterio del kit].
5. **08 «Shop Opening» B8 (10:00 AM, «Raise security gate and open front door»).** La puerta al público se abre a las
   11:00. Es el texto del base (aceptado en los hermanos) y se entiende como la entrada del equipo, pero
   `unlock the front door for the team` lo dejaría claro.
6. **06 «Catering» B23, la llegada a 10 °F o menos y «don't serve it».** Por encima de 10 °F sigue congelado: el
   criterio es de calidad, no sanitario. «Assess first» lo cubre.
7. **Etiqueta nutricional de los pints.** No la pido: los alimentos elaborados y vendidos solo en el propio local
   suelen estar exentos de Nutrition Facts (21 CFR 101.9(j)). No la he incluido en M4 para no afirmar una exención que
   el kit no tiene en `REGLAS_US`.
