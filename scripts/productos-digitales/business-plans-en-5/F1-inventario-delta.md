# Mobile Bar Business Plan Kit (EN, $39) — inventario delta de F1

> Sesión Claude Code, 13-oct-2026 (rama `feat/mobile-bar-business-plan-en`, base `19dd6b4a`). Medido en el Mac
> (`python3` con openpyxl 3.1.3 + python-docx; sin builds, CPU 50 °C). Fuente ES: `astro-site/public/dl/plan-negocio-cocteleria-eventos/`
> (9 ficheros, línea B antigua, 55 €). Molde: Catering EN (`business-plans-en-4/`, conjunto `cat`). Los recuentos de §1 salen
> de aplicar una regex de «vocabulario de catering de comida» (food, kitchen, commissary, chef, plated, buffet, drop-off,
> stations, chafing, ezCater, servers, menu…) al EN publicado del catering, celda a celda. Es una cota: la revisión semántica la
> hacen los redactores. sha256 (12) del diccionario: `textos_es.json` 9d02ffbeb6c0 · GM b05fd56a3ed3 · GR 7e2e0f23be5f ·
> GR.revision 976190192b0c · GCAT-plan 849c96d84281 · GCAT-check 56399ef7fc4e · docx_en_cat_a 2afccc350b80 · _b 858fcf7d3119.

## 0. Lo que manda (propuesta para la SPEC)

1. **La fuente del circuito sigue siendo el FOOD TRUCK ES**, como en el catering (`mapas_cat.py:43`). **El diccionario de reuso por celda pasa a ser el EN publicado del CATERING**, no el del FT. Como el catering se montó sobre la misma rejilla, el EN de la celda `CATP!X` es el candidato directo para `MBP!X`.
2. **El motor es el del catering tal cual**: B4 = eventos/año, B5 = precio medio por invitado, B6 = invitados/evento, con los 7 parches de `mapas_cat.py:97-105`. Para un bar móvil solo cambian los rótulos y el reparto de las dos líneas de venta (§3).
3. **Cuatro ficheros, igual que el catering.** La calculadora gana una pestaña «Drinks & Shopping List» (§2 y §4). No se añade un 5.º entregable.
4. **El modelo por defecto es el *dry hire*** (el cliente compra el alcohol y nosotros ponemos barra, bartenders W-2, mixers, garnish, hielo y cristalería). El servicio con licencia queda como opción. Lo confirma o lo tumba el research US.
5. **Del ES no se reutiliza ninguna cifra ni ninguna fórmula.** El plan financiero ES tiene 0 fórmulas (§8). Sí se aprovechan el contenido, la operativa, la carta de cócteles y las experiencias temáticas.

## 1. Gemelo, fuente del circuito y reuso

**Por qué el EN del catering y no el del FT.** El GM del catering *es* el EN del FT: `grupo_de` solo deja en GM lo que
no habla de actividad (`mapas_cat.py:248-253`), así que usarlo no cuesta nada. Lo que se gana son las cadenas que el catering ya escribió
en clave de eventos: invitados, anticipos, W-2 frente a 1099, service charge (IRS Rev. Rul. 2012-18), liquor liability, The
Knot/WeddingWire, venues y planners, D18 del método, y 25 filas del checklist. Con el FT como diccionario habría que
reescribir otra vez ≈ 94 cadenas del plan y 25 tareas, lo que sube la carga de redacción en torno a un 30 %.

**Qué hay que tocar.** Código común: **solo** una rama `elif CONJUNTO == 'mbar'` en `business-plans-en/mapas.py` (7
líneas, copiando `mapas.py:1211-1217`) y el mensaje de error de `:1219`. Todo lo demás vive en `business-plans-en-5/`:

| Fichero nuevo | Origen | Cambio |
|---|---|---|
| `mapas_mbar.py` | copia de `mapas_cat.py` | PLANES (`slug` `mobile-bar-business-plan`, `slug_es` `plan-negocio-cocteleria-eventos`, `dir_es` = FT ES), LIBROS `MBP`/`MBC`, pestaña F2 y AUTOTEST. **`_cargar_cat()` / `_cargar_cat_texto()`** copian `_cargar_ft` y `_cargar_ft_texto` (`:169-211`) pero leen `../business-plans-en-4/textos_es.json` más `textos_en/{GM,GR,GCAT-plan,GCAT-check}.json`, con `GR.revision.json` aplicado encima; `A_CAT = {'MBP':'CATP','MBC':'CATC'}`. `grupo_de`/`reuso_de` nuevos (abajo). Conviene fijar en el código el sha256 del diccionario para detectar si deriva |
| `datos_mbar.py` | copia de `datos_cat.py` (794 l.) | Contenido (§3-§7): es donde más trabaja el implementador |
| `bp5.py` · `fuente_mbar.py` · `barrido_mbar.py` · `calculadora_mbar.py` · `BRIEF-TRADUCTORES.md` | copias de `bp4.py` · `fuente_cat.py` · `barrido_cat.py` · `calculadora_cat.py` · brief | En `fuente_mbar.py`, el checklist ES de coctelería son **6 hojas**, no 1 (reescribir `checklist()`, ~20 l.); puede correr en el Mac |

