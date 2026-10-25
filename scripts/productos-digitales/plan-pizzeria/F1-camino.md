# Plan de Negocio: Pizzería Napolitana (ES, 35 €) · F1: camino de construcción
> Sesión Claude Code, 25-oct-2026. Arquitecto de F1, una pasada. Producto **NUEVO** (sin 1.x), slug `plan-negocio-pizzeria`,
> línea A (local fijo). Medido en el VPS (`main` @ `63ba1aef`, venv `/root/venv-guias`, salida en `/root/tmp-piz-f1`, ya borrada;
> `git status` vacío). Caso, mercado, normativa y cifras: `F1-research-pizzeria.md` (otro agente); aquí, el CÓMO y el QUÉ se toca.

## 0. Decisión en tres líneas

1. **Camino de la heladería 1.0, con semilla del TAPAS BAR 2.2**: `semilla_piz.py` copia los dos xlsx LIVE de
   `dl/plan-negocio-tapas-bar/` (molde A-β + checklist C2, solo lectura), escribe lo que el módulo de contenido no alcanza, y
   `planes-v2_0/main.py --dry-run --origen` + `grupo_a.py` lo reconstruyen con un módulo nuevo
   `planes-v2_0/contenido_plan_negocio_pizzeria/a.py` (mecánica del tapas bar, formato compacto de la heladería). Word en las
   131 ranuras del FT ES. Quinto entregable, la calculadora de masa y escandallo, **fuera del motor** (precedente: `calculadora_fin_es.py`).
2. **Cero cambios en código común**: `--producto` acepta cualquier pid y el contenido se resuelve solo (`main.py:876`);
   **NO se añade el pid a `PRODUCTOS` (`main.py:117-128`)**: `demo_moldes` exige `len(fuera) == 30` (`main.py:749`). El 21 % de la
   bebida para llevar va con la **línea partida que ya existe** (`grupo_a.py:2291-2314`) sobre la línea de bebida: **probado hoy** (§1).
3. **5 entregables, ≈ 48 ficheros de capa de producto** (§5) y **F2 + F3 ≈ 1,9 M** (§8): con la F1 (~0,8 M), ≈ 2,7 M ≤ 5 M.

## 1. Dry-run de control (VPS, 25-oct, línea A en verde hoy)

`CLAUDE_SCRATCHPAD=/root/tmp-piz-f1/<pid> main.py --producto <pid> --dry-run --solo a`, con el setter `Cell.value` de openpyxl
instrumentado (registra cada escritura del motor y compara el libro generado con el LIVE celda a celda):

| Semilla | Resultado |
|---|---|
| **`plan-negocio-tapas-bar`** | **exit 0 en 22 s**: idempotencia 0 · inject_cache 742 fórmulas (683 con caché) + 12 · data_only 694 con valor, 59 «""», 0 fallos · blancos 0 · **§9 13/13** · checklist **C2, 73 ítems** · censo `--fail` 0 · moldes **30/30** · 16/16 protegidas · TODO VERDE |
| `plan-negocio-bar-restaurante` | exit 0 en 24 s, TODO VERDE · checklist **C1** (64 ítems) · molde **A-α** |
| `plan-negocio-cafeteria` | exit 0 en 22 s, TODO VERDE · checklist C2 (75 ítems) · A-β |
| **Experimento** (copia del árbol en `/root/tmp-piz-f1/x`, sin tocar el repo): tapas con la línea de bebida PARTIDA al 21 % (`pct` 0,10) | **TODO VERDE** (13/13, idempotencia 0, 30/30, 0 fallos pycel): `PyG!H4` = cabecera, `G11` = `H11*0.21+(1-H11)*Supuestos!B39` = **11,1 %**, `H11` verde y desbloqueada, PVP equivalente 19,80 → 19,89 €, Tesorería (fila 16, IVA repercutido) lo lee por el SUMPRODUCT de las líneas. Quedan dos frases del motor que lo contradicen (abajo). Pendiente único en todos: «2 docx sin A4/autor» (Letter, informativo) |

