# Restaurant Financial Plan Kit Pro — F2 (entregables) · notas de cierre

> Sesión Claude Code, 3-oct-2026. SPEC §7 pasos 3-5 y §8 (G1-G8). Implementador único, sin subagentes.
> Entradas: `textos_en/G1.json` y `G2.json` (subagentes sonnet, regla 1bis), `mapas.py`, `censo_es.json`,
> `textos_es.json`. Fuente ES en solo lectura: `astro-site/public/dl/kit-plan-financiero/` (sin cambios). Construido
> y verificado en el **VPS** (D24: `/root/wt-fin`, venv `/root/venv-guias`); xlsx de vuelta por `scp` con sha256
> idénticos; commit desde el Mac; VPS limpio (worktree quitado).

## 1. Qué se ha construido

| Pieza | Qué es |
|---|---|
| `aplicar_en.py` | Copia adaptada de `staff-kit/aplicar_en.py` + `restaurar_graficos` de `recipe-costing-kit/`. Renombrado de hojas + referencias (fórmulas, DV, CF, títulos de impresión y series/categorías de los 9 gráficos); el patrón D10 de `FORMULAS_EN` celda a celda (48) y el resto por `CLAVES`; textos **por aparición**; DV: lista del B09 por `CLAVES`, **DV_PARTIDAS** (la DV 0-1 de C+H se parte: C la conserva, H estrena «decimal 0-50», título «Invalid useful life»); CF fórmula **y** `text`; capas título interior, `POR_CELDA`, `FIJOS` (por texto), `VALORES_EN`, `AJUSTE_TEXTO`, `ANCHOS`; formatos D17-D18 (+ `FORMATOS_POR_RANGO`: 04 H sin %); US Letter; docProps D5/D20; comillas rectas; cobertura de «regenerar»; gráficos restaurados desde el XML del ES (estilo 12, ancla, títulos EN, eje «Amount»). `inject_cache` AL FINAL **en el mismo proceso con `IRR` enseñada a pycel** (la Newton-Raphson del ES, `motor.tir_newton`; `#NUM!` sin cambio de signo → el `IFERROR` da «—») y `cachear_irr` del 07, que recalcula la TIR en Python desde los flujos cacheados y la compara (o la inyecta si faltara). `--dry-run [--salida]`, `--parcial`, `--idempotencia`, `--json` |
| `gates_en.py` | G1-G8 de SPEC §8 contra `censo_es.json`, los xlsx ES y `mapas.py`. G6 compara la caché EN con una **caché de referencia** (el ES publicado con `VALORES_EN` y el patrón D10, recalculado con pycel) celda a celda + cifras de SPEC §5 + caso trazado de la TIR + caso D10. `--autotest`: 22 defectos inyectados en copias (G1 ×3, G2 ×6, G3 ×5, G4 ×2, G5, G6 ×3, G7 ×2), los 22 cazados |
| `astro-site/public/dl/restaurant-financial-plan-templates/` | Los 10 xlsx EN con los nombres de SPEC §2.1 (≈ 213 KB) |
| `postprocess-transversal.py` | `restaurant-financial-plan-templates` en `EXCLUIDOS` (un `all` le forzaría A4 y español y le borraría la caché de la TIR) |
| `censo-entregables.py` | `restaurant-financial-plan-templates` en `PRODUCTOS_LETTER` |
| `mapas.py` | `dv_lista`, `FORMATOS_POR_RANGO`, `DV_MENSAJES_EN` (vacío), `AJUSTE_TEXTO`, `ANCHOS`; `DD/MM/YYYY` en `FORMATOS_EN`; 04 Licencias H vacía (D10); 6 `FIJOS` EN acortados o con la cita de un nivel (§4) |
| `textos_en/G2.json` | 1 cadena corregida (§4.6) |

## 2. Cómo regenerar (en el VPS; en el Mac solo en serie y con `istats` < 62 °C)

```bash
ssh vps
cd /root/chefpro-modernize && git fetch origin && git worktree add --detach /root/wt-fin origin/feat/restaurant-financial-plan-templates-en
cd /root/wt-fin/scripts/productos-digitales/financial-kit
PY=/root/venv-guias/bin/python
$PY mapas.py && $PY gate_f1.py                                     # 0 errores · VERDE
$PY aplicar_en.py --dry-run --salida /tmp/fin-dry --mes October    # ensayo (opcional)
$PY gates_en.py --dir /tmp/fin-dry --mes October
$PY aplicar_en.py --idempotencia --mes October                     # real: dl/restaurant-financial-plan-templates/ (inject_cache + TIR dentro)
$PY gates_en.py --mes October && $PY gates_en.py --mes October --autotest
cd /root/wt-fin && $PY scripts/productos-digitales/censo-entregables.py --only restaurant-financial-plan-templates --fail
$PY scripts/productos-digitales/gate-no-latinos.py --only restaurant-financial-plan-templates
# vuelta: scp 'vps:/root/wt-fin/astro-site/public/dl/restaurant-financial-plan-templates/*.xlsx' <worktree Mac>/astro-site/public/dl/restaurant-financial-plan-templates/
# limpieza: cd /root/chefpro-modernize && git worktree remove --force /root/wt-fin
```

