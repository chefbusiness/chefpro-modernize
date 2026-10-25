# Plan de Negocio: Pizzería Napolitana ES 1.0 — F2 (motor) · calibración, decisiones y gates

> Sesión Claude Code, 25-oct-2026. Implementador del MOTOR de la F2 (plan financiero + checklist) y de la herramienta del
> Word (sin redactar). SPEC: `SPEC.md` (D1-D19); cómo: `F1-camino.md` §1-§4; caso: `F1-research-pizzeria.md` §3. Código
> en el Mac (worktree de `feat/plan-negocio-pizzeria`); motor y xlsx en el VPS (`/root/wt-pizzeria`, venv
> `/root/venv-guias`, salidas en `/root/tmp-piz-f2/`). Cero código común: ni `motor.py`, ni `grupo_a.py`, ni `main.py`,
> ni el pid en `PRODUCTOS`.

## 1. Ficheros

| Fichero | Qué es |
|---|---|
| `planes-v2_0/contenido_plan_negocio_pizzeria/{__init__,a}.py` | Contenido: mecánica del tapas bar 2.2 (dos servicios, producción antes de abrir, `ROTACION` encendida con techo 3) y formato de la heladería 1.0 (sexto campo de fuente, `AMORTIZABLE` propio, `IVA_COMPRAS` numérico, Mes 1 girado, pagas, `RECALIBRADO = ()`); bebida con la **línea partida** del motor (`H` = 7 % al 21 %) |
| `plan-pizzeria/semilla_piz.py` | `semilla_hel.py` sobre el **tapas bar 2.2**: 18 partidas (7-24), 9 fijos (26-34), títulos (Inversión A1-A3, PyG A2, PE A2), `PyG!G13` por valor (6,4 %), supuestos, checklist y docProps. Sin vaciado de `PyG!H` (el tapas no trae línea partida) |
| `plan-pizzeria/datos_checklist.py` | 80 tareas: 12 · 15 · 14 · 13 · 13 · 13 (constitución · local, humos y licencia · cocina, horno y sanidad · personal y prevención · carta, marca y delivery · apertura y 90 días), con todas las del research §3 «tareas que obliga» y la fuente primaria en el docstring |
| `plan-pizzeria/ciclo.sh` | semilla → `main_piz.py --dry-run --solo a` (`SCR=/root/tmp-piz-f2/motor`) |
| `plan-pizzeria/cifras_piz_es.py` | 178 tokens para el Word (`cifras_caso_es.json`) + gates D9; con `--calc` lee la caché de la calculadora (`COSTE_BOLA`, `COSTE_MARGHERITA`, `FC_MARGHERITA`, `FC_LLEVAR_MARGHERITA`) |
| `plan-pizzeria/barrido_es.py` | `tandas_docx.PROHIBIDOS` (D12 + restos FT, tapas, heladería, motor sin traducir, pids) + `RX_CAMPANA`. SIN los restos de panadería: harina, masa, levadura y amasado son el oficio |
| `plan-pizzeria/tandas_docx.py` · `docx_piz_es.py` · `BRIEF-REDACTORES.md` | Herramienta del Word (§6) |

## 2. Decisiones que se apartan de la SPEC, del camino o del research (y por qué)

1. **Fila de suplencias** (SPEC D8: «si el molde la exige»): la exige. Con las 6 filas del research, `main.py` falla con
   «el post-proceso PERDIÓ 10 fórmulas» (`Personal!B12`, `B17`, `B27`…): el tapas trae 7 filas y el total cambia de
   sitio. Se añade la 7.ª (RC-19, 130 € al 10 %, = tapas y heladería): +2.421 €/año, personal 36,2 %.
2. **Tasa de terraza** (+1.200 €/año, = heladería, cifra de ejemplo «pon la de tu ayuntamiento»), FUNDIDA en la fila de
   residuos: `Tasa de terraza y gestión de residuos (pon las de tu ayuntamiento)` = 1.800 € → fijos 18.800 € (SPEC D8:
   17.600 €). Motivo: la demo §2.11.5 del motor (ramas del IS) no salía (ver §3); la terraza de 24 plazas paga su tasa y
   ni el research ni la SPEC la contaban. Como **10.ª fila** (`FIJOS_EXTRA`) desplaza el P&L y `main.py` marca 6
   fórmulas perdidas (`PyG!B35`, `B50`…): medido, descartado.
