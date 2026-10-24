# BBQ Catering Business Plan Kit (EN) — F2 (entregables) · notas

> Sesión Claude Code, 24-oct-2026. **Paso 1 de la F2** (conjunto «bbq», extracción, reuso del catering, caso US + D15,
> 4 tandas preparadas, calculadora D105-D106, regresión). Implementador único, sin subagentes. Código en el Mac
> (worktree `wt-bbq`); lo que abre xlsx/docx, en el **VPS** (`/root/wt-bbq`, venv `/root/venv-guias`). Rama
> `feat/bbq-catering-business-plan-en`. CPU del Mac < 52 °C en todo el paso.

## 1. Cómo se montó el conjunto «bbq» (fuente ES del circuito = FOOD TRUCK ES; diccionario = CATERING EN; código = MOBILE BAR)

`BP_CONJUNTO=bbq` → `mapas_bbq.instalar(M)`, `mapas.DATOS = business-plans-en-6/`, lanzador `bp6.py`. **Único cambio en
código común**: la rama `elif CONJUNTO == 'bbq'` de `business-plans-en/mapas.py` (+ el mensaje de error). El reuso por
celda lee el EN publicado del catering con los **mismos 8 sha256** que `mapas_mbar.py` (`bp6.py verificar`: 0 derivas).

| Fichero | Qué lleva |
|---|---|
| `mapas_bbq.py` | Producto D96-D98 (`dir_es` = FT ES, `slug_es` = parrillero ES), libros `BBQP`/`BBQC`, pestaña F2 «Phase 2 - Pits, Fire & Permits» (30 car.), 68 tareas 11/13/12/10/12/10, los **7 parches** del catering con el Break-Even en **±$3 / +$6** (D104), zonas D18/D19/TAREA, docx 131 ranuras, `RX_REESCRIBIR` invertido (van, refrigerat, generator, fuel, stations, chef, plated…), **51 `FORZAR_TRADUCTORES`**, `reuso_de` que deja pasar la propuesta del catering en las 5 filas D19 útiles (58, 62, 63, 65, 67), `PRESTAMO_SEMILLA` = 101,000 |
| `datos_bbq.py` | FIJOS (30 nuevos: motor, títulos, D19, líneas «BBQ packages / Add-ons» y su coste, «Disposables, wood & cooking fuel»), POR_CELDA (66: Supuestos, inversión 7-23 y A31 con el orden D102, P&L A10-A11/A22/A24-A27/A30-A35/A52/A55, 4 puestos W-2 + cobertura + nota del pit cook, `Cash Flow!O5`, notas del motor C20/C39/C67/E24, A2), `REGLA_UNIDADES` con la regla de temperaturas, cifras prohibidas + `RX_BBQ_NO` (D110), 118 tokens (alias de eventos, 14 partidas propias, `pago_dias` en su celda), 61 `DOCX_NOTAS` (§9 = 7 notas D108) con el **párrafo ES 2.2 del parrillero de la misma ranura** añadido al final, pistas (caso, D18 con 4 filas específicas, 14 filas D19, **68 tareas `TAREAS_BBQ`** con «[sobrevive]», «[sobrevive con ajuste]» o «[nueva]»), glosario §9 completo, caso US, `CALIBRACION_D15` (vacía), FORMULAS_EN |
| `bp6.py` | Lanzador (copia de `bp5.py`) + `verificar` (272 celdas de tarea en GBQ-check + sha256 del diccionario) + `fuente` + `calculadora` + `barrido` |
| `fuente_bbq.py` → `fuente_es_bbq.json` | Checklist ES del parrillero desde `parrillero-2_2/datos_checklist.py` (83 tareas, 11 SOLO_ES y 5 parciales marcadas), docx ES 2.2 por ranura (61), manual técnico (77 párrafos, 6 tablas), carta de cortes (40 / 12), 10 experiencias (179) y contrato (113 / 1) |
| `calculadora_bbq.py` · `barrido_bbq.py` · `BRIEF-TRADUCTORES.md` | D105-D106 (§5) · barrido del paso 3 · brief de las 4 tandas con el **glosario §9 completo pegado** (copia literal) y la regla «redactar, no traducir» |

**Grupos** (`textos_es.json`, 959 cadenas, sha256 `00b29195f643113b…`):