El código común ya admite el mecanismo sin tocarlo. `extraer_textos.py:640-645` llama a los ganchos `grupo_de`/`reuso_de`.
`preparar_tandas.py:49-58` escribe los grupos que no son de traductores desde `e['reuso']['en']`. `:117-119` pone el EN del
catering como `propuesta_en`, y `:129-142` manda a revisión varios grupos reutilizados por tanda (`REVISAR_EN_TANDA`).

**Grupos propuestos y recuento.** El `textos_es.json` del catering tiene hoy 959 cadenas: GM **331**, GR 7, GCAT-plan 206,
GCAT-check 272 y GX **143**. No son 335/139 porque la ronda de arreglos pasó 4 de GM a GX (`F2-NOTAS.md` §9).

| Origen (catering) | n | → Grupo mbar | Qué es |
|---|---|---|---|
| GM sin vocabulario de comida | **322** | GM (tal cual) | Motor y finanzas genéricas |
| GM con comida | 9 | GMB-plan | `0. Supuestos!A11/C11/C12/A13/A15`, `PyG!A13/A15/A33/A52`: «FOOD share», «COGS — food», «Disposables», «Pest control» |
| GR | 7 | 5 GRC-plan · 2 GMB-plan | Revisar contexto |
| GCAT-plan texto libre | 82 | 27 GRC-plan · **55 GMB-plan** | Notas de Supuestos, Inversión, P&L y Personal |
| GCAT-plan D18 (método) | 68 | 62 GRC-plan · 6 GMB-plan | Fila 39 (comisaria), A43 (burner fuel), D49, C50 |
| GCAT-plan D19 (benchmarks) | 56 | **56 GMB-plan** sin propuesta | Tabla nueva desde el research US |
| GCAT-check (68 tareas × 4) | 272 | **GMB-check** con propuesta | ≈ 25 filas casi literales, ≈ 19 con cambio de palabras, ≈ 24 nuevas (§5) |
| GX (FIJOS, POR_CELDA, pestañas…) | 143 | GX | ≈ 45-50 a reescribir en `datos_mbar.py` (§3) |

**Carga de redacción:** GMB-plan **128 cadenas** (≈ 2.700 palabras EN; 72 con propuesta del catering) más revisión de
GRC-plan **94** (solo se devuelven las que cambian; se estima un 20 %). GMB-check 272 celdas (≈ 1.900 palabras nuevas).
Docx: **61 ranuras** (§6). El catering redactó 478 cadenas + 61 ranuras: esto es **−37 %** de cadenas a escribir.

**Regla para el checklist.** El reuso por celda solo vale si la **ranura conserva su tarea**. `TAREAS_MBAR` (copia de
`datos_cat.py:519`) debe dejar en su sitio las tareas del catering que sobreviven (§5) y meter las nuevas en las ranuras que
se liberan. Si no se hace así, la propuesta EN de esa celda sería la de otra tarea.

**`grupo_de` del mbar:** GX sigue como hoy · D19 o vocabulario prohibido (`RX_BAR_NO`, §7) en el ES del FT o en el EN del
catering → GMB-plan / GMB-check · GM del catering limpio → GM · resto del plan → GRC-plan · checklist entero → GMB-check.
`GRUPOS = ('GM','GRC-plan','GMB-plan','GMB-check')` (el GR del catering se reparte y desaparece),
`GRUPOS_TRADUCTORES = ('GMB-plan','GMB-check')`, `REVISAR_EN_TANDA = {'GMB-plan': ('GRC-plan',)}`.

## 2. Contenido ES aprovechable (9 ficheros) y nº de entregables

