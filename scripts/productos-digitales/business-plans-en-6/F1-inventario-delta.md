# BBQ Catering Business Plan Kit (EN, $39) — inventario delta de F1

> Sesión Claude Code, 24-oct-2026 (rama `feat/bbq-catering-business-plan-en`). JSON y código leídos en el Mac; los 12
> ficheros ES y el libro del catering EN, abiertos en el VPS (`/root/wt-bbq`, venv `/root/venv-guias`; nada escrito fuera
> de `/tmp`). CPU del Mac < 51 °C. Fuente ES: `astro-site/public/dl/plan-negocio-parrillero-asador-eventos/` (2.2, 12 ficheros).
> Moldes: Catering EN (`business-plans-en-4/`, `cat`) y Mobile Bar EN (`business-plans-en-5/`, `mbar`). Los recuentos de §1
> salen de aplicar a cada cadena del catering EN publicado una regex de «vocabulario de catering que no vale para BBQ»
> (plated, stations, chef, induction, van, refrigerated, generator, fuel…) más una lista de celdas forzadas: es una cota y
> la revisión semántica la hacen los redactores. **Los 8 sha256 del diccionario del catering siguen idénticos a los fijados en
> `mapas_mbar.py:164-173`** (comprobado hoy): se pueden fijar los mismos.

## 0. Lo que manda (propuesta para la SPEC)

1. **Fuente del circuito = FOOD TRUCK ES** (como `cat` y `mbar`). **Diccionario de reuso por celda = EN publicado del CATERING**,
   no el del mobile bar: un BBQ catering es comida en eventos, y el EN del catering ya habla de food cost, commissary,
   buffets, drop-off, chafing, ezCater, servers W-2 y service charge. El del mobile bar quitó justo eso (`mapas_mbar.py:156-161`).
2. **El código se clona del mobile bar** (el más reciente: sha del diccionario, `REGLA_UNIDADES`, cifras con `propios` y
   `_importes_research`, autotest de calculadora con varias pestañas), **pero el contenido de comida sale de `datos_cat.py`**.
3. **Motor de eventos tal cual**: B4 eventos/año, B5 precio por invitado, B6 invitados/evento, con los 7 parches
   (`mapas_mbar.py:97-106`). Solo cambian los escalones del break-even: research §8 propone **±$3 / +$6** para B5 = $38.
4. **Cuatro ficheros.** La calculadora gana dos pestañas: **«Meat Yield & Smoke Schedule»** y **«Shopping List by Guest
   Count»** (§2 y §4). No hace falta un 5.º entregable.
5. **Del ES no se reutiliza ninguna cifra.** Sí se aprovechan las tablas técnicas del manual (pasadas a lb y °F), el escalado de
   la calculadora ES y el contenido de las 61 ranuras del docx. **Hallazgo clave:** el docx ES 2.2 está escrito en **las mismas 61
   ranuras** que el EN. `parrillero-2_2/textos/par_es_{a,b}.json` tiene 61 claves, idénticas a `docx_en_cat_{a,b}.json`. Cada ranura
   EN tiene, por tanto, su párrafo BBQ en español y su modelo EN del catering.

## 1. Gemelo, diccionario y código

**Por qué el catering y no el mobile bar (medido).** Del `textos_es.json` del catering (959 cadenas):
- **331 GM** no tocan el vocabulario vetado para BBQ y se reutilizan tal cual. En el mbar quedaron 312, y redactó 130 GMB-plan.
- En las 150 de texto libre del plan, solo **22 cadenas** traen vocabulario que no vale. Casi todas son el cambio de vehículo: «van», «refrigerated», «generator», «burner». Otras 2 son falsos positivos de «range».

Con el mbar como diccionario habría que volver a escribir en clave de comida unas 75 cadenas que el catering ya tiene, además de las 24 tareas nuevas del bar.

**Qué hay que tocar.** En el código común, **solo** una rama `elif CONJUNTO == 'bbq'` en `business-plans-en/mapas.py`: 7 líneas,
copiando `:1218-1224`, más el mensaje de error de `:1226`. El resto vive en `business-plans-en-6/`:

