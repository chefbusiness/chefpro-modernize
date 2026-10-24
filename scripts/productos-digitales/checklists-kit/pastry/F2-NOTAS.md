# Pastry Shop Checklists Kit Pro — F2: construcción real (24-oct-2026 · sesión Claude Code)

Todo el python se ha ejecutado en el VPS (`/root/wt-chocopastry`, rama `feat/chocolate-pastry-checklists-en`, venv
`/root/venv-guias`). La comprobación de los hermanos se hizo en un worktree aparte y limpio (`/root/tmp-wt-sib`, ya
borrado), porque otro agente estaba parcheando el ES de la chocolatería en el worktree común.

Textos: `textos_en/heredado.json` (63: 32 de la cafetería, 28 del bar, 2 de la heladería y 1 del base) + `G1.json` (457)
+ `G2.json` (363) = las 883 cadenas a traducir. GM 478 por `mapas_pastry.py` (203 `POR_CELDA`, 220 horas).
`heredar.py --kit pastry` al empezar: **0 cambios**.

## Riesgos de la F1, resueltos

- **G3 rojo falso en «Celery (UK)»** (12, «Allergen Matrix» K4 y «Allergen Chart» J5):
  - `aplicar_en.objetivo_ajuste` medía a lo ancho las cabeceras giradas 90° (fila de 95 pt, columna de 5).
  - Ahora toda celda con `textRotation` se mide contra el alto de su fila, o filas si está combinada
    (`PT_UNIDAD = 5,25 pt` por unidad de ancho; 95 pt ≈ 18 unidades).
  - No activa el ajuste ni sube el alto. Solo avisa de desborde si el EN no cabe a lo alto y el ES sí.
  - Efecto en la pastelería: «Tree nuts» ya no recibe un ajuste de texto que no le hacía falta (12: 2 ajustes en vez
    de 4); las 28 cabeceras caben, y la más larga es «Wheat (gluten)», con 15,1 unidades de las 18,1.
  - Prueba ad hoc: K4 = «Celery and celeriac (UK only list)» → G3 «el EN no cabe ni con ajuste».
  - Ningún otro ES del circuito trae celdas giradas: censo de los 10 ES, 0 en los 9 hermanos.
- **`--autotest` no corría**, por dos motivos:
  - la carpeta base no estaba limpia: era el G3 de arriba, ya resuelto;
  - `_bloquear_verde` buscaba una celda verde desbloqueada, y este ES tiene 0 hojas protegidas y 0 desbloqueadas.
    Ahora, si no la encuentra, hace la mutación inversa: desbloquea una verde, o la primera celda real. La caza el mismo
    control de G1 («desbloqueadas distintas»). En los hermanos se sigue eligiendo la misma celda que antes.
- **Cadenas largas (las 42 de la lista de la F1):** no han necesitado `ALTOS_FILA` ni recortes. Se ha comprobado con
  `cortadas.py`, que mira las 3.430 celdas de texto.
  - En este molde base las filas de tarea (01-07 y B01) tienen **alto automático**: la B, de 45 de ancho y con ajuste,
    crece sola. Ejemplos: 06 «Holiday Season» B9 (219 caracteres), 01 «Kitchen Opening» B10 y B21, 02 «Creams &
    Fillings» B12.
  - Las filas de alto fijo (08, 11, 12, 13) las sube `capa_ajuste`: 47 altos subidos.
- **c0746** (09 «Instructions» B17): fuera «unprotect the sheet if it is locked (no password)», porque el 09 EN no va
  protegido. También se ha quitado del ADAPTAR de `mapas_pastry`, para que no vuelva.
- **«sablée» / «brisée»** (c0143, c0145): G2 las rechazaba (tilde) → «sablee» y «brisee».

## Otros cambios de esta pasada

- **Celdas cortadas nuevas** (había 5 después de quitar el falso positivo) → **0**:
  - 13 «Receiving Log» A38:K40, criterios US: es una combinada de 3 filas automáticas, que se quedan en 45 pt. Con los
    huevos a 45 °F y la leche (3-202.11) pide 4 líneas, 54 pt, y `capa_ajuste` no sube combinadas de varias filas →
    `ALTOS_FILA` `('13', 'Recepción de Mercancía', 40): 30.0`.
  - 13 «Temperature Log» A38: «Readings» no cabía en la columna de 6 (G2 c1178) → «Count» (al lado del `=COUNT(B6:M36)`).
  - 09 «Cash Drawer Closing» A46 (`POR_CELDA`, columna de 5): «POS Z report: sales + tax, excl. tips» →
    «POS Z: sales + tax, excl. tips», sin palabras de más de 5 letras.