| Fichero ES (medido) | Vale para el EN | Solo España (fuera) |
|---|---|---|
| Plan docx · 150 párr., 6.962 pal., 10 H1, 0 tablas | Concepto [43], [49] (barra móvil en el espacio del cliente, sin local). Segmentos [50] (bodas, corporativo, cumpleaños, inauguraciones, despedidas). Propuesta de valor [52] («cero complejidad»: barra, bartender, cristalería, hielo). Modalidades de precio [53] (por hora, por invitado y hora, evento cerrado). Embudo B2B con planners, venues, fotógrafo y DJ [84], [86]. Operativa [94]: brief → mise en place D-1 → montaje 60-120 min → **1 bartender por 50 invitados** → servicio de 3-6 h → desmontaje de 45 min. Almacén de 15-25 m² [91]. Equipo [101]-[103]: fundador y bartender principal, red de 5-8 bartenders, runner a partir de 100 invitados. KPIs [133] | Mercado y cifras [42], [45], [56]-[60], [129] (INE, Bodas.net, «4.500 M»). Competidores españoles [65]. Autónomo, RETA, IAE 673.2, ICO, RGPD, normativa autonómica de alcohol [104], [115], [118]-[126]. Todas las cifras en € |
| Plan financiero xlsx · 6 hojas, **0 fórmulas** | Nombres de partidas (barra móvil, hielo, nevera, cristalería, kit de bar, decoración temática, LED, uniformes, consumibles) y de fijos (almacén, mantenimiento de la furgoneta, formación, reposición de cristalería). Comisión del 10 % a wedding planners. Estacionalidad mayo-sep + diciembre (solo la forma). Lista de ratios (sin las cifras) | Todos los importes, el caso (50 eventos × 1.400 €) y los ratios «España 2026» |
| Calculadora xlsx · 2 hojas, 13 fórmulas, 0 DV | Estructura coste → precio (§4): coste de bebida **por invitado y hora** en 3 niveles, bartenders y runners × tarifa × horas, hielo y consumibles por invitado, km, decoración repercutida, comisión del planner aplicada al precio, 3 niveles de precio | Tarifas en €, márgenes tecleados, «S/N» sin validación, hoja «10 ejemplos» tecleada (§8) |
| Checklist xlsx · 6 hojas, **71 tareas** (10/8/14/12/13/14) | 52 tareas adaptables (§5) | 7 solo España (§5) |
| Carta de 15 cócteles docx · 2.926 pal. + 15 tablas | Las 15 recetas (ml → oz: 60 ml = 2 oz, 30 ml = 1 oz), cristalería, consejos de batching, mocktail obligatorio, alérgenos (orgeat, coco) | Costes en €, «Cava», marcas españolas. Escalado erróneo (×½, §8) |
| 10 experiencias docx · 3.955 pal. | Las 10 temáticas con carta, props, música, luz, recargo (+15 % a +70 %) y público. Son el **diferencial**, como las estaciones temáticas del catering | «Mediterranean Sunset» como costa española; «Madrid/BCN» |
| Equipamiento docx · 1.186 pal. | Las categorías (barra, hielo, cristalería Tritan, furgoneta 5-8 años + adaptación) | Todos los proveedores, SKU y precios (GGM, Mewindo, SERHS, Makro…) |
| Contrato docx · 11 cláusulas | Cláusulas útiles para el contrato tipo (tarea P1): anticipo del 30 % a la firma + 50 % 7 días antes + 20 % después, cancelación por tramos de 60/30 días, variación de invitados ±10 %, toma eléctrica, derechos de imagen | Ley española, IVA del 21 %, Bizum, RGPD, juzgados |
| Proveedores xlsx · 96 + Hosply | Las 9 categorías como **lista de tipos** | Los 96 proveedores |

**¿4 o 5 ficheros? Cuatro.** El valor útil de la carta y del catálogo de equipamiento no está en el docx sino en el
cálculo: cuántas botellas, cuánto hielo y cuántos bartenders para X invitados y H horas. Eso se mete en la calculadora
como pestaña «Drinks & Shopping List», con la lista de compra que el bar entrega al cliente en el *dry hire*, más una tabla
«Signature Cocktail Specs» con 10-15 recetas en oz y el coste por copa a partir del precio de botella que teclee el usuario.
Cuesta ≈ 0,1-0,15 M de tokens: datos, fórmulas y el autotest que ya existe. Un 5.º docx (carta o equipamiento) costaría
≈ 0,3-0,4 M: generador nuevo sin circuito, 15 recetas redactadas, gate propio y una línea más en F3 (descargas, dashboard,
llms). Además, el catálogo de equipamiento caduca enseguida y habría que investigarlo entero para EE. UU. Las 10
experiencias entran en el docx §2 y §5 (D-concepto) y como recargo opcional («themed experience upcharge %») en la calculadora.

## 3. Delta del libro financiero (sobre el catering EN, celda a celda)

