# Restaurant Staff Scheduling Kit Pro — F2 (entregables) · notas de cierre

> Sesión Claude Code, 3-oct-2026. SPEC §7 pasos 3-5 y §8 (G1-G8). Implementador único (tamaño S), sin subagentes.
> Entradas: `textos_en/G1.json` y `G2.json` (subagentes sonnet, regla 1bis), `mapas.py`, `censo_es.json`,
> `textos_es.json`. Fuente ES en solo lectura: `astro-site/public/dl/kit-gestion-personal/` (sin cambios). Construido
> y verificado en el **VPS** (D24: `/root/wt-staff`, venv `/root/venv-guias`); xlsx de vuelta por `scp` con sha256
> idénticos; commit desde el Mac.

## 1. Qué se ha construido

| Pieza | Qué es |
|---|---|
| `aplicar_en.py` | Copia adaptada de `haccp-kit/aplicar_en.py`. Renombrado de hojas + referencias; fórmulas = los 10 patrones de `FORMULAS_EN` celda a celda (548 celdas) y el resto por `CLAVES` (estricto con todo literal que lleve letras o «€»); textos **por aparición** (`textos_es.json` → `donde`); DV: listas por `CLAVES` (el ítem vacío de «V,B,F,PE,» se conserva), D11 (`DV_LISTAS_ESPECIALES`), personalizadas con literales (05 «High/Normal»), mensajes por aparición y las 4 `DV_NUEVAS`; CF: fórmula **y** atributo `text` por `CLAVES`; capas `titulo_interior`, `TURNOS_EN` (horas reales), `LEYENDAS`, `POR_CELDA`, `PARAMETROS` (fila 3 de «Time Log»), `VALORES_EN`; formatos D17-D18 (moneda fuera, fecha 14, `m/d`, hora 18, `h:mm AM/PM;;`) y formatos propios sin uso renombrados; US Letter; docProps D18; comillas rectas; **cobertura**: toda aparición «regenerar» la escribe una capa o aborta. `--dry-run [--salida]`, `--parcial`, `--idempotencia`, `--json`; `inject_cache` AL FINAL |
| `gates_en.py` | G1-G8 de SPEC §8 contra `censo_es.json`, los xlsx ES y `mapas.py`. `--autotest`: 10 defectos inyectados en copias (G1 ×2, G2 ×2, G3 ×2, G4, G5, G6, G7), los 10 cazados |
| `astro-site/public/dl/restaurant-schedule-templates/` | Los 9 xlsx EN con los nombres de SPEC §2.1 |
| `postprocess-transversal.py` | `restaurant-schedule-templates` en `EXCLUIDOS` (un `all` le forzaría A4 y español) |
| `censo-entregables.py` | `restaurant-schedule-templates` en `PRODUCTOS_LETTER` (exige Letter; «Instructions» es hoja de texto) |
| `textos_en/G2.json` | 1 cadena corregida (§4.6) |

## 2. Cómo regenerar (en el VPS; en el Mac solo en serie y con `istats` < 62 °C)

```bash
ssh vps
cd /root/chefpro-modernize && git fetch origin && git worktree add /root/wt-staff origin/feat/restaurant-schedule-templates-en
cd /root/wt-staff/scripts/productos-digitales/staff-kit
PY=/root/venv-guias/bin/python
$PY mapas.py && $PY gate_f1.py                                   # 0 errores · VERDE
$PY aplicar_en.py --dry-run --salida /tmp/staff-dry              # ensayo (opcional)
$PY gates_en.py --dir /tmp/staff-dry
$PY aplicar_en.py --idempotencia [--mes October]                 # real: dl/restaurant-schedule-templates/ (inject_cache dentro)
$PY gates_en.py [--mes October] && $PY gates_en.py --autotest
cd /root/wt-staff && $PY scripts/productos-digitales/censo-entregables.py --only restaurant-schedule-templates --fail
$PY scripts/productos-digitales/gate-no-latinos.py --only restaurant-schedule-templates
# vuelta: scp 'vps:/root/wt-staff/astro-site/public/dl/restaurant-schedule-templates/*.xlsx' <worktree Mac>/astro-site/public/dl/restaurant-schedule-templates/
# limpieza: cd /root/chefpro-modernize && git worktree remove --force /root/wt-staff
```

