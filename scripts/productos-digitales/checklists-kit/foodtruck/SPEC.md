# Food Truck Checklists Kit Pro — SPEC DELTA (F1 · 31-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas Recurrentes: Food Truck** (`kit-tareas-food-truck`, 11 xlsx **v1.1**,
> origen ChefBusiness, 12 €). Duodécimo hermano vertical: **lo que no está aquí es la SPEC base** (`../SPEC.md` §0-§9).
> Mapas: `mapas_foodtruck.py` (importa `../mapas.py`). Tamaño S. 11 hojas. Producto hermano LIVE: **Food Truck Business
> Plan Kit** (jerga y trámites de `../../business-plans-en/F1-research-us.md` §5 y `SPEC.md` §2.3 y §4.2).

## 0. El molde PLANO (medido en el censo) — el primero del circuito

El mapa de libros es el de la taquería (01-04 propios, 05 manager, 06 perfiles, 07 semanal/mensual, 08 eventos, 09 en
blanco, B01, B02, sin caja), pero el **molde es otro**: el PLANO de los kits ChefBusiness (`../../kit-tareas-cb-v2-SPEC.md`
§0.1; también lo son **panadería, marisquería y tapas-bar**). Por libro: **UNA hoja**, A1 = marca «ChefBusiness Consultoria
Gastronomica», A2 = título, **cabecera en la fila 3**, bandas de sección fusionadas A:F, **sin columna Nº, sin hoja
«Instrucciones», sin contadores (0 fórmulas), sin protección, sin línea de versión ni bio**, última fila = línea de marca;
DV `"✓,—,N/A"` en la columna E (7 hojas, 126 celdas) y CF `$E4="✓"` (7); 05 y 09 sin DV ni CF; títulos de impresión
`$3:$3` en las 11; A4 (01-09 apaisado, bonus vertical). Tildes quitadas en todo el ES («electrica», «deposito»).

| Libro ES (hoja) | Columnas | Tratamiento |
|---|---|---|
| 01 Setup y Teardown | Fase · Tarea · Responsable · Tiempo · OK · Observaciones | 23 tareas en 4 bandas; D = duración («10 min», glosario) |
| 02 Operaciones Moviles · 03 APPCC Movil | Categoría / Registro · Tarea · **C/D cruzadas** (errata §5) · OK · Notas | 18 + 18; cabeceras corregidas por `POR_CELDA` |
| 04 Permisos y Eventos | Tipo · Tarea · Anticipación · Responsable · OK · Notas | 18 (12 trámites/pre-evento + 6 tipos de evento) |
| 05 Tareas Manager | Categoría · Tarea · Frecuencia · Prioridad · Estado · Notas | 15, sin DV |
| 06 Perfiles · 07 Semanales y Mensuales · 08 Eventos y Temporadas | como el 01 | 20 · 16 · 13 |
| 09 Personalizable · B01 Briefing Pre-Evento | — | en blanco (A26 instrucción) · 15 campos A/C |
| B02 Calendario Anual | Mes · Tipo Eventos · Menú · Mantenimiento · Marketing | 12 filas (4-15), sin filas libres |

**Tareas: 141** (01-08) + 12 meses del B02 = las 153 de la SPEC CB. `extraer_textos`, `heredar` y `mapas_foodtruck`
(autotest + `cruzar_censo`: **0 errores**) sirven tal cual. **Código común tocado en F1: ninguno** (solo `kit.py`).

### 0.1 Ganchos de F2 (molde plano; HECHOS en `f35b7355`, regresión 15/15 idéntica: `F2-NOTAS.md`)

Sin ellos `aplicar_en.py` aborta (escribe `Instrucciones!B2`) y `gates_en.py` da rojos falsos. Todos condicionados a
`MOLDE == 'plano'` → regresión byte a byte de `gates_en.py --kit <v>` sobre los 12 publicados (base + 11), como la taquería.
**Sirven también para panadería y marisquería** (mismo molde): hacerlos una vez.

