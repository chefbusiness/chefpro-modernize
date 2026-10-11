# Brief para los redactores (subagentes Sonnet) — Catering Business Plan Kit (EN)

> Sesión Claude Code, 11-oct-2026. F2 del producto 12 de la tienda EN (SPEC delta D71, D77, D78). Regla 1bis: los
> textos de producto los escriben subagentes Anthropic, **nunca bridge.py**. Carpetas (worktree del Mac):
> `scripts/productos-digitales/business-plans-en-4/` (= `BP4/`, datos y salidas del catering) y
> `scripts/productos-digitales/business-plans-en/` (= `BP/`, el código común y el brief de FT/CAF).
>
> **Cuatro tandas**, máximo 2 subagentes a la vez (`istats cpu temp` < 62 °C en el Mac):
> **tanda 1 = (a) GCAT-plan ‖ (b) GCAT-check** → **tanda 2 = (c) cat_a ‖ (d) cat_b**.
> **GM y GR no se escriben**: sus 335 + 7 cadenas son el motor común con el EN del Food Truck publicado que vale para
> catering (`BP4/textos_en/GM.json` y `GR.json`, los escribe `bp4.py preparar_tandas`). GR se **revisa** en (b).

**Cómo usar este brief**: el orquestador pega al subagente la sección **0 de `BP/BRIEF-TRADUCTORES.md`** (reglas
comunes: idioma, cero español, moneda, formato US, marca, cifras, pestañas citadas, glosario) + la sección **0** de
este fichero + la de su tanda. El subagente no hace commit y no toca nada más que su salida.

---

## 0. Lo que cambia frente a los briefs anteriores (manda sobre ellos en lo que choque)

**ESCRIBES, NO TRADUCES.** La fuente ES del circuito es el **FOOD TRUCK** (ranuras: celdas y párrafos del FT ES): su
`es` te dice el PAPEL de la celda o del párrafo, no su contenido. El contenido es de **catering**, desde
`BP4/fuente_es_cat.json` (checklist y plan de negocio del catering ES de línea B: concepto, mezcla particulares /
empresas, política comercial, operativa de un evento en 6 fases, riesgos) y research. **Ninguna cifra del ES de
catering** (D70). Cada cadena trae `propuesta_en` = el EN publicado del Food Truck en ESA celda: reutiliza lo que valga
(motor, impuestos, financiación) y reescribe todo lo que hable de food truck.

**Qué lees** (y nada más): tu entrada `BP4/tandas/<TANDA>.entrada.json`; `BP4/SPEC-delta.md` (D66-D80);
`BP4/F1-research-us-delta.md` §1, §4, §5, §6 y §8; `BP4/fuente_es_cat.json` (solo la parte de tu tanda); de lo
heredado, solo lo que tu entrada cite (`BP/SPEC.md` §1-§4); `BP/textos_en/glosario-GM.json`.

**Validación** (en el Mac, solo JSON):

```bash
istats cpu temp | head -1
python3 scripts/productos-digitales/business-plans-en-4/bp4.py check_textos --tanda <TANDA>
```

Itera hasta `OK (0 errores, …)` y revisa los AVISOS reales. Responde solo con: fichero escrito, nº de claves,
resultado del check y 3-5 decisiones que deban conocer las demás tandas.

**Concepto (D69): FULL-SERVICE OFF-SITE EVENT CATERER.** Produce en una **cocina comisaria compartida con permiso**
(horas + almacenaje + parking), transporta en **una furgoneta refrigerada usada** y sirve en el lugar del cliente.
Dos motores: **empresas** entre semana (drop-off, buffets de almuerzo, recepciones, fiestas de diciembre) y
**particulares** el fin de semana (bodas, ensayos, cumpleaños, celebrations of life). Estilos **drop-off · buffet ·
family-style · plated · stations**; diferencial = **chef-attended themed stations** (taco bar, carving, pasta, poke),
**nunca «12 cocinas del mundo»** ni su equipo. **Sin alcohol propio**: el cliente lo compra y lo sirven bartenders
certificados (TIPS / TABC) con liquor liability. **No desde casa** (cottage food y MEHKO no permiten catering).

