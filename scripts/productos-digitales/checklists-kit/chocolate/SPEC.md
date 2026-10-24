# Chocolate Shop Checklists Kit Pro — SPEC DELTA (F1 · 24-oct-2026 · sesión Claude Code)

> Edición EN (US con notas UK) del **Kit de Tareas Chocolatería** (`kit-tareas-chocolateria`, 11 xlsx v2.1, 338 tareas).
> Octavo hermano vertical (tras el bar, la cafetería, el catering, la pizzería, la hamburguesería, la ghost kitchen y la
> heladería): **lo que no está aquí es la SPEC base** (`../SPEC.md` §0-§9). Mapas: `mapas_chocolate.py` (importa
> `../mapas.py`). Tamaño S. 37 hojas. **Molde híbrido, como la heladería** (censo): el 01-07, el B01 y el B02 van en el
> molde ligero del catering (# · Tarea · Zona · Responsable · ✓ · Hora · Notas, cabeceras internas por sección, sin
> protección, subtítulo A2); el 08 y el 09, en el del kit base. **El 09 no es idéntico al base**: la venta al peso añade
> 2 tareas a la apertura y 2 al cierre, y el fondo y la tabla de caja bajan 2 filas (D12).

## 1. Decisiones del delta

| D | Tema | Decisión |
|---|---|---|
| D1 | Slug | `chocolate-shop-checklist-templates` → `/en/digital-products/chocolate-shop-checklist-templates` (+ `/access`, `/library`); productId = slug; JWT `chocolate-shop-checklist-templates-jwt`; env `VITE_STRIPE_PAYMENT_LINK_CHOCOLATE_SHOP_CHECKLISTS_KIT`; ficheros en `dl/chocolate-shop-checklist-templates/` |
| D2 | Nombre | **Chocolate Shop Checklists Kit Pro**; title SEO = H1: «Chocolate Shop Checklists Kit Pro: Opening, Closing & Tempering Templates» (73). Sin el sufijo «— Chocolatería / Bombonería». El subtítulo A2 («Kit de Tareas: Chocolatería / Obrador de Chocolate») va por `GLOSARIO` con el nombre EN. Versión EN **2.1** en los 11 libros (`VERSION_ES`; el ES mezcla 2.1 y 2.0) |
| D3-D4 | Precio | **$19 USD**, pago único; sin `priceOld`, «% off» ni anclas («One-time payment · lifetime access · updates included») |
| D5 | Ficheros | §2. Demanda US (§R): chocolate shop 49.500/mes (local) · bonbons 90.500 · chocolatier 27.100 · chocolate truffles 27.100 · chocolate tempering 9.900 · chocolate molds 9.900 · chocolate store 9.900; las variantes con «checklist» sin volumen, como en los hermanos |
| D6 | Pestañas | Opening · Closing · **Tempering** · **Molding & Bars** · Daily / Weekly / Monthly Tasks · **Chocolatier** · **Sales Associate** · **Shift Lead** · Weekly / Monthly Tasks (05) · Quarterly & Annual · **Holiday Season** · Valentine's Day · **Easter** · By Area / By Shift / By Role · **Shop Opening / Shop Closing** · cash del base · Pre-Shift Meeting · **Holiday Calendar**. «Semanal» y «Mensual» salen en el 03 y el 05: el mismo EN en los dos (únicas por libro) |
| D7 | CF | Desviación declarada (la del catering y la heladería): en 17 hojas del molde ligero la CF de «hecho» pasa de `$E6="✓"` a `AND($E6="✓",$B6<>"Task")` (`CF_POR_CELDA`); el 07 no. `CLAVES` + «Tarea» → «Task» |
| D8 | Glosario | base + 26 celdas (3 sobrescriben el base: Sala → **Shop floor**, Encargado → **Shift lead**, Responsable de caja → **Cashier / shift lead**; y la tabla del 02: Familia → **Product type**, Vida útil → **Shelf life**): Obrador → **Kitchen** · Templado → Tempering · Moldeado → Molding · Conservación → **Cool room** · Cámara → **Fridge** · Vitrina → **Display case** · Tienda → Shop · Mostrador → Counter · Envasado → **Wrapping** · Almacén → **Dry storage** · Gestión → Management · Producción → Production · RRSS → Social media |
| D9 | Horas | Las 30 horas de 24 h (08 E5-E21, 09 D5-D17) **+2 h** (07:00 → 9:00 AM; tienda a las 10 AM): la chocolate shop US abre la tienda a media mañana y la producción empieza antes, en el 01 [criterio del kit]; mismo orden e intervalos (`HORAS_ES`; el autotest comprueba +2 h y orden). El 01-07 no trae horas |
| D10 | Orden y erratas | **Errata ES corregida** (§5): 08 «Shop Closing», 15 filas reordenadas: clientes y música → patio y señalización → **vitrinas apagadas con el género ya en la cool room y temperatura de cierre del obrador** → caja → papeleras y seguridad («never the cool room or the fridges») → el local (HVAC: «keep the shop below 68 °F if any chocolate stays out») → alarma, puertas y llave. Cambian 4 responsables (vitrinas y temperatura → Shift lead; alarma y persianas → Last one out). Gas: en EE. UU. la llave general no se abre ni se cierra a diario (01 «Opening» B12, «Closing» B25, «Instructions» B15) |
| D11 | 05 «Quarterly & Annual» | plagas (mensual, licensed operator), extracción (NFPA 96 **solo si se cocina con grasa bajo campana**), **análisis de actividad de agua (aw)** de ganaches y rellenos nuevos (vida útil y si son TCS), food handler cards + CFPM (2-102.12), servicio técnico de temperadora y **bombo (panning machine)**, frío EPA 608 (cool room, neveras, vitrinas), calibración (32 °F) y báscula **legal-for-trade**, extintores OSHA 1910.157 + hidrostática, gas «per local code», seguros (product liability, business interruption, equipment breakdown con spoilage), **health permit + licencia estatal de fabricación si la piden** (caramelos, mayorista, venta por correo), POS + sales tax (**muchos estados gravan el candy**). Sin DDD, BIE, legionela, RGSEAA ni Verifactu. 03 «Mensual» B16 = fichajes FLSA (B16 del base) |
| D12 | Caja | 09 del base **desplazado**: fondo B23 → **B25**; tabla de billetes y resumen, filas 24-54 → **26-56** (`_mover`, `DENOMINACIONES` y `FORMULAS_POR_CELDA` recalculados). G5 con `CASOS_G5` (el caso de SPEC §5 del base en las celdas nuevas: 204.91; 4,200 y 0) y `CELDA_CACHE_MAL` = C52: `gates_en.caso_caja` tiene fijas las celdas del base y **no se toca código común**. Las 4 tareas propias (báscula, precio por libra, venta al peso, señales) van al traductor con ADAPTAR |
| D13 | Moneda | 282 formatos con € → `#,##0.00` (base) |
| D14 | Calendario | 12 meses (filas 5-16: A mes · B acciones · C productos · D temporada): A, C y D fijados; B = traductor con ADAPTAR por mes, en orden. Temporada US: **Peak** febrero y diciembre · **High** marzo-mayo y noviembre · **Medium** junio, septiembre, octubre · **Low** enero, julio, agosto (calor: envíos con cold packs). Valentine's (fecha límite el 10) · St. Patrick's · Easter (variable) · Mother's Day (2.º domingo de mayo) + **Teacher Appreciation Week** + graduaciones · Father's Day + bodas · 4 de julio · Labor Day + corporate gifting · Halloween + **Sweetest Day** + National Chocolate Day · Thanksgiving + Small Business Saturday · Christmas + **Hanukkah (gelt)** + shipping cutoff. Sin Reyes, turrón, monas, comuniones, panellets, Asunción ni alcohol |
| D-CHOC | Temperaturas | obrador **64–68 °F** · cool room **59–64 °F** y 50–60 % · vitrina **60–64 °F** y < 55 % · tienda 68–72 °F · por encima de 68 °F funde la manteca de cacao · moldes 68–72 °F · enfriado 54–57 °F · reparto < 64 °F [criterio del kit, cifras del ES en °F]. Templado (negro 122–131 → 81–82 → 88–90 °F; leche 113–122 → 79–81 → 84–86; blanco 104–113 → 77–79 → 82–84; temperadora a 113 °F) = cifras del kit y **«manda la curva del fabricante de tu cobertura»** [fabricante] |
| D-CHOC | Ganache TCS | la ganache de nata fresca y los rellenos con aw alta son **TCS salvo análisis de laboratorio**: nevera a 41 °F o menos y **date marking 7 días** (3-501.17); el ES daba 10-15 días: C41 = «7 days at 41 °F», D41 «longer only with a lab water-activity test»; 4-8 semanas (UHT, sorbato, alcohol) solo con aw comprobada; granel de ganache congelado a 0 °F; el chocolate acabado no se congela. Sin enfriado (3-501.14), recalentado ni mantenimiento en caliente: no aplican |
| D-CHOC | Alérgenos y etiqueta | los 9 de EE. UU. (soja = también la lecitina; «wheat», no «gluten»; sulfitos fuera, en el cartel si la fruta los lleva); **vitrina: aviso escrito de alérgenos de lo no envasado** (FDA Food Code 2022 3-602.12(C), donde se haya adoptado); «may contain» voluntario y veraz; **lo envasado en la tienda**: nombre, ingredientes, contenido neto (oz y g), alérgenos y negocio (3-602.11); lote y best-by = criterio del kit (la fecha es voluntaria salvo la fórmula infantil); sin mano desnuda en bombones, trufas y muestras (3-301.11) |
| D-CHOC | Venta al peso | precio por **libra**; báscula **legal-for-trade** (NTEP) revisada por pesas y medidas del estado; señales → **deposits** de los pre-orders, no son venta del día |
| D-CHOC | Lecciones de los hermanos | tiras de sanitizante en 7 tareas (mostrador al cerrar, mármol ×2, superficies de envasado, zona de degustación, mostrador del dependiente; 4-501.114) · sin enfriado/recalentado (fuera de `REGLAS_US`: G7 caza 135, 165, 70 o −31 °F) · CF sin cabeceras internas · `AJUSTE_MAQUETA_ES` · calendario cronológico · «2 weeks out» · `TERMINOS_PROHIBIDOS` (bartender, cocktails, beer, liquor, barista, espresso, cafe, dining room, server, waitstaff, head / sous chef, line / prep cook, MOD, FOH, BEO, banquet, venue, line-up, pizza, dough, burger, ghost kitchen, packer, app manager, ice cream, gelato, scooper, dipping cabinet, batch freezer, dipper well, «restaurant» salvo consultant / supply; permitidos: liqueur, hot chocolate, coffee como sabor, patio, kitchen). **Sin inventario con mínimos** en este ES: `VALORES_EN` vacío y la deuda de `adf52a52` no aplica |
| D-UK | UK | nota UK en el B02 (Mothering Sunday, bank holidays, Boxing Day); 14 alérgenos en las celdas de alérgenos; 18 °C y humedad en la FAQ de la landing (F3) |

