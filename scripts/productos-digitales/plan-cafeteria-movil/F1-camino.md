# Plan de Negocio: Cafetería Móvil para Eventos (ES, 45 €) · F1: camino de construcción
> Sesión Claude Code, 28-oct-2026. Arquitecto de F1, una pasada. Producto **NUEVO** (1.0), slug `plan-negocio-cafeteria-movil-eventos`,
> familia Planes, línea de eventos con el motor 2.2 (hermanos LIVE a 45 €: Catering Temático, Paellero, Parrillero-Asador y Finca).
> Promesa del hub: «Café de especialidad en eventos de empresa, bodas y ferias: inversión mínima, tarifas y logística».
> Medido en el VPS (`main` @ `c54309c2`, worktree `/root/wt-cafemovil` de la rama `tmp-cafemovil-dryrun`, salida en
> `/root/tmp-cafemovil-f1`; los tres ya borrados, `git worktree list` = solo `main`, `git status` vacío). Caso, mercado y normativa:
> `F1-research-cafeteria-movil.md` (otro agente). Aquí, el CÓMO, lo que se toca y lo que el research tiene que traer (§9).

## 0. Decisión en tres líneas

1. **Hipótesis confirmada: contenido del PARRILLERO 2.2 sobre la semilla del FOOD TRUCK ES 2.2** (la misma que usa el parrillero):
   módulo nuevo `planes-v2_0/contenido_plan_negocio_cafeteria_movil_eventos/a.py` clonado del `a.py` del parrillero (motor de eventos
   sin permutar, base sin local por `VOCABULARIO`, vehículo como «obra», fijos discontinuos) y `semilla_caf.py` = `semilla_par.py` sobre
   `dl/plan-negocio-food-truck/` (14 partidas, 4 filas de plantilla, 10 fijos: es literalmente un vehículo con barra). **Medido hoy**: el
   clon con pid nuevo FUERA de `PRODUCTOS` sale TODO VERDE (r1) y con las palancas del café también (r4, §1). De la **finca**: generador
   del contrato y versión 1.0. De la **pizzería**: bloque de escandallo de la calculadora y las herramientas del Word más nuevas.
2. **Cero código común**; el pid **no** entra en `PRODUCTOS` (`main.py:117-128`; `demo_moldes` exige 30, `main.py:749`). La «segunda
   línea» (ferias y mercados con venta directa) **no** va como 3.ª línea del P&L (defecto del motor con > 2 líneas, libro en blanco y
   gate RT-18, documentado en `contenido_plan_negocio_cafeteria/a.py:323-341`; los 11 hermanos LIVE usan exactamente 2): entra por el
   **canal `delivery`** del motor (cuota de ventas + comisión = canon del organizador), < 25 %. Medido verde con 18 % × 3 %.
3. **6 entregables** (§4), **≈ 41 ficheros de capa** + 6 entregables + 7 imágenes (réplica del diff de la finca `769a0e26`, con los
   arreglos de la pizzería `2e7a3af5`) y **F2 + F3 ≈ 2,1 M** (§8); con la F1 (~0,7 M), ≈ 2,8 M ≤ 5 M (finca real: 3,1 M en 4 h).
   ES listo para el Payment Link en **≈ 3 h** si calculadora, contrato y ficha arrancan en paralelo al implementador (§7).

## 1. Dry-run de control (VPS, 28-oct): el camino genera en verde hoy

| Paso (`PY=/root/venv-guias/bin/python`, en `/root/wt-cafemovil/scripts/productos-digitales/`) | Resultado |
|---|---|
| Clon por `sed`: `plan-cafeteria-movil/{semilla_caf,datos_checklist,caf_version,main_caf}.py` + `ciclo.sh` (de `parrillero-2_2/` y `plan-finca-eventos/`: PID, nombres de fichero, módulo) + `contenido_plan_negocio_cafeteria_movil_eventos/{__init__,a}.py` (`a.py` del parrillero con `CONCEPTO` nuevo y `RECALIBRADO = ()`) | 0 ficheros versionados tocados (`git status`: 2 carpetas `??`) |
| **r1** · `CLAUDE_SCRATCHPAD=/root/tmp-cafemovil-f1/r1 bash plan-cafeteria-movil/ciclo.sh` | **exit 0 en 26 s** · idempotencia 0 · inject_cache 722 fórmulas (656 con caché) + 12 · data_only 667 con valor, 66 «""», 0 fallos · blancos 0 · **§9 13/13** · checklist C2 83 ítems · censo `--fail` 0 · moldes **30/30** · 16/16 protegidas · **TODO VERDE** · sello `Instrucciones!A52` «Versión 1.0 · noviembre 2026 · aichef.pro/plan-negocio-cafeteria-movil-eventos» |
| `parrillero-2_2/cifras_par_es.py --xlsx <r1> --salida <scratch>` | 84 tokens · **D15 VERDE** (cifras = parrillero LIVE: 190.000 €, RAI 17.090 €) |
| **r2** · palancas del café sobre r1: «Ventas de bollería y dulces» `comida` 15 % / «Ventas de café y bebidas de especialidad» `bebida` 85 % · `coste_comida` 0,45 · `coste_bebida` 0,29 · `pct_bebida_alc` 0 · `pct_delivery` 0,18 (= ferias) · `comision_delivery` 0,03 (= canon) · `VOCABULARIO` de delivery → ferias | exit 1, **solo §2.11.5** (ramas del IS): el RAI subió 608 € (17.698 €) y la ventana del parrillero era de 128 € |
| **r3** · un fijo + 608 € en la semilla | §2.11.5 OK · exit 1 por RD-34: origen − usos = −109 € (el fondo de maniobra sube con los fijos) |
| **r4** · `recursos_propios` + 200 € | **exit 0 en 24 s · TODO VERDE**: `PyG!G11` 10 % (bebida sin alcohol), `G14` 10 %, fila 16 «Canon de ferias y mercados» 1.026 € con nota «Sobre las ventas DEL CANAL…». Las dos vueltas de siempre (fijo ±, propios o préstamo) |
| `parrillero-2_2/calculadora_par_es.py` · `plan-finca-eventos/calculadora_fin_es.py` · `plan-pizzeria/calculadora_piz_es.py` (`--salida`) | exit 0 en 1-3 s · autotest **552 / 588 / 422** comprobaciones VERDE · parrillero: 168 fórmulas, 0 fallos pycel |
| `plan-finca-eventos/contrato_fin_es.py` · `docx_fin_es.py` (`--salida`) | contrato 150 párrafos, 4.752 palabras, A4, VERDE · Word 131 párrafos, 10 H1, 6.906 palabras, VERDE |
| `plan-finca-eventos/barrido_es.py` sobre esos dos | 3 coincidencias legítimas del oficio de la finca («cubierto», «obrador»): el del café lleva su RX propio (§3) |

