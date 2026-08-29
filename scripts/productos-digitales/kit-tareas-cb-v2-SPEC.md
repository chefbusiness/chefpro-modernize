# Kits de Tareas portados de ChefBusiness — v2.0 (SPEC, 2026-08-29)

Sub-familia: `kit-tareas-sushi-bar` (representante, R1 hecha) · `kit-tareas-asador` ·
`kit-tareas-marisqueria` · `kit-tareas-panaderia` · `kit-tareas-food-truck` ·
`kit-tareas-tapas-bar` · `kit-tareas-chef-privado`.

Origen: `auditorias/kit-tareas-sushi-bar-R1.json` (76 hallazgos: DOM 31 · TEC 20 · COM 25;
tres lentes con veredicto «no listo»). Referencias: `kit-tareas-v2-SPEC.md` (§1-§11) y el paquete
`kit-tareas-v2_0/` (motor de FAMILIA 2.6, `contenido_<pid>.py`, `main.py --producto --dry-run`),
más el método de 5 tandas del handoff `SESSION_HANDOFF_2026-08-22-B-fase-a-entregables.md` §7-§9.

**Regla dura heredada:** `astro-site/public/dl/<pid>/` NO se toca. Todo se prueba con `--dry-run`
sobre scratchpad; la ejecución real la hace el orquestador con `KIT_TAREAS_APPLY=1` y respaldo.
Nada de builds ni de navegador; un `python3` cada vez; `istats cpu temp` antes de cada uno.

---

## 0. Alcance medido y VEREDICTO sobre el motor 2.4/2.6

### 0.1 La sub-familia son TRES moldes, no uno

Medido con `openpyxl` + `motor.geometria` / `motor.geometria_p4` / `motor.hojas_reconocidas`
sobre los 73 ficheros (2026-08-29). Éste es el hallazgo que condiciona toda la SPEC:

| Molde | Kits | Ficheros | Hoja `Instrucciones` | Hojas que el motor reconoce | Fórmulas | Desplegable | Tildes/ñ |
|---|---|---|---|---|---|---|---|
| **▸ (7 columnas)** | sushi-bar, asador | 11 + 11 | **11/11 y 11/11** | 16 ▸ · 17 ▸ | 30 · 32 | `"✓,—,N/A"` | **rotas** |
| **PLANO (1 hoja/fichero)** | marisqueria, panaderia, food-truck, tapas-bar | 11 ×4 | **0/11 en los cuatro** | **0** | **0** | `"✓,—,N/A"` en 7/11 | **rotas** |
| **P4 (AI Chef Pro)** | chef-privado | 9 | 9/9 | 11 P4 | 22 | `"✓,✗,—"` | **correctas** |

- **Molde ▸** — cabecera en la fila 4: `Nº · Tarea · Zona · Responsable · Hora Limite ·
  ✓ Completada · Firma`. Es el molde del representante de la familia menos la columna `Notas`.
  `motor.geometria` lo reconoce entero.
- **Molde PLANO** — cabecera en la fila **3**: `Area · Tarea · Responsable · Hora · OK ·
  Observaciones` (en `05` es `Categoria · Tarea · Frecuencia · Prioridad · Estado · Notas`).
  Un solo `worksheet` por fichero, **sin columna `Nº`, sin fila de contador, sin hoja
  `Instrucciones`, sin línea de versión y sin bio**. Ejemplo verificable:
  `kit-tareas-tapas-bar/01-apertura-cierre-tapas-bar.xlsx:'Apertura y Cierre'` — `A1` marca,
  `A2` título, `A3` cabecera, `A4/A12/A19/A25` bandas de sección, `A35` pie; 0 fórmulas.
- **Molde P4** — el de catering/hotel/heladería: cabecera **repetida en cada sección**
  (`# · Tarea · Zona · Responsable · ✓ · Hora · Notas` en la fila 5 y de nuevo en cada bloque),
  bandas con emoji, pie `© 2026 AI Chef Pro`. Marca de agua distinta: chef-privado **no lleva**
  «ChefBusiness Consultoria Gastronomica» en ninguna celda (los otros seis sí, 11-13 veces cada uno).

### 0.2 Veredicto: el motor 2.6 reconoce DOS de los tres moldes, y con tres defectos demostrados

Pruebas reales (`--dry-run --solo motor`, scratchpad
`…/9a6ebdb7…/scratchpad/cb-spec/dryrun-kt/`; informes `sushi-motor.json`, `asador-motor.json`,
`tapas-motor.json`, `chefpriv-motor.json`):

| Producto | `en alcance` | cambios | fórmulas nuevas | recuento | `f_negocio` / `f_caja` / `f_areas` |
|---|---|---|---|---|---|
| sushi-bar | **8/11** | 71 | **30** | 204 tareas | None / None / `01-apertura-cierre-sushi.xlsx` |
| asador | **9/11** | 75 | **32** | 223 tareas | None / None / `01-apertura-cierre-asador.xlsx` |
| tapas-bar | **0/11** | 11 (sólo metadata) | **0** | 0 | None / None / None |
| chef-privado | 0/9 ▸ pero **11/11 P4** | 50 | **22** | 224 tareas | None / None / None |

**Lo que SÍ resuelve el motor tal cual, sin tocar una línea:**

- Contador honesto y filas libres en los 33 checklists ▸ de sushi-bar y asador. Verificado en el
  dry-run: `01-apertura-cierre-sushi.xlsx:'Apertura Barra Sushi'!D42` pasa a
  `=COUNTIFS(B5:B40,"?*",F5:F40,"✓")` y `F42` a `=COUNTIF(B5:B40,"?*")-COUNTIF(F5:F40,"N/A")`,
  con 5 filas verdes libres DENTRO del rango. **Cierra DOM-17, TEC-04, TEC-05, COM-12 y COM-13.**
- Mensaje de error del desplegable (`DV_ERROR`), verde en las celdas editables, protección sin
  contraseña, `print_area`, alturas automáticas, bio anclada y `Versión 2.0` en **11/11**
  `Instrucciones`, metadata coherente en 11/11 ficheros (m5).
- **El molde P4 arregla chef-privado él solo, y es el hallazgo con más dinero detrás de esta
  sub-familia después del anisakis.** Sus 11 hojas mienten en el contador porque el `COUNTIF`
  original cuenta las cabeceras repetidas de cada sección, y la caché inyectada en la Fase A hace
  que el fichero **se imprima ya mintiendo, sin recalcular**:

  | Fichero : hoja | Contador impreso HOY | Tareas reales |
  |---|---|---|
  | `03-equipo-transporte.xlsx:'Equipo Transporte'!C57/E57` | **«5 de 41»** | **36** |
  | `01-ficha-cliente-consulta.xlsx:'Ficha Cliente'!C47/E47` | «3 de 35» | 32 |
  | `04-seguridad-alimentaria-appcc.xlsx:'APPCC Móvil'!C39/E39` | «3 de 27» | 24 |
  | `BONUS-01-briefing-pre-servicio.xlsx:'Briefing'!C36/E36` | «3 de 24» | 21 |
  | `05-checklist-servicio.xlsx:'Post-Servicio'!C28/E28` | «2 de 18» | 16 |

  9 de las 11 hojas están mal (las dos de una sola sección, `'Durante Servicio'` e
  `'Historial Servicios'`, salen bien por casualidad). Tras el dry-run, `E57` pasa a
  `=COUNTIF(B6:B56,"?*")-COUNTIF(B6:B56,"Tarea")-COUNTIF(E6:E56,"N/A")` → **«0 de 36»**, y el
  desplegable `"✓,✗,—"` se unifica a `"✓,—,N/A"` en las 11 hojas.

**Lo que NO resuelve (extensión obligatoria). Tres defectos DEMOSTRADOS, no supuestos:**

1. **El molde PLANO es invisible.** `tapas-bar` sale con `en alcance 0/11`, 0 fórmulas y un solo
   cambio por fichero (metadata). El motor emite 9 avisos `(j)` («no tiene hoja Instrucciones — no
   se inventa ninguna; lo decide el orquestador») y **guarda igual los 11 ficheros**. Un molde
   desconocido no puede terminar en «guardado sin novedad»: tiene que ABORTAR.