**Lo que el tapas bar 2.2 deja en el libro y el módulo de contenido NO reescribe** (medido; lo pisa la semilla):
`Inversión Inicial!A1` «PLAN DE NEGOCIO: TAPAS BAR / GASTROBAR», **`A2` «Inversión Inicial Estimada — España 2026»** (prohibido),
**`A3` «Ajusta las cifras a tu proyecto. Rangos mercado español actual.»**, partidas filas **7-24** (18: rótulo A, importe B, nota D;
la E la reescribe el motor por rótulo, `_lleva_iva` + `RX_SIN_IVA` anclado con `^`, `grupo_a.py:873-880`; fianza 25, renta previa 26
e imprevistos 27 son fórmulas), `PyG 3 Años!A2` «Escenario realista — Tapas Bar / Gastrobar 40-50 plazas», fijos filas **26-34**
(9: los 5 del molde + los 4 `FIJOS_EXTRA` del tapas, rótulo A e importe B; F vacía; Seguros en 25, Amortización en 35),
**`PyG!G13` = fórmula** (`=…Supuestos!$B$39`: con `IVA_COMPRAS` numérico, la semilla escribe el valor o el motor la cuenta como
fórmula perdida, gotcha de heladería y finca), `Punto Equilibrio!A2` «Break-even mensual y diario — Tapas Bar / Gastrobar»,
docProps `description`/`keywords` (`aichef.pro/plan-negocio-tapas-bar`; `title`/`subject` los pone el motor con `CONCEPTO`), y en el
checklist título, 6 fases, **73 tareas** (11/13/13/12/14/10), pestañas «F1 - Constitución…F6 - 90 Días», pie e `Instrucciones!A3` con el
pid. Los valores verdes de `0. Supuestos` también (**`grupo_a` conserva lo verde**): la semilla escribe los SUPUESTOS. La columna H
del P&L viene vacía (el motor la limpia siempre, `grupo_a.py:2162`). Lo rehace el motor: notas de Supuestos, **Personal entero**
(`_limpiar_area`, `grupo_a.py:1404`: vale cualquier nº de filas de `PLANTILLA`), Instrucciones (`grupo_a.py:4094`; el bloque «QUÉ HA
CAMBIADO» del tapas, filas 34-48, no se pinta con `RECALIBRADO = ()`, `grupo_a.py:4253`; las referencias «Fichero v1.1», filas 54-68,
las sustituye `INSTRUCCIONES['referencias']`), Tesorería, Financiación y Escenarios (rótulos genéricos).
**Frases del motor que hay que traducir con `VOCABULARIO`** (medidas en el experimento): `Supuestos!C9` «el alcohol que sale por
delivery y el pan común, si los tienes, mueven la media» · `Instrucciones!A8` «el libro lo aplica al alcohol del canal de delivery» ·
nota de `iva_general` (`motor.py:232-236`, «el que repercutes por el alcohol que sale por delivery»).

## 2. Semilla y molde de contenido: TAPAS BAR (mecánica) + heladería (formato)

| | Tapas bar (elegido) | Bar-restaurante | Cafetería |
|---|---|---|---|
| Molde del plan | **A-β** (lista plana: 18 partidas, 9 fijos) = el que sabe pisar la semilla de la heladería | A-α (hojas numeradas, inversión por bloques): semilla nueva | A-β |
| Checklist | **C2** (código de `semilla_hel.checklist` tal cual) | **C1**: otro código | C2 |
| Driver | cubierto, **dos servicios** (mediodía y noche), barra y sala | cubierto, dos servicios | cliente de brunch (`VOCABULARIO`) |
| `ROTACION` | **encendida**, techo 3 + `referencia` propia | encendida por defecto, sin `referencia` | encendida, techo 3 |
| `COBERTURA` | servicio 9,5 h × 2 + **producción antes de abrir 3,5 h × 2** (4 claves) | sin claves (cuadrante del motor) | sin producción |
| IVA y delivery | 2 líneas `mix_en_supuestos`, alcohol 85 % de la bebida, delivery 0 % (comisión 30 %) | 2 líneas, delivery 0 % (28 %) | 2 líneas, delivery 0 % |

Una pizzería napolitana con ~50 plazas es un **restaurante de dos servicios con producción antes de abrir** (amasado, puntata y
boleado, encendido del horno de leña, mise en place) y canal de llevar/domicilio: el tapas bar, no la cafetería. Del `a.py` del
tapas se toma la mecánica; **los textos se reescriben enteros** (sus notas citan «fichero v1.1», RD-xx, §7-bis). Formato y sexto
campo (`research §n` / `BOE` / `calibrado D9`) = `contenido_plan_negocio_heladeria/a.py` (466 l.).

