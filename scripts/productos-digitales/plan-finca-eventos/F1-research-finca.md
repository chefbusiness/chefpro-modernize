# Plan de Negocio: Finca de Eventos y Bodas (ES, 45 €) · F1 research (DELTA de un espacio fijo sobre la línea de eventos)

> Sesión Claude Code, 25-oct-2026. Una pasada: 19 textos del BOE descargados y leídos hoy (API de datos abiertos +
> extracción de la última versión de cada artículo), INE (tabla 77171), DataForSEO (España, EE. UU., México, Argentina y Colombia)
> y unas 25 búsquedas. **Lo común de la línea de eventos NO se repite** (IVA 10 % del servicio con comida, RD 1021/2022, RD 1086/2020
> art. 30 temperaturas, ATP, fijo discontinuo, SS 33 %, convenio provincial, IAE 677.9 del catering, alérgenos) → `catering-es-2_0/F1-research-es.md` §1.
> Fuego, gas y época de peligro → `paellero-2_2/F1-research-paellero.md` §1. Etiquetas: ✅ = leído hoy en origen (BOE, INE) ·
> 🟡 = fuente secundaria o solo en el resumen del buscador · ✅ hermano = leído por otra F1 · [medido] = DataForSEO hoy ·
> [estimado] = criterio de kit, con el cálculo a la vista · ❌ = no encontrado o no verificado.

## 0. Los 7 hallazgos que mandan

1. **La licencia ES el negocio, y en suelo rústico es excepcional.** Celebrar bodas en una finca rústica no es un uso ordinario:
   necesita una autorización previa a la licencia municipal, distinta en cada comunidad, con plazos largos y silencio negativo
   (detalle en §1.a). **Madrid**: calificación urbanística y solo en **edificaciones existentes** (Ley 8/2012 art. 9 ✅).
   **Andalucía**: actuación extraordinaria con **prestación compensatoria del 10 %** de las obras (LISTA art. 22 ✅).
   **Cataluña**: solo en **masías catalogadas**, con uso de restauración (TRLU art. 47.3 bis ✅). **C. Valenciana**: declaración
   de interés comunitario con canon del 2 % (TRLOTUP arts. 216 y 221 ✅), o la excepción por reutilizar arquitectura tradicional
   (art. 219 ✅). Esto cambia el producto: el arrendamiento lleva **condición suspensiva de licencias**, **no se venden fechas sin
   licencia** y la inversión incluye proyecto, tasas y prestación compensatoria.
2. **El RD 393/2007 ya no se aplica desde el 11-oct-2026.** Lo sustituye la **Directriz Básica de Autoprotección** (Orden
   INT/1068/2026, BOE 10-10-2026 ✅). En espectáculos y actividades recreativas obliga a un plan de autoprotección a partir de
   **1.000 personas** en edificio cerrado o **en instalación desmontable o de temporada** (la carpa). Al aire libre, desde **5.000**
   en recinto delimitado y desde 20.000 sin delimitar (anexo I, E ✅). Antes el umbral de los cerrados era 2.000. Una finca de 300
   invitados queda fuera de la norma estatal, salvo que la comunidad sea más exigente o la Administración se lo pida por estar en
   un **entorno de riesgo**, como el forestal (apdo. 2 ✅). Los planes vigentes se adaptan en 4 años (2.6.3 ✅). **No se cita
   el 393 en ningún entregable.**
3. **IVA partido y nada de paquetes al 10 % sin pensar.** El banquete con servicio va al 10 % (LIVA art. 91.Uno.2.2.º, ✅ hermano).
   **El alquiler del espacio cobrado con precio propio va al 21 %**: la DGT (V2664-22, 🟡) trata el alquiler de reservados de un
   restaurante y el servicio de hostelería como prestaciones independientes. En el modelo recomendado **todo lo que factura la
   finca va al 21 %**: el espacio y los servicios a los novios, y el canon al catering. El menú lo factura el catering al 10 %.
   El motor 2.2 admite IVA por línea (A3 de `planes-v2-motor-2.2-SPEC.md`).
4. **Modelo recomendado: finca arrendada + catering exclusivo concesionado con canon.** No hace falta cocina de producción ni
   brigada propia, y la responsabilidad sanitaria del menú es del catering. Es el modelo viable para quien no es hostelero.
   - Caso: **120 eventos × 82 invitados × 37 € ≈ 364.000 €**, con 30 bodas, 35 eventos de empresa, 40 celebraciones privadas y
     15 eventos pequeños.
   - Resultado a régimen: EBITDA ≈ 21 %, **neto ≈ 10 %**, **DSCR ≈ 1,65** con préstamo a 8 años y holgura contable ≈ 14,5 %.
   - Inversión ≈ 242.000 € sobre edificaciones existentes. **La finca no se compra.**
   - Sin el canon («solo alquiler») las ventas bajan a ≈ 284.000 € y no llegan al equilibrio de caja. Con catering propio la
     venta se multiplica por 2-3, y la complejidad también: es el caso de los hosteleros, a los que se envía al plan de catering.
5. **Estacionalidad con dato del INE.** En 2024 hubo **175.364 matrimonios** (+1,7 %) y el 83,6 % fueron civiles (✅). De mayo a
   octubre se concentra el **63,7 %** de todos y el **75 % de los religiosos**. Los picos son **septiembre (13,1 %) y junio
   (12,8 %)**; enero se queda en el 3,8 %. Según Bodas.net, el **28 % de las parejas celebra en una finca** y la boda se prepara con
   **12-18 meses** de antelación (13 de media, 🟡). **La primera temporada se vende antes de abrir**, así que la rampa del motor es
   larga (0,45 → 1 en 12 meses).
6. **Lo que la finca impone por contrato a quien cocina y a quien se casa.**
   - Al catering: **comida testigo** en toda boda o encargo de más de 40 personas (RD 1086/2020 art. 30.8.d-e ✅): una ración de
     ≥ 100 g, a ≤ 4 °C o ≤ −18 °C, durante 7 días (art. 30.10 ✅). La guarda quien sirve, en el momento del servicio (art. 30.9 ✅).
     También alérgenos, inscripción sanitaria de la cocina que use, seguro de intoxicación, horarios y canon auditable.
   - A los novios: la señal y las penalizaciones tienen que ser **proporcionales** (TRLGDCU art. 85.6 ✅) y **recíprocas**. Es
     abusivo retener lo pagado si el cliente renuncia sin prever una indemnización equivalente si renuncia la finca (art. 87.2 ✅).
7. **Demanda.** En España la intención de montar una finca es ≈ 0 en búsquedas, como en los hermanos. La demanda de clientes ronda
   las 4.000 búsquedas al mes con «finca» y ≈ 6.700 sumando salón y espacio para eventos. En EE. UU., «wedding venue business plan» tiene 1.000 de media, **pero cae de 1.900 (oct-25) a 260
   (sep-26)**. Es estacional (picos de octubre a marzo) y además baja: «how to start a wedding venue» se mantiene plano en ≈ 210.
   El gemelo EN es viable, pero no se cuenta con los 1.000.

## 1. Marco legal y fiscal (delta de un ESPACIO FIJO)

**1.a Urbanismo: el uso de eventos en suelo rústico** (en suelo urbano basta con el uso compatible del plan municipal y la licencia de actividad)