2. **El fichero de áreas se remite a sí mismo (T-01 otra vez).** En el dry-run,
   `01-apertura-cierre-sushi.xlsx:Instrucciones!B35` imprime
   «▸ 01-apertura-cierre-sushi.xlsx — el mismo día con el DETALLE por área (barra sushi).»
   **dentro del propio 01**, y `B36` añade «▸ Estás en 01-apertura-cierre-sushi.xlsx.». Los otros
   8 ficheros citan correctamente el 01. Causa: la rama genérica de `_bloque_conecta` excluye
   `f_negocio` y `f_caja` de los candidatos, pero nunca comprueba si `fname == f_areas`, que es
   el único papel que estos kits tienen.
3. **La plantilla personalizable queda peor que antes.** `09-plantilla-personalizable.xlsx`
   entra en alcance (3 cambios) pero con **0 fórmulas**: `geometria` devuelve `contador=None` y el
   motor no CREA contadores, sólo reescribe los que encuentra. Resultado del dry-run: sus
   `Instrucciones` ahora traen los bloques «Cómo cuenta el contador» (`B16-B20`) y «Filas libres»
   (`B22-B25`) prometiendo un total que se recalcula y 5 filas verdes libres — y la hoja
   `'Plantilla en Blanco'` sigue sin contador y sin filas libres. **DOM-16 / TEC-03 / COM-11 pasan
   de un renglón mentiroso a tres bloques mentirosos.** Idéntico en asador.

Y dos limitaciones que no son defectos pero condicionan los gates:

4. **`f_negocio` y `f_caja` son `None` en los 7 kits.** No existen los ficheros 08-negocio y
   09-caja de la familia. `main.py` emite el fallo *«no se ha identificado el fichero de NEGOCIO
   del kit: DOM-06 no se ha aplicado a nada»* y sale con `exit 1` **en los cuatro dry-runs**. Es
   estructural, no un defecto del producto: hay que declararlo.
5. **La ortografía no la toca nadie.** Tras el dry-run, `01:Instrucciones!B4` sigue diciendo
   «Como usar estas plantillas» y `B15` «Ajusta las horas limite a tus horarios reales». El motor
   reescribe el bloque entero y **reinyecta el texto sin tilde** que venía del fichero.

### 0.3 Alcance de la ortografía, medido

Palabras inequívocamente mal escritas (sin tilde o sin ñ), con frontera de palabra, en celdas y
en nombres de pestaña:

| Kit | Palabras | Celdas | Pestañas mal escritas |
|---|---|---|---|
| sushi-bar | **233** | 181 | `08!'Temporadas Pescado Espana'` |
| asador | **202** | 152 | `03!'Temperaturas Coccion'` |
| marisqueria | **122** | 95 | — |
| panaderia | **101** | 77 | `03!'Hornos y Coccion'` · `BONUS-01!'Briefing Produccion'` |
| tapas-bar | **94** | 74 | — |
| food-truck | **93** | 74 | `02!'Operaciones Moviles'` · `03!'APPCC Movil'` |
| chef-privado | **0** | 0 | — (192 celdas con acentos correctos) |
| **TOTAL** | **845** | **653** | **6 pestañas** |

Lo más caro de leer: `Ano: ______` en las dos hojas anuales de sushi-bar (`08!A2` y
`BONUS-02!A2`), `ANO NUEVO` como encabezado de sección (`08!'Eventos Especiales'!A13`),
`OTONO`, `banos`, `manana`, `desempeno`, `Anade`, y la razón social
**«ChefBusiness Consultoria Gastronomica»** repetida 11-13 veces por kit en los seis. Los seis
kits SÍ saben escribir la ñ en alguna celda (`08!'Eventos Especiales'!B16` dice «Año Nuevo
japones» tres filas debajo del `A13` que dice «ANO NUEVO»): es *stripping* parcial, no estilo.

### 0.4 El agregador `mega-pack-tareas`

Existe (`netlify/functions/get-download-urls.ts:392`, `src/pages/MegaPackTareas.tsx`,
`MegaPackTareasDashboard.tsx`); **no** tiene fichero de datos en
`astro-site/src/data/productos/tareas/`. Agrupa **13 kits / 155 entradas**, y de esta sub-familia
**sólo incluye `kit-tareas-chef-privado`** (9 entradas `kit-tareas-chef-privado__*`, mismas rutas
físicas). Sushi-bar, asador, marisquería, panadería, food-truck y tapas-bar **no están dentro**.
Consecuencia operativa: los cambios en chef-privado llegan al mega-pack sin trabajo extra (mismos
ficheros), pero **el gate LIVE de cierre tiene que correr también sobre `mega-pack-tareas`**.

---

## 1. MOTOR — qué se reutiliza y qué se extiende

### 1.1 Se reutiliza tal cual (sin tocar `motor.py`)

Todo lo firmado en `kit-tareas-v2-SPEC.md` §2 (checklists ▸), §8 (ronda 2), §9 (tandas 3-5 y motor
2.4) y §10.1 (m5, metadata en todos los ficheros): contador honesto con `COUNTIFS`, 5 filas libres
dentro del rango, `DV_LISTA` + `DV_ERROR`, verde `E8F5E9` en editables, CF de fila completada,
cabeceras `Día`/`Cadencia`/`Antelación`/`Cuándo`, `texto_grados` (`−18 °C` con U+2212),
referencias honestas al Pack APPCC, bio anclada, `Versión 2.0`, protección sin contraseña,
`print_area`, A4, `autoalto`, `inject_cache` al final, gate de idempotencia y censo `--fail`.

El bloque §1 completo (caja y negocio) queda **inerte** en esta sub-familia: no hay 08/09.

### 1.2 Extensiones obligatorias (`motor.py` + `main.py`)

Se numeran **CB-E1 … CB-E9** para no colisionar con los `m1…m8` de la familia.

**CB-E1 — `ortografia()`: barrido de tildes y ñ.** Paso NUEVO, ejecutado **después** de todo lo
demás y antes de `inject_cache` (si corriese antes, la reescritura de `Instrucciones` volvería a
meter el texto viejo: demostrado en el dry-run con `B4 = 'Como usar estas plantillas'`).
- Fuente: diccionario explícito de lemas (`LEX_TILDES`), no heurística. Cada entrada es
  `sin → con`, con frontera de palabra y respeto de mayúsculas/versalitas
  (`Ano→Año`, `ANO→AÑO`, `OTONO→OTOÑO`, `Espana→España`, `Consultoria→Consultoría`,
  `Gastronomica→Gastronómica`, `Limite→Límite`, `Como usar→Cómo usar`, `Anade→Añade`, …).
- **No toca**: celdas con `data_type == 'f'`, cadenas que contengan `://`, `aichef.pro`,
  `chefbusiness.co`, `@`, códigos (`FAO`, `RD`, `CE`, `UE`, siglas en mayúsculas de ≤5 letras),
  ni las etiquetas-contrato del motor (`ETIQ_*`, `CAB_*`, `DV_LISTA`).
- **Sí toca** nombres de hoja (renombrado con `wb[old].title = new`, que arrastra las referencias
  internas de openpyxl) y el `title`/`subject` de la metadata.
- Ambigüedades (`mas/más`, `esta/está`, `como/cómo`, `el/él`, `si/sí`) **no van por diccionario**:
  se resuelven por contexto en el módulo de contenido de cada kit, celda a celda, con la lista
  que emite el propio gate.
- **Gate `gates.ortografia`**: 0 palabras de `LEX_TILDES` supervivientes en celdas y en nombres de
  hoja. Rojo si ≠ 0. Baseline a batir: 845 / 653 / 6.

**CB-E2 — `crear_contador()`: crear el contador donde no existe.** Si `geometria(ws)` devuelve
geometría válida pero `contador is None`, el motor escribe la fila de totales con el mismo patrón
que las hermanas y añade las 5 filas libres. Aplica a `09-plantilla-personalizable.xlsx:'Plantilla
en Blanco'` de sushi-bar y asador. Concretamente, tras las 15 filas numeradas y antes de
`'Verificado por:'`: etiqueta `Tareas completadas:` fusionada `A:C`, `D` con
`=COUNTIFS(B5:B<ult>,"?*",F5:F<ult>,"✓")`, `E` con `de`, `F` con
`=COUNTIF(B5:B<ult>,"?*")-COUNTIF(F5:F<ult>,"N/A")`.
**Alternativa si el orquestador prefiere no crear nada:** condicionar los bloques «Cómo cuenta el
contador» y «Filas libres» de `instrucciones()` a que la hoja TENGA contador. Lo que no puede
quedarse es la combinación actual.

