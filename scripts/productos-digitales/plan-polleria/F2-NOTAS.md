# Plan de Negocio: Pollería y Asador de Pollos ES 1.0 — F2 (motor) · calibración, decisiones y gates

> Sesión Claude Code, 29-oct-2026. Motor de la F2 (plan + checklist) y herramienta del Word (sin redactar). SPEC =
> `F1-camino.md` §2 (firmada), §3-§4 y §7. Mac = código; VPS = motor (`/root/wt-polleria`, salidas `/root/tmp-pol-f2/`). Cero código común.

## 1. Ficheros

| Fichero | Qué es |
|---|---|
| `planes-v2_0/contenido_plan_negocio_polleria/{__init__,a}.py` | Contenido = el de la Taquería con el caso de R §3: `cubierto → pedido`, `ROTACION` apagada, Mes 1 = enero con el verano arriba; notas reescritas enteras (0 «comensal», «cubierto», «rotación» ni restos) |
| `plan-polleria/semilla_pol.py` | `semilla_taq.py` sobre la Taquería LIVE (solo plan + checklist): 18 partidas (88.500 € + imprevistos = 93.100 €), 9 fijos (13.900 €), títulos, docProps, `Instrucciones!A3`; **`_sin_rotacion`**: assert de que las 16 celdas son fórmula y a `None`; asserts `B60/B61` = 7/12 y `PyG!G13` valor |
| `plan-polleria/datos_checklist.py` | 80 tareas 12/15/14/13/13/13, pestañas ≤ 29, fuente primaria en el docstring (677.9 frente al 642.5, art. 4.1 y 9.2-9.3 del RD 1021/2022, art. 30 = RD 1086/2020, art. 5 del RD 126/2015, RD 919/2006, Ley 7/2022…) |
| `plan-polleria/main_pol.py` · `ciclo.sh` | `pol_version` (1.0 · noviembre 2026) + `main.py --dry-run --origen` (`SCR=/root/tmp-pol-f2/motor`) |
| `plan-polleria/cifras_pol_es.py` | 182 tokens (`cifras_caso_es.json`) + D9 + `prueba_mes1_enero` + **`prueba_polleria`** (F1-camino §7 F2 (3) y (4)); `--calc` lee TODO el `EXPUESTOS` de `calculadora_pol_es.py` (5 tokens) y, si no importa, por rótulo; no falla sin calculadora |
| `plan-polleria/barrido_es.py` · `tandas_docx.py` · `docx_pol_es.py` · `BRIEF-REDACTORES.md` | Herramienta del Word: `GEMELA` = `../plan-taqueria/textos`; `JERGA`, `PISTAS` (las cinco corrientes en §2-§4, §6 y §9), `PROHIBIDOS`, `AVISOS`; `PERMITIDAS` = base + las cifras de las pistas |
| `astro-site/public/dl/plan-negocio-polleria/{plan-financiero,checklist-apertura}-polleria.xlsx` | Salida del ciclo (Mac = VPS) |

## 2. Decisiones que se apartan de la SPEC o del gemelo (y por qué)

1. **`VOCABULARIO_SIN_TILDES = True`** (la SPEC lo pedía; la Taquería no lo lleva). Medido en la vuelta 1: sin él, las 7
   claves con tilde no casan (`grupo_a.compilar_vocabulario`: clave normalizada contra texto con tildes) y el libro
   conservaba las frases del motor «el alcohol que sale por delivery y el pan común» (`Supuestos!C9`,
   `Tesorería!O16`), «bollería y pastelería» (`Instrucciones!A8`) y «versión 1.1» (`Tesorería!D31`). Con él: las 10
   frases aplicadas y 0 restos. **La Taquería LIVE probablemente tiene esos 4 restos** (no comprobado: fuera de alcance).
