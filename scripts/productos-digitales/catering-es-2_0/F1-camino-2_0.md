# Plan de Negocio Catering Temático Eventos ES → 2.0 · F1: camino de construcción

> Sesión Claude Code, 11-oct-2026. Arquitecto de F1, una pasada. Medido en el VPS (`/root/wt-cates`, venv `/root/venv-guias`,
> scripts de medición fuera del árbol, ya borrados) sobre `ee9c03b1`. Defectos L1-L16 del 1.x:
> `business-plans-en-4/F1-inventario-delta.md`. Las cifras del caso español las fija el research (fichero aparte en esta carpeta).

## 0. Decisión en tres líneas

1. **Camino A**: el Excel 2.0 lo construye el **motor ES de línea A** (`planes-v2_0/main.py` + `grupo_a.py`) sobre una **copia del Food Truck ES v2.2**, con un módulo nuevo `contenido_plan_catering_tematico_eventos/a.py`. **Ensayado**: sale A-β, idempotencia 0, 13/13 gates, censo OK, en 9 s.
2. Driver **sin permutar**: `cubiertos/día` = **invitados por evento**, `ticket` = **precio por invitado sin IVA**, `días de apertura` = **eventos al año**. La cobertura de personal (horas × personas × eventos) y el aforo (máximo de invitados) salen bien **sin tocar fórmulas**.
3. Único cambio en código común: `VOCABULARIO` con frases e **insensible a tildes** en `grupo_a.compilar_vocabulario` (unas 6 líneas), con regresión por huella sobre los 5 de línea A. Lo demás va en ficheros locales de esta carpeta. **F2 + F3 ≈ 1,85 M**.

## 1. Excel financiero 2.0: comparación de caminos (leído el código, medido el A)

| | **A · motor ES línea A** | B · circuito EN en modo ES→ES | C · xlsx EN catering → español |
|---|---|---|---|
| Base | FT ES v2.2 (9 hojas, 722 fórmulas, IVA 10/21, IS 15/25 + BIN, SS 33 %, SMI, préstamo con carencia, DSCR, tesorería) | FT ES v2.2 | `catering-financial-projections.xlsx` |
| Fiscalidad española | **nativa** | nativa (no la toca) | **hay que reconstruirla**: el libro EN lleva sales tax, impuesto US, $, Letter y pestañas EN |
| Código común tocado | 1 función opt-in (§1.3) | `aplicar_en` / `gates_en` / `mapas`: pestañas EN, CLAVES de literales, formatos sin €, US Letter, aviso D21, docProps, calibración D15 y el detector de español residual (G-gates) **asumen inglés** → un «modo ES» atraviesa los 6 kits EN vivos | ninguno, pero es el circuito EN al revés |
| Gates | los de `main.py`: idempotencia, `verificar_cache`, `blancos_contaminados`, 12 de §9, censo, demos pycel (`DIRECCIONES`, TIR/VAN, anualidad) | habría que reescribirlos para ES | ninguno hecho |
| Tokens F2 del Excel | ≈ 0,65 M (código + textos) | > 1 M y riesgo de regresión EN | > 1 M |