3. **`IVA_COMPRAS` = 6,4 % (la COMIDA) y `pct_bebida_alc` = 80 %**, no 8,9 % en `G13` (SPEC D6). El motor aplica
   `IVA_COMPRAS` sólo a la línea «Coste de mercancía — comida»; la bebida soporta su propio tipo (`pct_bebida_alc` × 21 %
   + resto × 10 % = 18,8 %, research §1). Poner el 8,9 % ponderado en la comida contaba dos veces el 21 % de la bebida.
   Ponderado por el peso de la compra (79,9 / 20,1), la compra entera sale al 8,9 % del research.
4. **`vida_maquinaria` = 10 años** (research: «9 = heladería»; la heladería publicada usa 10 y cumple también el
   coeficiente del mobiliario, 10 %).
5. **Umbral de margen bruto 65 %** (research: 74 %). El 74 % es sobre la mercancía sola (el caso da 75,9 %); el del libro
   descuenta TODOS los variables (cajas, plataforma, TPV, varios) y el caso da 67,1 %. Mismo criterio que la heladería.
6. **Mes 1 = septiembre** (SPEC D7 manda sobre el camino §2, que decía enero): tupla girada con `assert`, pagas en los
   Meses 11 (julio) y 4 (diciembre), notas de Tesorería (`O5` estacionalidad, `A34` trimestres del 303) por `VOCABULARIO`.
7. **Leña como fijo** (SPEC D8, 3.600 €) y no en suministros (camino §2): manda la SPEC.
8. **«Campana» → «Campaña»** (aviso del orquestador): `motor.TILDES` acentúa «campana» suelta salvo las excepciones de
   `motor.EXCEPCIONES_CAMPANA`. En el primer dry-run `Inversión!A16` y `PyG!A27` decían «Campaña» y, como el rótulo ya no
   casaba con `AMORTIZABLE`, la partida de 3.000 € quedaba FUERA de la base de amortización (`B36` = 47.700 €). Arreglado
   en la fuente: siempre «campana extractora» (semilla, `a.py`, checklist); `B36` = 50.700 € con `B16` dentro. Guarda
   nueva: `barrido_es.py` `RX_CAMPANA` = `[Cc]ampa[ñÑ]a` salvo «campaña de apertura / lanzamiento / marketing /
   publicidad / Navidad».
9. **Rótulo del horno** sin «napolitano» («Horno de leña de cúpula baja de 120-130 cm de diámetro»), por D11.
10. **Neto «a régimen»** en el gate = años 2 y 3 entre el 7 y el 12 %; el año 1, ≤ 12 % (el motor normaliza la rampa
    dentro del año: el P&L del año 1 vende el régimen, 386.100 €).
11. **Plantilla de incorporaciones** 6.000 € el año 2 y 6.000 € el año 3: son los valores por defecto del motor que trae
    la semilla (= heladería). No se tocan; van como token `{INCORPORACIONES_A2}`.
12. El regex `raciones` del camino §3 casaba «Operaciones» (el título del §6 del Word): va como `\braciones\b`.

## 3. Calibración (2 vueltas de 3)

| Vuelta | Cambio | Resultado |
|---|---|---|
| 0 | caso del research (65.000 + 155.000 €, 6 filas de plantilla) | exit 1: RD-34 origen − usos = −1.929 € (−0,87 %) · 10 fórmulas perdidas en `Personal` |
| 1 | fila de suplencias · préstamo 158.000 € | exit 1: sólo la demo §2.11.5 (ensayos 65…54 comensales: ninguno con RAI1 < 0 < RAI2 < BIN2 e IS3 > 0; la ventana a 55 pide 700-4.100 € más de fijos y a 54, 800-3.300 € menos) |
| 2 | «campana extractora» (+300 €/año de amortización) · tasa de terraza +1.200 € en la fila de residuos · préstamo 159.000 € | **TODO VERDE** · D9 VERDE. Demo a 55 comensales: RAI1 −4.341 €, RAI2 +2.607 € < BIN 4.341 €, IS3 809 € al 15 % |