2. **`PROHIBIDOS`**: fuera `\ble[ñn]a\b`, `horno`, `tarrina`, `\braciones\b` (oficio, F1-camino §4) y **`pan com[uú]n`** (el pan
   se vende y va al 4 %: la frase del motor se traduce a «el pan común que vendas suelto, al superreducido…»; la
   frase sin traducir la caza `alcohol (que sale por|del canal de) delivery` y la nueva `harinas panificables`).
   «Chimenea» pasa a aviso. **«Tortilla» a secas NO se prohíbe** (instrucción del coordinador): sólo `tortillas? de
   (maíz|harina)` y `tortiller[oa]`, más los restos de la Taquería (taquer, trompo, taco(s), comal, pastor, gringa,
   nixtamal, mezcal, tequila, aguas frescas, carnitas, suadero, cochinita, guacamole, salsa macha); vuelven horchata,
   mantec y cubeta. Aviso «tortilla» salvo «de patatas».
3. **Nota de `cubiertos_dia`**: «un cliente sentado en la sala» y no «un comensal de sala» (la SPEC lo escribía así, pero
   choca con el gate (4) «0 comensal»). Igual en el aforo: «cada plaza se ocupa algo más de una vez al día» (sin «rotación»).
4. **Instrucciones, referencias**: 12 filas como la Taquería (Mes 1 + las 9 de R §3 + SMI + convenio), para no dejar filas
   del origen; la del coste del pollo entero cita el 38,8 % = caché de la calculadora (`FC_POLLO_ENTERO`).
5. **`cifras`**: tokens `PEDIDOS_*` (no `COMENSALES_*`), `ASADOR`, `VITRINA`, `BOTELLERO`, `RESIDUOS_ANO`, `COSTE_VAR_PEDIDO`,
   `MARGEN_PEDIDO`, `ESC_*_PEDIDOS`; fuera `ROT_*`, `ROTACION_IMPLICITA`, `TROMPO`, `PLANCHA`, `BARRA`, `TASAS_TERRAZA_*` y el
   gate de rotación. Derivados: `POLLOS_SEMANA` (301), `POLLOS_SEMANA_EQUILIBRIO_CAJA` (250, con los 64 pedidos del token),
   `POLLOS_SEMANA_EQUILIBRIO`, `POLLOS_ANO` (15.067) = pedidos × 302/463 (R §3). `BEBIDA_21_PCT` en `pct` (31,0 %).
6. **Calculadora**: la del otro agente usa «tanda» (no «carga») y expone `POLLOS_POR_TANDA`, `CAPACIDAD_DOMINGO`,
   `RENDIMIENTO_POLLO`, `COSTE_POLLO_ENTERO`, `FC_POLLO_ENTERO` (no los 10 `EXPUESTOS` de F1-camino §4). La jerga y las
   pistas dicen «carga o tanda».

## 3. Calibración (1 vuelta de 3: la vuelta 2 del F1-camino, reproducida)

Préstamo **112.000 €** + 50.000 € propios, fijos **13.900 €**: `ciclo.sh` exit 0 **TODO VERDE** a la primera (sin «PERDIÓ
… fórmulas»; demos §2.11 ok) y `cifras_pol_es.py --calc` **D9 VERDE** (18/18), sin palanca. Cifras = vuelta 2 al euro.

**Sensibilidad del pollo** (F1-camino §2 «Lo que la F2 mira» (1), vuelta suelta en `/root/tmp-pol-f2/sens/` con
`coste_comida` 0,335 = pollo a precio de Makro, tocando sólo el origen): EBITDA A1 45.320 → **40.393 €** (−4.927 €; ≈
3.300 € por punto de comida); neto **5,9 / 7,0 / 6,7 %** → D9 ROJA (año 3 < 7 %); DSCR 1,80; holgura A1 19,0 %. Si el
orquestador adopta el precio de Makro, la palanca de R §3 es el pollo entero a 13,50 €. Va a la pista §8.

## 4. Cifras del caso (`cifras_caso_es.json`, 182 tokens, con `--calc` de la calculadora de `dl/`)
- Ventas **364.980 / 386.879 / 402.354 €** (77 × 15,80 € × 300) · margen bruto 59,1 % · mercancía 31,8 % · personal
  128.683 € (35,3 %; 7 filas, 4,60 jornadas) · alquiler 3,9 % · EBITDA 45.320 € (12,4 %).
