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

## Ronda 1 de la revisión adversarial (`revision/REVISION-F2.md`: 1 BLOQUEANTE · 8 MAYOR · 22 menores · erratas ES de maquetación)

Aplicados el BLOQUEANTE, los 8 MAYOR y 20 de los 22 menores (decisiones del orquestador). Todo va por celda: G1/G2
JSON, `POR_CELDA`, `VALORES_EN`, `CF_POR_CELDA` y `ALTOS_FILA`. No hay filas nuevas ni tareas nuevas, así que las
cifras de tareas no cambian. M8 y m20 se han arreglado **en el ES LIVE** y la EN los hereda: G1 sigue exigiendo la
misma maqueta que el ES, sin desviación declarada.

### Parche del ES LIVE (`kit-tareas-pasteleria`, sin cambio de versión, XML)

Lo hace el script del scratchpad `patch_es_pas.py`. Estilos, DV, CF, caché y docProps quedan byte a byte.

| Fichero ES | Cambio |
|---|---|
| `09-apertura-cierre-caja.xlsx` | «Instrucciones»: área `$A$1:$A$20` → `$A$1:$B$30` · «Registro Mensual»: área `$A$1:$I$38` → `$A$1:$J$38` · «Cierre de Caja»: columna A 5 → **24** y B 50 → **31** (mismo ancho impreso; rótulos A41-A46 y «Denominación» A19 enteros) |
| `02-partidas-cocina.xlsx` | «Cremas y Rellenos» C8: «Almíbar a 118-121 °C · mantequilla a 18-20 °C» → «Italiano: almíbar a 118-121 °C · suizo: claras y azúcar a 71 °C · mantequilla a 18-20 °C» |

- El volcado ES de antes y de después difiere en 3 líneas: C8 y las dos áreas. Los anchos no salen en el volcado; se
  han comprobado con openpyxl: A 24, B 31.
- ES: `censo-entregables --only kit-tareas-pasteleria --fail` 0 defectos · `gate-no-latinos` 0.
- El generador `scripts/productos-digitales/kit-pasteleria-v2_0-postprocess.py` lleva lo mismo (C8, áreas y anchos).
  `generate-tareas-pasteleria*.py` no define ni esas celdas ni esas áreas.
- Regenerados `extraer_textos` (censo_es.json y textos_es.json), `mapas_pastry` y `heredar`: los 1.361 ids siguen
  igual, solo cambia el ES de c0162 (C8, regenerar) y los ADAPTAR. Siguen 63 heredadas y 820 pendientes.

### Tabla de la ronda

