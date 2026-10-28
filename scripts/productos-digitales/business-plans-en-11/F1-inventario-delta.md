# Coffee Cart Business Plan Kit (EN, $39) — inventario DELTA de F1 (frente a la Paella EN y al ES de la cafetería móvil)

> Sesión Claude Code, 28-oct-2026 (rama `feat/coffee-cart-business-plan`, apilada sobre la del ES en `d8984ffd`). JSON y código
> leídos en el Mac; xlsx/docx abiertos en el VPS (`/root/wt-coffeecart`, venv `/root/venv-guias`; el ES en F2 —`/root/
> wt-cafemovil`, `/root/tmp-caf-f2/`— solo leído). Todo lo de abajo está **medido** con el conjunto ya montado (paso 1a,
> `F2-NOTAS.md` §1-§3). Precedentes: **PAEL** = `../business-plans-en-7/` (Paella EN, LIVE), **BBQ** = `-6/`, **WED** = `-9/`
> (contrato), **PIZ** = `-8/` (bloque Escandallo), **ICE** = `-10/`.

## 0. Lo que manda (hipótesis del orquestador: «bbq de -6 + contrato de -9 + Escandallo de -8» → confirmada con un matiz)

1. **Se clona la PAELLA (`-7/`), no el BBQ**: es el BBQ con sus lecciones ya resueltas (M1-M6 de su revisión, cadena de
   diccionario, `GLB-check`, tokens con redondeo, cilindros…) y su EN cubre **las 959 cadenas del FT ES** (el BBQ en la cadena no
   aportaría nada). Mismo motor de eventos, misma fuente del circuito (**FOOD TRUCK ES**), mismos 7 parches (Break-Even a **±$1 /
   +$2**: B5 = $12.60), misma rejilla de 68 tareas y las mismas 61 ranuras del docx. **Conjunto nuevo: `cof`** (libros `COFP` /
   `COFC`, lanzador `bp11.py`).
2. **Diccionario en cadena POR CELDA: Paella LIVE → Catering publicado** (10 + 8 sha256). Medido: **0 fugas** en lo
   reutilizado (GM + GRP + GLP contra `RX_COF_NO`, cifras prohibidas y español).
3. **Contrato de WED** (`contrato_wed.py` + `check_contrato.py`, Letter, cabecera legal, Cooling-Off nunca afirmada), con UNA
   parte (el ES tiene 92 párrafos / 3,0 K palabras). **Escandallo de PIZ** (`calculadora_piz.hoja_escandallo`) dentro del
   esqueleto de `calculadora_pael.py` → **paso 1b** (la calculadora ES existe solo en borrador, §4).
4. **Fuente del circuito = FT ES, no el libro ES del café** (decisión, como BBQ y PAEL frente a sus ES 2.2): el ES de la
   cafetería es el motor 2.2 sobre la semilla FT con el `a.py` del parrillero (9 hojas, checklist de 80 tareas, versión en
   `Instrucciones!A52`); la línea EN de eventos traduce el FT (versión en A73, D18 35-51, D19 55-68, 68 tareas) y la research US
   ya está escrita en sus celdas. Ventaja extra hoy: **el EN no depende de que el libro ES esté cerrado**; del ES solo se toma
   contenido (checklist, Word por ranura, calculadora, contrato), re-extraíble (paso 1c).
5. **Una sola rama en código común**: `elif CONJUNTO == 'cof'` en `business-plans-en/mapas.py` (+ el mensaje de error), como la
   pizza y todos. **Regresión: 39/39 ficheros IGUAL** en los 10 conjuntos (`regresion_cof.sh`).

## 1. Recuento (medido, `textos_es.json` de 959 cadenas)

