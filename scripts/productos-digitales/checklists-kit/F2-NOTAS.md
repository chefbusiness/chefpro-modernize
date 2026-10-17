# Restaurant Checklists Kit Pro — F2 (entregables) · notas de cierre

> Sesión Claude Code, 17-oct-2026. SPEC §7 pasos 3-5 y §8 (G1-G8). Implementador único (tamaño S).
> Entradas: `textos_en/G1.json` (429) y `G2.json` (345), escritos por subagentes sonnet (regla 1bis); `mapas.py`,
> `censo_es.json` y `textos_es.json`. Fuente ES en solo lectura: `astro-site/public/dl/kit-tareas/` (sin cambios).
> Construido y verificado en el **VPS** (worktree `/root/wt-checklists`, venv `/root/venv-guias`, openpyxl 3.1.5),
> no en el Mac en serie como decía D22: el VPS volvió. Los xlsx han vuelto al Mac por `scp` con sha256 idénticos.

## 1. Qué se ha construido

| Pieza | Qué es |
|---|---|
| `aplicar_en.py` | Copia adaptada de `staff-kit/aplicar_en.py`. Hace, en orden: renombrado de hojas y de la única referencia a otra hoja (09 `C48` → `'Cash Drawer Opening'!C23`); las 15 `FORMULAS_POR_CELDA` (D12) y el resto por HOJAS + CLAVES; textos **por aparición** (traducir → `textos_en`; mapa-glosario, mapa-hoja y mapa-clave → `mapas.py`); las 172 horas → `hora_us`; versión, marca y pie D19; DV y CF; título interior y `POR_CELDA`; comillas rectas; **capa de ajuste**; `FORMATOS_EN` (y formatos propios con € sin uso, renombrados); US Letter; docProps; nombre EN. **Cobertura**: toda aparición «regenerar» tiene que escribirla una capa con su valor esperado, o el script aborta. `inject_cache` va AL FINAL. Modos: `--dry-run [--salida]`, `--parcial` (marca `PENDING-EN cNNNN`), `--textos DIR`, `--idempotencia`, `--mes`, `--json`, `--sin-cache` |
| `gates_en.py` | G1-G8 de SPEC §8 contra `censo_es.json`, los xlsx ES y `mapas.py`; `--parcial` tolera la marca de relleno. `--autotest`: 16 defectos inyectados en copias (G1 ×3, G2 ×4, G3 ×3, G4 ×2, G5, G6, G7 ×2), y los 16 se cazan |
| `volcar_xlsx.py` | Volcado legible (celda → valor, fórmula + caché, DV, CF, impresión, docProps), mismo formato para ES y EN → `revision/dump_en.txt` y `revision/dump_es.txt` (4.227 líneas cada uno) |
| `astro-site/public/dl/restaurant-checklist-templates/` | Los 11 xlsx EN con los nombres de SPEC §2.1 (≈ 216 KB) |
| `postprocess-transversal.py` | `restaurant-checklist-templates` en `EXCLUIDOS` (un `all` le forzaría A4 y español) |
| `censo-entregables.py` | `restaurant-checklist-templates` en `PRODUCTOS_LETTER` (exige Letter; «Instructions» es la hoja de texto) |
| `textos_en/G2.json` · `mapas.py` · `textos_es.json` | c0757 «sidewalk café permit» → «sidewalk **cafe** permit» (grafía de los permisos US, decisión del orquestador). En `mapas.py` y `textos_es.json` solo cambia el texto `ADAPTAR` de esa pista, que no se escribe en ningún xlsx. G2 ya no admite «café» como palabra inglesa |

## 2. Cómo regenerar (en el VPS; en el Mac, solo en serie y con `istats` < 62 °C)

