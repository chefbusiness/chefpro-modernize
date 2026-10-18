# Pizza Shop Checklists Kit Pro — SPEC DELTA (F1 · 18-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas para Pizzería** (`kit-tareas-pizzeria`, 11 xlsx v2.0). Cuarto
> hermano vertical del Restaurant Checklists Kit Pro, hecho como el bar, la cafetería y el catering: **lo que no está
> aquí es la SPEC base** (`../SPEC.md` §0-§9). Mapas: `mapas_pizza.py` (importa `../mapas.py`). Tamaño S. 46 hojas.

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `pizza-shop-checklist-templates` → `/en/digital-products/pizza-shop-checklist-templates` (+ `/access`, `/library`); productId = slug; JWT `pizza-shop-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_PIZZA_SHOP_CHECKLISTS_KIT`; ficheros en `dl/pizza-shop-checklist-templates/` |
| D2 | Nombre | **Pizza Shop Checklists Kit Pro**; title SEO = H1: «Pizza Shop Checklists Kit Pro: Pizzeria Opening & Closing Checklist Templates for Excel». Sin el sufijo «— Pizzería» |
| D3-D4 | Precio | **$19 USD**, pago único; sin `priceOld`, «% off» ni anclas |
| D5 | Ficheros | §2. Sin volumen US medido en «pizza shop / pizzeria checklist»: los ficheros usan los dos términos y la landing (F3) se apoya en la intención genérica «restaurant opening / closing checklist» (nunca en los xlsx: G2 la veta) |
| D6 | Pestañas | Estructura del base sin barra. Nuevas: **Pizza Oven Station** · **Make Line** · **Apps & Pasta** (sin coma: la coma rompe el área de impresión) · Pizza Maker · Line Cook · Shift Manager · Delivery Driver · Daily Inventory · **Game Night** · Holiday Season · Pizza Shop Opening / Closing. El resto, del base |
| D8 | Glosario | base + 30 celdas (4 sobrescriben el base: Auxiliar → **Dishwasher / prep**, Jefe de Cocina → Kitchen manager, Recepción → Front counter, Responsable de caja → Cashier / shift manager): Pizzero → Pizza maker, Repartidor → Delivery driver, Encargado/a → **Shift manager** (nunca «shift lead»), Horno → Oven, fechas y estaciones; unidades kg / g / L / ml / uds / manojos → lb / oz / qt / fl oz / ea / bunches |
| D9 | Horas | 177 horas de 24 h → `hora_us` (8 fijadas en `POR_CELDA` por el orden del 01 «FOH Closing») |
| D10 | Orden | **Errata ES corregida**: 01 «FOH Closing» (alarma y luces antes que los baños: los baños suben a «Delivery, Register & Restrooms» y la sección final es «Lock-Up») y 08 «Pizza Shop Closing» (el horno de leña se apagaba DESPUÉS de la alarma y la llave: 14 filas reordenadas, horno a enfriar al principio, alarma → puertas → llave al final) |
| D11 | 05 «Quarterly & Annual» | plagas (heredada), campana + conducto + chimenea NFPA 96 (combustible sólido: inspección **mensual** en «Monthly Maintenance», limpieza al haber depósitos), revisión del horno de leña, extintores OSHA 1910.157 + extinción, prueba hidrostática (Class K y CO2 cada 5 años), gas, frío EPA 608 (con la make line), legionela, agua (Consumer Confidence Report o pozo), aceite usado, seguros (+ liquor liability y hired & non-owned auto), POS / sales tax + apps. 03 `B9` = fichajes FLSA (B16 del base) |
| D12 | Caja | 09 igual que el base (53 `POR_CELDA` y 6 `ADAPTAR` heredados tras `cruzar_base`) |
| D14 | Calendario | Misma estructura que el base (filas 5-26), con los días fuertes de una pizza shop US: Reyes → **Super Bowl** · Día del Padre → St. Patrick's + **March Madness** · Semana Santa → **Lent Fridays** (meatless) + Easter · 1 de mayo → **NBA & NHL playoffs** · San Juan → Father's Day con las tareas del ES · vuelta al cole → + football season · Halloween de delivery · Todos los Santos → **Thanksgiving Eve** · cenas de empresa → office orders · NYE sin uvas ni cava; orden cronológico |
| D-PIZ | Horno | wood-fired / deck oven, peel, cutter, dough cutter; 400-450 °C = **750–840 °F**, 300 °C = **570 °F**; precalentado, enfriado y campana según el fabricante (45-60 min / 1 h del ES como referencia); leña lejos de la boca; **ceniza en frío a un contenedor metálico con tapa** (NFPA 96, solid fuel cooking) |
| D-PIZ | Masa · make line · queso | cold fermentation a **41 °F o menos**, dough boxes tapadas con fecha (y hora), plazo de la receta (la masa cruda no es TCS: criterio del kit); make line ≤ 41 °F; mozzarella TCS, abierta con date marking 7 días (3-501.17(B)); carne cruda separada (3-302.11); descongelar en cámara (3-501.13) |
| D-PIZ | Lecciones de los hermanos | tiras de sanitizante en 4 tareas diarias (amasado, mesas, make line, tablas) · 3-501.19 bien dicho en la pizza by the slice (a las 4 h se tira) · enfriar 135 → 70 °F en 2 h y → 41 °F en 4 h más (salsa casera, pre-elaboraciones) · recalentar a 165 °F en 2 h · aviso al consumidor (carbonara y tiramisú con huevo crudo) · date marking (mozzarella, fiambres, postres) · `TERMINOS_PROHIBIDOS` (restaurant, shift lead, busser, barista, cafe salvo «sidewalk cafe», venue, BEO…) · CF `$F5="✓"` sin cabeceras internas (no aplica la de catering) |
| D-PIZ | Delivery | apps US (DoorDash, Uber Eats, Grubhub); bolsa térmica: caliente ≥ 135 °F, frío aparte ≤ 41 °F; objetivo < 30 min del ES; coche propio: carnet y seguro (el personal puede excluir el reparto); propinas del repartidor = suyas (FLSA 203(m)(2)(B)) |
| D-PIZ | Alérgenos · alcohol | los 9 de EE. UU.: el **trigo** sí, el gluten en sí no; la lactosa es intolerancia (se recoge igual); UK: 14. Cerveza / vino / prosecco solo con licencia, 21+ con ID; regalarlo, según el estado |
| D-UK | UK | 14 alérgenos en las celdas de alérgenos; nota UK del B02 heredada; 8 °C / 63 °C en la FAQ de la landing |