1. `aplicar_en`: `capa_titulo` / `comprobar_titulo` / `regenerado_esperado` → el título interior es el `POR_CELDA` de
   `(corto, hoja, CELDA_TITULO)` (ya lo escribe `capa_por_celda`); nada en `Instrucciones`.
2. `gates_en` G3: sin hoja de instrucciones ni línea de versión (0 = ES); comprobar `CELDA_TITULO` = `titulo_interior`.
3. `gates_en.tareas()` (G1 y autotest `_quitar_tarea`): en plano, tarea = fila > `FILA_CABECERA` con texto en A y en B,
   que no es banda fusionada ni línea de marca (141 + 12; hoy daría 0 = 0, sin comprobar nada).
4. Autotest: las mutaciones sobre `Instrucciones!B6` (ES, moneda, «$», término prohibido, °F, cita) → una celda de la hoja
   única (`CELDA_AUTOTEST`, p. ej. 01 B5); `_hora_24` / `_hora_mal` (0 horas), `_contador_mal` (0 fórmulas),
   `_bloquear_verde` (0 verdes) y `_area_rota` (0 áreas) → saltar o cambiar por una equivalente (título de impresión
   `$3:$3`); `H_KO` / `H_DIARIO` / `F_VERDE` por `getattr`.
5. G6 (0 fórmulas) y G4 horas (0) pasan en vacío: declararlo en el informe, no es verde de verdad.

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `food-truck-checklist-templates` → `/en/digital-products/food-truck-checklist-templates` (+ `/access`, `/library`); productId = slug; JWT `food-truck-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_FOOD_TRUCK_CHECKLISTS_KIT`; ficheros en `dl/food-truck-checklist-templates/`; familia `kit-tareas-food-truck` en `tienda.ts` |
| D2 | Nombre | **Food Truck Checklists Kit Pro**; title SEO = H1 (Forma B): «Food Truck Checklists Kit Pro: **Inspection, Setup & Teardown** Checklist Templates for Excel». DataForSEO US (31-oct): food truck inspection checklist **170**, health inspection checklist **110**, food truck checklist 50, fire inspection checklist 40, opening / daily 10, closing / setup / template sin volumen; SERP con AI Overview, checklists de condados y bomberos + plantillas (Mitti); PAA «pre-trip inspection». Por eso no «Daily, Opening & Closing». Sin «— Food Truck» |
| D3-D4 | Precio | **$15 USD** (decisión del orquestador, 31-oct: los tres kits de molde plano —food truck, panadería, marisquería— a $15, no $19: ~140 tareas en hojas planas frente a 300-500 de los hermanos v2.0), pago único; sin `priceOld`, «% off», «worth $X» ni anclas: «One-time payment · lifetime access · updates included» |
| D5 | Ficheros | §2: inspection (03), pre-trip (02), setup & teardown (01) |
| D6 | Pestañas | Setup & Teardown · Vehicle & Mobile Ops · Food Safety & Inspection · Permits & Events · Manager Tasks · Duties by Role · Weekly & Monthly · Events & Seasons · Blank Template · Pre-Event Briefing · Annual Calendar |
| D7 | DV, CF, estructura | Idénticas (7 DV, 7 CF, 63 merges, 11 paneles A4, 11 títulos de impresión, anchos); `CLAVES` = {N/A}. **No se añade nada** (ni hoja de instrucciones, ni contador, ni DV en 05/09): duplicar, no reconstruir; la errata de cabeceras se corrige en las mismas celdas |
| D8 | Glosario | base + **114** (4 sobrescriben: Cierre → **Teardown**, Encargado → **Manager** (owner-operator), Caja → **Cash**, Pre-servicio → **Before service**): 32 cabeceras de las 11 hojas, fases y categorías, crew (Equipo), **Driver / tech** (Técnico: en un truck es el conductor), Prep cook, **Pre-trip** (Pre-salida), frecuencias, prioridades High / Medium, duraciones. «Servicio» como puesto (01 C18-C20, 06 A17-A21) → **Window staff** por `POR_CELDA`; como fase o momento, «Service» |
| D9 | Horas | 0 horas de 24 h en el ES |
| D10 | Seguridad alimentaria | °F + FDA Food Code 2022 (§3): cocción 165 / 155 / 145 °F (03 B8, `POR_CELDA`; el ES dice «≥ 74 °C aves, ≥ 63 °C otros»), frío 41 °F, caliente 135 °F o TPHC 4 h (sin las «2 h» del ES), descongelación 3-501.13, mano desnuda 3-301.11, gel solo tras lavarse 2-301.16, nada de cocina de casa 3-201.11, CFPM + food handler cards, 9 alérgenos + aviso escrito 3-602.12(C) |
| D11 | Truck | Agua: fresh / wastewater tank, residual ≥ 15 % mayor (5-401.11), vaciado solo en el commissary / servicing area (5-402.14), agua de fuente aprobada (5-101.11). Propano (sin butano), NFPA 58, prueba de fugas tras cada cambio de bombona (NFPA 1 / 58); 10 ft libres (NFPA 1 / 96, según edición); extintor ABC + clase K (NFPA 10), mensual / anual OSHA, extinción de campana cada 6 meses (NFPA 96); generador fuera, lejos de ventanilla y tomas (CO), según organizador y fire marshal; vehículo: DMV + commercial auto, sin ITV, CDL solo ≥ 26,001 lb GVWR |
| D12 | Sin caja | `HOJA_CAJA = None` (como la taquería; el gancho de `gates_en` ya existe). La caja del día: 01 B19 / B28, 05 B15, 06 B18 (POS, card reader, starting bank, cash count, over/short, tip pool) |
| D13 | Moneda | 1 texto con EUR (04 B7, RC 300.000 €) → `POR_CELDA` con «$1M per occurrence» (research §4.2; `zona_dolar` lo admite); 0 formatos € |
| D14 | Calendarios | **B02** (otro molde: A y B fijados, `CALENDARIO`; C, D, E traductor con 5 ADAPTAR): Super Bowl, Valentine's, Mardi Gras, St. Patrick's, Easter, Cinco de Mayo, Memorial Day, graduaciones, Father's Day, 4 de julio, county / state fairs, Labor Day, Halloween, Thanksgiving, holiday markets, NYE. **08**: MadrEat, Van Van Market y San Isidro / Fallas / Feria de Abril (A13-B15) → food truck festivals & rallies, farmers & night markets, county & state fairs (`POR_CELDA`); temporadas por ADAPTAR (verano = Memorial Day–Labor Day, sin chiringuitos) |
| D15 | Marca | A1 «ChefBusiness Consultoria Gastronomica» → **«AI Chef Pro»** (glosario) y la línea de marca → «AI Chef Pro · aichef.pro · Food Truck Checklists Kit Pro» (sin «—»: G2 lee «— Food Truck» como el sufijo ES), mismas celdas: precedente D34 del Restaurant Business Plan Kit. La decisión del 22-ago (CB deliberada) es sobre los ES que se venden tal cual; la EN es un juego nuevo con la marca de la tienda EN, como sus 12 hermanos |
| D16 | Versión, papel | v1.1 (changelog ES): docProps `subject` «Food Truck Checklists Kit Pro · v1.1»; sin línea de versión (el ES no la trae). A4 → **US Letter** en las 11, misma orientación y ajuste |
| D-PERM | Permisos | 04 B6 RGSEAA → mobile food unit health permit (plan review + inspección) + commissary agreement; B9 IAE → business license + seller's permit + EIN; venta ambulante → mobile vending license por ciudad, una por truck; temporary food event permit; COI + additional insured; POS con sales tax por lugar de venta; apps Roaming Hunger / StreetFoodFinder; food cost «about 28–35% (kit benchmark)» en vez del «< 25 %» del ES |
| D-LEX | Lecciones de los hermanos | Tiras de sanitizante (4-501.114) en 3 limpiezas · date marking · `AJUSTE_MAQUETA_ES = True` · `TERMINOS_PROHIBIDOS` (restaurant salvo consultant, host stand, head / sous chef, busser, barback, bartender, barista, banquet, BEO, line-up, server, dining room, **plancha**, **butane**, MOD, FOH, **ITV**) |
| D-UK | UK | Solo en la FAQ de la landing (F3; research §5): registro en el council 28 días antes, street trading licence, FHRS 0-5, 14 alérgenos, 8 °C / 63 °C |
| D-F3 | Landing | «141 food truck tasks + 12-month calendar»; **no prometer** hoja de caja, «cash count sheet» ni vitrina (la ES los cita y no están, §5); Google Sheets solo si el test de F3 lo confirma |