```bash
ssh vps
cd /root/chefpro-modernize && git fetch origin && git worktree add /root/wt-checklists origin/<rama>   # si no existe
cd /root/wt-checklists/scripts/productos-digitales/checklists-kit
PY=/root/venv-guias/bin/python
$PY mapas.py && $PY gate_f1.py                                     # 0 errores · VERDE
$PY aplicar_en.py --dry-run --salida /tmp/ck-dry --mes October     # ensayo (opcional)
$PY gates_en.py --dir /tmp/ck-dry --mes October
$PY aplicar_en.py --idempotencia --mes October                     # real: dl/restaurant-checklist-templates/ (inject_cache dentro)
$PY gates_en.py --mes October && $PY gates_en.py --mes October --autotest
cd /root/wt-checklists && $PY scripts/productos-digitales/censo-entregables.py --only restaurant-checklist-templates --fail
$PY scripts/productos-digitales/gate-no-latinos.py --only restaurant-checklist-templates
cd scripts/productos-digitales/checklists-kit && mkdir -p revision
$PY volcar_xlsx.py /root/wt-checklists/astro-site/public/dl/restaurant-checklist-templates revision/dump_en.txt --orden en
$PY volcar_xlsx.py /root/wt-checklists/astro-site/public/dl/kit-tareas revision/dump_es.txt --orden es
# vuelta: scp 'vps:/root/wt-checklists/astro-site/public/dl/restaurant-checklist-templates/*.xlsx' <worktree Mac>/astro-site/public/dl/restaurant-checklist-templates/
# y comparar `sha256sum` (VPS) con `shasum -a 256` (Mac)
```

- **`/dev/null` en el VPS**: no se puede usar como destino de una redirección; redirigir siempre a ficheros de `/tmp`.
- **Caché**: no guardar los xlsx con openpyxl después de `inject_cache`, porque borraría la caché.
- **`--mes`**: la línea de versión lleva el mes de la construcción («Version 2.0 · October 2026 · aichef.pro/en/digital-products/restaurant-checklist-templates · info@aichef.pro»). Si F3 publica en otro mes, se reconstruye con `--mes` y los gates se pasan con el mismo `--mes`.
- **Ensayo sin traducciones**: `--dry-run --parcial --textos <carpeta vacía>`, y los gates con `--parcial --textos <la misma>`.
- **Tiempos en el VPS**: construcción ~9 s con idempotencia e `inject_cache`; gates ~15 s; autotest ~40 s.

## 3. Resultados (construcción real tras la ronda 1, 17-oct, `--mes October`)

| Gate | Estado | Detalle |
|---|---|---|
| **G1 paridad** | OK | 47 hojas; 157 fórmulas = ES salvo las 15 por celda (D12); 1 fórmula con hoja; 34 DV (719 celdas); 35 CF; 308 merges; 36 protegidas sin contraseña, mismos flags; 47 áreas y 35 títulos de impresión; 82 definedNames crudos (los 2 de `'Valentine''s Day'!` incluidos); 35 paneles; 276 anchos iguales; 4.286 verdes y 5.995 desbloqueadas celda a celda; 491 tareas en sus filas; 0 gráficos e imágenes |
| **G2 restos** | OK | 3.054 valores, 68 mensajes de DV, 99 ítems, 77 docProps, 47 pies, 297 formatos: 0 español, 0 €, 0 no latinos, 0 comillas curvas, 0 horas de 24 h, 0 nombres de fichero ES. `$`/`¢` en 16 celdas: los 15 rótulos de billetes + 09 Instructions!B14 (lo pide `ADAPTAR`). 282 formatos con € reescritos |
| **G3 formato** | OK | Letter 47/47; pie 47; marca 47; versión 11; docProps y `Instructions!B2` D5 en los 11; ajuste de texto en 1 celda (01 «FOH Closing» A21) y alto de fila suficiente en 80 celdas; ninguna fila baja de alto; 0 desbordes |
| **G4 mapas** | OK | 984 apariciones traducir, 1.680 de glosario, 1 de hoja y 212 de regenerar = su EN; 68 mensajes de DV; 172 horas = `hora_us`; 14 citas de rótulos y 37 de ficheros con su EN exacto; firma de autor literal |
| **G5 caja** | OK | A27:A42 y C27:C42 = `DENOMINACIONES`. Caso de §5: 1 unidad de cada → 204.91. Cierre con 200 / 1,250 / 3,000 / 150 / Z 4,200 → TOTAL COLLECTED 4,200 y OVER / SHORT 0, igual en «Monthly Cash Log» F5/H5 |
| **G6 cálculo** | OK | `<v>` en las 157 fórmulas, 0 errores; caché EN = caché ES (66 contadores) |
| **G7 reglas** | OK | 21 °F, todos ∈ {−31, −4, 0, 10, 32, 41, 70, 100, 135, 165} (= cifras de `mapas.py`); 10 citas normativas ∈ las 44 de las fuentes de `REGLAS_US`; 12 de las 13 celdas ES con °C llevan °F, y la que falta (02 «Hot Line» B27, el aceite) está declarada sin cifra en `mapas.CELSIUS_SIN_F` |
| **G8** | OK | `censo-entregables --only restaurant-checklist-templates --fail`: 0 defectos. `gate-no-latinos`: 11 ficheros, 0 caracteres |