En el VPS `/dev/null` es un fichero normal: redirigir siempre a ficheros de `/tmp`. No guardar los xlsx con openpyxl
después de `inject_cache` (borraría la caché). `--mes`: la línea de versión lleva el mes de la construcción («Version
2.0 · October 2026 · …»); si F3 publica otro mes, reconstruir con `--mes` y pasar los gates con el mismo `--mes`.
Tiempos en el VPS: construcción ~22 s con idempotencia e `inject_cache`; gates ~40 s (los 4 casos FLSA recalculan
copias del 02); autotest ~10 s (sin los casos FLSA).

## 3. Resultados (construcción real, 3-oct, `--mes October`)

```
G1 paridad      OK  hojas 30 · fórmulas 4593 (10 patrones FORMULAS_EN = 548 celdas) · con hoja 2488 (= censo 2518 − 30:
                    «Monthly OT Summary»!G ya no cita «Time Log», D10) · DV 52 + 4 nuevas · D11 2 · dv_celdas 4814 · CF 127
                    · merges 165 · protegidas 21 (sin contraseña, mismos flags) · áreas 30 · títulos 14 · paneles 17
                    · columnas ocultas 27 · verdes 7503 = desbloqueadas 7503 (7500 + B3, D3, F3 de D10) · 0 gráficos/imágenes
G2 restos       OK  valores 1168 · literales 26812 · DV 180 mensajes + 138 ítems · docProps 63 · pies 30 · formatos 4700
                    · styles.xml 29 · 1 texto con °C (tras su °F)
G3 formato      OK  Letter 30/30 · fechas 14 = 1021 · m/d = 53 · horas 18 = 600 · Shifts C5:D12 «h:mm AM/PM;;» = 16 · pies 30
                    · líneas de marca 19 · versiones 9 · docProps y Instructions!B2 = título interior D5 en los 9
G4 claves       OK  24 DV de lista (ítems ∈ CLAVES o D11) · 44 valores dentro de su lista · 319 números dentro de su DV
                    numérica (horas reales incluidas) · tipos de negocio 03 y B02 = su DV (10 y 10)
G5 CF           OK  30 rangos · 126 tokens sin colisiones (ni de SEARCH) · mapas.cruzar_censo 0 errores
G6 cálculo      OK  <v> en las 4593 fórmulas, 0 errores · caché EN = caché ES (207 números, 55 fechas, 3 veredictos por
                    CLAVES, 4 textos calculados sin español) salvo las cifras D8/D20: Shifts!E5:E12 = 8,8,8,9,16,0,0,0 ·
                    03 Staffing Forecast B21 = 7, B22 = 23,356.67 · B02 B29 = 7, B38 = 23,356.67, B39 = 280,280.04,
                    B40 = 72,800, B41 = 32.08 %, D41 = 33 %, B43 = «🟢 EXCELLENT (below your target)» · B02 Instructions!B16
                    con 72,800 / 23,356.67 / 32.1 / EXCELLENT · semana 1 = domingo 1/3/2027 y +7
                    · FLSA (D10, copias del 02 recalculadas con pycel): 6 × 9 h → 14 h con F3 vacío y 14 h con F3 = 8;
                    4 × 10 h → 0 h con F3 vacío y 8 h con F3 = 8
G7 reglas       OK  57 celdas de VALORES_EN · 14 cifras = SPEC §3 (40 h, 1.5×, 10 h, 10 h, 10 %, 26, 50, 14, 41/135 °F…)
                    · D11 = 52/26/24/12 · PARAMETROS 6 · H FLSA ×300 con $B$3/$D$3/$F$3/WEEKDAY · TURNOS_EN 8 filas
G8              OK  censo-entregables: n=9 form=4593 f_sinCache=0 box=0 noA4=0 creator≠AICP=0 nonlat=0 emptyStr=0 err=0 →
                    0 defectos (--fail) · gate-no-latinos: 9 ficheros, 0 caracteres
VERDE: 8 gates, 0 fallos · AUTOTEST 10/10 CAZADO · idempotencia 0 diferencias · inject_cache fallos_pycel=0 en los 9
mapas.py 0 errores · gate_f1 VERDE
```

