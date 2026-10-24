# Ice Cream Shop Checklists Kit Pro — F2: construcción real (24-oct-2026 · sesión Claude Code)

Todo el python en el VPS (`/root/wt-icecream`, rama `feat/ice-cream-shop-checklists-en` en `37243d44` + los cambios de
abajo, venv `/root/venv-guias`). Textos: `textos_en/heredado.json` (87: 81 de la cafetería y 6 del catering) +
`textos_en/G1.json` (403, traductor sonnet en `37243d44`) = las 490 cadenas a traducir; GM 215 por `mapas_icecream.py`
(183 `POR_CELDA`, 29 horas). `heredar.py --kit icecream`: **0 cambios** (heredado.json y pendientes.json idénticos;
`extraer_textos` solo reescribe la fecha y el commit de `censo_es.json` / `textos_es.json`, revertidos).

## Dudas resueltas

- **c0332** (05 «Weekly Upkeep & Stock» B10), «If you serve coffee or hot drinks: backflush the group head…»: el ES
  dice «backflush del grupo… cambio de junta», que es la máquina de espresso (grupo y junta del portafiltro). Se queda
  como está, condicionada («If you serve…»); no lleva ningún término prohibido (barista, cafe).

## Cambios de esta pasada

- **`gates_en.py` (código común, solo el autotest)**: los libros del autotest se buscaban por nombre ES fijo
  (`02-partidas-cocina.xlsx`, `06-eventos-festivos.xlsx`) y la heladería los llama `02-partidas-produccion` y
  `06-eventos-temporada` → `KeyError` al importar. Ahora `_libro('01'…'09')` los busca por prefijo, como ya hacía el 09.
  En los hermanos devuelve el mismo fichero que antes (cada uno tiene un solo libro por prefijo).
- **G7 rojo en la primera pasada**: `REGLAS_US` heredaba del base «parasitos» (−31 °F) y «recalentado» (165 °F), que no
  están en `GRADOS_F_SPEC` (SPEC §3: «sin recalentado: no aplica»; una heladería no sirve pescado crudo). Ninguna celda EN
  las usa → fuera de `REGLAS_US` en `mapas_icecream` (no en el base). Así G7 caza cualquier 165 °F o −31 °F que se cuele.
  Citas permitidas: 62 → 56.
- **Celdas cortadas** (`ancho_texto` / `n_lineas` / `caja` de `aplicar_en`, sobre las 1.633 celdas de texto, EN contra
  ES; script del scratchpad, validado antes con la ghost kitchen, donde da sus 4 + 01 B9, y con el catering): **1 nueva**
  en la primera pasada, ninguna después:
  - 02 «Batch Freezing» C35 (tabla de vida útil): «6 months at 0 °F · 2–3 months refrigerated», 3 líneas en la columna
    de 14. En el ES la fila 35 es automática y la crece C35; en la EN, `capa_ajuste` le fija 30 pt por la nota
    combinada de la D (2 líneas, Excel no autoajusta las combinadas) y ese alto fijo cortaba C35 → `ALTOS_FILA`
    `('02', 'Mantecación', 35): 45.0`. Las filas 31-34 y 36 caben en 30 pt.
  - Queda 1, la de todos los hermanos: «Denomination» del 09 (molde base). El 07 es del molde ligero y no trae los tres
    «Verified by:» del base.
  - El ES trae 55 celdas que la EN deja de cortar: los títulos A1 combinados de alto automático, las notas D31-D36 de la
    tabla de vida útil y textos de «Instrucciones» sin ajuste (`AJUSTE_MAQUETA_ES` + altos de `capa_ajuste`).
  - «Dipping cabinet» en la columna de zona y los títulos largos (~80 caracteres): 0 avisos; G3 sin desbordes.
- **c0120** (02 «Pasteurizing» B13, G1.json): «…your state license minimum rule» → «…your state license minimums take precedence» (la coletilla del ADAPTAR quedaba sin verbo).
- **Letter**: las 38 hojas EN con `paperSize` 1 (Letter); el ES, 38 en A4 (9). G3 lo comprueba y el autotest lo caza.