En el VPS `/dev/null` es un fichero normal: redirigir siempre a ficheros de `/tmp`. **Nunca** guardar los xlsx con
openpyxl después de `inject_cache` (borraría la caché, la de la TIR incluida) ni correr `inject_cache.py` a pelo sobre
el 07 (sin el parche, pycel deja `Projections!B24` sin caché: `aplicar_en.cachear_irr` la repone). `--mes`: la línea
de versión lleva el mes de la construcción; si F3 publica otro mes, reconstruir con `--mes` y pasar los gates igual.
Tiempos en el VPS: construcción ~6 s (con idempotencia e `inject_cache`); gates ~30 s; autotest ~60 s.

## 3. Resultados (construcción real, 3-oct, `--mes October`)

```
G1 paridad   OK  hojas 56 · fórmulas 2437 (patrón D10 = 48) · con hoja 577 · DV 65 (60 + 5 partidas; unión de sqref = ES)
                 · dv_celdas 1922 · CF 59 · merges 83 · protegidas 56 (sin contraseña, mismos flags) · títulos 41 · paneles 42
                 · verdes 2082 · desbloqueadas 2187 · gráficos 9 / series 20 (tipo, estilo, ancla, ejes, refs con pestaña EN)
G2 restos    OK  valores 1790 · literales 2233 · DV 130 mensajes + 3 ítems · gráficos 18 textos · docProps 70 · pies 56
                 · formatos 4126 + styles.xml 31 · celdas con formato € reescritas 3273 = censo
G3 formato   OK  Letter 56/56 · fechas 61 → numFmtId 14 · «p.p.» 64 → 0.0% · « años» → « years» (3) · 04 H sin % (48)
                 · pies 56 · marcas 49 · versiones 10 · docProps y B2 D5/D20 · ajuste 17 · anchos 24
G4 claves    OK  B09: 54 estados ∈ Pending/In progress/Completed · 1850 números dentro de su DV (vida útil 0-50 incluida)
G5 CF        OK  25 rangos · 51 tokens sin colisión SEARCH · mapas.cruzar_censo 0 errores
G6 cálculo   OK  <v> en las 2437, 0 errores · caché EN = referencia (1564 números, 279 veredictos por CLAVES, 9 textos)
                 · movidas por la SPEC 3: 06 Ratios E18 «⚠️ Acceptable» → «✅ Excellent» (labor 28 % < 30 %, D15), F18 0.25 → 0.30,
                   C30 393.25 → 36.58 (31,460 / 860 sq ft, D14)
                 · SPEC §5: 02 ventas 31,460 · EBITDA 17.3 % · break-even 23,076.92/mes, 41 covers/día · caja 24,307.69, 43
                   covers/día · 03 saldo final 15,000 (umbral 5,000) · B08 31,460 / 17.29 % / EBITDA anual 65,282.40
                   (pesimista −1,460/mes, optimista 19,615/mes) · 07 sin datos: TIR «—», NPV 0, payback «—», DSCR «Enter the loan»
                 · TIR caso trazado (−150,000 / 30,000 / 45,000 / 60,000 / 70,000 / 0): 11.9592 % en el 07 EN = 07 ES
                   = bisección independiente = cachear_irr · NPV 8 % 15,440.05 · payback 3.21 años · préstamo SBA 100,000 al
                   10 % / 10 años: cuota 16,274.54, intereses año 1 10,000, DSCR 1.84× ✅
                 · D10: 7,000 / 7 años → 1,000 · vida vacía → 0 · Summary G6 = 1,000
G7 reglas    OK  105 celdas de VALORES_EN · 16 cifras = SPEC §3 (8 %, 0, 80 %, 10/7/7/5, licencias vacías, 860, 30/35, 6/10,
                 10 %, 10 años, 10 %, 1.25×, 1.15×, 25 %…) · 48 × =IFERROR($B/$H,0) · 5 DV de vida útil 0-50
G8           OK  censo-entregables: 0 defectos (--fail) · gate-no-latinos: 10 ficheros, 0 caracteres
VERDE: 8 gates, 0 fallos · AUTOTEST 22/22 CAZADO · idempotencia 0 diferencias · inject_cache fallos_pycel=0 en los 10
mapas.py 0 errores · gate_f1 VERDE
```

## 4. Desviaciones de la SPEC (y por qué)

1. **TIR**: en vez de dejar que pycel falle en `IRR` (el ES acepta `fallos_pycel=1` y cachea aparte), se le **enseña
   `IRR`** con la misma Newton-Raphson del ES (`motor.tir_newton`) dentro de `aplicar_en.inyectar_cache`: 0 fallos y la
   celda cacheada por el mismo camino que las demás. `cachear_irr` se mantiene como verificación independiente. Con los
   datos de ejemplo del 07 (vacíos a propósito, como el ES) no hay cambio de signo: la caché es «—», igual que el ES.