- **G2: «rosca de Reyes» y «pan de muerto»** (06 «Holiday Season» B6, B29 y B30; B02 E4 y E12) salían como
  «funcional ES «de»». Son los nombres US que pide la SPEC (D14) → `gates_en.FRASES_OK`, como «dulce de leche» en la
  heladería.
- **Etiqueta interna filtrada:** el traductor de G2 copió de la SPEC «[kit criterion]» en 9 cadenas del cliente (c0916,
  c0930, c0945, c1015, c1159, c1160, c1180, c1200, c1248).
  - Ahora dicen «Kit rule», «Kit guideline», «(a kit rule)», «Privacy (kit guideline, not legal advice)» o «Privacy
    notice.»; donde ya ponía «kit quality target, not a legal limit», sin nada más.
  - `gates_en.RX_ID_INTERNO` caza ya «[kit criterion…]». Los hermanos no lo llevan (la heladería escribe «(kit
    criterion, …)», entre paréntesis, que no casa).
- **`censo-entregables.py`**: `pastry-shop-checklist-templates` en `PRODUCTOS_LETTER`, en línea propia.
- `textos_es.json` / `pendientes.json` regenerados (`extraer_textos` + `heredar`): solo cambian el ADAPTAR de c0746 y el
  `en_por_celda` de «Z del TPV». La meta (fecha y commit) se ha dejado como estaba y `censo_es.json` no cambia.

## Código común (commit `831821ba`, aparte)

- `aplicar_en.py`: `PT_UNIDAD` y la rama de texto girado en `objetivo_ajuste`.
- `gates_en.py`:
  - `_bloquear_verde`, con la mutación inversa;
  - `FRASES_OK`, + 4 grafías de rosca y pan de muerto;
  - `RX_ID_INTERNO`, + «kit criterion».
- **Prueba de los 9 hermanos** (base, bar, cafe, catering, pizza, burger, ghost, icecream, chocolate), antes y después
  del cambio:
  - Dry-run con el código nuevo = publicado (volcado, 0 diferencias): base 4.227 líneas, bar 3.352, catering 2.695,
    heladería 2.510 y chocolatería 2.669.
  - Dry-run nuevo frente al dry-run con el código anterior: `aplicar_en.digest`, que mira valores, formato, ajuste,
    altos, DV, CF, protección y papel, da **0 diferencias** en los cinco. La chocolatería se compara contra su estado
    de `28efc8d3` (ronda 1), con el código de ese commit.
  - Salida de `gates_en` y de `--autotest`, antes y después: **idéntica en los 9**. VERDE 8/0 y autotest OK en base
    (16), bar (16), catering (20), heladería (19) y chocolatería (19).
  - **Cafetería, pizzería, hamburguesería y ghost kitchen**: dry-run abortado y gates en ROJO (43 / 40 / 36 / 40) por la
    deuda conocida de `adf52a52` (G4 «valor fijado»). Es idéntico antes y después: no viene de aquí.
  - `censo-entregables --fail` en los 9 slugs EN: 0 defectos cada uno.

## Comandos (en `scripts/productos-digitales/checklists-kit/`)

    python3 heredar.py --kit pastry
    python3 aplicar_en.py --kit pastry --dry-run --idempotencia --mes October --salida <tmp>
    python3 gates_en.py --kit pastry --mes October --dir <tmp> [--autotest]
    python3 aplicar_en.py --kit pastry --idempotencia --mes October     # → astro-site/public/dl/pastry-shop-checklist-templates/
    python3 gates_en.py --kit pastry --mes October [--autotest]
    python3 ../censo-entregables.py --only pastry-shop-checklist-templates --fail
    python3 ../gate-no-latinos.py --only pastry-shop-checklist-templates
    python3 volcar_xlsx.py --kit pastry ../../../astro-site/public/dl/pastry-shop-checklist-templates pastry/revision/dump_en.txt --orden en
    python3 volcar_xlsx.py --kit pastry ../../../astro-site/public/dl/kit-tareas-pasteleria pastry/revision/dump_es.txt --orden es

## Resultados

