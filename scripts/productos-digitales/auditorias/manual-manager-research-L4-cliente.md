# LENTE 4 — Voz del cliente y vocabulario por mercado
## Research para «Manual del Manager de Restaurante» (AI Chef Pro)

Fecha de research: 2026-09-04. Autor: subagente de research (Claude), a partir de WebSearch/WebFetch/curl — sin navegador local ni Playwright, según regla del proyecto. Producto: manual operativo para gerentes/encargados/directores/jefes de sala que YA operan un restaurante, en español, mercados España + México/Argentina/Colombia/Perú/Chile/Guatemala/Panamá/Uruguay.

---

## 0. Nota metodológica — léela antes de usar este informe

El encargo pedía explotar ofertas de empleo, Amazon, prensa/blogs sectoriales, LinkedIn Pulse, podcasts/YouTube (descripción/transcripción pública) e informes de encuestas (Hostelería de España, Randstad, Adecco, Deloitte, KPMG, TheFork, Mapal, ComboHR, Nory). Resultado real, verificado en esta sesión:

| Canal | Resultado |
|---|---|
| Ofertas de empleo (InfoJobs, Turijobs, Hosteleo, elempleo.com, OCC Mundial, Computrabajo ES/MX/AR/CO/PE/CL/GT/PA/UY) | **Funcionó bien.** InfoJobs y Turijobs se dejan leer con WebFetch directo (algún 456/403 puntual). Hosteleo devuelve la ficha de una oferta pero su buscador interno no lista resultados vía WebFetch. Computrabajo/elempleo.com casi siempre entregan agregados de salario + funciones-tipo en vez de la ficha de una oferta suelta — se han citado como «síntesis de mercado», no como cita literal de una empresa, salvo cuando el WebFetch trajo el listado con nombre de empresa real (elempleo.com Bogotá, sí lo hizo). |
| Amazon.es / Amazon.com (reseñas de libros) | **Accesible con curl + `--compressed` + user-agent de escritorio** (el primer intento sin `--compressed` devolvía gzip binario ilegible — gotcha a anotar). Se extrajeron **7 reseñas reales** con nombre/apodo, estrellas, fecha (cuando la había) y texto completo, de 3 libros de gestión de restaurantes en español. Un cuarto libro (*Administración de Restaurantes*, eBook Kindle) no expuso texto de reseña en el HTML estático — sólo un bloque de imagen sin cuerpo. |
| Prensa (El Español, Cuatro.com, Infobae, InfoHoreca, ManpowerGroup) | **Funcionó muy bien.** Varias piezas con declaraciones literales de hosteleros identificables por nombre/cargo/negocio, con fecha. |
| Blogs especializados (Barra de Ideas, Diego Coquillat, Qamarero, Mapal OS, Factorial, ComboHR…) | **Funcionó bien** para patrones de dolor con cifras, aunque son paráfrasis de blog, no testimonio directo de un gerente anónimo de foro. |
| LinkedIn Pulse | **Accesible.** Dos artículos leídos completos, autor identificable (Roberto Ruiz Rúa, Fabio De Vero), con fecha. |
| Podcasts/YouTube (descripción pública) | **No se encontró contenido específico verificable** sobre el día a día de un gerente de restaurante en los canales revisados; no se ha forzado ninguna cita de esta vía. |
| Informes de encuestas | **Tres fuentes primarias verificadas de origen**: ManpowerGroup *Talent Mismatch 2026* (nota de prensa propia), Synergie España *La situación del empleo en el sector Hospitality en España 2026* (citada vía InfoHoreca/El Confidencial Digital, no se localizó el PDF del informe en sí), TheFork *Retos y Desafíos de la Restauración en España* (vía InfoHoreca), Square + American Express *Recupera tu Tiempo* (nota de prensa propia con metodología). Memoria Anual de la ITSS 2023 (vía blog especializado, cifra de infracciones). **No se encontraron** informes específicos de Deloitte, KPMG, Mapal (más allá de su blog corporativo) o Nory sobre este tema con datos verificables en español. |

**Dos estadísticas se descartan explícitamente de este informe** por no poder verificarse en su página fuente exacta:
1. «El 80 % de los profesionales de hostelería declaró problemas de salud mental» atribuida a The Burnt Chef Project — apareció en un resumen de búsqueda pero, al leer el artículo completo señalado como fuente (`lunaexperiencias.com`), el dato **no está** en el texto.
2. «Un onboarding bien estructurado mejora la retención hasta un 82 % y la productividad más de un 70 %» — cifra de tipo Gallup/BambooHR muy repetida en blogs de RRHH sin atribución consistente; no se ha podido fijar una fuente primaria verificable en español para este research, así que no se usa.

Tampoco se usa la cifra «58 % de los comensales en España consulta apps de reservas antes de elegir restaurante» (la página que la citaba, tryotter.com, devolvió 404 al intentar verificarla).

**Consecuencia para este informe:** de las citas de gerentes/encargados con nombre y cargo verificable hay **9 fuentes primarias distintas** (una con varias citas), más **7 reseñas de Amazon** (con nombre/apodo, la mitad con fecha) — 16 citas primarias en total. El resto son paráfrasis de blogs especializados y de notas de prensa de encuestas, marcadas explícitamente como secundarias.

