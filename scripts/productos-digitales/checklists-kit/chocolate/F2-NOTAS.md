# Chocolate Shop Checklists Kit Pro — F2: construcción real (24-oct-2026 · sesión Claude Code)

Todo el python se ha ejecutado en el VPS (`/root/wt-chocopastry`, rama `feat/chocolate-pastry-checklists-en`, venv
`/root/venv-guias`).

Textos: `textos_en/heredado.json` (105: 101 de la heladería, 2 de la cafetería y 2 del catering) + `textos_en/G1.json`
(433, del traductor sonnet en `a5fa9b90`, con 38 retocadas en esta pasada) = las 538 cadenas a traducir. GM 215 por
`mapas_chocolate.py` (184 `POR_CELDA`, 30 horas). `heredar.py --kit chocolate`: **0 cambios** (heredado.json y
pendientes.json idénticos a lo commiteado).

## Dudas resueltas

- **«Tiras de sanitizante: no caben por ancho»** (nota del traductor sobre c0357, c0359 y c0366): no es así. En el
  molde ligero (01-07, B01, B02) las filas de tareas tienen alto **automático**: la celda B (45 de ancho, con ajuste)
  crece al alargarse. No ha hecho falta ni `ALTOS_FILA` ni `POR_CELDA`, así que las tiras van en las **6** tareas de
  superficies, con la fórmula de los hermanos.

## Cambios de esta pasada