| Fichero nuevo | Origen | Cambio |
|---|---|---|
| `mapas_bbq.py` | copia de `mapas_mbar.py` (332 l.) | PLANES (`slug` `bbq-catering-business-plan` [propuesta], `slug_es` `plan-negocio-parrillero-asador-eventos`, `dir_es` = FT ES; `:40-51`), LIBROS `BBQP`/`BBQC` (`:56-61`), `A_CAT` idéntico (`:66`). Pestaña F2 (`:77`): «Phase 2 - Pits, Fire & Permits» (30 caracteres). `SHA_DICCIONARIO`: los mismos 8 (`:164-173`). `RX_REESCRIBIR` **invertido** (abajo). `FORZAR_TRADUCTORES` con las 41 celdas de abajo (`:238-240`). En `reuso_de` (`:282-283`), dejar pasar la D19: 5 de las 14 filas sirven del catering. PARCHES: los 7, con B31/D31/E31 en `$B$8∓3` / `+6`. `PRESTAMO_SEMILLA` = punto fijo del dry-run |
| `datos_bbq.py` | estructura de `datos_mbar.py` (1.172 l.), contenido de `datos_cat.py` (794 l.) | FIJOS del motor (`datos_cat.py:42-58`) tal cual. ≈ 9 títulos nuevos y ≈ 21 POR_CELDA reescritos (§3). `REGLA_UNIDADES` (`datos_mbar.py:27`) entera. Fuera `GLOSA_DRY_HIRE` (`:25`). `_F13/_F14_MBAR` (`:1085-1087`) solo si la SPEC adopta las líneas «BBQ packages / Add-ons» de research §8 (si no, valen las notas «FOOD sales» del FT). `TAREAS_BBQ` (68 pistas con «[sobrevive]»). 61 `DOCX_NOTAS`. `RX_BBQ_NO`. Cifras (§7). Glosario = research §9 |
| `bp6.py` · `barrido_bbq.py` · `BRIEF-TRADUCTORES.md` | copias de `bp5.py` · `barrido_mbar.py` · brief del mbar | `verificar` (`bp5.py:35-83`) exige 272 celdas en GBQ-check y los sha |
| `fuente_bbq.py` | más simple que `fuente_mbar.py` | Checklist ES **importable** de `parrillero-2_2/datos_checklist.py:21-288` (sin xlsx). Ranuras del docx de `parrillero-2_2/textos/par_es_{a,b}.json` (ES con `{TOKENS}`). Tablas del manual (6), carta (12), experiencias y contrato con python-docx en el VPS (≈ 30 l.) |
| `calculadora_bbq.py` | §4 | El mayor código nuevo |

**Grupos y recuento** (sobre las 959 cadenas del catering; el GR de 7 se reparte: 5 → GRC-plan, 2 → GBQ-plan):

| Origen (catering) | n | Palabras EN | → Grupo bbq | Qué es |
|---|---|---|---|---|
| GM limpio | **331** | 3.738 | GM (tal cual) | Motor y finanzas genéricas |
| GCAT-plan + GR sin vocabulario vetado | **92** | 1.992 | GRC-plan (revisión, ≈ 15-20 % cambia) | D18 «método» y notas del motor |
| Con vocabulario vetado (vehículo, combustible) | **24** (2 falsos) | 728 | GBQ-plan con propuesta | `0. Assumptions!C27/C28/C31-C33`, `P&L!F22/F51`, `Instructions!A5/A39/C39/C41/D41/A42/A43/C44/D44/A49/B49/D49`, `Startup!D27`, `Cash Flow!D32` |
| Forzadas (contenido BBQ) | **41** | 1.354 | GBQ-plan con propuesta | `C6/C13/C24/C26/C44/C45/C51/C52/C54/C55`, `Startup!D7:D20`, `P&L!A10/F10/A11/F11/F24/F32/F34/F35/F53/F54/F55`, `Staffing!J5-J8/J18/J19` |
| D19 (14 filas × 4) | **56** | 466 | GBQ-plan (≈ 20 con propuesta: filas de marketplace, depósito, shared kitchen, seguros y neto) | Benchmarks de research §5 |
| GCAT-check (68 × 4) + 3 textos | **275** | 2.688 | GBQ-check con propuesta | 39 tareas casi literales, 21 con cambio de palabras y 8 nuevas (§5) |
| GX (FIJOS, POR_CELDA, pestañas…) | 143 | — | GX | ≈ 30 a reescribir en `datos_bbq.py` |

**Carga de redacción.** GBQ-plan **121 cadenas** (≈ 2.550 palabras EN de partida, 65 de ellas con propuesta) + revisión de GRC-plan
**92**. En GBQ-check se reescriben ≈ 29 filas (≈ 1.000 palabras nuevas); en la columna C de ≈ 20 filas, «Executive chef» pasa a «Pitmaster». Docx: **61 ranuras**, de las que ≈ 23 son casi
literales, 26 se adaptan y 12 son nuevas (§6). Frente al mbar (128 + 94 + 24 tareas nuevas + ≈ 36 ranuras nuevas), son **≈ −35-40 %
de palabras nuevas**. Con el ES alineado ranura a ranura y el checklist ES ya en Python, a los redactores les llega todo masticado.

**`RX_REESCRIBIR` del bbq** (clasifica, no es el gate): `plated|family-style|chef-attended|themed|stations?|(?<!AI )chefs?|sous|
owner-chef|induction|burners?|ovens?|reach-in|taco|pasta|cuisine|coffee|vans?|refrigerat|upfit|cargo|generator|\bfuel\b|insulated carriers|hot box`.
`grupo_de` = el de `mapas_mbar.py:258-276` con estos grupos: `GRUPOS = ('GM','GRC-plan','GBQ-plan','GBQ-check')`,
`GRUPOS_TRADUCTORES = ('GBQ-plan','GBQ-check')`, `REVISAR_EN_TANDA = {'GBQ-plan': ('GRC-plan',)}`. La regla de ranuras del checklist
es la del mbar: `TAREAS_BBQ` deja en su fila las tareas del catering que sobreviven, o la propuesta EN sería la de otra tarea.

## 2. Contenido ES aprovechable (12 ficheros) y nº de entregables