**Medido en r4 — frases de alcohol que la F2 reescribe** (M7 de la finca): `0. Supuestos!C9, C16, C40, C62, C63`, `Instrucciones!A8,
D43`, `Tesorería 12 meses!O16`; las de `a.py` se reescriben con el módulo y **C9, C40, A8 y O16 son del motor: por `VOCABULARIO`** (clave
que acabe en letra o cifra). **Restos del parrillero**: «parrill» 40, «cocina de apoyo» 19, «furgoneta» 17, «carne» 16, «carbón» 15,
«asado» 12, «remolque» 10, «brasa» 8: los pisan `a.py` y la semilla; `barrido_es.py` los demuestra a 0.

## 2. Molde de contenido: por qué el parrillero

| | **Parrillero 2.2** (elegido) | Finca 1.0 | Pizzería 1.0 | Cafetería 2.2 | Food Truck 2.2 |
|---|---|---|---|---|---|
| Driver | invitados × €/invitado × eventos | igual | comensales × ticket × días | cliente × ticket × días | cliente × ticket × días de venta |
| Base | cuota de base sin local (VOCABULARIO) | renta, obra y Mes 1 girado | local | local | base del vehículo |
| Semilla (partidas / plantilla / fijos) | **FT: 14 / 4 / 10** | panadería: 19 / 6 / 10 | tapas: 18 / 7 / 9 | — | es el origen |
| Lo que se toma | **todo el `a.py`** + calculadora (escalado por invitados, canal, cobro, tramos) | `contrato_fin_es.py` (contrato por JSON, revisado), `fin_version.py` | bloque Escandallo (`SUMPRODUCT`), tandas, cifras, barrido | notas de coste del café (`a.py:184-196`) | nada: el CALENDARIO (l. 574) manda «siempre para eventos, no calle» |

