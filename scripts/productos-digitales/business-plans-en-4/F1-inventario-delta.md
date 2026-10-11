# Catering Business Plan Kit (EN, $39) — inventario + mapeo de F1

> Sesión Claude Code, 11-oct-2026. Fuente: `astro-site/public/dl/plan-catering-tematico-eventos/` (ES, **línea B**, 45 €),
> leída con openpyxl / python-docx **en el VPS** (`/root/wt-cat`, venv `/root/venv-guias`). Script reproducible
> `inventario_cat.py` → `inventario_cat.json` (sha256 del JSON `d8dfc057…`); compara además con los 5 libros EN publicados.
>
>     ssh vps 'cd /root/wt-cat/scripts/productos-digitales/business-plans-en-4 && /root/venv-guias/bin/python inventario_cat.py'
>
> sha256 de las 4 fuentes en alcance: plan xlsx `98ad8949…391e37` · calculadora `8e2d3c65…bb6fa4` · checklist
> `5aa1a1da…ee4fc077` · docx `f079c60c…ed2dd575` (los 11 en el JSON). Fuera de alcance (D: decisión del orquestador):
> contratos, 12 menús, manual multicocina, catálogo, plantilla de proveedores, guía de especialización, 12 conceptos.

## 0. Lo que manda

1. **Gemelo = FOOD TRUCK EN** (no Bar/CAF/REST/PAN): es el único libro EN sin local a pie de calle, con **alquiler de cocina comisaria** (`0. Assumptions!B24`), vehículo depreciable, permisos de unidad móvil y de eventos temporales, 260 días operativos y un puesto de «Events and festival help». Fuente ES del circuito: `plan-negocio-food-truck/` (FT ES).
2. **El motor de ingresos se reinterpreta SOLO CON RÓTULOS** permutando los drivers: `B4` (lo que crece) = **eventos/año**, `B5` = **precio por invitado**, `B6` = **invitados por evento**. Ingresos = B4×B5×B6 (conmutativo); el break-even sale en **eventos/año** sin tocar fórmulas. Cambian **2 fórmulas obligatorias** (+3 opcionales). Detalle en §3.
3. **Del ES de línea B no se reutiliza NINGUNA cifra ni fórmula**: el modelo ES no es financiable (margen neto 50 %, break-even de 5,5 eventos/año, sin alquiler de cocina ni sueldo del dueño). Se reutiliza el **contenido**: concepto, mezcla particulares/empresas, política comercial, operativa de un evento en 6 fases y la lista de tareas.

## 1. Fuente ES en alcance (medido)

| Fichero | Hojas · rango | Fórmulas | Textos (palabras) | DV · CF | Notas de estructura |
|---|---|---|---|---|---|
| `plan-financiero-…xlsx` | Resumen A1:J21 · P&L Año 1 A1:N19 · Proyección 3 años A1:J18 · Break-even A1:J10 · Mix B2C-B2B A1:J14 · KPIs A1:J14 | **134** (18/84/27/5/0/0) | 191 (622) | 0 · 0 | sin protección, sin celdas de entrada marcadas, **51 fórmulas con la tasa tecleada dentro** |
| `calculadora-pricing-…xlsx` | Calculadora pricing A1:J35 · 10 ejemplos validados A1:J14 | **16** (16/0) | 108 (382) | 0 · 0 | 10 entradas en amarillo `FFF7C2` (B5:B14), 24 merges, 11 fórmulas con constantes, 6 con literales ES |
| `checklist-apertura-…xlsx` | **1 hoja** «Checklist 6 fases» A1:J123 | 0 | 446 (1.527) | 0 · 0 | cabecera fila 4 `Fase · # · Hito · Detalle / Acción · Plazo · OK` (sin «Responsable»); **108 tareas** |
| `plan-de-negocio-…docx` | 120 párrafos (119 con texto) · US Letter | — | 1.969 + 707 en tablas | — | estilos Normal 49 · List Bullet 65 · List Number 6 · **0 Heading** · 9 secciones · 19 subsecciones · **7 tablas** |