---

## 1. Dolores del manager — 11 grupos, 27 entradas (todas con URL)

### Dolor A — Rotación y falta de personal

**A1. [PRIMARIA]** Chema Fernández, director comercial de ManpowerGroup España, en la nota de prensa del informe *Talent Mismatch 2026* (6 de mayo de 2026):
> «La hostelería se enfrenta a un reto de talento que va más allá de la escasez de candidatos. Las empresas necesitan profesionales con actitud, competencias y orientación al cliente en entornos cada vez más exigentes.»
Cifra del mismo informe: **75 %** de las empresas de hostelería españolas reconoce dificultades para encontrar personal (69 % «algunas dificultades», 6 % «muchas dificultades»); frente al 74 % de media global y 76 % de media europea del sector.
Fuente: https://www.manpowergroup.es/notas-de-prensa/la-hosteleria-espanola-se-queda-sin-manos-el-75-de-los-empresarios-no-encuentran-personal (6-05-2026)

**A2. [PRIMARIA]** Paco Quirós, propietario de 8 restaurantes, entrevistado en El Español, 3 de septiembre de 2026:
> «Tengo un 60 % de rotación, he tenido que aprender a convivir con ello.» / «Estamos viviendo un momento que parece ser que nadie necesita trabajar» y esto «nos hace sufrir un poco». / «Hay que hacer lo que se pueda para que no repercuta en la calidad.»
Fuente: https://www.elespanol.com/sociedad/20260903/paco-quiros-propietario-restaurantes-momento-parece-nadie-necesita-trabajar-hace-sufrir/1003744369297_0.html (03-09-2026)

**A3. [secundaria — informe de mercado]** Synergie España, informe *La situación del empleo en el sector Hospitality en España 2026*: la hostelería registra la **mayor tasa de rotación laboral del país, 63,8 %** — «casi dos de cada tres empleados cambian de trabajo en el plazo de un año, obligando a las empresas a mantener procesos de selección permanentes en plena campaña de verano».
Fuente: https://www.infohoreca.com/noticias/20260626/bajos-salarios-verano-hosteleria (26-06-2026)

**A4. [secundaria — mismo informe]** Sobre el salario como causa raíz: «Mientras el salario bruto medio en España alcanza los 2.345 euros mensuales, en hostelería se sitúa en 1.512 euros, un 35 % por debajo de la media nacional.»
Fuente: https://www.infohoreca.com/noticias/20260626/bajos-salarios-verano-hosteleria (26-06-2026, mismo informe de Synergie España)

### Dolor B — Cuadrantes y bajas de última hora

**B1. [PRIMARIA]** Juanjo Gondar, gerente del Asador Lapamán, en Cuatro.com, 29 de abril de 2026, sobre el paso del turno partido al continuo:
> «Trabajan mejor mucho más motivados.»
Fuente: https://www.cuatro.com/noticias/economia/20260429/hosteleria-dice-adios-turno-partido-falta-mano-obra_18_019027074.html (29-04-2026)

**B2. [PRIMARIA]** Juan Pablo Domínguez, encargado de Hakuna, mismo artículo y fecha, describiendo el turno partido que se está abandonando:
> «Vienen a las 11:00, se van a las 16 y vuelven las 19.»
Fuente: misma URL que B1 (29-04-2026)

**B3. [secundaria — blog especializado]** Sobre por qué el cuadrante se rompe cada semana: «Los cambios de última hora (una baja, una mesa de 20 sin avisar) obligan a rehacer el cuadrante sobre la marcha (…) En verano coinciden dos cosas que rompen cualquier cuadrante: menos personal disponible y más demanda. Si cada semana hay conflictos con los mismos turnos, el problema quizá no son los empleados, es el diseño del horario.»
Fuente: https://www.pascualprofesional.com/blog/interes/como-organizar-los-turnos-en-hosteleria-y-evitar-perder-dinero-cada-dia/

### Dolor C — Presión del propietario y falta de autonomía

**C1. [PRIMARIA]** Dueño de un bar en Sant Feliu de Llobregat (Barcelona) — identificado por negocio y localización, no por nombre propio (decisión editorial del medio) — entrevistado por Naroa Caro para Infobae España, 9 de septiembre de 2025:
> «He dejado a mi familia de lado. Mis hijos me han perdido toda su infancia.» / Preguntado si repetiría la experiencia de montar el negocio: «No.»
Fuente: https://www.infobae.com/espana/2025/09/09/el-dueno-de-un-bar-explica-la-realidad-de-este-negocio-en-espana-los-clientes-son-lo-mas-dificil-de-gestionar/ (09-09-2025)

**C2. [PRIMARIA]** Paco Quirós, El Español, 03-09-2026:
> «Los restaurantes están hechos por personas y las personas tienen unas circunstancias.» / Sobre su estrategia: «Quiero crecer para que quienes me han acompañado y me acompañan puedan crecer ellos personalmente, económicamente y puedan tener unas vidas mejores.»
Fuente: misma URL que A2 (03-09-2026)