| Grupo cof | Cadenas | Palabras ES | Qué es | Va a |
|---|---|---|---|---|
| GM | 310 | 3.365 | motor cuyo EN (paella = BBQ = catering) no trae nada de paella | nadie (`textos_en/GM.json`) |
| GRP-plan | 59 | 1.050 | EN de la paella que vale con revisión: método D18 genérico, DV, notas de financiación | revisión en la tanda (a) |
| GLP-check | 186 | 759 | 183 celdas de tarea cuya propuesta vale tal cual (columna C mecánica: «Paella chef» → «Lead barista») + 3 textos | nadie |
| **GCF-plan** | **148** | 3.557 | 51 forzadas (notas del caso) + 36 forzadas del café + vocabulario de paella + **12 filas D19 nuevas** (48 celdas) | tanda (a) |
| **GCF-check** | **89** | 543 | las celdas que cambian de las 68 tareas (22 L · 42 A · 4 N) | tanda (b) |
| GX | 167 | 1.025 | pestañas, CLAVES, FIJOS, POR_CELDA, versión, pie, docProps | nadie |

Docx: 131 párrafos, **cof_a 29 ranuras / 2.954 pal. · cof_b 32 / 3.765**, cada una con la propuesta EN de la paella. Contrato:
92 párrafos ES → `textos_en/contrato_en.json`. **Hallazgo del paso 1a**: la lista de revisión de `preparar_tandas` no lleva
pistas → toda celda con pista de café que habría caído en GRP-plan (canal F16, umbrales F51/F56, E23, `Instructions!A12`,
filas D18 39-50, C25/C30/C63) se **fuerza** a GCF-plan (36 celdas).

## 2. Por qué la paella y no el bar móvil

El MBAR es el hermano más cercano en el **servicio** (bebida, drinks per hour, hosted / cash bar, COI) pero su EN quitó justo la
parte sanitaria (commissary, health permit, plan review, food handler, approved source) que un carro de café necesita (la leche
es TCS: el carro es una *mobile food unit*). Con la paella, 555 cadenas valen tal cual o con revisión; lo de bebida se reescribe
en las forzadas y en las pistas, y el MBAR entra solo como referencia de la research (COI, additional insured, motor de eventos).

## 3. Delta del libro (sobre la paella, celda a celda) — rótulo, importe y nota; **ninguna fórmula se mueve**

- **Bases de las fórmulas mandan** (`B31 = B7+B8+B11+B12+B15+B23`, `B32 = B9+B10+B16+B17+B20`, `B23 = (B7+B8+B11+B12+B15) ×
  B55`). Research §8 numeraba a su manera (contingencia «sobre 7, 8, 11, 13, 20»): se remapea (D222):

| Fila | Base | Paella | → Coffee cart (importe) |
|---|---|---|---|
| 7 · 8 | vehículo | quemadores · paelleras | **Espresso cart** (NSF, lavamanos, depósitos, bomba y filtro, nevera) $13,400 · **portable espresso bar** (+ nevera) $5,400 |
| 9 · 10 | equipo | kit de propano · fit-out | **2 máquinas** (2 grupos 220V + compacta) $15,700 · **4 molinos** $4,800 |
| 11 · 12 | vehículo | van usada · upfit | **remolque cerrado 6×12** $6,500 · wrap, enganche, anclajes y rampas $1,500 (vehículo de arrastre = el del dueño, $0) |
| 13 · 14 · 15 | — · — · vehículo | LLC · permisos · inspección | LLC $1,500 · permisos y certificaciones $1,400 · **plan review de la unidad móvil** $1,100 (Snohomish, leída) |
| 16 · 17 | equipo | software · smallwares | TPV y reservas $1,000 · batch brewer, cold brew, smallwares y estanterías $3,300 |
| 18 · 19 · 20 | — · — · equipo | stock · lanzamiento · montaje | inventario $1,500 · web, catas y lanzamiento $5,000 · **generador inverter 5,500 W + cables** $5,000 |

  = **$67,100** (= research) · contingencia **$2,790** · CAPEX **$71,290** · D&A ≈ $10,340.
- **Ventas**: A10/A11 «Coffee bar packages» 85 % / «Add-ons» 15 %; coste 12 % / 25 %; `B15` **compostable cups** 4 %.
- **Canal B16/B17 = festivales y farmers markets guest-pay** (5 % × 15 % de cuota del organizador), como el ES (ferias por el
  canal delivery), **no** los marketplaces de research §8 (van al marketing fijo). Rótulo FIJO «Festival & market organizer fees».
