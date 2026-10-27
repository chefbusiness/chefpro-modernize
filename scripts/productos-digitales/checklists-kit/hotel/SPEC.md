# Hotel Checklists Kit Pro — SPEC DELTA (F1 · 27-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas Hotel Completo** (`kit-tareas-hotel`, 18,50 €, 19 xlsx v2.0, 636
> tareas + 24 fechas). Décimo hermano vertical: **lo que no está aquí es la SPEC base** (`../SPEC.md` §0-§9). Mapas:
> `mapas_hotel.py` (importa `../mapas.py`). Inventario: `F1-inventario-es.md`. Tamaño M ($29). 74 hojas.

## 0. Cómo pasa el molde Hotel por el circuito (medido, no supuesto)

El Hotel **no** es un molde nuevo: es el **híbrido de la heladería** con más libros y otra numeración. El censo lo prueba:
- **01-15 y BONUS-01** (49 checklists): molde ligero del catering y la heladería (# · Tarea · Zona · Responsable · ✓ ·
  Hora · Notas, cabeceras internas, contadores que restan «Tarea», CF `$E6="✓"`, sin protección, subtítulo A2).
- **18 y 19** = el 08 y el 09 del kit base con la variante «Hotel Completo» (el 19, idéntico salvo la variante y las
  horas: `cruzar_base` compara textos y fórmulas de caja con el base y da 0 diferencias). No hay 16 ni 17.
- **BONUS-02**: calendario propio, 24 filas (5-28): # · Fecha / Período · Impacto · Preparación F&B · Antelación · Notas.

`extraer_textos`, `aplicar_en`, `heredar` y `volcar_xlsx` **sirven tal cual** (leen `mapas.LIBROS_ES` y el corto de
cualquier número). **Código común tocado (mínimo):** `gates_en.py` leía la caja del libro `'09'` fijo en 4 sitios (en el
hotel el 09 es housekeeping) → ahora `HOJA_CAJA[0]`, que vale `'09'` en los 10 kits publicados; y la mutación de área de
impresión del autotest tomaba la 3.ª pestaña del 06 (el 06 del hotel tiene una) → gancho `HOJA_AREA_AUTOTEST` (getattr,
sin él igual que antes). `kit.py`: `hotel` en `VERTICALES`. **Regresión** (§7.3): `gates_en` y `--autotest` de
`origin/main` frente a la rama sobre los 10 kits EN publicados = salida idéntica byte a byte; `aplicar_en.py` no cambia.