| Id | Dónde (EN) | Aplicado en |
|---|---|---|
| B1 | 02 «Decorating & Finishing» B15/C15 · 08 «Shop Opening» B15 · B02 G10 · 13 «Shelf Life» D17 · B01 B6 | c0208 (fruit danishes, sin custard en la vitrina ambiente), c0209 (lo relleno de natillas, crema o queso, a 41 °F, 3-501.16), c0697 (quiche, empanadas y croissant de jamón y queso a la vitrina refrigerada), c1320 («all year round»), c1259 · `POR_CELDA` D17 (relleno y salado: 41 °F o tiempo como control, 3-501.19) · `REGLAS_US['vitrina_tcs']` con lo salado |
| M1 | 02 «Creams & Fillings» B18 · 02 «Doughs & Fermentation» B25 · 04 «Pastry Cook» B17 · 01 «Kitchen Opening» B21 | c0178 (praline paste y nut brittle en su puesto, con utensilios propios), c0136 (sésamo y semillas en sus bandejas), c0348 (alergia confirmada: primero del día, mesa sanitizada, etiqueta aparte), c0043 (harinas de frutos secos y semillas en cubos cerrados) |
| M2 | B01 B23 · 01 «Kitchen Opening» B17 · 04 «Counter Associate» B11 | c1274 (exclusión, 2-201.11 / 2-201.12), c0037 (lavamanos, 6-301.12), c0376 (pinzas o papel, 3-301.11) · `REGLAS_US` + `enfermos_pas`, `lavamanos_pas`, `mano_desnuda` |
| M3 | 12 «Allergen Matrix» I8 (concha), I28 (polvorones) | `VALORES_EN` ○ → ● · c1103 (V28) · `G6_ESPERADO` (abajo) |
| M4 | 06 «Thanksgiving (Nov)» B13, B14, B22 | c0621 (fruit pies; pecan = nut pie, con huevo: en frío salvo que la autoridad sanitaria diga lo contrario), c0622 (custard pies, 135 → 70 °F en 2 h → 41 °F en 4 h, 3-501.14; TCS, 3-501.16), c0632 |
| M5 | 06 «Holiday Season» B9 | c0475 (HO 11 solo 16-17 años; batidoras portátiles ≤ 5 qt y ≤ ½ hp; 14-15 años sin máquinas eléctricas, 570.33(e), ni hornear, (h); nada antes de las 7 AM ni después de las 7 PM en curso escolar, 570.35) · `REGLAS_US['menores_hornear']` |
| M6 | 06 «Holiday Season» B29, B31, B32, B33 | c0503 (King cake del 6 de enero al Mardi Gras), c0507 (primera hornada: un tercio, para el 5 y la mañana del 6), c0509 (hornada principal 60-70 %: el 6 es el día fuerte), c0511 (rellena: al momento y a 41 °F; la mexicana suele ir sin rellenar). Las fechas E31/E32 («Jan 4–5», «Jan 5–6») ya casaban |
| M7 | 02 «Creams & Fillings» B15 · 13 «Shelf Life» D7 · 01 «Kitchen Opening» B16 | c0172 «melted chocolate», c1217 «Bring to room temperature», c0036 (mantequilla «to working temperature», el otro calco de «atemperar») |
| M8 | 09 «Cash Drawer Closing» A41-A46 | ES LIVE (columna A 24 / B 31) |
| m1 | 02 «Creams & Fillings» C8 | `POR_CELDA` «Italian: syrup at 244–250 °F · Swiss: whites and sugar to 160 °F · …» · `GRADOS_F_SPEC` + 160 · ES LIVE C8 |
| m2 | 02 «Doughs & Fermentation» B30/B31 | c0143/c0145 con su tilde («sablée», «brisée») · `gates_en.LISTA_BLANCA_TILDE` + las dos |
| m3 | 02 B18 | con M1 (c0178) |
| m4 | 05 «Monthly Maintenance» B6 · 06 «Easter» B8 · 08 B24 / «Shop Closing» B22 | c0424 (self-clean cycle), c0544 (chicks), c0709 / c0730 (roll-down security gate, if you have one) |
| m5 | 06 «Holiday Season» B12 | c0480 (24, 25 y 31 de diciembre y 1 de enero; el 6, solo si se venden roscas) |
| m6 | 06 «Valentine's Day» D17 · «Mother's & Father's Day» D14 | `POR_CELDA` = «Manager» |
| m7 | 01 «Kitchen Closing» E27, D27, D29 · 08 «Shop Opening» B5 | `POR_CELDA` E27 «8:05 PM», D27 y D29 «Shift lead» · c0684 (desarmar la zona de la tienda si el obrador no lo ha hecho) |
| m8 | 11 «Pickup Schedule» A17 | `POR_CELDA` «7:30 PM» (última franja antes de cerrar la puerta a las 7:50) |
| m9 | 12 «Case Labels» B2 · frase de contacto cruzado (12 «Allergen Matrix» A54 y «Case Sign» B7) · 11 «Order Form» A23 | c1146 (+ P peanuts, F fish, SH shellfish), c1122 (+ fish, «replace with your own list»), c0983 (+ sulfitos) |
| m10 | 12 «Allergen Matrix» N24 (hot cross buns) | `VALORES_EN` ○ → ● · c1098 (V24) |
| m11 | 13 «Receiving Log» CF G5:G34 · A38 | `CF_POR_CELDA` > 41 → **> 45** (huevos y leche legales a 42-45 °F ya no salen en rojo) · c1194 (paréntesis de la leche al derecho y aviso: rojo solo por encima de 45 °F; entre 41 y 45 °F, solo huevos con cáscara y leche o nata donde se permita) · `ALTOS_FILA` fila 40 → 42 pt |
| m12 | 13 «Temperature Log» D4 · M5 | `POR_CELDA` D4 «Dough retarder (36 to 41 °F, in retard mode)» · c1177 «Min. to 70 °F» |
| m13 | 13 «Temperature Log» A40 | c1180 (el tiempo como control exige procedimiento previo y hora marcada; no se aplica a posteriori a una avería) · `ALTOS_FILA` fila 41 → 37 pt |
| m14 | 13 «Shelf Life» A10 | c1222 «Cooked chocolate truffle cream (filling)» |
| m15 | 11 «Instructions» B17 · «Order Form» A46 | c0945 (bajo llave el tiempo que aconseje el seguro o el abogado, como prueba ante una reclamación) [criterio del kit], c1015 |
| m16 | B02 B9 / G9 | `CALENDARIO` B9 «May peak · Apr–Jun (varies)» (con «Apr–Jun» al principio, la comprobación cronológica de `mapas_pastry` falla: abril iría antes que mayo) · c1315 (parroquias hispanas, italianas, polacas y filipinas) |
| m17 | B02 «Instructions» B7 | c1283 (Mothering Sunday: 3 semanas antes de Pascua, marzo o principios de abril) |
| m18 | B02 G15 | c1341 (la venta mayorista puede necesitar su propia licencia; sin «restaurants», término prohibido) |
| m19 | B02 E4 | c1292 (+ paczki para el Fat Tuesday) |
| m20 | 09 áreas de impresión | ES LIVE |
| m21 | 10 «Made vs Sold» DV K | **No aplicado**: la lista del desplegable ya mide unos 200 de los 255 caracteres que admite Excel, y sus valores son claves (CLAVES, SUMIF). Añadir «Day-old markdown» obliga a tocar la DV del ES |
| m22 | 05 «Monthly Maintenance» B15 | c0433 (+ control de plagas: trampas, puntos de entrada e informe de la empresa) |
| Dudas 1-5 | — | Solo las que ya cubren los arreglos: 3 (fruit danishes) con B1; 4 (M8/m20) en el ES; 5 (matriz) con `VALORES_EN` + `G6_ESPERADO`. La 1 (suizo a 160 °F en las mousses) y la 2 (pecan) se quedan como están: B15-B16 siguen con «cooked Italian or Swiss meringue or pasteurized whites», y el pecan va con la frase de la autoridad sanitaria |