**Solo texto (GX, `datos_mbar.py`):**
- **Motor.** `FIJOS_NUEVOS` del motor (`datos_cat.py:42-58`) se reutilizan tal cual. Cambia solo el rótulo de B5: «Average price per guest (excl. sales tax; bar fees, staff and mixers included; client-supplied alcohol excluded)». En el *dry hire* el cliente paga el alcohol aparte, y las tarifas por hora se convierten a precio por invitado con la calculadora.
- **Títulos.** «BUSINESS PLAN: MOBILE BAR & EVENT BARTENDING», «Base case — mobile bar (dry hire)», «Break-even — Mobile Bar», «US MOBILE BAR BENCHMARKS (sourced) AND KIT ESTIMATES», «MOBILE BAR STARTUP CHECKLIST — …» y A3 del checklist.
- **Mezcla de ventas** (`0. Assumptions`):
  - A11/A12: «BAR SERVICE share (bartenders, bar rental, setup)» / «DRINK PACKAGES share (mixers, garnish, ice, NA drinks; alcohol only if licensed)».
  - A13/A14: COGS de cada línea.
  - A15: «Cups, straws, napkins and bar disposables».
  - A16/A17: **canal referido**, «Share of sales referred by planners / venues» y «Referral commission». El ES paga un 10 % a los wedding planners. La alternativa son los marketplaces de gigs (The Bash, GigSalad, Thumbtack): research.
  - A62/A63: alcohol **sobre las drink packages** (0 % en *dry hire*) y su impuesto (p. ej., el mixed beverage tax de TX).
  - A39/A40: sales tax de cada línea; si se grava el servicio de bartending depende del estado.
- **Inversión** (filas 7-20). La base de vida del vehículo (`B31` = 7+8+11+12+15+23) y la de equipo (`B32` = 9+10+16+17+20) no cambian:

| Fila | Base | Catering | → Bar móvil (propuesta; importes = research) |
|---|---|---|---|
| 7 · 8 | vehíc. | Furgoneta refrigerada · adaptación | Cargo van usada (o trailer bar) · adaptación: estanterías, sujeción de la barra, rotulación |
| 9 · 10 | equipo | Equipo de cocina · cocina portátil y energía | **Barra(s) portátil(es)** · energía e iluminación LED (batería o generador silencioso) |
| 11 · 12 | vehíc. | Unidad de frío · almacenaje en la comisaria | Rampa, enganche y protección de carga (o 0) · acondicionar el trastero o garaje (ES: almacén de 15-25 m²) |
| 13 · 14 | — | LLC · permisos del año 1 | LLC · permisos, licencias y certificaciones del año 1 (TIPS/RBS) |
| 15 | vehíc. | Health plan review | «License / health permit application (only if your state or county requires it)», por defecto 0 o research |
| 16 · 17 | equipo | Software + datáfono · menaje GN | Software de reservas y contratos + datáfono · **kit de bar** (shakers, jiggers, speed rails, pozos de hielo, coolers) |
| 18 · 19 | — | Inventario inicial · web y lanzamiento | Mixers, siropes, garnish y vasos iniciales · web, fotos y lanzamiento |
| 20 | equipo | Chafing y menaje de servicio | **Cristalería + kits de decoración temática** |

- **Fijos** (`3-Year P&L`): A22 «Storage unit / garage & van parking» (más la nota `C24` de Supuestos, el umbral A55 y su
  gemela `Instructions!A20`) · A24 «Utilities (phone, internet, storage power)» · A25 seguros = GL + **liquor liability** +
  commercial auto + inland marine · A26 «Annual permits and licenses» · A27 se queda · A31 «Cleaning and glass-washing
  supplies» · A32 «Glassware breakage and replacement» (ES: reposición de cristalería) · A33 «Continuing education and trade
  shows» (ES: formación y ferias) · A34 «Alcohol server certifications (TIPS / RBS / TABC)» · A35 «Cocktail tastings for
  couples and planners». Notas F22, F24, F32-F35 y F18 (`_F18_CAT`, fórmula con texto).
- **Personal** (`Staffing!A5:A8`, opción A heredada):
  - Puestos: owner / lead bartender & sales · senior bartender / bar lead · **event bartenders (hourly W-2)** · barbacks / driver. Con la E4 heredada, el pool de bartenders puede tener varias personas.
  - A18 «Hours per event to cover (load, travel, setup, service, breakdown)» y A19 «Bartenders and barbacks per event».
  - A24: nota W-2/AB5 más las reglas de propinas (FLSA: el empleador no puede quedarse las propinas).