- **Fijos 26-35 ($21,000)**: permisos 1,500 · vehículo y remolque 3,500 · marketing 8,000 · contabilidad 2,400 · software 1,500 ·
  linens, signage & smallwares 600 · **teléfono e internet** 900 (fila 32) · **servicio de la espresso, filtros y muelas** 1,800 ·
  formación 400 · catas 400. `B26` $100 = combustible del generador, agua y hielo (= FT: «Generator» va en suministros, D18 fila 43).
- **Staffing (4 filas)**: Owner / Lead Barista & Sales 1 × 1.0 $3,813 · Lead barista (part-time W-2) 1 × 0.3 $1,040 · Event
  baristas 2 × 0.08 $527 · On-call barista / driver 1 × 0.08 $264 = $5,644/mes, 1.54 FTE; `B18` 7 h, `B19` 1.6.
- **Tesorería**: Month 1 = marzo (Flashquotes; julio 3.8 %); **O5, O20 y A34 reescritas para marzo** (la paella LIVE dice
  «April, July, October, January»: deuda de la pizza heredada por el GM); C67/E24 con la holgura bien definida.
- **D19 (14 filas)**: 2 con propuesta de la paella (65 shared kitchen, 67 Insureon) + 12 nuevas de research (Flashquotes ×5,
  GrindKit ×2, BLS ×2, Snohomish, cart-king, Coffee Cart Boys).

## 4. Calculadora (paso 1b) — duplicar las 4 hojas de la ES (`/root/tmp-caf-f2/calc_pub/`, borrador medido)

| ES (`calculadora_caf_es.py`) | EN (`calculadora_cof.py`, `coffee-cart-pricing-calculator.xlsx`) |
|---|---|
| `Escandallo` A1:O54 — 16 insumos × 10 bebidas, g de café por doble, PVP con IVA, food cost y semáforo, **coste de la mezcla** | **«Cost per Drink»** (`hoja_escandallo` de PIZ): beans $/lb, milks $/gal (whole, lactose-free, oat, soy), cocoa, chai, syrup, tea, sugar, cups 8/12/16 oz, lid, sleeve, stir stick, napkin × 10 drinks en oz y g; **18 g (0.63 oz) por doble**; menu price, COGS %, semáforo (20-30 %, grindkit.app) |
| `Calculadora` A1:F159 — canal Particular / Empresa / Feria, invitados, formato (bebidas por invitado), horario, horas, electricidad, generador, €/h + SS, km, IVA, ticket de feria y canon, días para el evento; **logística por la tabla de escalado** (baristas, cafeteras, grupos, molinos, kg, l, vasos, agua), **aviso eléctrico**, coste directo, precio por invitado, por hora y por bebida, cobros, cancelación por tramos | **«Pricing Calculator»** (esqueleto de PAEL): Private / Corporate / Festival or market (guest-pay), guests, service format, time of day (+25 % mañana), service hours, **110V / 220V / generator**, $/h + payroll taxes, miles × $/mile, sales tax + «does your state tax the service charge?», festival price per drink + organizer fee + **minimum sales guarantee**; drinks, baristas (50-65 por hora), stations, grinders, lb of beans, gal of milk, cups, gal of water, **amps and outlet needed**; cost, price per guest / per service hour / per drink, retainer 30-50 % + balance 14 days, 4 tramos «from X to less than Y», margen calculado |
| `Ejemplos` (boda, congreso, feria) · `Instrucciones` | **«3 Example Quotes»** (boda 130, empresa 90, festival guest-pay) a ±10 % de su línea de la mezcla ($15 / $12 / $6.50) · **«Instructions»** (Food Code: leche a 41 °F; W-2; sales tax; electricidad; Kit estimates) |

Autotest pycel multipestaña (PAEL: 509 comprobaciones). Tabla de escalado = la misma en calculadora, `Instructions` y Word §6.

## 5. Checklist (68 = 11/13/12/10/12/10 sobre las filas FINALES de la paella) — 22 L · 42 A · 4 N