| Fichero ES (medido en el VPS) | Vale para el EN | Solo España (fuera) |
|---|---|---|
| Plan docx · 142 párr. · 8.211 pal. · 11 H1 (10 + anexo CCAA en [119]) | **61 ranuras alineadas** con el EN. Concepto [40] (fuego y corte delante del invitado, sonda), mezcla por tipo de cliente [48], 6 fases del evento [50] y [78], «es tuyo lo que viaja, lo que usas un día lo alquilas» [79], control con sonda [80], Porter y DAFO [62] [66], embudos y degustación [69] [73], plan B de fuego [112] | Cifras en € (tokens), RD 1021/2022, AESAN, IVA 10 %, fijos discontinuos, contrato menor/FACe, ATP. **Anexo CCAA [119-128] fuera**: en EN, «burn bans vary by county» en §9 |
| Plan financiero xlsx · 9 hojas (motor 2.2) | Nombres de partidas (§3) y la estructura de 4 puestos (titular + 3 a tiempo parcial). Nada más: ya tenemos motor EN | Todas las cifras y el caso 95 × 80 × 25 €. IS, IVA, SMI, 14 pagas |
| Checklist xlsx · 83 tareas (12/16/14/10/16/15) | 72 adaptables (§5); el texto está en `datos_checklist.py` | 11 enteras y 5 parciales (§5) |
| Calculadora xlsx · 3 hojas, 168 fórmulas | **Lo más valioso para la EN**: formato → g crudos por invitado, experiencia → materia prima por invitado, estilo → invitados por parrillero/ayudante, reglas de escalado (32 kg por parrilla, 0,8 kg de carbón por kg, merma 30 %, ayudante desde 40), tabla de 40/80/150/300 invitados, cancelación por tramos sin huecos y margen calculado (`calculadora_par_es.py:55-98`, `:242-257`) | €, IVA, 0,95 €/km, SS 33 %, canal Ayuntamiento/LCSP |
| Manual técnico docx · 1.226 pal. + 6 tablas | **T2: cocción de 18 cortes** (técnica, T.ª, tiempo, reposo) · **T3: mermas de 10 piezas** · **T4: escalado** · T0 8 salmueras · T1 12 marinados · chimichurri ×3 · 5 salsas · 8 errores | °C, Reg. 853/2004, MER/vértebra, denominación por edad, lechazo, cochinillo, pluma ibérica |
| Carta 12 cortes · 12 fichas | Brisket, St. Louis, picaña, tomahawk, asado de tira, vacío y chorizos → menú US (Texas, Argentine asado, churrasco) | IGP Lechazo, Cochinillo de Segovia, maridajes con vino español |
| 10 experiencias docx · 1.496 pal. | → **menu styles** de research §1: Texas · Carolina · KC · Memphis · Santa Maria · Argentine asado · churrasco · pig roast · fire show · corporate boxed lunch. Van al docx §2 y a la lista de paquetes de la calculadora | Criollo-castellano, mediterránea, llanero (como origen) |
| Guía 8 sistemas + roadmap food truck | Los 8 sistemas → equipo US (research §1). La fase de equipamiento (T8) sirve como orden de compra en el docx §6 | Roadmap food truck (otro producto: Food Truck Kit), CCAA, precios en € |
| Contrato docx · 2.011 pal. | Para la tarea P1 «contract»: tramos de cancelación, fuerza mayor por prohibición de fuego (burn ban → propano o nueva fecha), variación de invitados, derechos de imagen | TRLGDCU, IVA, Bizum, fuero |
| Catálogo · proveedores (93) · equivalencias | Solo las categorías, como lista de tipos | Marcas, SKU y precios españoles; la guía de equivalencias es ES ↔ LatAm |

**¿4 o 5 ficheros? Cuatro.** Como en el bar móvil (inventario `-5/` §2), el valor útil del manual y de la carta está **en el cálculo**:
cuántas libras de brisket crudo, cuántos packers, cuánta leña y cuántos pitmasters para N invitados, y a qué hora encender. Eso
cabe en la calculadora: **«Meat Yield & Smoke Schedule»** (≈ 12-14 cortes US desde T2/T3) y **«Shopping List by Guest Count»**
(desde T4 y las REGLAS ES). Cuesta ≈ 0,12-0,18 M, con datos, fórmulas y el autotest que ya existe. Un 5.º docx (manual o carta US)
costaría ≈ 0,3-0,4 M: generador sin circuito, recetas redactadas, gate propio y alta en F3 (descargas, dashboard, llms). Además,
las salmueras y marinados en g/L piden conversión y revisión de alérgenos. **Descartado también** meter «Rubs, Brines & Sauces»
como tercera pestaña: es texto, no cálculo, y el research no lo pide. Las 10 experiencias van al docx §2 y a la lista de paquetes.

## 3. Delta del libro financiero (sobre el catering EN, celda a celda)

**Solo texto (GX, `datos_bbq.py`):**
- **Motor.** `FIJOS_NUEVOS` del catering (`datos_cat.py:42-58`) tal cual. B5 sigue como «Average price per guest (excl. sales tax,
  service included)». Las notas C4-C6 se reescriben (GBQ-plan): drop-off, fiestas, empresa, bodas y live-fire.
- **Títulos:** «BUSINESS PLAN: BBQ CATERING COMPANY», «Base case — BBQ caterer (smoked meats, off-site)», «Break-even — BBQ
  Catering», «US BBQ CATERING BENCHMARKS (sourced) AND KIT ESTIMATES», «BBQ CATERING STARTUP CHECKLIST — OFF-SITE BBQ CATERER»,
  «PHASE 2: COMMISSARY, SMOKER TRAILER, FIRE RULES & PERMITS», título de Instrucciones y `Instructions!A3` de los dos libros.
