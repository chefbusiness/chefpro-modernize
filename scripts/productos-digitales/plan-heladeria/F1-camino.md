# Plan de Negocio: Heladería Artesanal (ES, 35 €) · F1: camino de construcción
> Sesión Claude Code, 25-oct-2026. Arquitecto de F1, una pasada. Producto **NUEVO** (sin 1.x), slug `plan-negocio-heladeria`,
> línea A (local fijo). Medido en el VPS (`main` @ `3e1f1d51`, venv `/root/venv-guias`, salida en `/root/tmp-hel-f1`, ya borrada;
> `git status` vacío). Caso, mercado y normativa: `F1-research-heladeria.md` (otro agente); aquí, el CÓMO y el QUÉ se toca.

## 0. Decisión en tres líneas

1. **Camino del parrillero 2.2, con semilla de la PANADERÍA 2.2**: `semilla_hel.py` copia los dos xlsx LIVE de
   `dl/plan-negocio-panaderia/` (molde A-β + checklist C2, solo lectura), escribe lo que el módulo de contenido no alcanza, y
   `planes-v2_0/main.py --dry-run --origen` + `grupo_a.py` lo reconstruyen con un módulo nuevo
   `planes-v2_0/contenido_plan_negocio_heladeria/a.py`. Word en las 131 ranuras del molde FT ES (como paellero y parrillero).
2. **Cero cambios en código común del motor**: `--producto` acepta cualquier pid; la carpeta de contenido se resuelve sola
   (`main.py:876`, `'contenido_' + pid.replace('-', '_')`); `motor.py:1605` ya sabe acentuar «heladería».
   **NO se añade el pid a `PRODUCTOS` (`main.py:117-128`)**: solo lo usa `demo_moldes`, que exige `len(fuera) == 30`
   (`main.py:749`); con el producto en la lista y su `dl/` creada contaría 32 y la demo saldría roja.
3. **4 entregables, ≈ 45 ficheros de capa de producto** (§5) y **F2 + F3 ≈ 1,75 M** (§8): con la F1 (~1,5 M), ≈ 3,3 M ≤ 5 M.

## 1. Dry-run de control (VPS, 25-oct, línea A en verde hoy)

`CLAUDE_SCRATCHPAD=/root/tmp-hel-f1 main.py --producto plan-negocio-panaderia --dry-run --solo a` → **exit 0 en 21 s**:
idempotencia 0 diferencias · inject_cache 737 fórmulas (678 con caché) + 12 · data_only 689 con valor, 59 «""» por diseño,
0 fallos · `blancos_contaminados` 0 · **gates §9 13/13** · checklist C2 **66 ítems** con desplegable · censo `--fail` 0 defectos ·
demos: anualidad, TIR, **moldes 30/30**, 16/16 hojas protegidas · TODO VERDE. Único pendiente: «2 docx sin A4/autor» (el Word 1.1
de la panadería y su guía de equivalencias, ambos Letter: informativo, no fallo).

**Lo que la panadería 2.2 deja en el libro y el módulo de contenido NO reescribe** (medido celda a celda; lo pisa la semilla):
`Inversión Inicial!A1` «PLAN DE NEGOCIO: PANADERÍA / OBRADOR», **`A2` «Inversión Inicial — España 2026»** (prohibido),
partidas filas **7-25** (19: rótulo A, importe B, nota D, «¿Lleva IVA?» E), `PyG 3 Años!A2`, fijos filas **26-35** (10: Gestoría,
«Mantenimiento hornos…», Marketing, Software, Limpieza, Varios + los 4 FIJOS_EXTRA de la panadería, importe en B y nota en F),
**`PyG!H4` «Pan común sobre la línea (%)» + `H10` = 0,76** (línea partida al 4 %: `grupo_a.py:2296` la escribe y no consta que
la borre sin línea partida), `Punto Equilibrio!A2`, y en el checklist título, fases, 66 tareas e `Instrucciones` (A3 con el pid). Los valores de
`0. Supuestos` también: **`grupo_a` conserva lo verde que trae el libro** (gotcha de `semilla_par._supuestos`), así que la semilla
escribe ahí los SUPUESTOS de la heladería. Las notas de Supuestos (C4…C68), Personal, Instrucciones y la tabla RECALIBRADO sí las
rehace el motor desde el `a.py` (`instrucciones()` limpia el área, `grupo_a.py:4094`).