| Fase | L | A (columnas) | N |
|---|---|---|---|
| P1 | contador, LLC, EIN, banco, licencia, CFPM | E: estructura, sales tax (hosted vs guest-pay), préstamo · BE: contrato (parte del modelo del kit), plan de seguridad (leche TCS 41 °F) | — |
| P2 | workers' comp, plagas | BE: commissary (agua, grises, leche, carro), MFU permit + plan review, fire marshal y generador, comprar el carro, remolque en el DMV + auto, equipar el remolque, política de alcohol, aguas grises · E: agreement, temporary permits, GL + COI | — |
| P3 | estanterías y FIFO | E: propio vs alquilado, vasos compostables · BE: cadena de frío, tostador y leches, smallwares, registro de temperaturas, evento de prueba | **máquinas y molinos · siropes y leches vegetales · segunda estación · agua de la espresso** |
| P4 | I-9 / W-4, new-hire, nóminas, food handler | E: pool W-2, propinas / tip jar · BE: baristas por evento, seguridad del barista, OSHA, protocolo y alérgenos | — |
| P5 | web, Google, The Knot / Zola, catas, salas, referidos | E: presupuesto con la calculadora, B2B (69.3 % corporativo), open house · BE: marca y carta, GigSalad / Thumbtack / The Bash, Instagram | — |
| P6 | saldo, reseña, revisión 90 días | E: llamada final + recuento 10 días · BE: comprobación de la sala (110V/220V, amperios), carga del remolque, montaje y servicio, recogida · BDE: pedidos y cold brew | — |

Columna C: «Paella chef» → «Lead barista», «Event captain» → «Lead barista», «Event staff» → «Event baristas» (mecánico).
Pestaña F2 **«Phase 2 - Permits & Commissary»** (30 car.; la de research tenía 36). Trámites US: research §6 (commissary
CA §114295 / WA RCW 43.20.148, plan review Snohomish, NFPA 96 para el generador «como ejemplo», cottage food fuera, vasos locales).

## 6. Docx: 61 ranuras de 131 (H1 37…109; §9 = 102-108)

| Nivel | Ranuras | Fuente |
|---|---|---|
| Casi literal (21) | 42 · 61 · 65 · 69-75 · 86 · 88 · 90 · 93 · 95 · 97-99 · 115-117 | EN de la paella + tokens |
| Adaptar (28) | 39 · 41 · 43 · 48 · 49 · 53-58 · 62-64 · 66 · 82 · 85 · 87 · 89 · 94 · 96 · 106-108 · 111-114 | EN de la paella + ES de la ranura |
| Nueva (12) | 40 concepto · 46-47 · 50 formatos · 78-81 commissary, equipo, operativa, calidad · **102-105** §9 (commissary, MFU permit, electricidad y generador, bollería / vasos / alcohol) | pista + research §1-§6 (+ ES cuando exista) |

Fijos: portada «Coffee Cart», línea 9 «…to launch a coffee cart and coffee catering company in the United States», [35] con
los 4 anexos (incluido el contrato), cierre = Coffee Shop Business Plan Kit · Mobile Bar Business Plan Kit · Coffee Shop
Checklists Kit Pro · HACCP Food Safety Kit Pro.

## 7. Capa de producto (F3) — `cp` del diff de la FINCA EN en `ae531f6b` (5 entregables, como aquí) + ICE para el hub