**Qué controla el módulo de contenido** (clasificadas las 713 celdas de texto del FT ES v2.2 por origen):
- **Contenido (≈ 240)**: `SUPUESTOS` (valor, rótulo, nota, fuente), `LINEAS_INGRESO`, `PLANTILLA` (puesto, personas, bruto, jornada), `COBERTURA`, `FIJOS` e `INVERSION` (importe, nota y **rótulo nuevo**, 3.er campo desde el motor 2.2; también `suprimir`), `INVERSION_EXTRA`, `AMORTIZABLE`, `UMBRALES`, `ESCENARIOS`, `ESTACIONALIDAD`, `INSTRUCCIONES` (131 celdas), `CHECKLIST`, `RECALIBRADO`, `ROTACION`, `VOCABULARIO`. `CONCEPTO` cambia el título de Instrucciones y los docProps.
- **Motor genérico (≈ 375)**: válido para cualquier negocio (IVA, préstamo, DSCR, tesorería). **54 celdas** hablan del driver o del FT. De ellas, **unas 25 frases de motor** solo se arreglan con vocabulario: «Días de apertura al año» (Supuestos A6, PyG A8, PE A11, Escenarios A7), «Cubiertos/Clientes necesarios al día/año (caja)» (PE A14-A20), «…previstos en el plan» (A23), las tablas A29/A31, «Ticket medio sin IVA», «Coste variable/Margen por cubierto», «Horas de servicio al día» (Personal A18), «En sala todo va al 10 %» (Supuestos C9, Tesorería O16, Instrucciones A8), «Alquiler mensual del local», «LOCAL Y FIJOS», «un local que acaba de abrir» (Tesorería O7) e Instrucciones A5/A30.
- **Fichero (≈ 95)**: lo hereda el libro y el contenido **no lo alcanza**: los títulos `Inversión Inicial!A1` «PLAN DE NEGOCIO: FOOD TRUCK», `PyG!A2` «…Food Truck urbano» y `Punto Equilibrio!A2`, y en el checklist A1/A2 y los nombres de pestaña. Las partidas (vehículo, ventanilla, generador, depósitos, proyecto técnico sanitario, «Mantenimiento vehículo + ITV») sí se reescriben con `INVERSION` y `FIJOS` (renombrar o suprimir) y `INVERSION_EXTRA`.

**`motor.detectar()`** firma por **títulos de hoja** normalizados (sin `0. Supuestos` ni `Instrucciones`) y aborta si nada casa. Plan A-β = `{inversion inicial, pyg 3 anos, punto equilibrio, escenarios, personal}`; el 1.x es **B-δ**, que `grupo_a` no procesa (`MOLDES = A-alfa, A-beta`): por eso se parte del FT. Checklist C2 = ≥ 6 hojas `^f[1-6]`. Calculadora `calc-beta` = hojas exactas `calculadora` + `ejemplos`: ⚠️ la nueva **tiene que llamarse así** o cualquier pasada de familia sobre `dl/plan-catering…` aborta (exit 2) y `demo_moldes` deja de dar 30/30. Proveedores P2 = `^\d+ proveedores$`: **no renombrar «96 proveedores»**.

**Ensayo de A (VPS)**: FT ES (plan + checklist) con los nombres de fichero del catering + contenido FT duplicado con `CONCEPTO`/`VOCABULARIO` de catering, `main.py --producto plan-catering-tematico-eventos --dry-run --origen … --solo a` → A-β 721 fórmulas nuevas, C2 68 ítems, idempotencia **0**, caché 0 fallos, `blancos_contaminados` 0, **13/13**, censo OK. Único fallo, y es lección: **un rótulo de driver no se renombra con el 2.º campo de `SUPUESTOS`** (las demos lo buscan por su rótulo canónico pasado por `VOCABULARIO`, `grupo_a.demos→R()`: «no se localizan las filas dias_sup»). El nombre del oficio va **siempre por `VOCABULARIO`**.

### 1.1 Construcción recomendada (F2, todo en el VPS)
1. `semilla_cat.py` (local): copia el FT ES v2.2.
   - Plan: reescribe los 3 títulos de fichero.
   - Checklist: título, cabeceras de fase, pestañas `F1 - …`…`F6 - …` y las filas de tarea con los recuentos de §2; el pie «Tareas completadas:» va debajo de la última. El motor recalcula DV, CF y contadores por filas: lo ha medido con CAF/TAP/PAN.
