# Refutación de la SPEC «Tareas Recurrentes: Taquería Mexicana» — 2026-09-20 (ronda ÚNICA por agente)

Refutador: 1 agente Opus con las tres lentes (A cifras/legal · B estructura/motor · C editorial/comercial), 277 k tokens.
Veredicto: **NO LISTO** → correcciones decididas por el orquestador (todas se aplican; la ronda 2 es un gate de script).
Fichero refutado: `scripts/productos-digitales/kit-tareas-taqueria/02-SPEC-kit-tareas-taqueria.md` (822 líneas).

## 🔴 Bloqueantes (decisión tomada)

**B1 · BONUS-02 fuera del alcance del motor.** La matriz `TAREA / ACCIÓN | Ene…Dic` solo se reconoce con `sub_cb()`
(`motor.py:1367-1369`), y D17 deja la taquería fuera de `SUBFAMILIA_CB` (`motor.py:4495-4501`). **Decisión: opción (a)**,
BONUS-02 al molde calendario de la familia NO-CB, cabecera exacta `Mes | Fecha / Evento | Tareas Clave | Antelación`
(`fila_calendario`, `motor.py:876`, exige literalmente `Antelación` + `Fecha / Evento` o `Evento` en las 8 primeras filas),
24-36 filas (2-3 por mes). Reescribir §3 BONUS-02, §3.1 y G9. Referencia LIVE: `kit-tareas/BONUS-02-calendario-anual-tareas.xlsx`.

**B2 · El molde de generador v1 NO emite el molde v2.0 de §3.0.** Medido en `scripts/generate-tareas-restaurante-creativo.py`:

| §3.0 de la SPEC (= sushi-bar real) | Lo que emite el generador v1 |
|---|---|
| `Nº \| Tarea \| Zona \| Responsable \| Hora Límite \| ✓ Completada \| Firma` | `:161` `# \| Tarea \| Zona \| Responsable \| ✓ \| Hora \| Notas` (rótulos y orden distintos) |
| DV `"✓,—,N/A"` (`motor.py:168`) | `:150`, `:237`, `:300` → `"✓,✗,—"` (3 sitios) |
| Anchos 5·48·14·20·13·12·16 | `:133-139` 5·45·14·18·12·12·15 |
| Fila 2 = `Fecha: ___/___/______  Turno: ☐…  Responsable: ___` | `:145-147` fila 2 = subtítulo; firma al pie (`:208`) |
| Cabecera en **fila 4** (fila 3 vacía) + `ws.freeze_panes = "A5"` | sin `freeze_panes`; cabecera repetida en cada sección (`:160-168` dentro del bucle) y numeración reiniciada por sección (`:170`) |
| Fila `Tareas completadas: X de Y` + 5 filas verdes libres SIN número en A | no existen |
| Pie `— Kit de Tareas Recurrentes · <kit> · AI Chef Pro · aichef.pro` | `:214` `© 2026 AI Chef Pro · aichef.pro` |
| BONUS-02 molde calendario (B1) | `create_calendar_sheet` (`:271-300`) emite un tercer molde que no casa con nada |

Con el v1 tal cual, `cabecera_checklist` (`motor.py:765-780`) devuelve `None` → ninguna hoja entra en alcance → G9/G11 rojos.
**Decisión:** §0 «Molde de generador para F2» debe decir que F2 escribe `scripts/generate-tareas-taqueria.py` con las
helpers REESCRITAS como contrato cerrado por UN agente antes de repartir contenido: `create_task_sheet` (rótulos, orden, DV,
anchos, fila 2, `freeze_panes="A5"`, una sola cabecera por hoja, numeración continua, contador + 5 filas libres sin número,
pie), `create_blank_template_sheet` (`:217-270`, misma DV mala), `create_calendar_sheet` → molde calendario,
`add_instructions_sheet` → los 5 bloques v2.0, `PRODUCT_SUBTITLE`, `OUTPUT_DIR` → `astro-site/public/dl/kit-tareas-taqueria/`.
Añadirlo a §7 R7 (hoy solo figura el `OUTPUT_DIR`). El contrato se valida comparando la estructura XML emitida con la del
sushi-bar (fila 4, `ySplit`, lista de DV, anchos, pie) ANTES de escribir contenido.