**Motor permutado (D72), solo con rótulos.** `B4` = **events per year** · `B5` = **average price per guest (excl.
sales tax, service included)** · `B6` = **average guests per event**. Ingresos = eventos × precio × invitados; los
años 2-3 crecen en EVENTOS; el break-even sale en **events per year**; «coste variable por cliente» = **per guest**;
«clientes al año» = **guests per year**. El personal (D73, opción A) es fijo + cobertura por evento: `Staffing!B18` =
horas por evento, `B19` = personas por evento, `B20` = horas × personas × **eventos**.

**Vocabulario PROHIBIDO (gate D72, `check_textos` lo rechaza):** «per day», «operating days», «customers» (di
**clients** o **guests**; «corporate customers» sí), «truck» / «food truck» (di **van** / **refrigerated van**; un
competidor = «mobile food vendors»), «window» / «service window», «festival». Tampoco «street», «markets», «vending»,
«propane», «trailer», «average check» aunque el check no los pare.

**Cifras PROHIBIDAS (D70; las rechaza el check):** del catering ES 603.700 · 303.364 · 8.520 · 21.410 · 54.440 · 10.560
· 846.720 · 2.200 · 4.500 · 5.500 · 11.500 · «14 eventos/mes» · «55 %» de margen · «110 hitos» · «10 ejemplos
validados» · «96 proveedores» · «12 cocinas»; y los importes del caso FT EN (p. ej. $291,200). Las notas del libro
describen el **método** o usan `valor_us`; el caso US (research §8, calibrado D15) es **180 eventos × 60 invitados ×
$60** = $648,000 (`valor_us` de B4 dice 170: es el de research; el libro calibrado usa 180).

**Rótulos fijados** (`fijos_en` de tu entrada y POR_CELDA, ya los escribe `mapas.py`; si los citas, con esas palabras):
- `0. Assumptions`: «Events per year (year-1 average)», «Average price per guest (excl. sales tax, service included)»,
  «Average guests per event», «Price per guest incl. sales tax (calculated)», «Corporate catering marketplace share of
  sales (e.g. ezCater)», «Marketplace commission on those sales», «Commissary kitchen (hours + storage) & van parking,
  per month», «Commissary deposit (months)», «Useful life of the van and its upfit (years)», «Max events a year your
  kitchen and crew can handle» (B51, informativo), «Months of commissary rent BEFORE opening», «Contingency on the van,
  upfit and fit-out lines (%)».
- `Startup Costs` filas 7-23 (D74): Refrigerated cargo van (used) · Van upfit (racks, shelving, wrap) · Kitchen and
  refrigeration equipment (own) · Portable cooking and power (induction, burners, generator) · Van refrigeration unit +
  install · Commissary storage fit-out · LLC formation and legal · First-year permits and licenses · Health plan review
  (only if you lease your own kitchen) · Catering software + card reader · Smallwares, hotel and sheet pans · Opening
  inventory · Website, photography, launch marketing · Chafing dishes, insulated carriers, serving ware · Commissary
  deposit · Commissary rent before opening · Van and fit-out contingency.
- `3-Year P&L`: A2 «Base case — full-service event caterer»; A16 «Corporate marketplace commissions»; A22 «Commissary
  kitchen rent & van parking»; A27 «Van fuel, maintenance and inspections»; A34 «Food safety and alcohol service
  training (ServSafe, TIPS)»; A35 «Tastings for prospects»; A55 «Commissary / Sales».
- `Staffing` (D73): Owner / executive chef & sales · Sous chef / kitchen lead · Event staff (servers, bartenders,
  attendants; hourly W-2) · Prep cook / driver; A24 = nota W-2 / 1099 (FLSA, California AB5). `12-Month Cash Flow!O5`
  = Month 1 = mes de apertura (marzo en el ejemplo) y anticipos no modelados.
