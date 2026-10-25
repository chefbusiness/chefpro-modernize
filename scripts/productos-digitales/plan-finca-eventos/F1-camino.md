# Plan de Negocio: Finca de Eventos y Bodas (ES, 45 €) · F1: camino de construcción
> Sesión Claude Code, 25-oct-2026. Arquitecto de F1, una pasada. Producto **NUEVO** (sin 1.x), slug `plan-negocio-finca-eventos-bodas`,
> familia Planes, línea de eventos (hermanos LIVE a 45 €: Catering Temático, Paellero y Parrillero-Asador, los tres 2.2).
> Medido en el VPS (`main` @ `bb566c8a`, worktree `/root/wt-finca` de la rama `tmp-finca-dryrun`, salida en `/root/tmp-finca-f1`; los
> tres ya borrados, `git status` vacío, `/root/wt-pdf` de otra sesión sin tocar). Caso, mercado y normativa: `F1-research-finca.md`
> (otro agente). Aquí, el CÓMO, lo que se toca y los huecos que el research tiene que llenar dentro de lo que el motor admite.

## 0. Decisión en tres líneas

1. **Contenido del PARRILLERO 2.2 + semilla de la HELADERÍA**: módulo nuevo `planes-v2_0/contenido_plan_negocio_finca_eventos_bodas/a.py`
   clonado del `a.py` del parrillero (motor de eventos SIN permutar, `VOCABULARIO` de eventos, notas de cobro, señal y fijos
   discontinuos) con los injertos de local fijo del de la heladería (renta real, obra amortizable, Mes 1 girado y pagas extra,
   `IVA_COMPRAS`, `COBERTURA` de 4 claves, `RECALIBRADO = ()`); `semilla_fin.py` = `semilla_hel.py` sobre los mismos xlsx LIVE de la
   **panadería 2.2** (19 partidas, 6 filas de plantilla, 10 fijos, A26-A28 «Fianza / Alquiler previo / Imprevistos de obra»). Ni el
   origen FT (14 partidas, 4 filas de plantilla: no caben ni la obra ni el personal por servicio), ni el paellero (mismo motor que el
   parrillero, más antiguo y con el fuego, que aquí no toca), ni el catering (su «cocina central» es una cuota y su `a.py` es anterior
   a las lecciones de paellero y parrillero). Una finca es un ESPACIO FIJO que vende EVENTOS: renta, obra y temporada del local fijo;
   driver, contrato y calculadora de la línea de eventos.
2. **Cero cambios en código común**, y **no** se mete el pid en `PRODUCTOS` (`main.py:117-128`; `demo_moldes` exige 30, `main.py:749`).
   Modelo = **finca arrendada con banquete propio en exclusiva** (lo que promete la tarjeta de «Próximos»: «aforo, packs de menú
   cerrado, estacionalidad de bodas y personal por servicio»): 2 líneas, banquete con la finca incluida y barra libre, todo al 10 %.
   Las palancas existen; las tres que no (coste de mercancía por línea, IVA de la renta, cobro anticipado) van por nota (§2).
3. **6 entregables** (plan xlsx, Word de 10 H1, checklist ~84 tareas, calculadora de presupuesto de boda —fork de la del parrillero—,
   modelo de contrato de reserva —molde físico del contrato del parrillero— y guía de equivalencias), **≈ 50 ficheros de capa** (réplica
   del diff de la heladería, `cbdcccd6`) y **F2 + F3 ≈ 2,1 M** (§8): con la F1 (~0,8 M), ≈ 2,9 M ≤ 5 M; reloj 3,5-4,5 h.

## 1. Dry-run de control (VPS, 25-oct): los dos caminos que se combinan, en verde hoy

| Comando (en `/root/wt-finca/scripts/productos-digitales/…`, `PY=/root/venv-guias/bin/python`) | Resultado |
|---|---|
| `parrillero-2_2/`: `CLAUDE_SCRATCHPAD=/root/tmp-finca-f1/par bash ciclo.sh` (semilla FT → `main.py --dry-run --origen --solo a`) | **exit 0 en 22 s** · idempotencia 0 · inject_cache 722 fórmulas (656 con caché) + 12 · data_only 667 con valor, 66 «""», 0 fallos · blancos 0 · **§9 13/13** · checklist C2 83 ítems · censo `--fail` 0 · moldes **30/30** · 16/16 protegidas · **TODO VERDE** |
| `$PY cifras_par_es.py --xlsx …/plan-financiero-parrillero-asador-eventos.xlsx` | 84 tokens · **D15 VERDE** (DSCR 1,51 · holguras 12,6/11,9 % · BE eventos caja 92/97) · `cifras_caso_es.json` idéntico al de `main` |
| `plan-heladeria/`: `CLAUDE_SCRATCHPAD=/root/tmp-finca-f1/hel bash ciclo.sh` (semilla panadería → motor) | **exit 0 en 20 s** · idempotencia 0 · 736 fórmulas (677 con caché) + 12 · 688 con valor, 59 «""», 0 fallos · blancos 0 · **13/13** · checklist 80 ítems · censo 0 · **30/30** · **TODO VERDE** (las aserciones de `semilla_hel.py` sobre la panadería LIVE siguen valiendo) |
| `$PY cifras_hel_es.py --xlsx …/plan-financiero-heladeria.xlsx` | 122 tokens · **D9 VERDE** · json idéntico |
| `$PY parrillero-2_2/calculadora_par_es.py --salida /root/tmp-finca-f1/calc` | 168 fórmulas, 0 fallos pycel · **autotest 552 comprobaciones VERDE** · 3 ejemplos (boda 42 €/inv., empresa 30,50, feria 10) |
| `$PY plan-heladeria/docx_hel_es.py --salida /root/tmp-finca-f1/docx` + `barrido_es.py` | 131 párrafos · 10 H1 · 7.061 palabras · **VERDE** · texto idéntico al LIVE (solo cambia la fecha de docProps) · barrido 0 |

