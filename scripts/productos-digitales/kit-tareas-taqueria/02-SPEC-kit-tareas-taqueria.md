# SPEC (F1 · Fundamentos) — «Tareas Recurrentes: Taquería Mexicana»

**Fuente de datos**: `scripts/productos-digitales/kit-tareas-taqueria/01-research-taqueria-mexicana.md` (601 líneas).
**Qué es este documento**: las decisiones cerradas y el guion ejecutable. Los redactores de F2 **no habrán leído el research**: todo lo que necesitan está aquí.
**Fecha**: 2026-09-20 · **Máquina**: Mac (restricción térmica: solo lecturas, `grep`, `curl`/WebFetch, `unzip -p` sobre el XML del xlsx).

### Cómo leer las cifras

| Etiqueta | Significa |
|---|---|
| **[medido]** | Leído hoy en un fichero de este repo o en un `.xlsx` de `astro-site/public/dl/` (se cita `fichero:línea` o `producto/fichero.xlsx`) |
| **[fuente]** | Dato externo con URL, verificado |
| **[estimado]** | Criterio propio. No es un dato |

Ninguna cifra de este documento está inventada. Donde no hay dato, la celda dice **«a fijar por el operador»**.

---

## §0 Ficha

| Campo | Valor |
|---|---|
| **pid** | `kit-tareas-taqueria` |
| **Nombre de tarjeta** | Tareas Recurrentes: Taquería Mexicana |
| **Landing** | `/kit-tareas-taqueria` |
| **Precio** | **14 €** · `priceOld: '€69'` · `discountBadge: '-80%'` |
| **Familia** | Kits de tareas (kit nº 20; 19 LIVE) |
| **Tamaño** | **S** — 1 sesión, 3 cortes |
| **Cortes** | **F1** fundamentos (este documento) · **F2** entregables (11 xlsx) · **F3** lanzamiento (capa de producto) |
| **Techo de tokens** | **2,5 M** de subagentes para todo el producto. El research ya gastó 0,24 M → quedan ≈ 2,26 M |
| **Entregables** | 11 `.xlsx` en `astro-site/public/dl/kit-tareas-taqueria/` |

### Molde de generador para F2

Censo de generadores v1 de la familia (`ls scripts | grep -i tarea`, con la fecha del último commit de cada uno) **[medido]**:

| Generador | Ficheros que emite | Último commit |
|---|---:|---|
| `scripts/generate-tareas-restaurante.py` | — (sin `def gen_`) | 2026-03-19 02:54 |
| `scripts/generate-tareas-bar.py` | — | 2026-03-21 02:52 |
| `scripts/generate-tareas-pasteleria.py` | — | 2026-03-21 02:52 |
| `scripts/generate-tareas-catering.py` | 9 | 2026-03-21 23:23 |
| `scripts/generate-tareas-hotel.py` | 17 | 2026-03-22 03:54 |
| `scripts/generate-tareas-heladeria.py` | 9 | 2026-03-22 04:50 |
| `scripts/generate-tareas-chocolateria.py` | 9 | 2026-03-23 13:35 |
| `scripts/generate-tareas-chef-privado.py` | 9 | 2026-03-23 14:54 |
| **`scripts/generate-tareas-restaurante-creativo.py`** | **11** | **2026-03-23 17:12** |
| `scripts/generate-tareas-pasteleria-extras.py` | — (parche, no generador) | 2026-09-10 02:40 |

**`sushi-bar`, `asador`, `marisqueria` y `tapas-bar` NO tienen generador en el repo** (`ls scripts | grep -iE "sushi|asador|marisq|tapas"` → vacío) **[medido]**. Se construyeron fuera y sólo se publicaron los `.xlsx`.

> **Punto de partida de F2: `scripts/generate-tareas-restaurante-creativo.py`** (1.167 líneas), que se copia a `scripts/generate-tareas-taqueria.py`. Es el generador v1 **más reciente** y el **único que emite 11 ficheros** (`gen_01`…`gen_09` + `gen_bonus_01` + `gen_bonus_02`, líneas 343-1117) **[medido]**. Trae las **firmas** de las cuatro funciones de construcción que necesita el kit (`add_instructions_sheet`, `create_task_sheet`, `create_blank_template_sheet`, `create_calendar_sheet`), pero **NO emiten el molde v2.0 de §3.0**: hay que reescribirlas (ver contrato más abajo).
>
> 🔴 **Gotcha del molde**: su `OUTPUT_DIR` (`:14-17`) resuelve `dirname(dirname(__file__)) + "public/dl/…"` = `<repo>/public/dl/…`, ruta **anterior a la migración a Astro**. En F2 hay que apuntarlo a `astro-site/public/dl/kit-tareas-taqueria` o el kit se escribirá en una carpeta que no se publica **[medido]**.
>
> Su `PRODUCT_SUBTITLE` (`:108`) es `"AI Chef Pro · aichef.pro — Kit de Tareas: Restaurante Creativo / De Autor"`; para la taquería: `"AI Chef Pro · aichef.pro — Kit de Tareas: Taquería Mexicana"` **[medido]**.

**Para la ESTRUCTURA de los 11 ficheros** (nombres, orden, reparto de hojas) el molde es `astro-site/public/dl/kit-tareas-sushi-bar/`; **para la PROSA** (tildes, bloques de `Instrucciones` de v2.0, pie de AI Chef Pro) el molde es `astro-site/public/dl/kit-tareas/` (el kit base). Ver D6 y D14 — no son el mismo fichero y mezclarlos es el error que hay que evitar.

### 🔴 Contrato de helpers de `scripts/generate-tareas-taqueria.py` (se cierra ANTES de repartir contenido)

Medido contra `astro-site/public/dl/kit-tareas-sushi-bar/01-apertura-cierre-sushi.xlsx`: `create_task_sheet`, `create_blank_template_sheet` (`:217-270`) y `create_calendar_sheet` (`:271-300`) del generador v1 divergen del molde real en rótulos, orden, validación de datos, anchos, fila 2, panel congelado, numeración y pie. Con el generador v1 tal cual, `cabecera_checklist` del motor (`motor.py:765-780`) devuelve `None`, ninguna hoja entra en alcance, y G9/G11 quedan rojos. **Un único agente cierra este contrato reescribiendo las helpers ANTES de que se reparta contenido a los redactores**:

| Helper | Contrato exigido |
|---|---|
| `create_task_sheet` | Rótulos y orden exactos `Nº \| Tarea \| Zona \| Responsable \| Hora Límite \| ✓ Completada \| Firma`; DV `"✓,—,N/A"` (no `"✓,✗,—"`); anchos 5·48·14·20·13·12·16; fila 2 = `Fecha: ___/___/______  Turno: ☐…  Responsable: ___`; `ws.freeze_panes = "A5"` con cabecera en fila 4 (fila 3 vacía); **una sola cabecera por hoja** (no repetida por sección); numeración **continua** (no reiniciada por sección); fila `Tareas completadas: X de Y` + 5 filas verdes libres sin número en A; pie `— Kit de Tareas Recurrentes · Taquería Mexicana · AI Chef Pro · aichef.pro` |
| `create_blank_template_sheet` | Misma rejilla y misma DV que `create_task_sheet` (hoy trae la DV mala `"✓,✗,—"` en `:150`, `:237`, `:300`) |
| `create_calendar_sheet` | Molde calendario de B1: cabecera `Mes \| Fecha / Evento \| Tareas Clave \| Antelación` en fila 4 (fila 3 vacía), `freeze_panes = "A5"`, 24-36 filas |
| `add_instructions_sheet` | Los cinco bloques v2.0 de §3.0 (`Cómo usar estas plantillas` · `Cómo personalizar` · `Cómo cuenta el contador` · `Filas libres` · `Protección de la hoja`) |
| `PRODUCT_SUBTITLE` | `"AI Chef Pro · aichef.pro — Kit de Tareas: Taquería Mexicana"` |
| `OUTPUT_DIR` | `astro-site/public/dl/kit-tareas-taqueria/` |

**Validación del contrato**: comparar la estructura XML emitida (cabecera en fila 4, `ySplit`, lista de DV, anchos, pie) contra la del kit base (`kit-tareas/01-apertura-cierre.xlsx`, v2.0; el sushi-bar está en molde v1.1 de ChefBusiness) con `extraer_molde.py` / `comparar_molde.py`, ANTES de escribir una sola tarea de contenido. Ver también §7 R7.

### Motor de post-proceso

```
python3 scripts/productos-digitales/kit-tareas-v2_0/main.py --producto kit-tareas-taqueria --dry-run
KIT_TAREAS_APPLY=1 python3 scripts/productos-digitales/kit-tareas-v2_0/main.py --producto kit-tareas-taqueria
```

Módulo de contenido propio: **`scripts/productos-digitales/kit-tareas-v2_0/contenido_kit_tareas_taqueria.py`**
(el orquestador lo carga por convención `contenido_<pid con guiones bajos>.py`, `main.py:11-12`) **[medido]**.
Contrato: `post(wb, fname, cambios) -> bool` **[medido]**, `contenido_kit_tareas_sushi_bar.py:22-26`.
Sin `--dry-run` el script **aborta** salvo `KIT_TAREAS_APPLY=1` (`main.py:17-19`) **[medido]**.

---

## §1 Decisiones firmadas

### D1-D13 — tomadas por el orquestador (no se reabren)

| # | Decisión | Fuente |
|---|---|---|
| **D1** | **Precio 14 €** con `priceOld: '€69'` (par de la familia; el escalón de 12 € lleva `'€39'`). Motivo: tres capas técnicas propias —trompo, nixtamal/tortillería, barra de salsas— como sushi-bar, asador, marisquería y tapas-bar | `01-research…md:191-201`, `:342-357`, `:518-560` (precio) |
| **D2** | pid `kit-tareas-taqueria`, landing `/kit-tareas-taqueria`, tarjeta «Tareas Recurrentes: Taquería Mexicana», familia Kits de tareas, tamaño **S** (1 sesión, 3 cortes F1/F2/F3), techo **2,5 M** tokens | `01-research…md:1-4` |
| **D3** | Los 11 ficheros son los del §8 del research. El **02 se llama «trompo, plancha y comal»** y su bloque de trompo va marcado **«(si aplica)»**: muchas taquerías españolas no tienen asador vertical | `01-research…md:262-273`, `:566` (si aplica) |
| **D4** | Umbrales legales: RD 1021/2022 (caliente **≥ 63 °C**; recalentado **≥ 74 °C/15 s** en el centro, en el término de 1 h; art. 8 **−20 °C/24 h** o **−35 °C/15 h**) + guía de kebab de ACSA para el trompo (cono **≤ −18 °C** congelado / **≤ 4 °C** refrigerado, expositor **≤ 4 °C**, sonda al inicio y a mitad del servicio; cocinado AESAN **70 °C/1 s**). **Ninguna fuente fija tiempo máximo de cono montado ni vida útil del fileteado: el kit deja la celda para el operador** | `01-research…md:283-322`; BOE verificado, ver §2 |
| **D5** | **Registro horario**: «registro de jornada (obligatorio; en el soporte que exija la normativa vigente)». **NUNCA** «registro horario digital obligatorio en 2026» | `01-research…md:356-363` |
| **D6** | **Español correcto con tildes** en todas las celdas. Sin caracteres no latinos | Orden del orquestador; ver D14 |
| **D7** | Glosar en la primera aparición de cada fichero: «trompo (asador vertical)», «tortillería (obrador de tortilla de maíz)», «guisados (cazuelas de relleno)», «salsero/a (responsable de salsas)», «APPCC (HACCP)», «escandallo (costeo)». Prohibido: «tex-mex», «gyro» como sinónimo, burrito/nachos como plato de taquería, «tortilla» a secas, importes en pesos | `01-research…md:495-522` |
| **D8** | Calendario (08 y BONUS-02): Candelaria, Cuaresma/Vigilia, chiles en nogada 15-jul→fin de sep, Grito 15/16-sep, Día de Muertos 1-2 nov, Guadalupe 12-dic, posadas 16-24 dic, Navidad/Nochevieja, **Cinco de Mayo presentado como fiesta sobre todo estadounidense**. Más campañas españolas (terrazas de verano, comidas de empresa de Navidad) | `01-research…md:426-440` |
| **D9** | Posicionamiento frente al BONUS 2 «Manual de Operaciones Mexicano» (39 €) de `guia-restaurante-mexicano`: **«las hojas que ejecutan ese manual, turno a turno»**. Cross-links en las DOS direcciones, alta en la cesta del caso de uso `restaurante-mexicano` y enlaces desde el pSEO de ciudades mexicanas (72 clics/90 días) | `01-research…md:212-218`, `:148-163` |
| **D10** | El **BONUS-02 «calendario anual de tareas»** sube al `title`/`h2` de la landing: es la única consulta no-marca con tracción de toda la familia (`/kit-tareas` pos. 8,8, 0 clics) | `01-research…md:178-185` |
| **D11** | **El Mega Pack queda fuera** (congelado en 13 kits) | `01-research…md:248-255` |
| **D12** | Alérgenos del formato: salsa macha (cacahuete y/o sésamo) a granel en barra de autoservicio · tortilla de harina (gluten) frente a maíz (sin gluten) con freidora/pinzas/superficie separadas · lácteos (crema, queso) · moles con frutos de cáscara. Reglamento (UE) 1169/2011 + RD 126/2015 | `01-research…md:341-354` |
| **D13** | Perfiles del 06: **taquero/a, tortillero/a, salsero/a, plancha y freidora, mostrador y caja, repartidor/delivery**. Los seis se sostienen en el research | `01-research…md:404-415` |

