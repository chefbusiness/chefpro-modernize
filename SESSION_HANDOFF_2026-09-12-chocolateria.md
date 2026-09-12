# Handoff — sesión Claude Code 2026-09-12 (Mac): Pastelería 1.0.1 LIVE + research de «Cómo Montar una Chocolatería» (producto nuevo nº 5)

> Sesión PAR del ciclo alternado. John: «ok nos lanzamos el desarrollo de un nuevo producto digital». Antes de tocar nada nuevo se cerró la
> deuda de la sesión anterior (el fixer de la Guía de Pastelería sin commitear) y después se hizo el research completo del último producto de
> la Hoja 4. **Estado al cierre: research cerrado, PENDIENTE DEL OK DE JOHN; no se ha escrito una línea de producto.**

## 1. Guía «Cómo Montar una Pastelería» — v1.0.1 LIVE y verificada (`0ba5158`, push 11:55, deploy 11:58)

- El handoff del 10-sep decía «fixer a mitad»; medido: estaba al 95 % (35/35 fixes mecanizables aplicados, documentos reensamblados a
  103/37 págs, landing y functions ya con 103/37). Se conservó el árbol tras pasar `gate_libros` 8/8, `verificar_guion` 0 rotas y
  `censo-entregables --fail` 0.
- **Verificación adversarial** (workflow `verificar-fixer-guia-pasteleria`: 3 verificadores por lente A/B/C + lector de regresiones + segundo
  voto; opus; 1,55 M tokens, 20 min): 60 revisiones, 53 RESUELTO, **7 residuos confirmados** y arreglados a mano: A3 (la NOTA de
  `calculadora-capex!Parámetros!E18` decía que los dos libros diferían en 134 € cuando ya coinciden → generador + regen del libro), A13 (tabla
  del anexo seguía con «lo sustituye el art. 30 del RD 1086/2020» → guion:3331), C2 (tabla del bonus 3 imprimía «0» → guion:4199 filas 39-41 +
  nota), C4 (presupuesto de muletillas: guía 15/15, bonus 5/5), C10 («cuatro bloques» eran cinco + párrafo del RD 193/2023), A4 causa raíz
  (`C('Fondo de maniobra calculado', …!Parámetros!B18)` apuntaba al gasto mensual → B19), A7/A10 (banda 30-35 % repetida en dos párrafos
  seguidos del cap. 12 → fundidos), B12 (nota del business plan decía que el IVA «no aparece» en la hoja y sí aparece en las filas 34-35 →
  nota fiel). A19 era un falso positivo del refutador (el art. 17 del RD 1021/2022 sí dice lo que la guía dice). BE-20 también en
  `guia-pasteleria-ids-PS.json`.
- Versión **1.0.1** en guion, portada/pie, landing (`updateNote`) y `productos-changelog.ts` (entrada nueva en lenguaje de cliente).
- Gates: documentos.py 23/23 · paginas-gate 5/5 · censo 0 · tests `test_fila_porcentual` y `test_reparto_puntos` verdes · md5 build = dl en
  los 13 entregables · **LIVE**: `gate-flujo-postpago --only` 13/13 y 0 fallos · `robots-gate --live` 1.208 públicas rastreables / 98
  privadas bloqueadas · `fase6-gate https://aichef.pro` 2 fallos de 2.283 (los dos son el recuento del sitemap contra la baseline congelada del
  cutover: 1.052 entonces, 1.208 hoy; baseline obsoleta del gate, no defecto) · GSC descargó el sitemap el 12-sep 02:08; la landing sigue
  «desconocida para Google» (dos días de vida).
- ⚠️ `documentos.py` es motor COMPARTIDO: sus 5 fixes (regex de %, `omitir_filas`, `sin_numerar`, un solo separador antes del cierre, pie con
  fecha) cambian el pie y el cierre de TODAS las guías cuando se regeneren (Food Cost, Manager, Chef Ejecutivo, gastronómico).