| Clave | Decisión (las cifras son huecos del research, §9, dentro de lo que admite el motor) |
|---|---|
| `CONCEPTO` | `'Cafetería Móvil para Eventos'` (`motor.TILDES` ya pone «café», «máquina», «eléctrica») |
| `VOCABULARIO` | **Se quedan** del parrillero: cubierto(s)/comensal(es) → invitado(s) (masculino: concordancias medidas; en ferias cada cliente cuenta como un invitado, nota de B4), días de apertura → eventos, horas de servicio al día → horas de trabajo por evento, ticket → precio por invitado, en cada franja → en cada evento, la frase del Word (`grupo_a.py:3766`), refrescos «con azúcares o edulcorantes añadidos». **Cambian**: cocina de apoyo → «almacén base» (garaje o nave con punto de agua donde duerme el vehículo; masculino), furgoneta → «vehículo», «en sala» → «en la barra del evento», delivery → «ferias y mercados», «comisiones de delivery» → «canon de ferias y mercados», «comisión de la plataforma de delivery» → «canon o comisión del organizador de la feria» (las cuatro medidas en r4). **Alcohol**: las 4 frases del motor de §1 |
| `SUPUESTOS` driver | `cubiertos_dia` = invitados (o clientes) por evento, media de la mezcla · `ticket_medio` = € por invitado sin IVA (paquete de barra o consumición en feria) · `dias_apertura` = eventos + jornadas de feria al año. El crecimiento de los años 2-3 va a los invitados (como el parrillero) |
| `LINEAS_INGRESO` | **2 exactas, comida → bebida** (`mix_en_supuestos`, `grupo_a.py:2256`): «Ventas de bollería y dulces» `comida` (**≥ 10 %**: la demo §2.11.9 sube `coste_comida` y exige que `cv_comida` se mueva, `grupo_a.py:4865`) · «Ventas de café y bebidas de especialidad» `bebida`. Rótulos sin «eventos», «invitados» ni «días» (`motor.RX_RECUENTO`, `motor.py:1378`). Todo al 10 % (servido: 91.Uno.2.2.º; para llevar: 91.Uno.1.1.º, research). Refrescos azucarados para llevar al 21 % **solo** si el research los pone ≥ 5 % de la bebida: línea partida (sexto campo dict, probada en la pizzería) |
| `pct_delivery` · `comision_delivery` | **ferias y mercados con venta directa**: cuota de las ventas **< 25 %** (la demo §2.11.9 la fuerza al 25 %, `grupo_a.py:4867`) · canon del organizador como % de lo vendido en feria (**> 0**; si es fijo por jornada, convertido y explicado en la nota) |
| `pct_bebida_alc` · `iva_bebida` | **0** (sin alcohol; probado en r4) · nota «sin efecto en este plan» |
| `coste_comida` · `coste_bebida` | bollería comprada · café + leche + extras, media ponderada por la mezcla de bebidas con la merma (purga, leche sobrante), **sin envases** (van a `pct_consumibles`). La nota dice que el coste de UNA bebida de la calculadora no se copia aquí (B1 de la pizzería) |
| `IVA_COMPRAS` | **no se declara** (bollería al 10 % = defecto). La compra de bebida soporta el 10 % por fórmula y la leche va al 4 %: el real es algo menor (deuda del motor, `IVA_COMPRAS` solo admite «comida», M7/G14 de la finca). Nota en Supuestos |
| `pct_consumibles` · `pct_varios` · `comision_tpv` | vasos compostables, tapas, removedores, servilletas y sobres · imprevistos · tarjeta (research) |
| `alquiler_mes` · `fianza_meses` · `meses_renta_previa` | cuota del almacén base · fianza · meses previos (research) |
| `suministros_mes` · `seguros_ano` | combustible y carga del generador o baterías fuera de la cuota · RC con productos + vehículo |
| `vida_obra` · `vida_maquinaria` · `pct_imprevistos` | `obra` = vehículo, carrozado y rotulación (8 años, base de los imprevistos, como la furgoneta del parrillero) · maquinaria (10, o lo que diga el research para la espresso) · % sobre la «obra» |
| `dias_cobro` · `dias_pago` | particular 0 (paga antes del evento) ponderado con empresa a 30 días; las señales no se modelan (nota en Tesorería) |
| Mes 1 · rampa | **Mes 1 = enero, sin girar** (como el parrillero: sin las 3 notas de Tesorería de heladería y finca). Girar solo si el research lo exige (~0,05 M, injerto de la finca) |
| `PLANTILLA` | **4 filas exactas** (molde FT; con 3 o 5 hay «fórmulas perdidas», gotcha de la pizzería): titular-barista (ventas y compras; administrador de la SL) · barista fijo discontinuo · 2 baristas o auxiliares de apoyo fijos discontinuos. Nunca «freelance»; bruto ≥ SMI en proporción a la jornada |
| `COBERTURA` · `ROTACION` | `horas_dia` = horas por evento y persona (carga, viaje, montaje, servicio, limpieza, descarga) × `personas_franja`; gate ≥ 98 % · `{'activa': False}` |
| `AMORTIZABLE` | `obra`: vehículo, carrozado, adaptación, rotulación · `maquinaria`: espresso, molino, generador, batería, inversor, depósito, bomba, frigorífico, barra, menaje, báscula, TPV · `no`: licencias, constitución, registro, stock, marca, web, lanzamiento, formación, fianza, cuota |
| `FIJOS` + `FIJOS_EXTRA = ()` | 10 exactos que escribe la semilla (patrón parrillero), p. ej.: gestoría · mantenimiento de la espresso, molinos y filtros de agua · vehículo: mantenimiento e ITV · marketing · software, CRM y teléfono · uniformes y lavandería · residuos · PRL · catas y degustaciones comerciales · portales de bodas (el research elige). Sin «eventos» en el rótulo |
| `UMBRALES` · `ESCENARIOS` · `ESTACIONALIDAD` | research; `r_alquiler` con rótulo «Cuota del almacén base / Ventas»; 12 pesos con `assert` de suma 1,000 |
| `INSTRUCCIONES` | `uso` 6-8 de la finca con su m16: «el Word usa las cifras de este Excel; la calculadora y el contrato, los mismos porcentajes de cobro y cancelación; si cambias una celda verde, manda el Excel» · `referencias`: tabla de la mezcla (como `D35` del parrillero) y tabla de escalado (la de la calculadora) |
| `CHECKLIST` / `RECALIBRADO` | `{}` (lo escribe la semilla) / **`()`** (producto nuevo) |

**Palancas que no existen** (sin tocar `motor.py` ni `grupo_a.py`): (1) 3.ª línea por canal → canal `delivery` (arriba); (2) precio por
hora o por consumición → lo convierte la calculadora, el motor trabaja en €/invitado; (3) IVA soportado de la leche al 4 % → nota;
(4) personal extra por evento (ETT) → plantilla en jornada equivalente y la calculadora evento a evento; (5) señales → no se modelan;
(6) canon fijo por jornada → % equivalente con la cuenta en la nota.

## 3. Carpeta `scripts/productos-digitales/plan-cafeteria-movil/`