**Medido en los orígenes** (`medir_finca_f1.py`, script del scratchpad por stdin): panadería 2.2 → `Personal` 6 filas (5-10:
maestro, oficial, ayudante, dependienta, extra de fin de semana, suplencias), `PyG` 2 líneas de venta (filas 10-11), `Inversión
Inicial` A26 «Fianza del alquiler», A27 «Alquiler de los meses previos a la apertura», A28 «Imprevistos de obra y acondicionamiento»;
FT 2.2 → `Personal` 4 filas. Contrato del parrillero (LIVE): 116 párrafos (74 `Normal` + 42 `List Bullet`), 1 tabla, 2.118
palabras, A4, autor AI Chef Pro, sin Heading. Calculadora del parrillero: `Calculadora` 108 filas/60 fórmulas/9 DV · `Ejemplos`
62/108 · `Instrucciones` 29. Supuestos de la heladería: `mes_paga_1`/`mes_paga_2` en B60/B61 (motor, genérico).
**Lo que la panadería deja y el módulo no reescribe** (heladería F1 §1, lo pisa la semilla; sigue igual hoy): `Inversión!A1/A2`
(«— España 2026»), partidas 7-25, `PyG!A2`, fijos 26-35, `PyG!H4:H11` (línea partida del pan), `PyG!G13` (FÓRMULA del IVA de compra
con el peso del pan: si la finca no la pisa con su valor, queda colgando de la H vaciada), `Punto Equilibrio!A2`, los valores verdes
de `0. Supuestos` (grupo_a conserva lo verde), checklist entero e `Instrucciones!A3` con el pid, docProps `description`/`keywords`.

## 2. Molde de contenido: `a.py` del parrillero + injertos de la heladería

| | Parrillero 2.2 (elegido para el contenido) | Paellero 2.2 | Catering 2.2 | Heladería 1.0 (injertos y semilla) |
|---|---|---|---|---|
| Driver | invitados/evento × €/invitado × eventos/año | igual | igual | clientes/día × ticket × días |
| Alquiler | «cuota de la cocina de apoyo» (VOCABULARIO) | igual | «cocina central» | **renta real del local** |
| Inversión / plantilla | furgoneta como «obra», 14 filas, 4 personas | igual | igual | **obra real, 19 filas, 6 personas** |
| Temporada | Mes 1 = enero | igual | igual | **Mes 1 girado + `mes_paga_1/2`** |
| Contrato y calculadora | **sí, revisados** (103.l, tramos, fuerza mayor, fuero) | sí | 1.x | no |

**Cómo se monta**: copiar `contenido_plan_negocio_parrillero_asador_eventos/` → `contenido_plan_negocio_finca_eventos_bodas/` y
reescribir TODOS los textos (sexto campo = fuente `research §n` / `BOE` / `calibrado D9`); de la heladería se copian las claves y las
entradas de `VOCABULARIO` que se citan abajo.

