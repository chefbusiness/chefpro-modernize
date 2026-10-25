# Brief para los traductores (subagentes Sonnet) — Pizza Shop Business Plan Kit (EN)

> Sesión Claude Code, 25-oct-2026 (F2-EN, paso 1a: preparado; **no se ha traducido nada**). SPEC delta D133-D155 y **§0,
> regla de jerga**. Regla 1bis: los textos de producto los escriben subagentes Anthropic, **nunca bridge.py**. Carpetas
> (worktree del Mac): `scripts/productos-digitales/business-plans-en-8/` (= `BP8/`, datos y salidas de la pizzería),
> `scripts/productos-digitales/business-plans-en-3/` (= `BP3/`, el **Bar EN** cerrado: libro gemelo, la forma) y
> `scripts/productos-digitales/business-plans-en/` (= `BP/`, el código común y el brief de FT/CAF).
>
> **Cuatro tandas**, máximo 2 subagentes a la vez (`istats cpu temp` < 62 °C en el Mac):
> **tanda 1 = (a) GPIZ-plan + revisión de GR ‖ (b) GPIZ-check** → **tanda 2 = (c) piz_a ‖ (d) piz_b** (cuando exista el Word
> ES: paso 1c). **No se escriben** GM (361 cadenas: mismo ES que el Bar EN en la misma celda o motor común) ni GR (27: se
> **revisa** en (a), casi todas «comensales» → «covers»): los escribe `bp8.py preparar_tandas`.
> **Antes de lanzar las tandas** el orquestador hace el paso 1c (re-extracción sobre el ES FINAL, F2-NOTAS §6): las
> entradas de este paso 1a salen del dry-run ES y sus ids pueden cambiar.

**Cómo usar este brief**: el orquestador pega al subagente la sección **0 de `BP/BRIEF-TRADUCTORES.md`** (reglas comunes:
idioma, cero español, moneda, formato US, marca, cifras, pestañas citadas, glosario) + las secciones **0 y 1** de este
fichero (la 1 es el glosario de research §9 completo, OBLIGATORIO) + la de su tanda. El subagente no hace commit y no toca
nada más que su salida.

---

## 0. Lo que cambia frente al brief del Bar EN (manda sobre él en lo que choque)

**Qué lees** (y nada más): tu entrada `BP8/tandas/<TANDA>.entrada.json`; `BP8/SPEC-delta.md` (D133-D155);
`BP8/F1-research-us-delta.md` §1, §4, §5, §6, §8 y §9; como FORMA (registro, longitud, fuentes comunes), el EN del Bar en
`BP3/textos_en/{GBAR-plan,GBAR-check}.json` y `BP3/docx_en_bar_{a,b}.json`: su vocabulario de bar NO vale.

**Concepto (D136): NEAPOLITAN-STYLE PIZZA SHOP de barrio**, ciudad media de EE. UU. (150-300 mil hab.), ~1,500 sq ft,
**50 plazas + patio de 24 (abril-octubre)**, mesa + take-out/delivery, horno de leña de cúpula de 47-51 in **listado UL
2162** (gas o eléctrico = variante, y no cumplen VPN), **beer & wine** (sin full liquor, sin cócteles), cierra los lunes; el
dueño es el head pizzaiolo y el GM. «Pizza shop» en el nombre, «pizzeria» como sinónimo en prosa. **«Neapolitan-style»
siempre**: nunca «authentic», «verace» ni «VPN-certified» como promesa (solo «VPN-certified only after AVPN
certification»). Volumen = **covers** (nunca «customers»). Fuera (y así lo dicen las FAQ): slice shop NY, franquicia, food
truck (→ Food Truck Kit), ghost kitchen, venta desde casa.

**Caso US** (`BP8/F2-NOTAS.md` §3; D137 con la calibración D15 de una vuelta: ticket $36): 62 covers × **$36.00** × 300
días = **$669,600** · CAPEX $242,550 (las 18 partidas de D139 = $217,300 + fianza + 2 meses de renta previa + imprevistos
por fórmula) + fondo de maniobra $86,724 · propios $130,000 (39 %) + préstamo **$200,000** (SBA 7(a), 10 %, 10 años) ·
COGS 26 % · personal 32.8 % · prime cost 58.8 % · EBITDA 14.7 % · **neto 5.9 %** (y no el «15-25 %» de la SERP: PMQ 2026,
2-3 %) · equilibrio 55 / 53 covers/día, holgura 18 % · DSCR mín 2.62×. Las notas del libro describen el **método** o usan
`valor_us`; el docx cita el caso SOLO con tokens `{{…}}`. **Ninguna cifra del ES** (D149: el gate las caza, en € y en $).

