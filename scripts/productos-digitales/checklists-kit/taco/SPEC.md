# Taco Shop Checklists Kit Pro — SPEC DELTA (F1 · 31-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas Recurrentes: Taquería Mexicana** (`kit-tareas-taqueria`, 11 xlsx v2.0,
> 298 tareas). Undécimo hermano vertical: **lo que no está aquí es la SPEC base** (`../SPEC.md` §0-§9). Mapas:
> `mapas_taco.py` (importa `../mapas.py`). Tamaño S. 36 hojas. Producto hermano LIVE: **Taco Shop Business Plan Kit**
> (jerga y reglas de `../../business-plans-en-12/F1-research-us-delta.md` §6 y §9).

## 0. Cómo pasa la Taquería por el circuito (medido en el censo)

**Molde del kit base** (P4 v2.0: Nº · Tarea · Zona · Responsable · Hora Límite · ✓ Completada · Firma; CF `$F5="✓"` sin
cabeceras internas; 25 hojas protegidas sin contraseña; horas precargadas; línea de marca) con **mapa de libros propio**:

| Libro ES | Molde / tratamiento del circuito |
|---|---|
| 01 apertura-cierre · 02 trompo-plancha-comal · 03 appcc-salsas-alergenos · 04 nixtamal-tortilla-guisados | checklists P4 del base (como el 01-02 de la pizzería), pestañas y tareas propias |
| 05 tareas-manager · 06 tareas-perfiles | = 03 y 04 del base (diario + semanal; 6 perfiles) |
| 07 semanales-mensuales | = 05 del base **sin «Trimestral y Anual»** (E = Día / Cadencia): sin bloque de servicios contratados (como la pastelería, D11) |
| 08 eventos-estacionales | = 06 del base (E = Antelación); «Calendario de Eventos» con códigos MX / ES / US-es / Todos en C |
| 09 plantilla-personalizable | = 07 del base (15 filas numeradas en blanco) |
| BONUS-01 · BONUS-02 | = B01 (hoja «Briefing Pre-Servicio», B:C) y B02 del base (A mes · B fecha · C tareas · D antelación), **27 filas (5-31)** + 5 libres |
| — | **Sin 08 de negocio ni 09 de caja** (lo dice el 01 «Instrucciones» B35): sin tabla de billetes, sin G5 |