- Checklist: título «CATERING STARTUP CHECKLIST — FULL-SERVICE EVENT CATERER», «PHASE 2: KITCHEN, VAN & PERMITS».
- Pestañas: «0. Assumptions», «Startup Costs», «3-Year P&L», «Break-Even», «Scenarios», «Staffing», «Instructions»,
  «12-Month Cash Flow», «Financing» · checklist «Phase 1 - Business Setup», **«Phase 2 - Kitchen, Van, Permits»**
  (Excel corta a 31 caracteres: sin «&» en la pestaña), «Phase 3 - Equipment», «Phase 4 - Staff», «Phase 5 -
  Marketing», «Phase 6 - First 90 Days».

**Glosario de catering** (en tu entrada, sobre el de FT/CAF y el del financial-kit): evento → event · invitados →
guests · precio por invitado → price per guest · cocina comisaria → commissary kitchen / shared kitchen · furgoneta
refrigerada → refrigerated (cargo) van · presupuesto → quote / proposal · anticipo → deposit · degustación → tasting ·
estación temática → chef-attended (themed) station · emplatado → plated · servicio compartido → family-style · entrega
sin servicio → drop-off · camarero de eventos → event server / event staff · cargo por servicio → service charge ·
propina voluntaria → gratuity · alquileres → party rentals · espacio → venue · organizador → wedding planner / event
planner · mínimo de invitados → guest minimum · caja isoterma → insulated food carrier · cliente corporativo →
corporate client.

**Formato US** (como siempre): punto decimal, coma de miles, «%» pegado, sin símbolo de moneda en el xlsx, «$» solo en el
docx y en rangos de mercado con fuente; pestañas citadas entre comillas dobles rectas con su nombre EN.

---

## (a) Tanda GCAT-plan — xlsx del plan financiero (206 cadenas · ≈ 4.350 palabras ES; 128 celdas de tabla)

Entrada `BP4/tandas/GCAT-plan.entrada.json` → salida `BP4/textos_en/GCAT-plan.json` (`{"<id>": "<EN>"}` con TODOS los
ids y nada más).

- **78 cadenas de texto libre**: notas de la col. C de `0. Assumptions` (pistas por celda C4-C62: caso, marketplaces,
  comisaria, capacidad B51 informativa, cobro 14 días sin anticipos, alcohol 0 %), notas de `Startup Costs` (col. D),
  del P&L (A10/A11: ventas de comida y servicio / bebida sin alcohol), de `Staffing`, de `Scenarios` (E23: en el
  pesimista el coste real del personal de eventos baja con los eventos), del `Break-Even` (A29/A31: eventos al año por
  precio por invitado en columnas, con escalones de $10 / +$20, × coste variable por invitado en filas) y las filas
  1-12 de `Instructions` (A5: «0. Assumptions» es la hoja de mando: eventos, precio por invitado, invitados; A12: el
  Word usa las MISMAS cifras que el libro). Dos mensajes de validación compartidos por B6 (invitados) y B58/B59 (días):
  un texto que valga para los dos (título ≤ 32 caracteres).
- **128 celdas de las tablas de `Instructions`, una por celda** (`por_celda: true`):
  - **D18, filas 35-51 «WHY THIS MODEL IS BUILT THIS WAY»**: describe el MÉTODO del libro; parte de `propuesta_en`
    (la del Food Truck) y reescribe lo de clientes/día, días, ticket, camión o aparcamiento. Sin cifras del caso.
  - **D19, filas 55-68 «US CATERING BENCHMARKS (sourced) AND KIT ESTIMATES»** (Benchmark | Value | Source | Note), sin
    propuesta: cada fila lleva su pista (food cost 28-35 % · margen bruto 65-70 % · personal 25-35 % · neto 7-8 % ·
    bodas $80 por plato · $20-$80 por invitado y 50-75 invitados (Kit estimate) · almuerzo corporativo (Kit estimate) ·
    marketplace ~15 % (Kit estimate) · anticipos 25-50 % (Kit estimate) · sueldos · cocina compartida $15-$45/h ·
    inversión $20,000-$65,000 / $250,000+ · seguros Insureon · ratio de servers (Kit estimate)). `Source` = dominio de
    la fuente LEÍDA o «Kit estimate»; nunca «Fichero v1.1».