| Paso | Resultado |
|---|---|
| Montaje | 15 xlsx (nombres de `SPEC.md` §2) · idempotencia 0 diferencias · `inject_cache` sin fallos de pycel (12: 828 fórmulas, 370 con caché; las 458 vacías también lo están en el ES, G6) · 0 desbordes · 0 rellenos · 46 ajustes activados · 47 altos subidos (1 por `ALTOS_FILA`) |
| G1 | 62 hojas · 1.866 fórmulas (15 por celda, 726 con hoja) · 41 DV (1.869 celdas) · 51 CF (7 por celda, D7) · 344 merges · 0 protegidas · 0 desbloqueadas · 6.815 verdes · 52 nombres definidos (4 con apóstrofo) · 9 áreas de impresión · 43 paneles · 429 tareas |
| G2 | sin español, €, no latinos, etiquetas internas ni términos prohibidos (3.783 términos revisados, 3.430 valores) · 945 formatos € reescritos |
| G3 | Letter 62/62 · pie 52 · marca 43 (el 09 sin marca, como su ES) · versión 2.0 en los 15 · 46 ajustes · 49 altos |
| G4 | 1.761 glosario · 276 regenerar · 955 traducir · 6 citas de rótulo · 7 de pestaña · 1 clave · 220 horas · 2 mensajes de DV |
| G5 | 15 denominaciones · 2 `CASOS_G5` (204.91; 200 / 1,250 / 3,000 / 150 / Z 4,200 → 4,200 y 0) · 9 comprobaciones |
| G6 | 1.866 fórmulas: 1.408 con valor, 458 vacías como en el ES · 136 contadores |
| G7 | 171 °F y 43 citas normativas, todas en `REGLAS_US` / `ADAPTAR` (33 permitidas) · 72 celdas ES con °C · `CELSIUS_SIN_F` vacío |
| G8 | censo + no-latinos OK |
| **Gates** | **VERDE 8/0** |
| Autotest | **19/19 CAZADOS**: los 16 del base (la G1 «desbloqueadas», con la mutación inversa), el término prohibido y las 2 de la CF de excepción del 13 (D7) · `VALORES_EN` vacío (el inventario no trae mínimos) |
| censo-entregables · no-latinos | 0 defectos (`--fail`, Letter exigido) · 15 ficheros, 0 con no latinos |
| Celdas cortadas | **0 nuevas** en 3.430 celdas. 50 heredadas: 28 «Verified by:», como en el base; 6 del 09 («Denomination», como en el base, y 5 rótulos del resumen en la columna A de 5, abajo); 14 rótulos de sección de 12 pt en filas de 15,8 pt (10, 11, 13) y 2 títulos (12 «Case Labels», 13 «Prep Labels»), por menos de 1 pt. 32 del ES que la EN deja de cortar |
| Hermanos | arriba («Código común») |
| Copia al Mac | `scp` de los 15 xlsx y los 2 volcados · sha256 17/17 iguales VPS ↔ Mac |
| Volcados | `revision/dump_en.txt` y `dump_es.txt`, 6.498 líneas cada uno |

sha256 (los 15 publicados):

    fd5c58d9a4d638974534030dad6cee28a9e53212fbaaedab8afee388d7b627bd  01-pastry-kitchen-bakery-case-opening-closing-checklists.xlsx
    c40d1318301ff1d6b3976b6be7f15d3149ed10172f6f02057c587722288027d9  02-pastry-kitchen-production-checklists.xlsx
    cae163c737a235d859151ce4a50551342e96e58f3f698567ca45de4e71b24624  03-pastry-shop-manager-checklist.xlsx
    20cf9eda1cf5be11f4ebc7d298ab1a5b047ddcc342742b98afbe7eacefb61b65  04-pastry-chef-duties-by-role.xlsx
    e29e0644eceb3f6df5e9b1e36e0b599e87e50ab6a51388586390f81f546529a0  05-bakery-cleaning-schedule-maintenance-inventory.xlsx
    507530d9758c3a1a8b8ef53b91fff1162b1a79efa88f7656d26eafcc719d2d20  06-pastry-shop-holiday-event-checklists.xlsx
    7c9533de013f33d4af296d00f3287f32a2d21a92a1168d9fc8b1553806b1276e  07-blank-pastry-shop-checklist-template.xlsx
    ca44e539eff921c8305201678fb9ccb1b48266a12549e94a5f91283043044744  08-pastry-shop-opening-closing-checklist.xlsx
    181b4b3729a86276587d7ed7fe532a2bda7aa53a7471a3997666e08dc52a78fc  09-cash-drawer-opening-closing.xlsx
    4e0b2446d6c9c1207618fee08a368879d1b861efd72b765c214028af24a7c134  10-bakery-production-schedule-waste-log.xlsx
    e505d2dfd3f41dd84abef04995fb900cabfe5b391fcdb4892aee5a3a0c52cd10  11-cake-order-form-order-log.xlsx
    bdccc8dacefb7844ce1a03d87d48571b9925c0c5a48d1e276f9fd72224f5c816  12-bakery-allergen-chart.xlsx
    d0c54a4b5f7777bf92decae28537a702da284213019d1e3299a52b08c87ccc42  13-food-temperature-log-receiving-log.xlsx
    d9280886004666586bda8f86d94bed02da1586210fa69b2225f8686f57c07e85  BONUS-01-pastry-shop-pre-shift-meeting-template.xlsx
    824ff6f46320fd2ca2a89826b29bc6c135790c6b1b1b4b59f7c0d771c2cf4616  BONUS-02-pastry-shop-holiday-calendar.xlsx