2. `contenido_plan_catering_tematico_eventos/a.py`, duplicado del FT con números y notas de catering: `alquiler_mes` = **alquiler de cocina central / obrador compartido** (contra L9) · `PLANTILLA` = dueño-chef + jefe/a de producción + **bolsa de personal de eventos** (N personas × jornada parcial: la columna Jornada ya existe, sin el parche SUMPRODUCT del EN) · `COBERTURA` = horas y personas por evento · `ROTACION` inactiva · `ESTACIONALIDAD` = forma del 1.x (bodas may-oct + empresa dic) · `Días medios de cobro` = mezcla B2C/B2B (nota: el anticipo no se modela) · `RECALIBRADO` 1.x → 2.0. Textos desde la celda gemela del **xlsx EN del catering** (mismo molde y coordenadas: Supuestos A1:C68 = Assumptions A1:C68) + el contenido del 1.x, en español nativo.
3. `VOCABULARIO` del catering, solo frases: `cubiertos/día→invitados/evento` · `cubiertos necesarios al día→invitados necesarios por evento` · `cubierto(s)→invitado(s)` · `días de apertura al año→eventos al año` · `días que abres→eventos del año` · `al día→por evento` · `ticket medio→precio medio por invitado` · `en sala→en el servicio de catering` · `alquiler mensual del local→alquiler mensual de la cocina central` · `local y fijos→cocina central y fijos` · `un local que acaba de abrir→un negocio que arranca`. ⚠️ `\bdía\b` suelto no (Personal J17 «30 días naturales» es correcto).
4. `main.py --dry-run --origen <semilla>`, sin `--sin-demos`. Copia a `dl/` con los **mismos nombres de fichero** (`get-download-urls.ts` no se toca).
5. Calibración (gate propio sobre la caché): DSCR mínimo ≥ 1,25 · saldo mínimo > 0 · cobertura de horas ≥ 98 % · holgura sobre el equilibrio de caja ≥ 15 % · los cinco semáforos verdes. Más el **barrido de cifras prohibidas** del 1.x (8.520 · 21.410 · 54.440 · 10.560 · 603.700 · 846.720 · 2.200 · 4.500 · «14 eventos/mes» · «5.500» · «11.500» · «55 %») y del vocabulario FT (food truck, vehículo, ventanilla, generador, ITV, clientes/día) a 0.

**Lectura del equilibrio.** Con el driver sin permutar, `Punto Equilibrio` da **invitados necesarios por evento** con los eventos del plan, e invitados/año. Los **eventos/año de equilibrio** (= ingresos de equilibrio ÷ (precio × invitados por evento)) los da el docx como token derivado y una referencia en Instrucciones. El crecimiento de los años 2-3 cae sobre el tamaño medio del evento, igual en euros; la nota de B7 lo explica.

### 1.2 Descartados con motivo
- **Permutar el driver como en el EN** (B4 = eventos/año): rompe la cobertura de personal (horas × invitados) y el aforo, y obliga a parchear fórmulas.
- **Pasada local tras `main.py`** en vez del cambio en `grupo_a`: la siguiente pasada de familia (motor 2.3) la desharía. Con el vocabulario en el motor, el catering queda como **miembro de pleno derecho** de la línea A.

### 1.3 El cambio en código común
`compilar_vocabulario` compila cada clave (ya `motor.norm`) con clases `a→[aá]`, `e→[eé]`, `i→[ií]`, `o→[oó]`, `u→[uúü]`, `n→[nñ]`; la búsqueda en `mapa` sigue siendo `norm(match)`. Hoy una clave con tilde **no casa nunca** (se normaliza a «dia» y el texto dice «día»): por eso FT/CAF/PAN solo usan claves sin tilde. Inerte para los 5 vivos (sus claves casan igual). **Gate de regresión**: `main.py --dry-run --solo a` de bar, tapas, cafetería, panadería y food truck con `diff_digest` frente a `dl/` = **0 diferencias**.

## 2. Checklist ES 2.0: molde de 6 hojas de línea A