**CB-E3 — molde REGISTRO.** `fila_registro_appcc(ws)`: cabecera con `#`/`Nº` en A, ≥5 rótulos, y
al menos uno de `{Fecha, Temp, Lote, Caducidad, Firma}`; devuelve `(fila, cols)`. Alcanza a
`kit-tareas-sushi-bar/03-seguridad-anisakis-appcc.xlsx` (`'Registro Congelacion'` A5:I5,
`'Trazabilidad Pescado'` A3:H3, `'Temperaturas Diario'` C4:I11) y a
`kit-tareas-marisqueria/03-trazabilidad-appcc-marisco.xlsx:'Trazabilidad APPCC'`. Aplica:
`number_format` de fecha `DD/MM/YYYY`, DV de lista en la columna de verificación, DV decimal y
formato `0.0 "°C"` en las de temperatura, CF de fuera-de-rango, altura explícita en las cabeceras
con `wrap_text` (TEC-19: hoy `row_dimensions` está vacío), protección y `print_area`.
**Cierra TEC-07, TEC-08 y TEC-19.**

**CB-E4 — Instrucciones por TIPO de entregable.** `_bloque_personalizar(papel)` con cuatro
variantes: `checklist` (la actual), `registro`, `formulario` y `calendario`. Hoy el bloque es
literal único y en tres ficheros del representante describe columnas que no existen:
`03:Instrucciones!B14/B16/B17` habla de responsables, horas límite y filas de tareas vacías en un
libro de registros, y `BONUS-01:Instrucciones!B13` promete «celdas verdes» en una hoja con **cero
rellenos**. **Cierra TEC-10 y COM-19.**

**CB-E5 — molde PLANO.** El grueso del trabajo. `geometria_plano(ws)`: cabecera en la fila 3, `Tarea`
en B, columna de marca llamada `OK` **o** `Estado`, sin columna `Nº`; bandas = celdas combinadas
`A:F`. Acciones, todas sobre la hoja única de cada uno de los 44 ficheros:
- contador al pie, con el patrón de la familia (denominador honesto);
- 5 filas libres en verde dentro del rango contado, con DV y CF;
- DV `"✓,—,N/A"` **también en `05-tareas-manager.xlsx`**, que hoy es el único fichero de los 11
  sin desplegable en los cuatro kits porque su columna de marca se llama `Estado`, no `OK`
  (escape de la Fase A verificado en los cuatro);
- CF de fila completada, verde en `Responsable`, `Hora`, `OK`/`Estado` y `Observaciones`;
- protección sin contraseña, `print_area`, alturas;
- hoja `Instrucciones` — **decisión abierta, §5 duda 1**;
- bio + `Versión 2.0` — sin hoja `Instrucciones` no hay dónde anclarlas (regla (j): el motor no
  inventa hojas). Si se decide no crearla, van en una fila nueva sobre el pie `A35`.

**CB-E6 — abortar si el molde no se reconoce.** Nueva `MoldeDesconocido(RuntimeError)`, hermana de
`KitAmbiguo`. Si tras `contexto()` el producto tiene **0 hojas reconocidas** por `geometria`,
`geometria_p4`, `geometria_plano`, `fila_registro_*`, `fila_calendario` o `es_briefing`, se aborta
con el informe escrito. Hoy tapas-bar «pasa» con 11 ficheros guardados y `censo --fail` en verde.

**CB-E7 — kit sin negocio ni caja.** `CTX['sin_caja'] = True` cuando `f_negocio is None and
f_caja is None` **y** ningún fichero tiene firma de recuento, registro mensual, liquidación o
registro de eventos. Con la bandera puesta, `gates.negocio_precargado` pasa de **fallo** a
**informativo**, y `frase_niveles()` emite una tercera variante (`FRASE_NIVELES_SOLO_AREAS`) que
no promete un nivel de «negocio» ni de «dinero» que el kit no tiene.

**CB-E8 — el fichero de áreas no se remite a sí mismo.** En `_bloque_conecta`, la rama de `f_areas`
se comprueba **antes** que la genérica, igual que T-01 hizo con `f_negocio`/`f_caja`. Si
`fname == CTX['f_areas']`, la cola es «Estás en …: es el DETALLE por área del día» y **no** se
enumera a sí mismo. Celda de prueba: `01-apertura-cierre-sushi.xlsx:Instrucciones!B35`.

**CB-E9 — legibilidad impresa.** (a) ancho de la columna `Tarea` de 48 a 60 en el molde ▸ (la fila
cabe: `5+60+14+20+13+12+16 = 140`, dentro de A4 apaisado con `fitToWidth=1`) o `wrap_text` con alto
30 pt — hay **110 celdas de tarea** por encima de 48 caracteres en sushi-bar; (b) ancho de `B` de
28 a 46 en `03:'Temperaturas Diario'`, donde `B6` mide 43 caracteres; (c) `wrap_text` + alto en las
11 hojas `Instrucciones` (`B21` mide 104 caracteres con la columna a 80); (d) CF de fila completada
a `A5D6A7`, para que se distinga del verde base `E8F5E9` en las columnas `Zona` y `Responsable`.
**Cierra TEC-15, TEC-16, TEC-17 y TEC-18.**

### 1.3 Gates nuevos de la sub-familia

| Gate | Qué exige | Rojo si |
|---|---|---|
| `ortografia` | 0 lemas de `LEX_TILDES` en celdas y pestañas | ≠ 0 |
| `molde` | cada fichero clasificado en ▸ / P4 / PLANO / REGISTRO / calendario / briefing | alguno sin clasificar |
| `contadores` | toda hoja con geometría de checklist tiene contador, y su valor cacheado = tareas contadas a mano | discrepancia ≥ 1 |
| `limite_unico` | cada equipo nombrado (cámara, vitrina, congelador, expositor) tiene **un solo** rango en todo el kit | dos rangos distintos |
| `citas_legales` | toda celda que nombre una norma pasa la lista blanca de §2.0 | cita fuera de lista |
| `promesas` | cada término distintivo del grid/CTA/bonus de la landing aparece en el corpus del kit | término ausente |
| `autorreferencia` | ningún «Se conecta con» nombra su propio fichero | ≥ 1 |

---

## 2. CONTENIDO por kit (`contenido_<pid>.py`)

### 2.0 Lista blanca normativa de la sub-familia (vale para los 7)

Redacción obligatoria, con la fuente en la celda de nota inmediatamente debajo del bloque:

- **Anisakis:** «Congelación previa obligatoria para pescado que se sirva crudo, marinado,
  en salazón, ahumado en frío o poco cocinado: **−20 °C en la totalidad del producto durante al
  menos 24 h, o −35 °C durante al menos 15 h**.» Nota: «Rgto. (CE) 853/2004, Anexo III, Secc. VIII,
  Cap. III.D, modificado por el Rgto. (UE) 1276/2011; exigido en España por el art. 8.1 del
  RD 1021/2022, que derogó el RD 1420/2006. El art. 8.2 obliga además a informar a la persona
  consumidora mediante carteles o cartas-menú.» (ver la decisión ANISAKIS-2026-08-29 al final)
- **Excepción:** «Quedan exentos los productos de la acuicultura criados con pienso que no puede
  contener parásitos y en un entorno libre de parásitos vivos, siempre que el proveedor lo
  acredite por escrito (Rgto. UE 1276/2011). Archiva esa acreditación junto a este registro.»
- **Los 7 días NO son la norma**: si se conserva, va como criterio propio del local
  («mínimo legal 24 h; este kit propone X como margen reforzado»), nunca atribuido al RD.
- **Alérgenos:** los 14 del Anexo II del **Rgto. (UE) 1169/2011**, con los propios del negocio
  destacados.
- **Registro sanitario:** el RGSEAA (**RD 191/2011**) **no se renueva** anualmente; se comunican
  modificaciones o cese.
- **Extintores:** revisión trimestral del titular + anual por empresa autorizada, retimbrado a los
  5 años (**RD 513/2017, RIPCI**).
- **Un solo límite crítico por PCC** en todo el kit.

### 2.1 Tabla por kit