**Contenido que vale la pena llevar (resumen):**
- **Concepto** (docx [6]-[7], [11]-[19], [21]-[28]): catering de eventos sin restaurante, estaciones temáticas en directo (show cooking), dietas especiales al mismo nivel, marca corporativa del menú, degustación previa. El «multi-concepto de 12 cocinas del mundo» queda como **diferencial** (estaciones temáticas), no como inventario de 12 equipos.
- **Mezcla particulares/empresas** (docx [30], tablas 1-2; `Mix B2C-B2B!A5:F14`): 35 % social (bodas, cumpleaños, aniversarios, comuniones, baby showers) / 65 % corporativo (eventos de marca, wedding planners, hoteles, embajadas, festivales); 10 tipologías con ticket, eventos/año y estacionalidad. Sirve para el texto y para la calculadora.
- **Política comercial** (docx [62]-[66]): anticipo 40 % para bloquear fecha, cancelación >21 d / 21-7 d (50 %) / <7 d (100 %), recargos por distancia, maridaje y ambientación, descuentos por acuerdo marco 5-12 %.
- **Operativa de un evento en 6 fases** (docx [69]-[75]) y **checklist F6** (filas 104-123): briefing D-21, visita técnica D-14, compras D-7/D-1, mise en place D-1, montaje 60-90 min, servicio, recogida, cobro y factura 24-48 h, reseña, CRM.
- **Riesgos** (tabla 5, 9 filas): cancelación, intoxicación, avería, impago B2B, falta de personal, alergias, lluvia, imitadores low-cost, coordinación multiestación → §8 del docx EN.
- **Estacionalidad** (`P&L Año 1!B7:M7`, ene→dic): 3,0 · 3,7 · 5,9 · 7,0 · 10,7 · 13,0 · 10,4 · 5,9 · 10,0 · 10,4 · 7,4 · 12,6 % (bodas may-oct + empresa en diciembre). Solo como **forma**; los pesos US los fija research.
- **Supuestos del caso ES** (no se trasladan): 173 eventos (76 + 97), ticket/evento 2.200 / 4.500 €, food cost 28 %, logística 5 %, personal freelance 15 % (variables), fijos 10.560 €/año, inversión 8.520 / 21.410 / 54.440 €.
- **KPIs** (`KPIs!A5:D14`): eventos/mes, ticket, food cost, margen, cancelación, NPS, repetición B2B, CAC, LTV, nº de conceptos. Solo los nombres (los «Sector top 25 %» no tienen fuente) → candidatos a la tabla D19 con fuente US.

## 2. Defectos del ES que NO pasan al EN

| # | Dónde | Defecto (medido) |
|---|---|---|
| L1 | `Break-even!B5:B10` | Break-even **sin amortización, sin sueldo del dueño ni alquiler de cocina**: fijos 10.560 €/año → **5,5 eventos/año (0,46/mes)**. La ficha dice «break-even 14 eventos/mes» (3 veces): confunde con `KPIs!B5` (objetivo 14 eventos/mes) |
| L2 | `Break-even!B6` `=2200*0.35+4500*0.65`, `B7` `=1-0.28-0.05-0.15`, `B10` `/12`; `P&L Año 1!B9:N11` (39) `=B7*0.28/0.05/0.15`; `Proyección!B12:D14` (9) | **Tasas dentro de las fórmulas** (51 celdas): cambiar el food cost obliga a reescribir fórmulas |
| L3 | `Proyección 3 años!B18:D18` | Margen neto **50,3 / 53,6 / 55,7 %**; la tabla 4 del docx dice 27 / 30 / 32 % y `KPIs!B8` «27 %» |
| L4 | `P&L Año 1!B5:M6` | Ingresos mensuales **tecleados**, no ligados a eventos × ticket (cuadran con `Proyección!B9:B10` por coincidencia); `Proyección!B15:D15` fijos tecleados |
| L5 | `Mix B2C-B2B!C5:D14` vs `Proyección!B7:B8` | Ticket ponderado del Mix **2.736,8 / 5.115,5 €** frente a 2.200 / 4.500 € usados en ingresos y PE |
| L6 | Resumen vs docx [8], [13] y ficha | Inversión xlsx **8.520 / 21.410 / 54.440 €**; docx [8] «11.500-16.000 € recomendada, mínimo 5.500, premium 35.000»; tabla 3 TOTAL mínimo «8.540 €» (suma real 8.520); en la ficha «5.500» aparece 4 veces y «11.500» 2 |
| L7 | docx tabla 4 | Año 2 «846.730 €» frente a 846.720 €; «margen bruto 62 %» sin cálculo en el xlsx |
| L8 | Todo el plan financiero | Sin IVA/impuestos, sin impuesto de sociedades, sin cash flow, sin financiación ni DSCR, inversión no conectada a nada (ni amortización ni payback). docx [60] cita «amortización 3.500-4.800 €/año» que el xlsx no calcula |
| L9 | docx [14], [13] | «**Sin licencia de actividad clasificada** — autorizaciones puntuales por evento» y «sin local fijo», mientras [72] y checklist fila 112 exigen «cocina central o compartida»: el coste de esa cocina no está en el modelo. En US es requisito: **cocina con permiso (commissary)** |
| L10 | Calculadora `B34` `=B31*0.55`, `B35` 0,55 | **Margen tecleado (55 %)**, no calculado desde costes; precio base por tramos tecleados en `B17` (65/55/48 y 58/48/42 €/pax), factores en `B18:B21`, 0,95 €/km `B24`, 135 €/freelance `B25`, 14 €/pax `B22`, 280 € `B23` |
| L11 | Calculadora `B5:B14` | Entradas de texto **sin validación**: `B17`, `B18`, `B20:B23` comparan con «B2B», «exclusivo», «premium», «japonés», «sí»: escribir «si» o «Japones» anula el recargo en silencio |
| L12 | Hoja «10 ejemplos validados» | 10 casos **tecleados** (0 fórmulas) con «validados… España 2026» sin respaldo; ficha «10 ejemplos validados» |
| L13 | Checklist `A2` y ficha | «110 hitos»: son **108** |
| L14 | docx: 0 Heading, 9 secciones | Sin estilos de encabezado (no navegable); portada [1] «España 2026», [3] y [119] «ChefBusiness Consultoría»; [89] «96 proveedores reales validados»; cifras sin fuente verificable en [35], [39], [46] (38 % bodas multiculturales, 58 %, 73 % millennials) |
| L15 | Ficha | «Plan de Negocio DOCX (60+ pp.)» (×4): el docx tiene 2.676 palabras; «€165» tachado / «73 % de descuento» (prohibido en EN, D49) |
| L16 | «Plantillas validadas con asesor legal» | **No aparece** en los 4 ficheros en alcance ni en la ficha (`git grep` sin resultados): está en contratos (fuera del EN). Nada que hacer |

