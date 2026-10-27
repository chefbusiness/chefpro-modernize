# Hotel Checklists Kit Pro — F2: montaje y gates (27-oct-2026 · sesión Claude Code)

Todo el python en el VPS (`/root/wt-hotel`, venv `/root/venv-guias`). Textos: `textos_en/heredado.json` (107) +
`textos_en/G1.json` (831, ya con G1 y G2) = las 938 cadenas a traducir; GM 298 por `mapas_hotel.py` (194 `POR_CELDA`,
29 horas). `heredar.py --kit hotel`: 107 heredadas, 831 pendientes (igual que F1). `extraer_textos` solo reescribe la
fecha en `censo_es.json` / `textos_es.json` (revertidos). Alta en `PRODUCTOS_LETTER` (`censo-entregables.py`) y
`EXCLUIDOS` (`postprocess-transversal.py`). **Código común intacto** (`kit.py`, `gates_en.py`, `aplicar_en.py`,
`mapas.py` sin cambios) → no hace falta repetir la regresión de los 10 kits. Ninguna traducción ni `mapas_hotel.py`
tocados: los gates salieron verdes a la primera (las comillas de «N/A», «—», «Notes», «Frequency» y
«No Lifeguard on Duty» no las marca ningún gate).

## Comandos (en `scripts/productos-digitales/checklists-kit/`)

    python3 extraer_textos.py --kit hotel && python3 hotel/mapas_hotel.py && python3 heredar.py --kit hotel
    python3 aplicar_en.py --kit hotel --dry-run --idempotencia --mes October --salida <tmp>
    python3 aplicar_en.py --kit hotel --idempotencia --mes October     # → astro-site/public/dl/hotel-checklist-templates/
    python3 gates_en.py --kit hotel --mes October [--autotest]
    python3 ../censo-entregables.py --only hotel-checklist-templates --fail
    python3 volcar_xlsx.py --kit hotel ../../../astro-site/public/dl/hotel-checklist-templates hotel/revision/dump_en.txt --orden en
    python3 volcar_xlsx.py --kit hotel ../../../astro-site/public/dl/kit-tareas-hotel hotel/revision/dump_es.txt --orden es

## Resultados

| Paso | Resultado |
|---|---|
| Montaje | 19 xlsx (nombres de `SPEC.md` §2; el rótulo «11 xlsx» de `aplicar_en` es solo texto); idempotencia 0 diferencias; `inject_cache` sin fallos de pycel (19/19; 197 fórmulas, todas con valor); 0 desbordes; 0 rellenos |
| Gates | **VERDE 8/0**. G1 74 hojas · 197 fórmulas (15 por celda, 1 con hoja) · 54 DV (671 celdas) · 55 CF (27 por celda) · 345 merges · 5 protegidas · 811 desbloqueadas · 62 nombres · 55 paneles · 7 áreas de impresión. G2 sin español, €, no latinos ni términos prohibidos (3.505 términos, 2.909 valores); 282 formatos € reescritos. G3 74 hojas, 74 pies, marca 7, versión 19, 70 ajustes · 85 altos. G4 1.343 glosario · 239 regenerar · 1.059 traducir · 6 citas de fichero · 21 de pestaña · 29 horas · 156 mensajes de DV. G5 15 denominaciones · 1 de cada = 204.91 · cierre 4,200 / over-short 0. G6 197 con valor (106 contadores). G7 48 °F y 42 citas normativas (79 permitidas); 23 celdas ES con °C. G8 censo + no-latinos OK |
| Autotest | **19/19 CAZADOS** |
| censo-entregables · no-latinos | 0 defectos (`--fail`) · 19 ficheros, 0 con no latinos |
| Copia al Mac | `scp` de los 19 xlsx y de los 2 volcados; hash agregado sha256 idéntico VPS ↔ Mac |
| Volcados | `revision/dump_en.txt` y `dump_es.txt`, 4.391 líneas cada uno |
| Tamaño | 19 xlsx = 296 KB en disco (258.900 bytes) |
