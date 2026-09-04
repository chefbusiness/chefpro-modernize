# «Manual del Manager de Restaurante» — SPEC v1.0 (2026-09-04)

> Producto NUEVO nº 2 del ciclo de sesiones alternadas (decisión de John, 2026-08-31); primer producto de
> la línea **«Manuales operativos»** de aichef.pro. John eligió el producto esta sesión («quiero hoy de nuevo
> que nos enfoquemos en un producto nuevo») y, como ayer, las decisiones del research las toma el
> orquestador. Fuentes: `auditorias/manual-manager-RESEARCH-2026-09-04.md` (síntesis), las cinco lentes
> `manual-manager-research-L1..L5`, y la refutación `manual-manager-research-REFUTACION-2026-09-04.md`
> (veredicto «CORREGIR ANTES»: 10 altos, 19 medios, 3 bajos). **Todos sus hallazgos se resuelven en §1.**
>
> Fuente de verdad del CONTENIDO: esta SPEC + `guias-v2_0/guion_manual_manager_restaurante.py`.
> Fuente de verdad de las CIFRAS del texto: los xlsx de `astro-site/public/dl/manual-manager-restaurante/`
> y `auditorias/guias-v2-research-sector.json` (ids `MM-*`). El PDF cita celdas y normas, no inventa.
> Molde de todo el proceso: `guia-food-cost-SPEC.md` (ayer) — lo que aquí no se dice, se hace igual.

## 0. Ficha del producto

| Campo | Valor |
|---|---|
| Nombre | **Manual del Manager de Restaurante** («manager (gerente/encargado)» en la primera mención de cada documento y en el hero) |
| Subtítulo | Operaciones, personas, números, servicio y ley — el criterio del día a día, verificado contra el BOE |
| `productId` / slug | **`manual-manager-restaurante`** (prefijo nuevo `manual-`; `robots.txt` ya lleva sus 10 reglas, gate `--live` verde en `68eb353`) |
| Landing · access · library | `/manual-manager-restaurante` · `-access` · `-library` |
| Env var Stripe | `VITE_STRIPE_PAYMENT_LINK_MANUAL_MANAGER` |
| Precio | **55 €** (D1) — IVA incluido para consumidor UE; Stripe con `automatic_tax`, `tax_behavior: exclusive` |
| Ancla | Sin `priceOld` ni `discountBadge` (producto nuevo, Ómnibus) |
| Entregables | 1 manual (PDF + DOCX) · 1 bonus «12 situaciones resueltas» (PDF + DOCX) · **7 libros de Excel** con fórmulas vivas |
| Público | Quien **ya dirige** un restaurante o un turno: gerente, encargado, director, jefe de sala, propietario-operador. NO es guía de apertura |
| Idioma/mercado | Español. Marco legal **español** (ET, ALEH VI, LIVA, RD 1021/2022…); todas las casillas de parámetros son editables para Hispanoamérica; euros; vocabulario ES con equivalencia LATAM la primera vez (gerente/encargado ↔ administrador; cuadrante ↔ rol/horario; arqueo ↔ corte de caja; nómina ↔ planilla; sala ↔ salón) |
| Canal | Hub, 5 posts del blog ES con banner FIJADO + enlace contextual (script propio `fase8g`), páginas `/usos/rol/…`, lista de compradores (Resend, segmento ES), plataforma. **No se promete tráfico SEO** (L2: «gerente de restaurante» 50/mes en España y 89 % empleo) |

## 1. Decisiones firmadas (resuelven la refutación; no se reabren al construir)