**Lo que el check rechaza** (`datos_piz.RX_PIZ_NO` + `cifras_prohibidas`): tapas, small plates, cocktails, spirits,
neighborhood bar, barback, last call, happy hour, draft beer system; ETG, pliego, convenio, SMI, autónomo, Veri\*factu, IVA,
SGAE, IAE, terraza, comensal, España/Spain, VAT fuera de la nota UK; «97/2010», «TSG» y «Napoletana» fuera de contexto UE /
AVPN (solo la fila D19 del nombre, su ranura del Word y «Verace Pizza Napoletana»); «authentic Neapolitan»; kg, km, litros o
°C fuera de paréntesis; el caso del Bar EN (95 covers, $27, 360 days, sus importes) y los del FT y el Restaurant EN.

**Unidades** (`datos_piz.REGLA_UNIDADES`): lb y oz, °F, gallons / quarts, sq ft; la métrica entre paréntesis; el horno en
pulgadas con cm entre paréntesis («47-51 in (120-130 cm)»); **la masa en gramos y % panadero** (así trabaja el oficio US,
D145).

**Claims que no se hacen** (D150): no prometer «gluten-free» (21 CFR 101.91, < 20 ppm; la harina en el aire lo impide sin
protocolo y análisis: «gluten-friendly / ask» con aviso); no prometer la licencia de alcohol ni que sobra la campana (NFPA
96 y el AHJ deciden: «ask the fire marshal in writing»); no prometer venta desde casa; no prometer márgenes de la SERP.

---

## 1. Glosario OBLIGATORIO (research §9, pegado entero)

## 9. Jerga profesional US (glosario OBLIGATORIO de los traductores)

(a) **Nombre**: **«Pizza Shop Business Plan Kit»** en landing/H1/ficheros (`pizza-shop-business-plan`), con «Neapolitan-style» en el subtítulo; «pizzeria» como sinónimo en prosa. **«Neapolitan pizza»** (sin «verace» ni «VPN-certified») salvo certificación. Nunca «authentic Neapolitan» como promesa del producto.