| Grupo | Cadenas | Palabras ES | Qué es | Va a |
|---|---|---|---|---|
| GM | 312 | 3.472 | Motor cuyo EN del catering no trae vocabulario que no valga para BBQ | nadie: `textos_en/GM.json` ya escrito |
| GRC-plan | 79 | 1.587 | EN del catering que vale con revisión: 57 celdas de la tabla D18 + 22 notas del motor | `textos_en/GRC-plan.json` escrito; revisión en la tanda (a) |
| **GBQ-plan** | 128 | 3.016 (entrada) | 72 de texto libre (notas C de Supuestos, D de inversión, F del P&L, J de Staffing, D18 con van / fuel, Instrucciones A5, Cash Flow D32) + 56 celdas D19 (20 con la propuesta del catering) | tanda 1 (a) |
| **GBQ-check** | 275 | 1.277 | 68 tareas × 4 columnas (una por celda, todas con la propuesta del catering de esa celda) + 3 textos del checklist | tanda 1 (b) |
| GX | 165 | 918 | Pestañas, CLAVES, FIJOS, POR_CELDA, versión, pie, docProps | nadie |

Docx (`docx_es_bbq.json`, VERDE): 131 párrafos, 0 multi-run; 61 ranuras → **bbq_a 29 / 2.954 palabras de ranura ·
bbq_b 32 / 3.765**; cada una con su nota BBQ y, al final, el ES 2.2 del parrillero (notas: 5.032 y 6.543 palabras con el ES).

## 2. No regresión (VPS, con la rama `bbq` en `mapas.py`; mismos comandos que `../business-plans-en-5/F2-NOTAS.md` §2)

| Conjunto | `mapas` | `gates_en` (dl/ publicados) · `--autotest` | `ensamblar_docx --autotest` | `check_textos --todas` | calculadora `--autotest` |
|---|---|---|---|---|---|
| FT/CAF (`mapas.py`, `gates_en.py`…) | 0 errores | **TODO VERDE** · **20/20** | **18/18** | las 7 OK | — |
| REST/PAN (`bp2.py`) | 0 errores | **TODO VERDE** · **20/20** | **16/16** | las 8 OK | — |
| BAR (`bp3.py`) | 0 errores | **TODO VERDE** · **20/20** | **8/8** | las 6 OK | — |
| CAT (`bp4.py`) | 0 errores | **TODO VERDE** · **20/20** | **8/8** | las 6 OK | VERDE (136) |
| MBAR (`bp5.py`) | 0 errores | **TODO VERDE** · **20/20** | **8/8** | las 6 OK | VERDE (778) |
| BBQ (`bp6.py`) | 0 errores (`verificar` OK, diccionario sin deriva) | parcial G1, G3-G7 **VERDE** sobre el dry-run (§3) | **8/8** | GM OK · GRC-plan OK · el resto, pendiente de redactar | VERDE (581) |

Script de la pasada: `/tmp/regresion.sh` del VPS (no versionado; reproducible con la tabla).

## 3. Caso US, dry-run y calibración D15 (`bp6.py aplicar_en --dry-run --parcial --salida /tmp/bbq-dry`, VPS)

Research §8 tal cual (150 eventos × $38 × 75 invitados, inversión con el orden D102): **D15 en verde sin tocar `B4` ni
`B35`** (holgura 18.0 %, DSCR mín 2.43, saldo mín > 0, cobertura 112 %). Préstamo de punto fijo **$101,000** en 2 vueltas
(semilla 98,000 → 101,000 → 101,000; `PRESTAMO_SEMILLA` = 101,000): supera el tope de $50,000 del SBA Microloan y encaja
en un **SBA 7(a)** (D100). **`CALIBRACION_D15` queda vacía** (G7: 0 calibraciones citadas).

Resultado (caché del dry-run, `cifras_caso.json` de esta carpeta, 118 tokens, sha256 `31d6545c612c0a45…`):
- Ventas **$427,500** / $478,800 / $517,104 (**$2,850 por evento**, 11,250 invitados).
- CAPEX **$83,300** (75,200 + fianza 1,800 + 1 mes previo 1,800 + contingencia 10 % × 45,000 = 4,500, por fórmula) +
  fondo de maniobra $52,371 = **$135,671** · fondos propios $35,000 (26 %) + préstamo **$101,000** al 10 % a 7 años
  (cuota $20,746).