## 2. Molde de contenido: `a.py` de la PANADERÍA, reescrito al formato compacto del parrillero

| | Panadería (elegida) | Cafetería (descartada) |
|---|---|---|
| Driver | transacción de mostrador | cliente sentado (brunch) |
| `ROTACION` | apagada (`{'activa': False}`) | encendida, techo 3 |
| `COBERTURA` | tienda + **horas de producción antes de abrir** | sin producción |
| IVA | por línea + `IVA_COMPRAS` | todo 10 % |

Una heladería artesana con obrador propio es **obrador + mostrador**: producción por tandas antes de abrir (pasteurizar,
madurar, mantecar, abatir), venta de mostrador y para llevar, y una terraza pequeña que no hace de la rotación de mesa una
métrica útil. Es la panadería, no la cafetería. Del `a.py` de la panadería se toma la **estructura y la mecánica**; los
**textos se reescriben enteros** (sus notas citan la «v1.1», `RECALIBRADO`, `Personal!F7`…). Formato: el del parrillero
(`contenido_plan_negocio_parrillero_asador_eventos/a.py`, 488 líneas, sexto campo = fuente `research §n` / `BOE` / `calibrado D15`).

| Clave | Decisión |
|---|---|
| `CONCEPTO` | `'Heladería Artesanal'` |
| `SUPUESTOS` | **las mismas claves que la panadería**, cada nota reescrita (si una clave falta, su nota de panadería se queda). Delivery: helado en tarrina de litro sí viaja (el valor y la comisión, research) |
| `LINEAS_INGRESO` | 2 líneas (`mix_en_supuestos`): **helado y obrador** (bola, cucurucho, tarrina, para llevar, tartas heladas, polos) / **cafetería y bebidas** (café, horchata/granizado, batidos). Sin línea partida: todo al 10 % (helado, art. 91.Uno.1.1.º LIVA; research lo confirma) |
| `IVA_COMPRAS` | **número** (celda verde, `grupo_a.py:2413`): ponderado de leche, huevos y fruta al 4 % con nata, azúcar, cacao y frutos secos al 10 % (peso: research) |
| `PLANTILLA` | maestro heladero/propietario · heladero de obrador · dependientes **fijos discontinuos** de temporada · refuerzo de fin de semana · suplencias (RC-19). Bruto ≥ SMI en proporción a la jornada |
| `COBERTURA` | `horas_dia` de tienda en temporada, `personas_franja`, **`horas_produccion`/`personas_produccion`** del obrador (las 4 claves de la panadería) |
| `ROTACION` | `{'activa': False}` |
| `VOCABULARIO` | `{'cubierto': 'cliente', 'cubiertos': 'clientes', 'sala': 'mostrador'}` (masculino: sin el arreglo de concordancias que necesitó «transacción»). F2 mide los rótulos del libro generado |
| `INVERSION` / `INVERSION_EXTRA` | `{'imprevistos': ('suprimir', …)}` si la semilla lo trae · `()` |
| `AMORTIZABLE` | **propio** (como el parrillero): `obra` = proyecto, obra, instalación eléctrica/climatización, fontanería y desagües, revestimientos; `maquinaria` = pasteurizador, mantecadora, abatidor, armario de conservación, vitrina de cubetas, cámara, batidora, cafetera, granizadora, mobiliario, TPV; `no` = constitución, licencia, tasas, marca, web, lanzamiento, stock |
| `FIJOS` + `FIJOS_EXTRA = ()` | patrón del parrillero: la semilla escribe rótulo e importe de las filas 26-35 y `FIJOS` pone la nota por rótulo normalizado. Candidatas: gestoría · **mantenimiento de la maquinaria de frío** · marketing · software · limpieza · **tasa de terraza** (en lugar de «Varios», que ya está en variables) · residuos · DDD · SGAE/AGEDI · PRL |
| `UMBRALES`, `ESCENARIOS`, `ESTACIONALIDAD` | research (12 pesos que suman 1,000 con `assert`; temporada mar-oct, pico jul-ago, invierno casi plano o cerrado) |
| `INSTRUCCIONES` | `uso` 6-8 del parrillero (8 = «el Word usa las cifras de este Excel»; **fuera** la línea 8 de la panadería «el Word es el de la versión 1.1») · `referencias` con fuente real del research, nunca «Versión anterior de este kit» |
| `CHECKLIST` / `RECALIBRADO` | `{}` (lo escribe la semilla) / **`()`**: producto nuevo, sin «QUÉ HA CAMBIADO RESPECTO DE LA VERSIÓN 1.1» (`grupo_a.py:4255` no pinta el bloque si está vacío) |

