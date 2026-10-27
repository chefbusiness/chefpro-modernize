# Wedding Venue Business Plan Kit (EN) — F2 (entregables) · notas

> Sesión Claude Code, 27-oct-2026. **Paso 1a de la F2-EN** (SPEC delta §10, D178): conjunto «wed», clones de la Pizza EN
> con la estructura de la panadería, caso US D160 + D15, tokens D170, `RX_WED_NO` y cifras prohibidas D173, extracción del
> ES LIVE, `preparar_tandas`, dry-run, regresión y la **tanda 1** preparada (2 traductores). Implementador único (opus), sin
> subagentes. Código en el Mac (worktree `wt-wedding`); lo que abre xlsx/docx, en el **VPS** (`/root/wt-wedding`, venv
> `/root/venv-guias`, temporales `/tmp/wed-*`). Rama `feat/wedding-venue-business-plan-en`.

## 1. Cómo se montó el conjunto «wed» (libro gemelo de la PANADERÍA ES; texto del motor = el EN de la PIZZA)

`BP_CONJUNTO=wed` → `mapas_wed.instalar(M)`, `mapas.DATOS = business-plans-en-9/`, lanzador `bp9.py`. **Único cambio en
código común**: la rama `elif CONJUNTO == 'wed'` de `business-plans-en/mapas.py` (+ el mensaje de error). Fuente ES en UN
sitio: `mapas_wed.FUENTE_ES` = `$WED_FUENTE_ES` o `astro-site/public/dl/plan-negocio-finca-eventos-bodas` (el LIVE).

| Fichero | Qué lleva |
|---|---|
| `mapas_wed.py` | Producto D156, libros `WEDP`/`WEDC`, pestañas D169 (≤ 31), 84 tareas 12/16/15/13/14/14, parches **E2 `G14`** y **E4 `Personal!C11`** (sin E3/E5), versión WEDP 53 / WEDC 11 (E1 en A54 / A12), zona D19 por cabecera (filas 35-48), docx de PAEL/PIZ (131, `ULTIMO_9` 108, tandas `wed_a`/`wed_b`), `PRESTAMO_SEMILLA` 460,000, autotest, grupos y **diccionario por TEXTO** (D161): Pizza EN (GM, GR, GPIZ-*) → BP2 (GM, GPAN, GREST, GN) → BP (GM, GCAF, GFT) → BBQ → PAEL; primero el ES exacto y luego el normalizado con el VOCABULARIO de la finca invertido (`normalizadores()`, de `inventario_delta.py`); `RX_REESCRIBIR` (vocabulario y caso de restaurante: clasifica propuestas); CLAVES `—` → `☐` (DV del checklist, como la pizza); sha256 del diccionario de la Pizza EN en `sha_piz.json` |
| `datos_wed.py` | FIJOS (D162 A1-A3 y las 19 partidas + A26-A28, D163 P&L A2/A10/A11/A13-A16/A22/A24-A35/A55 y los 6 puestos, títulos, D19), 15 POR_CELDA (`12-Month Cash Flow!O5`/`O13`/`O16`/`A34` D167/D164, `3-Year P&L!F10`/`F11` D164, `0. Assumptions!A62`/`C62`/`A63`/`C63` D164, `Staffing!A28`/`A29`), `REGLA_UNIDADES` (sq ft con m² entre paréntesis), `cifras_prohibidas()` (D173: 56 importes ES ≥ 10.000 € menos los del caso US y de research/SPEC + frases ES + caso de la Pizza EN) + `RX_WED_NO`, **135 tokens** (los del motor con los rótulos de la finca + 19 partidas + fianza, renta previa, imprevistos, bases de amortización, mezcla, comisión, intermediarios, horas por evento, holgura A2/A3, DSCR A2/A3, exceso de fondos y los derivados `ingreso_evento`, `equilibrio_eventos`, `equilibrio_caja_eventos`, `eventos_equivalentes_a2/a3`, `invitados_ano`), `DOCX_FIJOS` (cierre: Catering Business Plan Kit · Mobile Bar Business Plan Kit · Catering Checklists Kit Pro), 61 `DOCX_NOTAS` (sección + FORMA de la Pizza EN; §9 = 102-108 con los temas de D170 y las decisiones de orquestador; 108 con la nota UK), pistas (caso D160, inversión D162, 14 filas D19 de D165, **las 84 tareas US de D169** por celda, 33 por texto), glosario research §9, caso US (`VALORES_EN`, 123 celdas) y `CALIBRACION_D15` (1) |
| `bp9.py` | Lanzador (copia de `bp8.py`) + `verificar [--fijar]`, `derivar_formulas`, `calibracion`, `barrido`, `check_contrato` (y `calculadora` / `contrato`, que apuntan a `calculadora_wed.py` / `contrato_wed.py`: **aún no existen**, pasos 1b y 3) |
| `derivar_formulas_wed.py` + `formulas_wed_manual.py` → `formulas_wed.json` | 16 fórmulas con texto: **9 derivadas** de la Pizza EN (D26, D27, D30, D31, D33, D36, D37, F18, `Personal!A2`) y **7 manuales** (C9, D28, D38, F13, F14, `Break-Even!A26`, `12-Month Cash Flow!O11`); 0 pendientes |
| `calibracion_wed.py` | D15 de D160 sobre el informe de `aplicar_en --json`: holgura ≥ 15 %, **DSCR ≥ 1.30**, saldo > 0, cobertura ≥ 98 %, neto año 3 ≤ 16 %, exceso de fondos 0-5 %, umbrales D165 en verde; dice la palanca si falla |
| `barrido_wed.py` | Barrido independiente (`--dir`, `--parcial`) contra `RX_WED_NO`, cifras prohibidas, español y no latinos |
| `check_contrato.py` | Prepara `tandas/contrato_{1,2}.entrada.json` (`--preparar`) y valida `textos_en/contrato_en_{1,2}.json` (`--parte N` / `--todas`): estilos, tokens, español, no latinos, `cifras_prohibidas`, cabecera legal literal, «non-refundable» sin la tabla, Cooling-Off afirmada, normas «(resumen)» citadas, cláusulas obligatorias de D171 |
| `BRIEF-TRADUCTORES.md` | Tanda 1 (2 traductores) y tanda 2, con el glosario de research §9 pegado entero (§1) y el comando de verificación de cada traductor (§5) |

