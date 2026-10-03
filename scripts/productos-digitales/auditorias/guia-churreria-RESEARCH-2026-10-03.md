# RESEARCH CONSOLIDADO — «Cómo Montar una Churrería-Chocolatería»
## Producto digital NUEVO nº 51 · AI Chef Pro · línea «Cómo Montar» (hermana directa de `guia-chocolateria-obrador`)

**Fecha:** 2026-10-03 · **Sesión:** Claude Code (síntesis de F1, política de 3 fases) · **Tamaño:** L · **Techo:** ≤ 10 M de tokens de subagentes (F1 2 · F2 6 · F3 2), parada al +30 % (13 M).
**Fuentes:** las cinco lentes de este directorio, **leídas enteras** (`guia-churreria-research-L1-mercado-cliente.md`, `-L2-serp-demanda.md`, `-L3-normativa.md`, `-L4-sector-equipamiento.md`, `-L5-activos.md`), el research verificado de la hermana reutilizado **por id** (`guia-chocolateria-verificacion-legal-2026-09-12.json|.md`, 109 fichas `CHN-*`; `guia-chocolateria-ids-CHS.json`, 115 `CHS-*`; `guia-chocolateria-RESEARCH-2026-09-12.md` y su refutación), y **verificación propia** contra el repo (`main` en `f23fca98`), **GSC en vivo** (`sc-domain:aichef.pro`, 2026-07-05 → 2026-10-03) y **Resend en vivo** (`list-broadcasts`, 2026-10-03).
**Regla aplicada:** cada cifra lleva fuente (URL o id) y fecha de consulta, o va marcada **«sin fuente»** y no entra. Ids nuevos de este producto: **`CUN-*`** (normativa, L3: `CUN-01…42`) y **`CUS-*`** (sector: `CUS-01…59` de L4, `CUS-M*`/`CUS-V*` de L1, `CUS-D*` de L2). Este documento es research y propuesta: **no contiene contenido de producto**. John delegó nombre, precio y alcance el 20-sep: las decisiones del §15.5 van **numeradas, con recomendación y coste, para que las firme el orquestador**; solo el Payment Link de Stripe es suyo.

> ### Dieciséis verificaciones propias — siete CORRIGEN o amplían a las lentes (detalle en §16)
>
> 1. 🔴 **AMPLIACIÓN GRAVE A L4 (`CUS-01`), y toca a un producto vivo: el «85-90 %» fantasma de `CHS-31` YA ESTÁ PUBLICADO por la hermana — en dos Excel, no en la guía.** L4 demostró que «85», «90 %» y «85-90» no aparecen en la página de Loomis Pay que `CHS-31` cita, y supuso que la hermana «podría citarlo en cap. 01, FAQ o landing». Medido hoy: **no está** en el texto de la guía (`grep` sobre `guia-chocolateria/build/docs/txt/*.txt`: 0 coincidencias) **ni** en la ficha de la landing (`guia-chocolateria-obrador.ts`: 0). **Sí está** en `calculadora-capex-chocolateria.xlsx` (hoja «Variante del Formato»: «el margen bruto del churro es del 85-90 % (CHS-31)», que sale de `datos_ejemplo.py:2301`) y en `plan-financiero-3-anos-chocolateria.xlsx` (hoja «PyG 3 Años», `sheet4.xml`: «se cita entre el 85 y el 90 %»). Dos entregables vendidos publican una cifra que su fuente no dice. → **D7**.
> 2. ✅ **CONFIRMO a L5 celda a celda el veredicto por ratio de la hermana.** `plan-financiero-3-anos-chocolateria.xlsx!PyG 3 Años` (openpyxl, `read_only`, `data_only`): resultado neto 17.268,87 € → **20.043,54 €** (+2.774,67 €) y margen neto 8,674 % → 8,605 %; `B68` = «La taza y los churros restan: con estos supuestos te ocupan sala y personal para nada». La fórmula compara `C67>B67` (porcentajes). Esta guía dirá que la churrería-chocolatería es viable: **el comprador de las dos leería una contradicción de mensaje**. → **D7**.
> 3. 🔴 **CORRECCIÓN A L3 (`CUN-33`): SÍ hay un convenio provincial que nombra las masas fritas, y está en casa.** L3 concluye «no se ha localizado ningún convenio propio de churrerías» tras revisar boletines. `CHN-93` (`guia-chocolateria-verificacion-legal-2026-09-12.md:216`, REGCON, nivel A) ya recoge **Toledo 45000145011981 «MAZAPÁN, MASAS FRITAS, CONFITERÍAS Y CHOCOLATES», vigencia 01/01/2025-31/12/2026**. Lo correcto es: «ningún convenio nombra la palabra *churrería*; al menos uno provincial nombra las *masas fritas*». El copy **no puede** decir «no existe convenio de churrerías» (§15.2).
> 4. 🔴 **CORRECCIÓN A L5 en la base del presupuesto: la hermana tuvo 45 bloques de redacción, no 40.** Contados en `guion_guia_chocolateria_obrador.py`: guía **27** bloques en 21 entradas (37.900 palabras de presupuesto), business plan **6**, bonus **12**. 7,3 M / 45 = **0,162 M por bloque**, no 0,18. Y la desviación real de palabras, medida con PyMuPDF sobre los PDF vendidos: guía **59.334 palabras en 111 págs (534,5 pal/pág), +57 % sobre el presupuesto**; bonus **17.002 palabras en 34 págs, +62 %** sobre 10.500. Es la calibración que usa el §10.
> 5. ✅ **AMPLÍO a L5 la contradicción interna del post `ia-churrerias-guia-completa.md`: falla por los DOS extremos.** L5 vio que los suelos de su tabla de inversión suman 26.000 € y el post publica «12.000» como mínimo. Sumados los techos (`:52-58`: 17.000 + 8.000 + 6.000 + 15.000 + 1.500 + 15.000) dan **62.500 €** y el post publica **50.000** como máximo (`:60`). El «total orientativo 12.000-50.000» no sale de su propia tabla por ningún lado.
> 6. ✅ **Resend confirmado por API, con un matiz que L5 no podía ver.** `list-broadcasts` (2026-10-03): la cola ES programada termina en **Taquería, 29-oct 08:00Z** (antes: Panadería 4-oct, Food Truck 9-oct, Pastelería 14-oct, Kit Pastelería 2.1 19-oct, Chocolatería 24-oct). **Escandallos 2.1 (3-nov) y Kit Chocolatería 2.1 (8-nov) solo existen en el calendario** (`CALENDARIO-V2-SEMANAL.md:222-223`), no en Resend. El hueco del 13-nov es correcto **si** esos dos se programan; si el kit 2.1 no sale, 8-nov. → **D14**.
> 7. 🔴 **HALLAZGO NUEVO sobre `pack-appcc/09-control-aceite-fritura.xlsx`: además del conflicto de los 180 °C (R5 de L5), choca con la acrilamida.** `Instrucciones!B14` dice «Temperatura máxima de fritura **recomendada**: 180 °C» (sin norma) y `Control Aceite!F5` marca **OK** cualquier fritura hasta 180 °C con constantes `180`, `25` y `20` dentro de la fórmula. Para las patatas fritas —que el 644.6 faculta a freír en una churrería (`CUN-09`)— el Rgto. (UE) 2017/2158, anexo II, parte A, pide freír **por debajo de 175 °C** (`CUN-05`). Una churrería que fría patatas a 178 °C saldría «OK» en el Pack y fuera de la buena práctica obligatoria. Y la Orden de 26-01-1989 **no fija temperatura** (L3 §3, art. 6). → **D8** (deuda del Pack, no se arregla aquí).
> 8. ✅ **Confirmo GSC al dígito con L2, por PAGE (la dimensión que la hermana enseñó a usar):** `/blog/ia-churrerias-guia-completa` **4 clics · 133 impresiones · CTR 3,01 % · posición 4,9**; las otras 14 URLs con «churr» son del subdominio legacy (≤ 8 impresiones, 0 clics: no se leen como suelo).
> 9. ✅ **Censo de superficies:** `products-catalog.ts` **50** ids · `payment-links.ts` y `product-prices.ts` **52** claves (50 + los dos EN) · `zona-app.ts` **52** reales (53 coincidencias de `productId:` menos la declaración de tipo de `:31`) · slug `guia-churreria-chocolateria` **libre** en `src`, `astro-site/src`, `netlify` y `_redirects` · `robots.txt` con `/guia-*-access` y `/guia-*-library` en los **5 bloques** (`:44-45`, `:98-99`, `:152-153`, `:206-207`, `:260-261`): nada que tocar.
> 10. ✅ **Corrijo dos datos del encargo:** `comingSoon` tiene **21** tarjetas, no 22 (Astro `:1015-1035`, la nuestra en `:1015`; SPA `src/pages/ProductosDigitales.tsx:997-1019`, la nuestra en `:998`), y el **Kit Gestión de Personal cuesta 14 €**, no 18 (`products-catalog.ts:91`). La franja de 65 € tiene hoy **9** productos (incluida la hermana): este sería el **10.º**.
> 11. ✅ **La tarjeta de «Próximos Productos» NO puede llevar precio sin tocar el componente.** La política de 3 fases pide en F1 «tarjeta con precio en Próximos Productos» (`CALENDARIO-V2-SEMANAL.md:380`), pero el render de `comingSoon` (`…HubPage.astro:1511-1560`) solo pinta `name`, `desc`, dos `tags` y `phase`; ninguna de las 21 tarjetas lleva precio. → **D18**.
> 12. ✅ **Pickaxe:** cero agentes con «churr» en `scripts/astro-migration/fase8c-agentes/catalogo-hub.json`; los afines existen con estos nombres literales: **«Chocolatería Creativa»**, **«Chocolatero Consultor Pro»**, **«Food Truck AI+»**.
> 13. ✅ **Páginas de rol (`src/data/use-cases-content.es.ts`):** `chocolatero` `:1264` y `chocolateria` `:3248` llevan a la hermana en 1.ª posición; `cafeteria-brunch` `:2255` empieza por `guia-pasteleria-obrador`; `:4240` (coffee shop) por `kit-tareas-cafeteria`. Coincide con L5.
> 14. ✅ **El post del tema:** 62 menciones de «churr» (como dice el encargo), **6 preguntas** en el `faq:` del frontmatter (emite `FAQPage`), 3 banners ajenos (`/guia-dark-kitchen`, `/kit-tareas-bar`, `/kit-tareas-restaurante-creativo`) y solo 3 destinos internos (`8-errores-que-destruyen-el-food-cost…` ×2, `como-abrir-restaurante-ia-guia-completa`, `/productos-digitales` ×2). Blog ES: **327** posts, y **ningún otro** con más de una mención de «churrer».
> 15. ✅ **Tamaños del molde (para dimensionar F2):** 9 `gen_*.py` = **18.424** líneas · 5 `_comun_*.py` = **1.773** · `datos_ejemplo.py` **5.039** · guion **5.629** · SPEC hermana **937** · `documentos.py` **2.246** · existe `auditorias/guia-chocolateria-json-merge.py` (molde para fundir `CUN-*`/`CUS-*`) y `scripts/astro-migration/fase8x-sustituir-banner.py`.
> 16. ✅ **La hermana publica 527 € para la chocolatera Ugolini (`CHS-46a`, Equipo H, 12-sep); L4 la ve hoy a 496 € en otro distribuidor.** No es contradicción (dos tiendas, dos descuentos, las dos sin IVA), pero **un concepto = una fuente**: si esta guía nombra la Ugolini, usa `CHS-46a`; su dotación tipo usa otra máquina (Irimar MCH-5, `CUS-37a`).

> ⚠️ **Térmica:** `istats cpu temp` entre tandas: 47,8 → 54,2 → 54,9 → 56,0 → 54,9 → 54,4 → 52,0 → 50,9 → 51,0 °C. Un fichero xlsx cada vez (`read_only`), dos PDF con PyMuPDF uno tras otro. Sin builds, navegador ni Playwright. Ningún fichero del repo modificado salvo este informe; sin commits.

---

## 0. Lo primero: qué demanda hay de verdad y por dónde entra el dinero

**La demanda de apertura es minúscula, pero es la mayor de la familia «Cómo Montar» de obrador dulce.** DataForSEO, España, búsquedas/mes, 2026-10-03 (L2, §1.1):