| Clave | Decisión (las cifras son huecos del research, con la restricción del motor) |
|---|---|
| `CONCEPTO` | `'Finca de Eventos y Bodas'` (sin tildes que restaurar; «iluminación», «climatización», «decoración», «cristalería», «cubertería», «evacuación» ya están en `motor.py:1596-1605`) |
| `VOCABULARIO` | **del parrillero se quedan**: cubierto(s)/comensal(es) → invitado(s), «días de apertura (al año)» → «eventos (al año)», «horas de servicio al día» → «horas de trabajo por evento», «ticket (medio)» → «precio (medio) por invitado», «en cada franja» → «en cada evento», la frase M1 del Word (`grupo_a.py:3766`), refrescos/«bollería»/«pan común»/superreducido. **Se cambian**: «alquiler mensual del local» → «renta mensual de la finca», «alquiler de los meses previos a la apertura» → «renta de la finca durante la obra», «fianza del alquiler» → «fianza del arrendamiento», «el/del/tu local» → «la/de la/tu finca», «un local que acaba de abrir» → «una finca que acaba de abrir», «en barra y sala» → «en el banquete y la barra», «en sala» → «en el banquete», «delivery» → «venta sin servicio». **Fuera**: todo lo de cocina de apoyo, furgoneta y «obra → furgoneta». **De la heladería**: las 3 notas de Tesorería (Mes 1 y temporada; trimestres del plan frente a los del 303; personal repartido en 12 meses frente a fijos discontinuos de temporada). Femenino «la finca»: medir concordancias en el primer dry-run (grep de «la finca nuev», «la finca que acaba de abrir»…) |
| `SUPUESTOS` driver | `cubiertos_dia` = invitados/evento (media de la mezcla) · `ticket_medio` = €/invitado SIN IVA (menú cerrado con la finca incluida + barra) · `dias_apertura` = eventos/año (bodas + empresa + celebraciones). Research: la mezcla por tipo (eventos × invitados × €) y el **techo de fechas** (sábados y vísperas de temporada: va a Instrucciones, el motor no lo comprueba) |
| `LINEAS_INGRESO` | **2 líneas** (`mix_en_supuestos`, probado en heladería y parrillero): «Ventas de banquete con la finca incluida (cóctel, menú cerrado y resopón)» `comida` · «Ventas de barra libre y bebida del banquete» `bebida`. Todo al **10 %** (servicio de restauración con el espacio como accesorio: el research confirma el criterio de la DGT). **3.ª línea «alquiler del espacio sin banquete» al 21 % solo si el research la pone ≥ 10 % de la venta**: sexto campo `0.21` (`grupo_a.py:2317-2323`, celda G verde; sin usar aún en LIVE) y `coste_comida` ponderado (§2, palanca 2) |
| `IVA_COMPRAS` | **número, obligatorio con este origen** (la semilla pisa `PyG!G13`, como la heladería): mezcla 4 %/10 % de la compra de banquete (research) |
| `pct_bebida_alc` · `iva_bebida` | alcohol de la barra libre (alto) · 10 % (consumo en el acto, art. 91.Uno.2.2.º LIVA) |
| `pct_delivery` · `comision_delivery` | **0** (la finca no vende sin servicio, como 5 hermanos de local fijo) · **> 0** (la demo §2.11.9 lo fuerza al 25 % y exige que el RAI baje: `grupo_a.py:4867`) |
| `pct_varios` | imprevistos + comisiones de wedding planners y portales por reserva (research). No hay línea de coste variable para extras de ETT: van en la plantilla |
| `alquiler_mes` · `fianza_meses` · `meses_renta_previa` | renta de la finca · fianza · meses de obra pagando renta (research). La renta entra en fijos al 21 % de IVA soportado SIEMPRE (`grupo_a.py:2507-2512`, fórmula fija): §9 |
| `vida_obra` · `vida_maquinaria` · `pct_imprevistos` | obra en finca ajena: el **menor** de vida útil y duración del arrendamiento con prórrogas (research con la norma contable) · equipo · % sobre la obra |
| `mes_paga_1` · `mes_paga_2` · `rampa_mes1` · `meses_rampa` | Mes 1 = apertura de temporada (research: marzo o abril) → pagas en su mes del plan; rampa larga: la primera temporada se reserva con 9-18 meses de antelación |
| `dias_cobro` · `dias_pago` | **0** para particulares (pagan antes del evento; el libro no admite negativos: las señales no se modelan, «tu caja real será mejor») ponderado con empresa a 30 días · proveedores |
| `PLANTILLA` | **6 filas exactas** (molde panadería): titular-gerente y comercial de bodas · jefe/a de cocina · maître y coordinación del día · cocina de banquete (fijos discontinuos) · sala y barra (fijos discontinuos + ETT, en jornada equivalente) · mantenimiento, jardines y limpieza. Sin «freelance»; bruto ≥ SMI en proporción |
| `COBERTURA` | 4 claves: `horas_dia` (h por evento: montaje-servicio-recogida) × `personas_franja` (sala+cocina+barra a la vez) × eventos + `horas_produccion`/`personas_produccion` (mise en place de la víspera). Gate ≥ 98 % |
| `AMORTIZABLE` | `obra`: proyecto, obra, salón, cocina (obra), aseos, accesibilidad, instalación eléctrica, iluminación exterior, grupo electrógeno, PCI, climatización, jardines, caminos, aparcamiento · `maquinaria`: carpa/pérgola, equipo de cocina, cámaras, mobiliario, vajilla, cristalería, cubertería, barras, sonido, limitador, TPV · `no`: constitución, licencia, tasas, registro, APPCC, marca, web, ferias, lanzamiento, stock, fianza |
| `FIJOS` + `FIJOS_EXTRA = ()` | patrón parrillero/heladería: la semilla escribe rótulo e importe en 26-35 y `FIJOS` pone la nota por rótulo normalizado. **10 exactas**: gestoría (con llamamientos) · mantenimiento de jardines · mantenimiento de instalaciones (frío, climatización, PCI, grupo) · marketing y portales de bodas · software de reservas y CRM · limpieza y lavandería de mantelería · seguridad y vigilancia · residuos y aceite · DDD y autocontrol · SGAE/AGEDI (o PRL: el research elige) |
| `UMBRALES` · `ESCENARIOS` · `ESTACIONALIDAD` | research; `r_alquiler` con rótulo «Renta de la finca / Ventas»; 12 pesos con `assert` de suma 1,000, girados al Mes 1 |
| `INSTRUCCIONES` | `uso` 6-8 de la heladería (8 = «el Word, la calculadora y el contrato usan las cifras de este Excel») · `referencias` con fuente del research + **techo de fechas** + **tabla de personal por servicio** (la misma de la calculadora) |
| `CHECKLIST` / `RECALIBRADO` | `{}` (lo escribe la semilla) / **`()`** (producto nuevo, sin «qué ha cambiado»; `grupo_a.py:4255`) |

**Palancas que pide la finca y no existen** (sin tocar `motor.py` ni `grupo_a.py`):
1. *Renta fija de la finca*: **existe** (`alquiler_mes` + fila «Alquiler del local» × 12 + `fianza_meses` + `meses_renta_previa` +
   umbral `r_alquiler` + demo §2.11.9 `alquiler_sup`). Solo VOCABULARIO.