## 3. Carpeta `scripts/productos-digitales/plan-heladeria/` (copias del parrillero con PID y rutas)

| Fichero | Origen | Cambios |
|---|---|---|
| `semilla_hel.py` | `semilla_par.py` | origen `dl/plan-negocio-panaderia/`; `TITULOS_PLAN` (Inversión A1 **y A2**, PyG A2, Punto Equilibrio A2); **19 partidas** en las filas 7-25 (A/B/D/E; el assert de fianza/alquiler/imprevistos pasa a la fila 26+); **10 fijos** en 26-35 (B, y F vaciada); **vaciar `PyG!H4:H11`** (valor y relleno verde); `_supuestos` con el módulo nuevo; docProps `description`/`keywords`; checklist: assert de `Instrucciones!A3` contra `plan-negocio-panaderia` |
| `datos_checklist.py` | el del parrillero (formato) | tareas nuevas (§4) |
| `hel_version.py` + `main_hel.py` | `par_version.py` + `main_par.py` | `MES` = mes del merge (previsto «noviembre 2026»). Versión **2.2**: como los planes EN nacidos del motor 2.2 (bakery, bbq: `version: '2.2'` en el changelog) |
| `ciclo.sh` | el del parrillero | `SCR=/root/tmp-hel-f2/motor`, `--producto plan-negocio-heladeria` |
| `cifras_hel_es.py` | `cifras_par_es.py` | `MAPA` con los rótulos de línea A medidos el 25-oct: `^clientes/día \(media` (tras VOCABULARIO), `^ticket medio sin iva`, `^días de apertura al año`, `^alquiler mensual del local`, `^clientes necesarios al día$` / `(caja)`, `^holgura sobre el equilibrio de caja` (B/C/D = años 1-3), `^cobertura \(contratadas`, `^horas de producción`, más los de PyG, Financiación y Tesorería (iguales). Fuera los derivados de eventos. Gates D15 iguales (DSCR ≥ 1,25, saldo mínimo > 0, cobertura ≥ 98 %, holgura ≥ 15 %, origen-usos 0-5 %) |
| `tandas_docx.py` · `docx_hel_es.py` · `BRIEF-REDACTORES.md` | los del parrillero | §4; sin `fuente_par_11.json` (no hay 1.x): el material es el research |
| `barrido_es.py` | el del parrillero | `RX` = restos FT (camión, ventanilla, generador, aparcamiento, food truck) + **restos panadería** (`panader\|\bpan\b\|boller\|harina\|masa madre\|hornada\|horno de pisos\|amasad\|levadura\|madrugada\|pan común\|superreducido\|transacci`) + prohibidos |
| `gate_restos_ft.py` | **reusar** el de `catering-es-2_0/` | `<carpeta> --rx-extra '<restos panadería>\|plan-negocio-panaderia'`; correrlo **antes** de meter la guía de equivalencias (sale en Letter, como las 51, y su A4 lo cazaría) |

## 4. Word, checklist y entregables