## 2. Ficheros (D5) — títulos en `mapas_foodtruck.TITULOS` (A2 = «NN · título»; los bonus, «BONUS: …»)

| # | Fichero ES | Fichero EN |
|---|---|---|
| 01 | `01-setup-teardown-food-truck.xlsx` | `01-food-truck-setup-teardown-checklist.xlsx` |
| 02 | `02-operaciones-moviles-vehiculo.xlsx` | `02-food-truck-pre-trip-vehicle-checklist.xlsx` |
| 03 | `03-appcc-seguridad-alimentaria-movil.xlsx` | `03-food-truck-health-inspection-food-safety-checklist.xlsx` |
| 04 | `04-permisos-eventos-localizaciones.xlsx` | `04-food-truck-permits-events-locations-checklist.xlsx` |
| 05 | `05-tareas-manager.xlsx` | `05-food-truck-manager-checklist.xlsx` |
| 06 | `06-tareas-perfiles.xlsx` | `06-food-truck-duties-by-role.xlsx` |
| 07 | `07-semanales-mensuales.xlsx` | `07-food-truck-weekly-monthly-cleaning-maintenance-checklist.xlsx` |
| 08 | `08-eventos-estacionales.xlsx` | `08-food-truck-events-seasons-checklist.xlsx` |
| 09 | `09-plantilla-personalizable.xlsx` | `09-blank-food-truck-checklist-template.xlsx` |
| B01 | `BONUS-01-briefing-pre-evento.xlsx` | `BONUS-01-food-truck-pre-event-briefing-template.xlsx` |
| B02 | `BONUS-02-calendario-anual.xlsx` | `BONUS-02-food-truck-annual-calendar.xlsx` |