**C3. [indicio indirecto — oferta de empleo real]** Anuncio de «Director/a de Restaurante» de ILO Restaurante (Madrid), publicado en Hosteleo el 11 de junio de 2026, que ofrece explícitamente «gestionar con autonomía real» y «construir equipo desde el inicio» como reclamo del puesto — señal de que la falta de autonomía es lo bastante común en el sector como para venderse como diferencial cuando no ocurre.
Fuente: https://hosteleo.com/es/sala/madrid/197844/director-de-restaurante (11-06-2026)

### Dolor D — Falta de procedimientos escritos / estandarización

**D1. [secundaria — blog especializado]** Sobre restaurantes sin manual: «Sus procedimientos no están estandarizados, no hay un sistema que indique a la gente "qué hacer" ni "cómo hacerlo". Este es un problema común en la industria.»
Fuente: patrón repetido en varios blogs de gestión (mapal-os.com, combohr.com, gestiorante.com) al buscar estandarización de procedimientos; representativo: https://mapal-os.com/es/recursos/blog/como-estandarizar-procedimientos-restaurante

**D2. [secundaria — blog especializado, con cifra]** Barra de Ideas, «El tamaño no importa: los 7 problemas que comparten pequeños y grandes», 6 de junio de 2026, sobre la dependencia de personas en vez de sistemas:
> «Si se marcha, el local tiembla.» / «Un EBITDA del 15 % a nivel de grupo puede camuflar un local estrella que sostiene la estructura.» / La diferencia entre «gestionamos por personas» y «gestionamos por sistema».
Fuente: https://barradeideas.com/el-tamano-no-importa-los-7-problemas-que-comparten-los-grupos-pequenos-con-los-gigantes-del-sector/ (06-06-2026)

### Dolor E — Reseñas negativas y quejas de clientes

**E1. [PRIMARIA]** Dueño de bar de Sant Feliu de Llobregat, Infobae, 09-09-2025, sobre la gestión de clientes (titular del propio artículo):
> «Los clientes son lo más difícil de gestionar.» / «Tienes que tener mucha calma, mucho temperamento, porque hay clientes que de verdad son majísimos… pero también tienes un 10, un 15 % que…»
Fuente: misma URL que C1 (09-09-2025)

**E2. [secundaria — blog especializado]** Sobre el protocolo de respuesta: «Decide quién responde, en cuántos días y con qué tono; deja escritos el saludo y el cierre; acuerda cómo escalar las verdaderamente feas (…) Una respuesta genérica huele a bot y resta puntos.»
Fuente: https://www.menusmart.dev/blogs/gestionar-resenas-online-restaurante

### Dolor F — Control de caja y mermas

**F1. [secundaria — blog especializado]** Sobre el riesgo del descuadre de caja: «Si encuentras grandes diferencias, notifica al gerente, ya que podría indicar problemas más serios como robo o fraude (…) Las auditorías sorpresa son las más efectivas para detectar irregularidades precisamente porque no dan tiempo para prepararse.»
Fuente: patrón repetido en varios blogs de gestión de caja (nestleprofessional.com.mx, qamarero.com); representativo: https://qamarero.com/blog/como-hacer-arqueo-de-caja-diario-en-restaurantes/

**F2. [secundaria — blog especializado]** Sobre por qué el arqueo diario no basta: la diferencia entre **corte** (cambio de turno, sin verificación), **arqueo** (foto puntual del efectivo) y **cierre** (contabilidad completa del día) — un gerente que sólo hace una de las tres se queda ciego ante fugas que sólo aparecen en otra.
Fuente: https://www.haddock.app/blog/cierre-caja-restaurante y https://thelastbitemedia.com/cierre-caja-restaurante-diferencia-entre-x-z/

### Dolor G — Conflictos en el equipo y burnout

**G1. [PRIMARIA]** Diego Coquillat, consultor de hostelería, en diegocoquillat.com, 23 de diciembre de 2021:
> «Priorizar la salud y bienestar del trabajador es el principal aspecto a la hora de reducir el impacto del burnout.»
El artículo señala que los líderes deben reconocer «cambios inexplicables en su rendimiento físico, capacidad de trabajo y humor» como señales de alerta temprana, y que el reconocimiento «mitiga posibles efectos nocivos del sobreesfuerzo laboral».
Fuente: https://www.diegocoquillat.com/como-evitar-el-burnout-o-el-sindrome-del-trabajador-quemado-en-los-restaurantes/ (23-12-2021; se cita por autoría identificable y contenido verificado, no por actualidad)

**G2. [secundaria — blog testimonial anónimo]** Sobre el desgaste en primera persona (autora identificada como chef peruana afincada en España, sin nombre propio dado): «Siento que ya no disfruto lo que antes me apasionaba.»
Fuente: https://lunaexperiencias.com/2025/06/22/el-lado-invisible-de-la-cocina-burnout-en-la-hosteleria/ (22-06-2025)

### Dolor H — Formación de nuevos empleados

**H1. [secundaria — blog especializado, cifra con atribución parcial]** «En España, sustituir a un empleado en cocina o sala tiene un coste medio de entre 2.800 y 5.000 €, sumando selección, formación del nuevo incorporado y la caída temporal de productividad del equipo.» El artículo atribuye la cifra de rotación (63,8 % en 2026) a Randstad Research, pero **no especifica una fuente directa para el rango de 2.800-5.000 €** — se cita con esa reserva explícita.
Fuente: https://factorial.es/blog/capacitar-personal-gastronomico/