| Fichero | Origen | Cambios |
|---|---|---|
| `semilla_caf.py` | `parrillero-2_2/semilla_par.py` (el `sed` de hoy) | mismo origen FT y asserts (A25 Seguros, A36 Amortización, B4 «TRÁMITE», `Instrucciones!A3` del FT); `TITULOS_PLAN`; **14 partidas** (la de trámites EMPIEZA por «Licencias» → sin IVA, M8 de la finca); **10 fijos**; `_docprops`; `Instrucciones!A3` del checklist con el **nombre** del producto, no el slug (m13 de la pizzería) |
| `datos_checklist.py` | el del parrillero (lo legal común de eventos ya verificado) | ~80 tareas (§4) |
| `caf_version.py` + `main_caf.py` + `ciclo.sh` | `fin_version.py` + `main_fin.py` + `ciclo.sh` del parrillero (probados hoy) | `VERSION = '1.0'`, `MES` = mes del merge (si cae en octubre, «octubre 2026»: m17 de la pizzería); `SCR=/root/tmp-caf-f2/motor` |
| `cifras_caf_es.py` | `plan-pizzeria/cifras_piz_es.py` (redondeo comercial con `Decimal`, m2) + `MAPA` de eventos de `cifras_fin_es.py` | `BE_EVENTOS*`, `INVITADOS_EVENTO_A2/A3`, `PAYBACK` + `PAYBACK_CAPEX`, partidas propias; lee la caché de la calculadora (`COSTE_ESPRESSO`, `COSTE_LATTE`…); gates §6 |
| `calculadora_caf_es.py` | fork de `parrillero-2_2/calculadora_par_es.py` (844 l.) + bloque Escandallo de `plan-pizzeria/calculadora_piz_es.py` | §4; importa `caf_version` |
| `contrato_caf_es.py` | `plan-finca-eventos/contrato_fin_es.py` (133 l.; molde físico = contrato del parrillero) | rutas; `textos/contrato_es.json`; gates A4, 0 tokens, barrido, no latinos |
| `tandas_docx.py` · `docx_caf_es.py` · `BRIEF-REDACTORES.md` | los de la pizzería (los más nuevos: pista del payback M1, artículos con %) | `GEMELA` = `plan-finca-eventos/textos/fin_es_{a,b}.json` (formato ES 1.0) y, para el oficio itinerante, `parrillero-2_2/textos/par_es_{a,b}.json` |
| `barrido_es.py` | el de la pizzería (con `RX_PUBLICA` y `RX_CAMPANA`) | `RX` = restos parrillero (parrill, asado, brasa, carbón, `\bcarne`, furgoneta, remolque, cocina de apoyo, show de fuego) + FT (food truck, camión, ventanilla) + motor sin traducir (alcohol, delivery, cubierto, comensal, el local, en sala) + prohibidos. ⚠️ Fuera los restos de otros moldes que aquí son oficio: «bollería», «leche», «generador» |
| `gate_restos_ft.py` | **reusar** `catering-es-2_0/` | `--rx-extra '<restos parrillero>\|plan-negocio-parrillero'`, antes de meter la guía de equivalencias (Letter) |

## 4. Entregables

**Word** `plan-de-negocio-cafeteria-movil-eventos.docx`: molde físico = docx del FT ES (131 párrafos, 10 H1, 61 ranuras; mapa
`business-plans-en-4/docx_es_cat.json`), igual que finca y pizzería; **sin anexo** (no hay fuego ni comunidades que lo pidan): §9 da el
marco estatal y «qué preguntar en tu ayuntamiento y en tu comunidad». Gate 10 H1, A4, ≥ 6.000 palabras, 0 tokens, 0 no latinos, 0
prohibidos; `comments` = `aichef.pro/plan-negocio-cafeteria-movil-eventos`. Venta cruzada (127-129): → Kit de Tareas Recurrentes:
Cafetería · → Kit de Escandallos Pro · → Pack Plantillas APPCC. **2 Sonnet en paralelo**: `caf_es_a` §1-5 (29 ranuras) · `caf_es_b`
§6-10 (32). Pistas: barra contratada frente a venta en feria, mezcla, mercado (SERP), competencia, captación (planners, congresos,
portales de bodas), un evento tipo con la tabla de escalado, plantilla + bolsa, finanzas en eventos/año, legal, 90 días. ~75 tokens
(`INVITADOS_EVENTO`, `PRECIO_INVITADO(_IVA)`, `EVENTOS_ANO`, `CUOTA_FERIAS`, `CANON_FERIAS`, `VENTAS_A1-3`, `NETO_A1-3`, `PRESTAMO`,
`DSCR_MIN`, `SALDO_MINIMO`, `BE_EVENTOS(_CAJA)(_A2/_A3)`, `HOLGURA_CAJA(_A2/_A3)`, `PAYBACK(_CAPEX)`, `COSTE_ESPRESSO`, `ESC_*`…).

**Checklist** `checklist-apertura-cafeteria-movil-eventos.xlsx` (molde C2 del FT que deja el motor; pestañas ≤ 31): **~80 tareas** =
`F1 - Constitución` (12) · `F2 - Vehículo y sanidad` (16: homologación de la reforma e ITV, registro sanitario, agua de consumo,
autorización de cada recinto o feria) · `F3 - Equipo y proveedores` (14) · `F4 - Personal y formación` (10) · `F5 - Marca y captación`
(14) · `F6 - Primer evento y 90 días` (14).

**Calculadora** `calculadora-escandallo-presupuesto-cafe-eventos.xlsx` (`calculadora_caf_es.py`, VPS; A4, protegida sin contraseña, verdes
desbloqueadas; conserva la firma calc-beta `Calculadora · Ejemplos · Instrucciones` y suma `Escandallo`):

