# HACCP Food Safety Kit Pro — F2 (entregables) · notas de cierre

> Sesión Claude Code, 3-oct-2026. SPEC §7 pasos 3-5 y §8 (G1-G8). Implementador único (tamaño S), sin subagentes.
> Entradas: `textos_en/G1-G3.json` (subagentes sonnet, regla 1bis; sin tocar), `mapas.py`, `censo_es.json`,
> `textos_es.json`. Fuente ES en solo lectura: `astro-site/public/dl/pack-appcc/` (sin cambios). Construido y
> verificado en el **VPS** (D27: `/root/wt-haccp`, venv `/root/venv-guias`), xlsx de vuelta por `scp` con sha256
> idénticos; commit desde el Mac.

## 1. Qué se ha construido

| Pieza | Qué es |
|---|---|
| `aplicar_en.py` | Copia adaptada de `restaurant-inventory-kit/aplicar_en.py`. Renombrado de hojas + referencias; fórmulas = los 17 patrones de `FORMULAS_EN` celda a celda y el resto por `CLAVES` (estricto: un literal sin clave aborta); textos **por aparición** (`textos_es.json` → `donde`), no por cadena; DV (CLAVES, D13, `DV_NUM`, mensajes) + D14; CF; capas `LIMITES_02` (+ lista de Instructions B13:B22), `SEVERIDAD_15`, `POR_CELDA`, `EJEMPLOS_NUM`, `TEMP_COLUMNAS`, `PARAMETROS` (D15-D16), `ALTITUD_19`, `SIN_LETRAS`, `CONSERVAR_EN`; 62 fechas de texto → fechas reales; formatos 14/22/18; Letter + pie; docProps; comprobación de Instructions!B2 = título D5; **cobertura**: toda aparición «regenerar» del ES tiene que escribirla una capa o aborta. `--dry-run [--salida]`, `--parcial` (solo ensayo), `--idempotencia`, `--json`; `inject_cache` AL FINAL |
| `gates_en.py` | G1-G8 de SPEC §8 contra `censo_es.json`, los xlsx ES y `mapas.py`. `--autotest`: 10 defectos inyectados en copias (G1 ×2, G2 ×2, G3 ×2, G4, G5, G6, G7), los 10 cazados |
| `astro-site/public/dl/haccp-templates/` | Los 21 xlsx EN con los nombres de SPEC §2.1 |
| `postprocess-transversal.py` | `haccp-templates` en `EXCLUIDOS` (un `all` le forzaría A4 y español) |
| `censo-entregables.py` | `haccp-templates` en `PRODUCTOS_LETTER` (exige Letter; «Instructions» es hoja de texto) |
| `mapas.py` | 2 arreglos (§4.1 y §4.2) |

## 2. Cómo regenerar (en el VPS; en el Mac solo en serie y con `istats` < 62 °C)

```bash
ssh vps
cd /root/chefpro-modernize && git fetch origin && git worktree add /root/wt-haccp origin/feat/haccp-templates-en
cd /root/wt-haccp/scripts/productos-digitales/haccp-kit
PY=/root/venv-guias/bin/python
$PY mapas.py && $PY gate_f1.py                                   # 0 errores · VERDE
$PY aplicar_en.py --dry-run --salida /tmp/haccp-dry              # ensayo (opcional)
$PY gates_en.py --dir /tmp/haccp-dry
$PY aplicar_en.py --idempotencia [--mes October]                 # real: dl/haccp-templates/ (inject_cache va dentro)
$PY gates_en.py [--mes October] && $PY gates_en.py --autotest
cd /root/wt-haccp && $PY scripts/productos-digitales/censo-entregables.py --only haccp-templates --fail
$PY scripts/productos-digitales/gate-no-latinos.py --only haccp-templates
# vuelta: scp 'vps:/root/wt-haccp/astro-site/public/dl/haccp-templates/*.xlsx' <worktree Mac>/astro-site/public/dl/haccp-templates/
# limpieza: cd /root/chefpro-modernize && git worktree remove --force /root/wt-haccp
```

En el VPS `/dev/null` está roto: redirigir siempre a ficheros de `/tmp`. No guardar los xlsx con openpyxl después de
`inject_cache` (borraría la caché). `--mes`: la línea de versión lleva el mes de la construcción («Version 2.0 ·
October 2026 · …»); si F3 publica otro mes, reconstruir con `--mes` y volver a pasar los gates con el mismo `--mes`.
Construcción: ~15 s con idempotencia; gates ~1 min; autotest ~3 min.

## 3. Resultados (construcción real, 3-oct)