- Neto **25.704 € (7,0 %) / 31.605 € (8,2 %) / 30.969 € (7,7 %)**.
- Partidas + imprevistos 93.100 € · CAPEX 97.900 € · fondo 44.276 € · inversión 142.176 € · IVA 19.425 € ·
  **necesidad 161.601 €** · exceso 399 € (0,2 %) · cuota 22.777 € · **DSCR mín. 1,98** (2,05 / 1,98).
- Equilibrio contable 67 pedidos (holgura 16,3 %); caja 64 / 72 / 74 · **holgura A1 21,8 %** (14,8 / 15,9 %).
- **Saldo mínimo 50.818 € en el Mes 1 (enero)** · cierre 106.517 € · payback **«Más de 3 años»** (texto; 2,2 sobre el
  CAPEX) · cobertura 111 % · IVA bebida 13,4 % (H 31 %, 3,1 % de las ventas) · compras 9,1 / 17,7 %.
- Escenarios 292.050 € (neto −12.861 €) / 442.860 € (+64.827 €).
- Calculadora: 60 pollos por tanda, 180 antes de la hora límite del domingo, rendimiento 76 %, pollo entero 4,55 € (38,8 %).

## 5. Gates (VPS, 29-oct)

`ciclo.sh`: exit 0 en ~26 s, **TODO VERDE** (idempotencia 0 · caché 677/736 + 12, 0 fallos pycel · data_only 688 + 59
«""», 0 fallos · blancos 0 · §9 **13/13** · C2 80 ítems · censo `--fail` 0 · moldes **30/30** · 16/16 protegidas ·
demos 2.11 ok). `cifras_pol_es.py --calc`: **D9 VERDE** (11 de la Taquería sin el de rotación + 3 del Mes 1 + 4 de
`prueba_polleria`: `PE!A25` = «INTERPRETACIÓN» y 37-38 vacías, 0 «rotaci», 0 «comensal|cubierto», 8 rótulos «Pedidos/día»).
`barrido_es.py` sobre los 2 xlsx: **0**, 2 avisos («No prometer «sin gluten»…» y «Sin gluten» sólo con 20 mg/kg…:
correctos). `gate_restos_ft.py --rx-extra` (Taquería + Pizzería + tapas/heladería + pids): **VERDE** (2). VOCABULARIO
10/10 aplicado. `tandas_docx.py preparar`: `pol_es_a` 29 ranuras / 2.954 palabras · `pol_es_b` 32 / 3.765 · 182 tokens;
`check` sin salida → exit 2, `{}` → «faltan …». `docx_pol_es.py --parcial`: 131 párrafos, 10 Heading 1, VERDE; barrido 0.
sha256 Mac = VPS: plan `7122122f…eac4`, checklist `71ea9005…9946`.

## 6. Comandos

Subir fichero a fichero con `scp` a `/root/wt-polleria/…` (nunca `rsync --delete`) · VPS: `bash ciclo.sh` →
`cifras_pol_es.py --xlsx <dl>/plan-financiero-polleria.xlsx --calc <dl>/calculadora-pollo-asador-escandallo-polleria.xlsx`
→ `barrido_es.py <dl>/*.xlsx` → `../catering-es-2_0/gate_restos_ft.py <dl> --rx-extra '<restos>'` · Mac: `scp` del json
a `plan-polleria/` y `python3 tandas_docx.py preparar` → 2 Sonnet → `check --tanda pol_es_a|b` · VPS: subir
`textos/pol_es_{a,b}.json` y `docx_pol_es.py --salida <dl>`.

## 7. Pendientes para el Word y la revisión

- Si la calculadora cambia: `cifras --calc` y revisar el «38,8 %» de `a.py` (nota de `coste_comida` y referencia de
  Instrucciones). Pollo (§3): ¿precio de Makro y palanca del pollo entero a 13,50 €? Decide el orquestador.
- La F3 relee la LIVA art. 91 (versión con vigencia 1-12-2026, R §1) y contrasta landing y dashboard con los entregables.