## 3. Base estructural EN (medido sobre los 5 libros publicados)

| | **FT** | CAF | BAR | REST | PAN |
|---|---|---|---|---|---|
| Fórmulas plan | **722** | 742 | 742 | 772 (pestañas numeradas) | 737 |
| `B24` | **«Monthly commissary & truck parking» 1.200** | Monthly rent 4.500 | 6.500 | 7.000 | 4.200 |
| Actividad B4×B5×B6 | 80 × $14 × **260 días** | 145 × 11 × 340 | 95 × 27 × 360 | 125 × 28 × 310 | 210 × 10 × 310 |
| Startup tecleadas | **14** (filas 7-20: vehículo, adaptación, equipo, generador, propano, agua, permisos, plan review…) | 23 | 18 | 31 | 19 |
| Staffing | 4 puestos (B5:B8), **`C9` = SUM** (sin E4) | 6 | 7, SUMPRODUCT | 7, SUMPRODUCT | 6, SUMPRODUCT |
| Fijos P&L · estacionalidad | 16 · fila 5 de Cash Flow, 12 verdes | 15 · sí | 15 · sí | 17 · sí | 16 · sí |
| Checklist | **68** (11/13/12/10/12/10), F2 «Truck & Permits» | 75 | 73 | 1 hoja | 66 |
| Docx (párrafos · palabras EN) | **131** · 6.602 (H1 37·44·51·59·67·76·83·91·100·109) | 167 · 7.333 | 133 · 7.780 | 148 · 7.784 | 131 · 7.448 |

**Recomendación: FT.** Lo que un catering comparte con el food truck (cocina comisaria en vez de local, furgoneta,
permisos por evento, actividad por días/eventos, personal de eventos) son celdas que ya existen; con CAF/BAR/REST/PAN
habría que vaciar el bloque de local (obra, licencia de apertura, aforo) y seguiría sobrando la lógica de cubiertos/día.