- **Mezcla de ventas.** Hay que decidir en la SPEC si se adoptan las líneas de research §8: A11 «BBQ packages (smoked meats, sides,
  bread & sauces, staffing)» / A12 «Add-ons (desserts, appetizers, non-alcoholic drinks, rentals…)».
  - Si se adoptan, A11-A14 de Supuestos, A10/A11/A13/A14 del P&L y las notas de fórmula `P&L!F13/F14` pasan a GX y a FORMULAS_EN (≈ 10 cadenas, mecanismo `datos_mbar.py:1085-1087`).
  - Si no, GM tal cual, con A10 «Food sales (smoked meats and sides: drop-off, buffet and live-fire)» y A11 «Beverage sales (sweet tea, lemonade…)».
  - A15 → «**Disposables, wood & fuel**» (research §8: 3,5 %). La leña es variable, escala con las libras y **no** va en utilities.
  - A16/A17: marketplaces corporativos (ezCater), igual que en el catering (`datos_cat.py:66-67`). A62 alcohol 0 % (como en el catering).
- **Inversión, filas 7-20.** ⚠️ **Choque con la research.** La base de vida del vehículo es `B31 = B7+B8+B11+B12+B15+B23`, la de equipo
  `B32 = B9+B10+B16+B17+B20` y la contingencia `B23 = (B7+B8+B11+B12+B15) × B55` (fórmulas leídas en el catering publicado).
  Research §8 pone la *cargo van* (9) y su upfit (10) en la base de **equipo** y el *live-fire rig* (11) en la de **vehículo**, y estima
  la contingencia «sobre 7-11» ($4,900), cuando la fórmula da $4,500 con mi orden. **Propuesta de orden (solo se mueven filas; ninguna fórmula):**

| Fila | Base | Catering | → BBQ (importe = research §8) |
|---|---|---|---|
| 7 · 8 | vehíc. | Refrigerated van · upfit | **Smoker trailer** (offset / reverse-flow, clase 500 gal) · smoker trailer upfit (warming cabinet, lavamanos y depósitos si el condado lo pide) |
| 9 · 10 | equipo | Kitchen equipment · portable cooking | **Live-fire rig** (Santa Maria grill, Argentine parrilla, asado crosses, caja china) · commissary storage fit-out (racks, meat lugs, vacuum sealer) |
| 11 · 12 | vehíc. | Refrigeration unit · commissary fit-out | **Used cargo van** · van upfit (shelving, tie-downs, wrap). El vehículo de arrastre es el del dueño ($0), con nota |
| 13 · 14 · 15 | — · — · vehíc. | LLC · permisos · plan review | LLC · permisos y certificaciones del año 1 (catering/health permit, MFU o temporary event, fire inspection, ServSafe Manager) · plan review / trailer inspection |
| 16 · 17 | equipo | Software · smallwares | Software + card reader · **smallwares & pit tools** (cuchillos, hotel pans, probe thermometers, butcher paper) |
| 18 · 19 | — | Inventario · web | Opening inventory (carne de pruebas, rubs, salsas, leña) · website, photos, launch & bridal show |
| 20 | equipo | Chafing & serving ware | **Holding & service equipment** (insulated carriers, hot boxes, chafing, coolers, canopy, carving board) |

- **Rótulos de las bases:** A23 «Van, trailer and fit-out contingency» · A31 «Smoker trailer, van and fit-outs (depreciated over the
  vehicle life)» · A44 «Useful life of the smoker trailer, van and fit-outs» · A55 «Contingency on the trailer, van and fit-out
  lines (%)» · A51 «Max events a year your pit and crew can handle» (research: 220).
- **Fijos (`3-Year P&L`):**
  - A22 «Commissary kitchen rent & smoker trailer parking», con nota C24: ahumar en el patio de la commissary, research §1.
  - A24 «Utilities (propane backup, water, power not covered by the commissary)».
  - A25 seguros = GL/BOP + commercial auto **que cubra el remolque** + workers' comp + inland marine del smoker (C27).
  - A26 «Annual permits and licenses (catering / health permit, MFU or event permits, fire inspections)».
  - A27 «Vehicle & trailer fuel, maintenance and registration». Ojo: el catering movió el combustible a varios (M2) y la research lo devuelve al fijo. **Hay que elegir uno solo y reescribir A27, F18, C28 y D18 A49 en coherencia**.
  - A32 «Waste, grease and ash disposal».
  - A33 «Smoker & equipment repair» (sustituye a pest control, research §8; la nota F33 del catering sale).
  - A34 «Food safety training (ServSafe Manager, food handler cards)».
  - A35 «Tastings for prospects» se queda.
- **Personal** (`Staffing!A5:A8`, opción A heredada): Owner / Pitmaster & Sales · Pit cook / lead cook (W-2) · Event staff (servers,
  buffet attendants, carvers; hourly W-2) · Prep cook / driver (part-time W-2). A18 «Hours per event to cover (portioning, overnight
  cook, loading, travel, setup, service, breakdown)»; la nota J18 aclara que un pit cook vigila varias piezas a la vez. La nota A24
  del catering vale cambiando «servers, bartenders» por «servers, carvers».