| # | ES pizzería | Término US | Fuente / estado |
|---|---|---|---|
| 1 | Pizzaiolo | **pizzaiolo** (head pizzaiolo; «pizza chef» en menús) | DFS 40.500; VPN/Italiano; uso común en operadores |
| 2 | Bola de masa | **dough ball** / **dough balls** | DFS 2.400; Dough Doctor (Lehmann) en pizzamaking.com [foro, resumen] |
| 3 | Cornicione | **cornicione** (también «crust rim», «edge»); «cornice» no es uso US | DFS 1.600; Food Code N/A; Gozney/Tasting Table (SERP) |
| 4 | Manchas de leopardo | **leopard spotting** (char blistering) | DFS 40; términos de cocina (SERP) |
| 5 | Harina «00» · tipo 1 | **00 flour** (Caputo-type) · **"1" flour** | DFS 18.100; Tasting Table [leída]: «Only "00" or "0"… plus a small amount of "1"» |
| 6 | Fior di latte · búfala | **fior di latte** (fresh cow's milk mozzarella) · **mozzarella di bufala (DOP)** | DFS 27.100; Slice/Settebello menús (resumen: «Margherita DOC con búfala»); Casanova «fresh mozzarella» [leída] |
| 7 | Tomate San Marzano DOP | **San Marzano tomatoes (DOP)** | DFS 49.500; Flatbread/Settebello menús (resumen) |
| 8 | Prefermento | **biga** (5.400) · **poolish** (5.400) · **preferment** | DFS; Gozney recipe en SERP (preferment 240 g) |
| 9 | Pala | **peel** (wood/aluminum; «turning peel») | DFS 27.100 |
| 10 | Horno de cúpula · solera | **dome oven** · **deck** (deck oven = horno de cámara; «deck» ≠ «dome») | Marra Forni [leída]: Neapolitan (static brick), Rotator; VPN «dome»; Bakers Pride «deck» [leída] |
| 11 | Pizza napolitana vs americana | **Neapolitan-style** (soft, wood-fired, 60-90 s) · **New York-style** (90.500; slice, gas deck) · **Detroit-style** | DFS 18.100 / 90.500; AI Overview SERP [leída] |
| 12 | Pizzería | **pizza shop** (take-out/slice, 49.500 «near me») vs **pizzeria** (mesa; 1.000.000 ruido) | DFS; SERP |
| 13 | Cocina / sala | **BOH** (back of house) / **FOH** (front of house) | Toast/R365 (uso del sector; no abierto) |
| 14 | «86» (agotado) | **86'd** / "eighty-six" | uso del sector (no fuente leída) |
| 15 | Cubierto equivalente | **covers** (cubierto) / **cover** | ✅ hermanos (REST/BAR) |
| 16 | Ticket medio | **average check** / **check average** (excl. sales tax y tip) | ✅ hermanos |
| 17 | Coste de mercancía | **food cost %** (720 «pizza food cost») · **prime cost** (food + labor, 4.400) | DFS; ✅ REST §4 |
| 18 | Comida para llevar | **take-out** · **to-go** · **pickup** · **delivery** (marketplace) | DoorDash/Uber [leída] |
| 19 | Plataforma | **third-party delivery marketplace** (DoorDash, Uber Eats, Grubhub) | §5.3 |
| 20 | Escandallo | **plate costing** / **recipe costing** / **food cost per pizza** | ✅ hermanos |
| 21 | Manipulador | **food handler card** · **Certified Food Protection Manager (CFPM)** | Food Code 2-102.12 [leído] |
| 22 | Nombre protegido | **«Neapolitan-style»** (libre) vs **«VPN-certified»** (solo certificado) | §6.9 |
| 23 | Campana / chimenea | **Type I hood** · **flue / chimney** · **spark arrestor** · **UL 2162-listed** | Oregon 15-01; CMC 517.1.6 [leídas] |
| 24 | Control tiempo | **time as a public health control (TPHC)** | Food Code 3-501.19 [leído] |
| 25 | Hidratación · reposo | **hydration** (590) · **cold ferment** / **proof** | DFS; Dough Doctor |
| 26 | Anticipo · IVA | **deposit** · **sales tax** | ✅ hermanos |

(e) **No se traducen literalmente**: «napolitana» → **Neapolitan-style** (US sí permite) · «ETG/pliego» → *no aplica en EE. UU.* (solo nota) · «ordenanza de humos» → **NFPA 96 + local fire/mechanical code** · «registro sanitario» → **health permit + plan review** ·
«licencia de apertura» → **business license + certificate of occupancy** · «convenio» → **state/local minimum wage** · «IVA» → **sales tax** · «autónomo/SL» → **LLC** · «manipulador» → **food handler card + CFPM** · «cubiertos» → **covers** ·
«para llevar y domicilio» → **take-out & delivery** · «terraza» → **patio** · «barra» → **bar (beer & wine)** · «pliego» → no se traduce (eliminar del EN) · «plataforma» → **delivery marketplace**.

**Capas (1) y (2)**: **Pizza Shop Business Plan Kit** · slug `pizza-shop-business-plan` · `pizza-shop-business-plan.docx` «Pizza Shop Business Plan (10 Sections)» · `pizza-shop-financial-projections.xlsx` ·
`pizza-shop-startup-checklist.xlsx` · `pizza-dough-food-cost-calculator.xlsx` (calculadora; pestañas `Dough` / `Food Cost`; gramos↔oz y °C↔°F, **sq ft**) · `pizza-shop-equivalents-guide.docx` (según ES) ·
pestaña F2 **«Phase 2 - Oven, Hood & Permits»** (≤ 31 car.).


---

## 2. Tanda (a) — GPIZ-plan + revisión de GR

Entrada `BP8/tandas/GPIZ-plan.entrada.json` (paso 1a: 139 cadenas, ≈ 3,5 K palabras; las cifras exactas, tras el 1c).
Salidas: `BP8/textos_en/GPIZ-plan.json` (TODOS los ids) y `BP8/textos_en/GR.revision.json` (solo las de GR que cambian;
`{}` si ninguna).

- **Notas de `0. Assumptions` (col. C)**: el caso US de su pista (D137) o el método; sin el 10/21 % del IVA español: un solo
  sales tax de ejemplo (8 %, B39 = B40), sin crédito por compras (B41 = 0). La nota de `C62`/`C63` y de `3-Year P&L!F11`/`H4`
  ya está fijada (POR_CELDA): úsala con esas palabras si la citas.
- **Notas de `Startup Costs` (col. D, filas 7-24)**: las partidas de D139 (rótulos ya fijados); rangos solo con fuente de
  research §4 (Forno Bravo, WebstaurantStore, UpMenu) o ninguno. Beer & wine license en la fila 7 (estado sin cupo ≈
  $3,000); NFPA 96 en la 9; UL 2162 en la 12; Type I hood solo para la línea de apoyo en la 16.
- **Tabla D19 (`Instructions` 35-47, 52 celdas, una por celda, SIN propuesta)**: cada fila la dicta su pista (D142):
  Benchmark | Value | Source | Note. Solo lo «leída» con fuente; lo «(resumen)» = «Kit estimate». La fila 38 (pliego)
  es la ÚNICA donde caben «EU TSG», «Reg. (EU) 97/2010» y «AVPN», con «a reference, not a US rule».
- **`Instructions` A4-A12**: A8 sin divisores 1,10/1,21; A10 con el Mes 1 = SEPTEMBER (D144); A12: el Word cita las cifras de
  este Excel y la calculadora de masa y food cost va aparte.
- **Revisión de GR** (lista `revisar_reutilizadas`): casi todas son el EN del Bar casado tras normalizar «comensal» →
  «cubierto»: confirma «covers» y corrige solo lo que no case con una pizzería (p. ej. «Certificado digital» → «City or
  county business license» viene del FT EN: comprueba que no duplica otra tarea de la fase 1).

## 3. Tanda (b) — GPIZ-check (las 80 tareas, D146)

Entrada `BP8/tandas/GPIZ-check.entrada.json` (paso 1a: 219 cadenas, ≈ 3 K palabras). Salida
`BP8/textos_en/GPIZ-check.json`. Molde C2 (OK | TASK | OWNER | TIMING | NOTES); pestañas ya fijadas («Phase 2 - Site, Hood &
Permits»…); A1 = «PIZZA SHOP STARTUP CHECKLIST» y la cabecera de la fase 2, fijadas. **Equivalencias US de D146** (las
pistas de cada cadena las recuerdan): LLC vs S corp with your CPA · EIN + state payroll/unemployment · business license +
sales tax permit · POS that reports sales tax · zoning check before signing · building permit + CO · patio permit · **beer
& wine license** (state ABC + local, a menudo 3-12 meses: contingencia en el lease) · NFPA 96 ch. 14 + «ask the fire marshal
in writing: hood? suppression? UL 2162 file number?» · plan review (8-201.11) + health permit + inspection · licensed gas
contractor · Class K + 2-A · grease interceptor · TPHC written procedure (3-501.19) · cold holding ≤ 41 °F · required public
notices · offer letters, I-9, W-4, state minimum wage · OSHA basics · CFPM (2-102.12) + food handler cards · 9 allergens
incl. sesame · no «gluten-free» promise · own drivers = W-2 + hired & non-owned auto · DoorDash/Uber Eats/Grubhub tiers ·
local packaging ordinances · ASCAP/BMI/SESAC · «Neapolitan-style» allowed; «VPN-certified» only after AVPN certification.
Tareas sin equivalente US (aceite irrellenable, Ley 1/2025, hojas de reclamaciones, SGAE…) → su sustituto de D146, nunca
el trámite español.

## 4. Tandas (c) piz_a (§1-5) ‖ (d) piz_b (§6-10) — PENDIENTES del Word ES

`docx_es_piz.json` es hoy un marcador «pendiente». En el paso 1c, `bp8.py extraer_docx` lo rellena con las 131 ranuras del
FT ES (61 traducibles: piz_a 29 · piz_b 32, la estructura de PAEL) y cada párrafo trae su nota (`datos_piz.DOCX_NOTAS`: la
sección + la FORMA del Bar EN; las 7 de §9 = 102-108 con sus temas de D147, la 108 cierra con la nota UK). **El bloque D11
del ES (ETG y sus 3 reglamentos) NO cruza**: en su ranura, «Neapolitan-style vs VPN-certified: what you can put on your
menu» (research §6.9). Tokens del caso: los de `tandas/piz_a.entrada.json` → `tokens` (110, con `inv_horno`, `inv_chimenea`,
`inv_campana`, `inv_amasadora`, `inv_mesa_fria`, `lena_ano`, `plataforma_pct`, `comision_pct`, `bebida_pct`,
`prime_cost_pct`).

## 5. Validación (Mac, solo JSON)

```bash
istats cpu temp | head -1
python3 scripts/productos-digitales/business-plans-en-8/bp8.py check_textos --tanda <TANDA>   # GPIZ-plan | GPIZ-check | GR | piz_a | piz_b
```

Itera hasta `OK (0 errores, …)` y revisa los AVISOS reales. Responde solo con: fichero escrito, nº de claves, resultado del
check y 3-5 decisiones que deban conocer las demás tandas.
