# LENTE 2 — Keywords, SERP e intención — Manual del Manager de Restaurante

Fecha de research: 2026-09-04. Producto: categoría nueva «Manuales operativos», pago único, ES. Público: gerentes/encargados/directores/jefes de sala que YA operan (no aspirantes, no dueños que quieren montar el restaurante). Ejes: operaciones, personas, finanzas, servicio, liderazgo.

Herramienta: `scripts/dataforseo.py` (DataForSEO Google Ads + SERP orgánica en vivo). **Nota operativa**: el `python3` por defecto del Mac fallaba con `SSL: CERTIFICATE_VERIFY_FAILED` (cadena de certificados autofirmada); se resolvió corriendo `Install Certificates.command` del framework de Python 3.7 instalado en `/Library/Frameworks/Python.framework/Versions/3.7/`, que reenlaza el almacén de certs del sistema al bundle de `certifi`. Después de eso DataForSEO respondió con normalidad — **funcionó de principio a fin**, no hay datos «no medidos» por fallo de credenciales.

---

## §0. Lectura honesta: ¿hay demanda de búsqueda para este producto?

**Sí hay demanda — pero es demanda de PROBLEMA/PUESTO, no de nombre de producto, y está repartida en volúmenes bajos por keyword.** Ningún término suelto es un «volumen alto» al estilo de una keyword de e-commerce; el patrón se parece al de la Guía Food Cost (ayer): el dinero entra por research de intención y por activos propios, no por una sola keyword estrella.

Tres lecturas cruzadas:

1. **El puesto tiene búsqueda real, pero en España está DOMINADA por empleo.** «Gerente de restaurante» (50/mes ES) y «encargado de restaurante» (40/mes ES) traen SERP con AI Overview + 90% resultados de InfoJobs/LinkedIn/Turijobs/Indeed/Glassdoor. Nadie busca «cómo ser mejor gerente» con esas cadenas exactas — busca trabajo o busca cuánto cobra. Coincide con el diagnóstico de GSC: cero tráfico propio en «gerente»/«encargado».
2. **México multiplica el volumen del puesto ×14 respecto a España** («gerente de restaurante» 720/mes MX vs. 50/mes ES) y ahí la SERP YA NO es solo empleo — hay contenido educativo real compitiendo (Ostelea, ComboHR, Indeed-orientación, BCH). Argentina y Perú se quedan bajos (10-30/mes); Colombia y Chile prefieren «administrador de restaurante» sobre «gerente» (140-260/mes) — es el término local dominante, no una variante menor.
3. **Hay un libro real vendiéndose para esta búsqueda exacta.** La SERP de «manual del gerente de restaurante» (0 volumen medible, cola larguísima) trae en el puesto 2 y 14 el ebook «Gerente de Restaurantes: Manual de cabecera del líder de negocio de restauración» (Amazon/Gandhi/Casa del Libro) y en el 13 el clásico *Restaurant Manager's Handbook* (Douglas Robert Brown) traducido. **Esto no lo dice el volumen — lo dice la SERP**: hay compradores dispuestos a pagar por exactamente este formato, aunque la keyword de búsqueda directa no tenga volumen medible. Es la misma lógica que sostuvo la Guía Food Cost: «guia food cost» = 0 y aun así el producto vendió por canales propios.
4. **Los términos «herramienta del manager» (Grupo C) tienen intención MUY mixta y volumen bajo o nulo con la cadena exacta**, pero conducen a piezas de contenido reales (checklists, cuadrantes, KPIs) que sí tienen demanda cuando se generaliza el término (p. ej. «cuadrante de turnos» 50/mes sin «restaurante», «rotación de personal» 70/mes sin «hosteleria»). Esto es oportunidad de blog/interlinking, no de landing.

**Conclusión operativa**: la landing no puede depender de una sola keyword «cabeza» con volumen alto — no existe. Debe apoyarse en (a) la intención de PUESTO en México principalmente y España en menor medida, (b) diferenciarse desde el minuto uno de las ofertas de empleo (el mayor ruido de la SERP), y (c) usar el interlinking con los 8 posts propios ya publicados sobre gestión/gerente/rotación/KPIs (§5) como el motor de tráfico real, no el volumen de búsqueda directo.

---

## §1. Tablas de volúmenes por grupo y país

Volumen mensual, Google Ads, DataForSEO. `None` = sin dato devuelto (posible volumen 0 o cadena no reconocida). Escala de competencia LOW/MEDIUM/HIGH tal cual la devuelve la API (Google Ads Keyword Planner).

### Grupo A — Puesto y funciones (España)

| Keyword | Vol/mes ES | Competencia |
|---|---|---|
| gerente de restaurante | 50 | LOW |
| funciones encargado de restaurante | 50 | LOW |
| funciones de un gerente de restaurante | 40 | LOW |
| encargado de restaurante | 40 | LOW |
| jefe de sala funciones | 30 | LOW |
| director de restaurante | 20 | LOW |
| que hace un gerente de restaurante | 10 | LOW |
| manager de restaurante | 10 | MEDIUM |
| administrador de restaurante | 10 | LOW |
| gerente de restaurante sueldo | 10 | LOW |
| cuanto gana un gerente de restaurante | 10 | — |