**B3 · Env var de Stripe mal.** Los 19 kits usan `VITE_STRIPE_PAYMENT_LINK_TAREAS_<CONCEPTO>` sin `KIT_`
(`kit-tareas-sushi-bar.ts:12`; `grep -n stripeEnvKey astro-site/src/data/productos/tareas/*.ts` 20/20). Con el nombre mal,
`types.ts:92` cae a `#comprar` sin error de build. **Decisión:** `stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_TAQUERIA'`
y la variable en Netlify con ese nombre, scope builds. Corregir §6.1 fila 11.

**B4 · Faltan `kit-tareas-taqueria-access.astro` y `kit-tareas-taqueria-library.astro`** (el grep por pid no los ve;
los 19 kits tienen los tres `.astro`). Se generan con `python3 scripts/astro-migration/fase5-generate-zona-app.py` tras el
alta en `zona-app.ts`. Molde: landing con `whatsapp={false}` + `omitGlobalApp` (`kit-tareas-sushi-bar.astro:21-22`);
`-library` con `noindex whatsapp={false}`; `-access` con `title={ACCESS_TITLE} noindex` + `FunctionsOriginPatch`.
**Decisión:** filas 23 y 24 en §6.1 + mención del generador. El censo del grep son 21 ficheros (no 22): con estos, 24.

## 🟠 Medias (todas se aplican)

- **B5** D18 inflado: cuenta filas numeradas vacías. Medido (filas con entero en A y texto en B): sushi-bar **211**
  (no 266), asador **223** (no 238), base **522** (no 567). Densidad de la familia 13-15 tareas/hoja. **Decisión: objetivo
  300, rango 270-330**, 22 hojas intocables. Reajustar §3.1 (hoy suma 290-368) y la justificación de D18.
- **B6** `Responsable` y `Hora Límite` van RELLENAS en los 19 kits (`kit-tareas/01:D6='Cocinero apertura', E6='07:00'`;
  sushi `D6='Itamae', E6='10:00'`) y `motor.py:1755-1758` deriva la hora ancla de esa columna. **Decisión:** F2 rellena
  ambas con puesto y hora sugeridos; lo editable es sobrescribirlas. Corregir §3.2, §3.6 y las 6 menciones «celda para el
  operador»; añadir a §4.
- **B7** Cabecera de columnas en la **fila 4** con la fila 3 vacía (`ySplit="4"`), no en la 3. Corregir §3.0 (`:156`).
- **B8** Pie real del motor (`motor.py:1777-1779`): `— Kit de Tareas Recurrentes · Taquería Mexicana · AI Chef Pro ·
  aichef.pro`, segmento del kit idéntico en los 11 ficheros (`ctx['kit'] = _mayoria(kits)`). Corregir G9 y §3.0.
- **B9** En el 05, `Hora Límite` con «7 días» o «Según entrega» dispara `cadencia()` (`motor.py:2261-2325`) y renombra la
  columna. **Decisión:** plazo en el texto de la tarea («…, con su plazo: ______ días») y la columna lleva una HORA.
  Añadir a §4 y a §7 R7.
- **C1** 34 de 119 ejemplos juntan dos acciones. **Decisión:** relajar §4.3: «Una tarea = un momento, una zona y un
  responsable. Se admite `verbo + y anotar/registrar/comprobar` cuando el registro es parte del mismo acto. NUNCA dos
  momentos distintos». Partir `:231` en tres, `:229` en dos, `:226` en dos.
- **A1** U15 «12-24 h» sin fuente. **Decisión:** celda del operador: `Mantener el marinado a ≤ 4 °C el tiempo definido en
  tu ficha: ______ h`; U15 reetiquetado [estimado] (práctica de oficio).