| Hoja | Entradas (verdes, con DV) | Cálculo |
|---|---|---|
| `Escandallo` (de la pizzería) | ~16 insumos (A nombre · B €/kg o €/l o €/ud sin IVA del research · C merma %): café en grano, leches (entera, sin lactosa, avena, soja), cacao, chai, sirope, té, azúcar, vasos 4/8/12 oz, tapa, removedor, servilleta × **~10 bebidas** (espresso, americano, cortado, café con leche, flat white, capuchino, latte, mocha, chai latte, chocolate) en g o ml · g de café por shot · PVP de feria con IVA | €/ud neto = B / (1 − C) · coste de producto y coste con envase por bebida (`SUMPRODUCT`) · PVP sin IVA · food cost % (semáforo) · margen · coste por taza de la mezcla (lo lee `Calculadora`) |
| `Calculadora` (del parrillero) | canal Particular / Empresa / Feria (desplegable) · invitados · horas de servicio · tazas por invitado por la tabla del research · mezcla de bebidas · margen objetivo por canal · km · horas de montaje · €/h × (1 + SS) | **logística por la tabla de escalado**: baristas, máquinas o grupos, molinos, kg de café, l de leche, vasos, potencia y toma eléctrica o generador, agua · coste directo · precio por invitado sin IVA (redondeo 0,50) y con IVA 10 %, con su equivalente por hora y por taza · desplazamiento aparte sin margen · **cobro** (señal + resto) · **cancelación por tramos sin huecos** («de X a menos de Y») · margen calculado · Feria: previsión de la jornada (tazas × ticket − canon − coste) |
| `Ejemplos` | — | 3 por las mismas fórmulas: boda (barra tras la cena), congreso o evento de empresa (jornada con 2 pausas), jornada de feria |
| `Instrucciones` | — | verdes, fuentes, versión 1.0, bio; «el coste de una bebida no es el `coste_bebida` del Excel: aquel es la media de la mezcla con la merma» |

Autotest pycel ± 0,01 € con 3 juegos · Σ de la mezcla = 100 % · tabla de escalado = la de `Instrucciones` del plan y la del Word §6 ·
`motor.gate_formatos` 0 · 0 números tecleados en fórmulas (salvo 0/1) · docProps · barrido y no latinos 0.

**Contrato** `modelo-contrato-servicio-cafe-eventos.docx` (~2.000-2.500 palabras; gemela = `plan-finca-eventos/textos/contrato_es.json`,
ya revisado, + la cláusula de fuerza mayor y el reparto de permisos del parrillero): objeto y horas (extras), modalidad de precio (por
invitado, por hora o por consumición con mínimo), carta de bebidas y alérgenos (leche, soja, frutos de cáscara, gluten de la bollería),
requisitos del lugar (toma eléctrica o generador con suplemento, acceso y aparcamiento del vehículo, superficie, cubierta en exterior),
permisos (el cliente, el del recinto; el organizador, la autorización de la feria; la cafetería, registro sanitario, APPCC y RC), señal a
cuenta del precio y factura de cada cobro (LIVA art. 75.Dos), cancelación proporcionada y recíproca, plan B de lluvia (no es fuerza mayor)
y fuerza mayor, desistimiento (arts. 102 y 103.l solo a distancia), fuero del consumidor (90.2), datos e imagen; anexo para empresas y
organizadores de ferias. **Es lo primero que se recorta** si la F2 pasa de 2 h.

**Entregables** en `astro-site/public/dl/plan-negocio-cafeteria-movil-eventos/` (claves = las de la finca): `plan-financiero-cafeteria-movil-eventos.xlsx`
(`plan-financiero`) · `plan-de-negocio-cafeteria-movil-eventos.docx` (`plan-negocio`) · `checklist-apertura-cafeteria-movil-eventos.xlsx`
(`checklist-apertura`) · `calculadora-escandallo-presupuesto-cafe-eventos.xlsx` (`calculadora-pricing`) · `modelo-contrato-servicio-cafe-eventos.docx`
(`modelos-contrato`) · `guia-equivalencias-plan-negocio-cafeteria-movil-eventos.docx` (`guia-equivalencias`).

## 5. Capa de producto: crear (C), copiar de la finca (P) o editar (E). Patrón de cada E: `git show 769a0e26 -- <fichero>`

Slug, env y nombres de imagen comprobados con `git grep`: **0 choques**. Líneas medidas hoy en `main` @ `c54309c2`.