### Grupo A — México, Argentina, Colombia, Chile, Perú (subconjunto de 11 kws, misma cadena)

| Keyword | MX | AR | CO | CL | PE |
|---|---|---|---|---|---|
| gerente de restaurante | **720** | 10 | 20 | 20 | 30 |
| administrador de restaurante | 70 | 10 | **140** | **260** | **170** |
| administracion de restaurantes | 140 | 20 | 50 | 40 | 140 |
| funciones de un gerente de restaurante | 140 | 10 | 10 | 10 | 10 |
| cuanto gana un gerente de restaurante | 90 | 10 | 10 | 10 | 10 |
| encargado de restaurante | 50 | 30 | 10 | 10 | 10 |
| gestion de restaurantes | 50 | 20 | 20 | 10 | **210** |
| como administrar un restaurante | 50 | 10 | 10 | 10 | 50 |
| director de restaurante | 30 | 10 | 10 | 10 | 10 |
| manager de restaurante | 20 | 10 | 10 | 10 | 10 |
| curso gerente de restaurante | 10 | 10 | 0 | 0 | 10 |
| manual del gerente de restaurante | None | None | None | None | None |

**Lectura**: México es, con diferencia, el mercado de mayor volumen absoluto para «gerente». Fuera de México, «administrador de restaurante» le gana a «gerente» en Colombia, Chile y Perú — es el término preferido en el Cono Sur/Pacífico, no una curiosidad menor. Argentina se queda plana en todos los términos (10-30/mes): mercado de bajo volumen de búsqueda para este nicho, sea cual sea el término.

### Grupo B — Producto/formación (España)

| Keyword | Vol/mes ES | Competencia |
|---|---|---|
| gestion de restaurantes | 110 | MEDIUM |
| curso gestion de restaurantes | 70 | MEDIUM |
| como gestionar un restaurante | 30 | MEDIUM |
| direccion de restaurantes | 30 | LOW |
| manual de operaciones de un restaurante | 10 | MEDIUM |
| manual de operaciones restaurante pdf | 10 | LOW |
| manual de procedimientos de un restaurante | 10 | LOW |
| manual de funciones de un restaurante | 10 | — |
| curso gerente de restaurante | 10 | HIGH |
| como administrar un restaurante | 10 | — |
| administracion de restaurantes | 10 | HIGH |
| manual del gerente de restaurante | None | — |

Variantes adicionales probadas (todas `None`, es decir sin volumen medible): «manual de gestion de restaurante», «guia para gerente de restaurante», «como ser un buen gerente de restaurante» (10, HIGH), «habilidades de un gerente de restaurante» (10), «perfil de un gerente de restaurante» (10), «responsabilidades de un gerente de restaurante» (10), «formacion para gerentes de restaurante», «plan de formacion gerente restaurante», «manual del encargado de restaurante», «funciones de un director de restaurante» (10, HIGH), «que hace un encargado de restaurante» (10, LOW).

**Lectura**: el término genérico «gestión de restaurantes» (110/mes ES) es el único de este grupo con volumen apreciable, y su SERP (§2) es 100% formación reglada (másteres, cursos de escuelas de hostelería), no productos digitales de pago único. Ninguna variante con «manual» supera 10/mes en ningún mercado medido — confirma que nadie busca el FORMATO «manual» de forma explícita; busca el problema.

### Grupo C — Herramientas del manager (España; sin sufijo «restaurante» cuando la cadena con sufijo dio `None`)

| Keyword | Vol/mes ES | Competencia |
|---|---|---|
| rotacion de personal *(sin «hosteleria»)* | 70 | LOW |
| cuadrante de turnos *(sin «restaurante»)* | 50 | MEDIUM |
| kpi restaurante | 20 | LOW |
| protocolo de servicio en restaurante | 20 | LOW |
| indicadores de gestion de un restaurante | 10 | — |
| checklist restaurante | 10 | MEDIUM |
| checklist apertura restaurante | 10 | LOW |
| briefing restaurante | 10 | LOW |
| arqueo de caja restaurante | 10 | HIGH |
| libro de reclamaciones restaurante | 10 | MEDIUM |
| control horario hosteleria | 10 | HIGH |
| manual de servicio al cliente restaurante | 0 | — |
| estandares de servicio restaurante | None | — |
| reunion pre servicio restaurante | None | — |
| cuadrante de turnos restaurante *(con sufijo)* | None | — |
| como responder reseñas negativas restaurante | None | — |
| rotacion de personal hosteleria *(con sufijo)* | None | — |
| plantilla evaluacion desempeño restaurante | None | — |
| evaluacion de desempeño restaurante | None | — |
| reseñas negativas restaurante | None | — |
| registro de jornada hosteleria | None | — |
| desperdicio alimentario restaurantes | None | — |
| verifactu hosteleria | None | — |