**Sí, el molde admite recuentos distintos por fase** (FT 11/13/12/10/12/10 = 68 · CAF 11/13/15/12/14/10 = 75 · TAP 11/13/13/12/14/10 = 73 · PAN 11/12/12/10/11/10 = 66): `motor.checklist_ok_y_contador` deriva DV, CF y COUNTIF de las filas con texto; ninguna celda fija.

Columnas del FT ES: `OK · TRÁMITE / ACCIÓN · RESPONSABLE · PLAZO · NOTAS` (el 1.x no tenía «Responsable»: se rellena).

| Fase (pestaña) | Tareas | Origen (fila del 1.x · FT ES) |
|---|---|---|
| F1 - Constitución y fiscalidad | **12** | forma jurídica (6+22) · alta 036/037 con **IAE 677.9** (7) · RETA con cuota de inicio **sin cifra fija**, como el FT · certificado digital (FT) · cuenta (8) · gestoría + facturación **Veri\*factu** (16, FT) · 303 al 10 % (18) · 130/111 (17) · **390 + 347 + 349** en una tarea (19-21) · **RGPD** registro de actividades (13) · **LSSI** aviso legal y cookies (14) · condiciones B2C: precio final con IVA + cancelación (15) |
| F2 - Cocina, sanidad y permisos | **15** | APPCC (9) · registro sanitario autonómico (11) · **RGSEAA solo si sirves a otros establecimientos** (12) · contrato de **cocina central / obrador** (112, L9) · RC ≥ 600.000 € + intoxicación (25+26) · seguro de furgoneta (27) · equipo + cancelación/fuerza mayor (29+30) · permiso de evento en vía pública (31) · venta ambulante/ferias (32) · fuego/BBQ (33) · instalación del cliente (34) · hojas de reclamaciones · residuos y aceite · DDD (los tres del FT) · furgoneta isoterma (63) |
| F3 - Equipamiento y proveedores | **14** | equipo de las estaciones **que vendes primero** (37-45 → 1) · cocción portátil + sous-vide + tablas de color (46-48 → 1) · vajilla/cubertería/cristalería (49-51) · mantelería y emplatado (52-53) · frío + acumuladores (54) · cajas de transporte (55) · EPI (56) · báscula y sondas (57) · importadores (58+59) · carne y pescado (60+61) · verdura local (62) · TPV/datáfono (FT) · compra de furgoneta (63) |
| F4 - Personal | **10** | estructura de los FT ES adaptados: bolsa de personal de eventos (por horas / fijo discontinuo; **autónomo solo si lo es de verdad**: riesgo de falso autónomo, contra el «freelance 15 %» del 1.x) · alta en SS antes de cada evento · manipulador (10) · APPCC · alérgenos multiestación · PRL (28) · registro horario · información de datos · ensayo de montaje · fichas de estación (manual) |
| F5 - Marca y captación | **16** | 32 del 1.x condensadas: identidad · dominio · web con formulario de presupuesto (+SEO 78-79) · foto/vídeo (70+71) · GBP + reseñas (72+80) · RRSS (73/74/76) · LinkedIn · WhatsApp Business · directorios de bodas (81) · directorios B2B + Hosply (82+83+64) · planners: lista y outreach (86+87) · visita con degustación (88) · empresas/hoteles/embajadas (89, 92-94) · dossiers (90+91) · publicidad (95+96) · referidos + newsletter + showroom (97, 99, 100) |
| F6 - Primer evento y 90 días | **15** | briefing (104) · visita técnica (105) · presupuesto + anticipo 40 % (106) · contrato (107) · menús y alergias firmados (109) · plan B (108) · pedidos + frescos (110+111) · mise en place en obrador (112) · carga y salida (113+114) · montaje (115) · briefing + servicio (116+117) · recogida (118) · cobro y factura 24-48 h (119) · reseña + contenido (120+123) · CRM, costes reales y cierre trimestral (121+122, FT) |
| **Total** | **82** | 108 − 12 de multicocina (→ 2) − duplicados fusionados. **Siguen las 9 «solo España»** (IAE, RGSEAA, RGPD, LSSI, 390/347/349 y Hosply en directorios) |

