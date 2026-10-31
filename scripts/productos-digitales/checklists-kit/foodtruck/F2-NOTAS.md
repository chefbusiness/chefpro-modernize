# Food Truck Checklists Kit Pro — F2: traducción, ganchos del molde plano y montaje (31-oct-2026 · sesión Claude Code)

Python con xlsx, todo en el VPS (`/root/wt-kits`, venv `/root/venv-guias`). Textos: `textos_en/G1.json` (las 237
pendientes, traducidas en esta sesión; 0 heredadas) + GM 204 por `mapas_foodtruck.py`. Mes de los docProps: **October**.
Precio **$15** (decisión del orquestador para los tres kits planos, SPEC D3-D4). Alta en `PRODUCTOS_LETTER`
(`censo-entregables.py`) y `EXCLUIDOS` (`postprocess-transversal.py`).

## Ganchos del molde plano (`f35b7355`; todos con `mapas.MOLDE == 'plano'`, SPEC §0.1) — panadería y marisquería los reutilizan

- `extraer_textos.filas_tarea`: tarea = fila bajo `FILA_CABECERA` con texto en A y en B que no es banda fusionada; el
  censo cuenta **153** (141 + 12 meses del B02). `gates_en.tareas()` usa la misma regla en el molde plano.
- `aplicar_en`: `capa_titulo` no escribe en «Instrucciones» (el título va por `POR_CELDA` en `CELDA_TITULO`);
  `comprobar_titulo` lee `CELDA_TITULO` de la única hoja.
- `gates_en` G3: sin línea de versión (si aparece una, rojo), título interior en `CELDA_TITULO`, «versiones = n/a».
  G4: «firmas» y «horas» = n/a (el ES no trae firma ni horas). G5 y G6 con dato `n/a` → estado **N/A** (no «OK») y
  la línea final lo dice («N/A (sin nada que comprobar): G5, G6»).
- Autotest: hojas por índice 0 (sin «Instrucciones» delante), las mutaciones de texto de G2 / G7 en `CELDA_AUTOTEST`
  (01 B5; moneda en el 03 y «$» en el 02), fuera las de horas (0 horas en el censo) y la de contador de G6 (0
  fórmulas), y una nueva: título interior alterado (G3).

## Regresión (antes `55b1f417` → después `f35b7355`; `gates_en.py --kit <v> --mes October` sobre los `dl/` LIVE)

| Salida | Antes = después | Estado |
|---|---|---|
| base, bar, catering, chocolate, hotel, icecream, pastry, taco | idénticas byte a byte | VERDE 8/0 |
| pizza, burger, cafe, ghost | idénticas byte a byte | ROJO previo (32 · 28 · 34 · 32 fallos, deriva de G4 conocida; no se toca) |
| autotest base · hotel · taco | idénticas byte a byte | 16/16 · 19/19 · 16/16 |

**15 de 15 idénticas** (`/root/ft-reg/antes` y `/root/ft-reg/despues`, script `/root/ft_reg.sh`).

## Resultados del food truck

| Paso | Resultado |
|---|---|
| Montaje | 11 xlsx (nombres de SPEC §2), 82.953 bytes; idempotencia 0 diferencias; 0 fórmulas (inject_cache sin nada que hacer); 0 desbordes |
| Gates | **VERDE 8/0** (dry-run y publicado): G1 11 hojas · 7 DV (126 celdas) · 7 CF · 63 merges · 11 paneles · 11 títulos de impresión · 153 tareas · 0 protegidas; G2 905 piezas revisadas contra términos prohibidos; G3 81 altos de fila, 11 títulos interiores; G4 479 glosario · 69 regeneradas · 237 traducidas; **G5 y G6 N/A**; G7 18 °F y 40 citas, todas permitidas, 3 celdas ES con °C |
| Autotest | **14/14 CAZADOS** |
| censo-entregables · no-latinos · LIT255 | 0 defectos (`--fail`) · 11 ficheros, 0 no latinos · VERDE |
| Publicado | `astro-site/public/dl/food-truck-checklist-templates/`, `24f35098`; volcados `revision/dump_en.txt` y `dump_es.txt` (866 líneas cada uno) |

Arreglo de la F2: la línea de marca pasa a «AI Chef Pro · aichef.pro · Food Truck Checklists Kit Pro» (`f67adf64`): con
«—» G2 la leía como el sufijo ES «— Food Truck» (11 rojos). Ninguna traducción tocada tras el primer montaje.

## Lo que la F3 tiene que saber (landing, dashboard, email)

- **No prometer** lo que el molde plano no trae: contador de tareas («Tasks done: X of Y», N/A que no cuenta), hoja de
  instrucciones, protección de hojas (van **sin proteger**: todo editable), horas límite (el 01 trae **duración** por
  tarea), hoja de caja / cash count sheet, vitrina, firma o bio dentro del fichero, línea de versión.
- Sí: **141 tareas** en 8 checklists + plantilla en blanco + briefing pre-evento (15 campos) + calendario de 12 meses;
  desplegable ✓ / — / N/A con fila en verde en 7 hojas (01-04, 06-08; el 05 y el 09 no lo llevan); °F y FDA Food Code;
  commissary, agua potable / residual, propano, generador, extintores, DMV / CDL, permisos y eventos US; US Letter.
- Marca dentro de los ficheros: «AI Chef Pro» (A1) y la línea de marca; docProps `subject` «… · v1.1».
- `$15`, env `VITE_STRIPE_PAYMENT_LINK_FOOD_TRUCK_CHECKLISTS_KIT`, JWT `food-truck-checklist-templates-jwt`; UK solo en
  la FAQ (SPEC D-UK); Google Sheets solo si el test lo confirma.

Erratas del ES: las de `SPEC.md` §5 (cabeceras C3 / D3 del 02 y el 03, tildes, 63 °C, arqueo y vitrina prometidos, 05 y
09 sin desplegable, food cost < 25 %).

## Ronda de revisión de contenido (31-oct · sesión Claude Code; 0 bloqueantes)

Aplicado (`68694d7d` textos y mapas, `e6778f5c` remontaje y republicación): 01 B12 y 03 B7 — el 0 °F ya no se ata a
3-501.16: «41 °F or below (FDA Food Code 3-501.16); frozen food stays frozen (0 °F or below is the common target)» (y el
`_FRIO` de los ADAPTAR, igual); 06 C27 «When» = «Any time» (repetía la frecuencia «Weekly» de D27, `POR_CELDA`). Resultado:
**VERDE 8/0** (G5 y G6 N/A), autotest 14/14, idempotencia 0, censo-entregables / no-latinos / LIT255 en 0.