**Motor (uso medido de los drivers en FT EN):** `B4` → `P&L!B6` (1); `B5` → `P&L!B7` (1); `B6` → `P&L!B8` y
**`Staffing!B20`** (2); vía P&L: fila 6 en 12 fórmulas, fila 7 en 9, fila 8 en 12 (P&L B9:D9, C6:D8; Break-Even B8:D9,
B11:D11, B23:D23; Scenarios C5:C7). Con la permuta B4 = eventos/año, B5 = $/invitado, B6 = invitados/evento:
- Ingresos `P&L!B9 = B6·B7·B8` = eventos × $/invitado × invitados ✓; el crecimiento años 2-3 (`C6`, `D6`) cae sobre **eventos/año** ✓ (es como crece un catering); invitados/evento constante ✓.
- Break-Even: `B9` coste variable «por cliente» = por invitado; `B14` «clientes/año» = **invitados/año**; **`B15 = B14/B11` = eventos/año necesarios** ✓ (unidad recomendada: eventos al año con el tamaño medio de evento); `B19:B20` igual en caja; `B23` = eventos del plan; `B24` holgura ✓. Tabla de sensibilidad `B32:E36` = eventos/año por precio × coste ✓.
- Scenarios `B5/D5` eventos (verdes), `B6/D6` $/invitado, `B7/D7` invitados/evento; `B21` = eventos para equilibrio ✓; `B24` = invitados/año por FTE ✓.
- **Cambia (obligatorio, 2):** `Staffing!B20` `B18*B19*'0. Assumptions'!$B$6` → `…!$B$4` (horas por evento × personas por evento × **eventos**); `Staffing!C9` `SUM(C5:C8)` → `SUMPRODUCT(B5:B8,C5:C8)` (parche E4 de BP2: el puesto de personal de eventos tendrá >1 persona). **Opcional (3):** `Break-Even!B31,D31,E31` escalones ±2/+4 $ pensados para un ticket de $14 → ±10/+20 $ para $/invitado.
- **Decisión para la SPEC — personal de eventos.** En FT el personal es FIJO (`P&L!B23 = Staffing!G9`). Opción A (0 fórmulas más): fijo + cobertura por evento (horas × personas × eventos), nota de que en el escenario pesimista el coste real baja. Opción B (+6 fórmulas `P&L!B54:D54`, `Scenarios!B23:D23` para el ratio de personal): `B15` «Disposables» → «On-call event staff (hourly W-2 + payroll taxes) % of sales» y desechables dentro de food cost/misc. **Recomiendo A** (motor intacto; la calculadora ya presupuesta el personal por evento).
- Validaciones heredadas: `B6` entero 1-365 (vale para invitados medios/evento), `B4` 1-100.000, **`B58` 1-365 días de cobro: no admite anticipos** (riesgo R3).

**Rótulos de inversión (FT filas 7-20, sin tocar bases):** 7 Refrigerated cargo van (used) · 8 Van upfit (racks, shelving,
wrap) · 9 Kitchen and refrigeration equipment (own) · 10 Portable cooking and power (induction, burners, generator) · 11 Van
refrigeration unit + install · 12 Commissary storage fit-out · 13 LLC formation and legal · 14 First-year permits and
licenses · 15 Health plan review (only if you lease your own kitchen) · 16 Catering software + card reader · 17 Smallwares,
hotel and sheet pans · 18 Opening inventory · 19 Website, photography, launch marketing · 20 Chafing dishes, insulated
carriers, serving ware. Bases de amortización (`B31` = 7+8+11+12+15+23; `B32` = 9+10+16+17+20) siguen siendo coherentes.
**Fijos** (`P&L!A22:A35`): solo rótulos; A22 «Commissary kitchen rent & van parking», A27 «Van fuel, maintenance and
inspections», A35 Music licensing → sin sentido en catering, propuesta «Tastings for prospects». **Variables**: `B16/B17`
delivery platform → marketplaces de catering corporativo (cuota × comisión), cifras de research.

**Volumen de texto (FT ES como fuente del circuito):** cadenas propias del FT en el plan = **226 (≈ 4.270 pal. ES)**:
Supuestos 36/1.742 · Instrucciones 128/1.420 · Inversión 29/332 · P&L 23/584 · Personal 9/191 · PE 1/4 → se ESCRIBEN
nuevas para catering. Cadenas del motor (GM) que hablan de clientes/día, ticket o días → **32 (492 pal.)** a sobrescribir
por celda; en el FT EN, **91 celdas** de texto nombran la actividad (Supuestos 26, Instrucciones 22, P&L 14, PE 13,
Escenarios 7, Inversión 5, Personal 4). Fórmulas con texto a reescribir: `Break-Even!A26` (_PE) y
las listas de partidas de `Startup Costs!D23` y `D33` (argumentos de `_inversion`); de las 16 de FT, las 13 restantes
(`0. Assumptions!C9`, `P&L!F13/F14/F18`, `Staffing!A2`, `Cash Flow!O11`, `Startup Costs!D21/D22/D25/D26/D28/D31/D32`) valen.