| # | Decisión | Resuelve |
|---|---|---|
| D1 | **Precio 55 €.** Mismo recuento que la Guía Food Cost (20 caps + 7-8 xlsx + bonus) → mismo escalón. El ancla externa se escribe con cifras homogéneas: Last.app Growth **1.140 €/año sin IVA** (precio oficial) y el manual es un pago único; **no se cita el plan Starter** ni «menos que un mes de cualquiera de sus planes». Sin porcentaje «5,7 %» | B1, B2, B7 |
| D2 | **Sin precio tachado, sin `aggregateRating`, sin testimonios** (sección oculta con `items: []`) | — |
| D3 | **7 libros de Excel** (§2.2): el plan de 90 días deja de ser libro (duplicado estructural del de la Guía Food Cost) y pasa a ser UNA hoja del libro de reuniones; la hoja de briefing desaparece (existe 20 veces en el catálogo); el cuadro semanal conserva el prime cost pero se diferencia por cadencia (semana ISO), KPI operativos y la hoja de definiciones, y su hoja `Instrucciones` explica la relación con el cuadro mensual de la Guía Food Cost | B3 |
| D4 | **El libro legal (`calendario-cumplimiento-legal.xlsx`) absorbe tres hojas de referencia** —`Topes de Jornada`, `Permisos y Cómputo`, `Régimen Disciplinario ALEH`— para que los caps. 11, 12 y 14 tengan herramienta propia del pack. El cap. 01 dice qué incluye el pack y qué es cross-sell (Kit de Gestión de Personal 14 €, Kit de Tareas 12 €, Pack APPCC, Guía Food Cost 55 €) | B4 |
| D5 | **Cotización empresarial al 33 %** en el cuadro semanal (convención de familia: `kit-gestion-personal/03` y `cuadro-de-mando-prime-cost`), en celda verde con nota que desglosa las partidas (contingencias comunes 23,60 % + desempleo 5,50 % indefinido + FOGASA 0,20 % + FP 0,60 % + AT/EP según tarifa + MEI 0,80 % en 2026 ≈ 32-33 %; cita a la Orden de cotización vigente). **MM-17 (23,60 %) es «contingencias comunes», nunca «coste-empresa»** | A1 |
| D6 | **Permiso parental: dos figuras** (cap. 12, hoja `Permisos y Cómputo`, MM-26 reescrito): 8 semanas NO retribuidas (art. 48 bis ET) **y** 2 semanas retribuidas hasta los 8 años (RDL 9/2025, art. 48.4.c ET, prestación art. 177 LGSS); nacimiento **19 semanas** desde el RDL 9/2025. La lista negra se reescribe: lo prohibido es «el permiso parental de 8 semanas es retribuido», no hablar de la parte retribuida | A2 |
| D7 | **Organigrama del cap. 01 con el ALEH VI real** (BOE-A-2023-6344 + BOE-A-2026-18630): 6 áreas funcionales y 3 grupos; «encargado», «director» y «administrador» son **denominaciones de uso**, no categorías del convenio; el «gerente de centro» del ALEH es de *restauración moderna*. Nada de prometer que el convenio tipifica los cinco nombres | A3 |
| D8 | **Correcciones legales de la refutación que van al guion, a los xlsx y al JSON** (agente corrector, §7): *doggy bag* obligatorio desde el **22-12-2022** (RD 1021/2022) con la excepción del bufé y la obligación de informar; **factura simplificada cualificada** (con NIF del cliente) SÍ entra en la factura-e B2B → regla de tres casillas en el cap. 06 (art. 7.2 RD 1619/2012); exención de 1.300 m² de la Ley 1/2025 **sólo del apartado 4** (6.1, 6.2, 6.3 y 6.5 obligan a todo restaurante que no sea microempresa) → tabla «de qué estás exento / de qué no»; **propinas** al cap. 06 apoyadas solo en el RIRPF y en la norma de cotización (las consultas V3095-17 y V2236-13 NO se citan: no verificadas); reconocimientos médicos voluntarios **con las tres excepciones del art. 22.1 LPRL** e informe previo de la RLT; art. 41.3 ALEH con su excepción, la remisión al art. 55.1 ET y la vigencia **desde el 04-09-2026 hasta el 31-12-2030** | A4, A5, A6, A7, A9, A13 |
| D9 | **Datos del INE permitidos** con su etiqueta exacta: supervivencia de empresas de hostelería (75,6 % a 1 año, 53,5 % a 2, 38,8 % a 3), absentismo de hostelería (ETCL tabla 6043), coste salarial hostelería vs media (17.190,75 € vs 28.410,78 €). **Sustituyen** a Linkers (1.512/2.345 €) y a cualquier cifra secundaria. La temporalidad se fecha (2T 2026) o no se escribe | A8, A10 |
| D10 | **Las 11 citas acotadas en la propia frase** (A11): TheFork 39 % = muestra de ticket medio > 25 € y perfiles directivos; prime cost 60-65 % = Laube/RestaurantOwner, y Toast «60 % o menos»; CaixaBankLab (2017, rev. 2022) sin «Sapiens» ni «barra/autoservicio»; ticket medio 21 € = 2024; +19 pp = franja de las 19:00; 1,92 % CoverManager = un solo día; 17.094 € = cálculo propio (14 pagas × 1.221 €), no cita del RD; «beneficios sociales» fuera de la EACL; matices Square+AmEx. **El umbral ≤65 %/≤55 % de prime cost se presenta como criterio de la casa derivado de CaixaBankLab, no como cifra de fuente** | A11 |
| D11 | **Lista negra ampliada** (§8): todo lo del §11 de la síntesis + los 11 añadidos de A12 + «el permiso parental es retribuido» + «el 63,5 % es la tasa a 3 años» + «Starter/mes» + «5,7 %» + el 60 % de cierres (que además sigue publicado en 3 sitios del repo: tarea aparte, §9) | A12 |
| D12 | **Claim de actualización honesto**: «Verificado contra el BOE el 4 de septiembre de 2026, incluida la modificación del ALEH VI publicada ese mismo día». Cada tabla legal del manual lleva **al pie**: «Verificado el 04-09-2026 · <norma> · <URL>». Hoja `Estado Normativo` con fecha de corte editable. El RD del registro horario, si sale, entra en el changelog 1.1 (actualizaciones incluidas) | A14, B9 |
| D13 | **Mismo restaurante modelado** que la Guía Food Cost: «La Encina» (70 plazas, servicio en mesa, 52 servicios/mes, 3.900 cubiertos/mes, food cost objetivo 30 %); plantilla de **12 personas** y **6 estaciones**; sus cifras de personal cuadran con el prime cost de aquella guía. Caso **modelado**, no cliente real. Vive en `scripts/productos-digitales/manual-manager/datos_ejemplo.py` (única fuente) | — |
| D14 | **FAQ de compra**, 12 preguntas: se funden Q1+Q3+Q4 y Q5+Q6 del §10.2 de la síntesis (intención de empleo fuera) y los 3 huecos van a preguntas de compra (¿sirve fuera de España?, ¿necesito los kits?, ¿qué pasa cuando cambie la ley?). Se pasa `clasifica()` de `fase8d-faq-duplicadas.py` sobre la FAQ final: cero pares PARECIDA/DEFINICION | B5, C6 |
| D15 | **Enlaces internos verificados por existencia**: el rol es `/usos/rol/director-operaciones-grupo-restauracion` (no el `id`); antes de publicar, `ls` de cada destino en `astro-site/src/pages` / `content` / `use-cases.ts` | C1 |
| D16 | **Blog: script propio `fase8g-manual-manager-blog.py`** clonado de `fase8f` con `PRODUCTO`/`HOY` parametrizados y su propia `PRIORIDAD_SUSTITUIR` (primero `kit-escandallos`, `guia-food-cost`, guías «Cómo Montar») y `NUNCA` (`kit-gestion-personal`, `kit-tareas*`, `pack-appcc`: son cross-sell del manual). Gate de reversibilidad byte a byte. 5 posts (L2 §5 / síntesis §10.3) + `blog-lastmod.json` | C3 |
| D17 | **Gates de documentos**: `paginas_prometidas: 85` (calibración medida ≈ 330 palabras/página), `min_palabras_cap: 1200`, ~30.000 palabras; bonus `paginas_prometidas: 25`, ~7.500 palabras. La landing publica las páginas **medidas** | C4 |
| D18 | **`comingSoon`**: al lanzar se retira la entrada «Manual del Manager de Restaurante» de los DOS ficheros del hub (`ProductosDigitales.tsx` y `ProductosDigitalesHubPage.astro`) | C5 |
| D19 | **`tipo_doc = 'manual'`, `categoria_doc = 'Manual profesional'`** en el guion; residuo «esta guía» del prompt (`documentos.py` ~1027) parametrizado igual | C7, L5 |
| D20 | **Fichero de landing en `astro-site/src/data/productos/manuales/manual-manager-restaurante.ts`** con el tipo `GuiaData` (`why.titlePre = '¿Por Qué Este '`, `why.titleGold = 'Manual'`). `sync-payment-links.py` lee `productos/**` → no depende de la carpeta. Si el agente de capa de producto encuentra un glob sobre `productos/guias/` que lo rompa, cae a `guias/` y lo anota | L5 §3.3 |
| D21 | **Inglés: no.** Nada en EN (decisión de John del 31-ago) | — |
| D22 | **Límite del copy**: el manual explica la ley española; la landing lo dice en la primera pantalla y en la FAQ (el 60-70 % del volumen medido está en LATAM, donde solo valen las herramientas con casillas editables y el método) | B10 |