**Word** `plan-de-negocio-heladeria.docx`: molde físico = **docx del FT ES** (`dl/plan-negocio-food-truck/`, 131 párrafos,
10 Heading 1, 0 tablas, 61 ranuras de cuerpo / 6.719 palabras; mapa `business-plans-en-4/docx_es_cat.json`), el mismo de
paellero y parrillero: los índices de `FIJOS`, `ENCABEZADOS` (37…109) e `INDICE` (24-33) valen sin remapear. El de la panadería
tiene la misma rejilla (`business-plans-en-2/docx_es_pan.json`), pero obliga a remapear fijos sin ganar nada.
`docx_hel_es.py` = `docx_par_es.py` **sin `anexo()`**: gate **10 H1**, A4, ≥ 6.000 palabras, 0 tokens, 0 no latinos, 0
prohibidos; docProps `AI Chef Pro`, fecha 2026, `comments` = `aichef.pro/plan-negocio-heladeria`. `FIJOS` 127-129 =
→ Tareas Recurrentes: Heladería Artesanal · → Kit de Escandallos Pro · → Pack Plantillas APPCC.
**2 tandas Sonnet en paralelo**: `hel_es_a` §1-5 (29 ranuras, ~2.950 palabras) · `hel_es_b` §6-10 (32, ~3.770); gemela de formato =
`parrillero-2_2/textos/par_es_{a,b}.json` (la única ES 2.2 con tokens; no hay local fijo 2.2 en ES). `PISTAS` por sección
desde el research. Tokens: ~60 de `cifras_hel_es.py` (`CLIENTES_DIA`, `TICKET`, `DIAS_APERTURA`, `VENTAS_A1-3`, `NETO_A1-3`,
`INVERSION_TOTAL`, `CAPEX`, `PRESTAMO`, `DSCR_MIN`, `SALDO_MINIMO`, `MES_SALDO_MINIMO`, `BE_CLIENTES_DIA`(+`_CAJA`), `BE_INGRESOS`,
`HOLGURA_CAJA`(+`_A2/_A3`), `PAYBACK` (texto), `COBERTURA_HORAS`, `PLANTILLA_PERSONAS`, `MANTECADORA`, `VITRINA`, `ALQUILER_MES`,
`ESC_PES/OPT_*`…). Prohibidos del brief: «España 2026», «validad», «freelance», «carné de manipulador» (salvo «ya no existe»),
«tarifa plana» con cifra, «CNAE» como trámite, RGSEAA para el minorista, restos FT y panadería. **No repetir la errata del Kit de
Tareas Heladería ES** (24-oct): yemas y grasas van **antes** de pasteurizar, nunca después.

**Checklist** (`checklist-apertura-heladeria.xlsx`): de **`datos_checklist.py`** (como el parrillero), no del `CHECKLIST` del
`a.py`: el de la panadería son reemplazos sobre 66 tareas de panadería, sin sentido en un producto nuevo. Molde C2 de la
panadería (F1-F6 + Instrucciones; cabecera fila 4 `OK · TRÁMITE · RESPONSABLE · PLAZO · NOTAS`; pie «Tareas completadas:»),
pestañas renombradas ≤ 31 caracteres. **~80 tareas en 6 bloques**: F1 Constitución y fiscalidad (12) · F2 Local, obra,
licencia y terraza (15) · F3 Obrador, equipo y registro sanitario (15) · F4 Personal, APPCC y formación (12) · F5 Marca, carta
y captación (13) · F6 Apertura, temporada y 90 días (13). A verificar por el research (fuente primaria): epígrafe(s) de IAE,
registro sanitario autonómico vs RGSEAA si sirve a otros negocios, licencia (inocua o calificada por la potencia frigorífica),
ocupación de vía pública, temperaturas (pasteurización, maduración, conservación, vitrina), ovoproductos pasteurizados, alérgenos
a granel (RD 126/2015), fijo discontinuo (ET art. 16) y Veri\*factu.

**Entregables** en `astro-site/public/dl/plan-negocio-heladeria/` (claves de `PRODUCT_FILES` = las de la panadería):
`plan-financiero-heladeria.xlsx` (`plan-financiero`) · `plan-de-negocio-heladeria.docx` (`plan-negocio`) ·
`checklist-apertura-heladeria.xlsx` (`checklist-apertura`) · `guia-equivalencias-plan-negocio-heladeria.docx` (`guia-equivalencias`).