**Grupos** (`textos_es.json` del ES LIVE, 879 cadenas):

| Grupo | Cadenas | Palabras ES | Qué es | Va a |
|---|---|---|---|---|
| GM | 306 | 3,063 | ES exacto de una cadena GM del motor (Pizza EN 2.2 o BP/BP2) con EN limpio | nadie: `textos_en/GM.json` escrito (check_textos OK) |
| GR | 11 | 256 | EN de otro kit casado por texto o tras normalizar (solo plan) | `textos_en/GR.json` escrito; revisión en el traductor A |
| **GWED-plan** | 187 | 3,967 | texto libre del plan + 21 con propuesta sucia (FOOD/BEVERAGE, covers, shift…) + **55 celdas D19** (14 filas × 4, menos `A41`, que es FIJO) | tanda 1, traductor A |
| **GWED-check** | 241 | 2,720 | las 84 tareas y sus cabeceras; 19 con propuesta de otro kit (el checklist reutilizable no GM va aquí, no a GR: cada fila lleva su tarea US de D169) | tanda 1, traductor B |
| GX | 134 | 1,347 | pestañas, CLAVES, FIJOS, POR_CELDA, versión, pie, docProps | nadie |

Contrato (D171, `../plan-finca-eventos/textos/contrato_es.json`): parte 1 = portada + Modelo 1 + Anexo (102 párrafos, 3,324
palabras) → traductor B · parte 2 = Modelo 2 (48 párrafos, 1,419 palabras) → traductor A. Word: `wed_a` 29 párrafos / 3,071
palabras · `wed_b` 32 / 3,551 (tanda 2).

## 2. No regresión (VPS, con la rama `wed` en `mapas.py`; `/tmp/wed-regresion.sh`, no versionado = `/tmp/regresion-piz.sh` + `bp8 piz`)

Por conjunto: `mapas` + `aplicar_en --dry-run` + `ensamblar_docx --salida` en `/tmp/wed-regresion/` y **sha256 CANÓNICO**
(`/tmp/wed-canon.py` = `/tmp/canon_piz.py`) frente a `dl/`: FT/CAF, REST/PAN, BAR, CAT, MBAR, BBQ, PAEL y **PIZ** → `mapas`
0 errores en los 8 · **30/30 ficheros IGUAL**, 0 DISTINTO, todos rc 0 · `git status` del VPS limpio tras la regresión.

## 3. Caso US, dry-run y calibración D15 (`bp9.py aplicar_en --dry-run --parcial --idempotencia --salida /tmp/wed-dry --json /tmp/wed-dry.json`)

Research §8 / SPEC D160-D167 tal cual (vuelta 0): préstamo de punto fijo **$470,000** (semilla 460,000 → 470,000 →
470,000; research estimaba ≈ $458,000: el fondo de maniobra por fórmula es $99,216 y no $87,500). Todo D15 en verde salvo
el semáforo del margen bruto: el caso da **83.4 %** (variables 16.6 %, las de research §8) frente al umbral de D165 (85 %,
Kit sin fuente). **Vuelta 1 (única)**: el umbral, no el caso:

- **WEDP PyG 3 Años!E51** = 0.80 (umbral del margen bruto; D165 decía 85 %): el del ES (80 %); un venue con coste directo,
  comisiones y tarjeta ronda el 83-84 %. Ninguna cifra del caso cambia.

Resultado (`/tmp/wed-dry/cifras_caso.json`, `calibracion_wed.py` **VERDE**):
- Ventas **$612,000** / $660,960 / $694,008 (90 guests × $68 × 100 events; $72.79 por invitado con sales tax) · 88 % venue
  rental & services / 12 % caterer commission.
- CAPEX **$570,500** (19 partidas $503,500 + imprevistos de obra $37,000 por fórmula + fianza $10,000 + 4 meses de renta
  previa $20,000) + fondo de maniobra $99,216 = **$669,716** (= necesidad de caja: sin impuesto recuperable) · propios
  $200,000 (30 %) + préstamo **$470,000** al 10 % a 10 años (cuota $76,490) · exceso de fondos 0.04 %.
- Margen bruto **83.4 %** · coste directo 10.6 % · personal **31.4 %** ($191,862; 3.70 FTE con E4, cobertura 119 %) · renta
  9.8 % · EBITDA $160,791 (**26.3 %**) · D&A $40,990 · intereses $47,000 · neto **$54,600 (8.9 %)** / 12.3 % / **14.2 %**.
- Equilibrio contable $524,751 (**86** eventos del tamaño medio; 78 invitados por evento) · de caja $510,969 (**84** eventos;
  76 invitados) → holgura **20 %** (27 % / 31 % años 2-3) · **DSCR mín 1.86×** (2.18× año 2) · saldo mínimo **$66,103** (Month
  2) · payback > 3 años.
- Pesimista (85 · $60 · 85) **$433,500**, resultado −$76,140 y caja estimada al cierre del año 1 **$34,576** (no se agota) ·
  optimista (95 · $72 · 115) $786,600 y +$218,487.
- Umbrales D165 (E51 80 % · E53 15 % · E54 35 % · E55 12 % · E56 5 %): en verde (margen bruto, personal y neto los 3 años;
  coste directo y renta del año 1, los peores).

## 4. Gates del paso 1a (VPS, sobre el dry-run)

| Comprobación | Resultado |
|---|---|
| `bp9.py mapas` (autotest + cruce con el censo + `verificar`) | **0 errores** (16 pestañas, 9 claves, 105 fijos, 16 fórmulas EN, 123 valores, 135 tokens) · verificar OK: zona D19 55 celdas en GWED-plan sin propuesta, 8 sha256 de la Pizza EN OK; 7 avisos (FIJOS del motor sin uso) |
| `extraer_textos` · `extraer_docx` | 879 cadenas · docx 131 párrafos (61 traducibles, estilos = PAEL) · `extraer_docx` da **ROJO (1)** solo por «la página no es US Letter»: el Word ES es A4 y `ensamblar_docx` pone Letter siempre (l. 171-172): benigno, no se toca el común |
| `aplicar_en --dry-run --parcial --idempotencia` | préstamo $470,000 en 2 vueltas · idempotencia **0 diferencias** · inject_cache 699 + 12 fórmulas, **0 fallos de pycel** · D15 sin fallos |
| `bp9.py calibracion` | **VERDE** (holgura 19.8 %, DSCR 1.86, saldo $66,103, cobertura 119.1 %, neto año 3 14.2 %, exceso 0.04 %, D165 verde) |
| `gates_en --parcial --solo G1,G3,G4,G5,G6,G7` | **TODO VERDE**: G1 734 fórmulas + 84 tareas [12, 16, 15, 13, 14, 14] · G3 16 hojas Letter · **G4 239 valores bajo DV** (CLAVES `—` → `☐`) · G5 8 rangos CF · G6 0 diferencias · G7 123 valores, 1 calibración citada |
| `bp9.py barrido --parcial` (piezas ya en EN) | 1,285 piezas · **0 fallos** (RX_WED_NO, cifras ES / Pizza, español, no latinos); 498 piezas aún en ES = pendientes |
| `check_textos --todas` (Mac) | GM 306 y GR 11: **OK (0 errores)**; 5 avisos de longitud en GM |
| `check_contrato` con defectos inyectados | caza «non-refundable» solo, «The FTC Cooling-Off Rule applies…», finca/canon/señal/12 %, `{{token}}`, «82 guests», §1671 y un estilo desconocido; deja pasar «ask your attorney whether the FTC Cooling-Off Rule … applies» |
| 2.ª pasada (`aplicar_en --dry-run --parcial` en `/tmp/wed-dry2`) | sha256 canónico **IGUAL** en los 2 xlsx; `cifras_caso.json` igual salvo `generado` |