- Umbrales del P&L (D75, ya en el libro): margen bruto ≥ **60 %** (ver F2-NOTAS §4) · mercancía + desechables ≤ 35 % ·
  personal ≤ 38 % · comisaria ≤ 8 % · neto ≥ 5 %, «kit benchmark (editable estimate)».

```bash
python3 scripts/productos-digitales/business-plans-en-4/bp4.py check_textos --tanda GCAT-plan
```

## (b) Tanda GCAT-check — checklist (272 celdas · 68 tareas × 4 columnas) + revisión de las 7 reutilizadas GR

Entrada `BP4/tandas/GCAT-check.entrada.json` → **dos** salidas:

1. `BP4/textos_en/GCAT-check.json` (`{"<id>": "<EN>"}` con TODOS los ids): **68 tareas en 6 fases (11/13/12/10/12/10),
   no se añaden ni quitan**; cada celda es un id (`por_celda`): col. B = la tarea (corta, imperativa), C = responsable,
   D = plazo US, E = nota práctica. **La pista de cada fila dice qué tarea va en esa ranura** (D77: las 99 tareas
   válidas del ES condensadas + trámites US de research §6); el detalle sale de `fuente_es_cat.json` (fases ES 1-6;
   fuera las marcadas SOLO_ES y MULTICOCINA) y research §6. La `propuesta_en` (Food Truck) solo sirve para el tono y la
   longitud. P2 = cocina comisaria + permisos + furgoneta + seguros; P4 = I-9, W-4, new-hire reporting, workers' comp,
   food handler cards, OSHA, alcohol server certification; P5 = The Knot, WeddingWire, ezCater, Google.
2. `BP4/textos_en/GR.revision.json`: revisa `revisar_reutilizadas.GR` (7 cadenas: notas de la inversión y del P&L que
   hablan de «build-out», «menu price» o «delivery», títulos de las fases 1 y 3, el contador del checklist). Si
   `en_actual` vale para el catering, **no la incluyas**; si no, `{"<id>": "<EN corregido>"}` («build-out» → van upfit
   / fit-out; «delivery» → corporate catering marketplaces; «menu price» → quoted price). Si ninguna cambia: `{}`.

```bash
python3 scripts/productos-digitales/business-plans-en-4/bp4.py check_textos --tanda GCAT-check
python3 scripts/productos-digitales/business-plans-en-4/bp4.py preparar_tandas && \
python3 scripts/productos-digitales/business-plans-en-4/bp4.py check_textos --tanda GR
```

---

## Docx — reglas comunes de las tandas (c)-(d)

Las de `BP/BRIEF-TRADUCTORES.md` («Docx — reglas comunes»: un párrafo EN por párrafo ES, sin saltos de línea en el
cuerpo, subtítulos de una línea sin punto final, toda cifra del caso con su token `{{…}}`, importes y porcentajes de
mercado solo si están en research/SPEC con fuente), más:

- **Escribes cada párrafo** (D78): `notas_del_plan` y la `nota` de CADA párrafo (todos la tienen) dicen qué va en esa
  ranura; el `es` (food truck) solo da el papel y la longitud (±30 %). Contenido de `fuente_es_cat.json` (plan de
  negocio ES: párrafos y 7 tablas) + research §1-§6.
- **Tokens de catering** (usa estos, no los alias heredados): `eventos_a1/_a2/_a3`, `precio_invitado`,
  `precio_invitado_con_tax`, `invitados_evento`, `invitados_a1`, `ventas_evento`, `capacidad_eventos`,
  `equilibrio_eventos`, `equilibrio_caja_eventos`, `pesimista_/optimista_eventos`, `_precio`, `_invitados`,
  `marketplace_pct`, `marketplace_comision`, `cobro_dias`, `horas_evento`, `personas_evento`, `inv_vehiculo`,
  `inv_adaptacion`, `inv_frio`, `inv_equipo_cocina`, `inv_generador`, `inv_almacen`, `inv_llc`, `inv_permisos`,
  `inv_software`, `inv_menaje`, `inv_lanzamiento`, `inv_stock`, `inv_menaje_servicio`, y los del motor (ventas,
  márgenes, inversión, préstamo, DSCR, caja, payback, plantilla). `clientes_dia`, `ticket`, `dias`… son alias
  heredados de las mismas celdas: no los uses.
