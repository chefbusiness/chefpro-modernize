# Hotel Checklists Kit Pro — F1 · inventario del ES publicado (27-oct-2026 · sesión Claude Code)

> Fuente: los 19 xlsx PUBLICADOS en `astro-site/public/dl/kit-tareas-hotel/` (no el generador
> `scripts/generate-tareas-hotel.py`), leídos en el VPS con `extraer_textos.py --kit hotel` → `censo_es.json` y
> `textos_es.json`. El docx de equivalencias ES ↔ LatAm no cruza: en EN va el bonus común de `dl/en-shared/`.
> Decisiones: `SPEC.md`. Las tablas §0 y §1 son las que imprime `extraer_textos.tabla_md` / `tabla_dependencias_md`.

## 0. Censo por libro

| Libro | Hojas | Texto | Tareas | Fórmulas | Fx→hoja | DV | CF | Merges | Protegidas | Horas 24 h | °C | Fmt € | Textos € | Verdes | Desbloq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01-fb-buffet-desayuno | 3 | 250 | 64 | 4 | 0 | 2 | 2 | 27 | 0 | 0 | 8 | 0 | 0 | 155 | 0 |
| 02-fb-buffet-comida-cena | 3 | 135 | 35 | 4 | 0 | 2 | 2 | 13 | 0 | 0 | 4 | 0 | 0 | 70 | 0 |
| 03-fb-restaurante-carte | 3 | 110 | 28 | 4 | 0 | 2 | 2 | 12 | 0 | 0 | 2 | 0 | 0 | 56 | 0 |
| 04-fb-outlets | 4 | 162 | 39 | 6 | 0 | 3 | 3 | 19 | 0 | 0 | 3 | 0 | 0 | 78 | 0 |
| 05-fb-room-service-minibar | 3 | 146 | 38 | 4 | 0 | 2 | 2 | 14 | 0 | 0 | 0 | 0 | 0 | 76 | 0 |
| 06-fb-banquetes-eventos | 2 | 127 | 34 | 2 | 0 | 1 | 1 | 9 | 0 | 0 | 0 | 0 | 0 | 68 | 0 |
| 07-recepcion-turnos | 5 | 194 | 48 | 8 | 0 | 4 | 4 | 24 | 0 | 0 | 0 | 0 | 0 | 96 | 0 |
| 08-guest-services | 3 | 100 | 23 | 4 | 0 | 2 | 2 | 12 | 0 | 0 | 0 | 0 | 0 | 46 | 0 |
| 09-housekeeping | 6 | 216 | 52 | 10 | 0 | 5 | 5 | 29 | 0 | 0 | 1 | 0 | 0 | 104 | 0 |
| 10-areas-publicas | 5 | 122 | 28 | 8 | 0 | 4 | 4 | 20 | 0 | 0 | 0 | 0 | 0 | 56 | 0 |
| 11-piscina | 5 | 130 | 28 | 8 | 0 | 4 | 4 | 21 | 0 | 0 | 0 | 0 | 0 | 56 | 0 |
| 12-terraza | 3 | 80 | 17 | 4 | 0 | 2 | 2 | 11 | 0 | 0 | 0 | 0 | 0 | 34 | 0 |
| 13-mantenimiento | 8 | 299 | 69 | 14 | 0 | 7 | 7 | 38 | 0 | 0 | 3 | 0 | 0 | 138 | 0 |
| 14-administracion | 5 | 125 | 28 | 8 | 0 | 4 | 4 | 20 | 0 | 0 | 0 | 0 | 0 | 56 | 0 |
| 15-spa-wellness | 5 | 138 | 28 | 8 | 0 | 4 | 4 | 22 | 0 | 0 | 2 | 0 | 0 | 56 | 0 |
| 18-apertura-cierre-negocio | 3 | 189 | 33 | 4 | 0 | 2 | 2 | 12 | 2 | 18 | 0 | 0 | 0 | 278 | 344 |
| 19-apertura-cierre-caja | 4 | 182 | 23 | 95 | 1 | 3 | 4 | 32 | 3 | 11 | 0 | 282 | 20 | 421 | 467 |
| BONUS-01-briefing-servicio | 2 | 90 | 21 | 2 | 0 | 1 | 1 | 8 | 0 | 0 | 0 | 0 | 0 | 42 | 0 |
| BONUS-02-calendario-anual-tareas | 2 | 114 | 24 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 28 | 0 |
| **Total** | **74** | **2909** | **660** | **197** | **1** | **54** | **55** | **345** | **5** | **29** | **23** | **282** | **20** | **1914** | **811** |

Tareas = filas con número en A y texto en B: 636 de checklist + las 24 fechas del B02. Papel: A4 (`paperSize 9`) en las
74 hojas → US Letter. 7 áreas de impresión (18 y 19), 55 títulos de impresión y 55 paneles.