- **Fórmulas con texto:** `_PE_CAT`/`_C9_CAT`/`_F18_CAT` (`datos_cat.py:731-745`) y las listas de partidas de `_inversion` (`:756-760`),
  con los nombres nuevos.

**Valor (huecos de research §8; aquí solo se marcan):** B4/B5/B6 (150 · $38 · 75), mezcla B11-B18, B24-B28, B30-B35, vidas 7/5,
B51, B52-B55, B58/B59, los 14 importes 7-20 (con el orden de arriba), fijos B26-B35, personal B-D (4 puestos, 2.85 FTE), escenarios
B5:D7, estacionalidad (Month 1 = marzo), umbrales E51:E56 (**58 / 35 / 38 / 7 / 5 %**; en el catering, 60 / 35 / 38 / 8 / 5), escalones del
break-even y calibración D15 (holgura ≥ 15 %; préstamo ≈ $98,500 para SBA 7(a)).
**Tabla D19** (14 filas). Se reutilizan del catering, con propuesta: **marketplace 15 %** (D62), **depósito** (D63, que cambia a 50 %
nonrefundable), **shared kitchen rate** (D65), **seguros Insureon** (D67) y **neto 7-8 %** (D58). Son nuevas: precio por invitado por paquete
(drop-off $15-30 · buffet $25-50 · full-service $40-75+), carne por invitado (¼-⅓ lb cocinada), rendimiento del brisket / pork butt (≈ 50 %),
food cost, salarios OEWS (cooks, servers, chefs), inversión (smoker trailer $8,495-20,395), mínimos de invitados y leña por cocción.

## 4. Delta de la calculadora (`calculadora_bbq.py`)

**La ES (medida):**
- **Entradas** (`:100-134`): canal, invitados, formato, experiencia, estilo, bebida, menaje, horas, €/h, SS, alquileres, km, €/km, show e IVA.
- **Salidas** (`:139-191`): g crudos, materia prima, kg crudos y servidos, parrillas, parrilleros, ayudantes, carbón, costes, precio redondeado a 0,50 más el show, IVA, 4 cobros, margen calculado y 4 tramos de cancelación.
- **Tablas visibles** de reglas, servicios, formatos, experiencias y canal, más el escalado 40/80/150/300 (`:204-207`).

**Vale casi todo el diseño**: escalado por kilos, reglas editables, cancelación sin huecos y margen calculado. **No valen**: €, IVA,
canal Ayuntamiento, €/km sin margen, SS 1,33 ni los precios de materia prima de las experiencias.

**EN propuesta.** El esqueleto es `calculadora_mbar.py`: 5 pestañas, `hoja_compra` `:501`, `hoja_specs` `:659`, `hoja_ejemplos` `:738` y
autotest multipestaña `:880-1030`. Coste → precio de `calculadora_cat.py:47-108`, tablas y `escalar()` de `calculadora_par_es.py:55-77, :242-257`.
- **Entradas (verdes, con DV):**
  - Evento: invitados, **guest minimum**, **paquete** (lista: «Drop-off (pans, sides, setup)» · «Full-service BBQ buffet (attended, carving)» · «Premium live-fire (pit on site)»).
  - Carne: **oz de carne cocinada por invitado según el paquete** (Kit estimate de research §5: 4-8 oz) y **mezcla de carnes** (% brisket / pulled pork / ribs / chicken / sausage, tabla verde).
  - Costes: sides por invitado, pan y salsas, desechables, leña y carbón (lb por lb cruda y $/lb), **$/lb crudo por corte** (la research no tiene precios leídos de 2026: el usuario los teclea).
  - Personal: pitmasters y servers sugeridos (buffet 1 por 25-30), horas y horas de cocción nocturna, $/h, cargas %.
  - Logística: alquileres, millas × $/milla, event/travel fee fijo.
  - Cobro: margen objetivo, service charge %, sales tax % + «¿grava tu estado el service charge?» (`calculadora_cat.py:76-81`), depósito % (50 % nonrefundable) y tramos de cancelación (estructura ES, días US).
- **Salidas:** libras crudas y cocinadas por corte, nº de piezas (packers, butts, racks), leña, coste de carne y de sides, personal, coste
  directo, **precio por invitado** (y su equivalente **por libra** cocinada, como cotiza el drop-off US), subtotal facturable,
  service charge, impuesto, total, depósito, saldo, retención por tramo y **margen calculado**. La propina voluntaria queda fuera.
- **«Meat Yield & Smoke Schedule»:** 12-14 cortes (packer brisket, pork butt, St. Louis y baby back ribs, beef plate ribs, chicken
  thighs y halves, turkey breast, sausage, tri-tip, picanha, tomahawk/ribeye y whole hog opcional). Columnas:
  - Peso crudo por pieza, temperatura del pit en °F (°C) y temperatura final **de calidad** (brisket ≈ 203 °F).
  - **Mínimo seguro del Food Code** en columna aparte: 145 °F intacta, **155 °F inyectada o picada**, 165 °F aves (research §6.4).
  - Horas, reposo y hold, rendimiento % y raciones por libra cruda.
  - **«Start the pit by»** = hora de servicio − cocción − reposo − margen, por fórmula.
  - Nota de enfriado (135→70 °F en 2 h, →41 °F en 6 h) y recalentado a 165 °F.