## 2. Entregables (ruta `astro-site/public/dl/manual-manager-restaurante/`)

### 2.1 Documentos (pipeline `guias-v2_0/documentos.py`, guion `guion_manual_manager_restaurante.py`)

| Fichero | Contenido | Gates |
|---|---|---|
| `manual-manager-restaurante.pdf` + `.docx` | 20 capítulos (§4) | ≥ 85 páginas medidas · ≥ 28.500 palabras · ningún cap. < 1.200 · paridad PDF↔DOCX · tablas ancladas · no latinos · WinAnsi · fechas · coherencia de cifras · metadata |
| `BONUS-12-situaciones-resueltas.pdf` + `.docx` | 12 situaciones (§4.2) | ≥ 25 páginas · ≥ 7.100 palabras · idem |

### 2.2 Los 7 libros de Excel

Convenciones de familia (obligatorias, idénticas a `guia-food-cost-SPEC.md` §2.2): helpers de `guias-v2_0/motor.py`; hoja «Instrucciones» primero (celdas verdes = editables, línea `Versión 1.0 · septiembre 2026 · aichef.pro/manual-manager-restaurante · info@aichef.pro`, bio anclada, nota de desproteger); **cero constantes dentro de una fórmula**; `IFERROR(...,"")`; semáforos con `ISNUMBER`; «sin dato» = `""`; **prohibido `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`**; formatos `#,##0.00 €` / `0.0%` / `dd/mm/yyyy`; A4 con `print_setup`; metadata `author='AI Chef Pro'`; **datos de ejemplo desde `datos_ejemplo.py`** (la misma plantilla de 12 personas y las 6 estaciones en todos los libros); tras generar: `inject_cache.py` + verificación `data_only` de cada fórmula registrada + `mapa-<libro>.json` de celdas (contrato del guion).