| Clave | Decisión |
|---|---|
| `CONCEPTO` | `'Pizzería Napolitana'` |
| `VOCABULARIO` (+ `_SIN_TILDES = True`) | `{'cubierto': 'comensal', 'cubiertos': 'comensales'}`: masculino como «cubierto» (sin arreglos de concordancia) y en `RX_RECUENTO`/`RX_RECUENTO_DV` igual que él (`motor.py:768-772` y `1378-1382`). «Sala» se queda. Más las 3 frases del §1: «la bebida que sale para llevar o a domicilio mueve la media» · «el libro lo aplica a la parte de la bebida que declara la columna H de su línea en el P&L». F2 mide los rótulos con `barrido_es.py` |
| `SUPUESTOS` | las mismas claves que el tapas, cada nota reescrita. `cubiertos_dia` = **comensales al día de sala + para llevar + domicilio** (una pizza ≈ un comensal); ticket por comensal sin IVA. **`pct_delivery` = cuota por PLATAFORMA, < 25 %** (la demo §2.11.9, `grupo_a.py:4867`, lo sube al 25 % y exige que suba la comisión: finca `F2-NOTAS.md` §2.2); recogida en el local y reparto propio, sin comisión, en la nota. `pct_consumibles` con las cajas de cartón. `aforo` = plazas de sala (~50), terraza en la nota. `pct_bebida_alc` con **rótulo propio** «Bebida que compras al 21 % (alcohol y refrescos con azúcar) sobre el total de bebida»: con la línea partida solo mueve el IVA SOPORTADO (`grupo_a.py:2197-2204`), así que aquí acierta también con los refrescos. `iva_bebida` (B63): nota «sin efecto: el tipo lo fija la línea del P&L» (precedente heladería) |
| `LINEAS_INGRESO` | 2 (`mix_en_supuestos`): **pizzería y cocina** (sala, llevar y domicilio, todo al 10 %: art. 91.Uno.2.2.º y 91.Uno.1.1.º LIVA, sin partir) / **bebida** con sexto campo `{'cabecera': 'Bebida para llevar o a domicilio al 21 % (%)', 'pct': <research, ≈ 0,10>, 'tipo': 0.21, 'nota': …}`: alcohol y refrescos con azúcar que salen del local al 21 %; agua, café y zumos sin azúcar, al 10 %. **No se desprecia**: cuesta 0 líneas de código, el experimento lo dio verde y es lo que afirma la FAQ |
| `IVA_COMPRAS` | **número** (celda verde, `grupo_a.py:2400-2420`): harina panificable, quesos, tomate, hortalizas y aceite al 4 % frente a embutidos, carnes y salsas al 10 % (pesos y tipos: research, BOE). La semilla escribe `G13` por valor |
| `PLANTILLA` | 7 filas (como la semilla): titular-pizzaiolo maestro · pizzaiolo fornero · ayudante (estirado, boleado, mise en place) · jefe/a de sala · camarero/a a tiempo parcial (noches y fines de semana) · extra de fin de semana · suplencias (RC-19). Si el research pide reparto propio: fila de repartidor laboral (Ley 12/2021) y baja la cuota de plataforma. Bruto ≥ SMI × jornada; convenio provincial de hostelería |
| `COBERTURA` | 4 claves: `horas_dia` (comidas + cenas abiertas), `personas_franja` (horno + sala), **`horas_produccion`/`personas_produccion`** (masa, horno y mise en place antes de abrir; research) |
| `ROTACION` | encendida: `{'max': 3.0, 'nota_max': …, 'referencia': 'Incluye a quien se lleva la pizza o la recibe en casa, que no ocupa mesa: la rotación de tu sala es menor que esta cifra…'}`. Contar el domicilio en los comensales SOBREESTIMA la rotación (lado prudente) |
| `INVERSION` / `INVERSION_EXTRA` | `{}` / `()`: las 18 partidas las escribe la semilla |
| `AMORTIZABLE` | **propio** (como la heladería): `obra` = proyecto, obra, instalaciones, fontanería, **salida de humos y chimenea**, rótulo, decoración; `maquinaria` = horno, amasadora, mesa refrigerada, cámaras, armarios, barra, cafetera, mobiliario, terraza, vajilla, menaje, TPV; `no` = constitución, licencias, tasas, marca, web, lanzamiento, stock, formación |
| `FIJOS` + `FIJOS_EXTRA = ()` | patrón de la heladería: la semilla escribe las 9 filas 26-34 y `FIJOS` pone la nota por rótulo normalizado. Candidatas: gestoría · **mantenimiento del horno y limpieza de la chimenea** · marketing · software (TPV, reservas y plataformas) · limpieza, lavandería y EPI · residuos (cartón, orgánico, aceite) · DDD · SGAE y AGEDI-AIE · PRL; tasa de terraza en lugar de la que sobre (research). La **leña**, en `suministros_mes` (el horno se enciende cada día de servicio) |
| `UMBRALES`, `ESCENARIOS`, `ESTACIONALIDAD` | research; **Mes 1 = enero** (sin girar: pagas en 7 y 12 por defecto, sin las notas de Tesorería de la heladería); 12 pesos con `assert` |
| `INSTRUCCIONES` | `uso` 6-8 de la heladería (8 = «el Word y la calculadora usan las cifras de este Excel») · `referencias` con fuente real del research (pliego de la ETG, LIVA, convenio), nunca «Fichero v1.1» |
| `CHECKLIST` / `RECALIBRADO` | `{}` (lo escribe la semilla) / `()` · versión **1.0** con `piz_version.py` (`MES` = mes del merge, previsto «noviembre 2026») |

## 3. Carpeta `scripts/productos-digitales/plan-pizzeria/` (copias de la heladería con PID y rutas)

