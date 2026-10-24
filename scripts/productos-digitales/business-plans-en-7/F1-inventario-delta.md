# Paella Catering Business Plan Kit (EN, $39) — inventario delta de F1 (frente al BBQ)

> Sesión Claude Code, 24-oct-2026 (rama `feat/paella-catering-business-plan-en`, apilada sobre la del BBQ). JSON y código
> leídos en el Mac; los 12 ficheros ES del paellero, abiertos en el VPS (`/root/wt-paella`, venv `/root/venv-guias`, nada
> escrito). CPU del Mac < 49 °C. **Delta frente al BBQ** (`../business-plans-en-6/`, conjunto `bbq` = **BBQ §n** de su
> inventario), no frente al catering. Los recuentos de §1 salen de aplicar al EN del BBQ una regex de «vocabulario y caso
> del BBQ que no vale para la paella» (smoker, pitmaster, pit, brisket, ribs, meat, carving, trailer, wood, BBQ, $38,
> 150 events…): es una cota; la revisión semántica la hacen los redactores. El docx del BBQ se midió sobre los borradores
> `docx_en_bbq_{a,b}.json` del worktree del BBQ (sin commit aún): las cifras del docx son provisionales.

## 0. Lo que manda (propuesta para la SPEC)

1. **Diccionario en cadena, por celda**: propuesta = **EN del BBQ en esa celda** (`../business-plans-en-6/textos_en/*.json`
   + `GRC-plan.revision.json` y, por ranura, `docx_en_bbq_{a,b}.json`); si el BBQ no tiene EN en esa celda, el **EN
   publicado del catering** (los mismos 8 sha256 de `mapas_bbq.py:169-178`). Por celda y no por id: los ids de
   `textos_es.json` se mueven si cambian FIJOS o POR_CELDA (BBQ F2-NOTAS §7.8).
2. **Código = clon del `bbq`**: misma fuente del circuito (FT ES), mismo motor de eventos y **los mismos 7 parches**, con
   el Break-Even también en **±$3 / +$6** (B5 = $40, cerca de los $38 del BBQ): `PARCHES_FORMULA` se copia sin cambios.
3. **Cuatro ficheros**, como el BBQ: la calculadora cambia las pestañas de carne por **«Paella Yield & Pan Sizing»** y
   **«Shopping List by Guest Count»**. El valor del manual técnico ES está en el cálculo (paelleras, arroz, caldo, gas,
   paelleros), igual que en el BBQ (BBQ §2).
4. **Del ES no se reutiliza ninguna cifra.** Comprobado: el **docx ES 2.2 del paellero está en las mismas 61 ranuras**
   que el del parrillero (`paellero-2_2/textos/pae_es_{a,b}.json`: 29 + 32 claves, idénticas a `par_es_{a,b}.json` y a
   `docx_en_cat_{a,b}.json`). El docx publicado tiene la misma forma: 142 párrafos, 11 H1 (10 + anexo CCAA sin ranura),
   7.990 palabras (parrillero: 142 / 11 / 8.175). Y su **checklist ya está en Python** como el del parrillero:
   `paellero-2_2/datos_checklist.py`, 83 tareas 12/16/14/10/16/15, importable sin abrir el xlsx.

## 1. Diccionario, código y recuento

**Ficheros** (en `business-plans-en-7/`; código común: solo la rama `elif CONJUNTO == 'pael'` de `business-plans-en/mapas.py`,
copia de `:1225-1231` + el mensaje de `:1233`):