**Cada tabla o celda que fije un dato legal lleva nota «Verificado el 04-09-2026 · norma · URL» (D12).** La especificación celda a celda es la del §3.3 de la síntesis, con estos cambios:

| # | Fichero | Hojas | Cambios respecto a la síntesis |
|---|---|---|---|
| 1 | `cuadro-de-mando-semanal-manager.xlsx` ⭐ | Instrucciones · Parámetros · Semana (52 filas ISO) · KPI y Definiciones | SS empresa **33 %** en celda con desglose en nota (D5); `Instrucciones` explica la relación con `cuadro-de-mando-prime-cost` de la Guía Food Cost (semana vs mes) |
| 2 | `matriz-formacion-polivalencia.xlsx` | Instrucciones · Matriz · Plan de Cross-Training · Cobertura por Estación · Coste de una Baja | sin cambios; 12 empleados × 6 estaciones sembrados desde `datos_ejemplo.py` (la matriz admite 30 × 12) |
| 3 | `quejas-reclamaciones-resenas.xlsx` | Instrucciones · Parámetros · Registro de Quejas · Reclamaciones Formales · Reseñas · Resumen | plazos autonómicos sembrados **solo** con lo verificado (Cataluña 1 mes; Andalucía 10 días hábiles y hoja electrónica desde mayo 2026) y celda editable para el resto con nota «consulta tu comunidad» |
| 4 | `seleccion-scorecard-entrevista.xlsx` | Instrucciones · Scorecard · Comparativa de Candidatos · Preguntas por Competencia | nota legal art. 9.5 Ley 15/2022 en la hoja de preguntas |
| 5 | `calendario-cumplimiento-legal.xlsx` ⭐ | Instrucciones · Estado Normativo · Calendario y Vencimientos · Documentación Obligatoria · **Topes de Jornada** · **Permisos y Cómputo** · **Régimen Disciplinario ALEH** | tres hojas nuevas (D4): topes con norma/URL/fecha (40 h promedio, 9 h/día, 12 h entre jornadas, 1,5 días/semana acumulable en 14, 80 h extra/año, 15 min si lo dice el convenio, 4 años de conservación del registro); permisos con días y fuente (30 naturales; fallecimiento 2+2; enfermedad grave 5; parental 8 no retribuidas + 2 retribuidas; nacimiento 19; fuerza mayor en horas; guarda legal; adaptación con silencio positivo); régimen disciplinario (faltas leves/graves/muy graves del ALEH VI con las novedades del 04-09-2026: registro de jornada 2/3-4/≥5, móvil, fumar; audiencia previa de 2 días con su excepción). Columna «¿lo fija una norma estatal? Sí/No» en el calendario |
| 6 | `reuniones-acuerdos-plan-90-dias.xlsx` | Instrucciones · Calendario de Reuniones · Guion de Reunión Semanal · Uno-a-uno · Actas y Acuerdos · **Plan 90 Días** | sin hoja de briefing (D3); la hoja `Plan 90 Días` (20 decisiones: área, herramienta de origen, decisión, responsable, semana, impacto, estado; fecha objetivo calculada) sustituye al libro descartado; sin hoja de KPI (viven en el libro 1) |
| 7 | `auditoria-interna-servicio.xlsx` | Instrucciones · Auditoría · Resumen por Área · Histórico | ~60 puntos en 6 áreas; excluye APPCC/sanidad a propósito (remite al Pack APPCC) |