- Margen bruto **60.8 %** · mercancía 28.8 % · personal **32.7 %** ($139,682) · commissary y parking 5.1 % · EBITDA
  $60,367 (**14.1 %**) · D&A $10,511 · intereses $10,100 · neto **$29,816 (7.0 %)** / $50,242 / $64,826.
- Equilibrio **128 eventos/año** (127.04 contable · 127.12 de caja) frente a 150 → holgura **18 %** (caída absorbible
  **15 %**: es el «≈ 15 %» de la SPEC) · **DSCR mín 2.43×** · saldo mínimo **$41,591** (mes 2) · payback 2.2 años (1.5
  sobre el CAPEX) · 9 personas = 2.85 FTE, cobertura 112 % · seguros $6,000.
- Pesimista (113 · $34.20 · 68) **$262,793**, resultado −$60,321 (EBITDA ≈ −$39,700) y **caja estimada −$8,085: se
  agota** (el docx §8 [99] tiene que decirlo) · optimista (188 · $41.80 · 83) $652,247 y +$176,312.
- Los 5 umbrales del P&L (D104: margen bruto ≥ 58 %, mercancía ≤ 35 %, personal ≤ 38 %, commissary ≤ 7 %, neto ≥ 5 %)
  en verde los 3 años.

`bp6.py gates_en --dir /tmp/bbq-dry --parcial --solo G1,G3,G4,G5,G6,G7`: **TODO VERDE** (722 fórmulas; 68 tareas [11, 13,
12, 10, 12, 10]; 16 hojas Letter; 202 valores bajo DV; 8 rangos de CF; caché = referencia ES recalculada, 0 diferencias;
113 valores del caso, 0 calibraciones). Barrido de las 450 piezas ya en EN del dry-run (GM, GRC-plan, GX) contra cifras
prohibidas y `RX_BBQ_NO`: 0 fugas reales (los 14 avisos son celdas D19 aún en ES del FT, «Fichero v1.1» / «Ticket medio
food truck», que reescriben los redactores).

## 4. Decisiones y desviaciones de la SPEC

1. **Recuentos de grupos** (SPEC D101: GM 331 · GRC 92 · GBQ-plan 121 · GBQ-check 272): GM **312**, GRC-plan **79**,
   GBQ-plan **128**, GBQ-check **275** (las 272 celdas de tarea + 3 textos del checklist) y GX **165**, porque (a) la
   adopción de «BBQ packages / Add-ons» (D103) y los rótulos de D102-D103 fijan ≈ 22 rótulos más en POR_CELDA / FIJOS, y
   (b) **51 celdas forzadas** en vez de 41: fuera P&L A10/A11 (POR_CELDA) y dentro C4, C5, C27, C58, C62 (cambian con el
   caso BBQ) y C7/C8 («enter 0.15 for 15%»), C11/C12 («food + beverage = 100%»), C15 (desechables sin leña), C18 («The
   example (2.5%)», el M4 del bar móvil) y P&L F33 (pest control → smoker repair): sus EN del catering mentían con el caso.
2. **Calibración** (§3): ninguna; préstamo $101,000 (research ≈ $98,500).
3. **D19**: las 5 filas con propuesta del catering se quedan en SU fila (58 neto, 62 marketplace, 63 depósito → 50 %
   nonrefundable, 65 shared kitchen, 67 Insureon); las 9 nuevas incluyen, además de las 8 de D104, la del operador de Los
   Angeles (fiestas $40-58, bodas $65-85, mínimo 30, event fee).
4. **Checklist: 35 L · 25 A · 8 N** (inventario §5: 39 / 21 / 8): P1 fila 13 (contrato con depósito del 50 %
   nonrefundable, tramos y fuerza mayor por burn ban), P5 filas 8-9 (Zola; Thumbtack junto a ezCater) y P6 fila 11 (el
   saldo se cobra ANTES del evento: 72 h-14 días, Owen's) pasan de L a A. P4 fila 11 = seguridad del fuego (sustituye a
   la certificación de alcohol de los bartenders del catering).