| Fichero | Origen | Cambio |
|---|---|---|
| `mapas_pael.py` | copia de `mapas_bbq.py` (354 l.) | PLANES (`paella-catering-business-plan`, `slug_es` `plan-negocio-paellero-eventos`, env `…_PAELLA_CATERING_BUSINESS_PLAN`), LIBROS `PAEP`/`PAEC`, pestaña F2 **«Phase 2 - Propane & Permits»** (27 car.). `_cargar_bbq()` + `A_BBQ = {'PAEP': 'BBQP', 'PAEC': 'BBQC'}` delante de `_cargar_cat()`; `SHA_BBQ` (8 ficheros del BBQ: `textos_es.json`, 4 `textos_en`, la revisión y los 2 docx) junto a los 8 del catering. `RX_REESCRIBIR` = vocabulario BBQ + cifras del caso BBQ + lo que sigue vetado del catering (plated, executive / sous chef, induction, refrigerated van…); **salen** `burners?`, `stations?` y `chef` precedido de «paella». `FORZAR_TRADUCTORES` = los 51 del BBQ. `D19_CON_PROPUESTA` = 58, 60, 62, 64, 65, 67 (§3). PARCHES iguales. `PRESTAMO_SEMILLA` = 62,400 |
| `datos_pael.py` | estructura de `datos_bbq.py` (1.311 l.) | ≈ 44 GX a reescribir (FIJOS 10 de 31 y POR_CELDA 34 de 66 llevan vocabulario o caso del BBQ), caso US, 68 pistas, 14 filas D19, 61 `DOCX_NOTAS` con el **párrafo ES 2.2 del paellero de la misma ranura**, tokens propios (`inv_*` renombrados según §3), `RX_PAEL_NO`, cifras (§7), glosario = research §9 |
| `bp7.py` · `barrido_pael.py` · `fuente_pael.py` | copias de `bp6.py` · `barrido_bbq.py` · `fuente_bbq.py` | `verificar` exige 272 celdas en GPA-check y los 16 sha256. `fuente_pael.py`: checklist de `paellero-2_2/datos_checklist.py`, ranuras de `pae_es_{a,b}.json`, manual (10 tablas), carta 12, experiencias y contrato por python-docx en el VPS |
| `calculadora_pael.py` | sobre `calculadora_bbq.py` (1.194 l.) | §4: cambian 2 pestañas y la mitad de las entradas; esqueleto, cobro, cancelación y autotest se quedan |
| `BRIEF-TRADUCTORES.md` | copia del brief del BBQ | §0 «qué cambia frente al BBQ» + glosario de research §9 completo pegado |

**Recuento** (959 cadenas del BBQ; GX aparte). Grupos propuestos: `GM` · `GRB-plan` (EN del BBQ o del catering que vale
con revisión) · `GPA-plan` · `GPA-check`; `REVISAR_EN_TANDA = {'GPA-plan': ('GRB-plan',)}`.

| En el BBQ | n | Para la paella | → Grupo pael |
|---|---|---|---|
| GM | 312 (3.537 pal.) | **312 valen tal cual** (son EN del catering sin vocabulario BBQ) | GM |
| GRC-plan (+6 revisiones) | 79 | **74 valen** con revisión · 5 cambian (c0422 «smoked meat», c0437-38 leña, c0461 «trailer fuel», c0465 «BBQ packages») | 74 GRB-plan · 5 GPA-plan |
| GBQ-plan | 128 | 3 limpias y sin forzar → GRB-plan · **51 forzadas** (notas del caso: C4-C8, C11-C15, C18, C24-C27, C44-C62, Startup D7:D20, P&L F10-F55, Staffing J) · **18 con vocabulario BBQ** · **56 D19**: 24 con propuesta del BBQ (filas 58, 60, 62, 64, 65, 67) y 32 nuevas (8 filas) | 3 GRB · 125 GPA-plan |
| GBQ-check | 275 | 196 celdas limpias · 79 cambian: 54 de fondo + 25 solo por «Pitmaster» en la columna C. **Por tarea (lectura): 42 L · 23 A · 3 N** (§5) | GPA-check |
| Docx (borradores) | 61 ranuras, ≈ 7.800 pal. (a 3.340 · b 4.473) | 8 limpias (71, 72, 74, 75, 88, 90, 97, 98) · 2 solo nombre · 51 con vocabulario BBQ → **22 casi literales · 27 adaptadas · 12 nuevas** (§6) | pael_a 29 · pael_b 32 |