| Fichero | Origen | Cambios |
|---|---|---|
| `semilla_piz.py` | `semilla_hel.py` | origen `dl/plan-negocio-tapas-bar/`; `TITULOS_PLAN` (Inversión **A1, A2 y A3**, PyG A2, Punto Equilibrio A2); **18 partidas** en 7-24 (A/B/D/E; asserts `A25` fianza, `A26` alquiler, `A27` imprevistos); **9 fijos** en 26-34 (B, F a `None`; asserts `A25` Seguros, `A35` Amortización); `G13` por valor (assert de que era fórmula); **fuera** el vaciado de `PyG!H4:H11` y su assert de «pan» (la semilla no trae línea partida); `_supuestos` y `_docprops`; checklist: assert de `Instrucciones!A3` contra `plan-negocio-tapas-bar` |
| `datos_checklist.py` | el de la heladería (formato) | tareas nuevas (§4) |
| `piz_version.py` + `main_piz.py` | `hel_version.py` + `main_hel.py` | `MES`; la calculadora también importa `piz_version` (como `fin_version`) |
| `ciclo.sh` | el de la heladería | `SCR=/root/tmp-piz-f2/motor`, `--producto plan-negocio-pizzeria` |
| `cifras_piz_es.py` | `cifras_hel_es.py` | `MAPA`: `^comensales/d[ií]a \(media`, PE `^comensales necesarios al d[ií]a$`/`(caja)`, `^coste variable por comensal`, `^margen de contribuci[oó]n por comensal`, `^rotaciones al d[ií]a que exige`, Sup. `^rotaciones al d[ií]a impl[ií]citas` y `^aforo del local`, `PyG!H` de la bebida (`BEBIDA_21_PCT`), partidas propias (`HORNO`, `AMASADORA`, `MESA_FRIA`, `SALIDA_HUMOS`…); lee también la caché de la calculadora (`COSTE_BOLA`, `COSTE_MARGHERITA`, `FC_MARGHERITA`). Fuera `MESES` girados y lo de helado. Gates §6 |
| `calculadora_piz_es.py` | **nuevo**, con los helpers de `calculadora_fin_es.py` (`_f`, `_nota`, `_imprimir`, `_dv`, `generar` + `inject_cache`, `autotest`) | §4 |
| `tandas_docx.py` · `docx_piz_es.py` · `BRIEF-REDACTORES.md` | los de la heladería | §4; `PROHIBIDOS` propios |
| `barrido_es.py` | el de la heladería | `RX` = restos FT (camión, ventanilla, generador, aparcamiento, food truck) + **restos tapas** (`\btapas?\b\|gastrobar\|vermut\|raciones\|pinchos?\|tapeo\|afterwork\|salamandra\|rational\|[Ff]ichero v1\.1`) + **restos heladería** (`helad\|mantec\|cubeta\|sorbete\|pasteuriz\|granizad\|horchata\|tarrina`) + **motor sin traducir** (`alcohol (que sale por\|del canal de) delivery\|pan com[uú]n`) + prohibidos. ⚠️ **Fuera los restos de panadería de la heladería** (`harina`, `amasad`, `levadura`, `masa madre`, `\bpan\b`, `hornada`, `superreducido`): aquí son vocabulario del oficio |
| `gate_restos_ft.py` | **reusar** el de `catering-es-2_0/` | `--rx-extra '<restos tapas>\|<restos heladería>\|plan-negocio-tapas-bar\|plan-negocio-heladeria'`; antes de meter la guía (Letter) |

## 4. Word, checklist, calculadora y entregables

**Word** `plan-de-negocio-pizzeria.docx`: molde = docx del FT ES (131 párrafos, 10 H1, 61 ranuras de cuerpo, mapa
`business-plans-en-4/docx_es_cat.json`), el de heladería, paellero y parrillero: `FIJOS`, `ENCABEZADOS` (37…109) e `INDICE` (24-33)
valen sin remapear. `docx_piz_es.py` = `docx_hel_es.py`: gate 10 H1, A4, ≥ 6.000 palabras, 0 tokens, 0 no latinos, 0 prohibidos,
docProps AI Chef Pro 2026, `comments` = `aichef.pro/plan-negocio-pizzeria`. `FIJOS[35]` = «Anexos: Plan Financiero Excel + Checklist
de Apertura Excel + Calculadora de Masa y Escandallo Excel + Guía de Equivalencias». **`FIJOS` 127-129** (catálogo `products-catalog.ts`:
`kit-tareas-pizzeria` l. 165, hub «Tareas Recurrentes: Pizzería»; `kit-escandallos` l. 72; APPCC l. 85) = → Kit de Tareas Recurrentes:
Pizzería · → Kit de Escandallos Pro · → Pack Plantillas APPCC. **2 tandas Sonnet en paralelo**: `piz_es_a` §1-5 (29 ranuras) · `piz_es_b`
§6-10 (32); gemela de formato = `plan-heladeria/textos/hel_es_{a,b}.json` (la ES 1.0 de local fijo). `PISTAS` desde el research
(SERP, caso, errores). Prohibidos: los de la heladería que no son del oficio («España 2026», «validad», «freelance», «carné de
manipulador», «tarifa plana», «CNAE», RGSEAA minorista), **«STG/ETG» o «certificada» como sello propio y la AVPN como obligación**, restos §3.