### Cifras para la landing (F3)

Las tareas son las filas con número en A y texto en B. El ES da las mismas.

| Fichero | Hojas (sin Instructions) | Tareas |
|---|---|---|
| 01 Kitchen & Bakery Case Opening/Closing | Kitchen Opening 22 · Kitchen Closing 20 | 42 |
| 02 Production | Doughs & Fermentation 26 · Creams & Fillings 18 · Decorating & Finishing 13 (con la columna «Target / Spec» en °F) | 57 |
| 03 Manager | Daily 16 · Weekly 18 · Monthly 14 · Shift Handover 6 | 54 |
| 04 Duties by Role | Head Pastry Chef 14 · Pastry Cook 13 · Pastry Assistant 11 · Counter Associate 12 | 50 |
| 05 Cleaning, Maintenance & Inventory | Weekly Deep Clean 18 · Monthly Maintenance 13 · Weekly Inventory 13 | 44 |
| 06 Holiday & Event | Holiday Season 26 · Valentine's Day 11 · Easter 13 · Mother's & Father's Day 9 · Celebration Cakes (Apr-Jun) 17 · Thanksgiving (Nov) 14 | 90 |
| 07 Blank Template | By Time of Day · By Area · By Role (en blanco) | 0 |
| 08 Whole Shop | Shop Opening 20 (6:45-8:00 AM; abre a las 8:00 AM) · Shop Closing 19 (7:20-9:05 PM) | 39 |
| 09 Cash Drawer | Opening 11 · Closing 12 (recuento por denominación + resumen) · Monthly Cash Log | 23 |
| 10 Production Schedule & Waste Log | Weekly Plan · Made vs Sold · Summary by Category | — |
| 11 Cake Order Form & Order Log | Order Form · Order Log · Pickup Schedule · Today's Orders | — |
| 12 Bakery Allergen Chart | Allergen Matrix · Allergen Chart · Case Sign · Case Labels | — |
| 13 Temperature & Receiving Logs | Temperature Log · Receiving Log · Prep Labels · Shelf Life | — |
| B01 Pre-Shift Meeting | Pre-Shift Huddle 14 | 14 |
| B02 Holiday Calendar | 17 fechas y eventos | — |
| **Total** | **62 hojas** (47 de trabajo + 15 de Instructions) | **413 tareas en las checklists** (+ 17 eventos en el calendario; el censo cuenta 429 desde la fila 5) |

**Plantillas de los libros 10-13:**
- **10 Production Schedule & Waste Log**:
  - «Weekly Plan»: 32 productos de referencia en 5 categorías (Viennoiserie · Cakes & pastries · Bread · Savory · Cookies
    & small cakes), de lunes a domingo, con total semanal y filas verdes libres;
  - «Made vs Sold»: 250 filas, con planificado, hecho, vendido, sobrante, % de merma, coste unitario, coste de la merma
    y el desplegable «Action» con su condición en °F; la nota final (A257) dice que lo expuesto no se congela y cita la
    donación (42 U.S.C. 1791);
  - «Summary by Category»: merma semanal por categoría, con la pauta del 3-8 %.