5. **Calculadora — choque D105 / D106 / D111 resuelto así**: los $/lb crudos por línea están **en blanco** (ningún precio
   de carne tecleado, ni en la hoja principal ni en los ejemplos) y, **mientras falte alguno**, el coste de comida usa el
   **Kit estimate por invitado del paquete de research §5** ($6.50 drop-off · $8 buffet · $17 live-fire), con una fila de
   estado que lo dice («Missing: food cost uses the package estimate per guest») y una nota bajo la tabla de paquetes: no
   es un precio de carne. Con los 5 precios tecleados, coste = libras crudas × $/lb + (sides + pan y salsas) × invitados
   (el autotest lo prueba). Así los 3 ejemplos cumplen el ±10 % «con los valores por defecto».
6. **Calculadora — otras decisiones**: (a) 5 **líneas de carne con el corte elegible** (lista de los 13 cortes de la hoja
   de rendimientos) en vez de 5 categorías fijas, para que el live-fire use tri-tip, picanha o whole hog; por defecto
   brisket / pork butt / St. Louis ribs / chicken thighs / sausage (35/30/15/15/5 %). (b) El live pit fee y el event fee
   van **encima** del precio por invitado (en el bar móvil el bar fee se restaba): el margen calculado sigue ≥ objetivo.
   (c) La **calidad de tri-tip, picanha y tomahawk = 145 °F** y la del turkey breast = 165 °F: la calculadora nunca
   propone un punto por debajo del mínimo del Food Code (nota: menos hecho, «check your county rules»). (d) La boda de
   ejemplo usa el paquete full-service buffet + live pit (SPEC: «full-service + live pit on site») con su $8, no los $11 de
   bodas de research §5. (e) Tramos de cancelación 60 / 30 / 14 días con 50 / 75 / 90 / 100 % (Kit estimate; estructura
   ES sin huecos, comprobación de días descendentes). (f) Sin columna de gratuity: la voluntaria queda fuera (Rev. Rul.
   2012-18), como pide D105.
7. **Docx §9**: 102 commissary y nada de casa · 103 permisos, CFPM, food handlers, plan HACCP con 145 / 155 / 165 °F, 135
   °F, enfriado y recalentado, approved source · 104 trailer en el evento = mobile food unit · 105 fuego y burn bans ·
   106 sales tax + service charge + alcohol solo del cliente · 107 empleo y seguros · 108 trailer y van en el DMV + nota
   UK (el inventario §6 ponía el alcohol en 105; va en 106 para que las temperaturas entren en 103 sin pasar de largo).
8. **`FUENTES_CIFRAS`** = research y SPEC de BP, del catering (BP4) y del BBQ; NO la del bar móvil (sus cifras no son de
   este producto).
9. **`RX_BBQ_NO`** suma a D110 «grill master», «support kitchen», «grill / roast catering», «Cambro», los calcos
   «D-21 / D-14 / D-1» y kg / km / °C / litros fuera de paréntesis; la lista blanca va por lookbehind / lookahead
   («BBQ food trucks», «Food Truck Business Plan Kit» del cierre, «cocktail hour», «AI Chef Pro») y por excepción de
   texto (la firma; «chefs and head cooks» junto a OEWS / BLS / 35-1011). «lechón» lo rechaza el detector común de
   español (tilde): el brief lo avisa.
10. **Las pistas D18 no llegan al revisor de GRC-plan** (`preparar_tandas` solo le pasa id, es, en_actual y dónde): la
    coherencia por fila de la tabla D18 (39, 41-44, 49, 50) va en el brief, tanda (a).
11. **Fuera de mi alcance (paso 3/F3)**: `bbq-catering-business-plan` en `PRODUCTOS_LETTER` de `censo-entregables.py` y
    en `EXCLUIDOS` de `postprocess-transversal.py` (G9 de `gates_en`); hoy se pasa con `--letter --only`.

## 5. Calculadora D105-D106 (`calculadora_bbq.py` → `astro-site/public/dl/bbq-catering-business-plan/bbq-catering-pricing-calculator.xlsx`)