## 5. Capa de producto (slug nuevo): crear (C), copiar de la panadería (P) o editar (E)

| Fichero | Acción | Gate |
|---|---|---|
| `astro-site/src/data/productos/planes/plan-negocio-heladeria.ts` | P (312 l.): SEO sin «España 2026», hero, 8 testimonios coherentes (avatar, género, nicho), FAQ con «¿Sirve en México…?», BONUS guía (`es-guia-equivalencias.jpg`, 15 €), `stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_HELADERIA'`, cifras medidas del Excel | `sync-product-prices.py --check`, `gate-no-latinos` |
| `astro-site/src/pages/plan-negocio-heladeria{,-access,-library}.astro` | P (37/17/18 l.); sin `alternatesFamilia` (no hay gemelo EN) | `gate-flujo-postpago` D/E-f (3 puertas cripto: las monta `PlanNegocioLandingPage.astro`) |
| `astro-site/src/islands/library/PlanNegocioHeladeriaLibraryIsland.tsx` | P (16 l.) | idem |
| `src/pages/PlanNegocioHeladeriaDashboard.tsx` · `src/pages/PlanNegocioHeladeriaAccessGate.tsx` | P (135 / 13 l.); 4 tarjetas, guía con Globe | `gate-flujo-postpago` C |
| `astro-site/src/lib/zona-app.ts:80` | E (+1 entrada) | `gate-flujo-postpago` A |
| `netlify/functions/get-download-urls.ts:1229` | E (`PRODUCT_FILES`, 4 claves) | B (disco, git, 200 binario) |
| `netlify/functions/verify-purchase.ts:621` · `resend-access.ts:570` · `admin-generate-access.ts:80` | E (`emailBody` con lo medido: Word de 10 secciones, Excel de 9 hojas, checklist de N tareas, guía) | A |
| `netlify/shared/payment-links.ts:74` · `product-prices.ts:75` | E (link de John) · **regenerar** con `sync-product-prices.py` (35 €) | D (drift con la env) y E |
| Netlify env `VITE_STRIPE_PAYMENT_LINK_PLAN_HELADERIA` (builds) | John crea el Payment Link; Claude da de alta la env + redeploy | D |
| `src/data/products-catalog.ts:486` · `productos-changelog.ts:1940` (`'2.2'`, primera edición) · `productos-digitales-config.ts:577` · `src/pages/AdminGenerateAccess.tsx:74` | E (paridad; el catálogo lo lee `sync-product-prices`) | `sync --check` |
| Hubs ×7 (`ProductosDigitalesHubPage.astro:1032`, `DigitalProductsHubPage{,De,Fr,It,Nl,Pt}.astro` 995/888/889/889/886/888) + gemelo SPA `src/pages/ProductosDigitales.tsx:1015` | E: **quitar la tarjeta de `comingSoon`** y entrar en la **posición 1** con «✨ Nuevo» (lo pierde el Manual del Chef Ejecutivo, 5.º hoy); Mega Pack el último | `hub-gate.py`, `tienda-gate.py` |
| `astro-site/src/lib/sinonimos-buscador.json` | E (+ entrada heladería/gelatería/helados, como la churrería) | buscador del hub |
| `astro-site/public/llms-full.txt:137` (`llms.txt` no lista planes) · `astro-site/src/lib/sitemap-lastmod.json` (+ `/plan-negocio-heladeria` con su fecha) | E | sitemap en el `dist` + reenvío GSC |
| `astro-site/src/data/productos/tareas/kit-tareas-heladeria.ts` | E: enlace al plan (nada huérfano) | revisión |
| `scripts/productos-digitales/equivalencias-es/censo-terminos-es.py:186` y `build_guia_es.py:596` | E: **51 → 52** (el propio gate pide subirlo) + `datos/integracion.json` (ejemplos de la FAQ; copiar el de la panadería) + `terminos.json` si sale un término nuevo (mantecadora, cucurucho/barquillo, tarrina, granizado, horchata) | `build_guia_es.py --check --only plan-negocio-heladeria` |
| Imágenes `astro-site/public/lovable-uploads/ai-gallery/plan-heladeria-*.jpg` ×7 | C (skill `generate-images`); distintas de `tareas-heladeria-*` y `consultor-heladero-*` | `gate-flujo-postpago` D (200) |
| `scripts/productos-digitales/emails/broadcast-plan-negocio-heladeria-lanzamiento-es.html` | C desde `broadcast-kit-tareas-taqueria-lanzamiento-es.html` + bloques del de la panadería 2.2; «Hola, colegas», negro/dorado | `resend-broadcast.py --test` |
| `scripts/productos-digitales/CALENDARIO-V2-SEMANAL.md` + handoff | E | — |

