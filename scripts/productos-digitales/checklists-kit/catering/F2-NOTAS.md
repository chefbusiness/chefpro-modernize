# Catering Checklists Kit Pro — F2: construcción real (18-oct-2026 · sesión Claude Code)

Todo el python en el VPS (`/root/wt-catering`, rama en `810e54c9` + los cambios de abajo, venv `/root/venv-guias`).
Textos: `textos_en/heredado.json` (41, todas del base) + `textos_en/G1.json` (526, traductor sonnet, commit `810e54c9`)
= las 567 cadenas a traducir; GM 229 por `mapas_catering.py`. `heredar.py --kit catering` tras fusionar la ronda 1 de
la cafetería (`aa3229a5`): 0 cambios en heredado y en pendientes, salvo la cita de c0645 (abajo).

## Dudas del traductor (decididas)

- c0645 (09 «Event Settlement» D24): cita los ESTADOS de la columna «Status», así que «Pendiente» → "Pending" (`CLAVES`),
  no "Balance due" (que es la columna de importe H5 del registro). Arreglado en origen: `GLOSARIO['Pendiente']` =
  el estado (la H5 sigue en «Balance due» por `POR_CELDA`, que manda en su celda), `cita_rotulos` regenerada y el EN
  de c0645 corregido en `G1.json` (solo esa cadena).
- c0212 (cita a «HACCP Food Safety Kit Pro») se queda · c0350 «68–72 °F» sin °C se queda.
- Añadidos de esta pasada: `TERMINOS_PROHIBIDOS` del catering (restaurant salvo «restaurant consultant», host stand,
  sous chef, FOH / shift manager, coffee shop, cafe, barista, tip jar, line-up) → G2 los vigila y el autotest suma
  uno (18). El G1.json no traía ninguno.

## Comandos (en `scripts/productos-digitales/checklists-kit/`)

    python3 extraer_textos.py --kit catering && python3 catering/mapas_catering.py && python3 heredar.py --kit catering
    python3 aplicar_en.py --kit catering --idempotencia --mes October     # → astro-site/public/dl/catering-checklist-templates/
    python3 gates_en.py --kit catering --mes October [--autotest]
    python3 ../censo-entregables.py --only catering-checklist-templates --fail
    python3 ../gate-no-latinos.py --only catering-checklist-templates
    python3 volcar_xlsx.py --kit catering <dl/catering-checklist-templates> catering/revision/dump_en.txt --orden en
    python3 volcar_xlsx.py --kit catering <dl/kit-tareas-catering> catering/revision/dump_es.txt --orden es

## Resultados

| Paso | Resultado |
|---|---|
| Montaje | 11 xlsx (nombres de `SPEC.md` §2), idempotencia 0 diferencias, `inject_cache` sin fallos |
| Gates | **VERDE 8/0**: G1 36 hojas · 144 fórmulas (17 por celda; 1 con hoja: C15 lee el tipo del «Event Billing Log») · 22 DV · 26 CF · 196 merges · 6 protegidas · 810 desbloqueadas · 369 tareas; G2 sin español, €, no latinos ni términos prohibidos (2.017 piezas), 159 formatos € y 52 fechas reescritos; G3 Letter, pie, marca (8, solo 08 y 09) y versión; G4 816 glosario · 161 regenerar · 629 traducir · 9 citas de fichero · 24 de pestaña · 18 horas · 1 valor fijado; G5 15 denominaciones + 4 casos del 09 (22 comprobaciones); G6 117 con valor + 27 vacías como el ES; G7 51 °F y 21 citas, todas en `REGLAS_US` |
| Autotest | **18/18 CAZADOS** (los 16 del base + término prohibido + valor fijado); el de cita usa `CITA_AUTOTEST` = 3-501.18 (no está en `REGLAS_US`; el 3-501.19 sí), revisado tras la resolución del conflicto de `_cita_mal` |
| censo-entregables | OK, 0 defectos (`--fail`) |
| gate-no-latinos | 11 ficheros, 0 con no latinos |
| Base, bar y cafetería | dry-run con el código final = sus ramas (base `origin/main`, bar `96432c18`, cafe `ac1d63f8`): 0 diferencias en los volcados (4.227 / 3.352 / 4.515 líneas) y gates VERDE 8/0 |
| Copia al Mac | `scp` de los 11 xlsx a `astro-site/public/dl/catering-checklist-templates/`: sha256 11/11 iguales |
| Volcados | `revision/dump_en.txt` y `dump_es.txt`, 2.695 líneas cada uno |

«restaurant» solo aparece en la firma de autor (11, literal de la SPEC base §7.2). Siguiente: UNA revisión adversarial
sobre los volcados (lente de un catering manager US + lente técnica), sobre todo el 09 (sales tax con el tipo en C3 a 0
por defecto, service charge ≠ gratuity, estados), el calendario US, el orden del cierre del 08 y las 17 celdas con °C.
