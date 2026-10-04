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

## 6. Revisión final (sesión Claude Code, 3-oct-2026)

Arreglos de la revisión adversarial final, aplicados en la fuente (`textos_en/G1-G3.json` por id, `mapas.py`,
`aplicar_en.py`, `gates_en.py`) y los 21 xlsx reconstruidos en el VPS (worktree temporal, borrado al terminar; sha256
idénticos tras el `scp`). Todos los ids tocados tenían `n_apariciones = 1` salvo `c0431` («Caducidad», cabecera de
05 + ítem de la DV del 11), que cambia en los dos sitios a propósito. 74 textos cambiados.

| # | Qué | Dónde |
|---|---|---|
| 1 | Salud del personal: ictericia, dolor de garganta con fiebre, herida infectada/supurante; vómitos/diarrea = 24 h sin síntomas (§2-201.12-.13; UK 48 h, junto a esa regla y no a la de ictericia); garganta con fiebre = alta médica escrita; ictericia o Big 6 = vuelta solo con el visto bueno de sanidad | 13 Instructions!B16, Hygiene Checklist!B25-B26 y tarjeta 13 de la landing |
| 2 | ALERT de enfriamiento = desechar + 11; recalentar a 165 °F y reiniciar solo si se detecta antes de las 2 h | 17 Instructions!B13, Cooling!A46 |
| 3 | Desinfectante 50-200 ppm con tiras (§4-501.114, §4-302.14); «1:50» fuera de superficies de contacto (≈ 1 cucharadita por galón, escrito «about»: «≈» no está en la lista blanca de G2); lavavajillas químico 50-100 ppm; cada 4 h en uso continuo (§4-602.11). G6 pasa a lavar-aclarar-desinfectar-**secar al aire** (§4-901.11: un desinfectante sin aclarado no se aclara ni se seca con papel). En «Chemicals» la lejía 1:50 solo va a cubos, baños y contenedores (ninguna superficie de contacto); B7 añade la dilución de fregaderos | 03 Master Cleaning Plan!D6, D14, G6, G26, Chemicals!B7 |
| 4 | REPEAT por tiempo (> 2 h a 165 °F) = desechar + 11 (§3-403.11(E)) | 16 Cooking & Reheating!A46, Instructions!B13 |
| 5 | Fuera la frase «acota el tiempo en la zona de peligro»; agua fría corriente ≤ 70 °F (21 °C) admitida (§3-501.13(B)) | 12 Hazard Analysis!C12, I12, L12; 17 Thawing!A46 |
| 6 | Control del alérgeno en cocina = OPRP al 100 % de las comandas con alergia (coherente con H17) | 12 Instructions!B14 |
| 7 | 0,2 mg/L = mínimo a la entrada de la red; cloro total si hay cloramina; residual detectable en la red | 10 Water Checks!A37, Instructions!B13 y B26; 12!I15 |
| 8 | «Desinfección» → `CLAVES['Desinfección'] = 'Exclusion / proofing check'` (DV 07!B5:B84; ninguna celda de ejemplo la usaba) | 07 Instructions!B6, B15 · `mapas.CLAVES` |
| 9 | CFPM: «al menos un empleado con funciones de supervisión» (§2-102.12(A)) | 13 Instructions!B12, 15!C8, BONUS-01 Training Log!A49 |
| 10 | Exenciones de §3-402.11(B) completas + declaración escrita del proveedor (§3-402.12(C)); 3.ª vía de congelación −31 °F hasta solidificar + −4 °F 24 h (la fórmula no la comprueba: se anota en «Notes») | 18 Instructions!B13, B24; Parasite Destruction!A46, A48; 15!C33 |
| 11 | `FMT_FECHA_HORA = 'm/d/yy h:mm AM/PM'` (formato propio, ya no `numFmtId 22`): 160 celdas (17 Thawing D:E, 18 D:E…). `NUMFMT[FMT_FECHA_HORA] = None` y G3 lo compara por cadena | `aplicar_en.py`, `gates_en.py` G3 |
| 12 | A3 con ajuste de texto y fila 3 más alta: 45 en 17/18; 60 en 19 (su etiqueta ocupa 4 líneas en una columna de 14) | `aplicar_en.envolver_a3` |
| 13 | INC-001 = miércoles 9/9/26 (lectura de 44 °F de 01 Weekly Log!B9): `mapas.FECHAS_TEXTO_EN` (11!B5, L5), que leen `fechas_texto` y G3 | 11 Corrective Actions |
| 14 | Reacción alérgica: adrenalina primero, luego 911 (UK 999) | 14 Instructions!B13, Allergen Chart!B29-B30 y tarjeta 14 de la landing |
| 15 | Referencias cruzadas con paréntesis apilados → «template NN (Título corto)» con un solo nivel (35 textos reescritos; los títulos con paréntesis o dos puntos se acortan en todas las referencias: 01, 04, 06, 08, 09, 10, 12 → «HACCP Plan», 17, 18); «Expired» → «Expiry / date mark» (`CLAVES['Caducidad']` + `c0431`); «blast chiller» → «blast freezer» a −22 °F; punto 21 del 15: uñas = Pf (§2-302.11), el punto pasa a Priority foundation en `SEVERIDAD_15` (siguen 25 puntos) | 15, 16, 17, 18, 19, BONUS-02, 05, 11, 01 |

Resultados (VPS, construcción real con `--idempotencia`): idempotencia 0 diferencias · `inject_cache` fallos_pycel=0
en los 21 · G1-G8 VERDE (G2: 34 textos con °C, todos tras su °F; G3: fechas 14 = 495, fecha-hora = 160, 18 = 120) ·
AUTOTEST 10/10 CAZADO · `censo-entregables --only haccp-templates --fail` 0 defectos · `gate-no-latinos` 0 ·
comprobación openpyxl (data_only) en el Mac: los 1.141 valores en caché de las fórmulas, idénticos a los de antes de
la revisión (0 diferencias), y las celdas de la tabla con su texto nuevo.