| Bloque | Keywords | Vol/mes |
|---|---|---|
| **Consumidor** (no es nuestro) | `churros` 165.000 · `churreria cerca de mi` 135.000 · `churreria` 110.000 (local pack, sin AI Overview) · `porras` 12.100 · `tejeringos` 8.100 · `chocolate con churros` 5.400 · `chocolate a la taza` 4.400 (hermana) · `churros sin gluten` 2.900 · `churreria madrid` 2.900 | — |
| **Apertura** (la intención del producto) | `montar churreria` 50 · `como montar una churreria` 30 · `cuanto cuesta montar una churreria` 20 · `abrir / como abrir / poner una churreria`, `negocio de churros`, `rentabilidad`, `plan de negocio`, `licencia churreria` ≤ 10 cada una | **≈ 110-190** (suma no desduplicada) |
| **Equipo y formato móvil** (compra, no guía) | `puesto de churros` 880 · `maquina de churros` 590 · `churreria ambulante` 480 · `maquina churros` 320 · `churrera profesional` 260 · `food truck churros` 70 | — |
| **Franquicia, curso, traspaso** | `churreria franquicia` 70 · `curso de churrero` 40 · `traspaso churreria` 40 · `cafeteria churreria` 480 (intención ambigua) | — |

**Cinco lecturas:**

1. **Filtro de intención validado en 9 de 9 SERP** (L2 §2.1): AI Overview sin local pack ⇒ apertura (`montar una churreria 2026`, `como montar una churreria`, `licencia churreria`, `como poner una churreria` en MX); local pack sin AI Overview ⇒ consumidor (`churreria`, `puesto de churros`, `chocolateria churreria`, `franquicia churreria`).
2. **Fuera de España no hay demanda de apertura**: ≤ 10/mes en MX, CO, AR, CL, PE y EE. UU. en español, también con «poner» en México (L2 §1.2). Lo que hay allí es demanda de **maquinaria** (`maquina de churros` 1.600 en MX y CL, competencia HIGH). La adaptación LATAM va por la FAQ, no por captación.
3. **Ya ocupamos la posición 1** en `montar una churreria 2026` con el post propio (L2 §2.1), y **GSC lo confirma por page** (verificación 8): 4 clics / 133 impresiones en 90 días. **El post es el canal SEO del producto; la landing no lo es.**
4. **«Montar una churrería» es 5× «montar una chocolatería»** (50 frente a 10, contexto de la hermana): es el argumento de negocio de que este producto exista aparte, no un argumento de tráfico.
5. **Volumen pequeño no descalifica** (regla de John del 19-sep): el veto es canibalizar lo LIVE, y aquí no hay nada que canibalizar salvo el post, que se **amplía**, no se duplica (§13).

**Por dónde entra el dinero (como en los productos anteriores):** hub `/productos-digitales` (tarjeta en posición 1, buscador), lista de compradores (broadcast de lanzamiento), el post propio con banners, las páginas de rol (`chocolateria`, `cafeteria-brunch`), la venta cruzada desde la hermana y desde el Pack APPCC/food truck/cafetería, y la plataforma (agentes afines). **No se promete tráfico SEO.**

---

## 1. Bloque 1 — Tipos y sub-conceptos, y la decisión de ALCANCE

### 1.1 Las seis variantes con evidencia (L1 A5, L3, L4 §2, L5 §4.1)

| Var. | Formato | Lo que la separa (con id) | Inversión / entrada con fuente | Estacionalidad | Decisión |
|---|---|---|---|---|---|
| **(a)** | **Local fijo con obrador de masa y consumo en sala/terraza** | Alta en la sala (676 chocolatería / 673 bar) **más** 644.6 si vende al peso para llevar (`CUN-10`, `CUN-14`); **fuera** del Anexo de la Ley 12/2012 (`CHN-49c`); humos a cubierta en Madrid (`CUN-23`); convenio de hostelería (`CUN-31`, `CUN-39`) | Traspasos pedidos con sala **82.000-120.000 €** (`CUS-02`, `CUS-31h/i`); con cafetería 40.000-65.000 € (`CUS-31c/d/g`); dotación núcleo **8.618,35 € sin IVA** (`CUS-59`) | Pico de octubre a marzo, Navidad, domingos (`CUS-29`, `CUS-V17`) | **CASO CENTRAL CIFRADO** |
| **(b)** | Despacho / para llevar (por peso, barrio) | **644.6 dentro del Anexo de la Ley 12/2012: sin licencia previa hasta 750 m²** (`CUN-09`, `CUN-35`, `CHN-49b`); el 644.6 faculta a elaborar churros y patatas fritas en el propio local | Traspaso churrería pura de barrio **16.000-19.500 €** (`CUS-31a/b`); dotación núcleo **4.185,45 € sin IVA** (`CUS-58`) | Mañanas; horario partido o cierre a mediodía (`CUS-V05`, `CUS-48`) | **Columna de escenario** en CAPEX, P&L y checklist |
| **(c)** | Caseta / remolque de feria y temporada | 663.1 con nota propia de churrería (`CUN-11`); 675 o 674.7 con mesas, media cuota si ≤ 6 meses (`CUN-13`); autorización municipal temporal (Ley 7/1996 arts. 53-55, `CUN-20`; **RD 199/2010 derogado**, `CUN-19`); minorista con registro autonómico (`CUN-21`); anexo II cap. III del 852/2004 (`CUN-22`); bombona < 15 kg y un aparato no es instalación receptora (`CUN-28`) | Remolque 3×2×2,10 m **14.800 €**, mini carrito **6.190 €** (sin IVA, `CUS-42`) | **Invertida**: verano y fiestas; Fallas 2026, 146 puestos y 17 días (`CUS-29`) | **Capítulo-epígrafe + checklist + hoja «Punto Muerto por Evento»**, sin caso cifrado; remite al food truck |
| **(d)** | Franquicia frente a independiente | Canon + royalty 4-6 % + 1-2 % publicidad; la parte B del anexo II de acrilamida aplica a las franquicias (`CUN-05`) | Churros Factory 45.000 € · Madrid1883 ~96.000 € · Maestro Churrero desde 115.000 € · Valor 125.000 € · ChurroFácil desde 6.000 € (`CUS-M12…M25`, `§3.7` de L4) | — | **Capítulo comparador** con cifras como «orden de magnitud publicado», sin recomendar marca |
| **(e)** | Churros dentro de una cafetería o bar existente | La freidora cambia humos, licencia y aceite (`CUN-23…26`) | Churrería portátil para exteriores de cafetería **4.190 € sin IVA** (`CUS-42`) | — | **Epígrafe + remisión** a `plan-negocio-cafeteria` / `kit-tareas-cafeteria` |
| **(f)** | Obrador B2B (masa, churro congelado o prefrito) | 419.3 (`CUN-12`) y RGSEAA; «churrería o pastelería que sirve a la cafetería» es el ejemplo literal de actividad **restringida** (`CUN-30`); servir a un inscrito rompe la excepción (`CHN-41`) | Amasadora masa blanda 6.589 €, Inblan AM15 desde 9.425 € (`CUS-35b`); churro congelado **sin fuente** | — | **Fuera**: una línea de «cuándo dejas de ser minorista» |

### 1.2 Por qué (a) y no (b) como caso central

Las cinco lentes recomiendan (a) y ninguna lo discute. Tres razones que se refuerzan: **(1)** es el negocio que describe la tarjeta publicada («chocolate a la taza y churros: local, obrador, carta…», `…HubPage.astro:1015`) y el que define la venta («el 80 % del negocio se centraba en chocolate con churros», `CUS-V08`); **(2)** los comparables con cifras son de ese formato (`CHS-37a/b/c`, `CUS-02`, `CUS-31c-i`); **(3)** es el formato más difícil, y el que tiene la variante (b) como simplificación: con (a) cifrado, (b) sale como «lo que quitas», no al revés. **La normativa obliga a que la bifurcación (a)/(b) sea la primera fila del checklist**: la sala y el despacho se abren por regímenes distintos (`CUN-35`).

### 1.3 La frontera con la hermana, decidida en las dos direcciones

La hermana (`guia-chocolateria-SPEC.md`, D1/D3) dice que la chocolatería de taza y churros es «OTRO negocio» y lo argumenta con el Anexo de la Ley 12/2012 (`CHN-49/49b/49c`). **Esta guía lo confirma y lo completa sin contradecirlo**: el 676 sigue fuera del Anexo; lo nuevo es que el **despacho 644.6 sí está dentro** (`CUN-09`, `CUN-35`), cosa que la hermana no afirma ni niega. Espejo en el cap. 01: «la bombonería es OTRO negocio» → enlace a la hermana. **Lo que obliga a tocar la hermana es un error suyo, no una contradicción de criterio**: el 85-90 % y el veredicto por ratio (verificaciones 1 y 2, **D7**).

### 1.4 Los errores de método de lo gratuito que la guía corrige

1. **Cifras circulares**: Hostelmarkt y ASEST usan los mismos tramos (5-15 / 20-50 / 50-100 k€) y ASEST y Envanature los mismos 4.500-5.000 €/mes (L1 A3): nadie ha hecho cuentas propias.
2. **Ningún CAPEX desglosado** ni punto de equilibrio en raciones/día con personal real (L1 A3; L4 `CUS-05`: Loomis da 2.400-3.000 €/mes para tres personas cuando las ofertas reales son 1.300-1.600 €/mes **cada una**).
3. **Estacionalidad sin cuantificar, y contradictoria**: «constante todo el año» (Hostelmarkt) frente a dueños con pico invernal y feriantes con pico estival (`CUS-V17`, `CUS-V03`).
4. **Humos, aceite y PRL ausentes como bloque** en todas las fuentes leídas (L1 A3.4; L2 §2.3, solo por snippets).
5. **Errores normativos repetidos**: carnet de manipulador, «inspección antes de la licencia», RD 199/2010 derogado, Orden 1562/1998 derogada, cifra de licencias sin modelo (L3 §13, E1-E5).

---

## 2. Bloque 2 — Regulación España 2026 (ids `CUN-*` y `CHN-*` reutilizados)

L3 trabajó **contra fuente primaria, una cada vez** (BOE consolidado con su pestaña «Análisis», DOUE en la copia del BOE, BOCM, codigotecnico.org). Lo que ya verificó la hermana se cita por id sin reabrir.

### 2.1 El núcleo que sostiene el producto

| # | Hallazgo | Ids | Nivel |
|---|---|---|---|
| 1 | **Despacho (644.6) dentro del Anexo de la Ley 12/2012** → declaración responsable, sin licencia previa hasta 750 m². La sala (676/673) fuera → manda la ordenanza. Que el obrador de masa anexo vaya dentro de la actividad es **inferencia declarada** (lo faculta la nota del 644.6): confirmarla con el ayuntamiento | `CHN-49b`, `CHN-49c`, `CUN-09`, `CUN-35` | A (+ inferencia marcada) |
| 2 | **El IAE tiene cuatro casillas para el churro**: 644.6 (despacho con elaboración), 663.1 (ambulante, nota propia), 419.3 (industria de masas fritas «churros, buñuelos»), 676/673 (sala); 675 para quioscos en la vía pública. **676 y 675 pagan media cuota si abren ≤ 6 meses**. El 676 no lleva la nota de «vender en el propio establecimiento» de los 671-673 → con venta al peso, **inferencia**: alta también en el 644.6 | `CUN-09…14`, `CHN-73`, `CHN-94` | A (+ inferencia) |
| 3 | **Norma de aceites calentados VIGENTE**: «componentes polares será inferior al 25 por 100» (art. 6.3); su ámbito nombra freidurías, bares, comida para llevar y **ferias en la vía pública** (art. 3). **Arts. 7, 8, 10, 11 y 12 derogados** por el RD 176/2013, entre ellos el 8 («manipulaciones permitidas»); el art. 9 sigue (prohíbe reutilizar ese aceite para alimentos) | `CUN-01…03` | A |
| 4 | **Acrilamida**: «churro» aparece 0 veces en el art. 1.2 del Rgto. 2017/2158 y no tiene nivel de referencia (`CUN-07`: AESAN + CCAA, «no existe un valor de referencia para las masas fritas»). Las **patatas fritas sí**: parte A del anexo II (< 175 °C, espumar, guía de colores); **franquicia, además parte B**. La única mención expresa del churro es la **Recomendación 2019/1888** (no vinculante) | `CUN-04…07` | A / B |
| 5 | **CTE DB-SI**: las freidoras cuentan **1 kW por litro**; cocina de riesgo especial bajo > 20 kW, medio > 30, alto > 50; **extinción automática por encima de 50 kW**; conductos exclusivos EI 30, filtros a > 0,50 m del foco, inclinación > 45° | `CUN-26` | A |
| 6 | **Madrid, OCAS art. 23**: campana con recogida de grasas, conducto a cubierta, limpieza al menos anual; la exención del art. 24 (solo eléctricos ≤ 4 kW) **no ampara una freidora** (inferencia); art. 33: en la vía pública, caseta con filtrado a ≥ 15 m de huecos | `CUN-23…25` | A (Madrid) |
| 7 | **Madrid, horarios**: cafeterías y bares desde las **6:00**; **chocolaterías desde las 8:00**; deroga la Orden 1562/1998 | `CUN-34` | A (Madrid) |
| 8 | **Gas**: una sola bombona GLP < 15 kg con flexible a un solo aparato **no es instalación receptora**; con 35 kg o con dos aparatos, sí (inspección quinquenal, `CHN-48`) | `CUN-28`, `CHN-48` | A |
| 9 | **Clase F** de fuego (aceites de cocina) y agente extintor adecuado (RIPCI) | `CUN-38` | A |
| 10 | **Laboral**: trabajador nocturno = ≥ 3 h entre 22 y 6 (el churrero que entra a las 4-5); máx. 8 h de promedio; **sin horas extra**. ALEH VI nombra freidurías, quioscos y chocolaterías (no «churrerías») y **vigente hasta 31-12-2030**; Madrid, clase C «Chocolaterías», 2025 nivel III **1.160,37 €** de base + plus convenio 191,22 € × 11; **nocturnidad de 0 a 8 h, +25 %** | `CUN-29`, `CUN-31`, `CUN-32`, `CUN-39`, `CUN-40`; corrección: `CHN-93` | A |
| 11 | **Residuos y envases**: aceite de cocina usado comercial, recogida separada obligatoria desde 30-06-2022; vaso de papel plastificado = plástico de un solo uso, se cobra aparte en el ticket desde 1-1-2023; el cucurucho de papel sin plástico queda fuera (inferencia) | `CUN-27`, `CUN-41` | A (+ inferencia) |
| 12 | **Higiene y alérgenos**: servir taza y churros es elaborar comidas preparadas (63 °C, `CHN-51`); gluten siempre, leche en el chocolate, aceite compartido como contaminación cruzada (`CHN-33`); «sin gluten» casi nunca se puede decir (`CHN-37`); formación acreditada, **no carnet** (`CHN-69`) | `CHN-32…34`, `CHN-37`, `CHN-51`, `CHN-69` | A |
| 13 | **Chocolate a la taza** en la carta: el RD 1055/2003 define el **producto** (≥ 35 % cacao, ≥ 18 % manteca, ≤ 8 % harina/almidón), no la bebida servida; con un preparado que no cumple, ni «chocolate a la taza» ni «chocolate» | `CHN-05`, `CHN-11`, `CUN-42` | A (+ propuesta marcada) |
| 14 | **IVA**: churros en sala o para llevar, 10 %; **chocolate a la taza para llevar = zona gris** (con leche, 10 % por inferencia; con agua y preparado azucarado podría leerse como bebida refrescante, 21 %); sin consulta de la DGT | `CHN-71/71c`, `FC-IVA-01…03`, `CUN-17`, `CUN-18` | A / sin fuente para el tipo |

