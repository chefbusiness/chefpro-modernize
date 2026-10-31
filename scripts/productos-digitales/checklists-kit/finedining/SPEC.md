# Fine Dining Checklists Kit Pro — SPEC DELTA (F1 · 31-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas Recurrentes: Restaurante Creativo / De Autor**
> (`kit-tareas-restaurante-creativo`, 13 xlsx **v2.0**). Decimoquinto hermano: **lo que no está aquí es la SPEC base**
> (`../SPEC.md` §0-§9) y el hotel (`../hotel/SPEC.md`, mismo molde híbrido). Mapas: `mapas_finedining.py`. Tamaño S, $19.

## 0. Molde (medido en el censo): HÍBRIDO, como la heladería y el hotel

| Libros | Molde |
|---|---|
| 01-09, B01, B02 (49 hojas en total con 10 y 11) | **ligero**: # · Tarea · Zona · Responsable · ✓ · Hora · Notas, cabeceras internas por sección (21 hojas con la cabecera dentro del rango de CF → `CF_POR_CELDA`, como el hotel), contadores que restan «Tarea» (`CLAVES['Tarea']`), sin protección, subtítulo A2 en vez de línea de marca (`LIBROS_SIN_MARCA`), sin horas ni responsables precargados; 05 «Trimestral y Anual» con F = Cadencia; tabla de vida útil en congelación al pie de 05 «Semanales» |
| 10, 11 | el **08 y el 09 del kit base** con la variante «Restaurante Creativo» (protegidos; horas en el 10 y el 11 «Apertura de Caja»; la tabla de billetes 27-42 y el registro mensual del 09): POR_CELDA y ADAPTAR del 09 heredados con la clave renumerada, el ADAPTAR del 08 B8 en el 10 (`cruzar_base`: mismo texto ES y mismas fórmulas de caja) |
| B02 | calendario propio: A mes · B acciones / fechas · C producto estrella · D demanda · E ✓ · F notas (12 filas, 5-16) |