**H2. [secundaria — blog especializado]** Sobre el objetivo del primer día: «Mantener al nuevo empleado bien informado desde el primer día: pasos que debe seguir, explicarle cuáles serán sus funciones, compartirle el horario, quien será la persona de contacto, las expectativas, la formación de inducción.»
Fuente: https://mapal-os.com/es/recursos/blog/onboarding-exitoso-en-tu-restaurante-u-hotel

### Dolor I — Comunicación cocina-sala

**I1. [secundaria — blog especializado]** Barra de Ideas, «Comunicación interna en restaurantes: del conflicto al equipo», 27 de febrero de 2026:
> «Un plato que sale tarde. Una comanda mal cantada. Una alergia que no llegó a cocina. Y entonces, miradas. Suspiros. Fricción.» / «Sala y cocina son mundos distintos. Que unos "pasan platos" y otros "sufren el estrés".» / «La comunicación interna en restauración no es un concepto bonito para colgar en la pared. Es un sistema operativo. Sin él, el servicio chirría.»
Fuente: https://barradeideas.com/comunicacion-interna-en-restaurantes-del-conflicto-al-equipo/ (27-02-2026)

### Dolor J — No entender los números (rentabilidad, P&L, prime cost)

**J1. [PRIMARIA]** Jay Kim, Country Manager Iberia de TheFork, citado en InfoHoreca, 18 de marzo de 2026, sobre el estudio *Retos y Desafíos de la Restauración en España* (615 profesionales encuestados):
> «La restauración española ha demostrado una enorme capacidad de adaptación en los últimos años. Sin embargo, el contexto actual exige dar un paso más en términos de gestión operativa y eficiencia.»
Cifra del mismo estudio: sólo el **39 %** revisa su rentabilidad cada semana (el 50 % lo hace mensualmente), pese a que el **70 %** dice tener una situación económica sólida — la brecha entre percepción y control real de los números.
Fuente: https://www.infohoreca.com/noticias/20260318/estudio-rentabilidad-restauracion-espana-2026-thefork (18-03-2026)

**J2. [PRIMARIA]** Gonzalo Saenz, director de Ventas de Square en España, en la nota de prensa del informe *Recupera tu Tiempo* (Square + American Express, metodología: 152 propietarios de negocios hosteleros encuestados + 6 entrevistas en profundidad, recogida entre el 20 de marzo y el 6 de mayo de 2024):
> «Los negocios que automatizan la gestión de inventarios ahorran 4 horas a la semana.»
Cifras del mismo informe: los hosteleros dedican **38 horas semanales** a administración, supervisión y formación del personal; el **77 %** considera la gestión de personal «muy estresante»; la generación y gestión de datos del negocio es el reto principal para el **37 %**.
Fuente: https://squareup.com/es/es/press/informe-recupera-tu-tiempo-de-square-y-american-express

**J3. [secundaria — blog de referencia sector]** Sobre el indicador que de verdad importa: «Prime cost está dentro de un 60-70 % es vital para mantener la rentabilidad (…) los restaurantes cuyo prime cost está descontrolado casi siempre tienen problemas de consistencia del producto, calidad de la comida y malas prácticas de gestión» — el prime cost combina food cost y coste de personal, los dos números que un manager sin formación financiera no cruza.
Fuente: https://www.restaurantowner.com/public/Why-Prime-Cost-Is-the-Most-Important-Number-That-Should-Be-on-Your-PL.cfm

### Dolor K — Cumplimiento legal (inspecciones, registro horario)

**K1. [secundaria — fuente institucional citada por blog]** Según la Memoria Anual de la ITSS (Inspección de Trabajo y Seguridad Social) de 2023, la hostelería concentra el **19,64 % de todas las infracciones** detectadas en España — el sector más sancionado del país. En 2024, las actuaciones de la ITSS en hostelería descubrieron **15.045 puestos de trabajo irregulares**, «la cifra más alta por sector». Unos **450.000 trabajadores** del sector se vieron afectados por horas extra no pagadas en 2023 (38 % del total nacional afectado por esta irregularidad, no exclusivo del sector).
Fuente: https://www.inwout.com/post/control-horario-hosteleria-sector-mas-inspeccionado

**K2. [secundaria — blog especializado, con caveat]** Sobre el registro horario digital obligatorio: «Desde enero 2026 operar sin sistema digital homologado es sancionable», con un rango de **1.000 € a 10.000 € por trabajador** (leve: 1.000-2.000 €; grave: 2.001-5.000 €; muy grave: 5.001-10.000 €). El artículo no cita el número exacto del Real Decreto — está en tramitación por decreto-ley del Ministerio de Trabajo — así que la cifra se recoge con esa reserva.
Fuente: https://qamarero.com/blog/registro-horario-digital-obligatorio-hosteleria-2026/

---

## 2. Qué se le exige a un manager según las ofertas de empleo reales

15 ofertas/fuentes de mercado analizadas (9 España, 4 Colombia, 1 México, 1 Guatemala) más benchmarks salariales agregados de Argentina, Perú y Chile.