- **ADAPTAR**: un bloque «Ronda 1» en `mapas_pastry` alinea la guía del traductor con el EN nuevo. Así, una
  re-traducción no reintroduce ni el «con calor», ni el 5 de enero, ni las «custard danishes».
- **`REGLAS_US`**: cambia `menores_hornear` (570.33(e) y 570.35); se añaden `enfermos_pas` (2-201.11, 2-201.12),
  `lavamanos_pas` (6-301.12) y `mano_desnuda` (3-301.11); 3-501.14 y 3-501.16 ya estaban. G7: 52 citas, todas
  permitidas (42).

### Código común (`gates_en.py`, dos cambios)

- `G6_ESPERADO` (getattr, vacío por defecto) recoge los valores calculados que cambian a propósito porque dependen de
  `VALORES_EN`. G6 los compara con lo declarado, no con el ES.
  - En la pastelería son 10: los «Total ●» Q8, Q24 y Q28; los totales de columna I53, N53, I54 y N54; y la carta
    H9, M25 y H29.
  - Sin la declaración, G6 da exactamente esos 10 fallos. Cualquier otra diferencia sigue fallando.
- `LISTA_BLANCA_TILDE` + «sablée», «brisée».
- **Hermanos (9)**: comparé la salida de `gates_en` y `--autotest` de HEAD (`b3f6790c`) con la del nuevo, sobre lo
  publicado y en un worktree limpio. Es **idéntica en los 9**:
  - base, bar, catering, heladería y chocolatería: VERDE 8/0, autotest OK (16 / 16 / 20 / 19 / 19);
  - cafetería, pizzería, hamburguesería y ghost kitchen: su ROJO previo de `adf52a52`, igual que antes.
  `aplicar_en.py` no se toca en esta ronda.

### Resultados de la ronda

| Paso | Resultado |
|---|---|
| Montaje | 15 xlsx · idempotencia 0 diferencias · `inject_cache` sin fallos · 0 desbordes · 0 rellenos · 46 ajustes · 50 altos subidos (2 por `ALTOS_FILA`) |
| **Gates** | **VERDE 8/0**. G1 igual (62 hojas, 1.866 fórmulas, 41 DV, 51 CF, 344 merges, 429 tareas; anchos y áreas = censo regenerado). G3 46 ajustes · 53 altos. G4 280 regenerar · 955 traducir · 220 horas · **3 valores fijados**. G6 1.408 con valor · **10 declarados**. G7 183 °F · 52 citas (42 permitidas) |
| Autotest | **20/20 CAZADOS**: los 19 de antes y el «valor fijado» de `VALORES_EN` (12) |
| Celdas cortadas | **0 nuevas**. 44 que ya traía el ES (28 «Verified by:» y 16 rótulos y títulos que se pasan por menos de 1 pt); las 6 del 09 desaparecen con la columna A de 24. 30 del ES que la EN arregla |
| censo-entregables · no-latinos | EN 0 · 0 · ES 0 · 0 |
| Copia al Mac | sha256 26/26 iguales VPS ↔ Mac (15 EN, 2 ES, volcados, datos y código) |
| Volcados | `revision/dump_en.txt` y `dump_es.txt` regenerados, 6.498 líneas cada uno |

**Cifras para la landing**: las tareas no cambian (413 en las checklists + 17 eventos; por fichero, igual que arriba),
ni las hojas (62) ni las plantillas del 10 al 13. Lo que sí cambia de contenido:
- **12:** la matriz propone leche ● en la concha y los polvorones y sulfitos ● en los hot cross buns; la leyenda de
  las etiquetas trae ya 10 abreviaturas.
- **13:**
  - la recepción se pone en rojo por encima de 45 °F;
  - la cámara de masas se lee en modo retardo;
  - la vida útil añade lo salado y lo relleno a 41 °F.
- **11:** la última franja de recogida es a las 7:30 PM, y las fichas se guardan el tiempo que aconseje el seguro.
- **B02:** las comuniones son «May peak · Apr–Jun» y en enero aparecen los paczki para el Fat Tuesday.