## 4. Calculadora de precios por invitado

**Recomiendo REGENERARLA en EN con openpyxl** (`calculadora_cat.py`), no pasarla por `extraer_textos`/`aplicar_en`: el
circuito copiaría L10-L12 (margen tecleado, tramos y tasas en fórmulas, entradas de texto sin DV, ejemplos sin respaldo) y
sus literales ES viven dentro de 6 fórmulas. Es pequeña (16 fórmulas, 108 textos): regenerar cuesta lo mismo y sale limpia.

ES hoy: entradas `B5` canal · `B6` invitados · `B7` km · `B8` nº conceptos · `B9` cocina · `B10` nivel · `B11` maridaje ·
`B12` ambientación · `B13` show cooking · `B14` freelance → `B17` €/pax por tramo y canal × `B18` nivel × `B19` multiconcepto
× `B20` cocina premium × `B21` show cooking + `B22` maridaje → `B28` €/pax, `B29` comida, `B30` logística + personal +
ambientación (`B24` km×0,95×2, `B25` n×135), `B31` PVP sin IVA, `B32` €/pax, `B33` anticipo 40 %, `B34`/`B35` margen 55 %.

EN propuesta (coste → precio, todo verde con DV de lista): invitados · estilo de servicio (drop-off / buffet /
family-style / plated / stations) · coste de comida por invitado (escandallo) o food cost objetivo · paquete de bebida ·
personal de evento (personas × horas × $/h + payroll taxes) · alquileres repercutidos · millas × $/milla · **service
charge %** · **sales tax** (y si grava el service charge) · propina voluntaria (fuera del precio) · anticipo % · **mínimo
de invitados / mínimo de consumo** → $/invitado, subtotal, service charge, impuesto, total, anticipo y **margen bruto
calculado**. Lo que tiene que fijar research (no inventar): tratamiento fiscal del service charge por estado, distinción
service charge vs gratuity (IRS), tarifa por milla de referencia, rangos de anticipo y mínimos, ratios de personal por
invitado. Fuera la hoja «10 ejemplos validados» (L12); como mucho 3 presupuestos de ejemplo que salgan de la propia fórmula.

## 5. Checklist: 108 tareas ES (1 hoja) → molde EN de 6 hojas