**Plan: 389 de 519 cadenas (75 %) valen tal cual o con revisión** (GM 312 + GRB-plan 77), 74 se reescriben sobre la
propuesta del BBQ (51 forzadas + 23 con vocabulario) y 56 forman la D19 (24 con propuesta, 32 nuevas). Frente al BBQ (128
escritas + 79 revisadas sobre propuesta del catering), la carga de escritura baja ≈ 40 %: la propuesta ya es comida en
eventos, con commissary, furgoneta usada, W-2, deposit y service charge.

## 2. Contenido ES del paellero aprovechable (12 ficheros, abiertos en el VPS)

| Fichero ES | Vale para el EN | Fuera |
|---|---|---|
| Plan docx (61 ranuras) | Concepto «la paella se cocina en el evento, caldos y sofritos en la cocina de apoyo» [40], fases del evento [50] [78-80], plan B de viento y lluvia [112], Porter, DAFO, embudos y degustación | €, IVA 10 %, RD, fijos discontinuos, ayuntamientos y contrato menor, anexo CCAA [119-128] |
| Plan financiero xlsx | Solo la idea de **paelleras y quemadores como partidas separadas** (2.400 € / 2.100 € en el ES): apoya §3 | Todo el caso (105 × 94 × 16 €) |
| Checklist (83) | 73 adaptables (§5) | 10 enteras (F1·3, 4, 5, 8, 10, 11 · F2·3 · F4·2, 7 · F5·14) y 8 parciales (F1·7, 9, 12 · F2·10, 11, 14, 16 · F5·10) |
| Calculadora (3 hojas) | `TABLA` diámetro → raciones, arroz, caldo (`calculadora_pae_es.py:47-49`); **paelleros = paelleras ÷ 3**, ayudante desde 4 paelleras u 80 invitados; gas por paellera (1,3 kg); cancelación por tramos; margen calculado | €, IVA, SS 33 %, €/km, ayuntamiento, «show cooking +8 %» (aquí cocinar en vivo es la base) |
| Manual técnico (10 tablas) | **Escalado de 8 diámetros** (50-150 cm), **cubrir 50/100/200 invitados**, **12 paellas** (arroz, minutos, ingredientes, caldo, fases), cronograma del evento (15 pasos), **matriz de alérgenos 12 × 8**, tipos de arroz, gas frente a leña | Arroces por marca, °C, normativa ES |
| Carta 12 paellas y arroces | → **8 menu styles**: seafood · chicken & seafood · chicken & chorizo · Valencian (rabbit «on request») · farm vegetable (vegan) · paella negra · lobster & seafood (premium) · «senyoret» → easy-eat peeled seafood | Meloso y caldoso de bogavante, montaña, alicantina, a banda (sin demanda US leída); fideuá → solo nota de menú como «fideua (noodle paella)» |
| 10 experiencias | → tipos de evento del docx §2: backyard paella party, boda con tapas hour, corporate live cooking, rehearsal dinner, first communion / baptism / quinceañera, cumpleaños, drop-off corporativo, premium seafood & tapas, vegana | Fiesta del pueblo, Falles, show cooking de hotel |
| Catálogo equipamiento · Guía 8 sistemas | Orden de compra del docx §6 (paelleras por tamaño, quemadores de 3 aros con patas, propano, carpa de la estación, utensilios); gas = base, leña solo con permiso, inducción en interiores (Kit) | Marcas (Garcima, Vaello, GGM, Arcos), precios €, roadmap food truck |
| Contrato · Proveedores (88) · Equivalencias | Contrato → tarea P1 (deposit, tramos, recuento final, plan B de viento y lluvia, fuego no autorizado, vino del cliente). Proveedores: solo categorías | TRLGDCU, Bizum, marcas ES, guía ES ↔ LatAm |

## 3. Delta del libro (sobre el BBQ, celda a celda)

