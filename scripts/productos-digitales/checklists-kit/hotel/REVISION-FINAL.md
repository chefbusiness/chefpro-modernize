# Hotel Checklists Kit Pro — revisión final adversarial (27-oct-2026 · sesión Claude Code)

Una pasada sobre `revision/dump_en.txt` (19 libros, 74 hojas) con dos lentes: **GM / director de operaciones de un hotel
US** y **técnica y normativa**. Una ronda de arreglos, solo de texto (`textos_en/G1.json` y `mapas_hotel.py`: `POR_CELDA`,
`NO_HEREDAR`, `REGLAS_US`). Filas, hojas, DV, CF y fórmulas sin tocar. **Código común intacto** (`kit.py`, `mapas.py`,
`aplicar_en.py`, `gates_en.py`): no hace falta repetir la regresión de los 10 kits.

**Recuento: 1 B · 3 M · 15 m (10 aplicados, 5 anotados sin aplicar); B y M aplicados todos.** Erratas del ES LIVE → `ERRATAS-ES.md`.

## Fuentes abiertas en esta revisión

- **CDC MAHC 2024, 5.ª ed.** (PDF de código, `cdc.gov/model-aquatic-health-code/media/pdfs/2024/11/5th-Ed-MAHC-Code-508.pdf`),
  leído en texto: §5.7.1.1.1 (filtración y recirculación «in continuous operation 24 hours per day»; la reducción de
  caudal solo con la piscina cerrada y manteniendo desinfectante y pH), §5.12.1.1 (spa: filtración 24 h salvo vaciado,
  llenado y mantenimiento), §5.12.1.2 (vaciado del spa: galones ÷ 3 ÷ usuarios al día), §6.6.3.1 (peligro inminente →
  cierre: cloro bajo el mínimo, pH < 6.5 o > 8.0, «failure to continuously operate the filtration and disinfection
  equipment»), §6.4.1.2.1 (registros 3 años), §5.7.3.1.1.2.3 (spa ≥ 3.0 ppm), §5.7.3.4.1 (pH 7.0–7.8), §5.7.5.5
  (alcalinidad semanal), §5.6.9.2 (sin vidrio), §6.4.2.2.3.4 («No Lifeguard on Duty», menores de 14 con adulto de 18+),
  §6.4.2.2.3.7 (carteles del spa: 104 °F, menores de 5, alcohol, embarazo y corazón), §5.7.4.7.2 (104 °F).
- **IFC Table 405.2** (simulacros): Group R-1 = «Quarterly on each shift», participan los empleados. Leída en la copia
  adoptada de New Jersey (`nj.gov/dca/divisions/dfs/pdf/fire_evac_drill_405_2.pdf`) y en la adopción de Washington
  (SBCC, WAC 51-54A); el texto ICC vigente es de pago (la tabla deja al fire code official modificarla).
- Sin reabrir (las leyó en primaria la F1, `SPEC.md` §3 y §R, y el texto del kit coincide con ellas): FDA Food Code 2022
  (5-202.12, 2-201.11, 3-402.11/12, 3-501.14, 3-501.17, 3-302.15, 2-102.12, 3-306.11, 3-304.16, 3-306.13), 29 CFR
  1910.157(e)(2)-(3), 1910.1030, 1910.1200, 29 CFR 516.5-516.6, 16 CFR Part 464 (12-may-2025), 40 CFR Part 82 (EPA 608),
  NFPA 101 §7.9.3, 15 U.S.C. 8003.

## Hallazgos

### Bloqueante

**B1 · 15 «Spa Closing» B7** — «Turn off saunas, steam room and hot tub». Leído al pie de la letra, el cierre apaga la
filtración y la desinfección del hot tub: el MAHC 2024 exige filtración 24 h en el spa (§5.12.1.1) y en toda la
recirculación (§5.7.1.1.1), y no tenerla en marcha es **peligro inminente con cierre inmediato** (§6.6.3.1, punto 7);
además el hot tub parado y caliente es caldo de legionela (el riesgo que el kit trata en el 13). Es la misma clase de
errata heredada del ES que la de la heladería.
**Arreglo:** «Turn off saunas and steam room; on the hot tub switch off only the jets and air blower: filtration,
circulation and disinfection keep running 24 hours a day (MAHC 2024 §5.12.1.1)». `REGLAS_US['spa_continuo']` nueva
(§5.7.1.1.1, §5.12.1.1, §5.12.1.2, §6.6.3.1) para que G7 la permita. **ES con la misma errata → `ERRATAS-ES.md` E1.**

### Mayores