**Lectura clave — trampa de sufijo**: casi todas las keywords «herramienta + restaurante» exacta dan `None`, pero la MISMA herramienta sin el sufijo tiene volumen real («rotación de personal» 70, «cuadrante de turnos» 50). El patrón es igual al de «chile crisp» vs. «chili crisp» del 2026-08-02: **la gente no añade «restaurante»/«hostelería» a estas búsquedas; busca el concepto genérico y ya filtra ella misma en la SERP**. Esto es una señal de contenido de blog (título genérico + ángulo hostelería en el cuerpo), no de landing.

### Grupo D — Legal del manager (España)

| Keyword | Vol/mes ES | Competencia |
|---|---|---|
| verifactu *(genérico, sin «restaurantes»)* | **74.000** | MEDIUM |
| convenio hosteleria *(sin año)* | **1.600** | LOW |
| hojas de reclamaciones *(sin «restaurante»)* | **1.300** | LOW |
| ley de desperdicio alimentario | 390 | LOW |
| registro horario hosteleria | 10 | HIGH |
| libro de reclamaciones restaurante | 10 | MEDIUM |
| control horario hosteleria | 10 | HIGH |
| convenio hosteleria 2026 | None | — |
| hojas de reclamaciones restaurante | None | — |
| ley desperdicio alimentario restaurantes | None | — |
| verifactu restaurantes | None | — |
| desperdicio alimentario restaurantes | None | — |
| registro de jornada hosteleria | None | — |

**Lectura**: los términos legales genéricos (Verifactu, hojas de reclamaciones, convenio hostelería) tienen volumen ALTO pero son territorio horizontal (aplican a cualquier negocio, no solo restaurantes) y de alta exigencia de actualización normativa — no son la puerta de entrada de este producto, pero sí candidatos claros de **contenido de blog de captación** con ángulo hostelería, ya señalados como oportunidad general en `CLAUDE.md` («piezas de captación… se miden por tráfico»). Ninguno debe ir en el nombre/slug del producto: es contenido, no producto.

---

## §2. Análisis de SERP keyword a keyword