## 4. Desviaciones de la SPEC (y por qué)

1. **`TURNOS_EN` con `None` (OFF, V, S) se escribe como 0**, no como celda vacía: el formato `h:mm AM/PM;;` lo deja en
   blanco y `Shifts!E10:E12` da 0 como en el ES (G6 lo exige); vacía, la fórmula daría «» y cambiaría la caché.
2. **D10, fila 3 de «Time Log»**: el estilo se copia del propio libro 02 («Monthly OT Summary» A3 para las etiquetas y
   F3 para las celdas verdes desbloqueadas); etiquetas con ajuste de texto y fila 3 a 30 pt (C y E miden 14 y 12);
   formatos B3 `0`, D3 y F3 `General` (admiten 7.5). Sin combinar celdas (G1 exige 165 merges).
3. **`DV_NUEVAS`**: su único mensaje va como `prompt` y como `error` (estilo *stop*, admite vacío).
4. **G1, fórmulas con hoja**: 2.488 y no 2.518 — el patrón D10 de «Monthly OT Summary»!G (`=B × tarifa × recargo`) ya no
   cita «Time Log»; el gate calcula ese delta patrón a patrón en vez de exigir la cifra del censo.
5. **G2, lista blanca**: se deriva de los símbolos del ES publicado + tipografía EN, y admite además **💵** (B01
   «Shift Handover»!A46: el traductor cambió el 💶 del ES por el billete de dólar; no es un símbolo de moneda en texto).
6. **`textos_en/G2.json` · `c0783`** (DV de B01 «Shift Handover»!C17:C22): llevaba «TEC-28 · », un ID interno de
   ticket heredado del ES. Corregido a «Without a list, each shift types a different word…»; G2 caza ya `TEC-nn`
   (`RX_ID_INTERNO`). Es la única cadena de `textos_en/` tocada.
7. **Formatos propios sin uso** (`hh:mm`, `dd/mm`, `#,##0.00 €`, `€#,##0.00`, `dd/mm/yyyy`) se renombran en
   `styles.xml` a variantes US: ninguna celda los usa, pero G2 los leería.
8. **CF `text`**: los `containsText` del kit llevan el token también en el atributo `text`; se traduce por `CLAVES`
   igual que la fórmula (el HACCP no tenía ninguno y abortaba).

**Para la revisión adversarial** (no es un fallo de gate): los días del cuadrante siguen de lunes a domingo (como el
ES; la SPEC no los reordena) mientras la semana laboral FLSA del 02 y la semana 1 del 05 empiezan en domingo.

## 5. Lo que necesita F3

Ficheros (`astro-site/public/dl/restaurant-schedule-templates/`, 9 xlsx, ≈ 246 KB): nombres y títulos de SPEC §2.1 tal
cual. Datos verificables para la landing: 9 plantillas (7 + 2 bonus), 30 pestañas, 4.593 fórmulas con valor en caché,
56 validaciones y desplegables, 127 formatos condicionales (semáforos), 7.503 celdas verdes editables, 21 hojas
protegidas sin contraseña; turnos con horas reales en reloj de 12 h, alertas de *clopening* (10 h), turno largo (10 h),
40 h FLSA, menores (29 CFR 570) y 7.º día seguido (CA); horas extra FLSA por semana laboral con regla diaria estatal
opcional (CA 8 h) sin doble cómputo; periodos de pago 52/26/24/12; °F en el B01; US Letter y pie «AI Chef Pro ·
aichef.pro · Page &P of &N» en las 30 hojas. Recordatorios: SPEC §9 y `TIENDA-INTERNACIONAL.md` §6.