**M1 · 13 «Quarterly & Annual» B27/F27** — simulacro «as often as your local fire code requires» con Frequency
**Annual**, y las Instructions (B15) dicen que esa columna «ya trae la periodicidad legal». En un hotel US (Group R-1) el
IFC pide simulacro del personal **trimestral en cada turno** (Table 405.2): un fire marshal lo cita.
**Arreglo:** B27 «Evacuation drill on every shift, with the emergency action plan reviewed: model fire codes require
hotels to drill staff quarterly on each shift (IFC Table 405.2, Group R-1); your local fire code governs» y **F27 =
Quarterly** (`_SERVICIOS_13[27]`). `REGLAS_US['simulacro']` nueva. El ES («anual») es correcto para España: sin errata.

**M2 · 15 «Spa Opening» B6 + «Instructions» B6** — «Check hot tub / **pool** temperature (target 95–100 °F…)»: la errata
del ES (`SPEC.md` §5, «piscina/jacuzzi 35-38 °C») seguía en el EN aunque la SPEC la daba por corregida; una piscina
climatizada a 95–100 °F es un error de operación (y de agua). Las Instructions prometían además que el 15 cubre «the
indoor heated pool», que no tiene ninguna tarea propia.
**Arreglo:** «Check hot tub (whirlpool spa) temperature (…)» y B6 de Instructions «Covers the hot tub (whirlpool spa),
sauna, steam room and treatment rooms; an indoor heated pool uses the pool checklists in file 11.» (recupera además las
«cabinas» del ES, que la traducción había perdido).

**M3 · 01 y 02 (buffets)** — la SPEC (D-HOT) y `REGLAS_US['buffet']` declaran sneeze guard (3-306.11), plato limpio en
cada vuelta (3-304.16) y buffet vigilado (3-306.13), pero **ninguna celda los decía**: son los tres puntos de buffet que
mira primero un inspector sanitario US, y la landing (F3) sale de esta SPEC.
**Arreglo (sin filas nuevas):** 01 «Breakfast Opening» B31 «…behind the sneeze guard (FDA 3-306.11)»; B48 «Keep the
buffet watched by trained staff and clean at all times (FDA 3-306.13)…»; 02 «Lunch Buffet» B15 «…sneeze guards in place
and a sign asking guests to take a clean plate on every trip (FDA 3-306.11, 3-304.16)». (La cena remite a «as at lunch».)

### Menores aplicados

| # | Libro · hoja · celda | Problema | Arreglo |
|---|---|---|---|
| m1 | 18 «Opening Rounds» A1 · «Closing Rounds» A1 | «— Full Hotel»: resto de la variante «Hotel Completo» (D2 la prohíbe) y contradice «outlets y zonas públicas» | «Opening / Closing Rounds — F&B Outlets & Public Areas» |
| m2 | 18 «Instructions» B37 · 19 «Instructions» B48 | «Order of use: shop → register … the shop file»: EN heredado de la heladería | `NO_HEREDAR` + «rounds → cash drawer … the rounds file» en G1 (heredado 107 → 106) |
| m3 | 13 «Instructions» B15 | «note the **part number**»: mala traducción de «nº de parte» (= nº de informe; la B36 ya dice «report number») | «note the report number» |
| m4 | 13 «Quarterly & Annual» B10 | «Renew food handler cards … Annual»: las tarjetas caducan según el estado (no cada año) | «Check food handler cards are current … (renew them when your state requires), refresh allergen training…» |
| m5 | 13 «Quarterly & Annual» B8 | «many brands require an annual audit» con Frequency Semiannual | «…require one or two a year» |
| m6 | 13 «Quarterly & Annual» B18 | vaciado «Annual» de piscina y spa sin decir que el hot tub se vacía mucho más a menudo | «…the hot tub itself is drained, scrubbed and refilled far more often (MAHC 2024 §5.12.1.2)» |
| m7 | 11 «Pool Opening» B6 | se mide cloro y pH pero no dice qué hacer fuera de rango (MAHC §6.6.3.1: cierre) | «…if a reading is out of range, keep the pool closed until it is corrected…» |
| m8 | 18 «Opening Rounds» C11, C13 | sistema de reservas del restaurante y reservas del outlet con zona «Front desk» (la «Recepción» del molde de restaurante) | «Host stand» (`POR_CELDA`; C20-C21, check-ins y lobby, siguen «Front desk») |
| m9 | B02 «F&B Calendar» D10, D18 | «Closed adult and kids menus» (calco de «menú cerrado»); «seatings closed early» | «Set adult and kids' menus, private room…»; «reservations by seating, booked well ahead,» |
| m10 | 09 «Deep Cleaning» B13 · 09 «Checkout Room Cleaning» B7 | «Polish floors (… carpet …)» (la moqueta no se pule); «strip … pillows» | «Polish hard floors (hardwood, marble) and shampoo or hot-water-extract carpet, per material»; «pillowcases and pillow protectors» |

### Menores anotados, sin aplicar (motivo)