D9 en la calibración final (`cifras_piz_es.py`): DSCR mín. 1,88 · saldo mín. 61.519 € · cobertura 104 % · holgura de
caja 24,3 % (A1; 15,7 % y 17,4 % A2-A3) · exceso 1.106 € (0,5 %) · neto 8,5 / 10,0 / 9,6 % · rotación de equilibrio de
caja 1,06 / 1,21 / 1,24 ≤ 3 · plataforma 10 % · `PyG!G11` = 0,1077 = 0,07 × 21 % + 0,93 × 10 % (fórmula
`H11*0.21+(1-H11)*'0. Supuestos'!$B$39`). No hizo falta ninguna palanca del research (propios, plazo, comensales, ticket).

## 4. Cifras del caso (`cifras_caso_es.json`, 178 tokens)

- **Actividad**: 66 comensales equivalentes × 19,50 € sin IVA (21,48 € con IVA) × 300 días. Ventas **386.100 / 409.266 /
  425.637 €**. Comida 82 % · bebida 18 % (7 % de la bebida al 21 % = 1,3 % de las ventas; IVA medio de la bebida 10,8 %).
- **Márgenes**: mercancía 24,1 %; margen bruto 67,1 %; personal 139.873 € (36,2 %) → 145.873 → 151.873 €; alquiler 6,5 %;
  fijos totales 220.138 €; EBITDA 60.084 € (15,6 %) / 69.621 / 74.601 €.
- **Resultado**: RAI 38.819 €; neto **32.996 € (8,5 %) / 41.103 € (10,0 %) / 41.028 € (9,6 %)**.
- **Inversión**: partidas + imprevistos 130.250 € · CAPEX 142.850 € (fianza 6.300 y renta previa 6.300) · fondo 52.103 € ·
  inversión total 194.953 € · IVA 27.940 € · **necesidad 222.894 €**. Bases: obra 66.550 € (10 años), maquinaria 50.700 €
  (10 años); amortización 11.725 €.
- **Financiación**: 65.000 € propios + **159.000 €** al 6 %, 7 años con 1 de carencia; cuota 32.335 €. DSCR 1,93 / 1,88
  (**mínimo 1,88**).
- **Equilibrio**: contable **57 comensales/día** (328.222 €; holgura 17,6 %); caja **54 / 61 / 62** (310.740 € el año 1;
  holguras **24,3 % / 15,7 % / 17,4 %**). Rotación implícita 1,3 (con llevar y domicilio; la de sala ≈ 1,0).
- **Tesorería**: saldo mínimo **61.519 € en el Mes 1 (septiembre)**; cierre 123.546 € (agosto). Payback «Más de 3 años»
  (2,4 sobre el CAPEX). Cobertura de horas **104 %** (9.154 contratadas / 8.775 necesarias; 7 personas, 4,975 jornadas).
- **Escenarios**: pesimista 56 × 18,50 € × 295 = 305.620 € → neto −15.159 €; optimista 76 × 20,50 € × 305 = 475.190 € →
  +83.786 €.
- **Calculadora** (caché del xlsx publicado de `calculadora_piz_es.py`, otro agente): bola 0,23 €; Margherita 1,32 € (15 %;
  26 % para llevar con la caja). Si la calculadora cambia, se vuelve a pasar `cifras_piz_es.py --calc` antes del Word.

## 5. Gotchas

- `motor.TILDES` convierte «campana» en «campaña» (§2.8): escribir siempre «campana extractora».
- El molde tapas tiene 7 filas de Personal y 9 de fijos: ni una más ni una menos, o «fórmulas perdidas».
- `VOCABULARIO` casa con `\b` en los dos extremos: la clave tiene que acabar en letra o cifra («… al 21», no «… al 21 %»;
  «… 91.Dos.1.1.º», no «…º)»). Las 3 frases del motor del §1 del camino y `Supuestos!C40` («su tipo está en el bloque de
  desglose del IVA») van traducidas; `Tesorería!D31` («versión 1.1») también (= heladería).
- `ROTACION['referencia']` y la nota de `IVA_COMPRAS` van dentro de un literal de fórmula: cortas (< 255 caracteres).
- El rsync Mac → VPS de `plan-pizzeria/` excluye `calculadora_piz_es.py` y `__pycache__` (otro agente).