## Comandos (en `scripts/productos-digitales/checklists-kit/`)

    python3 extraer_textos.py --kit icecream && python3 icecream/mapas_icecream.py && python3 heredar.py --kit icecream
    python3 aplicar_en.py --kit icecream --dry-run --idempotencia --mes October --salida <tmp>
    python3 aplicar_en.py --kit icecream --idempotencia --mes October     # → astro-site/public/dl/ice-cream-shop-checklist-templates/
    python3 gates_en.py --kit icecream --mes October [--autotest]
    python3 ../censo-entregables.py --only ice-cream-shop-checklist-templates --fail
    python3 ../gate-no-latinos.py --only ice-cream-shop-checklist-templates
    python3 volcar_xlsx.py --kit icecream ../../../astro-site/public/dl/ice-cream-shop-checklist-templates icecream/revision/dump_en.txt --orden en
    python3 volcar_xlsx.py --kit icecream ../../../astro-site/public/dl/kit-tareas-heladeria icecream/revision/dump_es.txt --orden es

## Resultados

| Paso | Resultado |
|---|---|
| Montaje | 11 xlsx (nombres de `SPEC.md` §2); idempotencia 0 diferencias; `inject_cache` 141/141 sin fallos de pycel; 0 desbordes; 0 rellenos; 45 ajustes activados y 50 altos subidos (1 por `ALTOS_FILA`) |
| Gates | **VERDE 8/0**. G1 38 hojas · 141 fórmulas (15 por celda, 1 con hoja) · 27 DV (420 celdas) · 27 CF (18 por celda, D7) · 189 merges · 5 protegidas · 811 desbloqueadas · 31 nombres definidos · 24 paneles · 7 áreas de impresión. G2 sin español, €, no latinos ni términos prohibidos (1.938 términos revisados, 1.633 valores); 282 formatos € reescritos. G3 Letter 38/38, pie 38, marca 7 (01-07 sin marca, como el catering) y versión 11; 45 ajustes · 51 altos. G4 723 glosario · 183 regenerar · 557 traducir · 6 citas de fichero · 17 de pestaña · 29 horas · 74 mensajes de DV. G5 15 denominaciones · 1 de cada = 204.91 · cierre 4,200 / over-short 0. G6 141 con valor (50 contadores). G7 59 °F y 14 citas normativas, todas en `REGLAS_US`; 25 celdas ES con °C, 1 `CELSIUS_SIN_F` (08 B19). G8 censo + no-latinos OK |
| Autotest | **19/19 CAZADOS**: los 16 del base + término prohibido + las 2 de la CF de excepción (D7). Sin «valor fijado»: `VALORES_EN` vacío (no hay inventario con mínimos). La cita: `CITA_AUTOTEST` = 3-501.18 |
| censo-entregables · no-latinos | 0 defectos (`--fail`) · 11 ficheros, 0 con no latinos |
| Celdas cortadas | 0 nuevas; 1 heredada («Denomination», 09); 55 del ES arregladas en la EN |
| Hermanos | `aplicar_en.py` y `mapas.py` intactos. `gates_en.py` de la rama frente al de `origin/main` (`41fdfb9f`) en los 7 publicados: **salida idéntica** (0 diferencias en gates y en autotest). Base, bar y catering: dry-run = publicado (0 diferencias en los volcados: 4.227 · 3.352 · 2.695 líneas), VERDE 8/0, autotest 16 / 16 / 20 OK. **Cafetería, pizzería, hamburguesería y ghost kitchen: ROJO ya en `main`, ajeno a esta rama** (abajo) |
| Copia al Mac | `scp` de los 11 xlsx a `astro-site/public/dl/ice-cream-shop-checklist-templates/` y de los 2 volcados: sha256 13/13 iguales |
| Volcados | `revision/dump_en.txt` y `dump_es.txt`, 2.510 líneas cada uno |

**Aviso (fuera del alcance de la F2, no tocado):** `adf52a52` (18-oct, «mínimos del Inventario Diario como NÚMERO» en los ES de cafetería, dark kitchen, hamburguesería y pizzería) cambió el ES después de publicar esas cuatro EN. Desde entonces su dry-run aborta («05 Inventario Diario!D6: el ES trae 2, no lo esperado») y sus gates salen ROJO (36-43 fallos, todos de G4 `valor fijado` en el 05 «Daily Inventory»: el ES trae `2` y `VALORES_EN` espera `'2'`), con el `gates_en.py` de `main` igual que con el de la rama. Los xlsx EN publicados no cambian; falta adaptar la comprobación de `VALORES_EN` (o sus claves) al ES numérico en esos cuatro `mapas_<v>.py`.

