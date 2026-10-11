# Plan de Negocio Paellero para Eventos ES → 2.2 · F1: camino de construcción

> Sesión Claude Code, 11-oct-2026. Arquitecto de F1, una pasada. Medido en el VPS (`/root/wt-pae`, venv `/root/venv-guias`,
> scripts de medición fuera del árbol, ya borrados) sobre `2d6cac44` (paellero 1.2 LIVE, PR #115 + #116). Plantilla:
> `../catering-es-2_0/` (F1-camino, SPEC, F2-NOTAS §3/§5-§7, REVISION-FINAL). Las cifras del caso las fija el research (fichero aparte).

## 0. Decisión en tres líneas

1. **Mismo camino que el Catering ES 2.2**: motor ES de línea A (`planes-v2_0/main.py` + `grupo_a.py`) sobre una copia del **Food Truck ES v2.2**, módulo nuevo `contenido_plan_negocio_paellero_eventos/a.py` **clonado del del catering** (su `VOCABULARIO` vale al 80 %), y en `paellero-2_2/` las copias adaptadas de `semilla`, `datos_checklist`, `cifras`, `tandas_docx`, `docx`, `calculadora`, `arreglos_d9` y gates.
2. Driver **sin permutar**: cubiertos/día = **invitados (raciones) por evento**, ticket = **precio por invitado sin IVA**, días de apertura = **eventos al año**. Equilibrio del libro en invitados/evento e ingresos; los eventos/año, token derivado del Word.
3. **Cero cambios en código común** (`VOCABULARIO_SIN_TILDES = True` ya es opt-in): sin regresión obligatoria. Rehacer 4 ficheros (plan xlsx, checklist, calculadora, docx), parches de texto en 7. **F2 + F3 ≈ 1,45 M**.

## 1. Inventario del paellero 1.2 (VPS, openpyxl/python-docx)

| Fichero | Molde (`motor.detectar`) | Medido | Defectos que quedan |
|---|---|---|---|
| plan-financiero | **B-δ** (6 hojas: Resumen, P&L Año 1, Proyección 3 años, Break-even, Mix B2C-B2B, KPIs) · 128 fórmulas | ingresos 214.950 € · neto 109.822 € (**51 %**) · inversión 3.790 / 9.670 / 23.110 | **sin personal ni amortización ni IVA/IS/préstamo/caja**; `Break-even!B9 = 8.400 / 825 = 10,18 eventos/año` (landing: «18-22»); tasas tecleadas en fórmulas (`P&L!B9 = B7*0.28`, `B11 = B7*0.12`, `Proyección!D12 = D11*0.27`, `C14 = C11*0.13`); «Ayudantes freelance» (P&L A11, Proy. A14); «Tarifa plana 80€/mes» (Resumen F6, P&L fila 13); `KPIs!A2` «Benchmarks … España 2026» sin fuente; `Break-even!B6` tickets 850/1.850 tecleados |
| calculadora | **calc-gamma** (`Calculadora pricing` + `10 ejemplos validados`) | 15 fórmulas, 6 DV | **sin IVA**; margen tecleado (`B32 = B29*0.55`, `B33 = 0,55`); `B23` «ayudantes freelance» 120 €/jornada; recargos de precio tecleados (+25/+18/+10/+8/+4 %, −6 %); hoja «10 ejemplos **validados**» «España 2026» (valores fijos, no salen de las fórmulas) |
| checklist | **C4** (1 hoja, 104 hitos 19/10/27/16/14/18, DV ✓/☐/N/A, contador) | 645 celdas | `D6` tarifa plana 80 €; `C10`/`C13` curso y **carnet de manipulador**; `D12` «RGSEAA — clave si transportas alimentos»; `D30` «si subcontratas freelance»; `D108` mise en place en **«Domicilio** o cocina» (RD 1021/2022 art. 13.5.b lo prohíbe para eventos); `D36` cita **PATRICOVA** (es el plan de **inundaciones** de la C. Valenciana) e «INFOCYL» (el de CyL es INFOCAL); `C35` «si food truck» |
| proveedores | **P2** («88 proveedores», 10 bloques) | 69 «Validado» + 19 «Investigar» | `A1` «88 Proveedores Reales», `A2` «Validados España 2026», `G5:G92` «Validado», docProps título |
| plan de negocio docx | 118 párr., 2 tablas, **0 Heading**, ~2.450 palabras | | «España 2026» (p1, p28); inversión 3.500/8.500-12.000/25.000 (p7, p12, p68); «Sin licencia de actividad clasificada» (p13); «ayudantes freelance… 120 €/jornada» (p14, p65); mercado 3.200 M€ / 12-14 % / 38 % sin fuente (p30); «10 competidores reales» (t0, nombres sin verificar); ingresos 215-245 K, neto 47-62 K «margen 22-27 %» (p69-p70, el xlsx dice 51 %); «Break-even 18-22 eventos» (p71); «6 hojas» (p67); «88 verificados» (p92); mise en place D-1 sin sitio (p50) |
| 6 docx restantes | A4, docProps 2013-12-23 «AI Chef Pro» | ver §6 | |

**Contenido que vale la pena llevar a la 2.2** (fuente de las pistas de redacción y del módulo):
- **Concepto**: paella y arroces cocinados **en directo** en el evento (gas y leña), show cooking con narrativa, 12 arroces de carta, modelo híbrido sin local.
- **Mezcla**: `Mix B2C-B2B` A5:F13 — 4 tipos B2C (57 eventos) y 5 B2B (90) con pax, ticket y temporada → mezcla de eventos del docx §2-3 y días de cobro.
- **Precio y raciones**: carta (12 arroces, food cost 7,60-16,50 €/ración, PVP 22-48 €/ración) y experiencias (12-55 €/pax).
  ⚠️ Chocan con la calculadora 1.x (17-25 €/pax) y con los tickets del P&L (≈ 20-25 €/pax): **el research fija el precio medio** y los tres ficheros quedan dentro de su rango.
- **Escalado**: tabla 1 del manual 1.2 (8 diámetros → raciones, arroz, caldo, quemador); tabla 2 (50/100/200 invitados → paelleras y equipo: 1 paellero hasta ~80, + ayudante, 2.º paellero desde ~150).
- **Política comercial (contratos 1.2)**:
  - B2C: **30 % de anticipo + 70 % el día del evento**; cancelación del cliente 30 / 50 / 75 / 100 % del total (> 60 días / 60-30 / < 30 / 72 h), simétrica si cancela el paellero.
  - B2B: 30 % + 70 % a 30 días de factura; retiene 0 / 30 / 60 % del anticipo (+ 200 € de gestión) y 100 % a < 15 días; recargo de 0,95 €/km fuera del radio.
- **Estacionalidad** (`P&L Año 1` fila 7): 2,1 · 2,1 · 5,5 · 6,7 · 12,2 · 14,7 · 13,5 · 8,9 · 13,5 · 11,0 · 4,2 · 5,5 % → `ESTACIONALIDAD` (la forma; el research puede afinarla).
- **Riesgos** (t1, 7 filas) y **operativa D-30 → D+15** (p45-p63) → ranuras de §6 y §9 del docx.

**Se conserva de la 1.2 (no se toca salvo los parches de §6)**: manual técnico ampliado (4.437 palabras, 14 H1, 10 tablas, alioli con ovoproducto p151); catálogo con capacidades alineadas al manual; contratos 1.2 (IVA 10 % en B2B p49, cancelación B2C escalonada y simétrica, fuero del consumidor p39); **anexo legal autonómico** (docx p93-p110, nombres de planes revisados en la 1.2) → se trasplanta al docx 2.2; pestaña «88 proveedores» (firma P2: no renombrar).

## 2. Camino (confirmado: el del catering) y qué se reutiliza

| Pieza | Decisión | Por qué |
|---|---|---|
| `planes-v2_0/main.py`, `grupo_a.py`, `motor.py`, `inject_cache.py`, `censo-entregables.py`, `gate-no-latinos`, `paginas-gate` | **tal cual** | el paellero entra como 7.º miembro de línea A; `main.py` ya lo lista (l. 125) y carga `contenido_<pid>` |
| `contenido_plan_negocio_paellero_eventos/a.py` | **clon del catering** y reescribir datos | `VOCABULARIO` (driver, «en sala», «el local», delivery → **paella para recoger**, restos m8/m9) se queda; cambian `CONCEPTO`, `SUPUESTOS`, `LINEAS_INGRESO`, `PLANTILLA`, `COBERTURA`, `FIJOS`, `UMBRALES`, `ESCENARIOS`, `ESTACIONALIDAD`, `INSTRUCCIONES`, `RECALIBRADO` |
| `semilla_pae.py` + `datos_checklist.py` | **copia** de `semilla_cat.py` con datos nuevos | son datos (14 partidas en filas 7-20, fijos 26-35, títulos, 83 tareas). **Desde el día 1**: `Instrucciones!A3` del checklist + docProps `description`/`keywords` de los 2 xlsx (bloqueante B1 del catering) |
| `ciclo.sh`, `barrido_es.py`, `cifras_pae_es.py` | **copia** con PID/rutas | `cifras` lee la caché por rótulo: solo cambian ~8 regex del `MAPA` (p. ej. «cuota mensual de la cocina compartida»). Incluir desde el inicio los 5 tokens de año 2 (M3: `BE_INGRESOS_CAJA_A2`, `HOLGURA_CAJA_A2`, `BE_EVENTOS_CAJA_A2`, `INVITADOS_EVENTO_A2/A3`) |
| `gate_restos_ft.py` | **parametrizar** (`--pid`, `--rx-extra`, `--excluir`; por defecto = catering) | en el paellero «food truck» es **legítimo** en `guia-tipos-paellero-roadmap-food-truck.docx` y en el título de esa guía: se excluye el fichero y se añaden los restos del **catering** (`estaciones temáticas`, `cocina central`, `plan-catering`, `Catering Temático`) |
| `tandas_docx.py`, `docx_pae_es.py`, `BRIEF-REDACTORES.md` | **copia** | `PISTAS`, `PROHIBIDOS`, `PERMITIDAS`, `FIJOS` y la gemela son del producto; la lógica (preparar/check/ensamblar) no cambia |
| `calculadora_pae_es.py` | **copia** de `calculadora_cat_es.py` | declarativa: se reescriben `ENTRADAS`, `SALIDAS`, `EJEMPLOS`, `INSTRUCCIONES` (§5) |
| `arreglos_d9.py` | **copia**, lista nueva (§6), partiendo de los ficheros de `2d6cac44` | repetible e idempotente, como el del catering |
| `regresion5.py` | no hace falta (no se toca `grupo_a`); correrlo una vez cuesta 0,02 M | guarda barata |

**Decisiones de modelo para el research/SPEC** (no son cifras):
- **Forma jurídica SL unipersonal**: el motor calcula IS 15/25 % + BIN, no IRPF. Nota en Supuestos, checklist F1 y docx: «si arrancas como autónomo, el resultado tributa en IRPF».
- **Cocina de apoyo autorizada** (`alquiler_mes` = cuota de **cocina compartida por horas u obrador**, con almacén de paelleras y bombonas): la mise en place de la 1.x se hacía «en domicilio».
- **Personal**: plantilla en las **4 filas** del molde: dueño-paellero · ayudante fijo · bolsa de ayudantes **fijos discontinuos** · 2.º paellero fijo discontinuo. `COBERTURA` = horas por evento × personas a la vez.
- **Canales**: `pct_delivery` = **paella para recoger, sin servicio**, ≥ 5 % con comisión > 0 (la demo §2.11.9 falla con 0). Bebida pequeña, nunca 0 sin probar las demos.
- **Cobro**: días de cobro = mezcla (B2C 0 días, B2B 30). El anticipo del 30 % no se modela: nota en Tesorería.
- **Crecimiento**: el de los años 2-3 cae en **invitados por evento** con los mismos eventos. El docx lo dice así (M2).

## 3. Checklist: 104 hitos en 1 hoja → molde de 6 hojas del FT ES (83 tareas, 12/16/14/10/16/15)

Columnas del FT: `OK · TRÁMITE / ACCIÓN · RESPONSABLE · PLAZO · NOTAS`; DV, formato y contadores los rehace `checklist_ok_y_contador`.

| Pestaña | Nº | Origen (fila del 1.2) y lo nuevo |
|---|---|---|
| F1 - Constitución y fiscalidad | **12** | forma jurídica (SL / autónomo, ver §2) · 036/037 + **IAE 677.9** (r7) · RETA con cuota reducida **sin cifra** (r6) · certificado digital · cuenta y tarjeta (r8+r20) · gestoría + facturación **Veri\*factu** (r19) · 303 al 10 % (r23) · 111 + pagos a cuenta del IS (o 130 si autónomo) (r22) · 390 + 347 (r24) · RGPD (r15) · LSSI + aviso legal + cookies (r16+r17) · condiciones B2C: precio final con IVA, **sin desistimiento** en servicio con fecha (TRLGDCU 103.l) y cancelación (r18) |
| F2 - Sanidad, fuego, gas y permisos | **16** | APPCC itinerante (r9; PCC: cocción, frío del marisco, alioli con ovoproducto) · registro sanitario **autonómico por declaración responsable** (r11) · **RGSEAA solo si suministras a otros establecimientos** (r12 corregida) · **cocina compartida u obrador autorizado** para mise en place y almacén (nuevo; contra r108) · agua: análisis solo con depósito propio (r14) · RC ≥ 600.000 € + intoxicación (r27+r28) · seguro de furgoneta de uso comercial (r29) · equipo + cancelación/fuerza mayor (r32+r33) · autorización o comunicación municipal y del recinto por evento (r34) · **época de peligro de incendios**: plan autonómico y uso del fuego en terreno forestal y su franja (Ley 43/2003 de Montes + norma autonómica) (r36) · **gas**: aparatos con marcado CE (Reglamento (UE) 2016/426), mangueras y reguladores en fecha · **transporte de bombonas** en la furgoneta (exención ADR 1.1.3.6) · **extintor** revisado (RD 513/2017) + manta/arena en cada evento · venta ambulante **solo** en ferias o vía pública (r35) · hojas de reclamaciones · residuos y aceite usado |
| F3 - Equipamiento y proveedores | **14** | paelleras por diámetro según la tabla del manual (r39-r41) · quemadores de gas y anillos (r42) · trípode y leña, solo con permiso (r43+r45) · bombonas + reserva (r44) · cuchillería, tablas de color y cucharas (r46-r48) · vajilla, cubertería y cuencos de alioli para tu dotación (r49-r51) · neveras, acumuladores y sondas (r62+r64) · báscula (r63) · cajas de transporte + mantel de show cooking (r59+r60) · EPI de calor (r61) · arroz DO con precio trimestral (r52) · carne, marisco y verdura con trazabilidad (r53-r55) · caldos, azafrán y pimentón DO (r56+r57) · furgoneta y TPV/software de presupuestos (r58 + FT) |
| F4 - Personal | **10** | bolsa de ayudantes **fijos discontinuos** (art. 16 ET) o ETT, nunca facturas de autónomo (contra r30 y el «freelance» del P&L) · alta en SS antes de cada llamamiento · **formación en higiene alimentaria** acreditada por la empresa (Reglamento (CE) 852/2004, anexo II, cap. XII; contra r10/r13) · alérgenos (Reglamento (UE) 1169/2011) · PRL: quemaduras, gas, calor y cargas + EPI · registro horario (art. 34.9 ET) · información de datos al trabajador · 2.º paellero desde ~150 invitados (manual, tabla 2) · guion del show cooking (r113) · fichas por diámetro (manual) |
| F5 - Marca y captación | **16** | 30 de la 1.2 condensadas: identidad (r68) · dominio y correos (r69) · web con formulario + SEO técnico (r70+r79+r80) · fotos y vídeo (r71+r72) · GBP + reseñas (r73+r81) · Instagram/TikTok/Pinterest (r74+r75+r77) · LinkedIn (r76) · WhatsApp Business (r78) · directorios de bodas (r82) · directorios B2B + Hosply (r83+r65) · wedding planners: lista y outreach (r86+r87) · visita con degustación (r88) · agencias, empresas y hoteles (r89+r92+r94) · **ayuntamientos**: contrato menor y **factura electrónica por FACe** (r93 + nuevo) · dossiers B2B/B2C (r90+r91) · publicidad + referidos + showroom (r95-r99) |
| F6 - Primer evento y 90 días | **15** | briefing (r102) · visita técnica: punto de fuego, viento, acceso y agua (r103) · presupuesto + **anticipo 30 %** (r104) · contrato firmado (r105) · menú y alérgenos por escrito · plan B de lluvia y viento (riesgos t1) · pedidos (r106) + marisco D-1 (r107) · mise en place en la **cocina autorizada** (r108 corregida) · carga con la checklist del manual (r109) · salida, montaje y encendido (r110-r112) · servicio + show cooking (r113) · recogida, limpieza y foto (r114) · cobro y factura (B2C el día; B2B a 30 días) (r115) · reseña + agradecimiento al planner (r116+r118) · CRM, costes reales y cierre trimestral (r117+r119) |

**Verificar en F2 con fuente primaria** (una pasada, solo lo que se afirma): exención ADR 1.1.3.6 para propano (UN 1965) en furgoneta y su extintor · RD 513/2017 (mantenimiento de extintores) · Reglamento (UE) 2016/426 · Ley 43/2003 art. 44 (uso del fuego) · Ley 25/2013 (FACe: obligados y umbral) · **límite de 1.000 € en efectivo** (Ley 7/2012 art. 7, redacción de la Ley 11/2021), que choca con el contrato B2C p23. Lo demás ya lo verificó el catering: RD 1021/2022 art. 13.5.b y DF 1.ª, TRLGDCU 103.l y 97.1.m, IAE 677.9, Ley 37/1992 art. 91.Uno.2.2.º, ET arts. 1.1, 16 y 34.9.

## 4. Docx del plan: reescritura en las 131 ranuras del FT ES (confirmado)

- **Reescritura**, no arreglo: el 1.2 tiene 0 encabezados, ~2.450 palabras y cifras de un modelo que desaparece. Molde FT ES: 131 párrafos, 10 H1, ~61 ranuras de texto, **A4**, autor `AI Chef Pro`, todas las cifras por token.
- **Gemela = Catering ES 2.2** (`catering-es-2_0/textos/cat_es_{a,b}.json`): mismas ranuras, en español y del mismo oficio (eventos, B2C + B2B, sin local). Sustituye a la gemela EN, que el paellero no tiene. Redacción con 2 Sonnet en paralelo (`pae_es_a` §1-5, `pae_es_b` §6-10).

Fuentes por ranura:

| Ranura | Fuente |
|---|---|
| Argumento y longitud | la gemela del catering |
| §1-2 concepto y modelo | docx 1.2 p6-p27, sin cifras |
| §3 mercado | research (DataForSEO y fuentes citadas). Fuera 3.200 M€, 12-14 % y 38 % |
| §4 competencia | por categorías, salvo que el research verifique nombres. Fuera la tabla t0 |
| §5 marketing | p38-p43 |
| §6 operaciones | p45-p63 + manual (raciones, paelleras y equipo por invitados) |
| §7 personal | fijos discontinuos (catering p43/p64/p90) |
| §8 finanzas | tokens + lecciones M2/M3 (crecimiento en invitados; holgura del año de carencia y del año 2) |
| §9 riesgos | t1 + marco legal verificado (§3) |
| §10 conclusiones | tokens |
| Política comercial | contratos 1.2: B2C 30 % + 70 %, 30/50/75/100 %; B2B 30/70, 0/30/60/100 % |

- **Anexos** tras la ranura 131, bajo un H1 «Anexos» (gate: **11 H1**):
  - A, fuego al aire libre por CCAA: p93-p110 de la 1.2, trasplantados tal cual (ya revisados).
  - B, correo a wedding planners: p111-p117 con `[precio por invitado]` en lugar de «35 €» y sin «calendario 2026».
- **Gates**: 11 H1, A4, ≥ 6.000 palabras, 0 tokens sin resolver, cifras = caché, 0 no latinos, 0 prohibidas. Prohibido: «freelance», «validad», «España 2026», «carnet», «tarifa plana», «solopreneur», «sin licencia», cifras 1.x (3.790, 9.670, 23.110, 3.500, 8.500, 12.000, 214.950, 215.000, 245.000, 109.822, 47.000, 62.000, 10,18, «18-22 eventos», 51 %, 55 %, 80 €/mes, 120 €/jornada). «food truck» solo en el título de la guía.

## 5. Calculadora ES: fork de `calculadora_cat_es.py` (hojas `Calculadora` · `Ejemplos` · `Instrucciones`, firma calc-beta)

**Entradas**
- Canal: Particular / Empresa.
- Invitados.
- Tipo de arroz: lista de los 12 de la carta. Coste de materia prima por ración por búsqueda en una tabla al pie de `Ejemplos`, con los food cost de la carta (7,60-16,50 €).
- Diámetro de paellera: lista del manual (50-150 cm). Da las raciones por paellera, por el número bajo del rango (tabla 1).
- Gramos de arroz por ración (100).
- Coste de gas por paellera y servicio [estimación del kit].
- Ayudantes y horas por persona, a €/h bruto × (1 + SS 33 %).
- Menaje y desechables por ración: 0 si los pone el cliente; sustituye al −6 %.
- Alquileres repercutidos (carpa si llueve); sustituye al +4 %.
- Km de ida.
- Margen bruto objetivo.
- Suplemento de show cooking en %, 8 % por defecto (el de la 1.x).

**Salidas**
- **Logística**:
  - nº de paelleras = REDONDEAR.MAS(invitados / raciones);
  - **paelleros = REDONDEAR.MAS(paelleras / 3)** (manual p112);
  - **kg de arroz**, litros de caldo y gas.
- **Precio**:
  - coste directo;
  - **precio por invitado sin IVA** (redondeo a 0,50 €) y **con IVA**;
  - desplazamiento = km × 2 × **0,95 €/km**, línea aparte sin margen (la tarifa del contrato B2B);
  - subtotal, IVA 10 %, total.
- **Cobro**:
  - **anticipo 30 %** y resto (B2C el día; B2B a 30 días);
  - **importe retenido por tramo de cancelación** de cada canal (contratos 1.2);
  - **margen calculado**.
- La propina va fuera del total, como nota.

**Ejemplos, por las mismas fórmulas** (sustituyen a los «10 ejemplos validados»):
- cumpleaños particular, 30 invitados, valenciana;
- boda con wedding planner, 110 invitados, marisco + show cooking;
- fiesta de un ayuntamiento, 220 invitados, 2 paelleros.

**Autotest pycel** frente al espejo Python (± 0,01 €) y DV en las entradas de texto.

## 6. Los otros 7 ficheros: solo lo que contradice el modelo nuevo (`arreglos_d9.py`)

| Fichero | Dónde | Corrección |
|---|---|---|
| modelos-contrato | p2 | «Plantillas **validadas con asesor legal**» → «Plantillas orientativas: revísalas con tu asesor antes de usarlas» |
| modelos-contrato | CUARTA (tras p29) | + «Al tratarse de un servicio de comida con fecha determinada, el Cliente no dispone del derecho de desistimiento (art. 103.l TRLGDCU)» (art. 97.1.m) |
| modelos-contrato | p23 | «o efectivo el día del evento» → «… (en efectivo, solo hasta el límite legal de pagos en efectivo)» tras verificar §3 |
| plantilla-proveedores | `A1`, `A2`, `G5:G92`, docProps | «88 Proveedores Reales» → «88 proveedores»; fuera «Validados España 2026»; 69 «Validado» → «Por verificar» (DV Por verificar / Contactado / Homologado / Investigar). La hoja **no** se renombra |
| catálogo | p1, p2, p6 | «precio actualizado» → «precio orientativo: confírmalo con el proveedor»; «España 2026» → «Edición 2026» |
| carta | p1 | «Recetas profesionales · **Escandallo** · Maridaje» → «… · Food cost por ración · Maridaje» (no hay escandallo desglosado: lección M5) |
| 10 experiencias | p6 | «Cada una tiene su propio dossier visual» → «… para la que puedes preparar su dossier» (el kit no trae los dossiers) |
| guía sistemas + food truck | — | **sin cambios** (inversión 26.150-86.150 € de su tabla, coherente con su p66; «food truck» es su tema) |
| manual técnico | — | **sin cambios** (sin «carnet» ni «freelance»; capacidades = calculadora) |
| los 7 | docProps | autor `AI Chef Pro`, fecha ≥ 2026, sin «python-docx», A4 (ya lo están; el gate lo comprueba) |

Si el research fija un precio medio por invitado fuera de los rangos de la carta (22-48 €) y de las experiencias (12-55 €), se ajusta el modelo, **no** la carta.

## 7. Landing, dashboard, changelog y hubs

**Ficha** `astro-site/src/data/productos/planes/plan-negocio-paellero-eventos.ts`:

| Afirmación | Líneas | Corrección |
|---|---|---|
| «España 2026», «datos reales del mercado … 2026» | 32 · 42 · 140 · 142 · 173 | «España»; fuera «datos reales 2026» salvo las cifras que cite el research |
| «DOCX 60+ pp» | 32 · 42 · 126 · 142 · 270 | «más de N palabras» (medido en el docx 2.2) |
| «sin licencia (de actividad) clasificada» · «sin plantilla fija» · «ayudantes freelance» | 76 · 244 | «sin local propio: cocina compartida autorizada y permisos por evento» · «ayudantes fijos discontinuos» |
| inversión «3.500-25.000 EUR», «4-7x menor … 70-130K», «Inversión Mínima 3.500 EUR», «3 escenarios de inversión» | 76 · 143 · 178 · 244 · 256 | inversión total del modelo (token) y escenarios pesimista / realista / optimista; fuera la comparación |
| «break-even 18-22 eventos año 1», «break-even por número de eventos» | 84 · 143 · 178 · 256 | «equilibrio en invitados por evento y en ingresos (el Word lo traduce a eventos al año)» (M6) |
| «Formato ICO/microcrédito», «formato estándar que piden bancos» | 84 · 256 | «préstamo con su cuadro, DSCR y tesorería de 12 meses» |
| «Plan Financiero Excel (6 hojas)» | 143 · 270 | **9 hojas** |
| «10 ejemplos validados», «precio sugerido + margen» | 144 | «3 presupuestos calculados: precio con IVA, anticipo, cancelación y margen calculado» |
| «RGSEAA», «tarifa plana 80 EUR/mes», «104 hitos» | 147 · 240 | registro sanitario autonómico · cuota reducida sin cifra · **83 tareas** |
| «Receta + escandallo + maridaje» | 148 | «… + food cost por ración + maridaje» |
| «Roadmap food truck … 30-75K EUR» | 152 · 212 | «26.000-86.000 €» (tabla de la guía) |
| planes «INFOCA, **PATRICOVA**, PLADIGA, **INFOCYL**, IBANAT, SOSDeiak, PIDOM» | 80 · 175 · 248 | los 8 del anexo (INFOMA, INFOCAT, INFOBAL, INFOCA, plan valenciano, plan vasco, PLADIGA, INFOCAL) |
| «Modelo Híbrido … **Validado**», «88 Proveedores Reales **Validados**», «contactos verificables … (validado / investigar)» | 176 · 177 · 251-252 | sin «validado»; «con web y zona; estado Por verificar» |
| `updateNote` | 299 | «Producto actualizado · Versión 2.2 · octubre 2026» |

**Capa comercial, no se toca sin John** (precio tachado `€165`, testimonios). Pero **Marc Esteve** (`:65` reseña JSON-LD y `:163`), «Empecé con 4.200 EUR siguiendo el escenario mínimo viable», cita un escenario que la 2.2 **elimina**: decisión de John, como la de Yuki en el catering.

**Dashboard** `src/pages/PlanNegocioPaelleroEventosDashboard.tsx` (isla `PlanNegocioPaelleroEventosLibraryIsland.tsx`): `desc` de las líneas **19** (60+ páginas, España 2026, 10 competidores), **26** (3.500-25.000, break-even 18-22), **33** (10 ejemplos validados), **54** (RGSEAA, 104 hitos), **61** (escandallo) y **89** (30-75K). `src/components/plan-negocio-paellero-eventos/*` solo lo usa la SPA `src/pages/PlanNegocioPaelleroEventos.tsx`, que no se construye: **no tocar** (la 1.2 lo tocó; da igual).

**Changelog** `src/data/productos-changelog.ts:1569-1571`: `version '2.2'`, `updated`, y entrada 2.2 honesta arriba de la 1.2 (motor nuevo: personal, IVA/IS, préstamo, tesorería, 9 hojas, calculadora con IVA, checklist de 83).

**Hubs**: descripción con «60+» + 1.ª viñeta «DOCX 60+» + 2.ª viñeta «validado». La 3.ª (anexo de fuego, 8 CCAA) es verdad y se queda.

| Hub | Líneas |
|---|---|
| ES `ProductosDigitalesHubPage.astro` | 596 · 598 · 599 |
| EN `DigitalProductsHubPage.astro` | 558 · 560 · 561 |
| DE | 517 · 519 · 520 |
| FR | 518 · 520 · 521 |
| IT | 518 · 520 · 521 |
| NL | 515 · 517 · 518 |
| PT | 517 · 519 · 520 |

**No se tocan**: `get-download-urls.ts:961+` (mismos 11 nombres de fichero), `product-prices.ts:60`, `llms-full.txt:126` (solo enlaza), `products-catalog.ts:499` (sin cifras) y los 15 posts con banner (sin cifras).

## 8. Correo

El borrador `42ccda21` «Actualización Plan de Negocio Paellero 1.2 (ES)» (`emails/broadcast-plan-negocio-paellero-eventos-v1.2-es.html`, cita «versión 1.2» y «104 hitos») lo programa el 19-oct la routine `trig_01WdpgX2KtUL9PbTyXHC4dVg` para el **18-nov 08:00Z**. **No se toca aquí.** Con la 2.2 LIVE queda **obsoleto**: en F3, sustituir su contenido por el de la 2.2 en el mismo hueco (o avisar a John) **antes del 19-oct** si la 2.2 ya está LIVE, o reemplazar el broadcast programado después.

## 9. Riesgos

- **Tesorería con la estacionalidad 1.x** (enero y febrero al 2,1 %): el saldo mínimo > 0 puede exigir más fondo de maniobra o más préstamo. Calibrar como el catering (D15) e informar también la **holgura del año 2** (M3).
- **Restos cruzados**: al clonar del catering y sembrar del FT pueden quedar «cocina central», «estaciones temáticas», «food truck» o «plan-catering». Por eso el gate parametrizado del §2, y la excepción de la guía.
- **Rótulos de importe sin palabras de recuento** (`gate_formatos`), **filas del molde** (4 de plantilla, 14 de inversión, 10 de fijos: no añadir ni suprimir) y el **driver solo por `VOCABULARIO`**: gotchas medidos en el catering (F2-NOTAS §5).
- **Precio**: carta, experiencias, calculadora y modelo deben contar la misma historia de €/invitado (§1).
- **Versión**: el motor estampa «Versión 2.2 · septiembre 2026» en los xlsx (desviación aceptada en el catering); la landing dice octubre.

## 10. Presupuesto F2 + F3

| Pieza | Quién / dónde | Tokens |
|---|---|---|
| Módulo `a.py` (clon) + `semilla_pae.py` + `datos_checklist.py` (83) + `cifras` + `ciclo.sh` + calibración D15 | opus · VPS (un implementador) | 0,40 M |
| Textos del módulo (notas de Supuestos, partidas, plantilla, Instrucciones) | dentro del implementador o sonnet | 0,12 M |
| Docx: 2 tandas Sonnet ‖ + `docx_pae_es.py` con anexos | sonnet × 2 + opus | 0,30 M |
| Calculadora (fork) + autotest | sonnet | 0,10 M |
| `arreglos_d9.py` (§6) + gate de restos parametrizado | sonnet · VPS | 0,06 M |
| Landing, dashboard, changelog y 7 hubs | sonnet · Mac | 0,08 M |
| Verificación legal F2 (6 citas de §3, una pasada) | sonnet | 0,05 M |
| Gates + **una** revisión opus final | opus | 0,20 M |
| F3: PR, preview, gates LIVE (E-f, miselup, whatsapp), páginas, correo | orquestador | 0,14 M |
| **Total** | | **≈ 1,45 M** (≤ 1,5 M; F1 ≈ 0,3 M) |

Lo que lo dispararía: permutar el driver, mantener 104 tareas, conservar la tabla de competidores sin verificar, o arreglar el docx 1.2 en vez de reescribirlo.