- **Otros rótulos:** A44/A45 (vidas útiles), A51 «Max events a year your bars and crew can handle», A54 «Months of storage rent BEFORE opening», A55 (contingencia).
- **Fórmulas con texto:** `_PE_CAT`, `_C9_CAT` y `_F18_CAT` (`datos_cat.py:731-745`), y las listas de partidas de `_inversion` (`:756-760`).

**Valor (huecos que llena el research, `F1-research-us-delta.md`):** caso y mezcla (B4/B5/B6, B11-B18, B24-B28,
B39/B40/B62/B63, B58) · los 14 importes de inversión 7-20 · fijos B26-B35 · personal (B-D; horas y personas por evento,
ES: 1 bartender por 50 invitados) · escenarios B5:D7 · estacionalidad (fila 5 de Cash Flow, 12 valores, Month 1 = apertura)
· umbrales E51-E56 (margen bruto, «COGS / Sales» de bebida, personal, «Storage / Sales», neto) · escalones del
break-even `B31/D31/E31`: ±$10/+$20 puede ser demasiado si el *dry hire* por invitado es bajo → ±$5/+$10 según el B5 del
research (parche de valor, no estructural) · calibración D15 (holgura ≥ 15 %) y `PRESTAMO_SEMILLA`.
**Tabla D19** (14 filas, todo nuevo y con fuente): precio por invitado por paquete (*dry hire*, beer & wine, full bar) ·
tarifa por bartender y hora · ratio de bartenders por invitados · copas por invitado y hora · hielo por invitado ·
pour cost / liquor cost · primas de liquor liability y GL · inversión de arranque · coste de TIPS/RBS · anticipo y
mínimos · comisión de planners o marketplaces · sueldos.

## 4. Delta de la calculadora (`calculadora_mbar.py` sobre `calculadora_cat.py`)

**La ES (medida).** Entradas C5:C13 (invitados, horas, tipo, nivel 1-3, bartenders y runners extra, km, «S/N» del
planner, decoración) y parámetros F5:F13 (bebida por invitado y hora 2,5/4/6,5 €, bartender 22 €/h, runner 12 €/h,
consumibles 1,2 €, hielo 0,4 €, combustible 0,4 €/km, comisión del planner 12 %). Con 13 fórmulas da un precio mínimo,
recomendado y premium, **con márgenes tecleados** (35/45/55 %), y aplica la comisión del planner como `precio/(1−comisión)`.
**Vale la idea**: coste por invitado-hora, tres niveles y el planner aplicado al precio. **No valen** las tarifas, los
márgenes fijos, el «S/N» sin validación ni los ejemplos (§8).

**EN propuesta.** El motor de `calculadora_cat.py` se reutiliza: `ENTRADAS`/`SALIDAS`/`EJEMPLOS` son datos
(`:47-130`), y `hoja_calculadora`, `hoja_ejemplos`, `_dv`, `a_excel` y `autotest` no cambian. Cambian los datos y
`formula_sugerido` (`:168`), que pasa de servers por estilo a **bartenders por paquete**, más una pestaña nueva.

- **Entradas (verdes, con DV):**
  - Evento: invitados, **horas de servicio**, **paquete** (lista: «Dry hire (client buys alcohol)» / «Beer & wine (licensed)» / «Full bar (licensed)»), copas en la 1.ª hora y en las siguientes (Kit estimate).
  - Personal: bartenders y barbacks (con sugerencia por paquete), horas extra de montaje, viaje y desmontaje, $/h y cargas %.
  - Costes: mixers, garnish y NA por copa, coste medio del alcohol por copa (solo con licencia), vasos/cristalería por invitado, hielo (lb por invitado) y $/lb, **bar fee** fijo por evento, millas × $/milla, decoración o recargo temático %.
  - Precio y cobro: **referral commission %** (planner, como en el ES), margen objetivo, service charge %, sales tax %, ¿grava tu estado el service charge? (Yes/No), anticipo %, mínimo (invitados u horas) y precio de la hora extra.
- **Salidas:** copas estimadas, hielo en lb, coste directo, **precio por invitado** y equivalente **por hora**, subtotal, service charge, impuesto, total, anticipo, saldo y **margen calculado**. La propina voluntaria queda fuera.
- **Pestañas:** «Drinks & Shopping List» (copas por categoría según la mezcla, botellas de 750 ml de destilado ≈ 16 copas
  de 1,5 oz, vino 5 copas, cerveza, bolsas de hielo y la lista para el cliente) · «Signature Cocktail Specs» (10-15 recetas en
  oz con coste por copa) · «3 Example Quotes» (*dry hire* de boda, cóctel corporativo, fiesta privada con licencia, con la
  propia fórmula) · «Instructions».