2. *Alquiler de espacio al 21 % frente a banquete al 10 %*: el **IVA por línea existe** (sexto campo); el **coste por línea NO**: la
   mercancía va por grupo (`cv_comida = pct_comida × coste_comida`, `grupo_a.py:2419-2426`). Si entra la 3.ª línea como `comida`,
   `coste_comida` = coste del banquete × peso del banquete / (banquete + espacio), con la nota a la vista. Por defecto, 2 líneas.
3. *Canon de catering concesionado* (finca de solo alquiler): **no se modela**. Cambia todo el P&L (sin mercancía, sin cocina, sin
   APPCC propio) y contradice «packs de menú cerrado». Va en el Word §2 y §10 como alternativa razonada, sin Excel (patrón D7 de la heladería).
4. *IVA de la renta exenta* (finca rústica sin edificar): **no hay palanca** (G de la renta = `iva_soportado`). El caso modela una finca
   con edificaciones arrendada a una SL (sujeta al 21 %, research) y la nota lo dice.
5. *Señales 9-18 meses antes y su IVA* (devengo al cobro, LIVA art. 75.Dos): **no se modelan** (`dias_cobro` ≥ 0). Nota en Tesorería y Word.
6. *Personal extra por evento (ETT)*: **no hay coste variable de personal**; va en las filas 4-5 de la plantilla en jornada equivalente,
   y la calculadora lo calcula evento a evento.

## 3. Carpeta `scripts/productos-digitales/plan-finca-eventos/` (copias con PID y rutas)

| Fichero | Origen | Cambios |
|---|---|---|
| `semilla_fin.py` | `plan-heladeria/semilla_hel.py` | **mismo origen** (`dl/plan-negocio-panaderia/`, mismas aserciones: A26-A28, `PyG!A13`, `G13` fórmula, `H4` «pan», `Instrucciones!A3` panadería); `TITULOS_PLAN` de la finca; **19 partidas** en 7-25 (assert de suma con el research); **10 fijos** en 26-35; `G13` ← `IVA_COMPRAS['comida']`; vaciar `H4:H11`; `_supuestos` con el módulo nuevo; docProps |
| `datos_checklist.py` | el de la heladería (formato) | ~84 tareas nuevas (§4); tareas legales comunes de la línea de eventos desde `parrillero-2_2/datos_checklist.py` |
| `fin_version.py` + `main_fin.py` | `hel_version.py` + `main_hel.py` | `VERSION = '1.0'`, `MES = 'noviembre 2026'` |
| `ciclo.sh` | el de la heladería | `SCR=/root/tmp-fin-f2/motor`, `semilla_fin.py`, `main_fin.py --producto plan-negocio-finca-eventos-bodas` |
| `cifras_fin_es.py` | `cifras_hel_es.py` (gates D9) + `MAPA` de eventos de `cifras_par_es.py` | rótulos tras VOCABULARIO: `^invitados por evento \(media`, `^precio medio por invitado sin iva`, `^eventos al a[ñn]o$`, `^renta mensual de la finca`, `^invitados necesarios por evento` (+ caja) y **`BE_EVENTOS*` derivados** (ingresos de equilibrio / evento medio, años 1-3), partidas de inversión de la finca, `^cobertura \(contratadas`, `^horas de producci`; gates: DSCR ≥ 1,25 · saldo mínimo > 0 · cobertura ≥ 98 % · holgura caja A1 ≥ 15 % (A2/A3 informativas) · exceso 0-5 % · neto ≤ techo del research |
| `calculadora_fin_es.py` | fork de `parrillero-2_2/calculadora_par_es.py` (844 l.) | §4; importa `fin_version` |
| `contrato_fin_es.py` | **nuevo, ~130 l.** | copia el docx del contrato del parrillero como molde físico (estilos `Normal` + `List Bullet`, A4), vacía el cuerpo y escribe `textos/contrato_es.json` (`[{estilo, texto}]`); docProps AI Chef Pro 2026; gates A4, 0 tokens, barrido, no latinos |
| `tandas_docx.py` · `docx_fin_es.py` · `BRIEF-REDACTORES.md` | los de la heladería | `docx_fin_es.py` = `docx_hel_es.py` (sin anexo); `GEMELA` = `plan-heladeria/textos/hel_es_{a,b}.json` (formato ES 1.0 sin «versión anterior») y, para lo de eventos, `parrillero-2_2/textos/par_es_{a,b}.json` |
| `barrido_es.py` | el de la heladería | `PROHIBIDOS` sin `generador` ni `aparcamiento` (legítimos en una finca: grupo electrógeno y aparcamiento de invitados); `+` restos heladería (`helad\|mantec\|cubeta\|vitrina\|obrador\|cucurucho\|tarrina`) y parrillero/catering (`cocina de apoyo\|furgoneta\|remolque\|parrill\|\bbrasa\|carb[oó]n\|asado para llevar\|cocina central\|drop-off`); se quedan los de la panadería (`\bpan\b` incluido: los redactores escriben «panes» o lo evitan) |
| `gate_restos_ft.py` | **reusar** `catering-es-2_0/` | `<carpeta> --rx-extra '<restos panadería, heladería, parrillero>\|plan-negocio-panaderia\|plan-negocio-heladeria\|plan-negocio-parrillero'`, antes de meter la guía de equivalencias (Letter) |

## 4. Word, checklist, calculadora, contrato y entregables