| # | País / Ciudad | Empresa | Puesto | Funciones destacadas (literal cuando se indica) | Salario publicado | Contrato | Fuente |
|---|---|---|---|---|---|---|---|
| 1 | España, Madrid | Grupo Quispe | Jefe/a de sala | Gestión de personal, control de inventarios, supervisión del servicio | 24.000-30.000 €/año | Indefinido | Hosteleo |
| 2 | España, Madrid | Linkers (Espacio Gastronómico Emblemático) | Director/a | «Dirección y coordinación de un equipo multidisciplinar compuesto por más de 40 personas», control de costes, cumplimiento normativo | A convenir | Indefinido | Hosteleo |
| 3 | España, Madrid | ILO Restaurante | Director/a de Restaurante | «Construir equipo desde el inicio», implementar procesos, «gestionar con autonomía real» | Más de 36.000 €/año | No especif. | Hosteleo |
| 4 | España, Badajoz | Pomodoro Franquicia SL | Gerente de Restaurante | «Gestión integral del restaurante, desde la supervisión del personal hasta la optimización de costes»; gestión de RRHH, costes, seguridad alimentaria | No disponible | Duración determinada | InfoJobs |
| 5 | España, Barcelona | Restaurant Maná 75 | Encargado/Jefe de Sala | «Supervisar y coordinar el equipo de sala durante el servicio»; control de reservas, turnos, gestión operativa; volumen 300-500 comensales/día | Según convenio + incentivos | Indefinido | Turijobs |
| 6 | España, Madrid | Minor Hotels — NH Collection Eurobuilding (Casa de Comidas Rafa Zafra) | Restaurant Manager | Controlar KPIs (Food Cost, Payroll, Ticket Medio, GOP); cumplimiento APPCC; marketing digital local | Según valía | Indefinido | Turijobs |
| 7 | España, Jávea | Hotel SH Jávea | Jefe/a Restaurante — Maître | Organizar servicio, gestionar equipo de sala, controlar costes, estándares de calidad | No especif. | No especif. | Turijobs |
| 8 | España, Menorca | Meliá Hotels International (Cala Galdana 5*) | Food & Beverage Manager | Gestión de A&B en hotel 5 estrellas | No especif. | No especif. | Turijobs |
| 9 | España, Murcia | Barceló Hotel Group (Palacio San Juan) | Jefe Restaurante | Jornada completa, categoría hotelera | No especif. | No especif. | Turijobs |
| 10 | Colombia, Bogotá | Carolina Jaramillo Santacoloma | Gerente de Restaurante | Coordinar servicios de A&B, gestión de eventos, costes e inventario, liderazgo de equipos de 50+ personas | $3-3,5 M COP | Indefinido | elempleo.com |
| 11 | Colombia, Bogotá | Confidencial | Gerente de Restaurante y Eventos | Supervisar operación diaria y calidad, «planear y coordinar eventos», desarrollo de equipos y presupuestos | $5,5-6 M COP + comisión | Término fijo | elempleo.com |
| 12 | Colombia, Bogotá | Confidencial | Administrador de Restaurante | Liderar operación de sala/bar/domicilios, procesos financieros y arqueo de caja, cumplimiento sanitario, quejas de clientes | $2-2,5 M COP + propinas | Indefinido | elempleo.com |
| 13 | Colombia, Bogotá y Sabana | Compensar (agencia de empleo) | Administrador de Restaurante | Administración general, supervisión de servicio, manejo de caja e inventario, formación y evaluación de personal | $2-2,5 M COP | Término fijo | elempleo.com |
| 14 | México, CDMX | Agregado de ofertas activas | Gerente de Restaurante | Supervisión diaria, marketing y promociones, gestión de proveedores/inventario, formación de personal, control de gastos y rentabilidad | $15.000-18.000 MXN netos + alimentos + bonos por ventas | — | OCC Mundial |
| 15 | Guatemala, Ciudad de Guatemala | Agregado de ofertas activas | Gerente / Administrador de Restaurante | Coordinar y dirigir operaciones, garantizar protocolos de servicio, liderar equipo, cuadrar horarios semanales, gestionar inventario | Q3.000-11.000/mes según nivel | — | Computrabajo GT |

**Benchmarks salariales agregados (no ofertas individuales verificables con funciones literales, pero sí cifra de mercado con fuente):**
- **Argentina**: media nacional $59.641/mes; en Buenos Aires $683.905/año (~$329/hora), un 50 % por encima de la media nacional (Computrabajo AR / Glassdoor AR).
- **Perú**: entre S/ 1.994 y S/ 6.221/mes al empezar, entre S/ 2.719 y S/ 7.670/mes con 5 años de antigüedad, semana de 48 horas (Computrabajo PE / Wageindicator).
- **Chile**: entre $717.794 y $1.804.491/mes al empezar, hasta $2.556.289/mes con experiencia (Tusalario.org/Chile — Wageindicator).
- **Panamá**: media del sector restaurantes $752/mes (Computrabajo PA) — dato muy agregado, no específico de gerencia.

### Síntesis de funciones más repetidas (frecuencia sobre las 15 fuentes)

