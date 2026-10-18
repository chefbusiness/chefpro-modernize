# Pizza Shop Checklists Kit Pro — F2: construcción real (18-oct-2026 · sesión Claude Code)

Todo el python en el VPS (`/root/wt-pizza`, rama en `9f01e52a` + los cambios de abajo, venv `/root/venv-guias`). Textos:
`textos_en/heredado.json` (250: 197 del base, 50 de la cafetería, 3 del bar) + `textos_en/G1.json` (381, traductor
sonnet, commit `9f01e52a`) = las 631 cadenas a traducir; GM 278 por `mapas_pizza.py` (incluye los 32 `VALORES_EN` del
inventario). `heredar.py --kit pizza` sobre la rama: 0 cambios en heredado y pendientes (solo la marca de tiempo del censo).

## Cambios de esta pasada

- **Ajuste de texto (errata ES)**: las tareas largas del ES de la pizzería no llevan ajuste de texto (el base sí) y
  salen cortadas por la celda vecina también en el ES; `objetivo_ajuste` las dejaba como «maqueta heredada». Gancho
  nuevo `mapas.AJUSTE_MAQUETA_ES` (solo la pizzería): la EN activa el ajuste donde basta (palabra más larga dentro de
  la columna y una sola fila); las etiquetas de columna estrecha («Verified by:» del 07) se quedan como el ES. Filas de
  alto automático sin combinar: las ajusta Excel, como en el base. G3 usa la misma cuenta: 106 ajustes · 100 altos.
  Comprobación independiente (heurística de ancho × líneas sobre las 2.558 celdas de texto): 0 cortadas, 0 sin ajuste
  con vecina ocupada. Cubre las 74 celdas B que pasan del 115 % del ES; ninguna hubo que recortarla.
- `censo-entregables.py` (`PRODUCTOS_LETTER`) y `postprocess-transversal.py` (`EXCLUIDOS`): + el slug, como los
  hermanos (sin él, `noprint` en los 11: el kit EN es Letter).
- Citas de pestaña del traductor: «Monthly Maintenance» y «Quarterly & Annual» son pestañas del propio kit (barrido de
  las citas entre comillas del EN: 0 pestañas ajenas o inexistentes); G4: 14 citas de pestaña y 33 de fichero.

## Comandos (en `scripts/productos-digitales/checklists-kit/`)

    python3 extraer_textos.py --kit pizza && python3 pizza/mapas_pizza.py && python3 heredar.py --kit pizza
    python3 aplicar_en.py --kit pizza --idempotencia --mes October     # → astro-site/public/dl/pizza-shop-checklist-templates/
    python3 gates_en.py --kit pizza --mes October [--autotest]
    python3 ../censo-entregables.py --only pizza-shop-checklist-templates --fail
    python3 ../gate-no-latinos.py --only pizza-shop-checklist-templates
    python3 volcar_xlsx.py --kit pizza <dl/pizza-shop-checklist-templates> pizza/revision/dump_en.txt --orden en
    python3 volcar_xlsx.py --kit pizza <dl/kit-tareas-pizzeria> pizza/revision/dump_es.txt --orden es

## Resultados

| Paso | Resultado |
|---|---|
| Montaje | 11 xlsx (nombres de `SPEC.md` §2), idempotencia 0 diferencias, `inject_cache` sin fallos, 0 desbordes |
| Gates | **VERDE 8/0**: G1 46 hojas · 185 fórmulas (15 por celda) · 32 DV · 33 CF · 289 merges · 34 protegidas · 4.660 desbloqueadas; G2 sin español, €, no latinos ni términos prohibidos (2.884 piezas); G3 Letter, pie, marca (45) y versión, 106 ajustes · 100 altos; G4 1.178 glosario · 265 regenerar · 866 traducir · 33 citas de fichero · 14 de pestaña · 177 horas · 32 valores fijados; G5 caja 204.91 / 4,200 / 0; G6 153 con valor + 32 vacías como el ES; G7 33 °F y 33 citas, todas en `REGLAS_US` |
| Autotest | **18/18 CAZADOS** (los 16 del base + término prohibido + valor fijado; la cita, `CITA_AUTOTEST` = 3-501.18) |
| censo-entregables · no-latinos | 0 defectos (`--fail`) · 11 ficheros, 0 con no latinos |
| Hermanos | dry-run con el código final = lo publicado (base `origin/main`, bar `96432c18`, cafe `ac1d63f8`, catering `5726f66a`): 0 diferencias en los volcados (4.227 / 3.352 / 4.515 / 2.695 líneas), gates VERDE 8/0 y autotest 16 / 16 / 18 / 20 OK (`AJUSTE_MAQUETA_ES` no existe en ellos) |
| Copia al Mac | `scp` de los 11 xlsx a `astro-site/public/dl/pizza-shop-checklist-templates/`: sha256 11/11 iguales |
| Volcados | `revision/dump_en.txt` y `dump_es.txt`, 3.666 líneas cada uno |

Siguiente: UNA revisión adversarial sobre los volcados (lente de un pizza shop manager US + lente técnica): horno de
leña (ceniza, campana, NFPA 96), masa en frío, make line, mozzarella, delivery (bolsas, propinas, seguro), el orden de
los cierres 01 «FOH Closing» y 08, el calendario US y los mínimos del inventario en lb / oz.