2. **G6 por referencia**: «caché EN = caché ES salvo lo que mueven D8/D10/D12-D15» se implementa recalculando el ES
   publicado con `VALORES_EN` y el patrón D10 (pestañas ES) y comparando celda a celda; con los datos de ejemplo solo
   cambian 3 celdas (06, §3). El 03 y el 07 traen ceros en el ES, así que D8/D9/D12 no mueven ninguna cifra cacheada:
   el caso trazado de la TIR/DSCR y el caso D10 se prueban en copias recalculadas.
3. **04 columna H**: el formato `0.0%` del coeficiente ES pasa a `General` (`FORMATOS_POR_RANGO`): con años, `0.0%`
   enseñaría «1000.0%». **Licencias H5:H12 vacías** (D10 «licencias vacío»; `VALORES_EN` con `None`; IFERROR → 0).
4. **`ANCHOS`** (capa nueva, solo formato, como `recipe-costing-kit`): el sufijo «(excl. sales tax)» desbordaba la
   columna de rótulos de tablas numéricas; en vez de filas de dos líneas se ensancha la columna (01/01b años y
   Summary A → 36; 05 meses A → 36; 02 Break-Even B → 52; 07 Executive Summary B → 44). `AJUSTE_TEXTO` (ajuste +
   alto de fila) queda para notas: 02 Inputs B7, D7, D15, D17; 03 Assumptions D4:D9; 04 Dining Room FF&E A13; 07 Loan
   Schedule D4:D8; B08 Simulator A11. Las líneas largas de Instructions y las notas que desbordan hacia columnas
   vacías se dejan como en el ES (se leen enteras en pantalla).
5. **`FIJOS` EN tocados** (cadenas de `mapas.py`, no de los traductores): «All figures EXCLUDE sales tax; only file 03
   "Cash Flow Forecast" includes it…» y «…that file 07 "Lender & Investor Summary" needs» (la cita llevaba paréntesis:
   G2 «cita anidada»); «Sales per sq ft (excl. sales tax)», «Personal guarantee (SBA: owners of 20%+)», «Blanket lien on
   business assets (UCC-1)», «Assignment of life insurance (SBA lenders)» (los cortaba la columna de al lado).
6. **`textos_en/G2.json` · `c0519`** (07 Projections G12): citaba «the TOTAL INVESTMENT row», rótulo que no existe en
   el 04 EN. Corregido a «…"Summary" tab: "Annual depreciation" column, "TOTAL STARTUP COSTS (CAPEX)" row.» Es la única
   cadena de `textos_en/` tocada. Ninguna cadena de los traductores rompió un gate.
7. **docProps `title`** = título interior + « · Restaurant Financial Plan Kit Pro» (el mismo molde que el ES, D5).
8. No hay fechas escritas como texto en el ES (las 61 celdas de fecha están vacías): la capa «texto → fecha» del staff
   no aplica.

**Para la revisión adversarial** (no es fallo de gate): la caché de la TIR depende del parche de pycel; quien
regenere con `inject_cache.py` a pelo debe correr después `aplicar_en.cachear_irr`. Los textos C:E de `Benchmarks`
son guía de lectura (I3): si el usuario cambia F:G, no se mueven.

## 5. Lo que necesita F3

Ficheros (`astro-site/public/dl/restaurant-financial-plan-templates/`, 10 xlsx, ≈ 213 KB), nombres y títulos de SPEC
§2.1 tal cual. Datos verificables para la landing: 10 plantillas (8 + 2 bonus), 56 pestañas, 2.437 fórmulas con valor
en caché, 9 gráficos, 65 validaciones, 59 formatos condicionales (semáforos), 2.082 celdas verdes editables, 56 hojas
protegidas sin contraseña, US Letter y pie «AI Chef Pro · aichef.pro · Page &P of &N». Cifras del ejemplo: ventas
31,460/mes, EBITDA 17.3 %, break-even 23,076.92/mes (41 covers/día), break-even de caja 24,307.69 (43). El 07 llega
sin datos (TIR/NPV/payback/DSCR se calculan al rellenarlo; caso de prueba: TIR 11.96 %, DSCR 1.84×). Sales tax 8 %
de ejemplo y trimestral en el 03; vidas útiles 10/7/7/5; benchmarks US labor 30/35 % y ocupación 6/10 %; préstamo
SBA 7(a) 10 % / 10 años; DSCR 1.25× / 1.15×; aportación propia mínima 10 %. Recordatorios: SPEC §9 y
`TIENDA-INTERNACIONAL.md` §6 (test de Google Sheets antes de afirmarlo en la FAQ: IRR, gráficos, protección).