**Word** `plan-de-negocio-finca-eventos-bodas.docx`: molde físico = docx del FT ES (131 párrafos, 10 H1, 61 ranuras; mapa
`business-plans-en-4/docx_es_cat.json`), igual que paellero, parrillero y heladería: `FIJOS`, `ENCABEZADOS` e `INDICE` sin remapear.
**Sin anexo** por comunidades (proporcionalidad): §9 da el marco estatal y una lista de «qué preguntar en tu ayuntamiento y en tu
comunidad». Gate 10 H1, A4, ≥ 6.000 palabras, 0 tokens, 0 no latinos, 0 prohibidos; `comments` = `aichef.pro/plan-negocio-finca-eventos-bodas`.
Venta cruzada (127-129): → Kit de Tareas Recurrentes: Catering · → Kit de Escandallos Pro · → Pack Plantillas APPCC.
**2 Sonnet en paralelo**: `fin_es_a` §1-5 (29 ranuras, ~2.950 palabras) · `fin_es_b` §6-10 (32, ~3.770). Pistas por sección desde el
research: modelos de finca (solo alquiler / catering concesionado / banquete propio: el plan es el tercero), cliente y mezcla, mercado
de bodas (INE y SERP), competencia por tipo, captación con 9-18 meses de antelación (portales, ferias de novios, planners), operación de
un sábado tipo y personal por servicio, plantilla fija + bolsa, finanzas en eventos/año, legal (suelo rústico, actividad, ruido,
aforo, sanidad, contrato) y 90 días. Tokens: ~70 (`INVITADOS_EVENTO`, `PRECIO_INVITADO(_IVA)`, `EVENTOS_ANO`, `VENTAS_A1-3`, `NETO_A1-3`,
`RENTA_MES`, `INVERSION_TOTAL`, `CAPEX`, `PRESTAMO`, `DSCR_MIN`, `SALDO_MINIMO`, `MES_SALDO_MINIMO_NOMBRE`, `BE_EVENTOS(_CAJA)`,
`HOLGURA_CAJA(_A2/_A3)`, `PAYBACK`, `COBERTURA_HORAS`, `PLANTILLA_PERSONAS`, `ESC_*`…). Prohibidos del brief: los de §3 + «España
2026» como sello, «validad», «freelance», «carné de manipulador» (salvo «ya no existe»), «tarifa plana» con cifra, «CNAE» como trámite.

**Checklist** `checklist-apertura-finca-eventos-bodas.xlsx`: de `datos_checklist.py`, molde C2 de la panadería (cabecera `OK ·
TRÁMITE · RESPONSABLE · PLAZO · NOTAS`, pie «Tareas completadas:»). **~84 tareas**: `F1 - Constitución` (12) · `F2 - Finca y licencia`
(16: arrendamiento, urbanismo, actividad, aforo, ruido) · `F3 - Obra, cocina y sanidad` (15) · `F4 - Personal y APPCC` (13) · `F5 - Marca
y reservas` (14) · `F6 - Temporada y eventos` (14). Pestañas ≤ 31. **A verificar por el research con fuente primaria**: uso en suelo
rústico (autonómico: calificación o declaración de interés público/social), licencia de actividad y ley autonómica de espectáculos
públicos y actividades recreativas (salón de celebraciones), aforo, evacuación y autoprotección (RD 393/2007 y norma autonómica), ruido
(Ley 37/2003, limitador y ordenanza), horario de cierre, accesibilidad, epígrafes de IAE, registro sanitario autonómico (RGSEAA solo si
sirve a otros negocios), comida testigo (RD 1086/2020 art. 30), alérgenos (RD 126/2015), IVA del banquete con espacio y de las señales,
arrendamiento (LAU uso distinto de vivienda, IVA y retención), fijos discontinuos (ET art. 16), ceremonia civil fuera del juzgado
(Ley 15/2015) y alcohol a menores (autonómico).

**Calculadora** `calculadora-presupuesto-boda-evento-finca.xlsx` (fork del parrillero, firma calc-beta `Calculadora · Ejemplos ·
Instrucciones`): canal Particular / Empresa (desplegable) · fecha → temporada (alta/media/baja) y día (sábado / viernes-domingo /
entre semana) con su suplemento o descuento en una tabla VISIBLE · **mínimo de invitados** por temporada · invitados · **pack de
menú cerrado** (3, del research) → materia prima por invitado · barra libre en horas · resopón y extras · **personal por servicio**
por la tabla del research (camareros, cocineros, maître, barra, coordinación) a €/h × (1 + SS) · alquiler sin banquete en línea
aparte **al 21 %** (aquí sí: la calculadora no es el motor) · IVA desglosado 10/21 · señal y calendario de pagos · cancelación por
tramos en MESES sin huecos (research) · margen calculado. 3 ejemplos por las mismas fórmulas (boda de sábado en temporada alta, boda
de viernes en temporada media, evento de empresa entre semana); autotest pycel ± 0,01 €.

**Contrato** `modelo-contrato-reserva-finca-eventos.docx` (~2.000 palabras; gemela = contrato del parrillero, ya revisado): reserva de
fecha y señal (arras: el research dice cuáles), mínimo de invitados y recuento final, prueba de menú, catering en exclusiva y
proveedores externos, horario y ruido, aforo, montaje y daños, plan B por lluvia (no es fuerza mayor) y fuerza mayor, no desistimiento
(TRLGDCU art. 103.l), tramos de cancelación proporcionados, factura de cada cobro, fuero del consumidor (art. 90.2), alérgenos, datos e
imagen; anexo de condiciones para empresas. **Es lo primero que se recorta** si la F2 pasa de 2,5 h.