`extraer_textos`, `heredar` y `mapas_taco` (autotest + `cruzar_censo`: **0 errores**) sirven tal cual. `gate_f1.py` es solo
del base (importa `mapas` directo): no aplica. **Código común tocado en F1: ninguno** (solo `kit.py`: `taco` en `VERTICALES`).

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `taco-shop-checklist-templates` → `/en/digital-products/taco-shop-checklist-templates` (+ `/access`, `/library`); productId = slug; JWT `taco-shop-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_TACO_SHOP_CHECKLISTS_KIT`; ficheros en `dl/taco-shop-checklist-templates/`; familia `kit-tareas-taqueria` en `tienda.ts` |
| D2 | Nombre | **Taco Shop Checklists Kit Pro**; title SEO = H1 (Forma B): «Taco Shop Checklists Kit Pro: Taqueria Opening & Closing Checklist Templates for Excel». Sin «— Taquería Mexicana»; «taqueria» sin tilde; nunca «Tex-Mex» ni «authentic» (research US §9) |
| D3-D4 | Precio | **$19 USD**, pago único; sin `priceOld`, «% off», «worth $X» ni anclas: «One-time payment · lifetime access · updates included» |
| D5 | Ficheros | §2. «taco shop» 60.500 y «taqueria» 201.000 son ruido «near me»; las colas con «checklist» sin volumen, como en los hermanos: títulos con taco shop / taqueria + trompo, salsa bar, nixtamal (research US §9) |
| D6 | Pestañas | Taco Shop Opening / Closing · **Marinade & Trompo Stacking** · **Carving + Griddle + Comal** (sin coma) · Temp Logs & Receiving · Salsa Bar · **Allergens & Cross-Contact** · Nixtamal & Masa Milling · Tortillas & Comal · Guisados & Rotation · Manager Daily / Weekly · **Taquero (Trompo)** · Tortilla Maker · Salsa Prep · Griddle & Fryer · Counter & Register · Delivery Driver · Weekly / Monthly Tasks · Seasonal Ingredients · Event Calendar · Blank Template · Pre-Shift Meeting · **Annual Calendar** (el B02 mezcla fechas y mantenimiento) |
| D7 | CF y fórmulas | Idénticas: contadores `COUNTIFS`/`COUNTIF`, DV `"✓,—,N/A"`, `CLAVES` = {N/A}; sin `CF_POR_CELDA` (no hay cabeceras internas) |
| D8 | Glosario | base + 24 celdas (4 sobrescriben el base: Barra, Sala, Recepción, Al confirmar; celda entera, sin columna: zona y puesto con un solo EN). Zonas: Cámara → **Walk-in**, Barra → **Salsa bar**, Tortillería → **Tortilleria**, Mostrador → **Counter** (zona y puesto), Sala → **Dining area**, Recepción → **Receiving** (de mercancía), Almacén → Storage, Oficina → Office. Puestos: **Taquero**, Plancha → **Griddle cook** (nunca «plancha»), Tortillero/a → **Tortilla maker**, Salsero/a → **Salsa prep cook**, Repartidor → Delivery driver, Encargado → **Shift manager** (base). 08 C: MX → MX, ES y US-es → **US**, Todos → All. E: 1º de mes → 1st of month, Quincenal → Biweekly, Fin de mes → Month-end, Al confirmar → **When confirmed** (sobrescribe «At booking»), 2 semanas antes → 2 weeks out, Víspera → Day before |
| D9 | Horas | Las **246 horas de 24 h** → `hora_us` **sin desplazar** (servicio de 11:00 AM a medianoche, nixtamal desde las 5:00 AM: horario normal de una taquería US) |
| D10 | Orden y erratas | **Errata ES corregida** (§5): 01 «Taco Shop Opening» B14/B15 (el cono se comprobaba DESPUÉS de montar el trompo): comprobación a la fila 14 (11:00 AM), montaje a la 15 (11:05 AM), `POR_CELDA` |
| D11 | 05 / 07 | Fichajes FLSA (29 CFR 516.5-516.6) en 05 «Manager Weekly» B16 y 07 «Monthly Tasks» B13 (`POR_CELDA`, B16 del base). 07: gas = inspección visual del personal + profesional con licencia según el código local (B6, B9; B02 fila 8); campana: filtros por el equipo, conductos por empresa certificada (NFPA 96); calibración por punto de hielo 32 °F; plagas por licensed operator |
| D12 | Sin caja | `HOJA_CAJA = None`, `DENOMINACIONES = []`, `FORMULAS_POR_CELDA` vacío. La caja del día son tareas del 01 «Closing» y del 05 (POS, starting bank, cash count, over/short; propinas por tip pool escrito). **F2: gancho en `gates_en.py`** (G5, `F09`/`H_CC`/`F_CAJA0` de módulo y las mutaciones de caja del autotest se saltan si `HOJA_CAJA is None`) con regresión byte a byte sobre los 10 kits publicados, como el hotel |
| D13 | Moneda | 0 formatos y 0 textos con € en el ES: nada que reescribir |
| D14 | Calendarios | **B02** (27 filas, `CALENDARIO`, A/B/D fijados, C traductor con 20 ADAPTAR): las fechas mexicanas se quedan (Three Kings Day, Candelaria, Grito, Day of the Dead, Our Lady of Guadalupe, Posadas, chiles en nogada); las españolas pasan a US: + **Super Bowl** (con Candelaria, fila 7), **Lent Fridays**, Cinco de Mayo (en EE. UU. de los días más fuertes [criterio del kit]; en México, sobre todo Puebla), patio y **Memorial Day**, **Thanksgiving** (con las fiestas de empresa, fila 27); vacaciones → time off. **08 «Event Calendar»**: Semana Santa → Holy Week & Easter, terrazas → Patio season, inicio de verano → Memorial Day weekend (ADAPTAR) |
| D-TAC | Trompo | La capa que se corta: **≥ 145 °F** (cerdo entero en capas, 3-401.11(A)(1)) **o la cifra del condado si es más estricta** (algunos piden 155 °F); los 70 °C del ES (guía AESAN) **no se convierten**; tiempo máximo en el broiler y cono sobrante = los del condado, sin cifra; cono recibido 0 °F / 41 °F |
| D-TAC | Salsas, masa, guisados | Pico de gallo y salsas con tomate cortado **TCS** (1-201.10): 41 °F o **TPHC 4 h** con procedimiento escrito (3-501.19); guacamole como TCS [criterio del kit]; **masa fresca y nixtamal = alimento vegetal tratado por calor, TCS** (1-201.10): 41 °F o TPHC; guisados y carne cortada del trompo **≥ 135 °F**; recalentado **165 °F 15 s en 2 h** (3-403.11; el ES dice 1 h); enfriado 135 → 70 → 41 °F (3-501.14) + date marking 7 días; tinga (aves) **165 °F instantáneo** (3-401.11(A)(3)) |
| D-TAC | Pescado crudo | Aguachiles y tostadas: las tres opciones de 3-402.11, registro 90 días (3-402.12) y **aviso al consumidor** (3-603.11), en 03 B20 (`POR_CELDA`) y en Cuaresma |
| D-TAC | Alérgenos | Los 9 de EE. UU. (salsa macha = cacahuete y/o sésamo, moles = frutos de cáscara / cacahuete / sésamo, tortilla de harina = **trigo**, no «gluten»); **aviso escrito** de lo no envasado donde se adoptó el Food Code 2022 (3-602.12(C)); no prometer «gluten-free» con freidora o comal compartidos (21 CFR 101.91); limpiar licuadora y molcajete = lavar (quita el alérgeno) + sanitizar; UK: 14 |
| D-TAC | Alcohol, propinas, delivery | Mezcal, tequila y cerveza **solo con licencia**, 21+ con ID; propinas por tip pool escrito sin managers (29 U.S.C. 203(m)(2)(B)); apps DoorDash / Uber Eats / Grubhub; bolsa térmica 135 / 41 °F; precinto → tamper-evident seal; importador → **Mexican food distributor** |
| D-TAC | Lecciones de los hermanos | Tiras de sanitizante (4-501.114) en 8 tareas de limpieza · date marking · `AJUSTE_MAQUETA_ES = True` · `TERMINOS_PROHIBIDOS` (restaurant salvo consultant, host stand, head / sous chef, shift lead, busser, barback, banquet, BEO, commissary, venue, line-up, pizza, burger, **plancha**, **Tex-Mex**, MOD) · `FRASES_OK_EXTRA` = «al pastor» (**F2: gancho en `restos_espanol`**, «al» es funcional ES) · nunca «El Grito» ni «Día de…» (tilde y funcional) |
| D-UK | UK | Nota UK del B02 (B8, la del base); 14 alérgenos; 8 °C / 63 °C en la FAQ de la landing (F3) |