## 6. Comandos para regenerar

```bash
W=<worktree del Mac>; S=scripts/productos-digitales
rsync -a --exclude calculadora_piz_es.py --exclude __pycache__ "$W/$S/plan-pizzeria/" vps:/root/wt-pizzeria/$S/plan-pizzeria/
rsync -a --exclude __pycache__ "$W/$S/planes-v2_0/contenido_plan_negocio_pizzeria/" vps:/root/wt-pizzeria/$S/planes-v2_0/contenido_plan_negocio_pizzeria/
ssh vps 'cd /root/wt-pizzeria/scripts/productos-digitales/plan-pizzeria && bash ciclo.sh && grep -n "TODO VERDE\|FALLOS" /root/tmp-piz-f2/motor/run.log'
ssh vps 'cd /root/wt-pizzeria/scripts/productos-digitales/plan-pizzeria && D=/root/tmp-piz-f2/motor/dryrun/plan-negocio-pizzeria &&
  /root/venv-guias/bin/python cifras_piz_es.py --xlsx $D/plan-financiero-pizzeria.xlsx \
    --calc /root/wt-pizzeria/astro-site/public/dl/plan-negocio-pizzeria/calculadora-masa-escandallo-pizzeria.xlsx \
    --salida /root/tmp-piz-f2/cifras_caso_es.json &&
  /root/venv-guias/bin/python barrido_es.py $D/*.xlsx &&
  /root/venv-guias/bin/python ../catering-es-2_0/gate_restos_ft.py $D --rx-extra "\btapas?\b|gastrobar|vermut|\braciones\b|\bpinchos?\b|tapeo|afterwork|salamandra|rational|[Ff]ichero v1\.1|helad|mantec|cubeta|sorbete|pasteuriz|granizad|horchata|tarrina|plan-negocio-tapas-bar|plan-negocio-heladeria"'
scp vps:/root/tmp-piz-f2/motor/dryrun/plan-negocio-pizzeria/{plan-financiero,checklist-apertura}-pizzeria.xlsx "$W/astro-site/public/dl/plan-negocio-pizzeria/"
scp vps:/root/tmp-piz-f2/cifras_caso_es.json "$W/$S/plan-pizzeria/"
# Word: Mac (sólo JSON) → 2 redactores Sonnet → check → VPS ensambla
python3 $S/plan-pizzeria/tandas_docx.py preparar
python3 $S/plan-pizzeria/tandas_docx.py check --tanda piz_es_a        # y piz_es_b
ssh vps 'cd /root/wt-pizzeria/scripts/productos-digitales/plan-pizzeria && /root/venv-guias/bin/python docx_piz_es.py --salida /root/tmp-piz-f2/docx'
```

(Si la calculadora del `--calc` aún no está en el worktree del VPS, cópiala antes a `/root/tmp-piz-f2/calc_pub/` y apunta ahí.)

## 7. Gates de este paso (VPS, 25-oct)

`ciclo.sh`: main.py exit 0, **TODO VERDE** (idempotencia 0 · caché 682/741 + 12, 0 fallos pycel · data_only 0 fallos ·
blancos 0 · §9 13/13 · checklist C2 80 ítems · censo `--fail` 0 · moldes 30/30 · 16/16 protegidas · demos) ·
`cifras_piz_es.py` **D9 VERDE** (12/12) · `barrido_es.py` **0** en los 2 xlsx · `gate_restos_ft.py --rx-extra` **VERDE**
(2 ficheros). sha256 Mac = VPS: plan `aad4cabe…f22c9`, checklist `56a304c0…eb25`. `tandas_docx.py preparar`: `piz_es_a`
29 ranuras / 2.954 palabras · `piz_es_b` 32 / 3.765 (6.719 en total) · 178 tokens. `check` sin salida → exit 2 con
mensaje; fichero vacío → exit 1 «está vacío»; `{}` → «faltan [39…75]»; párrafos vacíos → «párrafo vacío» por ranura.
`docx_piz_es.py --parcial`: 131 párrafos, 10 Heading 1, A4, VERDE en modo ensayo; barrido 0.