### Cifras para la landing (F3)

| Fichero | Hojas (sin Instructions) | Tareas |
|---|---|---|
| 01 Opening & Closing | Opening 26 · Closing 17 | 43 |
| 02 Production | Pasteurizing 13 · Batch Freezing 14 (+ tabla de vida útil, 6 familias) | 27 |
| 03 Manager | Daily 13 · Weekly 11 · Monthly 14 | 38 |
| 04 Duties by Role | Ice Cream Maker 14 · Scooper & Counter 14 · Shift Lead 13 | 41 |
| 05 Cleaning & Maintenance | Weekly Deep Clean 12 · Weekly Upkeep & Stock 8 · Monthly 12 · Quarterly & Annual 12 | 44 |
| 06 Seasonal & Catering | Peak Season 11 · Off-Season 9 · Ice Cream Catering 16 | 36 |
| 07 Blank Template | By Area · By Shift · By Role (en blanco) | 0 |
| 08 Whole Shop | Shop Opening 18 (10:00-10:30 AM) · Shop Closing 15 | 33 |
| 09 Cash Drawer | Opening 11 · Closing 12 · Monthly Cash Log | 23 |
| B01 Pre-Shift Huddle | Pre-Shift Huddle 13 | 13 |
| B02 Seasonal Calendar | 12 meses (acciones, sabores y temporada Peak / Shoulder / Low) | 0 |
| **Total** | **38 hojas** (11 de Instructions) | **298** |

Calendario (B02): Valentine's (14 feb) · St. Patrick's (17 mar) + Opening Day · Easter · Mother's Day (2.º domingo de
mayo) + graduaciones + Memorial Day (inicio del pico) · Father's Day + Juneteenth (19 jun) · National Ice Cream Month y
National Ice Cream Day (3.er domingo de julio) + 4 de julio · county fairs y vuelta al cole · Labor Day · Halloween ·
Thanksgiving + Black Friday / Small Business Saturday · holidays (Christmas, New Year's Eve). Sin inventario con mínimos.

## Para la revisión adversarial (UNA, sobre los volcados: lente de un dueño de scoop shop de EE. UU. + lente técnica)

- **08 «Shop Closing»** (D10, reordenado): las vitrinas tapadas «stay ON, in storage mode» (B9) y la lectura de cierre
  «dipping cabinets already in storage mode (0 °F)» (B10): ¿es real un modo nocturno a 0 °F en las dipping cabinets, o
  hay que dejarlo en «según el fabricante»? Y «gas off» en B13 de una heladería.
- **08 «Shop Opening»**: horas +3 h (10:00-10:30 AM, puerta a las 11:00 AM); B20 «switched to service mode» y B21 a
  6–10 °F. El 09 con las mismas +3 h.
- **02**: pasteurización 185 °F 15 s y la nota de licencia estatal en «Instructions» B6; enfriado de la mezcla 135 → 70 →
  41 °F (3-501.14); aging 36–39 °F; draw temperature 16–19 / 10–14 °F; tabla de vida útil en °F.
- **Scoop y alérgenos**: dipper well de agua corriente (3-304.12(D)), los 9 alérgenos US, sin mano desnuda (3-301.11),
  catar con cuchara limpia (3-301.12); pints preenvasados con etiqueta (3-602.11).
- **05 «Quarterly & Annual»**: NFPA 96 solo si se cocina con grasa, EPA 608, backflow, health permit + licencia de frozen
  dessert, CFPM; y c0332 (backflush de espresso) en «Weekly Upkeep & Stock».
- **06 «Peak Season»**: menores de 14-15 años (29 CFR 570.35 / 570.34) y work permits; catering con hielo seco y
  llegada ≤ 10 °F.
- **B02**: calendario US (pico de Memorial Day a Labor Day; mayo en Shoulder; Easter «date varies»).
- **G7 sin recalentado**: si la revisión pide algo de caliente (hot fudge, chocolate caliente), «hot fudge in its warmer
  per the manufacturer» (01 B28) ya no lleva cifra; si alguien añade 165 °F, G7 lo para.
- **Código común**: `gates_en.py` solo cambia cómo el autotest busca los libros (por prefijo); `aplicar_en.py` y
  `mapas.py` intactos.