### 2.3 Lo que NO se construye (se cita con cross-sell)
Checklists del día (kit-tareas/03, 110 tareas), arqueo (kit-tareas/09), cuadrante y control de horas (kit-gestion-personal/01-02), coste laboral (03), onboarding (04), vacaciones (05), evaluación (06), directorio (07), plantilla óptima (BONUS-02), registros APPCC (pack-appcc), escandallo y matriz de carta (Guía Food Cost / Kit de Escandallos), plan de 90 días como libro.

## 3. Bloque legal — los 8 estados verificados a 2026-09-04 (fuente primaria leída; detalle en L3 y refutación)

| Norma | Estado a hoy | Qué escribe el manual |
|---|---|---|
| Jornada 37,5 h | **Rechazada** (Congreso, 10-09-2025) | 40 h de promedio en cómputo anual (art. 34.1 ET) |
| Registro horario digital | **En tramitación** (dictamen desfavorable del Consejo de Estado 23-03-2026; RD anunciado) | Rige el art. 34.9 ET: registro diario, 4 años, papel o Excel válidos. Si sale el RD → changelog 1.1 |
| Verifactu | **Aplazado a 2027** (RDL 15/2025, art. 3): 1-01-2027 sociedades, 1-07-2027 resto | Fechas nuevas; sin las de 2026 |
| Factura-e B2B | Reglamento aprobado (RD 238/2026), **aún no exigible** (12/24 meses desde la orden) | Simplificadas fuera **salvo las cualificadas** (D8) |
| Ley 1/2025 desperdicio | **Vigente**; art. 6 exigible desde 02-04-2026 | *Doggy bag* desde 22-12-2022 (RD 1021/2022 art. 18.5); exención 1.300 m² solo del apartado 4 |
| SMI 2026 | **1.221 €/mes** (RD 126/2026) | 14 pagas; 17.094 € es cálculo propio |
| Fumar en terrazas | **Proyecto de ley** (Consejo de Ministros 21-07-2026) | Terraza legal = máximo dos paredes (Ley 28/2005, art. 2.2) |
| RD 3484/2000 | **Derogado** desde 22-12-2022 (RD 1021/2022); también el RD 1420/2006 | Temperaturas del art. 30 RD 1086/2020; anisakis −20 °C/24 h o −35 °C/15 h |
| **ALEH VI** | **Modificado y publicado HOY** (BOE-A-2026-18630, BOE 219 de 04-09-2026; vigente desde hoy hasta 31-12-2030) | Audiencia previa (art. 41.3, 2 días, permiso retribuido si se aparta), régimen del registro de jornada (38.10 / 39.21 / 40.14), móvil (38.12), fumar (39.20), caps. XIII LGTBI y XIV catástrofes |

## 4. Índice del manual (guion cerrado en `guion_manual_manager_restaurante.py`)