| Kit | Legal | Horarios / cadencias | Alérgenos | Temporadas | Hojas NUEVAS (dentro de libro existente) | Tildes |
|---|---|---|---|---|---|---|
| **sushi-bar** (representante) | Anisakis mal citado en `03:Instrucciones!B7` y `03:'Registro Congelacion'!A2/B27` (DOM-01, COM-01, TEC-11); dos límites `−20`/`−18` (DOM-02, COM-16); falta la excepción de acuicultura (DOM-15); cámara `−2 a 0` vs `0-2` (DOM-12, COM-15) | Cadena del arroz imposible: `02:'Protocolo Arroz Sushi'!E6-E10` (reposo 30 min de 10:20 a 10:25) y desalineada con `01!E13-E18` (DOM-03, COM-18); vitrina «encender y verificar 2-4 °C» a las 10:00 (DOM-25); pedido a lonja a las 22:00/23:30 (DOM-24); turno Almuerzo/Cena con horas sólo de mediodía y sin 2.º lote de arroz (DOM-11); `05` anuncia 3 checklists y trae 2 (COM-17); 07 mensual vs BONUS-02 semestral (COM-10) | `06:'Sala y Servicio'!B8` enumera 4 y **omite pescado** (DOM-07); `03` no tiene ninguna hoja de alérgenos pese a venderlo (TEC-12) | Bonito y atún rojo **cruzados** (`08!B11`/`B16`, `BONUS-02!A7`/`A8`); sardina en marzo; lubina en otoño (DOM-09, DOM-18, COM-03) | `03` → **Matriz de Alérgenos**, **Registro de pH del arroz**, **Control de Recepción**; `01` o `03` → **Registro de Mermas**; `06` → **Delivery y Take Away**, **Office y Lavado**; `05` → **Comparativa de Proveedores** y **Reporting Diario** | 233 / 181 / `08!'Temporadas Pescado Espana'` |
| **asador** | Sin citas normativas propias (0 encontradas). Verificar las temperaturas de combustión declaradas: `02!B24-B26` («encina 800 °C, quebracho 900 °C, marabú 750 °C») | Coherencia de `03:'Temperaturas Coccion'!B6-B11` (blue 46-49 … well 70+) con «la temperatura sube 3-5 °C en reposo» (`B25`) | La landing no promete alérgenos; el corpus no los trata: se deja o se añade 1 tarea | Caza oct-feb y calçotada: sólo 1 mención de «caza» en todo el kit frente a la promesa del BONUS | `03` → **Registro de Mermas** (`03:'Control Maduracion Carne'!B25` remite a una «hoja de control» que no existe); `05` → **Comparativa de Proveedores** y **Reporting** (`reporting` y `comparativa`: 0 apariciones) | 202 / 152 / `03!'Temperaturas Coccion'` |
| **marisqueria** | **La cita falsa del anisakis se repite aquí**: `03:'Trazabilidad APPCC'!B22 = 'Anisakis: congelacion previa -20°C/7d para consumo crudo/marinado'` con `F22 = 'Obligatorio RD 1420/2006'` (cita del DEFECTO tal como está LIVE; **ese RD está derogado desde el 22-dic-2022**, ver la decisión ANISAKIS-2026-08-29). Cita correcta de `UE 1379/2013` en `F6` | Expositor con tres cadencias: `01!B12` (0-4 °C), `03!B21` («en hielo max 4 °C, rotación cada 2 h»), `04!B13` («hielo cada 90 min, 0-4 °C») | Promete «alérgenos de crustáceos y moluscos»; 3 menciones genéricas en el corpus | Vedas y temporadas SÍ presentes (percebe 8, ostra 10, veda 8) | **Registro de Mermas** (`06:'Perfiles'!B9` remite a un «libro de produccion» inexistente); hoja de **arqueo/caja** o corregir el copy (§5 duda 4) | 122 / 95 / — |
| **panaderia** | 1 sola mención APPCC (`07!B16`). Sin citas normativas | Temperaturas de obrador/masa/horno coherentes entre sí | 4 menciones de alérgenos | — | **Registro de Mermas** (2 menciones sin destino) | 101 / 77 / `03!'Hornos y Coccion'`, `BONUS-01!'Briefing Produccion'` |
| **food-truck** | `04!B6` cita el RGSEAA correctamente. `03:'APPCC Movil'!B8` fija `≥74 °C aves / ≥63 °C otros`, que choca con el `>75 °C` de chef-privado y el `≥63 °C` de marisquería: unificar criterio de familia | `03!B9` («caliente >65 °C o servido <2 h») OK | 8 menciones | — | **Registro de Mermas** (1 mención) | 93 / 74 / `02!'Operaciones Moviles'`, `03!'APPCC Movil'` |
| **tapas-bar** | 1 mención APPCC (`07!B19`). Sin citas | `03!B18` («mantenimiento >65 °C») y `01!B13` (`0-4` / `−18`) coherentes | 12 menciones (el mejor de los cuatro planos) | Calendario `BONUS-02` mes a mes, correcto y rico | **Registro de Mermas** (3 menciones) | 94 / 74 / — |
| **chef-privado** | `04:'APPCC Móvil'!B10` pide `>75 °C` interno; `B11`/`B12` gestionan bien la zona de peligro 5-65 °C. Sin citas de norma: añadir la referencia de los 14 alérgenos al `01`, que ya los promete | Coherentes | **25 menciones**, con «14 alérgenos UE» prometido y cumplido | Calendario de demanda, correcto | **Ninguna.** Todo lo que la landing promete está en los ficheros (`303`, `130`, `390`, margen, reseñas, meal prep, recurrencia: todos presentes) | **0** — es el único bien escrito |

### 2.2 Correcciones de FAMILIA (van en el motor o en los 7 módulos a la vez)

- **«Cierres por vacaciones»**: prometido en el `BONUS-02` de **los 7** y ausente en **los 7**
  (0 apariciones de «vacacion»). Se añade una fila «Cierre por vacaciones / plantilla reducida» y
  otra «Planificar vacaciones del equipo», o se borra de las landings. **COM-09.**
- **«Reporting» y «comparativa de proveedores»**: prometidos en la tarjeta del manager de
  sushi-bar, asador y marisquería; 0 apariciones en los tres. **DOM-28 / COM-24 / TEC-20.**
- **«Arqueo»**: prometido en el `01` de asador, marisquería, panadería y food-truck («cierre
  completo y arqueo»); 0 apariciones en los cuatro (tapas-bar sí lo tiene, 2). **§5 duda 4.**
- **Hoja de mermas**: citada sin destino en 5 de los 7 kits. Es además el argumento que sostiene
  el «€14 frente a €40/mes».
- **«Renovar registro sanitario»** en enero: revisar si la fila está replicada en los `BONUS-02`
  de los otros kits (en sushi-bar es `BONUS-02:'Calendario Anual'!A33`). **COM-21.**

---

## 3. Integración (capa de producto)

Ficheros: `astro-site/src/data/productos/tareas/kit-tareas-<pid>.ts` (7),
`src/components/kit-tareas-<pid>/` (7), `src/pages/KitTareas<Pid>.tsx` +
`…AccessGate.tsx` + `…Dashboard.tsx` (21), `src/data/productos-changelog.ts`,
`src/data/productos-digitales-config.ts`, `netlify/functions/{verify-purchase,resend-access,
admin-generate-access,get-download-urls}.ts`, y `src/pages/MegaPackTareas*.tsx`.
**Ningún nombre de fichero de descarga cambia** — las claves de `get-download-urls.ts` son
intocables.

1. **Recuento de tareas** (fuente = `gates.recuento_tareas.total`, T-03):
   sushi-bar **204** · asador **223** · chef-privado **224** · marisquería **190** ·
   tapas-bar **172** · panadería **160** · food-truck **153** (los cuatro últimos, contados a
   mano hasta que CB-E5 les dé contador). Ninguna landing publica hoy una cifra de tareas: al
   ponerla, sale de aquí.
2. **Anisakis**: sustituir «-20 ºC durante 7 días … RD 1420/2006» —cita del DEFECTO; ese RD está
   derogado, ver la decisión ANISAKIS-2026-08-29— por «−20 °C en la totalidad del producto durante
   al menos 24 h, o −35 °C durante al menos 15 h (RD 1021/2022, art. 8.1, que derogó el
   RD 1420/2006, y Rgto. (CE) 853/2004, Anexo III, Secc. VIII, Cap. III.D)» en las **8 apariciones** de
   `kit-tareas-sushi-bar.ts` (líneas 41, 52, 97, 126, 186, 253, 284, 307 — incluido el testimonio
   y la FAQ del schema) y en la tarjeta `anisakis-appcc` de `KitTareasSushiBarDashboard.tsx:18`.
   Revisar en paralelo `kit-tareas-marisqueria.ts` («Trazabilidad y APPCC Marisco»).