- **A2** G3 daría falsos positivos (`termómetro digital`). **Decisión:** G3 = 0 apariciones de `registro horario digital`,
  `control horario digital`, `fichaje digital`, `horario digital`, `obligatorio en 2026`, `digital obligatori`.
- **A3** G5: barrido **insensible a mayúsculas**; `Molcajete` fuera de la lista, como control negativo aparte; añadir
  `maría`, `número`, `sésamo`, `rotación`; `Nº` = N + U+00BA (ordinal), el grado = U+00B0.
- **C2** §6.1 fila 16 (`products-catalog.ts`): sin comentarios entre `description: {` y `es:` (parser del 30-ago);
  `name: { es: 'Tareas: Taquería Mexicana', en: … }`, `price: '€14'`; correr el gate de recuento del parser.

## 🟡 Bajas (todas se aplican)

- **D1** `censo-entregables.py:214` es `hoja_larga`, informativo (no cuenta para `--fail`): el censo no comprueba `/`.
  Corregir `:153` y R7; el único gate de nombres de pestaña es G9.
- **D2** Longitudes mal contadas: `Apertura Taquería` 17, `Cierre Taquería` 15, `Marinado y Montaje del Trompo` 29,
  `Calendario Anual` 16.
- **D3** D17: `promesas`/`limite_unico`/`PLANTILLA_09` los activa `main.py` por `getattr` sobre el módulo de contenido, no
  `SUBFAMILIA_CB`; lo que `sub_cb()` gatea son 11 puntos del motor (`:156, 1263, 1367, 1369, 2036, 2152, 2286, 2293, 4129,
  4216, 4303, 4767`). Decisión correcta, razón a reescribir.
- **D4** Citas: D1 → `01-research…md:518-560` (precio), D3 → `:273` y `:566` (si aplica).
- **D5** `:770` «22 ficheros» → 21 del grep + 2 `.astro` de B4 + `dl/` = 24 piezas.
- **D6** `comingSoon`: `ProductosDigitalesHubPage.astro:997` y `src/pages/ProductosDigitales.tsx:981`.
- **D7** R8 nuevo: `guia-restaurante-mexicano.ts:124` dice «Cinco de Mayo» sin matiz; es la página del cross-link D9.
- **D8** §3.3 sección → `CONGELACIÓN DE CRUDOS (SI APLICA) Y RECALENTADO`, coherente con §4.
- **D9** Nota en §3.4: 74 °C/1 s (aves, U11) y 74 °C/15 s (recalentado) conviven en `Guisados y Rotación`; retirar el 04
  de «dónde se imprime» de U11 o anotar la distinción.
- **D10** R1: 24 ocurrencias ✓ en **18 ficheros de 14 productos** (añadir casual, japonés, nikkei, peruano).
- **Pestañas del 06**: `Salsero` → `Salsas`, `Tortillero` → `Tortillería` (sin género, sin barra); fila 1 mantiene el
  prefijo `Checklist: ` del molde.

## OK verificados (no repetir): D14 U+0020 (`RX_GRADOS`, `motor.py:237`), D15 U+2212, «Hora Límite» con tilde detectada
fuera de CB (`_sin_tildes`, `:3409`), 25 pestañas ≤ 31 sin `/`, 0/119 ejemplos > 110 chars, 0 no latinos, §3.1 suma
290-368, U17 art. 34.9 ET, D5 válida con o sin RD, par 14 €/€69/-80 % (el de 12 € es -69 %), alérgenos, Cinco de Mayo,
65/75 °C solo en prohibiciones, glosario, «si aplica» del trompo con `N/A` fuera del denominador, `SUST_APPCC` lista
blanca, 9 scripts existen, `use-cases-content.es.ts:3580`, `zona-app.ts:67`, D19, D11.

## Estimación de F2 del refutador: 0,7-1,1 M tokens y 2,5-3,5 h si el contrato de helpers se cierra ANTES de repartir.
Consumo F1: research 0,24 M · SPEC 0,21 M · refutación 0,28 M = **0,73 M** de los 2,5 M del producto.