- **11 Cake Order Form & Order Log**:
  - «Order Form», imprimible: cliente, recogida o entrega, producto, alérgenos del cliente (9 US + gluten + sulfitos +
    UK), importes y depósito, política de depósito, aviso de privacidad US y casilla de marketing aparte (TCPA /
    CAN-SPAM);
  - «Order Log»: 40 encargos, con depósito y saldo pendiente;
  - «Pickup Schedule»: semanal, por hora, de 8:00 AM a 8:00 PM;
  - «Today's Orders»: 16 filas.
- **12 Bakery Allergen Chart**:
  - «Allergen Matrix», BORRADOR con los símbolos propuestos en gris: 43 elementos (40 productos + 3 bases) × 14
    alérgenos (los 9 de EE. UU. + sulfitos + 4 de UK), con proveedor y ficha técnica, fecha de verificación y estado;
  - «Allergen Chart», para el cliente, que se rellena sola desde la matriz;
  - «Case Sign» («Allergen information available in writing — ask our staff»);
  - «Case Labels».
- **13 Temperature & Receiving Logs**:
  - «Temperature Log»: 31 días × mañana y tarde para cámara (32-41 °F), cámara de masas (36-41 °F), congelador (0 °F o
    menos), 2 vitrinas (32-41 °F) y abatidor (≤ 70 °F a las 2 h, minutos), con CF en rojo fuera de rango;
  - «Receiving Log»: 30 filas, con temperatura a la entrega (rojo > 41 °F) y aceptado o rechazado;
  - «Prep Labels»: 25 etiquetas «Made / Use by (date & time) · Batch # · Made by»;
  - «Shelf Life»: 14 preparaciones con su conservación en °F y la nota de date marking.

**Calendario (B02)**, cronológico, con la columna verde «This year's date» para las fechas móviles:
- Three Kings Day y temporada de King cake (6 de enero → Mardi Gras; rosca de Reyes; el muñequito, aparte).
- Valentine's (14 de febrero).
- Pi Day (14 de marzo) y St. Patrick's (17).
- Easter (marzo o abril, variable; hot cross buns, carrot cake).
- Mother's Day (2.º domingo de mayo, pico fuerte; Father's Day, 3.er domingo de junio).
- First Communions y graduaciones (mayo-junio; catálogo en febrero).
- Verano, de Memorial Day a Labor Day, y 4 de julio.
- Halloween (31 de octubre).
- Day of the Dead (1-2 de noviembre, pan de muerto) y Thanksgiving (4.º jueves de noviembre; el miércoles anterior es
  el mayor día de recogida de pies).
- Black Friday y Small Business Saturday.
- Christmas y fiestas (la mayor temporada).
- New Year's Eve.
- Fechas variables: fiestas locales, temporada de bodas (pico de mayo a octubre), pedidos de empresa, cumpleaños, y
  bautizos, showers y aniversarios.

En «Instructions» B7 va la nota UK (Mothering Sunday, bank holidays, Boxing Day).

## Erratas del ES vistas en esta pasada (para su próxima v2.x; la EN las hereda porque G1 exige la misma maqueta)

- 09 «Instrucciones»: el área de impresión es `A1:A20`, pero el texto está en la B, hasta la fila 30. Impresa, sale en
  blanco.
- 09 «Cierre de Caja» A41-A46: los rótulos del resumen van en la columna A, de 5 de ancho, con ajuste. Excel parte las
  palabras («Efect/ivo» en el ES, «(coun/t)» en la EN). Lo natural sería combinar A:B o ensanchar A; en la EN no se
  puede, porque G1 exige los mismos anchos y combinaciones.

## Para la revisión adversarial (UNA, sobre los volcados: lente de un pastry chef con tienda en EE. UU. + lente técnica)

- **Recepción, 3-202.11**: 13 «Receiving Log» A38. Pide: refrigerado TCS ≤ 41 °F; huevos con cáscara en un camión con
  el aire ≤ 45 °F; leche y nata ≤ 45 °F solo donde la ley láctea lo permita, y enfriadas a 41 °F en 4 h (3-501.14);
  congelado sin señales de descongelación.
  - Ojo con la CF de la columna G («Temp at delivery», rojo > 41 °F): una entrega de huevos o leche a 42-45 °F, que es
    legal, sale en rojo. ¿Vale como aviso conservador, o hace falta una nota?
  - «On delivery» en 03 «Manager Weekly» E25 y 04 «Head Pastry Chef» E9.