## 2. Ficheros (D5)

| # | Fichero EN | Título EN |
|---|---|---|
| 01 | `01-pizza-shop-opening-closing-checklists.xlsx` | Pizza Shop Opening & Closing Checklists: Kitchen, FOH & Delivery |
| 02 | `02-pizza-kitchen-station-checklists.xlsx` | Pizza Kitchen Station Checklists: Pizza Oven, Make Line, Apps & Pasta |
| 03 | `03-pizzeria-manager-checklist.xlsx` | Pizzeria Manager Checklist: Daily, Weekly, Monthly & Shift Handover |
| 04 | `04-pizza-shop-duties-by-role.xlsx` | Pizza Shop Duties by Role: Pizza Maker, Line Cook, Shift Manager, Server & Driver |
| 05 | `05-pizzeria-cleaning-checklist-inventory-maintenance.xlsx` | Pizzeria Cleaning Checklist, Inventory & Maintenance Schedule |
| 06 | `06-pizza-shop-event-checklists.xlsx` | Pizza Shop Event Checklists: Game Night, Valentine's Day, Holidays & Patio |
| 07 | `07-blank-pizza-shop-checklist-template.xlsx` | Blank Pizza Shop Checklist Template (Editable) |
| 08 | `08-pizzeria-opening-closing-checklist.xlsx` | Pizzeria Opening & Closing Checklist (Whole Shop) |
| 09 | `09-cash-drawer-opening-closing.xlsx` | Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log |
| B01 | `BONUS-01-pizza-shop-pre-shift-meeting-template.xlsx` | BONUS: Pizza Shop Pre-Shift Meeting Template (Huddle Notes) |
| B02 | `BONUS-02-pizza-shop-holiday-calendar.xlsx` | BONUS: Pizza Shop Holiday & Busy Days Calendar (US) |

## 3. Reglas del delta (`mapas_pizza.REGLAS_US` = las del base + estas)

| Concepto | Fuente |
|---|---|
| Make line, mozzarella, bolsa caliente / fría (41 / 135 °F); date marking 7 días desde la apertura | FDA Food Code 2022 §3-501.16, §3-501.17(B) |
| Descongelar · carne cruda separada · pizza by the slice (4 h y se tira) | §3-501.13; §3-302.11; §3-501.19(B) |
| Ceniza en metálico con tapa · extracción de combustible sólido mensual | NFPA 96 cap. 14; NFPA 96 tabla 11.4 (base) |
| Propinas del repartidor · edad 21 · regalar alcohol | 29 U.S.C. 203(m)(2)(B); 23 U.S.C. 158; [estatal] ABC |
| Agua · alérgenos (trigo sí, gluten no) | 40 CFR Part 141 Subpart O; FALCPA + FASTER Act |
| Masa en frío (no TCS) · 750–840 / 570 °F · días fuertes · seguro de reparto · inventario kg → lb | [criterio del kit]; [fabricante] |

°F que el kit puede afirmar (G7, `GRADOS_F_SPEC`): −31, −4, 0, 32, 41, 70, 100, 135, 165, 570, 750, 840.

## 4. Memoria de traducción (`../heredar.py --kit pizza`, `MEMORIA`: base, bar, cafetería y catering)

909 cadenas; GM 278 (pestañas, glosario, horas, `POR_CELDA`, 32 `VALORES_EN`, marca, versión). De las 631 a traducir:
**250 heredadas** (247 exactas + 3 por sufijo; 197 del base, 50 de la cafetería, 3 del bar; 2.110 palabras) y **381
pendientes** (360 nuevas, 10 «contexto», 10 con otro ADAPTAR, 1 `NO_HEREDAR`; **2.565 palabras**; 86 cadenas con ADAPTAR)
en `textos_en/pendientes.json` → UN traductor sonnet → `textos_en/G1.json`.

    python3 extraer_textos.py --kit pizza && python3 pizza/mapas_pizza.py && python3 heredar.py --kit pizza
    python3 aplicar_en.py --kit pizza --dry-run [--parcial] --idempotencia --mes October
    python3 gates_en.py --kit pizza [--parcial] --dir <carpeta> [--autotest]

## 5. Erratas del ES (para su próxima v2.x; la EN nace corregida)

- 01 «Cierre Sala»: «Activar alarma y cerrar» (B19) antes que la limpieza de baños (B21-B22).
- 08 «Cierre del Negocio»: «Apagar horno de leña» (B18) DESPUÉS de activar la alarma y cerrar con llave.
- 05 «Inventario Diario» D6:D42: los mínimos son TEXTO y la fórmula pide siempre (como en la cafetería); A46: marca con
  otro formato. 05 «Instrucciones» B24 promete hojas protegidas y el inventario no lo está.
- 01 «Cierre Cocina» B13: «retirar ceniza cuando esté frío» a la hora del cierre (un horno de leña no se enfría en
  30 min). 05 «Trimestral» B15: «el agua es el 60 % de la masa» confunde la hidratación (60 % del peso de la harina).