## 2. Ficheros (D5)

| # | Fichero ES | Fichero EN | Título EN |
|---|---|---|---|
| 01 | `01-apertura-cierre.xlsx` | `01-chocolate-shop-opening-closing-checklists.xlsx` | Chocolate Shop Opening & Closing Checklists: Kitchen, Display Case & Counter |
| 02 | `02-partidas-produccion.xlsx` | `02-chocolate-tempering-molding-checklists.xlsx` | Chocolate Tempering & Molding Checklists: Dark, Milk & White, Bonbons & Bars |
| 03 | `03-tareas-manager.xlsx` | `03-chocolate-shop-manager-checklist.xlsx` | Chocolate Shop Manager Checklist: Daily, Weekly & Monthly |
| 04 | `04-tareas-perfiles.xlsx` | `04-chocolate-shop-duties-by-role.xlsx` | Chocolate Shop Duties by Role: Chocolatier, Sales Associate & Shift Lead |
| 05 | `05-tareas-semanales-mensuales.xlsx` | `05-chocolate-shop-cleaning-checklist-maintenance.xlsx` | Chocolate Shop Cleaning Checklist, Inventory & Maintenance Schedule |
| 06 | `06-eventos-temporada.xlsx` | `06-chocolate-shop-seasonal-checklists.xlsx` | Chocolate Shop Seasonal Checklists: Holiday Season, Valentine's Day & Easter |
| 07 | `07-plantilla-personalizable.xlsx` | `07-blank-chocolate-shop-checklist-template.xlsx` | Blank Chocolate Shop Checklist Template (Editable) |
| 08 | `08-apertura-cierre-negocio.xlsx` | `08-chocolate-store-opening-closing-checklist.xlsx` | Chocolate Store Opening & Closing Checklist (Whole Shop) |
| 09 | `09-apertura-cierre-caja.xlsx` | `09-cash-drawer-opening-closing.xlsx` | Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log |
| B01 | `BONUS-01-briefing-servicio.xlsx` | `BONUS-01-chocolate-shop-pre-shift-meeting-template.xlsx` | BONUS: Chocolate Shop Pre-Shift Meeting Template (Huddle Notes) |
| B02 | `BONUS-02-calendario-anual-tareas.xlsx` | `BONUS-02-chocolate-shop-holiday-calendar.xlsx` | BONUS: Chocolate Shop Holiday Calendar & Product Planner (US) |