**Totales**: VERDE, 8 gates, 0 fallos · autotest 16/16 cazado · idempotencia 0 diferencias · `inject_cache` `fallos_pycel=0` en los 11 · `mapas.py` 0 errores · `gate_f1` VERDE · sha256 VPS = Mac en los 11.

## 4. Desviaciones de la SPEC (aprobadas por el orquestador)

1. **`$`/`¢` (G2)**: además de A27:A42, se admiten en las celdas cuyo `mapas.ADAPTAR` los pide (09 Instructions!B14: «25¢ roll» = $10, «10¢ roll» = $5). La zona sale de `mapas.py`; no está fijada a mano.
2. **Ajuste de texto y alto de fila**: lo decide una regla automática (`aplicar_en.objetivo_ajuste`, la misma cuenta en G3), no una lista a mano como `AJUSTE_TEXTO` en el staff-kit.
   - Solo actúa donde el ES cabía y el EN no. Nunca toca anchos y nunca baja un alto.
   - Alto = líneas EN × 1.36 × cuerpo + el aire del ES (hasta 6 pt). La estimación es conservadora (1 carácter por unidad de ancho a 11 pt): sobra aire, no se corta.
   - Lo heredado se queda como en el ES: «Verified by:» en la columna A, de ancho 5, junto a B:D combinadas.
3. **Defecto heredado arreglado**: una celda combinada de alto automático no la ajusta Excel. Es el caso de 09 «Monthly Cash Log» A37, que en el ES salía cortado; en el EN lleva alto explícito (36.75).
4. **G4 y G7 amplían §8**: G4 comprueba las citas de rótulos y ficheros y la firma literal; G7 exige °F donde el ES tenía °C («____ °F» cuenta).

## 5. Ronda 1 de correcciones (revisión adversarial, `revision/REVISION-F2.md`)

- **Revisión**: 0 bloqueantes, 4 MAYOR, 16 menor y 6 dudas.
- **Qué se aplicó**: M1, M2, M4 y M3 en parte; 15 de los 16 menores; D1 con la regla neutra del aceite. La tabla
  completa, con lo no aplicado y por qué, está al final de `REVISION-F2.md`.
- **Dónde**: solo textos. 27 cadenas de `textos_en/`; en `mapas.py`, `POR_CELDA` (A49, A53, G4, 03 B16, 02 B10 ×2),
  `CALENDARIO` (6, 19), `ADAPTAR` (01 B10, 02 B27, 03 B18, 09 B15, A37), `REGLAS_US` (+frecuencia_pago, enfriamiento,
  recalentado, sanitizante, aviso_consumidor; fichajes con NY) y `CELSIUS_SIN_F`.
- **`textos_es.json` regenerado** con `extraer_textos.py`: ids y censo iguales; solo cambian `adaptar` y
  `en_por_celda`.
- **SPEC**: §3 (+5 filas), D12 (la Z del POS) y §8 G7 (+70, +165, −104).
- **G2** ya no admite «café» como palabra inglesa: c0757 dice «sidewalk cafe permit».
- **No aplicado**:
  - el recalentado a 165 °F, porque c0246 es mantenimiento en caliente, no recalentado;
  - las tiras en c0091, porque esa fila trata de los trapos;
  - E7 «Quarterly», porque es un valor de criterio.
  Todo eso queda para la v2.1.

## 6. Lo que necesita F3

- **Ficheros**: `astro-site/public/dl/restaurant-checklist-templates/`, 11 xlsx, con los nombres y títulos de SPEC §2.1 tal cual.
- **Datos verificables para la landing**: 9 plantillas + 2 bonus; 47 pestañas; 491 tareas ya escritas; 34 desplegables (✓ / — / N/A); contador que excluye N/A; 157 fórmulas con valor en caché; 4.286 celdas verdes editables; 36 hojas protegidas sin contraseña.
- **Contenido US**: horas en reloj de 12 h; °F y FDA Food Code; tabla de caja en dólares (15 filas con cartuchos) con propinas de tarjeta fuera de las ventas; calendario US de 22 fechas; US Letter y pie «AI Chef Pro · aichef.pro · Page &P of &N» en las 47 hojas.
- **Revisión adversarial**: `revision/dump_en.txt` frente a `revision/dump_es.txt` (mismo orden y formato).
- **Recordatorios**: SPEC §9 y `TIENDA-INTERNACIONAL.md` §6.