- Residuos aceptados para una 1.1: filas 34-35 de IVA en `plan-financiero!PyG 3 Años` siguen entre TOTAL COSTES FIJOS y el resultado (la
  nota del business plan ya lo explica); `guia-pasteleria-research-L4…md` y `…RESEARCH-2026-09-09.md` siguen diciendo «BP-20» (informes
  históricos; el JSON de ids está corregido); la nota C2 lleva «0,04 €» y «1,07 €» cosidos (igual que la del business plan).
- **Pendientes de John / próximas sesiones:** broadcast de lanzamiento (14-oct 08:00 UTC; HTML en `emails/`; programable desde el 14-sep por
  el tope de 30 días de Resend) · correo del Kit de Tareas Pastelería 2.1 (19-oct; desde el 19-sep) · compra de prueba real.

## 2. «Cómo Montar una Chocolatería» — research cerrado (workflow `research-guia-chocolateria`, 2,35 M tokens, 91 min)

Ficheros en `scripts/productos-digitales/auditorias/`: `guia-chocolateria-research-L1-competencia.md` (216 líneas) · `-L2-serp-demanda.md`
(589) · `-L3-normativa.md` (121 KB, ids `CHN-*`) · `-L4-sector-equipamiento.md` (89 KB, ids `CHS-*`) · `-L5-cliente.md` (517) ·
`-L6-assets.md` (659) · **`guia-chocolateria-RESEARCH-2026-09-12.md` (síntesis, 1.137 líneas)** · **`guia-chocolateria-research-REFUTACION-2026-09-12.md`
(«CORREGIR ANTES»: 8 altas · 14 medias · 6 bajas)**. Script del workflow reutilizable: transcripts de esta sesión
(`workflows/scripts/research-guia-chocolateria-wf_c44ad802-11e.js`), calcado del de Pastelería con el contexto del chocolate.

### 2.1 Lo que el research fija (verificado, con fuente)
- **Demanda**: «chocolateria» 9.900/mes es consumidor; «como montar una chocolateria» 10/mes con AI Overview; la mitad de la SERP es LATAM o
  traducción de EE. UU. y la única guía española de 2026 (plandenegocio.es) pide el «carnet de manipulador» (suprimido en 2010) y sus cuentas
  no suman. GSC por PÁGINA (no por query): 38 URLs de chocolate, 285 impresiones y 6 clics en 90 días. Venta por canales propios.
- **Competencia de pago**: el único libro de negocio es «The Chocolatier's Shop» (Callebaut, 49,90 €, en inglés, sin España ni Excel); en
  español sólo un autoeditado de 2020 desde Venezuela. Toda la formación española enseña a HACER chocolate (Callebaut 4.500 €, ESAH, Torreblanca
  180 €), el único programa con gestión son 19.200 € (BCH) y es de pastelería. Franquicias como ancla: Sven 33.000 € / canon 5.000 · Valor
  150.000 / 24.000 · Chök 200.000 / 30.000 · Maestro Churrero 115.000 / 15.000. **No existe en España una plantilla de escandallo, CAPEX o plan
  financiero para obrador de chocolate.**
- **Marco legal propio del chocolate que NINGUNA fuente gratuita menciona**: RD 1055/2003 (definiciones, % mínimos, grasas vegetales ≤5 %,
  «chocolate a la taza»; sin modificaciones), cadmio (Rgto. 2023/915), **EUDR** (Rgto. 2023/1115 consolidado a 26-12-2025 con el 2025/2650:
  cacao dentro; fecha 30-12-2026 para el «operador posterior», que es lo que es una chocolatería que compra cobertura — el aplazamiento a
  30-jun-2027 del art. 38.3 NO le aplica; ver A1/A2 de la refutación), IAE 644.5 (bombones sin alta industrial SÓLO si se venden en las propias
  dependencias: A3), convenio (no hay estatal localizable; el de Madrid condiciona la fabricación de bombones: D9), Ley 7/2022 (moldes fuera del
  impuesto, 0,45 €/kg).
- **Cifras de portada**: inversión en DOS cifras (núcleo de maquinaria verificado línea a línea 5.740 € con atemperadora de sobremesa → 24.105 €
  profesional de entrada) · 55-120 m² (tipo 60-100) · 1-2 personas · ticket 1,29-1,67 €/bombón, 20-45 € estuche, 25-45 € taller · break-even
  NO va en portada (la única fuente es plandenegocio.es y su aritmética no cuadra).