## 3. Reglas del delta (`mapas_chocolate.REGLAS_US` = las del base que aplican + estas)

| Concepto | Fuente |
|---|---|
| Obrador, cool room, vitrina, tienda, moldes, enfriado y reparto en °F | [criterio del kit] (cifras del ES) |
| Curvas de templado y precalentado de la temperadora | [fabricante] curva de cada cobertura; [criterio del kit] cifras del ES en °F |
| Ganache TCS salvo aw de laboratorio · frío 41 °F · date marking 7 días · congelado 0 °F | FDA Food Code 2022 §1-201.10 (TCS, tablas A y B); §3-501.16(A)(2); §3-501.17 |
| Sin mano desnuda en lo listo para consumir | §3-301.11 |
| Aviso escrito de alérgenos de lo no envasado (vitrina) | §3-602.12(C) (Food Code 2022, donde se adopte); FDA, ficha de diciembre de 2024 |
| Etiqueta de lo envasado en el local · «packaged» | §3-602.11(B); §1-201.10 |
| «May contain» voluntario · best-by voluntario salvo fórmula infantil | FDA Q&A Food Allergens (Ed. 5, 2022); USDA FSIS «Food Product Dating»; 21 CFR 107.20 |
| Alérgenos (9) · UK 14 | FALCPA + FASTER Act; Food Information Regulations 2014 (base) |
| Báscula legal para el comercio · CFPM y food handler cards | [estatal] pesas y medidas, NIST Handbook 44 (NTEP); §2-102.12 y [estatal] |
| Licencia de fabricación (caramelos, mayorista, correo) · bombones con alcohol · candy en el sales tax | [estatal]; Streamlined Sales and Use Tax Agreement (definición de «candy») |
| Campana NFPA 96 solo con grasa · EPA 608 · extintores · fichajes | base (tabla 11.4; 40 CFR 82 F; 29 CFR 1910.157; 29 CFR 516) |
| Fechas US · seguros · envíos con calor · food cost 30–35 % · cáscara 1/16–1/8 in | 5 U.S.C. 6103; 36 U.S.C. 117 y 109; [criterio del kit] |