Ficheros de prueba (solo en el VPS): `/tmp/wed-dry/wedding-venue-business-plan/wedding-venue-financial-projections.xlsx`
(`4bf3c62d…`), `…/wedding-venue-startup-checklist.xlsx` (`76f32f22…`), `/tmp/wed-dry/cifras_caso.json`, informe
`/tmp/wed-dry.json`. sha256 Mac = VPS: `censo_es.json` `e8c91c29…`, `textos_es.json` `1a2b0ab3…`, `docx_es_wed.json`
`c5d82440…`, `formulas_wed.json` `f9bc7a32…`; `textos_en/GM.json` `92ff393e…`, `GR.json` `beb04244…`.

## 5. Decisiones fuera de la SPEC y defectos

1. **Calibración** (§3): umbral E51 80 % en vez de mover el caso (las variables de research §8 dan 83.4 %).
2. **Tabla D19** con las filas del ES: `A41` («Canon del catering exclusivo») coincide con el rótulo del P&L y es FIJO
   («Caterer commission (exclusive caterer)»), así que cada tema de D165 va a la fila de su tema ES y «Venue rental fee»
   ocupa la de la comida testigo (46).
3. **Checklist reutilizable no GM → GWED-check** (con propuesta), no a GR: la tarea US de D169 (pista de cada fila) manda
   sobre el EN de otro kit. Las 4 tareas cuyo ES es un rótulo de la inversión (fase 3 filas 8, 11, 12, 16) salen con ese
   FIJO (sprinklers, generator, HVAC, sound), que ya es su tarea US.
4. **Contrato en la tanda 1** repartido para equilibrar palabras (A ≈ 5.6 K, B ≈ 6.0 K); `contrato_wed.py` (molde = el docx ES
   del contrato en Letter, docProps EN, concatena las 2 partes, gates) queda para el paso 3. La **calculadora** (D168) no va
   en tandas: es código (`calculadora_wed.py`, paso 1b).
5. **Decisiones de orquestador del 27-oct** (SPEC-delta §11) volcadas en pistas, POR_CELDA, notas del Word y reglas del
   contrato: arrendamiento ≥ préstamo contando prórrogas («SBA lenders typically require…; confirm with your lender»),
   purchase option / right of first refusal, consentimiento a la obra y a la garantía, TI allowance; Cooling-Off solo como
   «ask your attorney whether…»; lo «(resumen)» fuera de las cifras rotundas (sin MO/NY en las notas de sales tax, sin The
   Knot en D19, sin 40 CFR 141.2 ni umbrales de sprinklers con cifra).
6. **Defecto de la Pizza EN publicada** (para el orquestador): el aviso de error de la DV de su checklist dice «✓, —, N/A …
   — = pending» mientras la lista es «✓,☐,N/A» (c0659 de `business-plans-en-8`). En el wed va con «☐» (pista por texto).
7. **ES**: el Word ES es A4 (el de la pizza era Letter), sin efecto en el EN; los demás defectos ES, los de inv. §8.

## 6. Siguiente (orquestador)

**Tanda 1** (2 sonnet en paralelo, `BRIEF-TRADUCTORES.md` §2-§3): A = GWED-plan + revisión de GR + contrato parte 2 ‖ B =
GWED-check + contrato parte 1, cada uno con su comando de §5. Después (Mac): `bp9.py preparar_tandas && bp9.py check_textos
--todas && bp9.py check_contrato --todas`; ‖ 1b `calculadora_wed.py` (D168). Luego VPS:

```bash
cd /root/wt-wedding/scripts/productos-digitales/business-plans-en-9 && PY=/root/venv-guias/bin/python
$PY bp9.py mapas > /tmp/wed-mapas.txt && $PY bp9.py aplicar_en --idempotencia --json /tmp/wed-real.json > /tmp/wed-aplicar.txt
$PY bp9.py calibracion /tmp/wed-real.json        # 2 xlsx en dl/wedding-venue-business-plan/ + cifras_caso.json
```

→ **tanda 2** `wed_a` ‖ `wed_b` → `ensamblar_docx --plan wed`, `contrato_wed.py`, `calculadora --autotest`, gates D172 (alta
en `PRODUCTOS_LETTER` y `EXCLUIDOS` antes de G9), barrido, `/tmp/wed-regresion.sh`, 2.ª pasada, revisión D174.