### 2.2 Lo que NO está verificado y no puede entrar como afirmación

Ordenanzas de humos de **Barcelona, Sevilla y Valencia** · ruido y **terrazas** (ninguna ordenanza abierta) · **calificación ambiental autonómica** (GICA, Ley 6/2014 valenciana, Ley 20/2009 catalana) · **correspondencia IAE → CNAE-2025** (solo títulos; `CUN-16` es inferencia; trampa verificada: **47.81 es hoy «vehículos de motor»**, `CUN-15`) · **IVA del chocolate para llevar** · **estado 2026 del convenio de hostelería de Madrid** (vigencia inicial vencida el 31-12-2025; prórroga o denuncia sin verificar) · tablas salariales de otra provincia · **temperatura de fritura del churro** (sin fuente en ninguna lente) · PRL de quemaduras más allá de clase F y campana · RSCIEI para el obrador industrial.

### 2.3 Vigencia a 2026-10-03

Tabla completa en L3 §12. Lo que se mueve: **Rgto. 2017/2158 en revisión con niveles máximos por primera vez** (`CUN-08`, fuente secundaria Eurofins 28-05-2026) · **convenio de Madrid** vencido y sin estado verificado · **RD de registro horario digital** anunciado, no publicado en el BOE (`CHN-68` sigue vigente) · **Verifactu** 1-1-2027 / 1-7-2027 (`CHN-75`) · SMI 2026 (`CHN-67`). Derogadas y vivas en la SERP: **RD 199/2010** (07-08-2021) y **Orden de Madrid 1562/1998**.

### 2.4 Argumento de venta y lo que NO se puede decir

**Sí es argumento (en el cuerpo y en los entregables, no como «verificado contra el BOE» en el copy):** el checklist que bifurca **despacho / sala** y cambia el régimen de apertura; la calculadora **litros de freidora → kW → riesgo → ¿extinción automática?**; la trampa de las 8:00 de Madrid; el aceite con su umbral legal real y lo derogado; la caseta de feria con su checklist.
**No se puede decir** (L3 §14, ampliado): «la ley te obliga a controlar la acrilamida de los churros» · cualquier tipo de IVA para el chocolate para llevar · «necesitas / no necesitas licencia» sin decir el formato · cualquier artículo del RD 199/2010 o de la Orden 1562/1998 · **«no existe convenio de churrerías»** o «la categoría de churrero» (verificación 3) · requisitos de humos fuera de Madrid · «sin gluten» como argumento de carta · «carnet de manipulador» · el art. 8 de la norma del aceite · que el cucurucho «cumple la ley de plásticos» sin conocer su composición · cuotas del IAE · la tasa de Ochavillo (550 €/feria, `CUN-37`) como orden de magnitud nacional · **una temperatura de fritura del churro** mientras no tenga fuente.

### 2.5 Verificaciones que hay que cerrar ANTES del guion (F1, ≈ 0,15 M)

V-01 **Convenio de hostelería de Madrid en 2026** (REGCON/BOCM): ¿prorrogado, denunciado, nuevo? · V-02 **temperatura de fritura del churro** con fuente (guía de prácticas correctas o AESAN); si no aparece, el producto no da cifra · V-03 **notas del INE IAE → CNAE-2025** para 644.6, 676 y 663.1 · V-04 **consulta DGT** sobre bebida de cacao para llevar (si no existe, se queda como parámetro) · V-05 **Toledo 45000145011981**: ámbito funcional literal (¿incluye el despacho de churros?) para el capítulo de convenio.

---

## 3. Bloque 5 — Sector y modelo de negocio (ids `CUS-*` que entran)

### 3.1 El sector no tiene estadística propia, y se dice

**313.827 locales de hostelería** a 1-1-2025, el 8,1 % del total (`CUS-06`, INE DIRCE 2025). **No existe número de churrerías** (`CUS-07`: el CNAE no tiene clase propia) ni consumo de churros en el panel del MAPA (`CUS-08`: 0 apariciones en 645 págs.). La guía lo declara y no inventa un tamaño de mercado (el «3.400 M USD global» es snippet sin método: descartado, L1 anexo).

### 3.2 Ticket y precios publicados (todos con URL, L4 §3.3)

| Id | Dónde | Precio | Fiabilidad |
|---|---|---|---|
| `CUS-15` | La Churrería, Granada (carta propia, 2026-10-03) | **Ración de 6 churros 1,20 €** · chocolate a la taza **2,00 € barra / 2,50 € terraza** · desayuno 3,50 € | alta |
| `CUS-17` | La Artesana, Palma (El Español, 21-10-2025) | **Ración 2,60 €**, media 1,40 € | media |
| `CUS-16` | Churrería Antonio, Vallecas (Moncloa, 21-09-2026) | churro 0,30 € · porra 0,60 € | media-baja |
| `CUS-18` | Rafa, ferias de Galicia (El Español, 05-03-2026) | **docena 2 €** | media-baja |
| `CUS-19` | Chocolatería 1902, Madrid centro (El Español, 22-12-2024) | ~5 € por persona con chocolate | media |
| `CHS-32` / `CUS-20` | Loomis Pay (genérico) | ración de 4 uds 2,50 € · **con chocolate 3,50-4 €** · ticket medio 3 € | media-baja |

**La brecha ×4 entre Granada y el centro de Madrid es el dato**: no hay «ticket de churrería», hay ticket por plaza y por franja → parámetro del lector con estos valores como referencia.

### 3.3 Margen: los dos números, y por qué difieren

`CHS-31` (85-90 %) **va a lista negra** (L4 `CUS-01`, y verificación 1: está publicado en dos xlsx de la hermana). Lo que entra (`CUS-30`): **«márgenes superiores al 60 % en producto»** (Loomis, HTML leído con `curl`) y **«un poquito más del 50 %»** (dueña de La Artesana). Difieren por definición: el primero es materia prima sobre PVP; el segundo, rentabilidad tras más costes. **El libro 3 calcula los dos en la misma hoja** y el P&L usa el del lector (por defecto, 50 %, coherente con el P&L de la hermana, que ya modela la línea de taza y churros al 50 %).

### 3.4 Coste del churro: materia prima con precio actual (Churrofácil, sin IVA, 2026-10-03)

Mix de churros **34,80 €/caja de 24 kg = 1,45 €/kg**; rendimiento declarado por el vendedor 4 kg → ~11,5 kg de masa → **~0,50 €/kg de masa** (`CUS-21`) · mix de porras 0,98-1,35 €/kg (`CUS-22`, base inferida) · aceite **49,00-49,90 €/25 L ≈ 2 €/L** (`CUS-23`) · chocolate a la taza en polvo 6,31-7,19 €/kg (`CUS-24`, base inferida) · cucurucho 0,15 €/ud (`CUS-25`). **Sin fuente:** absorción de aceite, vida del aceite en la freidora, peso de la ración, piezas por kg de masa, churros/hora. Van en **celda verde sin valor por defecto presentado como dato**.

### 3.5 Personal, m², punto de equilibrio, mix y estacionalidad

- **Personal:** (a) 2-3 personas en turno; entrada 5:30-5:45 (`CUS-55`, `CUS-48`) → trabajador nocturno (`CUN-29`). Ofertas reales **1.300-1.600 €/mes bruto** (`CUS-54/55`, JobToday 2026-10-03, media-baja); convenio de Madrid como ejemplo (`CUN-39/40`). (b) 1-2; (c) 2-3 (`CUS-50`).
- **m²:** traspasos de 60-120 m² con sala (`CUS-31`, `CHS-37a/b/c`); puesto de feria 3-8 m². Los «30-50 m²» de un vendedor de mobiliario (`CUS-D7`) son despacho, no (a).
- **Volumen real:** 200-300 raciones entre semana y ~400 en fin de semana (`CUS-27`, La Artesana); hasta 2.000 churros/día y ~40 L de chocolate en días fuertes (`CUS-13`, media-baja).
- **Punto de equilibrio: sin cifra de portada.** El escenario de Loomis (≈ 55 raciones/día, `CUS-28`) usa un personal incoherente (`CUS-05`): entra como **método**, con el personal real.
- **Mix sala / para llevar / feria / B2B:** **sin fuente** cuantitativa. Lo único publicado: «80 % chocolate con churros» de un local (`CUS-V08`) y el reparto Uber Eats/Glovo de Vallecas (`CUS-02`, `CUS-12`). Parámetro.
- **Estacionalidad:** cualitativa (pico oct-dic y Navidad, `CUS-29`; local invierno / feria verano, `CUS-V17`, `CUS-V03`); curva mensual **sin fuente** → 12 coeficientes supuestos y declarados (patrón de la hermana). La serie de Google Ads de L2 **no** vale para el gráfico (orden de meses sin certificar).
- **Valle de verano: tres salidas con evidencia** — carta de verano (helado, horchata, granizado: Chocolatería 1902 y Vigo Churros, `CUS-11`), traspasos «heladería-churrería» (`CUS-31e/f`), ferias (`CUS-29`) o cierre con **media cuota del 676 si abre ≤ 6 meses** (`CUN-10`).

### 3.6 Traspasos (precio PEDIDO, Milanuncios 2026-10-03)

11 anuncios con m² y precio: **mediana ~571 €/m²**, rango 244-1.698. Churrería pura de barrio **16-19,5 k€**; con cafetería **40-65 k€**; con sala y terraza en área metropolitana **82-120 k€** (`CUS-31a-i`, `CUS-02`). Vallecas: **82.000 € negociable, 74 m², 910 €/mes, ~50.000 € de equipos declarados incluidos** (`CUS-02`; compatible con los «82.000-95.000» que publica la hermana en `CHS-37b`). Cuatro anuncios llevan 110-179 días y dos de Barcelona más de dos años: **pedido ≠ cierre**, y así va en la hoja.

---

## 4. Bloques 3 y 4 — Equipamiento crítico y proveedores reales

### 4.1 Equipamiento con base SIN IVA declarada en la ficha (L4 §4, 2026-10-03)