## 2. Ficheros (D5) — títulos en `mapas_taco.TITULOS`

| # | Fichero ES | Fichero EN |
|---|---|---|
| 01 | `01-apertura-cierre-taqueria.xlsx` | `01-taco-shop-opening-closing-checklists.xlsx` |
| 02 | `02-trompo-plancha-comal.xlsx` | `02-trompo-griddle-comal-checklists.xlsx` |
| 03 | `03-appcc-salsas-alergenos.xlsx` | `03-taco-shop-food-safety-salsa-bar-allergens.xlsx` |
| 04 | `04-nixtamal-tortilla-guisados.xlsx` | `04-nixtamal-masa-tortilla-guisados-checklists.xlsx` |
| 05 | `05-tareas-manager.xlsx` | `05-taqueria-manager-checklist.xlsx` |
| 06 | `06-tareas-perfiles.xlsx` | `06-taco-shop-duties-by-role.xlsx` |
| 07 | `07-semanales-mensuales.xlsx` | `07-taco-shop-weekly-monthly-cleaning-checklist.xlsx` |
| 08 | `08-eventos-estacionales.xlsx` | `08-taco-shop-event-seasonal-checklists.xlsx` |
| 09 | `09-plantilla-personalizable.xlsx` | `09-blank-taco-shop-checklist-template.xlsx` |
| B01 | `BONUS-01-briefing-servicio.xlsx` | `BONUS-01-taco-shop-pre-shift-meeting-template.xlsx` |
| B02 | `BONUS-02-calendario-anual.xlsx` | `BONUS-02-taco-shop-annual-calendar.xlsx` |

## 3. Reglas del delta (`mapas_taco.REGLAS_US` = las del base + estas; 45 en total)