- **«Shopping List by Guest Count»:** columna de los invitados de la hoja principal + referencia 40/80/150/300 (T4 del ES):
  libras crudas por corte, piezas, galones o half pans de sides, panecillos, salsa, leña o carbón, papel/aluminio, hotel
  pans, hot boxes, pitmasters y servers.
- **«3 Example Quotes»:** corporate drop-off 40 inv. · graduation buffet 70 · wedding live-fire 130, dentro de las bandas de research
  §5 (mbar M9: nada de ejemplos fuera de mercado). Más **«Instructions»**.
- **Riesgo de coherencia:** el B5 del libro es la mezcla ($38) y la calculadora cotiza por paquete. La nota de `C5` tiene que explicar
  cómo pasar de una a otro (catering M3).

## 5. Delta del checklist (68 = 11/13/12/10/12/10, ranuras `mapas_mbar.py:90-91`)

**Mapeo del ES** (83 tareas, `datos_checklist.py`):
- **Solo España, 11 enteras:** F1·3 IAE · F1·4 SS · F1·5 certificado digital · F1·8 IVA 303 · F1·10 390/347 · F1·11 RGPD · F2·3 RGSEAA · F2·5 comida testigo · F4·2 alta antes del llamamiento · F4·7 datos del trabajador · F5·14 ayuntamiento/FACe.
- **Parciales, 5:** F1·7 Veri*factu · F2·7 MER/vértebra · F2·12 ADR · F5·10 Hosply · F6·13 FACe.

| Fase ES | Tareas | → Fase EN |
|---|---|---|
| F1 Constitución | 12 | P1 (1-2 → LLC; 6 banco; 7 y 9 → accountant y estimated taxes; 12 no-desistimiento → contrato y cancelación) |
| F2 Sanidad, fuego y brasa | 16 | P2 (1 commissary; 2 → county catering / health permit; 8-9 → GL, commercial auto + remolque; 11-15 → **fire marshal, propane backup (LP ≤ 200 lb), extintores 2A:10BC + Class K, 10 ft, burn bans, cenizas**; 16 → temporary event permits y reglas del recinto) · P1 (4 → plan HACCP con 145/155/165 °F, hot holding 135 °F y enfriado) · P4 (6 alérgenos) · P1 (10 → force majeure en el contrato) |
| F3 Equipo y proveedores | 14 | P3 (1-5 → smoker trailer, live-fire rig, propane backup, **proveedor de leña**; 6, 8-9 → smallwares, hot boxes y probes, básculas para el yield test; 12 → meat purveyor USDA-inspected + Restaurant Depot; 13 sides) · P2 (14 → van) · P4 (11 EPI) |
| F4 Personal | 10 | P4 (1 → W-2 pool, nunca 1099; 3-5 → food handler cards, alérgenos, OSHA calor/humo/quemaduras; 6 → registros de horas FLSA; 8 → staffing por invitados; 9 → **guion del live-fire / carving**; 10 → fichas por paquete) |
| F5 Marca y captación | 16 | P5 (1 → USPTO; 3-7, 11-13, 15-16; 8 WhatsApp → texto/SMS; 9 → The Knot / WeddingWire; 10 → ezCater) |
| F6 Primer evento | 15 | P6 (1-3 briefing, visita y depósito; 5-7 alérgenos, plan B de lluvia y burn ban, pedido de carne 5-7 días; **8 rubs y porcionado en la commissary**; 9-15 → carga, encendido, cocción con sonda, cenizas, factura, reseña, yield real frente a la calculadora) |

**Ranuras del catering para BBQ** (filas del FT; L = casi literal · A = cambio de palabras · N = nueva):

| Fase | L | A | N |
|---|---|---|---|
| P1 (11) | 5-13, 15 (10) | 14: plan HACCP con enfriado y recalentado de carnes ahumadas (1) | — |
| P2 (13) | 6, 8, 13, 15, 17 (5) | 5: commissary + parking del trailer + almacén de leña · 7: health permit + **¿MFU si se ahúma en el evento?** · 9: fire marshal (solid fuel, LP, 10 ft) · 14: liquor liability solo con alcohol del cliente · 16: cenizas (5) | 10: comprar el smoker trailer · 11: título y registro del trailer en el DMV + auto que lo cubra · 12: upfit del trailer (3) |
| P3 (12) | 8, 12, 13, 14, 15 (5) | 5: propio vs alquilado · 6: hot boxes y probes · 10: meat purveyor · 16: test cook con yield test (4) | 7: smoker/rig/propano · 9: carving station · 11: proveedor de leña (3) |
| P4 (10) | 6-10, 14 (6) | 5: personal por invitados · 12: OSHA calor y humo · 13: alérgenos (3) | 11: seguridad del fuego y extintores (sustituye a alcohol server) (1) |
| P5 (12) | 6-13, 15 (9) | 5: marca + menú por estilos regionales · 14: plantilla con la calculadora (2) | 16: tasting / pop-up de lanzamiento (1) |
| P6 (10) | 10, 11, 12, 14 (4) | 5-9 y 13: **quitar el calco «D-21 / D-14 / D-7 / D-1»**, que el catering publicado aún tiene (mbar M3) → «3 weeks out»… · pedido de carne y horario de ahumado · hot holding · yield frente a la calculadora (6) | — |