| Fichero | Acción | Gate |
|---|---|---|
| `astro-site/src/data/productos/planes/plan-negocio-cafeteria-movil-eventos.ts` | P (251 l.): sin `testimonials`, rating ni tachado; SEO sin «España 2026»; FAQ «¿Sirve en México…?» con ejemplos que **existan** en la guía (M9 de la finca) y las del research (precio por invitado, toma eléctrica, ferias); BONUS guía (`es-guia-equivalencias.jpg`, 15 €); `stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_CAFETERIA_MOVIL'`; `schema.price` 45; `updateNote` «Producto nuevo · Versión 1.0 · <mes>»; `footerLinks` → Kit Tareas Cafetería, Plan Cafetería, Plan Coctelería de Eventos; nada movible (DSCR, payback, saldos) | `sync-product-prices.py --check`, `gate-no-latinos`, `nombre-gate.py` |
| `astro-site/src/pages/plan-negocio-cafeteria-movil-eventos{,-access,-library}.astro` · `islands/library/PlanNegocioCafeteriaMovilEventosLibraryIsland.tsx` | P (32/17/18/16 l.), `locales=['es']` | `gate-flujo-postpago` D/E-f (3 puertas cripto) |
| `src/pages/PlanNegocioCafeteriaMovilEventosDashboard.tsx` · `…AccessGate.tsx` | P (150/13 l.): **6 tarjetas** como la finca; textos = lo que hacen los ficheros (M6 y m14 de la pizzería) | C |
| `astro-site/src/lib/zona-app.ts` (tras l. 83) | E (+1; nombre corto del diálogo cripto) | A |
| `netlify/functions/get-download-urls.ts` (tras l. 1307) | E (`PRODUCT_FILES`, 6 claves) | B (disco, git, 200 binario) |
| `netlify/functions/verify-purchase.ts` (681) · `resend-access.ts` (627) · `admin-generate-access.ts` (87) | E (`emailBody` con lo MEDIDO: Word de 10 secciones, Excel de 9 hojas, checklist de N tareas, calculadora, contrato, guía). Las primeras apariciones del slug de la pizzería (424, 385) son comentarios del gemelo EN | A |
| `netlify/shared/product-prices.ts` (82, con `sync-product-prices.py`) · `payment-links.ts` (81, tras el link, `sync-payment-links.py`) | E | D y E |
| Netlify env `VITE_STRIPE_PAYMENT_LINK_PLAN_CAFETERIA_MOVIL` (builds) | John crea el link; Claude: env + redeploy | D |
| `src/data/products-catalog.ts` (tras el bloque de l. 528) · `productos-changelog.ts` (tras 2161; `'1.0'`) · `productos-digitales-config.ts` (tras 632; 6 ficheros) · `src/pages/AdminGenerateAccess.tsx` (81) | E. ⚠️ **Registros anidados**: la clave nueva va a PRIMER nivel de `RAW` (2 espacios) y el bloque anterior se cierra con `  },`. La finca nació DENTRO de la heladería y lo arregló la pizzería (`git show 2e7a3af5 -- src/data/products-catalog.ts`). Hoy: 54 claves de primer nivel, 0 anidadas. Gate: `grep -c "^  '[a-z0-9-]*': {"` = 55 y 0 a 4 o 6 espacios | `sync --check` + grep |
| Hubs: ES `ProductosDigitalesHubPage.astro` (posición 1 con «✨ Nuevo», l. 68; **quitar la tarjeta de «Próximos», l. 1092**; la Taquería, 6.ª novedad, pasa a «Nuevo») · EN `DigitalProductsHubPage.astro` (junto a la pizzería, l. 136; «Próximos» l. 1070) · DE 65/945 · FR 66/946 · IT 66/946 · NL 63/943 · PT 65/945 · SPA `src/pages/ProductosDigitales.tsx:52` / «Próximos» 1075 | E (las 7 tarjetas de «Próximos» ya están traducidas, icono `Coffee`) | `hub-gate.py`, `tienda-gate.py` |
| `astro-site/src/lib/sinonimos-buscador.json` (229) | E: «cafeteria movil cafe movil coffee van cafe para eventos barra de cafe barista eventos catering de cafe espresso cafe de especialidad» | buscador del hub |
| `astro-site/public/llms-full.txt` (144) · `astro-site/src/lib/sitemap-lastmod.json` (702) | E (+1 cada uno, fecha del LIVE) | sitemap en el `dist` + GSC |
| `tareas/kit-tareas-cafeteria.ts` · `planes/plan-negocio-cafeteria.ts` · `planes/plan-negocio-cocteleria-eventos.ts` (`footerLinks`) | E (+1 enlace al plan: nada huérfano) | revisión |
| `equivalencias-es/censo-terminos-es.py:190-191` · `build_guia_es.py:3` · `datos/integracion.json` · `datos/matriz.json` | E: **54 → 55**; `terminos.json` solo si un término cambia en ≥ 5 de 21 países con fuente (candidatos: cortado, bollería, semidesnatada, nata, sirope, furgoneta; tope 0,05 M) | `build_guia_es.py --check --only <slug>` |
| `astro-site/public/lovable-uploads/ai-gallery/plan-cafe-movil-{hero,plan,barra,espresso,boda,feria,equipo}.jpg` | C (`generate-images`): distintas de `plan-cafeteria-*` y `tareas-cafeteria-*` | D (200) |
| `scripts/productos-digitales/emails/broadcast-plan-negocio-cafeteria-movil-eventos-lanzamiento-es.html` | C desde el de la finca; «Hola, colegas», negro/dorado, sin cifras movibles | `resend-broadcast.py --test` |
| `PAYMENT_LINKS_PENDIENTES_JOHN.md` · `CALENDARIO-V2-SEMANAL.md` (l. 558 «Próximamente» → LIVE; l. 574 decía «línea B»: ya es línea A 2.2) · `tienda-gate.py:89` (`PLANES_ES`, tras el LIVE) · handoff · `plan-cafeteria-movil/NOTA-CARRIL-CURSOR.md` | E / C | — |

**No se tocan**: `robots.txt` (`/plan-*-access` y `-library` ya bloqueados), `tienda.ts` y `alternatesFamilia` (hasta el gemelo EN, que se
DUPLICARÁ de este), `src/App.tsx`, `og-meta.ts` (muerta), `main.py` `PRODUCTOS` y el blog (carril Cursor: posts de cafetería y barista, en la nota).

## 6. Gates

**F2 (VPS)**: `ciclo.sh` → `main.py` exit 0 (idempotencia 0, caché, blancos 0, §9 13/13, censo `--fail`, demos 30/30) · `cifras_caf_es.py`
**D9 VERDE**: DSCR mínimo ≥ 1,25 · saldo mínimo > 0 · cobertura ≥ 98 % · holgura de caja A1 ≥ 15 % (A2/A3 ≥ 0, informativas) · exceso
0-5 % · neto ≤ techo del research · `pct_delivery` < 25 % y = cuota de ferias de la mezcla ± 1 pt · `PyG!G11` = 10 % · `calculadora_caf_es.py`
autotest VERDE · `docx_caf_es.py` (10 H1, A4, ≥ 6.000, 0 tokens) · `tandas_docx.py check` ×2 · `contrato_caf_es.py` · `barrido_es.py` 0 en
los 5 · `gate_restos_ft.py --rx-extra` 0 · `gate-no-latinos.py --only` · `censo-entregables.py --only <slug> --fail` · `paginas-gate.py` ·
Mac = VPS (sha256) · **una** revisión Opus final (cifras · legal · editorial). **F3**: `sync-product-prices.py --check` · grep de
registros anidados · `build_guia_es.py --check --only` · `gate-flujo-postpago.py --base <preview> --crypto-products all --crypto-exclude
pro-prompts-ebook --only <slug>`, después LIVE (A-E-f) · `scripts/astro-migration/{miselup,whatsapp,robots,hub}-gate.py` · `nombre-gate.py`
· `tienda-gate.py --base https://aichef.pro` · `fase6-gate.py https://aichef.pro` · curl al checkout cripto (`qa-cafemovil@aichef.pro`, purgar)
· sitemap reenviado · `git pull` antes de fiarse de un gate LIVE.