**Inversión (filas 7-20)**: las bases son fijas: vida del vehículo `B31 = B7+B8+B11+B12+B15+B23`, equipo
`B32 = B9+B10+B16+B17+B20`, contingencia `B23 = (B7+B8+B11+B12+B15) × B55` (BBQ §3). Research §8 numera 7 pans · 8 burners ·
9 van · 10 upfit · 11 propano y estima la contingencia «sobre 7-11» ($2,620): con las fórmulas, la van caería en la base de
equipo (5 años). **Propuesta: los huecos del BBQ** (el equipo de cocción ocupa los del smoker trailer):

| Fila | Base | BBQ | → Paella (importe = research §8) |
|---|---|---|---|
| 7 · 8 | vehíc. | Smoker trailer · upfit | **Paella burners & stands** (four 3-ring burners with legs, one rolling stand, wind guards) $2,500 · **paella pans** (2 × 36 in, 3 × 32, 3 × 26) $1,800 |
| 9 · 10 | equipo | Live-fire rig · commissary fit-out | **Propane & fire-safety kit** (eight 20-lb cylinders, regulators, hoses, 2 extinguishers, fire blanket) $900 · commissary prep & storage fit-out $1,500 |
| 11 · 12 | vehíc. | Used cargo van · upfit | igual: van $18,000 · upfit (shelving, **upright cylinder racks**, tie-downs, wrap) $3,000 |
| 13-20 | — | LLC… holding | LLC $1,500 · permits $2,000 · **15 fire/event permit & propane setup inspection (if required)** $500 (base vehículo, como el plan review del catering) · software $1,200 · smallwares & paella tools $1,800 · inventory $2,500 · launch & bridal show $4,500 · **event setup & holding** (canopy for the cooking station, tables, handwashing station, coolers, chafing dishes, insulated carriers) $3,000 |

Total $44,700; contingencia 10 % × 25,800 = **$2,580** (no $2,620) → CAPEX ≈ **$49,480** (la research decía ≈ $49,500);
D&A ≈ 28,380 / 7 + 8,400 / 5 ≈ **$5,700** (no $5,200). Rótulos: A23 «Burner, pan, van and fit-out contingency» · A31 «Paella
burners, pans, van and fit-outs (depreciated over the vehicle life)» · A44 «Useful life of the burners, pans, van and
fit-outs» · A55 «Contingency on the burner, pan, van and fit-out lines (%)».
**Resto (GX y valores)**: A11 «Paella packages (live-cooked paella, salad & bread, paella chef & staff)» 88 % · A12
«Add-ons (tapas, desserts, non-alcoholic sangria & drinks, rentals, extra hours, travel fees)» · A15 «Disposables & cooking
fuel» 3,5 % · A22 «Commissary kitchen rent & equipment storage» $1,100 · A24 utilities sin propano (= BBQ) · A27 «Van fuel,
maintenance and registration» $5,000 · A33 «Pan, burner & hose replacement» $1,000 · A51 «Max events a year your paella
crew can handle» 200 · personal de research §8 (Owner / Paella Chef & Sales · Lead cook / second paella chef · Event staff ·
Prep cook / driver; 2.1 FTE, $8,026/mes; `B18` 9 h, `B19` 2,5) · fijos $25,100 · estacionalidad y escenarios de research §8.
Umbrales `E51:E56` = BBQ (58 / 35 / 38 / 7 / 5 %). **D19** (14 filas): se quedan del BBQ 58 neto · 60 food cost · 62
marketplace (Kit) · 64 OEWS · 65 shared kitchen · 67 Insureon; nuevas 55 precio por persona en vivo · 56 menú español con
personal · 57 arroz por invitado (Kit) · 59 invitados por paellera (Kit) · 61 paelleras y quemadores (Kit: tienda.com solo
en resumen) · **63 paella chef y attendant cobrados aparte** (cafesevilla, leída; la del BBQ citaba operadores BBQ) · 66
mínimos · 68 propano y desechables por evento (Kit).

## 4. Delta de la calculadora (`calculadora_pael.py` sobre `calculadora_bbq.py`)