°F que el kit puede afirmar (G7, `GRADOS_F_SPEC`): 0, 32, 41, 54, 57, 59, 60, 64, 68, 72, 77, 79, 81, 82, 84, 86, 88, 90,
100, 104, 113, 122, 131. Fuera del base: parásitos, moluscos, caliente, enfriado, recalentado, aviso de crudo, lavado de
vegetales, extinción de campana y FOG. `CELSIUS_SIN_F` = 08 «Cierre» B19 (su temperatura sube a la fila 10 con el reorden).

## 4. Memoria de traducción (`../heredar.py --kit chocolate`, `MEMORIA`: heladería, cafetería, base, catering, pizzería, hamburguesería, ghost kitchen y bar)

753 cadenas; GM 215 (958 palabras: pestañas, glosario, 184 `POR_CELDA` —09 47, 08 cierre 45, calendario 36, 30 horas,
05 13, tabla de vida útil 12, 03 1—, marca, versión). De las 538 a traducir: **105 heredadas** (102 exactas + 3 por
sufijo; 101 de la heladería, 2 de la cafetería y 2 del catering; 1.107 palabras) y **433 pendientes** (427 nuevas, 2
`NO_HEREDAR`, 2 con otro ADAPTAR, 2 «contexto»; **4.278 palabras**; 118 con ADAPTAR, 126 en total) → UN traductor
sonnet → `textos_en/G1.json` con los 433 ids. La heladería va delante: 107 heredadas frente a 105 con la cafetería
delante (mismo molde ligero).

    python3 extraer_textos.py --kit chocolate && python3 chocolate/mapas_chocolate.py && python3 heredar.py --kit chocolate
    python3 aplicar_en.py --kit chocolate --dry-run [--parcial] --idempotencia --mes October; python3 gates_en.py --kit chocolate [--parcial] --dir <carpeta> [--autotest]