## 7. Plan F2 y F3 (rama `feat/plan-negocio-cafeteria-movil`; en el VPS, worktree de la rama, nunca `main`)

**F2 — Entregables** (tres pistas en paralelo desde el minuto 0; Mac ≤ 3 agentes, `istats` < 60 °C)
1. Mac · orquestador: SPEC corta (≤ 80 líneas) cruzando el research con §9 (mezcla, 14 partidas, 10 fijos, 4 filas, cobertura, ferias y
   canon, escalado, consumo, cobro y tramos, prohibidos). Commit F1 + SPEC.
2. **Opus** (implementador): `a.py`, `semilla_caf.py`, `datos_checklist.py`, `caf_version.py`, `main_caf.py`, `ciclo.sh`, `cifras_caf_es.py`,
   `barrido_es.py`; VPS: `ciclo.sh` + `cifras` hasta D9 (máx. 3 vueltas: fijo ±, propios, préstamo; si no cuadra, se para y reporta).
   **‖ Sonnet A**: `calculadora_caf_es.py` + autotest (VPS). **‖ Sonnet B**: contrato (generador + JSON; solo depende de la SPEC).
3. Con `cifras_caso_es.json` verde: `tandas_docx.py preparar` → **2 Sonnet** (`caf_es_a`, `caf_es_b`) → `check` ×2.
4. VPS · `docx_caf_es.py` + contrato + gates; copia a `public/dl/<slug>/` en el worktree; scp al Mac.
5. **Una** revisión Opus de los 5 ficheros + una ronda de arreglos; VPS regenera. `F2-NOTAS.md`. Commit + push (`Via: Claude Code`).

**F3 — Producto y lanzamiento**
6. Sonnet C (desde el paso 3: la ficha no lleva cifras movibles): ficha + 3 páginas + isla + dashboard + access gate. Sonnet D:
   functions ×4, `zona-app`, configs, catálogo (primer nivel), changelog, hubs ×8 con su «Próximos», buscador, `llms-full`,
   `sitemap-lastmod`, `footerLinks` ×3. Los dos con el diff de `769a0e26`; `emailBody` con lo medido en F2.
7. Mac · 7 imágenes (`generate-images`). VPS · censo de términos (54 → 55) + `build_guia_es.py --only` + `--check`; FAQ de países.
8. `sync-product-prices.py`; PR draft → preview de Netlify; gates contra el preview.
9. **John · Payment Link** (45 EUR, prosa sin viñetas, éxito → `/plan-negocio-cafeteria-movil-eventos-access?session_id={CHECKOUT_SESSION_ID}`).
   Claude: env, `sync-payment-links.py`, redeploy; merge (aprueba John); gates LIVE; sitemap.
10. Correo: hueco ES **13-dic 08:00Z** (> 30 días) → borrador por curl + prueba a John + routine desde el 13-nov; CALENDARIO, handoff,
    nota al carril Cursor. Commit + push.

## 8. Presupuesto F2 + F3

| Pieza | Quién / dónde | Tokens |
|---|---|---|
| `a.py` + semilla + checklist (~80) + versión/ciclo + cifras + calibración D9 | opus · VPS | 0,45 M |
| Calculadora (fork del parrillero + Escandallo de la pizzería + autotest) | sonnet · VPS | 0,22 M |
| Contrato (generador copiado + texto) | sonnet | 0,10 M |
| Word: pistas + 2 tandas ‖ + ensamblado + barrido | sonnet × 2 + orquestador | 0,30 M |
| Revisión opus final + arreglos | opus | 0,30 M |
| Capa de producto (≈ 41 ficheros + 6 + 7) | sonnet × 2 · Mac | 0,38 M |
| Imágenes (7) · guía de equivalencias · correo | API / sonnet / orquestador | 0,18 M |
| PR, preview, gates LIVE, merge | orquestador | 0,15 M |
| **Total F2 + F3** | | **≈ 2,1 M** → con F1, **≈ 2,8 M ≤ 5 M** (finca: 3,1 M real con 6 entregables) |

Reloj: F2 ≈ 1,75-2 h (ciclo del motor 24-26 s; calculadora y contrato en paralelo al implementador; redactores ~20 min; revisión ~30 min),
F3 ≈ 1 h + la espera del link → **≈ 3 h**. Lo dispararía: una 3.ª línea en el P&L, el Mes 1 girado sin necesidad, un anexo legal por
comunidades, verificar cita a cita lo que el producto no afirma o más de una ronda de revisión. Si la F2 pasa de 2 h, se cae el contrato.

## 9. Huecos que tiene que traer el research (el orquestador los cruza en la SPEC)

1. **Mezcla del caso** por tipo (bodas · empresa y congresos · celebraciones privadas · ferias y mercados con venta directa): nº al año ×
   invitados o clientes × € sin IVA → B4, B5, B6; la **cuota de ferias** en las ventas (< 25 %) y el **canon** del organizador (% o fijo).
2. **Tarifas** con fuente (por invitado, por hora, mínimo, desplazamiento) y precio de feria por bebida. **Consumo**: tazas por invitado
   según formato y horas; mezcla de bebidas (solo, con leche, vegetal); g de café por shot; ml de leche.