```
G1 paridad      OK  hojas 48 · fórmulas 1141 (17 patrones FORMULAS_EN = 595 celdas) · con hoja 40 · DV 57 + D14 · D13 1
                    · dv_celdas 5610 + 40 · CF 195 · merges 294 · áreas 48 · títulos 25 · paneles 25
                    · verdes 10854 + 2 · desbloqueadas = verdes + 2 (D15-D16) · sin protección · 0 gráficos/imágenes
G2 restos       OK  valores 2350 · literales 9349 · DV 147 · docProps 147 · pies 48 · formatos 6961 · 31 textos con °C, todos
                    entre paréntesis tras su °F
G3 formato      OK  Letter 48/48 · fechas 14 = 495 celdas (incluidas las 62 de texto) · 22 = 160 · 18 = 120 · pies 48 · firmas 48
                    · versiones 21 · docProps y Instructions!B2 = D5 en los 21
G4 claves       OK  31 DV de lista (todos los ítems ∈ CLAVES o PROCESOS_16) · 362 valores dentro de su lista · 44 números
                    dentro de su DV numérica
G5 CF           OK  73 rangos sin colisiones · mapas.cruzar_censo 0 errores
G6 cálculo      OK  <v> en las 1141 fórmulas, 0 errores · 60 veredictos = CLAVES[veredicto ES] (01, 02, 08 Complete ×8, 09,
                    10, 12, 16, 17 ×2, 18, 19, B01) · 36 recuentos = ES · historia §5 64 celdas · INC-001…007 en el 11
G7 límites      OK  01 frío 42 / congelado 28 / caliente 14 · 311 fórmulas sondeadas contra LIMITES_F · LIMITES_02 10 ·
                    PARAMETROS 2 · PROCESOS_16 165/155/145/135/165 · 9 DV en °F con su mensaje
G8              OK  censo-entregables: n=21 form=1141 f_sinCache=0 box=0 noA4=0 creator≠AICP=0 nonlat=0 emptyStr=0 →
                    0 defectos (--fail) · gate-no-latinos: 21 ficheros, 0 caracteres
VERDE: 8 gates, 0 fallos · AUTOTEST 10/10 CAZADO · idempotencia 0 diferencias · inject_cache fallos_pycel=0 en los 21
```

## 4. Desviaciones de la SPEC (y por qué)

1. **`mapas.PARAMETROS` (18)**: la nota decía «24 h at -20 °C (-4 °F)», que contradice D9 («°F primero, °C entre
   paréntesis») y la regla de G2; queda «24 h at -4 °F (-20 °C)». Además, `mapas.autotest` llamaba `err(...)` sobre una
   lista (habría reventado si `POR_CELDA` trajera español): `err.append`.
2. **09 «Used Oil Pickups»!B5 = 10** (`aplicar_en.EJEMPLOS_EXTRA`): SPEC §5 dice «40 L → 10 gal» y la cabecera EN es
   «Gallons collected», pero `mapas.EJEMPLOS_NUM` solo cubre temperaturas. G6 lo comprueba.
3. **15 columna D = solo la categoría** («Priority» / «Priority foundation» / «Core»), sin el §: E41:E42 la cuentan con
   `COUNTIFS(...,"Priority")`, por igualdad. El § de cada punto sigue en `mapas.SEVERIDAD_15` para la revisión P/Pf/C.
4. **D14**: la DV nueva de `Cooling!I5:I44` copia flags y mensajes EN de la de D/F (-22…266 °F) y las 40 celdas toman
   el formato `0.0` de D5 (en el ES eran texto «Destino», formato General).
5. **D15-D16**: A3:C3 nuevas con el estilo copiado de `19!A3:C3` del ES (sin combinar celdas: G1 exige 294 merges).
6. **Formatos propios sin uso** (`DD/MM/YYYY`, `HH:MM`, `DD/MM/YYYY HH:MM` y el `yyyy-mm-dd h:mm:ss` que openpyxl crea
   al escribir una fecha) se renombran a variantes US en `styles.xml`: ninguna celda los usa, pero G2 los leería.
7. **G2, lo que se admite a propósito**: «EPA Reg. No.» (no es el «Reg.» europeo); `852/2004`, `1169/2011`… solo si el
   mismo texto dice «UK»/«retained» (D8, D25); `béchamel`, `Entrées` (= `CLAVES['Segundos']`), `Pedro Ximénez` y
   `boquerones` (nombres de plato de SPEC §5). Regla del °C: dentro de un paréntesis y con su °F dentro del paréntesis
   o en los 40 caracteres anteriores («135 °F or above (UK: 63 °C …)», «(39 °F / 4.1 °C)»).
8. **G6 «historia»** usa las cifras de SPEC §5 (son datos de la SPEC, no recuentos del censo).

**Ningún texto de `textos_en/` rompió un gate ni se ha tocado** (0 cadenas corregidas).

**Para la revisión adversarial** (no es un fallo de gate): D21 manda fecha-hora = `numFmtId 22` (`m/d/yy h:mm`), que
Excel US muestra en reloj de 24 h («9/5/26 18:00»); las horas sueltas sí van en 12 h (`numFmtId 18`). Si se quiere
AM/PM también ahí, basta cambiar `FMT_FECHA_HORA` por un formato propio `m/d/yy h:mm AM/PM` y la expectativa de G3.

## 5. Lo que necesita F3

Ficheros (`astro-site/public/dl/haccp-templates/`, 21 xlsx, ≈ 290 KB): los 21 nombres y títulos de SPEC §2.1, tal
cual. Datos verificables para la landing: 21 plantillas (19 + 2 bonus), 48 pestañas (21 de instrucciones + 27 de
trabajo), 1.141 fórmulas con valor en caché, 58 desplegables y validaciones, 195 formatos condicionales (semáforos),
10.856 celdas verdes editables, sin contraseñas ni protección; °F en todas las fórmulas y desplegables de temperatura
(FDA Food Code 2022: 41 °F frío, 135 °F caliente, 165/155/145/135 °F cocción, enfriamiento en 2 tramos 135→70→41 °F,
parásitos −4 °F 168 h / −31 °F 15 h, termómetros ±2 °F con corrección por altitud en pies); US Letter y pie
«AI Chef Pro · aichef.pro · Page &P of &N» en las 48 hojas. Recordatorios: SPEC §9 y `TIENDA-INTERNACIONAL.md` §6.