| Equipo | Marca/modelo · id | Precio sin IVA |
|---|---|---|
| Equipo completo de churros (dosificadora + caldero) | Mundigas CH-1-D `CUS-32a` · Repagas `CUS-32b` · Mundigas CH-6 `CUS-32c` | **2.188 €** · 2.198 € · 2.935 € |
| Freidora de churros 25 L | ClimaHosteleria EMPLK002 gas `CUS-33a` · EMPLK003 eléctrica `CUS-33b` | **1.907 €** · 2.053 € |
| Fogón-freidora | Churrofácil 80×80 gas natural 22 L `CUS-33g` · Inhospan FG `CUS-33c` · NTGAS CG80 32 L `CUS-33e` · J.L. Blanco `CUS-33f` | **2.890 €** · desde 2.560 € · 4.422 € · 6.050-8.690 € |
| Dosificadora | manual 2 kg `CUS-34a` · automática CH 5 kg `CUS-34c` · automática 25 kg con variador `CUS-34b` · J.L. Blanco 2-3 L `CUS-34d` | **795 €** · 1.798 € · **2.250 €** · 4.609-9.779 € |
| Amasadora | Churrofácil automática `CUS-35a` · caldero Inhospan CALD50 + pala | **2.550 €** · 247 € + 39 € |
| Campana 1200 con turbina y filtros | Churrofácil `CUS-36a` | **990 €** (conducto, obra y proyecto: **sin fuente**, `CUS-36b`) |
| Chocolatera | Irimar MCH-5 `CUS-37a` · Churrofácil vintage 10 L `CUS-37c` · (Ugolini Delice 3: **527 €**, `CHS-46a`) | **412,70 €** · 845 € |
| Medidor de compuestos polares | Testo 270 BT `CUS-38` | **499 €** (603,79 € con IVA, no se usa) |
| Remolque / carrito / portátil | Churrofácil `CUS-42` | 14.800 € · 6.190 € · 4.190 € |

**Dotación tipo, solo líneas con fuente, todo sin IVA (`CUS-58/59`, L4 §4.1):** A · despacho **4.185,45 €** núcleo (5.014,45 € con Testo y rellenadora) · B · local 60-80 m² **8.618,35 €** núcleo (9.447,35 €). **No es presupuesto de apertura**: faltan cafetera, vitrina calefactada, mostrador, TPV, mobiliario, vajilla, extintor clase F, filtrado de aceite y la obra de humos (`CUS-43`, **sin fuente**). La diferencia con los ~50.000 € de dotación declarados en Vallecas (`CUS-02`) es justo eso. ⚠️ hosteleria10 aplica descuentos del 15-35 % que pueden caducar: **re-comprobar al construir el libro 2**.

### 4.2 Proveedores verificados (con URL abierta)

Churrofácil CB, Linares (mix, aceite, chocolate, cucuruchos, maquinaria, remolques; formación «con la compra de un pallet», `CUS-44a`, `CUS-M09`) · **Harinas Sánchez Palencia** («Harina Especial Churros», `CUS-44b`) · HARIMSA (solo directorio para el producto, `CUS-44c`) · Harinas Costas y Harinera de Tardienta (**solo directorio**, `CUS-44d`: no se publican sin abrir su web) · fabricantes Inblan, J.L. Blanco, Inhospan, Mundigas, Repagas, NTGAS (`CUS-44e`) · HostelShop España, sin precios (`CUS-44f`) · chocolate a la taza Valor y Simón Coll (existencia; formato profesional **sin fuente**, `CUS-44g`) · **gestor de aceite Reseave** (`CUS-44h`). **Sin fuente:** azúcar, café. El listado FEHR-Geregras es de 2015 (`CUS-44i`): reconfirmar o no usar.

---

## 5. Bloque 6 — Casos de referencia reales (con la lección)

| Id | Caso | Dato público | Lección para el lector |
|---|---|---|---|
| `CUS-45` | Chocolatería San Ginés (Madrid, 1894) | Se exporta en kiosco y local pequeño (Lisboa, Austin, Miami, Buenos Aires, Filipinas); **los 3 locales de CDMX cerraron en 2025** (Wikipedia con «better source needed») | La marca viaja pequeña; cautela con «LATAM» |
| `CUS-46` | Chocolatería 1902 (Madrid) | 5.ª generación, chocolate propio, **carta de helados** | Diversificar el verano |
| `CUS-47` | Maestro Churrero (Madrid) | 2 locales, carta «de autor» (rellenos, sin gluten, bites, maki) | El producto innovado sube ticket y redes; inversión de franquicia **en discrepancia** |
| `CUS-48` | Churrería Antonio (Vallecas, 1935) | 5:45-12:30, hasta 2.000 churros/día, churro 0,30 € | Volumen con precio bajo y madrugada |
| `CUS-49` | La Artesana (Palma, 21 años) | 3 personas, 200-400 raciones/día, maquinaria inicial ≈ 3.000 € | **La máquina es barata: la inversión está en el local** |
| `CUS-50` | Rafa (ferias de Galicia, 15 años) | docena 2 €, 3 empleados, «facturamos 60.000 €/año» | La feria tiene techo |
| `CUS-52` | Churrería El Moro (CDMX) | entra en EE. UU. con un socio de distribución (2023, 2026) | Para el lector LATAM/EE. UU.: socio, no franquicia |
| `CUS-V08` | Churrería La Catedral (Valladolid, cierra 2026) | «El 80 % del negocio se centraba en chocolate con churros» | El negocio es la taza con el churro |
| — | La Oriental (Algeciras) cierra tras 67 años por falta de relevo (L1 B2-6) | — | El relevo y el oficio: la guía no enseña a freír y lo dice |

---

## 6. Voz del cliente: dolores, personas, objeciones y vocabulario

**Aviso de honestidad (L1 L-1…L-9):** 24 citas de prensa con URL y fecha, **extraídas vía WebFetch** (resumen por un modelo pequeño): son **evidencia interna, no copy ni testimonios**, y se reabren antes de usarse. Reddit bloqueado, Forocoches 403 (solo títulos de hilo), YouTube sin herramienta. Muestra sesgada a dueños que ya tienen churrería.

| # | Dolor (frecuencia en ~16 fuentes) | Evidencia | Dónde lo resuelve el producto |
|---|---|---|---|
| 1 | **Horas y madrugón** (5) | «10 años abriendo desde las 6 hasta las 9 de la noche» (`CUS-V05`) | Libro 8 + cap. 16 (nocturnidad real, horas del titular) |
| 2 | **Personal y conciliación** (4) | «No damos abasto» con 3 empleados (`CUS-V03`); cierre de domingos para conciliar (`CUS-V11`) | Libros 8 y 5 (refuerzo por pico) |
| 3 | **¿Es rentable?** (4) | 2 cts de coste y 28-30 de venta (`CUS-V01`); el «70 %» del foro (`CUS-V20a`) | Libro 3 (los dos márgenes) y libro 6 |
| 4 | **Estacionalidad** (4) | Pamplona en invierno, Zarautz en verano (`CUS-V17`) | Libro 5 + cap. 17 |
| 5 | **Inversión** (3) | guías sin desglose | Libro 2 + cap. 04 |
| 6 | **Relevo y oficio** (3) | «si no lo aprendes a base de golpes» (`CUS-V13`) | Cap. 01 y FAQ: no es un curso; cómo elegir uno (290-1.290 €) |
| 7 | **Ferias y vía pública** (3) | 400 €/mes de vía pública (`CUS-V02`) | Hoja «Punto Muerto por Evento» + checklist de feria |
| 8 | **Licencia, humos, aceite** (0 voces) | solo oferta y dos noticias (`CUS-D8`, `CUS-D9`) | Se prioriza por el **vacío** de lo gratuito y porque separa legalmente de la hermana, no por demanda |

**Personas (inferencia, L1 B3):** P1 «el de los 25.000 €» (sin hostelería, cree en el 70 %) · P2 «el relevista» (traspaso con maestro saliente) · P3 «el feriante que quiere local» · P4 «el mixto» (churrería en invierno, heladería en verano).
**Objeciones (L1 B5):** «está gratis» · «quiero aprender a freír» · «lo mío es un puesto o un bar» · «estoy en México» · «mi ayuntamiento hace lo que quiere» · «con una churrería ya se gana bien». Respuesta honesta de cada una en §14.

**Vocabulario (L2 §5 + L1 B4) — es-ES manda; equivalencia SOLO en la primera mención de cada documento:** churro (porra = churro grueso; **tejeringo** 8.100, **calentito** 1.000, **jeringo** 880 en España, una sola vez) · churrería-chocolatería · **chocolate a la taza (en LATAM «chocolate caliente»**: MX y CL 5.400 frente a 70 para «a la taza») · churrera / dosificadora (LATAM «máquina de churros»; «manga» sin cifra) · obrador · escandallo (costeo) · montar (en México «poner») · puesto / caseta / remolque (LATAM «carrito») · «bajera» (Navarra) y «darle a la pala» como color, no como término. **Reparto geográfico de los sinónimos: sin fuente**; la regla de redacción no depende de él.

---

## 7. Bloque 8 (parte 1) — Competencia de pago y hueco

- **Libros, plantillas o planes de pago único sobre montar una churrería: no localizados** (Hotmart, Etsy, Gumroad, Udemy; Amazon dio 503). Ausencia **no demostrada** (L1 L-4).
- **Cursos de oficio** con precio verificable: **290 €** (Academia de Churrería, Vallecas, 1 semana, sin Excel; dato de segunda mano porque su dominio redirige a otro, `CUS-M05`) y **1.290 €** (dos anuncios de Madrid, `CUS-M06`). Churrofácil **regala** la formación con la compra de insumos (`CUS-M09`).
- **Franquicias** (agregadores, «declarado por el franquiciador»): 14 marcas de 6.000 € a 320.000 € + IVA (`CUS-M12…M25`). Discrepancias abiertas: Valor 125.000 € frente a «desde 100.000 €»; Maestro Churrero 115.000 € frente a 75.000 € (lista negra, §15.1); Porfirio 300.000 frente a 800.000-1.000.000 MXN.
- **Gratuitas**: 10 fuentes, circulares, sin desglose, sin estacionalidad, sin Excel, sin humos ni aceite (L1 A3).

**Hueco:** una guía de pago único **con números desglosados, estacionalidad por formato y el bloque de fritura (humos, aceite, PRL)**, con hojas de cálculo. El comprador no la compara con otra guía —no la hay—, sino con **gratis** y con **un curso de 290-1.290 €**.

---

## 8. Lo que ya vendemos y la FRONTERA (reglas numeradas)

| # | Activo LIVE (precio, `products-catalog.ts`) | Riesgo | Regla |
|---|---|---|---|
| **R1** | `guia-chocolateria-obrador` (65 €) | Contradecir su argumento legal | La frase del 676 / agrupación 67 se reutiliza **literal** (`CHN-49c`); lo nuevo del 644.6 entra con `CUN-09/35` y su límite dentro |
| **R2** | Ídem | Contradecir sus cifras | Ticket 2,50 → 3,50-4 € con `CHS-32`; margen con `CUS-30`, **nunca** 85-90 %; y se arregla la hermana (**D7**) |
| **R3** | Ídem y `kit-tareas-chocolateria` (12 €) | Pisar la bombonería | Ni bombones ni templado; espejo «la bombonería es OTRO negocio» en el cap. 01 con enlace; la hermana añade el enlace inverso en su FAQ (`guia-chocolateria-obrador.ts:286` y `:349`) |
| **R4** | `pack-appcc` (14 €), `09-control-aceite-fritura.xlsx` | Duplicar el registro de aceite | Esta guía **no** trae registro diario de % CP: calcula **consumo, coste y punto económico de cambio** y cita el Pack como el registro |
| **R5** | Ídem | 180 °C sin norma y < 175 °C de las patatas (verificación 7) | La guía **no da temperatura de fritura** sin fuente (V-02); la corrección del Pack es deuda propia (**D8**) |
| **R6** | `plan-negocio-food-truck` (29 €) · `kit-tareas-food-truck` (12 €) | Copiar el vehículo-cocina | La variante (c) es **caseta/remolque de churros en feria**: sin vehículo, ITV ni generador como eje. Lo propio: **punto muerto por evento** y la estacionalidad invertida, que el food truck no tiene (L5 §2.1). Enlace a los dos para quien va a vehículo |
| **R7** | `kit-escandallos` (12 €), `08-food-truck.xlsx` | Copiar su «canon 60 €/día» | No se reutiliza (supuesto sin id); la tasa es parámetro por evento |
| **R8** | `plan-negocio-cafeteria` (29 €) · `kit-tareas-cafeteria` (12 €) | Pisar la cafetería | (e) = epígrafe + remisión; aquí solo «qué cambia al meter freidora» |
| **R9** | `kit-escandallos` y Guía Food Cost (55 €) | Duplicar el método | Escandallo propio **solo** de masa por kg → piezas, absorción, porra y taza; el método genérico se cita y se vende cruzado |
| **R10** | `kit-tareas-food-truck/04-permisos-eventos-localizaciones.xlsx` | Dice «Registro sanitario del vehículo (RGSEAA)» | La caseta es minorista con **registro autonómico** (`CUN-21`, `CHN-39`). Se anota como **deuda del kit**, no se arregla aquí |
| **R11** | — (variante f) | Obrador B2B | Fuera; una línea con `CHN-41` y `CUN-30` |
| **R12** | Post `ia-churrerias-guia-completa` | Que el post que vende el producto lo contradiga | Corrección quirúrgica de sus cifras en F3 (**D13**) |