- **Se quedan**: esqueleto de 5 pestañas, entradas verdes con DV, personal por evento, alquileres, millas, event / travel
  fee, comisión, margen objetivo, service charge, sales tax + «¿grava el service charge?», depósito, 4 tramos de cancelación,
  retención por tramo, margen calculado, «Instructions», docProps, Letter y autotest multipestaña (581 comprobaciones).
- **Cambian**: paquete (3: drop-off paella · live paella party · full-service live paella con tapas hour); el interruptor
  «Live pit on site» → **«Tapas hour?»** con coste por invitado; las 5 líneas de carne → **estilo de paella** (8, lista de la
  hoja 2); oz de **arroz crudo** por invitado (3,25; Kit 3-3,5); **tamaño de paellera** (lista); salad & bread, desechables,
  **propano** (lb por paellera × $/lb; cilindros de 20 lb); paella chefs = paelleras ÷ 3 y ayudante desde 4 paelleras u 80
  invitados (manual ES, Kit); servers 1 por 25 invitados (miamigrillcatering, leída).
- **«Paella Yield & Pan Sizing»**: tamaños 18-40 in (cm entre paréntesis), invitados por paellera (Kit: 36 in = 40 · 32 = 30 ·
  26 = 18; el resto, de la tabla ES convertida), arroz y caldo por paellera, aros del quemador; 8 estilos con oz por invitado
  de cada ingrediente, **$/lb en blanco** (lo teclea el usuario; si falta, coste por invitado del estilo = Kit de research §5:
  $5 chicken & chorizo · $8-9 seafood · $15-18 lobster), **mínimo del Food Code en columna aparte** (165 °F aves · 145 °F 15 s
  pescado y marisco · 155 °F chorizo crudo mexicano; hot holding 135 °F o TPHC 4 h) y alérgenos típicos («verify with your
  recipe and suppliers»).
- **«Shopping List by Guest Count»**: tu evento + 40 / 80 / 150 / 300: paelleras por tamaño, quemadores, arroz (lb), caldo
  (gal), ingredientes del estilo (lb), azafrán (g), limones, pan, ensalada, alioli, propano y cilindros, platos y cubiertos,
  coolers y hielo para el marisco, chafing de tapas, equipo humano. **«3 Example Quotes»**: drop-off corporativo 30 inv. ·
  backyard party 45 · boda 110 con tapas hour, cada uno a ±10 % de su línea de la mezcla ($22 / $34 / $52).

## 5. Delta del checklist (68 = 11/13/12/10/12/10 sobre las ranuras del BBQ; L literal · A ajuste · N nueva)

| Fase | L | A | N |
|---|---|---|---|
| P1 (11) | 6, 7, 8, 10, 11, 12, 15 (7) | 5 (notas: llama abierta en eventos, no smoker) · 9 (sales tax sin «smoked meats») · 13 contrato (deposit, recuento, **plan B de viento y lluvia**, fuego no autorizado) · 14 plan HACCP: **arroz TCS, TPHC 4 h por escrito, 145 / 165 °F, shellstock tags** (4) | — |
| P2 (13) | 6, 8, 13, 14, 15, 17 (6) | 5 commissary (sofrito, caldo, marisco limpio; guardar paelleras y **¿cilindros?**) · 7 permiso + **«¿cabe cocinar el arroz en el evento?»** (limited food preparation, CA) · 9 fire marshal: propano fuera de la carpa de invitados, cooking tents (VA 20 ft como ejemplo) · 10 van usada e inspección · 11 van + inland marine de paelleras y quemadores · 12 upfit con racks verticales y ventilación · 16 residuos, aceite y conchas, sin cenizas (7) | — |
| P3 (12) | 5, 6, 8, 12, 13, 14, 15 (7) | 10 marisco de approved source con etiquetas + cash-and-carry · 16 prueba por tamaño de paellera: arroz, caldo y propano reales (2) | 7 **paelleras y quemadores**, prueba de cada aro · 9 **kit de la estación** (paletas, wind guards, mesa, carpa) · 11 **arroz bomba, azafrán y despensa española** (importador) (3) |
| P4 (10) | 5-10, 14 (7) | 11 propano (fugas, extintores, corte) · 12 OSHA: quemaduras, calor, peso de paelleras y cilindros · 13 **guion del show** (socarrat reveal) y alérgenos: crustacean shellfish y fish (3) | — |
| P5 (12) | 6-12, 14, 15, 16 (10) | 5 marca y menu styles · 13 fotos y vídeo de la paella en vivo (2) | — |
| P6 (10) | 5, 11, 12, 13, 14 (5) | 6 visita: suelo llano, viento, distancia a la carpa, agua · 7 marisco 1-2 días antes con etiquetas, sofrito y caldo la víspera · 8 cocinar a 165 / 145 °F, servir ≥ 135 °F o TPHC, **sobras a la basura** · 9 llegar 2-3 h antes, encender, cocinar ≈ 1 h, servir · 10 limpiar y aceitar paelleras, cerrar cilindros (5) | — |