5 pestañas, **422 fórmulas**: «Pricing Calculator» (49 entradas verdes con DV + 12 en la tabla de paquetes: paquete de una lista de 3 leída de la
tabla de paquetes, 5 cortes de la lista de la hoja 2, Yes/No del live pit y del sales tax, enteros, importes ≥ 0, $/lb en
blanco permitido, porcentajes 0-1, comisión ≤ 30 %, margen ≤ 65 %, días 1-730; salidas: libras crudas y piezas por
línea, estado de los precios, costes, precio por invitado y por lb cocinada, live pit fee, subtotal, service charge,
impuesto, total, depósito del 50 %, saldo, comisión, margen calculado, pit crew y servers sugeridos, 4 retenciones por
tramo) · «Meat Yield & Smoke Schedule» (13 cortes; pit °F y (°C), **calidad (Kit estimate) y mínimo del Food Code en
columnas distintas**, horas, reposo, rendimiento con su fuente, raciones por lb cruda, lb cocinadas por pieza, **«Start
the pit by»** y día; notas de non-intact 155 °F, hot holding 135 °F, enfriado 70 °F en 2 h y 41 °F en 6 h, recalentado
165 °F, approved source del whole hog) · «Shopping List by Guest Count» (tu evento + 40 / 80 / 150 / 300 editables:
libras y piezas por línea, sides en galones y half pans, rolls, salsa, leña, butcher paper, hotel pans, hot boxes, pit
crew y servers) · «3 Example Quotes» · «Instructions» (oz por invitado con fuentes, Food Code, service charge y gratuity,
sales tax, live pit on site y el condado, nota UK, Kit estimates, firma, versión y aviso). docProps D20, Letter + ajuste
+ pie, hojas protegidas sin contraseña.

| Ejemplo (Kit estimate; sin precios de carne) | Inv. | Lb crudas | Coste | Precio/inv. | Con tarifas | Línea §8 | Subtotal | Total | Margen |
|---|---|---|---|---|---|---|---|---|---|
| Corporate drop-off (mín. 20) | 40 | 27.1 | 537.44 | **22.50** | 22.50 | $22 (+2.3 %) | 900.00 | 972.00 | 40.3 % |
| Graduation party, staffed buffet (mín. 30) | 70 | 63.3 | 1,200.20 | **34.50** | 34.50 | $35 (−1.4 %) | 2,415.00 | 2,608.20 | 50.3 % |
| Wedding, full-service + live pit $650, service charge 10 % (mín. 75) | 130 | 117.5 | 3,182.68 | **49.00** | 54.00 | $52 (−5.8 % / +3.8 %) | 7,020.00 | 8,339.76 | 54.7 % |
| Hoja principal por defecto (full-service buffet ≈ el caso: 75 inv.) | 75 | 67.8 | 1,363.15 | 33.50 | 33.50 | — | 2,512.50 | 2,713.50 | 45.7 % |

**Autotest** (`bp6.py calculadora`): inject_cache 422 fórmulas, 0 fallos de pycel; **581 comprobaciones** pycel + caché =
Python en las 4 pestañas de cálculo (hoja principal, rendimientos y horario, lista de la compra, 3 ejemplos y su
equivalente con tarifas) + **el paquete live-fire, el interruptor del live pit y los 5 precios de carne tecleados**
probados con `set_value` en la hoja principal (cada uno con un compilador nuevo); mezcla = 100 %, margen ≥ objetivo,
ejemplos a ±10 %, ningún $/lb tecleado, calidad y mínimo en columnas distintas, 0 cadenas vacías, 0 verdes bloqueadas,
sin «€» ni símbolo en formatos, 0 español / no latinos / cifras prohibidas / `RX_BBQ_NO` / anclas → **VERDE**.
`censo-entregables --fail --letter --only bbq-catering-business-plan`: 0 defectos; `gate-no-latinos --only`: 0. sha256
(Mac = VPS) `c07c582b937a60127dd65dadf0bf5e6b6bc2f96ac4f6421211b429e3d496ca63`.

## 6. Comandos para seguir