3. **Promesas contra contenido** (COM-05/06/07/08/09/20/24/25 y sus gemelos en los otros kits):
   `delivery`, `salmón salvaje`, `festivos asiáticos`/`Año Nuevo Chino`, `cierres por vacaciones`,
   `reporting`, `comparativa de proveedores`, `rotación FIFO por lotes`, `maki`, `wet-age`,
   `densidad` (vivero). Se corrige el fichero **o** el copy, nunca se deja la promesa suelta.
   `«11 checklists pre-rellenados»` → en sushi-bar son 8 pre-rellenados + 3 en blanco (03, 09,
   BONUS-01): redacción honesta.
4. **`why.reasons[3]`** de los 7: «Software de Gestión Cobra €40/mes» — cifra atribuida a un
   competidor genérico sin fuente, más «ilimitado en clientes» y «las mismas listas de tareas que
   usan sushi bars con software premium». Reescribir sin cifra ajena (mismo criterio que COM-18 de
   la familia). **COM-20.**
5. **`why.subtitle`** de sushi-bar (línea 176) está mal construido gramaticalmente. **COM-25.**
6. **Changelog v2.0** en lenguaje de cliente, por molde:
   - ▸ (sushi-bar, asador): contador que descuenta las N/A, 5 filas libres reales, hojas nuevas,
     ortografía, cita legal del anisakis corregida, hojas protegidas.
   - PLANO: «ahora cada plantilla lleva contador, desplegable en las 11 (antes faltaba en la del
     manager), filas libres, hoja de instrucciones y ortografía revisada».
   - P4 (chef-privado): «el contador ya no cuenta las cabeceras de sección: donde ponía *5 de 41*
     ahora pone *0 de 36*». Es un cambio que el cliente puede comprobar en 5 segundos.
   ⚠️ El v1.1 de asador y sushi-bar dice «Número de versión actualizado a 1.1 en la hoja de
   instrucciones de cada fichero», y el de los cuatro planos **no** lo dice (correcto: no tienen
   esa hoja). Mantener esa honestidad por molde en el v2.0.
7. **Emails y dashboards**: `verify-purchase.ts` / `resend-access.ts` /
   `productos-digitales-config.ts` describen «9 Checklists + 2 Bonus» (11) y «9 plantillas» en
   chef-privado. No cambia el número de ficheros, así que sólo se revisa el texto si se toca la
   descripción de algún entregable.
8. **Mega-pack**: `MegaPackTareas.tsx:32` declara `{ name: 'Chef Privado / Personal Chef',
   templates: 9 }`. Sigue valiendo. El gate LIVE final incluye `mega-pack-tareas`.

---

## 4. Descartes (con motivo)

- **`aggregateRating`, `reviews`, testimonios y ancla de precio: NO se tocan.** Decisión de John,
  heredada de la familia (§7 de `kit-tareas-v2-SPEC.md`, COM-02/COM-03). Va al §6 con el riesgo
  escrito. Cubre COM-02 y COM-04 de esta R1.
- **La marca «ChefBusiness Consultoria Gastronomica» NO se rebrandea** (John, 2026-08-22,
  `feedback_marca-chefbusiness-en-productos-aicp-es-deliberada`). **Sí se acentúa** →
  «ChefBusiness Consultoría Gastronómica», 11-13 celdas por kit en seis de los siete.
- **No se renombra ningún fichero ni se borra ninguna hoja.** Lo prometido y no entregado se
  construye como hoja NUEVA dentro de un libro existente (firma §7-bis.1).
- **No se regenera nada desde cero.** Post-proceso idempotente, como toda la familia.
- **No se rehace el molde PLANO al molde ▸ columna a columna.** Cambiar `Area|Tarea|Responsable|
  Hora|OK|Observaciones` por `Nº|Tarea|Zona|Responsable|Hora Límite|✓ Completada|Firma` movería
  todas las referencias, las bandas y el `print_title_rows` de 44 ficheros para ganar homogeneidad
  que el cliente no ve (nunca compra dos kits). Se le aplica el **mínimo funcional** de CB-E5.
- **`03:'Temperaturas Diario'` no se convierte a formato registro-por-filas** en esta versión
  (DOM-13/TEC-09): se desdobla cada día en `Apertura`/`Cierre`, que es un cambio de 7 columnas y
  no de toda la hoja. El rediseño completo, si se quiere, va a una v2.1.
- **`hora_apertura` = 07:00** que deduce `contexto()` es incorrecta para un sushi bar (abre a las
  10:00) pero **no se corrige**: sólo la consume `precargar_caja`, que en esta sub-familia no
  corre. Documentado para que no se reutilice a ciegas.

---

## 5. Dudas para el orquestador

1. **¿Se crean hojas `Instrucciones` en los 4 kits del molde PLANO?** Son 44 hojas nuevas. La
   regla (j) del motor dice explícitamente «no se inventa ninguna; lo decide el orquestador». A
   favor: es donde viven la bio, la versión, el «Se conecta con» y la explicación del contador —
   sin ella, esos cuatro kits no pueden ser «v2.0» en el mismo sentido que los otros tres. En
   contra: 44 hojas de contenido nuevo es la mitad del coste de la tanda.
2. **¿Molde PLANO al mínimo (CB-E5 sin instrucciones) o completo?** Ligado a la 1. Mi
   recomendación: **completo**, porque el `05-tareas-manager.xlsx` de los cuatro se entrega hoy
   sin desplegable y el `09-plantilla-personalizable.xlsx` de los cuatro está **literalmente
   vacío** (cabecera, una banda `TUS TAREAS PERSONALIZADAS` y nada más: 0 filas). Eso último es lo
   más difícil de defender de toda la sub-familia.
3. **chef-privado lleva marca AI Chef Pro, no ChefBusiness.** Los otros seis llevan la razón
   social de CB en `A1` y en el pie. ¿Es una excepción deliberada o un olvido del porte? Afecta al
   alcance de CB-E1 (si se unifica, hay que decidir hacia cuál) y es decisión de John.
4. **«Arqueo» prometido y ausente en 4 kits.** ¿Se construye una hoja de caja (portando el bloque
   `ajustar_09`/`_fondo_de_caja` de la familia, que ya existe y está probado) o se recorta el copy
   de las 4 landings? Construirla sería el mayor salto de valor de la tanda; también el mayor
   coste, y convertiría a estos kits en algo que hoy no son.
5. **Criterio único de temperatura interna de cocción**: `≥63 °C` (marisquería), `≥74 °C aves /
   ≥63 °C otros` (food-truck), `>75 °C` (chef-privado). ¿Se unifica a un criterio de familia o
   cada kit conserva el suyo con la fuente citada?
6. **pH del arroz (DOM-04/DOM-21/DOM-22).** Tres salidas: (a) pHmetro de punción calibrado
   —correcto, pero obliga al cliente a comprar un aparato—; (b) tiras de rango 4,0-5,0 con
   resolución 0,2, que existen y son baratas; (c) sustituir el PCC por «acidificación medida»
   (ratio de sushi-zu por kg de arroz cocido, registrado). Yo firmaría (b) + (c) juntas y dejaría
   el pHmetro como recomendación.
7. **Frecuencias contradictorias entre `07` y `BONUS-02` (COM-10).** Calibración de termómetros y
   revisión de frío: ¿trimestral (4 marcas en el calendario, fuera del mensual) o mensual? Y
   extintores: trimestral del titular + anual de empresa autorizada son **dos filas**, no una.
8. **¿Entran los otros 6 kits en `mega-pack-tareas`?** Hoy sólo está chef-privado. Sumarlos
   subiría el pack de 13 a 19 kits y de 155 a 221 entradas (66 nuevas), y obligaría a recalcular
   `totalIndividual` y el badge «Ahorra más del 45 %». Es decisión de producto, no de contenido.
9. **`gates.limite_unico` ¿aborta o avisa?** En sushi-bar hay al menos dos equipos con dos rangos
   (`cámara de pescado crudo`: `−2 a 0` vs `0-2`; `congelación anisakis`: `−20` vs `−18`) y en
   marisquería el expositor tiene tres redacciones. Si aborta, la tanda no cierra hasta resolverlos
   todos; si avisa, se arrastran.

---

## 6. Para John (no lo toco; queda el riesgo escrito)

> El brief pide este bloque como «§5 para John»; lo numero **§6** para no duplicar el §5.