**Checklist** `checklist-apertura-pizzeria.xlsx` de `datos_checklist.py`, molde C2 del tapas (F1-F6 + Instrucciones; cabecera fila 4
`OK · TRÁMITE / ACCIÓN · RESPONSABLE · PLAZO · NOTAS`; pie), pestañas ≤ 31 caracteres. **~80 tareas**: F1 Constitución y fiscalidad (12) ·
F2 Local, licencias, humos y terraza (15) · F3 Cocina, horno y registro sanitario (14) · F4 Personal, APPCC y alérgenos (13) · F5 Marca,
carta, delivery y captación (13) · F6 Apertura y 90 días (13). Research, con fuente primaria: IAE (sala y reparto), régimen de la actividad,
salida de humos a cubierta y ordenanza de hornos de leña, registro sanitario autonómico (RD 1021/2022), alérgenos (RD 126/2015 y venta a
distancia, Reg. 1169/2011 art. 14), temperatura del reparto, envases para llevar (Ley 7/2022 y RD 1055/2022), contrato de plataforma,
riders propios (Ley 12/2021), Veri\*factu y el uso del nombre «pizza napoletana» (ETG, Reg. (UE) 97/2010).

**Calculadora** `calculadora-masa-escandallo-pizzeria.xlsx` (`calculadora_piz_es.py`, VPS; A4, protegida sin contraseña, verdes desbloqueadas):

| Hoja | Entradas (verdes) | Cálculo |
|---|---|---|
| `Masa` · A, por litro de agua (pliego) | nº de bolas (DV entero > 0) · peso de bola g · merma de amasado y boleado % · harina, sal y levadura fresca **g por litro de agua** (valores del pliego de la ETG del research; su rango, en gris al lado) · €/kg de harina, sal y levadura · constante gris «1.000 g» | masa = bolas × peso × (1 + merma) · masa por litro = 1.000 + H + S + L · litros = masa / masa por litro · agua, harina, sal y levadura = litros × (1.000; H; S; L) · % panadero = agua/harina, S/H, L/H · semáforo «dentro del pliego» = `AND` de H y S en su rango |
| `Masa` · B, panadero | hidratación %, sal % y levadura % sobre la harina | harina = masa / (1 + h + s + l); agua, sal y levadura = harina × %; **coste de la masa y coste por bola** = Σ (g × €/kg) / 1.000 / bolas (de A) |
| `Escandallo` | IVA de la pizza 10 % · food cost objetivo % · coste de la caja para llevar € · ~22 ingredientes (A nombre · B €/kg sin IVA de ejemplo del research · C merma %) × **8 pizzas** (E-L, gramos): Margherita, Marinara, Diavola, Capricciosa, Quattro formaggi, Cotto e funghi, Bufalina, Salsiccia e friarielli · PVP con IVA de cada una | D €/kg neto = B / (1 − C) · por pizza: masa = coste por bola (`Masa`) · ingredientes = `SUMPRODUCT`(gramos; D) / 1.000 · coste · PVP sin IVA = PVP / (1 + IVA) · **food cost %** (semáforo contra el objetivo) · margen € · PVP con IVA para el objetivo = coste / objetivo × (1 + IVA) · food cost para llevar con la caja |
| `Instrucciones` | — | la de la finca: verdes, fuentes (pliego, LIVA), versión 1.0, bio |

**Gate de la calculadora** (`--autotest`, VPS, como la finca): pycel y caché ± 0,01 contra un `calcular()` en Python con 3 juegos
(por defecto + 2 por `set_value`) · Σ de ingredientes = masa ± 0,5 g · el bloque B con los % del A reproduce el A · food cost de la
Margherita de ejemplo en 12-30 % · A4, protección, verdes desbloqueadas, 0 fórmulas sin caché, 0 números tecleados en fórmulas (salvo 0/1)
· `motor.gate_formatos` 0 · DV · docProps · barrido y no latinos 0. Sin firma calc-beta (no pasa por `main.py`; el censo no clasifica moldes).

**Entregables** en `dl/plan-negocio-pizzeria/` (clave de `PRODUCT_FILES`): `plan-financiero-pizzeria.xlsx` (`plan-financiero`) ·
`plan-de-negocio-pizzeria.docx` (`plan-negocio`) · `checklist-apertura-pizzeria.xlsx` (`checklist-apertura`) ·
`calculadora-masa-escandallo-pizzeria.xlsx` (**`calculadora-masa`**, nueva: ningún gate fija los nombres) · guía (`guia-equivalencias`).

## 5. Capa de producto (slug nuevo; patrón exacto de cada E: `git show 769a0e26 -- <fichero>`, la finca, PR #164)