```bash
# PASO 2 — redactores Sonnet (Mac, máx. 2 a la vez, istats < 62 °C; BRIEF-TRADUCTORES.md, secciones 0 y 1 + la tanda)
#   tanda 1: (a) GBQ-plan + revisión GRC-plan ‖ (b) GBQ-check · tanda 2: (c) bbq_a ‖ (d) bbq_b
B=scripts/productos-digitales/business-plans-en-6
python3 $B/bp6.py check_textos --tanda GBQ-plan     # | GBQ-check | bbq_a | bbq_b
python3 $B/bp6.py preparar_tandas && python3 $B/bp6.py check_textos --tanda GRC-plan   # tras GRC-plan.revision.json
python3 $B/bp6.py check_textos --todas

# PASO 3 — VPS: aplicar (sin calibración), ensamblar, gates
ssh vps
cd /root/wt-bbq && git checkout -q -- . && git pull --ff-only && cd scripts/productos-digitales/business-plans-en-6 && PY=/root/venv-guias/bin/python
$PY bp6.py aplicar_en --idempotencia --json /tmp/bbq-real.json   # 2 xlsx en dl/bbq-catering-business-plan/ + cifras_caso.json
$PY bp6.py ensamblar_docx --plan bbq                             # tras bbq_a + bbq_b
# G9: antes, bbq-catering-business-plan en PRODUCTOS_LETTER (censo-entregables) y EXCLUIDOS (postprocess-transversal)
$PY bp6.py gates_en && $PY bp6.py gates_en --autotest && $PY bp6.py ensamblar_docx --autotest --dir /tmp/bbq-docx-at
$PY bp6.py calculadora --autotest && $PY bp6.py barrido           # → entregables_bbq.json
# regresión §2; vuelta por scp (sha256 iguales); commit desde el Mac; VPS limpio (borrar los generados sin seguimiento)
# si cambian FIJOS / POR_CELDA / zonas / grupos / pistas / FORZAR: $PY bp6.py extraer_textos > /tmp/bbq-ext.txt y
#   extraer_docx (VPS) y preparar_tandas (Mac); si cambia el catering publicado, bp6.py verificar avisa (sha256)
```

VPS: `/dev/null` es un fichero normal (redirigir a `/tmp/*.txt`); antes de cada `git pull`, `git checkout -- .` (los
JSON generados que ya están en git salen idénticos) y borrar los ficheros generados sin seguimiento tras comprobar su sha256.

## 7. Riesgos para los redactores (pasos 2-3)

1. **Redactar, no traducir**: el `es` puede ser del food truck, del catering o del parrillero; **la pista manda**. En el
   checklist, las 35 «[sobrevive]» parten de la propuesta; las 25 «[sobrevive con ajuste]» la cambian de palabras y las 8
   «[nueva]» son otra tarea. La revisión final debe leer el checklist entero (275 celdas) y la tabla D18 revisada.
2. **Temperaturas**: calidad (brisket ≈ 203 °F) y mínimo del Food Code nunca en la misma frase sin decir cuál es cuál;
   inyectado = non-intact, 155 °F; enfriado con la redacción de una sola regla («to 70 °F within 2 hours and to 41 °F
   within a total of 6 hours»). «window» salta en el gate («a 2-hour window»).
3. **Gate `RX_BBQ_NO`**: trampas típicas: «pickup truck» (→ «pickup» / «tow vehicle»), «chef» (→ pitmaster; «chefs and
   head cooks» solo en la fila 64 de la D19), «stations» (solo «carving station»), «refrigerated van», «cocktails» (solo
   «cocktail hour»), «bartender», «Cambro», «D-21», kg y °C fuera de paréntesis, «lechón».
4. **Legal sin cifras inventadas**: MFU (TX sí; FL y NC parecido; CA sin verificar), burn bans y carpas → «ask your
   county» / «check with your fire marshal».
5. **Realismo (D100)**: 150 eventos = operador a tiempo completo con pit cook y $10K de marketing, no la media del primer
   año (≈ $300K el año 1); holgura 18 % (caída absorbible 15 %); el pesimista agota la caja (−$8,085) y el docx lo dice.
6. **[98]**: `{{cobro_dias}}` para los cobros y `{{pago_dias}}` para los pagos a proveedores (la errata del ES, D113).
7. Cifras de mercado solo de research «leída» (check_textos lo comprueba); D19: 2 de 14 filas son «Kit estimate» (62
   marketplace y 68 leña / personal).
8. Si se rehace la extracción, los ids de `textos_es.json` pueden moverse y las salidas de los redactores dejan de casar.
