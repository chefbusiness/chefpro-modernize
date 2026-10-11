# Parrillero / Asador ES 2.2 — F2 paso 1 (implementador) · notas y comandos del paso 3

> Sesión Claude Code, 12-oct-2026. SPEC: `SPEC-2_2.md` (D1-D16). Código en el Mac; todo lo que abre xlsx/docx, en el
> VPS (`/root/wt-par`, venv `/root/venv-guias`, scratch **`/root/tmp-par-f2/motor`**: el resto de `/root/tmp-par-f2`
> es del agente de la calculadora y de `arreglos_d9.py`). **Nada escrito todavía en `dl/`.** Fuera de este paso
> (otro agente, en paralelo): `calculadora_par_es.py`, `arreglos_d9.py` y la tabla nueva del manual técnico.

## 1. Qué hay (todo en verde con lo escrito)

| Pieza | Fichero | Estado |
|---|---|---|
| Contenido (D2, D4-D7) | `planes-v2_0/contenido_plan_negocio_parrillero_asador_eventos/a.py` (clon del paellero) | caso del research; rótulos solo por `VOCABULARIO` («cocina de apoyo», «asado para llevar»); nota M1 del Word corregida; «versión 1.1» como anterior, intacta (D2) |
| Semilla + checklist (D3, D10) | `semilla_par.py` + `datos_checklist.py` (83 tareas 12/16/14/10/16/15, pestañas ≤ 31) | copia del FT ES v2.2; `Instrucciones!A3` y docProps del parrillero desde el día 1 (B1 del catering) |
| Motor | `ciclo.sh` → `main.py --dry-run --origen` | **TODO VERDE**: 13/13, idempotencia 0, caché 0 fallos, blancos 0, censo 0, demos OK (30/30 moldes) |
| Tokens + D15 | `cifras_par_es.py` → `cifras_caso_es.json` (84 tokens, en el repo) | **VERDE**, con las holguras de los años 2 y 3 (informativas) y `DSCR_A3` |
| Docx (D11) | `tandas_docx.py` + `BRIEF-REDACTORES.md` + `docx_par_es.py` + `fuente_par_11.json` | tandas listas (`tandas/par_es_{a,b}.entrada.json`); ensamblado `--parcial` VERDE (**11 H1**, A4, autor AI Chef Pro); anexo del paellero trasplantado y adaptado a la brasa |
| Barrido | `barrido_es.py` (lista de `tandas_docx.PROHIBIDOS`) | los 2 xlsx rehechos: 0 |
| Restos FT + catering + paellero | `../catering-es-2_0/gate_restos_ft.py` con las opciones del §4 | sobre los 3 rehechos (scratch): VERDE |

## 2. Caso calibrado (Excel del dry-run, `cifras_caso_es.json`)

- **Actividad**: 95 eventos × 80 invitados × 25 € sin IVA (27,51 € con IVA; evento medio 2.000 €). Ventas 190.000 € / 205.200 € / 215.460 €. Crecimiento: invitados por evento 80 → 86,4 → 90,7 con los mismos eventos.
- **Margen y costes**: margen bruto 57,7 %, mercancía 31,8 %, personal 57.983 € (30,5 %), fijos totales 92.616 € (amortización 4.912 €, intereses 4.251 €).
- **Resultados**: RAI 17.090 € / 19.867 € / 20.538 €; neto **14.527 € (7,6 %)** / 16.887 € / 15.403 € (el año 3 baja: el IS pasa del 15 % de nueva creación al general).
- **Inversión**: 76.522 € (compras 54.596 € + fondo de maniobra 21.926 €). IVA soportado 10.835 €. Necesidad de caja **87.357 €**.
- **Financiación**: 22.000 € propios + **préstamo 65.400 €** (calibrado; +43 €, 0,05 %), 6,5 %, 6 años con 1 de carencia; cuota 15.737 €.
- **Ratios**: DSCR año 2 **1,66**, año 3 / mínimo **1,51**. Saldo mínimo de tesorería 6.145 € (mes 4). Payback «Más de 3 años» (2,2 sobre las compras). Cobertura de horas 157 %.

**Equilibrio** (eventos al año = token derivado sobre el evento medio de 2.000 €):

| | Invitados por evento | Eventos al año | Ingresos | Holgura |
|---|---|---|---|---|
| Contable, año 1 | **68** (67,5) | **81** (80,2) | 160.401 € | 18,5 % |
| Caja, año 1 (carencia) | 64 | 76 | 151.894 € | **25,1 %** |
| Caja, año 2 (con principal) | — | 92 sin crecer | 182.179 € | **12,6 %** |
| Caja, año 3 | — | **97** sin crecer (> 95) | 192.570 € | **11,9 %** |