| Concepto | Fuente |
|---|---|
| Trompo ≥ 145 °F 15 s o la cifra del condado (155 °F en algunos); tiempo en el broiler y cono sobrante, del condado | FDA Food Code 2022 §3-401.11(A)(1); [local] research US §6.2 (Sacramento, Orange 145 °F; Alameda, Marin 155 °F; resumen) |
| Aves 165 °F instantáneo · recalentado 165 °F 15 s en 2 h · enfriado 135 → 70 → 41 °F · date marking 7 días | §3-401.11(A)(3); §3-403.11(A); §3-501.14; §3-501.17 |
| Tomate cortado y alimento vegetal tratado por calor (masa, nixtamal) = TCS · TPHC 4 h | §1-201.10; §3-501.19(B); guacamole [criterio del kit] (research US §6.1) |
| Frío 41 °F · congelado 0 °F · caliente 135 °F · bolsa de delivery 135 / 41 °F | §3-501.16 (base) |
| Pescado crudo: parásitos y registro · aviso al consumidor | §3-402.11, §3-402.12, §3-603.11 (base) |
| 9 alérgenos · aviso escrito de lo no envasado · «gluten-free» | FALCPA + FASTER Act; §3-602.12(C) (como el chocolate); 21 CFR 101.91 (research US §6.5) |
| Propinas sin managers · 21 años · licencia de alcohol | 29 U.S.C. 203(m)(2)(B); 23 U.S.C. 158; [estatal] ABC (research US §6.7) |
| Gas por profesional con licencia · campana NFPA 96 · calibración 32 °F | [local] código de gas (base 05 B10); NFPA 96 (base); [criterio del kit] + §4-502.11(B) |
| Días fuertes de una taquería US · kg → lb, litros → qt | [criterio del kit]; research ES §7.3 (Cinco de Mayo, fiesta sobre todo de EE. UU.) |

°F que el kit puede afirmar (G7, `GRADOS_F_SPEC`; el autotest exige la igualdad con POR_CELDA + ADAPTAR + reglas propias):
−31, −4, 0, 32, 41, 70, 100 (lavamanos, regla base), 135, 145, 155, 165. Las 31 celdas ES con °C llevan ADAPTAR o
POR_CELDA (`cruzar_censo` lo exige); `CELSIUS_SIN_F` = 01 «Apertura» B15 (F2: con el reorden, su °F va en la B14). `CITA_AUTOTEST` = 3-501.18 (la 3-501.19 sí está en las reglas).

## 4. Memoria de traducción (`../heredar.py --kit taco`; `MEMORIA`: base, pizzería, hamburguesería, cafetería, ghost kitchen)

**648 cadenas** (1.940 apariciones); **GM 158** (645 palabras: 26 pestañas, 55 de glosario y 77 regeneradas: 86 celdas `POR_CELDA`, las
246 horas, título interior, versión, marca). De las **490 a traducir: 32 heredadas** (todas exactas y del base: las
Instrucciones comunes; 293 palabras) y **458 pendientes** (457 nuevas + 1 «contexto», el «N/A» del base que dice
«restaurant»; **4.982 palabras**; 110 con ADAPTAR): **G1 222 cadenas / 2.672 palabras** (comunes + 01-04) y **G2 236 /
2.310** (05-09 y bonus). Los hermanos no aportan nada: las tareas de una taquería no existen en ellos. Propuesta F2:
UN traductor sonnet en dos tandas en serie (G1 fija la prosa en `textos_en/glosario.json`; G2 con ese glosario) →
`textos_en/G1.json` con los 458 ids.

    python3 extraer_textos.py --kit taco && python3 taco/mapas_taco.py && python3 heredar.py --kit taco
    python3 aplicar_en.py --kit taco --dry-run [--parcial] --idempotencia --mes <mes de la F2>; python3 gates_en.py --kit taco [--parcial] --dir <carpeta> [--autotest]

F2, además: los dos ganchos de `gates_en.py` (D12 sin caja, D-TAC `FRASES_OK_EXTRA`), `taco-shop-checklist-templates`
en `PRODUCTOS_LETTER` (`censo-entregables.py`) y `EXCLUIDOS` (`postprocess-transversal.py`); papel A4 → Letter en las 36.

## 5. Erratas del ES (para su próxima v2.x; la EN nace corregida)

- 01 «Apertura Taquería» B14-B15: «Montar el trompo del día» (11:00) va ANTES de «Comprobar el cono recibido» (11:05); en
  02 «Marinado» (B13 → B14) y 06 «Taquero» (B6 → B7) el orden es el bueno.
- 07 «Tareas Mensuales» B6 y B9, y B02 fila 8: «Revisar la instalación de gas … y archivar el parte» como tarea mensual
  del encargado mezcla la inspección visual (sí, del equipo) con la revisión periódica de la instalación (de empresa
  habilitada, con su certificado): separarlas.
- Horas fuera de orden dentro de una sección (sugerencias, la EN las deja): 02 «Marinado» B8 (19:02 tras 19:05) y B11
  (19:15 tras 20:00); 04 «Tortilla y Comal» B11-B14 (12:30, 11:00, 23:00, 15:00).