**Total: 39 L · 21 A · 8 N.** El mbar tuvo 25 · 19 · 24. **Trámites US que entran** (research §6): commissary por escrito (Food Code 3-201.11), MFU ligada a una central preparation facility
(TX 25 TAC §228.221; FL, NC), fire code (IFC 906.4.1, 319.8.1), approved source / USDA o inspección estatal (whole hog),
CFPM, sales tax sobre toda la factura y W-2. Pestaña «Phase 2 - Pits, Fire & Permits» (30 caracteres).

## 6. Docx: 61 ranuras de 131 (H1 37…109; §9 = 102-108)

| Nivel | Ranuras (palabras del catering EN) | Fuente |
|---|---|---|
| Casi literal: tokens y método (23, ≈ 2.300 pal.) | 42 · 56 · 61 · 65 · 69-75 · 86 · 88 · 90 · 93 · 95 · 97-99 · 106 · 115-117 | EN del catering + tokens (97-99: el pesimista agota la caja, research §8) |
| Adaptar: mismo esqueleto, otro sustantivo (26, ≈ 2.850) | 39 · 41 · 43 · 48 · 49 · 53-55 · 57 · 58 · 62-64 · 66 · 82 · 85 · 87 · 89 · 94 · 96 · 107 · 108 · 111-114 | Catering EN + ES en la misma ranura |
| Nueva, núcleo BBQ (12, ≈ 1.450) | 40 (concepto: ahumado en la commissary, pit en el evento como premium) · 46-47 (propuesta: smoke + live fire, pitmaster) · 50 (paquetes y estilos regionales) · 78-81 (commissary + trailer; equipo; 6 fases con cocción nocturna; seguridad de carnes ahumadas) · **102-105** (§9: sin casa ni cottage food para carne; MFU; fuego y burn bans; alcohol) | ES 2.2 de la ranura + research §1, §6 |

- **Fijos** (`datos_cat.py:281-295` / `datos_mbar.py:390`): portada «BBQ Catering», líneas 9 y 35 (anexos con los 4 ficheros) y
  `PRODUCTOS_CIERRE`. Para el cierre: Catering Business Plan Kit · Food Truck Business Plan Kit · Food Cost Kit Pro · HACCP Food Safety Kit Pro. Aquí la comida está permitida: el mbar los había quitado por su gate (`-5/F2-NOTAS` §4.6).
- Hay que reescribir las 61 `DOCX_NOTAS` y el anexo CCAA del ES no tiene ranura.

## 7. Cifras y vocabulario prohibidos (gate: `cifras_prohibidas()` + `RX_BBQ_NO`, como `datos_mbar.py:1126-1140`)

**Cifras del ES 2.2** (`parrillero-2_2/cifras_caso_es.json`, LIVE), como importe con `_num()`:
- **Importes:** 190.000 · 205.200 · 215.460 · 76.522 · 54.596 · 21.926 · 87.357 · 65.400 · 15.737 · 160.401 · 151.894 · 182.179 · 192.570 · 109.706 · 80.294 · 92.616 · 57.983 · 14.527 · 16.887 · 15.403 · 17.090 · 19.867 · 20.538 · 138.000 · 243.100 · 40.588 · 12.934 · 10.835 · 6.145 · 4.912 · 4.251.
- **Previas a la calibración** (SPEC ES / research): 49.900 y 62.000.
- **Ojo a las colisiones:** 20.000 (furgoneta ES) = $20,000 (smoker trailer US) y 4.500 = live-fire rig. Las salva el filtro `propios` (`:1129`). Por eso no se vetan cifras ES redondas de 4 dígitos (7.000, 3.200, 2.200, 1.950, 22.000).

**Frases** (los números pequeños solo así): «95 events» · «80 guests (per event)» · «81 events» · «76 events» · «6.7 events a month» ·
«25 €» / «€25» / «27.51» · «57.7 %» · «31.8 %» · «30.5 %» · «25.1 %» · «DSCR 1.51» · «83 tasks» · «93 suppliers» · «11 deliverables» ·
«8 (autonomous) regions» · «v1.1». **«$25 per guest» no se veta**: es un precio US plausible.

**Casos EN ajenos:**
- Catering: `_cifras_caso('../business-plans-en-4/cifras_caso.json','cat')` + `FRASES_CAT` (`datos_mbar.py:248-262`).
- Mobile bar: 212,800 · 76,972 · 47,530 · 35,772 · 130,032 · 323,400, más «160 events» y «$14 per guest».
- FT: `_cifras_ft` (`datos_cat.py:164`).
- Se respetan `propios` y `_importes_research` (`:1116`).