**Entregables** en `astro-site/public/dl/plan-negocio-finca-eventos-bodas/` (claves = las de los hermanos de eventos):
`plan-financiero-finca-eventos-bodas.xlsx` (`plan-financiero`) · `plan-de-negocio-finca-eventos-bodas.docx` (`plan-negocio`) ·
`checklist-apertura-finca-eventos-bodas.xlsx` (`checklist-apertura`) · `calculadora-presupuesto-boda-evento-finca.xlsx`
(`calculadora-pricing`) · `modelo-contrato-reserva-finca-eventos.docx` (`modelos-contrato`) ·
`guia-equivalencias-plan-negocio-finca-eventos-bodas.docx` (`guia-equivalencias`).

## 5. Capa de producto (slug nuevo): crear (C), copiar (P(h) heladería, la de un producto NUEVO · P(p) parrillero, lo de eventos) o editar (E)

Patrón exacto de cada E: `git show cbdcccd6 -- <fichero>` (PR #161, la heladería). Slug, env y nombres comprobados con `git grep`: 0 choques.

| Fichero | Acción | Gate |
|---|---|---|
| `astro-site/src/data/productos/planes/plan-negocio-finca-eventos-bodas.ts` | P(h) (265 l.): sin testimonios, rating ni tachado (producto nuevo); SEO sin «España 2026»; FAQ con «¿Sirve en México…?» y las del research (señal, mínimo de invitados, licencia en suelo rústico); BONUS guía (`es-guia-equivalencias.jpg`, 15 €); **`stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_FINCA_EVENTOS'`**; `schema.price` 45; `updateNote` «Producto nuevo · Versión 1.0 · noviembre 2026»; `footerLinks` → catering temático, coctelería de eventos, Kit Tareas Catering; cifras medidas, nada movible (DSCR, payback, saldos) | `sync-product-prices.py --check`, `gate-no-latinos` |
| `astro-site/src/pages/plan-negocio-finca-eventos-bodas{,-access,-library}.astro` | P(h) (32/17/18 l.); `locales=['es']` (sin gemelo EN todavía) | `gate-flujo-postpago` D/E-f (3 puertas cripto: `PlanNegocioLandingPage.astro`) |
| `astro-site/src/islands/library/PlanNegocioFincaEventosBodasLibraryIsland.tsx` | P(h) (16 l.) | ídem |
| `src/pages/PlanNegocioFincaEventosBodasDashboard.tsx` · `…AccessGate.tsx` | P(h) (135/13 l.) + 2 tarjetas P(p) (`calculadora-pricing`, `modelos-contrato`, `PlanNegocioParrilleroAsadorEventosDashboard.tsx:29-70`) = 6 tarjetas, guía con Globe | `gate-flujo-postpago` C |
| `astro-site/src/lib/zona-app.ts:81` | E (+1 entrada; nombre corto del diálogo cripto) | A |
| `netlify/functions/get-download-urls.ts:1235` | E (`PRODUCT_FILES`, 6 claves) | B (disco, git, 200 binario) |
| `netlify/functions/verify-purchase.ts:628` · `resend-access.ts:577` · `admin-generate-access.ts:81` | E (`emailBody` con lo MEDIDO: Word de 10 secciones, Excel de 9 hojas, checklist de N tareas, calculadora, contrato, guía) | A |
| `netlify/shared/product-prices.ts:74` (regenerar con `sync-product-prices.py`) · `payment-links.ts:73` (tras el link, `sync-payment-links.py`) | E | D y E |
| Netlify env `VITE_STRIPE_PAYMENT_LINK_PLAN_FINCA_EVENTOS` (builds) | John crea el link; Claude: env + redeploy | D |
| `src/data/products-catalog.ts:499` · `productos-changelog.ts:1972` (`'1.0'`, sin «qué ha cambiado») · `productos-digitales-config.ts:594` (6 ficheros) · `src/pages/AdminGenerateAccess.tsx:75` | E | `sync --check` |
| Hubs: ES `ProductosDigitalesHubPage.astro` (posición 1 con «✨ Nuevo», l. 68; **quitar la tarjeta de `comingSoon` l. 1051**; la Pastelería, 5.ª novedad, pierde el ✨) · EN `DigitalProductsHubPage.astro` (junto a la heladería, l. 606; `comingSoon` l. 1013) · DE 63/906 · FR 64/907 · IT 64/907 · NL 61/904 · PT 63/906 (las 6 tarjetas de «Próximos» ya traducidas, `PartyPopper`) · SPA `src/pages/ProductosDigitales.tsx:52` / `comingSoon` :1034 | E | `hub-gate.py`, `tienda-gate.py` |
| `astro-site/src/lib/sinonimos-buscador.json` (mapa por slug, como l. 227) | E: «finca fincas bodas boda salon de banquetes quinta hacienda jardin de eventos salon de eventos celebraciones convite venue» (el grupo de sinónimos finca/bodas/banquetes ya existe, l. 74-80) | buscador del hub |
| `astro-site/public/llms-full.txt:138` · `astro-site/src/lib/sitemap-lastmod.json:688` | E (+1 línea cada uno, fecha del LIVE) | sitemap en el `dist` + reenvío GSC |
| `astro-site/src/data/productos/tareas/kit-tareas-catering.ts:385` · `planes/plan-catering-tematico-eventos.ts:317` · `planes/plan-negocio-cocteleria-eventos.ts` (`footerLinks`) | E (+1 enlace al plan: nada huérfano) | revisión |
| `scripts/productos-digitales/equivalencias-es/censo-terminos-es.py:190-191` · `build_guia_es.py:3,596-597` | E: **52 → 53** + `datos/integracion.json` (ejemplos de la FAQ) + `terminos.json` solo para términos que cambien en ≥ 5 de 21 países con fuente (candidatos: finca de eventos, señal, barra libre, resopón; tope 0,05 M; si no, ejemplos en la FAQ, como la heladería) | `build_guia_es.py --check --only plan-negocio-finca-eventos-bodas` |
| Imágenes `astro-site/public/lovable-uploads/ai-gallery/plan-finca-{hero,plan,banquete,ceremonia,cocina,barra,montaje}.jpg` | C (skill `generate-images`): hero = og, hub y CTA; `cocina` = whyBg; `banquete` = buyBoxBg; 6 en galería; distintas de las de catering, paellero y parrillero | `gate-flujo-postpago` D (200) |
| `scripts/productos-digitales/emails/broadcast-plan-negocio-finca-eventos-bodas-lanzamiento-es.html` | C desde el de la heladería; «Hola, colegas», negro/dorado, sin cifras movibles | `resend-broadcast.py --test` |
| `PAYMENT_LINKS_PENDIENTES_JOHN.md` · `CALENDARIO-V2-SEMANAL.md` (l. 549 «Q1 2027» → LIVE; cola de correos) · `tienda-gate.py:84` (`PLANES_ES`, tras el LIVE) · handoff · `plan-finca-eventos/NOTA-CARRIL-CURSOR.md` | E / C | — |

**No se tocan**: `robots.txt` (`/plan-*-access` y `-library` ya bloqueados, l. 54-55…), `tienda.ts` y `alternatesFamilia` (hasta que nazca
«Wedding Venue Business Plan» EN, que se DUPLICARÁ de este), `src/App.tsx` y la SPA de landing (no se construyen), `og-meta.ts`
(muerta), `types.ts` (solo un comentario), `main.py` `PRODUCTOS`, y el blog (carril Cursor: banners en
`gestion-de-eventos-gastronomicos-con-ia.md` y `libreria-de-prompts-para-catering-ai.md`, va en la nota).

## 6. Gates

**F2 (VPS)**: `ciclo.sh` → `main.py` exit 0 (idempotencia 0, caché, blancos 0, §9 13/13, censo `--fail`, demos 30/30) ·
`cifras_fin_es.py` D9 VERDE · `calculadora_fin_es.py` autotest VERDE · `docx_fin_es.py` (10 H1, A4, ≥ 6.000, 0 tokens) ·
`tandas_docx.py check` ×2 · `contrato_fin_es.py` (A4, autor, 0 tokens) · `barrido_es.py` 0 en los 5 · `gate_restos_ft.py --rx-extra` 0 ·
`gate-no-latinos.py --only` · `censo-entregables.py --only plan-negocio-finca-eventos-bodas --fail` · `paginas-gate.py` · Mac = VPS
(sha256) · **una** revisión Opus final (cifras · legal · editorial). **F3**: `sync-product-prices.py --check` · `build_guia_es.py
--check --only` · `gate-flujo-postpago.py --base <preview> --crypto-products all --crypto-exclude pro-prompts-ebook --only
plan-negocio-finca-eventos-bodas`, después LIVE (A-E-f) · `scripts/astro-migration/{miselup,whatsapp,robots,hub}-gate.py` ·
`tienda-gate.py --base https://aichef.pro` · `fase6-gate.py https://aichef.pro` (URL BASE) · curl al checkout cripto (`qa-finca@aichef.pro`,
purgar) · sitemap reenviado. Antes de fiarse de un gate LIVE: `git pull` (leen el registro local).

## 7. Plan F2 y F3

**F2 — Entregables** (rama `feat/plan-negocio-finca-eventos`; worktree de la rama en el VPS, nunca `main`)
1. Mac · leer `F1-research-finca.md` y firmar SPEC corta (≤ 80 líneas): caso y mezcla, 19 partidas, 10 fijos, 6 filas, cobertura,
   Mes 1 y estacionalidad, packs y tabla de personal, tramos de cancelación, prohibidos. Commit F1.
2. Mac · **un** implementador opus: `a.py`, `semilla_fin.py`, `datos_checklist.py`, `fin_version.py`, `main_fin.py`, `ciclo.sh`,
   `cifras_fin_es.py`, `barrido_es.py`. **En paralelo, un sonnet**: `calculadora_fin_es.py` (fork) y `contrato_fin_es.py` (generador).
3. VPS · `bash ciclo.sh` + `cifras_fin_es.py` en bucle hasta D9 verde (máx. 3 vueltas de calibración; se para y se reporta si no
   cuadra); demo §2.11.5 con el fijo de ±100 € si hace falta; `calculadora_fin_es.py` autotest. scp de los xlsx y `cifras_caso_es.json`.
4. Mac · `tandas_docx.py preparar` → **3 Sonnet en paralelo** (`fin_es_a`, `fin_es_b`, `contrato_es`; `istats` < 60 °C) → `check`.
5. VPS · `docx_fin_es.py` + `contrato_fin_es.py` + gates; copia a `public/dl/plan-negocio-finca-eventos-bodas/` en el worktree.
6. Mac · **una** revisión Opus de los 5 ficheros + una ronda de arreglos; VPS regenera. `F2-NOTAS.md`. Commit + push (`Via: Claude Code`).
**F3 — Producto y lanzamiento**
7. Mac · Sonnet A: ficha + 3 páginas + isla + dashboard + access gate (FAQ, SEO). Sonnet B: functions ×4, `zona-app`, configs, catálogo,
   changelog, hubs ×8 (con su `comingSoon`), buscador, `llms-full`, `sitemap-lastmod`, `footerLinks` ×3. Los dos con el diff de `cbdcccd6`.
8. Mac · 7 imágenes con `generate-images`. VPS · censo de términos (52 → 53) + `build_guia_es.py --only` + `--check`; FAQ de países.
9. Mac · `sync-product-prices.py`; PR draft → preview de Netlify; gates contra el preview.
10. **John · Payment Link** (45 EUR, *exclusive*, impuesto automático, factura, descripción en prosa sin viñetas, éxito →
    `/plan-negocio-finca-eventos-bodas-access?session_id={CHECKOUT_SESSION_ID}`). Claude: `stripe get` del link, env, `sync-payment-links.py`,
    redeploy; merge (aprueba John); gates LIVE; sitemap.
11. Correo: hueco ES **3-dic 08:00Z** (CALENDARIO l. 744); > 30 días hoy → borrador por curl + prueba a John + routine que lo programe el
    3-nov o después; CALENDARIO y handoff. Nota al carril Cursor. Commit + push.

## 8. Presupuesto F2 + F3

| Pieza | Quién / dónde | Tokens |
|---|---|---|
| `a.py` + semilla + checklist (~84) + versión/ciclo + cifras + calibración D9 | opus · VPS | 0,50 M |
| Calculadora (fork: packs, temporada, mínimo, personal por servicio, IVA 10/21) + generador del contrato | sonnet · VPS | 0,17 M |
| Word: pistas + 2 tandas Sonnet ‖ + ensamblado + barrido | sonnet × 2 + orquestador | 0,30 M |
| Texto del contrato | sonnet | 0,08 M |
| Revisión opus final + arreglos | opus | 0,30 M |
| Capa de producto (≈ 50 ficheros, 7 nuevos de copia) | sonnet × 2 · Mac | 0,40 M |
| Imágenes (7) · guía de equivalencias · correo | API / sonnet / orquestador | 0,18 M |
| PR, preview, gates LIVE, merge | orquestador | 0,15 M |
| **Total F2 + F3** | | **≈ 2,1 M** (heladería: 1,75 M est. y 2,2 M real con F1; 6 entregables frente a 4) → con F1, **≈ 2,9 M ≤ 5 M** |

Reloj: F2 ≈ 2-2,5 h (cada ciclo del motor tarda 20-22 s; redactores en paralelo ~20 min; revisión ~30 min), F3 ≈ 1,5-2 h más la
espera del link. Lo dispararía: una 3.ª línea al 21 % sin necesidad, un anexo por comunidades, verificar cita a cita lo que el
producto no afirma, más de una ronda de revisión o modelar el canon de catering en el Excel. Si la F2 pasa de 2,5 h, se cae el contrato.

## 9. Riesgos

- **Restos de tres moldes**: panadería (origen: `PyG!H4:H11`, `G13`, `Inversión!A2` «España 2026», fijos, checklist, docProps), parrillero
  (`a.py` clonado: cocina de apoyo, furgoneta, brasa, asado para llevar) y heladería (semilla clonada). Los pisan la semilla y el
  VOCABULARIO; `barrido_es.py` y `gate_restos_ft.py` con el regex de §3 lo demuestran a 0. **Sin código común.**
- **Demo §2.11.5** (tres ramas del IS, `grupo_a.py:5312-5352`): una finca tiene mucho fijo (renta, plantilla de todo el año) y la ventana
  de RAI puede ser estrecha, como en el parrillero (128 €): se encaja con un fijo ±100 € mirando los `ensayos` de `inf.json`.
- **Temporada y Tesorería de 12 meses**: con el Mes 1 en primavera, el saldo mínimo cae en invierno (renta sin bodas) y la primera
  temporada sale corta porque se reserva con 9-18 meses; las señales no se modelan (caja real mejor) y el personal va repartido en 12
  meses (invierno más caro, verano más barato): las tres notas de la heladería por VOCABULARIO; se calibra con fondo, rampa y préstamo.
- **IVA**: renta al 21 % fijo en el motor (si la finca fuese rústica sin edificar y exenta, el libro deduciría un IVA que no hay: el caso
  no lo es y la nota lo dice); banquete con espacio al 10 % según el criterio que confirme el research; 3.ª línea al 21 % sin probar en LIVE.
- **Concordancias del femenino** («la finca») en frases del motor escritas para «el local», y rótulos de importe sin «eventos»,
  «invitados», «personas», «plazas», «días» ni «meses» (`motor.RX_RECUENTO`): medir en el primer dry-run.
- **Personal por servicio**: el motor no tiene coste variable de personal; la plantilla en jornada equivalente tiene que cuadrar con la
  cobertura (≥ 98 %) y con la tabla de la calculadora: si no cuadran, gana la tabla y se ajusta la plantilla.
- **Legal autonómico** (suelo rústico, espectáculos públicos, ruido, horario, aforo): sin anexo; marco estatal + «compruébalo» en Word,
  checklist y FAQ. Lo que afirme el contrato pasa por la revisión final.
- **La guía de equivalencias nace en Letter** (como las 52): por eso `gate_restos_ft` va antes de meterla.