## 1. Lo que depende de España

| Dependencia de España | Apariciones | Cadenas | Destino |
|---|---|---|---|
| Temperaturas en °C | 23 | 23 | D10: °F + FDA Food Code (ADAPTAR o POR_CELDA) |
| Horas de 24 h como celda («07:00») | 29 | 4 | D9: `mapas.hora_us` (regenerar) |
| Horas de 24 h dentro de una frase | 7 | 7 | D9: el traductor, reloj de 12 h |
| Euros (€) en textos | 20 | 20 | D12-D13: dólares en la tabla de caja; sin símbolo en el resto |
| Caja española: TPV, datáfono, Bizum, arqueo, descuadre | 39 | 37 | D12: POS, card terminal, Z/X report, starting bank, over/short, propinas fuera |
| APPCC y «Pack APPCC» | 4 | 4 | D10: HACCP · «HACCP Food Safety Kit Pro» |
| Normativa y administración española | 23 | 23 | D10-D11: FDA Food Code, OSHA, NFPA 96, EPA 608, FLSA, normas locales (POR_CELDA / ADAPTAR) |
| Festivos y costumbres españolas | 16 | 16 | D14: calendario US (`mapas.CALENDARIO`) y ADAPTAR en 06 «Christmas & NYE» |
| Terraza y temporada alta | 36 | 18 | D15: patio / patio season (Memorial Day–Labor Day) |
| Puestos y zonas de la hostelería española (celda entera) | 670 | 42 | D8: `mapas.GLOSARIO` (line cook, prep cook, server, porter, MOD…) |
| Plataformas españolas | 2 | 2 | D16: Google, Yelp, TripAdvisor; Google Business Profile |
| Alérgenos (UE 14) | 10 | 10 | D10: 9 alérgenos US; nota UK 14 |
| Papel A4 citado | 1 | 1 | D17: US Letter |
| Sufijo de variante «Hotel Completo / Integral» | 54 | 6 | D2: la EN no lleva sufijo |
| Citas a ficheros ES (.xlsx) | 6 | 4 | D5: nombre de fichero EN (`mapas.FICHEROS`) |
| Menús de Excel en español | 4 | 2 | Excel EN: «Review → Unprotect Sheet», «right-click → Insert», «Move or Copy» |
| Piscina: cloro, pH y libro obligatorio | 6 | 6 | D-HOT: MAHC 2024 + código estatal (ADAPTAR) |
| Legionela y ACS (RD 487/2022) | 8 | 8 | D-HOT: ASHRAE 188 + CDC (140 / 120 °F) |
| Inspecciones españolas (OCA, RITE, BIE, retimbrado) | 7 | 7 | D11: NFPA, OSHA, inspector estatal o municipal (POR_CELDA del 13) |
| Registro de jornada (RD-ley 8/2019) | 4 | 4 | D11: FLSA (29 CFR 516) + I-9 |
| OTAs y reseñas | 4 | 4 | D16: Google, TripAdvisor, Expedia |
| Categoría en estrellas | 3 | 3 | economy / midscale / upscale / luxury |
| Formatos de número con € | 282 | — | D13: `#,##0.00` |
| Hojas en A4 (paperSize 9) | 74 | — | D17: US Letter (paperSize 1) |

(Los destinos de las filas genéricas son los textos del kit base; en el hotel, «06 Christmas & NYE» = las filas 21-23
del B02, «patio season» no aplica: la terraza es la del 12 y la del 18, y las plataformas son Google, TripAdvisor y
Expedia.)

## 2. Qué cambia en cada libro además de la traducción (celdas exactas en `mapas_hotel.py`)