| Fase ES (filas) | Tareas | Solo España (sin sentido en US) | Adaptar a US | Multicocina | → Fase EN |
|---|---|---|---|---|---|
| 1 Constitución legal (6-22) | 17 | **7** — 7 IAE 677.9 · 12 RGSEAA · 13 RGPD/LOPD · 14 LSSI · 19 mod. 390 · 20 mod. 347 · 21 mod. 349 | 8 (alta autónomo → LLC+EIN, APPCC → food safety plan, manipulador → food manager/handler, registro sanitario → health permit, desistimiento → cancelación en contrato, mod. 130 → estimated taxes, IVA 10 % → sales tax permit, SL → LLC vs S corp) | 0 | P1 (7) · P2 (2) · P4 (1) |
| 2 Seguros y autorizaciones (25-34) | 10 | 0 | 10 (RC ≥ 600.000 € → GL, intoxicación → product liability, furgoneta → commercial auto, freelance → **workers' comp + W-2 vs 1099**, equipo, cancelación, permisos por evento, venta ambulante → temporary food permit, fuego → fire marshal, cocina del cliente) | 0 | P1 (6) · P2 (4) |
| 3 Equipamiento + proveedores (37-64) | 28 | **1** — 64 Hosply.pro | 6 (58-62 proveedores con marcas españolas, 63 furgoneta Renault/Iveco) | **12** (37-48: cuchillería japonesa, wok, teppanyaki, horno de leña, tandoor, smoker, trompo, comales, vaporeras…) | P3 (26 → condensar a 12) · P2 (furgoneta) |
| 4 Marca, web y SEO (67-83) | 17 | **1** — 83 Hosply.pro | 4 (foto en €, WhatsApp → texto/SMS, Bodas.net/Zankyou → The Knot/WeddingWire, CateringClick → marketplaces US) | 0 | P5 |
| 5 Captación B2C + B2B (86-101) | 16 | 0 | 1 (Google Ads en €) | 0 | P5 (32 con la fase 4 → condensar a 12) |
| 6 Operativa primer evento (104-123) | 20 | 0 | 1 (110 importadores españoles) | 0 | P6 (20 → condensar a 10; el detalle va al docx §5) |
| **Total** | **108** | **9** | **30** | **12** | 57 directas |

Reparto propuesto de las 99 válidas: **P1 13 · P2 7 · P3 26 · P4 1 · P5 32 · P6 20**. Recomendación: **quedarse en 68
tareas con los recuentos del FT (11/13/12/10/12/10)** y pasar el checklist por el circuito de texto sobre el FT ES (mismas
filas, contadores, DV `✓,☐,N/A` y CF): cero cambios de estructura. P2 sube de 7 a 13 con trámites US (commissary
agreement, catering/health permit, temporary event permits, fire marshal, registro y seguro de la furgoneta, permiso de
alcohol del caterer si se sirve); **P4 Staff no tiene tareas en el ES** (solo la fila 10): se escribe de cero reutilizando
el EN del FT/REST (I-9, W-4, new-hire reporting, workers' comp, food handler cards, OSHA, alcohol server). Columnas EN:
`OK | TASK / ACTION | RESPONSIBLE | TIMING | NOTES` (ES: Hito → Task, Detalle → Notes, Plazo → Timing; **Responsible
nuevo** en todas). Pestaña F2: «Phase 2 - Kitchen, Van & Permits». Título: «CATERING STARTUP CHECKLIST».

## 6. Riesgos para F2 y presupuesto

1. **R1 · Semántica del motor permutado.** Cualquier rótulo o nota que siga diciendo «per day», «operating days», «customers», «truck», «window» deja el break-even ilegible. Gate: barrido de vocabulario FT en el libro EN (0 apariciones) + autotest `Break-Even!B15` = eventos/año con el caso US.
2. **R2 · Personal de eventos fijo vs variable** (decisión A/B de §3) y su cobertura por evento: si no se decide en la SPEC, las notas de Supuestos, Staffing, Escenarios e Instrucciones se escriben dos veces.
3. **R3 · Caja de un catering**: anticipos (no modelables: `B58` ≥ 1 día), empresas a 30 días y estacionalidad por «Month 1» relativo (no por mes natural): la nota de `Cash Flow!A5` debe decir que se alinea el mes 1 con la apertura.
4. **R4 · Legal US con fuente** (research): cocina comisaria obligatoria (contra L9), permiso de alcohol del caterer por estado, impuesto sobre el service charge, workers' comp y **clasificación W-2 vs 1099** del personal de eventos (el «freelance 15 %» del ES es un riesgo de mala clasificación en US).
5. **R5 · Cero arrastre del caso ES** (L1-L8): el caso US sale entero de research + calibración D15; gate de cifras prohibidas: 603.700 · 303.364 · 8.520 · 21.410 · 54.440 · 10.560 · 2.200 · 4.500 · 846.720 · «14 eventos/mes» · «5.500» · «11.500» · «55 %». Y alcance: el EN es catering de eventos con estaciones temáticas, **no** 12 cocinas.
6. (Menores) La calculadora es código nuevo sin gate ES→EN: necesita su autotest (recalcular precio y margen); el docx se escribe en las ranuras fijas del FT ES (131 párrafos, §10 con el cierre fijo): los redactores no eligen el nº de párrafos.

**Estimación F2 (≤ 1,8 M):** implementador opus en VPS (`mapas_cat.py`, `datos_cat.py`, `bp4.py`, conjunto `cat`, 2
parches, `calculadora_cat.py`) ≈ **0,6 M** · tanda 1 Sonnet ‖ Sonnet: GCAT-plan (≈ 258 cadenas, ≈ 4,8 K pal.) ‖ GCAT-check
(68 tareas × 4 columnas + títulos, ≈ 3 K pal.) ≈ **0,35 M** · `aplicar_en` + calibración + tanda 2 docx `cat_a` ‖ `cat_b`
(≈ 6,6 K pal. escritas, no traducidas) ≈ **0,35 M** · gates G1-G9 + vocabulario + cifras + una revisión opus ≈ **0,3 M**.
**Total ≈ 1,6 M**; colchón 0,2 M para una iteración de la calculadora. Lo que lo dispararía: rediseñar el motor (opción B
ampliada) o escribir el checklist con más de 68 tareas (generador nuevo).