**Escenarios**: pesimista (80 eventos · 75 invitados · 23 €) −12.934 € · optimista (110 · 85 · 26 €) +40.588 €.

## 3. Desviaciones de la SPEC (para decidir)

1. **Préstamo de 65.400 €**, no ≈ 62.000: la necesidad del libro es de 87.357 € (el research estimaba ≈ 84.000: el IVA de la inversión sale en 10.835 € y el fondo en 21.926 €).
2. **Comisión del asado para llevar: 10 %** (research 2 %). La SPEC D4 lo permite («sube si lo exige la demo»): sin ella, la demo §2.11.5 no encontraba ventana.
3. **Fijo «Mantenimiento de extintores y revisión del gas»: 170 €** (research 300 €; fijos propios 10.920 €). La demo §2.11.5 (las tres ramas del IS) tiene aquí una ventana de **128 €**: el RAI del año 3 crece menos que el del año 2. Con 67 invitados, el RAI1 tiene que caer entre −803 y −675 €. Es el gotcha del paellero, pero con 130 € en vez de 100.
4. **Remolque-parrilla amortizado como maquinaria** (10 años), no como vehículo. Así los imprevistos del 8 % caen solo sobre la furgoneta y la rotulación: 1.696 € (research 1.600).
5. **Inversión en 14 filas**: «marca, web, fotos y dossier» y «lanzamiento» van juntas (4.500 €). Total 49.900 €, como el research.
6. **Holguras de caja de los años 2 y 3: 12,6 % y 11,9 %** (< 15 %). **Sin crecer, el año 3 necesitaría 97 eventos y el plan tiene 95**: el crecimiento lo cubre, pero es más justo que el paellero (102 de 105). Se informa (D4) y la pista §8 manda contarlo. Opciones si John quiere margen:
   - (a) aceptarlo y explicarlo, como en el paellero;
   - (b) +5 eventos de empresa (100 eventos; regla del research);
   - (c) carencia de 2 años.

   Cualquier cambio del caso obliga a volver a encajar la demo §2.11.5 (punto 3).
7. **Payback en texto** («Más de 3 años»): la pista §8 lo trata como texto. `PAYBACK_CAPEX` = 2,2 años.
8. **Cobertura de horas 157 %**: `personas_franja` = 3 (titular, segundo parrillero y un auxiliar en el evento medio), 8 h por evento. El titular va a jornada completa.
9. **Umbral de margen bruto 55 %** [estimado]: el research no lo daba. El caso da 57,7 %.
10. **«retención» en el barrido (D15)**: solo se prohíbe la afirmación falsa de la 1.1 (`retención del 7/15`, `7 %/15 %`). El checklist F1 y las referencias del Excel dicen, como pide D6, que las facturas **no** llevan retención (RIRPF art. 95.6).
11. **Versión «2.2 · septiembre 2026»** en los xlsx y la portada del docx: la estampa el motor (aceptado en catering y paellero; la landing dice octubre).
12. **Dependencias con el otro agente** (tienen que coincidir):
    - Pista §6 del docx: tramos de cancelación con 60 días o más / 30-59 / 7-29 / menos de 7, y en empresa 30 días o más / 15-29 / 7-14 / menos de 7, más el 10 % si cancela el parrillero = `arreglos_d9.py` (F1-camino §6).
    - Escalado de la pista §6, de las referencias del Excel y del checklist F3/F4 = tabla nueva del manual (research §2): 350-450 g; 1 parrilla de 120 cm y 1 parrillero por cada 60-80 invitados (40-50 con cortes en mesa); ayudante desde 40; 0,7-1 kg de carbón por kg de carne.
    - El checklist remite a «la tabla de escalado del manual técnico».
13. **Docx p127**: la venta cruzada pasa a «→ Kit de Tareas: Asador» (`/kit-tareas-asador`, el que ya enlaza la landing).

## 4. Paso 3 — comandos (en orden)