1. **`aggregateRating` 4,9 sobre 8 reseñas en los SIETE productos, idéntico**, sin sistema de
   reseñas detrás y con 8 testimonios nominales con avatares de stock compartidos con el resto del
   catálogo. Riesgo doble: política de datos estructurados de Google (reseñas fabricadas) y
   RDL 24/2021 (transposición de la Directiva Ómnibus), que prohíbe presentar como opiniones de
   consumidores reales lo que no se ha verificado. El mecanismo para retirarlo **ya existe**:
   `KitTareasLandingPage.astro` emite `aggregateRating` y `review` sólo si el fichero de datos los
   define (opcionales desde 2026-08-21).
2. **Ancla de precio permanente en los siete**, con `heroNote` «Precio especial de lanzamiento.
   Sube pronto» y `priceValidUntil: '2026-12-31'`:

   | Kit | Precio | Tachado | Badge |
   |---|---|---|---|
   | sushi-bar · asador · marisqueria | €14 | €69 | −80 % |
   | tapas-bar | €14 | €49 | −71 % |
   | panaderia · food-truck | €12 | €39 | −69 % |
   | chef-privado | €18 | €85 | −79 % |

   El de sushi-bar lleva sin variar desde el `45e065a` del 2026-05-05 (casi 4 meses). Art. 20.3
   del RDL 1/2007: el precio anterior anunciado debe ser el más bajo aplicado en los 30 días
   previos.
3. **Marca**: seis kits llevan «ChefBusiness Consultoria Gastronomica» (deliberado, confirmado el
   2026-08-22) y **chef-privado no la lleva**: va con marca AI Chef Pro. ¿Excepción o descuido?
4. **Precio vs. contenido**: marisquería y tapas-bar cuestan lo mismo que sushi-bar (€14) y
   entregan la mitad de máquina: 0 fórmulas, sin hoja de instrucciones, sin contador. Panadería y
   food-truck, con la misma estructura, van a €12. No propongo cambiar precios; lo señalo porque
   la v2.0 iguala la máquina y puede que quieras revisarlo después.
5. **Mega-pack**: 6 de estos 7 kits están fuera del pack de 13. Si fue deliberado, perfecto; si no,
   son 66 entradas y 6 tarjetas de añadir.

---

## 7-bis. Decisiones firmadas

Las ocho del orquestador, tal cual, más las mías argumentadas.

1. **Mismos ficheros y mismos nombres.** Lo prometido y no entregado se construye como HOJA dentro
   de un libro existente («Control de mermas» en el `01` o el `05`; perfil «Delivery» como hoja del
   `06`), salvo que la landing prometa un fichero con nombre propio — no lo hace en ninguno de los 7.
2. **Se reutiliza el motor de familia `kit-tareas-v2_0`** (extendido con CB-E1…CB-E9, con detección
   de molde y abort si no lo reconoce) + `contenido_<pid>.py` por kit. Representante sushi-bar con
   3 refutadores + corrector + ronda 2 + crítico; hermanos por `sonnet` verificando cada id;
   ejecución real en serie con canario.
3. **Barrido de tildes y ñ en TODAS las celdas de texto de los 7 kits y en los nombres de pestaña**,
   por diccionario + revisión por contexto, con gate de «palabras sin tilde conocidas» = 0, sin
   tocar fórmulas, rutas ni códigos.
4. **Normativa citada correctamente y con fuente en celda de nota**: anisakis
   (−20 °C ≥ 24 h o −35 °C ≥ 15 h, con la excepción del Rgto. 1276/2011), un solo límite crítico
   por PCC, pH del arroz con método verificable, temporadas de pescado por fuente (MAPA / campañas
   de costera) y coherentes con la landing.
5. **Alérgenos**: los 14 del Rgto. 1169/2011 en la tarea de alérgenos, con los propios del negocio
   destacados (pescado, crustáceos, moluscos, soja, sésamo, gluten, huevo, sulfitos, frutos secos…).
6. **`aggregateRating`, testimonios y ancla de precio: NO se tocan** (John). §6 con el riesgo.
7. **Capa de producto honesta con lo que hay**: promesas del grid, FAQ y emails contrastadas contra
   las hojas reales. Changelog v2.0 en lenguaje de cliente.
8. **Térmica y seguridad**: dry-run a scratchpad, APPLY con variable de entorno y respaldo, un
   python cada vez.

**Mías, argumentadas:**

9. **El MOLDE manda sobre el nombre del fichero, y son tres.** Ningún paso puede asumir que
   `09-plantilla-personalizable.xlsx` es el «07» de la familia ni que `08-eventos-estacionales.xlsx`
   es el «08 de negocio»: la numeración de esta sub-familia está desplazada respecto a la del
   representante. Todo se decide por cabecera (regla de oro del motor) y **CB-E6 aborta** si un
   fichero no cae en ningún molde. Motivo: hoy `tapas-bar` sale con `censo --fail` en verde
   habiendo tocado exactamente nada.
10. **La cita falsa del anisakis se corrige en DOS kits, no en uno.** `marisqueria/03-trazabilidad
    -appcc-marisco.xlsx:'Trazabilidad APPCC'!B22` repite «−20 °C/7 d» con `F22 = 'Obligatorio
    RD 1420/2006'` (cita del DEFECTO; RD derogado, ver la decisión ANISAKIS-2026-08-29).
    Tratarlo como hallazgo exclusivo del representante habría dejado vivo el
    segundo. **Los refutadores del representante NO ven los hermanos: el censo transversal se
    corre antes de la tanda 1, no después.**
11. **El barrido de ortografía va DESPUÉS del motor, como paso propio.** Demostrado: tras el
    dry-run, `01:Instrucciones!B4` sigue diciendo «Como usar estas plantillas» porque `instrucciones()`
    reescribe el bloque con el texto que lee del propio fichero. Si CB-E1 corriese antes, el motor
    lo desharía.
12. **chef-privado va PRIMERO, no último.** Es el más barato (el motor P4 ya lo arregla: 22
    fórmulas y la DV unificada sin escribir una línea nueva), es el único de los 7 dentro del
    mega-pack, y valida la vía P4 y el flujo de APPLY con el riesgo más bajo. Un canario de verdad.
13. **La plantilla personalizable: o se le crea el contador, o se le callan las Instrucciones.**
    La combinación actual del dry-run —instrucciones que prometen contador y filas libres sobre una
    hoja que no tiene ninguna de las dos cosas— es peor que el defecto original.
14. **Las hojas nuevas se añaden AL FINAL del libro** (`wb.create_sheet()` sin índice), nunca
    intercaladas: mover una pestaña reordena `print_title_rows`, `print_area` y las referencias
    cacheadas, y rompería la idempotencia del motor en la 2.ª pasada.
15. **El gate LIVE de cierre incluye `mega-pack-tareas`**, porque comparte los 9 ficheros físicos de
    chef-privado. Cerrar sin él dejaría el pack de €89 apuntando a ficheros que han cambiado sin
    que nadie lo haya comprobado.

---

16. **Molde PLANO (dudas 1 y 2): COMPLETO, con hoja «Instrucciones» nueva en los 44 ficheros.** No es inventar contenido: es el estándar de la
    familia (lo que el motor ya genera para ▸), y esos 4 kits se venden con la misma landing que promete instrucciones, contador y plantilla personalizable.
    El 09 vacío se construye con el molde de la familia (contador + filas libres) y el 05 recibe desplegable aunque su columna se llame «Estado».
17. **Marca (duda 3): chef-privado se queda con «AI Chef Pro» y los otros seis con «ChefBusiness Consultoría Gastronómica» (acentuada).** La marca CB en
    esos productos es decisión de John (2026-08-22); la excepción de chef-privado se le señala en «para John», no se toca.
18. **Arqueo (duda 4): se PORTA el bloque de caja de la familia** (como hoja dentro del libro donde la familia ▸ lo lleva), no se recorta el copy de las
    4 landings. Lo prometido se entrega.
19. **Temperaturas (duda 5): criterio ÚNICO de familia, con fuente en celda de nota**: cocción ≥ 70 °C en el centro del alimento (≥ 75 °C en aves,
    picados y recalentados) según las recomendaciones de AESAN; mantenimiento en caliente ≥ 65 °C y en frío ≤ 8 °C / ≤ 4 °C según RD 3484/2000
    (comidas preparadas) ⚠️ **el RD 3484/2000 también está derogado, por el mismo RD 1021/2022, que ya NO fija temperaturas: las fija y justifica el operador en su APPCC**; marisco y pescado crudo con su régimen específico (anisakis: −20 °C ≥ 24 h en la totalidad del producto o −35 °C ≥ 15 h, RD 1021/2022, art. 8.1, que derogó el RD 1420/2006, y Rgto. (CE) 853/2004, Anexo III, Secc. VIII, Cap. III.D — ver la decisión ANISAKIS-2026-08-29).
    Un solo valor por PCC; el constructor cita la norma en la celda y NO teclea ninguna cifra sin fuente.