- **Correcciones de la síntesis a las lentes** (ejemplos): el bug del % y el gate de tipo YA están arreglados (L6 los daba como bloqueantes);
  Pastelería está pusheada y LIVE (L6 la vio sin push porque corrió antes del push); Kaitxo está en Balmaseda, no en Karrantza; Moulin Chocolat
  es hoy de Oriol Balaguer; cámara de chocolate 15-18 °C con fuente (Llevats21, 23-jun-2026); **hallazgo nuevo**: `/usos/consultoria/chocolatero-consultor`
  publica en 7 idiomas una FAQ con «80.000-250.000 €» de inversión y una vitrina a 6.000-18.000 € (la real verificada: 2.685 € sin IVA) — y la
  refutación amplía: son SEIS FAQ del mismo fichero (heladería, chocolatería, pastelería, pizzería, cafetería, panadería), dos de ellas
  contradicen ya a guías de 65 € que se están vendiendo (B1).

### 2.2 Propuesta de producto (síntesis; la refutación pide corregir antes de firmar la SPEC)
- Nombre público «Cómo Montar una Chocolatería» (promesa del hub desde mayo) · catálogo «Guía Chocolatería con Obrador» · slug
  `guia-chocolateria-obrador` (404 hoy; robots.txt ya cubre `guia-*`) · **65 €** (la franja de 65 € son ya OCHO productos) · sin tachado, sin
  ratings, `testimonials.items: []` · nace con NOWPayments (`CRYPTO_PRODUCTS`, scope builds + functions).
- Alcance (a) bombonería artesana con obrador; caso «La Almendra», ~75 m², obrador + tienda a calle. Bean-to-bar como VARIANTE (columna de
  CAPEX + epígrafe cap. 11, sin cifras de maquinaria porque no tienen precio público). Chocolatería de taza y churros como EPÍGRAFE del cap. 01 +
  columna de escenario + párrafo en landing y FAQ (no capítulo, no producto).
- 20 capítulos + anexo, 2 bonus (business plan modelo relleno «La Almendra» + 12 decisiones de apertura), **9 libros de Excel** (D7): 1 capacidad
  de obrador y CLIMA · 2 CAPEX con variantes · 3 ⭐ sensibilidad al precio del cacao · 4 carta y escandallo con denominaciones legales y merma de
  templado · 5 ⭐ vida útil de rellenos y rotación · 6 campañas y VALLE DE VERANO · 7 plan financiero 3 años (motor planes 2.2) con talleres y
  regalo corporativo como hojas · 8 checklist legal con árbol de registro, cadmio y «EUDR: ¿te aplica?» · 9 equipamiento y proveedores de
  cobertura y cacao (dos columnas de entrega).
- Presupuesto: la síntesis dice 13,4-14,6 M; la refutación (A4) recomputa **≈14,7-14,9 M** (la síntesis omitió el guion en A2). Pastelería
  cerró en ≈14,1 M. Con el techo del 15 % → **dos sesiones** (D14).

### 2.3 Las 8 ALTAS de la refutación (todas se resuelven en la SPEC, como en Pastelería §1)
A1 EUDR: la fecha del «operador posterior» es 30-12-2026 SIEMPRE (el 38.3 sólo aplaza a «operadores» micro/pequeños) · A2 el nº de referencia
de la DDS sólo se exige si el proveedor es operador (art. 5.3.a) y falta el 5.3.b (registrar a quién suministras) · A3 el 644.5 sólo vale con
venta en las propias dependencias: excluye online, B2B y corporativo · A4 la tabla de presupuesto no suma (≈14,7-14,9 M reales) · B1 seis FAQ
de `use-cases-content.*.consultor.ts` con inversiones inventadas en 7 idiomas, dos contra guías en venta · C1 el libro 5 duplicaría la tabla de
vidas útiles que `kit-tareas-chocolateria/02-partidas-produccion.xlsx!Moldeado` ya publica con cifras incompatibles (ganache 10-15 días vs
«máximo 8») · C2 tres juegos de temperaturas para el mismo obrador (kit 18-20 °C / research 18-22 °C / vitrina 16-18 vs semáforo 14-17) ·
C3 tres libros declaran salidas que exigen cruzar datos entre libros (prohibido por la convención de familia).