**A verificar en F2 con fuente primaria** (una pasada, solo lo que el producto afirma): RGSEAA vs registro autonómico (RD 191/2011 art. 2.2, que el FT ES ya cita) · desistimiento B2C de 14 días en un servicio con fecha (art. 103.l TRLGDCU) · epígrafe IAE 677.9 · ¿ATP para la furgoneta isoterma en transporte nacional?

## 3. Docx ES: reescribir en las ranuras del FT ES, no arreglar el 1.x

| | Docx 1.x catering | FT ES v2.2 (molde) | EN catering (publicado hoy) |
|---|---|---|---|
| Párrafos · palabras | 120 · **2.059** | 131 · 6.948 | 131 · 6.662 |
| Encabezados | **0 Heading** (Normal 49, List Bullet 65, List Number 6) | **10 Heading 1** (37·44·51·59·67·76·83·91·100·109) | 10 H1, mismas ranuras |
| Tablas | 7 (todas con cifras del 1.x) | 0 | 0 |

**Decisión: reescritura en las 131 ranuras del FT ES con cifras por token.** Arreglar el 1.x es reescribirlo igual (cada cifra cambia, hay que añadir 10 encabezados y triplicar el texto) y peor estructurado.
- **Redacción** (Sonnet, 2 tandas en paralelo, una por mitad): ≈ 61 ranuras de texto, unas 6.700 palabras, como el EN (29 + 32). Fuentes por ranura: la gemela del EN catering (argumento) · el docx 1.x (concepto, mezcla 35/65, operativa en 6 fases, 9 riesgos) · el §9 legal del FT ES, ya verificado · los contratos (política comercial **B2C 40 % + 21/7 días + 48 h**; **B2B 40/30/30 + 28/14/7 días**).
- **Fuera**: «38 % bodas multiculturales», «73 % millennials», «96 proveedores reales validados», «España 2026», anexo de 17 CCAA. La firma ChefBusiness se queda (decisión de John del 22-ago).
- **Ensamblado**: `docx_cat_es.py` local (fork de `business-plans-en/ensamblar_docx.py`): clona el FT ES, sustituye por índice conservando estilo y resuelve los tokens leyendo la caché del xlsx ES por rótulo, más los derivados (eventos/año de equilibrio, inversión total, DSCR mínimo, caja mínima). **A4** (el FT ES sigue en Carta, defecto heredado) y autor `motor.CREATOR`.
- **Gates**: 10 Heading 1 · ≥ 6.000 palabras · 0 tokens sin resolver · cada cifra igual a la caché · 0 no latinos · 0 cifras prohibidas.

## 4. Calculadora ES: fork de `calculadora_cat.py`

El fichero ya es declarativo (`ENTRADAS`, `SALIDAS` con fórmula y espejo `calcular()`, `EJEMPLOS`, autotest pycel): se traduce y se cambian las reglas.
- Fichero: el de hoy (`calculadora-pricing-catering-tematico-eventos.xlsx`). Hojas `Calculadora` · `Ejemplos` · `Instrucciones` (firma `calc-beta`, §1). `#,##0.00 €`, A4, línea de versión y bio, docProps. **Fuera**: *service charge*, *sales tax* y su interruptor por estado, nota del IRS.
- **IVA 10 %** sobre el subtotal de catering. Verificado en fuentes secundarias que citan **DGT V0591-25** y **V0499-26**: el catering con servicio y el chef a domicilio van al 10 %. Menaje, mantelería y cristalería facturados con el catering siguen a la principal. Fila opcional «servicios no accesorios facturados aparte (decoración, animación) al 21 %». F2 cita la consulta original.
- **Precio final con IVA por invitado** visible: obligatorio en ofertas a consumidores (TRLGDCU art. 60).
- **Propina voluntaria** fuera del total y fuera de la base imponible: nota, no fila.
- **Entradas**: invitados · mínimo facturable · estilo (entrega sin servicio / bufé / cóctel / emplatado / estaciones) · **nº de estaciones temáticas** (personal y equipo por estación: mantiene verdad lo que prometen la ficha y los testimonios) · comida por invitado (escandallo) · bebida/maridaje · menaje y desechables · personal (personas × horas × €/h bruto × (1 + SS empresa 33 %)) · km ida × €/km × 2 · alquileres repercutidos · margen bruto objetivo.
- **Salidas**: precio por invitado sin IVA (redondeo 0,50 €), con IVA, subtotal, IVA, total, **anticipo 40 %**, importe retenido por tramo de cancelación (B2C y B2B, §3), **margen bruto CALCULADO**.
- **Ejemplos**: boda con estaciones, cóctel de empresa y cumpleaños de bufé, por las mismas fórmulas. Sustituyen a los «10 ejemplos validados» (L12).
- **Autotest**: espejo Python frente a pycel en los 3 ejemplos (± 0,01 €), y DV de lista en las entradas de texto (contra L11).