## 3. Reglas del delta (`mapas_foodtruck.REGLAS_US` = las del base + estas; 57 en total)

| Concepto | Fuente |
|---|---|
| Cocción 165 / 155 °F 17 s / 145 °F 15 s · descongelación · TPHC 4 h · mano desnuda · gel · cocina de casa | FDA Food Code 2022 §3-401.11(A); §3-501.13; §3-501.19(B); §3-301.11; §2-301.16; §3-201.11(B) |
| CFPM + food handler cards · 9 alérgenos + aviso escrito · «gluten-free» | §2-102.12 + [estatal]; FALCPA + FASTER Act, §3-602.12(C); 21 CFR 101.91 |
| Agua de fuente aprobada · residual ≥ 15 % · vaciado en servicing area | §5-101.11; §5-401.11(A) (MN 4626.1180, WA 246-215-05400); §5-402.14 y «servicing area» §1-201.10 |
| Commissary agreement · mobile vending license · mobile food unit permit · temporary event permit | [local] research US §5 (cabq.gov, chicago.gov) |
| Business license + seller's permit + EIN · POS con sales tax · GL $1M + COI · apps | research US §5 (sba.gov, irs.gov); Food Truck Business Plan Kit SPEC §4.2 |
| DMV + CDL ≥ 26,001 lb | 49 CFR 383.5 y 383.91 (research US §5) |
| Propano NFPA 58 · fugas tras cada cambio · 10 ft libres · clase K · extinción 6 meses | NFPA 58; NFPA 1 §50.7-50.8 / NFPA 96 cap. 17 según edición (fichas de bomberos que las citan: Yonkers NY, Estero FL, North Davis UT «NFPA Food Truck Safety Fact Sheet», TAMU EHS 2024); NFPA 10; NFPA 96 (base) |
| Generador fuera y lejos (CO), repostar apagado · propinas sin managers · food cost 28-35 % · calendario US | [criterio del kit] + manual del fabricante; 29 U.S.C. 203(m)(2)(B); research US §4 [criterio del kit]; 5 U.S.C. 6103 (base) |