**`RX_BBQ_NO` = 0 en los 4 ficheros:**
- **Del FT (D72):** per day, operating days, customers (salvo «corporate customers»), **truck** (→ «tow vehicle» / «pickup»; el competidor se nombra «mobile food vendors» o «BBQ food trucks» solo con lista blanca), window, festival(s).
- **Del catering genérico:** plated, chef-attended / themed stations, executive / sous chef y «chef» suelto (salvo la firma y «AI Chef Pro»; aquí es «pitmaster»), induction, taco bar, pasta, «12 cuisines», refrigerated van (la van no es frigorífica en este caso).
- **Del mobile bar** (por si algo se copia de `-5/`): dry hire, mobile bar, bartending service, barback, mixers, signature cocktails, specialty bar, cash bar.
- **Del ES:** España/Spain, IVA (VAT solo en la nota UK), autónomo, SL, IAE, fijo discontinuo, ETT, AESAN, APPCC, «RD 1021/2022» y demás RD/Reglamento (CE), CCAA, INFOCA, ATP, Veri*factu, FACe, Bodas.net, Zankyou, Hosply, GGM, Brogas, Texfire, parrillero, chuletón, lechazo, cochinillo, EUR/€, freelance, «carné».
- **Unidades** (regla de `REGLA_UNIDADES`): kg, km, litros y °C solo entre paréntesis.
- **Lista blanca:** chimichurri, Argentine asado, picanha, provoleta (en menú), commissary, food handler, «Caterer's Permit», smoker trailer, pickup, «BBQ food trucks» (no es nuestro comprador).

## 8. Deuda del ES (solo anotada)

1. **Merma del brisket incoherente.** 35-40 % en el manual (T3) y en la carta (ficha 08). 40-50 % en el manual §8 [68] y en la nota de `REGLAS['merma']` (`calculadora_par_es.py:73-74`).
2. **«Tabla de cocción de 18 cortes»** (ficha `:134`, `:155`, `:208`): incluye provoleta (queso) y chistorras/chorizos, así que son 16 cortes de carne. La **«Carta 12 cortes de carne»** (`:152`) incluye provoleta y chorizos/morcilla: 10 cortes.
3. **docx [98]** usa `{DIAS_COBRO}` en «a los proveedores les pagas a … días». Coincide porque B58 = B59 = 15, pero si el usuario cambia uno, el texto miente.
4. **Fuera del ES, pero se arrastraría:** el checklist del catering EN publicado conserva el calco «D-21 / D-14 / D-7 / D-1» en P6, que el mbar arregló en M3. Es deuda del catering y en el BBQ se corrige en la pista.

## 9. Esfuerzo de F2 y riesgos

| Paso | Contenido | Tokens |
|---|---|---|
| Implementador opus (Mac + VPS) | Rama `bbq` en `mapas.py`. `mapas_bbq.py` (clon del mbar, RX invertido, 41 forzadas, D19 con propuesta). `datos_bbq.py`: ≈ 30 GX, caso, 68 pistas, 14 D19, 61 notas, cifras y vocabulario. `bp6`/`fuente`/`barrido`. **Calculadora** (5 pestañas, 2 nuevas) | ≈ 0,55 M |
| Tanda 1 (Sonnet ‖ Sonnet) | GBQ-plan 121 + revisión GRC-plan 92 ‖ GBQ-check 275 (≈ 29 filas que cambian + columna C) | ≈ 0,25 M |
| Tanda 2 (Sonnet ‖ Sonnet) | Docx `bbq_a` ‖ `bbq_b`: 61 ranuras, ≈ 4.300 palabras escritas o adaptadas, con el ES alineado | ≈ 0,25 M |
| Gates y revisión | G1-G9, `RX_BBQ_NO`, cifras, autotests y regresión FT/CAF, REST/PAN, BAR, CAT y MBAR. Una revisión opus | ≈ 0,3 M |
| **Total** | Sin contar la F1 | **≈ 1,35 M** (colchón 0,2 M) |

**Riesgos:**
1. **Legal y fuego.** Hay que decidir si ahumar en el evento convierte el trailer en MFU ligada a la commissary (TX sí; CA sin verificar) y fijar el fire code de
   *solid fuel* (Class K, 10 ft, LP ≤ 200 lb, burn bans sin verificar), además del enfriado y recalentado de carnes ahumadas y del «inyectado = non-intact, 155 °F». Esto decide P2,
   §9 [102-105], las filas 14/15 y las notas de la calculadora. Se fija en la SPEC antes de los redactores, con «varies by county».
2. **Fuga de vocabulario y calcos heredados.** Chef/sous chef, stations, plated y van frigorífica del catering; «truck» del FT; el calco «D-21» del P6 del catering;
   «Executive chef» en la columna C. Gate `RX_BBQ_NO` con lista blanca y lectura entera del checklist en la revisión. **Además, research §8
   pone la van en la base de equipo:** aplicar el orden de filas de §3 o la depreciación y la contingencia no casan con su nota.
3. **Calculadora.** Rendimientos y raciones (¼-⅓ lb cocinada, ≈ 50 % de rendimiento) con fuente o «Kit estimate». Precios de carne sin fuente de 2026 (los teclea
   el usuario). Temperatura de calidad frente a la mínima segura, en columnas distintas. El precio por paquete tiene que casar con el B5 de mezcla. Autotest en las 4 pestañas de cálculo.

**Menores:**
- **Canibalización con el Catering Business Plan Kit:** la landing tiene que diferenciar (smoke, pitmaster, smoker trailer).
- **Altas antes de G9:** `bbq-catering-business-plan` en `PRODUCTOS_LETTER` (`censo-entregables.py:153-157`) y `EXCLUIDOS` (`postprocess-transversal.py:112-116`).
- **Combustible:** decidir si va en A27 (fijo) o en varios (variable) antes de redactar (§3).
- **Mezcla de ventas:** decidir si se adoptan «BBQ packages / Add-ons» (afecta a ≈ 10 GX y a 2 notas de fórmula).