## 5. Los otros 7 ficheros: solo lo que contradice el modelo nuevo

Barrido openpyxl/python-docx, 182 coincidencias revisadas a mano.

| Fichero | Dónde | Corrección |
|---|---|---|
| guía especialización | p14 | «Inversión inicial moderada (5.500-8.500 €)» → inversión del modelo (cifra del xlsx) |
| guía especialización | p38, p40 | «Según el research del mercado España 2026» / «El research detectó» → sin atribución |
| guía especialización | t0, col. «Margen» | «55-65 %» → «Margen bruto orientativo sobre materia prima» (no es margen neto) |
| guía especialización | p18, p47, p50 | «freelance» → personal de eventos contratado (o autónomo real) |
| manual APPCC multicocina | p55-p62, t1.r9 | «equipo/bolsa de freelance» → personal de eventos (coherente con F4 y el docx) |
| manual APPCC multicocina | p69 | «Inscripción RGSEAA si transportas alimentos elaborados» → lo que fije el checklist F2 tras verificarlo |
| catálogo equipamiento | t10.r1 | «Renault Master L2H2 · 16.000 € usado / 380 €/mes» → alinear con la partida de furgoneta de `Inversión Inicial` |
| catálogo equipamiento | p6 | «equipamiento especializado por cada cocina del mundo» → «para las estaciones que vendas» |
| contratos B2B | p76 | «10 % catering / 21 % servicios asociados» → los accesorios facturados con el catering van al 10 %; 21 % solo lo no accesorio |
| plantilla proveedores (xlsx) | `96 proveedores!A2` | «Validados España 2026» → fuera (la hoja no se renombra: firma P2) |
| plantilla proveedores (xlsx) | `G5:G100` | 92 × «Validado» → columna «Estado» con DV Pendiente/Contactado/Homologado, vacía |
| 4 docx | p2 de 12 conceptos, carta, catálogo y manual | «validados/validado España 2026» → «Edición 2026» |

Sin cambios: precios por concepto (35-90 €/pax), menús, cláusulas de cancelación de los contratos (son la fuente de la política comercial) y la firma ChefBusiness.

## 6. Landing y dashboard ES: afirmaciones a corregir

**`astro-site/src/data/productos/planes/plan-catering-tematico-eventos.ts`:**