| CCAA | Encaje del uso | Procedimiento y coste | Fuente · estado |
|---|---|---|---|
| Madrid | «Actos sociales y eventos familiares de especial singularidad» en **edificaciones existentes** habilitadas, en suelo no urbanizable con cualquier protección o urbanizable no sectorizado, salvo prohibición del plan municipal. También rehabilitación de edificios existentes «incluso con destino … hostelero» (art. 29.3.f) | **Calificación urbanística** (art. 148): la da el Alcalde, o el Pleno con protección sectorial. Informe en 1 mes, resolución en 3, **silencio negativo**, caduca al año sin pedir licencia. Luego, licencia | Ley 8/2012 art. 9 ✅ · Ley 9/2001 arts. 26-29 y 148 ✅ (red. Ley 7/2024) · una denegación de 2017 para «actos sociales y eventos familiares» 🟡 |
| Andalucía | Uso terciario o turístico de interés público como **actuación extraordinaria** (22.1-2), sin inducir asentamientos y proporcionado al uso (20) | **Autorización previa**, información pública ≥ 1 mes, 6 meses, **silencio desestimatorio** (22.3). **Prestación compensatoria del 10 %** del presupuesto de las obras sin maquinaria, con la licencia (22.5). Posible duración limitada (22.4) | LISTA arts. 20-22 ✅ · D. 550/2022 art. 35 🟡 · finca de Alcalá de Guadaíra para eventos tramitada así (2025) 🟡 |
| Cataluña | Solo **masías y casas rurales del catálogo** (50.2), con uso de restauración, equipamientos o servicios comunitarios (47.3 bis.h-j). Fuera: recreo al aire libre con obras mínimas, como actuación de interés público (47.4.a) | Licencia con **informe de la comisión territorial de urbanismo** (50.3), análisis de afecciones agrarias (50.1) y sin obra nueva salvo usos auxiliares (47.6.f) | TRLU arts. 47, 48 y 50 ✅ (art. 47 vigente desde el 26-03-2026) |
| C. Valenciana | Restauración a más de 5 km de suelo vacante apto, salvo turismo rural o patrimonio con informe de turismo (211.1.f.1.º); centros de ocio (211.1.f.2.º) | **DIC** previa a la licencia, también en edificios existentes (216). **Canon del 2 %** de las obras, hasta −50 % si crea empleo (221). Hasta 30 años (222). Sin DIC: reutilizar arquitectura tradicional para restauración, con informes vinculantes y +20 % (219.1), o ≤ 500 m² en suelo común (219.2.b) | TRLOTUP arts. 211-222 ✅ (art. 211 vigente desde el 11-08-2026) |

Lo común: **edificios existentes**, informe previo y **6-12 meses o más** antes de la licencia. En EE. UU. se cuentan 6-18 meses
de «zoning» y 12-36 hasta la primera boda (🟡). El resto de las CCAA, ❌: el Word da el método («pregunta en urbanismo qué figura
usa tu comunidad»).

**1.b Lo demás que el producto afirma**

| Tema | Regla para el plan | Fuente · estado |
|---|---|---|
| Espectáculos: ¿entra una boda? | La **boda** es privada (se excluyen los actos privados no abiertos al público: Madrid art. 3, Andalucía art. 1.4, C. Valenciana art. 2). **La finca que la alquila a terceros** es un establecimiento público: la C. Valenciana la cataloga como **«salón de banquetes»**, con baile solo si hay seguridad e insonorización (anexo 2.8.1) | Leyes 17/1997, 13/1999 y 14/2010 ✅ · catálogos de Madrid (D. 184/1998) y Andalucía (D. 155/2018) ❌ |
| Seguro obligatorio | Madrid: **incendio + RC** frente a asistentes y terceros (art. 6.3). Andalucía: RC (art. 14.c). Cataluña: RC como condición de la licencia (art. 23.2-3). C. Valenciana: RC con la cuantía mínima reglamentaria **para cada local** (art. 18). **Mínimos por aforo** en Andalucía (D. 109/2005, muerte e invalidez): ≤ 50 personas 225.000 € · 51-100 375.000 € · **101-300 526.000 €** · 301-700 901.000 € · > 700 1.201.000 € | Leyes ✅ · cuantías andaluzas 🟡 (documento municipal de Jerez) · Cataluña: D. 112/2010 arts. 80-81 ❌ · Madrid y C. Valenciana ❌ |
| Horarios | Los fija una orden autonómica (Madrid art. 23 ✅ remite a orden); la música exterior la limita, en la práctica, la ordenanza de ruido | orden de Madrid y del resto ❌ |
| Ruido | Límite de inmisión al exterior de una actividad nueva: **zona residencial 55 / 55 / 45 dBA (día / tarde / noche)**; zona recreativa 63 / 63 / 53. Ningún valor diario puede superarlo en 3 dB ni un LKeq,Ti en 5 dB. De noche manda el 45: **limitador-registrador**, baile final en interior y altavoces de espaldas a las viviendas | RD 1367/2007 art. 24 y anexo III tabla B1 ✅ · limitadores por ordenanza o norma autonómica ❌ |
| Autoprotección | Hallazgo 2. Con 300 invitados no hay plan estatal; sí medidas de emergencia y evacuación de la licencia y de prevención de riesgos laborales | Directriz Básica, Orden INT/1068/2026 ✅ · normas autonómicas más exigentes (p. ej., Cataluña, D. 30/2015) ❌ |
| Accesibilidad | Itinerario accesible, **aseo adaptado** y plazas de aparcamiento reservadas en la reforma (CTE DB-SUA); no discriminación en el servicio | RD 193/2023 y CTE 🟡 no releídos |
| Agua | Si la finca se abastece de **pozo propio** y tiene actividad comercial, aun con ≤ 10 m³/día es una «zona de abastecimiento tipo 1» (art. 2) y el titular responde de la calidad hasta el grifo (art. 4.3): analíticas y protocolo. Quien promueve un evento festivo garantiza agua de grifo no envasada (art. 10.5) | RD 3/2023 ✅ · vertidos y fosa séptica (autorización de la confederación hidrográfica) ❌ |
| Música (SGAE, AGEDI-AIE) | Un juzgado de Alicante entendió que la boda en un salón **no es estrictamente privada** y que paga el salón, ponga la música él o una orquesta: la finca paga la tarifa por evento o la repercute | TRLPI art. 20 🟡 · sentencia vía prensa 🟡 · tarifa de 254,20 € hasta 75 invitados (Bodas.net) 🟡 quizá antigua |
| IAE | Espacio: **861.2** (inmuebles urbanos) o **grupo 862** (rústicos). **Grupo 671** solo con catering propio; el concesionario, en el suyo (677.9). Exento de cuota con cifra de negocios < 1 M€ | RDLeg 1175/1990 ✅ · el epígrafe del espacio es criterio [estimado] · TRLRHL art. 82.1.c 🟡 |
| IVA | Hallazgo 3. En un «pack» de precio único, el espacio como accesorio del banquete al 10 % es un argumento posible (prestación accesoria del TJUE) pero arriesgado: precio propio al 21 % o **consulta vinculante** | DGT V2664-22 🟡 · TJUE C-349/96 🟡 |
| Arrendamiento de la finca | Con edificaciones es **uso distinto de vivienda** (LAU art. 3), de pacto libre (art. 4.3). El plan pide plazo ≥ 15 años, **condición suspensiva** de calificación y licencia, carencia durante las obras, reversión de mejoras y opción de compra. Finca familiar: renta **de mercado** igual (operación vinculada). Inmueble urbano: retención del 19 % (modelo 115); rústico, no | LAU arts. 3-4 ✅ · LIS art. 18 y RIRPF arts. 100-101 🟡 no releídos · cláusulas [criterio] |
| Convenio | El ALEH VI incluye a quien presta «servicio de comida y bebida… restaurantes, catering». **La finca que solo alquila no está en la lista** («no es exhaustiva»): el convenio de hostelería provincial, como referencia salarial prudente | ALEH VI art. 4 ✅ · encaje del espacio puro ❌ (asesoría) |
| Cocina de la finca | La cocina u office que use el concesionario la inscribe **él** en el registro autonómico; con catering propio, la finca | RD 1021/2022 ✅ hermano · por CCAA ❌ |
| Fuego y pirotecnia | Bengalas, fuegos y barbacoas en época de peligro: lo del paellero | paellero §1 ✅ hermano |