Slug, env y nombres de imagen comprobados con `git grep`: 0 choques. Líneas medidas hoy en `main` @ `63ba1aef`.

| Fichero | Acción | Gate |
|---|---|---|
| `astro-site/src/data/productos/planes/plan-negocio-pizzeria.ts` | P de la finca (251 l.): **sin `testimonials`** (clave omitida), rating ni tachado; SEO sin «España 2026»; FAQ con «¿Sirve en México…?», «¿Puedo llamarla napolitana?», delivery y horno; BONUS guía (`es-guia-equivalencias.jpg`, 15 €); `stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_PIZZERIA'`; `schema.price` 35; `updateNote` «Producto nuevo · Versión 1.0 · noviembre 2026»; `footerLinks` → Kit Tareas Pizzería, Kit Escandallos, Pack APPCC; cifras medidas, nada movible (DSCR, payback, saldos) | `sync-product-prices.py --check`, `gate-no-latinos`, `nombre-gate.py` |
| `astro-site/src/pages/plan-negocio-pizzeria{,-access,-library}.astro` | P (32/17/18 l.), `locales=['es']` | `gate-flujo-postpago` D/E-f (3 puertas cripto) |
| `astro-site/src/islands/library/PlanNegocioPizzeriaLibraryIsland.tsx` | P (16 l.) | ídem |
| `src/pages/PlanNegocioPizzeriaDashboard.tsx` · `…AccessGate.tsx` | P de la finca (150/13 l.): **5 tarjetas** (fuera `modelos-contrato`; `calculadora-masa` en lugar de `calculadora-pricing`), guía con Globe | C |
| `astro-site/src/lib/zona-app.ts:82` | E (+1 tras la finca) | A |
| `netlify/functions/get-download-urls.ts:1241-1248` | E (`PRODUCT_FILES`, 5 claves, tras la finca) | B (disco, git, 200 binario) |
| `netlify/functions/verify-purchase.ts:635` · `resend-access.ts:584` · `admin-generate-access.ts:82` | E (`emailBody` con lo MEDIDO: Word de 10 secciones, Excel de 9 hojas, checklist de N tareas, calculadora, guía) | A |
| `netlify/shared/product-prices.ts:73` (regenerar con `sync-product-prices.py`) · `payment-links.ts:72` (tras el link, `sync-payment-links.py`) | E | D y E |
| Netlify env `VITE_STRIPE_PAYMENT_LINK_PLAN_PIZZERIA` (builds) | John crea el link; Claude: env + redeploy | D |
| `src/data/products-catalog.ts:508` · `productos-changelog.ts:2051` (`'1.0'`, sin «qué ha cambiado») · `productos-digitales-config.ts:611` (5 ficheros) · `src/pages/AdminGenerateAccess.tsx:76` | E (tras la finca) | `sync --check` |
| Hubs: ES `ProductosDigitalesHubPage.astro` (posición 1 con «✨ Nuevo», l. 68; **quitar la tarjeta de `comingSoon` l. 1070**; la Chocolatería Boutique, 5.ª novedad, l. 151, pasa a «Nuevo») · EN `DigitalProductsHubPage.astro` (tarjeta junto a la finca, l. 608; `comingSoon` l. 1031) · DE 65/924 · FR 66/925 · IT 66/925 · NL 63/922 · PT 65/924 · SPA `src/pages/ProductosDigitales.tsx:52` / `comingSoon` l. 1053 | E (las 7 tarjetas de «Próximos» ya están traducidas, icono `Pizza`; «Mobile Wood-Fired Pizza» se queda) | `hub-gate.py`, `tienda-gate.py` |
| `astro-site/src/lib/sinonimos-buscador.json` (mapa por slug, como l. 228) | E: «pizzeria pizzerias pizza napolitana napoletana horno de lena pizzaiolo pizzero masa delivery a domicilio» | buscador del hub |
| `astro-site/public/llms-full.txt:139` · `astro-site/src/lib/sitemap-lastmod.json:697` | E (+1 línea cada uno, fecha del LIVE) | sitemap en el `dist` + reenvío GSC |
| `astro-site/src/data/productos/tareas/kit-tareas-pizzeria.ts:395-403` · `planes/plan-negocio-bar-restaurante.ts:299-303` (`footerLinks`) | E (+1 enlace al plan: nada huérfano) | revisión |
| `scripts/productos-digitales/equivalencias-es/censo-terminos-es.py:190-191` · `build_guia_es.py:3,596-597` | E: **53 → 54** + `datos/integracion.json` (ejemplos de la FAQ) + `terminos.json` solo si un término cambia en ≥ 5 de 21 países con fuente (candidatos: a domicilio/delivery, champiñón, pimiento, rúcula; tope 0,05 M; si no, ejemplos en la FAQ como heladería y finca) | `build_guia_es.py --check --only plan-negocio-pizzeria` |
| Imágenes `astro-site/public/lovable-uploads/ai-gallery/plan-pizzeria-{hero,plan,horno,masa,sala,delivery,equipo}.jpg` | C (skill `generate-images`): hero = og, hub y CTA; distintas de `tareas-pizzeria-*`, `consultor-pizzero-*` y `use-case-pizzeria-*` | D (200) |
| `scripts/productos-digitales/emails/broadcast-plan-negocio-pizzeria-lanzamiento-es.html` | C desde el de la finca; «Hola, colegas», negro/dorado, sin cifras movibles | `resend-broadcast.py --test` |
| `PAYMENT_LINKS_PENDIENTES_JOHN.md` · `CALENDARIO-V2-SEMANAL.md` (l. 552 «Q1 2027» → LIVE; cola de correos, l. 764) · `tienda-gate.py:84` (`PLANES_ES`, tras el LIVE) · handoff · `plan-pizzeria/NOTA-CARRIL-CURSOR.md` | E / C | — |

