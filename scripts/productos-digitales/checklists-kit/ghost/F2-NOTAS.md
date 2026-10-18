# Ghost Kitchen Checklists Kit Pro — F2: construcción real (18-oct-2026 · sesión Claude Code)

Todo el python en el VPS (`/root/wt-ghost`, rama en `d38772da` + los cambios de abajo, venv `/root/venv-guias`).
Textos: `textos_en/heredado.json` (203: 144 del base, 22 de la cafetería, 19 de la pizzería, 15 de la hamburguesería, 3
del bar) + `textos_en/G1.json` (362, traductor sonnet en `d38772da`) = las 565 cadenas a traducir; GM 290 por
`mapas_ghost.py` (239 `POR_CELDA`, 32 `VALORES_EN`). `heredar.py` tras el merge de la ronda 1 de la hamburguesería
(`318d23ae`, burger en `a345762f`): **0 cambios** (heredado.json y pendientes.json idénticos; nada nuevo que traducir).

## Dudas del traductor (resueltas en la fuente)

- c0343 (05 «Daily Inventory» A2) «☐ AM ☐ PM»: coherente, el ES trae dos turnos (Mañana / Noche).
- Coletilla «— log reading: ____ °F»: ninguna cadena del G1 la necesita. Las dos celdas ES con «anota la lectura» (01
  B16 y B15) van heredadas de la cafetería y de la hamburguesería y ya la llevan. G7 verde: todo °C del ES tiene su °F
  salvo las 4 `CELSIUS_SIN_F` del aceite.
- B02 c0810 (fila 11, warm weather), c0836 (20, Halloween), c0841 (22, frío y lluvia) y c0846 (24, office parties):
  cada tarea casa con su evento. Las 22 filas, cotejadas contra `CALENDARIO`: todas casan con su fila.
- c0319 / c0329 (04 «Operations Manager» B6 / B19): «Open the kitchen; disarm the alarm» (08:45, la primera) y «Close the
  kitchen» (22:30, la última): encajan con el orden del 08, que va fijado por filas en `POR_CELDA`.

## Cambios de esta pasada

- **Celdas cortadas** (`ancho_texto` / `n_lineas` de `aplicar_en`, sobre las 2.342 celdas de texto, EN contra ES):
  **0 nuevas**. Quedan 4, las mismas de los hermanos: «Verified by:» del 07 (×3) y «Denomination» del 09. Dos venían
  cortadas también en el ES y se arreglan en la EN:
  - 05 «Weekly FIFO Check» fila 34: necesitaba 27,2 pt y tenía 24,5 → `ALTOS_FILA` 27,5.
  - 01 «Kitchen Closing» B9: va sin ajuste en el ES, y su EN cita
    `05-cloud-kitchen-cleaning-checklist-inventory-maintenance.xlsx` (62 caracteres, más ancho que la columna B).
    `objetivo_ajuste` no actúa en ese caso, así que hay un gancho nuevo en `aplicar_en.capa_ajuste`:
    `mapas.AJUSTE_FORZADO` (ajuste de texto, la fila automática crece y Excel parte solo el nombre del fichero). Sin la
    constante no hace nada, así que los hermanos salen idénticos.
- **Título del 05**: aquí el ES cabe en una línea y `capa_ajuste` ya lo sube a 50,5, como en los otros 9 libros con
  título de dos líneas (el 07 cabe en una). La `ALTOS_FILA` de la fila 2 que traía la F1 era redundante: se quita.

## Comandos (en `scripts/productos-digitales/checklists-kit/`)

    python3 extraer_textos.py --kit ghost && python3 ghost/mapas_ghost.py && python3 heredar.py --kit ghost
    python3 aplicar_en.py --kit ghost --idempotencia --mes October     # → astro-site/public/dl/ghost-kitchen-checklist-templates/
    python3 gates_en.py --kit ghost --mes October [--autotest]
    python3 ../censo-entregables.py --only ghost-kitchen-checklist-templates --fail
    python3 ../gate-no-latinos.py --only ghost-kitchen-checklist-templates
    python3 volcar_xlsx.py --kit ghost <dl/ghost-kitchen-checklist-templates> ghost/revision/dump_en.txt --orden en
    python3 volcar_xlsx.py --kit ghost <dl/kit-tareas-dark-kitchen> ghost/revision/dump_es.txt --orden es

## Resultados

| Paso | Resultado |
|---|---|
| Montaje | 11 xlsx (nombres de `SPEC.md` §2); idempotencia 0 diferencias; `inject_cache` sin fallos; 0 desbordes; 0 rellenos |
| Gates | **VERDE 8/0**. G1 43 hojas · 179 fórmulas (15 por celda) · 29 DV · 30 CF · 264 merges · 31 protegidas · 4.251 desbloqueadas. G2 sin español, €, no latinos ni términos prohibidos (2.647 piezas). G3 Letter, pie, marca (42) y versión; 113 ajustes · 105 altos. G4 1.051 glosario · 291 regenerar · 787 traducir · 34 citas de fichero · 14 de pestaña · 148 horas · 32 valores fijados. G5 caja 204.91 / 4,200 / 0. G6 147 con valor + 32 vacías, como el ES. G7 46 °F y 40 citas, todas en `REGLAS_US`; 4 `CELSIUS_SIN_F` |
| Autotest | **18/18 CAZADOS**: los 16 del base, más término prohibido y valor fijado. La cita: `CITA_AUTOTEST` = 3-501.18 |
| censo-entregables · no-latinos | 0 defectos (`--fail`) · 11 ficheros, 0 con no latinos |
| Hermanos | dry-run con el código final (`AJUSTE_FORZADO` no existe en ellos) = lo publicado (burger = `a345762f`): 0 diferencias en los volcados (base 4.227 · bar 3.352 · cafe 4.515 · catering 2.695 · pizza 3.666 · burger 3.512 líneas), gates VERDE 8/0 y autotest 16 / 16 / 18 / 20 / 18 / 18 OK |
| Copia al Mac | `scp` de los 11 xlsx a `astro-site/public/dl/ghost-kitchen-checklist-templates/`: sha256 11/11 iguales |
| Volcados | `revision/dump_en.txt` y `dump_es.txt`, 3.387 líneas cada uno |

Siguiente: UNA revisión adversarial sobre los volcados, con dos lentes: un ghost kitchen manager de EE. UU. y una
técnica. Puntos a revisar:
- precintos (AB 3336) y alérgenos en las apps;
- pescado crudo: −4 °F 7 días, y el congelador a 0 °F no cuenta;
- arroz de sushi (3-502.11(D) / TPHC);
- caliente y frío separados hasta la recogida;
- el orden de la apertura y el cierre del 08, y el 07 sin sala ni barra;
- calendario US;
- mínimos del inventario en lb.