- **Lo que fija el research (no inventar):** si el *dry hire* es legal y en qué condiciones, sales tax del servicio de bartending y del service charge por estado, regla de propinas, ratios de bartenders y copas por invitado y hora (o «Kit estimate»), lb de hielo por invitado y tarifa por milla.

## 5. Delta del checklist (68 = 11/13/12/10/12/10 sobre la rejilla del FT, ranuras `mapas_cat.py:89-90`)

**Mapeo del ES de coctelería** (71 tareas). Solo España, **7**: F1 7 (RETA y tarifa plana), F1 8 (SL / Ley Crea y Crece), F1 10 (FNMT),
F1 13 (registro autonómico de eventos), F2 8 (protección jurídica), F2 11 (RGPD) y F4 15 (factura electrónica 2026).
Reparto de las 64 restantes:

| Fase ES | Tareas | → Fase EN |
|---|---|---|
| F1 Constitución | 10 | P1 (5, 6 → LLC y EIN; 9 banco; 14 marca → USPTO) · P2 (11 permiso de alcohol → modelo legal) · P4 (12 manipulador) |
| F2 Seguros | 8 | P2 (5 RC → GL + liquor liability; 6/7 → inland marine; 9 → commercial auto) · P4 (10 PRL → OSHA) · P5 (12 aviso legal → privacy policy) |
| F3 Equipamiento y vehículo | 14 | P3 (5 barra, 6 hielo, 7 neveras, 8 cristalería, 9 kit, 10 decoración temática, 11 LED, 16 stock inicial, 17 consumibles, 18 inventario) · P2 (13-15 furgoneta: compra, adaptación, DMV) · P4 (12 uniformes) |
| F4 Marca y web | 12 | P5 (5-12, 16) · P1 (13 presupuesto y contrato; 14 CRM) |
| F5 Captación | 13 | P5 (5 → The Knot, 6 → WeddingWire, 7-16) · P6 (17 tres eventos piloto) |
| F6 Operativa 90 días | 14 | P6 (5-9, 11-15) · P1 (10 derechos de imagen → cláusula) · P5 (16) · P4 (18 formación) · 17 BCB → Bar Convent Brooklyn / Tales of the Cocktail (research) |

**Ranuras del catering que sobreviven** (filas del FT, reuso por celda):