**No se tocan**: `robots.txt` (`/plan-*-access` y `/plan-*-library` ya bloqueados, l. 54-55 y 108-109; `robots-gate.py` lo
confirma), `tienda.ts` (sin gemelo EN), `src/App.tsx` y la landing SPA (no se construyen), `og-meta.ts` (muerta), `tienda-gate.py`
`PLANES_ES` (lista de regresión byte a byte contra producción: se añade tras el LIVE), los posts del blog (carril Cursor: el
banner en `innovacion-en-heladeria-aplicaciones-practicas-de-chatgpt.md` y los 17 que enlazan el kit, se le pasa la nota).

## 6. Gates

**F2 (VPS)**: `ciclo.sh` → `main.py` exit 0 (idempotencia 0, caché, blancos 0, §9 13/13, censo `--fail`, demos 30/30) ·
`cifras_hel_es.py` D15 VERDE · `docx_hel_es.py` (10 H1, A4, ≥ 6.000, 0 tokens) · `tandas_docx.py check` ×2 ·
`barrido_es.py` 0 (xlsx y docx) · `gate_restos_ft.py --rx-extra` 0 · `gate-no-latinos.py` · `censo-entregables.py --only
plan-negocio-heladeria --fail` · `paginas-gate.py` · **una** revisión Opus final (regresiones + legal). **F3**: `sync-product-prices.py --check` · `build_guia_es.py --check --only` · `gate-flujo-postpago.py --base <preview>
--crypto-products all --crypto-exclude pro-prompts-ebook` y después LIVE (A-E-f) · `miselup-gate.py` · `whatsapp-gate.py` ·
`robots-gate.py` · `hub-gate.py` · `tienda-gate.py` · `fase6-gate.py https://aichef.pro/plan-negocio-heladeria` · curl al
checkout cripto (email `qa-…@aichef.pro`, purgar) · sitemap reenviado. Antes de fiarse de un gate LIVE: `git pull` (leen el registro local).

## 7. Plan F2 y F3

**F2 — Entregables** (rama `feat/plan-negocio-heladeria`; worktree de la rama en el VPS)
1. Mac · leer `F1-research-heladeria.md` y firmar una SPEC corta (≤ 80 líneas: caso, mezcla, 19 partidas, 10 fijos,
   plantilla, estacionalidad, vocabulario, prohibidos).
2. Mac · **un** implementador opus: `a.py`, `semilla_hel.py`, `datos_checklist.py` (~80), `hel_version.py`, `main_hel.py`,
   `ciclo.sh`, `cifras_hel_es.py`, `barrido_es.py`.
3. VPS · `bash ciclo.sh` + `cifras_hel_es.py` en bucle hasta D15 verde (calibración de supuestos, máx. 3 vueltas); `barrido` y
   `gate_restos` a 0. scp de los 2 xlsx y de `cifras_caso_es.json` al Mac.