- **Rellenos TCS en vitrina (3-501.16)**:
  - 02 «Decorating & Finishing» C16;
  - 08 «Instructions» B7 y «Shop Opening» B5: vitrinas encendidas 45 min antes de montar;
  - 06 «Thanksgiving (Nov)» B14: cream pies TCS a 41 °F;
  - 13 «Shelf Life» D16-D17 y B17: «Baked viennoiserie: room temperature, in the case; same day»;
  - 10 «Made vs Sold» A257: lo expuesto no se congela; si se vende algo congelado, «say so», como regla del kit.
- **Merengue, 3-302.13**: 02 «Creams & Fillings» B15-B16 (mousses con merengue italiano o suizo cocido, o claras
  pasteurizadas); 13 «Shelf Life» A9 (Italian meringue, 24 h).
- **Date marking**: 7 días como máximo legal y 24 h como objetivo del kit con huevo.
  - 02 «Creams & Fillings» B12 / C12;
  - 01 «Kitchen Closing» B6;
  - 13 «Instructions» B12-B13, «Prep Labels» B2 y «Shelf Life» D5-D11 y A24;
  - ganache 5–7 días y trufas 5 días, a 32–41 °F (D7, D10).
- **Menores**: 06 «Holiday Season» B9.
  - Menores de 18: sin amasadoras, batidoras industriales, laminadoras ni divisoras, ni limpiarlas (29 CFR 570.62,
    HO 11), con la excepción de las batidoras de sobremesa de 5 qt o menos.
  - 14-15 años: nada de hornear (29 CFR 570.33(h)).
  - Confirmar el alcance exacto de la excepción de HO 11 y si hace falta citar a la DOL Fact Sheet #58.
- **Depósitos de encargos**: 06 «Celebration Cakes (Apr-Jun)» B14 (30–50 %, «common practice, not law; check your
  state's rules on nonrefundable deposits»); 11 «Order Form» A37-A39 e «Instructions» B9 y B21; «Order Log» K-L.
- **Alérgenos del 12**:
  - perfil ES → EN de cada referencia: Concha, Three Kings bread (rosca), Hot cross buns, Paczki, Amaretti, Pignoli,
    Polvorones (Mexican wedding cookies), torrone, Chocolate Easter cake, Tuna empanada;
  - las 4 columnas UK; sulfitos (10 ppm);
  - «Instructions» B4 y B7-B8 (borrador y 3-602.12(C) donde se haya adoptado) y «Case Sign» B28;
  - 11 «Order Form» A23 (alérgenos del cliente) y la privacidad: A46 «Privacy notice», «Instructions» B17 y la casilla
    de marketing A49 (TCPA / CAN-SPAM).
- **Umbrales °F del 13** (D7):
  - CF de «Temperature Log»: B:C 32-41, D:E 36-41, F:G > 0, H:I y J:K 32-41, L > 70 (2 h), M > 120 min;
  - «Instructions» B16-B17 (el 41 °F se puede bajar, nunca subir);
  - A40: más de 2 h por encima de 41 °F → se tira (regla del kit); 4 h solo con procedimiento escrito (3-501.19).
- **Calendario US (B02)**: Three Kings Day → Mardi Gras y King cake; Pi Day; First Communions; Day of the Dead; el
  miércoles antes de Thanksgiving; temporada de bodas de mayo a octubre; F de cada fila (plazos); G15 «Wholesale orders
  from other food businesses» en New Year's Eve.
- **Retoques de esta pasada**: las 9 cadenas sin «[kit criterion]», 13 «Temperature Log» A38 «Count» y 09 A46 «POS Z:
  sales + tax, excl. tips».
- **Horas**: obrador desde las 5:00 AM (01 «Kitchen Opening» 5:00-7:50 AM); tienda de 8:00 AM a 8:00 PM (08); cierre
  de obrador hasta las 9:00 PM.
- **Versión**: los 15 EN dicen «Version 2.0 · October 2026»; el ES mezcla 2.0 y 2.1 (SPEC §5).
- **Código común**: la rama de texto girado de `objetivo_ajuste`. ¿Es razonable 5,25 pt por unidad de ancho?
  Conservador: a 11 pt, un carácter mide unos 5,5-6 px y una unidad, 7 px.