| Fase | Sobreviven | Se sustituyen |
|---|---|---|
| P1 | 5-13 (contrato con cláusulas de alcohol) | 14-15 (HACCP, ServSafe Manager) → «elige tu modelo: *dry hire* o licencia» y marca |
| P2 | 11-15 (DMV, upfit, GL/COI, **liquor liability**, workers' comp) | 5-10 y 16-17 → reglas de alcohol del estado (ABC/TABC) para servicios de bartending, alquiler del trastero, health permit **solo si** el condado lo exige (hielo y garnish), permisos de eventos públicos (los pide el organizador), requisitos del venue, comprar la furgoneta o el trailer, inland marine, caterer's permit si se va con licencia |
| P3 | 12 y 16 (alquileres, dry run) | Resto → equipo del ES F3 |
| P4 | 5-9, 11-12 y 14 (con ajustes: ratio de bartenders, OSHA con cortes de cristal y cargas, propinas) | 10 y 13 → food handler según el estado / edad mínima para servir, y negativa a servir a menores y a ebrios |
| P5 | 5-8 y 10-16 (con ajustes) | 9 ezCater → The Bash / GigSalad / Thumbtack |
| P6 | 5-6 y 8-14 (con ajustes) | 7 → lista de compra al cliente en D-14 y compra de mixers, garnish y hielo en D-1 |

Total: ≈ 25 casi literales, ≈ 19 con cambio de palabras y ≈ 24 nuevas.

**Trámites US que entran** (los concreta el research): modelo legal del alcohol por estado, con la edad mínima para servir ·
certificación obligatoria de servidores (p. ej., RBS en CA o TABC en TX) · liquor liability · estatus sanitario de un bar
móvil (hielo de origen aprobado: el FDA Food Code considera alimento el hielo) · sales tax del servicio · propinas y pooling.

**Pestaña F2:** «Phase 2 - Licenses & Insurance» (30 caracteres) o «Phase 2 - Liquor Rules & Van» (28). Título de hoja
sin límite: «PHASE 2: LIQUOR RULES, LICENSES, INSURANCE & VAN».

## 6. Docx: 61 ranuras a redactar de 131 (H1 37…109; §9 = 102-108)

El EN del catering (`docx_en_cat_a/_b.json`, 6.409 palabras en las 61) sirve de **modelo por ranura**; el contenido sale del ES de coctelería (§2) y del research:

| Nivel | Ranuras | Palabras aprox. |
|---|---|---|
| Casi literal (tokens y método) | 42 · 56 · 58 · 90 · 93 · 95 · 97 · 99 · 117 | ≈ 880 |
| Adaptar el catering (mismo esqueleto, otro sustantivo) | 69-75 (§5: The Knot, GBP, venues, planners, reseñas, presupuesto) · 88 (W-2) · 94 · 96 · 98 · 106 · 107 · 108 (sales tax, empleo y seguros, DMV + nota UK: TENs, personal licence) · 112 · 114 · 115 | ≈ 1.700 |
| Nuevo | §1 39-41 y 43 · §2 46-50 (concepto, 10 experiencias, paquetes) · §3 53-55 y 57 · §4 61-66 (Porter y DAFO con la estructura del ES [68]-[76]) · §6 78-82 (operativa del ES [91]-[97]) · §7 85-87 y 89 · **§9 102-105 (el alcohol es el núcleo: *dry hire* frente a licencia, permisos, health permit, eventos públicos)** · §10 111, 113 y 116 | ≈ 3.800 |

Fijos del docx (`datos_cat.py:281-295`): portada «Mobile Bar», líneas 9 y 35 (anexos con los 4 ficheros). Hay que reescribir las 61 notas `DOCX_NOTAS` (`:297-442`).

## 7. Cifras y vocabulario prohibidos (gate: `CIFRAS_PROHIBIDAS` de `datos_mbar.py`, lo leen G2, `check_textos` y el barrido)

**Cifras del ES de coctelería.** Con `_num()`, solo números de 4 o más cifras: 40.030 · 25.580 · 18.000 / 35.000 (rango de inversión) · 70.000 · 112.500 ·
157.500 · 65.000 / 90.000 · 29.400 · 40.600 · 18.220 · 11.180 · 46.410 · 4.635 · 17.220 · 31.058 · 52.500 · 127.500 · 2.880 · 2.420. Los números pequeños van **como frase**, para no dar falsos positivos:
«31 events», «50 events a year», «2.6 events a month», «42% (gross) margin», «58% variable», «38% (safety) margin»,
«$/€1,400 per event», «$169 per hour», «12-18 per person», «4-7x», «4,500 million», «170,000 weddings», «96 suppliers»,
«71 (tasks|steps)», «10 (real|validated) examples».

**Cifras del caso catering EN** (reuso). Se aplica el patrón `_cifras_ft()` (`datos_cat.py:164`) a `../business-plans-en-4/cifras_caso.json`: los 29 importes ≥ 10.000 (648,000 · 745,200 · 819,720 · 185,453 · 146,000 · 107,200 · 78,253 · 94,276 · 48,466…) más «180 events», «$60 per guest» y «60 guests». Las del FT (`_cifras_ft`) se mantienen.

**Vocabulario: `RX_BAR_NO` = 0 en los 4 ficheros.**
- **Heredado del FT (D72):** food truck, truck, per day, operating days, customers (salvo corporate customers), window y festival(s). Si el research ve viables los festivales, se reabre.
- **Del catering de comida:** food (salvo «food handler card» si el research la exige), kitchen, commissary, chef/sous chef, prep cook, plated, buffet, drop-off, family-style, chef-attended / themed stations, chafing, hotel/sheet pans, recipe costing, food cost, boxed lunch, ezCater, broadline, HACCP, ServSafe Manager / Certified Food Protection Manager, servers (→ bartenders/barbacks), grease, pest control, «per plate».
- **Del ES:** España/Spain, Bodas.net, Zankyou, CateringClick, Hosply, GGM, Coalimentaria, Makro, IVA/VAT (salvo la nota UK), autónomo, ICO, RETA, EUR/€.
- **Lista blanca:** «Caterer's Permit» (nombre de licencia en TX y CA), «drink menu / cocktail menu», «bar station», «beverage catering» y «trailer» (el *trailer bar* es un formato US). El veto de «trailers?» del FT hay que levantarlo si el research lo adopta.

## 8. Deuda del ES (solo anotada; no se toca aquí)

1. **Inversión incoherente.** La landing dice «18-35K EUR» (ContentGrid y Why, `plan-negocio-cocteleria-eventos.ts:139,170`). El xlsx suma **40.030 €**, con una nota en su propia C30: «Rango típico 18.000-35.000». El catálogo da 25.580 €.
2. **Plan financiero sin modelo.** Tiene 0 fórmulas, sin cash flow ni hoja de financiación, mientras la landing promete «Listo para banco… plan de financiación… Formato ICO» (`:172`). La «estacionalidad de eventos» (`:125`) solo aparece como texto en A2. La columna E del P&L mezcla años: E34 11,6 %, E36 29,5 % y E40 19,7 % son del año 3, junto a cifras del año 1 (EBITDA real del año 1: 16 %).
3. **Break-even contradictorio.** xlsx: 31 eventos/año. Docx [45]: «meses 6-9». Docx [131]: «6-8 eventos». Escenarios C15: «10-12 meses». Testimonio: «mes 10».
4. **Escenarios.** Docx [114]: pesimista con 35 eventos, 52.500 € y resultado positivo. xlsx: 30 eventos, 33.000 € y EBITDA −4.360 €.
5. **Calculadora, «10 ejemplos reales» (`:140`).** Están tecleados y no salen de la calculadora. Con los valores por defecto (100 pax, 5 h, nivel medio, con planner) la calculadora da **5.165 € (51,65 €/pax)**. El ejemplo 2, con esos mismos parámetros, da 1.670 € (16,7 €/pax): unas 3 veces menos. Los márgenes también están tecleados.
6. **Carta de 15 cócteles, «escalado a 50/100/200».** El escalado está a la mitad: Old Fashioned de 60 ml × 100 = 6 L y la carta dice 3 L; Negroni de 30 ml × 100 = 3 L por ingrediente y dice 1,5 L.
7. **«Personal Freelance» B6:B9.** Las tarifas por hora están guardadas como **fechas** (1900-01-22 = 22 €/h).
8. **Erratas del docx.** «erforderida» [44] (alemán), «en lokasi» [94] (indonesio), «compared to» [53], «Debo señalar» [93], «gestoríasupone» [112], «cóctelera» / «prohibción».

## 9. Esfuerzo de F2 y riesgos

| Paso | Contenido | Tokens |
|---|---|---|
| Implementador opus (Mac + VPS) | Rama `mbar` en `mapas.py`; `mapas_mbar.py` (`_cargar_cat`, grupos); `datos_mbar.py` (≈ 50 GX, caso, 68 pistas de tarea, 14 de D19, 61 notas del docx, vocabulario); `bp5`/`fuente`/`barrido`; **calculadora** (3 pestañas nuevas) | ≈ 0,65 M |
| Tanda 1 (Sonnet ‖ Sonnet) | GMB-plan 128 + revisión GRC-plan 94 ‖ GMB-check 272 (≈ 43 filas nuevas o editadas) | ≈ 0,3 M |
| Tanda 2 (Sonnet ‖ Sonnet) | Docx `mbar_a` ‖ `mbar_b`: 61 ranuras, ≈ 5.500 palabras escritas o adaptadas | ≈ 0,3 M |
| Gates y revisión | G1-G9, `RX_BAR_NO`, cifras, autotests, regresión FT/CAF, REST/PAN, BAR, **CAT** y una revisión opus | ≈ 0,3 M |
| **Total** | Sin contar la F1. Regresión: el conjunto `cat` también, porque el diccionario lo lee | **≈ 1,55 M** (colchón 0,2 M) |

**Riesgos:**
1. **Modelo legal del alcohol.** Si el *dry hire* es legal o no, si un bar móvil necesita health permit o comisaria, y el sales tax del servicio y del service charge. Esto decide la P2, B11/B12/B62, los paquetes de la calculadora y el §9. Hay que fijarlo en la SPEC antes de los redactores (equivale al R2 del catering), con fuente estado a estado o «varies by state».
2. **Fuga de vocabulario de catering** por el reuso (322 GM, 94 GRC, propuestas del checklist): gate `RX_BAR_NO` con lista blanca y una lectura humana del checklist y de D18. Además, el diccionario no puede derivar: fijar los sha256 de arriba y, si el catering cambia, re-extraer.
3. **La calculadora es el mayor código nuevo** (*dry hire* / con licencia, lista de compra, recetas). Las heurísticas de copas, hielo y bartenders deben llevar fuente o «Kit estimate». El autotest tiene que recalcular las 3 pestañas. Y el precio por invitado del motor tiene que casar con la costumbre US de cotizar por hora: el B5 es el ingreso medio por invitado e incluye las tarifas por hora.

Menores: pestaña F2 de 31 caracteres · el checklist reutiliza por celda solo si `TAREAS_MBAR` respeta las ranuras que
sobreviven (§5) · las cifras pequeñas del ES solo se pueden vetar como frase · `PRODUCTOS_LETTER`
(`censo-entregables.py:153-157`) y `EXCLUIDOS` (`postprocess-transversal.py:97`) tienen que dar de alta
`mobile-bar-business-plan` antes de G9.