**Pipeline:** se reutiliza el molde de la hermana tal cual (`_comun_chocolateria.py` → `_comun_churreria.py`, `_comun_libro_7.py` con el motor `planes-v2_0` 2.2, `gate_libros.py`, `verificar_guion.py`, `dump_prompts.py`, `check_bloque.py`, `documentos.py`, `guia-chocolateria-json-merge.py`). **Trampas ya cazadas que se blindan con gate, no con atención** (L5 §5.4): constantes de Python impresas en el PDF; saltos de línea en celdas que viajan a tablas; bases de IVA mezcladas; «desde» publicado como cerrado; **veredictos por ratio cuando la pregunta es en euros**; dos cifras del mismo concepto entre guía y bonus; parser del catálogo con comentarios; purga de `.astro` al tocar frontmatter; enlaces dentro de celdas; U+202F / U+2011 por escape.

---

## 9. Bloque 7 — La lista DEFINITIVA de entregables

### 9.1 El juego de datos único: «Churrería-Chocolatería La Rueda»

Un solo `datos_ejemplo.py` del que beben los 8 libros, el guion y los dos bonus.

| Campo | Propuesta | Fuente / estado |
|---|---|---|
| Nombre | **«Churrería-Chocolatería La Rueda»** (la rueda es la porra en espiral; paralelo a La Encina, La Clara, La Almendra). ⚠️ **Comprobar en la OEPM antes de cerrar** y evitar las marcas de L1 | supuesto |
| Ciudad | ciudad media española **sin nombre**; los parámetros de Madrid (horario, OCAS, convenio) van como **ejemplo declarado** | patrón de familia |
| Superficie | **75 m²**: obrador de masa a la vista · freidora bajo campana · barra · sala · despacho a calle · aseos y vestuario · almacén; terraza aparte | convergencia `CHS-37a` (75 m²) y `CHS-37b`/`CUS-02` (74 m²) |
| Renta | **910 €/mes** como referencia observada | `CHS-37b` / `CUS-02` |
| Dotación | **variante B de L4** (8.618,35 € núcleo sin IVA) + líneas sin fuente **en blanco** para el lector | `CUS-59` |
| Horario | mañana y tarde a diario; madrugada viernes, sábado y festivos (supuesto); **apertura antes de las 8:00 solo si se clasifica como cafetería/bar** (nota Madrid) | `CUN-34` |
| Plantilla | titular + 2 churreros/as + 1 sala; refuerzo domingos y Navidad-Reyes | supuesto sobre `CUS-54/55`; convenio Madrid clase C como ejemplo (`CUN-39`) |
| Carta | **20 referencias en 5 familias**: churros y porras (ración, docena, kilo) · rellenos · chocolate a la taza (taza, para llevar) · bebidas calientes y frías · carta de verano | PVP de referencia `CUS-15/17`, `CHS-32`; el resto supuesto declarado |
| Materia prima | mix 1,45 €/kg, aceite 2 €/L, chocolate 6,31-7,19 €/kg | `CUS-21/23/24` |
| Sin fuente (verde, sin valor presentado como dato) | absorción de aceite, vida del aceite, piezas por kg, churros/hora, curva mensual, mix de canales | — |
| Variante feria | una caseta, temporada de verano y fiestas, nº de eventos supuesto | supuesto |

**Restricciones de familia** (heredadas): helpers del motor, hoja «Instrucciones» primero, celdas verdes con nota y fecha, **cero constantes en fórmulas** (el patrón de `pack-appcc/09` no se copia), `IFERROR` y `ISNUMBER`, «sin dato» = `""`, **prohibidos `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA` y referencias entre libros**, coma decimal, tildes, `inject_cache.py` + `data_only` + `mapa-<libro>.json`. **Cruces entre libros: celda verde «cópialo del libro N» + fila de cuadre con semáforo** (D7/D32 de la hermana).

### 9.2 Los 8 libros de Excel — arbitraje entre L5 (9), L3/L4 (feria sin cifrar) y el techo

**L5 propone 9, con un libro propio de ferias. L3 y L4 piden que la feria NO se cifre como caso. Mi arbitraje: 8**, con la feria como **hoja** del libro de temporada. Así existe el punto muerto por evento que el food truck no tiene (L5) sin modelar un segundo negocio (L3/L4), y se ahorran ≈ 0,25 M. El libro de turnos **se mantiene**: es el más pegado al dolor nº 1 y tiene norma verificada detrás (`CUN-29/40`).

| # | Fichero | Hojas | Entradas (verde) | Salidas | Decisión que permite | H/N · frontera |
|---|---|---|---|---|---|---|
| **1** | `produccion-hora-punta-y-local.xlsx` | Instrucciones · Parámetros · Equipos y Capacidad · **Freidoras, Potencia y Riesgo** · Demanda por Franja · Cuello de Botella · **Cola del Domingo** · Ficha de Visita a Local | kg de masa/h de churrera, litros y carga por tanda, minutos por tanda, piezas por kg (← 3), raciones/h por franja, personas en línea, **litros de cada freidora** | raciones/h que aguanta el conjunto; equipo que manda; espera y cola en el pico (aritmética simple); **kW computables (1 kW/L) → nivel de riesgo → ¿extinción automática?**; veredicto de la ficha (eliminatorios: conducto a cubierta, gas, potencia) | ¿Una churrera o dos? ¿Ese local sirve? | H (libro 1 hermana sin clima) + N · `CUN-26`, `CUN-23/24` |
| **2** | `calculadora-capex-churreria.xlsx` | Instrucciones · Parámetros · CAPEX por Bloque · **Equipamiento Línea a Línea** · Variante del Formato (local · despacho · caseta · franquicia) · **Franquicia frente a Independiente** · Traspaso vs Obra Nueva · IVA y Tesorería · Proveedores · Resumen | importe mín/máx/tuyo, **base de IVA por línea**, plazo de entrega, variante, traspaso pedido y renta, fondo de maniobra (← 6) | CAPEX por bloque y total; extra por variante; traspaso frente a obra a 5 años; IVA a adelantar; desviación contra lo presupuestado | ¿Cuánto necesito y en qué formato? | H (libros 2 y 9 hermana fundidos) · bloques nuevos: extracción y conducto, fritura y dosificación, sala y terraza · `CUS-32…43`, `CUS-58/59`, `CUS-31`, `CUS-M12…M25` (D11 hermana: orden de magnitud) |
| **3** | `carta-de-apertura-y-escandallo-churro.xlsx` | Instrucciones · Parámetros · **Escandallo por kg de Masa** (churro y porra) · **Absorción de Aceite y Merma** · Chocolate a la Taza · Coste Hora · Ración, Docena o Kilo · Mix y Ticket por Franja y Temporada · **Los Dos Márgenes** · Decisión de Surtido | receta por kg y precios, g por pieza, **% de absorción (sin fuente)**, merma, precio del aceite (← 4), receta de la taza, PVP con IVA, mix de invierno y de verano | coste por pieza, ración, docena, kg y taza; **margen sobre materia prima y margen tras aceite y mano de obra, juntos**; ticket por franja; margen € × rotación | ¿A cuánto vendo la ración, la docena y la taza? | H (libro 4) + N · `CUS-21…25`, `CUS-30`, `CHN-05`, `CUN-42` · ni Kit Escandallos ni Food Cost costean masa frita |
| **4** | `aceite-de-fritura-coste-y-cambio.xlsx` | Instrucciones · Parámetros · Consumo y Reposición · **Punto Económico de Cambio** · Comparativa de Aceites · Escenarios de Precio (aceite y harina) · Gestor de Aceite Usado | capacidad de cuba, reposición diaria, kg fritos/día (← 1), **días entre cambios según TU registro** (← Pack APPCC), €/L de cada aceite, % de subida | € de aceite por ración y por mes; litros al gestor; coste anual por aceite; impacto de la subida en el margen | ¿Qué aceite compro y cuánto me cuesta cambiarlo? | N (reusa «Escenarios de Precio» de la hermana) · `CUN-01…03`, `CUN-27`, `CUS-23`, `CUS-38`, `CUS-44h` · **no es registro APPCC** (R4) |
| **5** | `temporada-franjas-y-ferias.xlsx` | Instrucciones · Parámetros · Peso sobre el Año · Franjas del Día · Capacidad contra el Pico (← 1) · Refuerzo y Tesorería · **El Verano: Cerrar, Carta de Verano o Ferias** · **Punto Muerto por Evento** · Calendario de Ferias | 12 coeficientes (supuestos declarados), % por franja, días, refuerzos; por evento: días, horas, tasa (fija o €/m²·día), m², desplazamiento, montaje, personal, afluencia, ticket | ventas por mes y día; déficit de capacidad en domingos y Navidad-Reyes; resultado de julio-agosto en las tres salidas (con media cuota del 676 si cierra); **raciones para cubrir cada evento y ranking de eventos** | ¿Cierro en verano? ¿A qué ferias voy? | H (libro 6) + N · `CUS-11`, `CUS-29`, `CUN-10`, `CUN-13` · R6/R7 |
| **6** | `plan-financiero-3-anos-churreria.xlsx` | 0. Supuestos · Inversión Inicial (← 2) · PyG 3 Años · Punto de Equilibrio · Escenarios · Personal (← 8) · Tesorería 12 meses (← 5) · Financiación · **Canales y Punto Muerto** (sala · para llevar · ferias) · Instrucciones | clientes/día, ticket sin IVA, días, rampa, **IVA por canal** (10 % `CHN-71c`; chocolate para llevar en verde, `CUN-18`), deuda | P&L, punto muerto mensual y **en raciones/día**, tesorería con valle, DSCR; columna «local con sala / solo despacho» | ¿Aguanta el banco? ¿Qué canal paga los fijos? | H (motor 2.2) · **veredictos en euros, nunca por ratio** (verificación 2) |
| **7** | `checklist-legal-fritura-y-licencias.xlsx` | Instrucciones · Checklist Legal (F1-F6) · **Árbol IAE y CNAE por Formato** · **Régimen de Apertura y Horario** · Licencia, Humos y Gas · Árbol de Registro Sanitario · **Ferias y Venta Ambulante** · Alérgenos y Aceite Compartido · **PRL de la Fritura** · Registro de Formación · Cronograma y Ruta Crítica | estado, coste, fechas; respuestas del árbol (¿consumo en local? ¿para llevar? ¿ferias? ¿suministras a otros?); CCAA y municipio | contador por fase; **epígrafes que te tocan** (644.6 / 676-673 / 663.1 / 675 / 419.3); **¿Anexo de la Ley 12/2012 sí o no?**; aviso de las 8:00 en Madrid; bombona < 15 kg o instalación receptora; clase F; ruta crítica | ¿Qué papel me toca y en qué orden? | H (libro 8 sin cadmio, EUDR ni ruta doméstica) + N · `CUN-09…16`, `CUN-19…28`, `CUN-30`, `CUN-34…38`, `CHN-32…34/39/48/49/69/77/92` · CNAE solo con V-03 cerrada |
| **8** | `turnos-plantilla-y-madrugada.xlsx` | Instrucciones · Parámetros · Cuadrante por Franja · **Horas Nocturnas y Plus** · Coste de Plantilla · Convenio: Cómo Identificar el Tuyo · Horas del Titular | convenio y salario base del lector (ejemplo Madrid), horas por franja, tramos de nocturnidad (+1 % 22-0 h, +25 % 0-8 h en el ejemplo), jornadas | ¿quién es trabajador nocturno (≥ 3 h, 22-6)?; coste anual por puesto y total (→ 6); **horas del titular**; huecos de cobertura | ¿Cuánta gente necesito y cuánto me cuesta abrir de madrugada? | N · `CUN-29`, `CUN-31/32`, `CUN-39/40`, `CHN-67/68`, `CHN-93` (método), `CUS-54/55` |

**Cobertura de la promesa publicada en el hub** («local, obrador, carta, licencias y números»): local → 1 · obrador → 1, 2 · carta → 3 · licencias → 7 · números → 2, 3, 4, 5, 6, 8. **Los cinco sustantivos quedan cubiertos.**

### 9.3 Los dos bonus (par de familia) — y los que se descartan