### 2.4 DECISIONES PARA JOHN (D1-D18 de la síntesis; recomendación entre paréntesis)
D1 alcance: bombonería con obrador + taza/churros como epígrafe (sí) · D2 bean-to-bar dentro como variante sin cifras de maquinaria (sí) ·
D3 anotar «Churrería-Chocolatería» como candidato de la siguiente cola (sí, sólo anotar) · D4 «proveedores de cacao» → «de cobertura y cacao»
en la tarjeta (sí) · D5 fecha de revisión del EUDR dentro del documento (sí) · **D6 el `comingSoon` del hub se queda VACÍO**: ocultar la
sección o sembrar el siguiente producto (sembrar; y en cualquier caso guarda `{comingSoon.length > 0 && …}` en el Astro, que hoy sólo la
oculta por JS de cliente) · D7 9 libros (sí) · D8 slot de Resend 24-oct 08:00 UTC (dejarlo ahí: delante van Pastelería 14-oct y su kit
19-oct; programable desde el 24-sep) · D9 convenio: una pasada por el REGCON (0,1 M) y si no, la tabla de Madrid como ejemplo · D10
artesanía: Cataluña con articulado, el resto enlace (sí) · D11 columna «franquicia vs independiente» en el CAPEX con marca y fuente, como orden
de magnitud (sí) · D12/B1 corregir las SEIS FAQ de consultoría en 7 idiomas en el mismo commit del 49 (sí) · D13 5-10 min de voz de John
(precio del cacao y cómo repercutirlo, merma real de templado, caja vs unidad, julio-agosto, talleres) · D14 dos sesiones (sí) · D15 tarjeta del
kit «9 checklists» y dos posts de chocolate con banners de sushi/peruano/asador (arreglar con el 49; `kit-tareas-chef-privado` anuncia 9 y
entrega 7+2 → sesión impar) · D16 cripto desde el día uno (sí) · D17 H1 «Cómo Montar una Chocolatería» + catálogo «Guía Chocolatería con
Obrador» (sí) · D18 no mencionar el retraso de «Junio 2026»; tarjeta real con badge «Nuevo» (sí).

### 2.5 Siguiente sesión (cuando John dé el OK)
A2: verificación legal contra el BOE de los `CHN-*` (EUDR primero, con el consolidado CELEX 02023R1115-20251226) → SPEC v1.0 resolviendo los
28 hallazgos de la refutación uno a uno → `datos_ejemplo.py` «La Almendra» → 9 generadores (copiando `guia-pasteleria/` como
`guia-chocolateria/`; sin tocar `documentos.py`) → guion con `puntos_por_epigrafe` → `verificar_guion.py`. B: redactores por bloque
(`dump_prompts.py` + `check_bloque.py`) → `documentos.py` → refutación de documentos → capa de producto (49 en catálogo, payment-links,
product-prices, functions, zona app, hub sin «Próximamente» vacío, blog, use-cases) → Payment Link de John → gates LIVE → borrador de Resend.

## 3. Térmica y presupuesto
- Pico de 67,4 °C a las 11:36 por `mediaanalysisd` (40-51 % de CPU), no por los agentes; `pkill -STOP mediaanalysisd` y en un minuto 52 °C.
  El vigilante `scripts/termica/watchdog-termico.sh` ahora congela también `mediaanalysisd|photoanalysisd|bird`. Resto de la sesión 47-53 °C.
- Subagentes: verificación 1,55 M + research 2,35 M ≈ **3,9 M tokens** (sesión de research + cierre; la construcción va aparte).

## 4. Continuación de las 16:05 (sesión Claude Code, tras corte por cuota + kernel panic)