| Libro | Capas fijadas | ADAPTAR (traductor) |
|---|---|---|
| 01-05 F&B | CF de 11 hojas | higiene (2-303.11, 2-201.11, 100 °F), temperaturas 41 / 135 °F, parásitos 3-402.11, lavado 3-302.15, 9 alérgenos, buffet (3-306.11, 3-304.16, 3-306.13), sala 68–72 °F, sin vidrio en la piscina, alcohol 21+, date marking, etiqueta 3-602.11 |
| 06 Banquetes | CF | BEO: alergias, guarantee, precio por persona, aforo del salón |
| 07-08 Front desk y concierge | CF de 6 hojas | PMS US, walk the guest, ID + incidentals hold, ADR / RevPAR, reseñas Google · TripAdvisor · Expedia, sin estrellas |
| 09 Housekeeping | CF de 3 hojas | room attendant, botón de pánico donde la ley local lo exige, chinches, sangre y agujas (1910.1030), desinfectante EPA, DND + welfare check, 68–72 °F, par 3 |
| 10 Áreas públicas | — | ceniceros donde se permita fumar, sanitary receptacles, extintores (1910.157(e)(2)) |
| 11 Piscina | CF de 1 hoja | MAHC 2024: FC / pH / frecuencia / registro 3 años, «No Lifeguard on Duty», rescate, puerta de autocierre, HazCom, VGB |
| 12 Terraza | CF de 1 hoja | permiso de outdoor dining, ceniceros |
| 13 Mantenimiento | 23 filas de «Quarterly & Annual» (B y 6 cadencias), CF | ACS 140 °F, generador, extintores y standpipes, alumbrado de emergencia (NFPA 101), puertas cortafuegos (NFPA 80), EPA 608, legionela (ASHRAE 188 / CDC) |
| 14 Back office | fichajes del 14 B12 (= B16 del 03 del base) | FLSA + I-9, regla de la FTC sobre tarifas, MLOS / CTA / CTD, lote del procesador de tarjetas, overtime |
| 15 Spa | CF de 2 hojas | hot tub ≤ 104 °F y 3.0 ppm, cabina 75–79 °F, desinfectante EPA |
| 18 Rondas | cierre reordenado (45 celdas: B, C, D de 15 filas), 18 horas `hora_us` | el hotel no cierra: outlets y zonas públicas; persiana, reservas (OpenTable, Resy), BEOs |
| 19 Caja | la del base (47 + 15 fórmulas), 11 horas | las 7 del base |
| B01 · B02 | CF del B01; calendario: B, C, E de 24 filas | alergias; D de las 24 filas con la fecha US |

## 3. Jerga profesional

Sección «Hotel» de `../../GLOSARIO-JERGA-ES-EN.md` (17 filas, con estado y fuente): room attendant, executive
housekeeper, stayover / checkout, turndown, DND, OOO / OOS, linen par, front desk agent, night audit, shift log, walk the
guest, in-room dining, BEO, banquet captain, engineering / chief engineer / PM, MOD, pool shell / deck / backwash, free
chlorine y pool log, CPO, hot tub, treatment room, upscale / luxury, rate parity. Los puestos y zonas de celda entera
están en `mapas_hotel.GLOSARIO` (D8).

## 4. Regresión del código común (VPS, 27-oct-2026)

`gates_en.py` de `origin/main` frente al de la rama, sobre los 10 kits EN publicados (`dl/<slug>` de la rama), con
`--mes October`; gates (G1-G8) y `--autotest`. Script: el del scratchpad de la sesión (`regresion.sh`), salidas en
`/tmp/reg/` del VPS.

| Kit | Gates (viejo = nuevo) | Autotest (viejo = nuevo) |
|---|---|---|
| base (Restaurant) | idéntico · VERDE 8/0 | idéntico · OK 16/16 |
| bar | idéntico · VERDE 8/0 | idéntico · OK 16/16 |
| cafe | idéntico · ROJO 43 (deuda `adf52a52`, ya en `main`) | idéntico · FALLA (carpeta base no limpia) |
| catering | idéntico · VERDE 8/0 | idéntico · OK 20/20 |
| pizza | idéntico · ROJO 40 (deuda `adf52a52`) | idéntico · FALLA (carpeta base no limpia) |
| burger | idéntico · ROJO 36 (deuda `adf52a52`) | idéntico · FALLA (carpeta base no limpia) |
| ghost | idéntico · ROJO 40 (deuda `adf52a52`) | idéntico · FALLA (carpeta base no limpia) |
| icecream | idéntico · VERDE 8/0 | idéntico · OK 19/19 |
| chocolate | idéntico · VERDE 8/0 | idéntico · OK 19/19 |
| pastry | idéntico · VERDE 8/0 | idéntico · OK 20/20 |

Salidas idénticas byte a byte (`cmp`) en los 20 pares. Los xlsx publicados no se tocan: `aplicar_en.py` no cambia y, tras
las 40 ejecuciones, `git status` del worktree del VPS no muestra ningún cambio en `astro-site/public/dl/`. Los 4 ROJO son
la deuda conocida de los `VALORES_EN` del 05 «Daily Inventory» (`icecream/F2-NOTAS.md`), igual con el código viejo.

## 5. Prueba de humo F1 del hotel (VPS)

`aplicar_en.py --kit hotel --dry-run --parcial --textos <vacía> --mes October`: 19 libros en 11 s, `inject_cache` sin
fallos (197 fórmulas con valor), 0 desbordes, 938 cadenas con la marca de relleno, `--idempotencia` 0 diferencias. `gates_en.py --kit hotel --parcial`:
**VERDE 8/0**. `--autotest`: **19/19 CAZADOS**. `mapas_hotel.py`: autotest + `cruzar_censo` + `cruzar_base` con 0 errores.