3. **Costes unitarios**: café de especialidad €/kg, leches €/l, vasos 4/8/12 oz y tapas €/ud, bollería €/ud → `coste_bebida`,
   `coste_comida` (bollería ≥ 10 % de las ventas), `pct_consumibles`, merma, `comision_tpv`, `pct_varios`.
4. **Inversión en 14 partidas exactas** (vehículo: Piaggio, furgoneta, remolque o triciclo; carrozado; espresso; molinos; generador o
   baterías con inversor; agua; frío; barra; menaje; rotulación; TPV; licencias; web y lanzamiento; stock), vidas útiles, imprevistos,
   propios, préstamo, tipo, plazo y carencia · **10 fijos exactos**, `seguros_ano`, `suministros_mes`, cuota del almacén base y fianza.
5. **Plantilla en 4 filas** (brutos, jornada de los fijos discontinuos, convenio, SMI 2026), **cobertura** (horas por evento, personas a la
   vez) y **estacionalidad** (12 pesos; Mes 1 sin girar salvo razón).
6. **Tabla de escalado** con fuente o «estimación del kit»: invitados → baristas, grupos o máquinas, molinos, kg de café, l de leche, vasos,
   potencia eléctrica y agua (misma tabla en calculadora, Excel y Word).
7. **Cobro y cancelación**: señal, calendario de pagos por canal, tramos proporcionados y recíprocos (TRLGDCU 85.6 y 87.2).
8. **Legal que el producto afirma** (con fuente primaria): registro sanitario autonómico de un establecimiento móvil, venta ambulante en
    ferias de vía pública (RD 199/2010 y ordenanza) frente a eventos privados, reforma del vehículo e ITV, agua de consumo, alérgenos
    (RD 126/2015), IVA del café servido y para llevar y de los refrescos azucarados, IAE, ¿comida testigo (RD 1086/2020 art. 30.8.d, M1 del
    parrillero) en una barra de café con bollería?, ruido del generador, fijos discontinuos (ET art. 16), Veri\*factu.
9. **Términos ES ↔ LatAm** para la guía y la FAQ: cortado, café con leche, bollería, semidesnatada, nata, sirope, furgoneta.

## 10. Lo que cazaron las revisiones y aquí nace resuelto

| Lección (origen) | Cómo nace resuelta |
|---|---|
| Payback con mayúscula a mitad de frase (pizzería M1, finca m1, parrillero m5) | `{PAYBACK}` entre comillas + `{PAYBACK_CAPEX}`; pista en `tandas_docx.py` (el de la pizzería ya la trae) |
| Equilibrio contable con dos lecturas mezcladas (finca M1) y umbral de caja solo del año 1 (finca M2) | pistas §8 y §10: «X eventos del tamaño medio o Y invitados con los eventos del caso»; umbrales de caja A1 y A2-A3 juntos |
| Food cost de UNA receta copiado en Supuestos (pizzería B1) | nota de `coste_bebida` + punto de Instrucciones + hoja `Instrucciones` de la calculadora (§4) |
| La landing promete lo que el fichero no trae (finca M9, pizzería M6, parrillero M4) | la ficha se escribe DESPUÉS de los ficheros; FAQ de países con términos que estén en `matriz.json`; rangos = tabla de escalado |
| Contrato: arras del art. 1454, 103.l, 90.2, tramos con huecos, obligaciones de quien no firma, 100 % sin descontar ahorros (finca M5, M6, m21-m25) · permisos sin dueño (parrillero m10) | gemela = el contrato ya arreglado de la finca; tramos «de X a menos de Y»; quién tramita cada permiso, por escrito |
| Notas del IVA del motor que hablan de alcohol (finca M7) | las 8 celdas medidas en §1, por `a.py` y `VOCABULARIO` |
| IVA sobre tasas y licencias (finca M8) | rótulo que empieza por «Licencias» (`RX_SIN_IVA` anclado con `^`) |
| «de 22 %», «Comunitat» (finca m2, m10) · slug en el checklist (pizzería m13) · mes de versión incoherente (pizzería m17, parrillero m6) | pista y `PROHIBIDOS` del brief · semilla con el nombre · `caf_version.py` con el mes del merge en los 4 ficheros |
| «15 años» (censo `RX_BIO_VIEJA`) · «campana»/«publica» de `motor.TILDES` · «azúcares añadidos» sin «edulcorantes» (pizzería M2) | «quince años» · guardas `RX_CAMPANA`/`RX_PUBLICA` · entrada heredada del `VOCABULARIO` + grep en F2 |
| Neto de la landing que no vale el año 1 (pizzería M8) | ficha sin cifras movibles; si da una, por año |

**Riesgos.** (1) **Demo §2.11.5**: ventana estrecha (128 € en el parrillero; 608 € de RAI la rompieron en r2): fijo ±100 € mirando los
`ensayos` de `inf.json`, y RD-34 con propios o préstamo (r3-r4). (2) **Negocio pequeño**: con 4 filas a jornada parcial el RAI tiene que
salir positivo con holgura; si no, plantilla o cuota de ferias, nunca código común. (3) **B5 mezcla paquetes por invitado y consumiciones
de feria**: lo traducen la nota y el Word; la calculadora separa los canales. (4) IVA soportado de la bebida al 10 % (leche al 4 %): nota.
(5) `Personal!C11` sin ponderar (finca m13): el Word cita horas (`I11`). (6) Guía en Letter: `gate_restos_ft` antes de meterla. (7) «Para
eventos, no calle»: ferias como jornadas de evento con canon, nunca venta diaria en vía pública; el copy no pisa el Plan Food Truck.