| Función | Aparece en |
|---|---|
| Supervisión y coordinación del equipo/operación diaria | 15/15 |
| Control de costes / gestión de inventario | 12/15 |
| Cumplimiento normativo (seguridad alimentaria, APPCC, sanitario) | 8/15 |
| Gestión de caja / procesos financieros | 6/15 |
| Formación y desarrollo de personal | 7/15 |
| Gestión de eventos / banquetes | 3/15 |
| KPIs explícitos (Food Cost, Payroll, GOP, Ticket Medio) | 2/15 (ambas ofertas de cadena hotelera — Minor Hotels y Grupo Quispe) |
| Marketing/redes sociales local | 2/15 |

**Lectura para el producto:** el manager de un negocio independiente (5, 4, 10-13 de la tabla) recibe una descripción **operativa y difusa** («gestión integral», «supervisar»), mientras que sólo las cadenas hoteleras (6, 8) piden explícitamente que sepa leer KPIs concretos (Food Cost, Payroll, GOP). Esto confirma el hueco: la mayoría de managers de restaurante independiente **no tiene en su propia oferta de trabajo** una lista de qué números debe controlar — coincide con el dato de TheFork (J1: sólo 39 % revisa rentabilidad semanal).

---

## 3. Vocabulario por mercado

| Concepto | 🇪🇸 España | 🇲🇽 México | 🇦🇷 Argentina | 🇨🇴 Colombia | 🇵🇪 Perú / 🇨🇱 Chile | Recomendación para el manual y la landing |
|---|---|---|---|---|---|---|
| El puesto en sí | **Gerente** / **Encargado** (jerarquía distinta: el encargado reporta al gerente; en negocios pequeños son la misma persona) / **Director** (grupos grandes) / **Jefe de sala** (específico de sala, no de todo el negocio) | **Gerente** / **Administrador** | **Gerente** / **Encargado** | **Gerente** / **Administrador de restaurante** (frecuente en ofertas reales, ver tabla §2) | **Gerente** (PE/CL) | Usar **«Manager / Gerente / Encargado»** juntos en el título y en la primera mención — cubre a España (donde «encargado» es el puesto real de nivel medio) y a LATAM (donde «administrador» es frecuente en ofertas de Colombia). Fuente jerarquía: https://combohr.com/es/blog/funciones-de-un-encargado-de-restaurante |
| Documento de turnos | **Cuadrante (de turnos)** | **Cuadrante** (el término ya se ha homogeneizado vía software de RRHH: factorial.mx lo usa igual que factorial.es) / también **horario** | **Rol de turnos** / horario | **Turnos** / horario | **Turnos** / horario | «Cuadrante» ya funciona en México por la penetración de software de turnos, pero en el habla cotidiana de bar/restaurante independiente en LATAM se dice más «el horario» o «los turnos» sin más. Usar **«cuadrante de turnos (horario del personal)»** la primera vez. |
| Verificación de caja al cierre | **Arqueo de caja** (foto puntual del efectivo) | **Corte de caja** (cambio de turno, sin verificación de exactitud) | **Cierre de caja** (contabilidad completa del día) | **Cierre de caja** / arqueo | **Arqueo** / cierre | Los tres términos **no son sinónimos** — son tres pasos distintos del mismo control (ver F2). El manual debe explicar la diferencia una vez y usar **«arqueo/cierre de caja»** como término principal, con nota de que en México «corte de caja» es el paso intermedio de cambio de turno, no el cierre. |
| Persona que sirve la mesa | **Camarero/a** | **Mesero/a** | **Mozo/a** | **Mesero/a** | **Mesero/a** (PE) / **Garzón** (CL, menos frecuente ya) | Usar «camarero/mesero» juntos en la primera mención de cada capítulo dirigido a personal de sala. |
| Espacio donde se sirve | **Sala** / **salón** | **Salón** (uso más frecuente que «sala») | **Salón** | **Salón** | **Salón** | «Sala» es más marcado como término de España; «salón» se entiende en los 6 mercados. Usar **«sala/salón»** juntos. |
| Ticket de pedido a cocina | **Comanda** (del francés *commander*, jerga de sala/cocina asentada en los 6 mercados) | **Comanda** / orden | **Comanda** / pedido | **Comanda** / pedido | **Comanda** / pedido | «Comanda» funciona igual en los 6 mercados como jerga de oficio — no hace falta adaptarlo, a diferencia de «pedido» (que en delivery se usa más para el pedido completo del cliente, no la comanda interna). |
| Verbo para pedir comida | **Pedir** | **Ordenar** (uso coloquial) / **pedir** (uso más formal/educado) | **Pedir** (no «ordenar») | **Pedir** | **Pedir** | «Pedir» es el verbo seguro en los 6 mercados; «ordenar» sólo en México, y sonaría raro en España/Argentina si se usa como verbo principal del manual. |
| Nómina/pago de personal | **Nómina** | **Nómina** | **Sueldo** / recibo de sueldo | **Nómina** | **Planilla** (PE) | El coste añadido sobre el salario bruto **varía mucho por país**: en Perú ronda el 45 % adicional (ESSALUD 9 % + otros), en Colombia el 152 % del salario base con todas las prestaciones — el manual no puede dar una fórmula única de «coste real del empleado», tiene que dejar el % como variable a rellenar por país. Fuentes: https://www.panca.pe/blog/planilla-restaurante-peru-costos-laborales/ y https://warocol.com/blog/como-calcular-nomina-restaurante-colombia |
| Control horario legal | **Registro horario** (obligatorio, digital desde enero 2026) | Control de asistencia | Control horario | Control de horario | Control horario | El marco legal es **por país**: España tiene el caso más documentado en este research (K1, K2); el manual no puede prometer que las reglas de registro horario de España apliquen igual en LATAM — dejar la sección de cumplimiento legal como «consulta tu normativa local», igual que se hizo con el IVA en la guía de Food Cost. |