```bash
# 0) Mac: 2 redactores Sonnet ‖ (par_es_a 29 ranuras / 2.954 palabras; par_es_b 32 / 3.765). Cada uno lee
#    BRIEF-REDACTORES.md y tandas/par_es_{a,b}.entrada.json, escribe textos/par_es_{a,b}.json y deja 0 errores:
python3 scripts/productos-digitales/parrillero-2_2/tandas_docx.py check --tanda par_es_a   # y par_es_b
# commit + push. En el VPS, el worktree tiene COPIAS sin commitear (scp) de los ficheros de este paso, idénticas
# a las del Mac: límpialas antes del pull (git checkout -- . && git clean -fd scripts/) y luego git pull
C=/root/wt-par/scripts/productos-digitales/parrillero-2_2; DL=/root/wt-par/astro-site/public/dl/plan-negocio-parrillero-asador-eventos
PY=/root/venv-guias/bin/python; export CLAUDE_SCRATCHPAD=/root/tmp-par-f2/motor
# 1) Excel: semilla + motor (TODO VERDE) y copia a dl/ con los MISMOS nombres (inject_cache ya hecho)
cd $C && bash ciclo.sh && grep "TODO VERDE" $CLAUDE_SCRATCHPAD/run.log
cp $CLAUDE_SCRATCHPAD/dryrun/plan-negocio-parrillero-asador-eventos/{plan-financiero,checklist-apertura}-parrillero-asador-eventos.xlsx $DL/
# 2) tokens + calibración D15 sobre el publicado (debe dar el mismo cifras_caso_es.json)
$PY cifras_par_es.py --xlsx $DL/plan-financiero-parrillero-asador-eventos.xlsx
# 3) docx (sin --parcial) y calculadora (script del otro agente)
$PY docx_par_es.py --salida $DL && $PY calculadora_par_es.py --salida $DL
# 4) D13: arreglos de texto + A4/docProps de los otros 7 (script del otro agente; desde la 1.1 de git)
$PY arreglos_d9.py --aplicar
# 5) gates D15
$PY ../catering-es-2_0/gate_restos_ft.py $DL \
  --rx-extra '\bpaell|paeller|\barroz|\barroces|socarrat|caldo de|estaci[oó]n(es)? tem[aá]tica|cocina central|catering tem[aá]tico|plan-catering|plan-negocio-paellero' \
  --excluir guia-tipos-parrilla-roadmap-food-truck.docx \
  --permitir 'roadmap food truck|food truck integrado \(escalado\)|escalar a food truck especializado en parrilla'
$PY barrido_es.py $DL/{plan-financiero,checklist-apertura}-parrillero-asador-eventos.xlsx $DL/calculadora-pricing-eventos-parrillero.xlsx $DL/plan-de-negocio-parrillero-asador-eventos.docx
$PY barrido_es.py --prohibidos $(ls $DL/* | grep -v guia-tipos)          # la guía: «food truck» y «camión» legítimos
cd /root/wt-par && $PY scripts/productos-digitales/censo-entregables.py --only plan-negocio-parrillero-asador-eventos --fail --quiet
$PY scripts/productos-digitales/gate-no-latinos.py --only plan-negocio-parrillero-asador-eventos
# (opcional) con el checklist nuevo ya en dl/, un ciclo más deja sin el RC-29 la lista de PENDIENTE (lee dl/)
# 6) Mac: scp de los 11 ficheros de dl/ y de cifras_caso_es.json; commit + push. VPS limpio:
#    git reset --hard origin/feat/parrillero-2-2 && git clean -fd && rm -rf /root/tmp-par-f2/motor
```

**Después**:
1. **Una revisión opus final** (D15):
   - recalcular a mano 3 cifras del P&L y el préstamo;
   - leer enteros el checklist, el docx y el contrato;
   - abrir Reglamento (CE) 853/2004 (temperaturas), RD 1086/2020 arts. 26.2 y 30, RIRPF art. 95.6 y LIVA art. 75.Dos.
2. **D14**, con la lista de `F1-camino-2_2.md` §7, cifras por token. Sin DSCR, payback ni saldos; la media de 25 € nunca sin su mezcla.
3. **D16** (correo, hueco 23-nov) y `gate-flujo-postpago --only plan-negocio-parrillero-asador-eventos` en preview y en LIVE.

## 5. Gotchas medidos en este paso

- **La demo §2.11.5 es más frágil que en el paellero**: el RAI del año 3 crece menos que el del 2 (los fijos suben ≈ 5.000 € al año). Con este caso, la ventana es de 128 € de RAI1 con 67 invitados. **Cualquier cambio del caso** (precio, fijos, `pct_comida`, plantilla) puede romperla. Si vuelve a fallar, mueve el fijo de extintores ±100 € y mira los `ensayos` de `inf.json` → `5_IS_con_BIN_y_tipo_de_nueva_creacion`.
- **`(?<!hasta )5\.000` casaba con «15.000 €»** (contrato menor): el prohibido lleva también `(?<![\d.])`.
- **Las notas del contenido también pasan el barrido**: «la carne pesa más que el arroz» (umbral) y «CNAE» (checklist) los cazó el gate de restos, no la revisión.
- **«tres auxiliares»** con dos filas de auxiliar en la plantilla era el m8 del paellero: las notas dicen ahora «los dos auxiliares y un tercero de la bolsa o de una ETT».