20. **pH del arroz (duda 6): tiras de rango 4,0-5,0 con resolución 0,2 Y registro de acidificación medida** (vinagre dosificado por kg de arroz),
    las dos a la vez; el pHmetro se menciona como opción, no como obligación.
21. **Frecuencias (duda 7): una sola tabla de familia** que alimenta 07 y BONUS-02: calibración de termómetros mensual; revisión de frío mensual por el
    titular + anual por empresa; extintores en DOS filas (revisión trimestral del titular + retimbrado/revisión anual por empresa autorizada, RD 513/2017).
    Donde 07 y BONUS-02 discrepen gana la más frecuente y se documenta.
22. **Mega-pack (duda 8): NO se amplía en esta v2.0** — cambia precio, badge de ahorro y promesa; es decisión de John. Se le deja descrito.
23. **`gates.limite_unico` (duda 9): ABORTA.** Un PCC con dos límites es exactamente el defecto que se viene a arreglar; el módulo de contenido del kit
    unifica antes de que el motor escriba.
24. **Regresión sobre la familia ▸ (añadida por el orquestador): cualquier extensión del motor (CB-E1..E9) se prueba en dry-run sobre DOS kits ▸ ya
    en producción (kit-tareas-cafeteria y kit-tareas-hotel) y el resultado debe ser IDÉNTICO celda a celda a lo que hoy sirve `dl/`** (0 diferencias):
    el motor es el mismo que sostiene 11 kits LIVE. Gate bloqueante de T1.

## 8. Mapa id → sección (76/76)

`M` = motor (§1) · `C` = contenido (§2) · `P` = producto (§3) · `J` = John (§6) · `D` = descarte (§4).

### DOM (31)

| id | Sección | Destino |
|---|---|---|
| DOM-01 | §2.0 + §2.1 + §3.2 | C + P — anisakis mal citado |
| DOM-02 | §2.0 + §2.1 | C — `−20` vs `−18`, límite único |
| DOM-03 | §2.1 | C — cadena horaria del arroz |
| DOM-04 | §2.1 + §5.6 | C — pH verificable + hoja de registro |
| DOM-05 | §1.2 CB-E1 | M — tildes y ñ |
| DOM-06 | §2.1 | C — hoja «Delivery y Take Away» en `06` |
| DOM-07 | §2.0 + §2.1 | C — 14 alérgenos + matriz en `03` |
| DOM-08 | §2.1 + §2.2 | C — hoja «Registro de Mermas» |
| DOM-09 | §2.1 | C — bonito/atún cruzados |
| DOM-10 | §2.1 | C — regla de las 2 h |
| DOM-11 | §2.1 | C — turno almuerzo/cena y 2.º lote |
| DOM-12 | §2.1 + gate `limite_unico` | C + M |
| DOM-13 | §2.1 (+ §4) | C — desdoble apertura/cierre |
| DOM-14 | §2.1 | C — lote, etiquetado, descongelación |
| DOM-15 | §2.0 | C — excepción acuicultura 1276/2011 |
| DOM-16 | §1.2 CB-E2 | M — crear contador en `09` |
| DOM-17 | §1.1 (§2.2 familia) | M — ya resuelto, verificado |
| DOM-18 | §2.1 | C — sardina, lubina, prevalencia anisakis |
| DOM-19 | §2.0 + §2.2 | C — cenas de empresa, RGSEAA, DDD/extintores |
| DOM-20 | §2.2 + §3.3 | C + P — salmón salvaje, festivos, vacaciones |
| DOM-21 | §2.1 | C — acción correctiva escalada del pH |
| DOM-22 | §2.1 | C — base de cálculo del sushi-zu |
| DOM-23 | §2.1 | C — filas inútiles del registro de temperaturas |
| DOM-24 | §2.1 | C — hora de pedido a lonja |
| DOM-25 | §2.1 | C — vitrina encendida toda la noche |
| DOM-26 | §2.1 | C — hangiri y plan de L+D |
| DOM-27 | §2.1 | C — hoja «Control de Recepción» |
| DOM-28 | §2.1 + §2.2 + §3.3 | C + P — comparativa y reporting |
| DOM-29 | §2.1 | C — makisu, film, hamachi/seriola |
| DOM-30 | §2.1 | C — inari/aburaage |
| DOM-31 | §2.1 | C — cocina caliente + hoja «Office y Lavado» |

### TEC (20)

| id | Sección | Destino |
|---|---|---|
| TEC-01 | §1.2 CB-E1 | M — ñ en encabezados y en nombre de pestaña |
| TEC-02 | §1.2 CB-E1 | M — tildes sistemáticas (incluye la razón social) |
| TEC-03 | §1.2 CB-E2 | M — contador ausente en `09` |
| TEC-04 | §1.1 | M — filas libres (verificado en dry-run) |
| TEC-05 | §1.1 | M — denominador descuenta N/A (verificado) |
| TEC-06 | §1.1 | M — `showErrorMessage` + `DV_ERROR` (verificado) |
| TEC-07 | §1.2 CB-E3 | M — fórmulas y DV en los registros APPCC |
| TEC-08 | §1.2 CB-E3 | M — CF de fuera de rango en temperaturas |
| TEC-09 | §2.1 | C — dos lecturas / una celda |
| TEC-10 | §1.2 CB-E4 | M — «Cómo personalizar» por tipo |
| TEC-11 | §2.0 + §2.1 | C — `−20` vs `−18` en el mismo fichero |
| TEC-12 | §2.1 + §3.3 | C + P — alérgenos ausentes en `03` |
| TEC-13 | §1.2 CB-E4 + §2.1 | M + C — marcar ✓ en el calendario |
| TEC-14 | §1.1 | M — verde en `Tarea` y `Hora` (ya lo hace) |
| TEC-15 | §1.2 CB-E9 | M — ancho/wrap de la columna `Tarea` |
| TEC-16 | §1.2 CB-E9 | M — ancho de `B` en `Temperaturas Diario` |
| TEC-17 | §1.2 CB-E9 | M — wrap en las hojas `Instrucciones` |
| TEC-18 | §1.2 CB-E9 | M — paleta del CF vs verde base |
| TEC-19 | §1.2 CB-E3 + CB-E9 | M — alto de fila con `wrap_text` |
| TEC-20 | §2.1 + §3.3 | C + P — FIFO por lotes, reporting, maki |

### COM (25)

| id | Sección | Destino |
|---|---|---|
| COM-01 | §2.0 + §3.2 | C + P — anisakis en las 8 líneas de la landing |
| COM-02 | §4 + §6.1 | **J** — `aggregateRating` y reseñas |
| COM-03 | §2.1 | C — temporadas cruzadas en `08` y `BONUS-02` |
| COM-04 | §4 + §6.2 | **J** — ancla de precio |
| COM-05 | §3.3 | P — «11 pre-rellenados» → 8 + 3 en blanco |
| COM-06 | §2.1 + §3.3 | C + P — perfil delivery |
| COM-07 | §3.3 | P — salmón salvaje |
| COM-08 | §2.2 + §3.3 | C + P — festivos asiáticos / Año Nuevo Chino |
| COM-09 | §2.2 + §3.3 | C + P — cierres por vacaciones (los 7) |
| COM-10 | §2.1 + §5.7 | C — frecuencias `07` vs `BONUS-02` |
| COM-11 | §1.2 CB-E2 | M — contador de la plantilla |
| COM-12 | §1.1 | M — filas libres (verificado) |
| COM-13 | §1.1 | M — denominador honesto (verificado) |
| COM-14 | §1.2 CB-E1 | M — tildes y ñ |
| COM-15 | §2.1 + gate `limite_unico` | C + M — cámara con dos rangos |
| COM-16 | §2.0 + §2.1 | C — umbral de reinicio del conteo |
| COM-17 | §2.1 | C — `05` anuncia 3 checklists y trae 2 |
| COM-18 | §2.1 | C — horas del arroz `02` vs `01` |
| COM-19 | §1.2 CB-E4 | M — «celdas verdes» en `BONUS-01` |
| COM-20 | §3.4 | P — «€40/mes» y «ilimitado en clientes» |
| COM-21 | §2.0 + §2.2 | C — RGSEAA no se renueva |
| COM-22 | §1.1 + §2.1 | M + C — pedido y cuadre duplicados `05`/`01` |
| COM-23 | §1.1 | M — cabecera `Hora Límite` → `Día`/`Cadencia`/`Antelación` |
| COM-24 | §2.1 + §3.3 | C + P — comparativa y reporting del manager |
| COM-25 | §3.5 | P — `why.subtitle` mal construido |