**Crear (11)**: `astro-site/src/data/productos-en/planes/coffee-cart-business-plan.ts` (desde `wedding-venue-business-plan.ts`) ·
`astro-site/src/pages/en/digital-products/coffee-cart-business-plan{.astro,/access.astro,/library.astro}` ·
`astro-site/src/islands/library/CoffeeCartBusinessPlanLibraryIsland.tsx` · `src/pages/CoffeeCartBusinessPlanDashboard.tsx` (claves
`plan-negocio`, `plan-financiero`, `calculadora-pricing`, `checklist-apertura`, `modelos-contrato`) ·
`astro-site/public/og-coffee-cart-business-plan.jpg` · `scripts/productos-digitales/emails/broadcast-coffee-cart-business-plan-
lanzamiento-en.{html,subject.txt}` · los 5 entregables en `astro-site/public/dl/coffee-cart-business-plan/`.
**Editar (≈ 30)**: `DigitalProductsHubPage.astro` (**sustituir** la tarjeta ES que meta la F3 del ES junto a la pizza; el
«Coming soon» de la l. 1070 lo quita el ES) · `digital-products-catalogue.json` · `tienda.ts` (FAMILIA `plan-negocio-cafeteria-
movil-eventos`, es + en) · `plan-negocio-cafeteria-movil-eventos.astro` (`locales` → `alternatesFamilia`) · `zona-app.ts` ·
`linkify-use-case.{ts,tsx}` · `sitemap-lastmod.json` · `llms.txt` · `llms-full.txt` · `netlify/functions/{get-download-urls,
verify-purchase,resend-access,admin-generate-access}.ts` (+ `equivalents-guide` común en descargas) · `netlify/shared/{product-
prices,payment-links}.ts` · `src/data/{products-catalog,productos-digitales-config,productos-changelog}.ts` ('2.2') ·
`src/pages/AdminGenerateAccess.tsx` · `footerLinks` de Coffee Shop, Mobile Bar, Food Truck, Catering y Coffee Shop Checklists EN
(+ FAQ «Is there a business plan for a coffee cart?») · `censo-entregables.py` (`PRODUCTOS_LETTER`) · `postprocess-transversal.py`
(`EXCLUIDOS`) · `tienda-gate.py` · `CALENDARIO-V2-SEMANAL.md` · `PAYMENT_LINKS_PENDIENTES_JOHN.md` · `GLOSARIO-JERGA-ES-EN.md` (✅ hecho).

## 8. Gotchas (nacen resueltos)

1. **O20 / A34 con los meses del FT** (paella y pizza LIVE): POR_CELDA para Month 1 = marzo. 2. **DV del checklist «— = pending»**
(deuda PIZ): no aplica: el molde FT de eventos ya dice «Use the dropdown: ✓, ☐, N/A» (medido en el dry-run). 3. **«128 events»** era una frase
vetada del BBQ y aquí es el pesimista: fuera de `FRASES_BBQ`. 4. **«180 events»** (catering) se desactiva si D15 lleva B4 a 180.
5. **Importes ES vs US**: no se vetan los que cita la research ni los redondos ≤ $50,000 ($25,000 del carro, $50,000 del Microloan).
6. **«stations», «trailer», «festival», «service window», «coffee truck» (formato)** valen aquí aunque la paella / el FT los vetaran.
7. **«Spanish»/«Spain»** vetados (el café no tiene origen español que citar). 8. Holgura cómoda (24 %): no se calibra; el pesimista
agota la caja por $487 y el docx lo dice. 9. El saldo mínimo cae en el **mes 7 (septiembre)**, no en julio. 10. La lista de revisión
de `preparar_tandas` no lleva pistas (§1). 11. Choque de merge con la F3 del ES en el hub EN y en `tienda.ts`: el EN rebasa después.

## 9. Esfuerzo previsto (F2 restante + F3)

| Paso | Quién | Tokens |
|---|---|---|
| 1b calculadora (4 hojas + autotest) cuando el ES calc pase su revisión · 1c re-extracción del ES | 1 opus (o sonnet) · VPS | 0,20 + 0,03 M |
| Tanda 1: (a) GCF-plan 148 + revisión GRP 59 ‖ (b) GCF-check 89 + contrato (3,0 K) | 2 sonnet | 0,22 M |
| Tanda 2: cof_a 29 ‖ cof_b 32 (≈ 6,7 K pal. con propuesta) | 2 sonnet | 0,20 M |
| Paso 3 + gates + UNA revisión opus + 1 ronda | VPS + 1 opus | 0,25 M |
| F3 (2 sonnet) + PR + gates + link + LIVE | | 0,50 M |
| **Total** | | **≈ 1,4 M** (+ F1 ≈ 0,5 M) |