- **BONUS 1 — `business-plan-modelo-churreria-chocolateria.docx`** (relleno con «La Rueda»): ≥ 3.500 palabras y ≥ 9 tablas coherentes con el libro 6; **el resumen ejecutivo da el resultado neto, el margen y el punto de equilibrio** (defecto B2 de Pastelería). **3 bloques** de redacción (la hermana usó 6).
- **BONUS 2 — «12 decisiones de apertura resueltas»** (PDF + DOCX), **6 bloques de dos decisiones**: 1 · Sala o solo despacho (régimen de apertura, `CUN-35`) · 2 · Traspaso u obra nueva (`CUS-31`, `CUS-02`) · 3 · Equipo completo de 2.188 € o línea separada (`CUS-32/33/34`) · 4 · Gas o eléctrico (`CUN-28`, `CHN-48`, `CUN-26`) · 5 · Mix propio o preparado comercial (`CUS-21`) · 6 · Qué puedes llamar «chocolate a la taza» (`CHN-05`, `CUN-42`) · 7 · Ración, docena o kilo (`CUS-15/18`) · 8 · Abrir antes de las 8:00 (`CUN-34`) · 9 · Cerrar en verano, carta de verano o ferias (`CUN-10`, `CUS-11`) · 10 · Cuánta madrugada asumes tú (`CUN-29/40`) · 11 · Freidora dedicada o compartida (`CHN-33`) · 12 · Franquicia o por tu cuenta (`CUS-M12…M25`).
- ❌ **Bonus de ferias**: duplicaría la hoja del libro 5 y entraría en el territorio del food truck. ❌ **Recetario de masa con tiempos y temperaturas**: cifras que nadie ha ejecutado y riesgo físico (aceite a temperatura sin fuente); la guía **no enseña a freír**.

### 9.4 Resumen del paquete

**1 guía (PDF + DOCX) de 20 capítulos + anexo normativo fechado · 2 bonus (business plan relleno + 12 decisiones resueltas) · 8 libros de Excel con fórmulas vivas.** Pago único, acceso vitalicio al dashboard, actualizaciones incluidas. Tres libros sin molde previo (aceite, turnos y las hojas de fritura/feria de 1, 5 y 7).

---

## 10. Índice: 20 capítulos + anexo, con presupuesto de palabras calibrado

**Calibración medida hoy sobre la hermana (verificación 4):** guía 37.900 palabras de guion → **59.334 publicadas (+57 %, 534,5 pal/pág)**; bonus 10.500 → **17.002 (+62 %, 500 pal/pág)**. Aquí se presupuesta **menos** para entrar en techo: 1.500 por capítulo (1.700-1.800 los de fritura y legales), anexo 1.200.

| Entregable | Guion | Salida realista (+57 % / +62 %) | Gate | La landing publica |
|---|---|---|---|---|
| Guía 20 caps + anexo | **33.000 palabras** | ≈ 52.000 palabras → **≈ 95-100 págs** | `paginas_prometidas: 85` · `min_palabras_cap: 1.200` | la cifra MEDIDA tras construir |
| Bonus 2, 12 decisiones | 12 × 650 = **7.800** | ≈ 12.600 → **≈ 25 págs** | `paginas_prometidas: 22` · `min_palabras_cap: 500` | ídem |
| Bonus 1, business plan | **3.500 + 9 tablas** | 3.500-4.500 → ~18 págs | ≥ 9 `<w:tbl>` | ídem |

`H` hereda estructura y `puntos_por_epigrafe` de la hermana · `N` nuevo · 🔴 legal: lo firma el verificador antes de redactar. **Un bloque por capítulo** (21 + 3 + 6 = **30 bloques**). **`puntos_por_epigrafe` obligatorio** y con fronteras explícitas entre 06, 07 y 10 (el riesgo de desduplicación del Manual del Chef: ≈ 2,2 M).

| # | Capítulo | H/N | Palabras | Libro / hoja | Ids |
|---|---|---|---|---|---|
| 01 | Qué negocio estás montando: seis formatos y cuál te toca (con «la bombonería es otro negocio») | H | 1.700 | 2 · Variante del Formato | `CUN-09…13/35`, `CHN-49c` |
| 02 | El cliente, las franjas y la plaza | H | 1.500 | 5 · Franjas del Día | `CUS-06…08/13/15` |
| 03 | La carta de apertura: churro, porra, chocolate a la taza y para llevar | H+N | 1.500 | 3 · Mix y Ticket | `CUS-09…11/15…20`, `CHN-05`, `CUN-42` |
| 04 | Cuánto cuesta abrir, partida a partida (y lo que nadie publica) | H | 1.700 | 2 · CAPEX por Bloque | `CUS-31/32…43/58/59`, `CHS-37` |
| 05 | El local: metros, zonas, conducto y la ficha de visita | H | 1.500 | 1 · Ficha de Visita | `CUS-31`, `CUN-23/24` |
| 06 🔴 | Antes de firmar: el formato decide el régimen de apertura y el horario | N | 1.800 | 7 · Régimen de Apertura y Horario | `CUN-09/10/14/34/35`, `CHN-49/49b/49c/77` |
| 07 🔴 | Humos, extracción y fuego de aceite: lo que exige la norma y lo que fija el proyecto | N | 1.800 | 1 · Freidoras, Potencia y Riesgo · 7 · Licencia, Humos y Gas | `CUN-23…26/28/38`, `CHN-45/46/48` |
| 08 | Maquinaria: churrera, dosificadora, freidora, amasadora y chocolatera | H | 1.500 | 2 · Equipamiento Línea a Línea | `CUS-32…41`, `CHS-46a` |
| 09 | Producción en hora punta: la cola del domingo | N | 1.500 | 1 · Cola del Domingo | `CUS-26/27/13` |
| 10 🔴 | Alta fiscal y sanitaria de cada formato: IAE, CNAE y registro | H | 1.700 | 7 · Árbol IAE y CNAE · Árbol de Registro | `CUN-09…16/21/30`, `CHN-39/73/94` |
| 11 🔴 | Aceite de fritura: calidad, cambio, coste y gestor | N | 1.800 | 4 (cita Pack APPCC 09) | `CUN-01…03/27`, `CUS-23/38/44h` |
| 12 🔴 | Acrilamida, alérgenos y el aceite compartido | N | 1.600 | 7 · Alérgenos y Aceite Compartido | `CUN-04…08`, `CHN-33/34/37` |
| 13 | Autocontrol, formación y el día de la inspección | H | 1.400 | 7 · Registro de Formación | `CHN-32/51/69` |
| 14 | Escandallo del churro y de la porra: rendimiento, absorción y los dos márgenes | H+N | 1.700 | 3 · Los Dos Márgenes | `CUS-21…25/30`, lista negra `CHS-31` |
| 15 | Proveedores: harina, aceite, chocolate, envase y gestor | H | 1.300 | 2 · Proveedores | `CUS-44a…j`, `CUN-41` |
| 16 | El equipo, los turnos y la madrugada | H+N | 1.700 | 8 | `CUN-29/31/32/39/40`, `CHN-67/68/93`, `CUS-54…56` |
| 17 | La temporada: de octubre a marzo, y qué haces en verano | H | 1.500 | 5 · El Verano | `CUS-11/29/31e/f`, `CUN-10` |
| 18 | Ferias, casetas y venta ambulante | N | 1.500 | 5 · Punto Muerto por Evento · 7 · Ferias | `CUN-11/13/19…22/25/28/36/37`, `CUS-29/42/50` |
| 19 | Franquicia o independiente | N | 1.400 | 2 · Franquicia frente a Independiente | `CUS-M12…M25`, `CUS-03/14` |
| 20 | El plan financiero, el punto de equilibrio y los primeros 90 días | H | 1.700 | 6 · PyG · Punto de Equilibrio | `CHN-71c/75`, `CUN-18` |
| A | Anexo normativo fechado (vigencias y las normas que se mueven) | H | 1.200 | — | §2.3, §15.3 |

**Balance: 11 heredan (incluido el anexo), 3 mixtos, 7 nuevos.** Los H calcan guion y puntos de la hermana cambiando datos: es lo que baja el coste por bloque.

---

## 11. Bloque 8 (parte 2) — Precio y ancla

**Escalera verificada hoy (`products-catalog.ts`, 50 productos):** 9 € ×1 · 12 € ×13 · **14 € ×9** · 18 / 18,50 € ×2 · 24 € ×1 · 29 € ×2 · 35 € ×3 · 39 € ×1 · 45 € ×4 · 55 € ×3 · **65 € ×9** · 85 € ×1 · 89 € ×1.

**Recomendación: 65 €.** (1) **Paridad con la hermana directa** (65 €, LIVE 19-sep), que el hub enseña al lado y con la que comparte comprador y venta cruzada; y con Pastelería y Panadería. (2) **Anclas externas verificables:** 65 € es el **22 %** del curso de oficio más barato (290 €, `CUS-M05`), el **5 %** del de 1.290 € (`CUS-M06`), el **0,5 %** del canon de Churros Factory (12.000 €, `CUS-M15`) y **menos que un mes de alquiler** del local de referencia (910 €/mes, `CHS-37b`). (3) **Paquete de familia completo**: 20 capítulos, 2 bonus y 8 libros (Pastelería salió con 8; el Manager y el Chef Ejecutivo con 7). (4) **No hay comparable de pago** (L1 L-4): no hay techo de mercado que obligue a bajar.

**Sin `priceOld` ni `discountBadge`, sin `aggregateRating` ni `review`, `testimonials.items: []`.** Nace con **Stripe (principal) + NOWPayments (secundario)**: con `CRYPTO_PRODUCTS=all` no se toca la env; hay que regenerar `product-prices.ts` y dar el alta en `zona-app.ts` (regla del 19-sep).

**Alternativas:** **55 €** — cuesta romper la paridad con la hermana justo en el producto que más se venderá junto a ella, y no lo pide ningún comparable; solo se justificaría si F2 recortara el paquete (menos de 8 libros o un solo bonus). **85 €** — colisiona con la Guía Gastronómica y no hay argumento de paquete mayor que la hermana. **49 €** — vetado (precio tachado del Kit de Escandallos).

---

## 12. Nombre, slug, subtítulo, promesa y vocabulario

| Elemento | Propuesta | Nota |
|---|---|---|
| **H1 / nombre de catálogo / banner / email** | **«Cómo Montar una Churrería-Chocolatería»** | Es el nombre de la tarjeta publicada (`…HubPage.astro:1015`, SPA `:998`); la hermana usa su H1 también como nombre de catálogo («Cómo Montar una Chocolatería Boutique & Atelier», `products-catalog.ts:382`). Un solo nombre visible (D17 de la hermana) |
| **Slug** | **`guia-churreria-chocolateria`** → `-access`, `-library` | Libre (verificación 9); patrón `guia-<nicho>`; cubierto por robots en los 5 bloques. **Verificar con `robots-gate.py`, no suponerlo**. Descartados: `guia-churreria` (pierde la desambiguación con la hermana), `guia-como-montar-churreria` (patrón ajeno), `…-obrador` (alarga sin desambiguar) |
| **EN (futuro, solo nombre)** | «Guide: How to Open a Churro & Hot Chocolate Shop» | Propuesta; el nombre EN se elige con datos del mercado cuando toque (regla del 24-sep) |
| **Title** (≤ 60) | «Cómo Montar una Churrería-Chocolatería \| Guía y Excel» (52) | — |
| **Subtítulo** | «Local, obrador de masa, freidora y números: el dossier completo de apertura de una churrería-chocolatería, con los Excel que hacen tus cuentas.» | Lideran los entregables, no el «verificado contra el BOE» |
| **Promesa honesta** | «No te enseña a freír. Te dice qué decidir y en qué orden: si ese local admite una freidora, cuánto cuesta abrir de verdad, a cuánto vender la ración y la taza, cuánta madrugada te toca y qué haces en verano.» | Responde a las objeciones 2, 5 y 6 |
| **Declaración en negativo, arriba** | «No es un recetario ni un curso de churrero, y no sustituye al proyecto técnico de la extracción.» | Corta devoluciones |
| **Aviso de alcance, primera pantalla** | «A fondo: churrería-chocolatería con obrador de masa y sala. Despacho para llevar y caseta de feria, como variantes. Si lo tuyo es la bombonería, es otro negocio: tienes su guía.» | Enlace a la hermana |
| **Límite del copy** | Marco legal **español**; casillas editables; equivalencia LATAM en la primera mención; la FAQ ofrece la adaptación como servicio; **sin siglas en titulares** (IAE, RGSEAA, APPCC, CTE dentro, no en el hero) | Regla del 5-sep |
| **Keywords del cuerpo** | montar una churrería · cuánto cuesta montar una churrería · churrería rentable · licencia de churrería · maquinaria de churrería · porras · chocolate a la taza · traspaso de churrería · franquicia de churrería | No para el slug |

---

## 13. Canales, interenlazado y piezas de captación

### 13.1 Entrantes (cero huérfanas)