| Afirmación | Líneas | Corrección |
|---|---|---|
| «Inversión desde/mínima 5.500 EUR», «recomendado 11.500», «premium 35.000» | 32 · 145 · 180 · 262 | inversión total del modelo |
| «break-even 14 eventos/mes año 1» | 145 · 180 · 262 | equilibrio real (invitados/evento y eventos/año) |
| «5-9x menor que un catering con cocina central (45-120K EUR)» | 125 · 180 | **falso**: el modelo 2.0 alquila cocina central → fuera |
| «DOCX 60+ pp.» | 42 · 127 · 144 · 276 | páginas medidas con `paginas-gate` |
| «Plan Financiero Excel (6 hojas)», «ticket medio 2.200-4.500 €» | 128 · 145 · 276 | 9 hojas, precio por invitado |
| «10 ejemplos validados» | 146 | 3 presupuestos calculados |
| «freelance especializado» | 146 · 153 | personal de eventos |
| «110 hitos» | 149 · 246 | **82 tareas** |
| «tarifa plana 80 EUR/mes» | 246 | cuota reducida de inicio, sin cifra (como el FT) |
| «anexo 17 CCAA», «top 14 conceptos validados», «datos reales 2026 (4.585 M€, 25.183 €)» | 127 · 144 · 175 | fuera, salvo que el research los verifique y el docx los cite |
| «contactos verificables» de los 96 proveedores | 253-254 | «con web y zona; confirma disponibilidad» |
| «Formato estándar bancos para microcrédito o ICO emprendedores» | 262 | «préstamo con cuadro, DSCR y tesorería de 12 meses» |

**No se tocan**: `priceOld '€165'` / `-73%` (289-293) y testimonios (166-167), capa comercial intacta por decisión de John (la calculadora conserva «estaciones temáticas»); «11 entregables»; `get-download-urls.ts` (mismos nombres).

**Dashboard vivo** (`src/pages/PlanCateringTematicoEventosDashboard.tsx`, montado por `astro-site/src/islands/library/PlanCateringTematicoEventosLibraryIsland.tsx`): `desc` de las líneas **19** (60+ pp., 17 CCAA, validados), **26** (5.500-35.000, 14 eventos/mes), **33** (calculadora), **54** (checklist/RGSEAA), **82** (freelance) y **89** (guía). Importa solo componentes `shared/` (SaasDiscoveryBanner, ProductChangelog, LogoBadge, WhatsAppProductSupport): **`src/components/plan-catering-tematico-eventos/*` solo los usa la landing SPA `src/pages/PlanCateringTematicoEventos.tsx`, que no se construye: no tocar.** Añadir la entrada **2.0** en `src/data/productos-changelog.ts:1381` (alimenta `ProductVersionBadge`).

Cierre F3: `llms-full.txt:127` solo enlaza (no hay que tocarlo); 19 posts enlazan la landing sin cifras del 1.x; correo de actualización en la cola de 5 días.

## 7. Presupuesto F2 + F3

| Pieza | Quién / dónde | Tokens |
|---|---|---|
| Vocabulario sin tildes en `grupo_a` + regresión de los 5 de línea A | opus · VPS | 0,08 M |
| `semilla_cat.py` + `contenido_…/a.py` (cifras, reglas, `VOCABULARIO`, calibración) + `main.py` + gate de calibración | opus · VPS (un implementador) | 0,45 M |
| Textos del contenido (≈ 4 K palabras: notas de Supuestos, partidas, plantilla, Instrucciones) | sonnet | 0,20 M |
| Checklist 82 × 4 columnas (+ las 4 verificaciones legales de §2) | sonnet | 0,15 M |
| Docx: 2 tandas ‖ + `docx_cat_es.py` | sonnet × 2 + opus | 0,35 M |
| Calculadora ES (fork) + autotest | sonnet | 0,12 M |
| 7 ficheros: parches quirúrgicos de §5 | sonnet · VPS | 0,08 M |
| Landing, dashboard, changelog 2.0 | sonnet · Mac | 0,07 M |
| Gates + UNA revisión adversarial final | opus | 0,20 M |
| F3: PR, preview, gates LIVE (E-f, miselup, whatsapp), páginas, correo | orquestador | 0,15 M |
| **Total** | | **≈ 1,85 M** (colchón 0,15 M hasta 2 M) |

Lo que lo dispararía: permutar el driver como en el EN, mantener 108 tareas en el checklist o arreglar el docx 1.x en lugar de reescribirlo.