**Prueba de humo F1** (VPS, `--dry-run --parcial` con textos vacíos): `aplicar_en` monta los 19 libros en 11 s,
`inject_cache` sin fallos; **gates VERDE 8/0** (G1 74 hojas · 197 fórmulas · 54 DV · 55 CF, 27 por celda · 345 merges ·
5 protegidas · 811 desbloqueadas; G5 caja 204.91 / 4,200 / 0 sobre el 19; G8 censo + no latinos 0); **autotest 19/19
CAZADOS** (los 16 del base + término prohibido + 2 de la CF de excepción).

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `hotel-checklist-templates` → `/en/digital-products/hotel-checklist-templates` (+ `/access`, `/library`); productId = slug; JWT `hotel-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_HOTEL_CHECKLISTS_KIT`; ficheros en `dl/hotel-checklist-templates/`; familia `kit-tareas-hotel` en `tienda.ts` con hreflang recíproco |
| D2 | Nombre | **Hotel Checklists Kit Pro**; title SEO = H1 (Forma B, 69): «Hotel Checklists Kit Pro: Housekeeping, Front Desk, F&B & Maintenance». Sin «Hotel Completo / Integral»; el subtítulo A2 va por `GLOSARIO` con el nombre EN |
| D3-D4 | Precio | **$29 USD** pago único (19 libros; el ES va a 18,50 € frente a 12-14 € del resto, misma escalera que $19); sin `priceOld`, «% off», «worth $X» ni anclas (FTC 16 CFR 233.1, PR #117): «One-time payment · lifetime access · updates included». Sin `aggregateRating` ni `review` (el ES los lleva) |
| D5 | Ficheros | §2. Demanda US (§R): hotel housekeeping / room cleaning / cleaning checklist 260 (una sola serie) · maintenance 70 · front desk 30 · night audit 20; turndown service 4.400 y BEO 9.900 son informativas: van en títulos, no en el H1 |
| D6 | Pestañas | 55 checklists + 19 «Instructions»: Breakfast Opening / Closing · Lunch / Dinner Buffet · Restaurant Opening / Closing · Pool Bar · Lobby Bar & Lounge · Snack Bar & Grab-and-Go · In-Room Dining · Minibar · Banquets & Events · AM / PM / Night Audit Shift · Check-In & Check-Out · Concierge · Guest Experience · Checkout / Stayover Room Cleaning · Turndown Service · Deep Cleaning · Linen Control · Lobby · Corridors & Elevators · Public Restrooms · Parking · Pool Opening / Closing · Weekly Pool Maintenance · Towel Service · Seasonal Setup · Daily Service · Daily Rounds · Weekly PM · Monthly PM · Quarterly & Annual · HVAC · Plumbing · Electrical · Revenue Management · Reservations · Accounting · HR Operations · Spa Opening / Closing · Treatment Rooms · Locker Rooms · **Opening / Closing Rounds** (18) · caja del base · Daily F&B Briefing · F&B Calendar |
| D7 | CF | Desviación declarada (catering M5, heladería D7): en las **27 hojas** cuyo rango contiene una cabecera interna, `$E6="✓"` → `AND($E6="✓",$B6<>"Task")` (`CF_POR_CELDA`; `cruzar_censo` exige «cabecera dentro ⇔ en la lista»). `CLAVES` + «Tarea» → «Task» |
| D8 | Glosario | base + 43 celdas; 5 sobrescriben el base: Admin → **Admin**, Recepción → **Front desk**, Sala → **Dining room**, Zonas comunes → **Public areas**, Encargado → **Manager on duty** (MOD). Mantenimiento → **Engineering**, Room Service → **In-room dining**, Lencería → **Linen room**, À la Carte → Restaurant, Vestuarios → Locker rooms, cadencias (Semiannual, Every 2 years), tabla de congelación (6–12 / 3–6 / 1–2 months, Do not freeze), cabeceras del B02. 670 celdas de puesto/zona |
| D9 | Horas | Las 29 horas de celda (18 E5-E22, 19 D5-D15, 05:30-06:15) → `hora_us` **sin desplazar**: el F&B de un hotel arranca con el desayuno. Las 7 de los títulos de sección («(05:30-06:30)»), el traductor |
| D10 | Orden y erratas | 18 «Closing Rounds» reordenado (§5): los check-outs pendientes y la luz de zonas públicas van ANTES de la persiana, la alarma y la llave; 4 responsables cambian (`_RESPONSABLE_CAMBIA`). El hotel no cierra: el 18 son las rondas de los **outlets de F&B y las zonas públicas** (ADAPTAR del 18 «Instructions» B6 y «Opening Rounds» B5) |
| D11 | 13 «Quarterly & Annual» | 23 filas fijadas en `POR_CELDA` (B y, si cambia, F): plagas mensual con muestra de chinches · campana NFPA 96 · auditoría o ATP opcional · plan de seguridad alimentaria · food handler cards + CFPM · calibración (32 °F) · torres y ACS (ASHRAE 188; NY) · muestreo de legionela · agua caliente 140 / 120 °F (CDC) · agua de piscina y spa · vaciado y tapas VGB · rociadores y alarma (NFPA 25 / 72) · extintores (OSHA 1910.157(e)(3)) · gas · eléctrica (NFPA 70B) · ascensores y calderas (inspector estatal) · simulacro · aceite y residuos peligrosos · seguros · fichajes + I-9 · PMS / POS + PCI DSS · permisos. Las filas 35-36 (escandallos, nº de parte), el traductor. 14 RRHH B12 = fichajes FLSA (B16 del base) |
| D12 | Caja | 19 = 09 del base: `DENOMINACIONES`, `FORMULAS_POR_CELDA`, `POR_CELDA` (47) y `ADAPTAR` (7) heredados con la clave renumerada; `HOJA_CAJA = ('19', …)`; G5 con el caso de la SPEC base (204.91; 4,200 y 0) |
| D13 | Moneda | 282 formatos con € → `#,##0.00`; 20 textos con € → rótulos de caja o «in your currency» |
| D14 | Calendario | B02, 24 filas cronológicas con las anuales al final: New Year's Day · Valentine's · St. Patrick's · Spring break & Easter · shoulder (MICE) · **proms, graduations & showers** (sustituye a comuniones) · **Mother's Day** (pico de brunch) · **wedding season May–Oct** · **Memorial Day** · summer peak + July 4 · Labor Day & conferences · fall menus · Halloween · **Thanksgiving** · Black Friday · holiday parties · Christmas Eve / Day · NYE (21+) · brunch · VIP amenities · MICE · local events (+ nota UK) · health inspection. B, C y E fijados; D, traductor con ADAPTAR |
| D-HOT | F&B | FDA Food Code 2022 como el base: 41 / 135 °F, parásitos 3-402.11 (sin anisakis ni CE 853/2004), lavado 3-302.15, date marking 7 días, 9 alérgenos, tiras de sanitizante; buffet: sneeze guard 3-306.11, plato limpio 3-304.16, vigilancia 3-306.13; lo expuesto no se reutiliza [criterio del kit]; sala 68–72 °F; alcohol 21+; **sin vidrio en la zona de piscina** (MAHC §5.6.9.2) |
| D-HOT | Piscina y spa | **MAHC 2024 (5.ª ed.)**, código modelo (manda el estatal): cloro libre ≥ 1.0 ppm (2.0 con CYA), spa ≥ 3.0, pH 7.0–7.8, medir antes de abrir y cada 2 h (manual) / 4 h (automático), registros 3 años; «No Lifeguard on Duty»; VGB (15 U.S.C. 8003); HazCom; hot tub ≤ 104 °F (objetivo del kit 95–100 °F, ES 35-38 °C); operador cualificado (p. ej. CPO en Texas) |
| D-HOT | Housekeeping y seguridad | room attendant, stayover / checkout, DND con welfare check (política de la marca), par 3 [criterio del kit], chinches al deshacer la cama, sangre y agujas (OSHA 1910.1030), desinfectante registrado en la EPA con su tiempo de contacto, botón de pánico donde la ley local lo exige (Chicago, Seattle, New Jersey) |
| D-HOT | Back office | OTAs US (Expedia, Booking.com) y la **regla de la FTC sobre tarifas** (16 CFR Part 464: precio total con resort fee, desde 12-may-2025); FLSA 2/3 años + I-9; overtime > 40 h; walk the guest; sin estrellas oficiales (economy · midscale · upscale · luxury) |
| D-HOT | Testimonios (F3) | Los 10 del ES (`kit-tareas-hotel.ts` §testimonials y `src/data/testimonials-hotel.ts`) citan marcas reales (Palace, Meliá, W, Ritz-Carlton, Four Seasons, NH): en EN se traducen como en los hermanos **sin marcas, cadenas ni hoteles reales**: rol + tipo de hotel + ciudad («F&B Manager, luxury city hotel, Madrid»), subtítulo «…with Kit de Tareas Hotel, the Spanish edition of this kit» |
| D-HOT | Términos | `TERMINOS_PROHIBIDOS` (G2): pizza, burger, ghost kitchen, packer, app manager, commissary, coffee / ice cream / scoop / pastry / chocolate shop, dipping cabinet, batch freezer, scooper, bakery case, food truck, FOH. Permitidos: restaurant, bartender, server, host stand, banquet, BEO, line cook. `RX_CONTEXTO_PENDIENTE` (heredar): lo heredado con «restaurant», FOH, host stand o shift manager va al traductor con su `base_en` |
| D-UK | UK | nota UK en el B02 (bank holidays, Mothering Sunday, Boxing Day); 14 alérgenos; FAQ de la landing: PWTAG para piscinas, HSE L8 (60 / 50 °C), Fire Safety Order 2005, FIR 2014 |

## 2. Ficheros (D5) — títulos en `mapas_hotel.TITULOS`

| # | Fichero ES | Fichero EN |
|---|---|---|
| 01 | `01-fb-buffet-desayuno.xlsx` | `01-hotel-breakfast-buffet-checklists.xlsx` |
| 02 | `02-fb-buffet-comida-cena.xlsx` | `02-hotel-lunch-dinner-buffet-checklists.xlsx` |
| 03 | `03-fb-restaurante-carte.xlsx` | `03-hotel-restaurant-opening-closing-checklists.xlsx` |
| 04 | `04-fb-outlets.xlsx` | `04-hotel-bar-grab-and-go-checklists.xlsx` |
| 05 | `05-fb-room-service-minibar.xlsx` | `05-in-room-dining-minibar-checklists.xlsx` |
| 06 | `06-fb-banquetes-eventos.xlsx` | `06-hotel-banquet-event-checklist.xlsx` |
| 07 | `07-recepcion-turnos.xlsx` | `07-hotel-front-desk-checklists-night-audit.xlsx` |
| 08 | `08-guest-services.xlsx` | `08-concierge-guest-experience-checklists.xlsx` |
| 09 | `09-housekeeping.xlsx` | `09-hotel-housekeeping-checklists.xlsx` |
| 10 | `10-areas-publicas.xlsx` | `10-hotel-public-area-cleaning-checklists.xlsx` |
| 11 | `11-piscina.xlsx` | `11-hotel-pool-checklists.xlsx` |
| 12 | `12-terraza.xlsx` | `12-hotel-patio-terrace-checklists.xlsx` |
| 13 | `13-mantenimiento.xlsx` | `13-hotel-preventive-maintenance-checklists.xlsx` |
| 14 | `14-administracion.xlsx` | `14-hotel-back-office-checklists.xlsx` |
| 15 | `15-spa-wellness.xlsx` | `15-hotel-spa-checklists.xlsx` |
| 18 | `18-apertura-cierre-negocio.xlsx` | `18-hotel-daily-opening-closing-rounds.xlsx` |
| 19 | `19-apertura-cierre-caja.xlsx` | `19-cash-drawer-opening-closing.xlsx` |
| B01 | `BONUS-01-briefing-servicio.xlsx` | `BONUS-01-hotel-daily-fb-briefing-template.xlsx` |
| B02 | `BONUS-02-calendario-anual-tareas.xlsx` | `BONUS-02-hotel-fb-calendar.xlsx` |

## 3. Reglas del delta (`mapas_hotel.REGLAS_US` = las del base salvo recalentado + estas; 57 en total)

| Concepto | Fuente (estado) |
|---|---|
| Cloro libre ≥ 1.0 ppm (2.0 con CYA), spa ≥ 3.0; pH 7.0–7.8; antes de abrir y cada 2 / 4 h; registros 3 años | CDC MAHC 2024 §5.7.3.1.1.2, §5.7.3.4.1, §5.7.5, §6.4.1.2.1 (primaria) |
| Incidente fecal: 2 ppm 25 min (formadas o vómito), 20 ppm 12,75 h (diarrea), pH ≤ 7.5, agua ≥ 77 °F | MAHC 2024 §6.5.3 (primaria) |
| Sin vidrio · «No Lifeguard on Duty» · hot tub ≤ 104 °F y su cartel | MAHC 2024 §5.6.9.2, §6.4.2.2.3.4, §5.7.4.7.2, §6.4.2.2.3.7 (primaria) |
| Tapas de sumidero antiatrapamiento · operador cualificado | 15 U.S.C. 8003 (resumen del texto); MAHC §6.1; 25 TAC Ch. 265 (Texas) |
| Legionela: water management program; agua caliente ≥ 140 °F almacenada, ≥ 120 °F en circulación; purgar salidas sin uso | ASHRAE 188; CDC Legionella toolkit; NYC Local Law 77 (2015), 10 NYCRR Part 4 (124 °F de retorno: NO verificado, no se usa) |
| Rociadores, alarma, puertas cortafuegos; alumbrado de emergencia 30 s / mes y 90 min / año | NFPA 25, 72, 80 (secundaria: el kit solo dice «quarterly and annual items» y «periodic» en las puertas); NFPA 101 §7.9.3 (secundaria, Kansas Fire Marshal) |
| Extintores: visual mensual y mantenimiento anual | 29 CFR 1910.157(e)(2)-(3) (primaria) |
| Eléctrica: programa de mantenimiento, termografía anual [criterio del kit] · ascensores y calderas: inspector estatal | NFPA 70B (2023); [estatal] Texas H&S Code Ch. 754; 522 CMR 4.05 (Massachusetts) |
| Sangre y agujas · productos químicos · chinches · botón de pánico | 29 CFR 1910.1030 (primaria); 29 CFR 1910.1200; EPA; [local] Chicago, Seattle, New Jersey |
| FDA Food Code (buffet, temperaturas, parásitos, lavado, etiqueta, CFPM) | §3-306.11, 3-304.16, 3-306.13, 3-501.16, 3-402.11/12, 3-302.15, 3-602.11, 2-102.12 (primaria) |
| Tarifas obligatorias en el precio total · FLSA · I-9 · PCI DSS | 16 CFR Part 464 (primaria); 29 CFR 516.5-516.6; 8 CFR 274a.2(b)(2); PCI DSS (norma del sector) |

°F que el kit puede afirmar (G7, `GRADOS_F_SPEC`; el autotest de `mapas_hotel` exige la igualdad con lo que dicen REGLAS_US,
POR_CELDA y ADAPTAR): −31, −4, 0, 32, 41, 68, 70, 72, 75, 77, 79, 95, 100, 104, 120, 135, 140. `CELSIUS_SIN_F` vacío: las
23 celdas ES con °C llevan su °F en `ADAPTAR`.

## 4. Memoria de traducción (`../heredar.py --kit hotel`; `MEMORIA`: base, catering, heladería, chocolatería y el resto)

1.236 cadenas; **GM 298** (1.425 palabras: pestañas, glosario, 194 `POR_CELDA`, 29 horas, marca, versión). De las 938 a
traducir: **107 heredadas** (104 exactas + 3 por sufijo; 81 del base, 20 del catering, 5 de la heladería y 1 de la
chocolatería; 1.103 palabras) y **831 pendientes** (818 nuevas, 8 con otro ADAPTAR, 5 «contexto»; **7.217 palabras**;
133 con ADAPTAR): **G1 418 cadenas / 3.968 palabras** (comunes + 01-08) y **G2 413 / 3.249** (09-15, 18, 19 y bonus).

    python3 extraer_textos.py --kit hotel && python3 hotel/mapas_hotel.py && python3 heredar.py --kit hotel
    python3 aplicar_en.py --kit hotel --dry-run [--parcial] --idempotencia --mes October; python3 gates_en.py --kit hotel [--parcial] --dir <carpeta> [--autotest]

## 5. Erratas del ES (para su próxima v2.x; la EN nace corregida)

- 18 «Cierre del Negocio»: B18 (check-outs pendientes) y B19 (luz de zonas nobles) DESPUÉS de B16 (alarma) y B17 (llave);
  B9 cierra persianas antes de recoger la señalización (B12). En un hotel, la luz de zonas públicas pasa a modo noche
  (señales de salida y alumbrado de evacuación siempre encendidos).
- 18 y 19: la línea de marca y el título de «Instrucciones» B2 dicen «Apertura y Cierre» como variante (debería ser
  «Hotel Completo»).
- Frío incoherente: «< 5 °C» (01 «Apertura Desayuno» B26, 02 «Buffet Almuerzo» B16, 04 «Snack Bar» B7) frente a «0-4 °C»
  en el resto del kit. La EN: 41 °F en todos.
- 15 «Apertura Spa» B6: «piscina/jacuzzi (35-38 °C)»: 35-38 °C es del jacuzzi, no de una piscina. La EN: hot tub.
  **RESUELTA en el ES LIVE (27-oct-2026):** B6 → «Verificar temperatura del jacuzzi (35-38 °C) y ajustar».
- 18 «Apertura del Negocio» es la plantilla de restaurante (alarma, persianas, carta a las 05:30) con 3 tareas de hotel:
  en un hotel 24 h solo vale para los outlets; la EN lo dice (D10).

- **RESUELTAS en el ES LIVE (27-oct-2026, parche en el XML de las celdas, sin cambio de versión ni correo; mismo texto en
  `scripts/generate-tareas-hotel.py`; las 3 de `ERRATAS-ES.md`):** 15 «Cierre Spa» B7 (seguridad: «Apagar saunas y baño
  de vapor; en el jacuzzi apagar solo chorros y soplante: la filtración, la recirculación y la desinfección siguen en
  marcha toda la noche»), 15 «Apertura Spa» B6 (jacuzzi 35-38 °C) y 09 «Deep Cleaning» B13 (suelos duros pulidos,
  moqueta lavada por inyección-extracción).

## 6. Landing EN (F3) — réplica de `astro-site/src/data/productos/tareas/kit-tareas-hotel.ts`

En `data/productos-en/tareas/hotel-checklist-templates.ts` con `KitTareasLandingPage` (`lang`), como los 10 hermanos. Lo
que cambia respecto del molde de los hermanos: precio $29 (D3); sin `aggregateRating`, `priceOld` ni `discountBadge`
(el ES los lleva); testimonios sin marcas (D-HOT); grid de 17 plantillas + 2 bonus + Equivalents Guide; descripción con
«636 hotel tasks already written». **FAQ** (PAA US, §R): «What should be on a hotel housekeeping checklist?» · «What is
the proper procedure for cleaning a guest room?» · «How often are hotel rooms cleaned?» (stayover / checkout / deep
clean) · «How do hotels prevent bed bugs?» · «What are the steps of the night audit?» · «What is a hotel preventive
maintenance checklist?» · «Is there a free hotel checklist template in Excel?» + las del ES adaptadas + «Does it work in
the UK, Canada or Australia?». Google Sheets solo si el test de F3 lo confirma.

## 7. Plan, presupuesto y riesgos

1. **F2 (≤ 1,4 M):** DOS traductores sonnet en serie, G1 primero (fija la prosa: `textos_en/glosario.json` del base +
   lo nuevo), G2 con su glosario; cada uno: sus ids de `pendientes.json`, esta SPEC, `GLOSARIO`, `HOJAS`, `POR_CELDA`,
   `REGLAS_US`, `heredado.json`, la sección Hotel de `GLOSARIO-JERGA-ES-EN.md` y el brief de `../SPEC.md` §7.2 (≈ 0,5 M).
   Montaje y gates en el VPS (`/root/wt-hotel`, ya creado; ≈ 0,15 M); `hotel-checklist-templates` en `PRODUCTOS_LETTER`
   (`censo-entregables.py`) y `EXCLUIDOS` (`postprocess-transversal.py`); UNA revisión adversarial sonnet (lente de un
   GM / director de operaciones US + lente técnica, sobre los volcados) y una ronda (≈ 0,5 M).
2. **F3 (≤ 0,5 M):** landing §6, `tienda.ts`, backend con `lang: 'en'`, access / library (copia de un hermano con 19
   descargas), email, `llms.txt`, sitemap y enlaces entrantes (hub EN, catálogo, `footerLinks` de los hermanos).
3. **Regresión del código común (hecha en F1):** `gates_en.py` de `origin/main` frente al de la rama sobre los 10 kits
   publicados (gates + `--autotest`): salida idéntica (`F1-inventario-es.md` §4). Repetirla si la F2 toca código común.
4. **Riesgos para el orquestador:** (a) el 18 reinterpretado como rondas de outlets y su cierre reordenado (D10: 15 filas
   fijadas, 4 responsables cambian); (b) 13 «Quarterly & Annual» con 6 cadencias cambiadas (plagas mensual, campana
   semestral, extintores, gas, eléctrica y ascensores anuales) y NFPA 25 / 72 / 80 / 70B sin texto primario (el kit no
   da sus intervalos salvo el alumbrado de emergencia); (c) el MAHC es modelo: el kit dice siempre «manda tu código
   estatal»; (d) $29 frente a los $19 de los hermanos; (e) G1 = 3.968 palabras para un traductor (la pastelería hizo
   4.531 en uno); (f) testimonios sin marcas; (g) el texto «montaje de los 11 libros» de `aplicar_en` es solo un
   rótulo (monta 19).

## R. Research (una pasada, 27-oct-2026)

**Demanda (DataForSEO, US 2840/en):** banquet event order 9.900 · turndown service 4.400 · in room dining 880 · housekeeping
checklist 390 (HIGH; la doméstica de Pinterest) · hotel housekeeping / room cleaning / cleaning checklist 260 (una serie) ·
pool maintenance checklist 170 · pool log sheet 170 · pool opening checklist 110 · hotel maintenance / preventive
maintenance checklist 70 · pool chemical log 70 · hotel housekeeping checklist template 50 · hotel checklist 50 · hotel
room inspection checklist 40 · front desk checklist 30 · night audit checklist 20; hotel front desk, banquet, room
service, minibar, deep cleaning, linen inventory, spa cleaning, opening, manager checklist ≤ 10. **SERP:** «hotel
housekeeping checklist» = plantillas gratis (Cloudbeds, SafetyCulture / Mitti, GoAudits, Roommaster, HotelRunner,
template.net, Amadeus, Pinterest PDF), AI Overview; relacionadas «excel», «pdf», «template free». «hotel maintenance
checklist» = PM con CMMS (Maintainly, ClickMaint, Coast, Oxmaint, WorkTrek); PAA del 3 P's / 80-20. Nadie vende el hotel
entero en Excel con contadores y °F: el ángulo es «19 libros, 636 tareas, del desayuno al night audit». **PAA:** cleaning
a guest room, typical housekeeping tasks, how often rooms are cleaned, bedding washed between guests, bed bugs; night
audit steps, functions y responsibilities. **Normativa:** agente sonnet con el MAHC 2024 y el Food Code 2022 leídos en PDF
y el eCFR (1910.157, 1910.1030, 16 CFR 464); NFPA, ASHRAE e IPC sin texto primario (de pago): secundaria y marcada.