| Origen | Acción | Fichero:línea |
|---|---|---|
| **Hub** (Astro **y** SPA) | Quitar la tarjeta de `comingSoon` (quedan 20; la guarda `{comingSoon.length > 0 && (` ya existe en `:1511`), tarjeta real en **posición 1** con «✨ Nuevo» (la 5.ª novedad lo pierde), ItemList JSON-LD | `…HubPage.astro:1015` · `src/pages/ProductosDigitales.tsx:998` |
| **Buscador** | Alias `"/guia-churreria-chocolateria": "abrir montar poner una churreria churros porras tejeringos calentitos chocolate a la taza chocolate caliente freidora dosificadora churrera feria caseta puesto franquicia traspaso licencia"` — sin grupo de sinónimos nuevo | `astro-site/src/lib/sinonimos-buscador.json` (alias de la hermana en `:111`) |
| **Post del tema** | Sustitución quirúrgica de los 3 banners con `fase8x-sustituir-banner.py --producto guia-churreria-chocolateria`: `guia-dark-kitchen` → **esta guía** · `kit-tareas-bar` → **`guia-chocolateria-obrador`** · `kit-tareas-restaurante-creativo` → **`pack-appcc`** (aceite). Más enlace contextual en el cuerpo. Purga `.astro` si se toca el `faq:` y `fase8b-regen-lastmod.py` | `astro-site/src/content/blog/es/ia-churrerias-guia-completa.md:64`, `:123`, `:153` |
| **Rotación general** | Entrada 51 en el catálogo → `fase8e-banners-corpus.py` la reparte por los 327 posts | `src/data/products-catalog.ts` |
| **Páginas de rol** | `chocolateria` (2.ª posición) y `cafeteria-brunch` (variante e) | `src/data/use-cases-content.es.ts:3248`, `:2255` |
| **`PRODUCT_ALIASES`** | «Cómo Montar una Churrería-Chocolatería» | `src/lib/linkify-use-case.tsx`, `astro-site/src/lib/linkify-use-case.ts` |
| **`footerLinks` cruzados** | Desde la hermana, `pack-appcc`, `kit-escandallos`, `plan-negocio-food-truck`, `plan-negocio-cafeteria`; y enlace en la FAQ de la hermana | `guia-chocolateria-obrador.ts:286`, `:349` |
| **Plataforma** | Agentes afines **«Chocolatería Creativa»**, **«Chocolatero Consultor Pro»**, **«Food Truck AI+»** (nombres verificados) | `fase8c-agentes/catalogo-hub.json` |
| **Lista de compradores** | Broadcast de lanzamiento (§13.3) | — |

**Salientes de la landing:** `guia-chocolateria-obrador` (65 €), `pack-appcc` (14 €), `kit-escandallos` (12 €), `plan-negocio-food-truck` (29 €) para la feria con vehículo, `plan-negocio-cafeteria` (29 €) para la variante (e), con `utm_source=landing&utm_medium=cross-sell`. **Deuda anotada, no de este producto:** la página de rol `food-truck` no vende sus propios productos de food truck (L5 §3.2).

### 13.2 Resend

Cola ES confirmada por API hoy (verificación 6): … Chocolatería 24-oct · **Taquería 29-oct (último programado)** · Escandallos 2.1 3-nov y Kit Chocolatería 2.1 8-nov **solo en el calendario** → **hueco 13-nov 08:00 UTC** (8-nov si el kit 2.1 no sale). Programable desde el **14-oct** (tope de 30 días). Borrador con sufijo «— PROGRAMAR 13-nov», saludo «Hola, colegas», negro #111 + dorado #FFD700; recrear = GET → DELETE → POST leyendo el asunto antes.

### 13.3 Piezas de blog (no son este producto; se escriben con `bridge.py` y research propio)

1. **Ampliar** `ia-churrerias-guia-completa` (no crear un segundo «montar una churrería»: canibalizaría la posición 1), con encabezados comparados antes. 2. Medir SERP de **`porras vs churros`** (porras 12.100 + tejeringos 8.100, consumidor) y de **«¿cuántos churros salen de 1 kg de harina?»** (PAA en 7 de 9 SERP, sin volumen medido) antes de decidir. 3. `churreria ambulante` (480) + `puesto de churros` (880) solo si no pisa al food truck. 4. **No** escribir para `churros`, `churreria` ni `churreria cerca de mi`. 5. LATAM: sin captación (≤ 10/mes por país).

---

## 14. FAQ de COMPRA — 12 preguntas

Las de oficio («¿cómo se hace la masa?») y las de consumidor («¿la mejor churrería de Madrid?») quedan fuera. Seis salen del PAA medido (L2 §2.3).

| # | Pregunta | Cómo se responde |
|---|---|---|
| 1 | **¿Esto no está gratis en Google?** | Lo suelto, sí; pero las guías gratuitas **se copian los mismos tramos** y ninguna desglosa el CAPEX, cuantifica la temporada ni trata humos y aceite. Lo que no está: **el orden de decisión y ocho Excel con tus metros, tu carta y tu aceite** |
| 2 | **¿En qué se diferencia de la guía de Chocolatería Boutique & Atelier?** | Aquella es bombonería con obrador, **sin freidora**; esta es churro frito y chocolate a la taza, **con freidora**, y la freidora cambia licencia, humos, gas y aceite. Si haces las dos cosas, las dos se enlazan |
| 3 | **¿Me enseña a hacer churros?** | **No**, y lo decimos antes de que pagues. Para el oficio hay cursos presenciales (290-1.290 € en Madrid); la guía te ayuda a elegir uno y a pedir lo que importa en un traspaso con maestro saliente |
| 4 | **¿Cuánto cuesta montar una churrería?** | No damos un número: damos el modelo que produce **el tuyo**. Verificado: la maquinaria núcleo va de **~4.200 € (despacho) a ~8.600 € (local con sala), sin IVA**, y los traspasos que se piden hoy van de **16.000 a 120.000 €**. Las partidas que nadie publica (obra de humos, cafetera, vitrina, TPV) las presupuestas tú, con las preguntas que hacer |
| 5 | **¿Es rentable? ¿Cuánto gana un churrero?** | Te enseñamos **los dos márgenes** que circulan —más del 60 % sobre materia prima y algo más del 50 % que declara una dueña— y por qué difieren, y el punto de equilibrio **en raciones al día con tu personal real**. El «70 %» de los foros no aguanta una nómina |
| 6 | **¿Cuántos churros salen de 1 kg de harina?** | Depende de la receta y del gramaje, y no hay una cifra pública fiable. El libro de escandallo **parte de tu receta y de tus gramos** (y del rendimiento que declara tu proveedor de mix) y te da piezas, raciones y coste por kilo |
| 7 | **¿Necesito licencia de apertura?** | **Depende del formato**: un despacho para llevar hasta 750 m² va por declaración responsable; con mesas y consumo en el local, manda tu ayuntamiento. El checklist bifurca por ahí desde la primera fila |
| 8 | **¿Sirve para un puesto de feria o un food truck?** | La caseta de feria entra como **variante**, con su checklist y el **punto muerto por evento**. Si vas a vehículo-cocina, el Plan de Negocio Food Truck es tu producto |
| 9 | **Tengo una cafetería y quiero meter churros. ¿Me sirve?** | Te sirve el capítulo de lo que cambia al meter una freidora (humos, potencia, aceite, alérgenos); el negocio de cafetería lo cubren su plan y su kit |
| 10 | **¿Franquicia o por mi cuenta?** | Hay un capítulo con lo que publican las enseñas (de unos miles a más de cien mil euros de inversión, canon y royalty), **como orden de magnitud y con su fecha**, sin recomendar marca |
| 11 | **¿Los Excel funcionan en Google Sheets y en Numbers?** | Sí: sin `INDIRECT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA` ni referencias entre libros; parámetros en celda verde |
| 12 | **¿Sirve fuera de España y qué pasa cuando cambie la normativa?** | El marco legal explicado es el **español**; la estructura económica viaja entera y **la adaptación la ofrecemos como servicio**. Pago único con actualizaciones; anexo con fecha de corte y las normas que ya sabemos que se mueven (acrilamida en revisión, convenio, registro horario, Verifactu) |

**JSON-LD:** `Product` sin `aggregateRating` ni `review` + `FAQPage` + `BreadcrumbList`. Pasar `clasifica()` de `fase8d-faq-duplicadas.py`: vigilar los pares **4/5** (coste / rentabilidad) y **8/9** (variantes).

---

## 15. LISTA NEGRA, riesgos, presupuesto y decisiones

### 15.1 Cifras que NO entran (van a `cifras_ignorar` / `prohibido` del guion)

| # | Cifra | Por qué |
|---|---|---|
| N-1 | **«Margen bruto del churro 85-90 %»** (`CHS-31`) | No aparece en su fuente (L4 `CUS-01`, `curl`). **Y está publicada en dos xlsx de la hermana** (verificación 1) |
| N-2 | «Beneficio 40.000-60.000 €/año» (`CHS-33`, Qamarero) | Circular, sin método; ya en el post propio |
| N-3 | «Montar una churrería cuesta 12.000-50.000 €» (post propio) | Su propia tabla suma 26.000-62.500 € (verificación 5) |
| N-4 | «Licencias y permisos 2.000-6.000 €» (post propio, `:56`) | Sin fuente y sin distinguir despacho y sala |
| N-5 | Personal de Loomis «2.400-3.000 €/mes» para 3 personas (`CUS-05`) y el **break-even de 55 raciones/día** como cifra | Incoherente con las ofertas reales; solo método |
| N-6 | Casos de Loomis (food truck 9.800 €/mes, kiosco 7.200 €) | Escenarios del artículo, no negocios |
| N-7 | «El aceite absorbe un 30 % menos / dura el doble» | Ficha comercial |
| N-8 | **540 kg/h** del M-2020 | Máximo del fabricante, no ritmo |
| N-9 | **Maestro Churrero «desde 75.000 €, 40 m²»** | Discrepa de 115.000 € / 100 m²; hasta abrir su web, solo los 115.000 € «publicados por lexpress el 30-06-2026» |
| N-10 | Valor «3 propios + 29 franquiciados» | Hoy 39 locales, 32 franquiciados (`CUS-03`) |
| N-11 | Valor «≈ 50 % de cuota en chocolate a la taza» · San Ginés «4,90 € con 6 churros» · NTGAS «4.228 €» | Snippet / agregador / buscador contradicho por la página |
| N-12 | Grasa de los churros 23,7-35,2 g/100 g | Churros **de maíz** de un estudio ecuatoriano |
| N-13 | Traspasos de más de 2 años reeditados como precio de mercado | Pedido sin cierre |
| N-14 | «12 euros la docena» · Porfirio 16 M / 13,5 M USD · Jooble «7.306 vacantes» | Errata, dos cifras para el mismo año, incoherente |
| N-15 | «Rentabilidad del 70 %» (título de foro) | Sin fuente; se usa como objeción a desmontar |
| N-16 | Mercado global de churros 3.400 M USD | Sin autor ni método |
| N-17 | Maquinaria «800-1.500 €» (`CUS-D2`) · local «30-50 m²» (`CUS-D7`) | Vendedores, sin verificar; contradicen las fichas |
| N-18 | «Multas de 750-3.000 € por extractor» · «tasa 1,10 €/m²·día» | Snippets sin abrir, municipio sin identificar |
| N-19 | Tasa de Ochavillo 550 €/feria como orden nacional (`CUN-37`) | Pueblo pequeño; solo como ejemplo |
| N-20 | **Temperatura de fritura del churro (180-190 °C del encargo)** · % de absorción · vida del aceite · churros/hora · curva mensual · mix de canales | **Sin fuente**: parámetro sin valor presentado como dato |
| N-21 | Cualquier cita de L1 como **testimonio** | Prensa resumida por WebFetch; reabrir antes de usar y nunca como reseña |

### 15.2 Afirmaciones normativas falsas o caducas, y errores de método

**Normativas:** carnet de manipulador (`CHN-69`) · «inspección de sanidad antes de la licencia» (`CHN-39/43`) · RD 199/2010 como vigente (`CUN-19`) · Orden de Madrid 1562/1998 y «la chocolatería abre a las 6:00» (`CUN-34`) · «necesitas licencia» sin formato (`CUN-35`) · art. 8 de la norma del aceite (`CUN-03`) · «acrilamida obligatoria en churros» (`CUN-04/07`) · «sin gluten» (`CHN-37`) · **«no existe convenio de churrerías»** y «categoría de churrero» (`CHN-93`, `CUN-39`) · CNAE 4781 para un puesto (hoy 47.81 = vehículos, `CUN-15`) · ordenanzas que remiten al RD 199/2010 (Cehegín, `CUN-36`) · RGSEAA para la caseta de feria (`CUN-21`; deuda de `kit-tareas-food-truck/04`) · un tipo de IVA para el chocolate para llevar (`CUN-18`) · humos de Barcelona, Sevilla o Valencia.
**Método:** veredicto por ratio cuando la pregunta es en euros (verificación 2) · mezclar bases de IVA · «desde» como cifra cerrada · capacidad máxima de fabricante como ritmo · precio pedido como precio de cierre · citas de WebFetch como literales · posiciones de GSC de URLs legacy · constantes dentro de fórmulas (el patrón de `pack-appcc/09`) · **copiar «lo verificado» sin reabrir lo que una lente posterior contradice** (`CHS-31` lo reutilizaron L1, L2 y L5 hasta que L4 lo leyó en HTML).