**Cobertura: 31 + 20 + 25 = 76/76.** Al motor 20 · al contenido 39 · al producto 15 (con solape
C+P en 11 ids) · a John 2 (COM-02, COM-04).

---

## 9. Plan de ejecución

Método de la familia (5 tandas, canario, diff firmado, `agent()` con `model` explícito y **schema
siempre** — `feedback_workflow-agentes-sin-schema-devuelven-string`). Todo en serie; `istats`
antes de cada `python3`; dry-run a scratchpad propio; `KIT_TAREAS_APPLY=1` sólo cuando el
orquestador firma el diff.

### T0 — Censo transversal y extensiones «baratas» del motor · `sonnet` + `opus`

1. `sonnet`: censo de las 5 correcciones de FAMILIA (§2.2) sobre los 7 kits, con `fichero!hoja!celda`.
   Es lo que ha cazado la segunda cita falsa del anisakis (firma §7-bis.10). Salida: JSON con schema.
2. `opus`: **CB-E6, CB-E7, CB-E8** en `motor.py` (abort por molde, kit sin caja, autorreferencia de
   áreas). Son ~60 líneas y hacen que los informes de dry-run dejen de mentir.
3. **Verificación**: `--dry-run --solo motor` sobre sushi-bar → `01:Instrucciones!B35` ya no se
   autocita, `gates.negocio_precargado` informativo, `exit 0`. Sobre tapas-bar → **aborta**.

### T1 — chef-privado (canario real) · `sonnet` + orquestador

El motor ya lo arregla. Se corre el dry-run, se firma el diff (22 fórmulas + 11 DV + bio + versión
+ metadata), se aplica de verdad con respaldo, y se verifica el contador cacheado en las 11 hojas
(`«5 de 41»` → `«0 de 36»`). Valida el flujo de APPLY con el kit de menor riesgo y **de paso deja
el mega-pack correcto**. Producto: changelog v2.0 + revisión del copy (no hay promesas rotas).

### T2 — Representante sushi-bar · `opus` (motor y refutadores) + orquestador

1. `opus`: **CB-E1 (ortografía), CB-E2 (contador ausente), CB-E3 (registros), CB-E4 (instrucciones
   por tipo), CB-E9 (legibilidad)** en `motor.py`.
2. `opus`: `contenido_kit_tareas_sushi_bar.py` con las 39 correcciones de contenido y las 8 hojas
   nuevas de §2.1.
3. **3 refutadores en paralelo** (`opus`, schema obligatorio): DOMINIO (itamae), TÉCNICA EXCEL
   (pycel + openpyxl), COHERENCIA COMERCIAL. Cada hallazgo con `fichero!hoja!celda`.
4. Corrector (`opus`) → **ronda 2** de refutación (`sonnet`, verificando id por id) → **crítico**
   (`opus`) sobre el diff.
5. Firmas del orquestador sobre el `diff-firmado.json` (valor + DV + alturas + `locked`, desglosado
   como en m3).
6. Demostraciones exigibles: contador con 3 N/A → «22 de 22»; `09` con 8 tareas escritas → «x de 8»;
   `gates.ortografia` = 0; `gates.limite_unico` = 0; `gates.promesas` = 0 términos ausentes;
   DV `"✓,—,N/A"` en 16/16 hojas; bio en 11/11; idempotencia (2.ª pasada, diff vacío).

### T3 — asador (hermano ▸) · `sonnet` + motor

`main.py --producto kit-tareas-asador` con el motor extendido + `contenido_kit_tareas_asador.py`
(mucho más corto: sin problema legal propio, con mermas y reporting). Un `sonnet` verifica **cada
id MOTOR de la R1** contra el fichero regenerado y revisa los ids de CONTENIDO equivalentes.

### T4 — molde PLANO (4 kits) · `opus` (CB-E5) + `sonnet` (hermanos)

1. `opus`: **CB-E5** en `motor.py`, con la decisión del §5.1-5.2 ya firmada.
2. **Canario: tapas-bar** (el mejor escrito de los cuatro: 12 menciones de alérgenos, calendario
   rico). Diff firmado antes de tocar los otros tres.
3. `sonnet` ×3 en serie: marisquería (con la corrección legal del anisakis, que es lo único
   grave de los cuatro), panadería, food-truck.

### T5 — Capa de producto y cierre · `sonnet` + orquestador

7 landings + 21 ficheros SPA + changelog + config + `MegaPackTareas*`. Contraste promesa↔hoja con
`gates.promesas`. Recuentos de tareas desde `gates.recuento_tareas`. Después:
`gate-flujo-postpago.py` (los 7 + `mega-pack-tareas`), `censo-entregables.py --fail`,
y el **gate LIVE** de cierre con el baseline vigente (44 productos).

### Reparto de modelos

| Trabajo | Modelo |
|---|---|
| Censos, greps, verificación id por id, hermanos, ediciones mecánicas | `sonnet` |
| Extensiones del motor, módulos de contenido, refutadores adversariales, crítico | `opus` |
| Firmas de diff, decisiones de molde y de normativa, APPLY sobre `dl/`, gate LIVE | orquestador (Fable) |

### Orden real

`T0 → T1 (chef-privado) → T2 (sushi-bar) → T3 (asador) → T4 (tapas-bar canario → marisquería →
panadería → food-truck) → T5`.

Se para y se pregunta si: (a) `MoldeDesconocido` salta en un kit que no sea del molde PLANO;
(b) el diff del representante no cuadra con el recuento independiente del verificador; (c)
`gates.limite_unico` encuentra un conflicto que no esté en la R1; (d) cualquier cambio que toque
`aggregateRating`, `reviews`, `priceOld` o la marca ChefBusiness.

---

## Decisión ANISAKIS-2026-08-29 — el RD 1420/2006 está derogado

Vale para los 11 kits CB y para el representante. Verificado en el BOE
(`auditorias/guias-v2-research-sector.json`, entradas ANIS-01 a ANIS-05):

- El **RD 1420/2006** quedó **DEROGADO el 22-dic-2022** por la disposición derogatoria única.h)
  del **RD 1021/2022** (`BOE-A-2006-22171`, ficha de estado).
- Vigente: **art. 8.1 del RD 1021/2022** (`BOE-A-2022-21681`) — **−20 °C o inferior en la
  totalidad del producto durante ≥ 24 h**, o **−35 °C durante ≥ 15 h**; la congelación puede
  haberla hecho una etapa anterior **si está justificado documentalmente**. El **art. 8.2** obliga
  a informar a la persona consumidora «mediante carteles o cartas-menú».
- Europa: **Rgto. (CE) 853/2004, Anexo III, Secc. VIII, Cap. III.D** (redacción del
  **Rgto. (UE) 1276/2011**).

**Texto canónico**: «RD 1021/2022, art. 8.1 (que derogó el RD 1420/2006) y Rgto. (CE) 853/2004,
Anexo III, Secc. VIII, Cap. III.D».

**Gate**: `kit-tareas-v2_0/motor.py` → `PROHIBIDAS` / `restos_prohibidos()`, enganchado al veredicto
de `main.py`. **Sólo FALLA, nunca reescribe**: este motor sostiene 11 kits LIVE y una sustitución
automática los repintaría todos sin que nadie leyese la frase resultante.

⚠️ **Pendiente, fuera del alcance de la corrección del 2026-08-29**: los dos ficheros LIVE que
todavía llevan la cita derogada — `kit-tareas-sushi-bar/03-seguridad-anisakis-appcc.xlsx:'Registro
Congelacion'!A2` y `kit-tareas-marisqueria/03-trazabilidad-appcc-marisco.xlsx:'Trazabilidad
APPCC'!F22` — **no tienen constructor**: esta SPEC (CB) todavía no se ha ejecutado, así que no hay
`contenido_*.py` que los reescriba. Se corrigen cuando se construya la familia CB.