## 2. Benchmarks España

| Dato | Valor | Fuente |
|---|---|---|
| Bodas al año | **175.364 en 2024** (+1,7 %; definitivos, publicados el 19-11-2025). Civiles 146.605 (83,6 %) y religiosas 28.759 (16,4 %). Tasa de 3,6 por mil. Edad media: 39,9 años los hombres y 37,2 las mujeres | INE, MNP 2024 ✅ |
| Por meses (todas, % del año) | ene 3,8 · feb 5,0 · mar 5,9 · abr 8,4 · may 10,2 · jun 12,8 · jul 9,9 · ago 6,1 · **sep 13,1** · oct 11,6 · nov 7,9 · dic 5,3. Mayo-octubre: 63,7 % | INE, tabla 77171 ✅ |
| Por meses (religiosas, aproximación a la boda grande) | ene 0,8 · feb 1,8 · mar 3,5 · abr 7,3 · may 8,7 · **jun 16,2** · jul 9,3 · ago 9,0 · **sep 17,8** · oct 14,4 · nov 7,0 · dic 4,1 | INE ✅ |
| Perfil de la boda (2.100 parejas de 2025) | Coste medio **25.183 €** · **225 € por invitado** (el gasto total de la boda entre los invitados) · 53 % del presupuesto en el banquete · **115 invitados** (millennials) y 118 (Gen Z) · ceremonia civil 60 %, religiosa 35 %, simbólica 29 % · **finca 28 %**, restaurante 13 %, salón 12 %, hotel 10 % · contratan espacio el 99 %, catering el 93 %, DJ el 87 % y alquiler de mobiliario el 80 % · buscan en webs especializadas el 64 % · piden información a 6 espacios y visitan 3 · **preparan la boda 12-18 meses antes (13 de media)** | Bodas.net, Informe del Sector Nupcial 2026 🟡 (muestra de sus usuarios: sobrerrepresenta la boda grande y la finca) |
| Precio por invitado (banquete) | Menú 70-150 €, ≈ 120 € con barra libre, IVA incluido · Castilla-La Mancha, temporada media, 150 invitados: **95-200 €** por comensal (menú más barato con 2 h de barra libre); cada extra ≈ 1.500 € · fincas de Cal Blay (Barcelona): todo incluido desde 140-145 € **+ IVA**, mínimo 100 invitados | El Independiente, 27-06-2026 🟡 · OCU, 23-06-2025 🟡 · Bodas.net, promociones de 2026 🟡 |
| Alquiler del espacio | Finca Mi Cobijo (Guadalajara): sin catering exclusivo, **pago fijo de 2.500 €** y menú mínimo de 130 € · Monte y Lago: 2.900 / 3.500 / **4.500 €** (temporada baja / media / alta de 2027; dos noches con alojamiento para 30) · Santa Romana (Caldes d'Estrac): **9.700 €** en temporada alta · Castell de Vallgornera: 14.000 € con IVA el fin de semana · Madrid sin catering: «desde» 450-2.720 € el día · viernes, domingo o noviembre-marzo: **hasta −30 %** · Mallorca: gran finca desde 6.050 € (hasta 125 invitados) · directorios: «alquiler desde 200 €» o «desde 1.000 €» | fichas de Bodas.net, Venuu, todoboda, venuesplace, mallorca.com 🟡 (precios de escaparate) |
| Modelo de catering | Conviven **catering exclusivo** (SiempreVerde con Dalúa, Cal Blay como gestor de fincas), **cocina propia** («no es posible alquilar solo el espacio sin catering») y **catering libre con pago fijo** (Mi Cobijo). Bodas.net tiene en su ficha los campos «Exclusividad catering» y «¿Existe algún pago fijo por el lugar?» | fichas de Bodas.net y El Corte Inglés Bodamás 🟡 |
| Canon del catering a la finca | **12 % de lo que factura el catering** en la finca: ≈ 13 €/invitado en boda | [estimado] (rango habitual de las concesiones de hostelería, 8-15 %); ❌ sin fuente pública |
| Señal y pagos | Un laudo de consumo de Madrid recoge una señal de 1.000 € sobre 8.450 € y la cláusula «la cancelación … imputable al cliente supone la pérdida de todas las cantidades entregadas» · EE. UU.: anticipo (*retainer*) del 25-50 %, liquidación 30-60 días antes y cancelaciones del 1-5 % | laudo 🟡 · beancount 2026 🟡 · costumbre española ❌ |
| Bodas al año por finca | Sin dato español. En EE. UU., por debajo de 20 bodas al año «la mayoría está en equilibrio o por debajo», y el margen sube a partir de 25 (cifra de una consultora) · 45 de 52 sábados = 87 % (ejemplo de un local muy lleno) · 8-18 meses hasta caja positiva | fullybookedvenue 🟡 · beancount 🟡 · perfectvenue 🟡 · España ❌ |
| Tamaño de un negocio real | Traspaso de un espacio de 30.000 m² con **facturación de 250.000-500.000 €** · finca de 21.000 m² en Elda «con potencial para bodas»: **980.000 €** en venta → comprar la finca son ≈ 1-3 M€ | bedrijventekoop, cocampo 🟡 |
| Margen y comisiones | EE. UU.: ≈ 20 % (10-20 % habitual; 50-60 % los mejores) · 25-40 % neto pasadas 25 bodas (consultora) · hostelería española 7-8 % (✅ hermano) · proveedores preferentes: 500-1.500 $ por evento · cuota del escaparate de Bodas.net ❌ (por presupuesto) | Tripleseat, fullybookedvenue, beancount 🟡 |
| Costes del espacio | Limpieza tras el evento, reposición de aseos y consumibles, gasoil del grupo electrógeno, vigilancia o aparcamiento, SGAE: **≈ 650 € por boda, 350 € por evento de empresa, 300 € por celebración privada y 150 € por evento pequeño** · jardinería y mantenimiento 14.000 €/año · suministros 1.600 €/mes | [estimado] (sin tarifas públicas) |

## 3. Caso España (molde del motor de eventos: eventos × invitados × €/invitado)

**Decisiones de modelo**
- **(a) Finca + catering exclusivo concesionado.** El catering de la casa (uno o dos homologados) sirve menú y barra y paga canon.
  La finca factura el espacio y los servicios: ceremonia, mobiliario, coordinación, limpieza y aparcamiento. Es lo realista para
  la mayoría: sin cocina de producción (≈ 80-120.000 € más) ni brigada, y la seguridad alimentaria del menú es del concesionario.
  Alternativas para el Word [estimado]: **catering propio** (≈ 100-110 € por invitado, venta de ≈ 0,8-1 M€, mercancía ≈ 30 %,
  personal ≈ 35-38 %; para hosteleros, con el plan de catering) y **solo alquiler** (sin canon, ≈ 284.000 €: no cubre el
  equilibrio de caja de ≈ 290.000 €).
- **(b) La finca no se compra.** Se **arrienda con edificaciones existentes** (lo exigen Madrid, Cataluña y la vía rápida
  valenciana) o se cede la familiar con **renta de mercado**: 3.500 €/mes [estimado], el 11,5 % de las ventas y un 2,8-4,2 % bruto
  para una finca de ≈ 1-1,5 M€. Alternativa: renta mixta (2.500 € + 4 % de las ventas). Contrato de 15 años o más.

**Mezcla** [estimado; precios sin IVA para la finca = espacio y servicios + canon; anclados en §2]

| Tipología | Eventos | Inv./ev. | €/inv. | Ventas | Cómo se forma el €/inv. |
|---|---|---|---|---|---|
| Bodas: ceremonia en la finca, cóctel, banquete y fiesta (sábados y vísperas de temporada) | 30 | 120 | 47 | 169.200 | espacio ≈ 3.600 € = 30 € + canon 13 € (12 % de ≈ 110 €) + extras 4 € (horas de más, montaje premium) |
| Empresa: jornadas, convenciones, comidas, Navidad, team building | 35 | 80 | 34 | 95.200 | espacio ≈ 2.300 € = 29 € + canon 5 € |
| Celebraciones privadas: comuniones, bautizos, cumpleaños, aniversarios | 40 | 70 | 29 | 81.200 | espacio ≈ 1.600 € = 23 € + canon 6 € |
| Pequeños: preboda, brunch de después, bodas íntimas (≤ 50) | 15 | 40 | 30 | 18.000 | espacio ≈ 1.050 € = 26 € + canon 4 € |
| **Total** | **120** | **81,7** | **37,1** | **363.600** | bodas 46,5 % · empresa 26,2 % · privados 22,3 % · pequeños 5,0 % |

Las 30 bodas son ≈ 21 de mayo a octubre: ≈ 80 % de los 26 sábados de temporada (un local muy lleno de EE. UU., 87 %).

| Clave molde | Rótulo finca | Valor | Fuente |
|---|---|---|---|
| `cubiertos_dia` · `ticket_medio` · `dias_apertura` | **Mapear como el catering** (eventos al año en B4) para que el crecimiento sea de eventos, no de invitados | **120 · 37 € · 82** (= 364.080 €; +0,1 % sobre la mezcla) · 44,77 € con IVA | mezcla |
| `crec_a2` / `crec_a3` | Crecimiento de eventos | 8 % / 5 % | = hermanos [estimado] |
| Líneas de ingreso (A3, IVA por línea) | «Espacio y servicios» / **«Canon del catering»** (la línea de bebida se reutiliza como canon) | **78 % / 22 %**, las dos al **21 %** | hallazgo 3 |
| `coste_comida` / `coste_bebida` | Coste directo del evento / coste del canon | **16,3 %** de la línea de espacio (= 12,7 % de las ventas) / **0 %** | §2 [estimado] |
| `pct_consumibles` | Velas, flores base, papel y productos de los aseos | 2 % | [estimado] |
| `pct_delivery` / `comision_delivery` | Ventas que llegan por wedding planners y agencias / su comisión | 25 % / 10 % (el IVA no cambia: todo va al 21 %) | [estimado]; en EE. UU., 500-1.500 $ por evento 🟡 |
| `comision_tpv` · `pct_varios` | Cobro, sobre todo por transferencia · roturas, imprevistos y desplazamientos comerciales | 0,3 % · 2 % | [estimado] |
| `alquiler_mes` | **Renta de la finca** | **3.500 €** (fianza de 2 meses y 1 mes previo; carencia de renta durante las obras negociada aparte) | [estimado] |
| `suministros_mes` · `seguros_ano` | Luz con potencia para salón y exterior, agua de riego, gasoil, teléfono · RC de la actividad con capital por aforo (≥ 526.000 € en Andalucía para 101-300), daños a las mejoras, pérdida de beneficio y accidentes | **1.600 €** · **5.500 €** | [estimado] |
| `recursos_propios` · `prestamo` | | **100.000 €** (28 %) · **≈ 255.000 €** (CALIBRAR en F2) | [estimado] |
| `tipo` · `plazo` · `carencia` · `meses_fondo` | | 6,5 % · **8 años** (con 6, el DSCR cae a ≈ 1,25) · 1 · 3 | = hermanos, salvo el plazo |
| `vida_obra` · `vida_maquinaria` | Obras en finca arrendada: el plazo del contrato · mobiliario y equipos | **15** · 10 años | PGC (NRV 3.ª) 🟡 · LIS art. 12.1 ✅ hermano |
| `pct_bebida_alc` · `iva_bebida` | | 0 % · 21 % (es el canon) | hallazgo 3 |
| `aforo` | Invitados sentados como máximo (salón + carpa) | 300 | [estimado] |
| `rampa_mes1` · `meses_rampa` | Las bodas se reservan con 12-18 meses: la primera temporada solo trae lo que se vendió desde la licencia | **0,45 · 12** | Bodas.net 🟡 + [estimado] |
| `dias_cobro` · `dias_pago` | Novios: señal y pagos antes del evento (el motor no modela anticipos, así que es conservador) · empresa a 30-45 días · canon a 30 días | **10 · 30** | [derivado] |
| Mes 1 | Obras y licencias en otoño-invierno; se abre con las comuniones y la empresa de primavera | **marzo** | [estimado] |

**Plantilla** (€ brutos/mes en 14 pagas; jornada) [estimado, ≥ convenio de Madrid ≈ 1.337 € 🟡]
- Titular-gerente (ventas, visitas, coordinación general): **1 × 2.000 × 1,0**.
- Coordinador/a de eventos, fijo discontinuo de marzo a noviembre: **1 × 1.650 × 0,75**.
- Mantenimiento y jardinería: **1 × 1.450 × 1,0**.
- Auxiliares de evento (montaje, aparcamiento, aseos, control de acceso), fijos discontinuos: **2 × 1.350 × 0,40**.

Bruto 80.745 € + SS 33 % = **107.391 €/año (29,5 %)**. Cobertura de los auxiliares: 1.424 h disponibles frente a 1.430 necesarias
(boda 2 × 12 h · empresa 1 × 9 h · privado 1 × 8 h · pequeño 1 × 5 h) → 100 %. Camareros y cocina los pone el catering.

**Inversión** (15 partidas, **242.000 €**, sobre edificaciones existentes) [estimado; sin PVP públicos verificados]

| Partida | € |
|---|---|
| Adecuación del salón existente (suelos, cerramientos, carpintería, pintura, acústica) | 45.000 |
| Carpa estructural o pérgola para ceremonia y cóctel (plan B de lluvia) | 28.000 |
| Aseos: dos bloques y uno adaptado | 24.000 |
| Electricidad: cuadro, iluminación exterior, alumbrado de emergencia y grupo electrógeno | 26.000 |
| Climatización del salón | 18.000 |
| Office del catering: cámara, fregaderos, mesas inox, emplatado, agua y desagüe | 16.000 |
| Mobiliario de ceremonia, banquete y zona chill-out (mesas, 250 sillas, mantelería base) | 22.000 |
| Sonido, limitador-registrador y proyector | 6.000 |
| Aparcamiento y caminos (zahorra, señalización, iluminación) | 10.000 |
| Jardinería, paisajismo y riego inicial | 9.000 |
| Protección contra incendios, señalización de evacuación y accesibilidad | 7.000 |
| Proyecto técnico, calificación o autorización urbanística, licencia, tasas y prestación compensatoria o canon | 18.000 |
| Web, fotos, vídeo y marca | 6.000 |
| Constitución de la SL | 1.000 |
| Lanzamiento (feria nupcial, jornada de puertas abiertas, escaparate premium el primer año) | 6.000 |

**Necesidad ≈ 355.500 €**: inversión + fianza 7.000 + mes previo 3.500 + IVA soportado ≈ 48.700 + fondo de 3 meses ≈ 54.300.

**Fijos** (`FIJOS_EXTRA`, €/año) [estimado] = **43.000**: marketing 18.000 (escaparate de bodas, Google Ads, redes, dos ferias
nupciales y jornadas de puertas abiertas) · jardinería y mantenimiento externo 14.000 (césped, poda, riego, plagas, pintura y
reparaciones) · asesoría 3.000 · software, CRM, web y teléfono 1.800 · prevención de riesgos 500 · tasas e IBI repercutido 2.500 ·
revisiones de baja tensión y contra incendios 1.200 · limpieza general y plagas 2.000.

**Cuenta a mano, a régimen** (F2 recalcula con la rampa y la estacionalidad)

| Concepto | € | % ventas |
|---|---|---|
| Ventas | 364.080 | 100 |
| Variables: coste directo 12,7 + consumibles 2 + intermediarios 2,5 + TPV 0,3 + varios 2 | | 19,3 |
| Contribución | 293.813 | 80,7 |
| Personal | 107.391 | 29,5 |
| Renta de la finca | 42.000 | 11,5 |
| Suministros + seguros + fijos | 67.700 | 18,6 |
| **EBITDA** | **≈ 76.700** | **21,1** |
| Amortización ≈ 17.400 · intereses ≈ 16.600 | | |
| BAI | ≈ 42.700 | 11,7 |
| **Neto** (IS 15 %) | ≈ 36.300 | **≈ 10,0** |

Cuota tras la carencia ≈ 46.600 €/año → **DSCR ≈ 1,65**. Equilibrio **de caja** (fijos + intereses) ≈ 289.600 € = **95 eventos**
(holgura del 20,5 %). Equilibrio **contable** ≈ 311.200 € = **103 eventos** (holgura del 14,5 %). Si F2 da una holgura contable
< 12 %: renta mixta o +5 eventos de empresa. Si da > 25 %: bajar las bodas a 45 €. **Año 1 con rampa** (≈ 72 % de la actividad):
ventas ≈ 262.000 € y EBITDA ≈ −5.000 €, en torno a cero. Es lo esperable, porque un local tarda 8-18 meses en dar caja positiva (🟡), y el fondo de 3 meses
lo cubre. F2 lo comprueba en la Tesorería.

**Estacionalidad** (ene → dic = 100) [derivada]: bodas = media de la serie total y la religiosa del INE · empresa
4/7/9/9/10/11/5/2/9/10/9/15 [estimado] · privados con las comuniones en mayo 4/5/7/9/22/14/7/5/8/8/5/6 [estimado], ponderados por
ventas:
**3,1 · 4,7 · 6,3 · 8,4 · 12,4 · 13,5 · 7,8 · 5,5 · 12,1 · 11,1 · 7,3 · 7,7 %** (mayo-octubre 62,4 %). Con Mes 1 = marzo, la
tupla del motor va rotada: 6,3 · 8,4 · 12,4 · 13,5 · 7,8 · 5,5 · 12,1 · 11,1 · 7,3 · 7,7 · 3,1 · 4,7.

**Escenarios**: pesimista 100 eventos · 34 € · 78 invitados (≈ 265.000 €, en pérdidas); optimista 135 · 39 € · 85 (≈ 447.500 €).

**Umbrales**: coste directo ≤ 14 %, personal ≤ 33 %, renta ≤ 13 %, neto ≥ 5 %.

**Frente a los hermanos**: sin mercancía, el coste que manda es la **renta y la estructura fija** (59,6 % de las ventas frente al
≈ 40 % del parrillero). Por eso el riesgo es de ocupación, no de escandallo: con menos de ≈ 95 eventos no hay caja.

## 4. Demanda, SERP y canibalización

**Volúmenes al mes** [medido, DataForSEO 25-oct-2026]
- **España, cliente**: salón de celebraciones **1.300** · salón de eventos 1.000 · **finca para bodas 880** (pico de 1.600 en
  agosto) · fincas para eventos 720 · finca para celebraciones 590 · fincas para bodas madrid 590 · catering para bodas 590 ·
  empresa de eventos 590 · espacio para eventos 480 · **alquilar finca para eventos 480** · alquiler de fincas para eventos 210 ·
  finca de eventos 110 · hacienda para bodas 90 · fincas para bodas precios 90 · fincas para comuniones 90 · precio finca boda 50
  · cortijo para bodas 40.
- **España, emprendedor**: licencia para finca de eventos 10 · negocio de bodas 10. **Sin dato** (≈ 0): montar, negocio, plan de
  negocio, rentabilidad o «cuánto cuesta montar» una finca de bodas o eventos, licencia en suelo rústico, requisitos, plan de
  negocio de salón de eventos. Como en el catering y el paellero, **el producto vive del catálogo**.
- **EE. UU.** (oct-25 → sep-26): **wedding venue business plan 1.000** (1.900 · 1.600 · 1.300 · 1.600 · 1.000 · 1.300 · 1.000 ·
  880 · 720 · 720 · 390 · **260**) · **event venue business plan 720** (1.600 → 140, la misma forma) · how to start a wedding
  venue 210 (plano, 140-320) · event venue business 140 · wedding venue business 110 · starting a wedding venue 90 · how to open
  a wedding venue 70 · how much do wedding venues make 70 · wedding venue business plan template 50 · is owning a wedding venue
  profitable 40 · how much does it cost to start a wedding venue 30. **Lectura**: «plan» es estacional (sube de octubre a
  marzo) **y además cae**: septiembre de 2026 está un 86 % por debajo de octubre de 2025, mucho más de lo que explica la
  temporada, mientras «how to start» sigue plano. Puede ser el AI Overview o un cambio de agrupación de Google Ads ❌. Para el
  gemelo EN se cuenta con ≈ 300-800, no con 1.000.
- **Latinoamérica**: México: salón de eventos **135.000** · jardín de eventos **49.500** · salón de fiestas 33.100 · quinta para
  eventos 1.300 · hacienda para eventos 880 · jardín para bodas 720 · finca para eventos 320. Argentina: salón de eventos 18.100 ·
  quinta para eventos **3.600** · salón de fiestas 3.600 · quinta para casamientos 210 · estancia para eventos 110. Colombia:
  salón de eventos 4.400 · finca para eventos 260 · finca para bodas 70. El «plan de negocio» no tiene dato en ninguno.

**SERP ES** (las de emprendedor no tienen volumen; se miraron igual)
- **«cómo montar una finca de eventos»** (19 orgánicos, AI Overview): Mujer Urbana (cómo celebrar la boda), **10 pines de
  Pinterest con plantillas en inglés**, eventspro, totcatering (2017) y YouTube. **No hay ni una guía española del negocio.**
  PAA: ¿Cuánto se necesita para poner un salón de eventos? · ¿Cuánto cobra una organizadora de eventos?
- **«es rentable una finca de bodas»** (AI Overview): defincas, **inmoley (2017: Madrid «ha decidido restringir el régimen de
  licencias urbanísticas para las fincas rurales que organizan bodas»)**, Reddit, Emprendedores (2018), Forocoches, Finanzas
  para Mortales (2018) y venuesplace («menú desde 40 €, alquiler desde 200 €»). PAA: ¿Es un buen negocio un salón de fiestas? ·
  ¿Quién te puede casar en una finca?
- **«finca para bodas»**: local pack, AI Overview, Bodas.net, todoboda, Venuu y fichas de fincas. PAA: **¿Cuánto cuesta un
  cubierto de boda en una finca?** · ¿Quién te puede casar en una finca? · ¿Cuánto cuesta una boda para 100 personas?
  Relacionadas: baratas, precios, con alojamiento, pequeñas. **Hueco**: nadie en español explica la licencia en suelo rústico por
  comunidades, el IVA partido, el canon del catering, la Directriz de 2026 ni la tesorería del invierno.

**SERP EE. UU.**
- **«wedding venue business plan»** (AI Overview que cita a Tripleseat y Cvent): plan de un *wedding hall* (CSU, 2017),
  **Upmetrics** (ejemplo en PDF + suscripción), Kristin Binford (consultora), YouTube (plantilla gratis), Shopify,
  **ProjectionHub** (ejemplo gratis), template.net (gratis) y **Financial Models Lab: plan en Word 59 $, modelo financiero
  109 $**. PAA: Can I use my property as a wedding venue? · Do you need a license to run a wedding venue? · Is having a wedding
  venue a good investment? · What is a realistic wedding venue budget? Relacionadas: *template*, *template free*.
- **«how to start a wedding venue»**: el AI Overview da «desde 50.000 $ para arrendar o reconvertir»; Savills, Binford, Reddit,
  Cvent y Quora. PAA: Can I turn my backyard into a wedding venue? · Do you need a permit to host a backyard wedding?
- **«is owning a wedding venue profitable»**: el AI Overview dice «yes … 10-20 %, los mejores 50-60 %»; Tripleseat, Fully Booked
  Venue, Perfect Venue y Wexford (100.000-500.000 $ de ingresos).
- **Competencia de pago**: en inglés, de 59 $ (el plan) a 291 $ (el lote de Financial Models Lab), más suscripciones. **En
  español no hay ninguna**: solo plantillas para organizar la boda (Gumroad, 0-5 €) y diapositivas de Slidesgo.

**Canibalización y venta cruzada** (lo LIVE)

| Producto | Relación |
|---|---|
| `plan-catering-tematico-eventos` (45 €) · `plan-negocio-paellero-eventos` · `plan-negocio-parrillero-asador-eventos` · `plan-chef-privado-showcooking-eventos` (45 €) · `plan-negocio-cocteleria-eventos` (55 €) | **Complementarios, sin solape de keyword**: ellos son los proveedores que la finca homologa y la finca es su cliente. Enlace en los dos sentidos y el catering como «alternativa de catering propio» |
| `kit-tareas-catering` | Para el concesionario; enlace contextual |
| Hub, tarjeta de «Próximos productos» | `ProductosDigitalesHubPage.astro:1051` («packs de menú cerrado… personal por servicio»), `DigitalProductsHubPage.astro:1013` y la SPA `ProductosDigitales.tsx:1034`: **retirar al lanzar** y, si el modelo es el concesionado, cambiar el texto (la finca no vende menús ni pone personal de sala) |

**Interenlazado (cero huérfanas)**
- Añadir el plan a los `productIds` de `/usos/propietario-catering` (`src/data/use-cases-content.es.ts:822`), `catering-eventos`
  (`:2918`) y `chef-catering` (`:712`).
- Enlaces desde los posts ES `gestion-de-eventos-gastronomicos-con-ia` e `ia-catering-empresas-eventos-corporativos`, desde las
  cinco landings de eventos (`footerLinks`) y desde el hub.

## 5. Jerga y equivalencias

| España | México | Argentina | Colombia | Fuente |
|---|---|---|---|---|
| finca de eventos (y masía, cortijo, pazo, hacienda en Andalucía) | **salón de eventos**, **jardín de eventos**, hacienda, quinta | **quinta**, salón de eventos, estancia | **finca**, salón de eventos, hacienda | [medido] §4 |
| boda | boda | **casamiento** («quinta para casamientos» 210) | boda, **matrimonio** | [medido] · uso 🟡 |
| banquete, convite | banquete, recepción | fiesta, cena | recepción | glosario: «banquetes» en MX y «banquetería» en AR, CL, UY, BO y PY ✅ hermano · resto 🟡 |
| catering | catering, banquetes | **banquetería**, catering | catering | `GLOSARIO-JERGA-ES-LATAM.md` ✅ hermano |
| cóctel de bienvenida | coctel de bienvenida | **recepción** (la entrada) | coctel | 🟡 uso conocido, sin fuente leída |
| barra libre | barra libre | barra libre | barra libre | glosario: «= open bar en todas partes» ✅ hermano |
| recena | **tornafiesta** | **fin de fiesta** | — | 🟡 sin fuente leída |
| prueba de menú | degustación | degustación | degustación | 🟡 |
| señal | anticipo | **seña** | anticipo, abono | 🟡 |
| carpa, jaima | carpa, lona | carpa | carpa | 🟡 |
| salón de celebraciones | salón de fiestas (33.100) | salón de fiestas (3.600) | salón social | [medido] / 🟡 |
| fijo discontinuo, IVA, licencia | institución local (la guía de equivalencias de la familia) | | | regla del glosario ✅ |

**ES → EN (EE. UU.)**: finca de eventos y bodas → **wedding venue / event venue** ([medido]); estate venue, **barn venue**
(🟡) · alquiler del espacio → **venue fee / site fee** (beancount 🟡), *venue rental fees* (Tripleseat 🟡) · catering
exclusivo → **in-house / exclusive caterer** (🟡) · lista cerrada de proveedores → **preferred vendor list** (beancount 🟡) ·
catering libre → **outside caterer** (beancount 🟡) · señal → **retainer** (no reembolsable) + **damage deposit**
(reembolsable) (beancount 🟡; *deposit* en el glosario ✅) · prueba de menú → **tasting** (🟡) · temporada alta / baja →
**peak / off-peak season** (Tripleseat 🟡, glosario ✅) · barra libre → **open bar** (glosario ✅) · cóctel de bienvenida →
**cocktail hour** (🟡) · recena → **late-night snack** (🟡) · descorche → **corkage fee** (🟡) · consumo mínimo → **F&B
minimum** (🟡) · boda entre semana / micro-boda → **weekday wedding / micro-wedding** (Fully Booked 🟡) · licencia urbanística →
**zoning / conditional (special) use permit** (Fully Booked: *zoning* 🟡; *CUP* 🟡) · personal de evento → **W-2 event staff**
(glosario ✅) · coordinación del día → **day-of coordinator** (🟡).

## 6. Errores frecuentes, riesgos y FAQ de la landing

**Errores y riesgos** (cada uno con su sitio en el Word y en el checklist)
1. **Vender fechas sin licencia.** Si la calificación se deniega o se retrasa (silencio negativo), se devuelven señales y se
   pierde la reputación: se vende con la licencia, o con devolución íntegra pactada.
2. **Comprar la finca con el plan** (1-3 M€) o **arrendarla poco tiempo**: amortizar 242.000 € en 5 años hunde la cuenta.
   Arrendamiento de 15 años o más, con condición suspensiva, carencia durante las obras y reversión de mejoras.
3. **El ruido**: 45 dBA de noche junto a viviendas (RD 1367/2007). Sin limitador ni horario de música exterior llegan las
   denuncias y peligra la licencia.
4. **Vivir de los sábados de mayo a octubre** (64 % de las bodas, INE) con la renta y la plantilla planas: sin empresa ni
   celebraciones, el invierno quema el fondo.
5. **Infraestructura rural corta**: pozo sin control (RD 3/2023), fosa séptica para más de 150 invitados, potencia y grupo
   electrógeno, aparcamiento (una plaza por cada 2,5-3 invitados [estimado]).
6. **Un concesionario sin contrato serio**: exclusividad y plazo, canon con auditoría de cubiertos, prueba de menú, comida
   testigo, alérgenos, seguros, horarios, limpieza del office y salida.
7. **Un seguro corto**: RC con el capital por aforo de la comunidad, RC e intoxicación del catering, daños a la carpa y pérdida
   de beneficio.
8. **El clima y la fuerza mayor**: lluvia, calor o alerta de incendios (bengalas y fuegos, prohibidos en época de peligro). La
   carpa es inversión, no extra.
9. **Falsos autónomos** para el montaje y el aparcamiento: fijos discontinuos (✅ hermano).
10. **El escaparate premium sin medir el coste por contacto** (el 64 % busca en webs especializadas).
11. **El espacio al 10 % dentro de un pack**: precio propio al 21 % o consulta vinculante.

**FAQ de la landing** (de las PAA y del hueco; las cifras, las del Excel en F3)
1. **¿Cuánto cuesta montar una finca para bodas?** → El caso: ≈ 242.000 € de acondicionamiento sobre edificios existentes y
   ≈ 355.000 € con el colchón de caja. Por qué el plan no compra la finca.
2. **¿Es rentable una finca de bodas? ¿Cuánto gana?** → Neto ≈ 10 % a régimen, equilibrio en ≈ 95-103 eventos, y el primer año
   en torno a cero.
3. **¿Qué licencias necesito para celebrar bodas en una finca rústica?** → La autorización de tu comunidad antes de la licencia
   (Madrid, Andalucía, Cataluña y C. Valenciana como ejemplos), la licencia municipal, el salón de banquetes en espectáculos y el
   seguro.
4. **¿Catering propio, exclusivo o libre?** → El modelo con canon, cuándo pasar a catering propio y por qué el solo alquiler no
   cubre los fijos.
5. **¿Qué IVA lleva el alquiler de la finca y el banquete?** → 21 % el espacio con precio propio, 10 % el banquete, y cómo
   facturar el pack.
6. **¿Cuánta señal pido y qué pasa si los novios cancelan?** → Calendario de pagos y penalización proporcional y recíproca
   (TRLGDCU).
7. **¿Cómo lleno la finca fuera de temporada?** → Empresa, comuniones, bodas entre semana y la estacionalidad del INE.
8. **¿Sirve en México, Argentina, Colombia y el resto de Latinoamérica?** → La guía de equivalencias (quinta, jardín de eventos,
   salón de eventos, hacienda).

## 7. Sin verificar, preguntas abiertas y notas

- ❌ / 🟡 **Sin verificar**:
  - Normativa: cuantías del seguro en Madrid, Cataluña (D. 112/2010 arts. 80-81) y la C. Valenciana (D. 143/2015); las andaluzas
    salen de un documento municipal · catálogos de Madrid (D. 184/1998) y Andalucía (D. 155/2018) · horarios, ruido y limitadores
    · autoprotección autonómica · D. 550/2022 art. 35 · vertidos y fosa séptica · Ley de Arrendamientos Rústicos para una finca
    sin edificios · texto íntegro de la DGT V2664-22.
  - Fiscal y laboral: epígrafe de IAE del espacio puro, encaje en el ALEH, retención del alquiler en suelo rústico e inscripción
    sanitaria de la cocina usada por el concesionario.
  - Mercado: canon real de los caterings exclusivos, cuota del escaparate de Bodas.net, número de fincas y bodas por finca, señal
    y cancelación habituales, renta de mercado, tarifa vigente de SGAE y AGEDI-AIE, precios del catering propio y la caída de
    «wedding venue business plan».
- **Preguntas para el orquestador**:
  1. **Modelo**: ¿se confirma el **concesionado con canon** como caso, con el catering propio y el solo alquiler en el Word sin
     Excel? El texto del hub («packs de menú cerrado… personal por servicio») encaja mejor con el catering propio.
  2. **Canon del 12 %** sin fuente: ¿lo valida John (29 años de alta hostelería)? Mueve ≈ 22 % de las ventas.
  3. **Rampa 0,45 · 12 meses** y **Mes 1 = marzo**: comprobar en F2 que la Tesorería no se queda sin caja en el primer invierno.
     Si se queda, 4 meses de fondo.
  4. **Préstamo de ≈ 255.000 € a 8 años** sin garantía real (la finca no es nuestra): ¿nota sobre avales de una SGR? ❌ sin
     verificar qué SGR.
  5. **Mapeo del motor como el catering** (B4 = eventos) y **línea 2 = canon** con IVA del 21 % por línea: confirmar en la SPEC
     que no rompe gates heredados del parrillero.
  6. **Las cuatro CCAA**: el Word las cita como ejemplo y da el método para el resto. ¿Basta?
- **Para la SPEC**: el checklist de apertura empieza 12-18 meses antes, con el urbanismo y el arrendamiento. La calculadora de
  presupuesto por evento lleva tarifa por temporada y día (viernes y domingo −20/−30 %), mínimo de invitados, canon y extras.
  Contrato tipo con los novios (TRLGDCU) y con el concesionario (hallazgo 6).

## Fuentes

- Normativa leída hoy (BOE, API de legislación consolidada):
  - Autoprotección: [Orden INT/1068/2026, Directriz Básica de Autoprotección](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-21144) · [RD 393/2007 (nota de derogación)](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6237)
  - Urbanismo: [Ley 9/2001 del Suelo de Madrid](https://www.boe.es/buscar/act.php?id=BOE-A-2001-18984) · [Ley 8/2012 de Madrid, art. 9](https://www.boe.es/buscar/act.php?id=BOE-A-2013-2685) · [LISTA, Ley 7/2021 de Andalucía](https://www.boe.es/buscar/act.php?id=BOE-A-2021-20916) · [TRLU de Cataluña, DL 1/2010](https://www.boe.es/buscar/act.php?id=BOE-A-2010-13883) · [TRLOTUP, DL 1/2021 de la C. Valenciana](https://www.boe.es/buscar/act.php?id=DOGV-r-2021-90283)
  - Espectáculos: [Ley 17/1997 de Madrid](https://www.boe.es/buscar/act.php?id=BOE-A-1998-9648) · [Ley 13/1999 de Andalucía](https://www.boe.es/buscar/act.php?id=BOE-A-2000-1009) · [Ley 11/2009 de Cataluña](https://www.boe.es/buscar/act.php?id=BOE-A-2009-12856) · [Ley 14/2010 de la C. Valenciana](https://www.boe.es/buscar/act.php?id=BOE-A-2010-20014)
  - Ruido, higiene y agua: [RD 1367/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-18397) · [RD 1086/2020](https://www.boe.es/buscar/act.php?id=BOE-A-2020-15872) · [RD 3/2023](https://www.boe.es/buscar/act.php?id=BOE-A-2023-628)
  - Fiscal y contratos: [LIVA](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740) · [Tarifas del IAE](https://www.boe.es/buscar/act.php?id=BOE-A-1990-23930) · [LAU](https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003) · [TRLGDCU](https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555) · [ALEH VI](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2023-6344)
- Normativa reutilizada: IVA del servicio, RD 1021/2022, ET, Seguridad Social, IAE 677.9 → `catering-es-2_0/F1-research-es.md` §1 · fuego y pirotecnia → `paellero-2_2/F1-research-paellero.md` §1 · jerga → `GLOSARIO-JERGA-ES-LATAM.md` y `GLOSARIO-JERGA-ES-EN.md`.
- Secundarias legales (🟡):
  - [DGT V2664-22 (fiscal-impuestos)](https://www.fiscal-impuestos.com/tributacion-alquiler-reservados-dentro-locales-hosteleria-precio-independiente-prestacion-accesoria.html)
  - [Cuantías del D. 109/2005 (Jerez)](https://web.jerez.es/fileadmin/Documentos/OEP_2_EN_TRAMITE/0Poli_Local-2018-2018Adi-2020/4o_EJERCICIO__RESOLUCION_ALEGACIONES_ANEXO_I.pdf) · [Reus, D. 112/2010 arts. 80-81](https://www.papelea.com/ayuntamiento-de-reus/llicencia-municipal-despectacles-publics-i-activitats-recreatives-de-caracter)
  - [Comisión de Urbanismo de Madrid, 29-06-2017](https://Comunidad.madrid/sites/default/files/doc/urbanismo/cma_urb_acta_de_la_comisi-n_de_urbanismo_de_29-06-17.pdf) · [inmoley 2017](https://www.inmoley.com/NOTICIAS/1712345/2017-1-inmobiliario-urbanismo-vivienda/010-17-inmobiliario-011-23.html)
  - [Alcalá de Guadaíra, actuación extraordinaria para eventos](https://www.alcaladeguadaira.es/contenidos/downloads/ordenanzas/181-1/certificado-jgl-2025-0910-[jgl-10-10-25.-6-urbanismo_expte.-7180_2025.-admision-a-tramite-de-la-solicitud-de-autorizacion-previa-a-la-licencia-de-actuacion-extraord.pdf)
  - [SGAE y bodas (bandaancha)](https://bandaancha.eu/articulos/juez-autoriza-sgae-cobrar-bodas-3770) · [tarifas de la SGAE (Bodas.net)](https://www.bodas.net/articulos/musica-para-tu-boda-las-tarifas-de-la-sgae--c3074)
  - [Laudo de consumo de Madrid (señal)](https://www.comunidad.madrid/info/docs/2023-10/08611.0.2020.pdf)
- Mercado España:
  - Datos oficiales: [INE, MNP 2024](https://www.ine.es/dyngs/Prensa/es/MNP2024.htm) · [INE, tabla 77171](https://www.ine.es/jaxiT3/Tabla.htm?t=77171)
  - Bodas.net: [Informe del Sector Nupcial 2026](https://bodas.net/articulos/sobrevivir-organizacion-boda-informe-sector-nupcial--c9224) · [Banquete 2026](https://www.bodas.net/articulos/cuanto-cuesta-banquete-boda--c8700)
  - Precios del banquete: [OCU Castilla-La Mancha](https://www.ocu.org/organizacion/prensa/notas-de-prensa/2025/bodasclm230625) · [El Independiente](https://www.elindependiente.com/sociedad/2026/06/27/cuanto-cuesta-ir-invitada-boda-2026/) · [Cal Blay](https://www.bodas.net/fincas/sesoliveres-by-cal-blay--e2504/promociones/todo-incluido-desde-140-por-tiempo-limitado--pr347367)
  - Alquiler del espacio: [Mi Cobijo](https://www.bodas.net/fincas/finca-mi-cobijo--e273605) · [Monte y Lago](https://www.bodas.net/fincas/monte-y-lago--e124647) · [Santa Romana](https://www.bodas.net/fincas/santa-romana--e168069/promociones/oferta-precio-especial-alquiler-espacio-2026-27--pr304787) · [Castell de Vallgornera](https://www.bodas.net/castillos/castell-de-vallgornera--e253975/promociones/boda-entre-semana-ahorra-un-5--pr347207) · [Venuu Madrid](https://venuu.com/es/en/fincas-bodas-madrid-sin-catering) · [Mallorca](https://www.mallorca.com/es/consejos/vivir-en-mallorca/familia-y-vida/lugar-boda-mallorca) · [SiempreVerde (catering exclusivo)](https://www.elcorteingles.es/bodamas/finca-siempreverde-celebraciones/)
  - Compraventa y traspaso: [traspaso de un espacio de eventos](https://www.bedrijventekoop.nl/en/for-sale/109203/gran-oportunidad-de-traspaso) · [finca en Elda](https://www.cocampo.com/es/ca/properties/eeee2fcd-307b-4b88-baec-9c908539ea91/)
- Mercado y SERP de EE. UU.:
  - Rentabilidad y arranque: [Tripleseat](https://tripleseat.com/articles/opening-a-wedding-venue-101-what-you-need-to-know/) · [Fully Booked Venue](https://www.fullybookedvenue.com/owning-a-wedding-venue/) · [beancount 2026](https://beancount.io/es/blog/2026/06/03/wedding-venue-barn-private-estate-event-bookkeeping-asc-606-booking-retainer-deferred-revenue-vendor-commission-section-179-qualified-improvement-property-cost-segregation-force-majeure-cancellation-revenue-per-event-kpi-guide) · [Perfect Venue](https://www.perfectvenue.com/post/how-much-do-event-venues-make)
  - Competencia: [Financial Models Lab](https://financialmodelslab.com/products/wedding-venue-business-plan) · [Upmetrics](https://upmetrics.co/templates/wedding-venue-business-plan-example.pdf) · [ProjectionHub](https://www.projectionhub.com/post/event-venue-business-plan-guide-free-example) · [Cvent](https://www.cvent.com/en/blog/hospitality/how-to-start-an-event-venue)
- Material del repo: `src/data/products-catalog.ts:522-571` · `src/data/use-cases-content.es.ts:712, 822, 2918` · `astro-site/src/components/pages/ProductosDigitalesHubPage.astro:1051` · `DigitalProductsHubPage.astro:1013` · `src/pages/ProductosDigitales.tsx:1034` · `parrillero-2_2/cifras_caso_es.json` · `planes-v2-motor-2.2-SPEC.md` (A3)