### 15.3 Riesgos, incluidos los de caducidad

| # | Riesgo | Mitigación |
|---|---|---|
| 1 🔴 | Dos productos vivos con defectos que esta guía expone (hermana: 85-90 % y veredicto por ratio; Pack APPCC: 180 °C sin norma y < 175 °C de patatas) | **D7** y **D8**, antes de activar la venta cruzada |
| 2 | **Rgto. 2017/2158 en revisión** con niveles máximos (`CUN-08`) | Fecha de revisión dentro del capítulo 12 y del anexo |
| 3 | Convenio de Madrid vencido sin estado verificado | V-01 antes del guion; tabla como ejemplo en celda verde |
| 4 | Registro horario digital (no publicado) · Verifactu 2027 · SMI | Celda verde y anexo, nunca en la prosa |
| 5 | Ley 12/2012 (Anexo), RDLeg 1175/1990 (modificado el 21-03-2026), Orden de horarios de Madrid, CTE DB-SI | Vigilancia en el anexo; son el esqueleto del capítulo 06-10 |
| 6 | Precios de hosteleria10 con descuento | Re-comprobar al construir el libro 2 y anotar la fecha en cada celda |
| 7 | Vender profundidad LATAM que no tenemos | Primera pantalla + FAQ 12; demanda ≤ 10/mes por país |
| 8 | Presupuesto por encima del techo nominal (§15.4) | Palancas aplicadas desde el diseño; parada a 13 M |
| 9 | Térmica: F2 de tamaño L | **F2 en el VPS** (política de 3 fases); en el Mac, un python cada vez con el vigilante |

### 15.4 Presupuesto estimado por fase (M de tokens de subagentes)

Base medida: la hermana gastó ≈ 16 M en F2+F3 con 45 bloques (0,162 M/bloque real) y 9 libros. Aquí: **30 bloques, 8 libros y menos palabras por capítulo**.

| Fase | Partida | Hipótesis | M |
|---|---|---|---|
| F1 | 5 lentes + esta síntesis | en curso (sin recuento de transcripts) | 1,20-1,35 |
| F1 | Cierre de V-01…V-05 | solo lo abierto; L3 ya trabajó contra fuente primaria | 0,15 |
| F1 | SPEC + refutación (≤ 2 rondas) | molde de la hermana; decisiones ya numeradas aquí | 0,30 |
| F1 | `datos_ejemplo.py` + guion con `puntos_por_epigrafe` | 11 capítulos calcados, 10 con guion nuevo | 0,45 |
| | **Subtotal F1** | | **2,10-2,25** (+5-12 % sobre 2,0) |
| F2 | 8 libros | 5 sobre molde a ≈ 0,20 · 3 nuevos (4, 8 y las hojas nuevas de 1/5/7) a ≈ 0,28 | 1,85 |
| F2 | Refutación de xlsx | gates de script primero; 1 refutador opus + verificador sonnet | 0,40 |
| F2 | Redactores | **30 bloques** × 0,12-0,14 (capítulos más cortos que la hermana) | 3,60-4,20 |
| F2 | Refutación de documentos | r1 opus + r2 verificadores sonnet, sin fixer aparte | 0,90 |
| | **Subtotal F2** | | **6,75-7,35** (+12-22 % sobre 6,0) |
| F3 | Capa de producto calcada + gates + Resend + banners + **D7** (parche de la hermana) | lista de L5 §3.5 | 1,10-1,30 |
| | **TOTAL** | | **≈ 9,95-10,9 M** (central ≈ 10,4 M; por debajo del +30 % = 13 M) |

**Palancas si F1 cierra por encima de 2,25 M:** (1) business plan en **2** bloques (−0,13 M); (2) fundir los capítulos 05 y 09 (local y hora punta) en uno (−0,15 M, coste: la cola del domingo pierde su capítulo); (3) libro 8 dentro de `6!Personal` (−0,25 M, coste: el dolor nº 1 sin libro propio). **No se recomienda** bajar de 12 decisiones ni de 20 capítulos: es lo que sostiene la paridad de 65 €.

### 15.5 Decisiones (delegadas por John el 20-sep; las firma el orquestador)

| # | Decisión | Recomendación | Coste |
|---|---|---|---|
| **D1** | Nombre y slug | **«Cómo Montar una Churrería-Chocolatería»** (H1, catálogo, banner, email) · slug **`guia-churreria-chocolateria`** | Ninguno: es la tarjeta publicada; slug libre |
| **D2** 🔴 | Alcance | **(a) cifrado** (75 m², obrador de masa, sala, terraza, despacho a calle) · **(b) columna de escenario** con su régimen de apertura · **(c) capítulo-epígrafe + checklist + hoja de punto muerto por evento**, sin caso cifrado · **(d) capítulo comparador** con cifras como orden de magnitud publicado · **(e) epígrafe + remisión** · **(f) fuera**, una línea | Un caso de feria cifrado costaría ≈ 0,3 M y pisaría el food truck |
| **D3** | Precio | **65 €**, sin tachado ni ratings; Stripe + NOWPayments | 55 € rompe la paridad con la hermana sin razón de mercado |
| **D4** | Número de libros | **8** (feria como hoja del libro 5; turnos con libro propio) | 9 = +0,25 M; 7 = el dolor nº 1 sin libro |
| **D5** | Bonus | Par de familia: business plan relleno (3 bloques) + 12 decisiones (6 bloques) | Un bonus de ferias duplicaría el libro 5 |
| **D6** | Margen del churro | `CHS-31` a lista negra; publicar **>60 % (Loomis) y ~50 % (dueña)** con su definición, calculados en `3!Los Dos Márgenes`; P&L con el del lector (50 % por defecto) | Ninguno |
| **D7** 🔴 | **Parche de la hermana v1.0.1** | Sustituir el 85-90 % en `calculadora-capex-chocolateria.xlsx` (de `datos_ejemplo.py:2301`) y en `plan-financiero-3-anos-chocolateria.xlsx!PyG 3 Años`; **veredicto de `B68` por euros**; enlace a esta guía en su FAQ (`:286`, `:349`). Changelog v1.0.1, **sin broadcast** (es corrección, no versión nueva); hacerlo en F3, antes de activar la venta cruzada | ≈ 0,15 M; regenerar 2 xlsx con sus gates |
| **D8** | **Deuda del Pack APPCC 09** | Anotarla como trabajo propio (sesión impar): parametrizar 180/25/20 en celdas verdes, etiquetar la temperatura como criterio del operador y añadir el < 175 °C para patatas (`CUN-05`). **Esta guía no da temperatura del churro** salvo que V-02 encuentre fuente | 0 ahora; ≈ 0,1 M cuando se haga |
| **D9** | Convenio | Hostelería de Madrid, clase C, **como ejemplo declarado** y provincia como parámetro; cerrar V-01 antes del guion; método «identifica el tuyo» con `CHN-93` (Toledo, masas fritas) | 0,05 M |
| **D10** | Horario | Fila en el checklist y párrafo en el cap. 06: **en Madrid, la clasificación decide si abres a las 6:00 o a las 8:00**; sin extrapolar a otras CCAA | Ninguno |
| **D11** | IVA del chocolate para llevar | Parámetro verde (10 % por defecto) con aviso «consulta a tu asesor»; nunca en prosa | Ninguno |
| **D12** | Acrilamida | Buena práctica para el churro; **obligación** si se fríen patatas frescas; **parte B** si es franquicia | Ninguno |
| **D13** | Post `ia-churrerias-guia-completa` | En F3: sustituir sus 3 banners (§13.1) **y** corregir quirúrgicamente sus cifras sin fuente (N-2, N-3, N-4) alineándolas con la guía, sin regenerarlo; purga de `.astro` y `regen-lastmod` | ≈ 0,1 M |
| **D14** | Correo de lanzamiento | **13-nov 08:00Z** (8-nov si el Kit Chocolatería 2.1 no sale), programable desde el **14-oct**; confirmar antes que Escandallos 2.1 y el kit 2.1 estén programados | Ninguno |
| **D15** | Sesiones y máquina | 3 sesiones (F1 · F2 · F3), **F2 en el VPS**; parada si se pasa de 13 M | Ninguno |
| **D16** | Páginas de rol | Añadir a `chocolateria` (2.ª) y `cafeteria-brunch`; la de `food-truck`, deuda aparte | Ninguno |
| **D17** | Caso ficticio | «Churrería-Chocolatería **La Rueda**», con comprobación en la OEPM antes del guion | 5 minutos |
| **D18** | Tarjeta con precio en «Próximos Productos» | **No añadir campo de precio en F1**: ninguna de las 21 tarjetas lo lleva y obligaría a tocar los dos componentes gemelos; el precio aparece con la tarjeta real en F3 | Incumple literalmente un punto del DoD de F1, que se anota |
| **D19** | Vocabulario | es-ES; tejeringo/calentito/jeringo y «chocolate caliente» **solo en la primera mención** de cada documento; «poner» (México) una vez | Ninguno |
| **D20** | Blog | Solo ampliar el post propio; medir SERP de «porras vs churros» y «churros por kg de harina» antes de crear nada; fuera del presupuesto del producto | Ninguno |

---

## 16. Lo que este research NO pudo verificar (y lo que SÍ comprobé yo)

**L1:** Reddit bloqueado, Forocoches 403 (solo títulos), Amazon 503, TFG 403; ningún producto de pago de aprendizaje localizado (ausencia no demostrada); `academiadechurreria.es` redirige a un dominio ajeno (precio de 290 € de segunda mano); lexpress sin fecha visible en L1 (L4 la ve: actualizado 30-06-2026); citas resumidas por WebFetch. ❌ **Corregido por mí:** reutilizó `CHS-31` como válido (Parte C-2). Ids `CUS-M32` y `V-ctx` mencionados sin entrada: normalizar en la fusión.
**L2:** orden de los 6 meses sin certificar (no hay curva fiable); `10` = 0-10 y `None` ≠ 0; SERP de México mal localizada; cuerpos del top 10 sin abrir (el hueco de humos/aceite es lectura de snippets); EE. UU. en inglés sin medir. ✅ **GSC confirmado por mí al dígito.** ❌ reutilizó `CHS-31` (§6.4).
**L3:** humos de Barcelona (rate limit), Sevilla y Valencia; ruido y terrazas; calificación ambiental autonómica; notas del INE; IVA del chocolate para llevar; REGCON no repetido; convenio de Madrid 2026; EUR-Lex vacío (DOUE vía BOE). ❌ **Corregido por mí:** `CUN-33` sin `CHN-93` (Toledo, masas fritas).
**L4:** Milanuncios bloqueó fichas (solo 3 enteras); Idealista, InfoJobs, Indeed inaccesibles (salarios con 2 ofertas + Jooble); descuentos de hosteleria10 caducables; sin precio de cafetera, vitrina, TPV, obra de humos; absorción, vida del aceite y ritmo sin fuente. ✅ **Ampliado por mí:** dónde está publicado el 85-90 % en la hermana.
**L5:** sin web; `buscador-report.py` sin `ADMIN_PASSWORD` (búsquedas de «churr» en el hub, sin medir: correrlo en F3); cola de Resend leída del calendario. ✅ **Confirmado por mí:** el veredicto por ratio celda a celda, el censo de superficies y Resend por API. ❌ **Corregido por mí:** 45 bloques (no 40) y 0,162 M/bloque; ✅ ampliada la contradicción del post por el techo; rango de franquicias `CUS-M12…M25`, no `M13…M24`.

**Lo que SÍ comprobé:** catálogo 50 y escalera completa · `payment-links`/`product-prices` 52 · `zona-app` 52 reales · `comingSoon` 21 en los dos gemelos y su render sin precio · slug libre · robots en 5 bloques · ficha de la hermana (`:286`, `:349`) · `CHS-31/32/33/37b/12/46a/49` en su JSON · `CHN-49b/65/69/71c/72/93/48` en su JSON y `.md` · 85-90 % en 2 xlsx de la hermana y 0 en su guía y su landing · `PyG 3 Años` A54:C68 (valores y fórmula) · `pack-appcc/09` Instrucciones y `Control Aceite!F5` · el post (banners, enlaces, `faq:`, tabla y sus sumas) · 327 posts ES · páginas de rol · agentes en `catalogo-hub.json` · tamaños del pipeline y del guion de la hermana · páginas y palabras de la guía y el bonus de la hermana con PyMuPDF · GSC por page · Resend `list-broadcasts`.
**Lo que NO comprobé:** ninguna norma con mis manos (se apoya en L3 con sus niveles); ningún precio de L1/L4 re-descargado; la OEPM para «La Rueda»; el registro de búsquedas del hub.

---

**Estado: research cerrado, pendiente de refutación y de firma de decisiones.**

**Via: Claude Code**