**Total 42 L · 23 A · 3 N** (BBQ: 35 · 25 · 8). Columna C «Pitmaster» → **«Paella chef»** (≈ 20 filas, mecánico). Títulos: libro
«PAELLA CATERING STARTUP CHECKLIST — LIVE PAELLA CATERER», F2 «PHASE 2: COMMISSARY, PROPANE STATION, FIRE RULES & PERMITS».

## 6. Docx: 61 ranuras (H1 37…109; §9 = 102-108)

| Nivel | Ranuras | Fuente |
|---|---|---|
| Casi literal (22) | 42 · 56 · 61 · 65 · 69-75 · 86 · 88 · 90 · 93 · 95 · 97-99 · 115-117 | EN del BBQ + tokens (97-99: el pesimista agota la caja) |
| Adaptar (27) | 39 · 41 · 43 · 48 · 49 · 53-55 · 57 · 58 · 62-64 · 66 · 82 · 85 · 87 · 89 · 94 · 96 · **106** (sangría) · 107 · 108 · 111-114 | EN del BBQ + ES de la ranura |
| Nueva, núcleo paella (12) | 40 concepto (cocinar en vivo ES el producto) · 46-47 propuesta · 50 menu styles y tipos de evento · 78-81 commissary, equipo, fases, seguridad del arroz · **102-105** §9 | ES 2.2 de la ranura + research §1, §6 |

Fijos: portada «Paella Catering», línea 9 «…to launch a live paella catering company in the United States»,
`PRODUCTOS_CIERRE` = los del BBQ (Catering · Food Truck · Food Cost · HACCP). Anexo CCAA: sin ranura (fuera).

## 7. Cifras y vocabulario prohibidos (gate: `cifras_prohibidas()` + `RX_PAEL_NO`)

- **ES paellero** (`paellero-2_2/cifras_caso_es.json`): importes ≥ 10.000: 10.800 · 12.392 · 12.417 · 14.579 · 14.829 · 15.794 ·
  16.803 · 18.582 · 19.772 · 20.425 · 41.777 · 42.686 · 51.600 · 55.097 · 57.893 · 63.111 · 71.487 · 85.448 · 100.027 · 108.375 ·
  128.987 · 134.903 · 152.768 · 157.920 · 173.712 · 184.135 · 212.500 (18.000 y 20.000 chocan con la van y quedan al filtro
  `propios`); los pequeños (1.504, 1.750, 2.100, 2.400, 3.354, 3.747, 4.000, 6.130, 8.376) **solo con €**. Frases: «105
  events», «94 guests», «16 €/€16», «90 / 86 events», «81 / 77 guests», «85 / 125 events», «22.4 %», «DSCR 1.72», «83 tasks»,
  «88 suppliers», «11 deliverables» + las de research §8 («fiestas populares», «contrato menor», «autónomo»…).