> John a las 16:05: «el ordenador se ha apagado por recalentamiento supongo… restaura la sesión y continúa… revisa los registros, logs, jsons» + la regla térmica de siempre (65 °C, istats, nada de Playwright). Grabada otra vez en memoria (`feedback_regla-termica-cpu-65-grados`).

**Qué pasó (reconstruido del journal del workflow y del transcript):**
- 11:39 John delegó las 18 decisiones («decide tú, adelante!») → `scripts/productos-digitales/guia-chocolateria-DECISIONES-2026-09-12.md` (13:42).
- 13:45 → 15:08 workflow `fundamentos-guia-chocolateria` (`wf_7fcee771-183`, 4 agentes): verificación legal (opus, 109 fichas CHN, 22 documentos, gate de literalidad 81/81 con cinco canarios) ‖ censo CHS (sonnet, 115 ids; L4 decía 126 porque contaba cabeceras de tabla) → fusión (sonnet) ‖ SPEC (opus).
- **15:08 «You've hit your session limit · resets 3:50pm»**: el agente de la SPEC fue cortado tras `cat >>` la fila D46 — §0-§1 en disco (213 líneas), **§2-§10 nunca se escribieron**; el workflow acabó `failed: SPEC sin resultado`. La fusión también había abortado: **33 fallos de forma** en el censo CHS (26 fiabilidades `media-alta`/`media-baja` fuera del contrato de 3 niveles + 7 agregados sin URL con fiabilidad ≠ `baja`).
- 15:15 último apunte del transcript. **16:02 kernel panic** (`Kernel-2026-09-12-160212.panic`, SMC cause 5) SIN ningún agente vivo: macOS 13.7.8, con `wakeups_resource.diag` de Chrome Helper (15:04) y Claude Helper (15:52). Al arrancar: `bird` al 91 %, 65,2 °C, carga 33.

**Qué se hizo:**
1. `kill -STOP bird` (fuera del `.frozen` del vigilante para que no lo reanime) + `watchdog-termico.sh` en background + Monitor que avisa a ≥ 63 °C. 65,2 → 60,8 °C en un minuto; resto de la sesión 52-57 °C.
2. Censo CHS saneado sin perder información: `media-alta`/`media-baja` → `media` con «[fiabilidad L4: …]» en `nota`; los 7 agregados (CHS-02, 11, 25d, 39, 41, 47a, 47b: sumas y resúmenes de otros ids con fuente propia) → `baja` con «[AGREGADO sin fuente única — componentes…]». Respaldo del merge apuntado a este scratchpad. **Fusión aplicada: 411 → 635 (109 CHN + 115 CHS), 0 duplicados, 224/224 bien formadas**, `_meta.totales` 376/197/62.
3. D3 anotada en `CALENDARIO-V2-SEMANAL.md` §3 (churrería como candidata, sin hacer ni anunciar). Commit `ca48631` + push a las 16:13 (todo lo recuperado, ANTES de seguir).
4. Workflow `completar-spec-guia-chocolateria` (`wf_cfcafa92-9b8`): un opus anexa §2-§10 + Cierre por secciones (un `cat >>` por sección, para que un corte deje frontera limpia) y después refutador → fixer → re-refutación (máx. 3 rondas), agentes en serie. Los resultados de los agentes del workflow caído (correcciones clave, prohibiciones, dos «PENDIENTE PARA LA SPEC») están en el scratchpad como `resultados-wf_7fcee771.json` y se le pasan al redactor.

**Trampa para la memoria:** el límite de cuota corta a un agente igual que un apagón, pero sin dejar rastro en disco: el fichero queda a medias y el journal dice `failed` sin explicar por qué. Antes de dar por escrito lo que un journal afirme, `wc -l` + cola del fichero contra el molde. Y los ids «bare» (CHS-24, CHS-47…) no existen en el JSON: sólo con sufijo (D44).

## 5. Fase A2 + B1 ejecutada (16:25 → 22:00, sesión Claude Code en el Mac)