| # | Dónde | Observación | Por qué no |
|---|---|---|---|
| n1 | 13 «Quarterly & Annual» C8, C11 | Área «Engineering» para la auditoría / ATP y la calibración de termómetros (en un hotel US es la cocina) | Columna de departamento orientativa, igual que el ES; cambiarla toca celdas de glosario por poco valor |
| n2 | 18 «Closing Rounds» D10 | «Empty trash cans…» asignado al MOD | Celda verde editable; las Instructions dicen que el MOD reparte; tocarla rompe el invariante declarado `_RESPONSABLE_CAMBIA` |
| n3 | 19 «Instructions» B14 | «change the label and value of each row» (UK/CA/AU): el valor está en la fórmula de subtotal | Texto común heredado del base, publicado en los 10 kits EN: no se toca en un vertical |
| n4 | 01 «Breakfast Opening» C41-C42 | Área «Admin» para temperatura de sala y hora de apertura | Igual que el ES y que los hermanos; sin daño |
| n5 | 13 «Quarterly & Annual» B14/F14 | «Domestic hot water: cleaning and disinfection … Semiannual»: la desinfección rutinaria del ACS no es práctica US habitual | El texto la ata al water management program (ASHRAE 188), que es quien fija la frecuencia |

## Comprobado y sin hallazgo

- **Lente GM:** jerga US correcta (room attendant, stayover / checkout, turndown, DND + welfare check, par 3, PMS,
  night audit, no-shows, walk the guest, BEO, guaranteed count, in-room dining, MOD, AM/PM/night audit 7-3-11); sin €,
  IVA, festivos españoles ni cargos españoles; sin restos de pizza, café, heladería o catering salvo m2 (ya arreglado).
- **18 reinterpretado como rondas:** orden de cierre coherente (outlet → patio y señalización → TPV → papeleras →
  check-outs con el night auditor → zonas públicas a modo noche con señales de salida encendidas → ventanas → HVAC → luz →
  seguridad → persiana → alarma → llave); horas de apertura 5:30-6:15 AM alineadas con el desayuno.
- **19 caja:** denominaciones US (rollos 25¢ = $10 y 10¢ = $5; el penny ya no se acuña pero es de curso legal),
  saldo inicial leído de `'Cash Drawer Opening'!C23`, over/short y registro mensual (media del fondo, over/short en valor
  absoluto). G5 = 204.91 / 4,200 / 0.
- **Fórmulas y citas:** los contadores restan la clave «Task» (CLAVES) y todas las pestañas y ficheros citados existen
  («Breakfast Opening», «Breakfast Closing», «Monthly PM», «Quarterly & Annual», «HR Operations», file 11, file 13).
- **Normativa:** °F del Food Code (41/135, 135→70 en 2 h y →41 en 4 h más, −4 °F 7 días / −31 °F, 100 °F en lavamanos,
  7 días de date marking contando el día de elaboración), 9 alérgenos, 21+, OSHA (1910.1030, HazCom, extintores
  mensual/anual), EPA 608, FLSA 2/3 años (NY 6), I-9, PCI DSS como norma del sector, FTC 16 CFR 464 desde el
  12-may-2025, MAHC (cloro, pH, 2/4 h, 3 años, carteles, vidrio, VGB), NFPA con «at the NFPA intervals» sin inventar
  cifras salvo el alumbrado de emergencia (NFPA 101 §7.9.3, 30 s / 90 min), ascensores y calderas «as your state or city
  requires».

## Gates tras la ronda (VPS `/root/wt-hotel`, comandos de `F2-NOTAS.md`)

| Paso | Resultado |
|---|---|
| `extraer_textos` · `mapas_hotel.py` · `heredar` | 1.236 cadenas, ids estables; mapas 0 errores (59 reglas); heredado 106, pendientes 832 (1 «corregida») |
| `aplicar_en --dry-run --idempotencia` y montaje | 19 xlsx, idempotencia **0 diferencias**, 0 desbordes, 0 rellenos, `inject_cache` 197/197 sin fallos de pycel |
| `gates_en` | **VERDE 8/0** (G4 regenerar 242 · traducir 1.059; G5 204.91 / 4,200 / 0; G7 48 °F y 48 citas, 83 permitidas) |
| `--autotest` | **19/19 CAZADOS** |
| `censo-entregables --fail` · no latinos | 0 defectos · 19 ficheros, 0 con no latinos |
| Copia al Mac | 19 xlsx + `dump_en.txt` + `textos_es.json` + `heredado.json` + `pendientes.json`; hash agregado sha256 idéntico VPS ↔ Mac (`aa01851fd97a6028`) |
| Volcado | `revision/dump_en.txt` re-volcado (4.391 líneas); su diff = exactamente las celdas de esta tabla |