Para la F2: `aplicar_en`/`gates_en` ya traen los ganchos del molde ligero (`CF_POR_CELDA`, `LIBROS_SIN_MARCA`,
`HOJA_HORAS`, `HOJA_VERDE`) y del 09 propio (`CASOS_G5`, `CELDA_CACHE_MAL`); no se ha tocado código común. A4 → Letter
en las 37 hojas. `gate_f1.py` es solo del kit base (sin `--kit`): su comprobación 7 se hizo a mano (POR_CELDA → regenerar,
ADAPTAR → G1/G2, glosario → mapa-glosario: 0 fallos). **Prueba de humo de la F1 (VPS):** `aplicar_en --dry-run
--parcial` monta los 11 xlsx (idempotente a la F2) y `gates_en --parcial` sale **VERDE 8/0** (G5 con los 2 `CASOS_G5`, 9
comprobaciones; G1 37 hojas, 139 fórmulas, 15 por celda, 17 CF por celda) y el autotest **19/19 CAZADOS**.

**Dudas para el traductor:** «fichero 09» / «hito en 08/09» del 01 (B8, B9, B30) → «file 09» con la pestaña EN citada;
«Montaje de servicio» (heredado «Service setup»); las familias del 02 (B39-B48: rocas → clusters, garrapiñados → candied
nuts, barquillos bañados → chocolate-dipped wafers); 06 «Navidad» A1/B6/B15 y «Pascua» B6/B9/B15 (sin turrón ni monas,
ADAPTAR); 03 «Semanal» B32 food cost 30–35 % se queda.

## 5. Erratas del ES (para su próxima v2.x; la EN nace corregida)

- 08 «Cierre del Negocio» B18-B19: apagar las vitrinas y registrar la temperatura de cierre del obrador DESPUÉS de activar
  la alarma (B16) y cerrar con llave (B17); B9 cierra persianas antes de recoger la señalización (B12) y vaciar papeleras
  (B14); B15 «enchufes» sin excluir cámaras y neveras.
- Versión mezclada: 01, 02, 04, 06 y B01 dicen «2.1 · octubre 2026» y 03, 05, 07, 08, 09 y B02, «2.0 · agosto 2026»
  (la EN sale 2.1 en los 11).
- Sin más erratas de fondo: lo demás que cambia es mercado (gas a diario, 10-15 días de la ganache fresca, Reyes, monas,
  comuniones, panellets).

## R. Research (una pasada, 24-oct-2026)

**Negocio que describe el ES:** obrador-tienda de chocolate (bombonería): producción propia (templado, moldeado,
bombones, tabletas, figuras, trufas) con tienda, vitrina climatizada, venta al peso, encargos, regalos de empresa y
pedidos online; sin café ni hostelería. Equivalente US: **chocolate shop / chocolatier** con retail counter.
**Demanda (DataForSEO, US, 2840/en):** bonbons 90.500 · chocolate shop 49.500 (local) · candy shop 33.100 (más amplio:
tienda de caramelos) · chocolatier 27.100 · chocolate truffles 27.100 · chocolate tempering 9.900 · chocolate molds 9.900 ·
chocolate store 9.900 · chocolate tempering machine 2.400 · chocolatier business 110 · chocolate business 110 · chocolate
business plan 50 · how to start a chocolate business 30 · chocolate making business 10; «chocolate shop checklist», sin
volumen. **Jerga US** (alta en `../../GLOSARIO-JERGA-ES-EN.md`, sección Chocolatería): chocolatier · tempering (tabling,
seeding) · tempering machine / melter · couverture (callets) · bonbons (molded) · truffles · ganache / fillings · shell
y capping · polycarbonate molds · fat bloom / sugar bloom · snap · panning machine · cool room · display case · gift
boxes · pre-orders · corporate gifting · sales associate · shift lead. **Delicado, comprobado:** el aviso escrito de
alérgenos de lo no envasado es §3-602.12(C) del Food Code 2022 y solo obliga donde se adopta (FDA, ficha de diciembre de
2024; Illinois DPH; Georgia DPH); la ganache de nata fresca se trata como TCS salvo análisis de aw (definición TCS,
tablas A y B). Marcas reales en el ES: ninguna (xlsx, `kit-tareas-chocolateria.ts` y `src/data/testimonials-chocolateria.ts`, 8 testimonios).