**Nota sobre D13** — el research (`:415`) deja dos opciones: 6 hojas, o fundir «Plancha y freidora» con «Mostrador y caja» para quedarse en 5 y parecerse al sushi-bar (4 perfiles). **Se mantienen los 6.** Razón: el 06 del sushi-bar tiene 4 hojas de 10/8/6/9 tareas **[medido]** y el molde admite más sin tocar nada; y fundir plancha con caja mezclaría una partida de cocina con un puesto de sala, que es justo lo que hace inservible una hoja de perfil. El **repartidor/delivery** lleva en su cabecera «(si aplica)» como el trompo.

### D14-D20 — decisiones nuevas de esta SPEC

| # | Decisión | Justificación |
|---|---|---|
| **D14** | 🔴 **En los `.xlsx` el espacio antes de la unidad y del grado es ESPACIO NORMAL (U+0020), NO espacio fino U+202F.** El U+202F sólo se usa en el `.md` / copy de la landing de F3 | `motor.py:645` lo dice literalmente: *«(`0-4 °C`, `0,05 €`): el espacio fino U+202F es de los .md ensamblados»*. Y `motor.py:2415` normaliza con `RX_GRADOS.sub(' °C', v)` — **espacio normal**. Si F2 escribe U+202F, el motor lo reescribe en la 1.ª pasada, la 2.ª pasada ya no lo ve y **el gate de idempotencia se pone rojo sin que haya nada roto de verdad**. Verificado contra el kit base LIVE: `kit-tareas/01-apertura-cierre.xlsx` dice `refrigeración 0-4 °C / congelación ≤ −18 °C` con espacio normal **[medido]** |
| **D15** | **El signo menos de las temperaturas negativas es U+2212 (`−`), no el guion `-`.** `−18 °C`, `−20 °C`, `−35 °C` | El motor lo normaliza (`motor.py:235`, `:1143`, `:2415`) y así está en el kit base LIVE **[medido]** |
| **D16** | **El molde de PROSA es el kit base `kit-tareas`, no el sushi-bar.** Censo de los 19 kits LIVE en `astro-site/public/dl/` **[medido]**: 13 llevan tildes y pie de AI Chef Pro; **6 no llevan tildes** (asador, food-truck, marisquería, panadería, sushi-bar, tapas-bar) y **2 de ellos (sushi-bar y asador) llevan el pie «ChefBusiness Consultoría Gastronómica · chefbusiness.co» dentro de un producto de aichef.pro**. El research dedujo «la familia va sin tildes» mirando sólo esos dos | Esto **cierra D6 sin conflicto**: escribir con tildes pone a la taquería con la mayoría (13 de 19), no en la excepción. Deuda ajena → §7 |
| **D17** | **NO se añade `kit-tareas-taqueria` a `SUBFAMILIA_CB`** (`motor.py:4495-4498`) | Ese `frozenset` activa `sub_cb()`, el gate de 11 puntos del motor propio de la sub-familia ChefBusiness (`motor.py:156, 1263, 1367, 1369, 2036, 2152, 2286, 2293, 4129, 4216, 4303, 4767`), entre ellos `ortografia()` (barrido de tildes, `:4744-4774`). La taquería **nace ya con tildes**, así que no necesita el barrido. Los gates `promesas` / `limite_unico` / `PLANTILLA_09` **no** los activa `SUBFAMILIA_CB`: los activa `main.py` por `getattr` sobre el módulo de contenido (`contenido_kit_tareas_sushi_bar.py:30-34`); no añadir la taquería a `SUBFAMILIA_CB` sigue siendo la decisión correcta, sólo cambia la razón. El motor detecta columnas **comparando sin tildes** desde esa misma tanda (`motor.py:4756-4759`), así que «Hora Límite» con tilde **se reconoce igual** |
| **D18** | **Objetivo total: 300 tareas numeradas (rango aceptable 270-330)**, repartidas en las 22 hojas de checklist de los ficheros 01-08. El 09 aporta 15 filas numeradas **en blanco** y el BONUS-02 24-36 filas de calendario (B1), y **ninguno de los dos cuenta** | Recuento real de filas con entero en `A` y texto en `B` (no las filas numeradas vacías): `kit-tareas-sushi-bar` **211** (no 266), `kit-tareas-asador` **223** (no 238), `kit-tareas` (base, 9 ficheros de contenido) **522** (no 567) **[medido]**. Densidad de la familia: **13-15 tareas por hoja**. La taquería lleva 6 perfiles (frente a 4 del sushi-bar) y 3 capas técnicas: tiene que quedar por encima del sushi-bar y muy por debajo del base |
| **D19** | **El 08 lleva las hojas en el orden de la familia: `Temporadas y Producto` primero, `Calendario de Eventos` después.** El research las proponía al revés | En `kit-tareas-sushi-bar/08-eventos-estacionales.xlsx` el orden real es `Instrucciones` → `Temporadas Pescado Espana` → `Eventos Especiales` **[medido]**. Se respeta el molde |
| **D20** | **El kit no imprime ni un importe.** Ni euros ni pesos. Donde el research menciona «ticket medio» o «escandallo», la hoja pide la **acción** («revisar el escandallo (costeo) de los 5 tacos más vendidos»), nunca la cifra | Los precios cambian y el kit es de tareas; la regla de la casa prohíbe duplicar precios fuera de `products-catalog.ts`. Además `01-research…md:517` prohíbe los importes en pesos |

---

## §2 Umbrales y datos duros

Verificación del **RD 1021/2022** hecha hoy contra el BOE, texto consolidado
**[fuente: https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681]**. Título literal: *«Real Decreto 1021/2022, de 13 de diciembre, por el que se regulan determinados requisitos en materia de higiene de la producción y comercialización de los productos alimenticios en establecimientos de comercio al por menor»*. Su **disposición derogatoria única** deroga 8 normas, entre ellas el **RD 3484/2000** (comidas preparadas), el RD 1376/2003, el RD 1254/1991 y el RD 1420/2006 (anisakis) **[fuente, verificado]**.

Frases literales verificadas **[fuente: BOE, texto consolidado]**:

- **Art. 30.2**, caliente: *«se servirán para su consumo cuanto antes, a menos que se refrigeren, congelen o **se mantengan a una temperatura superior o igual a 63 °C**»*.
- **Art. 30**, recalentado: *«se recalentarán de tal manera que deberá alcanzarse una temperatura de **por lo menos 74 °C durante al menos quince segundos en el centro del alimento, en el término de una hora** desde que se han retirado del frigorífico»*.
- **Art. 30**, refrigeración: *«4 °C si su vida útil es superior a veinticuatro horas»* · *«8 °C si su vida útil es inferior a veinticuatro horas»*. Congelación: *«temperatura interna igual o inferior a −18 °C»*.
- **Art. 8**, pesca: *«han sido congelados a una temperatura igual o inferior en la totalidad del producto de: a) −20 °C durante un mínimo de veinticuatro horas o b) −35 °C durante un mínimo de quince horas»*.