### 1. «gerente de restaurante» (50 ES / 720 MX) — AI Overview: sí (empleo) · PAA: sí
Top 19: **17 de 19 resultados son empleo** (InfoJobs×3, LinkedIn, Turijobs, Glassdoor, Indeed×2, Jooble, Jobijoba) o descripciones de puesto para reclutadores (Workable). Solo 4 son contenido educativo: Indeed-orientación (#5, funciones/requisitos/salario), Frucosol (#6, «cómo ser buen gerente»), CombOHR (#10), Ostelea (#13), Barcelona Culinary Hub (#14), Fish Solutions/Pescanova (#19). **Ninguno es un producto de pago; todos son blog gratuito de escuelas o proveedores.**
PAA: ¿Cuáles son los 4 tipos de Gerentes? / ¿Cuáles son las 4 funciones de un gerente? / ¿Cuáles son las 5 características de un buen gerente? / ¿Cuáles son los 7 Hábitos para Gerentes®? / ¿Cuáles son las 10 habilidades más importantes para un gerente? / ¿Cuáles son las fortalezas de un gerente? / ¿Qué habilidades blandas debe tener un gerente? / ¿Cómo ser un buen gerente?
**Hueco**: el PAA es genérico de «gerente» (no específico de restaurante) — nadie en el top 19 responde con profundidad ESPECÍFICA de restaurante a «qué habilidades» o «qué tipos de gerente», y ninguno tiene tabla/checklist descargable.

### 2. «encargado de restaurante» (40 ES / 50 MX) — sin AI Overview · PAA: sí
Top 19: **13 de 19 son empleo** (JobToday×2, InfoJobs×3, Milanuncios×2, LinkedIn×2, Glassdoor, Indeed, Hosteleo, Jobted). Solo 5 educativos: Loomis Pay (#8, «10 funciones clave»), ProfesionalHoreca (#9), CombOHR (#12), un vídeo de YouTube (#19, «Funciones del Gerente» aunque la búsqueda es «encargado»). Dos resultados de SALARIO (Jooble #15, Indeed #17).
PAA: ¿Qué hace el encargado de un restaurante? / ¿Cuáles son los rangos en un restaurante? / ¿Qué funciones tiene un encargado? / ¿Cuáles son las funciones de un encargado de hostelería? / ¿Cómo se llama el encargado del restaurante? / ¿Cuáles son las tareas de un encargado de local? / ¿Cuáles son las 4 funciones de un supervisor? / ¿Cuánto cobra una encargada de tienda? / ¿Cuáles son las funciones de un encargado de local comercial?
**Hueco**: «¿Cuáles son los rangos en un restaurante?» y «¿Cómo se llama el encargado del restaurante?» delatan que el propio usuario no tiene claro el vocabulario del sector (gerente/encargado/director/jefe de sala) — nadie en el top 19 aclara la jerarquía con un organigrama.

### 3. «gestión de restaurantes» (110 ES / hasta 210 PE) — AI Overview: sí (definición) · PAA: sí · Related: sí
Top 19: **formación reglada domina** — másteres (UCM, Hofmann, Barcelona Culinary Hub×2), cursos (bculinary, grupoaspasia, ESAH, UOC, Chef Ejecutivo, egci.es), y blogs de gestión general (Gasma, La Famiglia, camarero10). Related searches confirma la intención: «Curso gestión restaurantes gratis», «Máster en gestión de restaurantes», «Gestión de la restauración SEPE» (formación pública/subvencionada).
PAA (mezclado con ruido de software genérico): ¿Qué es la gestión de restaurantes? / ¿Cómo se gestiona un restaurante? / ¿Cuáles son los 4 tipos de mise en place? (ruido) / ¿Qué programa puedo usar para gestionar un restaurante? / ¿Qué software recomienda para Restaurantes? / preguntas de ERP genérico (ruido).
**Hueco**: la intención de esta keyword es mayoritariamente FORMACIÓN CARA Y LARGA (másteres de meses, miles de euros) — un manual de pago único y consulta puntual es un sustituto de menor fricción que ningún resultado del top 19 ofrece; el «Curso gratis SEPE» es la única alternativa low-cost y no cubre operación real.

### 4. «como administrar un restaurante» (10-50 según país) — AI Overview: sí · PAA: sí (contaminado)
Top 18: mezcla de blogs latinoamericanos de software POS (Poster/joinposter.mx, DoorDash-merchants, Square) y blogs de escuelas (CESSA México, cursosgastronomia.com.mx). El AI Overview responde con «Control Financiero / Monitorea ventas / Vigila inventario» — una respuesta genérica de checklist.
PAA: **contaminado con preguntas de «tipos de menú» y «protocolo de servicio»** (¿Cuáles son los 3 tipos de menú? / ¿En qué orden se deben colocar los platos? / ¿Qué se sirve primero en una cena?) — señal de que Google no tiene intención clara para esta cadena y mezcla consultas de servicio de sala.
**Hueco**: ningún resultado integra finanzas + personal + servicio + legal en un solo documento; todos son listas de 5-25 tips sueltos sin profundidad ni ejemplo numérico.

### 5. «curso gestión de restaurantes» (70 ES) — AI Overview: sí · Related: sí
Top 19: **100% formación reglada** (bculinary, grupoaspasia -gratis SEPE-, ESAH, Cámara de Madrid, Hofmann, UOC, Adams -gratis-, UDIMA -específico para gerentes: «Curso Superior en Gerencia de Restaurantes»-, Mondragón, UCM, Gastrouni, Academyformacion). **Cero productos digitales de autoservicio**; todo es curso con matrícula, tutor y certificado.
**Hueco/oportunidad de posicionamiento**: esta intención es de FORMACIÓN, no de producto de consulta — confirma que el Manual no debe posicionarse como sustituto de un curso reglado (perdería contra instituciones con autoridad de dominio), sino como la herramienta de aplicación inmediata que ningún curso entrega en formato manual/checklist.

### 6. «manual de operaciones de un restaurante» (10 ES) — AI Overview: sí · PAA: sí · Related: sí
Top 18: **el más relevante de todo el research** — envanature.com (#1), elBulliFoundation/CaixaBankLab (#2, ya mapeado ayer en la lente de Food Cost), Scribd (#3, PDF universitario), Mapal-OS, ComboHR, Monouso, tesis universitaria (dspace.ucuenca.edu.ec), La Gastroria (MOF), ingenieriademenu.com, **Purohospitality («Manual de operaciones de restaurante rentable», 30-jul-2026, fecha reciente)**, tspoonlab.
Related searches: «Manual de operaciones restaurante PDF» · «Manual de procedimientos cocina restaurante» · «Manual restaurante» · **«Protocolo de servicio en un restaurante PDF»** · «Organigrama y funciones de un restaurante» · «Departamentos de un restaurante».
PAA: ¿Cómo hacer un manual de procedimientos para un restaurante? / ¿Cuáles son las operaciones de un restaurante? / ¿Qué debe contener un manual de operaciones? / (+ 6 preguntas de «normas de seguridad», ruido de HACCP/PRL).
**Hueco**: de 18 fuentes, NINGUNA es un producto de pago con plantilla lista para usar — todo es blog gratuito o PDF académico/institucional suelto. Es el hueco más claro de todo el research: la intención EXISTE, la cobertura es de blog, no de producto.

### 7. «kpi restaurante» (20 ES) — AI Overview: sí · PAA: sí · Related: sí
Top 17: blogs especializados de software (Orquest, Fudo, OlaClick, Rappi-merchants, CoverManager, Gastrobooster, Clab, Masterestaurant -con dashboard gratis descargable-), Barcelona Culinary Hub, CombOHR, un TikTok, un TFG universitario (URJC), Scribd («50 KPIs esenciales», documento de pago en la plataforma).
PAA (parcialmente contaminado con KPI genérico de ventas/RRHH): ¿Cuáles son los 5 principales KPIs? / ¿Qué son KPIs y ejemplos? / ¿Qué es un KPI de negocio? / (+ ruido de «indicadores de calidad», «indicadores de productividad»).
**Hueco**: hay un competidor directo de FORMATO — Masterestaurant ofrece un «Dashboard KPIs para Restaurantes Gratis» con 45+ indicadores — es la prueba de que el mercado SÍ compra/descarga estas herramientas cuando están bien empaquetadas, y que un manual de pago tendría que superar claramente a una alternativa gratuita ya existente en cobertura o en integración con el resto del manual (KPIs + personal + servicio + legal en un solo documento, no solo KPIs sueltos).

### 8. «checklist apertura restaurante» (10 ES) — AI Overview: sí · PAA: sí · Related: sí
Top 16: **el hueco de formato más evidente**: Scribd (PDF genérico de limpieza), Makro (checklist para ABRIR el NEGOCIO, no el turno diario — confusión de intención), Pinterest, Marketman (**«Lista de apertura para directores de restaurante»**, en inglés traducido, el más cercano al público del manual), avantagesfeedback.com (3-ago-2026, «caja, stock, equipo y servicio», publicado hace un mes — competencia activa reciente), CombOHR (plantilla descarga gratis), Shifty-app, Adrián Pollán (24 puntos, herramienta con seguimiento), Etsy (checklist de pago, formato editable).
Related: «Checklist Restaurante formato PDF» · «Checklist restaurante formato Excel» · «Check list de apertura y cierre» · «Check list restaurante gratis» — **la intención de FORMATO (PDF/Excel descargable) es explícita en las relacionadas**, mucho más que en cualquier otra keyword del research.
**Hueco**: la mitad de los resultados confunden «checklist de apertura DEL NEGOCIO» (trámites, licencias) con «checklist de apertura DE TURNO» (caja, stock, servicio) — el manual puede ganar autoridad simplemente distinguiendo ambas cosas desde el primer párrafo, cosa que Makro (#2) no hace.

### 9. «cuadrante de turnos» (50 ES, sin sufijo) — sin AI Overview · PAA: sí · Related: sí
Top 18: **100% herramientas de software/apps** (Factorial, CheckInGO, Bizneo, Skello, ComboHR, Cuadraturnos, apps de Google Play×2, Personio, Ofimood, Holded -plantillas Excel gratis-, Shiftbase, Aturnos, Cegid, Cucorent). Ninguno es específico de restaurantes — es intención horizontal de RRHH.
**Hueco**: no hay hueco de contenido aquí — es territorio de software SaaS bien cubierto y no específico de hostelería. Confirma que en el manual esta herramienta debe presentarse como PLANTILLA dentro del paquete, no como pieza de captación independiente (competir por esta keyword contra 15 SaaS de RRHH no es rentable).

### 10. «rotación de personal» (70 ES, sin «hosteleria») — AI Overview: sí · PAA: sí · Related: sí
Top 18: **100% contenido de RRHH genérico** (Cegos, Personio, Factorial, HRider, Nailted, TalentClue, Grupo Castilla, un paper académico Redalyc, Bizneo, Randstad, OpenHR, PeopleForce, DKV Integralia, Payfit, Adelantta, Edenred). **Ninguno menciona hostelería ni restaurantes.**
**Hueco real**: la rotación de personal en hostelería tiene características propias (temporalidad, turnos partidos, salario base bajo) que NINGUNO de los 18 resultados aborda — hay un post propio ya publicado sobre esto (`gestion-personal-hosteleria-ia-reducir-rotacion.md`, ver §5) que puede alimentar directamente esta sección del manual y enlazar de vuelta.

### 11. «cuanto gana un gerente de restaurante» (10-90 según país) — AI Overview: sí · PAA: sí (contaminado, reciclado del #1)
Top 19: **datos de salario dispersos y contradictorios entre fuentes**: Wageindicator (1.593-2.383€/mes inicial), Glassdoor (30.330€/año media, hasta 95.200€ percentil 90 — rango sospechosamente amplio), InfoJobs (20.500€ + variable), HuffPost (2.500-3.800€/mes, cifra muy superior a las anteriores), Barcelona Culinary Hub (25.000-33.000€/año Madrid/BCN), Ostelea (18.000-24.000€/año pequeño-mediano). **Ninguna fuente explica la varianza** (tipo de establecimiento, ciudad, si incluye variable).
**Hueco**: es una pregunta de referencia salarial que un manual puede responder con tabla comparativa y citando la varianza — no es tráfico de compra directa pero es material de FAQ/autoridad de bajo coste de producción.

### 12. «convenio hostelería» (1.600 ES, sin año) — AI Overview: sí · PAA: sí · Related: sí
Top 19: **legal puro, fragmentado por provincia** (Valencia, Málaga, Cataluña, Alicante, Murcia, Cádiz, Zaragoza, Pontevedra, Madrid + BOE estatal). Ningún resultado es un producto de pago; todo son sindicatos, patronales, boletines oficiales y 3-4 blogs de SaaS de RRHH (Skello, Payfit, Haddock, Qamarero) explicando el convenio en general.
**Hueco**: territorio de contenido de captación (alto volumen, baja competencia de producto), NO de landing de producto — un manual «del manager» no puede prometer cubrir 17 convenios provinciales distintos sin perder credibilidad; mejor un capítulo genérico + remisión a fuente oficial por provincia.

### 13. «hojas de reclamaciones» (1.300 ES, sin sufijo) — AI Overview: sí · PAA: sí · Related: sí
Top 18: **100% institucional** (portales autonómicos de consumo: Junta Andalucía, Comunidad de Madrid, Aragón, Canarias, Castilla-La Mancha, Murcia, Baleares, Castilla y León, Cataluña) + 2 blogs explicativos (Portal del Comerciante, Alex Legal). Cero contenido específico de restaurantes.
**Hueco**: mismo patrón que Verifactu — volumen alto pero horizontal y de máxima exigencia normativa (varía por comunidad autónoma). Blog, no landing de producto.

### 14. «administrador de restaurante» (México, 70/mes) — sin AI Overview · PAA: sí
Top 19: **mezcla de empleo (Indeed MX, OCC×3, Computrabajo×2) y contenido educativo real y específico** (Winterhalter, Nestlé Professional MX «guía completa», Siigo -software contable, con blog de «funciones»-, ISIL Perú, UFV -universidad española, curiosamente-, emcebar.org.mx -curso presencial CDMX/Puebla/Guadalajara-).
PAA: ¿Qué es lo que hace un administrador en un restaurante? / ¿Cuánto gana un administrador de restaurantes? / ¿Cómo se le llama al administrador de un restaurante? (la misma confusión de vocabulario que en ES) / + genérico de «administrador» (ruido).
**Hueco**: en México el término «administrador» convive con «gerente» sin que ninguna fuente aclare la diferencia (sinónimos regionales vs. jerarquía real) — oportunidad de aclarar esto en la FAQ para servir a los dos mercados con una sola landing.

---

## §3. Intenciones: EMPLEO / FORMACIÓN / PROBLEMA

| Keyword | Intención dominante | % aprox. en SERP |
|---|---|---|
| gerente de restaurante | **EMPLEO** | ~17/19 (89%) |
| encargado de restaurante | **EMPLEO** | ~13/19 (68%) |
| administrador de restaurante (MX) | EMPLEO + educativo mixto | ~7/19 (37%) empleo |
| cuanto gana un gerente de restaurante | EMPLEO/SALARIO (referencia, no oferta) | 19/19 salario, 0 compra |
| gestión de restaurantes | **FORMACIÓN** (másteres/cursos) | ~13/19 (68%) |
| curso gestión de restaurantes | **FORMACIÓN** | 19/19 (100%) |
| curso gerente de restaurante | **FORMACIÓN** (UDIMA: «Curso Superior en Gerencia») | alta |
| como administrar un restaurante | **PROBLEMA** (mezclado con tips genéricos) | ~14/18 (78%) |
| manual de operaciones de un restaurante | **PROBLEMA** (el más puro de todo el research) | 18/18 (100%) |
| kpi restaurante | **PROBLEMA** | 17/17 (100%) |
| checklist apertura restaurante | **PROBLEMA**, con confusión apertura-negocio vs. apertura-turno | 16/16 (100%) |
| cuadrante de turnos | **PROBLEMA** (pero horizontal SaaS, no específico) | 18/18 (100%) |
| rotación de personal | **PROBLEMA** (horizontal RRHH, sin ángulo hostelería) | 18/18 (100%) |
| convenio hostelería | **PROBLEMA/LEGAL** (institucional, no producto) | 19/19 |
| hojas de reclamaciones | **PROBLEMA/LEGAL** (institucional, no producto) | 18/18 |

**La trampa mayor, confirmada tal como avisaba el encargo**: «gerente de restaurante» —la keyword más obvia para nombrar el producto— es **90% ofertas de empleo**. Cualquier título/landing que use esa cadena exacta como cabecera competiría de facto contra InfoJobs y LinkedIn, no contra contenido educativo. La cadena «manual de operaciones de un restaurante» es, en cambio, **100% intención de problema/documento** y cero contaminación de empleo — es la mejor ancla de intención de todo el research, aunque su volumen (10/mes ES) sea bajo.

---

## §4. Propuesta title/H1/slug/description + FAQ

### Slug
1. **`manual-del-manager-de-restaurante`** (recomendado) — coincide con el nombre de trabajo del producto; el research no encontró ninguna cadena de alto volumen que lo desplace, así que no hay coste de SEO en mantenerlo. Empieza por `manual-`, cumple la convención del encargo.
2. `manual-de-operaciones-del-restaurante` — más alineado con la keyword de intención más limpia (§2.6, §3), pero renombra el producto lejos de «manager», que es como lo piensa John y como se referencia en el catálogo interno (agente «Gerente de Restaurante Pro AI» ya existe en la plataforma — ver §5).
3. `manual-del-gerente-de-restaurante` — máxima fidelidad al vocabulario español dominante en volumen (México 720/mes), pero hereda el ruido de empleo de esa cadena si algún día se optimiza el `<title>` a coincidencia exacta.

**Recomendación**: opción 1, y usar «operaciones» y «gerente/encargado» como sinónimos dentro del H1/description para capturar las tres variantes sin fragmentar el producto en tres landings.

### Title (2-3 opciones, ≤60 caracteres orientativo)
1. «Manual del Manager de Restaurante | Guía Operativa 2026» (58)
2. «Manual del Manager de Restaurante: Operaciones, Equipo y KPIs» (64, algo largo)
3. «Manual del Manager de Restaurante — Gerente, Encargado, Jefe de Sala» (70, cubre sinónimos pero excede longitud recomendada; usar solo si se prioriza cobertura de vocabulario sobre CTR)

### H1 (2-3 opciones)
1. «El Manual del Manager de Restaurante» (marca, como indica la regla de H1 hub/spoke del proyecto — nombre de producto, no keyword-stuffing)
2. «Manual del Manager de Restaurante: Operaciones, Personas y Números Bajo Control»
3. «El Manual Operativo para Gerentes y Encargados de Restaurante»

### Description (2-3 opciones, ~155 caracteres)
1. «Guía práctica para gerentes y encargados: checklists de apertura y cierre, cuadrantes, KPIs, protocolo de servicio y gestión de equipo. Pago único.» (152)
2. «El manual operativo que ningún curso te da: apertura, cierre, turnos, KPIs, reseñas y equipo de tu restaurante en un solo documento. Acceso vitalicio.» (155)
3. «Para quien ya gestiona un restaurante: plantillas de checklist, cuadrante de turnos, KPIs y protocolo de servicio listos para aplicar hoy mismo.» (147)

### Preguntas literales del PAA para la FAQ (18, agrupadas por bloque temático; todas verbatim de DataForSEO SERP)

**Puesto y jerarquía** (aclara la confusión detectada en 2 SERPs distintas — encargado #2 y administrador MX):
1. ¿Qué hace el encargado de un restaurante?
2. ¿Cuáles son los rangos en un restaurante?
3. ¿Cómo se llama el encargado del restaurante?
4. ¿Qué es lo que hace un administrador en un restaurante?
5. ¿Cómo se le llama al administrador de un restaurante?
6. ¿Cuáles son las 4 funciones de un gerente?

**Salario** (con la varianza sin explicar detectada en §2.11 — hueco de autoridad):
7. ¿Cuánto gana un gerente de restaurante?
8. ¿Cuánto gana un administrador de restaurantes?

**Operaciones y documentación** (el bloque de intención más limpia, §2.6):
9. ¿Cómo hacer un manual de procedimientos para un restaurante?
10. ¿Cuáles son las operaciones de un restaurante?
11. ¿Qué debe contener un manual de operaciones?
12. ¿Qué partes debe llevar un manual?

**Herramientas del día a día**:
13. ¿Cómo hacer un cuadrante de trabajo por turnos?
14. ¿Cuándo me tienen que entregar el cuadrante de trabajo? (legal — jornada)
15. ¿Cómo se calcula la rotación de personal?
16. ¿Qué porcentaje de rotación de personal es aceptable?
17. ¿Qué cosas necesito para abrir un restaurante? *(matizar: apertura de turno ≠ apertura de negocio — hueco detectado en §2.8)*

**Legal básico del manager** (sin prometer cobertura de los 17 convenios provinciales — solo lo estructural):
18. ¿Qué establecimientos están obligados a tener hoja de reclamaciones?

---

## §5. Contenidos propios del blog e interlinking

### Blog ES (`astro-site/src/content/blog/es/`) — coincidencias por grep de `gerente|manager|gestion|equipo|personal|turno|servicio|resena|caja|kpi|lider|encargado|checklist|briefing|rotacion`

| Post | Relevancia para el banner/enlace |
|---|---|
| `gerente-de-restaurante-20-areas-clave-donde-la-ia-te-puede-ayudar.md` | **Máxima** — mismo puesto exacto, título casi calcado al producto |
| `libreria-de-prompts-para-gerente-de-restaurante-pro-ai.md` | **Máxima** — es la librería de prompts del agente «Gerente de Restaurante Pro AI» ya existente en la plataforma; el manual y este post comparten público 100% |
| `gestion-personal-hosteleria-ia-reducir-rotacion.md` | Alta — cubre exactamente el hueco detectado en §2.10 (rotación sin ángulo hostelería en toda la SERP externa) |
| `rentabilidad-restaurante-kpis-metricas-2026.md` | Alta — KPIs, eje «finanzas» del manual |
| `30-hacks-con-inteligencia-artificial-para-mejorar-la-gestion-de-tu-restaurante.md` | Media — gestión general, buen punto de enlace saliente desde el manual hacia contenido IA |
| `inteligencia-artificial-rentabilidad-eficiencia-gestion-gastronomica.md` | Media — mismo eje finanzas/gestión |
| `ia-en-la-gestion-de-criticas-y-reputacion-de-restaurantes.md` | Media — cubre «reseñas negativas», uno de los huecos del Grupo C |
| `timlup-checklist-digital-tareas-recurrentes.md` | Media — checklist digital, tie-in de producto/herramienta hermana |
| `libreria-de-prompts-para-comida-de-personal.md` | Baja-media — eje «personas», tangente |

### Blog EN (`astro-site/src/content/blog/en/`)

| Post | Relevancia |
|---|---|
| `prompt-library-restaurant-manager.md` | **Máxima** — gemelo EN exacto de la librería ES; cuando el producto tenga versión inglesa nativa (regla de sesiones alternadas, ya prevista), este es el enlace de entrada natural |
| `ai-restaurant-management-software.md` | Alta |
| `best-restaurant-management-software-2026.md` | Alta |
| `restaurant-inventory-management-ai.md` | Media |
| `restaurant-waste-management-ai.md` | Media |

### Páginas `/usos/rol/…` (zona de casos de uso, SPA cross-root, `src/data/use-cases.ts` línea 166)

- **`/usos/rol/gerente-restaurante`** (EN: `/en/use-cases/role/restaurant-manager`) — la página de rol EXACTA para este público. Es la que ya trae 73 impresiones/1 clic en GSC (contexto de la tarea) y la que el manual debe enlazar en ambos sentidos: el `use-case` como entrada temática desde SEO de marca de agente, el manual como profundización pagada. **Es el enlace entrante/saliente más importante de toda la landing** — cierra el círculo agente gratuito → contenido → producto de pago que pide la regla de interenlazado del CLAUDE.md global.
- Otras páginas de rol candidatas a enlace secundario (no confirmadas por grep, revisar en `use-cases.ts` si hay roles de «jefe de sala», «encargado», «director»; el research no tuvo tiempo de listar el fichero completo de roles, ver §6).

**Recomendación de interenlazado**: banner del manual en los 2 posts de máxima relevancia (Gerente 20 áreas clave + Librería de prompts Gerente) + enlace contextual en los 3 de alta relevancia (rotación, KPIs, reputación/reseñas) + enlace bidireccional con `/usos/rol/gerente-restaurante`. Eso cubre las 5 alturas mínimas de interlinking sin inventar contenido nuevo.

---

## §6. Lo que NO se pudo medir

- **No se listó el fichero completo `src/data/use-cases.ts`** para confirmar si existen páginas de rol adicionales («encargado», «jefe de sala», «director de restaurante») más allá de la confirmada `gerente-restaurante` — solo se verificó esta por ser la que ya trae impresiones en GSC. Revisar antes de cerrar el interlinking definitivo.
- **No se corrió `serp` para Chile, Perú, Colombia ni Argentina** — todo el análisis de SERP (§2) es de España, más una única comprobación en México («administrador de restaurante»). Los volúmenes de esos 4 países (§1) están medidos, pero no se sabe si su SERP tiene la misma proporción empleo/formación/problema que España o México — con Argentina y Perú de volumen tan bajo, es dudoso que compense el gasto de más llamadas; con Colombia y Chile (140-260/mes en «administrador») sí sería razonable una pasada de SERP si se decide dar peso real a esos mercados en el copy.
- **No se verificó canibalización con posts propios existentes** vía GSC (`page,query`) — el encargo pedía research de SERP externa, no auditoría de posicionamiento propio; antes de publicar la landing conviene cruzar el slug definitivo y sus variantes contra Search Console, siguiendo el patrón de trampa ya documentado en `CLAUDE.md` («antes de ampliar, comprobar canibalización»).
- **No se probaron variantes con tilde/sin tilde de forma sistemática** (p. ej. «gestión» vs. «gestion») — DataForSEO normaliza internamente en la mayoría de los casos, pero no se verificó keyword por keyword si la tilde cambia el volumen devuelto, como sí se hizo puntualmente con «desempeño».
- **Ningún dato de este documento es una cifra inventada**: donde no hubo dato, se marca `None` o «no medido» explícitamente, tal como exige la regla del script.