Presupuesto: 20 capítulos · 1.400-1.600 palabras (el 19 y el 11, 1.800) · 1-3 tablas por capítulo construidas desde los xlsx o desde el bloque legal · `NO_COMUN` de familia + lista negra §8 · cifras solo desde celdas o ids `MM-*` (las reglas sin cifra llegan como «REGLA SIN CIFRA», parche del 04-09 en `documentos.py`).

Los 20 capítulos son los del **§8 de la síntesis** con estos cambios obligatorios:

| Cap. | Cambio |
|---|---|
| 01 | Organigrama con el ALEH VI real (D7); tabla «qué incluye el pack / qué es cross-sell» (D4); mapa problema → capítulo → herramienta con los 7 libros |
| 02 | Tabla desde `cuadro-de-mando-semanal-manager!KPI y Definiciones` |
| 04 | Coste-empresa con el desglose de cotización en celda (D5); umbral 65/55 como criterio de la casa (D10) |
| 06 | + bloque de **propinas** (RIRPF + cotización, sin consultas DGT) y regla de tres casillas de la factura-e (D8) |
| 11 | Tabla desde `calendario-cumplimiento-legal!Topes de Jornada`; régimen disciplinario del registro (ALEH 04-09-2026) |
| 12 | Tabla desde `…!Permisos y Cómputo` con las dos figuras del permiso parental (D6) |
| 13 | Datos INE permitidos (D9); por qué no se cita el 63,8 % |
| 14 | Tabla desde `…!Régimen Disciplinario ALEH`; art. 41.3 completo con excepción y vigencia (D8) |
| 15 | Reconocimientos médicos con las tres excepciones (D8) |
| 17 | Plazos autonómicos solo verificados; reseñas con las cifras acotadas (D10) |
| 19 | *Doggy bag* 22-12-2022 + excepción del bufé; exención 1.300 m² bien acotada (D8) |
| 20 | Plan 90 días = hoja del libro 6; auditoría = libro 7; calendario = libro 5 |

### 4.2 Bonus «12 situaciones resueltas del manager» (documento propio del pipeline, `BONUS` del guion)
Las 12 del §8.1 de la síntesis (baja a dos horas del servicio · caja descuadra 40 € tres días · hoja de reclamaciones · reseña de 1★ por intoxicación · 19 meses encadenando temporales · prime cost 71 % · reducción por guarda legal en viernes noche · inspección de Sanidad · comunicación de acoso · el cocinero clave se va · el propietario quiere subir la carta un 10 % · despido disciplinario con audiencia previa). Cada una: situación con datos del pack, qué NO hacer, protocolo, norma aplicable (con «verificado el 04-09-2026»), herramienta usada y guion literal de la conversación cuando la hay. 550-700 palabras y una tabla por situación.

## 5. Capa de producto
Mapa exacto en L5 §4.1 (mismos 20 ficheros del producto 45, con `Manual`/`MANUAL_MANAGER` donde iba `GuiaFoodCost`/`GUIA_FOOD_COST`): `zona-app.ts` (registro; genera `-access`, `-library` e island con `fase5-generate-zona-app.py`, bump 45→46), SPA (`ManualManagerAccessGate.tsx` wrapper de `ProductAccessGate`, `ManualManagerDashboard.tsx` con secciones Manual (2) · Herramientas (7) · Bonus (2), rutas en `App.tsx`), 4 functions + `productos-digitales-config.ts` (claves `manual-pdf`, `manual-docx`, `bonus-pdf`, `bonus-docx`, `cuadro-semanal`, `matriz-polivalencia`, `quejas-resenas`, `scorecard-seleccion`, `calendario-legal`, `reuniones-plan-90`, `auditoria-servicio`), landing `manuales/manual-manager-restaurante.ts` + wrapper `.astro` (env resuelta a mano), catálogo (46), hub (tarjeta «Nuevo» + retirar `comingSoon` en los dos ficheros, D18), `linkify-use-case.ts`, `productos-changelog.ts` (1.0), footerLinks cruzados en `kit-gestion-personal.ts`, `kit-tareas.ts` y `guia-food-cost-ingenieria-menu.ts`. Imágenes ya en `main` (`e884a8d`): `/lovable-uploads/ai-gallery/manual-manager-{hero,sala,briefing,oficina,pase,equipo}.jpg` + `/og-manual-manager-restaurante.jpg`. Stripe: John crea producto + Payment Link (55 €, `tax_behavior exclusive`, redirect a `-access?session_id={CHECKOUT_SESSION_ID}`, automatic_tax, invoice) → env var en Netlify (scope builds, todos los contextos) → `sync-payment-links.py`. Blog: `fase8g` (D16). Email de lanzamiento: `emails/broadcast-manual-manager-lanzamiento-es.html` + `resend-broadcast.py` (segmento «AI Chef Pro ES», prueba a John, programado 10:00 Madrid del día siguiente).