- **Caso BBQ**: `_cifras_caso('../business-plans-en-6/cifras_caso.json', 'bbq')` + frases «150 events», «$38 per guest», «75
  guests», «220 events», «128 events»; catering, mobile bar y FT, heredados.
- **Vocabulario**: `RX_BBQ_NO` heredado, con tres cambios (chef, Spain, stations; SPEC) + **BBQ** (smoker, smoked, pitmaster,
  pit, brisket, pulled pork, ribs, bark, smoke ring, live-fire, live pit, carving salvo «ham carving station», carver,
  trailer, tow vehicle, pickup, whole hog, pig roast, tri-tip, picanha, asado, churrasco, butcher paper, rub, BBQ, barbecue,
  grill) + **ES paellero** (paellero/a, garrofó, ferraura, bogavante, senyoret, «DO», Garcima, Vaello, finca, fiesta del pueblo,
  Falles, IDAE). Palabras con tilde que el detector común rechaza (`mapas.py:935`): jamón, fideuà, pimentón, española →
  **Serrano ham, fideua, smoked paprika, Spanish tortilla**.

## 8. Deuda del ES (solo anotada)

1. **«Paella valenciana DO» y «Paella vegetal DO»** (carta, manual, calculadora `ARROCES`, landing): la DO ampara el arroz
   (Arroz de Valencia), no el plato. Corregir en la próxima actualización ligera del paellero ES.
2. La errata del parrillero en [98] (`{DIAS_COBRO}` para proveedores) **no está** en el paellero: dice «en un plazo
   parecido». En el EN, igualmente, `{{pago_dias}}` para los pagos (D113 del BBQ).

## 9. Tandas previstas, esfuerzo y riesgos

| Paso | Contenido | Tokens |
|---|---|---|
| Paso 1 (1 opus, Mac + VPS) | rama `pael`, clon de los 6 ficheros, cadena de diccionario, ≈ 44 GX, caso, 68 pistas, 14 D19, 61 notas, calculadora (2 pestañas nuevas), dry-run y D15 | ≈ 0,35 M |
| Tanda 1 (2 sonnet ‖) | (a) GPA-plan **130** (≈ 3.700 pal. de propuesta; ≈ 2.300 a escribir) + revisión de GRB-plan **77** ‖ (b) GPA-check 275 (26 tareas que cambian, ≈ 900 pal., + columna C) | ≈ 0,2 M |
| Tanda 2 (2 sonnet ‖) | pael_a 29 ‖ pael_b 32: ≈ 7.500 pal., de las que ≈ 1.800 nuevas (12 ranuras) y ≈ 3.300 adaptadas | ≈ 0,2 M |
| Gates + revisión | G1-G9, autotests, regresión con BBQ, una revisión opus | ≈ 0,25 M |

**Riesgos**: (1) **Dependencia del BBQ en curso**: su docx_b se está escribiendo y su revisión D111 puede cambiar textos
después de construir las propuestas → fijar `SHA_BBQ` con el BBQ cerrado y verde; si deriva, `bp7.py verificar` avisa y se
rehace `preparar_tandas`. (2) **Legal del evento**: arroz TCS y *B. cereus*, TPHC de 4 h, limited food preparation (solo CA
leída), propano y carpas (solo VA leída), shellstock tags, alérgenos US frente a UK, GL sin exclusión de llama abierta →
«check with your county / fire marshal», nunca una cifra nacional. (3) **Fuga del BBQ**: las propuestas son texto BBQ
(meat, pounds, carving, pit, trailer) con cifras del caso BBQ dentro de notas («The example is a full-time pitmaster…») →
`RX_PAEL_NO` + cifras BBQ + lectura entera del checklist. Menores: rendimientos todos «Kit estimate» (la research solo leyó
resúmenes); D&A y contingencia cambian con §3 (D15 se recalcula); canibalización con Catering y BBQ (la landing diferencia
por paella en vivo, paelleras y arroz por invitado); altas en `PRODUCTOS_LETTER` y `EXCLUIDOS` antes de G9.