| # | Magnitud | Valor | Fuente | Dónde se imprime |
|---|---|---|---|---|
| U1 | Mantenimiento en **caliente** (baño maría de guisados, carne cortada del trompo) | **≥ 63 °C** | RD 1021/2022, **art. 30.2** [fuente, verificado en BOE hoy] | `01` Apertura y Cierre · `02` Corte · `03` Temperaturas · `04` Guisados · `05` Diarias |
| U2 | **Recalentado** de guisados | **≥ 74 °C durante ≥ 15 s en el centro, en el término de 1 hora** desde que sale del frigorífico | RD 1021/2022, **art. 30** [fuente, verificado] | `03` Temperaturas · `04` Guisados |
| U3 | **Refrigeración**, vida útil > 24 h | **≤ 4 °C** | RD 1021/2022, art. 30 [fuente, verificado] | `01` · `02` Marinado · `03` Temperaturas y Barra de Salsas |
| U4 | **Refrigeración**, vida útil ≤ 24 h | **≤ 8 °C** | RD 1021/2022, art. 30 [fuente, verificado] | `03` Barra de Salsas (nota de la hoja) |
| U5 | **Congelación** de conservación | **≤ −18 °C** | RD 1021/2022, art. 30 [fuente, verificado] | `01` · `03` Temperaturas |
| U6 | **Congelación preventiva** de pescado que se sirve crudo (aguachiles, ceviches, tostadas de atún, camarón crudo) | **−20 °C / ≥ 24 h** o **−35 °C / ≥ 15 h**, en la totalidad del producto | RD 1021/2022, **art. 8** [fuente, verificado] | `03` Temperaturas y Trazabilidad |
| U7 | **Cono del trompo** en recepción y conservación | **≤ −18 °C** si congelado · **≤ 4 °C** si refrigerado | ACSA, *Buenas prácticas en la elaboración de kebab* [fuente: https://acsa.gencat.cat/es/Publicacions/guies-i-documents-de-bones-practiques/documents-de-bones-practiques/bones-practiques-en-lelaboracio-de-kebab/index.html] | `02` Marinado y Montaje |
| U8 | **Salsas y vegetales crudos** en nevera y en **expositor** | **≤ 4 °C** | ACSA, misma guía [fuente] | `01` Apertura · `03` Barra de Salsas |
| U9 | **Sonda** en el asador vertical | Obligatoria; **al inicio y a mitad del servicio como mínimo** | ACSA, misma guía [fuente] | `02` Corte · `03` Temperaturas |
| U10 | **Cocinado** de la superficie de corte (carne) | **70 °C durante ≥ 1 s** en el centro | AESAN, *Informe del Comité Científico sobre combinaciones tiempo-temperatura* [fuente: https://www.aesan.gob.es/AECOSAN/docs/documentos/seguridad_alimentaria/evaluacion_riesgos/informes_comite/TIEMPO-TEMPERATURA.pdf] | `02` Corte |
| U11 | **Cocinado** de aves (pollo del trompo mixto, tinga) | **74 °C durante ≥ 1 s** | AESAN, mismo informe [fuente] | `02` Corte · `04` Guisados |
| U12 | **Tiempo máximo de cono montado** | **a fijar por el operador** — casilla «hora límite definida en tu APPCC: ______» | **Ninguna fuente lo fija.** Declarado expresamente en `01-research…md:318` | `02` Marinado y Montaje |
| U13 | **Vida útil de la carne ya fileteada** | **a fijar por el operador** | Ninguna fuente lo fija (`01-research…md:318`) | `02` Corte |
| U14 | **Vida útil de la masa nixtamalizada** | **a fijar por el operador** — la hoja pide hora de molienda, temperatura de conservación y hora límite | No hay normativa española específica; la literatura técnica es de laboratorio y con conservadores, no vale para una hoja de trabajo (`01-research…md:336-339`) | `04` Nixtamal y Molienda |
| U15 | **Marinado del pastor** | **[estimado]** tiempo a fijar por el operador en su ficha (práctica de oficio: 12-24 h orientativas), siempre a ≤ 4 °C | Ninguna fuente fija el tiempo; `01-research…md:388` es orientativo (ciclo productivo). La temperatura es U3 | `02` Marinado y Montaje |
| U16 | **Alérgenos de declaración obligatoria** | **14**, información gratuita y accesible, por escrito o de forma oral con soporte escrito verificable | Reglamento (UE) 1169/2011 + **RD 126/2015** [fuente: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2015-2293] | `03` Alérgenos · `BONUS-01` |
| U17 | **Registro de jornada** | Obligatorio para todas las empresas desde 2019; no tenerlo es infracción **grave** | **Art. 34.9 ET**, introducido por el **RD-ley 8/2019**. El repo ya lo cita bien: `src/pages/KitGestionPersonal.tsx:70` **[medido]** | `05` Semanales Manager |
| U18 | **Registro horario DIGITAL** | **NO es obligatorio todavía.** El RD seguía sin publicarse en el BOE a mediados de 2026 | `01-research…md:359` [fuente: medio especializado, **no oficial**]. **[no verificado contra el BOE en esta SPEC, pendiente F2]** — la redacción de D5 está construida para ser correcta en los dos escenarios | Ninguna hoja afirma nada sobre el soporte |

> ⚠️ **La cifra de 65 °C está DEROGADA.** Procede del RD 3484/2000, que el RD 1021/2022 derogó con efectos de 22-dic-2022. Cualquier hoja de este kit que diga «65 °C» en contexto de mantenimiento en caliente es un defecto (gate G2 del §5). La cifra vigente es **63 °C**, y el recalentado es **74 °C/15 s**, no «65 °C en el centro».

---

## §3 Guion de los 11 ficheros

### 3.0 El molde, medido

Estructura verificada en `astro-site/public/dl/kit-tareas-sushi-bar/` y en `astro-site/public/dl/kit-tareas/` **[medido]**:

- Cada `.xlsx` abre con una pestaña **`Instrucciones`** y luego 1-6 pestañas de contenido. **Los nombres de pestaña no pasan de 31 caracteres y no llevan `/`** (Excel los corta). `censo-entregables.py:214` (`hoja_larga`) es sólo informativo y no comprueba la `/`; **el único gate de nombres de pestaña es G9**.
- Cabecera de hoja de checklist (fila 2): `Fecha: ___/___/______    Turno: ☐ Almuerzo  ☐ Cena    Responsable: _________________________`
  Variantes reales: semanal → `Semana del ___/___/______ al ___/___/______    Manager: _________________________`; anual → `Año: ______    Taquería: _________________________` **[medido]**.
- **Columnas de toda hoja de checklist** (fila 4, con la fila 3 vacía): `Nº | Tarea | Zona | Responsable | Hora Límite | ✓ Completada | Firma`
  Anchos del molde: 5 · 45 · 12 · 18 · 12 · 12 · 15 **[medido]** sobre `kit-tareas/01-apertura-cierre.xlsx` (kit base v2.0, molde CANÓNICO; los 5 · 48 · 14 · 20 · 13 · 12 · 16 del sushi-bar son del molde v1.1 de ChefBusiness, sin tildes ni protección). Contrato completo y volcados: `03-contrato-molde-v2.md`, `molde-referencia-base.json`.
- Las tareas se agrupan bajo **secciones en MAYÚSCULAS con dos espacios de sangría** (`  TEMPERATURAS Y EQUIPOS`). Las secciones no llevan número.
- **Panel congelado** en la fila 4 (`ySplit="4"`) **[medido]**.
- `✓ Completada` lleva **validación de datos con la lista `"✓,—,N/A"`** (`motor.py:168`) **[medido]**. `N/A` sale del total; `—` cuenta como pendiente.
- Al final de cada tabla van **5 filas verdes libres DENTRO del rango del contador** (`kit-tareas/01-apertura-cierre.xlsx`, bloque «Filas libres» de `Instrucciones`) **[medido]**.
- La hoja `Instrucciones` del kit base v2.0 lleva **cinco bloques**: `Cómo usar estas plantillas` · `Cómo personalizar` · `Cómo cuenta el contador` · `Filas libres` · `Protección de la hoja`, y cierra con el pie `— Kit de Tareas Recurrentes · Taquería Mexicana · AI Chef Pro · aichef.pro` **[medido]** (el segmento del kit es idéntico en los 11 ficheros, `ctx['kit'] = _mayoria(kits)`, `motor.py:1777-1779`). **Los cinco son obligatorios** en la taquería (D16).

**Tres ficheros NO llevan la rejilla de checklist** **[medido]**:

| Fichero | Formato real |
|---|---|
| `09-plantilla-personalizable` | Misma rejilla de 7 columnas, **vacía**, con 3 secciones `  SECCIÓN 1 (PERSONALIZAR)` … y 15 filas numeradas en blanco |
| `BONUS-01-briefing-servicio` | **Formulario**, no checklist: pares `etiqueta: ______` en dos columnas, sin `Nº` ni `Firma` por fila |
| `BONUS-02-calendario-anual` | **Molde calendario** (no matriz, B1): fila 1 título, fila 2 `Año: ______`, fila 3 vacía, fila 4 cabecera `Mes \| Fecha / Evento \| Tareas Clave \| Antelación`, panel congelado en fila 4 |

### 3.1 Reparto de tareas (D18)

| # | Fichero | Hoja | Tareas objetivo |
|---:|---|---|---:|
| 01 | `01-apertura-cierre-taqueria.xlsx` | Apertura Taquería | 26-31 |
| 01 | | Cierre Taquería | 20-24 |
| 02 | `02-trompo-plancha-comal.xlsx` | Marinado y Montaje del Trompo | 16-20 |
| 02 | | Corte, Plancha y Comal | 16-19 |
| 03 | `03-appcc-salsas-alergenos.xlsx` | Temperaturas y Trazabilidad | 16-20 |
| 03 | | Barra de Salsas | 14-16 |
| 03 | | Alérgenos y Cruzada | 14-16 |
| 04 | `04-nixtamal-tortilla-guisados.xlsx` | Nixtamal y Molienda | 14-16 |
| 04 | | Tortilla y Comal | 10-12 |
| 04 | | Guisados y Rotación | 12-14 |
| 05 | `05-tareas-manager.xlsx` | Tareas Diarias Manager | 13-16 |
| 05 | | Tareas Semanales Manager | 9-12 |
| 06 | `06-tareas-perfiles.xlsx` | 6 hojas de perfil | 7-9 cada una (42-54) |
| 07 | `07-semanales-mensuales.xlsx` | Tareas Semanales | 13-16 |
| 07 | | Tareas Mensuales | 11-14 |
| 08 | `08-eventos-estacionales.xlsx` | Temporadas y Producto | 11-14 |
| 08 | | Calendario de Eventos | 13-16 |
| | | **TOTAL numeradas** | **270-330 · objetivo 300** |
| 09 | `09-plantilla-personalizable.xlsx` | Plantilla en Blanco | 15 filas **en blanco** (no cuentan) |
| B1 | `BONUS-01-briefing-servicio.xlsx` | Briefing Pre-Servicio | formulario (no cuentan) |
| B2 | `BONUS-02-calendario-anual.xlsx` | Calendario Anual | 24-36 filas (2-3 por mes; no cuentan) |

---

### 01 · `01-apertura-cierre-taqueria.xlsx`

Hojas: `Instrucciones` · `Apertura Taquería` (17 car.) · `Cierre Taquería` (15 car.).

#### Hoja `Apertura Taquería` — 26-31 tareas
**Propósito**: dejar la taquería lista para servir, con las temperaturas registradas y la barra de salsas montada en frío.
Secciones: `  TEMPERATURAS Y EQUIPOS` · `  TROMPO, PLANCHA Y COMAL` · `  SALSAS Y GUARNICIONES` · `  TORTILLA Y GUISADOS` · `  SALA, MOSTRADOR Y DELIVERY`.
Glosa obligatoria en la primera tarea que lo mencione: **trompo (asador vertical)**.
Ejemplos redactados en forma final:

1. `Registrar temperatura de la cámara de carne marinada (≤ 4 °C) — anota la lectura: ____ °C`
2. `Registrar temperatura del congelador (≤ −18 °C) — anota la lectura: ____ °C`
3. `Encender el trompo (asador vertical) y comprobar llama uniforme en todos los quemadores`
4. `Montar el trompo del día: orden de capas, grasa, piña y cebolla; anotar peso y hora`
5. `Calibrar plancha y comal por zonas (alta y media) y anotar la temperatura de trabajo`
6. `Sacar las salsas crudas a la barra fría y comprobar ≤ 4 °C antes de abrir`
7. `Verificar que el cartel de alérgenos está visible y marca la salsa macha (cacahuete y/o sésamo)`
8. `Poner los guisados (cazuelas de relleno) en baño maría y comprobar ≥ 63 °C`

**Celdas para el operador**: la lectura `____ °C` de cada temperatura · la hora y el peso del montaje del trompo. `Responsable` y `Hora Límite` vienen con el puesto y la hora sugeridos (§4); lo editable es sobrescribirlos.

#### Hoja `Cierre Taquería` — 20-24 tareas
**Propósito**: cerrar con el destino de cada producto registrado y los equipos críticos limpios.
Secciones: `  TROMPO Y PLANCHA` · `  SALSAS Y GUISADOS` · `  LIMPIEZA Y RESIDUOS` · `  CAJA Y CIERRE DE NEGOCIO`.
Ejemplos:

1. `Apagar el trompo (asador vertical) al cierre`
2. `Retirar la carne sobrante y registrar su destino: abatida o descartada`
3. `Vaciar, lavar y desinfectar la bandeja de grasas del asador vertical`
4. `Descartar las salsas crudas del día y anotar la merma en litros`
5. `Abatir el guisado apto y etiquetarlo con fecha y hora`
6. `Descartar el guisado no apto`
7. `Rascar y engrasar la plancha en caliente; limpiar el comal antes de que enfríe`
8. `Hacer el arqueo de caja`
9. `Cerrar el canal de delivery`
10. `Repartir las propinas del turno`
11. `Revisar que la hoja de temperaturas del turno queda firmada y archivada`

---

### 02 · `02-trompo-plancha-comal.xlsx`

Hojas: `Instrucciones` · `Marinado y Montaje del Trompo` (29 car.) · `Corte, Plancha y Comal` (22 car.).

> **«(si aplica)» (D3)**: la hoja `Marinado y Montaje del Trompo` abre con una tarea-aviso y la sección de trompo va marcada. Quien no tenga asador vertical usa la segunda hoja completa para plancha y comal. La nota va en `Instrucciones`: *«Si tu taquería no tiene trompo (asador vertical), marca N/A las tareas de la sección TROMPO: salen del total y el porcentaje sigue siendo honesto.»*

#### Hoja `Marinado y Montaje del Trompo` — 16-20 tareas
**Propósito**: trazar el pastor desde el adobo hasta el cono montado, con peso y hora.
Secciones: `  MARINADO (VÍSPERA)` · `  MONTAJE DEL TROMPO (SI APLICA)` · `  RENDIMIENTO`.
Ejemplos:

1. `Pesar carne y adobo por lote; anotar número de lote y hora de inicio del marinado`
2. `Mantener el marinado a ≤ 4 °C el tiempo definido en tu ficha: ______ h`
3. `Remover el lote a mitad del marinado y anotar la hora`
4. `Comprobar el cono recibido: ≤ −18 °C si congelado, ≤ 4 °C si refrigerado`
5. `Montar el trompo (asador vertical): capas, grasa, piña y cebolla; anotar peso total`
6. `Anotar la hora de montaje y la hora límite definida en tu APPCC (HACCP): ______`
7. `Esperar a que la capa exterior esté cocinada antes del primer corte`
8. `Anotar el peso sobrante al cierre y calcular el rendimiento en tacos por kilo`

**Celdas para el operador**: peso de carne y de adobo · número de lote · **tiempo del marinado (U15: [estimado], práctica de oficio; ninguna fuente lo fija)** · hora de montaje · **hora límite del cono montado (U12: ninguna norma la fija)** · rendimiento del día.

#### Hoja `Corte, Plancha y Comal` — 16-19 tareas
**Propósito**: que sólo salga carne que ha alcanzado temperatura y que nada cortado se quede a ambiente.
Secciones: `  SONDA Y CORTE (SI APLICA)` · `  PLANCHA` · `  COMAL` · `  CONTAMINACIÓN CRUZADA`.
Ejemplos:

1. `Sondar la capa exterior antes de cada tanda de corte — anota la lectura: ____ °C (≥ 70 °C)`
2. `Registrar la sonda al inicio y a mitad del servicio, como mínimo`
3. `Cortar sólo la capa cocinada; no rebanar hacia el interior todavía crudo`
4. `Pasar a mantenimiento ≥ 63 °C la carne cortada que no se sirve al momento; nunca a ambiente`
5. `Anotar la hora límite del fileteado definida en tu APPCC (HACCP): ______`
6. `Limpiar cuchillo y tabla del trompo antes de tocar producto listo para consumo`
7. `Comprobar la temperatura de trabajo de la plancha por zonas y anotarla`
8. `Registrar las mermas de tortilla del comal por turno`

---

### 03 · `03-appcc-salsas-alergenos.xlsx`

Hojas: `Instrucciones` · `Temperaturas y Trazabilidad` (27 car.) · `Barra de Salsas` (15 car.) · `Alérgenos y Cruzada` (19 car.).

> Nombre de la tercera pestaña: **`Alérgenos y Cruzada`**. «Alérgenos y Contaminación Cruzada» son 34 caracteres y Excel lo cortaría.
> Glosa obligatoria en la primera aparición: **APPCC (HACCP)**.

#### Hoja `Temperaturas y Trazabilidad` — 16-20 tareas
**Propósito**: la hoja que pide el inspector. Todas las temperaturas del día y el origen de cada lote.
Secciones: `  TEMPERATURAS (2 VECES POR TURNO)` · `  RECEPCIÓN Y TRAZABILIDAD` · `  CONGELACIÓN DE CRUDOS (SI APLICA) Y RECALENTADO`.
Ejemplos:

1. `Registrar cámaras de refrigeración (≤ 4 °C) dos veces por turno — anota la lectura: ____ °C`
2. `Registrar el congelador (≤ −18 °C) dos veces por turno — anota la lectura: ____ °C`
3. `Registrar el baño maría de guisados (≥ 63 °C) dos veces por turno`
4. `Registrar la barra fría de salsas (≤ 4 °C) dos veces por turno`
5. `Anotar lote y proveedor de la carne de pastor, de la masa o tortilla y de los chiles secos`
6. `Registrar cada recepción: temperatura, estado del envase, caducidad y número de albarán`
7. `Verificar la congelación del pescado crudo de aguachiles y tostadas: −20 °C/24 h o −35 °C/15 h`
8. `Recalentar los guisados a ≥ 74 °C durante 15 s en el centro, en menos de 1 hora`

**Celdas para el operador**: todas las lecturas `____ °C` · lote, proveedor y albarán · la acción correctora si hay desviación.

#### Hoja `Barra de Salsas` — 14-16 tareas
**Propósito**: el punto de mayor riesgo del formato. Hora de puesta y hora de descarte de cada salsa, siempre las dos.
Secciones: `  MONTAJE DE LA BARRA` · `  REPOSICIÓN POR TANDAS` · `  DESCARTE Y MERMA`.
Ejemplos:

1. `Medir la temperatura de pico de gallo, guacamole y salsas crudas (≤ 4 °C)`
2. `Anotar la hora de puesta en barra de cada salsa y su hora de descarte`
3. `Reponer por tandas pequeñas en recipiente limpio; PROHIBIDO rellenar sobre el resto anterior`
4. `Cambiar cucharas y pinzas de cada salsa por turno y registrar el cambio`
5. `Revisar visualmente la barra cada turno: restos, derrames y manipulación por el cliente`
6. `Descartar al cierre las salsas crudas del día y anotar la merma`
7. `Comprobar que cada salsa tiene su utensilio propio y que ninguno se comparte con la macha`

#### Hoja `Alérgenos y Cruzada` — 14-16 tareas
**Propósito**: los cuatro puntos donde se cae una taquería (D12).
Secciones: `  CACAHUETE Y SÉSAMO` · `  GLUTEN: MAÍZ FRENTE A HARINA` · `  LÁCTEOS Y FRUTOS DE CÁSCARA` · `  FICHAS Y CAMBIOS`.
Ejemplos:

1. `Marcar la salsa macha (cacahuete y/o sésamo) en el cartel y separarla físicamente del resto`
2. `Separar la tortilla de maíz (sin gluten) de la de harina de trigo: freidora, pinzas y superficie distintas`
3. `Revisar la ficha de alérgenos de los moles (frutos de cáscara, sésamo) antes del servicio`
4. `Comprobar que el mostrador sabe dar la información de alérgenos de los 14 de declaración obligatoria`
5. `Registrar cada cambio de proveedor o de receta que altere una ficha de alérgenos`
6. `Comprobar que la información de alérgenos es gratuita y accesible al cliente, por escrito`
7. `Limpiar y desinfectar licuadora y molcajete entre salsas para no arrastrar alérgenos`

---

### 04 · `04-nixtamal-tortilla-guisados.xlsx`

Hojas: `Instrucciones` · `Nixtamal y Molienda` (19 car.) · `Tortilla y Comal` (16 car.) · `Guisados y Rotación` (19 car.).

> Glosas obligatorias en `Instrucciones`: **tortillería (obrador de tortilla de maíz)**, **nixtamal (maíz cocido con cal para hacer masa)**, **guisados (cazuelas de relleno)**.
> La sección de nixtamal va marcada **(si aplica)**: quien compra la tortilla usa la sección de recepción.

#### Hoja `Nixtamal y Molienda` — 14-16 tareas
**Propósito**: el turno de madrugada del obrador, con el molino como punto crítico.
Secciones: `  COCCIÓN Y REPOSO (SI APLICA)` · `  MOLIENDA` · `  RENDIMIENTO Y CONSERVACIÓN`.
Ejemplos:

1. `Pesar maíz y cal, anotar la proporción y la hora de inicio de la cocción`
2. `Registrar el tiempo de reposo y la hora de lavado del nixtamal`
3. `Limpiar y desinfectar el molino ANTES de moler — es el punto crítico de la tortillería`
4. `Limpiar y desinfectar el molino DESPUÉS de moler y dejarlo seco`
5. `Anotar la hora de molienda y la temperatura de conservación de la masa`
6. `Anotar la hora límite de la masa definida en tu APPCC (HACCP): ______`
7. `Registrar el rendimiento: kg de maíz, kg de masa y número de tortillas`

**Celdas para el operador**: proporción de cal · horas · **hora límite de la masa (U14: no hay norma que la fije)** · rendimiento.

#### Hoja `Tortilla y Comal` — 10-12 tareas
Secciones: `  CALIBRADO` · `  PRODUCCIÓN Y MERMAS` · `  TORTILLA COMPRADA`.
Ejemplos:

1. `Calibrar la tortilladora al arranque: grosor y peso por pieza`
2. `Anotar las mermas de tortilla por turno y su causa`
3. `Registrar la recepción de tortilla comprada: proveedor, lote, fecha y temperatura`
4. `Comprobar que la tortilla de harina se almacena separada de la de maíz`
5. `Limpiar a fondo la tortilladora al cierre y dejarla seca`

#### Hoja `Guisados y Rotación` — 12-14 tareas
Secciones: `  ELABORACIÓN` · `  BAÑO MARÍA` · `  SOBRANTE Y MERMA`.
Ejemplos:

1. `Anotar hora de elaboración y hora de entrada en baño maría de cada guisado`
2. `Comprobar ≥ 63 °C en cada cazuela con dos lecturas por turno — anota: ____ °C`
3. `Anotar la hora límite de cada guisado (cazuela de relleno) en servicio`
4. `Cocinar el pollo del guisado (tinga) a ≥ 74 °C durante ≥ 1 s en el centro`
5. `Recalentar a ≥ 74 °C durante 15 s en el centro, en menos de 1 hora desde que sale del frío`
6. `Etiquetar y abatir el sobrante apto; descartar el no apto y anotar la merma`
7. `Comprobar la rotación: primero lo elaborado antes (PEPS)`

> ⚠️ **Dos umbrales de 74 °C conviven en esta hoja, y no son intercambiables (D9)**: el cocinado de aves (pollo del trompo mixto, tinga) exige **74 °C durante ≥ 1 s** (U11); el recalentado de guisados exige **74 °C durante ≥ 15 s, en el término de 1 hora** (U2). Toda tarea que use 74 °C lleva también el tiempo, para que no se confundan.

---

### 05 · `05-tareas-manager.xlsx`

Hojas: `Instrucciones` · `Tareas Diarias Manager` (22 car.) · `Tareas Semanales Manager` (24 car.). Calcado del molde **[medido]**.

#### Hoja `Tareas Diarias Manager` — 13-16 tareas
Secciones: `  ANTES DE APERTURA` · `  DURANTE EL SERVICIO` · `  CIERRE DE NEGOCIO`.
Ejemplos:

1. `Revisar la hoja de temperaturas firmada del turno anterior y archivarla`
2. `Medir el rendimiento del trompo del día: kg montados, tacos servidos y sobrante`
3. `Revisar los tiempos y las incidencias del canal de delivery`
4. `Hacer el arqueo y el cuadre de caja y dejar constancia del reparto de propinas`
5. `Responder las reseñas del día`

#### Hoja `Tareas Semanales Manager` — 9-12 tareas
Secciones: `  COMPRAS E IMPORTACIÓN` · `  COSTES` · `  EQUIPO`.
Ejemplos:

1. `Lanzar el pedido al importador de chiles secos, masa y producto mexicano, con su plazo: ______ días`
2. `Comparar precios de cerdo y de res con al menos dos proveedores`
3. `Hacer inventario de bebida, mezcal y tequila`
4. `Revisar el escandallo (costeo) de los 5 tacos más vendidos`
5. `Planificar los turnos de la semana siguiente`
6. `Cerrar y firmar el registro de jornada (obligatorio; en el soporte que exija la normativa vigente)`

> 🔴 La tarea 6 se escribe **exactamente así** (D5). Nunca «registro horario digital», nunca «obligatorio desde 2026».
> **B9**: la tarea 1 lleva el plazo de entrega **dentro del texto** (`con su plazo: ______ días`), nunca en la columna `Hora Límite`: escribir «7 días» o «Según entrega» ahí dispara `cadencia()` (`motor.py:2261-2325`) y renombra la columna. `Hora Límite` lleva siempre una **hora** (`HH:MM`), como en el resto del kit — es la diferencia de fondo con los demás kits de la familia: una taquería española depende de importación para el chile seco y la masa (`01-research…md:423`).

---

### 06 · `06-tareas-perfiles.xlsx`

Hojas: `Instrucciones` + **6 hojas de perfil**, 7-9 tareas cada una (42-54 en total).
Nombres de pestaña (todos ≤ 31 caracteres, sin `/`): `Taquero del Trompo` · `Tortillería` · `Salsas` · `Plancha y Freidora` · `Mostrador y Caja` · `Reparto y Delivery`.

> ⚠️ **Pestañas sin género y sin barra**: las pestañas se llaman `Tortillería` y `Salsas` (Excel no admite `/` en un nombre de pestaña, y así se evita el desdoblamiento de género en la cabecera). La fila 1 mantiene el prefijo del molde: `Checklist: Tortillería` y `Checklist: Salsas`. El puesto en persona (tortillero/a, salsero/a) puede mencionarse en el texto de las tareas cuando aporte, nunca en el nombre de la pestaña ni en la fila 1.
> `Reparto y Delivery` lleva **(si aplica)** en el subtítulo.

| Hoja | Propósito | Tareas |
|---|---|---:|
| `Taquero del Trompo` | Marinado, montaje, sonda, corte y limpieza del asador | 7-9 |
| `Tortillería` | Nixtamal, molienda, prensado, comal, mermas y limpieza del molino | 7-9 |
| `Salsas` | Molienda de chiles, salsas cocidas y crudas, barra, etiquetado y alérgenos | 7-9 |
| `Plancha y Freidora` | Tacos dorados, quesadillas, totopos, aceite y separación maíz/harina | 7-9 |
| `Mostrador y Caja` | Comanda, información de alérgenos, cobro, cola y entrega de delivery | 7-9 |
| `Reparto y Delivery` | Preparación y sellado, tiempos, temperatura de salida e incidencias | 7-9 |

Ejemplos de `Salsas` (hoja de referencia para las otras cinco):

1. `Tostar y moler los chiles del día y anotar la cantidad`
2. `Elaborar las salsas cocidas y etiquetarlas con fecha y hora de elaboración`
3. `Montar la barra de salsas y comprobar ≤ 4 °C en las crudas`
4. `Reponer por tandas en recipiente limpio; nunca rellenar sobre el resto anterior`
5. `Comprobar que la salsa macha (cacahuete y/o sésamo) está marcada y separada`
6. `Descartar las crudas al cierre y anotar la merma`
7. `Limpiar y desinfectar licuadora y molcajete entre salsas distintas`

Ejemplos de `Plancha y Freidora`:

1. `Filtrar el aceite de la freidora al cierre y anotar la fecha del último cambio`
2. `Comprobar el punto de humo del aceite antes del servicio y anotar la incidencia`
3. `Usar pinzas y cesta distintas para la tortilla de harina (gluten) y la de maíz`

Ejemplos de `Mostrador y Caja`:

1. `Preguntar por alergias e intolerancias antes de cerrar cada comanda`
2. `Dar la información de alérgenos por escrito cuando el cliente la pida`
3. `Comprobar que el pedido de delivery sale sellado y con el ticket correcto`

**Celdas para el operador**: `Responsable` y `Hora Límite` vienen con el puesto y la hora sugeridos en todas las hojas (§4); lo editable es sobrescribirlos con el nombre real de la persona.

---

### 07 · `07-semanales-mensuales.xlsx`

Hojas: `Instrucciones` · `Tareas Semanales` (16 car.) · `Tareas Mensuales` (16 car.).

#### Hoja `Tareas Semanales` — 13-16 tareas
Secciones: `  LIMPIEZA PROFUNDA` · `  INVENTARIO Y ALMACÉN` · `  EQUIPO`.
Ejemplos:

1. `Desengrasar a fondo el trompo (asador vertical) y la campana extractora`
2. `Afilar los cuchillos de corte y registrar la fecha`
3. `Limpiar a fondo el molino y la tortilladora, con desmontaje`
4. `Hacer inventario de chiles secos y revisar el control de plagas del almacén seco`
5. `Dar 15 minutos de formación al equipo y anotar el tema tratado`

#### Hoja `Tareas Mensuales` — 11-14 tareas
Secciones: `  INSTALACIONES` · `  APPCC Y DOCUMENTACIÓN` · `  PROVEEDORES`.
Ejemplos:

1. `Revisar la instalación de gas del asador vertical y del comal, y archivar el parte`
2. `Calibrar las sondas y los termómetros y anotar la desviación medida`
3. `Revisar el plan APPCC (HACCP) y las fichas de alérgenos`
4. `Auditar a los proveedores de importación: plazos, incidencias y documentación`
5. `Limpiar los filtros de extracción y registrar la fecha y el responsable`

---

### 08 · `08-eventos-estacionales.xlsx`

Hojas: `Instrucciones` · `Temporadas y Producto` (21 car.) · `Calendario de Eventos` (21 car.). **Este orden (D19)**.
La cabecera de la fila 2 de las dos hojas es la anual: `Año: ______    Taquería: _________________________`.

#### Hoja `Temporadas y Producto` — 11-14 tareas
Secciones: `  CHILES EN NOGADA (15-JUL A FIN DE SEP)` · `  CHILE SECO POR CAMPAÑA` · `  CARNE Y MAÍZ` · `  PRODUCTO FRESCO`.
Ejemplos:

1. `Reservar con el importador la nuez de Castilla y la granada para los chiles en nogada`
2. `Anotar el inicio real de la temporada de chiles en nogada, que depende de la cosecha`
3. `Revisar precio y disponibilidad del aguacate antes de fijar la carta del trimestre`
4. `Comprobar el precio del cerdo para pastor frente al de la campaña anterior`
5. `Anotar la campaña y el lote de cada chile seco recibido`

> La temporada de chiles en nogada va del **15 de julio a finales de septiembre**, con agosto como mes de mayor disponibilidad, y depende de la cosecha de granada roja, nuez de Castilla, manzana panochera, pera lechera, durazno criollo y chile poblano **[fuente: `01-research…md:433`]**.

#### Hoja `Calendario de Eventos` — 13-16 tareas
Secciones: `  PRIMER TRIMESTRE` · `  SEGUNDO TRIMESTRE` · `  TERCER TRIMESTRE` · `  CUARTO TRIMESTRE`.
Columna `Zona` usada como **mercado**: `ES`, `MX`, `US-es` o `Todos`.
Ejemplos:

1. `Día de Reyes (6 de enero): previsión de rosca y de turno reforzado`
2. `Candelaria (2 de febrero): producción de tamales y comunicación en redes`
3. `Cuaresma y Vigilia: reforzar tacos de pescado y capeados; activar el registro de congelación`
4. `Cinco de Mayo (5 de mayo): campaña sobre todo para EE. UU.; en México se celebra en Puebla`
5. `Grito e Independencia (15 y 16 de septiembre): pico del año fuera de México; pozole y mezcal`
6. `Día de Muertos (1 y 2 de noviembre): pan de muerto y calabaza en tacha`
7. `Virgen de Guadalupe (12 de diciembre): previsión de servicio y personal`
8. `Posadas (16 a 24 de diciembre) y comidas de empresa: cerrar aforos y menús cerrados`
9. `Terrazas de verano: ampliar horario y revisar el aforo autorizado`

> 🔴 **La tarea 4 se escribe con ese matiz siempre (D8)**. Nunca «la gran fiesta mexicana».

---

### 09 · `09-plantilla-personalizable.xlsx`

Hojas: `Instrucciones` · `Plantilla en Blanco` (19 car.).
**Propósito**: que el comprador cree checklists del formato exacto de su taquería (de barrio o de guisados, gourmet, con tortillería, cantina).
Misma rejilla de 7 columnas, **sin ninguna tarea escrita**: 3 secciones `  SECCIÓN 1 (PERSONALIZAR)`, `  SECCIÓN 2 (PERSONALIZAR)`, `  SECCIÓN 3 (PERSONALIZAR)` y **15 filas numeradas en blanco**, calcado del molde **[medido]**.
En `Instrucciones`, además de los cinco bloques de v2.0, el bloque **«Cómo personalizar por tipo de taquería»** con una línea por formato (`01-research…md:264-271`):

- **De barrio o de guisados** — la tarea crítica es la rotación de guisados: hora de elaboración, entrada en baño maría, hora límite y merma.
- **Gourmet o contemporánea** — fichas de emplatado, plato del día en el briefing, mermas de producto caro y reservas.
- **Con trompo al pastor** — es el formato con más carga de registro: usa el 02 entero.
- **Con tortillería propia** — turno de madrugada completo en el 04; el molino es el punto crítico.
- **Con barra de salsas de autoservicio** — el 03 es tu hoja principal.
- **Taquería-cantina** — doble cierre (cocina y barra), mermas de barra e inventario de mezcal y tequila.

---

### BONUS-01 · `BONUS-01-briefing-servicio.xlsx`

Hojas: `Instrucciones` · `Briefing Pre-Servicio` (21 car.).
**Formulario**, no checklist (D3.0). Título de la fila 1: `Briefing Pre-Servicio — Taquería Mexicana` (NO en versalitas: `motor.es_briefing` busca `'Briefing'` sensible a mayúsculas, `motor.py:1250`; con `BRIEFING` la hoja quedaría fuera de alcance). Fila 2: `Fecha:` `___/___/______` `Turno:` `☐ Almuerzo  ☐ Cena` `Responsable briefing:` `_________________________`.
Bloques y campos (todo son celdas del operador):

| Bloque | Campos |
|---|---|
| `TROMPO DEL DÍA (SI APLICA)` | `Peso montado: ____ kg` · `Hora de montaje: ____` · `Hora límite (tu APPCC): ____` · `Previsión de cortes: ____` |
| `GUISADOS DEL DÍA` | 4 líneas `Guisado __: __________ (hora de entrada: ____  hora límite: ____)` |
| `SALSAS DEL DÍA` | 5 líneas `Salsa __: __________ (picante: ☐ suave ☐ medio ☐ alto)` |
| `AVISO DE ALÉRGENOS` | `Salsa macha en barra: ☐ sí ☐ no  → CACAHUETE y/o SÉSAMO` · `Mole del día: __________ (frutos de cáscara: ☐ sí ☐ no)` · `Tortilla de harina disponible: ☐ sí ☐ no (GLUTEN)` |
| `ROTURAS Y «86»` | 5 líneas `Sin __________` (la voz «86» = se acabó, glosada en `Instrucciones`) |
| `SALA Y DELIVERY` | `Reservas: ____` · `Grupos: ____` · `Previsión de delivery: ____` · `Personal del turno: ____` |

---

### BONUS-02 · `BONUS-02-calendario-anual.xlsx`

Hojas: `Instrucciones` · `Calendario Anual` (16 car.).
**Molde calendario de la familia NO-CB** (B1; `sub_cb()` no reconoce la matriz `TAREA / ACCIÓN | Ene…Dic` para esta taquería, `motor.py:1367-1369`), calcado de `kit-tareas/BONUS-02-calendario-anual-tareas.xlsx` **[medido]**:

- Fila 1: `CALENDARIO ANUAL — TAQUERÍA MEXICANA`.
- Fila 2: `Año: ______    Taquería: _________________________`.
- Fila 3: vacía.
- Fila 4 (cabecera, panel congelado `ySplit="4"`): `Mes | Fecha / Evento | Tareas Clave | Antelación`.
- **24-36 filas** (2-3 por mes), una por evento o tarea de mantenimiento anual, cronológicas de enero a diciembre.

Ejemplos en forma final (`Mes | Fecha / Evento | Tareas Clave | Antelación`):

1. `Febrero | 2 Feb — Candelaria | Producción de tamales; comunicarlo en Google Business Profile y en redes | 2 semanas`
2. `Marzo-Abril | Cuaresma y Vigilia (variable) | Reforzar tacos de pescado y capeados; activar el registro de congelación de crudos (U6) | 2 semanas`
3. `Mayo | 5 Mayo — Cinco de Mayo | Campaña sobre todo para EE. UU.; en México se celebra en Puebla | 1 semana`
4. `Julio-Septiembre | 15 Jul a fin de Sep — Chiles en Nogada | Reservar con el importador nuez de Castilla y granada; depende de la cosecha | 1 mes`
5. `Septiembre | 15-16 Sep — Grito e Independencia | Pico del año fuera de México; reforzar pozole y mezcal | 2 semanas`
6. `Noviembre | 1-2 Nov — Día de Muertos | Producción de pan de muerto y calabaza en tacha | 2 semanas`
7. `Diciembre | 16-24 Dic — Posadas y comidas de empresa | Cerrar aforos y menús cerrados | 1 mes`

El resto de las 24-36 filas cubre, distribuido mes a mes, lo mismo que ya reunía el research: eventos y campañas (D8), temporadas de producto (chile seco, aguacate), mantenimiento (gas del asador, desengrase, limpieza del molino, calibración de sondas), APPCC y documentación (plan APPCC, fichas de alérgenos, auditoría de proveedores de importación) y equipo y cierres (formación, vacaciones, cierre anual). Cada fila es una sola combinación mes/evento; no hay columnas de mes ni marca `✓` por mes — eso era del molde matriz descartado en B1.

---

## §4 Reglas de redacción para los redactores de F2

**Tú escribes el texto de las celdas de un Excel que un cocinero imprime, rellena a boli y firma. No escribes un artículo.**

### Forma de la tarea

1. **Verbo en infinitivo al principio**: «Registrar…», «Comprobar…», «Anotar…», «Limpiar…», «Sondar…». Nunca «Se debe…», «Hay que…», «El responsable registrará…».
2. **Máximo 110 caracteres** por tarea. La columna mide 48 unidades de ancho: lo que pase de ahí se lee mal impreso.
3. **Una tarea = un momento, una zona y un responsable (C1).** Se admite `verbo + y anotar/registrar/comprobar` cuando el registro es parte del mismo acto. **NUNCA dos momentos distintos** en la misma fila.
4. **Con umbral y unidad cuando aplique**, y el umbral va **dentro** de la tarea, no en una nota:
   `Comprobar la sonda del trompo ≤ 4 °C antes de encender`
5. **Coletilla de lectura** cuando la tarea es una medición: ` — anota la lectura: ____ °C`. Es la forma que ya emite el motor (`kit-tareas/01-apertura-cierre.xlsx` **[medido]**); escribirla igual evita que el motor la añada por su cuenta y rompa la idempotencia.
6. **Sin punto final.** Las tareas del corpus no lo llevan **[medido]**.
7. **Secciones en MAYÚSCULAS con dos espacios de sangría** al principio: `  TEMPERATURAS Y EQUIPOS`. Las secciones **sí** llevan tildes (D6): `  ALÉRGENOS Y CRUZADA`.
8. **`Responsable` y `Hora Límite` no quedan en blanco (B6).** F2 las rellena con el puesto y la hora sugeridos para esa tarea; lo editable es sobrescribirlos con el nombre real de la persona y su horario, no inventarlos desde cero.
9. **El plazo en días va en el texto, nunca en `Hora Límite` (B9).** Un plazo de entrega («7 días», «Según entrega») escrito en la columna `Hora Límite` dispara `cadencia()` (`motor.py:2261-2325`) y renombra la columna. La forma correcta es dentro de la tarea: `…, con su plazo: ______ días`. La columna `Hora Límite` lleva siempre una hora (`HH:MM`).

### Unidades, horas y símbolos

| Elemento | Forma correcta | Forma incorrecta |
|---|---|---|
| Grado | `63 °C` — **espacio NORMAL U+0020** antes del `°` (D14) | `63°C` · `63 °C` con U+202F · `63 ºC` con masculina ordinal |
| Negativo | `−18 °C` con **U+2212** (D15) | `-18 °C` con guion ASCII |
| Comparadores | `≤ 4 °C`, `≥ 63 °C`, con espacio a los dos lados | `<=4C`, `>63ºC` |
| Rango | `12-24 h` con guion normal | `12–24 h` con raya |
| Hora | `10:00`, `14:30` (columna `Hora Límite`) | `10h`, `10.00` |
| Tiempo | `15 s`, `24 h`, `1 hora` | `15s`, `24h` |
| Peso | `10 kg`, `____ kg` | `10kg` |
| Decimal | coma: `0,5 kg` | punto |
| Casilla | `☐` (U+2610) · Marca `✓` (U+2713) · Guion largo de la DV `—` (U+2014) | `[ ]`, `X`, `-` |
| Relleno | `______` (6 guiones bajos) o `____ °C` | `___`, `....` |
| Dinero | **no se imprime** (D20) | `€`, `$`, `MXN` |

### Glosario obligatorio (D7)

**La primera vez que el término aparece en CADA fichero** (no una vez en todo el kit: cada `.xlsx` se imprime suelto):

| Término | Primera aparición |
|---|---|
| trompo | `trompo (asador vertical)` |
| tortillería | `tortillería (obrador de tortilla de maíz)` |
| guisados | `guisados (cazuelas de relleno)` |
| salsero/a | `salsero/a (responsable de salsas)` |
| APPCC | `APPCC (HACCP)` |
| escandallo | `escandallo (costeo)` |
| nixtamal | glosado en `Instrucciones` del 04: `nixtamal (maíz cocido con cal para hacer masa)` |
| macha | **siempre** `salsa macha (cacahuete y/o sésamo)` en cualquier hoja de alérgenos |
| 86 | glosado en `Instrucciones` del BONUS-01: `«86» (la voz de "se acabó")` |

**Mexicanismos que se dejan tal cual, sin glosa y sin traducir**: `taquero`, `comal`, `pastor`, `al pastor`, `aguachile`, `cochinita`, `carnitas`, `suadero`, `mole`, `pico de gallo`. Son el producto (`01-research…md:508-510`).

### Prohibiciones (D7, D5, D8, D20)

- **«tex-mex»** — en ninguna celda, en ningún fichero, en ninguna instrucción.
- **«gyro»** como sinónimo de trompo. Vale como comparación pedagógica en `Instrucciones` («funciona como un kebab»), nunca como sinónimo.
- **«burrito»** o **«nachos»** como plato de taquería.
- **«tortilla» a secas** — siempre `tortilla de maíz` o `tortilla de harina`. La distinción es el alérgeno.
- **«Cinco de Mayo» sin su matiz** — va siempre con «campaña sobre todo para EE. UU.» o equivalente.
- **«registro horario digital»**, **«obligatorio en 2026»**, **«digital obligatorio»** — la única redacción válida es `registro de jornada (obligatorio; en el soporte que exija la normativa vigente)`.
- **«65 °C»** en contexto de mantenimiento en caliente — es la cifra derogada (§2).
- **Importes**, en euros o en pesos.
- **«prueba gratis»** o **«plan gratuito»** de AI Chef Pro — el plan gratuito murió el 15-ago.
- **Cualquier carácter no latino** (CJK, cirílico, hangul, árabe, hebreo, tailandés).

### Cómo marcar «si aplica» (D3)

Tres niveles, y se usan los tres:

1. **En el nombre de la sección**: `  MONTAJE DEL TROMPO (SI APLICA)`.
2. **En `Instrucciones`**, una línea que explica qué hacer: *«Si tu taquería no tiene trompo (asador vertical), marca N/A las tareas de la sección TROMPO: salen del total y el porcentaje sigue siendo honesto.»*
3. **Nunca dentro del texto de la tarea**: gastaría caracteres y se repetiría 20 veces.

Llevan «(si aplica)»: la sección de trompo del 02 · la sección de nixtamal del 04 · la hoja `Reparto y Delivery` del 06 · la sección `  CONGELACIÓN DE CRUDOS (SI APLICA) Y RECALENTADO` del 03 (D8).

### Qué NO inventar

Estas cuatro cifras **no existen en ninguna fuente** y la celda las deja al operador (U12, U13, U14 del §2):

- tiempo máximo de cono montado,
- vida útil de la carne ya fileteada,
- vida útil de la masa nixtamalizada,
- vida útil de una salsa cruda en barra más allá del turno.

La forma de escribirlo es siempre: `Anotar la hora límite … definida en tu APPCC (HACCP): ______`. **Nunca «máximo 4 h»**.

---

## §5 Gates de aceptación de F2

Todos mecánicos. F2 no se da por cerrada hasta que los once están en verde.

| # | Gate | Comprobación | Umbral |
|---|---|---|---|
| **G1** | **Caracteres no latinos** | `python3 scripts/productos-digitales/gate-no-latinos.py --only kit-tareas-taqueria` | exit 0 · **0 ocurrencias** |
| **G2** | **Cifra derogada** | Barrido de las cadenas de los 11 `.xlsx`: **0** apariciones de `65 °C` / `65°C` / `65 ºC` en un contexto de ±60 caracteres que contenga «caliente», «baño maría», «mantenimiento» o «recalent». Y **≥ 1** aparición de `63 °C` | 0 y ≥ 1 |
| **G3** | **Registro horario** | **0** apariciones de las cadenas cerradas `registro horario digital`, `control horario digital`, `fichaje digital`, `horario digital`, `obligatorio en 2026`, `digital obligatori` (lista cerrada, A2: evita falsos positivos como «termómetro digital»). Y la cadena exacta `en el soporte que exija la normativa vigente` aparece **≥ 1** vez (05) | 0 y ≥ 1 |
| **G4** | **Cinco de Mayo** | Toda aparición de `Cinco de Mayo` lleva en la misma celda `EE. UU.` o `Estados Unidos` o `Puebla`. **0** apariciones de `fiesta nacional` junto a `mexicana` | 100 % |
| **G5** | **Tildes (D6)** | Barrido **insensible a mayúsculas** (A3). Estas palabras, cuando aparezcan, **deben** llevar tilde: `límite`, `cámara`, `preparación`, `alérgenos`, `año`, `día`, `rotación`, `refrigeración`, `congelación`, `información`, `contaminación`, `sésamo`, `taquería`, `tortillería`, `baño`, `máximo`, `número`, `después`, `añadir`, `cómo`, `protección`, `sección`, `maría` (de «baño maría»). Barrido: **0** apariciones de la forma sin tilde (`limite`, `camara`, `preparacion`, `alergenos`, `ano`, `dia`, `maria`, …) como palabra completa, en cualquier capitalización. **`Molcajete` queda FUERA de la lista, como control negativo aparte** (no lleva tilde; comprobar que el barrido no lo marca como falso positivo). Nota: `Nº` es `N` + `U+00BA` (ordinal masculino) — no confundir con el grado `U+00B0` | **0** sin tilde |
| **G6** | **Prohibiciones de vocabulario** | **0** apariciones de `tex-mex`, `Tex-Mex`, `burrito`, `nacho`, `gyro` (salvo la comparación pedagógica única de `Instrucciones` del 02), `peso mexicano`, `MXN`, `$`, `prueba gratis`, `plan gratuito` | 0 |
| **G7** | **Glosario** | En cada uno de los 11 ficheros, la **primera** aparición de `trompo`, `tortillería`, `guisado`, `salsero`, `APPCC`, `escandallo` va seguida de su paréntesis. Y **toda** aparición de `macha` lleva `cacahuete` en la misma celda | 100 % |
| **G8** | **Tareas por hoja** | Para cada una de las 22 hojas de checklist de los ficheros 01-08, el recuento de celdas numéricas en la columna `A` cae **dentro del rango del §3.1**. Total del kit en **[270, 330]** | 22/22 y total en rango |
| **G9** | **Estructura y DV** | Los 11 ficheros existen con el nombre exacto del §3 · toda hoja de checklist tiene la DV `"✓,—,N/A"` · nombres de pestaña ≤ 31 caracteres y sin `/` · panel congelado en la fila 4 · las 5 filas libres dentro del rango del contador · las 5 secciones de `Instrucciones` de v2.0 y el pie `— Kit de Tareas Recurrentes · Taquería Mexicana · AI Chef Pro · aichef.pro` | 11/11 |
| **G10** | **Censo de entregables** | `python3 scripts/productos-digitales/censo-entregables.py --only kit-tareas-taqueria --fail` | **exit 0**, 0 defectos |
| **G11** | **Motor e idempotencia** | `python3 scripts/productos-digitales/kit-tareas-v2_0/main.py --producto kit-tareas-taqueria --dry-run --json informe.json` → **0 diferencias** en la comparación celda a celda de la 2.ª pasada (`main.py:23-25`). Después, `python3 scripts/productos-digitales/~~postprocess-transversal~~ (**NO correr**: saneamiento v1.1 de la Fase A; medido el 20-sep, degrada el contador honesto a `COUNTIF`, la versión a 1.1 y la metadata v2.0) sobre el producto | 0 diferencias |

**Longitud**: ninguna tarea supera **110 caracteres** (§4.2). Se comprueba en el mismo barrido de G8.

**Orden de ejecución sugerido**: G9 → G8 → G5/G2/G3/G4/G6/G7 (un solo barrido de cadenas) → G1 → G11 → G10.

> ⚠️ **Gate G11, riesgo conocido**: la taquería **no está en `SUBFAMILIA_CB`** (D17), así que `motor.ortografia()` no corre sobre ella. Eso es lo que se quiere. Pero hay que confirmar en la 1.ª pasada del dry-run que el motor **reconoce la columna `Hora Límite` con tilde**: el propio motor documenta que `_col_tiempo` y `EDITABLES` comparan **sin tildes** desde la tanda CB (`motor.py:4753-4759`) **[medido]**, así que debería. **Si no la reconociera**, el síntoma sería la columna de tiempo sin pintar de verde y el contador sin rango; en ese caso la solución **no** es quitar las tildes, es corregir el detector.

---

## §6 Checklist de F3 (capa de producto)

### 6.1 Las 24 piezas a calcar de `kit-tareas-sushi-bar`

`grep -rl "kit-tareas-sushi-bar" --include="*.ts" --include="*.tsx" --include="*.astro" astro-site/src src netlify | sort` da **21 ficheros** **[medido, hoy]** — no 22: faltan los dos `.astro` de la zona app (B4, filas 22-23) y el `dl/` de F2 (fila 24), que el grep no ve:

| # | Fichero | Qué hay que hacer |
|---:|---|---|
| 1 | `astro-site/src/components/pages/ProductosDigitalesHubPage.astro` | Alta del producto **en posición 1** (novedades primero, `8b3fe17`) y **baja de `comingSoon`** (`:997`) |
| 2 | `astro-site/src/data/productos/tareas/kit-tareas-sushi-bar.ts` | → `kit-tareas-taqueria.ts`. Ficha completa (ver 6.2) |
| 3 | `astro-site/src/islands/library/KitTareasSushiBarLibraryIsland.tsx` | → `KitTareasTaqueriaLibraryIsland.tsx` |
| 4 | `astro-site/src/lib/zona-app.ts` | Entrada nueva, calcada de `:67` |
| 5 | `astro-site/src/pages/kit-tareas-sushi-bar.astro` | → `kit-tareas-taqueria.astro` |
| 6 | `netlify/edge-functions/og-meta.ts` | (edge **MUERTA** desde Fase 7; se mantiene por coherencia, no por efecto) |
| 7 | `netlify/functions/admin-generate-access.ts` | Alta del pid |
| 8 | `netlify/functions/get-download-urls.ts` | **Los 11 paths** de descarga |
| 9 | `netlify/functions/resend-access.ts` | Alta del pid |
| 10 | `netlify/functions/verify-purchase.ts` | Alta del pid |
| 11 | `netlify/shared/payment-links.ts` | Payment Link de Stripe + env var `VITE_STRIPE_PAYMENT_LINK_TAREAS_TAQUERIA` (sin `KIT_`, como los otros 19 kits; `kit-tareas-sushi-bar.ts:12`, scope **builds**) |
| 12 | `netlify/shared/product-prices.ts` | `'kit-tareas-taqueria': { eur: 14 }`, junto a los otros cuatro de 14 € (`:20-38`) |
| 13 | `src/App.tsx` | Rutas de la SPA |
| 14 | `src/data/productos-changelog.ts` | Entrada v1.0 |
| 15 | `src/data/productos-digitales-config.ts` | Config del producto |
| 16 | `src/data/products-catalog.ts` | **Alta obligatoria** o el producto queda invisible para los banners del blog. **Sin comentarios entre `description: {` y `es:`** (el parser de `fase8c-libreria-assemble.py` pierde la entrada en silencio si los hay, 30-ago); `name: { es: 'Tareas: Taquería Mexicana', en: … }`, `price: '€14'`. Correr el gate de recuento del parser tras el alta (C2) |
| 17 | `src/pages/AdminGenerateAccess.tsx` | Alta en el selector |
| 18 | `src/pages/KitTareasSushiBar.tsx` | → `KitTareasTaqueria.tsx` |
| 19 | `src/pages/KitTareasSushiBarAccessGate.tsx` | → `KitTareasTaqueriaAccessGate.tsx` |
| 20 | `src/pages/KitTareasSushiBarDashboard.tsx` | → `KitTareasTaqueriaDashboard.tsx` (11 descargas) |
| 21 | `src/pages/ProductosDigitales.tsx` | **Gemelo del hub**: alta en posición 1 y **baja de `comingSoon`** (`:981`) |
| 22 | `astro-site/src/pages/kit-tareas-taqueria-access.astro` | **Nuevo (B4)**. `title={ACCESS_TITLE} noindex` + `FunctionsOriginPatch`, molde `kit-tareas-sushi-bar-access.astro`. Se genera con `python3 scripts/astro-migration/fase5-generate-zona-app.py` tras el alta en `zona-app.ts` |
| 23 | `astro-site/src/pages/kit-tareas-taqueria-library.astro` | **Nuevo (B4)**. `noindex whatsapp={false}`, molde `kit-tareas-sushi-bar-library.astro`. Mismo generador que la fila 22 |
| 24 | `astro-site/public/dl/kit-tareas-taqueria/` | Los 11 `.xlsx` de F2, **incluidos en el mismo commit** |

> 🔴 **Los dos hub son gemelos y los dos tienen la tarjeta de la taquería en `comingSoon` hoy**: `ProductosDigitalesHubPage.astro:997` y `src/pages/ProductosDigitales.tsx:981` **[medido]**. Tocar sólo uno deja la tarjeta «Q4 2026» viva en media web.
> Nota: la tarjeta **ya se actualizó** respecto a lo que decía el research (`:244`): hoy dice *«Trompo, plancha, salsas y tortillería, turnos y cierre para una taquería que funciona sola, con calendario anual»* **[medido]** — ya menciona el trompo y el calendario anual (D10). Sirve de base para el `subtitleLine` del hero.

### 6.2 La ficha `kit-tareas-taqueria.ts`

Bloques obligatorios, en el orden del molde (`kit-tareas-sushi-bar.ts`, censados en `01-research…md:231`):
`slug` · `stripeEnvKey` · `seo{title,description,keywords,ogImage}` · `schema{productName,productDescription,price,priceValidUntil,aggregateRating,reviews[3],faqs[5],breadcrumbName}` · `images{gallery[6],whyBg,buyBoxBg,ctaBg}` · `hero{badge,titlePre,titleGold,subtitleLine,description,checkItems[5],ctaLabel}` · `stickyLabel` · `grid{countGold:'11',headingRest,subtitle,templates[11]}` · `why{reasons[4],compatPills[5]}` · `authorBio` · `bonus{items[2]}` · `buyBox` · `guarantee{text,stats[3]}` · `faqs[6]` · `cta{heading,subtitle,items[8],ctaLabel}` · `testimonials{items[8]}` · `pricing{priceOld:'€69',price:'€14',discountBadge:'-80%'}` · `footerLinks[6]` · `updateNote` · `alreadyBought`.

- **Par de precio (D1)**: `price: '€14'` + `priceOld: '€69'` + `discountBadge: '-80%'`. **No mezclar con `'€39'`**, que es el par del escalón de 12 € (`kit-tareas-food-truck.ts:353`) **[medido]**.
- **`title` / `h2` (D10)**: el BONUS-02 sube al título. Ejemplo: *«Tareas Recurrentes para Taquería Mexicana — 11 Excel + Calendario Anual de Tareas»*.
- **Las dos grafías** en `keywords`: `taqueria` y `taquería` devuelven filas distintas en DataForSEO (`01-research…md:67`) **[medido]**.
- **`grid.templates[11]`**: un `name` + `desc` por fichero, con el nombre exacto del §3.
- Capa comercial (`aggregateRating` 4,9 · 8 reseñas · 8 testimonios con avatar) **intacta**, por decisión de John.

### 6.3 Resto de la capa

| Tarea | Detalle |
|---|---|
| **Precios** | `python3 scripts/productos-digitales/sync-product-prices.py` **[medido: existe]** — el importe de la factura cripto sale de `netlify/shared/product-prices.ts`, nunca del cliente |
| **Zona app** | Alta en `astro-site/src/lib/zona-app.ts` (de ahí salen el nombre corto del diálogo cripto y la tarjeta de Miselup) |
| **Cripto (3 puertas)** | `CryptoPayButton` en `hero`, `buybox` y `cta` + nota de devoluciones bajo la garantía. **Sólo la variante `buybox` emite el `<dialog>` y el `<script>`** |
| **Imágenes** | Skill `generate-images`. **2 en el cuerpo + 1 destacada distinta**, que no se repite dentro |
| **FAQ** | 6 preguntas, alimentadas por el **People Also Ask medido** (`01-research…md:90-98`, `:120`): «¿Cuántos tacos salen de un trompo de 10 kilos?» · «¿Cuántos tacos salen de 1 kg de tortilla?» · «¿Cuántos kilos de carne necesito para 100 tacos?» · «¿Cómo se administra una taquería?» · «¿Qué incluye un manual de operaciones?». **Cinco de las nueve son preguntas de rendimiento**: el kit las responde con la hoja del 02, no con una cifra inventada |
| **Cross-links D9** | `guia-restaurante-mexicano.ts` → kit («las hojas que ejecutan el manual, turno a turno») **y** kit → guía. Las **dos** direcciones |
| **Cesta de use-case** | Añadir `kit-tareas-taqueria` a `src/data/use-cases-content.es.ts:3580` (cesta de `restaurante-mexicano`, hoy `['guia-restaurante-mexicano','kit-escandallos','pack-appcc','kit-inventario','kit-gestion-personal','pro-prompts-ebook']`) **[medido]** |
| **pSEO ciudades MX** | Enlaces de entrada desde `/abrir-restaurante/ciudad-de-mexico` (23 clics), `/licencia-restaurante/monterrey` (24), `/abrir-restaurante/queretaro` (10), `/licencia-restaurante/guadalajara` (4) — **72 clics y 5.738 impresiones en 90 días** ya en casa **[medido]** |
| **Banners de blog** | `tacos-al-pastor-autenticos-receta-mexicana.md` y `23-moles-regionales-mexicanos-con-ia-guia-definitiva-con-cocina-mexicana-ai.md`, con `fase8e-banners-corpus.py` (nunca con el ensamblador, que pisa el cuerpo) |
| **Broadcast** | Uno individual en la cola de Resend: hueco = el `scheduled_at` más tardío que haya + **5 días**, a las **08:00 UTC**. Plantilla de lanzamiento `scripts/productos-digitales/emails/broadcast-manual-manager-lanzamiento-es.html`. Anotar el slot en el handoff y en `CALENDARIO-V2-SEMANAL.md` |
| **Mega Pack** | **No se toca (D11)** |

### 6.4 Gates LIVE de cierre

```
python3 scripts/productos-digitales/gate-flujo-postpago.py     # 3 botones cripto + dialog + descargas
python3 scripts/astro-migration/miselup-gate.py                # tarjeta lateral en landing y dashboard
python3 scripts/astro-migration/whatsapp-gate.py               # 1 botón por página; el -library pasa whatsapp={false}
python3 scripts/astro-migration/robots-gate.py                 # /kit-tareas-taqueria-library bloqueado, landing rastreable
```

Más: `curl` al checkout cripto con email `qa-…@aichef.pro` y purga con `crypto-report?purge_unpaid_before=`; y reenvío del sitemap en GSC.

> ⚠️ **`robots-gate.py` es obligatorio aquí**: nace una URL `-library` nueva. Las reglas van ancladas al prefijo de familia (`/kit-*-library`), y `kit-tareas-taqueria-library` **empieza por `/kit-`**, así que ya está cubierta — pero se comprueba, no se supone.

---

## §7 Riesgos y deuda detectada fuera de alcance

**Nada de esto se arregla en este producto.** Se documenta para que no se arrastre y para que John decida.

### R1 · 🔴 La cifra derogada de 65 °C está viva en 14 productos que se venden hoy

Barrido de las cadenas de **todos** los `.xlsx` de `astro-site/public/dl/` **[medido, hoy]**: **24 apariciones** de `65 °C` en contexto de mantenimiento en caliente.

| Producto · fichero | Texto |
|---|---|
| `pack-appcc/01-registro-temperaturas-diario.xlsx` | «Exposición caliente (baño maría): **65 °C** o superior» · «Rango: **65 °C** o superior» |
| `pack-appcc/12-analisis-peligros-haccp.xlsx` | «exposición caliente **≥65 °C**» · «multiplicación microbiana en mantenimiento caliente por debajo de **65 °C**» · «**≥65 °C** en todo el producto expuesto» · «recuperar a **≥75 °C**, o desechar si lleva más de 2 h por debajo de **65 °C**» |
| `pack-appcc/15-guia-inspeccion-sanidad.xlsx` | «Exposición caliente (**≥ 65 °C**)» |
| **`kit-tareas/02-partidas-cocina.xlsx`** (kit base) | «Control de temperatura de mantenimiento en caliente (**≥ 65 °C**)» |
| **`guia-restaurante-mexicano/checklist-appcc.xlsx`** | «Registro temperaturas servicio (caliente **>65°C**)» |
| `guia-restaurante-casual` · `-japones` · `-nikkei` · `-peruano` `/checklist-appcc.xlsx` | ídem |
| `kit-tareas-catering/04-tareas-perfiles.xlsx` · `/06-eventos-festivos.xlsx` | «>**65 °C** caliente» · «Máximo 2 h entre 5 °C y **65 °C**» |
| `kit-tareas-chef-privado/04-seguridad-alimentaria-appcc.xlsx` | «>**65°C**» · «zona de peligro (5-**65°C**)» |
| `kit-tareas-food-truck/03-appcc-seguridad-alimentaria-movil.xlsx` | «mantenido >**65°C**» |
| `kit-tareas-hotel/01-fb-buffet-desayuno.xlsx` · `/02-fb-buffet-comida-cena.xlsx` | «(>**65 °C**)» |
| `kit-tareas-pasteleria/02-partidas-cocina.xlsx` | «De +**65 °C** a +10 °C en menos de 2 h» |
| `kit-tareas-tapas-bar/03-cocina-raciones-platos.xlsx` | «Control temperatura mantenimiento (>**65°C** centro)» |
| `kit-gestion-personal/BONUS-01-briefing-cambio-turno.xlsx` | «el mantenimiento en caliente sólo es conforme A PARTIR de **65 °C**» (×2) |

Dos agravantes: el `pack-appcc` es **el producto que vende el APPCC**, y el `guia-restaurante-mexicano` es justo el producto con el que la taquería hace cross-sell (D9). Además, `pack-appcc/12` dice «recuperar a **≥75 °C**», cuando el art. 30 dice **74 °C durante 15 s**.
**Propuesta [estimado]**: barrido transversal en una sesión propia, con gate permanente. No en este producto.

### R2 · Copy vivo que afirma «control horario digital obligatorio 2026»

`grep -rn "horario digital|control horario"` sobre `astro-site/src` y `src` **[medido, hoy]**:

- `astro-site/src/data/productos/guias/guia-panaderia-obrador.ts:75` — *«Requisitos Legales España 2026: … + control horario digital»*
- `astro-site/src/data/productos/guias/guia-panaderia-obrador.ts:105` — testimonio: *«El control horario digital 2026 …»*
- **Y sus gemelos de la SPA, que el research no vio**: `src/components/guia-panaderia-obrador/ContentGrid.tsx:14` (el mismo item 05) y `src/data/testimonials-guia-panaderia-obrador.ts:58` (el mismo testimonio) **[medido]**. **Son 4 apariciones, no 2**: arreglar sólo el `.ts` de Astro dejaría el texto vivo en la SPA.

**Lo correcto**, por contraste: `src/pages/KitGestionPersonal.tsx:70` y `astro-site/src/data/productos/kits/kit-gestion-personal.ts:78` responden *«No. El registro de jornada es obligatorio en España desde 2019 (RD-ley 8/2019, art. 34.9 ET)…»* **[medido]**. Ese es el modelo.

### R3 · Seis kits LIVE sin tildes, y dos con el pie de otra marca

Censo de los 19 kits de `astro-site/public/dl/` **[medido, hoy]**:

| Estado | Kits |
|---|---|
| v2.0 (bloques de contador/filas/protección) · pie **aichef.pro** · **con tildes** | `kit-tareas` (base), bar, cafetería, catering, dark-kitchen, hamburguesería, hotel, pizzería *(9)* |
| Sin v2.0 · pie **aichef.pro** · **con tildes** | chef-privado, chocolatería, heladería, pastelería, restaurante-creativo *(5)* |
| Sin v2.0 · **SIN tildes** | asador, food-truck, marisquería, panadería, sushi-bar, tapas-bar *(6)* |
| De esos seis, con el pie **«ChefBusiness Consultoría Gastronómica · chefbusiness.co»** dentro de un producto de **aichef.pro** | **sushi-bar** y **asador** *(2)* |

El motor **ya tiene** el barrido de tildes (`motor.ortografia`, `motor.py:4744`), pero sólo corre para `SUBFAMILIA_CB` y la copia que se corrigió fue la de chefbusiness.co, no la de `astro-site/public/dl/`. **Deuda de familia, con un arreglo ya escrito y sin aplicar.**

### R4 · El kit no aparece en ninguna cesta de use-case hasta F3

`src/data/use-cases-content.es.ts:3580` no lo incluye (obvio, no existe). Pero el patrón se repite: **ningún kit de tareas de concepto está en la cesta de su caso de uso**. Comprobarlo al cerrar F3 es barato; arreglarlo para los 19 es otra sesión.

### R5 · Mega Pack: dice «13 kits» y hay 19 (pronto 20)

`src/data/products-catalog.ts:516` y `src/pages/MegaPackTareas.tsx:20-33` **[medido en el research, `:250-254`]**. D11 lo congela a propósito, pero cada kit nuevo agranda la distancia entre lo que dice el copy y lo que hay. La decisión ya estaba anotada en `CALENDARIO-V2-SEMANAL.md:311`.

### R6 · El post del blog al que se querría colgar el kit no tiene tracción

`blog.aichef.pro/tacos-al-pastor-autenticos-receta-mexicana/` sale en GSC con 2 impresiones y posición 80, **pero es la URL legacy ya 301-eada**; la URL migrada no aparece en el top-500 **[medido, `01-research…md:142-146`]**. Sirve para un banner, **no** como activo del que colgar el lanzamiento. El activo real es el pSEO de ciudades mexicanas (§6.3).

### R7 · Riesgo técnico de F2, con mitigación ya escrita

| Riesgo | Mitigación |
|---|---|
| El molde `generate-tareas-restaurante-creativo.py` escribe en `<repo>/public/dl/`, ruta pre-Astro | Corregir `OUTPUT_DIR` (§0) y comprobar con `ls astro-site/public/dl/kit-tareas-taqueria/` |
| Las helpers `create_task_sheet`, `create_blank_template_sheet`, `create_calendar_sheet` y `add_instructions_sheet` del generador v1 no emiten el molde v2.0 (rótulos, DV, fila 2, `freeze_panes`, cabecera única, numeración continua, pie) | Reescribirlas como contrato cerrado por un agente ANTES de repartir contenido (§0, B2); validar la estructura XML contra el sushi-bar antes de escribir tareas |
| El motor no reconoce `Hora Límite` con tilde | Documentado que compara sin tildes (`motor.py:4756-4759`); se verifica en el dry-run (G11) |
| U+202F rompe la idempotencia | D14: espacio normal en los `.xlsx`; U+202F sólo en el `.md` de F3 |
| Nombres de pestaña con `/` o > 31 caracteres | §3 los da ya resueltos (`Alérgenos y Cruzada`, `Taquero del Trompo`…); **el único gate es G9** (`censo-entregables.py:214` es informativo, no comprueba la `/`; D1) |
| Escribir un plazo en días («7 días», «Según entrega») en la columna `Hora Límite` (05) | Dispara `cadencia()` (`motor.py:2261-2325`) y renombra la columna; el plazo va dentro del texto de la tarea (§4), la columna lleva siempre una hora (B9) |
| `bridge.py` **no se usa** en este producto | Los textos los escriben subagentes Anthropic desde esta SPEC (matiz de John del 2026-09-04). `bridge.py` queda para el copy SEO de la landing en F3 |

### R8 · `guia-restaurante-mexicano.ts:124` dice «Cinco de Mayo» sin matiz

Es la página con la que este kit hace cross-link en las dos direcciones (D9 §1, cesta de use-case). Su copy vivo no lleva el matiz «campaña sobre todo para EE. UU.» que exige D8/G4 para este producto. **No se arregla en este producto** — esa ficha no es de este kit —; se documenta para que la sesión que la toque lo corrija.

---

## Autocomprobación de esta SPEC

- **(a)** Los 11 ficheros tienen todas sus hojas con propósito, rango de tareas y ejemplos redactados en forma final: `01` (2 hojas) · `02` (2) · `03` (3) · `04` (3) · `05` (2) · `06` (6) · `07` (2) · `08` (2) · `09` (1) · `BONUS-01` (1) · `BONUS-02` (1) = **25 hojas de contenido + 11 de `Instrucciones`**. ✓
- **(b)** D1-D13 aparecen las trece en la tabla del §1, con su cita al research; D14-D20 son nuevas y van justificadas. ✓
- **(c)** `65 °C` aparece en este documento **sólo** en frases que dicen que la cifra está **derogada** (§2 aviso, §4 prohibiciones, §5 gate G2, §7 R1). ✓
- **(d)** Sin caracteres no latinos. Los únicos símbolos no ASCII son los de la tipografía española y los de la familia: `° − ≤ ≥ ✓ ☐ — ▸ · « » ñ á é í ó ú ü ¿ ¡`. ✓
