# Coffee Shop Checklists Kit Pro — F2: construcción real (18-oct-2026 · sesión Claude Code)

Todo el python en el VPS (`/root/wt-cafe`, rama en `a81bf032`, venv `/root/venv-guias`). Textos:
`textos_en/heredado.json` (229: 225 del base y 4 del bar) + `textos_en/G1.json` (617, traductor sonnet, commit
`a81bf032`) = las 846 cadenas a traducir; GM 262 por `mapas_cafe.py` (incluye los 34 `VALORES_EN` del inventario).
`heredar.py --kit cafe` tras fusionar la ronda 1 del bar (`96432c18`, `NO_HEREDAR`): 0 cambios en heredado/pendientes.
Decisiones del traductor aprobadas: cabeceras del inventario, hazelnut, «Final dish area» (04 «Auxiliar» B17).

## Comandos (en `scripts/productos-digitales/checklists-kit/`)

    python3 cafe/mapas_cafe.py                                          # 0 errores
    python3 aplicar_en.py --kit cafe --idempotencia --mes October      # → astro-site/public/dl/coffee-shop-checklist-templates/
    python3 gates_en.py --kit cafe --mes October [--autotest]
    python3 ../censo-entregables.py --only coffee-shop-checklist-templates --fail
    python3 ../gate-no-latinos.py --only coffee-shop-checklist-templates
    python3 volcar_xlsx.py --kit cafe <dl/coffee-shop-checklist-templates> cafe/revision/dump_en.txt --orden en
    python3 volcar_xlsx.py --kit cafe <dl/kit-tareas-cafeteria> cafe/revision/dump_es.txt --orden es

## Resultados

| Paso | Resultado |
|---|---|
| Montaje | 11 xlsx (nombres de `SPEC.md` §2), idempotencia 0 diferencias, `inject_cache` sin fallos |
| Gates | **VERDE 8/0**: G1 49 hojas · 235 fórmulas (15 por celda) · 34 DV · 35 CF · 328 merges · 36 protegidas · 5.636 desbloqueadas; G2 sin español, € ni no latinos; G3 Letter, pie, marca (47 + 2 sueltas del inventario) y versión; G4 1.563 glosario · 205 regenerar · 1.099 traducir · 33 citas de fichero · 12 de pestaña · 274 horas · **34 valores fijados**; G5 caja 204.91 / 4,200 / 0; G6 158 con valor + 77 vacías como el ES; G7 22 °F y 5 citas, todas en `SPEC.md` §3 |
| Autotest | 17/17 defectos inyectados CAZADOS (16 del base + el valor fijado del inventario) |
| censo-entregables | OK, 0 defectos (`--fail`) |
| gate-no-latinos | 11 ficheros, 0 con no latinos |
| Base y bar | dry-run = lo publicado en la rama (base = `origin/main`; bar = `96432c18`): 0 diferencias en los volcados (4.227 y 3.352 líneas) y los mismos gates (VERDE 8/0) |
| Copia al Mac | `scp` de los 11 xlsx a `astro-site/public/dl/coffee-shop-checklist-templates/`: sha256 11/11 iguales |
| Volcados | `revision/dump_en.txt` y `dump_es.txt`, 4.515 líneas cada uno |

«restaurant» solo aparece en la firma de autor (11, literal de la SPEC base §7.2); ni «café» con tilde, ni «cava», ni
«shift manager», ni «venue» en el EN. Siguiente: UNA revisión adversarial sobre los volcados (lente de un coffee shop
manager US + lente técnica), sobre todo el delta de `SPEC.md` §1 y §3, las 10 celdas con °C, el calendario y los
mínimos del inventario en lb / oz / qt.