| Pieza | Estado | Commit |
|---|---|---|
| SPEC v1.0 completa (§0-§10 + Cierre, 935 líneas, **53 decisiones**, 28/28 hallazgos del research resueltos) | ✅ **LISTO** tras **cinco rondas** de refutación adversarial (23 + 15 + 11 + 5 fixes por agentes; 3 bajas residuales a mano). Informes `auditorias/guia-chocolateria-SPEC-refutacion-2026-09-12{,-r2,-r3,-r4,-r5}.md` | `dd9bfe8`, `7538c23` |
| Juego de datos «La Almendra» (`guia-chocolateria/datos_ejemplo.py`, 4.850 líneas) | ✅ `comprobar()` en verde: 28 refs en 5 familias con denominación legal + matriz 28×8 alérgenos; 12 campañas del kit; 5 canales; 106 ids legales con `gate_legal()`; **8 cruces** entre libros; principal del préstamo **derivado por punto fijo** (60,01 %); margen neto calibrado al **10,05 %** (67 tickets/día) | `7feb146` |
| 9 libros de Excel (`guia-chocolateria/build/*.xlsx` = `astro-site/public/dl/guia-chocolateria-obrador/`, md5 idéntico) | ✅ 5 constructores opus en dos tandas (térmica) · **6.322 fórmulas, 0 sin caché, 0 verdes vacías** · refutación 24 hallazgos (4 altos · 10 medios · 10 bajos) → 23 fixes en los generadores + 1 descartado (B14) · **`gate_libros.py` 9/9 VERDE** (con la comprobación nueva de cero referencias entre ficheros + los 8 cuadres) | `e8bea93` |
| Pipeline reutilizable (`guia-chocolateria/pipeline/`: scripts de los 3 workflows + prompts de datos y guion) | ✅ para calcar en el siguiente producto (VPS) | `66f9c45` |
| Guion `guias-v2_0/guion_guia_chocolateria_obrador.py` + `guia-chocolateria/verificar_guion.py` | ⏳ opus escribiéndolo (arrancó 22:00) | — |
| Verificación independiente de los 23 fixes de los xlsx | ⏳ sonnet (solo lee; informe `auditorias/guia-chocolateria-xlsx-verificacion-fixes-2026-09-12.md`) | — |

**Decisiones del orquestador durante la construcción (no reabren D1-D53):**
- **D53 reformulada**: la guía publica los 8 alérgenos y la humedad 50-60 %; regenerar el Kit de Tareas Chocolatería a 2.1 es **PROPUESTA para John** (≈0,15 M, con broadcast propio → guía al 29-oct si se aprueba), no bloquea el cap. 12 (nota-puente).
- **Maestro Churrero sin cifras** (no tiene ficha `CHS-*`); solo Chök (`CHS-58`) con números en la columna franquicia.
- **Perfiles = nombres de hoja** de `04-tareas-perfiles.xlsx`; el propio kit usa rótulos largos («Maestro Chocolatero / Obrador») en fila 1.
- Unidad de capacidad del paquete: **«bombón equivalente»** (libro 1, 512/día); una caja de 35 es una pieza vendible pero 35+ equivalentes.
- «Meses de colchón» vive **solo en el libro 7**; el libro 2 recibe el fondo de maniobra por el cruce 2 ← 7.

**Trampas nuevas (para la memoria):** `Δ` (U+0394) no es WinAnsi (`barrer_cp1252` lo caza; escribir «salto de temperatura») · un cruce por celda verde puede «cuadrar» contra su propio valor por defecto si los dos constructores siembran distinto (A1: 465 vs 512) — el gate de cuadres compara ahora contra la celda ORIGEN · el vigilante térmico muere a la hora (relanzar en bucle) · el límite de cuota corta a un agente a mitad de `cat >>` sin rastro en disco.

**Presupuesto de subagentes hoy (sesión de las 16:05):** SPEC §2-§10 + 3 rondas 1,75 M · cierre SPEC 0,94 M · datos 0,52 M (+0,03 ajustes) · 9 libros + refutación + fixer 3,06 M · guion y verificación de fixes: pendientes. Acumulado del producto ≈ 3,9 (research + verificación, sesión de la mañana) + 6,3 = **≈10,2 M** antes del guion.