**Tareas: 486** (01 55 · 02 63 · 03 50 · 04 60 · 05 63 · 06 32 · 07 44 · 08 34 · 09 9 · 10 33 · 11 23 · B01 20). Código
común tocado: **ninguno** (el hotel ya dejó los ganchos: `N_LIBROS`, `HOJA_CAJA` del 11, `HOJA_HORAS`, `HOJA_VERDE`).

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `fine-dining-checklist-templates` (libre) → `/en/digital-products/fine-dining-checklist-templates`; JWT `…-jwt`; env `VITE_STRIPE_PAYMENT_LINK_FINE_DINING_CHECKLISTS_KIT`; familia `kit-tareas-restaurante-creativo` |
| D2 | Nombre y title | **Fine Dining Checklists Kit Pro**; title SEO = H1: «Fine Dining Checklists Kit Pro: **Tasting Menu, Brigade & Chef's Table** Checklist Templates for Excel». DataForSEO US (31-oct): fine dining restaurant **135.000**, fine dining **74.000**, chef's table **33.100**, tasting menu **8.100**, kitchen brigade 2.900, fine dining steps of service 210; fine dining checklist / service checklist / sommelier checklist sin volumen. Se descartó `fine-dining-restaurant-checklist-templates` (más largo, misma intención) |
| D3-D4 | Precio | **$19 USD** (v2.0), pago único, sin anclas |
| D6 | Pestañas | AM Opening · PM Closing · Long-Lead / Mid-Lead / Same-Day Prep · Plating Bible · R&D Sessions · Recipe Documentation · Executive Chef · Sous Chef · Hot Line · Garde Manger · Pastry Chef · Sommelier · Maître & Dining Room (sin apóstrofo en la pestaña) · Weekly · Monthly · Quarterly & Annual · Tasting Menu Pairing · Wine Cellar · Chef's Table · Pop-Ups · Special Dinners · Food Photography · Social Media · Press & Guides · Template A/B/C · Restaurant Opening / Closing · Cash Drawer Opening / Closing · Monthly Cash Log · Pre-Shift Meeting · Annual Calendar |
| D7 | CF | `CF_POR_CELDA` en 21 hojas (`AND($E6="✓",$B6<>"Task")`), desviación declarada como el hotel; el resto idéntico |
| D8 | Jerga | Brigada US: **executive chef**, **chef de cuisine**, **sous chef**, **chef de partie**, **garde manger** (partida fría), hot line, **pastry chef**, **sommelier**, **maître d'**; sala: **dining room** (Sala sobrescribe «FOH»), **captain**, **server**, **back server**, **food runner**, **expo / the pass**; I+D → **R&D**; menú degustación → **tasting menu**, pase → **course**; Roner → **immersion circulator**; sifón → whipping siphon; microbrotes → microgreens; maduración → **dry aging**; escandallo → plate cost |
| D9 | Horas | Las de celda del 10 y el 11 → `hora_us` (sin desplazar); las de los textos, el traductor |
| D10 | Seguridad (FDA Food Code 2022) | Frío 41 °F / 0 °F (3-501.16); **pescado crudo**: parásitos 3-402.11 + registro 3-402.12 + **aviso al consumidor 3-603.11** (sustituye a la congelación UE de anisakis; el ácido del ceviche no la sustituye); huevo sous vide 63 °C → **145 °F** (3-401.11); **sous vide / ROP con almacenaje: HACCP plan o variance** (3-502.11 / 3-502.12); enfriado 3-501.14; date marking 7 días (3-501.17); lavado de microbrotes 3-302.15 (sin «lejía 70 ppm»); higiene 2-303.11, 2-201.11, 5-202.12; CFPM (2-102.12); 9 alérgenos con sésamo + aviso escrito 3-602.12(C) (UK 14) |
| D11 | 05 «Trimestral y Anual» | 19 filas por `POR_CELDA` (como el 13 del hotel): plagas, campana NFPA 96, auditoría opcional, plan HACCP / variance, food handler cards + CFPM, permiso sanitario (sous vide, curado y dry aging pueden pedir variance), gas, frío EPA 608, sondas a 32 °F, aceite usado, extintores OSHA + extinción NFPA 96, alarma NFPA 72 y luces NFPA 101, legionela ASHRAE 188 solo si aplica, eléctrica NFPA 70B, plan de emergencia, seguros, fichajes FLSA + I-9, POS / sales tax / PCI DSS, permisos y licencias; 4 filas al traductor (calibración de básculas, SAT, escandallos, nº de parte) |
| D12 | Caja y cierre | 10 «Cierre del Negocio» reordenado (errata §5). El 11 = el 09 del base: billetes y monedas US, propinas fuera de ventas, OVER / SHORT (POR_CELDA y ADAPTAR heredados) |
| D13 | Personal | Fichajes FLSA (2 / 3 años; NY 6) en vez del «registro de jornada 4 años»; propinas por tip pool sin managers (29 U.S.C. 203(m)(2)(B)); **service charge ≠ propina** (IRS Rev. Rul. 2012-18); IVA → sales tax |
| D14 | Calendario | B02: A y D por glosario; B y C traductor con ADAPTAR: Easter / Passover, graduaciones y bodas (no comuniones), Mother's Day 2.º domingo de mayo, Father's Day 3.er domingo de junio, Jul 4, Labor Day, Thanksgiving, holiday parties, Christmas Eve, NYE (brindis 21+); sin Reyes, Día del Padre en marzo, Asunción, Todos los Santos ni puente de diciembre |
| D-ALC | Alcohol | Con la licencia del local y 21+ con ID (23 U.S.C. 158); maridaje sin alcohol se queda |
| D-GUIAS | Guías | Michelin Guide (en sus ciudades), World's / North America's 50 Best, OAD, James Beard Awards; sin Repsol |
| D-LEX | Prohibidos | hotel (salvo «hotel pan»), housekeeping, front desk, room attendant, ice cream / pastry / chocolate shop, scooper, dipping cabinet, bakery case, food truck, commissary, plancha, workshop, obrador, casual dining |
| D-UK | UK | 14 alérgenos y 8 °C / 63 °C solo en la FAQ de la landing |

## 2. Ficheros (D5)