°F que el kit puede afirmar (G7, `GRADOS_F_SPEC`; el autotest exige la igualdad con POR_CELDA + ADAPTAR + REGLAS_US):
−31, −4, 0, 41, 70, 100, 135, 145, 155, 165. Las 3 celdas ES con °C (03 B5, B8, B9) llevan ADAPTAR o POR_CELDA;
`CELSIUS_SIN_F` vacío. `CITA_AUTOTEST` = 3-501.18.

## 4. Memoria de traducción (`../heredar.py --kit foodtruck`; `MEMORIA`: base, catering, taquería, hamburguesería, ghost)

**441 cadenas** (862 apariciones); **GM 204** (560 palabras: 11 pestañas, 130 de glosario, 63 regeneradas: 58 celdas
`POR_CELDA` —11 títulos A2, cabeceras, Window staff, cocción, permisos, 08 y B02—, 11 líneas de marca, pies y docProps). De
las **237 a traducir: 0 heredadas** (otra fuente y otro molde: ninguna cadena ES coincide) y **237 pendientes** (todas
«nueva»; **1.233 palabras**; 75 con ADAPTAR): **G1 113 cadenas / 666 palabras** (01-05; 49 ADAPTAR) y **G2 124 / 567**
(06-B02; 26). Sin cadenas comunes a ≥ 3 libros (lo repetido va por glosario). Propuesta F2: UN traductor sonnet, una sola
tanda (1.233 palabras) → `textos_en/G1.json` con los 237 ids; brief §7.2 base + D2, D-LEX y `PISTAS_EXTRA` (el ES va sin
tildes: «Anade» = «Añade»).

    python3 extraer_textos.py --kit foodtruck && python3 foodtruck/mapas_foodtruck.py && python3 heredar.py --kit foodtruck
    python3 aplicar_en.py --kit foodtruck --dry-run [--parcial] --idempotencia --mes <mes de la F2>   # tras los ganchos §0.1
    python3 gates_en.py --kit foodtruck [--parcial] --dir <carpeta> [--autotest]

F2, además: los ganchos de §0.1, `food-truck-checklist-templates` en `PRODUCTOS_LETTER` (`censo-entregables.py`) y
`EXCLUIDOS` (`postprocess-transversal.py`).

## 5. Erratas del ES (para su v2.0, en el calendario S15; la EN nace corregida o las deja como el ES)

- **02 y 03: cabeceras C3 / D3 cruzadas**: C3 dice «Frecuencia» y trae responsables; D3 dice «Responsable» y trae
  frecuencias (corregido en la EN por `POR_CELDA`).
- Tildes quitadas en todo el kit (93 palabras en 74 celdas y las pestañas «Operaciones Moviles» y «APPCC Movil»,
  `kit-tareas-cb-v2-SPEC.md` §1).
- 03 B8 «≥ 63 °C otros» como cocción de todo lo que no es ave (carne picada incluida) queda por debajo de los «> 65 °C» de
  mantenimiento de la B9: unificar (ya lo pedía la SPEC CB §2.1).
- La landing ES promete «arqueo» y «vitrina» en el setup / cierre y no están (SPEC CB §2.2); 05 «Estado» y 09 sin el
  desplegable ✓ / — / N/A que anuncia el changelog 1.1.
- 05 B12 «food cost < 25 % en food truck» sin fuente (el research US da 28-35 %); 06 fila 27: Momento «Semanal» =
  Frecuencia «Semanal».