**Recomendación de fondo:** igual que en la Guía Food Cost, no crear versión por país. El término de portada recomendado es **«Manual del Manager de Restaurante»** — «manager» ya es un anglicismo asentado en las 9 ofertas de empleo de España revisadas (aparece literalmente en 4 de 9) y se entiende sin traducción en los 6 mercados LATAM revisados; añadir «(gerente / encargado)» entre paréntesis en la primera mención para no dejar fuera a quien busca por el término local.

---

## 4. Objeciones de compra probables

**1. «Ya hay plantillas Excel/checklists gratis, ¿para qué pago por un manual?»**
Objeción bien fundada: existen decenas de checklists y plantillas gratuitas de gestión operativa (ej. https://combohr.com/es/blog/plantilla-checklist-restaurante, paquete de 30 plantillas en https://ingenieriademenu.com/producto/checklist-para-restaurantes/).
**Respuesta honesta:** el valor no puede ser «tener una plantilla» — tiene que ser el **criterio operativo completo** que conecta las plantillas sueltas (cuándo usar cada una, qué hacer con lo que sale de ellas) más los 5 ejes anunciados (operaciones, personas, finanzas, servicio, liderazgo) integrados, que ningún checklist gratuito cubre junto.

**2. «Esto es para cadenas / grupos grandes, mi negocio es demasiado pequeño.»**
Objeción **refutada explícitamente** por una fuente identificada: Barra de Ideas, 06-06-2026, argumenta que pequeños y grandes comparten los mismos 7 problemas estructurales (decisiones con datos fiables, ejecución consistente, mandos intermedios, rentabilidad por unidad, dependencia de «héroes» locales, arquitectura de responsabilidad, sistema vs. personas) — sólo cambia la escala, no la naturaleza del problema.
**Respuesta honesta:** el manual debe dejar explícito, con un ejemplo por escala (restaurante independiente de 8-15 empleados vs. grupo de varios locales), que los mismos 5 ejes aplican a los dos — sin fingir que un solo local necesita la misma profundidad de sistemas que una cadena.

**3. «Ya lo sé hacer / llevo años en esto, ¿qué me va a enseñar un libro?»**
Objeción confirmada literalmente por dos reseñas de Amazon sobre libros de temática afín:
- Juan Manuel Vera (2★, *Gerencia Asertiva de Restaurantes*): «Hay algunos temas interesantes pero tratadas demasiado básicos. Parece más bien un conjunto de entradas de blog.»
- oriol (3★, *Revenue Management para Restaurantes*): «Parece un trabajo final de bachillerato impreso en amazon (…) con interlineados y márgenes grandes para que ocupen más páginas.»
**Respuesta honesta:** el manual no puede competir en «explicar qué es un cuadrante de turnos» (lo hacen gratis decenas de blogs, ver §1-B3, D1). Tiene que empezar donde termina lo gratuito: casos resueltos con cifras reales por eje (una semana de cuadrante roto por bajas, un mes con caja descuadrada, un conflicto cocina-sala documentado paso a paso), no teoría general.

**4. «Es caro para lo que es.»**
Confirmada por Jorge H. (3★, *Revenue Management para Restaurantes*, reseña desde México, 02-12-2025): título de la reseña, literalmente, «Costoso», cuerpo: «Precio elevado.»
**Respuesta honesta:** contextualizar el precio contra el salario real del comprador (tabla §2: un gerente en México gana 15.000-18.000 MXN/mes, en Colombia 2-6 M COP/mes, en España 24.000-36.000 €/año) y contra el coste de UN error que el manual evita (H1: sustituir a un empleado cuesta 2.800-5.000 € en España; C2/A2: Paco Quirós describe la rotación como el problema que más «sufrimiento» le genera como propietario de 8 locales) — no ocultar el precio, situarlo al lado de lo que cuesta no tener criterio.

**5. «Mi jefe/el dueño no me va a dejar aplicar nada de esto.»**
Objeción con **evidencia indirecta pero no una cita textual verificada** — un intento de fetch a una fuente que parecía confirmarla (metodogas.com) falló por certificado SSL inválido, así que no se usa esa cita. La evidencia indirecta que sí se sostiene: el anuncio de ILO Restaurante vendiendo «autonomía real» como reclamo (§1-C3) y el propio patrón de Paco Quirós, que es dueño-gestor y describe la rotación como algo que gestiona él en persona, no delega.
**Respuesta honesta:** el manual no puede prometer que el lector conseguirá autonomía si no la tiene — puede sí ofrecer un capítulo de «cómo argumentar un cambio con datos» (conecta con el dolor J: números como palanca de autoridad frente al propietario), que es lo único que un manager sin autoridad formal puede controlar.

**6. «No me fío de comprar un documento digital sin poder probarlo antes.»**
Objeción genérica de infoproductos — **sin fuente específica encontrada en este research** dirigida a este público. Se incluye porque es la objeción estándar de cualquier producto digital de pago único, y el catálogo de AI Chef Pro ya la resuelve con el mecanismo habitual (página de producto con detalle del contenido y capturas).

---

## 5. Qué formato de producto piden

**Evidencia a favor de checklists/plantillas cortas y accionables sobre teoría larga:**
- Las dos quejas más fuertes encontradas en reseñas de Amazon apuntan en la misma dirección — **relleno vs. densidad**: «un tercio del libro dedicado a explicar matrices básicas» (A1 de la Guía Food Cost, mismo patrón) y «interlineados y márgenes grandes para que ocupen más páginas» (oriol, reseña *Revenue Management*, 07-03-2025). Un comprador de este perfil penaliza el relleno, no pide más páginas.
- La reseña más positiva encontrada premia justo lo contrario — aplicabilidad inmediata: Jules (5★, *Gerente de Restaurantes*, 08-03-2026): «Un manual de gestión sencillo y práctico que podrás ejecutar en tu negocio desde el minuto 1.» Oscar (5★, misma obra, 05-03-2025): «Un enfoque objetivo y con pasos muy útiles para organizar y gestionar el negocio de una manera eficaz y sencilla.»
- El mercado de plantillas/checklists gratuitas es grande y activo (§4-1): paquetes de 30 plantillas, checklists de apertura/cierre, formatos de arqueo — señal de demanda constante de herramientas cortas y ejecutables, no de lectura larga.
- El informe *Recupera tu Tiempo* (J2) mide el problema de fondo que explica esta preferencia: los hosteleros ya dedican **38 horas semanales** a administración y el **77 %** vive la gestión de personal como «muy estresante» — no tienen margen de tiempo para un manual que no vaya directo al grano.

**Evidencia a favor de profundidad por encima de un PDF corto:**
- Ninguna de las 7 reseñas de Amazon analizadas critica que un libro sea «demasiado corto» — todas las críticas negativas van en la dirección contraria (relleno, precio, errores de edición). Esto sugiere que el punto de fricción real no es la extensión del documento sino la **densidad de contenido útil por página**, coherente con la lección ya registrada en el research de la Guía Food Cost («documento técnico premium, no un folleto» — el problema no es la longitud, es que cada página aporte).

**Conclusión para el producto:** estructurar el manual por **capítulos autoconclusivos por eje** (operaciones, personas, finanzas, servicio, liderazgo), cada uno con casos resueltos y al menos una plantilla o checklist aplicable de inmediato — replicando el patrón ya usado en la Guía Food Cost (research L4 de ayer, §4, objeción 4) de capítulos que se leen sueltos sin depender de los demás.

---

## 6. Lo que no se pudo verificar

- **Reddit, Quora, Udemy, comentarios de YouTube**: no se han intentado en esta sesión porque el research previo del mismo proyecto (Guía Food Cost, 2026-09-03) ya confirmó el bloqueo técnico de estas cuatro vías con las herramientas disponibles en este entorno; repetir el intento habría sido gasto de tiempo sin nueva información.
- **The Burnt Chef Project** — cifra «80 % con problemas de salud mental, encuesta a 1.273 profesionales»: apareció en un resumen de búsqueda pero no se localizó en el texto completo de la página que se señalaba como fuente. Descartada.
- **Onboarding: «+82 % retención, +70 % productividad»**: cifra de tipo Gallup/BambooHR muy repetida en blogs de RRHH sin una fuente primaria consistente localizada en español. Descartada.
- **«58 % de los comensales en España consulta apps de reservas antes de elegir restaurante»**: la página que la citaba (tryotter.com) devolvió 404 al intentar verificar el dato en su fuente. Descartada.
- **Cita textual sobre «mi jefe no me deja» / falta de autonomía frente al propietario**: un intento de verificación (metodogas.com) falló por certificado SSL inválido del dominio. Se ha usado evidencia indirecta (anuncio de empleo, §1-C3) en vez de una cita directa — se señala explícitamente en §4-5.
- **Voz directa (nombre propio + cargo) de un manager en Argentina, Perú, Chile, Guatemala, Panamá o Uruguay**: no se encontró ninguna cita textual atribuida a una persona identificable en estos 6 mercados, pese a varios intentos de búsqueda dirigida — el research de estos mercados se apoya en ofertas de empleo agregadas (§2) y blogs especializados (Panca.pe para Perú, Warocol para Colombia), no en testimonio directo. Es el mismo hueco geográfico que ya se documentó ayer para la Guía Food Cost (México sin voz propia).
- **Cifra exacta del Real Decreto de registro horario digital 2026**: se cita el rango de sanciones (K2) pero la fuente no da el número oficial del decreto — está en tramitación por decreto-ley y no se ha localizado el BOE correspondiente en esta sesión.
- **Informes específicos de Deloitte, KPMG, Mapal (más allá de su blog) o Nory** sobre gestión de restaurantes en español: no se encontraron informes públicos con datos verificables de estas cuatro fuentes citadas en el encargo original; sólo Mapal OS aportó contenido (de blog corporativo, no informe con metodología publicada).
