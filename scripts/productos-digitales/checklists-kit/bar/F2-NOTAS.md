# Bar Checklists Kit Pro — F2: construcción real (18-oct-2026 · sesión Claude Code)

Todo el python en el VPS (`/root/wt-bar`, venv `/root/venv-guias`). Textos: `textos_en/heredado.json` (121) +
`textos_en/G1.json` (488, traductor sonnet, commit `e6616089`) = las 609 cadenas a traducir; GM 244 por `mapas_bar.py`.
Decisiones aprobadas para la traducción: fichajes FLSA con «some states require more»; «Open patio season: patio at
full capacity»; espresso en ml y «9 bar»; sulfitos fuera de los 9 alérgenos.

## Comandos (en `scripts/productos-digitales/checklists-kit/`)

    python3 bar/mapas_bar.py                                            # 0 errores (autotest + censo + cruce con el base)
    python3 aplicar_en.py --kit bar --idempotencia --mes October       # → astro-site/public/dl/bar-checklist-templates/
    python3 gates_en.py --kit bar --mes October
    python3 gates_en.py --kit bar --mes October --autotest
    python3 ../censo-entregables.py --only bar-checklist-templates --fail
    python3 ../gate-no-latinos.py --only bar-checklist-templates
    python3 volcar_xlsx.py --kit bar <dl/bar-checklist-templates> bar/revision/dump_en.txt --orden en
    python3 volcar_xlsx.py --kit bar <dl/kit-tareas-bar> bar/revision/dump_es.txt --orden es

## Resultados

| Paso | Resultado |
|---|---|
| Montaje | 11 xlsx (nombres de `SPEC.md` §2), idempotencia 0 diferencias, `inject_cache` sin fallos (147 fórmulas con caché) |
| Gates | **VERDE 8/0**: G1 41 hojas · 147 fórmulas (15 por celda) · 29 DV · 30 CF · 248 merges · 30 protegidas · 342 tareas · 4.640 desbloqueadas · 2 definedNames con apóstrofo («New Year's Eve»); G2 sin español, € ni no latinos; G3 Letter, pie, marca y versión en 41/11; G4 1.195 glosario · 179 regenerar · 803 traducir · 36 citas de fichero · 19 de pestaña · 152 horas; G5 caja 204.91 / 4,200 / 0; G6 147/147; G7 12 °F y 3 citas, todas en §3 |
| Autotest | 16/16 defectos inyectados CAZADOS |
| censo-entregables | OK, 0 defectos (`--fail`) |
| gate-no-latinos | 11 ficheros, 0 con no latinos |
| Kit base | dry-run idéntico al de antes de generalizar (0 diferencias en los 11 xlsx); gates del base idénticos (VERDE 8/0) |
| Copia al Mac | `scp` de los 11 xlsx a `astro-site/public/dl/bar-checklist-templates/`: sha256 11/11 iguales |
| Volcados | `revision/dump_en.txt` y `dump_es.txt`, 3.352 líneas cada uno (para la revisión adversarial) |

«restaurant» solo aparece en la firma de autor (11, literal de la SPEC base §7.2); ni «cava» ni «grapes» en el EN.
## Ronda 1 de la revisión (`revision/REVISION-F2.md`: 0 bloqueantes · 6 MAYORES · 16 menores · 6 dudas)

Aplicados los 6 MAYORES y los 16 menores, solo con texto: G1.json pasa a 483 ids (+c0598; −6 que ahora fija
`POR_CELDA`), y `mapas_bar.py` gana `Vida útil` = «Shelf life», filas 9/10 y 21 del B02, `POR_CELDA` del 02 `E4` y del
08 16-19, 7 ADAPTAR y 3 reglas. Detalle en la tabla final de `REVISION-F2.md`. Comandos, además de los de arriba:
`extraer_textos.py --kit bar` + `heredar.py --kit bar` (118 heredadas + 483 pendientes = 601).

| Paso | Resultado |
|---|---|
| Montaje real | idempotencia 0 diferencias, `inject_cache` 11/11 sin fallos |
| Gates | **VERDE 8/0** (G4: 196 regenerar · 795 traducir · 1.186 glosario; G7: 12 °F, 4 citas) |
| Autotest · censo · no-latinos | 16/16 · 0 defectos · 0 |
| Kit base | dry-run 0 diferencias y gates idénticos |
| Copia al Mac | sha256 11/11 xlsx y 6/6 ficheros de datos; `dump_en.txt` regenerado (3.352 líneas) |

Código compartido tocado en la ronda: solo `heredar.py` (admite `mapas.NO_HEREDAR`); ni `mapas.py` ni `aplicar_en.py`
ni `gates_en.py`.