- Fuentes citables (research delta §4-§6, solo las leídas): restroworks.com (inversión $20,000-$65,000 con cocina
  compartida, $250,000+ con propia; sueldos), thefoodcorridor.com ($15-$45/h), galleysolutions.com (food cost 28-35 %,
  margen bruto 65-70 %, personal 25-35 %), itsacheckmate.com (neto 7-8 %), The Knot 2025 Real Weddings Study vía Fox
  Business ($80 por plato), insureon.com (pólizas), eldoradocounty.ca.gov (comisaria y permiso de catering en CA),
  cdtfa.ca.gov (sales tax del catering en CA), tax.ny.gov TB-ST-320 (gratuities), IRS Rev. Rul. 2012-18, HMRC VAT
  Notice 709/1 y gov.uk Temporary Event Notice. Lo marcado «(resumen)» en research → sin cifra o «Kit estimate».
- Fuera (L14): portada «España 2026», «ChefBusiness Consultoría», «96 proveedores validados», porcentajes sin fuente
  (38 % bodas multiculturales, 73 % millennials), «60+ páginas», multicocina de 12 cocinas. Financiación: préstamo
  bancario o SBA 7(a) a 7 años, «lender-ready, approval not guaranteed». Sin superlativos.
- El cierre (productos de la tienda) lo escribe el ensamblador (123-130); el 35 (anexos) nombra los 3 Excel.

## (c) Tanda cat_a — docx §1-§5 (29 párrafos · ≈ 2.950 palabras de ranura)

Entrada `BP4/tandas/cat_a.entrada.json` → salida `BP4/docx_en_cat_a.json` (`{"<i>": "<párrafo EN>"}`). §1 resumen con
tokens; §2 concepto y propuesta de valor (estaciones temáticas, dietas especiales, degustación, estilos de servicio);
§3 mercado desde el lado del cliente (bodas y empresas; temporada) sin tamaño de mercado inventado; §4 competencia
(caterers, restaurantes con catering, marketplaces; Porter y DAFO); §5 marketing (The Knot, WeddingWire, ezCater,
Google Business Profile, venta B2B a office managers y planners, degustaciones).

```bash
python3 scripts/productos-digitales/business-plans-en-4/bp4.py check_textos --tanda cat_a
```

## (d) Tanda cat_b — docx §6-§10 (32 párrafos · ≈ 3.770 palabras de ranura)

Entrada `BP4/tandas/cat_b.entrada.json` → salida `BP4/docx_en_cat_b.json`. §6 operaciones (comisaria, furgoneta,
equipo, operativa de un evento en 6 fases, transporte en frío / caliente); §7 equipo (puestos de `Staffing`, W-2,
service charge ≠ propina); §8 plan financiero SOLO con tokens (break-even en eventos al año); §9 legal con las 7 notas
(102-108; **el 108 cierra con la nota UK**: council 28 días antes, FHRS, VAT 20 % del catering de eventos (Notice
709/1), TEN £21 para el alcohol, 14 alérgenos); §10 conclusiones y hoja de ruta en el orden del checklist.

```bash
python3 scripts/productos-digitales/business-plans-en-4/bp4.py check_textos --tanda cat_b
```

## Después de las 4 tandas (orquestador)

```bash
python3 scripts/productos-digitales/business-plans-en-4/bp4.py preparar_tandas      # aplica GR.revision.json
python3 scripts/productos-digitales/business-plans-en-4/bp4.py check_textos --todas  # GM, GR, GCAT-plan, GCAT-check + 2 docx
```

Luego la tanda de `aplicar_en.py` (VPS): ver `F2-NOTAS.md` §6.