- **G1.json: 38 cadenas.** El traductor había dejado fuera el ADAPTAR de la SPEC en 38 de las 118 que lo llevaban. Se
  ha aplicado en la fuente (script `g1_adaptar.py` del scratchpad); todo sale de `mapas_chocolate.ADAPTAR`, así que G7 lo
  admite.

  | Tema | Ids (dónde) |
  |---|---|
  | Tiras de sanitizante «(approved sanitizer at label strength, test strip; FDA 4-501.114)» | c0078 (01 Closing B10) · c0086 (01 Closing B18, + «dry them well») · c0322 (04 Sales Associate B23) · c0357 (05 Weekly B7, + «dry it well») · c0359 (05 Weekly B9) · c0366 (05 Weekly B18) |
  | Higiene y mano desnuda (3-301.11, 2-201.11, 100 °F) | c0031 (01 Opening B8) · c0033 (B10: + ictericia y dolor de garganta con fiebre) · c0056 (B29) · c0311 (04 B8) · c0316 (04 B15) |
  | Gas: protocolo si huele (D10) | c0035 (01 Opening B12) |
  | Los 9 alérgenos y el aviso escrito de la vitrina (3-602.12(C), donde se haya adoptado) | c0052 (01 Opening B26) · c0310 (04 B7) · c0396 (05 Monthly B25) |
  | Etiqueta de lo envasado (3-602.11: nombre, ingredientes, peso neto oz y g, alérgenos, negocio) | c0154 (02 Molding B25) · c0295 (04 Chocolatier B12) · c0479 (06 Easter B17) |
  | Date marking de 7 días de lo TCS (3-501.17) | c0159 (02 Molding B31) · c0239 (03 Weekly B14) |
  | Tabla de vida útil | c0176 (D42: solo con aw de laboratorio) · c0185 (D45: «Alcohol-filled candy: check your state rules») · c0110 (02 Instructions B17: granel a 0 °F) |
  | Báscula, calibración, extintores, plagas | c0378 (05 Weekly B34, legal-for-trade) · c0411 (05 Q&A B16) · c0384 (05 Monthly B9, 32 °F) · c0385 (B10, OSHA 1910.157(e)(2)) · c0394 (B23, licensed operator) · c0409 (Q&A B14, auger) |
  | Campañas y calendario | c0432 (06 Instructions B15: shipping cutoff, 22 de diciembre) · c0435 (gelt) · c0440 (shipping cutoff, Christmas Eve / New Year's Eve) · c0467 (insulated mailer y cold packs) · c0548 (08 B17, permiso de la ciudad) · c0708 (B02 Instructions B7: nota UK) · c0719 (febrero: shipping cutoff) · c0729 (mayo: «2 weeks out») · c0273 (03 Monthly B23: Yelp) |

- **`censo-entregables.py` (`PRODUCTOS_LETTER`)**: faltaba `chocolate-shop-checklist-templates`. El primer montaje
  real salía en ROJO en G8 («noprint» en los 11: el censo exigía A4). Se ha añadido en una línea propia, para no chocar
  con la pastelería. Los 8 hermanos siguen con 0 defectos.
- **Celdas cortadas**: con el script del scratchpad `cortadas.py` (`ancho_texto` / `n_lineas` / `caja` de `aplicar_en`,
  EN contra ES, sobre las 1.759 celdas de texto), **0 nuevas** antes y después de los retoques de G1. Por eso no hay
  `ALTOS_FILA` ni `AJUSTE_FORZADO` en `mapas_chocolate`.
  - D42 crece a 4 líneas (60 pt): el alto de la fila de la tabla lo pone `capa_ajuste`.
  - Queda 1, la de todos los hermanos: «Denomination» del 09 (Cash Drawer Closing A27, la A25 del base +2).
  - El ES trae 65 celdas que la EN deja de cortar: títulos A1, notas D39-D48 de la tabla de vida útil, «Instrucciones»
    sin ajuste y C4/F4/A37 del registro mensual.
- **Letter**: las 37 hojas EN llevan `paperSize` 1. G3 lo comprueba y el autotest lo caza.
- **Código común** (`mapas.py`, `aplicar_en.py`, `gates_en.py`, `kit.py`): **intacto**. No hace falta el dry-run de
  los hermanos.

## Comandos (en `scripts/productos-digitales/checklists-kit/`)

    python3 heredar.py --kit chocolate
    python3 aplicar_en.py --kit chocolate --dry-run --idempotencia --mes October --salida <tmp>
    python3 gates_en.py --kit chocolate --mes October --dir <tmp> [--autotest]
    python3 aplicar_en.py --kit chocolate --idempotencia --mes October     # → astro-site/public/dl/chocolate-shop-checklist-templates/
    python3 gates_en.py --kit chocolate --mes October [--autotest]
    python3 ../censo-entregables.py --only chocolate-shop-checklist-templates --fail
    python3 ../gate-no-latinos.py --only chocolate-shop-checklist-templates
    python3 volcar_xlsx.py --kit chocolate ../../../astro-site/public/dl/chocolate-shop-checklist-templates chocolate/revision/dump_en.txt --orden en
    python3 volcar_xlsx.py --kit chocolate ../../../astro-site/public/dl/kit-tareas-chocolateria chocolate/revision/dump_es.txt --orden es

## Resultados

| Paso | Resultado |
|---|---|
| Montaje | 11 xlsx (nombres de `SPEC.md` §2) · idempotencia: 0 diferencias · `inject_cache` 139/139 sin fallos de pycel · 0 desbordes · 0 rellenos · 42 ajustes activados y 53 altos subidos (ninguno a mano) |
| G1 | 37 hojas · 139 fórmulas (15 por celda, 1 con hoja) · 26 DV (460 celdas) · 26 CF (17 por celda, D7) · 195 merges · 5 protegidas · 831 desbloqueadas · 30 nombres definidos · 7 áreas de impresión |
| G2 | sin español, €, no latinos ni términos prohibidos (2.056 términos revisados, 1.759 valores) · 282 formatos € reescritos |
| G3 | Letter 37/37 · pie 37 · marca 7 (01-07 y bonus sin marca) · versión 2.1 en 11 · 42 ajustes · 55 altos |
| G4 | 794 glosario · 183 regenerar · 601 traducir · 6 citas de fichero · 20 de pestaña · 30 horas · 71 mensajes de DV |
| G5 | 15 denominaciones · 2 `CASOS_G5` (204.91; 4,200 y over/short 0) · 9 comprobaciones |
| G6 | 139 fórmulas con valor (48 contadores) |
| G7 | 87 °F y 24 citas normativas (antes de los retoques, 9), todas en `REGLAS_US`/`ADAPTAR` (41 permitidas) · 36 celdas ES con °C · 1 `CELSIUS_SIN_F` (08 B19) |
| G8 | censo + no-latinos OK |
| **Gates** | **VERDE 8/0** |
| Autotest | **19/19 CAZADOS**: los 16 del base, el término prohibido y las 2 de la CF de excepción (D7) · `VALORES_EN` vacío (no hay inventario con mínimos) |
| censo-entregables · no-latinos | 0 defectos (`--fail`) · 11 ficheros, 0 con no latinos |
| Celdas cortadas | 0 nuevas · 1 heredada («Denomination», 09) · 65 del ES arregladas en la EN |
| Hermanos | código de la F2 intacto · `censo-entregables --fail`: restaurant, bar, coffee-shop, catering, pizza-shop, burger-joint, ghost-kitchen e ice-cream-shop, 0 defectos cada uno |
| Copia al Mac | `scp` de los 11 xlsx a `astro-site/public/dl/chocolate-shop-checklist-templates/` y de los 2 volcados · sha256 13/13 iguales |
| Volcados | `revision/dump_en.txt` y `dump_es.txt`, 2.669 líneas cada uno |

### Cifras para la landing (F3)

Las tareas son las filas con número en A y texto en B; el método da 298 en la heladería, como su F2. ES: 338, igual que
la SPEC.

| Fichero | Hojas (sin Instructions) | Tareas |
|---|---|---|
| 01 Opening & Closing | Opening 25 · Closing 16 | 41 |
| 02 Tempering & Molding | Tempering 19 (dark, milk y white) · Molding & Bars 22 (+ tabla de vida útil, 10 tipos) | 41 |
| 03 Manager | Daily 15 · Weekly 20 · Monthly 12 | 47 |
| 04 Duties by Role | Chocolatier 16 · Sales Associate 16 · Shift Lead 12 | 44 |
| 05 Cleaning & Maintenance | Weekly 20 · Monthly 14 · Quarterly & Annual 14 | 48 |
| 06 Seasonal | Holiday Season 15 · Valentine's Day 12 · Easter 13 | 40 |
| 07 Blank Template | By Area · By Shift · By Role (en blanco) | 0 |
| 08 Whole Shop | Shop Opening 17 (9:00-9:30 AM; la tienda abre a las 10 AM) · Shop Closing 15 | 32 |
| 09 Cash Drawer | Opening 13 (9:15-9:45 AM) · Closing 14 · Monthly Cash Log | 27 |
| B01 Pre-Shift Meeting | Pre-Shift Meeting 18 | 18 |
| B02 Holiday Calendar | 12 meses (acciones, productos y temporada Peak / High / Medium / Low) | 0 |
| **Total** | **37 hojas** (11 de Instructions) | **338** |

**Tabla de vida útil** (02 «Molding & Bars» B39-D48; a 59–64 °F y 50–60 %):

| Tipo | Vida útil |
|---|---|
| Bars and unfilled chocolate | 12–18 months |
| Hollow figures and solid pieces | 6–12 months |
| Fresh-cream ganache bonbons | 7 days at 41 °F (TCS) |
| UHT cream, sorbate or alcohol | 4–8 weeks, solo con aw de laboratorio |
| Praline, gianduja and nut | 2–4 months |
| Truffles and coated clusters | 3–4 weeks |
| Liqueur and sugar-crystallized | 3–6 months |
| Candied nuts and dipped fruit | 1–3 months |
| Dipped wafers and crisps | 3–4 weeks |
| Finished chocolate | Never frozen (solo el granel de ganache, a 0 °F, 1–2 months) |

**Calendario (B02).** Temporada: Peak en febrero y diciembre · High de marzo a mayo y en noviembre · Medium en junio,
septiembre y octubre · Low en enero, julio y agosto.
- Enero: liquidación de las fiestas.
- Febrero: Valentine's (14); encargos hasta el 10, exprés el 13 y el 14, shipping cutoff.
- Marzo: St. Patrick's (17) y preparación de Easter.
- Abril: Easter (fecha variable) y graduaciones.
- Mayo: Mother's Day (2.º domingo; encargos 2 weeks out), Teacher Appreciation Week, graduaciones.
- Junio: Father's Day (3.er domingo) y bodas.
- Julio: 4 de julio y cold packs.
- Agosto: calor, mantenimiento y pedido de couverture.
- Septiembre: Labor Day (1.er lunes) y apertura del corporate gifting.
- Octubre: Halloween (31), Sweetest Day y National Chocolate Day (28).
- Noviembre: Thanksgiving (4.º jueves), Black Friday y Small Business Saturday.
- Diciembre: Christmas, Hanukkah (gelt), shipping cutoff y horario especial del 24 y el 31.

En «Instructions» B7 va la nota UK (Mothering Sunday, bank holidays, Boxing Day). El kit no trae inventario con mínimos.

## Para la revisión adversarial (UNA, sobre los volcados: lente de un chocolatier con tienda en EE. UU. + lente técnica)

- **Curvas de templado en °F** (02 «Tempering», del traductor; las conversiones de las cifras del ES cuadran):
  - dark: 122–131 → 81–82 → 88–90 °F; test a 68 °F en 3–5 min;
  - milk: 113–122 → 79–81 → 84–86;
  - white: 104–113 → 77–79 → 82–84; el test de milk y white, a 64–68 °F;
  - temperadora precalentada a 113 °F (01 «Opening» B15).

  Hay que confirmar que basta con «per the manufacturer's curve» en «Instructions» B11 y B15, sin repetirlo en cada
  celda. Mirar también los porcentajes de cacao de B6-B8 (55–70 / 35–40 / 28–33 %).
- **Ganache TCS, 7 días**: C41/D41 de la tabla, 02 B31 (c0159), 03 «Weekly» B14 (c0239); D42 (4–8 semanas solo con
  aw de laboratorio); D48 (granel congelado a 0 °F, 1–2 meses, descongelado 24 h en la nevera).
- **Licor en bombones**: tabla B45/D45 («Liqueur and sugar-crystallized bonbons», 3–6 months; «Alcohol-filled candy:
  check your state rules»). ¿Hace falta algo más (límite de alcohol, venta a menores) o vale con remitir al estado?
- **Gas (D10)**: 01 «Opening» B12 (ahora con el protocolo de olor a gas), «Closing» B25, «Instructions» B15 y 08 «Shop
  Closing» B13. Comprobar también el reorden del 08 «Shop Closing»: vitrinas y temperatura del obrador (B9-B10) antes
  de la caja y la alarma; HVAC < 68 °F (B15).
- **Calendario US (B02)**:
  - Sweetest Day (3.er sábado de octubre) y National Chocolate Day (28);
  - Teacher Appreciation Week;
  - «chocolate turkeys» en noviembre;
  - «Hot Chocolate» en los productos de enero (término permitido);
  - las temporadas Peak/High/Medium/Low;
  - abril con graduaciones en lugar de bodas y baby showers.
- **Las 38 cadenas que reescribe esta pasada** (tabla de arriba). Mirar sobre todo:
  - los 9 alérgenos (incluidos fish y shellfish) en una chocolatería;
  - la longitud de 01 «Opening» B26 y 04 B7;
  - «production day = day 1».
- **Rarezas del traductor que no he tocado**:
  - c0442, 06 «Holiday Season» B15: «Make artisan bark and toffee: praline, nut brittle, truffle»;
  - c0477, 06 «Easter» B15: «Make decorated chocolate Easter baskets», que repite B9; el ADAPTAR pedía huevos grandes
    rellenos o centros de mesa;
  - c0204: FLSA, «2 years», sin las nóminas a 3 años.
- **Horas +2 h**: 08 9:00-9:30 AM y 09 9:15-9:45 AM; la tienda abre a las 10 AM (D9).
- **05 «Quarterly & Annual»**: aw de laboratorio, bombo (panning machine), báscula legal-for-trade, candy en el sales
  tax, NFPA 96 solo con grasa, EPA 608.
- **Código común**: no se toca nada de la F2. `censo-entregables.py` solo añade el slug a `PRODUCTOS_LETTER`.