4. Mac · `tandas_docx.py preparar` → **2 Sonnet en paralelo** (`istats` < 60 °C) → `check` ×2.
5. VPS · `docx_hel_es.py` + gates; copia a `public/dl/plan-negocio-heladeria/` **en el worktree** (nunca en `main` del VPS).
6. Mac · **una** revisión Opus de los 3 ficheros + una ronda de arreglos; VPS regenera. Commit + push (`Via: Claude Code`).
**F3 — Producto y lanzamiento**
7. Mac · Sonnet A: ficha + 3 páginas + isla + dashboard + access gate (+ testimonios, FAQ, SEO). Sonnet B: functions ×4,
   `zona-app`, configs, catálogo, changelog, hubs ×8, buscador, `llms-full`, `sitemap-lastmod`, kit-tareas.
8. Mac · 7 imágenes con `generate-images`. VPS · censo de términos (51 → 52) + `build_guia_es.py --only` + `--check`; FAQ de países.
9. Mac · `sync-product-prices.py`; PR draft → preview de Netlify; gates contra el preview.
10. **John · Payment Link de Stripe** (descripción en prosa, sin viñetas; éxito → `/plan-negocio-heladeria-access`). Claude:
    `payment-links.ts` + env + redeploy; merge; gates LIVE; reenviar sitemap.
11. Correo: hueco ES **28-nov 08:00Z** (CALENDARIO); está a > 30 días hasta el 29-oct → borrador por curl + prueba a John +
    routine que lo programa ese día; anotarlo en CALENDARIO y handoff. Commit + push.

## 8. Presupuesto F2 + F3

| Pieza | Quién / dónde | Tokens |
|---|---|---|
| `a.py` + semilla + checklist (~80) + versión/ciclo + cifras + calibración D15 | opus · VPS | 0,45 M |
| Word: pistas + 2 tandas Sonnet ‖ + ensamblado + barrido | sonnet × 2 + opus | 0,30 M |
| Revisión opus final + arreglos | opus | 0,25 M |
| Capa de producto (≈ 45 ficheros, 6 nuevos de copia) | sonnet × 2 · Mac | 0,40 M |
| Imágenes (7) · guía de equivalencias · correo | API / sonnet / orquestador | 0,18 M |
| PR, preview, gates LIVE, merge | orquestador | 0,15 M |
| **Total F2 + F3** | | **≈ 1,75 M** (parrillero 1,6 M est. / 2,2 M real; paellero 2,4 M) → con F1, **≈ 3,3 M ≤ 5 M** |

4 entregables frente a 11 del parrillero, pero capa de producto entera desde cero. Lo dispararía: reconstruir el molde en vez de
copiar la panadería, verificar cita a cita lo que no afirma el producto, más de una ronda de revisión o inventar cifras.

## 9. Riesgos

- **Restos de la panadería** donde el módulo no llega (§1): `PyG!H4/H10`, `Inversión!A2` («España 2026»), fijos, checklist,
  docProps. Los pisa la semilla; `barrido_es.py` y `gate_restos_ft.py` con el regex de §3 lo demuestran a 0. **Sin código común.**
- **Estacionalidad fuerte / cierre en invierno**: el motor arranca la rampa en enero (mes 1 = enero) y reparte las nóminas en 12 + pagas extra
  (`grupo_a.py:3511`): con dependientes fijos discontinuos el invierno sale más caro que en la realidad (conservador). Se dice en
  una nota de Tesorería; si el saldo mínimo cae, se calibra con el fondo de maniobra y los meses de rampa, no tocando el motor; meses a ~0 coherentes con los días de apertura.
- **Concordancia del VOCABULARIO** y rótulos de importe sin palabras de recuento (`motor.RX_RECUENTO`): medir en el primer dry-run.
- **Errata de seguridad**: orden de pasteurización (yemas y grasas antes) en checklist, Word y brief.
- **La guía de equivalencias nace en Letter** (como las 51): coherente con la familia; por eso `gate_restos_ft` va antes de meterla.
- Hallazgos colaterales en LIVE (fuera del alcance, para la cola): la panadería 2.2 conserva `Inversión Inicial!A2` «— España
  2026» en el xlsx y «España 2026» en `seo.description` de su ficha; su `emailBody` (`verify-purchase.ts:625`) promete «60+
  trámites RGSEAA obrador» (son 66 y el registro es el autonómico).