**No se tocan**: `robots.txt` (`/plan-*-access` y `-library` ya bloqueados), `tienda.ts` y `alternatesFamilia` (el gemelo EN se DUPLICARÁ
de este), `src/App.tsx`, `og-meta.ts`, `main.py` `PRODUCTOS` y el blog (carril Cursor, va en la nota: 19 posts enlazan el kit,
`ia-para-pizzerias.md`, la librería del Pizzero Consultor Pro y las `/usos/` de pizzería).

## 6. Gates

**F2 (VPS)**: `ciclo.sh` → `main.py` exit 0 (idempotencia 0, caché, blancos 0, §9 13/13, censo `--fail`, demos 30/30) ·
`cifras_piz_es.py` **D9 VERDE**: DSCR mínimo ≥ 1,25 · saldo mínimo > 0 · cobertura ≥ 98 % · holgura de caja del año 1 ≥ 15 % (años 2 y 3
informativas) · exceso de financiación 0-5 % · neto a régimen ≤ 12 % · rotación de equilibrio de caja ≤ techo · `pct_delivery` < 25 % ·
`PyG!G11` = H × 21 % + (1 − H) × 10 % · `calculadora_piz_es.py --autotest` VERDE · `docx_piz_es.py` (10 H1, A4, ≥ 6.000, 0 tokens) ·
`tandas_docx.py check` ×2 · `barrido_es.py` 0 en los 4 · `gate_restos_ft.py --rx-extra` 0 · `gate-no-latinos.py --only` ·
`censo-entregables.py --only plan-negocio-pizzeria --fail` · `paginas-gate.py` · Mac = VPS (sha256) · **una** revisión Opus final
(cifras · legal · editorial). **F3**: `sync-product-prices.py --check` · `build_guia_es.py --check --only` · `gate-flujo-postpago.py
--base <preview> --crypto-products all --crypto-exclude pro-prompts-ebook --only plan-negocio-pizzeria`, después LIVE (A-E-f) ·
`scripts/astro-migration/{miselup,whatsapp,robots,hub}-gate.py` · `nombre-gate.py` · `tienda-gate.py --base https://aichef.pro` ·
`fase6-gate.py https://aichef.pro` · curl al checkout cripto (`qa-pizzeria@aichef.pro`, purgar) · sitemap reenviado · `git pull` antes.

## 7. Plan F2 y F3

**F2 — Entregables** (rama `feat/plan-negocio-pizzeria`; worktree de la rama en el VPS, nunca `main`)
1. Mac · leer `F1-research-pizzeria.md` y firmar SPEC corta (≤ 80 líneas): caso y mezcla, 18 partidas, 9 fijos, 7 filas, cobertura,
   cuota de plataforma y H de la bebida, estacionalidad, pliego de la masa y 8 pizzas, prohibidos. Commit F1.
2. Mac · **un** implementador opus: `a.py`, `semilla_piz.py`, `datos_checklist.py`, `piz_version.py`, `main_piz.py`, `ciclo.sh`,
   `cifras_piz_es.py`, `barrido_es.py`. **En paralelo, un sonnet**: `calculadora_piz_es.py`.
3. VPS · `bash ciclo.sh` + `cifras_piz_es.py` en bucle hasta D9 verde (máx. 3 vueltas; si no cuadra, se para y se reporta); demo
   §2.11.5 con un fijo de ±100 € si hace falta; `calculadora_piz_es.py --autotest`; `barrido` y `gate_restos` a 0. scp al Mac.
4. Mac · `tandas_docx.py preparar` → **2 Sonnet en paralelo** (`istats` < 60 °C) → `check` ×2.
5. VPS · `docx_piz_es.py` + gates; copia a `public/dl/plan-negocio-pizzeria/` en el worktree.
6. Mac · **una** revisión Opus de los 4 ficheros + una ronda de arreglos; VPS regenera. `F2-NOTAS.md`. Commit + push (`Via: Claude Code`).
**F3 — Producto y lanzamiento**
7. Mac · Sonnet A: ficha + 3 páginas + isla + dashboard + access gate (FAQ, SEO). Sonnet B: functions ×4, `zona-app`, configs, catálogo,
   changelog, hubs ×8 (con su `comingSoon`), buscador, `llms-full`, `sitemap-lastmod`, `footerLinks` ×2. Los dos con el diff de `769a0e26`.