## 6. Gates antes de LIVE
`inject_cache.py` + `data_only` por fórmula registrada · `postprocess-transversal.py <ruta> --dry-run` · `censo-entregables.py --only manual-manager-restaurante --fail` = 0 · `gate-no-latinos.py --only <carpeta>` · `documentos.py` todo `ok` y páginas medidas (≥ 85 / ≥ 25) · script del Bug #2 (`MISSING: 0`) · `gate-flujo-postpago.py --offline --only manual-manager-restaurante` · `fase5-generate-zona-app.py --check` · `robots-gate.py --live` (ya verde; repetir tras el deploy) · `whatsapp-gate.py` por inspección (landing sin `whatsapp={false}`, library con él) · FAQ por `clasifica()` (D14) · enlaces internos por existencia (D15) · build Netlify `ready` · `gate-flujo-postpago.py --only …` LIVE · compra de prueba real.

## 7. Presupuesto y reparto
Research + síntesis + refutación (cerrado): ≈ 2,4 M tokens de subagentes. Construcción: 1 opus `datos_ejemplo.py` → 3 constructores opus (libros 1-2 · 3-4 · 5-6-7) → 1 refutador opus de los xlsx (dos lentes) → fixer sonnet → 1 opus corrector del JSON/lista negra (D6, D8, D9, D10; ya lanzado) → 1 opus guion → `dump_prompts.py` → ~45 redactores sonnet por bloque con `check_bloque.py` → `documentos.py` ensambla → 1 opus capa de producto + 1 sonnet `fase8g` blog → gates → Fable: functions/Stripe/env, verificación final, LIVE, email. Térmica: `istats cpu temp` antes de cada python local; un python cada vez por agente.

## 8. Lista negra (va íntegra al `NO_COMUN` del guion)
Todo el §11 de la síntesis (cifras sin fuente primaria, afirmaciones caducas, errores de método) **más**: «el permiso parental es retribuido» / «el permiso parental no es retribuido» sin distinguir las dos figuras · «el 63,5 % de las empresas de hostelería cierra a los 3 años» (es 46,5 % a 2 años: 53,5 % supervivencia) · «menos de lo que cuesta un mes del plan Starter» · «5,7 %» · «60 % de los restaurantes cierra» en cualquier forma · «el ALEH tipifica al encargado/director/administrador» · «SS a cargo de la empresa 23,60 %» · «el carné de manipulador es obligatorio» · «la campana/las plagas/los termómetros tienen periodicidad legal» · «las consultas V3095-17 / V2236-13 dicen…» · «Verifactu obliga desde 2026» · «el registro horario debe ser digital» · «la jornada máxima es de 37,5 h» · «el doggy bag obliga desde 2025» / «desde el 15-12-2022» · «un restaurante de menos de 1.300 m² está exento de la Ley 1/2025» (solo del apartado 4) · «Toast recomienda 60-65 %».

## 9. Seguimientos fuera de esta sesión (no bloquean el lanzamiento)
- A12: «el 60 % de los restaurantes cierra» sigue publicado en `guia-restaurante-casual.ts:21`, `HeroSection.tsx:71` y `pseo-cities-content.es.ts:60` → decisión de John (copy comercial de otras páginas).
- C6: extender `fase8d-faq-duplicadas.py` a `astro-site/src/data/productos/**` (45 landings).
- C1: extender `fase8c-enlaces-vivos.py` a las landings de producto.
- Piezas de captación del blog con volumen y sin dueño (Verifactu 74.000, convenio 1.600, hojas de reclamaciones 1.300, desperdicio 390): sesión de contenidos web con `bridge.py`.
- B6: medir con GSC (`page × query`) los 5 posts y las 5 páginas de rol, y el tamaño del segmento Resend, para saber cuánto vende cada canal.
- RD del registro horario: si se publica este mes, changelog 1.1 del manual y del Kit de Gestión de Personal.

Via: Claude Code