| # | Fichero ES | Fichero EN |
|---|---|---|
| 01 | `01-apertura-cierre.xlsx` | `01-fine-dining-opening-closing-checklist.xlsx` |
| 02 | `02-mise-en-place-degustacion.xlsx` | `02-tasting-menu-mise-en-place-checklist.xlsx` |
| 03 | `03-id-desarrollo-menu.xlsx` | `03-menu-development-rd-checklist.xlsx` |
| 04 | `04-tareas-brigada-creativa.xlsx` | `04-kitchen-brigade-duties-by-role.xlsx` |
| 05 | `05-tareas-semanales-mensuales.xlsx` | `05-fine-dining-weekly-monthly-maintenance-checklist.xlsx` |
| 06 | `06-sumiller-maridajes.xlsx` | `06-sommelier-wine-pairing-checklist.xlsx` |
| 07 | `07-chefs-table-eventos.xlsx` | `07-chefs-table-special-events-checklist.xlsx` |
| 08 | `08-fotografia-storytelling.xlsx` | `08-food-photography-social-media-press-checklist.xlsx` |
| 09 | `09-plantilla-personalizable.xlsx` | `09-blank-fine-dining-checklist-template.xlsx` |
| 10 | `10-apertura-cierre-negocio.xlsx` | `10-restaurant-opening-closing-checklist.xlsx` |
| 11 | `11-apertura-cierre-caja.xlsx` | `11-cash-drawer-opening-closing.xlsx` |
| B01 | `BONUS-01-briefing-servicio.xlsx` | `BONUS-01-fine-dining-pre-shift-meeting-template.xlsx` |
| B02 | `BONUS-02-calendario-anual.xlsx` | `BONUS-02-fine-dining-annual-calendar.xlsx` |

## 3. Reglas del delta (`REGLAS_US` = base + 14; 44 en total)

Huevo 145 °F (3-401.11(A)(1), 3-603.11) · sous vide / ROP con HACCP o variance (3-502.11, 3-502.12) · CFPM (2-102.12) ·
aviso escrito de alérgenos (3-602.12(C)) · 21+ (23 U.S.C. 158) y licencia [estatal] · tip pool (29 U.S.C. 203(m)(2)(B)) ·
service charge (IRS Rev. Rul. 2012-18) · NFPA 72 y NFPA 101 §7.9.3 · NFPA 70B · ASHRAE 188 · calibración 32 °F ·
guías y calendario [criterio del kit]. °F permitidos (G7): −31, −4, 0, 32, 41, 70, 100, 135, 145, 165.

## 4. Memoria de traducción (`MEMORIA`: base, hotel, heladería, catering, chocolatería, pastelería)

**1.006 cadenas** (2.309 apariciones); **GM 207**. De las **799 a traducir: 115 heredadas** (102 del base, 11 del hotel,
2 de la chocolatería; 1.166 palabras; la firma de autor incluida) y **684 pendientes** (679 nuevas, 4 «adaptar», 1
«contexto»; **5.788 palabras**; 45 ADAPTAR): G1 395 / 3.257 (01-05 + comunes) y G2 289 / 2.531 (06-B02). Más de 3.000
palabras → **un traductor sonnet** (como la taquería) → `textos_en/G1.json` con los 684 ids.

## 5. Erratas del ES (para su v2.x; la EN nace corregida)

- **10 «Cierre del Negocio»**: «Retirar decoración fresca de mesas» (B18) y «Actualizar carta de vinos» (B19) van DESPUÉS
  de «Activar alarma» (B16) y «Cerrar con llave» (B17), y las persianas (B9) se cierran antes de recoger la señalización
  (B12). La EN reordena las mismas 15 filas (`POR_CELDA` B5:D19, `_CIERRE_10`) con persiana, alarma y llave al final; la
  decoración y la carta de vinos pasan del «Último en salir» al encargado.
- 03 «Sesiones I+D» B22: «alérgenos comunes (14 UE)» — son los de declaración obligatoria, no los «comunes».
- Revisado y NO es errata (es correcto en España, la EN lo adapta): pescado «cocinado por encima de 60 °C» (anisakis),
  gas y eléctrica «cada 5 años», «lejía 70 ppm» para vegetales crudos, Día de la Madre el 1.er domingo de mayo.