8. Mac · 7 imágenes con `generate-images`. VPS · censo de términos (53 → 54) + `build_guia_es.py --only` + `--check`; FAQ de países.
9. Mac · `sync-product-prices.py`; PR draft → preview de Netlify; gates contra el preview.
10. **John · Payment Link** (35 EUR, descripción en prosa sin viñetas, éxito → `/plan-negocio-pizzeria-access?session_id={CHECKOUT_SESSION_ID}`).
    Claude: env, `sync-payment-links.py`, redeploy; merge (aprueba John); gates LIVE; sitemap.
11. Correo: hueco ES **8-dic 08:00Z** (CALENDARIO l. 764); > 30 días hoy → borrador por curl + prueba a John + routine que lo programe el
    8-nov o después; CALENDARIO y handoff. Nota al carril Cursor. Commit + push.

## 8. Presupuesto F2 + F3

| Pieza | Quién / dónde | Tokens |
|---|---|---|
| `a.py` + semilla + checklist (~80) + versión/ciclo + cifras + calibración D9 | opus · VPS | 0,45 M |
| Calculadora de masa y escandallo (generador nuevo sobre los helpers de la finca + autotest) | sonnet · VPS | 0,15 M |
| Word: pistas + 2 tandas Sonnet ‖ + ensamblado + barrido | sonnet × 2 + orquestador | 0,30 M |
| Revisión opus final + arreglos | opus | 0,25 M |
| Capa de producto (≈ 48 ficheros, 7 nuevos de copia) | sonnet × 2 · Mac | 0,40 M |
| Imágenes (7) · guía de equivalencias · correo | API / sonnet / orquestador | 0,18 M |
| PR, preview, gates LIVE, merge | orquestador | 0,15 M |
| **Total F2 + F3** | | **≈ 1,9 M** (heladería 2,2 M real con F1; finca ≈ 2,1 M est. con 6 entregables) → con F1, **≈ 2,7 M ≤ 5 M** |

Reloj: F2 ≈ 2-2,5 h (ciclo del motor 22 s; redactores ~20 min; revisión ~30 min), F3 ≈ 1,5-2 h + el link. Lo dispararía: una 3.ª línea
(domicilio aparte), reparto propio en el Excel, un anexo de ordenanzas de hornos, verificar citas que el producto no afirma o 2 revisiones.

## 9. Riesgos

- **Restos del tapas bar** (§1: `Inversión!A1-A3`, 18 partidas, `PyG!A2`, 9 fijos, `PE!A2`, `G13`, 73 tareas, docProps) y de la heladería
  (formato del `a.py`): los pisan semilla y contenido; `barrido_es.py` y `gate_restos_ft.py` con el regex de §3 a 0. **Sin código común.**
  El `PROHIBIDOS` de la heladería trae `harina`, `levadura`, `amasad`, `masa madre`: copiado tal cual, rojo en cada página. Se rehace.
- **Delivery y rotación**: contar el domicilio en los comensales infla la rotación implícita (prudente; la `referencia` lo dice). La
  comisión cae solo sobre la cuota de plataforma, **< 25 %** por la demo §2.11.9; si el research da 25-30 % de delivery, el resto es
  recogida o reparto propio, sin comisión. Riders propios = contrato laboral (Ley 12/2021): fila en `PLANTILLA`, nunca falso autónomo.
- **IVA de la bebida**: la línea partida deja `iva_bebida` (B63) sin efecto y cambia el sentido de `pct_bebida_alc` (solo soportado):
  rótulo y nota propios en `SUPUESTOS` y las tres frases del motor por `VOCABULARIO` (§1); `barrido_es.py` las busca sin traducir.
- **Nombre «napolitana»**: «Pizza Napoletana» es ETG (Reg. (UE) 97/2010). Si el nombre está reservado al pliego, título, landing y Word
  no prometen «napolitana STG» sin certificación: lo cierra el research con fuente y lo comprueba la revisión; la AVPN es privada.
- **Horno de leña**: hay ordenanzas que lo limitan (humos, calidad del aire): consulta urbanística previa en el checklist y gas o
  eléctrico como alternativa en el Word, sin Excel. **Demo §2.11.5** (ramas del IS, `grupo_a.py:5312-5352`): si la ventana de RAI es
  estrecha, un fijo de ±100 € mirando los `ensayos` de `inf.json`. **Guía de equivalencias en Letter** (como las 53): `gate_restos_ft` antes.
- Colateral en LIVE: las tarjetas de «Próximos» dicen «Masa madre» / «Sourdough»; salen con el producto y el copy nuevo no lo repite.
